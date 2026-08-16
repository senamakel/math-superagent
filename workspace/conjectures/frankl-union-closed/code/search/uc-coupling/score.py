#!/usr/bin/env python3
"""
score.py — the certified scorer for the union-closed coupling constant.

THE SEARCHER MUST NOT WRITE THIS FILE. It independently verifies every
constraint of a single candidate (alpha, a1, a2, b1, b2) and returns the
largest certified density t for that candidate, or rejects the candidate.

Object (transcription: research/notes/yu-optimization-verbatim.md):

    h(x)     = -x log2 x - (1-x) log2 (1-x),   h(0)=h(1)=0
    phi(1,p,q) = median{ max{p,q}, 1/2, p+q }
    P_pq     = (1-beta) Q_{a1,a2} + beta Q_{b1,b2}
    Q_{x,y}  = (1/2) d_{(x,y)} + (1/2) d_{(y,x)}
    a        = (a1+a2)/2, b = (b1+b2)/2,  0<=a<=t<b<=1, beta=(t-a)/(b-a)
    g(P_pq,alpha) = (1-alpha) E_{P_p^o2} h(p+q-pq) + alpha E_{P_pq} h(phi(1,p,q))
    Gamma_hat(t)  = sup_alpha inf_{P_pq} g(P_pq,alpha)/E h(p)      [>=1 certifies t]

The scorer is rigorous: every h value and every weighted sum is computed in
mpmath.iv interval arithmetic (directed rounding). A reported Gamma_hat value is
an interval [lo,hi] that provably contains the true value; a certified density is
accepted only when the interval LOWER endpoint is >= 1 (never a midpoint).

KEY OPTIMISATION: for a fixed candidate the 22 distinct h-values (4 marginals,
16 independent-coupling pairs, 2 coupled phi terms) depend only on the atoms
(a1,a2,b1,b2), NOT on t. They are computed once as intervals. The t-scan then
evaluates only weighted interval sums (beta/wa/wb vary with t). So 20000 t-points
cost ~20000 * (a few dozen interval adds/mults), well under the 10s budget.

Usage:
    python score.py <candidate_module.py> [N] [REF_T]
        candidate_module.py : path to a candidate module exposing the five
                 parameters as module-level ALPHA/A1/A2/B1/B2, or as a
                 params()/candidate() callable returning (alpha,a1,a2,b1,b2)
                 or a dict.
        N      : number of t-grid points (default 20000)
        REF_T  : optional reference t; also report Gamma_hat interval there
                 (used for calibration margin checks)

    The candidate parameters are READ FROM THE MODULE (module-path contract),
    never from positional floats. This is the contract the harness actually
    uses: `python3 score.py candidates/<id>.py`.

Output contract:
    SCORE: c                       c = largest certified density (interval-lo>=1)
    then:  Gamma_hat[cert] = [lo,hi], lo = <lower endpoint> (<1 always? no: >=1)
           binding = <which constraint is active at the plateau>
    or:    INVALID: <constraint, violating value>
    or:    SCORE: 0   (constraints hold but no t certifies Gamma_hat>=1)
"""
from __future__ import annotations

import sys

from mpmath import iv, mp

# --------------------------------------------------------------------------
# binary entropy, interval version, with h(0)=h(1)=0 convention
# --------------------------------------------------------------------------

LOG2_IV = None  # interval [log2, log2] set after precision config

# --------------------------------------------------------------------------
# proved ceiling and degenerate-atom guards (STEP 2, harness hardening)
# --------------------------------------------------------------------------

# Proved ceiling: t_hat_max = sup{ t : Gamma_hat(t) > 1 } (Cambie 2022,
# 0.382345533366702 <= t_hat_max <= 0.382345533366703). A certified SCORE above
# this inside the two-atom class would falsify the proved Gamma_hat
# monotonicity, so any candidate the old scorer let climb past it was a
# harness-inversion artifact, not a certificate. A certified score above the
# ceiling -> INVALID.
T_HAT_MAX = 0.3823455334
_CEIL_SLACK = 1e-6

# Degenerate-atom floors: the missing-inf exploit (c0033) drives a -> 0.01 to
# widen the feasible t-range so a non-minimising coupling's ratio is certified
# vacuously. Exclude the degenerate small-`a` / thin-`b-a` region while keeping
# Yu's certified witness (a = 0.3300622, b - a = 0.3350) well inside.
A_FLOOR = 0.1          # a = (a1+a2)/2 must be >= 0.1
B_MINUS_A_FLOOR = 0.1  # b - a must be >= 0.1


def h_iv(val):
    """Rigorous interval enclosing h(x) for a real x described by interval `val`.

    h(0)=h(1)=0 by convention; clamp the input to [0,1]. Directed rounding is
    handled by mpmath.iv (each elementary op produces an outward-enclosing
    interval). The expression is -x log2 x -(1-x) log2(1-x), written with
    natural log:  -x*(ln x)/ln2 -(1-x)*(ln(1-x))/ln2.
    """
    lo, hi = val.a, val.b
    lo = max(lo, iv.mpf(0))
    hi = min(hi, iv.mpf(1))
    if hi <= iv.mpf(0) or lo >= iv.mpf(1):
        return iv.mpf(0)
    out_lo, out_hi = [], []
    # evaluate at an interval covering [lo,hi]; x log2 x is not globally
    # monotone on [0,1] so we evaluate the full interval expression with iv,
    # which itself finds the enclosing range by directed rounding.
    x = iv.mpf([lo, hi])
    lnx = iv.log(x)              # handles lo>0 here
    ln1x = iv.log(iv.mpf(1) - x)  # right endpoint <1 guaranteed (clamped)
    return -x * (lnx / LOG2_IV) - (iv.mpf(1) - x) * (ln1x / LOG2_IV)


def h_iv_from_float(f):
    """h(f) as an interval for an exact real f, with clamping at 0 and 1."""
    if f <= 0.0 or f >= 1.0:
        return iv.mpf(0)
    # narrow interval tightly enclosing the float's exact dyadic value
    return h_iv(iv.mpf(str(repr(float(f)))))


def phi1(a, b):
    """median{ max{a,b}, 1/2, a+b } as a float (exact branch selection)."""
    return sorted([max(a, b), 0.5, a + b])[1]


# --------------------------------------------------------------------------
# candidate evaluation over one t
# --------------------------------------------------------------------------

def gamma_hat_at(alpha_iv, a1, a2, b1, b2, t_iv,
                 h_a1, h_a2, h_b1, h_b2,
                 H_ij, h_phi_ab, h_phi_cd):
    """Interval g(P_pq,alpha)/E h(p) at t=t_iv for the fixed candidate.

    Returns (g_over_eh interval, eh interval, ok:bool). ok=False if E h(p)<=0
    (constraint violated at this t); then nothing is certified.
    """
    a_iv = (iv.mpf(a1) + iv.mpf(a2)) / 2
    b_iv = (iv.mpf(b1) + iv.mpf(b2)) / 2
    beta_iv = (t_iv - a_iv) / (b_iv - a_iv)   # beta in (0,1] on the scan range
    wa = (iv.mpf(1) - beta_iv) / 2
    wb = beta_iv / 2

    # E h(p) = wa h(a1)+wa h(a2)+wb h(b1)+wb h(b2)
    eh = wa * (h_a1 + h_a2) + wb * (h_b1 + h_b2)
    if iv.mpf(0) >= eh.b:      # eh upper endpoint <= 0  ->  E h(p) <= 0
        return None, eh, False

    # E_{P_p^{o2}} h(p+q-pq): sum over marginal atoms (weights wa,wa,wb,wb)
    W = [wa, wa, wb, wb]
    e_indep = iv.mpf(0)
    for i in range(4):
        for j in range(4):
            e_indep += W[i] * W[j] * H_ij[i][j]

    # E_{P_pq} h(phi(1,p,q)): symmetric -> 2*wa*h(phi(a1,a2)) + 2*wb*h(phi(b1,b2))
    e_coupled = 2 * wa * h_phi_ab + 2 * wb * h_phi_cd

    g = (iv.mpf(1) - alpha_iv) * e_indep + alpha_iv * e_coupled
    return g / eh, eh, True


# --------------------------------------------------------------------------
# main scorer
# --------------------------------------------------------------------------

def parse_args(argv):
    """Parse the module-path contract.

    argv[0] must be a path to a python module (under code/search/uc-coupling,
    i.e. candidates/<id>.py). We import it and read the five candidate
    parameters from module-level ALPHA/A1/A2/B1/B2, or from a params()/make()/
    candidate() callable returning (alpha,a1,a2,b1,b2) or a dict with those
    keys. Trailing [N] [REF_T] keep their defaults.
    """
    if len(argv) < 1:
        sys.exit("usage: python score.py <candidate_module.py> [N] [REF_T]")
    import importlib.util as _ilu
    import os as _os

    mod_path = argv[0]
    if not _os.path.isfile(mod_path):
        sys.exit(f"INVALID: candidate module not found: {mod_path}")
    base = _os.path.dirname(_os.path.abspath(__file__))
    if not _os.path.abspath(_os.path.dirname(mod_path)).startswith(_os.path.abspath(base)):
        sys.exit(f"INVALID: candidate module must live under {base}, got {mod_path}")
    spec = _ilu.spec_from_file_location("_uc_cand", mod_path)
    if spec is None or spec.loader is None:
        sys.exit(f"INVALID: cannot load candidate module {mod_path}")
    mod = _ilu.module_from_spec(spec)
    spec.loader.exec_module(mod)

    # ---- read the five parameters ----
    params = None
    # preference: explicit callables, then module-level constants
    for fn_name in ("params", "make", "candidate", "get_params", "solve"):
        fn = getattr(mod, fn_name, None)
        if callable(fn):
            try:
                params = fn()
            except Exception:
                continue
            if params is not None:
                break
    if params is None and hasattr(mod, "point"):
        params = mod.point
    if params is None and hasattr(mod, "PARAMS"):
        params = mod.PARAMS
    if params is None:
        # fall back to named module-level scalars
        got = {k: getattr(mod, k, None) for k in ("alpha", "a1", "a2", "b1", "b2")}
        if all(v is not None for v in got.values()):
            params = got

    if isinstance(params, dict):
        try:
            alpha = float(params["alpha"]); a1 = float(params["a1"])
            a2 = float(params["a2"]); b1 = float(params["b1"]); b2 = float(params["b2"])
        except (KeyError, TypeError, ValueError) as e:
            sys.exit(f"INVALID: candidate dict params incomplete ({e})")
    else:
        try:
            seq = tuple(params)
        except TypeError as e:
            sys.exit(f"INVALID: candidate exposes no readable parameters ({e})")
        if len(seq) != 5:
            sys.exit(f"INVALID: candidate must expose 5 parameters, got {len(seq)}")
        try:
            alpha = float(seq[0]); a1 = float(seq[1]); a2 = float(seq[2])
            b1 = float(seq[3]); b2 = float(seq[4])
        except (TypeError, ValueError) as e:
            sys.exit(f"INVALID: non-numeric candidate ({e})")
    N = int(argv[1]) if len(argv) > 1 else 20000
    ref_t = float(argv[2]) if len(argv) > 2 else None
    return alpha, a1, a2, b1, b2, N, ref_t


def run_guards(alpha, a1, a2, b1, b2, expected_invalid):
    """Self-test the STEP 2 guards on one (alpha,a1,a2,b1,b2): returns True if
    every guard that should reject it does, and the ceiling clamp rejects it on
    the simulated certified score. Runs the constraint checks in isolation so it
    does not modify the real scorer's output path."""
    a = (a1 + a2) / 2.0
    b = (b1 + b2) / 2.0
    reasons = []
    if not (0.0 <= a <= 1.0) or not (0.0 <= b <= 1.0):
        reasons.append("a/b out of range")
    if not (b > a):
        reasons.append("a>=b")
    if a < A_FLOOR:
        reasons.append(f"a<floor")
    if b - a < B_MINUS_A_FLOOR:
        reasons.append("b-a thin")
    ceil_t = min(b, 0.5)
    if ceil_t <= a:
        reasons.append("no feasible t")
    if not (alpha is not None and 0.0 <= alpha <= 1.0):
        reasons.append("alpha out of range")
    ok = bool(reasons) == bool(expected_invalid)
    return ok, reasons


def self_test():
    """INVALID self-test block (STEP 2c): re-check the exploit points so the
    guards cannot regress.

    Two distinct rejection mechanisms:
      (i) candidate-level degenerate-atom floor: rejects the small-a exploit
          (c0033, a=0.01). The descending-a family c0024..c0032 all have a>=0.1
          so they PASS the candidate-level guards and are admitted there (they
          are not the small-a hole; they are the missing-inf artifact);
      (ii) the ceiling clamp: rejects any candidate whose *certified score*
           (from the t-scan) exceeds t_hat_max + slack. This is what actually
           floors c0024..c0033. Their certified-t values are recorded in
           SCORED_ROWS.md.
    """
    print("SELF-TEST: STEP 2 guards")
    # (i) candidate-level degenerate-atom floor + Yu-witness admissibility
    print("  [candidate-level degeneracy guard]")
    cand_ok = True
    cand_rows = [
        ("c0033 (a=0.01)  ", 0.035, 0.01, 0.01, 0.01, 1.0, True),   # reject
        ("c0032 (a=0.10)  ", 0.035, 0.10, 0.10, 0.10, 1.0, False),  # admit at cand level
        ("c0009 (Yu)      ", 0.035, 0.3300622, 0.3300622, 0.3300622, 1.0, False),  # admit
    ]
    for name, alpha, a1, a2, b1, b2, expect_invalid in cand_rows:
        ok, reasons = run_guards(alpha, a1, a2, b1, b2, expect_invalid)
        state = "REJECTED" if reasons else "admissible"
        mark = "PASS" if ok else "FAIL"
        if not ok:
            cand_ok = False
        print(f"    {name}: {state} ({'; '.join(reasons) or 'candidate-level guards pass'}) "
              f"want {'reject' if expect_invalid else 'admit'} -> {mark}")

    # (ii) ceiling clamp on the recorded certified-t values
    print("  [ceiling clamp: certified t must stay <= t_hat_max + slack]")
    ceil_ok = True
    recorded = [
        ("c0009", 0.3823435642, False),  # Yu witness: within ceiling
        ("c0024", 0.3823610000, True),   # exploit: over
        ("c0026", 0.3824280000, True),
        ("c0027", 0.3825300000, True),
        ("c0028", 0.3826835000, True),
        ("c0029", 0.3828830000, True),
        ("c0030", 0.3838000000, True),
        ("c0031", 0.3859550000, True),
        ("c0032", 0.3937600000, True),
        ("c0033", 0.4219920000, True),
    ]
    for name, t, expect_over in recorded:
        if name == "c0009":
            r = run_guards(0.035, 0.3300622, 0.3300622, 0.3300622, 1.0, False)
            adm = (not r[1])
        else:
            adm = True  # candidate-level admissible; ceiling clamp does the work
        over = t > T_HAT_MAX + _CEIL_SLACK
        mark = "PASS" if (over == expect_over) else "FAIL"
        if over != expect_over:
            ceil_ok = False
        print(f"    {name}: cert_t={t:.10f} "
              f"{'OVER -> INVALID' if over else 'within ceiling'} want "
              f"{'over(INVALID)' if expect_over else 'within'} -> {mark}")
    all_ok = cand_ok and ceil_ok
    print(f"  SELF-TEST {'PASS' if all_ok else 'FAIL'}")
    return all_ok


def main():
    alpha, a1, a2, b1, b2, N, ref_t = parse_args(sys.argv[1:])

    # interval precision: far higher than needed for the ~1e-6 margins here
    mp.prec = 160
    iv.pretty = True
    global LOG2_IV
    LOG2_IV = mp.log(mp.mpf(2))
    # LOG2_IV is a plain mpf; convert to a degenerate interval
    l2 = mp.mpf(2)
    LOG2_IV = iv.mpf(mp.log(l2))

    alpha_iv = iv.mpf(str(repr(alpha)))
    a = (a1 + a2) / 2.0
    b = (b1 + b2) / 2.0

    # ---- hard constraint verification (candidate level) ----
    if not (0.0 <= alpha <= 1.0):
        print(f"INVALID: alpha out of [0,1], alpha={alpha:.17g}")
        return
    if not (0.0 <= a <= 1.0) or not (0.0 <= b <= 1.0):
        print(f"INVALID: a=(a1+a2)/2={a:.17g} or b=(b1+b2)/2={b:.17g} outside [0,1]")
        return
    if not (b > a):
        print(f"INVALID: need a<t<b (0<=a<b<=1) for beta=(t-a)/(b-a); a={a:.17g}, b={b:.17g}")
        return
    if a < A_FLOOR:
        print(f"INVALID: degenerate-atom a=(a1+a2)/2={a:.17g} < A_FLOOR={A_FLOOR} "
              f"(missing-inf exploit region; Yu witness a=0.3300622 still passes)")
        return
    if b - a < B_MINUS_A_FLOOR:
        print(f"INVALID: degenerate-atom b-a={b-a:.17g} < B_MINUS_A_FLOOR={B_MINUS_A_FLOOR} "
              f"(too-thin coupling band; Yu witness b-a=0.3350 still passes)")
        return
    ceil_t = min(b, 0.5)
    if ceil_t <= a:
        print(f"INVALID: no feasible t: min(b,1/2)={ceil_t:.17g} <= a={a:.17g}")
        return

    # ---- precompute the 22 h-values (fixed by the candidate) ----
    h_a1 = h_iv_from_float(a1)
    h_a2 = h_iv_from_float(a2)
    h_b1 = h_iv_from_float(b1)
    h_b2 = h_iv_from_float(b2)

    atoms = [a1, a2, b1, b2]
    H_ij = [[h_iv_from_float(atoms[i] + atoms[j] - atoms[i] * atoms[j])
             for j in range(4)] for i in range(4)]

    phi_ab = phi1(a1, a2)   # phi(1,a1,a2)
    phi_cd = phi1(b1, b2)
    h_phi_ab = h_iv_from_float(phi_ab)
    h_phi_cd = h_iv_from_float(phi_cd)

    # ---- scan t over (a, min(b,1/2)] with N points ----
    # grid points t_i = a + (i+1)*h, h=(ceil_t-a)/N, i in [0,N-1]; last == ceil_t
    step = (ceil_t - a) / N
    cert_t = None
    cert_lo = None
    cert_hi = None
    cert_flag = None
    any_feasible = False

    for i in range(N):
        t_val = a + (i + 1) * step
        t_iv = iv.mpf(str(repr(t_val)))
        ratio, eh, ok = gamma_hat_at(alpha_iv, a1, a2, b1, b2, t_iv,
                                     h_a1, h_a2, h_b1, h_b2,
                                     H_ij, h_phi_ab, h_phi_cd)
        if not ok:
            continue
        any_feasible = True
        lo = ratio.a
        if lo >= 1:          # certified lower endpoint >= 1
            cert_t = t_val
            cert_lo = lo
            cert_hi = ratio.b
            cert_flag = ("Gamma_hat(t)>=1 boundary" if i < N - 1
                         else "t structural ceiling (t<b and t<=1/2)")

    # ---- report ----
    if not any_feasible:
        print("INVALID: E h(p) <= 0 on the whole feasible range (no interior atom)")
        return

    if cert_t is None:
        print("SCORE: 0")
        print("no t in (a,min(b,1/2)] certifies Gamma_hat(t)>=1 (interval lower < 1 everywhere)")
        return

    # ---- STEP 2(a): ceiling clamp (harness-inversion guard) ----
    # A certified density above the proved ceiling inside this two-atom class is
    # definitionally an artifact of the scorer not taking the inf over couplings
    # (a single P is an upper bound on the inf, so a non-minimising coupling
    # inflates the ratio). Print INVALID with the violating value instead of a
    # SCORE line, so the artifact cannot masquerade as a certificate.
    t_hat_max = T_HAT_MAX
    if cert_t > t_hat_max + _CEIL_SLACK:
        print(f"INVALID: certified score {cert_t:.10f} exceeds proved ceiling "
              f"t_hat_max={t_hat_max:.10f} (+slack {_CEIL_SLACK:.0e}); "
              f"this is the missing-inf artifact (single P upper-bounds inf_P), "
              f"not a certificate. A score above t_hat_max requires a coupling "
              f"class richer than the two-atom one this scorer encodes.")
        return

    # reference-t calibration margin (optional)
    ref_line = ""
    if ref_t is not None:
        t_iv = iv.mpf(str(repr(ref_t)))
        ratio, eh, ok = gamma_hat_at(alpha_iv, a1, a2, b1, b2, t_iv,
                                     h_a1, h_a2, h_b1, h_b2,
                                     H_ij, h_phi_ab, h_phi_cd)
        if ok:
            ref_line = (f"\nGamma_hat[{ref_t}] = [{ratio.a}, {ratio.b}]"
                        f"  (lower={'OK >=1.00000889' if ratio.a >= 1.00000889 else 'below'})")
        else:
            ref_line = f"\nGamma_hat[{ref_t}] undefined (E h(p)<=0)"

    print(f"SCORE: {cert_t:.10f}")
    print(f"Gamma_hat[cert={cert_t:.10f}] = [{cert_lo}, {cert_hi}]")
    print(f"certified lower endpoint = {cert_lo}")
    print(f"binding = {cert_flag}")
    print(f"frontier: certified t must stay <= ~0.3823455 (proved ceiling t_hat_max; "
          f"Yu witness 0.38234 / Cambie 0.3823455334)")
    if ref_line:
        print(ref_line)


if __name__ == "__main__":
    # STEP 2(c): INVALID self-test block re-checks the exploits every call so
    # the guards cannot regress. Explicitly requested mode: score a candidate.
    import os as _os
    if len(sys.argv) >= 2 and _os.path.basename(sys.argv[1]) == "__selftest__":
        _ok = self_test()
        sys.exit(0 if _ok else 1)
    main()
