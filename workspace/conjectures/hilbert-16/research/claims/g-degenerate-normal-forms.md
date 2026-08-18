# G-degenerate-normal-forms — DR 2009 Props 2.1–2.3, conditional in Lean

```claim
id: g-degenerate-normal-forms
statement: For the three DR 2009 normal-form families, the quadratic family near the degenerate graphic reduces, by an affine change of coordinates and time scaling depending analytically on the parameters, to the 5-parameter unfoldings (2.2) [finite-plane line: ẋ = y+bxy−y²+µ1+µ2x+µ3x², ẏ = xy+µ4, b∈(−2,2)], (2.8) [line at infinity: ẋ = cx−y+1+(1+µ2)x²+µ1xy+µ0y², ẏ = xy−µ3x², c∈(−2,2)], (2.14) [two lines, 7 parameters: ẋ = xy(1+µ4)+µ0+µ1x+µ2x²+µ3y², ẏ = −y+y²−µ6x²+(µ2−µ5)xy], fixing the invariant line/equator, the contact point, and the compact parameter box on which the displacement is studied. Proved in DR 2009 Props 2.1–2.3 (held full text). The three families cover all 13 degenerate DRR graphics: Prop 2.1 covers DF1a, DF1b, DF2a, DF2b, DH1, DH2; Prop 2.2 covers DI1a, DI1b, DI2a, DI2b, DH3, DH4; Prop 2.3 covers DH5.
hypotheses: (DR 2009 Prop 2.1) a quadratic system with a line of singular points in the finite plane, all but one normally hyperbolic, and a focus (strong or weak) or center — normal form (2.2) with b0 ∈ (−2,2), b = b0 + µ0; (Prop 2.2) a line of singular points at infinity, a finite invariant line, focus/center — normal form (2.8) with c0 ∈ (−2,2), c = c0 + µ4; (Prop 2.3) two lines of singular points (graphic DH5) — the full quadratic unfolding needs 7 parameters, normal form (2.14). Affine changes (2.4), (2.10) reduce to the identity on the unperturbed system; scalings in (X,Y,t) absorb the remaining coefficients.
holds-here: yes
status: conditional
formalisation: code/lean/h16_2_degenerate_graphics_finite_cyclicity_G_degenerate_normal_forms-71af02d5.lean
axioms: Cited.DR2009_props_2_1_2_3 (the packaged proposition: existence of the analytic affine/time normalisation with the invariant line/equator, contact point, compact box data)
falsifier: A primary source showing one of the three displayed families is not reachable by an analytic affine coordinate change and time scaling from the stated stratum hypotheses; or a corrected normal form replacing (2.2), (2.8), or (2.14) in DR 2009.
sources: https://doi.org/10.3934/cpaa.2009.8.1133 (Dumortier–Rousseau 2009, CPAA 8:1133–1157)
anchors: research/sources/dumortier-rousseau-2009-degenerate-graphics-cpaa.full.md lines 162-180 (Prop 2.1, normal form (2.2), parameter count (µ0..µ4)); lines 197-244 (Prop 2.2, normal form (2.8)); lines 247-264 (Prop 2.3, normal form (2.14), 7 parameters)
```

## What the Lean file carries

- The three displayed families are stated as explicit `def`s over `ℝ × ℝ → ℝ × ℝ`
  (`finitePlane`, `lineAtInfinity`, `twoLines`), so the polynomial content of the
  node — every monomial and parameter of (2.2), (2.8), (2.14) — is in the file and
  kernel-checked for well-typedness.
- **Eight transcription facts are `verified` (kernel-closed, no axioms)**:
  at µ = 0 each family restricts to the source's unperturbed system (2.1)/(2.7)/
  (2.13); the x-axis is a line of singular points for (2.1) and (2.13) and an
  invariant line for (2.7); and the focus/center of (2.1) and (2.7) sits at
  (0,1) — each closed by `simp`/`norm_num`. These verify the "unperturbed
  system / invariant line / contact point" content of the node against the
  displayed systems in the held text, independent of the cited proposition.
- The node's proposition (existence of the analytic affine/time reduction with
  the fixing data) is packaged as the cited axiom
  `Cited.DR2009_props_2_1_2_3` under `namespace Cited`, with the source in the
  docstring, exactly as the workspace records results that are a paper's to
  prove.
- The theorem `h16_2_degenerate_graphics_finite_cyclicity_G_degenerate_normal_forms`
  is the kernel-checked implication from the cited proposition to the node
  statement. `#print axioms` names only `Cited.DR2009_props_2_1_2_3` (plus the
  source's own holding axiom); there is no `sorry` and no `native_decide`.
- Standing is **conditional**, never `formalised`: the kernel checked the step
  from DR 2009 to the node, and nothing about DR 2009 itself.

## Why the parameter binders are the source's

- In (2.2), `µ0` never appears in the displayed monomials because it enters as
  `b = b0 + µ0` (DR 2009: "where b = b0 + µ0 is a variable parameter inside
  (−2,2)"). The Lean `finitePlane` takes `b` as the combined parameter; the
  linter's unused-`µ0` warning is faithful to the source, not a transcription
  error.
- In (2.8), `µ4` likewise enters as `c = c0 + µ4`; the same remark applies.
- In (2.14), all seven parameters `µ0..µ6` appear in the displayed monomials.
