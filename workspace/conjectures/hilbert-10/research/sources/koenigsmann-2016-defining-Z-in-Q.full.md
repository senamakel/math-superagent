<!-- source: https://arxiv.org/pdf/1011.3424 | converted from PDF -->

arXiv:1011.3424v2  [math.NT]  13 Nov 2013Deﬁning Z in Q

Jochen Koenigsmann

Accepted for publication in Annals of Mathematics

Abstract

We show that Z is deﬁnable in Q by a universal ﬁrst-order formula
in the language of rings. We also present an ∀∃-formula for Z in Q with
just one universal quantiﬁer. We exhibit new diophantine subsets of Q
like the complement of the image of the norm map under a quadratic
extension, and we give an elementary proof for the fact that the set of
non-squares is diophantine. Finally, we show that there is no existen-
tial formula for Z in Q, provided one assumes a strong variant of the
Bombieri-Lang Conjecture for varieties over Q with many Q-rational
points.1

1 Z is universally deﬁnable in Q

Hilbert’s 10th problem was to ﬁnd a general algorithm for deciding, given
any n and any polynomial f ∈ Z[x1, . . . , xn], whether or not f has a zero
in Zn. Building on earlier work by Martin Davis, Hilary Putnam and Julia
Robinson, Yuri Matiyasevich proved in 1970 that there can be no such al-
gorithm. In particular, the existential ﬁrst-order theory Th∃(Z) of Z (in the
language of rings L := {+, ·; 0, 1}) is undecidable. Hilbert’s 10th problem
over Q, i.e., the question whether Th∃(Q) is decidable, is still open.
If one had an existential (or diophantine) deﬁnition of Z in Q (i.e.,
a deﬁnition by an existential 1st-order L-formula), then Th∃(Z) would be
interpretable in Th∃(Q), and the answer would, by Matiyasevich’s Theorem,
again be no. But it is still open whether Z is existentially deﬁnable in Q,

12000 Mathematics Subject Classiﬁcation. Primary 11U05; Secondary 11R52, 11G35,
11U09.
Key words and phrases. Hilbert’s Tenth Problem, diophantine set, undecidability, deﬁn-
ability, quaternion algebra, Bombieri-Lang Conjecture.
The research on this paper started while the author enjoyed the hospitality of the Max-
Planck-Institut Bonn.
 1

and, in fact, towards the end of the paper we provide a reason why it should
not (Corollary 23).
The earliest 1st-order deﬁnition of Z in Q, due to Julia Robinson ([R]),
can be expressed by an ∀∃∀-formula of the shape

φ(t) : ∀x1∀x2∃y1 . . . ∃y7∀z1 . . . ∀z6 f (t; x1, x2; y1, . . . , y7; z1, . . . , z6) = 0

for some f ∈ Z[t; x1, x2; y1, . . . , y7; z1, . . . , z6], i.e., for any t ∈ Q,

t ∈ Z if and only if φ(t) holds in Q.

Recently, Bjorn Poonen ([P1]) managed to ﬁnd an ∀∃-deﬁnition with 2 uni-
versal and 7 existential quantiﬁers. In this paper we present an ∀-deﬁnition
of Z in Q. To search for such a creature is motivated by the following

Observation 0. If there is an existential deﬁnition of Z in Q then there is
also a universal one.

Proof: If Z is diophantine in Q then so is

Q \ Z = {x ∈ Q | ∃m, n, a, b ∈ Z with n ̸= 0, ±1, am + bn = 1 and m = xn}.

Theorem 1. 2 There is a positive integer n and a polynomial g ∈ Z[t; x1, . . . , xn]
such that, for any t ∈ Q,

t ∈ Z if and only if ∀x1 . . . ∀xn ∈ Q g(t; x1, . . . , xn) ̸= 0.

If one measures logical complexity in terms of the number of changes of
quantiﬁers then this is a deﬁnition of Z in Q of least possible complexity:
there is no quantiﬁer-free deﬁnition of Z in Q.

Corollary 2. Q \ Z is diophantine in Q.

In more geometric terms, this says

Corollary 2’. There is a (not necessarily irreducible) aﬃne variety V over
Q and a Q-morphism π : V → A1 such that the image of V (Q) is Q \ Z.

Together with the undecidability of Th∃(Z), Theorem 1 immediately implies

Corollary 3. Th∀∃(Q) is undecidable.

2In the meantime, Theorem 1 has been generalized to arbitrary number ﬁelds K: the
ring of integers of K is universally deﬁnable in K ([Pa]).

2

Here Th∀∃(Q) is the set of all sentences of the shape

∀x1 . . . ∀xk∃y1 . . . ∃yl φ(x1, . . . , xk, y1, . . . , yl),

where φ is a quantiﬁer-free formula in the language of rings L = {+, ·; 0, 1},
that is, a boolean combination of polynomial equations and inequalities be-
tween polynomials in Z[x1, . . . , xk, y1, . . . , yl]. Corollary 3 was proved condi-
tionally, using a conjecture on elliptic curves, in [CZ]. Again, we can phrase
this in more geometric terms:

Corollary 3’. There is no algorithm that decides on input a Q-morphism
π : V → W between aﬃne Q-varieties V, W whether or not π : V (Q) →
W (Q) is surjective.

Acknowledgement: Among many others, I would, in particular, like to
thank Boris Zilber, Jonathan Pila, Marc Hindry and Joseph Silverman for
very helpful discussions. I am also most grateful to the anonymous referee
whose numerous suggestions have greatly improved the paper. The now
much shorter proofs of Proposition 16(a) and Corollary 23 are the referee’s.

2 The proof of Theorem 1

Like all previous deﬁnitions of Z in Q, we use elementary facts on quadratic
forms over R and Qp, together with Hasse’s Local-Global-Principle for quadratic
forms. What is new in our approach is the use of the Quadratic Reciprocity
Law (e.g., in Proposition 10 or 16) and, inspired by the model theory of
local ﬁelds, the transformation of some existential formulas into universal
formulas (Step 4). A technical key trick is the existential deﬁnition of the Ja-
cobson radical of certain rings (Step 3) which makes implicit use of so-called
‘rigid elements’ as they occur, e.g., in [K].

Step 1: Diophantine deﬁnition of quaternionic semi-local rings
`a la Poonen

The ﬁrst step modiﬁes Poonen’s proof ([P1]), thus arriving at a formula for
Z in Q which, like the formula in his Theorem 4.1, has 2 ∀’s followed by 7
∃’s, but we managed to bring down the degree of the polynomial involved
from 9244 to 8.

Deﬁnition 4. Let P be the set of rational primes and let Q∞ := R.
For a, b ∈ Q×, let
 3

• Ha,b := Q · 1 ⊕ Q · α ⊕ Q · β ⊕ Q · αβ be the quaternion algebra over Q
with multiplication deﬁned by α2 = a, β2 = b and αβ = −βα,

• ∆a,b := {p ∈ P ∪ {∞} | Ha,b ⊗ Qp ̸∼= M2(Qp)} the set of primes
(including ∞) where Ha,b does not split locally — ∆a,b is always ﬁnite,
and ∆a,b = ∅ iﬀ a ∈ N (b), i.e., a is in the image of the norm map
Q(
√
b) → Q,

• Sa,b := {2x1 ∈ Q | ∃x2, x3, x4 ∈ Q : x2
1 − ax2
2 − bx2
3 + abx2
4 = 1} the set
of traces of norm-1 elements of Ha,b, and

• Ta,b := Sa,b + Sa,b – note that Ta,b is an existentially deﬁned subset of
Q. Here we deviate from Poonen’s terminology: his Ta,b is Sa,b +Sa,b +
{0, 1, . . . , 2309}.

For each p ∈ P ∪ {∞}, we can similarly deﬁne Sa,b(Qp) and Ta,b(Qp) by
replacing Q by Qp.
For each p ∈ P, we will denote the p-adic valuation on Q or on Qp by vp,
and the assoicated residue map by φp : Z(p) → Fp resp. φp : Zp → Fp.
An explicit criterion for checking whether or not an element p ∈ P ∪ {∞}
belongs to ∆a,b, is given in the following

Observation 5. Assume a, b ∈ Q× and p ∈ P ∪ {∞}. Then p ∈ ∆a,b if and
only if

for p = 2: After multiplying by suitable rational squares and integers ≡ 1
mod 8 and, possibly, swapping a and b, the pair (a, b) is one of the
following:
 (2, 3) (3, 3) (5, 6) (6, 6) (15, 15)
(2, 5) (3, 10) (5, 10) (6, 15) (15, 30)
(2, 6) (3, 15) (5, 30) (10, 30) (30, 30)
(2, 10)

for 2 ̸= p ∈ P:

vp(a) is odd, vp(b) is even, and ( bp−vp(b)
p ) = −1, or

vp(a) is even, vp(b) is odd, and ( ap−vp(a)
p ) = −1 or

vp(a) is odd, vp(b) is odd, and ( −abp−vp(ab)
p ) = −1.

for p = ∞: a < 0 and b < 0.
 4

Proof: This is an immediate translation of the computation of the Hilbert
symbol (a, b)p (which is 1 or −1 depending on whether or not p ∈ ∆a,b) as
in Theorem 1 of Ch.III in [Se]:
For ﬁnite odd p and a = pαu and b = pβv (with u, v p-adic units) the formula
is
 (a, b)p = (−1)
αβǫ(p) ( u
p
 )β ( v
p
 )α ,

where ǫ(p) := p−1
2 mod 2.
For p = 2, the formula is

(a, b)2 = (−1)
ǫ(u)ǫ(v)+αω(v)+βω(u),

where ω(u) := u2−1
8 mod 2.
For p = ∞ the statement is obvious.

Proposition 6. For any a, b ∈ Q×,

Ta,b = ⋂

p∈∆a,b Z(p),

where Z(∞) := {x ∈ Q | −4 ≤ x ≤ 4}.

Here and throughout the rest of the paper, we use the following

Convention: Given an empty collection of subsets of Q, the intersection is
Q.
 Proof: For each p ∈ P, let

Up := {s ∈ Fp | x2 − sx + 1 is irreducible over Fp}

. We shall use the following

Facts For any a, b ∈ Q× and for any p ∈ P:

(a) If p ̸∈ ∆a,b then Sa,b(Qp) = Qp.

(b) If p ∈ ∆a,b then φ−1
p (Up) ⊆ Sa,b(Qp) ⊆ Zp.

(c) Sa,b(R) = { R for a > 0 or b > 0
[ − 2, 2] for a, b < 0.

(d) If p > 11 then Fp = Up + Up.

(e) Sa,b(Q) = Q ∩ ⋂
p∈∆a,b Sa,b(Qp).
 5

(a) and (b) are [P1], Lemma 2.1, (c) is a straightforward computation,
(d) is [P1], Lemma 2.3, and (e) is a special case of the Hasse-Minkowski
local-global principle for representing rationals by quadratic forms.
(b) and (c) immediately give the inclusion Ta,b ⊆ ⋂p∈∆a,b Z(p).
To prove the converse inclusion Ta,b ⊇ ⋂p∈∆a,b Z(p), let us ﬁrst compute
Up for the primes p ≤ 11:
 U2 = {1}
U3 = {0}
U5 = {1, 4}
U7 = {0, 3, 4}
U11 = {0, 1, 5, 6, 10}.

For each p ∈ P ∪ {∞} deﬁne Vp ⊆ Zp as follows:

Vp =
 



 φ
−1
2 (U2) ∪ (4 + 8Z2) for p = 2
φ−1
p (Up) ∪ [(±2 + pZp) \ (±2 + p2Zp)] for 3 ≤ p ≤ 11
φ−1
p (Up) for 11 < p ∈ P
[ − 2, 2] for p = ∞.

(We deﬁne Z∞ to be the real interval [−4, 4] ⊆ R.)
By Fact (b), Fact (c), Observation 5 together with an easy direct calculation
in the cases p = 3, 5, 7, 11 and, for p = 2, by the table below, one always has

Vp ⊆ Sa,b(Qp) and, for p ̸= ∞, Vp is open.

The table for p = 2 lists those pairs (a, b) with (a, b)2 = −1 as in Obser-
vation 5, and gives, in each case,

4 + 8Z2 ⊆ Sa,b(Q2)

by assuming that we are given x1 ∈ 2 + 8Z2 or x1 ∈ 6 + 8Z2 (which is
equivalent to 2x1 ∈ 4 + 8Z2) and by specifying elements x2, x3 and x4 which
guarantee that

−ax2
2 − bx2
3 + abx2
4 ≡2 1 − x2
1 ≡2 −3 mod 8Z2.

Multiplying x2
2, x2
3, x2
4 by a suitable common element from 1 + 8Z2 ⊆ (Q×
2 )2,

6

makes then sure that 2x1 ∈ Sa,b(Q2).

(a, b) x2 x3 x4
(2, 3) 0 1 0
(2, 5) 2 1 1
(2, 6) 0 1 1
2
(2, 10) 2 0 1
2
(3, 3) 1 0 0
(3, 10) 1 0 0
(3, 15) 1 0 0
(5, 6) 1 1 0
(5, 10) 1 0 1
(5, 30) 1 1 0
(6, 6) 1
2 1
2 0
(6, 15) 1 1 0
(10, 30) 0 1 1
10
(15, 15) 1 0 2
15
(15, 30) 1 1 1
15
(30, 30) 1 1 1
30

Fact (d) and another elementary case-by-case-check for p ≤ 11 shows
that for any p ∈ P ∪ {∞} Zp = Vp + Vp.

Now pick t ∈ ⋂p∈∆a,b Z(p). For each p ∈ ∆a,b, there is some sp ∈ Zp such
that sp, t − sp ∈ Vp.
If t = ±4 then, clearly, t = ±2 ± 2 ∈ Sa,b + Sa,b = Ta,b.
If t ̸= ±4 and ∞ ∈ ∆a,b we can choose s∞ ∈ Z∞ = [−4, 4] ⊆ R such that
s∞, t − s∞ ∈] − 2, 2[. Now approximate the ﬁnitely many sp ∈ Zp (p ∈ ∆a,b)
by a single s ∈ Q such that

s − sp ∈
 



 8Z2 if p = 2
p2Zp if 3 ≤ p ≤ 11
pZp if 11 < p ∈ P
] − ǫ, ǫ[ if p = ∞

where ǫ = min{| 2 ± s∞ |, | 2 ± (t − s∞) |}. This guarantees that for all
p ∈ ∆a,b s, t − s ∈ Vp ⊆ Sa,b(Qp),

and hence, by Fact (e), that s, t − s ∈ Sa,b = Sa,b(Q).

7

One then obtains an ∀∃-deﬁnition of Z in Q from the fact that

Z = ⋂

l∈P Z(l) = ⋂

a,b>0 Ta,b

as in [P1], Theorem 4.1. With our simpliﬁed Ta,b, the formula now becomes,
for any t ∈ Q,

t ∈ Z ⇐⇒
 ∀a, b ∃x1, x2, x3, x4, y2, y3, y4
(a + x2
1 + x2
2 + x2
3 + x2
4) · (b + x2
1 + x2
2 + x2
3 + x2
4)·
[(x2
1 − ax2
2 − bx2
3 + abx2
4 − 1)2+
+ ((t − 2x1)2 − 4ay2
2 − 4by2
3 + 4aby2
4 − 4)2] = 0

Step 2: Towards a uniform diophantine deﬁnition of all Z(p)’s
in Q

We will present a diophantine deﬁnition for the local rings Z(p) = Zp ∩ Q
depending on the congruence of the prime p modulo 8, and involving p (and
if p ≡ 1 mod 8 an auxiliary prime q) as a parameter. However, since in any
ﬁrst-order deﬁnition of a subset of Q we can only quantify over the elements
of Q, and not, e.g., over all primes, we will allow arbitrary non-zero rational
numbers p and q as parameters in the following deﬁnition.

Deﬁnition 7. For p, q ∈ Q×, let

• R[3]
p := T−1,−p + T2,−p

• R[5]
p := T−2,−p + T2,−p

• R[7]
p := T−1,−p + T−2,p

• R[1]
p,q := T−2p,q + T2p,q

Remark 8. (a) For any a, b, c, d ∈ Q× with at least one of them positive,

Ta,b + Tc,d = ⋂

l∈∆a,b Z(l) + ⋂

l∈∆c,d Z(l) = ⋂

l∈∆a,b∩∆c,d Z(l)

(b) The R’s are are existentially deﬁned, uniform in p and q, so that for
k = 3, 5 or 7 the sets

{(p, x) ∈ Q× × Q | x ∈ R[k]
p }

and the set {(p, q, x) ∈ Q× × Q×Q | x ∈ R[1]
p,q}

are diophantine.
 8

Proof: (a) The ﬁrst equation is from Proposition 6. For the second
equation, the inclusion ‘⊆’ is obvious. For ‘⊇’, assume x ∈ ⋂l∈∆a,b∩∆c,d Z(l).
By approximation, there is y ∈ Q such that

y ∈ { x + lZ(l) for l ∈ ∆c,d
Z(l) for l ∈ ∆a,b \ ∆c,d

Then y ∈ ⋂l∈∆a,b Z(l) and x − y ∈ ⋂l∈∆c,d Z(l), so that x = y + (x − y) ∈
⋂l∈∆a,b Z(l) + ⋂
l∈∆c,d Z(l).

(b) This is immediate from deﬁnitions 4 and 7.

Deﬁnition 9. (a) For k = 1, 3, 5 or 7, deﬁne P[k] := {l ∈ P | l ≡ k
mod 8}

(b) For p ∈ Q×, deﬁne

• P(p) := {l ∈ P | vl(p) is odd}

• P[k](p) := P(p) ∩ P[k], where k = 1, 3, 5 or 7.

Proposition 10. (a) Z(2) = T3,3 + T2,5

(b) Suppose that k = 3, 5 or 7. Then, for p ∈ Q×,

R[k]
p =
 { ⋂l∈P[k](p) Z(l) if p ≡ k ( mod 8Z(2))
⋂l∈P[k](p) Z(l) or ⋂l∈P[k](p)∪{2} Z(l) otherwise

(As before, ⋂l∈∅ Z(l) = Q.)

In particular, if p is a prime and p ≡ k mod 8 then Z(p) = R[k]
p .

(c) For p, q ∈ Q× with p ≡ 1 ( mod 8Z(2)) and q ≡ 3 ( mod 8Z(2)),

R[1]
p,q = ⋂

l∈P(p,q) Z(l)

where P(p, q) := ∆−2p,q ∩ ∆2p,q.

In particular, if p is a prime ≡ 1 mod 8 and q is a prime ≡ 3 mod 8

with ( p
q
 ) = −1 then Z(p) = R[1]
p,q.

Proof: (a) By Observation 5, ∆3,3 = {2, 3} and ∆2,5 = {2, 5}, hence, by
Remark 8(a), T3,3 + T2,5 = ⋂

l∈∆3,3∩∆2,5 Z(l) = Z(2).

9

(b) First assume p ∈ Q× with p ≡ 3 ( mod 8Z(2)). Then, by Observation 5,

∆−1,−p ∩ P = P[3](p) ∪ P[7](p)
∆2,−p = P[3](p) ∪ P[5](p) ∪ {2},

so ∆−1,−p ∩ ∆2,−p = P[3](p), and, by Remark 8(a),

R[3]
p := T−1,−p + T2,−p = ⋂

l∈∆−1,−p∩∆2,−p Z(l) = ⋂

l∈P[3](p) Z(l).

If p ̸≡ 3 ( mod 8Z(2)), the only possible additional prime is 2 (e.g. if p ≡ 5 (
mod 8Z(2))).
If p ≡ 5 ( mod 8Z(2)) then, again by Observation 5,

∆−2,−p ∩ P = P[5](p) ∪ P[7](p)
∆2,−p = P[3](p) ∪ P[5](p) ∪ {2},

so ∆−2,−p ∩ ∆2,−p = P[5](p), and

R[5]
p := T−2p,−p + T2p,−p = ⋂

l∈∆−2,−p∩∆2,−p Z(l) = ⋂

l∈P[5](p) Z(l).

Again, the prime 2 (and no other prime) may or may not enter if p ̸≡ 5 (
mod 8Z(2)).
Finally, if p ≡ 7 ( mod 8Z(2)) then, again by Observation 5,

∆−1,−p ∩ P = P[3](p) ∪ P[7](p)
∆−2,p ∩ P = P[5](p) ∪ P[7](p) ∪ {2},

so ∆−1,−p ∩ ∆−2,p = P[7](p), and

R[7]
p := T−p,−p + T2p,p = ⋂

l∈∆−1,−p∩∆−2,p Z(l) = ⋂

l∈P[7](p) Z(l).

As before, 2 may enter if p ̸≡ 7 ( mod 8Z(2)).
(c) The ﬁrst statement is immediate from Remark 8(a). For the ‘in
particular’, assume p and q are primes with p ≡ 1 mod 8, q ≡ 3 mod 8
and ( p
q ) = −1. Then, by quadratic reciprocity, ( q
p ) = −1, and so, from

Observation 5, ∆−2p,q = {p} and ∆2p,q = {p, q}. Hence R[1]
p,q = Z(p).

10

Corollary 11.
 Z = Z(2) ∩ ⋂

p,q∈Q×(R[3]
p ∩ R[5]
p ∩ R[7]
p ∩ R[1]
p,q)

Proof: By Remark 8(a), all R’s on the right hand side are semilocal
subrings of Q containing Z. On the other hand, by the ‘in particular’ parts
of the proposition, for each prime p, the right hand side is contained in Z(p);
note that for p ≡ 1 mod 8 one always ﬁnds a prime q ≡ 3 mod 8 such that
q is congruent to a non-square mod p.

Step 3: An existential deﬁnition for the Jacobson radical

We will show that, for some rings R occuring in Proposition 10, the Jacobson
radical J(R) can be deﬁned by an existential formula. This will also give
rise to new diophantine predicates in Q.

Deﬁnition 12. For a, b, c ∈ Q× we deﬁne

• T ×
a,b := {u ∈ Ta,b | ∃v ∈ Ta,b with uv = 1}

• I c
a,b := c · Q2 · T ×
a,b ∩ (1 − Q2 · T ×
a,b)

• Ja,b := (I a
a,b + I a
a,b) ∩ (I b
a,b + I b
a,b)

Note that the set {(a, b, x) ∈ Q× × Q× × Q | x ∈ Ja,b} is diophantine.

Lemma 13. Assume a, b, c ∈ Q×. Then

(a) T ×
a,b =
 { ⋂l∈∆a,b Z×
(l) if ∞ ̸∈ ∆a,b
([−4, − 1
4 ] ∪ [ 1
4 , 4]) ∩ ⋂l∈∆a,b\{∞} Z×
(l) if ∞ ∈ ∆a,b

(b) I c
a,b = {0}∪{y ∈ Q× vl(y)is odd and positive for all l ∈ ∆a,b ∩ P(c) and
vl(y), vl(1 − y)are even for all l ∈ ∆a,b \ (P(c) ∪ {∞})
 }
3

(c) I c
a,b + I c
a,b = ⋂
l∈∆a,b∩P(c) l Z(l),

(d) Ja,b = ⋂
l∈∆ lZ(l), where ∆ = { ∆a,b \ {2, ∞} if 2 ∈ ∆a,b and v2(a), v2(b) are even
∆a,b \ {∞} else

3Here we adopt the convention that ∞ is even (to include the case that y = 1 which
can only happen when ∆a,b ∩ P(c) = ∅, a case that will never be used later).

11

In particular, if ∞ ̸∈ ∆a,b then T ×
a,b is the group of units of the ring Ta,b and,
if also 2 ̸∈ ∆a,b or at least one of v2(a), v2(b) is odd, Ja,b is the Jacobson
radical of Ta,b.

Proof: (a) This is an immediate consequence of Proposition 6.
(b) ‘⊆’: By weak approximation,

Q2 · T ×
a,b = {0} ∪ ⋂

l∈∆a,b\{∞} v−1
l (2Z).

So if y ∈ I c
a,b \ {0} and l ∈ ∆a,b ∩ P(c) then vl(y) is odd. On the other hand,
1 − y ∈ Q2 · T ×
a,b, so vl(1 − y) is even. By the ultrametric inequality, this is
only possible when vl(y) > 0. If, on the other hand, l ∈ ∆a,b \ (P(c) ∪ {∞})
then vl(y) and vl(1 − y) are even.
‘⊇’: Clearly, 0 ∈ I c
a,b. Now assume y ∈ Q× such that, for all l ∈ ∆a,b ∩ P(c),
vl(y) is positive and odd. Then c−1y ∈ ⋂l∈∆a,b∩P(c) v−1
l (2Z) and 1 − y ∈
⋂l∈∆a,b∩P(c) Z×
(l) ⊆ ⋂l∈∆a,b∩P(c) v−1
l (2Z).
If we assume that vl(y) and vl(1 − y) are even for all l ∈ ∆′ := ∆a,b \
(P(c) ∪ {∞}) then both c−1y and 1 − y lie in ⋂l∈∆′ v−1
l (2Z).
So with both assumptions we see that both c−1y and 1 − y lie in
⋂

l∈∆a,b\{∞} v−1
l (2Z) ⊆ Q2 · T ×
a,b

. (c) For any prime l, any x ∈ Q with vl(x) > 0 can be written as the
sum of two elements of odd positive value. And any x ∈ Q can be written
as the sum of two elements y1 and y2 such that vl(yi) and vl(1 − yi) are
both even for both i = 1, 2: choose y1 of even value < min{0, vl(x)} and let
y2 = x − y1; then vl(1 − y1) = vl(y1) = vl(y2) = vl(1 − y2). Hence the claim
follows by approximation.
(d) By deﬁnition, Ja,b = (I a
a,b + I a
a,b) ∩ (I b
a,b + I b
a,b), so, from (c),

Ja,b = ⋂

l∈∆a,b∩P(a) lZ(l) ∩ ⋂

l∈∆a,b∩P(b) lZ(l) = ⋂

l∈∆a,b∩(P(a)∪P(b)) lZ(l),

where the second equality is, again, by weak approximation. But now, from
Observation 5,

∆a,b∩(P(a)∪P(b)) = { ∆a,b \ {2, ∞} if 2 ∈ ∆a,b and v2(a), v2(b) are even
∆a,b \ {∞} else

12

Before we give the existential deﬁnition of the Jacobson radical J(R)
for some of the rings R deﬁned in Step 2 (Corollary 15 and Proposition 16
below) we require another easy Lemma:

Lemma 14. Let a, b, c, d ∈ Q×, at least one of which positive and at least one
of which with odd dyadic value. Let ∆ := ∆a,b ∩ ∆c,d and let R = ⋂l∈∆ Z(l).
Then Ja,b + Jc,d = ⋂

l∈∆ lZ(l).

In particular, if ∆ ̸= ∅ then Ja,b + Jc,d is the Jacobson radical J(R) of the
semilocal ring R.

Proof: Let ∆′
a,b := { ∆a,b \ {2, ∞} if 2 ∈ ∆a,b and v2(a), v2(b) are even
∆a,b \ {∞} else ,

and similarly ∆′
c,d. Then, by Lemma 13(d) (for the ﬁrst equality) and by
weak approximation (for the second),

Ja,b + Jc,d = ⋂

l∈∆′
a,b
 lZ(l) + ⋂

l∈∆′
c,d
 lZ(l) = ⋂

l∈∆′
a,b∩∆′
c,d
 lZ(l).

By our assumption on a, b, c, d, however, ∆a,b ∩ ∆c,d = ∆′
a,b ∩ ∆′
c,d, which
proves the ﬁrst claim.
The ‘in particular’ follows immediately.
Now let us ﬁrst turn to the rings R[k]
p for k = 3, 5 and 7 deﬁned in
Deﬁnition 7 and recall that

R[k]
p =
 



 T−1,−p + T2,−p if k = 3
T−2,−p + T2,−p if k = 5
T−1,−p + T−2,p if k = 7

Corollary 15. Deﬁne for k = 1, 3, 5 and 7,

Φk := {p ∈ Q>0 | p ≡ k ( mod 8Z(2)) and P(p) ⊆ P[1] ∪ P[k]}
Ψ := {(p, q) ∈ Φ1 × Φ3 | p ∈ 2 · (Q×)2 · (1 + J(R[3]
q ))}.

(a) Then Φk is diophantine in Q.

(b) If k = 3, 5 or 7 and if p ∈ Φk then P[k](p) ̸= ∅ and

{0} ̸= J(R[k]
p ) =
 



 J−1,−p + J2,−p if k = 3
J−2,−p + J2,−p if k = 5
J−1,−p + J−2,p if k = 7

13

In particular, in each of the cases, the Jacobson radical is diophantine
in Q, by a formula that is uniform in p.

(c) Ψ is diophantine in Q.

Proof: (a) It is clear that ‘p > 0’ is diophantine. It is also clear
from Proposition 10(a) that, for k = 1, 3, 5 and 7, the property ‘p ≡ k (
mod 8Z(2))’ is diophantine.
Moreover, if v2(p) is even and k′ = 3, 5 or 7, then, by Proposition 10(b),

P[k′](p) = ∅ ⇐⇒ p ∈ (Q×)
2 · (R[k′]
p )
×

(Note that we are not assuming that p ≡ k′ ( mod 8Z(2).) So the property
on the left is diophantine. But then so are

Φ1 = {p ≡ 1 ( mod 8Z(2)) | P3(p) = ∅, P5(p) = ∅ and P7(p) = ∅}
Φ3 = {p ≡ 3 ( mod 8Z(2)) | P5(p) = ∅ and P7(p) = ∅}
Φ5 = {p ≡ 5 ( mod 8Z(2)) | P3(p) = ∅ and P7(p) = ∅}
Φ7 = {p ≡ 7 ( mod 8Z(2)) | P3(p) = ∅ and P5(p) = ∅}.

(b) Assume k = 3, 5 or 7 and that p ∈ Φk. Then p ≡ k ( mod 8Z(2)) and so,

by Proposition 10(b), R[k]
p = ⋂l∈P[k](p) Z(l). As p > 0 and p ≡ k ( mod 8Z(2)),

P[k](p) ̸= ∅ and hence J(R[k]
p ) = ⋂
l∈P[k](p) lZ(l) ̸= {0}. The explicit formulas
now follow from Lemma 14, as the assumptions of the Lemma are satisﬁed
in each case. (c) follows directly from (a) and (b).

The most diﬃcult case is when p ∈ Φ1. Recall from Deﬁnition 7 and from
Proposition 10(c) that, for p, q ∈ Q×, we have deﬁned R[1]
p,q := T−2p,q + T2p,q
and P(p, q) := ∆−2p,q ∩ ∆2p,q.

Proposition 16. (a) If (p, q) ∈ Ψ, then P(p, q) ̸= ∅.

(b) If (p, q) ∈ Ψ, then J(R[1]
p,q) = J−2p,q + J2p,q.

(c) The set {(p, q, x) ∈ Q3 | (p, q) ∈ Ψ and x ∈ J(R[1]
p,q)} is diophantine.

Proof: (a) Assume (p, q) ∈ Ψ. Multiplying p or q by nonzero rational
squares does not change R[1]
p,q or J−2p,q or J2p,q, so we can assume that p
and q are squarefree positive integers. Since p ≡ 1 ( mod 8Z(2)) and q ≡ 3 (
mod 8Z(2), we have, by Observation 5, (2p, q)2 = −1. By Hilbert reciprocity,
there must also be an odd prime l such that (2p, q)l = −1. By deﬁnition
of Ψ and, again, by Observation 5, this implies that l ∈ {1, 3} + 8Z(2) and

14

l ̸∈ P[3](q). These two conditions imply (−1, q)l = 1. Multiplying yields
(−2p, q)l = −1. Thus l ∈ P(p, q).
(b) is immediate from (a) and Lemma 14.
(c) follows from Corollary 15(c), from (b) and the note preceding Lemma
13.

Step 4: From existential to universal

Let R be a semilocal subring of Q, i.e., R = ⋂
l∈∆ Z(l) for some ﬁnite ∆ ⊆ P.
Deﬁne ̃R := {x ∈ Q | ¬∃y ∈ J(R) with x · y = 1}.

Lemma 17. (a) If J(R) is diophantine in Q then ̃R is deﬁned by a uni-
versal formula in Q.

(b) ̃R = ⋃
l∈∆ Z(l), provided ∆ ̸= ∅, i.e., provided R ̸= Q.

(c) In particular, if R = Z(p) for some p ∈ P then ̃R = R.

Proof: (a) is obvious from the deﬁnition of ̃R, and (c) is a special case
of (b). So we only need to prove (b).
For the inclusion ‘⊆’, pick x ∈ ̃R and assume that x ̸∈ ⋃
l∈∆ Z(l). Then
for all l ∈ ∆, vl(x) < 0, and hence y := x−1 ∈ ⋂l∈∆ l Z(l) = J(R), contra-
dicting our assumption that x ∈ ̃R.
For the converse inclusion ‘⊇’, assume x ∈ Z(l) for some l ∈ ∆. Then,
for any y ∈ J(R), x · y ∈ l Z(l), so, in particular x · y ̸= 1.

Now we can give our universal deﬁnition of Z in Q:

Proposition 18. (a)

Z = ˜Z(2) ∩
 

 ⋂

k=3,5,7
 ⋂

p∈Φk
 ˜
R[k]
p
 

 ∩ ⋂

(p,q)∈Ψ
 ˜
R[1]
p,q,

where Φk and Ψ are the diophantine sets deﬁned in Corollary 15.

(b) for any t ∈ Q,

t ∈ Z ⇐⇒ t ∈ ˜Z(2)∧

∀p ⋀
k=3,5,7(t ∈ ˜
R[k]
p ∨ p ̸∈ Φk)∧

∀p, q(t ∈ ˜
R[1]
p,q ∨ (p, q) ̸∈ Ψ)

15

(c) (Theorem 1) There is a natural number n and a polynomial g ∈
Z[t; x1, . . . , xn] such that, for any t ∈ Q,

t ∈ Z iﬀ ∀x1 . . . ∀xn ∈ Q g(t; x1, . . . , xn) ̸= 0.

Proof: (a) The equation is valid by Proposition 10 and Lemma 17(b),
(c).(b) This is a reformulation of (a) revealing that the formula thus obtained
for Z in Q is universal: the ̃R’s are universal by Corollary 15, Proposition
16 and Lemma 17(a); Φk and Ψ are existential by Corollary 15(a) and (c),
so their negation is universal as well.
(c) This is immediate from (b).

3 More diophantine predicates in Q

From the results and techniques of section 2, one obtains new diophantine
predicates in Q. They are of interest in their own right, but maybe they
can also be used to show that Hilbert’s 10th problem over Q cannot be
solved, not by deﬁning or interpreting Z in Q, but, e.g., by assigning graphs
to the various ﬁnite sets of primes encoded in these predicates, and using
graph theoretic undecidability results. We will also use some of these new
predicates for our ∀∃-deﬁnition of Z in Q which uses just one universal
quantiﬁer (Corollary 21).
Before listing the new diophantine predicates we shall ﬁrst prove the
following

Lemma 19. Assume p ∈ Φ1 and deﬁne4

R[1]
p := {x ∈ Q | ∃q with (p, q) ∈ Ψ, q ∈ (R[1]
p,q)
× and x ∈ R[1]
p,q}.

Then R[1]
p is diophantine in Q and R[1]
p = ⋃l∈P(p) Z(l) (which is ∅ if P(p) = ∅,
i.e., if p ∈ Q2).
In particular, if p is a prime ≡ 1 mod 8 then R[1]
p = Z(p).

Proof: That R[1]
p is diophantine in Q is immediate from Corollary 15.
Assuming (p, q) ∈ Ψ, the condition ‘q ∈ (R[1]
p,q)×’ implies that, in the
terminology of Proposition 10(c), P(p, q) ⊆ P(p): Suppose q ∈ (R[1]
p,q)× and

4We hope the notation R[1]
p is not too confusing as the deﬁnition is diﬀerent from that
of R[k]
p for k = 3, 5 or 7. The crucial property, however, the ‘in particualr’, gives the same
result as in Corollary 10(b).
 16

l ∈ P(p, q). Then vl(q) = 0, so l ̸∈ P(q). Hence, by the deﬁnition of P(p, q),
l ∈ P(p) (note that, by Observation 5, 2 ̸∈ P(p, q), as (p, q) ∈ Φ1 × Φ3).
This yields the last inclusion in

R[1]
p = ⋃

q ∈ (R[1]
p,q)×with
(p, q) ∈ Ψ
 R[1]
p,q = ⋃

q ∈ (R[1]
p,q)×with
(p, q) ∈ Ψ
 ⋂

l∈P(p,q) Z(l) ⊆ ⋃

l∈P(p) Z(l).

The ﬁrst equality is by deﬁnition, the second by Proposition 10(c) using
that, from Proposition 16(a), P(p, q) ̸= ∅.
Conversely, suppose l ∈ P(p) and x ∈ Z(l). Choose a prime q ≡ 3 mod 8

with ( l
q
 ) = −1 and with ( l′

q
 ) = 1 for each l′ ∈ P(p) \ {l}.

Then ( pq−vq(p)

q
 ) = −1, so (p, q) ∈ Ψ: note that vq(p) is even since

p ∈ Φ1, so φq(pq−vq(p)) is a non-square in Fq, i.e., ∈ 2 · (F×
q )2; hence p ∈
2 · (Q×)2(1 + qZ(q)).
Therefore, by Proposition 10(c) and the Quadratic Reciprocity Law,

P(p, q) = {l}: Clearly l ∈ P(p, q) as l ∈ P(p) and ( q
l
 ) = ( l
q
 ) = −1

(p ∈ Φ1, so l ≡ 1 mod 8); and for any l′ ∈ P(p) \ {l}, ( l′

q
 ) = ( q
l′
 ) = 1,

so l′ ̸∈ P(p, q); ﬁnally P(q) = {q}, but ( 2pq−vq(2p)

q
 ) = 1, hence q ̸∈ P(p, q).

Thus x ∈ Z(l) = R[1]
p,q and q ∈ (R[1]
p,q)×.

Proposition 20. For x, y ∈ Q×, the following properties are diophantine:

(a) for ﬁxed k ∈ {3, 5, 7}, the property that x, y ∈ Φk and P[k](x)∩P[k](y) =
∅

(b) x ̸∈ Q2

(c) for ﬁxed k ∈ {1, 3, 5, 7}, the property that x ≡ k ( mod 8Z(2)) and
x ̸∈ Φk

(d) for ﬁxed k ∈ {3, 5, 7}, the property that P[k](x) = ∅

(e) x ̸∈ N (y), where N (y) is the image of the norm Q(
√y) → Q

17

Proof: (a) By Corollary 15(a), Φk is diophantine. By Corollary 15(b), for
any x ∈ Φk, P[k](x) ̸= ∅ and hence J(R[k]
x ) is diophantine. Now let x, y ∈ Φk
and recall that, by Proposition 10, R[k]
x = ⋂
l∈P[k](x) Z(l), and likewise for

R[k]
y . So we have the equivalence

P[k](x) ∩ P[k](y) = ∅ ⇐⇒ 1 ∈ J(R[k]
x ) + J(R[k]
y )

which then proves (a).

(b) The property that ‘v2(x) is odd’ is diophantine: v2(x) is odd if and
only if x = 2yz2 for some y ∈ Z×
(2) and some z ∈ Q×. As the property
‘x < 0’ is diophantine as well, by Corollary 15(a) and (b), it suﬃces to show

x ̸∈ Q2 ⇐⇒
 { x < 0 or v2(x) is odd or
∃p ∈ Φ3 with x ∈ 2 · (Q×)2 · (1 + J(R[3]
p ))

‘⇒’: Assume that x ̸∈ Q2, that x > 0 and that v2(x) is even. Multiplying
x by a nonzero rational square does not change the truth of either side of
the implication, so we may assume that x = p1 · · · pr for distinct odd primes
p1, . . . , pr where r ≥ 1.

Choose a1 ∈ Z with ( a1
p1
 ) = { −1 if p1 ≡ 1 mod 4
1 if p1 ≡ 3 mod 4

and, for i > 1,

choose ai ∈ Z with ( ai
pi
 ) = { 1 if pi ≡ 1 mod 4
−1 if pi ≡ 3 mod 4

Finally, choose a prime p ≡ 3 mod 8 with p ≡ ai mod pi (i = 1, . . . , r).

Then, by the Quadratic Reciprocity Law, ( x
p
 ) = −1.

Clearly, p ∈ Φ3. By Lemma 10(b), R[3]
p = Z(p). Hence x ∈ 2 · (Q×)2 ·

(1 + J(R[3]
p )), as ( 2
p
 ) = −1.

‘⇐’: If x < 0 or v2(x) is odd then clearly x ̸∈ Q2.
If x ∈ 2 · (Q×)2 · (1 + J(R[3]
p )) for some p ∈ Φ3 then P[3](p) ̸= ∅, and for

any l ∈ P[3](p) one has that vl(x) is even and ( xl−vl(x)

l
 ) = ( 2
l
 ) = −1.

Hence x ̸∈ Q2.
 18

(c) By Proposition 10(a), x ≡ k ( mod 8Z(2)) is diophantine. First
assume x ≡ 1 ( mod 8Z(2)). Then x ̸∈ Φ1 if and only if x ≤ 0 or x > 0 and,
for some k ∈ {3, 5, 7}, P[k](x) ̸= ∅.
This last condition can be expressed diophantinely by distinguishing the
cases whether the number of k ∈ {3, 5, 7} with P[k](x) ̸= ∅ is 1, 2 or 3.
If it is 1, say P[k](x) ̸= ∅, then ♯P[k](x) must be even (in order to get
x ≡ 1 ( mod 8Z(2))), so we can choose p ∈ P[k](x) and let

yk := pvp(x) and y′
k := ∏

l∈P[1](x) lvl(x) · ∏

l∈P[k](x)\{p} lvl(x).

Then yk, y′
k ∈ Φk, P[k](yk) ∩ P[k](y′
k) = ∅ and x = yk · y′
k. By (a), the
condition that there exist such yk, y′
k is diophantine, and, when satisﬁed, it
implies x ̸∈ Φ1.
If {k ∈ {3, 5, 7} | P[k](x) ̸= ∅} = {k1, k2} for distinct k1, k2 then both
♯P[k1](x) and ♯P[k2](x) must be even, again, and so one constructs similarly
y1, y′
1 ∈ Φk1 and y2, y′
2 ∈ Φk2 with P[ki](yi) ∩ P[ki](y′
i) = ∅ for i = 1, 2 such
that x = y1 · y′
1 · y2 · y′
2.
If P[k](x) ̸= ∅ for all three k ∈ {3, 5, 7} then either all three sets have an
even number of elements or all three have an odd number of elements, and
in either case it is clear how to proceed along the same lines.
Now assume x ≡ 3 ( mod 8Z(2)). Then x ̸∈ Φ3 if and only if x ≤ 0 or x >
0 and P[5](x) ̸= ∅ or P[7](x) ̸= ∅. Here the last condition is diophantine again,
distinguishing the cases whether the number of k ∈ {5, 7} with P[k](x) ̸= ∅
is 1 or 2 etc.
It is clear how similar existential formulas can be written down for ‘x ̸∈
Φ5’ and ‘x ̸∈ Φ7’.

(d) P[3](x) = ∅ if and only if, modulo a nonzero rational square factor,
x or −x or 2x or −2x is a product of primes in ⋃
k=1,5,7 P[k]. Note that for
a ﬁxed k ∈ {1, 5, 7}, each product of primes in P[k] can be expressed as a
product of one or two factors of elements in Φk. Hence P[3](x) = ∅ if and
only if
 ∃y1, . . . , y8, z
(y1, y2 ∈ Φ1 ∧ y3, y4 ∈ Φ5 ∧ y5, y6 ∈ Φ7 ∧ y7 = −1 ∧ y8 = 2

∧ ⋁
I⊆{1,...,8} x = z2 ∏
i∈I yi)

And, again, similar formulas hold for k = 5 and k = 7.

19

(e) x ̸∈ N (y) iﬀ

(x < 0 ∧ y < 0)
∨ ⋁
k=3,5,7 ∃p ∈ Φk with((
x ∈ p · (Q×)2 · (R[k]
p )×) ∧ (
y or − xy ∈ ak · (Q×)2 · (1 + J(R[k]
p ))
)

∨ (
y ∈ p · (Q×)2 · (R[k]
p )×) ∧ (x or − xy ∈ ak · (Q×)2 · (1 + J(R[k]
p ))
))

∨∃(p, q) ∈ Ψ with q ∈ (R[1]
p,q)× and((
x ∈ p · (Q×)2 · (R[1]
p,q)×) ∧ (
y or − xy ∈ q · (Q×)2 · (1 + J(R[1]
p,q))
)

∨ (
y ∈ p · (Q×)2 · (R[1]
p,q)×) ∧ (
x or − xy ∈ q · (Q×)2 · (1 + J(R[1]
p,q))
))

where a3 = a5 = 2 and a7 = −1.
This uses Observation 5(b) and (c), Corollary 15(b) and (c), the previous
parts and the local-global principle for norms.
The ﬁrst line says that x ̸∈ N (y) over R.
Lines 2-4 say that x ̸∈ N (y) over Ql for some non-empty set of primes
l ≡ 3, 5 or 7 mod 8: Fix k ∈ {3, 5, 7}. By Corollary 15(b), p ∈ Φk implies
that P[k](p) ̸= ∅. We claim that

(x, y)l = −1 for some l ∈ P[k] ⇐⇒ ∃p ∈ Φk with (. . .) ,

where (. . .) is the bracket is line 3 and 4.
‘⇒’: Assume l ∈ P[k] with (x, y)l = −1. Let p = l. Then R[k]
p = Zl and
‘(. . .)’ says that vl(x) is odd and yl−vl(y) or −xyl−vl(xy) is a quadratic non-
residue mod l or the same with x and y swapped. By Observation 5, this
is equivalent to (x, y)l = −1, so it holds by our assumption.
‘⇐’: Suppose p ∈ Φk satisﬁes ‘(. . .)’. Then P[k](p) ̸= ∅ and, for any l ∈
P[k](p), vl(x) is odd and, by the choice of ak, either yl−vl(y) or −xyl−vl(xy)

is a quadratic non-residues mod l or the same with x and y swapped, so
(x, y)l = −1.
Lines 5-7 say that x ̸∈ N (y) over Ql for some non-empty set of primes
l ≡ 1 mod 8. As in the proof of Lemma 19, the condition ‘q ∈ (R[1]
p,q)×’
makes sure that, in the terminology of Proposition 10(c), P(p, q) ∩ P(q) = ∅,
so P(p, q) ⊆ P(p). And, by Proposition 16(a), P(p, q) ̸= ∅. Line 6 and 7
then say that x ̸∈ N (y) over Ql for any l ∈ P(p, q). Note that the role of
ak in lines 3 and 4 of being a quadratic non-residue mod l for all l ∈ P[k]

is here taken by q which is a quadratic non-residue for all l ∈ P[1](p) with
(p, q) ∈ Ψ.
We could disregard the prime p = 2, as ‘x ̸∈ N (y)’ either happens
nowhere locally, or at least at two primes in P ∪ {∞}.

20

The result in (b) was also obtained in [P2] – using a deep result on
Chˆatelet surfaces from [CSS] – our proof is elementary.
Let us also mention that (b) follows from (e): x ̸∈ Q2 ⇔ ∃y x ̸∈ N (y)
(and we did not use (b) in order to prove (e)).

We close this section by showing that there is an ∀∃-deﬁnition of Z in Q
with just one universal quantiﬁer:

Corollary 21. For all t ∈ Q, t ∈ Z if and only if

∀p
 


t ∈ Z(2) ∧
 



 (
p ∈ Q2 · (2 + 4Z(2))
)

∨ ⋁
k=1,3,5,7
 { (p ̸= 0 ∧ p ∈ Q2 · (k + 8Z(2))
)

∧ (
(p ̸∈ Φk) ∨ p ∈ Q2 ∨ (
p ∈ Φk \ Q2 ∧ t ∈ R[k]
p ))
 




Proof: The equivalence holds by Proposition 10(a) and (b) and by
Lemma 19.
That the resulting formula is of the shape ∀∃ with just one universal
quantiﬁer ‘∀p’ follows from Proposition 10, Corollary 15, Lemma 19 and
Proposition 20. Note that, under the assumption ‘p ∈ Q2 · (k + 8Z(2))’, the
property ‘p ̸∈ Φk’ is equivalent to ‘p ̸∈ Z×
(2) or (p ∈ k + Z(2) and p ̸∈ Φk)’
which is diophantine by Proposition 20(c). And ‘p ̸∈ Q2’ is diophantine by
20(b).

4 Why Z should not be diophantine in Q

In this section we show that Z is not diophantine in Q, provided one believes
in a certain version of what one may (arguably) call ‘the Bombieri-Lang
Conjecture’ on varieties with many rational points.
The version of this conjecture in the special case of varieties over Q on
which our result is based is the following (mainly after section F.5.2 of [HS]):

Bombieri-Lang Conjecture Let V be an absolutely irreducible aﬃne or
projective positive-dimensional variety over Q such that V (Q) is Zariski
dense in V . Then so is ⋃

φ:A 99KV φ(A(Q)),

where the φ : A 99K V run through all non-constant Q-rational maps from
positive-dimensional abelian varieties A deﬁned over Q to V .

21

Lemma 22. Assume the Bombieri-Lang Conjecture as above. Let f ∈
Q[x1, . . . , xn+1] \ Q[x1, . . . , xn] be absolutely irreducible and let Let V =
V (f ) ⊆ An+1 be the aﬃne hypersurface deﬁned over Q by f . Assume that
V (Q) is Zariski dense in V . Let π : An+1 → A1 be the projection onto the
ﬁrst coordinate. Then V (Q) ∩ π−1(Q \ Z) is also Zariski dense in V .

(For n = 1 the Lemma holds unconditionally, by Siegel’s Theorem.)

Proof: Choose any g ∈ Q[x1, . . . , xn]\{0}. By the Bombieri-Lang Conjecture
there are an abelian variety A and a rational map φ : A 99K V , both deﬁned
over Q, such that φ(A(Q)) \ V (g)(Q) is inﬁnite (considering V (g) as subset
of An+1). By possibly composing φ with another rational map (from the
left), we may assume that π(φ(A(Q)) \ V (g)(Q)) is inﬁnite, and that the
pole divisor D of π ◦ φ is ample. By Corollary 6.2 in [F], there are only
ﬁnitely many P ∈ A(Q) \ D(Q) with π(φ(P )) ∈ Z (cf. the remarks following
Theorem 1 in [Si]). This implies that (V (Q) \ V (g)(Q)) ∩ π−1(Q \ Z) ̸= ∅.
Since g was arbitrary this shows that V (Q) ∩ π−1(Q \ Z) is Zariski dense in
V .

Corollary 23. Assume the Bombieri-Lang Conjecture as stated above. Then
there is no inﬁnite subset of Z existentially deﬁnable in Q. In particular, Z
is not diophantine in Q.

Proof: If Z contains an inﬁnite subset that is diophantine over Q then
there is a hypersurface W in An+1 such that π(W (Q)) is inﬁnite (where
π is as in Lemma 22). Replace W by the Zariski closure W of W (Q); this
ensures that the irreducible components V of W are geometrically irreducible
(given by absolutely irreducible polynomials). For at least one such V the
set π(V (Q)) is inﬁnite (and still contained in Z: note that W (Q) = W (Q)).
This contradicts Lemma 22.

Let us conclude with a collection of closure properties for pairs of models
of Th(Q) (in the ring language), one a substructure of the other, which might
have a bearing on the ﬁnal (unconditional) answer to the question whether
or not Z is diophantine in Q.

Proposition 24. Let Q⋆, Q⋆⋆ be models of Th(Q) (i.e. elementary exten-
sions of Q) with Q⋆ ⊆ Q⋆⋆, and let Z⋆ and Z⋆⋆ be their rings of integers.
Then

(a) Z⋆⋆ ∩ Q⋆ ⊆ Z⋆.

(b) Z⋆⋆ ∩ Q⋆ is integrally closed in Q⋆.

22

(c) (Q⋆⋆)2 ∩ Q⋆ = (Q⋆)2, i.e. Q⋆ is quadratically closed in Q⋆⋆.

(d) If Z is diophantine in Q then Z⋆⋆ ∩ Q⋆ = Z⋆ and Q⋆ is algebraically
closed in Q⋆⋆.

(e) Q is not model complete, i.e., there are Q⋆ and Q⋆⋆ such that Q⋆ is
not existentially closed in Q⋆⋆.

Proof: (a) is an immediate consequence of our universal deﬁnition of Z in
Q. The very same deﬁnition holds for Z⋆ in Q⋆ and for Z⋆⋆ in Q⋆⋆ (it is part
of Th(Q) that all deﬁnitions of Z in Q are equivalent). So if this universal
formula holds for x ∈ Z⋆⋆ ∩ Q⋆ in Q⋆⋆ it also holds in Q⋆, i.e. x ∈ Z⋆.
(b) is true because Z⋆⋆ is integrally closed in Q⋆⋆.
(c) follows from the fact that both being a square and, by Proposition
20(b), not being a square are diophantine in Q.
(d) If Z is diophantine in Q then Z⋆⋆ ∩Q⋆ ⊇ Z⋆ and hence equality holds,
by (a).
To show that then also Q⋆ is algebraically closed in Q⋆⋆, let us observe
that, for each n ∈ N,

An := {(a0, . . . , an−1) ∈ Zn | ∃x ∈ Z with xn + an−1xn−1 + . . . + a0 = 0}

is decidable: zeros of polynomials in one variable are bounded in terms of
their coeﬃcients, so one only has to check ﬁnitely many x ∈ Z. In particular,
by (for short) Matiyasevich’s Theorem, there is an ∃-formula φ(t0, . . . , tn−1)
such that

Z |= ∀t0 . . . tn−1 (
{∀x[xn + tn−1xn−1 + . . . + t0 ̸= 0]} ↔ φ(t0, . . . , tn−1)
) .

Since both An and its complement in Zn are diophantine in Z, the same holds
in Q, by our assumption of Z being diophantine in Q, i.e. A⋆⋆
n ∩ (Q⋆)n = A⋆
n.
As any ﬁnite extension of Q⋆ is generated by an integral primitive element
this implies that Q⋆ is relatively algebraically closed in Q⋆⋆.
(e) Choose a recursivley enumerable subset A ⊆ Z which is not decidable.
Then B := Z \ A is deﬁnable in Z, and hence in Q. If B were diophantine
in Q it would be recursively enumerable. But then A would be decidable:
contradiction.
So not every deﬁnable subset of Q is diophantine in Q, and hence Q is
not model complete. Or, in other words, there are models Q⋆, Q⋆⋆ of Th(Q)
with Q⋆ ⊆ Q⋆⋆ where Q⋆ is not existentially closed in Q⋆⋆.

We are conﬁdent that with similar methods as used in this paper one
can show for an arbitrary prime p that the unary predicate ‘x ̸∈ Qp’ is also

23

diophantine. This would imply that, in the setting of the Proposition, Q⋆ is
always radically closed in Q⋆⋆. However, we have no bias towards an answer
(let alone an answer) to the following (unconditional)

Question 25. For Q⋆ ≡ Q⋆⋆ ≡ Q with Q⋆ ⊆ Q⋆⋆, is Q⋆ always algebraically
closed in Q⋆⋆?

References

[CSS] Jean-Louis Colliot-Th´el`ene, Jean-Jacques Sansuc, Peter Swinnerton-
Dyer, Interactions of two quadrics and Chˆatelet surfaces I resp. II, J.
Reine Angew. Math. 373 (1987), 37-107 resp. 374 (1987), 72-168.

[CZ] Gunther Cornelissen, Karim Zahidi, Elliptic divisibility sequences and
undecidable problems about rational points, J. Reine Angew. Math.
613 (2007), 1-33.

[F] Gerd Faltings, Diophantine approximation on abelian varieties, Annals
of Mathematics 133 (1991), 549-576.

[HS] Marc Hindry, Joseph H. Silverman, Diophantine geometry, Springer
Graduate Texts in Mathematics 201, 2000.

[K] Jochen Koenigsmann, From p-rigid elements to valuations (with a
Galois-characterization of p-adic ﬁelds), J. Reine Angew. Math. 465
(1995), 165-182.

[Pa] Jennifer Park, A universal ﬁrst order formula deﬁning the ring of in-
tegers in a number ﬁeld, arXiv:1202.6371v1 [math.NT] (2012).

[P1] Bjorn Poonen, Characterizing integers among rational numbers with a
universal-existential formula, Amer. J. Math. 131(3) (2009), 675-682.

[P2] Bjorn Poonen, The set of nonsquares in a number ﬁeld is diophantine,
Math. Res. Lett. 16(1) (2009), 165-170.

[R] Julia Robinson, Deﬁnability and decision problems in arithmetic, J.
Symbolic Logic 14(2) (1949), 98-114.

[Si] Joseph H. Silverman, Integral points on abelian varieties, Invent. math.
81 (1985), 341-346.

Mathematical Institute, 24-29 St Giles’, Oxford OX1 3LB, UK
koenigsmann@maths.ox.ac.uk
 24
