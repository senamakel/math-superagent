```approach
id: bombieri-pila-determinant
idea: Bombieri–Pila (1989) determinant method — apply the Bombieri–Pila bound on the number of integer points on an algebraic curve, which gives a bound that depends only on the degree d of the curve (not on its coefficients or genus), to the family of curves C(x,k1)=C(y,k2). This is a genuinely different technique from the algebraic-geometry toolbox because the Bombieri–Pila bound is uniform in the curve within a fixed degree — it does not require genus, Jacobian, or Mordell–Weil information.

mechanism: The Bombieri–Pila theorem (Duke Math. J. 59 (1989), 337-357) states: for a plane algebraic curve C of degree d, the number of integer points (x,y) with |x|,|y| ≤ N on C is at most (c₁ d⁴) N^(1/d) (log N)^(c₂), where c₁,c₂ are absolute constants. More precisely, for d ≥ 2, |C(Z)| ∩ [-N,N]²| ≪_d N^(1/d+ε). The key innovation here is to group all the binomial curves by their degree and apply the bound simultaneously.

For the equation C(x,k1)=C(y,k2), after clearing denominators: k2!·x(x-1)...(x-k1+1) = k1!·y(y-1)...(y-k2+1). This is a plane curve of degree max(k1,k2) in the variables (x,y). The Bombieri–Pila bound applies with N roughly the larger of the two binomial-values (since x ≤ 2a for any representation of a), giving:

For each fixed (k1,k2), the number of integer solutions with C(x,k1)=a ≤ N is at most C(d) N^(1/d) (log N)^c, where d = max(k1,k2).

The crucial point: N(a) sums over pairs (k1,k2) with k1,k2 ≤ log₂(a). So we get:
N(a) ≤ Σ_{k1,k2 ≤ log₂(a)} (number of solutions for that pair)
≤ Σ_{k1,k2 ≤ log₂(a)} C(max(k1,k2)) · a^(1/max(k1,k2)) · (log a)^c

Now notice: for any pair with max(k1,k2) ≥ 3, the term a^(1/3) is small in aggregate, and the sum over all pairs is bounded by a convergent series if the constants can be made uniform. The "boundary" pairs where one of k1,k2 is small (k=1 or k=2) are the ones that contribute a^(1/1)=a and a^(1/2)=√a, which are unbounded — but those correspond to the trivial pair and the triangular column. The combinatorial contribution from all k1,k2 ≥ 3 is controlled by the sum of a^(1/3) terms over ~ (log a)² pairs, which is ~ (log a)² · a^(1/3).

The target partial result: prove that for any a, the number of nontrivial representations with both k1,k2 ≥ 3 is O(1), and all remaining multiplicity comes from the k=1 (trivial) and k=2 (triangular) columns — which are exactly where all known witnesses live. This would reduce the uniform-bound problem to solving C(x,2)=C(y,k) for all k, i.e. the triangular column.

Status: proposed
Precedent:
  - Bombieri–Pila 1989 (Duke Math. J. 59, 337-357): |C(Z)| ∩ [-N,N]²| ≤ c₁ d⁴ N^(1/d) (log N)^c₂ for plane curves of degree d ≥ 2.
  - Pila 1991 (J. Number Theory 38, 73-88): refinement for determinant method — the implied constant is fully effective and can be computed.
  - Walkowiak 2007 (PhD thesis): explicit constant c₁ for the Bombieri–Pila bound.
  - NOT previously proposed for Singmaster; all prior geometric approaches used Faltings/Siegel (ineffective) or elliptic logarithms (per-curve), not uniform-degree bounds.

first-step:
  1. State the Bombieri–Pila theorem exactly with the best available explicit constants (Pila 1991 or Walkowiak 2007).
  2. For the binomial curve after clearing denominators, compute its degree d = max(k1,k2) and verify it satisfies the hypotheses (irreducible, no linear factors giving trivial integer-point families).
  3. Compute the bound explicitly for the small-k regime: a table of Bombieri–Pila bounds for each (k1,k2) pair with 2 ≤ k2 ≤ k1 ≤ 10, as a function of a.
  4. Sum over all pairs with k1,k2 ≥ 3 to verify the convergence of Σ a^(1/max(k1,k2)) and extract a constant.

Speculative: The Bombieri–Pila bound is very weak — N^(1/d) means the bound only becomes useful when d is large relative to log N. For small d (d=2,3,4) with N large, the bound may exceed the trivial bound that a degree-d equation has at most d integer solutions in one variable. The key insight is that the bound is uniform across curves of a given degree, so it couples the ~(log a)² equations together. However, the exponent a^(1/3) for d=3 still grows with a, and the sum over ~(log a)² pairs of a^(1/3) terms is asymptotically ~(log a)² a^(1/3), which goes to infinity with a — not O(1). So the approach needs an additional argument: the degree for most contributing pairs is substantially larger than 3 (since small-k2 contributions are the k2=2 column which is the worst case), AND the Bombieri–Pila constant may be tiny enough that the sum converges. This is speculative and needs checking.
```