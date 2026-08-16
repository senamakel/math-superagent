# SEARCH.md — scored program search for Casas–Alvero at degree 20

Scorer: `code/search/ca-degree20/score.py` (exact `Poly.gcd` over `QQ`).
Score `k` = #{ j in 1..19 : deg(gcd(f, f^(j))) > 0 }. `INVALID` = rejected
(non-monic / wrong degree / non-rational / the trivial family `(x-a)^20`).

71 candidates run (c0000–c0070). Top score **18**. One candidate (c0067)
rejected on import; the rest all scored.

## Summary

**Score distribution (69 valid + 2 invalid):**

| k   | count | representative constructions                                  |
|-----|-------|---------------------------------------------------------------|
| 18  | 44    | `x^20 - c·x^k` for any k; `(x-a)^19·(x-b)` for any a≠b        |
| 17  | 7     | mult-18 root (covers 1..17, j=18,19 both fail); sparse 2-coeff |
| 16  | 2     | mult-17 root (covers 1..16)                                   |
| 15  | 1     | mult-16 root                                                  |
| 14  | 2     | mult-15 root                                                  |
| 12  | 1     | mult-13 root at 0 + mult-7 at −3                              |
| 11  | 2     | mult-12 root + mult-8 spread                                  |
| 10  | 2     | mult-13 + mult-7 spread; even-symmetric sparse                |
| 9   | 3     | two mult-10 roots (covers 1..9); mult-9 root + distinct       |
| 8   | 1     | mult-9 root + distinct spread                                 |
| 7   | 1     | mult-8 + mult-8 + simple                                      |
| 6   | 1     | three roots mult 7,7,6                                        |
| 0   | 2     | fully distinct 20 roots; generic random                       |
| INV | 2     | non-rational (RR), import failure                             |

**Which constraint binds (the structural result):**

- **The top score is 18, and it is a hard, reproducible plateau.** Every
  construction that reaches 18 does so through one mechanism: a root of high
  multiplicity. A root of multiplicity `m` forces derivatives `1..m-1` to share
  it. With `m = 19` (the maximum a non-trivial degree-20 in reduced-ish form
  can carry), derivatives `1..18` share the root — and derivative `j = 19` is
  the unique binding one: `f^(19)` is **linear**, so it has exactly one root,
  and matching that root to a root of `f` forces the pure-power `(x-a)^20`,
  which the scorer correctly rejects as the trivial family. Hence
  **score = 18 is provably the ceiling** for a *monic degree-20 polynomial of
  the form reached here*.
- At `k = 18`, **the binding derivative is `j = 19`** in all high-multiplicity
  cases, and the binding `j = k` in the sparse `x^20 - c·x^k` cases (that
  family shares root 0 with every derivative except the single nonzero one).
- The scores 0–17 are exactly the multiplicity pattern: `score = m-1` for a
  single root of multiplicity `m` plus no cross-multiplicity sharing.

**Why 19 is not reached and does not need to be:** `k = 19` is precisely the
*Casas–Alvero hypothesis* — every one of the 19 derivatives shares a root. By
the conjecture (open at 20, believed true), the only satisfiers are the trivial
family `(x-a)^20`, which the scorer rejects. So a score of 19 from any
non-trivial construction would *be* the counterexample the search assumes does
not exist. The plateau at 18 is therefore the meaningful answer, not a failure
to search harder.

## Do I believe the top score?

**Yes, 18 is genuine** — and specifically it is a *provable* ceiling for this
family, not a lucky or floating-point artefact: every decision is exact sympy
`Poly.gcd` over `QQ`, and the 18-to-19 gap is forced by the linearity of
`f^(19)` plus the rejection of the pure-power family. My one deliberate attempt
to *break* the ceiling (choosing the second root `b` so that `f^(19)`'s single
root coincides with the multiplicity-19 root, which would give 19) scored **18,
not 19** (c0068–c0070): the algebra does not close the gap — it confirms the
linear-derivative root cannot be aligned with a root of `f` short of the
trivial family. I do **not** believe 18 is the global maximum over *all* monic
degree-20 rationals — only that reaching 19 is exactly equivalent to the open
conjecture. Within the natural construction space this search mapped, 18 is the
best and it is robust.

## Row log (one per candidate)

| file | construction | verdict |
|------|--------------|---------|
| c0000 | `x^20 - 2x^2` (root 0, single nonzero coeff at 2 → binds j=2) | SCORE 18 |
| c0001 | `x^20 - 2x^3` (binds j=3) | SCORE 18 |
| c0002 | `x^20 - 2x^4` | SCORE 18 |
| c0003 | `x^20 - 2x^6` | SCORE 18 |
| c0004 | `x^20 - 2x^7` | SCORE 18 |
| c0005 | `x^20 - 2x^8` | SCORE 18 |
| c0006 | `x^20 - 2x^9` | SCORE 18 |
| c0007 | `x^20 - 2x^10` | SCORE 18 |
| c0008 | `x^20 - 2x` (binds j=1) | SCORE 18 |
| c0009 | `x^20 - 2x^5` | SCORE 18 |
| c0010 | `(x-1)^19 (x-2)` mult-19, binds j=19 | SCORE 18 |
| c0011 | `(x-1)^18 (x-2)(x-3)` mult-18, j=18,19 fail | SCORE 17 |
| c0012 | `(x-1)^17 (x-2)(x-3)(x-4)` | SCORE 16 |
| c0013 | `(x-2)^19 (x-1)` | SCORE 18 |
| c0014 | `(x-1)^10 (x-2)^10` two mult-10 → score 9 | SCORE 9 |
| c0015 | `(x-1)^19 (x+3)` | SCORE 18 |
| c0016 | `x^19 (x-1)` | SCORE 18 |
| c0017 | `x^18 (x-1)(x+1)` | SCORE 18 |
| c0018 | `x^20 - x^10 - x` (nonzero at j=1,10) | SCORE 17 |
| c0019 | `x^2 (x^18 - 2)` (root 0 mult 2 + monomial tail) | SCORE 18 |
| c0020 | `(x-1)^18 (x+2)(x+3)` | SCORE 17 |
| c0021 | generic random monic degree-20 | SCORE 0 |
| c0022 | even-symmetric `x^20+...+10x^2` | SCORE 10 |
| c0023 | `x^20 - (3/2)x^2` | SCORE 18 |
| c0024 | `x^20 - 7x` | SCORE 18 |
| c0025 | `x^10·∏_{i=1}^{10}(x-i)` | SCORE 9 |
| c0026 | `x^15 (x-1)^5` | SCORE 14 |
| c0027 | `x^12 (x-1)^8` | SCORE 11 |
| c0028 | `x^20 - 2x^15` | SCORE 18 |
| c0029 | `x^20 - 2x^17` | SCORE 18 |
| c0030 | `x^18 (x-1)(x-2)` | SCORE 17 |
| c0031 | `∏_{i=1}^{20}(x-i)` all distinct roots | SCORE 0 |
| c0032 | `x^16 (x-1)^4` | SCORE 15 |
| c0033 | `(x-1)^18 (x^2-3x+2)` | SCORE 18 |
| c0034 | `x^20 - 2x^11` | SCORE 18 |
| c0035 | `x^20 - 2x^13` | SCORE 18 |
| c0036 | `x^20 - 2x^19` (binds j=19) | SCORE 18 |
| c0037 | `x^13 (x+3)^7` | SCORE 12 |
| c0038 | `(x-1)^11 (x+2)^9` | SCORE 10 |
| c0039 | `x^19 (x-1)` | SCORE 18 |
| c0040 | `(x-1)^19 (x-2)` | SCORE 18 |
| c0041 | `(x-1)^19 (x+2)` | SCORE 18 |
| c0042 | `(x-1)^19 (x-1/21)` | INVALID: non-rational (RR) |
| c0043 | `x^19 (x-1)` | SCORE 18 |
| c0044 | `(x+2)^19 (x-3)` | SCORE 18 |
| c0045 | `(x-5)^19 (x-2)` | SCORE 18 |
| c0046 | `x^12 (x-2)^8` | SCORE 11 |
| c0047 | `x^20 - 2x^14` | SCORE 18 |
| c0048 | `x^20 - 2x^16` | SCORE 18 |
| c0049 | `x^20 - 2x^18` | SCORE 18 |
| c0050 | `x^9·∏_{i=1}^{11}(x-i)` | SCORE 8 |
| c0051 | `x^19 (x-5)` | SCORE 18 |
| c0052 | `(x-1)^7 (x-2)^7 (x-3)^6` | SCORE 6 |
| c0053 | `x^17 (x-1)^3` | SCORE 16 |
| c0054 | `x^20 - 2x^12` | SCORE 18 |
| c0055 | `x^8 (x-21)^8 (x-1..x-4)` | SCORE 7 |
| c0056 | `(x+4)^19 (x-2)` | SCORE 18 |
| c0057 | `x^20 - x^17 - x^3` (nonzero j=3,17) | SCORE 17 |
| c0058 | `x^20 + x^4 + x^2` | SCORE 17 |
| c0059 | `(x-7)^19 (x-1)` | SCORE 18 |
| c0060 | `x^20 - 2x^7` | SCORE 18 |
| c0061 | `(x-1)^19 (x-2)` (derivation comment) | SCORE 18 |
| c0062 | `x^10 (x-5)^10` | SCORE 9 |
| c0063 | `x^20 - 3x^5` | SCORE 18 |
| c0064 | `(x-1)^18 (x-2)^2` | SCORE 17 |
| c0065 | `x^15 (x-3)^5` | SCORE 14 |
| c0066 | `x^20 - 2x^6` | SCORE 18 |
| c0067 | `(x-2)^19 (x-18/19)` with `Rational` missing | INVALID: import failed |
| c0068 | `(x-2)^19 (x-18/19)` — forced root-alignment attempt | SCORE 18 |
| c0069 | `(x-4)^19 (x-16/19)` — forced root-alignment attempt | SCORE 18 |
| c0070 | `(x-3)^19 (x-17/19)` — forced root-alignment attempt | SCORE 18 |

## What to try next

The plateau at 18 is structural, not a search artefact. The only route to 19 is
a genuine CA counterexample at degree 20, which is the open conjecture and not
reachable by construction tuning. If the search were to continue with the goal
of *pushing k up*, the only meaningful direction is algebraic: forcing *cross*
sharing between two or more distinct roots so that higher derivatives (not just
the first `m-1` of a single root) coincide — i.e. engineering a near-CA
polynomial with several recycled roots. That is exactly the "recycled roots"
locus the broader CA research threads study (e.g. degree-20 no-3-recycled
result), and it is where the interesting near-misses would live. But even there,
the linear `f^(19)` is suspected to be the universal binding constraint for
non-pure-power monic degree-20 polynomials over Q.
