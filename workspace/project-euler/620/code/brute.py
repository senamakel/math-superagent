"""PE620 naive brute oracle: grid-scan of the n_t meshing model.

MODEL (n_t integer-level model; formulas identical to
code/pattern/n_integer_count.py):
  A type-t planet (circumference t) tangent internally to ring C and
  externally to sun S has its centre at distance a_t = R - rho_t from the
  ring centre O and b_t = r + rho_t from the sun centre S, where
  R = c/2pi, r = s/2pi, rho_t = t/2pi.  For a centre-offset d:
      x = (a_t^2 - b_t^2 + d^2)/(2d),   y = sqrt(a_t^2 - x^2),
      beta = atan2(y, x),               mu = atan2(y, x - d),
      n_t(d) = [(c - t)*beta + (s + t)*mu] / pi.
  A valid arrangement (the two p-planets at the mirror tangency pair, the
  two q-planets at theirs) exists at an interior d iff n_p(d) and n_q(d)
  are integers with (n_p - n_q) == (p - q) (mod 2).  Endpoints where a
  type's two tangency points coincide (y ~ 0) are degenerate and excluded.

NAIVE ORACLE (this file): scan d in [d_min, d_max] on a grid of N = 2^20
points; mark points with |n_p - round(n_p)| < 1e-3 AND
|n_q - round(n_q)| < 1e-3 AND (round(n_p) - round(n_q)) mod 2 == (p - q)
mod 2 AND y_p, y_q > 1e-5; g = number of DISTINCT integer levels of n_p
attained at marked points (n_p is monotone, so one level = one arrangement
root; levels sitting on degenerate endpoints are removed by the y test).

This is the bounded brute-force oracle that validates the O(1)-per-tuple
closed form in code/solution.py on every reachable tuple; it is NOT the
G(500) method (its cost scales with the grid resolution N, appropriate only
for the small c,s,p,q of the oracle values).

Expected: g(16,5,5,6)=9, G(16)=9, 22 per-tuple G(20) values summing 205.
Transcript: /workspace/code/out/brute_oracle_final.txt
"""
import math
import os
import time

import numpy as np

OUT = "/workspace/code/out/brute_oracle_final.txt"
NGRID = 1 << 20
TOL = 1e-3
YTOL = 1e-5


def n_arrays(c, s, t, dv):
    """n_t(d) = [(c-t)*beta + (s+t)*mu]/pi over the d grid (float scan)."""
    R = c / (2.0 * math.pi)
    r = s / (2.0 * math.pi)
    rho = t / (2.0 * math.pi)
    a = R - rho
    b = r + rho
    x = (a * a - b * b + dv * dv) / (2.0 * dv)
    y = np.sqrt(np.maximum(a * a - x * x, 0.0))
    beta = np.arctan2(y, x)
    mu = np.arctan2(y, x - dv)
    return ((c - t) * beta + (s + t) * mu) / math.pi


def y_array(c, s, t, dv):
    """Half-height y of the tangency point (degeneracy measure), per grid d."""
    R = c / (2.0 * math.pi)
    r = s / (2.0 * math.pi)
    rho = t / (2.0 * math.pi)
    a = R - rho
    b = r + rho
    x = (a * a - b * b + dv * dv) / (2.0 * dv)
    return np.sqrt(np.maximum(a * a - x * x, 0.0))


def d_interval(c, s, p, q):
    """(d_min, d_max): interior centre-offset range with both types tangent
    and the 1 cm S-C gap, d_max = R - r - 1."""
    R = c / (2.0 * math.pi)
    r = s / (2.0 * math.pi)
    ap, bp = R - p / (2.0 * math.pi), r + p / (2.0 * math.pi)
    aq, bq = R - q / (2.0 * math.pi), r + q / (2.0 * math.pi)
    d_min = max(abs(ap - bp), abs(aq - bq))
    d_max = min(ap + bp, aq + bq, R - r - 1.0)
    return d_min, d_max


def g_grid(c, s, p, q, N=NGRID, tol=TOL, ytol=YTOL):
    """Naive-oracle g(c,s,p,q): distinct integer levels of n_p at valid grid
    points.  Returns (g, sorted level list)."""
    d_min, d_max = d_interval(c, s, p, q)
    if d_min > d_max:
        return 0, []
    dv = np.linspace(d_min, d_max, N)
    npv = n_arrays(c, s, p, dv)
    nqv = n_arrays(c, s, q, dv)
    rp = np.rint(npv)
    rq = np.rint(nqv)
    ok = (np.abs(npv - rp) < tol) & (np.abs(nqv - rq) < tol)
    ok &= ((rp.astype(np.int64) - rq.astype(np.int64)) % 2) == ((p - q) % 2)
    yp = y_array(c, s, p, dv)
    yq = y_array(c, s, q, dv)
    ok &= (yp > ytol) & (yq > ytol)
    levels = sorted(set(rp.astype(np.int64)[ok]))
    return len(levels), levels


def all_tuples(n):
    """(c,s,p,q) with s+p+q<=n, s>=5, p>=5, p<q (c = s+p+q), sorted."""
    return sorted((s + p + q, s, p, q)
                  for s in range(5, n - 10)
                  for p in range(5, n - s - 5)
                  for q in range(p + 1, n - s - p + 1))


def run_table(n, emit):
    """All per-tuple g for s+p+q<=n; returns (rows, total)."""
    rows = []
    total = 0
    for (c, s, p, q) in all_tuples(n):
        gi, _ = g_grid(c, s, p, q)
        rows.append((c, s, p, q, gi))
        total += gi
    return rows, total


def main():
    lines = []
    def emit(s_=""):
        print(s_, flush=True)
        lines.append(s_)

    emit("PE620 naive brute oracle: n_t = [(c-t)*beta + (s+t)*mu]/pi, grid scan")
    emit("grid N = 2^%d, |n-round| < %.0e for BOTH types, parity"
         % (NGRID.bit_length() - 1, TOL))
    emit("(round(n_p)-round(n_q)) mod 2 == (p-q) mod 2, degenerate endpoints")
    emit("excluded (y_p, y_q > %.0e);  g = distinct integer levels of n_p"
         % YTOL)
    emit("at valid grid points.")
    emit("=" * 74)

    # [1] g(16,5,5,6)
    t0 = time.perf_counter()
    g, lv = g_grid(16, 5, 5, 6)
    dt = time.perf_counter() - t0
    emit("")
    emit("[1] g(16,5,5,6) = %d   (oracle 9)   %s   [%.2fs]"
         % (g, "AGREE" if g == 9 else "DISAGREE", dt))
    emit("    n_p integer levels attained at valid d: %s" % (lv,))

    # [2] G(16)
    t0 = time.perf_counter()
    rows16, g16 = run_table(16, emit)
    dt = time.perf_counter() - t0
    emit("")
    emit("[2] G(16) = %d   (oracle 9)   %s   [%.2fs]"
         % (g16, "AGREE" if g16 == 9 else "DISAGREE", dt))
    for (c, s, p, q, gi) in rows16:
        emit("      g(%2d,%2d,%2d,%2d) = %3d" % (c, s, p, q, gi))

    # [3] G(20)
    t0 = time.perf_counter()
    rows20, g20 = run_table(20, emit)
    dt = time.perf_counter() - t0
    emit("")
    emit("[3] G(20): %d tuples (s+p+q<=20), per-tuple g:" % len(rows20))
    for (c, s, p, q, gi) in rows20:
        emit("      g(%2d,%2d,%2d,%2d) = %3d" % (c, s, p, q, gi))
    emit("")
    emit("G(20) = %d   (oracle 205)   %s   [%.2fs]"
         % (g20, "AGREE" if g20 == 205 else "DISAGREE", dt))

    v_ok = (g == 9 and g16 == 9 and g20 == 205)
    emit("")
    emit("Naive oracle %s the three oracle values 9 / 9 / 205."
         % ("MATCHES" if v_ok else "DOES NOT MATCH"))
    emit("")
    emit("Transcript saved to %s" % OUT)
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()