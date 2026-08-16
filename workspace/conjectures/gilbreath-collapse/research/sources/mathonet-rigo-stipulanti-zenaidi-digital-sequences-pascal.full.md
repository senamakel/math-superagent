<!-- source: https://arxiv.org/pdf/2201.06636 | converted from PDF -->

ON DIGITAL SEQUENCES ASSOCIATED WITH PASCAL’S
TRIANGLE

P. MATHONET, M. RIGO, M. STIPULANTI, AND N. ZENA¨IDI

Abstract. We consider the sequence of integers whose nth term has base-p
expansion given by the nth row of Pascal’s triangle modulo p (where p is a
prime number). We ﬁrst present and generalize well-known relations concern-
ing this sequence. Then, with the great help of Sloane’s On-Line Encyclopedia
of Integer Sequences, we show that it appears naturally as a subsequence of
a 2-regular sequence. Its study provides interesting relations and surprisingly
involves odious and evil numbers, Nim-sum and even Gray codes. Further-
more, we examine similar sequences emerging from prime numbers involving
alternating sum-of-digits modulo p. This note ends with a discussion about
Pascal’s pyramid involving trinomial coeﬃcients.

1. Introduction

The problem of determining the number of sides of constructible regular poly-
gons (with straightedge and compass) has captivated geometers for centuries. The
Gauss–Wantzel theorem [10] translates this question in the framework of number
theory: it states that a regular n-sided polygon is constructible if and only if n is
the product of a power of 2 and any number (possibly none) of distinct Fermat
primes i.e., primes of the form Fl := 2
2
l + 1, l ≥ 0.
The sequence of (ordered) products of Fermat numbers
1 (f2,n)n≥0, starting with

1, 3, 5, 15, 17, 51, 85, 255, 257, 771, 1285, 3855, 4369, 13107, 21845, 65535, 65537, . . .

actually appears as entry A001317 in Sloane’s Encyclopedia [20]. Note that the
sequence of Fermat primes, which appears in the OEIS [20] under entry A019434,
is not completely known: the primality of Fermat numbers is in general an open
problem and only the numbers F0, F1, . . . , F4 (that have been underlined here) are
known to be prime.
This sequence has in turn intriguing properties from the point of view of comi-
natorics. It turns out that it can be extracted from Pascal’s triangle. Indeed, for
any prime number p, we can consider the elements of Pascal’s triangle modulo p,(n
i ) mod p, where for any integer k, we let k mod p or even [k%p] denote the unique
integer in {0, . . . , p − 1} congruent to k modulo p. For instance, for p = 2, we get
[(
n
i
 ) mod p
]
 n≥0,
0≤i≤n = 1|1, 1|1, 0, 1|1, 1, 1, 1|1, 0, 0, 0, 1|1, 1, 0, 0, 1, 1| · · ·

where bars separate consecutive terms in the sequence. We thus ﬁnd Sierpi´nski’s
triangle (the usual Pascal’s triangle modulo 2).
Identifying each row of the triangle to an integer through the base p-expansion,
we get the sequence (tp,n)n≥0 deﬁned, for n ≥ 0, by

tp,n =
 n∑

i=0
 [(
n
i
 ) mod p
] p
i.

1The sequence starts with the product of no such numbers which is 1 by convention.

1arXiv:2201.06636v1  [math.NT]  17 Jan 2022
2 P. MATHONET, M. RIGO, M. STIPULANTI, AND N. ZENA¨IDI

These numbers t2,n are sometimes called Roberts’ numbers [12]. It is easily seen
from the examples above that the ﬁrst few terms of the sequences f2,n and t2,n
coincide. It was observed by several authors that the sequences are indeed equal.
Conway and Guy refer to Gardner [9, 11]. Investigating connections of Fermat
numbers with Pascal’s triangle, Krizek et al. in their monograph [16, Chap. 8]
mention the earlier work of Hewgill [14].
For p = 3, the sequence t3,n also appears in the OEIS [20] as entry A173019

(t3,n)n≥0 = 1, 4, 16, 28, 112, 448, 784, 3136, 12301, 19684, 78736, 314944, . . . .

It turns out that it no longer coincides with the natural generalization f3,n of f2,n
deﬁned as the (ordered) products of numbers of the form 33
l + 1, l ≥ 0.
In Section 2, considering the nth row of Pascal’s triangle mod p, we write n =
nk pk +s where p
k is the largest power of p smaller or equal to n, nk ∈ {1, . . . , p−1}
and s = n mod p
k. We give a simple formula that expresses tp,n from tp,s. This
formula enables us to recover the equality of the sequences f2,n and t2,n and explain
why in general fp,n ̸= tp,n. We also interpret this formula in terms of self-similarity
of Pascal’s triangle mod p.
In Section 3, we consider another approach: we study polynomial identities whose
evaluation at the speciﬁc value p gives the sequence (tp,n)n≥0. Evaluations at other
values give generalized versions of these sequences having similar properties.
In Section 4, we start with the simple observation
2 that t2,n+1 = t2,n ⊕ (2 t2,n)
where ⊕ is the classical Nim-sum (addition digit-wise modulo 2 without carry).
This leads us to study another related sequence (N (m))m≥0 := (m ⊕ 2m)m≥0 of
which (t2,n)n≥0 is a subsequence, and more generally, the sequence (Np(m))m≥0 :=
(m ⊕p p m)m≥0, where ⊕p is addition digit-wise modulo p without carry. We show
that Np(m) is a p-regular sequence whereas tp,n is not.
In Section 5, we consider a particular partition of the set {N (m) | m ≥ 1}.
It turns out that (N (m))m≥0 is a well-understood permutation of the sequence of
evil numbers, those numbers whose base-2 expansions have an even number of ones
(i.e., the characteristic sequence of the considered set is given by the Thue–Morse
sequence). We then naturally extend this result to any prime p by showing that
the characteristic sequence of the set {Np(m) | m ≥ 0} is a generalization of the
Thue–Morse sequence: it is the set of numbers whose alternate sum-of-digit is zero
modulo p. Finally, in [2], an exact formula for the summatory function of evil
numbers is given. Here we consider the summatory function of (N (m))m≥0 taking
advantage of the known permutation.
In Section 6, we examine the problem in three dimensions and consider Pascal’s
pyramid made of trinomial coeﬃcients. We deﬁne a sequence analogous to tp,n:
when the pyramid is intersected with convenient planes whose equation is of the
form x+y+z = n for some integer n, we get rows of coeﬃcients modulo p. Similarly
to what is done in Section 2, we derive a recurrence relation for the corresponding
integer sequence. Finally we study the relation existing between coeﬃcients modulo
p occurring at speciﬁc positions. In particular, we show that Pascal’s pyramid
modulo p is p-automatic.
Note that, in this text, appear the sequences A001317, A001969, A003188, A019434,
A048724, A071770, A173019 and A242399 from the OEIS [20].

2It follows directly from Pascal’s rule.

ON DIGITAL SEQUENCES ASSOCIATED WITH PASCAL’S TRIANGLE 3

2. A recursive formula

In this section, for any prime p, considering an index n ̸= 0 whose base p-
expansion is n = ∑k
ℓ=0 nℓp
ℓ, with nk ̸= 0, we let repp(n) denote the base-p rep-
resentation of the integer n > 0 i.e., the word
3 nk · · · n0 over {0, . . . , p − 1}. We
also decompose n as n = nk pk + s where 0 < nk < p and s = n mod pk. With
Theorem 3 we describe a formula to compute tp,n from tp,s. We essentially follow
the same description as in [12], which makes use of Lucas’ theorem, which we now
recall.

Theorem 1 (Lucas). Let p ≥ 2 be a prime and let m, n be non-negative integers.
If repp(m) = mk · · · m0 and repp(n) = nk · · · n04, then
(m
n
 ) ≡
 k∏

j=0
 (
mj
nj
 ) (mod p),

with the convention that (a
b) = 0 if a < b.

In our situation, we use this theorem to compute (n
i ) for n = ∑k
ℓ=0 nℓp
ℓ, with
nk ̸= 0 and i ≤ n. We write i = ∑k
ℓ=0 iℓp
ℓ (allowing leading zeroes whenever
i < p
k) and since i ≤ n, we have 0 ≤ ik ≤ nk. From Lucas’ theorem, we then have

(1) (
n
i
 ) ≡ (nk
ik
 )(n mod p
k

i mod pk
 ) (mod p).

Proposition 2. If n = ∑k
ℓ=0 nℓpℓ with nk ̸= 0 and if s = n mod pk, then we have

(2) tp,n =
 nk∑

m=0
 

 s∑

j=0
 ((nk
m
 )(s
j
) mod p) p
j


 pmp
k .

Proof. By deﬁnition and Equation (1) (and using the same notation) we have

tp,n =
 n∑

i=0
 [(n
i
 ) mod p] p
i =
 n∑

i=0
 [(
nk
ik
 )(n mod p
k

i mod pk
 ) mod p
] p
i.

In order to conclude, it is suﬃcient to observe that the set of indices i ≤ n satisfying
the condition (nk
ik )(n mod pk

i mod pk ) ̸= 0 mod p is precisely the set of those indices i which
satisfy the same condition and decompose as i = ik p
k + (i mod p
k), with ik ≤ nk,
i mod pk ≤ s. We thus have

tp,n =
 nk∑

m=0
 

 s∑

j=0
 (
nk
m
 )(s
j
) mod p



 pmp
k+j,

and the result follows. □

We now interpret Proposition 2 as a recursive formula relating tp,n and tp,s. We
simply observe that the expression within brackets in (2) is obtained by multiplying
each digit of repp(tp,s) by (nk
m ) and then taking the remainder mod p. In order to
express this fact, we introduce some notation.
We denote by Z/(pZ) or simply Zp the ﬁeld of integers modulo p. The canonical
projection π : Z → Zp induces a bijection from Z<p = {0, . . . , p − 1} to Zp and
enables the deﬁnitions of operations on Z<p for which π is an isomorphism. These

3By convention, 0 is represented by the empty word ε.
4With the convention that the shortest representation is padded with extra leading zeroes as
most signiﬁcant digits when the two base-p representations have diﬀerent lengths.

4 P. MATHONET, M. RIGO, M. STIPULANTI, AND N. ZENA¨IDI

are simply the addition and multiplication mod p. For integers 0 ≤ b ≤ a such that(a
b) ̸= 0 (mod p) we let µa,b denote the one-to-one correspondence

µa,b : Z<p → Z<p : x ↦→ (a
b
) · x mod p.

This map is a permutation of Z<p since it corresponds via π to the left multiplication
by the class of (a
b) ̸= 0 in Zp. Also, we have µa,b(x) = 0 if and only if x = 0. This
fact will be extensively used in this text (notably in Section 6). Note also that for
b = 0 or a = b, µa,b is just the identity. We extend this map to a morphism of the
free monoid {0, . . . , p − 1}
∗ equipped with concatenation by setting

µa,b(zm · · · z0) = µa,b(zm) · · · µa,b(z0).

Finally, for a ﬁnite sequence δk · · · δ0 of digits in {0, . . . , p − 1}, we let valp(δk · · · δ0)
denote the p-evaluation ∑k
i=0 δi p
i. We are now able to translate Proposition 2.

Theorem 3. If n = ∑k
ℓ=0 nℓp
ℓ with nk ̸= 0 and if s = n mod p
k, then we have

(3) tp,n =
 nk∑

m=0 p
mpk valp(µnk,m(repp(tp,s))).

Proof. By deﬁnition, we have repp(tp,s) = ((s
j) mod p)j=0,...,s. Then we compute

µnk,m(repp(tp,s)) = (
(nk
m
 ) (
s
j
) mod p)j=0,...,s

and ﬁnally
 valp(µnk,m(repp(tp,s))) =
 s∑

j=0((nk
m
 ) (
s
j
) mod p)pj,

and the result follows from Proposition 2. □

Theorem 3 now has an interpretation in terms of the rows of Pascal’s triangle
mod p, as follows. We start indexing rows and columns of Pascal’s triangle at
0. The nth row of this triangle is nothing but repp(tp,n) and the sth is the word
Ps := repp(tp,s) := ts,0 · · · ts,s made of s+1 entries over Z<p. Equation (3) suggests
to work with words of length pk, so we pad this row with trailing zeroes:

Qs := ts,0 · · · ts,s 0 · · · 0︸ ︷︷ ︸
pk−s−1 .

Example 4. Let p = 5 and n = 23. We have rep5(23) = 43 thus k = 1, n1 = 4
and s = 3. The third row of Pascal’s triangle (modulo 5) is with 1, 3, 3, 1, so
P3 = 1331 and Q3 = 13310 (see Figure 1 where diﬀerent colors represent diﬀerent
values modulo 5).

From Theorem 3 we directly obtain

Pn = µnk,0(Qs) µnk,1(Qs) · · · µnk,nk−1(Qs) µnk,nk (Ps).

Figure 1. The ﬁrst ﬁve rows of Pascal’s triangle mod 5.

ON DIGITAL SEQUENCES ASSOCIATED WITH PASCAL’S TRIANGLE 5

By deﬁnition of Qs, we have

Pn = µnk,0(Ps)0
pk−s−1µnk,1(Ps)0
pk−s−1 · · · µnk,nk−1(Ps)0pk−s−1µnk,nk (Ps).

For instance, the third row will help describe the 23rd row, for which

P23 = 133104224013310422401331

(see Figure 2). Similarly, for the row with index 48, we have rep5(48) = 143 thus

Figure 2. The rows 20 ≤ i ≤ 24 of Pascal’s triangle mod 5.

k = 2, nk = 1 and s = 23. So P48 is described in terms of P23 and therefore in
terms of P3 and Q3 (see Figure 3).

Figure 3. The rows 45 ≤ i ≤ 49 of Pascal’s triangle mod 5.

For the special case p = 2, we have nk = 1, no permutation is needed in Theorem
3 because µ1,0 = µ1,1 is the identity. Also, in Equation (2), with p = 2 and nk = 1,
the sum is restricted to two terms giving the kth Fermat number times t2,s. So
from Theorem 3 or Proposition 2, we recover the following result.

Corollary 5. For all k ≥ 0 and all 0 ≤ s < 2
k, we have

t2,2k+s = (2
2k + 1) t2,s.

From this corollary, one deduces that [4, p. 113] (an unpublished result attributed
to Larry Roberts) for n ≥ 1,

(4) t2,n = ∏

j:nj =1
(2
2j + 1),

which is the product of the Fermat numbers for those indices that occur in the
base-2 expansion of n. In particular, since the base-2 expansions of 2n and 2n + 1
only diﬀer by their last digit, we have

(5) t2,2n+1
t2,2n = 2
2
0 + 1 = 3

which is the ﬁrst Fermat number F0.

2.1. A variant sequence. If one only looks at the zero or non-zero binomial
coeﬃcients modulo p (so, considering only divisibility by p as, for instance, in [13]),
we can study the sequence

t′
p,n =
 n∑

i=0 sgn [(
n
i
 ) mod p
] 2
i

6 P. MATHONET, M. RIGO, M. STIPULANTI, AND N. ZENA¨IDI

where the sign function maps any non-zero value to 1 (and 0 to 0). For instance,
t2,n = t
′
2,n and the ﬁrst few terms of (t
′
3,n)n≥0 are

1, 3, 7, 9, 27, 63, 73, 219, 511, 513, 1539, 3591, 4617, . . . .

In that case, we can directly adapt Equation (2) where the multiplication by (nk
m )

is no more necessary, or in Theorem 3 where there is no permutation to consider,
and we get the following result.

Proposition 6. If n = ∑k
ℓ=0 nℓp
ℓ with nk ̸= 0 and if s = n mod pk, then we have

t
′
p,n = t
′
p,s
 nk∑

m=0 2mp
k .

3. Polynomial identities

As a preliminary, we state a classical result about formal power series

∞∏

i=0
(1 + X pi + X 2pi + · · · + X (p−1)pi) =
 ∞∑

n=0 X n.

Expanding the left-hand side, we see that this result is equivalent to the fact that
every integer has a unique base-p expansion. In this section, we will often make use
of similar arguments to obtain polynomial identities. Our developments are based
on [16] (also see [14]).
We will consider the polynomial rings Z[X] and Zp[X] over Z and Zp respectively.
The canonical projection π : Z → Zp : n ↦→ [n]p extends to a ring homomorphism
from Z[X] to Zp[X], wich we also denote by π. Note that the restriction of this map
to the subset Z<p[X] of Z[X] made of polynomials with coeﬃcients in {0, . . . , p−1}
is injective. Using this notion, we are able to present the following result, which
was already noticed on several occasions for p = 2.

Proposition 7. If n = ∑k
ℓ=0 nℓp
ℓ with nk ̸= 0 and if ∏k
i=0 (ni
δi ) < p for all indices
δ0, . . . , δk, then we have

(6)
 n∑

j=0
 [(n
j
 ) mod p] X j =
 k∏

i=0
(1 + X pi)
ni

in Z[X].

Proof. We ﬁrst observe that both polynomials

(7) Pn(X) =
 n∑

j=0
 [(
n
j
 ) mod p
] X j and Qn(X) =
 k∏

i=0
(1 + X pi)
ni

have the same projection in Zp[X]. Indeed, on the one hand, we have

π (Pn(X)) =
 n∑

j=0
 [(
n
j
 )]
p X j = π ((1 + X)n) .

On the other hand, using that π is a ring homomorphism and taking into account
the equalities π((1 + X)
pi) = π(1 + X pi), for i ∈ N, we ﬁnd

π(Qn(X)) = π
 ( k∏

i=0
 (1 + X pi)ni)
 = π
 ( k∏

i=0
(1 + X)
nipi)
 = π ((1 + X)
n) .

ON DIGITAL SEQUENCES ASSOCIATED WITH PASCAL’S TRIANGLE 7

Secondly, we check that the polynomials Pn(X) and Qn(X) have coeﬃcients in
Z<p. Since it is direct for Pn(X), we concentrate on Qn(X) and ﬁnd

k∏

i=0
 (1 + X pi)ni =
 k∏

i=0
 ni∑

δi=0
 (
ni
δi
 )X δip
i =
 nk∑

δk=0 . . .
 n0∑

δ0=0
 ( k∏

i=0
 (ni
δi
 ))
 X δkpk+...+δ0.

Using the uniqueness of the base-p expansion of every integer together with the as-
sumption of the proposition, we obtain that Qn(X) belongs Z<p[X]. The conclusion
then follows from the injectivity of the restriction of π to this set. □

Remark 8. For p = 2, the assumption (nk
δk ) · · · (n0
δ0 ) < 2 of Proposition 7 always
holds because ni ≤ 1 and thus (ni
δi ) ≤ 1 for all i. Evaluating (6) at X = 2, we get

back t2,n = ∏k
i=0(22
i + 1)ni, which is (4).
We even get a family of sequences by evaluating this polynomials identity at
other values of X. For instance, for X = 3, the ﬁrst few terms of the corresponding
sequence are
 1, 4, 10, 40, 82, 328, 820, 3280, 6562, 26248, 65620, . . .

and of course, such a sequence (xn)n≥0 satisﬁes

x2i+s = (3
2
i + 1) xs.

Remark 9. On the other hand, for p = 3, (ni
δi ) = 2 whenever ni = 2 and δi = 1. In
all other situations, the corresponding binomial coeﬃcient is 1. So (nk
δk ) · · · (n0
δ0 ) < 3
holds for all δi if and only if at most one digit ni = 2 occurs. Precisely,
(nk
δk
 ) · · · (n0
δ0
 ) = 2
#{i:(ni,δi)=(2,1)}.

Let p ≥ 3. If the condition in Proposition 7 is not met, then the polynomials Pn(X)
and Qn(X) (deﬁned in Equation (7)) are no longer equal and we have a non-zero
diﬀerence in Z[X] expressed as

k∏

i=0
(1 + X pi)
ni −
 n∑

j=0
 [(
n
j
 ) mod p
] X j

=
 nk∑

δk=0 · · ·
 n0∑

δ0=0
 {(
nk
δk
 ) · · · (n0
δ0
 ) − [( n
valp(δk pk + · · · + δ0)
) mod p]} X δk pk+···+δ0 .

Let us denote the latter polynomial by κp,n(X). Otherwise stated, we get

n∑

j=0
 [(n
j
 ) mod p
] X j =
 k∏

i=0
(1 + X pi)
ni − κp,n(X).

Remark 10. Let us write n = nk pk + · · · + n1 p + n0 with ni ∈ {0, . . . , p − 1} for
all 0 ≤ i ≤ k. Hence pn + 1 = nk pk+1 + · · · + n1 p2 + n0 p + 1. Let us compare the
polynomials
 pn∑

j=0
 [(pn
j
 ) mod p
] X j and
 pn+1∑

j=0
 [(pn + 1
j
 ) mod p
] X j

over Z[X]. The second one is equal to

(1 + X)
 k∏

i=0(1 + X pi+1)ni − κp,pn+1(X).

8 P. MATHONET, M. RIGO, M. STIPULANTI, AND N. ZENA¨IDI

We can rewrite κp,pn+1(X) as

nk∑

δk=0 · · ·
 n0∑

δ0=0
 1∑

j=0
{(nk
δk
 ) · · · (
n0
δ0
 )(1
j
) − [( pn + 1
valp(δk pk+1 + · · · + δ0 p + j)

) mod p
]}

X δk pk+1+···+δ0 p+j.

Since (1
j) = 1, Lucas’ theorem gives
( pn + 1
valp(δk pk+1 + · · · + δ0 p + j)
) ≡ ( pn
valp(δk pk+1 + · · · + δ0 p)

) (mod p).

We conclude that κp,pn+1(X) = (1 + X) · κp,pn(X). Consequently, we have

pn+1∑

j=0
 [(
pn + 1
j
 ) mod p] X j = (1 + X) ·
 ( k∏

i=0(1 + X pi+1)ni − κp,pn(X)
)

= (1 + X) ·
 pn∑

j=0
 [(
pn
j
 ) mod p] X j.

Evaluating this polynomial at X = p, we generalize (5) to
tp,pn+1
tp,pn = p + 1.

Notice that we can carry these computations because (1
j) = 1. Considering pn+r
with r > 1 is therefore trickier.

4. A Nim interlude

Let k ≥ 2 be an integer. Recall that a sequence (xn)n≥0 of integers is k-regular
if the Z-module generated by the set of subsequences

{(xken+r)n≥0 | e ≥ 0, 0 ≤ r < ke}

is ﬁnitely generated, i.e., these subsequences are linear combinations of a ﬁnite num-
ber of sequences. This notion extends to multidimensional sequences. In particular,
a bidimensional sequence (xm,n)m,n≥0 is k-regular if the Z-module generated by the
set of subsequences
{(xkem+r,ken+s)m,n≥0 | e ≥ 0, 0 ≤ r, s < ke}

is ﬁnitely generated. See [4, Chap. 14,16].
Let us focus again on t2,n. In this section, we show that the sequence (t2,n)n≥1
naturally appears as a subsequence of a well-studied 2-regular sequence that we
denote by (N (m))m≥0. For the sake of presentation, we limit ourselves to the case
p = 2 but a similar discussion can be carried on for any modulo.
We let m ⊕ n denote the Nim-sum of the integers m, n, i.e., addition digit-wise
modulo 2 of their base-2 expansions (without carry). For instance, 5 ⊕ 12 = 9.
From Pascal’s rule (n+1
i ) = (n
i ) + ( n
i−1
), we have that

(8) t2,n+1 = t2,n ⊕ (2t2,n).

For all r, s ∈ {0, 1}, we have

(2m + r) ⊕ (2n + s) = 2(m ⊕ n) + (r + s mod 2),

which means that the bidimensional sequence (m ⊕ n)m,n≥0 is 2-regular; see [4,
Example 16.5.5]. In view of relation (8), consider the subsequence (N (m))m≥0

ON DIGITAL SEQUENCES ASSOCIATED WITH PASCAL’S TRIANGLE 9

extracted from the previous bidimensional Nim-sum array and deﬁned by N (m) =
m⊕2m for all m ≥ 0. The sequence (N (m))m≥0 starts with values given in Table 1,
which are also depicted in Figure 4, and appears as entry A048724 in the OEIS [20]
(it also appears in [19]). In Figure 4, observe that a pattern repeats itself between

m 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
N (m) 0 3 6 5 12 15 10 9 24 27 30 29 20 23 18 17 48 51

Table 1. The sequence (N (m))m≥0.

1 8 16 32 64 128

50

100

150

200

250
 Figure 4. The ﬁrst few values of (N (m))m≥0.

two consecutive powers of 2, suggesting that the considered sequence is 2-regular.
This property is shown below. The red dots in Figure 4 represent the ﬁrst few
values of the subsequence (t2,n)n≥0 of N (m))m≥0. Since | rep2(t2,n)| = n + 1,
note that there is only one red dot in an interval made of consecutive powers of 2.
Playing with base-2 expansions, it is easily seen that any subsequence of the form
(N (4m + r))m≥0, 0 ≤ r < 4, can be expressed as a linear combination of the three
sequences (N (m))m≥0, (N (2m + 1))m≥0, (1, 1, 1, 1, . . .).
Indeed we have

(9)
 



 N (4m) = 4N (m),
N (4m + 1) = 4N (m) + 3,
N (4m + 2) = 2N (2m + 1),
N (4m + 3) = 2N (2m + 1) − 1.

For instance, the ﬁrst relation holds as 4m ⊕ 8m = 4(m ⊕ 2m) since rep2(8m) =
rep2(m)000 and rep2(4m) = rep2(m)00. Now let us come back to the sequence
(t2,n)n≥1 of interest. From (8), this is a subsequence of (N (m))m≥0. Namely,
t2,0 = 1 and, for all n > 0,

(10) t2,n = N (t2,n−1).

In Table 1, (t2,n)n≥1 appears underlined. In the next section, we focus on this kind
of subsequence extraction.

Remark 11. Note that the same argument can be carried out for a general prime
p as long as one deﬁnes a suitable Nim-sum in base p: addition digit-wise modulo p
(without carry). For instance, 23 ⊕3 13 = 6. We have tp,n+1 = tp,n ⊕p (p tp,n) and
we may deﬁne Np(m) = m ⊕p (p m) to get tp,n = Np(tp,n−1). In the following, we
keep the notation N (m) for N2(m).

10 P. MATHONET, M. RIGO, M. STIPULANTI, AND N. ZENA¨IDI

4.1. Regularity of (Np(m))m≥0 and ﬁnite automata. We assume that the
reader has some basic knowledge of automata theory. A (deterministic ﬁnite) au-
tomaton is a machine devised to recognize/accept some sequences of symbols read
once at a time. In our setting, these symbols are usually pairs or tuples of digits.
See for instance [4, 6] for some background on the matter.
In the remaining of this section, we show that the sequence (Np(m))m≥0 is
p-synchronized but that the sequence (tp,n)n≥0 is not p-regular. We recall the
necessary deﬁnitions. Let d ≥ 1 and k ≥ 2 be integers. A subset X of Nd is k-
recognizable (or said to be a k-synchronized relation with the terminology of [7]) if
the language
 {pad(repk(x1), . . . , repk(xd)) | (x1, . . . , xd) ∈ X}

is accepted by a ﬁnite automaton with input alphabet {0, . . . , k − 1}d and where
pad(m1, . . . , md) is the d-tuple of words of the same length
(0
M −|m1|m1, . . . , 0
M −|md|md)

with M = maxi |mi|. A sequence (xn)n≥0 is k-synchronized (see [7]) if the set
{(n, xn) | n ≥ 0} is k-recognizable. Every k-synchronized sequence is k-regular [7,
Prop. 2.6].

Proposition 12. Let a, b be non-negative integers. The set of pairs {(m, am +
b) | m ≥ 0} is p-recognizable. Otherwise stated, the sequence (am + b)m≥0 is p-
synchronized.

Proof. This is a classical exercise in automata theory or, one can make use of the
fact that this set of pairs is p-deﬁnable (i.e., deﬁnable by a ﬁrst order formula in
⟨N, +, Vp⟩) — see, for instance, [6]. Indeed, multiplication by a constant is deﬁnable
in this structure. □

Proposition 13. The set of triples {(m, n, m ⊕p n) | m, n ≥ 0} is p-recognizable.

Proof. A single-state automaton with a loop of labels (a, b, a + b mod p) is enough.
There is no carry to take into account. □

Composing synchronized relations [7], we get the following.

Corollary 14. Let a, b be non-negative integers. The sequence (m ⊕p (am + b))m≥0
is p-synchronized. In particular, (Np(m))m≥0 is p-synchronized.

Proof. Combining the above two propositions, the set

{(m, am + b, m ⊕p (am + b)) | m ≥ 0}

is p-recognizable. □

In Figure 5, we have represented an automaton recognizing {(m, N (m)) | m ≥ 0},
where all transitions leading to a sink state are not drawn. The ﬁrst few pairs of
words that are accepted are
(
ε
ε
), (01
11
)
, (010
110
)
, (011
101
)
, (0100
1100

), (0101
1111

)

which correspond to the pairs of integers (0, 0), (1, 3), (2, 6), (3, 5), (4, 12), (5, 15).
For example, an accepting run for the pair (4, 12), starting from the initial state 0,
is given by
 0 (0
1)
−→ 1 (1
1)
−→ 0 (0
0)
−→ 0 (0
0)
−→ 0.

ON DIGITAL SEQUENCES ASSOCIATED WITH PASCAL’S TRIANGLE 11

0 1

(0
0
) (0
1) (1
0
)

(1
1)

Figure 5. A DFA recognizing the pairs (m, N (m)).

From the classical theory of regular sequences, we can also obtain a linear rep-
resentation for (N (m))m≥0:

λ = (1 0 0
) , µ(0) =
 


2 0 0
0 0 1
4 0 1



 , µ(1) =
 

 0 1 0
4/3 2 −1/3
−4 4 1
 

 , ν =
 


0
3
3


 .

This means that N (m) can be computed as λ·µ(rep2(m)R)·ν where µ is a morphism
from the monoid {0, 1}
∗ equipped with concatenation to the monoid Z
3×3 equipped
with multiplication. Matrix multiplications are considered starting with the least
signiﬁcant digit ﬁrst or, with the reversal of the base-2 expansion of m. For instance,
rep2(4) = 100 and λ · µ(0) · µ(0) · µ(1) · ν = 12 = N (4).

Proposition 15. The sequence (tp,n)n≥0 is not p-regular.

Proof. If a sequence is p-regular then its growth rate is in O(nc) for some constant c.
But from (5), t2,n+4 ≥ 9 t2,n and thus t2,n ≥ 9
n/4. More generally, for an arbitrary
p ≥ 2, from Remark 10, tp,n+2p ≥ (p + 1)2 tp,n and thus tp,n ≥ (p + 1)n/p. □

5. The set {Np(m) | m ≥ 0}

Throughout this section, we let p ≥ 2 be a prime number. Our goal is to study
the set {Np(m) | m ≥ 0}.

Lemma 16. The map m ↦→ Np(m) is injective.

Proof. Let x, y be such that repp(x) = xℓ · · · x0, repp(y) = yℓ · · · y0. If the two
representations have diﬀerent lengths, we allow leading zeroes for the shortest one.
Assume x ̸= y. Let k ≥ 0 be the smallest index such that xk ̸= yk. Then xk ⊕p
xk−1 = xk ⊕p yk−1 diﬀers from yk ⊕p yk−1, so Np(x) ̸= Np(y). □

5.1. Partitioning {N (m) | m ≥ 1}. We start with the case p = 2 and we show that
{N (m) | m ≥ 0} may be partitioned into sets of numbers obtained by recursively
iterating the map m ↦→ N (m) on odious numbers. An evil (resp. odious) number
is an integer having an even (resp. odd) number of 1’s in its base-2 expansion.

Lemma 17. Let e be an evil number. There is a unique integer m such that
N (m) = e.

Proof. Let e be an evil number, and write rep2(e) = eℓ · · · e0 with eℓ = 1. We show
that there exists m such that rep2(m) = mℓ−1 · · · m0 with mℓ−1 = 1 and N (m) = e.
If such an integer m exists, then it must satisfy m0 = e0, mℓ−1 = eℓ = 1 and we
ﬁnd mi = ei ⊕ mi−1 for i = 1, . . . , ℓ (if, for convenience, we set mℓ = 0). Otherwise
stated, rep2(m) is made of blocks of 0’s or 1’s. If ei = 1, then mi = 1 − mi−1, so
these two kinds of blocks alternate each time we encounter a letter 1 in the base-2
expansion of e. Starting from the least signiﬁcant digit, the rightmost block in
rep2(m) is made of letters e0. Since e is evil, with eℓ = 1, we indeed get mℓ = 0

12 P. MATHONET, M. RIGO, M. STIPULANTI, AND N. ZENA¨IDI

(we thus have a solution to the system of equations). Uniqueness follows from the
previous lemma. □

Example 18. In the proof of the previous lemma, we start with an evil number.
Let us take e = 43 with rep2(n) = 101011. Then we would like to ﬁnd the solution
to the equation N (m) = e, which is represented in the following table.

rep2(m) 0 m4 m3 m2 m1 m0
rep2(2m) ⊕ m4 m3 m2 m1 m0 0
rep2(e) 1 0 1 0 1 1

Starting from the right of the table, we get m0 = 1. We may update the table as
follows. rep2(m) 0 m4 m3 m2 m1 1
rep2(2m) ⊕ m4 m3 m2 m1 1 0
rep2(e) 1 0 1 0 1 1
Examining the second column on the right, we get m1 = 0. Pursuing like this for
the other columns, we obtain rep2(m) = 11001.

Lemma 19. The set {N (m) | m ≥ 0} = {0, 3, 5, 6, 9, 10, . . .} is exactly the set
of evil numbers. In particular, the sequence (N (m))m≥1 is a permutation of the
increasing sequence A001969 of evil numbers.

Proof. We ﬁrst show by induction on m that N (m) is evil. This is readily checked
for the ﬁrst few values of m. We make use of (9): rep2(N (4m)) = rep2(N (m))00,
rep2(N (4m + 1)) = rep2(N (m))11 and rep2(N (4m + 2)) = rep2(N (2m + 1))0. By
induction hypothesis, rep2(N (m)) and rep2(N (2m + 1)) are evil, so are N (4m + r)
for r = 0, 1, 2. Observe that N (2m + 1) is odd by deﬁnition of the Nim-sum. Thus
rep2(N (2m + 1)) is of the form u1 for some binary word u. Hence, rep2(2N (2m +
1) − 1) = u01 has the same number of letters 1 as rep2(N (2m + 1)). By induction
hypothesis, N (2m + 1) is evil and thus N (4m + 3) is also evil.
Conversely, every evil number belongs to the set as a consequence of the previous
lemma. □

Since N (m) > m for all m ≥ 1, we can extract subsequences in a recursive way
similar to (10). Let i ≥ 1 be an integer. We let (sub(i, m))m≥0 be the sequence
(xm)m≥0 deﬁned by x0 = i and xm+1 = N (xm). In other words we consider the
sequence (N m(i))m≥0 of iterations of N on i. We have seen in particular that
t2,m = sub(1, m) for all m ≥ 1 (recall, for instance, Table 1).
We claim the following.

Theorem 20. We have the partition

{N (m) | m ≥ 1} = ⋃

i∈O{sub(i, m) | m ≥ 1}

where the sets in the above union are pairwise disjoint and O = {1, 2, 4, 7, 8, 11, . . .}
is the set of odious numbers.

1 2 3 4 5 6 7 8
sub(1, m) 3 5 15 17 51 85 255 257 · · ·
sub(2, m) 6 10 30 34 102 170 510 514
sub(4, m) 12 20 60 68 204 340 1020 1028
sub(7, m) 9 27 45 119 153 427 765 1799
sub(8, m) 24 40 120 136 408 680 2040 2056
sub(11, m) 29 39 105 187 461 599 1785 2827
...

ON DIGITAL SEQUENCES ASSOCIATED WITH PASCAL’S TRIANGLE 13

With the same reasoning as in the proof of Proposition 15 from (5), none of
these sequences is 2-regular.

Proof. Let i ̸= j be odious numbers. The sets {sub(i, m) | m ≥ 1} and {sub(j, m) |
m ≥ 1} are disjoint. Proceed by contradiction and assume that there exist integers
m, n ≥ 1 such that N m(i) = N n(j). Without loss of generality, assume m ≥ n.
From Lemma 16, N m−n(i) = j. If m = n, we get i = j, which is a contradiction.
If m > n, then N m−n(i) is evil but j is odious, which is again a contradiction.
We still have to show that for every evil number n, there exists some integer i
such that n belongs to {sub(i, m) | m ≥ 1}. If a number e is evil, then ﬁnd N −1(e)
and repeat this procedure while the result is evil and positive. Since N −1(e) < e,
this procedure stops when we reach an odious number i meaning that e belongs to
{sub(i, m) | m ≥ 1}.
Finally, by Lemma 19 every evil number appears in the set, from the ﬁrst part
of the proof, the partition must thus runs over all odious numbers. □

5.2. A known permutation. Since (N (m))m≥1 is a permutation of the sequence
A001969 of the evil numbers, it is natural to consider the sequence α mapping
m ≥ 1 to the position of N (m) within the ordered sequence of evil numbers. The
ﬁrst few terms of this permutation α of N>0 are

1, 3, 2, 6, 7, 5, 4, 12, 13, 15, 14, 10, 11, 9, 8,

24, 25, 27, 26, 30, 31, 29, 28, 20, 21, 23, 22, 18, 19, 17, 16, . . . .

Otherwise stated, if e(m) is the mth evil number, the ﬁrst evil numbers being
e(0) = 0 and e(1) = 3, then

(11) e(α(m)) = N (m).

This sequence appears as A003188 in [20] and is described as an integer equivalent
of the Gray code for n considered as a base-2 expansion (Gray code provides a way
to enumerate integers by only changing one digit in their base-2 expansion from
one element to the next one). As observed by Paul D. Hanna (we refer again to
[20]), it is known that

(12) α(m) = m ⊕ ⌊m/2⌋

for all m ≥ 1. In the following we deﬁne α through this relation. In particular,
N (m) is roughly twice α(m). One can easily deduce that the map α restricted to
[2n, 2
n+1[ is again a one-to-one correspondence mapping [2
n, 2
n + 2
n−1[ to [2
n +
2n−1, 2n+1[ and [2
n + 2
n−1, 2
n+1[ to [2n, 2n + 2
n−1[, as shown in Figure 6. From

4 8 16 32 64 128

-60

-40

-20

20

40
 Figure 6. The graph of n ↦→ α(n) − n over [0, 127[.

14 P. MATHONET, M. RIGO, M. STIPULANTI, AND N. ZENA¨IDI

Hanna’s remark (12), we have

(13)
 



 α(4n) = 2α(2n)
α(4n + 1) = 2α(2n) + 1
α(4n + 2) = 2α(2n + 1) + 1
α(4n + 3) = 2α(2n + 1).

To get e(n), notice that one simply writes down rep2(n) and appends an extra
digit, either 0 or 1 to get an evil number. This is rather straightforward: indeed
rep2(n) ranges over all the words in 1{0, 1}
∗, and appending the convenient digit,
we get all the evil numbers (and the order is preserved). If rep2(α(m)) = aℓ · · · a1,
then relation (12) yields rep2(N (m)) = rep2(2m ⊕ m) = aℓ · · · a1a0 where a0 is the
least signiﬁcant digit of m. Moreover it is the only evil number having aℓ · · · a1 as
length-ℓ preﬁx. From these observations, we get (11) that can be expressed by

rep2(N (m)) = { rep2(α(m))0, if α(m) is evil;
rep2(α(m))1, if α(m) is odious

(recall that N (m) is evil).

5.3. A generalization of the Thue–Morse sequence. In this section, we show
that the set Ep = {Np(m) | m ≥ 0}, generalizing the set of evil numbers for p > 2,
is p-automatic. Recall that a set S of non-negative integers is said to be p-automatic
if its characteristic sequence
 χS(n) =
 {1 if n ∈ S
0 otherwise

is itself p-automatic [4]. For more details about automaticity, we refer the reader
to [4] or [6].

Lemma 21. Let e be an integer and write repp(e) = ek+1 · · · e0. There exists an
integer m such that Np(m) = e if and only if ∑k+1
i=0 (−1)
iei = 0 (mod p). When
such an integer m exists, it is unique.

Proof. Let repp(m) = mk · · · m0. As in the proof of Lemma 17, we have to consider
the following linear system over Zp











1 0 0 · · · 0
1 1 0 0
0 1 1 0
... . . . . . . ...
1 1
0 · · · 0 1











 



m0
...
mk



 =
 



 e0
...
ek+1



 .

The (k + 2) × (k + 1) matrix has rank k + 1. The system has a solution if and only
the determinant 









1 0 0 · · · 0 e0
1 1 0 0 e1
0 1 1 0 e2
... . . . . . . ...
1 1 ek
0 · · · 0 1 ek+1











is zero in Zp. Uniqueness follows from Lemma 16. □

A classical generalization of the Thue–Morse sequence to a p-letter alphabet is to
consider the ﬁxed point starting with 0 of the morphism over {0, . . . , p − 1} deﬁned
by i ↦→ i(i + 1) · · · (p − 1) 0 · · · (i − 1). The nth symbol occurring in the ﬁxed point

ON DIGITAL SEQUENCES ASSOCIATED WITH PASCAL’S TRIANGLE 15

is equal to the sum-of-digits modulo p of n written in base p. See, for instance, [3]
and the references therein.

Proposition 22. Let ϕ be the p-uniform morphism over {0, . . . , p − 1} deﬁned by
ϕ(0) = 0 (p−1) (p−2) · · · 1 and ϕ(j) = (p−j) (p−j−1) · · · 0 (p−1) (p−2) · · · (p−j+1)
for all j ∈ {1, . . . , p − 1}, and let τ be the coding over {0, . . . , p − 1} deﬁned by
τ (0) = 1 and τ (j) = 0 for all j > 1. Then the set Ep = {Np(m) | m ≥ 0} is
p-automatic, i.e., its characteristic sequence is the image, under the coding τ , of
the ﬁxed point of the morphism ϕ.

Proof. Consider a DFA with 2p states of the form (i, +) or (i, −) with i ∈ {0, . . . , p−
1}. The transitions between states are given by

(i, +) d
−→ (i + d mod p, −)

and (i, −) d
−→ (i − d mod p, +)

for all digits d ∈ {0, . . . , p − 1}. The initial state is (0, +) and the ﬁnal states are
(0, +) and (0, −). This DFA accepts words (i.e., ﬁnite sequences of digits) whose
alternating sum equals 0 modulo p. We can minimize this DFA. For 0 ≤ i < p, the
states (i, +) and (p − i mod p, −) are Nerode equivalent, i.e., the same sequences
are accepted from both states. Indeed, reading d0 · · · dk from (i, +) leads to a state
whose ﬁrst component is i + d0 − d1 + · · · + (−1)kdk = 0 modulo p. Reading the
same word d0 · · · dk but from (p − i, −) leads to p − i − d0 + d1 + · · · − (−1)kdk,
which is also equal to 0 modulo p. After merging states, the minimal automaton
has p states of the form [(i, +), (p − i mod p, −)] for 0 ≤ i < p and transitions

[(i, +), (p − i mod p, −)] d
−→ [(p − i − d mod p, +), (i + d mod p, −)]

for all digits d ∈ {0, . . . , p − 1}. If we identify [(j, +), (p − j mod p, −)] with j,
we get the expected morphism using a classical construction due to Cobham. For
instance, see [4, Theorem 6.3.2].
Now, if repp(n) = nk · · · n0, observe that reading the word nk · · · n0 from the
state (0, +) leads to the state (n0 − n1 + · · · + (−1)knk, (−1)
k+1). We conclude the
proof by using Lemma 21. □

We can make the same discussion as in Subsection 5.2. In an attempt to gener-
alize (11), we extend (12) by deﬁning αp(m) := m ⊕ ⌊m/p⌋ and by letting Ep(m)
denote the mth element in Ep. It is clear that {αp(m) | m ≥ 1} = N>0, and thus,
αp is a permutation of N>0. For instance, for p = 3, the ﬁrst few terms of α3 [20,
A071770] are 0, 1, 2, 4, 5, 3, 8, 6, 7, 12, 13, 14, 16, 17, 15,

11, 9, 10, 24, 25, 26, 19, 20, 18, 23, 21, 22, 9, 37, 38, 40, 41, . . . .

For every integer m ≥ 0 such that repp(αp(m)) = aℓ · · · a1, there exists a unique
digit a0 such that valp(aℓ · · · a1a0) belongs to Ep by Lemma 21. This is the mth
element in Ep; thus Ep(αp(m)) = Np(m).

5.4. Summatory function. Jean-Paul Allouche et al. [2] provide an exact for-
mula for the summatory function of the evil numbers (they also consider the gen-
eralization to arbitrary bases and digits)

Se(M ) :=
 M∑

i=1 e(i) = M (M + 1) + ⌊ M
2
 ⌋ − [M %2]([M %2] + 1)
2

+[s2(⌊M/2⌋)%2]([M %2] + 1) + 2 max
{
0, [M %2] − [s2(⌊M/2⌋)%2]
},

16 P. MATHONET, M. RIGO, M. STIPULANTI, AND N. ZENA¨IDI

where we let s2 denote the sum-of-digits in base 2 and [n%k] denote the unique
integer in {0, . . . , k−1} congruent to n modulo k. In this formula, the ﬁrst two terms
explain the general behavior and last three terms only give a possible correction of
1 to the main terms. In the same vein, let us consider the summatory function of
N given by
 SN (M ) :=
 M∑

i=1 N (i).

Instead of considering general/advanced techniques on the summatory function of
k-regular sequences [4, Section 3.5], we will make use of elementary operations and
of the permutation α to express SN (M ). Now let k ≥ 0 be an integer. Because
of (11), e(·) and N (·) take the same set of values over any interval of the form
[2k, 2
k+1[, thus we have SN (2
k − 1) = Se(2k − 1). However for M ∈ [2k, 2k+1 − 1[,
SN (M ) > Se(M ). The graph of the diﬀerence between SN and Se is given in
Figure 7. Taking into account the behavior of the permutation α on the interval

256 512 1024 2048

100 000

200 000

300 000

400 000

500 000
 Figure 7. The diﬀerence M ↦→ SN (M ) − Se(M ).

[2k, 2
k+1[, we obtain

2
k+2k−1−1∑

j=2k N (j) =
 2
k+1−1∑

j=2k+2k−1 e(j) and
 2
k+1−1∑

j=2k+2k−1 N (j) =
 2
k+2k−1−1∑

j=2k e(j).

Since e is an increasing sequence, the maximum of SN (M ) − Se(M ) on [2k, 2
k+1[
is attained at 2
k + 2k−1 − 1 and is given by

Se(2k+1 − 1) − 2Se(2k + 2k−1 − 1) + Se(2k − 1)

because

SN (2k + 2k−1 − 1) = SN (2k − 1) +
 2
k+2
k−1−1∑

j=2k N (j)

= Se(2
k − 1) +
 2
k+1−1∑

j=2k+2k−1 e(j)

= Se(2
k − 1) + Se(2k+1 − 1) − Se(2k + 2k−1 − 1).

For M ∈ [2
k, 2
k+1[, we also get

(14) SN (M ) − Se(M ) =
 M∑

j=2k(N (j) − e(j)).

ON DIGITAL SEQUENCES ASSOCIATED WITH PASCAL’S TRIANGLE 17

Lemma 23. For all j ≥ 1,

N (j) − e(j) = e(α(j)) − e(j) ∈ 2(α(j) − j) + {−1, 0, 1}

and moreover, for two consecutive indices,

1∑

r=0 [N (2j + r) − e(2j + r) − 2 (α(2j + r) − (2j + r))] = 0.

Proof. The ﬁrst part is obvious since we have e(α(j)) ∈ 2α(j) + {0, 1} and e(j) ∈
2j + {0, 1} for any j.
For the second part, let u be the base-2 expansion of j. The four terms in

2(2j + 2j + 1) − e(2j) − e(2j + 1)

are respectively represented by u00, u10, u0a and u1(1 − a) for some a ∈ {0, 1}
such that u0a and u1(1 − a) have an even number of ones. So, this sum is equal to
−1. By deﬁnition of N and α, observe that the remaining terms can be grouped as

N (2j) − 2α(2j) = 0 and N (2j + 1) − 2α(2j + 1) = 1

and the conclusion follows. □

As a consequence of this lemma, for M ∈ [2k, 2k+1[, we get

SN (M ) = Se(M ) + 2
 M∑

j=2k α(j) − (M − 2
k + 1) (
2
k + M ) + R

with R ∈ {−1, 0, 1}. If M is odd, then the number of terms in the sum (14) is even
so by the second part of Lemma 23, we get R = 0. If M is even, then only the ﬁrst
part of the lemma can be applied and replacing N (j) − e(j) with 2(α(j) − j) could
lead to an oﬀset of ±1.
Let ℓ ≥ 0 such that M = 2
k + ℓ. Observe that the above sum has ℓ + 1 terms.
If we group together every two consecutive terms, we can make use of (13) to get

α(4n) + α(4n + 1) = 4α(2n) + 1 and α(4n + 2) + α(4n + 3) = 4α(2n + 1) + 1

so

(15)
 M∑

j=2k α(j) = 4
 2
k−1+⌊ ℓ−1
2 ⌋∑

j=2k−1 α(j) + ⌊ ℓ − 1
2
 ⌋ + 1 + [(ℓ + 1)%2] α(M ),

where the last term only appears when ℓ is even since, in that case, the sum
has an odd number of terms and the last term has thus to be treated sepa-
rately. By using (15) repeatedly, one can write SN (M ) as the sum of Se(M ) −
(M − 2k + 1) (
2
k + M )+R and k terms of the form ⌊ ℓ′−1
2 ⌋+1+[(ℓ
′ +1)%2] α(2k′ +

ℓ
′) for decreasing values of k′, ℓ
′, each term being multiplied by 2 · 4
k−k′.

Remark 24. Since the main term in Se(M ) is quadratic (recall the formula ob-
tained in [2]), in Figure 8 we compare, on some interval [2k, 2k+1[, SN (M ) − Se(M )
and the parabola −2M 2 + 6 · 2kM − 4 · 2
2k (which can be obtained from the inter-
sections with the axis y = 0 and knowing the maximum of the function).

6. Extension to trinomial coefficients

One can also consider the generalization of Pascal’s triangle to a three-dimensional
pyramid made of trinomial coeﬃcients (see, for instance, [21]). Let n ≥ 0. The
plane of equation x + y + z = n with x, y, z ≥ 0 contains (n + 1)(n + 2)/2 integer
points with value ( n
x, y, z
) = n!
x! y! z! .

18 P. MATHONET, M. RIGO, M. STIPULANTI, AND N. ZENA¨IDI

Figure 8. Comparison of SN (m) − Se(M ) with a parabola be-
tween two consecutive powers of 2.

If these trinomial coeﬃcients depicted by unit cubes are colored with respect to their
value modulo p, we get representations like the one in Figure 9. In this section, we
will generalize the observations from Section 2 and the recursive formula (8).

Figure 9. The ﬁrst levels of Pascal’s pyramid modulo 5.

For instance, for n = 5, the sixth plane x + y + z = 5 of the pyramid is a
triangle that contains six rows ordered for y = 5, 4, . . . , 0. Since the coeﬃcients are
symmetric in the variables, one can also let vary either x or z (and take instead
columns or diagonals of the form x + y = z). In the subsequent ﬁgures, we assume
as usual that the x-axis is horizontal and the y-axis is vertical.

Deﬁnition 25. Let 0 ≤ k ≤ n. We take these trinomial coeﬃcients modulo p, so
the kth line (i.e., z = n − k) in the nth plane (i.e., x + y + z = n) of the pyramid
is the base-p expansion of an integer tp,n,k deﬁned by

tp,n,k =
 k∑

i=0
 [( n
i, k − i, n − k
) mod p
] pi.

For p = 2, if we order the elements plane by plane, and then for each plane, by row
of increasing length, we get a sequence t2,0,0, t2,1,0, t2,1,1, t2,2,0, t2,2,1, t2,2,2, t2,3,0, . . .
whose ﬁrst few terms are

1|1, 3|1, 0, 5|1, 3, 5, 15|1, 0, 0, 0, 17|1, 3, 0, 0, 17, 51| · · · .

ON DIGITAL SEQUENCES ASSOCIATED WITH PASCAL’S TRIANGLE 19

See, for instance, Figure 10 for n = 5. Note that t2,n,n = t2,n for all n ≥ 0, because
the boundaries of the nth plane are copies of the nth row of Pascal’s triangle.

1
5 5
10 20 10
10 30 30 10
5 20 30 20 5
1 5 10 10 5 1
 1 t2,5,0 = 1
1 1 t2,5,1 = 3
0 0 0 t2,5,2 = 0
0 0 0 0 t2,5,3 = 0
1 0 0 0 1 t2,5,4 = 17
1 1 0 0 1 1 t2,5,5 = 51

Figure 10. The sixth row (t2,5,k)0≤k≤5 of Pascal’s pyramid.

Expand (a + b + c)
n by the multinomial theorem and consider the coeﬃcient
of a
ib
jck with i + j + k = n. It is equal to the corresponding coeﬃcient in the
product (a + b + c) · (a + b + c)n−1 where the latter factor is again expanded by the
multinomial theorem. We get a generalization of Pascal’s rule
( n
i, j, k
) = ( n − 1
i − 1, j, k
) + ( n − 1
i, j − 1, k
) + ( n − 1
i, j, k − 1

).

From this tree-term relation, we get the generalization of (8)

∀i, j : 0 ≤ j ≤ i, t2,i,j = t2,i−1,j ⊕ t2,i−1,j−1 ⊕ 2t2,i−1,j−1

where we assume that t2,i,j = 0 whenever j > i or j < 0.

6.1. Lucas’ theorem again and again. As in Section 2, let us compare the values
modulo p taken in the ith plane x + y + z = i with i = d · pk + s, 0 < d < p and
0 ≤ s < p
k, and those in the sth plane x + y + z = s. We will explain that the
pattern modulo p of the sth plane repeats itself (d + 1)(d + 2)/2 times as square
patches of size p
k × p
k under some well-understood permutation. In Figure 11, we
consider p = 5, i = 23, d = 4, k = 1, and s = 3.

0 1 2 3 4

1 2 3 4

1

2

3

4
 5 10 15 20

5

10

15

20
 Figure 11. The 3rd and 23rd planes of Pascal’s pyramid modulo 5.

20 P. MATHONET, M. RIGO, M. STIPULANTI, AND N. ZENA¨IDI

Let i = x + y + z. We let xk ≥ 0 denote the quotient of x by pk. Let us compare
the values modulo p of
( i
x, y, z
) with ( i
x − xkpk, y + xkpk, z
).

Geometrically, the map (x, y, z) ↦→ (x − xkp
k, y + xkpk, z) corresponds to a trans-
lation parallel to a side of the triangular boundary of the plane. For instance,
in Figure 11 where p = 5, i = 23 and k = 1, if we take x = 11, then xk = 2
and we have depicted the corresponding translation vector. Adding (−10, 10, 0) to
(x, y, z) does not change the sum of the three components (we remain in the plane
x + y + z = 23) but translates the 5 × 5 square region bounded by 10 ≤ x < 15
and 5 ≤ y < 10 to the square 0 ≤ x′ < 5 and 15 ≤ y′ < 20. Similarly, we could
have considered a transformation of the form (x, y, z) ↦→ (x − xkp
k, y, z + xkpk).
Due to the symmetry of the trinomial coeﬃcients, six such transformations can be
considered and correspond to translations in two directions parallel to one of the
three sides of the boundary. We will indeed compose two such translations. On the
one hand, recalling that i = x + y + z, we have
( i
x − xkpk, y + xkpk, z
) = i!
z! (x + y)! · (x + y)!
(x − xkpk)! (y + xkpk)!

= (i
z
) ( i − z
x − xkpk
)

≡ (i
z
) (
ϵk(i − z)
0
 )

︸ ︷︷ ︸
=1
 k−1∏

j=0
 (
ϵj(i − z)
ϵj(x)
 ) mod p,

where ϵj(n) is the jth least signiﬁcant digit in the base-p expansion of n (and
leading zeroes are allowed, for instance, ϵk(i − z) = 0 whenever i − z < pk). On the
other hand, we ﬁnd
( i
x, y, z
) = (i
z
) (
i − z
x
 )

≡ (i
z
)(ϵk(i − z)
xk
 ) k−1∏

j=0
 (ϵj(i − z)
ϵj(x)
 ) (mod p).

Hence with the same notation as in Section 2, we have

µ
−1
ϵk(i−z),xk
 ( i
x, y, z
) ≡ ( i
x − xkpk, y + xkpk, z
) (mod p).

We now apply a second map of the form (x′, y′, z′) ↦→ (x′, y′ −y′
k, z′ +z′
k) and we get
the permutation µ
−1
ϵk(i−x′),y′
k acting of the values of the coeﬃcients of the translated
region. Combining these two transformations, we may relate the value modulo p of
the initially considered trinomial coeﬃcient with the trinomial coeﬃcient of some
( i
x′, y′, z′
) with x
′, y′ < p
k.

In Figure 11, adding (0, −15, 15) to (x, y, z) does not change the sum of the three
components but translate the 5 × 5 square region bounded by 0 ≤ x < 5 and
15 ≤ y < 20 to the square 0 ≤ x′ < 5 and 0 ≤ y′ < 5. Consequently, the values
modulo p are modiﬁed according to the composition of two permutations of the
form µa,b.
 ON DIGITAL SEQUENCES ASSOCIATED WITH PASCAL’S TRIANGLE 21

To conclude with the example given in Figure 11, start from the region 10 ≤
x < 15, 5 ≤ y < 10. First consider the sub-region with the extra constraint
15 ≤ x + y ≤ 18, we make such a splitting to consider the “colored” region and
avoid ambiguity about ϵ1(x + y). So we have ϵ1(x + y) = 3 and ϵ1(x) = x1 = 2. We
thus consider a multiplication by the inverse (modulo 5) of the coeﬃcient (3
2
) = 3
which is 2 — the reader may compare the two colored triangles connected by a
diagonal arrow: they are oﬀ by a multiple of 2. Now inside the region 0 ≤ x < 5,
15 ≤ y < 20, 15 ≤ x + y ≤ 18, we observe that x ≤ 3. So 20 ≤ 23 − x = y + z ≤ 23.
We thus have ϵ1(y + z) = 4 and ϵ1(y) = y1 = 3. So we consider a multiplication
by the inverse (modulo 5) of the coeﬃcient (4
3
) = 4 which is 4 — the reader may
compare the two colored triangles connected by a vertical arrow: again they are oﬀ
by a multiple of 4.
We have not discussed yet the white region corresponding to coeﬃcients con-
gruent to zero. For the region 10 ≤ x < 15, 5 ≤ y < 10, 19 ≤ x + y < 25, so
we ﬁrst have a multiplication by the inverse of (ϵ1(x+y)
2 ). But such a computa-
tion is irrelevant, because µa,b(0) = 0 for all a, b ; meaning that white squares are
mapped to white squares for all the considered translations. Another way to see
this phenomenon is explained in the next subsection.

6.2. A p-automatic pyramid. Let us quote Granville about Pascal’s triangle
modulo p: “Lucas’ theorem may be viewed as a result about automata with p possible
states! ” [12]. Let us also mention [1] where a substitution mapping elements from
{0, . . . , p − 1} to (p × p)-blocks allows the authors to compute the rectangular
block complexity of the associated bidimensional sequence. For p = 2, the iterated
substitution is

(16) 1 ↦→ 1 0
1 1 , 0 ↦→ 0 0
0 0 .

With a reasoning similar to the one of the previous subsection, we show that such
a construction still holds in higher dimension. Note that for dimension 2 (thus
from Pascal’s triangle), it is known that ((m
n ) mod d)
m,n≥0 is k-automatic for some
integer k ≥ 0 if and only if d is a power of a prime p. In that case, the sequence is
p-automatic [5]. Here we show that ((x+y+z
x, y, z ) mod p
)
x,y,z≥0 is p-automatic.

Lemma 26. If 0 ≤ x ≤ y < p and x + y ≥ p, then x > ⌊(x + y)/p⌋.

Proof. Since x + y < 2p and x + y ≥ p, write x + y = p + r with r = ⌊(x + y)/p⌋ < p.
Thus we get x = r + p − y with p − y > 0. □

The next result permits us to obtain the values modulo p of trinomial coeﬃcients
within the cube p(x, y, z)+{0, . . . , p−1}
3 from the value at (x, y, z). The other way
round, a value at a speciﬁc position is determining p3 values at further positions
in the space. In particular, the statement also explains why a pyramid is created.
The cube is cut by a plane x + y + z = p and is thus split into two regions. In the
subset belonging to the half-space x + y + z ≥ p, values modulo p of the coeﬃcients
are zero.

Proposition 27. Let a, b, c ∈ {0, . . . , p − 1}. If a + b + c < p, then
(p(x + y + z) + a + b + c
px + a, py + b, pz + c
 ) ≡ (a + b + c
a
 )(b + c
b
 )(x + y + z
x, y, z
 ) (mod p).

Otherwise (
p(x + y + z) + a + b + c
px + a, py + b, pz + c
 ) ≡ 0 (mod p).

22 P. MATHONET, M. RIGO, M. STIPULANTI, AND N. ZENA¨IDI

Proof. Without loss of generality, assume a ≤ b ≤ c. We have
(p(x + y + z) + a + b + c
px + a, py + b, pz + c
 ) = (
p(x + y + z) + a + b + c
px + a
 )(p(y + z) + b + c
py + b
 ).

Let uk · · · u0, vk · · · v0, xk · · · x0, yk · · · y0 respectively be the base-p expansions of
x + y + z, y + z, x, y such that uk ̸= 0. As usual, we allow leading zeroes to get
expansions of the same length if necessary. We examine two cases.
Suppose ﬁrst that a + b + c < p. Then

repp(p(x + y + z) + a + b + c) = uk · · · u0(a + b + c)

because a+b+c is a single digit. In particular, b+c < p and repp(p(y +z)+b+c) =
vk · · · v0(b+c). We may apply Lucas’ theorem to both binomial coeﬃcients to obtain

(p(x + y + z) + a + b + c
px + a, py + b, pz + c
 ) ≡
 k∏

i=0
 (ui
xi
)(a + b + c
a
 ) k∏

j=0
 (vj
yj
)(b + c
b
 ) (mod p)

≡ (a + b + c
a
 )(b + c
b
 )(x + y + z
x, y, z
 ) (mod p),

as expected.
Assume now that a + b + c ≥ p. As a ﬁrst sub-case, assume b + c ≥ p. By the
above lemma, b > ⌊(b+c)/p⌋. If we compute the base-p expansion of p(y +z)+b+c,
the last digit is ⌊(b + c)/p⌋ followed by repp(p(y + z) + 1) = v′
k · · · v′
0; there is a carry
to deal with. Applying as above Lucas’ theorem yields

(p(x + y + z) + a + b + c
px + a, py + b, pz + c
 ) ≡
 k∏

i=0
 (ui
xi
)(a + b + c
a
 ) k∏

j=0
 (v′
j
yj
) (
⌊(b + c)/p⌋
b
 )

︸ ︷︷ ︸
=0
 (mod p),

as desired. As a ﬁnal sub-case, assume that a ≤ b + c < p. By the above lemma,
a > ⌊(a + (b + c))/p⌋. Now the reasoning is similar. If we compute the base-p
expansion of p(x + y + z) + a + b + c, the last digit is ⌊(a + b + c)/p⌋ followed by
repp(p(x + y + z) + 1) = u
′
k · · · u
′
0. Applying as above Lucas’ theorem yields

(p(x + y + z) + a + b + c
px + a, py + b, pz + c
 ) ≡
 k∏

i=0
 (ui
xi
) (
⌊(a + b + c)/p⌋
a
 )

︸ ︷︷ ︸
=0
 k∏

j=0
 (v′
j
yj
)(b + c
b
 ) (mod p),

as wanted. □

This proposition permits us to deﬁne a 3D-substitution over {0, . . . , p − 1}
3

similar to (16) or, equivalently, an automaton reading triplets of digits. The initial
symbol is 1. The image of a symbol q ∈ {0, . . . , p − 1} is a cube of size p indexed
by {0, . . . , p − 1}3 such that, for all a, b, c ∈ {0, . . . , p − 1}, if a + b + c ≥ p, then
[σ(q)]a,b,c = 0 and if a + b + c < p, then

σ(q)a,b,c = q(
a + b + c
a
 )(b + c
b
 ) mod p.

See Figure 12 for an example of images of σ in the case p = 5. Observe that
iterations of σ on 1 are converging. Indeed, if we iterate σ on 1, then σn(1) is a
cube of size pn and σn(1) appears inside σn+1(1) at the origin (0, 0, 0).

ON DIGITAL SEQUENCES ASSOCIATED WITH PASCAL’S TRIANGLE 23

Figure 12. The images σ(q) for p = 5 and q ∈ {1, 2, 3, 4} (in this order).

7. Concluding remarks

In Section 4, we focused on base 2. For a general integer base p > 2, with ⊕p
being the addition digit-wise modulo p (without carry), it is obvious that tp,n+1 =
tp,n ⊕p (p tp,n). We can introduce a sequence Np(m) deﬁned by (m ⊕p p.m)m≥0.
Nevertheless, except for p = 3 with A242399, no such sequences appear in the OEIS
and contrarily to the binary case, we do not ﬁnd any nice property to report.
In [17], we have considered generalizations of Pascal’s triangle to binomial co-
eﬃcients of words. When these coeﬃcients are reduced modulo p, we could also
deﬁne an analogue of the sequence (tp,n)n≥0. A natural candidate to consider is the
Fibonacci numeration system, i.e., the words of the numeration language belong to
1{0, 01}
∗ ∪ {ε}. The rows of this Pascal’s triangle modulo 2 evaluated as base-2
expansions give the sequence whose ﬁrst terms are

1, 3, 5, 5, 29, 9, 57, 129, 249, 177, 705, 3681, . . .

and evaluating these rows as Fibonacci representations (not necessarily greedy)
gives
 1, 3, 4, 4, 17, 6, 27, 35, 82, 56, 145, 501, 624, 22, 1056, . . . .

In the last section, we considered trinomial coeﬃcients but the reasoning can
be extended to multinomial coeﬃcients. In particular, Proposition 27 can be ex-
tended showing that the multidimensional sequence ((x1+···+xn
x1, ..., xn ) mod p
)
x1,...,xn≥0
is p-automatic.
With Proposition 27, one could also think about a possible connection with the
so-called combinatorial numeration system where every integer can be decomposed
as a sum of binomial coeﬃcients of a prescribed form [8, 15].

24 P. MATHONET, M. RIGO, M. STIPULANTI, AND N. ZENA¨IDI

Acknowledgment

Manon Stipulanti is supported by the FNRS Research grant 1.B.397.20.

References

[1] J.-P. Allouche, V. Berth´e, Triangle de Pascal, complexit´e et automates, Bull. Belg. Math.
Soc. Simon Stevin 4 (1997), 1–23 .
[2] J.-P. Allouche, B. Cloitre, V. Shevelev, Beyond odious and evil, Aequat. Math. 90 (2016),
341–353.
[3] J.-P. Allouche, J. Shallit, The ubiquitous Prouhet-Thue-Morse sequence, Sequences and their
applications (Singapore, 1998), 1–16, Springer Ser. Discrete Math. Theor. Comput. Sci.,
Springer, London, 1999.
[4] J.-P. Allouche, J. Shallit, Automatic Sequences: Theory, Applications, Generalizations, Cam-
bridge University Press, Cambridge, (2003).
[5] J.-P. Allouche, F. von Haeseler, H.-O. Peitgen, G. Skordev, Linear cellular automata, ﬁnite
automata and Pascal’s triangle, Disc. Applied Math. 66 (1996), 1–22.
[6] V. Bruy`ere, G. Hansel, C. Michaux, R. Villemaire, Logic and p-recognizable sets of integers,
Bull. Belg. Math. Soc. Simon Stevin 1 (1994), 191–238.
[7] A. Carpi, C. Maggi, On synchronized sequences and their separators, Theor. Inform. Appl.
35 (2001), 513–524.
[8] ´E. Charlier, M. Rigo, W. Steiner, Abstract numeration systems on bounded languages and
multiplication by a constant, INTEGERS 8 (2008), # A35.
[9] J. H. Conway, R. K. Guy, The book of numbers, Copernicus, New York, 1996.
[10] D. A. Cox, Galois Theory, Pure and Applied Mathematics (2nd ed.), John Wiley & Sons
(2012).
[11] M. Gardner, Mathematical carnival, Mathematical Association of America, Washington, DC,
(1989).
[12] A. Granville, Arithmetic properties of binomial coeﬃcients I: Binomial coeﬃcients modulo
prime powers, Canadian Math. Soc. Conference Proceedings 20 (1997), 253–275.
[13] F. von Haeseler, H.-O. Peitgen, G. Skordev, Pascal’s triangle, dynamical systems and attrac-
tors, Ergod. Th. & Dynam. Sys. 12 (1992), 479–486.
[14] D. Hewgill, A relationship between Pascal’s triangle and Fermat’s numbers, Fibonacci Quart.
15 (1977), 183–184.
[15] G. Katona, A theorem on ﬁnite sets, Theory of Graphs, Proc. Colloquium, Tihany, Hungary
(1966), 187–207.
[16] M. Kˇr´ıˇzek, F. Luca, S. Lawrence, 17 lectures on Fermat numbers. From number theory to
geometry, CMS Books in Mathematics 9, Springer-Verlag, New York, (2001).
[17] J. Leroy, M. Rigo, M. Stipulanti, Generalized Pascal triangle for binomial coeﬃcients of
words, Adv. Appl. Math. 80, 24–47.
[18] Y. Li, W. Wu, Self-similarity of P-positions of (2n + 1)-dimensional Wythoﬀ’s game, Fractals
29 (2021).
[19] H. D. Nguyen, A mixing of Prouhet–Thue–Morse sequences and Rademacher functions, In-
tergers 15 (2015), paper # A14.
[20] N. Sloane et al., The On-Line Encyclopedia of Integer Sequences, http://oeis.org.
[21] S. Wolfram, Geometry of binomial coeﬃcients, Amer. Math. Monthly. Vol. 91, No. 9 (1984).
