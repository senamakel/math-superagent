<!-- source: https://www.cecm.sfu.ca/personal/monaganm/papers/trigpoly.pdf | converted from PDF -->

Algorithms for Trigonometric Polynomials

Jamie Mulholland
Department of Mathematics
University of British Columbia
Vancouver, B.C. Canada, V6T 1Z2
jmulholl@cecm.sfu.ca
 Michael Monagan
Department of Mathematics
Simon Fraser University
Burnaby, B.C. Canada, V5A 1S6
monagan@cecm.sfu.ca

ABSTRACT
In this paper we present algorithms for simplifying ratios of
trigonometric polynomials and algorithms for dividing, fac-
toring and computing greatest common divisors of trigono-
metric polynomials, that is, polynomials in sin(x) and cos(x).

1. INTRODUCTION
Let s and c denote sin(x) and cos(x) respectively. We are
interested in methods for simplifying ratios of trigonometric
polynomials, that is, elements of the ring Q[s, c]/⟨s
2+c2−1⟩.
For example, we would like to make the simpliﬁcation

(1 + c) s + 1 − c
2

s − 2 c2 + c4 + 1 → 1 + s + c
(1 − c2) s + 1 .

Such simpliﬁcation problems occur naturally in engineering
applications. They will also occur in any computation with
trigonometric polynomials that assumes a ﬁeld, for example,
if Gaussian elimination were applied to a matrix of trigono-
metric polynomials.

One approach to this problem is to try to cancel out a great-
est common divisor (GCD) from the numerator and denom-
inator trigonometric polynomials. In the above example the
simpliﬁed result was obtained by cancelling out the common
divisor s. What makes this problem non-trivial is that the
quotient ring Q[s, c]/⟨s
2 + c
2 − 1⟩ is not a unique factoriza-
tion domain, thus GCDs are not unique in general. In our
example the numerator trigonometric polynomial has the
following two irreducible factorizations

(1 + c)s + 1 − c2 = s(1 + s + c) = (1 + c)(1 + s − c)

and the denominator polynomial the following two

(1 + s − 2c
2 + c
4) = s(1 + s)(2 − s − c2)

= 1
2 (1 + s + c)(1 + s − c)(2 − s − c2).

∗This work was supported by NSERC of Canada and the
MITACS NCE of Canada.

Permission to make digital or hard copies of all or part of this work for
personal or classroom use is granted without fee provided that copies are
not made or distributed for proﬁt or commercial advantage, and that copies
bear this notice and the full citation on the ﬁrst page. To copy otherwise, to
republish, to post on servers or to redistribute to lists, requires prior speciﬁc
permission and/or a fee.
ISSAC 2001, UWO, Canada
c⃝2001 ACM 1-58113-218-2/ 00/ 0008 $5.00
 Thus we could also have cancelled out the common factor
1 + s + c or the common factor 1 + s − c.

The non-uniqueness of factorization in Q[s, c]/⟨s
2 + c2 − 1⟩
is pointed out by Trotter in [4] though no algorithms are
given. In [3], Roach studies this problem in the context of
indeﬁnite integration of trigonometric functions. Roach’s
approach applies to a subset of trigonometric polynomials,
those which he terms “co-ordinated”. We give some details
of his method in section 4 and an implementation of it in
REDUCE for comparison with our approach.

In this paper we will show how to compute greatest com-
mon divisors of trigonometric polynomials in all cases. To
do this we must ﬁrst understand factorization in the ring
Q[s, c]/⟨s
2 + c
2 − 1⟩. We study this in section 2. We show
that Q[s, c]/⟨s
2 + c2 − 1⟩ is an integral domain and how to
do division in it. This facilitates algorithms like fraction-free
Gaussian elimination. Next we characterize irreducibles in
Q[s, c]/⟨s
2 + c2 − 1⟩ and show how to determine all distinct
factorizations of an element of this ring. An application for
factoring trigonometric polynomials would be solving equa-
tions involving trigonometric polynomials.

In section 3 we study how to simplify ratios of trigonometric
polynomials, i.e. elements of the fraction ﬁeld of Q[s, c]/⟨s
2+
c
2 − 1⟩. We deﬁne and show how to compute greatest com-
mon divisors in Q[s, c]/⟨s
2 + c
2 − 1⟩ which gives one solution
to the simpliﬁcation problem, but, surprisingly, this does
not always lead to the simplest result. We give a more di-
rect approach which is easy to compute and always yields
the simplest result. The ability to simplify ratios of trigono-
metric polynomials to lowest terms means that algorithms
which work over a ﬁeld can be applied to trigonometric poly-
nomials without “blowing up”.

2. DIVISION AND FACTORIZATION
To study trigonometric polynomials we consider the ring of
polynomials Q[s, c] modulo s
2 + c2 − 1 = 0.

Definition 1. Deﬁne the relation ≡ on Q[s, c] by p ≡
q ⇔ s
2 + c
2 − 1 | p − q.

It is well known that ≡ is an equivalence relation on Q[s, c].
For each p ∈ Q[s, c] the equivalence class [p] = {q ∈ Q[s, c]
: p ≡ q}. When we speak of a trigonometric polynomial
q we mean a representative of the equivalence class [q] in
Q[s, c]/⟨s
2 + c2 − 1⟩.

245

Definition 2. Deﬁne φ : Q[s, c] −→ Q[s, c] by
φ(p) = p mod s
2 + c
2 − 1 where s
2 is replaced by 1 − c2.

Thus φ(p) is an element of the equivalence class [p] which
is at most linear in s. The following lemma shows that it is
unique.

Lemma 1. Let p ∈ Q[s, c]. Then φ(p) is the unique element
in Q[s, c] of the form A(c)s + B(c) equivalent to p.

Proof: Clearly φ(p) is linear in s by deﬁnition and φ(p) ≡ p.
Let q = A(c)s + B(c) such that q ≡ p. Write φ(p) = a(c)s +
b(c). Then φ(p) ≡ q and so s
2 + c2 − 1 | (A − a)s + (B − b).
This is impossible in Q[s, c] unless A = a and B = b. ■

Since ⟨s
2+c2−1⟩ is prime in Q[s, c] it follows that Q[s, c]/⟨s
2+
c2 − 1⟩ is an integral domain. We now discuss the degree of
a trigonometric polynomial and an analogue to the degree-
sum formula for polynomials.

Definition 3 (Trigonometric polynomial degree).
For p ∈ Q[s, c]/⟨s
2 + c
2 − 1⟩ we deﬁne the trigonometric de-
gree of p to be TD(p) = degs,c(φ(p)) where degs,c means
total degree.

Example 1: The polynomial p = s
2 + c
2 has total degree
2 in Q[s, c] but considered as a trigonometric polynomial it
has trigonometric degree 0 since φ(p) = 1.

Lemma 2 (Trigonometric degree-sum formula). Let
p, q ∈ Q[s, c]/⟨s
2 + c2 − 1⟩. Then TD(pq) = TD(p) + TD(q).

Proof: Write φ(p) = A(c)s + B(c) and φ(q) = a(c)s + b(c).
Let n1 = degc(A) + 1 , m1 = degc(B), n2 = degc(a) + 1 ,
and m2 = degc(b). Now

φ(φ(p)φ(q)) = (Ab + aB)s + (Bb + Aa − Aac2).

We claim that

deg(φ(φ(p)φ(q))) = deg(φ(p)) + deg(φ(q)).

This is easy to verify except for the case when m1 = n1, m2 =
n2. To determine deg(φ(φ(p)φ(q))) in this case we argue
as follows. Let A(c) = Pn1−1
i=0 Aic
i, B(c) = Pm1
i=0 Bic
i,
a(c) = Pn2−1
i=0 aici, and b(c) = Pm2
i=0 bic
i. The leading coef-
ﬁcient in Ab + aB is An1−1bm2 + an2−1Bm1 , and the leading
coeﬃcient of Bb+Aa−Aac2 is Bm1 bm2 −An1−1an2−2. If the
claim were false then both these coeﬃcients must be zero.
The solutions of the system

{An1−1bm2 + an2−1Bm1 = 0, Bm1 bm2 − An1−1an2−1 = 0}

are the two zero solutions

{An1−1 = 0, Bm1 = 0}, {an2−1 = 0, bm1 = 0}

and the two complex solutions

{an2−1 = ±ibm2 , An1−1 = ∓iBm1 }.

The former contradict the degree of p and q respectively and
the latter are not solutions in Q. Therefore deg(φ(φ(p)φ(q))) =
n1 + m2 and the claim is true for this case.
 Note that p ≡ φ(p), q ≡ φ(q), pq ≡ φ(pq) implies φ(p)φ(q) ≡
pq ≡ φ(pq). Therefore TD(φ(p)φ(q)) = deg(φ(pq)). There-
fore
 TD(pq) = deg(φ(pq))

= TD(φ(p)φ(q))

= deg(φ(φ(p)φ(q)))

= deg(φ(p)) + deg(φ(q))

= TD(p) + TD(q). ■

2.1 Tan-half angle substitution
To simplify ratios of trigonometric polynomials, and to study
factorization in the ring Q[s, c]/⟨s
2 + c2 − 1⟩ we will use the
tan-half angle substitution

sin(x) = 2 tan(x/2)
1 + tan(x/2)2 , cos(x) = 1 − tan(x/2)
2

1 + tan(x/2)2 .

For the rest of this paper we will denote tan(x/2) by t. This
substitution converts trigonometric polynomials into poly-
nomials in Q[t] divided by powers of (1 + t2). We employ
the tan half-angle substitution instead of the complex ex-
ponential mapping simply because it avoids computing in
Q(i) which is more expensive than computing over Q, but
otherwise the complex exponential mapping could be used.

Definition 4 (t-substitution). Deﬁne

ψt : Q[s, c] → Q(t) by ψt(p(s, c)) = p( 2t
1 + t2 , 1 − t2

1 + t2 ).

We recall the following well known results.

Lemma 3. ψt : Q[s, c] −→ Q(t) is a ring morphism and the
kernel of ψt is the principle ideal generated by s
2 + c2 − 1.

Lemma 4. Let p ∈ Q[s, c]/⟨s
2 + c
2 − 1⟩ with TD(p) = d.
Then ψt(p) = a(t)
(1+t2)d where a(t) ∈ Q[t] such that degt(a) ≤

2d and 1 + t2 ∤ a(t).

To make use of this ring morphism we need to be able to in-
vert the t-substitution. We now show how to do this and give
some results about the inversion. The inverse t-substitution
given by t = 1−c
s can be used to convert a rational polyno-
mial in t of the correct form back into a trigonometric poly-
nomial. Two questions arise: (i) What is the correct form?
(ii) Does direct substitution of the formula for t always re-
turn a trigonometric polynomial? The second question is
more involved than it seems. After making the t = 1−c
s sub-
stitution we have a rational trigonometric polynomial and
so to get a trigonometric polynomial we need to do trigono-
metric polynomial division. This is a problem in its own
right. There are simple ways to do the division in this case
but we will not consider them since we can answer both
questions by cleverly making the inverse t-substitution us-
ing resultants. How we do this is illustrated in the following
theorem and subsequent comments. However, ﬁrst we must
state the following useful lemma.

Lemma 5. Let a(t) = P2n
i=0 viti such that
v2n = Pn
i=1(−1)
i+1v2(n−i) and
v2n−1 = Pn−1
i=1 (−1)
i+1v2(n−i)−1 then 1 + t2 | a(t).

246

Proof: Consider b(t) = P2n−2
i=0 biti where bi = Pi/2
k=0(−1)
kvi−2k
if i even and bi = P(i−1)/2
k=0 (−1)
kvi−2k if i odd. We leave it
to the reader to verify a(t) = (1 + t2) · b(t). ■

Lemma 6. Let n ∈ N. For each polynomial a(t) with
1 + t2 ∤ a(t) and degt(a) ≤ 2n, the resultant

rest(a(t) − X(1 + t2)
n, st + (c − 1)) = p(s, c)X + q(s, c)

where p(s, c), q(s, c) ∈ Q[s, c]. Moreover, φ(p) = −2
n(1 − c)
n

and φ(p)|φ(q) in Q[s, c] and TD(q(s, c)) = 2n.

Proof: Write a(t) = P2n
i=0 viti, where of course if degt(a) <
2n then vi = 0 for i > degt(a(t)). The resultant in the
lemma is the determinant of Sylvesters’ matrix

S =
 2

6
6
6
6
6
4
v2n − `n
0´X v2n−1 v2n−2 − `n
1´X v2n−3 . . .
s c − 1 0 0 . . .
0 s c − 1 0 . . .
0 0 s c − 1 . . .
... ... ... ... ...
 3

7
7
7
7
7
5

The reader can verify that det(S) = p(s, c)X + q(s, c) where
φ(p(s, c)) = −2
n(1−c)
n and φ(q(s, c)) = (1−c)
n[
Pn
i=0 v2(n−i)
(1 + c)
i(1 − c)
n−i + Pn−1
i=0 v2(n−i)−1s(1 + c)
i(1 − c)
n−i−1].
The only thing left to show is that TD(q(s, c)) = 2n, that
is, degs,c φ(q(s, c)) = 2n. If the total degree of φ(q(s, c)) is
< 2n then both the coeﬃcient of cn and sc
n must be zero
in the second factor of φ(q(s, c)). This means that v2n =Pn
i=1(−1)
i+1v2(n−i) and v2n−1 = Pn−1
i=1 (−1)
i+1v2(n−i)−1,
and by Lemma 5 1 + t2 divides a(t). This is a contradiction.
Therefore TD(q(s, c)) = 2n. ■

Theorem 1. Let n ∈ N. Let a(t) be a polynomial such that
1 + t2 ∤ a(t) and degt(a) ≤ 2n. Then there exists a unique
trigonometric polynomial ˆa of trigonometric degree n such
that ψt(ˆa) = a(t)
(1+t2)n .

Proof: From the previous lemma we have that

rest(a(t) − X(1 + t2)
n, st + (c − 1)) = p(s, c)X + q(s, c)

where φ(p)|φ(q) in Q[s, c], TD(p) = n and TD(q) = 2n.
Solving p(s, c)X + q(s, c) = 0 for X in Q[s, c]/⟨s
2 + c2 − 1⟩
we get
 X = φ(q)
φ(p) ∈ Q[s, c]/⟨s
2 + c2 − 1⟩.

Now X ∈ Q[s, c]/⟨s
2 + c2 − 1⟩ has trigonometric degree n
and from the deﬁnition of the resultant we have

ψt(X) = a(t)
(1 + t2)n .

To show uniqueness, let ˆa, ˆb ∈ Q[s, c]/⟨s
2 + c
2 − 1⟩ such that
ψt(ˆa) = ψt(ˆb) = a(t)
(1+t2)n . Since ψt is a ring morphism then

ψt(ˆa − ˆb) = 0 so ˆa − ˆb ∈ kerψt = ⟨s
2 + c2 − 1⟩, thus ˆa = ˆb.
■

Theorem 1 says that every rational polynomial of the form
a(t)
(1+t2)n where a ∈ Q[t], 1 + t2 ∤ a(t) and degt(a) ≤ 2n is
the image under ψt of a trigonometric polynomial of degree
n. In what follows we denote ψ−1
t ( a(t)
(1+t2)n ) = X(s, c) where
X(s, c) is the unique polynomial in the proof.
 2.2 Division in Q[s, c]/⟨s
2 + c2 − 1⟩
The following theorem shows when one trigonometric poly-
nomial divides another in Q[s, c]/⟨s
2 + c
2 − 1⟩ and the proof
shows how to compute the quotient. In what follows we
denote by NU the numerator of a rational function, for ex-
ample, NU( a(t)
(1+t2)n ) = a(t).

Theorem 2. For a, b ∈ Q[s, c]/⟨s
2 + c2 − 1⟩

a|b ⇔ (i) TD(a) ≤ TD(b)

(ii) NU(ψt(a))|NU(ψt(b)) in Q[t]

(iii) deg(NU(ψt(b))) − deg(NU(ψt(a)))

≤ 2(TD(b) − TD(a))

Proof: (⇒) Let q be such that b = qa in Q[s, c]/⟨s
2 +c
2 −1⟩.
Then ∃r ∈ Q[s, c] such that b = qa + r(s
2 + c
2 − 1) in
Q[s, c]. By the trigonometric degree-sum formula, Lemma
2, TD(b) = TD(q) + TD(a). Moreover,

ψt(b) = ψt(qa + r(s
2 + c
2 − 1))

= ψt(q)ψt(a) + ψt(r) · 0

= ψt(q)ψt(a).

Expanding this equation we have

NU(ψt(b))
(1 + t2)db = NU(ψt(q))
(1 + t2)dq · NU(ψt(a))
(1 + t2)da

where dx = TD(x) for x = a, b, q. Since db = dq + da then
NU(ψt(b)) = NU(ψt(q)) · NU(ψt(a)). Moreover,

deg(NU(ψt(b))) − deg(NU(ψt(a)))

= deg(NU(ψt(q)))

≤ 2TD(q)

= 2(TD(b) − TD(a)).

This proves (⇒). For (⇐) suppose that the three conditions
hold as stated in the theorem. Then NU(ψt(b)) = q(t) ·
NU(ψt(a)) for some q ∈ Q[t]. So

NU(ψt(b))
(1 + t2)db = q(t)
(1 + t2)db−da · NU(ψt(a))
(1 + t2)da .

Since
 degt(q) = deg(NU(ψt(b)) − deg(NU(ψt(a)))

≤ 2(TD(b) − TD(a)) from (ii),

= 2(db − da)

we are guaranteed (by Theorem 1) that

bq = ψ−1
t ( q(t)
(1 + t2)db−da ) ∈ Q[s, c]/⟨s
2 + c2 − 1⟩

Therefore, a = bq · b in Q[s, c]/⟨s
2 + c2 − 1⟩. ■

Corollary 1. Let p ∈ Q[s, c]/⟨s
2+c
2−1⟩ such that TD(p) ≥
1. If deg(NU(ψt(p))) ≤ 2TD(p) − 2 then c + 1|p.

Proof: Since ψt(c + 1) = 2
1+t2 , then from the previous
theorem we have

c + 1|p ⇔ (i) 1 ≤ TD(p)

(ii) 2|NU(ψt(p))

(iii) deg(NU(ψt(p))) ≤ 2(TD(p) − 1).

Since (i),(ii),(iii) are all true then c + 1|p. ■

247

2.3 Irreducibility in Q[s, c]/⟨s
2 + c
2 − 1⟩
In this section we will identify irreducibles in Q[s, c]/⟨s
2 +
c2 − 1⟩. Since the units in Q[s, c]/⟨s
2 + c
2 − 1⟩ are the non-
zero rational numbers, this leads to the following deﬁnition
of the irreducibles in Q[s, c]/⟨s
2 + c
2 − 1⟩.

Definition 5. A non-zero element p ∈ Q[s, c]/⟨s
2 + c2 − 1⟩
is irreducible if
(a) p is not in Q (i.e. p is not a unit)
(b) whenever p = ab either a or b is in Q.

Theorem 3. Let p ∈ Q[s, c]/⟨s
2 + c
2 − 1⟩ such that p is not
a unit (i.e. TD(p) ≥ 1),
(a) if TD(p) = 1 then p is irreducible.
(b) if TD(p) > 1 then p is irreducible ⇔

(i) degt(NU(ψt(p))) ≥ 2TD(p) − 1,

(ii) NU(ψt(p)) is irreducible in Q[t] or

NU(ψt(p)) is a product of two irreducible

polynomials in Q[t] each of odd degree.

Proof: If TD(p) = 1 then p is irreducible by the trigono-
metric degree-sum formula. Now suppose TD(p) ≥ 2.
(⇒) Suppose that (i) or (ii) does not hold. If (i) does not
hold then c + 1|p by Corollary 1, so p is reducible. So sup-
pose (i) holds but (ii) does not hold, then we must have
NU(ψt(p)) is reducible but is not the product of two irre-
ducible polynomials in Q[t] of odd degree. Write

NU(ψt(p)) = q1(t) · q2(t),

for some q1, q2 ∈ Q[t] such that deg(q1), deg(q2) ≥ 1, q1
irreducible and if q2 irreducible then deg(q1), deg(q2) cannot
both be odd. Since (i) holds we have two case to consider,
namely

(1) degt(NU(ψt(p))) = 2d or

(2) degt(NU(ψt(p))) = 2d − 1.

Case (1): If degrees of q1 and q2 are both even then we can
split up ψt(p) as

ψt(p) = q1
(1 + t2)d1 · q2
(1 + t2)d2

where di = (1/2) degt(qi) for i = 1, 2. If degrees are both
odd then q2 must be reducible. Moreover, q2 must have an
irreducible factor of odd degree, say q3. Write q2 = q3 · q4
(note degt(q4) even). We can split up ψt(p) as

ψt(p) = q1 · q3
(1 + t2)d1 · q4
(1 + t2)d2

where d1 = (1/2)(degt(q1)+degt(q3)) and d2 = (1/2) degt(q4).

Case (2): Exactly one of q1 and q2 is of odd degree, say q1.
Split up ψt(p) as

ψt(p) = q1
(1 + t2)d1 · q2
(1 + t2)d2

where d1 = (1/2)(degt(q1) + 1) and d2 = (1/2)(degt(q2)).

In either case we can split up ψt(p) as

ψt(p) = ˆq1
(1 + t2)d1 · ˆq2
(1 + t2)d2
 where 2di ≥ degt( ˆqi) and di ≥ 1, i = 1, 2. By Theorem
1 both of these correspond to trigonometric polynomials in
Q[s, c]/⟨s
2 + c2 − 1⟩ with degrees d1 and d2 respectively,
where d1, d2 ≥ 1. Thus p is reducible.

(⇐) Suppose (i) and (ii) hold. Towards a contradiction sup-
pose p is reducible. Write p = a · b where a, b ∈ Q[s, c]/⟨s
2 +
c
2 − 1⟩ , and TD(a) ≥ 1, TD(b) ≥ 1. Now

ψt(p) = ψt(a) · ψt(b)

= NU(ψt(a))
(1 + t2)da · NU(ψt(b))
(1 + t2)db

where da = TD(a) and db = TD(b). By the trig degree-sum
formula da + db = TD(p). If degt(NU(ψt(a))) = 0 then

degt(NU(ψt(p))) = deg(NU(ψt(b)))

≤ 2db
= 2(TD(p) − da)

= 2TD(p) − 2da
≤ 2TD(p) − 2 since da ≥ 1

< 2TD(p) − 1.

This contradicts (i). Similarly if degt(NU(ψt(b))) = 0. So
NU(ψt(a)), NU(ψt(b)) /∈ Q. Thus NU(ψt(p)) is reducible in
Q[t]. Since (ii) holds and NU(ψt(p)) is reducible then both
NU(ψt(a)), NU(ψt(b)) are irreducible and degt(NU(ψ(a))),
degt(NU(ψ(b))) are odd. Let cda = degt(NU(ψ(a))) and bdb =
degt(NU(ψ(b))). Since cda, bdb are both odd and ≤ 2da and
2db respectively then cda ≤ 2da − 1 and bdb ≤ 2db − 1.

Since (i) holds then

degt(NU(ψt(p))) = 2d or 2d − 1.

If degt(NU(ψ(p))) = 2d then 2d = cda + bdb < 2da + 2db = 2d.
If degt(NU(ψ(p))) = 2d − 1 then 2d − 1 = cda + bdb < 2da +
2db − 2 = 2d − 2 which implies 2d ≤ 2d − 1. In each case we
get a contradiction. Therefore p is irreducible. ■

It follows from Theorem 3 that s, 1 + c and 1 − c are all irre-
ducible in Q[s, c]/⟨s
2 +c
2 −1⟩, hence the trigonometric poly-
nomial s
2 = 1 − c2 has two distinct factorizations, namely,
s × s and (1 + c)(1 − c). Notice also that Theorem 3 says
that an irreducible trigonometric polynomial may not have
an irreducible image under ψt. Moreover, an irreducible
image does not imply that the trigonometric polynomial is
irreducible either as the numerator of the image of c + 1 has
degree 0 in t.

2.4 Factorization in Q[s, c]/⟨s
2 + c2 − 1⟩
In this subsection we will sketch, by way of examples, an
algorithm for determining all factorizations of a trigonomet-
ric polynomial. We will not present an explicit algorithm
for doing this because the details are many and messy. A
Maple code for doing this is available from the authors.

Theorem 3 characterizes the irreducible trigonometric poly-
nomials in terms of their images under the t-substitution.
So to ﬁnd all factorizations of a trigonometric polynomial
we need to factor the numerator and look at combinations
of pairs of the odd degree factors, and also take into account
the possibility of (1 + c) factors.

248

Example 2: Let p = sc.
First we ﬁnd the image of p under ψt:

ψt(p) = ψt(sc) = 2t(1 + t)(1 − t)
(1 + t2)2 .

Each factor of p, under ψt, must have denominator 1 + t2 to
some power, thus p can have at most two factors since the
power of 1 + t2 in the denominator of ψt(p) is 2. Applying
Theorem 3 we see that the possible factorizations of ψt(p)
are:
 2 t
1 + t2 · (1 + t)(1 − t)
1 + t2 , 2 1 + t
1 + t2 · t(1 − t)
1 + t2 , and

2 1 − t
1 + t2 · t(1 + t)
1 + t2 .

These correspond to the three distinct factorizations of p

2(1/2s) · c = sc, 2(1/2(c + s + 1)) · (1/2(c + s − 1))

= 1/2(c + s + 1)(c + s − 1), and

2(1/2(c − s + 1)) · (1/2(−c + s + 1))

= 1/2(c − s + 1)(s − c + 1). □

Example 3 (from the introduction): Let p = (1+c)s+1−c2.
Again, we ﬁrst ﬁnd the image of p under ψt:

ψt(p) = 4t(1 + t)
(1 + t2)2 .

Each factor of p, under ψt, must have denominator 1 + t2 to
some power, thus p can have at most two factors. A possible
factorization of ψt(p) is

4 t
1 + t2 · 1 + t
1 + t2 .

However, there is still another factorization

4 1
1 + t2 · t(1 + t)
1 + t2 .

This factorization follows from Corollary 1. We can eas-
ily see that there are no other factorizations of ψt(p) in
which each factor corresponds to a trigonometric polyno-
mial. Therefore the two distinct factorizations of p are:

4(1/2s)(1/2(c + s + 1)) = s(c + s + 1),

4(1/2(1 + c))(1/2(s − c + 1)) = (1 + c)(s − c + 1). □

We end this section by noting that the number of distinct
factorizations of p ∈ Q[s, c]/⟨s
2 +c2 −1⟩ grows exponentially
with the number of distinct odd degree factors of a(t) =
NU(ψt(p)). For example, if TD(p) = d and a(t) factors into
2d distinct linear factors then there are 1×3×5×...×(2d−1)
distinct factorizations of p and `2d
2 ´ = 2d
2 − d distinct irre-
ducible divisors of p. Instead of computing all trigonometric
factorizations of a trigonometric polynomial p, an applica-
tion may require only a single factorization or the set of
irreducible trigonometric polynomial divisors of p. This in-
formation is also easily determined from the factorization of
a(t) and application of Theorem 3.
 3. GCDS AND SIMPLIFICATION
In this section we deﬁne the trigonometric GCD of two
trigonometric polynomials and give an algorithm for com-
puting it. The classical deﬁnition of GCD for a commutative
ring R, as stated, for example, by Hungerford in [2], is

Definition 6 (classical GCD). Let R be a commuta-
tive ring and let a, b ∈ R. An element g ∈ R is a greatest
common divisor of a and b if
(i) g|a and g|b, and

(ii) if p|a and p|b then p|g.

Example 4 below shows that under this deﬁnition a GCD
may not exist even when common divisors exist. This is not
useful for computational purposes so we are led to consider
the following deﬁnition for a GCD. The two deﬁnitions are
equivalent when we are in a UFD.

Definition 7 (alternative GCD). Let R be a commu-
tative ring and let a, b ∈ R. An element g ∈ R is a greatest
common divisor of a and b if
(i) g|a and g|b, and

(ii) if p|(a/g) and p|(b/g) then p is a unit.

Example 4: Let a = s(1 + c), b = −c
2 + cs + s + 1.
Using the methods of Section 2.4 we ﬁnd that a and b have
exactly the following factorizations:

a = s(c + 1),

b = (c + s + 1)s = (−c + s + 1)(1 + c).

Now, s and 1 + c divide both a and b, hence under the
classical deﬁnition of GCD we would have that the GCD
g, if it exists, of a and b is divisible by both s and 1 + c.
Thus, s, 1 + c | g and g | a = s(1 + c) so g = s(1 + c)
(up to multiplication by a unit). But g = s(1 + c) ∤ b, a
contradiction. However, we have that both s and 1 + c are
GCDs of a and b according to the alternative deﬁnition. □

The previous example shows that GCDs are not unique. The
next example shows that two GCDs may not even have the
same trigonometric degree.

Example 5: Let a = −5c3 + 5sc
2 − 5c
2 + 2cs + c + 9s + 9,
b = −c
5 + 17c
4 − 7sc
4 + 6c3 − 16sc
3 + 2c2 − 14sc
2 − 21c −
24cs − 3 − 3s. The images of a and b under ψt are:

ψt(a) = 8 t(t + 1)(t3 + 2)(t + 2)
(1 + t2)3 ,

ψt(b) = 32 t(t + 1)(t3 + 2)(t5 − 2)
(1 + t2)5 .

We cannot take the image of the GCD to be t(t+1)(t3+2) for
if we did we cannot partition the three (1 + t2) factors in the
denominator of ψt(a) between t(t+1)(t3+2) and the cofactor
image (t + 2) so that both are images of a trigonometric
polynomials. We can split these images of trigonometric
polynomials as follows:

ψt(a) = 8 t(t + 1)
1 + t2 · (t3 + 2)(t + 2)
(1 + t2)2 and

249

ψt(b) = 32 t(t + 1)
1 + t2 · (t3 + 2)(t5 − 2)
(1 + t2)4 .

We can also split them as:

ψt(a) = 8 t(t3 + 2)
(1 + t2)2 · (t + 1)(t + 2)
1 + t2 and

ψt(b) = 32 t(t3 + 2)
(1 + t2)2 · (t + 1)(t5 − 2)
(1 + t2)3 .

The ﬁrst way we have the common factor t(t+1)
1+t2 which corre-
sponds to the GCD s−c+1 of a and b whereas in the second
way we have the common factor t(t
3+2)
(1+t2)2 which corresponds
to the GCD c2 + 2cs − 2c + 2s + 1. □

This example shows that two GCDs may have diﬀerent trigono-
metric degrees. It seems reasonable that a GCD of high-
est trigonometric degree is the one we really are interested
in. This motivates the following deﬁnition for a GCD in
Q[s, c]/⟨s
2 + c2 − 1⟩.

Definition 8 (trigonometric GCD). Let a, b ∈
Q[s, c]/⟨s
2 + c
2 − 1⟩. An element g ∈ Q[s, c]/⟨s
2 + c
2 −
1⟩ is called a trigonometric greatest common divisor (trig
GCD) of a and b if
(i) g|a and g|b, and

(ii) if p|(a/g) and p|(b/g) then p is a unit.

(iii) if h satisﬁes (i) and (ii) then TD(g) ≥ TD(h)

Following the method in the previous example we now present
an algorithm for computing trigonometric greatest common
divisors.

Algorithm [trig GCD]
Input: Two trigonometric polynomials a and b.

(da, db) ← (TD(a), TD(b))

(at, bt) ← (ψt(a) · (1 + t2)
da, ψt(b) · (1 + t2)
db)

gt ← gcd(at, bt)

( ¯at, ¯bt) ← (at/gt, bt/gt)

l ← min(da − ⌈degt( ¯at)/2⌉, db − ⌈degt( ¯bt)/2⌉)

if degt(gt) > 2 · l then

f ← a smallest odd degree factor of gt.
gt ← gt/f, ¯at ← ¯at · f, ¯bt ← ¯bt · f .
l ← min(da − ⌈degt( ¯at)/2⌉, db − ⌈degt( ¯bt)/2⌉).

g ← ψ−1
t ( gt
(1+t2)l )

RETURN(g). ♦

In the algorithm there is an extra adjustment that has to
be made if the degree of gt is too big. Example 5 illustrated
this. Note that with condition (iii) the GCD is still non-
unique as illustrated by example 4.
 Note, in the algorithm we may need to remove from p ∈ Q[t]
a factor of least odd degree. This can be done by factoring p
over Q but it makes the trigonometric GCD algorithm rela-
tively expensive. In some applications it will be worthwhile
computing any linear factors of p before attempting a full
factorization of p.

Since we now know how to compute trigonometric GCDs,
simplifying a ratio of trigonometric polynomials should be
straight forward, namely, compute and divide out by a trigono-
metric GCD. However, it turns out that we may be able to
simplify the ratio further than by dividing out by a trigono-
metric GCD. Consider the following example.

Example 6: Let a = 5c3 + 21c2 + 4cs + 23c + 15 + 12s,
b = 7c
3 − c2s + 31c2 + 2cs + 37c + 15s + 21. The images
under the t-substitution are:

ψt(a) = 8(t2 + 2)(t3 + 2)(t + 2)
(1 + t2)3

and
 ψt(b) = 8(t2 + 2)(t3 + 2)(t + 3)
(1 + t2)3 .

Now,
 ψt(a)
ψt(b) = t + 2
t + 3 =
 t+2
1+t2

t+3
1+t2 .

Converting both the numerator and the denominator back
to trigonometric polynomials we get

a
b = 2c + s + 2
3c + s + 3 .

So a
b can be simpliﬁed to a ratio of two degree 1 trigonomet-
ric polynomials. This suggests that a trigonometric polyno-
mial of trigonometric degree 2 must have been cancelled out
from both a and b. But the only trigonometric GCD of a
and b is c + 3 which has trigonometric degree 1. There is no
common divisor of a and b with trigonometric degree greater
than 1. This implies that 2c + s + 2 does not divide a and
3c + s + 3 does not divide b. □

The previous example illustrates that simplifying rational
trigonometric polynomials done via the t-substitution may
produce a rational trigonometric polynomial where the trigono-
metric degrees of the numerator and denominator have dropped
more than that of just cancelling the trigonometric GCD. In
fact, simplifying this way we are guaranteed that we will not
do any worse than if we had cancelled a trigonometric GCD.
We prove this in the theorem following the statement of the
algorithm. Notice also that we do not need to factor in Q[t]
as we might have to if we attempt to cancel a trigonometric
GCD. We now present the algorithm for simplifying rational
trigonometric polynomials done via the t-substitution.

Algorithm [trig simplify]
Input: A rational trigonometric polynomial a
b .

(da, db) ← (TD(a), TD(b))

(at, bt) ← (ψt(a) · (1 + t2)
da, ψt(b) · (1 + t2)
db)

gt ← gcd(at, bt)

250

( ¯at, ¯bt) ← (at/gt, bt/gt)

if da ≤ db then
¯at ← ¯at(1 + t2)
db−da

else ¯bt ← ¯bt(1 + t2)
da−db

l ← max(⌈degt( ¯at)/2⌉, ⌈degt( ¯bt)/2⌉)

¯a ← ψ−1
t ( ¯at/(1 + t2)
l)

¯b ← ψ−1
t ( ¯bt/(1 + t2)
l)

RETURN(¯a/¯b). ♦

Theorem 4. Let f, g ∈ Q[s, c]/⟨s
2 + c2 − 1⟩ be non-zero
trigonometric polynomials. Let p/q be the output of algo-
rithm trig simplify. Then there does not exist trigonometric
polynomials a, b satisfying a/b = p/q and
TD(a) + TD(b) < TD(p) + TD(q).

Proof: Let dp = TD(p), dq = TD(q). Let pt = ψt(p)(1 +
t2)
dp and qt = ψt(q)(1 + t2)
dq. We claim that the output of
algorithm trig simplify satisﬁes GCD(pt, qt) = 1 and either
(i) deg pt > 2dp − 2 or (ii) deg qt > 2dq − 2, that is p and q
are not both divisible by 1 + c. Let da = TD(a), db = TD(b)
and let at = ψt(a)(1 + t2)
da and bt = ψt(b)(1 + t2)
db. Now
a/b = p/q implies

btpt(1 + t2)
dq−dp = qtat(1 + t2)
db−da.

Since 1 + t2 is relatively prime to at, bt, pt, qt then dq − dp =
db − da, that is,
 dq + da = db + dp.

Next we note that because GCD(pt, qt)=1 and GCD(pt, 1 +
t2)=1 then pt|at. In case (i) we have deg pt > 2dp − 2. Since
pt|at then we have 2da ≥ deg at ≥ deg pt > 2dp − 2, hence
da ≥ dp, equivalently −da ≤ −dp. Adding this to the above
equation yields dq ≤ db hence the theorem follows for this
case. A similar argument may be used for case (ii). ■

4. OTHER APPROACHES
One of the approaches tried by Maple 6’s simplify com-
mand when given a ratio of trigonometric polynomials is
the following. Replacing s by √
1 − c2 we may view a ratio
of trigonometric polynomials as an algebraic function, that
is, an element of the function ﬁeld Q(c, √
1 − c2). A stan-
dard form for algebraic functions is to clear √
1 − c2 from the
denominator. Replacing √
1 − c2 back by s yields a result of
form a(c) + b(c)s where a(c) and b(c) are in Q(c). When ap-
plied to the simpliﬁcation problem in the introduction this
yields the following result
`c
2 + c − 1
´

c (c4 − 3 c2 + 3) s − (1 + c) `c2 − c − 1
´

c (c4 − 3 c2 + 3) .

We observe that the trigonometric degree of the numerator
is 3 and that of the denominator is 5 which is greater than
that of the input, thus this is not the simplest form even
though it is a canonical form.

The approach taken by REDUCE 7’s trigsimp command
[1] when given an input involving sin x and cos x is to apply
 rewriting techniques similar to those used by the simplify
and combine commands in Maple 6. The numerator and
denominator of a ratio of trigonometric polynomials is put
in a canonical form but there is no guarantee that a common
factor of the numerator and denominator will be detected
and cancelled out. REDUCE 7 succeeds on the example in
the introduction but fails on example 5.

The approach taken by REDUCE 7’s trigfactorize and
triggcd commands [1] is to apply the method of Roach [3].
We give some details of this method here. Roach’s method
ﬁrst converts inputs to complex exponentials. Let i = √
−1
and e denote e
ix. Let f ∈ Q[s, c]/⟨s
2 + c2 − 1⟩ and g ∈
Q(i)[e, e
−1] be the image of f under the complex exponential
map.

Definition 9. g ∈ Q(i)[e, e
−1] is co-ordinated if g(e) is an
even or odd function of e.

Example 7: s = i
2 e
−1 − i
2 e and sc = i
4 e
−2 − i
4 e
2 are co-
ordinated but s + 1 = i
2 e
−1 + 1 − i
2 e and s
2 + s = − 1
4 e
−2 +
i
2 e + 1
2 − i
2 e − 1
4 e
2 are not co-ordinated.

To factor a trigonometric polynomial Roach requires that it
be co-ordinated. We remark that most trigonometric poly-
nomials are not co-ordinated. Roach multiplies through by
the least power of e so that the input is now in Q(i)[e]. No-
tice that the input will now be an even polynomial of e so
the substitution e → √
e can be made. Roach then factors
the resulting polynomial in Q(i)[e] and reverses this process
to obtain a factorization in Q[s, c]/⟨s
2 + c2 − 1⟩. The pro-
cedure for computing a GCD of co-ordinated polynomials
in Q[s, c]/⟨s
2 + c
2 − 1⟩ is analogous. The key observation
made by Roach is that if a trigonometric polynomial is co-
ordinated and irreducible then when this procedure is ap-
plied to express it in Q(i)[e], it will be irreducible. Because
Q(i)[e] is a UFD, these procedures will return unique results
for any given input, however, this does not mean that the
factorization and GCD is unique.

Example 8: To factor sc = i
4 e
−2 − i
4 e
2 Roach’s algorithm
factors the polynomial i
4 − i
4 e
2 = i
4 (e + 1)(e − 1) from which
one recovers the factorization s × c, not the two other fac-
torizatons shown in example 2.

To deal with the non co-ordinated case, Roach suggests that
one make the substitution x → 2x to the input polynomials.
This makes them co-ordinated. But, reversing the substitu-
tion results in outputs involving sin x
2 and cos x
2 of double
the degree.

Example 9: To factor sin(x) + 1 and sin(x)
2 + sin x one
factors the polynomials −i e
2 + 2e + i = −i(e + i)
2 and
− 1
4 (e
4 + 2i e
3 − 2e
2 − 2i e + 1) = − 1
4 (e − 1)(e + 1)(e + i)
2

respectively. This yields the factorizations (sin x
2 + cos x
2 )
2

and 2 sin x
2 cos x
2 (sin x
2 + cos x
2 )
2 respectively.

The REDUCE 7 trigfactorize command, on input of trigono-
metric polynomials which are not co-ordinated returns the
input polynomials unfactored. Similarly, the triggcd com-
mand returns 1 for the GCD. The user may specify x
2 as an
option to either command to eﬀect the x → 2x substitution
just described.

251

5. CONCLUSIONS AND FINAL REMARKS
The main result of our paper is a way to simplify ratios
of trigonometric polynomials. We have also shown how to
divide, factor and compute GCDs of trigonometric polyno-
mials. Though we have not given the algorithmic details for
dividing and factoring trigonometric polynomials in the pa-
per, we have implemented all of these operations in Maple.
Our Maple code is available from the authors or from our
web site www.cecm.sfu.ca/CAG/products.html.

The theory for factorization of trigonometric polynomials
which we developed over Q holds for any constant ﬁeld k
provided i = √
−1 ̸∈ k. If i ∈ k then s + ic and s − ic are
units as (s + ic)(s − ic) = 1 and consequently the trigono-
metric degree sum formula that we gave no longer holds. We
have not modiﬁed the theory for this case but we note that
it will be simpler because Q(i)[s, c]/⟨s
2 + c2 − 1⟩ is a UFD,
thus GCDs are unique up to multiplication by units. Con-
sequently simpliﬁcation can be accomplished by cancelling
a GCD.

Acknowledgement
We acknowledge helpful discussions with our colleagues, in
particular Hans Bauck, Mark van Hoeij, and Petr Lisonek.
We also thank Wolfram Koepf for providing us with informa-
tion about REDUCE’s trigonometric polynomial commands
and the referees for their comments.

6. REFERENCES
[1] Koepf, W., Bernig A., Melenk H. (1999) TRIGSIMP: A
REDUCE Package for the Simpliﬁcation and
Factorization of Trigonometric and Hyperbolic
Expressions. REDUCE 7 documentation.

[2] Hungerford, T.W. (1980) Algebra, second edition,
Graduate Texts in Mathematics, Springer-Verlag.

[3] Roach, K. (1992), Trigonometric Factorization and
Integration, Unpublished manuscript. Presented at the
Maple Retreat, June, 1992.

[4] Trotter, H.F. (1989), An Overlooked Example of
Nonunique Factorization, American Mathematical
Monthly, 95(4), 339–342.
 252
