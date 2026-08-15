# G-supply-transfer is NOT a universal combinatorial statement (S1 fork resolved)

**Cycle / source:** this scholar cycle, consolidating the refuter's board report
(`teams/board_refuter_g_supply_transfer.md`), the pattern_finder's exact
enumeration, and this cycle's independent hand check. The refutation was on the
board and in Cognee but not filed as a claim, and the backward gap
`G-supply-transfer` still read `open`. This note files it.

## Statement attacked

`G-supply-transfer` (research/backward/nu2-supply-split.md): for every
**successful 2-then-odds prefix** q_1..q_n (q_1=2, q_2=3, q_j odd increasing,
all gaps even), with w(n) = #{j∈[2,n−1] : q_{j+1}−q_j ≡ 2 (mod 4)} and ν₂(q_n) =
#2s in the maximal {0,2} suffix of the right diagonal δ(q_n):

```
ν₂(q_n) ≥ (2/3)·w(n).
```

This is the *combinatorial* half of the supply-split: if it held universally, it
would offload all the number-theoretic content of G-supply onto an F₂-linear
(XOR / Rule-90) inequality that is prime-free.

## Refutation — a whole family, not one instance

**Consecutive-odds family.** q = (2,3,5,7,…) i.e. all gaps = 2. Every gap ≡ 2
(mod 4), so w(n) = n−2 (maximal). But the triangle collapses:

```
A_0 = (2,3,5,7,9,…)
A_1 = (1,2,2,2,2,…)
A_2 = (1,0,0,0,…)
A_3 = (1,0,0,…)
```

For n ≥ 4 every row from k=2 on is (1,0,0,…), and the right diagonal's maximal
{0,2} suffix is **all zeros** — so ν₂(q_n) = 0 for every n ≥ 4 (both under the
literal and the run's `d[2:-1]` convention). Then ν₂ = 0 < (2/3)w = (2/3)(n−2)
for all n ≥ 4. **FALSE.** Smallest instance n=4 (any n≥4 works).

Consecutive-odds is a *successful* prefix (bottom entry 1 forever — the settled
class `R2-consecutive-odds-class`), so the counterexample lies squarely inside
the lemma's stated domain.

## Independent confirmations

1. **Refuter** (`board_refuter_g_supply_transfer.md`): hand arithmetic on
   (2,3,5,7,9), n=4, δ=(9,2,0,0): ν₂=1 literal / 0 tail-convention, (2/3)w=4/3.
2. **pattern_finder** (S1-fork resolution, in Cognee): exact enumeration over
   all {2,4}-gap 2-then-odds strings (first gap=2, up to length m=14) finds
   violations of the weaker ν₂≥w/2 growing with length (m=7:10, m=12:145,
   m=13:258, m=14:461); the all-2 string of length 12 has w=12, ν₂=1. So even
   ν₂≥w/2 is not a universal F₂ identity.
3. **This cycle**: hand re-verification of the consecutive-odds family (above).

## What it decides

The S1 fork in `nu2-supply-split` lands on **(b) prime-specific**: `ν₂ ≥ c·w`
is **not** a universal combinatorial transfer. The supply decomposition cannot
offload the number-theoretic content onto a clean F₂ weight inequality. The
primes *do* measure ν₂/w ∈ [0.689, 0.867] (`g-supply-transfer-measured`), so
the supply *statement* is not dead — but it is a claim about the particular
prime bit string, not a general identity. This matches the independently
refuted `nu2-supply-mod4-transfer` (S1 both-legs) already marked broken.

## What it does NOT touch (Directive 55 — three precise boundaries)

The operator checked this refutation independently and confirms it is genuine.
Three things it does NOT do, stated so nobody over-reads it:

1. **It does not touch the primes.** Measured ν₂/w on real prime rows is
   [0.689, 0.867], confirmed to N=30000. The primes have varied gaps; the
   counterexample has constant ones (all gaps = 2). The refutation is about the
   *universal* transfer, not the supply statement on the prime bit string.

2. **It does not refute the general-class theorem** "any successful 2-then-odds
   sequence with w(n) ≥ 2·n^0.526 is Gilbreath." Consecutive odds *satisfies*
   that hypothesis and *is* successful, so it is not a counterexample to that
   statement — it only breaks the particular PROOF ROUTE through ν₂. A refuted
   route is not a refuted theorem.

3. **It does not kill Route B.** It kills G-supply-transfer AS A UNIVERSAL
   LEMMA only. Lemma 5.4 (the sufficiency budget `g*_n ≤ 2ν₂+2`) is unaffected:
   a lower bound on the transfer is not needed to run the budget on the primes.
   The whole of Route B still rests on the single named-open two-point mod-4
   supply bound (`abgs-2011-s9-mod4-switch-limit-open`); this refutation only
   removes the *triangulated shortcut* to it.

**The repair (Directive 55):** find the hypothesis the counterexample violates.
Constant gaps are degenerate — the triangle dies at row 2 and never
regenerates, so w counts switches that never reach the tail. The needed
hypothesis is some gap-variety / non-degeneracy condition that the primes
satisfy and constant-gap sequences do not. Find the **WEAKEST** such condition,
not the first one that works: the value of the transfer lemma was that it was
prime-free, and every added hypothesis spends some of that.

```claim
id: g-supply-transfer-universal-refuted
statement: The universal combinatorial transfer nu2(q_n) >= (2/3)·w(n) for every
  successful 2-then-odds prefix is FALSE. Counterexample family: consecutive odds
  (all gaps = 2), successful for every n, gives w(n) = n-2 (maximal) while the
  triangle collapses to (1,0,0,...) from row 2 on, so the maximal {0,2} suffix of
  the right diagonal is all zeros and nu2 = 0 for every n >= 4. Hence nu2 < (2/3)w
  for all n >= 4. Even the weaker nu2 >= w/2 is not a universal F2 identity: exact
  enumeration over {2,4}-gap strings (first gap 2, length <= 14) finds violations
  (all-2 string of length 12: w=12, nu2=1). The S1 fork resolves to case (b)
  prime-specific: the nu2 >= c*w supply decomposition cannot offload the mod-4
  number-theoretic content onto a clean XOR/Rule-90 weight inequality. The primes
  still measure nu2/w in [0.689, 0.867], so the supply statement survives for the
  primes; only the universal transfer (the triangulated shortcut to it) is dead.
hypotheses: successful 2-then-odds prefixes; nu2 = #2s in maximal {0,2} suffix of
  the right diagonal; w = Hamming weight of halved-gap mod-4-switch bits over [2,n-1].
holds-here: yes (the counterexample family is within the stated domain)
status: checked (refuter hand-arithmetic + pattern_finder exact enumeration to
  length 14 + this cycle's independent hand re-verification)
bearing: closes the G-supply-transfer gap in research/backward/nu2-supply-split.md
  as refuted (it was left open); the honest supply route must carry the mod-4 gap
  density content directly (conditional at Hardy-Littlewood / LOS level), not
  through a combinatorial weight shortcut. Lemma 5.4 and the recharge identity are
  unaffected.
anchor: teams/board_refuter_g_supply_transfer.md, research/backward/nu2-supply-split.md,
  research/backward/nu2-supply-mod4-transfer.md (already broken)
contradicts: g-supply-transfer (the universal form as stated in the gap) - which
  has no claim row; refutes the open gap, not g-supply-transfer-measured (the
  prime-specific measurement, which stands)
answers: none (closes the open gap in the backward ledger)
```
