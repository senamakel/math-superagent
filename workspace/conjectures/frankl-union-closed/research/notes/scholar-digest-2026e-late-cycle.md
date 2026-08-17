# Scholar digest — late-cycle confirmation pass (2026e)

Purpose: confirm the state of the reference library after the Maric body repair,
store the durable findings that Cognee is refusing (outage), and flag any
remaining loose end. All numbers/claims below were re-traced to their anchors
this pass, not re-derived.

## Maric body repair — verified sound, no contradiction

The genuine body `research/sources/maric-zivkovic-vuckovic-fc-families-2012.full.md`
(arXiv:1207.3604) carries Theorem 5.1(5): all families containing four 3-element
sets whose union is in a 7-element set (uniform `73_4`) are FC-families, proved
by the Isabelle/HOL `ssn`-verified computation (Lemma 9; ~22.8 min of the 28-min
check is the uniform-73_4 case). The earlier wrong body (arXiv:1209.5628,
Oberdieck number theory) appears ONLY in "do not cite this" contexts across the
workspace — verified by grep (4 files, all negative-reference contexts).

- Claim `maric-4-3subsets-7set-fc` is correctly primary-anchored (status: proved,
  by the paper's own machine-verified computation), returned by `search_claims`.
- Contradiction check: no durable recalled memory says anything contradictory.
  The claim matches the survey's §5.1 restatement and the n≤12 FC-based
  verification chain.

## Coupling claims — both correctly filed, ceilings preserved

- `coupling-true-inf-crossing-4d` (verified-numerically, NON-rigorous): true inf
  of g/Eh over the 4-parameter two-atom class crosses 1 between t=0.3824 and
  0.3825 at alpha=0.035, minimizer a≈0.3300622 (b2=1) — the published 0.38234
  frontier recovered from the CORRECT sup-inf object after the scorer inversion.
- `coupling-interval-bb-infeasible-10s` (measured, checked): generic mpmath.iv
  4D interval B&B cannot certify t=0.38234 in 10s (margin 8.89e-6, enclosure
  slope C~21, minimizer on b2=1 boundary). A method/harness result, NOT a UC
  result and NOT a failure of the theorem.

Both are returned by `search_claims`. Their ceilings (numerical vs measured,
never "proved") are stated in the blocks.

## The one mechanical loose end: stale odd-filter task/goal

The task `verify-odd-filter-minmax` is left OPEN but its detail still instructs
"assert the unique minimizer is the odd filter". That uniqueness is REFUTED by
the run's own completed capture `code/out/odd_filter_minmax.captured.txt`
(three programs, exhaustive n≤4 + independent inline route + structural n≤8):
the minimizers of max-density over non-Boolean UC families are exactly n+1 —
the odd filter plus, for each x, the power-set-minus-singleton `2^[n]\{{x}}` —
all at `2^{n-1}/(2^n-1)`. The live goal `abundance-profile-odd-filter-minmax`
rests on this refuted uniqueness phrasing.

The value `2^{n-1}/(2^n-1)` stands; only the UNIQUENESS is false. Already flagged
in `research/threads/abundance-profile.md` ("Stale-task warning"). This pass
re-confirmed from the capture end-to-end (n=2:3, n=3:4, n=4:5 minimizers; odd
filter is one of them, yes). This row is the only place the run still carries a
refuted claim as an open target — a later pass should close the task and restate
the goal's uniqueness half.

## Durable memory is blocked; workspace is the fallback

`remember_memory` and `relate_memory` are refused (Cognee outage, 5 failures).
Per the tool's own guidance, the durable findings that cannot reach Cognee are
written here and are already safe in the on-disk claim store (`maric-4-3subsets-7set-fc`,
`coupling-true-inf-crossing-4d`, `coupling-interval-bb-infeasible-10s`,
`odd-filter-max-density-extremal-nonboolean`). When the memory service recovers,
store these four durably so they surface in cross-run recall.

## What the run still lacks

- Cognee durable recall of the four claims above (blocked by the outage; parked
  safely on disk).
- The open moduli of the odd-filter task/goal uniqueness phrasing (the value is
  settled; only the "unique" word is wrong).
- No source fetched this pass and no new contradiction introduced: the library
  remains internally consistent.
