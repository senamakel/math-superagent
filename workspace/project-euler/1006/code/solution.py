"""Project Euler 1006 — mechanical-word construction, phases 1..4.

Follows the [steering:redirect] correction in CONTEXT.md: the slope of the
mechanical word is a = m/N with N = |S_n| = fib(n+2) and m = #ones(S_n) =
fib(n) (n minimal with fib(n+2) > k), i.e. the density of ones ~ 1/phi^2
~ 0.382.  This is NOT F(n-1)/F(n) ~ 0.618 (that is the binary complement and
does NOT reproduce the factor set — checked and rejected).

Definitions (all exact integer / Fraction arithmetic, no floats):
  S_0='0', S_1='01', S_n = S_{n-1}S_{n-2}.  len(S_n)=F_{n+2}, ones(S_n)=F_n.
  For length k with n minimal s.t. F_{n+2} > k, slope a = F_n/F_{n+2}.
  Cut the unit circle at the k+1 points p_j = frac(-j*a), j=0..k, take the
  midpoint x_m of each of the k+1 cyclically consecutive arcs.
  digit_j(x) = floor(x+(j+1)a) - floor(x+j a), j=0..k-1.
  v(x) = sum_j digit_j * 10^(k-1-j), telescoped to
        floor(x+ka) - 10^(k-1) floor(x) + 9 sum_{j=1}^{k-1} 10^(k-1-j) floor(x+j a).
  Psi(k) = sum_{m=0}^{k} v(x_m)^2.

Phases (per the redirect):
  P1: the produced word multiset EQUALS brute distinct length-k factors, k=1..150.
  P2: Psi_direct = sum_m v(x_m)^2 == brute Psi, exact for k=1..60, mod M 61..150.
  P3: C(j,jp)=sum_m digit_j digit_jp == A(jp-j), A(d)=max(0,m-t)+max(0,m-(N-t)),
      t=(d*m) mod N, all 0<=j<=jp<=k-1, k=1..150.  Then Psi == sum_d A(d) W(d) mod M.
  P4: Psi(k) mod M for k=10^4 and 10^6 via the one-dimensional (phase-3) sum,
      recorded as anchors for the future O(log) universal-Euclidean method.
      (NOT the m=0..k sum at 10^18 — the redirect forbids it.)
"""

from fractions import Fraction

M = 101001001

# ---------------------------------------------------------------------------
# Fibonacci arithmetic
# ---------------------------------------------------------------------------

def fib_list(Nmax_index):
    """F_0..F_N where F_0=0,F_1=1.  Index limit Nmax_index inclusive."""
    out = [0, 1]
    while len(out) <= Nmax_index:
        out.append(out[-1] + out[-2])
    return out


def slope_for(k, fibs):
    """Return (a, n) with n minimal such that F_{n+2} > k and a = F_n/F_{n+2}."""
    n = 0
    while True:
        N = fibs[n + 2]
        if N > k:
            return (Fraction(fibs[n], fibs[n + 2]), n, fibs[n], fibs[n + 2])
        n += 1


def frac(r):
    """Fraction r mod 1 in [0,1).  r may be any Fraction."""
    return r - (r.numerator // r.denominator)


def arc_midpoints(k, a):
    """The k+1 arc midpoints x_m (Fractions in [0,1)) from points frac(-j a)."""
    pts = sorted(frac((-j) * a) for j in range(k + 1))
    xs = []
    for i in range(k):
        xs.append((pts[i] + pts[i + 1]) / 2)
    w = (pts[k] + pts[0] + 1) / 2          # wrap arc, going the short way
    if w >= 1:
        w -= 1
    xs.append(w)
    return xs


def digit(x, j, a):
    """digit_j(x) = floor(x+(j+1)a) - floor(x+j a)."""
    return ((x + (j + 1) * a).numerator // (x + (j + 1) * a).denominator
            - (x + j * a).numerator // (x + j * a).denominator)


def word_from_arc(x, k, a):
    """Length-k word (as digits list) for arc midpoint x."""
    return [digit(x, j, a) for j in range(k)]


def v_telescoped(x, k, a):
    """v(x) = floor(x+ka) - 10^(k-1) floor(x) + 9 sum_{j=1}^{k-1} 10^(k-1-j) floor(x+j a)."""
    fl = lambda r: r.numerator // r.denominator
    s = fl(x + k * a) - 10 ** (k - 1) * fl(x)
    for j in range(1, k):
        s += 9 * 10 ** (k - 1 - j) * fl(x + j * a)
    return s


def v_direct(x, k, a):
    """v(x) = sum_j digit_j 10^(k-1-j) (direct; cross-check of telescoping)."""
    return sum(digit(x, j, a) * 10 ** (k - 1 - j) for j in range(k))


def psi_direct(k, a):
    """Psi(k) = sum_{m=0}^{k} v(x_m)^2 by the telescoped form."""
    xs = arc_midpoints(k, a)
    return sum(v_telescoped(x, k, a) ** 2 for x in xs)


# ---------------------------------------------------------------------------
# Brute oracle
# ---------------------------------------------------------------------------

def fib_word(min_len):
    a, b = '0', '01'
    while len(b) < min_len:
        a, b = b, b + a
    return b


def distinct_factors(word, k):
    return {word[i:i + k] for i in range(len(word) - k + 1)}


def psi_brute(k):
    """Brute Psi(k) as exact int; also returns the distinct factor word set."""
    word = fib_word(4 * k + 8)
    factors = distinct_factors(word, k)
    return sum(int(f) ** 2 for f in factors), factors


# ---------------------------------------------------------------------------
# Phase 3 helpers
# ---------------------------------------------------------------------------

def A_d(d, m, N):
    """A(d) = max(0,m-t) + max(0,m-(N-t)), t=(d*m) mod N."""
    t = (d * m) % N
    return max(0, m - t) + max(0, m - (N - t))


def C_matrix(k, a):
    """C(j,jp) = sum over the k+1 arcs of digit_j(x_m)*digit_jp(x_m)."""
    xs = arc_midpoints(k, a)
    digs = [[digit(x, j, a) for j in range(k)] for x in xs]
    C = [[0] * k for _ in range(k)]
    for row in digs:
        for j in range(k):
            if row[j]:
                for jp in range(k):
                    if row[jp]:
                        C[j][jp] += 1
    return C


def Psi_from_C(C, k):
    return sum(C[j][jp] * 10 ** (2 * k - 2 - j - jp)
               for j in range(k) for jp in range(k))


def W_single(d, k, M):
    """W(d) = 10^(2k-2-d) * sum_{j=0}^{k-1-d} (10^-2)^j  mod M (geometric, O(1))."""
    if d > k - 1:
        return 0
    inv100 = pow(100, -1, M)
    J = k - 1 - d
    geom = (pow(inv100, J + 1, M) - 1) * pow(inv100 - 1, -1, M) % M if inv100 != 1 else (J + 1) % M
    return pow(10, 2 * k - 2 - d, M) * geom % M


def Psi_collapse(k, m, N):
    """Psi(k) mod M via sum_d A(d) W(d), ordered double sum (d=0 once, d>0 twice)."""
    total = A_d(0, m, N) * W_single(0, k, M)
    for d in range(1, k):
        total += 2 * A_d(d, m, N) * W_single(d, k, M)
    return total % M


# ---------------------------------------------------------------------------
# Main / phases
# ---------------------------------------------------------------------------

def run_phases():
    import time
    fibs = fib_list(2000)
    lines = []
    def log(*a):
        s = " ".join(str(x) for x in a)
        print(s)
        lines.append(s)

    log("PE1006 solution.py — mechanical-word construction, phases 1..4 (corrected slope a=m/N).")

    # ---------- Phase 1 + Phase 2 ----------
    log("\n=== Phase 1: construction word set == brute distinct factors ===")
    p1_fail = []
    for k in range(1, 151):
        a, n, m, N = slope_for(k, fibs)
        xs = arc_midpoints(k, a)
        produced = {"".join(str(d) for d in word_from_arc(x, k, a)) for x in xs}
        _, brute_f = psi_brute(k)
        if produced != brute_f:
            p1_fail.append((k, sorted(produced), sorted(brute_f)))
    if p1_fail:
        log("P1 FAIL at k=%d" % p1_fail[0][0])
        log("  produced=%s" % (p1_fail[0][1],))
        log("  brute   =%s" % (p1_fail[0][2],))
    else:
        log("P1 PASS: construction word set == brute distinct factors for all k=1..150.")

    log("\n=== Phase 2: Psi_direct (telescoped v) vs brute Psi ===")
    p2_fail = []
    for k in range(1, 61):
        a, n, m, N = slope_for(k, fibs)
        d = psi_direct(k, a)
        b, _ = psi_brute(k)
        if d != b:
            p2_fail.append((k, d, b))
    for k in range(61, 151):
        a, n, m, N = slope_for(k, fibs)
        if psi_direct(k, a) % M != psi_brute(k)[0] % M:
            p2_fail.append((k, psi_direct(k, a) % M, psi_brute(k)[0] % M))
    if p2_fail:
        log("P2 FAIL first at k=%d direct=%s brute=%s" % p2_fail[0])
    else:
        log("P2 PASS: exact for k=1..60, mod M for 61..150.")

    # ---------- Phase 3 ----------
    log("\n=== Phase 3: C(j,jp)==A(jp-j) and Psi==sum A(d)W(d) mod M ===")
    p3_fail = []
    p3_wfail = []
    for k in range(1, 151):
        a, n, m, N = slope_for(k, fibs)
        C = C_matrix(k, a)
        ok_set = True
        for j in range(k):
            for jp in range(j, k):
                if C[j][jp] != A_d(jp - j, m, N):
                    if not p3_fail:
                        p3_fail.append((k, j, jp, C[j][jp], A_d(jp - j, m, N)))
                    ok_set = False
                    break
            if not ok_set:
                break
        # Psi via collapse
        pc = Psi_collapse(k, m, N)
        if pc != psi_brute(k)[0] % M and not p3_wfail:
            p3_wfail.append((k, pc, psi_brute(k)[0] % M))
    if p3_fail:
        k, j, jp, cc, aa = p3_fail[0]
        log("P3 FAIL: first C!=A at k=%d j=%d jp=%d C=%d A=%d" % (k, j, jp, cc, aa))
    else:
        log("P3 PASS: C(j,jp)==A(jp-j) for all 0<=j<=jp<=k-1, k=1..150.")
    if p3_wfail:
        k, pc, pb = p3_wfail[0]
        log("P3-collapse FAIL at k=%d: Psi_collapse=%d brute=%d" % (k, pc, pb))
    else:
        log("P3-collapse PASS: Psi==sum_d A(d)W(d) mod M for k=1..150.")

    # extra: cross-check collapse vs direct (telescoped) at larger k, no brute
    log("\n=== P3 extra: collapse vs Psi_direct at k=200..600 (no brute) ===")
    xfail = []
    for k in range(200, 601, 50):
        a, n, m, N = slope_for(k, fibs)
        pc = Psi_collapse(k, m, N)
        pd = psi_direct(k, a) % M
        if pc != pd:
            xfail.append((k, pc, pd))
    if xfail:
        log("P3-extra FAIL at k=%d: collapse=%d direct=%d" % xfail[0])
    else:
        log("P3-extra PASS: collapse agrees with Psi_direct mod M at k=200..600.")

    # ---------- Phase 4: anchors at 10^4 and 10^6 ----------
    log("\n=== Phase 4: anchors Psi(k) mod M at k=10^4, 10^6 (O(k) phase-3 sum) ===")
    anchors = {}
    for k in [10000, 10 ** 6]:
        a, n, m, N = slope_for(k, fibs)
        t0 = time.time()
        val = Psi_collapse(k, m, N)
        dt = time.time() - t0
        anchors[k] = val
        log("Psi(%d) mod %d = %d   (a=%d/%d, n=%d, took %.2fs)"
            % (k, M, val, m, N, n, dt))

    log("\nNote: Psi(10^18) mod M requires the O(log) universal-Euclidean method")
    log("(thread G4); the naive m=0..k sum is forbidden at 10^18 by the redirect.")
    log("The Phase-4 anchors above are what that method must reproduce.")

    with open("code/out/solution_checks.md", "a") as f:
        f.write("\n\n---\n\n" + "\n".join(lines) + "\n")
    return anchors


if __name__ == "__main__":
    run_phases()
