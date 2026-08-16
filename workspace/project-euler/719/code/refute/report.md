# Refutation attempts — Project Euler 719

This folder records the refuter's attacks on the run's claims. All targets were
**not refuted**; the run's claims held up. `find_counterexample` returned
`undecided` for the mod-9 encodings because the abstract finite-domain
encodings cannot faithfully resolve ordinary decimal arithmetic at the relevant
sizes, and no counterexample is expected from a provable digit-sum fact.

## mod9-invariant.p — the mod-9 filter (claim `partition-sum-invariant-mod9`)

The claim: every S-number n = m^2 has its root m satisfying m ≡ 0 or 1 (mod 9),
because the witness block-sum equals m and is congruent to m^2 (mod 9) (the
digit-sum rule, 10 ≡ 1 mod 9). The run uses this as a pruning filter.

- **Attack.** Try to exhibit a root m ≡ 2..8 (mod 9) that is an S-root.
  Hand checks of the smallest residue-2 candidates (m = 2, 11, 20, 29, 47) all
  fail to split to m (e.g. 11^2=121 has 2+-block sums 22, 13, 4 — none = 11).
- **Outcome.** `find_counterexample` = `undecided`. No counterexample and no
  proof at the sizes searched.
- **Reason no counterexample is expected.** The invariant is a *provable*
  arithmetic fact: modulo 9, 10 ≡ 1, so any split's block-sum is ≡ the full
  number (mod 9). The filter is sound. A refutation would require an arithmetic
  inconsistency, which does not arise.
- **Boundary strength.** The strongest instance — 10^12 itself is an S-number
  via split `1000000|0|0|0|0|0|0` summing to 1000000 — checks out by hand, so
  the claim (and the b-file coverage) is intact.

## Conclusion for the run

No statement of the run was refuted. The weakest load-bearing claim that the
run itself flagged as "asserted, not checked" (`partition-sum-invariant-mod9`)
survived both hand inspection of the smallest residue-2 candidates and the
finite-model search. This is consistent with the claim being a proven digit-sum
invariant; the TPTP tool cannot refute a true statement here, and the honest
report is `undecided` (weak evidence, nothing more).
