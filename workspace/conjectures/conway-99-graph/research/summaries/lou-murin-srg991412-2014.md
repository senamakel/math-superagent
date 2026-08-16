# Lou & Murin 2014 — On the Strongly Regular Graph of Parameters (99, 14, 1, 2)

<!-- source: https://math.mit.edu/research/highschool/primes/materials/2014/Lou-Murin.pdf -->
<!-- Full text: ../sources/lou-murin-srg991412-2014.full.md -->

## What this source is

Suzy Lou and Max Murin, MIT PRIMES-USA 2014 (mentor Peter Csikvari). A PRIMES
undergraduate research paper — **unrefereed**. Treat every result as a lead to be
re-derived within this run, not as an established theorem. It was the lead the
library had flagged as unobtainable ("Lou & Murin ... appears unpublished/a working
note"); it is in fact this PRIMES-USA paper, open on math.mit.edu.

The paper analyzes a hypothetical G = srg(99,14,1,2): possible substructures,
independent sets, triangle/rotation structure, automorphism orders 11, 13, and 7.

## What it establishes (leads, to be checked against the controls)

- **Thm 2.1.** If G contains H (the unique srg(9,4,1,2)) minus an edge as a
  subgraph, then G contains H as an *induced* subgraph.
- **Thm 4.1.** An independent set of size 9 in G cannot be maximal.
- **Thm 4.3.** alpha(G) <= 22; if alpha = 22 then every vertex outside the
  independent set has exactly 4 neighbours in it.
  - This **independently confirms** the run's checked closed form
    alpha = (u·k+2)/2 = 22 at u=4, k=14 (claim `coclique-bound-closed-form`,
    verified computationally). The proof here is a different route (RMS–AM on the
    F(i) counts) than the eigenvalue bound, so it cross-verifies the number 22.
- **Lemma 5.1.** chromatic number of G is in [5, 11].
- **Thm 6.1.** No automorphism of prime order p > 14. (If p | 99 were needed for
  an orbit-free action; since p ∤ 99 a fixed point connects to an orbit, so
  deg = 14 >= p.)
- **Thm 6.2.** No automorphism of order 13 (λ = 1 double-common-neighbour argument).
- **Thm 6.3.** No automorphism of order 11 (orbit-matrix M eigenvalue argument:
  M's eigenvalues ⊆ {14, 3, −4}; trace must be 38, 24 or 10; enumerated row
  possibilities give no matrix).
- **Section 7.** If alpha = 22 with independent set S, then the bipartite
  G′ = G minus edges inside V\S gives a **(22,4,2) block design** B′ (77 blocks of
  4, each treatment in 14 blocks, each pair in 2 blocks) — the neighbourhood
  traces of the 77 outside vertices on S. Not every block design yields a graph
  (repeated blocks / blocks sharing ≥3 elements violate μ). The cyclic and
  2-rotational block designs are candidate constructions, but the natural
  2-rotational construction would give an automorphism of order 11, which Thm 6.3
  excludes.
- **Section 8.** Order-7 automorphism analysis: forces a single fixed point P
  connected to exactly two 7-orbits A, B; builds a 15×15 orbit matrix M whose
  trace is even and either 0 or 14 (divisible by 7). Mirrors the run's
  `wilbrink-order11-makhnev` / `makhnev-symmetric-graphs` finding that order-7
  automorphisms force a one-fixed-point structure (Cesarz–Woldar: 7||G| ⇒ G ≅ Z₇).

## Relation to in-library material

- **Automorphism orders**: Thm 6.1–6.3 (no p>14, 13, 11) agree with and partially
  replicate the stronger sourced results (Makhnev–Minakova: |G| | 2·3³·7·11;
  Wilbrink: no order 11; Cesarz–Woldar: 7||G| ⇒ Z₇). The orbit-matrix eigenvalue
  technique in Thm 6.3 is the same family of argument as Crnković–Maksimović.
- **alpha = 22**: matches `coclique-bound-closed-form` (checked). The α=22 ⇒
  (22,4,2)-block-design reduction is new to the library and sits on the
  `spread-resolvable-partial-sts` / `pq-2-6-2-classification` angle: it is a
  design-theoretic refinement of the independent-set extremal case.
- **α ≥ 10** (Guseinov) and **α ≤ 22** (here, and the run's closed form) bracket
  alpha ∈ [10, 22] for a putative (99,14,1,2).

## Caveats for downstream use

Treat Thm 4.1/4.3's equations as independently re-derivable and re-derive them
before building a nonexistence argument on them; the paper is unrefereed and a
PRIMES write-up. The (22,4,2) block-design encoding is a genuine new reduction:
a finite-design constraint worth checking (does any (22,4,2) block design with the
extra "no repeated block / no 3-shared block" conditions lift to a graph?).
