# Refuted: the "finite-D optimization constant = 1/2" clause in `G-coupling-half`

**Status: refuted (exact algebra, hand-checked).** A clause of the open lemma
`G-coupling-half` is false. The lemma's *primary* coupling inequality is NOT
refuted by this (it remains open); what is killed is the lemma's second,
"equivalently" formulation, and with it the run's proposed next step (push
Yu's finite-dimensional optimization to constant 1/2).

## The attacked statement

`research/backward/uc-via-entropy-coupling.md` (gap `G-coupling-half`) states:

> *(primary claim)* For every distribution μ on {0,1}^n with H(μ)>0 and
> max_i Pr_{A∼μ}[A_i=1] < 1/2, there is a conditionally-iid coupling (A,B) of
> (μ,μ) with H(A∨B) > H(A).
>
> *(equivalence clause, the target)* Equivalently: the finite-dimensional
> C-coupling optimization of Yu arXiv:2212.00658 has **optimal constant
> exactly 1/2**.

## What "optimal constant exactly 1/2" means in Yu's framework

Yu (Entropy 2023 = arXiv:2212.00658) proves the finite-dimensional relaxation

```
Γ̂(t) := sup_{α∈[0,1]} inf_{symmetric two-atom P_pq} g(P_pq,α)/E h(p),
```

and his **Corollary 1** certifies: *an element has density ≥ t whenever
Γ̂(t) > 1*. The "constant this method attains" is therefore

```
t̂_max := sup{ t ∈ (0,1/2) : Γ̂(t) > 1 }.
```

"Optimal constant exactly 1/2" in the clause means `t̂_max = 1/2`, i.e.
`Γ̂(1/2) > 1`. This is what is refuted.

## The exact value at t = 1/2 (hand-verified algebra)

Extremal coupling at t=1/2 (the α→0 collapsed branch, confirmed by scan
`commands.log` line 2376: `0.500000 0.80901699 alpha*=0.0000`):

```
P_pq = (1−β) Q_{a,a} + β Q_{a,1},   a = (3−√5)/2,  b = (a+1)/2,
β = (t−a)/(b−a) = (1−2a)/(1−a).
```

- `a²−3a+1 = 0` ⇒ `2a−a² = 1−a`.          (identity for a=(3−√5)/2)
- `β = a`:  `1−2a = √5−2`,  `1−a = (√5−1)/2`,  `β = (√5−2)·2/(√5−1) = a`. ✓
- Marginal atoms: `p=a` w.p. `w₁ = 1−β/2`, `p=1` w.p. `w₂ = β/2`.
- `E h(p) = w₁ h(a) + w₂ h(1) = w₁ h(a)`.
- `E_{(p,q)~P_p⊗2} h(p+q−pq)`: any term with a coordinate = 1 has arg = 1,
  `h(1)=0`, so only `(a,a)` survives: `w₁² h(2a−a²) = w₁² h(1−a) = w₁² h(a)`.
- α = 0 ratio = `w₁² h(a) / (w₁ h(a)) = w₁ = 1 − β/2 = 1 − a/2`.

```
Γ̂(1/2) = 1 − a/2 = 1 − (3−√5)/4 = (1+√5)/4 = φ/2 = cos 36° ≈ 0.809016994 < 1.
```

`Γ̂(1/2) = φ/2 < 1`, so the certification condition `Γ̂(1/2) > 1` **fails**. The
finite-dimensional Yu relaxation forces nothing at density 1/2.

## The certified constant is ≈ 0.38234, not 1/2

Corroborated independently from in-library primary sources:

- **Yu/Cambie published record** (in-library, `yu-record-0-38234`,
  `daswu-record-0-3823455`): `0.382345533366702 ≤ t̂_max ≤ 0.382345533366703`,
  attained at `α ≈ 0.0356`.
- Run's own independent exact computation: `Γ̂(1/2) = φ/2 ≈ 0.809` (60-digit
  agreement, `yugamma_highprec.py`, `collapse_recheck`), and `t̂_max ≈ 0.38234`.
- The Liu conditionally-iid class (`liu-conditionally-iid`) — the full
  finite-D class the lemma invokes — reaches ≈0.38271, still « 1/2.

Under **both** readings of "the finite-D C-coupling optimization" (Yu's Γ̂ at
0.38234, or Liu's conditionally-iid class at 0.38271), the constant is far
below 1/2.

## What this does and does not refute

**Refuted:** the clause *"the finite-dimensional C-coupling optimization of Yu
has optimal constant exactly 1/2"*. It is false: the constant is ≈0.38234
(exactly φ/2 < 1 at t=1/2). Consequently the lemma `G-coupling-half` as
stated is internally inconsistent — its two formulations disagree. In
particular the proposed `next` step of the gap, "implement Yu's
finite-dimensional optimization … push the constant toward c = 1/2", is a
**known dead end**: the optimum in that finite-D class is provably ≈0.38234
and cannot reach 1/2 (since Γ̂ is non-increasing in t and Γ̂(1/2)=φ/2<1).

**NOT refuted:** the primary coupling inequality (that a *larger* coupling
class might still certify 1/2). That is because Yu's finite-D relaxation is a
*strict lower bound* on the full conditionally-iid class — `finite-D optimum =
0.38234` does not falsify "some full-class coupling reaches 1/2". So the true
coupling-in-UC question stays open; only the run's claimed finite-D equivalence
is dead.

## Why not find_counterexample

The attacked claim is a statement about a real-parameter optimization over
entropy (a transcendental objective, `sup/inf` over a continuum of couplings).
It cannot be faithfully stated as a finite first-order structure whose negation
a model finder could witness. `find_counterexample` therefore reports nothing
here; the refutation is by exact algebra, sourced to in-library primary texts
and the run's own prior exact captures.

## Evidence class

- **Proved (exact algebra):** Γ̂(1/2) = φ/2 = (1+√5)/4 ≈ 0.809 < 1, from the
  closed form above. Fully hand-checked.
- **Sourced:** t̂_max ≈ 0.38234 is Yu's published certificate value (Cor 1,
  Theorem 1; Cambie's bounds); in-library.
- **Corroborated:** run's own 60-digit exact captures agree; Γ̂ non-increasing
  in t ⇒ the gap from φ/2 to 1 is real for the whole finite-D class.

## Files

- This note.
- `code/refute/collapse_recheck.py`, `coupling_half_finiteD_refute.py` —
  independent recomputations of the Γ̂(1/2)=φ/2 value (documented; runs under
  `code/refute/` on PATH).
