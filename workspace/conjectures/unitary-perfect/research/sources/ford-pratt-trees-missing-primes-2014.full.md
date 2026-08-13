<!-- source: https://arxiv.org/pdf/1212.3498 | converted from PDF -->

arXiv:1212.3498v2  [math.NT]  4 Feb 2013
SIEVING VERY THIN SETS OF PRIMES, AND PRATT TREES WITH MISSING PRIMES

KEVIN FORD

Dedicated to the memory of Paul T. Bateman

ABSTRACT. Suppose P is a set of primes, such that for every p ∈ P, every prime factor of p − 1 is also in P.
We apply a new sieve method to show that either P contains all of the primes or the counting function of P is
O(x1−c) for some c > 0, where c depends only on the smallest prime not in P. Our proof makes use of results
connected with Artin's primitive root conjecture.

1 Introduction

Consider a set P of primes satisfying the condition:

(1.1) p ∈ P =⇒ ∀q|(p − 1), q ∈ P.

Here and throughout, the letters p, q and r denote primes. Trivial examples of sets P are the empty set and
the set of all primes.
We are concerned in this note with nontrivial examples, nonempty P omitting at least one prime (since
2 ̸∈ P implies that P is empty, the smallest omitted prime must be odd). Let p0 denote the smallest prime
not in P and let P (x) = #{p ∈ P : p ⩽ x} be the associated counting function. Our main result is the
following.

Theorem 1. Let P be a set of primes satisfying (1.1) that does not contain the prime p0. There are constants
δ > 0 and c > 0, depending only on p0, such that P (x) ⩽ cx1−δ.

Theorem 1 implies that either P is the set of all primes or P is a very “thin” set of primes. The elements
of P have the property that for every prime p ̸∈ P, P omits the residue classes 0, 1 mod p. Standard
application of sieve methods produce only the much weaker bound P (x) ≪ x/ log2 x (see Proposition 1
below). The weakness stems from the fact that sieve methods ignore congruential restrictions for “large”
primes (i.e., those primes > √x, when bounding the number of elements of a set that are ⩽ x). With our
new method, we are able exploit these large prime restrictions.
To the author's knowledge, sets of primes satisfying (1.1) w ere ﬁrst considered by R. D. Carmichael [2, 3]
in his work on the conjecture that now bears his name. Here φ is Euler's “totient” function.

Conjecture 1 (Carmichael's Conjecture) . For every positive integer a, there is an positive integer b ̸= a
such that φ(b) = φ(a).

The conjecture remains open, although the smallest counterexample a, if there is one, is known to exceed
101010 [6]. Assuming a counterexample a exists, Carmichael [3] attacked the problem with the following
simple result.

(1.2) If d ∏

p|d p divides a and p = 1 + d is prime, then p2|a.

Date: October 27, 2018. 1

2 KEVIN FORD

Applying (1.2) successively with d = 1, 2, 6 and 42, it follows immediately that 223272432|a. From
here, Carmichael considers two cases: (i) 32∥a, which easily implies 132|a, and (ii) 33|a, which im-
plies by (1.2) that 192|a. In each case, one can use (1.2) to produce many more primes which divide
a. More precisely, in case (i), a must be divisible by all primes in P ′, where P ′ contains 2, 3, 7, 13, 43
and for other primes p, p ∈ P ′ if and only if p − 1 is squarefree and for every q|(p − 1), q ∈ P ′.
Then P ′ = {2, 3, 7, 13, 43, 79, 547, 3319, 6163, . . .}. Similarly, in case (ii), a is divisible by every prime
in P ′′, where 2, 3, 7, 19, 43 are in P ′′ and for other primes p, p ∈ P ′′ if and only if (a) p − 1 is ei-
ther squarefree or 32|(p − 1) and p−1
9 is squarefree and (b) for every q|(p − 1), q ∈ P ′′. Then P ′′ =
{2, 3, 7, 19, 43, 127, 2287, 4903, 5419, . . .}. Thus, the sets P ′ and P ′′ each satisfy (1.1) and omit the prime
5. By Theorem 1, each of P ′ and P ′′ has counting function satisfying P (x) ≪ x1−c for some c > 0.
Carmichael's conjecture follows if both P ′ and P ′′ are inﬁnite.
In a similar spirit, Pomerance [15] showed that if x satisﬁes p2|x whenever (p − 1)|φ(x), then there is
no number b ̸= x with φ(b) = φ(x). However, Pomerance argued heuristically that no x with this property
exists.

Sets satisfying (1.1) also arise in the distribution of iterates of Euler's function. Let φk(n) denote the k-th
iterate of φ (e.g., φ2(n) = φ(φ(n))), and let F (n) = ∏
k⩾1 φk(n) (the product is ﬁnite, since φk(n) = 1
for large k). Divisibility properties of F (n) were considered by Luca and Pomerance [13] in connection
with construction of irreducible, radical extensions of Q. The prime factors of F (p), where p runs over the
primes, were considered by Bayless [1]. Further results on φk(n) may be found in [4].

Corollary 1. For every prime r ⩾ 3, there is a constant s < 1 so that #{n ⩽ x : r ∤ F (n)} ≪ xs.

Proof. Let Pr be the largest set satisfying (1.1) such that r ̸∈ Pr; i.e., Pr contains all primes less than r,
r ̸∈ Pr and a prime p > r lies in Pr if and only if for all q|(p − 1), q ∈ Pr. For example,

P3 = {2, 5, 11, 17, 23, 41, 43, 83, 89, 101, 137, 167, 179, 251, 257, . . .},

P5 = {2, 3, 7, 13, 17, 19, 29, 37, 43, 53, 59, 73, 79, 97, 103, . . .}.

Since φ(pa) = pa−1(p − 1), for each n the (ﬁnite) set P of prime factors of F (n) satisﬁes (1.1). Hence, if
r ∤ F (n), then all the prime factors of n belong to Pr. By Theorem 1, for some c > 0, depending on r, there
are ≪ x1−c primes in Pr that are less than x. For any s > 1 − c, it follows by partial summation that the
number of n ⩽ x with r ∤ F (n) is at most
∑

p|n =⇒ p∈Pr
 ( x
n
 )s = xs ∏

p∈Pr
 (1 − p−s)−1 ⩽ xs exp { ∑

p∈Pr
 1
ps − 1
 } ≪r,s xs. □

The set Pr is also the set of all primes p for which the Pratt tree for p has no node labeled r. The Pratt
tree for a prime p is recursively deﬁne as the tree with root labeled p, and below p are links to the Pratt trees
of each q|(p − 1). Properties of Pratt trees (e.g. the distribution of the height H(p), number of nodes, etc.)
were extensively studied in [7]. In alternative terminology, Pr is the set of primes p for which there is no
prime chain r ≺ p0 ≺ · · · ≺ pk ≺ p, where a ≺ b means b ≡ 1 (mod a), and p0, . . . , pk are primes.

A ﬁnite group G is said to have Perfect Order Subsets (POS) if the number of elements of G of any given
order divides |G|. This notion was introduced by Finch and Jones [5] in 2002. In the case of Abelian groups,
Finch and Jones reduced the problem of determining which groups have POS to studying those of the form
G = (Z/p1Z)a1 × · · · × (Z/pjZ)aj , where p1, . . . , pj are distinct primes. This group has POS if and only
if f (n)|n, where n = pa1
1 · · · paj
j = |G| and f (n) = ∏pa∥n(pa − 1). Suppose that 3 ∤ n. It follows quickly
that the primes dividing n must lie in P3. Developing explicit estimates for the counting function of P3, it
was shown in [8] that an Abelian group with POS is either Z/2Z or has order divisible by 3. This answered
a question posed in [5].

SIEVING VERY THIN SETS OF PRIMES, AND PRATT TREES WITH MISSING PRIMES 3

It is intractible with existing methods to prove nontrivial lower bounds for P (x) even in the “easiest”
cases when P = Pr. The difﬁculty, now evident from Theorem 1, is to show that many primes exist with
the prime factors of p − 1 restricted to a very thin set.

Conjecture 2. Each set Pr is inﬁnite.

This conjecture follows, for instance, if there are iniﬁnitely many primes of the form 2a3b + 1 and
inﬁnitely many primes of the form 2a5b + 1. Each of these latter statements appears to be plausible, based
on computations.
The author computed the elements of P3 up to 244 (≈ 1.7 × 1013) for use in [8], and P (x) ≈ x0.62 in
this range. The recursive nature of the sets P, however, does not lead to any natural heuristic argument for
the size of P (x). The growth appers to be highly dependent on which small primes are omitted from the
set. For an extreme example, consider P to be the “largest ” set omitting the primes 3, 5, 17, 257, 65537 (the
list of known Fermat primes – primes that are 1 more than a power of 2). It is a famour unsolved problem
whether or not there are additional Fermat primes. If there are no further Fermat primes then P = {2},
while if another Fermat prime exists then P could potentially be inﬁnite.
Based partly on the computations for P3, we make an educated guess for the growth of P (x).

Conjecture 3. For each r, there is a number δr > 0 such that P (x) = x1−δr+o(1) as x → ∞.

We further guess that δr → 0 as r → ∞.

Outline of the paper. The next section contains relatively simple estimates for P (x) which are needed to
bootstrap the more complicated iterative method in Sections 3 and 4. Basically, we ﬁnd recursive inequalities
for the density of primes whose Pratt tree has height ⩽ j, for j = 0, 1, 2, . . .. The main iteration inequalities
are proved in Section 3, together with a conditional result that implies Theorem 1 under the assumption that
a certain matrix has eigenvalues all inside the unit circle. Section 4 concludes the proof of Theorem 1 by
showing that indeed the matrix has this property. Our method uses results from the circle of ideas used to
attack Artin's primitive root conjecture.

2 Simple sieve estimates

From now on, we always assume that P is a set of primes satisfying (1.1) and that there is some prime
not in P, the smallest such we denote by p0. All estimates using the Landau O−symbol and Vinogradov
≪ −symbol may depend on p0, but not on any other quantity. The symbols p an q, with or without
subscripts, always denote primes.

Proposition 1. We have P (x) ≪ x/ log2 x and ∑

p∈P
 1
p ≪ 1.

Proof. By (1.1) and standard application of sieve methods [10, Theorem 4.2],

(2.1) P (x) ≪ x
log x
 ∏

q⩽x1/4
q̸∈P
 (1 − 1
q
 ) .

Since P omits all primes q ≡ 1 (mod p0), (2.1) and Mertens' estimate for primes in arithmetic progr essions
imply that P (x) ≪ x

(log x)1+1/(p0−1) .

By partial summation, ∑p∈P 1/p ≪ 1 and thus ∏p∈P (1 − 1/p) ≫ 1. Applying (2.1) again and Mertens'
bound, we ﬁnd that P (x) ≪ x/ log2 x. □

4 KEVIN FORD

Our proof of Theorem 1 requires a slight improvement to Proposition 1 to bootstrap the method.

Lemma 2.1. We have P (x) ≪ x(log x)−5/2.

Proof. For p ∈ P with p ⩽ x, let q be the largest prime factor of p − 1, write p = 1 + qm and deﬁne
y = x1/(10 log log x). By standard counts of smooth numbers (see e.g., Theorem 1 in §III.5 of [16]), the
number of p with q ⩽ y is ≪ x/ log5 x. Next, ﬁx m ⩽ x/y, and observe that q ̸≡ 1 (mod r) for each prime
r ̸∈ P. By sieve methods [10, Theorem 4.2] and Proposition 1, the number of p ⩽ x is bounded above by

#{n ⩽ x/m : ∀r ̸∈ P, r ∤ n(n + 1)(mn + 1)} ≪ x/m
log3(x/m)
 ∏

p|m(m+1)
 (1 − 1
p
 )−1

⩽ x/m
log3(x/y) m2 + m
φ(m2 + m)

≪ x(log log x)4

m log3 x .

Since m is composed of prime factors in P, Proposition 1 implies

∑

m
 1
m ⩽ ∏

p∈P
 (1 − 1
p
 )−1 ≪ 1.

The claimed bound follows. □

3 The main iteration

The proof of Theorem 1 is based on recursive inequalities for sums over subsets of P. We partition the
primes p ∈ P according to the height H(p) of their Pratt trees. The height may be deﬁned iteratively by

H(2) = 1, H(p) = 1 + max
q|(p−1) H(q).

We denote Ph = {p ∈ P : H(p) ⩽ h} (h ∈ N)

and also deﬁne, for h ∈ N and real s > 0,

Vh(s) = ∑

p∈Ph
 1
(p − 1)s , Th = {n ∈ N : p|n =⇒ p ∈ Ph}.

We also allow h = ∞ in the above notations. In particular, P1 = {2} and P∞ = P. A trivial, but very
useful observation, is that

(3.1) p ∈ Ph =⇒ p − 1 ∈ Th−1.

Our goal is to show that V∞(s) is ﬁnite for some s < 1, which is clearly equivalent to Theorem 1.
A trivial bound which we will use often is

(3.2)
 ∞∑

a=1
 1
qas = 1
qs − 1 ⩽ λ(s)
(q − 1)s , λ(s) = 1
2s − 1 (0 < s ⩽ 1).

Lemma 3.1. For every h ⩾ 1, Vh(s) is continuous for 0 < s ⩽ 1.

SIEVING VERY THIN SETS OF PRIMES, AND PRATT TREES WITH MISSING PRIMES 5

Proof. It sufﬁces to show that Vh(s) is ﬁnite. This follows by induction on h, starting from V1(s) = 1 for
all s, and using (3.1) and (3.2) to obtain the iterative bound

Vh(s) ⩽ ∑

m∈Th−1
 1
ms = ∏

p∈Ph−1
 1
1 − p−s = ∏

p∈Ph−1
 (1 + 1
ps − 1
 )

⩽ ∏

p∈Ph−1
 (1 + λ(s)
(p − 1)s
 ) ⩽ eλ(s)Vh−1(s).
(3.3)

We next develop more sophisticated bounds for Vh(s) in terms of Vh−1(s). It turns out that when s is
close to 1, Vh(s) is dominated by primes p ∈ Ph for which p − 1 has only a single “large” prime factor
(meaning a prime q with large height H(q)). For k > j ⩾ 1, denote

̃Tj,k = {n ∈ Tk \ Tj : p2|n for some p ∈ Pk \ Pj, or n has at least 2 prime factors in Pk \ Pj},

T j,k = (Tk \ Tj) \ ̃Tj,k.

Lemma 3.2. For k > j ⩾ 1 and s > 0, we have
∑

n∈ ̃Tj,k
 1
ns ⩽ 2λ(s)
2 (Vk(s) − Vj(s))2 e
λ(s)Vk(s).

Proof. For n ∈ ̃Tj,k, let q1, . . . , qd be the prime factors of n that are in Pk \ Pj (“large” prime factors). Then
n = qa1
1 · · · qad
d m, where m ∈ Tj and a1, . . . , ad are positive integers. Also, either (i) d ⩾ 2 or (ii) d = 1
and q2
1|n. We deduce that

∑

n∈ ̃Tj,k
 1
ns ⩽
 [ ∑

q∈Pk\Pj
 ∞∑

a=2
 1
qas +
 ∞∑

d=2
 1
d!
 ( ∑

q∈Pk\Pj
 ∞∑

a=1
 1
qas
 )d] ∑

m∈Tj
 1
ms .

Using (3.2) multiple times, we see that the ﬁrst double sum on the right side is at most
∑

q∈Pk\Pj
 1
qs(qs − 1) ⩽ ∑

q∈Pk\Pj
 λ(s)
(q − 1)2s ⩽ λ(s) (Vk(s) − Vj(s))
2 ,

the second double sum over q and a is at most
∑

q∈Pk\Pj
 λ(s)
(q − 1)s = λ(s) (Vk(s) − Vj(s)) ,

and the sum on m is bounded above by
∏

p∈Pj(1 − 1/ps)
−1 ⩽ e
λ(s)Vj (s).

Thus,
 ∑

n∈ ̃Tj,k
 1
ns ⩽ e
λ(s)Vj (s) (Vk(s) − Vj(s))2 [
λ(s) + λ(s)
2 ∞∑

d=2
 (Vk(s) − Vj(s))d−2λ(s)d−2

d!
 ]
.

Finally, d! > (d − 2)! and so the sum on d is less than eλ(s)(Vk(s)−Vj (s)). □

6 KEVIN FORD

We now come to the main iteration inequality. Instead of descending just one level as in the proof of
Lemma 3.1 (that is, examining the prime factors of p − 1), we descend a ﬁnite (and bounded) number of
levels, examining the prime factors q1 of p − 1, the prime factors q2 of each q1 − 1, etc. To state our result,
we introduce a family of matrices Ms,j,Q. Let

(3.4) UQ = {1 ⩽ n ⩽ Q : (n, Q) = 1 and ∀p|Q such that p ̸∈ P, n ̸≡ 1 (mod p)}.

By (1.1), for any Q and p ∈ P with p ∤ Q, we have p mod Q ∈ UQ. For j ⩾ 1, s > 0 and Q ∈ N, let
Ms,j,Q be the Q × Q matrix whose entries are given by

(3.5) Ms,j,Q(a, b) = ∑

m∈Tj
am≡b (mod Q)
 m−s

if a ∈ UQ and b ∈ UQ, and Ms,j,Q(a, b) = 0 otherwise. For a generic square matrix M with non-negative
entries, we introduce notation for row sums and column sums:

Ra(M ) = ∑

b M (a, b), R(M ) = max
a Ra(M ), Cb(M ) = ∑

a M (a, b), C(M ) = max
b Cb(M ).

Lemma 3.3. Suppose that n ∈ N, h > j ⩾ n, Q ∈ N and Pj−n contains every prime in P which divides
Q. Then, for M = Ms,j,Q,

Vh(s) ⩽ Vj(s) + ∑

q∈Ph−n\Pj−n
 Rq mod Q(M n)
qs + 2nλ(s)
2e
nλ(s)Vh−1(s) (Vh−1(s) − Vj−n(s))2 .

Proof. We'll ﬁrst show, by induction on n, that for any integers h and j satifying h > j ⩾ n,

(3.6) Vh(s) ⩽ Vj(s) + 2nλ(s)
2enλ(s)Vh−1(s) (Vh−1(s) − Vj−n(s))2

+ ∑

qn∈Ph−n\Pj−n
 1
qs
n
 ∑

mn∈Tj−n
mnqn+1=qn−1
qn−1 prime
 1
ms
n
 ∑

mn−1∈Tj−n+1
mn−1qn−1+1=qn−2
qn−2 prime
 1
ms
n−1 · · · ∑

m1∈Tj−1
m1q1+1=q0
q0 prime
 1
ms
1 .

To begin the induction, we use (3.1) and Lemma 3.2 to obtain

Vh(s) = Vj(s) + ∑

q0−1∈Th−1\Tj−1
 1
(q0 − 1)s

⩽ Vj(s) + 2λ(s)
2e
λ(s)Vh−1(s) (Vh−1(s) − Vj−1(s))2 + ∑

q0−1∈T j−1,h−1
 1
(q0 − 1)s .

In the ﬁnal sum, we may write q0 = 1 + m1q1, where m1 ∈ Tj−1 and q1 ∈ Ph−1 \ Pj−1. This proves (3.6)
when n = 1.
Now suppose that (3.6) holds for some n, and assume that h > j ⩾ n + 1. In the multiple sum in (3.6),
replace q−s
n with (qn − 1)−s and observe that qn − 1 ∈ Th−n−1 \ Tj−n−1. The contribution to the multiple
sum from those summands with qn − 1 ∈ ̃Tj−n−1,h−n−1 is, by Lemma 3.2 and (3.3), at most

2λ(s)
2eλ(s)Vh−n−1(s) (Vh−n−1(s) − Vj−n−1(s))2 ∑

mn∈Tj−n m−s
n · · · ∑

m1∈Tj−1 m−s
1

⩽ 2λ(s)
2e
λ(s)Vh−1(s) (Vh−1(s) − Vj−n−1(s))
2 e
λ(s)(Vj−n(s)+···+Vj−1(s))

⩽ 2λ(s)
2e
λ(s)(n+1)Vh−1(s) (Vh−1(s) − Vj−n−1(s))
2 .

SIEVING VERY THIN SETS OF PRIMES, AND PRATT TREES WITH MISSING PRIMES 7

If qn −1 ∈ T j−n−1,h−n−1, then qn = 1+qn+1mn+1, where qn+1 ∈ Ph−n−1\Pj−n−1 and mn+1 ∈ Tj−n−1.
This proves (3.6) with n replaced by n + 1. By induction, (3.6) follows for all n.
In (3.6), we enlarge the range of all sums on mi to mi ∈ Tj−1. Also, for 0 ⩽ i ⩽ n − 1, we relax the
condition that qi is prime to qi ≡ ai (mod Q), where ai ∈ UQ. Recalling (3.5), we ﬁnd that the multiple
sum in (3.6) is at most
∑

qn∈Ph−n\Pj−n q−s
n ∑

an−1∈UQ
 ∑

mn∈Tj−1
mnqn+1≡an−1 (mod Q)
 m−s
n · · · ∑

a0∈UQ
 ∑

m1∈Tj−1
m1a1+1≡a0 (mod Q)
 m−s
1

= ∑

qn∈Ph−n\Pj−n q−s
n ∑

an−1,...,a0∈UQ M (qn mod Q, an−1)M (an−1, an−2) · · · M (a1, a0)

= ∑

qn∈Ph−n\Pj−n q−s
n Rqn mod Q(M n).

This completes the proof of the lemma. □

Assuming V∞(s) exists and h and j are large, Vh−1(s) − Vj−n(s) will be very small if j is large. Con-
sequently, of the three terms on the right side of the inequality in Lemma 3.3, the third may be regarded as
“small”, since it is quadratic in Vh−1(s)−Vj−n(s). The second term is at most (Vh−1(s)−Vj−n(s))R(M n),
and can be regarded as larger than the third term. It can also be made very small, provided that M is a con-
tracting matrix (all eigenvalues lie inside the unit circle) and n is large enough. Under this assumption on
M , it follows that Vh(s) ⩽ Vj(s) + (Vh−1(s) − Vj−n(s))ε,

where ε is small. Iteration of this inequality, with j and n ﬁxed, then shows that the sequence V0(s), V1(s), . . .
is bounded. The next lemma makes this heuristic precise.

Lemma 3.4. Suppose that for some y and for Q = ∏
p⩽y p, M1,∞,Q is a contracting matrix. Then for some
s < 1, V∞(s) is ﬁnite.

Proof. By assumption, R(M n
1,∞,Q) ⩽ 1
4 for some n. Let D = V∞(1) (D exists by Proposition 1) and let

ε = 1
100ne2n(D+2) .

Fix j large enough so that j > n, Pj−n contains all primes in P which are ⩽ y, and Vj(1) − Vj−n(1) ⩽ ε/2.
By Lemma 3.1, Vj(s) and Vj−n(s) are continuous for 0 < s ⩽ 1, as are all entries of Ms,j,Q. Note that
R(M n
1,j,Q) ⩽ R(M n
1,∞,Q) ⩽ 1
4 . Therefore, there is an s ∈ [0.9, 1) such that

(a) Vj(s) ⩽ D + 1,
(b) Vj(s) − Vj−n(s) ⩽ ε,
(c) R(M n
s,j,Q) ⩽ 1
3 .

Since s ⩾ 0.9, we have λ(s) ⩽ 2. By Lemma 3.3 and (c), for any h > j, it follows that

Vh(s) ⩽ Vj(s) + 1
3 (Vh−1(s) − Vj−n(s)) + 8ne
2nVh−1(s) (Vh−1(s) − Vj−n(s))
2 .

For k ⩾ 0, let xk = Vj+k(s) − Vj(s). Then x0 = 0 and, by (a) and (b), for k ⩾ 1 we have

xk ⩽ 1
3 (xk−1 + Vj(s) − Vj−n(s)) + 8ne
2n(xk−1+Vj(s)) (xk−1 + Vj(s) − Vj−n(s))2

⩽ 1
3 (xk−1 + ε) + 8ne2n(D+1+xk−1)(xk−1 + ε)
2 =: f (xk−1).

8 KEVIN FORD

We have f (0) > 0, f ′′(x) > 0 for x > 0 and

f (ε) = 2
3 ε + 8ne2n(D+1+ε)(2ε)
2 < 2
3 ε + 32
100 ε < ε.

Therefore, f (x) = x has a unique root ˜x ∈ (0, ε) and it follows that limk→∞ xk ⩽ ˜x. Consequently,

V∞(s) ⩽ Vj(s) + ˜x ⩽ D + 1 + ε. □

4 Matrix eigenvalues and the proof of Theorem 1

Throughout this section, we assume that Q = ∏p⩽y p and M = M1,∞,Q. Observe that by Proposition 1,

(4.1) K = ∏

p∈P
 (1 − 1
p
 ) ≫ 1.

Because all entries of M are nonnegative, the Perron-Frobenius theorem implies that there is an eigenvalue
of largest modulus which is real and positive. The matrices M are similar to the matrices studied in [7, §2],
and we will likewise focus on bounding column sums of M . However, the estimation problem is much more
complicated than the analogous problem in [7].

Lemma 4.1. For any b ∈ UQ, let d = (b − 1, Q) and b′ = b−1
d . Then

(4.2) Cb(M ) = φ(d)
d
 ∑

k∈T∞
(k,Q/d)=1
(4.3)
 1
k ,

where

(4.3) ∀p ⩽ y with p ̸∈ P, k ̸≡ b′ (mod p).

Proof. By the deﬁnition of UQ in (3.4), 2|d and for all p|d, p ∈ P. In (3.5), therefore, am + 1 ≡ b (mod Q)
implies that d|m. Writing m = dk, we have (k, Q/d) = 1 and ak ≡ b′ (mod Q/d). Since a ∈ UQ, a ̸≡ 1
(mod p) for any p ⩽ y with p ̸∈ P. Hence, (4.3) holds. Therefore, by (3.5),

Cb(M ) = ∑

a∈UQ
 ∑

k∈T∞
ak≡b′ (mod Q/d)
(4.3)
 1
dk = 1
d
 ∑

k∈T∞
(k,Q/d)=1
(4.3)
 1
k #{a ∈ UQ : ak ≡ b′ (mod Q/d)}.

For every k ∈ T∞ satisfying (k, Q/d) = 1 and (4.3), there is a unique solution a mod Q/d of the con-
gruence ak ≡ b′ (mod Q/d) and moreover this solutions satisﬁes a ∈ UQ. Thus, there are φ(d) solutions
a ∈ UQ, and this completes the proof. □

Notice that if we ignore condition (4.3), then we obtain from (4.2) the upper bound

(4.4) Cb(M ) ⩽ φ(d)
d
 ∑

k∈T∞
(k,Q/d)=1
 1
k = φ(d)
d
 ∏

p∈P
p|d or p>y
 (
1 − 1
p
 )−1 = ∏

p∈P,p>y
 (1 − 1
p
 )−1 .

The product on the far right side of (4.4) is always greater than 1, however it tends to 1 as y → ∞ by
Proposition 1. In order to obtain a bound C(M ) < 1, it is necessary to use (4.3) to eliminate some numbers
k from the sum in (4.4). However, if k ∈ T∞ with (k, Q/d) = 1 and k < y, then only primes dividing d
may divide k. In the worst case d = 2, the only numbers k < y that are available to eliminate are powers of
2. If there is a prime p ̸∈ P for which 2 is a primitive root (generator of (Z/pZ)∗), then we will succeed.

SIEVING VERY THIN SETS OF PRIMES, AND PRATT TREES WITH MISSING PRIMES 9

Lemma 4.2. Suppose p ̸∈ P and 2 is a primitive root of p. Then, for large enough y depending on p,

C(M ) ⩽ 1 − 2
1−pK,

where K is deﬁned in (4.1).

Proof. For any b ∈ UQ, let d = (b − 1, Q) and b′ = b−1
d as before. Since b ̸≡ 1 (mod p), we have
(b′, p) = 1. Hence, there is an exponent θ ∈ {0, 1, . . . , p − 2} such that 2θ ≡ b′ (mod p). By Lemma 4.1
and (4.4),
 Cb(M ) ⩽ φ(d)
d
 [ ∑

k∈T∞
(k,Q/d)=1
 1
k − 1
2θ
 ]
 ⩽ ∏

p∈P
p>y
 (1 − 1
p
 )−1 − 2
2−p φ(d)
d .

The lemma follows upon observing that
 inf
d∈T∞ φ(d)
d = K

and that if y is large then ∏

p∈P
p>y
 (1 − 1
p
 )−1 ⩽ 1 + 2
1−pK. □

Remarks. It is conjectured that there are inﬁnitely many primes that have 2 as a primitive root, but
this is an open problem. Hooley [12] showed that the Riemann Hypothesis for the Dedekind zeta functions
ζKr (s) for the number ﬁelds Kr = Q(21/r, e2πi/r), where r runs over the primes, implies that the number of
primes p ⩽ x which have 2 as a primitive root is ∼ cx/ log x, where c = ∏r(1− 1
r(r−1) ) = 0.3739 . . .. This
asymptotic formula is known as Artin's primitive root conje cture for the base 2. If true, then by Proposition
1, most of these primes are not in P, and we obtain Theorem 1 upon invoking Lemma 4.2. For more about
Artin's conjecture, the reader may consult the comprehensi ve survey article [14].
Unconditionally, Lemmas 3.4 and 4.2 imply Theorem 1 in the case that 2 is a primitive root of p0 (p0 ∈
{3, 5, 11, 13, 19, . . .}), or if there is a prime q ≡ 1 (mod p0) with 2 as a primitive root; for example if
p0 = 7 then we may take q = 29.

There is a way around invoking Artin's conjecture: by examin ing column sums of small powers of M , we
succeed if there is a prime p ̸∈ P with (Z/pZ)∗ generated by a bounded set of small primes. The following
result of Gupta and Murty [9] supplies us with the necessary prime p.

Lemma 4.3. For ≫ x/ log2 x primes p ⩽ x, (Z/pZ)∗ is generated by 2, 3 and 5.

Remarks. Heath-Brown [11] proved the stronger statement that for ≫ x/ log2 x primes p ⩽ x, either 2,
3 or 5 is a primitive root of p. Our argument below, in fact, requires only the weaker statement that for some
k and primes p1, . . . , pk, each with 2 as a primitive root, there are ≫ x/ log2 x primes p ⩽ x for which
(Z/pZ)∗ is generated by 2, p1, . . . , pk. We would then iterate Lemma 4.4 below k times instead of twice.

Utilizing Lemma 4.3, we will show that C(M 3) < 1 for large y. Our main tool is the following, which
roughly says that if Cb(M k) < 1 for every b lying in some arithmetic progression, then Cb(M k+1) < 1 for
all b lying in a larger arithmetic progression.

Lemma 4.4. Let p be a prime in P with 2 as a primitive root, and let n ∈ T∞ satisfy n|Q and p ∤ n. Let
u ∈ N. Suppose that for large y and for all b ≡ 1 (mod pn), Cb(M u) ⩽ 1 − δ where δ > 0. Then, for
large enough y (depending on p, n, δ, p0, u) and all b ≡ 1 (mod n), Cb(M u+1) ⩽ 1 − δ′, where

δ′ = δK
2
pn .

10 KEVIN FORD

Proof. Suppose that b ∈ UQ with b ≡ 1 (mod n). If p|(b − 1), we apply (4.4) and the general inequality
Cb(AB) ⩽ C(A)Cb(B) to obtain

Cb(M u+1) ⩽ Cb(M u)C(M ) ⩽ (1 − δ) ∏

p∈P,p>y
 (1 − 1
p
 )−1 ⩽ 1 − δ
2 ⩽ 1 − δ′

if y is large enough. Now assume p ∤ (b − 1). As in Lemma 4.1, put d = (b − 1, Q) and b′ = b−1
d . We have

Cb(M u+1) = ∑

a∈UQ Ca(M u)M (a, b)

= ∑

a∈UQ Ca(M u) ∑

m∈T∞
am+1≡b (mod Q)
 1
m

= 1
d
 ∑

k∈T∞
(k,Q/d)=1
(4.3)
 1
k
 ∑

a∈UQ
ak≡b′ (mod Q/d)
 Ca(M u).

(4.5)

For each k, the congruence ak ≡ b′ (mod Q/d) has a unique solution a mod Q/d, hence there are φ(d)
solutions a ∈ UQ. By assumption, there is a θ ∈ {0, 1, . . . , p − 2} with 2θ ≡ b′ (mod p). In (4.5), we
use the crude bound Ca(M u) ⩽ C(M u) ⩽ C(M )u for all pairs a, k except when both k = 2θ and a ≡ 1
(mod n). In the latter case, a ≡ 1 (mod p) as well, hence a ≡ 1 (mod pn) and Ca(M u) ⩽ 1 − δ. Also,
since n|Q and b ≡ 1 (mod n), we have n|d. By (4.4) and (4.5),

Cb(M u+1) ⩽ C(M )
u[ φ(d)
d
 ∑

k∈T∞
(k,Q/d)=1
 1
k − 1
2θd
 ∑

a∈UQ
a≡1 (mod nQ/d)
 1

]
 + 1
2θd
 ∑

a∈UQ
a≡1 (mod nQ/d)

(1 − δ)

⩽ max (1, C(M )
u) φ(d)
d
 ∑

k∈T∞
(k,Q/d)=1
 1
k − δ
2θd φ ( d
n
 )

⩽ ∏

p∈P,p>y
 (1 − 1
p
 )−(u+1) − δ

2
p−2d φ ( d
n
 ) .

Since φ(d/n) ⩾ φ(d)/n and φ(d)/d ⩾ K, upon recalling the deﬁnition of δ′ we conclude that

Cb(M u+1) ⩽ ∏

p∈P,p>y
 (1 − 1
p
 )−(u+1) − δK

2
p−2n ⩽ 1 − δ′

if y is large enough. □

Proof of Theorem 1. If p0 ∈ {3, 5}, Lemma 4.2 (with p = p0) implies that C(M ) < 1 for large enough y.
Hence, by Lemma 3.4, V∞(s) is ﬁnite for some s < 1.
Now assume that 3 ∈ P and 5 ∈ P. Combining Lemmas 2.1 and 4.3, we ﬁnd that there is a prime p1 ̸∈ P
for which 2,3 and 5 generate (Z/p1Z)∗. Following the proof of Lemma 4.2, for any b ∈ UQ with b ≡ 1
(mod 30), there are exponents a2, a3, a5 ∈ {0, 1, . . . , p1 − 2} so that 2
a2 3
a3 5
a5 ≡ b′ (mod p1). As before,

SIEVING VERY THIN SETS OF PRIMES, AND PRATT TREES WITH MISSING PRIMES 11

b′ = b−1
(b−1,Q) . By (4.3), k = 2
a2 3
a3 5
a5 is excluded from the sum in (4.2). By (4.4), if y is large enough then

Cb(M ) ⩽ ∏

p∈P,p>y
 (1 − 1
p
 )−1 − φ(d)/d

2
a2 3
a3 5
a5 ⩽ ∏

p∈P,p>y
 (1 − 1
p
 )−1 − K

30
p1−2 < 1 − δ,

where δ = K/30
p1 −1. By Lemma 4.4 with n = 6, p = 5 and u = 1, we ﬁnd that for large enough y,
Cb(M 2) ⩽ 1 − δ′ for every b ≡ 1 (mod 6), where

δ′ = Kδ
25 · 6 .

A second application of Lemma 4.4, with n = 2, p = 3 and u = 2 implies that for every b ∈ UQ,
Cb(M 3) ⩽ 1 − δ′′ if y is large enough, where δ′′ = Kδ′/16. Thus, the dominant eigenvalue of M 3 is at
most 1 − δ′′, hence the dominant eigenvalue of M is ⩽ (1 − δ′′)1/3 < 1. Finally, applying Lemma 3.4, we
ﬁnd that V∞(s) is ﬁnite for some s < 1. It follows immediately that P (x) = O(X s). □

Acknowledgements. The author thanks Paul Pollack for helpful conversations concerning Lemma 2.1, and
is thankful to Paul Bateman for introducing to him Carmichael's conjecture and related problems.
The author's research was supported by National Science Fou ndation Grants DMS-0901339 and DMS-
1201442. Much of the work was accomplished while the author attended the N.S.F. supported Workshop in
Linear Analysis and Probability at Texas A&M University, July-August, 2012.

References

[1] J. Bayless, The Lucas-Pratt primality tree, Math. Comp. 77 (2008), 495-502.
[2] R. D. Carmichael , On Euler's φ-function , Bull. Amer. Math. Soc. 13 (1907) , 241–243.
[3] , Note on Euler's φ-function , Bull. Amer. Math. Soc. 28 (1922) , 109–110.
[4] P. Erd˝os, A. Granville, C. Pomerance, and C. Spiro, On the normal behavior of the iterates of some arithmetic functions, in
Analytic Number Theory, Proceedings of a conference in honor of Paul T. Bateman, Birkh¨auser, Boston, 1990, 165–204.
[5] C. Finch and L. Jones, A Curious Connection Between Fermat Numbers and Finite Groups, Amer. Math. Monthly 109 (2002),
517–524.
[6] K. Ford, The distribution of totients, Ramanujan J. (Paul Erd˝os memorial issue) 2 (1998), 67–151.
[7] K. Ford, S. Konyagin and F. Luca, Prime chains and Pratt trees, Geom. Funct. Anal. 20 (2010), 1231–1258.
[8] K. Ford, S. Konyagin and F. Luca, On groups with perfect order subsets, Moscow J. Comb. Number Theory 2, no. 4 (2012),
to appear.
[9] R. Gupta and M. Ram Murty, A remark on Artin's conjecture , Inv. Math. 78 (1984), 127–130.
[10] H. Halberstam and H.-E. Richert, Sieve methods, Academic Press, London, 1974.
[11] D. R. Heath-Brown, Artin's conjecture for primitive roots , Quart. J. Math. Oxford (2) 37 (1986), 27–38.
[12] C. Hooley, On Artin's conjecture , J. Reine Angew. Math. 225 (1967), 209–220.
[13] F. Luca and C. Pomerance, Irreducible radical extensions and Euler-function chains, in “Combinatorial number theory”,
351–361, de Gruyter, Berlin (2007).
[14] P. Moree, Artin's primitive root conjecture - a survey , INTEGERS (The electronic journal of combinatorial number theory)
12A (2012), paper A13. See also arXiv.math/0412262v2 (2012).
[15] C. Pomerance, On Carmichael's conjecture , Proc. Amer. Math. Soc. 43 (1974), 297–298.
[16] G. Tenenbaum, Introduction `a la th´eorie analytique et probabiliste des nombres, troisi`eme ´Edition, coll. ´Echelles, Belin, 2008,
592 pp. English translation of the second edition: Introduction to analytic and probabilistic number theory, Cambridge Univ.
Press, 1995.

DEPARTMENT OF MATHEMATICS, 1409 WEST GREEN STREET, UNIVERSITY OF ILLINOIS AT URBANA-CHAMPAIGN,
URBANA, IL 61801, USA
E-mail address: ford@math.uiuc.edu
