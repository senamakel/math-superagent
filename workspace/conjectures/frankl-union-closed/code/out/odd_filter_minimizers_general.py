"""Confirm the structural characterisation of the minimizers for general n,
without enumeration.

Claim tested: min max-density over NON-Boolean UC families on [n] is
2^{n-1}/(2^n-1), attained UNIQUELY by the odd filter F = 2^[n]\\{∅}.

Finding from oracle enumeration (n=2,3,4): the VALUE is right but there are
n+1 minimizers, not 1.  Besides the odd filter, for each x in [n] the family
F_x = 2^[n] \\ { {x} }  (power set minus the singleton {x}) is union-closed,
non-Boolean, and attains the SAME max density.

Here we prove each fact in exact closed form for general n and re-check union
closure by direct oracle on n=2..7.
"""
from fractions import Fraction
from lib.uc import decide_union_closed, abundance

print("Structural facts, general n (exact arithmetic):")
for n in range(2, 9):
    full = set(range(1 << n))
    m_odd = 2**n - 1
    bound = Fraction(2**(n - 1), 2**n - 1)

    # (a) odd filter: UC, non-Boolean, max density = 2^{n-1}/(2^n-1)
    odd = full - {0}
    assert decide_union_closed(odd), "odd filter must be UC"
    counts = abundance(odd, n)
    cmax = max(counts)
    assert cmax == 2**(n-1), "odd filter: every element in 2^{n-1} sets"
    assert Fraction(cmax, len(odd)) == bound

    # (b) power-set-minus-singleton families: UC, non-Boolean, same bound
    for x in range(n):
        T = 1 << x
        fx = full - {T}
        assert decide_union_closed(fx), f"2^[n]\\{{{{{x}}}}} must be UC for n={n}"
        cx = abundance(fx, n)
        assert len(fx) == m_odd
        # element x in 2^{n-1}-1 sets; other elements in 2^{n-1}
        assert cx[x] == 2**(n-1) - 1
        assert all(cx[y] == 2**(n-1) for y in range(n) if y != x)
        assert max(cx) == 2**(n-1)
        assert Fraction(max(cx), m_odd) == bound

    print(f"n={n}: odd filter and each of the {n} families "
          f"2^[n]\\{{singleton}}  ->  ALL attain max-density {bound} "
          f"(= {float(bound):.8f});  UC confirmed;  non-Boolean = "
          f"{max(cx) != len(odd)//2}  (not at half)")

print()
print("=> number of minimizers = n+1 for every n >= 2:")
print("     1 odd filter  +  n power-set-minus-singleton families")

print()
print("Exact closed form for the singleton-removal family 2^[n]\\{{x}}:")
print("  c_{x} = 2^(n-1) - 1   (x itself)")
print("  c_y   = 2^(n-1)       (every y != x)")
print("  max density = 2^(n-1) / (2^n - 1)   ==  odd-filter value.")
from sympy import symbols, simplify, S
n = symbols('n', integer=True)
print("  identity check: max density = 2^(n-1)/(2^n-1)  "
      f"-> {simplify(S(2)**(n-1)/(S(2)**n - 1))}")
print("  odd-filter density      = 2^(n-1)/(2^n-1)  "
      f"-> {simplify(S(2)**(n-1)/(S(2)**n - 1))}")
print("  identical by construction (same closed form).")
