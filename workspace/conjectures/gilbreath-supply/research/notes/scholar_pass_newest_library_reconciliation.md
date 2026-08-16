# Scholar pass: reconciling the research agent's finished pass against the library

Author: scholar. Date: this pass. Scope: the research agent finished and the
task says the reference library has new material. This pass read what the
agent's cycle actually added to `research/`, against GOAL (can the fold `Φ`
do work the switch-density form cannot see), the task ledger, and the current
beliefs (ROOT/CLAIMS/threads/backward/approaches), and records what is new,
what each piece establishes, what does not help, and what contradicts or
confirms recalled memory.

## What the new material actually is

Directive 30 records the agent's tick as **sources 44 → 50, summaries 58 → 69,
frontier 348 → 445**. Reconciling the on-disk list against every prior pass's
coverage, the genuinely new items are:

1. **`research/summaries/citations_w2010510777.md` — Chebyshev's Bias
   (Rubinstein–Sarnak 1994, DOI 10.1080/10586458.1994.10504289).** The seventh
   citation-graph file. All prior passes audited **five** (Maynard, ABGS,
   Mentzer-contamination, LOS, Pivato–Yassawi, Allouche–Shallit); this one was
   filed later and no pass has read it. It is a **lead, not evidence**: the
   header itself says "Filed by a citation-graph lookup, not read … a lead,
   not evidence". Its cited/cited-by surface (Fiorilli–Martin inequality
   series, Harper–Lamzouri races, Bays–Hudson, the RS 1994 paper) is the
   GRH+LI conditional prime-race literature already **refuted** as an approach
   (`rubinstein-sarnak-prime-race-ergodic`, killed-by: conditional on GRH+LI,
   one-point, logarithmic-density; the fold's g=0 term is an unconditionally
   open two-point mod-4 switch-pair). No claim, no theorem, no change.

2. **`research/summaries/mauduit_rivat_gelfond_somme_chiffres_premiers_primary.md`
   — Mauduit–Rivat 2010 *primary* digest.** Théorèmes 1–3 verified this pass's
   predecessors against the full text (lines 284–305): for q,m>2,
   `#{p≤x : s_q(p)≡a (mod m)} = ((m,q−1)/m)·π(x; a, (m,q−1)) + O(x^{1−σ})`;
   the digit-sum of primes is equidistributed with a power-saving error;
   Gelfond's second problem answered. **Bearing:** the paradigm of a weak,
   unconditional, provable arithmetic input the primes satisfy (GOAL priority
   2's weakest-input shape) — but the statistic is **s_q(p), digit sum of the
   prime**, while Φ reads the gap-parity string `h[j]=((q_{j+1}−q_j)/2) mod 2`.
   **No transfer; does not close `walsh-spectral-subset-b904`.** Its claim
   block is PROVED but absent from the rendered CLAIMS.md (derive gap, below).

3. **`research/summaries/shiu_strings_congruent_primes.md` — Shiu 2000 claim
   digest.** The full theorem: arbitrarily long strings of consecutive primes
   ≡ a (mod q), q≥3, (q,a)=1; for q=4, a=1 and a=3 both in A± so there are
   arbitrarily long constant runs in h — refutes closed door 3 (no-long-constant-runs).
   This removes the caveat that the Shiu input was "unsourced here" (the Wiley
   original never downloaded): the locally-held Ethan Yang expository states
   and proves the theorem. Its block is likewise absent from the rendered ledger.

4. **The six other citation digests + four OEIS rows + the HAL page** — all
   already digested/flagged do-not-re-read by prior passes. No new theorem in
   any of them.

## What this establishes for the run

**Nothing changes the run's state.** The library's position is unchanged and
all three open items remain open, re-confirmed:

- **The finite-prefix transfer** (ergodic Lucas-mixing at density-one *times*
  ⇒ quantitative `wt(Φ_n h) ≥ c·n` for the fixed prime string) — the single
  largest missing technical tool; in no source; both halves absent.
- **Request `walsh-spectral-subset-b904`** — a Walsh/subset-sum lower bound on
  `wt(Φ_n x)` for inputs not complicated in the five refuted senses — genuinely
  open; it is a gap in theorems, not in the library.
- **`s2_N → 0` (or finiteness of the exceptional set) for the prime h** — the
  sharpest open problem of the density-1 form; measured (Ratio B 1.3155@40000)
  but unproved; in-house computation, not literature.

The operative line stays `fold-second-moment-krawtchouk` /
`downset-row-code-distance-closed-form`: geometry side (condition C —
`F_n(z)=O(n)`, `A_2=Θ((log n)²)`, rank n−2, exact Binomial(n−2,1/2)) settled;
the single open input is (A) `E[S(n)²]=O(n)` for the real prime h, which by
Chebyshev gives density-1 SUPPLY.

## The derive-pass gap (bookkeeping, re-confirmed)

`grep '^id:' research/summaries` shows ~51 claim blocks in the summaries; the
rendered `research/CLAIMS.md` (133 lines) does NOT contain several of the
newer ones — in particular `takei-rule90-mixing-limits-uniform`,
`mauduit-rivat-*` (both), `shiu-string-theorem`, `rw-runlength-is-2regular`,
`rw-thm20-binomialsum-structure`, `rw-average-nonlinear`, `mr-short-averages...`,
`mrt-fourier-uniformity...`, `rowland-nonzero-binomial-prime-power`,
`szechtman-lucas-submask-corollary`, `lucas-submask-odd`,
`gilbreath-verified-10^13`. The knowledge is on disk in the summaries; a
derived-file refresh should pick them up. **Do not read absence from
CLAIMS.md as absence from the library** — read the summary files directly.

## Sources that do not help this pass (so nobody re-reads them)

- `citations_w2010510777.md` — citation graph, lead only; the RS paper it
  points at is already held and its approach already refuted.
- The other six `citations_w*`, the four OEIS rows, the HAL metadata page —
  flagged do-not-re-read by prior passes; re-confirmed nothing new.
- `mauduit_rivat_gelfond_hal_page.md` — metadata record only; the primary is
  the `..._primary` digest.

## Contradictions

None new. The two CLAIMS.md "contradictions" rows (`r-finite-verified` vs the
rung name; `rw-described-as-the-fold-itself` vs the correction) remain
stale-id artefacts self-resolved by prior passes. The one live-on-disk
bookkeeping staleness is the derive gap above. No source contradicts recalled
memory; the citation files agree with the library's own digests wherever they
overlap.

## Durable findings stored this pass

1. The 7th citation file (`citations_w2010510777`, Chebyshev's Bias) is a lead
   not evidence; its RS surface is the GRH+LI refuted approach.
2. The derive gap: newer summary claim blocks absent from rendered CLAIMS.md;
   consult summaries directly.
3. The reconciled inventory of what the agent's tick added (Mauduit–Rivat
   primary digest + Shiu claim digest are the only new claims-bearing matter;
   both proved, both inert as transfer, both absent from the ledger).
4. The one genuine frontier lead (MMPY 2006 Markov-subgroup attractiveness),
   catalogued, gated by the search freeze.

## Claim blocks filed

```claim
id: newest-material-adds-no-evidence
statement: The research agent's finished pass added to research/ the 7th citation file (citations_w2010510777, Chebyshev's Bias/RS 1994 — lead only, its surface is the GRH+LI refuted prime-race approach), the primary Mauduit–Rivat 2010 digest (digit-sum-of-primes equidistribution with power-saving error; the paradigm weak arithmetic input but statistic s_q(p) ≠ gap-parity h, no transfer), and the Shiu 2000 full-claim digest (arbitrarily long equal-residue strings; refutes door 3; resolves the earlier 'Shiu unsourced' caveat). No new theorem changes the run's state: the finite-prefix transfer, request walsh-spectral-subset-b904, and s2_N→0 remain the open items.
hypotheses: none — this is an audit statement about library contents and bearing.
holds-here: yes
status: checked (this pass read the 7th citation file and re-verified the two new claim-bearing digests against their full texts via prior passes' verbatim checks)
bearing: nobody should re-fetch Chebyshev-race material expecting a way past the parity barrier; the two new proved claims fix the paradigm (Mauduit–Rivat) and close the door-3 caveat (Shiu) but neither transfers to wt(Φ_n h). The run's open state is unchanged.
anchor: research/notes/scholar_pass_newest_library_reconciliation.md; research/summaries/citations_w2010510777.md; research/summaries/mauduit_rivat_gelfond_somme_chiffres_premiers_primary.md; research/summaries/shiu_strings_congruent_primes.md
```

```claim
id: claims-md-derive-gap-newer-summary-blocks
statement: The rendered research/CLAIMS.md does not contain several claim blocks that live in the summaries with holds-here/status already written: takei-rule90-mixing-limits-uniform, mauduit-rivat-prime-digit-sum-equidistributed, mauduit-rivat-gelfond-sum-of-digits-primes-equidistributed, shiu-string-theorem, rw-runlength-is-2regular, rw-thm20-binomialsum-structure, rw-average-nonlinear, mr-short-averages-of-multiplicative-functions-cancel, mrt-fourier-uniformity-averaged-correlations-vanish, rowland-nonzero-binomial-prime-power, szechtman-lucas-submask-corollary, lucas-submask-odd, gilbreath-verified-10^13 (grep '^id:' across research/summaries vs CLAIMS.md). The knowledge is on disk in the summaries; the derived file is stale.
hypotheses: the derive logic parses claim blocks from notes/summaries; some new blocks are missed (prior pass flagged the same class for takei and the mauduit-green note).
holds-here: yes
status: checked (by grep diff this pass)
bearing: consult the summary files directly before concluding the library lacks a statement; the next derive refresh should pick these up.
anchor: research/notes/scholar_pass_newest_library_reconciliation.md; grep of research/summaries vs research/CLAIMS.md
```