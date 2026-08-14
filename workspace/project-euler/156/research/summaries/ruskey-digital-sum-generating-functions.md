# Adams-Watters & Ruskey — "Generating Functions for the Digital Sum and Other Digit Counting Sequences"

**Source:** F. T. Adams-Watters and F. Ruskey, *Journal of Integer Sequences* Vol. 12 (2009), Article 09.5.6. Original: https://cs.uwaterloo.ca/journals/JIS/VOL12/Ruskey2/ruskey14.pdf (download blocked in this run); held copy from the TCD-hosted EMIS mirror: https://www.maths.tcd.ie/EMIS/journals/JIS/VOL12/Ruskey2/ruskey14.pdf . Abstract/HTML landing page captured at `research/summaries/ruskey-digital-sum-abstract-page.md`; full text: `research/sources/ruskey-digital-sum-generating-functions.full.md`.

Peer-reviewed treatment of the digit-counting statistics of numeration systems through generating functions.

## What it establishes

- A numeration system maps each positive integer to a unique digit string over a finite alphabet; the paper gives a unifying framework for the generating functions of digit-counting statistics in many numeration systems.
- Theorem 5 (verified verbatim in the full text, p. 4): for base k and digit d
  with 0 < d < k, the generating function of c_{k,d}(n) — the number of digits
  equal to d in the k-ary expansion of n — is
  Σ_{n≥0} c_{k,d}(n) z^n = 1/(1−z) · Σ_{m≥0} z^{d·k^m} / (1 + z^{k^m} + z^{2k^m} + ⋯ + z^{(k−1)k^m})
  = 1/(1−z) · Σ_{m≥0} z^{d·k^m}(1 − z^{k^m}) / (1 − z^{k^{m+1}}).
  This is an **infinite sum of rational terms** (a Mahler / divide-and-conquer
  object), NOT a rational function. The paper itself contrasts it with the
  Zeckendorf case: "does not have a rational generating function" (p. 7).
- Also: digital sum in base k (Theorem 1; k=2 case is Knuth TAOCP exercise 7.1.3.41), multi-radix and factorial-base digital sums (Theorems 8–9), binary even/odd-position 1-counts (Corollary 7), row sums of a column pattern via morphisms (Theorems 2–3).

## Bearing on PE156

- The problem's f(n,d) is the cumulative count of digit d in the decimal writings of 1..n — the partial sum of c_{10,d}(1..n), whose generating function is F(z)/(1−z). The paper is thus a second, fully analytical route to the same digit-count family the run computes with the place-value closed form (`G1-digit-count-closed-form`); its Theorem 5 is the per-number count in any base, so it covers the base-10 case as an instance.
- Confirms the counts are classical and exactly computable in every base, independent of the run's algorithm. Background/theory tier: the solver uses the O(log n) closed form, and the G2 bound comes from Khovanova–Marton Prop 9.1, not from this paper.

## Does not settle

- No statement about the fixed-point equation f(n,d)=n: no finiteness proof, no bound on solutions, no per-digit solution data. (Finiteness in the problem's sense is not its subject.)

```claim
id: ruskey-theorem5-digit-count-generating-function
statement: >
  For base k ≥ 2 and digit d with 0 < d < k, the generating function
  Σ_{n≥0} c_{k,d}(n) z^n of c_{k,d}(n) — the number of digits equal to d in
  the base-k expansion of n — is the infinite series of rational terms
  1/(1−z) · Σ_{m≥0} z^{d·k^m} / (1 + z^{k^m} + z^{2k^m} + ⋯ + z^{(k−1)k^m})
  (Adams-Watters & Ruskey, JIS Vol. 12 (2009), Article 09.5.6, Theorem 5,
  verified verbatim in the full text).  It is a Mahler/divide-and-conquer
  object, not a rational function; the paper contrasts it with the Zeckendorf
  generating function, which "does not have a rational generating function".
  Hence in base 10 the problem's per-number count of digit d in n has such a
  generating function, and f(n,d) (occurrences of d in 1..n, i.e. the
  problem's 0..n count for d > 0) is its prefix sum.
hypotheses: >
  k ≥ 2 and 0 < d < k.  For PE156: base 10 (k = 10), d ∈ {1,...,9}; the
  hypothesis 0 < d < k holds for every digit d used in the problem.
holds-here: yes
status: asserted (sourced; theorem statement and both equalities quoted
  verbatim in the full text on disk)
bearing: >
  Second, fully analytical route to the digit-count family behind claim
  G1-digit-count-closed-form.  Background/theory tier — the solver uses the
  O(log n) place-value closed form; this supports rather than replaces it.
  Also confirms the counts are classical and exactly computable in every base.
anchor: >
  https://www.maths.tcd.ie/EMIS/journals/JIS/VOL12/Ruskey2/ruskey14.pdf
  (full text on disk: research/sources/ruskey-digital-sum-generating-functions.full.md)
```