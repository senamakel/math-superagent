# Bello-Hernández, Benito & Fernández, "On Egyptian fractions" (2012)

Source: https://arxiv.org/abs/1010.2035 (arXiv:1010.2035v2), the paper
Schuh 2025 cites as [10]; direct download (abstract page) filed at
`research/sources/bello-benito-fernandez-2012-egyptian-fractions.full.md`.
(Note: an *earlier* run mis-filed the *other* arXiv paper 1001.1100 under
"ionascu-wilson"; see the correction below.)

Authors: M. Bello-Hernández, M. Benito, E. Fernández.

## What it establishes (sourced, primary)

- **A polynomial in three variables whose values (at nonnegative integer
  inputs) all satisfy the Erdős–Straus conjecture.** The perfect squares are
  NOT covered by these values.
- **Consequence**: there are arbitrarily long runs of consecutive integers
  all satisfying ESC.
- **Conjecture**: the polynomial's values include all primes of the form
  4q+5; checked up to **10¹⁴**.
- A greedy-type algorithm finds ESC decompositions; its convergence is proved
  for a wide class of numbers. Combining the polynomial with the algorithm,
  ESC is verified for all 2 ≤ n ≤ **2×10¹⁴**.

## Relation to the rest of the library

- This is the *original source* of several facts the library recorded from
  later retellings:
  - Schuh 2025 cites it for "verified Conjecture A for Pythagorean primes up
    to 10¹⁴" and "S_A contains no perfect squares."
  - The 2×10¹⁴ verification bound appears in this run's `verification-bounds`
    claim as "2012 (Bello-Hernandez, Benito, Fernandez)": now directly
    sourced.
  - The "squares are not covered" statement is the same boundary as Schinzel
    (2000) Theorem 1, Dubickas–Novikas E(4) (no squares), and Elsholtz–Tao
    Prop 1.6 (odd squares have no Type-I/II) — stated here in the
    polynomial-values form.
- ArXiv ID: 1010.2035 — the FRONTIER already listed it (1 electron);
  now in the library.

```claim
id: bello-2012-polynomial-3var-covers-nonsquares
statement: There is a polynomial in three variables whose values at nonnegative integer points all satisfy 4/n = 1/a+1/b+1/c; the perfect squares are not among these values. Consequently ESC holds for arbitrarily long runs of consecutive integers, and (with a greedy algorithm) for all n ≤ 2×10¹⁴.
hypotheses: none.
holds-here: true — the polynomial-side boundary: squares escape every known polynomial family, consistent with Schinzel/Dubickas/Prop1.6.
status: sourced (Bello–Hernández, Benito, Fernández 2012; abstract + full text).
bearing: the "arbitrarily long runs" property and the 2×10¹⁴ bound come from here; when the run claims a new family, it must check the family isn't just the values of this 3-variable polynomial.
anchor: research/sources/bello-benito-fernandez-2012-egyptian-fractions.full.md
```

## Correction to an earlier mis-file note

`research/sources/ionascu-wilson-erdos-straus.full.md` (arXiv:1001.1100) is
**Ionascu & Wilson, "On the Erdos-Straus conjecture"** — NOT Bello/Benito/
Fernández as the earlier `unobtained-sources.md` note claimed. The earlier
note ("the document behind it is arXiv:1001.1100, which is Bello-Hernández…")
was itself mistaken about the *content* of 1001.1100. The earlier note was
right only that the *name* was misleading: it is Ionascu & Wilson's paper.
The summary `research/summaries/ionascu-wilson-erdos-straus.md` should stay
named that way — it was right after all — while the note saying "the document
behind it is the Bello trio" should be dropped. (See unobtained-sources.md
correction appended below.)