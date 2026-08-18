# The Collatz conjecture (3n + 1 problem)

## Statement

> Define $T : \mathbb{Z}^+ \to \mathbb{Z}^+$ by
>
> $$T(n) = \begin{cases} n/2 & n \text{ even} \\ 3n+1 & n \text{ odd} \end{cases}$$
>
> For every positive integer $n$, the orbit $n, T(n), T(T(n)), \dots$ eventually
> reaches $1$ (and then cycles $1 \to 4 \to 2 \to 1$).

Also called the $3n+1$ problem, the Ulam conjecture, the Kakutani problem, the
Thwaites conjecture, or Syracuse problem (a closely related variant divides out
all factors of 2 in one step: $n \mapsto (3n+1)/2^{v_2(3n+1)}$ for odd $n$).
Posed in the 1930s (commonly attributed to Lothar Collatz, 1937). It is **open**
— nobody has proved it and nobody has produced a counterexample, and it has
resisted since the 1930s, so the working assumption for this run is that a
full proof is out of reach, and the deliverable is a genuine partial result
stated exactly, not a claim of the conjecture.

## What the statement does and does not say

- The claim is about *every* positive integer, not almost every one. Tao's 2019
  result (see below) is a near-resolution in a precise asymptotic-density
  sense and is **not** a proof of the conjecture — it does not rule out a
  vanishingly rare divergent or non-trivial-cycle orbit. Do not conflate the
  two.
- Three sub-claims are bundled together and worth separating: (a) no orbit
  diverges to infinity, (b) no orbit enters a cycle other than
  $1 \to 4 \to 2 \to 1$, (c) therefore every orbit reaches 1. A partial result
  that rules out one of (a)/(b) for a class of $n$, without the other, is
  still real progress and should be reported as such.
- $n$ ranges over positive integers; behavior on $0$ or negative integers is a
  different (also studied, also open in places) question and out of scope
  unless it bears on the positive case.
- The map is deterministic and total on $\mathbb{Z}^+$; there is no
  probabilistic element in the actual problem, only in heuristic arguments
  about it (the "random walk" heuristic explaining *why* it's expected to be
  true — not a proof).

## Why it is hard, stated as the obstruction to beat

The $3n+1$ map mixes multiplicative structure (division by 2, dependent on
2-adic valuation) with an additive perturbation ($+1$) under multiplication by
3 — two operations governed by different primes with no known algebraic
relation tying them together. Heuristically, each step multiplies $n$ by
roughly $3$ or $1/2$ with "probability" $1/2$ each, giving expected
multiplicative drift $\sqrt{3}/2 < 1$, which is why almost all orbits are
expected to shrink — but this heuristic assumes independence between
consecutive parities that is not proved and is exactly what would need to be
established (or replaced by something rigorous) to get a real theorem, not
just Tao's almost-all-orbits statement. Any successful approach must handle
the *worst case*, not the average case; a result that only controls typical
orbits (however strong, e.g. density-one) has not touched the conjecture
itself, only its statistical shadow.

That is the single sentence to keep in view: an approach that ends in "almost
every orbit" or "density 1" or "for $n$ up to $N$" has produced real
mathematics but has not made progress on the *conjecture*, only on the
landscape around it — report it as exactly that, not as narrowing the open
case.

## Where the literature is known to have got to

**These are leads to verify, not established facts.** Every one must be checked
against a primary source before anything is built on it, and any that cannot
be found must be recorded as unfound rather than assumed. Names and years here
are starting queries and may be wrong.

- Terence Tao, "Almost all orbits of the Collatz map attain almost bounded
  values" (2019/2022, published form) — shows that for the Syracuse map, all
  but a set of logarithmic density zero of starting values eventually reach a
  value below any prescribed slowly-growing function. Find the exact statement
  and exactly what it does *not* claim.
- Computational verification: every starting value up to some large bound
  (historically $2^{60}$-ish, more recently reported far higher, e.g. via
  distributed projects) has been checked to reach 1. Find the current record,
  the method (which almost certainly uses the accelerated/Syracuse form and a
  tree/coverage argument to avoid checking every integer individually), and
  who holds it.
- Non-existence of small non-trivial cycles has been checked computationally
  up to very large bounds on cycle length / minimum element; find the current
  bound and the argument type (continued-fraction / Baker's-theorem-style
  lower bounds on $|q \log 2 - p \log 3|$ are the classical tool here).
- Results ruling out divergent orbits with restricted growth rate, and results
  on the structure of the $3x+1$ function as a dynamical system / measure-
  theoretic problem (Lagarias's survey and annotated bibliography is the
  standard entry point — find and cite it directly rather than relying on
  secondary summaries).
- Generalizations: $qx+r$ maps, the conjecture's undecidability in generalized
  form (a Conway-style result that a broadly analogous class of maps is
  Turing-complete / has undecidable behavior) — relevant context for *why*
  a fully general algebraic proof technique is unlikely to exist, but check
  precisely what was shown undecidable, since it is not this specific map.

## What counts as a result here

In descending order of value, and every one of these is a real contribution:

1. A proof for a natural class of $n$ (e.g. a residue class, a growth-bounded
   family), with the hypotheses stated exactly.
2. A structural theorem about a hypothetical minimal counterexample or
   non-trivial cycle: bounds on cycle length, bounds on the minimum element,
   constraints from Diophantine approximation of $\log 3/\log 2$.
3. A computational verification pushed past whatever the literature reached
   (for either the "every orbit reaches 1 below $N$" bound or the "no
   non-trivial cycle below $N$" bound), with the search space and method
   stated so the bound is checkable.
4. A precise reduction: statement $S$ implies the conjecture (or implies no
   non-trivial cycle exists, or implies no orbit diverges), and $S$ is a
   cleaner problem.
5. A counterexample (a divergent orbit or non-trivial cycle). Extremely
   unlikely given the verified range, and the bar for reporting one is a
   machine-checked, independently reproducible orbit computation.
6. A formalisation in Lean 4 of the statement, and of whichever lemmas are
   proved along the way, with no `sorry`.

Reporting the conjecture as proved, on anything short of a complete argument
that survives adversarial attack, is the one outright failure available on
this run. Reporting Tao's density-one result (or any statistical/almost-all
result) as resolving the conjecture is the specific version of that failure
to watch for here.
