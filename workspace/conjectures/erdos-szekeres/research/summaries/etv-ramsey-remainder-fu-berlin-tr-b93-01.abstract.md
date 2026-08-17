# Valtr (Erdős–Tuza–Valtr), "Ramsey-remainder" — abstract-level note

Source: FU Berlin preprint B 93-01 abstract page,
http://www.inf.fu-berlin.de/inst/pubs/tr-b-93-01.abstract.html
Published version: **Erdős–Tuza–Valtr, "Ramsey-remainder", European J. Combin. 17 (1996) 519–532**
(doi 10.1006/eujc.1996.0054). The 1993 Berlin preprint B 93-01 is Pavel Valtr's own
write-up of the same work. Full text: **paywalled / FTP-only — NOT held.** Held item is the
dated abstract page only.
Wikilink: [[etv-ramsey-remainder-fu-berlin-tr-b93-01.abstract]] (no full-text companion exists
on disk; the summary is the only held form).

## What the abstract asserts (asserted-by-source, abstract-level)

- **Definition.** `rr(k)` (Ramsey-remainder) = the smallest integer such that: if `n` is
  sufficiently large with respect to `k`, and `S` is any set of `n` planar points in general
  position, then **all but at most `rr(k)` points of S can be partitioned into convex sets of
  sizes ≥ k**.
- **Estimate.** The paper "provides estimates on rr(k) which are best possible if a classic
  conjecture of Erdős and Szekeres on the Ramsey number for convex sets is valid" — i.e. the
  conditional **ES conjecture holds ⟹ these rr(k) estimates are best possible** (one-way).
- **Combinatorial analogue.** "In many types of combinatorial structures, the corresponding
  Ramsey-remainder rr(k) is equal to the off-diagonal Ramsey number r(k,k−1) minus 1" — a
  general-structure calibration with no planar-point content in itself.

## Relationship to the partition line already in the library

Consistent with (not contradicting) the library's partitioned-theorem tier: Pór–Valtr
partitioned ES theorem (any finite general-position X partitions into ≤ c_n convex
clusterings plus ≤ c'_n leftover points) and Bárány–Valtr positive-fraction ES theorem.
rr(k) is the *sharp* remainder constant; the conjectured ES value would make the provided
estimates tight. This is context for the partition/structural route, not a new bound.

## claim blocks

```claim
id: etv-rr-definition
statement: rr(k) (Ramsey-remainder) is the least integer such that for n sufficiently large relative to k, every n-point planar general-position set has all but at most rr(k) of its points partitionable into convex sets of size at least k.
hypotheses: n sufficiently large w.r.t. k; planar general position; partition into convex subsets each of size >= k
holds-here: yes — definition of a structural invariant of exactly the objects this run studies (2^{n-2}-point no-convex-n-gon sets are candidates for large remainder)
status: asserted (abstract-level; the definition itself is uncontroversial but the full text is not held)
bearing: a well-posed structural question on extremal sets: how many points of a 2^{n-2}-point no-convex-n-gon set can be covered by disjoint convex (n−2)-subsets? If ES holds, rr estimates are tight.
anchor: research/summaries/etv-ramsey-remainder-fu-berlin-tr-b93-01.abstract.md
```

```claim
id: etv-rr-es-conditional
statement: The estimates on rr(k) in the paper are best possible IF the Erdős–Szekeres conjecture (ES(n)=2^{n-2}+1) is valid. One-way conditional: ES ⟹ tight rr estimates.
hypotheses: ES conjecture valid; the paper's stated estimates
holds-here: yes as a conditional; gives no new upper bound on ES(n) by itself (needs the converse direction, which is not asserted)
status: asserted (abstract-level; full proof not held)
bearing: calibrates the partitioned-ES line: the exact 2^{n-2} constant, if true, forces sharp Ramsey-remainder estimates — a testable consistency condition, not a proof route. Does NOT help settle ES(7)=33.
anchor: research/summaries/etv-ramsey-remainder-fu-berlin-tr-b93-01.abstract.md
```

```claim
id: etv-rr-offdiagonal
statement: In many types of combinatorial structures (not planar points per se), the Ramsey-remainder equals the off-diagonal Ramsey number r(k,k−1) minus 1.
hypotheses: the combinatorial structure type stated in the paper (full text not held)
holds-here: unchecked — the abstract does not name the structure classes and the full text is paywalled
status: asserted (abstract-level)
bearing: context only; a hint at where the 2^{n-2} numerology might come from (r(k,k−1)-type counts), but no precise planar statement can be drawn from the abstract alone
anchor: research/summaries/etv-ramsey-remainder-fu-berlin-tr-b93-01.abstract.md
```

## What this source does NOT help with

- It does not establish any new upper bound on ES(n); the only ES-connection is the one-way
  conditional (ES ⟹ rr estimates best possible).
- The full text is unobtainable via HTTP (ScienceDirect paywall; Berlin preprint FTP-only),
  so the exact rr(k) estimates are NOT on disk. If the run needs the numbers, request the
  EJC 1996 full text or a faithful secondary statement of the rr estimates.
- It is not a restricted class of the ES conjecture; it is a Ramsey-remainder statistic on
  the same objects. Adjacent-keeping: do not file rr(k) estimates as ES progress.