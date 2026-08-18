# Écalle, "Introduction aux fonctions analysables et preuve constructive de la conjecture de Dulac" — author's avant-propos page

**Source URL:** https://www.imo.universite-paris-saclay.fr/~jean.ecalle/ecadulac.html
(author's own page, Université Paris-Saclay; the book itself: Hermann, Actualités
mathématiques, 1992, 337 pp, ISBN 2-7056-6199-9 — **not held**, no legitimate
open copy located; the shadow-library "copies" found by search are not stored)

**Evidence class: primary author text** — Écalle's own account of the book's
scope and of the Dulac proof as a resummation exercise (avant-propos dated
January 1991).

## What the page establishes

1. **Book's structure.** Originally conceived as only the proof of Dulac's
   conjecture, it became a general treatise on resummation introducing two new
   function classes — **analysable functions** (fonctions analysables) and
   **cohesive functions** (fonctions cohésives). The Dulac proof proper occupies
   only chapters 3–4 of ten. Written "without any concern for Hilbert's 16th
   problem".
2. **Analysable functions.** Grosso modo the natural closure of the algebra of
   real-analytic germs (at +∞) under `{+, ×, ∂, ∘}` and their inverses. They are
   **totally formalisable**: each analysable germ reduces to a formal transseries
   (well-ordered sums of transmonomials built from ℝ-coefficients and
   `{+,×,∂,∘,exp,log}`). The corresponding transseries are generically
   **divergent**, so reconstructing the geometric object from the formal one
   requires **accelero-summation** through finitely many intermediate models
   linked by acceleration operators (Borel–Laplace transmutations of changes of
   variable). The accelerates are **cohesive** or analytic germs with a unique
   (generally ramified) development over ℝ⁺; cohesive functions form a
   quasianalytic class with all the regularity properties Carleman classes
   lacked. Every cohesive function is a weak accelerate (proved at the end of
   the book).
3. **The Dulac proof as resummation.** Decompose the first-return map
   `F = G_r ∘ … ∘ G_1` into passage maps at the polycycle's vertices; take the
   formal counterpart `F̃ = G̃_r ∘ … ∘ G̃_1` (each factor a formal series or an
   elementary transseries). The composition `F̃` is a general transseries with
   potentially maximal exp–log stacking, but is **always accelero-summable**;
   its sum `F` is an analysable function which, **if it differs from the
   identity, can only have isolated fixed points** — the non-oscillation
   statement that proves Dulac's conjecture.
4. **Length and uniqueness.** Admitting the theory of analysable functions
   (especially closure under composition) as external, proving analysability of
   the factors takes ~10 pages; building the theory from scratch is ~100
   incompressible pages. The return map is a *very special* analysable function
   (each factor has a single critical time, summable by Borel–Laplace without
   acceleration), so other routes exist — notably Ilyashenko's geometric
   non-constructive method (Lindelöf-principle extension), and the
   "immiscibility lemmas" of §4.6 (of which **one remained unproved at the time
   of writing**, but the acquired ones already suffice to greatly simplify the
   non-oscillation proof — so the missing lemma is not load-bearing for the
   main result).
5. **Écalle's three convictions.** (1) The only sensible real-coefficient formal
   object carrying all the information of `F` is the **median transseries** `F̃`;
   (2) the only explicit constructive reconstruction of `F` from `F̃` is
   **median accelero-summation**; (3) only total formalisation of `F` gives a
   complete understanding of it and of everything built from it (e.g.
   non-oscillation of its successive derivatives).
6. **Chapters 5–10** (complements): quartage / cryptolinear formulas (ch. 5);
   identity of cohesive functions with weak accelerates (ch. 6); analysable
   functions as the **ultimate limit of formalisability of germs** — beyond the
   scale of iterated exponentials and logs there are no canonical reference
   functions (universal asymptotics of slow/fast germs, indiscernability
   theorem) (ch. 7–9); natural notion of transfinitely iterated growth scales and
   the "Grand Cantor" (ch. 10).

## Why it matters to this run

- **This is the answer to Test 1 of problem.md for the Écalle route.** The
  step that fails for C^∞ fields is precisely analysability + cohesivity: a
  flat C^∞ germ is invisible to the transseries, so the median transseries
  determines the map only within the analysable class. The proof is
  constructive: `F` is determined by `F̃` via accelero-summation, and
  non-identity analysable maps have isolated fixed points. A finiteness
  argument that never uses analysability/cohesivity (or some other
  quasianalytic input) proves a false statement.
- Distinguishes the **1992 book** from the **1990 LNM 1455 article**
  ("Finitude des cycles-limites et accéléro-sommation de l'application de
  retour", claim `ecalle-1990-accelerosommation-record`): the 1990 article is
  the Luminy 1989 conference version; the 1992 book is the full treatment
  introducing analysable/cohesive functions. Both are Écalle's independent
  proof of Dulac's conjecture (with Ilyashenko 1991).
- Records, in the author's own words, that one immiscibility lemma was
  unproved at writing but was **not load-bearing** — a useful precision for the
  Dulac-gap thread (Yeung's contentions concern Ilyashenko's proof; this page
  concerns Écalle's).
- The alien-limit-cycle phenomenon (Luca–Dumortier–Caubergh–Roussarie 2009,
  held) and the natural-levels thread (Yeung) live precisely in the
  formal-vs-geometric gap this avant-propos describes.

## Status / disposition for the ledger

- The book's full text is **not held** (no legitimate open copy). This page is
  the author's own description of the proof's architecture and is a primary
  statement of *what the proof claims and where analyticity enters* — usable as
  a citation anchor for the method, not as the proof itself.
- Cross-links: claims `ecalle-1990-accelerosommation-record`,
  `h16-dulac-finiteness`, thread `lu-h14-3-verification` (adjacent),
  `research/sources/primary-ecalle-1990-finitude.full.md` (the 1990 article
  held).
