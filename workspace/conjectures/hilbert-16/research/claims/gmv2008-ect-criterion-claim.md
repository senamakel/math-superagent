```claim
id: gmv2008-ect-criterion
statement: For analytic Abelian integrals I_i(h)=∮_{γ_h} f_i(x)g(y)dx over ovals of H=Φ(x)+Ψ(y), the balances B_{σ1}(f_i/Φ') and B_{σ2}(g_i), with g_0=g and g_{i+1}=g_i'/Ψ', forming CT-systems and B_{σ2}(g_0)=o(y^{2m(n−2)}) imply that (I_0,…,I_{n−1}) is an ECT-system; in the form H=A(x)+B(x)y^{2m}, g=y^{2s−1}, it suffices that s>m(n−2) and the corresponding balances ℓ_i form a CT-system (Grau–Mañosas–Villadelprat 2008, arXiv:0805.1140).
hypotheses: analytic functions; a period annulus of ovals; separated Hamiltonian H=Φ+Ψ (or H=A+B y^{2m}); stated involutions and balance conditions; for Theorem B, s>m(n−2).
holds-here: unchecked (the analytic family here is the reduced displacement, not verified to be of this Abelian form)
status: proved
evidence: sourced — full text research/sources/grau-manosas-villadelprat-chebyshev-abelian-2008-arxiv.full.md; summary research/summaries/slow-divergence-ect-route-rr2015-huzak2018-gmv.md.
falsifier: A counterexample to the balance→ECT implication under the stated hypotheses would falsify the criterion; the hypotheses being unverified for the full I^1_6b displacement is a separate, standing gap (see i6b-slow-divergence-ect-not-applicable-as-held), not a falsification of the criterion itself.
formalisation: code/lean/gmv2008_ect_criterion-ada3b5cc.lean (interface theorem only, placeholder definitions; not a formalisation of the analytic GMV theorem)
note: This block previously had no statement, so the entailment ledger could not read it and flagged h16-ftv2013-chebyshev-abelian-ca as "following from nothing". The statement is restored from the documented summary content. The GMV criterion does not by itself control the full nonlinear, parameter-uniform displacement map near the blown-up nonhyperbolic graphic.
follows-from:
answers: slow-divergence-ect-missing-step
```
