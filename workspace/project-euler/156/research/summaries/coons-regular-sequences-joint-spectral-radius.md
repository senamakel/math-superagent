# Michael Coons — "Regular Sequences and the Joint Spectral Radius"

**Source:** arXiv:1511.07535v1 [math.CO], 24 Nov 2015 (final revision Feb 2018). Full text: `[[coons-regular-sequences-joint-spectral-radius.full]]` — `research/sources/coons-regular-sequences-joint-spectral-radius.full.md`.

## What it establishes

**Setup (Section 1).** For f : Z≥0 → K (K a field of characteristic zero), the *k-kernel* is
Ker_k(f) = { {f(k^ℓ n + r)}_n : ℓ ≥ 0, 0 ≤ r < k^ℓ }. f is *k-regular* iff the K-vector space spanned by Ker_k(f) is finite-dimensional (Allouche–Shallit 1992). A k-regular f has a **linear representation**: there are d×d matrices A_f = {A_0,…,A_{k−1}} and vectors v, w with f(n) = w^T A_{i_0}⋯A_{i_s} v where (n)_k = i_s⋯i_0 (Allouche–Shallit Lemma 4.1). Every k-regular f satisfies f(n) = O(n^c) for some c (Allouche–Shallit Thm 2.10).

**Main theorem (Theorem 1).** The *growth exponent*
GrExp(f) := limsup_{n→∞, f(n)≠0} log|f(n)| / log n
equals **log_k ρ(A_f)**, the base-k logarithm of the *joint spectral radius* of any set A_f of k matrices associated to a *basis* of the K-span of Ker_k(f). (Holds over any Noetherian ring, in particular ℤ.)

**Supporting results.**
- Proposition 4: for A_f from a *spanning* set, |f(n)| ≤ c·n^{log_k(ρ(A_f)+ε)} for all n.
- Proposition 6: for A_f from a *basis*, |f(n)| ≥ c·n^{log_k(ρ(A_f)−ε)} for infinitely many n (Bell–Coons–Hare word method).
- Corollary 7: ρ(A_f) ≤ ρ(B_f) for any representation B_f of f; equality can fail (explicit 2-regular example with ρ(A)=1 < x = ρ(B)).

## Bearing on PE156

- Background/theory tier for the *proposed* approach `research/approaches/regular-sequence-linear-representation.md`: that note proposes building the linear representation of a(n,d) = f(n,d) − n (which is 10-regular) and evaluating fixed points by matrix products. Coons gives the machinery to *classify the growth* of such a sequence — in particular that its growth exponent is log_10 ρ(A_f) — but it is **not** needed for the solver: the run computes f(n,d) with the O(log n) place-value closed form (`G1-digit-count-closed-form`) and bounds solutions by Prop 9.1 (`G2-solution-bound`). The matrix-product evaluator was never implemented; the regular-sequence route is recorded as proposed, not taken.
- The abstract confirms the theoretical underpinning (linear representations exist for the digit-count family) but supplies no bound on the zero set {n : f(n,d)=n} and no per-digit data.

## Does not settle

- Nothing about the fixed-point equation f(n,d)=n: no finiteness, no bound, no solution data. Not an answer source, and not a correctness input for the run's chosen method.

## Caveat

- This summary replaces the previous placeholder digest (the file had not been read into a proper note). The full text is 13 291 characters; everything above is quoted or paraphrased from it.
