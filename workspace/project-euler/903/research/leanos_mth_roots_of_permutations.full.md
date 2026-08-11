<!-- source: https://arxiv.org/pdf/1005.1531 | converted from PDF -->

arXiv:1005.1531v4  [math.CO]  12 Sep 2011On the number of mth roots of
permutations

Jes´us Lea˜nos, Rutilo Moreno and Luis M. Rivera-Mart´ınez

Abstract

Let m be a ﬁxed positive integer. It is well-known that a permutation σ of

{1, ..., n} may have one, many, or no mth roots. In this article we provide an

explicit expression and a generating function for the number of mth roots of σ. Let

pm(n) be the probability that a random n-permutation has an mth root. We also

include a proof of the fact that pm(jq) = pm(jq + 1) = · · · = pm(jq + (q − 1)),

j = 0, 1, ..., when m is a power of prime number q.

1 Introduction and main results

Let Sn be the group of all permutations of the ﬁnite set [n] = {1, ..., n}. Let m be a ﬁxed

positive integer. We say that σ ∈ Sn has an mth root or that σ is an mth power if there
exists a permutation τ ∈ Sn with τ m = σ. For ﬁxed m, not all permutations have an

mth root ([15], Theorem 4.8.2), however, L. Glebsky and L. M. Rivera [7] have proved
that for suﬃciently large n, any permutation has an “almost” mth root (in the sense
of the Hamming distance [6]). Now, if we know that a permutation σ has at least one

mth root, how many mth roots can σ have? We can ﬁnd an explicit expression for this
quantity in the paper of A. I. Pavlov [10]. Also, in the article of S. Annin, T. Jansen and

C. Smith [1], appeared a classiﬁcation of the elements in Sn and An that has mth roots,
and they propose some problems related with the roots of permutations. In particular,
our work is about some questions on Problem 1 in Section 4 of [1].

2000 Mathematics Subject Classiﬁcation: 05A05, 05A15.
Key words and phrases: Permutations, mth roots, Enumeration.
Rivera-Mart´ınez was partially supported by PROMEP (SEP), grant UAZ-PTC-103.

1

The main results of this paper are an explicit expression for the number of mth roots
of any n-permutation σ (Theorem 1) and a generating function for this number (Theo-

rem 2). In order to obtain our expression we deﬁne some sets of non-negative integers
that seem interesting by themselves (see Section 2). In particular, such sets provide a
simpler expression than the corresponding expression in [10]. Moreover, this new expres-

sion allows us to compute the number of mth roots of a permutation in an eﬀective way
using a computer algebra system.

Another classical problem consists in estimating the number of permutations in Sn
that admit an mth root. P. Tur´an [14] gave an upper bound when m is a prime number
and Blum [2] gave an asymptotic formula for the case m = 2. Recently, M. B´ona, A.

McLennan and D. White [4] proved that the probability that a random permutation of
length n has an mth root with m prime, is monotonically non-increasing in n. See also

the work of N. Pouyanne [12] for an asymptotic study for any positive integer m and the
work of B. Bollob´as and B. Pittel [3] who continued the work of N. Pouyanne and studied
the limiting distribution of the root degree of a permutation. This problem can be easily

reformulated as the problem about the probability, pm(n), that a n-permutation chosen
uniformly at random has an mth root. For this problem, we give a proof of the fact that
when m is a power of a prime q, for all j ≥ 0, pm(jq) = pm(jq +1) = · · · = pm(jq +(q −1)).

For the case m a prime, see the paper of M. B´ona, et al. [4] that includes a combinatorial
proof of the equivalent equalities. It is also recommended the paper of A. Mar´oti [9] and

the bibliography therein for related results about the proportion of ℓ-regular elements in
the symmetric group Sn. Another interesting article is due to M. R. Pournaki [11], who
worked in the problem of determining the number of even permutations with roots.

Before stating our main results, we shall give some notation and deﬁnitions. As usual,
we denote by N (respectively N0) the set of positive (respectively, non-negative) integers.

The cycle type of an n-permutation is a vector a = (a1, a2, ..., an) that indicates that the
permutation has ai cycles of length i for every i ∈ [n]. It is an easy exercise to prove that
conjugated permutations have the same number of mth roots. Let m, ℓ ∈ N and a ∈ N0.

We deﬁne the following sets

Gm(ℓ, a) := {g ∈ N : g ≤ a; gcd (gℓ, m) = g},

2

and
 Gm(ℓ) := {g ∈ N : gcd (gℓ, m) = g}.

Clearly Gm(ℓ, a) ⊆ Gm(ℓ), and both are ﬁnite sets. Note that if a = 0, then Gm(ℓ, a) = ∅.
We will name (g1, ..., gk) the associate vector of Gm(ℓ, a) if Gm(ℓ, a) = {g1, · · · , gk} and

g1 < g2 < · · · < gk. For every set Gm(ℓ, a) of cardinality k ≥ 1 we deﬁne the set of vectors

Em(ℓ, a) := {ε ∈ Nk
0 : g · ε = a, with g the associate vector of Gm(ℓ, a)}.

Note that if equation g1x1 + · · · + gkxk = a does not have non-negative integer solutions
then Em(ℓ, a) = ∅. We use the convention that ∑

i∈I si = 0 if I is empty.

Next, we present our main results about the number of mth roots of permutations.

Theorem 1. Let m be a ﬁxed positive integer. Let σ be any n-permutation of type a, i.e.
for every ℓ ∈ [n], σ has aℓ cycles of length ℓ. Let r(m)(a) be the number of mth roots of

σ, then
 r(m)(a) = ∏

ℓ≥1
aℓ̸=0
 aℓ!
 

 ∑

ε ∈Em(ℓ,aℓ)
 k∏

i=1
 ℓ(gi−1)εi

giεiεi!
 

 ,

where k = |Gm(ℓ, aℓ)|, and g = (g1, ..., gk) is the associate vector of Gm(ℓ, aℓ).

Our next theorem provides a generating function for the number of mth roots of
permutations.

Theorem 2. Let m, n be positive integers, and a1, ..., an be non-negative integers. For
n = a1 + 2a2 + · · · + nan, the coeﬃcient of t
a1
1 ···t
an
n
a1!···an! in the expansion of

exp ( ∑

ℓ≥1
 ∑

g∈Gm(ℓ)
 ℓg−1

g t
g
ℓ )
,

is the number of mth roots of an n-permutation of cycle type a = (a1, ..., an).

Note that Theorems 1 and 2 allow us to compute the number of mth roots of a
permutation in an eﬀective way using a computer algebra system.

3

The outline of the paper is as follows. In Section 2 we present some preliminaries
results about the sets Gm(ℓ, a) and Gm(ℓ). In Section 3 we recall how to extract roots

of permutations. In Section 4 we give the proofs of Theorem 1 and Theorem 2. Finally,
in Section 5 we present a proof of the fact that probability pm(n) satisﬁes pm(jq) =
pm(jq + 1) = · · · = pm(jq + (q − 1)), where j = 1, ... and m is a power of a prime number

q.

2 Preliminaries

The next notation is standard, and it can be found in several books, for example, in the
book of V. Schoup ([13], Section 1.3). For integer n and prime p we will write νp(n) for
the highest power of p that divides n. In this notation the deﬁnition of gcd(a, b) is

gcd(a, b) = ∏

p ∈P pmin(νp(a),νp(b)),

where P is the set of all primes. We use the convention that gcd(g) = g for every g ∈ N.
If a and b are positive integers then

νp(gcd(a, b)) = min(νp(a), νp(b)),

and
 νp(a · b) = νp(a) + νp(b).

Note that a divides b if and only if νp(a) ≤ νp(b) for all primes p. The following deﬁnition
can be found in the book of H. Wilf ([15], page 148). For a pair ℓ, m in N, the number

((ℓ, m)) is deﬁned as ((ℓ, m)) = ∏

p | ℓ
p ∈P
 pνp(m).

The number ((ℓ, m)) is very important in the characterization of the permutations that

admit mth roots (Theorem 3, Section 3). As the sets Gm(ℓ, a), and Gm(ℓ) play an im-
portant role in our expressions, we ﬁrst prove some interesting propositions about the
elements in these sets. Some of these propositions show the relation between the elements

of Gm(ℓ, a) and Gm(ℓ) with the number ((ℓ, m)).

Proposition 1. If a ≥ 1 then 1 ∈ Gm(ℓ, a) if and only if gcd(ℓ, m) = 1.

4

Proof. Because 1 = gcd(ℓ, m) = gcd(1 · ℓ, m), we have 1 ∈ Gm(ℓ, a). The converse follows
from the deﬁnition of Gm(ℓ, a).

Proposition 2. Let g, ℓ and m be positive integers. Then g ∈ Gm(ℓ) if and only if
conditions 1 and 2 hold

1. Any prime divisor p of g divides m and satisﬁes one of the following:

(a) If p divides ℓ, then νp(g) = νp(m),

(b) If p does not divide ℓ, then νp(g) ≤ νp(m).

2. If p is a prime that does not divide g, then p does not divide gcd(ℓ, m).

Proof. For the if part: As any prime divisor p of g satisﬁes (1) νp(g) ≤ νp(m), and therefore
g | m and g | gcd(gℓ, m). Now we prove that gcd(gℓ, m) | g. Let p be any prime divisor

of gcd(gℓ, m), then p | gℓ and p | m. If p ∤ g then p | ℓ and p | gcd(ℓ, m), which implies a
contradiction of condition (2), so p | g. If p divides ℓ then by (1a), νp(g) = νp(m). Thus

νp(gcd(gℓ, m)) = min(νp(gℓ), νp(g)) = νp(g).

If p does not divide ℓ, νp(ℓ) = 0, and by property (1b) νp(g) ≤ νp(m). Then

νp(gcd(gℓ, m)) = min(νp(g) + νp(ℓ), νp(m)) = νp(g).

Therefore gcd(gℓ, m) | g, and g ∈ Gm(ℓ).

For the converse. Let p be any prime divisor of g ∈ Gm(ℓ). By deﬁnition g = gcd(gℓ, m)
and then p | m. We ﬁrst prove (1a). The hypothesis p | ℓ implies νp(ℓ) > 0, and
νp(g) = min(νp(g) + νp(ℓ), νp(m)) = νp(m). Now we prove (1b). As p ∤ ℓ, νp(ℓ) = 0

and νp(g) = min(νp(g) + νp(ℓ), νp(m)), and therefore νp(g) ≤ νp(m). Finally, we prove
(2), Suppose that there exists a prime p such that p ∤ g and p | gcd(ℓ, m). Then

p | gcd(gℓ, m) = g, which is clearly a contradiction.

Remark 1. There is another way to build the set Gm(ℓ): choose any divisor d ≥ 1 of

m, with d relatively prime to ℓ, and deﬁne g := m/d. Thus, we have that gcd(ℓg, m) =
gcd(ℓg, gd) = g, as it is required. Then, the set Gm(ℓ) can be deﬁned as the set {g =
m/d : d ∈ N, d | m and gcd(d, ℓ) = 1}. It is an easy exercise to show that both sets are

the same. To build the set Gm(ℓ, a) follow the same procedure only with the condition
that g = m/d ≤ a.
 5

The following proposition shows that ((ℓ, m)) is an element of Gm(ℓ)

Proposition 3. Let ℓ, m, a be positive integers. Then

1. ((ℓ, m)) belongs to Gm(ℓ),

2. if ((ℓ, m)) divides a, then ((ℓ, m)) ∈ Gm(ℓ, a).

Proof. First we show 1. The case gcd(ℓ, m) = 1 follows from Proposition 1. If gcd(ℓ, m) >

1, for any prime divisor p of ((ℓ, m)), we have that p divides gcd(ℓ, m) and p divides ℓ
and m. By deﬁnition of ((ℓ, m)), νp(((ℓ, m))) = νp(m), and condition (1) in Proposition 2

holds. Let q be a prime that does not divide ((ℓ, m)), if q ∤ ℓ clearly q ∤ gcd(ℓ, m) and if
q | ℓ, use the hypothesis that q ∤ ((ℓ, m)) and the deﬁnition of ((ℓ, m)) to obtain νq(m) = 0.
Therefore, condition (2) in Proposition 2 also holds, and ((ℓ, m)) ∈ Gm(ℓ). Now we show

the second part. As a consequence of the ﬁrst part of this proposition, ((ℓ, m)) ∈ Gm(ℓ).
As ((ℓ, m)) divides a, ((ℓ, m)) ≤ a, and therefore ((ℓ, m)) ∈ Gm(ℓ, a).

Remark 2. Note that if k = gcd(kℓ, m) then gcd(ℓ, m) divides k.

Proposition 4. Let ℓ, m be positive integers. If Gm(ℓ) = {g1, ..., gh}, then gcd(g1, ..., gh) =

((ℓ, m)).

Proof. We begin with the case gcd(g1, ..., gh) = 1. As a consequence of Remark 2, if gi =
gcd(giℓ, m) then gcd(ℓ, m) divides gi for any i ∈ [h], and therefore we have gcd(ℓ, m) = 1

which implies that ((ℓ, m)) = 1. Now, for d := gcd(g1, ..., gh) > 1, from part (1) of
Proposition 3, ((ℓ, m)) ∈ Gm(ℓ), and therefore d divides ((ℓ, m)). Now we prove that

((ℓ, m)) divides d. As d > 1 and d | ((ℓ, m)) then ((ℓ, m)) > 1. Let p be any prime factor
of ((ℓ, m)). From the deﬁnition of ((ℓ, m)), p divides ℓ and m, thus p divides gcd(ℓ, m).
Let g be any element in Gm(ℓ). So g = gcd(gℓ, m). By Remark 1, we know that gcd(ℓ, m)

divides gcd(gℓ, m) and therefore p divides g. By Proposition 2 (1a), the exponent of
p in any g ∈ Gm(ℓ) is νp(m), then νp(d) = νp(m). On the other hand, by deﬁnition

νp(((ℓ, m))) = νp(m), and therefore νp(((ℓ, m))) = νp(d), so we conclude that ((ℓ, m))
divides d.

A consequence of this proposition is that ((ℓ, m)) is the least element of the set Gm(ℓ).
We also obtain the following corollary
 6

Corollary 1. Let a, ℓ, m be positive integers. Let Gm(ℓ, a) = {g1, ..., gj}. Then

gcd(g1, ..., gj) = ((ℓ, m)).

Proposition 5. Let m, ℓ, a be positive integers. Let Gm(ℓ, a) = {g1, ..., gh}. Then ((ℓ, m))
divides a if and only if
 g1x1 + g2x2 + · · · + ghxh = a, (1)

has non-negative integer solutions.

Proof. If h = 1, then Gm(ℓ, a) = {((ℓ, m))} by Proposition 4, and the result follows.
Now, we assume h > 1. The if part follows easily because ((ℓ, m)) = gcd(g1, ..., gh)

(Corollary 1). For the converse, by Proposition 3 part (2), ((ℓ, m)) ∈ {g1, ..., gh}. Now,
take gi = ((ℓ, m)), xi = a/((ℓ, m)) and xj = 0 for any j ̸= i.

We conclude this section with one proposition about the elements of Gm(ℓ) for the

case when ℓ and m are relatively prime.

Proposition 6. If gcd(ℓ, m) = 1, then Gm(ℓ) is equal to the set of positive divisors of m.

Proof. As gcd(ℓ, m) = 1 then gcd(gℓ, m) = gcd(g, m). Any g that satisﬁes the relation

g = gcd(gℓ, m) = gcd(g, m) is a positive divisor of m.

3 Roots of permutations

Let σ be an n-permutation and let m be a ﬁxed positive integer. A permutation τ ∈ Sn
that satisﬁes τ m = σ may or may not exist. If such τ exists, it is called an mth root of σ.
The following theorem is due to A. Knopfmacher and R. Warlimont [15, p. 148, Theorem
4.8.2], and it gives a characterization of the n-permutations that have mth roots.

Theorem 3. Let m be a positive integer. A permutation σ has an mth root if and only

if for every ℓ = 1, 2, ... the number of ℓ-cycles that σ has is divisible by ((ℓ, m)).

This theorem gives us information about the cycle structure of permutations that
admits mth roots. But, if we know that a permutation has mth roots, we need a procedure
to get all of its roots (see, for example [8, §3.3]). The ﬁrst important observation is that we

can build any mth root τ of σ if we work with cycles of σ with diﬀerent lengths separately.
Indeed, if τ is an mth root of σ, with τ = C1 · · · Cs its disjoint cycle factorization, then

7

σ = τ m = C m
1 · · · C m
s , where C m
i consists in gcd(|Ci|, m) cycles of length |Ci|/ gcd(|Ci|, m)
each. Let σℓ be the part of σ, that consists in the product of all cycles Di of length ℓ in

σ (aℓ ̸= 0, where aℓ is the number of cycles of length ℓ in σ). So, we can see permutation
σ as a product of parts σℓ, where every part σℓ consist in all the cycles of length ℓ in the
disjoint cycle factorization of σ. Let τℓ be the part of τ whose mth power produces the

part σℓ τ m
ℓ = σℓ = ∏

|Di|=ℓ Di.

and we can ﬁnd τℓ, and therefore τ , working with σℓ independently. This is for every length

ℓ ̸= 0 in cycles of σ. Now, we need to ﬁnd the admissible lengths, |Ci|, of cycles in τℓ.
We know that for any cycle Ci in τℓ, |Ci| = ℓ gcd(|Ci|, m), and we write g = gcd(|Ci|, m).

We need to ﬁnd g ≤ aℓ, in such a way that g = gcd(gℓ, m). Note that this number exists
because we are assuming that the permutation has mth roots, and by Theorem 3 and
Proposition 3 (part 2), ((ℓ, m)) ∈ Gm(ℓ, aℓ). Thus, any g cycles of σℓ, Di1, · · · , Dig, can

be combined in a suitable way (see, for example, proof of Theorem 3 in [1] or proof of
Theorem 4.8.2 in [15]) into one gℓ-cycle Ci for τℓ with C m
i = Di1 · · · Dig.

Now, to obtain all the mth roots of σ, we build the sets Gm(ℓ, aℓ) and Em(ℓ, aℓ), for
every ℓ with aℓ ̸= 0. Theorem 3 and Proposition 5 shows that Em(ℓ, aℓ) is not empty if
and only if ((ℓ, m)) divides aℓ. The elements of Em(ℓ, aℓ) represents the diﬀerent ways in

which we can group the cycles of σℓ. This is, for ε ∈ Em(ℓ, aℓ), the coordinates ε1, ε2, . . .
of ε and the coordinates g1, g2, ... of the associate vector g of Gm(ℓ, aℓ) means that τℓ has

ε1 cycles of length g1ℓ, ε2 cycles of length g2ℓ, etc.

4 Proof of Theorems 1 and 2

In this section, we present the proofs of two of our main results. Theorem 1 provides an

explicit expression for the number of mth roots of permutations of type a, and Theorem 2
provides a generating function for this number. We use the next notation: Let i, j be any

positive integers. For an n-permutation of Type (i)j we mean that this permutation has
j cycles of length i, and n = ij. First, we prove the following proposition.

Proposition 7. Let ℓ, m ∈ N be ﬁxed. Let g ∈ Gm(ℓ) and p ∈ N. Let σ be any permutation

8

of Type (ℓ)gp. Then the number of mth roots of σ, τ , of Type (gℓ)p is

(gp)!ℓp(g−1)

gpp! .

Proof. From the gp cycles, we need to build p cycles of length gℓ for τ . This we make
by grouping the cycles in p bundles of g cycles each (C1, C2, . . . , Cg), and then, we build

with each bundle, a cycle of length gℓ. In how many ways can we group the bundles?
As no matter the order of the bundles, this problem is reduced to count the number of
unordered partitions of a set of cardinality gp in p equal parts. This number is

(gp)!
(g!)pp! .

For each of the p bundles (C1, C2, . . . , Cg), we need to arrange the elements of cycles
C1, C2, . . . , Cg in a cycle D that satisﬁes Dm = C1 · · · Cg. We can use the procedure

in the proof of Theorem 4.8.2 [15, §4.8]), applying it to all the possible combinations
of cycles C1, C2, . . . , Cg and their elements in order to obtain all the possible diﬀerent
cycles D. With this procedure we obtain (g − 1)!ℓg−1 diﬀerent such cycles. As we have

p bundles, with g disjoint cycles each, we have ((g − 1)!ℓg−1)p diﬀerent bundles of cycles
(D1, D2, · · · , Dp) with which we can build the diﬀerent mth roots. Therefore the number

of mth roots of the required Type is

(gp)!
(g!)pp! ((g − 1)!ℓg−1)p = (gp)!ℓp(g−1)

gpp! .

4.1 Proof of Theorem 1

Let m be a positive integer, let σ be an n-permutation of type a, i.e. σ has aℓ cycles of
length ℓ for every ℓ ∈ [n]. As we see in Section 3, we can build τ from σ working separately

with each part σℓ, aℓ ̸= 0. For every ℓ-cycle in σ we build the sets Gm(ℓ, aℓ), and Em(ℓ, aℓ).
By Proposition 5, if σℓ has an mth root, then Em(ℓ, aℓ) will be a non-empty set. We will
count all the mth roots of σℓ. Take ε in Em(ℓ, aℓ), and for every i ∈ [h], h = |Gm(ℓ, aℓ)|,

we will build εi giℓ-cycles for τℓ. From the aℓ cycles of σℓ, choose h subsets of giεi cycles

9

each one, this can be made in aℓ!
∏h
i=1(giεi)!

ways. Now, from every one of the giεi cycles, we build εi cycles of length giℓ. By

proposition 7 we have (giεi)!
(gi!)εiεi! ((gi − 1)!ℓgi−1)εi.

As this is for every i ∈ [h] and all the cycles are disjoint, by the principle of multiplication
we have
 aℓ!
 h∏

i=1
 1
(giεi)! (giεi)!
(gi!)εiεi! ((gi − 1)!ℓgi−1)εi ,

mth roots of σℓ that consist of εi cycles of length giℓ, for every i ∈ [h]. This expression
reduces to
 aℓ!
 h∏

i=1
 ℓ(gi−1)εi

gεi
i εi! .

Finally, we sum over all the elements in Em(ℓ, aℓ). Repeat the process for every cycle
length ℓ in σ with aℓ ̸= 0. So we have that the number of mth roots of a permutation of

type a is
 r(m)(a) = ∏

ℓ≥1
aℓ̸=0
 aℓ!
 

 ∑

ε ∈Em(ℓ,aℓ)
 h∏

i=1
 ℓ(gi−1)εi

giεiεi!
 

 .

Note that r(m)(a) is zero if and only if Em(ℓ, aℓ) is an empty set for some ℓ, i. e. if aℓ is
not a multiple of ((ℓ, m)).

4.2 A generating function: Proof of Theorem 2

First we obtain a generating function for permutations of Type (ℓ)gp.

Proposition 8. Let ℓ, m be ﬁxed positive integers. Let g ∈ Gm(ℓ). Let p ∈ N0. Let σ be
any permutation of Type (ℓ)gp. Let f (gp) be the number of mth roots of Type (gℓ)p of σ.

10

Then
 ∑

p≥0 f (gp) t
gp
ℓ
(gp)! = exp (ℓ(g−1)

g t
g
ℓ )
.

Proof. Use Proposition 7 to obtain

∑

p≥0 f (gp) t
gp
ℓ
(gp)! = ∑

p≥0
 (gp)!ℓp(g−1)

gpp! t
gp
ℓ
(gp)!

= ∑

p≥0
 ℓp(g−1)

gp t
gp
ℓ
(p)!

= exp (ℓ(g−1)

g t
g
ℓ )
.

Note that if p = 0, f (gp) = 1, but p = 0 does not have sense in this context, we use
it only for technical purposes. Now, we give a generating function for the number of mth

roots of a permutation of type a, for m ﬁxed.
Theorem 2. For n = a1 + 2a2 + · · · + nan, the coeﬃcient of t
a1
1 ···t
an
n
a1!···an! in the expansion
of
 exp ( ∑

ℓ≥1
 ∑

g∈Gm(ℓ)
 ℓg−1

g t
g
ℓ )
, (2)

is the number the mth roots of an n-permutation of type a = (a1, ..., an).

Proof. We expand equation (2) and we look the coeﬃcients of our interest. First note
that for any ℓ the only factors that contribute to exponent of t
aℓ
ℓ (aℓ ̸= 0) are the factors
in ∏

g∈Gm(ℓ) e ℓg−1
g t
g
ℓ = ∏

g∈Gm(ℓ)
 ( ∑

j≥0
 ℓ(g−1)j

gj t
gj
ℓ ) 1
j! ,

with aℓ = g1j1 + · · · + gkjk, where k = |Gm(ℓ)|, g = (gi, ..., gk) is the associate vector of
Gm(ℓ) and j1, ..., jk is any non negative solution of equation g1x1 + · · · + gkxk = aℓ. The

coeﬃcient of any t
aℓ
ℓ is ∑

g1j1+···+gkjk=aℓ
 k∏

i=1
 ℓ(gi−1)ji

gji
i
 1
ji! .

11

For the coeﬃcient of t
aℓ
ℓ /aℓ! multiply the previous expression by aℓ!. Clearly the coeﬃcient
of t
a1
1 ···t
an
n
a1!···an! comes from equation (2) when we take ℓ from 1 to n and this coeﬃcient is

∏

ℓ≥1
aℓ̸=0
 aℓ! ∑

g1j1+···+gkjk=aℓ
 k∏

i=1
 ℓ(gi−1)ji

gji
i
 1
ji! .

Note that this expression is equivalent to the right hand side of equation in Theorem 1

by changing g1j1 + · · · + gkjk = aℓ in the index of summation by ε ∈ Em(ℓ, aℓ), where
ε = (j1, ..., jk) ∈ Em(ℓ, aℓ) = {ε ∈ Nk
0 : g1j1 + · · · + gkjk = aℓ}.

Another proof can be obtained using Proposition 8. For ﬁxed length ℓ, we build the set
Gm(ℓ), and for ﬁxed g ∈ Gm(ℓ) we can obtain the generating function as in Proposition 8.

Then we use properties of generating functions to obtain ∏

g∈Gm(ℓ) e ℓg−1
g t
g
ℓ . As for diﬀerent

ℓ, the variables tℓ are diﬀerent, then we can obtain the desired generating function as the
product ∏

ℓ≥1 ∏

g∈Gm(ℓ) e ℓg−1
g t
g
ℓ .
The next corollary is for the special case when m is equal to a prime number p. Note

that by Propositions 2 and 6, we have that if gcd(ℓ, p) = 1 then Gp(ℓ) = {1, p} and for
gcd(ℓ, p) = p, Gp(ℓ) = {p}.

Corollary 2. Let p be a ﬁxed prime number. For n = a1 + 2a2 + · · · + nan, the coeﬃcient
of t
a1
1 ···t
an
n
a1!···an! in the expansion of
 exp ( ∑

i≥1
 i
p−1

p t
p
i + ∑

j≥1
gcd(j,p)=1
 tj)

is the number of p-th roots of an n-permutation of type a = (a1, ..., an).

5 A property of the probability pm(n)

Let m be a power of a prime number p. In this section we include a proof of an interesting
property about the probability, pm(n), that an n-permutation chosen at random has an

mth root. In the work of B´ona et al. [4], there are a combinatorial proof of the identity
pm(n) = pm(n + 1), with m a prime number, and for all n not congruent to −1 mod m.
We prove the analogous result for the case when m is a power of prime number q, ﬁrst by

using the generating function of the number of permutations that admit an mth root (see

12

[5] for a diﬀerent proof). We use the terminology in [15]. For q ≥ 1, let expq(x) denote
the formal series deﬁned by
 expq(x) = ∑

i≥0
 x
iq

(iq)! .

The following statement can be found as Theorem 4.8.3 in H. Wilf’s generatingfunctionol-
ogy (p. 149, [15])

Theorem 4. Let r(n, m) be the number of n-permutations that have an mth root. Then

∞∑

n=0 r(n, m) x
n

n! =
 ∞∏

ℓ=1 exp((ℓ,m)) (x
ℓ

ℓ
 )
.

Remark 3. Note that if m is a prime power, m = pr, then for any l ∈ N

((l, m)) =
 


1 if gcd(l, p) = 1

m otherwise

The next proposition gives one property of pm(n).

Proposition 9. Let p be a prime. Let pm(n) be the probability that an n-permutation

chosen uniformly at random has an mth root. If m = pr, r ∈ N, then for all j ∈ N0 we
have
 pm(jp) = pm(jp + 1) = · · · = pm(jp + (p − 1))

Proof. By Remark 3 the generating function in Theorem 4 can be written as

∏

l ∈ N exp((l,m))
 ( x
l

l
 ) = ∏

l ∈ N
gcd(l,m)=1
 exp (x
l

l
 ) ∞∏

j=1 expm
 ( x
jp

jp
 )

which can be written in the form

∞∏

j=1 exp ( x
j

j
 ) ∞∏

j=1 exp (
−x
jp

jp
 ) ∞∏

j=1 expm
 ( x
jp

jp
 ) ,

or
 13

1
(1 − x) (1 − x
p)1/p ∞∏

j=1 expm
 (x
jp

jp
 ) .

Notice that, due to the fact that m = pr, we can write (1 − x
p)1/p ∏∞
j=1 expm ( xjp
jp ) as a
function of the form G (x) = ∑∞
j=0 bjx
pj, for any adequate election of bj. Now 1
(1−x)G (x),
where G(x) := (1 − x
p)1/p ∏∞
j=1 expm (x
jp/jp) is the power series of some function in the

variable x
p. Note that pm(n) is the coeﬃcient of x
n in the expansion of

∞∑

n=0 r(n, m) x
n

n! = 1
(1 − x) G (x) = 1
(1 − x)
 ∞∑

k=0 bkx
kp

Now, if we take n = kp, for any k = 0, 1, ... we have that

pm(kp) = b0 + b1 + b2 + · · · + bk

pm(kp + 1) = b0 + b1 + b2 + · · · + bk
.

pm(kp + (p − 1)) = b0 + b1 + b2 + · · · + bk

5.1 A second proof of Proposition 9

In this section, we give a second proof of Proposition 9. Here we deduce Proposition 9
from Corollary 2.12 in [4]. We start by recalling some notation and deﬁnitions used in

[4]. Let P OW ERm(n) be the set of n-permutations that have at least one mth root. Let
DIVρ,m(n) denote the set of n-permutations whose cycles of length a multiple of m have
type ρ and let divρ,m(n) = |DIVρ,m(n)|/n!. For π ∈ DIVρ,m(n), we denote with π(m) (re-

spectively π(∼m)) the part of π consisting of the cycles of lengths which are (respectively
not are) multiples of m. By Theorem 3 and Remark 3, if m = pr is a power of a prime p,

then the set P OW ERpr(n) consist of all n-permutations whose number of cycles of length
a multiple of p is divisible by pr. Corollary 2.12 in [4] says that if p does not divide n + 1
then divρ,p(n) = divρ,m(n + 1). So in order to prove Proposition 9 we only need to show

14

that if n + 1 is not a multiple of p then the only possible cycle types for π(p) are the same
for P OW ERm(n) as for P OW ERm(n + 1). We will prove that this is the case. Let ρ be

any cycle type of π(p) with π ∈ P OW ERm(n) then, clearly, ρ is a cycle type of π′
(p) for
some π′ in P OW ERm(n + 1). Let π ∈ P OW ERm(n + 1). Since p does not divide n + 1,
then π(∼p) cannot be empty. Then the n-permutation π′ with π′
(p) = π(p) and with the part

π′
(∼p) (possible empty) containing as ﬁxed points all the elements (diﬀerent that n + 1) in
π(∼p), has prth root and hence ρ is also the cycle type of a permutation π′ in P OW ERm(n).

Acknowledgements. The authors would like to thank E. Ugalde and L. Glebsky for
many useful comments. Also the authors would like to thank the anonymous referees for

its carefully reading and valuable comments and suggestions. Section 5.1 was not present
in the original version. Its addition was inspired on a referee’s thoughtful question. Part of

this work was made when R. Moreno was staying at Campus Jalpa, UAZ. The ﬁnal version
was written while Rivera-Mart´ınez was a postdoctoral fellow at the University of Vienna,
supported by the European Research Council (ERC) grant of Goulnara Arzhantseva,

grant agreement n
o 259527.

References

[1] S. Annin, T. Jansen and C. Smith, On kth roots in the symmetric and alternating
groups, Pi Mu Epsilon Journal, 12, No. 10 (2009), 581-589.

[2] J. Blum, Enumeration of the square permutations in Sn, J. Comb. Theory, (A) 17,

(1974), 156–161.

[3] B. Bollob´as and B. Pittel, The distribution of the root degree of a random permuta-

tion, Combinatorica 29 (2) (2009), 131–151.

[4] M. B´ona, A. McLennan and D. White, Permutations with roots, Random Structures
E algorithms, 17 (2000), No. 2, 157–167.

[5] W. W. Chernoﬀ, Permutations with pl-th roots, Disc. Math., 125 (1994) 123–127.

[6] M. Deza and T. Huang, Metrics on Permutations, a Survey, J. Comb. Inf. Sys. Sci.,

23 (1998), 173–185.
 15

[7] L. Glebsky and L. M. Rivera, Almost solutions of equations in permutations, Tai-
wanese J. Math., 13 (2009), No. 2A, 493–500.

[8] A. Groch, D. Hofheinz, and R. Steinwandt, A practical attack on the root problem

in braid groups, Contemporary Math., 418 (2006), 121–132.

[9] A. Mar´oti, Symmetric functions, generalized blocks, and permutations with restricted

cycle structure, European J. Combin. 28, (2007), No. 3, 942–963.

[10] A. I. Pavlov, On the number of solutions of the equation x
k = a in the symmetric
group Sn, Mat. Sb., 112(154)(1980), 380–395; English transl. Math. USSR Sb., 40

(1981).

[11] M. R. Pournaki, On the number of even permutations with roots, Australas.
J.Combin., 45 (2009), 37–12.

[12] N. Pouyanne, On the number of permutations admitting an mth root, Electron. J.

Comb., 9 (2002), #R3., 1–12.

[13] V. Schoup, A Computational Introduction to Number Theory and Algebra, Cam-

bridge University Press, 2nd edition, (2008)

[14] P. Tur´an, On some connections between combinatorics and group theory, Colloq.
Math. Soc. J´anos Bolyai, P. Erd¨os, A. R´enyi and V. T. S´os, eds., North Holland,

Amsterdan (1970), 1055–1082.

[15] H. S. Wilf, Generatingfunctionology, Academic Press, San Diego, 2nd edition, (1994).

Jes´us Lea˜nos
Unidad Acad´emica de Matem´aticas,
Universidad Aut´onoma de Zacatecas,
Zacatecas, Zac. CP 98000, M´exico.

E-mail: jelema@uaz.edu.mx

Rutilo Moreno
Instituto de F´ısica,
Universidad Aut´onoma de San Luis Potos´ı,
San Luis Potos´ı, SLP. CP 78210, M´exico.

E-mail: rutilo.moreno@gmail.com

Luis Manuel Rivera-Mart´ınez,
Ingenier´ıa El´ectrica Jalpa,
Universidad Aut´onoma de Zacatecas,
E-mail: luismanuel.rivera@gmail.com
 16
