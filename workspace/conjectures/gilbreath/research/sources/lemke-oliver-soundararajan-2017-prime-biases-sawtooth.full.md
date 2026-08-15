<!-- source: https://arxiv.org/pdf/1709.06168 | converted from PDF -->

arXiv:1709.06168v1  [math.NT]  18 Sep 2017
THE DISTRIBUTION OF CONSECUTIVE PRIME BIASES AND SUMS
OF SAWTOOTH RANDOM VARIABLES

ROBERT J. LEMKE OLIVER AND KANNAN SOUNDARARAJAN

Abstract. In recent work, we considered the frequencies of patterns of consecutive primes
(mod q) and numerically found biases toward certain patterns and against others. We made
a conjecture explaining these biases, the dominant factor in which permits an easy descrip-
tion but fails to distinguish many patterns that have seemingly very diﬀerent frequencies.
There was a secondary factor in our conjecture accounting for this additional variation, but
it was given only by a complicated expression whose distribution was not easily understood.
Here, we study this term, which proves to be connected to both the Fourier transform of
classical Dedekind sums and the error term in the asymptotic formula for the sum of φ(n).

1. Introduction

Let pn denote the sequence of primes in ascending order. Given q ≥ 3 and a = (a1, . . . , ar)
satisfying (ai, q) = 1 for all 1 ≤ i ≤ r, in recent work [7] we studied biases in the occurrence
of the pattern a in strings of r consecutive primes reduced (mod q). Thus, we deﬁned

π(x; q, a) := #{pn ≤ x : pn+i−1 ≡ ai (mod q) for 1 ≤ i ≤ r},

and conjectured that

(1.1) π(x; q, a) = li(x)
φ(q)r
 (1 + c1(q; a) log log x
log x + c2(q; a) 1
log x + O((log x)−7/4))
,

where c1(q; a) and c2(q; a) are certain explicit constants. The term c1(q; a) is easily described,

c1(q; a) = φ(q)
2
 (r − 1
φ(q) − #{i ≤ r − 1 : ai ≡ ai+1 (mod q)})
,

and it acts as a bias against immediate repetitions in the pattern a. The term c2(q; a) is
more complicated, and the goal of this paper is to understand its distribution. If r ≥ 3 then

c2(q; a) =
 r−1∑

i=1 c2(q; (ai, ai+1)) + φ(q)
2
 r−2∑

j=1
 1
j
 ( r − 1 − j
φ(q) − #{i : ai ≡ ai+j+1 (mod q)})
,

so that it is suﬃcient to understand the case r = 2; that is, c2(q; (a, b)) with (a, q) = (b, q) = 1.
For the sake of simplicity, we shall conﬁne ourselves to the case when q is prime. For any
character χ (mod q) we deﬁne

(1.2) Aq,χ = ∏

p∤q
 (
1 − (1 − χ(p))2

(p − 1)2
 ).

Robert Lemke Oliver was partially supported by NSF grant DMS-1601398. Kannan Soundararajan
was partially supported by NSF grant DMS-1500237 and by a Simons Investigator grant from the Simons
Foundation. 1

2 ROBERT J. LEMKE OLIVER AND KANNAN SOUNDARARAJAN

Then the quantity c2(q; (a, b)) is given by

c2(q; (a, a)) = q − 2
2 log(q/2π),

and when a ̸≡ b (mod q) by
(1.3)

c2(q; (a, b)) = 1
2 log 2π
q + q
φ(q)
 ∑

χ̸=χ0 (mod q)
 (χ(b − a) + 1
φ(q) (χ(b) − χ(a)))
L(0, χ)L(1, χ)Aq,χ.

The diagonal term c2(q; (a, a)) is thus completely explicit, and of size q log q. Our work here
shows that the oﬀ-diagonal terms c2(q; (a, b)) can also be large; usually they are of size about
q, occasionally getting to size q log log q (attaining both positive and negative values), which
we believe is their maximal size.
Before stating our result, we make one more simpliﬁcation. Deﬁne

(1.4) C(k) = C(k; q) = 1
φ(q)
 ∑

χ̸=χ0 (mod q) χ(k)L(0, χ)L(1, χ)Aq,χ.

Since Aq,χ ≪ 1, L(1, χ) ≪ log q, and (upon using the functional equation) L(0, χ) ≪
√q log q, from (1.3) it follows that for a ̸≡ b (mod q)

(1.5) c2(q; (a, b))
q = C(b − a) + O((log q)2
√q
 )
.

Thus for large q it is enough to understand the distribution of C(k) as k varies over all
non-zero residue classes (mod q). Since L(0, χ) = 0 for even characters χ, in (1.4) only odd
characters χ make a contribution, and therefore C(k) = −C(−k) is an odd function of k.

Theorem 1.1. (1) As q → ∞ the distribution of C(k) tends to a continuous probabil-
ity distribution, symmetric around 0. Precisely, there is a continuous function ΦC with
ΦC(−x) + ΦC(x) = 1 such that uniformly for all x ∈ [−X, X] one has
1
q #{k (mod q) : C(k) ≤ eγ
2 x} = ΦC(x) + o(1).

(2) Uniformly for all e ≤ x ≤ ( 1
2 − ǫ) log log q one has

exp(−A1e
x/x) ≥ 1
q #{k (mod q) : C(k) ≥ eγ
2 x} ≥ exp(−A2e
x log x)

for some positive constants A1 and A2.
(3) For all large q, there exists k (mod q) with

−C(−k) = C(k) ≥ (e
γ

4 − ǫ
) log log q.

(4) For all k (mod q) we have

C(k) ≪ (log q) 2
3 (log log q)2.

(5) The values C(k) have an “almost periodic” structure. Precisely, suppose 1 ≤ m ≤ q/4
is a multiple of every natural number below B ≥ 2. Then
1
q
 ∑

k (mod q) |C(k) − C(k + m)|2 ≪ 1
B1−ǫ + m
q log B.

CONSECUTIVE PRIME BIASES AND SAWTOOTH RANDOM VARIABLES 3

We make a few comments concerning Theorem 1.1 before proceeding to related results. In
part 1, we believe that the distribution for C(k) has a density, which is to say that ΦC is in
fact diﬀerentiable. Our proof falls just a little short of establishing this. In part 2, there is a
gap between the upper and lower bounds for the tail frequencies. With a little more care, we
can improve the lower bound there to exp(−A3e
x) for a suitable positive constant A3, but
there still remains a gap between the two bounds. The distribution of C(k), and especially
the double exponential decay seen in part 2, are reminiscent of the distribution of values of
L(1, χd) (see [4]). Motivated by this analogy, or by extrapolating the lower bounds in part
2, we believe that in part 3 there should exist values of C(k) as large as ( eγ
2 − ǫ) log log q.
We also conjecture that ( eγ
2 + ǫ) log log q should be the largest possible value of C(k), which
would be a substantial strengthening of part 4. Finally, in addition to the almost periodic
structure given in part 5 (where k varies), there should be an almost periodic structure as q
varies. That is, if q1 and q2 are two large random primes with q1 − q2 being a multiple of the
numbers below B, then C(k; q1) and C(k; q2) will be close to each other (on average over k).
We hope that an interested reader will embrace some of these remaining problems.
While the quantity C(k) is the main focus of this paper, closely related objects arise in
two other seemingly unrelated contexts. The ﬁrst of these concerns Dedekind sums. Let
ψ(x) denote the sawtooth function deﬁned by

ψ(x) =
 {
{x} − 1/2 if x ̸∈ Z,
0 if x ∈ Z,

which is an odd function, periodic with period 1. If q is prime and a is a reduced residue
(mod q), then the Dedekind sum sq(a) is deﬁned by

(1.6) sq(a) := ∑

x (mod q) ψ(x
q
 )
ψ( ax
q
 ).

The Dedekind sum arises naturally in number theory when studying the modular trans-
formation properties of the Dedekind η-function, but it also appears in other contexts and
satisﬁes many interesting properties [1, 11]. We study here the discrete Fourier transform of
the Dedekind sum sq(a). Thus for a prime q and residue class t (mod q) we deﬁne

(1.7) ̂sq(t) := 1
q
 ∑

a (mod q) sq(a)e(at/q),

where e(z) = e
2πiz throughout. In Lemma 2.1 we shall see that

̂sq(t) = −1
πiφ(q)
 ∑

χ̸=χ0 (mod q) ¯χ(t)L(0, χ)L(1, χ),

so that ̂sq(t) is indeed a simpler version of C(k). An alternative useful expression is

(1.8) ̂sq(t) = 1
πi
 ∞∑

n=1
(n,q)=1
 ψ(tn/q)
n ,

where n denotes the multiplicative inverse of the reduced residue class n (mod q) and the
sum converges since the partial sums ∑

n≤x,(n,q)=1 ψ(tn/q) are bounded.

4 ROBERT J. LEMKE OLIVER AND KANNAN SOUNDARARAJAN

Theorem 1.2. (1) As q → ∞ the distribution of πîsq(t) tends to a continuous probability
distribution, symmetric around 0. Precisely, there is a continuous function Φs with Φs(−x)+
Φs(x) = 1 such that uniformly for all x ∈ [−X, X] one has

1
q #{t (mod q) : πîsq(t) ≤ eγ
2 x} = Φs(x) + o(1).

(2) Uniformly for all e ≤ x ≤ ( 1
2 − ǫ) log log q one has

exp(−A1e
x/x) ≥ 1
q #{t (mod q) : πîsq(t) ≥ e
γ

2 x} ≥ exp(−A2e
x log x)

for some positive constants A1 and A2.
(3) For all large q, there exists t (mod q) with

−πîsq(−t) = πîsq(t) ≥ ( e
γ

4 − ǫ
) log log q.

(4) For all t (mod q) we have
 ̂sq(t) ≪ (log q) 2
3 (log log q)2.

(5) The values ̂sq(t) have an “almost periodic” structure. Precisely, suppose 1 ≤ m ≤ q/4
is a multiple of every natural number below B ≥ 2. Then

1
q
 ∑

t (mod q) |̂sq(t) − ̂sq(k + m)|2 ≪ 1
B1−ǫ + m
q log B.

Theorem 1.2 exactly parallels the results of Theorem 1.1, with the same deﬁciencies dis-
cussed there. The proofs of Theorems 1.1 and 1.2 are nearly identical, and so we give details
only for Theorem 1.1.
Our third topic concerns the remainder term in the asymptotic for the mean value of
Euler’s φ-function. Deﬁne the quantity R(x) by the relation

∑

n≤x φ(n) = 3
π2 x
2 + R(x).

Simple arguments show that R(x) ≪ x log x, and Walﬁsz [12] established that R(x) ≪
x(log x)2/3(log log x)4/3, which is presently the best known estimate. Montgomery [8] con-
jectured that R(x) ≪ x log log x and R(x) = Ω±(x log log x), and he showed that R(x) =
Ω±(x
√log log x). Key to Montgomery’s work is the expression

R(x) = φ(x)
2 − x ∑

n≤x
 µ(n)ψ(x/n)
n + O(
x exp(−c√log x))

for some positive constant c, where φ(x) = 0 if x ̸∈ Z. The sum in this expression is akin to
the equation (1.8) for ̂sq(t) with n/q replaced by 1/n and with the weight 1/n replaced with
µ(n)/n. Accordingly, many of the techniques used to prove Theorems 1.1 and 1.2 apply to
R(x) as well, though unfortunately with less precision owing to the presence of µ(n). For
convenience, we deﬁne ̃R(x) = R(x)/x − φ(x)/2x.

CONSECUTIVE PRIME BIASES AND SAWTOOTH RANDOM VARIABLES 5

Theorem 1.3. As y → ∞ the distribution of ̃R(u) for real u ≤ y tends to a probability
distribution, symmetric around 0. Precisely, there is a function ΦR with ΦR(−x)+ΦR(x) = 1
such that uniformly for all x ∈ [−X, X] one has
1
y meas({u ≤ y : ̃R(u) ≤ 3eγ
π2 x}) = ΦR(x) + o(1),

where meas(I) denotes the Lebesgue measure of I ⊆ R. Moreover, uniformly for all e ≤ x ≤
( 1
2 − ǫ) log log y one has

1
y meas({u ≤ y : ̃R(u) ≥ 3eγ
π2 x}) ≤ exp(−A1e
x/x)

for some positive constant A1.

We prove Theorem 1.3 by showing that all positive integral moments of ̃R(n) exist and
are not too large. The moment calculation reﬁnes earlier work of Pillai and Chowla [10] and
Chowla [3], who computed the mean and variance respectively:
∑

n≤x ̃R(n) = o(x) and 1
y
 ∫ y

0 ̃R(u)2 du ∼ 1
2π2 .

In Theorem 1.3, using Montgomery’s construction in his Ω-result, we can obtain a lower
bound for the frequency of large values of ̃R(u) of the form exp(−e
x2+ǫ), which is very far
from the upper bound. We expect that there is a lower bound similar to that in Theorems
1.1 and 1.2 in this situation also, and this would be in keeping with Montgomery’s conjecture
on the true size of ̃R(u).

Organization. Our main focus is the proofs of Theorems 1.1 and 1.2. We establish pre-
liminary results useful for both in Sections 2 and 3. We then prove Theorem 1.1 in Sections
4-6; since the proof of Theorem 1.2 follows along identical lines, we omit it. In Section 7, we
discuss the modiﬁcations that lead to Theorem 1.3.

2. First steps

Here we establish some formulae for ̂sq(t) and C(k) which will be the basis for our subse-
quent work.

Lemma 2.1. Let q be prime. For any (t, q) = 1, we have

̂sq(t) = −1
πiφ(q)
 ∑

χ̸=χ0 (mod q) ¯χ(t)L(0, χ)L(1, χ) = 1
πi
 ∞∑

n=1
(n,q)=1
 ψ(tn/q)
n .

Moreover, for any x ≥ 1 we have

̂sq(t) = 1
πi
 ∑

n≤x
(n,q)=1
 ψ(tn/q)
n + O( q
x
).

Proof. For any non-principal character χ (mod q), we have (see, e.g., [13, Theorem 4.2])

(2.1) L(0, χ) = − ∑

a (mod q) χ(a)ψ(a/q).

6 ROBERT J. LEMKE OLIVER AND KANNAN SOUNDARARAJAN

Notice that L(0, χ) = 0 if χ is an even character, and that right side of the formula in (2.1)
evaluates to 0 if χ is principal. The functional equation for odd characters gives

L(1, χ) = −τ (χ)πi
q L(0, ¯χ),

where τ (χ) = ∑

m (mod q) χ(m)e(m/q) denotes the Gauss sum. Thus we obtain
∑

χ̸=χ0 (mod q) ¯χ(t)L(0, χ)L(1, χ) = −πi
q
 ∑

χ (mod q) τ (χ)∣
∣
∣ ∑

a (mod q) χ(a)ψ( a
q
 )∣
∣
∣
2

= −πi
q
 ∑

a,b,m (mod q) e(m/q)ψ( a
q
 )
ψ( b
q
 ) ∑

χ (mod q) χ(am) ¯χ(bt)

= −φ(q)πi
q
 ∑

a,b̸≡0 (mod q) e
(tba
q
 )ψ(a
q
 )ψ( b
q
 )

= −φ(q)πi ̂sq(t).

The ﬁrst identity in the lemma follows.
To obtain the second identity, note that using (2.1) and the orthogonality relation for
characters

− ∑

χ̸=χ0 (mod q) χ(t)L(0, χ) ∑

n≤N
 χ(n)
n = ∑

χ (mod q) χ(t) ∑

a (mod q) χ(a)ψ(a/q) ∑

n≤N
 χ(n)
n

= φ(q) ∑

n≤N
(n,q)=1
 1
nψ(tn/q).(2.2)

Letting N → ∞, the second identity follows.
To obtain the truncated version, note that
∣
∣
∣ ∑

n≤x
(n,q)=1
 ψ(tn/q)∣
∣
∣ ≤ q

trivially, and therefore ∑

n>x
(n,q)=1
 ψ(tn/q)
n = ∫ ∞

x
 1
y2 ∑

x<n≤y ψ(tn/q)dy ≪ q
x.
 □

Recall the deﬁnition of Aq,χ from (1.2). Expanding this product out, we ﬁnd

(2.3) Aq,χ = (2χ(2) − χ(2)2) ∏

p∤2q
 (1 − 1
(p − 1)2
 )(
1 + 2χ(p) − χ(p)2

p2 − 2p
 ) = C
 ∞∑

n=1 a(n)χ(2n).

Here

(2.4) C = 2 ∏

p≥3
p∤q
 (1 − 1
(p − 1)2
 )
,

CONSECUTIVE PRIME BIASES AND SAWTOOTH RANDOM VARIABLES 7

and a(n) is a multiplicative function deﬁned by a(2) = −1/2 and a(2v) = 0 for all v ≥ 2,
and for odd primes p we have

(2.5) a(p) = 2
p(p − 2) , a(p2) = − 1
p(p − 2) , and a(pv) = 0 for all v ≥ 3.

From the deﬁnition of a(n) it is easy to check that ∑∞
n=1 |a(n)|n
σ converges for all σ < 1/2
so that

(2.6) ∑

n≥N |a(n)| ≪ N − 1
2 +ǫ and C ∑

n≤N
(n,q)=1
 a(n) = 1 + O(N − 1
2 +ǫ).

Lemma 2.2. Deﬁne the multiplicative function b(n) by setting b(n) = ∑

uv=n a(u)/v, so that
b(n) = 0 unless n is odd and square-free, and b(p) = 1/(p − 2) for all odd primes p. Then
for any natural number N we have

C(k) = −C ∑

n≤N
(n,q)=1
 b(n)ψ(k2n/q) + O(q 3
2 +ǫN − 1
4 +ǫ).

Proof. Arguing as in (2.2) we ﬁnd

(2.7) 1
φ(q)
 ∑

χ̸=χ0 (mod q) χ(k)L(0, χ) ∑

n≤N
(n,q)=1
 b(n)χ(2n) = − ∑

n≤N
(n,q)=1
 b(n)ψ(k2n/q).

Now if n = uv ≤ N then either u ≤ √N or v ≤ √N and √N < u ≤ N/v. Therefore

(2.8) ∑

n≤N b(n)χ(2n) = ∑

u≤√
N a(u)χ(2u) ∑

v≤N/u
 χ(v)
v + ∑

v≤√N
 χ(v)
v
 ∑

√N <u≤N/v a(u)χ(2u).

Bounding the partial sums of characters trivially, we ﬁnd

(2.9) L(1, χ) = ∑

n≤x
 χ(n)
n + ∫ ∞

x
 ∑

x<n≤y χ(n) dy
y2 = ∑

n≤x
 χ(n)
n + O( q
x
 )
,

and so the ﬁrst term in (2.8) is (using (2.6))
∑

u≤√
N a(u)χ(2u)(
L(1, χ) + O(qu
N
 ))

=C −1Aq,χL(1, χ) + O((log q)N − 1
4 +ǫ) + O(qN − 1
2 )

=C −1Aq,χL(1, χ) + O(qN − 1
4 +ǫ).

As for the second term in (2.8), using (2.6) we may bound this by

≪ ∑

v≤√N
 1
v N − 1
4 +ǫ ≪ N − 1
4 +ǫ.

We conclude that

C ∑

n≤N
(n,q)=1
 b(n)ψ(k2n/q) = − 1
φ(q)
 ∑

χ̸=χ0 (mod q) χ(k)L(0, χ)(Aq,χL(1, χ) + O(qN − 1
4 +ǫ))
,

and since L(0, χ) ≪ √q log q, the lemma follows. □

8 ROBERT J. LEMKE OLIVER AND KANNAN SOUNDARARAJAN

Lemmas 2.1 and 2.2 give crude approximations to ̂sq(t) and C(k) by long sums (for example
taking x = q2 in Lemma 2.1, or taking N = q8 in Lemma 2.2). However, on average over t
or k, it is possible to approximate these quantities by very short sums.

Lemma 2.3. Let 1 ≤ B < q be a real number. Then
1
φ(q)
 ∑

k (mod q)
 ∣
∣
∣C(k) + C ∑

n≤B b(n)ψ(k2n/q)∣
∣
∣
2 ≪ B−1+ǫ,

and 1
φ(q)
 ∑

t (mod q)
 ∣
∣
∣̂sq(t) − 1
πi
 ∑

n≤B
 ψ(tn/q)
n
 ∣
∣
∣
2 ≪ B−1+ǫ.

Proof. We shall content ourselves with proving the estimate for C(k), the situation for ̂sq(t)
being entirely similar. Using (2.7) and Lemma 2.2 we see that
1
φ(q)
 ∑

k (mod q)
 ∣
∣
∣C(k) + C ∑

n≤B b(n)ψ(k2n/q)∣
∣
∣
2

= 1
φ(q)
 ∑

k (mod q)
 ∣
∣
∣ C
φ(q)
 ∑

χ̸=χ0 (mod q) χ(k)L(0, χ) ∑

B<n≤q10 b(n)χ(2n) + O(q−1+ǫ)∣
∣
∣
2.

Using the orthogonality of characters to evaluate the sum over k, this is

≪ 1
φ(q)2 ∑

χ̸=χ0 (mod q) |L(0, χ)|2∣
∣
∣ ∑

B<n≤q10 b(n)χ(n)∣
∣
∣2 + q−2+ǫ,

and using (2.9) and the functional equation this is

≪ 1
q
 ∑

χ̸=χ0 (mod q)
 ∣
∣
∣ ∑

m≤q2
 χ(m)
m
 ∑

B<n≤q10 b(n)χ(n)∣
∣
∣2 + q−2+ǫ.

Write temporarily ∑

m≤q2
 χ(m)
m
 ∑

B<n≤q10 b(n)χ(n) = ∑

B<n≤q12
 α(n)
n χ(n),

for some coeﬃcients α(n) ≪ n
ǫ. Then (including also the contribution of χ0 below)
1
q
 ∑

χ̸=χ0 (mod q)
 ∣
∣
∣ ∑

B<n≤q12
 α(n)
n χ(n)∣
∣
∣2 ≪ ∑

B<n1,n2≤q12
n1≡n2 (mod q)
 |α(n1)α(n2)|
n1n2 .

The terms with n1, n2 both below q (so that n1 = n2) contribute

≪ ∑

B<n<q
 n
ǫ

n2 ≪ B−1+ǫ.

The terms with max(n1, n2) ≥ q contribute (assume without loss of generality that n2 is the
larger one)
 ≪ qǫ ∑

B<n1≤q12
 1
n1
 ∑

q<n2≤q12
n2≡n1 (mod q)
 1
n2 ≪ qǫ log q log q
q ≪ q−1+ǫ.

Assembling these estimates, the lemma follows. □

CONSECUTIVE PRIME BIASES AND SAWTOOTH RANDOM VARIABLES 9

3. A key quantity

We shall study ̂sq(t) and C(k) by computing their moments, and the following key quantity
will arise in this context. Let ℓ be a natural number, and suppose n1, . . ., nℓ are ℓ natural
numbers. Then set

(3.1) B(n1, . . . , nℓ) = 1
n1 · · · nℓ
 ∫ n1···nℓ

0
 ℓ∏

j=1 ψ(x/nj)dx.

Proposition 3.1. The quantity B(n1, . . . , nℓ) satisﬁes the following properties.
(1) If ℓ is odd then B(n1, . . . , nℓ) = 0. For even ℓ we have

(3.2) B(n1, . . . , nℓ) = ( i
2π
 )ℓ ∑

k1,...,kℓ̸=0∑ kj/nj =0
 1
k1 · · · kℓ ,

where the sum is over all non-zero integers kj, and this sum is absolutely convergent. In the
case ℓ = 2 one has
 B(n1, n2) = (n1, n2)2

12n1n2 .

(2) If p is a prime dividing nj and such that p does not divide any other ni, then

B(n1, . . . , nj, . . . , nℓ) = 1
p B(n1, . . . , nj/p, . . . , nℓ).

(3) If we write n1 · · · nℓ = rs where r and s are coprime and r is square-free while s is
square-full then |B(n1, . . . , nℓ)| ≤ 2−ℓr−1.

We begin by recalling the Fourier expansion of the sawtooth function. Note that ̂ψ(0) = 0
and for k ̸= 0 we have

(3.3) ̂ψ(k) = ∫ 1

0 ψ(x)e(−kx)dx = 1
−2πik = i
2πk ,

and so

(3.4) ψ(x) = i ∑

k̸=0
 e(kx)
2πk .

This series converges conditionally pointwise for each x ̸∈ Z, and also in the L
2-sense. For
any non-negative integer N, recall also the Fejer kernel

(3.5) KN (x) =
 N∑

j=−N
 (
1 − |j|
N + 1
)e(jx) = 1
N + 1
 (sin(π(N + 1)x)
sin πx
 )2.

We shall ﬁnd it convenient to replace ψ(x) by the approximation ψN (x) deﬁned by

(3.6) ψN (x) = i ∑

0<|k|≤N
 e(kx)
2πk
 (1 − |k|
N + 1
).

Note that ψN is the convolution of ψ with the Fejer kernel KN

ψN (x) = ∫ 1

0 ψ(y)KN (x − y)dy,

10 ROBERT J. LEMKE OLIVER AND KANNAN SOUNDARARAJAN

and so

(3.7) |ψN (x) − ψ(x)| ≪ min (
1, 1
N∥x∥
 ),

which implies that

(3.8) ∫ 1

0 |ψN (x) − ψ(x)|dx ≪ 1 + log N
N .

Note also that |ψN (x)| ≤ 1/2 always.

Proof of Proposition 3.1: Part 1. Since ψ is an odd function, it is clear that B(n1, . . . , nℓ) = 0
for odd ℓ. Now suppose ℓ is even. By Parseval it follows that
(3.9) 1
n1 · · · nℓ
 ∫ n1···nℓ

0 ψN (x/n1) · · · ψN (x/nℓ)dx = ( i
2π
 )ℓ ∑

0<|kj|≤N∑ kj/nj =0
 1
k1 · · · kℓ
 ℓ∏

j=1
 (1 − |kj|
N + 1
 )
.

For any complex numbers α1, . . ., αℓ and β1, . . ., βℓ note the simple identity

(3.10) α1 · · · αℓ − β1 · · · βℓ = (α1 − β1)α2 · · · αℓ + β1(α2 − β2)α3 · · · αℓ + β1 · · · βℓ−1(αℓ − βℓ).

Applying this, we obtain

|ψ(x/n1) · · · ψ(x/nℓ) − ψN (x/n1) · · · ψN (x/nℓ)| ≤ 1
2ℓ−1
 ℓ∑

j=1 |ψ(x/nj) − ψN (x/nj)|,

and so by (3.9) and (3.8) we conclude that

B(n1, . . . , nℓ) = 1
n1 · · · nℓ
 ∫ n1···nℓ

0 ψ(x/n1) · · · ψ(x/nℓ)dx

= ( i
2π
 )ℓ ∑

0<|kj|≤N∑ kj /nj=0
 1
k1 · · · kℓ
 ℓ∏

j=1
 (
1 − |kj|
N + 1
 ) + O(1 + log N
N
 )
.(3.11)

We now show that ∑

0<|kj|≤N∑ kj /nj=0
 1
|k1 · · · kℓ|

is bounded, so that (3.11) will imply (letting N → ∞) the stated formula (3.2) for B(n1, . . . , nℓ)
and that the sum there converges absolutely. By Parseval

∑

0<|kj|≤N∑ kj/nj =0
 1
|k1 · · · kℓ| = 1
n1 · · · nℓ
 ∫ n1···nℓ

0
 ℓ∏

j=1
 ( ∑

0<|kj|≤N
 e(kjx/nj)
|kj|
 )dx.

One may check that (with ∥x∥ denoting the distance of x from the nearest integer)
∑

0<|k|≤N
 e(kθ)
|k| ≪ log min (
N, 1
∥θ∥
 ) ≪ log N
1 + N∥θ∥ .

CONSECUTIVE PRIME BIASES AND SAWTOOTH RANDOM VARIABLES 11

Using this and the arithmetic-geometric mean inequality above, we ﬁnd

∑

0<|kj|≤N∑ kj/nj =0
 1
|k1 · · · kℓ| ≪
 ℓ∑

j=1
 1
n1 · · · nℓ
 ∫ n1···nℓ

0
 ( log N
1 + N∥x/nj∥
 )ℓdx

≪ ∫ 1

0
 ( log N
1 + N∥x∥
 )ℓdx ≪ 1.

This proves our claim, and establishes (3.2).
If ℓ = 2 then the condition k1/n1 + k2/n2 = 0 means that k1 = rn1/(n1, n2) and k2 =
−rn2/(n1, n2) for some non-zero integer r. Therefore

B(n1, n2) = − 1
4π2 ∑

r̸=0
 −1
r2 (n1, n2)2

n1n2 = (n1, n2)2

12n1n2 .
 □

Proof of Proposition 3.1: Parts 2 and 3. If p divides nj and no other ni, then, in (3.2), kj
must necessarily be a multiple of p. Cancelling p from kj and nj, Part 2 follows. Part 3
follows from Part 2, and noting that |B(n1, . . . , nℓ)| ≤ 2−ℓ always. □

For computing the moments of ̂sq(t) and C(k) the following proposition, which connects
correlations of the sawtooth function with B, will be very useful.

Proposition 3.2. Let n1, . . ., nℓ be positive integers. Deﬁne K = n1 · · · nℓ/ min(n1, . . . , nℓ).
If K < q/ℓ then

1
q
 ∑

k (mod q) ψ(kn1/q) · · · ψ(knℓ/q) = B(n1, . . . , nℓ) + O(ℓK
q log (eq
K
 ))
.

Proof. Take N = ⌊q/(ℓK)⌋. The identity (3.10) gives
∑

k (mod q) |ψ(kn1/q) · · · ψ(knℓ/q) − ψN (kn1/q) · · · ψN (knℓ/q)|

≤ 1
2ℓ−1
 ℓ∑

j=1
 ∑

k (mod q) |ψ(knj/q) − ψN (knj/q)|.

Using now (3.7), the above is

(3.12) ≪ 1
2ℓ
 ℓ∑

j=1
 ∑

k (mod q) min (1, 1
N∥knj/q∥
 ) ≪ q
N log(eN).

By Parseval
(3.13)
1
q
 ∑

k (mod q) ψN (kn1/q) · · · ψN (knℓ/q) = ( i
2π
 )ℓ ∑

0<|kj|≤N∑j kjnj ≡0 (mod q)
 1
k1 · · · kℓ
 ℓ∏

j=1
 (
1 − |kj|
N + 1
 )
,

which bears a striking resemblance to (3.9). With our choice for N, we claim that in fact
the right side of (3.13) is exactly equal to the expression in (3.9). Multiplying through

12 ROBERT J. LEMKE OLIVER AND KANNAN SOUNDARARAJAN

by n1 · · · nℓ, the congruence ∑ kjnj ≡ 0 (mod q) becomes ∑

j kj(n1 · · · nℓ/nj) ≡ 0 (mod q).
Since |kj| < q/(ℓK) and (n1 · · · nℓ/nj) ≤ K for all j, it follows that | ∑

j kj(n1 · · · nℓ/nj)| < q
so that the congruence becomes the equality ∑

j kj(n1 · · · nℓ/nj) = 0, which is the same as
the criterion ∑

j kj/nj = 0 of (3.9). Combining this observation with (3.11) and (3.12), our
proposition follows. □

4. The moments of ̂sq(t) and C(k)

We now state our main result on computing the moments of ̂sq(t) and C(k).

Theorem 4.1. Let q be a prime, and ℓ a natural number. Then, uniformly in the range
ℓ ≤ √log q/ log log q,

(4.1) 1
q
 ∑

k (mod q) C(k)ℓ = MC(ℓ) + O(q−1/(20ℓ log ℓ)),

where
 MC(ℓ) = C ℓ ∑

n1,...,nℓ≥1 b(n1) · · · b(nℓ)B(n1, . . . , nℓ).

The quantity MC(ℓ) equals zero for all odd ℓ, and for even ℓ satisﬁes

(4.2) e
γ

2 (log ℓ − log log ℓ + O(1)) ≤ MC(ℓ) 1
ℓ ≤ e
γ

2 log ℓ + O(1).

Theorem 4.2. Let q be a prime, and ℓ a natural number. Then, uniformly in ℓ,

1
q
 ∑

t (mod q)
(πîsq(t))ℓ = Ms(ℓ) + O(q−1/(20ℓ log ℓ)),

where
 Ms(ℓ) = ∑

n1,...,nℓ≥1
 B(n1, . . . , nℓ)
n1 · · · nℓ .

The quantity Ms(ℓ) equals zero for all odd ℓ, and for even ℓ satisﬁes

e
γ

2 (log ℓ − log log ℓ + O(1)) ≤ Ms(ℓ) 1
ℓ ≤ e
γ

2 log ℓ + O(1).

We conﬁne ourselves to proving Theorem 4.1, and the proof of Theorem 4.2 follows along
similar lines. In the rest of this section, we establish the asymptotic (4.1) and the upper
bound in (4.2); the lower bound in (4.2) needs more work, and will be treated in the next
section.

Proof of (4.1). Since C(−k) = −C(k) the odd moments of C(k) vanish. When ℓ is odd,
B(n1, . . . , nℓ) = 0 and so the quantity MC(ℓ) is also zero here. In what follows, we may
therefore assume that ℓ is an even natural number.

CONSECUTIVE PRIME BIASES AND SAWTOOTH RANDOM VARIABLES 13

Let 1 ≤ B ≤ q be a parameter to be chosen shortly. Note that
∣
∣
∣C(k)ℓ − ( − C ∑

n≤B b(n)ψ( k2n
q
 ))ℓ∣
∣
∣

≤
∣
∣
∣C(k) + C ∑

n≤B b(n)ψ( k2n
q
 )∣
∣
∣ ·
 ℓ−1∑

j=0 |C(k)|j∣
∣
∣C ∑

n≤B b(n)ψ( k2n
q
 )∣
∣
∣
ℓ−1−j

≤(C0 log q)ℓ−1∣
∣
∣C(k) + C ∑

n≤B b(n)ψ( k2n
q
 )∣
∣
∣,

for some absolute constant C0. By Cauchy-Schwarz and Lemma 2.3,

1
q
 ∑

k (mod q)
 ∣
∣
∣C(k) + C ∑

n≤B b(n)ψ( k2n
q
 )∣
∣
∣ ≪ B− 1
2 +ǫ.

We choose B = q1/ℓ, and (in the range ℓ ≤ √log q/ log log q) deduce that

1
q
 ∑

k (mod q) C(k)ℓ = 1
q
 ∑

k (mod q)
 (
C ∑

n≤B b(n)ψ( k2n
q
 ))ℓ + O(q− 1
4ℓ ).

Expand out the main term above, replace k (mod q) by 2k (mod q), and appeal to Proposi-
tion 3.2 with K there being ≤ q(ℓ−1)/ℓ. It follows that

(4.3) 1
q
 ∑

k (mod q) C(k)ℓ = C ℓ ∑

n1,...,nℓ≤q1/ℓ b(n1) · · · b(nℓ)B(n1, . . . , nℓ) + O(q− 1
4ℓ ).

It remains now to bound the diﬀerence between the main term in (4.3) and the expression
for MC(ℓ), which is

≤ C ℓ ∑

n>q1/ℓ
 ∑

n1···nℓ=n b(n1) · · · b(nℓ)|B(n1, . . . , nℓ)| ≤ (C/2)ℓ ∑

n>q1/ℓ
 ∑

n1···nℓ=n b(n1) · · · b(nℓ) 1
sf(n) ,

where sf(n) is the largest squarefree divisor d of n that is coprime to n/d. We estimate the
sum above by Rankin’s trick; with α = 1/(10 log ℓ) the above is

≤ (C/2)ℓq−α/ℓ ∞∑

n=1
 ∑

n1···nℓ=n b(n1) · · · b(nℓ) n
α

sf(n)

≤ e
O(ℓ)q−α/ℓ ∏

p≥3
 (1 + ℓpα

p(p − 2) +
 ℓ∑

j=2
 (ℓ
j
) pjα

(p − 2)j
 ),

upon recalling the deﬁnition of b(n). The contribution of primes p ≤ ℓ to the product above
is
 ≤ ∏

3≤p≤ℓ
 (
1 + pα

p − 2
 )ℓ ≤ (log ℓ)ℓe
O(ℓ),

while the contribution of primes p > ℓ to the product above is

≪ ∏

p>ℓ exp (O(ℓ2p2α

p2
 )) = e
O(ℓ).

14 ROBERT J. LEMKE OLIVER AND KANNAN SOUNDARARAJAN

We conclude that the diﬀerence between the main term in (4.3) and the expression for MC(ℓ)
is ≪ (log ℓ)ℓe
O(ℓ)q−α/ℓ ≪ q−1/(20ℓ log ℓ),
completing the proof of (4.1). □

Proof of the upper bound in (4.2). Note that

MC(ℓ) ≤ C ℓ ∑

n1,...,nℓ b(n1) · · · b(nℓ)|B(n1, . . . , nℓ)| ≤ (C/2)ℓ ∑

n1,...,nℓ
 b(n1) · · · b(nℓ)
sf(n)

≤ (C/2)ℓ ∏

p≥3
 (1 + ℓ
p(p − 2) +
 ℓ∑

j=2
 (ℓ
j
) 1
(p − 2)j
 )
.

The contribution of primes p ≤ ℓ is

≤ ∏

3≤p≤ℓ
 (
1 + 1
p − 2
 )ℓ = ( ∏

3≤p≤ℓ
 (
1 − 1
(p − 1)2
 )−1(1 − 1
p
 )−1)ℓ = C −ℓ(e
γ log ℓ + O(1))ℓ,

upon using Mertens’s theorem. The contribution of primes p > ℓ is

exp ( ∑

p>ℓ O( ℓ2

p2
 )) = exp (
O( ℓ
log ℓ
))
,

and so the upper bound in (4.2) follows. □

5. Completing the proof of Theorem 4.1: Proof of the lower bound in (4.2)

To obtain the lower bound in (4.2) we take an indirect approach, working with a continuous
model that has the same moments as C(k). Let B be a positive integer, and let L(B) denote
the least common multiple of the natural numbers n ≤ B. For a real number x, deﬁne

C(x; B) = C ∑

n≤B b(n)ψ(x/n).

It follows readily that

1
L(B)
 ∫ L(B)

0 C(x; B)ℓdx = C ℓ ∑

n1,...,nℓ≤B b(n1) · · · b(nℓ)B(n1, . . . , nℓ),

so that

(5.1) MC(ℓ) = lim
B→∞ 1
L(B)
 ∫ L(B)

0 C(x; B)ℓdx.

We shall obtain a lower bound for the right side of (5.1); naturally, we may assume that ℓ is
even and large.
Suppose that B > ℓ, and put ℓ0 = ℓ/ log ℓ. Let I denote the subset of [0, L(B)] consisting
of points x = kL(ℓ0) − y with 1 ≤ k ≤ L(B)/L(ℓ0), and 0 < y ≤ 1/10. Let ψ+(t) = ψ(t)
whenever t is not an integer, and ψ+(t) = 1/2 when t is an integer. Then for x = kL(ℓ0)−y ∈
I note that

C(x; B) = C ∑

n≤B b(n)ψ((kL(ℓ0) − y)/n) = C ∑

n≤B b(n)(ψ+(kL(ℓ0)/n) − y/n
)
.

CONSECUTIVE PRIME BIASES AND SAWTOOTH RANDOM VARIABLES 15

Since, for n ≤ B,
 L(B)/L(ℓ0)∑

k=1 ψ+( kL(ℓ0)
n
 ) = 1
2 L(B)
L(ℓ0) (n, L(ℓ0))
n ,

it follows that (note |I| = L(B)/(10L(ℓ0)))

1
|I|
 ∫

I C(x; B)dx = C
2
 ∑

n≤B b(n) (n, L(ℓ0)) − 1/20
n ,

and therefore by H¨older’s inequality that

1
L(B)
 ∫ B

0 C(x, B)ℓdx ≥ 1
10L(ℓ0) 1
|I|
 ∫
I C(x; B)ℓdx ≥ 1
10L(ℓ0)
 (C
2
 ∑

n≤B b(n) (n, L(ℓ0)) − 1/20
n
 )ℓ.

Now letting B → ∞, we ﬁnd by (5.1) that

MC(ℓ) ≥ 1
10L(ℓ0)
 ( C
2
 ∞∑

n=1
 b(n)(n, L(ℓ0))
n + O(1))ℓ ≥ e
−O(ℓ0)(C
2
 ∏

3≤p≤ℓ0
 (1 + 1
p − 2
 ) + O(1))ℓ,

upon using the prime number theorem to estimate L(ℓ0), and recalling the deﬁnition of b.
Now C
2
 ∏

3≤p≤ℓ0
 (1 + 1
p − 2
 ) = ∏

3≤p≤ℓ0
 (1 − 1
p
 )−1(1 + O( 1
ℓ0
 )) = e
γ

2 log ℓ0 + O(1),

and therefore the lower bound in (4.2) follows.

6. Proof of Theorem 1.1

Proof of Part 1. Theorem 4.1 shows that all the moments of C(k) exist, and do not grow too
rapidly. The moment generating function ∑∞
ℓ=0 x
ℓMC(ℓ)/ℓ! converges for all x, and therefore
the sequence of moments MC(ℓ) uniquely determines a distribution, which is the limiting
distribution for C(k). Since C(k) = −C(−k), the limiting distribution is clearly symmetric
around 0.
To gain an understanding of this limiting distribution, and to establish its continuity, it
is helpful to think of the continuous model C(x; B) discussed in Section 5. Consider the
characteristic function (that is, Fourier transform) of C(x; B); namely

E(e
itC(x,B)) = 1
L(B)
 ∫ L(B)

0 e
itC(x,B)dx.

Omit the measure zero set of integers x, and write x = k − y with 1 ≤ k ≤ L(B) and
0 < y < 1. Then, with ψ+ as in Section 5 and C +(x; B) = C ∑
b≤B b(n)ψ+(x/b), we have
C(x; B) = C +(k; B) − y ∑

n≤B b(n)/n, and so

(6.1) 1
L(B)
 ∫ L(B)

0 e
itC(x,B)dx = 1
L(B)
 L(B)∑

k=1 e
itC+(k,B) ∫ 1

0 e
−ity ∑n≤B b(n)/ndy ≪ 1
1 + |t| .

Given an interval I = (α − ǫ, α + ǫ) with ǫ < 1/2, we can readily ﬁnd a majorant Ψ(x)
of the indicator function of I, with | ̂Ψ(x)| ≪ ǫ/(1 + (ǫx)2). For example take Ψ(x) =

16 ROBERT J. LEMKE OLIVER AND KANNAN SOUNDARARAJAN

max(2 − |x − α|/ǫ, 0), which is a relative of the Fejer kernel. Then by Fourier inversion

1
L(B)
 ∫

x∈[0,L(B)]
C(x,B)∈I dx ≤ 1
L(B)
 ∫ L(B)

0 Ψ(C(x, B))dx

= ∫ ∞

−∞ ̂Ψ(t)E(e
itC(x,B))dt ≪ ∫ ∞

−∞
 1
1 + |t| ǫ
1 + (ǫt)2 dt ≪ ǫ log(1/ǫ).

Therefore C(x, B) has a continuous distribution, and the continuity is uniform in B, so that
letting B → ∞, we conclude that the limiting distribution for C(k) is also continuous. □

Proof of Parts 2 and 3. Since Part 3 follows upon taking x = ( 1
2 − ǫ) log log q in Part 2, it is
enough to prove Part 2. For any even ℓ ≤ √log q/ log log q, we see using Theorem 4.1 that

1
q #{k (mod q) : C(k) ≥ e
γ

2 x} ≤ (e
γ

2 x
)−ℓ(MC(ℓ) + o(1)) ≪ (log ℓ + O(1)
x
 )ℓ.

Choosing ℓ to be an even integer around Ae
x for a suitably small positive constant A, the
upper bound in Part 2 follows.
To establish the lower bound in Part 2, note that for even ℓ ≤ √log q/(2 log log q), we have
by Theorem 4.1

(6.2) (e
γ

2 (log ℓ − log log ℓ + O(1)))ℓ ≪ 1
q
 ∑

k (mod q) C(k)ℓ.

The contribution from terms k with |C(k)| ≤ eγ
2 (log ℓ − log log ℓ − A) for a suitably large
constant A is clearly negligible compared to the right side of (6.2). The contribution from
terms k with |C(k)| ≥ eγ
2 (log ℓ + log log ℓ + A) for a suitably large constant A is

≤ (e
γ

2 (log ℓ + log log ℓ + A))−ℓ 1
q
 ∑

k (mod q) C(k)2ℓ

≪ (e
γ

2 (log ℓ + log log ℓ + A))−ℓ( e
γ

2 log ℓ + O(1))2ℓ,

upon using Theorem 4.1 to estimate the 2ℓ-th moment. If A is suitably large, then this too
is negligible in comparison to the right side of (6.2). Therefore it is the terms with |C(k)|
lying between eγ
2 (log ℓ − log log ℓ − A) and eγ
2 (log ℓ + log log ℓ + A) that account for the bulk
of the contribution to (6.2), and so
(e
γ

2 (log ℓ + log log ℓ + A))ℓ 1
q #{k : |C(k)| ≥ eγ
2 (log ℓ − log log ℓ − A)}

≫(e
γ

2 (log ℓ − log log ℓ + O(1)))ℓ.

Choosing ℓ of size xe
x, the lower bound in Part 2 follows. □

Proof of Part 4. First suppose that C(k) is negative. From [9] (Chapter 1, page 6) we recall
that for each natural number K there is a trigonometric polynomial

BK(x) = 1
2(K + 1) + ∑

1≤|j|≤K cje(jx)

CONSECUTIVE PRIME BIASES AND SAWTOOTH RANDOM VARIABLES 17

with cj ≪ 1/j, such that BK(x) ≥ ψ(x) for all x. Using Lemma 2.2 with N = q8 we obtain

0 ≤ −C(k) = C ∑

n≤q8
(n,q)=1
 b(n)ψ(k2n/q) + O(1) ≤ C ∑

n≤q8 b(n)BK(k2n/q) + O(1).

Thus, for some positive constant A,

(6.3) − C(k) ≤ A
(
1 + 1
K + 1
 ∑

n≤q8 b(n) + ∑

1≤|j|≤K
 1
j
 ∣
∣
∣ ∑

n≤q8
(n,q)=1
 b(n)e
( kj2n
q
 )∣
∣
∣
).

At this stage, we need the following result which follows from work of Bourgain and Garaev
[2] (reﬁning earlier work of Karatsuba [5]; see also Korolev [6]).

Lemma 6.1. Let q be a prime, and a be any integer coprime to q. Then for all N ≥ 1
∣
∣
∣ ∑

n≤N
(n,q)=1
 1
ne
( an
q
 )∣
∣
∣ ≪ (log q) 2
3 (log log q)2.

Proof. Theorem 16 of Bourgain and Garaev [2] gives
∣
∣
∣ ∑

n≤x e
( an
q
 )∣
∣
∣ ≪ x

(log x) 3
2 log q(log log q)3.

Partial summation using this bound for x ≥ exp((log q) 2
3 (log log q)2), and the trivial bound
(that the sum is at most x) for smaller x yields the lemma. □

Returning to (6.3), take there K = ⌊log q⌋. Then the right side of (6.3) is (recalling the
deﬁnition b(n) = ∑
uv=n a(u)/v)

≪ 1 + ∑

j≤K
 1
j
 ∑

u≤q8
(u,q)=1
 |a(u)|∣
∣
∣ ∑

v≤q8/u
(v,q)=1
 1
v e
(kj2uv
q
 )∣
∣
∣ ≪ (log q) 2
3 (log log q)3,

using Lemma 6.1 and since ∑

n |a(n)| ≪ 1. This proves that −C(k) ≤ A(log q) 2
3 (log log q)3,
which is the desired bound in the case C(k) negative. Arguing similarly with a minorant
for ψ(x) instead of a majorant, leads to the same bound for C(k) in the case when it is
positive. □

Proof of Part 5. Applying Lemma 2.3 we ﬁnd that

1
q
 ∑

k (mod q) |C(k) − C(k + m)|2 ≪ B−1+ǫ + 1
q
 ∑

k (mod q)
 ∣
∣
∣ ∑

n≤B b(n)(ψ( (k + m)2n
q
 ) − ψ(k2n
q
 ))∣
∣
∣
2.

Using Cauchy-Schwarz the second term above is

(6.4) ≪ 1
q
 ( ∑

n≤B b(n)) ∑

n≤B b(n) ∑

k (mod q)
 (
ψ( k + m2n
q
 ) − ψ(k
q
 ))2,

where in the inner sum we replaced k by 2kn. Since |ψ((k + a)/q) − ψ(k/q)| ≤ |a|/q unless
there is an integer between k/q and (k + a)/q, we may check that
1
q
 ∑

k (mod q)
 (ψ(k + a
q
 ) − ψ( k
q
 ))2 ≪ a
q .

18 ROBERT J. LEMKE OLIVER AND KANNAN SOUNDARARAJAN

Since m is a multiple of all numbers B (and recalling that b(n) = 0 unless n is odd), we may
write m2n = qr + a with a = m/(2n). Therefore the quantity in (6.4) is

≪ (log B) ∑

n≤B
 m
nq ≪ m
q log B,

completing our proof. □

7. Proof of Theorem 1.3

As in the proofs of Theorems 1.1 and 1.2, the main result is to compute the moments of
̃R(u). The proof of Theorem 1.3 then follows in exactly the same way as the corresponding
parts of Theorem 1.1.

Theorem 7.1. There is a positive number c < 1 such that uniformly for all natural numbers
ℓ in the range ℓ ≤ c
9√log y/log log y, we have

1
y
 ∫ y

0 ̃R(u)ℓ du = MR(ℓ) + O( exp ( − c
8
 √
log y))
,

where
 MR(ℓ) = ∑

n1,...,nℓ
 µ(n1) . . . µ(nℓ)
n1 . . . nℓ B(n1, . . . , nℓ).

For odd ℓ, MR(ℓ) = 0, while MR(2) = 1/2π2 and for even ℓ ≥ 4 we have

MR(ℓ) ≤ ( 3e
γ

π2 log ℓ + O(1))ℓ.

We begin with a lemma, which will allow us to truncate ̃R(u) by a short sum of sawtooth
functions.

Lemma 7.2. For all 1 ≤ N ≤ y we have
∑

N <n1,n2≤2N
 ∣
∣
∣ 1
y
 ∫ y

0 ψ(x/n1)ψ(x/n2)dx
∣
∣
∣ ≪ (log y)2(
N + N 2 √N
√y
 ).

Proof. Let K ≥ 2 be a parameter to be chosen shortly, and let ψK(x) be as in (3.6). First
note that

1
y
 ∫ y

0 |ψ(x/n1)ψ(x/n2) − ψK(x/n1)ψK(x/n2)|dx ≤ 1
y
 ∫ y

0
 2∑

j=1 |ψ(x/nj) − ψK(x/nj)|dx ≪ 1
K ,

upon using (3.8), and since n1 and n2 are at most N ≤ y. Next, from the Fourier expansion
of ψK (see (3.6)) it follows that
1
y
 ∣
∣
∣ ∫ y

0 ψK(x/n1)ψK(x/n2)dx
∣
∣
∣ ≪ ∑

0<|k1|,|k2|≤K
 1
|k1k2|
 ∣
∣
∣ 1
y
 ∫ y

0 e
(x
( k1
n1 + k2
n2
 ))
dx
∣
∣
∣

≪ ∑

0<|k1|,|k2|≤K
 1
|k1k2| min (
1, 1
y|k1/n1 + k2/n2|
 )
.

From these two estimates it follows that the sum to be bounded is

≪ N 2

K + ∑

0<|k1|,|k2|≤K
 1
|k1k2|
 ∑

N <n1,n2≤2N min (
1, 1
y|k1/n1 + k2/n2|
).

CONSECUTIVE PRIME BIASES AND SAWTOOTH RANDOM VARIABLES 19

To estimate the sum above, we split the terms into two groups: those with |k1/n1+k2/n2| ≥
K/y and those terms with |k1/n1 + k2/n2| < K/y. The ﬁrst group contributes

≪ N 2

K
 ∑

0<|k1|,|k2|≤K
 1
|k1k2| 1
|k1k2| ≪ N 2

K (log K)2.

Terms in the second group only exist for k1 and k2 of opposite sign, and here |k1n2 + k2n1| ≪
KN 2/y, so that if k1, n1, and k2 are ﬁxed, then n2 has ≪ 1 + KN 2/y choices. Therefore the
second group contributes

≪ (
1 + KN 2

y
 )N ∑

0<|k1|,|k2|≤K
 1
|k1k2| ≪ (log K)2N(1 + KN 2

y
 )
.

Choosing K = 2⌈
√y/N⌉, the lemma follows. □

Proof of Theorem 7.1. From Theorem 1 and Lemma 1 of [8] (but beware of the changes in
notation, especially that his saw tooth function diﬀers from ours in sign) it follows that with
N = y exp(−c√log y) for a suitable positive constant c < 1, one has

̃R(u) = − ∑

n≤N
 µ(n)
n ψ(u/n) + O(exp(−c√log y)),

for all N ≤ u ≤ y. Since ̃R(u) and the sum over n above are ≪ log y, it follows that for
ℓ ≤ c
9√log y/ log log y

(7.1) 1
y
 ∫ y

0 ̃R(u)ℓdu = (−1)ℓ

y
 ∫ y

0
 ( ∑

n≤N
 µ(n)
n ψ(u/n))ℓdu + O(exp(− c
2√log y)).

Now applying (3.10) we see that

1
y
 ∫ y

0
 ( ∑

n≤N
 µ(n)
n ψ(u/n))ℓdu = 1
y
 ∫ y

0
 ( ∑

n≤y1/(2ℓ)
 µ(n)
n ψ(u/n))ℓdu

+ O(ℓ(log y)ℓ−1

y
 ∫ y

0
 ∣
∣
∣ ∑

y1/(2ℓ)≤n≤N
 µ(n)
n ψ(u/n)∣
∣
∣du)
.(7.2)

Expanding out, the main term in (7.2) is

∑

n1,...,nℓ≤y1/(2ℓ)
 µ(n1) · · · µ(nℓ)
n1 · · · nℓ
 1
y
 ∫ y

0
 ℓ∏

j=1 ψ(u/nj)du

= ∑

n1,...,nℓ≤y1/(2ℓ)
 µ(n1) · · · µ(nℓ)
n1 · · · nℓ (B(n1, . . . , nℓ) + O(n1 · · · nℓ)).

Arguing as in the proof of Theorem 4.1, this may be seen to equal MR(ℓ) + O(y−1/(40ℓ log ℓ)).
As for the remainder term in (7.2), splitting the terms y1/(2ℓ) ≤ n ≤ N into dyadic blocks,
we may bound this by

≪ exp( c
8 √
log y) max
y1/(2ℓ)≤M ≤N
I⊂[M,2M ]
 1
y
 ∫ y

0
 ∣
∣
∣ ∑

n∈I
 µ(n)
n ψ(u/n)∣
∣
∣du,

20 ROBERT J. LEMKE OLIVER AND KANNAN SOUNDARARAJAN

where the maximum is over subintervals I of [M, 2M]. By Cauchy-Schwarz and Lemma 7.2,
this is
 ≪ exp( c
8 √
log y) max
y1/(2ℓ)≤M ≤N
I⊂[M,2M ] (log y)( 1
M +
 √M
√y
 ) 1
2 ≪ exp(− c
8√log y).

This justiﬁes the ﬁrst claim of the theorem. It is also clear that MR(ℓ) = 0 for odd ℓ, and
the formula for MR(2) follows from our knowledge of B(n1, n2). Lastly, the claimed upper
bound on MR(ℓ) follows exactly as the upper bound for MC(ℓ) in Theorem 4.1. □

References

[1] T. M. Apostol. Modular functions and Dirichlet series in number theory, volume 41 of Graduate Texts
in Mathematics. Springer-Verlag, New York, second edition, 1990.
[2] J. Bourgain and M. Z. Garaev. Sumsets of reciprocals in prime ﬁelds and multilinear Kloosterman sums.
Izv. Ross. Akad. Nauk Ser. Mat., 78(4):19–72, 2014.
[3] S. Chowla. Contributions to the analytic theory of numbers. Math. Z., 35(1):279–299, 1932.
[4] A. Granville and K. Soundararajan. The distribution of values of L(1, χd). Geom. Funct. Anal.,
13(5):992–1028, 2003.
[5] A. A. Karatsuba. New estimates for short Kloosterman sums. Mat. Zametki, 88(3):384–398, 2010.
[6] M. A. Korol¨ev. On Karatsuba’s method of estimating Kloosterman sums. Mat. Sb., 207(8):117–134,
2016.
[7] R. J. Lemke Oliver and K. Soundararajan. Unexpected biases in the distribution of consecutive primes.
Proc. Natl. Acad. Sci. USA, 113(31):E4446–E4454, 2016.
[8] H. L. Montgomery. Fluctuations in the mean of Euler’s phi function. Proc. Indian Acad. Sci. Math.
Sci., 97(1-3):239–245 (1988), 1987.
[9] H. L. Montgomery. Ten lectures on the interface between analytic number theory and harmonic analysis,
volume 84 of CBMS Regional Conference Series in Mathematics. Published for the Conference Board of
the Mathematical Sciences, Washington, DC; by the American Mathematical Society, Providence, RI,
1994.
[10] S. S. Pillai and S. D. Chowla. On the Error Terms in some Asymptotic Formulae in the Theory of
Numbers (1). J. London Math. Soc., S1-5(2):95.
[11] I. Vardi. Dedekind sums have a limiting distribution. Internat. Math. Res. Notices, (1):1–12, 1993.
[12] A. Walﬁsz. Weylsche Exponentialsummen in der neueren Zahlentheorie. Mathematische Forschungs-
berichte, XV. VEB Deutscher Verlag der Wissenschaften, Berlin, 1963.
[13] L. C. Washington. Introduction to cyclotomic ﬁelds, volume 83 of Graduate Texts in Mathematics.
Springer-Verlag, New York, second edition, 1997.

Department of Mathematics, Tufts University
E-mail address: robert.lemke oliver@tufts.edu

Department of Mathematics, Stanford University
E-mail address: ksound@stanford.edu
