"""PE620 discrete-lattice brute oracle (least-mesh-angle model).

MODEL (least-mesh-angle lattice, positions as multiples of beta=2*pi/(s+c)):
  C at origin, radius R = c/(2*pi).  S at (d,0), radius r = s/(2*pi).
  d is the off-centre distance, a free (real) parameter of an arrangement.
  A planet of size k (radius rho = k/(2*pi)) tangent internally to C and
  externally to S has centre at distance a = R-rho from O and b = r+rho from
  S.  A planet centred on the ray from S at angle m*beta meshes with both
  gears iff, by the law of cosines at S (sides OS=d, SP=b, OP=a):
      d^2 + b^2 - 2*d*b*cos(m*beta) = a^2
  i.e.  f_k(d) := (d^2 + b^2 - a^2) / (2*d*b)  equals cos(2*pi*m/N).
  Slots m in {0,...,N-1}, N = s+c.  Slot m and its mirror N-m are the two
  tangency points of the same pair of positions; when m=0 or 2*m=N the two
  coincide (degenerate) and are excluded.  cos is strictly decreasing on the
  non-degenerate half-range, so each size has at most ONE non-degenerate slot
  pair per d, hence one placement of its two planets per d -- so an
  arrangement for a valid d is unique, and g = number of valid d values.

  The two sizes p, q must work with the SAME d.  So g = number of distinct
  valid candidate d values, where a candidate d is a root of
  f_p(d)=cos(m_p*beta) for some integer slot m_p that ALSO satisfies
  f_q(d)=cos(m_q*beta) for some integer slot m_q.

  Closed form: f_k(d)=cos(2*pi*m/N)  <=>  d^2 - 2*b*cos(2*pi*m/N)*d
  + (b^2-a^2) = 0, roots  d = b*cos(2*pi*m/N)
  +/- sqrt(b^2*cos^2(2*pi*m/N) - (b^2-a^2)).  Note a^2 - b^2*sin^2 >= 0 is
  the two-circle intersection condition along the ray.

  Physical constraints on candidate d (checked on every root):
    * both planet types' two-circle intersection: |a-b| <= d <= a+b;
    * 1 cm closest gap between S and C boundaries:  R - r - d >= 1;
    * d > 0.

  Algorithm per (c,s,p,q): for every non-degenerate slot m_p, form the
  quadratic in d and keep its real roots inside the valid d interval; dedupe;
  for each candidate d, check whether size q has any non-degenerate valid
  slot (|f_q(d)-cos(2*pi*m/N)| < TOL).  g = number of such d.
  Complexity O(N) per pair (N = s+c staircase to ~40 for the oracle cases).

  This file IS the brute oracle.  It is a bounded, tiny-N program that
  reproduces the statement's worked values; it is not the G(500) method.

  Oracle values to reproduce:
      g(16,5,5,6) = 9
      G(16)       = 9      (only pair: g(16,5,5,6))
      G(20)       = 205    (22 pairs with s+p+q <= 20)
  Output goes to /workspace/code/out/lattice_test.txt
"""

import math
import time

OUTFILE = "/workspace/code/out/lattice_test.txt"
TOL = 1e-9

# ----------------------------------------------------------------------
# geometry helpers
# ----------------------------------------------------------------------

def radii(c, s):
    """(R, r, N): ring radius, sun radius, lattice size N = c + s."""
    R = c / (2.0 * math.pi)
    r = s / (2.0 * math.pi)
    return R, r, c + s


def a_b(k, R, r):
    """(a, b): centre distances to O and to S for a size-k planet (radius
    rho = k/(2pi) gives a = R-rho, b = r+rho)."""
    rho = k / (2.0 * math.pi)
    return R - rho, r + rho


def f_k(d, k, R, r):
    """cos of the angle at S (between SO and SP) of a size-k planet whose
    centre is at offset d from S: f = (d^2 + b^2 - a^2)/(2db)."""
    a, b = a_b(k, R, r)
    return (d * d + b * b - a * a) / (2.0 * d * b)


def cos_slot(m, N):
    """cos(2*pi*m/N) for slot m in a lattice of size N."""
    return math.cos(2.0 * math.pi * m / N)


def nondegenerate_slots(N):
    """Non-degenerate slot representatives m with 0 < m < N/2.  Each such m
    is the mirror pair {m, N-m} of positions; m=0 and 2*m=N are degenerate
    (both positions coincide) and excluded."""
    out = []
    for m in range(1, N // 2 + 1):
        if 2 * m == N:
            continue
        out.append(m)
    return out


def candidate_roots(m, k, R, r):
    """Real d roots of f_k(d) = cos(2*pi*m/N) (closed-form quadratic roots).
    Returns [] if the discriminant is negative."""
    a, b = a_b(k, R, r)
    c = cos_slot(m, int(round(2.0 * math.pi * (R + r))))
    disc = b * b * c * c - (b * b - a * a)
    if disc < 0:
        return []
    sd = math.sqrt(disc)
    return [d for d in (b * c + sd, b * c - sd) if d > 1e-12]


def valid_d_interval(c, s, p, q):
    """(DL, DU) or None: d range with both sizes' two-circle intersections
    and the 1 cm gap R - r - d >= 1 and d > 0."""
    R, r, _ = radii(c, s)
    bounds = []
    for k in (p, q):
        a, b = a_b(k, R, r)
        bounds.append((abs(a - b), a + b))
    DL = max(lo for lo, _ in bounds)
    DU = min(hi for _, hi in bounds)
    DU = min(DU, R - r - 1.0)
    if DL > DU or DU <= 0:
        return None
    return DL, DU


def valid_slots(d, k, N, R, r, tol=TOL):
    """Non-degenerate slots m (0 < m < N/2) for which f_k(d) = cos(2*pi*m/N)
    within tol.  Each such m describes the two positions {m, N-m}."""
    out = []
    for m in nondegenerate_slots(N):
        if abs(f_k(d, k, R, r) - cos_slot(m, N)) <= tol:
            out.append(m)
    return out


# ----------------------------------------------------------------------
# counting
# ----------------------------------------------------------------------

def g_count(c, s, p, q, verbose=False):
    """g(c,s,p,q) per the discrete-lattice model.

    Returns (g, details) where details is a list of dicts
      {d: float, m_p: [non-degenerate p slots], m_q: [non-degenerate q
      slots], passed_q: bool}.
    Each d with passed_q and with at least one non-degenerate slot for both
    sizes contributes exactly ONE arrangement (two p-planets at the mirror
    pair, two q-planets at theirs).
    """
    R, r, N = radii(c, s)
    dr = valid_d_interval(c, s, p, q)
    if dr is None:
        return 0, []
    DL, DU = dr

    # candidate d values: roots of the p-equation over non-degenerate slots
    candidates = {}           # rounded key -> (d, m_p)
    for mp in nondegenerate_slots(N):
        for d in candidate_roots(mp, p, R, r):
            if DL - 1e-9 <= d <= DU + 1e-9:
                key = round(d, 9)
                if key not in candidates:
                    candidates[key] = (d, mp)
                else:
                    # same d from another slot: keep both m's for reporting
                    pass

    details = []
    for key in sorted(candidates):
        d, mp = candidates[key]
        mps = valid_slots(d, p, N, R, r)
        mqs = valid_slots(d, q, N, R, r)
        passed_q = len(mqs) > 0
        if mps and mqs:
            details.append(dict(d=d, m_p=mps, m_q=mqs, passed_q=True))
        elif verbose:
            details.append(dict(d=d, m_p=mps, m_q=mqs, passed_q=False))

    if verbose:
        for v in details:
            print("  d = %.17g   p-slots %-10s q-slots %-10s %s"
                  % (v['d'], v['m_p'], v['m_q'],
                     "VALID" if v['passed_q'] else "(q fails)"))
    valid = [v for v in details if v['passed_q']]
    return len(valid), valid


def G_sum(n, verbose=False):
    """G(n) = sum over s>=5, p>=5, p<q, s+p+q<=n of g(s+p+q, s, p, q)."""
    total = 0
    rows = []
    for s in range(5, n - 10):
        for p in range(5, n - s - 5):
            for q in range(p + 1, n - s - p + 1):
                c = s + p + q
                g, _ = g_count(c, s, p, q, verbose=verbose)
                rows.append((c, s, p, q, g))
                total += g
    return total, rows


# ----------------------------------------------------------------------
# oracle driver
# ----------------------------------------------------------------------

def main():
    out = []
    def emit(s=""):
        print(s, flush=True)
        out.append(s)

    emit("PE620 discrete-lattice brute oracle (least-mesh-angle model)")
    emit("beta = 2*pi/(s+c), N = s+c slots; candidate d = closed-form roots")
    emit("of f_p(d)=cos(2*pi*m_p/N); each candidate needs a valid q slot.")
    emit("Each valid d = exactly one arrangement (2 p-planets + 2 q-planets")
    emit("at the mirror slot pairs).  tol = %.0e." % TOL)
    emit("=" * 72)

    # [1] g(16,5,5,6) must be 9
    t0 = time.perf_counter()
    g, dvals = g_count(16, 5, 5, 6, verbose=True)
    dt = time.perf_counter() - t0
    emit("")
    emit("[1] g(16,5,5,6) = %d   (oracle 9)   %s   [%.2fs]"
         % (g, "AGREE" if g == 9 else "DISAGREE", dt))
    emit("    %d distinct valid d values:" % len(dvals))
    for v in dvals:
        emit("      d = %.17g   p-slots %s   q-slots %s"
             % (v['d'], v['m_p'], v['m_q']))
    emit("")

    # [2] G(16) must be 9
    t0 = time.perf_counter()
    g16, rows16 = G_sum(16)
    dt = time.perf_counter() - t0
    emit("[2] G(16) = %d   (oracle 9)   %s   [%.2fs]"
         % (g16, "AGREE" if g16 == 9 else "DISAGREE", dt))
    for c, s, p, q, gv in rows16:
        emit("      g(%d,%d,%d,%d) = %d" % (c, s, p, q, gv))
    emit("")

    # [3] G(20) must be 205
    t0 = time.perf_counter()
    g20, rows20 = G_sum(20)
    dt = time.perf_counter() - t0
    emit("[3] G(20) = %d   (oracle 205)   %s   [%.2fs]"
         % (g20, "AGREE" if g20 == 205 else "DISAGREE", dt))
    emit("    per-pair g values (%d pairs, s+p+q<=20):" % len(rows20))
    emit("      c  s  p  q    g")
    for c, s, p, q, gv in rows20:
        emit("     %2d %2d %2d %2d  %3d" % (c, s, p, q, gv))
    emit("")

    v1 = "AGREE" if g == 9 else "DISAGREE"
    v2 = "AGREE" if g16 == 9 else "DISAGREE"
    v3 = "AGREE" if g20 == 205 else "DISAGREE"
    emit("Verdicts: g(16,5,5,6)=9 -> %s | G(16)=9 -> %s | G(20)=205 -> %s"
         % (v1, v2, v3))
    emit("MODEL %s the oracle on all three values."
         % ("MATCHES" if v1 == v2 == v3 == "AGREE" else "DOES NOT MATCH"))
    emit("")
    emit("Output saved to %s" % OUTFILE)

    with open(OUTFILE, "w") as f:
        f.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()