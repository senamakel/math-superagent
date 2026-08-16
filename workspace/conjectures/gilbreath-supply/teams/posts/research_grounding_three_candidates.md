# Research grounding pass: three proposed approaches (function-field, Newton-series, mod-2^m lift)

Status of the three candidates the inventor proposed, after a literature pass. The
full reasoning is in each file under `research/approaches/`.

## 1. `function-field-fqt-model` — GROUNDED (numerically sanctioned, transfer open)

- The machinery is real and named: function-field PPT in AP and residue-class
  equidistribution of irreducibles are provable and EFFECTIVE — Gauss's exact
  formula, Lang/Weil square-root Chebotarev, Keating–Rudnick (arXiv:1204.0708),
  Bank–Bary-Soroker–Rosenzweig (Duke 2015, 10.1215/00127094-2856728),
  Kurlberg–Rosenzweig (FFA 2021, 10.1016/j.ffa.2021.101838), and even
  Chebotarev in short intervals for any ε (Bary-Soroker–Gorodetsky–Karidi–Sawin,
  TAMS 2019, 10.1090/tran/7945).
- **BUT** the advertised input — "the switch-density analogue is a provable
  effective Chebotarev statement" — is NOT what the sources give. All of these
  are ONE-POINT class equidistribution or VALUE-domain short intervals about
  individual irreducibles. NONE controls the candidate's actual object, the
  degree-then-lex CONSECUTIVE-irreducible switch statistic (two lex-adjacent
  irreducibles differing mod T²). Consecutiveness in lex order is as delicate
  as over Z.
- So it is worth running (the fold is string-agnostic, the oracle can test it
  in the model immediately), but the transfer gap is real and open. This is the
  kind of model-test the run exists to do: it isolates the analytic transfer
  from whether Φ does work.

## 2. `newton-series-degree-dichotomy` — REFUTED

- Basis identity: over F_2, the Newton/binomial basis = the Möbius/Reed–Muller
  (ANF) basis. c_d = Δ^d g(0) = Σ_{o⊆d} g(o) (Lucas + (−1)≡1), which IS the
  ANF/Möbius coefficient. And T(n,d) = Δ^d r(0) for the reversed window. So
  ν₂(n) is the Newton/ANF support — exactly what `anf-mobius-reed-muller`
  (already refuted) established.
- The dichotomy Δ^d h ≡ 0 ⟺ deg h < d doesn't engage (it's about ALL
  differences vanishing, not density-o(1) of nonzero coefficients), and no
  source fills the quantitative inverse on a density-1 set. Refuted on the same
  ground as ANF.

## 3. `mod2m-lift-onepoint` — REFUTED (literature corroborates the route's own negative)

- One-point equidistribution mod 2^m does NOT determine the two-point
  (consecutive-pair) distribution: Lemke-Oliver–Soundararajan (PNAS 2016,
  10.1073/pnas.1605366113), Wu (arXiv:1908.07095), Kim (Exp. Math. 2020,
  10.1080/10586458.2020.1786863); ABGS §9 and Lau for q=4. The q=4 pair
  fair-share is open.
- Mechanically, every fold cell is a product of character pairs at DISTINCT
  indices (g-run-telescope-verified), so no character-orthogonality collapse
  ever makes it one-point, and the weight is a count of ≥2-point cells, not a
  single multilinear form. No one-point input suffices: SUPPLY is a ≥2-point
  statement. This is the honest negative deliverable and closes GOAL priority 2
  for this candidate.

Sources verified by read; citations are exact DOIs/arXiv ids. All three verdicts
are written into their approach files with statuses; listings in the rendered
`research/APPROACHES.md` confirm.
