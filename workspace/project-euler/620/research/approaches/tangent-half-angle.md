```approach
idea: Rational parametrization of the phase congruences via eccentric anomaly and tangent half-angle substitution
mechanism: The planet-centre ellipse (foci at O and S, major semiaxis a = (c+s)/(4pi), focal half-distance c_f = d/2) is parametrized by eccentric anomaly E. The triangle interior angles phi, chi, gamma at S, C, P are arccos of rational functions of cos E and sin E. Substitute t = tan(E/2): every trig expression becomes rational in t. The phase invariant W = s*phi + c*chi - t*gamma becomes a linear combination of arctan(sqrt(rational(t))). The condition tan(W) = 0 becomes, after tangent addition and clearing square roots, a polynomial equation in t, whose real roots in the admissible interval give g via Sturm sequences — no numerical scanning.
status: refuted
killed-by: superseded — the winning n_t model needs no W-invariant and no tangent half-angle; the unit-circle substitution z = e^{i beta_p} gives a degree-(c+s) polynomial directly on the actual tangency triangle, without square-root clearing or spurious roots
precedent: https://www.cecm.sfu.ca/personal/monaganm/papers/trigpoly.pdf ; https://en.wikipedia.org/wiki/Sturm%27s_theorem ; https://encyclopediaofmath.org/wiki/Sturm_theorem ; https://www-sop.inria.fr/hephaistos/logiciels/ALIAS/ALIAS-C++/node4.html ; thread `offcentre-mesh-phase-model` (claim `offcentre_dual_mesh_phase_invariant`)
first-step: (superseded — see research/approaches/arc-closure-cs-polynomial.md, which replaces the W-invariant with n_t = [(c-t)beta + (s+t)mu]/pi and the t-substitution with z = e^{i beta})
```

## Research verdict (the technique is grounded; its guarantee is upstream)

The tangent half-angle substitution is a ring morphism Q[sin,cos] -> Q(t) with
kernel <s^2+c^2-1> (Mulholland & Monagan, Lemmas 3-4, Theorem 1), and Sturm's
theorem counts real roots exactly (Wikipedia; Encyclopedia of Mathematics); the
INRIA ALIAS system implements the trig->polynomial->Sturm pipeline. So the
*technique* is standard and exact.

**Why it is now refuted anyway.** The run has since found the winning
discreteness: `n_t(d) = [(c-t)beta + (s+t)mu]/pi in Z` (reproducing 9/9/205),
with the identity `n_p + n_q = c+s`. That model does not use the W-invariant
that this candidate's polynomial would root-count, and it does not need the
eccentric-anomaly parametrisation at all: the correct algebraic object is the
unit-circle variable z = e^{i beta_p} on the actual triangle OSP, giving
`z^{c-p}(a_p z - d)^{s+p} = (-1)^k b_p^{s+p}` (degree c+s) with no square roots
and no spurious-root filtering. The t-substitution is correct machinery applied
to a superseded discreteness; it is closed in favour of
`arc-closure-cs-polynomial`, which subsumes its goal (exact non-probabilistic
root counting) more cleanly.
