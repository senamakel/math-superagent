# Koshelev & Koshka, "Combinatorial Geometry of Erdős–Szekeres Type Problems: SAT/ASP Modeling and Linear Subreduction" (2026)

> **Source:** V. Koshelev and A. Koshka, arXiv:2604.20120 (math.CO), submitted 22 Apr 2026.
> Full text: `research/sources/koshelev-koshka-SAT-ASP-esz-linear-subreduction-arxiv2604.20120-html.full.md`
> (also abstract stub `...-html.full.md`). **Preprint, not yet peer-reviewed as far as the library knows.**

## Why this source matters to this run

Not a direct ES(7) attack (that would be adjacent-drift), but the most relevant recent
**methodology** paper for the run's SAT/ASP + realizability arm, and it reproduces values
on the ES(6)=17 boundary with new encodings and gives explicit point coordinates the
run's oracle can check. Its novelty for the library: a *linear subreduction* method that
turns the realizability problem (∃ℝ-hard) into linear-integer arithmetic by fixing
abscissae, and an ASP (clingo) encoding instead of pure CNF.

## What it establishes (methodology — the durable part)

- **Linear subreduction method (§5.2):** to realize an admissible signotope, feed the
  *whole* logical formula (coloring + signotope axioms + geometric inequalities) to an
  SMT solver (Z3), fixing abscissae x_i = i or exponential spacing x_i ∈ {…,–C²,–C,–1,0,1,C,C²,…}.
  Fixing x makes the orientation determinant constraints linear in the ordinates y_i, so
  LIA (integer) solvers apply. Uses integer type (Int), justified by orientation being
  scale-invariant and the feasible region open. Caveat they state explicitly: fixing x
  can in principle lose realizations, but empirically "in almost all cases where SAT
  confirmed an abstract signotope, SMT found an integer realization with x_i = i."
- **Signotope (monotone) axioms (§4.2):** for each 4-tuple a<b<c<d, exactly one sign
  change in the sequence (L_abc, L_abd, L_acd, L_bcd), encoded as 4 forbidden
  conjunctions / 8 clauses. Same "orientation variables + transitivity/signature" model
  the run's required SAT arm must use.
- **ASP with clingo presets (frumpy/crafty):** rivals pure CNF for whole-configuration
  verification; reproduces ES-boundary values in 70–190 min without manual decomposition.
- **Reproduced/relevant exact values:**
  - Theorem 1: h(6,≥2)=17, h(6,1)=18 (hexagon with ≤2 / 1 interior point forced).
    These confirm and refine the ES(6)=17 boundary. Gives an explicit 17-point coordinate
    set (x=0..16, large integer y) with neither an empty nor a 1-interior hexagon — a
    concrete set the run's oracle can verify.
  - The corner value h_nc(4,0;4,0)=26 (bicolored sets, non-convex / empty monochromatic
    quadrilateral) and RE_C(3,3)=21 (geometric Ramsey); these are **adjacent** — bicolored /
    Ramsey variants, NOT the planar ES(7) conjecture. Do not mistake them for progress on ES(7).
  - Coordinates given for 17/18/19/20-point sets realizing various {⬡_k} hexagon-interior
    spectra (each with exact integer coordinates, checkable by the oracle).
- **Definition of the model:** points ranked by x (x_0<…<x_N–1); constants: L_abc
  (orientation vs +1), C_i(a) (colors, inverse logic), EXT_abc(z) (z outside △abc),
  TR_abc(q) (≤q points inside △abc).

## Status

`status: asserted-by-source (preprint)`. Numbers are the authors' computational claims,
not independently re-derived here. The methodology (linear subreduction, clingo ASP
signotope encoding) is the useful transfer to this run's SAT/ASP arm.

## Bearing on this run

1. The run's `sat_solver`/`smt_solver` arm can adopt the **linear subreduction** trick:
   fix abscissae, feed the full formula (not a pre-realized signotope) to Z3/clingo,
   search realizations directly. This directly supports GOAL.md's "reproduce ES(5)=9 /
   ES(6)=17 with an encoder" and the realizability requirement (explicit rational integer
   coordinates, exact determinants).
2. The signotope four-sign-change axiom (§4.2, 8 clauses per quadruple) is a compact
   alternative to SMQH's dynamic-ordering axioms already in the library — worth comparing.
3. The 17-point explicit set (x=0..16) with no empty/1-interior hexagon is a concrete
   oracle test case at the ES(6)=17 boundary.
4. **Do not** record h_nc(4,0;4,0)=26 or R_EC(3,3)=21 as ES(7) progress — they are
   bicolored/Ramsey variants (adjacent).

## claim blocks

```claim
id: kk-linear-subreduction
statement: A signotope satisfying a boolean geometric formula can be realized (given it is realizable) by feeding the full formula to an SMT solver with abscissae fixed (x_i=i or exponential), turning the orientation determinants into linear-integer constraints; empirically succeeds for almost all SAT-verified signotopes.
hypotheses: point set in general position; orientation of each triple encoded as a boolean; any realizable signotope has some realization (fixing x needs the set to admit those abscissae).
holds-here: true for the run's realizability arm, with the caveat the authors themselves state — fixing x can in principle exclude realizations, and the claim is empirical, not a theorem.
status: asserted-by-source (2026 preprint; not independently reproduced here).
bearing: gives the run's SAT/ASP + SMT arm a concrete realizability method for ES(5)/ES(6) reproduction and any ES(7) candidate realization, and an explicit integer-coordinate route.
anchor: research/sources/koshelev-koshka-SAT-ASP-esz-linear-subreduction-arxiv2604.20120-html.full.md
```

```claim
id: kk-h61-h62
statement: h(6,1)=18 and h(6,≥2)=17, i.e. every 17-point set in general position contains a convex hexagon with ≤2 interior points, and every 18-point set contains one with ≤1 interior point; an explicit 17-point set with neither an empty nor a 1-interior hexagon is given by integer coordinates.
hypotheses: points in general position; hexagon interior-point counts as defined.
holds-here: true and relevant — refines/pins the ES(6)=17 boundary; explicit coordinates are an oracle checkpoint.
status: asserted-by-source (computer-assisted, clingo ASP; preprint; not re-derived here).
bearing: a concrete 17-point configuration to feed the oracle, and an upper bound consistent with ES(6)=17.
anchor: research/sources/koshelev-koshka-SAT-ASP-esz-linear-subreduction-arxiv2604.20120-html.full.md
```

```claim
id: kk-adjacent-not-esz7
statement: The exact values h_nc(4,0;4,0)=26 and R_EC(3,3)=21 concern bicolored point sets and geometric Ramsey numbers respectively, NOT the planar Erdős–Szekeres ES(7)=33 conjecture.
hypotheses: none beyond the definitions of the bicolored/Ramsey variants.
holds-here: FALSE relevance — adjacent problems; do not cite as ES(7) progress.
status: asserted-by-source.
bearing: drift guard — keeps the run from mistaking these exact values for progress on ES(7).
anchor: research/sources/koshelev-koshka-SAT-ASP-esz-linear-subreduction-arxiv2604.20120-html.full.md
```
