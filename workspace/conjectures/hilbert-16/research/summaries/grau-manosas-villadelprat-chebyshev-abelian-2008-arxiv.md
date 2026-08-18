# Grau, Mañosas & Villadelprat, "A Chebyshev criterion for Abelian integrals" (TAMS, arXiv:0805.1140)

<!-- source: https://ar5iv.labs.arxiv.org/html/0805.1140 | converted from HTML. Full text pushed to research/notes/claims.md claim `h16-grau-manosas-villadelprat-chebyshev-2010`. [[grau-manosas-villadelprat-chebyshev-abelian-2008-arxiv.full]] -->

## What it establishes

A sufficient **Chebyshev criterion** for a collection of Abelian integrals to be an
**extended complete Chebyshev (ECT) system** — the instrument for sharp, explicit
zero counts of Abelian integrals (infinitesimal Hilbert 16 / Arnold). The
criterion reduces the hard analytic problem to **algebra**: verifying that certain
functions form a Chebyshev system, checkable by non-vanishing of Wronskians
computed via **resultants** and **Sturm's theorem**.

**Setup.** Near a period annulus of a center, Abelian integrals reduce to
`I_i(h) = ∫_{γ_h} f_i(x) g(y) dx` (i=0..n−1) over the oval `γ_h ⊂ {H=h}`,
`H = Φ(x) + Ψ(y)` separated variables (or `H = A(x) + B(x)y^{2m}`).

**Theorem A** (H=Φ+Ψ). `(I_0,…,I_{n−1})` is an ECT-system on (0,h₀) if the
"balances" `ℬ_σ1(f_i/Φ')` (with σ₁ the involution of Φ) form a CT-system on
(0,x_r), and `ℬ_σ2(g_i)` (σ₂ the involution of Ψ, `g_{i+1}=g'_i/Ψ'`) form a
CT-system on (0,y_r) with the o-order condition `ℬ_σ2(g₀)(y)=o(y^{2m(n−2)})`.

**Theorem B** (H=A(x)+B(x)y^{2m}, g=y^{2s−1}). `(I_0,…,I_{n−1})` is an
ECT-system on (0,h₀) if `s > m(n−2)` and the balances
`ℓ_i = ℬ_σ(f_i/(A'B^{(2s−1)/(2m)}))` form a CT-system on (0,x_r).

Since CT/ECT-property is checked on the Wronskians (Lemma 2.3: CT ⇔ continuous
Wronskians never vanish; T ⇔ discrete Wronskians never vanish on L^k), the whole
criterion is **algorithmic**: compute Wronskians as rational functions in
`(x, σ(x))`, eliminate σ via the involution relation `q(x,σ(x))=0`, take
resultants, and discharge non-vanishing on the interval by Sturm.

## Application — the run's key harvest

Applied to the **Gautier–Gavrilov–Iliev (2008)** program for the cyclicity of
period annuli of quadratic centers of genus one (26 open cases):

- reproves the GGI case **(r11)** (first integral
  `H = x²(x+3)/(6(x+1)³) + y²/(2(x+1)³)`) → period-annulus cyclicity **2**;
- **proves the GGI conjecture in four NEW cases: (r7-r14), (r15), (r17), (rlv3)**,
  each shown to have period-annulus cyclicity **2** under quadratic perturbations;
- case (r18) is noted as *not* solvable by this criterion (needs other methods).

Each case is closed by explicit rational first integral, explicit
`f_i, l_i`, explicit rational Wronskians, and a **Sturm argument that a polynomial's
Wronskians never vanish on the annulus interval** — every step algebraic and
Lean-certifiable (resultant + Sturm is exactly the kind of finite algebraic core GOAL
wants to push to a kernel-checked theorem).

## Hypotheses / holds here

Analytic (or smooth) integrand functions; separated-variable or
`A(x)+B(x)y^{2m}` Hamiltonians; period annulus about a center; first-order
(Melnikov) bifurcation. **Holds here: yes** — sharp Abelian-integral zero counts
for concrete quadratic centers is GOAL's "sharp zero-count in one named
Hamiltonian family" route, and the resultant+Sturm method is genuinely
Lean-statablycheckable. The GGI genus-one cases bear directly on the quadratic
(DRR) program's open native rows.

**Evidence class: sourced** (peer-reviewed Trans. AMS, full text held,
arXiv:0805.1140).

## Bearing / implication

- Gives the standard modern Chebyshev instrument (matches claim
  `h16-grau-manosas-villadelprat-chebyshev-2010`, whose "not held" note is now
  corrected — full text IS held).
- Proves period-annulus cyclicity 2 for five named quadratic centers of genus
  one — concrete, explicit, and fully algebraic (ideal target for a Lean
  statement + resultant/Sturm certificate).
- Reinforces the run's Chebyshev/Wronskian machinery from Gasull–Lázaro–
  Torregrosa and Mañosas–Villadelprat.
