<!-- source: https://math.uchicago.edu/~may/REU2021/REUPapers/Xu,Nancy.pdf | converted from PDF -->

RECIPROCITY LAWS

NANCY XU

Abstract. This paper surveys four of the early reciprocity laws. We start
with a discussion of quadratic reciprocity, which we will prove using the split-
ting of primes in algebraic number ﬁelds. We then introduce Gauss and Jacobi
sums before using them to prove cubic, biquadratic, and Eisenstein reciprocity.

Contents

1. Introduction 1
2. Quadratic Reciprocity 2
3. Gauss and Jacobi Sums 8
4. Cubic Reciprocity 10
5. Biquadratic Reciprocity 14
6. Eisenstein Reciprocity 18
Acknowledgments 24
References 24

1. Introduction

For distinct primes p, q, reciprocity laws turn the question of whether q is an nth
power modulo p into the question of whether p is an nth power modulo q, hence
the name ”reciprocity.” The case n = 2 is quadratic reciprocity. The cases n = 3
and n = 4 are cubic and biquadratic reciprocity, respectively, where we move from
the familiar Z to Z[ζ3] or Z[i]. The Eisenstein reciprocity covers the case n = l for
an odd prime l in the cyclotomic ﬁeld Z[ζl].
Quadratc reciprocity can be used to solve the problem of whether a prime can
be expressed in the form x2 + ny2, where x, y ∈ Z and n is a ﬁxed integer. In
particular, if x2 + ny2 ≡ 0 (mod p) and (x, y) = 1, then x2 ≡ −ny2 (mod p), so n
must be a square modulo p. Conversely, if n is a square modulo p then p|(x2 + ny2).
When n = 1, 2, 3, if p|(x2 + ny2) for x, y relatively prime, then p can be written as
p = x2 + ny2 , thus in these cases of n quadratic reciprocity provides a complete
characterization of primes expressable as x2 + ny2. Reciprocity laws also have
applications in cryptography; for example, biquadratic reciprocity can be used to
identify the encrypted message in the Rabin public-key cryptosystem.
We begin with the discussion of quadratic reciprocity in Section 2, where we ﬁrst
introduce prime splitting in number ﬁelds before proceeding to a proof. We then
proceed to establishing preliminaries for higher reciprocity with a brief introduction
of characters, Gauss sums, and Jacobi sums in Section 3, before diving into cubic,
biquadratic, and Eisenstein reciprocity in Sections 4, 5, and 6, respectively.

1

2 NANCY XU

For this paper, we will assume basic knowledge of abstract algebra and Galois
Theory.
 2. Quadratic Reciprocity

To formulate quadratic reciprocity we will introduce the Legendre symbol, an
indicator function whose output is determined by whether the input integer is a
square modulo a prime p. While quadratic reciprocity has many equivalent for-
mulations, its symmetry is the most apparent when presented using the Legendre
symbol.

Deﬁnition 2.1. For a, p ∈ Z, p a prime, deﬁne the Legendre symbol as

(
a
p
) =
 




1 if a is a square modulo p and p ∤ a
−1 if a is not a square modulo p
0 if p|a.

Proposition 2.2. Let a, b, p ∈ Z, where p is a prime. We have the following
properties:

(1) (Euler’s Criterion) a p−1
2 ≡ (a
p) (mod p).
(2) (ab
p ) = (a
p)(b
p).
(3) If a ≡ b (mod p), then (a
p) = (b
p).

Proof. (2) and (3) are clear from deﬁnition, so we will only prove (1).
Let γ be a generator of Fp, α ≡ γa (mod p), and x ≡ γn (mod p) for positive
integers a, n. Then x2 ≡ α (mod p) is solvable if and only if 2n ≡ a (mod p − 1) is
solvable, where the latter is true when 2|a, as (2, p − 1) = 2. Since γ is a generator,
this condition holds if and only if γ a(p−1)
2 ≡ 1 (mod p). □

Proposition 2.2 (2) is a particularly nice property, since using quadratic reci-
procity it is possible to determine when an arbitrary integer is a square modulo p
by decomposing it into primes and using this multiplicative property. The law of
quadratic reciprocity is as follows:

Theorem 2.3. For odd primes p, q ∈ Z,
(
p
q
)(q
p
) = (−1) p−1
2 · q−1
2 .

Moreover, we have the following supplements:

• (First Supplement) (−1
p ) = (−1) p−1
2 .

• (Second Supplement) (2
p) = (−1) p2−1
8 .

The ﬁrst supplement follows directly from Proposition 2.2 (1). We will present a
proof of the second supplement using prime splitting; it is not the simplest known
proof but motivates some of the ideas in higher reciprocity laws. Our strategy is as
follows: In Section 2.1, we will show that Q[p∗], where p∗ = (−1) p−1
2 p, is the unique
quadratic subﬁeld of Q[ζp]. Section 2.2 shows that a prime q splits completely in an
intermediate ﬁeld if and only if this ﬁeld contains the decomposition ﬁeld, and we
will show that Q[p∗] satisﬁes this property in Section 2.4. Section 2.3 shows that q
splits completely in Q[p∗] if and only if p∗ is a square modulo q, and ﬁnally Section
2.4 will show that q is a square modulo p if and only if q splits completely in Q[p∗]

RECIPROCITY LAWS 3

and tie together the pieces from the previous sections. Relevant terminology will
be deﬁned in the next few sections.

2.1. Quadratic Subﬁeld. In this section, we will determine the unique quadratic
subﬁeld of Q[ζp] by computing the discriminant of the pth roots of unity using
norms. Consider a number ﬁeld K/Q of degree n with σ1, . . . , σn as the n embed-
dings of K ∈ C.

Deﬁnition 2.4. The norm of an element α ∈ K is given by

N (α) = σ1(α)σ2(α) . . . σn(α).

Deﬁnition 2.5. For any n-tuple α1, . . . , αn ∈ K, the discriminant of α1, . . . , αn is
given by ∆(α1, . . . , αn) = |σi(αj)|2,

i.e. the square of the determinant of the matrix with σi(αj) in the ith row and jth
column.

As deﬁned, the discriminant is quite diﬃcult to calculate, but interpreting it as
the norm of a polynomial can simplify computations.

Proposition 2.6. For a ring Q[α], let f be the monic irreducible polynomial for α
over Q and α1, . . . , αn be the conjugates of α. Then

∆(1, α, . . . , αn−1) = ∏

1≤r<s≤n(αs − αr)
2 = ±N (f ′(α),

where the + sign holds if and only if n ≡ 0, 1 (mod 4).

Proof. Let σi be the automorphism such that σi(α) = αi, where 1 ≤ i ≤ n. To
show the ﬁrst equality, we have

|σi(αj)| = |σi(α)
j| = |αj
i |,

where |αj
i | is a Vandermonde determinant. Thus

|a
j
i |
2 =
 

 ∏

1≤r<s≤n(αs − αr)




2
 = ∏

1≤r<s≤n(αs − αr)
2.

Now ∆(1, α, . . . , αn−1) = (−1)
 n(n−1)
2 ∏

1≤r<s≤n
(αr − αs),

so (−1) n(n−1)
2 = 1 if and only if n ≡ 0, 1 (mod 4). Since f ′ has rational coeﬃcients,
it follows that

N (f ′(α)) =
 n∏

r=1 σr(f ′(α)) =
 n∏

r=1 f ′(σr(α)) =
 n∏

r=1 f ′(αr).

Since f (x) = ∏

i(x − αi), for each r, we have f ′(αr) = ∏

i̸=r(αr − αi), which shows
the second equality. □

Proposition 2.7. Let p ∈ Z be a prime, and deﬁne p∗ = (−1) p−1
2 p. Then √p∗ ∈
Q[ζp].

4 NANCY XU

Proof. We will ﬁrst apply Proposition 2.6 to compute ∆(1, ζp, . . . , ζ p−2
p ) in Q[ζp].
The irreducible polynomial of ζp is given by f (x) = 1 + x + . . . + xp−1, which
can be rewritten as xp − 1 = (x − 1)f (x). We diﬀerentiate the equation to get
pxp−1 = f (x)+(x−1)f ′(x), and substituting x = ζp gives us f ′(ζp) = p/(ζp(ζp−1)).
We take the norm to get
 N (f ′(ζp)) = N (p)
N (ζp)N (ζp − 1) .

Since Q[ζp] is a Galois extension over Q, the embeddings of Q[ζp] into C are precisely
the elements in the Galois group of Q[ζp] over Q. We have

N (p) = p
p−1

N (ζp) =
 p−1∏

i=1 ζ i
p = ζ
 p(p−1)
2
p = 1

N (ζp − 1) = N (−1)N (1 − ζp) = (−1)p−1 p−1∏

i=1(1 − ζ i
p) = p.

Then N (f ′(ζp)) = ±p
p−2, where the + sign holds if and only if p ≡ 1 (mod 4)
by Proposition 2.6. From the deﬁnition of the discriminant, its square root must be
in Q[ζp], which we ﬁnd to be √
±pp−2 = p p−3
2 √p∗, so √p∗ ∈ Q[ζp] as desired. □

Corollary 2.8. The unique quadratic subﬁeld of Q[ζp] is Q[√p∗].

Proof. The Galois group G of Q[ζp] over Q is cyclic of order p−1, so it has a unique
subgroup of order 2. By the Main Theorem of Galois Theory, there exists a unique
quadratic subﬁeld of Q[ζp], which by Proposition 2.7 is Q[
√p∗]. □

2.2. Prime Splitting. Prime elements often do not remain irreducible in a larger
ring; for example, while 2 is prime in Z, it splits in Z[i] as 2 = (1 + i)(1 − i).
Splitting becomes complicated in rings that are not unique factorization domains,
thus we will instead work with prime ideals instead of prime elements, since prime
ideals can be decomposed uniquely in Dedekind domains.
We begin by establishing notation for this subsection. Let K, L be ﬁeld ex-
tensions of Q such that K ⊂ L. For an arbitrary ﬁeld F , let OF be the ring of
integers associated to F . Let P ⊂ OK and Q ⊂ OL be prime ideals in their respec-
tive number rings. The goal of this section is to determine the ﬁelds K ′ such that
K ⊂ K ′ ⊂ L in which every prime ideal P ⊂ OK splits completely in K ′.

Deﬁnition 2.9. A prime P ⊂ OK splits completely in OL if and only if P splits
into [L : K] distinct primes.

We do so by showing that every prime in OK splits completely in what we will
call the decomposition ﬁeld, and that all intermediate ﬁelds satisfying this property
contain this ﬁeld. Before we proceed, it is important to establish some preliminary
deﬁnitions to describe a prime decomposition:

Deﬁnition 2.10. Q lies over P , or P lies under Q, if Q|P OL. Equivalently,
P ⊂ Q, or alternatively Q ∩ OK = P .

Every prime Q ⊂ OL lies over a unique prime P ⊂ OK, and the argument goes
as follows: for a nonzero α ∈ Q, there exists an ai ∈ OK such that αm + a1αm−1 +
. . . + am = 0, where we can assume that am ̸= 0 since we’re working in the ﬁeld L,

RECIPROCITY LAWS 5

so am ∈ Q ∩ OK and Q ∩ OK is nonempty. Since 1 /∈ Q, it follows that Q ∩ OK is
prime.

Deﬁnition 2.11. The ramiﬁcation index e is the unique nonnegative integer such
that P ⊂ Q
e and P ̸⊂ Q
e+1, denoted as e(Q|P ).

In other words, if we decompose P ⊂ OK in OL as P = Q
e1
1 Q
e2
2 . . . Q
eg
g , then
Q1, Q2, . . . , Qg lie over P and have ramiﬁcation indices e1, e2, . . . , eg, respectively.
The containment of OK in OL induces a ring homomorphism OK −→ OL/Q
with kernel OK ∩ Q = P , thus OK/P embeds in OL/Q, and OL/Q is a ﬁnite ﬁeld
extension of OK/P .

Deﬁnition 2.12. The degree of the ﬁeld extension f of OL/Q over OK/P is the
inertial degree of Q over P , denoted as f (Q|P ).

One useful property regarding ramiﬁcation degrees and inertial ﬁelds is that
they are multiplicative in towers, i.e. if P ⊂ Q ⊂ U are prime ideals in the ring of
integers of the ﬁeld extension F ⊂ L ⊂ K, then

e(U |P ) = e(U |Q)e(Q|P )

f (U |P ) = f (U |Q)f (Q|P ).

The next two Propositions will relate the ramiﬁcation index, inertial degree, and
the degree of the extension K ⊂ L for when the extension L/K is Galois.

Proposition 2.13. Let Q, Q
′ ⊂ OL be prime ideals lying over the prime ideal
P ⊂ OK. Then σ(Q) = Q
′ for some σ ∈ G(L/K).

Proof. See Section 3, Theorem 23 of Marcus [5]. □

In other words, the Galois group of L/K permutes the prime ideals lying over
P transitively.

Proposition 2.14. Let n = [L : K], and write P OL = Q
e1
1 Q
e2
2 . . . Q
eg
g , where
Qi ∈ OL is a prime ideal for 1 ≤ i ≤ g and Qi = Qj if and only if i = j. Then
e1 = e2 = . . . = eg and f1 = f2 = . . . = fg. Let e and f denote these common
values. Then gef = n.

Proof. See Section 3 of Marcus [5] or Section 12.3, Theorem 3’ of Ireland and Rosen
[3]. □

Proposition 2.14 is particularly useful in characterizing primes when n is small,
as we will see in Sections 4 and 5. For now, if we want to show that every prime
splits completely in an intermediate ﬁeld K ′, it is enough for us to prove that
[K : K ′] = g and e = f = 1.
For groups H, G, we write H ⊂ G if H is an arbitrary subgroup of G and H ▹ G
if H is a normal subgroup of G.

Deﬁnition 2.15. Let G be the Galois group of L/K, and suppose that Q lies over
P . The decomposition group D ⊂ G is given by D = D(Q|P ) = {σ ∈ G : σQ = Q}.
The ﬁxed ﬁeld LD of of D is called the decomposition ﬁeld.

It follows that D = G(L/LD). It can also be checked that D is indeed a subgroup
of G.

6 NANCY XU

Proposition 2.16. Let g be the number of distinct prime ideals in the decomposi-
tion of P in OL. Let QD ∈ D(Q|P ) be a prime ideal over P . Then [LD : K] = g
and e(QD|P ) = f (QD|P ) = 1.

Proof. We know from Galois Theory that [LD : K] = [G : D], so it is enough to
compute the latter. Every left coset σD, σ ∈ G, sends Q to σQ. We know that
σD = τ D if and only if σQ = τ Q, for any σ, τ ∈ G, so there exists a bijection
between the set of left cosets σD and set of primes σQ. But by Proposition 2.13,
primes of the form σQ are precisely those lying over P , hence there are g of them
and [LD : K] = g.
To show e(QD|P ) = f (QD|P ) = 1, notice that Q is the only prime in S lying
over P , since primes lying over P are permuted transitively by D = G(L/LD).
By Proposition 2.14, we have [L : LD] = e(Q|QD)f (Q|QD). Our previous results
shows that [LD : K] = g, hence again by Proposition 2.14, it follows that [L : LD] =
e(Q|P )f (Q|P ). But e(Q|QD) ≤ e(Q|P ) and f (Q|QD) ≤ f (Q|P ), so e(Q|QD) =
e(Q|P ) and f (Q|QD) = f (Q|P ). Since ramiﬁcation indices and inertial degrees are
multiplicative in towers, we get e(QD|P ) = f (QD|P ) = 1, as desired. □

Corollary 2.17. If D ▹ G, P splits into g distinct primes in OLD .

Proof. Since D is a normal subgroup of G, LD/K is a Galois extension, so the
primes lying over P are transitive. Thus from proposition 2.16, it follows that for
any P ′ ⊂ LD lying over P , we have e(P ′|P ) = f (P ′|P ) = 1. Since [LD : K] = g, it
follows again from Proposition 2.14 that P splits into g distinct primes in LD. □

Proposition 2.18. Let P ′ ⊂ OK be a prime lying over P . Then LD is the largest
intermediate ﬁeld K ′ such that e(P ′|P ) = f (P ′|P ) = 1.

L LDK ′ K ′

LD K

e′f ′

ef
 r′

r

Proof. Suppose that K ′ is the ﬁxed ﬁeld of some H ⊂ G. We know L is a Ga-
lois extension of K ′, thus the decomposition group of Q over P ′ ⊂ K is given
by D(Q|P ′) = D ∩ H. Therefore, from Galois Theory it follows that LDK ′

is the decomposition ﬁeld for Q over P . By Theorem 2.16 and the multiplica-
tivity of the degree of ﬁeld extensions, we get [L : LD] = e(Q|P )f (Q|P ) and
[L : LDK ′] = e(Q|P ′)f (Q|P ′). But by multiplicativity e(Q|P ′)e(P ′|P ) = e(Q|P )
and f (Q|P ′)f (P ′|P ) = f (Q|P ), so since e(P ′|P ) = f (P ′|P ) = 1, we have [L :
LD] = [L : LDK ′]. Thus [LDK ′ : LD] = 1 and K ′ ⊂ LD, as desired. □

Corollary 2.19. Let K ′ be a ﬁeld such that K ⊂ K ′ ⊂ L. If D ▹ G, then P splits
completely in K if and only if K ′ ⊂ LD.

Proof. First, by Proposition 2.14, P splits completely in K ′ if and only if e(P ′|P ) =
f (P ′|P ) = 1 for a prime P ′ ⊂ OK′ lying over P . Thus Proposition 2.18 tell us that
K ′ ⊂ LD if P splits completely in K ′, and conversely if K ′ ⊂ LD, Corollary 2.17
tells us that P splits completely in K ′. □

RECIPROCITY LAWS 7

2.3. Prime Splitting in Quadratic Fields. Our next task is to show that a
prime q splits completely in Q[p∗] if and only if it is a square modulo p. To
determine the decomposition of prime ideals in quadratic ﬁelds, ﬁrst notice that by
Proposition 2.14 there are only three ways a prime can decompose in a quadratic
ﬁeld; since gef = 2, either (e, f, g) = (2, 1, 1), (1, 1, 2) or (1, 2, 1). The prime
splits completely only in the second case. For this subsection, let K = Q[
√d] be a
quadratic ﬁeld with d ∈ Z square-free.

Proposition 2.20. Let p ∈ Z be an odd prime. The splitting behavior of p in K
is as follows:
(1) If p ∤ d and d is a square modulo p, then (p) = P P ′, where P ̸= P ′.
(2) If p ∤ d and d is not a square modulo p, then (p) = P .
(3) If p|d, then (p) = P 2.
Here P and P ′ are prime ideals in OK.

Proof. For (1), suppose that p ∤ d and a
2 ≡ d (mod p) for some a ∈ Fp. We
have (p, a + √d)(q, a − √d) = (p)(p, a + √d, a − √d, (a
2 − d)/p), where the latter
ideal contains 2a = (a + √d) + (a − √d) and p, which are relatively prime, so
OK = (p, a + √d, a − √d, (a
2 − d)/p). Let P = (p, a + √d) and P ′ = (p, a − √d).
If P = P ′, then 2a, p ∈ P and P = OK, so P ̸= P ′.
For (2), suppose that p ∤ d and d is not a square modulo p, and let P ⊂ OK be
a prime ideal lying over p. If f (P |p) = 1, then Fp ∼= OK/P , so there exists some
a ∈ Fp such that a ≡ √d (mod p). But then a
2 ≡ d (mod p), which contradicts
our assumption, so f (P |p) = 2 and P is the only prime lying over p.
For (3), suppose that p|d. Then (p, √d)
2 = (p2, p
√d, d) = (p)(p, (d/p)√d). We
know p and d/p are relatively prime since d is square-free, so OK = (p, (d/p)
√d).
Setting P = (p, √d)
2 gives us what we want. □

The prime decomposition of p = 2 can be found in a similar manner.

Proposition 2.21. Suppose p = 2.
(1) If m ≡ 1 (mod 8), then (2) = P P ′, where P ̸= P ′.
(2) If m ≡ 5 (mod 8), then (2) = P .
(3) If m ≡ 3 (mod 4), Then (2) = P 2.

Proof. The same argument as in Proposition 2.20 shows that

• If m ≡ 1 (mod 8), then (2) = (2, 1+
√m
2 )(2, 1−√m
2 ).
• If m ≡ 3 (mod 4), then (2) = (2, 1 + √m)2.
This will show (1) and (3). For (2), if we suppose the contrary, then as in
Proposition 2.20 there exists an integer a ∈ Z such that a ≡ (1 + √m)/2 (mod P ).
But since (1+√m)/2 satisﬁes x2 −x+(1−d)/4, it follows that a
2 −a+(1−d)/4 ≡ 0
(mod 2). However, 2|(a
2 − a) for all a ∈ Z, so it follows that (1 − d)/4 ≡ 0 (mod 2)
and d ≡ 1 (mod 8), giving us a contradiction. □

2.4. Proof. We are now ready to assemble the proof of quadratic reciprocity. Be-
fore we do so, we need one more result concerning the splitting behavior in cyclo-
tomic ﬁelds.

Proposition 2.22. Let p, m ∈ Z be such that p is a prime and and p ∤ m. Let f
be the order of p modulo m. Then (p) = P1P2 . . . Pg in OQ[ζp], where the Pis are
distinct prime ideals with f (Pi|P ) = f and g = φ(m)/f .

8 NANCY XU

Proof. See Section 13.2, Theorem 2 of Ireland and Rosen [3]. □

Let Fd ⊂ Q[ζp] be the unique subﬁeld of degree d over Q for each divisor d of
p − 1. The next proposition will use Proposition 2.22 to relate prime splitting and
being a square modulo p.

Proposition 2.23. Let p, q ∈ Z be odd primes such that p ̸= q. For a divisor d of
p − 1, q is a dth power modulo p if and only if q splits completely in Fd.

Proof. By Proposition 2.22, q splits into g distinct primes in Q[ζp], where each
prime has order f = (p − 1)/r, where f is the order of q in F
×
p . Let γ ∈ F×
p generate
the ﬁeld. Then the dth powers {γd, γd
2 , . . . , γd
p−1} form the unique subgroup of
order (p − 1)/d. Since f is the order of q, we know that q is a dth power modulo
p if and only f |(p − 1)/d, which is true if and only if Fd ⊂ Fr. We know that the
decomposition ﬁeld has degree r over Q and Fr is the only such ﬁeld, thus Fr is
the decomposition ﬁeld. By Corollary 2.19, the condition Fd ⊂ Fr is equivalent to
q splitting completely in Fd. □

All that is left of the proof is tying together the results established thus far.

Proof. Proposition 2.23 tells us that (q
p) = 1 if and only if q splits completely in
F2, which we found to be Q[
√p∗] in Corollary 2.8. By Proposition 2.20, q splits
completely in Q[√p∗] if and only if (p∗
q ) = 1, thus
(q
p
) = (p∗
q
 ) = ((−1) p−1
2
q
 )(p
q
) = (−1) p−1
2 · q−1
2 (p
q
),

so (
p
q
)(q
p
) = (−1) p−1
2 · q−1
2 ,

as desired.
The same argument and Proposition 2.21 proves the second supplement. □

3. Gauss and Jacobi Sums

To prove the cubic, biquadratic, and Eisenstein reciprocity laws, it is necessary
to introduce Gauss and Jacobi sums as well as their essential properties. These
sums are deﬁned in terms of characters.

Deﬁnition 3.1. A multiplicative character on Fp is a map χ : F
×
p −→ C× satisfying
χ(a)χ(b) = χ(ab) for all a, b ∈ F×
p .

Let a ∈ F
×
p . The multiplicative character satisﬁes the following properties:
(1) χ(1) = 1.
(2) χ(a) is a (p − 1)th root of unity.
(3) χ(a
−1) = χ(a)−1 = χ(a).
The Legendre symbol is an example of a multiplicative character, and so are
its analogs for higher reciprocity laws. Another example is the trivial character
ϵ(a) = 1 for all a ∈ F
×
p . It is sometimes useful to extend the deﬁnition of χ to all
of Fp by letting ϵ(0) = 0 and χ(0) = 1 for all χ ̸= ϵ.
The following will be useful in proving certain properties of Gauss and Jacobi
sums.
 RECIPROCITY LAWS 9

Proposition 3.2. Let χ be a character on Fp. Then

∑

t∈Fp χ(t) =
 {0 if χ ̸= ϵ
p if χ = ϵ.

Proof. If χ = ϵ, then ϵ(t) = 1 for all t ∈ Fp, so the sum equals p. Otherwise, ﬁx an
a ∈ F
×
p . Then
 χ(a) ∑

t∈Fp χ(t) = ∑

t∈Fp χ(at) = ∑

t∈Fp χ(t),

since multiplication by a permutes the elements in Fp. Since χ(a) ̸= 1, it follows
that ∑

t∈Fp χ(t) = 0. □

We will now introduce Gauss and Jacobi sums.

Deﬁnition 3.3. Let χ be a character on Fp. The Gauss sum on Fp belonging to
χ is deﬁned as ga(χ) = ∑

t∈Fp χ(t)ζ at
p .

For simplicity of notation, let g1(χ) = g(χ). For a ∈ F
×
p and χ a nontrivial
character on Fp, we have:

χ(a)ga(χ) = χ(a) ∑

t∈Fp χ(t)ζ at
p = ∑

t∈Fp χ(at)ζ at
p = g(χ),

which gives us the identity ga(χ) = χ(a
−1)g(χ).

Proposition 3.4. Let χ ̸= ϵ be a character on Fp. Then |g(χ)|
2 = p.

Proof. The strategy is to compute ∑

a∈Fp ga(χ)ga(χ) in two diﬀerent ways.

First, if a ̸= 0 we can write ga(χ) = χ(a
−1)g(χ) and ga(χ) = χ(a−1)g(χ) =
χ(a)g(χ), so taking the sum over Fp gives us
∑

a∈Fp ga(χ)ga(χ) = ∑

a∈Fp χ(a)χ(a−1)g(χ)g(χ) = (p − 1)g(χ)g(χ),

since χ(a)χ(a
−1) = 1 for a ̸= 0 and χ(0)χ(0) = 0.
Next, using the deﬁnition of Gauss sums, we have
∑

a∈Fp ga(χ)ga(χ) = ∑

a∈Fp
 ∑

x,y∈Fp χ(x)χ(y)ζ a(x−y)
p = ∑

x,y∈Fp χ(x)χ(y) ∑

a∈Fp ζ a(x−y)
p . (∗)

When x ̸= y, the inner expression sums over all pth roots of unity, which equals
zero since ∑

i∈Fp ζ i
p = (ζ p
p − 1)/(ζp − 1) = 0. When x = y, the inner expression

sums to p. We know that χ(x)χ(x) = 1 if x ̸= 0 and χ(0)χ(0) = 0, so (∗) reduces
to ∑

x∈Fp χ(x)χ(x)p = (p − 1)p.

Equating the two expressions gives us |g(χ)|
2 = p. □

There is also a nice relationship between g(χ) and g(χ):

g(χ) = ∑

t∈Fp χ(t)ζ −t
p = χ(−1) ∑

t∈Fp χ(−t)ζ −t
p = χ(−1)g(χ),

so the result from Proposition 3.4 can also be expressed as

g(χ)g(χ) = χ(−1)p.

10 NANCY XU

The Jacobi sum is very similar to the Gauss sum and the two sums are very
much related, as we’ll see in the next proposition. We will primarily use Jacobi
sums to decompose certain Gauss sums into primes.

Deﬁnition 3.5. For characters χ, λ of Fp, the Jacobi sum is deﬁned to be J(χ, λ) =∑
x+y=1 χ(x)λ(y).

Proposition 3.6. Let χ, λ be nontrivial characters of Fp such that χλ ̸= ϵ. Then
J(χ, λ) = g(χ)g(λ)/g(χλ).

Proof. Note that
 g(χ)g(λ) =
 

 ∑

x∈Fp χ(x)ζ x
p
 


 

 ∑

y∈Fp λ(y)ζ y
p
 



= ∑

x,y∈Fp χ(x)λ(y)ζ x+y
p

= ∑

t∈Fp
 ( ∑

x+y=t χ(x)λ(y)

)
 ζ t
p.

Since χ, λ are characters, χλ must also be a character. If t = 0, by Proposition
3.2 we have ∑

x+y=0 χ(x)λ(y) = ∑

x∈Fp χ(x)λ(−x) = λ(−1) ∑

x∈Fp χ(x)λ(x) = 0.

If t ̸= 0, let x
′, y′ be such that x = tx′ and y = ty′, so the condition x + y = t
becomes x′ + y′ = 1. Then
∑

x+y=t χ(x)λ(y) = ∑

x′+y′=1 χ(tx
′)λ(ty′) = χ(t)λ(t)J(χ, λ),

so g(χ)g(λ) = ∑

t∈Fp χ(t)λ(t)J(χ, λ)ζ t
p = J(χ, λ)g(χλ),

as desired. □

4. Cubic Reciprocity

Cubic reciprocity answers the question of when a prime is a perfect cube mod-
ulo another prime. Similar to in quadratic reciprocity, we will formulate cubic
reciprocity in terms of the cubic residue character, which will best display the un-
derlying symmetry. We will see that the cubic residue character is either 0 or a
third root of unity, so it makes sense for us to work in Z[ζ3] instead of Z for cubic
reciprocity.
Our ﬁrst step is to determine the prime elements in Z[ζ3]. Every prime in Z[ζ3]
lies over a unique prime in Z, so the primes in Z[ζ3] can be completely characterized
using Proposition 2.22:

Proposition 4.1. Let p ∈ Z be a rational prime.
(1) If p ≡ 1 (mod 3), then p = ππ, where π is prime in Z[ζ3].
(2) If p ≡ 2 (mod 3), then p is prime in Z[ζ3].
(3) If p = 3, then p = −ζ 2
3 (1 − ζ3)
2, where 1 − ζ3 is prime in Z[ζ3].

RECIPROCITY LAWS 11

Let π ∈ Z[ζ3] be a prime such that N π ̸= 3. For any α relatively prime to π, the
analog of Fermat’s Little Theorem states that αN π−1 ≡ 1 (mod π). The residue
classes of 1, ζ3, ζ 2
3 are distinct modulo π and α N π−1
3 is a third root of unity, thus
there must be a unique m modulo 3 such that α N π−1
3 ≡ ζ m
3 (mod π).

Deﬁnition 4.2. If N π ̸= 3, the cubic residue character of α modulo π is given by
(1) (α
π)
3 = 0 if π|α.

(2) (α
π)
3 = ζ m
3 where m is the unique integer modulo 3 such that α N π−1
3 ≡ ζ m
3
(mod π), if π ∤ α.

The cubic residue character is also a multiplicative character, and it satisﬁes
similar properties to the Legendre symbol:

Proposition 4.3. For π, α ∈ Z[ζ3] where π is prime,
(1) (α
π)
3 = 1 if and only if x3 ≡ α (mod π) is solvable, i.e. if and only if α is
a cubic residue.
(2) (αβ
π )
3 = (α
π)
3(β
π)
3.
(3) If α ≡ β (mod π), then (α
π)
3 = (β
π)
3.

Proof. (2) and (3) are clear from deﬁnition, and the proof of (1) is similar to that
of Proposition 2.2, but instead we work in [Z[ζ3]/πZ[ζ3].
As before, the multiplicative property will allow us to determine whether any
α ∈ Z[ζ3] is a perfect cubic modulo a prime, since we can factor α into primes and
use multiplicativity. □

Every element in Z[ζ3] has 6 associates, including itself, so it is enough to deter-
mine the reciprocity law for one of its associates and the units in Z3. We will state
cubic reciprocity for one such associate – which we will designate primary – and
the units will be taken care of in the supplementary laws. See Section 9.3, Theorem
1 of Ireland and Rosen [3] for the supplements.

Deﬁnition 4.4. A prime π ∈ Z[ζ3] is primary if π ≡ 2 (mod 3).

Proposition 4.5. Let N π = p ≡ 1 (mod 3). Then exactly one of the associates of
π is primary.

Proof. Write π = a + bζ3. We will ﬁrst prove existence. The associates of π are

a + bζ3, −b + (a − b)ζ3, (b − a) − aζ3, −a − bζ3, b + (b − a)ζ3, (a − b) + aζ3.

Since p = a
2 − ab + b
2 ≡ 1 (mod 3), either 3 ∤ a or 3 ∤ b. Thus the ﬁrst term of
either the ﬁrst or second associate is not divisible by 3, so suppose 3 ∤ a. Similarly,
from the ﬁrst and fourth associates, we can further assume that a ≡ 2 (mod 3).
Now 1 ≡ 4 − 2b + b2 (mod 3), so b(b − 2) ≡ 0 (mod 3). If 3|b, the a + bζ3 is primary,
and if b ≡ 2 (mod 3), then b + (b − a)ζ3 is primary.
To prove uniqueness, suppose that a + bζ3 is primary. It is clear from taking
congruences modulo 3 that no other associate is primary. □

We are now in a position to state the law of cubic reciprocity.

Theorem 4.6 (Cubic Reciprocity). Let π1, π2 ∈ Z[i] be primary primes with
N π1, N π2 ̸= 3 and N π1 ̸= N π2. Then
(π1
π2
)

3 = (π2
π1
)
3.

12 NANCY XU

For simplicity of notation, let χπ = ( ·
π)
3 for the remainder of this section. Let
π ∈ Z[ζ3] be a complex prime. Then N π = p ≡ 1 (mod 3) for an odd rational
prime p. We know Z[ζ3]/πZ[ζ3] is a ﬁnite ﬁeld of characteristic p, so Z[ζ3]/πZ[ζ3]
is isomorphic to Fp. Then we can consider χπ as a character on Fp, which allows
us to work with G(χπ) and J(χπ, χπ).
The proof will proceed as follows: We will ﬁrst ﬁnd the prime factorization of
g(χπ)
3 in Z[ζ3] by writing it in terms of a Jacobi sum, which is easier to compute.
We will then separate into cases based on whether π1, π2 are complex or rational
primes, but the general procedure will be to deduce reciprocity by rewriting a Gauss
sum in two diﬀerent ways.
The following propositions will lead us to the prime factorization of g(χπ)
3.

Proposition 4.7. Let χπ be the cubic residue character, where π is primary. Then
g(χπ)
3 = pJ(χπ, χπ).

Proof. Proposition 3.6 tells us that

g(χπ)
3 = g(χπ)g(χ
2
π)J(χπ, χπ) = g(χπ)g(χπ)J(χπ, χπ).

Using Proposition 3.4 and observing that χπ(−1) = χπ((−1)3) = 1, we get g(χπ)
3 =
pJ(χπ, χπ). □

Proposition 4.8. Let χπ be as before. Then J(χπ, χπ) = π.

Proof. Proposition 3.4 and Proposition 3.6 tells us that J(χπ, χπ)J(χπ, χπ) = p,
where we recall that N π = p ≡ 1 (mod 3) and p is a rational prime. Thus J(χπ, χπ)
is a prime in Z[ζ3] with norm p. Reducing modulo 3 gives us:

g(χπ) =
 

 ∑

t∈Fp χπ(t)ζ 3t
p
 



3
 ≡ ∑

t∈Fp χπ(t)3ζ 3t
p (mod 3).

Since χπ is cubic, we have χ(0) = 0 and χ(t)3 = 1 for t ̸= 0, so ∑
t∈Fp χπ(t)3ζ 3t
p =
−1. Then pJ(χπ, χπ) = g(χπ)
3 ≡ −1 (mod 3),
and since p ≡ 1 (mod 3), we have J(χπ, χπ) ≡ −1 + 0 · ζ3 (mod 3). Thus J(χπ, χπ)
is in fact a primary prime.
Let J(χπ, χπ) = π′. We know p = ππ = π′π′, so either π|π′ or π|π′, and since
the primes are primary, either π = π′ or π = π′. We want to show the former. We
have J(χπ, χπ) = ∑

t∈Fp χπ(t)χπ(1 − t) = ∑

t∈Fp t p−1
3 (1 − t) p−1
3 (mod π)

by deﬁnition. The coeﬃcients in the polynomial are of the form a ∑
c∈Fp c
k for
some a and (p − 1)/3 ≤ k < 2(p − 1)/3, so if γ is a generator of Fp, the sum reduces
as
 a ∑

c∈Fp c
k = a
 p−1∑

i=1 γik = a γ(p−1)k − 1
γk − 1 ≡ 0 (mod p),

since (k, p − 1) = 1. Thus J(χπ, χπ) ≡ 0 (mod π) and π = π′, as desired. □

Corollary 4.9. With deﬁnitions as above, we have g(χπ)3 = π2π = pπ.

Proof. This follows directly from Propositions 4.7 and 4.8. □

RECIPROCITY LAWS 13

We can now present the proof of cubic reciprocity.

Proof. We will consider three cases: if π1, π2 are both rational primes, one is rational
and one is complex, and both are complex.
Case 1. Suppose that π1 = q and π2 = p, where p, q are rational primes. We
need a few preliminary results:
(1) χπ(α) = χπ(α)2 = χπ(α2).
(2) χπ(α) = χπ(α).
(3) χp(n) = 1 if n is a rational integer relatively prime to p.
For (1), χπ(α) equals 1, ζ3, or ζ 2
3 , and in each case its square is equal to its
conjugate. For (2), by deﬁnition we have

α N π−1
3 ≡ χπ(α) (mod π),

and taking the conjugate gives us

α N π−1
3 ≡ χπ(α) (mod π).

Since N π = N π, we have χπ(α) ≡ χπ(α) (mod π), thus χπ(α) ≡ χπ(α). To show
(3), we have from (1) and (2) that

χp(n) = χp(n) = χp(n)
2,

so χp(n) = 1. From (3), χq(p), χp(q) = 1, so χq(p) = χp(q) trivially.
Case 2. Suppose that π1 = q ≡ 2 (mod 3) is a rational prime and π2 is a
complex prime with norm p ≡ 1 (mod 3). Raising both side of g(χπ2) = pπ to the
(q2 − 1)/3th power and reducing modulo q gives us

g(χπ2)q2−1 = (pπ2) q2−1
3 ≡ χq(pπ2) (mod q).

But χq(p) = 1 by Case 1, so

g(χπ)
q2 ≡ χq(π2)g(χπ2 ) (mod q).

Expanding g(χπ2)q2 using the deﬁnition of Gauss sums gives us

g(χπ2)q2 =
 

 ∑

t∈Fp(t)ζ t
p



q2
 ≡ ∑

t∈Fp χπ2(t)q2 ζ q2t
p (mod q).

Since q2 ≡ 1 (mod 3) and χπ2 is a cubic residue, the expression simpliﬁes as

g(χπ2)q2 ≡ χq2(χπ2) ≡ χπ2 (q−2)g(χπ2 ) ≡ χπ(q)g(χπ2) (mod q).

Putting everything together, we have χπ2 (q)g(χπ2) ≡ χq(π2)g(χπ2) (mod q), so
multiplying both sides by g(χπ) and then by p−1 gives us χπ2(q) ≡ χq(π2) (mod q),
so it follows that χπ2(q) = χq(π).
Case 3. Suppose that π1, π2 are complex primes with N π1 = p1 and N π2 = p2
such that p1, p2 ≡ 1 (mod 3). From g(χπ1)3 = p1π1, raising both sides to the
(N π2 − 1)/3 = (p2 − 1)/3th power, taking the congruence modulo π2, and applying
the same argument as in the second case gives us

χπ1(p
2
2) = χπ2(p1π1).

Similarly, raising both sides of g(χπ2 )
3 = p2π2 to the (p1 − 1)/3th power and
reducing modulo π1 gives us
 χπ2 (p2
1) = χπ1 (p2π2).

14 NANCY XU

It follows from Case 1 (2) that χπ1 (p
2
2) = χπ1(p2). Then

χπ1(π2)χπ2 (p1π1) = χπ1(π2)χπ1(p
2
2)

= χπ1(π2)χπ1(p2)

= χπ2(p
2
1)

= χπ2(π1)χ(p1π1),

so it follows that χπ1(π2) = χπ2 (π1). □

5. Biquadratic Reciprocity

Biquadratic reciprocity addresses the question of when an element is a perfect
fourth power modulo another element relatively prime to it. The major distinction
between this and the previous two reciprocity laws is that it is no longer stated
for primes, but for elements that are relatively prime, thus new notation is needed.
However, much of the proof techniques will be similar to in cubic reciprocity, hence
some details in this section will be omitted. The biquadratic residue character will
either be 0 or a fourth root of unity, hence we will work in Z[i]. We can characterize
the primes in Z[i] by decomposing primes in Z using Proposition 2.22.

Proposition 5.1. Let p ∈ Z be a rational prime.
(1) If p ≡ 1 (mod 4), then p = ππ, where π is prime in Z[i].
(2) If p ≡ 3 (mod 4), then p is prime in Z[i].
(3) If p = 2, then p = −i(1 + i)2 where (1 + i) is prime in Z[i].

For any prime π ∈ Z[i] such that N π ̸= 2, we know that the residue classes of
1, −1, i, −i are distinct modulo π, so as before there exists a unique j modulo 4
such that α(N π−1)/4 ≡ i
j (mod π).

Deﬁnition 5.2. Let π ∈ Z[i] be an irreducible element such that N π ̸= 2. The
biquadratic (or quartic) residue character of α over π is given by
(1) (α
π)
4 = 0 if π|α.

(2) (α
π)
4 = i
j, where α N π−1
4 ≡ i
j (mod π) for a unique j modulo 4, when π ∤ α.

The biquadratic residue character satisﬁes the same properties as listed in Propo-
sition 4.3, with the modiﬁcation in (1) that (α
π)
4 = 1 if and only if α is a perfect
fourth power in Z[i]. The proof proceeds in a similar manner.
We can extend Deﬁnition 5.2 so that the residue character is deﬁned for any pair
of relatively prime elements:

Deﬁnition 5.3. For a nonunit α ∈ Z[i] such that (1 + i) ∤ α, write α = ∏

i λi,
where λi is irreducible. Let β ∈ Z[i] be such that β is relatively prime to α. Deﬁne
(β
α
)
4 = ∏

i
 ( β
λi
)
4.

This symbol is well-deﬁned since (α
π)
4 = (α
λ)
4 if (π) = (λ).
Like in the cubic case, it is convenient to introduce the notion of ”primary.”
However, here primary elements in Z[i] need not be prime.

Deﬁnition 5.4. A nonunit α ∈ Z[i] is primary if α ≡ 1 (mod (1 + i)3).

RECIPROCITY LAWS 15

Proposition 5.5. A nonunit α ∈ Z[i] is primary iﬀ either a ≡ 1 (mod 4), b ≡ 0
(mod 4), or a ≡ 3 (mod 4).

Proof. See Section 9.7, Lemma 6 of Ireland and Rosen [3]. □

Proposition 5.6. For a nonunit α ∈ Z[i] such that (1+i) ∤ α, there exists a unique
unit u such that uα is primary.

Proof. See Section 9.7, Lemma 7 of Ireland and Rosen [3]. □

It can be shown that a primary element can be written as the product of primary
irreducibles. Observe that for the biquadratic case, it is no longer necessary for a
primary element to be prime in Z[i]; in fact biquadratic reciprocity will be stated
for two relatively prime elements rather than two primes.
We will ﬁrst prove a supplemental case that will be useful in the proof of bi-
quadratic reciprocity.

Proposition 5.7. Given n ∈ Z such that n ≡ 1 (mod 4), we have χn(i) =
(−1) n−1
4 .

Proof. If n = p ≡ 1 (mod 4) for p a positive prime, then p = ππ for an irreducible
π and (i
p
)

4 = ( i
π
)
4
( i
π
)
4 = (i p−1
4 )
2 = (−1) p−1
4 .

If n = −q for an odd prime q ≡ 3 (mod 4), then
( i
−q
)
4 = i q2 −1
4 = (i
q−1) q+1
4 = (−1) −q−1
4 .

An arbitrary n can be written as a product of primes of the form p and −q, so
it is enough to show that for n = st we have (n − 1)/4 ≡ (s − 1)/4 + (t − 1)/4
(mod 2), since the general case will follow by induction. This can be shown by
doing casework on whether s, t are congruent to 1 or 5 (mod 8). □

We will now state biquadratic reciprocity.

Theorem 5.8 (Biquadratic Reciprocity). Let λ, π be relatively prime primary el-
ements of Z[i]. Then (λ
π
)

4 = (π
λ
)
4(−1) N λ−1
4 · N π−1
4 .

For simplicity of notation, let χπ = ( ·
π)
4 for the remainder of the section. As in
the cubic case, let π ∈ Z[i] be a complex primary irreducible so that N π = p ≡ 1
(mod 4). Since Z[i]/πZ[i] ≃ Fp, we can consider χπ as a biquadratic character on
Fp. The structure of the proof will be similar to in cubic reciprocity: we will ﬁrst
ﬁnd the prime factorization of g(χπ)
4, then prove special cases of the theorem to
build up to the general case.

Proposition 5.9. For p ≡ 1 (mod 4) an odd prime, g(χπ)
4 = pJ(χp, χp)2. Also,
we have −χπ(−1)J(χπ, χπ) = π, so consequently g(χπ)4 = π3π.

Proof. See Section 9.9 of Ireland and Rosen [3]. □

We will begin the proof by considering special cases. When λ, π are rational
integers, the case is similar to in cubic reciprocity.

16 NANCY XU

Proposition 5.10. Let α, a ∈ Z be such that α ̸= 0, a is an odd nonunit, and α
and a are relatively prime. Then χa(α) = 1.

Proof. Without loss of generality, suppose a > 0 and write a = ΠpiΠqi, where
pi, qi are primes such that pi ≡ 1 (mod 4) and qi ≡ 3 (mod 4). It follows from
deﬁnition that for π, α ∈ Z[i] where π is irreducible with N π ̸= 2 and π ∤ α, we
have χπ(α) = χπ(α). Therefore, if pi = ππ for an irreducible element π, we have

χα(pi) = χα(π)χα(π) = χα(π)χα(π) = 1.

On the other hand, since N qi = q2
i ,

χa(qi) ≡ a
 q2
i −1
4 ≡ (a
qi−1)
 qi+1
4 ≡ 1 (mod q)i.

From multiplicativity it follows that χa(α) = 1. □

From the preceding proposition, if λ = a, π = α for relatively prime nonunits
a, α ∈ Z, we have trivially that χα(a) = χa(α) = 1. This settles the case of when
λ, π are relatively prime rational integers.
We will now consider the case of when one element is complex and the other a
rational integer, starting with when λ, π are irreducibles.

Proposition 5.11. For an odd prime q ∈ Z, χπ((−1) q−1
2 q) = χq(π).

Proof. First, notice that what we have is indeed a special case of biquadratic reci-
procity since (−1) q−1
2 q is primary for any odd prime q ∈ Z. We can consider sepa-
rately when q ≡ 1 or 3 (mod 4), but in both cases the strategy is to write g(χπ)
q+1

(resp. g(χπ)q+3) in two diﬀerent ways, one by using the deﬁnition of Gauss sums
to simplify g(χπ)q, and the other by raising g(χπ)4 = π3π to the (q + 1)/4th (resp.
(q +3)/4th) power. Details can be found in Section 9.9 of Ireland and Rosen [3]. □

The previous result can be generalized as follows:

Proposition 5.12. Let a ∈ Z be such that a ≡ 1 (mod 4) and let λ ∈ Z[i] be
primary, where λ is relatively prime to a. Then χa(λ) = χλ(a).

Proof. By assumption a is primary, so we can write it as a product of primary primes
p1, . . . , pn and q1, . . . , qm, where pi ≡ 1 (mod 4) and qj ≡ 3 (mod 4), for 1 ≤ i ≤ n
and 1 ≤ j ≤ m. Since a ≡ 1 (mod 4), it follows that a = p1 . . . pn(−q1) . . . (−qm).
Applying Proposition 5.11 gives us

χa(λ) = ∏

i χpi(λ) ∏

j χqj (λ) = χλ(pi)χλ(−qj) = χλ(a).
 □

For the next case, suppose that π = a + bi and λ = c + di are primary and
relatively prime.

Proposition 5.13. If (a, b) = 1, (c, d) = 1, then χπ(λ) = χλ(π)(−1) a−1
2 · c−1
2 .

Proof. From the hypothesis, we have (a, π) = (b, π) = (c, λ) = (d, λ). From ci ≡ d
(mod λ), multiplying both sides by b and simplifying gives us cπ ≡ ac+bd (mod λ),
so (ac + bd, λ) = (ac + bd, π) = 1 and

χλ(c)χλ(π) = χλ(ac + bd). (1)

RECIPROCITY LAWS 17

Similarly, aλ ≡ ac + bd (mod π), so

χπ(a)χπ(λ) = χπ(ac + bd). (2)

Multiplying the conjugate of (2) by (1) gives us:

χλ(c)χπ(a)χλ(π)χπ(λ) = χλπ(ac + bd),

or
 χλ(π)χπ(λ) = χλ(c)χπ(a)χλπ(ac + bd).

Suppose ﬁrst that c, a, and ac + bd are nonunits. For each odd integer n, let
ϵ(n) = (−1) n−1
2 . Then ϵ(n)n ≡ 1 (mod 4) is primary, so working in terms of ϵ(n)n
and using Proposition 5.12 gives us:

χλ(π)χπ(λ) = χc(λ)χa(π)χac+bd(λπ).

From Proposition 5.10, it follows that

χc(λ) = χc(c − di) = χc(−di) = χc(i)

χa(π) = χa(a + bi) = χa(bi) = χa(i)

χac+bd(πλ) = χac+bd((ad − bc)i) = χac+bd(i).

Thus
 χλ(π)χπ(λ) = χ(ac+bd)ac(i)

= (−1)
 (ac+bd)ac−1
4

= (−1) a−1
2 · c−1
2 .

We get the ﬁrst equality from Proposition 5.7, and the second can be shown using
Proposition 5.5 and casework.
When a, c, or ac + bd equals ±1, we have χπ(±1) = χ±1(π) = 1, and a similar
strategy as the one illustrated will suﬃce. □

Most of the work has already been done, and to prove the general case of bi-
quadratic reciprocity, all that is left is to put together the special cases.

Proof. Write π = m(a + bi) and λ = n(c + di), where (a, b) = (c, d) = 1 and
m ≡ n ≡ 1 (mod 4), so a + bi and c + di are primary. It follows from Proposition
5.11 that χπ(n) = χn(π) and χλ(m) = χm(λ), and from Proposition 5.10 that
χm(n) = χn(m) = 1. Thus

χλ(π) = χλ(m)χλ(a + bi)

= χm(λ)χn(a + bi)χc+di(a + bi)

= χm(λ)χa+bi(n)χa+bi(c + di)(−1) a−1
2 · c−1
2

= χπ(λ)(−1) a−1
2 · c−1
2

= χπ(λ)(−1) N π−1
4 · N λ−1
4 ,

where the last equality follows from m ≡ n ≡ 1 (mod 4). □

18 NANCY XU

6. Eisenstein Reciprocity

Eisenstein’s reciprocity generalizes some of the previous reciprocity laws for
perfect odd powers. We will work in the ring of integers of the cyclotomic ﬁeld
K = Q[ζm], denoted OK. To take advantage of unique prime factorization, we will
consider prime ideals rather than prime elements in K, so it is necessary for us to
extend the notion of a norm to ideals.

Deﬁnition 6.1. For an ideal A ⊂ OK, we deﬁne the norm of A, N (A), to be the
number of elements in OK/A.

The norm is well-deﬁned since OK/A is always ﬁnite, and it can be checked
that the norm is multiplicative (see Section 14.1, Proposition 14.1.1 of Ireland and
Rosen [3] for details).

Proposition 6.2. Let K/Q be a Galois extension with G its Galois group. Then
∏

σ∈G σ(A) = (N (A)).

Proof. See Section 14.1, Propositon 14.1.2 of Ireland and Rosen [3]. □

Let P ⊂ OK be a prime ideal not containing m, and let q = N (P ) = |OK/P |.
For simplicity, for any w ∈ OK, we will denote as w its coset in OK/P .
We know xm − 1 = ∑m−1
i=0 (x − ζ i
m), so dividing both sides by x − 1 gives us

1 + x + . . . + xm−1 =
 m−1∏

i=1 (x − ζ i
m).

Let x = 1. Then m = ∏m−1
i=1 (1 − ζ i
m), so reducing modulo OK/P gives us m =
∏m−1
i=1 (1 − ζ i
m). We know m ̸= 0, so it follows that ζ i
m ̸= 1 for 1 ≤ i ≤ m − 1.

Therefore ζ i
m = ζ j
m if and only if i = j for 0 ≤ i, j ≤ m − 1, so the cosets of
1, ζm, . . . , ζ m−1
m are distinct in OK/P . From the analog of Fermat’s Little Theorem,
we have αq−1 ≡ 1 (mod P ) for α ∈ OK, α /∈ P , so

m−1∑

i=0 (α q−1
m − ζ i
m) ≡ 0 (mod P ).

Since P is prime it follows that there exists a unique i modulo m such that α q−1
m ≡
ζ i
m (mod P ).

Deﬁnition 6.3. For α ∈ OK and P a prime ideal such that m /∈ P , deﬁne the mth
power residue symbol, (α
P )
m, as:

(1) (α
P )
m = 0 if α ∈ P .

(2) (α
P )
m = ζ i
m, where i is the unique integer modulo m such that α N P −1
m ≡ ζ i
m
(mod P ), if α /∈ P .

The power residue symbol generalizes the quadratic, cubic, and quartic residue
characters and satisﬁes the same properties, speciﬁcally those listed in Proposition
4.3 with the modiﬁcation in (1) that (α
P )
m = 1 if and only if x
m ≡ α (mod P ) is
solvable in OK.
As in the quartic case, we can extend this deﬁnition to an arbitrary ideal:

RECIPROCITY LAWS 19

Deﬁnition 6.4. Let A ⊂ OK be an ideal prime to m with prime decomposition
A = P1P2 . . . Pn. For α ∈ OK, deﬁne (α
A
)
m = ∏n
i=1 ( α
Pi)
m. If β ∈ OK is relatively
prime to m, deﬁne (α
β)
m = ( α
(β))
m.

The purpose of this deﬁnition is so that we can express the power residue symbol
in terms of two elements in OK rather than an element and an ideal. Eisenstein’s
Reciprocity law will also be stated using this reﬁned deﬁnition.

Proposition 6.5. Let A, B ⊂ OK be ideals relatively prime to m. Then

(1) (αβ
A )
m = (α
A)
m(β
A)
m.
(2) ( α
AB)
m = (α
A
)
m(α
B)
m.
(3) If α is relatively prime to A and xm ≡ α (mod A) is solvable in OK, then(α
A
)
m = 1.

Proof. All three properties follow from deﬁnition. □

The multiplicativity properties will be particularly useful, since it would mean
that for statements concerning general ideals, we only need to prove them for prime
ideals, and the general case will follow. One point to note is that the converse of
(3) is not necessarily true; to determine whether α is an mth power modulo A, it
is necessary to decompose A into prime ideals.
As before, an integral part of the proof of the reciprocity law involves decom-
posing a Gauss sum into primes, and our case the primes lying over the Gauss sum
will be transitive and hence can be described in terms of a single prime and auto-
morphisms in G = G(Q(ζm)/Q). It is therefore necessary for us to consider how
these automorphisms will behave with respect to (α
A)
m. For σ ∈ G and α ∈ Q(ζm),
it will be convenient for us to use the exponential notation and write ασ instead of
σ(α), which we will do for the rest of the paper.

Proposition 6.6. Let A ⊂ OK be an ideal prime to m, and let σ ∈ G. Then
(α
A
)

m = (ασ

Aσ
)
m.

Proof. It is enough for us to prove the proposition for the prime ideal A = P , as
the general case will follow from multiplicativity. By deﬁnition

α N P −1
m ≡ (α
P
 )
m (mod P ),

so applying σ gives us
 (ασ) N P −1
m ≡ (α
P
 )σ

m (mod P σ).

Since P is prime to m, it follows that P σ is also prime to m. We also know
N P = N P σ, so (ασ
P σ)
m = (α
P )σ
m. □

Similar to the cubic and biquadratic cases, we will state reciprocity in terms of
primary elements:

Deﬁnition 6.7. Let m = l be an odd prime. A nonzero element α ∈ OK is primary
if it is not a unit, is relatively prime to l, and is congruent to an integer modulo
(1 − ζl)2.

20 NANCY XU

Proposition 6.8. Let α ∈ OK, where α is relatively prime to l. Then there exists
an integer c unique modulo l such that ζ c
l α is primary.

Proof. Let λ = 1 − ζl. It can be shown that λl−1 = l (see Section 13.2, Proposition
13.2.7 of Ireland and Rosen [3]), thus from Proposition 2.14 it follows that (λ) is a
prime ideal of inertial degree 1, so there exists an a ∈ Z such that α ≡ a (mod λ).
Then (α − a)/λ ∈ OK, so there exists a b ∈ Z such that (α − a)/λ ≡ b (mod λ
2),
thus α ≡ a + bλ (mod λ2). Since ζl = 1 − λ, we have ζ c
l ≡ 1 − cλ (mod λ2) and
thus ζ c
l α ≡ a + (b − ac)λ (mod λ2). By assumption l ∤ α, so l ∤ a. Then we can
choose a unique c modulo l such that ac ≡ b (mod l), so ζ c
l α ≡ a (mod λ2) and
thus ζ c
l α is primary. □

This deﬁnition of primary is slightly weaker than the ones in the cubic and
biquadratic case, since we only have uniqueness up to multiplication by roots of
unity, but for our purposes this will suﬃce.
We can now state the reciprocity law.

Theorem 6.9 (Eisenstein Reciprocity). Let l, a ∈ Z be such that l is an odd prime
and (l, a) = 1, and let α ∈ OK be a primary element such that a and α are relatively
prime. Then (α
a
)
l = (a
α
)

l.

The remainder of this section will be dedicated to a proof of this theorem. Some
results we present below will hold in Z[ζm] for an arbitrary m while others hold
only if m = l, where l is an odd prime, and we will use m or l accordingly.
We begin with a discussion of the Stickelberger relation, a result which provides
a prime decomposition for certain powers of Gauss sums. We have seen the utility
of analogous statements in the cubic and biquadratic cases in Corollary 4.9 and
Proposition 5.9.
Let F be a ﬁnite ﬁeld with q = pf elements, χ a multiplicative character of order
m, and ψ a nontrivial additive character. Then χ is an mth root of unity while ψ is
a pth root of unity since p is the characteristic of F , so g(χ, ψ) = ∑

t∈F χ(t)ψ(t) ⊂
Q[ζm, ζp]. It will be convenient for us to specify χ and ψ.
Let P ⊂ OK be a prime ideal such that m /∈ P , and with this deﬁne χP (t) =
( t
P )−1
m . Let p ∈ Z be the unique prime under P , so that N P = q = p
f , where
f is the order of p modulo m by Proposition 2.22. Let F = OK/P . Now let
ψ(t) = ζ tr(t)
p , where tr : F −→ Fp is deﬁned as tr(t) = t + tp + . . . + tpf −1. Deﬁne
g(P ) = g(χP , ψ) and Φ(P ) = g(P )m.
We will formulate the Stickelberger relation using “symbolic powers.” For a Ga-
lois extension K over Q with Galois group G = G(K/Q), deﬁne Z[G] to be the set
of formal expressions ∑

σ∈G a(σ)σ with coeﬃcients a(σ) ∈ Z. For an ideal A ⊂ K,
deﬁne A∑ a(σ)σ ∏

σ (Aσ)a(σ).

For the remainder of the paper, let σt be the automorphism deﬁned as σt(x) = xt,
where x ∈ Q[ζm]/Q and t is a ﬁxed integer such that (t, m) = 1.

Theorem 6.10 (The Stickelberger Relation). Let P ⊂ OK be a prime ideal not
containing m. Then (Φ(P )) = P ∑ tσ−1
t ,

RECIPROCITY LAWS 21

where the sum is over all 1 ≤ t < m such that (t, m) = 1.

Proof. See Section 14.4, Theorem 2 of Ireland and Rosen [3]. □

As an example, when m = 3, we proved using Jacobi sums in Corollary 4.9 that
g(P )
3 = Φ(P ) = ππ2. If σ ∈ G(Q[ζ3]/Q) is the nontrivial automorphism, then
Φ(P ) = π1+2σ since σ = σ−1. The prime factorization of g(P )
3 played a vital role
in the proof of cubic reciprocity, and the generalized result will be equally important
here. For simplicity, let γ = ∑ tσ−1
t for 1 ≤ t < m and (t, m) = 1.
Since we will work with ideals that are not prime, it is necessary to extend the
deﬁnition of Φ.

Deﬁnition 6.11. Let A ⊂ OK be an ideal prime to m with prime decomposition
A = P1 . . . Pn. Deﬁne Φ(A) = Φ(P1)Φ(P2) . . . Φ(Pn).

It is clear by deﬁnition that Φ is multiplicative. For simplicity we will write
Φ((α)) as Φ(α).
For the ﬁrst step of the proof, we will take a similar approach as in cubic and
biquadratic reciprocity by computing a power of g(P ) in two diﬀerent ways.

Proposition 6.12. Let P, P ′ ⊂ OK be prime ideals relatively prime to m such that
N P and N P ′ are relatively prime. Then
(
Φ(P )
P ′
 )
m = (N P ′

P
 )
m.

Proof. Let q′ = p
′f ′ = N P ′. By Proposition 2.22, it follows that q′ ≡ 1 (mod m).
We will compute g(P )q′−1 in two ways. First,

g(P )q′ ≡ ∑

t∈Fq′ χP (t)q′ψ(t)q′ (mod p′)

≡ ∑

t∈Fq′ χP (t)ψ(q′t) (mod p
′)

≡ (q′

P
 )
mg(P ) (mod p′).

Next,
 g(P ′)q′−1 = Φ(P ) q′ −1
m ≡ (
Φ(P )
P ′
 ) (mod P ′),

so it follows that (Φ(P )
P ′ )
m = (N P ′
P )
m. □

Corollary 6.13. Let A, P ∈ OK be such that A = (α) is principal and relatively
prime to m, P is a prime ideal, and N A and N P are relatively prime. Then
(ϵ(α)
P
 )
m
( α
N P
 )
m = (
N P
α
 )
m.

Proof. From Stickelberger’s relation and using multiplicativity, it follows that (Φ(α)) =
(α)
γ = (αγ), and thus (
Φ(α)
P
 )
m = (ϵ(α)
P
 )
m
(
αγ

P
 )
m,

22 NANCY XU

where ϵ(α) is a unit in OK. We have
(αtσ−1
t

P
 )

m = (
ασ−1
t

P
 )t

m = (
ασ−1
t

P
 )σt

m = ( α
P σt
)
m,

so (αγ

P
 )
m = ∏

t
 (αtσ−1
t

P
 )
m = ∏

t
 ( α
P σt
)

m = ( α
N P
 )

m,

where the product is over 1 ≤ t < m for (t, m) = 1. Decomposing (α) into primes
and use multiplicativity gives us (N P
α )
m = (Φ(α)
P )
m by Proposition 6.12, and the
result follows. □

Notice that for m = l an odd prime, we would be done if (ϵ(α)
P )
l = 1 for α
primary, and the argument proceeds as follows: Let p ∈ Z be a prime such that
(p, l) = 1 and p is relatively prime to α in OK. Let P ⊂ OK be a prime ideal
containing p. Then N P = p
f and
(α
p
)

l = (p
α
)f

l .

From Proposition 2.22 it follows that f |(l − 1), thus (f, l) = 1 and so (α
p)
l = (p
α
)
l.
By multiplicativity, for any a ∈ Z relatively prime to l and α, we have (α
a)
l = (a
α
)
l.

To show (ϵ(α)
P )
l = 1, we will begin by determining ϵ(α). We ﬁrst need two results
concerning roots of unity and another concerning automorphisms:

Lemma 6.14. The only roots of unity in Q[ζm] are ±ζ i
m for 1 ≤ i < m.

Lemma 6.15. Let K/Q be a number ﬁeld, and let σ1, σ2, . . . , σn be the n = [K : Q]
be the isomorphisms of K into Q. If α ∈ K satisﬁes |ασi| ≤ 1 for 1 ≤ i ≤ n, then
α is a root of unity.

The proofs to both lemmas can be found in Section 14.5 of Ireland and Rosen
[3].

Lemma 6.16. Let A ⊂ OK be an ideal relatively prime to m, and let σ be an
automorphism of Q[ζm]/Q. Then Φ(A)σ = Φ(Aσ).

Proof. It is enough to prove the result for A = P a prime ideal, as the general case
follows from multiplicativity.
Let σ be an automorphism of Q[ζm, ζp]/Q that restricts to σ on Q[ζm] and the
identity on Q[ζp]. It follows from Proposition 6.6 that

g(P )σ = ∑

t∈FN P
 (ασ

P σ
)−1

m ζ tr(α)
p ,

since tr(ασ) = tr(α) as tr(α) ∈ Fp. Thus g(P )σ = g(P σ), and raising both sides to
the mth power gives our result. □

Proposition 6.17. Let α ∈ OK, where α is relatively prime to m. Then Φ(α) =
ϵ(α)αγ, where ϵ(α) = ±ζ i
m for some i.

Proof. We ﬁrst need three results:
(1) |Φ(α)|
2 = (N (α))
m.
(2) |αγ|
2 = |N α|m.
 RECIPROCITY LAWS 23

(3) N (α) = |N α|.

For (1), it is enough to show the identity for a prime ideal P by multiplicativity.
An argument similar to the proof of Proposition 3.4 shows that |g(P )|2 = q, so
|Φ(P )|
2 = |g(P )|2m = (N P )
m and the result follows.
For (2), we have
 |αγ|
2 = αγαγσ−1 = αγ(1+σ−1)

since σ−1 acts as complex conjugation on Q[ζm]. We know σ−1γ = σ−1 ∑ tσ−1
t =∑ tσ−1
−t , and we can rewrite γ as γ = ∑
(m − t)σ−1
−t , so

(1 + σ−1)γ = ∑ tσ−1
t + σ−1 ∑ tσ−1
t = m ∑ σ−1
t ,

and the result follows since N α = α∑ σ−1
t . To show (3), it follows from Proposition
6.2 that for a principal ideal (α)

(N ((α))) = Πσ((α)) = Π(ασ) = (Π(ασ)) = (N (α)).

From Proposition 6.2 and Deﬁnition 2.4, it follows that N ((α)) and N (α) are ﬁxed
under automorphisms of Q[ζm] over Q, so N ((α)), N (α) ∈ Q and thus N (α) =
|N (α)|.
Putting together (1), (2), and (3) gives us that |ϵ(α)| = 1. A similar argument
will show that |ϵ(ασ)| = 1 for any σ ∈ G(Q[ζm]/Q), and it follows from Lemma
6.16 that |ϵ(α)
σ| = 1. Thus by Lemma 6.15 ϵ(α) must be a root of unity, and by
Lemma 6.14, we have ϵ(α) = ±ζ i
m. □

Lemma 6.18. If A ⊂ OK is an ideal prime to l then Φ(A) ≡ ±1 (mod l).

Proof. It is enough to show that Φ(P ) ≡ −1 (mod l) for a prime ideal P ⊂ OK
relatively prime to l. Let q = pf = N P , where p is an odd prime. We have:

Φ(P ) = g(P )
l ≡ ∑

t∈Fq χP (t)
lψ(t)
l (mod l)

≡ ∑

t∈Fq,t̸=0 ψ(lt) ≡ −1 (mod l).
 □

The next proposition is where the assumption that α is primary becomes impor-
tant.

Proposition 6.19. If α ∈ OK is primary, then ϵ(α) = ±1.

Proof. It follows from Lemma 6.18 that (α)
γ ≡ ±1 (mod l). Since α is primary,
we have α ≡ x (mod (1 − ζl)2) and

αγ ≡ xγ ≡ x1+2+...+(l−1) (mod (1 − ζl)
2).

Since x l−1
2 ≡ ±1 (mod l), we get

αγ ≡ (±1)l ≡ ±1 (mod (1 − ζl)
2),

so ϵ(α) ≡ ±1 (mod (1 − ζl)2). By Proposition 6.17, we know ϵ(α) = ±ζ i
l . By the
uniqueness criterion in Proposition 6.8, it follows that ϵ(α) = ±1. □

24 NANCY XU

Thus if α is primary, we have
(ϵ(α)
B
 )

l = (
±1
B
 )
l = (±1
B
 )l

l

since l is odd, thus (ϵ(α)
B )
l = 1, which completes the proof.
The discussion of reciprocity laws does not end here. In fact, much of the results
presented in this paper are consequences of Artin’s reciprocity law, a central result
in class ﬁeld theory that, in simplistic terms, shows that the power residue symbol(α
P )
m only depends on the residue class of α modulo some multiple of P . An
introduction to this topic is presented in Cox [2].

Acknowledgments

I would like to thank my mentors Eric Chen and Wei Yao for their general
guidance, patience and thoughtfulness in answering my questions, recommendations
of resources, and feedback for this paper. I would also like to thank Peter May for
his eﬀorts in organizing this REU program.

References

[1] Michael Artin, Algebra, Pearson, Second edition, 2010.
[2] David A. Cox, Primes of the form x2 + ny2: Fermat, Class Field Theory, and Complex
Multiplication, John Wiley & Sons, Inc., 1989.
[3] Kenneth Ireland and Michael Rosen. A Classical Introduction to Modern Number Theory.
Springer-Verlag, Inc., New York, NY, Second edition, 1990.
[4] Franz Lemmermeyer. Reciprocity Laws: From Euler to Eisenstein. Springer-Verlag, Inc.,
Berlin, 2000.
[5] Daniel A. Marcus. Number Fields. Springer International Publishing AG, New York, NY,
Second edition, 2018.
