```approach
id: integral-brauer-manin-nine-square
idea: Apply Colliot-Thélène–Xu integral Brauer-Manin obstruction to the full
  nine-square affine variety V/Z, not the six-square K3 of Bremner II.
  Every previous approach works at the level of rational points (K3,
  elliptic curves, Φ); the integral BM obstruction is a refinement that
  uses denominators — precisely what separates Q from extension fields
  where MSS exist.  An integral point surviving a Brauer class over Q can
  fail over Z because the denominator structure differs from Q(√3,√133).
status: refuted
killed-by: The integral BM technique is real, but the nine-square affine
  scheme V/Z (7 line-sums + 8 norm equations; singular, non-proper — the
  magic variety X⊂P⁸ is already a surface with 256 singular points) lies
  outside every class where the integral BM group is computable:
  smooth homogeneous spaces (CT-Xu, Compos. Math. 145 (2009) 309–363),
  normic hypersurfaces N_{K/k}(z)=P(t) (Browning–Matthiesen, Ann. ENS 50
  (2017)), and norm-one torus torsors (Harpaz). No source computes
  Br(V)/Br(Q) or an integral BM obstruction for the MSS variety. The
  separating premise — an integral point over Z[√3,√133] but not over Z —
  is itself the whole content and is unproved; the candidate offers no
  Brauer class to evaluate.
precedent:
  - "Colliot-Thélène–Xu, Brauer–Manin obstruction for integral points of
    homogeneous spaces and representation by integral quadratic forms,
    Compos. Math. 145 (2009) 309–363"
    url: https://www.cambridge.org/core/journals/compositio-mathematica
  - "Browning–Matthiesen, Norm forms for arbitrary number fields as
    products of linear polynomials, Ann. Sci. ENS 50 (2017),
    https://numdam.org/articles/10.24033/asens.2348/"
  - "Harpaz, unramified Brauer group of norm-one tori"
  - "Claim: integral-bm-nine-square-not-applicable (research/notes/
    literature-check-3-new-approaches.md)"
first-step: NONE — the hypotheses for a computable integral BM group fail for
  V (singular, non-proper, outside homogeneous/normic/torus classes) and
  the separating premise is unproved. Re-proposing requires first finding
  a smooth projective model of the MSS variety with a computable Br,
  which no source provides.
speculation: (as originally written) computing Br(V)/Br(Q) for an affine
  variety of 8 norm equations has never been done. Confirmed: it has
  never been done, and the structural reasons above are why.
```
