# MISLABELED SOURCE: "Abdesselam–Chipalkatti Hilbert covariants" is the wrong paper

**File on disk:** `research/sources/abdesselam-chipalkatti-hilbert-covariants.full.md`
(580 lines, 29,571 bytes) · Summary: `research/summaries/abdesselam-chipalkatti-hilbert-covariants.md`

## What the file actually contains

The full text and the summary are **Campagna & Pagh, "On Finding Frequent
Patterns in Event Sequences"** (arXiv:1010.2358v1, cs.DS, 12 Oct 2010) — a
data-mining paper about sampling frequent "traces" in directed acyclic graphs from
RFID baggage-trolley readings at Copenhagen Airport, with algorithms
SAMPLETRACES and streaming approximations. It has **nothing to do with Hilbert
covariants, binary forms, the Hessian, or the Casas-Alvero conjecture.**

The file's `<!-- source: https://arxiv.org/pdf/1010.2358 -->` header grabbed the
wrong arXiv id.

## What was intended

The intended source is **Abdesselam & Chipalkatti, "On Hilbert covariants",
Canad. J. Math. 64(5):975–994 (2012), doi:10.4153/cjm-2012-046-1** (arXiv id
**1010.2667**, NOT 1010.2358). Its load-bearing content for this run is:
"the Hessian (second transvectant (F,F)_2) of a binary form F of degree n vanishes
identically **iff** F is a perfect n-th power of a linear form" — the Hilbert
covariant H_{1,d} whose coefficients cut out the perfect-power locus
scheme-theoretically.

**The intended paper is NOT held anywhere in RESEARCH/.** A grep for the content
terms (`Hilbert covariant`, `binary form`, `1010.2667`) across `research/sources/`
returns nothing. The hessian-covariant approach and the grounding note cite it by
name/DOI, but the actual text is absent.

## Consequence for the run

1. **The approach files cite a source that is not held.** `hessian-covariant-
   transvectant.md` (killed-by) and `grounding-three-proposed-approaches.md`
   attribute the Hessian ⟺ perfect-power theorem to "Abdesselam–Chipalkatti 2012,
   arXiv:1010.2358". That theorem is *real* (it is the classical Hilbert
   criterion), but the file held under that name is the Campagna–Pagh data-mining
   paper — a **non sequitur** for the claim. The theorem's citation is therefore
   currently **unanchored** in the library.
2. **The hessian-covariant approach was already refuted on the unproved bridge**
   ("the derivative-sharing conditions force (F,F)_2 = 0" is the run's own
   conjecture, no source applies covariant algebra to CA). So the missing source
   does not un-refute the approach. It only means the *one sourced fact* the
   approach kept is attributed to a paper the library does not actually hold.
3. **Action:** the correct arXiv id is 1010.2667; the library should re-fetch the
   true Abdesselam–Chipalkatti paper if that fact is ever needed as a held source
   (it is not needed for the adopted arithmetic-jet-lift route). Until then, treat
   `hessian-covariant-transvectant.md`'s "arXiv:1010.2358" pointer as **wrong id**.

## Record as a contradiction / integrity flag

The librarian-audit note already flags Kostov's `2020_higher-order` as a
mislabeled duplicate. This is a **second, more severe mislabel**: a downloaded
file whose entire content is an unrelated paper. Worth recording so no later pass
quotes the "Hilbert covariants" file as evidence.

```claim
id: abdesselam-chipalkatti-file-mislabeled
statement: The file research/sources/abdesselam-chipalkatti-hilbert-covariants.full.md (and its summary) holds the WRONG paper: Campagna & Pagh, "On Finding Frequent Patterns in Event Sequences", arXiv:1010.2358 (cs.DS data-mining), not Abdesselam & Chipalkatti, "On Hilbert covariants", Canad. J. Math. 2012 (arXiv:1010.2667) which the run cites for Hessian-iff-perfect-power. The intended Hilbert covariants paper is NOT held.
hypotheses: the arXiv id 1010.2358 belongs to Campagna-Pagh; the intended paper is 1010.2667
holds-here: yes
status: checked
bearing: any claim citing 'Abdesselam-Chipalkatti arXiv:1010.2358' for the Hessian-iff-perfect-power theorem is currently anchored to a non-sequitur file; re-fetch 1010.2667 if that fact is ever needed as a held source. The hessian-covariant approach was already refuted on the unproved bridge, so this does not affect the adopted route.
anchor: research/sources/abdesselam-chipalkatti-hilbert-covariants.full.md
```
