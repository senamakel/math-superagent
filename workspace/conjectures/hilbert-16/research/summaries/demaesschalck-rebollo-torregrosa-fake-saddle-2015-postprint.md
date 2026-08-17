# De Maesschalck–Rebollo-Perdomo–Torregrosa, "Cyclicity of a fake saddle inside the quadratic vector fields", JDE 258(2):588–620 (2015) — postprint (held)

<!-- source: https://ddd.uab.cat/pub/artpub/2015/gsduab_3787/joudifequ_a2015v258n2p588preprint.pdf | DOI 10.1016/j.jde.2014.09.024 -->

Full text: `research/sources/demaesschalck-rebollo-torregrosa-fake-saddle-2015-postprint.full.md`.
Obtained this pass from the UAB open repository (postprint). Supersedes the
`demaesschalck-rebollo-torregrosa-fake-saddle-2014.full.md` record stub (110 bytes, "Redirecting").

## What the source establishes

**Object.** Limit cycles born near an unfolding of a **fake saddle** (alias
*impassable grain*): a degree-2 degenerate singular point with exactly two
separatrices both boundary of a hyperbolic sector, with a degenerate flow-box
normal form. The unperturbed model is `X0: {ẋ=0, ẏ=x²+y²}`.

**Normal forms.** (Lemma 1) A fake saddle with exactly two separatrices is
smoothly (linearly, when the invariant fibre is a straight line) brought to
`{ẋ = Ax²+Bxy+O(3), ẏ = x²+y²+O(3)}` with `A ≥ 0`, `B < 1`, `A² < 4(1−B)`.
(Lemma 2) The degenerate flow-box property persists under smooth perturbation.
Unfoldings: `{ẋ = ax²+bxy+µ1+µ2x+µ3y+O(3), ẏ = x²+y²−µ4+O(3)}`, 6 parameters
(`(a,b)` + `(µ1,µ2,µ3,µ4)`), with `a=A+o(1), b=B+o(1)`.

**Cyclicity results (the thread's key fact).** Small-amplitude limit cycles
near the unfolded fake saddle: cyclicity **≥ 2** when the normal form is
quadratic, with configurations **(2:0)** and **(1:1)** reachable by perturbative
mechanisms (Hopf, Bogdanov–Takens, slow-fast/canard, homoclinic/heteroclinic).
For the symmetric-restricted family (2) `{ẋ=ax²+bxy+µ, ẏ=x²+y²−1}` (µ2=µ3=0)
the paper proves **at most two limit cycles in configuration (1:1)**; limit
cycles exist only in the parameter region `R11` (whose complement `R0` never
exhibits them, proven for `R0⁺`, simulated for `R0⁻`). A precise upper bound for
the general (unrestricted) family is **not** established — the authors state an
upper bound "turned out to be too difficult", requiring a multi-parameter global
phase-portrait study beyond perturbative methods.

**Critical remark for the DRR frame.** The paper notes explicitly that the fake
saddle at `X0` has **no contribution in the degree-2 programme** of
Dumortier–Roussarie–Rousseau [13]: in that programme homogeneous vector fields
are avoided by rescalings. So the fake-saddle cyclicity result, while a genuine
bifurcation-theory result for the singularity, does **not** by itself close a DRR
graphic row.

## What it implies for this problem

- This is the primary source the `fake-saddle-transition-maps` thread rested on
  via the Marín 2026 survey (which attributes to DMRT the cyclicity ≤ 2 result)
  and via the stub. The primary text confirms: cyclicity **≥ 2** for the
  quadratic fake saddle, configurations (2:0) and (1:1); symmetric family has
  at most 2 in (1:1).
- The "no contribution to DRR degree-2 programme" caveat must temper any claim
  that closing fake-saddle cyclicity closes a DRR graphic row.
- The paper is a model for the transition-map diagram + bifurcation-mechanism
  approach in the degenerate-graphics family, and for the remark that an upper
  bound on cyclicity there is genuinely hard (multi-parameter global analysis).

## Evidence class
Every claim above is read from the held primary full text (postprint), so
**sourced-held**. None is a theorem proved by this run.
