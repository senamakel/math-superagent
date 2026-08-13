```approach
idea: Finite-difference descent — use the discrete derivative identity ΔC(n,k) = C(n,k-1) (where Δf(n) = f(n+1)-f(n)) to convert the equality C(x,k1) = C(y,k2) into a tower of equalities on lower rows. Repeated application forces a structure on (x,k1) and (y,k2) that severely restricts the possibilities.

mechanism: The binomial coefficient C(n,k) as a function of n is the unique degree-k polynomial with leading coefficient 1/k! and roots 0,1,...,k-1. Its k-th finite difference is identically 1/k!; its (k-1)-st finite difference is linear. Now, C(x,k1) = C(y,k2) = a. Apply the forward difference operator Δ_x to both sides, where Δ_x acts on the variable x. Since the RHS does not depend on x, Δ_x(C(y,k2)) = 0. Meanwhile Δ_x(C(x,k1)) = C(x,k1-1). So C(x,k1-1) = 0, which forces x ∈ {0,1,...,k1-2} — but those are exactly the roots where C(x,k1) = 0, not a. Wait — this reasoning is too naive because Δ_x acts on the *equation* C(x,k1)-a = 0, not on C(x,k1) alone. Let me be more careful.

The correct setup: For each representation (n,k) of a, we have a point on the curve C(n,k)=a. Consider the *polynomial* P_k(T) = C(T,k) - a, of degree k in T. Its roots are the n-values with C(n,k)=a. If a has many representations with the same k, P_k has many integer roots. More interesting: if a has representations with *different* k values, then consider the *set* of polynomials {P_k(T) = C(T,k) - a : a fixed, varying k}. For each such k where a occurs, P_k has at least one integer root n_k.

The key structural observation: the polynomials P_k(T) for varying k are NOT independent. They satisfy the Pascal recurrence: C(T,k) = C(T-1,k) + C(T-1,k-1). Hence P_k(T) = P_k(T-1) + C(T-1,k-1). And C(T-1,k-1) = P_{k-1}(T-1) + a.

Now take two representations (x,k1) and (y,k2) of a with k1 > k2. Apply Pascal's rule repeatedly: C(x,k1) = C(x-1,k1) + C(x-1,k1-1) = C(x-2,k1) + C(x-2,k1-1) + C(x-1,k1-1) = ... After k1-k2 steps of expansion, every term on the RHS is of the form C(something, ≤k2). Since the total sum equals a = C(y,k2), we get:

C(y,k2) = sum of binomial coefficients with second argument ≤ k2, evaluated at integers near x.

This is a *linear relation* among binomial coefficients with bounded second index. Such relations are highly constrained: if the sum involves terms from rows that are far apart, the binomial coefficients grow exponentially in the row index for fixed column, forcing most terms to be zero or the rows to be close.

The concrete first computation: For the witness 3003 = C(15,5) = C(14,6), expand C(14,6) down to column 5: C(14,6) = C(13,6) + C(13,5). Then C(15,5) - C(13,5) = C(13,6). But C(15,5) - C(13,5) = C(14,5) + C(13,4) (by Pascal twice). So C(13,6) = C(14,5) + C(13,4). This is a nontrivial identity constraining the 3003 representations.

The mechanism in general: given representations (x,k) and (y,l) with k > l, expanding C(x,k) down to level l via the Pascal recurrence yields a decomposition of C(y,l) as a sum of binomial coefficients at level ≤ l. The number and magnitude of terms in this expansion is controlled by k-l and x. If k is much larger than l, the expansion forces C(y,l) to be a sum of many terms, which by size considerations can only happen if x and y are close — giving a "gap" condition that bounds how different the column indices of different representations of the same a can be.

status: proposed
first-step: For the witness set (3003 and the six N=6 values), expand each representation with the largest column index down to the level of the representation with the smallest column index using Pascal's rule. Count the number of terms and their magnitudes. Then formulate a general lemma: if C(x,k) = C(y,l) with k > l, then after expanding C(x,k) to level l, the sum representation forces |x-y| ≤ some function of k-l. Test this against all known witnesses.
```
