# Raz (2017) counterexample . abundance half — manual verification

Claim `raz-reimers-condition-insufficient` (anchor:
`research/sources/raz-note-union-closed-2017.full.md`, source URL
https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i3p53/pdf/).

The 11 sets on universe [8]:

    A0    {1,2,3,4,5,6,7,8}
    A1    {2,4,6,7,8}
    A2    {1,3,5,8}
    A3    {1,4,7,8}
    A4    {2,3,5,6}
    A5    {1,3,7}
    A6    {2,3,5}
    A7    {2,4,6}
    A8    {4,5,6,7}
    B1,2  {8}
    B3,4  {1}

## Per-element membership counts (manual, from the list above)

- 1: A0, A2, A3, A5, B3,4  → 5
- 2: A0, A1, A4, A6, A7    → 5
- 3: A0, A2, A4, A5, A6    → 5
- 4: A0, A1, A3, A7, A8    → 5
- 5: A0, A2, A4, A6, A8    → 5
- 6: A0, A1, A4, A7, A8    → 5
- 7: A0, A1, A3, A5, A8    → 5
- 8: A0, A1, A2, A3, B1,2  → 5

Every element is in exactly **5 of 11** sets. |A|/2 = 5.5, so an abundant
element would need ≥ 6. **None is abundant.** Confirms the abundance half of
the claim.

## Negative control

The family is NOT union-closed: e.g. A5 ∪ A6 = {1,3,7}∪{2,3,5} = {1,2,3,5,7},
which is none of the 11 sets. So this is a *Reimer-Condition-1 family without an
abundant element* — it is a counterexample to Balla/Gowers' Conjecture 3, NOT a
counterexample to Frankl's conjecture. It therefore does not contradict UC; it
is a negative control for any proof that uses only Reimer's averaging structure.

## Status

- Abundance half (`each element in <= 5 of 11`): **verified by hand** here;
  the oracle stub `code/out/verify_raz_counterexample.py` and crosscheck
  `code/out/verify/run_raz_crosscheck.py` are ready for a compute-capable pass
  to execute mechanically.
- Condition-1 filter/bijection half: **asserted-by-source** (full explicit
  bijection in the paper's appendix; not re-derived here).

## Claim block

```claim
id: raz-reimers-condition-insufficient-verified
statement: Reimer's Condition (a filter F ⊆ 2^[n] with a bijection A↦F_A,
  A⊆F_A, disjoint intervals [A,F_A]) does NOT imply an abundant element:
  the explicit family on [8] with |A|=11 has every element in exactly 5 of
  11 sets, none abundant (needs ≥6); and the family is NOT union-closed, so
  this is a counterexample only to Balla/Gowers' Conjecture 3, not to UC.
hypotheses: the 11 explicit sets on [8]; abundance = an element in ≥|A|/2=5.5
  sets i.e. ≥6.
holds-here: yes
status: checked (abundance half verified by hand from the explicit set list in
  the source; the not-union-closed negative control checked by A5∪A6 example)
bearing: negative control: any UC proof using only Reimer's averaging structure
  is provably insufficient. Parallels the entropy (3−√5)/2 barrier for the iid
  method — each successful structural relaxation has its own obstruction.
anchor: code/out/verify/raz_counterexample_verified.md; research/sources/raz-note-union-closed-2017.full.md
contradicts: (none — consistent with lu-raz-reimer-conditions-dont-force which
  generalises it)
answers: raz-reimer-condition-insufficient (strengthens its status from
  asserted to checked on the abundance half)
```

## Files

- `code/out/verify_raz_counterexample.py` — oracle stub (direct abundance route)
- `code/out/verify/run_raz_crosscheck.py` — independent counts + not-UC negative
  control
- `code/out/verify/run_raz_full.py`, `code/out/run_raz_full.sh` — driver for a
  compute-capable pass
