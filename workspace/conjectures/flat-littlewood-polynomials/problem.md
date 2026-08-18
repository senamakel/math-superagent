# Flat Littlewood polynomials: is the sup norm always $(1+c)\sqrt n$?

*Erdős Problem #1150 (erdosproblems.com/1150), from [Ha74, 4.31] and [Va99, 2.36].*

## Statement

A **Littlewood polynomial** of degree `n` is

```
P(z) = a_0 + a_1 z + ... + a_n z^n,      every a_k in {-1, +1}.
```

Write `||P||_inf = max_{|z|=1} |P(z)|` for its supremum over the unit circle.

> **Question.** Does there exist a constant `c > 0` such that, for all large `n`
> and **every** Littlewood polynomial `P` of degree `n`,
>
> ```
> max_{|z|=1} |P(z)|  >  (1 + c) sqrt(n) ?
> ```

Equivalently, and this is the phrasing to keep in mind: **is there no
"ultraflat" polynomial with `±1` coefficients?** A family would be ultraflat if
`||P_n||_inf / sqrt(n) -> 1`.

## What the statement does and does not say

- The `L^2` norm is forced. By Parseval, for every Littlewood polynomial of
  degree `n`,
  ```
  (1/2pi) * integral_{|z|=1} |P(z)|^2 = n + 1,
  ```
  so `||P||_inf >= sqrt(n+1) > sqrt(n)` **trivially**. The conjecture asks for a
  *constant factor* above that trivial floor. Re-derive the Parseval identity in
  this workspace before anything else; it is the calibration for every number
  the run computes.
- The quantifier is over **all** `P`. A construction that is flat is a
  counterexample; a bound that holds for all `P` is the theorem. The run must do
  both — hunt the flat family as seriously as the lower bound.
- Coefficients are exactly `±1`. The same question with coefficients **anywhere
  on the unit circle** has answer *yes, ultraflat families exist* (Kahane); the
  entire difficulty is the discreteness of `{-1,+1}`. An argument that never uses
  discreteness cannot be right, because it would contradict Kahane.
- `n -> infinity` asymptotics. Small `n` is finite and exactly computable, and it
  is the only ground truth available. Compute it.

## Where the literature is known to have got to — verify each

Nothing below may be cited without a primary source and a claim block.

- **The trivial lower bound `sqrt(n+1)`** from Parseval. Cheap, exact, and the
  baseline every computed number is measured against.
- **Kahane's ultraflat polynomials**, with unimodular (not `±1`) coefficients,
  achieving `(1+o(1))sqrt(n)` uniformly. This is the result that says the
  problem is about discreteness. Get its exact statement.
- **Rudin–Shapiro polynomials**: an explicit `±1` family with
  `||P||_inf <= sqrt(2) * sqrt(n+1)`. This is the best explicit upper bound and
  it is a *long* way from `1 + c`. Reconstruct the recursion here and verify the
  bound numerically — the recursion is two lines and the verification is exact.
- **Recent flatness results** (Balister–Bollobás–Morris–Sahasrabudhe–Tiba and
  successors) constructing `±1` polynomials with `||P||_inf <= C sqrt(n)` and
  `||P||_inf >= c sqrt(n)` simultaneously — "flat" in the two-sided sense but
  with constants far from `1`. Establish exactly which constants are achieved,
  because they bound how much room the conjecture has left.
- **The `L^4` route.** `||P||_4^4` is a finite sum of autocorrelation squares and
  is *exactly computable*, and `||P||_inf >= ||P||_4`. The **merit factor**
  literature (Golay, Littlewood, Turyn) is exactly the study of how small
  `||P||_4` can be, and the record asymptotic merit factor is a specific finite
  number. Get it: it converts directly into a lower bound of the shape
  `(1+c)sqrt(n)` with an explicit `c`, and **this is the most likely place a
  genuine partial result of this run lives.**

## The obstruction, stated honestly

Three facts pin the difficulty.

1. **`L^2` gives exactly `sqrt(n)` and nothing more.** Any argument that only
   uses the mean square is finished at the trivial bound. The gain must come
   from `sup` exceeding the mean, i.e. from a *variance* or a *higher moment*.

2. **The `L^4` route gives a constant, but the wrong one.** `||P||_4 >= ||P||_2`
   with equality impossible, and the merit-factor record turns into
   `||P||_inf >= (1 + c_0)sqrt(n)` for a specific small `c_0` — *if* the merit
   factor is bounded. Whether the merit factor can go to infinity is itself open
   (Littlewood's problem), and if it can, the `L^4` route yields nothing. So:
   **the `L^4` route is conditional on a second open problem.** Say so whenever
   using it.

3. **Kahane forbids any soft argument.** Unimodular coefficients admit ultraflat
   families, so no argument using only `|a_k| = 1` can work. The proof must see
   that `a_k` lies in a two-point set — via an integrality, a parity, a
   character-sum, or a counting argument over `2^{n+1}` sign patterns.

Stated as the thing to beat:

> **A proof must extract a constant-factor gain over the `L^2` bound from a
> quantity that is sensitive to the discreteness of `{-1,+1}`, without routing
> through an unbounded-merit-factor assumption.**

Say which of the three the approach is on. An approach reducing to "the merit
factor is bounded" has produced a *conditional* result, which is still a result
and must be labelled as such with the hypothesis stated exactly.

## The oracle: exact sup norms, and a falsifier

`||P||_inf` for a fixed `P` is a computable real number, and the minimum over
all `2^{n+1}` sign patterns is a finite computation for small `n`. Build both.

1. **`supnorm(P)` — certified.** `|P(e^{i t})|^2` is a real trigonometric
   polynomial of degree `n`; its maximum can be located exactly by finding the
   real roots of its derivative (a polynomial system, exact over `Q`) rather
   than by sampling. **A sampled maximum is a lower bound only, and a run that
   reports a sampled value as `||P||_inf` has reported a number that is not the
   one in the conjecture.** Sampling on a fine FFT grid is fine as a *search*
   heuristic; every published number must be certified.

2. **`m(n) = min over all 2^{n+1} sign patterns of ||P||_inf`**, exactly, for as
   many `n` as reachable (symmetry: negation and reversal, so the search is over
   `2^{n-1}` classes). **Report the largest `n` reached, the method, and the
   runtime.** Then `m(n)/sqrt(n)` is the sequence the conjecture is about, and
   whether it is bounded away from `1` is visible in it.

3. **`L4norm(P)` exactly**, from the autocorrelations — an `O(n^2)` exact integer
   computation, no analysis. This gives a certified lower bound on `||P||_inf`
   for free and is the cheapest real evidence available here.

4. **The falsification oracle.** Every claimed lower bound `||P||_inf >= g(n)`
   must be evaluated against the exact minimisers from (2) and against the
   Rudin–Shapiro family. **A claimed bound exceeding a computed `m(n)` is false —
   record it refuted, not weakened.** In the other direction, any claimed flat
   family must be run through (1) at several `n` before its asymptotics are
   believed.

Expect `m(n)/sqrt(n)` at small `n` to be uninformative about the asymptotic
constant. Compute it anyway: it is the only thing standing between the run and a
plausible false theorem.

## Leads — verify each before relying on it

- **Merit factor** `F(P) = (n+1)^2 / (||P||_4^4 - (n+1)^2)`, its known records
  (Rudin–Shapiro, Legendre-symbol rotations, Turyn's `F -> 6.34...`), and the
  exact conversion from a merit-factor bound to a constant `c`.
- **Autocorrelation formulation.** `||P||_4^4` in terms of aperiodic
  autocorrelations; the low-autocorrelation binary sequence (LABS) literature,
  which has exact optimal values tabulated far beyond brute force.
- **Rudin–Shapiro** recursion, its exact sup-norm behaviour, and whether its
  `||P||_inf/sqrt(n)` converges.
- **Kahane's theorem** and precisely where its construction needs the full
  circle rather than two points.
- **The `±1` flat-polynomial construction of Balister et al.**, its constants,
  and what it rules out.
- **Random `±1` polynomials**: the typical size of `||P||_inf` is
  `~ sqrt(n log n)`, far above `sqrt n`. So a flat family, if it exists, is
  exponentially rare — which is why search must be structured, not random.
