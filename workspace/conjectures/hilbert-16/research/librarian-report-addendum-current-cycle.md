# Librarian cycle report — DRR elementary closures + Abelian-integral caveat

## What was added this cycle (2 primary full texts)

1. **Dumortier–Guzmán–Rousseau 2002**, "Finite cyclicity of elementary graphics
   surrounding a focus or center in quadratic systems", Qual. Theory Dyn. Syst.
   3:123–154. Obtained the open PDF from Rousseau's own page
   (`dms.umontreal.ca/~rousseac/DGR.pdf`), a source the library had previously
   only *cited* through other held papers.
   - **Full text**: `research/sources/dumortier-guzman-rousseau-elementary-graphics-focus-center-2002.full.md`
   - **Summary**: `research/summaries/dumortier-guzman-rousseau-elementary-graphics-focus-center-2002.md`
   - **Claim**: `drr-dgr-2002-elementary-closures` (in `research/notes/claims.md` +
     `derived/CLAIMS.md`)
   - **What it closes**: seven elementary DRR graphics now carry a held primary
     source with explicit cyclicity bounds — (H³₄),(H³₅) ≤ 2, (H³₆) ≤ 2/≤ 3,
     (I²₂₇) ≤ 2, (I²₁₄a),(I²₁₅a) finite, (I²₁₅b) ≤ 2. These rows were added to
     `research/drr-list.md` as sourced-held (previously untracked/not-primary).

2. **Luca–Dumortier–Caubergh–Roussarie 2009**, "Detecting alien limit cycles
   near a Hamiltonian 2-saddle cycle", DCDS 25(4):1081–1108. Obtained the open
   preprint from the first author's UGent page.
   - **Full text**: `research/sources/luca-dumortier-caubergh-roussarie-alien-limit-cycles-2009.full.md`
   - **Summary**: `research/summaries/luca-dumortier-caubergh-roussarie-alien-limit-cycles-2009.md`
   - **Claim**: `h16-alien-limit-cycles-abelian-insufficiency`
   - **What it establishes**: a **caveat on the Abelian-integral route** — a
     cubic Hamiltonian 2-saddle cycle can produce an *alien* limit cycle not
     controlled by zeros of the Abelian integral, via the second derivative of
     the transition map along the saddle connection. This is the canonical
     counterexample to "Abelian-integral zero counts alone bound limit cycles
     from Hamiltonian perturbations" for degree ≥ 3, and bears directly on
     GOAL step 4's Abelian-integral candidate.

## Why these, from the frontier/requests

The open request (`dumortier-roussarie-rousseau-9c4f`) is the DRR ledger, and
prior passes established no consolidated post-2020 ledger exists. I therefore
worked the *gaps within* the DRR inventory: the elementary-graphics closures had
no held primary source, and the tangential-H16 thread lacked the alien-cycle
caution that bounds how much the Abelian-integral route can deliver. Both gaps
are now closed with primary full texts.

## Where things stand / notes

- Memory server (Cognee) is down this cycle, so nothing was stored to durable
  memory; the findings were persisted in the workspace's own ledger
  (`research/notes/claims.md`) and `LIBRARY-STATUS.md`, which is where this run
  stores findings while Cognee is unavailable.
- `describe_file` is blocked for `research/` (Cognee index refusal), so file
  purposes are recorded in `LIBRARY-STATUS.md` instead of an INDEX.md.
- The frontier work is not exhausted (Rousseau 1997 survey still paywalled on
  ScienceDirect; DRR 1994 raw list still paywalled), but both were re-confirmed
  unavailable this cycle and their content is substantively reproduced by held
  sources, so re-fetching them spent nothing more.
