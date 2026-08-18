# Gautier–Gavrilov–Iliev, "Perturbations of quadratic centers of genus one"

**Source**: arXiv:0705.1609v2 (published: Discrete Contin. Dyn. Syst. 25(2):511–535, 2009).
Held full text: `research/sources/gautier-gavrilov-iliev-quadratic-centers-genus-one.arxiv.full.md`
(URL: https://arxiv.org/pdf/0705.1609).
Claim: `h16-ggi-quadratic-centers-genus-one-2009`.

## What it establishes

A program for the cyclicity of **period annuli of quadratic systems with
centers of genus one** (generic level sets elliptic curves):

- **Classification**: Theorem 1 — phase curves of (1.1) are genus one iff a
  stated condition; Theorem 2 + Propositions 1–3 classify the **reversible**
  (2.1) and **generic Lotka–Volterra** genus-one families, with explicit normal
  forms (e.g. `(lv1) H = x²y³(1−x−y)`).
- **Essential perturbations**: for each genus-one center class, the essential
  **one-parameter quadratic perturbations** producing the maximal number of
  limit cycles are determined, and the associated
  **Poincaré–Pontryagin–Melnikov functions** (whose zeros control the number
  of limit cycles) are computed.
- **Conjecture 1** (r-classes): cyclicity under small quadratic perturbations is
  **three** for the reversible cases (r1) with a\*<a<4, (r3) 7/3<a<4, (r4)
  4<a<5, (r5) a=4, (r6) a>4, (r10), and **two otherwise**.
- **Conjecture 2** (LV-classes): three in (rlv1) (the Hamiltonian triangle), two
  otherwise.
- **Theorem 3**: the exact upper bound of the number of limit cycles produced by
  the period annulus under quadratic perturbations of the reversible system
  **(r18)** or **(r11)** is **two** — an established sharp count in the exact
  shape the adopted approach wants to re-run.
- **Theorem 4**: the three-dimensional space of Abelian integrals
  `J(t) = I′(t)`, `t ∈ [−⅙, 0)`, is **Chebyshev** — each `J(t)` has **at most
  two zeros** (counted with multiplicity) on `[−⅙, 0)`.
- **Proposition 4**: the Picard–Fuchs system is of dimension 3 in cases
  (r1),(r3)–(r4) with b=−⅓,(r6) with b=2,(r9),(r11)–(r12),(r17)–(r18), and of
  dimension 4 in the remaining cases.

## Why it matters for this run

This is the **exact prior art for the adopted sharp-Abelian approach**
(`abelian-picard-fuchs-argument-principle-sharp-count`): a named class of
quadratic centers (genus one, reversible and Lotka–Volterra) whose period-
annulus cyclicity is fully determined (Theorems 3–4, conjectures 1–2). The
explicit Melnikov functions, the Picard–Fuchs dimensions, and the Chebyshev
zero-bounds give the **validation targets** the approach's first step names: a
published sharp count whose algebraic core (generators over the Picard–Fuchs
module, Wronskian/Chebyshev chain) is written out explicitly and hence
machine-checkable. The GMV 2010/2011 Chebyshev criterion (held) §4.1 explicitly
applies to the GGI program, so the three sources close the instrument loop:
GGI computes the Melnikov functions and bounds, GMV gives the general
criterion, Novikov–Yakovenko (held this cycle) gives the Picard–Fuchs structure
theorem, and Gavrilov 1999 (held this cycle) gives the module freeness for the
semiweighted-homogeneous Hamiltonian case.

**Boundary**: the theorems are for quadratic perturbations of the specific
reversible genus-one systems; the conjectures cover the full r-class. For the
strategy: (r11)/(r18) are the *established* sharp cases to rebuild and verify
first; the conjectural classes are where a clean-room re-derivation could
either graduate a conjecture to a theorem or find a counterexample — either is
a result.