# arXiv API listing, "square peg" query, 2025–2026 (status sweep)

**Source:** live arXiv API query (`all:"square peg"`, 50 results, sorted by
submitted date, retrieved 2026-08-18), captured at
[[research/sources/arxiv-api-square-peg-2025-2026.full.md]].

**What this sweep establishes — nothing is proved by a listing, but absence is
informative:**

1. **No arXiv preprint from 2025–2026 claims a full proof of the Toeplitz
   conjecture.** The only mathematics papers in the 50 hits are: Chambers 2022/25
   (stability near C², already in library), Hugelmeyer 2024 periodic square peg
   (see below), Greene–Lobb 2024 ×2 and Tao 2017 and Rifford 2021 and Matschke
   2009 and CDM 2014/2021 ×2 and van Heijst 2014 and Pak 2008 (all already in
   library), Naseri Sadr 2024 (table theorem, uses smooth square-peg as input),
   Friedl–İnce 2023 (table theorem ↔ square peg connection), Hugelmeyer 2023
   square envelopes (in library), Aslam et al. 2020 (splitting loops and
   necklaces — continuous-curve rectangle variants), Sagols–Marín 2010, Akopyan–
   Avvakumov 2018. The rest of the 50 hits are robotics/papers on "square peg"
   in a literal peg-in-hole sense (noise).

2. **Hugelmeyer 2024, "A Solution to the Periodic Square Peg Problem"
   (arXiv:2407.20412):** abstract states the periodic variant is resolved by a
   Lagrangian Floer homology argument, inscribed squares as intersections of two
   non-displaceable Lagrangian submanifolds of a symplectic 4-torus. Full text
   not in library. This **contradicts the standing claim `tao2017-periodic-
   variant-open`** (Tao 2017 Conjecture 4.1 reported open even for PL curves),
   unless Hugelmeyer's statement differs from Tao's — the exact match is
   unverified. Relevance: Tao's Conjecture 4.6 says Toeplitz implies the
   periodic variant; the converse (periodic ⇒ Toeplitz) is not asserted, so
   Hugelmeyer's resolution does NOT settle the Toeplitz conjecture. It is a
   shrinkout-insensitive reformulation, so it is methodologically adjacent to
   this run's frontier.

3. **Naseri Sadr 2024** ("A Table Theorem for Surfaces with Odd Euler
   Characteristic", arXiv:2412.01977): uses the *smooth* square-peg result as
   an ingredient for table theorems on surfaces. Consequence direction: square
   peg → table theorem, not the reverse. Not a square-peg advance.

4. **Friedl–İnce 2023** ("When does the table theorem imply a solution to the
   square peg problem?", arXiv:2303.17711): discusses the relationship between
   Fenn's table theorem and the square peg problem. Not a proof; a lead on a
   different route (if the run wants the table-theorem attack surface).

5. **van Heijst 2014** ("The algebraic square peg problem", Master's thesis):
   an algebraic curve of degree m inscribes either infinitely many squares or at
   most (m⁴ − 5m² + 4m)/4 squares (Bernshtein's theorem count). A quantitative
   algebraic bound — candidate exact-arithmetic oracle target for algebraic
   curves, and a possible formalization target.

**What it implies here:** the survey horizon is clean — no new positive class
and no counterexample appeared in 2025–26 on arXiv; the legendrian-lift frontier
(R4 of the ladder, thesis `legendrian-lift-frontier`) remains the sharp open
question. The one ledger-level action: flag `tao2017-periodic-variant-open` as
contradicted-by-abstract by Hugelmeyer 2024 (asserted-by-source, unverified
match). Nothing else changes.

```claim
id: arxiv-sweep-2025-2026-no-full-proof
statement: As of the 2026-08-18 arXiv sweep, no arXiv preprint claims a full proof of the Toeplitz square peg conjecture for all continuous Jordan curves; the only full-proof-style claim found anywhere is Ueoka's Zenodo series (2025–26, unvalidated, see asano-ike-2024-status.md).
status: catalogued (sweep of one query, 50 results)
evidence: arXiv API query all:"square peg" retrieved 2026-08-18
holds-here: yes — confirms the conjecture's open status against 2025–26 arXiv activity
falsifies: an arXiv preprint dated 2025–2026 proving the full conjecture
anchor: research/sources/arxiv-api-square-peg-2025-2026.full.md
```

```claim
id: hugelmeyer2024-periodic-square-peg
statement: The periodic square peg problem (Tao 2017 Conjecture 4.1) is resolved by a Lagrangian Floer homology argument: inscribed squares are intersections of two non-displaceable Lagrangian submanifolds of a symplectic 4-torus.
status: asserted-by-source (abstract only; full text not in library; peer-review status unknown)
evidence: Hugelmeyer, arXiv:2407.20412 (abstract, via arXiv API dump)
holds-here: yes — if the statement matches Tao's Conjecture 4.1 exactly, it contradicts tao2017-periodic-variant-open; the match is unverified
falsifies: a discrepancy between Hugelmeyer's theorem and Tao's Conjecture 4.1; a correction/retraction
contradicts: tao2017-periodic-variant-open
answers: tao2017-periodic-variant-open
anchor: research/sources/arxiv-api-square-peg-2025-2026.full.md
```

```claim
id: van-heijst-2014-algebraic-count
statement: An algebraic plane curve defined by a polynomial of degree m inscribes either infinitely many squares or at most (m⁴ − 5m² + 4m)/4 squares (by Bernshtein's theorem).
status: asserted-by-source (abstract only; full text not in library)
evidence: van Heijst, "The algebraic square peg problem", Master's thesis 2014, arXiv:1403.5979 (abstract)
holds-here: yes — a quantitative bound for algebraic curves; candidate exact-arithmetic oracle target and Lean statement
falsifies: an algebraic curve of degree m with a finite square count exceeding the bound
anchor: research/sources/arxiv-api-square-peg-2025-2026.full.md
```
