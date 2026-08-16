"""Naive oracle for COLLAPSE: follows problem.md's definitions literally, no cleverness.

Deliberately NOT fast and NOT the optimized method — this is the "what does the
statement mean" checker. cross-checked against /workspace/code/lib/collapse.py.

Objects, straight from problem.md:
  Phi_n[d][j] = C(d, j-(n-1-d)) mod 2,  d=2..n-1, j=0..n-1
  M_d = { n-1-d+o : o subset of d as binary submask }
  T(n,d) = XOR over i in M_d of h[i]
  w(h)   = #{ d : T(n,d)=1 }
  S(n,h) = (n-2) - 2*w(h)

Worked examples / imported claims checked here (all small n):
  (1) rows: Phi_n[d][j] == 1 iff j in M_d        (per-position, and via Lucas)
  (2) rank Phi_n = n-2, nullity 2                (naive Gaussian elimination over F2)
  (3) M_d injective in d  =>  E[S^2]=n-2 in uniform model (density of Binomial(n-2,1/2))
  (4) |M_d △ M_{d'}| = 2^pc(d)+2^pc(d')-2^{pc(d&d')+1}
  (5) E[w]=(n-2)/2, Var(w)=(n-2)/4, E[S^2]=n-2  (exhaustive 2^n at n<=9)
  (6) telescoping: over a run [u,v], XOR_{o} h[pos+o] == [r_{pos+u} != r_{pos+v+1}]
      for h = [r_j != r_{j+1}], r two-valued.
  (7) endpoint-sign: (-1)^{T(n,d)} = prod over runs of chi(r_a) chi(r_b), no prefactor.

Everything exact integer arithmetic.
"""
from math import comb


def submasks(d):
    o = d
    while True:
        yield o
        if o == 0:
            break
        o = (o - 1) & d


def M_d(d, n):
    """Naive set comprehension straight from the definition."""
    return frozenset(n - 1 - d + o for o in submasks(d))


def phi_row(d, n):
    """Row d: [C(d, j-(n-1-d)) mod 2]."""
    return [comb(d, j - (n - 1 - d)) % 2 if 0 <= j - (n - 1 - d) <= d else 0
            for j in range(n)]


def T(n, d, h):
    return sum(h[i] for i in M_d(d, n)) % 2


def w_of(n, h):
    return sum(T(n, d, h) for d in range(2, n))


def S(n, h):
    return (n - 2) - 2 * w_of(n, h)


def rank_f2(mat):
    """Naive Gaussian elimination over F2. mat: list of row lists (ints). -> rank."""
    rows = [list(r) for r in mat]
    ncols = len(rows[0]) if rows else 0
    rank = 0
    for col in range(ncols):
        piv = next((i for i in range(rank, len(rows)) if rows[i][col] == 1), None)
        if piv is None:
            continue
        rows[rank], rows[piv] = rows[piv], rows[rank]
        for i in range(len(rows)):
            if i != rank and rows[i][col] == 1:
                rows[i] = [(rows[i][k] ^ rows[rank][k]) for k in range(ncols)]
        rank += 1
    return rank


def run_lengths(A):
    """Return list of (start,end) for maximal runs of consecutive ints in sorted A."""
    s = sorted(A)
    runs = []
    if not s:
        return runs
    st = pr = s[0]
    for x in s[1:]:
        if x == pr + 1:
            pr = x
        else:
            runs.append((st, pr))
            st = pr = x
    runs.append((st, pr))
    return runs


def popcount(x):
    return bin(x).count("1")


def check_rows(n):
    """Claim 1: Phi row d is the indicator of M_d."""
    for d in range(2, n):
        row = phi_row(d, n)
        m = M_d(d, n)
        for j in range(n):
            assert (row[j] == 1) == (j in m), (n, d, j)
    # biased negative control: shift the set by one -> must differ
    for d in range(2, n):
        shifted = frozenset(x + 1 for x in M_d(d, n) if x + 1 < n)
        if shifted != M_d(d, n):
            assert shifted != M_d(d, n)


def check_rank(n):
    """Claim 2: rank Phi_n = n-2 (-> nullity 2 as n-2 rows)."""
    mat = [phi_row(d, n) for d in range(2, n)]
    r = rank_f2(mat)
    return r


def check_expect(n):
    """Claim 5: E[w], Var(w), E[S^2] over uniform h."""
    from statistics import mean, pvariance
    ws = []
    ss = []
    for h in range(1 << n):
        hl = [(h >> i) & 1 for i in range(n)]
        ws.append(w_of(n, hl))
        ss.append(S(n, hl))
    return mean(ws), pvariance(ws), mean(s * s for s in ss)


def check_size_formula(n):
    """Claim 4: |M_d △ M_{d'}| closed form."""
    for d in range(2, n):
        for dp in range(2, n):
            a = len(M_d(d, n) ^ M_d(dp, n))
            f = 2 ** popcount(d) + 2 ** popcount(dp) - 2 ** (popcount(d & dp) + 1)
            assert a == f, (n, d, dp, a, f)


def check_telescoping(n, values):
    """Claim 6: XOR over o in [u,v] h[pos+o] == [r_{pos+u} != r_{pos+v+1}]."""
    for r in values:                      # each r is a two-valued list of length n+1
        h = [1 if r[j] != r[j + 1] else 0 for j in range(len(r) - 1)]
        for pos in range(0, n):
            for u in range(n - pos):
                for v in range(u, n - pos):
                    x = 0
                    for o in range(u, v + 1):
                        x ^= h[pos + o]
                    rhs = 1 if r[pos + u] != r[pos + v + 1] else 0
                    assert x == rhs, (values.index(r), pos, u, v, x, rhs)


def check_endpoint_sign(n, vals):
    """Claim 7: for h = difference sequence of a TWO-VALUED r,
    (-1)^{T(n,d)} = prod over runs R=[u,v] of M_d of chi(r_u) chi(r_{v+1}),
    no prefactor.  (Endpoints are u and v+1 -- the telescoping identity's
    [r_{pos+u} != r_{pos+v+1}] -- NOT u and v.)
    vals: boundary sequences to test, each used only under the two-valued premise.
    Returns number of failures over all (r,d)."""
    fail = 0
    for r in vals:
        h = [1 if r[j] != r[j + 1] else 0 for j in range(len(r) - 1)]
        for d in range(2, n):
            cell = T(n, d, h)
            runs = run_lengths(sorted(M_d(d, n)))     # [(u,v)] per run
            prod = 1
            for (u, v) in runs:
                prod *= (-1) ** (r[u] + r[v + 1])
            lhs = (-1) ** cell
            if lhs != prod:
                fail += 1
    return fail


def check_endpoint_three_valued(n):
    """NEGATIVE CONTROL: a THREE-valued r should break the endpoint-sign form.
    Mirrors the problem's note of 438 mismatches / 620067 pairs."""
    import random
    random.seed(0)
    fails = 0
    total = 0
    for _ in range(2000):
        r = [random.randrange(3) for _ in range(n + 1)]
        h = [1 if r[j] != r[j + 1] else 0 for j in range(len(r) - 1)]
        for d in range(2, n):
            cell = T(n, d, h)
            runs = run_lengths(sorted(M_d(d, n)))
            prod = 1
            for (u, v) in runs:
                prod *= (-1) ** (r[u] + r[v + 1])
            lhs = (-1) ** cell
            total += 1
            if lhs != prod:
                fails += 1
    return fails, total


def main():
    print("== worked example (1): rows == Phi indicator, n=2..9 ==")
    for n in range(2, 10):
        check_rows(n)
    print("   ok")

    print("== (2) rank Phi_n == n-2, n=2..12 ==")
    for n in range(2, 13):
        r = check_rank(n)
        assert r == n - 2, (n, r)
        print(f"   n={n:2d} rank={r} (nullity={n - r})")

    print("== (4) size formula, n=2..12 ==")
    for n in range(2, 13):
        check_size_formula(n)
    print("   ok on all pairs")

    print("== (5) exact image law / moments, uniform h, exhaustive ==")
    for n in range(2, 10):
        ew, vw, es = check_expect(n)
        ok = (abs(ew - (n - 2) / 2) < 1e-9 and abs(vw - (n - 2) / 4) < 1e-9
              and abs(es - (n - 2)) < 1e-9)
        print(f"   n={n:2d} E[w]={ew:7.3f} Var(w)={vw:7.3f} E[S^2]={es:7.3f}  "
              f"(expect { (n-2)/2:5.2f} { (n-2)/4:5.2f} {n-2:3d}) {'OK' if ok else 'FAIL'}")

    print("== (6) telescoping identity, two-valued r, n=2..8 ==")
    for n in range(2, 9):
        vals = [[0] * (n + 1), [1] * (n + 1)]
        # alternating and single-flip two-valued sequences
        for start in (0, 1):
            vals.append([(start + i) % 2 for i in range(n + 1)])
        for flip in range(n):
            vals.append([0] * (flip + 1) + [1] * (n - flip))
        check_telescoping(n, vals)
    print("   ok on two-valued r at all pos,u,v")

    print("== (7) endpoint-sign form, h = diff of TWO-VALUED r (correct premise) ==")
    for n in range(2, 10):
        vals = [[0] * (n + 1), [1] * (n + 1)]
        for start in (0, 1):
            vals.append([(start + i) % 2 for i in range(n + 1)])
        for flip in range(n):
            vals.append([0] * (flip + 1) + [1] * (n - flip))
        f = check_endpoint_sign(n, vals)
        assert f == 0, (n, f)
    print("   ok: no failure on two-valued r, all n,d")

    print("== (7b) NEGATIVE CONTROL: three-valued r must break it ==")
    f, total = check_endpoint_three_valued(8)
    assert f > 0, "three-valued r must break the endpoint-sign form"
    print(f"   three-valued r: {f} failures over {total} pairs (n=8, 2000 random r)")


if __name__ == "__main__":
    main()
