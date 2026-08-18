# I^1_6b: boundary/full displacement and ECT status

## Precise source-backed hypotheses

**Roussarie–Rousseau, _Finite cyclicity of some center graphics through a nilpotent point inside quadratic systems_, Memoirs AMS 2015, DOI [10.1090/mosc/248](https://doi.org/10.1090/mosc/248).** The paper works in the quadratic family after the weighted family blow-up
\[(x,y,\nu)=(r\bar x,r^2\bar y,r\rho),\quad r>0,\]
with invariant leaves \(r\rho=\nu\), and studies the rescaled family
\[
\dot{\bar x}=\bar y+a\bar x^2+\bar\mu_2,\qquad
\dot{\bar y}=\bar\mu_1+\bar\mu_3\bar y+\bar x\bar y.
\]
Theorem 1.1 states: for each of \(I^1_{14},I^1_{6b},H^3_{13},DI_{2b}\), the **boundary** limit-periodic set obtained in the blow-up has finite cyclicity. This is a local statement for the boundary stratum, not the full graphic.

The same source states that the full \(I^1_{6b}\) result was not proved. Some non-boundary limit-periodic sets involve four second-type Dulac maps; the center problem becomes a system of two equations in \((r_1,\rho_1,r_2,\rho_2)\), subject to \(r_1\rho_1=\nu_1\), \(r_2\rho_2=\nu_2\), rather than one scalar displacement equation. The authors explicitly defer these cases. Thus the exact full-displacement hypotheses currently available are: quadratic family, the above blow-up chart/foliation, and the relevant non-boundary stratum; **no theorem supplying the four endpoint germs is stated there**.

For comparison, their first-type theorem assumes a C^k normal form
\[
\dot r=r,\quad\dot\rho=-\rho,\quad\dot{\tilde y}_i=G(r,\rho,\tilde y_i),
\]
with the displayed irrational/rational-resonant forms of \(G\), compensator \(\omega(x,\alpha)=(x^{-\alpha}-1)/\alpha\) (or \(-\log x\)), and a remainder of property J. This theorem is **not** a theorem for second-type maps: the paper explicitly says only first-type maps are needed in that work.

**Huzak, _Finite cyclicity of the degenerate graphic DF_{2a}_, Comm. Pure Appl. Anal. 17 (2018), 1305–1316, DOI [10.3934/cpaa.2018.17.1305](https://doi.org/10.3934/cpaa.2018.17.1305).** The abstract identifies the hypotheses as the different quadratic graphic DF_{2a}, treated by geometric singular perturbation theory, family blow-up, slow divergence integral, and slow-fast systems. This is a precedent for the mechanism only; it does not identify DF_{2a}'s slow manifold, transition maps, or integral with the four-second-type \(I^1_{6b}\) problem.

## Does a four-second-type sum admit an ECT reduction?

No source-backed result was found. **Grau–Manosas–Villadelprat, _A Chebyshev criterion for Abelian integrals_, JDE 2008/2010, DOI [10.1016/j.jde.2009.07.014](https://doi.org/10.1016/j.jde.2009.07.014), Theorem A** applies to a specified finite family
\[
I_i(h)=\oint_{\gamma_h}f_i(x)g(y)\,dx
\]
over ovals of a separated Hamiltonian \(H=\Phi(x)+\Psi(y)\). It requires the two balance-function tuples to be CT-systems and the endpoint condition \(\mathcal B_{\sigma_2}(g_0)(y)=o(y^{2m(n-2)})\). These hypotheses are not supplied for the complete \(I^1_{6b}\) displacement, which is a nonlinear composition/two-equation problem involving four second-type endpoint maps, not a first-order Abelian-integral family.

Therefore an ECT reduction would require a new theorem proving: (i) a common parameter-uniform analytic/quasianalytic expansion for all four second-type maps and their regular transitions; (ii) contact/zero-count equivalence of the resulting two-equation system with a *specified finite-dimensional* ECT family; and (iii) uniform CT/Wronskian nonvanishing, including the vanishing slow-divergence strata and section transversality. None is in the primary sources checked.

## Falsifiers

This verdict is falsified by a primary source that either (a) proves full finite cyclicity of \(I^1_{6b}\) and states the four-map normal forms/remainder hypotheses, or (b) explicitly represents the full four-map displacement/two-equation center problem as a finite Abelian-integral ECT system and verifies the GMV balance hypotheses uniformly. Huzak DF_{2a} alone is not such a source.

## Evidence class

Boundary finiteness: asserted-by-source (primary paper, theorem stated; not independently formalized). Full \(I^1_{6b}\) ECT reduction: blocker / not established. Search was run against the primary RR paper, Huzak's primary article, GMV's primary criterion, and current literature queries; no qualifying source was found.