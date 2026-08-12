"""Check the direct tooth-phase meshing model (n-integer form) against the
PE620 oracle g(16,5,5,6)=9 and G(16)=9, G(20)=205.

Derivation (free rotations: ring Theta_C, sun Theta_S, planet spins Theta_pj):
  sun-planet contact (external, pitch point on ray S->P at angle mu_j):
      s*(mu_j - Theta_S) - t*(mu_j + pi - Theta_pj) == pi        (mod 2pi)
  ring-planet contact (internal, pitch point on ray O->P at angle beta_j,
      contact on the planet in the same outward direction beta_j):
      c*(beta_j - Theta_C) - t*(beta_j - Theta_pj) == pi         (mod 2pi)
  subtract:   L_j := (c-t_j)*beta_j + (t_j-s)*mu_j + t_j*pi
                    == c*Theta_C - s*Theta_S                     (mod 2pi)
  RHS common to all planets -> all L_j pairwise congruent mod 2pi.

  n_t(d) := [(c-t)*beta(d) + (t-s)*mu(d)] / pi   (dimensionless).
  Mirror pair (upper/lower): beta,mu -> -beta,-mu gives L_L = -pi*n_t + t*pi,
  so L_U == L_L mod 2pi  <=>  n_t integer.
  Cross-type: pi*(n_p - n_q) == (q-p)*pi (mod 2pi) <=> n_p - n_q == q-p (mod 2).

  g(c,s,p,q) = #{ d in (d_min,d_max) : n_p(d) in Z, n_q(d) in Z,
                                  n_p(d) - n_q(d) == q-p (mod 2) }.
  Each valid d gives exactly ONE arrangement: the p planets at the two
  tangency points (mirror pair), the q planets at theirs.

This is a small-case check of the model (d scanning is O(N) in the grid and
is NOT the G(500) method); the oracle decides whether the model is right.
"""
import math
import numpy as np
import os

OUT = "/workspace/code/out/n_integer_model.txt"
os.makedirs("/workspace/code/out", exist_ok=True)


def n_arrays(c, s, t, d_array):
    """n_t(d) = [(c-t)*beta + (t-s)*mu]/pi over the d grid (float scan)."""
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
    return ((c - t) * beta + (t - s) * mu) / pi


def count_case(c, s, p, q, tol=1e-4, N=None, dump=None):
    """Grid-count valid d for (c,s,p,q).  Returns list of (d, n_p, n_q, parity
    ok?)."""
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
    if dump is not None:
        with open(dump, "w") as f:
            f.write("# d  n_p  n_q  parity(round)  ok_p  ok_q\n")
            for k in range(0, N, 512):
                f.write("%.12g %.6f %.6f %d %d %d\n"
                        % (dv[k], np_[k], nq[k], 0, 0, 0))
    # valid requires parity == (q-p) mod 2; report for both parities
    out = []
    for parity_req in (0, 1):
        sel = ok_p & ok_q & (parity == parity_req)
        runs, vals = [], []
        inrun = False
        for k in range(N):
            if sel[k] and not inrun:
                inrun = True
                start = k
            elif not sel[k] and inrun:
                inrun = False
                runs.append((start, k - 1))
                vals.append((float(dv[start]), float(np_[start]), float(nq[start])))
        if inrun:
            runs.append((start, N - 1))
            vals.append((float(dv[start]), float(np_[start]), float(nq[start])))
        out.append((parity_req, vals))
    return out


def main():
    out = []
    def emit(s_=""):
        print(s_, flush=True)
        out.append(s_)

    emit("Direct tooth-phase meshing model (L_j congruence, n-integer form)")
    emit("n_t(d) = [(c-t)*beta + (t-s)*mu]/pi;  g = #{d: n_p,n_q in Z,")
    emit("n_p - n_q == q-p (mod 2)}")
    emit("=" * 72)

    for parity_req, vals in count_case(16, 5, 5, 6):
        emit("")
        emit("g(16,5,5,6) with parity n_p-n_q == %d (mod 2): %d  %s"
             % (parity_req, len(vals),
                "MATCHES oracle 9" if len(vals) == 9 and parity_req == 1
                else ""))
        for d, npv, nqv in vals:
            emit("    d=%.17g   n_p=%.9g  n_q=%.9g" % (d, npv, nqv))
    emit("")
    emit("Check the mirror-quantity levels: n_p should hit consecutive integers")
    emit("as d varies; list the levels for the winning parity if any.")

    # G(16) and G(20) sanity (only the winning parity, if we find one)
    tmp = count_case(16, 5, 5, 6)
    wins = [v for par, v in tmp if par == 1]
    if wins:
        win_par, win_vals = 1, wins[0]
    else:
        win_par, win_vals = None, []
    if win_par is not None and len(win_vals) == 9:
        tot16 = len(win_vals)
        emit("")
        emit("[G(16)] total = %d  (oracle 9)  %s"
             % (tot16, "AGREE" if tot16 == 9 else "DISAGREE"))
        # G(20): enumerate the 22 pairs
        pairs = []
        for s_ in range(5, 20 - 10):
            for p_ in range(5, 20 - s_ - 5):
                for q_ in range(p_ + 1, 20 - s_ - p_ + 1):
                    pairs.append((s_ + p_ + q_, s_, p_, q_))
        tot20 = 0
        emit("")
        emit("[G(20)] 22 pairs, per-pair g (parity %d):" % win_par)
        for (c_, s_, p_, q_) in sorted(pairs):
            res = count_case(c_, s_, p_, q_)
            g_ = len([v for par, v in res if par == win_par][0])
            tot20 += g_
            emit("    g(%2d,%2d,%2d,%2d) = %d" % (c_, s_, p_, q_, g_))
        emit("    G(20) total = %d  (oracle 205)  %s"
             % (tot20, "AGREE" if tot20 == 205 else "DISAGREE"))
    else:
        emit("(no parity-1 winner for g(16,5,5,6); G-sums skipped)")

    with open(OUT, "w") as f:
        f.write("\n".join(out) + "\n")
    emit("")
    emit("Output saved to %s" % OUT)


if __name__ == "__main__":
    main()