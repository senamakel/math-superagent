# What ends this run, and what counts as a result

## The one thing this run must not do

**Do not search for a sixth unitary perfect number.** Not to `10^12`, not to
`10^50`, not "further than before", not "with a better sieve", and not as a
warm-up while you think. Wall searched past `10^102` in 1975 and found nothing.
Any bound this container can reach is smaller than that by scores of orders of
magnitude, so a search here cannot produce a positive result and cannot produce
a negative one that is not already known. It is the degenerate move this problem
offers, it will consume the run, and a capture reporting "no unitary perfect
number below `10^N`" for any `N` you can reach is worth **nothing**.

The same goes for the product form `Π (1 + 1/p^a) = 2`. It makes a structural
backtracking search look tractable — the denominator rule forces the next prime
whenever the remaining target is not an integer, so the tree looks thin. The
operator wrote that search, ran it, and it recovers exactly the five known
numbers within any bound reachable here. It is recorded in
`research/notes/why-the-search-is-closed.md` **as a closed route**, not as an
instrument. Reproducing it is the one guaranteed waste available.

The deliverable is a **structural theorem or a genuine partial result stated
exactly**. This conjecture is Subbarao's and has been open since 1966.

## What would count

- **A bound on `H_even`**, the set of even `m` for which every prime divisor of
  `2^m + 1` is 3-Higgs. arXiv:2605.20475 leaves this as the single remaining
  branch and proves only the counting bounds `|H_even ∩ [2,40000]| ≤ 201` and
  `|H_even ∩ [2,50000]| ≤ 272`. Finiteness of `H_even`, a density statement, or
  a proof that a stated approach cannot reach it, all count. So does a
  *correction* to those bounds.
- **Progress on the divisor-level problem for `Φ_{4p}(2)`** that the same paper
  names as the analytic target for closing the branch. State what a solution
  would give and what it would not.
- **An impossibility lemma for a structural class**, run against the witness set
  (see the oracle below). Extending Graham's squarefree-odd-part theorem to a
  named larger class — bounded odd exponents, bounded `ω`, a congruence class of
  `a` — counts. "Any sixth example has property X" counts if X is proved.
- **A sharpening of the 2-adic budget.** This workspace already proves the exact
  identity `Σ_i v2(p_i^{e_i} + 1) = a + 1` and its corollary `ω(odd part) ≤ a+1`
  (`research/notes/parity-and-2-adic-budget.md`, checked against all five). A
  *lower* bound on `a` in terms of `ω`, or a proof that some residue class of
  `a` is impossible, is real progress. Re-deriving the identity is not.
- **A resolution of whether 3 | n is forced.** All five known examples are
  divisible by 3 and nobody has proved a sixth must be. Either direction is a
  result.
- **A located error** in arXiv:2605.20475, Graham 1989, Subbarao–Warren 1966 or
  Wall 1975 — with the specific step named.

A result stated without the hypothesis it was established under is not a result.
A bound verified for `a ≤ 10000` is a statement about `a ≤ 10000`.

## The oracle: an exact check and a witness set

There is no value to compute; the answer is a proof. So the oracle is a
falsifier.

1. **`sigma_star(n)`** — factor `n`, return `Π (p^a + 1)` over `p^a || n`, in
   exact integer arithmetic, no floats. `n` is unitary perfect iff
   `sigma_star(n) == 2*n`. Verify it by hand on `6` and on a number that is not
   unitary perfect before trusting anything built on it.

2. **The witness set is the five known numbers.**

   ```
   6, 60, 90, 87360, 146361946186458562560000
   ```

> **Every claimed obstruction must be run against all five.** A lemma that
> forbids `90 = 2 · 3^2 · 5` or the `5^4` component of the fifth example is
> false. Record it as **refuted**, not as "needs adjustment". A lemma not run
> against the five is `asserted`, never `checked`.

The two non-squarefree kernels `3^2` (in 90) and `5^4` (in the fifth) are the
sharpest part of the witness set, because Graham's theorem says any sixth
example must have a kernel of that kind. An argument that kills all repeated odd
prime powers kills two of the five known numbers and is wrong.

## Compute policy

Compute is for **checking a structural claim**, not for finding `n`.

- Legitimate: factoring `2^m + 1` for `m` in a stated range to test a property
  of `H_even`; computing `Φ_{4p}(2)` and its divisors; verifying a proposed
  impossibility lemma against the witness set; reproducing a table from
  arXiv:2605.20475 to check it.
- Illegitimate: enumerating `n` and testing `σ*(n) = 2n`; backtracking over
  prime-power products to hunt for a solution; extending either "further".

Factoring `2^m + 1` gets hard fast and it is the real cost centre here. Bound
every run as
`timeout 540 python3 <prog> 2>&1 | tee code/out/<name>.captured.txt; echo EXIT_CODE=$?`
and say in the capture what range was covered and what was left unfactored. A
partial factorisation with its bound stated is a result; an unbounded run that
is killed is not. The box has 28 CPUs and the container has no CPU quota, so
split `m` ranges across workers and say how many ran.

## The trap specific to this problem

An argument that shows unitary perfect numbers are **rare** — density zero,
counting function `o(x)`, `O(x^ε)` — has proved something true and almost
certainly already known, and has not touched the question, which is finiteness.
Rarity is not finiteness. Say which one you have.

The second trap is the seductive one: the product identity `Π(1 + 1/p^a) = 2`
is exact and elementary, so it invites an elementary attack. Every such attack
that has been tried reduces to a search. Before pursuing one, say what it does
that a search does not.

## Ending

Stop and report when you have a partial result of the kind listed above, or when
you can state precisely what blocks **the route you actually pursued** and why.
Report the five witnesses reproduced through your own oracle, the evidence class
of every claim, and — if you are stopping on a blocker — which of the listed
results you attempted and what defeated each.

"No sixth unitary perfect number below `10^N`" does not end this run, at any
`N`. Neither does re-deriving the 2-adic budget identity or the non-existence of
odd unitary perfect numbers; both are already proved and written down here.
