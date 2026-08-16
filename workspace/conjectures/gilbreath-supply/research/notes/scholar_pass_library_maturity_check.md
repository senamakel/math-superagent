# Scholar pass: the (mature) reference library, the ladder contradiction, and the stale sign factor

Author: scholar. Date: this pass. Scope: re-read `research/` against GOAL
(can the fold `Φ` do work the switch-density form cannot see), TASKS, current
beliefs (ROOT/CLAIMS/threads), and the recalled durable findings.

## Verdict on the "new material"

The library is **mature and fully digested.** Every one of the 43 full texts
under `research/sources/` has a matching claim-bearing digest under
`research/summaries/` (5 of them explicitly marked not-to-help: the four OEIS
rows and `odlyzko_gilbreath`; the five `citations_w*` files are citation
graphs, "not evidence"). Six prior scholar passes have each verified the same
conclusion. **What is genuinely new in this pass is not a source but two
on-disk contradictions between existing claims plus one stale formula**, and
one open bookkeeping request the refuter left.

## 1. R-random-pointwise: the ladder and a note disagree (live contradiction)

- `research/weakened/supply.md` (and the derived `research/WEAKENED.md`; and
  ROOT's "settled restricted classes" list) still call `R-random-pointwise`
  **the current open rung** — with the merge note "concentration does not
  follow from uniform on a rank-(n−2) subspace alone… must use Φ_n-specific
  structure (Lucas), not the bare rank".
- `research/notes/refute_random_pointwise_closed.md` claims
  `r-random-pointwise-closed-by-exact-binomial` (currently registered in the
  claim ledger): with rank Φ_n = n−2 (proved), Φ_n is **surjective onto
  F₂^{n−2}**, so Mh is uniform on the whole cube, `wt(Φ_n h) ~ Binomial(n−2,1/2)`
  exactly, and Chernoff gives P(wt < n/4) ≤ exp(−Ω(n)) — the rung closed by the
  run's own proved claims, "without new work". The merge caveat's counterexample
  (a rank-2 image subspace) is a map F₂² → F₂ⁿ, the **opposite direction** to
  Φ_n's surjective F₂ⁿ → F₂^{n−2}; equal-size fibers make the image uniform on
  the cube, so the caveat does not obstruct this fold.
- `research/notes/refute_random_pointwise_small_n.md` (preserved from the
  deleted refute-spray) says the literal exp(−Ω(n)) form **fails at n=4,5**
  (constants 1/4, >1/8) and "whether the asymptotic concentration holds is
  genuinely open and needs Lucas structure, not bare rank".

**Resolution:** the small-n constants are the binomial lower tail and decay
exponentially (the "closed" note shows the model explicitly); the asymptotic
form is a theorem by Chernoff on the proved exact binomial — surjectivity in the
(n−2)-image direction is sufficient, Lucas is not needed. `WEAKENED.md`'s
"open" marker and its merge caveat are stale. The rung's only content is the
asymptotic form, and that form is proved. (Two independent checks: the full
weight fibre census n=2..9, and the model-finder confirming a small-n
falsifying assignment that is harmless.)

## 2. Stale sign factor in a live backward skeleton (documented defect)

`research/backward/supply-from-endpoint-parity.md` line 113 (inside the
G-endpoint-comparison-density gap block) still carries

    (−1)^{T(n,d)} = (−1)^{#runs(d)} · ∏_R χ(r_{a_R}) χ(r_{b_R})

with the spurious `(−1)^{#runs(d)}` prefactor. The refuter
(`research/notes/refuter_endpoint_sign.md`, verified by hand at d=3 and on all
6868 (n,d) pairs n=20..120, spurious form failing 449) proved the correct
identity is

    (−1)^{T(n,d)} = ∏_R χ(r_{a_R}) χ(r_{b_R})

— each run telescopes independently, XOR carries signs multiplicatively, and
`(−1)^{[x≠y]} = χ(x)χ(y)`. The `(−1)^{#runs}` version is false for every binary
string at odd d. Nothing downstream leans on the prefactor (the density #{T=1}
is unaffected), but the live skeleton should be corrected so a reader does not
recompute the wrong product. The refuter explicitly asks for this update.

## 3. Refuter request still open (bookkeeping)

`research/notes/refuter_endpoint_sign.md` also asks to merge the closed
`R-random-pointwise` rung (item 1) so it stops being re-attacked as open.

## What the library does NOT contain (unchanged, restated precisely)

- **Finite-prefix transfer** (thread `finite-prefix-transfer`): Pivato–Yassawi
  2006 Thm 7.1 is an ergodic iff-statement at density-one *times*; no source
  gives the quantitative `wt(Φ_n h) ≥ c·n` for the one fixed prime string. Both
  halves — (a) is the prime-gap measure Lucas mixing, (b) quantitative weak-* →
  weight — absent. This is the single largest missing technical tool.
- **Walsh/subset-sum lower bound on `wt(Mx)` for the submask-XOR map M**,
  independent of h-complexity (request `walsh-spectral-subset-b904`): the
  Meshulam/Tao/Donoho–Stark bounds fix the Walsh-side *support* trade-offs and
  their extremals (subgroup indicators = exactly the five-closed-doors low-weight
  inputs); they are not image-weight bounds. Request stays genuinely open — the
  Pivato note's earlier `answers:` line was retracted by a prior pass.
- **`s2_N → 0` for the prime h** from an arithmetic input (the sharpest open
  problem, density-1 form via Chebyshev): measured (`s2_N` 0.000783@4000 →
  0.0000934@40000; Ratio B 1.3155@40000; primes/fair 1.329@40000) but unproved;
  in-house computation, not literature.

## What this pass adds to durable knowledge

1. The `R-random-pointwise` rung is provably closed (surjectivity ⇒ uniform
   image ⇒ Binomial ⇒ Chernoff), so `WEAKENED.md`'s open marker and its
   Lucas-merit caveat are stale; the next attack should start at
   `R-submask-sufficiency`, not re-open this rung.
2. The spurious `(−1)^{#runs(d)}` prefactor must be removed from
   `research/backward/supply-from-endpoint-parity.md` (refuter-verified defect).
3. No new source, claim, or theorem entered the library this pass; the two open
   requests and the central gap are unchanged and still constitute the whole of
   what the run lacks.

## Sources that do NOT help this pass (so nobody re-reads them)

- The five `citations_w*` files — citation-graph lookup tables, explicitly "not
  evidence"; their cited sources that bear are already digested.
- `odlyzko_gilbreath` — bibliography index page; canonical Odlyzko 1993 is held.
- `granville_martin_prime_number_races` / `_prime_races` — two mirrors of one
  paper; single-residue race context only (already `gm-chebyshev-bias-positive-density`).
- The four OEIS rows — base-4 digits / fractal ternary sequences; nothing to do
  with the fold.

## Contradictions with recalled memory

None new. The two `CLAIMS.md` "contradictions" rows (`r-finite-verified` vs the
rung name; `rw-described-as-the-fold-itself` vs the correction) are stale-id
artefacts, already self-resolved by prior verification passes and flagged as
such there. The live content-level contradiction this pass found is the one in
item 1 (ladder vs proof note), which is a bookkeeping staleness, not a factual
dispute between two theorems that both hold.