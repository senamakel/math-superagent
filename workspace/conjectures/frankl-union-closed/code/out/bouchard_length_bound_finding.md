# Bouchard length bound — definition of ell: gloss vs source (resolved)

Source: `research/sources/bouchard-upper-bound-family-size-2511.full.md`
(arXiv:2511.10608), Theorem 1.

## The contradiction found

The note `research/summaries/bouchard-upper-bound-family-size-2511.md` glossed
`ell` as "the size of the largest member set". The claim block (below) stated
"one less than the maximal chain length". These two readings cannot both be
right, and the gloss is the wrong one.

## What the source actually says

Read from `§1` and the proof's base case directly (lines 19-40, 41-88):

> "a chain C in A is a subfamily ... such that X1,X2 in C implies (X1 ⊆ X2) ∨
> (X2 ⊆ X1), and the **length** of A, denoted ell = ell(A), is **one less than
> the maximum size of a chain** in A."

Proof base case `n=1`: `A = {[1]} = {{1}}` has `ell = 0` (chain size 1), and
`|A| = C(1,0) = 1`; `A = {{1}, ∅}` has `ell = 1` (chain size 2), `|A| = 2`.
Also in §1: "If ell = n, then ... |A| ≤ sum_{i=0}^{ell} C(n,i) = 2^n with
equality iff A = ∪_{i=0}^{ell} C([n], n−i) = 2^[n]".

**So ell = (maximal inclusion-chain size) − 1.** This is what the claim block
says.

## Why the "largest member size" gloss is definitively wrong

The equality family is `A = {S ⊆ [n] : |S| ≥ n − ell}`. Its largest member is
`[n]` (size n), and it is union-closed. If "ell = size of largest member" were
right, this family would have `ell = n` and the bound `sum_{i≤n} C(n,i) = 2^n`,
which is never tight for ell < n — the equality characterization would be
vacuous/trivially-non-tight, contradicting that the equality family is the
stated sharp extremal.

Consistency of the chain reading with the equality family: the longest chain
within `{S : |S| ≥ n−ell}` goes from an `(n−ell)`-set up to `[n]`, adding one
element at a time, i.e. `ell+1` members → chain size `ell+1` → `ell(A)=ell`.
And `|A| = sum_{i=0}^{ell} C(n, n−i) = sum_{i=0}^{ell} C(n,i)`, matching the
RHS. Both directions of the equality-iff hold under the chain reading.

## Resolution

The summary's prose was corrected to the source's definition and cross-linked
to this note and to `code/out/bouchard_length_bound_check.py` (a ready oracle
check of Theorem 1 under the corrected reading, to be run by the coder: bound
and equality-iff over all union-closed families for n = 1..4).

The claim block itself already carried the correct definition and needs no
edit; only the surrounding summary prose was wrong.

## Status

Claim `bouchard-upper-bound-length` remains `asserted` (source proof is an
elementary induction; not yet oracle-checked). The ready check, once run, can
promote it to `checked` for n ≤ 4 and confirm the mismatch between readings.
