# Primary treatments used in the local reference set

## Scope
The target is H16.2: uniform finiteness of isolated periodic orbits of planar polynomial vector fields. The relevant object is the displacement/return-map germ near a limit-periodic set.

## Source-backed claim blocks

### Panazzolo–Rousseau framework
**Source:** Belotto da Silva–Espín Buendía, *Topological Classification of Limit Periodic Sets of Polynomial Planar Vector Fields*, arXiv:1702.04965v1, https://arxiv.org/abs/1702.04965 (local full text: `research/sources/primary-panazzolo-rousseau-limit-periodic-sets-v1.full.md`).
**Claim:** A limit-periodic set in a polynomial family is a Hausdorff limit of limit cycles under parameter convergence. Its compactification is one of a singular point, periodic orbit, polycycle, or degenerate limit cycle; the DRR quadratic program is described as a 121-case analysis based on limit-periodic sets.
**Evidence:** primary-source text, lines 1–70. **Status:** asserted-by-source. **Falsifier:** a primary correction showing the definition/classification or DRR count is inapplicable to the polynomial family under consideration.

### Elementary polycycle cyclicity
**Source:** Kaloshin, *The Hilbert 16-th Problem and an Estimate for Cyclicity of an Elementary Polycycle*, arXiv:math/0010174, https://arxiv.org/abs/math/0010174 (local full text: `research/sources/primary-ilyashenko-yakovenko-elementary-polycycles-2000.full.md`).
**Claim:** The existential H16 asks for a uniform H(n); the individual Dulac problem and uniform existential problem differ. After compactification, the obstruction is uniform cyclicity of polycycles. Kaloshin treats elementary polycycles in generic finite-parameter families and provides explicit estimates.
**Evidence:** primary-source introduction, lines 1–40. **Status:** asserted-by-source. **Falsifier:** a theorem whose hypotheses omit elementary/nondegeneracy or genericity and still gives the claimed uniform bound.

### Tangential/Abelian instrument
**Source:** Binyamini–Novikov–Yakovenko, *On the Number of Zeros of Abelian Integrals*, arXiv:0808.2952, https://arxiv.org/abs/0808.2952, DOI https://doi.org/10.1007/s00222-010-0244-0 (local full text: `research/sources/primary-binyamini-novikov-yakovenko-abelian-integrals-2010.full.md`).
**Claim:** For nonsingular energy-level ovals of a polynomial Hamiltonian under a small nonconservative polynomial perturbation, the number of generated cycles is bounded by an explicit double-exponential function of field degree. The proof uses the Gauss–Manin connection, regular flat meromorphic systems, and quasiunipotent monodromy. This is tangential H16, not full H16.2.
**Evidence:** abstract and §1, lines 1–45. **Status:** asserted-by-source. **Falsifier:** a source showing the result applies to arbitrary polynomial families rather than first-order Hamiltonian perturbations.

### Bautin local quadratic result
**Source:** Bautin, *On the number of limit cycles which appear with variation of the coefficients from an equilibrium state of focus or center type*, Mat. Sb. 30 (1952), local full text `research/sources/bautin-1952-full.pdf.full.md`, URL https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&paperid=5421&what=fullt&option_lang=eng.
**Claim:** In the quadratic family, the maximum local cyclicity of a focus/center is 3; the paper explicitly constructs a quadratic system with 3 limit cycles.
**Evidence:** translated primary text, lines 1–25. **Status:** asserted-by-source; local algebraic certificates are separately present in `code/lean/Lib/BautinRecurrence.lean`. **Falsifier:** a verified quadratic example with 4 small-amplitude cycles at one focus or a proof that Bautin's coefficient family differs from the stated quadratic family.

### Cubic local lower bound
**Source:** Torregrosa, *Cubic planar vector fields with high local cyclicity*, São Paulo J. Math. 2024, local full text `research/sources/torregrosa-cubic-high-local-cyclicity-2024.full.md`, URL recorded in source header.
**Claim:** Two one-parameter cubic families exhibit twelve small-amplitude cycles for exceptional parameter values. This supersedes any attempt whose target is merely a twelfth cubic local cycle.
**Status:** asserted-by-source. **Falsifier:** a correction/retraction or failure of the construction's hypotheses.

## Local availability
The source directory contains primary/full-text treatments of compactified limit-periodic sets; elementary polycycles; Écalle/Ilyashenko analytic finiteness; DRR and successor quadratic graphics; Bautin ideals; Abelian integrals/Picard–Fuchs systems; Dulac/transition maps; slow–fast Liénard constructions; and current lower-bound/critique papers. Navigation reports: `research/ROOT.md`, `research/REFERENCE-SET-REPORT.md`, and `research/LIBRARY-STATUS.md`.
