# Ruled out: OEIS entries co-returned with the perfect-powers catalogue

When this run looked up the perfect-powers sequence `1,4,8,9,16,25,27,32,36,49,64,81,100,121,125,128,144`
in the OEIS, three entries matched. Only one is the problem's object. The other
two share the term head but are unrelated gadgets; they must not be mistaken for
leads. Recording them here so nobody re-looks.

## A001597 — perfect powers: m^k, m >= 1, k >= 2  (the real object)

Digested in `research/summaries/oeis_a001597.md`. This is the set the equation
`x^p - y^q = 1` lives in.

## A359493 — RULED OUT (coincidental term match)

Numbers k whose divisor-ratio triangle's bottom entry is 1. This is a gadget
about divisor-count ratios `d(i)/d(i+1)` for divisors of k; it *is* a
subsequence of A001597 through the first 41+ terms (the entry states A001597(20)
= 216, A001597(41) = 1000, A001597(53) = 1728 are absent), i.e. it shares a long
term head with A001597 purely because for small perfect powers the divisibility
condition happens to coincide. It has no bearing on which integers are perfect
powers and no closed form relevant to `x^p - y^q = 1`. **Not a lead.**

## A157985 — RULED OUT (sign-flipped variant)

Perfect powers `m^k` with a `-1` factor attached when the base `m` is prime
(when `m^k` is a prime power), i.e. `a(n) = A001597(n) * (-1)^[m prime]`. This is
an *encoding gadget* that relabels the same perfect powers by the primality of
their base; it carries no information about consecutive pairs or about the
equation. **Not a lead.**

## Why they were looked up at all

The OEIS lookup is term-match based and returns every entry containing the given
terms in order; a catalogue record for a *different* object that happens to
contain the perfect powers as a head is returned alongside the genuine one. The
rule is: a match is a lead only when the *object and its closed form* bear on
the problem, never merely the terms. These two fail the object test and are
closed.

```claim
id: oeis-spurious-matches-ruled-out
statement: >
  The two OEIS entries co-returned with the perfect-powers lookup —
  A359493 (numbers whose divisor-ratio triangle's bottom entry is 1, a
  coincidental term-head subsequence) and A157985 (perfect powers sign-flipped
  by base-primality, an encoding gadget) — are ruled out as leads: neither
  describes the set of perfect powers nor carries information about consecutive
  pairs or the equation x^p - y^q = 1. Only A001597 is the problem's object.
hypotheses: none beyond the term-match that surfaced them.
holds-here: yes (ruling them out is correct; they share terms with A001597 but
  are different objects).
status: ruled out (by object identity, not computation).
anchor: research/summaries/oeis_spurious-matches.md
bearing: prevents the run from treating a coincidental OEIS term match as a
  mathematical lead; the perfect-powers catalogue is A001597 alone.
```
