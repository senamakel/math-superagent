# Adjacent-problem summaries (kept apart from the planar ES conjecture)

These are recorded so the run does not mis-hang claims on them. None is the planar ES conjecture.

## Heule–Scheucher & Subercaseaux — empty hexagon (ENCODED in sat-machinery note)

h(6)=30 (empty convex hexagon), Lean-formalized: ADJACENT problem. Not ES(6)=17.

## Scheucher — higher-dimensional ES/hole numbers: ADJACENT (d>=3). g^(3)(7)=13 etc.

## Erdős–Szekeres theorem (Wikipedia) — [[wikipedia-erdos-szekeres-theorem.full]]

This is the **monotone-subsequence** theorem: any (r-1)(s-1)+1 distinct reals contain an
increasing subseq of length r or decreasing of length s. PROOF appeared in the same 1935 paper as
the happy-ending problem. It shares the name and is in Mathlib — MUST NOT be confused with the
convex-polygon ES. GOAL.md explicitly flags this as the "wrong ES theorem" drift.

## MathWorld & Wikipedia happy-ending entries — [[mathworld-happy-end-problem.full]], [[wikipedia-happy-ending-problem.full]]

Encyclopedic restatements: ES(4)=5 (Klein), general theorem, conjecture. No new mathematics;
used only to cross-check the canonical values (ES(3)=3, ES(4)=5).

## Erdős Problems #107 (Bloom) — [[erdosproblems-107-happy-ending-entry.full]]

Current-status database entry: prize $500 (proof) / $100 (disproof), Graham $1000; confirms
bounds 2^{n-2}+1 ≤ f(n) ≤ 2^{n+O(sqrt(n log n))}; f(4)=5 (Klein), f(5)=9 (Turán–Makai); no claimed
partial solutions at access time. Has a formalised-statement pointer (formal-conjectures 107.lean).

## OEIS — [[oeis_a000051]], [[oeis_a083318]], [[oeis_a094373]], [[oeis_a356784]]

A000051: a(n)=2^n+1 — exactly the sequence ES(n)=2^{n-2}+1 would be (2,3,5,9,17,33,65,...).
A083318/A094373: variants differing at the initial term. These are **catalogued** (status:
catalogued), not a proof of the ES values: they establish only that 2^{n-2}+1 is a known catalogued
sequence, which is the conjecture itself, not a consequence. A356784 is unrelated (an
inventory-position table). None bears on the open upper bound.
