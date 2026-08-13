```approach
idea: Legendre-digit-sum functional equations — for C(x,k1) = C(y,k2), the exponent v_p of each prime p in both sides must match. By Legendre's formula, v_p(C(n,k)) = (s_p(k) + s_p(n-k) - s_p(n))/(p-1) where s_p is the sum of base-p digits. Equality of these for all primes p (or at least all p dividing a·k1!k2!) gives a system of simultaneous constraints on the digit-sum functions of x, x-k1, y, y-k2. This is a genuinely additive-combinatorial approach orthogonal to algebraic geometry.

mechanism: For each prime p, Legendre's formula gives:
v_p(C(n,k)) = (s_p(k) + s_p(n-k) - s_p(n)) / (p-1)

where s_p(m) is the sum of digits of m in base p. This is a classical result (Legendre 1808) that follows from counting multiples of p, p^2, etc. in n!.

If C(x,k1) = C(y,k2), then for every prime p:
s_p(k1) + s_p(x-k1) - s_p(x) = s_p(k2) + s_p(y-k2) - s_p(y)

since the (p-1) denominator cancels.

Now, k1 and k2 are FIXED for a given equality. So s_p(k1) and s_p(k2) are known constants for each p. The unknowns are x and y (and hence x-k1, y-k2). The digit-sum function s_p has the property that for numbers in a bounded range, it is approximately (p-1)/2 times the number of digits. More importantly, s_p(m) changes predictably under addition: for m up to n, the average of s_p(m) is about (p-1)/2 · log_p(n).

The crucial new angle: Fix a candidate value a. For each possible k (1 ≤ k ≤ log_2 a), define n_k as the unique n with C(n,k) = a (if it exists — there are at most k such n per k by degree). For each such pair (n_k, k), the digit-sum functional s_p(n_k) - s_p(n_k - k) is forced to equal s_p(k) - (p-1)·v_p(a). This is a constraint that n_k must satisfy for EVERY prime p dividing a·k!.

Now, s_p(n) - s_p(n-k) for fixed k has a specific behavior as a function of n: it depends on whether the subtraction n-k crosses base-p digit boundaries. This is essentially a "carry" function. The key observation: if n is much larger than k, the subtraction n-k rarely causes many carries, so s_p(n) - s_p(n-k) ≈ s_p(k) for most p. The deviation from s_p(k) measures the carries.

For C(n,k) = a, we have:
s_p(n) - s_p(n-k) = s_p(k) - (p-1)·v_p(a)

The RHS is independent of n! So for each p dividing a, the carry pattern in the subtraction n-k (base p) is fully determined by a and k. This means: for a given a and k, the possible n are those for which the base-p subtraction n-k produces EXACTLY the specified number of carries (equal to s_p(k) - (p-1)·v_p(a) - s_p(n) + s_p(n-k), which rearranges to a carry count).

Now intersect over all primes p|a: n must satisfy simultaneous carry conditions in every base p. This is the ADELIC digit constraint, not the failed single-prime Lucas approach. The simultaneous constraint across MANY primes is what the refuted Kummer-Lucas approach missed — it looked at one prime at a time and found large classes; the intersection across all primes dividing a is exponentially more restrictive.

Concrete target: Prove that for a given a, the number of k for which there exists an n satisfying the simultaneous digit constraints (for all p dividing a·k!) is bounded by an absolute constant. The digit constraints are "almost" independent across primes, so the intersection cardinality should drop exponentially with the number of prime factors of a.

status: proposed
first-step: Write a program that, for each witness value a (3003, 120, 210, 1540, 7140, 11628, 24310), computes all (n,k) with C(n,k)=a by the standard binary-search method, then for each such (n,k) and for each prime p dividing a·k!, computes s_p(n) - s_p(n-k) and verifies the Legendre equality. Then for each k, characterizes the set of n (in some range) that satisfy the carry constraint for a single prime p, and measures how the intersection shrinks as more primes are added.
```
