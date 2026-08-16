# Pattern-finder survey 3 — every sequence re-examined; one new miss recorded

Scope: every exact integer sequence the run has actually computed, re-examined
with `analyze_sequence` / `find_linear_recurrence` / `oeis_lookup`, plus one
newly computed tabulation. Each item states verdict precisely.

---

## 1. Distinct-abundance-profile counts — NEW, catalogued nowhere genuine

The oracle's exhaustive scan (`profile_listing.captured.txt`) tabulates the
number of **distinct sorted-descending abundance profiles** over all UC
families on `[n]`:

```
n:       1   2    3     4
profiles: 1   4   18   138
```

I independently re-counted from the raw listing text (regex over the `[..]`
profile rows): **1, 4, 18, 138 — confirmed**, exact over the source data.

`analyze_sequence([1,4,18,138])`: differences 3,14,120 (not low-degree), ratios
4.0, 4.5, 7.67. `find_linear_recurrence` fits an order-2 recurrence
`a_n = 33 a_{n-1} − 114 a_{n-2}` — this is **spurious overfitting**: any order-2
recurrence reproduces 4 terms by construction, and the coefficients 33/114 have
no reason. Discarded.

`oeis_lookup([1,4,18,138])` returns two "matches" — **A156445** (n×n arrays of
squares of integers with rows summing to 8) and **A012930** (a Maclaurin-series
coefficient sequence). Both share only these four initial terms by coincidence;
neither is the abundance-profile count. Both are spurious for this object. This
is a **recorded miss**: the profile-count sequence is not catalogued (and with 4
terms and no extension route — n=5 enumeration is 2^32 subfamilies, declared
infeasible — no honest regularity can be claimed). No recurrence is asserted.

**Status:** the four values are checked (exhaustive, exact); no claim of a
catalogued closed form or a recurrence; the two OEIS hits are discarded as
coincidences.

## 2. WORST(n) denominators — settled, catalogued

WORST(n) = 1/(2^{n-1}+1) for n=1..4 (exhaustive), achieving family the
near-n-cube. Denominators 2,3,5,9,17 = OEIS A000051 (catalogued closed form
`2^{n-1}+1`; I re-ran `analyze_sequence([2,3,5,9,17,33,65])` confirming the
geometric-difference structure). This is a **sourced theorem** (Das–Wu Nagel
sharpness), corroborated by the exhaustive scan. Not a new finding; already
filed.

## 3. Union-closed family enumeration counts — catalogued, out of scope

3, 13, 121, 4959, 2771103 = OEIS A121921 (re-confirmed by a fresh lookup).
A recurrence for the count says nothing about abundance; operator directive
excludes it. Dead end recorded.

## 4. FC(4,n) threshold — too few terms, no structure

FC(4,n) = 5, 7, 10, 12 (Morris, Pulaj–Wood). `analyze_sequence` reports
differences 2,3,2; not low-degree; the mod-5 period-2 artefact is a 4-term
span coincidence. Not catalogued (earlier miss recorded). **No honest
conjecture on 4 terms.**

## 5. k-fold iid-OR barrier c_k — already proved

c_k strictly decreasing in k≥2, max c_2 = (3−√5)/2. Proved
(`kfold_barrier_claim.md`); corroborated to k=60 and re-tied to Yuster's ψ_k
and Ho's α_k/(1+α_k). Nothing new to add.

## 6. Möbius-algebra grounding — confirmed against a bogus FAIL

`mobius_algebra_check.py` printed FAIL on idempotent expansion / orthogonality
on B_3, B_4 — a **checker bug**: it tests `if p:` on a coefficient dict, so a
zero-coefficient product `{15: Fraction(0,1)}` is reported truthy. The
corrected `mobius_verify2.py` detects zero properly; B_2..B_4 all pass
(expansion, orthogonality, dim(L·a)=|↑a|). The Möbius-algebra grounding of the
`mobius-algebra-join-irreducibles` approach holds; the FAIL was never a
refutation. Second independent route (different zero-detection + standard Möbius
recursion) agrees; also the classical Solomon/Knop result.

## What is exploitable and what is not

- **The abundance-profile structure is the only exploitable regularity**, and
  it is already established: the unique worst case (min min-density) is the
  near-k-cube, value 1/(2^{n-1}+1), matching the sharp Das–Wu Nagel extremal.
  It fixes the shape any barrier must beat. It is a *lower* bound on the hard
  (minimum) direction, so it is not itself a route to UC.
- The distinct-profile **count** carries no low-order structure and is
  uncatalogued; the two OEIS hits are coincidental. Not worth pursuing.
- Enumeration counts (A121921) and c_k are settled; FC(4,n) is too short.
- Möbius-algebra grounding confirmed (dead-end detection, not a new conjecture).

Every value above is from an executed program; each claim is labelled checked
(exhaustive, exact) or sourced-theorem. No fit is dressed up as a proof.
