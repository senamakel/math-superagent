# SUPPLY — the growth-rate ladder (the fixed prime string, pointwise)

This ladder weakens SUPPLY along the one axis the other ladders do not: the
*growth rate* of `ν₂(n)` for the real prime string, kept pointwise and with the
primes on throughout. `supply.md` weakens by switching off the primes (random
`h`) and the pointwise quantifier (density-1 set); `supply-threshold-limit.md`
owns the `w/n` threshold where linear supply becomes *typical* (GOAL's head
question). Neither asks the intermediate question this ladder asks, and the
problem's own result type 2 (`ν₂(n) > n^β` for `β > 0.525`) lives here and
nowhere else.

The climb is: `ν₂ ≥ 1` (rank/nullity + the prime prefix) → `ν₂ → ∞` →
`ν₂ ≥ n^β` for some `β > 0` → `β > 0.525` → `ν₂ ≥ c·n` (SUPPLY). Each rung
keeps the primes and the pointwise quantifier fixed and only turns up the
demanded rate.

```ladder
goal: There is a constant c > 0 such that ν₂(n) ≥ c·n for all sufficiently large n, where ν₂(n) = wt(Φ_n h) over F₂, h[j] = ((q_{j+1} − q_j)/2) mod 2, and Φ_n is the Pascal-mod-2 fold of problem.md (rows d = 2..n−1).
difficulties: primes-input, pointwise-all-n, collapse-ruleout, power-rate, threshold-rate, linear-rate
status: open
```

- `primes-input` — unconditional control of the prime gap-parity string `h` is
  the parity barrier (positive mod-4 switch density is open, ABGS 2011 §9).
  **ON in every rung of this ladder** — the primes are never switched off; the
  weakening is all in the rate. (The primes-off branch lives in `supply.md`.)
- `pointwise-all-n` — the bound must hold for every `n ≥ N₀`, not merely on a
  density-1 set. **ON in every rung of this ladder** — this is deliberately the
  pointwise axis; the averaged branch is `supply.md`'s `R-averaged-supply`.
- `collapse-ruleout` — show `ν₂(n)` is unbounded, i.e. the fold does not
  collapse to bounded weight on the *fixed* prime window. This needs a
  kernel-approximation lemma (bounded `ν₂` ⇒ `h` eventually 2-power-periodic),
  which is **not a theorem in the library** and is threatened by the fixed
  Thue–Morse string (aperiodic; its `ν₂` is only known to be sublinear, not
  whether it is O(1)).
- `power-rate` — promote unboundedness to a *uniform* `n^β` for some fixed
  `β > 0`; infinitely-often growth is not a rate.
- `threshold-rate` — reach `β > 0.525`, the specific exponent problem.md names
  as result type 2 (source of the 0.525 not re-derived here).
- `linear-rate` — promote sublinear `n^β` to linear `c·n`; the final
  parity-barrier step, inherited from every other route.

```rung
id: R-nu2-ge-1
statement: ν₂(n) ≥ 1 for every n ≥ 4, for the real prime string h (floored convention, d ∈ [2, n−1]). This is the β = 0 floor of the rate axis: the fold image is nonzero for the fixed prime window. Derivation: ν₂(n) = wt(Φ_n h), and wt(Φ_n h) = 0 iff Φ_n h = 0 iff h ∈ ker Φ_n; by the proved all-n rank fact (fold-rank-n-minus-2-binomial-proved), ker Φ_n = span(even-alt, odd-alt) = the period-2 strings {0000…, 1111…, 0101…, 1010…}. The prime prefix h[0..3] = 1110 (primes 2,3,5,7,11 are 2,3,1,3,3 mod 4, so the switch indicators are 1,1,1,0) is none of the four period-2 strings, so h ∉ ker Φ_n and wt(Φ_n h) ≥ 1 for n ≥ 4. The on-disk capture seq_nu2_from2 confirms the sharpness: ν₂(3) = 0 (prefix 111 is the all-ones kernel prefix) and ν₂(4) = 2.
off: collapse-ruleout, power-rate, threshold-rate, linear-rate
stance: settled
merge: Settled by the proved rank/nullity fact plus a hand-check of the first four prime gap bits (both already in the library; no new computation). Turn `collapse-ruleout` back on: the next rung asks whether this single guaranteed nonzero cell grows to infinitely many. First move is R-nu2-unbounded.
```

```rung
id: R-nu2-unbounded
statement: ν₂(n) → ∞ as n → ∞, for the real prime string h. Equivalently, the fold does not collapse to bounded weight on the fixed prime window (the per-window closed-door witnesses do not settle this, because they are per-window, not fixed strings). For every B there is N₀(B) with ν₂(n) > B for all n ≥ N₀(B) — or, failing that, a fixed aperiodic witness h with ν₂(n) = O(1) is exhibited.
off: power-rate, threshold-rate, linear-rate
stance: open
merge: The first move is a two-fronted attack. (a) Resolve the threat first: compute whether the FIXED Thue–Morse string has ν₂ = O(1) or unbounded — it is the falsifier for the lemma "wt(Φ_n h) ≤ B for all large n ⇒ h eventually 2-power-periodic"; if Thue–Morse is O(1) and aperiodic, the lemma is dead and `collapse-ruleout` needs a different engine. (b) If the lemma survives, prove it via dyadic shifts: bounded weight forces each anchor position i to satisfy h[i − 2^m] = h[i] for all but ≤ B powers of two, and an overlap/counting argument should force eventual periodicity; then the primes' non-eventual-periodicity (problem.md result 5, conditional on Shiu 2000, sourced locally) gives ν₂ → ∞. Expected bite: `collapse-ruleout` — this is the rung where the near-kernel/per-window distinction first costs real work.
```

```rung
id: R-nu2-nbeta
statement: There is a fixed β > 0 with ν₂(n) ≥ n^β for all sufficiently large n, for the real prime string h. Unboundedness is upgraded to a uniform polynomial rate: the fold grows at least as fast as some positive power of n, however small.
off: threshold-rate, linear-rate
stance: open
merge: Turn `power-rate` back on is exactly this rung's content; settle it by a rate version of the collapse-ruleout argument. If bounded weight forces near-periodicity, then sub-polynomial (but unbounded) weight forces a quantified weakening of periodicity — an exception set on the dyadic-shift structure with density tied to the exponent. The first move is to derive that density/exponent tradeoff: how many exceptions per anchor force ν₂ ≥ n^β, and does the resulting structure still contradict the primes' non-periodicity. Expected bite: `power-rate` — going from "infinitely many odd depths" to "at least n^β odd depths for a fixed β" is where a real exponent must be named, not borrowed.
```

```rung
id: R-nu2-nbeta-0525
statement: ν₂(n) ≥ n^β for β > 0.525, for all sufficiently large n, for the real prime string h. This is problem.md's result type 2 verbatim — the stated intermediate target below linear supply.
off: linear-rate
stance: open
merge: Turn `threshold-rate` back on. The first move is to name where the 0.525 exponent originates (a sieve/concentration threshold — not re-derived in this workspace, and not to be assumed) and whether the engine that sets it is available unconditionally; if 0.525 is an artifact of a specific sieve bound rather than a structural constant, the honest statement is the best β the available engine yields, whatever it is. Expected bite: `threshold-rate` — the exact exponent is the least-understood knob, and it must be sourced, not fitted.
```

```rung
id: R-nu2-linear
statement: There is a constant c > 0 with ν₂(n) ≥ c·n for all sufficiently large n — the full SUPPLY conjecture, no difficulty switched off.
off:
stance: open
merge: Terminal rung of this ladder. If every previous rung merges back, the rate has been promoted from n^β through 0.525 to linear, and this rung is reached. Expected last bite: `primes-input` (the parity barrier) through `linear-rate` — the step from sublinear to linear is where the known dead-end reduction (positive mod-4 switch density) re-enters, and beating it is the whole problem.
```
