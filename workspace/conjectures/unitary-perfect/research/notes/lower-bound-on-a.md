# A lower bound on `a`, which is the direction GOAL.md asked for

`GOAL.md` names a *lower* bound on `a` in terms of `ω` as real progress, and
observes that the workspace's own budget corollary `ω(odd) ≤ a + 1` bounds `ω`
above and "says nothing that stops `a` growing". It does not have to. Combined
with a result already sitting in this workspace's own sources, it runs backwards.

## The two inputs

1. **Wall (1988), *New unitary perfect numbers have at least nine odd
   components*** — `research/sources/wall-1988-nine-odd-components.full.md`, a
   scanned Fibonacci Quarterly PDF (13,919 bytes, genuine text, 25
   theorem/proof occurrences). Any unitary perfect number other than the five
   known has `ω(odd) ≥ 9`.

2. **The 2-adic budget corollary**, proved in
   `research/notes/parity-and-2-adic-budget.md`: for `n = 2^a · Π p_i^{e_i}`
   unitary perfect, `Σ_i v2(p_i^{e_i} + 1) = a + 1` exactly, hence
   `ω(odd) ≤ a + 1`, with equality iff every odd component is `1 mod 4`.

## The consequence

```
ω(odd) ≥ 9   and   ω(odd) ≤ a + 1     ⟹     a ≥ ω(odd) − 1 ≥ 8.
```

So **`2^8 = 256` divides any sixth unitary perfect number**, and more sharply
`a ≥ ω(odd) − 1` holds as a genuine two-sided link rather than a single
inequality. Equality `a = 8` forces `ω(odd) = 9` with *every one* of the nine
odd components `≡ 1 (mod 4)` — the equality case of the budget corollary — which
is a very rigid configuration and a natural next target to eliminate outright.

This is not a re-derivation of the budget identity. The identity is one input;
the bound is the identity read in the direction the identity alone does not give,
using a literature theorem that supplies the missing side.

## Run against the witness set

`code/out/wall1988_budget_lower_bound.captured.txt`. All five known numbers are
re-verified through the oracle (`σ*(n) = 2n` true for all five), the budget
identity is re-checked as an assertion in the program, and the bound is tested:

| `n` | `a` | `ω(odd)` | `ω ≤ a+1` | `a ≥ 8` |
| --- | --- | --- | --- | --- |
| 6 | 1 | 1 | yes | no |
| 60 | 2 | 2 | yes | no |
| 90 | 1 | 2 | yes | no |
| 87360 | 6 | 4 | yes | no |
| 146361946186458562560000 | 18 | 11 | yes | **yes** |

**No witness is refuted.** Four of the five fail `a ≥ 8`, and that is correct
rather than a contradiction: Wall's theorem is about a *new* example, and those
four have `ω(odd) ∈ {1,2,2,4} < 9`, which is exactly the range his theorem
excludes from its scope. The one known number in scope, the fifth, has
`ω(odd) = 11 ≥ 9` and `a = 18 ≥ 8`, and satisfies the bound. Stating the
hypothesis "other than the five known" is load-bearing here; dropped, the
statement is false.

## What it does not give

It does not bound `a` above, so it does not finitise anything on its own. Its
value is that it makes the seed factor `2^a + 1` large — at least `2^8 + 1 = 257`
— which is the object `H_even` is about. Every prime divisor of `2^a + 1` must
be accounted for by the odd components, and `a ≥ 8` puts a floor on how much
there is to account for. That is the join between this bound and the branch
`METHOD.md` sends the run at.

```claim
id: unitary-perfect-lower-bound-on-a
statement: Any unitary perfect number other than the five known ones satisfies
  a >= omega(odd part) - 1 >= 8, where 2^a || n. Equivalently 2^8 = 256 divides
  any sixth unitary perfect number. This follows by combining Wall (1988), that
  a new unitary perfect number has at least nine odd components, with the
  workspace-proved budget corollary omega(odd) <= a + 1. Equality a = 8 forces
  omega(odd) = 9 with every odd unitary component congruent to 1 mod 4.
hypotheses: n is unitary perfect and is not one of the five known numbers -
  this hypothesis is load-bearing and the statement is false without it, since
  6, 60, 90 and 87360 all have a < 8. Wall's nine-odd-components theorem is
  taken from the scanned Fibonacci Quarterly source in research/sources and is
  not re-proved here; the budget corollary is proved in this workspace
holds-here: yes. Run against all five known numbers in
  code/out/wall1988_budget_lower_bound.captured.txt, where the oracle
  re-verifies sigma*(n) = 2n for all five, the budget identity is asserted in
  the program for all five, and no witness is refuted - the four small ones
  fall outside Wall's hypothesis and the fifth satisfies the bound with
  omega_odd = 11 and a = 18
status: checked
bearing: supplies the lower bound on a in terms of omega that GOAL.md names as
  an open direction, which the budget corollary alone does not give. It does
  not bound a above and so finitises nothing by itself; its use is that it
  forces the seed factor 2^a + 1 to be at least 257, which is the object
  H_even concerns, so it joins directly to the branch METHOD.md targets. The
  equality case a = 8 with nine odd components all 1 mod 4 is rigid and is the
  natural next class to try to eliminate
anchor: code/out/wall1988_budget_lower_bound.captured.txt;
  research/sources/wall-1988-nine-odd-components.full.md;
  research/notes/parity-and-2-adic-budget.md
source: operator-computation
```
