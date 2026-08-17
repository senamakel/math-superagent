# Scholar synthesis — Fibonacci family per-a boundary count is settled (decisive gap closed)

Status: this is a durable, numerically-checked finding written to disk because the
Cognee memory server is not responding in this session (the standard
`remember_memory` path is unavailable; see CONTEXT.md's and ROOT.md's notes).

## What the run now knows that it did not before this session

The backward decomposition's single open gap (`G-boundary-uniform-count`, in
`research/backward/boundary-finite-collisions.md`) has its decisive open question
answered. The open question (directive 26 / `G-boundary-collision-a-finite.next`)
was: for the infinite Fibonacci family `a_j` (j=1..12), does the number of
nontrivial boundary representatives stay at the construction's 2, or grow with j?
The answer, from an **exhaustive exact oracle** that inverts `C(n,k)=a_j` for
EVERY k-column with `C(2k,k) <= a_j`:

- j=2 (29 digits): N = 6; half-reps = {(104,39),(103,40)} — exactly the
  construction's two. (`code/out/family_sequences.captured.txt`)
- j=3 (205 digits): N = 6; half-reps = {(714,272),(713,273)}.
- j=4 (1412 digits): N = 6; half-reps = {(4895,1869),(4894,1870)}, 28 workers,
  1.9s (`code/out/extend_exact_N_family_i4.captured.txt`).
- j=5 (9688 digits): N = 6; half-reps = {(33552,12815),(33551,12816)},
  32,183 columns scanned, 330.4s (`code/out/extend_exact_N_family_i5.captured.txt`).
- j=1 (3003): N = 8, half-reps = {(78,2),(15,5),(14,6)} — the extra rep is the
  k=2 collision C(78,2); it never recurs for j>=2.

## Conclusion (the claim)

Every member a_j with j>=2 of the infinite family contributes exactly **2**
nontrivial left-half representatives, both of which are boundary under the
corrected MRSTT cut for every eps > 1/3 (verified in
`code/out/boundary_cut_corrected.captured.txt` and `boundary_family_always_boundary.captured.txt`).
The per-a boundary-representative count is therefore **constant**, bounded by 3
(the maximum, attained only at 3003; =2 for every other j). Hence:

- `G-boundary-uniform-count` is NOT refuted by the infinite family — the count
  does not grow with j, so C is not forced unbounded by it.
- C >= 3 (from 3003) remains the live lower bound.
- The dangerous scenario (additional boundary reps appearing and growing with j,
  which would make C unbounded and break the decomposition) is ruled out for
  j=2..5, i.e. for every a_j up to ~10^9688, by exhaustive search.

Registered claim: `fibonacci-family-per-a-boundary-count-bounded` (status:
`checked`), anchor `research/notes/fibonacci-family-boundary-proved.md`
(the note whose "Bearing on G-boundary-uniform-count" section I updated).

## Bearing on the decomposition's remaining hard step

This resolves the "Fibonacci per-a" sub-question, NOT the whole gap. The
decomposition's core open step remains `G-nonfibonacci-pairs-are-bounded`:
proving that non-Fibonacci boundary-collision pairs are confined to a finite,
computable set of columns (which is where the effective/small-k results and the
Bilu-Tichy/HPT classification would be needed). The Fibonacci family no longer
threatens C, but the "extra from non-Fibonacci columns" term is untouched.

## What the run still lacks

1. A resolution of `G-nonfibonacci-pairs-are-bounded` (the real core of the
   boundary regime).
2. An effective height bound with a computed constant for a specific small
   (k1,k2) family (the GOAL-eligible partial result; Matveev 2000 Thm 2.3
   K=Q constants are held — this is a compute task, `compute, not fetch`).
3. The delta-invariant/genus-closed-form proof promotion (compute/proof task).
