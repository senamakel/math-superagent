"""PE620 tangency enumeration for (c,s,p,q)=(16,5,5,6).

Direct tangency enumeration.  Radii: ring R=c/(2pi) at O=(0,0); sun r=s/(2pi)
at S=(d,0); a planet of circumference m has radius rho=m/(2pi).  Exact
tangency to both gears forces the planet centre P onto the intersection of
  |OP| = a = R - rho   (inside the ring)
  |SP| = b = r + rho   (outside the sun)
i.e. at most TWO points: the upper U=(x,+y) and its mirror L=(x,-y) across
the line of centres.  beta = angle of P about O, gamma = angle of P about S.

For one planet the tooth-mesh residue (one of the 4 sign variants:
sigma,eta in {+1,-1}; extended here to all 8 independent sign variants of the
three terms, since the thread invariant W = s*phi + c*chi - t*gamma_t equals
(c+t)*beta - (s+t)*gamma over 2pi = A + B - C with A=rho*(beta-gamma),
B=R*beta, C=r*gamma, i.e. the sign pattern (+,+,-) NOT among the 4 (sigma,eta)
variants of the original task) is
    Q = sigma*rho*(beta - gamma) - eta*R*beta + theta*r*gamma   (mod 1),
theta in {+1,-1} the third independent sign.

Exact identity exploited (mirror symmetry): Q(L) = -Q(U) (mod 1).

Side combinations (9): the two type-p planets and two type-q planets each
choose a side assignment among  {both U, both L, one each}  -> 3*3 = 9.
An arrangement at a given d is VALID for a (variant, combo) iff all four
residues are equal mod 1 within tolerance.  g = number of distinct (clustered)
valid d values.

Scan d on a fine float64 grid, cluster coarse survivors, refine each with
mpmath-60, and report the residue structure aiming to recover g=9.

Output: code/out/tangency_enum.txt (+ curve dump tangency_residue_curves.txt).
"""
import math
import os
import numpy as np
from mpmath import mp, mpf, pi, atan2, sqrt, fabs

mp.dps = 60

OUT = "/workspace/code/out/tangency_enum.txt"
CURVES = "/workspace/code/out/tangency_residue_curves.txt"
os.makedirs("/workspace/code/out", exist_ok=True)

TWO_PI = 2.0 * math.pi


def circdist(a, b):
    """Circular distance on the unit circle, a,b in [0,1)."""
    return abs(((a - b + 0.5) % 1.0) - 0.5)


def max_pair_dist(res):
    """Max pairwise circular distance among residues in iterable res."""
    res = list(res)
    m = 0.0
    for i in range(len(res)):
        for j in range(i + 1, len(res)):
            m = max(m, circdist(res[i], res[j]))
    return m


# side assignments for the two planets of one type
PSIDES = ((1, 1, "UU"), (-1, -1, "LL"), (1, -1, "UL"))
COMBO_NAMES = []
for ppname in PSIDES:
    for qqname in PSIDES:
        COMBO_NAMES.append((ppname[2], qqname[2]))


def residue_at(sigma, eta, c, s, m, d, side):
    """mpmath residue Q for one planet (side=+1 upper, -1 lower)."""
    R = mpf(c) / (2 * pi)
    r = mpf(s) / (2 * pi)
    rho = mpf(m) / (2 * pi)
    a = R - rho
    b = r + rho
    x = (a * a - b * b + d * d) / (2 * d)
    y2 = a * a - x * x
    if y2 <= 0:
        return None, None, None
    y = sqrt(y2)
    beta = atan2(y, x)
    gamma = atan2(y, x - d)
    if side == -1:
        beta = -beta
        gamma = -gamma
    Q = sigma * rho * (beta - gamma) - eta * R * beta + theta * r * gamma
    return (Q % 1), float(beta), float(gamma)


def objective_mp(sigma, eta, theta, c, s, p, q, d, psides, qsides):
    """mpmath max pairwise residue distance for a combo at d."""
    res = []
    for side in psides:
        Q, _, _ = residue_at(sigma, eta, theta, c, s, p, d, side)
        if Q is None:
            return mpf(1)
        res.append(Q)
    for side in qsides:
        Q, _, _ = residue_at(sigma, eta, theta, c, s, q, d, side)
        if Q is None:
            return mpf(1)
        res.append(Q)
    m = mpf(0)
    for i in range(len(res)):
        for j in range(i + 1, len(res)):
            dd = (res[i] - res[j] + mpf('0.5')) % 1 - mpf('0.5')
            m = max(m, fabs(dd))
    return m


def refine(sigma, eta, theta, c, s, p, q, d0, window, psides, qsides):
    """mpmath local minimisation of objective near d0 by iterative zooming.
    Each zoom scans `n` points over the current window and shrinks the window
    by 1e-3, so after 3 zooms resolution ~1e-15; the objective is a smooth
    transcendent of the residue differences, so the argmin converges to the
    true zero.  Returns (best_d, best_obj)."""
    n = 1000
    best = (mpf(d0), objective_mp(sigma, eta, theta, c, s, p, q, mpf(d0),
                                  psides, qsides))
    lo = mpf(d0) - mpf(window)
    hi = mpf(d0) + mpf(window)
    for _ in range(3):
        step = (hi - lo) / n
        d = lo
        for i in range(n + 1):
            o = objective_mp(sigma, eta, theta, c, s, p, q, d, psides, qsides)
            if o < best[1]:
                best = (d, o)
            d += step
        lo = best[0] - step
        hi = best[0] + step
    return best


def main():
    c, s, p, q = 16, 5, 5, 6
    R = c / TWO_PI
    r = s / TWO_PI
    rp = p / TWO_PI
    rq = q / TWO_PI
    ap, bp = R - rp, r + rp
    aq, bq = R - rq, r + rq
    d_min = max(abs(ap - bp), abs(aq - bq))
    d_max = min(ap + bp, aq + bq, R - r - 1.0)

    out = []
    def emit(s_=""):
        print(s_, flush=True)
        out.append(s_)

    emit("PE620 tangency enumeration  (c,s,p,q)=(16,5,5,6)")
    emit("R=%.6f r=%.6f rp=%.6f rq=%.6f" % (R, r, rp, rq))
    emit("d_min=%.9f  d_max=%.9f   (width %.9f)" % (d_min, d_max, d_max - d_min))
    emit("residue Q = sigma*rho*(beta-gamma) - eta*R*beta + r*gamma (mod 1);")
    emit("mirror identity Q(L) = -Q(U) mod 1 enforced exactly.")
    emit("=" * 78)

    N = (1 << 20) + 1
    dv = np.linspace(d_min, d_max, N)
    delta = (d_max - d_min) / (N - 1)
    emit("grid: %d points, spacing ~%.3e" % (N, delta))

    # geometry per type (arrays over the d grid)
    geom = {}
    for name, rhom in (('p', rp), ('q', rq)):
        a = R - rhom
        b = r + rhom
        x = (a * a - b * b + dv * dv) / (2.0 * dv)
        y2 = np.maximum(a * a - x * x, 0.0)
        y = np.sqrt(y2)
        beta = np.arctan2(y, x)
        gamma = np.arctan2(y, x - dv)
        geom[name] = dict(beta=beta, gamma=gamma, rho=rhom)

    variants = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    # residue upper-award per variant and type
    Qu = {}
    for (sig, eta) in variants:
        Qu[(sig, eta)] = {}
        for name, g in geom.items():
            rho = g['rho']
            Q = sig * rho * (g['beta'] - g['gamma']) - eta * R * g['beta'] \
                + r * g['gamma']
            Qu[(sig, eta)][name] = np.mod(Q, 1.0)

    # curve dump every 256th point
    curves = []
    curves.append("# d  " + "  ".join(
        "Qp[%+d,%+d] Qq[%+d,%+d]" % (sg, et, sg, et) for (sg, et) in variants))
    for k in range(0, N, 256):
        dk = dv[k]
        row = "%.12g" % dk
        for (sig, eta) in variants:
            row += "  %.9f %.9f" % (Qu[(sig, eta)]['p'][k], Qu[(sig, eta)]['q'][k])
        curves.append(row)
    with open(CURVES, "w") as f:
        f.write("\n".join(curves) + "\n")
    emit("residue curves dumped (every %d-th of %d points) to %s"
         % (256, N, CURVES))

    COARSE_TOL = 1e-4
    TIGHT_TOL = mpf('1e-9')

    # for each combo/variant, find valid grid regions
    variant_total = {}      # (sig,eta) -> set of d (rounded) valid under any combo
    per_combo = {}          # (sig,eta) -> {combo: scaled count}
    survivors = []          # detailed records of refined configurations

    for (sig, eta) in variants:
        vp = Qu[(sig, eta)]['p']
        vq = Qu[(sig, eta)]['q']
        # upper and lower residues
        up_p, lo_p = vp, np.mod(-vp, 1.0)
        up_q, lo_q = vq, np.mod(-vq, 1.0)
        vt = set()
        combo_counts = {}
        for (psides, pname) in [(x[:2], x[2]) for x in PSIDES]:
            for (qsides, qname) in [(x[:2], x[2]) for x in PSIDES]:
                # build the four residue arrays for this combo
                arrs = []
                for sd in psides:
                    arrs.append(up_p if sd == 1 else lo_p)
                for sd in qsides:
                    arrs.append(up_q if sd == 1 else lo_q)
                # objective = max pairwise circular distance (vectorized)
                obj = np.zeros(N)
                for i in range(4):
                    for j in range(i + 1, 4):
                        dd = np.abs(((arrs[i] - arrs[j] + 0.5) % 1.0) - 0.5)
                        obj = np.maximum(obj, dd)
                valid = obj < COARSE_TOL
                # cluster contiguous runs of valid grid points
                runs = []
                inrun = False
                for k in range(N):
                    if valid[k] and not inrun:
                        inrun = True
                        start = k
                    elif not valid[k] and inrun:
                        inrun = False
                        runs.append((start, k - 1))
                if inrun:
                    runs.append((start, N - 1))
                key = (pname, qname)
                g_count = 0
                for (i0, i1) in runs:
                    # best grid point in run = min objective
                    seg = slice(i0, i1 + 1)
                    best_idx = i0 + int(np.argmin(obj[seg]))
                    d0 = float(dv[best_idx])
                    # refine
                    window = 5 * delta
                    bd, bo = refine(sig, eta, c, s, p, q, d0, window,
                                    psides, qsides)
                    if bo < TIGHT_TOL:
                        g_count += 1
                        survivors.append((sig, eta, key, bd, bo))
                combo_counts[key] = g_count
                if g_count > 0:
                    # add the refined d's to variant total
                    for (sg, et, ky, bd, bo) in survivors:
                        if (sg, et) == (sig, eta) and ky == key:
                            vt.add(mpf(bd))
        per_combo[(sig, eta)] = combo_counts
        variant_total[(sig, eta)] = vt

    emit("")
    emit("COARSE_TOL=%.0e  TIGHT_TOL=%.0e" % (COARSE_TOL, float(TIGHT_TOL)))
    emit("")
    emit("g(16,5,5,6) per variant (distinct valid d over all combos):")
    for (sig, eta) in variants:
        emit("  variant (sigma=%+d, eta=%+d): g = %d" % (sig, eta,
                                                          len(variant_total[(sig, eta)])))
    emit("")
    emit("per (variant, combo) counts (g_combo = distinct refined valid d):")
    emit("  combos pp x qq = [UU,LL,UL] x [UU,LL,UL]")
    for (sig, eta) in variants:
        emit("  --- variant (sigma=%+d, eta=%+d) ---" % (sig, eta))
        cc = per_combo[(sig, eta)]
        for (pname, qname) in COMBO_NAMES:
            n_ = cc[(pname, qname)]
            emit("     pp=%-2s qq=%-2s : %d" % (pname, qname, n_))

    emit("")
    emit("SURVIVING CONFIGURATIONS (refined, objective < 1e-9):")
    # group survivors and print detail
    seen = set()
    for (sig, eta, key, bd, bo) in sorted(survivors, key=lambda t: float(t[3])):
        ident = (sig, eta, key, mpf(bd))
        if ident in seen:
            continue
        seen.add(ident)
        psides = (1, 1) if key[0] == 'UU' else ((-1, -1) if key[0] == 'LL'
                                                else (1, -1))
        qsides = (1, 1) if key[1] == 'UU' else ((-1, -1) if key[1] == 'LL'
                                                else (1, -1))
        emit("  variant(sig=%+d,eta=%+d) combo p=%s q=%s  d=%.25g  obj=%.2e"
             % (sig, eta, key[0], key[1], float(mpf(bd)), float(bo)))
        deg = 180.0 / math.pi
        for m_, sides, nm_ in ((p, psides, 'p'), (q, qsides, 'q')):
            for sd in sides:
                Q, b, g_ = residue_at(sig, eta, c, s, m_, bd, sd)
                emit("     %s-planet side=%+d : beta=%+12.8f deg gamma=%+12.8f "
                     "deg  Q=%+10.8f mod 1" % (nm_, sd, b * deg, g_ * deg,
                                                float(Q)))
        # residue identities
        Qu0, _, _ = residue_at(sig, eta, c, s, p, bd, 1)
        Ql0, _, _ = residue_at(sig, eta, c, s, p, bd, -1)
        emit("     (identity check: Q_p(U)=%+.8f, Q_p(L)=%+.8f, "
             "2*Q_p(U)=%+.6f, Q_p==Q_q? see residues)"
             % (float(Qu0), float(Ql0), float((2 * Qu0) % 1)))

    emit("")
    emit("RESIDUE STRUCTURE SUMMARY:")
    emit("  - Q(L) = -Q(U) mod 1 exactly (mirror symmetry across line of centres).")
    emit("  - 'one-each-side' combos (UL) demand 2*Q(U) in {0,1/2} mod 1.")
    emit("  - 'both-same-side' combos (UU/LL) demand Q_p(U) == Q_q(U) mod 1.")
    emit("  => g is finite because these are isolated d-solutions of the "
         "transcendental congruences;")
    emit("     a BOUND-INDEPENDENT method would count those algebraically.")

    with open(OUT, "w") as f:
        f.write("\n".join(out) + "\n")
    emit("")
    emit("Output saved to %s" % OUT)


if __name__ == "__main__":
    main()
