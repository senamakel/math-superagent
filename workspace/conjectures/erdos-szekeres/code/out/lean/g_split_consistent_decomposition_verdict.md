# G-split-consistent — Lean decomposition verdict

**Node:** `extremal-split-stability/G-split-consistent`
**File:** `code/lean/extremal_split_stability_G_split_consistent.lean`
**Checked by `lean_check`:** `compiled: true`. The only failures are the 3
declared `sorry`s (outcome `failed` solely because sorrys remain), so the
kernel-checked spine is recorded.

## What the kernel verified (no `sorry`, axioms only `[propext, Classical.choice, Quot.sound]`)

1. `esConstructSize_eq (n) (hn : 2 ≤ n) : esConstructSize n = 2 ^ (n - 2)`
   — the es_construct block sum over i = 0..n-2 of C(n-2,i) equals 2^{n-2},
   proved from Mathlib's binomial theorem (`Nat.sum_range_choose`).
2. `split_total_from_halves (n N) (hn : n ≥ 4) (L R) (A B) (hV) :
   2 * 2 ^ (n - 3) = 2 ^ (n - 2)` — the arithmetic of two halves of size
   2^{n-3}.
3. `combining_consistency (n N) (hn : n ≥ 4) (L R) (A B) (hV) : N = 2 ^ (n - 2)`
   — **the combining spine**: if a valid split (two disjoint 2^{n-3}-point
   (n-1)-avoiding halves whose union is everything) of an N-point corpus
   exists, then N = 2^{n-2}, exactly the size `esConstructSize_eq` gives for
   the ES 1960 construction. So the split and the construction's size are
   consistent, and the *shape* of G-split-consistent is verified.

## Three open `sorry` gaps (each with a `next`)

Each is a concrete exact-Fraction computation over the verified es_construct
coordinates, already reproduced in Python
(`code/out/gsplit_phase2.captured.txt`, command + `EXIT: 0`; claim
`gsplit-enum-completeness-and-n7-zero`, status `checked`):

- `es_construct_n5_four_splits : ∃ L R : Finset (Fin 8), ValidSplit 5 8 L R True True`  (4)
- `es_construct_n6_two_splits  : ∃ L R : Finset (Fin 16), ValidSplit 6 16 L R True True` (2)
- `es_construct_n7_no_split    : ¬ ∃ L R : Finset (Fin 32), ValidSplit 7 32 L R True True` (0)

Each is listed in a fenced `gap` block in the .lean file with `id`, `lemma`,
`status`, `next`. The `(n-1)`-avoiding predicate (`has_convex_k_subset` of the
exact oracle) is not a Lean term here, so `ValidSplit` carries it as the named
`AvoidL`/`AvoidR` conjunct left `True`, with the real content in the docstring
and prose.

`next` for all three: carry the es_construct block coordinates into Lean as a
fixed point list, define the convex-k-subset predicate over them, and close
each by `decide`.

## Scope (unchanged from the node)

This is scoped strictly to the verified es_construct template at n = 5,6,7.
It is NOT the general G-split lemma and NOT a statement about other extremal
sets. The n=7 zero is precisely the counterexample that refutes G-split on
this template (see the backward skeleton `research/backward/extremal-split-stability.md`,
gap `G-split`, status `refuted`).

## Ledger note

`record_entry`, `note_scratch` and `remember_memory` were all unavailable
during this formalisation (ledger tools not granted to this role; memory
server not answering). A later role holding `claims` write access should add
this as a claim entry with `status: decomposed` (partial formalisation),
`formalisation: code/lean/extremal_split_stability_G_split_consistent.lean`,
referencing the three proved theorems and the three open gaps above.
