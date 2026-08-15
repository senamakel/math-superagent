# Weakened ladder: the gap-jump axis (corner vs injected defects)

This ladder decomposes Gilbreath's conjecture along the *gap-sequence Lipschitz*
axis, which the canonical ladder (`recharge-ladder.md`) names only obliquely as
`unbounded-gap-arrangement`. The sharp observation: the corner — the absorbing
state that settles the conjecture — is reached at row 2 whenever the gaps are
1-Lipschitz. So the *entire* difficulty is the gap-jumps of size ≥ 4 and whether
the value ≥ 4 they inject into row 2 is healed before it reaches the left edge.

Status corrections this file makes to the existing ledgers:

- `R-carved-gap24` (recharge-ladder, marked open) is **settled**: it is the
  `gaps ⊆ {2,4}`, `g_1 = 2` special case of `R-lipschitz-corner` below, and the
  proof is one line (the library already has the `{2,4}` case as the *proved*
  claim `sweep-corner-mechanism`). The 1-Lipschitz generalisation is the same
  one line, stated inline.
- `R-intruder-4` / `R6-intruder-4-regeneration` (marked open) is **not** settled
  by the naive step-law + edge-invertibility assembly: that assembly silently
  assumes the block is nonzero, and the all-zero block `(1,0,...,0)` shows edge 0
  for its whole life, so an intruder-4 kills it without any (2,4)-event. A
  backward-induction argument (stated in full in the rung's `merge`) appears to
  close the hole — it shows the all-zero block with intruder 4 is unreachable,
  the v=2 branch forcing an intruder 6 and the v=0 branch extending the zero block
  back to row 1 contradicting g_1 = 2. That argument is a **hand derivation, not
  yet oracle-checked**, so the rung stays `open` until the forward loop confirms
  both branches — one short attempt.

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
- `gap-lipschitz` — adjacent input gaps may differ by ≥ 4 (a "jump", e.g. the
  prime gaps have `...,6,2,...`, `|6−2| = 4`). A jump of 4 injects a 4 into row 2
  (`|2−6| = 4`); a jump of ≥ 6 injects ≥ 6. Row 2 is the all-{0,2} corner *iff*
  the gaps are 1-Lipschitz (see R-lipschitz-corner). This is the concrete,
  checkable form of `unbounded-gap-arrangement`: it is the jumps, not the
  magnitude, that hurt.
- `intruder-coincidence` — a (2,4)-event needs edge = 2 **and** intruder = 4 in
  the *same* row. Edge-invertibility forces edge = 2 at least once per (nonzero)
  block lifetime, but the intruder value at those rows is uncontrolled; an
  intruder ≥ 6 at an edge-2 row forces erosion (`|2−6| = 4`).
- `non-concentration` — the deterministic prime gap sequence carries no
  independence / frequency hypothesis; every proved "events recur" theorem is a
  random analogue (Chase 2024, CHT 2026) whose hypotheses are unchecked for the
  primes.

---

```rung
id: R-parity-reduction
statement: For ANY sequence beginning (2, 3, odd, odd, ...) — equivalently any A_1 = (1, even, even, ...) — every row A_k has shape (odd, even, even, ...): A_k(0) is odd for all k, and A_{k+1}(0) = 1 ⟺ A_k(1) ∈ {0,2}. The settled half is the parity statement; the ⟺ is the bridge to the exact target. Claim `gilbreath-reduces-to-second-in-02` (proved, Lean-formalised).
off: regeneration-rate, gap-lipschitz, intruder-coincidence, non-concentration
stance: settled
merge: Restore magnitude content — distinguish {0,2} from {4,6,...}. First move: prove a difference of two {0,2} entries is in {0,2}, and that a row (1,c,c,c,...) with c ∈ {0,2} is a fixed shape (next rung).
```

```rung
id: R-corner-closure
statement: If some row equals (1, c, c, c, ...) with every c ∈ {0,2} (the "corner"), then every later row begins with 1. The corner is a fixed shape: |1−c| = 1 for c ∈ {0,2}, and a difference of two {0,2} entries is in {0,2}. Claim `closure-0d-double-edge` (proved).
off: regeneration-rate, gap-lipschitz, intruder-coincidence, non-concentration
stance: settled
merge: The corner is the absorbing state; reaching it settles everything. Restore the question of *reaching* it: which input gap sequences already put row 2 in the corner? Next rung answers exactly that.
```

```rung
id: R-lipschitz-corner
statement: For a 2-then-odds sequence with first even gap g_1 = 2 and |g_i − g_{i+1}| ≤ 2 for all i ≥ 1 (the gap sequence is 1-Lipschitz), A_2 is the all-{0,2} corner, hence A_k(0) = 1 for every k ≥ 1. Proof (one line): |g_1 − g_2| ≤ 2 with g_2 even and positive forces g_2 ∈ {2,4}, so A_2(1) = |2 − g_2| ∈ {0,2}; and for i ≥ 2, A_2(i) = |g_i − g_{i+1}| is an even difference of magnitude ≤ 2, so ∈ {0,2}. Row 2 is the corner; R-corner-closure finishes. Strictly generalises the consecutive-odds case (all gaps 2) and R-carved-gap24 (gaps ⊆ {2,4}); also admits slow chains like (2,4,6,4,2,...), where |4−6| = 2 is harmless. The {2,4} special case is the run's proved claim `sweep-corner-mechanism`.
off: gap-lipschitz, regeneration-rate, intruder-coincidence, non-concentration
stance: settled
merge: Turn `gap-lipschitz` back on minimally — allow one adjacent jump of size 4 (a single 6 in a {2,4} background). That is R-single-gap-jump-4, and it fails: even *one* jump injects a 4 that propagates to the left edge. The first move up that survives is therefore not a wider gap class but a constraint on the *effect* of jumps — that is R-intruder-4-always, which pins the intruder instead of the gaps.
```

```rung
id: R-intruder-4-always
statement: For a 2-then-odds triangle with g_1 = 2, if the block-boundary intruder value is 4 at every row where the leading block is nonempty and finite (y_k = A_k(b_k+1) = 4), then A_k(0) = 1 for all k — the leading block never dies.
off: intruder-coincidence, non-concentration
stance: open
merge: This is the rung to attack next, and a complete candidate proof exists (hand argument, NOT yet checked against the run's oracle — do not mark settled until a program confirms both branches). Assembly: (step law) growth ⟺ (edge,intruder)=(2,4); (edge-invertibility) a nonzero block shows edge 2 at least once per lifetime. So the block survives iff it is never ALL-zero. The candidate proof shows all-zero is unreachable: if A_k = (1, 0^n, 4, ...), then A_{k−1}(1..n+1) are all equal to v, and |1−v| = 1 forces v ∈ {0,2}. Branch v=2: A_{k−1} = (1, 2^{n+1}, 6, ...), full block length n+1, intruder 6 — violates the intruder≡4 hypothesis, eliminated. Branch v=0: A_{k−1} = (1, 0^{n+1}, 4, ...) — the zero block extends backward one position per row. Inducting to row 1 forces A_1(1) = 0, contradicting g_1 = 2. First move: check this backward induction against the oracle by exhaustive search over small even-gap inputs for any row of shape (1, 0^n, 4, ...) with all prior intruders 4 — UNSAT confirms the lemma and settles the rung; a found row refutes it and the all-zero block is the obstruction. Verify the v=2 branch carefully: it is the only place the hypothesis is used.
```

```rung
id: R-single-gap-jump-4
statement: For a 2-then-odds sequence with g_1 = 2, gaps in {2,4} except a single 6, the leading 1 persists forever.
off: non-concentration
stance: failed
killed-by: gaps (2,2,6,2,2,2,...) — A_0=(2,3,5,7,13,15,17,19,...), A_1=(1,2,2,6,2,2,2,...), A_2=(1,0,4,4,0,0,...), A_3=(1,4,0,4,0,...), A_4=(3,4,4,4,...). A_4(0) = 3: dead at row 4. (All four rows written out for transparency; hand-computed here — the forward loop should confirm against the oracle's `rows()` before this is cited as checked.)
reason: The 2→6 jump injects a 4 into row 2 (|2−6| = 4). In a {0,2} background the 4 propagates one position left per row (|0−4| = 4) until it becomes the second entry (row 3) and then the leading entry (|1−4| = 3, row 4). It is healed iff a 2 sits immediately to its left (|2−4| = 2); here the left neighbour is 0, so it is not healed. Sharper than Colonna's delete-5 (whose killer is g_1 = 4, not a jump): this fixes g_1 = 2 and still dies.
merge: Even a single non-Lipschitz jump kills unless the injected 4 meets a 2 to its left in time. Survival is exactly the statement that the {0,2} interior always supplies that 2 — the coincidence difficulty. The next surviving rung is not a wider gap class (R-bounded-gap-4 fails) but a frequency/arrangement condition; that is the open core.
```

```rung
id: R-bounded-gap-4
statement: For every 2-then-odds sequence with all gaps (after the first) ≤ 4, the leading 1 persists forever — the deterministic bounded-gap class at g = 4.
off: gap-lipschitz
stance: failed
killed-by: Colonna's delete-5 example (2,3,7,11,13,17,...): gaps (4,4,2,4,2) all ≤ 4, but g_1 = 4, so A_1 = (1,4,...) has A_1(1) = 4 ∉ {0,2} and A_2(0) = |1−4| = 3 — dead at row 2. Eppstein's anti-Gilbreath construction kills every fixed g ≥ 4.
reason: The class does not force g_1 = 2, and g_1 = 4 alone kills at row 2. Note the contrast with R-lipschitz-corner: all gaps ≤ 4 *is* 1-Lipschitz (adjacent diffs ≤ 2), so the only thing missing is g_1 = 2 — and that single missing constraint is the whole difference between settled (R-carved-gap24) and dead. Eppstein 2011 kills every fixed g.
merge: No bounded-gap class survives without g_1 = 2, and even with g_1 = 2 any jump ≥ 4 kills (R-single-gap-jump-4). The surviving route is a *frequency* restriction tolerating rare large jumps — the deterministic seed of a non-concentration condition; see next rung.
```

```rung
id: R-primes-events-infinitely-often
statement: For the prime triangle, (2,4)-regeneration events occur infinitely often as k → ∞. Strictly weaker than the goal (occurrence, not rate), and the natural first target with the prime gap arrangement switched back on. In the gap-jump framing: infinitely many of the values ≥ 4 injected by gap-jumps of size ≥ 4 are healed back into {0,2} by a coincident (edge=2, intruder=4) event before they reach position 0.
off: regeneration-rate
stance: open
merge: Infinitely-often is necessary but not sufficient: the recharge surplus Σ(j_i+1) must never fall k−2 behind, so a *rate* statement is required. First move: mark the gap-jump sites of the prime gap sequence (where |g_i − g_{i+1}| ≥ 4) against the (2,4)-event rows of the depth-1000 data and measure whether each injected defect is healed within a bounded number of rows — that bound is the seed of a rate.
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

- **Settled (bottom three rungs):** R-parity-reduction (`gilbreath-reduces-to-second-in-02`),
  R-corner-closure (`closure-0d-double-edge`), R-lipschitz-corner (the `{2,4}` case is
  the proved `sweep-corner-mechanism`; the 1-Lipschitz extension is the same one line,
  stated inline). R-lipschitz-corner upgrades the open-marked R-carved-gap24 to settled.
- **Open, one check from settled:** R-intruder-4-always — a complete candidate proof is
  stated in its `merge` (backward induction shows the all-zero block `(1,0^n,4,...)` is
  unreachable: the v=2 branch forces an intruder 6, the v=0 branch extends the zero block
  back to row 1 contradicting g_1 = 2). The argument is a hand derivation; the forward loop
  must confirm both branches against the oracle (exhaustive small even-gap search, UNSAT =
  settled, a found row = refuted) before it is marked settled. This is the next rung to
  attack, and it is a one-attempt job.
- **Failed and kept:** R-single-gap-jump-4 (new counterexample: gaps (2,2,6,2,2,...)
  dies at row 4 — hand-computed, confirm against oracle), R-bounded-gap-4 (Colonna
  delete-5 via g_1 = 4; Eppstein for every g).
- **Next to attack:** R-intruder-4-always (settle or refute the all-zero-block
  reachability lemma), then R-primes-events-infinitely-often.
- **Difficulty expected to bite:** `intruder-coincidence` at gap-jump sites — an
  intruder ≥ 6 (injected by a gap-jump ≥ 4) forces erosion even at edge 2, and survival
  is exactly that a coincident (edge=2, intruder=4) event heals each injected value
  before it reaches position 0. `gap-lipschitz` is its input-side form: the primes fail
  1-Lipschitz exactly at jumps like `...,6,2,...`.
