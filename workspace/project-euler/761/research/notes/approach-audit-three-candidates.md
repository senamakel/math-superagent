# Approach audit — three proposed lines of attack for V_hexagon (PE 761)

Audited by the research specialist against the held library (20 primary
sources) and the web. Per candidate: what the reformulation is called, the
precise theorem/premise, whether anyone has applied it here, and what it
would buy. Statuses written into `research/approaches/*.md`.

Reference answers being checked against (all in the library, all consistent):
V_circle = 4.60333885, V_square = 5.78859314, V_hexagon = 5.05505046 =
2 + 2√21/3 ((40+8√21)/3 under the radical; minpoly of V² = 9x²−240x+256).

---

## 1. `schwarz-christoffel-conformal-mapping` — REFUTED

**What it's called / the premise.** It relies on the Riemann mapping theorem:
the regular hexagon and the unit disk are conformally equivalent via an
explicit Schwarz–Christoffel integral with factor (1−z⁶)⁻¹/³. The premise is
that the known flat-disk critical speed "pulls back" to the hexagon through
the conformal factor, giving an independent closed-form route free of the
K/α trig machinery.

**Why it fails — the run's own oracles are the counterexample.** The critical
speed is NOT a conformal invariant. The disk and the hexagon ARE conformally
equivalent (an SC map exists — so the map itself is real), yet
V_disk = 4.60333885 ≠ V_hexagon = 5.05505046. Two conformally-equivalent
domains have different critical speeds. The reason is that the game's data
are Euclidean distances (the swimmer's straight dash) and boundary ARC
LENGTHS (the runner's travel time along the perimeter). A conformal map
preserves only angles, not either of these: it does not preserve hexagon
chord lengths and it does not preserve runner arc length. Any conformal
diagram sends the Euclidean game to one in a non-Euclidean Riemannian metric
whose solution is a NEW problem, not the known flat-disk one. There is no
transfer.

**Has anyone applied it?** No — and this is an absence, not the argument. A
web + research-paper + all-held-sources search for conformal/Schwarz-Christoffel
treatment of escape or critical-speed games returns nothing; the two oracle
values themselves falsify the premise regardless of prior attempts. No claim
in the library supports it; claim `circle-critical-speed-identity-e375` and
`oeis-a328227-circle-critical-speed` fix V_circle for the disk only, exactly
analogous to how `stewbasic-regular-ngon-cutoff` fixes V_hexagon for the
polygon without any conformal bridge.

**What it would have bought:** an independent closed-form route — but the
premise is false, so nothing.

---

## 2. `david-k-hexagon-construction` — GROUNDED (as a method), with the
   execution gap explicitly open

**What it's called.** David K's synthetic equal-time geometric construction
(the square case is in the held library, q.1762665). It identifies the
critical exit geometry, writes the equal-time condition
swimmer_chord = runner_perimeter / v (τ = 0 when d2 = v·d1), and solves for v
exactly. For the square: V_square = √(5/2(7+√41)) = 5.78859314, a genuinely
distinct route from stewbasic's general-n formula (claim
`davidk-square-closed-form`).

**Precise claims and whether they hold.**
- The *method* is real and sourced (David K's square; also the harmonic
  parallel in Abel et al. "Escaping a Polygon", arXiv:2007.08965, and in the
  stage-opposite-then-dash mechanism, claims `escaping-polygon-wellposed-exact-square-disk`,
  `lady-in-the-lake-differential-game-equilibrium`, `tao-square-pool-6x-capture`).
- The *target* is an exact quadratic surd: V_hexagon = 2 + 2√21/3 =
  (40+8√21)/3, V² minpoly 9x²−240x+256 (the run's own exact algebra,
  `code/hexagon_closed_form.py`, `code/v2_quadratic_test.py`). Confirmed.
- The *claim "the equation must be quadratic in v²"* is true for n=6 but NOT
  a general principle: the run itself established V(n)² is quadratic only for
  n=3,4,6; n=5 and n≥7 have minimal polynomial degree > 2. So the quadratic
  closure is a hexagon fact, not a reason in itself.
- **Execution gap:** the hexagonal specialization is the run's PLANNED but
  UNEXECUTED independent route. `research/notes/hexagon-first-principles.md`
  does not exist on disk; `code/hexagon_first_principles_explore.py` exists but
  was never run (no captured output). Abel et al. explicitly leave n>4 OPEN
  (claim `abel-open-ngon-ngt4`), so no held primary source already has the
  hexagon construction. Until its output is captured and agrees with
  5.05505046, the hexagon value stays single-route (formula-derived +
  exact-closed-form-confirmed), exactly per CONTEXT.md.

**Has anyone applied it to the hexagon?** Not in the held literature (Abel
et al. stop at the square). It would be this run's own independent derivation
— the missing second route. Status: grounded as a method, with the
verification gap explicitly open, not closed.

---

## 3. `angular-speed-safe-region` — REFUTED

**What it's called.** A differential-game construction of the safe region from
the angular-speed-matching constraint (swimmer can keep centrally opposite
the runner only at radius r ≤ ρ(φ)/v), claimed to be a star-shaped
piecewise-defined region rather than the stewbasic 1/v homothetic scaled copy.
The stated purpose is to independently confirm-or-falsify the stewbasic
ansatz; the circle (ρ(φ)≡1 → disk of radius 1/v → V=4.60333885) is the
built-in gate.

**Why it fails as an independent test — it is a restatement, and any genuine
alternative is a lower bound.**
- For a REGULAR polygon, the angular-speed-matching boundary {r ≤ ρ(φ)/v} IS
  the 1/v homothetic scaled copy of the pool — the very same safe region
  stewbasic's model uses. Constructing it from the angular-speed constraint
  reproduces the same region and the same V; it is not an independent model,
  so it cannot confirm-or-falsify.
- Any genuinely DIFFERENT safe region (inner circle, diamond, octagon,
  square) is a strict LOWER BOUND on V — documented in the held math.SE thread
  (TMM/Jens: inner square 5.00, diamond 5.25, circle 5.27, octagon 5.38, vs
  the optimal homothetic scaled-pool 5.7886 for the square). A safe-region
  route can land at-or-below the true value but can never exceed it, so it
  can never falsify the stewbasic value upward; it can only ever confirm a
  (possibly strict) lower bound. The run's own `code/indep_game_encoding.py`,
  exactly this "max over dash-landing-point from a staged region" form,
  produced 3.98 for the hexagon — the same lower-bound trap.
- **What is real in the idea:** the angular-matching staging principle is
  genuine and sourced for the CIRCLE — the Lady in the Lake auxiliary
  differential game stages at antipodal radius r=1/v where angular speeds
  match (claim `lady-in-the-lake-differential-game-equilibrium`; also
  Hesterberg, Ponder This). But on polygons it degenerates into the escaper's
  lower-bound construction. The circle validation gate is real; it just does
  not rescue the polygon case into an independent test.

**What it would have bought:** an independent physical confirm/falsify of the
stewbasic ansatz — but it is a restatement (homothetic coincidence) or a
strict lower bound, so it cannot deliver.

---

## Bottom line

- Two of the three candidates are refuted on structural grounds, not on
  absence of literature:
  - Schwarz–Christoffel: the critical speed is not conformally invariant —
    the run's own disk-vs-hexagon oracle values are a direct counterexample.
  - Angular-speed safe region: for a regular polygon the region coincides with
    the homothetic scaled pool (restatement), and every other safe region is a
    strict lower bound that cannot falsify upward.
- David-K hexagon construction is grounded as a method and its exact target is
  verified, but the hexagon specialization is unexecuted — it is the run's
  planned independent route and the verification gap remains open.

Files written: `research/approaches/schwarz-christoffel-conformal-mapping.md`
(status refuted, killed-by), `research/approaches/angular-speed-safe-region.md`
(status refuted, killed-by), `research/approaches/david-k-hexagon-construction.md`
(status grounded with the execution gap stated).
