# Yu's finite-dimensional optimization — verbatim (for implementation)

Source: Lei Yu, "Dimension-Free Bounds for the Union-Closed Sets Conjecture",
Entropy 2023, 25(5), doi:10.3390/e25050767 = arXiv:2212.00658.
Full text: `research/sources/yu-dimension-free-bounds-2023.full.md` (lines 71–132).
This is the note the operator directive required BEFORE any code: the objective,
the constraint set, and the dimension of the auxiliary variable, transcribed
verbatim from the source.

`h` is binary entropy (base does not matter; ratios are base-free).

## Theorem 1 (the master bound)

If `Γ(t) > 1` for some `t ∈ (0, 1/2)`, then `p_A ≥ t` for any OR-closed
(union-closed) family. Equivalently `p_A ≥ t_max` where
`t_max := sup{ t ∈ (0,1/2) : Γ(t) > 1 }`.

## The computable bound — Proposition 1

```
Γ(t) ≥ Γ̂(t) := sup_{α∈[0,1]} inf_{symmetric P_pq : Eh(p)>0}  g(P_pq, α) / E h(p)
```

where the infimum runs over all symmetric distributions `P_pq` of the form

```
P_pq = (1−β) Q_{a1,a2} + β Q_{b1,b2}
```

with

```
0 ≤ a := (a1+a2)/2 ≤ t < b := (b1+b2)/2 ≤ 1
```

and `β = 0` or `β = (t−a)/(b−a) > 0`, such that `E h(p) > 0`. Here

```
Q_{x,y} := 1/2 δ_{(x,y)} + 1/2 δ_{(y,x)}
```

and `δ_(x,y)` is the Dirac measure at `(x,y)`. `P_p` is the p-marginal of `P_pq`.

The objective is

```
g(P_pq, α) := (1−α) E_{(p,q)~P_p⊗2} h(p+q−pq)
            +  α  E_{(p,q)~P_pq}   h(φ(1,p,q))
```

with

```
φ(0,p,q) = p+q−pq
φ(1,p,q) = median{ max{p,q}, 1/2, p+q }
```

## Corollary 1

If `Γ̂(t) > 1` for some `t ∈ (0,1/2)`, then `p_A ≥ t` for any OR-closed `A`.
So the constant this method certifies is

```
t̂_max := sup{ t ∈ (0,1/2) : Γ̂(t) > 1 }
```

## The numbers (Yu's evaluation, verbatim)

"if we set `α = 0.035, t = 0.38234`, then the optimal
`P_pq = (1−β) Q_{a,a} + β Q_{a,1}` with `a ≈ 0.3300622` and `β ≈ 0.1560676`
which leads to the lower bound `Γ̂(t) ≥ 1.00000889`. Hence `p_A ≥ 0.38234`."

Cambie's sharper value (quoted in Yu):
`0.382345533366702 ≤ t̂_max ≤ 0.382345533366703`, attained at
`α ≈ 0.03560698136437784`.

## Auxiliary variable's dimension

The auxiliary variable in the coupling is `ρ` (conditional maximal
correlation), and Yu chooses its law `P_ρ = (1−α)δ_0 + α δ_1`. So the
"dimension of the auxiliary variable" is 1 (the scalar `ρ ∈ {0,1}` mixed by
`α`); the finite-dimensional parameter set to optimize is `(α, a, β)` with
`β` tied to `(t, a,b)` by `β=(t−a)/(b−a)` and `E[p]=t`.

## Closed-form reduction for the optimal two-point case

For the specific `P_pq = (1−β)Q_{a,a} + β Q_{a,1}` (so `a1=a2=a`, `b1=a,b2=1`:
`a=a`, `b=(a+1)/2`, `β=2(t−a)/(1−a)`), the marginal is `P_p: p=a` w.p.
`1−β/2`, `p=1` w.p. `β/2`. Then, since `h(1)=h(0)=0`:

- `E h(p) = (1−β/2) h(a)`
- `E_{(p,q)~P_p⊗2} h(p+q−pq) = (1−β/2)² h(2a−a²)`
- `E_{(p,q)~P_pq} h(φ(1,p,q)) = (1−β) h(median{a, 1/2, 2a})`

so

```
R(α,a;t) := g/Eh(p)
  = [ (1−α)(1−β/2)² h(2a−a²) + α(1−β) h(median{a,1/2,2a}) ] / [ (1−β/2) h(a) ],
    β = 2(t−a)/(1−a).
```

At `a≈0.33` we have `median{a,1/2,2a}=1/2`, so the second numerator term is
`α(1−β)·1`. This is a 2-variable scalar optimization in `(α,a)` once `t` is
fixed; `t_max` is the largest `t` with `sup_{α,a} R > 1`.

**Correctness check to reproduce:** at `α=0.035, t=0.38234, a=0.3300622,
β=0.1560676`, the closed form must give `R ≈ 1.00000889`.
