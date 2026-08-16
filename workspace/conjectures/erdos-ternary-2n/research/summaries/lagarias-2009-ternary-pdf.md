# Lagarias, "Ternary Expansions of Powers of 2"

Source: arXiv:math/0512006v4 (math.DS / math.NT), 11 Jul 2008. Full text: `[[lagarias-2009-ternary-pdf.full]]` (https://arxiv.org/pdf/math/0512006). Published: J. London Math. Soc. 79 (2009) 562–588.

## The theorem that fixes the obstruction for this run

Erdős asked how frequently `2^n` omits digit 2 in ternary; conjectured only finitely many n. Lagarias reframes it as dynamics on `Z_3` under `y → 2y`.

**Witnesses:** `2^0=1=(1)_3`, `2^2=4=(11)_3`, `2^8=256=(100111)_3`.

**Theorem 1.4 (generalizes Narkiewicz to all λ).** For each nonzero `λ ∈ Z_3` and each `X ≥ 2`,
```
Ñ_λ(X) := #{ n ≤ X : (λ·2^n)_3 omits digit 2 } ≤ 2·X^α0,   α0 = log_3 2 ≈ 0.63092.
```

**Theorem 1.5 (Hausdorff dimension of 3-adic exceptional sets).**
- `dim_H(E^(1)(Z_3)) = α0 ≈ 0.63092`
- `(1/2)log_3 2 ≤ dim_H(E^(2)(Z_3)) ≤ 1/2`
- `(1/6)log_3 2 ≤ dim_H(E^(3)(Z_3)) ≤ dim_H(E^(2)(Z_3))`
where `E^(k)(Z_3) = {λ : at least k values of λ·2^n omit digit 2}`.

**Theorem 1.6 (intersections of 3-adic Cantor translates).** For `M` not a power of 3,
```
dim_H(C(1,M)) = dim_H(Σ_{3,2} ∩ (1/M)Σ_{3,2}) ≤ 1/2
```
and `dim_H(C(1,7)) = log_3((1+√5)/2) ≈ 0.438` exactly.

**Conjecture B:** the 3-adic exceptional set `E(Z_3) := {λ : infinitely many λ·2^n omit digit 2}` has Hausdorff dimension zero. Erdős's conjecture is EQUIVALENT to `1 ∉ E(Z_3)`.

## What dimension results do and do NOT give — the gap this run must state

Lagarias is explicit: the real method reaches only the `log_3 X` most-significant digits, the 3-adic method only the `log_3 X` least-significant, and "the vast number of digits in the middle of the expansion are not exploited in either method." A statement that `dim_H(E(Z_3)) = 0` — or that `S` (the digit-{0,1} Cantor set) has dimension `log_3 2 < 1` — says the exceptional SET is small in measure, but does NOT say which specific integers `n` give digit-2-free `2^n`. Dimension 0 of `E(Z_3)` would not imply `1 ∉ E(Z_3)`: a single point `λ` (like `λ=1`) could still be exceptional, and no dimension statement rules that out. **This is the precise sense in which "Hausdorff dimension of S" cannot be the deliverable.**

Conjecture E (generalization of Furstenberg): for multiplicatively independent `p,q`, any finite pattern of q-ary digits occurs in `(p^n)_q` for all sufficiently large n. Erdős's original is the case p=2, q=3, pattern "2".

## Claims

```claim
id: LAGARIAS-NARKIEWICZ-BOUND
statement: N1(X) := #{n <= X : (2^n)_3 omits digit 2} <= 1.62·X^alpha0 with
  alpha0 = log_3 2 ≈ 0.63092 (Narkiewicz 1980; Thm 1.4 generalises to
  N~_lambda(X) <= 2·X^alpha0 for every nonzero lambda in Z_3).
hypotheses: X >= 2, lambda nonzero in Z_3.
holds-here: yes — the lambda = 1 case is exactly Erdős's thin sequence 2^n.
status: proved (peer-reviewed JLMS; verified here against full text)
bearing: a real sub-polynomial upper bound on the count of digit-2-free n up to
  X exists; the exponent log_3 2 is the target any combined high+low method aims
  to beat. Says nothing about WHICH n — no equation is excluded.
anchor: research/sources/lagarias-2009-ternary-pdf.full.md
```

```claim
id: LAGARIAS-MIDDLE-DIGITS-OPEN
statement: The real method (Thm 1.1) controls only the log_3 X most-significant
  ternary digits; the 3-adic method (Thm 1.4) only the log_3 X least-significant.
  The ~alpha0·n digits in the middle are not exploited by either. Proving an
  upper bound O(X^beta) with beta < log_3 2, or quantifying that high and low
  digits are uncorrelated, is posed as open (Lagarias §1.6).
hypotheses: none — a statement of where the two methods fall silent.
holds-here: yes — this is exactly the middle-digit gap the run aims at.
status: asserted-by-source (posed as open problem by Lagarias)
bearing: any symbolic invariant that constrains the MIDDLE ternary digits of
  2^n is the thing no existing method reaches; a middle-digit constraint IS a
  genuine partial result.
anchor: research/sources/lagarias-2009-ternary-pdf.full.md
answers: middle-digits-open
```

```claim
id: LAGARIAS-DIMENSION-SET-NOT-INTEGERS
statement: dim_H(E^(1)(Z_3)) = log_3 2; (1/2)log_3 2 <= dim_H(E^(2)(Z_3)) <= 1/2;
  (1/6)log_3 2 <= dim_H(E^(3)(Z_3)) <= dim_H(E^(2)(Z_3)). Conjecture B: dim_H of the
  exceptional set E(Z_3) := {lambda : infinitely many lambda·2^n omit digit 2} is zero.
  Erdős's conjecture is equivalent to 1 ∉ E(Z_3).
hypotheses: none — the E^(k)(Z_3) are countable unions of intersections of
  multiplicative translates of the 3-adic Cantor set.
holds-here: yes — dimension statements, even dim_H E(Z_3) = 0, do NOT rule out
  1 ∉ E(Z_3): a single point (lambda = 1) could still be exceptional.
status: Theorem 1.5 proved; Conjecture B asserted.
bearing: A dimension bound on S (or E(Z_3)) cannot be the deliverable. It bounds
  the size of the exceptional SET, not which integers n lie in it. This is the
  precise sense in which the Hausdorff-dimension line cannot close the conjecture.
anchor: research/sources/lagarias-2009-ternary-pdf.full.md
```

```claim
id: naive-density-as-proof
statement: The density of integers whose ternary expansion avoids the digit 2
  tends to 0 (true). But this says nothing about the thin sequence 2^n: no
  density statement about all integers reaches the specific powers of 2.
  An argument that proves "density of digit-2-free integers tends to 0" has
  proved something true and IRRELEVANT.
hypotheses: none — a statement of why the density route cannot deliver.
holds-here: yes — the density trap of GOAL.md/problem.md.
status: asserted (structural fact about the method; the irrelevance is
  definitional)
bearing: never record a density statement as proof of Erdős. This is why the
  dimension/measure line (LAGARIAS-DIMENSION-SET-NOT-INTEGERS, WU, SHMERKIN,
  GMR) cannot be the deliverable.
```

```claim
id: LAGARIAS-CONJECTURE-E
statement: (Conjecture E, generalising Furstenberg) for multiplicatively
  independent p, q, every finite pattern of q-ary digits occurs in (p^n)_q for
  all sufficiently large n. Erdős's problem is p=2, q=3, pattern P=2.
hypotheses: p, q multiplicatively independent; pattern P a finite consecutive
  q-ary digit string.
holds-here: yes (P = "2").
status: asserted (conjecture, unproved by source and open today)
bearing: frames Erdős's as the special pattern case of a broader ×p ×q
  recurrence conjecture; a mechanism forcing one pattern from some point on
  "should apply to all patterns" (Lagarias). Not usable as a theorem.
anchor: research/sources/lagarias-2009-ternary-pdf.full.md
```

## Status

Sourced, peer-reviewed (J. London Math. Soc.) / arXiv v4. This is the standard reference the whole run's 3-adic route rests on. Relevant flags for the run: (a) the 3-adic and real methods are "independent" (high vs low digits) and (b) Lagarias explicitly poses as open the problem of combining them to get β < log_3 2 — that is the very gap the run's middle-digits aim would fill.
