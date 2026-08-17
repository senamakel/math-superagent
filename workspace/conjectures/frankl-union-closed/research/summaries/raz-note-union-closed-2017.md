<!-- source: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i3p53/pdf/ -->

# Raz, "Note on the union-closed sets conjecture" (2017) — summary

**Source URL:** https://www.combinatorics.org/ojs/index.php/eljc/article/download/v24i3p53/pdf/
**Full text:** `research/sources/raz-note-union-closed-2017.full.md`
**Bibliographic:** Electron. J. Combin. 24(3) (2017), #P3.53. DOI 10.37236/6989.

## What this paper is

Answers a question raised in Gowers' Polymath 11 project: does "Reimer's
Condition" (the structural condition Reimer proved every union-closed family
satisfies, and which implies his average-set-size bound) by itself force an
element in at least half the sets? **No.**

## Reimer's framework, made precise

- **Theorem 1 (Reimer, restated):** If A ⊆ 2^[n] is union-closed then the
  average set size ∑|A|/|A| ≥ (1/2)log₂|A|.
- **Condition 1 (Reimer's condition):** There exists a filter F ⊆ 2^[n] and a
  bijection A ↦ F_A from A to F with (i) A ⊆ F_A for all A, and (ii) for
  distinct A,B, [A,F_A] ∩ [B,F_B] = ∅.
  Reimer: every union-closed family satisfies Condition 1, and Condition 1
  implies Theorem 1.
- **Conjecture 3 (Balla/Gowers):** Condition 1 alone implies an element in at
  least half the sets. This note disproves it.

## The counterexample

- Universe [8], |A| = 11. The filter F has all sets of size ≥ n−1 plus
  [8]\{1,2} and [8]\{3,4}, so |F| = |A| = n+3 = 11.
- A consists of A0 = [8]; A1..A8 (each missing some elements); B1,2 = {8};
  B3,4 = {1}. Each element appears in at most 5 = |A|/2 − 0.5 sets (i.e.,
  ≤ n/2 + 1 = 5), so **no element is in more than half** the sets.
- The proof that n ≥ 8 for any such counterexample (when |A\A′| = 2) uses a
  digraph/tournament argument: D on [k] must contain a tournament; each B_{i,j}
  forces an extra out-degree; combining out-degree bounds forces n ≥ 8 (and
  n ≥ 13 for the odd case).
- **Raz also shows the minimality:** no counterexample exists for n < 8.

## How it relates to this library

The Lu–Raz 2024 note (arXiv:2405.10639, `lu-raz-reimer-note-2024.full.md`)
generalizes this: infinitely many families satisfying Reimer's condition with
any fixed lower bound on member-set size, all failing the abundance condition.
Raz's note is the primary source for the n=8, |S|=11 minimal counterexample
to the P3.53 Conjecture 3.

## Claim blocks

```claim
id: raz-reimers-condition-insufficient
statement: Reimer's Condition (a filter F ⊆ 2^[n] with a bijection A↦F_A
  satisfying A ⊆ F_A and disjoint intervals [A,F_A]) does NOT imply the
  existence of an element in at least half the sets: there is an explicit
  counterexample on universe [8] with |A| = 11, each element in at most 5 sets,
  and no counterexample exists for n < 8.
hypotheses: A ⊆ 2^[8] satisfies Reimer's Condition; |A| = 11; abundance means
  an element in ≥ |A|/2 = 5.5 sets, i.e., ≥ 6.
holds-here: yes (this is a statement about the structural relaxation, not about
  union-closed families themselves)
status: asserted-by-source (published EJC 24(3) #P3.53, 2017)
bearing: Sets a precise boundary of the averaging/Reimer-condition method: the
  condition that makes Reimer's average-set-size theorem work is NOT enough for
  the abundance conclusion. This is a sibling of the entropy barrier row: each
  successful structural relaxation has its own obstruction.
anchor: research/sources/raz-note-union-closed-2017.full.md
falsifies: A smaller (n<8) or larger-density counterexample to Balla's
  Conjecture 3, or an error in the explicit family's abundance counts.
```