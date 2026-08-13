<!-- source: https://www.numdam.org/item/10.5802/jtnb.641.pdf | converted from PDF -->

Bill ALLOMBERT et Karim BELABAS

Practical Aurifeuillian factorization
Tome 20, no 3 (2008), p. 543-553.

<http://jtnb.cedram.org/item?id=JTNB_2008__20_3_543_0>

© Université Bordeaux 1, 2008, tous droits réservés.

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
de Bordeaux 20 (2008), 543-553

Practical Aurifeuillian factorization

par Bill ALLOMBERT et Karim BELABAS

Dedicated to Henri Cohen on his 60th birthday

Résumé. Nous décrivons un algorithme simple pour déterminer
les facteurs d’Aurifeuille des entiers Φd(a), où Φd est le d-ème
polynôme cyclotomique, et a un entier. Sous une hypothèse de
Riemann convenable, l’algorithme termine en temps polynomial
déterministe ˜O(d2L), utilisant un espace O(dL), où l’on a noté
L := log(|a| + 1).

Abstract. We describe a simple procedure to ﬁnd Aurifeuillian
factors of values of cyclotomic polynomials Φd(a) for integers a and
d > 0. Assuming a suitable Riemann Hypothesis, the algorithm
runs in deterministic time ˜O(d2L), using O(dL) space, where L :=
log(|a| + 1).
 Contents

1. When does an Aurifeuillian factorization exist ?. . . . . . . . . . . . . . . . 544
2. A product formula for an Aurifeuillian factor . . . . . . . . . . . . . . . . . . 546
3. An ℓ-adic algorithm and its complexity (a ∈ Z) . . . . . . . . . . . . . . . 548
4. Rational inputs . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 551
5. A gratuitous example . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 552
References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 552

Let Φd denote the d-th cyclotomic polynomial

Φd(X) = ∏

k∈(Z/dZ)∗(X − ζ k
d ),

where ζd is a d-th primitive root of unity. To factor integers of the form
an − 1, it is advantageous to start from the algebraic factors

a
n − 1 = ∏

d|n Φd(a).

Manuscrit reçu le 22 mars 2008.

544 Bill Allombert, Karim Belabas

This trick generalizes to

a
n + 1 = a2n − 1
an − 1 = ∏

d|2n, d∤n Φd(a),

and in fact to an ± bn for integers a and b since rational factors of Φd(a/b)
lead to integer factors of the requested integer.
Less widely known but still classical, it is often possible to reﬁne further
these algebraic factorization. An Aurifeuillian factorization exists if a ∈ Q
is such that aζd =: α2 is a square in Q(ζd). In that case, let N x denote the
absolute norm from Q(ζd) to Q; then

(1) Φd(a) = N (a − ζd) = ±N (ζda − ζ 2
d ) = ±N (α − ζd)N (α + ζd),

where we have used N ζd ∈ Z∗ = {−1, 1}. (In fact, N ζd = 1 for d ̸= 2.) We
thus get two rational factors, the so-called Aurifeuillian factors of Φd(a).
For all complex embeddings σ : Q(ζd) → C, we have |σ(α ± ζd)| ⩾ √a − 1
by the triangle inequality. If a ∈ Z satisﬁes |a| > 4, then √a − 1 > 1 and
we obtain a non-trivial factorization of Φd(a): both Aurifeuillian factors are
integers larger than 1. In fact, essentially the same argument proves that
both factors have roughly the same size.
Usually, Aurifeuille’s trick is presented as polynomial identities of the
form
 Φd(X) = U 2
c,d(X) − cXV 2
c,d(X),

for various constants c and polynomials U, V depending on c, d (Schinzel [9]).
Stevenhagen [10] and Brent [2] give algorithms to compute U and V , us-
ing a Euclidean algorithm and Newton sums identities respectively. Both
algorithms use O(d2) integer operations, and ˜O(d) using asymptotically
fast arithmetic. We do not know a reference for their bit complexity but,
as remarked by Brent, a straightforward implementation of Stevenhagen’s
Euclidean algorithm suﬀers from intermediate expression swell.
In this short note, we propose an algorithm to ﬁnd Aurifeuillian factors,
which is easier to describe and implement than the polynomial approaches
sketched above. It is also more explicit in the sense that extracting from the
literature a polynomial formula yielding a factor for a given factorization
problem is not obvious, whereas we obtain directly an Aurifeuillian factor
of Φd(a), whenever one exists.

1. When does an Aurifeuillian factorization exist ?

Proposition 1.1 (Granville-Pleasants [5]). Let a ∈ Q∗ and let ζd be a
primitive d-th root of unity. Let a∗ be the squarefree integer, which is the

Practical Aurifeuillian factorization 545

canonical representative of a in Q∗/(Q∗)2. Then aζd is a square in Q(ζd) if
and only if a∗ | d and one of the following is true:

• a∗ ≡ 1 (mod 4) and d is odd.
• a∗ ≡ 3 (mod 4) and v2(d) = 1.
• a∗ is even and v2(d) = 2.

Note that the second case v2(d) = 1 reduces to the ﬁrst, because Φd(X) =
Φd/2(−X) in that case. Less obvious, but even more interesting: if

D = 2
v2(d) ∏

p|d,p̸=2 p and A = a
d/D,

we have Φd(a) = ΦD(A) and (d, a) satisﬁes the above conditions if and only
if (D, A) does; in fact A∗ = a∗ and v2(D) = v2(d). On the other hand, if
D′ = ∏p|d p and A′ = ad/D′, we still have Φd(a) = ΦD′(A′), but the pair
(D′, A′) never satisﬁes the above conditions when 4 | d: indeed D′ is even
but (A′)∗ = 1.
The proof of the Proposition is a straightforward case by case analysis,
and provides an explicit square root in each case in terms of Gaussian sums.
Namely, for p an odd prime and ( .
q) the Legendre-Jacobi symbol modulo
the integer q > 1, we have

g(p)
2 =
 (
−1
p
 )

p, where g(p) := ∑

x∈Fp
 (
x
p
)

ζ x
p and ζp := ζ d/p
d ,

g(2)
2 = −2i, where g(2) := i − 1 and i := ζ d/4
d ,

assuming p | d and 4 | d respectively. Let

G(a
∗) = ∏

p|a∗ g(p).

If |a∗| = ∏p p is odd, this yields for instance

G2 =
 ( −1
|a∗|

)
 |a
∗| = (−1) |a∗|−1
2 |a
∗| = (−1) a∗−1
2 a
∗

=
 { a∗ if a∗ ≡ 1 (mod 4),
−a∗ if a∗ ≡ 3 (mod 4).

Note that Proposition 1.1 implies that, if aζd is a square, then a∗ | d, hence
all the primes p | a∗ also divide d; if further a∗ is even, then 4 | d.
Remark 1.2. The interesting special case a = p prime was our original
motivation for this work. Namely, to compute the order of elements in F∗
pn,

546 Bill Allombert, Karim Belabas

in particular to test prospective primitive roots, we need to complete the
factorization of pn − 1 = ∏

d|n Φd(p).

If p divides n, Aurifeuille’s trick provides extra useful factors of the Φd(p)
such that p divides d.

2. A product formula for an Aurifeuillian factor

There are beautiful and unexpected formulas for Aurifeuillian polyno-
mials, see [2, Theorem 1]. Our formula for Aurifeuillian factors is neither
beautiful nor unexpected, but algorithmically useful nevertheless. The Ga-
lois action on the Gaussian sum G is explicit and we write down a variation
on (1) optimized for computational purposes:

Proposition 2.1. Let d > 2, and (d, a) satisfy the conditions of Propo-
sition 1.1. Write a = a∗f 2, f ∈ Q∗ and let G(a) = f ∏p|a∗ g(p) ∈ Q(ζd).
Then ∏

j∈(Z/dZ)∗(χ(j)G − ζ j
d)

is an Aurifeuillian divisor of Φd(a), where

χ(j) =
 




( j
|a∗|) if a∗ odd,
( j
|a∗/2|) if a∗ even and j ≡ 1 (mod 4),
( j
|a∗/2|) i if a∗ even and j ≡ 3 (mod 4).

Proof. The σj : ζd ↦→ ζ j
d, j ∈ (Z/dZ)∗, run over the Galois group of
Gal(Q(ζd)/Q), and N x = ∏j σjx for all x ∈ Q(ζd).

1) We ﬁrst treat the case d odd, a∗ ≡ 1 (mod 4): then a = G(a)2 and ζ 2
d is
a primitive d-th root of 1. In particular

Φd(a) = N (G2 − ζ 2
d ) = N (G − ζd)N (G + ζd).

Since σjg(p) = (j
p
)g(p) for all odd primes p, we obtain

σjG =
 ( j
|a∗|

)

G, hence σj(G − ζd) = χ(j)G − ζ j
d.

2) For completeness, we include the case v2(d) = 1 and a∗ ≡ 3 (mod 4):
then a = −G(a)2 and −ζ 2
d is a primitive d-th root of 1. In particular

Φd(a) = N (−G2 + ζ 2
d ) = N (G − ζd)N (G + ζd).

The computation of σj(G − ζd) is still valid.

Practical Aurifeuillian factorization 547

3) Assume ﬁnally that v2(d) = 2 and a∗ even: then ±iζ2
d = ζ 2±d/4
d are
primitive d-th roots of 1, since gcd(2 ± d/4, d) = 1: indeed 2 ± d/4 is odd
and any odd prime divisor of d and 2 ± d/4 would divide 2. Reusing the
previous computations,

G(a)
2 = f 2(−2i)(−1) (a∗/2)−1
2 (a
∗/2) = (−1) (a∗/2)+1
2 ai,

hence a = ±iG(a)2. It follows

Φd(a) = N (a − (±i)ζ 2
d ) = N ((±i)G2 − (±i)ζ 2
d ) = N (G − ζd)N (G + ζd),

where we use N (±i) = 1 in the last equality. As for the Galois action, we
have σj g(2)
g(2) = ε(j) :=
 {
1 if j ≡ 1 (mod 4)
i if j ≡ 3 (mod 4),

and it follows that
 σjG = ε(j)

( j
|a∗/2|

)

G.
 □

Many analogous products can be written, involving terms of the form
±ζ iG ± ζ j; our product is written so as to

• always multiply G by a trivial factor in a given term: χ(j)G takes
values in {±G, ±iG} which is easily precomputed.
• require the powers of ζ in increasing order, so there is no need to
precompute and store them: they can be obtained by successive
multiplications.
Remark 2.2. In fact, storing a few powers of ζ is still useful: if j1 < j2
are two consecutive integer representatives for elements in (Z/dZ)∗, ζ j2 is
computed as ζ j1 × ζ j2−j1 and the latter lives in a small set which should
be precomputed. As an obvious example, when 2 | d is even, j2 − j1 is even
and only powers of ζ 2 occur, but we can be more thorough and store all
ζ j2−j1.
Estimating the maximal gap j2 − j1 in terms of d is a famous question
of Jacobstahl, and Iwaniec [7] proved that j2 − j1 ≪ (r log(r + 1))2 if d has
r distinct prime divisors. In particular, j2 − j1 = ˜O(log d)2 remains small.
Consequently, the ζ j for j ∈ (Z/dZ)∗ are obtained using ϕ(d) + ˜O(log d)2

modular multiplications, storing no more than ˜O(log d)2 values at a time.
Compared to the obvious algorithm using d − 1 modular multiplications,
we save a factor (d − 1)/ϕ(d) which can be of the order of log log d (when d
is a product of small primes). Of course this technique becomes less useful
if d has few prime factors, in particular it is useless if d is prime!

548 Bill Allombert, Karim Belabas

Remark 2.3. If d is an odd prime such that 2 is a primitive root mod d, a
diﬀerent optimization applies, even though we no longer save on the number
of multiplications: we write j ∈ (Z/dZ)∗ as 2k, and compute

∏

k∈Z/(d−1)Z
 (( 2
|a∗|

)kG − ζ 2k
d
 ),

where the ζ 2k
d are computed by successive squarings, which are slightly
faster than general multiplications. Of course, ( 2
|a∗|) = ±1 is constant and
computed only once. The condition on d implies d ≡ 3, 5 (mod 8) (other-
wise 2 is a square), and is not very restrictive otherwise: out of the 332365
primes congruent to 3, 5 (mod 8) and less than 107, 248491 satisfy it, about
74%.
Remark 2.4. In the case v2(d) = 2, replacing our ad hoc g(2) by the
customary g(2) := ζ2d + ζ −1
2d yields nicer formulas since we then have
σj g(p) = (j
p
)g(p) for all primes p and g(2)2 = 2. Unfortunately, we would
then factor

Φd(a)
2 = NQ(ζ2d)/Q(G2 − ζ 2
2d) = NQ(ζ2d)/Q(G − ζ2d)NQ(ζ2d)/Q(G + ζ2d),

producing essentially the squares of the requested Aurifeuillian factors,
which would force us to work at double accuracy in the next section.

3. An ℓ-adic algorithm and its complexity (a ∈ Z)

There are two main ideas to implement easily and eﬃciently the previ-
ous formula. The ﬁrst one is to compute the product as an ℓ-adic number
for a suitable ℓ, not as a complex number: as usual, this avoids tedious
estimates of roundoﬀ errors. The second one is to compute the product of
local Gaussian sums G directly, as a single ℓ-adic square root of a known
number. We now restrict to a ∈ Z, and defer the general case a ∈ Q to the
next section.
Algorithm 3.1 (Aurifeuillian factorization)
Input: Integers d ∈ Z>0 and a ∈ Z, a ̸= 0.
Output: An Aurifeuillian factor of Φd(a), if one exists.

(1) [Handle trivial cases d ⩽ 2]. If d > 2, goto (2).
If d = 2, set a ← −a.
Return A + 1 if a =: A2 is a square in Z and fail otherwise.
(2) Use Sub-Algorithm 3.2: fail if (d, a) does not satisfy the Granville-
Pleasants criterion. Replace (d, a) by the simpler pair returned by the
algorithm; at this point we also know a∗ and ϕ(d).
(3) Find ℓ, the smallest prime ≡ 1 mod d, and ζ ∈ F∗
ℓ of exact order d.

Practical Aurifeuillian factorization 549

(4) Let B = (
√|a| + 1)ϕ(d) and e the smallest integer such that ℓe > B.
(5) ζ lifts to a primitive d-th root of 1 in Zℓ, still denoted ζ. Using Hensel
lifting, compute z ∈ (Z/ℓeZ) such that z ≡ ζ (mod ℓe).
[End of ℓ-adic initializations.]
(6) Deﬁne γ ∈ (Z/ℓeZ) in the following way: if d is odd, let γ ← a; else

let i ← zd/4 and γ ← (−1) (a∗/2)+1
2 ai.
(7) Compute an approximate ℓ-adic square root G of γ: an integer 0 ⩽
G < ℓe, such that G2 ≡ γ (mod ℓe) (Hensel lift).
(8) Let χ as in Proposition 2.1 and compute the integer 0 ⩽ F < ℓe such
that
 F ≡ ∏

j∈(Z/dZ)∗
 (χ(j)G − zj) (mod ℓ
e).

[Compute zj by successive multiplications; if d is even, precompute
iG.]
(9) Return F .
Sub-Algorithm 3.2 Input: Integers d ∈ Z>0 and a ∈ Z, a ̸= 0.
Output: Fail if the Granville-Pleasants criterion is not satisﬁed. Otherwise re-
turns a pair (D, A) with ΦD(A) = Φd(a), admitting an Aurifeuillian factor;
D = δ or 4δ, where δ is odd and squarefree. Byproducts: computes a∗ = A∗,
and ϕ(D).

(1) If d ≡ 2 (mod 4) set d ← d/2, a ← −a. [Now d is odd or divisible
by 4.]
(2) [Early abort.] Fail if 8 | d, or if d ≡ v2(a) (mod 2), or if (d odd and
a/2v2(a) ̸≡ 1 (mod 4)).
(3) Factor d = ∏ pdp.
(4) Compute the ap := vp(a) for the above p | d, to obtain a partial
factorization a = sign(a) ∏ papb, where b > 0, (b, d) = 1. Fail if b is
not a square in Z.
(5) Let a∗ = sign(a) ∏ap odd p. Fail if a∗ ≡ 3 (mod 4), or a∗ ̸≡ d
(mod 2).
(6) Compute D = 2d2 ∏p|d,p̸=2 p, and let A = ad/D.
(7) Compute ϕ(D); note that the factorization of D is known.
(8) Return (D, A, a∗, ϕ(D)).

Proof. Sub-Algorithm 3.2 is a straightforward implementation of Proposi-
tion 1.1. Now on to the main Algorithm.
Since d > 2 from step (2) on, the d-th cyclotomic ﬁeld has no real
embeddings and the norm has non-negative values. In particular, the Au-
rifeuillian factors N (α ± ζd) are non-negative. Since they are obviously less
than B < ℓe, knowing them mod ℓe is enough to reconstruct them.

550 Bill Allombert, Karim Belabas

For d > 2, a primitive d-th root of 1 exists in Zℓ if and only if ℓ ≡ 1
(mod d); Hensel lifting a solution of X d = 1 of exact order d in F∗
ℓ , we can
approximate it to any desired ℓ-adic accuracy (note that (d, ℓ) = 1).
Since the computed G has the correct square, it is equal to the one
deﬁned in Proposition 2.1 up to sign, but changing G into −G corresponds
to swapping the Aurifeuilian factors, i.e. computing N (G + ζd) instead of
N (G − ζd). □

Remark 3.3. Recall that a = p a small prime is an important special case,
useful in basic computations involving F∗
pn. In the case a = 2, Step (7) of
the main Algorithm simpliﬁes since a = a∗ = 2 and an ℓ-adic square root
G of −ai is i − 1. An analogous simpliﬁcation applies if we only assume
a∗ = 2, since a square root G of −ai is f (i − 1), where a = a∗f 2.

Theorem 3.4. Let L := log(|a| + 1), and M(n) an upper bound for the
bit complexity of multiplication of two n-bits integers. Assume that for all
d > 1, there exists a prime ℓ ≡ 1 (mod d) satisfying ℓ ⩽ DdC for some con-
stants C < 8 and D. Given such an ℓ, Algorithm 3.1 runs in deterministic
time O(dM(dL) + dC/4+ε) = ˜O(d2L), using O(dL) space.

Proof. The Sub-Algorithm handles numbers ⩽ d for a negligible time O(dε)
(including the factorization of d), then computes O(log d) valuations of a
at small primes p ⩽ d in time O((log d)2L), then computes an approximate
square root of b ⩽ |a| in time O(M(L)).
Finding an element of order o in F∗
ℓ is done quickly using randomization.
To do it in deterministic time, we may look for a primitive root and raise
it to the (ℓ − 1)/o-th power. Unconditionally, the least primitive root mod
ℓ is ≪ ℓ1/4+ε by Burgess’s famous result [3].
Hensel lifting a root of X d = 1 to accuracy ℓe is done in time
˜O(dM(log ℓe)), and the square root computation yielding G in time
O(M(log ℓe)). Finally we have O(ϕ(d)) = O(d) multiplications in Z/ℓeZ,
in time O(dM(log ℓe)), and O(d) Jacobi symbols mod a∗, each in time ˜O(d)
(note that a∗ ⩽ d at this point).
From ℓe > B ⩾ ℓe−1, we obtain ℓe ⩽ ℓB, hence

log ℓ
e ⩽ log ℓ + log B ≪ log d + ϕ(d)L ≪ dL,

using ℓ ⩽ DdC, which implies log ℓ ≪C,D log d.
The space complexity follows from noting that the computation stores
O(1) integers less than ℓe, provided we compute the zj successively. Note
that using Remark 2.2 increases our space requirements by a factor r2+ε if
d has r prime divisors. □

Practical Aurifeuillian factorization 551

The existence of ℓ ⩽ DdC as in the Theorem is ensured by Linnik’s theo-
rem, and the best unconditional bound so far is C = 5.5 (Heath-Brown [6]),
which is indeed less than 8. Obviously, such an ℓ can be found in deter-
ministic polynomial time ˜O(dC−1) by applying primality tests to successive
members of the arithmetic progression 1 + d, 1 + 2d, . . . . Unfortunately, this
becomes dominant, and in order to obtain a realistic estimate, we must
make it conditional:

Corollary 3.5. Assuming the Generalized Riemann Hypothesis, Algo-
rithm 3.1 runs in time ˜O(d2L).

Proof. Assuming the Riemann Hypothesis, ℓ ⩽ 2(d log d)2, see [1, Theo-
rem 5.3], and may be found using ˜O(d) compositeness tests. □

Remark 3.6. For a practical randomized way to ﬁnd ζ ∈ F∗
ℓ of order d, factor
ℓ − 1 (notice that the factorization of d | ℓ − 1 is known and the cofactor
(ℓ − 1)/d is expected to be small). Then pick z ∈ [1, ℓ − 1] uniformly at
random until the following test succeeds: compute the order o of z, using [4,
Algorithm 1.4.3]; if d | o, set ζ = zo/d and stop. The probability to ﬁnd an
element whose order is a multiple of d in a cyclic group of order n = ℓ − 1
is 1
n
 ∑

k| n
d ϕ(kd) ⩾ 1
n
 ∑

k| n
d ϕ(k)ϕ(d) = ϕ(d)
d ,

with equality when gcd(n/d, d) = 1. This lower bound does not depend on
ℓ.
Remark 3.7. The ℓ-adic initialization is almost independent from a. To
obtain Aurifeuillian factors of Φd(ai) for ﬁxed d and varying ai, we can
set B = (√maxi |ai| + 1)ϕ(d); the corresponding z may be reused in all
computations.
Remark 3.8. Our straightforward upper bound B = (
√|a| + 1)ϕ(d) is rather
sharp since both factors are also ⩾ (
√|a| − 1)ϕ(d). This also means that,
even if only one factor is desired, the output size is of order Ld; thus our
runtime ˜O(Ld2) is essentially optimal in the L aspect, but d times slower
than an optimal, as yet unknown, quasi-linear algorithm.

4. Rational inputs

To factor Φ(a) where a ∈ Q, essentially the same algorithm applies with
the following modiﬁcations:

(1) We now compute explicitly f ∈ Q∗ such that a = a∗f 2, say f =
u/v for coprime integers u, v.
(2) Our prime ℓ ≡ 1 (mod d) must now also satisfy ℓ ∤ v.

552 Bill Allombert, Karim Belabas

(3) The product
 F = ∏

j∈(Z/dZ)∗(χ(j)G − ζ j
d)

is now a rational number, whose denominator divides vϕ(d). So we
use the bound B = (v(
√a + 1)
)ϕ(d) and compute F vϕ(d) mod ℓe as
before. This is an integer which we can now recognize, and divide
by vϕ(d) to obtain a rational factor of Φd(a).

5. A gratuitous example

Recall that Henri Cohen’s favourite small integer is 49; to celebrate his
60th birthday, we let our PARI/GP [8] implementation compute the Au-
rifeuillian factors of Φ6049(6049):

? install(factor_Aurifeuille, GL);
? d = a = 6049;
? F = factor_Aurifeuille(a,d); \\ one factor.
Output suppressed!
time = 13,760ms
? polcyclo(d, a) / F; \\ the cofactor.
time = 0ms.

The computation was run on an Opteron 880 at 2.4Ghz using PARI/GP
version 2.4.3 (with GMP-4.1.4 multiprecision kernel), producing two fac-
tors having 10899 and 10900 decimal digits in about 14 seconds.
Increasing d by a factor about 10, our implementation computes the
Aurifeuillian factors of Φ60049(60049) (126726 and 126727 decimal digits)
in about 99 minutes on the same machine.

References

[1] E. Bach & J. Sorenson, Explicit bounds for primes in residue classes. Math. Comp. 65
(1996), no. 216, pp. 1717–1735.
[2] R. P. Brent, Computing Aurifeuillian factors, in Computational algebra and number theory
(Sydney, 1992). Math. Appl., vol. 325, Kluwer Acad. Publ., 1995, pp. 201–212.
[3] D. A. Burgess, On character sums and primitive roots. Proc. London Math. Soc. (3) 12
(1962), pp. 179–192.
[4] H. Cohen, A course in computational algebraic number theory. Graduate Texts in Mathe-
matics, vol. 138, Springer-Verlag, Berlin, 1993.
[5] A. Granville & P. Pleasants, Aurifeuillian factorization. Math. Comp. 75 (2006),
no. 253, pp. 497–508.
[6] D. R. Heath-Brown, Zero-free regions for Dirichlet L-functions, and the least prime in an
arithmetic progression. Proc. London Math. Soc. (3) 64 (1992), no. 2, pp. 265–338.
[7] H. Iwaniec, On the problem of Jacobsthal. Demonstratio Math. 11 (1978), no. 1, pp. 225–
231.
[8] PARI/GP, version 2.4.3, Bordeaux, 2008, http://pari.math.u-bordeaux.fr/.

Practical Aurifeuillian factorization 553

[9] A. Schinzel, On primitive prime factors of an −bn. Proc. Cambridge Philos. Soc. 58 (1962),
pp. 555–562.
[10] P. Stevenhagen, On Aurifeuillian factorizations. Nederl. Akad. Wetensch. Indag. Math.
49 (1987), no. 4, pp. 451–468.

Bill Allombert
Université Montpellier 2
CNRS I3M/LIRMM
Place Eugène Bataillon
F-34095 Montpellier cedex, France
E-mail: Bill.Allombert@univ-montp2.fr

Karim Belabas
Université Bordeaux I
Institut de mathématiques de Bordeaux (A2X)
351 cours de la Libération
F-33405 Talence cedex, France
E-mail: Karim.Belabas@math.u-bordeaux.fr
