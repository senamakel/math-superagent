> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/krapivin-przybocki-heule - Toward Satisfiability Modulo Realizability - PointSAT HTML.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/html/2607.02958v1 | converted from HTML -->

## What is in it

- Toward Satisfiability Modulo Realizability
        - Abstract
        - Keywords:
  - 1 Introduction
        - Theorem 1.1
  - 2 The Happy Ending Problem and Its Variants
  - 3 Order Types and Realizability
  - 4 Description of PointSAT
    - 4.1 Generating Diverse Abstract Solutions
    - 4.2 Testing if Partial Realizations Are Solutions
    - 4.3 Omitting Flippable Orientations
    - 4.4 Summary
  - 5 Experiments for 23 Points With No 6-Gon or 7-Hole
    - 5.1 Evaluation
    - 5.2 Finding Figure 1
    - 5.3 Convex Hull Layers
        - Theorem 5.1
        - Proof
  - 6 Comparison of Experiments for Four Problems
    - 6.1 Number of Flippable Orientations
    - 6.2 Distribution of Number of Violations
- …


## What it claims

Problems complete for the existential theory of the reals ( ∃ ℝ \exists\mathbb{R}) arise throughout discrete geometry. We introduce *satisfiability modulo realizability*, a SAT-based approach for solving satisfiable instances of ∃ ℝ \exists\mathbb{R} whose solutions correspond to realizable geometric configurations. Our method encodes an underapproximation of a geometric problem as a SAT instance over abstract order types. Since almost all abstract order types are unrealizable, naive search is infeasible. We guide the search toward realizable order types using diversity-driven sampling, partial realizability feedback, and a novel flippability heuristic that passes only limited information between components. We apply our method to discrete geometry problems and resolve an open problem by showing that the largest set of points avoiding empty convex hexagons and convex heptagons is of size 23.

## Statements it makes

###### Theorem 1.1

###### Theorem 5.1

*[digest of a 53412 character source; every section, statement, and proof in full at `research/sources/krapivin-przybocki-heule - Toward Satisfiability Modulo Realizability - PointSAT HTML.full.md`]*
