# Spence, "Auditing Two Claimed Proofs of Frankl's Conjecture and Structural Reductions for Minimal Counterexamples" (2026, preprint)

Source: https://zenodo.org/records/20800102 (frankl-conjecture-audit.pdf, 485.2 kB, CC BY 4.0)
Author: Nelson Daniel Spence, Project Navi. Preprint, June 22, 2026. Does NOT claim a proof of UC.

## What this paper is

An *audit* of two recent claimed proofs of Frankl's conjecture — it refutes the
proof *mechanisms* on small explicit objects, not the conjecture itself — plus
a constructive reduction for minimum-cardinality counterexamples. This is the
minimal-counterexample-structural line the run's ROOT.md and the
`abundance-profile` thread are thinnest on, and the paper is fresh (2026) with
theses that build directly on Bouchard's lattice formulation (arXiv:2503.00277,
already in this library).

## Headline results

1. **Prop 3.1 / Cor 3.2 — Heavy Column Theorem false as stated.** The 5×4 matrix
   with rows {0000, 0011, 0101, 1010, 1100} has distinct rows, distinct columns,
   no all-zero column, and every column exactly two ones (so NO heavy column, m=5
   needs ≥3). Yet the recursive algorithm A2 of Abdurakhmanov returns True on it,
   refuting the Heavy Column Theorem used in that claimed proof. **Remark 3.3
   is the crucial caveat**: the row set is NOT closed under componentwise
   disjunction (not a union-closed family), so this does *not* refute a
   strengthened theorem restricted to union-closed row sets — that stronger
   statement "contains essentially the unresolved combinatorial content".
   Prop 3.4: 5 rows is minimal for such an example.

2. **Prop 4.1 — Schrader's discarding-set upper bound fails.** On the
   intersection-closed family {∅,{1},{2},{3}} (N=[3]), the recursive quantity
   t0=4, t1=4, t2=4−2=2, t3=2−1−1=0, but |F3|=1; so t3 ≥ |F3| fails. Remark 4.2
   locates the accounting failure: t_{i−1} is only a numerical upper bound from
   the previous coordinate; subtracting |H| requires the newly excluded sets to
   lie inside a common candidate universe, and disjointness alone does not give
   that containment.

3. **Minimum-counterexample structure (Section 6) — the genuinely valuable
   part, all elementary proofs:**
   - Prop 6.2: a minimum-cardinality counterexample may be normalized to have
     ∅ as a member.
   - **Thm 6.3: a minimum-cardinality counterexample has ODD cardinality
     |F| = 2k+1**, and every element has frequency ≤ k. (Proof: m=2k, delete an
     inclusion-minimal nonempty member A (removable by Lemma 6.1), apply
     minimality to the smaller family, contradiction.)
   - **Thm 6.4: every admissibly-removable member A is "tight-witnessed":**
     ∃ x_A ∉ A with d_F(x_A) = k. Every inclusion-minimal nonempty member omits
     a tight element.
   - **Thm 6.7 (lattice form, strengthens Bouchard [4, Cor 2.11]):** in a
     minimum lattice counterexample (|L| = 2k+1), any two distinct
     meet-irreducibles m1,m2 have a common *lattice-tight* join-irreducible
     j ≤ m1, m2 below them, where lattice-tight means |(↑j)_L| = k+1. Proof
     by deleting {m1,m2} (valid: deleting meet-irreducibles from a finite
     lattice leaves a lattice) and showing the subposet is a smaller
     counterexample.
   - Cor 7.1 (exact-three case): if the tight join-irreducibles are exactly
     {a,b,c}, every meet-irreducible has |S(m)| ≥ 2 and all three two-element
     traces {a,b},{a,c},{b,c} each occur.

## Relation to this run's library

- **Extends** ROOT.md's minimal-counterexample structure: the prior library
  bound was `|F| ≥ 4q−1 ≥ 51` (Roberts–Simpson / Hu, with q≥13); Spence adds
  *parity* (|F| odd) and a *tight-witness-per-deletion* property — different
  axes, both compatible. ROOT's `|F| ≥ 51` says nothing about parity; Spence's
  odd-cardinality + ≤k-frequency is a genuinely new structurally-imposed
  constraint.
- **Builds on** Bouchard (arXiv:2503.00277, already held) — Thm 6.7 strengthens
  Bouchard's Cor 2.11 from "a common join-irreducible" to "a common *tight*
  join-irreducible".
- **Cites** Hachimori–Kashiwabara [9] (Graphs Combin. 40:130, 2024) as the
  source of the 2-transversal configuration to be excluded; HK is already held
  (`hachimori-kashiwabara-averaging-ideal-families-lean-2025`).
- The frontier added the two claimed-proof sources it audits: Abdurakhmanov
  (arXiv:2601.18450; HAL hal-05482771) and Schrader (arXiv:2501.03302) — these
  are the failed-proof mechanism references.

## Caveats / what is NOT established here

- This does NOT refute Frankl's conjecture; it refutes two proof mechanisms.
- The matrix of Prop 3.1 is not union-closed, so it does not attack the
  union-closed version of the heavy-column idea.
- The structural results (Thm 6.3, 6.4, 6.7) assume a minimum-cardinality
  counterexample EXISTS and derive necessary conditions on it — they are
  implications toward a contradiction, not unconditional theorems, and the
  "exact-three finishing step" (Section 7) is explicitly NOT proved here.

## Verification status

The finite claims in Prop 3.1 and Prop 4.1 are directly checkable with the
oracle (`code/lib/uc.py`); `code/out/spence_verify.py` reproduces Prop 3.1's
column counts (every column exactly 2 ones) and non-union-closure, and Prop 4.1's
t-values. The paper ships `verify_counterexamples.py` (Python stdlib). The paper's
own §5 states the arguments do not depend on trusting a search heuristic.
Structural lemmas are elementary (short proofs reproduced above verbatim) and
are asserted-by-source in this library until a theorem-prover run formalises them.

```claim
id: spence-minimum-counterexample-odd
statement: If Frankl's conjecture is false and F is a counterexample with the
  minimum possible number of members, then |F| is odd (|F| = 2k+1), every element
  has frequency ≤ k, and every admissibly-removable member A omits a "tight"
  element x_A ∉ A with d_F(x_A) = k (Thm 6.3, 6.4). In the lattice form (|L|=2k+1),
  any two distinct meet-irreducibles share a common "lattice-tight" join-irreducible
  j below both, i.e. |(↑j)_L| = k+1 (Thm 6.7).
hypotheses: F (resp. L) is a minimum-cardinality counterexample to Frankl's
  conjecture having the fewest members; harmless normalization to ∅ ∈ F (Prop 6.2).
holds-here: true (these are necessary conditions on a hypothesized minimal counterexample,
  not unconditional theorems; they are forward implications toward contradiction)
status: asserted-by-source (Spence 2026 preprint, elementary proofs reproduced in
  the full text; not yet formalised in a theorem prover)
bearing: NEW structural constraint on a minimal counterexample. ROOT's |F| ≥ 4q−1 ≥ 51
  (Hu) says nothing about parity; Spence adds that |F| must be odd and that every
  single-member deletion exposes a tight element. Thm 6.7 strengthens Bouchard's
  Cor 2.11 from "a common join-irreducible" to "a common TIGHT join-irreducible".
  This is ammunition for the abundance-profile and minimal-counterexample threads.
  The exact-three incidence structure (Cor 7.1) reduces that case to a rigid
  triangular incidence shadow, with the finishing step explicitly unproved.
anchor: research/sources/spence-auditing-claimed-proofs-minimal-counterexamples-2026.full.md
falsifies: If a minimum-cardinality counterexample with an even number of members
  is exhibited, or one whose removable members never omit a frequency-k element,
  Thm 6.3/6.4 are refuted.
```
