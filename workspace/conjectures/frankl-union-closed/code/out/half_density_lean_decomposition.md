# Lean decomposition: node `half-density-max-eq-bool-subalgebra`

File: `code/lean/half_density_max_eq_bool_subalgebra.lean` — checked with
`lean_check`, **compiles with 5 `sorry` leaves**.

## What the kernel now holds

The node was split into a hard direction (the content: max-half ⟹ block
family) and a supported direction (block family ⟹ the three asserted
properties). The **reverse/supporting direction is PROVED kernel-closed**:

- `block_is_union_closed`: a block-partition family (atoms pairwise disjoint;
  `F` = set of unions of subfamilies of its atoms) is genuinely union-closed.
  Proof is real — uses `Finset.biUnion`, `union_biUnion`, `Finset.union_subset`.
  Axioms: `propext, Classical.choice, Quot.sound` only (**no sorryAx**).

The **combining node** `half_density_max_eq_bool_subalgebra` and its atom
corollary `half_density_atoms_structure` are stated and kernel-checked for
*shape*: each is a single application of the four (or five) gapped lemmas, so
the structure of the argument is verified even while its leaves are open.

## The five gaps (each with id/lemma/status/next, in the file)

| gap | statement | status | next |
|---|---|---|---|
| `gap-max-half-is-block` | max-half UC family (n≤5) is a block family | open — **the hard direction** | hunt n≥6 counterexample (claim's ceiling) or prove regular `|F|=2^k` case; only verified computationally (half_density_front.captured.txt PART 2); general-n truth genuinely open |
| `gap-block-elements-half` | block ⟹ every present element density 1/2 | open | counting bijection subfamilies containing vs omitting one atom, then `2·2^(k-1)=2^k` |
| `gap-block-card-two-pow` | block ⟹ `|F| = 2^k`, k≥1 | open | injectivity of union map over pairwise disjoint nonempty atoms + `card_powerset` |
| `gap-block-symm-diff-closed` | block ⟹ closed under symmetric difference | open | `(⋃S1)∆(⋃S2)=⋃(S1∆S2)` via `mem_symmDiff` + disjointness |
| `gap-block-atoms-exactly-one` | block ⟹ atoms pairwise disjoint, each present element in exactly one atom | open | derives from max-half + uniqueness via `DisjointAtoms` |

## What was NOT formalised (external / out of scope here)

- The **count refinement**: `H(n) = Bell(n+1) − 1` and
  `#(families with |F|=2^k) = S(n+1,k+1)` are purely combinatorial counting
  results, not encoded.
- The **exhaustive n≤5 verdict** itself is the computational evidence behind
  `gap-max-half-is-block`, not a Lean proof.
- The related `half-density-coordinatewise-false` claim (coordinate-wise
  statement is false) is deliberately **not** used; only the max-density
  statement is formalised.

## Faithful to the informal claim

The convention "half counts as abundant" (`2·count = F.card`) and the atom /
block-partition definitions match `half_density_claims.md`. All arithmetic is
exact `Nat`; no floats anywhere.
