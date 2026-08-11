# An Explicit Solution to the Chessboard Pebbling Problem — Zhen & Knessl, arXiv:1009.5731

<!-- source: https://arxiv.org/pdf/1009.5731 ; abstract page https://arxiv.org/abs/1009.5731 -->
<!-- published context: after CGMO (1995) and Knessl (2008, Math. Comput. Modelling 47, 127-139) -->

## Question answered

Exact enumeration of the 2D chessboard pebbling number G(k) (number of
reachable configurations with k pebbles) and the two-parameter sequence
G(k, m) (starting configuration sitting in level L(m+1)). This is the 2D
amoeba count: G(k) = OEIS A007902(k+1).

## The recurrence it both uses and re-derives (CGMO's, as in [3])

With level sets L(l) = {(i,j): i+j = l}, the number of reachable configs
G(k,m) (starting with m+1 level set doubly full as described in the paper)
satisfies the exact recurrence (this is the same G(k,m) as OEIS A007902, Alois
P. Heinz):

```
G(k, 0) = 2*G(k-1, 0) + G(k, 1) + δ(k,2)                       (2.1)
G(k, 1) = G(k-3, 0) + 2*G(k-2, 1) + G(k-1, 2) + G(k-4, 1)     (2.2)
G(k, m) = G(k-m-2, m-1) + 2*G(k-m-1, m) + G(k-m, m+1),  m>=2  (2.3)
```
with G(k) = G(k,0) for k>=2, δ the Kronecker delta. Boundary condition (2.1)
can be replaced by (2.4): G(k,0) = 2^(k-2) + Σ_{l=1}^{k} 2^(k-l) G(l,1).

## Exact (contour-integral) formula — Theorem 2.1

G(k,m) = (1/2πi) ∮_C (−1)^m z^{m−k−1} V_m(z) dz, where C is a closed CCW
contour around the origin with |z| < 1/2 on C, and
```
V_m(z) = z^{1+m(m+1)/2}/S(z) · Σ_{n>=1} (−1)^{n+m} z^{n(n+1)/2+nm}
         · ∏_{L=0}^{m} 1/(1 − z^{L+n}) · ∏_{L=1}^{n-1} 1/(1−z^L)^2
S(z) = (2z²−3z+2)S_1(z) − (4z²−4z+1)S_2(z) + 2z² − z − 1
S_k(z) = Σ_{i>=1} (−1)^{i+1} z^{i²/2+(2k−1)i/2} ∏_{j=1}^{i} 1/(1−z^j)^2
```
**Corollary 2.1**: G(k) = 2^{k−2} + (1/2πi)∮_C (2^k − z^{−k})/(1 − 2z) V_1(z) dz.

## Asymptotics — Theorem 2.2 / Corollary 2.2

There is a unique root z_* < 1/2 of S(z)=0, z_* ≈ 0.43072 95931 37930…,
with a = 1/z_* ≈ 2.321642199494… the 2D growth rate. As k→∞,
G(k) ~ C·(1/z_*)^k with C = c* ≈ 0.12268707… (the constant on OEIS A007902
as c·d^n). Regimes for G(k,m): (i) k→∞, m=O(1); (ii) k,m→∞ with 2k/m² > 1;
(iii) k,m→∞ with l = k − m(m+5)/2 = O(1).

Corrections: the constant c1 ≈ 2.02740 20474 68498 and c1K* ≈ 0.28777 77049
35052 correct earlier 15-digit claims of [7] to only ~5 digits.

## Bearing on this run (3D PE763)

This paper is the *2D* solution set — it hands us the exact 2D structural
recurrence (the G(k,m) that OEIS uses) and the exact/enumerative 2D machinery,
but it is specific to dimension 2 (2 children per split, level sets L(l) of
size l+1). It does NOT contain the 3D version. The structural generalisation to
higher dimension is Eriksson's folded-polyominoid theory (see
research/L2.0/pebbling_ejc_survey.md), which is the right ladder to the 3D
count. The 3D D(N) (1,1,3,9,30,99,336,…) is a reachable-position count in the
3D process, exactly the object of the 3D analogue; this note only gives the 2D
precedent that the same class of recurrence/generating-function machinery can
be (and was) made exact.

## Sources
- Zhen & Knessl, arXiv:1009.5731 (PDF). https://arxiv.org/pdf/1009.5731
- Knessl, "On the number of reachable configurations for the chessboard
  pebbling problem", Math. Comput. Modelling 47 (2008) 127-139
  (doi 10.1016/j.mcm.2007.02.010).
- Chung, Graham, Morrison, Odlyzko, AMM 102 (1995) 113-123.
