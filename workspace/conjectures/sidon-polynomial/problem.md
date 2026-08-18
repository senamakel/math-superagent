# Is some integer polynomial a Sidon set?

*Erdős Problem #324 (erdosproblems.com/324), from Erdős–Graham [ErGr80, p.53].
Erdős and Graham describe it as "very annoying".*

## Statement

> **Question.** Does there exist a polynomial `f(x)` in `Z[x]` such that all the
> sums
>
> ```
> f(a) + f(b),      a < b nonnegative integers,
> ```
>
> are distinct?

Equivalently: is the image `{ f(n) : n >= 0 }` a **Sidon set** (a `B_2` set) —
a set in which every element has at most one representation as an unordered sum
of two of its members?

## What the statement does and does not say

- Distinctness is over **unordered pairs `a < b`**. The trivial coincidence
  `f(a) + f(b) = f(b) + f(a)` is excluded by the ordering, and nothing else is.
- Written out, the condition is: **the only integer solutions of**
  ```
  f(a) + f(b) = f(c) + f(d),      0 <= a < b,  0 <= c < d
  ```
  **are `(a,b) = (c,d)`.** That is a Diophantine statement, and it is the form
  every computation and every Lean statement in this run should use.
- `f` need not be monic, need not have positive leading coefficient on the
  relevant range, and its degree is not prescribed. But `f` must be injective on
  a cofinite set for the question to have content, so the degree matters and
  low degrees are provably impossible (below).
- The problem asks only for **existence of one such `f`**. A single verified
  polynomial closes it. That asymmetry is the reason this problem is worth a
  computational run: the positive side is witnessed, the negative side is a
  theorem about all polynomials.

## Where the literature is known to have got to — verify each

Nothing below may be cited without a primary source and a claim block. Every
degree bound below should be **re-proved in this workspace**, because they are
small and they are the calibration for everything else.

- **Degree 1 fails**, trivially: `f(a)+f(b)` depends only on `a+b`.
- **Degree 2 fails.** "It is easy to check that a quadratic `f` cannot have this
  property." Re-derive it — the identity that kills it is short, and finding it
  tells you what shape of obstruction to look for in general.
- **Degree 3 fails.** Dubickas and Novikas [DuNo21] proved no cubic works.
  Get their argument; it is the deepest *negative* result available and it is
  the template for degree 4 and beyond.
- **`x^4` fails**, classically — `a^4 + b^4 = c^4 + d^4` has nontrivial solutions
  (the smallest is famous and small). **Find it with the oracle before reading
  it anywhere.** Note this kills the *monomial* `x^4`, not every quartic; whether
  some other quartic works is a separate question the run should state clearly.
- **`x^5` is believed to work.** The Lander–Parkin–Selfridge conjecture would
  imply `f(x) = x^n` has the property for every `n >= 5`. So the conjecture is
  believed true, conditionally, with an explicit witness — and the open problem
  is to prove *some* `f` works unconditionally.
- **Ruzsa [Ru01b]** proved there exists `c` in `[0,1]` and `n_0 >= 1` such that
  ```
  { n^5 + floor(c * n^4) : n >= n_0 }
  ```
  is a Sidon set. **This is the strongest known result and it is the one to
  understand first.** Note what it does and does not give: an *existence* of a
  real parameter `c`, not an effective one, and a set that is the image of an
  integer sequence rather than of a polynomial in `Z[x]`. **Whether Ruzsa's
  theorem can be made effective, or made to produce an actual polynomial, is the
  most promising line available here** — say exactly what stands in the way.
- Guy's collection [Gu04], problems C9, D1, F30, for the surrounding equations.

## The obstruction, stated honestly

1. **The believed witness is conditional on a famous open conjecture.** `x^5`
   almost certainly works, and proving it would prove a case of
   Lander–Parkin–Selfridge, which is far out of reach. **So a run that sets out
   to prove `x^5` works has chosen the hardest possible route to the answer.**

2. **Ruzsa's route avoids that, by not fixing the polynomial.** The gain is that
   a free parameter can be tuned to destroy collisions. The loss is
   non-effectivity, and the fact that `n^5 + floor(c n^4)` is not a polynomial
   in `Z[x]` unless `c` is rational with small denominator — in which case the
   argument may not survive. **Understanding whether some rational `c` works is
   a concrete, computable question, and it is the natural first target of this
   run.**

3. **Low degrees fail for structural reasons that do not extend.** The
   quadratic and cubic obstructions come from identities/parametrisations that
   produce infinitely many collisions. No such identity is known for degree
   `>= 5`, and the absence of an identity is not a proof.

Stated as the thing to beat:

> **Either produce an explicit `f` in `Z[x]` and prove `f(a)+f(b)=f(c)+f(d)`
> forces `(a,b)=(c,d)` — which for a monomial means proving a case of
> Lander–Parkin–Selfridge — or make Ruzsa's parametrised construction effective
> and land it inside `Z[x]`.**

Say which of these the approach is. An approach assuming
Lander–Parkin–Selfridge has produced a **conditional** result and must label it
so, with the hypothesis stated exactly.

## The oracle: a collision search, and the falsifier that matters

1. **`collisions(f, N)`** — all `(a,b,c,d)` with `0 <= a < b <= N`,
   `0 <= c < d <= N`, `(a,b) != (c,d)`, and `f(a)+f(b) = f(c)+f(d)`. Exact
   integer arithmetic only; **never floating point** — `f(n)` for degree 5 and
   `n ~ 10^6` overflows a double long before the search gets interesting, and a
   float comparison reports collisions that do not exist and misses ones that
   do. Implement by hashing the `O(N^2)` sums, and **report the `N` reached and
   the runtime.**

2. **Calibration, before any new polynomial is tried.** The oracle must, on its
   own, find:
   - infinitely many collisions for every quadratic (report the family);
   - a collision for `x^3` and for `x^4` (both exist and are small);
   - **no** collision for `x^5` up to the largest `N` reached.
   A search that does not rediscover the `x^4` collision is broken, and every
   number it later reports is worthless.

3. **`sweep(D, H, N)`** — search every `f` in `Z[x]` of degree `<= D` with
   coefficients bounded by `H` for a collision below `N`, and report the ones
   that survive. This is the run's own experiment, and its output — which
   low-height polynomials of degree 4 and 5 survive, and how the survivors are
   structured — is the kind of data that suggests a construction. **Ruzsa's
   `n^5 + floor(c n^4)` says to look hard at degree 5 with a nonzero `x^4`
   coefficient; sweep exactly there.**

4. **The falsification oracle.** Any claimed proof that "no polynomial of degree
   `d` works" must be run against every surviving degree-`d` polynomial from the
   sweep, and any claimed witness `f` must survive `collisions(f, N)` at the
   largest feasible `N` before it is written down as anything. **A claimed
   witness that collides is refuted, not weakened.**

Note the direction of danger. The conjecture asserts *existence*, so the
characteristic failure here is a **false witness** — a polynomial declared Sidon
on a search that was too short or done in floating point. Every witness carries
the `N` it survived and the arithmetic it was checked in.

## Leads — verify each before relying on it

- **Ruzsa [Ru01b]** in full: the construction, why `c` is non-effective, and
  what would make it effective.
- **Dubickas–Novikas [DuNo21]**: the cubic obstruction, and whether the method
  says anything about quartics.
- **Lander–Parkin–Selfridge**, its exact statement, and precisely which case
  `x^5` needs.
- **`a^4 + b^4 = c^4 + d^4`** and `a^5+b^5=c^5+d^5`: the classical solution
  theory, the parametrisations that exist for degree `<= 4`, and the searches
  that have found none for degree `5`. Record the bound those searches reached.
- **Sidon sets from polynomial images** more generally — perfect difference sets,
  Singer/Bose constructions, and Sidon sets in `Z` of polynomial growth. The
  question here is whether *polynomial* image can be Sidon; what is known about
  the growth rate of Sidon sets bounds what a witness could look like.
