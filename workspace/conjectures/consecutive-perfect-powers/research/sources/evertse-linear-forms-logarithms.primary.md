# Evertse, "Diophantine Approximation", Chapter 5 — Linear forms in logarithms (Baker's method)

**Source URL:** https://pub.math.leidenuniv.nl/~evertsejh/dio19-5.pdf
**Author/venue:** J.-H. Evertse, "Diophantine Approximation" (Leiden University
course notes, Chapter 5, "Linear forms in logarithms"). Freely hosted PDF.
**Type:** University lecture notes (primary, freely hosted).
**Status:** CAPTURED full-text excerpt via `read_sources` (server-side). Full
PDF not stored locally (download blocked); exact theorem statements quoted
below read directly from the PDF.

## Why this source is in the library

PROVENANCE.md records that the linear-forms tier is held only via the Tijdeman
survey (*abstract*-level shape `e^{−C (log A)^κ (log B)}`). This Evertse chapter
is the full-text primary treatment of the same machinery, giving the *exact*
Baker lower bound and the *explicit* exponent-upper-bound corollary that the
problem statement calls "the effective bound — astronomically large, far too
large to exhaust." It is the technique reference the run needs to say precisely
*why* computation cannot close the gap, without retrieving the concrete
computed constant for `x^p - y^q = 1` (which would be answer-bearing).

## Verified content (exact statements, quoted from the chapter)

### Baker's theorem (1975) — effective lower bound for a linear form

Let `α_1, …, α_m ∈ Q̄ \ {0,1}` and `γ, β_1, …, β_m ∈ Q̄`. For each `i` let
`log α_i` be any solution of `e^z = α_i`. Assume

    Λ := γ + β_1 log α_1 + … + β_m log α_m ≠ 0.

**Theorem 5.2 (Baker, 1975).** Then

    |Λ| > (eB)^(−C),

where `B = max(H(γ), H(β_1), …, H(β_m))` (heights) and `C` is an *effectively
computable* positive number depending on `m`, the degrees and heights of the
`α_i`, and the chosen branches of the logs. "Effectively computable" means: by
going through the proof one can compute an explicit `C`.

### Corollary 5.3 — the multiplicative form that drives exponent bounds

Restrict to `γ = 0`, `β_i = b_i ∈ Z`. If `α_1^{b_1} · … · α_m^{b_m} ≠ 1`, then

    | α_1^{b_1} · … · α_m^{b_m} − 1 | > (eB)^(−C_0),

where `B := max(|b_1|, …, |b_m|)` and `C_0` is effectively computable, depending
only on `m` and the degrees and heights of the `α_i`.

### How this produces the effective bound for `a^x − b^y = 1`

The chapter shows the mechanism: for an equation like `α^x = β^y c` (units in a
number field, or `a^x − b^y = 1`), one rewrites it so that a nonzero form `Λ`
is compared against a lower bound, then a smallness (from the equation making
two algebraic numbers nearly equal) gives the upper bound on the exponents. The
deduction is: `max{x, y} ≤ C(a, b)`, an explicit but typically enormous
computable function of the fixed bases. This is exactly why the problem is
*finitely decidable in principle but not by exhaustion*: the bound on `x, y`
(whence on `p, q` and `x, y`) is computable yet astronomically large.

## Falsifier note

Baker's method gives *upper* bounds on solutions; it never asserts a solution
exists. Evaluated at the known solution `3^2 - 2^3 = 1`, the corollary is
consistent (it just gives a lower bound on other near-equalities). No claim
here eliminates a solution; the falsifier discipline is intact.

## Claims

```claim
id: baker-effective-lower-bound
statement: >
  If Lambda = gamma + sum beta_i log alpha_i != 0 is a linear form in
  logarithms of algebraic numbers (alpha_i != 0,1; gamma, beta_i algebraic),
  then |Lambda| > (eB)^(-C) with B the maximum height and C an effectively
  computable constant depending on m, the degrees/heights of the alpha_i and
  the chosen log branches. (Evertse, Diophantine Approximation Ch. 5, Thm 5.2
  = Baker 1975.) Special multiplicative case: if alpha_1^b1 ... alpha_m^bm != 1
  then |alpha_1^b1 ... alpha_m^bm - 1| > (eB)^(-C0) with B = max|b_i| (Cor
  5.3).
hypotheses: alpha_i algebraic != 0,1; beta_i (resp. b_i) algebraic (resp.
  integer); the form is nonzero; C effectively computable.
holds-here: yes — this is the machinery that makes x^p - y^q = 1 effectively
  finite by bounding the exponents p, q in terms of x, y (or vice versa), which
  is the reason the problem's effective bound is huge.
status: sourced (primary course text, exact statement quoted; cross-checks
  ch. time Tijdeman survey shape e^{-C (log A)^k (log B)} and Stewart
  notes Baker-Wustholz (16 n d)^(2n+4) form).
anchor: research/sources/evertse-linear-forms-logarithms.primary.md
bearing: the exact shape of the effective bound — the answer to "why can't
  computation finish the job" — stated as technique, not as a concrete
  numerical constant for this equation.
```

```claim
id: effective-finite-but-not-computable
statement: >
  Baker's method yields an effective (explicit computable) upper bound on the
  exponents of equations of the shape a^x - b^y = 1 for fixed bases a, b: any
  solution has max{x,y} <= C(a,b) with C explicit but typically enormous. The
  bound is computable in principle but too large to exhaust. (Evertse Ch. 5;
  Stewart notes; Tijdeman survey.)
hypotheses: a, b fixed positive integers > 1, gcd(a,b) = 1; x, y >= 1.
holds-here: partial — the run's problem has x, y (the bases) also unknown, so
  the fixed-base bound C(a,b) does not directly apply. But the *shape* of the
  argument (compare a baker lower bound to a smallness from near-equality) is
  what produces the "astronomically large effective bound" the problem statement
  describes.
status: sourced (primary course text, mechanism quoted).
anchor: research/sources/evertse-linear-forms-logarithms.primary.md
bearing: states precisely why computation cannot settle the problem, satisfying
  the GOAL requirement to "establish the bound, state the gap in orders of
  magnitude, and stop" rather than proposing to close it by search.
```
