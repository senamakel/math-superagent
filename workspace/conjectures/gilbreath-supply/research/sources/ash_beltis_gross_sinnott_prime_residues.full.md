<!-- source: http://fmwww.bc.edu/gross/ABGS.pdf | converted from PDF -->

This article was downloaded by: [Boston College], [Robert Gross]
On: 09 December 2011, At: 16:07
Publisher: Taylor & Francis
Informa Ltd Registered in England and Wales Registered Number: 1072954 Registered office: Mortimer House,
37-41 Mortimer Street, London W1T 3JH, UK

Experimental Mathematics
Publication details, including instructions for authors and subscription information:
http://www.tandfonline.com/loi/uexm20

Frequencies of Successive Pairs of Prime Residues

Avner Ash a
 , Laura Beltis b
 , Robert Gross a
 & Warren Sinnott c

a
 Department of Mathematics, Boston College, Chestnut Hill, MA, 02467-3806, USA
b
 Actuarial Analysis Department, Tufts Health Plan, Watertown, MA, 02472, USA
c
 Department of Mathematics, The Ohio State University, Columbus, OH, 43210-1174, USA

Available online: 28 Nov 2011

To cite this article: Avner Ash, Laura Beltis, Robert Gross & Warren Sinnott (2011): Frequencies of Successive Pairs of Prime
Residues, Experimental Mathematics, 20:4, 400-411

To link to this article:  http://dx.doi.org/10.1080/10586458.2011.565256

PLEASE SCROLL DOWN FOR ARTICLE

Full terms and conditions of use: http://www.tandfonline.com/page/terms-and-conditions

This article may be used for research, teaching, and private study purposes. Any substantial or systematic
reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to
anyone is expressly forbidden.

The publisher does not give any warranty express or implied or make any representation that the contents
will be complete or accurate or up to date. The accuracy of any instructions, formulae, and drug doses should
be independently verified with primary sources. The publisher shall not be liable for any loss, actions, claims,
proceedings, demand, or costs or damages whatsoever or howsoever caused arising directly or indirectly in
connection with or arising out of the use of this material.

Experimental Mathematics, 20(4):400–411, 2011
Copyright C· Taylor & Francis Group, LLC
ISSN: 1058-6458 print / 1944-950X online
DOI: 10.1080/10586458.2011.565256

Frequencies of Successive Pairs of Prime Residues

Avner Ash, Laura Beltis, Robert Gross, and Warren Sinnott

CONTENTS

1. Introduction
2. Notation
3. The Heuristic
4. Some Observations
5. Numerical Checks of Antidiagonal Symmetry
6. Numerical Checks of Power-of-2 Prediction
7. Numerical Checks of the Heuristic
8. Another Prediction
9. Further Open Questions
Acknowledgments
References

2000 AMS Subject Classiﬁcation: 11N05, 11K45, 11N69
Keywords: prime pairs, Bateman–Horn, Hardy–Littlewood, P´olya
 We consider statistical properties of the sequence of ordered
pairs obtained by taking the sequence of prime numbers and
reducing modulo m. Using an inclusion/exclusion argument and
a cutoff of an inﬁnite product suggested by P ·olya, we obtain a
heuristic formula for the “probability” that a pair of consecutive
prime numbers of size approximately x will be congruent to
(a, a + d) modulo m. We demonstrate some symmetries of our
formula. We test our formula and some of its consequences
against data for x in various ranges.

1. INTRODUCTION

In a beautiful paper from 1959, P´olya presented a heuris-
tic formula to approximate the number of primes p<x
such that q = p + d is also prime, where d is a positive
even integer [P´olya 59]. His formula is a special case of the
Bateman–Horn conjecture [Bateman and Horn 62], and
had already been proposed in [Hardy and Littlewood 23].
However, his method of derivation is much more elemen-
tary.
P´olya uses the standard probabilistic model of the
primes. His innovation is in deciding where to cut oﬀ
a certain product, which he determines by invoking
Mertens’s theorem. In our treatment, this cutoﬀ step,
involving Euler’s constant, occurs in (3–1).
P´olya does not care whether there are primes between
p and q. In contrast, we ask about consecutive prime
pairs, and we are interested in gaps not only equal to d
but congruent to d modulo a given positive integer m.
This interest stems from our earlier work [Ash et al. 09],
in which we studied the statistics of the sequence of prime
numbers modulo m. For this reason, we actually look at
the ﬁner count of consecutive prime pairs congruent to a
given (a, a + d) (mod m).
We can thus state our problem as follows:

Problem 1.1. Given positive integers a, d,and m and a
positive number x, deﬁne N (a, d, m, x) to be the number
of consecutive prime pairs p<q such that p<x, p ≡

400Downloaded by [Boston College], [Robert Gross] at 16:07 09 December 2011
Ash et al.: Frequencies of Successive Pairs of Prime Residues 401

a,and q ≡ a + d (mod m). What are the asymptotics of
N (a, d, m, x)as x tends to inﬁnity?

Dirichlet’s theorem tells us that if we look only at
single primes, the number of primes p<x with p ≡ a
(mod m) is approximately π(x)/ϕ(m), independent of a
(provided that a is relatively prime to m). Here ϕ is the
Euler ϕ-function. One might suppose that the residues
modulo m of consecutive prime pairs would be “indepen-
dent” in a pseudoprobabilistic sense, and therefore that
N (a, d, m, x) would be approximately independent of a
and d (provided that a and a + d are relatively prime to
m). However, this appears not to be the case in the nu-
merical evidence compiled in [Ash et al. 09] and in this
paper.
For example, suppose m = 4 and consider consecutive
pairs of primes congruent to (1, 1) and (1, 3) respectively.
Our data show that there is a deﬁnite tendency for the
(1, 1)-pairs to occur considerably less frequently than the
(1, 3)-pairs. We do not know whether this tendency per-
sists as x increases.
The results in [Hardy and Littlewood 23] suggest
an explanation of the imbalance. If d is a posi-
tive even integer, then Hardy and Littlewood propose
[Hardy and Littlewood 23, p. 42, Conjecture B] that the
probability that x and x + d are prime is asymptotic to
∏

p|d,p> 2
 p − 1
p − 2 · 2C2
(log x)2 .

Here
 C2 = ∏

p> 2
 (1 − 1
(p − 1)2
 ) .

In particular, the probability that x and x + 2 are prime
is asymptotic to
 2C2
(log x)2 .

We observe that the dependence on d occurs only
through the factor ∏
p|d,p> 2 p−1
p−2 , and therefore this factor
should tell us the relative frequency of primes p such that
p + d is also prime when compared to the frequency of
twin primes. Here is a table of values for small d:

d 2 4 6 8 10 12 14 16
∏p|d,p> 2 p−1
p−2 1 1 2 1 4
3 2 6
5 1

Thus, for example, primes p such that p + 6 is also prime
should occur twice as often as twin primes.
If p is a prime congruent to 1 mod 4, and the next
prime q is congruent to 3 mod 4, then q = p + d for d ∈
 {2, 6, 10, 14,... }, while if the next prime q is congruent to
1 mod 4, then q = p + d for d ∈{4, 8, 12, 16,... }. The ta-
ble above suggests that (p, q) ≡ (1, 3) (mod 4) would be
more likely. However, the suggestion raises further ques-
tions, since even if p + d is prime, it does not mean that
it is the next prime after p. For example, it is perfectly
possible for each of p, p +4, and p + 6 to be prime. Thus
there are interactions among the various events “p and
p + d are prime” that need to be taken into account if we
want to predict whether (p, q) ≡ (1, 3) (mod 4) is more
likely than (p, q) ≡ (1, 1) (mod 4).
To the best of our knowledge, Problem 1.1 is wide
open, and cannot be treated using L-functions, unlike
the case of Dirichlet’s theorem. In this paper, we at-
tempt a heuristic solution to Problem 1.1 by applying
an inclusion/exclusion argument, together with P´olya’s
heuristic argument, in Section 3. This leads to a formula
for a function we call P (a, d, m, x), which heuristically
should be the “probability” that x is a prime congruent
to a (mod m) and the next largest prime is congruent to
a + d (mod m). Thus, we should have the approximation
N (a, d, m, x) ≈ P (a, d, m, x)x, in the sense that

lim
x→∞ P (a, d, m, x)x
N (a, d, m, x) =1. (1–1)

However, (1–1) is not the appropriate conjecture to
verify. For the same reasons that the approximation
π(x) ≈ x/ log x is less accurate than π(x) ≈ ∫ x
2 dy/ log y,
we instead compare N (a, d, m, X) − N (a, d, m, x) with
∑X
y =x+1 P (a, d, m, y). We do not attempt to provide a
measure of how good this approximation should be, since
there is no actual underlying probability distribution we
are sampling. Nor did P´olya do so in [P´olya 59].
In fact, our expression for P is an inﬁnite series, and
we do not know whether this series converges. Thus, we
choose an integer J ≥ 0 and truncate P at the Jth term
to obtain a ﬁnite expression PJ (a, d, m, x). Our heuris-
tic proposes that PJ (a, d, m, x) should be the “proba-
bility” that x is a prime congruent to a (mod m)and
that the next prime is x + d + jm for some j =0,...,J.
Thus, if J is suﬃciently large (given x), our heuristic sug-
gests that PJ (a, d, m, x) should be a “density function”
for N (a, d, m, x) in the sense given above. Our heuris-
tic does not tell us exactly how to choose J. We suggest
below that d + Jm ≈ 4 log x is a reasonable choice.
We ﬁrst investigate properties of the heuristic formula
for PJ for a ﬁxed J and test them against some actual
data. Below we present data for only a few values of m,
which suﬃce to convey the general picture.Downloaded by [Boston College], [Robert Gross] at 16:07 09 December 2011
402 Experimental Mathematics, Vol. 20 (2011), No. 4

The function PJ (a, d, m, x) possesses two exact sym-
metries. First, Proposition 4.2 states that

PJ (a, d, m, x)= PJ (−a − d, d, m, x).

We call this “antidiagonal symmetry” because of its ap-
pearance when we arrange the values of PJ (a, d, m, x)in
a matrix indexed by a and a + d. Second, Proposition 4.1
says that when m is a power of 2, PJ (a, d, 2
k ,x) is inde-
pendent of a.
We test these two symmetry predictions against ac-
tual data in Sections 5 and 6 respectively. The idea is
that ∑X
y =x+1 PJ (a, d, m, y) should closely approximate
N (a, d, m, X) − N (a, d, m, x). Therefore the matrix of
N (a, d, m, X), indexed by (a, a + d), should show approx-
imately these two symmetries.
In addition to these symmetries, the observations at
the start of Section 4 imply that if we combine the terms
in 1/(log x)
2 from PJ (a, d, m, x), we obtain a sum that
is independent of a. Heuristically, we might expect this
term to be dominant as x →∞, and therefore indepen-
dence of a should appear for large x. We test this predic-
tion numerically in Section 8.
It would be interesting to have analytical proofs of
any of these symmetries for the ratio N (a, d, m, x)/π(x)
in the limit as x →∞. As stated above, we do not know
whether N (a, d, m, x)/π(x) might be independent of both
a and d in this limit.
We compare the actual values of

X∑

y =x+1 PJ (a, d, m, y)and N (a, d, m, X) − N (a, d, m, x)

for x =10
3, X =10
6, and various small values of a, d,
and m in Section 7. We begin our sum at 10
3, because our
heuristic relies on x being large relative to a, d,and m.
The alternating sums (1–9) become too large for feasible
computation when X gets much beyond 10
6.
For any x, PJ (1, 2, 2,x) should approximate (log x)
−1.
We test this for J = 28 and various x in Section 4.
We also discuss what happens when J varies. We prove
an internal consistency, called “vertical compatibility,” in
Proposition 4.3 and Corollary 4.4. This asserts that if m |
n and J ′ is given, there exists J such that PJ (a, d, m, x)
equals a certain sum of PJ ′(a
′,d′,n,x)’s.
The function PJ appears to stabilize surprisingly
quickly as a function of J. Experimentally, for small val-
ues of x, PJ still appears to remain approximately con-
stant, even when J is much larger than 4 log x. See the
remarks at the end of Section 4. This stabilization as J
varies is somewhat surprising; our heuristic is based on
 a probabilistic picture, whereas, for example, we know
that the next prime after p is certainly less than 2p.It
would be interesting to have a theoretical grasp of how
PJ varies with J.
We could try to eliminate the dependence on J by
looking at
 P (a, d, m, x) := lim
J →∞ PJ (a, d, m, x).

However, we see no way of proving that the limit exists.
The sum deﬁned by the limit is certainly not absolutely
convergent (see Section 4 below). Our heuristic makes
less and less sense if x is ﬁxed and J increases.

2. NOTATION

To simplify the job of the reader, we record all of our
considerable notation at the outset. Fix an integer m> 1
and a positive integer a.Let S be a ﬁnite set of nonneg-
ative numbers containing 0. Let p be aprime.Let x> 2
be an integer. We present a list of some of our notation
in Table 1.
The deﬁnition of np in (1–3) means the number of dis-
tinct residue classes modulo p in the set S. Once p is
larger than the largest element in S,wehave np (S)=
n(S). The product in (1–5) is inﬁnite but converges, be-
cause for p>n, both the numerator and denominator
have leading terms 1 − n
p . The product in (1–6) contains
only ﬁnitely many terms that do not equal 1, because
once p>n and p> max(S), the numerator and denom-
inator are equal.
Below, we will typically think of a as a positive in-
teger. However, a appears only as the ﬁrst argument
in β(a, m, S). In turn, the deﬁnition of β(a, m, S) de-
pends only on a in testing the condition (a + s, m)=1.
Thus, β(a, m, S), Q(a, d, m, x, j), and PJ (a, d, m, x) de-
pend only on the value of a (mod m).

3. THE HEURISTIC

We apply P´olya’s heuristic to the problem of determining
the following probabilities:

1. Given a positive integer d, the probability that
x and x + d are successive primes.

2. Given integers a, d ≥ 1and m ≥ 2, the probabil-
ity that x and x + d are successive primes and
x ≡ a (mod m).Downloaded by [Boston College], [Robert Gross] at 16:07 09 December 2011
Ash et al.: Frequencies of Successive Pairs of Prime Residues 403

n = n(S) = card(S) (1–2)

np = np (S) = card(S mod p) (1–3)
(1 − n
p
 )♮ =
 ⎧
⎨

⎩

1if p ≤ n

1 − n
p otherwise (1–4)

An = ∏

p
 (1 − n
p
 )♮

(1 − 1
p
 )n (1–5)

α(S)= ∏

p
 (1 − np (S)
p
 )

(1 − n(S)
p
 )♮ (1–6)

β(a, m, S)=
 { 1
m ∏p|m p
p−n p (S ) if (a + s, m) = 1 for all s ∈ S

0 otherwise (1–7)

Sk = {0, 1,... ,k} (1–8)

Q(a, d, m, x, j)= ∑

{0,d+jm }⊆S ⊆S d + jm (−1)
n (S )α(S)β(a, m, S) An (S )
(log x)n (S ) (1–9)

PJ (a, d, m, x)=
 J∑

j =0 Q(a, d, m, x, j) (1–10)

TABLE 1. Summary of notation.

3. Given integers a, d ≥ 1and m ≥ 2, the proba-
bility that x is prime, x ≡ a (mod m), and the
next prime is congruent to a + d (mod m).

3.1. The Probability That x and x + d Are Successive
Primes

Let S be a nonempty ﬁnite set of nonnegative integers.
Let p be a prime number. Then for integers x,

Prob(p ∤ x + k for k ∈ S) ∼ p − np
p ,

where np = np (S) is deﬁned in (1–3). Note that 1 ≤ np ≤
p. Furthermore, if np = p, then each residue class modulo
p is represented by some k ∈ S; hence p | x + k for some
k ∈ S,sothatProb(p ∤ x + k for k ∈ S) is indeed 0. Also
np = n := card S as soon as p is suﬃciently large (p larger
than the largest element in S will suﬃce).
In [P´olya 59] a way is proposed to pass from the prob-
ability that “p ∤ x + k for k ∈ S” to the probability that
“x + k is prime for k ∈ S.” P´olya argues that the events
“p ∤ x + k for k ∈ S” for various primes p should be con-
sidered heuristically independent as long as p is small
 compared with x, so that we may conclude that

Prob(p ∤ x + k for k ∈ S for all p<y) ∼ ∏

p< y
 p − np
p

as long as x is suﬃciently larger than y.Now if x>y >
x
1/2, then
 p ∤ x + k for k ∈ S for all p<y
⇐⇒ x + k is prime for k ∈ S,

at least if x is large enough that the size of the elements of
S can be ignored. P´olya proposed that the correct value
of y should be xµ , where µ = e
−γ ,and γ =0.5772 ...
is Euler’s constant. His justiﬁcation for this “trick of the
magic µ” is simply and solely that it works when S = {0}:
indeed, by Mertens’s theorem,
∏

p< x µ
 p − 1
p ∼ 1
log x ,

while the probability that x is prime is also 1
log x ,bythe
prime number theorem. Accordingly we propose

Prob(x + k is prime for each k ∈ S) ∼ ∏

p< x µ
 p − np
p .

(3–1)Downloaded by [Boston College], [Robert Gross] at 16:07 09 December 2011
404 Experimental Mathematics, Vol. 20 (2011), No. 4

We rewrite (3–1) as follows:
∏

p< x µ
 p − np
p

∼ ∏

p≤n
 p − np
p
 ∏

n< p< x µ
 ( p − np
p − n
 (1 − n
p
 ))

∼ ∏

p≤n
 p − np
p
 ∏

n< p< x µ
 p − np
p − n
 ∏

n< p< x µ
 (1 − n
p )

(1 − 1
p )n

× ∏

n< p< x µ
 (1 − 1
p
 )n

∼ ∏

p≤n
 p − np
p
 ∏

n< p< ∞
 p − np
p − n
 ∏

p< x µ
 (1 − n
p )♮

(1 − 1
p )n

× ∏

p< x µ
 (1 − 1
p
 )n . (3–2)

The second product may be viewed as a ﬁnite product,
because np = n for p suﬃciently large.
The ﬁrst two products are α(S), as deﬁned in (1–6).
The third product approaches An , as deﬁned in (1–5).
The fourth product satisﬁes

∏

p< x µ
 (1 − 1
p
 )n ∼ 1
(log x)n

by Mertens’s theorem. Putting all this together gives

Prob(x + k is prime for k ∈ S) ∼ α(S) An
(log x)n . (3–3)

As a check, let d be a positive integer and take S =
{0,d}. We should retrieve the Hardy–Littlewood formula.
In fact,
 A2 = ∏

p
 (1 − 2
p )♮

(1 − 1
p )2 =4 ∏

p> 2
 (1 − 2
p )

(1 − 1
p )2

=4 ∏

p> 2
 (1 − 1
(p − 1)2
 ) ,

and np (S)=1 if p | d, with np (S) = 2 otherwise. Hence,

α({0,d})=
 {
0if d is odd,

1
2 ∏p|d,p> 2 p−1
p−2 if d is even,

which agrees with the formula from
[Hardy and Littlewood 23] quoted in the introduction
(note that our A2 is four times Hardy and Littlewood’s
C2).
Let d be a positive integer. We want to apply the for-
mula (3–3) to ﬁnd the probability that x and x + d are
 successive primes. Let Sd = {0, 1,... ,d}. Then by inclu-
sion/exclusion,

Prob(x is prime and x + d is the next prime)

= ∑

{0,d}⊆S ⊆S d (−1)
n (S )α(S) An (S )
(log x)n (S ) .

3.2. The Probability That x and x + d Are Successive
Primes and x ≡ a (mod m)

We start over with a congruence condition. Let m ≥ 2
and a ≥ 1 be integers. Then

Prob(x ≡ a (modm)) ∼ 1
m .

Suppose that p is a prime divisor of m. Then the con-
gruence x ≡ a mod m determines whether p | x + k for
any k ∈ S. Indeed, if a + k is not relatively prime to m
for some k ∈ S, then

Prob(x ≡ a (mod m)and x + S are primes) = 0.

Here x + S denotes {x + s : s ∈ S}. On the other hand,
if p ∤ m, the conditions “p ∤ x + k for k ∈ S” should be
independent of congruences modulo m (and independent
of each other), heuristically speaking. So if a + k is rela-
tively prime to m for every k ∈ S, then

Prob(x ≡ a (mod m)and x + S are primes)

∼ 1
m
 ∏

p< x µ
p∤m
 p − np
p .

So

Prob(x ≡ a (mod m)and x + S are primes)

∼
 ⎧
⎪⎨

⎪⎩
 1
m ∏

p< x µ p∤m
 p − np
p if (a + k, m)=1 ∀k ∈ S,

0 otherwise.

In the ﬁrst case, when the elements of a + S are all
relatively prime to m,wehave np <p for all p | m,and
therefore
1
m
 ∏

p< x µ
p∤m
 p − np
p = 1
m
 ∏

p|m
 p
p − np
 ∏

p< x µ
 p − np
p

∼ 1
m
 ∏

p|m
 p
p − np α(S) An
(log x)n .

Thus
 Prob(x ≡ a (mod m)and x + S are primes)

∼ β(a, m, S)α(S) An
(log x)n ,Downloaded by [Boston College], [Robert Gross] at 16:07 09 December 2011
Ash et al.: Frequencies of Successive Pairs of Prime Residues 405

where β(a, m, S) is deﬁned in (1–7).
Let d be a positive integer. Then by inclu-
sion/exclusion,

Prob(x is prime, x ≡ a (mod m),
and x + d is the next prime)

∼ ∑

{0,d}⊆S ⊆S d (−1)
n (S )−2Prob(x ≡ a (mod m)

and x + S are primes)

∼ ∑

{0,d}⊆S ⊆S d (−1)
n (S )α(S)β(a, m, S) An (S )
(log x)n (S ) .

= Q(a, d, m, x, 0).

3.3. The Probability That x Is Prime, x ≡ a (mod m),
and the Next Prime Is ≡ a + d (mod m)

Finally, suppose that 1 ≤ d ≤ m and that (a, m)=1 and
(a + d, m) = 1. Then

Prob(x ≡ a (mod m), x prime,
and the next prime is ≡ a + d mod m)

∼ PJ (a, d, m, x)

=
 J∑

j =0
 ∑

S (−1)
n (S )α(S)β(a, m, S) An (S )
(log x)n (S ) ,

where the second sum is over {0,d + jm}⊆ S ⊆ Sd+jm .
One possibility is to let j range from 0 to ∞. However,
there are various ﬁnite upper bounds that can be used.
We need to use a large enough value of J to ensure that
the set x + Sd+jm contains the next prime after x (as-
suming that x is prime). Bertrand’s postulate guaran-
tees that choosing J such that d + Jm ≥ x is suﬃcient.
We can safely use a much smaller value of J, however.
The average gap between primes of size x is log x,and
the standard deviation is also log x.Wecan be almost
certain that x + Sd+jm will contain the next prime if
d + Jm ≥ 4 log x.
It is worth recalling P´olya’s remark in [P´olya 59,
p. 384, footnote]:

When we consider a ﬁxed number of
primes, the “probabilities” introduced
can be regarded as “independent,” but
they cannot be so regarded when the
number of primes increases in an arbi-
trary manner.

Unfortunately, as a practical matter, we are only able
to choose J such that d + Jm is smaller than 55 so that
 J = ⌊(55 − d)/m⌋; otherwise, the number of subsets of
Sd+jm is too large to be computationally feasible. Thus
in computing our heuristic, we need to limit ourselves to
4 log x ≤ 55, or x less than roughly 10
6. We will discuss
this further below.

4. SOME OBSERVATIONS

We observe the following:
 If S contains any odd integers, then α(S)=0, be-
cause n2(S)=2.
 If (a, m) ≡= 1, then β(a, m, S) = 0, because 0 ∈
S. Therefore, we will henceforth assume that
(a, m)=1.
 If {0,d + jm}⊆ S and (a + d, m) ≡= 1, then
β(a, m, S)=0.
 If a ≡ a
′ (mod m), then β(a, m, S)= β(a
′,m,S).
 If β(a, m, S) ≡= 0, then β(a, m, S) is independent
of a.

Proposition 4.1. If m is a power of 2, then α(S)β(a, m, S)
is independent of a.Hence,if m =2
k and a is odd, then
PJ (a, d, m, x) is independent of a.

Proof. Because (a, m) = 1, we know that a is odd. If
S contains any odd elements, then α(S)=0. If S con-
tains only even numbers, then a + S will contain only
odd numbers, and hence will be relatively prime to m,
regardless of the value of a.

It is tempting to rearrange the terms in (1–10) in
order of increasing n(S) and let J →∞. However, the
sum of the terms with n(S) = 2 is divergent. This is
true in general, but it is simplest to see when m =2
k .
In that case, we must have a odd and d even in order
for α(S)β(a, m, S) ≡= 0. The terms with n(S) = 2 all have
the form S = {0,d + jm}. In this situation, we can easily
compute that

β(a, m, S)= ( 1
2k
 )( 2
1
 ) = 1
2k −1 .

On the other hand, α(S) will always be larger than 1
2 ,so
all of the (inﬁnitely many) terms with n(S) = 2 will be
larger than A 2
2k (log x)2 , and hence will diverge.

Proposition 4.2. (“Antidiagonal symmetry.”)

PJ (a, d, m, x)= PJ (−a − d, d, m, x).Downloaded by [Boston College], [Robert Gross] at 16:07 09 December 2011
406 Experimental Mathematics, Vol. 20 (2011), No. 4

Proof. We will show that for each set {0,d + jm}⊆ S ⊂
Sd+jm in the sum in (1–10) for PJ (a, d, m, x), there is a
set {0,d + jm}⊆ S′ ⊆ Sd+jm with n(S)= n(S′), α(S)=
α(S′), and β(a, m, S)= β(−a − d, m, S′).
In particular, set S′ =(d + jm) − S. We automati-
cally have {0,d + jm}⊆ S′ ⊆ Sd+jm . Obviously, n(S)=
n(S′), and for any prime p, np (S)= np (S′). This shows
that α(S)= α(S′).
Finally, suppose that for every element s ∈ S,wehave
(a + s, m)=1, so β(a, m, S) ≡= 0. Then (−a − s, m)=1,
and so (jm − a − s, m) = 1. Therefore, ((d + jm − s)+
(−a − d),m) = 1, showing that β(−a − d, m, S′) ≡=0. We
know that np (S)= np (S′), and therefore if β(a, m, S) ≡=
0, we see that β(a, m, S)= β(−a − d, m, S′). Conversely,
if β(a, m, S) = 0, the same argument shows that β(−a −
d, m, S′) = 0. We may conclude that PJ (a, d, m, x)=
PJ (−a − d, d, m, x).

Proposition 4.3. (“Vertical compatibility.”) Fix J ′.Sup-
pose that n is a positive integer and m | n.Then

PJ (a, d, m, x)= ∑

a ′≡a(m o d m )
d ′≡d(m o d m )
1≤a ′,d ′≤n
 PJ ′(a
′,d′,n,x),

where (J +1)m =(J ′ +1)n.

Proof. We will ﬁrst show that each set Sd+jm used in the
sum on the left-hand side of the equation appears in the
sum on the right-hand side of the equation for a unique d′.
To see this, choose d′ ≡ d + jm (mod n) with 1 ≤ d′ ≤ n.
Write (d + jm) − d′ = j′n, and then d + jm = d′ + j′n.
On the other hand, if we start with d′ ≡ d (mod m)and
j′ ≥ 0, it is clear that we can ﬁnd a unique j such that
d + jm = d′ + j′n. We know that j′ ≤ J ′ and d′ ≤ n +
d − m. Therefore, the upper bound for J is (J ′+1)n −m
m .
This leaves us needing to show that

β(a, m, S)= ∑

a ′≡a (m o d m )
1≤a ′≤n
 β(a
′,n,S).

Notice that if β(a, m, S) = 0, then automatically
β(a
′,n,S) = 0 for all possible values of a
′ ≡ a (mod m).
So we may assume that β(a, m, S) ≡=0.
It suﬃces to consider the case n = qm, with q prime.
Notice that the set {a, a + m, a +2m,...,a +(q − 1)m}
contains the complete set of integers a
′ with a
′ ≡ a
(mod m) and 1 ≤ a
′ ≤ qm. In particular, there are q such
integers a
′.
There are two cases to ﬁnish the proof:
 Case 1: q | m.If a + S contains only elements relatively
prime to m,and a
′ ≡ a (mod m), then a
′ + S contains
only elements relatively prime to m. Hence, a
′ + S con-
tains only elements relatively prime to qm. Therefore,
β(a, m, S)=0 ⇐⇒ β(a
′,qm, S) = 0. Note also that if p
is prime, then p | qm ⇐⇒ p | m.
If β(a
′,qm, S) ≡= 0, then we know that β(a
′,qm, S)is
independent of a
′. There are q possible values of a
′,and
we have
∑

a ′ β(a
′,qm, S)= ∑ ( 1
qm
 ∏

p|qm
 p
p − np (S)
 )

= ∑ ( 1
qm
 ∏

p|m
 p
p − np (S)
 )

= q( 1
qm
 ∏

p|m
 p
p − np (S)
 )

= 1
m
 ∏

p|m
 ( p
p − np (S)
 ) = β(a, m, S).

Case 2: q ∤ m. In this case, the elements of the set
{a, a + m,...,a +(q − 1)m} are distributed over all q of
the residue classes modulo q. Suppose that nq (S)= c.
Then there are q − c possible residue classes r modulo q
such that r + S will be relatively prime to q, and there
are c residue classes such that r + S will have a factor in
common with q (namely r ≡−s (mod q) for some s ∈ S).
Let r′ be one of the residue classes with r′ + S relatively
prime to q. Recall as usual that if β(a, qm, S) ≡= 0, then
it is independent of a.
We have
∑

a ′≡a (m o d m )
1≤a ′≤qm
 β(a
′,qm, S)

=(q − nq (S))β(r′,qm, S)

=(q − nq (S)) 1
qm
 ∏

p|qm
 p
p − np (S)

=(q − nq (S)) 1
qm
 ( q
q − nq (S)
 ) ∏

p|m
 p
p − np (S)

= 1
m
 ∏

p|m
 p
p − np (S) = β(a, m, S).

Corollary 4.4. Choose an even integer m> 2,ﬁx J ′,and
let J = (J ′+1)m −2
2 .Then
∑

1≤a≤m
1≤d≤m
 PJ ′ (a, d, m, x)= PJ (1, 2, 2,x). (4–1)Downloaded by [Boston College], [Robert Gross] at 16:07 09 December 2011
Ash et al.: Frequencies of Successive Pairs of Prime Residues 407

Proof. Proposition 4.3 reduces the left-hand side of (4–1)
to

P (1, 2, 2,x)+ P (1, 1, 2,x)+ P (2, 1, 2,x)+ P (2, 2, 2,x).

The last three terms in this sum are all 0.
Note that if for some reason it is desirable to begin
with odd m, we may replace m with 2m without changing
the sum on the left-hand side of (4–1), again because of
Proposition 4.3.

Theoretically, PJ (1, 2, 2,x) should give the probabil-
ity that x is prime, which according to our heuristic is
(log x)
−1. We can sum only to J = 28, because the com-
putational time involved becomes inordinate, and we tab-
ulate our results here:

x P28 (1, 2, 2,x) (log x)−1 Ratio
10 0.425586 0.434294 0.9799
102 0.217147 0.217147 1.0000
103 0.144765 0.144765 1.0000
104 0.108567 0.108574 0.9999
105 0.0867455 0.0868589 0.9987
106 0.0719549 0.0723824 0.9941

We conjecture that the relatively poor agreement with
prediction when x = 10 is caused by replacing a ﬁnite
product over the range p<x
µ with the inﬁnite product
deﬁning An in the penultimate term of formula (3–2).
The product deﬁning An converges relatively rapidly, but
there is still an appreciable error introduced by includ-
ing so many more terms when x = 10. The fact that
the ratio is slowly tending away from 1 might show
that for x ≥ 10
4, J should be larger than 28 for best
results.
More interestingly, the computations for x =10
2 and
x =10
3 converged relatively rapidly and did not change
signiﬁcantly when more terms were included in the sum.
For x =10
2, the series attained the value 0.217 ... for
J = 13. Extending the sum over larger values of J did not
change the ﬁrst three signiﬁcant digits. The sum took the
value 0.21715 ... at J = 20, and that did not change up
to our maximum value of J = 28. For x =10
3,the sum-
mation takes values varying between 0.144765 ... and
0.144767 ... when J runs from 16 to 28. It is hard to
understand this apparent stabilization of PJ for varying
J; our heuristic makes less and less sense as J increases
for ﬁxed x.
 5. NUMERICAL CHECKS OF ANTIDIAGONAL
SYMMETRY

Take, for example, m = 5. We count residues modulo
5 of consecutive prime pairs p<q with p< 982451653.
(982451653 is the 50 millionth prime number). We then
record our results in a matrix with ϕ(m)rowsand
columns. The results for m =5 are

2289170 3778890 3732547 2698886

3189954 2190360 3386288 3734018

2995506 3535854 2191584 3777311

4024863 2995514 3189838 2289414

where aij records the count of (p ≡ i (mod 5),q ≡ j
(mod 5)). (The pairs (3, 5) and (5, 7) are thus omitted
from the counts in this table.)
To check antidiagonal symmetry, we take the ratio of
each entry to its reﬂection across the antidiagonal. We
obtain (rounded to six places)

0.999893 1.000418 0.999606 1.000000

1.000036 0.999441 1.000000 1.000394

0.999997 1.000000 1.000559 0.999582

1.000000 1.000003 0.999964 1.000107

The entries are all within 0.0006 of 1, while the ratio of
the largest to the smallest entry in the original array is
about 1.84.
If m = 12, we have the following table of counts of
prime pair residues (p mod 12,q mod 12), where p<q
are consecutive primes with p< 982451653; we omit the
pairs (2, 3) and (3, 5) that are not relatively prime to 12:

2265842 3746000 3296656 3190380

2944446 2266005 3994598 3295820

3294707 3190968 2268555 3745878

3993884 3297895 2940299 2268064

For example, the entry 3994598 records the number of
pairs of consecutive primes congruent to (5, 7) (mod 12).
Again, our heuristic predicts that this matrix should
be symmetric across the antidiagonal. Taking the ratio
of each entry to its reﬂection across the antidiagonal, we
obtain (rounded to six places)

0.999020 1.000033 1.000254 1.000000

1.001410 0.998876 1.000000 0.999746

0.999033 1.000000 1.001125 0.999967

1.000000 1.000968 0.998592 1.000981Downloaded by [Boston College], [Robert Gross] at 16:07 09 December 2011
408 Experimental Mathematics, Vol. 20 (2011), No. 4

409015 997313 843077 1082276 749027 721892 804113 642323
643202 408017 995715 843672 1083407 748537 722996 805076
803581 643323 408783 996936 842431 1082780 749737 723085
721382 805281 642633 408177 997195 843473 1081932 749402
750223 721241 804604 642735 407612 997681 843417 1082432
1082176 750074 723110 803572 643435 407018 996935 843628
842474 1082071 751349 721474 804368 643327 408482 996565
996983 843301 1081386 750633 722470 805240 642498 407695

TABLE 2. Residues modulo 16 of consecutive prime pairs p< q with p< 982451653.

The entries are all within 0.002 of 1, while the ratio of
the largest to the smallest entry in the original array is
about 1.76.

6. NUMERICAL CHECKS OF POWER-OF-2
PREDICTION

As noted above, when m =2
k , our heuristic predicts that
N (a, d, 2
k ,x) should be independent of a. Taking m =
16, we count residues modulo 16 of consecutive prime
pairs p<q with p< 982451653, with the result shown in
Table 2.
Our conjecture predicts that the numbers on the “bro-
ken diagonals” parallel to the main diagonal should be
approximately equal. For example, the numbers in bold-
face in the table form a “broken diagonal.” We can test
our conjecture by noting that the counts in the matrix
range from 407018 to 1083407, with a ratio approxi-
mately 2.66, while the counts in the broken diagonal in
boldface range from 842431 to 843672, with a ratio of
1.00147 ... . The next broken diagonal (beginning with
1082276) varies from 1081386 to 1083407, with a ratio
of 1.00186 ... . The remaining broken diagonals exhibit
similar behavior.

7. NUMERICAL CHECKS OF THE HEURISTIC

In Sections 5 and 6, we tested the heuristic indirectly, by
observing symmetries in the heuristic and seeing whether
the same symmetries appeared in the counts of residues
of prime pairs. In this section we compare our heuristic
formula directly with such counts. This requires comput-
ing the heuristic numerically, which, as noted above, be-
comes rapidly unwieldy as J increases, so that we must
restrict J so that d + Jm < 55 in our calculations, and
correspondingly restrict x to be at most 106.
We will use m = 4, 5, 11, and 12 as typical examples.
We count prime pairs reduced modulo m between 103
 and 10
6:
 m =5

3207 6536 6284 3550

5053 2868 5430 6224

4383 5800 2810 6630

6934 4371 5100 3150

m =12

2942 6315 5253 5018

4358 2959 7034 5216

5257 5010 2918 6438

6970 5283 4419 2940

We compute ∑106
x=103 PJ (a, d, m, x) for all possible val-
ues of a and d for each value of m above. Because
of limited computer time, we chose J maximal with
d + Jm < 55. The results are as follows:

m =5

3136.4 6562.3 6237.6 3570.7

5081.4 2738.6 5464.4 6237.6

4360.4 5838.2 2738.6 6562.3

6946.5 4360.4 5081.4 3136.4

m =12

2960.0 6418.9 5258.5 4877.2

4279.9 2960.0 7013.5 5258.5

5258.5 4877.2 2960.0 6418.9

7013.5 5258.5 4279.9 2960.0

To gauge the success of the heuristic in predicting the
counts, we take the ratios of the corresponding entries
in these tables, that is, we calculate, for each congruence
class (i, j) (mod m), the ratio (actual count)/(predictedDownloaded by [Boston College], [Robert Gross] at 16:07 09 December 2011
Ash et al.: Frequencies of Successive Pairs of Prime Residues 409

m =11
263 1071 1242 522 1019 426 1625 617 771 285
819 200 836 1181 485 1106 329 1603 501 765
346 814 217 987 1227 675 1063 324 1555 588
834 328 817 272 834 1221 499 1060 318 1640
682 1015 362 1028 271 1095 1223 663 1049 448
1618 534 775 256 794 275 866 1219 485 1036
382 1826 594 784 253 1004 262 1004 1230 518
1055 366 1599 596 779 387 803 198 867 1208
604 1072 316 1795 577 1004 355 836 192 1062
1238 599 1038 403 1597 665 832 333 845 273

10 6∑

x =1 0 3 PJ (a, d, 11,x)

263.7 1048.5 1242.9 497.9 1029.7 434.8 1642.4 606.3 778.9 257.8
802.7 191.4 851.5 1219.9 486.6 1077.4 313.4 1595.3 488.1 778.9
335.3 823.1 193.7 983.5 1205.5 655.8 1069.6 331.0 1595.3 606.3
801.8 332.3 800.4 237.2 865.3 1250.3 493.8 1069.6 313.4 1642.4
656.4 1000.8 359.0 1018.3 230.0 1117.3 1250.3 655.8 1077.4 434.8
1627.2 560.9 777.0 252.1 780.6 230.0 865.3 1205.5 486.6 1029.7
389.7 1806.0 592.5 805.6 252.1 1018.3 237.2 983.5 1219.9 497.9
1072.6 322.0 1596.1 592.5 777.0 359.0 800.4 193.7 851.5 1242.9
615.4 1103.7 322.0 1806.0 560.9 1000.8 332.3 823.1 191.4 1048.5
1245.0 615.4 1072.6 389.7 1627.2 656.4 801.8 335.3 802.7 263.7

Ratios
1.00 1.02 1.00 1.05 0.99 0.98 0.99 1.02 0.99 1.11
1.02 1.04 0.98 0.97 1.00 1.03 1.05 1.00 1.03 0.98
1.03 0.99 1.12 1.00 1.02 1.03 0.99 0.98 0.97 0.97
1.04 0.99 1.02 1.15 0.96 0.98 1.01 0.99 1.01 1.00
1.04 1.01 1.01 1.01 1.18 0.98 0.98 1.01 0.97 1.03
0.99 0.95 1.00 1.02 1.02 1.20 1.00 1.01 1.00 1.01
0.98 1.01 1.00 0.97 1.00 0.99 1.10 1.02 1.01 1.04
0.98 1.14 1.00 1.01 1.00 1.08 1.00 1.02 1.02 0.97
0.98 0.97 0.98 0.99 1.03 1.00 1.07 1.02 1.00 1.01
0.99 0.97 0.97 1.03 0.98 1.01 1.04 0.99 1.05 1.04

TABLE 3. Actual counts and predicted values for m = 11.

count), with the following results, rounded to two places:

m =5

1.02 1.00 1.01 0.99

0.99 1.05 0.99 1.00

1.01 0.99 1.03 1.01

1.00 1.00 1.00 1.00

m =12

0.99 0.98 1.00 1.03

1.02 1.00 1.00 0.99

1.00 1.03 0.99 1.00

0.99 1.00 1.03 0.99
 By comparison, the ratio of the largest to the smallest
count is 6934/2810 ≈ 2.47 (for m = 5), and 7034/2918 ≈
2.41 (for m = 12).
Here are the results for m = 4, again for the range 10
3

to 10
6:
 m =4: 16574 22521

22520 16715

106
∑

x=103 PJ (a, d, 4,x): 16618.8 22407.7

22407.7 16618.8

ratios: 1.00 1.01

1.01 1.01Downloaded by [Boston College], [Robert Gross] at 16:07 09 December 2011
410 Experimental Mathematics, Vol. 20 (2011), No. 4

Finally, for m = 11, the calculations appear in Ta-
ble 3. The counts for m = 11 vary from 192 to 1826,
with ratio 1826/192 ≈ 9.51. Our predicted values are for
the most part quite close to the observed counts, though
the predictions for a few entries (notably, and curiously,
(3, 3), (4, 4), (5, 5), (6, 6), (7, 7)) are a bit low, only 85%–
90% of their observed counts. This is partly explained by
the size of the entries themselves—the main diagonal en-
tries are the smallest, in both the table of counts and the
table of predictions, so a discrepancy there between pre-
diction and observation shows up as a larger percentage
error than the same discrepancy elsewhere. For example,
the observed count for (5, 5) is 41 above the predicted
count, or 18%; the observed count for (10, 9) is 42 above
predicted, or 5%; the observed count for (2, 4) is 39 below
predicted, or 3%.

8. ANOTHER PREDICTION

If we let x →∞ and ﬁx J, we can view the dominant
terms in PJ (a, d, m, x) as those with n(S) = 2. (In real-
ity, the estimation is more complex, because the value
of J should increase with x.) If n(S) = 2, then S =
{0,d + jm}.Aslongas(a, m)=(a + d, m) = 1, these
“dominant” terms in PJ (a, d, m, x) will be independent
of a.
To see whether in fact this prediction appears to be
true, we compute prime pair counts modulo 5 and 12
for the ﬁrst 10
7 (probable) primes larger than 10
100.The
results are
 m =5

300655 318723 320000 310947

313970 300412 315948 319266

312837 317325 300976 318355

322830 313721 314012 300023

m =12

301604 318324 315239 314667

313320 300633 319515 316479

315294 315144 300873 318316

320319 315883 314055 300335

These data are consistent with prediction: for exam-
ple, for m = d = 5 (respectively m = d = 12), part of
the prediction is that the entries on the main diagonal
should tend to equality; an ad hoc way to judge this is
to take the ratio of the largest to the smallest terms on
the diagonal for both our ﬁrst set of residues, involving
 primes less than 106, and this set. For m = 5 (respec-
tively m = 12), the ratio for the “small-prime” data set
is 1638
1390 ≈ 1.18 (respectively 1501
1430 ≈ 1.05), while for the
“large-prime” data set, the ratio is 300976
300023 ≈ 1.003 (re-
spectively 301604
300335 ≈ 1.004).

9. FURTHER OPEN QUESTIONS

One obvious question is whether the diﬀerent residue
classes of prime pairs occur asymptotically equally often:
in other words, given any a, d, a
′,d′ with a, a + d, a
′,a
′ +
d′ relatively prime to m,dowehave

N (a, d, m, x)
N (a′,d′,m,x) → 1

as x →∞?
This corresponds to asking whether all of the entries in
the matrices in the previous section are tending toward
equality as x tends to inﬁnity. One way to gauge the
variation in our tables is to take the ratio of the largest
to the smallest counts. In Section 7, the ratio for m =
5 is approximately 2.47 (respectively 2.39 for m = 12),
while for the “large prime” data set in Section 8, the
ratio for m = 5 is approximately 1.08 (respectively 1.07).
Obviously, the terms appear to be getting closer together,
but of course we cannot tell whether they are tending
toward a limiting ratio of 1.
If the diﬀerent residue classes of prime pairs do oc-
cur asymptotically equally often, we are in a “prime
race” situation, as studied in [Rubinstein and Sarnak 94]
and [Granville and Martin 06]. For example, take m =
4 and count prime pairs congruent to (1, 1) (mod 4)
versus prime pairs congruent to (1, 3) (mod 4). Even
if the counts are asymptotically equal, i.e., if
limx→∞ N (1, 4, 4,x)/N (1, 2, 4,x) = 1, we observe for ﬁ-
nite chunks of primes a decided tendency for the total
of (1, 3)’s to exceed the total of (1, 1)’s. We can keep
score, as we search through the sequence of odd primes
3, 5, 7,... , and see when the (1, 1)’s are ahead of the
(1, 3)’s and when the opposite holds. It seems quite possi-
ble that N (1, 4, 4,x) >N (1, 2, 4,x) for almost all values
of x.
Another question concerns the appropriate value of
J to use in our heuristic. The computation mentioned
at the end of Section 4 shows that in at least one case,
PJ (a, d, m, x) is nearly independent of J for a range of
values of J. A precise understanding of the dependence
of PJ (a, d, m, x)on J would go a long way toward estab-
lishing the solidity of our heuristic.Downloaded by [Boston College], [Robert Gross] at 16:07 09 December 2011
Ash et al.: Frequencies of Successive Pairs of Prime Residues 411

ACKNOWLEDGMENTS

We thank Jenny Baglivo and K. Soundarajan for their help,
and the referee for helpful comments. The ﬁrst and second
authors thank the National Science Foundation for partial
funding of this research under grant DMS-0455240.

REFERENCES

[Ash et al. 09] A. Ash, B. Bate, and R. Gross. “Frequencies
of Successful Tuples of Frobenius Classes.” Experiment.
Math. 18 (2009), 55–63.

[Bateman and Horn 62] Paul T. Bateman and Roger A. Horn.
“A Heuristic Asymptotic Formula Concerning the Dis-
tribution of Prime Numbers.” Math. Comp. 16 (1962),
363–367.
 [Granville and Martin 06] Andrew Granville and Greg Mar-
tin. “Prime Number Races.” Amer. Math. Monthly 113
(2006), 1–33.

[Hardy and Littlewood 23] G. H. Hardy and J. E. Littlewood.
“Some Problems of Partitio Numerorum III: On the Ex-
pression of a Number as a Sum of Primes.” Acta Math.
44 (1923), 1–70.

[P´olya 59] G, P´olya. “Heuristic Reasoning in the The-
ory of Numbers.” Amer. Math. Monthly 66 (1959),
375–384.

[Rubinstein and Sarnak 94] Michael Rubinstein and Peter
Sarnak. “Chebyshev’s Bias.” Experiment. Math. 3 (1994),
173–197.

Avner Ash, Department of Mathematics, Boston College, Chestnut Hill, MA 02467-3806, USA (ashav@bc.edu)

Laura Beltis, Actuarial Analysis Department, Tufts Health Plan, Watertown, MA 02472, USA (lbeltis@gmail.com)

Robert Gross, Department of Mathematics, Boston College, Chestnut Hill, MA 02467-3806, USA (gross@bc.edu)

Warren Sinnott, Department of Mathematics, The Ohio State University, Columbus, OH 43210-1174, USA
(sinnott@math.ohio-state.edu)

Received February 2, 2010; accepted May 11, 2010.Downloaded by [Boston College], [Robert Gross] at 16:07 09 December 2011
