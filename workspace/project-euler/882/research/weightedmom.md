# Moments of the weighted sum-of-digits function — Larcher & Pillichshammer (2005)

Source: https://www.ajol.info/index.php/qm/article/view/21757
Larcher, G. & Pillichshammer, F. (2005). *Moments of the weighted sum-of-digits
function*. Quaestiones Mathematicae 28(3), 321–336.
DOI: 10.2989/16073600509486132.

Note on availability: this entry holds the abstract plus editorial metadata only.
The full PDF is subscription-gated on the AJOL page, so only the abstract-level
claims below could be recorded. Stored once (no `.full.md` needed; both files
hold the same abstract).

## What it establishes
- The **weighted sum-of-digits function** generalizes the ordinary sum-of-digits
  function by assigning a weight to each digit; the alternated sum-of-digits is
  a special case.
- The authors **compute the first and second moments** (means/fluctuations) of
  this weighted sum-of-digits function.
- They give an **alternative representation to Delange's formula** for the first
  moment of the ordinary sum-of-digits function, with a *non-periodic,
  piece-wise differentiable* fluctuation replacing Delange's periodic,
  nowhere-differentiable one.
- A **(weak) Delange-type result for the first moment of the weighted
  sum-of-digits function holds iff the weight sequence converges.**

## Why it applies here
The run's arithmetic engine needs the two board totals
- A(n) = Σ_{k=1..n} k·popcount(k)  (total 1-bits, k copies of k)
- B(n) = Σ_{k=1..n} k·zerocount(k) (total 0-bits, k copies of k).

Both are *first-moment / weighted* sums of binary digit-count functions — exactly
the object this paper formalizes (here the weight is the index k itself; the
paper's own weight is positional, but the moment machinery is the same Delange-
type treatment). The paper's central structural claim — that such weighted digit
sums admit closed-form/delange asymptotic expressions (main term + fluctuation),
rather than requiring term-by-term iteration — is the theoretical warrant that
A(n) and B(n) are computable in O(poly log n) and not by iterating to n. The
practical O(log n) recurrences for the specific unweighted pieces come from the
companion entries A000788 (bitcount.md) and A059015 (zerocount.md); the k·
weighting is the run's own bit-position decomposition (solution.md/context.md).

## Caveat
- Only the abstract is locally available; the specific moment formulas are not.
  The paper is cited for the *existence and structure* of closed-form weighted
  digit-sum moments, not for any formula used numerically here.
- The board's weighting (k copies of k) is not the paper's positional weighting;
  the shared object is "first moment of a digit-sum function", not identical sums.
