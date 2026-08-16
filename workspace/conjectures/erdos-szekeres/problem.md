# The Erdős–Szekeres conjecture

## Statement

Let $\mathrm{ES}(n)$ be the least integer $N$ such that **every** set of $N$
points in the plane in general position (no three collinear) contains $n$ points
in convex position — that is, the vertices of a convex $n$-gon.

> **Conjecture (Erdős–Szekeres, 1935).** For every $n \ge 3$,
> $$\mathrm{ES}(n) = 2^{n-2} + 1.$$

The function is known to be finite — that is the Erdős–Szekeres theorem (1935),
proved twice in the original paper, once via Ramsey's theorem and once via a
"cups and caps" argument. What is **open** is the exact value. The conjectured
formula is the *Erdős–Szekeres conjecture* and it has resisted since 1935.

## What the statement does and does not say

- **General position** means no three of the $N$ points are collinear. Some
  authors drop this and ask for $n$ points in *strictly* convex position; state
  which convention any formal statement or program uses, because the degenerate
  case changes small values.
- **Convex position** means the $n$ points are exactly the vertex set of their
  own convex hull. The $n$ points need not be consecutive on the hull of the
  whole set, and the remaining $N - n$ points may lie anywhere, inside or
  outside.
- $\mathrm{ES}(n)$ is a *worst-case* quantity: an upper bound $\mathrm{ES}(n)
  \le N$ is a statement about all $N$-point sets, and a lower bound
  $\mathrm{ES}(n) > N$ is a single explicit $N$-point construction with no
  convex $n$-gon.
- The lower bound $\mathrm{ES}(n) \ge 2^{n-2}+1$ is **not** open. Erdős and
  Szekeres (1960) gave a construction of $2^{n-2}$ points in general position
  with no convex $n$-gon. So the conjecture is entirely an *upper bound*
  question: prove $\mathrm{ES}(n) \le 2^{n-2}+1$.
- The problem is sometimes called the *happy ending problem*.

## The obstruction to beat, stated in one place

Every known upper bound is, at bottom, a **Ramsey-type or cups-and-caps counting
argument**, and both are lossy in the same way.

- The original cups-and-caps bound is $\mathrm{ES}(n) \le \binom{2n-4}{n-2}+1
  \approx 4^n/\sqrt{n}$, which is the *square* of the truth. It is tight for the
  cups-and-caps subproblem — $f(k,\ell) = \binom{k+\ell-4}{k-2}$ is exactly
  right — so the loss is not in that lemma but in the reduction *to* it: a set
  with no convex $n$-gon is only forced to avoid cups and caps of a size that
  splits the budget, and the binomial pays for both halves independently.
- The modern improvements shave the exponent's lower-order terms, not the base.
  Getting from $4^{n}$ to $2^{n}$ was the achievement of the 2010s; getting from
  $2^{n+o(n)}$ to the exact $2^{n-2}+1$ requires an argument with **no slack at
  all**, which no counting method has produced.
- The extremal configurations are believed to be essentially unique (the
  Erdős–Szekeres construction, a "compressed" union of $n-1$ sets of sizes
  $\binom{n-2}{i}$). An exact bound therefore has to be a *stability* or
  *uniqueness* statement, not an estimate — and Ramsey-type arguments cannot see
  uniqueness.

Keep that in view: **an argument that ends in an asymptotic improvement to the
$o(n)$ term has not touched this conjecture.** An argument that ends in an exact
statement for a restricted class, or an exact value for one new $n$, has.

## Where the literature is known to have got to

**These are leads to verify, not established facts.** Every one must be checked
against a primary source before anything is built on it, and any that cannot be
found must be recorded as unfound rather than assumed. Names, years and exact
constants below are starting queries and may be wrong.

- **Erdős–Szekeres 1935** ("A combinatorial problem in geometry", Compositio
  Math.): finiteness, the cups–caps lemma $f(k,\ell) = \binom{k+\ell-4}{k-2}$,
  and the bound $\mathrm{ES}(n) \le \binom{2n-4}{n-2}+1$.
- **Erdős–Szekeres 1960**: the lower-bound construction giving
  $\mathrm{ES}(n) \ge 2^{n-2}+1$, conjectured tight.
- **Chung–Graham 1998**, **Kleitman–Pachter 1998**, **Tóth–Valtr 1998/2005**:
  successive subtractions from the binomial, ending at
  $\mathrm{ES}(n) \le \binom{2n-5}{n-2}+1$ (Tóth–Valtr). This stood as the best
  bound for roughly fifteen years and is still the best *binomial-form* bound.
- **Suk 2016** ("On the Erdős–Szekeres convex polygon problem", JAMS):
  $\mathrm{ES}(n) \le 2^{n+o(n)}$, the breakthrough that reached the right base.
  Find the exact error term as published, and the correction if any.
- **Holmsen–Mojarrad–Pach–Tardos**: a refinement of Suk's argument, reportedly
  $\mathrm{ES}(n) \le 2^{n + O(\sqrt{n \log n})}$. Verify the exact form.
- **Exact values.** $\mathrm{ES}(3)=3$, $\mathrm{ES}(4)=5$ (Klein),
  $\mathrm{ES}(5)=9$ (Makai / Kalbfleisch–Kalbfleisch–Stanton),
  $\mathrm{ES}(6)=17$ (**Peters–Szekeres 2006**, a computer-assisted SAT/exhaustive
  proof). $\mathrm{ES}(7)$ is **open**; the conjecture predicts $33$. Find the
  Peters–Szekeres method, its encoding, and its runtime, because it is both the
  oracle model for this run and the evidence about what a $n=7$ attack costs.
  Check whether any later work (SAT solvers, order types, Marić's formal
  verification of the $n=6$ case) has improved the $n=6$ proof or attempted $7$.
- **Order types / realizability.** The finite combinatorial abstraction of a
  planar point set is its *order type* (the chirotope of a rank-3 oriented
  matroid). Convex position is an order-type property, so $\mathrm{ES}(n)$ is
  decidable by finite search over order types — but not every abstract order
  type is realizable by actual points (realizability is $\exists\mathbb{R}$-complete).
  An upper-bound proof over abstract order types is *stronger* than needed and
  may be false; a lower-bound construction must be realized by explicit
  coordinates. Aichholzer's order-type database (all order types up to 11
  points) is the standard computational resource — verify what it covers.
- **Adjacent statements worth separating from this one**: the empty-hexagon /
  Erdős–Szekeres–Horton problem (Gerken, Nicolás, Heule–Scheucher's SAT proof of
  the empty hexagon number 30), the higher-dimensional analogue, the
  monotone-path and cups–caps generalisations, and the "$n$ points in convex
  position with no point inside" variants. Results there do **not** transfer
  automatically. Record which is which.
- The problem carries an Erdős prize; the amount is a fact about its standing,
  not about its mathematics.

## What counts as a result here

In descending order of value, and every one of these is a real contribution:

1. A proof of $\mathrm{ES}(n) \le 2^{n-2}+1$ for a natural restricted class of
   point sets or order types, with the hypotheses stated exactly (e.g. sets in
   convex-layer-bounded position, sets with a bounded number of interior points,
   sets whose order type has a prescribed symmetry).
2. A structural theorem about a hypothetical extremal set: any set of
   $2^{n-2}$ points in general position with no convex $n$-gon must have
   properties $P_1,\dots,P_k$ — layer structure, cup/cap spectrum, forbidden
   subconfigurations, near-uniqueness against the Erdős–Szekeres construction.
   This is the standard route and is what an exact proof is assembled from.
3. A computational result: an independently reproduced verification of
   $\mathrm{ES}(6)=17$ with the encoding stated, or genuine partial progress on
   $\mathrm{ES}(7)$ — for instance an exact value for a restricted subclass on
   32 or 33 points, or a certified lower bound improvement on the search
   frontier, with the search space, symmetry reduction and isomorph rejection
   argued.
4. A precise reduction: statement $S$ implies the conjecture (or implies
   $\mathrm{ES}(n) \le c\cdot 2^n$ for an explicit $c$), where $S$ is cleaner.
5. A quantitative improvement over the published upper bound with a complete
   proof. Extremely unlikely; the bar is a full argument that survives attack.
6. A counterexample — a set of $2^{n-2}+1$ points in general position with no
   convex $n$-gon. Would refute the conjecture. The bar for reporting one is
   exact rational or integer coordinates plus a machine verification, over exact
   arithmetic, that no $n$-subset is in convex position.
7. A Lean 4 formalisation of the statement of $\mathrm{ES}(n)$ and of whichever
   lemmas are proved along the way, with no `sorry`. Note that the
   Erdős–Szekeres theorem's cups-and-caps proof is already in Mathlib in some
   form — check `Mathlib.Combinatorics.Pigeonhole` / the `ErdosSzekeres` file
   (which may be the *monotone subsequence* result, a different theorem with the
   same name) before claiming novelty.

Reporting the conjecture as proved, on anything short of a complete argument
that survives adversarial attack, is the one outright failure available on this
run. The second-worst is reporting an asymptotic bound as if it bore on the
exact conjecture.
