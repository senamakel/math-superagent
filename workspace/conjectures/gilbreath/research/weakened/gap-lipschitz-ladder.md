# Weakened ladder: the gap-jump axis (corner vs injected defects)

This ladder decomposes Gilbreath's conjecture along the *gap-sequence Lipschitz*
axis, which the existing canonical ladder (`recharge-ladder.md`) names only
obliquely as `unbounded-gap-arrangement`. The new observation (settled, trivial,
but not previously recorded as such): the corner is reached at row 2 whenever the
gaps are 1-Lipschitz, so the *entire* difficulty is the gap-jumps of size ≥ 4 and
whether the value ≥ 4 they inject into row 2 is healed before it reaches the left
edge.

Two statuses here correct the existing ledgers:

- `R-carved-gap24` (recharge-ladder, marked open) is **settled** — it is the special
  case `gaps ⊆ {2,4}` of `R-lipschitz-corner` below (adjacent diffs of `{2,4}`-valued
  gaps are in `{0,2}` automatically), and the proof is one line, not "empirical
  support only". Claim `sweep-corner-mechanism` already records this.
- `R-intruder-4` (gilbreath-regeneration-ladder, marked open) is **settled by
  assembly** from two proved claims: `step-law-theorem-proved` + 
  `edge-interior-invertibility-sharpened`. Proof in the rung.

```ladder
goal: For A_0 = (2,3,5,7,11,13,...) the primes in order and A_{k+1}(i) = |A_k(i) − A_k(i+1)|, prove A_k(0) = 1 for every k ≥ 1 (Gilbreath's conjecture, Proth 1878 / Gilbreath 1958).
difficulties: infinite-horizon, regeneration-rate, gap-lipschitz, intruder-coincidence, non-concentration
status: open
```

What each difficulty names, exactly:

- `infinite-horizon` — the conclusion quantifies over every k ≥ 1 with no finite
  bound; a finite check is a fact about that depth only.
- `regeneration-rate` — the (2,4)-event arrival rate is unproved. GC is exactly
  `Σ_{i<k}(j_i+1) ≥ k−2` for all k (`step-law-theorem-proved`); nobody has shown
  events keep arriving fast enough. This is the whole open core.
- `gap-lipschitz` — adjacent input gaps may differ by ≥ 4 (e.g. a 2→6 jump, which
  the primes have at gap index 9→10: `...,6,2,...`). A jump of 4 injects a value 4
  into row 2; a jump of ≥ 6 injects ≥ 6. Row 2 is the all-{0,2} corner *iff* the
  gaps are 1-Lipschitz (see R-lipschitz-corner). This is the concrete form of
  `unbounded-gap-arrangement`.
- `intruder-coincidence` — a (2,4)-event needs edge = 2 **and** intruder = 4 in the
  *same* row. Edge-invertibility forces edge = 2 at least once per block lifetime,
  but the intruder value at those rows is uncontrolled.
- `non-concentration` — the deterministic prime gap sequence carries no
  independence / frequency hypothesis; every proved "events recur" theorem is a
  random analogue (Chase 2024, CHT 2026) whose hypotheses are unchecked for the
  primes.

---

```rung
id: R-parity-reduction
statement: For ANY sequence beginning (2, 3, odd, odd, ...) — equivalently any A_1 = (1, even, even, ...) — every row A_k has shape (odd, even, even, ...): A_k(0) is odd for all k, and A_{k+1}(0) = 1 ⟺ A_k(1) ∈ {0,2}. The weakened target settled here is the parity half; the ⟺ is the bridge to the exact target. Claim `gilbreath-reduces-to-second-in-02`.
off: regeneration-rate, gap-lipschitz, intruder-coincidence, non-concentration
stance: settled
merge: Restore magnitude content — distinguish {0,2} from {4,6,...}. First move: prove a difference of two {0,2} entries is in {0,2}, and that a row (1,c,c,c,...) with c∈{0,2} is a fixed shape (next rung).
```

```rung
id: R-corner-closure
statement: If some row equals (1, c, c, c, ...) with every c ∈ {0,2} (the "corner"), then every later row begins with 1. The corner is a fixed shape: |1−c| = 1 for c∈{0,2}, and a difference of two {0,2} entries is in {0,2}. Claim `closure-0d-double-edge`.
off: regeneration-rate, gap-lipschitz, intruder-coincidence, non-concentration
stance: settled
merge: The corner is the absorbing state; reaching it solves everything. Restore the question of *reaching* it: which input gap sequences put row 2 already in the corner? Next rung answers that exactly.
```

```rung
id: R-lipschitz-corner
statement: For a 2-then-odds sequence with first gap g_1 = 2 and |g_i − g_{i+1}| ≤ 2 for all i ≥ 1 (the gap sequence is 1-Lipschitz), A_2 is the all-{0,2} corner, hence A_k(0) = 1 for every k ≥ 1. Proof: g_2 ∈ {2,4} is forced (g_2 even, |g_2−2|≤2); A_2(1) = |2−g_2| ∈ {0,2} and A_2(i) = |g_i−g_{i+1}| ∈ {0,2} for all i ≥ 2, so row 2 is the corner; closedness (R-corner-closure) finishes. Strictly generalises the consecutive-odds case (all gaps 2) and R-carved-gap24 (gaps ⊆ {2,4}); also admits 1-Lipschitz chains like (2,4,6,4,2,...) with a 6, because |4−6|=2 is harmless.
off: regeneration-rate, intruder-coincidence, non-concentration
stance: settled
merge: Turn `gap-lipschitz` back on minimally — allow one adjacent jump of size 4 (a single 6 in a {2,4} background). That is R-single-gap-jump-4, and it fails. The lesson: even *one* jump injects a 4 that propagates to the left edge. The first move up that actually survives is to face the injected value directly and ask when it is healed — that is R-intruder-4-always, which pins the intruder instead of the gaps.
```

```rung
id: R-intruder-4-always
statement: For any 2-then-odds triangle whose block-boundary intruder value is 4 at every row where the block is nonempty (y_k = A_k(b_k+1) = 4), the leading 1 persists forever. Proof by assembly of two proved claims: the step law gives growth ⟺ (edge,intruder)=(2,4), so with intruder≡4 growth ⟺ edge=2; edge-invertibility says a nonzero block of length n shows edge 2 at least once in its n erosion reads, so an event-free stretch has length ≤ n−1 < n and the block never reaches length 0.
off: intruder-coincidence, non-concentration
stance: settled
merge: This is the last settled rung, and it isolates the bite exactly. It pins the *intruder* and concludes survival; it says nothing about whether the prime rows realize intruder = 4 often enough, or at all. The difficulty that bites is `regeneration-rate` in its concrete form: an intruder ≥ 6 (injected by a gap-jump ≥ 4) forces erosion even at edge 2, so the block dies unless a coincident (edge=2, intruder=4) event heals the injected value first. Restore that — next open rung.
```

```rung
id: R-single-gap-jump-4
statement: For a 2-then-odds sequence with g_1 = 2, gaps in {2,4} except a single 6 (equivalently: 1-Lipschitz except one adjacent jump of size 4), the leading 1 persists forever.
off: non-concentration
stance: failed
killed-by: gaps (2,2,6,2,2,2,...) — A_0=(2,3,5,7,13,15,17,19,...), A_1=(1,2,2,6,2,2,2,...), A_2=(1,0,4,4,0,0,...), A_3=(1,4,0,4,0,...), A_4=(3,4,4,4,...). A_4(0)=3: dead at row 4.
reason: A single 2→6 (or 6→2) jump injects a 4 into row 2 (|2−6|=4). The 4 propagates one position left per row (|0−4|=4) until it becomes the second entry (row 3) and then the leading entry (|1−4|=3, row 4). In a pure {0,2} background it is healed iff a 2 sits immediately to its left (|2−4|=2); here the left neighbour is 0, so it is not healed. Sharper than Colonna delete-5 (whose killer is g_1=4, not a jump): this fixes g_1=2 and still dies.
merge: Even a single non-Lipschitz jump kills unless the injected 4 meets a 2 to its left. So survival is exactly the statement that the {0,2} interior always supplies a 2 to the left of each injected 4 in time — the coincidence difficulty. The next surviving rung is not a wider gap class (R-bounded-gap-4, below, fails) but a frequency/arrangement condition, which is the open core.
```

```rung
id: R-bounded-gap-4
statement: For every 2-then-odds sequence with all gaps (after the first) ≤ 4, the leading 1 persists forever — the deterministic bounded-gap class at g = 4.
off: gap-lipschitz
stance: failed
killed-by: Colonna's delete-5 example (2,3,7,11,13,17,...): gaps (1,4,4,2,4,2) all ≤ 4, but g_1 = 4, so A_2(0) = |1−4| = 3 — dead at row 2. Eppstein's anti-Gilbreath construction kills every fixed g ≥ 4.
reason: The class does not force g_1 = 2, and g_1 = 4 alone already kills at row 2 (|1−4|=3). Eppstein 2011 kills every fixed g. The deterministic bounded-gap route is dead; only g = 2 (consecutive odds, in R-lipschitz-corner) survives as a plain bound.
merge: No bounded-gap class survives. The surviving route is a *frequency* restriction tolerating rare large gaps — the deterministic seed of a non-concentration condition — which is the open core; see next rung.
```

```rung
id: R-primes-events-infinitely-often
statement: For the prime triangle, (2,4)-regeneration events occur infinitely often as k → ∞. Strictly weaker than the goal (occurrence, not rate), and the natural first target with the prime gap arrangement switched back on. In the gap-jump framing: infinitely many of the values ≥ 4 injected by gap-jumps of size ≥ 4 are healed back into {0,2} by a coincident (edge=2, intruder=4) event before they reach the left edge.
off: regeneration-rate
stance: open
merge: Infinitely-often is necessary but not sufficient: the recharge surplus Σ(j_i+1) must never fall k−2 behind, so a *rate* statement is required. First move: measure the gap-jump sites of the prime gap sequence against the (2,4)-event rows of the depth-1000 data and see whether each injected defect is healed within a bounded number of rows — that bound is the seed of a rate.
```

```rung
id: R-full
statement: The full goal: for the primes in order, A_k(0) = 1 for every k ≥ 1, equivalently A_k(1) ∈ {0,2} for every k ≥ 1, equivalently Σ_{events i<k}(j_i+1) ≥ k−2 for all k.
off:
stance: open
merge: n/a — top of the ladder. Reached exactly when the injected-defect healing rate (R-primes-events-infinitely-often, upgraded from occurrence to rate) is proved for the prime gap arrangement.
```

---

## Summary

- **Settled (bottom to the last-but-one rung):** R-parity-reduction,
  R-corner-closure, R-lipschitz-corner, R-intruder-4-always. All are already in
  the library as proved claims (`gilbreath-reduces-to-second-in-02`,
  `closure-0d-double-edge`, `sweep-corner-mechanism` + the trivial 1-Lipschitz
  generalisation, `step-law-theorem-proved` +
  `edge-interior-invertibility-sharpened`). R-lipschitz-corner upgrades the
  open-marked R-carved-gap24 to settled; R-intruder-4-always upgrades the
  open-marked R-intruder-4/R6 to settled.
- **Failed and kept:** R-single-gap-jump-4 (new counterexample, gaps
  (2,2,6,2,2,...) dies at row 4), R-bounded-gap-4 (Colonna delete-5, Eppstein).
- **Next to attack:** R-primes-events-infinitely-often — the weakest statement
  with the prime gap arrangement switched back on.
- **Difficulty expected to bite:** `regeneration-rate`, in its concrete form
  `intruder-coincidence` at gap-jump sites — an intruder ≥ 6 (injected by a
  gap-jump ≥ 4) forces erosion even at edge 2, and survival is exactly that a
  coincident (edge=2, intruder=4) event heals each injected value before it
  reaches position 0.
