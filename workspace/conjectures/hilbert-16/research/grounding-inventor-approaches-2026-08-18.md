# Grounding report: inventor's three approaches (2026-08-18)

The three candidate files were updated with fenced `approach` blocks and the derived approach ledger was regenerated.

## 1. spectral-determinant-hill-operator — refuted

**Name in the literature:** Hill determinant/Hill formula and Floquet discriminant theory. Bolotin–Treschev, DOI https://doi.org/10.1070/rm2010v065n02abeh004671, relates a monodromy determinant to a Hessian determinant for periodic trajectories in continuous/discrete Lagrangian systems. Kuchment, DOI https://doi.org/10.1090/bull/1528, states the standard Hill operator/Floquet facts: analytic fundamental solutions, monodromy matrix, discriminant, and band relation.

**Precise usable theorem:** under the Lagrangian hypotheses and the relevant nondegeneracy/reduction assumptions, Hill's formula relates `det(P-rho I)` to a suitably defined Hill determinant; for a fixed periodic coefficient, the Floquet discriminant is analytic in the spectral parameter. This is a theorem about stability/degeneracy of an already-existing periodic trajectory.

**Applicability:** fails for the proposed full problem. A general planar polynomial vector field is not Lagrangian, and no source identifies zeros in an auxiliary spectral parameter with zeros of the nonlinear Poincare displacement. No uniform degree-dependent growth estimate over all cycles was found. The proposed global trace-formula step is unsupported.

**What it buys:** on a restricted Lagrangian/Hamiltonian family, a stability or degeneracy diagnostic; not a global H16.2 bound. Literature precedent: the two Hill sources above; claims `h16-drr-121-graphics`, `h16-dulac-finiteness-theorem`.

## 2. elimination-displacement-taylor-ideal — narrowed

**Name in the literature:** Bautin ideal, Bautin index, Taylor domination, and reduced Bautin depth—not generic finite-jet determinacy.

**Precise theorem:** for an analytic family `f_lambda(z)=sum a_k(lambda) z^k` satisfying the A-family/A0-series hypotheses and with finitely generated Bautin ideal of index `d`, Batenkov–Yomdin (https://doi.org/10.48550/arxiv.1411.7629, Theorem 4.1) gives Taylor domination by the first `d` generators, hence local zero control. Yomdin (https://doi.org/10.5565/publmat_extra14_25) gives the corresponding local uniform-zero framework, with additional growth hypotheses needed for stronger disk-wide control. García (https://doi.org/10.1090/proc/12896, Theorem 5) states that for a monodromic singularity with reduced Bautin depth `kappa`, `Cyc(X_lambda,p0) <= kappa-1`; his computable criterion additionally assumes the radicality, variety equality, and integral-closure stabilization conditions described in Theorem 6.

**Applicability:** holds locally for analytic monodromic focus/center families and selected nilpotent/degenerate centers. It does not automatically hold at a regular transversal for a nonhyperbolic DRR graphic: a common analytic parameter domain and uniform radius are precisely what fail as passages approach the polycycle. No theorem was found converting the open four-Dulac displacements into finite polynomial jet elimination.

**What it buys:** a legitimate local, potentially Lean-checkable cyclicity bound after proving a common analytic chart and Bautin stabilization. It is narrowed, not a full-H16 route. Supporting claims: `h16-bny-abelian-bound`, `g-lean-cert-kernel-checked`; Yakovenko survey/source https://doi.org/10.48550/arxiv.math/0104140.

## 3. tropical-discriminant-bkk-cyclicity — refuted

**Name in the literature:** Bernstein–Kushnirenko–Khovanskii (BKK) mixed-volume root bound, often combined with averaging; tropical discriminants do not automatically count components of arbitrary semialgebraic sets.

**Precise theorem:** for a specified square system of Laurent polynomials with Newton polytopes `Delta_i`, the number of isolated solutions in `(C*)^n`, counted with multiplicity, is bounded by the mixed-volume BKK bound; equality holds under BKK nondegeneracy/genericity. Huang–Wang (https://doi.org/10.48550/arxiv.2205.14450) applies this after averaging to special zero-Hopf systems, with bounds such as `H_1(n,m) <= (m-1)m^(n-2)` and `H_k(n,m) <= (km)^(n-1)` under its stated generic homogeneous hypotheses.

**Applicability:** the open DRR displacement has not been shown to be a finite Laurent-polynomial system, and the set of parameters with at least `N` cycles has not been given a defining system with controlled supports. BKK counts isolated roots, not connected components of an arbitrary semialgebraic `Sigma_N`; the proposed reduction is the missing theorem. Ilyashenko (https://doi.org/10.1090/bull/2002-39-03) and claim `h16-bny-abelian-bound` show fewnomial/Abelian methods in the tangential problem, not full nonlinear H16.2.

**What it buys:** explicit bounds for restricted averaged, near-Hamiltonian, or Abelian-integral families once the finite polynomial reduction and nondegeneracy are proved. It does not presently attack full H16.2.
