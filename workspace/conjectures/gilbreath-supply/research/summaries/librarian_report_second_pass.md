# Librarian report — second pass (reopened workspace)

Author: librarian. Date: this run (reopened)/terminus. Scope: verify the reference
library is intact and indexed for the reopened question, fix the one surviving
stale evidentiary label, and confirm the genuine open gap so nobody re-fetches.

## What I verified

- **Library complete and indexed.** `research/sources/` holds 45 full texts
  (each with its source URL recorded on the first line), `research/summaries/`
  holds 70 digests, including the claim-bearing Shiu expository digest and the
  higher-order-`K` prime-gap source (Lacasa et al., Entropy 2018 —
  `lacasa_dynamical_prime_sequences`), which is directly relevant to the reopened
  question (forbidden gap-blocks, unconditional K>1 structure; maps to forbidden
  binary blocks in h after mod-4 parity projection).
- **Search-reachability.** Spot-checked `search_documents` on the load-bearing
  subjects: Chowla/Shiu strings, Mauduit–Rivat, Krawtchouk/MacWilliams,
  Pivato–Yassawi Rule 90, Lacasa. All present and reachable. The ranking is
  dominated by large texts (808 KB coding-theory book) — a reader wanting a small
  source should go by filename, not search ranking.

## The one correction (CONTEXT.md)

Four passages in CONTEXT.md labelled the Shiu-2000 input "unsourced / Wiley
cookie-error stub". That is now **false** and was corrected: the library holds the
freely-available Ethan Yang expository
(`sources/shiu_strings_expository.full.md`,
http://simonrs.com/eulercircle/analyticnt/ethan-shiustrings.pdf) which states and
proves the full theorem (Thms 1.1/1.2/4.1), verified by scholar passes; claim
`shiu-string-theorem` carries it. For q=4, a=1,3 both in A± ⇒ arbitrarily long
constant mod-4 runs in the gap-parity string h — refutes closed door 3 and gives
primes-not-eventually-periodic. Only the primary's own PDF is absent (Wiley
paywall; confirmed no free copy exists by search this run). All four stale
passages in CONTEXT.md were edited to say the input is **sourced locally via the
expository**.

## The genuine open gap

`walsh-spectral-subset-b904` in REQUESTS.md — a Walsh-spectral/subset-sum lower
bound on `wt(Φ_n x)` for inputs not "complicated" in the five refuted senses —
remains open, and it is a **gap in theorems, not in the library**: no source
anywhere states such an input-dependent bound for the fixed prime string. No
further download can close it. (A Walsh-spectral/Boolean-function-analysis angle
was already examined and refuted as a standalone route —
`anf-mobius-reed-muller` and `walsh-subset-sum-fold-structure` are both closed.)

## Report of availability

| Tier | Present | Files |
|---|---|---|
| Switch-density / prime-residue barrier | yes | ABGS 2011, Lau 2024, LOS 2016, Granville–Martin, Rubinstein–Sarnak |
| Equal-residue strings (refute doors 1–3) | yes | Shiu (expository), Maynard 2016, BFTB 2015, Freiberg 2011 |
| The fold / Lucas / 2-regular | yes | Meštrović, Bacher, Hofer, Allouche–Shallit I&II, Rampersad–Wiebe, Rowland, Szechtman |
| Coding engine (Krawtchouk/MacWilliams/Delsarte) | yes | MacWilliams 1963, Guruswami LP notes, Essential Coding Theory, Ashikhmin–Barg–Litsyn, Friedlander, Wikipedia K+M |
| Ergodic / Rule-90 CA | yes | Pivato–Yassawi (3x), Takei, Pivato, Matusiak (Donoho–Stark), Tao |
| Analytic-NT (weak prime inputs) | yes | Matomäki–Radziwiłł, MRT, Green–Tao, Mauduit–Rivat |
| Higher-order prime-gap structure (reopened pass) | yes | Lacasa et al., Entropy 2018 |
| The `{0,2}` difference object itself | yes | Odlyzko 1993, Chase 2022, encyclopedia Gilbreath |

## Could not be obtained (reported so nobody retries)

- **Shiu 2000 primary PDF** — Wiley paywall, no free copy; content fully
  reproduced by the held expository.
- **The `walsh-spectral-subset-b904` bound** — not a download gap; no such
  theorem exists in the literature to fetch.
