# Pinned centroid — pinning the top derivative's root in the scenario machinery (adopted, synthesis)

```approach
idea: The top Hasse derivative is linear, H_{n-1}(f)(x) = nx + a_1 (where a_1 is the coefficient of x^{n-1} in monic f), with the single root c = -a_1/n = (Σ_j β_j)/n, the centroid of the root multiset. Hence gcd(f, H_{n-1}f) ≠ 1 ⇔ f(c) = 0: any Casas-Alvero polynomial over a field with n invertible has its own centroid among its roots. THIS CONDITION IS NOT NEW — it is the i = n-1 case of the hypothesis, and the literature already uses it (see Knownness below). The new content is what the condition does to the scenario/tuple machinery: it pins the last coordinate.
mechanism: For monic f = ∏(x-β_j), the adopted identity H_i(f)(β_j) = e_{n-i}(β_j-β_1,…,[j removed],…,β_j-β_n) at i = n-1 gives e_1 = Σ_{k≠j}(β_j-β_k) = nβ_j + a_1 = n(β_j - c). So the root witnessing derivative n-1 is *forced* to be β_j = c: the last coordinate j_{n-1} of every scenario tuple T = (j_1,…,j_{n-1}) in Ghosh's G_{T,i} / regular-sequence reformulation is fixed — the scenario set shrinks from n^{n-1} to n^{n-2}, and each G_{T,n-1} becomes the single linear form. Over char 0, f = (x-c)·g gives centroid(g) = c, a monic degree-(n-1) form with the same pinned point, the explicit descent f ↦ g (translate c to 0: f = x·g, a_1 = 0). The two facts (the condition, the pinning, the descent identity) are proved; the induction "g is Casas-Alvero of degree n-1" is speculation.
status: refuted
killed-by: non-distinct — it is the i = n−1 (e_1) case of the adopted
      root-difference-coloring identity H_{n−1}(f)(β_j) = n(β_j−c). The pinning
      of scenario coordinate j_{n−1} and the descent f=(x−c)·g are absorbed into
      research/approaches/root-difference-coloring.md (primary line); its only
      load-bearing step — "g inherits CA of degree n−1" — is the same unproved
      induction, now stated explicitly as the attack target there. Folded, not
      discarded.
first-step: (tool_builder, exact sympy, oracle-guarded via lib.casas_alvero) (1) Verify H_{n-1}(f) = nx + a_1 and f(c) = 0 ⟺ gcd(f, H_{n-1}f) ≠ 1 for random monic f at n = 4,5,6,8; (2) verify f = (x-c)g with centroid(g) = c over QQ; (3) run the guard set: (x-1)^n passes (c = 1, a root), a generic f fails, and the char-p witness x^{p+1}-x^p over GF(p) for p = 2,3,5,7 — confirm the centroid condition *holds there* (c = -a_1/n = 1/(p+1) = 1 is a root) but the descent centroid(g) = c *fails* because n-1 = p ≡ 0 (the named break); (4) for n = 5,6 count scenario tuples T = (j_1,…,j_{n-1}) with j_{n-1} forced to the centroid root versus all n^{n-1}, and compare to the run's existing scenario count — the concrete saving this refinement buys.
precedent: root-difference-coloring (adopted: H_i(f)(β_j) = e_{n-i}(β_j-β_*)); ghosh-complete-intersection (the G_{T,i} scenario reformulation); castryck2012 Lemma 6 + Prop 15/16 (the root of f^{(d-1)} = centroid already used as a distinguished point); polstra-convex-hull. The e_1 case of the adopted identity is this file's engine; the scenario-pinning and the explicit descent are this approach's own content.
charp-break: two distinct, named breaks. (i) The linear step H_{n-1} = nx + a_1 needs n invertible: at p | n, H_{n-1} drops to the constant a_1 and the condition becomes "a_1 = 0", not "centroid is a root". (ii) The descent "centroid(g) = c" divides by n-1: it fails exactly at p | n-1. The witness x^{p+1}-x^p has n = p+1, so step (i) survives (c = -a_1/n = 1 is a root) while step (ii) fails (n-1 = p ≡ 0) — the char-p counterexample sits precisely on the descent break, which is where any CA proof must die.
```

## Status of the parts

- **Proved (elementary, char-free up to the named divisions):** (a) H_{n-1}(f)(x) = nx + a_1; (b) the single root of H_{n-1}(f) is the centroid c = -a_1/n; (c) therefore gcd(f, H_{n-1}f) ≠ 1 ⇔ f(c) = 0 whenever n is invertible; (d) H_{n-1}(f)(β_j) = n(β_j - c), so the only root of f that can witness derivative n-1 is β_j = c. (e) over char 0, f = (x-c)g ⟹ centroid(g) = c. All are one- or two-line coefficient computations; hand-verified, machine verification is the first step.
- **Speculation:** that the pinned centroid, together with the remaining n-2 conditions, forces g to be Casas-Alvero of degree n-1 (the induction). This is unproved, and it overlaps with Ghosh's claimed "downward induction" — the exact relation to that claim must be checked before relying on it.

## Knownness (honest correction, after reading the held source)

The centroid condition **is known**, in the literature's own normalization. Castryck–Laterveer–Ounaïes 2012 (arXiv:1208.5404, `research/sources/castryck2012_degree12_html.full.md`) use form (6) `f = x^d + (d choose 1)a_1 x^{d-1} + … + (d choose d-1)a_{d-1} x` with sum of roots `-d·a_1`, so the centroid is `-a_1` = the root of `f^{(d-1)}`; their d = p+1 normal form (line ~470) lists `x_d = -a_1` *as a root of f*, and Prop 15/16 derive that this root is simple and is not the mean of two distinct roots. So "the centroid is a root" is the trivial `i = d-1` case of the hypothesis, already used there, NOT new. What this approach adds is (i) the *pinning of the scenario coordinate* `j_{n-1}` in Ghosh's tuple machinery, (ii) the explicit descent `f = (x-c)g` with `centroid(g) = c`, and (iii) the phrasing as a dimension-one drop (one scalar equation replacing the (n-1)-st resultant). Claim those, not the condition.

## Why it is not one of the closed approaches

None of the closed lines (catalecticant, copolygon, Mason-Stothers, milnor, Ritt, tropical, Walsh) pins the top derivative's root into the scenario machinery. It is a refinement of the *adopted* root-difference-coloring line (its e_1 case) and of the run's ghosh-complete-intersection scenario data: it sharpens adopted engines rather than re-opening a refuted one.
