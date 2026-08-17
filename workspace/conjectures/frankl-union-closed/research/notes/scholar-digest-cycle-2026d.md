# Scholar digest — five new primary sources (librarian cycle 2026d)

The librarian landed five primary sources and filed their claim blocks. This
note records what the scholar verified, what conflicts with recalled memory, and
the durable findings (remember_memory is down; fold into Cognee when it recovers).

## Verification performed this pass

### Raz 2017 — hand-checked, confirmed
`raz-reimers-condition-insufficient` is **hand-confirmed** on the abundance half:
explicit family on [8], |A|=11, sets
A0=[8], A1={2,4,6,7,8}, A2={1,3,5,8}, A3={1,4,7,8}, A4={2,3,5,6},
A5={1,3,7}, A6={2,3,5}, A7={2,4,6}, A8={4,5,6,7}, B1,2={8}, B3,4={1}.
Every element appears in **exactly 5 of 11** sets; |A|/2=5.5, so none is
abundant. The Condition-1 filter/bijection half remains asserted-by-source
(full bijection in the paper's appendix; not re-derived here).
`code/out/verify_raz_counterexample.py` is the oracle stub for a later pass to
execute and confirm mechanically.

### Czédli 2009 — confirmed against full text
Theorem 1 (decoded from the OCR'd PDF): F union-closed over m-element A, m≥3,
n=|F| ≥ 2^m − 2^(m/2) (F "large") satisfies the **averaged** Frankl property
Σ_{a∈A}(n − 2·#{B∈F: a∈B}) ≤ 0, hence UC. Theorem 2 is the lattice version
(Σ_{a∈J(L)}(|L|−2|↑a|) ≤ 0). The paper **explicitly states** the averaged
property fails for some union-closed families — confirming the on-disk
`cms-averaged-frankl-wrong` claim and delimiting the averaging method.

### Marković 2007 — confirmed
UC holds for |⋃F| ≤ 10; multi-weight (several Poonen weights simultaneously)
method; author states it will "most probably not prove the whole conjecture."

## Contradictions / tensions with recalled memory

- **None found.** The five sources contradict no recalled-memory row. Raz 2017
  *reinforces* the Reimer-condition closure already on disk (lu-raz-reimer-note
  generalises it). Czédli 2009 *reinforces* the CMS averaging-limits claim. All
  are consistent with the run's established rows and its negative controls
  (union-closure must be used; the averaging relaxation is insufficient).

## Bearing on the run

- **Raz's counterexample is a concrete negative control**: any proof of UC that
  only uses Reimer's Condition 1 (the structural condition behind the
  average-set-size theorem) is provably insufficient. This is not a barrier to
  UC itself, but it is the exact obstruction any averaging-leaning line must
  beat, paralleling the entropy barrier (3−√5)/2 for the iid method.
- **Czédli large-family threshold** |F| ≥ 2^m − 2^(m/2) is a settled class;
  a minimal counterexample has |F| < 2^(n−1) (Karpas) as already recorded.
- **Marković / Pulaj–Raymond–Theis / Moghaddas** are background: they confirm
  the small-universe ladder, the IP viewpoint, and the matrix-relaxation
  pattern respectively, none of which moves the constant record.

## Still missing (unchanged)

- **Reimer's own primary proof** that union-closure implies Condition 1 is not
  primary-held (paywalled, no open copy). Raz restates both directions (UC ⇒
  Condition 1 ⇒ average-set-size bound) but does not reproduce Reimer's first
  implication. Gap recorded in `research/notes/librarian-cycle-2026d-...`.
- **Hachimori–Kashiwabara 2024** minimality-concepts: paywalled, no arXiv,
  tracked as `hak-minimality-concepts-2024-paywalled-gap`.

## Durable findings to fold into Cognee on recovery

1. Raz 2017 counterexample: Reimer's Condition 1 does not imply an abundant
   element; explicit [8], |A|=11, every element in 5 of 11 sets; verified.
2. Czédli 2009: averaged Frankl property holds for large families
   |F| ≥ 2^m − 2^(m/2), and fails for some small (non-large) families.
3. Marković 2007: UC for |⋃F| ≤ 10 by a multi-weight method the author
   himself judged unable to prove the full conjecture.
