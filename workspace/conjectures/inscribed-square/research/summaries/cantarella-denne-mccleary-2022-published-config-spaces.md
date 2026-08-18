# Cantarella–Denne–McCleary 2022 (published) — Configuration spaces, multijet transversality, and the square-peg problem

**Source:** Jason Cantarella, Elizabeth Denne, John McCleary, "Configuration spaces, multijet transversality, and the square-peg problem," Illinois Journal of Mathematics 66(2), 2022, 285–314. DOI: 10.1215/00192082-10120454. arXiv:2103.07506. Full text at [[research/sources/cantarella-denne-mccleary-2022-published-config-spaces.full.md]].

## What it establishes

The published, peer-reviewed version of the CDM square-peg work (the arXiv:1402.6174 preprint was split; this is the version of record for the square-peg part).

**Main theorem (transversality lifting property):** given a submanifold M ⊂ R^k, the compactified configuration space C_n[M] can be made transverse to any submanifold Z ⊂ C_n[R^k] (boundary-disjoint case) by an arbitrarily C¹-small (in fact C^m-dense) variation of the embedding of M, via the multijet transversality theorem.

**Square-peg consequence (the paper's own abstract):** there is a **dense family of smoothly embedded circles in the plane where each simple closed curve has an odd number of inscribed squares**, and a dense family of smoothly embedded circles in Rⁿ each with an odd number of inscribed square-like quadrilaterals.

**Structural ingredients (verified in the full text):**
- Theorem 4 ([42],[6]): C_n[M] is a manifold-with-boundary and corners whose interior C_n(M) has the same homotopy type; compact when M is.
- Theorem 7: in any configuration of points in C_n[M], pairs have well-defined limiting unit direction vectors and triples well-defined limiting distance ratios (the compactification records the degenerate directions).
- Theorem 16 (Transversality Theorem for Configuration Spaces): given ε > 0 there is a C^m-dense set of embeddings i′ with C_n(i′) ⋔ Z, ε-close to i.
- Theorem 17 (compactified version): the same with boundary-disjointness of Z from ∂C_n[N].
- Theorem 16/17 are the engine: they make the configuration-space intersection transverse, so the intersection is a finite set of points whose parity (odd) is computed by topology.

## Why it matters here

- **Confirms cdm2022-genericity-odd-squares at the version-of-record level:** the published IJM paper proves the odd-count theorem for a dense family of *smooth* curves. It is a genericity theorem, not a proof for arbitrary continuous curves — the full conjecture remains open. This is the checked, not assumed, status GOAL.md demands.
- The paper is about *smooth* curves throughout: the transversality machinery (multijet transversality, manifolds-with-corners) has no purchase on a general continuous Jordan curve. This is the precise reason the CDM method does not extend.
- The compactified configuration space C_4[S¹] with its boundary directions is the same object problem.md calls the Mobius band; CDM's contribution is the transversality lifting theorem that makes the count robust for the dense family.

## Claims

```claim
id: cdm2022-published-genericity-odd-squares
statement: There is a dense family of smoothly embedded circles in the plane where each simple closed curve has an odd number of inscribed squares (published, peer-reviewed: Illinois J. Math. 66(2) 2022).
status: asserted-by-source
evidence: Cantarella–Denne–McCleary, Illinois J. Math. 66(2) 2022, main theorem (arXiv:2103.07506)
holds-here: yes — the version of record of cdm2022-genericity-odd-squares; no full-conjecture claim exists in either version
falsifies: a published CDM paper proving the conjecture for all continuous curves
anchor: research/sources/cantarella-denne-mccleary-2022-published-config-spaces.full.md
```

```claim
id: cdm2022-transversality-lifting
statement: Given a submanifold M ⊂ R^k and a boundary-disjoint submanifold Z ⊂ C_n[R^k], the compactified configuration space C_n[i] can be made transverse to Z by an arbitrarily C¹-small (C^m-dense) variation of the smooth embedding i : M ↪→ R^k.
status: asserted-by-source
evidence: Cantarella–Denne–McCleary, IJM 66(2) 2022, Theorems 16–17
holds-here: yes — the technical engine of the odd-count theorem; smooth-only, so it does not address continuous curves
falsifies: a smooth embedding i and boundary-disjoint Z with no transverse C¹-perturbation
anchor: research/sources/cantarella-denne-mccleary-2022-published-config-spaces.full.md
```
