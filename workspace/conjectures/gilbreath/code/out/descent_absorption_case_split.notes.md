# Directive 43 — descent/absorption lemma, corrected case-split proof: exhaustive machine check

## Status

`id: lemma54-descent-absorption-case-split-L18`
`status: checked` (exact-integer exhaustive verification, not a proof)
`holds-here: yes`
`bearing:` Route B (Granville ν_2). This is the machine check of the CORRECTED
case-split proof of the descent/absorption lemma (Granville Lemma 5.4 core),
extending the prior L=1..16 check (`code/out/lemma54_descent_check.captured.txt`,
claim `lemma54-re-derived-proof`) to L=18 and adding explicit verification of the
case-split structure that repairs the flagged algebra defect.

## The defect being repaired

The published/earlier proof line "after consuming the ν₂ twos, δ = v − 2ν₂" is
**false on bounce trajectories**: with v = 0, ε = (2,2,2), the orbit is
0 → 2 → 0 → 2 (x_L = 2 ∈ {0,2}, correct conclusion) while v − 2ν₂ = −6.
The subtraction "each 2 contributes −2" fails when δ = 0 and ε = 2 (the step is
+2, a bounce into {0,2}). This was flagged in
`research/notes/lemma54-re-derived-proof.md`.

**Corrected case split (Directive 43):**
- **Branch 1 — absorption:** if some x_t ≤ 2 for t ∈ 1..L, then x_t ∈ {0,2}
  (parity: every x_s even; nonnegativity) and {0,2} is closed under the step
  (|0−0|=0, |0−2|=2, |2−0|=2, |2−2|=0), so x_L ∈ {0,2}. Bounces live here.
- **Branch 2 — descent:** else every x_s ≥ 4; each c_s=2 subtracts exactly 2
  (|x−2| = x−2 for x ≥ 2, no bounce possible since x ≥ 4), each c_s=0 passes
  through, so x_L = v − 2ν₂. And x_L ≥ 4 ⟺ v − 2ν₂ ≥ 4 ⟺ v > 2ν₂+2.
- **Partition:** branch 1 ⟺ v ≤ 2ν₂+2 (if v ≤ 2ν₂+2 and we were in branch 2,
  x_L = v−2ν₂ ≤ 2 contradicts x_L ≥ 4; if v > 2ν₂+2 and we were in branch 1,
  absorption would give x_L ∈ {0,2} contradicting the necessity direction
  below), branch 2 ⟺ v > 2ν₂+2.
- **Necessity (the "only if" of the biconditional):** v > 2ν₂+2 forces branch 2
  (contrapositive of branch-1-implies-v≤budget), giving x_L = v−2ν₂ ≥ 4 ∉ {0,2}.

Nothing is discarded: the δ=0 "exception" Granville's published proof drops is
branch 1's bounce, the main case here.

## Domain and counts (exact integers, no floats)

- L = 1..18; ALL 2^L patterns of {0,2}^L per L; **524,286 patterns**.
- Even v in [0, 2L+8] for each L (L+5 even values per pattern);
  **11,534,328 (pattern, v) pairs**.
- Inner |a−b| steps: Σ 2^L·(L+5)·L = 197,132,292.
- Branch partition over all pairs: branch 1 (absorption) 5,505,021,
  branch 2 (descent) 6,029,307; sum = 11,534,328 ✓.

## Results — ALL ZERO VIOLATIONS

| Check | Violations |
| --- | --- |
| (a) x_L ∈ {0,2} ⟺ v ≤ 2ν₂+2, suff direction | 0 |
| (a) x_L ∈ {0,2} ⟺ v ≤ 2ν₂+2, nec direction | 0 |
| (b) v > 2ν₂+2 ⟹ x_L == v − 2ν₂ AND x_L ≥ 4 | 0 |
| (0) every x_s even | 0 |
| (0) {0,2} closed under the step (once in, never out) | 0 |
| (c) branch 1: min x_s ≤ 2 ⟹ x_L ∈ {0,2} | 0 |
| (c) branch 2: all x_s ≥ 4 ⟹ every step exact (−2 on 2, 0 on 0) | 0 |
| (c) branch 2: x_L == v − 2ν₂ | 0 |
| (c) partition (branch1 ⟺ v≤budget, branch2 ⟺ v>budget) | 0 |
| (d) v = 2ν₂+2 ⟹ x_L ∈ {0,2} | 0 |
| (d) v = 2ν₂+2 ⟹ x_L == 2 exactly (not 0) | 0 (all 524,286 patterns give exactly 2) |
| (d) v = 2ν₂+4 ⟹ x_L == 4 exactly | 0 |

Largest L reached: **18**. Total pairs: **11,534,328**.

## Independent re-derivation

A second, structurally different route (halved units: e = c/2 ∈ {0,1},
d_s = |d_{s−1} − e_s|, verifying x_s == 2·d_s at every step plus claims (a),(b)
in the halved form) on L ∈ {1,2,3,4,5,6,10,18}: 6,045,944 (pattern,v) pairs,
**0 mismatches** (assert-checked, would abort on any failure).

## Hand-verified boundary cases

- v=0, c=(2,2,2): x_L = 2 ∈ {0,2} (bounce trajectory; old algebra v−2ν₂ = −6
  invalid here — exactly the case the corrected split handles via branch 1).
- v=6, c=(2,2): x_L = 2 (budget 2ν₂+2 = 6 is tight, lands inside {0,2}).
- v=8, c=(2,2): x_L = 4 = v−2ν₂, ≥ 4 (failure regime, exact value).
- Parity sanity: all even v stay even (|even−even| = even), odd v is out of
  domain (|odd−even| = odd would never reach {0,2} — the located parity
  boundary of the published statement; real prime diagonals are even-valued).

## Proof status

This is **verification, not a proof** — the proof must come from the case-split
argument written out (as summarised above), which every premise and conclusion
of has now been machine-checked over the full finite domain L ≤ 18. The
remaining work to close the flagged proof defect at the "proved" level is the
written repair in `research/notes/lemma54-re-derived-proof.md` and a Lean
formalisation (TASKS.md Directive 44 item 1).

```claim
id: lemma54-descent-absorption-case-split-L18
statement: Exhaustive exact-integer check of the descent/absorption lemma (Granville Lemma 5.4 core) under the CORRECTED case-split proof, L=1..18, all 524,286 patterns c in {0,2}^L, all 11,534,328 even (pattern,v) pairs v in [0,2L+8], x_0=v, x_s=|x_{s-1}-c_s|. ZERO violations of: (a) x_L in {0,2} <=> v <= 2*nu2+2 (both directions), (b) v > 2*nu2+2 => x_L == v-2*nu2 >= 4, (0) every x_s even and {0,2} closed under the step, (c) the corrected case-split partition (branch 1 absorption: min x_s <= 2 <=> v <= budget; branch 2 descent: all x_s >= 4 <=> v > budget, with every step exact -2-on-2/0-on-0 and x_L == v-2*nu2 in branch 2), (d) tight boundary v=2*nu2+2 -> x_L == 2 exactly and v=2*nu2+4 -> x_L == 4 exactly for every pattern. The old proof algebra x_L = v-2*nu2 is false on bounce trajectories (v=0, c=(2,2,2): orbit 0->2->0->2 but v-2*nu2 = -6); the corrected case split never applies the subtraction outside branch 2. Verification NOT proof; the proof is the case-split argument now fully machine-instantiated. Independent halved-unit re-derivation (x_s == 2*d_s) on L in {1,2,3,4,5,6,10,18}: 6,045,944 pairs, 0 mismatches.
hypotheses: c in {0,2}^L; v even in [0,2L+8]; exact integer |a-b|; exhaustive over the full finite domain (no sampling); oracle: definitional simulation
holds-here: yes (real prime right-diagonals are even-valued)
status: checked
bearing: Route B (Granville nu_2). Repairs the algebra defect flagged in lemma54-re-derived-proof (Directive 43/44): the corrected case-split proof is machine-verified over the extended domain L<=18; the written proof + Lean formalisation remain (Directive 44 item 1).
anchor: code/gap_analysis/descent_absorption_case_split.py, code/out/descent_absorption_case_split.captured.txt
answers: lemma54-re-derived-proof (proof-defect repair, machine-checked leg)
```

## How to reproduce

```
cd /workspace
timeout 540 python3 code/gap_analysis/descent_absorption_case_split.py \
    2>&1 | tee code/out/descent_absorption_case_split.captured.txt
# expect: RESULT: ALL CHECKS PASSED (total pairs 11534328, largest L 18), EXIT 0
```
