# Weakened ladder: the first-failure ladder

The six existing ladders organise the goal around its *forward* dynamics —
block regeneration, recharge accounting, spike propagation, the ν₂ supply. This
ladder is the dual object: it assumes the conjecture fails and studies the
**minimal failure**. Every rung is the goal with the named difficulties of a
first failure switched off, and the climb is the standard contradiction route
for a ∀ statement: characterise the first bad row, force its predecessor, and
find the step where the contradiction is supposed to land.

The one-sentence reduction that makes this a well-defined ladder (proved,
Lean-formalised, claim `gilbreath-reduces-to-second-in-02`): the conjecture is
equivalent to **A_k(1) ∈ {0,2} for every k ≥ 1**. A *first failure* is a
minimal k with A_k(1) ∉ {0,2}; then A_j(1) ∈ {0,2} for all 1 ≤ j < k, so
A_{k−1}(0) = 1 and the failing value is A_k(1) = |A_{k−1}(1) − A_{k−1}(2)|.

**The five difficulties.**

- `infinite-horizon` — the goal quantifies ∀k; any finite check is a fact about
  that depth only.
- `edge0-death` — one of exactly two death modes: the last-live block has edge
  0 and the intruder y ≥ 4 escapes as the next row's second entry
  (|0 − y| = y ≥ 4).
- `edge2-death` — the other death mode: the last-live block has edge 2 and the
  intruder y ≥ 6 escapes (|2 − y| ≥ 4 ⟺ y ≥ 6; |2 − 4| = 2 is safe).
- `fan-width` — excluding a first failure forces a backward trace through the
  block's erosion history, and A_k(1) depends on the first k+1 gaps; the fan
  the trace must climb is unbounded.
- `gap-arrangement` — the specific primes' unbounded, non-concentrated gap
  sequence; it is the only thing separating the primes (no failure) from
  Colonna's deletion sequences (failures), so any exclusion that does not use
  it must fail.

```ladder
goal: For A_0 = (2,3,5,7,11,13,...) the primes in order and A_{k+1}(i) = |A_k(i) − A_k(i+1)|, prove A_k(0) = 1 for every k ≥ 1 (Gilbreath's conjecture, Proth 1878 / Gilbreath 1958)
difficulties: infinite-horizon, edge0-death, edge2-death, fan-width, gap-arrangement
status: open
```

## Rungs, bottom to top

```rung
id: R-first-failure-shape
statement: In any 2-then-odds triangle, let k ≥ 2 be minimal with A_k(1) ∉ {0,2}. Then A_{k−1}(0) = 1, A_{k−1}(1) = e ∈ {0,2}, A_{k−1}(2) = y is even, and |e − y| ≥ 4, so the leading block of row k−1 has length exactly 1 and the failure occurs by exactly one of two modes: (a) e = 0 and y ≥ 4, or (b) e = 2 and y ≥ 6.
off: infinite-horizon, edge0-death, edge2-death, fan-width, gap-arrangement
stance: settled
merge: This is the bare shape, no exclusion claimed (that is why every difficulty is off). It is a one-line corollary of the proved reduction (claim gilbreath-reduces-to-second-in-02) plus second-entry-4-kills and the arithmetic |e−y| ≥ 4 with e ∈ {0,2}, y even. Restore the exclusion: turn on `edge2-death` and `edge0-death` one at a time and ask whether either mode is reachable at all in the class.
```

```rung
id: R-erosion-chain
statement: A first failure forces the leading block to be dead at row k (b_k = 0) and b_j to decrease by exactly one on every non-(2,4) step of the descent, so the failure is a strict erosion of the block to length 0; the recharge identity b_k = b_1 + Σ_{i<k}(j_i+1) − (k−1) is the exact accounting of the path that leads to it.
off: edge0-death, edge2-death, gap-arrangement
stance: settled
merge: This is the proved step law + recharge identity (claim step-law-theorem-proved) restated on the minimal-failure path. It settles the *consumption* half of the failure story and leaves the two death modes and the fan as the entire remaining content. First move: none needed — proceed to the two mode-exclusion rungs, which is where the ladder first becomes nontrivial.
```

```rung
id: R-consecutive-odds-no-first-failure
statement: For A_0 = (2,3,5,7,9,...) (consecutive odd numbers, every gap 2), there is no first failure: A_k(1) ∈ {0,2} for all k ≥ 1. Equivalently, no k is a first failure in this class, so both death modes are unattainable here.
off: gap-arrangement, edge0-death, edge2-death, fan-width
stance: settled
merge: This is the run's proved consecutive-odds class (claim/claims behind R2-consecutive-odds-class): row 2 onward is the corner and {0,2} closure carries the leading 1 forever, discharging `infinite-horizon` without touching the death modes. Restoring any difficulty: turn `gap-arrangement` back on (non-uniform gaps) — the failure modes become live immediately, which is exactly what the next two rungs test.
```

```rung
id: R-edge2-death-excluded
statement: In any 2-then-odds triangle with first even gap g_1 = 2 (so A_1 = (1,2,...)), a first failure cannot occur by mode (b): there is no k with A_{k−1} = (1, 2, y, ...), y ≥ 6, and A_j(1) ∈ {0,2} for all j < k.
off: edge0-death, fan-width, gap-arrangement
stance: failed
killed-by: Colonna's delete-7 example (2,3,5,11,13,17,19,...): gaps (1,2,6,2,4,2), A_1 = (1,2,6,2,4,2), A_2 = (1,4,4,2,2). Here A_1(1)=2 ∈ {0,2} and A_2(1)=|2−6|=4, so k=2 is a first failure by mode (b) with edge 2 and intruder 6. The claim colonna-deletion-left-edge-failure records the row data.
reason: The mode-(b) exclusion is FALSE as a universal class statement. Colonna's delete-7 sequence has g_1 = 2 yet fails at row 2 exactly through edge 2 and intruder 6. So `edge2-death` cannot be excluded by any local/two-row argument that ignores the gap arrangement.
merge: The failure is the finding: `edge2-death` is realizable at g_1 = 2, so the conjecture's truth must live in `gap-arrangement` (or a non-concentration condition), not in a universal exclusion of the intruder-≥6 mode. The surviving climb is to the {2,4}-gap class (R-carved-gap24-no-first-failure), where the intruder-6 killer is absent structurally, or to a frequency condition tolerating rare ≥6 gaps.
```

```rung
id: R-edge0-death-excluded
statement: In any 2-then-odds triangle with first even gap g_1 = 2, a first failure cannot occur by mode (a): there is no k with A_{k−1} = (1, 0, y, ...), y ≥ 4, and A_j(1) ∈ {0,2} for all j < k.
off: edge2-death, fan-width, gap-arrangement
stance: failed
killed-by: Colonna's delete-11 example (2,3,5,7,13,17,19,...): gaps (1,2,2,6,4,2), A_1 = (1,2,2,6,4,2), A_2 = (1,0,4,2,2), A_3 = (1,4,2,...). Here A_1(1)=2, A_2(1)=0 are both in {0,2}, and A_3(1)=|0−4|=4, so k=3 is a first failure by mode (a) with edge 0 and intruder 4. The claim colonna-deletion-left-edge-failure records that delete-11 fails; the row arithmetic is elementary.
reason: The mode-(a) exclusion is FALSE as a universal class statement: delete-11 has g_1 = 2 and fails at row 3 through edge 0 and intruder 4. So `edge0-death` is also realizable at g_1 = 2, and no two-row backward forcing can exclude it in general.
merge: Both death modes are now shown reachable in the class, which is the sharp content of this ladder: **the gap-arrangement difficulty bites at the very first step**, and any universal "no first failure" claim with it switched off is false. The only surviving weakened targets are (i) a structural class where the killers are absent — the {2,4}-gap class, next rung — or (ii) a frequency bound on ≥6 gaps, the seed of a non-concentration condition for the primes.
```

```rung
id: R-carved-gap24-no-first-failure
statement: Let A_0 = (2,3,x_1,x_2,...) with every x_i odd, x_1 − 3 = 2, and x_{i+1} − x_i ∈ {2,4} for all i ≥ 1 (gaps after the first all 2 or 4). Then there is no first failure: A_k(1) ∈ {0,2} for all k ≥ 1. This is the goal with the unbounded, irregularly arranged gap sequence switched off; it is the first-failure view of the run's open rung R-carved-gap24 (recharge-ladder) and R-gaps-24 (spike-propagation-ladder). Note the class structure also kills mode (b): A_1 has all entries in {2,4} and the row maximum is non-increasing, so no intruder ever exceeds 4.
off: gap-arrangement, edge2-death
stance: open
merge: Turn `gap-arrangement` back on — the single step from this rung to the primes. First move: since both universal death-mode exclusions above are refuted by a single 6 (delete-7, delete-11), understand how one ≥6 gap inserted into a {2,4} stream either (a) is shielded by the left-4 structure or (b) escapes; the {2,4} class has no such gap, which is the whole reason it is the natural floor of the gap-arrangement difficulty. Empirical support only: 0 deaths among 48 measured {2,4} sequences to depth 4000 (event-rate sweep) — not a proof. This is the rung to attack next.
```

```rung
id: R-full
statement: The full goal: for the primes in order, A_k(0) = 1 for every k ≥ 1, equivalently A_k(1) ∈ {0,2} for every k ≥ 1, equivalently no first failure exists in the prime triangle.
off:
stance: open
merge: n/a — top of the ladder. The ladder is exhausted exactly when this rung is settled. The two universal death-mode exclusions failed, which is the proof that reaching this rung requires the gap-arrangement difficulty to be turned back on and survived — the same single open content the regeneration and recharge ladders locate, seen here from the failure side.
```
