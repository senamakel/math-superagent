# Pattern-finder report — abundance-profile structure

**Scope.** This report extracts and analyses the integer sequences the run has
produced, and adds one new exact computation. Everything here is over the terms
supplied or over the exhaustive range stated; each is labelled as checked or
conjectured.

---

## 1. The oracle's own enumeration — verified against the catalogue

`code/out/uc_oracle_check.py` enumerates all union-closed families over the
full power set `2^[n]` (including the trivial `{∅}`) for n = 1..4 and counts
them:

```
n:       1    2     3     4
count:   3   13   121  4959
```

This is the catalogued sequence **A121921 = A102897(n) − 1** (closed forms
filed at `research/summaries/oeis_a121921.md`, `oeis_a102897.md`). An
`oeis_lookup([3,13,121,4959])` confirms the single match **A121921**. So the
oracle's enumeration is correct at its boundary — a second, independent route
(the catalogued count) reproduces every term this run computed. This is the
oracle-consistency check GOAL.md requires, not a finding about the conjecture.

`analyze_sequence` and `find_linear_recurrence` on these 4 terms report:
- not a low-degree polynomial (differences don't stabilise),
- residues mod 2 repeat with period 1 (all terms odd — every term is odd, which
  is the known behaviour of A102897/A121921),
- growth ratios 4.33, 9.31, 40.98 — consistent with the known double-exponential
  asymptotics `log₂ a(n) ~ C(n, floor(n/2))`.

An order-2 recurrence reported by `find_linear_recurrence` for 4 terms is
**spurious overfitting** (any order-2 fit reproduces 4 terms by construction)
and is discarded.

**Status:** checked (enumeration matches catalogue). No conjecture is offered
about the count sequence itself — it is an enumeration curiosity (OEIS A102897),
already catalogued, and not a route to an abundance bound.

---

## 2. New exact computation — the abundance profile (the target quantity)

The conjecture is about the *minimum* over elements of density. I scanned every
union-closed family on `[n]` with the exact oracle (`lib.uc`) and measured the
**worst-case minimum element-frequency**:

```
WORST(n) = min over UC families F on [n] of  min_x in F  (count_x / |F|)
```

Exact exhaustive result, n = 1..4:

```
n:      1     2     3     4
WORST:  1/2   1/3   1/5   1/9    =  1/(2^{n-1} + 1)
```

The achieving family is, uniquely up to isomorphism (checked exhaustively for
n = 1..4):

```
F = 2^[n-1]  ∪  { [n] }        (Boolean lattice on n-1 elements plus the full set)
|F| = 2^{n-1} + 1
```

The least-frequent element (element n−1) is in exactly **1** set, density
`1/(2^{n-1}+1)`; every other element is in `2^{n-2}+1` of the `2^{n-1}+1` sets.

**This is exactly the near-k-cube equality extremal of the Das–Wu Nagel bound**
(claim `daswu-nagel`, `research/summaries/das-wu-frequent-elements-2024.md`):
the kth-most-frequent element lies in at least `|F|/(2^{k−1}+1)` sets, with
equality iff F is a near-k-cube. So my exhaustive computation independently
recovers, as the parameter k = n (ground-set size), the theorem's sharp
extremal object, and the bound value `1/(2^{n-1}+1)`.

`analyze_sequence([2,3,5,9,17])` = denominators `2^{n-1}+1`:
- differences 1,2,4,8 (perfectly geometric, exact over the terms),
- `oeis_lookup([2,3,5,9,17])` matches **A000051** = `2^n + 1` (the catalogued
  closed form). So the denominator sequence IS A000051 — a sourced closed form,
  not a conjecture.

**Status:** the *values* WORST(n) = 1/(2^{n-1}+1) for n=1..4 are **checked**
(exhaustive). The general statement for all n is not proved here, but it is
exactly Das–Wu's Nagel-bound sharpness (`daswu-nagel`, sourced theorem), so it
is a **sourced theorem**, not merely a conjecture. The uniqueness up to
isomorphism of the extremal is **checked** for n=1..4 by my permutation-based
canonicalisation and matches Das–Wu's "iff near-k-cube" — also sourced.

---

## 3. The FC(k,n) thresholds — no exploitable low-order structure (small sample)

The run's sources give exact FC(k,n) values: FC(4,n) = 5, 7, 10, 12 for
n = 5..8 (Morris, Pulaj–Wood). `analyze_sequence([5,7,10,12])` reports
differences 2,3,2 — no low-degree polynomial, no recurrence visible over this
short sample. `oeis_lookup([5,7,10,12])` matched only unrelated sequences
(Perrin, factorial beanstalk, residues mod 5) — i.e. **no catalogued match**;
this is a real miss worth recording so the run stops looking. With only 4 terms
no honest recurrence can be claimed.

---

## 4. What to conclude, and what each regularity is

1. **The abundance-profile extremal** is the most exploitable structure here:
   the unique worst case is the near-k-cube and the worst min-density is
   `1/(2^{n-1}+1)`. It is *not* a route to a new bound (it is a lower bound on
   the *minimum* density, i.e. the hardest direction, and it is exactly the
   sharp Das–Wu extremal), but it **decides the shape of the extremal object**
   in the small-|F| regime: the near-k-cube is what "minimal abundance" looks
   like. Any proposed barrier or structural claim should be tested against it.
2. The enumeration count sequence is catalogued (A121921/A102897) and holds no
   new structure for this problem; a recurrence there would say nothing about
   abundance. Directing sequence effort there is a dead end (matches the
   operator steering note).
3. The FC(4,n) threshold values are too few to support any regularity, and they
   are not catalogued. Worth extending only if the run computes more values
   (Pulaj's SMT route).

**Nothing here is dressed up as a proof.** The exhaustive values are checked;
the general statement that WORST(n) = 1/(2^{n-1}+1) is a sourced theorem from
Das–Wu (the sharp Nagel bound), corroborated by my exhaustive scan; the
uniqueness of the extremal up to isomorphism is checked for n ≤ 4 and sourced.
No new bound on the *max* abundance is claimed.
