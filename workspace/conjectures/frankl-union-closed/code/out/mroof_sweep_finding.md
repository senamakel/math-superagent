# M♮-certificate classification sweep, n = 1..4

The full sweep completed: every union-closed family on `[n]` for `n = 1..4`
(all 3, 13, 121, 4959 = A102896) × every element `x in [n]` — **20228 exact
QF_LRA solves** via `is_feasible_mroof` from `code/out/mroof_z3.py` (the one
canonical checker, reused verbatim, never rewritten), parallelised across 28
cores. `Alb(F)` comes from the one canonical oracle `lib.uc.abundant_elements`.

Capture: `code/out/mroof_sweep.captured.txt`. Categories per family:

- **over** — `Cert(F) \ Alb(F) ≠ ∅`: some **non-abundant** element is
  M♮-certifiable;
- **under** — `Alb(F) \ Cert(F) ≠ ∅`: some **abundant** element is **not**
  M♮-certifiable;
- **totally-uncertifiable** — `Cert(F) ∩ Alb(F) = ∅`: **no abundant element is
  certifiable at all**;
- **Cert == Alb** exactly.

## Results

```
n | #fams | over | under | totally-unc | Cert==Alb | (tot w/ Alb≠∅)
1 |     3 |    0 |    0 |           1 |         3 |            0
2 |    13 |    2 |    2 |           3 |         9 |            2
3 |   121 |   24 |   46 |          41 |        51 |           40
4 |  4959 |  686 | 2992 |        2789 |      1281 |         2788
```

The `totally-uncertifiable` total at each `n` includes the degenerate singleton
`F = {∅}` (whose `Alb` is empty because every element has abundance 0 < 1/2).
Among families with **nonempty** `Alb`, the counts are 0, 2, 40, 2788.

**Headline: on `n=4`, 2788 of 4959 union-closed families (56.2%) have a
nonempty `Alb` yet NO abundant element is M♮-certifiable**, and **2992 of 4959
(60.3%) have some abundant element that is not certifiable**. Only 1281 of 4959
(25.8%) have `Cert == Alb` exactly.

## Cross-checks

- The enumeration counts were asserted against A102896 (3, 13, 121, 4959) at
  entry, and matched.
- The `n=2` and `n=3` category counts were **recomputed independently** from
  the same canonical checker + oracle and matched the sweep exactly
  (13/121 families, over 2/24, under 2/46, total 3/41, exact 9/51).
- One concrete family was verified by hand and by direct solve: `F = {3,7}` on
  `n=3` (`{{a,b},{a,b,c}}`), abundance `[2,2,1]`, `Alb=[0,1,2]`, yet every
  element solves infeasible. The M♮-constraint forces `w(S) = 0` on the
  size-2 atom (B1 with `X=S, Y=∅`), and then the size-3 atom must carry all
  mass 1, which violates the other M♮ branch (`B1` at `X={a,b,c}, Y={a}, u=b`
  reads `1 + 0 ≤ 0 + 0`). So the family is genuinely totally-uncertifiable —
  an early copy of the same structure the `F={5,7}` predecessor (`{{x,z},
  {x,y,z}}` on `n=3`) exhibits. Its density-1 members are infeasible.
- All of these are **exact** decisions: no floats in abundance, and the
  feasibility decision is an exact `QF_LRA` solve.

## What this does and does not say (read carefully)

This is a statement about the **support-restricted** M♮-certificate: the
checker imposes `w(A) = 0` for every `A ∉ F` (constraint (i) of
`is_feasible_mroof`), i.e. it asks whether there is a probability measure on
the **family itself** that is M♮-concave on the Boolean lattice and gives the
chosen element abundance ≥ 1/2. That is far stricter than the conjecture's
demand, and its failure at scale is **not** a refutation of Frankl's
conjecture nor of any direct argument for it.

In particular the "whole-lattice constant" `w ≡ 1/|F|` (which is trivially
M♮-concave) is *not* the function the checker tests: the checker tests the
**support-restricted** constant, which generally violates M♮-concavity
(module docstring of `mroof_z3.py` gives the `n=2, F={∅,{x,y}}` counterexample).
So these counts measure how often the *restricted* M♮-certificate class can
witness an abundant element, not how often the conjecture holds. The value of
the sweep is:

1. It sharply delimits the **support-restricted M♮-method**: it failed to make
   the conjecture's own abundant elements certifiable on a majority of small
   UC families, so any claim that "M♮-concavity on the support proves UC" is
   refuted computationally at n ≤ 4 (though `F={∅}` is a degenerate outlier,
   the nonempty-`Alb` cases are not: 2788 of them on n=4).
2. It confirms the `F={5,7}` / `F={3,7}` "density-1 element infeasible"
   structure is not an isolated quirk: the totally-uncertifiable families on
   `n=3` include all 15 `F={S,∅-or-not}` size-1/2 families whose `Alb` is every
   element of `S` (e.g. `{a},{b},{c}` singletons, `{a,b},{a,c},{b,c}` pairs,
   `{a,b,c}` — the pair `{S,{a,b,c}}` and `{∅,S,{a,b,c}}` forms). The genuinely
   interesting dense ones are the `{-,S,{a,b,c}}` forms like `F={0,1,3,7}`.

## Limits / ceiling

- Hard ceiling reached exactly at `n=4`, `|F| ≤ 7` masks, with all 20228
  solves completed. `n=5` would require 2^32 ≈ 4.3×10⁹ candidate subfamilies
  to enumerate (not feasible by this brute enumeration) and the M♮-constraint
  alone is 2^n × 2^n × n triples = 8000 per solve at n=5 — both blow up.

## Files

- `code/out/mroof_sweep.py` — the sweep driver (parallel).
- `code/out/mroof_sweep.captured.txt` — the capture.
- This note.

# Filed claim: support-restricted M♮-certificate under-certification is typical

<!-- regenerator-trigger -->

```claim
id: mroof-sweep-under-certification-typical-n4
statement: Over ALL union-closed families on [n] (counts 3, 13, 121, 4959 =
A102896), for the support-restricted M♮-certificate check
is_feasible_mroof(F_masks, n, x) (w supported on F, w>=0, sum=1, x-abundance
>= 1/2, M♮-concave on the Boolean lattice), the counts are: n=1 totally-unc 1
(only F={∅}, Alb empty), over 0, under 0, Cert==Alb 3; n=2 totally-unc 3 (2
with nonempty Alb), over 2, under 2, Cert==Alb 9; n=3 totally-unc 41 (40
nonempty-Alb), over 24, under 46, Cert==Alb 51; n=4 totally-unc 2789 (2788
nonempty-Alb), over 686, under 2992, Cert==Alb 1281. On n=4, 2788/4959 (56.2%)
union-closed families have nonempty Alb yet NO abundant element is
M♮-certifiable, and 60.3% have some abundant element not certifiable; only
25.8% have Cert==Alb. So the SUPPORT-RESTRICTED M♮-certificate class typically
FAILS to witness the conjecture's own abundant elements on small UC families;
the F={5,7}/{3,7} 'density-1 infeasible' structure is widespread, not isolated.
hypotheses: support-restricted M♮-concavity (w(A)=0 outside F) — far stricter
than the conjecture's demand; exact QF_LRA solves over the reals; enumeration
convention incl. F={∅}, excl. empty collection.
holds-here: yes
status: verified-computational — 20228 exact Z3 QF_LRA solves (canonical
checker code/out/mroof_z3.py reused verbatim; Alb from lib.uc), parallel 28
cores; enumeration counts asserted = A102896; n=2,3 category counts
independently recomputed and matched; F={3,7} n=3 verified infeasible-for-all
elements by hand and direct solve. NOT a refutation of Frankl's conjecture:
it bounds only the restricted-M♮-method.
bearing: rules out "support-restricted M♮-concavity proves UC" computationally
at n <= 4; delimits the restricted-M♮-certificate method, and confirms the
{S,{a,b,c}} dense structure observed at F={5,7}. Does NOT lift to a positive
or negative UC result.
anchor: code/out/mroof_sweep.captured.txt, code/out/mroof_sweep.py,
code/out/mroof_z3.py
```
