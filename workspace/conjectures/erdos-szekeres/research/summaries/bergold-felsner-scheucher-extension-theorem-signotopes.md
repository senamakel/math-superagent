# Bergold, Felsner, Scheucher 2023 — "An extension theorem for signotopes" (SoCG 2023)

Source: https://arxiv.org/abs/2303.04079 (SoCG 2023, LIPIcs 258, 17:1–17:14, DOI 10.4230/LIPIcs.SoCG.2023.17)
Full text: [[bergold-felsner-scheucher-extension-theorem-signotopes.full]]
Verified: downloaded and read this run.

## Definition of signotopes (the foundational bit this run's encoders rely on)

An **r-signotope** on [n] is a sign map σ: [n]^r → {+,−} such that in every (r+1)-subset, the induced r-sign sequence has **at most one sign change** (read in lex/colex order). Key facts used everywhere in the SAT-encoding literature:
- r=2: signotopes ↔ permutations.
- **r=3 (rank 3): signotopes ↔ simple pseudoline arrangements in the plane with a fixed top/north cell** (Felsner & Weil 2001, "Sweeps, arrangements and signotopes"). This is the exact correspondence the run's orientation-variable SAT encoders (SMQH, Dumitru, Scheucher, Balko–Valtr) mirror: the "ordered-signotope axioms" and "triple orientation / transitivity" constraints are precisely this rank-3 structure. A *realizable* point set corresponds to a *stretchable* pseudoline arrangement (all pseudolines straight).
- Signotopes form a rich subclass of oriented matroids; ≈ 2^{Θ(n^{r−1})} r-signotopes on n elements.
- Partial order on signotopes by inclusion of the +-preimage; r=2 recovers weak Bruhat order on S_n. Related to higher Bruhat orders (Manin–Schechtman, Kapranov–Voevodsky, Ziegler).

## What the paper itself proves (extendability, not needed for the run's core but good theory)

- **Odd rank r ≥ 3**: every r-signotope is 2-extendable — given two prescribed crossing points ((r−1)-sets I, J), one can add a new element so that I∪{new} and J∪{new} are fliples in the extension. Purely combinatorial proof; recovers Levi's 1926 extension lemma for pseudoline arrangements (the rank-3, planar case).
- **Even rank r ≥ 4**: there exist NON-2-extendable signotopes, verified by SAT-based search for ranks 4,6,8,10,12; conjecture no extension theorem holds for any even r ≥ 4. (Contrast: Richter-Gebert's non-extendable pseudoplane arrangement in R³.)

## Implication for this run

The run's SAT arms encode the ES problem as rank-3 signotopes / ordered-signotope / CC-system (Knuth triples) with transitivity axioms, then distinguish realizable (stretchable, straight-line) from merely-abstract configurations — exactly because not every rank-3 signotope is stretchable (realizability is ∃ℝ-complete). This paper gives the precise definition and the Felsner–Weil r=3 correspondence that justifies that encoding, and it confirms the correct level of abstraction: **order type = reorientation class / stretchability class of a rank-3 signotope**. Its own result (extendability parity) is tangent to ES(n), but it supplies the vocabulary and the exact axiom the encoders use. (The Felsner–Weil 2001 primary source itself remains the canonical citation; its open access full text could not be fetched this run, but this paper restates the correspondence it needs.)

```claim
id: signotope-rank3-pseudoline-correspondence
statement: Rank-3 signotopes on [n] (sign maps on triples with at-most-one-sign-change per 4-set) are in bijection with simple pseudoline arrangements with a fixed top cell (Felsner–Weil 2001). This is the combinatorial backbone of the orientation-variable SAT encodings of the ES problem: the ordered-signotope/transitivity axioms encode exactly this rank-3 structure, and a point set of size n corresponds to a stretchable (straight-line-realizable) rank-3 signotope. Realizability of a rank-3 signotope is ∃ℝ-complete.
hypotheses: rank-3 signotope, n points in general position (or n pseudolines), fixed top cell.
holds-here: yes — this is the precise statement underpinning the run's SAT arm (SMQH encoder: 'ordered-signotope axioms', 'CC-system/Knuth triples').
status: checked (read the source file this run; the Felsner–Weil bijection is stated there with citation).
bearing: GOAL 3 & the SAT arm — justifies the orientation-variable formulation and the need to separate realizable from abstract (the ES construction is realized in exact coordinates; abstract solutions need realizability checking before they count).
anchor: research/summaries/bergold-felsner-scheucher-extension-theorem-signotopes.md
follows-from: fw-rank3-signotope-pseudoline (this is the same bijection, stated from the secondary source; the primary Felsner–Weil statement is the source of the content)
```
