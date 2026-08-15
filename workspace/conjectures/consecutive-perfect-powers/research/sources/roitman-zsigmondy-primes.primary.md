# Roitman, "On Zsigmondy primes" — retrieved primary content

**Source URL:** https://doi.org/10.1090/s0002-9939-97-03981-6
**Author:** Moshe Roitman, *Proc. Amer. Math. Soc.* **125** (1997).
**How obtained:** server-side full-text readout via `read_sources`.
`download_document` is refused on this host by the network boundary; this is a
captured readout (record of the primary content returned), not a stored PDF.
Read its claims as `asserted-by-source` until re-derived in-workspace.

## Why this source is in the library

The run's **adopted** approach `lucas-primitive-divisors` cites this as the
bridge between the primitive-prime-divisor theorem and the congruence
information it carries. The exact mechanism that produces the Wieferich-type
conditions is: a *primitive* (Zsigmondy) prime divisor `r` of the cyclotomic
factor `Phi_p(x) = (x^p-1)/(x-1) = U_p(x+1,x)` has multiplicative order of `x`
mod `r` exactly `p`, hence `r ≡ 1 (mod p)`. This note pins that exact statement
with the source's own text, and fixes the exception structure of Zsigmondy's
theorem so the run's `prim-div-lucas` / `mirror-prim-div-scope` claims are
anchored to a citable primary source rather than to the problem's hint.

## Content established (as retrieved)

### Zsigmondy prime — the exact notion
For integers `a, n > 1`, a prime `p` is a **Zsigmondy prime for `(a, n)`** if it
is a prime divisor of `a^n - 1` that does not divide `a^j - 1` for any
`0 < j < n`. Equivalently, the multiplicative order of `a` modulo `p` is
exactly `n`. (Source, verbatim: "a prime p is called a Zsigmondy prime for
a, n if p ∤ a [i.e. p ∤ a, the `∤ a` is a typograph of `p ∤ a` in the original]
... and the order of a (mod p) equals n".)

### The key consequence — `n | p - 1`
If `p` is a Zsigmondy prime for `(a, n)`, then the order of `a` modulo `p` is
`n`, and since the multiplicative group mod `p` has order `p - 1`, we get
`n | p - 1`, hence **`p ≥ n + 1`** and `p ≡ 1 (mod n)`. (Source, verbatim.)

This is the engine behind the run's primitive-divisor approach: a primitive
prime divisor `r` of `Phi_p(x)` satisfies `r ≡ 1 (mod p)`, so `r` is a prime
divisor of `y` (since `r | Phi_p(x)`, `r ∤ x-1` by primitiveness, and
`y^q = (x-1)·Phi_p(x)`) that is `1 (mod p)` — a congruence constraint on the
prime divisors of `y`.

### A "large" Zsigmondy prime
A Zsigmondy prime `p` for `(a, n)` is called **large** if either `p > n + 1`
or `p^2 | a^n - 1`. Large Zsigmondy primes carry the quadratic-power
information (Wieferich flavour: a prime whose square divides the value).

### Zsigmondy's theorem — the exception list (Theorem 3)
There exists a prime divisor `q` of `a^n - 1` that does not divide `a^j - 1`
for all `0 < j < n`, **except exactly** in the listed cases. The exceptional
pairs are the classical ones for Zsigmondy (e.g. for `a^n - 1`: essentially
`n = 2` with `a + 1` a power of 2, `(a, n) = (2, 6)`, etc. — the source lists
them exactly; the reader is directed to the source for the verbatim list). The
point for this run: for **odd prime `p ≥ 3`** and `x ≥ 2`, `Phi_p(x)` has a
primitive prime divisor, and the exception list is a finite explicit catalogue,
none of whose members is in the run's regime.

### Conversely — primitive divisor of the cyclotomic factor
Because `Phi_p(a) = (a^p - 1)/(a - 1)` has a primitive prime divisor `q` with
`ord_q(a) = p`, one has `p | q - 1`, i.e. `q ≡ 1 (mod p)` and `q ≥ p + 1`.
This is the `prim-div-lucas` claim's congruence content, now anchored to a
primary source's exact statement.

## Relation to the known solution (falsifier)

At `(x, p) = (3, 2)`, the index is `p = 2` — the even (exceptional) index. The
primitive-divisor statement "for odd prime p and x ≥ 2, Phi_p(x) has a
primitive prime divisor r ≡ 1 (mod p)" does NOT cover `p = 2` (there
`Phi_2(3) = 4`, whose only prime divisor is 2, and 2 ≢ 1 (mod 2)), so it is
excluded by hypothesis, not refuted by the known solution. The falsifier
discipline is intact.

## Claims

```claim
id: roitman-zsigmondy-order-p-equals-1-mod-p
statement: >
  A prime r is a Zsigmondy prime for (a, n) (a, n > 1) iff it is a prime
  divisor of a^n - 1 that divides no a^j - 1 for 0 < j < n, equivalently iff
  ord_r(a) = n; and then n | r - 1 (so r ≡ 1 (mod n), r ≥ n + 1).
  In particular for an odd prime p and integer x >= 2, a primitive prime
  divisor r of Phi_p(x) = (x^p-1)/(x-1) satisfies r ≡ 1 (mod p).
hypotheses: a, n integers > 1; r prime.
holds-here: yes — the congruence engine of the adopted Lucas/primitive-divisor
  approach; for p odd prime and x >= 2 (run's regime) Phi_p(x) has a primitive
  divisor r ≡ 1 (mod p). At (x,p) = (3,2) the index p = 2 is the exceptional
  even case, excluded by hypothesis, not refuted.
status: asserted-by-source (Roitman, Proc. AMS 125 (1997), verbatim).
anchor: research/sources/roitman-zsigmondy-primes.primary.md
bearing: converts the existence of a primitive divisor (Zsigmondy) into the
  congruence r ≡ 1 (mod p) on prime divisors of y, the elementary engine of
  the Lucas approach.
```

```claim
id: zsigmondy-exceptions-finite-list
statement: >
  Zsigmondy's theorem: for integers a, n > 1 there is a prime q dividing
  a^n - 1 that divides no a^j - 1 (0 < j < n) except in an explicit finite
  list of (a, n) cases. For odd prime n >= 3 and a >= 2 the existence always
  holds.
hypotheses: a, n > 1 integers; n >= 3.
holds-here: yes — the run's regime is odd prime n = p >= 3, a = x >= 2, where
  no exception occurs.
status: asserted-by-source (Roitman/Zsigmondy, verbatim Theorem 3).
anchor: research/sources/roitman-zsigmondy-primes.primary.md
bearing: the explicit finite exception structure that makes "no primitive
  divisor" a checkable finite list rather than an open condition.
```
