# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `_run_tmp.py` | _(undescribed)_ |
| `brute.py` | _(undescribed)_ |
| `confirm_hexagon_closedform.py` | Independent mpmath confirmation of V_hexagon = 2 + 2sqrt21/3 via two routes (stewbasic direct eval vs closed-form surd), agreeing to 4.27e-50 and matching the 8-dp answer. |
| `explore_general_dash.py` | Disproof oracle-check: general straight-line dash (free direction phi) from the stage point (rho,0), landing where the ray hits the unit circle, runner takes shorter arc from antipode. >V = pi+1 = 4.14159265 for every dash direction. This is the brute-force proof that the task's "stage at antipode then dash" model cannot reproduce 4.60333885: any straight dash from the radially-opposite stage point tops out at pi+1. Kept as the falsifying oracle that forced the correct two-phase model in brute.py. |
| `hex_check.py` | Hand-cross-check of stewbasic general-n formula for n=4 and n=6 (redundant with polygon_critical.py; kept as an independent numeric reference for the hexagon candidate). |
| `hexagon_closed_form.py` | _(undescribed)_ |
| `hexagon_verify_exact.py` | Fully exact sympy derivation of the hexagon closed form V(6)=2+2sqrt21/3: shows acos arg = -1/8, cos(alpha)=(sqrt21-3)/8, V=8/(sqrt21-3)=(6+2sqrt21)/3 rationalized, plus K=2 sign check. Exact algebraic confirmation of the PE 761 hexagon answer 5.05505046. |
| `indep_game_encoding.py` | Independent game-encoding solver (geometry-first bisection on g(v)=v, NO stewbasic K/alpha formula — verified by reading the source). Ran it: it does NOT reproduce the oracles; it encodes the naive straight-dash model, a known dead end. Output in `indep_game_encoding_OUTPUT.txt`: circle 4.14159 vs 4.60333885, square 4.09372 vs 5.78859314, hexagon 3.98231 vs 5.05505046. Not a second verification of V_hexagon; the value remains single-route (stewbasic formula + exact closed form). |
| `indep_game_encoding_OUTPUT.txt` | Captured full run output of `indep_game_encoding.py` (5 bisections on g(v)=v plus r=0 controls). Shows the staging model reproduces NONE of the three oracles (circle=pi+1=4.14159, square=4.09372, hexagon=3.98231) — the solver is the naive straight-dash model, not the real two-phase (staging-arc + tangent-chord) game. |
| `indep_sanity_circle.py` | Independent coarse reimplementation of the script's circle geometry. Confirms the hand analysis: straight dash from a radial-opposite stage point gives g(v)=max_theta theta/sqrt(1+r^2+2r cos theta)=pi/(1-r) (attained at theta=pi) and fixed point v=pi+1=4.14159, matching the script's delta=pi result; delta=0 gives pi-1=2.14159. Shows the solver's circle value is exactly the naive bound and can never reach 4.60333885. |
| `indep_time_probe.py` | Budget probe timing one g_ratio full-grid call per shape for indep_game_encoding (~0.08-0.17 s/call) to confirm the full run fits the 600 s tool budget. |
| `k_deviation_structure.py` | _(undescribed)_ |
| `k_sequence_exact.py` | _(undescribed)_ |
| `patseq_deg.py` | _(undescribed)_ |
| `patseq_k.py` | Computes K(n) (stewbasic critical-speed cutoff index) for regular n-gons n=3..60 with mpmath dps=50, printed as a comma list. K(n)=largest k in [0,n] with sin(k*pi/n)-(k+n)tan(pi/n)cos(k*pi/n)<0. Correct per the definition; cross-checked against an exact sympy route for the same range (identical output) and matches known K values (K(4)=1, K(6)=2, K(3)=1). |
| `patseq_k_recurrence_falsify.py` | Finds the exact first n where the empirically-observed K(n) order-8 recurrence fails (n=86) and where K(n)!=floor(3n/7) (also n=86), with valid anchors K(3..10). This is the falsifying term for the period-7 structure conjecture. |
| `pattern_V_closedforms.py` | _(undescribed)_ |
| `pattern_asymptotic.py` | _(undescribed)_ |
| `pattern_asymptotic2.py` | _(undescribed)_ |
| `pattern_break.py` | _(undescribed)_ |
| `pattern_clean.py` | _(undescribed)_ |
| `pattern_d_structure2.py` | _(undescribed)_ |
| `pattern_deg_phi.py` | _(undescribed)_ |
| `pattern_deg_phi2.py` | _(undescribed)_ |
| `pattern_deg_phi3.py` | _(undescribed)_ |
| `pattern_deg_single.py` | _(undescribed)_ |
| `pattern_fail_list.py` | _(undescribed)_ |
| `pattern_findings.md` | Pattern-finder deliverable: asymptotic slope c of K(n) (root of tan(cπ)=π(c+1)), proof that floor(3n/7) is asymptotically wrong, K(n)~floor(c·n) robustness, and that K-deviations don't affect the hexagon answer. |
| `pattern_hexagon.py` | _(undescribed)_ |
| `pattern_k_c_attack.py` | Attack K(n)=floor(c*n), c=0.43029665312 (root tan(c*pi)=pi*(c+1)); finds first failure n=165 and total fails in n in [3,2999]. |
| `pattern_k_check.py` | Exact sympy check that K(n) != floor(3n/7) (first fails n=86) and != floor(n*sqrt(3)/4) Beatty (first fails n=37). Confirm exact K(n) values. |
| `pattern_k_closedform.py` | _(undescribed)_ |
| `pattern_k_deviation_linear.py` | _(undescribed)_ |
| `pattern_k_deviation_structure2.py` | _(undescribed)_ |
| `pattern_k_fail_details.py` | _(undescribed)_ |
| `pattern_k_find_mismatch.py` | _(undescribed)_ |
| `pattern_k_gen.py` | _(undescribed)_ |
| `pattern_k_refined_model.py` | _(undescribed)_ |
| `pattern_k_structure.py` | _(undescribed)_ |
| `pattern_k_terms.py` | _(undescribed)_ |
| `pattern_k_threshold_structure.py` | _(undescribed)_ |
| `pattern_k_verify.py` | _(undescribed)_ |
| `pattern_period7.py` | _(undescribed)_ |
| `pattern_recurrence_range.py` | _(undescribed)_ |
| `pattern_regenerate.py` | _(undescribed)_ |
| `pattern_root_asymptotic.py` | _(undescribed)_ |
| `pattern_v2degree_regenerate.py` | _(undescribed)_ |
| `pattern_vdeg2.py` | _(undescribed)_ |
| `pattern_vdeg_num.py` | _(undescribed)_ |
| `pattern_vdegree_seq.py` | _(undescribed)_ |
| `polygon_critical.py` | Computes the exact regular n-gon critical runner speed V(n) via the stewbasic formula. Validation: matches Abel et al. exact triangle/square values and the statement oracle 5.78859314. Yields V_hexagon=5.05505046. |
| `run_verify.py` | _(undescribed)_ |
| `solution.py` | PE 761 answer: exact stewbasic formula (math.SE 1762665) for regular n-gon critical speed V(n)=1/cos(alpha), mpmath dps=50. Reproduces anchors n=3->7.4049183473 (Abel), n=4->5.78859314459 (oracle 5.78859314), n->inf->4.60333885 (circle oracle, via tan mu=mu+pi). Answer V_hexagon=5.055050463303893 (15 dp), 5.05505046 (8 dp). |
| `v2_quad_independent2.py` | _(undescribed)_ |
| `v2_quadratic_test.py` | _(undescribed)_ |
| `verify_circle_constant.py` | Verifies the exact governing equation/constant for the circular swimmer-runner critical speed (Ponder This T = 4.60333885) via sympy, and the naive pi+1 bound. |
| `verify_hexagon.py` | High-precision sympy verification of V_hexagon=5.0550504633 (-> 5.05505046) and cross-checks against triangle/square closed forms and the circle limit. |
| `verify_polygon_formula.py` | Numerically evaluates stewbasic's general-n critical-speed formula (given alpha from root of tan(rθ)=(r+n)tanθ) for regular n-gons, checks the square against V_square oracle (5.78859314), the large-n limit against the circle oracle (4.60333885), and David K's independent square closed form sqrt(5/2(7+sqrt41)). |
| `verify_sources_geometry.py` | _(undescribed)_ |
