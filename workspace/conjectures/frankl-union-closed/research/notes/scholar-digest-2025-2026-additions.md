# Scholar pass — digesting the 2025–2026 additions (Bouchard ×2, Spence)

This pass read the genuinely new primary sources in the library against the
run's goals (GOAL.md), tasks, and durable beliefs, and verified each digest
against its full text before recording anything.

## What was genuinely new

The librarian had already closed the run's gathering under operator directive;
most of `research/` was digested and claim-bearing. The three sources whose
results had **not** yet reached the claim store were:

1. **Bouchard, "An averaging result..." arXiv:2509.12537 (2025)** — digest was
   accurate; **lacked a claim block**. Added `bouchard-averaging-height4`.
2. **Bouchard, "An upper bound for union-closed family size" arXiv:2511.10608
   (2025)** — digest was accurate; **lacked a claim block**. Added
   `bouchard-upper-bound-length`.
3. **Spence, "Auditing Two Claimed Proofs..." zenodo 2026** — claim block
   `spence-minimum-counterexample-odd` was already filed and present in the
   store (verified with `search_claims`, not grep).

All three were cross-checked against the primary full texts in
`research/sources/` before writing the claim blocks.

## What each establishes (verified against primary text)

- **Bouchard 2509.12537**: separating UC family with height h=4≤n and 0≤|B|≤2
  (B a smallest irredundant subfamily of A_<n/2) has Avg ≥ n/2 (Thm 2.1), hence
  abundant element (Cor 2.2); h≤3 also UC (Thm 1.4); h=4 is the LARGEST height
  reachable by averaging — explicit separating UC with h≥5, |B|=1, Avg<n/2
  (Thm 3.2). **New settled class** + explicit modern witness on limits of
  averaging (sharpens `cms-averaged-frankl-wrong`).
- **Bouchard 2511.10608**: |A| ≤ Σ_{i=0}^ℓ C(n,i), equality iff all subsets of
  size ≥ n−ℓ; tightens Erdős from largest-ℓ+1 to first-ℓ+1; Cor 2.1 "at most"
  dual frequency; analytic binomial-sum bound. Structural refinement of the
  Reimer/Erdős size line.
- **Spence 2026**: refutes two claimed-proof mechanisms on tiny explicit objects
  (Heavy-Column Theorem via a non-union-closed 5×4 matrix; Schrader's
  discarding bound), NOT the conjecture; Section 6 gives new MINIMUM-counterexample
  necessary conditions: |F| odd = 2k+1, every frequency ≤ k, tight-witness
  per deletion, and (lattice) common tight join-irreducible below any two
  meet-irreducibles (strengthens Bouchard 2503.00277 Cor 2.11).

## Implications for the run

- New structural ammunition for the **abundance-profile** and
  **minimal-counterexample** threads (ROOT.md's |F|≥51 carries no parity; Spence
  adds oddness + tight-witness; Bouchard-height bounds which height classes a
  counterexample cannot inhabit; Bouchard-length bounds how short its height can
  be). Updated `research/threads/abundance-profile.md` to cite all three.
- No change to the constant record (Yu 0.38234 published / Liu 0.38271
  conditional preprint) — none of the three is an entropy/constant result.
- No source-vs-source contradiction with recalled memory. Spence's "Heavy
  Column Theorem false" is explicitly noted by the paper itself NOT to refute
  the union-closed version, so it does not contradict anything the run holds.

## Durable findings stored

`remember_memory`: Bouchard-averaging, Bouchard-upper-bound, Spence audit +
minimum-counterexample structure (each with URL + falsifier).

## Sources that do not help (already known)

- OEIS A1xxxxx catalogue files, citation-graph files, the eccles-stability probe,
  and the mislabeled `vaughan-families-implying-frankl-2002` (algebroids paper)
  — none is evidence; do not re-read.

## What the run still lacks (unchanged)

The entropy-coupling global-sup-over-α claim and the reproduction of Yu's
optimisation remain open; the library is finished per operator directive. The
novelty of φ/2 = Γ̂(1/2) against Yu/Cambie remains unchecked. None of these
new sources moves them.
