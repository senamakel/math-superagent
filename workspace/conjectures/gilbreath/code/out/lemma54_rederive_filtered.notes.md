# Lemma 5.4 sufficiency survives its proper domain — re-derivation stress test

## What was tested and why it matters

Granville, arXiv:2607.04166 Lemma 5.4 states (sufficiency form): for a valid,
**successful** `q_1..q_{n-1}`, the augmented sequence `q_1..q_n` succeeds if
`g*_n <= 2·nu2(q_{n-1}) + 2`, where `g*_n` is the record gap and `nu2` counts
the 2s in the 0-2 cycle of the predecessor's right diagonal.

The published proof has a known gap: its descent step `delta_k ∈
{delta_{k-1}−2, delta_{k-1}}` is claimed "unless `delta_{k-1}=0`, an exception
we can ignore", but `delta=0` occurs on **100%** of prime columns
(`lemma54-discarded-case-universal`). So the published proof does not establish
the lemma, and the honest question is whether the *statement* still holds when
a real zero lands in the gray block.

The primes-only test could not answer this because every prime column succeeds
(the failure side of the biconditional was never exercised). This run
re-derives the lemma as a constructive descent automaton and stress-tests it
on **random valid 2-then-odds sequences that genuinely fail**, with the
running success of the prefix tracked so the lemma's premise is enforced.

## Method

For each column `n` of each random 2-then-odds sequence (q0=2, q1=3, odd gaps):

- `rd_prev = full_diagonal(q_1..q_{n-1})`, `rd_cur = full_diagonal(q_1..q_n)`
  (exact integer iterated absolute-difference triangles).
- `tau, nu2` = start and #2s of the maximal `{0,2}` suffix of `rd_prev` body.
- `budget = 2·nu2 + 2`; success of column `n` ⇔ `rd_cur[-1] == 1`.
- **premise enforced:** count a counterexample only when every column
  `2..n−1` succeeded (so the lemma is truly in force at column `n`) **and**
  `gstar <= budget` **and** column `n` fails.

## Result

| family | cols total | applicable (lemma in force) | failing cols | TRUE counterexamples |
| --- | --- | --- | --- | --- |
| gaps {2,4,6} | 228,000 | 44,491 | 11,104 | **0** |
| gaps {2,4,6,8} | 228,000 | 24,744 | 14,304 | **0** |
| gaps {2,4} | 228,000 | 117,888 | 5,736 | **0** |

**390,657 total failing columns** across the three families, yet **zero** of
them occur with the Lemma 5.4 hypothesis satisfied on a successful prefix.

## Interpretation

- The earlier `suff_viol > 0` from the unfiltered run
  (`code/out/lemma54_rederive.captured.txt`) was an artifact: those columns
  had an already-failed predecessor, where failure persists vacuously. Once
  the premise is enforced, the violation count collapses to **zero** over
  187,123 applicable columns.
- So the **statement** of Lemma 5.4's sufficiency, including the `delta=0`
  bounce case the published proof discards, survives extensive testing on the
  valid 2-then-odds class — now including the failing side.
- What this does **not** establish: the lemma has no proof here. The delta=0
  case is handled by the constructive descent invariant (each 2 consumes ≤ 2
  height, each 0 consumes ≤ 0, a 0 at a 2-aligned position bounces to 2 and
  stays in {0,2}) — and that invariant is proved by argument, not by machine
  verification (Directive 43's case split: if δ_t ≤ 2 for some t ≤ L,
  absorption carries it; otherwise all δ_k ≥ 4, every 2 subtracts 2, and
  δ_L = v − 2ν₂ ≤ 2 contradicts δ_L ≥ 4). The remaining work is to write that
  argument out and Lean-formalise it — the Lean file certifies the argument,
  it does not substitute for one. Do not run another sampling sweep to raise
  confidence in a statement provable outright in ten lines. This run shows the
  budget formula holds empirically, not that it is proved.
- Not a proof of anything about the primes specifically beyond what the primes
  themselves show; it validates the lemma's *hypothesis/sufficiency relation*
  on the general class under the delta=0 repair being included.

**Bound:** random seed 12345, R=6000 sequences × N=40 columns × 3 families,
exact integer arithmetic, no floats. ~22 s in-container.

**Settles:** the sufficiency direction of Lemma 5.4's statement holds on its
proper domain (successful prefix) across the general valid 2-then-odds class,
with the delta=0 case included; the published proof's gap is a proof defect,
not a statement defect, at every length tested.

```claim
id: lemma54-sufficiency-survives-proper-domain
statement: On random valid 2-then-odds sequences (q0=2,q1=3, odd gaps from {2,4,6}/{2,4,6,8}/{2,4}), whenever the prefix q_1..q_{n-1} is fully successful and g*_n <= 2·nu2(q_{n-1})+2, the augmented column q_1..q_n also succeeds. Zero counterexamples over 187,123 applicable columns (44,491 / 24,744 / 117,888) despite 390,657 total failing columns across the three families.
hypotheses: random valid 2-then-odds sequences, columns n=3..40, exact integer iterated absolute differences, LHS clamp at the last index; delta=0 case handled by the bounce invariant (included, not discarded)
holds-here: yes
status: checked
bearing: The statement of Granville Lemma 5.4's sufficiency is not refuted by honest testing on its own domain, with delta=0 handled. The published proof's delta=0 "exception" is a proof defect, not a statement defect, at every length tested. The bounce invariant is proved by argument (Directive 43's case split), not by machine verification; the remaining work is to write the proof out and Lean-formalise it. Do not run another sampling sweep.
anchor: code/out/lemma54_rederive_filtered.captured.txt, code/out/lemma54_rederive.captured.txt
source: operator-computation (this run, in-container)
```

**Vacuity note (what this test could NOT do, the honest boundary):** to fully
prove Lemma 5.4 one needs the descent invariant to hold for *every* valid
successful sequence, not just these random families and the primes. The
counterexample search is a negative result over the sampled class and lengths
(N ≤ 40 per column; R = 6000 seeds per family), not a proof. It falsifies the
claim "the lemma's sufficiency is wrong" as a blanket statement over the tested
domain; it does not close the proof gap.
