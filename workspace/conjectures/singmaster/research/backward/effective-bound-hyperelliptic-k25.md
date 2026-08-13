```skeleton
goal: An explicit effective bound with a computed constant on the integral solutions of C(x,2)=C(y,k) for a fixed hyperelliptic pair, stated with its k-dependence (GOAL.md partial-result deliverable).
implies: The pair {2,k} has genus floor((k-1)/2) (superelliptic-genus-formula), so the curve is hyperelliptic with RHS C(y,k) of degree k. For k=5 the genus is 2, where BMSST's completely-explicit bound applies once (i) a rational point and a Mordell-Weil basis of the Jacobian are exhibited, and (ii) Matveev's constants for the resulting linear form are evaluated. The explicit log|x| bound then determines all integral solutions, reproducing the known complete list for (2,5). For k >= 7 the genus is >= 3, where canonical-height-difference bounds are unavailable (effective-methods-wall), so the honest scope of a computed constant is k in {5,6} — both genus 2, both already solved; this skeleton pins down the computation that makes the constant explicit rather than cited.
status: closed (Matveev route refuted — Lambda=0 at root; surviving claim records the correct tool per pair: elliptic-logarithm, effective yes, uniform no)
rests-on: superelliptic-genus-formula, bmsst-hyperelliptic-effective-method, effective-methods-wall, matveev-2000-explicit-constants-primary
surviving: The skeleton established that for the (2,k) hyperelliptic family the effective route is elliptic-logarithm per pair (SDW 1999 Thm B23), NOT Matveev.  Claim: [[effective-hyperelliptic-elliptic-logarithm-per-pair]] — effective: yes (computable constants per (2,k) for k up to where genus-2 BMSST applies); uniform in k: no (per-curve MW basis and height-difference bounds grow with k).  This is a real statement about WHICH tool applies, preventing re-proposal of Matveev here.
```

```gap
id: G-matveev-kummer-check
lemma: For the linear form in two logarithms arising from the (2,5) reduction (BMSST's reduction of C(x,2)=C(y,5) to a hyperelliptic integral-point problem), the Kummer condition [K(sqrt(alpha_1),...,sqrt(alpha_n)):K] = 2^n holds with K=Q, and the heights A_j are specified under Matveev's logarithm-heights convention (not the exponentiated one used by some later authors).
status: refuted
killed-by: The linear form Lambda = ln(3x(x-1)) - ln(y(y-1)(y-2)) is IDENTICALLY ZERO at every solution of C(x,2)=C(y,3) (equal integers have equal prime factorizations), so Matveev Thm 2.2 (Lambda != 0 hypothesis) does not apply.  See claim matveev-2-3-constants-computed (checked, capture code/out/matveev_2_3_constant.captured.txt).  The (2,3) case, the simplest member of the hyperelliptic family, is vacuous for Matveev; the same Lambda=0 problem propagates to every (2,k) pair because both sides compute the same integer a and ln(a/a)=0.  Nonzero forms exist only for differences between distinct collision values (U - V = 6d, d != 0), where constants are effective but astronomically large (log10 y-bound ~10^22 before LLL), and the effective route for d=0 is David's elliptic-logarithm method via SDW 1999 Thm B23 — effective, per-pair, NOT uniform in k.  (Directive 22.)
```

```gap
id: G-constant-evaluation
lemma: Evaluating Matveev Thm 2.3 (K=Q case, D=rho=1, carrying the 2^n improvement) on the (2,5) linear form yields an explicit numerical log|x| bound with C1, C2, C0', Omega, and B all computed, stated with its k-dependence.
status: refuted
killed-by: Depends on G-matveev-kummer-check (refuted — Lambda=0, Matveev does not apply).  The whole Matveev-based (2,k) skeleton is dead at the root.
```
