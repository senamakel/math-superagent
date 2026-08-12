"""PE620 winner-model term generator (pattern-finder).

Model (validated on the oracle: g(16,5,5,6)=9, G(16)=9, G(20)=205; roots
verified at 60 digits in code/out/winner_refine.txt):
  For a type-t planet at centre-offset d (upper tangency point, centre at
  P with |OP| = a_t = R - rho_t, |SP| = b_t = r + rho_t):
      beta = atan2(y, x),  mu = atan2(y, x-d)     (radians)
      n_t(d) = [(c-t)*beta + (s+t)*mu]/pi
  A valid arrangement (the two p-planets at the upper/lower mirror pair,
  the two q planets at theirs)  <=>  n_p(d), n_q(d) in Z  with
  n_p - n_q == p - q (mod 2), at an interior d in (DL, DU).

Structural conjectures this generator tests per tuple:
  (i)  n_p(d) + n_q(d) = s + c   identically in d  (and then the parity
       condition is automatic: with c = s+p+q, s+c+p-q = 2s+2p even)
  (ii) n_p strictly increasing on (DL, DU)
  If both hold, g = number of integer levels k of n_p crossed in the
  interior of (DL, DU), each found by bisection of n_p(d) - k = 0.

Cost: O(s+c) bisections per tuple (float64, ~100 iterations), plus
O(1) checks per tuple.  Bounded by enumeration of integer levels of a
monotone function -- NOT by the problem bound (this is a term generator
for sequence analysis, not the G(500) answer program).

Emits code/out/seqgen.txt: per-tuple g rows (c,s,p,q,g), the per-c
column sums C(c) = sum_{s+p+q=c} g, and cumulative G(n).
"""
import math
import os

OUT = "/workspace/code/out/seqgen.txt"
os.makedirs("/workspace/code/out", exist_ok=True)

PI = math.pi


def geom(c, s, t, d):
    R = c / (2.0 * PI)
    r = s / (2.0 * PI)
    rho = t / (2.0 * PI)
    a = R - rho
    b = r + rho
    x = (a * a - b * b + d * d) / (2.0 * d)
    y2 = a * a - x * x
    if y2 <= 0:
        return None
    return R, r, a, b, x, math.sqrt(y2)


def n_t(c, s, t, d):
    g = geom(c, s, t, d)
    if g is None:
        return None
    R, r, a, b, x, y = g
    beta = math.atan2(y, x)
    mu = math.atan2(y, x - d)
    return ((c - t) * beta + (s + t) * mu) / PI


def bounds(c, s, p, q):
    R = c / (2.0 * PI)
    r = s / (2.0 * PI)
    lo = []
    hi = []
    for t in (p, q):
        rho = t / (2.0 * PI)
        a, b = R - rho, r + rho
        lo.append(abs(a - b))
        hi.append(a + b)
    DL = max(lo)
    DU = min(hi + [R - r - 1.0])
    return DL, DU


def g_count(c, s, p, q, out=None, checks=True):
    """Return (g, diag). g = number of interior integer crossings of n_p."""
    DL, DU = bounds(c, s, p, q)
    diag = dict(DL=DL, DU=DU)
    if DL >= DU:
        diag['empty'] = True
        return 0, diag

    # --- monotonicity of n_p and identity n_p + n_q = s+c, sampled ---
    # (strictly interior samples; endpoints may be degenerate y=0)
    ok_mono, ok_id, worst_id = True, True, 0.0
    ds = [DL + (DU - DL) * (i + 0.5) / 40.0 for i in range(40)]
    prev = None
    for d in ds:
        npv = n_t(c, s, p, d)
        nqv = n_t(c, s, q, d)
        if npv is None or nqv is None:
            ok_mono = ok_id = False
            break
        if prev is not None and npv < prev - 1e-9:
            ok_mono = False
        prev = npv
        err = abs((npv + nqv) - (s + c))
        worst_id = max(worst_id, err)
        if err > 1e-8:
            ok_id = False
    diag['monotone'] = ok_mono
    diag['identity_holds'] = ok_id
    diag['worst_id_err'] = worst_id

    # --- count integer levels of n_p crossed in the interior ---
    eps = (DU - DL) / 1e6
    lo0 = DL + eps
    hi0 = DU - eps
    nlo = n_t(c, s, p, lo0)
    nhi = n_t(c, s, p, hi0)
    diag['np_lo'] = nlo
    diag['np_hi'] = nhi
    kmin = int(math.ceil(nlo))
    kmax = int(math.floor(nhi))

    def y_at(t, d):
        g = geom(c, s, t, d)
        return g[5] if g else 0.0

    roots = []
    for k in range(kmin, kmax + 1):
        lo, hi = lo0, hi0
        flo = n_t(c, s, p, lo) - k
        fhi = n_t(c, s, p, hi) - k
        if flo is None or fhi is None or flo * fhi > 0:
            continue  # no crossing of level k inside (should not happen)
        for _ in range(120):
            mid = (lo + hi) / 2
            fm = n_t(c, s, p, mid)
            if fm is None:
                # shrink toward the side with a defined value
                if flo is not None and flo * (0) <= 0:
                    hi, fhi = mid, None
                else:
                    lo, flo = mid, None
                continue
            fm = fm - k
            if flo * fm <= 0:
                hi, fhi = mid, fm
            else:
                lo, flo = mid, fm
        d = (lo + hi) / 2
        yp, yq = y_at(p, d), y_at(q, d)
        YTOL = 1e-7
        if yp > YTOL and yq > YTOL:
            roots.append((k, d, yp, yq))
    diag['k_range'] = (kmin, kmax)
    diag['roots'] = roots
    return len(roots), diag


def main():
    lines = []
    def emit(s=""):
        print(s, flush=True)
        lines.append(s)

    emit("PE620 winner-model term generator (pattern-finder)")
    emit("n_t=[(c-t)beta+(s+t)mu]/pi; valid iff n_p,n_q in Z (mirror pairs),")
    emit("interior d; conjectures tested: n_p+n_q=s+c identity, n_p monotone.")
    emit("=" * 76)

    # oracle check first
    g0, d0 = g_count(16, 5, 5, 6)
    emit("g(16,5,5,6) = %d (oracle 9)  %s   mono=%s ident=%s"
         % (g0, "AGREE" if g0 == 9 else "DISAGREE",
            d0['monotone'], d0['identity_holds']))

    C = {}          # c -> column sum
    G = {}          # n -> cumulative
    rows = []
    NMAX = int(os.environ.get("SEQGEN_NMAX", "40"))
    nbad = 0
    for c in range(16, NMAX + 1):
        tot = 0
        for s in range(5, c - 10):              # s <= c-11 (room for p>=5,q>=6)
            for p in range(5, (c - s - 1) // 2 + 1):  # q = c-s-p >= p+1
                q = c - s - p                   # exact sum s+p+q = c, p<q
                g, diag = g_count(c, s, p, q)
                if g < 0:
                    nbad += 1
                    g = 0
                rows.append((c, s, p, q, g))
                tot += g
        C[c] = tot
    acc = 0
    emit("")
    emit("structural-assumption failures (mono/identity): %d" % nbad)
    emit("")
    emit("per-c column sums C(c) = sum_{s+p+q=c} g  and  cumulative G(n):")
    emit("   c   C(c)     G(c)")
    for c in range(16, NMAX + 1):
        acc += C[c]
        G[c] = acc
        emit("  %3d  %5d  %7d" % (c, C[c], acc))
    emit("")
    emit("G(16)=%d (oracle 9)  G(20)=%d (oracle 205)  %s"
         % (G[16], G[20],
            "AGREE" if (G[16] == 9 and G[20] == 205) else "DISAGREE"))

    # per-tuple rows (for later slicing)
    emit("")
    emit("per-tuple rows c,s,p,q,g (c<=%d):" % NMAX)
    for row in rows:
        emit("  %d %d %d %d %d" % row)

    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    emit("")
    emit("saved %s" % OUT)


if __name__ == "__main__":
    main()