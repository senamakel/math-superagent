# Álvarez–Coll–De Maesschalck–Prohens 2020 — broken capture / claim carried at review level

<!-- source: https://doi.org/10.1016/j.jde.2019.09.057 | the held file is a "Redirecting" HTML stub, not the paper. Do not re-download. -->

## Status of this held file

The file `research/sources/alvarez-coll-demaesschalck-prohens-canard-lower-bounds.full.md`
(if present) is a **broken "Redirecting" capture** — an Elsevier redirect stub
with no mathematics. It establishes nothing on its own and is kept only as a
provenance record that the paper was looked for.

## What the paper claims (sourced at MaRDI-review level — full text paywalled at ScienceDirect)

Claim `h16-canard-asymptotic-lower-bound-2020` (in `research/notes/claims.md`)
carries the verified statement: Álvarez, Coll, De Maesschalck, Prohens,
"Asymptotic lower bounds on Hilbert numbers using canard cycles",
J. Differential Equations 268 (2020) 3370–3391, defines
**H̲(N) = (N² log N)/(2 log 2)·(1+o(1))** and proves there is a sequence
N_k → ∞ with H(N_k) ≥ H̲(N_k) for all k — the modern slow-fast/canard
construction confirming the Christopher–Lloyd / Han–Li n²-log-n lower bound.
Method: singularly perturbed Liénard systems (ẋ = y−F(x), ẏ = εG(x)), canard
cycles and nests, singular Hopf bifurcation. Evidence class is **sourced
(MaRDI review text)**, NOT held-full-text.

## What it implies here

- This is a **second independent confirmation of the n²-log-n growth**, via
  canards rather than Abelian integrals — the same mechanism as Huzak's
  cyclicity-bounds route (held full).
- The held claim, not this broken file, is what downstream work may cite.

```claim
id: data-canard-2020-summary-broken-capture
statement: The held summary/source for Álvarez–Coll–De Maesschalck–Prohens
  (canard lower bounds, JDE 268 (2020) 3370–3391) is a broken "Redirecting"
  HTML capture with no mathematics; the paper's claims are carried at
  MaRDI-review level by h16-canard-asymptotic-lower-bound-2020 (full text
  paywalled at ScienceDirect, no open copy located).
hypotheses: none -- a provenance fact.
holds-here: yes
status: checked
bearing: prevents re-downloading or citing a number from the broken capture;
  the canard n^2 log n lower-bound claim rides on the MaRDI-sourced claim
  block, not on this file.
anchor: research/summaries/alvarez-coll-demaesschalck-prohens-canard-lower-bounds.md
follows-from: h16-canard-asymptotic-lower-bound-2020
```