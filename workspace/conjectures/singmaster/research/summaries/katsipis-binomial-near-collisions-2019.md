# N. Katsipis, "Diophantine equations coming from binomial near-collisions" (arXiv:1901.03841, 2019)

Source: https://arxiv.org/abs/1901.03841
Full text: `research/sources/katsipis-binomial-near-collisions-2019.full.md`

## What it is

The 2019 preprint (Katsipis, University of Crete) that resolved the remaining
cases of the near-collision equation C(n,k) = C(m,l) + d with d = 1 for
(k,l) = (8,2), and (k,l),(l,k) = (3,6) for various d. It established the
Blokhuis–Brouwer–de Weger 2017 conjecture that (6,3), (3,6), (8,2) have no
d=1 near-collisions.

## Results

- Solves C(m,l) - C(n,k) = d for (k,l) = (3,6) (various d) and (k,l)=(8,2),
  d=1.
- As a byproduct, (k,l)-near-collisions with difference 1 do not exist for
  (k,l) = (6,3), (3,6), (8,2) — establishing the conjecture from
  Blokhuis–Brouwer–de Weger, Integers 17 (2017) #A64.
- Methods: elliptic curve reductions (the (3,6) cases become rank-3 elliptic
  curves whose integral points need elliptic-logarithm bounds), 27 pages.

## Relevance

Complements the GRKTU 2020 paper (which cites it as [14]) and the
Blokhuis–Brouwer–de Weger 2017 verification. It documents the per-pair
near-collision resolution that supports the claim "no unknown collisions below
10^60 / n ≤ 10^6" — the d=1 boundary cases are exactly the closest the
multiplicity witnesses can approach each other in value.

No new claims beyond corroborating `bbw-verification-bound` and the d=1 part of
`grktu-near-collision-complete`. Filed as the primary record of the (8,2) and
(3,6) d=1 resolutions and of the near-collision conjecture being settled.