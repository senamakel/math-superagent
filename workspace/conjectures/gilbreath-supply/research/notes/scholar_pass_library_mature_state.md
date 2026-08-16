# Scholar pass — library maturity verification, no new undigested sources

Author: scholar. This pass's mandate: read what is now in `research/`, record each
new source's actual statements against SUPPLY, store durable findings, and flag
contradictions with recalled memory.

## Headline finding: the library is mature; there is no undigested new source

The research agent's latest activity added **no new full text** to `research/sources/`.
Every one of the full texts on disk has a matching, claim-bearing digest under
`research/summaries/` (verified by cross-checking the two listings and by
`grep '^id:'` — 51 claim blocks across 40 digest files, plus work-product claim
blocks under `code/out/` and `research/notes/`). The two QA-download stubs
(`ashikhmin_barg_litsyn_polynomial_method`, `friedlander_macwilliams_krawtchouk`)
are correctly quarantined as "metadata stub, not a full text" — they carry no
downloadable content and their advertised theorems are held, better, by
`macwilliams_1963` and `guruswami_macwilliams_lp_notes`. The wrong-download
placeholder `matomaki_radziwill_tao_averaged_chowla` is correctly quarantined
and its real target is `..._fourier_uniformity_averaged` (digested). So the only
new work this pass could add is verification and correction, which it did.

## What the library establishes, restated against SUPPLY

The single hypothesis under test (GOAL): can the fold `Φ` be made to do work the
switch-density form cannot see? The library's answer, source by source:

- **The parity barrier (why the switch-density reduction is a dead end) — proved
  sourced facts.** ABGS 2011 §1/§9: the consecutive-pair residue frequency problem
  is "wide open and cannot be treated using L-functions" (verbatim, §1 p.401; §9
  leaves even the frequency-limit open). Lau 2024: even a single non-constant
  2-term pattern mod 4 is not known to occur infinitely often. These are the
  arithmetic inputs the reduction would need, and both are beyond reach.
- **The equal-residue side is fully understood and is the wrong direction.** Shiu
  2000 (arbitrarily long all-0 runs in `h`, refutes door 3), Maynard 2016 Thm 3.3
  (positive density), Freiberg, BFTB (bounded gaps). None touches the switch side.
- **The fold's structure is settled and proved (computed+checked, the strongest
  evidence class).** Rank `Φ_n = n−2`, nullity 2, `ker = span(even-alt, odd-alt)`
  (corrected from the inherited "rank n−3, nullity 1"; supersedes problem.md fact 3).
  Surjectivity onto F₂^{n−2} makes `wt(Φ_n h)` exactly `Binomial(n−2,1/2)` for
  uniform h (Chernoff ⇒ SUPPLY w.h.p. for random h; the difficulty is entirely the
  fixed prime string). Lucas: the depth-d cell is an XOR over the `2^{s₂(d)}`
  binary submasks of d.
- **The weak-input candidate and its hard limit.** Pivato–Yassawi 2006 Thm 7.1:
  `Φ=1+σ` asymptotically randomizes µ iff µ is Lucas mixing — the *sharp*,
  *weakest* ergodic condition, reading exactly the submask sets Lucas makes Φ read.
  **But it does not close the run's request**: it is a measure-level equivalence at
  density-one *times*, and the step to `wt(Φ_n h) ≥ c·n` for the one fixed string
  (the finite-prefix transfer, halves (a) prime-gap measure Lucas mixing and (b)
  quantitative weak-*→weight) is absent and is the single largest missing tool.
- **The Walsh side is not the engine.** Meshulam/Tao/Donoho–Stark fix sharp
  Walsh-support trade-offs; their equality cases (subgroup indicators) are exactly
  the five-closed-doors low-weight inputs, so they constrain supports, not
  co-domain weight.

## Sources that do not help (so nobody re-reads them)

- The five `citations_w*` files — citation-graph lookup tables, explicitly "not
  evidence"; their cited sources that bear are already digested.
- `odlyzko_gilbreath` — a bibliography index page (leads, not evidence); canonical
  Odlyzko 1993 is digested.
- `granville_martin_prime_number_races` / `_prime_races` — two mirrors of one paper;
  single-residue race context only.
- The four OEIS rows — base-4 digits / fractal ternary sequences; nothing to do with
  the fold.
- `ashikhmin_barg_litsyn_polynomial_method`, `friedlander_macwilliams_krawtchouk` —
  metadata stubs (no full text on disk); their content is covered by the primary
  MacWilliams/Guruswami tier.

## Contradictions with recalled memory

None new at the level of two theorems that both hold. Two live items:

1. **Request overreach retracted (correct).** `pivato_lucas_mixing_equivalence.md`
   once carried `answers: walsh-spectral-subset-b904`; that line is retracted
   (verified in the claim ledger) because Thm 7.1 is ergodic, not a finite bound.
   The request `walsh-spectral-subset-b904` stays **open**.
2. **Root ladder staleness (bookkeeping).** `weakened/supply.md` / `WEAKENED.md`
   still list `R-random-pointwise` open, contradicting the proof that surjectivity
   (n−2) ⇒ uniform image ⇒ exact Binomial ⇒ Chernoff closes it. Bookkeeping only,
   the asymptotic form is proved; the next attack should start at `R-submask-sufficiency`,
   not re-open this rung.

## What the run still lacks (unchanged, precisely)

1. **The finite-prefix transfer** — ergodic Lucas/harmonic randomization ⇒
   `wt(Φ_n h) ≥ c·n` for the fixed prime string. The single largest missing
   technical tool; in no source.
2. **An arithmetic input that suffices** — specifically `E[S(n)²] = O(n)` for the
   real prime `h` (GOAL priority 2), strictly weaker than positive mod-4 switch
   density. This is the one open step between the settled geometry side (condition C,
   `F_n(1−2p)=O(n)`, `A_2=O(n^{0.48})`) and density-1 SUPPLY.
3. Whether the prime-gap empirical measure is Lucas mixing (the arithmetic heart,
   in no source).

## Actionable item handed on (portfolio of work, not my tool to run)

`code/scholar/mr_gap_correlation_probe.py` — probes whether the Mauduit–Rivat
digit-sum statistic is even correlated with the gap-parity string `h` the fold
reads — is **UNEXECUTED** (no capture in `code/out/`). It tests whether
Mauduit–Rivat/Green (the digit-sum theorems) are truly inert for the fold or do
touch it. Run:

```
python3 -m lib.capture --target code/out/mr_gap_correlation_probe.captured.txt -- python3 code/scholar/mr_gap_correlation_probe.py 300000
```

## Durable findings stored this pass

1. Library maturity cross-check: every source digested, the stubs quarantined, the
   one actionable item is the unexecuted MR↔gap-parity correlation probe.
2. `walsh-spectral-subset-b904` stays open; the Pivato `answers:` line is retracted
   and the finite-prefix transfer is the central gap.
