# H. R. Gallegos-Ruiz, N. Katsipis, Sz. Tengely, M. Ulas, "On the Diophantine equation C(n,k) = C(m,l) + d" (J. Number Theory 208 (2020) 1-28; arXiv:1904.11369)

Source: https://arxiv.org/abs/1904.11369 ; full text:
`research/sources/gallega-ruiz-katsipis-tengely-ulas-binommld-2019.full.md`

## What it is

The current systematic treatment of the **binomial near-collision equation**
C(n,k) = C(m,l) + d, with -3 ≤ d ≤ 3 and the nine "small" index pairs
(2,3),(2,4),(2,5),(2,6),(2,8),(3,4),(3,6),(4,6),(4,8). It completely solves
each case by finding all integral points on the attached elliptic/hyperelliptic
curves (Magma IntegralPoints/IntegralQuarticPoints, elliptic logarithm method
of Stroeker–Tzanakis, Baker bounds + LLL reduction + Mordell-Weil sieve). It is
the natural extension of Blokhuis–Brouwer–de Weger 2017 (d=1) and
Katsipis 2019.

## The reference list of ALL known solutions of C(n,k)=C(m,l)

(2 ≤ k ≤ n/2, 2 ≤ l ≤ m/2, k < l; the paper's Table 1 / intro list):

    3003:  C(78,2) = C(15,5) = C(14,6)   (triple)
    120:   C(16,2) = C(10,3)
    210:   C(21,2) = C(10,4)
    1540:  C(56,2) = C(22,3)
    7140:  C(120,2) = C(36,3)
    11628: C(153,2) = C(19,5)
    24310: C(221,2) = C(17,8)
    infinite:  C(F_{2i+2}F_{2i+3}, F_{2i}F_{2i+3}) =
               C(F_{2i+2}F_{2i+3}-1, F_{2i}F_{2i+3}+1)  (i = 1,2,...; Lind 1968,
               Singmaster 1975)

This matches the run's witness ledger exactly (3003 with N=8 counting mirrors;
the six N=6 values 120,210,1540,7140,11628,24310; the infinite Fibonacci family
=n=F_{2j+2}F_{2j+3}-1, k=F_{2j}F_{2j+3}-1 up to re-indexing). So the paper is
an independent 2019 primary confirmation of the library's witness frame.

## Solved status of equation (1) C(n,k)=C(m,l) per pair

- (2,3): Avanesov 1966 (all solutions).
- (2,4): de Weger 1996 and Pintér 1995 independently.
- (3,4): reduces to Y(Y+1)=X(X+1)(X+2), solved by Mordell 1963.
- (2,6),(2,8),(3,6),(4,6),(4,8): Stroeker–de Weger 1999, linear forms in
  elliptic logarithms.
- (2,5): BMSST 2008 (genus-2 hyperelliptic, Baker + Mordell-Weil sieve, full
  integral point list).
- (2,p) p odd prime: finite (Kiss 1988); k=2, l≥3 finite via Baker (Brindza
  1991).

## The new results (this paper)

- **Thm 1** ((2,4) congruence obstruction): if 3 is a quadratic non-residue mod
  p and ν_p(12d+1) is odd, C(n,2)=C(m,4)+d is unsolvable mod p, hence has no
  integer solutions; explicit d ≡ 7,12,... (mod 75) unsolvable.
- **Thm 2** (k=l): all solutions of C(n,k)=C(m,k)+d with k∈{3,4,5}, d∈{1..20},
  d≠0: a short list (e.g. (k,d,sol) = (3,3,(4,3)), (4,4,(5,4)), (5,5,(6,5)),...);
  method: C(n,k)-C(m,k) = d·k! factors as (n-m)·F(n,m).
- **Thm 3** (elliptic cases): complete solutions of C(n,k)=C(m,l)+d for
  -3≤d≤3 and (k,l) = (2,3),(2,4),(2,6),(2,8),(3,4),(3,6),(4,6),(4,8) — full
  tables given (e.g. (2,3): d=3 → (75,368),(77,383),(421726,158118758);
  d=1 → the 8 known; d=0 → the known 5). The (3,6) d=2 case is a rank-3
  elliptic curve with a full elliptic-logarithm resolution (Baker bound
  M ≤ 6.64×10^86, LLL-reduced to M≤10).
- **Thm 4** (genus-2 case (2,5)): complete solutions for -3≤d≤3; e.g. d=3 →
  C(31,2)=C(11,5)+3, C(94,2)=C(16,5)+3, C(346888,2)=C(375,5)+3,
  C(356263,2)=C(379,5)+3 (genus-2, Jacobian rank 6, log|x| ≤ 1.028×10^612,
  reduced to ‖n‖ ≤ 13.8, 1500-digit precision, 3h23m parallel enumeration).
  Also: rank of Jac(C_d) computed for d∈[-50,50] (Table 8; rank up to 7);
  d=66=C(12,2) has rank 8; parametric families of solutions for
  C(n,2)=C(m,5)+C(w,2) with x=15(2w-1)², 15(2w-1)²+4.
- **Thm 5** (polynomial near-collisions): C(f₁(x),k)+C(x,2)=C(f₂(x),2) with
  deg f₁=2, deg f₂=k has exactly 3 solutions for k=3,5; 1 for k=7; none for
  k∈{9,11,13,15,17,19} (Gröbner-basis classification).

## Conjecture (for context)

For each N there is d_N with the same-column difference equation
C(n,3)-C(m,3)=d_N having at least N positive solutions (numerics: d=2180 has 3
solutions; d ∈ {10053736, 209920964, 1928818640} each have 4). This is the
difference analogue of the multiplicity question — same-column multiplicity of
a *fixed difference*, not of a fixed value.

## Relevance to Singmaster

The d=0 column of Thm 3/Thm 4 gives, independently of any other source, the
complete known-solutions list and the per-pair solved status. It is also the
practical "what do effective methods actually compute" documentation: every
case is per-(k,l) (and per-d), with bounds growing astronomically in the curve's
rank/heights — the concrete form of the ineffectivity wall.

## Claims

```claim
id: grktu-known-solutions-list
statement: Gallegos-Ruiz-Katsipis-Tengely-Ulas 2020 (JNT 208, arXiv:1904.11369,
  held): the complete list of known solutions of C(n,k)=C(m,l) (2<=k<=n/2,
  2<=l<=m/2, k<l) is 3003=C(78,2)=C(15,5)=C(14,6); 120=C(16,2)=C(10,3);
  210=C(21,2)=C(10,4); 1540=C(56,2)=C(22,3); 7140=C(120,2)=C(36,3);
  11628=C(153,2)=C(19,5); 24310=C(221,2)=C(17,8); and the infinite family
  C(F_{2i+2}F_{2i+3}, F_{2i}F_{2i+3}) = C(F_{2i+2}F_{2i+3}-1,
  F_{2i}F_{2i+3}+1) for i>=1 (Lind 1968, Singmaster 1975). Per-pair solved:
  (2,3) Avanesov; (2,4) de Weger/Pinter; (3,4) Mordell; (2,6),(2,8),(3,6),
  (4,6),(4,8) Stroeker-de Weger; (2,5) BMSST 2008; (2,p) p odd prime Kiss;
  k=2, l>=3 finite via Baker (Brindza).
hypotheses: k<l, k<=n/2, l<=m/2 (half-triangle convention); "known" = proved
  complete for the solved pairs listed, conjecturally complete overall.
holds-here: yes — matches the run's witness ledger exactly (3003 N=8, the six
  N=6 values, the infinite family).
status: asserted (quoted from the arXiv full text)
bearing: independent 2019 primary confirmation of the entire witness frame and
  the per-pair solved status of the effective-methods toolbox.
anchor: research/sources/gallega-ruiz-katsipis-tengely-ulas-binommld-2019.full.md
```

```claim
id: grktu-near-collision-complete
statement: GRKTU 2020 solves C(n,k)=C(m,l)+d completely for -3<=d<=3 and
  (k,l) in {(2,3),(2,4),(2,5),(2,6),(2,8),(3,4),(3,6),(4,6),(4,8)}, with full
  tables; also C(n,k)=C(m,k)+d for k in {3,4,5}, d in {1..20}; also the
  polynomial near-collision equation C(f1(x),k)+C(x,2)=C(f2(x),2) (deg f1=2,
  deg f2=k) has 3 solutions for k=3,5, one for k=7, none for odd k=9..19.
  Methods: elliptic logarithms (Stroeker-Tzanakis), Baker bounds, LLL
  reduction, Mordell-Weil sieve, Magma; bounds like log|x| <= 1.028*10^612
  reduced to coefficient search bound 13.8.
hypotheses: fixed (k,l), fixed small d; integral points on the attached
  elliptic/hyperelliptic curves.
holds-here: yes (d=0 column is equation (1) itself; the near-collision
  extensions are the same curves with a parameter shift).
status: asserted (quoted from the arXiv full text)
bearing: documents concretely what effective integral-point machinery achieves
  per fixed pair: complete solution lists with astronomically large but
  reducible bounds — the exact shape of the per-pair (non-uniform) effective
  toolbox the run's approach must either use or beat.
anchor: research/sources/gallega-ruiz-katsipis-tengely-ulas-binommld-2019.full.md
```