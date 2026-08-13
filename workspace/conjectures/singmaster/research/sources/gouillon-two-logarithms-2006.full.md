<!-- source: https://jtnb.centre-mersenne.org/item/10.5802/jtnb.537.pdf | converted from PDF -->

Nicolas GOUILLON

Explicit lower bounds for linear forms in two logarithms
Tome 18, no 1 (2006), p. 125-146.

<http://jtnb.cedram.org/item?id=JTNB_2006__18_1_125_0>

© Université Bordeaux 1, 2006, tous droits réservés.

L’accès aux articles de la revue « Journal de Théorie des Nom-
bres de Bordeaux » (http://jtnb.cedram.org/), implique l’accord
avec les conditions générales d’utilisation (http://jtnb.cedram.
org/legal/). Toute reproduction en tout ou partie cet article sous
quelque forme que ce soit pour tout usage autre que l’utilisation à
ﬁn strictement personnelle du copiste est constitutive d’une infrac-
tion pénale. Toute copie ou impression de ce ﬁchier doit contenir la
présente mention de copyright.

cedram
 Article mis en ligne dans le cadre du
Centre de diffusion des revues académiques de mathématiques
http://www.cedram.org/

Journal de Théorie des Nombres
de Bordeaux 18 (2006), 125-146

Explicit lower bounds for linear forms in two
logarithms

par Nicolas GOUILLON

Résumé. Nous donnons une minoration explicite pour les formes
linéaires en deux logarithmes. Pour cela nous spécialisons la mé-
thode de Schneider avec multiplicité décrite dans [10]. Nous amé-
liorons substantiellement les constantes numériques intervenant
dans les énoncés existants pour le cas de deux logarithmes, ob-
tenus avec la méthode de Baker ou bien celle de Schneider avec
multiplicité. Notre constante est de l’ordre de 5.104 au lieu de 108.

Abstract. We give an explicit lower bound for linear forms
in two logarithms. For this we specialize the so-called Schneider
method with multiplicity described in [10]. We substantially im-
prove the numerical constants involved in existing statements for
linear forms in two logarithms, obtained from Baker’s method
or Schneider’s method with multiplicity. Our constant is around
5.104 instead of 108.
 1. Introduction

Our goal is to give explicit lower bounds for linear forms in two loga-
rithms with numerical coeﬃcients as small as possible. To this end we intend
to specify in the case of linear forms in two logarithms the most general
works of [9] and [10] on linear forms in n logarithms. Our method combines
the use of interpolation determinants with that of Shneider’s method with
multiplicity. This last method can be seen as the dual of Baker’s method
(see [9] for duality). Our work is situated between those of [5] which study
linear forms in two logarithms with Schneider’s classical method and those
of [10] which use Schneider’s method with multiplicity. The interest of the
method used here is to provide the same type of lower bound as Baker’s
method [1] but with smaller numerical coeﬃcients. We improve the exist-
ing results : for example the essential constant of Corollary 9.22 in [10]
is greater than 5.108 in the case of two logarithms. Here we reduce this
value to under 6.104. Let us note that the works using Baker’s method
furnish a constant around 108 in the case of two logarithms (Corollary 3 of

Manuscrit reçu le 11 mars 2004.

126 Nicolas Gouillon

[7]). The improvements obtained in this paper result from two important
points. First we use a multiplicity estimate whose proof is reminiscent of
the original method by D.W. Masser [6] and which appears in our case
to be more eﬃcient than the general statements previously employed. Sec-
ondly we have studied precisely the numerical constraints connecting the
parameters of Theorem 2.1 below.
The plan of this paper is the following. We give our results in section 2.
All of them follow from Theorem 2.1 which is our main result. The zero
estimate used in the proof of main theorem is proved in section 3. The
section 4 is devoted to the proof of Theorem 2.1. Finally we prove the
corollaries in section 5.
The author gratefully acknowledges the many helpful suggestions of M.
Laurent during the preparation of the paper.

2. Statements of the results

Let α1 and α2 be two non zero complex algebraic numbers and let log α1
and log α2 be any nonzero determinations of their logarithms. Our aim is
to obtain lower bounds for the absolute value of the linear form :

Λ = b1 log α1 − b2 log α2,

with b1 and b2 two nonzero relative integers.
For any algebraic number α of degree d over Q and whose minimal poly-
nomial over Z is written as a ∏d
i=1(X−α(i)) where the roots α(i) are complex
numbers, let us denote by

h(α) = 1
d
 (

log |a| +
 d∑

i=1 log max(1, |α(i)|)

)

the usual absolute logarithmic height of α. We put

D = [Q(α1, α2) : Q]/[R(α1, α2) : R].

Our main result is the following.

Theorem 2.1. Let K and L be integers ≥ 1, let T1, T2, T3 , R1, R2, R3,
S1, S2 and S3 be integers ≥ 0. Let E be a real number ≥ e. We set

R = R1 + R2 + R3, S = S1 + S2 + S3, T = T1 + T2 + T3.

So we put
 N = (K + 1)(K + 2)
2 (L + 1), B = R|b2| + S|b1|
2K
and denote by g, ω, ω0 real numbers which satisfy the lower bounds :

g ≥ 1
4 − N
12(R + 1)(S + 1)(T + 1) , ω ≥ 1 − N
2(R + 1)(S + 1)(T + 1) ,

Explicit lower bounds for linear forms in two logarithms 127

ω0 ≥ 2(R + 1)(S + 1)(T + 1)
N .

Let a1, a2 be positive real numbers so that

ai ≥ E| log αi| − log |αi| + 2Dh(αi), i = 1, 2.

Suppose that
 T1 ≥ K,

Card {rb2 + sb1; 0 ≤ r ≤ R1, 0 ≤ s ≤ S1} ≥ K + 1,

(T1 + 1)Card {αr
1αs
2; 0 ≤ r ≤ R1, 0 ≤ s ≤ S1} ≥ L + 1,

(T2 + 1)Card {αr
1αs
2; 0 ≤ r ≤ R2, 0 ≤ s ≤ S2} ≥ 2KL + 1, (1)

(T2 + 1)Card {rb2 + sb1; 0 ≤ r ≤ R2, 0 ≤ s ≤ S2} ≥ K2 + 1,

(T3 + 1)Card {(rb2 + sb1, αr
1αs
2); 0 ≤ r ≤ R3, 0 ≤ s ≤ S3} ≥ 3K2L + 1.

Suppose moreover that

V
2 > D [
log( N
2 ) + K
3 log ( Rb2 + Sb1
2K
 ) + 1454K
927 + K
3 log ( T
KL
 )

+1 + (ωT + ω0) log ( 107(K + 3)L
309ωT
 ) + 2ωT + ω0
]
(2)
 +T log E + K
3 log E + log 2 + g L + 1
2 ((R + 1)a1 + (S + 1)a2),

where
 V = 1
4
 

1 − 1
L + 1 +
 √
1 − 2
L + 1
 

 (K + 2)(L + 1) log E.

Then we have

|Λ′| ≥ e
−V , with Λ′ = Λ · max
 { LSeLS|Λ|/(2b2)

2b2 , LReLR|Λ|/(2b1)

2b1
 }
 .

Now we give three corollaries of Theorem 2.1 in the case where α1 and
α2 are multiplicatively independent. We put

b = b1
D log A2 + b2
D log A1 ,

with A1, A2 real numbers > 1 so that

log Ai ≥ max {h(αi), | log αi|
D , 1
D
 } , (i = 1, 2).

128 Nicolas Gouillon

Corollary 2.2. Suppose that α1 and α2 are multiplicatively independent.
Then

log |Λ| ≥ −9400 (3.317 + 1.888
D + 0.946 log D) D4h log A1 log A2,

with
 h = max {log b + 3.1, 1000
D , 498 + 284
D + 142 log D} .

Corollary 2.3. Suppose moreover that α1 and α2 are real numbers > 0.
Then

log |Λ| ≥ −7200 (3.409 + 1.705
D + 0.946 log D) D4h log A1 log A2,

with
 h = max {log b + 3.1, 1000
D , 512 + 256
D + 142 log D} .

Corollary 2.4. Suppose that the determinations chosen for log α1 and
log α2 are positive real numbers and are linearly independent over Q. Put

E = 1 + min { D log A1
log α1 , D log A2
log α2
 } ≥ 2,

log E∗ = max { log E
D , log E
D + 0.946 log D
log log E + 3.965} ,

h = max {log b + log(E) − log log(E) − 2.27, 265 log(E)
D , 150 log E∗} .

Suppose moreover that E ≤ min{A
D/2
1 , AD/3
2 }, then

log |Λ| ≥ −8550D4h log A1 log A2 log(E∗)(log E)
−3.

The choice of the above constant 1000 (respectively 265) in the def-
inition of the parameter h in Corollaries 2.2 and 2.3 (respectively 2.4) is
arbitrary. The other numerical constants in these corollaries depend on this
choice. We note that the multiplicative constants are decreasing functions
in the variable b. Asymptoticaly (when b tends to inﬁnity) the multiplica-
tive constants of Corollaries 2.2, 2.3 and 2.4 are respectively around of 8800,
6800 and 8450. If we compare our results with those obtained from Baker’s
method as in [7] Corollary 2, or from Schneider’s method with multiplicity
as in [10] Corollary 9.22, we notice that they are better. Our constants
are roughly equal to the square root of corresponding constants in [7] and
[10]. We can also compare Corollaries 2.2 and 2.3 (resp. 2.4) with Corol-
laries 1 and 2 (resp. 3) in [5]. In this case we note that the lower bounds
given in Corollaries 2.2 and 2.3 (resp. 2.4) are more eﬃcient only if we have
approximatively log b ≥ 3000 log eD (resp. log b ≥ 3200 log E∗).

Explicit lower bounds for linear forms in two logarithms 129

3. Multiplicity estimate

An important point of the proof is an improvement of multiplicity esti-
mate used. In our case we work with the product group Cm × C× whose
group law is written additively. For any element w in C× and any ele-
ment (v0, . . . , vm−1) in Cm we denote brieﬂy (v, w) = (v0, . . . , vm−1, w) ∈
Cm × C×. Let D := ∂
∂X0 + Y ∂
∂Y a derivation operating on the poly-
nomial’s ring C[X, Y ]. Let T be an integer ≥ 0, we say that a polyno-
mial P ∈ C[X, Y ] vanishes to order > T with respect to D on the set
Σ ⊆ Cm × C×, if for any integer 0 ≤ t ≤ T , DtP vanishes identically on
Σ. This condition meaning that P ≡ 0 on Σ when t = 0. We give here a
reﬁnement of the zero estimate of [2] by replacing in condition (2) the term
Card ( Σj
W ×{µ}
 ) by Card ( Σj
W ×{1}
 ).

Theorem 3.1. Let K, L, m be integers ≥ 1, let T1, . . . , Tm+1 be integers
≥ 0 and let Σ1, . . . , Σm+1 be nonempty ﬁnite sets of Cm × C×. Assume that
the following conditions hold.
(1) For all j = 1, . . . , m, and any vector subspace W of Cm with dimension
≤ m − j, we have
( Tj +1
εj
 ) Card ( Σj
W × C×
 ) > Kj, where εj = { 1 if (1, 0, . . . , 0) /∈ W
0 otherwise.

(2) For all j = 1, . . . , m + 1, and any vector subspace W of Cm with di-
mension ≤ m + 1 − j, we have

(Tj +1)Card ( Σj
W × {1}
 ) > jKj−1L.

Then any polynomial P ∈ C[X, Y ] of total degree ≤ K in X and of degree
≤ L in Y which vanishes on Σ1 + · · · + Σm+1 to order > T1 + · · · + Tm+1
with respect to D is identically zero.

Proof. We argue as in the proof of Theorem 1 in [2] with a reﬁnement in
case iii. In this case we use the inequality δr−1,1(V ) ≥ Card (µ) instead of
δr−1,1(V ) ≥ 1. Indeed since HV = W × µ where µ ⊆ C× is ﬁnite we have

Card (V ∩ (Lr−1 × P1)) ≥ Card (( ˜V ∩ Lr−1) × (µ ∩ P1)) ≥ Card (µ).

Then we deduce
 Card (µ)Card ( Σj
HV
 ) (Tj + 1) ≤ jKj−1L.

Observe ﬁnally that

Card ( Σj
W × µ
 ) ≥ Card ( Σj
W × {1}
 ) /Card (µ),

130 Nicolas Gouillon

we obtain the inequality

Card (µ) Card ( Σj
W ×{1}
 )

Card (µ) ≤ jKj−1L

which contradicts condition (2) of Theorem 3.1. □

4. Proof of Theorem 2.1

Without loss of generality we may assume |α1| ≥ 1, |α2| ≥ 1 and b1 ≥ 1,
b2 ≥ 1 (see [5] for more details). The proof combines the approachs of [5]
and [10] using interpolation determinants as in [4]. For this we introduce
the matrix M whose coeﬃcients are

γr,s,t
k0,k1,l = (rb2 + sb1)
k1lt−k0 ( t
k0
)

αrl
1 αsl
2 ,

where (r, s, t) with (0 ≤ t ≤ T, 0 ≤ r ≤ R, 0 ≤ s ≤ S) is the column
index, while (k0, k1, l) with (k0 + k1 ≤ K, 0 ≤ l ≤ L) is the row index. The
sketch of proof is the usual one : we use a zero estimate to show that the
matrix M has maximal rank, we take a maximal square submatrix with
non-vanishing determinant ∆, we produce a lower bound for |∆| by means
of Liouville’s estimate and an upper bound by means of Schwarz’s Lemma,
and the conclusion follows.

4.1. Rank of M . The following lemma implies that M has maximal rank.

Lemma 4.1. Under condition (1) of Theorem 2.1 the matrix M has max-
imal rank equal to N .

Proof. The coeﬃcients of M are the values of the monomials

D
t ( X k0
0
k0! X k1
1 Y l)

evaluated at the points (0, rb2 + sb1, αr
1αs
2), (0 ≤ r ≤ R, 0 ≤ s ≤ S). So if
the N rows of M are lineary dependent there exists a nonzero polynomial
P ∈ C[X0, X1, Y ] of total degree ≤ K in X and of degree ≤ L in Y which
vanishes at the points (0, rb2 + sb1, αr
1αs
2), 0 ≤ r ≤ R, 0 ≤ s ≤ S, to order
> T with respect to D. Then Theorem 3.1 furnishes a contradiction. □

4.2. Transformation of M . To obtain the lower bound announced we
must modify the matrix M . Indeed if we work directly with M we obtain
an extra term log log b in the lower bound of corollaries. To this end we
deﬁne for any z ∈ C and any n ∈ N the function △ by

△ (z; n) = z(z − 1) · · · (z − n + 1)
n! ,

Explicit lower bounds for linear forms in two logarithms 131

with for n = 0 △ (z; 0) = 1.

For any a ∈ N and any b ∈ N∗ we deﬁne the polynomial δb(z; a) ∈ Q[z] of
degree a by δb(z; a) =△ (z; b)
q △ (z; r),

where by Euclidean division a = bq + r. For any integer c ≥ 0 we denote
furthermore
 δb(z; a, c) = ( d
dz
 )c δb(z; a).

For any positive integer n, let us denote by ν(n) the least common multiple
of 1, 2, . . . , n. Let now ˜M be the matrix with the coeﬃcients

˜γr,s,t
k0,k1,l =△ (rb2 + sb1; k1)ν(T ′)
k0 δT ′(l; t, k0)
k0! αrl
1 αsl
2 ,

where T ′ is a parameter which will be chosen later. We deduce ˜M from M
by linear combinations on rows and columns. The diﬃculty is to prove that
if we replace lt−k0 by δT ′(l; t, k0) we do not change the rank of M . This is
achevied by

Lemma 4.2. Let T ∈ N∗ and let {δ(z; t); 0 ≤ t ≤ T } be a basis in C[z]
of the space of the polynomials of degree ≤ T . Let Q ∈ GLT +1(C) be the
matrix deﬁned by
 (1, z, . . . , zT )Q = (δ(z; 0), . . . , δ(z; T )).

We recall furthermore
δ(l; t, i) =
 (( d
dz
 )i δ(z; t)

)

z=l .

Then for any l ∈ N, any k ∈ N and any 0 ≤ t ≤ T , we have

δ(l; t, k)
k! =
 T∑

ν=0 qν,t
(
ν
k
)

lν−k, (4.1)

where the qν,t are the coeﬃcients of Q.

Proof. Notice that we have for all k ∈ N
( d
dz
 )k (1, z, . . . , zT )Q = ( d
dz
 )k (δ(z; 0), . . . , δ(z; T )).
 □

Then as in paragraph 9.2.2 of [10] it is easy to prove that M and ˜M have
the same rank.

132 Nicolas Gouillon

4.3. Arithmetical lower bounds for the minors of ˜M . To prove the
main Lemma 4.6 below, we give here three technical Lemmas. First we state
Lemmas 4.3 and 4.4 whose proofs are omitted (see the appendix of [3] for
details).

Lemma 4.3. Let K be an integer ≥ 1. We have the upper bound

log
 





 ∏

(k0,k1)∈N2
k0+k1≤K
 1
k0!
 




 ≤ (− K
3 (K + 1)(K + 2)
2
 ) log(K)

+ 11
18 K (K + 1)(K + 2)
2 .

Lemma 4.4. Let N be an integer ≥ 1 and let R, S, T be integers ≥ 0
verifying (R + 1)(S + 1)(T + 1) ≥ N . Let (t1, . . . , tN ) be a sequence of
integers between 0 and T with each value appearing at most (R + 1)(S + 1)
times. Then we have

N∑

i=1 ti ≤ N T − N 2

2(R + 1)(S + 1) + 2T (R + 1)(S + 1) − N
2 .

Lemma 4.5. Let T and T ′ be two integers so that 0 < T ′ < T . Let (tk0,k1,l)
be a sequence of N integers between 0 and T which is indexed by the triplets
(k0, k1, l) where 0 ≤ k0 + k1 ≤ K and 0 ≤ l ≤ L. Assume that each tk0,k1,l
appears at most (R + 1)(S + 1) times. Then we have

log
 

 L∏

l=0
 ∏

k0+k1≤K
 ∣
∣
∣
∣ 1
k0! δT ′(l; tk0,k1,l, k0)
∣
∣
∣
∣




≤ KN
3 log T
KL + 11
18 KN + (ωT + ω0 + T ′)N

+ (ωT + ω0)N log max{L, T ′ − 1}
T ′

with ω and ω0 deﬁned in Theorem 2.1.

Proof. Using the estimate 1
b!qr! ≤ 1
ba e
a+b,

we obtain for any l ∈ N,

|δb(l; a, c)| ≤ c!

(
a
c
)

|(l − b + 1)|
a−c 1
b!qr!

≤ c!

(
a
c
) max{l, b − 1}a−c

ba e
a+b.

Explicit lower bounds for linear forms in two logarithms 133

Then we have

(4.3) ∣
∣
∣
∣ 1
k0! δT ′(l; tk0,k1,l, k0)
∣
∣
∣
∣

≤
 (
tk0,k1,l
k0
 ) max{l, T ′ − 1}
tk0,k1,l−k0

T ′tk0,k1,l e
tk0,k1,l+T ′.

Then we bound trivialy in the right hand-side of (4.3) : (tk0,k1,l
k0 ) ≤ T k0
k0!
and l ≤ L. Thus we use Lemmas 4.3 and 4.4 to conclude. □

We give now the main lemma of this section. Let ∆ be a nonzero minor
of order N extracted of ˜M . For a suitable ordering of rows and columns in
∆ we can write

∆ = det
 (

△ (rjb2 + sjb1; k1,i) ν(T ′)k0,i

k0,i! δT ′(li; tj, k0,i)αrj li
1 αsj li
2
 )

1≤i,j≤N .

Lemma 4.6. Put
 g = 1
4 − N
12(R + 1)(S + 1)(T + 1) ,

G1 = N (L + 1)(R + 1)g
2 G2 = N (L + 1)(S + 1)g
2 ,

M1 = L(r1 + · · · + rN )
2 , M2 = L(s1 + · · · + sN )
2 .

Then we have the lower bound

log |∆| ≥ −(D − 1) [
log(N !) + KN
3 log ( Rb2 + Sb1
2K
 ) + 22KN
18

+ KN
3 log ( T
KL
 ) + (ωT + ω0)N log ( max{L, T ′ − 1}
T ′
 )

+ 107KN T ′

309 + (ωT + ω0 + T ′)N ] + (M1 + G1) log(|α1|)

+ (M2 + G2) log(|α2|) − 2DG1h(α1) − 2DG2h(α2).

Proof. We proceed along the same lines as Lemma 6 of [5]. Consider the
polynomial

P (X, Y ) = ∑

σ sgn(σ)
 N∏

i=1 △ (b2rσ(i) + b1sσ(i); k1,i)ν(T ′)
k0,i

× δT ′(li; tσ(i), k0,i)
k0,i! X lirσ(i)Y lisσ(i),

where σ runs over all permutations σ ∈ SN and where sgn(σ) means the
signature of the permutation σ. By expanding the determinant ∆, we get

134 Nicolas Gouillon

∆ = P (α1, α2). By multilinearity of determinant we can write for any η ∈ C
:
 P (z1, z2) = det
 ( (b2rj + b1sj − η)k1,i

k1,i! ν(T ′)k0,i

k0,i! δT ′(li; tj, k0,i)zlirj
1 zlisj
2
 )
 .

Choose η = (Rb2 + Sb1)/2. We bound ν(n) ≤ exp( 107n
103 ) (see [11], Lemma
2.3 p. 127). Then Lemma 4.5 implies the upper bound

L(P ) ≤ N ! ( Rb2 + Sb1
2K
 ) KN
3 ( T
KL
 ) KN
3 ( max{L, T ′ − 1}
T ′
 )(ωT +ω0)N

× exp [ 22KN
18 + 107KN T ′

309 + (ωT + ω0 + T ′)N ] .(4.2)

To get a good lower bound for |∆| we have to notice that P is divisible
by a large power of X and Y. More precisely we use the estimates

M1 − G1 ≤
 N∑

ν=1 lνrν ≤ G1 + M1, M2 − G2 ≤
 N∑

ν=1 lνsν ≤ G2 + M2,

which follow from Lemma 4 of [5] where to obtain G1 and M1 we replace
K by (K + 1)(K + 2)/2, L by L + 1, R by R + 1 and S by (S + 1)(T + 1).
Then we conclude in the same way as in the proof of Lemma 6 of [5]. □

4.4. Analytic upper bound for |∆|. As in [4] here is the crucial point
where the smallness of |Λ| is used.

Lemma 4.7. Let E be a real number ≥ e. Assume |Λ′| ≤ e−V and recall

V = 1
4
 

1 − 1
L + 1 +
 √
1 − 2
L + 1
 

 (K + 2)(L + 1) log E.

Then we have

log |∆| ≤ M1 log |α1| + M2 log |α2| + N log 2 − N V
2 + T N log E

+ log(N !) + KN
3 log ( Rb2 + Sb1
2K
 ) + 22KN
18 + KN
3 log E

+ KN
3 log ( T
KL
 ) + (ωT + ω0)N log ( max{L, T ′ − 1}
T ′
 )

+ 107KN T ′

309 + (ωT + ω0 + T ′)N + E(G1| log α1| + G2| log α2|).

Proof. We proceed in the same way as in Lemma 6 of [4]. First we center the
exponents li around their average value L/2. Next without loss of generality
we may assume b1 log α1 ≤ b2 log α2,

Explicit lower bounds for linear forms in two logarithms 135

so that Λ ≥ 0. Set β = b1/b2, then

log α2 = β log α1 + Λ
b2 .

Therefore using the above equality and (4.1) we expand ∆ to obtain :

∆ = αM1
1 αM2
2 ∑

(ν1,...,νN )∈NN

νj ≤T,1≤j≤N
 N∏

j=1 qνj ,tj ∑

I⊆{1,...,N }(Λ′)
N −|I|∆I,ν,

where |I| is the cardinality of I and

∆I,ν = det
 

 ci,1 . . . ci,N

θi,1ci,1 . . . θi,N ci,N
 


 } i ∈ I

} i /∈ I

with
 ci,j = bk1,i
2
k1,i! (rj + sjβ − η)
k1,iν(T ′)
k0,i( νj
k0,i
)

lνj −k0,i
i αλi(rj +sj β−η)
1

θi,j = eλisj Λ/b2 − 1
Λ′ , λi = li − L
2 .

We give now an upper bound for |∆I |. Let us consider the entire function
ΦI of the complex variable z deﬁned by

ΦI (z) = ∑

(ν1,...,νN )∈NN

νj ≤T,1≤j≤N
 N∏

k=1 qνj ,tj ΦI,ν(z),

where

ΦI,ν(z) = det
 




 ( ∂
∂z0
 )ν1 ϕi(zξ1), . . . , ( ∂
∂z0
 )νN ϕi(zξN )

θi,1 ( ∂
∂z0
 )ν1 ϕi(zξ1), . . . , θi,N ( ∂
∂z0
 )νN ϕi(zξN )
 




 } i ∈ I

} i /∈ I

with
 ϕi(z0, z1) = bk1,i
2
k1,i! zk1,i
1 ν(T ′)k0,i

k0,i! zk0,i
0 e
z0liαλiz1
1

and ξj = (ξ0,j, ξ1,j) = (0, rj + sjβ − η).

Notice that ΦI (1) = ∆I . Here is the key point of our argument.

136 Nicolas Gouillon

Lemma 4.8. For any set I ⊆ {1, . . . , N } of cardinality |I| and all N -tuples
(ν1, . . . , νN ), νi ≤ T (i = 1, . . . , N ), the function ΦI,ν(z) has a zero at the
origin with multiplicity

TI ≥ |I|
2
 ( |I| + 1
K + 1 − K
2 − 1) − T N.

Proof. We can write

ϕi(z0, z1) = pi(z0, z1)e
li(z0+z1 log α1)e
−(L/2)z1,

where
 pi(z0, z1) = bk1,i
2
k1,i
 ν(T ′)k0,i

k0,i zk0,i
0 zk1,i
1 ,

is a monomial of total degree ≤ K. By multilinearity we obtain

ΦI,ν(z) = exp
 

− Lz
2
 N∑

j=1 ξ1,j


 ˜ΦI,ν(z),

where

˜ΦI,ν(z) = det
 




 ( ∂
∂z0
 )ν1 φi(zξ1), . . . , ( ∂
∂z0
 )νN φi(zξN )

θi,1 ( ∂
∂z0
 )ν1 φi(zξ1), . . . , θi,N ( ∂
∂z0
 )νN φi(zξN )
 




 } i ∈ I

} i /∈ I

with φi = pi(z0, z1)e
li(z0+z1 log α1), i = 1, . . . , N.

We apply Lemma 9.14 of [10] and next Lemma 7.3 of [10] to the function
˜ΦI,µ(z) to conclude. □

Then it follows that the function ΦI (z) has a zero at the origin with
multiplicity ≥ TI . Hence usual Schwarz Lemma implies

|∆I |1 ≤ E−TI |∆I |E. (4.4)

Now we give an upper bound for |ΦI (z)|.

Lemma 4.9. For any set I ⊆ {1, . . . , N } and any complex number z so
that |z| > 1 we have

|ΦI (z)| ≤ N ! ( Rb2 + Sb1
2K
 ) KN
3 ( T
KL
 ) KN
3 ( max{L, T ′ − 1}
T ′
 )(ωT +ω0)N

× exp [ 22KN
18 + (ωT + ω0 + T ′)N + 107KN T ′

309
 ]

× |z| KN
3 exp(|z|(G1| log α1| + G2| log α2|).

Explicit lower bounds for linear forms in two logarithms 137

Proof. From equality (4.1) we have for all 1 ≤ j ≤ N and all i ∈ I

T∑

ν=0 qν,tj
 ( ∂
∂z0
 )ν ϕi(zξj) = bk1,i
2
k1,i! (zξ1,j)
k1,iν(T ′)
k0,i δT ′(li; tj, k0,i)
k0,i! αλi(zξ1,j )
1 .

Then since |θi,j| ≤ 1, for all 1 ≤ i, j ≤ N , it follows that

|ΦI (z)| ≤ ∑

σ sg(σ)

∣
∣
∣
∣
∣
 N∏

i=1 αz ∑
λiξ1,σ(i)
1 (zb2ξ1,σ(i))k1,i

k1,i! ν(T ′)k0,i

k0,i! δT ′(li; tσ(i), k0,i)

∣
∣
∣
∣
∣ ,

where σ runs over all permutations σ ∈ SN . Therefore

|∆I (z)| ≤ L(P ) ∣
∣
∣
∣αz ∑ λiξ1,σ(i)
1
 ∣
∣
∣
∣ |z| KN
3 . (4.5)

Hence the same arguments as in Lemma 8 of [4] implie that
∣
∣
∣
∣α∑ λiξ1,σ(i)
1
 ∣
∣
∣
∣ ≤ exp(|z|(G1| log α1| + G2| log α2|)). (4.6)

Combining (4.5), (4.6) and (4.2) we conclude immediately. □

Now we restart from (4.4) and we combine Lemma 4.8 and Lemma 4.9
applied with |z| ≤ E to obtain

|∆| ≤ ∣
∣
∣αM1
1 ∣
∣
∣ ∣
∣
∣αM2
2 ∣
∣
∣ 2N L(P )E K
3 e
E(G1| log α1|+G2| log α2|) max
I
 {
|Λ′|
N −|I|E−TI } .

We recall that |Λ′| ≤ e−V . So we maximize in function of |I| the expression

−(N − |I|)V − TI log E.

This maximum over R is reached for

|I| = ( V
log E + K + 2
4 − 1
2(K + 1)
 ) (K + 1).

Then since

V = 1
4
 (

1 − 1
(L + 1) +
 √
1 − 2
(L + 1)
 )
 (K + 2)(L + 1) log E

we have
 log max
I {−(N − |I|)V − TI log E} ≤ − N V
2 + T N log E.

This ﬁnishes the proof. □

138 Nicolas Gouillon

4.5. Conclusion. Choose

T ′ = [ 309ωT
(309 + 107K)
 ] + 1

and observe that N ! ≤ ( N
2
 )N for N ≥ 6 and that

log ( L
T ′
 ) ≤ log ( 107(K + 3)L
309ωT
 ) .

Then from Lemma 4.6 and 4.7 we obtain
V
2 ≤ D [
log( N
2 ) + K
3 log ( Rb2 + Sb1
2K
 ) + 22K
18 + 107K
309 + 1

+ K
3 log ( T
KL
 ) + (ωT + ω0) log ( 107(K + 3)L
309ωT
 ) + 2ωT + ω0
]

+ T log E + K
3 log E + log 2 + g L + 1
2 ((R + 1)a1 + (S + 1)a2).

This inequality contradicts hypothesis (2) of Theorem 2.1 therefore |Λ′| ≥
e−V .
 5. Proof of corollaries

In this section we assume that α1 and α2 are multiplicatively indepen-
dent. Our goal is to give a lower bound for |Λ|. To this end we specialize,
as in [5], a part of the parameters involved in Theorem 2.1. We recall the
notations log E = λ and N = (K+2)(K+1)(L+1)
2 . Fix

g = 0.241 , ω = 0.946, ω0 = 20 and γ = 1.309.

5.1. Choices of parameters. Let c0 and c1 be positive real numbers
which will be speciﬁed later. Set :

K = [c0a1a2D log E∗λ−3] , (5.1)

L = [c1Dhλ−1] , (5.2)

R1 = [√K + 1
√ a2
a1
 ] , (5.3a)

R2 =
 [

max
{ 21/3

(K + 1)1/3 , 1
(L + 1)1/3

}

(K + 1)
2/3 (2γD log E∗)1/331/3

g1/3(a1a2)1/6
 √ a2
a1
 ]
,

(5.3b)

R3 =
 [
(K + 1)
2/3 (2γD log E∗)1/331/3

g1/3(a1a2)1/6
 √ a2
a1
 ]
 , (5.3c)

S1 = [√K + 1
√ a1
a2
 ] , (5.4a)

Explicit lower bounds for linear forms in two logarithms 139

S2 =
 [

max
{ 21/3

(K + 1)1/3 , 1
(L + 1)1/3

}

(K + 1)
2/3 (2γD log E∗)1/331/3

g1/3(a1a2)1/6
 √ a1
a2
 ]
,

(5.4b)

S3 =
 [
(K + 1)
2/3 (2γD log E∗)1/331/3

g1/3(a1a2)1/6
 √ a1
a2
 ]
 , (5.4c)

T1 = max {[ L + 1
K + 1
 ] , K} , (5.5a)

T2 =
 [ g2/3(L + 1)(a1a2)1/3(K + 1)2/3

(2γD log E∗)2/3 max
 { 21/3

(K + 1)1/3 , 1
(L + 1)1/3
 }]
 ,

(5.5b)

T3 =
 [ g2/3(L + 1)(a1a2)1/331/3(K + 1)2/3

(2γD log E∗)2/3
 ]
 . (5.5c)

We give now some conditions on the parameters c0, c1, λ, a1, a2, h and E∗.
We need these to obtain Corollaries 2.2, 2.3 et 2.4 :

λ ≥ 1, (5.6)

ai ≥ max{3, 3λ, E| log αi| − log |αi| + 2Dh(αi), (i = 1, 2). (5.7)

log E∗ ≥ max { λ
D , λ
D + 2.101 − ω log λ + ω
3 log c0 + ω log D} , (5.8)

h ≥ max {4, 265λ
D , 150 log E∗} , (5.9)

h ≥ log ( b1
a2 + b2
a1
 ) + log(λ) + λ
D + 2.72, (5.10)

5000 ≥ c0 ≥ 300, (5.11)

c1 ≥ 5.1. (5.12)

We deduce from (5.7), (5.8), (5.9), (5.11) and (5.12) that :

K + 1 ≥ 2700 and L + 1 ≥ 1350. (5.13)

From (5.8) and (5.11) we obtain

log E∗ ≥ λ
D + 3.898 − ω log λ + ω log D ≥ 4.84. (5.14)

These choices enable us to show that the values chosen for g, ω, ω0 in
this section are upper bound for respectively 1
4 − N
12(R+1)(S+1)(T +1) , 1 −

N
2(R+1)(S+1)(T +1) and 2(R+1)(S+1)(T +1)
N . The computations are tedious but
elementary (see [3] for details).

Remark. The signiﬁcant hypotheses are (5.8) and (5.10).

140 Nicolas Gouillon

Remark. The numerical constants contained in the above conditions implie
the three corollaries and can be changed to other applications.

5.2. Lower bound for |Λ|. We assume here that the numbers rb2 + sb1
(0 ≤ r ≤ R, 0 ≤ s ≤ S) are pairwise distinct. If this last condition is not
satisﬁed, Liouville’s inequality furnishes a much better lower bound for |Λ|
than the one which is required.

5.2.1. Study of condition (1) of Theorem 2.1. Since all the numbers rb1 +
sb2, (0 ≤ r ≤ R, 0 ≤ s ≤ S) are pairwise distinct, condition (1) of Theorem
2.1 can be written T1 ≥ K, (5.15a)

(R1 + 1)(S1 + 1) ≥ max {K + 1, L + 1
T1 + 1
 } = K + 1, (5.15b)

(R2 + 1)(S2 + 1) ≥ max
 { K2 + 1
T2 + 1 , 2KL + 1
T2 + 1
 }

, (5.15c)

(R3 + 1)(S3 + 1) ≥ 3K2L + 1
T3 + 1 , (5.15d).

This inequality are clearly veriﬁed with our above choices.

5.2.2. Study of condition (2). In this section we show, under conditions
(5.6) − (5.17) that condition (2) of Theorem 2.1 is implied by condition (2′)
given at the end of paragraph. To prove this we use the following Lemmas
5.1 and 5.2. Put
 B = Rb2 + Sb1
2K .

Lemma 5.1. Under the hypotheses (5.7) − (5.13) we have

log B + 1454
309 + λ
D + 6
K log ( K + 2
2
 ) + log ( T
KL
 ) ≤ h.

Proof. First we deduce from (5.1) and (5.3) that

R
K = R
K + 1 (1 + 1
K )

≤ λ
a1 (1 + 1
K )
 ( 1
√c0D log E∗λ−1 + (2γ)1/3

c
1/3
0 g1/3
 (31/3 + 1
Γ1/3
 ))
 ,

where
 Γ = min { K + 1
2 , L + 1
} .

Then (5.8), (5.11) and (5.13) implie :

R
K ≤ 0.566 λ
a1 , et S
K ≤ 0.566 λ
a2 ,

Explicit lower bounds for linear forms in two logarithms 141

hence that
 log B ≤ log ( b2
a1 + b1
a2
 ) + log λ − 1.26. (5.16)

Now from (5.5), (5.6), (5.11) and (5.13) we obtain the upper bound

T
KL ≤ 0.475. (5.17)

Then combining (5.16), (5.17) and (5.13) we deduce our claim. □

Lemma 5.2. Under the same hypotheses (5.7) − (5.13) we have the upper
bound

T (λ + Dω (2 + log 107(K + 3)L
309ωT
 )) + g(L + 1)
2 ((R + 1)a1 + (S + 1)a2)

≤ Φ + γD log E∗ L + 1
K + 1
where

Φ = Dγ log E∗K + g(L + 1)
√(K + 1)a1a2 + g(L + 1)(a1 + a2)
2

+ 3g2/3(γa1a2D log E∗)1/3

22/3 (L + 1)(K + 1)
2/3 (31/3 + 1
Γ1/3
 ) .

Proof. First we notice that we have by (5.5), (5.11) and (5.13)

(K + 3)L
T ≤ K + 3
K + 1 (K + 1)(L + 1)
T ≤ 3.404c
1/3
0 D log E∗

λ .

Therefore combining this upper bound and (5.8), (5.14) we deduce

λ
D + 2ω + ω log ( 107(K + 3)L
309ωT
 ) ≤ (1 + ω log log E∗

log E∗
 ) log E∗ ≤ γ log E∗.

Hence Lemma 5.2 follows easily from the estimate

DT γ log E∗ + g(L + 1)
2 ((R + 1)a1 + (S + 1)a2) ≤ Φ + γD log E∗ L + 1
K + 1

which is obtained by (5.3) − (5.5) (see [3] for details). □

Let us denote
 θ = 1
8
 

1 − 1
L + 1 +
 √
1 − 2
L + 1
 

 ,

so that V
2 = θ(K + 2)(L + 1)λ.

142 Nicolas Gouillon

Notice that log(N/2) ≤ 2 log((K + 2)/2) + log(L + 1), then Lemmas 5.1
and 5.2 show that condition (2) of Theorem 2.1 is implied by

θ(K + 1)(L + 1)λ ≥ D(K + 1)h
3 + Φ + Ω, (5.18)

where
 Ω = −θ(L + 1)λ − Dh
3 + Dω0
 (1 + log 107(K + 3)L
309ωT
 )

+ D log(L + 1) + Dγ log E∗ L + 1
K + 1 + log 2 + D.

First we give an upper bound for Ω. Put

Ω1 = −θ(L + 1)λ + log 2 + D + γ(L + 1)λ
2700 + D log(c1h) + 8 · 10−4D,

Ω2 = − Dh
3 + Dω0
 (1 + log 107(K + 3)L
309ωT
 ) + D log D.

It is easily seen that Ω ≤ Ω1 + Ω2. Remark θ ≥ 0.249 we easily verify that
Ω1 is a decreasing function in the variable c1h. Then we deduce Ω1 < 0
from (5.9) and (5.12). To bound Ω2 we proceed as in Lemma 5.2 and we
obtain
 Ω2 ≤ − Dh
3 + D(ω0 + 1)
ω (log E∗ + log log E∗).

Therefore Ω2 ≤ 0 by (5.9). Now we establish the inequality

θ(K + 1)(L + 1)λ ≥ DKh
3 + Φ.

Since L + 1 ≥ c1Dhλ−1 it suﬃces to prove that

θ − 1
3c1 − Φ
(K + 1)(L + 1)λ ≥ 0. (5.19)

By the deﬁnition of Φ we have

Φ
(K + 1)(L + 1)λ ≤ γ log E∗

c1h + 3γ1/3g2/3

22/3c
1/3
0
 ( 1
˜Γ1/3 + 3
1/3)

+ g
√c0D log E∗λ−1 + gλ2

c0 min{a1, a2}D log E∗ ,

where ˜Γ = min{c1Dhλ−1, c0a1a2D log E∗λ−3/2}.

Moreover by (5.2) and (5.12) we have

θ ≥ 1
8
 (

1 − 1
5.1Dhλ−1 +
 √1 − 2
5.1Dhλ−1
 )
 .

Explicit lower bounds for linear forms in two logarithms 143

Therefore we deduce that (5.19) holds if

1
3c1 + γ log E∗

hc1 ≤ 1
8
 (

1 − 1
5.1Dhλ−1 +
 √1 − 2
5.1Dhλ−1
 )

− g
√c0(D log E∗)λ−1 − g
c0 min{a1, a2}D log E∗λ−2

− 3γ1/3g2/3

22/3c
1/3
0
 ( 1
˜Γ1/3 + 3
1/3) .(2’)

In conclusion we have shown that (2′) implies (2). Hence to apply Theorem
2.1 in the proof of corollaries we shall verify (2′) instead of (2).

5.3. Obtention of numerical values in corollaries. First notice that
if conditions (1) and (2) of Theorem 2.1 are veriﬁed the conclusion of this
theorem implies that
 log |Λ′| ≥ −2θ(K + 2)(L + 1)λ.

Then in the same way as in [5] we obtain

log |Λ| ≥ −2θ(1 + 2.10−5)(K + 2)(L + 1)λ. (5.20)

Therefore we have (5.20) if (2′) and (5.7) − (5.13) are satisﬁed. Now we
continue the specialization of the parameters to obtain the statements of
Corollaries 2.2, 2.3 and 2.4. These corollaries are deduced from the lower
bound

log |Λ| ≥ − 1
2 (1 + 2
K )(1 + 1
L )(1 + 2.10−5)c0c1D2ha1a2 log E∗λ−3, (5.23)

which follows from (5.22), (5.1) and (5.2).
For Corollary 2.2 we put

E = 6.6, c0 = 317, c1 = 5.378, ai = (E + 2)D log Ai, (i = 1, 2),

log E∗ = 3.317 + 1.888
D + 0.946 log D,

h = max {log b + 3.1, 1000
D , 498 + 284
D + 142 log D} .

Then (5.8) and (5.9) hold. Next we check (5.7) and (5.10) which follow
respectively from

E| log αi| − log |αi| + 2Dh(αi) ≤ E| log αi| + 2Dh(αi)

≤ (E + 2)D log Ai, (i = 1, 2)

and
 log ( b2
a1 + b1
a2
 ) = log b − log(E + 2).

144 Nicolas Gouillon

Finally we must prove that (2′) holds. To this end we remark that
ai ≥ 8.6, (i = 1, 2), and that log E∗ ≥ 4.84 by (5.14). Moreover we have
log E∗
h ≤ 1
150 by (5.9) and 1
Dh ≤ 1
1000 by our choice of h. Then replacing the
parameters c0, c1 and E by their numerical above choices we get (2′).
The proof of Corollary 2.3 is similar. Without loss of generality we may
assume that log α1 and log α2 are two real positive numbers . Then we
choose

E = 5.5, c0 = 313, c1 = 5.386, ai = (E + 1)D log Ai, (i = 1, 2),

log E∗ = 3.409 + 1.705
D + 0.946 log D,

h = max {log b + 3.1, 1000
D , 512 + 256
D + 142 log D} .

In this case (5.7) and (5.10) follow respectively from

E| log αi| − log |αi| + 2Dh(αi) ≤ (E − 1)| log αi| + 2Dh(αi)

≤ (E + 1)D log Ai, (i = 1, 2)

and
 log ( b2
a1 + b1
a2
 ) = log b − log(E + 1).

The condition (2′) is shown as in Corollary 2.2.
For Corollary 2.4, we choose

c0 = 368, c1 = 5.141, ai = 3D log Ai, (i = 1, 2),

E = 1 + min { D log A1
log α1 , D log A2
log α2
 } ,

log E∗ = max { λ
D , λ
D + 0.946 log D
log λ + 3.965} ,

h = max {log b + log λ + λ
D + 1.622, 150 log E∗, 500λ
D
 } .

With these choices it is obvious to prove (5.8) − (5.10). To etablish (5.7)
we use the following upper bound :

(E − 1) log αi + 2Dh(αi) = min { D log A1
log α1 , D log A2
log α2
 } log αi + 2Dh(αi)

≤ 3D log Ai = ai.

Finally (2′) is proved in the same way as Corollaries 2.2 and 2.3 with ai ≥
3λ.

Remark. For D ﬁxed, we can reﬁne our computations to improve the state-
ments of corollaries.

Explicit lower bounds for linear forms in two logarithms 145

5.4. Numerical appendix. This appendix containes numerical tables
which complete Corollaries 2.2, 2.3 and 2.4.
TABLE 1

h1 600 800 1500 2000 2500 3000
E 6.55 6.55 6.6 6.6 6.6 6.6
c0 325 320 311 308 306 304
c1 5.378 5.381 5.387 5.381 5.374 5.368
C1 9650 9490 9230 9130 9050 9000
This ﬁrst table refers to Corollary 2.2. We give diﬀerent choices for the
constant h1 involved in the deﬁnition of h :

h = max {log b + 3.4, h1
D , h1
4 log E∗} .

For any value 600 ≤ h1 ≤ 3000 we have the upper bound

log E∗ ≤ 3.328 + 1.888
D + 0.946 log D.

For the values of table 1 the lower bound of Corollary 2.2 is

log |Λ| ≥ −C1
 (3.328 + 1.888
D + 0.946 log D) D4h log A1 log A2.

We remark that for h1 ≥ 3000 the constant C1 closed to 9000. This follows
from the fact that in this case L + 1 ≥ K+1
2 .
TABLE 2

h2 600 800 1500 1750 2000 2100
E 5.5 5.5 5.55 5.55 5.55 5.55
c0 321 316 308 306 305 304
c1 5.383 5.389 5.382 5.389 5.381 5.389
C2 7380 7270 7080 7030 7000 6990
This second table refers to Corollary 2.3. As above we give diﬀerent
choices for the constant h2 which is in the deﬁnition of h :

h = max {log b + 3.4, h2
D , h2
4 logE∗} .

We have in any case the upper bound

log E∗ ≤ 3.417 + 1.714
D + 0.946 log D.

The lower bound in Corollary 2.3 is here :

log |Λ| ≥ −C2
 (3.417 + 1.714
D + 0.946 log D) D4h log A1 log A2.

For the same reasons as before we only consider the value of h2 up to 2100.

146 Nicolas Gouillon

In the case of corollary 2.4 the variations of the main constant are too
small to construct an interesting table.

References

[1] Alan Baker, Transcendental number theory. Cambridge University Press, London, 1975.
[2] Nicolas Gouillon, Un lemme de zéros. C. R. Math. Acad. Sci. Paris, 335 (2) (2002),
167–170.
[3] Nicolas Gouillon, Minorations explicites de formes linéaires en deux logarithmes. Thesis
(2003) : http://tel.ccsd.cnrs.fr/documents/archives0/00/00/39/64/index_fr.html
[4] Michel Laurent, Linear forms in two logarithms and interpolation determinants. Acta
Arith. 66 (2) (1994), 181–199.
[5] Michel Laurent, Maurice Mignotte, Yuri Nesterenko, Formes linéaires en deux log-
arithmes et déterminants d’interpolation. J. Number Theory 55 (2) (1995), 285–321.
[6] D. W. Masser, On polynomials and exponential polynomials in several complex variables.
Invent. Math. 63 (1) (1981), 81–95.
[7] E. M. Matveev, An explicit lower bound for a homogeneous rational linear form in loga-
rithms of algebraic numbers. II. Izv. Ross. Akad. Nauk Ser. Mat. 64 (6) (2000), 125–180.
[8] Maurice Mignotte, Michel Waldschmidt, Linear forms in two logarithms and Schnei-
der’s method. II. Acta Arith. 53 (3) (1989), 251–287.
[9] Michel Waldschmidt, Minorations de combinaisons linéaires de logarithmes de nombres
algébriques. Canad. J. Math. 45 (1) (1993), 176–224.
[10] Michel Waldschmidt, Diophantine Approximation on Linear Algebraic Groups. Springer-
Verlag, 1999.
[11] Kun Rui Yu, Linear forms in p-adic logarithms. Acta Arith. 53 (2) (1989), 107–186.

Nicolas Gouillon
Institut de Mathématiques de Luminy
163, Avenue de Luminy, case 907
13288 Marseille Cedex 9, France
E-mail: gouillon@iml.univ-mrs.fr
