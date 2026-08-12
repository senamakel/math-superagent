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
| `k_deviation_structure.py` | _(undescribed)_ |
| `k_sequence_exact.py` | _(undescribed)_ |
| `pattern_V_closedforms.py` | _(undescribed)_ |
| `pattern_asymptotic.py` | _(undescribed)_ |
| `pattern_asymptotic2.py` | _(undescribed)_ |
| `pattern_break.py` | _(undescribed)_ |
| `pattern_clean.py` | _(undescribed)_ |
| `pattern_findings.md` | Pattern-finder deliverable: asymptotic slope c of K(n) (root of tan(cπ)=π(c+1)), proof that floor(3n/7) is asymptotically wrong, K(n)~floor(c·n) robustness, and that K-deviations don't affect the hexagon answer. |
| `pattern_hexagon.py` | _(undescribed)_ |
| `pattern_k_check.py` | Exact sympy check that K(n) != floor(3n/7) (first fails n=86) and != floor(n*sqrt(3)/4) Beatty (first fails n=37). Confirm exact K(n) values. |
| `pattern_k_closedform.py` | _(undescribed)_ |
| `pattern_k_deviation_linear.py` | _(undescribed)_ |
| `pattern_k_fail_details.py` | _(undescribed)_ |
| `pattern_k_find_mismatch.py` | _(undescribed)_ |
| `pattern_k_structure.py` | _(undescribed)_ |
| `pattern_k_terms.py` | _(undescribed)_ |
| `polygon_critical.py` | Computes the exact regular n-gon critical runner speed V(n) via the stewbasic formula. Validation: matches Abel et al. exact triangle/square values and the statement oracle 5.78859314. Yields V_hexagon=5.05505046. |
| `run_verify.py` | _(undescribed)_ |
| `solution.py` | PE 761 answer: exact stewbasic formula (math.SE 1762665) for regular n-gon critical speed V(n)=1/cos(alpha), mpmath dps=50. Reproduces anchors n=3->7.4049183473 (Abel), n=4->5.78859314459 (oracle 5.78859314), n->inf->4.60333885 (circle oracle, via tan mu=mu+pi). Answer V_hexagon=5.055050463303893 (15 dp), 5.05505046 (8 dp). |
| `verify_circle_constant.py` | Verifies the exact governing equation/constant for the circular swimmer-runner critical speed (Ponder This T = 4.60333885) via sympy, and the naive pi+1 bound. |
| `verify_hexagon.py` | High-precision sympy verification of V_hexagon=5.0550504633 (-> 5.05505046) and cross-checks against triangle/square closed forms and the circle limit. |
| `verify_polygon_formula.py` | Numerically evaluates stewbasic's general-n critical-speed formula (given alpha from root of tan(rθ)=(r+n)tanθ) for regular n-gons, checks the square against V_square oracle (5.78859314), the large-n limit against the circle oracle (4.60333885), and David K's independent square closed form sqrt(5/2(7+sqrt41)). |
