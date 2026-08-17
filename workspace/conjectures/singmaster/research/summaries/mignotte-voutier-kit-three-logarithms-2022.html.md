# Mignotte–Voutier 2022/2023 — "A kit for linear forms in three logarithms"

<!-- source: https://arxiv.org/html/2205.08899v3 | full text: research/sources/mignotte-voutier-kit-three-logarithms-2022.html.full.md -->

Maurice Mignotte, Paul Voutier, "A kit for linear forms in three logarithms",
Math. Comp. (accepted); arXiv:2205.08899v3 (Sep 2023), appendix by Michel
Laurent. This source REPLACES the earlier partial hold (the old
`research/sources/mignotte-voutier-kit-three-logarithms-2022.full.md` was only
the arXiv landing page). Full text is on disk (2221 lines).

## What it establishes

A technique for turning problems reducible to a nonzero linear form
`Λ = b1 log α1 + b2 log α2 + b3 log α3` in three logarithms of algebraic numbers
into an explicit lower bound on `|Λ|`, with constants significantly better than
the general Matveev bound. The method: Waldschmidt's degenerate-case handling +
Matveev's three-log theorem (their Theorem 3.1, quoted in full: `log|Λ| > −C1·D²·A1·A2·A3·log(1.5eDB·log(eD))` with `C1 = 5·16^5/(6χ)·e³·(7+2χ)·(3e/2)^χ·(26.25+log(D² log(eD)))`), plus interpolation determinants giving choices of K,L,R,S,T and a "solve by brute force over four parameters" §5 recipe.

Key structural points for this run:

- **Main Theorem 2.1** (full statement at lines 183–265). Under the conditions
  (2.7)–(2.13) — size conditions on R,S,T, the zero-lemma count conditions
  (2.10)–(2.13), and `0 < |Λ| < 2π/w` where w is the maximal root-of-unity order
  in `Q(α1,α2,α3)` — either `Λ' > ρ^(−KL)` (the effective bound, cleaner than
  Matveev's overflow term) or a degeneracy condition (2.14)/(2.15) holds: either
  the `b_i` are bounded by the R,S,T, or there is an integer linear relation
  `u1 b1 + u2 b2 + u3 b3 = 0` with bounded coefficients. **The linear-dependence
  escape (2.15) is the same shape as the (2,3) vacuity found in this run**: an
  exact solution of the Diophantine equation makes `Λ = 0` or puts `b` in a
  small linear relation, so the method constrains only genuine near-misses.
- Worked examples in §2.1 (the paper states its log's are Q-linearly independent
  in both cases presented, so no degeneracy there).

## Bearing for this run

The adopted `baker-linear-forms-two-logarithms` approach uses Gouillon 2006
(held) for TWO logs; this kit is the current state of the art for THREE logs
and is the natural upgrade if a reduction produces a 3-log form (e.g. a
`C(x,k1)=C(y,k2)` reduction to an equality of products of 3 factorials, or a
Pell-type family where the unit group has rank 2). Publicly shared code is
mentioned in the paper — §1.4; worth locating if the constant-evaluation task
(`G-constant-evaluation` in BACKWARD.md) picks a 3-log form. History: the
"5·10⁴ instead of 10⁸" gain over Baker's method that Gouillon 2006 achieved for
two logs is extended here in the same style. The degeneracy escape clause
matches the run's established `matveev-explicit-2-3` closure: an exact equality
produces `n_nonzero = 0` or a linear relation, so these theorems bound
near-misses, not exact solutions — state that when citing.

```claim
id: mv-kit-three-logarithms-main
statement: Mignotte-Voutier 2023 (Thm 2.1): for a nonzero 3-log form
  Λ = b1 log α1 + b2 log α2 + b3 log α3 with α_i distinct nonzero algebraic,
  logs Q-linearly independent, and conditions (2.7)-(2.13) on parameters
  R,S,T,K,L plus 0<|Λ|<2π/w (w maximal root-of-unity order in Q(α1,α2,α3)),
  either |Λ|·LT·e^{LT|Λ|/(2b3)}/(2|b3|) > ρ^{−KL}, or a degeneracy holds:
  |b_i| bounded by R,S,T, or an integer linear relation u1 b1+u2 b2+u3 b3=0
  with bounded u_i. Matveev's 3-log theorem (their Thm 3.1) is quoted with
  explicit C1.
hypotheses: as stated; Q-linear independence of the logs is the operative
  hypothesis, and the escape clause handles its failure.
holds-here: no clean application yet — the run's linear forms are over
  factorials of small parameters (2 or 3 logs), and the (2,3) exact-equality
  case is degenerate (matveev-explicit-2-3). A 3-log form arises only if a
  specific reduction produces one; flag for G-constant-evaluation if it does.
status: sourced (full text read; Thm 2.1 and Thm 3.1 quoted verbatim above)
bearing: the best currently-available explicit constants for 3-log forms; the
  degeneracy escape clause is the same wall as matveev-explicit-2-3 — these
  bounds constrain near-misses, not exact solutions.
anchor: research/summaries/mignotte-voutier-kit-three-logarithms-2022.html.md
```