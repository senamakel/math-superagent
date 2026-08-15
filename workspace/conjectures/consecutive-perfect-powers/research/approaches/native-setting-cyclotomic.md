# Native setting — where `x^p - y^q = 1` is an ordinary statement

Status: setting analysis (rising-sea). Not a claim.

## 1. What kind of object the statement is really about

`x^p - y^q = 1` is a statement about **perfect powers within 1 of each other**.
Rewritten it is `x^p - 1 = y^q` and `y^q + 1 = x^p`, which are statements of a
**power being a q-th power up to an additive unit**:

```
x^p - 1 = y^q      in the ring Z[ζ_p],   x^p - 1 = ∏_{i=0}^{p-1} (x - ζ_p^i)
y^q + 1 = x^p      in the ring Z[ζ_q],   y^q + 1 = ∏_{j=0}^{q-1} (y + ζ_q^j)
```

The setting in which this is *ordinary*, not exotic, is the **factorisation into
pairwise-coprime (off one ramified prime) ideals in a cyclotomic integer ring**.
In `Z` and `Z[i]` (one exponent 2) that is the elementary factorisation and the
problem closes. In `Z[ζ_p]` for odd p the pairwise coprimality survives but the
*ideal → element* lift does not — that lift is exactly the class group. So the
category the statement is native to is **algebraic number theory of cyclotomic
fields via ideal factorisation**, and the obstruction is class-group non-
triviality.

## 2. The change of ground that beats the elementary method

The elementary method (`Z`, `Z[i]`) works when an exponent is 2 and stops when
both are odd. The ground we must move to is the **idèle / ideal class group
side of `Z[ζ_p]`**: there `x^p - 1 = y^q` becomes "the divisor of `y` is a
`q`-th power", and comparing `(1-ζ_p)`-adic (the ramified prime) valuations is
the *first* consequence, giving Cassels: `p | y` and `q | x`. This single step —
valuation descent at the ramified prime — is the cheapest real content and is
reproducible in-workspace (see backward/cassels-selfcontained.md), no external
source needed.

## 3. Why this setting reproduces the working case (Scholze's rule)

In the `q = 2` case (`x^p - y^2 = 1`), the setting is `Z[ζ_p]` with `q = 2`; the
ramified-prime valuation descent reproduces the elementary `Z[i]` argument and
gives "no solution for odd p". In the `p = 2` case it reproduces the `Z`
factorisation. So the cyclotomic ground covers both working cases; the exponent
in which the old setting was working well is preserved. This is the check that
makes the reformulation worth having.

## 4. What each subsequent level of the ground costs

- Level 1 (both odd, one exponent 2): closes in `Z` / `Z[i]`. **Done this run by
  oracle + dedicated search.**
- Level 2 (Cassels' divisibility `p|y, q|x`): one ramified-prime valuation
  descent. Real content, self-contained, runnable first moves listed.
- Level 3 (double-Wieferich): needs a cyclotomic-unit / ideal relation
  (`q^{p-1} ≡ 1 mod p²`, `p^{q-1} ≡ 1 mod q²`). Reproduces the condition all
  searches use; the direct evaluator `check_conditions` is the runnable form.
- Level 4 (both-odd exclusion): the deep content, minus-class-group /
  Stickelberger. Out of reach; stated honestly as the obstruction.

## 5. What this does for the run

A concrete partial result and its verification are banked: the oracle
(exactly `(3,2,2,3)`), the closed exponent-2 cases, and the
double-Wieferich-pair catalogue plus `check_conditions`. Each is a lemma about
the same object, each is checked at the known solution `3^2 - 2^3 = 1`, and none
over-eliminates: the known solution is never excluded by an argument that would
also exclude it.
