# Mourtada 1991 — finite cyclicity of hyperbolic polycycles (primary)

```claim
id: h16-mourtada-1991-hyperbolic-finite-cyclicity-primary
status: asserted
statement: Mourtada (1991), "Cyclicite finie des polycycles hyperboliques de champs de vecteurs du plan. Algorithme de finitude", Ann. Inst. Fourier 41(3):719-753: (Theorem 0) for every n there is an open dense O_n in the space P_n of planar polynomial fields of degree <= n such that H16-part-2 is locally true on O_n: every X in O_n has a neighbourhood V_X and bound N_X on the number of limit cycles of all Y in V_X. (Theorem 3) there is a finite set G(k) of algebraic generic conditions on the hyperbolicity ratios (r_1,..,r_k) of a hyperbolic monodromic polycycle Gamma_k, containing all product conditions prod_{j in J} r_j != 1, and an integer e(k) such that every Gamma_k satisfying G(k) has cyclicity <= e(k) in every C^infty family. For k <= 3 all G(k) conditions are of product type; for k >= 4 some are not; e(k) satisfies recurrences in k with an explicit coarse bound.
hypotheses: planar vector fields; hyperbolic monodromic polycycles (vertices hyperbolic saddles, possibly at infinity); C^infty families; generic = hyperbolicity-ratio point in an open dense subset of R^k.
holds-here: yes (as the primary anchor for "hyperbolic polycycles are finitely cyclic" in the C^infty category); does NOT cover non-hyperbolic graphics (nilpotent, degenerate, semi-hyperbolic) — exactly the open DRR rows.
evidence-class: sourced (open-access PDF full text held, research/sources/mourtada-1991-cyclicite-finie-polycycles-hyperboliques-pdf.full.md)
falsifier: a generic hyperbolic polycycle (ratios satisfying G(k)) and a C^infty family with more than e(k) limit cycles bifurcating from it — none known; the recurrences defining e(k) are stated but the coarse bound is what is explicit, so any quantitative use must cite the bound form actually given.
anchor: research/sources/mourtada-1991-cyclicite-finie-polycycles-hyperboliques-pdf.full.md
follows-from: h16-dulac-finiteness-theorem
answers:
```

## Why this block is in research/claims/

This is the same claim block previously carried in
`research/summaries/mourtada-1991-cyclicite-finie-polycycles-hyperboliques.md`. The
entailment parser only resolves `follows-from:` edges to claim blocks in
`research/claims/`, so the two Dukov claims (which follow from this Mourtada anchor)
were being flagged as "following from nothing". Moving the block here (content
unchanged) makes the entailment edge resolvable. The source summary keeps its full
digest.
