# Claim — Figueras–Tucker–Villadelprat 2013, computer-assisted Chebyshev verification

```claim
id: h16-ftv2013-chebyshev-abelian-ca
statement: (Theorem A) Let Jbar_i(h) = ∫_{γh} y^{2i-1} dx where γh ⊂ {A(x) + B(x)y^2 = h} with A(x) = 1/2 − e^{−2x}(x + 1/2), B(x) = e^{−2x}. Then (Jbar_0, Jbar_1, Jbar_2) is an ECT-system (extended complete Chebyshev system) on [0, 1/2). This proves the Dumortier–Roussarie conjecture [Birth of canard cycles, DCDS 2 (2009) 723–781] for n = 0, 1, 2 (q ≤ 2), giving explicit cyclicity bounds at slow-fast Hopf points of codimension 1–2 (via [7, Thms 1.5, 1.8]). Method: Theorem 1.1 (Grau–Mañosas–Villadelprat Chebyshev criterion) applied to the non-polynomial (transcendental) family; σ-balance functions ℓ_i; Wronskian nonvanishing proved by interval-arithmetic (CAP) computations plus analytic arguments (Lemma 4.7–4.9, Fujiwara root bound).
hypotheses: A, B analytic with A(x) = 1/2 − e^{−2x}(x + 1/2), B(x) = e^{−2x} (non-algebraic case); ovals γh of H = A(x) + B(x)y^2, h ∈ [0, 1/2); ECT = Wronskian leading principal minors never vanish (Lemma 3.3).
holds-here: yes — this is the instrument-level result the run's sharp-Abelian approach (`abelian-picard-fuchs-argument-principle-sharp-count`, `reduced-bautin-depth-…`) relies on: it certifies ECT/Chebyshev zero bounds for Abelian integrals by interval arithmetic when the integrand is not algebraic. It does not by itself close any DRR graphic.
status: proved
evidence-class: proved (peer-reviewed JDE 254 (2013) 2647–3663; postprint held; computer-assisted proof with CAP interval arithmetic)
falsifier: A counterexample to the ECT property on [0,1/2), or a failed independent interval-arithmetic re-check of the Wronskian nonvanishing (Lemma 4.9).
answers: none
follows-from: gmv2008-ect-criterion
contradicts: none
anchors: research/sources/figueras-tucker-villadelprat-chebyshev-abelian-2013-postprint.full.md
url: https://ddd.uab.cat/record/150616 (postprint https://ddd.uab.cat/pub/artpub/2013/gsduab_3450/FigTucVil2012.pdf); DOI 10.1016/j.jde.2013.01.036
```

## Notes

- The criterion (their Theorem 1.1, from Grau–Mañosas–Villadelprat [13]) reduces
  ECT verification to a Wronskian of the σ-balanced functions `ℓ_i = B_σ(f_i/(A'B^{(2s-1)/(2m)}))`;
  in the polynomial case this becomes a resultant/Sturm check, in the non-polynomial
  case (this paper) an interval-arithmetic check.
- Relevance to this run: this is the certified-verification instrument named in
  `research/approaches/slow-divergence-integral-ect.md` ("Figueras–Tucker–Villadelprat
  2013 reduces the Wronskian nonvanishing ...") — now the primary full text is held.
- It is a canard/slow-fast result (Dumortier–Roussarie birth-of-canard-cycles
  conjecture), i.e., exactly the slow–fast test regime of problem.md.
