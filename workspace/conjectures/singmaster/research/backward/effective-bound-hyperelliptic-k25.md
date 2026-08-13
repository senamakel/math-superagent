```skeleton
goal: An explicit effective bound with a computed constant on the integral solutions of C(x,2)=C(y,k) for a fixed hyperelliptic pair, stated with its k-dependence (GOAL.md partial-result deliverable).
implies: The pair {2,k} has genus floor((k-1)/2) (superelliptic-genus-formula), so the curve is hyperelliptic with RHS C(y,k) of degree k. For k=5 the genus is 2, where BMSST's completely-explicit bound applies once (i) a rational point and a Mordell-Weil basis of the Jacobian are exhibited, and (ii) Matveev's constants for the resulting linear form are evaluated. The explicit log|x| bound then determines all integral solutions, reproducing the known complete list for (2,5). For k >= 7 the genus is >= 3, where canonical-height-difference bounds are unavailable (effective-methods-wall), so the honest scope of a computed constant is k in {5,6} — both genus 2, both already solved; this skeleton pins down the computation that makes the constant explicit rather than cited.
status: live
rests-on: superelliptic-genus-formula, bmsst-hyperelliptic-effective-method, effective-methods-wall, matveev-2000-explicit-constants-primary
```

```gap
id: G-matveev-kummer-check
lemma: For the linear form in two logarithms arising from the (2,5) reduction (BMSST's reduction of C(x,2)=C(y,5) to a hyperelliptic integral-point problem), the Kummer condition [K(sqrt(alpha_1),...,sqrt(alpha_n)):K] = 2^n holds with K=Q, and the heights A_j are specified under Matveev's logarithm-heights convention (not the exponentiated one used by some later authors).
status: open
next: theorem_prover/symbolic_math: write down the exact linear form Lambda for C(x,2)=C(y,5), verify the alpha_j are multiplicatively independent rationals/primes, check [Q(sqrt{alpha_1..alpha_n}):Q] = 2^n, and record which height convention (Matveev's A_j as log-heights) is in force.
```

```gap
id: G-constant-evaluation
lemma: Evaluating Matveev Thm 2.3 (K=Q case, D=rho=1, carrying the 2^n improvement) on the (2,5) linear form yields an explicit numerical log|x| bound with C1, C2, C0', Omega, and B all computed, stated with its k-dependence.
status: open
next: tool_builder: implement Matveev Thm 2.3 for K=Q in exact integer arithmetic, plug in the alpha_j, A_j, b_j from G-matveev-kummer-check, and print the resulting log|x| <= ... bound; cross-check the order of magnitude against BMSST's worked hyperelliptic examples (log x bounds in the 10^263-10^565 range).
```
