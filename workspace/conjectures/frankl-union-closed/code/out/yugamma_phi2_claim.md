# Yu/Sawin Γ̂(t): exact value at t = 1/2 is φ/2

**Status: exact value of the collapsed extremal PROVED (symbolic algebra);
that it is the global sup Γ̂(1/2) corroborated (numerical + monotonicity).**

<!-- regenerator-trigger -->

## The object

Yu's finite-dimensional relaxation (Entropy 2023, Prop 1):

```
Γ̂(t) := sup_{α∈[0,1]}  inf_{symmetric P_pq ∈ F_t}  g(P_pq,α)/E h(p)
```

with the two-atom symmetric coupling family

```
P_pq = (1−β)·Q_{a1,a2} + β·Q_{b1,b2},  Q_{x,y} = ½δ_{(x,y)} + ½δ_{(y,x)}
a = (a1+a2)/2 ≤ t < b = (b1+b2)/2 ≤ 1,  β = (t−a)/(b−a)
g = (1−α)·E_{P^⊗2} h(p+q−pq) + α·E_{P_pq} h(φ(1,p,q))
```

`Γ̂(t) > 1` is Yu's sufficient certificate that some element has density ≥ t
(theorem 1 + Prop 1). Cambie found 0.3823455333667 is t̂_max = sup{t : Γ̂(t) > 1}.

## The finding

At t = 1/2 the extremal coupling collapses (scan `commands.log`): the α* → 0
branch with a₁ = a₂ = (3−√5)/2, b₂ = 1, b₁ = a. The α = 0 value is **exactly φ/2**.

**Proof (exact algebra).** Take a = (3−√5)/2, so a² − 3a + 1 = 0, i.e. 2a − a² = 1 − a.
Coupling: P = (1−β)Q_{a,a} + βQ_{a,1}, t = 1/2, b = (1+a)/2.

- β = (t−a)/(b−a) = (½−a)/((1−a)/2) = (1−2a)/(1−a). With a=(3−√5)/2 this gives
  β = a exactly (1−2a = √5−2 = a(1−a)). ✓ (checked to 1e-14)
- marginal P_p atoms: p = a with weight w₁ = (1−β) + β/2 = 1 − β/2; p = 1 with
  weight w₂ = β/2 (and h(1) = 0).
- E h(p) = w₁·h(a).
- E_{P^⊗2} h(p+q−pq): a term vanishes when either coordinate is 1 (p+q−pq = 1,
  h(1)=0). Only the (a,a) product survives: w₁²·h(2a−a²) = w₁²·h(1−a) = w₁²·h(a).
- α = 0 ratio = w₁²·h(a) / (w₁·h(a)) = w₁ = 1 − β/2 = 1 − a/2.

Since a = (3−√5)/2, a/2 = (3−√5)/4, so

```
Γ̂(1/2)  =  1 − a/2  =  1 − (3−√5)/4  =  (1+√5)/4  =  φ/2  =  cos 36°  ≈ 0.8090169944
```

Independently: `yugamma_highprec.py` gives 60-digit diff exactly 0.0;
`yugamma_confirm.py` numeric inf over the full 4-parameter family at t=1/2 is
0.809016994375 at α=0, and is *larger* there than at any α>0 (α=0.05 → 0.801,
α=0.1 → 0.770, α=0.2 → 0.688), so sup_α = φ/2 at α=0. The scan (`commands.log`
line 2372) reads `0.500000  0.80901699  alpha*=0.0000  (0.381966…)`.

## Why it matters — the barrier with a number on it

- **Γ̂(t) is non-increasing in t** (proved by set-inclusion F_t ⊆ F_{t′}; in
  `yu_optimization_verbatim.md`).
- Γ̂(1/2) = φ/2 = 0.809 < 1. So the Yu/Sawin finite-dimensional coupling
  **certifies nothing at density 1/2**, and its certificate value AT 1/2 is the
  clean number φ/2, not some scan artifact.
- More: Γ̂(1/2) = φ/2 ≈ 0.809 is the same constant as the **iid-OR barrier**
  family — (3−√5)/2 — since the collapsed extremal has a = (3−√5)/2. At t = 1/2
  the optimal coupling degenerates to the pure independent coupling on the
  (3−√5)/2 atom, i.e. **the dependent relaxation offers no entropy gain at 1/2
  beyond the iid class**, and its gap to certification (>1) is 1 − φ/2 ≈ 0.19.

## Evidence class

- **Proved (exact algebra):** the α=0 collapsed coupling value at t=1/2 equals φ/2.
- **Corroborated (numeric + monotonicity):** that this is the sup Γ̂(1/2) (i.e. no
  α>0 coupling beats φ/2) — full-4-param SLSQP inf grid, matched to ~1e-14; and
  the scan's alpha*=0 line. This is *not* a theorem; the full-4-param inf is a
  numerical search.
- **Independent direct-search check of the α=0 full-4-param inf
  (`code/out/alpha0_inf_scan.py`):** at α=0 the objective is exactly the iid-OR
  ratio of the marginal, `E_{P^⊗2}h(p+q−pq)/E h(p)`. A 400-start SLSQP over the
  full (a1,a2,b1,b2) feasible class finds inf = 0.8090169943749473, matching
  φ/2 to 1e-16, with mpmath 50-digit value 0.80901699437494755 (diff from φ/2
  ≈ 9.9e-17) at the boundary a1=a2=(3−√5)/2, b1=b2=1. A targeted grid agrees
  (0.80901699457, same achiever). This rules out my doubt that an *admissible*
  marginal could approach the unconstrained iid-OR barrier (3−√5)/2=0.382: the
  feasibility constraint a=(a1+a2)/2 ≤ t=1/2 < b forces the ratio up to φ/2.
  Still numerical (SLSQP locations + 50-digit evaluation), so the global inf
  remains a numeric corroboration, not a theorem — consistent with the claim's
  status.
- **Consistent:** monotonicity Γ̂ non-increasing + scan values 1.134 @ 0.30 → 1.005
  @ 0.38 → 0.809 @ 0.5.

## Falsifiers and what would break it

- A coupling at t=1/2, α>0, with g/Eh(P) > φ/2 would refute the "global sup"
  part. Numeric search found none (α=0.05..0.20 all give infs < φ/2). A symbolic
  inf over the full 4-parameter family at t=1/2 remains open (numerical only).
- The exact φ/2 value of the collapsed coupling cannot be broken — it is proven
  algebra, and reproduces to 60 digits.

## Files

- `code/out/yugamma_structure.py` (first incorrect marginal — superseded)
- `code/out/yugamma_highprec.py` — 60-digit diff = 0.0
- `code/out/yugamma_confirm.py` — exact derivation + full-4-param numeric inf
- `code/out/yugamma_collapse.py` — scan corroboration across t
- scan data: `code/out/commands.log` (t=0.454..0.500 collapse; 0.500 → 0.80901699)

```claim
id: yu-gamma-half-is-phi-over-2
statement: The collapsed alpha=0 extremal of Yu's Gamma_hat(t) at t=1/2, on the coupling P_pq = (1-beta)Q_{a,a} + beta Q_{a,1} with a=(3-sqrt5)/2 and beta=a, has value g/Eh(p) = 1 - a/2 = (1+sqrt5)/4 = phi/2 = cos(36deg). Proved by exact algebra: 2a-a^2 = 1-a collapses the numerator to w1^2 h(a), denominator w1 h(a), ratio w1 = 1 - beta/2 = 1 - a/2, since beta(t=1/2)=a. 60-digit mpmath diff = 0.0 from phi/2. The exact value is proven; that it is the global sup Gamma_hat(1/2) is corroborated numerically (full-4-param SLSQP inf 0.80901699 at alpha=0; alpha>0 gives smaller infs) and by Gamma_hat non-increasing in t.
hypotheses: Yu Prop 1 two-atom symmetric coupling, alpha=0 branch, t=1/2, a=(3-sqrt5)/2
holds-here: yes
status: proved (exact algebra) for the collapsed value; numerical/scan corroboration that it is the sup Gamma_hat(1/2)
bearing: the Yu/Sawin finite-dimensional relaxation certifies nothing at density 1/2, and its certificate value AT 1/2 is exactly phi/2 = 0.809, not 1 -- a quantitative barrier statement, consistent with Gamma_hat(1/2)<1 and Gamma_hat non-increasing in t. The collapsed extremal's a=(3-sqrt5)/2 ties it to the iid-OR barrier constant.
anchor: code/out/yugamma_phi2_claim.md (yugamma_highprec.py, yugamma_confirm.py, commands.log)
answers: coupling-half (partial: the Yu/Sawin relaxation at 1/2 has value phi/2<1, not a certificate; secure upper barrier statement)
```
