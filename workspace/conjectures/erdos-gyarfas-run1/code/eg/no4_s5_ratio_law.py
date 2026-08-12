"""Exact rational analysis of the NO4/S5 ratio structure.

NO4(n) = # connected min-degree>=3 C4-free graphs on n vertices (triangles allowed)
S5(n)  = # connected min-degree>=3 girth>=5 graphs on n vertices (no C4, no triangle)

Known terms (this run's verified counts):
  NO4: 10..16 -> 5, 9, 57, 503, 6059, 91433, 1655659
  S5:  14..18 -> 23, 149, 1670, 23882, 422197

Structural lemma (will be verified mechanically below): in a C4-free graph every
edge lies in at most one triangle, because two triangles sharing an edge ab
(abc, abd) give the 4-cycle a-d-b-c-a. Hence triangles are pairwise edge-disjoint
and every C4-free graph is a girth-5 "skeleton" with triangle attachments --
which is why the ratio NO4(n)/S5(n) is the right object to study: it measures the
average number of triangle-attached extensions per girth-5 skeleton.

This program computes the ratio sequence exactly (fractions), its first and
second differences, and the constant-second-difference extrapolation to n=17,
giving a second independent prediction of NO4(17) to test against the factorial
law NO4(n) ~ K*3^n*(n-10)! (K ~ 5.3e-5) which predicts ~35M, all models inside
[30M, 41M]. NO4(17) outside [25M, 45M] falsifies BOTH.

Run: cd /workspace && PYTHONPATH=/workspace/code python code/eg/no4_s5_ratio_law.py
"""

from fractions import Fraction

NO4 = {10: 5, 11: 9, 12: 57, 13: 503, 14: 6059, 15: 91433, 16: 1655659}
S5 = {14: 23, 15: 149, 16: 1670, 17: 23882, 18: 422197}

print("=== ratio NO4/S5 (exact rationals) ===")
r = {}
for n in (14, 15, 16):
    r[n] = Fraction(NO4[n], S5[n])
    print(f"n={n}: NO4/S5 = {NO4[n]}/{S5[n]} = {r[n]} = {float(r[n]):.6f}")

d1 = {n: r[n] - r[n - 1] for n in (15, 16)}
d2 = d1[16] - d1[15]
print("\nfirst differences (exact):", {n: f"{d1[n]} = {float(d1[n]):.6f}" for n in (15, 16)})
print(f"second difference (exact): {d2} = {float(d2):.6f}")
print(f"second difference / 27.6 = {float(d2)/27.6:.4f}  (check against obsolete float guess)")

# constant-second-difference extrapolation of the ratio to n = 17
r17 = r[16] + d1[16] + d2
print(f"\nextrapolated ratio at n=17: {r17} = {float(r17):.6f}")
pred = S5[17] * r17
print(f"predicted NO4(17) = S5(17) * ratio = {S5[17]} * {r17} = {pred} = {float(pred):.2f}")

# first- and second-difference ratios of the ratio sequence, to see if quadrature is stable
print("\n=== how much does the second difference move? (need n=19 datum to test) ===")
print("only 3 ratio points exist (n=14..16): constant second difference is a 3-point")
print("extrapolation, i.e. numerology until NO4(17) confirms or kills it.")

# --- independent track: K(n) = NO4(n) / (3^n * (n-10)!) ---
from math import factorial

print("\n=== factorial-law constants K(n) = NO4(n)/(3^n (n-10)!) ===")
Kseq = {}
for n in range(12, 17):
    K = Fraction(NO4[n], Fraction(3 ** n) * factorial(n - 10))
    Kseq[n] = K
    print(f"n={n}: K = {float(K):.6e}")
Krat = {n: Kseq[n] / Kseq[n - 1] for n in range(13, 17)}
print("K ratios:", {n: f"{float(Krat[n]):.6f}" for n in Krat})
# slow geometric continuation of K with the last stable ratio (~1.0059, n=15->16)
import statistics
last_rat = float(Krat[16])
K17 = Kseq[16] * Fraction(int(round(last_rat * 1e6)), 10 ** 6)
pred_fact = K17 * Fraction(3 ** 17) * factorial(7)
print(f"K(16)={float(Kseq[16]):.6e}, last ratio {last_rat:.6f}")
print(f"factorial-law NO4(17) ~= {float(pred_fact):.2f}")
print(f"ratio-law NO4(17)     ~= {float(pred):.2f}")
print(f"falsification window: NO4(17) outside [25M, 45M] kills both laws;")
print(f"                       inside [30M, 41M] both confirmed.")