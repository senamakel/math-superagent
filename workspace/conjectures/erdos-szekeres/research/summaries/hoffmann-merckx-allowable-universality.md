# Hoffmann & Merckx, "A universality theorem for allowable sequences with applications"

Source: https://arxiv.org/pdf/1801.05992 (arXiv:1801.05992, cs.CG; journal version SoCG 2018). The held file is the arXiv **abstract page only** — the full PDF was never fetched, so the only primary content this run has is the abstract. Claims below are about what the abstract establishes; nothing in the body (definitions, proofs, the realizability reduction) is held.

## What it establishes

- **Theorem (abstract).** The realization spaces of allowable sequences are *universal*: for each semi-algebraic set $V$ there is an allowable sequence whose realization space is stably equivalent to $V$. Consequently, **deciding realizability of an allowable sequence is ∃ℝ-complete**, and this holds even when the realization space of the order type induced by the allowable sequence is non-empty.
- Applications: ∃ℝ-hardness of the realizability of abstract convex geometries, and of recognition of visibility graphs of polygons with holes — solving two longstanding open problems.

## Consequence for this run

The allowable sequence is a *refinement* of the order type (strictly more data; the order type is induced from it). Its realizability is ∃ℝ-complete, exactly the order-type trap — so any upper bound proved over ALL abstract allowable sequences is stronger than the geometric ES conjecture and may be false. The adopted approach (`allowable-sequence-circular-representation`) must therefore realize every construction explicitly and check its geometric content in exact coordinates, and an abstract-allowable-sequence proof does not transfer to point sets.

## Not in this source

- No definition of the allowable sequence, no k-set or convexity statements in the circular sequence, no reversal-depth statistic. The abstract uses the term as standard GP80 machinery without restating it.
- The paper itself (arXiv v1) is downloadable at https://arxiv.org/pdf/1801.05992 — fetch the PDF if the realizability-reduction details are ever needed; the held file does not contain them.

```claim
id: hm-allowable-realizability-etr-complete
statement: Deciding whether a given allowable (circular) sequence is realizable by a planar point set is ∃ℝ-complete, even when the order type induced by the allowable sequence is realizable. Realization spaces of allowable sequences are universal (stably equivalent to arbitrary semi-algebraic sets).
hypotheses: allowable sequences in the Goodman–Pollack sense (the abstract relies on that standard notion without restating it); realizability by point sets in the plane.
holds-here: unchecked — the held file is only the arXiv abstract page; the term 'allowable sequence' is used without definition in the abstract, so the exact class of objects the theorem quantifies over is asserted rather than verified against GP80's definition.
status: asserted (source's own abstract; the ∃ℝ-completeness statement is the paper's main theorem, but this run holds no proof text and no definition section).
bearing: binds the allowable-sequence approach exactly as the order-type/chirotope trap binds the SAT arm: an upper bound proved over all abstract allowable sequences would be stronger than the ES conjecture and may be false; every candidate must be realized explicitly in exact coordinates before it counts.
anchor: research/sources/hoffmann-merckx-allowable-universality.full.md
```

## Bottom line

The only held primary content is the abstract: allowable-sequence realizability is ∃ℝ-complete (universality). No definitional or convexity content for circular sequences lives in this source; those must come from GP80 / Abello–Eğecioğlu–Kumar, which are not held.
