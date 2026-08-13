<!-- source: https://hal.science/hal-03216054/document | converted from PDF -->

HAL Id: hal-03216054

https://hal.science/hal-03216054v1

Submitted on 3 May 2021

HAL is a multi-disciplinary open access archive
for the deposit and dissemination of scientific re-
search documents, whether they are published or not.
The documents may come from teaching and research
institutions in France or abroad, or from public or pri-
vate research centers.
 L’archive ouverte pluridisciplinaire HAL, est des-
tinée au dépôt et à la diffusion de documents scien-
tifiques de niveau recherche, publiés ou non, émanant
des établissements d’enseignement et de recherche
français ou étrangers, des laboratoires publics ou
privés.

HAL Authorization

ELLIOTT-HALBERSTAM CONJECTURE AND VALUES
TAKEN BY THE LARGEST PRIME FACTOR OF SHIFTED
PRIMES

Jie Wu

To cite this version:

Jie Wu. ELLIOTT-HALBERSTAM CONJECTURE AND VALUES TAKEN BY THE LARGEST PRIME FACTOR
OF SHIFTED PRIMES. Journal of Number Theory, 2020, 206, pp.282-295. ⟨10.1016/j.jnt.2019.06.015⟩. ⟨hal-
03216054⟩

ELLIOTT-HALBERSTAM CONJECTURE AND VALUES TAKEN BY
THE LARGEST PRIME FACTOR OF SHIFTED PRIMES

JIE WU

Abstract. Denote by P the set of all primes and by P +(n) the largest prime factor of
integer n ⩾ 1 with the convention P +(1) = 1. For each η > 1, let c = c(η) > 1 be some
constant depending on η and

Pa,c,η := {p ∈ P : p = P +(q − a) for some prime q with p
η < q ⩽ c(η)pη}.

In this paper, under the Elliott-Halberstam conjecture we prove, for y → ∞,

πa,c,η(x) := |(1, x] ∩ Pa,c,η| ∼ π(x) or πa,c,η(x) ≫a,η π(x)

according to values of η. These complement for some results of Banks-Shparlinski [1], of
Wu [12] and of Chen-Wu [2].
 1. Introduction

Denote by P the set of all prime numbers and by P +(n) the largest prime factor of the
positive integer n ⩾ 1 with the convention P +(1) = 1. Banks & Shparlinski [1] proposed to
estimate the number of primes p that occur as the largest prime factor of a shifted prime
q − a when q ∈ P lies in a certain interval determined by p. This question has applications
in theoretical computer science and has been considered by Vishnoi [10].
Let Z
∗ be the set of non-zero integers. For a ∈ Z
∗, c > 1 and η > 0, we put

Pa,c,η := {r ∈ P : r = P +(q − a) for some prime q with rη < q ⩽ crη}

and πa,c,η(y) := |{r ⩽ y : r ∈ Pa,c,η}|, π(y) := |{r ⩽ y : r ∈ P}|.

Banks & Shparlinski [1, Theorem 1.1] proved that for each η ∈ ( 32
17, 1 + 3
4√
2), there exists a
constant c = c(η) > 1 such that the asymptotic formula

(1.1) πa,c,η(y) = π(y) + OA,a,c,η
( y
(log y)A
 ) (y → ∞)

holds for every ﬁxed non-zero integer a ∈ Z
∗ and any constant A > 1. Moreover for
2 ⩽ η < 1 + 3
4√2 ≈ 2.0606, this estimate holds for any constant c > 1. Very recently, Wu
[12] extended Banks-Shparlinski’s interval ( 32
17, 1 + 3
4√
2) to ( 32
17, η0), where η0 ≈ 2.142 is the
unique solution of the equation η − 1 − 4η log(η − 1) = 0 in (1, ∞). Banks & Shparlinski
[1, page 144] also remarked that the asymptotic formula (1.1) holds for η ∈ (1, 32
17] if we
assume the Elliott-Halberstam conjecture (see EHprime[ε] below). Subsequently, Chen & Wu

Date: July 2, 2019.
2010 Mathematics Subject Classiﬁcation. 11N05, 11N25, 11N36.
Key words and phrases. Shifted prime, Friable integer, Sieve.
1

2 JIE WU

[2] further extended the domain of η at the price proportion positive instead of density 1.
More precisely, they proved that

(1.2) πa,c,η(y) ⩾ ( log 4√2
) η − 1
η
 (1 − 4 log(η − 1) − δ log(η − 1)8

c − 1
 )π(y),

where δ = δ(c, η) is suﬃciently small positive number. Clearly, (1.2) implies

πa,c,η(y) ≫ π(y)

provided η < 1 + 4√
e. This is complement for the results of Banks-Shparlinski and of Wu
mentioned above. It seems rather natural to pose the following question.

Question 1. Is the asymptotic formula (1.1) true for all η > 1 ?

In this paper, we shall try to answer this question under the well-known Elliott-Halberstam
conjecture. Firstly we state two versions of this conjecture for prime numbers.

Conjecture 1 (Elliott–Halberstam). Let a ∈ Z
∗ and ε ∈ (0, 1) be ﬁxed constants.
(i) For any A > 0, the inequality
∑

q⩽x1−ε
(a,q)=1
 ∣
∣
∣
∣ ∑

p⩽x
p≡a(mod q)
 1 − π(x)
ϕ(q)
 ∣
∣
∣
∣ ≪A,a,ε x
(log x)A(EHprime[ε])

holds uniformly for all x ⩾ 3, where the letter p always denotes prime numbers, ϕ(q) is the
Euler function and the implied constant depends on A, a and ε.
(ii) Let κ1(m) and κ2(m) be the characteristic functions of the odd integers and of even
integers, respectively. Then for any A > 0, we have
∑

q⩽x1−ε
(a,q)=1
 ∣
∣
∣
∣ ∑

mp⩽x
mp≡a(mod q)

κi(m) − 1
ϕ(q)
 ∑

mp⩽x
(mp,q)=1
 κi(m)∣
∣
∣
∣ ≪A,a,ε x
(log x)A(EH
∗
prime[ε])

uniformly for all x ⩾ 3, where the letter p always denotes prime numbers and the implied
constant depends on A and a.

Remark 1. According to the classical Bombieri-Vinogradov theorem and Proposition 2.2 of
Wu [12], the Elliott-Halberstam conjectures EHprime[ε] and EH
∗
prime[ε] hold for all ε ∈ ( 1
2, 1).

Secondly we also need a version of this conjecture for friable numbers.

Conjecture 2 (Elliott–Halberstam). Let a ∈ Z
∗ and ε ∈ (0, 1) be ﬁxed constants. For any
A > 0, we have ∑

q⩽x1−ε
(a,q)=1
 ∣
∣
∣
∣ ∑

n⩽x
n≡a(mod q), P +(n)⩽y
 1 − 1
ϕ(q)
 ∑

n⩽x
(n,q)=1, P +(n)⩽y
 1
∣
∣
∣
∣ ≪A,a,ε x
(log x)A(EHfriable[ε])

uniformly in x ⩾ y ⩾ 2.

Remark 2. According to Wolke’s work [11] (see also [4, Theorem 6]), EHfriable[ε] holds un-
conditionally for all ε ∈ ( 1
2, 1).

ELLIOTT-HALBERSTAM CONJECTURE AND SHIFTED PRIMES 3

Our results are as follows.

Theorem 1. Let a ∈ Z
∗ and c > 1 be ﬁxed constants.
(i) Let η ∈ (1, 32
17] and assume the Elliott-Halberstam conjecture EHprime[ε] with ε = 1 −
1/η > 0. Then for any A > 1 we have

(1.3) πa,c,η(y) = π(y) + OA,a,c,η
( y
(log y)A
 ),

as y → ∞.
(ii) Let η1 ≈ 2.3303 be the unique positive zero of the equation η − 1 − 2η log(η − 1) = 0
in (1, ∞). For each η ∈ [η0, η1), there is a suﬃciently small positive number ε = ε(η) such
that assuming the Elliott-Halberstam conjecture EHprime[ε], for any A > 1 we have

(1.4) πa,c,η(y) = π(y) + OA,a,c,η
( y
(log y)A
 ),

as y → ∞.

Theorem 2. Let a ∈ Z
∗ and c > 1 be ﬁxed constants. For every η ∈ [2, ∞), there is a
suﬃciently small positive number ε = ε(η) such that under the Elliott-Halberstam conjecture
EHfriable[ε], we have

(1.5) πa,c,η(y) ⩾ ( log 4√
2
) η − 1
η π(y)
{
1 + Oa,c,η
( 1

3√log y + ε)}
,

as y → ∞.

Remark 3. (a) For comparaison, we have

1 + 3
4√
2 ≈ 2.060, η0 ≈ 2.142, η1 ≈ 2.330, 1 + 4√e ≈ 2.284, 1 + √e ≈ 2.648.

(b) The ﬁrst assertion of Theorem 1 is due to Banks & Shparlinski [1, page 144]. Here
we give a proof for convenience of the reader. By combining Theorem 1 with results of [12],
we see that the asymptotic formula (1.1) holds for 1 < η < η1 under the Elliott-Halberstam
conjecture.
(c) Theorem 2 improves signaﬁcantively Chen-Wu’s result (1.2) in two aspects : result
and method. Firstly the proportion in (1.5) increases from log 2
8 to log 2
4 when η runs over
[2, ∞), and that in (1.2) tends toward 0 as η → 1 + 4√e. Secondly our proof of (1.5) needs
information of prime numbers in “arithmetical progressions” {a + mq}m friable with friable
indice. For (a, q) = 1 and x ⩾ y ⩾ 2, deﬁne the counting function

(1.6) π(x, y; q, a) := ∑

p⩽x
p≡a(mod q)
P +((p−a)/q)⩽y
 1.

A systematic study on the asymptotical behaviour has been done by Liu, Wu & Xi [8],
recently. We need a theorem of Bombieri-Vinogradov type and an inequality of Brun-
Titichmarsh for this new counting function (see Lemmas 2.2–2.3 below).

4 JIE WU

2. Some preliminary lemmas

In this section, we present three lemmas, which will be useful later.

2.1. The Rosser-Iwaniec linear sieve.
The ﬁrst lemma is due to Iwaniec [6, 7].

Lemma 2.1. Let D ⩾ 2 and let µ(n) be the M¨obius function. Then there are two sequences
{λ
±
d }d⩾1, vanishing for d > D or µ(d) = 0, satisfying |λ
±
d | ⩽ 1, such that

(2.1) ∑

d|n λ−
d ⩽ ∑

d|n µ(d) ⩽ ∑

d|n λ+
d (n ⩾ 1)

and ∑

d|PP(z) λ
+
d w(d)
d ⩽ ∏

p⩽z
p∈P
 (1 − w(p)
p
 ){F (s) + O( e√L−s

3√log D
 )}
(2.2)
 ∑

d|PP(z) λ
−
d w(d)
d ⩾ ∏

p⩽z
p∈P
 (1 − w(p)
p
 ){f (s) + O( e√L−s

3√log D
 )}
(2.3)

for any z ∈ [2, D], s = (log D)/ log z, set of prime numbers P and multiplicative function w
satisfying
 0 < w(p) < p (p ∈ P),(2.4) ∏

u<p⩽v, p∈P
 (1 − w(p)
p
 )−1 ⩽ log v
log u
(1 + L
log u
) (2 ⩽ u ⩽ v),(2.5)

where PP(z) := ∏
p⩽z, p∈P p and the implied O-constants are absolute. Here F, f are deﬁned
by the continuous solutions to the system




sF (s) = 2eγ (1 ⩽ s ⩽ 2)
sf (s) = 0 (0 < s ⩽ 2)
(sF (s))
′ = f (s − 1) (s > 2)
(sf (s))
′ = F (s − 1) (s > 2)

where γ is the Euler constant.

2.2. Bombieri-Vinogradov theorem of for π(x, y; q, a).
The second lemma is a theorem of Bombieri-Vinogradov type for the counting function
π(x, y; q, a) deﬁned as in (1.6) (see [8, Theorem 2]).

Lemma 2.2. Let a ∈ Z
∗, A > 0 and κ a non-negative arithmetic function. Assuming the
Elliott-Halberstam conjecture EHprime[ε], the following estimate
∑

q⩽Q
(q,a)=1
 κ(q)
∣
∣
∣
∣π(x, y; q, a) − π(x)
ϕ(q) ρ( log(x/q)
log y
 )∣
∣
∣
∣ ≪a,A x
(log x)A
 √
∑

q⩽x
 κ(q)2

q + π(x)εu ∑

q⩽Q
 κ(q)
ϕ(q)

holds uniformly in x ⩾ 2, exp {
(log x)
2/5+ε} ⩽ y ⩽ x and Q ⩽ min{y, √
x}, where ρ(u) is
the Dickman function.

ELLIOTT-HALBERSTAM CONJECTURE AND SHIFTED PRIMES 5

2.3. Brun-Titichmarsh inequality for π(x, y; q, a).
The lemma below is a variant of [8, Theorem 1].

Lemma 2.3. Let a ∈ Z
∗ and c > 1 be ﬁxed constants. For any ε > 0, we have

(2.6)
 π(cx, y; q, a) − π(x, y; q, a) ⩽ 4(c − 1)x
ϕ(q) log(x/q)ρ(log(x/q)
log y
 ){1 + Oa,c,ε
( 1

3√log x
 )}

+ OA,a,c
( x
q(log x)A
 )

uniformly in exp{log log x)
5/3+ε} ⩽ y ⩽ x and 1 ⩽ q ⩽ min{y, √
x} with (a, q) = 1.

Proof. Denote by S the quantity on the left-hand side of (2.6). Without loss of generality,
we can assume q is even and a is odd. Put P2a(z) := ∏
p⩽z,p∤2a p. By the M¨obius inversion,
we can write
 S = ∑

x<a+mq⩽cx
(mq,a)=(a+mq,P2a(
√cx))=1
P +(m)⩽y
 1 + O(xε)

= ∑

x<a+mq⩽cx
(a,mq)=1, P +(m)⩽y
 ∑

d|(a+mq,P2a(
√cx)) µ(d) + O(xε),

Using Lemma 2.1 and switching summations, it follows that

S ⩽ ∑

x<a+mq⩽cx
(a,mq)=1, P +(m)⩽y
 ∑

d|(a+mq,P2a(
√cx)) λ+
d + O(xε)

= ∑

d⩽D
d|P2aq(
√cx)
 λ
+
d ∑

(x−a)/q<m⩽(cx−a)/q
m≡−aq (mod d)
(a,m)=1, P +(m)⩽y
 1 + O(xε),

where {λ
+
d }d⩾1 is an upper bound sieve of level D as in Lemma 2.1 and q is the inverse of q
modulo d (i.e. qq ≡ 1 (mod d)). To apply the Elliott-Halberstam conjecture EHfriable[ε], we
would like to remove the restriction (a, m) = 1 by M¨obius inversion, so that

S ⩽ ∑

ℓ|a µ(ℓ) ∑

d⩽D
d|P2aq(√cx)
 λ
+
d ∑

(x−a)/q<m⩽(cx−a)/q
m≡−aq (mod d)
ℓ|m, P +(m)⩽y
 1 + O(xε)

= ∑

ℓ|a
P +(ℓ)⩽y
 µ(ℓ) ∑

d⩽D
d|P2aq(√cx)
 λ+
d ∑

(x−a)/ℓq<m⩽(cx−a)/ℓq
m≡−aℓq (mod d)
P +(m)⩽y
 1 + O(xε).

We are now in a good position to employ the Elliott-Halberstam conjecture EHfriable[ε] with
D = (x/q)1−ε, getting
 S ⩽ S+ + O( x
q(log x)A
 ),(2.7)

6 JIE WU

where
 S
+ := ∑

ℓ|a µ(ℓ) ∑

d⩽D
d|P2aq(
√cx)
 λ+
d
ϕ(d)
 ∑

x/ℓq<m⩽cx/ℓq
(d,m)=1, P +(m)⩽y
 1.

and we have used the trivial bound
∑

ℓ|a
 ∑

d⩽D
d|P2aq(
√cx)
 |λ+
d |
ϕ(d)
 ∑

cx/ℓq<m⩽(cx−a)/ℓq
(d,m)=1, P +(m)⩽y
 1 ≪a log x.

Here we removed the restriction that P +(ℓ) ⩽ y since we henceforth assume y > |a|.
Switching summations, it follows that

S
+ = ∑

ℓ|a µ(ℓ) ∑

x/ℓq<m⩽cx/ℓq
P +(m)⩽y
 ∑

d⩽D
d|P2amq(
√cx)
 λ+
d
ϕ(d)

= ∑

x/q<m⩽cx/q
(a,m)=1, P +(m)⩽y
 ∑

d⩽D
d|P2amq(
√cx)
 λ
+
d
ϕ(d)·

From Lemma 2.1, we deduce

(2.8)
 S
+ ⩽ log √
x
log(x/q)
{
2e
γ + O( 1

3√log x
)} ∑

x/q<m⩽cx/q
(a,m)=1, P +(m)⩽y
 ∏

p<√x
p∤2amq
 (1 − 1
p − 1
)

⩽ log √
x
log(x/q)
{
2e
γ + O( 1

3√log x
)} ∏

p<√x
p∤2aq
 (1 − 1
p − 1
 ) ∑

x/q<m⩽cx/q
(a,m)=1, P +(m)⩽y
 H(m),

where H(m) is the multiplicative function, deﬁned by

H(pν) =
 {
1 if p | 2q or p > x
1/2

p−1
p−2 if p ∤ 2q and p ⩽ x1/2

for all ν ⩾ 1. According to [8, (3.5)], we have

∑

m∈S(x/q,y)
(a,m)=1
 H(m) = Ψ( x
q , y) ϕ(a)
a
 ∏

p<√x
p∤2aq
 (
1 + 1
p(p − 2)
){
1 + O( (log log x)2

log y
 )}
,

where S(x, y) := {n ⩽ x : P +(n) ⩽ y} and Ψ(x, y) := |S(x, y)|. Combining this with (2.8),
we ﬁnd that

(2.9) S
+ ⩽ log x
log(x/q)
{2e
γ + O( 1

3√
log x
 )}ϕ(a)
a
 {
Ψ
(cx
q , y) − Ψ
( x
q , y)} ∏

p⩽
√x
p∤aq
 (1 − 1
p
 )
.

ELLIOTT-HALBERSTAM CONJECTURE AND SHIFTED PRIMES 7

By the Mertens formula, it follows that
∏

p⩽x1/2
p∤aq
 (1 − 1
p
) = aq
ϕ(a)ϕ(q) · 2e
−γ

log x
{1 + O( 1
log x
)}.

On the other hand, according to [5, Theorem 1], we have

Ψ(x, y) = xρ( log x
log y
 ){1 + O( log((log x)/ log y + 1)
log y
 )}

uniformly for x ⩾ 3 and exp{(log log x)5/3+ε} ⩽ y ⩽ x. Combining these with (2.9) and
(2.7), we can get the required inequality (2.6). □

3. Proof of Theorem 2

For each prime r ∈ ( 1
2y, y], consider

(3.1) Qr(y) := ∑

x<q⩽cx
P +(q−a)=r
 1.

Noticing that P +(q − a) = r ⇔ q ≡ a (mod r) and P +(q − a) ⩽ r,
we can write

(3.2)
 ∑

y<r⩽2y Qr(y) ⩾ ∑

y<r⩽2y
 ∑

x<q⩽cx
q≡a (mod r), P +(q−a)⩽y
 1

= ∑

y<r⩽2y
 (π(cx, y; r, a) − π(x, y; r, a)
)

= M + E,

where
 M := ∑

y<r⩽2y
 ( π(cx)
ϕ(r) ρ( log(cx/r)
log y
 ) − π(x)
ϕ(r) ρ( log(x/r)
log y
 ))
,

E := ∑

y<r⩽2y
 (
E(cx, y; r, a) − E(x, y; r, a)
)
,

and
 E(x, y; r, a) := π(x, y; r, a) − π(x)
ϕ(r) ρ( log(x/r)
log y
 )
.

Since η ⩾ 2, we have y = x1/η ⩽ x1/2 and Q = min(y, √x) = y. Using Lemma 2.2 with the
characteristic function of prime numbers in (y, 2y] in place of κ(q), we easily derive, under
the conjecture of Elliott-Halberstam EHprime[ε], that

(3.3)
 |E| ⩽ ∑

y<r⩽2y
 (
|E(cx, y; r, a)| + |E(x, y; r, a)|
)

≪a x
(log x)3 + εη π(x)
log y ≪a,η ε π(x)
log y

8 JIE WU

for all x ⩾ x0(ε), where we have used the following bound

(3.4) ∑

y<r⩽2y
 1
ϕ(r) = ∑

y<r⩽2y
 1
r
 {
1 + O( 1
y
 )} = log 2
log y
 {
1 + O( 1
log y
 )}

and the implied constant depends on a, η at most.
According to [9, Corollary III.5.8.3], we have |ρ′(u)| ≪ ρ(u) log u (u > 1). Thus for all
r ∈ (y, 2y], we have
 ρ( log(x/r)
log y
 ) = ρ(η − 1)
{
1 + Oη
( 1
log y
 )}.

From this and (3.4), we derive

(3.5) M = (log 2)(c − 1)ρ(η − 1) π(x)
log y
 {
1 + Oη
( 1
log y
 )}
.

Inserting (3.5) and (3.3) into (3.2), it follows that

(3.6) ∑

y<r⩽2y Qr(y) ⩾ (log 2)(c − 1)ρ(η − 1) π(x)
log y
 {1 + Oa,c,η
( 1
log y + ε)}.

On the other hand, the Brun-Titchmarsh inequality (2.6) give us

Qr(y) ⩽ 4(c − 1)x
ϕ(r) log(x/r)ρ(η − 1){
1 + Oa,η
( 1

3√log x
 )}

⩽ 4(c − 1)ρ(η − 1)
η − 1 · x
y log y
 {1 + Oa,η
( 1

3√
log x
 )}

for all primes r ∈ (y, 2y]. This implies that

(3.7) ∑

y<r⩽2y Qr(y) ⩽ ρ(η − 1)4(c − 1)
(η − 1) · x
y log y
 {1 + Oa,η
( 1

3√log x
)} ∑

y<r⩽2y
Qr(y)̸=0
 1.

Combining (3.6) and (3.7), it follows that
∑

y<r⩽2y
Qr(y)̸=0
 1 ⩾ ( log 4√
2
) η − 1
η π(y){
1 + Oa,c,η
( 1

3√log x + ε)}.

This completes the proof of Theorem 2.

4. Proof of Theorem 1

As in [12], the letters p, q, r and ℓ are always used to denote prime numbers, and d, m, and
n always denote positive integers. In what follows, let a ∈ Z
∗ and η ∈ (1, 32
17] ∪ [η0, η1). Let δ
be a suﬃciently small positive constant and let c > 1 be a parameter to be chosen later. Let
x0(A, a, c, η, δ) be a large constant depending on A, a, c, η, δ at most. For x ⩾ x0(A, a, c, η, δ)
and r ∈ ( 1
2y, y], put x := rη. As usual, for (a, d) = 1 deﬁne

π(x; d, a) := ∑

p⩽x
p≡a(mod d)
 1.

ELLIOTT-HALBERSTAM CONJECTURE AND SHIFTED PRIMES 9

4.1. The case of η ∈ (1, 32
17].
For η > 1, c > 1, y ⩾ 3 and x = yη, put

R
′
b(y) := {y < r ⩽ 2y : ∣
∣
∣
∣π(x; r, a) − π(x)
ϕ(r)
 ∣
∣
∣
∣ ⩾ δ π(x)
ϕ(r)
 }
,

R
′′
b(y) := {y < r ⩽ 2y : ∣
∣
∣
∣π(cx; r, a) − π(cx)
ϕ(r)
 ∣
∣
∣
∣ ⩾ δ π(cx)
ϕ(r)
 }
.

Noticing that y = x1/η = x1−(1−1/η), the Elliott-Halberstam conjecture EHprime[ε] with ε =
1 − 1/η allows us to deduce tthat

δ π(x)
y |R
′
b(y)| ⩽ ∑

y<r⩽2y
 ∣
∣
∣
∣π(x; r, a) − π(x)
ϕ(r)
 ∣
∣
∣
∣

≪A,a,δ,η x
(log x)A+1 ,

which gives immediately

(4.1) |R
′
b(y)| ≪A,a,δ,η y
(log y)A ·

Similarly

(4.2) |R
′′
b(y)| ≪A,a,c,δ,η y
(log y)A ·

Deﬁne
 R
′
g(y) := {
y < r ⩽ 2y : π(x; r, a) ⩽ (1 + δ)π(x)
ϕ(r)
 }
,

R
′′
g(y) := {
y < r ⩽ 2y : π(cx; r, a) ⩾ (1 − δ)π(cx)
ϕ(r)
 }
,

and Rg(y) := R
′
g(y) ∩ R
′′
g(y).
Clearly Rg(y) ⊂ P ∩ (y, 2y] ⊂ R
′
b(x) ∪ R
′′
b(x) ∪ Rg(y).
Thus the estimations (4.1) and (4.2) imply that

(4.3) |Rg(y)| = π(2y) − π(y) + OA,a,c,δ,η( y
(log y)A
 ) (y ⩾ 2).

Let r ∈ Rg(y) and let Qr(y) be deﬁned as in (3.1). When η ∈ (1, 32
17], we have r > y =
x1/η ⩾ x17/32 > (cx)
1/2. Thus the deﬁnition of Rg(y) allows us to write

(4.4) Qr(y) = π(cx; r, a) − π(x; r, a) ⩾ (c − 1 − 3δ)π(x)
ϕ(r) > 0,

where we have used the inequality π(cx) ⩾ (c − δ)π(x) for x ⩾ x0(a, c, δ). By the deﬁnition
of Pa,c,η and (4.4), it is easy to see that Rg(y) ⊂ Pa,c,η ∩ [y, 2y]. In view of (4.3), we ﬁnd that

πa,c,η(2y) − πa,c,η(y) = π(2y) − π(y) + OA,a,c,η
( y
(log y)A
 ).

This implies the ﬁrst assertion of Theorem 1, thanks to standard dyadic split.

10 JIE WU

4.2. The case of η ∈ [η0, η1).
In this case, for every prime r ∈ Rg(y), we can write

(4.5) Qr(y) = π(cx; r, a) − π(x; r, a) − Qr(y)

⩾ (c − 1 − 3δ)π(x)
ϕ(r) − Qr(y).

for x ⩾ x0(a, c, δ), where

(4.6) Qr(y) := ∑

x<q⩽cx
q≡a(mod r), P (q−a)>r
 1.

Similar to [12, Proposition 2.1] ∗, we can prove

(4.7) Qr(y) ⩽ (c − 1 + 2δ)2η log(η − 1)
η − 1 · π(y)
ϕ(r)
{
1 + Oa,c,δ,η,ε
( 1

3√log r
 )}

for y ⩾ 3, r ∈ (y, 2y] and η ⩾ 2.
Inserting (4.7) into (4.4) and taking c = 1 + 2√
δ, we can ﬁnd that

Qr(y) ⩾ 2
 √
δ − δ
η − 1
 (
η − 1 − 2η log(η − 1) · 1 + √δ
1 − √
δ
 ) π(y)
ϕ(r)

= {G(η) + O(√
δ)}2
√
δ 1 − √
δ
η − 1 · π(y)
ϕ(r),

where

(4.8) G(η) := η − 1 − 2η log(η − 1).

It is easy to see that G(η) is decreasing on [2, ∞) and G(2) = 1. Therefore there is a unique
real number η1 ∈ (2, ∞) such that G(η1) = 0 and for η ∈ [2, η1) we have the inequality

(4.9) Qr(y) ≫A,a,δ,η π(y)
ϕ(r)

for y ⩾ y0(A, a, δ, η). As before, (4.9) allows us to deduce that Rg(y) ⊆ Pa,c,η ∩ (y, 2y].
Combining this with (4.3) leads to

πa,c,η(2y) − πa,c,η(y) = π(2y) − π(y) + OA,a,c,δ,η( y
(log y)A
 ).

This implies the required asymptotic formula (1.4).

Acknowledgements. This work is supported in part by Scientiﬁc Research Innovation
Team Project Aﬃliated to Yangtze Normal University (No. 2016XJTD01).

∗The proof is identical and the only diﬀerence is that we can take z = (y/q)
(1−ε)/2 and D = z2 thanks to
the Elliott-Halberstam conjecture EH
∗
prime[ε], instead of z = (y/q)
1/4/(log y)B and D = z2

ELLIOTT-HALBERSTAM CONJECTURE AND SHIFTED PRIMES 11

References

[1] W. Banks & Igor E. Shparlinski, On values taken by the largest prime factor of shifted primes, J. Aust.
Math. Soc. 82 (2007), 133–147.
[2] B. Chen & J. Wu, On values taken by the largest prime factor of shifted primes (II), International J.
Number Theory, 15 (2019), no. 5, 935–944.
[3] B. Feng & J. Wu, On the density of shifted primes with large prime factors, Science China Mathematics,
61 (2018), no. 1, 83–94.
[4] ´E. Fouvry & G. Tenenbaum, Entiers sans grand facteur premier en progressions arithm´etiques, Proc.
London Math. Soc. 63 (1991) 449–494.
[5] A. Hildebrand, On the number of positive integers ⩽ x and free of prime factors > y, J. Number
Theory, 22 (1986), 289–307.
[6] H. Iwaniec, Rosser’s sieve, Acta Arith., 36 (1980), 171–202.
[7] H. Iwaniec, A new form of the error term in the linear sieve, Acta Arith., 37 (1980), 307–320.
[8] Jianya Liu, Jie Wu & Ping Xi, Primes in arithmetic progressions with friable indices, Science China
Mathematics, to appear.
[9] G. Tenenbaum, Introduction to analytic and probabilistic number theory, Translated from the second
French edition (1995) by C. B. Thomas, Cambridge Studies in Advanced Mathematics 46, Cambridge
University Press, Cambridge, 1995. xvi+448 pp.
[10] N. K. Vishnoi, Theoretical aspects of randomization in computation, Ph. D. Thesis, Georgia Inst. of
Tchnogy, 2004. (http://smartech.gatech.edu:8282/dspace/handle/1853/5049)
[11] D. Wolke, ¨Uber die mittlere Verteilung der Werte zahlentheoretischer Funktionen auf Restklassen. II,
Math. Ann. 204 (1973), 145–153.
[12] J. Wu, On values taken by the largest prime factor of shifted primes, J. Aust. Math. Soc., to appear.
doi:10.1017/S144678871800023X.

School of Mathematics and Statistics, Yangtze Normal University, Fuling, Chongqing
408100, China
Current address: CNRS LAMA 8050, Laboratoire d’Analyse et de Math´ematiques Appliqu´ees, Universit´e
Paris-Est Cr´eteil, 94010 Cr´eteil Cedex, France
E-mail address: jie.wu@math.cnrs.fr
