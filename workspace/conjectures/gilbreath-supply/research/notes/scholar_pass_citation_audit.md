# Scholar pass: audit of the research agent's citation-fetch pass

Author: scholar. Date: this pass. Scope: the research agent finished and the
reference library gained new files; this pass read what is now in `research/`
against GOAL (test whether the fold `Φ` can do work the switch-density form
cannot see), the task ledger, and the current beliefs (ROOT/CLAIMS/threads),
and records what the new material actually establishes.

## What the new material is

The six `research/summaries/citations_w*.md` files are **citation-graph lookup
tables** (OpenAlex/DOI metadata): the abstract, reference list, and cited-by
list of one paper each. Each file's own header says "Filed by a citation-graph
lookup, not read … a lead, not evidence". They are:

| File | Paper | Verdict |
| --- | --- | --- |
| `w1554274636` | Maynard 2016, *Dense clusters of primes in subsets* | lead only; the paper is already fully digested (`maynard-positive-density-congruent-strings`) |
| `w2027719385` | Ash–Beltis–Gross–Sinnott 2011 | lead only; already digested (`abgs-*` claims, the parity barrier) |
| `w2070854196` | **Mentzer et al. 2001, "Defining Supply Chain Management"** | **contamination** — a business-management paper pulled by a word-match on "SUPPLY"; zero bearing; its citation ring (~40 supply-chain rows) pollutes FRONTIER.md's ranking |
| `w2295728007` | Lemke Oliver–Soundararajan 2016 | lead only; already digested (`los-switch-preferred-mod4`, `los-scale-bias-slowdecay`) |
| `w2953389333` | Pivato–Yassawi 2003, *Asymptotic randomization of sofic shifts* | lead only; already digested (`lucas-mixing-iff-fold-randomization` etc.) |
| `w4210391712` | Allouche–Shallit 1992, *The ring of k-regular sequences* | lead only; already digested (`as-kregular-*`) |

**No new source, theorem, or claim entered the library through this pass.**
Five of the six files point at papers the run already holds in full; the sixth
is off-topic noise.

## The one genuinely new lead the citation files surface

`w2953389333` (Pivato–Yassawi 2003) lists as its top cited-by row:

> **Maass, Martínez, Pivato, Yassawi 2006, "Attractiveness of the Haar measure
> for linear cellular automata on Markov subgroups"** (IMS Lecture Notes–
> Monograph Series, 10.1214/lnms/1196285812).

This is the direct follow-up to the digested Pivato–Yassawi 2003 that extends
the Lucas-mixing / asymptotic-randomization theory to measures supported on
**Markov subgroups** — the exact shape of the `lucas-mixing-finite-transfer`
thread's demand (a measure class richer than Bernoulli, still provably
randomized by `Φ = 1+σ`). It is **absent from FRONTIER.md**. It is a lead, not
evidence: (a) it is measure-level, so it cannot by itself close request
`walsh-spectral-subset-b904` (a finite `wt(Φ_n h) ≥ c·n` bound); (b) the search
freeze (directives 7, 27) gates any fetch behind naming an unworked frontier
candidate. Recorded here so a later pass can name it if the freeze lifts.

## What this pass confirmed about the rest of the library

- **Fully digested:** every full text in `research/sources/` has a claim-
  bearing digest in `research/summaries/`; the claim ledger (`search_claims`,
  100+ rows) is consistent with the notes. No template stub remains: the two
  "metadata stub" summaries (`ashikhmin_barg_litsyn_polynomial_method`,
  `friedlander_macwilliams_krawtchouk`) are correctly flagged as landing-page-
  only fetches whose content is covered by better digested local sources
  (`macwilliams_1963`, `guruswami_macwilliams_lp_notes`) — do not re-fetch.
- **Wrong-download quarantine is correct:** `matomaki_radziwill_tao_averaged_chowla`
  is a pointer to the correctly-named MRT source; `DELETED_wrong_arxiv.md`
  records the four arXiv-ID collisions. No wrong content entered the claims.
- **Does-not-help files are all marked:** the four OEIS rows (base-4 digits of
  e/π, 3-adic sqrt(−2), fractal ternary — none touches the fold),
  `odlyzko_gilbreath` (bibliography index), the Granville–Martin duplicate
  mirror, `chase_random_gilbreath` (`holds-here: no`), the Gilbreath
  encyclopedic row (out of scope per GOAL.md).
- **The parity-barrier tier is verified verbatim:** ABGS §1/§9 "wide open, and
  cannot be treated using L-functions"; Lau: even one non-constant 2-term mod-4
  pattern is beyond reach; the equal-residue side (Shiu/Maynard/BFTB/Freiberg)
  is unconditional but wrong-direction. The reduction of SUPPLY to switch
  density is a dead end; attacking the fold directly is the only live route.

## FRONTIER.md contamination (persistent, not fixed)

`research/FRONTIER.md` still carries ~40 rows of "DEFINING SUPPLY CHAIN
MANAGEMENT" citations (blockchain, operations research, sustainability) ranked
at the top by the cited-by count of the business paper. These are noise: they
matched the word "SUPPLY" in the wrong domain and must not be downloaded. The
math rows (consecutive-prime tuples, prime races, Lucas 2-regular sums,
affine-CA limit measures) are the real frontier; read FRONTIER by subject, not
by rank. Fixing the ranking (excluding the contamination ring from derivation)
is a hygiene item for whoever owns the frontier derivation.

## Contradictions with recalled memory

None new. The two CLAIMS.md "contradictions" rows (`r-finite-verified` vs the
rung name; `rw-described-as-the-fold-itself` vs the correction) are stale-id
artefacts already self-resolved by prior verification passes and flagged as
such there. The citation files agree with the library's own digests wherever
they overlap (same DOIs, same abstracts).

## What the run still lacks (unchanged, restated once)

1. **The finite-prefix transfer** — the single largest missing technical tool:
   ergodic "Lucas mixing ⟺ randomization at density-one times" (Pivato–Yassawi
   Thm 7.1) to a quantitative `wt(Φ_n h) ≥ c·n` for the fixed prime string.
   In no source; both halves (a: the prime-gap measure is Lucas mixing,
   b: quantitative weak-*→weight) absent.
2. **Request `walsh-spectral-subset-b904`** — a Walsh-spectral/subset-sum lower
   bound on `wt(Φ_n x)` for inputs not complicated in the five refuted senses.
   Genuinely open; no source states it (it is a gap in theorems, not in the
   library).
3. **`s2_N → 0` (or finiteness of the exceptional set) for the prime h** — the
   sharpest open problem of the density-1 form; measured (s2_N 0.000783@4000 →
   0.0000934@40000, Ratio B 1.3155@40000) but unproved; in-house computation,
   not literature.

## Bottom line

The research agent's citation pass added **no new evidence and no new claims**:
five leads to already-held papers and one contamination file. The run's state
is exactly where the prior scholar passes left it: the geometry side of the
adopted `fold-second-moment-krawtchouk` line is settled (rank n−2, exact
Binomial(n−2,1/2), down-set meet formula, A₂ = Θ((log n)²), F_n(z) = O(n));
the arithmetic heart (A) — `E[S(n)²] = O(n)` for the prime h — remains the
single open input. The next loop should not re-read the citation files; it
should attack the in-house computation, per the search freeze.

Durable findings from this pass stored with `remember_memory`: the citation-
files-are-leads verdict + the one new lead (MMPY 2006 Attractiveness), and the
library-integrity confirmation (no stubs, quarantine correct, FRONTIER
contamination identified).

```claim
id: citation-pass-added-no-evidence
statement: The research agent's citation-fetch pass added six files under research/summaries/citations_w*.md, all citation-graph lookup tables ("filed by a citation-graph lookup, not read ... a lead, not evidence"). Five point at papers already fully digested in the library (Maynard 2016, ABGS 2011, Lemke Oliver–Soundararajan 2016, Pivato–Yassawi 2003, Allouche–Shallit 1992); the sixth (w2070854196) is Mentzer et al. 2001 "Defining Supply Chain Management", a business-management paper pulled by a word-match on SUPPLY — off-topic contamination. No new source, theorem, or claim entered the library through this pass.
hypotheses: none — this is a bookkeeping/audit statement about the library's contents, not a mathematical theorem.
holds-here: yes
status: checked (all six citation files read this pass; overlap with digested sources verified by DOI/name)
bearing: nobody should re-read the citation files expecting content; the run's open state is unchanged (finite-prefix transfer and request walsh-spectral-subset-b904 remain the genuine gaps); FRONTIER.md's supply-chain spam rows are noise to be excluded from ranking.
anchor: research/notes/scholar_pass_citation_audit.md; research/summaries/citations_w*.md
```

```claim
id: mmpy2006-attractiveness-new-lead
statement: The Pivato–Yassawi 2003 citation graph lists as its top cited-by row Maass, Martínez, Pivato, Yassawi 2006, "Attractiveness of the Haar measure for linear cellular automata on Markov subgroups" (IMS Lecture Notes–Monograph Series, doi 10.1214/lnms/1196285812), the direct follow-up extending asymptotic-randomization-by-Phi=1+sigma theory to measures supported on Markov subgroups. This paper is absent from research/FRONTIER.md. It is a lead, not evidence: it is measure-level, so it cannot by itself close request walsh-spectral-subset-b904 (a finite wt(Phi_n h) >= c*n bound), and the search freeze (directives 7, 27) gates any fetch behind naming an unworked frontier candidate.
hypotheses: the paper exists as cited (citation-graph metadata only, not read); its bearing on the finite SUPPLY bound is unestablished.
holds-here: unchecked (lead only)
status: catalogued
bearing: the one genuinely new frontier candidate surfaced by the citation pass; name it if the search freeze lifts and a Markov-subgroup-measure input is wanted for the lucas-mixing-finite-transfer thread.
anchor: research/summaries/citations_w2953389333.md; research/notes/scholar_pass_citation_audit.md
```

