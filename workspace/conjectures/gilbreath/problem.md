# Gilbreath's conjecture

## Statement

Let `A_0 = (2, 3, 5, 7, 11, 13, 17, ...)` be the primes in order. Define

```
A_{k+1}(i) = | A_k(i) - A_k(i+1) |
```

the row of iterated absolute differences.

**Conjecture (Gilbreath, 1958; Proth, 1878).** For every `k >= 1`, the first
entry of `A_k` is `1`.

```
A_0 :  2  3  5  7 11 13 17 19 23 29 31 ...
A_1 :  1  2  2  4  2  4  2  4  6  2 ...
A_2 :  1  0  2  2  2  2  2  2  4 ...
A_3 :  1  2  0  0  0  0  0  2 ...
A_4 :  1  2  0  0  0  0  2 ...
```

The conjecture is believed **true** and has been verified to enormous depth.
The objective here is a proof or a genuine partial result — not another
verification sweep.

## The real content, stated exactly

The leading `1` is **not** the hard part, and seeing why is the first thing to
establish.

`2` is the only even prime, so every difference `p_{i+1} - p_i` with `i >= 2`
is even, and `3 - 2 = 1` is odd. So `A_1 = (1, even, even, ...)`. Now induct:
if `A_k = (1, e_1, e_2, ...)` with every `e_j` even, then

```
A_{k+1}(0) = |1 - e_1|   and   A_{k+1}(j) = |e_j - e_{j+1}| is even for j >= 1
```

so the shape `(odd, even, even, ...)` is preserved, and

> **`A_{k+1}(0) = 1` if and only if `e_1 ∈ {0, 2}`.**

If ever `A_k(1) = 4`, the next row starts with `3` and the conjecture dies.
**So the entire conjecture is the statement that the second entry of every row
is 0 or 2.** Everything else is bookkeeping. Any write-up that does not put
this at the centre has not understood the problem.

## Odlyzko's observation, and why this is not about primes

**Odlyzko (1993)** made the decisive structural remark, and it must be verified
here before being relied on:

- If a row begins with `1` followed by a block of length `n` all of whose
  entries lie in `{0, 2}`, then the next `≈ n/2` rows all begin with `1`. The
  `{0,2}` structure is self-propagating for a while, and it degrades only at
  the rate the block shortens.
- Consequently the conjecture reduces to showing rows keep entering the `{0,2}`
  regime, which is a statement about **any** sequence starting `2` followed by
  odd numbers with sufficiently small gaps — not about primality.

That last point is the honest framing: **Gilbreath's conjecture is very likely
not a theorem about primes at all.** It is a combinatorial/dynamical statement
about the absolute-difference operator on sequences of this shape, and the
primes merely supply an instance. An approach that leans on deep prime
distribution is probably attacking the wrong object; an approach that proves it
for a general class of sequences would settle it for primes as a corollary.

State this in `research/ROOT.md` and say which side the run's approach is on.

## The obstruction, stated honestly

The `{0,2}` block shrinks. Odlyzko's argument gives `≈ n/2` rows of protection
from a block of length `n`, so protection is consumed geometrically, and each
new stretch of `{0,2}` must be **regenerated** by the rows below. Nobody has
proved that regeneration always happens.

This is where every attempt stops. A proof must either

- show the regeneration rate exceeds the consumption rate, with an explicit
  mechanism, or
- find an invariant of the difference operator that forces `A_k(1) ∈ {0,2}`
  directly, without tracking blocks.

Say which of these the approach attempts, and what makes it able to beat the
consumption/regeneration balance.

## Leads — verify each before relying on it

Not established facts here. Each needs a primary source and its own claim block
with an explicit status.

- **Odlyzko (1993)**, *Iterated absolute values of differences of consecutive
  primes* — the verification to large depth and the `{0,2}`-block argument.
  Get the exact statement of the block lemma and the constant in `≈ n/2`.
- **Proth (1878)** — claimed a proof; it is regarded as flawed. If the paper or
  a description of the argument is reachable, **locate the error and record it
  as a refuted claim.** A located error in a claimed proof is a genuine result.
- **Killgrove and Ralston (1959)** — early verification.
- **Generalisations** — the conjecture is stated for other sequences
  (Gilbreath-like sequences); results there are the ones most likely to
  transfer, since the problem is probably not about primes.
- **Verification depth** — reported bounds vary. State the depth this run
  actually reproduces separately from what the literature claims.
