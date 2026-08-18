# Slow-divergence / ECT route: RR 2015, Huzak 2018, GMV

Sources: [[rousseau-shan-zhu-2015-second-type-dulac-full.full]], [[huzak-cyclicity-degenerate-df2a.full]], [[grau-manosas-villadelprat-chebyshev-abelian-2008-arxiv.full]].

## Claim blocks

```claim
id: rr2015-i6b-boundary-cyclicity
statement: In the quadratic family, Roussarie–Rousseau 2015 proves finite cyclicity only for the boundary limit-periodic set arising after family blow-up of the graphics (I^1_6b), (H^3_13), and (DI_2b), not for the complete graphics.
hypotheses: planar quadratic vector fields; the named triple-nilpotent-at-infinity graphics surround a center; boundary limit-periodic set in the blown-up family; full parameter unfolding as specified by RR.
holds-here: yes
status: asserted
bearing: The slow-divergence/blow-up argument closes a boundary stratum but leaves the full displacement problem for I^1_6b open.
anchor: research/sources/rousseau-shan-zhu-2015-second-type-dulac-full.full.md
answers: slow-divergence-ect-missing-step
```

```claim
id: huzak2018-df2a-finite-cyclicity
statement: Huzak proves that the degenerate quadratic DRR graphic DF_{2a} (the b=0 center case of the DF_{1a} family) has finite cyclicity.
hypotheses: quadratic polynomial family; DF_{2a}, b=0; family blow-up; slow-fast geometric singular perturbation analysis and slow divergence integral.
holds-here: yes
status: asserted
bearing: This is a complete graphic-level closure for DF_{2a}, but its slow-fast mechanism does not automatically transfer to the triple-nilpotent-at-infinity I^1_6b displacement.
anchor: research/sources/huzak-cyclicity-degenerate-df2a.full.md
answers: slow-divergence-ect-missing-step
```

```claim
id: gmv2008-ect-criterion
statement: For analytic Abelian integrals I_i(h)=∮_{γ_h} f_i(x)g(y)dx over ovals of H=Φ(x)+Ψ(y), the balances B_{σ1}(f_i/Φ') and B_{σ2}(g_i), with g_0=g and g_{i+1}=g_i'/Ψ', form CT-systems and B_{σ2}(g_0)=o(y^{2m(n−2)}) imply that (I_0,…,I_{n−1}) is an ECT-system; in the form H=A(x)+B(x)y^{2m}, g=y^{2s−1}, it suffices that s>m(n−2) and the corresponding balances ℓ_i form a CT-system.
hypotheses: analytic functions; a period annulus of ovals; separated Hamiltonian H=Φ+Ψ (or H=A+B y^{2m}); stated involutions and balance conditions; for Theorem B, s>m(n−2).
holds-here: unchecked
status: proved
bearing: If the leading displacement/Melnikov function for a reduced I^1_6b subproblem can be represented in this Abelian-integral form and the balance hypotheses are verified, GMV gives a finite zero bound via ECT. It does not itself control the full nonlinear, parameter-uniform displacement map near the blown-up nonhyperbolic graphic.
anchor: research/sources/grau-manosas-villadelprat-chebyshev-abelian-2008-arxiv.full.md
answers: slow-divergence-ect-missing-step
```

## Exact missing step

The sources establish mechanisms only on reduced strata: RR uses family blow-up, Dulac transitions and displacement functions; its boundary result does not supply a finite zero bound for the full `(I^1_6b)` unfolding. Huzak closes a different degenerate graphic by slow-fast analysis. GMV applies to analytic Abelian integrals over Hamiltonian ovals, whereas the target displacement contains compositions of parameter-dependent Dulac/regular transition maps near a nonhyperbolic triple nilpotent point. The missing theorem is therefore a uniform reduction of the full blown-up displacement (including all parameter sectors and the center/integrable degeneration) to an Abelian/ECT-controlled function, with a proved remainder/contact-equivalence statement preserving a finite zero bound. Without that reduction, an ECT computation would establish only a first-order or restricted Melnikov result, not full finite cyclicity.
