# Formalisation checkpoint — second independent route to L8 ∉ ⟨L4, L6⟩

(Authored by the formalisation specialist. Memory server down this cycle, so
these findings are persisted here instead, per CONTEXT.md.)

## Re-verification of the three host-fixed Lib files (verdicts filed)

`lean_check` re-run and JSON captures refreshed in `code/out/lean/*.json`
(fresh source digests, timestamps 2026-08-17 22:31–22:32):

| file | compiled | outcome | sorries | axioms |
| --- | --- | --- | --- | --- |
| `Lib/Bautin.lean` | true | **conditional** | none | `V3_not_mem_span_V1_V2` → `[propext, Classical.choice, Quot.sound]`; `bautin_ideal_eq_span_three`, `M_two_eq_three` rest on `Cited.*` |
| `Lib/BautinRecurrence.lean` | true | **verified** | none | cited axioms: none |
| `Lib/Statement.lean` | true | failed | 1 deliberate `sorry` in `h16_2` | includes `sorryAx` — not formalised, as designed |

`Bautin.lean`'s `V3_not_mem_span_V1_V2` (L8∉⟨L4,L6⟩) is therefore a real
kernel-checked theorem: the implication from the three evaluations is checked,
the axioms are exactly the kernel's three. Good to build on.

## Certificate.lean — the general non-membership lemma (VERIFIED)

Self-contained, no `sorry`, no cited axiom, axioms `[propext,
Classical.choice, Quot.sound]`, verified by lean_check.

- `Certificate.eval_cert_nonmem : (φ : R →+* S) → φ f1 = 0 → φ f2 = 0 →
  φ f3 ≠ 0 → f3 ∉ Ideal.span {f1, f2}`
- `Certificate.eval_point_cert_nonmem`: the same with `φ = MvPolynomial.eval p`.

This is the quotient-homomorphism / cofactor-linear-functional certificate
underlying the Bautin.lean evaluation witness and Route A below. Do not
re-derive it.

## Second evaluation point — independent route (found + kernel-checked shape)

`code/bautin/cofactor_certificate2.py` (exact sympy, full-box sweep over
{-3..3}^6, proportionality check against certPt) found:

    certPt2 = (a1,a2,a3,b1,b2,b3) = (-3,-3,2,0,1,-1)
    L4=0, L6=0, L8=-25/8 ≠ 0 ; non-proportional to certPt
    cleared: V1num=0, V2num=0, V3num=-57600 (denoms 8/192/18432)

Capture: `code/out/cofactor_certificate2.captured.txt`.

## L8NotInIdeal_alt.lean — second route to the SAME statement (compiles)

- **Route A** `second_point_route` — quotient-homomorphism certificate at
  certPt2: **KERNEL-CLOSED** (axioms `[propext, Classical.choice,
  Quot.sound]`). Takes the three evaluation hypotheses as binders; those are
  established by the capture, not by the kernel. The same non-membership
  theorem as Bautin.lean, proved through a genuinely distinct second point.
- **Route B** `graded_membership_shape` — graded/degree-6 reformulation
  (L8 = a4·L4 + b2·L6 with a4, b2 homogeneous of degrees 4, 2). **`by sorry`**
  gap, {gap id: graded-reformulation-L8}. Needs the homogeneous-degree
  decomposition of MvPolynomial (projection onto R_d) and the
  multiplicativity of the filtration — not in the file, not needed by Route A.

## What closed / what stayed sorry

- Closed: `Certificate.eval_cert_nonmem`, `eval_point_cert_nonmem`
  (verified); `BautinAlt.second_point_route` (verified). Re-confirmed:
  `Bautin.lean.V3_not_mem_span_V1_V2`, all of `BautinRecurrence.lean`.
- Sorry: `BautinAlt.graded_membership_shape` (Route B, deliberate gap);
  `H16.h16_2` (Statement.lean, deliberate; not part of this task).
