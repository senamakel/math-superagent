"""Bad-prime UPPER BOUND (Schaub-Spivakovsky 2411.13967, Cor 3.2) log10 as
a function of degree n.  The bound B(n) = C! * prod_i binom(i+n-2,n-2) *
binom(d-i+n-2,n-2) is astronomically large, so we compute log10 exactly via
log-gamma (never forming the integer).  d=(n^2-3n+4)/2, C=comb((n^2-n)/2,n-2).
"""
from math import comb, lgamma, log

LN10 = log(10.0)

def lg10_fact(k):
    return lgamma(k + 1) / LN10

def lg10_binom(a, b):
    return (lgamma(a + 1) - lgamma(b + 1) - lgamma(a - b + 1)) / LN10

def bad_prime_bound_log10(n):
    d = (n * n - 3 * n + 4) // 2
    C = comb((n * n - n) // 2, n - 2)
    lg = lg10_fact(C)
    for i in range(1, n):
        lg += lg10_binom(i + n - 2, n - 2)
        lg += lg10_binom(d - i + n - 2, n - 2)
    return lg, C, d

print("n | log10(bad-prime upper bound B(n)) | C | d")
for n in range(3, 13):
    lg, C, d = bad_prime_bound_log10(n)
    print(f"{n:2d} | {lg:12.3f} | {C} | {d}")
