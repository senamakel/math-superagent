"""Clean check: does the published 'open degrees <= 100' list (Castryck et al
2012, eq 6.5) equal EXACTLY the set of n in (8,100] with n != 12 NOT covered by
any settled char-0 family?

Settled families (char 0), each n = m * p^k with m its multiplier:
  m=1: p^k                  (Graf-von-Bothmer 2007)             no exclusions
  m=2: 2*p^k                (Graf-von-Bothmer 2007)             no exclusions
  m=3: 3*p^k, p != 2        (Draisma-de Jong)
  m=4: 4*p^k, p not in {3,5,7}
  m=5: 5*p^k, p not in {2,3,7,11,131,193,599,3541,8009}
  m=6: 6*p^k, with bad-prime exclusions for degree 6 (list unheld -> can't
       decide exactly; we mark 6p^k as 'candidate' and report separately)
  m=7: 7*p^k, same caveat
  plus: n <= 8 (Diaz-Toca & Gonzalez-Vega), n = 12 (Castryck 2012).

We report: for each published-open n, WHICH families (if any) exclude it, and
whether the published list agrees with '3/4/5 + p^k + 2p^k' coverage.
"""
from sympy import isprime, factorint

def is_prime_power(n):
    f = factorint(n)
    return len(f) == 1

def prime_power_base(n):
    """Return (p, k) if n = p^k, else (None, None)."""
    f = factorint(n)
    if len(f) == 1:
        p = list(f)[0]
        return p, f[p]
    return None, None

EXCL5 = {2, 3, 7, 11, 131, 193, 599, 3541, 8009}
EXCL4 = {3, 5, 7}
EXCL3 = {2}

def mult_method(n):
    """Return a list of settled-family representations of n, or why not."""
    ways = []
    # m=1: prime power
    p, k = prime_power_base(n)
    if p is not None:
        ways.append(f"p^k (p={p})")
    # m=2
    if n % 2 == 0 and is_prime_power(n // 2):
        ways.append(f"2*p^k (p={prime_power_base(n//2)[0]})")
    # m=3
    if n % 3 == 0 and is_prime_power(n // 3):
        p = prime_power_base(n // 3)[0]
        if p not in EXCL3:
            ways.append(f"3*p^k (p={p})")
    # m=4
    if n % 4 == 0 and is_prime_power(n // 4):
        p = prime_power_base(n // 4)[0]
        if p not in EXCL4:
            ways.append(f"4*p^k (p={p}, 4*p^k only good when p not in {{3,5,7}})")
    # m=5
    if n % 5 == 0 and is_prime_power(n // 5):
        p = prime_power_base(n // 5)[0]
        if p not in EXCL5:
            ways.append(f"5*p^k (p={p})")
    return ways

def covered_no67(n):
    """Covered by p^k, 2p^k, 3p^k, 4p^k, 5p^k families (m <= 5), or n<=8/n=12."""
    if n <= 8 or n == 12:
        return True
    return len(mult_method(n)) > 0

published_open = [20, 24, 28, 30, 35, 36, 40, 42, 45, 48, 55, 56, 60, 63, 66,
                  70, 72, 77, 78, 80, 84, 88, 90, 91, 98, 99, 100]

print("=== Predicted open (no 6/7 family) vs published ===")
pred = [n for n in range(9, 101) if n != 12 and not covered_no67(n)]
print("predicted open (m<=5 families):", pred)
print("published open          :", published_open)
print("pred == published?", pred == published_open)

only_in_pred = [n for n in pred if n not in published_open]
only_in_pub  = [n for n in published_open if n not in pred]
print("\nIn predicted but NOT published (would need 6/7 to close):", only_in_pred)
print("In published but NOT predicted (covered by m<=5 but listed open):", only_in_pub)

print("\n=== For each published-open n: how is it excluded / or why uncovered ===")
for n in published_open:
    ways = mult_method(n)
    s6 = "6*p^k candidate" if (n % 6 == 0 and is_prime_power(n // 6)) else ""
    s7 = "7*p^k candidate" if (n % 7 == 0 and is_prime_power(n // 7)) else ""
    tag = ""
    if n % 5 == 0 and is_prime_power(n // 5):
        p = prime_power_base(n // 5)[0]
        if p in EXCL5:
            tag += f" [5*p^k excluded: p={p} is bad for 5]"
    if n % 4 == 0 and is_prime_power(n // 4):
        p = prime_power_base(n // 4)[0]
        if p in EXCL4:
            tag += f" [4*p^k excluded: p={p}]"
    if n % 3 == 0 and is_prime_power(n // 3):
        p = prime_power_base(n // 3)[0]
        if p in EXCL3:
            tag += f" [3*p^k excluded: p={p}]"
    print(f"  n={n:3d}: came-from={ways or 'NOTHING(m<=5)'}  {s6} {s7}{tag}")
