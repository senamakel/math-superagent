# Non-abelian Chabauty (Kim) — past the refuted rank < g hypothesis

```approach
idea: Replace the refuted abelian Chabauty (rank J(Q) < g) by Minhyong Kim's non-abelian Chabauty — π_1^un and the Selmer variety — where rational points are a proper subvariety of the local space even when rank(J) ≥ g. Apply to the Catalan superelliptic curve y^q = x^p − 1, whose Jacobian has CM by Q(ζ_p, ζ_q).
mechanism: for a superelliptic/cyclic-cover curve with CM Jacobian, the Galois action on π_1^un is determined by the CM field, so Selmer variety and Coleman integrals are machine-computable for fixed (p,q); finiteness (or an effective determination of rational points) follows when Sel(X) has positive codimension.
status: refuted
killed-by: finiteness-only-no-effective-determination (the genus-≥4 obstruction the proposal guessed is refuted by Ellenberg–Hast; the real obstruction is that CK gives finiteness, not a computable ruling-out, and effective CK at varying genus ≥ 4 is infeasible in the same orders of magnitude already ruled out for effective bounds)
precedent: Ellenberg–Hast, "Rational points on solvable curves over Q via non-abelian Chabauty", https://doi.org/10.1093/imrn/rnab141; Balakrishnan–Dogra–Müller–Tuitman–Vonk, "Explicit Chabauty–Kim for the split Cartan modular curve of level 13", https://doi.org/10.4007/annals.2019.189.3.6; Betts–Corwin–Leonhardt, "Bounds on the Chabauty–Kim locus of hyperbolic curves", https://doi.org/10.48550/arxiv.2206.11085; geometric quadratic Chabauty, https://www.sciencedirect.com/science/article/pii/S0723086923000452
```

**Literature verdict: REFUTED — but by a *different* reason than the genus one the proposal guessed.**

## The proposal's own kill-shot question has a documented answer, and it is *no*

The proposal's first step is: "Determines whether any Chabauty–Kim variant survives genus ≥ 4. If none does, the line closes fast with the genus obstruction named."

That premise is **false on the literature**. Ellenberg–Hast, "Rational points on solvable curves over Q via non-abelian Chabauty" (Int. Math. Res. Not., 2021; https://doi.org/10.1093/imrn/rnab141), prove: **any smooth superelliptic curve `y^d = f(x)` of genus ≥ 2 over Q has finitely many rational points**, obtainable through non-abelian Chabauty — precisely because it geometrically dominates a curve with CM Jacobian and so satisfies Kim's dimension hypothesis. The Catalan curve `y^q = x^p − 1` is exactly such a superelliptic curve, with genus (p−1)(q−1)/2 ≥ 4 for every distinct-odd-prime pair. So Kim's method **does survive genus ≥ 4** for this curve; "the genus obstruction" that would close the line is not an obstruction.

## So the line does not close on genus. It closes on a deeper ineffectiveness.

The Ellenberg–Hast result is a **finiteness** theorem (a Faltings-type statement), not an **effective determination** of the finite set. The candidate's actual hope — to *compute* the rational points on each Catalan curve to rule out a second solution — requires *explicit/effective* non-abelian Chabauty. The only worked explicit cases in the literature (Xs(13), genus 3 with rank = genus — Balakrishnan–Dogra–Müller–Tuitman–Vonk, https://doi.org/10.4007/annals.2019.189.3.6) are hard one-off computations at genus 3. There is no effective CK framework that runs at genus ≥ 4 while the pair (p,q) varies over all odd primes; the Bloch–Kato Selmer data involved are exactly as hard as (in practice harder than) the class-group data this run already treats as the obstacle.

Nor, even in principle, would the computation settle the problem: finiteness does not distinguish the known solution (3,2,2,3) — which, with p=2, lies on no *odd-prime* Catalan curve — from a hypothetical second solution. Both would be rational points on whatever curve; the method's conclusion is "the set is finite," which the run already knows (Tijdeman/Baker bounds), and it does not say "the set is {the known point}."

So the honest closure: the *finiteness* side of non-abelian Chabauty is fully grounded and even has a theorem tailored to this curve (Ellenberg–Hast); the *effective/ruling-out* side is ungrounded and, at varying genus ≥ 4, infeasible in exactly the orders of magnitude the run has already flagged for effective bounds (GOAL.md). The proposal's suggested "genus obstruction" was the wrong obstruction; the real one is finiteness-versus-effectivity.

precedent: Ellenberg–Hast, "Rational points on solvable curves over Q via non-abelian Chabauty", https://doi.org/10.1093/imrn/rnab141 (superelliptic y^d=f(x), genus ≥ 2, CM-dominated ⇒ dimension hypothesis ⇒ finiteness via non-abelian Chabauty); Balakrishnan–Dogra–Müller–Tuitman–Vonk, "Explicit Chabauty–Kim for the split Cartan modular curve of level 13", https://doi.org/10.4007/annals.2019.189.3.6 (only worked explicit genus-3 example); Betts–Corwin–Leonhardt, "Bounds on the Chabauty–Kim locus of hyperbolic curves", https://doi.org/10.48550/arxiv.2206.11085 (effective CK bounds conditional on TS/Bloch–Kato, in terms of p, g, r); Besser–Balakrishnan–Dogra, geometric quadratic Chabauty, https://www.sciencedirect.com/science/article/pii/S0723086923000452.
killed-by: finiteness-only-no-effective-determination (the genus-≥4 obstruction the proposal guessed is refuted by Ellenberg–Hast; the real obstruction is that CK gives finiteness, not a computable ruling-out, and effective CK at varying genus ≥ 4 is infeasible in the same orders of magnitude already ruled out for effective bounds).
