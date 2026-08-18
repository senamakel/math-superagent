# Canard lower bound: H̲(N) = (N² log N)/(2 log 2)·(1+o(1)) (Álvarez–Coll–De Maesschalck–Prohens 2020)

```claim
id: h16-canard-asymptotic-lower-bound-2020
statement: Álvarez, Coll, De Maesschalck, Prohens, "Asymptotic lower bounds on Hilbert numbers using canard cycles", J. Differential Equations 268 (2020) 3370–3391, define H̲(N) = (N² log N)/(2 log 2)·(1+o(1)) and prove there is a sequence N_k → ∞ with H(N_k) ≥ H̲(N_k) for all k — the modern slow-fast/canard construction confirming the Christopher–Lloyd / Han–Li n²-log-n lower bound. Method: singularly perturbed Liénard systems (ẋ = y−F(x), ẏ = εG(x)), canard cycles and nests, singular Hopf bifurcation.
hypotheses: slow-fast Liénard singular perturbation; canard-cycle construction; the Hilbert number H(N) for degree N.
holds-here: yes (as a lower bound; it does not bound H(n) above)
status: asserted-by-source
evidence: sourced at MaRDI-review level — full text paywalled at ScienceDirect, no open copy located; the held file research/sources/alvarez-coll-demaesschalck-prohens-canard-lower-bounds.full.md is a broken "Redirecting" stub with no mathematics (see claim data-canard-2020-summary-broken-capture). The claim statement is carried by research/summaries/alvarez-coll-demaesschalck-prohens-canard-lower-bounds.md.
falsifier: A source showing the canard construction is invalid (e.g. the canard cycles are not distinct or not limit cycles), or a correction retracting the lower-bound claim, would falsify it. The n² log n lower growth itself is independently confirmed by Christopher–Lloyd 1995 / Han–Li 2012 (claim h16-hn-lower-bound-asymptotic), so only the canard route's specifics ride on this source.
sources: https://doi.org/10.1016/j.jde.2019.09.057
anchors: research/summaries/alvarez-coll-demaesschalck-prohens-canard-lower-bounds.md
note: This claim block replaces the dangling reference — the id was cited as living in research/notes/claims.md but no block with this id existed on disk. The evidence class is sourced-at-review-level, NOT held-full-text: treat the exact theorem statement as provisional until the paper body is obtained.
follows-from:
answers:
```

## Why this claim block exists

The entailment ledger flagged `data-canard-2020-summary-broken-capture` as following
from `h16-canard-asymptotic-lower-bound-2020`, which "does not exist". The id was
referenced in summaries and LIBRARY-STATUS but never written as a claim block. This
block records the canard lower-bound claim with its honest evidence class (MaRDI
review level, full text paywalled).
