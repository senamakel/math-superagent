"""PE620 parity-filter test for the n_t integer meshing model.

Compares g(c,s,p,q) under the current model (valid iff n_p, n_q in Z AND
n_p - n_q == p - q mod 2) against the same model with the parity filter
REMOVED (valid iff n_p, n_q in Z only).  All 22 (c,s,p,q) tuples of G(20)
are run both ways, side by side, plus g(16,5,5,6) detail.

Expected structural fact: the model satisfies the functional identity
    n_p(d) + n_q(d) = c + s   for EVERY interior d   (c = s+p+q in G-sums),
so for any integer solution
    n_p - n_q = 2 n_p - (c+s)  ≡  c+s  =  2s+p+q  ≡  p+q  ≡  p-q  (mod 2),
i.e. the parity filter holds automatically and removing it changes nothing.
This program checks that by direct comparison and also prints the min/max of
n_p + n_q over all valid d found (expect exactly s+c at every one).

Note: what would have to be true for this to be wrong is that some candidate
d has n_p and n_q both within tol of integers while n_p+n_q deviates from
c+s by >= 0.5 (then rint(n_q) could land on the other parity).  The identity
is exact to ~1e-13, so that cannot happen; the run confirms it.

Complexity: same fixed-grid O(N) probe as n_integer_count.py (N = 2^20+1,
23 tuples) -- a small-case model test, NOT the G(500) method.
"""
import math
import os

import numpy as np

from n_integer_count import n_arrays

OUT = "/workspace/code/out/n_integer_parity_test.txt"
os.makedirs("/workspace/code/out", exist_ok=True)


def y_array(c, s, t, d_array):
    """|y| of the upper tangency point of a type-t planet at centre sep d."""
    pi = math.pi
    R = c / (2 * pi)
    r = s / (2 * pi)
    rho = t / (2 * pi)
    a = R - rho
    b = r + rho
    x = (a * a - b * b + d_array * d_array) / (2.0 * d_array)
    return np.sqrt(np.maximum(a * a - x * x, 0.0))


def valid_ds(c, s, p, q, use_parity=True, tol=1e-3, N=None):
    """Valid interior d values under the n_t model.

    use_parity=True  -> n_p, n_q in Z AND n_p-n_q == p-q (mod 2)   [current]
    use_parity=False -> n_p, n_q in Z only (parity filter removed).
    Returns list of (d, n_p, n_q, y_p, y_q).  Degenerate endpoints (y ~ 0,
    coincident planets) excluded, exactly as in n_integer_count.valid_ds.
    """
    pi = math.pi
    R = c / (2 * pi)
    r = s / (2 * pi)
    rp, rq = p / (2 * pi), q / (2 * pi)
    a_p, b_p = R - rp, r + rp
    a_q, b_q = R - rq, r + rq
    d_min = max(abs(a_p - b_p), abs(a_q - b_q))
    d_max = min(a_p + b_p, a_q + b_q, R - r - 1.0)
    if d_min > d_max:
        return []
    if N is None:
        N = (1 << 20) + 1
    dv = np.linspace(d_min, d_max, N)
    np_ = n_arrays(c, s, p, dv)
    nq = n_arrays(c, s, q, dv)
    rp_ = np.rint(np_)
    rq_ = np.rint(nq)
    ok_p = np.abs(np_ - rp_) < tol
    ok_q = np.abs(nq - rq_) < tol
    if use_parity:
        parity = ((rp_.astype(int) - rq_.astype(int)) % 2)
        sel = ok_p & ok_q & (parity == (p - q) % 2)
    else:
        sel = ok_p & ok_q

    yp = y_array(c, s, p, dv)
    yq = y_array(c, s, q, dv)

    vals = []
    inrun = False
    for k in range(N):
        if sel[k] and not inrun:
            inrun = True
            start = k
        elif not sel[k] and inrun:
            inrun = False
            seg = slice(start, k)
            cost = (np.abs(np_[seg] - rp_[seg]) + np.abs(nq[seg] - rq_[seg]))
            bi = start + int(np.argmin(cost))
            vals.append((float(dv[bi]), float(np_[bi]), float(nq[bi]),
                         float(yp[bi]), float(yq[bi])))
    if inrun:
        seg = slice(start, N)
        cost = (np.abs(np_[seg] - rp_[seg]) + np.abs(nq[seg] - rq_[seg]))
        bi = start + int(np.argmin(cost))
        vals.append((float(dv[bi]), float(np_[bi]), float(nq[bi]),
                     float(yp[bi]), float(yq[bi])))
    YTOL = 1e-5
    vals = [v for v in vals if v[3] > YTOL and v[4] > YTOL]
    return vals


def g20_tuples():
    return [(s + p + q, s, p, q)
            for s in range(5, 20 - 10)
            for p in range(5, 20 - s - 5)
            for q in range(p + 1, 20 - s - p + 1)]


def main():
    out = []

    def emit(s_=""):
        print(s_, flush=True)
        out.append(s_)

    emit("PE620 parity-filter test of the n_t integer meshing model")
    emit("model: n_t(d) = [(c-t)*beta + (s+t)*mu]/pi (see n_integer_count.py)")
    emit("with-parity:  n_p,n_q in Z and n_p-n_q == p-q (mod 2)")
    emit("without-parity: n_p,n_q in Z only (filter removed)")
    emit("=" * 76)

    # -- flagship detail, both ways
    emit("")
    emit("g(16,5,5,6): with parity = %d, without parity = %d"
         % (len(valid_ds(16, 5, 5, 6, True)),
            len(valid_ds(16, 5, 5, 6, False))))
    vals = valid_ds(16, 5, 5, 6, False)
    sums = [npv + nqv for (_, npv, nqv, _, _) in vals]
    emit("   valid d count (no parity) = %d" % len(vals))
    emit("   n_p+n_q over valid d: min=%.10f max=%.10f (s+c = %d)"
         % (min(sums), max(sums), 16 + 5))

    # -- all 22 G(20) tuples, side by side
    pairs = sorted(g20_tuples())
    emit("")
    emit("G(20) tuples, g with vs without parity filter   [c+s even => filter"
         " parity condition n_p-n_q==p-q (mod 2) reduces to n_p==n_q (mod 2)]")
    emit("  #    c  s  p  q   g(par)  g(nopar)  change?  c+s parity")
    tot_par = 0
    tot_nopar = 0
    changed = []
    smin_all, smax_all = 1e300, -1e300
    for idx, (c, s, p, q) in enumerate(pairs, 1):
        gp = len(valid_ds(c, s, p, q, True))
        gn = len(valid_ds(c, s, p, q, False))
        tot_par += gp
        tot_nopar += gn
        ch = (gp != gn)
        if ch:
            changed.append((c, s, p, q))
        parity_cs = (c + s) % 2
        emit("  %2d %3d %2d %2d %2d   %6d   %6d    %s   %d%s"
             % (idx, c, s, p, q, gp, gn,
                "CHANGED" if ch else "      -", parity_cs,
                " (odd)" if parity_cs else ""))
        # min/max of n_p+n_q over valid d found without parity
        if gn:
            sums = [npv + nqv for (_, npv, nqv, _, _)
                    in valid_ds(c, s, p, q, False)]
            smin_all = min(smin_all, min(sums))
            smax_all = max(smax_all, max(sums))

    emit("")
    emit("G(20) with parity    = %d" % tot_par)
    emit("G(20) without parity = %d" % tot_nopar)
    emit("tuples whose g changed: %s" % (changed if changed else "NONE"))
    odd_cs = [(c, s, p, q) for (c, s, p, q) in pairs if (c + s) % 2 == 1]
    emit("tuples with c+s odd: %s" % odd_cs)
    emit("change set == odd-c+s set: %s"
         % (sorted(changed) == sorted(odd_cs)))
    emit("n_p+n_q over ALL valid d of all tuples: min=%.10f max=%.10f"
         % (smin_all, smax_all))
    emit("   (model identity: n_p+n_q = s+c at every d; all tuples here have"
         " s+c = 2s+p+q)")

    with open(OUT, "w") as f:
        f.write("\n".join(out) + "\n")
    emit("")
    emit("Output saved to %s" % OUT)


if __name__ == "__main__":
    main()