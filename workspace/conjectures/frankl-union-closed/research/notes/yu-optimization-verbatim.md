# Yu's finite-dimensional optimization — verbatim from the source

Source: `research/sources/yu-dimension-free-bounds-2023.full.md`
(Yu, "Dimension-Free Bounds for the Union-Closed Sets Conjecture", Entropy 2023),
lines 37–166. Everything below is transcribed from that file, not re-derived.

## The objects

- `h(a) = −a·log₂(a) − (1−a)·log₂(1−a)`  (binary entropy, h(0)=h(1)=0 by convention).
- `φ(1,p,q) = median{ max{p,q}, 1/2, p+q }`  — the median of three numbers, treated as a
  multiset (so median{a,a,b}=a).  [This is eq (4), the ρ=1 value of φ.]

## The function g  [after eq (4), before Proposition 1]

```
g(P_pq, α) := (1−α) · E_{(p,q)∼P_p^{⊗2}} h(p+q−pq)
            + α  · E_{(p,q)∼P_pq}     h(φ(1,p,q))
```

where `P_p` is the marginal of the joint distribution `P_pq`, and `P_p^{⊗2}` is the
independent (product) coupling of two copies of the marginal.

## Proposition 1 (the finite-dimensional bound)  [eq (5)]

For t ∈ (0, 1/2):

```
Γ̂(t) := sup_{α∈[0,1]}  inf_{symmetric P_pq : E h(p) > 0}  g(P_pq, α) / E h(p)
```

where the infimum is over all distributions `P_pq` of the form

```
P_pq = (1−β)·Q_{a1,a2} + β·Q_{b1,b2}
```

with the **constraint set**

```
0 ≤ a := (a1+a2)/2 ≤ t < b := (b1+b2)/2 ≤ 1
β = 0   or   β = (t−a)/(b−a) > 0
E h(p) > 0
```

and

```
Q_{x,y} := (1/2)·δ_{(x,y)} + (1/2)·δ_{(y,x)}          [eq (7)]
```

(δ_{(x,y)} = Dirac at the point (x,y).)

## Dimension of the auxiliary variable

The auxiliary random variable is the pair `(p,q) ∈ [0,1]²` (2-dimensional), of which
`p` is the original auxiliary variable in Γ(t) eq (2) and `q` its coupled copy. In the
finite reduction the joint `P_pq` is an **extreme point** of the convex set of symmetric
couplings concentrated on B² with E p ≤ t; by Krein–Milman + Carathéodory these extreme
points are parameterized by **4 real parameters (a1,a2,b1,b2) plus the β determined by
the constraint**, so the finite optimization is over `(α, a1, a2, b1, b2)` — 5 continuous
parameters — with β a function of them.

## The reduction chain (Theorem 1 → Proposition 1 → Corollary 1)

- **Theorem 1:** if Γ(t) > 1 for some t ∈ (0,1/2), then p_A ≥ t for any OR-closed A ⊆ Ωⁿ.
  (p_A = max density; Γ(t) is the dimension-free object in eq (2).)
- **Proposition 1:** Γ(t) ≥ Γ̂(t)  (so Γ̂(t) > 1 implies Γ(t) > 1).
- **Corollary 1:** if Γ̂(t) > 1 for some t ∈ (0,1/2), then p_A ≥ t.
- **t̂_max := sup{ t ∈ (0,1/2) : Γ̂(t) > 1 }.**

## The 0.38234 evaluation to reproduce

> "if we set α = 0.035, t = 0.38234, then the optimal
> P_pq = (1−β)·Q_{a,a} + β·Q_{a,1}
> with a ≈ 0.3300622 and β ≈ 0.1560676 which leads to the lower bound
> Γ̂(t) ≥ 1.00000889. Hence, p_A ≥ 0.38234."

So the certified point is: α = 0.035, a1 = a2 = a = 0.3300622, b1 = a = 0.3300622,
b2 = 1 (i.e. Q_{a,1}), β = (t−a)/(b−a) ≈ 0.1560676. Check:
b = (a+1)/2 = 0.6650311; (t−a)/(b−a) = (0.38234−0.3300622)/(0.6650311−0.3300622)
= 0.0522778 / 0.3349689 ≈ 0.1560676 ✓.

## The precise question for the c=1/2 push

t̂_max = sup{ t ∈ (0,1/2) : Γ̂(t) > 1 }. Cambie (2022) computed
0.382345533366702 ≤ t̂_max ≤ 0.382345533366703 (attained at α ≈ 0.03560698136437784).
The task: evaluate Γ̂(t) for t increasing toward 1/2 and determine which happens:
**(a)** Γ̂(t) > 1 certifies H(A∨B) > H(A) at density t, driving toward 1/2; or
**(b)** Γ̂(t) crosses 1 at some t < 1/2, and the extremal P_pq achieving the inf is the
blocking μ. Realistically (b), with the blocking μ ≈ the α/a/β triple above.
