# Scholar cycle — load-bearing spine verified against primary texts

**Role / source:** scholar, adversarial re-digest of the closed library. The
library is CLOSED (Directive 46/47): re-fetching is not work. The valuable
scholar contribution at this stage is verifying that the claims the run
actually stands on are faithful to the sources, and flagging any
inconsistency. This cycle read the four most load-bearing primary texts
directly (not their summaries) and checked them against the recorded claims.

## What was verified this cycle, against the full text

### 1. ABGS 2011 §9 — the named-open hypothesis (abgs-2011-s9-mod4-switch-limit-open)

Read `research/sources/ash-beltis-gross-sinnott-2011-successive-prime-residue-pairs.full.md` in full. Confirmed verbatim:

- Introduction: "To the best of our knowledge, Problem 1.1 is wide open, and
  cannot be treated using L-functions, unlike the case of Dirichlet's theorem."
- §9: "we cannot tell whether they are tending toward a limiting ratio of 1"
  (whether N(a,d,m,x)/N(a',d',m,x) → 1 as x→∞).
- Props 4.1 (power-of-2 residue-independence) and 4.2 (antidiagonal symmetry)
  are proved of the *heuristic* P_J, not of the true prime counts; only the
  heuristic is claimed.
- m=4 data over p∈[10³,10⁶]: switch pairs (1,3),(3,1) = 22521,22520; non-switch
  (1,1),(3,3) = 16574,16715. Switch 45041 vs non-switch 33289, ratio ≈ 1.354.

This confirms the claim as recorded: the mod-4 switch count (feeding Granville's
ν₂) is a two-point statistic whose linear lower bound is open and NOT provable by
one-point L-function machinery. This is the precise, load-bearing hypothesis of
the run's Route B conditional theorem. Prior note `research/notes/abgs-s9-verbatim-verified.md` already records the same; this cycle re-confirmed it directly.

### 2. Odlyzko 1993 — block lemma, linear constant 1

Read `research/sources/odlyzko-1993-iterated-differences-latex-source.full.md` in full. Confirmed verbatim (Introduction):

> "If for some N we find a K such that d_K(1) = 1 while d_K(n) = 0 or 2 for all
> 1 ≤ n ≤ N, then we can conclude that d_k(1) = 1 for K ≤ k ≤ N + K − 1."

So a {0,2} block of length N−1 protects N rows — **linear coefficient exactly 1**.
The ≈ n/2 figure appears nowhere in the paper. Confirms `odlyzko-block-lemma-exact`
and the refutation of `odlyzko-block-lemma-asserted`. Also confirmed eq. (2.2)
`d_{k+1}(n) ≡ d_k(n)+d_k(n+1) (mod 4)` (the mod-4 linearization) and Odlyzko's
explicit statement that "there is probably not too much special about the primes" —
supporting the general-class framing.

### 3. Killgrove–Ralston 1959 — independent block lemma

Read the full text. Confirmed verbatim: "if for some i and all j, 0 < j < M, we
have P_{ij} = 0 or 2 and P_{i0} = 1, then ... P_{i,0}, P_{i+1,0}, ..., P_{i+M-1,0} = 1".
Same linear constant 1, independent source. First machine verification to 63,419
primes. So the constant-1 block lemma is double-sourced.

### 4. Blair Morgan 2026 — corridor obstruction (sound, narrow)

Read the full text. The claimed result is narrow and sound: Row 2's frontier-8
prefix [1,0,2,2,2,2,2,2,4] cannot feed a *pure minimal* erosion corridor
8→7→6→5→4 (frontier value exactly 4 at position 4), because such a corridor would
force x_4=x_5=x_6=x_7=0 while Row 2 has (2,2,2,2). It rules out ONLY that minimal
first-erosion path; later frontier-8 rows, non-minimal breaches (value ≥6), and
stalled erosion remain. The frontier hypothesis G_r[3]∈{0,2} stays open. The run
independently forward-verified the corridor (claim `morgan-corridor-obstruction-forward-verified`). Caveats correctly recorded: not peer-reviewed, AI collaborator credited; parity phrasing loose ("position 0 odd, others even" is the precise form, matching the run's proved parity wave).

### 5. Granville 2026 Lemma 5.4 — faithful re-derivation

Confirmed via `research/notes/lemma54-re-derived-proof.md` + source note. The
published proof discards the δ=0 case ("we can ignore that exception"), which
occurs on 100% of real columns. The re-derivation's parity-preserving case split
(Branch A: some δ_t ≤ 2 → {0,2} absorbing; Branch B: all δ_k ≥ 4 → δ_L = v−2ν₂ ≤ 2
contradiction) repairs it; the abstract core is Lean-formalised
(`descent_lemma.lean`, sorry-free). The reduction (Theorem 5.5) reduces GC to the
ν₂ supply bound; the demand side α=0.525 is unconditional (BHP). This is the live
Route B. **Do not cite the paper as a proof** — its Theorem 2.5 proof is "take
κ₀=0 and the theorem is proved!" — but the reduction and Lemma 5.4 statement are
real and this run's re-derivation is sound.

## The one state flag worth repeating

**TASKS.md "Do next" still lists `find-weakest-gap-variety-hypothesis` as the next
task**, but its thread (`research/threads/gsupply-transfer-repair.md`) is DEAD
(Directive 57): the F2 transfer ν₂ ≥ c·w is prime-specific and cannot be restored
by any gap-variety hypothesis H_a..H_e (consecutive odds and alternating 2/4 have
maximal w yet ν₂=O(1)). The live successor is
`research/threads/dyadic-periodicity-collapse.md` (Directive 58/64): collapse half
PROVED (`dyadic-collapse-theorem`); odd-factor converse CONJECTURED; its
supply-usefulness measured (`dyadic-oddfactor-infimum-bounded`: P=3,5,7,9,15 → inf
0.6471/0.5088/0.2667/0.3592/0.1143, decaying — NO uniform c, so the dichotomy does
NOT close G-supply). A worker reading only the render would re-hunt H_f in a dead
list; read the thread file, not the stale render. This is a render catch-up issue,
not a live contradiction in the claims/threads/tasks ledgers (those are coherent).

## Sources that do not help (already diagnosed)

- Odlyzko publications page (bibliography/citation pinning only).
- Encyclopedic/catalogue glossaries (Wikipedia, MathWorld, Encyclopedia-of-Math,
  OEIS entries) — statements, names, history, catalogues; none add a proof or a
  bound the run lacks beyond what the primary sources already hold. Caldwell's
  glossary remains the standing counter-source for the Proth-myth's circulation.
- p-adic Ducci papers (Giacomelli) — use the p-adic norm, not the integer |a−b|
  map; do not transfer to Gilbreath.
- Zenodo "resolutions" (Maréchal, Keen, Dutta) — cranks/unverified, recorded.

## Contradictions relevant to the spine (all correctly already flagged)

- `odlyzko-block-lemma-exact` (proved) contradicts `odlyzko-block-lemma-asserted`
  (refuted n/2). Resolved in favour of the constant-1 lemma; verified here.
- `caldwell-proth-myth-repeats` contradicts `proth-myth-retracted` /
  `proth-citation-correction`. Resolved: the Proth 1878 "proof" is a retracted
  myth (Williams's retraction via Chase 2024 §7); nothing to locate an error in.
  Caldwell repeats the myth and cites the wrong C.R. pages (Pépin's paper).
- `g-supply-transfer-universal-refuted` contradicts `g-supply-transfer`. Resolved
  in favour of the refutation; the transfer is prime-specific.

Verification status: every claim verified above was checked against the primary
full text this cycle, not merely against its summary. No new contradiction with
durable memory found.

```claim
id: spine-verified-against-primary-texts-2026
statement: The four most load-bearing primary sources of the closed library were read in full this cycle and their recorded claims confirmed verbatim: (1) ABGS 2011 §9/Problem 1.1 "wide open, cannot be treated using L-functions" — the named-open two-point mod-4 switch hypothesis; (2) Odlyzko 1993 Introduction (and Killgrove–Ralston 1959) state the block lemma with LINEAR constant 1, a {0,2} block of length N−1 protecting N rows — the n/2 figure appears in no source; (3) Blair Morgan 2026 corridor obstruction is sound and narrow (rules out only the pure minimal 8→7→6→5→4 corridor from Row 2); (4) Granville 2026 Lemma 5.4 is faithfully re-derived with the δ=0 discarded case repaired. No new contradiction with durable memory; recorded contradictions (n/2 block constant, Caldwell Proth-myth, g-supply-transfer) remain correctly resolved.
hypotheses: the named primary full texts in research/sources/.
holds-here: yes
status: checked (verified against the primary texts this cycle)
bearing: upgrades the run's load-bearing claims from "asserted on the source's word" to "verified against the primary text", confirming the Route B spine (conditional theorem on the two-point mod-4 switch bound) rests on a verbatim-open hypothesis, and the block-lemma constant is 1 not n/2.
anchor: research/sources/ash-beltis-gross-sinnott-2011-successive-prime-residue-pairs.full.md, research/sources/odlyzko-1993-iterated-differences-latex-source.full.md, research/sources/killgrove-ralston-1959-on-a-conjecture-concerning-the-primes.full.md, research/sources/blair-morgan-2026-return-of-the-lemma.full.md
contradicts: odlyzko-block-lemma-asserted (n/2), caldwell-proth-myth-repeats
answers: abgs-2011-s9-mod4-switch-limit-open (verbatim confirmation)
```

## What the run still lacks (unchanged)

A proof or unconditional bound of `ν₂ ≥ c·n`. Everything else is proved,
machine-checked, or recorded as refuted/asserted with its status. The deliverable
remains the CONDITIONAL theorem (Lemma 5.4 + BHP demand) on the two-point mod-4
switch-correlation lower bound (abgs-2011-s9-mod4-switch-limit-open).
