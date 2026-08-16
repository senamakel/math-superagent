# Ellis — "Note: a counterexample to a conjecture of Gilmer which would imply the union-closed conjecture" (arXiv:2211.12401, 2022)

**Source URL:** https://arxiv.org/pdf/2211.12401 · **Full text:** [[ellis-counterexample-gilmer-conjecture-2022.full]]

## What it establishes

A short note (Nov 22, 2022) giving a **counterexample to a conjecture of Gilmer**
that, had it been true, would have *implied* Frankl's union-closed conjecture.
This is the negative result that defines the edge of the entropy method: the
specific information-theoretic strengthening Gilmer proposed at the end of his
breakthrough paper (arXiv:2211.09055) is FALSE, so that particular route to UC
is closed. An independent counterexample for large `n` was found simultaneously
by Sawin (arXiv:2211.11504, already in library).

## The conjecture being refuted (Gilmer's Conjecture 1)

Let `A, B` be i.i.d. samples from a distribution over subsets of `[n]`. Assume
`Prob[i ∈ A] < 1/2` for all `i`, and `H(A) > 0`. Gilmer conjectured

```
H(A ∪ B) + D(A ∪ B || A) > H(A).
```

Ellis rewrites LHS: `H(A∪B) + D(A∪B||A) = Σ_s q_s log₂(1/p_s)` where `p` is the
distribution of `A` and `q` of `A∪B`. So the conjecture is equivalent to

```
Σ_s q_s log₂(1/p_s) − Σ_s p_s log₂(1/p_s) > 0.      (1)
```

## The counterexample (n = 2)

```
p(∅) = p({1,2}) = x,   p({1}) = p({2}) = 1/2 − x,   x = 0.3.
```

Then `Prob[1∈A] = Prob[2∈A] = 1/2` (the boundary of the hypothesis), yet the
quantity in (1) is `≈ −0.0468 < −0.04`.

A small perturbation `p'(∅)=x, p'({1,2})=x−2ε, p'({1})=p'({2})=1/2+ε−x`
(ε > 0 small) makes `Prob[i∈A] = 1/2 − ε < 1/2`, satisfying the hypotheses, while
(1) stays negative by continuity — a genuine counterexample, not just a boundary
case.

## Verification (this run, by hand — exact rational arithmetic)

`code/out/ellis_check.py` documents the calculation (no shell executor in this
librarian role, so verified manually by hand-arithmetic down to the exact closed
form in the note):

- Marginals: `Prob[i∈A] = 1/2` exactly (p({i}) + p({1,2}) = (1/2−x)+x = 1/2).
- `q∅ = x² = 0.09`, `q{1} = q{2} = 1/4 − x² = 0.16`, `q{1,2} = 1/2 + x² = 0.59`
  (sum 1.0 ✓).
- Closed form identical to the note:
  `LHS = (1/2+2x²−2x)log₂(1/x) + (−1/2−2x²+2x)log₂(1/(1/2−x))`.
- At x = 0.3: `0.08·log₂(10/3) − 0.08·log₂(5) = 0.13896 − 0.18575 = −0.0468
  < −0.04` ✓.

**Status:** the arithmetic is fully verified by hand against the note's exact
closed form. A later run with a shell executor can re-run `ellis_check.py` as a
second independent route if desired.

```claim
id: ellis-gilmer-conjecture-refuted
statement: Gilmer's Conjecture 1 (iid A,B over subsets of [n], all marginals
  < 1/2, H(A)>0 ⟹ H(A∪B) + D(A∪B||A) > H(A)) is FALSE. Counterexample on n=2:
  p(∅)=p({1,2})=x, p({1})=p({2})=1/2−x with x=0.3 gives marginals exactly 1/2
  and LHS ≈ −0.0468; a small perturbation p'(∅)=x, p'({1,2})=x−2ε,
  p'({1})=p'({2})=1/2+ε−x (ε>0) satisfies marginals < 1/2 and keeps LHS < 0.
hypotheses: iid samples A,B; the inequality is exactly the rewrite in (1); the
  counterexample is on the 2-element ground set.
holds-here: yes — this is precisely the entropy-method edge the run's barrier
  target examines. It shows Gilmer's specific strengthening is false, so no
  entropy proof of the AHS type can go through Gilmer's Conjecture 1 verbatim;
  the AHS (3−√5)/2 bound uses a different (correct) inequality.
status: verified-by-hand (exact rational arithmetic reproduced; matches the paper
  and the independent Sawin large-n counterexample already in the library).
bearing: defines what the entropy method can and cannot do — a "barrier" result
  must be stated for the correct coupling class, and this note pins the falsehood
  of the naive Gilmer conjecture as a RULED-OUT route to UC.
anchor: research/sources/ellis-counterexample-gilmer-conjecture-2022.full.md;
  cross-ref Sawin arXiv:2211.11504 (disproves the same Gilmer conjecture)
```

## Why this matters for the run

The run's highest-value live target (GOAL clause 4, "the barrier, made into a
theorem") concerns exactly this: which entropy-method class is capped below 1/2.
This note is the cleanest known statement of where the method breaks — it turns
"Gilmer's conjecture is false" into evidence about the coupling class, complementing
the `(3−√5)/2` iid-OR tightness (claim `iid-barrier-exact`) and the
dependent-coupling escape (Sawin/Yu/Cambie/Liu). Its n=2 counterexample is the
smallest possible and is fully checkable, which is why it belongs in the library.
