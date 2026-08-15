# Milinković, Malešević, Banjac — Continued fractions, intermediate fractions and their relation to the best approximations

<!-- source: https://www.josa.ro/docs/josa_2020_3/a_05_Milinkovic_545-560_16p.pdf ; DOI 10.46939/J.Sci.Arts-20.3-a05 ; full text at research/sources/milinkovic-intermediate-fractions-best-approx.full.md -->

Luka Milinković & Branko Malešević (Univ. Belgrade), Bojan Banjac (Univ. Novi Sad).
_J. Sci. Arts_ 20(3):545–560, 2020. Survey unifying the terminology around convergents,
intermediate fractions (semiconvergents), and best rational approximations of the first and
second kind.

## Load-bearing statements for this problem

- **Definition 2 + Theorem 7 (proved, after Khinchin):** every **best approximation of the
  second kind** (fraction p/q, q ≤ Q, minimising |qα − p| among denominators ≤ q) **is a
  convergent** of α. The two-sided second-kind best approximations are exactly the convergents.
- **Definition 3 + note:** intermediate fractions lie strictly between two consecutive
  convergents and, **by Theorem 7, cannot be best approximations of the second kind**.
  This is the crucial boundary: the ordinary two-sided "best approximation of the 2nd kind"
  theory admits only convergents, never semiconvergents.
- **Definition 4 + Theorem 9:** a best approximation of the **first kind** is either a best
  approximation of the second kind **or an intermediate fraction**. "Fine intermediate
  fraction" = an intermediate fraction that is itself a best approximation of the first kind.

## Why it applies — and why it does *not* cover this problem

The Eulercoins of PE 700 are the **record lows** of `a_n = A·n mod M`. Writing
`a_n = M·(n·(A/M) − floor(...))`, a record low is a lattice point (n, p) **below** the line
`y = (A/M)·x` whose **signed vertical gap to the line is a new minimum**. That is a
**one-sided "best lower approximation"** (from below only), *not* the two-sided second-kind
notion of Theorem 7.

Consequence: applying only the two-sided theory here would be a mistake — it would say "best
approximations of the 2nd kind are just the convergents", which is true two-sided but is
**not** the coin list. The coins include non-convergent indices (e.g. 506, 2527, 4548, …),
i.e. intermediate fractions. Reaching those requires the **one-sided** characterisation —
convergents *and* their appropriate semiconvergents — which is the result in the Hancl–Turek /
Kimberling notes, not this paper.

So this source fixes the boundary of the two-sided theory (convergents only) and confirms that
the load-bearing one-sided statement lives elsewhere. It is **corroboration / boundary**, not
the method.

## Status

Two-sided Theorem 7 is proved in the paper (stated as following Khinchin) — usable as a
sourced claim for the *two-sided* result. The one-sided (record-low ↔ semiconvergents)
identification rests on Hancl–Turek / Kimberling (claims `eu700-record-lows-are-best-lower-approximations`,
`…-kimberling`), which remain `asserted` / not independently checked.

## Source URL

https://www.josa.ro/docs/josa_2020_3/a_05_Milinkovic_545-560_16p.pdf (DOI 10.46939/J.Sci.Arts-20.3-a05)

```claim
id: eu700-2-sided-best-2nd-kind-are-convergents
statement: A fraction p/q is a best approximation of the second kind to real alpha (minimises |q alpha - p| over denominators q' <= q) if and only if it is a regular convergent of alpha. Intermediate fractions (semiconvergents) lie strictly between consecutive convergents and are therefore never best approximations of the second kind; they can at best be best approximations of the first kind.
hypotheses: alpha a positive real; best approximation of the second kind as in Definition 2 (|q alpha - p| < |q' alpha - p'| for all q' <= q, p' != p when applicable); intermediate fractions defined between consecutive convergents (Definition 3).
holds-here: true and load-bearing-as-boundary. alpha = A/M = 1504170715041707/4503599627370517 is rational (and gcd(A,M)=1). The two-sided theorem does NOT characterise the Eulercoins: those are one-sided record lows and include non-convergent indices (506, 2527, 4548, ...). This theorem fixes that the two-sided theory alone is insufficient — the one-sided theory (Hancl-Turek/Kimberling) is needed for coins.
status: asserted (stated in Milinkovic-Malesevic-Banjac following Khinchin; not re-derived here) — but only the two-sided result, which is NOT the method.
bearing: clarifies that the Eulercoin list is a one-sided object; prevents the mistake of using only two-sided convergent theory for the coins.
anchor: research/summaries/milinkovic-intermediate-fractions-best-approx.md
```
