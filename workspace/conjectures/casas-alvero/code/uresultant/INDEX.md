# Index — code/uresultant

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `_charp_debug.py` | _(undescribed)_ |
| `_debug_elim.py` | _(undescribed)_ |
| `_debug_elim2.py` | _(undescribed)_ |
| `_dump_gb.py` | _(undescribed)_ |
| `_fix_length.py` | _(undescribed)_ |
| `_full_length.py` | _(undescribed)_ |
| `_full_resultant.py` | _(undescribed)_ |
| `_gb_full.py` | _(undescribed)_ |
| `_length_cap.py` | _(undescribed)_ |
| `_probe2.py` | _(undescribed)_ |
| `_probe3.py` | _(undescribed)_ |
| `_probe3b.py` | _(undescribed)_ |
| `_probe4.py` | _(undescribed)_ |
| `_probe4b.py` | _(undescribed)_ |
| `_probe_n4.py` | _(undescribed)_ |
| `_probe_n7.py` | _(undescribed)_ |
| `_probe_n7_construct.py` | _(undescribed)_ |
| `_probe_n8_construct.py` | _(undescribed)_ |
| `_probe_n8_cost.py` | _(undescribed)_ |
| `_recheck_n4.py` | _(undescribed)_ |
| `_reconcile.py` | _(undescribed)_ |
| `_singular_mult.py` | _(undescribed)_ |
| `_slice_length.py` | _(undescribed)_ |
| `_verify_n4.py` | _(undescribed)_ |
| `closed_form_check.py` | _(undescribed)_ |
| `closed_form_derivation.md` | _(undescribed)_ |
| `extend_n6.py` | _(undescribed)_ |
| `extend_n6_capture.py` | Captures the n=6 Samuel-multiplicity extension of the CA traceless-slice scheme: oracle guard on (x-1)^6, Singular vdim (dp/std/vdim, exact), independent Samuel identity ord_0(R_i)=n(n-i) with prod/prod check, writes code/out/uresultant_n6.captured.txt temp-file-then-move. Exit 0 iff no FAIL. |
| `extend_n6_n7.py` | _(undescribed)_ |
| `extend_n7_capture.py` | _(undescribed)_ |
| `mult_map_multiplicity.py` | _(undescribed)_ |
| `multmap_n45_certificate.py` | Lex-free u-resultant certificate for the CA traceless-slice scheme at degrees 4 and 5. (A) At n=4, validates the multiplication-map characteristic polynomial: mul-by-a2 on the 16-dim quotient QQ[a2,a3,a4]/I has char poly the pure power t^16 = 4^2, so V(I)={0} (=CA) certified without lex, agreeing with the lex eliminant u^8. (B) At n=5, extends past the lex wall (which does not close in 180s): exact coordinate nilpotency via Singular reduce gives a2^19, a3^13, a4^10, a5^1 all in I; together with 0-dim vdim=125=5^3 this certifies rad(I)=m_0, V(I)={0}=CA at degree 5 using only the grevlex GB. Engine Singular 4.3.1 dp/std/reduce, exact rational arithmetic, oracle-guarded by lib.casas_alvero is_ca/is_pure_power on (x-1)^n. Established correct: ALL CHECKS PASSED (code/out/uresultant_n5_multmap.captured.txt). |
| `n5_boundary_capture.py` | _(undescribed)_ |
| `n5_cost_probe.py` | _(undescribed)_ |
| `probe_n5_debug_f.py` | _(undescribed)_ |
| `probe_n5_dim.py` | _(undescribed)_ |
| `probe_n5_gbcheck.py` | _(undescribed)_ |
| `probe_n5_hunt.py` | _(undescribed)_ |
| `probe_n5_membership.py` | _(undescribed)_ |
| `probe_n5_membership2.py` | _(undescribed)_ |
| `probe_n5_modp.py` | _(undescribed)_ |
| `probe_n5_restrict.py` | _(undescribed)_ |
| `probe_n5_singular.py` | _(undescribed)_ |
| `probe_n5_singular2.py` | _(undescribed)_ |
| `probe_n7_slimgb.py` | _(undescribed)_ |
| `probe_n7_vdim.py` | _(undescribed)_ |
| `ureesultant_first_step_clean.py` | _(undescribed)_ |
| `uresultant_n4_certificate.py` | _(undescribed)_ |
| `verify_disc_sign_content.py` | Confirms sign R_1=(-1)^{n(n-1)/2}Disc (n=3..7) and content of R_{n-1}=n^n (char-p collapse when p |
| `verify_extreme_closedforms.py` | Verifies the extreme closed forms of R_i against true resultants: i=n-1 gives (-1)^n n^n a_n, i=1 gives ±Discriminant. n=3..6. |
| `verify_leadcoeff_explicit.py` | Re-confirms root-form weighted-homogeneity of R_i and evaluates the leading (whole) weighted term ∏_k e_{n-i}({beta_k-beta_j}) at distinct traceless rational points; supports Lemma B. |
| `verify_leadcoeff_traceless.py` | _(undescribed)_ |
| `verify_leadcoeff_traceless2.py` | Shows the leading weighted coefficient of R_i (∏_k e_{n−i} of root differences) is nonzero on the traceless slice Σβ=0, for n=3..8, at distinct exact integer roots. The i=1 leading coefficient equals the discriminant squared (nonzero for distinct roots). |
| `verify_lemmaB_rigorous.py` | Stress-tests Lemma B of weighted-order-theorem.md: symbolically expands each elementary-symmetric factor e_{n-i}({beta_k-beta_j}) in the free traceless parameters and confirms every factor is a nonzero polynomial (n=3..7), making the product's nonvanishing a symbolic fact not merely a point sample. |
| `verify_length_direct.py` | Actual quotient length |
| `verify_length_formula.py` | _(undescribed)_ |
| `verify_length_orders.py` | Confirms ∏_i ord_0(R_i)/n! == n^(n−2) for n=3,4,5 (3,16,125), i.e. the Samuel length predicted by the weighted orders. |
| `verify_length_stdmonos.py` | _(undescribed)_ |
| `verify_order_length_independent.py` | _(undescribed)_ |
| `verify_order_n6.py` | Exact weighted order ord_0(R_i) at n=6 via resultant substitution; confirms {30,24,18,12,6}=6(6−i) too, extending the identity's direct check to n=6. |
| `verify_samuel_n45.py` | _(undescribed)_ |
| `verify_weighted_homogeneous.py` | Proof-of-A check for weighted-order-theorem.md: confirms R_i=Res_x(f,H_i) is exactly weighted-homogeneous of degree n(n-i) by decomposing into monomials and checking every term's weight, n=3,4,5. ALL HOMOGENEITY CHECKS PASS. |
| `verify_weighted_order.py` | Proves ord_0(R_i)=n(n−i) for n=3..8: Method A computes the exact resultant R_i=Res_x(f,H_i) over QQ[a_2..a_n], substitutes a_j→t^j a_j, reads the lowest t-exponent and its (nonzero) coefficient; Method B evaluates the structural product ∏_k e_{n−i}((β_k−β_j)) to show the leading coefficient is nonzero. Both exact. |
