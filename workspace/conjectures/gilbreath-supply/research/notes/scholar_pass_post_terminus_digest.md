# Scholar pass — digesting the post-terminus material (board rows 44–50, grounded approaches)

Author: scholar. Scope: the research agent finished; the task says the library has
new material. Prior passes (`scholar_pass_terminus_audit`, `scholar_pass_terminus_reconciliation`,
`scholar_pass_library_at_terminus_no_new_material`) established that **no new
claim-bearing *source* arrived** — 50 full texts ↔ 50 digests, 51 claim blocks on
disk. This pass verifies that and digests what the audit did not cover: the
**post-terminus work-product** the other schools produced after the audit's last
read.

## What the genuinely new material is

The board has grown from 43 rows (audit's count) to **50**. Rows 44–50 are
post-terminus posts. The new work-product is not sources but **approaches**:
three newly grounded (`meet-join-parseval-self-duality`, `read-cone-column-equivalence`,
`mixing-implies-linear-fold`, plus the re-grounded `squared-excess-higher-order-dyadic-correlations`,
`function-field-fqt-model`, `derivative-ladder-delta-commutation`) and several
newly refuted (`log-chowla-entropy-decrement-switch`, `spacetime-diagonal-furstenberg`,
`vandercorput-differencing-excess`). All 45 approach files carry status; 6 grounded,
39 refuted.

## What each genuinely-new approach establishes

1. **`meet-join-parseval-self-duality` (grounded).** Exact identity: the Walsh
   spectrum of the fold row set EQUALS the excess functional, `Ĉ_n(ω) = S_ω(n)`
   (index bookkeeping, hand-checked n=4). This yields the Parseval identity
   `F_n(z) = 2^{−n} Σ_ω (1−z)^{wt}(1+z)^{n−wt} S_ω(n)²` reproducing the proved
   fair-model binomial at z=0 (Scholze gate: passes). **Refuter correction
   (checked, `parseval-second-moment-not-uniform-in-p`)**: "uniformly in p" is
   FALSE — at p→0, F_n(1−2p)→(n−2)²=Θ(n²) via the kernel input h≡0. The route's
   working instance p≈0.585 is an interior point and survives.
   **Sharp negative**: the pointwise bound extracted from Parseval,
   `S_h² ≤ O(n)·2^{nH(p)}`, is exponentially weaker than trivial — so the
   geometry provably carries NO pointwise force and statement (A) is irreducibly
   arithmetic. This is the cleanest statement yet of why the fold hypothesis dies.

2. **`read-cone-column-equivalence` (grounded).** Exact column bound: coordinate
   j of h is read only through its read-cone `C_j(n)`, `|C_j(n)| ≈ n/2^{popcount(n−1−j)}`,
   so `ν₂(n) ≤ n·Σ_{j∈S}2^{−popcount(n−1−j)}`. The whole converse
   `G-sup-implies-switch` reduces to: for every density-0 support S,
   `inf_n W_S(n) = 0` for `W_S(n)=Σ_{j∈S}2^{−popcount(n−1−j)}`. Sanity: powers of 2
   have `W_S = Ω(1)` at `n=2^m+1` but `W_S(2^m)=o(1)` — exactly the measured
   liminf-0. This is a concrete, checkable target for the SUPPLY⇔switch-density
   equivalence (GOAL priority 3), not a refutation.

3. **`mixing-implies-linear-fold` (grounded).** The transfer theorem attempt:
   from product measures to ψ-mixing measures, `E_μ[S²] = O(n)` given summable
   correlation decay of ε_j=χ₄(q_j)χ₄(q_{j+1}). Correctly priced: interval counts
   are `2^{popcount(d)−ν₂(d+1)}`, exponential — the naive per-pair mixing bound is
   wrong; needs the distance-enumerator popcount split. Live risk named: LOS
   switch bias decays at loglog/log (non-summable), so full ψ-mixing may be too
   strong — the theorem would then need only the second-moment input. **No
   theorem proved; the input hypothesis is the gate and is not established.**

4. **`squared-excess-higher-order-dyadic-correlations` (grounded).** Squared
   run-telescope identity over symmetric differences: `S(n)² = (n−2) + Σ_{d≠d'}
   ∏_R χ(r_{a_R})χ(r_{b_R})`. **Load-bearing theorem (no arithmetic)**: the switch
   density `Σ_j u_j` NEVER appears as a standalone term of S(n)² — every symmetric
   difference has even size, so no singleton; switch signs enter only as factors
   in products (order ≥ 4 in χ, or a single factor at separation ≥ 4). Hand-verified
   n=5 and n=4 examples. The priced question (products of switch signs at the fold's
   separations: strictly weaker than switch density (priority 4) or equivalent
   (priority 5)) is now exactly decidable.

5. **`function-field-fqt-model` (grounded, model-test).** Run the identical fold
   on the gap-parity string of monic irreducibles of F₂[t]. **Grounding correction
   (load-bearing)**: the model does NOT grant the switch-density analogue — Chebotarev
   gives one-point class equidistribution and macroscopic value-domain short
   intervals, NOT the lex-consecutive two-point switch (as delicate as over Z). So
   the model's job is to localize which correlation order Φ needs, not to model the
   switch statistic. First step is one cheap decisive run (n=50..4000, TM control is
   the kill condition).

6. **`derivative-ladder-delta-commutation` (grounded; refuter check
   `derivative-ladder-identities-survive`, checked).** Backbone identities
   (L1) shift, (L4) anti-Pascal, (L5) two-point hold under hostile engine
   verification (find_counterexample: proved on the two cells). The route's open
   cost is the distance-2 two-point correlation — the parity barrier, untouched.

## What the refuted approaches establish (so nobody re-proposes)

- **`log-chowla-entropy-decrement-switch` (refuted):** Tao's log-averaged Chowla/
  Elliott theorems require a bounded MULTIPLICATIVE function at affine-integer
  shifts; the fold's second moment is a bilinear sum over PRIME indices (j↦χ(q_j)
  not multiplicative in j). The index-vs-value obstruction again. Priority 5
  (equivalent to switch-density family) corroborated.
- **`spacetime-diagonal-furstenberg` (refuted):** Furstenberg's diagonal-of-rational
  needs a rational bivariate GF, forcing the boundary eventually periodic —
  contradicting the primes' non-periodicity.
- **`vandercorput-differencing-excess` (refuted):** first-moment identity, dominated
  by squared-excess, no new arithmetic.

## Consistency with the library and prior beliefs

Nothing in the new material contradicts a claim on the claims ledger or the
terminus. All six grounded approaches reproduce established claims (rank n−2,
fair-model binomial, distance enumerator O(n)) — the Scholze gate passes for each
where stated. The single surviving open statement (E[S(n)²]=O(n) for the prime
string) is untouched and re-confirmed: the Parseval sharp negative shows why no
geometry argument reaches it, the mixing route shows what arithmetic input would
(and the risk that even it is too strong), and the read-cone route prices the
converse. **No new belief changes.**

## Wiring state (resolving the prior passes' contradiction)

- **CONTEXT.md is at terminus** (directive 34 head, sixth door, CONCLUSION.md
  named) — the audit's "stale CONTEXT.md" is fixed.
- **ROOT.md still carries no terminus mirror**: grep finds neither
  `goal-hypothesis-refuted-fold-adds-nothing-measurable` nor
  `sixth-door-no-nu2-statistic-prime-specific` — the reconciliation pass's
  "both present in ROOT.md" is not on disk.
- **No board post carries the terminus claim ids or witness numbers** (763/699–996,
  5655/5595–6989) — board rows 44–50 are the other schools' own new posts, not the
  terminus post.
- `code/out/pattern_finder_deliverable_3_fold_genericity.md` still has no fenced
  claim block.
- The two stale CLAIMS.md "contradiction" rows remain self-resolved bookkeeping
  artefacts.

## Sources that do not help (so nobody re-reads them)

All 50 full texts are digested (matching claim-bearing summaries). The 7
`citations_w*` files are lead-only lookup tables; the 4 OEIS rows, the
`mauduit_rivat_gelfond_hal_page` metadata stub, and the two Krawtchouk/MacWilliams
metadata stubs carry no theorems beyond the primary digests. `DELETED_wrong_arxiv.md`
is an overwrite note, not a source. FRONTIER.md's ~40 "DEFINING SUPPLY CHAIN
MANAGEMENT" rows are business-domain contamination — read by subject, not by rank.

## What the run still lacks (unchanged)

1. The **finite-prefix transfer** (ergodic Lucas-mixing ⇒ quantitative wt(Φ_n h)≥c·n
   for the fixed prime string) — in no source.
2. The **unconditional second-moment/submask-Walsh bound** E[S(n)²]=O(n) on the
   prime string — the single surviving route; the Parseval sharp negative and the
   mixing-route pricing both re-confirm it is arithmetic, not geometric.
3. **Wiring**: ROOT.md terminus mirror, board terminus post, deliverable_3 claim
   block — recorded-as-done, not on disk (this pass's grep audit).

```claim
id: post-terminus-digest-state-unchanged
statement: >
  The post-terminus work-product (board rows 44-50; grounded approaches
  meet-join-parseval-self-duality, read-cone-column-equivalence,
  mixing-implies-linear-fold, squared-excess-higher-order-dyadic-correlations,
  function-field-fqt-model, derivative-ladder-delta-commutation; refuted
  log-chowla-entropy-decrement-switch, spacetime-diagonal-furstenberg,
  vandercorput-differencing-excess) establishes no new claim-bearing source and
  no new theorem about wt(Phi_n h) >= c*n for the fixed prime string. The
  Parseval self-duality is exact and reproduces the fair-model law (Scholze gate
  passes) but its sharp negative shows the geometry provably carries no pointwise
  force (S_h^2 <= O(n) 2^{nH(p)} weaker than trivial); the mixing route names the
  arithmetic input that would close statement (A) and the live risk that even it
  is too strong (LOS non-summable); the read-cone route reduces the converse
  G-sup-implies-switch to inf_n W_S(n)=0 for every density-0 support S; the
  function-field model does NOT grant the switch-density analogue (lex-consecutive
  two-point is as open as over Z). Wiring: CONTEXT.md is at terminus (directive 34
  head), but ROOT.md carries no terminus mirror, no board post carries the
  terminus claim ids/witness numbers, and deliverable_3 still has no claim block.
hypotheses: the approach files under research/approaches/, the refuter reports
  under code/out/, the board rows 44-50, CONTEXT.md, ROOT.md, CLAIMS.md as they
  sit on disk this pass.
holds-here: yes (grep-verified: 45 approach files with status, 6 grounded;
  search_claims confirms parseval-second-moment-not-uniform-in-p and
  derivative-ladder-identities-survive reach the ledger; ROOT.md grep finds no
  terminus ids).
status: checked
bearing: >
  Nobody should re-fetch Chebotarev, Chowla/entropy-decrement, Furstenberg
  diagonal, or van der Corput material expecting a way past the parity barrier:
  all three new refutations are the same index-vs-value obstruction, and the two
  new grounded routes (read-cone, mixing) each reduce to an explicitly named,
  checkable arithmetic statement. The next loop should attack one of those named
  objects, not the library.
anchor: research/approaches/meet-join-parseval-self-duality.md;
  research/approaches/read-cone-column-equivalence.md;
  research/approaches/mixing-implies-linear-fold.md;
  research/approaches/squared-excess-higher-order-dyadic-correlations.md;
  research/approaches/function-field-fqt-model.md;
  code/out/refuter_parseval_uniform_p.md; code/out/refuter_derivative_ladder_check.md;
  research/CONCLUSION.md; teams/board.jsonl rows 44-50; research/ROOT.md (grep: no terminus mirror).
contradicts: research/notes/scholar_pass_terminus_reconciliation.md (which claims
  both terminus claims are "mirrored in research/ROOT.md"; grep shows they are not)
answers: none — walsh-spectral-subset-b904 stays open (superseded by CONCLUSION.md §5)
```
