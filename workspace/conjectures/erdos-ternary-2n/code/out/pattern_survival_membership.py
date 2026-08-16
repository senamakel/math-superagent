"""Verify the exact survival-depth membership structure.

Claim: for even n = 2m, let f(n) = first LSB base-3 digit position of 2^n
that is a 2 (the sieve survival depth; n survives level k iff f(n) >= k).
Then
    g(m) := f(2m)   satisfies   g(m) >= k  <=>  m mod 3^(k-1) in B_k
where B_k = { (r/2) mod 3^(k-1) : r in A_k }, |A_k| = 2^(k-1).

This restates the proved sieve bijection for the even exponents: 2m is in
A_k (as a residue mod 2*3^(k-1)) iff m mod 3^(k-1) lies in the halved set.

Verify directly: build A_k by survivor lifting (exact, mod 3^k), halve,
and compare with g(m)>=k from the direct big-int oracle.
"""
from erdos.oracle import digit_free

def f_of_n(n):
    m = 2 ** n
    i = 0
    while m > 0:
        if m % 3 == 2:
            return i
        m //= 3
        i += 1
    return None

def survivor_set(k):
    """A_k as a set of residues mod 2*3^(k-1), by survivor lifting (exact)."""
    A = {0}
    cur = 1
    while cur < k:
        L = 2 * 3 ** (cur - 1)
        next_mod = 3 ** (cur + 1)
        g = pow(2, L, next_mod)
        p3k = 3 ** cur
        Anext = set()
        for r in A:
            base = pow(2, r, next_mod)
            gp = 1
            for j in range(3):
                v = (base * gp) % next_mod
                d = (v // p3k) % 3
                if d in (0, 1):
                    Anext.add(r + j * L)
                gp = gp * g % next_mod
        A = Anext
        cur += 1
    return A

def check(k, mmax):
    A = survivor_set(k)
    period = 2 * 3 ** (k - 1)
    # B_k = residues mod 3^(k-1) of r/2 for r in A (r even).
    B = set()
    for r in A:
        assert r % 2 == 0
        B.add((r // 2) % (3 ** (k - 1)))
    assert len(B) == 2 ** (k - 1), (k, len(B))
    bad = 0
    for m in range(0, mmax):
        n = 2 * m
        f = f_of_n(n) if n < mmax else None
        survived = (f is not None and f >= k)
        membership = (m % 3 ** (k - 1)) in B
        if survived != membership:
            bad += 1
            if bad < 10:
                print(f"  MISMATCH k={k} m={m}: survived={survived} membership={membership}")
    return bad

def main():
    print("=== g(m)>=k <=> m mod 3^(k-1) in B_k  (B_k = halved A_k) ===")
    total_bad = 0
    for k in range(2, 15):
        mmax = 3 ** (k - 1) * 2   # a few periods
        # cap mmax to keep big-int cheap-ish
        mmax = min(mmax, 4000)
        b = check(k, mmax)
        total_bad += b
        print(f"k={k:3d} |B_k|={2**(k-1):6d}  m<{mmax:5d} mismatches={b}")
    print("TOTAL mismatches:", total_bad)
    print("(0 mismatches => the exact membership restatement holds over these k,m)")

if __name__ == "__main__":
    main()
