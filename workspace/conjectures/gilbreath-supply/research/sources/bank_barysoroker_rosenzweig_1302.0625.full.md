<!-- source: https://arxiv.org/pdf/1302.0625 | converted from PDF -->

arXiv:1302.0625v3  [math.NT]  22 May 2014
Prime polynomials in short intervals
and in arithmetic progressions

Efrat Bank ∗ Lior Bary-Soroker † Lior Rosenzweig ‡

May 23, 2014

In this paper we establish function ﬁeld versions of two classical conjectures
on prime numbers. The ﬁrst says that the number of primes in intervals
(x, x + x
ǫ] is about x
ǫ/ log x. The second says that the number of primes
p < x in the arithmetic progression p ≡ a (mod d), for d < x
1−δ, is about
π(x)
φ(d) , where φ is the Euler totient function.
More precisely, for short intervals we prove: Let k be a ﬁxed integer. Then

πq(I(f, ǫ)) ∼ #I(f, ǫ)
k , q → ∞

holds uniformly for all prime powers q, degree k monic polynomials f ∈ Fq[t]
and ǫ0(f, q) ≤ ǫ, where ǫ0 is either 1
k , or 2
k if p | k(k − 1), or 3
k if further
p = 2 and deg f ′ ≤ 1. Here I(f, ǫ) = {g ∈ Fq[t] | deg(f − g) ≤ ǫ deg f },
and πq(I(f, ǫ)) denotes the number of prime polynomials in I(f, ǫ). We show
that this estimation fails in the neglected cases.
For arithmetic progressions we prove: Let k be a ﬁxed integer. Then

πq(k; D, f ) ∼ πq(k)
φ(D) , q → ∞,

holds uniformly for all relatively prime polynomials D, f ∈ Fq[t] satisfying
∥D∥ ≤ qk(1−δ0), where δ0 is either 3
k or 4
k if p = 2 and (f /D)′ is a constant.
Here πq(k) is the number of degree k prime polynomials and πq(k; D, f ) is the
number of such polynomials in the arithmetic progression P ≡ f (mod D).
We also generalize these results to arbitrary factorization types.

∗School of Mathematical Sciences, Tel Aviv University, Ramat Aviv, Tel Aviv 69978, Israel,
efratban@post.tau.ac.il
†School of Mathematical Sciences, Tel Aviv University, Ramat Aviv, Tel Aviv 69978, Israel,
barylior@post.tau.ac.il
‡Department of Mathematics, KTH, SE-10044, Stockholm, Sweden, lior.rosenzweig@gmail.com

1

1 Introduction

We study two function ﬁeld analogues of two classical problems in number theory con-
cerning the number of primes in short intervals and in arithmetic progressions. We ﬁrst
introduce the classical problems. In the next sections we formulate the corresponding
function ﬁeld conjectures and the resolution of them in the limit q → ∞.

1.1 Primes in short intervals

Let π(x) = #{0 < p ≤ x | p is a prime} be the prime counting function. By the Prime
Number Theorem (PNT) π(x) ∼ x
log x , x → ∞.

Therefore, one may expect that an interval I = (x, x + Φ(x)] of size Φ(x) starting at a
large x contains about Φ(x)/ log x primes, i.e.

π(I) := π(x + Φ(x)) − π(x) ∼ Φ(x)
log x . (1)

From PNT (1) holds for Φ(x) ∼ cx, for any ﬁxed 0 < c < 1. By Riemann Hypothesis
(1) holds for Φ(x) ∼ √x log x or even Φ(x) ∼ ǫ
√x log x assuming a strong form of
Montgomery’s pair correlation conjecture [8]. Concerning smaller powers of x Granville
conjectures [5, p. 7]

Conjecture 1.1. If Φ(x) > x
ǫ then (1) holds.

But even for Φ(x) = √x Granville says [6, p. 73]:

we know of no approach to prove that there are primes in all intervals [x, x +√x].

Heath-Brown [7], improving Huxley [9], proves Conjecture 1.1 unconditionally, for
x 7
12 −ǫ(x) ≤ Φ(x) ≤ x
log4 x , where ǫ(x) → 0.

We note that for extremely short intervals (e.g., for Φ(x) = log x log log x log log log log x
log log log x ) (1)
fails [13] uniformly, but may hold for almost all x, see [14] and the survey [6, Section 4].

1.2 Primes in arithmetic progressions

Let π(x; d, a) denote the number of primes p ≤ x such that p ≡ a (mod d). The Prime
Number Theorem for arithmetic progressions says that if a and d are relatively prime
and ﬁxed, then
 π(x; d, a) ∼ π(x)
φ(d) , x → ∞, (2)

where π(x) is the prime counting function and φ(d) is the Euler totient function, giving
the number of positive integers i up to d with gcd(i, d) = 1.

2

In many applications it is crucial to allow the modulus d to grow with x. The inter-
esting range is d < x since if d ≥ x, there can be at most one prime in the arithmetic
progression p ≡ i (mod d). A classical conjecture is the following (for a slightly diﬀerent
form see [12, Conjecture 13.9]).

Conjecture 1.2. For every δ > 0, (2) holds in the range d1+δ < x.

Concerning results on this conjecture Granville says [6, p. 69]:

. . . the best proven results have x bigger than the exponential of a power of
q (Granville’s q is our d) far larger than what we expect. If we are prepared
to assume the unproven Generalized Riemann Hypothesis we do much better,
being able to prove that the primes up to q2+δ are equally distributed amongst
the arithmetic progressions mod q, for q suﬃciently large, though notice
that this is still somewhat larger than what we expect to be true.

In this work we establish function ﬁeld analogues of Conjectures 1.1 and 1.2 for certain
intervals of parameters ǫ, δ which may be arbitrary small, and in particular breaking the
barriers ǫ = 1/2 in the former and δ = 1 in the latter. This indicates that Conjectures 1.1
and 1.2 should hold. A crucial ingredient is a type of Hilbert’s irreducibility theorem
over ﬁnite ﬁelds [2].

2 Function ﬁelds

Let P≤k be the space of polynomials of degree at most k over Fq and M(k, q) ⊆ P≤k
the subset of monic polynomials of degree k. If deg f = k, we let ∥f ∥ = qk.

2.1 Short intervals

Let πq(k) = #{g ∈ M(k, q) | g is a prime polynomial} be the prime polynomial counting
function. The Prime Polynomial Theorem (PPT) asserts that

πq(k) = qk

k + O(qk/2

k
 ).

We replace the interval [x, x + x
ǫ) around x with the interval I around f ∈ M(k, q)
given by I = I(f, ǫ) = {g ∈ Fq[t] | ∥f − g∥ ≤ ∥f ∥ǫ} = f + P≤m,

where m = ⌊ǫ deg(f )⌋. From this it is clear that it suﬃces to consider only ǫ = m
deg f ,
where m is a nonnegative integer. If ǫ ≥ 1, then I(f, ǫ) = P≤m, and so the PPT gives
the number of primes there. Therefore, the interesting range is ǫ < 1, in which case we
say that I is a short interval around f . In particular, M(k, q) = I(t
k, k−1
k ) is a short
interval. We note that all the polynomials in a short interval around a monic polynomial
are monic.
 3

For a short interval I let πq(I) = #{g ∈ I | g is a prime polynomial}. The naive
analogue of Conjecture 1.1 says that πq(I(f, ǫ)) ∼ #I(f, ǫ)/ deg f when qdeg(f ) is large.
However some anomalies can occur when both ǫ and deg f are small. For example if
ǫ < 1
deg f this naive approximation fails, see Section 6.2. Thus in the function ﬁeld
conjecture we add the assumption that ǫ is not too small when deg f is small:

Conjecture 2.1. There exists a function ǫ0(f, q) > 0 deﬁned on f ∈ Fq[t] such that
lim
deg f →∞ ǫ0(f, q) = 0 and such that for any ﬁxed ǫ the asymptotic formula

πq(I(f, ǫ)) ∼ #I(f, ǫ)
deg(f ) , qdeg(f ) → ∞,

holds uniformly for all q, f ∈ Fq[t] monic with ǫ0(f, q) ≤ ǫ < 1.

2.2 Primes in arithmetic progressions

For relatively prime f, D ∈ Fq[t] let

πq(k; D, f ) = #{h = f + Dg ∈ M(k, q) | h is a prime polynomial}.

The Prime Polynomial Theorem for arithmetic progressions says that

πq(k; D, f ) = πq(k)
φ(D) + O(qk/2

k deg D)
. (3)

Here φ(D) is the function ﬁeld Euler totient function, giving the number of units in
Fq[t]/DFq[t].
As in the classical case, we want to allow deg D to grow with k. The interesting range
of parameters is deg D < k because if deg D ≥ k, there is at most one monic prime in
the arithmetic progression h ≡ f mod D of degree k. As in the short interval case, we
must restrict the range δ when k is small.

Conjecture 2.2. There exists a function δ0(f, D, q, k) deﬁned over relatively prime
f, D ∈ Fq[t] such that lim
k→∞ δ0(f, D, q, k) = 0 and such that for any ﬁxed δ the asymptotic

formula
 πq(k; D, f ) ∼ πq(k)
φ(D) , qk → ∞,

holds uniformly for all q and relatively prime polynomials f, D ∈ Fq[t] satisfying deg D ≤
k(1 − δ0(f, D, q, k)).

(We replaced the range d1+δ < x as in Conjecture 1.2 with d < x
1−δ, for technical
reasons.)
We note that φ(D) ∼ qdeg D, q → ∞.

4

Therefore, if deg D < k
2 , then (3) gives that

πq(k; D, f ) ∼ πq(k)
φ(D) , q → ∞.

This range corresponds to δ > 1
2 in Conjecture 2.2. On the other hand (3) gives nothing
when δ ≤ 1
2.
Partial results towards Conjectures 2.1 and 2.2 in the limit q → ∞ can be deduced
from work of Cohen [3] when the characteristic of Fq is greater than deg F and from the
work of Keating and Rudnick [10] in an almost everywhere sense.
We prove these conjectures in the limit q → ∞ in general.

2.3 Results

We settle both Conjectures 2.1 and 2.2 in the limit q → ∞. In fact, our method allows
us to count polynomials with any given factorization type. Let us start by setting up
the notation.
The degrees of the primes in the factorization of a polynomial f ∈ Fq[t] to a product
of prime polynomials gives a partition of deg f , denoted by λf . Similarly, the lengths of
the cycles in the factorization of a permutation σ ∈ Sk to a product of disjoint cycles
gives a partition of k, denoted by λσ. For a partition λ of k we denote the probability
for σ ∈ Sk to have λσ = λ by
 P (λ) = #{σ ∈ Sk | λσ = λ}
k! . (4)

Let k be a positive integer and λ a partition of k. For a short interval I around
f ∈ M(k, q) we deﬁne the counting function

πq(I; λ) = #{g ∈ I | λg = λ}.

Theorem 2.3. Let k be a positive integer. Then there exists a constant c(k) > 0
depending only on k such that for any

• partition λ of k,

• prime power q = pν,

• short interval I = f + P≤m, where f ∈ M(k, q) and 3 ≤ m < k

we have ∣
∣πq(I; λ) − P (λ)qm+1∣
∣ ≤ c(k)qm+ 1
2 .

We may take m = 1 if p ∤ k(k − 1) and m = 2 if p ̸= 2 or if deg f ′ > 1.

5

For q = pν and f ∈ M(k, q), set

ǫ0(f, q) =
 



 3
k , if p = 2 and deg f ′ ≤ 1,

1
k , if p ∤ k(k − 1),

2
k , p | k(k − 1) .

Applying Theorem 2.3 with the partition λ consisting of one part, gives Conjecture 2.1
in the limit q → ∞.

Corollary 2.4. Let k > 0 be ﬁxed. The asymptotic formula

πq(I(f, ǫ)) ∼ #I(f, ǫ)
k , q → ∞

holds uniformly for all q, all f ∈ M(k, q), and all ǫ ∈ [ǫ0(f, q), 1).

In Section 6 we discuss the cases which are not included in Corollary 2.4. This is done
by studying the intervals I(t
k, ǫ) and showing that the Corollary 2.4 fails for ǫ < ǫ0 in
the cases where p ̸= 2 or deg f ′ > 1. We do not know whether the corollary holds true
in the remaining case.
Next we discuss polynomials with given factorization type in arithmetic progressions:
For relatively prime f, D ∈ Fq[t] with D monic we deﬁne the counting function

πq(k; D, f ; λ) = #{g ≡ f (mod D) | deg g = k and λg = λ}.

We prove the following theorem for polynomials in arithmetic progressions.

Theorem 2.5. Let k be a positive integer. Then there exists a constant c(k) > 0
depending only on k such that for any

• partition λ of k,

• prime power q = pν,

• D ∈ Fq[t] monic, such that deg D ≤ k − 4,

• f ∈ Fq[t] relatively prime to D,

we have ∣
∣
∣
∣πq(k; D, f ; λ) − πq(k; λ)
φ(D)
 ∣
∣
∣
∣ ≤ c(k)

q 1
2 · πq(k; λ)
φ(D) .

Except when p = 2 and (f /D)′ is constant, we may take deg D ≤ k − 3.

In particular, when we consider the special case of λ being the partition into one part,
we get Conjecture 2.2 in the limit q → ∞:

Corollary 2.6. Let k be a ﬁxed integer. Then

πq(k; D, f ) ∼ πq(k)
φ(D) , q → ∞,

holds uniformly for all relatively prime D, f ∈ Fq[t] satisfying ∥D∥ ≤ qk(1−δ0), where
δ0 = 4
k if (f /D)′ is constant and p = 2 and δ0 = 3
k otherwise.

6

3 Auxiliary results

3.1 Specializations

We brieﬂy recall some deﬁnitions and basic facts on specializations, see [2, Section 2.1]
for more details and proofs. Let

K be a ﬁeld with algebraic closure ˜K,
Gal(K) = Aut( ˜K/K) the absolute Galois group of K,
W = Spec S and V = Spec R absolutely irreducible smooth aﬃne K-varieties,
ρ : W → V a ﬁnite separable morphism which is generically Galois,
F/E the function ﬁeld Galois extension that corresponds to ρ,
K-rational point p ∈ V (K) that is ´etale in W , and
P ∈ ρ
−1(p).

Then p induces a homomorphism φp : R → K that extends to a homomorphism φP : S →
˜K (via the inclusion R → S induced by ρ). Since p is ´etale in W , we have a homomor-
phism P∗ : Gal(K) → Gal(F/E) such that

φP(P∗(σ)(x)) = σ(φP(x)), ∀x ∈ S, ∀σ ∈ Gal(K). (5)

For every other Q ∈ ρ
−1(p) there is τ ∈ Gal(F/E) such that φQ = φP ◦ τ . Thus, by
(5), Q
∗ = τ −1P∗τ and vice-versa every τ −1P∗τ comes from a point Q ∈ ρ
−1(p) . Hence
p∗ = {Q
∗ | Q ∈ ρ
−1(p)} is the orbit of P∗ under the conjugation action of Gal(F/E).
The key ingredients in the proof of the following proposition are the Lang-Weil esti-
mates [11, Theorem 1] and the ﬁeld crossing argument (as utilized in [2, Proposition 2.2]).

Proposition 3.1. Let k, m, and B be positive integers, let λ be a partition of k, let
F be an algebraic closure of Fq, and let F ∈ Fq[A0, . . . , Am, t] be a polynomial that is
separable in t with deg F ≤ B and degt F = k. Assume that

Gal(F , F(A0, . . . , Am)) = Sk.

Denote by N = N(F , q) the number of (a0, . . . , am) ∈ Fm+1
q such that f = F (a0, . . . , am, t)
has factorization type λf = λ. Then there is a constant c(m, B) that depends only on m
and B such that ∣
∣N − P (λ)qm+1∣
∣ ≤ c(m, B)qm+1/2,

where P (λ) is deﬁned in (4).

Proof. Let A = (A0, . . . , Am) and F the splitting ﬁeld of F over Fq(A). Since

Sk = Gal(F , F(A)) = Gal(F · F/F(A)) ≤ Gal(F/Fq(A)) ≤ Sk,

all inequalities are in fact equalities and Fq = F ∩ F. In particular, α : Gal(F/Fq(A)) →
Gal(F ∩ F/Fq) = 1, so ker α = Sk. (6)

7

Since Gal(Fq) = ⟨ϕ⟩ ∼= ˆZ (with ϕ being the Frobenius map x ↦→ x
q) the homomor-
phisms θ : Gal(Fq) → Sk can be parametrized by permutations σ ∈ Sk. Explicitly, each
σ ∈ Sk gives rise to θσ : Gal(Fq) → Sk deﬁned by θσ(ϕ) = σ. Let C be the conjugacy
class of all permutations σ with λσ = λ and let Θ = {θσ | σ ∈ C}. Fix θ ∈ Θ. Clearly
#Θ = #C, so by (6) we have
 # ker α
#Θ = #Sk
#C = 1
P (λ). (7)

Let Z be the closed subset of Am+1 = Spec Fq[A] deﬁned by D = disct(F ) = 0 and
V = Am+1 ∖ Z = Spec Fq[A, D−1]. By assumption F is separable in t, so D is a nonzero
polynomial of degree depending only on B. By [11, Lemma 1], there exists a constant
c1 = c1(m, B) such that #Z(K) ≤ c1qm. (8)

Let u1, . . . , uk be the roots of F in some algebraic closure of F(A0, . . . , Am) and let
W = Spec Fq[u1, . . . , uk, D−1] ⊆ Ak+1. Then W is an absolutely irreducible smooth
aﬃne Fq-variety of degree bounded in terms of B = deg F . The embedding Fq[A, D−1] →
Fq[u1, . . . , uk, D−1] induces a ﬁnite separable ´etale morphism ρ : W → V .
We apply [2, Proposition 2.2] to get an absolutely irreducible smooth Fq-variety ̂W
together with a ﬁnite separable ´etale morphism π : ̂W → V with the following properties:

i. Let U ⊆ V (Fq) be the set of p ∈ V (Fq) that are ´etale in W and such that p∗ = Θ.
Then π(̂W (Fq)) = U.

ii. For every p ∈ U,
 #(π−1(p) ∩ ̂W (Fq)) = # ker α
#Θ = 1
P (λ).

(See (7) for the last equality.)

By the construction of ̂W in loc. cit. it holds that ̂WL = WL, for some ﬁnite extension
L/Fq (where subscript L indicates the extension of scalars to L). Hence ̂W and W have
the same degree, which is bounded in terms of B. Thus, by [11, Theorem 1], there is a
constant c2 = c2(m, B) such that

|#̂W (Fq) − qm+1| ≤ c2qm+1/2. (9)

Applying (ii) gives P (λ) · #π(̂W (Fq)) = #̂W (Fq). So multiplying (9) by P (λ) implies

|#π(̂W (Fq)) − P (λ)qm+1| ≤ P (λ)c2qm+1/2 ≤ c2qm+1/2. (10)

Since for p = (a0, . . . , am) ∈ V (Fq) ⊆ Fm+1
q we have p∗ = Θ if and only if the orbit
type of p∗ is λ (in the sense of [2, p. 859]). Thus λF (a0,...,am,t) = λ if and only p∗ = Θ ([2,
Lemma 2.1]). Let

X = {p = (a0, . . . , am) ∈ Fm+1
q | λF (a0,...,am,t) = λ and D(a0, . . . , am) ̸= 0}.

8

Then N = #X. Equation (i) gives X ∩ V (Fq) = π(̂W (Fq)). Since V = Am+1 ∖ Z, it
follows from (8) and (10) that
∣
∣N − P (λ)qm+1∣
∣ = ∣
∣#X − P (λ)qm+1∣
∣

= ∣
∣#(X ∩ V (Fq)) + #(X ∩ Z(Fq)) − P (λ)qm+1∣
∣

≤ ∣
∣#(X ∩ V (Fq)) − P (λ)qm+1∣
∣ + #(X ∩ Z(Fq))

≤ ∣
∣
∣π(̂W (Fq)) − P (λ)qm+1∣
∣
∣ + #Z(Fq)

≤ c2qm+1/2 + c1qm ≤ c(m, B)qm+1/2,

where c = c1 + c2.

3.2 Calculating a Galois Group

Lemma 3.2. Let F be an algebraically closed ﬁeld, A = (A0, . . . , Am) an m-tuple of
variables with m ≥ 1, and f, g ∈ F [t] relatively prime polynomials. Then F (A, t) =
f (t) + g(t) · (∑m
i=0 Ait
i) is separable in t and irreducible in the ring F (A)[t].

Proof. Since F is linear in A0 and since f, g are relatively prime, it follows that F is
irreducible in F [A, t], hence by Gauss’ lemma also in F (A)[t]. Take α ∈ F with g(α) ̸= 0.
Then
 F ′(α) = f ′(α) + g′(α)(
 m∑

i=0 Aiαi) + g(α)A1 + (
 m∑

i=2 iAiαi−1) ̸= 0,

hence F ′ ̸= 0, so F is separable.

Lemma 3.3. Let F be an algebraically closed ﬁeld, A = (A0, . . . , Am) an m-tuple of
variables with m ≥ 2, and f, g ∈ F [t] relatively prime polynomials with deg f > deg g.
The Galois group G of F (A, t) = f (t) + g(t) · (∑m
i=0 Ait
i) over F (A) is doubly transitive
(with respect to the action on the roots of F ).

Proof. By replacing t by t+α, where α ∈ F is a root of f , we may assume that f (0) = 0.
Hence f0(t) = f (t)/t is a polynomial. By Lemma 3.2 the group G is transitive. The
image of F under the substitution A0 = 0 is

¯F = f (t) + g(t) · ( m∑

i=0 Ait
i) = t
(f0(t) + g(t) · ( m−1∑

i=1 Ait
i−1))
.

Lemma 3.2 then gives that f0(t)+g(t)·( ∑m−1
i=1 Ait
i−1) is separable and irreducible. This
means that the stabilizer of the root t = 0 in the Galois group of ¯F acts transitively
on the other roots. But since ¯F is separable, its Galois group embeds into G, so the
stabilizer of a root of F in G is transitive. Thus G is doubly transitive.

For a rational function ψ(t) ∈ F (t) the ﬁrst and second Hasse-Schmidt derivatives of
ψ are denoted by ψ′ and ψ[2], respectively, and deﬁned by

ψ(t + u) ≡ ψ(t) + ψ′(t)u + ψ[2](t)u2 mod u3.

9

A trivial observation is that ψ′ is the usual derivative of ψ and, if the characteristic of
F ̸= 2, then ψ[2] = 1
2 ψ′′.

Lemma 3.4. Let ψ(t) ∈ F (t) be a rational function with ψ[2] nonzero and A1 a variable.
Then ψ′(t) + A1 and ψ[2](t) have no common zeros.

Proof. This is obvious since the roots of ψ′ + A1 are transcendental over F , while those
of ψ[2] are algebraic.

Lemma 3.5. Let F be an algebraically closed ﬁeld of characteristic p ≥ 0, m ≥ 2,
A = (A1, . . . , Am), f, g ∈ F [t] relatively prime polynomials and put ψ = f /g and Ψ =
ψ + ∑m
i=1 Ait
i. Assume deg f > deg g + m. Further assume that ψ′ is not a constant if
p = m = 2. Then the system of equations

Ψ′(ρ1) = 0
Ψ′(ρ2) = 0
Ψ(ρ1) = Ψ(ρ2) (11)

has no solution with distinct ρ1, ρ2 in an algebraic closure Ω of F (A).

Proof. For short we write ρ = (ρ1, ρ2). Let

−ϕ(t) = (
ψ +
 m∑

i=3 Ait
i)′ = ψ′ +
 m∑

i=3 iAit
i−1 = f ′g − f g′

g2 +
 m∑

i=3 iAit
i−1.

Then Ψ′(t) = 2A2t + A1 − ϕ(t). If m = 2, then ϕ = −ψ′, the latter being nonconstant
if also p = 2, by assumption.
Let
 c(ρ) = ψ(ρ1) − ψ(ρ2) +
 m∑

i=3 (ρ
i
1 − ρ
i
2)Ai

= Ψ(ρ1) − Ψ(ρ2) − ((ρ
2
1 − ρ
2
2)A2 + (ρ1 − ρ2)A1).

The system of equations (11) deﬁnes an algebraic set T ⊆ A2 × Am in the variables
ρ1, ρ2, A1, . . . , Am. Let α : T → A2 and β : T → Am the projection maps. The system of
equations (11) takes the matrix form

M(ρ) · ( A2
A1 ) = B(ρ) = ( ϕ(ρ1)
ϕ(ρ2)
c(ρ)
 )
, (12)

where M(ρ) = ( 2ρ1 1
2ρ2 1
ρ2
2−ρ2
1 ρ2−ρ1
 )
. For every ρ ∈ U = {ρ | ρ1 ̸= ρ2, ϕ(ρi) ̸= ∞, i = 1, 2},

the rank of M(ρ) is 2. Thus the dimension of the ﬁber α−1(ρ), for any ρ ∈ U, is at most
m − 2. Moreover, for a given ρ ∈ U, (12) is solvable if and only if rank(M|B) = 2 if
and only if d(ρ) = det(M|B) = 0. Thus, the solution space (restricting to ρ ∈ U) lies in
d(ρ) = 0.
 10

It suﬃces to prove that d(ρ) is a nonzero rational function in the variables ρ = (ρ1, ρ2).
Indeed, this implies that dim(α(T )) ≤ dim{d(ρ) = 0} = 1, so dim T ≤ 1 + m − 2 < m.
Thus β(T ) does not contain the generic point of Am which is A = (A0, . . . , Am) and
hence (11) has no solution with ρ ∈ Ω
2.
A straightforward calculation gives

d(ρ) = (ρ1 − ρ2)(2c(ρ) + (ρ1 − ρ2)(ϕ(ρ1) + ϕ(ρ2))).

If m ≥ 3, then the coeﬃcient of A3 in 2c(ρ) + (ρ1 − ρ2)(ϕ(ρ1) + ϕ(ρ2)) is

2(ρ
3
1 − ρ
3
2) + 3(ρ
2
1 − ρ
2
2),

which is nonzero in any characteristic and we are done.
To this end assume m = 2. If p = 2, then 2c(ρ) = 0. Since ϕ is not constant in this
case, we have ϕ(ρ1) + ϕ(ρ2) ̸= 0 and we are done.
Finally assume m = 2 and p ̸= 2. Then c(ρ) = ψ(ρ1) − ψ(ρ2) and ϕ = −ψ′. We
may assume without loss of generality that f (0) = 0 (and hence ψ(0) = 0). Since
f (t)/t + g(t)(A2t + A1) is separable (Lemma 3.2), we can replace A1 and A2 by A1 + α1
and A2 +α2, respectively, and f by f (t)+g(t)(α2t
2 +α1t), for suitably chosen α1, α2 ∈ F ,
to assume that f (t)/t is separable. Since deg f > deg g + m ≥ 2, this implies that f (t)
has at least one simple root, say α. Then α is a simple root of ψ = f /g. So ψ′(α) ̸= 0.
Let β ̸= α be another root of f , hence of ψ.
If ψ′(β) = 0, then we have c(α, β) = ψ(α) − ψ(β) = 0, so

d(α, β) = −(α − β)2ψ′(α) ̸= 0

and we are done. If ψ′(β) ̸= 0, then β is a simple root of ψ, hence of f . But deg f > 2,
so there must be another root γ of ψ. If d = 0, then we must have

d(α, β)
−(α − β)2 = 0 = ψ′(α) + ψ′(β)

d(α, γ)
−(α − γ)2 = 0 = ψ′(α) + ψ′(γ)

d(γ, β)
−(γ − β)2 = 0 = ψ′(γ) + ψ′(β).

So 2ψ′(α) = 0. This contradiction implies that d ̸= 0, as needed.

Proposition 3.6. Let F be a ﬁeld of characteristic p ≥ 0, let 1 ≤ m < k, let
A = (A0, . . . , Am) an (m + 1)-tuple of variables, and let f, g ∈ F [t] be relatively prime
polynomials with deg g + m < k = deg f . Assume

1. 2 ≤ m if deg g > 0,

2. 2 ≤ m if p | k(k − 1), and

3. (f /g)′ is not constant if p = m = 2.
 11

Then the Galois group of F (A, t) = f (t) + g(t) · (∑m
i=0 Ait
i) over F (A) is

Gal (F , F (A)) = Sk.

Proof. Let ˜F be an algebraic closure of F . Since Gal(F , ˜F (A)) ≤ Gal(F , F (A)) ≤ Sk,
we may replace, without loss of generality, F by ˜F to assume that F is algebraically
closed.
If p ∤ k(k − 1) and deg g = 0, the result follows from [4, Theorem 1] (note that
F (A0, . . . , Am) = F (A2, . . . , Am−1)(A0, A1), hence the result for m = 1 in loc. cit. ex-
tends to m > 1).
Assume that 2 ≤ m. Then G = Gal(F , F (A)) ≤ Sk is doubly transitive by Lemma 3.3.
Let Ω be an algebraic closure of F (A1, . . . , Am) and consider the map Ψ : P1
Ω → P1
Ω
deﬁned locally by t ↦→ −A0 := f (t)
g(t) + ∑m
i=1 Ait
i. The numerator of Ψ′ = f ′g−g′f
g2 +
∑m
i=1 iAit
i is f ′g − g′f + g2 · (· · · + 2A2t + A1).

If m ≥ 3 or if p ̸= 2, this numerator has positive degree. If p = m = 2, then this
numerator is f ′g − g′f + g2A1, so it is not constant by (3). In any case, the numerator of
Ψ′, hence Ψ′, has a root, say α ∈ Ω. Then Ψ is ramiﬁed at t = α. Lemma 3.4 says that
the orders of ramiﬁcations are ≤ 2, so the equation Ψ(t) = Ψ(α) has at most double
roots in Ω. Lemma 3.5 says that the critical values are distinct, so Ψ(t) = Ψ(α) has at
least k − 1 solutions. But since α is a ramiﬁcation point, the ﬁber over Ψ(α) is with
exactly one double points. Hence the inertia group over Ψ(α) permutes two roots of

F (A, t) = g(t)(Ψ(t) + A0),

and ﬁxes the other roots (cf. [1, Proposition 2.6]). In other words G contains a transpo-
sition. Therefore, G = Sk [15, Lemma 4.4.3].

4 Proof of Theorem 2.3

Let k be a positive integer, λ a partition of k, q = pν a prime power, f ∈ M(k, q),
3 ≤ m < k (or 1 ≤ m < k if p ∤ k(k − 1) or 2 ≤ m < k if p ̸= 2 or deg f ′ > 1), and
I = f + P≤m.
Let F be an algebraic closure of Fq.
Let F (A0, · · · , Am, t) = f (t) + ∑m
i=0 Ait
i. Then F satisﬁes the assumptions of Propo-
sition 3.6, so Gal(F , F(A0, . . . , Am)) = Sk.
Since deg F = degt F = deg f = k and m < k, by Proposition 3.1, the number N of
(a0, . . . , am) ∈ Fm+1
q such that f (t) + ∑m
i=0 ait
i has factorization type λ satisﬁes

∣
∣N − P (λ)qm+1∣
∣ ≤ c(k)qm+1/2,

where c(k) > 0 is a constant depending only on k (and not on f , q). This ﬁnishes the
proof since by deﬁnition N = πq(I; λ).
 12

5 Proof of Theorem 2.5

Let k be a positive integer, λ a partition of k, q = pν a prime power, D ∈ Fq[t] monic
of deg D with deg D ≤ k − 3 (or deg D ≤ k − 4 if p = 2 and (f /D)′ is constant), and
f ∈ Fq[t]. Since we are interested in the number of prime polynomials in the arithmetic
progression g ≡ f mod D, we may replace f by f − QD, for some polynomial Q to
assume that deg f < deg D. Let m = deg D and F be an algebraic closure of Fq.
Let

F (A, t) = f (t) + D(t) · (
t
m+1 +
 m∑

i=0 Ait
i) = ˜f (t) + D(t) · ( m∑

i=0 Ait
i), ˜f = f + D · t
m+1,

where A = (A0, . . . , Am) is an (m + 1)-tuple of variables. Since deg ˜f = m + 1 + deg D =
k > deg D + m, Proposition 3.6 gives that

Gal(F , F(A)) = Sk,

Since deg F = degt F = k, Proposition 3.1 implies that the number N of (a0, . . . , am) ∈
Fm+1
q such that f (t) + D(t) · (t
m+1 + ∑m
i=0 ait
i) has factorization type λ satisﬁes
∣
∣N − P (λ)qm+1∣
∣ ≤ c1(k)qm+1/2,

where c(k) > 0 is a constant depending only on k (and not on f , q).
Finally, φ(D) = ∥D∥ ∏

P |f (1 − 1/∥P ∥), where the products runs over the distinct
prime polynomials P dividing D. Since ∥P ∥ ≥ q we have

φ(D) = qdeg D (1 + O (1
q
 )) = qk−m−1 + Ok(qk−m−2).

By applying Theorem 2.3 to the interval I(t
k, k − 1), it follows that

πq(k; λ) = P (λ)qk + Ok(qm+1/2).

Thus ∣
∣
∣
∣πq(k; λ)
φ(D) − P (λ)qm+1∣
∣
∣
∣ ≤ c2(k)qm+1/2

and ∣
∣
∣
∣N − πq(k; λ)
φ(D)
 ∣
∣
∣
∣ ≤ ∣
∣
∣
∣N − P (λ)qm+1∣
∣
∣
∣ + ∣
∣
∣
∣ πq(k; λ)
φ(D) − P (λ)qm+1∣
∣
∣
∣ ≤ c(k)qm+1/2,

where c = c1 + c2. This ﬁnishes the proof since by deﬁnition N = πq(k; D, f ; λ).

6 Small ǫ

In this section we study the cases ǫ < ǫ0 in Corollary 2.3, except for the case p = m = 2,
and deg f ′ ≤ 1 and show that the implication fails to hold in these cases. In the latter
case we do not know whether the result holds or not. For the rest of the section let
m = ǫk.
 13

6.1 ǫ < 1
k
We denote Euler’s totient function by φ(k) = |(Z/kZ)∗|.

Proposition 6.1. For k > 1 and 0 < ǫ < 1
k we have

πq(I(t
k, ǫ)) = πq(I(t
k, 0)) =
 {
0, q ̸≡ 1 mod k
φ(k)
k (q − 1), q ≡ 1 mod k.

In particular, if k > 2, |πq(I(t
k, 0)) − q/k| ≫ q.

Proof. We separate the proof into cases.

Case I. gcd(q, k) > 1.
In this case t
k − a is inseparable for any a ∈ Fp. Since Fq is perfect, this implies that
t
k − a is reducible. So πq(I(t
k, 0)) = 0.

Case II. gcd(q(q − 1), k) = 1.
In this case k ̸= 2 and 1 − q is invertible modulo k. Assume, by contradiction, that
there exists a ∈ Fq such that f = t
k − a is irreducible in Fp[t]. Then the Frobenius map,
ϕ : x ↦→ x
q, acts transitively on the roots of f . Thus αq = ζα, where ζ is a primitive
k-th root of unity. We get that the orbit of α under ϕ is

α ↦→ αq = ζα ↦→ (ζα)q = ζ 1+qα ↦→ · · · ↦→ ζ 1+q+···+qk−1α = α.

On the other hand, this orbit equals to the set of roots of f which is {ζ iα | i = 0, . . . , k −
1}. So for every i mod k there is a unique 1 ≤ r ≤ k such that

i ≡ 1 + q + · · · + qr−1 ≡ (1 − q)−1(1 − qr) (mod k).

This is a contradiction since there are at most φ(k) < k powers of q mod k, hence
#{(1 − q)−1(1 − qr) mod k} < k = #{i mod k}.

Case III. gcd(q, k) = 1 and q ̸≡ 1 mod k.
Let g = gcd(q − 1, k); then l = k/g > 1 and gcd(q(q − 1), l) = 1. Let a ∈ Fq, and let
α be a root of f = t
k − a. Then the polynomial f1 = t
l − αl ∈ Fq[αl][t] is reducible by
Case II. Since α is a root of g and since αl is a root of f2 = t
g − a, we get that

[Fq[α] : Fq] = [Fq[α] : Fq[αl]] · [Fq[αl] : Fq] < l · g = k.

In particular, f is reducible.

Case IV. q ≡ 1 mod k.
In this case Fq contains a primitive k-th root of unity. By Kummer theory t
k − a is
irreducible in Fq if and only if the order of a(F∗
q)k in C = F∗
q/(F∗
q)k is k. Since F∗
q is cyclic
of order q − 1, the subgroup C is also cyclic of order k. Hence, there are exactly φ(k)
cosets of order k in C. Each coset contains q−1
k elements. So there are exactly φ(k)
k (q − 1)
prime polynomials t
k − a.
 14

6.2 1
k ≤ ǫ < 2
k and p | k

In this case we study the interval I(t
p2, ǫ) = I(t
p2, 1
k ) = {t
p2 − at + b | a, b ∈ Fq} for
q = p2n.

Proposition 6.2. For q = p2n, k = p2, and 1
k ≤ ǫ < 2
k we have

πq(I(t
p2, ǫ)) = 0.

In particular, |πq(I(t
p, ǫ)) − q2/p| ≫ q.

Proof. Let F = Fp2, let E be the splitting ﬁeld of F = t
p2 − At + B over K = Fq(A, B).
Then, by [16, Theorem 2],

G = Gal(F , F ) ∼= Gal(E/F ) ∼= Gal(E · F, F(A, B)) ∼= Aﬀ(F ),

as permutation groups. Here F is an algebraic closure of Fq and Aﬀ(F ) is the group of
transformation of the aﬃne line A1(F ) = F :

Mc,d : x ↦→ cx + d, 0 ̸= c, d ∈ F.

Since |G| = p2(p2 − 1) and since the group of translation T = {x ↦→ x + d} ∼= Fp2 is of
order p2, we get that T is a p-sylow subgroup of T . But T is of exponent p, hence there
are no p2-cycles in G.
For every a, b ∈ Fq, the Galois group Ga,b of f = t
p2 − at + b is a cyclic sub-quotient
of G, hence of order < p2. In particular Ga,b acts intransitively on the roots of f , hence
f is reducible.

6.3 1
k ≤ ǫ < 2
k and p | k − 1

The details of this case are nearly identical to Section 6.2 with the distinction that the
group Aﬀ(F ) is replaced by the group of transformations on the projective line, cf. [16,
Theorem 2]. Hence we state the result but omit the details.

Proposition 6.3. For q = p2n, f = t
p2+1, k = p2 + 1, and 1
k ≤ ǫ < 2
k we have

πq(I(t
p2+1, ǫ) = 0.

Acknowledgments

We thank Zeev Rudnick for helpful remarks on earlier drafts of this paper and for the
suggestions to consider arithmetic progressions and diﬀerent factorization types. We
thank the referees for their many helpful comments.
The ﬁrst two authors were supported by a Grant from the GIF, the German-Israeli
Foundation for Scientiﬁc Research and Development. The last author was supported by
the G¨oran Gustafsson Foundation (KVA).
 15

References

[1] L. Bary-Soroker. Dirichlet’s theorem for polynomial rings. Proc. Amer. Math. Soc.,
137(1):73–83, 2009.

[2] L. Bary-Soroker. Irreducible values of polynomials. Adv. Math., 229(2): 854–874,
2012.

[3] S. D. Cohen. Uniform distribution of polynomials over ﬁnite ﬁelds. J. London Math.
Soc., 6(2):93–102, 1972.

[4] S. D. Cohen. The Galois group of a polynomial with two indeterminate coeﬃcients.
Paciﬁc J. Math., 90(1):63–76, 1980.

[5] A. Granville. Unexpected irregularities in the distribution of prime numbers. Pro-
ceedings of the International Congress of Mathematicians, Vol. 1, 2 (Z¨urich, 1994),
388–399, Birkh¨auser, Basel, 1995.

[6] A. Granville. Diﬀerent approaches to the distribution of primes. Milan J. Math.,
78(1):65–84, 2010.

[7] D. R. Heath-Brown. The number of primes in a short interval. J. Reine Angew.
Math., 389:22–63, 1988.

[8] D. R. Heath-Brown and D. A. Goldston. A note on the diﬀerences between consec-
utive primes. Math. Ann., 266(3):317–320.

[9] M. N. Huxley. On the diﬀerence between consecutive primes. Invent. Math., 15:164–
170, 1972.

[10] J. P. Keating and Z. Rudnick. The variance of the number of prime polynomials
in short intervals and in residue classes. Int. Math. Res. Not. IMRN, page 30 pp.,
April 2012.

[11] S. Lang and A. Weil. Number of points of varieties in ﬁnite ﬁelds. Amer. J. Math.,
76:819–827, 1954.

[12] H. L. Montgomery and R. C. Vaughan. Multiplicative Number Theory I. Classical
Theory. Cambridge Studies in Advanced Mathematics, 97. Cambridge University
Press, Cambridge, 2007. xviii+552 pp..

[13] R. A. Rankin. The Diﬀerence between Consecutive Prime Numbers. J. London
Math. Soc., 13:242–247, 1938.

[14] A. Selberg. On the normal density of primes in small intervals, and the diﬀerence
between consecutive primes. Arch. Math. Naturvid., 47(6):87–105, 1943.

[15] J.-P. Serre. Topics in Galois Theory (Research Notes in Mathematics) [Hardcover].
A. K. Peters, Ltd., 2 edition, 2008.
 16

[16] K. Uchida. Galois group of an equation X n − aX + b = 0. Tohoku Math. J. (2),
22(4):670–678, 1970.
 17
