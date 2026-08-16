<!-- source: http://simonrs.com/eulercircle/analyticnt/ethan-shiustrings.pdf | converted from PDF -->

ON STRINGS OF CONGRUENT PRIMES

ETHAN YANG

1. Introduction

This expository account serves as an overview of the work surrounding Shiu’s result on
strings of congruent primes. [KLS00] In 1920, Chowla conjectured that there were inﬁnitely
many pairs of consecutive primes such that they were congruent to a modulo q, for any
relatively prime a and q. In particular, let p1 = 2, p2 = 3, p3 = 5 . . . be the sequence of
primes. Then Chowla’s conjecture says that for any relatively prime q, a, there are inﬁnitely
many pairs of consecutive primes pn and pn+1 such that

pn ≡ pn+1 ≡ a (mod q).

Shiu proved in 2000 a stronger version of Chowla’s conjecture, that for any k ∈ N there
exists a string of k congruent primes such that

pn+1 ≡ pn+2 ≡ · · · ≡ pn+k ≡ a (mod q).

He gave a bound on the size of the string versus the size of the largest prime. In particular,
he split his argument into two cases of choices for a. We deﬁne

A+ = {a : ∀p | q, a ≡ 1 mod p}

and A− = {a : ∀p | q, a ≡ −1 mod p} .
and A± = A+ ∪ A−. Shiu found that longer strings in terms of the largest prime could be
found when considering residues from A±.
The main theorem we will prove is the following:

Theorem 1.1. (1) For each q and a ∈ A± and large x, there exists a string of primes

pn+1 ≡ pn+2 ≡ · · · ≡ pn+k ≡ a (mod q),

where pn+k < x and
 k ≫ ( log log x
log log log x
 )1/φ(q) .

(2) For each q and a with (q, a) = 1 and large x, there exists a string of primes

pn+1 ≡ pn+2 ≡ · · · ≡ pn+k ≡ a (mod q),

where pn+k < x and

k ≫ ( log log x log log log log x
(log log log x)2
 )1/φ(q) .

Further work on similar results to this theorem by Freiberg in 2010, where he found that
that consecutive primes can be made close together as well [Fre11].
1

2 ETHAN YANG

Theorem 1.2. Let q ≥ 3 and a be integers with (q, a) = 1, and ﬁx any ε > 0. There
exist inﬁnitely many pairs of consecutive primes pr, pr+1 such that pr ≡ pr+1 ≡ a mod q and
pr+1 − pr < ε log pr.

From state of the art work on the theory of small gaps between primes developed by
Maynard, Tao, Zhang, and others in [May15], Freiberg was further able to show in 2015 a
stronger version of Shiu’s result [Fre13].

Theorem 1.3. Let p1 = 2 < p2 = 3 < · · · be the sequence of all primes. Let q ≥ 3
and a be a coprime pair of integers, and let m ≥ 2 be an integer. There exists a constant
B = B(q, a, m), depending only on q, a and m, such that the following holds. There exist
inﬁnitely many n such that

pn+1 ≡ pn+2 ≡ · · · ≡ pn+m ≡ a mod q and pn+m − pn+1 ≤ B.

Although we won’t prove these two theorems, the reader can read the proofs of them.

2. Outline

The rest of the paper focuses on proving Theorem 1.1. Section 3 deﬁnes useful notation
and states necessary lemmas without proof. The proof of the theorem deﬁnes Q(y) as a
product of q and a subset of primes less than y, where y is carefully chosen such that the
L-functions modulo Q(y) have no Siegel zeros. This is done so that the distribution of primes
in residue classes modulo Q(y) are all the same and what we expect it to be.
After creating intervals such that they are dense in primes equivalent to a mod q and
sparse in other primes, a matrix M is created similar to in Maier’s proof of the existance of
chains of large gaps between consecutive primes [Mai85]. The matrix has rows of consecutive
integers, and the columns are arithmetic progressions with common diﬀerence Q(y).
We prove that most of the primes in M are congruent to a mod q, exceeding the other
primes by a constant factor. After considering two cases, this implies that there is a string
of primes that are congruent to a mod q in one of the columns of the matrix. The length
of the string is estimated as well.
 3. Background

Throughout the proof, we will use the following function

P (y, p0) = q ∏

p≤y
p̸=p0
 p,

where q is as in the statement of Theorem 1.1.
We provide lemmas used in the proof that will not be proven here, but can be found in
the original paper by Shiu.

Lemma 3.1. There exists a ﬁxed constant C such that for all q ∈ N and large X there exists
y and prime p0 ≫ log y such that none of the L-functions modulo P (y, p0) has a zero in the
region 1 ≥ ℜ(s) ≥ 1 − c
log(P (y, p0)(|ℑ(s)| + 1))
and X < P (y, p0) ≪ X(log X)
2.

ON STRINGS OF CONGRUENT PRIMES 3

Lemma 3.2. Let C be a constant and let q′ be a natural number such that the L-functions
induced by characters mod q′ have no zeros in the region

1 ≥ ℜ(s) ≥ 1 − c
log(q′(|ℑ(s)| + 1)) .

Then there exists a constant D depending on at most C such that the estimates
x
φ(q′) log x ≪ π(x; q′, a
′) ≪ x
φ(q′) log x

hold uniformly for (q′, a
′) = 1 and x ≥ q′D, where π(x; q′, a
′) counts the number of primes
less than or equal to x congruent to a′ mod q′.

Lemma 3.3. Let q be a natural number and S (x) denote the set of positive integers n ≤ x
which only have primes congruent to 1 mod q in its prime factorization. Then as x → ∞,
we have
 |S (x)| = (
c0 + O( 1
log x)
) x
log x(log x)1/φ(q),

where c0 is a constant depending at at most q.

Before stating the next lemma, we must deﬁne what it means to be a smooth number.

Deﬁnition 3.4. For a positive real number y and positive integer n, n is said to be y-smooth
if every prime factor of n is ≤ y. Let Ψ(x, y) be the number of y-smooth numbers n ≤ x.

The next lemma attempts to estimate Ψ(x, y) as both x and y go to inﬁnity. More precisely,
we have the following inequality due to de Bruijin:

Lemma 3.5. For y ≤ x and y approaching inﬁnity with x, we have

Ψ(x, y) ≤ x(log y)2 exp(−u log u − u log log u + O(u)),

where u = log x/ log y.

Armed with these lemmas, we are ready to prove Shiu’s theorem.

4. Main Result

We now proceed to prove Theorem 1.1. For a given q, a, x from the statement of the
theorem and suﬃciently large D, Lemma 3.1 gives us a y and prime p0 such that

x1/D < P (y, p0) ≪ x1/D(log x)
2.

and such that there is no L-function that has a zero in the region described in the lemma.
We deﬁne the product Q(y) = q ∏
p∈Pa p, where the product is over primes in the set Pa,
which is deﬁned next. We further deﬁne z ≤ y and t ≤ (yz)
1/2 and deﬁne a set of primes
less than y, depending on whether a is in A±.

Pa =
 



{p ≤ y : p ̸= p0, p ̸≡ 1 mod q} for a ∈ A±,
{p ≤ y : p ̸= p0, p ̸≡ 1, a mod q}
∪ {t ≤ p ≤ y : p ̸= p0, p ≡ 1 mod q}
∪ {p ≤ yz/t : p ̸= p0, p ≡ a mod q} otherwise.

4 ETHAN YANG

For either of these cases, since Pa only excludes primes that are less than y, we have that
Q(y) | P (y, p0) and that log P ≤ 3 log Q. As a result, there are no L-functions modulo Q(y)
such that 1 ≥ ℜ(s) ≥ 1 − c
3 log(Q(y)(|ℑ(s)| + 1)) ,

because an L-function modulo Q(y) that has a zero in that region would imply a zero in the
same region for an L-function modulo P (y, p0) and thus contradict the assumption made on
choice of y and p0 from Lemma 3.1.
An interval I of length yz is deﬁned in various cases of the residue class of a

I =
 



(m, m + yz] for a ∈ A+
[n − yz, n) for a ∈ A−
(0, yz] otherwise,

where m and n satisfy
 m ≡ n ≡
 {
0 mod p for pq | Q
a − 1 mod q .

We now construct a matrix M that has dimensions of Q(y)
D−1 rows and yz columns of
integers
 M =
 Q(y)D−1
⋃

k=1
 ⋃

i∈I(i + kQ(y)).

The columns of the matrix M are an arithmetic progression with common diﬀerence Q(y),
so we are trying to ﬁnd a column that contains our string of primes. We also deﬁne the sets

S = {i ∈ I : (i, Q) = 1, i ≡ a mod q},

T = {i ∈ I : (i, Q) = 1, i ̸≡ a mod q},

P1 = {p ∈ M : p prime, p ≡ a mod q},

P2 = {p ∈ M : p prime, p ̸≡ a mod q}.
Our goal is to estimate |P1| and |P2|, showing that there are more primes in P1. We do this
by ﬁrst estimating |S| and |T |. We ﬁrst estimate the two sets for the case a ∈ A±.
In particular, when a ∈ A±, we have that

S = |{j ∈ (0, yz] : (j, Q) = 1, j ≡ 1 mod q}|,

T = |{j ∈ (0, yz] : (j, Q) = 1, j ̸≡ 1 mod q}|.
This can be seen with a bijection from S to the interval (0, yz]. If a ∈ A+, then i ∈ I
and i ≡ a mod q if and only if i − m ≡ 1 mod q. Furthermore, (i, Q) = 1 if and only if
(i − m, Q) = 1 since m | Q which completes the bijection for the case a ∈ A+. In the other
case where a ∈ A−, we can take n − i instead of i − m and the same arguments follow.
We know that if n ∈ (0, yz] and only has primes p ≡ 1 mod q in its prime factorization,
then n ≡ 1 mod q and (n, Q) = 1 by our construction of P. This implies that n ∈ S when
n ∈ S (yz) and thus we have the following bound from Lemma 3.3.

|S| ≥ |S (yz)| ≫ yz(log y)
1/φ(q)

log y .

ON STRINGS OF CONGRUENT PRIMES 5

For every j ̸≡ 1 mod q, there exists a prime p | j such that p ̸≡ 1 mod q. Elements of
T are estimated by estimating the number of elements of the form pn where p ̸≡ 1 mod q
and n ∈ S (z) and multiples of p0 in (0, yz]. There are O(yz/ log y) such multiples which is
less than the elements of the ﬁrst type. We estimate those such elements by splitting the
interval (y, yz] into O(log z) intervals of length 2
ly.

|T | ≪ ∑

l≪log z
 ∑

2l−1y<p≤2ly |S (z/2
l)|

≪ ∑

l≪log z
 2
l−1y
log y z(log z)
1/φ(q)

2l log z

≪ yz(log z)1/φ(q)

log y .

When a ̸∈ A±, we can employ a similar strategy as the above splitting argument to estimate
|S|. From our construction of P, the elements of S are of the form pn such that p >
yz/t, p ≡ a mod q, n ∈ S (t) in the interval (0, yz]. Using the splitting argument, replacing
z with t, we have the following bound.

|S| ≫ yz(log t)
1/φ(q)

log y .

Elements of T are now of three possible types. They are composed of multiples of p0, special
multiples of a prime larger than y that we estimated using our splitting argument, or only
have prime factors less than t and congruent to 1 mod q. We already estimated the ﬁrst
two types, and the third type is estimated using de Bruijin’s bound for smooth numbers in
Lemma 3.5. We take
 t = exp (
θ log y log log log y
log log y
 ) .

From Lemma 3.5, we have the inequality

Ψ(yz, t) ≤ yz(log t)
2 exp(−θ−1 log log y + o(log log y)) ≪ yz
log y ,

when θ is suﬃciently small (θ = 1/4 works). The dominating term is thus still the one from
the splitting argument, so in both cases of Theorem 1.1, we have the estimate

|T | ≪ yz(log z)1/φ(q)

log y .

Every element of S and T is the ﬁrst term in an arithmetic progression mod Q(y). We now
estimate |P1| and |P2| by using Lemma 3.2. We can choose D such that

|P1| ≫ |S| x
φ(Q) log x, |P2| ≪ |T | x
φ(Q) log x

for suﬃciently large x such that x ≥ Qd. There are two cases that we argue one of which
happens. Let M ′ be the subset of columns of M which contain a prime in P2. The ﬁrst is
that there exists an interval in M ′ where the primes belonging to P1 exceed those belonging
to P2 by a factor of |P1|/2|P2 or the number of primes in M \ M ′ is at least |P1|/2. Formally,
there either exists
 I0 ∈ M ′ : |I0 ∩ P1| ≥ 1
2 |P1|
|P2| |I0 ∩ P2|

6 ETHAN YANG

or |(M \ M ′) ∩ P1| ≥ 1
2 |P1|.

One of these two cases must be true, as if we assume by contradiction that both of them are
false, then
 |P1| = |P1 ∩ M ′| + |P1 ∩ (M \ M ′)|

= ∑

I∈M ′ |P1 ∩ I| + |P1 ∩ (M \ M ′)|

< 1
2 |P1|
|P2|
 ∑

I∈M ′ |I ∩ P2| + 1
2|P1|

= 1
2 |P1|
|P2||P2| + 1
2 |P1| = |P1|.

Since this leaves us with |P1| < |P1|, we have reached a contradiction and thus at least one
of our two cases must arise.
If the ﬁrst case is true, then our interval I0 must contain a string of primes of length k
where k ≫ |P1|/|P2|. If the second case is true, we ﬁrst note that there can be at most x/Q
intervals in M \ M ′ and thus one of them must contain a string of primes of length k where
k ≫ Q|P1|/x. From our above bound for |P1|,

Q|P1|
x ≫ |S| Q
φ(Q) log x.

Substituting our deﬁnition of Q,

Q
φ(Q) = q
φ(q)
 ∏

p∈P
 p
p − 1 = q
φ(q)
 ∏

p∈P
 (
1 − 1
p
 )−1 .

By a generalization of Merten’s theorem, we have Q/φ(Q) ≫ (log y)1/φ(q)/ log y if a ∈ A±
and Q/φ(Q) ≫ (log t)
1/φ(q)/ log y otherwise. Then

Q|P1|
x ≫ yz
log x ≫ z

because log x ≪ Q ≪ y.
Combining the bounds on k for the two cases, there exists a column in m with a string of
length k where
 k ≫ min ( P1
P2 , z) .

Substituting our bounds for |P1|, |P2|, |S|, and |T |, we end up with the following when a ∈ A±:

k ≫ min
 (( log y
log z
 )1/φ(q) , z
)
 .

Otherwise when a ̸∈ A±,
 k ≫ min
 (( log t
log z
 )1/φ(q) , z
)
 .

Setting z = log log x proves Theorem 1.1.

ON STRINGS OF CONGRUENT PRIMES 7

Shiu also provided an estimate for the number of such strings in his paper through Theorem
2, which we will not prove here. Similar to Theorem 1.1, Shiu split his theorem into two
cases on the residue class of a. In particular, when a ∈ A±, there are more strings.

Theorem 4.1. Deﬁne
 ε1(x) = C(q)k (log log log x
log log x
 )1/φ(q)

and
 ε2(x) = C ′(q)k ( (log log log x)
2

log log x log log log log x
 )1/φ(q)

(1) Given q, k, a ∈ A±, the number B of strings of primes of the form

pn+1 ≡ pn+2 ≡ · · · ≡ pn+k ≡ a (mod q),

where pn+k < x, has the asymptotic bound

B ≫ x1−ε1(x).

(2) Given q, k, a, where q and a are relatively prime, the number B of strings of primes
of the form pn+1 ≡ pn+2 ≡ · · · ≡ pn+k ≡ a (mod q),
where pn+k < x, has the asymptotic bound

B ≫ x1−ε2(x).

References

[Fre11] Tristan Freiberg. Strings of congruent primes in short intervals. Journal of the London Mathematical
Society, 84(2):344–364, 07 2011.
[Fre13] Tristan Freiberg. A note on the theorem of maynard and tao. 77, 11 2013.
[KLS00] D K. L. SHIU . Strings of congruent primes. Journal of the London Mathematical Society, 61:359
– 373, 04 2000.
[Mai85] Helmut Maier. Primes in short intervals. Michigan Math. J., 32(2):221–225, 1985.
[May15] James Maynard. Small gaps between primes. Annals of Mathematics, 181(1):383–413, 2015.
