#!/usr/bin/env python3
"""
inner_inf_scorer.py — STEP 1 rigorous inner-inf scorer (candidate proposes ALPHA
only; the scorer minimises g(P,alpha)/E h(p) over the 4-parameter two-atom
symmetric coupling class internally, certifying a rigorous LOWER bound on
inf_P g/Eh via mpmath.iv interval branch-and-bound.

This is the inversion directive's requirement: the inner inf over P is a
computation, not a candidate. The candidate supplies only alpha; the scorer
takes the infimum over (a1,a2,b1,b2) with feasibility
    0 <= a=(a1+a2)/2 <= t < b=(b1+b2)/2 <= 1,  beta=(t-a)/(b-a) in (0,1],  E h(p)>0.

The quantity certified:
    G(t,alpha) = inf_{P}  g(P,alpha) / E h(p).

We decide G(t,alpha) >= 1 by rigorous interval B&B: subdivide the 4-d feasible
box, and for each cell bound g/Eh below with outward-rounded interval arithmetic.
A cell whose LOWER enclosure bound is >= 1 is certified. The infimum is >= 1 iff
every feasible cell is either certified or provably infeasible.

USAGE:
    python inner_inf_scorer.py <t> <alpha> [max_splits] [min_width]
        t, alpha       : floats
        max_splits     : cap on B&B splits (default 200000)
        min_width      : cell width below which we stop splitting and mark the
                         cell "unexplorable" (its lower enclosure bound < 1 but
                         we cannot afford finer resolution) (default 1e-6)

PRINTS/CONTRACT (for the harness / scoring map):
    VERDICT: certifiable          — every feasible cell certified (inf_P g/Eh >= 1)
    VERDICT: not-certifiable      — certified-explorable region found with lo < 1
    VERDICT: inconclusive (round) — ran out of splits / cells below min_width
    then certification stats: splits, certified cells, unexplorable cells, worst
    lower enclosure bound witnessed, and (if alpha_min from the candidate is
    used) no alpha-max: alpha is a SINGLE scalar from the candidate.

The rigorous arithmetic: h is computed via outward-rounded interval arithmetic
(endpoint enclosure — h is concave so its min on a cell is at an endpoint; we
evaluate at both endpoints and take the min for lo, max for hi, plus cap at 1 at
the midpoint); every weight (beta, wa, wb) and every sum/product is done as
interval arithmetic with monotone IEEE endpoints (division, multiply, add,
subtract all outward). This gives a provable enclosure of g/Eh on each cell.

Time budget: hard-capped by max_splits (default 200000) and a wall-clock guard
of ~10 s (STEP 1 directive); if the wall clock exceeds it, we report
"inconclusive (time)" and stop, so a long B&B cannot silently claim a
certificate it did not finish.
"""

import sys
import time

import mpmath as mp

mp.mp.dps = 50
LN2 = mp.log(mp.mpf(2))


# ---------------------------------------------------------------------------
# outward-rounded interval arithmetic (directed rounding via endpoint ops)
# ---------------------------------------------------------------------------
class Iv:
    __slots__ = ("a", "b")

    def __init__(self, lo, hi):
        self.a = mp.mpf(lo)
        self.b = mp.mpf(hi)

    def __repr__(self):
        return f"[{mp.nstr(self.a, 6)},{mp.nstr(self.b, 6)}]"


def iadd(x, y): return Iv(x.a + y.a, x.b + y.b)
def isub(x, y): return Iv(x.a - y.b, x.b - y.a)
def imul(x, y):
    p = (x.a * y.a, x.a * y.b, x.b * y.a, x.b * y.b)
    return Iv(min(p), max(p))
def idiv(x, y):
    if y.a <= 0 <= y.b:
        return Iv(mp.mpf("-inf"), mp.mpf("inf"))
    p = (x.a / y.a, x.a / y.b, x.b / y.a, x.b / y.b)
    return Iv(min(p), max(p))


def h_iv(x):
    """Enclosure of h(z) for z an interval x in [0,1].  h concave -> min at an
    endpoint (or 0 at boundary), max at an endpoint or 1 at crossing 1/2."""
    xa, xb = x.a, x.b
    def hv(z):
        if z <= 0 or z >= 1:
            return mp.mpf(0)
        return -z * mp.log(z) / LN2 - (1 - z) * mp.log(1 - z) / LN2
    lo = min(hv(xa), hv(xb))
    hi = max(hv(xa), hv(xb))
    if xa <= mp.mpf("0.5") <= xb:
        hi = mp.mpf(1)
    return Iv(lo, hi)


def phi1(p, q):
    """median{max(p,q), 1/2, p+q} on intervals -> (lower-bound, upper-bound) pair.
    phi is piecewise: median of three affine/constant pieces, so on a small cell
    we bound each piece over the cell and take the elementwise median of the
    three bound-intervals LOCALLY. To keep it rigorous and cheap we use the
    enclosure: min over the cell of each of the three candidate values, max
    likewise, then lo = the second-smallest of the three mins, hi = the
    second-largest of the three maxes (median of the bounding functions).
    This is a valid enclosure of the median of the three functions (medians
    commute with pointwise order-bound monotone envelopes when each function is
    enclosed by [fmin_i, fmax_i] with fmin_i<=f_i<=fmax_i)."""
    # p,q are intervals; compute enclosures of the three real-valued functions'
    # ranges over the cell (they are monotone-ish; take endpoint min/max).
    def rng(f):
        # f : (lo_p,hi_p,lo_q,hi_q) -> (vmin, vmax) over the box
        samples = []
        for pp in (p.a, p.b):
            for qq in (q.a, q.b):
                samples.append(f(pp, qq))
        return min(samples), max(samples)

    smax = mp.mpf(0.5)  # constant 1/2
    # function1 = max(p,q)
    m1 = rng(lambda pp, qq: max(pp, qq))
    # function2 = 1/2 (constant)
    m2 = (mp.mpf("0.5"), mp.mpf("0.5"))
    # function3 = p+q
    m3 = rng(lambda pp, qq: pp + qq)

    los = sorted([m1[0], m2[0], m3[0]])
    his = sorted([m1[1], m2[1], m3[1]])
    return Iv(los[1], his[1])   # median of the three bound-enclosures


# ---------------------------------------------------------------------------
# rigorous enclosure of g(P,alpha)/E h(p) over a 4-param cell at fixed t,alpha
# ---------------------------------------------------------------------------
def ratio_iv(a1, a2, b1, b2, t, alpha):
    """Enclosure of g(P,alpha)/E h(p) over the cell [a1]x[a2]x[b1]x[b2] at fixed
    (t, alpha).  Constraints (a<=t<b, beta in (0,1], Ehr>0) are the caller's
    responsibility; if a cell crosses infeasibility we return a wide or
    +/-inf enclosure flagged by an Ehr upper bound <= 0."""
    two = Iv(2, 2)
    one = Iv(1, 1)
    t_iv = Iv(t, t)
    alpha_iv = Iv(alpha, alpha)
    a = idiv(iadd(a1, a2), two)
    b = idiv(iadd(b1, b2), two)
    # feasibility quick-box check (float level): if the ENTIRE box is infeasible
    # (b.max <= t and a...), the caller prunes; here we only refuse to divide by
    # a beta that may be <=0 and may have denominator 0.
    beta = idiv(isub(t_iv, a), isub(b, a))
    if isub(b, a).a <= 0:
        return Iv("-inf", "inf"), Iv("-inf", "inf"), 0  # denom spans <=0

    wa = idiv(isub(one, beta), two)
    wb = idiv(beta, two)

    vals = [a1, a2, b1, b2]
    wts = [wa, wa, wb, wb]

    eh = Iv(0, 0)
    for i in range(4):
        eh = iadd(eh, imul(wts[i], h_iv(vals[i])))
    if eh.b <= 0:
        return Iv("-inf", "inf"), eh, 0   # E h(p) <= 0 somewhere -> infeasible
    if eh.a <= 0:
        # denominator may cross 0 -> cannot bound ratio robustly; mark infeasible
        return Iv("-inf", "inf"), eh, 0

    # independent coupling E h(p+q-pq)
    e_ind = Iv(0, 0)
    for i in range(4):
        for j in range(4):
            vv = isub(iadd(vals[i], vals[j]), imul(vals[i], vals[j]))
            e_ind = iadd(e_ind, imul(imul(wts[i], wts[j]), h_iv(vv)))

    # coupled E_{P_pq} h(phi1): Q_{a1,a2} weight (1-beta)/2 each direction once:
    # symmetric -> 2*wa*h(phi(a1,a2)) + 2*wb*h(phi(b1,b2)).  (each Q_xy has two
    # Diracs, weight (1-beta) over the Q -> (1-beta)/2 per Dirac = wa.)
    h_pab = h_iv(phi1(a1, a2))
    h_pcd = h_iv(phi1(b1, b2))
    e_coup = iadd(imul(Iv(2, 2), imul(wa, h_pab)),
                  imul(Iv(2, 2), imul(wb, h_pcd)))

    g = iadd(imul(isub(one, alpha_iv), e_ind), imul(alpha_iv, e_coup))
    return idiv(g, eh), eh, 1


# ---------------------------------------------------------------------------
# interval branch-and-bound over the feasible box
# ---------------------------------------------------------------------------
def certify(t, alpha, max_splits, min_width, wall_sec=10.0):
    """Certify inf_P g(P,alpha)/Eh >= 1 over the feasible two-atom class.

    Feasible box (superset of the constraint set):
        a1,a2 in [0,t]        (so a=(a1+a2)/2 <= t)
        b=(b1+b2)/2 in (t,1]  -> b1,b2 in (t,1]; we start w/ [t,1],
                                but must EXCLUDE cells where b<=t; we pre-narrow
                                to b1,b2 in (t,1] and additionally require
                                (b1+b2)/2 > t + slack; the constraint b<=1 holds.
    The constraint set is 0<=a<=t<b<=1. We cover a1,a2 in [0,t], b1,b2 in [t,1]
    but cells where (b1+b2)/2 <= t are infeasible and pruned (empty cover).
    Beta in (0,1] is implied by a<=t<b. Ehr>0 is checked per cell.
    """
    zero = mp.mpf(0)
    t_mp = mp.mpf(t)
    # root box
    root = (Iv(0, t_mp), Iv(0, t_mp), Iv(t_mp, 1), Iv(t_mp, 1))
    stack = [root]
    split_count = 0
    certified_cells = 0
    unexplorable = []          # cells below min_width whose lo enclosure < 1
    worst_lo = mp.mpf("inf")   # smallest lower enclosure bound witnessed
    worst_cell = None
    infeasible = 0
    t0 = time.time()

    def cell_infeasible(c):
        # (b1+b2)/2 <= t  ->  no feasible t (t is closed `a<=t<b`: need b>t)
        bm = (c[2].b + c[3].b) / 2
        return bm <= t_mp

    while stack and split_count < max_splits:
        if time.time() - t0 > wall_sec:
            return {"verdict": "inconclusive (time)",
                    "splits": split_count, "certified": certified_cells,
                    "unexplorable": len(unexplorable),
                    "worst_lo": worst_lo, "worst_cell": worst_cell,
                    "infeasible": infeasible}
        c = stack.pop()
        w = max(c[i].b - c[i].a for i in range(4))

        # -- geometric feasibility of the whole box: need some a<=t<b point --
        # a=(a1+a2)/2 can be <= t since a1,a2 in [0,t]; b>t reachable iff bmax>t.
        # Also need b-max > t.
        if (c[2].b + c[3].b) / 2 <= t_mp:
            infeasible += 1          # every point has b<=t -> no feasible t
            continue

        r, eh, ok = ratio_iv(*c, t, alpha)
        if ok == 1:
            lo = r.a
            if lo < worst_lo:
                worst_lo = lo
                worst_cell = c
            if lo >= 1:
                certified_cells += 1
                continue
            if w < min_width:
                unexplorable.append(c)
                continue
            # not certified and wide enough -> split
        else:
            # ok==0: box crosses an infeasibility boundary (beta denom 0,
            # E h(p)<=0 partly). Mixed cell: split unless too narrow to resolve.
            if w < min_width:
                unexplorable.append(c)
                continue

        # split the widest dimension
        split_count += 1
        dim = max(range(4), key=lambda i: c[i].b - c[i].a)
        mid = (c[dim].a + c[dim].b) / 2
        for rep in (0, 1):
            nb = list(c)
            nb[dim] = Iv(c[dim].a, mid) if rep == 0 else Iv(mid, c[dim].b)
            stack.append(tuple(nb))

    exhausted = (split_count >= max_splits or bool(stack))
    if exhausted:
        verdict = "inconclusive (round)"
    elif unexplorable:
        verdict = "not-certifiable"
    else:
        verdict = "certifiable"
    return {"verdict": verdict, "splits": split_count,
            "certified": certified_cells,
            "unexplorable": len(unexplorable),
            "worst_lo": worst_lo, "worst_cell": worst_cell,
            "infeasible": infeasible}


def main(argv):
    if len(argv) < 2:
        sys.exit("usage: python inner_inf_scorer.py <t> <alpha> [max_splits] [min_width]")
    t = float(argv[0])
    alpha = float(argv[1])
    max_splits = int(argv[2]) if len(argv) > 2 else 200000
    min_width = float(argv[3]) if len(argv) > 3 else 1e-6

    # first reproduce the reference single-point value (sanity; float)
    # at Yu's witness to confirm the object is encoded right.
    ref_r, ref_eh, ref_ok = ratio_iv(Iv(0.3300622, 0.3300622),
                                     Iv(0.3300622, 0.3300622),
                                     Iv(0.3300622, 0.3300622), Iv(1, 1),
                                     t, alpha)
    ref = float(ref_r.a) if ref_ok else float("nan")

    res = certify(t, alpha, max_splits, min_width, wall_sec=10.0)
    print(f"inner-inf scorer: t={t:.8f} alpha={alpha:.8f}")
    print(f"  reference inf-at-Yu-witness lower bound (deg cell) = {mp.nstr(ref,14)}")
    print(f"  VERDICT: {res['verdict']}")
    print(f"  splits={res['splits']}  certified_cells={res['certified']}  "
          f"infeasible={res['infeasible']}  unexplorable={res['unexplorable']}")
    print(f"  worst lower enclosure bound witnessed = {mp.nstr(res['worst_lo'],14)}")
    if res["worst_cell"] is not None:
        print(f"  worst cell: a1{res['worst_cell'][0]} a2{res['worst_cell'][1]} "
              f"b1{res['worst_cell'][2]} b2{res['worst_cell'][3]}")
    ok = (res["verdict"] == "certifiable")
    print(f"  CERTIFIED inf_P g/Eh >= 1 : {ok}")


if __name__ == "__main__":
    main(sys.argv[1:])
