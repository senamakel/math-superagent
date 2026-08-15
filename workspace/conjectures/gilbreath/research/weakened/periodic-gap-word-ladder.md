# Weakened ladder: the periodic gap word

> This ladder switches off the one difficulty every other ladder *bottoms out at*,
> rather than naming it obliquely. The input to the whole conjecture is the **gap
> word** `g = (g_1, g_2, g_3, ...)` with `g_1 = 2` and every `g_i` even positive
> (`A_1 = (1, g_1, g_2, ...)`). The conjecture is exactly the claim that this word
> lies in `S_∞ = { words : A_k(1) ∈ {0,2} for all k }`. The difficulty is that the
> *prime* gap word is aperiodic and unbounded. This ladder makes the gap word
> **eventually periodic**, where a finite-cycle argument turns the ∀k statement into
> a decidable finite check — and then turns `aperiodicity` back on, which is the
> whole open content.

The one-sentence bridge (proved, `gilbreath-reduces-to-second-in-02`): `A_k(0) = 1
⟺ A_k(1) ∈ {0,2}`, so every rung below states survival at position 1. The other
free fact (proved, `czz2011-ducci-2-lipschitz`): the row maximum is non-increasing,
so a gap word with max gap `M` keeps every entry of every row `≤ M` — this is what
makes the periodic case a *finite* system.

```ladder
goal: For A_0 = (2,3,5,7,11,13,...) the primes in order and A_{k+1}(i) = |A_k(i) − A_k(i+1)|, prove A_k(0) = 1 for every k ≥ 1 (Gilbreath's conjecture, Proth 1878 / Gilbreath 1958), equivalently: the prime gap word (g_1 = 2, g_i = p_{i+2} − p_{i+1}) satisfies A_k(1) ∈ {0,2} for every k ≥ 1.
difficulties: aperiodicity, unbounded-gap-values, infinite-horizon, gap-arrangement
status: open
```

The four difficulties, each specific:

- `aperiodicity` — the prime gap word (equivalently its mod-4 switch bit
  `h[j] = [gap_{j+1} ≡ 2 (mod 4)]`) is **not eventually periodic**: there is no
  `N, p` with `g_{i+p} = g_i` for all `i ≥ N`. This is the single obstruction the
  ladder is built to remove and then restore. Its content is measured, not just
  asserted: no unconditional linear lower bound on the mod-4 switch count exists
  (`abgs-2011-s9-mod4-switch-limit-open` — whether the pair frequency even tends to
  a limit is open). So no periodicity-based finiteness reaches the primes.
- `unbounded-gap-values` — prime gaps are unbounded, so there is no finite `M` with
  every row bounded by `M`; max-nonincrease (`czz2011-ducci-2-lipschitz`) is what
  fails, and the finite-state argument below dies without a finite `M`.
- `infinite-horizon` — the quantifier `∀ k ≥ 1` over rows. For a periodic word this
  is *discharged* by eventual periodicity of the left edge; it is not the hard part
  once `aperiodicity` is off.
- `gap-arrangement` — the positions/order of large gaps (6s) relative to shields
  (4s). Magnitude upper bounds provably cannot force survival
  (`gap-bounds-cannot-force-block-growth`, Eppstein's anti-Gilbreath construction),
  so it is the *arrangement*, not the size, that carries the difficulty. This ladder
  **never switches `gap-arrangement` off**: a periodic word is still a particular
  arrangement, and the whole point is to study the arrangement in its purest,
  decidable form.

---

```rung
id: R-per-gap-pure-periodic-small
statement: For pure-periodic gap words (g_1 = 2, g_{i+p} = g_i for all i ≥ 1, no preperiod) with period p ∈ {1,2,3,4,5,6,8} and gaps drawn from {2,4,6}, compute the left edge A_k(1) (equivalently A_{k+1}(0)) for k = 1..K with K large enough to exhibit the eventual cycle, and report for each word (preperiod T0, cycle C, cycle values, survival verdict: "A_k(1) ∈ {0,2} for all k" versus the first failing row). The {2,4}-only words are already known to all survive (settled `R-lipschitz-corner`); the point is the {2,4,6} words, where deaths are known to exist (the single-gap-6 word is eventually periodic, `R-spike-6-fatal`), so the table separates survivors from diers at the smallest nontrivial alphabet.
off: aperiodicity, unbounded-gap-values, infinite-horizon
stance: open
merge: Attack next. This is one bounded exact-integer computation (all words of the given periods over a 3-letter alphabet, K ~ a few thousand), and the deliverable is the table plus the observed eventual cycle for each word. Turning `infinite-horizon` back on is the next rung: prove the eventual cycle found is real for ALL k, not just k ≤ K.
```

```rung
id: R-per-gap-eventual-periodicity-theorem
statement: If the gap word g is eventually periodic (∃ N,p ≥ 1 with g_{i+p} = g_i for all i ≥ N), then the left edge A_k(1) is eventually periodic in k, and survival is DECIDABLE: there are explicit T0, C with A_{k+C}(1) = A_k(1) for all k ≥ T0, and C ≤ (M+1)^p · (M+1)^(N−1) where M = max gap, so checking the finitely many rows k ≤ T0+C decides whether A_k(1) ∈ {0,2} for all k.
off: aperiodicity, unbounded-gap-values
stance: open
merge: The proof is elementary and needs only a formalisation/check to settle. Sketch: (i) max-nonincrease (`czz2011-ducci-2-lipschitz`) bounds every row by M, so all state spaces below are finite; (ii) induction shows the interior tail i ≥ N is p-periodic in EVERY row (|A_k(i)−A_k(i+1)| is p-periodic because both operands are), so the tail block evolves as the CYCLIC Ducci map on p-tuples over {0..M} — a map on ≤ (M+1)^p states, hence eventually periodic in time with cycle C; (iii) the transient prefix i = 1..N−1 is then a finite-state system (≤ (M+1)^(N−1) states) driven by the C-periodic tail input, hence its first coordinate A_k(1) is eventually periodic. This is the precise left-edge + preperiod form of `czz2011-infinite-periodic-ducci-is-gilbreath-operator` (which is `unchecked` here and only covers the pure-periodic tail). Settling this makes every periodic gap word a finite question. Turn the next difficulty back on by *using* the decidability to classify rather than merely bound — R3.
```

```rung
id: R-per-gap-classify-246
statement: Classify survival for eventually-periodic gap words over the alphabet {2,4,6}: determine exactly which such words satisfy A_k(1) ∈ {0,2} for all k. Known partial: all {2,4}-only words survive (settled `R-lipschitz-corner`, since gaps ∈ {2,4} ⟹ |g_i − g_{i+1}| ∈ {0,2} ≤ 2); words containing a 6 can die (`R-spike-6-fatal` — a single 6 in a 2-background is eventually periodic with period 1 and fails at row 4). So the open content is exactly which periodic arrangements of 6s are shielded by left 4s — the periodic shadow of the open `R-leftmost-decides`.
off: aperiodicity, unbounded-gap-values
stance: open
merge: R2 makes each word a finite computation, but the *closed-form* classification in terms of the positions of 6s and shields is the real content, and it is where `gap-arrangement` first bites. If a periodic {2,4,6} word with a 6 survives, it is a concrete witness for the shield mechanism; if every unshielded 6 is fatal, the shield law is the classification. Expected first bite of the ladder: the arrangement of 6s relative to 4s, not their count. Turning `aperiodicity` back on within bounded gaps is R4.
```

```rung
id: R-per-gap-automatic-residue
statement: For a BOUNDED gap word (all gaps ≤ M) whose halved-gap bit string h[j] = (g_j/2) mod 2 is automatic (equivalently its F2 generating function is algebraic over F2(X)), the left-edge mod-4 residue A_k(1) mod 4 = 2·X_k is itself automatic, where X_k is the Pascal/Rule-90 fold of h over the gap window. This is the composition of the proved even-domain linearization `|a−b| ≡ a+b (mod 4)` (R-mod4-linearization) with the binary left-edge operator `T(f)(X) = f(X/(1+X))·(1/(1+X))` of the Proth–Gilbreath triangle (`bcz-2023-left-edge-stabilization`, an F2 involution that preserves algebraicity). Hence "A_k(1) is never a positive multiple of 4" is decidable by a finite automaton.
off: unbounded-gap-values
stance: open
merge: This turns `aperiodicity` back on within bounded gaps, and it is the first rung where it can bite: automatic words may be aperiodic, so the finite-cycle argument is gone and only automaton-decidability of the *residue* survives. The residue being automatic does NOT pin the exact value (0↔4, 2↔6 — the `exact-value` ceiling, `R-mod4-only-insufficient` failed). The merge to the goal needs the two things this rung deliberately does not have: unbounded gaps (turn `unbounded-gap-values` back on) and an exact-value lift (which the mod-4 ladder shows collapses onto the conjecture itself). Expected bite here: `aperiodicity` — automaticity gives decidability but no density, which is precisely the ABGS-open content.
```

```rung
id: R-per-gap-full
statement: The full goal: for A_0 = (2,3,5,7,11,13,...) the primes in order, A_k(0) = 1 for every k ≥ 1, equivalently A_k(1) ∈ {0,2} for every k ≥ 1 — equivalently, the prime gap word (aperiodic, unbounded) lies in S_∞.
off:
stance: open
merge: n/a — top of the ladder. Reaching it means `aperiodicity` and `unbounded-gap-values` are both back on and survived. The prime gap word is aperiodic and unbounded, and it sits strictly above the automaticity hierarchy this ladder climbs (its mod-4 switch count has no proved linear density, `abgs-2011-s9-mod4-switch-limit-open`), so none of the periodic/automatic finiteness machinery reaches it. That gap *is* the conjecture.
```

---

## Summary

- **Settled floor (imported, not new):** the parity reduction
  (`gilbreath-reduces-to-second-in-02`) and max-nonincrease
  (`czz2011-ducci-2-lipschitz`) — the two free facts that make the periodic case a
  finite system. The {2,4}-only periodic words are settled by `R-lipschitz-corner`.
- **Attack next:** `R-per-gap-pure-periodic-small` — one bounded computation, no proof
  needed, and it produces the table the structural rung (R2) must reproduce.
- **Cheapest real theorem:** `R-per-gap-eventual-periodicity-theorem` — elementary
  finite-system argument, settleable this run (Lean + machine check against R1's
  tables). It makes every eventually-periodic gap word a *decidable* instance of the
  conjecture, which is a theorem no existing ladder states.
- **Where the ladder first bites:** `R-per-gap-classify-246` — the arrangement of 6s
  relative to 4-shields, the periodic shadow of the open `R-leftmost-decides`.
- **Difficulty expected to actually bite (and finally defeat the ladder):**
  `aperiodicity` — first at `R-per-gap-automatic-residue`, where automatic aperiodic
  words enter and only residue-decidability survives, and definitively at the top
  rung, where the prime word has no finite period and its switch count has no proved
  linear density. That is the same named-open content every other ladder bottom out
  at, stated here from the input-word-complexity side.
