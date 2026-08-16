# Scholar synthesis — what the library establishes about SUPPLY

A digest pass over the reference library, its goal being to turn the sources
into knowledge the run can act on. Every source was read against the central
hypothesis under test (GOAL.md): *can the fold `Φ` do work the switch-density
form cannot see, i.e. is `wt(Φ_n h) ≥ c·n` forced by an input strictly weaker
than positive mod-4 switch density?* Nothing here settles that question; it
remains open. What the library does settle is *why* the standard routes are
closed and *which structure is left available.

## What the library establishes, claim by claim

All claim blocks live in the notes under `research/summaries/` and are
re-derived into `research/CLAIMS.md`. The durable versions are in Cognee.

**The parity barrier (why the reduction is a dead end).** ABGS 2011 §1 p.401
and §9: the asymptotic frequency of consecutive-prime pairs in an ordered
residue class mod m is wide open and *cannot be treated using L-functions*.
Lau 2024 sharpens this: even a single non-constant 2-term pattern (1,3) or
(3,1) mod 4 is not known to occur infinitely often. The unconditional
literature (Shiu, Freiberg, Maynard, BFTB, Shiu again) bounds the *equal*-
residue side — the wrong direction for switch density. So the reduction of
SUPPLY to positive switch density lands on an L-function-inaccessible open
problem. This is the entire justification for attacking the fold directly.

**The five closed doors (why "h is complicated" cannot work).** `Φ` has
low-weight images on structurally rich inputs. Rampersad–Wiebe supply the
language: the submask-XOR objects `Φ` reads are 2-regular-expressible, and
2-regular sequences cannot grow linearly. The dyadic collapse and the
anti-dyadicity bounded-wt counterexample are both 2-regular phenomena. So any
route must use `Φ`'s structure (Lucas submask-XOR, kernel, self-similar block
structure) rather than `h`'s complexity.

**The structure left to exploit.** `Φ_n` is the Pascal-mod-2 fold, entries
`C(k−1, j−(n−k)) mod 2`; by Lucas each depth-d cell is the XOR of the input
over binary submasks of d. The operative Φ_n has rank n−2, nullity 2,
ker = span(even-alt, odd-alt) — corrected from the inherited
"rank n−3, nullity 1, ker = span(all-ones)" (see
fold-rank-is-n-2-nullity-2-alternating); all-ones = their sum lies in the kernel.
Bacher supplies the linear-algebra/self-similar "recurrence-matrix" structure
of Pascal-mod-2 matrices — with the caveat that his determinant theorems are
for the *symmetric* Pascal matrix, not the rectangular offset `Φ_n`, so
transfer is unchecked and must be verified by direct computation. Szechtman
restates Lucas/Kummer with the power-of-two cancellations that underlie the
dyadic collapse.

**Generic expectation is no obstruction.** For uniform h and linear M,
E[wt(Mh)] = (# nonzero rows)/2 ≥ rank/2 = (n−2)/2 ≥ n/3 for n ≥ 6 (corrected
rank). So the fold imposes no weight obstruction on generic input; the
difficulty is entirely the specific prime string h. But this is expectation
only, no concentration — pointwise work needs Lucas structure.

**Measured data (don't build theorems on it).** ABGS mod-4 (x=10^3..10^6):
switch pairs 45041 (57.5%) vs equal 33289 (42.5%), ratio 1.35 — the diagonal
bias, consistent with LOS. Odlyzko: the triangle reduces to {0,2} very fast
(g≈22 at 10^8 … 33 at 10^12); deep cells ≥ 4 are rare and prime-gap-driven,
so long {0,2} suffixes (large ν₂) break where large gaps are. LOS conjecture
mod-4 switch pairs strictly exceed equal pairs at every x, with a slowly
decaying secondary term — the strongest *heuristic* support for the switch-
density input, but conjecture only.

## What the library does NOT settle (gaps)

- Whether SUPPLY is equivalent to positive switch density (GOAL priority 3) —
  a genuine negative theorem that would close the problem. No source states this.
- Any Walsh-spectral / subset-sum lower bound on `wt(Φ x)` using `Φ`'s
  submask structure rather than `h`'s complexity — the open request
  `walsh-spectral-subset-b904`.
- The averaged / density-1 form (GOAL priority 1), which sieve methods might
  reach even where the pointwise form is blind.
- The weakest arithmetic input on h that forces `wt(Φ_n h) ≥ c·n` (GOAL
  priority 2).

## Contradictions / flags

1. **ABGS vs LOS emphasis (not factual).** ABGS treat even the *frequency
   limit* of switch pairs as unknown; LOS conjecture switch pairs *strictly
   dominate* at every x. Both can be true; neither is a theorem. Do not cite
   LOS as evidence SUPPLY's arithmetic input is proved.
2. **Bacher holds-here is unchecked.** The determinant/LU theorems are for the
   symmetric Pascal matrix; `Φ_n` is the rectangular offset matrix. The
   corroboration of rank n−3 and self-similarity is *in spirit only* until a
   direct computation on `Φ_n` confirms it. A claim built on Bacher's exact
   formula for `Φ_n` would be wrong.
3. **A stale/garbled ledger row.** An earlier version of `abgs-mod4-...` was
   recorded with garbled numbers ("16574/16715 range"); the canonical note and
   the on-disk CLAIMS.md carry the corrected split (45041/33289). The
   verification script reproduces the corrected counts.
4. **problem.md fact (3) contains an internal convention tension.** "rank
   Φ_n = n−3, nullity 1, ker = span(all-ones)" with domain F₂^d forces d = n−2
   (rank+nullity = d). The expectation bound uses only rank, so it is safe, but
   any rung needing the domain dimension must fix it (problem.md convention).

## What to do next

Read `research/FRONTIER.md` and `research/REQUESTS.md` (request
`walsh-spectral-subset-b904`). The sharpest open target per GOAL priorities:
(1) the density-1/averaged form first, (2) then the weakest-input question,
(3) then the equivalence. Bacher's self-similar block structure and Szechtman's
cancellations are the raw material for a structure-of-`Φ` bound; a direct check
of whether Bacher's LU/determinant structure transfers to the rectangular
`Φ_n` should be the first computation, since it governs whether the fold-side
route is even available.
