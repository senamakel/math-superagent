<!-- source: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i3p23/pdf -->

# Pulaj, Raymond, Theis, "New Conjectures for Union-Closed Families" (2016) — summary

**Source URL:** https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i3p23/pdf
**Full text:** `research/sources/pulaj-raymond-theis-new-conjectures-2016.full.md`
**Bibliographic:** Electron. J. Combin. 23(3) (2016), #P3.23. DOI 10.37236/5749.

## What this paper is

A computational/optimization treatment of Frankl's conjecture. It reformulates
the conjecture as two families of integer programs — one asking whether 2a is
an upper bound on |F| for a union-closed family on ground set [n] with each
element in ≤ a sets, the other whether the minimum number of sets containing
the most frequent element is ≥ m/2 — and observes computationally that the
optimal values do **not vary with n** (for large n). The authors formalize these
observations as new conjectures, prove they are not equivalent to Frankl, prove
special cases, and discuss approaches.

## Key content

- Formalizes the IP formulations (upper bound on 2a; lower bound on the
  most-frequent count).
- New conjectures: the optimal bounds depend only on a (not on n).
- Proves the conjectures are not equivalent to Frankl's conjecture.
- Proves special cases and discusses algorithmic routes (this is the companion
  to Pulaj's cutting-planes paper, `pulaj-cutting-planes-2017.full.md`, and
  Pulaj–Wood local configurations, `pulaj-wood-local-configurations-2023.full.md`).

## Claim blocks

```claim
id: pulaj-raymond-theis-ip-reformulation
statement: Frankl's conjecture is equivalent to a family of integer programs:
  for all a,n ∈ N+, 2a is an upper bound on |F| for a union-closed family on
  [n] with each element in ≤ a sets, iff the minimum number of sets containing
  the most frequent element is ≥ m/2; computationally the optimal values do not
  vary with n, formalized as new (non-equivalent) conjectures.
hypotheses: F union-closed on [n], each element in ≤ a sets.
holds-here: yes
status: asserted-by-source (published EJC 23(3) #P3.23, 2016)
bearing: This establishes the IP/optimization viewpoint that underlies the
  cutting-plane approach to FC-families; the new conjectures are a distinct
  (stronger-looking but non-equivalent) route.
anchor: research/sources/pulaj-raymond-theis-new-conjectures-2016.full.md
falsifies: An n-dependence in the optimal IP values, or an equivalence proof
  that contradicts the non-equivalence result.
```