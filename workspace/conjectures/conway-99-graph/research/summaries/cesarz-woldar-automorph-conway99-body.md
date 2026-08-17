# Cesarz & Woldar — "On the automorphism group of a putative Conway 99-graph"

**Source:** https://arxiv.org/html/2308.02978v1 (arXiv:2308.02978; published version at
https://alco.centre-mersenne.org/articles/10.5802/alco.418/, Algebraic Combinatorics 8(2)). 
Full text: `research/sources/cesarz-woldar-automorph-conway99-body.full.md`.
**This is the full proof body of the paper** — the `cesarz-woldar-automorph-conway99` file is
only its arXiv landing page, and this was the one automorphism source whose proof body the
library was missing.

## What it establishes

Let Γ be a putative Conway 99-graph, i.e. srg(99,14,1,2), and G = Aut(Γ).

- **(1′)** If 7 divides |G| then G ≅ **Z₇**. (The strengthening of Makhnev–Minakova's
  "|G| | 42" and Makhnev's Cor 2.4.)
- **(2′)** If 2 divides |G| then |G| divides **6**, i.e. G ∈ {Z₂, Z₆, S₃}.
- **No order-14 automorphism** (Section 3): Γ embeds into symmetric group of degree 14
  under a 7-divisibility labelling; a cyclic K of order 14 is excluded by adjacency-count
  analysis of the 14 vertices and their labels.
- If 7 | |G|, the stage-2 result is G ≅ Z₇ **or Frob(21)** (the Frobenius group of order 21).
- **Frob(21) is eliminated by computer** (Sections 5–6): a structural framework on Γ under
  G ≅ Frob(21) — orbit valencies determined in Section 4 — reduces the computer search to a
  feasible enumeration, which finds no graph. So divisibility by 7 forces G ≅ Z₇.
  **This is the computer-assisted step; (1′),(2′) without it give Z₇-or-Frob(21).**

The paper confirms the Makhnev–Minakova background: srg(v,k,1,2) exists only for
k = u²+u+2, u ∈ {1,3,4,10,31}; 99 ⟷ u=3; exists for u∈{1,4} (i.e. rook(3)=srg(9,4,1,2)
and BvLS=srg(243,22,1,2)).

## Bearing on the run

Together with **Crnković–Maksimović 2020** (no Z₆,S₃,Z₉,E₉) and **Behbahani–Lam 2011**
(prime divisors of |G| ⊆ {2,3}), the net automorphism picture is: a nontrivial G, if any, is
at most Z₂, Z₃, or Z₇ — and triviality of G remains **open**. This confirms the claims
`aut-cw-2025`, `automorphism-orders-consolidated`, `c3`: 2||G| ⟹ |G| | 6; 7||G| ⟹ G ≅ Z₇.
The only excluded-order finding that rests on the computer is the Frob(21) elimination,
noted in the claims ledger as computer-assisted.

Full claim block lives in `research/notes/automorphism-orders-consolidated.md`
(`answers: exact-list-prime-051a`).
