# UC via the entropy–coupling method — iid sub-instance

Sub-instance of `G-coupling-half` on the iid coupling class. **Refuted**: this
is the exact falsehood of Gilmer's "Conjecture 1". Recorded so no later turn
re-poses the entropy reduction at the iid class.

```skeleton
goal: For every distribution μ on {0,1}^n with H(μ) > 0 and
       max_i Pr_{A∼μ}[A_i=1] < 1/2, the iid coupling (A,B independent, both ∼μ)
       satisfies H(A∨B) > H(A).   [Gilmer's "Conjecture 1"]
implies: this is the sub-instance of G-coupling-half obtained by restricting the
  coupling class to the independent product coupling; if it held it would prove
  UC, but it is false, so the surviving gap must use a dependent class.
status: refuted
rests-on: ellis-gilmer-conjecture-refuted, iid-barrier-exact, ahs-barrier-3-minus-rt5-over-2
killed-by: ellis-gilmer-conjecture-refuted — counterexample on n=2
  (p(∅)=p({1,2})=x, p({1})=p({2})=1/2−x with x=0.3, then a perturbation with
  marginals < 1/2) keeps the iid-OR LHS < 0; iid-OR entropy in fact certifies
  nothing above (3−√5)/2 (iid-barrier-exact, ahs-barrier-3-minus-rt5-over-2).
```

```gap
id: G-iid-half
lemma: For every distribution μ on {0,1}^n with H(μ) > 0 and
       max_i Pr_{A∼μ}[A_i=1] < 1/2, the iid coupling satisfies H(A∨B) > H(A).
       [Gilmer Conjecture 1 — FALSE]
status: refuted
discharged-by: ellis-gilmer-conjecture-refuted (n=2 counterexample;
  also Sawin arXiv:2211.11504, Liu arXiv:2306.08824); the iid-OR method is
  capped at (3−√5)/2 (iid-barrier-exact, ahs-barrier-3-minus-rt5-over-2).
next: none — dead end. Any entropy proof of UC must use a dependent coupling.
```