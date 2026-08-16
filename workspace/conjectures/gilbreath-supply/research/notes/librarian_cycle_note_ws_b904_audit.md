# Librarian cycle — open-request audit (walsh-spectral-subset-b904)

**Verdict: NOTHING FURTHER.** No new source this cycle. This is a fresh
determination by the librarian prompt directly (not a prior-pass rubber-stamp):
I re-checked the one open request and the correctness of the three prior
"NOTHING FURTHER" determinations.

## What I actually did this cycle

Three targeted searches, two of which were the narrowest defensible phrasings
of the open request:

1. `exa_search` "weight spectrum of Reed-Muller codes two families Carlet Solé"
   — surfaced Carlet–Solé 2023 (Discrete Math, DOI 10.1016/j.disc.2023.113568),
   Lou–Wang 2024 RM(m−6,m) (arXiv:2406.03803), Carlet 2023/2024 RM(m−5,m).
   **All lead somewhere, none closes the request** (see below).
2. `exa_search` "Walsh spectrum lower bound weight of image of linear map F2
   binomial basis folded weight" — surfaced Boole-an-function/code-construction
   papers (Ding, Xiang–Feng–Tang) that bound the *weight enumerator of a code
   from a Walsh spectrum*, i.e. the reverse direction of what the request needs
   (they need a known Walsh spectrum to get weights; the request needs a weight
   bound from a weak input). Not equivalent; nothing new.
3. `search_documents` + `grep_workspace` over `research/sources/` confirmed
   every reachable candidate is already held or already ruled out.

## Why the reachable literature does not close the request

The open request asks for a Walsh/subset-sum **lower bound** on `wt(Φ_n x)` for
the submask (Pascal-mod-2 / Rule-90) fold, valid for inputs not "complicated"
in the five refuted senses — i.e. a deterministic per-image bound from a weak
arithmetic input, not a distribution.

- **Carlet–Solé 2023** determines the *weight spectra* (sets, not per-image
  bounds) of `RM(m−3,m)`, `RM(m−4,m)` — the **high-order** codes (r close to
  m). The fold image is a **low-order** Boolean function (sublinear ANF support),
  so the high-order spectrum is the wrong end and gives no per-image bound.
  Confirmed NOT on disk: the prior run recorded a guessed arXiv id fetched an
  unrelated paper (`DELETED_wrong_arxiv_carlet_sole.md`); the true DOI is
  paywalled on ScienceDirect. **Re-fetch not warranted** — even obtained, it
  does not bear on the request's low-order per-image question.
- **Lou–Wang RM(m−6,m)** (arXiv:2406.03803) and the middle-order survey
  **Abbe–Shpilka–Ye** (arXiv:2002.03317) are **already held**
  (`lou_wang_weight_spectrum_RMm6.full.md`,
  `abbe_shpilka_ye_reedmuller_survey.full.md`); the grounding
  `rm_weight_spectrum_grounding.md` already documented that middle-order weight
  spectra resolve only the "set of weights", not a per-image lower bound from an
  input hypothesis. Nothing new to fetch.
- The Walsh-spectrum→code papers (Ding 2015, Xiang–Feng–Tang 2015) go the wrong
  direction and require a *computed* Walsh spectrum; they cannot serve as a
  *lower bound from an input on x*.

## Prior determinations corroborated

Three prior librarian audits (`librarian_pass3_terminus_cycle.md`,
`librarian_audit_pass3_closed.md`, `librarian_audit_this_cycle.md`) independently
concluded NOTHING FURTHER. I re-checked the load-bearing facts directly:
FRONTIER top rows held, the coding-theory engine (MacWilliams/Krawtchouk/
Delsarte/O'Donnell/Yoshida) present, the one open request a theorem gap. All
hold.

## State

- The one open request `walsh-spectral-subset-b904` stays **open and is a
  theorem gap**: it needs an in-house F₂ / hypergeometric / Krawtchouk input
  argument, not a downloaded paper. The existing on-disk weight lemmas
  (Yoshida Lemma 2: power-of-two leading-row floor, sublinear; Donoho–Stark;
  MacWilliams/Krawtchouk; the proved Binomial(n−2,1/2) law) remain the state of
  that line.
- The two live open lemmas (G-threshold-asymptotic-zero, G-threshold-concentration)
  and the prime-second-moment `E[S(n)²]=O(n)` are self-provable /
  in-house-computable, not missing sources.
- No FRONTIER candidate read this cycle answers a stated gap (directive 7/27/30
  gate; a fetch would require naming one — I did not find a case where any would
  answer).

Nothing new to add to the library this cycle; the collection is complete for
the live line.
