<!-- source: https://arxiv.org/pdf/2208.11316 | converted from PDF -->

arXiv:2208.11316v2  [math.NT]  3 Nov 2022
ON A CONJECTURE ON SHIFTED PRIMES WITH LARGE PRIME
FACTORS

YUCHEN DING

Abstract. Let P be the set of all primes and π(x) be the number of primes up to x.
For any n ≥ 2, let P +(n) be the largest prime factor of n. For 0 < c < 1, let

Tc(x) = #{p ≤ x : p ∈ P, P +(p − 1) ≥ pc}.

In this note, we prove that there exists some c < 1 such that

lim sup
x→∞ Tc(x)
π(x) < 1
2 ,

which disproves a conjecture of Chen and Chen.

1. Introduction

The investigations of the largest prime factors of shifted primes start from a cute
article of Goldfeld [6], where he proved that

#{p ≤ x : p ∈ P, P +(p − 1) > p1/2} ≥ 1
2 x
log x + O (x log log x
(log x)2
 ) ,

where P is the set of all primes and P +(n) denotes the largest prime factor of integer

n. Conventionally, we set P +(1) = 1. For 0 < c < 1, let

Tc(x) = #{p ≤ x : p ∈ P, P +(p − 1) ≥ pc}.

Goldfeld further remarked that one can show

lim inf
x→∞ Tc(x)
π(x) > 0 (1.1)

provided that c < 7/12, where π(x) is the number of primes up to x. Fouvry [5]
improved this by showing that there is some c0 ∈ (2/3, 1) such that inequality (1.1)

holds.
In the same direction, Luca et al. [9] considered the lower bound for Tc(x) for small

values of c. They proved that for 1/4 ≤ c ≤ 1/2

Tc(x) ≥ (1 − c) x
log x + E(x),

where
 E(x) ≪
 { x log log x/(log x)2, for 1/4 < c ≤ 1/2,
x/(log x)5/3, for c = 1/4.

2010 Mathematics Subject Classiﬁcation. Primary 11N05.
Key words and phrases. Shifted prime; The Bombieri–Vinogradov theorem.
*Corresponding author. 1

2 YUCHEN DING

As pointed out by Chen and Chen [3], the method of Luca et al. (essentially due to
Goldfeld) cannot be applied to c ∈ (0, 1/4). By some reﬁnements of the argument

employed by Luca et al., Chen and Chen could extend c to the interval (0, 1/2) with
slightly better error terms of the order of magnitude O(x/(log x)2). Moreover, Chen

and Chen proved the following interesting result. For any integer k ≥ 2, there exists at
most one c ∈ [ 1
k+1, 1
k ) such that

Tc(x) = (1 − c) x
log x + o ( x
log x
) .

Based on this result, Chen and Chen made the following conjecture.

Conjecture 1.1. For any integer k ≥ 1 and any c ∈ [ 1
k+1, 1
k ), we have

Tc(x) ≥ (1 − 1
k + 1
 ) x
log x + o ( x
log x
 ) .

Let ρ(u) be the Dickman function, deﬁned as the unique continuous solution of the

equation diﬀerential–diﬀerence
{ ρ(u) = 1, 0 ≤ u ≤ 1,
uρ
′(u) = −ρ(u − 1), u > 1.

Let θ1 ≈ 0.3517 be the unique solution of equation

θ − 4 ∫ 1/θ

1/θ−1
 ρ(t)
t dt = 0.

Feng and Wu [4] proved that

Tc(x) ≥
 (
1 − 4 ∫ 1/θ

1/θ−1
 ρ(t)
t dt + o(1)
)
 π(x)

provided 0 < c < θ1, which conﬁrmed Conjecture 1.1 for k ≥ 3 by numerical values

involving Dickman’s function. Later, the lower bound for Tc(x) was further improved
to
 Tc(x) ≥ (1 − 4ρ(1/θ) + o(1)) π(x)

by Liu, Wu and Xi [8] provided that 0 < θ < θ2 ≈ 0.3734, where θ2 is the unique

solution to equation θ − 4ρ(1/θ) = 0.
In the present note, we show that Conjecture 1.1 is actually incorrect for k = 1.
Precisely,

Theorem 1.1. There is an absolute constant c < 1 such that

lim sup
x→∞ Tc(x)
π(x) < 1/2.

ON A CONJECTURE ON SHIFTED PRIMES WITH LARGE PRIME FACTORS 3

2. Proofs

Before presenting the proof of Theorem 1.1, we ﬁrst ﬁx some notations and then state
a few lemmas to be used later. Let Λ(n) be the von Mangoldt function. As usual, ϕ(n)
denotes the Euler totient function. Let π(x; b, a) be the number of primes p ≡ a (mod b)

up to x. Following Goldfeld and Luca et al., we deﬁne

L(x; u, v) = ∑

u<m≤v Λ(m)π(x; m, 1).

The ﬁrst two lemmas are included in the proof of Goldfeld (see also [3, Lemma 2.1]).

Lemma 2.1. [6, bottom of page 23] For suﬃciently large x, we have

L(x; 1, x) = x + O (x/ log x) .

Lemma 2.2. [6, equations (2) and (3)] For suﬃciently large x, we have

L(x; 1, x
1/2) = x/2 + O (x log log x
log x
 ) .

The next lemma is another conjecture of Chen and Chen conﬁrmed by Wu later.

Lemma 2.3. [14, Theorem 2] For 0 < c < 1, let

T ′
c(x) = #{p ≤ x : p ∈ P, P +(p − 1) ≥ x
c}.

Then for suﬃciently large x we have

Tc(x) = T ′
c(x) + O (x log log x
(log x)2
 ) .

The proof of our theorem, among other things, is based on the following deep result

which appeared ﬁrst in the paper of Banks and Shparlinski [2, Lemma 2.1]. Here, we
use the version stated by Wu with a slight adjustment from prime modulus q to integer

modulus m.

Lemma 2.4. [14, Lemma 2.2] There exist two functions K2(θ) > K1(θ) > 0, deﬁned

on the interval (0, 17/32) such that for each ﬁxed real A > 0, and all suﬃciently large
Q = x
θ, the inequalities
 K1(θ) π(x)
ϕ(m) ≤ π(x; m, 1) ≤ K2(θ) π(x)
ϕ(m)

hold for all integers m ∈ (Q, 2Q] with at most O (
Q(log Q)−A) exceptions, where the

implied constant depends only on a, A and θ. Moreover, for any ﬁxed ε > 0, these
functions can be chosen to satisfy the following properties:

• K1(θ) is monotonic decreasing, and K2(θ) is monotonic increasing.
• K1(1/2) = 1 − ε and K2(1/2) = 1 + ε.

4 YUCHEN DING

Remark. The above lemma is due to the Bombieri–Vinogradov theorem for 0 < θ <
1/2, Baker–Harman [1] for 1/2 ≤ θ ≤ 13/25 and Mikawa [10] for 13/25 ≤ θ ≤ 17/32.

Now we turn to the proof of Theorem 1.1.

Proof of Theorem 1.1. Let 33/64 < c < 1 be a ﬁxed constant. Throughout our proof, p

and q will always denote primes unless indicated otherwise. The lower bound on Tc(x),
as observed by Goldfeld, starts from

Tc(x) ≥ ∑

p≤x
 ∑

xc≤q≤x
q|p−1
 1 ≥ 1
log x
 ∑

p≤x
 ∑

xc≤q≤x
q|p−1
 log q.

For an upper bound of Tc(x), we begin with the dual observation inspired by Goldfeld

with the help of Lemma 2.3

Tc(x) = ∑

p≤x
 ∑

xc≤q≤x
q|p−1
 1 + O ( x log log x
(log x)2
 ) ≤ log x
c
 ∑

p≤x
 ∑

xc≤q≤x
q|p−1
 log q + O (x log log x
(log x)2
 ) .

Changing the order of summations above, we get

Tc(x) ≤ log x
c
 ∑

xc≤q≤x π(x; q, 1) log q + O (x log log x
(log x)2
 ) . (2.1)

Following Goldfeld, the above estimate can be handled ﬁrstly by manipulating the

weighted sum L(x; x
c, x). For 33/64 < c < 1, from Lemmas 2.1 and 2.2 we clearly have

L(x; x
c, x) = L(x; 1, x) − L(x; 1, x
1/2) − L(x; x
1/2, x
c) + O(log x)

= x/2 − L(x; x
1/2, x
c) + O (x log log x
log x
 )

≤ x/2 − L(x; x
1/2, x
33/64) + O ( x log log x
log x
 ) . (2.2)

We now employ Lemma 2.4 to give a nontrivial lower bound of L(x; x
1/2, x
33/64). For
integers 1 ≤ j ≤ ⌊ log x
65 log 2⌋
, let Qj = 2jx
1/2. Then we have Qj > x
1/2 and 2Qj < x
33/64

for suﬃciently large x. For any 1 ≤ j ≤ ⌊ log x
65 log 2⌋, from Lemma 2.4 (with A = 2) we
have
 π(x; m, 1) > K1(33/64)
2 x
ϕ(m) log x (2.3)

for all integers m ∈ (Qj, 2Qj] with at most O (Qj/(log x)2) exceptions. For 1 ≤ j ≤⌊ log x
65 log 2⌋
, let Sj be the set of exceptions of m in the interval (Qj, 2Qj]. Thus, in view of

ON A CONJECTURE ON SHIFTED PRIMES WITH LARGE PRIME FACTORS 5

equation (2.3), we have

L(x; x
1/2, x
33/64) = ∑

x1/2<m≤x33/64 Λ(m)π(x; m, 1)

≥ ⌊ log x
65 log 2⌋∑

j=1
 ∑

Qj<m≤2Qj
m̸∈Sj
 Λ(m)π(x; m, 1)

≥ K1(33/64)
2 x
log x
 ⌊ log x
65 log 2⌋∑

j=1
 ∑

Qj<m≤2Qj
m̸∈Sj
 Λ(m)
ϕ(m) . (2.4)

For 1 ≤ j ≤ ⌊ log x
65 log 2⌋, we clearly have

∑

Qj<m≤2Qj
 Λ(m)
ϕ(m) ≥ ∑

Qj<p≤2Qj
 log p
p ≥ log Qj ∑

Qj<p≤2Qj
 1
p .

Chebyshev’s estimate or the prime number theorem gives us
∑

Qj<p≤2Qj
 1
p ≥ 1
2Qj
 ∑

Qj<p≤2Qj 1 ≥ 1
2Qj
 Qj
2 log Qj = 1
4 log Qj ,

from which we deduce that ∑

Qj<m≤2Qj
 Λ(m)
ϕ(m) ≥ 1
4.

Moreover, we have

∑

m∈Sj
 Λ(m)
ϕ(m) ≪ log(2Qj) ∑

m∈Sj
 log log m
m ≪ log x log log x ∑

m∈Sj
 1
m

since ϕ(m) ≫ m
log log m (see for example [11, Theorem 2.9]), where the implied constants
are all absolute. Noticing that Sj ⊂ (Qj, 2Qj] and |Sj| ≪ Qj/(log x)2 by its deﬁnition,

we get ∑

m∈Sj
 1
m ≪ 1
Qj
 Qj
(log x)2 = 1/(log x)2.

It follows that ∑

m∈Sj
 Λ(m)
ϕ(m) ≪ log log x
log x ,

where the implied constant is absolute. Thus, we have

∑

Qj<m≤2Qj
m̸∈Sj
 Λ(m)
ϕ(m) ≥ 1/5 (2.5)

6 YUCHEN DING

provided that x is suﬃciently large. Combining equation (2.2), inequalities (2.4) and
(2.5) we conclude that there exists some δ > 0 such that

L(x; x
c, x) ≤ (1/2 − δ)x + O (x log log x
log x
 ) . (2.6)

The transition from L(x; x
c, x) to ∑

xc≤q≤x π(x; q, 1) log q is somewhat standard. It is
clear that

L(x; x
c, x) − ∑

xc≤q≤x π(x; q, 1) log q = ∑

xc≤qk≤x
k>1
 π(x; qk, 1) log q + O(log x). (2.7)

For simplicity, we now require that 3/4 < c < 1. Trivial estimates lead to
∑

xc≤qk≤x
k>1
 π(x; qk, 1) log q ≤ ∑

x3/4≤qk≤x
q≤x1/2
k>1
 π(x; qk, 1) log q ≪ x
1/4 ∑

x3/4≤qk≤x
q≤x1/2
k>1
 log q

≪ x
1/4 ∑

q≤x1/2 log q log x ≪ x
3/4(log x)2. (2.8)

From equations (2.6), (2.7) and (2.8), we obtain
∑

xc≤q≤x π(x; q, 1) log q ≤ (1/2 − δ)x + O (x log log x
log x
 ) (2.9)

provided that 3/4 < c < 1. Hence, equation (2.9) together with equation (2.1) yield

Tc(x) ≤ 1
c (1/2 − δ)x/ log x + O ( x log log x
(log x)2
 ) .

Now the theorem follows from taking c = max{1 − δ, 4/5}. □

3. Final remarks

As early as 1980, Pomerance [12] conjectured that for any c ∈ (0, 1) we have
∑

p≤x
P +(p−1)≤xc
 1 ∼ ρ(1/c)π(x), as x → ∞.

This is surely a rather diﬃcult conjecture which is beyond the power of present math-

ematics. Granville [7] claimed that it follows from the Eillott–Halberstam conjecture.
Recently, Wang [13] oﬀered an alternative proof of this claim. Therefore, assuming the

Eillott–Halberstam conjecture, one can prove

lim
x→∞ Tc(x)/π(x) → 0, as c → 1

by Lemma 2.3. This immediately leads to a negative answer of Conjecture 1.1 for k = 1
under the Eillott–Halberstam conjecture. So this note can be viewed as an unconditional

proof of this matter. The exceptional result for level greater than 1/2 (see Lemma 2.4)
is crucial for this goal.

ON A CONJECTURE ON SHIFTED PRIMES WITH LARGE PRIME FACTORS 7

Acknowledgments

The author would like to thank the anonymous referee for his/her helpful comments
which improved the quality of this note greatly.
The author is supported by National Natural Science Foundation of China under

Grant No. 12201544, Natural Science Foundation of Jiangsu Province, China, Grant No.
BK20210784, China Postdoctoral Science Foundation, Grant No. 2022M710121, the

foundations of the projects ”Jiangsu Provincial Double–Innovation Doctor Program”,
Grant No. JSSCBS20211023 and ”Golden Phoenix of the Green City–Yang Zhou” to

excellent PhD, Grant No. YZLYJF2020PHD051.

References

[1] R.C. Baker and G. Harman, The Brun–Titchmarsh theorem on average, In analytic number
theory, Vol. 1 (Allerton Park, IL, 1995), 138 of Progr. Math., 39–103. Birkh¨auser Boston,
Boston, MA, 1996.
[2] W.D. Banks and I. E. Shparlinski, On values taken on by the largest prime factor of shifted
primes, J. Australian Math. Soc., 82 (2007) 133–147.
[3] F.–J. Chen and Y.–G. Chen, On the largest prime factor of shifted primes, Acta Math. Sin.
(Engl Ser), 33 (2017) 377–382.
[4] B. Feng, J. Wu, On the density of shifted primes with large prime factors, Sci. China Math.,
61 (2018) 83–94.
[5] ´Etienne Fouvry, Th´eor`eme de Brun–Titchmarsh: application au th´eor`eme de Fermat, Invent.
Math., 79 (1985) 383–407.
[6] M. Goldfeld, On the number of primes p for which p+ a has a large prime factor, Mathematika,
16 (1969) 23–27.
[7] A. Granville, Smooth numbers: computational number theory and beyond, In: Algorithmic
Number Theory: Lattices, Number Fields, Curves and Cryptography, vol. 44. Cambridge Uni-
versity Press, Cambridge (2008).
[8] J. Liu, J. Wu, P. Xi, Primes in arithmetic progressions with friable indices, Sci. China Math.,
63 (2020) 23–38.
[9] F. Luca F, R. Menares, A. Pizarro–Madariaga, On shifted primes with large prime factors and
their products, Bul.l Belg. Math. Soc. Simon Stevin, 22 (2015) 39–47.
[10] H. Mikawa, On primes in arithmetic progressions, Tsukuba J. Math., 25 (2001) 121–153.
[11] H. L. Montgomery, R. C. Vaughan, Multiplicative Number Theory I: Classical Theory. Cam-
bridge University Press, Cambridge, (2006).
[12] C. Pomerance, Popular values of Euler’s function, Mathematika, 27 (1980) 84–89.
[13] Z.–W. Wang, Autour des plus grands facteurs premiers d’entiers cons´ecutifs voisins d’un entier
cribl´e, Q. J. Math., 69 (2018) 995–1013.
[14] J. Wu, On shifted primes with large prime factors and their products, Arch. Math. (Basel), 112
(2019) 387–393.

(Yuchen Ding) School of Mathematical Science, Yangzhou University, Yangzhou
225002, People’s Republic of China
Email address: ycding@yzu.edu.cn
