# Lei Yu, "Dimension-Free Bounds for the Union-Closed Sets Conjecture" — Entropy 25(5), 2023 (arXiv:2212.00658v2)

**Note — replaces the structural digest.** Wikilink to full text:
[[yu-dimension-free-bounds-2023.html.full]]

Full text: `research/sources/yu-dimension-free-bounds-2023.html.full.md`.
Published in *Entropy* 25(5):767 (2023), open access, doi:10.3390/e25050767.

## What it establishes (precise statements)

The union-closed/OR-closed conjecture: every nonempty OR-closed `A ⊆ Ωⁿ`
(`A` closed under coordinatewise OR, equivalent to union-closed `ℱ` of subsets
of an `n`-set) has an element with marginal density `p_A ≥ 1/2`. Yu reduces
UC to a single dimension-free optimization.

**Setting.** For a symmetric coupling `P_{XY}` of `(P_X, P_X)` (i.e.
`P_{XY}(x,y)=P_{XY}(y,x)`), `ρ_m(X;Y)` = maximal (Hirschfeld–Gebelein–Rényi)
correlation. For `p,q,ρ ∈ [0,1]` define tail function `φ(ρ,p,q)` =
`median{max{p,q,p+q−z₂}, 1/2, min{p+q, p+q−z₁}}` with
`z₁=pq−ρ√(p(1−p)q(1−q))`, `z₂=pq+ρ√(…·…)`. Then `φ(0,p,q)=p+q−pq`
(the OR density of two independent bits) and
`φ(1,p,q)=median{max{p,q},1/2,p+q}`.

**Theorem 1.** Defining (eq. 2, in the note)
`Γ(t) := sup_{P_ρ} inf_{P_p: Eh(p)>0, Ep≤t} E_ρ[ inf_{P_pq∈C_s(P_p): ρ_m(p;q)≤ρ} (E h(φ(ρ,p,q)) / E h(p)) ]`,
we have: if `Γ(t) > 1` for some `t∈(0,1/2)`, then `p_A ≥ t` for every OR-closed
`A ⊆ Ωⁿ`, **for all `n`** (dimension-free). Contrapositive route is Gilmer's:
`H(Unif A) = log|A|`, every symmetric coupling `Z=X∨Y ∈ A` a.s. so
`sup_{P_{XY}∈C_s} H(Z)/H(X) ≤ 1`; if every marginal `≤t` then this forces
`Γ_n(t) ≤ 1`. `Γ(t)` lower-bounds `Γ_n(t)` for all `n`.

**Proposition 1 (computable bound) — the actual optimization.** Choosing
`P_ρ = (1−α)δ₀ + αδ₁` gives
`Γ(t) ≥ Γ̂(t) := sup_{α∈[0,1]} inf_{symmetric P_pq: Eh(p)>0} g(P_pq,α)/Eh(p)`
with `g := (1−α)E_{P_p⊗2} h(p+q−pq) + α E_{P_pq} h(φ(1,p,q))`.
**Cardinality bound (the exact form the attack must implement):** in the outer
infimum it suffices to take `P_pq = (1−β)Q_{a₁,a₂} + βQ_{b₁,b₂}`, a 2-atom
symmetric coupling, with `0 ≤ a=(a₁+a₂)/2 ≤ t < b=(b₁+b₂)/2 ≤ 1` and either
`β=0` or `β=(t−a)/(b−a)`; `Q_{x,y} = ½δ_{(x,y)} + ½δ_{(y,x)}`.

**Corollary 1.** If `Γ̂(t) > 1` then `p_A ≥ t`. Hence
`p_A ≥ t̂_max := sup{t∈(0,1/2): Γ̂(t)>1}`.

**Numerical record.** With `α=0.035`, `t=0.38234`, optimal
`P_pq=(1−β)Q_{a,a}+βQ_{a,1}`, `a≈0.3300622`, `β≈0.1560676` gives
`Γ̂(t) ≥ 1.00000889`. **So `p_A ≥ 0.38234`, the current published record.**
Cambie (arXiv:2212.12500, preprint) computed the tight bounds
`0.382345533366702 ≤ t̂_max ≤ 0.382345533366703`, attained near
`α≈0.03560698136437784` — so the true value of Yu's `Γ̂` optimisation is
`t̂_max ≈ 0.3823455333667`, and `0.38234` is a safe published lower bound.

## Hypotheses and holds-here

- `A` OR-closed, finite, `|A|≥2`; element densities are exact marginals
  `p_A := (1/|A|)Σ_{S∈A} 1_{i∈S}`. **Holds-here: yes** — this is precisely the
  union-closed families of this problem.
- The chain-rule split `H(Xⁿ)=Σ H(Xᵢ|Xⁱ⁻¹)` and the symmetric-coupling
  relaxation are the whole proof; the only gap for an eventual `1/2` is that
  `Γ̂(t) < 1` numerically well below `t=1/2` (the record `t̂_max ≈ 0.38235`).
  **What is asserted, not proved:** the numerical evaluation of the 2-atom
  optimum (floating-point); Cambie's 10⁻¹⁵-error bounds; the claim that no
  other `P_pq` shape beats `(1−β)Q_{a,a}+βQ_{a,1}` at the optimum. **What is
  proved:** the reduction `Γ̂(t)>1 ⟹ p_A≥t` and the 2-atom cardinality
  reduction.

## What this lets the run do

- **Implements the exact attack object.** `G-coupling-half` needs precisely
  `Γ̂(t)` from Proposition 1: a 4-parameter (`a,b,β,α` or `a₁,a₂,b₁,b₂,β,α`)
  finite-dimensional optimisation. Reproducing `t̂_max=0.3823455333667` (or the
  safer `0.38234` at `Γ̂≥1.00000889`) is the stated correctness check for
  attack-coupling, before any attempt to push `t` toward `1/2`.
- The 2-atom form `(1−β)Q_{a,a}+βQ_{a,1}` at the optimum (where the intended
  `Q_{a,a}` term is the iid self-coupling and `Q_{a,1}` aligns one coordinate)
  is the concrete extremal against which to test the conjecture that the class
  optimum falls short of `1/2`.

## What it does not settle

Does not settle whether `Γ̂(t)` reaches `1/2` (numerically it is `≈0.38235`,
strictly below); by Corollary 1, exceeding `1/2` in `Γ̂` would *be* UC for this
coupling class, but the class is capped well below by the computation. There is
no closed-form expression for `Γ̂`; only the numeric record.

```claim
id: yu-record-0-38234
statement: The finite-dimensional (dimension-free, 2-atom symmetric-coupling)
  optimization Γ̂(t) of Yu satisfies Γ̂(0.38234) ≥ 1.00000889 (attained by
  P_pq=(1−β)Q_{a,a}+βQ_{a,1}, a≈0.3300622, β≈0.1560676, α=0.035), hence
  p_A ≥ 0.38234 for every union-closed family (current published record).
hypotheses: A union-closed/OR-closed, finite, |A|≥2; densities = uniform-exact marginals
holds-here: yes
status: proved (the reduction Γ̂>1 ⟹ p_A≥t and the 2-atom cardinality reduction
  are proved in-paper; the 0.38234 value rests on a floating-point evaluation)
bearing: the attack object for G-coupling-half is exactly this Γ̂ optimization;
  reproducing 0.38234 (or Cambie's t̂_max=0.3823455333667) is the correctness
  check, and the 2-atom extremal form is the test case for whether the class
  optimum is capped below 1/2
anchor: research/sources/yu-dimension-free-bounds-2023.html.full.md
contradicts: nothing (resolves the record vs the (3−√5)/2 iid barrier — see thread)
follows-from: yu-theorem1, yu-proposition1
answers: exact-current-published-c8b8
```

```claim
id: yu-theorem1
statement: If Γ(t) > 1 for some t∈(0,1/2), then p_A ≥ t for every OR-closed
  A⊆Ωⁿ, for all n simultaneously (dimension-free reduction of UC to a coupling
  entropy inequality at the level of element marginal densities).
hypotheses: A finite, OR-closed, |A|≥2; Γ over symmetric couplings of (P_X,P_X),
  P_X any distribution on [0,1] with Eh(p)>0
holds-here: yes
status: proved
bearing: the single analytical gap of the entropy-coupling attack; Γ and Γ̂ are
  the finite-dimensional forms the run optimizes
anchor: research/sources/yu-dimension-free-bounds-2023.html.full.md
follows-from: (Gilmer's reduction, generalised to dependent couplings)
```

```claim
id: yu-proposition1
statement: The distribution family over which Γ(t) is optimized can be
  restricted, for a computable bound, to 2-atom symmetric couplings
  P_pq=(1−β)Q_{a₁,a₂}+βQ_{b₁,b₂} with 0≤a≤t<b≤1 and β=0 or β=(t−a)/(b−a),
  giving Γ(t)≥Γ̂(t); Γ̂(t)>1 ⟹ p_A≥t (Corollary 1).
hypotheses: same as yu-theorem1; P_ρ=(1−α)δ₀+αδ₁
holds-here: yes
status: proved
bearing: makes the gap finite-dimensional: the attack optimises finitely many
  reals rather than distributions
anchor: research/sources/yu-dimension-free-bounds-2023.html.full.md
follows-from: yu-theorem1
```
