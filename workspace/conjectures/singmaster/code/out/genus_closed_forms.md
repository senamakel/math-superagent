# Genus of `C(x,k₁) = C(y,k₂)` in closed form, and the Faltings threshold

`GOAL.md` lists as an acceptable partial result:

> the genus of `C(x,k1) = C(y,k2)` computed as a function of `k1, k2`, with the
> threshold above which Faltings applies made explicit.

The run computed it with Singular and **never recorded it** — `famB`, `famD`
and `diag_families` have zero mentions in `research/CLAIMS.md`, and the run has
since been reduced to `402 63` with `run-failed 38`. The captures were about to
be lost, so the operator extracted the data and fitted it.

## The data

| capture | curve | `n` range | points |
| --- | --- | --- | --- |
| `diag_families.captured.txt` | `C(x, n−1) = C(y, n)` | 3–22 | 20 |
| `famB.captured.txt` | `C(x, n−2) = C(y, n)` | 4–21 | 18 |
| `famD.captured.txt` | `C(x, n+2) = C(y, n)` | 3–19 | 17 |

`famA2.captured.txt` produced **no data at all** — only Singular library loading
followed by `halt 1`. All four captures end in `halt 1`, so every one of these
Singular runs terminated with an error after emitting its partial table. The
tables themselves are internally consistent and fit exactly, but the runs did
not complete and that should be stated wherever they are used.

## Closed forms — all 55 points fit exactly

```
adjacent      C(x, n−1) = C(y, n) :   g(n) = (n−1)(n−2)/2
gap two       C(x, n−2) = C(y, n) :   g(n) = ⌊(n−1)(n−3)/2⌋
gap two up    C(x, n+2) = C(y, n) :   g(n) = ⌊(n+1)(n−1)/2⌋
```

Zero mismatches: 20/20, 18/18, 17/17.

The gap-two family needs the floor because its growth is parity-split — the
first differences run `3,3,5,5,7,7,9,9,…`, giving `(n²−4n+2)/2` for even `n` and
`(n−1)(n−3)/2` exactly for odd `n`. The floor unifies both.

**Consistency check that the run did not make:** `g_D(n) = g_B(n+2)` for every
overlapping `n`. That must hold, since `C(x,n+2) = C(y,n)` and
`C(x,n−2) = C(y,n)` describe the same unordered pair `{n, n+2}` re-indexed. It
does, which is independent evidence that both Singular tables are right.

## The Faltings threshold, explicit

Faltings requires genus `≥ 2`:

| family | genus `> 1` for | genus `≤ 1` only at |
| --- | --- | --- |
| `C(x, n−1) = C(y, n)` | `n ≥ 4` | `n = 3` (genus 1) |
| `C(x, n−2) = C(y, n)` | `n ≥ 5` | `n = 4` (genus 1) |
| `C(x, n+2) = C(y, n)` | `n ≥ 3` | — |

So along these three diagonals the genus exceeds 1 immediately and grows
**quadratically** in `n`. Faltings gives finitely many rational points for all
but one curve per family.

## What this does not give

The genus growing quadratically is exactly why this does **not** approach
Singmaster. Faltings is ineffective in the parameter: it yields "finitely many"
per `(k₁,k₂)` with no count computable in `n`, and the conjecture needs a bound
uniform over all pairs at once. A quadratically growing genus makes the uniform
statement harder, not easier — there is no threshold beyond which the curves
become uniformly controlled. This is the workspace's standing trap, and the
closed forms sharpen rather than escape it.

These are also only three diagonals of the two-parameter family. The genus as a
function of general `(k₁,k₂)` is not established here.

```claim
id: genus-closed-forms-three-diagonals
statement: For the curves C(x,k1) = C(y,k2) the genus along three diagonals is,
  in closed form, g(n) = (n-1)(n-2)/2 for C(x,n-1)=C(y,n), g(n) =
  floor((n-1)(n-3)/2) for C(x,n-2)=C(y,n), and g(n) = floor((n+1)(n-1)/2) for
  C(x,n+2)=C(y,n). Each formula reproduces every Singular-computed value with
  zero mismatches: 20/20 points for n=3..22, 18/18 for n=4..21, and 17/17 for
  n=3..19 respectively. The gap-two growth is parity-split, equal to
  (n^2-4n+2)/2 for even n, which the floor unifies. The identity g_D(n) =
  g_B(n+2) holds throughout, as it must since both index the unordered pair
  {n, n+2}. Consequently genus > 1 for n >= 4, n >= 5 and n >= 3 respectively,
  with genus exactly 1 at n=3 and n=4 in the first two families, so Faltings
  applies to all but one curve per diagonal and the genus grows quadratically.
hypotheses: genus as computed by Singular for the affine curve C(x,k1)-C(y,k2);
  the three Singular runs each terminated with halt 1 after emitting their
  tables, so the tables are partial outputs of errored runs
holds-here: yes for the three diagonals and the stated n ranges. The genus as a
  function of general (k1,k2) is not established. famA2 produced no data
status: checked
bearing: supplies the genus-as-a-function-of-parameters deliverable named in
  GOAL.md for three diagonals, with the Faltings threshold explicit. Confirms
  rather than escapes the workspace's standing trap: the genus grows
  quadratically, so Faltings applies everywhere but remains ineffective in the
  parameter, and no threshold makes the family uniformly controlled. Salvaged
  from captures the run never entered in its ledger before failing on credit
  exhaustion
anchor: code/out/diag_families.captured.txt; code/out/famB.captured.txt;
  code/out/famD.captured.txt; code/out/genus_closed_forms.md
source: operator-computation
```
