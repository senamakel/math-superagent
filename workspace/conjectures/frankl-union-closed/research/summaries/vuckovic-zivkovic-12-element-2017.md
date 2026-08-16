# Vučković & Živković, "The 12-Element Case of Frankl's Conjecture" (IPSI BgD Trans. 13(1):65–71, 2017)

**Full text:** [[vuckovic-zivkovic-12-element-2017.full]] · **Source URL:** http://ipsitransactions.org/journals/papers/tir/2017jan/p9.pdf

## What it establishes

The primary source for the **n ≤ 12** verification bound (previously the library
held only the Bruhn–Schaudt survey's word, claim `survey-thm17-m12`).

Method: computer-assisted, via Marković's FC-families. A family F is *Frankl's*
(FC) if it forces an abundant element in every union-closed superfamily. The paper
reduces the n = 12 case to checking that certain families `F_i` (i = 1..33, the
"12-FC" families of Table I) are FC, then proves the reduction lemmas and runs
backtracking search (Algorithms 1–4) to certify no counterexample exists on 12
elements.

```claim
id: vuckovic-zivkovic-n12
statement: Frankl's union-closed sets conjecture holds for every union-closed
  family F ⊆ 2^X with |X| = |∪F| ≤ 12. In particular any counterexample must have
  ground-set size ≥ 13.
hypotheses: F finite union-closed, F ≠ {∅}, |∪F| ≤ 12.
holds-here: yes (this is the exact verification bound the run's oracle must match).
status: asserted-by-source (computer-assisted proof; primary paper, published IPSI
  BgD Transactions on Internet Research 13(1):65–71, 2017). NOT independently
  checked by the oracle in this run — the oracle exhaustively checks n ≤ 4 only.
bearing: the largest *ground-set* size machine-verified. Combined with
  `faro-roberts-simpson-40` (|F| ≥ 4m−1 for a counterexample on m elements), this
  yields UC for |F| ≤ 50. Confirms and upgrades the survey only-sourced
  `survey-thm17-m12`.
anchor: research/sources/vuckovic-zivkovic-12-element-2017.full.md
```

```claim
id: vuckovic-zivkovic-fc-lemma
statement: A union-closed family F is Frankl's (has an abundant element in every
  union-closed superfamily) iff there is a weight function w : X → R on X = ∪F with
  the sum over F of weights matching t(w) = (1/2)w(X) — Poonen-type weight criterion;
  and singleton/doublet/any three 3-subsets of [5] are FC (Lemma 1, Thm 1).
hypotheses: F union-closed, X = ∪F.
holds-here: yes
status: asserted-by-source (Poonen-style weight characterization).
bearing: the weight/FC machinery the computational verifications run on — matches
  the run's FC-families line (GOAL item 6) and Poonen's Theorem already in CLAIMS.
anchor: research/sources/vuckovic-zivkovic-12-element-2017.full.md
```

## Bearing for this run
This is the primary citation the `G-coupling-half`/verification work needs:
the exact method and ceiling of the n≤12 bound. The oracle in `code/` checks n ≤ 4
exhaustively; reproducing or matching n=12 would be a large computation (the paper
itself notes naive enumeration of 2^12 = 4096-set subfamilies is infeasible and
requires the FC/backtracking machinery). This source is the authoritative boundary
fact: **any counterexample has |∪F| ≥ 13**.
