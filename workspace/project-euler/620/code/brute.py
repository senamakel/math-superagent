"""PE620 discrete-lattice brute oracle (least-mesh-angle model).

MODEL (least-mesh-angle lattice, positions as multiples of beta=2*pi/(s+c)):
  C at origin, radius R = c/(2*pi).  S at (d,0), radius r = s/(2*pi).
  d is the off-centre distance, a free (real) parameter.
  A planet of size k (radius rho = k/(2*pi)) tangent internally to C and
  externally to S has centre at distance a = R-rho from O and b = r+rho from
  S.  A planet centred on the ray from S at angle m*beta meshes with both
  gears iff, by the law of cosines,
      d^2 + b^2 - 2*d*b*cos(m*beta) = a^2
  i.e.  f_k(d) := (d^2 + b^2 - a^2) / (2*d*b)  equals cos(m*beta).
  Slots m in {0,...,N-1}, N = s+c.  A slot m and its mirror N-m give the two
  tangency points of the *same* pair of positions; when m=0 or 2*m=N the two
  positions coincide (degenerate) and are excluded.  Because cos(x)=cos(y)
  forces y = +/-x mod 2*pi, each size has at most ONE non-degenerate slot
  pair per d, hence exactly one placement of its two planets per d: the
  arrangement for a valid d (p-slot pair + q-slot pair) is unique, and
  g = number of distinct valid d values.

  The two sizes p, q must work with the SAME d.  So g = number of valid
  candidate d values, where a candidate d is a root of f_p(d)=cos(m_p*beta)
  for some integer slot m_p that ALSO satisfies f_q(d)=cos(m_q*beta) for
  some integer slot m_q.

  Closed form: f_k(d)=cos(m*beta)  <=>  d^2 - 2*b*cos(m*beta)*d + (b^2-a^2)=0
  with roots d = b*cos(m*beta) +/- sqrt(b^2*cos^2(m*beta) - (b^2-a^2)).
  (Real roots automatically have |a-b| <= d <= a+b, i.e. the two-circle
  intersection exists.)

  Physical constraints on d:
    * d > 0;
    * closest gap between the S and C boundaries >= 1cm:  R - r - d >= 1;
    * both sizes have a valid two-circle intersection (implied by real roots,
      kept as an explicit interval check on the candidates).

  Algorithm per (c,s,p,q):
    valid_d_interval: DL..DU with DL = max(|a_k-b_k|), DU = min(a_k+b_k,
    R-r-1), k in {p,q}.
    For each non-degenerate slot m_p (0 < m_p < N/2): solve the quadratic in
    d, keep roots in [DL,DU].  For each candidate d (deduped), check size q:
    does some non-degenerate slot m_q satisfy |f_q(d)-cos(m_q*beta)| < TOL?
    If yes, d is valid and contributes exactly one arrangement.
    g = number of distinct such d.

  Complexity: O(N) quadratics + O(N) slot checks per candidate => well below
  O(N^2) per pair; this is the brute oracle and is only run for tiny
  s+p+q <= ~40.  Floating point is used (radii are irrational 1/(2*pi)
  multiples), but every claim is re-verified against its defining equation
  with TOL=1e-9, and d values are printed at 17 significant digits.

  Oracle values to reproduce:
      g(16,5,5,6) = 9
      G(16)       = 9      (only pair: g(16,5,5,6))
      G(20)       = 205    (22 pairs, s+p+q <= 20)
"""

import math
import time

OUTFILE = "/workspace/code/out/lattice_test.txt"
TOL = 1e-9


def f_k(d, k, R, r):
    """cos of the angle at S between the centre line and a size-k planet at
    centre offset d:  f = (d^2 + b^2 - a^2)/(2db) with a=R-rho, b=r+rho."""
    rho = k / (2.0 * math.pi)
    a = R - rho
    b = r + rho
    return (d * d + b * b - a * a) / (2.0 * d * b)


def quadratic_roots(m, k, R, r):
    """Roots d of f_k(d)=cos(2*pi*m/N), N=s+c given by R,r. Returns (list,
    exactness-hint): the two closed-form roots (possibly one) of
    d^2 - 2*b*cos(m*beta)*d + (b^2-a^2) = 0."""
    rho = k / (2.0 * math.pi)
    a = R - rho
    b = r + rho
    c = math.cos(2.0 * math.pi * m / (2.0 * math.pi * (R + r)))
    disc = b * b * c * c - (b * b - a * a)
    if disc < 0:
        return []
    roots = []
    sd = math.sqrt(disc)
    for d in (b * c + sd, b * c - sd):
        if d > 1e-12:
            roots.append(d)
    return roots


def valid_slot_exists(d, k, N, R, r, tol=TOL):
    """True iff size k at offset d has a non-degenerate valid slot:
    some m in {0..N-1} with 0 < m, 2*m != N, |f_k(d)-cos(2*pi*m/N)| < tol."""
    for m in range(1, N):
        if 2 * m == N:
            continue
        target = math.cos(2.0 * math.pi * m / N)
        if abs(f_k(d, k, R, r) - target) <= tol:
            return True
    return False


def p_slots(d, N, R, r, k, tol=TOL):
    """All non-degenerate valid slots (0 < m < N/2, mirrors deduped) for size
    k at offset d.  Used for reporting."""
    out = []
    for m in range(1, N // 2 + 1):
        if 2 * m == N:
            continue
        target = math.cos(2.0 * math.pi * m / N)
        if abs(f_k(d, k, R, r) - target) <= tol:
            out.append(m)
    return out


def g_count(c, s, p, q, verbose=False):
    """g(c,s,p,q) per the discrete lattice model.

    Returns (g, details) where details is a list of dicts
      {d: float, m_p: non-degenerate p-slot(s), m_q: q-slot(s)}.
    Each valid d contributes exactly one arrangement.
    """
    R = c / (2.0 * math.pi)
    r = s / (2.0 * math.pi)
    N = s + c

    # valid d interval from the geometry of both sizes plus the 1cm gap
    bounds = []
    for k in (p, q):
        rho = k / (2.0 * math.pi)
        a = R - rho
        b = r + rho
        bounds.append((abs(a - b), a + b))
    DL = max(lo for lo, _ in bounds)
    DU = min(hi for _, hi in bounds)
    DU = min(DU, R - r - 1.0)
    if DL > DU or DU <= 0:
        return 0, []

    # candidate d's: roots of the p-equation over non-degenerate slots in range
    candidates = set()          # rounded key -> exact d
    for mp in range(1, N // 2 + 1):
        if 2 * mp == N:
            continue
        for d in quadratic_roots(mp, p, R, r):
            if DL - 1e-9 <= d <= DU + 1e-9:
                candidates[round(d, 9)] = d

    # each candidate must also give q a valid non-degenerate slot
    details = []
    for key in sorted(candidates):
        d = candidates[key]
        if not valid_slot_exists(d, q, N, R, r):
            continue
        mps = p_slots(d, N, R, r, p)
        mqs = p_slots(d, N, R, r, q)
        if not mps or not mqs:
            continue
        details.append(dict(d=d, m_p=mps, m_q=mqs))

    if verbose:
        for v in details:
            print("  d = %.17g   p-slots %s   q-slots %s"
                  % (v['d'], v['m_p'], v['m_q']))
    return len(details), details


def G_sum(n, verbose=False):
    """G(n) = sum over s>=5, p>=5, p<q, s+p+q<=n of g(s+p+q, s, p, q)."""
    total = 0
    rows = []
    for s in range(5, n - 10 + 1):
        for p in range(5, n - s - 5 + 1):
            for q in range(p + 1, n - s - p + 1):
                c = s + p + q
                g, _ = g_count(c, s, p, q, verbose=verbose)
                rows.append((c, s, p, q, g))
                total += g
    return total, rows


def main():
    out = []
    def emit(s=""):
        print(s, flush=True)
        out.append(s)

    emit("PE620 discrete-lattice brute oracle (least-mesh-angle model)")
    emit("beta = 2*pi/(s+c); candidate d from closed-form roots of")
    emit("f_p(d)=cos(m_p*beta); each candidate checked for a valid q slot.")
    emit("Each valid d gives exactly one arrangement "
         "(2 p-planets at slot-pair {m,N-m}, same for q).")
    emit("=" * 72)

    # [1] g(16,5,5,6) must be 9
    t0 = time.perf_counter()
    g, dvals = g_count(16, 5, 5, 6, verbose=True)
    dt = time.perf_counter() - t0
    emit("[1] g(16,5,5,6) = %d   (oracle 9)   %s   [%.2fs]"
         % (g, "AGREE" if g == 9 else "DISAGREE", dt))
    emit("    %d distinct candidate d values:" % len(dvals))
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
    emit("    per-pair g values:")
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