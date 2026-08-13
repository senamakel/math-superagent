# Librarian cycle — 2026-08-13 (uniform-Mordell-Lang foundation tier + frontier arXiv:2010.04919)

## Gap filled

`research/THREADS.md` flagged the adopted approach `uniform-height-bound-elliptic-ap`
as "Resting on nothing recorded": its two foundational inputs (`height-uniform-mordell`
= Dimitrov–Gao–Habegger, `uniform-mordell-lang` = Gao–Ge–Kühne) had no primary source
on disk, and no claim block established either. The GFP 2026 theorem's constant chain
("ineffective, via Rémond's quantitative Mordell-Lang") was asserted, not anchored.
This cycle fixed all of that with **four** primary full-text PDFs plus one companion:

## Downloads added (all full PDFs on disk)

1. **DGH, "Uniformity in Mordell-Lang for curves"** — arXiv:2001.10276 (the Annals
   Math. 194 (2021) 237–298 paper). If you search for this paper you will be offered
   **arXiv:2103.06203** by a search summary — that is **WRONG**: 2103.06203 is Kühne's
   relative Bogomolov paper. The real DGH preprint is 2001.10276. Both are now filed
   under their own names (this conflation is recorded in the Kühne summary so nobody
   trips on it again).
   - Full: `research/sources/dimitrov-gao-habegger-uniform-mordell-lang-2021.full.md`
   - Summary: `research/summaries/dimitrov-gao-habegger-uniform-mordell-lang-2021.md`
2. **GGK, "The Uniform Mordell-Lang Conjecture"** — arXiv:2105.15085v4 (accepted at
   Publ. Math. IHÉS).
   - Full: `research/sources/gao-ge-kuhne-uniform-mordell-lang-2021.full.md`
   - Summary: `research/summaries/gao-ge-kuhne-uniform-mordell-lang-2021.md`
3. **Gao, survey "Recent developments of the Uniform Mordell-Lang Conjecture"** —
   arXiv:2104.03431.
   - Full: `research/sources/gao-survey-uniform-mordell-lang-2021.full.md`
   - Summary: `research/summaries/gao-survey-uniform-mordell-lang-2021.md`
4. **Kühne, "Equidistribution in Families of Abelian Varieties and Uniformity"** —
   arXiv:2101.10272.
   - Full: `research/sources/kuhne-equidistribution-families-abelian-2021.full.md`
   - Summary: `research/summaries/kuhne-equidistribution-families-abelian-2021.md`
5. **Kühne, "The Relative Bogomolov Conjecture for Fibered Products of Elliptic
   Curves"** — arXiv:2103.06203 (the mis-identified-identifier paper, now correctly
   filed under its own name).
   - Full: `research/sources/kuhne-relative-bogomolov-fibered-products-2021.full.md`
   - Summary: `research/summaries/kuhne-relative-bogomolov-fibered-products-2021.md`
6. **Wu, "Châtelet surfaces and non-invariance of the Brauer-Manin obstruction for
   3-folds"** — arXiv:2010.04919 (the frontier's remaining cited-by-2 row, the
   companion to the already-held 2103.01784 surfaces paper).
   - Full: `research/sources/wu-chatelet-surfaces-noninvariance-3folds-2020.full.md`
   - Summary: `research/summaries/wu-chatelet-surfaces-noninvariance-3folds-2020.md`

## What this cycle establishes (claim blocks written, in research/CLAIMS.md)

- `ggk-uniform-mordell-lang-theorem` (proved): GGK Thm 1.1 — X(F) ∩ Γ covered by
  ≤ c(g,d)^(1+rkΓ) cosets, constants **existential**.
- `dp07-explicit-uniform-ml-elliptic-self-products` (asserted): per GGK p. 3, DP07
  (IMRP 2007, Thm 1.13) is the **only** prior uniform-ML result with a *completely
  explicit* constant, and it targets subvarieties of self-products of an elliptic
  curve — the shape of the MSS AP configuration.
- `dgh-uniform-mordell-lang-curves` (proved, holds-here **no**): DGH Thm 1.1 is for
  genus ≥ 2; the MSS's E_c is genus 1, so DGH does not apply directly — the effective
  lane is DP07/Rémond.
- `dgh-height-inequality-nondegenerate` (proved): the height inequality that anchors
  the uniformity results (existential constants).
- `kuhne-equidistribution-uniform-ml-curves` (proved, holds-here **no**): g ≥ 2 again.
- `kuhne-relative-bogomolov-fibered-products` (proved): encyclopedic-technical.
- `wu-chatelet-3folds-bm-noninvariance` (proved): BM non-invariance caution for 3-folds.

## Net effect on the adopted approach

The `uniform-height-bound-elliptic-ap` thread's "resting on nothing" rows in
THREADS.md are now anchored at primary sources, and the run's belief that "the
constant C is ineffective" is **verified at the primary source** (GGK state it; also
DGH's and Kühne's constants are existential). The one genuinely open lane for an
effective constant is **David–Philippon IMRP 2007** — the unique explicit-constant
uniform-ML result, of the right (E^n) shape. The `request_research` for DP07's
statement/constant was auto-rejected (the library's pointer claims matched), so the
gap is recorded **here** for the scholar: obtain DP07 Thm 1.13, check the AP-in-
x-coordinates subvariety of E^2 satisfies its hypotheses, and see whether its explicit
C can reach C^(1+ρ) < 3. Until that is done, the uniform-height approach remains
blocked by the ineffective constant — now with the full primary-source chain on disk
to prove why.

## Deliberate boundary

This cycle's 6 downloads all serve the *adopted* thread's foundation and the frontier
top tier. No further gathering is warranted except against a stated gap in
REQUESTS.md / this note (DP07, or a new thread's need).