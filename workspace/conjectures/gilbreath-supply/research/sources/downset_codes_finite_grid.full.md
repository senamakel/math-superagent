<!-- source: https://arxiv.org/pdf/1908.07215 | converted from PDF -->

arXiv:1908.07215v1  [cs.CC]  20 Aug 2019
Decoding Downset codes over a grid

Srikanth Srinivasan∗ Utkarsh Tripathi† S. Venkitesh‡

August 21, 2019

Abstract
In a recent paper, Kim and Kopparty (Theory of Computing, 2017) gave a deter-
ministic algorithm for the unique decoding problem for polynomials of bounded total
degree over a general grid S1 × · · · × Sm. We show that their algorithm can be adapted
to solve the unique decoding problem for the general family of Downset codes. Here, a
downset code is speciﬁed by a family D of monomials closed under taking factors: the
corresponding code is the space of evaluations of all polynomials that can be written
as linear combinations of monomials from D.

Polynomial-based codes play an important role in Theoretical Computer Science in gen-
eral and Computational Complexity in particular. Combinatorial and computational char-
acteristics of such codes are crucial in proving many of the landmark results of the area,
including those related to interactive proofs [LFKN92, Sha92, BFL91], hardness of approxi-
mation [ALM
+98], trading hardness for randomness [BFNW93, STV01] etc..
Often, in these applications, we consider polynomials of total degree at most d evaluated
at all points of a ﬁnite grid S = S1 × · · · × Sm ⊆ Fm for some ﬁeld F. When d < k :=
mini{|Si| | i ∈ [m]}, this space of polynomials forms a code of positive distance µ := |S| · (1 −
(d/k)) given by the well-known DeMillo-Lipton-Schwartz-Zippel lemma [DL78, Sch80, Zip79]
(DLSZ lemma from here on).
A natural algorithmic question related to this is the Unique Decoding problem: given
f : S → F that is guaranteed to have (Hamming) distance less than µ/2 from some element
P of the code, can we ﬁnd this P eﬃciently? This problem was solved in full generality only
very recently, by an elegant result of Kim and Kopparty [KK17] who gave a deterministic
polynomial-time algorithm for this problem. We refer to this algorithm as the KK algorithm.
What about the Unique decoding problem when d ≥ k? In this setting, one must be
careful in deﬁning the problem since the space of polynomials of total degree at most d
no longer has positive distance.1 However, one can ensure positive distance by enforcing

∗Department of Mathematics, IIT Bombay. Email: srikanth@math.iitb.ac.in. Supported by SERB
grant MTR/20l7/000958.
†Department of Mathematics, IIT Bombay. Email: utkarshtripathi.math@gmail.com. Supported by
the Ph.D. Scholarship of NBHM, DAE, Government of India.
‡Department of Mathematics, IIT Bombay. Email: venkitesh.mail@gmail.com. Supported by the
Senior Research Fellowship of HRDG, CSIR, Government of India.
1e.g. if d ≥ |Sj|, the non-zero polynomial ∏a∈Sj (Xj − a) of degree at most d vanishes over all of S.

1

additional individual degree constraints: speciﬁcally, we require that the degree of each
variable Xi in the underlying polynomial be strictly smaller than |Si|. With a little bit
of eﬀort, one can check that the KK algorithm can also be adapted to this setting. In
particular, this means that the KK algorithm generalizes a result of Reed [Ree54] from the
1950s, which gives an algorithm for decoding multilinear (i.e. all individual degrees are at
most 1) polynomials over {0, 1}m.
Motivated by this, we try to understand the scope of applicability of the KK algorithm.
Can we show that the KK algorithm works for a cleanly deﬁned general family of codes
encompassing the results above? As a possible answer to this question, we put forward
the class of Downset Codes. A Downset D is a ﬁnite set of monomials (over the variables
X1, . . . , Xm) that is closed under taking factors. The downset code C(S, D) is the code
consisting of all polynomials that can be written as linear combinations of monomials from
D. The space of polynomials of total degree at most d, for example, is clearly a downset code.
But one can also add individual degree constraints, weighted degree constraints, bounds on
the support-size (i.e. number of variables) in any monomial etc.. Downset codes thus yield
a fairly general family of codes.
Furthermore, there is a natural variant of the DLSZ lemma that yields a combinatorial
characterization of the minimum distance of any downset code C(S, D).
2 (The proof of this
lemma uses a classical theorem of Macaulay [Mac27] that reduces the problem of estimating
the size of a ﬁnite variety to counting the number of non-leading monomials in the ideal of
the variety.) It is thus natural to ask if we can solve the unique decoding problem for such
codes.
Our main result is that the KK algorithm can be suitably adapted to yield a deterministic
polynomial-time algorithm that solves the unique decoding problem for any downset code
C(S, D). Furthermore, the algorithm and its proof of correctness are quite clean; in particular,
working in the fairly general setting of downset codes leads to a simple abstract analysis of
the algorithm.

1 Preliminaries

Throughout ﬁx a ﬁeld F. Let S1, . . . , Sm be ﬁnite non-empty subsets of F and let S denote
the grid S1 × S2 × · · · × Sm. We use ki to denote |Si|. Given functions f, g : S → F, we use
∆(f, g) to denote the Hamming distance between f and g, i.e. the number of points where
they diﬀer.
Let M denote the set {0, . . . , k1 − 1} × · · · × {0, . . . , km − 1} with the natural partial
order ≼ . For each α ∈ M, we denote by ∇(α) the set {β ∈ M | α ≼ β} and by ∆(α) the
set {β ∈ M | β ≼ α}. For any α ∈ M, we will identify the monomial Xα := X α1
1 · · · X αm
m
with α and use the monomial notation and the multi-index notation interchangeably.
The following fact is standard.

2In particular, a code C(S, D) has positive distance if and only if all the monomials in D have individual
degree less than ki w.r.t. each variable Xi.
 2

Fact 1. Each f : S → F has a unique representation as a polynomial P (X1, . . . , Xm) where
the degree of Xi in P is at most ki − 1 for each i ∈ [m]. Equivalently, there is a natural
one-one correspondence between the space of all functions from S to F and C(S, M).

Given a downset D ⊆ M, we associate with it the linear code C(S, D), called a downset
code, deﬁned by

C(S, D) = {f : S → F | f can be represented by a linear combination of monomials from D}.

The following lemma allows us to compute the minimum distance µ(S, D) for any downset
D ⊆ M. Recall (see e.g. [CLO07]) that a monomial order on monomials in X1, . . . , Xm is a
total ordering ⊑ of the monomials that is a well order and moreover satisﬁes the following
for any α, β, γ ∈ Nm: Xα ⊑ Xβ ⇒ Xα+γ ⊑ Xβ+γ.

Lemma 2 (Schwartz-Zippel Lemma for C(S, D)). 1. Let f ∈ C(S, M) be arbitrary and
let X α be the leading monomial of f w.r.t. a monomial order. Then, |Supp(f )| ≥
|∇(α)|.

2. For each α ∈ M, there is an f : S → F such that |Supp(f )| = |∇(α)| and f can be
represented by a linear combination of monomials from ∆(α). In particular, if α ∈ D,
then such an f ∈ C(S, D).
Thus, µ(S, D) = minα∈D |∇(α)|. In particular, given D, it can be found in polynomial
time.

Proof. Item 1 is an easy consequence of the proof of Macaulay’s theorem [Mac27] (see
also [CLO07, Chapter 5.3, Proposition 4]). For completeness, we present a short proof
here. Given any polynomial P ∈ F[X1, . . . , Xm], let mSupp(P ) denote the set of monomials
with non-zero coeﬃcient in P . For any set of monomials M′, let ∆(M′) denote the set of
monomials that divide some monomial in M′.
For any i ∈ [m], let fi(Xi) = ∏

a∈Si(Xi − a). Note that fi is a univariate polynomial of
degree ki that vanishes on S. Given any polynomial P ∈ F[X1, . . . , Xm], the remainder Pi
obtained upon dividing P by fi has degree < ki in the variable Xi and evaluates to the same
value as P at points in S. Further, each monomial in mSupp(Pi) divides some monomial in
mSupp(P ) (i.e. mSupp(Pi) ⊆ ∆(mSupp(P ))) . Repeating this process, we eventually obtain
a polynomial ̃P ∈ C(S, M ∩ ∆(mSupp(P ))) representing the same function as P .
Let A be the subset of points in x ∈ S where f (x) = 0. To prove item 1 of the lemma, it
suﬃces to show that every g : A → F can be represented as a polynomial from C(S, M\∇(α)).
Standard linear algebra then implies that |A| ≤ |M| − |∇(α)| = |S| − |∇(α)|, which proves
item 1.
To prove the above, ﬁx any g : A → F. By extending g in an arbitrary way to S, we know
that g can be represented by some polynomial Q ∈ C(S, M). If mSupp(Q) does not contain
any monomial from ∇(α), then we are done. Otherwise, we choose the largest (w.r.t. ⊑)
monomial Xβ ∈ ∇(α) ∩ mSupp(Q). Let a be the coeﬃcient of Xβ in Q.
Assume that f (X) = Xα + f1(X) where LM(f1) < Xα. Multiplying by Xβ−α, we see
that the polynomial Xβ + Xβ−αf1(X) vanishes on A. Note that Q1 = Q − aXβ−αf is a

3

polynomial such that mSupp(Q1) ̸∋ Xβ that also represents the function g at points in A.
Repeating this process, we eventually obtain a polynomial P without any monomials from
∇(Xα) that represents g. The polynomial ̃P (obtained by dividing by fi as mentioned above)
also represents g and furthermore is an element of C(S, M∩∆(mSupp(P )) ⊆ C(S, M\∇(α)).
For item 2, assume that Si = {a
i
1, . . . , a
i
ki} for each i ∈ [m] and consider f (X) =∏

i∈[m] ∏

j≤αi(Xi − a
i
j).

Let ̃M denote {0, . . . , k1 − 1} × · · · × {0, . . . , km−1 − 1} with its natural partial order. Let
̃S denote the set S1 × · · · × Sm−1.
Given a downset D ⊆ M as above, let degm(D) = max{j ∈ [km − 1] | ∃ α ∈ D s.t. αm =
j}. For i ∈ {0, . . . , degm(D)}, deﬁne

Di = {β ∈ ̃M | (β, i) ∈ D}.

The following observation will be useful.

Lemma 3. Let D ⊆ M be any downset, and let d = degm(D).

1. For each i ∈ {0, . . . , d}, Di is a downset in ̃M. Further, we have D0 ⊇ D1 ⊇ · · · ⊇ Dd.

2. For each i ∈ {0, . . . , d}, we have µ(S, D) ≤ µ( ̃S, Di) · µ(Sm, {0, . . . , i}).

Proof. 1. Clear from the deﬁnition, since D is a downset.

2. Let U ∈ C( ̃S, Di) and have weight equal to µ( ̃S, Di), and V ∈ C(Sm, {0, . . . , i}) and
have weight equal to µ(Sm, {0, . . . , i}). Let Xα be any monomial in U(X) and Y j be
any monomial in V (Y ). So Xα ∈ Di and j ∈ {0, . . . , i}. Then by Item 1, Di ⊆ Dj and
so Xα ∈ Dj, that is, XαY j ∈ D. Thus, U · V ∈ C(S, D) and hence, has weight at least
µ(S, D). So we see that
 µ(S, D) ≤ µ( ̃S, Di) · µ(Sm, {0, . . . , i}).

(Note that the quantity µ(Sm, {0, . . . , i}) is the distance of the degree-i Reed-Solomon
code on the set Sm.)
As in the result of Kim and Kopparty, we work with the more general problem of decoding
Weighted functions (or weighted received word). A weighted function over S is a function
w : S → F × [0, 1] or equivalently a pair (f, u) where f : S → F and u : S → [0, 1]. Given a
weighted function w = (f, u) and a function g : S → F, we deﬁne their distance ∆(w, g) by

∆(w, g) = ∑

x:f (x)=g(x)
 u(x)
2 + ∑

x:f (x)̸=g(x)
 (
1 − u(x)
2
 ) .

A (unweighted) function h : S → F is identiﬁed with the weighted function (h, u) where u is
the identically zero function. Note that with this identiﬁcation, ∆((h, u), g) agrees with the

4

standard Hamming distance ∆(h, g) between h and g. In particular, the unique decoding
problem for C(S, D) immediately reduces to the problem of ﬁnding a codeword of distance
less than µ(S, D)/2 from a given weighted function.
We will also need the following lemma about weighted codewords of a downset code
C(S, D). The proof (in a more general setting) can be found in [KK17, Lemma 2.1].

Lemma 4. Assume that G, H ∈ C(S, D) are distinct.3 Let f : S → F × [0, 1] be any weighted
received word. Then, ∆(f, G) + ∆(f, H) ≥ ∆(G, H) ≥ µ(S, D). In particular, both G and H
cannot be at distance strictly less than µ(S, D)/2 from f .

2 The main theorem

Theorem 5. There is a deterministic polynomial time algorithm that given, S, D and a
weighted codeword w : S → F × [0, 1] produces a codeword C ∈ C(S, D) such that ∆(w, C) <
µ(S, D)/2, if one exists. (If no such codeword C exists, the algorithm outputs some arbitrary
polynomial.)

For the case when m = 1, a result of Forney [Jr.66] yields a deterministic polynomial-time
algorithm for this problem. We call this algorithm WeightedRSDecoder and refer the reader
to [Jr.66] or [KK17] for a description.

Proof. The algorithm is speciﬁed as WeightedDownsetDecoder below (Algorithm 1). We
prove its correctness by induction on m.
For the base case m = 1, we simply use the algorithm WeightedRSDecoder and so there
is nothing to prove.
Now we assume the correctness of WeightedDownsetDecoder algorithm for m − 1 indeter-
minates.
Let w : S → F × [0, 1] be a received weighted word. Suppose there is a C ∈ C(S, D) with
∆(w, C) < µ(S, D)/2. We can write

C(X, Y ) =
 d∑

i=0 Pi(X)Y d−i,

where d = degm(D) as in Algorithm 1.
We show, by induction on i ∈ {0, . . . , d}, that the algorithm correctly decodes the poly-
nomial Pi(X). In other words, for each i ∈ {0, . . . , d}, the polynomial Qi(X) computed by
Algorithm 1 is the same as the polynomial Pi(X).
Fix i ∈ {0, . . . , d}. Assume that the algorithm has correctly decoded Pj(X) for each
j < i. Let Ci(X, Y ) = ∑d
j=i Pj(X)Y d−j. Note that Pj ∈ C( ̃S, Dd−j), for all j ∈ {0, . . . , d}.
To show that Qi(X) = Pi(X), it is enough to show that ∆(fi, Pi) < µ( ̃S, Dd−i)/2 where
fi is as computed by the algorithm. Then, the induction hypothesis implies that Qi(X) =
Pi(X).

3In the algorithm, we will only need this for m = 1, i.e. for the Reed-Solomon code.

5

Algorithm 1 WeightedDownsetDecoder: Decoding a downset code over a grid

1: Input: (S, D, w), where

• S = S1 × · · · × Sm is a ﬁnite grid in Fn with ki = |Si|. ⊲ We have
̃S = S1 × · · · × Sm−1.

• D ⊆ M is a downset.

• w : S → F × [0, 1] is a weighted received word.

2: if m = 1 then
3: return WeightedRSDecoder(S, D, w). ⊲ Here S ⊆ F and D = {0, . . . , d}, for some d.
4: else
5: Deﬁne r : S → F and u : S → [0, 1] by

w(x, y) = (r(x, y), u(x, y)), for all (x, y) ∈ ̃S × Sm.

6: for i = 0, . . . , d = degm(D) do
7: Deﬁne wi : S → F × [0, 1] by

wi(x, y) =
 (
r(x, y) −
 i−1∑

j=0 Qj(x)yd−j, u(x, y)
)
 , for all (x, y) ∈ ̃S × Sm.

8: for x ∈ ̃S do
9: Deﬁne wi,x : Sm → F by wi,x(y) = w(x, y), for all (x, y) ∈ ̃S × Sm.
10: Let Gx(Y ) = WeightedRSDecoder(Sm, {0, . . . , d − i}, wi,x) ∈ F[Y ].
11: if ∆(wi,x, Gx) < µ(Sm, {0, . . . , d − i})/2 then
12: σx = coeﬀ(Y d−i, Gx(Y )).
13: δx = ∆(wi,x, Gx).
14: else
15: σx = 0.
16: δx = µ(Sm, {0, . . . , d − i})/2.
17: end if
18: end for
19: Deﬁne weighted word fi : ̃S → F × [0, 1] and δi : ̃S → [0, 1] by

fi(x) = (
σx, δx
µ(Sm, {0, . . . , d − i})/2
) = (σx, δi(x)).

20: Let Qi(X) = WeightedDownsetDecoder( ̃S, Dd−i, fi).
21: end for
22: return ∑d
i=0 Qi(X)Y d−i.
23: end if
 6

Deﬁne wi : S → F × [0, 1] as in the algorithm by

wi(x, y) =
 (
r(x, y) −
 i−1∑

j=0 Qj(x)yd−j, u(x, y)
)
 =: (ri(x, y), ui(x, y)), for all (x, y) ∈ ̃S×Sm.

By induction, we know that Qj(X) = Pj(X) for j < i. Hence, we observe that

ri(X, Y ) − Ci(X, Y ) = (ri(X, Y ) +
 i−1∑

j=0 Pj(X)Y d−j) − (
Ci(X, Y ) +
 i−1∑

j=0 Pj(X)Y d−j)

= (ri(X, Y ) +
 i−1∑

j=0 Qj(X)Y d−j) − C(X, Y )

= r(X, Y ) − C(X, Y ).

Hence, ∆(wi, Ci) = ∆(w, C) < µ(S, D)/2.
We now analyze ∆(fi, Pi). Recall that we have

∆(fi, Pi) = ∑

x∈ ̃S:σx=Pi(x)
 δi(x)
2 + ∑

x∈ ̃S:σx̸=Pi(x)
 (
1 − δi(x)
2
 ) .

Fix some x ∈ ̃S. Deﬁne Ci,x(Y ) = Ci(x, Y ). Also, deﬁne

∆(fi(x), Pi(x)) =
 



δi(x)
2 , σx = Pi(x)

1 − δi(x)
2 , σx ̸= Pi(x)

We claim that
 ∆(fi(x), Pi(x)) ≤ ∆(wi,x, Ci,x)
µ(Sm, {0, . . . , d − i}) . (1)

We prove (1) by a case analysis.

(a) δi(x) = 1.

This implies that ∆(wi,x, Gx) ≥ µ(Sm, {0, . . . , d − i})/2. In particular, this implies that
∆(wi,x, Ci,x) ≥ µ(Sm, {0, . . . , d − i})/2 since otherwise the Reed-Solomon decoder would
have returned Ci,x instead of Gx. This immediately implies (1).

So from now we will assume that δi(x) = ∆(wi,x, Gx)/(µ(Sm, {0, . . . , d − i})/2) < 1. By
Lemma 4, it follows that ∆(wi,x, Ci,x) ≥ µ(Sm, {0, . . . , d − i})/2 > ∆(wi,x, Gx).

(b) δi(x) < 1 and σx = Pi(x).

In this case, we immediately have

∆(fi(x), Pi(x)) = δi(x)
2 = ∆(wi,x, Gx)
µ(Sm, {0, . . . , d − i}) ≤ ∆(wi,x, Ci,x)
µ(Sm, {0, . . . , d − i}) .

7

(c) δi(x) < 1 and σx ̸= Pi(x).

As in the previous case, we have δi(x)
2 = ∆(wi,x, Gx)
µ(Sm, {0, . . . , d − i}) . But as σx ̸= Pi(x),

we have Gx ̸= Ci,x. Thus, by Lemma 4, it follows that ∆(wi,x, Ci,x) + ∆(wi,x, Gx) ≥
µ(Sm, {0, . . . , d − i}). Hence

∆(fi(x), Pi(x)) = 1−δi(x)
2 = µ(Sm, {0, . . . , d − i}) − ∆(wi,x, Gx)
µ(Sm, {0, . . . , d − i}) ≤ ∆(wi,x, Ci,x)
µ(Sm, {0, . . . , d − i}) .

This concludes the proof of (1). Using (1), we get

∆(fi, Pi) = ∑

x∈ ̃S ∆(fi(x), Pi(x)) ≤ ∑

x∈ ̃S
 ∆(wi,x, Ci,x)
µ(Sm, {0, . . . , d − i})

= ∆(wi, Ci)
µ(Sm, {0, . . . , d − i}) = ∆(w, C)
µ(Sm, {0, . . . , d − i})

< µ(S, D)
2µ(Sm, {0, . . . , d − i})

≤ µ( ̃S, Dd−i)
2 , by Lemma 3 Item 2.

This completes the proof.

Acknowledgments. The authors are grateful to Swastik Kopparty and Madhu Sudan for
their helpful comments and encouragement.

References

[ALM
+98] Sanjeev Arora, Carsten Lund, Rajeev Motwani, Madhu Sudan, and Mario
Szegedy. Proof veriﬁcation and the hardness of approximation problems. J.
ACM, 45(3):501–555, 1998.

[BFL91] L´aszl´o Babai, Lance Fortnow, and Carsten Lund. Non-deterministic exponential
time has two-prover interactive protocols. Computational Complexity, 1:3–40,
1991.

[BFNW93] L´aszl´o Babai, Lance Fortnow, Noam Nisan, and Avi Wigderson. BPP has subex-
ponential time simulations unless EXPTIME has publishable proofs. Computa-
tional Complexity, 3:307–318, 1993.

[CLO07] David Cox, John Little, and Donal O’Shea. Ideals, varieties, and algorithms.
Undergraduate Texts in Mathematics. Springer, New York, third edition, 2007.
An introduction to computational algebraic geometry and commutative algebra.

8

[DL78] Richard A. DeMillo and Richard J. Lipton. A probabilistic remark on algebraic
program testing. Inf. Process. Lett., 7(4):193–195, 1978.

[Jr.66] G. David Forney Jr. Generalized minimum distance decoding. IEEE Trans.
Information Theory, 12(2):125–131, 1966.

[KK17] John Y. Kim and Swastik Kopparty. Decoding reed-muller codes over product
sets. Theory of Computing, 13(21):1–38, 2017.

[LFKN92] Carsten Lund, Lance Fortnow, Howard J. Karloﬀ, and Noam Nisan. Algebraic
methods for interactive proof systems. J. ACM, 39(4):859–868, 1992.

[Mac27] F. S. Macaulay. Some properties of enumeration in the theory of modular sys-
tems. Proceedings of the London Mathematical Society, s2-26(1):531–555, 1927.

[Ree54] Irving S. Reed. A class of multiple-error-correcting codes and the decoding
scheme. Trans. of the IRE Professional Group on Information Theory (TIT),
4:38–49, 1954.

[Sch80] Jacob T. Schwartz. Fast probabilistic algorithms for veriﬁcation of polynomial
identities. J. ACM, 27(4):701–717, 1980.

[Sha92] Adi Shamir. IP = PSPACE. J. ACM, 39(4):869–877, 1992.

[STV01] Madhu Sudan, Luca Trevisan, and Salil P. Vadhan. Pseudorandom generators
without the XOR lemma. J. Comput. Syst. Sci., 62(2):236–266, 2001.

[Zip79] Richard Zippel. Probabilistic algorithms for sparse polynomials. In Symbolic
and Algebraic Computation, EUROSAM ’79, An International Symposiumon
Symbolic and Algebraic Computation, Marseille, France, June 1979, Proceedings,
pages 216–226, 1979.
 9
