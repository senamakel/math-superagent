# Singmaster's conjecture

## Statement

For an integer `a > 1` let `N(a)` be the number of times `a` appears in
Pascal's triangle:

```
N(a) = #{ (n, k) : 0 <= k <= n,  C(n, k) = a }
```

**Conjecture (Singmaster, 1971).** `N(a)` is bounded above by an absolute
constant. That is, there is a finite `B` with `N(a) <= B` for every `a > 1`.

The conjecture is believed **true**, and `B = 8` is the usual guess because no
number is known to appear more than eight times. The objective here is a proof
or a genuine partial result — a bound, a reduction, or a settled subcase — not
a search for a number with high multiplicity.

## What is elementary and must be established here first

Each of these is easy, and everything downstream leans on them, so each becomes
a claim block verified in this workspace rather than quoted:

- **Every `a > 1` appears at least twice**, since `C(a,1) = C(a,a-1) = a`. So
  `N(a) >= 2` always, and the conjecture is about the *nontrivial* entries.
- **The symmetry `C(n,k) = C(n,n-k)`** means occurrences come in pairs unless
  `k = n/2`. Any count must fix a convention — usually `k <= n/2` — and state
  it. A bound of 8 under one convention is a bound of 4 under the other, and
  confusing them is the easiest way to state a wrong result.
- **`3003` appears eight times**, the record:

```
3003 = C(3003,1) = C(78,2) = C(15,5) = C(14,6)
```

  together with the four mirrored occurrences. Verify this by direct
  computation before relying on it; it is the witness set.

## The structure worth exploiting

Fix `k1, k2 >= 2`. The equation

```
C(x, k1) = C(y, k2)
```

is a polynomial equation in two variables, so it defines an **algebraic
curve**. Its genus grows with `k1, k2`, and:

- for large enough `k1, k2` the genus exceeds 1 and **Faltings** gives finitely
  many rational points, hence finitely many solutions;
- even at genus 1 — the classical small cases — **Siegel's theorem** gives
  finitely many *integral* points, which is what the problem is about.

So for each fixed pair `(k1, k2)` the count is finite. **That is not the
conjecture**, and the gap is the whole difficulty: Singmaster needs a bound
uniform over all `k1, k2` simultaneously, and Faltings and Siegel are both
ineffective in the relevant sense — they give finiteness without a bound
computable in the parameters. State this obstruction in `research/ROOT.md`
before proposing an approach, and say how the approach beats it.

This is the same shape as the constant-size blocker recorded in the
magic-square workspace: a theorem that applies cleanly and yields no usable
number. Expect it, and say early whether the chosen route produces an effective
bound or another ineffective one.

## Why a naive bound is not enough

`N(a) = O(log a)` is classical and the exponent has been improved several
times, but every such bound **grows with `a`**, and the conjecture asserts a
constant. A run that reproduces a `log`-type bound has reproduced known work; a
run that shows the growth can be removed under a stated hypothesis has done
something.

## Leads — verify each before relying on it

Not established facts here. Each needs a primary source and its own claim block
with an explicit status. Several of the attributions below are from memory and
**may be wrong in detail** — treat the names as search keys, and record what
the sources actually say.

- **Singmaster (1971)** — the original, with the first `O(log a)` bound.
- **Abbott, Erdős and Hanson** — an improvement of the form
  `O(log a / log log a)`. Get the exact statement and constant.
- **Kane** — a further improvement. Find the current record and its shape.
- **Matomäki, Radziwiłł, Shao, Tao and Teräväinen**, *Singmaster's conjecture
  in the interior of Pascal's triangle* — the modern breakthrough, bounding the
  count in an interior range of `k`. This is likely the single most useful
  source: get the exact theorem, the range of `k` it covers, the constant, and
  precisely which part of the triangle it leaves open.
- **The infinite family with multiplicity at least 6.** There is a known
  Fibonacci-indexed identity producing infinitely many `a` with `N(a) >= 6`.
  Find it, verify it computationally, and record it — it is the reason `B >= 6`
  and it constrains any proposed proof.
- **de Weger, and work on `C(x,2) = C(y,k)`** — the small-`k` curves treated
  explicitly, where effective methods do apply.

## The realistic target

Proving Singmaster outright is not expected. What is reachable:

- the exact statement of what MRSTT leaves open, with the boundary made
  precise;
- an **effective** bound for a specific `(k1, k2)` family where Baker's method
  on linear forms in logarithms applies, with the constant computed rather than
  cited as existing;
- a proof that some stated approach *cannot* give a uniform bound, with the
  obstruction named.
