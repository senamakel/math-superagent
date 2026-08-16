<!-- source: https://arxiv.org/pdf/1204.0450 | converted from PDF -->

arXiv:1204.0450v1  [math.CV]  2 Apr 2012
CONSTRAINTS ON HYPOTHETICAL COUNTEREXAMPLES TO THE
CASAS-ALVERO CONJECTURE

R. LATERVEER & M. OUNAIES

In [1], Casas-Alvero formulated the following :

Conjecture. Let f ∈ C[X] be a polynomial of degree N ≥ 1. Assume that f has a common
root with each of its derivatives f (1), · · · , f (N −1) (we will say that f is CA). Then f is of the form
f (z) = a(z − b)N , a, b ∈ C.

The conjecture is known to be true in low degrees [3]. The ﬁrst major break-through in the
subject was [5], where the conjecture is proven for all N that are powers of a prime number.
A very nice overview of all that is currently known concerning this conjecture, as well as an
alternative proof of the result of [5], can be found in [4].
This note is the fruit of a failed attempt to prove the conjecture for N = 12 (this is the lowest
degree for which the conjecture has not been settled as yet).
What follows is a short description of the contents of this note.
In the ﬁrst section, which is largely expository, techniques are elementary. The degree N is
arbitrary, and we ask ourselves under what extra conditions on the number of roots the conjecture
can be proven: The main new result in this ﬁrst section is proposition 5: the conjecture is true if
f has at most 4 distinct roots.
In the second section we restrict attention to the case N = pr + 1 (where p is a prime), and
then further specialize to the case N = p + 1. We use the p-adic valuation, inspired by Draisma
and de Jong's take ([4], [6]) on the result of Graf von Bothmer et alii [5]. The main results of the
second section are: If f is a CA-polynomial of degree N = p + 1, and c is the root of f (N −1),
then there are at least 2 other indices 2 ≤ l1 < l2 < N − 1 such that f (l1)(c) = f (l2)(c) = 0 (this
is Proposition 7). Also, we are able to prove the conjecture for degree p + 1 polynomials all of
whose roots are rational (Proposition 8).
In the third and last section, we present a short remark that gives some additional constraints
on hypothetical counterexamples to the conjecture in degree 12.
We hope this note may raise interest in the subject, and perhaps spark further progress towards
proving the conjecture...

Convention. In what follows, we will call a polynomial non-trivial if it has at least two distinct
roots. The conjecture says that there exists no non-trivial CA-polynomial.

From the deﬁnition of a CA-polynomial, it is easily seen that:

Date: November 15, 2018.
1991 Mathematics Subject Classiﬁcation. 30E05, 42A85.
Key words and phrases. Casas-Alvero conjecture, polynomials.
1

2 R. LATERVEER, M. OUNA¨IES

Lemma 1. Let f be a monic CA-polynomial of degree N ≥ 1 and α ∈ C∗ and β ∈ C. The
polynomial g(z) = α−N f (αz + β) is also a monic CA-polynomial of degree N.

In consequence, whenever convenient, we may choose any root of f and assume it to be equal
to 0. When we have two distinct roots of f , we may assume the ﬁrst to be equal to 0 and the
second to be equal to 1.

1. CONSTRAINTS ON THE NUMBER OF DISTINCT ROOTS

The following result, proven by Draisma and de Jong, conveniently subsumes many “easy”
cases where the conjecture can be proven:

Proposition 1. [4, Proposition 6] Let f be a CA-polynomial of degree N ≥ 1. Let αi, i =
1, · · · , N − 1 be a common root of f and f (i). Then the cardinality of {α1, · · · , αN −1} cannot
be two.

Remark 1. As immediate corollaries of Proposition 1, we get the following three special cases:
1. If f is CA and f ′′(z) = N(N − 1)(z − a)N −2, then f (z) = (z − a)N .
2. Let f be a monic CA-polynomial of degree N, and suppose that f has a root a of multiplicity
at least N − 1. Then f (z) = (z − a)N .
3. Let f be a non-trivial CA-polynomial, then f has at least three distinct roots.
We note that case 1 was also dealt with in [11, Proposition 2.2].

In the next two propositions, we will go a step further in directions 1 and 2. Later on (Propo-
sitions 4 and 5), we will go two steps further in direction 3.

Proposition 2. Let f be a CA-polynomial of degree N ≥ 4. Assume that for some a ∈ C,
f (3)(z) = N !
(N −3)! (z − a)N −3. Then f (z) = (z − a)N .

Proof. Thanks to Lemma 1, we may choose a = 0.
Assume that f ′(0) ̸= 0, then f has a root of multiplicity at least 2 which is different from 0
and again by Lemma1, we may assume f (1) = f ′(1) = 0. Thus

f (z) = zN − (N − 1)z2 + (N − 2)z; f ′′(z) = (N − 1) (
NzN −2 − 2) .

Solving f (z) = f ′′(z) = 0, we get z = N
N +1 and ( N +1
N )N −2 = N
2 . We easily see that the function
φ(t) = (t − 2) ln t+1
t − ln t
2 is strictly decreasing for t ≥ 4 and that φ(4) < 0. Thus the equality
φ(N) = 0 is never reached for N ≥ 4.
We conclude that we necessarily have f ′(0) = 0. Then, for some constant c, f ′′(z) = N(N −
1)zN −2 + 2c and f (z) = zN + cz2. Solving f (z) = f ′′(z) = 0, we get that c = 0. □

Proposition 3. Let f be a monic CA-polynomial of degree N ≥ 3, and suppose f has a root a
of multiplicity at least N − 2. Then f (z) = (z − a)N .

Proof. Let a = 0. If f (N −1)(0) ̸= 0, then we may assume that f (1) = f (N −1)(1) = 0. Hence

f (z) = zN −2(z2 − Nz + N − 1), f (N −2)(z) = (N − 1)!
2 (Nz2 − 2Nz + 2).

CONSTRAINTS ON HYPOTHETICAL COUNTEREXAMPLES TO THE CASAS-ALVERO CONJECTURE 3

Solving f (z) = f (N −2)(z) = 0, we get z2 = 2 and z = N +1
N . Thus (N + 1)2 = 2N 2 which is
impossible.
We conclude that we necessarily have f (N −1)(0) = 0. Then, for some constant c, f (z) =
zN + czN −2 and f (N −2)(z) = N !
2 z2 + c. Solving f (z) = f (N −2)(z) = 0, we get c = 0. □

Remark 2. We have chosen to present an elementary proof of Proposition 3, though we also can
see it as direct consequence of the forthcoming Proposition 4.

Now, before going further, let us recall some basic properties of the elementary symmetric
polynomials. Let a polynomial f and its derivatives be of the form

f (l)(z) = N!
N − l! (a0zN −l + (
N − l
1
 )
a1zN −l−1 + (
N − l
2
 )
a2zN −l−2 + · · · + aN −l).

(Here by convention f = f (0)). Let σm(l) be the sum of the mth powers of the roots of f (l), for
l = 0, · · · , N − 1. Then Newton formulas applied to each f (l) give the following relations (See
for example [7] for more details on Newton formulas):

Lemma 2. j∑

k=1 σk(l)(N − l
j − k
 )aj−k = −j(N − l
j
 )aj

for 0 ≤ l ≤ N − 1, 1 ≤ j ≤ N − l.

Remark 3. In particular, for j = 1, we have that

σ1(l)
N − l = σ1(0)
N
for l = 0, · · · , N − 1, which means that the center of mass of the roots of the derivatives is ﬁxed.
As obviously
 σ1(N − 1) = σ1(0)
N = a1

is the only root of f (N −1), we see that whenever f is a Casas-Alvero polynomial, the center of

mass of its roots σ1(0)
N is itself a root of f . As a direct consequence, the number of distinct roots
of a Casas-Alvero polynomial cannot be two. Actually, we can say more: if f has more than two
distinct roots, then at least one of them (the center of mass) has to be in the interior of the convex
hull of the roots.

In order to go further in the study of this convex hull, let us ﬁrst recall the well-known Gauss-
Lucas theorem:

Theorem 1 (Gauss-Lucas). Let f ∈ C[X]. Let f be a complex polynomial, f ′ be its derivative
and Γ be the convex hull of the roots of f . Then each root of f ′ is either a multiple root of f , or
belongs to the interior of Γ.

We will call the convex hull Γ of the roots of f the Gaus-Lucas hull of f , the interior of Γ the
open Gauss-Lucas hull and the boundary of Γ the Gauss-Lucas polygon.

4 R. LATERVEER, M. OUNA¨IES

Corollary 1. [8] Let f be a polynomial of degree N. Let ζ be a root of f located on its Gauss-
Lucas polygon, with multiplicity m ≤ N − 1. Then, for all m ≤ k ≤ N − 1, f (k)(ζ) ̸= 0.

This corollary yields another way of seeing that a non-trivial CA-polynomial f must have at
least one of its roots in its open Gauss-Lucas hull, and in particular that the number of distinct
roots cannot be two. Actually, we can also use Gauss-Lucas theorem to show that this number
cannot be three either and more generally that a non-trivial CA-polynomial must have at least
two distinct roots in its open Gauss-Lucas hull.

Proposition 4. Let f be a non-trivial Casas-Alvero polynomial of degree N ≥ 3. Then f has at
least two distinct roots in its open Gauss-Lucas hull. In particular, N ≥ 5 and f has at least 4
distinct roots.

Proof. Assume that f has exactly one root, say 0, in its open Gauss-Lucas hull and let ζ be
the one among the roots of f located on the Gauss-Lucas polygon with maximal multiplicity
m. Then by Corollary1, f (m)(0) = f (m+1)(0) = · · · = f (N −1)(0) = 0 which means that for
j = m, . . . , N − 1:
 f (j)(z) = N!
(N − j)! zN −j.

Taylor expansion gives

f (0) =
 N∑

j=m
 f (j)(ζ)
j! (−ζ)j = ζ N N∑

j=m
(−1)j(
N
j
 ) = ζ N (−1)m(
N − 1
m
 )
.

As f (0) = 0, we get ζ = 0, which is a contradiction. □

Remark 4. Proposition 4 can also be deduced from Draisma and de Jong's result Proposition
1.
 As pointed out in [4], arguments based only on Gauss-Lucas theorem are not sufﬁcient to deal
with polynomials of degree greater than 5. In the next proposition, we will use Rolle's theorem
and relations 2 to go further :

Proposition 5. Let f be a non-trivial Casas-Alvero polynomial of degree N ≥ 5. Then f has at
least ﬁve distinct roots. In particular, N ≥ 6.

Proof. Assume that f has four distinct roots. Then by the previous proposition, it has at least
two distinct roots in its open Gauss-Lucas hull. This implies that the four roots are on a line. By
Lemma 1, we may assume that it is the real line. Then by Gauss-Lucas theorem, all its derivatives
also have only real roots. We will use the following lemma based on Rolle's theorem :

Lemma 3. [9, Lemma 4.2] A root of multiplicity m of f , 0 ≤ m ≤ i can be at most a simple
root of f (i).

We denote by M the maximal multiplicity of the roots of f . By Proposition 3, we know that
2 ≤ M ≤ N − 3.

CONSTRAINTS ON HYPOTHETICAL COUNTEREXAMPLES TO THE CASAS-ALVERO CONJECTURE 5

• First case : M ≤ N −5. Again using Lemma 1, we may assume without loss of generality
that the roots of f are as follows : a < 0 < 1 < b and f (N −1)(0) = 0. By Corollary 1, a
and b cannot be zeros of f (k) for N − 5 ≤ k ≤ N − 1. Besides, by Lemma 3, each zero
of f (k) is simple. Then we necessarily have f (N −2)(1) = 0, f (N −3)(0) = 0, f (N −4)(1) =
0, f (N −5)(0) = 0. Integrating ﬁve times the expression f (N −1)(z) = N!z and taking

into account these constraints, we get f (N −5)(z) = N!
5! z(z2 − 5)2. But this contradicts
Lemma 3.
• Second case : M = N − 4 (which implies that N ≥ 6). By Lemma 1, we arrange
the roots as follows : a < 0 < b < 1 and we assume that f (N −1)(0) = 0. Denote by
ma, m0, mb, m1 their respective multiplicities. Then again by Lemma 3, we must have
f (N −2)(b) = 0, f (N −3)(0) = 0, f (N −4)(b) = 0. Like in the ﬁrst case, computing the last
derivatives, we get

f (N −1)(z) = N!z, 2!f (N −2)(z) = N!(z2 − b
2),

3!f (N −3)(z) = N!z(z2 − 3b
2), 4!f (N −4)(z) = N!z(z2 − 5b
2)(z2 − b
2).

Obviously, as f (N −4)(b) = 0, we have mb ≤ N − 5. From Gauss-Lucas theorem, we
deduce that a < −
√5b. Now we apply Lemma 2 with l = 0, j = 1 and with l = 0, j = 3
to obtain

(1) maa + mbb + m1 = maa
3 + mbb
3 + m1 = 0.

We deduce that maa(a
2 −1) = −mbb(b
2 −1) and looking at the sign, we see that −a < 1.
Then ma > −ama = mbb + m1 > m1 which implies that ma ≥ 2 and m1 ≤ N − 5.
Let us note that in the case where ma = 2, m1 = mb = 1, equations 1 give : a(a+1)2 =
0. Thus, this case cannot occur. We can readily deduce that m0 ≤ N − 5. The only
possibility left is ma = M = N − 4.
From the relation −(N − 4)a(1 − a
2) = mbb(1 − b
2), we deduce that φ(−a) ≤ φ(b)
where we put φ(t) = t(1 − t
2). But φ is increasing on [0, 1/√
3] and we know that
−a > b > 0. Thus we have −a > 1/√3. Now we get back to the linear equation in 1 :

N − 4 = mb b
−a + m1 1
−a < mb√5 + m1√3.

If m1 = mb = 1, this leads to N = 6 and ma = 2. But we have already shown above
that this case can't occur.
If m1 = 1, mb = 2, we also obtain N = 6 and ma = 2.
Equations 1 now imply that 4a
2 + 2a − 1 = 0. But this equation has no real solution.
If m1 = 2, mb = 1, we obtain N ≤ 7. On the other hand, we know that m1 ≤ N − 5.
Thus N = 7 and ma = 3.
Equations 1 imply (a + 1)2(4a + 1) = 0. Thus we must have a = −1/4 and b = −5/4.
But this contradicts the fact that b > 0.
Finally, the second case leads to a contradiction.

6 R. LATERVEER, M. OUNA¨IES

• Third case : M = N − 3. We proceed similarly to the previous case. Again, we obtain
that ma ≥ 2. Thus we necessarily have : ma = M, m0 = m1 = mb = 1. The linear
equation in 1 gives :
 N − 3 = b
−a + 1
−a < 1
√5 + √3 < 3.

It follows that N = 5 and ma = 2. But we have already shown that this is impossible. □

2. POLYNOMIALS OF DEGREE pr + 1

We quickly recall the deﬁnition of the p-adic valuation (for more details, the reader is referred
to [10])

Deﬁnition 1. Let p be a prime number. For a positive integer n ∈ N∗, the p-adic valuation vp(n)
is deﬁned to be the exponent of p in the prime decomposition of n: If n = pr · n
′ with n
′ prime to
p, then vp(n) = r.

The map vp : N∗ → N can be extended to a map vp : C → Q∪{+∞} ([10, Chapter 4, Theorem
1]). This map satisﬁes the following properties:
• vp(c) = +∞ if and only if c = 0;
• vp(ab) = vp(a) + vp(b) for all a, b in C;
• vp(a + b) ≥ min{vp(a), vp(b)} for all a, b in C.

Remark 5. It is important to note that the last property implies : vp(a + b) = min{vp(a), vp(b)}
if vp(a) ̸= vp(b).
We will make a frequent use of this fact.

Lemma 4. [5, Lemma 2.4] Let r ≥ 1 be an integer and p be a prime number. Then vp((pr

j )
) ≥ 1
for 1 ≤ j ≤ pr − 1.

From the relation vp((pr+1
k )) = vp(( pr

k−1
) + (pr

k )
) we immediately deduce :

Lemma 5. Let p be a prime, and suppose N = pr + 1. Then

vp((
N
k
 )) ≥ 1

for 2 ≤ k ≤ N − 2.

Proposition 6. Let p be a prime number and let f be a non-trivial polynomial of degree N =
pr + 1. Assume that f has a common root with f (2), · · · , f (N −1). Let c be the center of mass of
f . Then the following conditions are satisﬁed :
• f ′(c) ̸= 0,
• If p ≥ 3, there is no w ∈ C∗ such that f (c − w) = f (c + w) = 0,
• If p ≥ 3, there is no w ∈ C∗ such that f ′(c − w) = f ′(c + w) = 0.

CONSTRAINTS ON HYPOTHETICAL COUNTEREXAMPLES TO THE CASAS-ALVERO CONJECTURE 7

Proof. We may assume without loss of generality, using Lemma 1, that f is of the form

f (z) = zN + (N
2
 )a2zN −2 + · · · + (
N
k
 )
akzN −k + · · · + (
N
2
 )
aN −2z2 + aN −1z

and that min{vp(zj), j = 1, · · · , N} = 0, where we have denoted by z1, z2, · · · , zN −1, zN = 0
the zeros of f .
For l = 1, · · · , N − 1, we have:

(2) l!
N! f (N −l)(z) = zl + (l
2
)
a2zl−2 + · · · + ( l
k
)akzl−k + · · · + (l
1

)al−1z + al.

Following the proof of [4, Proposition 9], using equality (2) with l = 2, · · · , N − 2 and z the
common root of f (N −l) and f , we prove by induction on l that

(3) vp(al) ≥ 0 for all l = 2, · · · , N − 2.

Let zj be such that vp(zj) = 0. The equality

−aN −1zj = zN
j + (N
2
 )a2zN −2
j + · · · + (
N
k
 )
akzN −k
j + · · · + (
N
2
 )
aN −2z2
j

shows that vp(aN −1) = 0. In particular, f ′(0) ̸= 0. Besides, as aN −1 = ∏N −1
j=0 zj, we have
vp(zj) = 0 for j ∈ {1, · · · , N − 1}.
If p ≥ 3, we can also see that it is not possible to have a non-zero complex number w such
that f (w) = f (−w) = 0. Indeed, otherwise, 0 = f (w) − f (−w) would give the identity :

−aN −1w = (
N
3
 )a3wN −3 + (N
5
 )a5wN −5 + · · · + (
N
3
 )aN −3w3

which contradicts (14).
We can use the same argument to show that there is no complex number w such that f ′(w) =
f ′(−w) = 0. □

Remark 6. For N = p + 1, it has been noted independently by Castryck that there is no
non-trivial CA–polynomial of degree N whose center of mass coincides with its double root
[2, Lemma 9].

From now on, we will assume that f is a non-trivial CA-polynomial of degree N = p + 1
where p ≥ 3 is a prime number.
Using once again Lemma 1, we may assume that

(4)
 



 f (z) = zN + Na1zN −1 + (
N
2 )a2zN −2 + · · · + (N
k )akzN −k + · · · + (
N
2 )aN −2z2,

N = p + 1, min{vp(zj), j = 1, · · · , N} = 0, ,

where we have denoted by z1, · · · , zN −3, zN −2 = zN −1 = 0, zN = −a1 the roots of f .
For l = 1, · · · , N − 1, we have:

8 R. LATERVEER, M. OUNA¨IES

(5) l!
N! f (N −l)(z) = zl + (l
1

)a1zl−1 + (l
2
)
a2zl−2 + · · · + ( l
k
)akzl−k + · · · + (l
1
)
al−1z + al.

Observe that vp(a1) ≥ 0 because −a1 (the center of mass of f ) is one of the roots of f . Once
again following the proof of [4, Proposition 9] and using equality (5) with l = 2, · · · , N − 2 and
z the common root of f (N −l) and f , we prove by induction on l that

(6) vp(al) ≥ 0 for all l = 2, · · · , N − 2.

Let zj be such that vp(zj) = 0. The equality

−Na1zN −1
j = zN
j + (N
2
 )a2zN −2
j + · · · + (
N
k
 )
akzN −k
j + · · · + (
N
2
 )
aN −2z2
j

shows that vp(a1) = 0. Therefore, we may assume without loss of generality that a1 = −1. Then
we can write f (z) = (z − 1)g(z) where

g(z) = (zN −1 − (N − 1)zN −2 + ((
N
2
 )
a2 − (N − 1))zN −3+

((
N
3
 )
a3 + (
N
2
 )
a2 − (N − 1))zN −4 + · · · + ((
N
3
 )
aN −3 + · · · + (N
2
 )
a2 − (N − 1))z2)
.

In view of (6) and Lemma 5, all roots of g have strictly positive valuations (actually greater than
1/(N − 3)). As a consequence, we see that 1 is a simple root of of f and that vp(zj) > 0 for
j = 1, · · · , N − 3.
Whenever f (N −l)(1) ̸= 0, the Casas-Alvero property implies that f (N −l)(zj) = 0 with vp(zj) >
0 and from equality (5) we get vp(al) > 0.
But as
 f (1) = 1 − N + (
N
2
 )
a2 + · · · + (N
k
 )ak + · · · + (
N
2
 )
aN −2 = 0,

there is at least one index 2 ≤ l ≤ N − 2 such that vp(al) = 0. In other words, at least one of the
derivatives f (N −l)(1) = 0. If we put this result together with Proposition 1, we get :

Lemma 6. Let f be a non-trivial CA-polynomial of degree N = p + 1, p prime. Let c be the
center of mass of f . Then the following conditions are satisﬁed :
• f (N −1)(c) = 0,
• f (l)(c) ̸= 0 for at least one l ∈ {2, · · · , N − 2},
• f (k)(c) = 0 for at least one k ∈ {2, · · · , N − 2}.

Let us now go further into the investigation of the orders of the derivatives having the center
of mass as a root.
We may again assume that f is of the form (4) and that a1 = −1.
For the sake of clarity, we will use the notation x ≡ y if vp(x − y) > 0.
In view of Lemma 6, let l1 < l2 < · · · < lm be the indices between 2 and N − 2 such that
f (N −lj )(1) = 0, j = 1, · · · , m.

CONSTRAINTS ON HYPOTHETICAL COUNTEREXAMPLES TO THE CASAS-ALVERO CONJECTURE 9

As observed previously, for all k ∈ {2, · · · , N − 2}, we have vp(ak) ≥ 0. Moreover, if
k /∈ {l1, · · · , lm}, ak ≡ 0.
From equality (5) with z = 1 and l = l1, l2 · · · , lm, we get

(7)
 



 1 − l1 + al1 ≡ 0
1 − l2 + (
l2
l1)al1 + al2 ≡ 0
...
1 − lm + (lm
l1 )al1 + (lm
l2 )al2 + · · · + alm ≡ 0

Now, using that f (1)
p = 0 and that vp(( k
N)
) ≥ 1 for k = 2, · · · , N − 2, we obtain

(8) − 1 +
 (
N
l1)

p al1 + · · · +
 ( N
lm)

p alm ≡ 0.

Now observe that for all 2 ≤ l ≤ N − 2, we have :
(N
l )

p = N(N − 2)(N − 3) · · · (N − (l − 1))
l!

= (p + 1)(p − 1)(p − 2) · · · (p − (l − 2))
l!

= 1
l! (pl−1 + αl−2pl−2 + · · · + α1p) + (−1)l−2(l − 2)!
l!
where α1, · · · , αl−2 are integers.
Therefore: (N
l )

p ≡ (−1)l

l(l − 1) .

Putting equations (7) and (8) together and putting ˜alj = alj
lj(lj −1) , we obtain:

(9)
 



 −1 + l1˜al1 ≡ 0
−1 + (l2−2
l1−2
)l2˜al1 + l2˜al2 ≡ 0
...
−1 + (lm−2
l1−2 )lm˜al1 + (lm−2
l2−2 )lm˜al2 + · · · + lm˜alm ≡ 0
−1 + (−1)l1al1 + (−1)l2˜al2 + · · · + (−1)lm˜alm ≡ 0.

Let us deﬁne the determinant

(10) ∆ =
 







 −1 l1 0 0 · · · 0
−1 (l2−2
l1−2
)l2 l2 0 · · · 0
... ... ... ... ...
−1 (lm−2
l1−2 )lm (
lm−2
l2−2 )lm · · · lm
−1 (−1)l1 (−1)l2 · · · (−1)lm
 






 .

We see that necessarily ∆ = 0. Otherwise, inverting (9), we would get in particular that 1 ≡ 0.
Let us summarize this result by:

10 R. LATERVEER, M. OUNA¨IES

Lemma 7. Let f be a Casas-Alvero polynomial of the form (4) with a1 = −1. Let l1 < l2 <
· · · < lm be the indices between 2 and N − 2 such that f (N −lj )(1) = 0, j = 1, · · · , m and let ∆
the determinant deﬁned by (10). Then p divides ∆.

Proposition 7. Let f be a non-trivial CA-polynomial of degree N = p + 1, p prime. Then there
are at least two indices 2 ≤ l1 < l2 ≤ N − 2 such that f (l1)(c) = f (l2)(c) = 0.

Proof. If not, in virtue of Lemma 6, there exists a unique index 2 ≤ l ≤ N − 2 such that
f (N −l)(c) = 0.
We can assume without loss of generality that f is of the form (4) with a1 = −1 and apply
Lemma 7. Then m = 1 and

(11) ∆ = [ −1 l
−1 (−1)l
 ] = l − (−1)l.

Observe that 1 ≤ l − (−1)l ≤ l + 1 ≤ N − 2 for l ∈ 2, · · · , N − 3.
Besides, N − 2 − (−1)N −2 = N − 3 because N is even.
Finally, there is no way for p to divide ∆ and this contradicts Lemma 7. □

Remark 7. We can actually go a bit further, but the results are not as conclusive. For instance,
let f be a CA-polynomial of degree N = 12, and suppose there are exactly two indices 2 ≤ l1 <
l2 < N − 1 such that f (l1), f (l2) and f (N −1) have a common root. Then applying Lemma 7, we
can check that there are only 4 possibilities for (l1, l2): (l1, l2) must be (3, 8), (5, 6), (6, 8) or
(6, 9).

Remark 8. In [2], Castryck deﬁnes the type of a CA-polynomial f of degree N as follows: Let
{α1, . . . , αk} denote the roots of f . A subset S ⊂ {α1, . . . , αk} is called covering if for each
i = 1, . . . , N − 1, there exists α ∈ S such that f (i)(α) = 0. The type of f is deﬁned as

type(f ) = min{Card S − 1, S covering}.

Castryck establishes that 2 ≤ type(f ) ≤ N − 3
for any non-trivial CA-polynomial f ([2]; the lower bound follows from Proposition 1). Our
result Proposition 7 gives something more: any CA-polynomial f of degree N = p + 1 satisﬁes

type(f ) ≤ N − 4.

In particular, for N = 12, this bound combined with the results of Castryck (loc. cit.) implies
that in order to prove the Casas-Alvero conjecture in degree 12, the only cases remaining to be
checked are polynomials of type 6, 7 and 8.

Our ﬁnal result proves the Casas-Alvero conjecture for degree p + 1 polynomials whose roots
are rational numbers:

Proposition 8. There is no non-trivial CA-polynomial of degree N = p + 1, p ≥ 3 prime, with
rational roots.

CONSTRAINTS ON HYPOTHETICAL COUNTEREXAMPLES TO THE CASAS-ALVERO CONJECTURE 11

Proof. Using the same notations as in the proof of Lemma 4, we may assume that f is of the
form
 f (z) =zN − NzN −1 + (N
2
 )
zN −2

+ · · · + (−1)k−1( N
k − 1
)
zN −k+1 + (
N
k
 )
akzN −k + · · · + (
N
2
 )
aN −2z2,

with vp(zj) ≥ 1 for j = 1, · · · , N − 3. Here, we have denoted by k the smallest index between
2 and N − 2 such that f (N −k)(1) ̸= 0 (we know from Lemma 4 such a k exists).
We introduce the notation
 Sm =
 N −3∑

j=1 zm
j .

Then we have: vp(S1) = vp(N − 1) = 1, and vp(Sj) ≥ 2 for j = 2, · · · , N − 2. Using Newton
formulas (see Lemma 2, l = 0), we obtain

−k(N
k
 )ak =
 k−1∑

j=0 (−1)j(1 + Sk−j)(
N
j
 )

=
 k−1∑

j=0 (−1)j(N
j
 ) +
 k−1∑

j=0(−1)jSk−j
(
N
j
 )

= (−1)k−1(
N − 1
k − 1
 ) +
 k−1∑

j=0(−1)jSk−j
(
N
j
 )
.

Note that vp((
N
k )ak) > 1 which will lead to a contradiction:
Case 1: k = 2. The last equality becomes :

−2(N
2
 )
a2 = −(N − 1) + S2 − NS1 = −(N − 1) + S2 − N(N − 1) = −(N + 1)(N − 1) + S2.

The valuation of the right-hand term is 1.
Case 2: 3 ≤ k ≤ N − 2 : The right-hand term is

(−1)k−1(
N − 1
k − 1
 ) +
 k−2∑

j=0 (−1)jSk−j
(
N
j
 ) + (−1)k−1S1
( N
k − 1
)
.

But vp(Sk−j) ≥ 2 for j = 0, · · · , k − 2, and vp(S1( N
k−1
)) = 2, so the valuation of the right-hand
term is vp((
N −1
k−1 )
) = 1. □

12 R. LATERVEER, M. OUNA¨IES

3. A FINAL REMARK ABOUT A POSSIBLE COUNTEREXAMPLE IN DEGREE 12

Proposition 9. Let f be a non-trivial CA-polynomial of degree N ≥ 1.

1) Assume that some prime q ≥ 2 divides all binomial coefﬁcients (N
k ), k = 1, · · · , N − 1
except for k = qs and k = N − qs = qt, s, t ∈ N. Then the derivatives f (qs) and f (N −qs)

don't have any common root.
2) Assume that some prime q ≥ 2 divides all binomial coefﬁcients (N
k ), k = 1, · · · , N − 1
except for k = l1, · · · , lm. Then there is no a ∈ C such that

f (a) = f l1(a) = · · · = f lm(0).

Remark 9. 1) This implies in particular that s ̸= t. This means that there doesn't exist a no-
trivial CA-polynomial with degree N = 2qr, q prime. But this result is already proved in [5].

Proof. 1) We may assume that s ≤ t and that f and its derivatives are of the form :

(12) l!
N! f (N −l)(z) = zl + (l
1
)
a1zl−1 + · · · + (l
1

)al−1z + al,

with aN = aqs = 0 and min{vq(zj), j = 1, · · · , N} = 0 where we have denoted by
z1, · · · , zN the roots of f .
As in [4, Proposition 9], using equality (12) with l = 1, · · · , N − 1 and z the common
root of f (N −l) and f , we prove by induction on l that

(13) vq(al) ≥ 0 for all l = 1, · · · , N.

Using f (zj) = 0 with vq(zj) = 0, we deduce that vq(aqt) = 0.
Now we apply formula (12) with l = qs then l = N − qs. We ﬁnd, with the help
of Lemma 4, that all roots of f (N −qs) have q-valuation > 0 while all roots of f (qs) have
q-valuation = 0.
2) We proceed by contradiction. Let us repeat the beginning of the proof in 1) but this time
assuming that aN = al1 = · · · = alm = 0. We still get

(14) vq(al) ≥ 0 for all l = 1, · · · , N.

Using f (zj) = 0 with vq(zj) = 0 we have

−zN
j = (
N
1
 )
a1zN −1
j + · · · + ( N
N − 1
)
aN −1zj.

But by assumption, the q-valuation of the right-hand term is ≥ 1 and we reach a contra-
diction. □

Remark 10 (Case N=12). Observe that 2 (respectively 3) divides (12
k )
, k = 1, · · · , 11, except for
k = 4, 8 (resp. k=3,9). Thus, a possible counterexample in degree 12 should satisfy : f (4) and
f (8) (respectively f (3) and f (9)) don't share any root.

CONSTRAINTS ON HYPOTHETICAL COUNTEREXAMPLES TO THE CASAS-ALVERO CONJECTURE 13

REFERENCES

[1] E. Casas-Alvero, Higher order polar germs, Journal of Algebra 240(1) (2001), 326–337,
[2] W. Castryck, Revisiting the computational approach to the Casas-Alvero conjecture, preprint 27-02-2012,
[3] G. Diaz-Toca and L. Gonzalez-Vega, On a conjecture about univariate polynomials and their roots. In
Algorithmic Algebra and Logic 2005 (A. Dolzmann, A. Seidl and T. Sturm, eds.), Norderstedt 2005,
[4] J. Draisma and J. P. de Jong, On the Casas-Alvero conjecture, EMS Newsletter June 2011, 29–33,
[5] H.-C. Graf von Bothmer, O. Labs, J. Schicho and C. van de Woestijne, The Casas-Alvero conjecture for
inﬁnitely many degrees, Journal of Algebra 316(1) (2007), 224–230,
[6] J. P. de Jong, Het Casas-Alvero vermoeden, 19-04-2010,
[7] V. V. Prasolov, Polynomials, Algorithms and Computation in Mathematics Volume 11 Springer,
[8] A. Sudbury, The number of distinct roots of a polynomial and its derivatives, Bull. London Math. Soc., 5
(1973), 13–17,
[9] V. P. Kostov and B.Z. Shapiro, On arrangements of roots for a real hyperbolic polynomial and its deriva-
tives Bull. Sci. math. Volume 126 (2002), 45–60,
[10] P. Ribenboim, The theory of classical valuations, Springer Monographs in Mathematics, Springer–Verlag
New York Berlin Heidelberg 1999,
[11] H. Verhoek, Some remarks about a polynomial conjecture of Casas-Alvero, S´eminaire Bourbakettes, Paris
2009,

INSTITUT DE RECHERCHE MATH ´EMATIQUE AVANC ´EE, UNIVERSIT ´E LOUIS PASTEUR 7 RUE REN ´E DES-

CARTES, 67084 STRASBOURG CEDEX, FRANCE.
E-mail address: robert.laterveer@math.unistra.fr

INSTITUT DE RECHERCHE MATH ´EMATIQUE AVANC ´EE, UNIVERSIT ´E DE STRASBOURG 7 RUE REN ´E DES-
CARTES, 67084 STRASBOURG CEDEX, FRANCE.
E-mail address: myriam.ounaies@math.unistra.fr
