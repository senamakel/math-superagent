# Claim: g-degenerate-slow-divergence

**Node:** `h16-2-degenerate-graphics-finite-cyclicity/G-degenerate-slow-divergence`
(from `research/backward/h16-2-degenerate-graphics-finite-cyclicity.md`).

**Status: formalised** (lean_check verdict: verified, no sorries, axioms
exactly `[propext, Classical.choice, Quot.sound]`).
**Formalisation:** `code/lean/h16_2_degenerate_graphics_finite_cyclicity_G_degenerate_slow_divergence-451220d2.lean`

## Statement (as formalised)

Let `Parameter` (the normal-form/blow-up parameter space) and `Chart` (the
desingularized section coordinate) be given, with `D : Set Chart` the chart
domain.  For a displacement map `displacement : Parameter → Chart → ℝ`, a
candidate slow-divergence integral `slowDivergence : Parameter → Chart → ℝ`,
and two strata `genericStratum centerStratum : Set Parameter`, the data
`SlowDivergenceData D displacement slowDivergence genericStratum centerStratum`
consists of:

- `bound : ℕ` together with, for every `p ∈ genericStratum`, finiteness of
  `ZeroSet D (displacement p)` and `ncard ≤ bound`;
- for every `p ∈ centerStratum`, `slowDivergence p` is identically zero on
  `Chart`;
- a two-stratum cover `genericStratum ∪ centerStratum = univ`.

From that data the file proves (kernel-verified):

1. `generic_slow_divergence_zero_bound` — the generic-stratum uniform bound:
   `∃ B, ∀ p ∈ genericStratum, (ZeroSet D (displacement p)).Finite ∧
   ncard (ZeroSet D (displacement p)) ≤ B`, with `B := bound`;
2. `center_stratum_sdi_identically_zero` — the vanishing-stratum audit:
   `∀ p ∈ centerStratum, ∀ x, slowDivergence p x = 0`.

## Binder correspondence (which original hypothesis each binder carries)

| Original node content | Binder in the formalisation | Status |
| --- | --- | --- |
| "On the desingularized charts of the family blow-up at the contact point" | `Chart`, `D : Set Chart` (the section coordinate and its domain) | data (no assertion) |
| "the displacement map's derivative is C^∞ contact-equivalent to a development whose leading term is the SDI" | NOT formalised here — this analytic theorem is the node's open hypothesis; in this file its zero-count consequence is carried by `SlowDivergenceData.hgeneric` | **hypothesis** — no claim of the run or the literature establishes it for the DI₂a family (2.8); the DR 2009 method statement (CPAA 8 (2009) p. 2) describes the technique for DF1a/DF2a, not a theorem for DI₂a |
| "wherever that integral is not identically zero, the displacement has at most B zeros with B read off the SDI" | `bound : ℕ` + `hgeneric` (the ≤ bound on the generic stratum, per-parameter) | **hypothesis** — the actual computation of the DI₂a SDI and its zero count is the work the gap demands; not supplied by any held source |
| "≤3 cycles for DF1a generic, ≤5 for the DF2a center case, ≤1 under sign conditions" | not binders — illustrative DR 2009 Theorem 3.1 numbers for the *other* graphics; nothing here claims them for DI₂a | excluded deliberately |
| "the strata where it vanishes identically are identified — that list is exactly the input to G-degenerate-pstar-and-center" | `centerStratum` + `hcenter` (identically zero there) + `hpartition` (cover); theorem 2 states the audit | **hypothesis** (the identification itself) + formalised consequence |
| "the SDI ... is computed explicitly" | `slowDivergence` is an explicit function argument; no particular formula is asserted | data (no assertion) |

So the only *mathematical* content the kernel checks is: given the generic
stratum bound, the displacement zero count is bounded there (trivially — `B :=
bound`), and given the identically-zero identification, the SDI vanishes on the
center stratum.  The implication is exactly the recombination the node's `next`
consumes; the SDI computation, the contact-equivalence, and the zero-count
theorem remain open hypotheses, honestly binder-carried rather than asserted.

## What this claim does NOT establish

- No bound for the DI₂a graphic: there is no `Parameter`, `D`, `displacement`,
  `slowDivergence`, or `bound` supplied with `SlowDivergenceData`.
- No C^∞ contact-equivalence theorem, no SDI computation, no vanishing-strata
  identification — those are the hypotheses (`hgeneric`, `hcenter`,
  `hpartition`), and the file proves no instance of them.
- Nothing about the residual non-desingularizable P\* stratum or the
  identically-zero-SDI center closure (the separate node
  `G-degenerate-pstar-and-center`, which consumes `centerStratum` as input).

## Downstream

`G-degenerate-pstar-and-center` (`h16_2_degenerate_graphics_finite_cyclicity_G_degenerate_pstar_and_center-83c75492.lean`,
already kernel-verified) consumes exactly the `centerStratum`/`hcenter`
identification as its input; the two files combine to a two-stratum cover
bound (generic bound from this file, residual bounds from the P\*/center
node).

## Falsifiers

- An explicit DI₂a parameter point in the (2.8) family at which the SDI is
  computed and shown to have more zeros than the bound carried by `hgeneric` —
  but no such `bound` is instantiated here, so the honest failure mode is
  simply that nobody can supply `SlowDivergenceData` for DI₂a; that is exactly
  the known open gap (DR 2009 p. 2: method described for DF1a/DF2a; ADL 2009
  partial results only).
