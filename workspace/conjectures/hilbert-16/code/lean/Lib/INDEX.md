# Index — code/lean/Lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `Bautin.lean` | _(undescribed)_ |
| `BautinRecurrence.lean` | Hand-written Lean checker for the H14^3 finite core: reconstructs P30 from untrusted Generated/P30Data data, closes checkP30 (P30 + 12*weighted_g6 = 0) by decide; restates Darboux/bridge identities (part B) with named sorries pending the in-Lean recurrence. |
| `Certificate.lean` | General, self-contained, kernel-verified certificate lemma for ideal non-membership: a ring hom φ R->+* S with φ f1 = φ f2 = 0 and φ f3 ≠ 0 proves f3 ∉ Ideal.span {f1,f2}; plus its MvPolynomial.eval form. This is the quotient-homomorphism/linear-functional certificate that underlies the Bautin.lean evaluation witness and L8NotInIdeal_alt.lean Route A. |
| `CheckProof.lean` | _(undescribed)_ |
| `CurrentStatement.lean` | _(undescribed)_ |
| `DRR.lean` | _(undescribed)_ |
| `DRR_citation.lean` | _(undescribed)_ |
| `DRR_citations.lean` | _(undescribed)_ |
| `DumortierRoussarieRousseau1994.lean` | _(undescribed)_ |
| `ECT.lean` | _(undescribed)_ |
| `ECTSlowDivergence.lean` | Kernel-checked abstract ECT-family zero-bound lemma: a nontrivial linear combination on a finite-dimensional family has at most card(index)-1 zeros, conditional on the explicit ECT certificate; deliberately omits the open slow-divergence analytic reduction. |
| `FullCheck.lean` | _(undescribed)_ |
| `FullCheck2.lean` | _(undescribed)_ |
| `FullCheck3.lean` | _(undescribed)_ |
| `FullCheck4.lean` | _(undescribed)_ |
| `GMV.lean` | _(undescribed)_ |
| `L8NotInIdeal_alt.lean` | Second INDEPENDENT route to L8 ∉ ⟨L4,L6⟩ (same statement as Bautin.lean's V3_not_mem_span_V1_V2). Route A: quotient-homomorphism certificate at a second, non-proportional evaluation point certPt2=(-3,-3,2,0,1,-1) — kernel-closed (second_point_route). Route B: graded/degree-6 linear-algebra reformulation, stated with by-sorry gap (graded_membership_shape). Cross-checks the certPt proof via a fresh full-box search (cofactor_certificate2.py). |
| `LuH14Remainder.lean` | Lean statement of the conditional jointly-uniform analytic remainder bound needed to lift Lu's finite Bautin core to a displacement zero bound; proof intentionally open. |
| `Marin2026.lean` | _(undescribed)_ |
| `Probe.lean` | _(undescribed)_ |
| `Search.lean` | _(undescribed)_ |
| `Search2.lean` | _(undescribed)_ |
| `Search3.lean` | _(undescribed)_ |
| `Search4.lean` | _(undescribed)_ |
| `SecondTypeDulacRemainder.lean` | Kernel-checked conditional interface for second-type Dulac composition and uniform displacement zero transfer; exposes the unproved analytic hypotheses without claiming H16.2. |
| `SlowDivergenceECTBound.lean` | Kernel-checkable abstract combining lemma for a slow-divergence displacement represented by a nonzero ECT-family combination; exposes finite zero and cardinal hypotheses. |
| `SlowDivergenceECTPartial.lean` | Kernel-checked conditional theorem: explicit ECT and endpoint/remainder hypotheses imply a uniform zero bound for the composed displacement. |
| `SourceSummary.lean` | _(undescribed)_ |
| `Statement.lean` | H16.2 stated in Lean: PlanarPolyField n carries P Q : MvPolynomial (Fin 2) ℝ with totalDegree ≤ n; IsLimitCycle = non-constant periodic integral curve isolated in the set of periodic orbits; h16_2 states ∀ n, ∃ N, ∀ f, (LimitCycleSet f.toMap).Finite ∧ ncard ≤ N, ending in by sorry. Compiles via lean_check (only axiom beyond the kernel's own three is sorryAx from the intentional sorry). |
| `StatementLibraryCycle.lean` | Typed blueprint for H16.2 used in the library-building cycle; exposes the missing flow, periodic-orbit, and isolatedness interfaces instead of claiming Mathlib already provides them. |
| `claimed_hilbert_number_formula.lean` | _(undescribed)_ |
| `cycle-index-note.md` | _(undescribed)_ |
| `g_drr_status-a0a5b3a8.lean` | _(undescribed)_ |
| `g_drr_status.lean` | _(undescribed)_ |
| `global_uniform_bound_elementary_sphere_family.lean` | _(undescribed)_ |
| `hyperbolic_polycycle_delta_zero_iff_all_ratios_one.lean` | _(undescribed)_ |
| `node_g_transition.lean` | _(undescribed)_ |
| `research_summary.lean` | _(undescribed)_ |
| `target.lean` | _(undescribed)_ |
| `target_node.lean` | _(undescribed)_ |
