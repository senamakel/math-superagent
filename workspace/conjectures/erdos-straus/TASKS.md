# Tasks

Priority follows operator directive 3: the 554 subprogression families are
real (operator-verified, 554/554 polynomial identities in ℤ[k]), they cover
94.72% of n ≡ 1 mod 840, but they touch only one of the six open classes and
novelty against Elsholtz–Tao is unchecked.

## 1. Promote the subprogression claim — done this cycle

- [x] Claim `subprogression-families-verified-and-coverage` exists in
      `code/out/subprogression_coverage.md` with a proper claim block. It must
      be absorbed into `research/CLAIMS.md` (the ledger is auto-derived from
      claim blocks, so the block in the coverage file is sufficient — the next
      re-derivation will pick it up). Status in the block is `checked`, backed
      by the operator's exact integer polynomial arithmetic pass (554/554).

## 2. Novelty check — the next work

- [ ] For each of the 554 families, determine whether the shape is a
      rediscovery of a known Elsholtz–Tao type (Type I / Type II polynomial
      family from E-T Prop 1.9 / Salez seven equations) in different
      coordinates, or genuinely new. Use
      `research/sources/elsholtz-sums-of-k-unit-fractions.full.md` and
      `research/sources/elsholtz-tao-counting.full.md` as the reference. A
      rediscovery honestly labelled is fine; a rediscovery announced as new is
      the failure the operator named.
- [ ] State for each of the 12 moduli m ∈ {11,13,17,19,22,23,26,29,31,33,34,37}
      which E-T family (if any) produces that modulus, and whether the 83
      residue classes of t are a subset of what E-T already classifies.

## 3. State the positive-density gap — what closes it

- [ ] The uncovered 5.28% of n ≡ 1 mod 840 is 7375872/139671337, a positive
      density. No further family with the same 12 moduli can close it — the
      complement is a union of full residue classes of t. State what a closing
      mechanism would look like: new moduli m coprime to the existing set
      {11,13,17,19,23,29,31,37} (with 2 and 3 already at full density within
      the class via the classical families), or a different family shape
      (non-ℤ[k]-polynomial, rational-function, or per-prime rather than
      per-progression).
- [ ] Compute the exact uncovered residue classes of t and state what prime
      moduli would close which fraction of them.

## 4. The other five classes — state explicitly

- [ ] n ≡ 121, 169, 289, 361, 529 (mod 840) have zero families from the
      subprogression sweep. State in every report: "one of six open classes
      touched; about 0.1128% of all n settled." Do not say "progress on the
      open classes" plural.

## 5. Stop the exa_search

- [x] The exa_search went from 29 to 44 with no claim changed. The operator
      has directed: stop it. It is dead.

## Done (prior cycles)

Oracle (`code/oracle.py`), parallel self-check, witness cross-check (12/12),
small brute sweep n≤200, the corrected n≡3 (mod 4) + even-case identities, and
the eight classical covering identities — all captured, identity-checked, and
recorded.

## Source integrity (operator directive 2) — done

- [x] Yamamoto 1965 tombstoned; claim demoted to asserted-never-read.
- [x] MathWorld annotated as orientation-only.
- [x] Eight classical identities identity-checked (last block of
      `code/out/commands.log`).

## Claim conversion (operator directive 2) — superseded by directive 3

The eight classical identities are identity-checked but still `asserted` in
the ledger. Promoting them from asserted → checked is still needed but is
lower priority than the novelty check; the subprogression 554 are now the
largest block of proved-identity claims and those get promoted first.

- [ ] Promote the eight classical identities to `checked` with explicit
      identity proofs documented in claim blocks.
- [ ] Promote `prime-reduction` and `reduction-mod24` to `checked` by
      verifying the scaling lift in exact arithmetic.