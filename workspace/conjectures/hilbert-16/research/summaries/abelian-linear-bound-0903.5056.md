# Malev–Novikov 2009 — linear estimate for zeros of Abelian integrals (named family)

Full text: [[abelian-linear-bound-0903.5056.full]] (arXiv:0903.5056; published as
S. Malev, D. Novikov, "Linear estimate for the number of zeros of Abelian integrals",
Ann. Fac. Sci. Toulouse Math. 19 (2010) 97–110).

## What the source establishes (held full text, verbatim)

**Object:** the complete Abelian integral I(t) = ∮_{δ(t)} ω for the Hamiltonian
H(x,y) = x²y(1−x−y), δ(t) ⊂ {H = t} the compact ovals for t ∈ (0, 1/64), and ω a
polynomial 1-form of degree n.

**Theorem 1.1:** the number of isolated zeros of I(t) on (0, 1/64) does not exceed
**(7/4)n + 9**, where n = deg ω. This is an explicit answer to the Infinitesimal
Hilbert 16th problem for this particular family (case (rlv3) in the Gautier–Gavrilov–
Iliev list of integrable quadratic centers with elliptic trajectories).

**Theorem 1.2:** the number of limit cycles appearing in the non-conservative
perturbation (1/x)dH − εω = 0 and converging to a smooth cycle δ(t) as ε→0 does not
exceed **(1/4)(7n + 43)** (from Theorem 1.1 applied to xω, degree n+1).

**Method (the part this run reuses):** the Abelian integral is generated, as a ℂ[t]-
module, by **three basic Abelian integrals** J₁=I₀,₀, J₂=I₂,₀, J₃=I₃,₀ (Petrov-module
decomposition, Lemma 2.2); a Picard–Fuchs system is constructed (§3); the zero bound
comes from the fewnomials/Rolle technique on the Picard–Fuchs solutions (§4). The
paper also states the general context: BNY double-exponential bound; Petrov–Khovanskii
linear-in-degω bound with no coefficient information; the expectation that these
combine to linear-in-n and double-exponential-in-degH; Horozov–Iliev's linear bound
for generic cubic H via ellipticity + Riccati + fewnomials.

## What it lets this run conclude

- This is a **fully explicit, named-family sharp-type Abelian-integral count** — GOAL
  result-type 3, and the exact validation shape the run's
  `abelian-picard-fuchs-argument-principle-sharp-count` approach needs: the Petrov
  module rank (3), the Picard–Fuchs system, and the Rolle/fewnomial zero count are all
  written out, hence machine-checkable over Q (sympy + Wronskian/Sturm core).
- The linear-in-degω bound with explicit constant (7/4)n+9 is the sharpest published
  per-family bound of this shape; it is the concrete precedent for the run's claim
  that executed PF/Wronskian counts produce numbers.
- It is the companion to Binyamini–Dor's uniform linear-in-degω bound (that one for
  all H, existential constant; this one explicit for one named H).

```claim
id: h16-malev-novikov-2009-linear-abelian-rlv3
statement: Malev–Novikov (arXiv:0903.5056, Ann. Fac. Sci. Toulouse 19 (2010)): for H=x^2 y(1−x−y), ovals δ(t)⊂{H=t}, t∈(0,1/64), and deg ω = n, the complete Abelian integral I(t)=∮_{δ(t)}ω has at most (7/4)n+9 isolated zeros on (0,1/64) (Theorem 1.1); the non-conservative perturbation (1/x)dH−εω=0 produces at most (1/4)(7n+43) limit cycles converging to smooth cycles (Theorem 1.2). The proof: Petrov-module generation by three basic integrals J_1=I_{0,0}, J_2=I_{2,0}, J_3=I_{3,0}, an explicit Picard–Fuchs system, and a fewnomials/Rolle zero count.
hypotheses: H=x^2y(1−x−y); ovals in {x,y>0}, t∈(0,1/64); ω polynomial 1-form degree n; non-conservative (first-order) perturbation.
holds-here: yes — the explicit sharp-type per-family Abelian count (GOAL result-type 3) and the validation exemplar for the adopted sharp-count approach.
status: asserted
evidence: full text held at research/sources/abelian-linear-bound-0903.5056.full.md; Theorem 1.1 at lines 28-30, Theorem 1.2 at lines 42-46, method §§2-4.
falsifier: a degree-n ω with more than (7/4)n+9 zeros of I on (0,1/64), or an error in the Petrov-module/PF construction.
sources: https://arxiv.org/abs/0903.5056
anchor: research/sources/abelian-linear-bound-0903.5056.full.md
follows-from: h16-abelian-integral-bounds
answers:
```
