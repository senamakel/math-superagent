<!-- source: https://arxiv.org/pdf/math/9804035 | converted from PDF -->

arXiv:math/9804035v1  [math.CV]  7 Apr 1998ON THE RIEMANN-HILBERT PROBLEMS

G. Giorgadze
Institute of Cybernetics
Georgian Academy of Sciences
e-mail: giorgadze@rmi.acnet.ge

Abstract

We discuss some topological aspects of the Riemann-Hilbert trans-
mission problem and Riemann-Hilbert monodromy problem on Rie-
mann surfaces. In particular, we describe the construction of a holo-
morphic vector bundle starting from the given representation of the
fundamental group and investigate the local behaviour of connex-
ions on this bundle. We give formulæ for the partial indices of the
Riemann-Hilbert transmission problem in the three-dimensional case
in terms of the correspoding vector bundle on the Riemann sphere.

Introduction

The problem which we below call Riemann-Hilbert transmission problem
(RHTP) consists in ﬁnding piecewise holomorphic matrix functions which
satisfy certain transmission condition on the unit circle. It was ﬁrst formu-
lated by B. Riemann as an auxiliary proposition for solving the following
problem: starting with the given m points on the Riemann sphere CP
1 and
m nondegenerate matrices, one has to construct a system of ordinary dif-
ferential equations (ODE’s) for which the given points are poles of the ﬁrst
kind, and matrices are monodromy matrices around the given points. Such
systems are called Fuchsian and this problem is called the Riemann-Hilbert
monodromy problem (RHMP). Riemann himself did not give a detailed so-
lution. A valuable contribution to solving Riemann’s problem was made by
D. Hilbert. He solved the problem in certain particular case and stated an

1

analogous problem for the system of ODE’s which later became known as
the Hilbert’s 21-st problem.
Plemelj in the paper “Riemannsche Funktionenscharen mit gegebenen
Monodromiegruppe” solved a weak version of Hilberts’s 21-st problem. He
proved existence of a system of ODE’s which has the prescribed monodromy,
but also has a higher order pole. A system of this kind is called a regular
system. Plemelj used a diﬀerent method than Hilbert. He made use of a
Cauchy type integral for solving the transmission problem. Besides that,
he brought a regular system to Fuchsian type by certain tranformation and
therefore gave a seemingly complete solution of RHMP.
However his proof was not completely rigorous, as was indicated by many
authors: [Mus], [V], [Kohn], [Ar-Il], [An-Bl]; this refers to RHTP as well as
to RHMP.
In subsequent years, research of the RHTP and RHMP was going indepe-
dently. RHTP was developed by the Georgian mathematical school and re-
sults of this research were presented in the monographies of N. Muskhelishvili
[Mus] and N. Vekua [V]. Further results were obtained by W. Koppelman
[Kop], F. Gachov [Gah], Yu. Rodin [Rod], G. Khimshiashvili [Kh] and so on.
The history of the RHMP is even more interesing. It was Lappo-Dani-
levski˘i [LD] who was able to construct a Fuchsian system via its monodromy
group. Although Plemelj’s proposition on the reduction of a regular system to
Fuchsian system was not true in general, Lappo-Danilevski˘i’s result remains
true because he considered the particular case when the monodromy matrices
are close to the identity matrix.
V. Golubeva, A. Bolibruch, V. Leksin considered RHMP on n-dimensional
complex manifolds. They obtained many interesing results [Gol], [Lek1],
[Lek2] and their algebraic topological approach turned out to be useful for
the investigation of the monodromy representation of braid groups, Knizhnik-
Zamolodchikov and Yang-Baxter equations [Lek2], [Kohno]. Eventually,
A. Bolibruch proved that Plemelj’s result is not true, i. e. the answer on
the Hilbert’s question on the existence of a Fuchsian system with prescribed
monodromy group is negative.
More detailed historical information may be found in the books [Mus],
[V], [Gah], [An-Bl]. In the sequel we will freely refer to these books.
The author became interested in these problems, because in last 20 years,
they found applications in mathematical physics, in particular, in holonomic
ﬁeld theory [S-M-J], two dimensional Yang-Mills theory [At-Bot] and topo-

2

logical quantum ﬁeld theory [Wi].
The moduli space of holomorphic vector bundles on the Riemann surface
traditionally plays important role in complex analysis. Recently it also be-
came crucial for topological quantum ﬁeld theory. It turned out that for its
description the language of loop groups is quite adequate, which represents
a generalization of ideas by Birkhoﬀ and Bojarski to the case of a Riemann
surface of higher genus.
The holomorphic structure for a bundle on the Riemann sphere is deter-
mined completely by the partial indices of the corresponding matrix function.
These are obtained via Birkhoﬀ factorization of invertible matrix functions.
The condition of stability of a matrix function and the corresponding notion
of stability for vector bundles are expressible in the language of partial in-
dices developed by B. Bojarski and I. Gohberg with M. Krein. B. Bojarski
also explored the topology of stable matrix functions. The diagonal matrix
entering in the Birkhoﬀ factorization of a matrix function represents a co-
cycle which deﬁnes a holomorpic vector bundle on CP
1. This bundle has
connexions with regular singularities. The space of Fuchsian connexions is
contained in the space of connexions with regular singularities. A. Bolibruch
discovered that for every conformal structure on the marked Riemann sphere
there exists a bundle which has no Fuchsian connexion. He also explored the
solution in a neighbourhood of a regular singularity by Levelt’s theory and
transition from local solution to global solutions. Due to this, the descrip-
tion of the moduli space of the holomorphic vector bundles on a Riemann
surface of higher genus became possible in terms of local numeric invariants
of ODE’s. Our paper is devoted to the same topic and written in the same
spirit.
This text emerged from a talk given by the author at Prof. Bojarski’s
seminar in the Institute of Mathematics of the Polish Academy of Sciences.
During discussions with Prof. B. Bojarski several new ideas appeared which
will be considered in future publications.
I am very grateful to Prof. B. Bojarski and the Banach Centre for the
invitation and warm hospitality.
 3

1 Riemann-Hilbert transmission problem

Let U + be a bounded domain in the extended complex plane CP1 = C1 ∪
∞, with the boundary L, U − – the complementary domain, so that L =
U + ⋂ U −, CP
1 = U + ⋃ L ⋃ U −. For convenience of notation assume 0 ∈ U +

and L is a piecewise smooth Jordan curve.
Let ϕ(t) be a given function on L, bounded everywhere on L with the
possible exception of a ﬁnite number of points s1, s2,...,sm, where it satisﬁes
the H¨older condition |ϕ(t)| ≤ C
|t − sj|α ,

for any sj, j = 1, 2, ..., m. The numbers C, α are positive constants and α < 1.
Consider the Cauchy type integral

Φ(z) = 1
2πi
 ∫

L
 ϕ(t)
t − z dt, (1.1)

where z ∈ CP
1 and t ∈ L. The function Φ(z) is piecewise holomorphic in
CP
1 \ L and for suﬃciently large |z| we have a decomposition of Φ(z) into
the sum
 Φ(z) ∼
 ∞∑

j=1
 aj
zj (1.2)

where aj = − 1
2πi ∫
L t
j−1ϕ(t)dt, j = 1, 2, .... Therefore, we have Φ(∞) = 0.
Let t0 ∈ L and t0 /∈ {s1, s2, ..., sm} , then in ordinary sense integral (1.1)
does not exist. Consider the formal expression

Φ(t0) = 1
2πi
 ∫

L
 ϕ(t)
t − t0 dt. (1.3)

Describe about t0 as centre a circle with so small a radius ε that it inter-
sects L in two points t1 and t2. Denote by l the arc t1t2. If for ε → 0 the
integral 1
2πi
 ∫

L\l
 ϕ(t)
t − t0 dt (1.4)

tends to a deﬁnite limit, then this limit is called the principal value of the
Cauchy type integral (1.1).
 4

Remark. It is obvious that, if the integral (1.3) exists in the ordinary
(i. e. Riemann) sense, then the principal value also exists (but not con-
versely). The integral (1.3) exists in the ordinary sense, if the integral (1.4)
tends to a deﬁnite limit whatever the arc l cut oﬀ around t0 may be, as long
as the length of this arc tends to zero; it is essential for the deﬁnition of the
principal value that the ends t1 and t2 of the arc l lie at equal distances from
t0. Theorem 1.1. If in the neighbourhood of t0 the function ϕ(t) satisﬁes
the H¨older continuity condition then there exists the principal value of the
Cauchy type integral.
This theorem allows to deﬁne the value of the function Φ(z) on the curve
L. Denote Φ
±(t0) = lim
z→t0,z∈U ± Φ(z), t0 ∈ L,

then we have Sohocki˘i-Plemelj formulas for boundary values

Φ
+(t0) = 1
2 ϕ(t0) + 1
2πi
 ∫

L
 ϕ(t)
t − t0 dt,

Φ
−(t0) = −1
2 ϕ(t0) + 1
2πi
 ∫

L
 ϕ(t)
t − t0 dt.

The aforementioned deﬁnitions and propositions also extend for those
cases when ϕ is an n-vector or an n × n−matrix function.
The Riemann-Hilbert transmission problem for vector valued functions
can be formulated as follows:

Riemann-Hilbert transmission problem: Suppose one has H¨older
continuous matrix-functions G : L → GL(n, C). Describe the totality of
the piecewise holomorphic vector functions Φ(t) in U + ∪ U −, which admit
continuous boundary values on L, satisfy the transmission condition

Φ
+(t) = G(t)Φ
−(t), (1.5)

for any t ∈ L, and have ﬁnite order at ∞.

5

This problem is reduced to the system of singular integral equations in
the following manner.
Let the identity Φ
+(t) − Φ
−(t) = ϕ(t)

be satisﬁed on the curve L. The piecewise holomorphic function, which has
ﬁnite order at ∞ is represented by the Cauchy type integral

Φ(z) = 1
2πi
 ∫

L
 ϕ(t)
t − z dt + γ(z), (1.6)

where γ(z) = (γ1(z), γ2(z), ..., γn(z)) is the principal part of the function
Φ(z) at ∞. Therefore, our problem is reduced to ﬁnding functions ϕ and γ.
Let us use Sohocki˘i-Plemelj formulas for Φ(z) and substitute the obtained
expression in the transmission condition (1.5). We obtain the system of
singular integral equations for the functions ϕ1, ϕ2, ..., ϕn :

A(t0)ϕ(t0) + B(t0)
πi
 ∫

L
 ϕ(t)
t − t0 dt = F (t0), (1.7)

where A(t0) = 1+G(t0), B(t0) = 1−G(t0), F (t0) = (G(t0) − 1)γ(t) and 1 is
the unit matrix in GL(n, C).
The function F (t0) contains an unknown polynomial γ(t0). It must be
chosen so that the system (1.7) must have solutions. This last condition is
satisﬁed if and only if the system

∫

L f (t)ψk(t)dt = 0, k = 1, 2, ..., k′ (1.8)

is satisﬁed, where ψk(t), k = 1, 2, ..., k′ forms a complete system of linearly
independent solutions of the adjoint of problem (1.5).
Properties of the solutions of RHTP:
Property 1. If Φ1(z), ..., Φn(z) are solutions of the RHTP, then for any
polynomial functions p1(z), ..., pn(z) the function

Φ1(z)p1(z) + ... + Φn(z)pn(z)

again is a solution.
 6

Property 2. Suppose for some z0 we have Φ(z0) = 0. Then

Φ(z)
z − z0

again is a solution of the RHTP.
Property 3. Let k be the number of linearly indepedent solutions of
the system of singular integral equations (1.7), then the order at inﬁnity of
nontrivial solutions of the RHTP is at least k (note, that k ≥indG + (m +
1)n − k′, where m is order of the pole at inﬁnity).
Let
 Ψ(z) =
 





 Φ
1
1(z) Φ
2
1(z) ... Φ
n
1 (z)
Φ
1
2(z) Φ
2
2(z) ... Φ
n
2 (z)
... ... ... ...
Φ
1
n(z) Φ
2
n(z) ... Φ
n
n(z)
 






where the column Ψi(z) = (Φ
i
1(z), ..., Φ
i
n(z)) of the matrix Ψ(z) consists of
solutions of the RHTP and let det Ψ(z) be not identically zero. In this case
the system of the solutions Ψ1(z), ..., Ψn(z) is called a fundamental system
of solutions.
If det Ψ(z) ̸= 0 for any z ∈ C (including the curve L), then Ψ1(z),...,Ψn(z)
is called normal. Note, that det Ψ(t) ̸= 0 for t ∈ L means, that det Ψ+(t) ̸=
0, det Ψ−(t) ̸= 0.
Determinant of the system of normal solutions may be 0 at inﬁnity, or
∞ may be a pole for it. Denote by κ1, κ2, ..., κn the order at inﬁnity of the
system of normal solutions Ψ1(z), ..., Ψn(z) and consider the matrix-function
Ψ(z)zdK , where
 dK =
 


 zκ1 0
...
0 zκn
 


 (1.9)

is a diagonal matrix with entries zκi and the integers κ1, κ2, ..., κn satisﬁes
the conditions κ1 ≥ κ2 ≥ ... ≥ κn. (1.10)

It is clear that limz→∞ det(Ψ(z)zdK ) = c < ∞ and therefore Ψ(z)zdK is a
holomorphic matrix function in the neighbourhood of ∞.
The normal system of solutions is called canonical, if the function ∆(z) =
det(Ψ(z)zdK ) is not zero at ∞. Denote by χ(z) the system of canonical
solutions.
 7

The integers (1.10) are called partial indices of the homogeneous trans-
mission problem or of the matrix function G(t). The number

κ = 1
2πi∆L arg det G(t)

is called the global index or simply index of the RHTP.
Theorem 1.2.(Muskhelishvili [Mus]). For every G(t) canonical solutions
always exist. The sequence (1.9) does not depend on the considered canonical
solution and κ = κ1 + κ2 + ... + κn.

The matrix-function χ0(z) = Ψ(z)zdK

is holomorphic invertible in U − and det χ0(z) ̸= 0, for every points t ∈ L.
Using the identity (1.5) we obtain the Birkhoﬀ factorization of the matrix-
function G(t) : G(t) = χ
+(t)t
dK [
χ
−
0 (t)]−1 .

It is reasonable to detalize this Birkhoﬀ theorem as we’ll use it again.
Denote by Ω the space of all H¨older-continuous loops G : L → GL(n, C).
It is a Banach Lie group with natural norm and operetion.
Let
Ω
+ = {f ∈ Ω : f is the boundary value of the matrix function holomor-
phic in U
+},
Ω
− = {f ∈ Ω : f is the boundary value of the matrix function holomor-
phic in U
− and is regular at inﬁnity f (∞) = 1}.
Theorem 1.3. (Birkhoﬀ) Any loop f ∈ Ω can be represented as

f (t) = f −(t)dKf +(t), (1.11)

where f ± ∈ Ω
± and dK is a diagonal loop (1.9) with condition (1.10).
The diagonal matrix dK will be called the characteristic loop of the cor-
responding matrix-function, whereas K = (k1, k2, ..., kn) – the characteristic
multiindex. Two loops f, g ∈ Ω will be called equivalent, if f and g have
identical characteristic multiindices. For K = (k1, k2, ..., kn), denote by ΩK
the set of equivalence classes of loops Ω and call it the Birkhoﬀ-Bojarski
stratum. The topological structure of ΩK has been studied by Bojarski,
who showed, that if L is a Jordan curve, then the strata ΩK are connected.

8

The representation (1.11) is not unique, but if one ﬁxes f + (or f −) then f −

(respectively f +) will be uniquely deﬁned.
The Banach Lie group Ω
+ × Ω
− acts analytically on Ω via

f α
↦−→ h1f h
−1
2 , f ∈ Ω, h1 ∈ Ω
+, h2 ∈ Ω
−.

It is clear, that the orbit of the diagonal matrix dK by the action α is ΩK.
Theorem 1.4 (Disney [Dis]) The stability subgroup HK of f under the
action α consists of those pairs (h1, h2) of upper triangular matrix-functions
where the (i, j)-th entry in h1 is a polynomial in z of degree at most (k1 − k2)
and f = h1f h
−1
2 , the space HK has ﬁnite dimension

dim HK = ∑

ki≥kj (ki − kj + 1).

The stratum ΩK is a locally closed analytical submanifold of Ω and codi-
mension of ΩK in Ω is equal to

dim Ω/ΩK = ∑

ki⟩kj (ki − kj − 1).

Consider the holomorphic vector bundle on CP1 which is obtained by
the covering of the Riemann sphere CP
1 by three open sets {U +, U −, U3 =
CP
1\{0, ∞}}, with transition functions

g13 = h1 : U + ∩ U3 → GL(n, C),

g23 = h2dK : U − ∩ U3 → GL(n, C).

It is denoted by E → CP1. From the Birkhoﬀ theorem it follows, that every
holomorphic vector bundle splits into direct sum of the line bundles

E ∼= E(k1) ⊕ ... ⊕ E(kn). (1.12)

Remark. Possibility of decomposition of a holomorphic vector bundle
into the sum (1.12) is proved by A. Grothendieck, without applying the
Birkhoﬀ theorem.
The numbers k1,...,kn are the Chern numbers of the line bundles E(k1),...,E(kn)
and satisfy the conditions k1 ≥...≥ kn. The integer-valued vector K =

9

(k1, ..., kn) ∈ Z
n is called the splitting type of the holomorphic vector bundle
E. It deﬁnes uniquely the holomorphic type of the bundle E.
Connection between partial indices κ1, ..., κn of the RHTP, characteristic
multiindex of the matrix-function f ∈ Ω and splitting type of the holomor-
phic vector bundle E are presented in the following summarizing theorem:
Theorem 1.5. There is a one-to-one correspodence between the strata
ΩK and holomorphic vector bundles on CP
1.
Denote by O(E) the sheaf of germs of holomorphic sections of the bundle
E, then the solutions of the RHTP are elements of the zeroth cohomology
group H 0(CP1, O(E)), therefore the number l of the linearly independent
solutions is dim H 0(CP1, O(E)), as the Chern number c1(E) of the bundle
E is equal to index det G(t), we obtained the known criterion of solvability
of the RHTP. In particular the following theorem is true:
Theorem 1.6. The RHTP has solutions if and only if c1(E) ≥ 0 and
the number l of linearly independent solutions is

l = dim H 0(CP1, O(E)) =
 n∑

i=1 ki + 1.

Suppose L is the same as above and G : L → GL(n, C) is a discontinuous
function of the ﬁrst kind at the point s1 ∈ L, i. e. lim
t→s1+0 G(t) ̸= lim
t→ss−0 G(t).

Denote by G(s1 + 0) = lim
t→s1+0 G(t), G(s1 − 0) = lim
t→s1−0 G(t).

Let G = G−1(s1 + 0)G(s1 − 0) (1.13)

and Γ = 1
2πi ln G, so that if λi are eigenvalues of G, then µi = 1
2πi ln λi satisﬁes
the conditions 0 ≤ Reµi < 1.
Consider the functons

ω+(z) = (z − s1)Γ def
= e
Γ ln(z−s1),

ω−(z) = ( z − s1
z − z0
 )Γ def
= e
Γ ln
( z−s1
z−z0
 )
,

where z0 is some ﬁxed point in U +. It is known that ω+(z) is a single valued
matrix-function on C \ l1, where l1 is a curve with endpoints s1 and ∞. ω−(z)
is a single valued matrix-function on C\l2, where l1 is a curve with endpoints
z0 and s1.
 10

Suppose lim
t→s1+0 (t − z0)Γ = (s1 − z0)Γ,

then lim
t→s1−0 (t − z0)Γ = e
2πi(t1 − z0)Γ = G(t1 − z0)Γ. (1.14)

Introduce new vector-functions f +
1 (z) and f −
1 (z) :

f +
1 (z) = (z − s1)ΓG−1(s1 + 0)f +(z),

f −
1 (z) = (z − s1
z − z0
 )−Γ f −(z).

They are holomorphic respectively on U ± and satisfy the transmission con-
dition
 G(s1 + 0)(z − s1)Γf +(z) = G(t) (z − s1
z − z0
 )Γ f −(z),

or
 f +
1 (z) = (z − s1)−ΓG−1(s1 + 0)G(t) (z − s1
z − z0
 )Γ f −
1 (z).

Let us denote G1(z) = (z −s1)−ΓG−1(s1 + 0)G(t) ( z−s1
z−z0
 )−Γ and prove that
G1(t) is continuous at the point s1. Indeed

G1(s1 + 0) = lim
t→s1+0
 [(t − s1)−ΓG−1(s1 + 0)G(t) (t − s1
t − z0
 )Γ] = (s1 − z0)−Γ.

To calculate G1(s1 − 0) we use (1.13), (1.14) and obtain

G1(s1 − 0) = lim
t→s1−0
 [(t − s1)−ΓG−1(s1 + 0)G(t) ( t−s1
t−z0
 )Γ] =

= lim
t→s1−0
 [(t − s1)−ΓGG−1 ( t−s1
t−z0
 )Γ] = (s1 − z0)−Γ.

Now consider the general case. Let s1, ..., sm ∈ L be points of discontinu-
ity and let there be ﬁnite limits G(sj + 0) = lim
t→s1+0 G(t) and G(sj −0) = lim
t→s1−0
G(t). The curve L will be understood to be the union of smooth, noninter-
secting arcs L1, L2, ..., Lm with deﬁnite positive directions. Therefore ends of
arcs Lj (j=1,2,...,m) are sj and sj+1.
Suppose
Gj = G−1(sj + 0)G(sj −0) and Γj = 1
2πi ln Gj, so that if λi
j are eigenvalues
of Gj, then µj
i = 1
2πi ln λi
j. Denote ρ
j
i = Reµj
i and normalize the choice of ln
demanding that 0 ≤ ρ
j
i < 1.
 11

Consider the matrix-functions

Ω
+
j (z) = AjG(sj + 0)(z − sj)Γj , Ω
−
j (z) = Bj
 ( z − sj
z − z0
 )Γj ,

where Aj, Bj are constant matrices:

A1 = E, Aj =
 

j−1∏

k=1 Ω
+
k (sj)




−1 ,

B1 = E, Bj =
 

j−1∏

k=1 Ω
−
k (sj)



−1 , j = 2, 3, ...m.

The functions Ω
+
j (z) are holomorphic respectively in U ±.
Introduce new vector-functions

f +(z) =
 m∏

j=1 Ω
+
j (z)f +
1 (z),

f −(z) =
 m∏

j=1 Ω
−
j (z)f −
1 (z).

Use the transmission condition (1.5) and obtain:

f +
1 (t) =
 






 m∏

j=1 Ω
+
j (t)




−1 G(t)
 m∏

j=1 Ω
−
j (t)



 f −
1 (t).

Proposition 1.1.The matrix-function

G1(t) =
 

 m∏

j=1 Ω
+
j (t)



−1 G(t)
 m∏

j=1 Ω
−
j (t)

is continuous at points s1, ..., sm.
Proof. Calculate G1(sj + 0) and G1(sj − 0).

G1(sj + 0) =

= lim
t→s1+0
 

 m∏

k=j+1 Ω
+
k (sj)



−1 (t − sj)−Γj G−1(sj + 0)A
−1
j
 

j−1∏

k=1 Ω
+
k (sj)



−1 =

12

= G(sj + 0)
 j−1∏

k=1 Ω
−
k (sj)Bj
 ( t − sj
t − z0
 )Γj m∏

k=j+1 Ω
−
k (sj) =

=
 

 m∏

k=j+1 Ω
+
k (sj)



−1 lim
t→s1+0
 ((t − sj)−Γj ( t − sj
t − z0
 )Γj ) m∏

k=j+1 Ω
−
k (sj) =

=
 

 m∏

k=j+1 Ω
+
k (sj)



−1 (sj − z0)−Γj m∏

k=j+1 Ω
−
k (sj),

G1(sj−0) = lim
t→s1−0
 

 m∏

k=j+1 Ω
+
k (sj)




−1 (t−sj)−Γj G−1(sj+0)A
−1
j
 

j−1∏

k=1 Ω
+
k (sj)



−1

G(sj − 0)
 j−1∏

k=1 Ω
−
k (sj)Bj
 ( t − sj
t − z0
 )Γj m∏

k=j+1 Ω
−
k (sj) =

=
 

 m∏

k=j+1 Ω
+
k (sj)




−1 lim
t→s1−0
 

(t − sj)−Γj GjG−1
j
 ( t − sj
sj − z0
 )Γj 

 m∏

k=j+1 Ω
−
k (sj) =

=
 

 m∏

k=j+1 Ω
+
k (sj)



−1 (sj − z0)−Γj m∏

k=j+1 Ω
−
k (sj).

Therefore, the RHTP with discontinuity points reduces to the transmis-
sion problem considered at the very beginning, but in this case it is necessary
to ﬁnd solutions, which are holomorphic respectively in U ± and its bound-
ary values have discontinuity points. It can be proved that if (f +, f −) is
a solution of RHTP with discontinuity points, then this solution extends
continuously to these points too. It means, that there is a system of canoni-
cal solutions χ0(z) of the transmission problem, which satisﬁes the following
conditions:
1. det χ(z) ̸= 0, on C with possible exception of points s1, s2, ..., sm.
2. There are the diagonal matrix-function dK, that then

lim
z→∞ χ(z)dK(z) = c ̸= 0 < ∞.

3. If sj is some singular point, then

lim
z→sj (z − sj)εχ(z) = 0,

for some real number ε > 0.
 13

2 The system of ordinary diﬀerential equa-
tions with regular singularity

Consider the system on a small disk U ⊂C with center 0,

df
dz = A(z)f (z), f (z) = (f 1(z), ..., f n(z)) ∈ Cn, (2.1)

where A(z) is a holomorphic matrix function on U ∗ = U\{0}.
Let p : ̃U ∗ → U ∗ be the universal covering of U ∗ and let ξ and z denote
the local coordinate on ̃U ∗ and U ∗, respectively.
The system (2.1) has n linearly independent holomorphic solutions in a
small neighbourhood of z0 ∈ U ∗. Denote the space of solutions by ℜ. If
f ∈ ℜ, then f is a holomorphic function on ̃U ∗. Let Γ be the group of deck
transformations of the covering
 p : ̃U ∗ → U ∗.

If α ∈ Γ, then α deﬁnes the automorphism α∗ : ℜ → ℜ of the solution
space in this manner:

α∗f = f ◦ α−1, i.e. (α∗f )(ξ) = f (α−1ξ).

Clearly, α∗f is also a solution to (2.1) and therefore a map

ρ : Γ → GL(n, C), α ↦−→ α∗. (2.2)

is obtained.
If β ∈ Γ is another element, then (αβ)∗ = α∗β∗, i. e. the map (2.2) is a
homomorphism. Thus f = (f ◦ α)ρ(α). (2.3)

The homomorphism ρ is called the monodromy representation corre-
sponding to the system (2.1).
Let Φ(z) be the fundamental system of solutions to (2.1) and let Φ1(z)
be another invertible solution of the matrix ODE’s:

dΦ1
dz = A(z)Φ1(z).

14

Then Φ1(z) = Φ(z)G with some constant matrix G ∈ GL(n, C). Instead of
(2.3) we get Φ1(z) = (Φ1 ◦ α)ρ1(α) with some

ρ1 : Γ → GL(n, C).

So Φ(z)G = (Φ(z)G ◦ α)ρ1(α) = (Φ ◦ α)Gρ1(α).

But Φ(z) = (Φ(z) ◦ α)ρ(α), thus (Φ(z) ◦ α)ρ(α)G = (Φ(z) ◦ α)Gρ1(α).
Hence ρ1(α) = G−1ρ(α)G, where G is the same for all α. We see that to a
system (2.1) there corresponds a class of mutually conjugate representations
ρ : Γ → GL(n, C). We will call this class the monodromy representation or
simply monodromy.
The group of deck transformations Γ is now the inﬁnite cyclic group gen-
erated by the deck transformation α which corresponds to one trip around 0
counterclockwise. Clearly, ln ξ is a holomorphic function on ˜U ∗ and ln(αξ) =
ln ξ + 2πi. Let G = ρ(α−1) so that

Φ(αξ) = Φ(ξ)G. (2.4)

Let E = 1
2πi ln G, so that if λj are eigenvalues of G and µj of E, then
µj = 1
2πi ln λj. Denote τj = Re µj and normalize the choice of ln demanding
that 0 ≤ τj < 1.
Introduce the function ξE = e
E ln ξ (which is holomorphic on ˜U ∗):

(αξ)E = e
E(ln ξ+2πi) = ξEG.

Then by (2.4)
 Φ(αξ)(αξ)−E = Φ(ξ)GG−1ξ−E = Φ(ξ)ξ−E.

Hence Φ(ξ)ξ−E can be considered as a single-valued holomorphic function on
U ∗.Consider any sector Σ having vertex at 0. 0 is a regular singularity of
this system, if for the covering sector Σ
′ on U ′ and for any solution f (ξ), the
restriction f (ξ) |Σ′ has at most polynomial growth as z → 0 remaining in Σ.
Analogically one deﬁnes the regular singularity of the n-th order diﬀer-
ential equation

x
(n)(z) + a1(z)x
(n−1)(z) + ... + an−1(z)x
′(z) + an(z)x(z) = 0. (2.5)

15

Observe that the system (2.1) and the equation (2.5) have regular singular
points.
Theorem 2.1.(Poincar`e) Let f (z) be some solution of the system (2.1).
Then f (z) can be represented as follows:

f (ξ) = Z(z)ξE,

where Z is holomorphic on U ∗.
Proposition 2.1. Every coordinate function fj(ξ) of a solution f (ξ) is

fj(ξ) = ∑

p,q ξτphp,q(z) ln
lq ξ, (2.6)

0 ≤ Reτq < 1, lq ∈ Z, lq ≥ 0.

Let n
j
pq denote order of the zero of the function hpq(z) at the point 0, and
let n
j = minp,q n
j
p,q. There is deﬁned a map

ϕ : ℜ → Z, ϕ(f ) = min
j=1,...,n n
j.

The map ϕ will be called Levelt’s normalization of the solution f (z). It
has the following properties:
1. ϕ(λf ) = ϕ(f ), if λ ∈ C ∗;
2. ϕ(0) = ∞;
3. ϕ(f1 + f2) ≥ min(ϕ(f1), ϕ(f2)), with equality if ϕ(f1) ̸= ϕ(f2).
From the algebraic viewpoint ϕ is a nonarchimedean valuation on ℜ over
the trivial valuation on C.
The integer valued function ϕ deﬁnes a ﬁltration of ℜ :

0 ⊂ ℜ0 ⊂ ℜ1 ⊂ ℜ2 ⊂ ... ⊂ ℜm ⊂ ℜ, (2.7)

such that ϕ is constant on the quotient space ℜj/ℜj−1 and if ki
j = ϕ(ℜj/ℜj−1),
then k1 > k2 > ... > km. Let dj = dim(ℜj/ℜj−1). We say that ϕ takes the
value kj with multiplicity dj.
We shall use also the notation

ϕ1 = ϕ2 = ... = ϕd1 = k1 > ϕd1+1 = ... = ϕd1+d2 = k2 > ... > ϕd1+d2+...+dm−1

= ϕd1+d2+...+dm = km.

16

Note that ϕ1 ≥ ϕ2 ≥ ... ≥ ϕm.

By deﬁnition of ϕ it follows that

ϕ(α∗f ) = ϕ(f ),

hence it follows that α∗ preserves the ﬁltration (2.7) and the monodromy
matrix G is upper triangular.
A basis f1(z), f2(z),...,fn(z) of the solution space ℜ, satisfying the condi-
tions ϕ(fi) = ϕi and such that the monodromy matrix G is upper triangular,
will be called a Levelt’s basis.
Theorem 2.2. [Le]. The fundamental system of solutions Φ(ξ) related
to a Levelt’s basis is Φ(ξ) = U(z)zΨξE,

where U(z) is holomorphic on U ∗ and det U(z) ̸= 0, Ψ = diag(ϕ1, ...ϕm) and
E = 1
2πi G is upper triangular.
Remark. If 0 is a regular singular point, then U(z) is meromorphic in
U, i. e. U(z) is a single valued function.
Proposition 2.2. Let U(z) be holomorphically invertible at z = 0 and
let L(z) = Ψ + zΨEz−Ψ

be holomorphic. Then the system
df = ωf

is Fuchsian at z = 0, where ω = dΦ(z)
dz Φ
−1(z).
Proof.
 dΦ(z)
dz = dU(z)
dz zΨξE + 1
z U(z)zΨEξE =

1
z (z dU(z)
dz + U(z)L(z))zΨξE,

where L(z) = Ψ + zΨEz−Ψ,

then dΦ(z)
dz Φ
−1(z) = 1
z (z dU(z)
dz + U(z)L(z))U −1(z)

17

is Fuchsian at point 0.
If 0 is a pole of order one for the matrix valued function A(z), then the
system (2.1) is called Fuchsian. Let

A = Resz=0A(z),

then (2.1) gives df
dz = A
z f (z)

Proposition 2.3. 1) Every Fuchsian system is regular.
2) 0 is a regular singular point for the equation (2.5) if and only if the
functions zjaj(z) are holomorphic at 0.
Remark. 1) The set of regular singular systems contains the set of
Fuchsian systems.
2) The ordinary diﬀerential equation (2.5) is regular if and only if it is
Fuchsian.
From the proposition 2.3 follows that the coeﬃcients a1(z), a2(z), ..., an(z)
are holomorphic in some punctured neighdourhood of 0 and a1(z) has there
at most a pole of the 1-st order, ..., ai(z) — at most a pole of the i-th order,
..., an(z) — at most a pole of the n−th order.
It turns out that (2.5) is regular at the point 0 if and only if the system
is describing the behavior of the vector

(f 1(z), ..., f n(z)) = (x(z), dx(z)
dz , ..., dn−1x(z)
dzn−1 )

i. e. the system

df (z)
dz =
 





 0 −1 ... 0
... ... ... ...
0 0 ... −1
−an(z) −an−1(z) ... −a1(z)
 




 f (z)

is regular at 0. It is well known that (2.5) is regular at z = 0 if and only if
it is Fuchsian at z = 0.
The systems df (z)
dz = A(z)f (z) and dg(z)
dz = B(z)g(z) are holomorphically
(meromorphically) equivalent if there exists in a neighbourhood of 0 a holo-
morphic (meromorphic) at 0 matrix function H : V → GL(n, C), such that

18

the transformation (z, f (z)) = (z, H(z)f (z)) maps one equation to another,
i. e.
 B(z) = dH(z)
dz H −1(z) + H(z)A(z)H −1(z). (2.8)

If two systems of equations are equivalent then their monodromy groups
are conjugate. Besides, if 0 is a regular singular point for the system, this
system is equivalent to df
dz = A
z f (z), where A is a constant matrix.
To eliminate ambiguity we introduce some standard deﬁnitions.
Meromorphic connexion at the point 0 is called a pair (F, ∇), where F is
an n-dimensional vector space over the ﬁeld K = O[ 1
z ], whereas ∇ : F → F
is an operator which satisﬁes the Leibniz rule

∇(h, s) = dh
dz s + h∇s,

for each function f ∈ K and s ∈ F .
Let e1, e2, ..., en be a basis of F and let ∇ei be expressed in this basis in
the following manner:
 ∇ei = −
 n∑

j=1 θij(z)ej

where θ = (θij(z)) ∈ End(n, K), then for s = ∑n
j=1 sj(z)ei we shall obtain

∇s =
 n∑

i=1( dsi(z)
dz −
 n∑

j=1 θij(z)ej(z))ei.

By the last formula it follows, that ∇s = 0 is equivalent to ds
dz = θs, or
(d − θ)s = 0.
Let us denote the matrix-valued 1-form θdz by ω, then the system will
be (d − ω) = 0 and the connexion will be ∇ = d − ω. Connexions are gauge
equivalent if and only if correspoding systems of equations are equivalent,
i. e. satisfy the equality (2.8).

3 Connection between RHTP and RHMP

Let G(t) be the transmission matrix-function for the RHTP and suppose it
is piecewise constant, i. e. G(t) = GiGi−1...G1 if t ∈ sisi+1. Let χ0(z) be the

19

canonical solution and ω = dχ0(z)χ
−1
0 (z) be a form which is single-valued on
the Riemann sphere and holomorphic outside the points s1, ..., sm.
Proposition 3.1. The monodromy matrices of the regular system of
ODE’s df = ωf (3.1)

are G1, G2, ..., Gm.
Indeed, consider RHTP with the piecewise constant transmission func-
tion G(t) and denote by χ0(z) the canonical solution of the corresponding
transmission problem. Let z0 ∈ U −. Take some singular point si and let γi
be a loop beginning at z0 and going around the singular point si along a
small circle. It in transmission condition follows, that the extension of χ
−
0 (z)
along the loop γi goes to Giχ
−
0 (z).
Theorem 3.1. (Plemelj) If some monodromy matrix is diagonalizable,
then the system (3.1) is Fuchsian.
Proof. Let Y (ξ) be the fundamental system of solutions and let the
monodromy matrix Ej which corresponds to the singular point sj be diagonal.
By theorem 2.1 in the neighbourhood of sj one can represent Yj(ξ) as follows:

Yj(ξ) = Uj(z)(ξ − sj)Ej

where Uj(z) is holomorphic on U ∗. By Sauvage’s lemma there exists a matrix
Γ(z) holomorphically invertible outside sj such that

Γ(z)Uj(z) = Vj(z)(z − sj)Ψj

where Vj(z) is holomorphically invertible at sj and Ψ = diag(ϕ1, ..., ϕn).
Introduce a new dependent variable g = Γ(z)f. By (2.8) we have

dg(z)
dz =
 ( dΓ(z)
dz Γ−1(z) + Γ(z)A(z)Γ−1(z)
) g(z).

Therefore the new system is still Fuchsian outside sj.
We want to prove that if conditions of the theorem are satisﬁed, then the
system is Fuchsian at the point sj too.
Take Levelt’s Y (ξ) (theorem 2.2) in the neighbourhood sj :

Y (ξ) = U(z)(z − sj)Ψj (ξ − sj)Ej .

20

We repeat the calculation presented during the proof of proposition 2.2.

dΦ(z)
dz = dU(z)
dz (z − sj)Ψj (ξ − sj)Ej + 1
z U(z)Ψj(z − sj)Ψj (ξ − sj)Ej +

+ 1
z U(z)(z − sj)Ψj Ej(ξ − sj)Ej =

= 1
z (z dU(z)
dz + V (z)L(z))(z − sj)Ψj (ξ − sj)Ej ,

where L(z) = ¯Ψ + (z − sj)Ψj Ej(z − sj)−Ψj ,

then we obtain:

dΦ(z)
dz Φ
−1(z) = 1.
z (z dU(z)
dz + U(z)L(z))U −1(z),

Ej is diagonal, because L(z) = Ψj + Ej is holomorphic. Therefore, by propo-
sition 2.3 our system is Fuchsian at the point sj too.

4 Extension of a bundle with connexion

Let X be a Riemann surface of genus g and S = {s1, s2, ..., sm} be a set of
marked points on X. Denote by Xm = X \ S. Let ˜X → Xm be the universal
covering map of Xm, then it is a bundle with ﬁbre π1(Xm, z0), where z0 ∈ Xm.
π1(Xm, z0) is isomorphic to the group of deck transformations of this covering
and therefore acts on ˜X.
Let ρ : π1(Xm, z0) → GL(n, C) (4.1)

be some representation.
Consider the trivial principal bundle ˜X×GL(n, C) → ˜X (or vector bundle
˜X × Cn → ˜X). The quotient space ˜X × GL(n, C)/ ∼ gives the locally
trivial bundle on Xm, where ∼ is an equivalence relation identifying the pairs
(˜x, g) and (σ˜x, ρ(σ)g), for every ˜x ∈ ˜X, g ∈ GL(n, C) (or g ∈ Cn). Denote
the obtained bundle by Pρ → Xm (or Eρ → Xm) and call it the bundle
associated with the representation ρ. In obvious form this bundle according
to the transformation functions may be constructed in the following manner.

21

Let {Uα} be a simple covering of Xm, i. e. every intersection Uα1 ∩ Uα2 ∩
... ∩ Uαk is connected and simply connected. For each Uα, we choose a point
zα ∈ Uα and join z0 and zα by a γα starting at z0 and ending at zα. For a
point z ∈ Uα ∩ Uβ we choose a path τα ⊂ Uα which starts at zα and ends at
z. Consider gαβ (z) = ρ (γατα (z) τ −1
β (z) γ−1
β ) . (4.2)

We see that gαγ (z) = gβα (z)

and gαβgβγ (z) = gαγ (z)

on Uα ∩ Uβ ∩ Uγ.
The cocycle {gαβ (z)} does not depend on the choice of z. Hence from
this cocycle we obtain a ﬂat vector (or principal) bundle, which is denoted
by E′
ρ (P′
ρ).
Let {tα (z)} be a trivialization of our bundle, i. e.

tα : p−1 (Uα) → GL(n, C)

is a holomorphic mapping. Consider the matrix valued 1-form {ωα} :

ωα = −t
−1
α dtα.

{gαβ (z)} are constant on the intersection Uα ∩ Uβ and gαβ(z)tβ (z) = tα (z),
so on Uα ∩ Uβ the identity ωα = ωβ holds. Indeed, replacing tβ by t
−1
β gαβ in
the expression ωβ = −t
−1
β dtβ, we obtain

ωβ = −t
−1
α gαβ (z) dtαg−1
αβ (z) = −t
−1
α dtα.

So, ω = {ωα} is a holomorphic 1-form on Xm and therefore is a connexion
form of the bundle P′
ρ → Xm. Corresponding connexion is denoted by ∇′.
We will extend the pair (
P′
ρ, ∇′) to X. As the required construction is of
local character, we shall extend P′
ρ → Xm to the bundle P′′
ρ → Xm ∪ {si} ,
where si ∈ S.
First consider the extension of the principal bundle P′
ρ → Xm.
Let a neighbourhood Vi of the point si meet Uα1, Uα2, ...Uαk . As we noted
when constructing the bundle from transition functions (4.1) only one of

22

them is diﬀerent from identity. Let us denote it by g1k, then g1k = Gi, where
Gi is the monodromy which corresponds to the singular point si. Mark a
branch of the many valued function (˜z − si)Ei containing the point ˜si ∈ ˜Ui
(where Ei = 1
2πi ln Gi). Thus the marked branch deﬁnes a function

g01 = (z − si)Ei. (4.3)

Denote by g02 the extension of g01 along the path which goes around si
counterclockwise, and similarly for other points. At last on Ui ∩ Uαk ∩ Uα1
we shall have: g0k(z) = g01(z)Gi = g01(z)g0k(z).

The function g0k : Vi → GL(n, C) is the one deﬁned at the point si, and
takes there value coinciding with the monodromy matrix. It means, that we
made extension of the bundle to the point si. In a neighbourhood of si one
will have ωi = dg0kg−1
0k = Ei dz
z − si .

So we obtained the holomorphic principal bundle Pρ → X on the surface
X. The vector bundle associated to Pρ → X, which we denote by Eρ → X
and call canonical, is not topologically trivial. Its connexion is denoted by
∇. The holomorphic sections of Eρ are solutions of the equation

∇f = 0 ⇐⇒ df = ωf. (4.4)

Theorem 4.1.1) The system (4.4) has regular singularity at points
s1, s2, ..., sm.
2) The Chern number c1( Eρ) of Eρ → X is equal to

c1(Eρ) =
 m∑

i=1 tr(Ei). (4.5)

The triple (X, S, ρ) is called Riemann data, where X is a Riemann surface,
S ⊂ X denotes a ﬁnite subset of X, ρ : π1 (X \ S, z0) → GL(n, C) is any
representation with trivial kernel.

Riemann-Hilbert monodromy problem for Riemann surfaces.
Let us ﬁnd a system of ODE df = ωf, (4.6)

23

on a Riemann surface X for the given Riemann data (X, S, ρ), where S is
the set of regular singular points of the system (4.6) and its monodromy
representation coincides with ρ.

Theorem 4.2 [R¨oh]. For every Riemann data there exists a solution of
the Riemann-Hilbert problem for ODE’s with regular singularity.
Let (4.6) be the regular system of ODE’s which is induced by the rep-
resentation (4.1). By theorem 2.2 the fundamental matrix of solutions in a
neighbourhood of sj is

Φj (˜z) = Uj(z)(z − sj)Ψj (˜z − sj)Ej . (4.7)

Here Ψj are exponents of the solution space ℜ of the system (4.6) and Ej =
1
2πi ln Gj, with eigenvalues µ1
j , µ2
j , ..., µn
j satisfying the conditons 0 ≤ Reµi
j <
1. The numbers βi
j = ϕi
j + µi
j will be called exponents of the solution space
ℜ at the point sj (or j-exponents).
Proposition 4.1 [Le], [Bl1]. The system (4.6) is Fuchsian at sj if and
only if det Uj(sj) ̸= 0.
Proposition 4.2. If the system (4.5) is Fuchsian in a neighbourhood of
sj, then
 ωj = Aj
z − sj dz,

where Ai is a constant matrix with eigenvalues βi
j, i = 1, ..., n.
Proof. Indeed, suppose ω = A(z)dz, then

Aj = lim
z→sj ((z − sj)A(z)) = lim
z→sj
 ((z − sj) dΦj(z)
dz Φ
−1(z)
) =

lim
z→sj((z − sj) dUj(z)
dz Uj(z)+

+Uj(z) (
Ψj + (z − sj)Ψj Ej(z − sj)−Ψj ) U −1
j (z) =

= Uj(sj)(Ψj + Ej)U −1
j (sj).

Here Ej = limz→sj Ej(z), Ej(z) = (z − si)Ψj Ej(z − si)−Ψj . Therefore we
obtain that ψi
j + µi
j are eigenvalues of the matrix Aj.
Let the system (4.5) be Fuchsian. Transform the monodromy matrices
Gj, j = 1, 2, ...m to upper-triangular form by some matrices Cj. Assume

24

that Ψj, j = 1, 2, ..., m are diagonal integer valued matrices whose entries ϕi
j
satisfy the inequalities ϕ1
j ≥ ϕ2
j ≥ ... ≥ ϕn
j .

Consider the local section Uj(z) of the principal bundle Pρ → X over
Vj\sj such that the corresponding Φj(z) has the form (4.7).
The following proposition holds:
Proposition 4.3. Every extension of P′
ρ → Xm to the points sj which
is induced by a connexion ∇ with at most logarithmic singularities at sj, is
determined by matrices Cj and Ψj such that
1) C −1
j GjCj is upper triangular,
2) Ψj = diag(ϕ1
j , ϕ2
j , ..., ϕn
j ), ϕi
j ∈ Z,ϕ1
j ≥ ϕ2
j ≥ ... ≥ ϕn
j .
Extend P′
ρ → Xm in a similar way to all singular points. Denote by C
the collection (C1, C2, ..., Cm) and by Ψ the collection (Ψ1, Ψ2, ..., Ψm), where
Ψj = (ϕ1
j , ϕ2
j , ..., ϕn
j ). Denote by PC,Ψ
ρ → X the correspoding extension of the
bundle P′
ρ → Xm.
The collection C, Ψ is said to be admissible, if Cj, Ψj satisfy 1), 2) for
every j.
Proposition 4.4. There is a one-to-one correspodence between the set
of all Fuchsian systems of ODE’s on the Riemann surface with prescribed
monodromy and the set {
H 0(X, O(PC,Ψ
ρ )} of holomorphic sections of all
admisible extensions of the principal bundle P′
ρ → Xm.
The proof of the last two propositions in the case when X is the Riemann
sphere, is contained in [Bl3].

5 Criterion of stability.

Let E → X be a holomorphic vector bundle on a Riemann surface X, with
deg E = k and rankE = n. The normalized Chern class of the vector bundle
E is deﬁned by µ (E) = k
n .
A bundle E is called stable (resp. semi-stable) if for every proper sub-
bundle F ⊂ E, we have µ (F ) < µ (E) ,

(resp. µ (F ) ≤ µ (E)).

25

Properties of stable bundles:
1) If E → X is semi-stable and (n, k) = 1, then E is stable.
2) A line bundle L → X is stable.
3) Let L → X be a line bundle. E → X is stable if and only if E ⊗L → X
is stable.
4) If E → X is stable, then E is indecomposable and by the Riemann-
Roch theorem
 dim H 1 (X, O (EndE)) = n
2(g − 1) + 1. (5.1)

The deﬁnition of stability has been given by D. Mumford [Mum] oriented
towards Riemann surfaces of negative curvature. For example, in case g = 0,
stable bundle (in sense of Mumford) may be only line bundle E (k) (semi-
stable are E (k)⊕r), but there exist stable bundles on the Riemann sphere,
of rank more than one.
A criterion of stability for vector bundles on the Riemann sphere CP
1

given by B. Bojarski, will be reproduced below.
Let ℑ(n, k) be the space of all vector bundles on CP
1 of rank n with
Chern class k. By Grothendieck’s theorem every bundle E → CP1 splits
into direct sum (1.12) of line bundles.
The splitting type K = (k1, k2, ...kn) ∈ Z
n completely deﬁnes the holo-
morphic structure of E.
Theorem 5.1. [Boj1] [Boj2]. 1) A vector bundle E →CP
1 is stable if
and only if k1 − kn ≤ 1.
2) The space of stable bundles is an open and dense subspace of ℑ(n, k).
If E → X is a holomorphic vector bundle over a Riemann surface of genus
g ≥ 2, then it does not split into the sum of line bundles but some analogy
exists [Gi].
A criterion of stability belongs to A. Weil. In particular the following
theorem is true.
Theorem 5.2. [We]. A topologically trivial vector bundle is stable
if and only if it corresponds to an irreducible unitary representation of the
fundamental group π1 (X)
 ρ : π1 (X) → U(n). (5.2)

A generalization of Weil’s theorem is Narasimhan and Seshadri theorem,
which is a criterion of stability for topologically nontrivial holomorphic vector
bundles.
 26

Theorem 5.3.[N-S]. A holomorphic vector bundle E → X of rank n
and with Chern class k is stable if and only if it is induced from an irreducible
representation of the Fuchsian group, ρ : Γ → U(n), where Γ is a group with
2g + 1 generators a1, b1, a2, b2, ..., ag, bg, c (where g is genus of X), satisfying
the relations: q∏

i=1 [ai, bi] c = 1, (5.3)

ck = 1, (5.4)

whereas the irreducible representation ρ is

ρ (c) = exp (−2πiµ (E)) 1.

Let s ∈ X be a marked point and k < 0 any integer. As it is known, there
exists a covering π : H → X, which is branched at the point s and generators
(5.3) of the uniformization group Γ satisfying the conditions (5.4) − (5.5) and
H/Γ ∼= X \ {s} . So, Γ contains a ﬁnite cyclic subgroup with generator c,
it means that π−1(S) ⊂ H is the only ﬁxed point of Γ, and Γ is a central
extension of π1(X) :
 1 → Zm → Γ → π1(X) → 1.

The group Γ acts on the trivial bundle H × Cn → X via

(z, c) ↦−→ (cz, ρ (c) v) .

This action gives us the holomorphic bundle Eρ → X \ {s} .
For the Riemann data (X, {s} , ρ) by the theorem 4.2 there exists the
system of ODE’s df = ωf, (5.5)

which has regular singular points and monodromy representation of the sys-
tem (5.5) coinciding with ρ. This means that ω is a connexion form for the
holomorphic bundle Eρ → X \ {s}. The corresponding holomorphic connex-
ion is denoted by ∇′.
According to the construction of the 4-th section it is possible to ex-
tend (E′
ρ, ∇′) to Eρ → X. By proposition 4.2 the connexion form ω in the
neighbourhood of s will be:
 ω = µ (Eρ) 1 dz
z − s .

27

We obtain the following statement:
Theorem 5.4. Let E → X be a stable holomorphic vector bundle. Then
there exists a Fuchsian connexion θ on E which has only one singular point.
The system (5.5) has apparent singular points, and their quantity will be
estimated if a local representation induced by ρ is semi-simple.
A local representation induced by ρ at a point sk ∈ S is deﬁned as follows:
Let U be a neighbourhood of p that is biholomorphic to the unit disk satisfy-
ing U ∩S = {sk} . The injection U \{sk} → M \S induces a representation of
π1 (U \ {sk}) in GL(n, C). This is the local representation at sk ∈ S induced
by ρ.
Theorem 5.5.[O]. If the representation ρ is irreducible and the local
representation at some point of S induced by ρ is semi-stable, there exists a
Fuchsian linear diﬀerential equation on M which has at most

1 − n(1 − g) + n(n − 1)
2 (m + 2g − 2) (5.6)

apparent singularities, where m = cardS.
This estimate will be obtained by calculating zeros of the Wronskian of
our system. Indeed,let Φ (z) be the fundamental system of solutions of (5.5)
and f1(z), f2(z), ... , fn(z) be any row. Denote by D the operator d
dz .
Consider the equation

det
 





 g(z) f1(z) ... fn(z)
Dg(z) Df1(z) ... Dfn(z)
... ... ... ...
Dng(z) Dnf1(z) ... Dnfn(z)
 




 = 0, (5.7)

i. e. ω0(z)Dng(z) + ω1(z)Dn−1g(z) + ... + ωn(z)g(z) = 0, (5.8)

where
 ω0(z) = det
 





 f1(z) f2(z) ... fn(z)
Df1(z) Df2(z) ... Dfn(z)
... ... ... ...
Dnf1(z) Dnf2(z) ... Dnfn(z)
 






is the Wronskian of f (z) = (f1(z), f2(z), ..., fn(z)) . We denote it by W (z).
Write (5.8) as follows:

1
W (z) (ω0(z)Dng(z) + ω1(z)Dn−1g(z) + ... + ωn(z)g(z)) = 0. (5.9)

28

This equation is Fuchsian and its monodromy coincides with monodromy
of the system (5.5), but (5.9) has apparent singular points, they are zeros of
the Wronskian W (z). It is clear, that the poles of W (z) are singular points
of the system (5.5).
Collorary. The connexion θ has at most

n
2g − n(n − 1)
2 + 1

apparent singular points.
Let (X, S, ρ) be any Riemann data, where S is empty and ρ is an irre-
ducible unitary representation, then (5.6) is an ODE with apparent singular
points. The number p of apparent singular points will be estimated (by the-
orem 5.4): p ≤ n
2(g − 1) + 1.

Note that the right hand side of this inequality is the dimension of the
moduli space of stable holomorphic n-rank vector bundles on a Riemann
surface of genus g.
Every holomorphic bundle E has a canonical ﬁltration [At-Bo]

0 = E0 ⊂ E1 ⊂ E2 ⊂ ... ⊂ Er = E,

with Fi = Ei/Ei−1 semi-stable and

µ(F1) > µ(F2) > ... > µ(Fr).

E is a direct sum of semi-stable bundles F1, F2, ..., Fp. Hence

E ∼= F1 ⊕ F2 ⊕ ... ⊕ Fp. (5.10)

On the other hand, for any semi-stable vector bundle V there exists a
ﬁltration V = Vq ⊃ Vq−1 ⊃ ... ⊃ V1 = ∅,

such that V1 and Wi = Vi−1/Vi are stable. Since V1 is stable, it follows that
the cocycle z−µ(V1) deﬁnes V1. Analogically the cocycle for V2 is

aV2 =
 ( (z − x∞)−µ(W1)............∗
0.............(z − x∞)−µ(W2)
 )

29

and so on. Finally, for V we have

aV =
 


 (z − x∞)−µ(W1)............∗
.....
0.............(z − x∞)−µ(Wq)
 


 .

By (5.10) it follows that

ΨE = diag(AF1, ..., AFp). (5.11)

This gives the proof of the following result.
Theorem 5.6. Let E → X be a holomorphic vector bundle. Then the
cocycle (5.11) deﬁnes the given bundle up to an isomorphism.
The connexion ω agrees with the holomorphic structure on Eρ → X and
if ω1 is gauge equivalent to ω, the bundle Eρ1 → X is holomorphically equiv-
alent to Eρ → X. This gives possibility to describe holomorphic structures
on the C ∞-bundle E → X.
We consider therefore a ﬁxed C ∞ complex vector bundle E → X of rank
n and Chern class k and we denote the space of all holomorphic structures
on E by ℵ(n, k).
Let Aut(E) denote the group of automorphisms of E which means that
any element of this group is locally a C ∞ map of X into GL(n, C). Then
Aut(E) acts on ℵ(n, k) and the orbits by deﬁnition are the isomorphism
classes of complex analytic bundles on X with Chern class k and rank n.
Suppose Fi has rank ni and Chern class ki so that n = ∑ ni and k = ∑ ki.
So, we have the sequence of rational numbers

µ =
 ( k1
n1 , ... k1
n1 , k2
n2 , ..., k2
n2 , ..., kr
nr , ... kr
nr
 ) ,

which we call the type of E.
All the holomorphic bundles of given type µ deﬁne a subspace ℵµ of
ℵ(n, k). In particular, if all components of µ are equal (hence are all equal to
k
n ), then ℵµ ∼= ℵss is the semi-stable part of ℵ(n, k).
The codimension of ℵµ in ℵ (n, k) is equal to

∑

µi>µj (µi − µj + (g − 1)) .

If g = 0, we obtain the well known formula (theorem 1.3).

30

6 Holomorphic bundles on CP
1

Let S = {s1, s2, ...sm} be a set of marked points on CP
1 and

df = ωf (6.1)

be the system of ODE’s which is induced by the representation

ρ : π1 (CP1\S, z0) → GL(n, C). (6.2)

By proposition 1.2 the fundamental matrix of solutions in the neighbour-
hood of sj is Φj (˜z) = Uj(z)(z − sj)Ψj (˜z − sj)Ej (6.3),

where Ψj are exponents of the solution space ℜ of the system (6.1) and
Ej = 1
2πi ln Gj. Again denote by µ1
j , µ2
j , ..., µn
j the eigenvalues of Ej. Then
eigenvalues βi
j = ϕi
j + µi
j of the matrix Ψj + Fj are the exponents of the
solution space ℜ at the point sj (or j-exponents).
Let every singular point satisfy the condition det Uj(sj) ̸= 0. Then the
system (6.1) will be Fuchsian and therefore the 1-form ω will have single
poles. Denote Ai = Ressiω,

then the system (6.1) will be written in the following form

df =
 m∑

i=1
 Ai
z − si dz (6.4).

where the matrices Ai satisfy the condition ∑m
i=1 Ai = 0.
Proposition 6.1. [Le], [Bl1] 1) The number

β =
 m∑

j=1
 n∑

i=1 βi
j

is integer and is at most 0.
2) The system (6.1) is Fuchsian if and only if β = 0.
Our following discussion concerns Fuchsian systems. We emphasize this,
because after the Plemelj’s work “Problems in the sense of Riemann and
Klein” it was believed that Hilbert’s 21-st problem is solved for Fuchsian

31

systems, but A. Bolibruch in 1989 gave an example of a representation of the
fundamental group π1(CP
1\S, z0) which does not give a Fuchsian system.
Theorem 6.1.[Bl1]. Let (CP
1, S, ρ) be any Riemann data.
1) Case n=2. Then there exists a Fuchsian system where monodromy
representation coincides with ρ.
2) Case n=3. a) if m =CardS = 3 or b) m is arbitrary and ρ is irreducible
then Hilbert’s 21-st problem can be solved.
3) Case n > 3. For every S, where CardS > 3, there exists a representation
ρ which does not induce a Fuchsian system.
Let us make few comments on this theorem.
1) Let n=2. There exists a representation of the fundamental group,
which is not monodromy representation for any Fuchsian system, even in
case, when n=3.
Examples. Let s1, s2, s3 ∈CP
1. Correspoding monodromy matrices are

G1 =
 ( 1 c1
0 1
 ) , G2 =
 ( 1 c2
0 1
 ) , G3 =
 ( 1 −c1 − c2
0 1
 ) ,

where the numbers c1, c2 satisfy the condition c1c2(c1 + c2) ̸= 0. There
does not exist Fuchsian equation, whose monodromy group is generated by
these G1, G2, G3 matrices. There always exists a Fuchsian system for this
representation. This follows from Dekkers’ [D] theorem.
2) For the system

df =
 







 0 1 0
0 z 0
0 0 −z
 


 dz
z2 + 1
6
 


 0 6 0
0 −1 1
0 −1 1
 


 dz
z + 1

+ 1
2
 


 0 0 2
0 −1 −1
0 0 1
 


 dz
z − 1 + 1
3
 


 0 −3 −3
0 −1 1
0 −1 1
 


 dz
z − 1
2
 


 f

0, −1, 1, 1
2 are regular singular points (The points −1, 1, 1
2 are Fuchsian singu-
larities. However 0 is not Fuchsian, as it is a pole of order 2). Its monodromy
representation ρ is reduced. Therefore the Fuchsian system does not exists,
with these singular points and representation ρ.
From theorem 6.1 n. 3) follows, in general case, that on the marked
Riemann sphere always exists a vector bunble, which has no Fuchsian con-
nexions. So, solvability of Hilbert’s 21st problem depends on the conformal

32

structure on the Riemann sphere. The problem has topological character
only for rank two vector bundles. This case we consider below.
For every Fuchsian equation there exists a Fuchsian system (6.4), which
has the same singular point and monodromy. In particular, for the hyperge-
ometric equation
 y′′ + γ + (α + β + 1)
z(z − 1) y′ − αβ
z(z − 1) = 0

the aforementioned system will be:

df =
 (( 0 0
−αβ −γ
 ) d
dz +
 ( 0 1
0 γ − (α + β)
 ) dz
z − 1
 ) f

As we mentioned there exists a representation whose corresponding Fuch-
sian equation does not exist without apparent singular points. But if repre-
sentation is irreducible, for the estimation of the quantity of apparent singular
points we may have more precise inequality than in theorem 5.5.
Consider the vector bundle EC,Ψ associated with the principal bundle
P C,Ψ, which we introduced in section 4. Let K C,Ψ = (kC,Ψ
1 , kC,Ψ
2 , ..., kC,Ψ
n ) be
the splitting type of the vector bundle EC,Ψ.
The number
 τ (EC,Ψ) =
 n∑

i=1(kC,Ψ
1 − kC,Ψ
i )

is called the wieght of the bundle τ (EC,Ψ) and the number τ (EC,Ψ)
rankE is called
the normalized weight.
Theorem 6.2 [Bl3]. For any holomorphic vector bundle E → CP
1

with splitting type K C,Ψ = (kC,Ψ
1 , kC,Ψ
2 , ..., kC,Ψ
n ) and for any points S =
{s1, s2, ...sm} , where

m = max( max
i=1,2,...,n−1
(kC,Ψ
i − kC,Ψ
i+1 + 2), 3)

there exists a Fuchsian system with the singular points s1, s2, ...sm and with
monodromy ρ such that the following conditions hold:
1) ρ is irreducible.
2) The canonical extension E → CP1 of the vector bundle E′
ρ → CP
1\S,
constructed by means of the monodromy representation ρ, has the splitting

33

type k1 − γ(E), k2 − γ(E), ..., kn − γ(E), where γ(E) is equal to the integer
part of the normalized Chern number of the vector bundle E.
3) For the vector bundle E → CP
1 there exists a meromorphic connexion
with at most logarithmic singularities and with an irreducible monodromy
whose number of singular points is equal m and there is no connexion with
the properties mentioned above whose number of singular points is less than
m. Let (CP1, S, ρ) be any Riemann data with cardS = m, ρ : π1(CP1\S) →
GL(n, C) be irreducible and let the type of the canonical bundle induced
from ρ be (k1, k2, ...kn) . Denote by l the quantity of the ﬁrst equal numbers,
i. e. k1 = k2 = ... = kl. Under these conditions the quantity of apparent
singular points is at most

(m − 2)n(n − 1)
2 −
 n∑

i=1(k1 − ki) + 1 − l. [Bl2].

Consequently, we obtain an estimate for the partial indices in the case
when ρ is irreducible:

n∑

i=1(k1 − ki) ≤ (m − 2)n(n − 1)
2 + 1 − l. (6.5).

If the equality is achieved it means that we have the ODE induced by ρ
which has no apparent singular points.
Consider the canonical extension E → CP1 of the vector bundle E′
ρ →
CP
1\S induced by the representation (6.2) of the Fuchsian system (6.4).
The splitting type of E → CP1 can be algorithmically calculated with the
aid of system (6.4) as follows (we are repeating here the nice argument from
[Bl3]):
Consider the matrix A1 of (6.4), with eigenvalues β1
1, β2
1, ..., βn
1 . Let αi
j =
Re βi
j and α1
1 ̸= 0. Without loss of generality, we can assume that α1
1 ≥ 1.
(The case α1
1 ≤ −1 can be investigated in a similar way).
Consider the change g1 = T1f (6.6)

of the dependent variable f under the action of the constant nondegenerate
matrix T1 such that the coeﬃcient matrix A
′
1 = T1A1T −1
1 of the new sys-
tem has Jordan normal form with the ﬁrst eigenvalue equal to β1
1. Recall

34

that under the transformation (6.6) the system (6.1) is transformed into the
system dg1
dz = A
′(z)g1 (6.7)

where A
′ = T1AT −1
1 + dT1
dz T −1
1 .
Then consider the transformation

g2 = (z − s1)Dg1 (6.8)

where D = diag(−1, 0, ..., 0). Under transformations (6.6), (6.8) our original
system (6.4) is transformed into system (6.1), which is Fuchsian at s1, s2, ...sm
with an additional apparent singular point ∞.Moreover, the eigenvalues of
its coeﬃcient matrix A
′′
1 at s1 are equal to the following ones: β1
1 − 1, β2
1, ...,
βn
1 . Using the procedure whose ﬁrst step was described above, we can obtain
system (6.1), which is Fuchsian at s1, s2, ...sm with the additional apparent
singularity at ∞, and whose coeﬃceient matrix ̃A1 has an eigenvalue ̃β1
1 such
that [Re ̃β1
1 ] = 0.
In a similar way, we can obtain a system whose αi
j at all points s1, s2, ...sm
are equal to zero. This system is Fuchsian at these points and has one
additional apparent singular point at ∞. The transformation matrix T (z),
which transforms our (6.4) system into this new one, is meromorphic at
s1, s2, ...sm and ∞, holomorphically invertible oﬀ these points, and can be
calculated algorithmically on the basis of the system (6.4).
Treat the matrix T (z) as a transition function of some vector bundle on
CP
1 trivialized on C1 and a coordinate neighborhood V∞ of inﬁnity. Then
there exists a matrix Γ(z) holomorphically invertible in C1 and a matrix U(z)
holomorphically invertible in V∞ such that

Γ(z)T (z) = zKU(z),

where K = diag(k1, k2, ..., kn), k1 ≥ k2 ≥ ... ≥ kn.
Proposition 6.2. The collection of the numbers −k1, −k2, ..., −kn coin-
cides with the splitting type of the canonical extension E → CP
1 constructed
by the monodromy of the Fuchsian system (6.4).
Consider the case n=2.
Let i-exponents for the solutions space ℜ be ϕ1
i , ϕ2
i and let us assume
ϕ1
i ≥ ϕ2
i (which is always possible).
 35

The number γω = ∑m
i=1 (ϕ1
i − ϕ2
i ) is called Fuchsian weight for system
(6.4).
Fix a representation ρ for any Riemann data (CP 1, S, ρ) and denote by
Ωρ the set of Fuchsian systems corresponding to this data. The number
γρ = minΩρ γω is called Fuchsian weight for the representation ρ.
Let E → CP 1 be the holomorphic vector bundle induced by the repre-
sentation ρ and (k1, k2) be its splitting type. Then

γρ = k1 − k2.

Every rank two holomorphic bundle on CP 1 is holomorphically equivalent
to any bundle F → CP 1, which is obtained by the extension of the bundle
induced by an irreducible representation. So, for every rank 2 holomorphic
bundle there exists an irreducible connexion, which is holomorphic except
for the ﬁnite number nω of points, where it has simple poles. Denote by Ω
irr

the space of irreducible Fuchsian connexions. Let

p = min
ω∈Ωirr nω.

The identity p = k1 − k2 + 2 (6.9)

is satisﬁed.
From this follows the proposition.

Proposition 6.3. A rank two vector bundle F →CP
1 is stable if and
only if it is induced by the Gauss equation.
Proof. Let the bundle be stable, then from (6.9) we obtain p=3. As we
mentioned, there exists an irreducible representation

ρ : π1 (CP1\ {s1, s2, s3} , z0) → GL(n, C),

from which F is induced. It means that there exists the Gauss equation for
every irreducible representation [Bl2]. Therefore, F has Gauss connexion.
Converse proposition is obtained from (6.9), taking p=3.

36

7 On the splitting type of a rank three vector
bundle

B. Bojarski in [Boj3] has posed the question: whether the partial indices are
invariants of conformal transformation of the complex plane. Our following
reasoning is intended to move in this direction.
Let E → CP1 be a holomorphic vector bundle with characteristic matrix
dK, K = (k1, k2, ..., kn), k1 ≥ k2 ≥ ... ≥ kn. Consider the vector bundle
EndE → CP
1. The characteriestic matrix of this bundle is dK ⊗ d−1
K .
Clearly
 dim H 0 (
CP1, O(EndE)) = ∑

ki≥kj(ki − kj + 1),

dim H 1 (
CP1, O(EndE)) = ∑

ki>kj(ki − kj − 1) = ∑

ki>kj(ki − kj) + 1
2 n(n − 1).

The number
 ν(E) = dim H 1 (
CP1, O(EndE)) − 1
2n(n − 1)

will be called reduced dimension of the deformation space of complex struc-
tures of the bundle E.
For every holomorphic bundle E → CP1 consider the following diagram:

k1 − k2 k1 − k3 ... ... k1 − kn
k2 − k3 k2 − k4 ... k2 − kn
... ... ... ... ...
kn−1 − kn

The sum of the ﬁrst row is the weight of the bundle E → CP1, i. e.

τ (E) =
 n∑

i=1(k1 − ki) = nk1 − c1(E) (7.1)

The sum of all elements of this diagram is equal to the reduced dimension
of the deformation space of the complex structures of the bundle E. From
(7.1) it follows:
 37

1) The higher partial index of RHTP equals k1 = τ (E)
n + c1(E)
n and therefore
the sum of the normalized weight and normalized Chern number of the vector
bundle E is an integer.
2) If E is a rank two vector bundle, then τ (E) = ν(E).
Theorem 7.1. Let E → CP
1 be a rank three vector bundle. Then the
splitting type of E is given by

k1 = 1
3 (c1(E) + τ (E)),

k2 = 1
3 c1(E) − 2
3 τ (E)) + 1
2 ν(E),

k3 = 1
3 (c1(E) + τ (E)) − 1
2 ν(E).

Theorem 7.2. Let E → CP1 be a rank two vector bundle. Then

k1 = 1
2(c1(E) + ν(E)),

k2 = 1
2 (c1(E) − ν(E)).

References

[An-Bl] D.V.Anosov, A.A.Bolibruch. The Rieman-Hilbert problem.Aspects
of Mathematics,Vieweg,Brauschweig,Wiesbaden,1994.

[Ar-Il] V.I.Arnold, Yu.S.Il’yashenko.Ordinary diﬀerential equations, in the
book: Dynamical system I, Encyclopaedia of the Mathematical sci-
ences, 1, Springer, 1988.

[At-Bot] M. Atiyah, R. Bott. The Yang-Mills equations over Riemann sur-
face. Phil. Trans. R. Soc. London, 1982, A308, p. 523-615.

[Boj1] B. Bojarski. Stability of the Hilbert problem for a holomorphic vec-
tor. Bull. Acad. Sci. Georgia, 1958, vol. 21, p.391-398.

[Boj2] B. Bojarski. Connections between Complex Analytical and Geo-
metrical Aspects of the Riemann-Hilbert transmission Problem.
In Book “Complex Analysis. Methods, Applications.” Berlin, A.V.
1983
 38

[Boj3] B. Bojarski. Analysis of the boundary problem via function theory.
In “Investigation on modern problems of the function theory of
complex variables.” Moscow, 1960.

[Bl1] A. Bolibruch. Riemann-Hilbert problem. Usp. Mat. Nauk, 1990,
vol. 45, N2, p. 3-47.

[Bl2] A. Bolibruch. Mat. Zam. 1990, vol. 48, N5, p. 22-34.

[Bl3] A.Bolibruch Vector bundle associaced with monodromies and asym-
totics of Fuchsian systems. Journal of Dynamical and control sys-
tems.1996,vol.1,No. 2, pp.229-252.

[D] W. Dekkers. Moduli spaces for pairs of 2×2 matrix and for certain
connections on CP1. 1976, Meppel,Krips repro.

[Gi] G. Giorgadze. Factorization problem and a moduli space of the
holomorphic vector bundles on the Riemann surface. Ph. D. Thesis.
Steklov Mathematical Institute Moscow, 1992.

[Go] V.A.Golubeva.Reconstruction of a Pfaﬀ system of Fuchs type from
the generators of the monodromy group. Math.USSR-Izv. 1981, No
17, pp.227-241.

[Kh] G. N. Khimshiashvili. Lie groups and transmission problems on
Riemann surface. Contemp. Math. 1992, vol. 131, pp.164-178.

[Kohn] Treibich A. Kohn. Un result de Plemelj, Progress in Mathem.
Birkh¨auser, 1983, vol. 37.

[Kohno] T. Kohno. Monodromy representations of braid groups and Yang-
Baxter equations. Ann. Inst. Fourier, Grenoble. 1987, vol.37,
pp.134-160.

[LD] I. Lappo-Danilevskii. Memoires sur la theorie des systemes des
equations diﬀeretielles lineres,Chelsea, New-York,1953.

[Le] H. M. Levelt. Hypergeometric functions. Proc. Koninkl. Nether-
lands Acad. Wet., Ser. A, Math.Sci. 1961, vol.64, p.361-401.

39

[Lek1] V.P.Leksin.Meromorphic Pfaﬃan systems on complex projective
spaces,Math.USSR-Sb.1987, Vol.57, pp.211-227.

[Lek2] V.P.Leksin. Math.USSR-Zam.1991, Vol.50, No.2, pp.89-97.

[Mum] D. Mumford. Geometric invariant theory. Berlin, Springer-Verlag.

[Mus] N. I. Muskhelishvili. Singular integral equations. Noordhoﬀ,
Groningen, 1953.

[N-S] M. Narasimhan, C. Seshadri. Holomoirphic vector bundles on a
compact Riemann surface. Math.Ann. 1964, vol.55, p.69-80.

[O] M. Ohtsuki. On the number of apparent singularites of a linear
diﬀerential equation. Tokyo J. Math. 1982,vol.5, N1, p.23-29.

[Rod] Yu.L.Rodin. The Riemannboundary problem on Riemann surface.
D.Riedel Publ.Com. 1988.

[Roh] H. R¨ohrl. Holomorphic vector bundles over Riemann surfaces. Bull.
Amer. Math.Soc. 1962, vol.68, N3, p.125-160.

[S-M-J] M. Sato, T. Miwa, M. Jimbo. Holonomic quantum ﬁeld theory. Pub.
RIMS, Kyoto universty. 1978, vol. 14, pp. 223-267.

[V] N.P.Vekua. The system of singular integral equations.

[We] A. Weil. Generalization de fonctions abeliannes. J. Math. Pure
Appl., 1938, vol.17, p.47-87.

[Wi] E.Witten. Topological quantum ﬁeld theory. Comm. Math. Phys.
1988, vol. 117, pp. 353-386.

Institute of Cybernetics
Georgian Academy of Sciences
Sandro Euli st. 5
Tbilisi 380086
Republic of Georgia
email: giorgadze@rmi.acnet.ge
 40
