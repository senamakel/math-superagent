# Hegedüs & Nagy — Representations of Circular Words (arXiv:1405.5607; EPTCS 151, AFL 2014, 261–270)

<!-- source: https://arxiv.org/abs/1405.5607 (full text at research/sources/hegedus-nagy-representations-circular-words-arxiv.full.md) | read 2026-08-19 -->

Full text: `research/sources/hegedus-nagy-representations-circular-words-arxiv.full.md`
(`research/sources/hegedus-nagy-representations-circular-words-2014.full.md` is only the arXiv *abstract page*; the -arxiv file is the actual paper.)

## What it establishes

**Objects.** Circular words (necklaces) over {a,b}; tree representation φᵢ of the circular Fibonacci word (fᵢ)°, where paths from root to level-ℓ nodes are the length-ℓ factors of the circular word.

**Theorem 3.** For the tree φᵢ of the finite Fibonacci word fᵢ, every level has exactly **one branching node**, except the last two levels. Proof: the number of distinct length-k factors of the infinite Fibonacci word is k+1 (Sturmian complexity), all appear in the tree because (fᵢ)° contains fᵢ², and a primitive word of length n has exactly n branching nodes in its tree, so all must sit on distinct levels.

**Corollary 1.** If j > i then φᵢ is a subtree of φⱼ — the trees are nested, and the limit tree φ of the infinite Fibonacci word is well-defined; each path in φ is an infinite suffix of the Fibonacci word.

**Theorem 4.** In any φᵢ, two branching nodes u,u′ on the same path with no branching node between them satisfy |ℓ(u) − ℓ(u′)| a Fibonacci number. Proof: otherwise the infinite Fibonacci word would contain a square vv whose v is not conjugate to a Fibonacci word, contradicting the well-known square-factor characterization (Lemma 2).

**§3 (tuples/iterative representations).** Every binary circular word can be built from ab by iterated fractional-power and cyclic-shift operations; the greedy algorithm (Figure 2) finds an iterative representation but not always an optimal one.

## Why it matters for PE1006

- The branching-node structure of the circular-Fibonacci tree is the factor-extension skeleton: the single branching node per level (except the last two) is exactly the **unique right-special factor** R_k of each length k, and the two children of R_k are the two extensions used in the run's extension recurrence Ψ(k+1) = 100Ψ(k) + 100V(R_k)² + 20S1(k) + J(k).
- Corollary 1's nesting is the finite-word justification that the k+1 length-k factors of the *infinite* word are exactly the level-k nodes of the circular tree of a sufficiently large fᵢ — matching the Sivasankar–Rama positional theorem (prefixes of rotations of qₙ).
- Theorems 3-4 confirm the Sturmian complexity count k+1 from the circular/tree side, an independent corroboration of `governing-factor-complexity`.

## What it does NOT establish

- No formula for Ψ(k), no decimal weighting, no floor-sum evaluation. It is a structural/combinatorial source about the factor tree, not about weighted sums.
- Theorem 4's Fibonacci-gap structure of branching nodes is suggestive for block-collapse but not directly a Ψ identity.

## Claims anchored here

Corroborates `governing-factor-complexity`, `fibonacci-unique-special-factor-reverse` (the unique right-special factor per level), `sivasankar-rama-position-theorem`. No new claim block needed.
