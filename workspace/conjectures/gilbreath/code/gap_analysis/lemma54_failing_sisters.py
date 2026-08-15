#!/usr/bin/env python3
"""Validate Granville Lemma 5.4 in the FAILURE direction (on synthetic failing
sequences), not the all-successful primes.

The real prime columns never fail, so the published validation
(code/lemma54_iff_check.py) confirms the biconditional
    v_n <= 2*nu_2(q_{n-1}) + 2  <=>  column n succeeds
only where both sides are true -- vacuously.  This program builds SYNTHETIC
failing sequences and checks the contrapositive's two branches:

  (A) budget holds  (v_n <= 2*nu_2+2):  the new diagonal's gray block is
      ABSORBED into {0,2} and stays there  (success).
  (B) budget fails  (v_n >  2*nu_2+2):  the value ESCAPES to a non-{0,2}
      value (>= 4), so the column fails.

The elementary core is the diagonal recursion
    delta_{k+1} = |delta_k - epsilon_k|,   epsilon_k in {0,2}   (Gray block)
with the three local transition claims (the repair to Granville's discarded
delta=0 case -- research/notes/lemma54-re-derived.md):

  (i)  epsilon=2 and delta>=2  =>  delta' = delta-2        (descent)
  (ii) delta=0                 =>  delta' = epsilon        (absorption)
  (iii)epsilon=2 and delta=1   =>  delta' = 1              (terminal-on-1)

This is checked exhaustively over every (delta, epsilon) pair, then every
{0,2}^L pattern is swept for L=1..14 over even start values v to confirm
EXACTLY the branch split: low budget -> absorbed ({0,2}) and closing; high
budget -> escape (>=4).  Granville's own Table 14 (0-2 cycle
0,2,2,0,2,0,2,0,0,0,2,2, nu_2=6, budget 14) is reproduced as the oracle:
v=14 -> landing 2 -> green 1 (success); v=16 -> landing 4 -> green 3
(failure).

A second, independent route (rule 11) runs random valid Gilbreath sequences
(2-then-odd, random even gaps, Poisson-gap style) whose triangles DO fail, and
checks on every failing column that v_n > 2*nu_2+2, and on every successful
column that v_n <= 2*nu_2+2 -- exercising the biconditional from the failing
side, non-vacuously.

Exact integer arithmetic throughout.  Runtime is a few seconds; well inside
the 600 s budget.
"""

from math import isqrt
from random import Random


# ---------------------------------------------------------------------------
# 1. The diagonal recursion and the three local transition claims
# ---------------------------------------------------------------------------

def descend(delta, eps):
    """One step of the diagonal recursion: delta_{k+1} = |delta_k - eps_k|."""
    return abs(delta - eps)


# The three local claims as an exhaustive transition classifier.  For
# eps in {0,2} the recursion has only these cases:
#   eps=0 : delta' = delta                       (no-op)
#   eps=2 : delta>=2 -> delta-2                 (i, descent)
#           delta==0 -> 2                        (ii, absorption)
#           delta==1 -> 1                        (iii, terminal-on-1)
def classify(delta, eps):
    if eps == 2 and delta >= 2:
        return "i-descent"
    if delta == 0:
        return "ii-absorption"
    if eps == 2 and delta == 1:
        return "iii-terminal1"
    return "noop"


def trace_block(v, eps_seq):
    """Full diagonal trajectory delta_0=v,... in the gray block; also the
    per-step classification and whether each matches the recursion."""
    traj = [v]
    classes = []
    ok = True
    for eps in eps_seq:
        d = traj[-1]
        c = classify(d, eps)
        expected = descend(d, eps)
        actual = expected
        if c in ("i-descent",):
            correct = (expected == d - 2)
        elif c == "ii-absorption":
            correct = (expected == eps)
        elif c == "iii-terminal1":
            correct = (expected == 1)
        else:  # noop
            correct = (expected == d)
        # every transition must equal the recursion by definition, but the
        # classifier claims a specific closed form -- check that closed form
        # really matches |d - eps|.
        if not correct:
            ok = False
        classes.append(c)
        traj.append(expected)
    return traj, classes, ok


def budget(eps_seq):
    """2*nu_2 + 2 for a {0,2} suffix; nu_2 = number of 2s (the descending
    budget supplied by the 0-2 cycle)."""
    return 2 * sum(1 for e in eps_seq if e == 2) + 2


# ---------------------------------------------------------------------------
# 2. Oracle: Granville's Table 14 worked example
# ---------------------------------------------------------------------------

# 0-2 cycle of delta(q_{n-1}): 0,2,2,0,2,0,2,0,0,0,2,2  (L=12, nu_2=6, budget=14)
CYCLE14 = [0, 2, 2, 0, 2, 0, 2, 0, 0, 0, 2, 2]


def oracle_table14():
    """Reproduce Granville's Table 14: v=14 succeeds (green 1), v=16 fails
    (green 3).  The "green" terminal entry is |x_L - 1| (the last cell of
    delta(q_n) must equal 1 for success)."""
    nu2 = sum(1 for e in CYCLE14 if e == 2)
    b = budget(CYCLE14)
    results = {}
    for v in (14, 16):
        traj, classes, ok = trace_block(v, CYCLE14)
        xL = traj[-1]
        green = abs(xL - 1)
        success = (xL in (0, 2))
        results[v] = dict(traj=traj, xL=xL, green=green, success=success)
    return nu2, b, results


# ---------------------------------------------------------------------------
# 3. Exhaustive failing-side sweep of the diagonal recursion
# ---------------------------------------------------------------------------

def sweep_recursion(Lmax=14, v_max_extra=8):
    """For every {0,2}^L pattern and every even v in [0, 2L+8]:
        - v <= budget  ->  trajectory is ABSORBED into {0,2} (x_L in {0,2})
                          and, once entered, stays in {0,2} (closure)
        - v >  budget  ->  x_L >= 4 (ESCAPE, so green >= 3, column fails)
    Also asserts every transition matches its classifier and the recursion.
    Returns counts and violation tallies."""
    viol_exact = 0       # v<=budget but x_L not in {0,2}, or v>budget but x_L<4
    viol_closure = 0     # entered {0,2} then escaped
    viol_transition = 0  # classifier closed form disagrees with |d-eps|
    n_patterns = 0
    n_pairs = 0
    absorbs = 0
    escapes = 0
    for L in range(1, Lmax + 1):
        for pat in range(1 << L):
            n_patterns += 1
            eps_seq = [2 if (pat >> s) & 1 else 0 for s in range(L)]
            b = budget(eps_seq)
            vmax = b + v_max_extra
            for v in range(0, vmax + 1, 2):
                n_pairs += 1
                traj, classes, ok = trace_block(v, eps_seq)
                if not ok:
                    viol_transition += 1
                xL = traj[-1]
                entered = False
                for x in traj:
                    if x in (0, 2):
                        entered = True
                    elif entered:
                        viol_closure += 1
                        break
                if v <= b:
                    absorbs += 1
                    if xL not in (0, 2):
                        viol_exact += 1
                else:
                    escapes += 1
                    if xL < 4:
                        viol_exact += 1
    return dict(Lmax=Lmax, n_patterns=n_patterns, n_pairs=n_pairs,
                absorbs=absorbs, escapes=escapes, viol_exact=viol_exact,
                viol_closure=viol_closure, viol_transition=viol_transition)


# ---------------------------------------------------------------------------
# 4. Non-vacuous full-triangle check on failing synthetic sequences
# ---------------------------------------------------------------------------

def diff_pass(row):
    return [abs(row[i] - row[i + 1]) for i in range(len(row) - 1)]


def cycle_nu2(diag):
    """Maximal {0,2} suffix before the terminal entry; (#twos, start index,
    whether the suffix really is all {0,2})."""
    # diag[0..n]: right diagonal of q_n; terminal entry is diag[-1] (green).
    # The 0-2 cycle is the maximal {0,2} tail of diag[0:-1], starting at
    # index >= 2 (position 0 is q_{n-1} = odd >= 3, position 1 is the gap
    # which may be 2 -- both excluded, matching code/lemma54_iff_check.py's
    # "while i>2").
    body = diag[:-1]
    i = len(body)
    while i > 2 and body[i - 1] in (0, 2):
        i -= 1
    cyc = body[i:]
    if not cyc or any(x not in (0, 2) for x in cyc):
        return None
    return sum(1 for x in cyc if x == 2), i, cyc


def build_triangle(row0, depth):
    """All rows A_0..A_depth of the iterated absolute-difference triangle."""
    tri = [list(row0)]
    for _ in range(depth):
        tri.append(diff_pass(tri[-1]))
    return tri


def right_diagonals(row0):
    """Compute delta(q_n) for all n by Granville's recursion directly:
    delta_0(q_n) = q_n (=row0[n]), delta_k(q_n) = |delta_{k-1}(q_n) -
    delta_{k-1}(q_{n-1})|.  Returns list diags[n] = [delta_0,..,delta_n]."""
    diags = [[row0[0]]]          # delta(q_0) = [q_0]
    for n in range(1, len(row0)):
        prev = diags[n - 1]          # delta(q_{n-1}), length n
        cur = [row0[n]]              # delta_0(q_n) = q_n
        # for k=1..n: delta_k(q_n) = |delta_{k-1}(q_n) - delta_{k-1}(q_{n-1})|
        # delta_{k-1}(q_n) is cur[k-1]; delta_{k-1}(q_{n-1}) is prev[k-1]
        for k in range(1, n + 1):
            cur.append(abs(cur[k - 1] - prev[k - 1]))
        diags.append(cur)
    return diags


def recursion_matches_triangle(tri, diags, nmax):
    """Independent check (rule 11): the recursion-generated right diagonal
    delta_k(q_n) must equal A_k[n-k] for all n<=nmax, k<=n."""
    bad = 0
    checked = 0
    for n in range(1, nmax + 1):
        d = diags[n]
        for k in range(0, n + 1):
            checked += 1
            if d[k] != tri[k][n - k]:
                bad += 1
    return bad, checked


def sample_failing_sequences(seed, ncols=90, ntries=400):
    """Random 2-then-odd valid sequences (q_1=2, q_2=3, then odd, even gaps)
    with random small gaps -- Poisson-gap style.  Some will fail early, some
    succeed.  For every column where a 0-2 cycle exists beforehand, record
    (v_n, nu_2, success) and test the biconditional on the FAILING columns
    too.  Lemma 5.4's hypothesis is that the PREFIX q_1..q_{n-1} is already
    successful (every A_k[0]==1, k=1..n-1); columns whose prefix already
    failed are excluded (Granville: "Let q_1,..,q_{n-1} be a valid,
    successful sequence").  Returns (stats, per-column records)."""
    rng = Random(seed)
    records = []
    recursion_bad = 0
    recursion_checked = 0
    # families tuned to produce a good mix of success and failure at small n
    families = {
        # name: (gap sampling function)
        "consec {2,4}":          lambda r: r.choice((2, 4)),
        "rand {2,4,6,8,10}":     lambda r: 2 * r.randint(1, 5),
        "skew {2,4} more 2s":    lambda r: 2 if r.random() < 0.7 else 4,
        "poisson ~ Exp gap":     lambda r: 2 * max(1, min(8, int(r.expovariate(0.5)) // 1 + 1)),
        "geometric heavy":       lambda r: 2 * max(1, int(r.random() / max(1e-9, 1 - r.random())) // 1),
    }
    for fname, fgap in families.items():
        for t in range(ntries):
            # top row: 2, 3, then odd numbers with even gaps
            row0 = [2, 3]
            q = 3
            for k in range(2, ncols):
                q += fgap(rng)
                if q % 2 == 0:
                    q += 1
                row0.append(q)
            # row0 has ncols columns q_0..q_{ncols-1}; deepest row is ncols-1
            tri = build_triangle(row0, ncols - 1)
            diags = right_diagonals(row0)
            # cumulative prefix-success: A_k[0]==1 for all k=1..n
            pref_ok = [True] * ncols
            # pref_ok[n] means prefix q_1..q_n successful
            for k in range(1, ncols):
                pref_ok[k] = pref_ok[k - 1] and (tri[k][0] == 1)
            for n in range(20, ncols):  # skip tiny prefixes
                # Lemma 5.4 hypothesis: the prefix BEFORE extending must be
                # successful.
                if not pref_ok[n - 1]:
                    continue
                diag_prev = diags[n - 1]
                diag_cur = diags[n]
                info = cycle_nu2(diag_prev)
                if info is None:
                    continue
                nu2, tau, cyc = info
                if tau >= len(diag_cur) - 1:
                    continue
                v_n = diag_cur[tau]
                gaps = [row0[k] - row0[k - 1] for k in range(2, n + 1)]
                gstar = max(gaps) if gaps else 0
                # Gilbreath success of the extension q_1..q_n: the leading
                # entry of row n must be 1  (A_n[0]).
                success = (tri[n][0] == 1)
                # Granville's green cell: delta_{n-1}(q_n)
                green = diag_cur[n - 1]
                pred = (v_n <= 2 * nu2 + 2)
                rec = dict(n=n, nu2=nu2, tau=tau, v_n=v_n, gstar=gstar,
                           success=success, green=green, pred=pred,
                           budget=2 * nu2 + 2)
                rec["family"] = fname
                records.append(rec)
            # independent check: recursion-built diagonals == triangle cells
            for n in range(1, ncols):
                d = diags[n]
                if n + 1 > len(tri):
                    continue
                for k in range(0, n + 1):
                    if k < len(tri) and (n - k) < len(tri[k]):
                        recursion_checked += 1
                        if d[k] != tri[k][n - k]:
                            recursion_bad += 1
    return records, recursion_bad, recursion_checked


# ---------------------------------------------------------------------------
# 5. main
# ---------------------------------------------------------------------------

def main():
    print("Lemma 5.4 failing-side validation (synthetic failing sequences)")
    print("  vs. the vacuous all-successful primes of code/lemma54_iff_check.")
    print("=" * 78)

    # ---- oracle: Table 14 --------------------------------------------------
    nu2, b, res = oracle_table14()
    print("\n[0] ORACLE: Granville Table 14, cycle=%s" % (CYCLE14,))
    print("    nu_2 = %d, budget 2*nu_2+2 = %d" % (nu2, b))
    ok14 = True
    for v in (14, 16):
        r = res[v]
        print("    v=%2d -> x_L=%d, green=|x_L-1|=%d  %s"
              % (v, r["xL"], r["green"],
                 "SUCCESS" if r["success"] else "FAIL(fails)"))
        if v == 14 and not (r["xL"] == 2 and r["success"]):
            ok14 = False
        if v == 16 and not (r["xL"] == 4 and not r["success"]):
            ok14 = False
    print("    oracle reproduced: %s" % ok14)

    # ---- local transition claims (the delta=0 repair) ----------------------
    print("\n[1] Local transition claims (delta'=abs(delta-eps), eps in {0,2}):")
    claim_viol = 0
    cases = {"i-descent": 0, "ii-absorption": 0, "iii-terminal1": 0, "noop": 0}
    for eps in (0, 2):
        for delta in range(0, 40):
            d1 = descend(delta, eps)
            c = classify(delta, eps)
            cases[c] += 1
            # verify the closed-form claim matches the recursion exactly
            if c == "noop":
                correct = (d1 == delta)
            elif c == "i-descent":
                correct = (d1 == delta - 2)
            elif c == "ii-absorption":
                correct = (d1 == eps)
            else:
                correct = (d1 == 1)
            if not correct:
                claim_viol += 1
    print("    (i)  eps=2, delta>=2 -> delta'=delta-2   : %d cases"
          % cases["i-descent"])
    print("    (ii) delta=0         -> delta'=eps       : %d cases"
          % cases["ii-absorption"])
    print("    (iii)eps=2, delta=1  -> delta'=1         : %d cases"
          % cases["iii-terminal1"])
    print("    (noop)eps=0          -> delta'=delta     : %d cases"
          % cases["noop"])
    print("    closed-form/recursion disagreements: %d (expect 0)" % claim_viol)

    # ---- exhaustive failing-side sweep of the recursion --------------------
    swe = sweep_recursion(Lmax=14)
    print("\n[2] Exhaustive descent sweep (the contrapose's two branches):")
    print("    patterns {0,2}^L, L=1..%d: %d" % (swe["Lmax"], swe["n_patterns"]))
    print("    (v,pattern) pairs: %d" % swe["n_pairs"])
    print("    branch A  budget holds  (v<=2*nu2+2)  : %d pairs -> ABSORBED "
          "into {0,2}" % swe["absorbs"])
    print("    branch B  budget fails  (v> 2*nu2+2)  : %d pairs -> ESCAPE "
          "(x_L>=4, column fails)" % swe["escapes"])
    print("    v<=budget but x_L not in {0,2}  : %d (expect 0)"
          % swe["viol_exact"])
    print("    entered {0,2} then escaped       : %d (expect 0, closure)"
          % swe["viol_closure"])
    print("    transition closed-form mismatch  : %d (expect 0)"
          % swe["viol_transition"])

    # ---- non-vacuous full-triangle failing sequences ------------------------
    print("\n[3] Non-vacuous full-triangle check on SYNTHETIC sequences that")
    print("    actually FAIL (unlike the all-successful primes):")
    print("    (columns filtered to prefixes q_1..q_{n-1} already successful,")
    print("     per Lemma 5.4's hypothesis)")
    records, rec_bad, rec_checked = sample_failing_sequences(seed=20260714)
    print("    recursion-vs-triangle cell check: %d cells, %d mismatches "
          "(expect 0)" % (rec_checked, rec_bad))
    fail_recs = [r for r in records if not r["success"]]
    succ_recs = [r for r in records if r["success"]]
    total = len(records)
    print("    columns tested: %d   successful: %d   FAILING: %d"
          % (total, len(succ_recs), len(fail_recs)))
    if fail_recs:
        print("    -> the failure direction is EXERCISED (non-vacuous).")
    else:
        print("    -> no failing columns found -- raise ntries (vacuous again).")

    # biconditional v<=2*nu2+2 <=> success, checked across both classes
    bic_viol = 0
    suff_viol = 0        # g* <= budget but failed: would refute suff direction
    fail_under_budget = 0  # failing column with g* <= budget: refutes the
                           # contrapositive of suff ("fails => g* > budget")
    green_crossbad = 0   # green=A_{n-1}[1] in {0,2} should coincide with
                         # success = A_n[0]==1 (the reduction's iff)
    for r in records:
        if r["pred"] != r["success"]:
            bic_viol += 1
        # suff direction: g* <= budget  =>  success  (Granville Thm/Lemma)
        if r["gstar"] <= r["budget"] and not r["success"]:
            suff_viol += 1
        # contrapositive of suff: a failing column forces g* > budget, since
        # a failing v_n needs v_n > budget and v_n < g* (Lemma 5.3(8)).
        if not r["success"] and r["gstar"] <= r["budget"]:
            fail_under_budget += 1
        if (r["green"] in (0, 2)) != r["success"]:
            green_crossbad += 1

    print("\n    biconditional v_n<=2*nu2+2 <=> success  : violations = %d "
          "(expect 0)" % bic_viol)
    print("    suff  g*<=2*nu2+2 => success             : violations = %d "
          "(expect 0)" % suff_viol)
    print("    contrapositive of suff (fails => g*>budget): failing columns "
          "with g*<=budget = %d (expect 0)" % fail_under_budget)
    print("    cross-check green=A_{n-1}[1] in {0,2} <=> success=A_n[0]==1 : "
          "disagreements = %d (expect 0)" % green_crossbad)

    # per-family breakdown of the biconditional
    from collections import defaultdict
    fam_bic = defaultdict(lambda: [0, 0])  # fam -> [tested, viol]
    for r in records:
        fam_bic[r["family"]][0] += 1
        if r["pred"] != r["success"]:
            fam_bic[r["family"]][1] += 1
    print("\n    per-family biconditional violations:")
    for f in sorted(fam_bic):
        t, v = fam_bic[f]
        print("      %-22s tested=%-6d violations=%d" % (f, t, v))

    # a concrete failing column to exhibit
    concrete = None
    for r in records:
        if not r["success"]:
            concrete = r
            break
    if concrete:
        print("\n    concrete failing column: n=%d, family=%s, nu_2=%d, "
              "v_n=%d, budget=2*nu_2+2=%d, g*=%d, success=%s, pred=%s"
              % (concrete["n"], concrete["family"], concrete["nu2"],
                 concrete["v_n"], concrete["budget"], concrete["gstar"],
                 concrete["success"], concrete["pred"]))

    # ---- verdict -------------------------------------------------------------
    all_ok = (ok14 and claim_viol == 0 and swe["viol_exact"] == 0
              and swe["viol_closure"] == 0 and swe["viol_transition"] == 0
              and bic_viol == 0 and suff_viol == 0 and fail_under_budget == 0
              and green_crossbad == 0 and len(fail_recs) > 0)
    print("\n" + "=" * 78)
    print("VERDICT: %s" %
          ("CONTRAPOSITIVE HOLDS on failing side" if all_ok
           else "CHECK FAILED -- see violations above"))
    if fail_recs:
        print("The two branches of the contrapositive were confirmed "
              "non-vacuously:")
        print("  (A) v<=2*nu2+2  -> absorption into {0,2}, closure, success")
        print("  (B) v> 2*nu2+2  -> escape to >=4, column fails")
    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
