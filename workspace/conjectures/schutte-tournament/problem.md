# Schütte's problem: the smallest $n$-dominated tournament

*Erdős Problem #902 (erdosproblems.com/902), from [Er63c] and [Er82e]. Asked of
Erdős by Schütte in the early 1960s.*

## Statement

A **tournament** is a complete directed graph: for every pair of distinct
vertices `u, v` exactly one of `u -> v`, `v -> u` is present. Say a tournament
has **property `S_n`** if for **every** set `X` of `n` vertices there is some
vertex `y` outside `X` with `y -> x` for all `x` in `X` (`X` is *dominated*).

Let

```
f(n) = min { |V(T)| : T is a tournament with property S_n }.
```

> **Question.** Estimate `f(n)`.

## What the statement does and does not say

- **Every** `n`-set must be dominated, by **some** vertex, and that vertex must
  beat all `n` of them. The dominating vertex depends on the set.
- `f(n)` is a **finite, exactly computable number** for each `n`: property `S_n`
  is a first-order condition on a finite structure, so "is there a tournament on
  `N` vertices with property `S_n`?" is a satisfiability question with
  `binom(N,2)` Boolean variables and one clause-group per `n`-subset. That is
  the whole oracle.
- The known exact values are `f(1) = 3`, `f(2) = 7`, `f(3) = 19`. `f(4)` is
  **not known exactly**. Those three values plus the bounds below are the entire
  ground truth, and every claim in this run is measured against them.
- The problem says "estimate", so an improved upper bound (a construction) and
  an improved lower bound (a proof, or an exhaustive search) are both results.

## Where the literature is known to have got to — verify each

Nothing below may be cited without a primary source and a claim block.

- **`f(1) = 3`** — the 3-cycle. **`f(2) = 7`** — the quadratic residue
  tournament on 7 vertices (Paley). Both are within exhaustive reach and must be
  re-derived here on day one; they calibrate the oracle.
- **`f(3) = 19`**, proved by **Szekeres and Szekeres [SzSz65]**. The upper bound
  is a construction on 19 vertices; the lower bound is an exhaustive argument
  that 18 do not suffice. **Reproducing the 19-vertex witness is a realistic
  early target for the oracle and would prove it works.**
- **Erdős [Er63c]** proved
  ```
  2^{n+1} - 1  <=  f(n)  <<  n^2 * 2^n.
  ```
  The upper bound is the probabilistic method — a random tournament on
  `C n^2 2^n` vertices has property `S_n` with positive probability — and it is
  one of the founding examples of that method. **Re-derive it here; it is short,
  it is exact, and it sets the scale.**
- **Szekeres and Szekeres [SzSz65]** improved the lower bound to `n 2^n << f(n)`.

So the gap is
```
c * n * 2^n   <=   f(n)   <=   C * n^2 * 2^n,
```
a factor of `n`, unmoved for sixty years. **Say this in `CONTEXT.md` on day
one.** Note the striking parallel with Erdős Problem #901 (Property B), which
has the same `2^n`-scale, the same factor-`n` gap, and the same probabilistic
upper bound — if this workspace and that one both run, the shared obstruction is
worth stating.

- **Explicit constructions.** Paley (quadratic residue) tournaments on `q`
  vertices have property `S_n` for `q` above roughly `n^2 4^n` — worse than the
  probabilistic bound, but **explicit**, which the random construction is not.
  Get the exact threshold; the gap between the explicit and probabilistic
  constructions is itself a well-known open question.

## The obstruction, stated honestly

1. **Both bounds are ancient and the methods are exhausted.** The upper bound is
   the plain first-moment method; the lower bound is a counting argument. Sixty
   years of no movement means an approach that is a refinement of either is
   attacking the well-worked side.

2. **The exact values stop at `n = 3` for a reason.** Deciding property `S_4`
   requires checking `binom(N,4)` sets on a tournament with `binom(N,2)` free
   bits, and the lower bound requires ruling out **all** tournaments on `N-1`
   vertices — a search over an astronomically large isomorphism class space.
   **This must not be attempted as an enumeration.** SAT with strong symmetry
   breaking, or a clever combinatorial reduction, is the only route, and even a
   better *upper* bound for `f(4)` would be new territory.

3. **The explicit-versus-random gap is the conceptually interesting half.** The
   random construction gives `n^2 2^n` and names no tournament; every explicit
   family known is worse. **Derandomising, even partially, is a recognised
   objective and a legitimate deliverable of this run.**

Stated as the thing to beat:

> **A better upper bound must exhibit (or prove the existence of) a tournament on
> `o(n^2 2^n)` vertices with property `S_n`; a better lower bound must beat the
> counting argument giving `n 2^n`. Sixty years say neither will come from a
> refinement of the existing proof.**

Say which side the approach is on and what it does that the existing argument
does not.

## The oracle: a SAT decision procedure, and the falsifier

1. **`hasS_n(T)`** — given an explicit tournament, decide property `S_n` by
   direct check over all `binom(N,n)` subsets. Exact, and the cost is
   combinatorial rather than clever. Verify by hand on the 3-cycle (`S_1`, yes)
   and on the Paley tournament on 7 vertices (`S_2`, yes) and on any tournament
   on 6 vertices (`S_2`, must be **no**, since `f(2) = 7`).

2. **`exists(N, n)`** — is there a tournament on `N` vertices with property
   `S_n`? Encode as SAT: one Boolean `x_{uv}` per unordered pair (`u -> v` iff
   true), and for each `n`-subset `X` a clause saying some `y` outside `X` beats
   all of `X` — which needs auxiliary variables (`d_{y,X}`) or a cardinality
   encoding. **State the encoding in full and count its clauses before running
   it**; the naive encoding for `n = 4` is enormous and the encoding choice is
   the difference between a result and a timeout.

3. **Symmetry breaking is mandatory.** Tournaments have a huge automorphism
   group acting on the search space; without lex-leader or partial symmetry
   breaking, a lower-bound search is hopeless. Say exactly which symmetry
   breaking was used, and whether it is complete (preserves satisfiability) or
   partial.

4. **The falsification oracle.** Any claimed lower bound `f(n) >= g(n)` is
   evaluated at `f(1)=3`, `f(2)=7`, `f(3)=19` — **a bound exceeding one of these
   is false; record it refuted, not weakened.** Any claimed construction is fed
   to `hasS_n` and must come back yes; one that does not is refuted immediately.
   Any claimed asymptotic upper bound is evaluated at `n = 1,2,3` and compared
   against `3, 7, 19`.

Expect `n <= 3` to be unable to distinguish `n 2^n` from `n^2 2^n`. Compute it
anyway; it is the only thing standing between the run and a plausible false
theorem.

## Leads — verify each before relying on it

- **Szekeres–Szekeres [SzSz65]**: the 19-vertex construction, the exhaustive
  lower bound argument, and the `n 2^n` bound in full.
- **Erdős [Er63c]**: the first-moment upper bound, with the exact constant.
- **Paley / quadratic-residue tournaments**: the exact `n` for which `Q_q` has
  property `S_n`, via the Weil bound on character sums. This is the standard
  explicit construction and its threshold is computable.
- **Known bounds on `f(4)`**: what is the best published upper bound, and what
  is the best published lower bound? Record both with their sources; this run
  should know exactly what it is trying to beat.
- **Derandomisation of the first-moment argument** for this and neighbouring
  problems (`Property B`, Ramsey lower bounds) — where explicit constructions
  have and have not caught up with random ones.
