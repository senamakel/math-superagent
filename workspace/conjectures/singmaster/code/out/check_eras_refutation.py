"""Verify the decisive numerical facts for grounding/refuting the three candidates:

1. erdos-selfridge-structural: the premise 'for every k>=2 there is a prime p>k
   with exponent exactly 1 in (n+1)...(n+k)' is FALSE for k=2: find n with
   (n+1)(n+2) having no prime > 2 to exponent 1. (The theorem only gives p>=k
   with exponent not divisible by l, and the exponent-1 statement is an open
   conjecture for k>=4.)

2. bombieri-pila-determinant: the naive Bombieri-Pila application with box
   [1,a]^2 gives ~ (log a)^{O(d)} a^{1/d} per curve of degree d, summed over
   pairs with 3 <= k1,k2 <= log2 a. Show this is much worse than the trivial
   bound N(a) <= O((log a)^2) (each fixed-k equation C(n,k)=a is a degree-k
   polynomial with <= k integer roots). Print the comparison for sample a.

3. hypergeometric-wz-bijection: verify C(15,5)=C(14,6)=3003 equals the equal
   products form (sanity check for the witness) and that the shared large
   primes just sit inside both blocks - no structural restriction beyond the
   coincidence itself.
"""
from sympy import binomial, factorint

print("=== 1. Erdos-Selfridge k=2 exponent-1 prime ===")
fails = []
for n in range(1, 200):
    prod = (n + 1) * (n + 2)
    fac = factorint(prod)
    has_p_gt_2_exp1 = any(p > 2 and e == 1 for p, e in fac.items())
    if not has_p_gt_2_exp1:
        fails.append((n, prod, fac))
print(f"n in [1,200) with (n+1)(n+2) having NO prime > 2 to exponent 1: {len(fails)}")
for n, prod, fac in fails[:8]:
    print(f"  n={n}: (n+1)(n+2)={prod} = {fac}")
print("First such: n=7 gives 8*9=72=2^3*3^2 -- no prime > 2 with exponent 1.")

print()
print("=== 2. Bombieri-Pila vs trivial bound ===")
from math import log, floor


def log2(x):
    return log(x) / log(2)


def trivial_bound(a):
    """Each k <= log2(a): C(n,k)=a is degree-k poly in n, at most k integer
    roots (plus the trivial C(a,1) pair). Sum k over k=1..floor(log2 a)."""
    K = floor(log2(a))
    return sum(k for k in range(1, K + 1)) + 2  # +2 for trivial pair under both-halves conv


def bp_smallest_term(a):
    """Smallest Bombieri-Pila-type term for pairs with max(k1,k2)>=3:
    (log a)^{O(3)} * a^{1/3} times number of pairs with max=3 (~5)."""
    K = floor(log2(a))
    pairs_max3 = 5 if K >= 3 else 0  # (2,3),(3,2),(3,4),(4,3),(3,3)-ish, minus diagonal
    return pairs_max3 * (a ** (1.0 / 3.0)) * (log(a)) ** 2  # crude (log a)^{O(3)}


for a in [3003, 10**6, 10**12, 10**18, 10**30]:
    print(f"a={a:>12}: trivial N(a)<=O((log a)^2) ~ {trivial_bound(a):>8}, "
          f"BP-degree3 term ~ {bp_smallest_term(a):>14.3e} (worse by "
          f"{bp_smallest_term(a)/max(1,trivial_bound(a)):.2e}x)")

print()
print("=== 3. Witness 3003 equal-products alignment ===")
print(f"C(15,5) = {binomial(15, 5)}, C(14,6) = {binomial(14, 6)}")
A = 15 * 14 * 13 * 12 * 11
B = 14 * 13 * 12 * 11 * 10 * 9
print(f"A={A}, B={B}, A*6!={A*720}, B*5!={B*120}, equal: {A*720 == B*120}")
print(f"factor A: {factorint(A)}")
print(f"factor B: {factorint(B)}")
print("primes > 6 in A: {p for p,e in factorint(A).items() if p>6} =",
      {p for p, e in factorint(A).items() if p > 6})
print("prime-exponents > 6 in B:",
      {p: e for p, e in factorint(B).items() if p > 6})