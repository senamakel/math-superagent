# Cesarz & Woldar, "On the automorphism group of a putative Conway 99-graph" (Algebraic Combinatorics 8(2), 2025, pp. 379-398; doi 10.5802/alco.418; arXiv:2308.02978)

## What the paper establishes

Let Γ be a Conway 99-graph, i.e. an srg(99,14,1,2), and G = Aut(Γ). Main results, with **computer-free proofs**:

- **If 7 divides |G| then G ≅ Z₇.**
- **If 2 divides |G| then |G| divides 6**, i.e. G is isomorphic to one of Z₂, Z₆, S₃.

These refine earlier results: Makhnev & Minakova 2004 prove |G| divides 2·3³·7·11, and further show that if |G| is divisible by 2 then |G| divides 42. Cesarz–Woldar sharpen the 2-part to |G| | 6 and give the 7-divisibility structural conclusion.

(The arXiv version's Frob(21)-elimination step is computer-assisted; the published Algebraic Combinatorics version says the 2| and 7| claims are computer-free. See claim `aut-bounds-established` for the status nuance.)

## Implication here

Directly answers GOAL's second question (which automorphism orders are excluded). Combined with Crnković–Maksimović 2020 (no Z₆, S₃, Z₉, E₉), the automorphism group of any (99,14,1,2) is very small — the allowed orders are suborders of {Z₂, Z₆, S₃, Z₇} with the composite orders ruled out, likely trivial. This is why symmetry-assuming construction searches have largely been eliminated, and why no search under a nontrivial group has settled it.

```claim
id: aut-cw-2025
statement: If 7 | |G| then G ≅ Z_7 and if 2 | |G| then |G| | 6 (G in {Z2,Z6,S3}) for G=Aut of a putative srg(99,14,1,2), with computer-free proofs.
hypotheses: existence of srg(99,14,1,2) assumed (conditional constraints on the hypothetical group).
holds-here: yes — this is exactly the 99 case.
status: sourced (published Algebraic Combinatorics 2025, computer-free claims; arXiv version has a computer-assisted Frob(21) elimination)
bearing: the automorphism group is very small (likely trivial), eliminating symmetry-assuming search routes.
anchor: research/sources/automorph-putative-conway-99-graph.full.md
contradicts: none — confirms and sharpens Makhnev-Minakova 2004 as recalled in problem.md
```

## Does not settle

Existence of (99,14,1,2). Whether |G| can be 2, 3, 6, 7 or is necessarily trivial — it bounds, does not decide.

[[automorph-putative-conway-99-graph.full]]
