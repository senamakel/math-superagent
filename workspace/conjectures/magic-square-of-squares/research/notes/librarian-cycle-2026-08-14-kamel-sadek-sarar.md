# Librarian cycle — 2026-08-14 (1): Kamel–Sadek consecutive-squares-AP context; Sarar 2025 search-bound verification

## What was added

1. **Kamel–Sadek 2016 (arXiv:1602.05862), Glasnik Mat. 52(1) (2017) 45–52 —
   peer-reviewed, full text on disk.**
   `research/sources/kamel-sadek-consecutive-squares-elliptic-2016-body.full.md`,
   summary `research/summaries/kamel-sadek-consecutive-squares-elliptic-2016-body.md`.
   Adjacent to the adopted `uniformity-bremner-ap-bound` thread: it builds an
   infinite family of elliptic curves `E_m` of **rank ≥ 5** carrying a 5-term
   sequence of *consecutive squares* of x-coordinates, and it documents that
   infinitely many elliptic curves carry APs of x-coordinates of length ≥ 8.
   Its bearing: **a generic "APs of x-coordinates on elliptic curves are short"
   argument is provably dead** — the force for the MSS must come from the
   specific `2E(Q)`-membership of the three points AND the specific curve form
   `y²=x(x²−c²)`, never from a generic AP-length bound alone.

```claim
id: kamel-sadek-consecutive-squares-rank-5
statement: For any non-trivial 5-term sequence of consecutive rational squares
  t0²,(t0+1)²,...,(t0+4)², there exist infinitely many elliptic curves
  Em: y² = a_m x³ + b_m x + c_m (m ∈ Z∖{0}) such that the five x-coordinates
  (t0+i)² are the x-coordinates of rational points on Em, and those five points
  are linearly independent in Em(Q); hence rank Em(Q) ≥ 5.
hypotheses: Em is in the general affine family y² = ax³ + bx + c over Q; the
  points are ordinary points of Em(Q), NOT required to lie in 2Em(Q).
holds-here: yes (as context/adjacent), but the special-form curve
  E: y² = x(x²−c²) required by the MSS (robertson-elliptic-reduction) is NOT
  shown to admit such sequences.
status: proved (peer-reviewed journal, explicit construction, MAGMA-verified
  independence + Silverman specialisation)
bearing: A generic "APs of x-coordinates on elliptic curves are short" argument
  cannot prove the 3×3 MSS non-existence: length≥8 APs and rank≥5 consecutive-
  square curves exist in profusion on the general family. The MSS obstruction
  must use 2E(Q)-membership and the specific congruent-number-form family.
anchor: research/summaries/kamel-sadek-consecutive-squares-elliptic-2016-body.md
```

2. **Sarar 2025 Zenodo preprint (search-bound claim) — considered, NOT added.**
   The search surfaced a 2025-12 Zenodo preprint (doi 10.5281/zenodo.17779697,
   Md. Rad Sarar & Anando) claiming exhaustive non-existence up to centre
   4.41×10³⁴ via Gaussian-integer pre-pruning and symmetry-forced backtracking.
   This was NOT downloaded: it is a non-peer-reviewed preprint of unknown
   provenance on a topic where the literature's verified bound is Buell's
   `25×10²⁴` (hourglass, coprime caveat) and Morgenstern's `2.4×10¹⁹`
   three-AP equal-d search. A single author with "Experimental and Theoretical
   Physics / Agriculture" topic tags, 0 citations, a YouTube-channel-promoting
   Figshare sibling, and no derivable method description does not clear the
   bar for a *computational bound this run would quote*. Per ROOT.md's own rule
   — a search bound is a fact about a range that must carry its method — a
   claim of `4.41×10³⁴` with no checkable method is worse than no bound. The
   gap is noted here so nobody re-fetches it. (If a future cycle wants it,
   the falsifies test is: does its method actually cover centres to that size
   AND enforce the full 8-line magic sum with distinct entries? Most "non-
   existence" preprints on this problem fail on one of the two.)

3. **DP07 explicit-constant lane — re-confirmed blocked, alternate route examined and judged marginal.**
   The only open request (`dp07-explicit-constant-for-e3-ap`) needs David–Philippon
   IMRP 2007 Thm 1.13's explicit constant for subvarieties of E^n. This cycle
   confirmed: (a) Numdam carries only DP99 "Minorations ... des tores"
   (`ASNSP_1999_4_28_3_489_0`), NOT the IMRP 2007 abelian-varieties II paper —
   so no Numdam/Cambridge open route exists for DP07; (b) a candidate alternate
   route, Kumar–Sahoo (Int. J. Number Theory 2024, arXiv:2311.11266,
   "Lehmer-type bounds and counting rational points of bounded heights on
   Abelian varieties"), makes its constant explicit for elliptic curves and
   products of elliptic curves — but it is a *counting-points / Lehmer* bound,
   not an AP-length bound, so it does not supply the C needed for `C^(r+1) < 3`;
   WorldScientific version is 403-paywalled (arXiv preprint has the same
   content). **Verdict: the DP07 constant is genuinely unobtainable through any
   open route this cycle; the Kumar–Sahoo lane does not substitute.** The thread
   step 0 must be a library/institutional scan of IMRP 2007 — no further open-web
   fetch should attempt it.

## Net state

- The `uniformity-bremner-ap-bound` thread's "risks" row is now backed by a
  peer-reviewed source proving long APs / rank ≥ 5 exist on the general
  elliptic family — the generic-bound route is dead regardless of constant
  size.
- No new CONTEXT.md conflict: the claimed rank-≥-5 curves are on `y²=ax³+bx+c`,
  not the special `x(x²−c²)` form, and the doubled-point caveat still holds.
- No download of the unverifiable Sarar preprint; recorded as deliberately
  excluded.
