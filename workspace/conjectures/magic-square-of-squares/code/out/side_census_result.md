# The M=800 complete run

`code/phi_triple_variety/side_census_par.py` (parallel, exact-sorted,
checkpointed) run to completion on 26 workers (28 CPUs available):

```
M=800 |Phi|=129870 pairs sum<1: 2509516913
  1-(q1+q2) rational square: 718
  1+(q1+q2) rational square: 150
  both: 0
```

Coverage: the **entire** outer index [0,129870) — the earlier
`side_census_M800.captured.txt` was a budget-killed partial run that stopped
at outer-i=22988/129870 (~18% of the index, the smallest Phi-values only) and
printed 6/11/0 there; it is superseded. The checkpoint file
`code/out/side_census_stages_M800.jsonl` sums to exactly the printed totals
(pairs 2509516913, minus 718, plus 150, both 0), and four example witnesses
(two kinds) were independently re-verified: both q's really lie in Phi
(lib.phi.in_phi) and the claimed side is a rational square while the other is
not.

The invariant now stands at four consecutive complete sizes, each a full
census over its index:

| M | \|Phi(M)\| | pairs | minus | plus | both |
| --- | --- | --- | --- | --- | --- |
| 100 | 2040 | 614,165 | 46 | 5 | 0 |
| 200 | 8156 | 9,856,010 | 132 | 24 | 0 |
| 400 | 32495 | 156,988,030 | 325 | 66 | 0 |
| 800 | 129870 | 2,509,516,913 | 718 | 150 | 0 |

Each side condition alone is satisfiable at every M and the counts grow — so
`both = 0` is not an artefact of either side being empty. A "both" witness
would be a necessary-condition survivor for q1+q2 in Phi, i.e. exactly the
kind of pair the no-triple conjecture needs to rule out; none exists through
M = 800 (2.5e9 pairs). Still a computation, not a theorem; the structural
question (why the two square conditions are incompatible for s = q1+q2 with
q1,q2 in Phi) remains open.

```claim
id: phi-pair-sides-both-square-zero-through-M800
statement: For every M in {100, 200, 400, 800} and every pair q1 > q2 from
  Phi(M) with q1 + q2 < 1 (614165, 9856010, 156988030 and 2509516913 pairs
  respectively), the quantity 1-(q1+q2) is a rational square exactly {46,
  132, 325, 718} times and 1+(q1+q2) exactly {5, 24, 66, 150} times, and no
  pair has both rational squares. The M=800 count is a COMPLETE census over
  the full outer index (a prior partial capture that stopped at 18% of the
  index and reported 6/11/0 there is superseded).
hypotheses: M <= 800; q1, q2 in Phi(M); q1 > q2; q1 + q2 < 1; exact integer
  arithmetic throughout; M=800 run parallel over 26 workers, checkpoint sums
  equal the printed result, example witnesses re-verified independently
holds-here: yes for M <= 800 only; a computation, not a theorem for all M
status: checked
bearing: extends phi-pair-sides-never-both-square to a complete 2.5e9-pair
  census and so keeps alive the strongest unbroken side statement: the two
  square conditions 1+s and 1-s are never simultaneously satisfied for a
  pair-sum s realisable from Phi. A proof of that incompatibility would be an
  impossibility lemma on pair sums (s = 2t/(1+t^2) parametrisation of
  x^2+y^2=2 intersected with Phi-pair-sums), and it would not forbid the
  known near-miss witnesses, which are not pair sums of Phi elements in
  (0,1) with both sides square
anchor: code/out/side_census_M800_complete.captured.txt;
  code/out/side_census_stages_M800.jsonl;
  code/phi_triple_variety/side_census_par.py;
  code/out/side_census.captured.txt (M=400 serial)
source: operator-computation
```

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
