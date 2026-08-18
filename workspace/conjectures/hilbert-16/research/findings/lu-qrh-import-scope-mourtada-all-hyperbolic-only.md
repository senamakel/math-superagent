# Lu H14³ QRH import scope — Mourtada used for the all-hyperbolic sub-word only, DIR2002 for the semihyperbolic endpoints

## Finding (scholar, verified against held sources)

Lu arXiv:2607.13785 (held full text `research/sources/lu-h14-3-2026.full.md`)
imports **Mourtada's QRH theorem** (the 2009 source now held in full) for a
*narrow, matched* scope, and the semihyperbolic part is covered by a different
source — there is no category error in the import.

**The exact scope (lines 1443–1451):**

> "We begin with an exact-once itinerary already shown in Part I to contain
> only **separated hyperbolic saddles and regular first hits**. We first
> construct its physical analytic system, then verify QRH membership and a
> common admissible representative, and only then invoke Mourtada's local
> finiteness theorem. We use Mourtada's principal-orbit and integral-projection
> framework, the local rational and quasi-resonant construction in Appendix VA
> and the proof of Theorem 0, the QRH inverse result VB4, and the local
> finiteness theorem IVC1 along an admissible Hilbert derivation [3]."
>
> "IVC1 gives finite local degree only for a QRH closing germ along an
> admissible derivation χ ∈ ΞH_k[QRH], on one common admissible positive-corner
> representative. It is **not a finiteness theorem for an arbitrary C^p
> functional system**."
>
> "For the central and lips cases we use Theorem 3, Theorems 3.1–3.2, and
> Corollary 3.6 of **Dumortier–Ilyashenko–Rousseau [2]**" (DIR2002 saddle-node
> normal forms).

So: Mourtada IVC1/Théorème 0 is applied only to the **all-hyperbolic word**
(separated hyperbolic saddles, exact-once itinerary), and the **semihyperbolic
horizontal endpoints** (the "additional difficulty" RR 2015 flagged) are handled
by DIR2002's finite-multiplicity saddle-node machinery — not by Mourtada. The
title "Semihyperbolic Hemicycle" describes the whole graphic; the imported
theorems each cover their own matching sub-structure.

## What this implies for the run's verification

1. The `lu-h14-3-verification` thread's reliance on Mourtada 2009 is **well
   grounded**: the import is the all-hyperbolic sub-word, exactly the class
   Mourtada's Théorème 0 (hyperbolic polycycle, eigenvalue ratio −1) covers.
2. The semihyperbolic endpoints are NOT covered by Mourtada — they rest on
   DIR2002. The run's verification of Lu's finite core must check the **DIR2002
   hypothesis verification** (Theorem 3.1's saddle-nodes of opposite
   attractivity, pp/BP clauses, Corollary 3.6 no-pp) against the physical
   family, which is a separate and equally load-bearing step.
3. Mourtada's Théorème 0 in the PDF (lines 50–62) restricts the presentation to
   eigenvalue ratio −1 "pour simplifier la présentation"; Lu's positive double
   ramification (23.2) r̃ = mr/n → 1+μ reduces a fixed rational ratio r₀=n/m to
   the resonant case — consistent with Mourtada's framework, not an extension
   of it.

## Evidence class

`asserted-by-source` — quoted from the held Lu full text (lines 1443–1455) and
the held Mourtada PDF (lines 50–62). No theorem proved by this run.

## Contradictions

None with recalled memory. This *confirms* the thread's `rests-on` (Mourtada
QRH for all-hyperbolic words) and sharpens it: the DIR2002 hypothesis-check is
the additional step the thread should verify, not Mourtada's applicability.
