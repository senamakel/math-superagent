# Index — code/lean/Lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `Bautin.lean` | _(undescribed)_ |
| `BautinRecurrence.lean` | Hand-written Lean checker for the H14^3 finite core: reconstructs P30 from untrusted Generated/P30Data data, closes checkP30 (P30 + 12*weighted_g6 = 0) by decide; restates Darboux/bridge identities (part B) with named sorries pending the in-Lean recurrence. |
| `Certificate.lean` | General, self-contained, kernel-verified certificate lemma for ideal non-membership: a ring hom φ R->+* S with φ f1 = φ f2 = 0 and φ f3 ≠ 0 proves f3 ∉ Ideal.span {f1,f2}; plus its MvPolynomial.eval form. This is the quotient-homomorphism/linear-functional certificate that underlies the Bautin.lean evaluation witness and L8NotInIdeal_alt.lean Route A. |
| `CheckProof.lean` | _(undescribed)_ |
| `L8NotInIdeal_alt.lean` | Second INDEPENDENT route to L8 ∉ ⟨L4,L6⟩ (same statement as Bautin.lean's V3_not_mem_span_V1_V2). Route A: quotient-homomorphism certificate at a second, non-proportional evaluation point certPt2=(-3,-3,2,0,1,-1) — kernel-closed (second_point_route). Route B: graded/degree-6 linear-algebra reformulation, stated with by-sorry gap (graded_membership_shape). Cross-checks the certPt proof via a fresh full-box search (cofactor_certificate2.py). |
| `Statement.lean` | H16.2 stated in Lean: PlanarPolyField n carries P Q : MvPolynomial (Fin 2) ℝ with totalDegree ≤ n; IsLimitCycle = non-constant periodic integral curve isolated in the set of periodic orbits; h16_2 states ∀ n, ∃ N, ∀ f, (LimitCycleSet f.toMap).Finite ∧ ncard ≤ N, ending in by sorry. Compiles via lean_check (only axiom beyond the kernel's own three is sorryAx from the intentional sorry). |
