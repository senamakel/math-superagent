# The excess functional is orthogonal to switch density: a degree-spectrum dichotomy

```approach
idea: >
  Prove a sharp structural fact that reframes the parity barrier, then use it to
  settle GOAL priority 3 (the equivalence). Every fold cell is
  ε_d = ∏_{j∈M_d} u_j with |M_d| = 2^{pc(d)} an EVEN number of switch signs
  (d ≥ 2 forces pc(d) ≥ 1). Hence the excess functional
  S(n) = Σ_{d=2}^{n−1} ε_d is a sum of even-degree monomials in the switch
  signs u_j = χ(q_j)χ(q_{j+1}), and its first-order (Walsh/degree-1) mode is
  exactly zero: ⟨S(n), u_j⟩ = #{d : M_d = {j}} = 0 for every j. The fold is
  blind to the switch density D = Σ_j u_j itself — it reads only even-order
  (≥2) switch-sign correlations. This makes the dead reduction "SUPPLY reduces
  to positive switch density" provably lossy in a precise sense, and turns the
  question into a DICHOTOMY: (a) if the even-order correlations needed for
  E[S(n)²] = O(n) are equivalent in strength to the switch density, then
  SUPPLY ⟺ switch density (GOAL priority 5, proved as a theorem); (b) if they
  are strictly weaker, then a strictly weaker arithmetic input suffices
  (priority 4). The dichotomy is decided by the exact degree spectrum of S(n)²
  as a multilinear polynomial.
mechanism: >
  Named machinery: Fourier–Walsh expansion on the hypercube and the degree
  (Gowers U^d) filtration of multilinear polynomials. S(n)'s Walsh support is
  exactly the row-window set {M_d : d ∈ [2,n−1]}, and its degree-2^p level has
  weight #{d : pc(d) = p} (a Lucas count) — so S(n) is concentrated in even
  degrees ≥ 2, orthogonal to all odd modes including switch density. The
  degree-2 and degree-4 spectra of S(n)² are exact combinatorial counts, given
  by the meet formula |M_d △ M_{d'}| = 2^{pc(d)} + 2^{pc(d')} − 2^{pc(d∧d')+1}
  (claim downset-row-intersection-meet-formula). This is NOT the refuted
  gowers-u2-nilsequence-uniformity route (which tried to bound the FIRST moment
  by U² uniformity and hit a basis mismatch) and NOT haar-chaos-hypercontractive
  (a random-input moment inequality): it is an exact degree/orthogonality
  analysis of the deterministic polynomial S(n), used as a pricing tool, not a
  bound.
status: proposed
first-step: >
  tool_builder, exact arithmetic. (1) Prove-and-verify the evenness fact:
  |M_d| = 2^{pc(d)} for d ∈ [2,n−1] (one-line Lucas count), hence every monomial
  of S(n) has even degree ≥ 2; compute the first-order Walsh coefficients
  ⟨S(n), u_j⟩ = 0 and the constant term ⟨S(n), 1⟩ = 0 for n ≤ 200 against the
  brute submask-XOR oracle, with a negative control — a degree-1 statistic such
  as Σ_j u_j must have NONZERO first-order coefficients. (2) Compute the exact
  degree-2 and degree-4 Walsh spectra of S(n)² for n ≤ 64 (each coefficient is a
  count of (d,d') pairs with a given symmetric difference), and print which
  separations carry them. (3) State the dichotomy precisely and determine
  whether the degree-2 stratum (products u_a u_b at separation ≥ 2) is provably
  decorrelated by PNT-in-AP alone, or is the open adjacent-pair object in
  disguise. FALSIFIER: if a degree-1 term appears in S(n) (some |M_d| = 1), the
  evenness fact is false and the orthogonality claim dies; if the degree-2
  spectrum collapses to separation-1 switch signs, the bypass fails and
  priority 5 is the truth.
falsifies: >
  (a) some |M_d| = 1 for d ≥ 2 (then S(n) has a degree-1 term and switch density
  is NOT orthogonal to the fold); (b) the degree-2/4 spectrum of S(n)² is carried
  entirely by separation-1 switch signs (then the even-order correlations are the
  adjacent-pair object in disguise and priority 5 is the truth); (c) the degree
  spectrum fails to match the Lucas/meet count against the oracle (a bookkeeping
  defect in the linearisation).
```
