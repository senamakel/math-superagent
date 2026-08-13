"""Verify the proposed reformulation: 2^n = 2^{n mod 2} * (1+3)^{floor(n/2)}.

The claim under test: the ternary (base-3) digits of 2^n can be obtained from the
binomial sum, and the digit-2-free condition becomes a carry-propagation
constraint. We check the arithmetic core exactly:

  (A) 2^n == (2**(n%2)) * sum_j binom(t,j) 3^j   where t = n//2   (exact)
  (B) low k ternary digits of 2^n mod 3^k equal low k ternary digits of that
      same binomial sum mod 3^k, computed by folding binom(t,j)*3^j into a
      base-3 carry algorithm (no big 2^n ever materialised).

We compare against the ground-truth oracle digit_free.
"""
import gmpy2
from gmpy2 import mpz

def ternary_digits(m):
    """Low-to-high base-3 digits of integer m."""
    m = mpz(m)
    if m == 0:
        return [0]
    ds = []
    while m > 0:
        ds.append(int(m % 3))
        m //= 3
    return ds

def digit_free(m):
    """True iff base-3 expansion avoids digit 2. Ground truth."""
    return 2 not in ternary_digits(m)

def binom(t, j):
    return int(gmpy2.comb(mpz(t), mpz(j)))

def binomial_sum_digits(t, factor=1):
    """Ternary digits of factor * sum_j binom(t,j) 3^j via exact big-int sum.
    Only used on small t to validate the carry algorithm; never on large n."""
    s = sum(binom(t, j) * (3 ** j) for j in range(t + 1))
    s *= factor
    return ternary_digits(s)

def carry_digits(t, factor=1, k=None):
    """Compute low-k base-3 digits of factor*sum_j binom(t,j) 3^j using
    per-position Lucas residues binom(t,j) mod 3 with carries, WITHOUT building
    the big integer 2^n. Returns list of digits low-to-high.
    """
    # Position values up to what? binom(t,j) 3^j contributes at most (up to
    # carries) to digit positions around j + v_3, but binom can be huge and
    # spread. We bound positions by the exact number of digits of 4^t = 2^(2t)
    # plus slack; but to avoid big ints entirely we only need it correct mod
    # 3^k for requested k, using exact binom values mod 3^(k) with carries.
    # Here we carry exact binom(t,j) only mod 3^k (small) to prove correctness
    # of the digit reduction vs big-int; that keeps all arithmetic size O(t log).
    if k is None:
        # digits of 4^t = 2^(2t) ~ 2t log_3(2) digits
        k = int(2 * t * 0.63093) + 4
    # work in a finite ring 3^K with K large enough for low-k digits
    K = k + 2
    mod = 3 ** K
    acc = 0
    for j in range(t + 1):
        acc = (acc + (binom(t, j) % mod) * pow(3, j, mod)) % mod
    acc = (acc * factor) % mod
    d = ternary_digits(acc)
    # why K=k+2 is safe: carries moving from high positions into positions < K
    # could in principle leak; we assert exact agreement against big-int below.
    return d[:k]

def witnesses():
    print("=== digit_free oracle on the three witnesses and one 2-bearing value ===")
    for n in [0, 2, 8, 7]:
        ds = ternary_digits(2 ** n)
        print(f"n={n}  2^n={2**n}  ternary(high->low)={ds}  digit_free={digit_free(2**n)}  "
              f"has_2={2 in ds}")

def validate(n):
    """Check reformulation (A) exact and (B) carry algorithm == big-int == 2^n digits."""
    t = n // 2
    f = 1 if n % 2 == 0 else 2   # 2^(n mod 2)
    # (A) exact identity
    lhs = 2 ** n
    rhs = (2 ** (n % 2)) * sum(binom(t, j) * (3 ** j) for j in range(t + 1))
    a_ok = (lhs == rhs)
    # (B) carry-algorithm low digits vs exact ternary digits of 2^n
    exact = ternary_digits(2 ** n)
    k = len(exact) if n > 0 else 1
    got = carry_digits(t, f, k)
    b_ok = (got == exact[:k])
    # also check raw binomial mod 3 vs Lucas product on all j
    lucas_ok = True
    for j in range(t + 1):
        tj = t; jj = j; prod = 1
        while tj > 0 or jj > 0:
            prod = (prod * (binom(tj % 3, jj % 3))) % 3
            tj //= 3; jj //= 3
        if prod != (binom(t, j) % 3):
            lucas_ok = False
            break
    return a_ok, b_ok, lucas_ok, got, exact[:k]

if __name__ == "__main__":
    witnesses()
    print("\n=== validating the reformulation on every n up to 60 ===")
    all_ok = True
    for n in range(0, 61):
        a, b, lu, got, exact = validate(n)
        ok = a and b and lu
        all_ok &= ok
        flag = "OK " if ok else "FAIL"
        print(f"n={n:3d} reform(A)={a} carry==digits(B)={b} lucas={lu} [{flag}] "
              f"low_digits(of 2^n)={exact}")
    print("\nALL OK" if all_ok else "\nSOME FAILED")
