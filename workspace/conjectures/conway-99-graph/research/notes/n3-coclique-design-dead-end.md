# The coclique-design line at 99 is a dead end — the forced 2-(22,4,2) exists arithmetically

## What was tested

The most promising non-local structural number the run produced (§3 of solution.md):
the coclique bound `α = v·(−s)/(k−s)` for `srg(99,14,1,2)` equals
`α = 99·4/18 = 22`, parameter-specific (controls have α = 3, 5, 9, 45 — all
different), so a Wilbrink–Brouwer-style "tight coclique forces a design" argument
at 99 is **not** refuted on arrival.

## Claim block

```claim
id: coclique-alpha22-forces-22242-design
statement: If a hypothetical srg(99,14,1,2) contained a coclique C of the
  Hoffman-bound size alpha = v*(-s)/(k-s) = 22, then equality in the ratio bound
  forces f = 1_C - (alpha/v)1 into the s=-4 eigenspace, hence every vertex
  outside C has exactly d_C = alpha*(k-s)/v = 22*18/99 = 4 neighbours inside C;
  and since every pair in C is non-adjacent with exactly mu=2 common neighbours
  (outside C), the outside-neighbourhood sets form a 2-(22,4,2) design with
  b = 77 blocks, replication r = 2*21/3 = 14, block size 4. The three parameter
  identities hold exactly (77*C(4,2)=2*C(22,2)=462; 22*14=77*4=308; r=14). The
  design is ARITHMETICALLY FEASIBLE (b=77 != v=22 so symmetric-form BRC does not
  apply; all necessary conditions incl. the sum-of-squares determinant condition
  hold), so no contradiction arises from arithmetic alone. The force is real and
  verified on the controls: rook(3)'s maximal 3-cocliques have every outside
  vertex at the forced value d_C = 2 (exhaustive; matches alpha(k-s)/v = 2);
  BvLS's forced value for a 45-coclique is d_C = 45*27/243 = 5 (2-(45,5,2)).
hypotheses: existence of srg(99,14,1,2) assumed; C a coclique of size exactly
  alpha=22 (a nontrivial hypothesis); mu=2 regular structure.
holds-here: yes for the reduction (the force is an exact derivation); whether
  the hypothesis |C|=22 holds is the open question itself.
status: checked (exact integer/sympy; derivation + control match + design
  feasibility).
bearing: closes the arithmetic avenue of the coclique-design line; the live
  remainder is whether any feasible 2-(22,4,2) design lifts (a finite
  construction/exclusion question), per lou-murin-alpha22-block-design-reduction.
anchor: code/out/coclique_design.captured.txt
```

## The mechanism (exact, checked — code/out/coclique_design.captured.txt)

Let `C` be a coclique of size `α = 22` in a hypothetical `srg(99,14,1,2)`.
Equality in the Hoffman/Delsarte ratio bound forces `f = 1_C − (α/v)1` into the
`s = −4` eigenspace, i.e. `Af = s·f`. For `x ∉ C`:

- `(Af)_x = d_C(x) − αk/v = d_C(x) − 28/9` (regularity, exact)
- must equal `s·f_x = −4·(−2/9) = 8/9`

so `d_C(x) = 36/9 = 4`. **Every outside vertex has exactly 4 neighbours in C.**
Every pair in `C` is non-adjacent, hence shares exactly `μ = 2` common neighbours
(outside `C`), so the outside-neighbourhood sets are 4-subsets of `C` forming a
**2-(22,4,2) design**: `b = 77` blocks, replication `r = 2·21/3 = 14`, block size 4.

Parameter identities hold exactly: `77·C(4,2) = 2·C(22,2) = 462`;
`22·14 = 77·4 = 308`; `r = 14`.

## The obstruction that closes the line

**2-(22,4,2) is NOT arithmetically excluded.** All necessary conditions pass:
integers (`b=77, r=14`), Fisher (`b ≥ v`), the three parameter identities, and
the Gram/determinant sum-of-squares condition (`det(NᵀN) = 12²¹·308` has
squarefree part 231, trivially a sum of ≥4 squares by Lagrange).

Crucially, **symmetric-form Bruck–Ryser–Chowla does not apply**: BRC concerns
*symmetric* 2-designs (`b = v`), and here `b = 77 ≠ v = 22`. The tempting
"`r − λ = 12` is not a square" exclusion only bites for symmetric designs, so it
does not rule out 2-(22,4,2). Existence is a construction question the
arithmetic does not decide.

## Conclusion (accurate framing)

A tight 22-coclique in a putative srg(99,14,1,2) forces the outside
neighbourhoods to form a **2-(22,4,2)** design, and that design is
**arithmetically feasible** (b=77≠v=22, so symmetric-form BRC does not apply;
all necessary conditions hold). So **arithmetic alone gives no contradiction** —
this closes the *arithmetic* avenue of the coclique-design line.

The line is NOT fully dead: the live sub-question, already flagged by the
Lou-Murin note (`lou-murin-alpha22-block-design-reduction`), is whether *any*
feasible 2-(22,4,2) design lifts to a graph — a design with a repeated block or a
block sharing ≥3 treatments would give two outside vertices ≥4 or 3 common
neighbours, violating μ=2. That lift step is a finite construction/exclusion
question, not settled by the feasibility here. This run's contribution is to
pin down the force exactly (d_C = 4, 2-(22,4,2) with b=77, r=14) and to record
that the design's arithmetic does not itself kill the case. The route does not
bear negatively or positively on the existence of srg(99,14,1,2) short of the
lift step.

The equality-force itself is real and verified against the controls: rook(3)'s
maximal 3-cocliques have every outside vertex at forced value d_C = 2 (exhaustive,
matches α(k−s)/v = 3·6/9 = 2); BvLS's forced value for a 45-coclique is
d_C = 45·27/243 = 5 (giving 2-(45,5,2), identities hold).

Evidence class: **verified-computationally** (exact integer/sympy rational
arithmetic; the design-parameter force is a derivation, the control match an
exotic check, the design-existence verdict an arithmetic check). Not a
nonexistence claim about srg(99,14,1,2).

Claim id: `coclique-design-dead-end-22242-feasible`.
Anchors: `code/out/coclique_design.captured.txt`, `code/out/coclique_design.py`.
