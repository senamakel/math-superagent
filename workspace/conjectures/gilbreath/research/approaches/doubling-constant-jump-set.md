```approach
idea: Attack the recharge deficit as a structural (additive-combinatorial) statement about the multiset of (2,4)-event jump sizes — apply Freiman's theorem and Plünnecke's inequality to show that any counterexample forces the jump set to have small doubling, hence forces the underlying gap word to be almost periodic, contradicting a prime-free "large doubling" density property.
mechanism: |
  The recharge identity (proved, zero failures to depth 800) is
      b_k = b_1 + sum_{events i<k} (j_i + 1) - (k - 1),   j_i >= 0.
  Each event contributes j_i + 1 >= 1, and consumption is exactly (k-1), so
  the block dies iff the partial sum S_m = sum_{i<=m}(j_i + 1) ever falls
  below m - b_1. The minimal sustainable event has j_i = 0 and contributes
  exactly 1, i.e. it only breaks even. Therefore a counterexample is NOT
  primarily about event RATE (one event every row is barely enough); it is
  about the DISTRIBUTION OF JUMP SIZES: the cumulative surplus sum(j_i)
  must stay o(m) while the event count m grows linearly. This is a
  statement about a specific sequence of non-negative integers j_i that is
  a DETERMINISTIC function of the initial gap word (each jump j_i is the
  length of a 1-Lipschitz stretch of the halved row past the block front).

  The reformulation: for an initial sequence with gaps g = (g_1, g_2, ...),
  define the jump sequence J(g) = (j_1, j_2, ...) and its multiset of values.
  The conjecture holds iff for the prime gap word, the multiset {j_i} is
  "rich enough" that no prefix has small sum relative to its length. The
  contrapositive is the structural claim: if Gilbreath FAILS for some gap
  word, then the jump multiset (equivalently the gap word's 1-Lipschitz
  excursion lengths) has SMALL DOUBLING |J + J| <= C|J|, and by Freiman's
  theorem is Freiman-isomorphic to a low-dimensional generalized arithmetic
  progression. Consecutive odds (the universal refutation of the F2 transfer
  bound) have all j_i = 0: doubling constant 1, maximally structured. The
  primes' jump set is measured to have heavy tails (jumps grow sublinearly,
  geometric giants), i.e. large doubling.

  So the theorem to hunt: "large doubling of the jump multiset => recharge
  surplus grows at least linearly => block survives." This is a genuinely
  different axis: it converts the open RATE question into an additive-
  combinatorial STRUCTURE question about a derived integer sequence, and it
  is prime-free (a general class theorem), matching GOAL.md's preferred
  side. Named mathematics: Freiman's 3k-4 theorem / Freiman-Ruzsa, the
  Plünnecke-Ruzsa triangle inequality, and the Bogolyubov-Ruzsa lemma on
  iterated sumsets.
status: refuted
killed-by: |
  The load-bearing transfer from Freiman/Plünnecke to the recharge surplus
  does not exist. Freiman's theorem and Plünnecke's inequality are statements
  about the SUM OF AN ADDITIVE SET |A + A| in terms of |A|: small doubling
  |A + A| <= C|A| forces A to be Freiman-isomorphic to an AP. The recharge
  identity, however, needs a lower bound on the PARTIAL SUM of the SEQUENCE
  sum_{i<=m} j_i — a quantity that has no relation to the cardinality of the
  SET of distinct jump values. A multiset of m jump sizes can have arbitrarily
  LARGE sumset doubling (choose the values spread) while its partial sums are
  o(m) (take the sequence: m-1 zeros then one huge jump); the candidate's own
  primes, with a heavy tail of jump values, have large doubling exactly while
  the surplus is dominated by a few giants. So "large doubling of the jump
  set" and "linear growth of the recharge surplus" are not coupled at all:
  Plünnecke/Freiman put no lower bound on partial sums of a sequence from the
  doubling of its value set. The contrapositive is a claim about the wrong
  object.
precedent: |
  No source applies Freiman/Plünnecke/additive combinatorics to the Gilbreath
  or iterated-absolute-difference problem (searched "Freiman theorem Gilbreath
  small doubling", "iterated absolute differences jump sizes additive
  combinatorics"; the only additive-combinatorics hits on Gilbreath are
  generic sumset-theory papers with no Gilbreath connection — e.g. the iterated
  sumsets / dimension-growth literature (Granville-Smith-Walker 2025;
  Iterated sumsets and subsequence sums), which study |nA| of a SET, not the
  partial sums of a derived SEQUENCE, and therefore do not help). The run's
  subadditive-growth-ergodic-block-length approach (adopted) already abstracts
  the recharge surplus correctly into the criterion r·J > 1 — the relevant
  macroscopic objects (event density r, per-event mass J) that additive
  combinatorics cannot reach.
```

**Grounding note (research, this cycle).** Refuted on a structural mismatch, not on a missing application. The additivity that matters for the recharge surplus is the *sequence* additivity (S_{k-1} additive over event intervals), which is exactly the subadditive/renewal-reward setup of the already-adopted `subadditive-growth-ergodic-block-length` approach; Freiman/Plünnecke address the *set* cardinality, which is a different and inert quantity here. The speculative point the inventor flagged — doubling of the jump *set* vs surplus of the jump *sequence* — is not a detail to be resolved: it is the fatal gap, because there is no known lemma (additive-combinatorial or otherwise) turning |J+J|/|J| into a lower bound on Σ_{i≤m} j_i. The correct reformulation of the recharge is r·J > 1 (adopted approach), not a small-doubling condition on the jump-value set.
