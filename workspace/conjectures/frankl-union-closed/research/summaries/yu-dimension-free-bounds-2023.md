# Dimension-Free Bounds for the Union-Closed Sets Conjecture

Lei Yu. arXiv:2212.00658 (Dec 2022; v2 5 May 2023); published in *Entropy*
25(5), 2023, doi:10.3390/e25050767. This is the strongest **published**
(machine-verified constant ≈ 0.38234) lower bound.
Full text (read): `research/sources/yu-dimension-free-bounds-2023.html.full.md`

<!-- source: https://arxiv.org/html/2212.00658v2 ; also https://arxiv.org/pdf/2212.00658 -->

## What it establishes (primary source, read)

Uses the entropy / coupling (Sawin-style, non-iid) method. The bound is stated
as an **optimization**: an element density `p_A ≥ t` is forced whenever
`Γ(t) > 1` (Theorem 1), where

```
Γ(t) := sup_{P_ρ} inf_{P_p: Eh(p)>0, Ep≤t} E_ρ [ inf_{P_pq ∈ C_s(P_p): ρ_m(p;q)≤ρ} E_{p,q}h(φ(ρ,p,q)) / Eh(p) ]
```

with `φ(ρ,p,q) = median{ max{p,q,p+q−z₂}, 1/2, min{p+q, p+q−z₁} }`,
`z₁ = pq−ρ√(p(1−p)q(1−q))`, `z₂ = pq+ρ√(p(1−p)q(1−q))`, `h` binary entropy.

The `ρ` (conditional maximal correlation) parameter is where Sawin's
improvement enters: `ρ=0` is the independent/Gilmer case, `ρ=1` arbitrary
couplings. Choosing `P_ρ=(1−α)δ₀+αδ₁` (mixture of independent and arbitrary
couplings) gives a computable lower bound **Proposition 1**:

```
Γ̂(t) = sup_{α∈[0,1]} inf_{symmetric P_pq: Eh(p)>0} g(P_pq,α)/Eh(p),
g(P_pq,α) = (1−α)E_{(p,q)~P_p^⊗2} h(p+q−pq) + α E_{(p,q)~P_pq} h(φ(1,p,q))
```

with `P_pq` of the form `(1−β)Q_{a1,a2}+βQ_{b1,b2}` (at most two symmetric
atoms) and `0 ≤ a=(a1+a2)/2 ≤ t < b=(b1+b2)/2 ≤ 1`, `β=0` or
`β=(t−a)/(b−a)>0`. This two-point structure is the finite-dimensional,
conditionally-iid coupling the attack-coupling work needs.

**Numerics (Yu):** `α=0.035, t=0.38234`, optimal `P_pq=(1−β)Q_{a,a}+βQ_{a,1}`
with `a≈0.3300622`, `β≈0.1560676`, gives `Γ̂(t) ≥ 1.00000889`, hence
`p_A ≥ 0.38234`. Cambie's more precise value (cited in Yu):
`0.382345533366702 ≤ t̂_max ≤ 0.382345533366703`, attained at
`α≈0.03560698136437784`.

## Why it matters for this run

This is the single number to beat in **print**: **0.38234**. It is the
computable, explicit form of Sawin's dependent-coupling improvement, and the
full optimization objective (not reconstructable from the abstract) is now in
the library. The barrier `(3−√5)/2 ≈ 0.38197` is only the iid-entropy case
(`ρ=0`); the dependent couplings (ρ>0 chosen via α) escape it.

```claim
id: yu-optimization-objective
statement: The Yu/Sawin entropy bound is the optimization Γ̂(t) =
  sup_α inf_{symmetric P_pq} [(1−α)E h(p+q−pq) + α E h(φ(1,p,q))]/Eh(p) over
  two-atom symmetric couplings P_pq=(1−β)Q_{a,a}+βQ_{a,1}; p_A ≥ t whenever
  Γ̂(t)>1.
hypotheses: F union-closed (OR-closed), |F|≥2, every element density ≤ t.
holds-here: true
status: proved
bearing: states the exact finite-dimensional conditionally-iid coupling
  optimization to implement; unblocks attack-coupling-half.
anchor: Yu arXiv:2212.00658, Theorem 1, Prop. 1, Corollary 1; full text in sources.
```

```claim
id: yu-record-0-38234
answers: daswu-record-0-3823455
statement: p_A ≥ 0.38234 for every union-closed family, via the (published,
  Entropy 2023) Yu bound; Cambie computed t̂_max = 0.382345533366703.
hypotheses: none beyond UCC.
holds-here: true
status: asserted
bearing: the published record to beat; (3−√5)/2 is only the iid case.
anchor: Yu arXiv:2212.00658, §1-2 numerical results; published Entropy 2023.
```
