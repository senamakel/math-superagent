# Claim — Lu H14³ finite-core identity half, checked by executed run

Beside the capture `code/out/lu_core.captured.txt`. Filed here by the reducer
so the goals ledger can mark the identity half of `G-lu-core` discharged by a
claim rather than by an unanchored program: a claim a program produced belongs
in the ledger with `status: checked` and its evidence on disk.

```claim
id: lu-finite-core-identity-half-checked
statement: The identity half of Lu arXiv:2607.13785's finite algebraic core is
       verified by an executed clean-room run: the Bautin/Lyapunov recurrence
       gives 8·L4 = AC+CD+2DF−EF and 192·L6+P30 = 0 (also 12·weighted_g6+P30=0),
       P30 is exactly the 30-monomial polynomial spelled out in the certificate,
       and the Darboux identities X(L)=(x+dy)L, X(F)=(2Bx+dy)F with the
       inverse-integrating-factor cofactor div X=(x+dy)+(2Bx+dy) hold.
hypotheses: n=2 quadratic focus normal form; homogeneous quadratic part
       Q1 = A u^2 + C u v + D v^2, Q2 = E u v + F v^2; rotation
       R(p) = −v p_u + u p_v; recurrence R(c_k)+Q1 V_{k-1,u}+Q2 V_{k-1,v}
       = L_k (u^2+v^2)^{k/2}, gauge c_{k,0}=0; H14^3 field
       P = −y−dx+B(x^2−y^2), Q = (1+y)(x+dy), L=1+y, F the conic as in the
       paper. Exact sympy rational/symbolic arithmetic, no floats.
holds-here: yes — this is the H14^3 five-parameter unfolding B=0 case of RR 2015
       Theorem 3.1, the run's target graphic.
status: checked
verified-by: executed run `python code/bautin/verify_lu_core.py`, capture
       code/out/lu_core.captured.txt ("ALL CLEAN-ROOM CHECKS PASS", checks
       I–VI); cross-confirmed by code/out/mono_counts.captured.txt (L4
       reconciliation True; exact monomial counts L4:4, L6:30, L8:97, L10:236,
       L12:485, L14:890).
bearing: the algebraic identities that make the center-ideal division of the
       displacement legitimate (the Bautin trick); they are the finite core of
       the H14^3 finite-cyclicity claim and the content G-lean-cert must carry
       to the kernel.
anchor: code/out/lu_core.captured.txt; code/out/mono_counts.captured.txt
search-frame: exact symbolic sweep of the Bautin/Lyapunov recurrence (rotation
       R, homogeneous quadratic Q1,Q2 in 5 vars A,C,D,E,F over Q) through
       degrees k=3..6, full homogeneous terms at each degree (c_{k,0}=0 gauge),
       plus the Darboux/Lie-derivative identities over the 5-parameter (B,mu2,
       mu4,mu5,d) bridge — the same universe Lu's certificate `verify_bautin_
       recurrence.py` computes in, re-derived clean-room without importing it.
scope-limits: DOES NOT include the ideal memberships L8∈⟨L4,L6⟩,
       L10,L12∈⟨L4,L6,L8⟩ (lyap_extend.py crashed in poly_terms — still open),
       nor the analytic remainder of Lu's Theorem 1 (root uniqueness, Hadamard
       divisibility, domain completeness, zero theorems — G-remainder).
```

**What this does not claim.** No theorem of finite cyclicity is established
here; the preprint is unrefereed; the cyclicity bound is existential; the
membership extension and the analytic remainder remain open (gaps `G-lu-core`
extension half, `G-lean-cert`, `G-remainder` in
`research/backward/h16-2-h14-3-finite-cyclicity.md`).