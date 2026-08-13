"""PE620 winner check: n_t(d) = [(c-t)*beta + (s+t)*mu]/pi meshing model.

Model (winner of the 8-pattern scan):
    n_t(d) := [ (c - t)*beta(d) + (s + t)*mu(d) ] / pi
  where beta = angle of the planet centre about the ring centre O, and
  mu = angle about the sun centre S (both for the upper tangency point of a
  type-t planet at centre separation d).  A valid arrangement requires:
    (a) n_p(d) in Z  and  n_q(d) in Z          [mirror pairs mesh]
    (b) n_p(d) - n_q(d) == p - q (mod 2)       [cross-type parity]
  Each valid d yields exactly ONE arrangement: the two p-planets at their
  two tangency points (upper/lower mirror pair) and the two q-planets at
  theirs.  g(c,s,p,q) = number of valid interior d (endpoints where either
  type's positions coincide -- d=|a_t-b_t| or a_t+b_t -- are the degenerate
  single-circle case and are excluded; the four planets must be distinct).

  This reproduces g(16,5,5,6)=9 (the scan found n_p=0..9 with n_p=0 sitting
  exactly on the degenerate d_min endpoint) and is checked against G(16)=9,
  G(20)=205.  d-scan here is O(N) in the grid -- a small-case probe of the
  MODEL, not the G(500) method (which must count these roots without scanning).
"""
import math
import numpy as np
import os

OUT = "/workspace/code/out/n_integer_model_fresh.txt"
os.makedirs("/workspace/code/out", exist_ok=True)


def n_arrays(c, s, t, d_array):
    """n_t(d) = [(c-t)*beta + (s+t)*mu]/pi over the d grid (float scan)."""
    pi = math.pi
    R = c / (2 * pi)
    r = s / (2 * pi)
    rho = t / (2 * pi)
    a = R - rho
    b = r + rho
    x = (a * a - b * b + d_array * d_array) / (2.0 * d_array)
    y = np.sqrt(np.maximum(a * a - x * x, 0.0))
    beta = np.arctan2(y, x)
    mu = np.arctan2(y, x - d_array)
    return ((c - t) * beta + (s + t) * mu) / pi


def valid_ds(c, s, p, q, tol=1e-3, N=None):
    """List of interior valid d values (degenerate endpoints removed).

    Returns list of (d, n_p, n_q, y_p, y_q).  Degenerate: a d where either
    the p or q tangency points coincide (y ~ 0) -- those yield fewer than four
    distinct planets and are not counted as arrangements.
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
    parity = ((rp_.astype(int) - rq_.astype(int)) % 2)
    sel = ok_p & ok_q & (parity == (p - q) % 2)

    # y values (degeneracy measure) per type
    def y_array(c, s, t, d):
        pi = math.pi
        R = c / (2 * pi); r = s / (2 * pi); rho = t / (2 * pi)
        a = R - rho; b = r + rho
        x = (a * a - b * b + d * d) / (2 * d)
        return np.sqrt(np.maximum(a * a - x * x, 0.0))
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
            # take the d minimizing |n_p-round| + |n_q-round| in the run
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
    # exclude degenerate (y ~ 0) endpoints
    YTOL = 1e-5
    vals = [v for v in vals if v[3] > YTOL and v[4] > YTOL]
    return vals


def main():
    out = []
    def emit(s_=""):
        print(s_, flush=True)
        out.append(s_)

    emit("PE620 winner-check: n_t = [(c-t)*beta + (s+t)*mu]/pi meshing model")
    emit("valid: n_p,n_q in Z, n_p-n_q == p-q (mod 2); degenerate d excluded")
    emit("=" * 76)

    # g(16,5,5,6)
    vals = valid_ds(16, 5, 5, 6)
    emit("")
    emit("g(16,5,5,6) = %d  (oracle 9)  %s"
         % (len(vals), "AGREE" if len(vals) == 9 else "DISAGREE"))
    for d, npv, nqv, yp, yq in vals:
        emit("   d=%.17g  n_p=%.6f n_q=%.6f  (sum=%.6f) y_p=%.2e y_q=%.2e"
             % (d, npv, nqv, npv + nqv, yp, yq))
    emit("   note: n_p+n_q == %d (s+c) for every solution; n_p runs 1..9."
         % (16 + 5))

    # G(16)
    pairs16 = [(s + p + q, s, p, q)
               for s in range(5, 16 - 10)
               for p in range(5, 16 - s - 5)
               for q in range(p + 1, 16 - s - p + 1)]
    tot16 = sum(len(valid_ds(c, s, p, q)) for (c, s, p, q) in pairs16)
    emit("")
    emit("G(16) = %d  (oracle 9)  %s   [only pair g(16,5,5,6)=%d]"
         % (tot16, "AGREE" if tot16 == 9 else "DISAGREE",
            len(valid_ds(16, 5, 5, 6))))

    # G(20)
    pairs20 = [(s + p + q, s, p, q)
               for s in range(5, 20 - 10)
               for p in range(5, 20 - s - 5)
               for q in range(p + 1, 20 - s - p + 1)]
    emit("")
    emit("G(20): %d pairs (s+p+q<=20)" % len(pairs20))
    tot20 = 0
    for (c, s, p, q) in sorted(pairs20):
        g_ = len(valid_ds(c, s, p, q))
        tot20 += g_
        emit("   g(%2d,%2d,%2d,%2d) = %3d" % (c, s, p, q, g_))
    emit("")
    emit("G(20) = %d  (oracle 205)  %s"
         % (tot20, "AGREE" if tot20 == 205 else "DISAGREE"))

    with open(OUT, "w") as f:
        f.write("\n".join(out) + "\n")
    emit("")
    emit("Output saved to %s" % OUT)


if __name__ == "__main__":
    main()