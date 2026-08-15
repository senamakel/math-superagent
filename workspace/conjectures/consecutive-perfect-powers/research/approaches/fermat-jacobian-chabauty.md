# Approach: Fermat curve / Jacobian / Chabauty–Coleman

```approach
idea: View integer solutions of x^p - y^q = 1 as rational points on the affine
       curve C : X^p - Y^q = 1, pass to its smooth projective model (a Fermat
       curve), and attack the finiteness of C(Z) via the Jacobian — Weil's
       decomposition of the Fermat Jacobian into abelian varieties with complex
       multiplication, combined with Chabauty's method (or Chabauty–Coleman
       beyond genus 1) on the group of rational points.
mechanism: For gcd(p, q) = 1 the smooth projective model of X^p - Y^q = 1 has
       genus g = (p-1)(q-1)/2. Weil showed the Jacobian J of the Fermat curve
       X^p + Y^p = Z^p (equivalently, up to a twist, X^p - Y^q = Z^{?}) is
       isogenous to a product of abelian varieties of CM type, so its
       L-function factorises and its Mordell–Weil rank can be analysed via CM
       theory. Chabauty's theorem: if rank(J(Q)) < g, then C(Q) is finite and
       effectively computable; Chabauty–Coleman extends the method to cases
       where the rank is slightly larger by p-adic integration. For the Catalan
       curve the interesting regime is p, q both odd primes, where g grows but
       the CM decomposition gives the rank bound in terms of the minus part of
       the class group of Q(zeta_p) — connecting this geometric route back to
       the class-group obstruction, but now through the arithmetic of the
       Jacobian rather than through ideal factorisation of (x - zeta_p^i).
status: refuted
precedent: Hazama "Hodge cycles on the Jacobian variety of the Catalan curve" 1997 https://doi.org/10.1023/a:1000106427229 ; Goodson "Sato-Tate distributions of Catalan curves" J. Theor. Nombres Bordeaux 2023 https://doi.org/10.5802/jtnb.1238 ; Murabayashi "Mordell-Weil rank of jacobians of curves y^p=f(x)" Acta Arith. 64 (1993) https://doi.org/10.4064/aa-64-4-297-302 ; Dogra "Chabauty-Coleman method and p-adic linear forms in logarithms" https://arxiv.org/abs/2008.09560 ; Balakrishnan-Besser-Bianchi-Muller "Explicit quadratic Chabauty over number fields" https://doi.org/10.1007/s11856-021-2158-5 ; Lorenzini-Tucker "Thue equations and the method of Coleman-Chabauty" https://arxiv.org/abs/math/0005186
killed-by: The Catalan curve X^p - Y^q = 1 (gcd(p,q)=1) is NOT the Fermat curve X^N + Y^N = Z^N. Multiple independent sources (Hazama, Goodson, Murabayashi, Dogra) state it is a superelliptic/cyclic cover, y^q = x^p - 1 (a (p,q)-twist of a hyperelliptic/cyclic cover), whose Jacobian has CM-type by Q(zeta_p, zeta_q) — real and named, but not "the Fermat Jacobian", so Weil's CM decomposition of the Fermat Jacobian does NOT apply as literally stated. Moreover the method is conditional on rank(J(Q)) < g, and no general Mordell-Weil rank formula is known for these Jacobians (Murabayashi, Goodson): the rank bound is exactly as hard as the class-group obstruction it was meant to avoid. The corrected statement (genus (p-1)(q-1)/2 holds; a CM JP of dimension g with CM by Q(zeta_p,zeta_q) exists; Chabauty applies iff rank < g) is grounded, but as a route to a proof it is a conditional theorem whose hypothesis is the original obstruction.
research-note: Corrected object is live as a thread but not as stated. The honest value: Chabauty/Chabauty-Coleman would settle C(Z) for a fixed (p,q) with rank < g, but establishing rank < g for all odd prime pairs is the same obstruction. Do NOT re-propose "Fermat Jacobian" without the corrected object.
first-step: Fix the smooth model of X^p - Y^q = 1 and its genus (g = (p-1)(q-1)/2
       for gcd(p,q)=1; handle the degenerate p=q and the one-exponent-even
       elliptic case p=2, q=3 separately), then write the Weil CM decomposition
       of the Fermat Jacobian and identify which isogeny factors must carry the
       rational points of the Catalan curve.
```

## What this buys

A change of object. The run's current line works with *ideals* in `Z[zeta_p]`
and their class-group ambiguity. This line works with the *abelian variety* J
and its rational points. The two are genuinely different: the class group of a
cyclotomic field is arithmetic information about `Q(zeta_p)`, while the
Mordell–Weil group of the Fermat Jacobian is geometric information about the
curve that *carries* the solutions. Weil's decomposition is what bridges them
(the CM factors have fields of definition whose class groups control their
ranks), so the obstruction is not avoided but is repackaged in a form where
standard geometric tools (Chabauty, Coleman integration, Chabauty–Kim) apply.

## The known solution and where it sits

At `3^2 - 2^3 = 1`: `(p, q) = (2, 3)`, `gcd(p,q) = 1`, `g = (2-1)(3-1)/2 = 1`.
So the known solution lives on an *elliptic curve* `X^2 - Y^3 = 1` (a Mordell
curve, isomorphic to `y^2 = x^3 - 1` up to twist), and Chabauty is vacuous there
(rank may equal genus). The falsification oracle says: **any lemma that claims
"rank < g for all p, q" is false**, because the known solution exists on the
genus-1 case and would need `rank(J(Q)) = 1 = g`. The honest statement is
conditional: for odd primes p, q (both ≥ 3) with p ≠ q, Chabauty–Coleman applies
whenever the CM-decomposition gives `rank(J(Q)) < g`, and that rank bound is
what must be established (or assumed and named exactly) — it is not automatic.

## Why it beats the standard alternative here

- The class-group route is stuck at the *ideal → element* lift, i.e. at
  principality. Chabauty bypasses principality entirely: it counts rational
  points on the curve directly via p-adic integration, so an ideal that is not
  principal does not block the argument — the Jacobian already accounts for it.
- The method is a *proved finiteness theorem with an effective computing step*
  (Coleman's explicit Chabauty computes the finitely many points), so it is a
  theorem-shaped route, not a search.
- It has known successes on exactly this shape of equation (generalised Fermat
  equations have been solved for many small exponent triples by the modular
  method's sibling, the Chabauty method, and by p-adic approaches to Fermat
  curves).

## What could kill it

1. **The genus is huge for large p, q**, and Chabauty–Coleman needs the rank to
   be strictly below g. The CM decomposition might bound the rank far below g
   (that is the hope), but establishing `rank < g` for *all* odd prime pairs is
   precisely as hard as the class-group obstruction it repackages — the approach
   would then be a conditional theorem `rank(J) < g ⟹ no solution`, which is a
   genuine partial result but not the whole.
2. The p = q case is degenerate (X^p - Y^p factors over Q, the curve is
   reducible) and must be handled separately; forgetting this produces a false
   genus formula.
3. The genus formula `(p-1)(q-1)/2` is only for `gcd(p,q)=1`; using it blindly
   for p = q (or for the affine model without the smooth compactification)
   manufactures a wrong genus, which the falsifier must catch.

## Cost

Formalising the smooth model and the Weil decomposition is symbolic algebra
(sympy / Singular for the curve; the decomposition is classical and can be
quoted once sourced). Running Chabauty–Coleman is a p-adic computation (Coleman
integrals) doable in Sage-like tooling for small p, q. The cost is in
*establishing* the rank bound, not in any computation that grows with the
problem's effective bound.
