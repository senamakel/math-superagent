# Crnković & Maksimović, "Construction of strongly regular graphs having an automorphism group of composite order" (Contributions to Discrete Math 15(1), 2020; doi 10.55016/ojs/cdm.v15i1.62323)

## What the paper establishes

A method for constructing strongly regular graphs from orbit matrices admitting an automorphism group of composite order, generalising Lam–Behbahani's orbit-matrix algorithm (which handles prime order).

Main applications:
- Classifies srg(49,18,7,6) admitting an automorphism group of order 6 (11 new; 385 more by switching; at least 727 up to isomorphism).
- **For this run's problem:** *there are no srg(99,14,1,2) with an automorphism group of order six or nine*, i.e. automorphism groups isomorphic to Z₆, S₃, Z₉, or E₉ are all ruled out.

## Implication here

Directly answers GOAL's question on excluded automorphism orders. Jointly with Cesarz–Woldar (computer-free: 7||G| ⟹ Z₇, 2||G| ⟹ |G||6), the allowed group structure is very restricted. Crnković–Maksimović's method is computational (orbit-matrix enumeration/classification), so the Z₆/S₃/Z₉/E₉ exclusions are computational results, not hand proofs — contrast with Cesarz–Woldar's computer-free 2-part and 7-part.

```claim
id: aut-cm-2020
statement: No srg(99,14,1,2) has an automorphism group isomorphic to Z6, S3, Z9, or E9 (orders 6 and 9). Consequently the order of the automorphism group of any (99,14,1,2) is of the form 2^a 3^b with b in {0,1} (and the allowed orders surviving other constraints).
hypotheses: existence of srg(99,14,1,2) assumed; orbit-matrix classification method.
holds-here: yes — the 99 case.
status: sourced (Crnkovic-Maksimovic 2020 abstract, Contributions to Discrete Math; computational orbit-matrix method)
bearing: together with aut-cw-2025 narrows Aut(99-graph) to a very small (likely trivial) set; excludes the composite orders a symmetry search would need.
anchor: research/sources/crnkovic-maksimovic-composite-automorphism.full.md
contradicts: none; refines Makhnev-Minakova 2004 (recalled in problem.md) which only bounded |G| | 2.3^3.7.11.
```

## Does not settle

Existence of (99,14,1,2). Whether |G|=2,3,6,7 or 1 is actually possible.

[[crnkovic-maksimovic-composite-automorphism.full]]
