# Blair Morgan — Reducing Gilbreath's Conjecture to a Local Condition (2026)

**Source:** https://zenodo.org/records/19143644 (DOI 10.5281/zenodo.19143644), working paper v1.0, March 2026, author Blair Morgan (ORCID 0009-0003-1942-8103). Full text: `research/sources/blair-morgan-2026-local-condition-frontier.full.md`. Predecessor of the frontier/basin note described in `blair-morgan-2026-return-of-the-lemma.md`.

## What it proves

**Theorem (Sufficiency).** If Conjecture L holds — `|G_r[2] − G_r[1]| ≤ 2` for all `r ≥ 1` — then Gilbreath's Conjecture holds.

*Proof (verbatim structure):* by the parity invariant, `G_r[1]`, `G_r[2]` are even for `r ≥ 1`; Conjecture L bounds their absolute difference by 2, so `G_{r+1}[1] = |G_r[2] − G_r[1]| ∈ {0,2}`. Boundary stability `|1 − {0,2}| = 1` then gives `G_{r+1}[0] = 1` from `G_r[1] ∈ {0,2}`. Base `G_1[0] = 1`, `G_1[1] = 2`. Induction gives `G_r[0] = 1` for all `r ≥ 1`. ∎

**Converse not claimed:** Gilbreath ⇒ Conjecture L is not proved (only noted that computationally position 1 lies in {0,2} through 100,000 rows). Claims only sufficiency.

## Supporting lemmas stated

1. **Parity invariant:** for `r ≥ 1`, position 0 is the unique odd value in each row.
2. **Monotone maximum:** global interior max is non-increasing.
3. **Strict descent:** max drops by ≥ 2 unless an `(M, 0)` adjacency exists.
4. **Boundary stability:** `|1 − {0,2}| = 1`.

## Minimal violation analysis (structural, not a proof)

Smallest violation of Conjecture L is `|G_r[2] − G_r[1]| = 4`. Model case `(G_r[1], G_r[2]) = (4, 0)`: the parent triple at positions (1,2,3) of row r−1 must be `(b ± 4, b, b)` — a ±4 jump immediately followed by equality. Propagating back, `b = c` requires `|G_{r−2}[2] − G_{r−2}[3]| = |G_{r−2}[3] − G_{r−2}[4]|`, branching into rigid constrained ancestor families. The author does not claim this is an impossibility proof.

## Numerical verification

Conjecture L + position 1 ∈ {0,2} verified through 100,000 rows (49,737 zeros, 50,263 twos). Reference script: iterative `np.abs(np.diff(a))` over `sympy.primerange`.

## Bearing on this run

- Independently confirms this run's central reduction: the conjecture is equivalent to `G_r[1] ∈ {0,2}` for all `r ≥ 1` (the author's Conjecture L is a *sufficient* strengthening: `|G_r[2] − G_r[1]| ≤ 2` with both even forces `G_{r+1}[1] ∈ {0,2}`; it is strictly stronger than the reduction).
- The run's depth-1000 data already contains everything the author verified to 100,000 rows (and the run's `(edge, intruder) = (2,4)` regeneration criterion is the boundary-dynamics version of the same gap).
- The honest remainder is the same as the run's: prove Conjecture L (or the frontier hypothesis of the companion note), i.e. the local bound propagates. The note explicitly lists as its own open question whether `|G_r[2] − G_r[1]| ≤ 2` propagates inductively — no source answering that is known.
- Lemma 2 (monotone max) and Lemma 3 (strict descent) are the Ducci potential facts this run's `ducci-potential-max-decrease` approach relies on, stated here as lemmas without full proofs of their equality-case rigidity.

## Caveats

- Working paper, not peer-reviewed; AI-collaborator credited ("Claude Opus 4.5"), accountability asserted by the author.
- "Unique odd value" wording in Lemma 1 is inaccurate as stated (position 0 is odd, other positions even — uniqueness is of the oddness pattern, not a single odd value in a row with many odds): the parity claim that matters is the evenness of positions ≥ 1, which matches this run's proved parity wave.