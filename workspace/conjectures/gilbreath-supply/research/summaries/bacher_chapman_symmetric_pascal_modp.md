# Bacher & Chapman, *Symmetric Pascal matrices modulo p*

arXiv:math/0212144v2 [math.NT], 31 Jan 2003. Roland Bacher, Robin Chapman.
Full text: `research/sources/bacher_chapman_symmetric_pascal_modp.full.md`

<!-- source: https://arxiv.org/pdf/math/0212144 -->

## What it establishes

Studies the **symmetric** Pascal matrix `P(n)[i,j] = C(i+j, i)`, 0 ≤ i,j < n,
and its reduction mod a prime p. Key structural fact about the family: writing
`T` for the infinite unit-lower-triangular matrix with `T[i,j] = C(i,j)` (the
*left-justified Pascal triangle*, exactly the fold family), one has
`P(∞) = T·Tᵗ`. So the symmetric Pascal matrix is the transpose-product of the
lower-triangular Pascal matrix. Consequences:

- `det(P(n)) = 1` and `P(n)` positive definite over Z for all n (from the
  factorization into unit-lower-triangular × its transpose).
- The paper's main results are about the **reduction mod p of the
  characteristic polynomial** of `P(q)` at prime powers `q = p^l`. For p=2 it
  gets a complete explicit formula (Thm 1.3 → determines χ mod 2 recursively
  via the sequence γ); the p=3 case is a **conjecture** (Conj 1.6/1.7). It also
  states `P(q)` has order 3 over F_p with a stated χ_q congruence (Prop 1.2),
  and introduces the notion of a **b-autosimilar matrix** with a factorization
  theorem for them (Thm 2.1).

## Bearing on SUPPLY

The connection to the fold is real but **indirect** — the fold Φ_n is the
lower-triangular `T` (rows d, the `(1+σ)^d` submask-XOR operator), whereas this
paper works with the symmetric `P = T·Tᵗ`. The `det(P)=1`, `P=TTᵗ`,
positive-definiteness facts are structural confirmation that the lower-triangular
Pascal family (our Φ) sits inside a well-behaved matrix algebra over Z/F_p. The
mod-2 characteristic-polynomial result governs the **eigen/structure** of the
symmetric product, not directly the Hamming weight of `wt(Φ_n h)`. So this is
background for the fold-geometry tier rather than a route-closer.

**What it does NOT provide:** no lower bound on `wt(Φ_n h)` for sparse h; the
open request `walsh-spectral-subset-b904` (weight of the image of a sparse input
under the fold) is not addressed by the symmetric-Pascal characteristic
polynomial. It is a supporting structural reference, not the theorem gap.

## Status / honest labels

Proved results (determinant=1, P=TTᵗ, p=2 characteristic polynomial formula) and
conjectures (p=3). Not a SUPPLY result. No numeric claim blocks to add. It
confirms the existing `fold-rank-n-minus-2-binomial-proved` structural picture
from the symmetric side.

## Relations

- Stronger than the Callan note: Callan's Theorems (S⁻¹ = S(-1), S(x)S(y)=S(x+y))
  are, per Callan's "Added in Proof", exactly the Kronecker-product observation
  that Bacher reported and that the b-autosimilarity machinery here generalises.
  Same family, two phrasings — keep both; this is the primary, Callan the compact
  statement with the free-of/sign structure.
- In-library mirrors: `hofer_pascal_matrices_mod2`, `bacher_beeblebrox_reduction`
  (different Bacher paper), `mestrovic_lucas_theorem_survey`, `callan_sierpinski_triangle_prouhet_thuemorse`.
- Bacher, *La suite de Thue-Morse et la catégorie Rec* (CRAS 342, 2006) is cited
  by Callan and matches the k-regular tier (Allouche–Shallit II in-library).
