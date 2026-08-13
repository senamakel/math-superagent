# Sub-progression finite sub-covering of the open class n ≡ 1 (mod 840)

**Pattern finder** — every number below comes from exact-integer programs run
by this role and is re-verified; each claim carries its evidence class.

## What was examined

The Salez 7-equation modular enumeration (`code/search_subprogression.py`,
extended by `code/pattern_mining/extended_subprogression.py`) was run over
moduli M ≤ 61 and the relevant residues of the open class
`n ≡ 1 (mod 840)`. Each found family is an **explicit polynomial identity**

```
4 / (840M·k + b)  =  1/x(k) + 1/y(k) + 1/z(k),   b ≡ 1 (mod 840),
```

i.e. it settles every n in the sub-progression `n = 840M·k + b` forever.
Within the class `n = 840K + 1` this is exactly the residue `K ≡ (b-1)/840
(mod M)`.

## The verified result

**603 distinct families** were found and **all 603 independently re-verified**
(`code/pattern_mining/reverify_extended_families.py`,
`numeric_recheck_sample.py`):

- **symbolic identity:** `4/n(k) − 1/x − 1/y − 1/z == 0` for every family
  (0 failures over 603);
- **exact numeric + positivity:** at sampled k ∈ {1,5,17,100}, every x,y,z is
  a positive integer and the equation holds exactly under `Fraction`
  arithmetic (0 failures).

Per-modulus covered residues (K mod M):

| M | covered residues | fraction |
|---|---|---|
| 11 | {5,7,10} | 3/11 |
| 13 | {7,9,11,12} | 4/13 |
| 17 | {4,8,10,11,14,16} | 6/17 |
| 19 | {8,9,13,16,17} | 5/19 |
| 22 | {5,7,10,16,18,21} | 6/22 |
| 23 | {5,9,12,13,15,17,18,19,20} | 9/23 |
| 26 | {5,7,9,11,12,17,20,22,24,25} | 10/26 |
| 29 | {3,4,9,11,12,16} | 6/29 |
| 31 | {7,15,18,19,20,28,30} | 7/31 |
| 33 | {4,5,7,10,14,16,18,21,26,27,29,32} | 12/33 |
| 34 | {4,8,10,11,14,16,21,25,27,28,31,33} | 12/34 |
| 37 | {3,7,8,12,14,21,22,25} | 8/37 |

## Union density over the whole open class

- Original 7 families (M ∈ {11,13,17}): **1279/2431 = 0.526121** — exact over
  the lcm period (independent direct count over K < 10^6 gives 0.52612).
- All 603 families (moduli up to 37): **0.945305** — computed via the
  6-branch CRT decomposition of the period lcm(11,…,37) =
  212021089566 (each branch is the independent product of per-prime coverage);
  independently confirmed by direct counting: K<10^4 → 0.9418, K<3·10^6 →
  0.94530.

## Structure that explains the ceiling

Residue **K≡0 (mod M)**, i.e. `b = 1`, is **never** covered for any modulus.
This is exactly the prediction of **Schinzel Theorem 1**: `b=1` is a quadratic
residue mod `a = 840M`, so no `Z[x]` polynomial identity `4/(a k + b) =
Σ 1/F_i` exists. Hence no finite sub-cover of this shape can reach the
`K≡0 (mod M)` class for any M, so by CRT the complement
(those K ≡ 0 mod M for every M) has density exactly
`Π_p (1 − |cov_p|/p) ≈ 0.0547` and is nonempty (infinitely many n).

## What this is

A **genuine partial result**: an explicit, verified finite family of identity
sub-progressions that covers **94.5% of the hardest open residue class**
`n ≡ 1 (mod 840)`. It does **not** complete the class (density-gap ~5.5%
persists, by the Schinzel QR obstruction at `b=1`). It is not claimed to be a
covering system or a full proof.

## Evidence classes

- **603 exact symbolic identities** — checked (0 failures), plus exact numeric
  at sampled k.
- **density 0.526121** (7 families) — **exact** (one-period enumeration).
- **density 0.945305** (603 families) — **computed exactly** by CRT
  decomposition and **independently confirmed** by direct counting; not a
  closed form, but an exact value over the lcm period.
- **residue 0 never covered / Schinzel ceiling** — sourced (Schinzel Thm 1),
  consistent with the computed coverage (no M has c=0).

## Falsification terms

- If any of the 603 claimed identities fails for some k (tested k up to 100 in
  exact arithmetic; the symbolic check already covers all k), the family list
  is wrong.
- If the union density differs from 0.945305 over a full period, the CRT
  decomposition is wrong (direct count over 3·10^6 matches to 6 digits).
- If a family with `b=1` (c=0) is ever found, the Schinzel-based ceiling is
  refuted (it would contradict Schinzel Thm 1).
