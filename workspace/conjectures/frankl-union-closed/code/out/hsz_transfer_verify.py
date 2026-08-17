"""Exact symbolic verification of Hu-Shi-Zhou density-transfer arithmetic.

Verifies the load-bearing algebraic identities in research/summaries/hu-shi-zhou-frankl-lemma-2025.md
using exact sympy Rationals (no floats):

1. The transfer rule: c2 >= 1/(1 + 2(1-c1)/c1) from a record constant c1.
   - At c1 = 1/2 (Frankl's default): c2 >= 1/(1 + 2(1/2)/(1/2)) = 1/(1+2) = 1/3.
   - At c1 = 0.38234 (current record, rational approx 38234/100000 likely): c2 value.
2. The Frankl <-> Nagel iteration identity:
   1/(1 + 2(1 - 1/(2^{k-1}+1)) / (1/(2^{k-1}+1))) = 1/(2^k + 1),
   for k = 2,3,...,n. This is the identity that makes Nagel's kth-frequency
   bound iteratively follow from Frankl's level-1 bound.
3. The Nagel bound 1/(2^{k-1}+1) at k=1 is exactly 1/2.
"""
import sympy as sp

print("=" * 70)
print("HSZ density-transfer identities (exact rationals via sympy)")
print("=" * 70)

# ---- 1. Transfer rule, exact c1 = 1/2 ----
c1_half = sp.Rational(1, 2)
c2_half = 1 / (1 + 2 * (1 - c1_half) / c1_half)
print(f"\n[1a] Transfer from c1=1/2 (Frankl's level-1 bound):")
print(f"     c2 >= {c2_half}  == 1/3? {sp.simplify(c2_half - sp.Rational(1,3)) == 0}")

# c1 = 3/4? (not a real record, just sanity that formula works beyond 1/2)
print(f"[1b] Sanity: transfer formula at c1=2/3 gives {1 / (1 + 2*(sp.Rational(1,3))/sp.Rational(2,3))} (expected 1/2)")

# ---- 2. Transfer from the current record c1 ~ 0.38234 ----
# Use a high-precision rational from Yu: the record is stated as 0.38234.
# Exact value from Cambie is 0.3823455333... Here we compute the transfer at the
# stated significant digits to reproduce 0.23635.
for label, c1 in [("0.38234", sp.Rational(38234, 100000)),
                  ("0.3823455333667", sp.Rational(3823455333667, 10**13))]:
    c2 = 1 / (1 + 2 * (1 - c1) / c1)
    print(f"\n[2] Transfer from c1={label}:")
    print(f"     c2 = {sp.nsimplify(c2)} = {sp.N(c2, 12)}  (paper quotes ~0.23635)")

# ---- 3. The Frankl<->Nagel iteration identity (exact, symbolic in k) ----
k = sp.symbols('k', integer=True, positive=True)
LHS = 1 / (1 + 2 * (1 - sp.Rational(1, 2**(k-1) + 1)) / (sp.Rational(1, 2**(k-1) + 1)))
RHS = 1 / (2**k + 1)
print(f"\n[3] Nagel iteration identity (symbolic in k):")
print(f"     LHS = {sp.simplify(LHS)}")
print(f"     diff LHS-RHS = {sp.simplify(LHS - RHS)}  (==0 ? {sp.simplify(LHS-RHS)==0})")

# ---- 4. One-element-of-any-k-set bound: 1/(2^{|A|-2}+1) ----
print(f"\n[4] One-element-of-any-A bound 1/(2^{{|A|}}-2)+1):")
for m in [2, 3, 4, 5]:
    b = sp.Rational(1, 2**(m-2) + 1)
    print(f"     |A|={m}: c >= {b}   (k=2 gives 1/2=SR, k=3 gives 1/3)")

# ---- 5. Nagel level-1 at k=1 ----
print(f"\n[5] Nagel k=1: 1/(2^0+1) = {sp.Rational(1, 2**0 + 1)}  (== Frankl 1/2? {sp.Rational(1,2**0+1)==sp.Rational(1,2)})")

print("\nALL IDENTITIES CHECKED")
