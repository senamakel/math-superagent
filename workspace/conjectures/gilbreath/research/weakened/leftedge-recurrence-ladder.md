# Weakened ladder: the quantifier over rows (invariance vs recurrence)

> Complements, does not supersede, the 15 existing ladders. Every one of those
> keeps the conclusion's `∀k` quantifier intact and instead weakens the *input*:
> bounded gaps, `{2,4}`-support, a pinned intruder, an i.i.d. random analogue, a
> periodic halved-gap bit string. This ladder does the opposite. It keeps the
> input the primes and weakens the *conclusion* — from "`A_k(0)=1` for every row"
> down through "for a density-one set of rows", "for a positive-density set", and
> "for infinitely many rows". The new difficulty this exposes is the difference
> between **invariance** (the row never leaves 1) and **recurrence** (it returns
> to 1 after leaving), which none of the other ladders names.

The one-sentence reduction that makes the ladder well-defined (proved,
Lean-formalised, claim `gilbreath-reduces-to-second-in-02`): every row has shape
`(odd, even, even, ...)`, and `A_{k+1}(0)=1 ⟺ A_k(1) ∈ {0,2}`. So the left edge
is always **odd**, the goal is that it is always **exactly 1**, and a "return to
1" at row `k+1` is exactly "`A_k(1) ∈ {0,2}`". The ladder is the graded
restoration of the `∀k` quantifier, with the input held fixed at the primes.

**The five difficulties.**

- `infinite-horizon` — the target quantifies over every `k ≥ 1` with no finite
  bound; a finite check is a fact about that depth only. This is the difficulty
  the ladder switches off at the bottom and grades back on: finite → infinitely
  often → positive density → density one → every row.
- `return-rate` — for the weakened quantifiers the object is *recurrence* of
  `A_k(0)=1`, and the obstacle is bounding the gaps between consecutive rows with
  `A_k(0)=1`. "Infinitely often" needs no such bound; "positive density" does;
  "density one" needs the failure set to be sparse. No unconditional return-time
  law exists for the prime triangle.
- `regeneration-rate` — the proved recharge identity (`step-law-theorem-proved`)
  makes the FULL goal exactly `Σ_{events i<k}(j_i+1) ≥ k−2` for all k. Ruling out
  even a *single* failure needs this arrival rate, so this is the open core behind
  the top rung; consumption is settled, this rate is not.
- `gap-arrangement` — the deterministic, unbounded, irregular prime gap word. It
  alone separates the primes (no failure) from Colonna's single-deletion sequences
  (failure at row 2–3), so any statement about the primes that outlives the
  settled model rungs must use it.
- `non-concentration` — no independence / renewal hypothesis holds for the primes;
  every proved recurrence theorem is a random analogue (Chase 2024 Thm 1, CHT 2026
  Thm 1.3) whose hypotheses are unchecked here.

```ladder
goal: For A_0 = (2,3,5,7,11,13,...) the primes in order and A_{k+1}(i) = |A_k(i) − A_k(i+1)|, prove A_k(0) = 1 for every k ≥ 1 (Gilbreath's conjecture, Proth 1878 / Gilbreath 1958).
difficulties: infinite-horizon, return-rate, regeneration-rate, gap-arrangement, non-concentration
status: open
```

## Rungs, bottom to top

```rung
id: R-left-edge-odd
statement: For ANY sequence beginning (2, 3, odd, odd, ...) — equivalently any A_1 = (1, even, even, ...) — the first entry A_k(0) is odd for every k ≥ 1. This is the goal with the exact value 1 replaced by its parity: the left edge never takes an even value, but it could in principle be 3, 5, 7, ... forever. The settled half of the reduction; the bridge A_{k+1}(0)=1 ⟺ A_k(1) ∈ {0,2} (claim gilbreath-reduces-to-second-in-02, proved) is how "odd" becomes the exact target.
off: return-rate, regeneration-rate, gap-arrangement, non-concentration
stance: settled
merge: Restore the value content — distinguish {0,2} from {4,6,...}. The first move up is the finite record, where the value 1 is *checked* (not proved) for a long prefix: this is the largest rung the run can settle without facing any of the four off difficulties.
```

```rung
id: R-finite-record-1e9
statement: In the prime Gilbreath triangle below 1e9, A_k(0) = 1 for every row 1 ≤ k ≤ 50,847,533: rows 1..247 computed exactly, rows 248..50,847,533 by the proved block lemma from the row-248 all-{0,2} block (claim block-lemma-verification-bound-1e9). The goal with the for-all-k quantifier cut off at a finite (large) bound.
off: infinite-horizon, return-rate, regeneration-rate, gap-arrangement, non-concentration
stance: settled
merge: Restore `infinite-horizon`. The record is a computation plus one protection step; nothing here bounds row 50,847,534. The weakest infinite statement that does not yet need a rate is the next rung — the left edge returns to 1 infinitely often.
```

```rung
id: R-carved-gap24-full-survival
statement: Let A_0 = (2,3,x_1,x_2,...) with every x_i odd, x_1 − 3 = 2, and x_{i+1} − x_i ∈ {2,4} for all i ≥ 1 (gaps after the first all 2 or 4). Then A_k(0) = 1 for every k ≥ 1: row 2 is the all-{0,2} corner, which is closed under absolute differencing. This is a model in which the whole ladder collapses to the bottom — every quantifier (infinitely often, positive density, density one, every row) holds trivially because the left edge never leaves 1. It is included as the witness that the ladder *is* exhaustible once the input is tame; note several existing ladders still mark this class `open`, but it is settled (claim carved-gap24-is-r-lipschitz-corner, proved; sweep-corner-mechanism).
off: return-rate, regeneration-rate, gap-arrangement, non-concentration
stance: settled
merge: Restore `gap-arrangement` — introduce a single gap ≥ 6. A lone 6 in a sea of 2s is fatal (this run's spike-6 counterexample, gaps (2,2,6,2,...) dies at row 4), so the {2,4} model's corner does not survive even one irregularity. The climb from here to the primes is exactly the `gap-arrangement` difficulty, and the next rung re-enters the real prime input at the weakest quantifier.
```

```rung
id: R-infinitely-often
statement: For the prime triangle, A_k(0) = 1 for infinitely many k ≥ 1. Equivalently A_k(1) ∈ {0,2} for infinitely many k. This is the goal with `∀k` weakened to `∃∞ k`: it is the weakest infinite-horizon statement, strictly weaker than the goal and strictly weaker than the already-open "a (2,4)-event occurs infinitely often" (a (2,4)-event at row τ forces b_{τ+1} ≥ 1, so A_{τ+1}(1) ∈ {0,2} and A_{τ+2}(0) = 1 — see regeneration-ladder's R7-primes-events-infinitely-often).
off: return-rate, regeneration-rate, gap-arrangement, non-concentration
stance: open
merge: This is the rung to attack next, and it is deliberately *weaker* than the open R7-events-i.o. — a soft recurrence argument on the prime gap word that shows the {0,2} corner is re-entered infinitely often would settle it without any rate. Turning `return-rate` back on is the next step: promote `∃∞` to positive density, which requires the rows with A_k(0)=1 not to thin out — a bound on the gaps between returns that "infinitely often" does not demand.
```

```rung
id: R-positive-density
statement: For the prime triangle, the set {k ≥ 1 : A_k(0) = 1} has positive upper density: limsup_n #{k ≤ n : A_k(0) = 1} / n > 0. The goal with `∀k` weakened to "a positive fraction of rows".
off: regeneration-rate, gap-arrangement, non-concentration
stance: open
merge: `return-rate` is now ON: infinitely often gives no lower bound on how frequent the returns are, and positive density is precisely a linear lower bound on the count of returns. First move: bound the inter-event gap in the (2,4)-event stream (the recharge-balance ladder's `unbounded-event-gap` difficulty — measured max 64 among the genuine giants at 1e9, unproved in general); a bounded-gap or bounded-average-gap law on events would give positive density. Then promote to density one, where the failure set must be sublinear.
```

```rung
id: R-density-one
statement: For the prime triangle, #{k ≤ n : A_k(0) ≠ 1} = o(n): the left edge is 1 on a density-one set of rows. The goal with `∀k` weakened to "all but a zero-density set of rows".
off: regeneration-rate, gap-arrangement, non-concentration
stance: open
merge: Density one still permits an infinite (zero-density) set of failures, so it is strictly weaker than the goal. `return-rate` is on in its strongest form (the failure set must be sparse), and turning `regeneration-rate` back on is the final step: ruling out the *last* failure is exactly the recharge budget `Σ_{events i<k}(j_i+1) ≥ k−2` for all k (the proved identity, step-law-theorem-proved). Next rung is the full statement.
```

```rung
id: R-full
statement: The full goal: for the primes in order, A_k(0) = 1 for every k ≥ 1 — equivalently A_k(1) ∈ {0,2} for every k ≥ 1, equivalently Σ_{events i<k}(j_i+1) ≥ k−2 for all k (recharge identity).
off:
stance: open
merge: n/a — top of the ladder. The ladder is exhausted exactly when this rung settles: `regeneration-rate` has been turned fully back on (a zero-density failure set upgraded to zero failures) and survived, which is the single open core every other ladder also bottoms out at.
```

## Summary

- **Settled floor, three rungs deep.** `R-left-edge-odd` (`gilbreath-reduces-to-second-in-02`,
  proved), `R-finite-record-1e9` (`block-lemma-verification-bound-1e9`, checked), and
  `R-carved-gap24-full-survival` (`carved-gap24-is-r-lipschitz-corner` + `sweep-corner-mechanism`,
  proved — the model where every quantifier collapses to the bottom, correcting the
  several ladders that still list the {2,4} class as open).
- **First open rung, and the one to attack next:** `R-infinitely-often` — the weakest
  infinite-horizon statement for the primes, strictly weaker than the goal and strictly
  weaker than the already-open events-i.o. (R7). It needs no rate and no return-time law,
  only that the {0,2} corner is re-entered infinitely often.
- **The graded difficulty this ladder isolates:** `return-rate` — the step from
  `∃∞ k` (no frequency bound) to positive density (linear return count) to density one
  (sublinear failure set). No other ladder names it, because all of them keep `∀k` and
  pay for it with an input-class weakening instead.
- **Difficulty expected to bite:** `regeneration-rate` through `gap-arrangement`. Even the
  `R-infinitely-often` rung is currently open precisely because it is implied by (and is
  the weak shadow of) events-occurring-infinitely-often, which no held theorem provides
  for the deterministic prime gap word (ABGS 2011 §9 records the mod-4 switch frequency as
  named-open). The new value here is not a shortcut past that — it is the observation that
  the *weakest* form of the conjecture is strictly easier than the events-i.o. statement
  everyone else is chasing, and a soft recurrence argument might settle it first.
