# Lean status — Statement.lean, BautinRecurrence.lean, Bautin.lean (verified state)

Verification note for the Lean deliverables, reflecting the host-fixed state
(2026). **Do not revert these files; build on them.**

## Files and their verified status

- **`code/lean/Lib/Statement.lean`** — H16.2 stated with a real degree bound
  (`f.P.totalDegree ≤ n`, `f.Q.totalDegree ≤ n` via `PlanarPolyField` carrying
  two `MvPolynomial (Fin 2) ℝ`) and the non-vacuous finiteness statement
  `(LimitCycleSet f.toMap).Finite ∧ (LimitCycleSet f.toMap).ncard ≤ N`.
  The lone `:= by sorry` at `h16_2` is the deliberate deliverable; the axiom
  set is exactly `sorryAx` (plus the kernel's own `propext`, `Classical`,
  `Quot.sound`). Compiles.

- **`code/lean/Lib/BautinRecurrence.lean`** — **VERIFIED** (no `sorry`, no
  cited axiom). Closed theorems: `h14_p30_check`, `p30_sound`,
  `bautin_L6_identity`, `L4num_ne_zero`, `param_identities`,
  `darboux_L_identity`, `darboux_F_identity`. The P30 coefficient data is
  **inline in a `namespace Generated`** carrying no theorem; the
  kernel-checked path is `p30_sound : (∀ k : Fin 30, Generated.coeffs k +
  W6coeffs k = 0) → P30poly + W6poly = 0`, an explicit bridge from the
  coefficientwise check to the polynomial identity.

- **`code/lean/Lib/Generated/P30Data.lean`** — provenance copy of the P30 data
  (`ms : Fin 30 → Fin 5 → Nat`, `coeffs : Fin 30 → ℤ`), no theorems, kept in
  step by `code/bautin/generate_p30.py`. It is NOT imported by the checker:
  the kernel runs on ONE file against Mathlib with no lake root, so a second
  module (`LuH14.Generated` or `Lib.Generated.P30Data`) fails with unknown
  module prefix. Do not re-introduce a second import.

- **`code/lean/Lib/Bautin.lean`** — **CONDITIONAL** (no `sorry`; rests only on
  `Cited` axioms for Bautin 1952). Holds `focalValue : ℕ → LyapunovRing`,
  `focalValue_eq`, and `bautin_finite_generation` as `axiom`s under
  `namespace Cited` (/-- src: Bautin 1952 -/). The old `V1=V2=V3=0` body is
  GONE: the three focal values are computed exactly by
  `code/bautin/lyapunov_quadratic.py`, capture `code/out/bautin_focal_values.captured.txt`
  — V1 as a machine-emitted term, V2 and V3 as data tables (a 220-term chain
  will not elaborate even at 2,000,000 heartbeats).

## The four engineering facts that shape any further Lean work

1. **One file per kernel run.** No second-module import; keep data inline in a
   `Generated` namespace or in the same file.
2. **`decide` over an `MvPolynomial` equality does not reduce** — it is a
   `Finsupp` equality. The check is coefficientwise over `Fin 30`, and
   `p30_sound` proves the bridge to the polynomial identity. Do not put
   `decide` back on a polynomial equality.
3. **`MvPolynomial` is not a division ring**, so dividing by 8 does not
   elaborate; the degree-4 obstruction is `L4num` with the factor in its name.
4. **The quadratic family has six coefficients and no cubic terms** — the old
   normal form carried `a30,a21,b12,b03`, which a degree-2 field has not.

## What the captures establish (exact, over Q)

`code/out/bautin_focal_values.captured.txt` (lyapunov_quadratic.py):
- Full-family focal values L4 (6 monomials), L6 (56), L8 (220) for the
  general quadratic focus with six coefficients.
- **L8 ∉ ⟨L4, L6⟩ by exact Gröbner over Q** — so three generators are
  genuinely needed for Bautin finite generation; two would not suffice.
  CHECK: PASS.

`code/out/membership.captured.txt` (verify_membership.py, chart family
Q1 = Au²+Cuv+Dv², Q2 = Euv+Fv², lex Gröbner, degrees 4..12):
- Sanity guards: `8·L4 − (AC+CD+2DF−EF) = 0` PASS; `192·L6 + P30 = 0`
  (P30 30-monomial) PASS.
- Monomial counts L_d: 4, 30, 97, 236, 485 for d = 4,6,8,10,12.
- **Membership: L8 ∉ ⟨L4,L6⟩; L6 ∉ ⟨L4⟩; L10 ∉ ⟨L4,L6,L8⟩; L12 ∉
  ⟨L4,L6,L8⟩** — all False by exact Gröbner reduction. The Bautin-trick step
  ("L10,L12 ∈ ⟨L4,L6,L8⟩", the ideal closure that would make three generators
  finite-generation-complete) **fails in the 5-coefficient chart ring**.
  The earlier `lyap_extend.py` crash (poly_terms TypeError) is superseded by
  this completed run.

## Honest scope

- `BautinRecurrence.lean` VERIFIED means the transcription identities and the
  bridge from coefficientwise data to the polynomial identity are
  kernel-checked. It does NOT prove the H₁₄³ theorem — the human-proof
  remainder (root uniqueness, Hadamard divisibility, domain completeness, zero
  theorems) is machine-unchecked and Lu 2026 is unrefereed.
- `Bautin.lean` CONDITIONAL means: the kernel checked the step from Bautin
  1952's cited theorem to what the run builds on it; the cited theorem itself
  is the run's word, not its proof.
- **Open Lean task**: the membership results are now exact-computational facts
  (L8 ∉ ⟨L4,L6⟩ with a 9-monomial nonzero remainder; L10, L12 ∉ ⟨L4,L6,L8⟩
  with 38- and 110-monomial remainders). Turning "L8 needs a third generator"
  into a kernel-checked theorem needs a cofactor certificate (explicit
  remainder representation), and the non-membership of L10,L12 bears on
  whether Bautin finite generation for this chart needs MORE generators than
  the three focal values — worth stating before any Bautin-ideal Lean claim
  goes further (see research/notes/claims.md).