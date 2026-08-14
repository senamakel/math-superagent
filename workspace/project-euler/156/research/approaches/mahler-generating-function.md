# Approach — Mahler functional equation for the generating function

```approach
idea: Recover the fixed-point sets of f(n,d)=n from the Mahler functional
equation of the ordinary generating function G_d(x) = Σ_n f(n,d) x^n, using
the Mahler↔regular-sequence correspondence (Becker; Allouche–Shallit).
mechanism: f(n,d) is 10-regular (see the regular-sequence approach), so each
G_d is a Mahler function satisfying a linear Mahler-type functional equation
relating G_d(x) to G_d(x^10).  The known instance is A094798 (f(n,1)): its
g.f. g(x) satisfies g(x) = x/((1−x)(1−x^10)) + ((1−x^10)/(1−x))^2 g(x^10),
recorded in research/notes/oeis-catalogue-pe156.md.  The equation
f(n,d) = n is, coefficient-wise, the vanishing of the difference of G_d(x)
and x/(1−x)^2 = Σ_n n x^n.  Coefficient extraction on the Mahler equation
turns that vanishing condition into a functional identity analysed
10-adically layer by layer (blocks of 10^m consecutive coefficients), which
has a chance of yielding a recurrence or closed form for the solutions —
rather than a numeric search over the interval.
status: refuted
killed-by: the Mahler equation gives a coefficient/evaluation engine, not a
classification. Reading the zero set of a Mahler function off its functional
equation is intractable here (no closed form for the zero coefficients), and
the route still leans on the Prop 9.1 bound for finiteness. The adopted
block-transfer theorem is strictly stronger: it classifies the entire
solution set as translates of one seed set and gives s(d) in closed form.
```

## Why it was not adopted

The correspondence "k-regular ⟺ Mahler functional equation" is sound, sourced
theory (Becker 1994; Adamczewski–Bell–Smertnig JEMS 2023, on disk), and the
d=1 instance really is A094798's equation. But the step that mattered — turning
the functional equation into the *set of fixed points* — was the speculation,
and nothing in the Mahler-function literature gives a general way to extract a
zero-coefficient set in closed form. It would have produced at best a fourth
evaluator. The block-transfer route turned out to be a true classification
theorem (residue identity proven; bijection verified against all 661 solutions
on disk), which the Mahler route cannot match for this problem.
