# Approach: symmetric multi-affine polarization and the Walsh coincidence theorem

```approach
idea: Change representation from "polynomial and its derivatives" to the symmetric
       multi-affine polarization Φ(z_1,…,z_n) of f (the unique symmetric multi-affine
       polynomial with Φ(z,…,z) = f(z)). The derivative conditions f^{(i)}(r_i) = 0
       translate into partial-derivative conditions on Φ, and the conclusion
       f = (x−a)^n translates into "all n variables coincide". The named tool is the
       Walsh coincidence theorem (Rahman–Schmeisser, *Analytic Theory of Polynomials*,
       the refinement of Grace–Walsh–Szegő): a symmetric multi-affine polynomial whose
       partial derivatives vanish in a compatible way at points of one circular region
       is forced to be a monomial in a single linear factor — precisely a
       coincidence-forcing result, which is what CA's conclusion *is*.
mechanism: CA is a coincidence statement, and the analytic theory of polynomials has
       exactly one classical family of coincidence theorems — Grace–Walsh–Szegő and
       Walsh's coincidence theorem — whose hypotheses (symmetric, multi-affine, roots
       in a circular region) the polarization of f satisfies by construction. The
       derivative tower f^{(i)} is recovered from Φ by specializing (n−i) variables to
       the same point and differentiating, so each gcd(f, f^{(i)}) ≠ 1 condition is a
       partial-derivative vanishing of Φ. The char-0 content is structural: a circular
       region is a notion of order/absolute value that has no analogue in char p, so
       the argument is char-0-only for the right reason, and its char-p break is that
       the region hypothesis is vacuous/meaningless there. This is the "known theorem
       whose hypotheses the problem happens to satisfy" shape: the polarization is the
       bijection, Walsh's coincidence theorem is the engine. The likely honest output
       is a new restricted class — CA for polynomials whose roots (or shared roots r_i)
       lie in one circular region — generalising the real-rooted (Polstra) result.
first-step: Source the exact statement and hypotheses of Walsh's coincidence theorem
       (Rahman–Schmeisser §15/§16), then for the polarization Φ of a monic f write the
       conditions f^{(i)}(r_i)=0 as partial derivatives of Φ at multi-points, and check
       whether the theorem applies directly or needs the r_i confined to a disk/half-
       plane; verify on (x−1)^n and on small counterexample candidates through the
       oracle. Precise theorem statement must be sourced, not recalled.
charp-break: the circular-region hypothesis uses an ordering/absolute value absent in
       char p; the same argument cannot be restated there, so it cannot prove the false
       char-p statement. The falsifier to hunt: a char-0 CA candidate whose r_i escape
       every circular region, showing the hypothesis cannot be forced.
status: refuted
killed-by: (1) The circular-region hypothesis cannot be forced: the proposal's
       own falsifier (a candidate whose shared roots r_i escape every circular
       region) is the generic situation, so the restricted class is near-vacuous
       and cannot reach a general counterexample. (2) The run already holds a
       stronger, sourced, char-honest root-geometry constraint — Polstra's
       convex-hull reformulation (every root a vertex of the hull iff pure
       power) — which dominates Walsh's coincidence conclusion. (3) It abandons
       the agreed Z-scheme/resultant method for an analytic argument whose
       char-p break is only "the hypothesis is meaningless in char p", so it
       probes none of the char-p witnesses and fails the purpose of the
       admissibility test.
```
