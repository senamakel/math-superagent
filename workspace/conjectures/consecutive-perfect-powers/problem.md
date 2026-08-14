# Consecutive perfect powers

## Statement

Call an integer a **perfect power** if it is `x^p` for integers `x >= 1` and
`p >= 2`. The perfect powers begin

```
1, 4, 8, 9, 16, 25, 27, 32, 36, 49, 64, 81, 100, 121, 125, 128, 144, ...
```

Two of them differ by `1`: `8 = 2^3` and `9 = 3^2`.

> **Question.** Are there any others? Equivalently, determine all solutions in
> integers of
>
> ```
> x^p - y^q = 1,     x, y > 0,     p, q > 1.
> ```

`(x, p, y, q) = (3, 2, 2, 3)` is one. **It is believed to be the only one, and
this has not been proved.** Proving it, or exhibiting a second solution, is the
objective.

## What the statement does and does not say

- `x, y > 0` and `p, q > 1`. The degenerate readings — `1^p - 0^q`, or exponent
  `1` — are excluded, and excluding them is the whole reason the question has
  content.
- It suffices to consider **prime** `p` and `q`. If `p = ab` then
  `x^p = (x^a)^b`, so any solution with composite exponents yields one with
  prime exponents. Establish this reduction here; everything downstream assumes
  it.
- The case `p = 2` or `q = 2` is **not** the general case, and it is not open.
  `x^2 - y^q = 1` and `x^p - y^2 = 1` are classical and were settled long ago by
  elementary factorisation in `Z` and in `Z[i]`. Re-derive both — they are the
  base of everything and they show what the difficulty is *not*.
- The difficulty is therefore entirely in **`p, q` both odd primes**.

## Where the literature is known to have got to

Three results, each to be verified rather than cited.

**The exponent-2 cases are closed.** `x^2 - y^q = 1` has only `3^2 - 2^3`; the
proof factors `y^q = (x-1)(x+1)` and uses that the two factors are nearly
coprime. `x^p - y^2 = 1` has no solutions with `p` odd. Both are within reach of
this workspace and should be redone in it.

**The number of solutions is finite, effectively.** There is an effective upper
bound: any solution has `max(x, y, p, q)` below an explicitly computable
constant. The bound comes from the theory of linear forms in logarithms and it
is **astronomically large** — far too large to be exhausted by any computation
that will ever be run. So the problem is "solved" in the sense that a finite
check would settle it, and this is worth nothing in practice. Do not propose
closing the gap by computation; say what the bound actually is and how many
orders of magnitude separate it from feasibility.

**There are strong necessary conditions on a hypothetical second solution.** A
solution with `p, q` odd primes forces divisibility relations linking `p`, `q`,
`x` and `y` — relations of the shape "`p^2` divides `y^{p-1} - 1`" and its
mirror. Conditions of this kind are what have driven every computational search,
and searches have confirmed no second solution for all exponent pairs below very
large bounds.

Reconstruct these conditions here. **The exact form of the divisibility
relations, and what they cost to verify, is the most useful single thing this
run can establish early**, because everything else is measured against them.

## The obstruction, stated honestly

Three things are true at once, and together they say where the problem is.

1. **The elementary factorisation method works when an exponent is `2` and stops
   dead when both are odd.** With `p = 2`, `x^2 - 1` factors over `Z`. With both
   exponents odd there is no factorisation in `Z`, and one has to work in
   `Z[zeta_p]`, the ring of integers of the `p`-th cyclotomic field. That is
   where the problem actually lives.

2. **In the cyclotomic setting the obstruction is the class group.** The
   equation forces an ideal factorisation, and turning an ideal relation into an
   element relation requires the relevant ideal to be principal. It need not be.
   Everything hard about this problem is the failure of unique factorisation,
   and every partial result is a way of controlling it — by bounding the class
   number, by working in a subfield where it is better behaved, or by finding a
   relation that survives the ambiguity.

3. **The effective bound and the computational searches approach each other far
   too slowly to meet.** The gap is not going to be closed from both ends. A
   proof has to be structural.

Stated as the thing to beat:

> **A proof must control the arithmetic of `Z[zeta_p]` well enough to convert
> the ideal relation forced by the equation into an element relation — without
> assuming anything about class numbers that is not proved.**

Say which of these the approach attempts. An approach that reduces to a
statement about class numbers has not finished; it has produced a new
conditional statement, which may still be a result, but it must be labelled
conditional and the hypothesis stated exactly.

## The oracle is a search over a bounded box and a falsifier

There is no value to recompute — the deliverable is a proof — but there is a
cheap and essential mechanical check.

1. **`solutions(N)`** — all `(x, p, y, q)` with `x^p, y^q <= N` and
   `x^p - y^q = 1`. Exact integer arithmetic only; no floating point anywhere,
   because `x^p` overflows a float long before `N` gets interesting and a float
   comparison will report false solutions. Must return exactly `(3,2,2,3)` for
   every `N >= 9` the run can reach. **Report the `N` actually reached and the
   runtime.**

2. **`check_conditions(p, q)`** — a direct verification of the necessary
   divisibility relations for a given exponent pair, used to confirm that the
   reconstructed conditions are the right ones. Test them against `(2,3)`, the
   known solution, which must satisfy them.

3. **The falsification oracle, which is the one that matters.**

> **Every claimed lemma must be run against the known solution `3^2 - 2^3 = 1`.**
> A lemma implying there are *no* solutions with `p, q > 1` is false, because
> there is one. This is the single most effective check available here and it
> catches the characteristic failure of this problem: an argument that proves
> too much because it silently assumed both exponents odd, or silently divided
> by something that vanishes in the known case.

The asymmetry to note: the conjecture asserts a **negative** — no second
solution — so the dangerous failure is an argument that appears to eliminate all
solutions, including the one that exists. Every lemma must state where the known
solution sits relative to it.

## Leads — verify each before relying on it

Not established facts here. Each needs a primary source and its own claim block
with an explicit status.

- **The exponent-2 cases**, both of them, with full proofs redone here. The
  cheapest real content available and the calibration for everything else.
- **The reduction to odd prime exponents.** Small, and it must be airtight.
- **The effective bound from linear forms in logarithms.** Get its actual
  statement and its actual size. The point of establishing it is to show that
  computation cannot finish the job.
- **The divisibility conditions** on a hypothetical solution. Get the exact
  form, verify them computationally for many exponent pairs, and record the
  bound to which searches have confirmed no second solution.
- **Cyclotomic fields `Q(zeta_p)`**: rings of integers, units, the cyclotomic
  units, class numbers, and the split of the class number into its two factors.
  This is the machinery the problem lives in, and the run should build a working
  knowledge of it rather than treating it as a black box.
- **Related equations** — differences of perfect powers equal to a fixed
  constant other than `1`, and the general question of gaps between perfect
  powers. Results there are the ones most likely to transfer, and they indicate
  which techniques have any power at all.
