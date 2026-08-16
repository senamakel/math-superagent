# CORRECTION — Bagchi, "On strongly regular graphs with mu <= 2" (2006)

<!-- source: correction record.

Original error: the librarian guessed arXiv id math/0512558 for "Bagchi, On
strongly regular graphs with mu<=2", but math/0512558 is "On complete affine
structures in Lie groups" by V. M. Gichev — a pre-Lie/left-symmetric algebra
paper, unrelated to strongly regular graphs. THAT CONTENT IS NOT RELEVANT and
has been removed from this record. Do not cite arXiv:math/0512558 for
graph-theoretic content. -->

## The real paper

Bhaskar Bagchi, "On strongly regular graphs with μ ⩽ 2," Discrete Mathematics
(Bhaskar Bagchi), Elsevier. (The ScienceDirect record S0012365X06002056.)
This run could not download the full text (403 Forbidden; paywalled). The
theorem statement below is verified from the ScienceDirect excerpt + proof
passage captured in the run transcript, and from the citing paper summaries.

## Verified theorem (from the excerpted abstract + proof)

- If an srg has μ = 1 then k ≥ (λ+1)(λ+2).
- **Theorem 4:** any srg with μ = 2 is either a **grid graph** or satisfies
  **k ≥ 12·λ·(λ+3)**.

## The proof that must be read carefully (crucial subtlety)

Proof of Thm 4: *Suppose k < 12λ(λ+3). By a result of [5] (Brouwer–Neumaier
1988), any srg with μ=2 and k < 12λ(λ+3) is K₁,₁,₂-free. Therefore (by
Lemma 1) the graph is the collinearity graph of an (s,t)-generalized quadrangle.
Since t+1 = μ = 2, it is a grid graph.*

**The dichotomy is NOT unconditional.** The grid conclusion enters through
K₁,₁,₂-freeness. So a μ=2 srg with k<12λ(λ+3) that is NOT K₁,₁,₂-free escapes
the theorem.

**Consequence for the controls:** BvLS (243,22,1,2) has k=22 < 48 = 12·1·4 and
is not a grid graph — yet exists. The only consistent escape is that BvLS is
NOT K₁,₁,₂-free (it contains an induced K₁,₁,₂). A hypothetical (99,14,1,2) has
k=14 < 48, so IF it is forced K₁,₁,₂-free it is a grid — impossible. So the
loaded question is whether a putative 99-graph is K₁,₁,₂-free, and whether BvLS
is not. This is the most promising and most dangerous route of the run; the
oracle should build BvLS and test for an induced K₁,₁,₂.

See research/notes/bagchi-mu2-dichotomy-resolution.md for the full resolution
note, and the claims ledger c6 / c6-correction.

## Status

- Bagchi full text NOT in library (403/paywalled). Only the abstract + proof
  excerpt are verified.
- This correction record replaces a wrong download (math/0512558).
- Gap: the exact statement of Lemma 1 and the Brouwer–Neumaier [5]
  K₁,₁,₂-free condition; and whether BvLS contains induced K₁,₁,₂ (computable
  once the oracle builds BvLS).
