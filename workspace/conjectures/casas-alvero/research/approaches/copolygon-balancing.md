# Non-Archimedean copolygon / Berkovich balancing

```approach
idea: Attach to f the Newton copolygon — the piecewise-linear convex function on the Berkovich
      line whose left and right slopes at every point are the valuations of the roots of f on
      the two sides of that point (Gauss point = unit disk point). Reformulate CA: H_i(f)(r_i)=0
      with f(r_i)=0 is a coincidence condition between the copolygon of f and the copolygon of
      H_i(f), which is the same polygon with slopes shifted by binomial-coefficient weights.
mechanism: The copolygon of f determines, for every point of the Berkovich affine line, the
      multiset of root-valuations, and the copolygon of H_i(f) is obtained from it by a slope
      perturbation (each slope s_β contributes a weighted combination at the same points). The
      equation H_i(f)(r_i) = 0 says: a point r_i, which is a zero of f (one slope of the
      copolygon), must simultaneously make the perturbed polygon touch zero — a balancing
      condition among slopes. Requiring this for all i forces the n slope-intercepts to coincide
      (all roots have equal valuation at every point), which over an algebraically closed char-0
      field forces f to be a power. This is the non-Archimedean/Gauss–Lucas avatar of the
      real-rooted convex-hull result the run already holds (Polstra), promoted to a *global*
      invariant instead of one convex hull.
status: refuted
killed-by: refuted on paper. The load-bearing inference fails in characteristic 0, not merely char p: the copolygon records only root *valuations*, and slope-coincidence (a one-segment polygon) does not force a pure power — x^2 - p over Q_p has a single-segment Newton polygon (both roots valuation 1/2) yet is squarefree with two distinct roots. So "slope-coincidence => pure power" fails exactly where the proposal locates its char-p break, and the route has no surviving inference. Independently: C carries no non-Archimedean valuation, so there is no copolygon over C — one valuation at a time is precisely the pdic method the proposal disclaims, not a global invariant bundling all valuations; and the claimed slope-shift identity (Newton polygon of H_i = that of f with binomial weights) is not a theorem, since the polygon of a derivative is a lower convex hull of a shifted point set.
first-step: Implement the copolygon (sympy/PARI, exact, over Q or a number field) and verify
      the slope-shift identity H_i(f) → copolygon of f with weighted slopes on small f (n = 4,5,6,
      guard set (x−1)^n and the char-p witness). Then check the key fact: is "f and H_i(f) share
      a root" equivalent to a *single* local balancing identity of the two polygons, exact in the
      Hasse convention? That single identity is what the whole route reduces to.
```

## What is established vs. what is speculation

- **Established (named theory, source to confirm):** Newton polygons/copolygons of
  polynomials and their behaviour under derivatives/translation (Cassels, *Local Fields*;
  the Berkovich-line account is in Rüth's and Baker–Rumely's treatments). The fact that the
  copolygon records the valuations of *all* roots at every point is standard. The Gauss–Lucas
  geometry it encodes is exactly the constraint the run already holds as load-bearing
  (`real-rooted-and-convex-hull`, Polstra 2012; `min-counter-structure`, Laterveer–Ounaïes).
- **Speculation (mine, to be attacked):** the claim that the n−1 conditions reduce to one
  clean balancing identity and that it forces slope-coincidence. No source in the library
  does this.

## Char-`p` break (mandatory)

The Newton-polygon side is characteristic-free (it only needs a valuation), but the
"all slopes coincide ⇒ pure power" inference uses `char = 0` (separability) — in char `p`
coincident valuations permit `x^{p+1} − x^p`-type polynomials. So the expected break is
*exactly* the final step (slope-coincidence ⇒ monomial-in-one-factor), and the witness
`x^{p+1} − x^p` must survive every earlier step of the argument and fail only there. That
is a precise, checkable char-p break — better than "the hypothesis is meaningless", which
killed the walsh-coincidence route.

## Why it is not a restatement of a closed approach

- Not tropical-resultant-fan: that tropicalized the *ideal of resultants* over the
  coefficient ring; this attaches one copolygon to *one polynomial f* over the *root
  field*, a strictly smaller object, and asks for a balancing identity, not a fan.
- Not the Draisma–de Jong `pdic-valuation-method`: that uses one `p`-adic valuation per
  prime in a reduction-mod-`p` counting argument; the copolygon is the char-0-global
  invariant bundling *all* valuations simultaneously, and its output is a geometric
  coincidence statement, not a mod-`p` count.

## Honest likely output

A geometric certificate that "CA ⟺ the copolygon of f is a single straight line", i.e. a
new, checkable reformulation with a sharp char-0 break, plus a new family of restrictions
(valuation-theoretic constraints on a minimal counterexample). If the single-identity
reduction fails, the failure shape (which i's need more than the copolygon) is itself data.
