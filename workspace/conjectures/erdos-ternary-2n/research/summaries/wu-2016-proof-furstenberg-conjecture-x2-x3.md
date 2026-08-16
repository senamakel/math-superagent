# Wu, "A proof of Furstenberg's conjecture on the intersections of ×p and ×q-invariant sets"

Source: arXiv:1609.08053v3, Annals of Mathematics (2019). Full text: `research/sources/wu-2016-proof-furstenberg-conjecture-x2-x3.full.md` (arXiv HTML page; only abstract captured — the PDF body is not in the library).

## What it establishes

**Furstenberg's intersection conjecture (proved).** If `A, B ⊂ [0,1]` are closed, `A` invariant under `×p mod 1`, `B` invariant under `×q mod 1`, with `log p / log q ∉ ℚ` (multiplicatively independent), then for all real `u, v`,

```
dim_H ( (uA + v) ∩ B ) ≤ max{ 0, dim_H A + dim_H B − 1 }.
```

Obtained as a consequence of a study of intersections of incommensurable self-similar sets on ℝ; the methods also give upper bounds for dimensions of arbitrary slices of planar self-similar sets satisfying the SSC and natural irreducible conditions.

## What it does NOT do for this problem

The conjecture Erdős needs is about the **discrete sequence** `2^n`, i.e. about whether a specific integer point lies in the digit-`{0,1}` set `S ⊂ Z_3`. Wu's theorem is a **dimension** bound on the intersection of two ×p / ×q-invariant subsets of the **unit interval**. It is the flagship result of the ×2 ×3 line, but — exactly like Lagarias's dimension theorems — it bounds the *size* of an intersection of sets, not *which integers* lie in it. Transferring it to a statement about the thin subsequence `2^n` embedded in `Z_3` is not done in the source.

## Status

Sourced, peer-reviewed (Annals). The theorem is proved; its relevance to the Erdős conjecture is indirect (dimension-set, not integer-point). The full PDF body is not in the library — this summary rests on the arXiv abstract alone.

```claim
id: WU-FURSTENBERG-INTERSECTION
statement: A closed under ×p mod 1, B closed under ×q mod 1, log p/log q ∉ ℚ ⟹
  dim_H((uA+v) ∩ B) ≤ max{0, dim_H A + dim_H B − 1} for all real u,v.
hypotheses: A,B closed subsets of [0,1]; p,q multiplicatively independent.
holds-here: yes for the dimension statement (p=2,q=3); but it bounds dimension of
  a set intersection, not which integers lie in S — does not reach the thin
  sequence 2^n. Holds as a dimension theorem, not as a route to the conjecture.
status: proved (Annals 2019; verdict on abstract)
bearing: confirms the ×2 ×3 dimension landscape this run cites, and reinforces
  that dimension/measure statements about S cannot be the deliverable (same
  limitation as LAGARIAS-DIMENSION-SET-NOT-INTEGERS).
anchor: research/sources/wu-2016-proof-furstenberg-conjecture-x2-x3.full.md
follows-from: LAGARIAS-DIMENSION-SET-NOT-INTEGERS
```
