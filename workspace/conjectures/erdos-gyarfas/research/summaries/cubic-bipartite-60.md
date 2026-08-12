> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/cubic-bipartite-60.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/html/2608.02675v1 | converted from HTML -->

## What is in it

- A 60-Vertex Lower Bound for Cubic Bipartite
Counterexamples to the Erdős–Gyárfás…
        - Abstract
  - 1 Introduction
        - Theorem 1 (Finite cubic-bipartite frontier).
        - Corollary 2.
        - Proof.
    - 1.1 Comparison with previous bounds
    - 1.2 Proof outline
  - 2 Incidence configurations and cycle translations
        - Proposition 3 (Incidence translation).
        - Proof.
        - Definition 4.
        - Lemma 5 ( C 4 C_{4}).
        - Proof.
      - Worked example.
        - Lemma 6 ( C 8 C_{8}).
        - Proof.
        - Lemma 7 (Incremental C 16 C_{16} oracle).
        - Proof.
  - 3 Triangle-rooted proof
    - 3.1 Moore reduction and two normalized roots
        - Lemma 8 (Edge-rooted Moore reduction).
- …


## What it claims

A certified exhaustive computation shows that every simple cubic bipartite graph on at most 58 58 vertices contains a cycle of length 4 4, 8 8, or 16 16. Consequently, any cubic bipartite counterexample to the Erdős–Gyárfás conjecture has at least 60 60 vertices, improving the established published lower bound of 30 30.

The proof begins with a Moore-bound observation: below 62 62 vertices, a cubic bipartite graph avoiding 4 4 - and 8 8 -cycles must contain a 6 6 -cycle. Viewing the graph as the Levi graph of a linear symmetric v 3 v_{3} -configuration turns this 6 6 -cycle into a Berge triangle. Up to symmetry, only two rooted extensions are possible. A complete restricted-growth search on at most 29 29 points closes both search trees. The computation is checked by two separately implemented searches using different C 16 C_{16} oracles and by a static witness certificate. Source code, certificates, and reproduction instructions are archived with the paper.

Keywords. Erdős–Gyárfás conjecture; cubic bipartite graphs; prescribed cycle lengths; exhaustive generation; symmetric…

2020…

## Statements it makes

###### Theorem 1 (Finite cubic-bipartite frontier).

###### Corollary 2.

Theorem 1 also shows that one of the first three relevant power-of-two cycle lengths is forced; no 32 32 -cycle is needed.

###### Proposition 3 (Incidence translation).

###### Definition 4.

###### Lemma 5 ( C 4 C_{4}).

###### Lemma 6 ( C 8 C_{8}).

###### Lemma 7 (Incremental C 16 C_{16} oracle).

###### Lemma 8 (Edge-rooted Moore reduction).

###### Lemma 9 (Triangle-root orbits).

###### Proposition 10 (Triangle-rooted coverage).

###### Proposition 11 (Certified universal triangle search).

###### Proposition 12 (Six deepest kernels).

*[digest of a 29175 character source; every section, statement, and proof in full at `research/sources/cubic-bipartite-60.full.md`]*
