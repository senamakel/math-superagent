# O'Bryant — On the Sum of the Heights of Sturmian Factors (arXiv:math/0611365)

<!-- source: https://arxiv.org/abs/math/0611365 | full text read 2026-08-19 -->

Full text: `research/sources/oybryant-sum-heights-sturmian-factors.full.md`
(also `research/sources/obryant-sum-heights-sturmian-factors.full.md` — same paper, arXiv spelling variant.)

## What it establishes

**Setup.** F_n(W) = the n+1 distinct length-n factors of a binary Sturmian word W (|F_n(W)| = n+1 for all n). h(w⃗) = height = number of 1's. It suffices to consider characteristic words c_α(n) = ⌊(n+2)α⌋ − ⌊(n+1)α⌋ (Lothaire Thm 2.1.13: every Sturmian word has the same length-n factor set as some c_α).

**The factor parametrisation (used in Lemma 1, verbatim).** Let 0 = π₀ < π₁ < ⋯ < πₙ = the sorted set {0, {−α}, {−2α}, …, {−nα}} — the arc midpoints of the circle cut at the orbit points. Define v_i(x) = ⌊(i+1)α + x⌋ − ⌊iα + x⌋ (the lower mechanical digit) and w_i = (v₀(πᵢ), v₁(πᵢ), …, v_{n−1}(πᵢ)). Then F_n(α) = {w_i : 0 ≤ i ≤ n}, lexicographically ordered. **This is precisely the run's mechanical-word/arc-midpoint construction of the k+1 factors**, in the literature.

**Lemma 1 (exact first-moment formula).** Σ_{w⃗ ∈ F_n(α)} h(w⃗) = B_α(n) + (n+1)⌊nα⌋ + 1, where B_α(k) = #{q : 1 ≤ q < k, {qα} < {kα}} counts "better" denominators of α from below. Proof: h(w_i) = |ℤ ∩ (πᵢ, nα+πᵢ]| ∈ {⌊nα⌋, ⌊nα⌋+1}; exactly B_α(n)+1 of the n+1 factors have the higher weight.

**Lemma 2.** B_α(k) + B_{1−α}(k) = k−1, B_α(1)=0, B_α(2)=1, and for k ≥ 3 the second difference of B_α(k) is given by a 3-case formula in {kα} (the three-distance structure; proof "inspired by Sós's proof of the Three-Gap Theorem").

**Lemma 3.** Parity: B_α(k) even for k odd; B_α(k) ≡ ⌊kα⌋+1 (mod 2) for k even.

**Theorem 1.** Σ_{w⃗ ∈ F_n(W)} h(w⃗) ≡ n (mod 2), independent of the Sturmian word W.

## Why it matters for PE1006

- This is the **only source in the library that proves a formula for a sum over the n+1 factors** of a Sturmian word with the identical mechanical/arc-midpoint parametrisation the run uses. It confirms the factor set {w_i} at intercepts πᵢ is literature-standard, and that the height (number of 1's) takes exactly two consecutive values ⌊nα⌋, ⌊nα⌋+1 with a precise count B_α(n)+1 of the higher ones.
- Ψ(k) is the *decimal second moment* of the same w_i — Σ val(w_i)² where val is the base-10 reading. O'Bryant gives the *first moment of heights*, not the decimal-weighted sum, so it does not solve G4, but it validates the orbit-interval machinery and gives a clean exact identity any Ψ evaluation must be consistent with.
- The B_α quantity (count of q with {qα} < {kα}) is itself a floor-sum-type statistic — the kind of object the universal-Euclidean primitive evaluates in O(log) — suggesting the run's second-moment analogue should be expressible in similar "better-denominator" counts.

## What it does NOT establish

- No decimal weights, no squares, no Ψ(k); the parity theorem is the headline result.
- No O(log) evaluation of anything; the recurrence in Lemma 2 is over k, not a Euclidean recursion.

## Claims anchored here

Corroborates `mechanical-word-digit-rule` (factor set = mechanical words at arc-midpoint intercepts, now with a sourced Lemma-1 parametrisation), `governing-factor-complexity`. No new claim block needed (no Ψ-relevant new theorem).
