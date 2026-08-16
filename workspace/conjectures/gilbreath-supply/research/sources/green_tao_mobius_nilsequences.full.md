<!-- source: https://arxiv.org/pdf/0807.1736 | converted from PDF -->

arXiv:0807.1736v4  [math.NT]  29 May 2011
THE M ¨OBIUS FUNCTION IS STRONGLY ORTHOGONAL TO
NILSEQUENCES

BEN GREEN AND TERENCE TAO

Abstract. We show that the M¨obius function µ(n) is strongly asymptotically or-
thogonal to any polynomial nilsequence (F (g(n)Γ))n∈N. Here, G is a simply-connected
nilpotent Lie group with a discrete and cocompact subgroup Γ (so G/Γ is a nilmani-
fold ), g : Z → G is a polynomial sequence and F : G/Γ → R is a Lipschitz function.
More precisely, we show that | 1
N ∑N
n=1 µ(n)F (g(n)Γ)| ≪F,G,Γ,A log−A N for all A > 0.
In particular, this implies the M¨obius and Nilsequence conjecture MN(s) from our ear-
lier paper [8] for every positive integer s. This is one of two major ingredients in
our programme in [8] to establish a large number of cases of the generalised Hardy-
Littlewood conjecture, which predicts how often a collection ψ1, . . . , ψt : Z
d → Z of
linear forms all take prime values. The proof is a relatively quick application of the
results in our recent companion paper [9].
We give some applications of our main theorem. We show, for example, that the
M¨obius function is uncorrelated with any bracket polynomial such as n√
3⌊n√
2⌋. We
also obtain a result about the distribution of nilsequences (anxΓ)n∈N as n ranges only
over the primes.
 1. Introduction

Important remark. This paper is intimately tied to, and is intended to be read
in conjunction with, the longer companion paper [9], which proves results about the
distribution of ﬁnite polynomial orbits on nilmanifolds. In particular, we shall make
heavy use of the notation and lemmas from that paper.

The aim of this paper is to establish what the authors have been referring to as the
M¨obius and Nilsequence conjecture MN(s), ﬁrst stated as [8, Conjecture 8.5]. Roughly
speaking, this states that the M¨obius function µ(n), deﬁned as (−1)k when n is the
product of k distinct primes, and 0 otherwise, is asymptotically strongly orthogonal to
any Lipschitz s-step nilsequence (F (a
nx))n∈Z, in the sense that the inner product

En∈[N ]µ(n)F (a
nx)

of these two functions on [N] := {1, . . . , N} decays to zero faster than any ﬁxed
power of 1/ log N. Here and in the sequel we use the averaging notation Ex∈X f (x) :=
1
|X| ∑

x∈X f (x) for any ﬁnite set X. Recall also that an Lipschitz s-step nilsequence is
any sequence of the form F (a
nx), where a is an element of an s-step connected and sim-
ply connected nilpotent Lie group G, x is an element of the nilmanifold G/Γ for some
discrete cocompact subgroup Γ ⩽ G of G, and F : G/Γ → R is a Lipschitz function.

The diﬃculty of this conjecture increases with s. The case s = 0 of this conjecture is
the estimate En∈[N ]µ(n) ≪A log−A N.
1

2 BEN GREEN AND TERENCE TAO

The stronger estimate En∈[N ]µ(n) ≪ e
−c√
log N

is essentially equivalent to the prime number theorem (with classical error term).

The case s = 1 may be reduced by Fourier analysis to the estimate

|En∈[N ]µ(n)e(αn)| ≪A log−A N (1.1)

where e(x) := e
2πix, required to hold uniformly for all α ∈ R. This was established
by Davenport [3] in the 1930s by modifying Vinogradov’s method of bilinear forms (or
“Type I and Type II sums”).

In the case s = 2 the conjecture was established by the authors in [7]. For a more
complete discussion of the conjecture and the reasons for being interested in it (and
in particular, its applications to the generalised Hardy-Littlewood conjecture on the
number of solutions to systems of linear equations in which the unknowns are all prime)
the reader may refer to the introduction of [7], the ﬁrst several sections of [8], or any of
the expository articles [4, 5, 15, 16].

In this paper we settle the M¨obius and Nilsequence conjecture. In fact, we shall
prove the marginally stronger result that the M¨obius function is asymptotically strongly
orthogonal to any polynomial nilsequence (F (g(n)Γ))n∈Z.

Theorem 1.1 (Main Theorem). Let G/Γ be a nilmanifold of some dimension m ⩾ 1,
let G• be a ﬁltration1 of G of some degree d ⩾ 1, and let g ∈ poly(Z, G•) be a polynomial
sequence2. Suppose that G/Γ has a Q-rational Mal’cev basis3 X for some Q ⩾ 2, deﬁning
a metric dX on G/Γ. Suppose that F : G/Γ → [−1, 1] is a Lipschitz function. Then we
have the bound

|En∈[N ]µ(n)F (g(n)Γ)| ≪m,d,A Q
Om,d,A(1)(1 + ∥F ∥Lip) log−A N

for any A > 0 and N ⩾ 2. The implied constant is ineﬀective.

Remarks. By specialising to the linear case g(n) := a
nh for some a, h ∈ G (and using
the existence of Q-rational Mal’cev bases, see [9, Proposition A.9]), Theorem 1.1 im-
mediately implies the M¨obius and nilsequences conjecture [8, Conjecture 8.5]. In fact it
gives a somewhat more precise result, since the dependence on Q and ∥F ∥Lip is given
quite explicitly. For the application of Theorem 1.1 in [8], however, knowledge of these
dependencies is not necessary.

The ineﬀectivity of the bound in Theorem 1.1 already occurs for suﬃciently large A in
the 1-step case (which, as mentioned before, is essentially (1.1)), and is ultimately due
to the well-known ineﬀective bounds on Siegel zeroes. On the other hand, the remainder
of the argument is eﬀective, and so any eﬀective bound for Siegel’s theorem would imply
eﬀective bounds for Theorem 1.1. In particular, this would be the case if one assumed
GRH. In fact, in that case it is not diﬃcult to see from modifying the arguments below

1In other words, G• = (Gi)
d
i=0 where G = G0 ⊂ G1 ⊂ . . . Gd is a descending sequence of Lie groups
and [Gi, Gj] ⊂ Gi+j for all i, j ⩾ 0, with the convention that Gi is trivial for i > d; see [9, Deﬁnition
1.2].
2A sequence g : Z → G lies in poly(Z, G•) if ∂h1 . . . ∂hig takes values in Gi for all h1, . . . , hi ∈ Z and
i ≥ 0, where ∂hg(n) := g(n + h)g(n)
−1; see [9, Deﬁnition 1.11] and the ensuing discussion.
3The notion of a Q-rational Mal’cev basis is deﬁned in [9, Deﬁnition 2.6] and the construction of
the metric dX is given in the same section.

THE M ¨OBIUS FUNCTION IS STRONGLY ORTHOGONAL TO NILSEQUENCES 3

that we can replace the logarithmic decay log−A N by polynomial decay N −c for some
c > 0 depending only on d and m.

The authors learnt in [9] that it is in many ways more natural to consider the class
of polynomial sequences poly(Z, G•) rather than simply the class of linear sequences
n ↦→ a
nx. This is ultimately due to the stability of the polynomial class under a wide
variety of operations, such as pointwise multiplication. On the other hand, these two
categories are certainly closely related (and are, in some sense, equivalent): see [13] for
further discussion.

Acknowledgements. The ﬁrst author is partly supported by a Leverhulme Prize.
The second author is supported by a grant from the Macarthur Foundation and by NSF
grant DMS-0649473. We are extremely grateful to the referee for a careful reading of
the paper, and for suggesting and explaining an alternative (and more self-contained)
proof of Theorem 7.1.

2. Reducing to the equidistributed case

To prove Theorem 1.1, we will apply [9, Theorem 1.19] to decompose g as a product
εg′γ where ε is “smooth”, γ is “rational” and g′ is highly equidistributed in some closed
subgroup G′ ⊆ G. We will recall the precise statement shortly.

In ths section we shall show how the rather harmless factors ε and γ in the above
factorisation may be eliminated, and then make an additional reduction to the case∫

G/Γ F = 0 (using the Haar measure on G/Γ, of course). This leaves us with the task
of proving an “equidistributed” case of Theorem 1.1: see Proposition 2.1 below.

For the rest of the paper, all constants c, C, including those in the asymptotic notation
≪ and O(), are allowed to depend on m and d. Diﬀerent occurrences of the letters c, C
may represent diﬀerent constants; typically we will have 0 < c ≪ 1 ≪ C < ∞. For ease
of notation we drop the subscript whenever Lipschitz norms are mentioned, so ∥F ∥Lip
becomes simply ∥F ∥.

Recall from [9, Deﬁnition 1.3(v)] that a sequence (g(n)Γ)n∈[N ] in a nilmanifold is
totally δ-equidistributed if we have

|En∈P F (g(n)Γ)| ⩽ δ∥F ∥ (2.1)

for all Lipschitz functions F : G/Γ → C with ∫

G/Γ F = 0 and all arithmetic progressions
P ⊆ [N] of length at least δN.

In the next section we shall establish the following result about the lack of correlation
of M¨obius with equidistributed nilsequences.

Proposition 2.1 (M¨obius is orthogonal to equidistributed sequences). Let m ⩾ 0,
d ⩾ 1 be integers and let N ⩾ 1 be an integer parameter which is suﬃciently large
depending on m and d. Let δ, 0 < δ < 1/2, and Q ⩾ 2 be real parameters. Let
G/Γ be an m-dimensional nilmanifold, and suppose that G• is a ﬁltration of degree d.
Suppose that G/Γ has a Q-rational Mal’cev basis X adapted to the ﬁltration G•. Let
g ∈ poly(Z, G•) and suppose that (g(n)Γ)n∈[N ] is totally δ-equidistributed. Then for any
function F : G/Γ → R with ∫

G/Γ F = 0 and for any arithmetic progression P ⊆ [N] of

4 BEN GREEN AND TERENCE TAO

size at least N/Q, we have the bound

|En∈[N ]µ(n)1P (n)F (g(n)Γ)| ≪ δcQ∥F ∥ log N.

The proof of Proposition 2.1 proceeds via the method of Type I/II sums, which is
also known as the method of bilinear forms. This is the same method that one might
use to tackle the “minor arcs” case of (1.1), where α is not close to a rational with
small denominator. We will describe it in detail in the next section. Our task for the
remainder of this section is to reduce Theorem 1.1 to Proposition 2.1.

Proof that Proposition 2.1 implies Theorem 1.1. We start with a brief overview. The
main ingredient of this argument is [9, Theorem 1.19], that is to say the factorization
g = εg′γ mentioned above. In addition to that we require estimates for sums of the type
En∈[N ]µ(n)1P (n), where P ⊆ [N] is a progression. After standard harmonic analysis,
such bounds ultimately depend on results about the zeros of L-functions L(s, χ), and
as such this is analysis of the same type as would be used to establish the “major arc”
cases of (1.1). Finally, a fair amount of what might be called “quantitative nil-linear
algebra” is required to keep track of the various nilmanifolds and Lipschitz functions
involved in the argument. Here we draw repeatedly on the material assembled in [9,
Appendix A] for this purpose; we encourage the reader to gloss over these essentially
routine issues on a ﬁrst reading.

We now turn to the details. We allow all implied constants to depend on m and d.

Let the hypotheses be as in Theorem 1.1. To simplify the notation slightly we will
also assume that ∥F ∥ ⩾ 1; the case ∥F ∥ < 1 can easily be deduced from that case. By
dividing out by ∥F ∥ we may in fact normalize and assume that ∥F ∥ = 1.

We may of course take A ⩾ 1. We may also assume that Q ⩽ log N, since the claim
is vacuously true otherwise; thus X is now a log N-rational Mal’cev basis. By increasing
A if necessary, it will suﬃce to show an estimate of the form

|En∈[N ]µ(n)F (g(n)Γ)| ≪A log−A+O(1) N. (2.2)

Let B be a parameter (depending on A) to be speciﬁed later. We may assume that N
is suﬃciently large depending on A, B. By [9, Theorem 1.19] (with M0 := log N) we
can ﬁnd an integer M, log N ⩽ M ≪ logOB(1) N,
a rational subgroup G′ ⊆ G, a Mal’cev basis X ′ for G′/Γ′ (where Γ′ := G ∩ Γ) in which
each element is an M-rational combination (see [9, Deﬁnition 1.21]) of the elements of
X , and a decomposition g = εg′γ (2.3)
into polynomial sequences ε, g′, γ ∈ poly(Z, G•) with the following properties:

(i) ε : Z → G• is (M, N)-smooth (see [9, Deﬁnition 1.22] for a deﬁnition);
(ii) g′ : Z → G′ takes values in G′, and the ﬁnite sequence (g′(n)Γ′)n∈[N ] is totally
M −B-equidistributed in G′/Γ′, using the metric dX ′ on G′/Γ′;
(iii) γ : Z → G is M-rational (see [9, Deﬁnition 1.21]), and (γ(n)Γ)n∈Z is periodic
with period 1 ⩽ q ⩽ M.

From (2.3) we have

En∈[N ]µ(n)F (g(n)Γ) = En∈[N ]µ(n)F (ε(n)g′(n)γ(n)Γ). (2.4)

THE M ¨OBIUS FUNCTION IS STRONGLY ORTHOGONAL TO NILSEQUENCES 5

The sequence (γ(n)Γ)n∈Z is periodic with some period q, 1 ⩽ q ⩽ M. For each j =
0, 1, . . . , q − 1 let γj := {γ(j)} be the fractional part of γ(j) with respect to Γ, thus
γjΓ = γ(j)Γ and all the coordinates ψX (γj) lie in [0, 1). This construction is described
in [9, Lemma A.14].

Now by [9, Lemma A.12], the coordinates ψX (γ(j)) lie in 1
M ′ Z
m for some M ′ ≪ M O(1).
Since γj = γ(j)η for some η with integer coordinates, it follows from [9, Lemma A.3]
that the coordinates ψX (γj) are rationals with height ≪ M O(1).

We now take advantage of the periodicity of γ(n)Γ to split the right-hand side of
(2.4) as q−1∑

j=0 En∈[N ]µ(n)1n≡j(mod q)F (ε(n)g′(n)γjΓ); (2.5)

By the right-invariance of d, the (M, N)-smoothness of ε (see [9, Deﬁnition 1.21]) and
the 1-Lipschitz bound on F we see that

|F (ε(n)g′(n)γjΓ) − F (ε(n0)g′(n)γjΓ)| ⩽ dX (ε(n)g′(n)γj, ε(n0)g′(n)γj)

= dX (ε(n0), ε(n))

⩽ log−A N.

whenever if |n − n0| ⩽ N
M logA N . Hence if we split each progression n ≡ j(mod q) into

further progressions Pj,k for k = O(M logA N), each having diameter at most N
M logA N ,
we see that (2.5) is equal to
∑

j,k En∈[N ]µ(n)1Pj,k(n)F (aj,kg′(n)γjΓ) + O(log−A N). (2.6)

Here each aj,k := ε(n0,j,k) for some n0,j,k ∈ Pj,k; by the deﬁnition of what it means for
ε : Z → G to be (M, N)-smooth (i.e. [9, Deﬁnition 1.21]), it follows that dX (aj,k, idG) ⩽
M and hence, by [9, Lemma A.4], that

|ψX (aj,k)| ≪ M O(1). (2.7)

If N is suﬃciently large depending on A and B then N ⩾ 10M logA N (say), and this
partition of [N] may be arranged in such a way that

|Pj,k| ⩾ N
2qM logA N ⩾ N
2M 2 logA N .

Since the number of j is at most M, and the number of k is at most M logA N, we
thus see that to show (2.2) it suﬃces by the triangle inequality to show that

|En∈[N ]µ(n)1Pj,k(n)F (aj,kg′(n)γjΓ)| ≪A M −2 log−2A+O(1) N (2.8)

for each j, k.

Fix j, k. Write Hj := γ−1
j G′γj and let gj : Z → Hj be the sequence deﬁned by
gj(n) := γ−1
j g′(n)γj. It is clear that each gj is a polynomial sequence with coeﬃcients
in the ﬁltration (Hj)• := γ−1
j G′
•γj.

Set Λj := Γ ∩ Hj and deﬁne functions

Fj,k : Hj/Λj → [−1, 1]

6 BEN GREEN AND TERENCE TAO

by the formula Fj,k(xΛj) := F (aj,kγjxΓ).

Then (2.8) can be rewritten as

|En∈[N ]µ(n)1Pj,k(n)Fj,k(gj(n)Λj)| ≪A M −2 log−2A+O(1) N. (2.9)

Suppose for the moment that Fj,k were a constant function. Recall that Pj,k has
common diﬀerence q ⩽ M. We may thus apply Proposition A.2 (with A replaced by a
suﬃciently large exponent A
′ depending on A and B) to obtain the desired claim, since
M ≪ logOB(1) N. Therefore we may subtract oﬀ the mean of Fj,k and assume without
loss of generality that ∫

Hj/Λj Fj,k = 0. This may cause Fj,k to take values in [−2, 2]
rather than [−1, 1], but we can easily counter this trivial issue by dividing Fj,k by two.

In a moment we shall use Proposition 2.1 to estimate the terms appearing here. Before
doing that we record quantitative rationality properties of the nilmanifold Hj/Λj, as
well as a Lipschitz bound on ∥Fj,k∥.

Claim. There is a Mal’cev basis Yj for Hj/Λj adapted to the ﬁltration (Hj)• such
that each Yj is an M C-rational combination of the Xi. With respect to the metric
dYj on Hj/Λj induced by this basis, the polynomial sequence gj ∈ poly(Z, (Hj)•) is
M −cB+O(1)-totally equidistributed for some c > 0 depending only on m, d, and we have
∥Fj,k∥ ⩽ M O(1).

Proof. We shall apply suitable combinations of the lemmas in [9, Appendix A].
The existence of Yj follows from Proposition A.9 and Lemma A.13 of [9] together
with the fact that each γj has rational coordinates with height M O(1). Now the map
x ↦→ F (aj,kγjxΓ) on G/Γ has Lipschitz constant at most M O(1) by [9, Lemma A.5]
and the bounds |ψX (aj,k)|, |ψX (γj)| ⩽ M O(1). The ﬁnal statement of the claim, and
the statement about the quantitative equidistribution of gj, now follow from [9, Lemma
A.17].

Let us now apply Proposition 2.1 to (2.9). We apply the proposition with parameters
(which we distinguish using tildes) as follows: ˜G := Hj, ˜Γ := Λj, ˜G• := (Hj)•, ˜g := gj,
˜X := Yj, ˜Q := M O(1), ˜F := Fj,k and ˜δ := M −cB+O(1). We quickly see that (2.9) is

bounded by O (
M −cB+O(1) logO(A) N). Choosing B suﬃciently large depending on A,
we obtain (2.9) as claimed.

3. The equidistributed case: Type I and II sums

In this section we establish Proposition 2.1 using Vinogradov’s method of Type I and
II sums in the form due to Vaughan [17]. More precisely, we will use the following
proposition.

Proposition 3.1 (Method of Type I/II sums). Let f : N → C be a function with
∥f ∥∞ ⩽ 1 such that
 |EN <n⩽2N µ(n)f (n)| ⩾ ε

for some ε > 0. Then one of the following statements holds:

THE M ¨OBIUS FUNCTION IS STRONGLY ORTHOGONAL TO NILSEQUENCES 7

• (Type I sum is large) There exists an integer 1 ⩽ K ⩽ N 2/3 such that

|EN/k<w⩽2N/kf (kw)| ≫ (ε/ log N)O(1) (3.1)

for ≫ (ε/ log N)O(1)K integers k such that K < k ⩽ 2K.

• (Type II sum is large) There exist integers K, W with 1
2 N 1/3 ⩽ K ⩽ 4N 2/3 and
N/4 ⩽ KW ⩽ 4N, such that

|EK<k,k′⩽2KEW ⩽w,w′<2W f (kw)f (k′w)f (kw′)f (k′w′)| ≫ (ε/ log N)O(1). (3.2)

Proof. This is [7, Proposition 4.2], specialised to the case U = V = N 1/3, and with
certain explicit exponents replaced by unspeciﬁed constants O(1).

We now begin the proof of Proposition 2.1. As before we may normalise so that
∥F ∥ = 1. From this and the mean zero assumption, we see in particular that

|F (x)| ⩽ diam(G/Γ) ≪ Q
O(1) (3.3)

for all x ∈ G/Γ (the diameter bound here is [9, Lemma A.16]).

If δ ⩽ 1/N then by (2.1) we have |F (g(n)Γ)| ⩽ δ for all n ∈ [N], and the claim is
trivial, so we may assume that δ > 1/N. By increasing δ if necessary (and shrinking c)
we thus see that we may assume that
 δ > N −σ (3.4)

for any ﬁxed small constant σ > 0 depending only on m, d.

The basic idea, which will become clearer upon reading the details, is to make good use
of the fact that one may test the quantitative equidistribution properties of a polynomial
nilsequence on G/Γ by passing to the abelianisation (G/Γ)ab, a phenomenon referred
to in [9, Theorem 2.9] as the “quantitative Leibman Dichotomy” (cf. [13]). The abelian
issues that one must then deal with are of a very similar nature to those involved in
dealing with exponential sums such as En∈[N ]µ(n)e(p(n)), where p : R → R/Z is an
ordinary polynomial. Rather than quote results from the existing literature on this
problem it is easier for us to invoke various lemmas from [9], which were stated and
proved in a language which is helpful for the present paper.

Let ε := δc1Q log N, for a constant c1 to be speciﬁed later. We may assume that
ε < 1, otherwise the claim is trivial from (3.3) and the triangle inequality. In particular,
we have Q, log N ⩽ δ−c1

and we will use these estimates frequently in the sequel to absorb any polynomial factors
in Q or log N into a power of δ−c1.

Suppose for contradiction that Proposition 2.1 failed for these parameters. We then
apply Proposition 3.1 with f (n) := 1P (n)F (g(n)Γ) and ε as above, concluding that
either (3.1) or (3.2) holds. We deal with these two cases in turn.

The Type I case. Suppose that (3.1) holds. Thus there are ≫ δO(c1)K values of
k ∈ (K, 2K] such that
 |EN/k<w⩽2N/k1P (kw)F (g(kw)Γ)| ≫ δO(c1).

8 BEN GREEN AND TERENCE TAO

Let l denote the common diﬀerence of P ; since |P | ⩾ N/Q, we must have 1 ⩽ l ⩽ Q.
Splitting into progressions with common diﬀerence l, we see that for some b(mod l) and
for ≫ δO(c1)K values of k ∈ (K, 2K] we have

| ∑

N/k<w⩽2N/k
w≡b(mod l)
 1P (kw)F (g(kw)Γ)| ≫ δO(c1) N
kl .

Setting w = b + lw′, this may be rewritten as
∣
∣
∣
∣
∣
 ∑

w′∈Ik F (g(k(b + lw′)Γ)
∣
∣
∣
∣
∣ ≫ δO(c1) N
kl , (3.5)

where Ik ⊆ [ N
2kl − 1, N
kl ] is an interval.

For each value of k for which this holds, consider the sequence gk : Z → G deﬁned
by gk(n) := g(kn) and also the sequence ˜gk : Z → G deﬁned by ˜gk(n) = g(k(b + ln)).
It follows from [9, Corollary 6.8] that gk, ˜gk ∈ poly(Z, G•). Now (3.5) implies that
(˜gk(n)Γ)n∈[Nk] fails to be δO(c1)-equidistributed in G/Γ, where Nk ∼ N/kl.

It follows from [9, Theorem 2.9] that there is a nontrivial horizontal character ψk :
G → R/Z (i.e. a continuous homomorphism from G to R/Z which annihilates Γ) with
magnitude |ψk| ≪ δ−O(c1) such that

∥ψk ◦ ˜gk∥C∞[Nk] ≪ δ−O(c1).

Recall from [9, Deﬁnition 2.10] that the C ∞[N]-norm of a polynomial p : Z → R/Z
expanded in binomial coeﬃcients as

p(n) = α0 + α1
(n
1
) + · · · + αd
(n
d
)
, (3.6)

is deﬁned by ∥p∥C∞[N ] := sup
1⩽j⩽d N j∥αj∥R/Z.

By [9, Lemma 8.4] (specialised to the single-parameter case t = 1), there is some
qk ≪ δ−O(c1) such that ∥qkψk ◦ gk∥C∞[Nk] ≪ δ−O(c1).

Pigeonholing in the possible choices of qkψk, we may ﬁnd some ψ with 0 < |ψ| ≪
δ−O(c1) such that ∥ψ ◦ gk∥C∞[Nk] ≪ δ−O(c1) (3.7)

for ≫ δO(c1)K values of k ∈ (K, 2K].

Write ψ ◦ g(n) = βdn
d + · · · + β0. (3.8)

Then ψ ◦ gk(n) = βdkdn
d + · · · + β0. (3.9)

We would like to use this and (3.7) to conclude that the coeﬃcients kjβj are close
to being integer (or rational with small denominator). This will follow from a simple
lemma.
 THE M ¨OBIUS FUNCTION IS STRONGLY ORTHOGONAL TO NILSEQUENCES 9

Lemma 3.2. Suppose that p : Z → R/Z is a polynomial of the form p(n) = βdn
d +
· · · + β0. Then there is some q ⩾ 1, q = O(1), such that ∥qβj∥R/Z ≪ N −j∥p∥C∞[N ] for
j = 1, . . . , d.

Proof. Consider the representation (3.6) which is used to deﬁne the C ∞[N]-norm.
Observing that βj can be written as a linear combination of αj, . . . , αd with rational
coeﬃcients of height O(1), the result follows upon clearing denominators.

From (3.7), (3.9) and Lemma 3.2 we see that there is some q ⩾ 1, q = O(1), such
that ∥qkjβj∥R/Z ≪ δ−O(c1)(N/K)−j (3.10)

for j = 1, 2, . . . , d and for at least δO(c1)K values of k ∈ (K, 2K].

Fix j, 1 ⩽ j ⩽ d. To pass from the jth powers kj to more general integers we shall
need the following Waring-type result.

Lemma 3.3. Let K ⩾ 1 be an integer, and suppose that S ⊆ [K] is a set of size αK.
Suppose that t ⩾ 2j + 1. Then ≫j,t α2tK j integers in the interval [tK j] can be written
in the form kj
1 + · · · + kj
t , k1, . . . , kt ∈ S.

Proof. It is a well-known consequence of Hardy and Littlewood’s asymptotic formula
for Waring’s problem (see e.g. [18]) that the number of solutions to

x
j
1 + · · · + x
j
t = M, x1, . . . xt ∈ [K]

is ≪j,t K t−j uniformly in M provided that t ⩾ 2j +1. (In fact, by subsequent work, such
a result is known for much smaller values of t when j is large.) Let X = {kj : k ∈ S}
and let r(n) be the number of representations of n as the sum of t elements of X. Then
by the Cauchy-Schwarz inequality and the preceding remarks we have

α2tK 2t = (∑

n r(n))2 ⩽ |tX| ∑

n r(n)2 ≪j |tX|K 2t−j,

which implies the result.

By (3.10) and Lemma 3.3 it follows that

∥qlβj∥R/Z ≪ δ−O(c1)(K/N)j

for ≫ δO(c1)K j values of l ∈ [10dK j].

The following lemma, which is [9, Lemma 3.2], may be applied to this situation.

Lemma 3.4 (Strongly recurrent linear functions are highly non-diophantine). Let α ∈
R, 0 < σ < 1/2, and 0 < µ ⩽ σ/2, and let I ⊆ R/Z be an interval of length µ
such that αn ∈ I for at least σN values of n ∈ [N]. Then there is some k ∈ Z with
0 < |k| ≪ σ−O(1) such that ∥kα∥R/Z ≪ µσ−O(1)/N.

Let us attempt to apply this lemma with σ ≫ δO(c1) and µ ≪ δ−O(c1)(K/N)j. If N
is suﬃciently large and the exponent σ in (3.4) is suﬃciently small, we see using the
bound K/N ⩽ N −1/3 that the hypotheses of the lemma are satisﬁed and that such an
application is permissible. The conclusion is that there is some q′, 1 ⩽ q′ ≪ δ−O(c1),
such that ∥qq′βi∥R/Z ≪ δ−O(c1)N −i. (3.11)

10 BEN GREEN AND TERENCE TAO

Writing ˜ψ := qq′ψ, it follows from (3.8) and (3.11) that for any n we have the bound

∥ ˜ψ ◦ g(n)∥R/Z ≪ δ−O(c1)n/N.

If N ′ := δCc1N for some suﬃciently large C, and if n ∈ [N ′], this implies that

∥ ˜ψ ◦ g(n)∥R/Z ⩽ 1/10. (3.12)

Now set ˜F : G/Γ → [−1, 1] to be the function ˜F := η ◦ ˜ψ, where η : R/Z → [−1, 1]
is a function of Lipschitz norm O(1) and mean zero which equals 1 on [−1/10, 1/10].
Then we have ∫

G/Γ ˜F = 0 and ∥ ˜F ∥ ≪ δ−O(c1). From (3.12), we have

|En∈[N ′] ˜F (g(n)Γ)| ⩾ 1 > δ∥ ˜F ∥,

provided that c1 is chosen suﬃciently small. This is contrary to the assumption that
(g(n)Γ)n∈[N ] is δ-totally equidistributed.

The Type II case. This is in many ways very closely similar to the Type I case, as the
reader will see. Recall the situation that (3.2) puts us in (with our choice of ε): there
are K, W with 1
2N 1/3 ⩽ K ⩽ 4N 2/3 and N/4 ⩽ KW ⩽ 4N such that

|EK<k,k′⩽2KEW <w,w′⩽2W f (kw)f (kw′)f (k′w)f (k′w′)| ≫ δO(c1),

where f (n) = 1P (n)F (g(n)Γ). Writing the left-hand side here as

EK<k,k′⩽2K|EW <w⩽2W f (kw)f (k′w)|2,

we see that there are ≫ δO(c1)K 2 pairs (k, k′) ∈ (K, 2K]
2 such that

|EW <w⩽2W f (kw)f (k′w)| ≫ δO(c1).

Written out in full, for each such pair (k, k′) we have

|EW <w⩽2W 1P (kw)1P (k′w)F (g(kw)Γ)F (g(k′w)Γ)| ≫ (ε/ log N)O(1).

Writing l for the common diﬀerence of P (thus 1 ⩽ l ⩽ Q) we see that there is some
b(mod l) such that for ≫ (ε/ log N)O(1)K 2 pairs (k, k′) we have
∑

W <w⩽2W
w≡b(mod l)
 1P (kw)1P (k′w)F (g(kw)Γ)F (g(k′w)Γ)| ≫ δO(c1) W
l .

Setting w = lw′ + b, this may be written as

| ∑

w′∈Ik,k′ F (g(k(b + lw′)Γ)F (g(k′(b + lw′))Γ)| ≫ δO(c1) W
l , (3.13)

where Ik,k′ ⊆ ( W
l − 1, 2W
l ] is an interval. Since 1 ⩽ l ⩽ Q, which is bounded by a small
power of N, and W ≫ N 1/3, this is contained in [ W
2l , 2W
l ].

For each k, k′ for which this holds, consider the sequence gk,k′ : Z → G × G deﬁned
by gk,k′(n) = (g(kn), g(k′n)), and also the sequence ˜gk,k′ : Z → G × G deﬁned by
˜gk,k′(n) = (g(k(b + ln), g(k′(b + ln))). It follows from [9, Corollary 6.8] that gk,k′, ˜gk,k′ ∈
poly(Z, G• × G•). Now from (3.13) we see that the sequence (˜gk,k′(n)(Γ × Γ))n∈[Nk,k′ ]
fails to be δO(c1)-equidistributed in (G/Γ) × (G/Γ), for some Nk,k′ ∈ [ W
2l , 2W
l ].

THE M ¨OBIUS FUNCTION IS STRONGLY ORTHOGONAL TO NILSEQUENCES 11

It follows from [9, Theorem 2.9] that there is a nontrivial horizontal character ψk,k′ :
G × G → R/Z with |ψk| ≪ δ−O(c1) such that

∥ψk,k′ ◦ ˜gk,k′∥C∞[Nk,k′ ] ≪ δ−O(c1).

By [9, Lemma 8.4] there is some qk,k′ ≪ δ−O(c1) such that

∥qk,k′ψk,k′ ◦ gk,k′∥C∞[Nk,k′ ] ≪ δ−O(c1).

Pigeonholing in the possible choices of qk,k′ψk,k′, we may ﬁnd some ψ with 0 < |ψ| ≪
δ−O(c1) such that
 ∥ψ ◦ gk,k′∥C∞[Nk,k′ ] ≪ δ−O(c1) (3.14)

for ≫ δO(c1)K 2 pairs k, k′ ∈ (K, 2K].

Write ψ = ψ1 ⊕ ψ2, where ψ1, ψ2 : G → R/Z are horizontal characters, not both zero.
If
 ψ1 ◦ g(n) = βdn
d + · · · + β0

and
 ψ2 ◦ g(n) = β′
dn
d + · · · + β′
0

then
 ψ ◦ gk,k′(n) = (βdkd + β′
dk′d)n
d + · · · + (β0 + β′
0),

By Lemma 3.2 and (3.14) there is some 1 ⩽ q ≪ δ−O(c1) such that

∥q(kjβj + k′jβ′
j)∥R/Z ≪ δ−O(c1)N −j
k,k′ ≪ δ−O(c1)(K/N)j

for j = 1, 2, . . . , d and for ≫ δO(c1)K 2 pairs k, k′ ∈ (K, 2K].

Suppose, without loss of generality, that ψ1 ̸= 0. Selecting some k′ that occurs in
≫ δO(c1)K of the pairs k, k′ and subtracting, we see that

∥qkjβj∥R/Z ≪ δ−O(c1)(K/N)j (3.15)

for ≫ δO(c1)K values of k ∈ (−K, K). Using the bounds K ≫ N 1/3 and (3.4) it follows
that we may ignore the contribution of k = 0, that is to say (3.15) holds for ≫ δO(c1)K
values of k ∈ [1, K].

Remark. Note carefully that (3.15) carries no information when k = 0. In our
treatment of Type I sums there was no need for a lower bound on K, but such an
assumption is essential if one has any desire to bound Type II sums.

The estimate (3.15) is identical to (3.10). We may now repeat the arguments used to
obtain a contradiction to (3.10) in Type I case. The proof of Proposition 2.1 and thus
Theorem 1.1 is now complete.

The main business of the paper is now complete. In the next section we give a brief
discussion of how our argument compares with the classical Hardy-Littlewood method.
After that we give a number of applications of Theorem 1.1.

12 BEN GREEN AND TERENCE TAO

4. Remarks on a nilpotent Hardy-Littlewood method

It may be of interest to interpret our method in terms of the “major and minor
arcs” terminology of the Hardy-Littlewood method. Recall that to prove Davenport’s
estimate
 |En∈[N ]µ(n)e(αn)| ≪A log−A N

one divides into two cases: the major arcs where α is close to a rational with small
denominator, and the minor arcs where it is not. The major arcs are handled using
L-function technology as in Appendix A, and the minor arcs are handled using Type
I/II sums as in Proposition 3.1.

Suppose that we are considering the sum

En∈[N ]µ(n)F (g(n)Γ),

where ∫

G/Γ F = 0. Decompose g as a product εg′γ where ε is smooth, γ is rational
and g′ is highly equidistributed on some subgroup G′. Then one might think of g as a
“major arc” nilsequence if G′ = {idG}, and as “minor arc” if G′ is nontrivial.

To justify this terminology, observe that one may interpret e(αn) as F (g(n)Γ), where
G/Γ = R/Z, g : Z → R is the polynomial sequence g(n) = αn and the Lipschitz
function F , taking values in the unit ball of the complex plane, is simply e(θ).

If α = a
q + ε, where ε is small, then the decomposition g = εg′γ will be given by
ε(n) = εn, g′(n) = idG and γ(n) = an/q and so this does indeed correspond to a “major
arc nilsequence”.

If α is not close to a rational with small denominator then g(n) will already be highly
equidistributed on R/Z, and so the decomposition g = εg′γ has ε = γ = idG and g′ = g.
Thus G′ = R is nontrivial and this corresponds to a “minor arc nilsequence”.

5. On bracket polynomials

By a bracket polynomial we mean an object formed from the scalar ﬁeld R and the
indeterminate n using ﬁnitely many instances of the standard arithmetic operations +,
× together with the integer part operation ⌊ ⌋ and the fractional part operation { }. The
following are all bracket polynomials: n
2+n
√2, n
√2⌊n
√3⌋ and {n
3√2+n
7⌊n
√5⌋+√7}.
One may associate a notion of complexity to any bracket polynomial p(n), this being
(for instance) the least number of operations +, ×, ⌊ ⌋, { } required to write down p. In
view of the relation {x}+⌊x⌋ = x, it is not strictly speaking necessary to retain both the
integer and fractional part operations, but we do so here for convenience. Dispensing
with one of them would slightly alter the deﬁnition of complexity.

The following remarkable theorem of Bergelson and Leibman [2] demonstrates a close
link between bracket polynomials and nilmanifolds (see also earlier work of H˚aland, for
example [10]). If G/Γ is a nilmanifold with Mal’cev basis X then recall from [9, Lemma
A.14] that the coordinate map ψ : G → Rm provides an identiﬁcation between G/Γ and
[0, 1)m. Write τ1, . . . , τm for the individual coordinate maps from G/Γ to [0, 1), that is
to say τi is the composition of ψ with the map (t1, . . . , tm) ↦→ ti.

THE M ¨OBIUS FUNCTION IS STRONGLY ORTHOGONAL TO NILSEQUENCES 13

Theorem 5.1 (Bergelson-Leibman). The functions of the form n ↦→ {p(n)}, where p
is a bracket polynomial, coincide with the functions of the form n ↦→ τi(g(n)Γ), where
G/Γ is a nilmanifold equipped with a Mal’cev basis X and g : Z → G is a polynomial
map with coeﬃcients in some ﬁltration G•. The rationality of X , the dimension of G,
the degree of g and the rationality of G• may all be bounded in terms of the complexity
of p, and conversely the complexity of p may be bounded in terms of these quantities.

In fact, Bergelson and Leibman prove a number of rather reﬁned variants of this
type of result, and they also give a comprehensive and edifying discussion of bracket
polynomials in general. At ﬁrst glance it appears that one might immediately combine
Theorem 5.1 with Theorem 1.1 to obtain a result about the correlation of the M¨obius
function with bracket polynomials. There is a serious catch, however: the coordinate
functions τi are not continuous on the nilmanifold G/Γ. Furthermore, as observed by
Bergelson and Leibman, there are bracket polynomials which cannot be written in the
form F (g(n)Γ) for a continuous F . Indeed the results of Leibman [13] on the distribution
of (g(n)Γ)n∈Z imply that the sequence (F (g(n)Γ))n∈Z cannot have isolated values, yet
there are bracket polynomials which do. A simple example is ⌊1 − {n
√2}⌋, which is
zero except when n = 0.

One does nonetheless feel that the discontinuities of τi are “mild”, as this function is
continuous on that part of G/Γ which is identiﬁed with (0, 1)m. However, the sequence
(g(n)Γ)n∈Z may well concentrate on a highly singular subset of G/Γ, as we discussed at
length in [9]. Thus a certain amount of further work is required to obtain the expected
result, which is the following.

Theorem 5.2 (M¨obius and bracket polynomials). Suppose that p(n) is a bracket poly-
nomial and that Ψ : [0, 1] → [−1, 1] is a Lipschitz function. Then we have the estimate

En∈[N ]µ(n)Ψ({p(n)}) ≪A,Ψ log−A N,

where the implied constant depends only on A, Ψ and the complexity of p (but is inef-
fective).

We shall illustrate how this theorem may be deduced from Theorem 1.1 by discussing
two related special cases. We will then sketch the details that are required in order to
write down a complete proof. The authors plan to include a complete proof of Theorem
5.2 in a future publication.

Both special cases will take place on the Heisenberg nilmanifold G/Γ, where

G = ( 1 R R
0 1 R
0 0 1
 ) , Γ = ( 1 Z Z
0 1 Z
0 0 1
 ) .

Computations with Mal’cev bases in this setting were given in [7, Appendix B] and then
again in [9, §5], where we took

e1 = exp(X1) = ( 1 1 0
0 1 0
0 0 1
 ) , e2 = exp(X2) = ( 1 0 0
0 1 1
0 0 1
 ) , e3 = exp(X3) = ( 1 0 1
0 1 0
0 0 1
 ) .

We brieﬂy recall some of the computations carried out in somewhat more detail in that
paper; in any case the proofs are nothing more than computations with 3 × 3 matrices.
The coordinate function ψ : G → R3 is then given by the formula

ψ (( 1 x z
0 1 y
0 0 1
 )) = (x, y, z − xy),

14 BEN GREEN AND TERENCE TAO

and the element written here is equivalent, under right multiplication by an element of
Γ, to the element with coordinates

({x}, {y}, {z − xy − ⌊x⌋y}).

Note that this lies inside the fundamental domain [0, 1)3. It follows that, for any α, β ∈
R, we have {nβ⌊nα⌋} = τ3(g(n)Γ),
where τ3 : G/Γ → [0, 1) is the map into the third coordinate and g : Z → G is the
polynomial sequence given by
 g(n) = ( 1 nα n2αβ
0 1 nβ
0 0 1
 ) .

This is an explicit example of the representation of a bracket polynomial, in this case
{nβ⌊nα⌋}, in the form discussed in Bergelson and Leibman’s theorem.

We discuss two diﬀerent cases.

Case 1. α = √2, β = √3. Then the sequence (g(n)Γ)n∈[N ] is totally N −c-equidistrib-
uted on G/Γ, which makes life rather easy. To prove the equidistribution one may use
[9, Theorem 2.9] together with the lower bound

min
|k1|,|k2|,|k3|⩽K
(k1,k2,k3)̸=(0,0,0) ∥k1√2 + k2√3∥R/Z ≫ K −C,

which follows from the fact that, for any k3 with |k3| ⩽ K, k1√2 + k2√3 + k3 satisﬁes a
quartic over Z with coeﬃcients of size K O(1). Although the function τ3 is not continuous,
it is continuous outside of a subset of G/Γ of measure zero, namely outside of [0, 1)3 \
(0, 1)3. This means that it may be approximated by Lipschitz functions. More precisely,
for any ﬁxed Lipschitz function Ψ : [0, 1] → [−1, 1] and any ε > 0 one may ﬁnd functions
F1, F2 : G/Γ → C with ∥F1∥∞, ∥F2∥∞ ⩽ 1, ∥F1∥Lip, ∥F2∥Lip ⩽ ε−O(1), |Ψ ◦ τ3 − F1| ⩽ F2
pointwise and ∫

G/Γ F2 ⩽ ε. From Proposition (2.1) we have

En∈[N ]µ(n)F1(g(n)Γ) ≪ N −c,

and the uniform distribution of (g(n)Γ)n∈[N ] implies that

En∈[N ]F2(g(n)Γ) ⩽ ε + O(ε−O(1)N −c).

Now we have the bounds

|En∈[N ]µ(n)Ψ(n
√3⌊n
√2⌋)| = |En∈[N ]µ(n)Ψ ◦ τ3(g(n)Γ)|

⩽ |En∈[N ]µ(n)F1(g(n)Γ)| + En∈[N ]F2(g(n)Γ).

Letting ǫ = N −c′ for some suﬃciently small c′ > 0, we obtain an eﬀective and much
stronger version of Theorem 5.2 in this case, namely the bound

En∈[N ]µ(n)Ψ({n
√3⌊n
√2⌋}) ≪ N −c.

Case 2. α = β = √2. Now the sequence (g(n)Γ)n∈[N ] is manifestly not uniformly
distributed on G/Γ. In fact g takes values in the one-dimensional subgroup G′ ⊆ G
deﬁned by
 G′ = {( 1 x x2/2
0 1 x
0 0 1
 ) : x ∈ R}.

THE M ¨OBIUS FUNCTION IS STRONGLY ORTHOGONAL TO NILSEQUENCES 15

The preceding argument breaks down. One could appeal to Theorem 1.1 instead of
Proposition 2.1, but the problem comes when one tries to control the term

En∈[N ]F2(g(n)Γ).

Without knowing something more about the relation between the support properties of
F2 and the orbit (g(n)Γ)n∈[N ], it is not possible to control this term.

In the case at hand (g(n)Γ)n∈[N ] is N −c-equidistributed in the nilmanifold G′/Γ′ where
Γ′ := Γ ∩ G. Topologically and algebraically this nilmanifold is nothing more that R/Z,
but one should note carefully that the Haar measure on this nilmanifold is not the same
as the measure induced from the Haar measure on G. This may be used to “explain”
the observation that n
√2⌊n
√2⌋ is not uniformly distributed modulo one; see [2] for
further details.

Inside G/Γ, G′/Γ′ may be identiﬁed with the union of two segments

{( 1 x x2/2
0 1 x
0 0 1
 ) : 0 ⩽ x < 1} ∪ {( 1 x (1+x2)/2
0 1 x
0 0 1
 ) : 0 ⩽ x < 1},

and this makes it clear that the induced map τ3 : G′/Γ′ → [0, 1) is continuous away
from a single point. By an analysis very similar to the preceding one it may once again
be shown that
 En∈[N ]µ(n)Ψ({n
√2⌊n
√2⌋}) ≪ N −c

for any ﬁxed Lipschitz function Ψ : [0, 1] → [−1, 1].

Amongst examples of the form nβ⌊nα⌋ there is a third distinct case, typiﬁed by
α = β = 21/3. We leave the analysis of this to the reader.

Sketch proof of the general case of Theorem 5.2. By Theorem 5.1, the result of
Bergelson and Leibman, it suﬃces to show, for any ﬁxed Lipschitz function Ψ : [0, 1] →
[−1, 1], that En∈[N ]µ(n)(Ψ ◦ τi)(g(n)Γ) ≪A log−A N.
Here, the notation and parameters are as described in Theorem 5.1. Now τi is continuous
outside the set [0, 1)m \ (0, 1)m, which has zero measure in G/Γ. The issue lies in
understanding how the orbit (g(n)Γ)n∈[N ] interacts with this.

Now the main results of [9] allow us to get a handle on this situation. Consider in
particular the decomposition of g as εg′γ which was obtained in [9, Theorem 1.19].
Recall that ε : Z → G is slowly varying, γ : Z → G is rational and g′ : Z → G′ is
such that (g′(n)Γ′)n∈[N ] is totally equidistributed. For a full proof of Theorem 5.2 one
would naturally need to specify appropriate quantitative parameters here. Suppose for
simplicity that ε = γ = idG (this was, in fact, the case in the two examples above).

Choose a Mal’cev basis for G′/Γ′ with coordinate map ψ′ : G′ → Rm′. Then G′/Γ′

may be identiﬁed with the region ψ′−1([0, 1)m′) ⊆ G, and in this way we think of the
coordinate function τi as a function on G′/Γ′. Write ˜τi for the corresponding function
on [0, 1)m′. It can be shown, making extensive use of the results of [9, Appendix A],
that ˜τi is continuous outside of a piecewise polynomial set of positive codimension, that
is to say outside of a ﬁnite union of sets each of which is deﬁned by some polynomial
inequalities a ⩽ P (t1, . . . , tm′) < b and at least one nontrivial polynomial equation
Q(t1, . . . , tm′) = c. Related matters are discussed at greater length in [2]; in the two

16 BEN GREEN AND TERENCE TAO

examples we discussed, these piecewise polynomial sets were rather simple. These sets
are certainly well-behaved enough that τi may be approximated using Lipschitz functions
F1 and F2 as in our treatment of the bracket polynomial n
√3⌊n
√2⌋, and in this way
one may use Theorem 1.1 to obtain the desired bound

En∈[N ]µ(n)(Ψ ◦ τi)(g′(n)Γ) ≪A log−A N.

If G′ ̸= {id} then one may in fact use Proposition 2.1 to obtain the stronger bound of
N −c, as in the examples.

If ε and γ are not trivial it is even more complicated to write down a fully rigorous
argument, but conceptually things are not much harder at all. The introduction of the
smooth function ε(n) has a rather benign eﬀect; if n ranges over an interval of length
δ′N, for suitably small δ′ = δ′(δ), the discontinuities of the functions x ↦→ τi(ε(n)xΓ)
are all contained inside a “nice” set of measure at most δ, and one may proceed much
as before. All one need do, then, is split the range [N] into suitably short intervals of
this type.

The introduction of γ may be handled much as it was in the proof of Theorem 1.1.
One splits each of the intervals from the previous paragraph into progressions Pj with
the same (small) common diﬀerence q such that γ(n)Γ is constant and equal to γjΓ on
P . One then works with the conjugated sequences γ−1
j g′(n)γj as we did at the end of
§2.

We conclude by remarking on some variants and generalizations of Theorem 5.2. If
p1, . . . , pM are bracket polynomials and F : (R/Z)M → C is a smooth function then one
could establish the estimate

En∈[N ]µ(n)F ({p1(n)}, . . . , {pM (n)}) ≪A log−A N

by Fourier decomposition of F and Theorem 5.2. One could, if desired, restrict the
range of the average to some ﬁxed subprogression P ⊆ [N] by the standard technique
of approximating the cutoﬀ 1P (n) by a smoother function ̃1P (n) and then developing
this as a Fourier expansion.
 6. The Liouville function

Everything we have proved for the M¨obius function also holds for the Liouville func-
tion λ : N → {−1, 1}, deﬁned to be the unique completely multiplicative function such
that λ(p) = −1 for all primes p. This function is related to the M¨obius function via the
identity λ(n) = ∑

r:r2|n µ(n/r2).

Thus, with the notation and assumptions of Theorem 1.1, we have

|En∈[N ]λ(n)F (g(n)Γ)| ≪ ∑

1⩽r⩽√
N
 1
r2 |Em∈[N/r2]µ(m)F (g(r2m)Γ)|.

Now by [9, Corollary 6.8] m ↦→ g(r2m) is a polynomial sequence with coeﬃcients in the
same ﬁltration G• as g, and so we have the bound

|Em∈[N/r2]µ(m)F (g(r2m)Γ)| ≪m,d,A Q
Om,d,A(1)(1 + ∥F ∥Lip) log−A(N/r2)

THE M ¨OBIUS FUNCTION IS STRONGLY ORTHOGONAL TO NILSEQUENCES 17

uniformly in r, so long as N/r2 ⩾ 2. Summing over r we obtain

|En∈[N ]λ(n)F (g(n)Γ)| ≪m,d,A Q
Om,d,A(1)(1 + ∥F ∥Lip)( ∑

r⩽√
N /2
 1
r2 log−A(N/r2)

+ ∑

√N /2<r⩽√
N
 1
r2 )

≪m,d,A Q
Om,d,A(1)(1 + ∥F ∥Lip) log−A N.

This is precisely Theorem 1.1, but with λ taking the place of µ. In a similar fashion,
all of the results of the preceding section concerning bracket polynomials may now also
be deduced with λ in place of µ.

7. A recurrence result along the primes

In this section we derive the following result. Here p1, p2, p3, . . . is the sequence of
primes.

Theorem 7.1 (Prime return times on a nilmanifold). Suppose that G/Γ is a nilmanifold
and that g ∈ G is such that left-multiplication by g is ergodic. Then for every x ∈ G/Γ
the sequence (gpnxΓ)n=1,2,... is equidistributed in G/Γ in the sense that

lim
N →∞ En∈[N ]F (gpnxΓ) = ∫

G/Γ F

for all continuous functions F : G/Γ → [−1, 1].

Remarks. We recall (from discussions in the companion paper [9]) Leon Green’s
criterion for ergodicity of left-multiplication by g; this map is ergodic if and only if
rotation by π(g) is ergodic on the horizontal torus (G/Γ)ab, that is to say if and only if
the entries of π(g) together with 1 are linearly independent over Q. If this is the case
then left-multiplication by any power of g is uniquely ergodic, that is to say

lim
N →∞ En∈[N ]F (gtnxΓ) = ∫

G/Γ F (7.1)

for all x ∈ G/Γ and for t = 1, 2, 3, . . . .

We shall give two proofs of this result. The ﬁrst is quite short but does depend on
results from our earlier paper [8]. The second argument, indicated to us by the referee,
uses only the results of this paper (and [9]).

First proof of Theorem 7.1. Let w be a large number and set W := ∏

p⩽w p. Fix a
nilmanifold G/Γ and a continuous (and hence Lipschitz) function F : G/Γ → [−1, 1].
Then uniformly in the residues b coprime to W we have

lim
N →∞ En∈[N ]( φ(W )
W Λ′(W n + b) − 1)F (gnxΓ) = ow→∞(1), (7.2)

where the convergence is uniform in x ∈ G/Γ and g ∈ G. This follows very quickly
from [8, Proposition 10.2], which was proved under the assumption of the M¨obius and
Nilsequences conjectures MN(s) which we have established in this paper. Recall that
Λ′(p) = log p and that Λ′(n) = 0 if n is not a prime, that is to say Λ′ is a modiﬁed version

18 BEN GREEN AND TERENCE TAO

of the von Mangoldt function with no support on the prime powers p2, p3, . . . . We recall
that the proof of (7.2) is quite substantial. One splits the von Mangoldt function Λ
in a certain way as the sum of two pieces Λ♯ + Λ♭. The contribution from the second
piece is bounded using the MN(s) conjecture, and this is not particularly diﬃcult. The
contribution from the ﬁrst piece is bounded using the machinery of Gowers norms, and
here one must estimate the dual Gowers norm of the nilsequence F (gnxΓ) as well as the
Gowers norm of objects related to Λ♯. This is a substantial amount of work.

Let us return to the proof at hand. Since (7.2) is uniform in g and x, we may replace
g by gW and x by gbx to get

lim
N →∞ En∈Pb,W ( φ(W )
W Λ′(n) − 1)F (gnxΓ) = ow→∞(1)

uniformly for all progressions Pb,W = {W n + b : n ∈ [N]}, b = 0, 1, . . . , W − 1. However
it follows from (7.1) that, for ﬁxed b and W ,

lim
N →∞ En∈Pb,W F (gnxΓ) = ∫
G/Γ F.

Comparing these last two expressions we obtain

φ(W )
W lim
N →∞ En∈Pb,W Λ′(n)F (gnxΓ) = ∫

G/Γ F + ow→∞(1),

uniformly for b coprime to W . Now if b is not coprime to W we obviously have

φ(W )
W lim
N →∞ En∈Pb,W Λ′(n)F (gnxΓ) = ow→∞(1)

since Λ′ is supported on the primes and F is bounded by 1.

Summing over b, one may conclude that

lim
N →∞ En∈[W N ]Λ′(n)F (gnxΓ) = ∫

G/Γ F + ow→∞(1).

This is easily seen to imply that

lim
N →∞ En∈[N ]Λ′(n)F (gnxΓ) = ∫

G/Γ F + ow→∞(1).

The left-hand side no longer depends on w, so we may let w → ∞. Doing so, we obtain

lim
N →∞ En∈[N ]Λ′(n)F (gnxΓ) = ∫

G/Γ F.

An easy argument using the prime number theorem, noting that Λ′(pn) is essentially
log N for almost all primes pn, n ⩽ N, concludes the proof.

Second proof of Theorem 7.1. We sketch a second proof of Theorem 7.1, indicated to
us by the referee. The starting point for this is the observation that Proposition 3.1 holds
equally well with the von Mangoldt function Λ in place of µ, with an almost identical
proof: see [11, Chapter 13]. Therefore, by the techniques of this paper, Proposition 2.1
holds with Λ in place of µ (perhaps with a worse power of log N). One may now model
the arguments of §2, starting with (2.4), the aim being to decompose

En∈[N ]Λ(n)F (gnΓ)

THE M ¨OBIUS FUNCTION IS STRONGLY ORTHOGONAL TO NILSEQUENCES 19

into pieces of the shape En∈[N ]Λ(n)1P (n)F (g(n)Γ)
with (g(n)Γ)n∈[N ] totally equidistributed and ∫

G/Γ F = 0. Then we can apply Proposi-
tion 3.1, with Λ in place of µ.

The argument is very similar to that followed in §2, except that we cannot assert the
analogue of (2.9) unless ∫ Fj,k = 0, and so we are forced to deal with the sums

En∈[N ]Λ(n)1Pj,k(n) ∫

Hj/Γj Fj,k. (7.3)

This can be estimated using the Siegel-Walﬁsz theorem on the progressions Pj,k, noting
that En∈[N ]Λ(n)1Pj,k(n) is equal to q|Pj,k|/φ(q)N if (j, q) = 1 and is negligible otherwise.
Here, q = logO(1) N is the common diﬀerence of the progressions Pj,k. Furthermore, by
equidistribution of (gj(n)Λj)n∈Pj,k we have
∫

Hj /Γj Fj,k ≈ En∈Pj,kFj,k(gj(n)Λj) = En∈Pj,kF (aj,kg′(n)γjΓ).

Hence, by the analysis preceding (2.6), we obtain

En∈[N ]Λ(n)F (gnΓ) = En∈[N ]:(n,q)=1F (gnΓ) + oF,G/Γ,N →∞(1). (7.4)

To handle the term En∈[N ],(n,q)=1F (gnΓ) appearing here, we apply the following rather
curious lemma.

Lemma 7.2. Let G/Γ be a nilmanifold, and suppose that g : Z → G is any polynomial
nilsequence. Let F : G/Γ → [−1, 1] be a Lipschitz function. Let q be squarefree with
1 ⩽ q < N 1/10. Then there is some squarefree q′ < √q such that

En∈[N ],(n,q)=1F (g(n)Γ) = En∈[N ],(n,q′)=1F (g(n)Γ) + O(q−c).

Here, c = cG/Γ,F > 0 is an absolute constant.

To deduce Theorem 7.1 from this and (7.4) is fairly straightforward. Indeed let ε > 0
be arbitrary. Set q1 to be the maximal squarefree divisor of q, the quantity appearing
in (7.4). The conditions (n, q) = 1 and (n, q1) = 1 are of course the same. Now apply
Lemma 7.2 repeatedly, obtaining q2 = q′
1, q3 = q′
2, and so on until the ﬁrst time that
qk < 1/ε. The sum q−c
1 + q−c
2 + · · · + q−c
k−1 arising from the error term in Lemma 7.2 is
bounded by εO(1), and so we obtain

En∈[N ]Λ(n)F (gnΓ) = En∈[N ],(n,qk)=1F (gnΓ) + oF,G/Γ,N →∞(1) + O(εO(1)).

However g acts ergodically on G/Γ, and therefore so does any power of g. It follows
that
 En∈[N ],(n,qk)=1F (gnΓ) = ∫

G/Γ F + oε,F,G/Γ,g;N →∞(1).

Putting all this information together and letting ε → 0 gives the result.

It remains to establish Lemma 7.2. To do this, we use a consequence of [9, Theorem
1.19]: for every M0 there is some r, M0 ⩽ r ⩽ M C
0 , such that

En∈[N ],n≡a(mod r),n≡0(mod d)F (gnΓ) = En∈[N ],n≡a(mod r)F (gnΓ) + O( 1
M0 ) (7.5)

20 BEN GREEN AND TERENCE TAO

uniformly for a(mod r) and for all d ⩽ M0. To see this, apply [9, Theorem 1.19] to get
a decomposition g = εg′γ and choose r, M0 ⩽ r ⩽ M C
0 , to be a period of the rational
sequence γ(n)Γ. Then split the two sums in (7.5) into small intervals on which the
smooth sequence ε(n) is roughly constant, and apply the total equidistribution of g′ to
compare the average with the condition n ≡ 0(mod d) to that without. We leave the
details to the reader.

To establish Lemma 7.2, take M0 = qc with c chosen so small that r ⩽ √q. Set
q′ = (q, r) and split the sum in the lemma as

En∈[N ],(n,q)=1F (gnΓ) = O(N −1/2) + Ea(mod r),(a,q′)=1h(a), (7.6)

where h(a) := En∈[N ],n≡a(mod r),(n,q)=1F (gnΓ).

The error term of O(N −1/2) comes from the fact that various subprogressions of [N]
deﬁned by congruence conditions modulo q or r may have slightly diﬀerent lengths.
Since we are only interested in those a which are coprime to q′We have

h(a) = En∈[N ],n≡a(mod r),(n,q∗)=1F (gnΓ),

where q∗ is the part of q with no factors in common with r. This is equal to

O(N −1/2) + q∗

φ(q∗) En∈[N ],n≡a(mod r)1(n,q∗)=1F (gnΓ).

Using the fact that ∑

d|m µ(d) equals 1 if m = 1 and is zero otherwise, this equals

O(N −1/2) + q∗

φ(q∗) En∈[N ],n≡a(mod r) ∑

d|(n,q∗) µ(d)F (gnΓ),

which is
 O(N −1/2) + q∗

φ(q∗)
 ∑

d|q∗
 µ(d)
d En∈[N ],n≡a(mod r),n≡0(mod d)F (gnΓ).

Split the sum over d into the two ranges d ⩽ M0 and d > M0. The contribution from the
second range can be bounded trivially by O(τ (q∗)2/M0), where τ is the divisor function.
Inside the sum over the ﬁrst range d ⩽ M0, we may apply (7.5). This implies that

h(a) = O(N −1/2) + O( τ (q∗)2

M0 ) + q∗

φ(q∗)
 ∑

d|q∗,d⩽M0
 µ(d)
d En∈[N ],n≡a(mod r)F (gnΓ).

We may drop the condition d ⩽ M0, absorbing the error into the existing O(τ (q∗)2/M0)
term.

Finally, recalling (7.6), we have

En∈[N ],(n,q)=1F (gnΓ) = O(N −1/2) + O( τ (q∗)2

M0 ) + ( q∗

φ(q∗)
 ∑

d|q∗
 µ(d)
d )En∈[N ],(n,q′)=1F (gnΓ).

By M¨obius inversion we have ∑

d|m µ(d)/d = φ(m)/m, thereby concluding the proof.

We remark that very straightforward approximation arguments allow one to replace
the continuous function F in Theorem 7.1 by a function with mild discontinuities. In
this way one could prove, for example, that the sequence pn√3⌊pn√2⌋ is uniformly

THE M ¨OBIUS FUNCTION IS STRONGLY ORTHOGONAL TO NILSEQUENCES 21

distributed modulo one. We leave the details, which are essentially all present in the
earlier discussion of n
√3⌊n
√2⌋, to the reader.

Appendix A. M¨obius and periodic functions

In this appendix we give the proof of Proposition A.2. The argument is, quite apart
from being completely standard, already contained in [7, Chapter 3]. We nonetheless
take the opportunity to recall it here, as we wish to emphasise the fact that the main
input to this part of the argument is information on the zeros of L-functions. Our
starting point is the following proposition.

Proposition A.1. For any A > 0 we have

En∈[N ]µ(n)χ(n) ≪A q1/2 log−A N (A.1)

for all Dirichlet characters χ to modulus q.

Remark. This follows from the nonexistence of zeros of L(s, χ) close to the line ℜs = 1.
For the details, see [11, Prop. 5.29]. As noted in [11, p. 124] there are diﬃculties involved
in applying the standard Perron’s formula approach to En∈[N ]µ(n)χ(n) directly, and it
is rather easier to ﬁrst obtain bounds on En∈[N ]Λ(n)χ(n).

Using standard techniques of harmonic analysis we may obtain the following conse-
quence of Proposition A.1.

Proposition A.2 (M¨obius is orthogonal to periodic sequences). Let f : N → C be a
sequence bounded in magnitude by 1 which is periodic of some period q ⩾ 1. Then we
have En∈[N ]µ(n)f (n) ≪A q log−A N

for all A > 0, where the implied constant is ineﬀective.

Proof. We ﬁrst establish the estimate under the additional assumption that f (n) van-
ishes whenever (n, q) ̸= 1. Then f can be viewed as a function on the multiplicative
group (Z/qZ)×, and thus has a Fourier expansion

f (n) = ∑

χ ˆf (χ)χ(n), where ˆf (χ) := En∈(Z/qZ)× f (n)χ(n),

with χ ranging over all the characters on (Z/qZ)×. Applying Proposition A.1 and the
triangle inequality, we conclude

En∈[N ]µ(n)f (n) ≪A q1/2 log−A N( ∑

χ | ˆf (χ)|)
.

But from Cauchy-Schwarz and Plancherel we have
∑

χ | ˆf (χ)| ⩽ φ(q)1/2(∑

χ | ˆf (χ)|2)1/2 = φ(q)1/2(En∈(Z/qZ)× |f (n)|2)1/2 = O(φ(q)1/2),

where φ(q) := |(Z/qZ)×| is the Euler totient function. Since φ(q) ⩽ q, the claim follows.

Now we consider the general case, in which (n, q) is not necessarily equal to 1 on
the support of f . Observe that if µ(n) is non-zero, then n is square-free, and we can

22 BEN GREEN AND TERENCE TAO

split n = dm, where d = (n, q) is square-free (so µ2(d) = 1) and m is coprime to q.
Furthermore we have µ(n) = µ(d)µ(m). We thus obtain the decomposition

En∈[N ]µ(n)f (n) = 1
N
 ∑

d|q;µ2(d)=1 µ(d) ∑

1⩽m⩽N/d µ(m)f (dm)1(m,q)=1. (A.2)

The sequence m ↦→ f (dm)1(m,q)=1 is periodic of period q/d and vanishes whenever
(m, q/d) ̸= 1, hence by the preceding arguments
∑

1⩽m⩽N/d µ(m)f (dm)1(m,q)=1 ≪A Nq
d2 log−A N.

Thus from (A.2) we have

En∈[N ]µ(n)f (n) ≪A q log−A N ∑

d|q
 1
d2 ≪ q log−A N,

concluding the proof of Proposition A.2.

References

[1] V. Bergelson and I. J. H˚aland, Sets of recurrence and generalized polynomials, Convergence in
ergodic theory and probability (Columbus, OH, 1993), 91–110, Ohio State Univ. Math. Res. Inst.
Publ., 5, de Gruyter, Berlin, 1996.
[2] V. Bergelson and A. Leibman, Distribution of values of bounded generalized polynomials, Acta
Mathematica 198 (2007), 155–230 .
[3] H. Davenport, On some inﬁnite series involving arithmetical functions. II, Quart. J. Math. Oxf.
8 (1937), 313–320.
[4] B. J. Green, Generalising the Hardy-Littlewood method for primes, International Congress of Math-
ematicians. Vol. II, 373–399, Eur. Math. Soc., Z¨urich, 2006.
[5] , Three topics in additive prime number theory, Current developments in mathematics,
2007, 1–41, Int. Press, Somerville, MA, 2009.
[6] B. J. Green and T. C. Tao, An inverse theorem for the Gowers U 3-norm, Proc. Edinburgh Math.
Soc. 51 (2008), no. 1, 73–153.
[7] , Quadratic uniformity of the M¨obius function, Ann. Inst. Fourier (Grenoble) 58 (2008),
no. 6, 1863–1935.
[8] , Linear equations in primes, to appear in Annals of Math.
[9] , The quantitative behaviour of polynomial orbits on nilmanifolds, to appear in Annals of
Math.
[10] I. J. H˚aland, Uniform distribution of generalized polynomials, J. Number Theory 45 (1993), no.
3, 327–366.
[11] H. Iwaniec and E. Kowalski, Analytic number theory, American Mathematical Society Colloquium
Publications, 53. American Mathematical Society, Providence, RI, 2004. xii+615 pp
[12] A. Leibman, Polynomial sequences in groups, Journal of Algebra 201 (1998), 189–206.
[13] , Pointwise convergence of ergodic averages for polynomial sequences of translations on a
nilmanifold, Ergodic Theory and Dynamical Systems 25 (2005), no. 1, 201–213.
[14] A. Mal’cev, On a class of homogeneous spaces, Izvestiya Akad. Nauk SSSR, Ser Mat. 13 (1949),
9–32.
[15] T. C. Tao, Obstructions to uniformity, and arithmetic patterns in the primes, Pure Appl. Math.
Q. 2 (2006), no. 2, part 2, 395–433.
[16] The dichotomy between structure and randomness, arithmetic progressions, and the primes,
International Congress of Mathematicians. Vol. I, 581–608, Eur. Math. Soc., Z¨urich, 2007.
[17] R. C. Vaughan, Sommes trigonom´etriques sur les nombres premiers, C. R. Acad. Sci. Paris S´er.
A-B 285 (1977), no. 16, A981–A983.

THE M ¨OBIUS FUNCTION IS STRONGLY ORTHOGONAL TO NILSEQUENCES 23

[18] , The Hardy-Littlewood method, Second edition. Cambridge Tracts in Mathematics, 125.
Cambridge University Press, Cambridge, 1997. xiv+232 pp

Centre for Mathematical Sciences, Wilberforce Road, Cambridge CB3 0WA, Eng-
land

E-mail address: b.j.green@dpmms.cam.ac.uk

UCLA Department of Mathematics, Los Angeles, CA 90095-1596, USA

E-mail address: tao@math.ucla.edu
