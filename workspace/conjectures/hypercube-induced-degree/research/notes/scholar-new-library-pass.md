# Scholar pass — new-library-material digest (research agent's last delivery)

This pass reviewed the library against the goal (exact value / Θ(√n) residue of
f(n)=min{D(S):|S|=2^{n-1}+1}, max internal degree) after the research agent
finished. Almost everything was already digested and claimed across three prior
scholar notes (`scholar-research-library-digest.md`,
`scholar-synthesis-gap-closed.md`, `scholar-digest-new-sources.md`,
`scholar-digest-new-sources-v2.md`, `scholar-unread-material-digest.md`). What
this pass actually added:

## New / previously unclaimed material

The three OEIS catalogue stubs that were in `research/summaries/` but had no
claim block and were NOT covered by the prior unread-material digest (which only
handled A002264, A003056, A053251, A202453 and the four citation graphs):

- `oeis_a007895.md` (Zeckendorf term count) → new claim `oeis-a007895-not-f`
- `oeis_a033307.md` (Champernowne decimal expansion) → new claim `oeis-a033307-not-f`
- `oeis_a238279.md` (compositions by runs) → new claim `oeis-a238279-not-f`

All three are catalogue noise, unrelated to f(n); each now carries a claim block
(status: catalogued, holds-here: yes) and entered CLAIMS.md. No closed form for
f(n) comes from any of the seven OEIS sequences the run has looked up. The sqrt
of f(n) is structural (A_n²=nI), not a catalogue index.

## Everything else: already digested

The ~18 real mathematical sources (Barber, Liu–Zhou, Falik–Samorodnitsky,
Keevash–Long, Harper ×2, Ellis ×2, Ellis–Keller–Lifshitz, KKL, Beckner,
Friedgut, Beltrán–Ivanisvili–Madrid, Durcik–Ivanisvili–Roos, Kruskal–Katona,
induced-subgraphs, Barber–Erde) were already claimed and synthesised. No
re-digest needed. The four citation-graph stubs were already judged in
`scholar-unread-material-digest.md`.

## One real contradiction, carried forward

Barber's balanced-independent-set formula is transcribed two ways in the
library (odd-n max = 2^{n-1}−2^{n-2}(n−1) without /2 in the source prose vs
with /2 in its own claim block and summary). The code check
(`barber-balanced-formula-odd-half`, status checked) confirms the /2 version.
Not load-bearing for D(S) (it is the d=0 line). Stored in durable memory.

## Open lead (not evidence)

Ambainis–Bavarian–Gao–Mao–Sun–Zuo (LICS 2014), "Tighter Relations between
Sensitivity and Other Complexity Measures", surfaced from the Falik–Samorodnitsky
citation graph. It sits on problem.md's "Connections to Boolean function
complexity" sidebar; the transfer from sensitivity-complexity to D(S) is the
run's recorded unproved gap. Lead only — not fetched. (`request_research` gate
refused to queue it on keyword overlap; recorded in durable memory and in the
citation stub.)

## Bottom line

Nothing in the new library changes the decisive result: f(n) ≥ √n for all n
(spectral proof, re-derived and machine-verified), so f(n)=Θ(√n) and the
log–sqrt gap is closed from below. The live residue is exact f(n)=ceil(√n) for
non-square n (n=2,5 exceed √n) and rebuilding the upper construction. The new
OEIS rows and the Ambainis lead change none of that.
