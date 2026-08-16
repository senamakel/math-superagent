<!-- source: https://arxiv.org/pdf/1802.01215 | converted from PDF -->

arXiv:1802.01215v2  [math.NT]  4 Jul 2020
PRIME AND M ¨OBIUS CORRELATIONS FOR VERY
SHORT INTERVALS IN Fq[x].

P ¨AR KURLBERG, LIOR ROSENZWEIG

Abstract. We investigate function ﬁeld analogs of the distribu-
tion of primes, and prime k-tuples, in “very short intervals” of the
form I(f ) := {f (x) + a : a ∈ Fp} for f (x) ∈ Fp[x] and p prime,
as well as cancellation in sums of function ﬁeld analogs of the
M¨obius µ function and its correlations (similar to sums appearing
in Chowla’s conjecture). For generic f , i.e., for f a Morse polyno-
mial, the error terms are roughly of size O(
√p) (with typical main
terms of order p). For non-generic f we prove that independence
still holds for “generic” set of shifts. We can also exhibit exam-
ples for which there is no cancellation at all in M¨obius/Chowla
type sums (in fact, it turns out that (square root) cancellation in
M¨obius sums is equivalent to (square root) cancellation in Chowla
type sums), as well as intervals where the heuristic “primes are
independent” fails badly.
The results are deduced from a general theorem on correlations
of arithmetic class functions; these include characteristic functions
on primes, the M¨obius µ function, and divisor functions (e.g.,
function ﬁeld analogs of the Titchmarsh divisor problem can be
treated.) We also prove analogous, but slightly weaker, results in
the more delicate ﬁxed characteristic setting, i.e., for f (x) ∈ Fq[x]
and intervals of the form f (x) + a for a ∈ Fq, where p is ﬁxed and
q = pl grows.
 1. Introduction

Given a prime p, let Fp denote the ﬁnite ﬁeld with p elements, and
let
 Md = Md(Fp) := {f ∈ Fp[x] : f is monic and deg(f ) = d}

denote the set of monic polynomials of degree d. Gauss gave an exact
formula for the number of prime, or irreducible, polynomials in Md(Fp),

Date: July 1, 2020.
The authors were partially supported by grants from the G¨oran Gustafsson Foun-
dation for Research in Natural Sciences and Medicine, and the Swedish Research
Council (621-2011-5498, 2016-03701). 1

2 P ¨AR KURLBERG, LIOR ROSENZWEIG

namely

|{f ∈ Md(Fp) : f is prime }| = 1
d
 ∑

e|d µ(d/e)pe = pd

d · (1 + O(p−d/2));

since |Md(Fp)| = pd this can be viewed as a function ﬁeld analog of the
Prime Number Theorem as pd tends to inﬁnity, with 1/d playing the
role of the ”prime density”, with square root cancellation in the error
term. In this paper, we shall be concerned with “short interval” analogs
of Gauss’ result, various generalizations to prime k-tuples, square root
cancellation in M¨obius µ sums, as well as sums appearing in Chowla’s
conjecture (these will be described in detail below.) Given f ∈ Fp[x]
we deﬁne a very short interval around f as the set

I(f ) := {f (x) + a : a ∈ Fp};

clearly |I(f )| = p. In order to avoid trivialities we will from now on
assume that deg(f ) ≥ 2. Further, as we are mainly interested in the
large p limit, we will assume that p > d unless otherwise noted (cf.
Section 7 for results when p is ﬁxed but q = pl grows.)

1.1. Results for generic intervals. An element f ∈ Md(Fp) is said
to be a Morse polynomial provided that f has d − 1 distinct critical
values, i.e., |{f (ξ) : f ′(ξ) = 0}| = d − 1. A basic fact (cf. Section 2.2)
is that f is Morse for a generic choice of coeﬃcients; in particular,
given f (x) ∈ Md(Fp), the polynomials f (x) + sx will be Morse for all
but Od(1) elements s ∈ Fp. Our ﬁrst result is that an analog of the
Hardy-Littlewood prime k-tuple conjecture holds for almost all very
short intervals, namely the ones “centered” at Morse polynomials. For
simplicity we state the result only for simultaneous prime specializa-
tion, but in fact any set of k factorization patterns can be treated, cf.
Section 1.1.1.

Theorem 1. Assume that f ∈ Md(Fp) is a Morse polynomial, and
d ≥ 2. We then have

(1) |{g ∈ I(f ) : g is prime }| = p
d + Od(√p)

Moreover, given k distinct shifts h1, h2, . . . , hk ∈ Fp, we have

(2) |{g ∈ I(f ) : g + h1, g + h2, . . . , g + hk are prime }|

= p
dk + Od,k(√
p)

The latter assertion is a natural function ﬁeld analogue of the prime
k-tuple conjecture for integers in short intervals. However, unlike

PRIME AND M ¨OBIUS CORRELATIONS FOR VERY SHORT INTERVALS 3

the integer case, for f Morse there are no ﬂuctuations in the Hardy-
Littlewood constants as h1, . . . , hk varies over distinct elements. In-
terestingly, large variations do occur in the non-Morse case (cf. Sec-
tion 1.4), and, very surprisingly, there are non-Morse examples where
“prime independence” breaks down completely for certain rare shifts
(cf. Section 1.4.6.)
We remark that an easy consequence of (1) is a prime number theo-
rem for progressions that is valid for “very large” Morse moduli: given
b ∈ F×
p and a Morse polynomial q(x) ∈ Md(Fp),

|{a ∈ Fp : a · q(x) + b is prime}| = p/d + Od(√p).

The distribution of primes, and prime k-tuples, in “short intervals”,
i.e., sets of the form I(f, 1) := {f (x) + a1x + a0 : a0, a1 ∈ Fq}, or more
generally, sets of the form I(f, m) := {f (x) + ∑m
n=0 anx
n : a0, . . . , am ∈
Fq} for 1 ≤ m < deg(f ), has received considerable attention in the
large ﬁeld limit, i.e., where q = pk → ∞ (in particular allowing for p
ﬁxed). That (1) holds for f “in general” (i.e., when f (x) − t has Galois
group Sd over Fq(t)) goes back to Cohen’s pioneering work [8]; in [9] he
showed that it holds for the short interval I(f, 1) provided f ∈ Md(Fq)
and p > d. In [4] Bary-Soroker removed this size condition for p odd,
and allowed for more general shifts. In [3], the second author, together
with Bank and Bary-Soroker, show that for any prime power q, for all
polynomials f , and m ≥ 3

| {g ∈ I(f, m) : g is prime} | = qm+1

deg(f ) + Odeg f (qm+1/2);

in fact, under minor restrictions on f and q one may take m = 2 or
even m = 1 (it is also implicit that (1) holds for f Morse.) An ana-
log of the prime k-tuple conjecture for the “long” interval Md(Fp) was
shown by Pollack [20] provided that (2p, d) = 1. This co-primality
condition was removed by Bary-Soroker [4]; Bank and Bary-Soroker
then treated the case of short intervals (i.e., I(f, m), m ≥ 2) and q
odd in [2]. We also mention that Entin [11] has shown prime k-tuple
equidistribution for short intervals in a more general setting, namely
for “Bateman-Horn” type specializations (e.g., for nonassociate, sep-
arable and irreducible polynomials F1(x, t), . . . , Fk(x, t) ∈ Fq[x, t], he
obtains the asymptotics for simultaneous irreducibility of the k special-
ized polynomials F1(g(t), t), . . . , Fk(g(t), t), for g ∈ I(f, m)); cf. [10]
for recent further developments. For a nice survey of recent results
on function ﬁeld analogs of similar questions in classical number the-
ory, including analogs of cancellation in M¨obius µ and Chowla sums
described below, see [21].

4 P ¨AR KURLBERG, LIOR ROSENZWEIG

A function ﬁeld analog of the M¨obius µ function on Md(Fp) can be
deﬁned as follows: given a squarefree polynomial g ∈ Md(Fp), write
g as a product of l distinct monic irreducibles, i.e., g = ∏l
i=1 gi, and
deﬁne µ(g) := (−1)l; if g is not squarefree we set µ(g) = 0. We then
ﬁnd that there is square root cancellation in M¨obius sums, as well as in
the auto-correlation type sums appearing in Chowla’s conjecture (cf.
[7]), for very short intervals in the large p limit.

Theorem 2. Assume that f ∈ Md(Fp) is Morse, and d ≥ 2. Then

(3) ∑

g∈I(f ) µ(g) = Od(√p).

More generally, given distinct elements h1, h2, . . . , hk ∈ Fp, we have

(4) ∑

g∈I(f )
 ( k∏

i=1 µ(g + hi)
)
 = Od,k(√p).

For general f (i.e., non-Morse) we shall see that square root cancel-
lation in (3) is equivalent to square root cancellation in (4); moreover
either there is square root cancellation, or there is no cancellation at
all. See Section 1.3 for more details, as well as examples of intervals
on which µ has constant sign.
In [6], Carmon and Rudnick showed that Chowla type sums over
Md(Fq) has square root cancellation as q → ∞, provided q is odd;
in [5], Carmon treated even q. In [16] Keating and Rudnick proved
square root cancellation for M¨obius sum over intervals of type I(f, m)
for m ≥ 2; they also gave examples of polynomials f for which the
M¨obius sum over I(f, 1) has no cancellation at all. We also note that
Entin [11] can treat cancellation in short Chowla type sums in the more
general Bateman-Horn type setting described earlier.

1.1.1. Class function correlations. The above results are easily deduced
from a more general result valid for functions induced from class func-
tions on Sd, the symmetric group on d letters. Brieﬂy, for squarefree
g ∈ Md(Fp) we associate a conjugacy class σg in Sd as follows: fac-
toring g into prime polynomials, i.e., writing g = ∏l
i=1 Pi, choose l
disjoint cycles c1, . . . , cl ∈ Sd such that the length of ci equals deg(Pi)
for 1 ≤ i ≤ l; we then deﬁne σg as the conjugacy class generated by
∏l
i=1 ci.
Now, given a class function φ on Sd (i.e. φ(σ) only depends on
the conjugacy class of σ), the above construction allows us to deﬁne a
function, also denoted φ, on the set of squarefree elements in Md(Fp).
As the number of non-squarefree polynomials in I(f ), for f ∈ Md

PRIME AND M ¨OBIUS CORRELATIONS FOR VERY SHORT INTERVALS 5

is Od(1) (cf. (9)) we may then choose any bounded extension of φ
to Md(Fp). In order to simplify statements we will in what follows
always assume that the supremum norms of all class functions, and
their extensions, are bounded by some absolute constant.

Theorem 3. Assume that f ∈ Md(Fp) is a Morse polynomial, and
d ≥ 2. Further, let φ1, . . . , φk be class functions on Sd, extended as
above to functions on Md(Fp) .Then there exists constants {c(φi)}k
i=1,
given by
 c(φi) = 1
|Sd|
 ∑

σ∈Sd φi(σ), i = 1, . . . , k.

such that ∑

g∈I(f ) φi(g) = p · c(φi) + Od(√p)

for i = 1, . . . , k. Moreover, given distinct elements h1, h2, . . . , hk ∈ Fp,
we have

(5) ∑

g∈I(f )
 ( k∏

i=1 φi(g + hi)
)
 = p ·
 k∏

i=1 c(φi) + Od,k(√p).

We remark that Theorem 3 does not hold in the large q limit, cf. Sec-
tion 7 for further details, together with a suitably weakened indepen-
dence result valid for the large q limit.
When detecting factorization patterns the constants c(φi) can be
given a simple combinatorial interpretation. Namely, given a desired
factorization pattern of g ∈ Md(Fp), associate an Sd-conjugacy class
C as described above. This in turn can be interpreted as a partition
of d, i.e., d = ∑

j≥1 djj (e.g., for the partition 4 = 2 + 1 + 1, d1 = 2,
d2 = 1, and dj = 0 for j > 2). With φ = 1C, where 1C denotes the
characteristic function of the conjugacy class C, we have

c(φ) = |C|
|Sd| = 1
∏

j(jdj (dj!))

(since |C| = |Sd|
∏j jdj (dj !).) For example, if C = {σ ∈ Sd : σ ∼ (123 . . . d)},

we ﬁnd that 1C = 1Prime (the characteristic function on the set of prime
polynomials), and c(1Prime) = |C|/|Sd| = (d − 1)!/d! = 1/d.
Other interesting examples of class functions include the M¨obius µ
function, as well as the function ﬁeld analog of divisor functions dr for
integer r ≥ 2; e.g., d2(g) is the number of ways to decompose g as a
product of two monic polynomials. In particular, Theorems 1 and 2 are
immediate consequences of Theorem 3. In similar fashion we can treat
short interval function ﬁeld analogs of the “shifted divisor problem”,

6 P ¨AR KURLBERG, LIOR ROSENZWEIG

e.g., the sum ∑

g∈I(f ) dr(g)dr(g + 1), as well as the Titchmarsh divisor
problem, e.g., sums of the form ∑

g∈I(f ) 1Prime(g)dr(g+1). These results
can be viewed as very short interval versions of recent results [1] by
Andrade, Bary-Soroker and Rudnick for the full interval Md(Fq).
We remark that Theorem 3 is, via the Chebotarev density theorem,
Galois theoretic at heart (cf. Section 2.3): to each polynomial f (x) +
hi + t we can associate a ﬁeld extension Lhi/Fp(t) with Galois group
Ghi = Gal(Lhi/Fp(t)) ≃ Sd, and the independence implicit in (5) boils
down to linear independence of the ﬁeld extensions Lh1, Lh2, . . . , Lhk.
In particular, with L
k denoting the compositium of Lh1, . . . , Lhk, we
have Gal(L
k/Fp(t)) ≃ (Sd)k.

1.2. Independence results for non-generic intervals. For non-
Morse polynomials the situation is more complicated since Ghi might
be smaller than Sd, and Gal(L
k/Fp(t)) is in general not a product of
groups. However, while independence can fail for non-Morse polyno-
mials (cf. Section 1.4.6), we can still show that independence holds for
“generic” choices of distinct shifts h1, . . . , hk ∈ Fp and p large.

Theorem 4. Let d ≥ 2, and let φ1, . . . , φk be class functions on Sd,
extended as before to functions on Md(Fp). There exists ﬁnite sets
C(φ1, d), . . . , C(φk, d) (with C(φi, d) only depending on φi, d) such that
the following holds: For f ∈ Md(Fp),
∑

g∈I(f ) φi(g) = p · ci + Od(√
p),

where ci ∈ C(φi, d), for i = 1, . . . , k. Moreover, there exists a set
B(f ) ⊂ Fp, of cardinality at most (d − 1)2, with the following property:
given distinct elements h1, h2, . . . , hk ∈ Fp such that hi − hj ̸∈ B(f ) for
i ̸= j, we have

∑

g∈I(f )
 ( k∏

i=1 φi(g + hi)
)
 = p ·
 k∏

i=1 ci + Od,k(√p).

Note that the number of distinct shifts h1, . . . , hk ∈ Fp such that
hi −hj ∈ B(f ) is Ok,d(pk−1), hence independence holds for most choices
of shifts.
Determining the constants ci is delicate
1 and requires some knowl-
edge about Gh1 = Gal(Lh1/Fp(t)) (it turns out that the isomorphism
class of Ghi does not change with hi.) With lh1 := Lh1 ∩ Fp denot-
ing the ﬁeld of constants in Lh1, let Gh1,geom := Gal(Lh1/lh1(t)) denote

1E.g., some factorization patterns might not occur at all, cf. Section 1.4.

PRIME AND M ¨OBIUS CORRELATIONS FOR VERY SHORT INTERVALS 7

the “geometric part” of Gh1. After making a non-canonical labeling of
the roots of f (x) + h1 + t and f (x) + hi + t (regarded as polynomials
with coeﬃcients in Fp(t)), we obtain an identiﬁcation and inclusion
Ghi ≃ Gh1 ⊂ Sd and can write

(6) ci = 1
|Gh1,geom|
 ∑

σ∈τ ·Gh1,geom φi(σ)

where τ ∈ Gh1 is any element such that τ |lh1 acts as Frobenious on
the ﬁnite ﬁeld extension lh1/Fp, i.e., τ (α) = αp for α ∈ lh1. For some
examples where class function constants are computed using Galois
theory, see Sections 1.4.3 and 1.4.4.
The independence can also be explained in terms of Galois theory.
Brieﬂy, after making non-canonical identiﬁcations Ghi ≃ Gh1 for i =
2, 3, . . . , k, we obtain inclusions

Gal(L
k/Fp(t)) ⊂
 k∏

i=1 Ghi ⊂ (Gh1)k

and the independence amounts to Frobenius equidistribution inside the
coset (τ · Gh1,geom)k. We note that the methods (cf. the remark after
Proposition 12) allows us to take φ1, . . . , φk to be class functions on
Gh1, . . . , Ghk, rather than on Sd, and this sometimes allows for going
beyond factorization patterns. E.g., the cycles (123) and (132) are
conjugate in S3, but not in A3 (the latter group is abelian); when
Ghi ≃ A3, after a non-canonical labeling of the roots, we can distinguish
the two cases in terms of the Frobenious action on the roots. Another
example is given in Section 1.4.5.
A more detailed discussion, in particular regarding the set B(f ) can
be found in Sections 2.3 and 2.4.

1.3. Lack of cancellation in M¨obius and Chowla sums. An un-
expected phenomena is the existence of elements f ∈ Md(Fp) for which
there is no cancellation in short interval M¨obius sum, i.e.,
∣
∣
∣
∣
∣
∣
 ∑

g∈I(f ) µ(g)
∣
∣
∣
∣
∣
∣ = p + Od(1).

For example, for d odd and p ≡ 1 mod d, take f (x) = x
d (cf.
Sections 1.4.2 and 5.1.1). Even more surprising, as noted in [16], for
f (x) = x
2p there is complete lack of cancellation for the sum over the
longer interval I(f, 1). In fact, either there is square root cancellation in
both the M¨obius sum as well as the Chowla sum, or there is essentially
no cancellation whatsoever in either sum (cf. Theorem 2.)

8 P ¨AR KURLBERG, LIOR ROSENZWEIG

Theorem 5. Let f ∈ Md(Fp) for d ≥ 2, and let h1, . . . , hk ∈ Fp be
distinct elements. Then one of the following occurs: either both
∣
∣
∣
∣
∣
∣
 ∑

g∈I(f ) µ(g)
∣
∣
∣
∣
∣
∣ = p + Od(1),
 ∣
∣
∣
∣
∣
∣
 ∑

g∈I(f )
 ( k∏

i=1 µ(g + hi)
)∣
∣
∣
∣
∣
∣ = p + Ok,d(1)

holds, or both
∣
∣
∣
∣
∣
∣
 ∑

g∈I(f ) µ(g)
∣
∣
∣
∣
∣
∣ = Od(√
p),
 ∣
∣
∣
∣
∣
∣
 ∑

g∈I(f )
 ( k∏

i=1 µ(g + hi)
)∣
∣
∣
∣
∣
∣ = Ok,d(√p)

holds.

We remark that lack of cancellation is equivalent to the “geometric
part” of a certain Galois group being contained in the alternating group
Ad. More details on this, as well as the proof of Theorem 5 can be found
in Section 5. Moreover, we note that Theorem 5 is not true in the large
q limit (i.e., for p ﬁxed), cf. Section 7.

1.4. Further examples of degenerate intervals. We next give some
additional examples of short intervals exhibiting irregular behavior. For
more details regarding these examples, see Section 6.

1.4.1. Prime density ﬂuctuations. Let f (x) = x
3 and take φ1 = φ2 =
1Prime. Here the constants vary with p, namely c(1Prime, p) = 2/3 for
p ≡ 1 mod 3, whereas c(1Prime, p) = 0 for p ≡ 2 mod 3. In fact, there
are no primes in I(f ) if p ≡ 2 mod 3, and in this case the second
part of Theorem 4 is trivial. On the other hand, it can be shown that
B(f ) = ∅ and hence, for p ≡ 1 mod 3 and h ̸≡ 0 mod p,

(7) ∑

g∈I(f ) 1Prime(g)1Prime(g + h) = (2/3)2 · p + O(√
p).

In other words, after taking into account the larger than expected
prime density (for generic degree 3 polynomials it is 1/3), the short
interval contains the expected number of twin primes (and similarly
for prime k-tuples) — the heuristic “primes are independent” indeed
holds in I(f ) as p → ∞, even though f (x) = x
3 is not Morse.

1.4.2. Lack of cancellation in M¨obius sums. Again we take f (x) = x
3

and, as noted before, for p ≡ 1 mod 3, either f (x)+a splits completely
or is irreducible. In either case, f (x) + a factors into an odd number
of irreducibles and hence µ(f (x) + a) = −1 if f (x) + a is square free,
i.e., for all nonzero a ∈ Fp. If p ≡ 2 mod 3, x
3 + a is a permutation
for all a ∈ Fp. Consequently for all nonzero a, f (x) + a has one linear

PRIME AND M ¨OBIUS CORRELATIONS FOR VERY SHORT INTERVALS 9

factor, and one irreducible quadratic factor, and thus µ(x
3 + a) = 1 for
all nonzero a ∈ Fp.

1.4.3. Class function constants via Galois theory. To illustrate how av-
erages over cosets of the geometric part of G0 determines the class
function constants (cf. (6)) we return to the example f (x) = x
3. Then
L0 = Fp(t, ζ3, 3√
−t), where ζ3 denotes a non-trivial third root of unity,
and l0 = L0 ∩ Fp = Fp(ζ3). If p ≡ 1 mod 3, we have ζ3 ∈ Fp, hence
l0 = Fp, and G0 = G0,geom ≃ A3. Letting φ1, φ2, φ3 denote characteris-
tic functions of the three S3-conjugacy classes {()}, {(123), (132)}, and
{(12), (13), (23)}, the corresponding class function constants given by
Theorem 4 and (6) is then given by c1 = 1/3, c2 = 2/3, c3 = 0 (the key
point is that Frobenious equidistributes in A3.)
If p ≡ 2 mod 3, then l0 = Fp(ζ3) = Fp2, and thus G0 ≃ S3 and
G0,geom ≃ A3. Further, as the action of the Frobenious map α → αp

must act nontrivially on l0, the image of Frobenious equidistributes
in the single conjugacy class given by the non-trival coset of A3 (in
S3), consisting of the three transpositions {(12), (13), (23)}. Hence, for
p ≡ 2 mod 3, we have c1 = c2 = 0, c3 = 1.

1.4.4. Class function constants and “missing” factorization patterns.
Let p be a large prime and let f (x) = x
4−2x
2. Then Gal(f (x)+t, Fp(t))
is isomorphic to D4, the dihedral group with 8 elements. Regarding D4
as a subgroup of S4, the elements of D4, in cycle notation, are

{(1, 4)(2, 3), (1, 3)(2, 4), (1, 3), (2, 4), (1, 2)(3, 4), (1, 2, 3, 4), (1, 4, 3, 2)}.

Parametrizing the factorization patterns of f (x) + a, for a ∈ Fp, by
partitions of 4, we ﬁnd that the diﬀerent factorization patterns occurs
with the following frequencies: 4 = 1+1+1+1: 1/8, 4 = 2+1+1: 2/8,
4 = 3 + 1: 0/8, 4 = 2 + 2: 3/8, and ﬁnally 4 = 4: 2/8. In particular,
f (x) + a cannot split into a linear and a cubic (irreducible) factor.
Let φ1, . . . , φ5 denote class functions (in S4) that equals one on all
permutations corresponding to the factorization pattern given by the
5 diﬀerent partitions of 4 (see above), and zero otherwise. The corre-
sponding class function constants in Theorem 4 are then the same as
the corresponding frequencies listed above, and thus c1 = 1/8, c2 = 2/8,
c3 = 0, c4 = 3/8, and c5 = 2/8.

1.4.5. Going beyond factorization patterns. Again take f (x) = x
4−2x
2;
as noted above we then have Gal(f (x) + t, Fp(t)) ≃ D4. The elements
of D4 that are products of two disjoint transpositions fall into two D4
conjugacy classes, namely {(1, 2)(3, 4), (1, 4)(2, 3)} and {(1, 3)(2, 4)};

10 P ¨AR KURLBERG, LIOR ROSENZWEIG

these two cases (after labeling the roots) can then be distinguished if
we take class functions on D4 rather than on S4.

1.4.6. Breakdown of independence of primes. For general f the issue
of independence for “bad shifts” appears delicate, but we can give an
explicit example of a polynomial f ∈ M4(Fp) for which the interval
I(f ) has the expected prime density, yet prime independence breaks
down for a few “bad” shifts h — there can be large ﬂuctuations in the
Hardy-Littlewood constants for f non-Morse.
Again let f (x) = x
4 − 2x
2 and ﬁrst consider primes p ≡ 1 mod 4;
abusing notation we will let f = fp denote the reduction of f modulo
p. Then

(8) ∑

g∈I(f ) 1Prime(g) = 1
4 · p + O(√
p)

and for h ∈ Fp \ {0, ±1} we have
∑

g∈I(f ) 1Prime(g) · 1Prime(g + h) = 1
42 · p + O(√p),

i.e., prime independence holds. However, for h = ±1, we have
∑

g∈I(f ) 1Prime(g) · 1Prime(g + h) = 1
8 · p + O(√
p)

and independence is clearly violated.
On the other hand, for p ≡ 3 mod 4, the prime density is still 1/4
(e.g., (8) holds), but if h = ±1, then
∑

g∈I(f ) 1Prime(g) · 1Prime(g + h) = O(√
p);

in a sense independence is violated in the worst possible way as the
“twin prime constant” is zero.
We remark that the p-averaged twin prime constant (asymptotically
p ≡ 1 mod 4 holds for half the primes) equals 1/2 · 1/8 + 1/2 · 0 = 1/42,
i.e., we arrive at the expected “independent” density — this is no
coincidence, cf. Section 6.2.

1.5. Acknowledgments. We thank L. Bary-Soroker, A. Granville,
and Z. Rudnick for stimulating and fruitful discussions, as well as their
comments on an early draft, and L. Klurman for pointing out the ap-
plication to primes in progressions to very large moduli.

PRIME AND M ¨OBIUS CORRELATIONS FOR VERY SHORT INTERVALS 11

2. Preliminaries

2.1. Squarefree polynomials in very short intervals. As we are
concerned with class functions on very short intervals we begin by
recording the useful fact that almost all g ∈ I(f ) are squarefree, for
f ∈ Md(Fq) and q large. In fact, given f ∈ Md and distinct shifts
h1, . . . , hk ∈ Fq,

(9) |{g ∈ I(f ) : g + h1, . . . , g + hk are squarefree}| = q + Ok,d(1)

To see this it is enough to verify that (f + h, f ′) = 1 for all but Od(1)
choices of h ∈ Fq, but this is clear as f ′(ξ) = 0 for at most d − 1 values
of ξ ∈ Fq, so the number of h so that f (ξ) + h = 0 is at most d − 1.

2.2. Morse polynomials are generic. As recalled in the introduc-
tion, a polynomial of degree d is called a Morse polynomial if the set
of critical values is of cardinality d − 1. It turns out that for f a Morse
polynomial, the Galois group of f (x) − t is maximal (over Q(t) this
goes back to Hilbert [14].)

Proposition 6 (Cf. [23], Theorem 4.4.5). Assume that (q, 2d) = 1 and
that f ∈ Md(Fq) is a Morse polynomial. Then Gal(f (x)−t/Fq(t)) ≃ Sd.

We remark that Geyer, in the appendix of [15], also treats the case
(q, d) = 1 by introducing a more general notion of Morseness, namely
assuming non-vanishing of the second Hasse-Schmidt derivative of f .
Moreover, he also gives a beautiful Galois theoretic proof that “generic”
polynomials are Morse.

Proposition 7. Let f (x) ∈ Md(Fq) with f ′′(x) ̸= 0, and assume that
(q, 2d) = 1. Then, for all but Od(1) values of s ∈ Fq, the polynomial
fs(x) = f (x) + sx is a Morse polynomial.

Although not stated this way, Proposition 7 is in fact proved in the
last page of the proof of Proposition 4.3 in [15].
Similar criteria for showing that Gal(f (x) + tx
m/Fp(t)) ≃ Sd for
“generic” f and integer m ∈ [1, d − 1] can be found in [18, Section 5].

2.3. Galois theory and the Chebotarev density theorem. For
the convenience of the reader, we collect here some results about Galois
groups of function ﬁelds over ﬁnite ﬁelds. Before doing so, we begin
with the following notations, similar to the ones used in [13, 17].
For f ∈ Md(Fp) and h ∈ Fp, deﬁne Fh(x, t) ∈ Fp[x, t] by

Fh(x, t) := f (x) + h + t.

12 P ¨AR KURLBERG, LIOR ROSENZWEIG

Set Kh = Fp(t)[x]/(Fh(x, t)), let Lh denote its Galois closure, and
let lh := Lh ∩ Fp be the corresponding ﬁeld of constants. As lh is
independent of h (cf. [17, Lemma 5]), it is convenient to deﬁne l = l0.
Given k distinct shifts h1, . . . , hk ∈ Fp, let L
k := Lh1 · Lh2 . . . · Lhk be
the compositum of the ﬁelds Lh1, . . . , Lhk, and let Gk = Gal(L
k/Fp(t)).
Note that Gk is not necessarily a product of groups. We also de-
ﬁne Ghi := Gal(Lhi/Fp(t)) for i = 1, . . . , k; after labeling the roots
of Fh(x, t) we obtain a natural inclusion Gh ֒−→ Sd; similarly we obtain
a natural inclusion Gk ֒−→ Sk
d .
Let lk := L
k ∩Fp denote the ﬁeld of constants in L
k, and let Gk
geom :=
Gal(L
k/lk(t)) denote the geometric part of Gk. Similarly let Ghi,geom :=
Gal(Lhi/lhi(t)) = Gal(Lhi/l(t)) denote the geometric parts of Ghi, for
i = 1, . . . , k. (Here we use that lh does not depend on h, and that
l = l0.)
The set of critical values of f is given by

Rf := {f (ξ) : ξ ∈ Fp, f ′(ξ) = 0};

we then put B(f ) := ((Rf − Rf ) \ {0}) ∩ Fp,

where Rf − Rf denotes the set of diﬀerences {r1 − r2 : r1, r2 ∈ Rf }.
We shall make use of the following properties of the Artin symbol.
Let F (x, t) ∈ Fq[x, t] be a separable irreducible polynomial, and let
L denote its splitting ﬁeld over Fq(t). For all but ﬁnitely many a ∈
Fq, the prime ideal pa = (t − a) ⊂ Fq[t] is unramiﬁed in L, yielding
a well deﬁned conjugacy class ( L/Fq(t)
pa ) ∈ Gal(L/Fq(t)) — the Artin
symbol. Moreover, for these choices of a the splitting type, or the
cycle pattern, of the polynomial F (x, a) (i.e., when specializing t →
a ∈ Fq) is the same as the cycle pattern of ( L/Fq(t)
pa ), interpreted as a
permutation on the roots of F (x, t). Further, given a conjugacy class
C ⊂ Gal(L/Fq(T )), the density of prime ideals for which Artin symbol
lies in C is given by the Chebotarev density Theorem.

Proposition 8 ([12], Proposition 6.4.8.). Let K be a function ﬁeld over
Fq, let d = [K : Fq(t)], let L/K be a ﬁnite Galois extension, and let
C be a conjugacy class in Gal(L/K). With Fqn denoting the algebraic
closure of Fq in L, let m = [L : KFqn]. Let b be a positive integer with
resFqn τ = resFqn Frob
b
q for each τ ∈ C. Let k be a positive integer. If
k ̸≡ b mod n, then Ck(L/K, C) is empty. If k ≡ b mod n, then
∣
∣
∣
∣|Ck(L/K, C)| − |C|
kmqk∣
∣
∣
∣ < 2|C|
km ((m+gL)qk/2+m(2gK +1)qk/4+gL+dm).

PRIME AND M ¨OBIUS CORRELATIONS FOR VERY SHORT INTERVALS 13

Here Frobq ∈ Gal(Fq/Fq) is the Frobenius map given by Frobq(α) =
αq, gL, gK are the genera of the ﬁelds L, K, and

Ck(L/K, C) = {p ⊂ OK : deg(p) = k, p unramiﬁed, (L/K
p
 ) = C}

where OK ⊂ K is the integral closure of Fq[t] in K. In our applications
we will always take K = Fq(t) and in this case OK = Fq[t].
For a squarefree polynomial f ∈ Md(Fq), deﬁne a conjugacy class
σ = σf ⊂ Sd by the Frobenius action α ↦→ αq on the roots of f .
Further, if we let fa(x) := f (x) + a, the conjugacy classes σfa (as
a ∈ Fp ranges over elements such that fa is squarefree) is the same
as the Artin symbols ( L/K
pa ) as a ∈ Fp ranges over elements for which
the prime ideal pa := (t − a) is unramiﬁed, if we take K = Fp(t) and
L = L0 with notation as above (also note that m = |G0,geom| in this
case.)
We next collect some crucial facts about the Galois extensions intro-
duced above. Given a ﬁnite extension E/Fp it will be convenient to let
FrobE denote the map α → α|E|.

Proposition 9 ([17], Section 2). Let f ∈ Md(Fp). Then

(1) For any h ∈ Fp, lh = l0 and Gh ≃ G0.
(2) If h = (h1, . . . , hk) is such that hi − hj /∈ B(f ), then the ﬁeld
extensions Lh1/l(T ), . . . , Lhk/l(T ) are linearly disjoint, where
l = l0 is the ﬁeld of constants of L
k. In particular,

Gk
geom =
 k∏

i=1 Ghi,geom ≃ (G0,geom)k

(3) For h = (h1, . . . , hk) such that hi − hj /∈ B(f ), let C ⊂ Gk be
a conjugacy class of the form C = C1 × . . . Ck, where each Ci
is the corresponding conjugacy class in Ghi (i.e., where Gk <
Gh1 × · · · × Ghk and Ci = πi(C) is the image of C under the i-th
projection.) Then
{
γ ∈ Gk : γ|lk = Froblk, γ|Lhi ∈ Chi ∀i = 1, . . . , k}

is in 1 − 1 correspondence with

k∏

i=1 {γ ∈ G0 : γ|l = Frobl, γ ∈ Ci}

14 P ¨AR KURLBERG, LIOR ROSENZWEIG

which, if we let δ ∈ G0 denote any element such that δ|l = Frobl,
is in 1 − 1 correspondence with

k∏

i=1 ((δ · G0,geom) ∩ Ci) ,

Proof. The proof of the proposition is the content of Lemma 5, Propo-
sition 8, and (the proof of) Lemma 10 in [17]. We note that in Propo-
sition 8 and Lemma 10, the ﬁrst author shows that if Rf + h1, . . . , Rf +
hk are pairwise disjoint (more precisely, he considers h1 = 0, and
Fh(x, t) = f (x)−(h+t), and therefore the sets are of the form Rf −hi),
then linear disjointedness holds, and from that also Lemma 10. We note
that the sets are indeed pairwise disjoint if hi −hj /∈ B(f ) for i ̸= j. □

To prove independence when disjoint ramiﬁcation does not hold, we
need the following key result (cf. [13], Proposition 17 and Lemma 16.)

Proposition 10. If f ∈ Md(Fp) is a Morse polynomial and h1, . . . , hk ∈
Fp are distinct then Gk = Sk
d provided that p > 4k+d−1 + 1.

2.4. Class functions. As mentioned in the introduction, any class
function on Sd can be viewed as an arithmetic class function on the set
of squarefree polynomials in Md(Fp); we then consider any bounded
(by some absolute constant) extension to the set of all polynomials in
Md(Fp).

Proposition 11. Let f ∈ Md(Fp), d ≥ 2 and let φ be a class function
on Sd. Choose γ ∈ G0 such that γ|l acts via α → αp, and let G0,geom
denote the geometric part of G0. Then
∑

g∈I(f ) φ(g) = c(φ) · p + Od(√
p)

where c(φ) = 1
|G0,geom|
 ∑

σ∈γ·G0,geom φ(σ)

Proof. The contribution from non-squarefree g ∈ I(f ) is Od(1) (cf. (9).)
The result now follows from the Chebotarev density theorem. □

Remark: If f is Morse and h ∈ Fp, then Gh,geom = Sd. In the non-
Morse case, the set of possible constants C(φ, d) can be shown to only
depend on φ and d by noting that C(φ, d) is a subset of
(10){ 1
|H|
 ∑

σ∈γH φ(σ) : γ ∈ Sd, H < Sd acts transitively on {1, . . . , d}
}

PRIME AND M ¨OBIUS CORRELATIONS FOR VERY SHORT INTERVALS 15

As an immediate consequence of the Chebotarev density theorem we
can give a more precise description of what the constants might be for
several shifts, when independence is allowed to break down.

Proposition 12. Let φ1, . . . , φk be class functions on Sd and let h1, . . . , hk ∈
Fp be distinct shifts. Choosing γ ∈ Gk such that γ|lk acts via α → αp,
we have ∑

g∈I(f )
 ( k∏

i=1 φi(g + hi)
)
 = c · p + Od,k(√p)

where
 c = 1
|Gk
geom| · ∑

σ∈γ·Gk
geom
 ( k∏

i=1 φi(σi)
)
 ,

and (σ1, . . . , σk) ∈ Sk
d denotes the image of σ ∈ Gk under the natural
inclusion Gk ֒−→ Sk
d .

Remark. In order to go beyond factorization patterns (to distinguish
conjugacy classes having the same factorization pattern), note that the
proof gives a slightly more general version of Proposition 12, where
φ1, . . . , φk are class functions on Gh1, . . . , Ghk, and using the inclusion
Gk ⊂ Gh1 × Gh2 × · · · × Ghk to map σ ∈ Gk to (σ1, . . . , σk) ∈ Gh1 ×
Gh2 × · · · × Ghk.
3. Proofs of Theorems 3 and 4

We begin with proving Theorem 3. The ﬁrst part of the Theorem
is an immediate corollary of Propositions 6 and 11. Indeed, for f ∈
Md(Fp) Morse, G0 = G0,geom = Sd, and the sums in Theorem 3 and in
Proposition 11 are the same. As for the second part, for p suﬃciently
large, Proposition 10 gives that Gk = Gk
geom = Sk
d . By Proposition 12,

∑

g∈I(f )
 ( k∏

i=1 φi(g + hi)
)
 = c · p + Od,k(√p)

where
 c = 1
|Sk
d | · ∑

σ∈Sk
d
 ( k∏

i=1 φi(σi)
)
 =
 k∏

i=1 c(φi),

and c(φi) = 1
|Sd| ∑

σ∈Sd φi(σ) for i = 1, . . . k.
The proof of Theorem 4 is similar. The ﬁrst part follows from Propo-
sition 11; letting ci = 1
|G0,geom| ∑

σ∈˜γ·G0,geom φi(σ) it is clear that C(φi, d),
the set of possible values of ci, is clearly a subset of the ﬁnite set given

16 P ¨AR KURLBERG, LIOR ROSENZWEIG

in (10). As for the second part, we note that, by part (2) of Proposition
9, Gk
geom = (G0,geom)k and it follows that the constant in front of p is

c = 1
|Gk
geom| · ∑

σ∈γ·Gk
geom
 ( k∏

i=1 φi(σi)
)
 =

= 1
|G0,geom|k
 k∏

i=1
 

 ∑

σ∈˜γ·G0,geom φi(σ)


 =
 k∏

i=1 ci,

where γ ∈ Gk is some element such that γ|lk = Froblk, and ˜γ denotes
the image of γ under the projection from Gk to G0.

4. Proof of Theorem 1

Recall that f ∈ Md(Fp) denotes a Morse polynomial. We begin by
showing that the characteristic function on prime polynomials is a class
function. With

1d-cycle(σ) =
 {
1 σ = (i1 · · · id) is a d-cycle
0 otherwise

the function
 φ(f ) =
 {
1d-cycles(σf ) f is squarefree
0 otherwise

on Md(Fp) is a class function, which equals 1Prime since a polynomial is
irreducible if and only if σf is a d-cycle. Hence c(1Prime) is the density
of d-cycles in Sd, namely 1
d, and Theorem 1 now follows from Theorem
3. In a similar way, the “Titchmarsh divisor problem”, and the “shifted
divisor problem” for very short intervals I(f ) may be treated. The
former consider sums of the form
∑

g∈I(f ) 1Primedr(f + h)

where dr(f ) is the number of ways to decompose f as a product of r
monic polynomials, and the latter concerns sums of the form
∑

g∈I(f ) dr1(f + h1) · · · drk(f + hk)

where r1, . . . , rk are positive integers, and h1, . . . hk ∈ Fp are distinct.
Once again, dr(f ) is a class function, since for f squarefree, dr(f ) =

PRIME AND M ¨OBIUS CORRELATIONS FOR VERY SHORT INTERVALS 17

dr(σf ), where dr(σ) is the number of ways to decompose the permu-
tation σ as a product of r disjoint cycles (here we allow for empty
cycles.) We can therefore apply Theorem 3 for these sums and get that
for distinct h1, . . . , hk ∈ Fp,

(11) ∑

g∈I(f ) dr1(f + h1) · · · drk(f + hk) =
 k∏

i=1
 (
n + ri − 1
ri − 1
 )
p + O(p1/2)

(the constants are derived in [1, Lemma 2.2]), and for all nonzero h ∈ Fp

(12) ∑

g∈I(f ) 1Prime · dr(f + h) = 1
n
(n + r − 1
r − 1
 )p + O(p1/2).

5. M¨obius and Chowla type sums in very short intervals

In this section we give proofs of Theorems 2 and 5. We begin with
a discussion of the M¨obius µ function for function ﬁelds.
Given a polynomial f ∈ Md(Fp), let ω(f ) denote the number of
distinct irreducible divisors of f . It is natural to deﬁne the function
ﬁeld M¨obius µ-function by µ(f ) := (−1)ω(f ) for f squarefree; otherwise
we set µ(f ) = 0. For p large and f ∈ Md(Fp), essentially all g ∈ I(f )
are squarefree (cf. (9)), and hence µ is a class function in the sense
previously discussed.
Given σ ∈ Sd, let c(σ) denote the number of cycles in the cycle
representation of σ, including all 1-cycles, e.g., for (12) ∈ S4 we write
(12) = (12)(3)(4) and ﬁnd that c(σ) = 3. Thus µ(f ), for f squarefree,
is given by (−1)c(σf ). It is convenient to abuse notation and deﬁne
µ(σ) := (−1)c(σ) for σ ∈ Sd. It turns out that (−1)c(σ) is closely related
to sgn(σ), the sign of σ regarded as a permutation:

µ(σ) = (−1)c(σ) = (−1)d · sgn(σ)

To see this consider the disjoint cycle decomposition σ = ∏L
i=1 ci (in-
cluding one-cycles). We then have µ(σ) = (−1)L. Now, with L1
denoting the number of even length cycles, and L2 the number of
odd length cycles, we trivially have L = L1 + L2 and moreover that
sgn(σ) = (−1)L1. As the sum of the length of all cycles c1, . . . , cL equals
d (here it is crucial to include one-cycles), we ﬁnd that L2 and d has
the same parity. Hence

sgn(σ) = (−1)L1 = (−1)L1+L2+d = (−1)L+d = µ(σ)(−1)d

and we ﬁnd that µ(σ) = ± sgn(σ), where the sign is given by the parity
of d.

18 P ¨AR KURLBERG, LIOR ROSENZWEIG

Now, if f is Morse, we have G0 = Ggeom = Sd, hence (cf. Theorem 4

c(µ) = 1
|G|
 ∑

σ∈G0 µ(σ) = (−1)d

|Sd|
 ∑

σ∈Sd sgn(σ) = 0.

Thus Theorem 2 immediately follows from Theorem 3.

5.1. The non-Morse case. We begin by characterizing short intervals
on which there is no cancellation in the sum ∑

g∈I(f ) µ(g). Fix γ ∈ G0
such that γ|l acts as α → αp.
First case: We begin by considering the case G0,geom ⊂ Ad (with
Ad ⊂ Sd denoting the alternating group.) Since µ is a class function,
(6) gives that
 c(µ) = 1
|G0,geom|
 ∑

σ∈γ·G0,geom µ(σ)

and since sgn is trivial on G0,geom ⊂ Ad, we ﬁnd that µ(g) has constant
sign for g ∈ I(f ), with the possible exception of O(1) non-squarefree
g. Hence | ∑

g∈I(f ) µ(g)| = p + Od(√p).
Second case: If G0,geom is not contained in Ad, there exist at least
one odd permutation τ ∈ G0,geom; in particular, ∑

σ∈G0,geom sgn(σ) = 0.
Thus,

c(µ) = 1
|G0,geom|
 ∑

σ∈γG0,geom µ(σ) = (−1)d sgn(γ)
|G0,geom|
 ∑

σ∈G0,geom sgn(σ) = 0,

and hence Theorem 3 gives that
∑

g∈I(f ) µ(g) = O(√
p)

In summary, there is (square root) cancellation in ∑

g∈I(f ) µ(g) if and
only if there is sign cancellation in ∑

σ∈G0,geom sgn(σ).

5.1.1. Cancellation in Chowla sums. We ﬁrst note that if h1, . . . , hk ∈
Fp are distinct elements such that hi − hj ̸∈ B(f ) (“the uncorrelated
case”), Theorem 5 follows immediately from Theorem 4.
If hi − hj ∈ B(f ) (“the correlated case”) we argue as follows. As we
have seen, no cancellation in the M¨obius sum ∑

g∈I(f ) µ(g + h1) (which
in turn happens if and only if there is no cancellation in the unshifted
sum ∑

g∈I(f ) µ(g), or in any other shifted sum ∑

g∈I(f ) µ(g + hi), i =
2, . . . , k) is equivalent to Ghi,geom ⊂ Ad for all i. In particular, Gk
geom ⊂

PRIME AND M ¨OBIUS CORRELATIONS FOR VERY SHORT INTERVALS 19
∏k
i=1 Ghi,geom ⊂ A
k
d. Since ∑

g∈I(f ) ∏k
i=1 µ(g + hi) = c · p + Od,k(√p)
where
 c = 1
|Gk
geom| · ∑

(σ1,...,σk)∈γ·Gk
geom
 ( k∏

i=1 µ(σi)
)
 ,

(cf. Proposition 12 and use the natural embedding Gk ֒−→ Sk
d ) we ﬁnd
that there is no cancellation in the Chowla sum.
On the other hand, if there is cancellation in the short M¨obius sum,
there must be some odd permutation in Gh1,geom, and this in fact implies
that the same holds for Gk
geom, provided p is suﬃciently large (in terms
of k.) To see this, deﬁne Rodd ⊂ Rf as the set of critical values of f
giving rise to odd permutations in Gh1,geom. Then, as Gh1,geom is gener-
ated by the inertia subgroups of points outside ∞, and their conjugates
(cf. [23, Proposition 4.4.6]), Rodd is nonempty. By [13, Lemma 16] (in
particular, take H = {−h1, −h2, . . . , −hk}, S = Rodd and note that we
may assume that p > 4k+d ≥ 4k+|Rodd| since the implied constants in
the error terms are allowed to depend on d and k) there must be some
element in the multi-set generated by Rodd + h1, . . . , Rodd + hk that has
odd parity, and hence Gk
geom contains an odd element given by a prod-
uct of an odd number of odd permutations. Thus the elements of Gk
geom
do not have constant sign, and hence there is square root cancellation
in the Chowla sum also in this case.
To see that G0,geom ⊂ Ad does indeed occur (for p large and d ﬁxed;
for interesting examples when p|d, see [6]), we can take f (x) = x
l and
p ≡ 1 mod l for some odd prime l; then G = Ggeom is cyclic of order
l, and all nontrivial elements are given by even l-cycles.

6. Examples of degenerate intervals — further details

6.1. Prime density ﬂuctuations. We take f (x) = x
3, φ1 = φ2 =
1Prime. As I(f ) = {x
3 − t, t ∈ Fp} it is enough to consider splitting
patterns of x
3 − t = 0. For primes p ≡ 1 mod 3, x
3 − t has either zero
or three roots in Fp; the latter happens if and only if t is a cube of
some element in Fp, and there are 1 + (p − 1)/3 such elements. Hence
c(1Prime, p) = 2/3 for p ≡ 1 mod 3. On the other hand, for p ≡ 2
mod 3, the map x → x
3 is a permutation of the elements in Fp, hence
x
3 − t = 0 has one root in Fp no matter what t is. In particular,
c(1Prime, p) = 0 for p ≡ 2 mod 3.
Since x
3 only has one critical value, |Rf | = 1 and hence (h1 + Rf ) ∩
(h2 + Rf ) = ∅ unless h1 = h2; in particular B(f ) = (Rf −Rf ) \ {0} = ∅,
and (7) follows from Theorem 4.

20 P ¨AR KURLBERG, LIOR ROSENZWEIG

6.2. Breakdown of independence of primes. Take f (x) = x
4−2x
2,
and let p be a large prime. The following was shown in [13, Section
4.2]: G ≃ D4, and for h1 = 0, h2 = 1, we have G2 = Gal(L
2/Fp(T ))
(where L
2 denotes the compositum Lh1Lh2), and G2 genuinely depends
on p. Namely, for p ≡ 3 mod 4 we have G2 ≃ D4 × D4, whereas for
p ≡ 1 mod 4, G2 = G2
geom = H is a certain index two subgroup of
D4 × D4. More precisely,

H = ⟨(6, 7), (2, 3)(5, 6)(7, 8), (1, 2)(3, 4)⟩ ⊂ D4 × D4,

where we have identiﬁed the ﬁrst copy of D4 as permutation of {1, 2, 3, 4},
and the second copy as a permutation of {5, 6, 7, 8}. As

D4 = {(1, 4)(2, 3), (1, 3)(2, 4), (1, 3), (2, 4), (1, 2)(3, 4), (1, 2, 3, 4), (1, 4, 3, 2)}

(note that D4 contains exactly two 4-cycles) the Chebotarev density
theorem gives that
 c(1Prime) = 2/|D4| = 2/8 = 1/4

A tedious but straightforward calculation gives that |H| = 32 and
that there are exactly four elements in H corresponding to both f (x)+t
and f (x) + 1 + t being prime for t ∈ Fp, namely (1, 3, 4, 2)(5, 7, 8, 6),
(1, 3, 4, 2)(5, 6, 8, 7), (1, 2, 4, 3)(5, 6, 8, 7), and (1, 2, 4, 3)(5, 7, 8, 6). Hence
the “twin prime density” for the shift h = 1 equals 4/|H| = 4/32 =
1/8 ̸= 1/42. Similarly, the density for the shift h = −1 also equals 1/8.
As mentioned above, for p ≡ 3 mod 4, the compositum L
2 of L0 and
L1 was shown to have maximal Galois group, namely G2 ≃ D4 × D4;
further the ﬁeld of constants of the compositum was shown to equal
Fp[i] (where i
2 = 1). Thus, if σ ∈ G is any element such that σ(i) =
−i, we ﬁnd that Frobenius takes values in the coset σH ⊂ D4 × D4.
In particular, as all elements of G consisting of two 4-cycles in D4 ×
D4 are contained in H, there are no such elements in the coset σH.
Consequently the Chebotarev density for (g, g + 1) both being prime
is zero for p ≡ 3 mod 4 and g ∈ I(f ) (even though c(1Prime) = 1/4.)
On the other hand, the critical points of f (i.e., zeros of f ′) are
{0, −1, 1}, and thus the critical values of f are given by Rf = {0, −1}.
Hence B(f ) = (Rf − Rf ) \ {0} = {−1, 1}, and thus Theorem 4 gives
independence in the sense that the simultaneous prime density for g, g+
h equals 1/42 for h ̸= 0, ±1 and g ∈ I(f ).
The “coincidence” of getting the expected twin prime density when
averaging over all primes p can be explained as follows. We lift the
setup to Q and consider G = Gal(f (x) + t, f (x) + 1 + t/Q(t)). Then
G ≃ D4 × D4, and the constant ﬁeld extension is Q(i). Thus, if we ﬁrst
average over primes p, and then over t ∈ Fp, the Frobenius element

PRIME AND M ¨OBIUS CORRELATIONS FOR VERY SHORT INTERVALS 21

equidistributes in all of G (for p ≡ 1 mod 4 it equidistributes in H,
and for p ≡ 3 mod 4 it equidistributes in the nontrivial coset of H,
and G is the union of these two cosets.) In particular, as there are
4 elements in G whose cycle structure corresponds two simultaneous
prime specialization, we ﬁnd that the p-averaged twin prime density
equals 4/|G| = 4/64 = 1/42, “as expected”.

7. The large q limit

The previous results can be extended to the setting of very short
intervals in Md(Fq) for q = pl as long as p grows (the key point is that
the proof of Lemma 16 in [13] also works for Fq provided p is suﬃciently
large).
The setting of p ﬁxed and letting l grow is more complicated. We
ﬁrst note there is an obvious obstruction to f (x) + sx being Morse
for any value of s ∈ Fq in case p| deg(f ) — clearly deg(f ′) < d − 1
and hence there are at most d − 2 critical values. However, even if we
assume (deg(f ), p) = 1 there are other obstructions for the the Galois
group being maximal (i.e., that Gk
geom = Sk
d ), even though Ghi = Sd
for 1 ≤ i ≤ k. For example, consider the family fs(x) = x
3 + sx for
s ∈ Fq where q = pl and p > 3 is ﬁxed. For all but O(1) choices
of s, fs(x) is Morse, and f ′
s(x) = 3x
2 + s is a quadratic with two
distinct roots in Fq2, and it is easy to see that Rfs = {αs, −αs} for
some αs ∈ Fq2. Taking k = p and letting hi = iαs for 1 ≤ i ≤ k, we
ﬁnd that the multiset-union of R + h1, R + h2, . . . , R + hk, as a set is
a linear Fp-subspace in Fq2, with each element having multiplicity two
(since |R| = 2). Consequently Gk
geom contains only even permutations.
In particular, the equivalence between cancellation in M¨obius sums and
Chowla sums (cf. Theorem 5) does not hold in the large q limit.
A more subtle example of independence breaking down can also be
given. For f (x) = x
4 + x
3 + 3x
2 ∈ M4(F7), the critical values are
given by R = {0, 1, 3}; taking (h1, . . . , h4) = (0, 1, 2, 4) we ﬁnd that
the multiset union of hi + R has multiplicity two on its support. This
type of example cannot occur for p large, but if we ﬁx p and consider
polynomials of the form fs(x) = f (x) + sx, s ∈ F7l for growing l, it
is clear that the above phenomena occur at least once (for s = 0.)
However, if we ﬁx h1, . . . , hk, in some extension of Fp, this can only
happen for Od,k(1) values s ∈ Fq (but note that this set of “exceptional”
s-values depends on the shifts h1, . . . , hk.)

Theorem 13. Fix distinct elements h1, . . . , hk ∈ Fp, and let f0 ∈
Md(Fp) with (p, d(d − 1)) = 1, and let q = pl for some l ≥ 1 large
enough so that f0 ∈ Fq[x] and h1, . . . , hk ∈ Fq. Given s ∈ Fq, let

22 P ¨AR KURLBERG, LIOR ROSENZWEIG

fs(x) = f0(x) + sx and for i = 1, . . . , k, let Ki/Fq(t) denote the ﬁeld
extension generated by fs(x) + hi + t, let Li denote the Galois closure of
Ki, and let L
k denote the compositum of L1, . . . , Lk. Then, for all but
Od,k(1) values of s ∈ Fq, fs is Morse, and we have Gal(L
k/Fq(t)) ≃ Sk
d .

Before giving the proof of Theorem 13 we deduce an immediate corol-
lary, namely a somewhat weaker “large q” analogue of Theorems 1, 2
and 3. To do so we need some additional notation: given f ∈ Md(Fq),
let IFq(f ) := {f (x) + a : a ∈ Fq}, and as usual, for s ∈ Fq let
fs(x) = f (x) + sx.

Corollary 14. Fix distinct elements h1, . . . , hk ∈ Fp, and let f0 ∈
Md(Fp) with (p, d(d − 1)) = 1. There exists a subset Sbad ⊂ Fp, depend-
ing on f0 and h1, . . . , hk, with the following properties:

(1) |Sbad| = Od,k(1).
(2) Let q = pl be any prime power such that h1, . . . , hk ∈ Fq and
f0 ∈ Fq[x]. Then, for s ∈ Fq \ Sbad, Theorems 1, 2, and 3 hold
for the very short interval IFq(fs). For example, if s ∈ Fq \ Sbad,
then

|{g ∈ IFq(fs) : g + h1, . . . , g + hk are irreducible }| = q
dk + Od,k(√q),

and
 ∑

g∈IFq (fs)
 ( k∏

i=1 µ(g + hi)
)
 = Od,k(√q).

As for the proof of Theorem 13, we ﬁrst show that critical values
having constant diﬀerence is a rare occurrence.

Proposition 15. Let f ∈ Md(Fq) where q = pl, and assume that
p ∤ d(d − 1). With s transcendental over Fp, denote fs(x) := f (x) + sx,
and let τ1, τ2 be distinct roots of f ′
s(x) = f ′(x) + s = 0. Then fs(τ1) −
fs(τ2) /∈ Fp.

Proof. Assume by contradiction that c = fs(τ1) − fs(τ2) ∈ Fp, and
deﬁne E = Fq(c). Now, fs(x) = f (x) + sx and f ′
s(x) = f ′(x) + s
are irreducible polynomials over E(s), so for both i = 1, 2, [E(τi) :
E(s)] = d − 1, and [E(τi) : E(fs(τi))] = d. Since the degrees of both
extensions are co-prime we ﬁnd that E(τi) = E(s, fs(τi)), and thus,
since we assume that fs(τ1) = fs(τ2) + c, we ﬁnd that E(τ1) = E(τ2).
This implies that there exist A, B, C, D ∈ E such that τ2 = Aτ1+B
Cτ1+D . We

PRIME AND M ¨OBIUS CORRELATIONS FOR VERY SHORT INTERVALS 23

claim that C = 0, otherwise (note that f ′(τi) = −s for i = 1, 2)

(13)
f (τ1) −f ′(τ1)τ1 = f (τ1) + sτ1 = fs(τ1) = fs(τ2) + c = f (τ2) + sτ2 + c =

f (τ2) − f ′(τ2)τ2 + c = f ( Aτ1 + B
Cτ1 + D ) − Aτ1 + B
Cτ1 + D f ′( Aτ1 + B
Cτ1 + D ) + c,

and after clearing denominators we ﬁnd that τ1 is a root of a polynomial
of degree 2d (here we use p ∤ d −1 so that deg(f (x) −xf ′(x)) = d), with
coeﬃcients in Fp, contradicting that τ1 is transcendental. Therefore
C = 0, and thus τ2 = Aτ1 + B for some A, B ∈ E. Denote h(x) =
f (x) − xf ′(x). Then h(x) − c = h(Ax + B). Let Rh be the multiset
of critical values of h, and Ah the set of critical points of h. For any
a ∈ Ah, (a − B)/A is a critical point of h(Ax + B), and h(a) is a critical
value of h(Ax + B). Therefore Rh is the multiset of critical values also
for h(Ax+B). On the other hand, by the equality h(x)−c = h(Ax+B),
we ﬁnd that Rh = Rh − c. By [15] (cf. Claim D’ in the proof of
Proposition 4.3), critical values are distinct and hence c ̸= 0. We
thus ﬁnd that there exists a nontrivial Fp-action on the multiset Rh,
and therefore p divides the multiset cardinality of Rh, i.e., p divides
deg(h
′) = d − 1, contradicting the assumption that p ∤ d − 1. □

Corollary 16. For f ∈ Md(Fq) such that (q, d(d −1)) = 1, and any set
of k distinct elements H = {h1, . . . , hk} ⊂ Fq, the set B(fs) ∩ (H − H)
is empty for all but Od,k(1) values of s, where B(fs) = (Rfs −Rfs)\{0}.

Proof. By Proposition 15, for s transcendental over Fp, hi ̸= hj, and
τi ̸= τj denoting any two distinct roots of f ′
s(x),

fs(τi) − fs(τj) − (hi − hj) ̸= 0

Let Π(s) := ∏

hi̸=hj
 ∏

τi̸=τj(fs(τi) − fs(τj) − (hi − hj))

Then Π(s) ̸= 0, and as Π(s) is a symmetric polynomial in the roots of
f ′
s(x) = 0, it is a polynomial in s, of degree bounded in terms of d and
k. Since B(fs) ∩ (H − H) ̸= ∅ is equivalent to Π(s) = 0, the result
follows. □

Theorem 13 now follows easily as the extensions L1, . . . , Lk are lin-
early disjoint by Corollary 16.

References

[1] J. C. Andrade, L. Bary-Soroker, and Z. Rudnick. Shifted convolution and
the titchmarsh divisor problem over Fq[t]. Philosophical Transactions of the

24 P ¨AR KURLBERG, LIOR ROSENZWEIG

Royal Society of London A: Mathematical, Physical and Engineering Sciences,
373(2040), 2015.
[2] E. Bank and L. Bary-Soroker. Prime polynomial values of linear functions
in short intervals. Journal of Number Theory, 151(Supplement C):263 – 275,
2015.
[3] E. Bank, L. Bary-Soroker, and L. Rosenzweig. Prime polynomials in short
intervals and in arithmetic progressions. Duke Math. J., 164(2):277–295, 02
2015.
[4] L. Bary-Soroker. Hardy–littlewood tuple conjecture over large ﬁnite ﬁelds. In-
ternational Mathematics Research Notices, 2014(2):568–575, 2014.
[5] D. Carmon. The autocorrelation of the M¨obius function and Chowla’s conjec-
ture for the rational function ﬁeld in characteristic 2. Philos. Trans. Roy. Soc.
A, 373(2040):20140311, 14, 2015.
[6] D. Carmon and Z. Rudnick. The autocorrelation of the M¨obius function and
Chowla’s conjecture for the rational function ﬁeld. Q. J. Math., 65(1):53–61,
2014.
[7] S. Chowla. The Riemann Hypothesis and Hilbert’s Tenth Problem. Mathemat-
ics and its applications. Gordon and Breach, 1987.
[8] S. D. Cohen. The distribution of polynomials over ﬁnite ﬁelds. Acta Arith.,
17:255–271, 1970.
[9] S. D. Cohen. Uniform distribution of polynomials over ﬁnite ﬁelds. J. London
Math. Soc. (2), 6:93–102, 1972.
[10] A. Entin. Monodromy of hyperplane sections of curves and decomposition sta-
tistics over ﬁnite ﬁelds. In preparation.
[11] A. Entin. On the Bateman-Horn conjecture for polynomials over large ﬁnite
ﬁelds. Compos. Math., 152(12):2525–2544, 2016.
[12] M. Fried and M. Jarden. Field Arithmetic. Ergebnisse der Mathematik und
ihrer Grenzgebiete. 3. Folge / A Series of Modern Surveys in Mathematics.
Springer Berlin Heidelberg, 2006.
[13] A. Granville and P. Kurlberg. Poisson statistics via the chinese remainder
theorem. Advances in Mathematics, 218(6):2013 – 2042, 2008.
[14] D. Hilbert. Ueber die Irreducibilit¨at ganzer rationaler Functionen mit ganz-
zahligen Coeﬃcienten. J. Reine Angew. Math., 110:104–129, 1892.
[15] M. Jarden and A. Razon. Skolem density problems over large. In Hilbert’s
Tenth Problem: Relations with Arithmetic and Algebraic Geometry: Workshop
on Hilbert’s Tenth Problem: Relations with Arithmetic and Algebraic Geome-
try, November 2-5, 1999, Ghent University, Belgium, volume 270, page 213.
American Mathematical Soc., 2000.
[16] J. Keating and Z. Rudnick. Squarefree polynomials and m¨obius values in short
intervals and arithmetic progressions. Algebra Number Theory, 10(2):375–420,
2016.
[17] P. Kurlberg. Poisson spacing statistics for value sets of polynomials. Interna-
tional Journal of Number Theory, 05(03):489–513, 2009.
[18] P. Kurlberg and L. Rosenzweig. The chebotarev density theorem for function
ﬁelds — incomplete intervals. Preprint.
[19] W. Li. Number Theory with Applications. Series on University Mathematics.
1996.

PRIME AND M ¨OBIUS CORRELATIONS FOR VERY SHORT INTERVALS 25

[20] P. Pollack. Simultaneous prime specializations of polynomials over ﬁnite ﬁelds.
Proc. Lond. Math. Soc. (3), 97(3):545–567, 2008.
[21] Z. Rudnick. Some problems in analytic number theory for polynomials over a
ﬁnite ﬁeld. In Proc. International Congress of Math (Seoul), volume 2, pages
443–460.
[22] A. Selberg. On the normal density of primes in small intervals, and the diﬀer-
ence between consecutive primes. Arch. Math. Naturvid., 47(6):87–105, 1943.
[23] J.-P. Serre. Topics in Galois theory, volume 1 of Research Notes in Mathemat-
ics. Jones and Bartlett Publishers, Boston, MA, 1992.
[24] A. Weil. Basic Number Theory. Grundlehren der mathematischen Wis-
senschaften. Springer Berlin Heidelberg, 2013.
URL: www.math.kth.se/~kurlberg

Department of Mathematics, KTH Royal Institute of Technology,
SE-100 44 Stockholm, Sweden
E-mail address: kurlberg@math.kth.se

Unit of Mathematics, Afeka Tel Aviv College of Engineering, Mivtza
Kadesh 38, Tel Aviv, Israel
E-mail address: liorr@afeka.ac.il
