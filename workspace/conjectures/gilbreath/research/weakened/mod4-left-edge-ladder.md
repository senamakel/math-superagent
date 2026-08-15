# Weakened ladder: the mod-4 residue of the left edge

> Complements the other ladders on a genuinely different axis. `granville-nu2-supply-ladder`
> counts 2s in the **right diagonal** (the supply side of Route B). This ladder is about
> the **left-edge second entry** `A_k(1)` and its residue mod 4. The spine of the ladder is
> a single difficulty the others name only obliquely: `exact-value` — the difference
> between the residue `A_k(1) mod 4` and the exact value `A_k(1) ∈ {0,2}`.

The one-sentence motivation: for even entries `|a−b| ≡ a+b (mod 4)`, so the whole even
interior of a Gilbreath triangle becomes a **linear** system mod 4, and `A_k(1) mod 4`
is an F2-linear (Pascal/Rule-90) fold of the mod-4 switch bits of the prime gaps. The
library already carries this as `mod4-linearization` / `odlyzko-mod4-linearization` —
but only `asserted`, not proved or checked here. So the bottom of this ladder is a
genuinely cheap new result, and the top documents exactly where the residue axis stops.

**The five difficulties.**

- `infinite-horizon` — the conclusion quantifies over every k ≥ 1 with no finite bound;
  a finite check is a fact about that depth only.
- `exact-value` — the goal is the exact statement `A_k(1) ∈ {0,2}`. Mod 4 conflates
  `0↔4` and `2↔6`, so residue data alone cannot pin the exact value; this is the
  difficulty the ladder tries to switch off, and it is the one expected to bite.
- `regeneration-rate` — the (2,4)-event arrival / recharge surplus
  `Σ_{i<k}(j_i+1) ≥ k−2` is the open core (`step-law-theorem-proved`); consumption is
  settled, this rate is not.
- `gap-arrangement` — the deterministic, unbounded, irregular prime gap sequence; the
  residue formula reads the switch bits off it, but proving anything about their
  Pascal-folds needs the arrangement itself.
- `non-concentration` — no independence / 2-separated hypothesis holds for the primes;
  every proved "events recur" theorem is a random analogue (Chase 2024, CHT 2026).

```ladder
goal: For A_0 = (2,3,5,7,11,13,...) the primes in order and A_{k+1}(i) = |A_k(i) − A_k(i+1)|, prove A_k(0) = 1 for every k ≥ 1 (Gilbreath's conjecture, Proth 1878 / Gilbreath 1958), equivalently A_k(1) ∈ {0,2} for every k ≥ 1.
difficulties: infinite-horizon, exact-value, regeneration-rate, gap-arrangement, non-concentration
status: open
```

## Rungs, bottom to top

```rung
id: R-mod4-linearization
statement: For even nonnegative a,b, |a−b| ≡ a+b (mod 4). Consequently in any 2-then-odds triangle (A_1 = (1, even, even, ...)), every row k ≥ 2 has entries in columns ≥ 1 even, and A_{k+1}(i) ≡ A_k(i) + A_k(i+1) (mod 4) for all i ≥ 1: the even interior evolves linearly mod 4.
off: exact-value, regeneration-rate, gap-arrangement, non-concentration
stance: open
merge: This is a two-line proof (for even b, a−b ≡ a+b mod 4 because 2b ≡ 0; and |x| ≡ x mod 4 for even x), but the ledger currently carries it only as `odlyzko-mod4-linearization` and `mod4-linearization` with status **asserted** (sourced, not proved or checked here). Settling it upgrades two asserted claims to proved and is the cheapest new result on the ladder — one forward attempt, then Lean-formalise the even-domain identity. The linearization is the whole reason the next rung is an F2-linear object rather than a nested absolute value.
```

```rung
id: R-switch-xor-residue
statement: With h_j = [gap_{j+2} ≡ 2 (mod 4)] the mod-4 switch bit of the prime gaps, A_k(1) ≡ 2·X_k (mod 4), where X_k = XOR over j=0..k−1 with C(k−1,j) odd of h_j (the Pascal-mod-2 / Rule-90 fold of the switch bits over the gap window [2, k+1]). In particular A_k(1) mod 4 ∈ {0,2}, and the residue is an F2-linear function of the gap sequence.
off: exact-value, regeneration-rate, gap-arrangement, non-concentration
stance: open
merge: A one-line induction from R-mod4-linearization (Pascal-fold of a mod-4-linear recurrence with A_1(1+j) ≡ 2·h_j mod 4). Settle it right after R-mod4-linearization; it is the bridge that turns "the interior is linear mod 4" into a concrete invariant at position 1. It does NOT touch survival — it only says the residue is governed by a clean linear rule. Turn `exact-value` back on next and ask what the residue cannot see.
```

```rung
id: R-residue-weakened-target
statement: For the prime triangle, A_k(0) ≡ 1 (mod 4) for every k ≥ 1 — equivalently, A_k(1) is never a positive multiple of 4 (never 4, 8, 12, ...). This is the goal with the exact value {0,2} replaced by its mod-4 residue. It is strictly weaker than the goal: a first failure of value 6 (≡ 2 mod 4) violates the conjecture but not this statement.
off: exact-value
stance: open
merge: Turn `exact-value` back on. The residue statement is equivalent to "whenever the switch-XOR X_k = 0 (so A_k(1) ≡ 0 mod 4), the exact value is A_k(1) = 0, never 4, 8, ...". The smallest positive multiple of 4 is 4, which is exactly the canonical first-failure killer (a first failure with value 4 makes A_{k+1}(0) = |1−4| = 3 ≡ 3 mod 4). So this rung bites at the same place the full conjecture does: proving "never a positive multiple of 4" requires at minimum ruling out the value 4, which is Gilbreath's conjecture. This is the ladder's honest finding, not a path. The only thing the residue axis genuinely buys is the exact *location* where the exact value must be resolved: precisely the rows with X_k = 0.
```

```rung
id: R-mod4-only-insufficient
statement: The residue A_k(1) mod 4 alone determines whether A_k(1) ∈ {0,2} (i.e. the mod-4 data suffices to force survival).
off: exact-value, regeneration-rate, gap-arrangement, non-concentration
stance: failed
killed-by: residue 0 is realized by both survival and death. The corner (1,0,0,...) has A_k(1) = 0 ≡ 0 (mod 4) and survives; the single-gap-6 death, gaps (2,2,6,2,2,...), has A_2(1) = 4 ≡ 0 (mod 4) and dies (this run's `R-spike-6-fatal` / `R-intruder-le-6`). So residue 0 cannot separate the safe value 0 from the killer 4.
reason: mod 4 is the ceiling exactly because it conflates the failure values (0↔4, 2↔6) — the run's already-established finding that the mod-4 lift is the ceiling and mod 8 and above are dead (`|a−b| ≡ a+b mod 2^t` over evens fails at t=3). No mod-4-only invariant can force the exact {0,2} statement.
merge: The failure is the finding: the residue axis cannot climb to the exact goal — `exact-value` is not switchable by mod 4. What survives is R-mod4-linearization and R-switch-xor-residue, which are exact and new: they reduce the *nonlinear* question "is A_k(1) ∈ {0,2}?" to the *linear* statement "the switch-XOR X_k vanishes iff A_k(1) = 0 exactly", i.e. they say where the exact value must be resolved (only when X_k = 0) without resolving it.
```

```rung
id: R-full
statement: The full goal: for the primes in order, A_k(0) = 1 for every k ≥ 1 — equivalently A_k(1) ∈ {0,2} for every k ≥ 1, equivalently Σ_{i<k}(j_i+1) ≥ k−2 for all k.
off:
stance: open
merge: n/a — top of the ladder. Reaching it means `exact-value` has been turned back on and survived, which the failed rung R-mod4-only-insufficient shows the residue axis cannot do; the climb must leave this axis and rejoin `regeneration-rate`, which is the shared open core of every ladder.
```

## Summary

- **Settle first (cheap new results):** R-mod4-linearization and R-switch-xor-residue. Both are
  one-line corollaries currently only `asserted` in the library; proving them upgrades two
  asserted claims to proved and gives an exact F2-linear residue invariant at position 1
  that no other ladder states in this form.
- **Failed and kept:** R-mod4-only-insufficient — residue 0 is realized by both the safe
  value 0 (corner) and the killer 4 (single-gap-6 death), so no mod-4-only invariant can
  force the conjecture. The reason is the established mod-4-is-the-ceiling fact.
- **Open, and the honest finding:** R-residue-weakened-target ("A_k(0) ≡ 1 mod 4 for all k")
  is strictly weaker than the goal — a value-6 first failure does not violate it (hand check:
  gaps (2,2,8,2,2,...) gives A_1=(1,2,2,8,2,2,...), A_2=(1,0,6,6,0,...), A_3=(1,6,0,6,...),
  A_4=(5,6,6,...): first failure value 6, yet A_4(0)=5 ≡ 1 mod 4 — confirm against the oracle).
  But the first place it bites is value 4, the canonical first-failure killer, so the
  weakening collapses onto the full conjecture at exactly value 4.
- **Difficulty expected to bite:** `exact-value`. The mod-4 axis resolves the residue but not
  the value, and the value 4 (≡ 0 mod 4) is where the conjecture lives; `regeneration-rate`
  is the shared deep difficulty every ladder bottoms out at.
