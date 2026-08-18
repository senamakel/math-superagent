# reversibility-quotient-ect

```approach
name: reversibility-quotient-ect
idea: Use a time-reversing involution in reversible center graphics to quotient the configuration and test whether second-type Dulac passages reduce to first-type maps, after which an ECT/Chebyshev zero theorem could control the displacement.
status: refuted
killed-by: Reversibility does not establish the required analytic equivalence between the four second-type Dulac passages and first-type maps for the full I¹₆b or DI₂b graphics, nor does it imply that the quotient displacement is an Abelian-integral ECT family. Leading-term agreement would be only diagnostic, not a proof of conjugacy or the GMV hypotheses.
precedent: https://doi.org/10.1090/mosc/248 (Roussarie–Rousseau, finite cyclicity of center graphics); https://doi.org/10.48550/arxiv.1502.00689 (Rousseau–Shan–Zhu, nilpotent saddle graphics); https://doi.org/10.48550/arxiv.0805.1140 (Grau–Manosas–Villadelprat, Chebyshev criterion for Abelian integrals); https://doi.org/10.3934/dcds.2009.25.511 (Gautier–Gavrilov–Iliev, genus-one quadratic centers); claim:gmv-ect-does-not-cover-i6b-four-dulac; claim:i6b-four-second-type-dulac-hypotheses-not-established; claim:i6b-four-second-type-full-graphic-not-covered
killed-by: Reversibility simplifies center-case transitions and can make selected maps identities after section choices, but the literature does not establish that the four second-type Dulac maps for the full I^1_6b or DI_2b graphics descend to first-type passages, nor that the quotient displacement is an Abelian-integral ECT family. The required reduction is the central unproved assertion, so the proposed route cannot be grounded as stated.
```

## Literature assessment

The relevant theories are **reversible planar systems**, **Dulac-map normal forms**, and **extended complete Chebyshev (ECT) systems for Abelian integrals**. An ECT system is a finite ordered family whose initial Wronskians do not vanish (equivalently, every nonzero linear combination has the prescribed bounded number of zeros, counted with multiplicity, on the interval). GMV's criterion applies to explicitly specified Abelian-integral families over Hamiltonian/reversible period annuli, under their Wronskian and separated-oval hypotheses. It does not apply merely because the original vector field is reversible.

Roussarie–Rousseau 2015 does use reversibility in center graphics and obtains simplifications for selected transitions, while its full results for I^1_6b and DI_2b concern boundary limit-periodic sets, not the proposed quotient theorem for the complete four-second-type displacement. Rousseau–Shan–Zhu explicitly distinguish the two Dulac-map types and, in the relevant cited treatment, provide the needed first-type formulas; the required uniform second-type reduction is not supplied. ECT results for reversible quadratic centers and genus-one period annuli are genuine applications, but they concern Abelian/Melnikov integrals, not the full non-Hamiltonian polycycle holonomy.

Therefore the first finite computation is useful diagnostically, but a failure or success of leading-term matching cannot establish the claimed analytic conjugacy or ECT representation. The route could buy a restricted theorem if one first proves a section-by-section quotient identity and an Abelian-integral representation; absent that, it is refuted as a proposed closure of the open graphics.

Tests: smooth test would be satisfied only by a proved analytic Dulac/Abelian reduction; symmetry alone is insufficient. Lower-bound test is not relevant to a restricted upper bound but applies to any global claim. Slow-fast test is a warning that parameter-dependent second-type passages need not remain in a fixed ECT family under degeneration.

This verdict is evidence-based rather than a claim that no reversible quotient can ever work: the exact reduction was not found in the cited primary literature, and held claims explicitly record the missing hypotheses.
