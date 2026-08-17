# Lean status — Statement.lean, BautinRecurrence.lean, Generated/P30Data.lean

Verification note for the Lean deliverable files touching the directive.

## Files

- `code/lean/Lib/Statement.lean` — H16.2 stated with **real** degree bound
  (`f.P.totalDegree ≤ n`, `f.Q.totalDegree ≤ n`, via `PlanarPolyField` carrying
  two `MvPolynomial (Fin 2) ℝ`), and with the **non-vacuous** finiteness
  statement `(LimitCycleSet f.toMap).Finite ∧ (LimitCycleSet f.toMap).ncard ≤ N`.
  The old `degree_at_most : True` and the vacuous bare-`ncard` inequality are
  gone. The lone `:= by sorry` at `h16_2` is the deliberate deliverable.
  Axioms expected on elaboration: `propext` (from the `sorries`), `Classical`,
  `Quot.sound` (from `MvPolynomial`/`Set`). NOT yet compiled in this pass
  (no Lean tool); lean_prover must compile and report #print axioms + sorry.

- `code/lean/Lib/Generated/P30Data.lean` — UNTRUSTED data: `ms : Fin 30 → Fin 5 → Nat`
  (30 monomial exponent vectors) and `coeffs : Fin 30 → ℤ` (30 integer
  coefficients of P30). No theorems inside. The 30 entries match the
  certificate `verify_bautin_recurrence.py`'s spelled-out P30 term by term:
  76A³C, 24A³F, 142A²CD, 29A²CE, 192A²DF, −96A²EF, 23AC³, 109AC²F, 76ACD²,
  42ACDE, 3ACE², 144ACF², 132AD²F, −28ADEF, −37AE²F, −24AF³, 23C³D, 159C²DF,
  −27C²EF, 10CD³, 13CD²E, 3CDE², 350CDF², −101CEF², 20D³F, 16D²EF, −27DE²F,
  248DF³, E³F, −124EF³.

- `code/lean/Lib/BautinRecurrence.lean` — the checker, written by hand OUTSIDE
  Generated/. It reconstructs `P30poly` from the untrusted dataset 1 and
  `W6poly` (the integer `12·weighted_g6`, stated separately as dataset 2) from
  dataset 2, defines `checkP30 := decide (P30poly + W6poly = 0)`, and closes
  `h14_p30_check : checkP30 = true` by `decide` — the directive's required
  shape (untrusted data in Generated/, checker outside, `decide` not
  `native_decide`). The two datasets are stated independently so a
  transcription error in either FAILS the check rather than silently passing.
  Also restates the Darboux/bridge identities (part B) which `ring` can close.
  `bautin_L6_identity`, `bautin_L4_identity`, `darboux_identities` are LEFT as
  named `sorry`s pending the in-Lean recurrence / explicit-coordinate Lie
  derivative — each is located and declared; none is silently true. The former
  body of BautinRecurrence.lean (P30 = 0 placeholder) is replaced.

## Honest scope (what this does and does not establish)

- `h14_p30_check` proves the two transcribed datasets (P30 and its negation
  scaled by 1/12, i.e. 12·weighted_g6) are consistent, i.e. `P30 + 12·weighted_g6
  = 0` — exactly the certificate's `192·L6 + P30 = 0` with L6 = weighted_g6/16.
  This is a transcription-consistency check between two copies of the same
  certificate data, NOT an independent re-derivation of weighted_g6 from the
  recurrence. The independent re-derivation is `code/bautin/verify_lu_core.py`,
  which is written but NOT executed (no execution tool in this pass).
- Nothing here proves the full H14^3 theorem (finite cyclicity of the graphic).
  The human-proof remainder (root uniqueness, Hadamard divisibility, domain
  completeness, zero theorems) is not machine-checked, and the Lu 2026 preprint
  is unrefereed.

## Required next steps (for lean_prover / tool_builder / coder)

1. Compile Statement.lean; report #print axioms and the (single) h16_2 sorry.
2. Compile BautinRecurrence.lean + Generated/P30Data.lean; confirm `decide`
   closes `h14_p30_check : checkP30 = true`, and report #print axioms and every
   remaining sorry (bautin_L6_identity, bautin_L4_identity, darboux_identities).
3. Run `python code/bautin/verify_lu_core.py` and file
   `code/out/lu_core.captured.txt`. Until that capture shows
   "ALL ASSERTIONS PASS", the Lu finite core is NOT verified-computationally.
4. Run `python code/bautin/generate_p30.py` to re-emit Generated/P30Data.lean
   and diff against the hand-written data (a cross-check of the transcription).
