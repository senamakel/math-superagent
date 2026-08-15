# Goal

Attack **SUPPLY** (`problem.md`) as a self-contained problem about the primes
and one explicit `F₂` fold. Gilbreath's conjecture is not the goal here and must
not be claimed; SUPPLY is one input to it and stands on its own.

## What this run is for

The parent investigation reduced Gilbreath to SUPPLY, proved everything else,
and then closed five structural routes to SUPPLY — see *Five closed doors*.
The reduction of SUPPLY to mod-4 switch density is available and is a named
open problem behind the parity barrier. **This run exists to test whether the
fold `Φ` can be made to do work that the switch-density form cannot see.**

That is the single hypothesis under test. If it fails, say so and close the
problem; a clean negative is the second-best outcome and far better than
drift.

## Priorities

1. **Target the averaged forms first.** `ν₂(n) ≥ c·n` for almost all `n`, or on
   a density-1 set, is the most likely place a real theorem exists — the parity
   barrier is pointwise and is sometimes porous on average.
2. **Find the weakest arithmetic input that suffices.** Not "does positive
   switch density imply SUPPLY" — that is known. Rather: *what is the weakest
   statement about the primes from which `wt(Φ_n h) ≥ c·n` follows?* Candidates
   worth pricing: bounded autocorrelation of `h`, a second-moment or variance
   bound, a Fourier/Walsh coefficient bound on `h`, or an input about `h` only
   along binary-submask sets (which is what Lucas makes `Φ` read).
3. **Prove the equivalence, if that is the truth.** If SUPPLY really is
   equivalent to switch density, prove it. That is a genuine theorem and it
   closes this problem honestly rather than leaving it ambiguous.

## Rules

- **Stream, never materialise.** The parent run was OOM-killed at 161 minutes
  holding a depth-4000 exact-integer triangle. One row at a time; collect the
  single diagonal cell per depth as you go. Every capture prints the depth it
  reached.
- **A measurement is not a proof.** Label it. The parent run measured
  `ν₂/n ≈ 0.49` and that is evidence, not progress.
- **Do not reopen a closed door.** Five are listed in `problem.md` with their
  witnesses. A proposal implying any of them is wrong; check before spending.
- **No hypothesis of the form "h is complicated enough".** That family is
  refuted as a family, not case by case. The obstruction is that `Φ` has
  low-weight images on rich inputs.
- **Every settled conclusion gets a fenced claim block** with `id`, `statement`,
  `hypotheses`, `holds-here`, `status`, `bearing`, `anchor`. Mirror the id in
  `research/ROOT.md`, which is not derived.
- **A capture that checked nothing must not read as a pass.** State the count
  checked. Include a negative control — a case that *should* fail — in every
  verification, and show it failing.
- **Lean claims need `#print axioms`.** No `sorryAx` in a footprint that a note
  calls sorry-free. The parent run shipped six such theorems before it was
  caught.

## Out of scope

The Gilbreath reduction, Lemma 5.4, the demand side, BHP record gaps, and the
absorption/descent machinery are all **already proved** in the parent workspace
and are not to be re-derived. If a result there is needed, cite it; do not
rebuild it.
