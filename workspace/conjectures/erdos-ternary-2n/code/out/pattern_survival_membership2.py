"""Re-verify survival-depth membership with corrected conditions.

Fix 1: digit-free n (m=0,1,4 -> n=0,2,8) survive ALL levels, so survived=True.
Fix 2: cap m (not n) for the big-int window, and use a separate n-cap for f.

Claim (restates the proved sieve bijection for even exponents):
  g(m)=f(2m) satisfies  g(m)>=k  <=>  m mod 3^(k-1) in B_k,  B_k = halved A_k.
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

def check(k, m_lo, m_hi):
    A = survivor_set(k)
    n_hi = 2 * m_hi + 10
    B = set()
    for r in A:
        assert r % 2 == 0
        B.add((r // 2) % (3 ** (k - 1)))
    assert len(B) == 2 ** (k - 1)
    bad = []
    for m in range(m_lo, m_hi):
        n = 2 * m
        f = f_of_n(n) if n < n_hi else None
        # survived: digit-free (n in {0,2,8}) OR f>=k
        survived = (n in (0, 2, 8)) or (f is not None and f >= k)
        membership = (m % 3 ** (k - 1)) in B
        if survived != membership:
            bad.append((m, n, survived, membership, f))
    return bad

def main():
    print("=== corrected check: g(m)>=k <=> m mod 3^(k-1) in B_k ===")
    total = 0
    for k in range(2, 15):
        m_hi = min(2 * 3 ** (k - 1), 2500)
        bad = check(k, 0, m_hi)
        total += len(bad)
        print(f"k={k:3d} |B_k|={2**(k-1):5d}  m<{m_hi:5d} mismatches={len(bad)}"
              + (f"  {bad[:6]}" if bad else ""))
    print("TOTAL mismatches:", total)
    if total == 0:
        print("=> restatement holds exactly over all k,m tested.")

if __name__ == "__main__":
    main()
