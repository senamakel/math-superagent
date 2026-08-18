# Decision note — inventor converging round (candidates chen / bautin-flatness / holonomy)

Date: this cycle. Memory server down; decision persisted here per workspace
fallback (CONTEXT.md).

## Outcome

- **Adopted:** `reduced-bautin-depth-chen-coefficient-engine`
  (`research/approaches/reduced-bautin-depth-chen-coefficient-engine.md`).
- **Narrowed (surviving restriction absorbed into the synthesis):**
  `bautin-scheme-flatness-discriminant` → García's reduced Bautin depth;
  `chen-iterated-integrals-shuffle-displacement` → Chen/Fliess coefficient engine.
- **Refuted:** `holonomy-differential-galois-jet-determinacy` — the literature
  gives differential-Galois *integrability obstructions* (Ochoa et al. 2018,
  doi:10.1016/j.jde.2018.02.016), not the claimed bridge from bounded variational
  Galois complexity to finite jet determinacy or a nonlinear displacement zero
  bound.

## The new line (why it is new to this run)

García, "The cyclicity of polynomial centers via the reduced Bautin depth",
Proc. AMS 143 (2015) (doi:10.1090/proc/12896); companion 2016
(doi:10.1090/proc/13570): for a monodromic singularity with an analytic Poincaré
first-return map whose Bautin ideal is polynomial in the parameters, the
ascending chain J_k = ⟨v_1,…,v_k⟩ of coefficient ideals stabilizes, and the index
κ at which the INTEGRAL CLOSURES of the J_k stabilize satisfies Cyc ≤ κ−1. Works
for non-radical Bautin ideals; reported minimum bound; class includes
nondegenerate centers, generic nilpotent centers, some degenerate centers.

The polynomial-Bautin-ideal hypothesis is exactly the boundary where the open DRR
center graphics (I¹₆b, H³₁₃, DI₂b — triple nilpotent points at infinity
surrounding a center) sit: their displacement is a composition of second-type
Dulac maps with transseries coefficients. The Chen/Fliess iterated-integral
expansion (Costin 2009 doi:10.1155/2009/590856; Brudnyi arXiv:1602.08655) is a
grounded coefficient engine that computes those coefficients exactly. The attack
line: run reduced-Bautin-depth integral-closure stabilization on the exact
coefficient chain and locate the first generator where the polynomial chain fails
to contain a genuine Dulac coefficient. Stabilize in an enlarged finite-type ring
→ new finite-cyclicity theorem; provably fail at generator k → that generator is
the named obstruction to adjoin.

## First step (tool_builder-ready)

(a) Validate: quadratic focus family (run already computes L4,L6,L8 over ℚ):
J₁=⟨L4⟩, J₂=⟨L4,L6⟩, J₃=⟨L4,L6,L8⟩; compute integral closures over ℚ; expect
κ=4 → Cyc ≤ 3 = M(2), matching Bautin 1952.
(b) Nilpotent center family (Andreev normal form ẋ=y+…, ẏ=x²+…): compute chain,
reduced Bautin depth, match published bound.
(c) Lean: `Cited.reduced_bautin_depth_bound` axiom with `/-- src: García, Proc.
AMS 143 (2015) -/`; discharge the stabilization certificate by `decide`/`norm_num`
over ℚ.

## Three tests

1. Smooth test: integral-closure stabilization decides the germ only via
   analyticity of the return map — false for C^∞ (Dulac's error).
2. Uniformity: local setting has it via polynomiality of the Bautin ideal; open
   graphics do NOT — first step stays local and names the gap.
3. Counterexample hunt: hunt the degenerate-center first non-polynomial generator
   as hard as stabilization; a provable failure is a result (located obstruction).
