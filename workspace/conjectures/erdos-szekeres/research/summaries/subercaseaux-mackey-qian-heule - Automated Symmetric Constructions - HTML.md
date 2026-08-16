> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/subercaseaux-mackey-qian-heule - Automated Symmetric Constructions - HTML.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/html/2506.00224v1 | converted from HTML -->

## What is in it

- Automated Symmetric Constructions
in Discrete Geometry
        - Abstract.
        - Key words and phrases:
  - 1. Introduction
      - Erdős-Szekeres.
      - Everywhere-unbalanced-points.
    - 1.1. Our contributions and methodology
  - 2. Background
    - 2.1. Geometric and combinatorial symmetries
    - 2.2. Orientation Variables
    - 2.3. CC Systems and Axioms
    - 2.4. Signotope Axioms
    - 2.5. Realizability Problem
  - 3. Symmetry Constraints
    - 3.1. Filtering Isomorphic Constraints
    - 3.2. Symmetry Breaking
  - 4. Encodings
    - 4.1. Dynamic Point Ordering Axioms
        - Proposition 1.
        - Proposition 2.
    - 4.2. Axioms for Collinear Point Sets
    - 4.3. Constraints for k k -Gons
- …


## What it claims

We present a computational methodology for obtaining rotationally symmetric sets of points satisfying discrete geometric constraints, and demonstrate its applicability by discovering new solutions to some well-known problems in combinatorial geometry. Our approach takes the usage of SAT solvers in discrete geometry further by directly embedding rotational symmetry into the combinatorial encoding of geometric configurations. Then, to realize concrete point sets corresponding to abstract designs provided by a SAT solver, we introduce a novel local-search realizability solver, which shows excellent practical performance despite the intrinsic ∃ ℝ \exists\mathbb{R} -completeness of the problem. Leveraging this combined approach, we provide symmetric extremal solutions to the Erdős-Szekeres problem, as well as a minimal odd-sized solution with 21 points for the everywhere-unbalanced-points problem, improving on the previously known 23-point configuration. The imposed symmetries yield more aesthetically appealing solutions, enhancing human interpretability, and simultaneously offer…

## Statements it makes

###### Proposition 1.

###### Proposition 2.

Proposition 1 is stating that the dynamic-ordering axioms are respected by actual pointsets, and Proposition 2 is Intuitively stating that these axioms are no more permisive than the CC axioms. In other words, an empty set of axioms would trivially satisfy Proposition 1 but not Proposition 2, and on the other hand, an inconsistent set of axioms would trivially satisfy Proposition 2 but not Proposition 1. Both proofs are included in Appendix D. The first proof is algebraic, and similar to the proof of the signotope axioms in [22], whereas the second proof is computational, since it reduces to the case n = 5 n=5.

Algorithm 1 Auxiliary functions for Localizer.

Algorithm 2 Localizer Thread

*[digest of a 71382 character source; every section, statement, and proof in full at `research/sources/subercaseaux-mackey-qian-heule - Automated Symmetric Constructions - HTML.full.md`]*
