# Pettersson–Tverberg–Östergård 2014 — A Note on Toeplitz' Conjecture

**Source:** Ville H. Pettersson, Helge Tverberg, Patric R. J. Östergård, "A Note on Toeplitz' Conjecture," Discrete & Computational Geometry 51 (2014), 722–728. DOI: 10.1007/s00454-014-9578-5. Full text at [[research/sources/pettersson-tverberg-ostergard-2014-toeplitz-note.full.md]].

## What it establishes — the verification bound

This is the **computational verification bound** for the Square Peg Problem, and the answer to ROOT.md's "current verification bound" question.

**Conjecture C.** A Jordan curve J ∈ 𝒥′ (finite Jordan curves composed of unit axis-parallel segments with integer endpoints — grid curves) contains four points of the integer lattice that form the corners of a square of side length at least i(J)/√2, where i(J) is the side length of the largest axis-aligned open square contained in the bounded component of R²∖J, and o(J) is the side length of the smallest closed axis-aligned square containing J.

- **Theorem 1:** Conjecture C implies Toeplitz' conjecture. *Proof:* approximate any Jordan curve by scaled grid curves Jₙ/n (Jₙ in an n×n grid), get a square on each with side ≥ i(Jₙ/n)/√2, take a limit; compactness gives a limiting square, and since i(Jₙ/n) → i(J) > 0, the limit square has positive side length (nondegenerate). **This is a shrinkout-free argument** — the bound i(J)/√2 > 0 is exactly what prevents the degenerate limit.
- **Theorem 2:** At least one inscribed square of maximum size on a grid curve J ∈ 𝒥′ has all four corners on lattice points. (Enables exhaustive computer search over lattice-point squares.)
- **Theorem 3 (minimality reduction):** if a minimal-length counterexample J to Conjecture C has a unit chord AB (length-1 lattice segment), a chord surgery gives a shorter counterexample — so a minimal counterexample has no unit chords. This is the pruning rule for the search.
- **Theorem 4:** Conjecture C holds for every J ∈ 𝒥′ with o(J) ≤ 13 — verified by exhaustive depth-first search with pruning over chordless cycles in the (n+1)×(n+1) grid graph, n ≤ 13. **No counterexample found for n ≤ 13.**

*Discrepancy note:* Matschke's 2014 survey says the computation covers "any Jordan curve in the 12×12 square grid"; the paper itself states n ≤ 13 (o(J) ≤ 13). The paper's own abstract says "verified computationally for n ≤ 13." ROOT.md should cite the paper's n ≤ 13, noting the survey's n ≤ 12 is a retelling.

## Why it matters here

- The verification bound is **grid curves up to n = 13** (o(J) ≤ 13), via Conjecture C, established 2014. This is the honest "current verification bound" for the problem.
- The proof of Theorem 1 is the cleanest published answer to shrinkout: a positive lower bound i(J)/√2 on the inscribed-square side length is preserved in the limit. This is the exact template for what any extension of the locally-monotone theorem needs — a scale certificate.
- The discrete formulation (Conjecture C) is a finite, checkable statement — a natural candidate for the run's exact-arithmetic oracle (check that every grid curve of small size inscribes a lattice square of the stated size), and for a Lean formalization (the statement is combinatorial).
- The minimal-counterexample structure (no unit chords) is a concrete structural constraint on any counterexample to Conjecture C — directly relevant to ROOT.md's "structure of a minimal counterexample" section.

## Claims

```claim
id: pto2014-conjecture-c-implies-T
statement: Conjecture C (a grid curve J ∈ 𝒥′ inscribes a lattice square of side ≥ i(J)/√2) implies Toeplitz' conjecture.
status: asserted-by-source
evidence: Pettersson–Tverberg–Östergård 2014, Theorem 1, Discrete Comput. Geom. 51, 722–728
holds-here: yes — the shrinkout-free limiting argument; the positive bound i(J)/√2 prevents degenerate limit squares
falsifies: a flaw in the compactness argument of Theorem 1's proof (none found); a grid curve violating Conjecture C
```

```claim
id: pto2014-verification-bound-n13
statement: Conjecture C holds for every grid Jordan curve J ∈ 𝒥′ with o(J) ≤ 13 (grid size n ≤ 13), by exhaustive computer search.
status: verified-numerically (computer-assisted proof as published)
evidence: Pettersson–Tverberg–Östergård 2014, Theorem 4 (exhaustive DFS with pruning over chordless cycles; no counterexample found)
holds-here: yes — this is the current verification bound for the problem; ROOT.md cites n ≤ 13 (paper) rather than n ≤ 12 (survey retelling)
falsifies: a grid curve with o(J) ≤ 13 violating Conjecture C; a bug in the search (reproduce with an independent checker)
```

```claim
id: pto2014-lattice-square-max
statement: On a grid curve J ∈ 𝒥′, at least one inscribed square of maximum side length has all four corners on lattice points.
status: asserted-by-source
evidence: Pettersson–Tverberg–Östergård 2014, Theorem 2
holds-here: yes — makes the discrete search exact: only lattice-point squares need checking
falsifies: a grid curve whose largest inscribed square has no lattice-point realization
```
