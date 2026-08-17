# Raicu–Sam–Weyman–Yang 2026 — Powers of binary forms and derived Hermite reciprocity

<!-- source: https://arxiv.org/pdf/2602.15175 -->
Claudiu Raicu, Steven V Sam, Jerzy Weyman, Fuxiang Yang, "Powers of binary forms and derived Hermite reciprocity" (arXiv:2602.15175v1, 16 Feb 2026). Full text: [[raicu-sam-weyman-yang2026_powers-binary-forms-hermite.full]].

## What it establishes

Let `P^d = P(Sym^d C^2)` parametrize complex binary forms of degree d up to scaling. For a partition `λ ⊢ d`, `X_λ = {[F]: F = L_1^{λ_1} L_2^{λ_2} … , L_i linear}` is the coincidence-root (factorization) locus. The **pure-power locus** `λ = (ab)`, `d=ab`, is the main theorem's target.

```claim
id: rswy-powers-binary-forms-ideal
statement: For a,b≥2, d=ab, the homogeneous ideal I(X(ab)) of the locus of a-th powers of degree-b binary forms is generated in degree b+1 (by the maximal minors of a matrix of linear forms) and has a linear minimal free resolution; its projective dimension is d−1. The Foulkes–Howe map Sym^k(Sym^{ab} C^2) → Sym^{ak}(Sym^b C^2) is injective for k≤b and surjective for k≥b (Thm 1.4). Key rank criterion: for the bilinear map ω: Sym^d U × Sym^b U → Sym^{d+b−2} U, ω(F,G)=0 (the associated matrix drops rank) iff [F]=[G^a]∈P^d (eq 1.2b).
hypotheses: a,b≥2, d=ab, binary forms over C.
holds-here: yes for the rank criterion (the ω(F,G)=0 ⟺ F=G^a characterization is the structure of the pure-power target variety of the CA scheme); the ideal generation theorem itself concerns X(ab) which is NOT the CA target.
status: proved (claim of the paper's main theorem)
bearing: The CA conclusion is f = L^n, a pure power of a LINEAR form — this is λ=(n) with b=1, the rational normal curve, the trivial ACM case EXCLUDED from Theorem 1.1 (b=1 is ACM, X_{1,n} is the rational normal curve). So the ideal-generation theorem does not directly settle the CA target. Its value is the ω rank-drop criterion: it gives the homogeneous equations (minors) that cut out the pure-power locus the CA scheme must prove is the only solution. Also CONFIRMS Abdesselam–Chipalkatti's Conjecture 5.1(c1) in the equal-parts case.
anchor: research/sources/raicu-sam-weyman-yang2026_powers-binary-forms-hermite.full.md (Thm 1.1, Thm 1.4, eq 1.2b)
contradicts: none (agrees with the run's held Abdesselam-Chipalkatti Hessian claim)
follows-from: none (RSWY's ideal-generation theorem is genuinely new: it PROVES AC's open Conjecture 5.1 in the equal-parts case rather than following from it; it is built on, not logically derived from, the AC Foulkes-Howe analogue)
answers: none
```

## Cross-source confirmation (new)

RSWY 2026 Thm 1.1 **proves** AC's **Conjecture 5.1** (AC2012: for `r | d`, (c1) `I_X`
minimally generated in degree `r+1`, (c2) `g = I_X`) in the equal-parts case `d = ab`
(with `r = a`, generation degree `b+1 = r+1`). This is the genuine cross-link between
the two held sources: they corroborate each other on the structure of power loci.

## Honest assessment — supporting, not load-bearing, for CA

Resolves the defining ideal of the equal-parts power locus — complete and beautiful,
but the CA-relevant "power of a single linear form" (b=1, rational normal curve) is
precisely the trivial ACM case its theorem excludes. What the run takes from it: the
ω-rank-drop homogeneous-minors description of `F = G^a`, the algebraic shape of CA's
pure-power conclusion. It corroborates the held Abdesselam–Chipalkatti line but
introduces no new CA constraint. Filed so nobody re-derives the SL2-equivariant
resolution machinery against a task that only needs the b=1 rational-normal-curve case.
