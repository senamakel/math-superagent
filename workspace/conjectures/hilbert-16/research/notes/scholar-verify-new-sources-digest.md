# Scholar pass — verifying/resolving the research agent's new sources against the goal

## What the research agent added, and what I did

The current librarian cycle (addendum) added two primary full texts — **DGR 2002**
and **Luca 2009** — which a prior scholar pass had already digested into claim
blocks. My job this pass: re-verify those claims against the held full texts,
store the durable findings (they were made when Cognee was down and never
persisted), complete the durable record for the fifth-pass items, and confirm
none of the newer material contradicts what the run already holds.

## Verified against full text (this pass)

### DGR 2002 — every bound confirmed
`research/sources/dumortier-guzman-rousseau-elementary-graphics-focus-center-2002.full.md`
(1910 lines). I read the theorem lines and confirmed the claim
`drr-dgr-2002-elementary-closures` verbatim:
- Thm 3.1 (l.456-460): (H³₄),(H³₅) cyclicity ≤ 2, **irrational** ratios.
- Thm 3.2 (l.987-990): (H³₄),(H³₅) ≤ 2, **rational** ratios; r(0)=1 (A=2) ⇒ first
  saddle quantity 2B≠0.
- Thm 3.3 (l.997): (H³₆) ≤ 2 if r(0)≠1, ≤ 3 if r(0)=1, full 5-param unfolding.
- Thm 4.1 (l.1292): (I²₂₇) ≤ 2.
- Thm 5.1 (l.1432): (I²₁₄a),(I²₁₅a) finite cyclicity.
- Lemma 5.2 (l.1504-1506): (R(x))^r not affine, nonvanishing higher derivative.
- Thm 5.3 (l.1534): (I²₁₅b) ≤ 2. **All seven rows sourced-held with explicit
  small cyclicity bounds (2 or 3) — among the few DRR rows Lean can carry an
  exact number for.**

### Luca 2009 — alien-cycle caveat confirmed
`research/sources/luca-dumortier-caubergh-roussarie-alien-limit-cycles-2009.full.md`
(2642 lines). Abstract (l.28-37) confirms: a limit cycle "not controlled by a
zero of the related Abelian integral", via the **second derivative of the
transition map** along the saddle connection. Claim
`h16-alien-limit-cycles-abelian-insufficiency` accurate. The alien example is
**cubic** (n=3), so it does not touch the quadratic DRR frame (already recorded
in `research/approaches/abelian-picard-fuchs-argument-principle-sharp-count.md`
l.34-40).

## Confirmations / corrections carried from the fifth pass (persisted to memory now)

- **Torregrosa 2024, M(3) ≥ 12** — current best local cubic lower bound,
  supersedes Żołądek's 11; the "twelfth small-amplitude cubic cycle" target is
  already achieved, so the certified-lower-bound approach must beat 12
  (`approach-certified-lower-bound-target-escalated`).
- **Villanueva–Tucker 2026** — Bautin-ideal **enclosure** 𝔅(ℱ_h(n)) ⊆
  ⟨v_{n+1,*}⟩ (even n) / ⊆⟨L_{(n−1)/2}, v_{n+1,*}⟩ (odd n), sufficiency,
  unrefereed, conditional. An instrument for the Bautin step.
- **Lu 2026 bundle scripts** — both HELD now but NOT re-executed in this
  workspace; the U(0)=1/48 / both-centre-components / global-barrier rows are
  **asserted** until a clean-room capture (`lu-h14-3-bautin-focal-values-u0`,
  `lu-h14-3-global-center-domains-checked-statements`).

## NEW finding this pass: a stale memory EDGE persists after the text fix

`recall_memory` this pass returned — alongside two correctly-worded memory
passages ("The two Lu (2026) H14^3 bundle scripts ... NOW HELD") — a live graph
**edge** `lu-h14-3-verification --[not_held]--> verify_h14_center_bautin.py`.
Prior digest passes corrected the *text* of the memory (CONTEXT gap-2 closed at
holding level) but this `not_held` **connection** still sits in the graph. The
contradiction is between the graph edge and the memory passages, not between
memory and the library: the library holds both scripts in full
(`research/sources/lu-h14-3-verify-center-bautin.py.full.md`,
`lu-h14-3-verify-center-global-domains.py.full.md`), so **the `not_held` edge is
wrong**. The corrective half is preserved: verification is still outstanding, so
the claims stay `asserted`. Re-storing the corrected relationship so the graph
drops the `not_held` edge.

## Sources that do NOT help (and why)

- **Gasull–Lázaro–Torregrosa 2010** — the held `.full.md` is only the arXiv
  **abstract page**; the exact (K,n) Abelian zero bounds are NOT establishable
  from it. **Do not cite a number from it.** The concrete Chebyshev instrument
  the run can lean on is Grau–Mañosas–Villadelprat (Trans AMS 2011, fully held).
- **Álvarez–Coll–De Maesschalck–Prohens 2020** canard-lower-bound summary is a
  broken "Redirecting" capture (claim `data-canard-2020-summary-broken-capture`);
  carried at MaRDI-review level only.
- The **`llibre-zhang-lienard-conjecture-survey`** file is contaminated (an
  unrelated Mureddu power-grid paper, arXiv:1612.05532) — never cite it for the
  Liénard survey.
- The landing-pages inventory (`data-landing-pages-inventory`) — kaloshin.html,
  binyamini.html, yakovenko.html, rousseau-shan-zhu .full, etc. are record pages
  with no mathematics beyond an abstract; do not re-read them as full texts.

## Contradictions — none new; existing ones stand

- Dulac finiteness "settled" vs Yeung 2024-25 peer-reviewed gap claim vs
  community view (Llibre 2024) that Dulac's problem is again under review. The
  theorem is not disproved; the *proof's completeness* is contested.
- DRR 121 vs 125 (RSZ/RR/Ilyashenko vs Shan 2013) — unresolved; DRR 1994 raw
  catalogue not held.
- Liénard n=5 still open (Llibre–Zhang 2017); Rychkov 1975 settles only the
  odd-only degree-5 case (refines, does not strike, `h16-lienard-n5-open`).
- The monomial-count quadratic-complement note in scratch is **not** established
  (its own text: "not yet a theorem... weak evidence") — no conflict with the
  established "do not chase a closed form" position in CONTEXT.

## What I stored to memory (all verified/recorded, with source URLs)

1. DGR 2002 seven elementary closures with exact bounds and theorem-line anchors.
   Source: dms.umontreal.ca/~rousseac/DGR.pdf.
2. Luca 2009 alien-cycle/Abelian-insufficiency caveat. Source: users.ugent.be
   LUCA preprint.
3. Torregrosa 2024 M(3)≥12. Source: DOI 10.1007/s40863-024-00486-9.
4. Villanueva–Tucker 2026 Bautin-ideal enclosure (conditional). Source:
   arXiv:2602.22558v2.
5. Lu bundle scripts held-but-asserted (U(0)=1/48 etc.). Source:
   arXiv:2607.13785v2.
6. Gasull–Lázaro–Torregrosa 2010 landing-page-only (do-not-cite).
7. Huzak 2022 canard cyclicity bounds.

## What the run still lacks (unchanged)

- **Clean-room re-execution of the two held Lu bundle scripts** — would upgrade
  the focused bundle rows from asserted to checked (thread
  `lu-h14-3-verification`, next-step).
- Complete current 121-graphic ledger (DRR 1994 raw list / post-2020
  consolidation) — the standing gap, requests `complete-current-ledger-cb3d` /
  `dumortier-roussarie-rousseau-9c4f` still open.
- Full texts of Li–Liu–Yang 2009 (H(3)≥13), Han–Li 2011, Mañosas–Villadelprat
  2011 (all paywalled) — captured at claim level only.
