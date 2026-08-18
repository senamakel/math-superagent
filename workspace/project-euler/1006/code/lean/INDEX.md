# Index — code/lean

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `CorrectedMechanicalWord.lean` | Kernel-checkable central corrected mechanical-word factor representation; deep Fibonacci/Sturmian identification is explicitly cited as a conditional axiom. |
| `G4.lean` | _(undescribed)_ |
| `G4BlockStateNonClosure.lean` | Small corrected G4 obstruction theorem: k=2 binary blocks share count/sum/squares summary but have different rolling boundary cross terms. |
| `G4JointIntercept.lean` | Explicit Lean formalisation skeleton for the unresolved G4 joint-intercept/universal-Euclidean evaluation theorem; the sole open theorem remains sorry-marked. |
| `G4JointInterceptProposition.lean` | Kernel-checked precise statement of the unresolved fixed-dimensional G4 joint-intercept evaluator. |
| `G4Statement.lean` | Formal statement of the joint-intercept sum and the unresolved fixed-dimensional logarithmic evaluator, retaining the older conditional G4 shell. |
| `PE1006.lean` | _(undescribed)_ |
| `UniversalEuclideanComposition.lean` | Statement artifact for the universal-Euclidean weighted floor-moment segment composition law; hypotheses and composition formulas are explicit, with an intentional sorry proof. |
| `blueprint.lean` | _(undescribed)_ |
| `conjugate_christoffel_factor_sturmian-0be2e715.lean` | Decomposes the conjugate-Christoffel/Sturmian-factor node into explicit Lean gaps and a kernel-checkable combining equivalence. |
| `directive6_anchors_verified_incontainer-c98a97b5.lean` | Lean theorem formalising the numerical anchor residues and factor-count equalities for the directive-6 verification node. |
| `explore.lean` | _(undescribed)_ |
| `farey_slope_stabilisation-ab3f4c35.lean` | Formal statement shell for the Farey/Sturmian special-factor coincidence node; currently exposes the cited mathematical gap. |
| `fibonacci_position_theorem_contiguous_windows-af501dab.lean` | Formal statement of the Fibonacci contiguous-window position theorem, with finite-word definitions and an explicitly cited Proposition 1 axiom; the theorem is checked as a conditional implication. |
| `fibonacci_sturmian_complexity-1649cd8e.lean` | Decomposition of node fibonacci-sturmian-complexity: the count (FibSubwords k).ncard = k+1 split into subword_count_upper (≤ k+1) and subword_count_lower (≥ k+1, the constructive/existence half), with a kernel-checked combining theorem fib_subword_count = le_antisymm of the two. Provable shell (factor-chain nesting) reproduced sorry-free; the two bounds are declared gaps with next-moves; Cited.fibonacci_word_factor_complexity held as a conditional route only. Finite decide-certificates for k=3,4,5. |
| `g1_factor_chain_nested-de74dba9.lean` | Statement-graph node g1-factor-chain-nested: monotone nesting of PE1006 length-k factor sets. Defines fibWord (S_n), FactorSet, FibSubwords, and proves factorSet_chain (FactorSet(fibWord n) k ⊆ FactorSet(fibWord (n+1)) k) and factorSet_chain_any (monotone across n+d) sorry-free, axioms propext/Quot.sound only. |
| `g1_oracle_length3-ed70ff6a.lean` | Formalises node g1-oracle-length3: the length-3 Fibonacci subwords are exactly 001,010,100,101 — the length-3 factor set of S_5=0100101001001 has card 4 and equals {010,001,100,101}. Kernel-verified sorry-free via `decide` (no native_decide); file name carries claim id ed70ff6a. |
| `g1_sturmian_factor_structure_G1_count__fib_subword_count_-27ea8c49.lean` | Requested Lean statement and attempted proof of the positive-length Fibonacci subword count theorem. |
| `g2_mechanical_word_representation-d47418d3.lean` | Statement and conditional proof of the corrected G2 mechanical-word representation, with explicit cited rotational-factor axiom. |
| `g3_telescoped_second_moment-6c18394c.lean` | Lean formalisation of the G3 telescoped second-moment identity; defines the weighted floor expression and proves the stated sum equality by definitional unfolding. |
| `governing_factor_complexity-542ce8cd.lean` | Formalisation of node governing-factor-complexity: (1) governing_theorem_pos proves a Sturmian word (defined as factorComplexity s n = n+1 for all n, per Morse-Hedlund) has exactly k+1 length-k factors — this is definitional and sorry-free, status formalised; (2) fib_subword_count (FibSubwords k).ncard = k+1 is the Fibonacci-word consequence, resting on two Cited axioms (fibonacci_sturmian, factors_stabilise) — status conditional. |
| `mechanical_word_digit_rule-f4995b0e.lean` | _(undescribed)_ |
| `monoid_composition_formulas_verified-9ccd80eb.lean` | Decomposition of the geometric floor-sum monoid composition claim into representation preservation, associativity, and Euclidean merge correctness, with a combining theorem. |
| `pe1006_contiguous_window_prefix_CW1_terminal_window_set-ce5f2423.lean` | Decomposes CW1 terminal-window set into factor stabilization, terminal index coverage, and uniqueness; combines the open leaves. |
| `pe1006_contiguous_window_prefix_CW2_rolling_window_recurrence-240fc05d.lean` | _(undescribed)_ |
| `pe1006_contiguous_window_prefix_CW3_summary_composition-2dd515e8.lean` | Lean formalisation of CW3: additive summaries over adjacent finite window ranges compose, with associative componentwise addition. |
| `pe1006_contiguous_window_prefix_CW5_terminal_correction-3084f1e6.lean` | CW5 decomposition of terminal cyclic-window correction; isolates the missing width hypothesis, proves interval partition/sum helpers, and combines them with an open terminal-identification leaf. |
| `pe1006_psi_G1_factor_chain-87f94deb.lean` | The kernel-verified (sorry-free, axioms propext/Quot.sound) provable shell of node G1-sturmian-factor-structure: fibWord/S_n definition, FactorSet (length-k factors), FibSubwords k = union over S_n, and the monotone nesting factorSet_prefix_nest / factorSet_chain / factorSet_chain_any (a factor of S_n is a factor of S_{n+1} since S_n is a prefix of S_{n+1}). Backs claim g1-factor-chain-nested. The count theorem is gapped in the sibling file pe1006_psi_G1_sturmian_factor_structure-87f94deb.lean. |
| `pe1006_psi_G1_finite_subword_limit_identification-74d235bb.lean` | Decomposition of finite Fibonacci subword limit identification into prefix stabilization, finite/infinite factor equivalence, and Sturmian complexity lemmas. |
| `pe1006_psi_G1_sturmian_factor_structure-87f94deb.lean` | Node G1-sturmian-factor-structure: the full statement of the Sturmian factor-complexity count fib_subword_count : (FibSubwords k).ncard = k+1 with h : 1 ≤ k, left as a declared gap (sorry) — the mathematical heart, not yet formalised; plus factor_limit_stabilises restatement and Cited.sturmian_factor_complexity axiom (unused). The provable nesting shell is split into the sibling verified file pe1006_psi_G1_factor_chain-87f94deb.lean; oracle example (length-3 factors {001,010,100,101}) checked via native_decide. |
| `pe1006_psi_G2_mech_shell-1f79c34f.lean` | Sorry-free kernel-verified shell of node G2: slope in [0,1], digits in {0,1}, exact-binary mechanical words with corrected slope fib(n)/fib(n+2). Verified by lean_check (axioms propext/Classical.choice/Quot.sound). The deep factor-identity is gapped in the companion node file. |
| `pe1006_psi_G2_mechanical_factor_parametrisation-3b6fbf7e.lean` | Conditional Lean formalisation of the G2 mechanical-factor parametrisation statement, with explicit convergent, intercept, digit, word, and factor-set binders. |
| `pe1006_psi_G2_mechanical_word_representation-1f79c34f.lean` | Node G2 statement file with corrected slope: formalises the mechanical/rotation representation of the length-k factors of the Fibonacci word. Shell lemmas proved; the deep factor identity mech_reproduces_factors/mech_set_card are declared gaps (sorry + Cited axiom, not formalised). |
| `pe1006_psi_G3_telescoped_decimal_second_moment-89c7a94a.lean` | _(undescribed)_ |
| `pe1006_psi_G3_telescoped_v-1f79c34f.lean` | G3 telescoped-v identity statement: wordVal a x k = telescoped a x k (digit-weighted mechanical word value equals its telescoped second-moment floor-sum form), stated with the hypotheses 1≤k, 0<a<1, proof left := by sorry. Kernel-checked. |
| `pe1006_psi_G4_joint_intercept_evaluation-fd780321.lean` | _(undescribed)_ |
| `pe1006_psi_G4_universal_euclidean_floor_sum-7383014a.lean` | G4 decomposition of the PE1006 universal-Euclidean double-sum claim into node composition, recursion semantics, quadratic moment extraction, and orbit-index encoding lemmas. |
| `pe1006_psi_goal-1f79c34f.lean` | Overall PE1006 goal in the mechanical-word second-moment language: G3 telescoped-v identity, digit/wordVal/telescoped defs, arc-midpoint representatives, PsiMech (sum of v(x_m)^2), and the two key theorems psi_mech_reduction (Psi(k) ≡ PsiMech a k mod M) and pe1006_answer_active (the k=10^18 residue, given existentially). All theorems := by sorry, kernel-checked. |
| `pe1006_psi_pe1006_psi_G1_finite_subword_limit_identification-fee23d1f.lean` | _(undescribed)_ |
| `pe1006_psi_pe1006_psi_G2_mechanical_factor_parametrisation-5857f6ca.lean` | Lean formalisation of the G2 mechanical-factor parametrisation statement; the implication is checked conditional on the explicitly cited Sturmian rotational-factor axiom. |
| `pe1006_psi_pe1006_psi_G3_telescoped_decimal_second_moment-f2d769d6.lean` | _(undescribed)_ |
| `pe1006_psi_pe1006_psi_G4_joint_intercept_evaluation-5dbefc6d.lean` | _(undescribed)_ |
| `probe_algebra.lean` | _(undescribed)_ |
| `probe_anchor.lean` | _(undescribed)_ |
| `probe_char_binary.lean` | _(undescribed)_ |
| `probe_floor_normnum.lean` | _(undescribed)_ |
| `probe_lowshift.lean` | _(undescribed)_ |
| `probe_wiki.lean` | _(undescribed)_ |
| `research.lean` | _(undescribed)_ |
| `ueuclid_incontainer_fails_s1s2-e1947a2b.lean` | _(undescribed)_ |
| `ueuclid_s1s2_false_alarm_refuted-b0766630.lean` | Kernel-checkable 1-indexed S1/S2 arithmetic refuting the false alarm; proves the stated instance values 547 and 2551. |
| `universal_euclidean_geometric_floor_sum-8768a07e.lean` | _(undescribed)_ |
