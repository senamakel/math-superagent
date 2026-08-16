# Librarian report — third pass (reopened, verification-only)

Author: librarian. Scope: verify the reference library is intact, complete, and
indexed for the reopened question (a functional of the fold `Φ` sensitive to
correlation order `1 < K ≲ n/2`, controllable by an arithmetic input strictly
weaker than pointwise mod-4 switch density); confirm no genuine library gap
remains; report availability with source URLs. No new download is made — every
on-topic candidate is already held, and the one open gap is a gap in theorems,
not in the library.

## What I verified this pass

**Library complete and indexed.** `research/sources/` holds 63 files, of which
61 are full texts each carrying its source URL on line 1 (via the
`<!-- source: ... -->` marker, spot-checked across all 60 in a grep sweep);
two are the correctly-superseded "wrong download" markers
(`matomaki_radziwill_tao_averaged_chowla`) that point at the correct MRT file
and must not be cited — this is the in-place supersession rule, not a dead
weight. `research/summaries/` holds 91 digests including claim blocks.

**The reopened question's territory is covered.** GOAL priority 2 asks for a
`K > 1` functional of the fold controlled by a weaker-than-switch arithmetic
input. The library's coverage of that territory:

- **Higher-order (K>1) structure of the prime gap sequence is on disk and
  digested:**
  - Lacasa, Luque, Gómez, Miramontes, *On a dynamical approach to some prime
    number sequences*, Entropy 20(2):131, 2018, arXiv:1802.08349 — exact
    **unconditional** forbidden multi-gap-block enumeration (K>1) from
    divisibility: |F(m)| = 3^m − 2^{m+1} forbidden mod-6 gap blocks. (Claim
    `lacasa-forbidden-gap-blocks-unconditional`.)
  - Lemke Oliver & Soundararajan, *...sums of sawtooth random variables*,
    arXiv:1709.06168 — the **K≥2** secondary bias term c₂ via
    Σ conj(χ(k))L(0,χ)L(1,χ)A_{q,χ}, odd in k. (Claim
    `los-sawtooth-secondary-bias-term`.)
  - Lau 2024, arXiv:2409.12819 — even one non-constant 2-term residue pattern
    mod 4 is beyond reach (claims `lau-nonconstant-pattern-open`,
    `lau-pattern-count-bound`).
- **The switch-density (K=1) barrier and the fold machinery are all held**:
  ABGS 2011, LOS 2016, Granville–Martin, Rubinstein–Sarnak (switch/mod-4 side);
  Meštrović (Lucas), Bacher, Hofer, Allouche–Shallit I&II, Rampersad–Wiebe,
  Rowland, Szechtman (fold/2-regular side); Pivato–Yassawi ×3, Takei,
  Matusiak/Donoho–Stark, Tao (Rule-90/Ca/uncertainty); Odlyzko 1993, Chase 2022,
  encyclopedia Gilbreath (the {0,2} difference object itself); and the
  coding/Boolean-analysis engine (O'Donnell, Essential Coding Theory,
  MacWilliams 1963).

**Search-reachability.** `search_documents` on the load-bearing subjects
(higher-order prime structure, Rule-90 randomization, Shiu strings, Krawtchouk/
MacWilliams, Lucas) returns the right sources. The ranking is dominated by the
large textbook files (O'Donnell 980 KB, Essential Coding Theory 808 KB) — a
reader wanting a small source should go by filename, not by search rank.

**The genuine open gap is a theorem gap, not a library gap.** `walsh-spectral-
subset-b904` in REQUESTS.md — a Walsh-spectral/subset-sum lower bound on
`wt(Φ_n x)` for inputs not "complicated" in the five refuted senses — remains
open. No source states such an input-dependent bound for the fixed prime
string, and no further download can produce one. This matches directive 7's
freeze: the remaining work is in-house computation and theorem, not
literature.

## Availability (tiers — all present)

| Tier | Present | Key sources (full text in research/sources/, URL on line 1) |
|---|---|---|
| Switch-density / mod-4 residue barrier | yes | ABGS 2011 (fmwww.bc.edu/gross/ABGS.pdf); LOS 2016 (pmc.ncbi.nlm.nih.gov/PMC4978288); Granville–Martin Prime Number Races (dms.umontreal.ca/~andrew/PDF/PrimeRace.pdf); Rubinstein–Sarnak (math.uwaterloo.ca/~mrubinst/publications/Chebyshev.pdf); Lau 2024 (arxiv 2409.12819) |
| Equal-residue strings (doors 1–3) | yes | Shiu (expository, simonrs.com .../ethan-shiustrings.pdf); Maynard 2016 (arxiv 1405.2593); BFTB (arxiv 1311.7003); Freiberg (arxiv 1005.4703) |
| K>1 higher-order prime structure (reopened territory) | yes | Lacasa (arxiv 1802.08349); LOS sawtooth (ar5iv 1709.06168) |
| The fold / Lucas / 2-regular | yes | Meštrović (arxiv 1409.3820); Bacher (arxiv 0708.1430); Hofer (arxiv 2502.01343); Allouche–Shallit I&II (cs.uwaterloo.ca/~shallit/Papers/as0.pdf, plouffe.fr kreg2.pdf); Rampersad–Wiebe (arxiv 2309.04012); Szechtman (arxiv 2405.10352) |
| Coding / Krawtchouk / MacWilliams / Delsarte | yes | MacWilliams 1963 (user.eng.umd.edu/~abarg/ECC/macwilliams1963.pdf); O'Donnell (cs.cmu.edu/~odonnell/.../Analysis-of-Boolean-Functions.pdf); Guruswami LP notes; Essential Coding Theory |
| Ergodic / Rule-90 CA | yes | Pivato–Yassawi ×3 (arxiv math/0108082, math/0108083, math/0306136); Takei (doi 10.15803/ijnc.7.2_124); Pivato entropy (math/0210241); Matusiak/Donoho–Stark |
| Analytic-NT (weak prime inputs) | yes | Matomäki–Radziwiłł (arxiv 1501.04585); MRT Fourier uniformity (arxiv 1812.01224); Green–Tao (arxiv 0807.1736); Mauduit–Rivat (annals.math.princeton.edu) |
| The `{0,2}` difference object | yes | Odlyzko 1993 (ams.org/journals/mcom/...); Chase 2022 (arxiv 2005.00530); encyclopedia Gilbreath |

## Could not be obtained (reported so nobody retries)

- **Shiu 2000 primary PDF** — Wiley paywall; no free copy exists. Content fully
  reproduced by the held expository (`shiou_strings_expository`); the claim
  `shiu-string-theorem` is sourced from it. Do NOT retry the Wiley URL.
- **The `walsh-spectral-subset-b904` bound** — not a download gap; no such
  theorem exists in the literature to fetch.

## Bottom line

The reference library meets the phase-1 exit test and is topically complete for
the reopened `1 < K ≲ n/2` question. No further download is warranted; any new
source demanded by the run must first name an unworked FRONTIER candidate it has
read and why none answers (directive 7), and the one genuine open gap in
REQUESTS.md is a theorem to be proven, not a paper to be fetched.
