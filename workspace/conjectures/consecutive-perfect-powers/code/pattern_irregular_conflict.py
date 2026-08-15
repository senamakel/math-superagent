"""Resolve the conflict: is 911 | num(B_60)?  Is 2903 | num(B_2386)?

Earlier run (pattern_dw_structure.captured.txt) claimed 2903 irregular
index 2386 and 911 irregular index 60.  My modular recurrence says both
regular.  Decide by exact arithmetic on the specific Bernoulli numerators.

sympy.bernoulli(60) and sympy.bernoulli(2386) are exact; we take .p numerator.
Only the two contested primes at their two claimed indices.
"""
import sympy as sp

cases = [(911, 60), (2903, 2386)]
for p, m in cases:
    num = sp.bernoulli(m).p
    print(f"B_{m} numerator magnit log10 ~ {num.bit_length()*0.30103:.1f}")
    print(f"  p={p}: p | num(B_{m})?  {num % p == 0}")

# Also cross-check the index-0 members the older note had as REGULAR (83) and
# re-check the small known irregular primes we already trust (37,59,67)
for p, m in [(83, 32), (37, 32), (59, 44), (67, 58)]:
    num = sp.bernoulli(m).p
    print(f"[cross] p={p}, B_{m}: p | num?  {num % p == 0}")
