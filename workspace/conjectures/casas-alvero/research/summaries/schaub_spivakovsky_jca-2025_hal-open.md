# Schaub & Spivakovsky, "On the Casas-Alvero Conjecture" (J. Commut. Algebra 17(2):199–202, 2025) — FULL REFEREED TEXT

Source: https://hal.science/hal-04341794/document (open HAL deposit, v3, 5 Feb 2025)
Full text: `research/sources/schaub_spivakovsky_jca-2025_hal-open.full.md`
Journal record: DOI 10.1216/jca.2025.17.199, J. Commut. Algebra 17(2):199–202, Summer 2025
(received Nov 2024, accepted Jan 2025). Peer-reviewed; published independently of Ghosh's preprint.

This is the **full refereed text** of a source previously held only as an abstract. It is a
4-page commutative-algebra partial result toward CA, and the cleanest statement in the held
library of the resultant/height reformulation the run's scheme-theoretic method targets.

## The reformulation (Conjectures 1–4, Remarks 2–4)

Let f = x^d + a_1 x^{d−1} + ⋯ + a_{d−1} x (after translating a root to 0, so a_d = 0), char K = 0.
Let H_i(f) be the i-th Hasse derivative, R_i = Res(f, H_i(f)) ∈ K[a_1,…,a_{d−1}]. Then:

- CA ⇔ V(R_1,…,R_{d−1}) = {0} in K^{d−1} (Conjecture 2).
- If K algebraically closed, CA ⇔ √(R_1,…,R_{d−1}) = (a_1,…,a_{d−1}) (Conjecture 3); a_i^N ∈ (R_1,…,R_{d−1}).
- Truth of Conjecture 3 depends only on the characteristic of K (faithfully-flat extension
  argument, Remark 2) — so it is enough to take K = ℂ.
- Equivalences to "R_1,…,R_{d−1} form a regular sequence" / "R_{i+1} is not a zero-divisor mod
  (R_1,…,R_i)" (Remark 4(a),(b)), independent of the numbering of the R_i.

This is precisely the height/regular-sequence picture this run's scheme-theoretic elimination
method is aimed at. It is now published in a peer-reviewed venue — cite it rather than re-derive
the equivalence.

## Main theorem (Theorem 5) — the concrete partial result

**Theorem 5.** For i ∈ {d−3, d−2, d−1}: R_i ∉ √(R_1,…,R̂_i,…,R_{d−1}).

That is, the three highest-order resultants are each NOT in the radical of the ideal generated
by the other resultants. This is a real step toward the regular-sequence / independence claim,
exactly on the three top derivative orders.

## Why the proof is load-bearing for the char-p test

The proof uses **real-rooted polynomials + Rolle's theorem** (Proposition 6: H_1(f) interlaces
the roots of f; Corollary 7: all H_i(f) are real-rooted) and the Draisma–de Jong almost-counterexample
construction (Theorem 9, with the "recycled roots" α_{k_j,m_j}). It shows a contradiction by
root-ordering: if R_i were in the radical, an almost-counterexample of level i would become a true
counterexample, and the first-root recursion forces α_{m,1}(f) ∈ ]0, β^{(m−1)}[ ⊂ ]0,β[, which
cannot be a root of f.

**This proof is analytic/order-based and has NO characteristic-p analogue** — Rolle interlaces
the real roots using the real line, which does not exist over 𝔽_p. This is the same failure mode as
the Gauss–Lucas / convex-hull step this run already located in its root-difference-coloring
approach (`rdc-charp-break`). So Theorem 5 is a genuine char-0 partial result whose proof
necessarily cannot transfer to char p — consistent with CA being false in char p.

Note the "Added in press" line: "In two recent preprints [6] and [7] Soham Ghosh gave a complete
proof of the Casas-Alvero conjecture." — the refereed source itself flags Ghosh's claim but does
not endorse/verify it.

## Role in this run

- States Conjecture 3 (√-equality), the exact regular-sequence reformulation the scheme-theoretic
  elimination method targets, in a refereed venue.
- Theorem 5 is a concrete, verified partial result on the top three resultants — the natural object
  to stress-test or extend (char-p break located: Rolle/real-root ordering).
- Provides the almost-counterexample / Draisma–de Jong theorem with explicit recycled roots as a
  tool for constructing or constraining candidates.
