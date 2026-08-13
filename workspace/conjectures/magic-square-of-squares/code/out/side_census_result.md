# `side_census`: the stated hypothesis is false, and the true statement is stronger

`code/phi_triple_variety/side_census.py` had never been run. It was written to
test the hypothesis in its own docstring:

> `1+(q1+q2)` is **NEVER** a rational square, while `1-(q1+q2)` frequently is.

Run by the operator at `M=400` (`PYTHONPATH=code`, 480 s budget, completed
without hitting the budget). Capture: `code/out/side_census.captured.txt`.

```
M=400  |Phi|=32495   pairs with q1>q2 and q1+q2<1:  156,988,030
  1-(q1+q2) a rational square:  325
  1+(q1+q2) a rational square:   66
  both:                           0
```

## The hypothesis is refuted

`1+(q1+q2)` is a rational square for **66** of the 156,988,030 pairs, so the
"never" is false. Three of the exhibited witnesses were re-verified
independently by the operator in exact `Fraction` arithmetic, with `in_phi`
confirming that both members of each pair really are in `Phi`:

| `q1` | `q2` | `1+(q1+q2)` square | `1-(q1+q2)` square |
| --- | --- | --- | --- |
| `2258256/17181025` | `6571656/193905625` | yes | no |
| `1476984/9765625` | `1257456/21390625` | yes | no |
| `10226040/65237929` | `70160160/534950641` | yes | no |

Record the docstring hypothesis **refuted**, not weakened.

## What the run actually found

The interesting column is the one the hypothesis did not mention. Across all
156,988,030 pairs, the two conditions **never hold together**:

> No pair `q1 > q2` in `Phi(400)` with `q1 + q2 < 1` has both `1-(q1+q2)` and
> `1+(q1+q2)` a rational square.

Each condition alone is satisfiable — 325 times and 66 times respectively — so
`both = 0` is not an artefact of either being empty. Every one of the 66
`plus`-witnesses inspected has `1-(q1+q2)` a non-square, and vice versa.

This is a **computation at `M = 400`, not a theorem.** It is exactly the kind of
statement that should be proved or refuted at larger `M` before anything is
built on it, and the obvious next step is to decide whether the two conditions
are provably incompatible — that is, whether `1-s` and `1+s` being
simultaneously rational squares forces `s` outside the set of sums realisable
from `Phi`. If they are incompatible, say by which invariant; a congruence
obstruction or a descent on the associated curve is the shape to look for.

```claim
id: phi-pair-sides-never-both-square
statement: For all pairs q1 > q2 drawn from Phi(M) with q1 + q2 < 1 and
  M = 400 (32495 values of Phi, 156988030 pairs), the quantity 1-(q1+q2) is a
  rational square for exactly 325 pairs and 1+(q1+q2) is a rational square for
  exactly 66 pairs, and there is no pair for which both are rational squares.
  This also refutes the hypothesis recorded in the docstring of
  code/phi_triple_variety/side_census.py, that 1+(q1+q2) is never a rational
  square: it is a rational square 66 times, and three witnesses were verified
  independently in exact Fraction arithmetic with in_phi confirming both
  members lie in Phi.
hypotheses: M = 400; q1, q2 in Phi(M); q1 > q2; q1 + q2 < 1; exact integer
  arithmetic throughout, no floating point
holds-here: yes for the stated range only. This is a computation at M = 400 and
  is not a theorem for all M. The refutation of the docstring hypothesis is
  unconditional, since a counterexample settles it
status: checked
bearing: kills the side_census docstring hypothesis outright, so nothing may be
  built on 1+(q1+q2) being non-square. Replaces it with a sharper and so far
  unbroken statement, that the two square conditions are never simultaneously
  satisfied, which if proved would be an impossibility lemma on pair sums
  rather than on triples. Must be pushed to larger M and then proved or
  refuted; a computation at M = 400 is a fact about M = 400
anchor: code/out/side_census.captured.txt; code/phi_triple_variety/side_census.py
source: operator-computation
```
