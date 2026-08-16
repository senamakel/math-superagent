<!-- source: https://arxiv.org/pdf/0710.0823 | converted from PDF -->

arXiv:0710.0823v1  [math.NT]  3 Oct 2007
THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY

BEN GREEN

Abstract. We discuss, in varying degrees of detail, three contemporary themes in
prime number theory. Topic 1: the work of Goldston, Pintz and Yıldırım on short
gaps between primes. Topic 2: the work of Mauduit and Rivat, establishing that 50%
of the primes have odd digit sum in base 2. Topic 3: work of Tao and the author on
linear equations in primes.

Introduction. These notes are to accompany two lectures I am scheduled to give at
the Current Developments in Mathematics conference at Harvard in November 2007.
The title of those lectures is ‘A good new millennium for primes’, but I have chosen
a rather drier title for these notes for two reasons. Firstly, the title of the lectures
was unashamedly stolen (albeit with permission) from Andrew Granville’s entertaining
article [16] of the same name. Secondly, and more seriously, I do not wish to claim that
the topics chosen here represent a complete survey of developments in prime number
theory since 2000 or even a selection of the most important ones. Indeed there are
certainly omissions, such as the lack of any discussion of the polynomial-time primality
test [2], the failure to even mention the recent work on primes in orbits by Bourgain,
Gamburd and Sarnak, and many others.

I propose to discuss the following three topics, in greatly varying degrees of depth.
Suggestions for further reading will be provided. The three sections may be read inde-
pendently although there are links between them.

1. Gaps between primes. Let pn be the nth prime number, thus p1 = 2, p2 = 3, and so
on. The prime number theorem, conjectured by Gauss and proven by Hadamard and
de la Vall´ee Poussin over 110 years ago, tells us that pn is asymptotic to n log n, or in
other words that
 lim
n→∞ pn
n log n = 1.

This implies that the gap between the nth and (n + 1)st primes, pn+1 − pn, is about
log n on average. About 2 years ago Goldston, Pintz and Yıldırım proved the following
remarkable result: for any ǫ > 0, there are inﬁnitely many n such that pn+1−pn < ǫ log n.
That is, inﬁnitely often there are consecutive primes whose spacing is much closer than
the average.

2. Digits of primes. Written in binary, the ﬁrst few primes are

10, 11, 101, 111, 1011, 1101, 10001, 10011, 10111, . . .
1

2 BEN GREEN

There is no obvious pattern
1. Indeed, why would there be, since the deﬁnition of ‘prime’
has nothing to do with digital expansions. Proving such a statement, or even formulating
it correctly, is an entirely diﬀerent matter. A couple of years ago, however, Mauduit
and Rivat did manage to prove that the digit sum is odd 50% of the time (and hence
even 50% of the time). They also obtained results in other bases.

3. Patterns of primes. Additive questions concerning primes have a long history. It
has been known for over 70 years that there are inﬁnitely many 3-term arithmetic
progressions of primes such as 3, 5, 7 and 5, 11, 17, and that every large odd number is
the sum of three primes. Recently, in joint work with Tao, we have been able to study
more complicated patterns of primes. In this section we provide a guide to this recent
joint work.

Throughout these notes we will write

Ex∈Xf (x) := 1
X
 ∑

x∈X f (x),

where X is any ﬁnite set and f : X → C is a function.

1. Gaps between primes

These notes were originally prepared for a series of lectures I gave at the Norwegian
Mathematical Society’s Ski og mathematikk, which took place at Rondablikk in January
2006. It is a pleasure to thank Christian Skau for inviting me to that event. The
argument of Goldston, Pintz and Yıldırım was ﬁrst described to me by K. Soundararajan
at the Highbury Vaults in Bristol. It is a pleasure to thank him, and to refer the
interested reader to his lectures on the subject [41], which are superior to these in every
respect.

1.1. The result. In 2005 Goldston, Pintz and Yıldırım created a sensation by an-
nouncing a proof that
 liminfn→∞ pn+1 − pn
log n = 0,

where pn denotes the nth prime number. According to the prime number theorem we
have pn ∼ n log n,

and therefore pn+1 − pn
log n
has average value 1. The Goldston, Pintz and Yıldırım result thus states that the
distance between consecutive primes can be ǫ of the average spacing, for any ǫ, and is
thus certainly most spectacular.

1Except, of course, that the last digit of primes except the ﬁrst is always 1.

THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 3

Previous eﬀorts at locating small gaps between primes focussed on proving successively
smaller upper bounds for C := liminfn→∞ pn+1−pn
log n . The following table describing the
history of these improvements does not make the Goldston-Pintz-Yıldırım result look
any less striking:
 C
Trivial from PNT 1
Hardy-Littlewood [27] 1926 2/3 on GRH
Rankin [39] 3/5 on GRH
Erd˝os [8] 1940 1 - c unconditionally
Ricci [40] 1954 15/16
Bombieri-Davenport [4] 1965 0.4665 . . .
Pilt’ai [38] 1972 0.4571 . . .
Uchiyama [47] 0.4542 . . .
Huxley [29, 30, 31] 1984 0.4393 . . .
Maier [35] 1989 0.2484 . . .
Goldston-Pintz-Yıldırım 2005 0

For the detailed proof of this result we refer the reader to the authors’ paper [13], as
well as to their expository account [12] and to their short article with Motohashi [14].
Our aim here is to give a very rough outline of the proof. One distinctive feature of
the argument is that it ‘only just’ works, in a way that seems rather miraculous. We
will endeavour to give some sense of this. We begin with two sections of background
material.

1.2. The Elliott-Halberstam Conjecture and level of distribution. Let
q be a positive integer and suppose that a is prime to q. We write

ψ(N; a, q) := En⩽N,n≡a(mod q)Λ(n),

where Λ is the von Mangoldt function. For constant q (and in fact for q growing slowly
with N, say q ⩽ (log N)A for some ﬁxed A) the prime number theorem in arithmetic
progressions tells us that
 ψ(N; a, q) ∼ 1/φ(q).

Conditional upon the GRH, we may assert the same result up to about q ≈ N 1/2. The
remarkable theorem of Bombieri-Vinogradov (a proof of which the reader will ﬁnd in
many texts on analytic number theory, such as [32]) states that something like this is
true unconditionally, provided one is prepared to average over q. A weak version of the
theorem is that ∑

q⩽Q max
(a,q)=1 |ψ(N; a, q) − 1
φ(q)| ≪A,ǫ 1
(log N)A (1.1)

for any ﬁxed A and for any Q ⩽ N 1/2−ǫ.

4 BEN GREEN

By using sieve theory one may show that ψ(N; a, q) ≪ N/φ(q), and so the LHS of (1.1)
is trivially bounded by ∑

q⩽Q
 1
φ(q) ≈ log Q.

The Bombieri-Vinogradov theorem permits us to save an arbitrary power of a logarithm
over this trivial bound.

Even conjectures on L-functions (such as the GRH) appear to tell us nothing about
the expression (1.1) when Q ≫ N 1/2. Nonetheless, one may make conjectures. If
θ ∈ [1/2, 1) is a parameter then we say that the primes have level of distribution θ, or
that the Elliott-Halberstam conjecture EH(θ) holds, if we have the bound

∑

q⩽Q max
(a,q)=1 |ψ(N; a, q) − 1
φ(q)| ≪A,θ 1
(log N)A (1.2)

for any Q ⩽ N θ.

The full Elliott-Halberstam conjecture [7] is that EH(θ) holds for all θ < 1. Assuming
any Elliott-Halberstam conjecture EH(θ) with θ > 1/2, Goldston, Pintz and Yıldırım
can prove the remarkable result that gaps between consecutive primes are inﬁnitely
often less than some absolute constant C(θ). Assuming EH(0.95971), they prove that

liminfn→∞(pn+1 − pn) ⩽ 16

(actually they prove a slightly weaker result – the value 0.95971 comes from unpublished
computations of J. Brian Conrey).

It should be stressed however that it is not expected that any conjecture EH(θ) for
θ > 1/2 will be established in the near future. There are results of Bombieri, Friedlander
and Iwaniec which go a little beyond the Bombieri-Vinogradov theorem in something
resembling the required manner, although experts seem to be of the opinion that these
results will not help to improve the bounds on gaps between primes (cf. [1, §16]).

1.3. Selberg’s weights. This is the second section of background material.

In the 1940s Selberg introduced a wonderfully simple, yet powerful, idea to analytic
number theory. Write 1P for the characteristic function of the primes. Then if R is any
parameter and if (λd)d⩽R is an sequence with λ1 = 1, we have the pointwise inequality

1P (n) ⩽ ( ∑

d|n
d⩽R
 λd)2

provided that n > R (the proof is obvious).

This provides an enormous family of majorants for the sequence of primes. In a typical
application we will be interested in something like the set of primes p less than some
cutoﬀ N, and then R will be some power N γ, γ < 1. In this situation Selberg’s weights

THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 5

majorise the primes between N γ and N, that is to say almost all of the primes less than
N.

What weights λd should one choose? This depends on the application, but a very basic
application is to the estimation of 1
y (π(x + y) − π(x)), the density of primes in the
interval (x, x + y] (the Brun-Titchmarsh problem). In discussing this problem we will
also see why it is advantageous to construct a majorant for the primes, rather than work
with 1P itself.

For any choice of weights λd, then, we have
1
y (π(x + y) − π(x)) ⩽ Ex+1⩽n⩽x+y( ∑

d|n
d⩽R
 λd)2

= ∑

d⩽R
 ∑

d′⩽R λdλ′
dEx+1⩽n⩽x+y1d|n1d′|n

= ∑

d⩽R
 ∑

d′⩽R
 λdλd′
[d, d′] + O( 1
y
 ∑

d⩽R
 ∑

d′⩽R |λd||λd′|)
. (1.3)

Let us imagine that the weights λd are chosen to be ≪ yǫ in absolute value (this is always
the case in practice). Then the second term here is O(R2y2ǫ−1). If R ⩽ y1/2−2ǫ then
this is O(y−ǫ) and may be thought of as an error term. This is why it is advantageous
(indeed essential) to work with a majorant taken over a truncated range of divisors, and
not with 1P itself.

The ﬁrst term in (1.3), ∑

d⩽R
 ∑

d′⩽R
 λdλd′
[d, d′] ,

is a quadratic form. It may be explicitly minimised subject to the condition λ1 = 1,
giving optimal weights λOPT
d which are independent of x and y, and the resultant
expression may then be evaluated asymptotically. In this way one obtains the well-
known bound 1
y (π(x + y) − π(x)) ⩽ (2 + ǫ) π(y)
y ,

valid for y > y0(ǫ).

What is the optimal choice of weights λSEL
d for the Brun-Titchmarsh problem? The
precise form will not concern us here (see, for example, [37]). However, it may be shown
that
 λSEL
d ≈ µ(d) log(R/d)
log R .

(For a detailed discussion, see the appendix to [20] and the references to work of Ramar´e
therein.)

We write
 λGY
d := µ(d) log(R/d)
log R .

6 BEN GREEN

These weights are very natural for two reasons: their simplicity of form, and the fact
that they approximate the optimal weights for the Brun-Titchmarsh problem. There is
a third reason for considering them, which comes upon recalling the formula

Λ(n) = ∑

d|n µ(d) log(n/d).

We see, then, that ΛR(n) := ∑

d|n
d⩽R
 µ(d) log(R/d)

is a kind of divisor-truncated version of Λ.

We have arrived at the conclusion that the function
1
(log R)2 Λ2
R(n) = ( ∑

d|n
d⩽R
 λGY
d )2

might be a very useful majorant for the primes.

What might we hope to do with such a majorant? By the computation leading to (1.3),
we see that it is possible to ﬁnd an asymptotic for

EN ⩽n<2N ΛR(n)2 (1.4)

provided that R ⩽ N 1/2−ǫ. Later on we will wish to consider more complicated expres-
sions involving genuine primes, such as

EN ⩽n<2N Λ′(n + 2)ΛR(n)2. (1.5)

Here we write Λ′ for the von Mangoldt function restricted to primes (as opposed to
prime powers), thus
 Λ′(n) := { log n if n is prime
0 otherwise.
The problem of evaluating (1.4) may be thought of as a kind of approximation to the
twin prime problem, though we do not know of a way to relate this expression to that
problem rigourously. Expanding out, we see that (1.5) is equal to
∑

d⩽R
 ∑

d′⩽R µ(d)µ(d′) log(R/d) log(R/d′)EN ⩽n<2N
[d,d′]|n Λ(n + 2).

Now we expect that
 EN ⩽n<2N
[d,d′]|n Λ′(n + 2) ≈ 1
φ([d, d′]) (1.6)

if both d and d′ are odd.

The Bombieri-Vinogradov theorem clearly oﬀers a chance of obtaining a statement to
this eﬀect on average over d, d′ ⩽ R if R ⩽ N 1/4−ǫ, though there is certainly still work
to be done as the distribution of [d, d′] as d, d′ range over d, d′ ⩽ R is not particularly
uniform. For the details (which involve moment estimates for divisor functions) see [13,
§9].
 THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 7

Once this is done we are left with the main term
∑

d⩽R
d odd
 ∑

d′⩽R
d′ odd
 µ(d)µ(d′)
φ([d, d′]) log(R/d) log(R/d′). (1.7)

This term (and related expressions) may all be estimated rather accurately using the
standard Dirichlet series techniques of analytic number theory, whereby the sums are
expressed as integrals involving products of ζ-functions.

If we had EH(θ), that is to say if the primes had level of distribution θ, one could
show that (1.5) is roughly (1.7) in the wider range R ⩽ N θ/2−ǫ. In particular on the
full Elliott-Halberstam conjecture one could work in the range R ⩽ N 1/2‘−ǫ, which is
essentially the same as for (1.4).

Perhaps we should make a few remarks about the form of the asymptotic for (1.7). One
may in fact show that it is
 ∼ log R ∏

p⩾3
 (1 − 1
(p − 1)2 ).

We will see products such as this again in §3.

1.4. A strategy for gaps between primes. We now trun to a discussion of the
results of Goldston, Pintz and Yıldırım themselves. From the conceptual viewpoint it
is easiest to begin by discussing the very strong conditional results proved under the
assumption of the Elliott-Halberstam conjecture. We stated in the introduction that
they prove liminfn→∞(pn+1 − pn) ⩽ 16 (1.8)
assuming EH(θ) for some θ less than 1.

In fact, a much more general result is obtained. Let H = {h1, . . . , hk} be a k-tuple of
distinct integers with h1 < h2 < · · · < hk. A generalisation of the twin prime conjecture
is that there are inﬁnitely many n such that all of n + h1, . . . , n + hk are prime unless
this is “obviously impossible for trivial reasons”, which would be the case if there is
some p such that {h1, . . . , hk} occupy all residue classes (mod p). If this is not the case
then we say that H is admissible.

Goldston, Pintz and Yıldırım prove the following.

Theorem 1.4.1. Suppose that EH(θ) is known for some θ > 1/2. Then there is k0(θ)
with the following property. If k ⩾ k0(θ) and if H = {h1, . . . , hk} is an admissible
k-tuple then for inﬁnitely many n at least two of the numbers n + h1, . . . , n + hk are
prime.

Note in particular that

liminfn→∞(pn+1 − pn) ⩽ min
{h1,...,hk} admissible
k⩾k0(θ) (hk − h1).

8 BEN GREEN

It turns out that k0(θ) can be taken to be 6 for θ > 0.95971, and this leads to (1.8)
since the 6-tuple {0, 4, 6, 10, 12, 16} is admissible.

Here is a very general strategy for detecting primes in admissible tuples. According
to [12], this has its origins in work of Selberg and Heath-Brown. Fix a range [N, 2N),
suppose that 0 ⩽ h1 < · · · < hk ⩽ N, and let (µn)N ⩽n<2N be arbitrary non-negative
weights which are certainly allowed to depend on the hi. We will compare

Q1 := EN ⩽n<2N µn
with Q
(i)
2 := 1
log 3N EN ⩽n<2N Λ′(n + hi)µn,

for i = 1, . . . , k. T. Tao remarked to me that a nice way to think of this as follows:
one may renormalise so that ∑ µn = 1, and then ρ
(i) := Q
(i)
2 /Q1 is essentially the
probability that n + hi is prime if n is drawn at random from the distribution µ (one
might then write the expected values in the deﬁnitions of Q1 and Q
(i)
2 as integrals with
respect to µ).

Now if one can choose the weights µ so that ρ
(i) > 1/k, we will have upon summing
over i = 1, . . . , k that
 EN ⩽n<2N ( k∑

i=1
 Λ′(n + hi)
log 3N − 1)µn > 0,

which means that there is some n such that

Λ′(n + h1) + · · · + Λ′(n + hk) > log 3N.

For such an n, at least two of n+ h1, . . . , n+ hk are prime. In the probabilistic language,
we have essentially used the fact that if n + h1, . . . , n + hk are each drawn at random
from µ, the expected number of primes amongst these numbers is > 1.

1.5. Choosing good weights. We continue the discussion of the previous section.
How should the weights µn be chosen to optimise the factors ρ
(i)? In retrospect, one
may view most of the earlier developments on gaps between primes as attempts to ﬁnd
good weights µn in this context – see [13, §4] for further remarks on this.

A very good choice of weights might be

µn := Λ′(n + h1) . . . Λ′(n + hk).

One would indeed expect that ρ
(i) ≈ 1 in this case. The only problem is that we have
no idea how to prove this, one particular issue being that we cannot show that Q1 ̸= 0
(indeed, this is equivalent to ﬁnding n such that all of n + h1, . . . , n + hk are prime).

We must restrict ourselves to weights µn for which it is possible to estimate Q1 and
Q
(i)
2 . As we saw in §1.3, there is a rather large class of such weights. In fact if

µn = ( ∑

d|n
d⩽R
 λd)2

THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 9

then our chances are good if R ⩽ N θ/2−ǫ, where θ is the best exponent for which we
know EH(θ). Crucially, there is a rather more general class of weights one is able to
consider, and that is weights of the form

µn = ( ∑

d|F (n)
d⩽R
 λd)2, (1.9)

where F (n) = (n + a1) . . . (n + am) is an integer polynomial. It is an interesting exercise
to reprise the arguments of §1.3 in this more general context. In place of the trivial
estimate En⩽N,[d,d′]|n1 = 1
[d, d′] + O(1)

which we used to derive (1.3) one must instead input information about

En⩽N,[d,d′]|F (n)1.

But one knows that (for example) p|F (n) precisely if n ≡ −aj(mod p) for some j ∈
{1, . . . , m}, and so such a task is not too frightening. The same is true of sums, such
as (1.6), which involve the von Mangoldt function.

For the remainder of the discussion we will narrow down our search for good weights
µn to those having the form (1.9). We will assume that for any sensible choice of F
and the λd we may evaluate Q1 and Q
(i)
2 for R ⩽ N θ/2−ǫ using the standard techniques
which we sketched in §1.3.

Now we remarked that an ideal choice of weights is

µn = Λ′(n + h1) . . . Λ′(n + hk),

but we cannot compute with this choice. A closely related choice of weights is

µn = Λk(
(n + h1) . . . (n + hk)).

Here the function Λk is deﬁned by

Λk(n) := ∑

d|n µ(d) log(n/d)k,

and so in particular Λ1 = Λ. For general k the function Λk is supported on those integers
with at most k distinct prime factors. (One way to check this is to use the identity

Λk = LΛk−1 + Λ ∗ Λk−1,

where L(n) := log n and ∗ denotes Dirichlet convolution.)

Now in §1.3 we saw the advantages of replacing Λ with ΛR, a divisor-truncated version
of it. By analogy one might consider

Λk,R(n) := ∑

d|n
d⩽R
 µ(d) log(R/d)k.

This could be negative, but its square Λ2
k,R certainly cannot. Furthermore

µn := Λ2
k,R((n + h1) . . . (n + hk))

10 BEN GREEN

is of the form (1.9) (with F (n) = (n + h1) . . . (n + hk)). This, then, is a very natural
choice of the weights µn and it is with some anticipation that we await the results of
computing Q1 and the Q
(i)
2 , and hence the factors ρ
(i). What we obtain is this:

ρ
(i) ∼ 2
k + 1 · log R
log N .

This is something of a disappointment, since it is not greater than 1/k even when
R = N θ/2−ǫ for θ very close to 1 (that is, with a very strong form of the Elliott-
Halberstam conjecture).

Astonishingly, a seemingly small change tips the balance in our favour. We consider
instead µn := Λ2
k+l,R((n + h1) . . . (n + hk)),

where 0 < l ≪ k is a further parameter. In the probabilistic language, ρ
(i) may then be
thought of (very roughly) as something like the probability that n + hi is prime given
that (n + h1) . . . (n + hk) has at most k + l prime factors.

With this choice of weights it is possible to compute that

ρ
(i) ∼ 2k
k + 2l + 1 2l + 1
l + 1 · log R
log N . (1.10)

Note that as k, l → ∞ with l = o(k), this is essentially 4 log R/k log N. In particular
with R := N θ/2−ǫ one has ρ
(i) > 1/k for k ⩾ k0(θ), for any θ > 1/2. This is enough to
establish Theorem 1.4.1.

1.6. The unconditional result. In this section we explain some aspects of the
proof that
 liminfn→∞ pn+1 − pn
log n = 0.

Recall that in the last section we chose weights

µn := Λ2
k+l,R((n + h1) . . . (n + hk)).

Taking R := N 1/4−ǫ, the quantities Q1 and Q
(i)
2 can be evaluated using the Bombieri-
Vinogradov theorem (rather than the Elliott-Halberstam conjecture). If k, l are large
with l ≪ k then (from (1.10)) the quantities ρ
(i) are all at least 1/k − ǫ
′ for k ⩾ k1(ǫ),
and hence we have that

EN ⩽n<2N ( k∑

i=1
 Λ′(n + hi)
log 3N )
µn ⩾ (1 − δ)∥µ∥1, (1.11)

for any δ > 0, and any k ⩾ k2(δ). Here

∥µ∥1 := EN ⩽n<2N µn

is the total mass of µ. This means that if n is drawn at random from the distribution µ,
then the expected number of primes amongst the numbers n + h1, . . . n + hk is at least
1 − δ. Clearly, this is not an immediately applicable result if one wishes to obtain two
or more primes in the tuple {n + h1, . . . , n + hk}.

THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 11

There is, however, a tiny bit of further information available to us. Even if h0 /∈
{h1, . . . , hk}, there is still a chance that if n is drawn at random from µ then n + h0 will
be prime. One can work out that this probability is asymptotically

S(h0, h1, . . . , hk)
log N ,

where S(h0, h1, . . . , hk) is a certain singular series reﬂecting the arithmetic properties
of the numbers h0, h1, . . . , hk (it is similar in form to the product deﬁning the twin prime
constant). Formally what we mean by this is that

EN ⩽n<2N Λ′(n + h0)
log 3N µn ∼ S(h0, h1, . . . , hk)
log N ∥µ∥1,

and this may once again be rigorously established using the Bombieri-Vinogradov the-
orem.

Let η > 0 be arbitrary. Summing over all h0 with

0 ⩽ h0 ⩽ η log N,

we obtain from (1.11) that

EN ⩽n<2N ( η log N∑

h=0
 Λ′(n + h)
log 3N )µn ⩾ (
1 − δ +
 η log N∑

h0=0
h0 /∈{h1,...,hk}
 S(h0, h1, . . . , hk)
log N
 )
∥µ∥1. (1.12)

For a typical choice of h1, . . . , hk, the right-hand side will be of a predictable size. Indeed
by a result of Gallagher one may infer that
∑

h0,...,hk⩽H
hi distinct
 S(h0, h1, . . . , hk) ∼ H k+1

as H → ∞. Taking expectations over all k-tuples {h1, . . . , hk} of distinct integers with
0 ⩽ hi ⩽ η log N, we therefore obtain from (1.12) that

EN ⩽n⩽2N ( η log N∑

h=0
 Λ′(n + h)
log 3N )µn ⩾ (1 − δ + η − o(1))∥µ∥1.

Recall that this is valid for any δ > 0, provided that k is suﬃciently large. Taking
δ = η/2, we therefore see that (if n is drawn at random from µ) the expected number
of primes in the interval [n, n + η log N] is strictly greater than 1. In particular there is
some such interval containing at least two primes.

1.7. Further results. Since the original paper of Goldston, Pintz and Yıldırım sev-
eral further works have appeared or are scheduled to appear giving reﬁnements and
variants of the main theorem. Here is a summary of what has been done:

• In the forthcoming paper [10] it is shown, by reﬁning the ideas just described
as far as seems possible, that

lim inf
n→∞ pn+1 − pn
(log pn)1/2(log log pn)2 < ∞.

12 BEN GREEN

This remarkable result asserts that the gap between primes is inﬁnitely often
almost as small as the square root of the average gap.
• Let q1 < q2 < . . . be the numbers which are the product of exactly two distinct
primes. Then lim inf
n→∞ (qn+1 − qn) ⩽ 26,

and in fact lim inf
n→∞ (qn+1 − qn) ⩽ 6

if one assumes the Elliott-Halberstam conjecture. These results are obtained in
the paper [11] by the three authors and S. W. Graham.
• In the original paper [13] one also ﬁnds results concerning several primes bunch-
ing together. Thus assuming EH(θ) one has, for any r ⩾ 2, the bound

lim inf
n→∞ pn+r − pn
log pn ⩽ (√r − √2θ)2.

One rather curious feature of this bound is that the full Elliott-Halberstam
conjecture EH(1) implies that

lim inf
n→∞ pn+2 − pn
log pn = 0.

Nothing of this sort is known for pn+3 − pn, even conditionally.

2. Binary digits of primes

These notes originated from a course I lectured in Part III of the Mathematical Tripos
at Cambridge University in the Lent Term 2007. My aim was to work through the
result of Mauduit and Rivat in the case of binary expansions of primes, and to produce
a reasonably short exposition (the original paper is 49 pages long). Because we provide
complete details this section is considerably more technical than either §1 or §3. Readers
not interested in these technicalities may still wish to read §2.3.

2.1. Statement of results. In a recent preprint [36], Mauduit and Rivat proved
that asymptotically 50% of the primes have odd digit sum in base 2 (and hence, of
course, 50% of the primes have even digit sum in base 2 as well!), answering a long-
standing question of Gelfond. Our aim in this section is to give a self-contained proof
of their theorem in the following form, which is easily seen to imply the result as just
stated.

Theorem 2.1.1 (Mauduit-Rivat). Let Λ be the von-Mangoldt function, and let s : N →
N be the function which sums the binary digits of n. Then

En⩽XΛ(n)(−1)s(n) = O(X −δ)

for some δ > 0.

In fact Mauduit and Rivat proved rather more than this: they counted primes whose
digit sum in base q is congruent to a(mod m), for any natural numbers a, q, m. To prove

THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 13

a result in this generality requires some extra technical devices and a lot more notation,
so we leave the interested reader to consult the original paper [36].

I ﬁnd the result intrinsically interesting, but another reason for studying it is that it
represents a pleasingly self-contained example of Vinogradov’s method of ‘Type I and
II sums’ or ‘bilinear forms’ for handling prime number sums.

In contrast with the last chapter we provide a fairly complete technical discussion.

2.2. Some notation. Throughout this section X will be thought of as a large pa-
rameter. If Y1 and Y2 are two quantities which depend on X we write Y1 ⪆ Y2 if
Y1 ≫ǫ X −ǫY2 for all ǫ > 0. We use the notation Y1 ⪅ Y2 similarly. Typically we might
have Y1 ≫ Y2 log−C X for some C, but the notation is occasionally applied in even
looser situations. For example we have the bound τ (x) ⪅ 1 uniformly in x ⩽ X, where
τ (x) denotes the number of divisors of x.

If n ∈ N we write ν2(n) for the 2-exponent of n, the maximal r such that 2r|n.

The letter c will always denote a small, positive, absolute constant. Diﬀerent instances
of the letter will not necessarily denote the same constant.

2.3. Vinogradov’s method of Type I/II sums. Suppose that f : N → C is a
function, bounded by 1. This section concerns a method which can be often be used to
show that a sum of the form
 En⩽X Λ(n)f (n)

is substantially smaller than X. The method is particularly inclined to work when f is
“far” from being multiplicative. It is clear that such a sum cannot be small in many
cases when f does have some multiplicative tendancies, for example when f (n) = µ(n)
or when f (n) is a Dirichlet character to small modulus.

We will develop a develop a form of the method which includes some technical reﬁne-
ments particularly suited to the study of the function f (n) = (−1)s(n). These are rather
insubstantial and consist in large part of ensuring that various cutoﬀs are exact powers
of two. In these notes we will endow the ∼ symbol with a rather speciﬁc meaning: if we
write ∑

n∼2ν then we understand that the variable n is to range over the dyadic interval
[2ν−1, 2ν).

Here is the version of Vinogradov’s method that we shall require.

Proposition 2.3.1 (Method of Type I/II sums). Suppose that f : N → C is a function
with |f (n)| ⩽ 1 for all n. Let δ ∈ (0, 1] be a parameter. We say that Type I sums are
δ-small if 1
X
 ∑

m∼2µ | ∑

n∈Im f (mn)| ⩽ δ

14 BEN GREEN

whenever 2µ ⩽ X 1/100, Im ⊆ [2ν−1, 2ν) is an interval and 2µ+ν ⩽ X. We say that Type
II sums are δ-small if 1
X
 ∣
∣ ∑

m∼2µ
 ∑

n∼2ν ambnf (mn)∣
∣ ⩽ δ

uniformly for all sequences (am), (bn) with |am|, |bn| ⩽ 1 and for all µ, ν such that
X 1/100 ⩽ 2µ, 2ν ⩽ X 99/100. Suppose that f is a function for which Type I and Type II
sums are δ-small. Then
 En⩽X Λ(n)f (n) ≪ δ1/2 logC X.

Remarks. One can take C = 11/2. Note that both Type I and Type II sums are
trivially bounded by X. The important feature of the proposition, then, is that a big
enough gain over these trivial bounds leads to an improvement of the trivial bound on
En⩽XΛ(n)f (n), which is O(log X).

In our statement of the result we have made a particular choice of the the ranges of µ, ν
for which estimates for Type I/II sums are required. There is considerable ﬂexibility
in the choice of these ranges. Though this matter does not concern us here, we remark
that it has apparently not been completely clariﬁed in the literature (though see [6, §8]
for a related discussion).

When is an attempt to use the method of Type I/II sums likely to be successful in
establishing a non-trivial bound for En⩽XΛ(n)f (n)? In general, one might hope for
success when f does not behave “multiplicatively”. Certainly if f is multiplicative, say
f = χ for some Dirichlet character χ, then by choosing am = f (m) and bn = f (n) we see
that the Type II sums are not always small. A similar phenomenon persists for those f
which are the sum of a few multiplicative functions, for example the additive character
f (n) = e(an/q) with q a small integer. Fortunately one can estimate En⩽X Λ(n)f (n)
for these functions by other means, namely the explicit formula and theorems on the
location of zeroes of L-functions.

If, on the other hand, f does not exhibit signiﬁcant multiplicative behaviour then one
may hope that the method of Type I and II sums will work. The most classical instance
of this, worked out by Vinogradov in the course of proving that every large odd number
is the sum of three primes, is the case f (n) = e(αn) where α is not close to a rational
a/q. Our task here is to handle the case f (n) = (−1)s(n).

2.4. Proof of the method of Type I/II sums. Even though Proposition 2.3.1 is
not normally stated with quite the same technical reﬁnements that we have done, the
reader familiar with the basics of this theory may prefer to skip this somewhat technical
section.

Before making a start on the proof proper, we show that the assumption that Type II
sums are small implies that Type I sums are small for a much larger range of µ than
we have hypothesised.

THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 15

Lemma 2.4.1 (Type II implies extended Type I). Suppose that f : {1, . . . , N} → C
is a function with ∥f ∥∞ ⩽ 1 for which Type I and Type II sums are δ-small. Then we
have the Type I estimate 1
X
 ∑

m∼2µ
 ∣
∣ ∑

n∈Im f (mn)∣
∣ ≪ δ log X

in range 2µ ⩽ X 99/100.

Proof. Since Type I sums are δ-small, we may assume that 2µ ⩾ X 1/100. It clearly
suﬃces to prove that 1
X
 ∑

m∼2µ
 ∑

n∼2ν ωm1Im(n)f (mn) ≪ δ log X (2.1)

for all choices of ωm with |ωm| = 1. But for the cutoﬀ 1Im(n), which does not factor as
a product of a function of m with a function of n, this looks like a Type II sum. To
remove the cutoﬀ, we employ a standard “separation of variables” trick. By the Fourier
inversion formula on Z we have

1Im(n) = ∫ 1

0 ̂1Im(θ)e(nθ) dθ.

Thus the left-hand side of (2.1) is equal to

1
X
 ∫ 1

0
 ( ∑

m∼2µ
 ∑

n∼2ν ωm̂1Im(θ)e(θn)f (mn)) dθ.

Since Type II sums are δ-small and

|̂1Im(θ)| ≪ min(X, |θ|−1)

we see that this is at most
 δ ∫ 1

0 min(X, |θ|−1) dθ ≪ δ log X.

This concludes the proof.

Proof of Proposition 2.3.1. The argument is essentially that of Vaughan [48], but I have
followed the beautiful presentation in the book of Iwaniec and Kowalski [32]. We start
with the easily-veriﬁed relation
 Λ(n) = ∑

b,c
bc|n
 Λ(b)µ(c).

Let U := X 1/3 (say), and decompose this sum as

Λ(n) = Λ♯♯(n) + Λ♯♭(n) + Λ♭♯(n) + Λ♭♭(n),

where ♭ denotes “large” divisors and ♯ denotes “small” divisors, so that for example

Λ♭♯(n) := ∑

b⩾U,c<U
bc|n
 Λ(b)µ(c).

16 BEN GREEN

We observe that Λ♯♭(n) + Λ♯♯(n) = ∑

b<U Λ(b) ∑

c| n
b µ(c) = 1n<U

whilst
 Λ♭♯(n) + Λ♯♯(n) = ∑

c<U
c|n
 µ(c) ∑

b| n
c Λ(b)

= ∑

c<U
c|n
 µ(c) log(n/c).

Thus we obtain what is essentially Vaughan’s identity,

Λ(n) = −Λ♯♯(n) + Λ♭♭(n) + 1n<U Λ(n) + ∑

c<U
c|n
 µ(c) log(n/c). (2.2)

Weighting by f (n) and summing over n ⩽ X we obtain
∑

n⩽X Λ(n)f (n)

= − ∑

n⩽X Λ♯♯(n)f (n) + ∑

n⩽X Λ♭♭(n)f (n) + ∑

n<U Λ(n)f (n) + ∑

c<U
c|n
 µ(c) ∑

n⩽X f (n) log(n/c)

= S1 + S2 + S3 + S4.

Our objective is to use the assumption that Type I and II sums are small in order to
bound the sums Si.

Bounding S1. We have
 S1 = ∑

b,c<U Λ(b)µ(c) ∑

n⩽X/bc f (bcn).

This may be rewritten as ∑

m<U 2 ωm ∑

n⩽X/m f (mn), (2.3)

where ωm := ∑

b,c<U
bc=m
 Λ(b)µ(c).

By splitting into O(log2 X) dyadic ranges for m and n, we see that it suﬃces to prove
that ∑

m∼2µ |ωm|∣
∣ ∑

n∈Im f (mn)∣
∣ ≪ δ1/2X logC−2 X (2.4)

whenever Im ⊆ [2ν−1, 2ν) is an interval and 2µ+ν ⩽ X. This does not quite follow from
Lemma 2.4.1 since ωm is not bounded. We do, however have |ωm| ≪ τ (m) log X, where
τ is the divisor function, and hence since ∑

n⩽N τ (n)2 ≪ N log3 N we have
∑

m∼2ν |ωm|2 ≪ 2µ log5 X.

THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 17

This means that for any Q > 0 we have the estimate
∑

m∼2µ
|ωm|>Q
 |ωm| ≪ 2µQ
−1 log5 X.

Splitting the sum in (2.4) into two parts according as |ωm| is or is not greater that Q
we obtain ∑

m∼2µ |ωm|∣
∣ ∑

n∈Im f (mn)∣
∣ ≪ Q
−1X log5 X + Q ∑

m∼2µ
 ∣
∣ ∑

n∈Im f (mn)∣
∣.

By Lemma 2.4.1 this is bounded by

Q
−1X log6 X + δQX log X.

Choosing Q := δ−1/2 log5/2 X, we obtain a bound of the required type.

Bounding S2. The sum S2 may be written as
∑

b,c⩾U
 ∑

t⩽X/bc Λ(b)µ(c)f (bct).

Changing variables and rearranging, this may be written as
∑

m⩾U
mn⩽X
 ambnf (mn), (2.5)

where am := Λ(m) and bn := ∑

c⩾U :c|n µ(c). Observing that bn = 0 if n < U, we see
that the sum over m, n is covered by O(log2 X) dyadic ranges m ∼ 2µ, n ∼ 2ν with
X 0.01 ⩽ 2µ, 2ν ⩽ X 0.99. We may therefore split (2.5) into O(log2 X) sums of the form
∑

m∼2µ
 ∑

n∼2ν 1I(n)(m)ambnf (mn), (2.6)

where I(n) ⊆ [2µ−1, 2µ) is an interval. It suﬃces to show that any such sum is ≪
δ1/2X logC−2 X.

These sums look rather like Type II sums, except for the presence of the cutoﬀ 1I(n)(m)
and the fact that the sequences am, bn are not bounded.

To remove the cutoﬀ we use the same device as in the proof of Lemma 2.4.1, writing
(2.6) as ∫ 1

0
 ( ∑

m∼2µ
 ∑

n∼2ν ame(θm)̂1I(n)(θ)bnf (mn)) dθ.

Since |̂1I(n)(θ)| ≪ min(X, |θ|−1) we see that it suﬃces to prove that
∑

m∼2µ
 ∑

n∼2ν a
′
mb
′
nf (mn) ≪ δ1/2X logC−3 X

uniformly for all choices of a
′
m with |a
′
m| ⩽ |am| and |b
′
n| ⩽ |bn| for all m, n.

This has eﬀectively removed the cutoﬀ that we were worried about. It remains to deal
with the non-boundedness of the sequences (a
′
m)m∼2µ, (b
′
n)n∼2ν . The non-boundedness

18 BEN GREEN

of a
′
m is rather minor, since clearly a
′
m ⩽ log X for all m. Thus we may deﬁne a
′′
m :=
a
′
m/ log X and reduce to proving that
∑

m∼2µ
 ∑

n∼2ν a
′′
mb
′
nf (mn) ≪ δ1/2X logC−4 X (2.7)

whenever |a
′′
m| ⩽ 1. To deal with b
′
n, we note that |b
′
n| ⩽ τ (n). Thus, by the argument
used in dealing with S1, we have
∑

n∼2ν
|b′
n|⩾Q
 |b
′
n| ≪ 2νQ
−1 log3 X.

Splitting the sum in (2.7) into parts according as |b
′
n| ⩾ Q or not, we conclude as before.

Bounding S3. The sum S3 is trivially bounded by U = X 1/3 log X. The δ-smallness of
Type I sums implies (rather vacuously) that |f (n)| ⩽ δX. Since we are assuming that
∥f ∥∞ = 1, it follows that δ ⩾ 1/X and hence this term may be absorbed into the bound
δ1/2X logC X that we are trying to establish.

Bounding S4. The sum may be written as
∑

m⩽U
 ∑

n⩽X/m µ(m) log nf (mn).

This may be split into O(log2 X) sums of the form
∑

m∼2µ
 ∑

n∈Im µ(m) log nf (mn), (2.8)

where Im ⊆ [2ν−1, 2ν). This is almost a Type I sum: only the presence of the log n
term prevents it being so. This term is so smooth, however, that it may be eﬀectively
removed by “partial summation”. To do this, simply write

log n = ∫ n

1
 dt
t

and rearrange (2.8) as ∫ 2ν

1
 dt
t
 ∑

m∼2ν µ(m) ∑

n∈Im,t f (mn),

where Im,t ⊆ [2ν−1, 2ν) is an interval. The smallness of Type I sums, as given in Lemma
2.4.1, may now be used to see that this is bounded as required.

This completes the bounding of S4, and hence the proof of Proposition 2.3.1.

2.5. The sum-of-digits function and related functions. If n is a positive
integer and n = ∑
i⩾0 ni2i is its binary expansion, we write

s(n) := ∑

i ni.

THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 19

This is, of course, a ﬁnite sum. For each positive integer k we consider also the truncated
functions
 sk(n) :=
 k−1∑

i=0 ni.

These functions are closely related to s(n), of course; on any interval [2kt, 2k(t + 1)) the
functions sk(n) and s(n) diﬀer by a ﬁxed constant. The truncated functions sk(n) are
periodic with period 2k, however, and this makes them rather amenable to study using
Fourier analysis on the ﬁnite group Z/2kZ.

In fact we will be more interested in the oscillatory functions

f (n) := (−1)s(n)

and fk(n) := (−1)sk(n).

The functions sk and fk may, by abuse of notation, be regarded as functions on Z/2kZ.

Deﬁnition 2.5.1 (Finite Fourier transform). Let k ⩾ 0 be a ﬁxed integer. Then we
deﬁne ̂fk(r) := Ex∈Z/2kZfk(x)e(−rx/2k).

We now proceed to establish several properties of the Fourier transform ̂fk which will
be useful later on. We collect these here since they are all proved in a very similar way.
The reader might wish to read through the proof of the ﬁrst one, then skip to the next
section. She might return here as each result is required.

Proposition 2.5.2 (L
∞ bound). We have | ̂fk(r)| ≪ 2−ck for all r ∈ Z/2kZ.

Proof. We observe that

̂fk(r) = 2−k(1 − e(t))(1 − e(2t)) . . . (1 − e(2k−1t)), (2.9)

where t = r/2k. The result now follows by observing that

|1 − e(u)||1 − e(2u)| = 4| sin(πu) sin(2πu)| = 8| cos(πu)|(1 − cos
2(πu))

is maximised when cos2(πu) = 1/3, and attains the value 16/3√
3 there. Thus, grouping
terms in pairs, we see that
 ̂fk(r) ≪ (4/3√
3)k/2 ≪ 2−k/10.

This concludes the proof.

Proposition 2.5.3 (L
1 bound in progressions). Suppose that 0 ⩽ k′ ⩽ k and that a is
a residue class (mod 2k′). Then
∑

r∈Z/2kZ
r≡a(mod 2k′ )
 | ̂fk(r)| ≪ 2( 1
2 −c)(k−k′)| ̂fk′(a)|.

20 BEN GREEN

Remark. For the purposes of discussion suppose that k′ = a = 0. Then this proposition
states that ∑

r∈Z/2kZ | ̂fk(r)| ≪ 2( 1
2 −c)k.

By contrast the trivial bound (arising from Parseval’s identity and an application of
Cauchy-Schwarz) for this quantity would be 2k/2.

One tends to imagine that a saving over a trivial bound can be expected whenever there
is some kind of “cancellation”, such as one might expect if the function fk : Z/2kZ →
{−1, 1} were chosen at random. This setting is rather diﬀerent, and this represents
perhaps the most remarkable feature of the paper [36]. It is possible to show that if fk
is chosen randomly then ∑

r∈Z/2kZ | ̂fk(r)| ≫ 2k/2.

Our proposition therefore captures a very speciﬁc property of the functions fk(n) =
(−1)sk(n).

Proof. Write S(a, k) for the sum on the left. For any r ∈ Z/2kZ the expansion (2.9)
yields | ̂fk(r)| = 1
2|1 − e(r/2k)|| ̂fk−1(r)|.

Suppose that k ⩾ k′ + 1. Since ̂fk−1(r) is periodic with period 2k−1, we may split S(a, r)
as a sum over two ranges 0 ⩽ r < 2k−1 and 2k−1 ⩽ r < 2k, thereby obtaining

S(a, k) ⩽ S(a, k − 1) sup
t∈[0,1]
 1
2(|1 + e(t)| + |1 − e(t)|).

Now a simple exercise in Euclidean geometry conﬁrms that

|1 + e(t)| + |1 − e(t)| ⩽ 2√
2, (2.10)

with equality if and only if t = ±1/4. Hence

S(a, k) ⩽ √2S(a, k − 1). (2.11)

This does not, in itself, suﬃce to establish a nontrivial bound for S(a, k).

If k ⩾ k′ + 2 one may improve things by splitting the sum S(a, k) into four ranges
j2k−2 ⩽ r < (j + 1)2k−2 (j = 0, 1, 2, 3). This leads to

S(a, k) ⩽ S(a, k − 2) sup
t∈[0,1]
 1
4
 3∑

j=0 |1 − e(t + j/4)||1 − e(2(t + j/4))|. (2.12)

Now two applications of (2.10) conﬁrm that

3∑

j=0|1 − e(t + j/4)||1 − e(2(t + j/4))|

= |1 − e(2t)|(|1 − e(t)| + |1 + e(t)|) + |1 + e(2t)|(
|1 − e(t + 1/4)| + |1 + e(t + 1/4)|)

⩽ 2√
2(|1 − e(2t)| + |1 + e(2t)|)

⩽ 8.
 THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 21

Furthermore equality can never occur, and so by compactness this expression is bounded
by 8 − c for some c > 0. Comparing with (2.12) we see that

S(a, k) ⩽ (2 − c)S(a, k − 2).

To complete the proof of the proposition one may apply this repeatedly, followed perhaps
by one application of (2.11), to bound S(a, k) above in terms of S(a, k′).

2.6. Analysis of Type I sums.

Proposition 2.6.1 (Estimate for Type I sums). Suppose that 2µ ⩽ X 1/20. For each
m ∼ 2µ, suppose that Im ⊆ (2ν−1, 2ν] is an interval. Then
∑

m∼2µ | ∑

n∈Im f (mn)| ≪ǫ X 19/20+ǫ.

Remark. In [36] an alternative argument (related to the large sieve) is used, in which
the same estimate is established under the weaker assumption that 2µ = Oǫ(X 1/2−ǫ).
Proof. For m, n in the ranges under consideration we have have f (mn) = fk(mn), where
k := µ + ν. Fix a value of m, and write Sm := ∑

n∈Im f (mn). We thus have

Sm = ∑

x∈Z/2kZ f (x)1P (x),

where P = Pm := {mn : n ∈ Im}. By Parseval’s identity this is

2k ∑

r∈Z/2kZ
 ̂fk(r)̂1P (r),

which is bounded by 2k∥ ̂fk∥∞∥̂1P ∥1. By summing a geometric series we have

|̂1P (r)| ≪ min(1, ∥r/2k∥−1),

and therefore ∥̂1P ∥1 ≪ k ≪ log X. It follows from Lemma 2.5.2 that

Sm ≪ 2kX −1/10 log X.

Summing over m ∼ 2µ, we obtain the required bound.

2.7. Two diophantine lemmas. In this section we give two results of a ‘diophantine’
nature which we will use in the next section, in which Type II sums are analysed. Both
of these are more-or-less standard in this subject.

Lemma 2.7.1 (Vinogradov). Suppose that q, Q, R are all natural numbers less than X,
that β ∈ R, and suppose that (a, q) = 1. Then

R∑

x=0 min (Q, ∥ax/q + β∥−1) ⪅ Q + q + R + QR/q.

22 BEN GREEN

Proof. The key observation is that as x ranges over any interval of length q, the numbers
ax/q(mod 1) range over the set 0, 1/q, . . . , (q − 1)/q. It follows easily that if I is any
interval of length at most q then
∑

x∈I min (
Q, ∥ax/q + β∥−1) ≪ Q + q log q.

Since the range x = 1, . . . , R may be split into at most R/Q + 1 such ranges, the result
follows immediately.

Lemma 2.7.2 (Equidistribution lemma). Suppose that α ∈ R and that I is an interval
of integers with |I| = N. Suppose that δ1, δ2 satisfy δ1 < δ2/16, and suppose that there
are at least δ2N elements n ∈ I for which ∥αn∥R/Z ⩽ δ1. Suppose that N ⩾ 8/δ2. Then
there is some q ⩽ 8/δ2 such that ∥αq∥R/Z ⩽ 4δ1δ−1
2 N −1.

Proof. By a well-known argument of Dirichlet there is some q ⩽ N and an a coprime to
q such that |α − a/q| ⩽ 1/qN. Set θ := α − a/q, let n0 ∈ I be ﬁxed, and set β := n0θ.
Then for any n ∈ I we have, by the triangle inequality,

∥αn∥R/Z ⩾ ∥an/q + β∥R/Z − ∥θ(n − n0)∥R/Z ⩾ ∥an/q + β∥R/Z − 1/q,

and so
 ∥an/q + β∥R/Z ⩽ δ1 + 1
q (2.13)

for at least δ2N values of n ∈ I.

Now as n ranges over any interval of length q the numbers an/q range over the set
{0, 1/q, 2/q, . . . }. Thus in any such interval the number of n satisfying (2.14) is no
more than δ1q + 2. Now I may be divided into at most N/q + 1 intervals of length no
more than q, and thus the number of n ∈ I satisfying (2.13) is bounded by

( N
q + 1)(δ1q + 2).

On the other hand, we are assuming this quantity is at least δ2N. Since δ2 ⩾ 4δ1,
N ⩾ 8/δ2 and q ⩽ N this easily implies that q ⩽ 8/δ2.

Now the assumption of the lemma implies, by piegonholing, that ∥αn∥R/Z ⩽ 2δ1 for at
least δ2N/2 values of n ∈ {1, . . . , N/2}. We have

αn = an
q + θn

where |θ| ⩽ 1/qN. If n ⩽ N/2, it follows that either

∥αn∥R/Z ⩾ 1/2q ⩾ δ2/16 > δ1

or else n is a multiple of q. But for k ⩽ N/2q we have simply

∥αkq∥R/Z = |θkq|.

Thus |θkq| ⩽ 2δ1 for at least δ2N/2 such values of k, and in particular for some k0 ⩾
δ2N/2. Hence |θ| ⩽ 2δ1/qk0 ⩽ 4δ1/qδ2N, which implies the result.

THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 23

2.8. Analysis of Type II sums. We start with an inequality which is often used in
the estimation of Type II sums, van der Corput’s inequality.

Van der Corput’s inequality. Van der Corput’s inequality is a kind of generalisation of
the Cauchy-Schwarz inequality.

Lemma 2.8.1 (van der Corput inequality). Let N, H be positive integers and suppose
that (an)n∈{1,...,N } is a sequence of complex numbers. Extend (an) to all of Z by deﬁning
an := 0 when n /∈ {1, . . . , N}. Then

| ∑

n an|2 ⩽ N + H
H
 ∑

|h|⩽H
 (1 − |h|
H ) ∑

n anan+h.

Proof. We have ∑

n an = 1
H
 ∑

−H<n⩽N
 H−1∑

h=0 an+h.

Thus, applying the Cauchy-Schwarz inequality, we have

∣
∣ ∑

n an∣
∣2 = 1
H 2 ∣
∣ ∑

−H<n⩽N
 H−1∑

h=0 an+h∣
∣2

⩽ N + H
H 2 ∑

−H<n⩽N
 ∣
∣
 H−1∑

h=0 an+h∣
∣
2

= N + H
H 2 ∑

−H<n⩽N
 H−1∑

h=0
 H−1∑

h′=0 an+ha
′
n+h,

which equals the right hand side of the claimed inequality. This concludes the proof.

Proposition 2.8.2 (Estimate for Type II sums). Suppose that X 1/100 ⩽ 2µ, 2ν ⩽
X 99/100. Suppose that (am)m∼2µ and (bn)n∼2ν are arbitrary sequences of complex numbers
with |am|, |bn| ⩽ 1. Then ∑

m∼2µ
 ∑

n∼2ν ambnf (mn) ≪ X 1−κ

for some absolute κ > 0.

Proof. We may assume without loss of generality that ν ⩾ µ. Suppose for a contradic-
tion that the result is false. We write this
∑

m∼2µ
 ∑

n∼2ν ambnf (mn) ⪆ 2µ+ν.

By Cauchy-Schwarz we obtain
∑

m∼2µ | ∑

n∼2ν bnf (mn)|2 ⪆ 2µ+2ν.

24 BEN GREEN

Let ρ := c(µ + ν), where c > 0 is a constant to be chosen later, and apply the van der
Corput inequality (Lemma 2.8.1) with H := 2ρ. It follows that
∑

m∼2µ
 ∑

n∼2ν
 ∑

|h|⩽H
 (1 − |h|
H )
bnbn+hf (m(n + h))f (mn) ⪆ 2µ+ν+ρ.

The h = 0 term is negligible, and so we obtain
∑

1⩽|h|⩽2ρ
 ∑

n∼2ν | ∑

m∼2µ f (m(n + h))f (mn)| ⪆ 2µ+ν+ρ. (2.14)

Our aim is to obtain some cancellation in the inner sum and thereby reach a contra-
diction. The ﬁrst step is to show that f can be replaced by the truncated function fk,
where k := µ + 2ρ (say) is not much bigger than µ.

Now we have s(m(n + h)) − sk(m(n + h)) = s(mn) − sk(mn)
if mn, m(n + h) lie in the same interval [2kt, 2k(t + 1)]. Since mh is much smaller
than 2k, this will happen most of the time. In fact for it not to hold we must have
mn ∈ [2kt − 2µ+ρ, 2kt] for some t (that is, there is a “carry” on adding mh to mn). Now
for x ⩽ X the divisor function τ satisﬁes τ (x) ⪅ 1, and therefore the number of “bad”
pairs (m, n) is at most ∑

t⩽2ν−2ρ
 2kt∑

l=2kt−2µ+ρ τ (l) ⪅ 2µ+ν−ρ.

The contribution of the bad pairs to (2.14) is therefore negligible, and we may replace
that inequality by ∑

1⩽|h|⩽2ρ
 ∑

n∼2ν | ∑

m∼2µ fk(m(n + h))fk(mn)| ⪆ 2µ+ν+ρ. (2.15)

Let us now focus on the inner sum

En,h := ∑

m∼2µ fk(m(n + h))fk(mn),

which we will study using Fourier analysis on Z/2kZ. Expanding both copies of fk using
the inversion formula, we see that

En,h = ∑

m∼2µ
 ∑

r,s∈Z/2kZ
 ̂fk(r) ̂fk(s)e
( rm(n + h) + smn
2k )
,

which is bounded by ∑

r,s∈Z/2kZ | ̂fk(r)|| ̂fk(s)| min(2µ, ∥ r(n + h) + sn
2k ∥−1).

From (2.15) we thus have
∑

r,s∈Z/2kZ | ̂fk(r)|| ̂fk(s)| ∑

n∼2ν
 ∑

1⩽|h|⩽2ρ min(2µ, ∥ r(n + h) + sn
2k ∥−1) ⪆ 2µ+ν+ρ. (2.16)

THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 25

Deﬁne the weights

ωr,s := 2−µ−ν−ρ ∑

n∼2ν
 ∑

1⩽|h|⩽2ρ min(2µ, ∥ r(n + h) + sn
2k ∥−1).

Then (2.16) becomes ∑

r,s∈Z/2kZ | ̂fk(r)|| ̂fk(s)|ωr,s ⪆ 1. (2.17)

To do anything with this we need to gain a greater understanding of the weights ωr,s.

Lemma 2.8.3 (Size of ωr,s). Suppose that ν2(r + s) = t. Then

ωr,s ⪅ 2−µ + 2k−t−µ−ν + 2t−k.

Proof. Write (r + s)/2k = a/2k−t, where is odd. Thus

ωr,s = 2−µ−ν−ρ ∑

n∼2ν
 ∑

1⩽|h|⩽2ρ min (2µ, ∥ a
2k−t n + r
2k h∥−1).

Thus ωr,s ⩽ 2−µ−ν sup
1⩽|h|⩽2ρ
 ∑

n∼2ν min(2µ, ∥ a
2k−t n + r
2k h∥−1)

By Lemma 2.7.1 we obtain

ωr,s ⪅ 2−ν + 2−µ + 2k−t−µ−ν + 2t−k.

Recalling that ν ⩾ µ, we see that this implies the claimed bound.

Let us recall (2.17). This clearly implies that there is t, 0 ⩽ t ⩽ k, such that
∑

r,s∈Z/2kZ
ν2(r+s)=t
 | ̂fk(r)|| ̂fk(s)|ωr,s ⪆ 1. (2.18)

Now by Lemma 2.8.3, Proposition 2.5.3 and Parseval’s inequality (in turn) we have
∑

r,s∈Z/2kZ
ν2(r+s)=t
 | ̂fk(r)|| ̂fk(s)|ωr,s

⪅ (2−µ + 2k−t−µ−ν + 2t−k) ∑

a∈Z/2tZ
 ∑

r≡a(mod 2t) | ̂fk(r)| ∑

s≡−a(mod 2t) | ̂fk(s)|

⪅ 2(k−t)(1−c)(2−µ + 2k−t−µ−ν + 2t−k) ∑

a∈Z/2tZ | ̂ft(a)|| ̂ft(−a)|

⩽ 2(k−t)(1−c)(2−µ + 2k−t−µ−ν + 2t−k)

for some absolute constant c > 0. Recalling that k = µ + 2ρ we see that the ﬁrst two
terms are at most 24ρ−ck, which is not ⪆ 1 if ρ is chosen suﬃciently small. Thus we see
that if (2.18) holds then 2−c(k−t) ⪆ 1, which implies that 2t ⪆ 2k.

26 BEN GREEN

Assume, then, that this is the case. Applying Parseval’s identity again (or Proposition
2.5.3, but this is overkill now) we obtain, for any ε,

∑

r,s∈Z/2kZ
ν2(r+s)=t
ωr,s⩽2−εk
 | ̂fk(r)|| ̂fk(s)|ωr,s ⩽ 2−εk ∑

a∈Z/2tZ
 ∑

r≡a(mod 2t) | ̂fk(r)| ∑

s≡−a(mod 2t) | ̂fk(s)|

⩽ 2k−t−εk ⪅ 2−εk.

It follows that, in (2.18), we may restrict attention to values of r, s for which ωr,s ⪆ 1,
thus
 ∑

r,s∈Z/2kZ
ωr,s⪆1
 | ̂fk(r)|| ̂fk(s)|ωr,s ⪆ 1. (2.19)

In the next lemma we will show that there are rather few pairs (r, s) with ωr,s ⪆ 1. To
do this we will make use of the as yet unexploited averaging over h which occurs in the
deﬁnition of ωr,s.

Lemma 2.8.4 (Large values of ωr,s). There are ⪅ 2ρ pairs (r, s) ∈ Z/2kZ × Z/2kZ such
that ωr,s ⪆ 1.

Proof. We know already, by Lemma 2.8.3, that we must have ν2(r + s) = t, where
2t ⪆ 2k. Write (r + s)/2k = a/2k−t, where a is odd. We have
∑

1⩽|h|⩽2ρ
 ∑

n∼2ν min(2µ, ∥ a
2k−t n + r
2k h∥−1) ⪆ 2µ+ν+ρ.

Dividing the sum over n into residue classes (mod 2k−t), of which there are ⪅ 1, we see
that there is θ such that ∑

1⩽|h|⩽2ρ min(2µ, ∥θ + r
2k h∥−1) ⪆ 2µ+ρ. (2.20)

Although this looks to be of the form covered by Vinogradov’s lemma (Lemma 2.7.1),
the fact that 2ρ ≪ 2k means that more information may be gleaned by appealing
instead to Lemma 2.7.2. From (2.20) it follows that for ⪆ 2ρ values of h, 1 ⩽ |h| < 2ρ,
we have ∥θ + r
2k h∥ ⪅ 2−µ.

Fixing some h0 with this property and considering the numbers h − h0, we may assume
that θ = 0. Applying Lemma 2.7.2, we see that

∥qr/2k∥R/Z ⪅ 2−µ−ρ

for some q ⪅ 1. Thus if ωr,s ⪆ 1 then there is some q ⪅ 1 such that |rq(mod 2k)| ⪅ 2ρ

(recall that k = µ + 2ρ). There are ⪅ 2ρ such values of r, and for each of them there
are just ⪅ 1 values of s such that t := ν2(r + s) satisﬁes 2t ⪆ 2k.

THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 27

It is now an easy matter to show that (2.19) cannot hold which, as we have shown,
implies that Type II sums are small. Indeed using Lemma (2.8.4) and Proposition 2.5.2
we obtain
 ∑

r,s∈Z/2kZ
ωr,s⪆1
 | ̂fk(r)|| ̂fk(s)|ωr,s ⪅ 2ρ−2ck.

This contradicts (2.19) if ρ is chosen suﬃciently small.

Proof of Theorem 2.1.1. Almost nothing more need be said: Theorem 2.1.1 is an
immediate consequence of Propositions 2.3.1, 2.6.1 and 2.8.2.

3. Patterns of primes

The aim of this section is to discuss work of the author and T. Tao on linear equations
in primes. This programme is not yet completed and what has been done so far is
spread across a number of papers [21, 22, 23, 24, 25, 26]. It is also discussed in several
expository articles [17, 19, 42, 43, 44].

Our aim here is to do little more than try to describe what we have proved and what we
hope to prove, and to furnish the reader with some idea of how the various papers ﬁt
together. In other words we hope that this section may be used as a sort of ‘roadmap’ for
readers interested in a more detailed study of the papers. There are some conspicuous
absences from the current section. Our treatment of the history of the subject is very
patchy (see the article [34] for this), and we omit any discussion of links with the ergodic
theory literature (see [28, 33] for this). References are to the versions of the papers which
were available on www.arxiv.org on October 1st 2007. It is quite likely that published
versions will have diﬀerent theorem numberings.

Suppose that ψ1, . . . , ψt : Z
d → Z are aﬃne-linear forms. The basic questions which
motivate our work are the following.

Question 3.0.5 (Existence of prime values). Are there values of ⃗n ∈ Z
d for which these
forms all take prime values? Are there inﬁnitely many such ⃗n?

Question 3.0.6 (Asymptotics). How many such ⃗n are there inside the box [−N, N]d?

In this generality, our questions contain many of the classical questions in additive prime
number theory.

(i) When d = 1, t = 2, ψ1(n) = n and ψ2(n) = 2m − n we have the Goldbach
Conjecture: is 2m the sum of two primes?
(ii) When d = 1, t = 2, ψ1(n) = n and ψ2(n) = n + 2 we have the Twin Prime
Conjecture: are there inﬁnitely pairs of primes which diﬀer by 2?

28 BEN GREEN

(iii) When d = 2, t = 3, ψ1(⃗n) = n1, ψ2(⃗n) = n2 and ψ3(⃗n) = m − n1 − n2 (m odd)
we have the Ternary Goldbach Conjecture: is m the sum of three primes?
(iv) When d = 2, t = k and ψi(⃗n) = n1 + (i − 1)n2, i = 1, . . . , k we have the question
of whether there exist arithmetic progressions of length k consisting entirely of
primes.

Essentially nothing is known about either Question 3.0.5 or Question 3.0.6 in cases
(i) and (ii). Both Questions were answered in case (iii) some seventy years ago by
Vinogradov, building on earlier work of Hardy and Littlewood. Question 3.0.5 was
answered in case (iv) by the author and Tao [21]. Question 3.0.6 in that case is much
harder and was answered for k = 3 by Chowla and van der Corput in 1939 and for
k = 4 by the author and Tao [22, 23, 24]. Question 3.0.6 for k ⩾ 5 is one of the main
goals of our current programme of research, and we shall report on what progress has
been made so far. We will not give any further separate discussion of Question 3.0.5, as
this has now been exposited in many places. Particularly recommended are the articles
[28] and [33]. See also [19, 42, 43, 44].

There are very natural conjectural answers to Questions 3.0.5 and 3.0.6. It is clear that
congruence conditions may result in there being no, or very few, choices of ⃗n for which all
of the forms ψi(⃗n) are prime. A trivial example is the system ψ1(n) = n, ψ2(n) = n + 7
– consideration of this (mod 2) obviously implies that ψ1(n) and ψ2(n) cannot both be
prime. Congruence conditions may alter our expectations in more subtle ways too. For
example if n is known to be prime (and is not 2) then one feels that n + 2 is more likely
to be prime than a random integer of the same size, for it is already known to be odd.
Pulling against this, however, is the observation that if n ̸= 3 then n is congruent to
either 1 or 2(mod 3), and so n + 2 is congruent to either 0 or 1(mod 3), but never to 2.
On this (mod 3) evidence one feels that n + 2 is less likely to be prime than a random
integer of the same size. Another obvious way in which one could fail to have any
prime values among the ψi(⃗n) is if they cannot be simultaneously positive, for example
ψ1(⃗n) = n1 − n2, ψ2(⃗n) = n2 − n3, ψ3(⃗n) = n3 − n1.

A more profound analysis of these intuitions suggests the following conjecture. In the
formulation of this conjecture we use the local von Mangoldt functions ΛZ/pZ, deﬁned
by
 ΛZ/pZ(x) = { p/(p − 1) if (x, p) = 1
0 otherwise.

Dickson’s Conjecture. Suppose that d, t, N ⩾ 1 are integers. Suppose that no two
of the forms ψi are rational multiples of one another, and that no form ψi is constant.
Write ψi(⃗n) = li1n1 + · · · + lidnd + bi and suppose that we have |lij| ⩽ L, |bi| ⩽ LN for
some real number L. Then for any convex body K ⊆ [−N, N]d we have
∑

⃗n∈K∩Zd Λ(ψ1(⃗n)) . . . Λ(ψd(⃗n)) = β∞ ∏

p βp + od,t,L(N d),

where the local factors βp are deﬁned by

βp := E⃗x∈(Z/pZ)dΛZ/pZ(ψ1(⃗x)) . . . ΛZ/pZ(ψd(⃗x))

THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 29

and
 β∞ := vol(K ∩ ψ−1
1 (R⩾0) ∩ · · · ∩ ψ−1
t (R⩾0)).

Remarks. We have counted primes weighted using the von Mangoldt function, as this
gives tidier expressions. For an unweighted version see [24, Conjecture 1.4]. It is quite
fun to play with particular cases of the conjecture. For example with d = 1, t = 2,
ψ1(n) = n, ψ2(n) = n + 2 and K = [0, N] we obtain the conjecture

∑

n⩽N Λ(n)Λ(n + 2) = 2 ∏

p⩾3
 (
1 − 1
(p − 1)2 )N + o(N)

for the (weighted) number of twin primes less than or equal to N. The numerical value
of the constant here is about 1.32. Some other examples are worked out in [24, §1].

Let us return to the speciﬁc examples (i) – (iv) mentioned above. What makes some of
these questions much easier than others? The most important parameter in determining
the diﬃculty of Questions 3.0.5 and 3.0.6 is the complexity of the system of forms
{ψ1, . . . , ψt}.

The deﬁnition of complexity involves nothing more than simple linear algebra, but it is
not especially illuminating at ﬁrst sight. Let s be a positive integer. We say that the
complexity of the system {ψ1, . . . , ψt} is at most s if, for any i ∈ {1, . . . , t}, the forms
{ψ1, . . . , ψi−1, ψi+1, . . . , ψt} may be divided into s + 1 classes in such a way that ψi is not
in the aﬃne linear span of any of them. Thus the system {n1, n1 +n2, n1 +2n2, n1 +3n2}
has complexity at most 2 since, quite obviously, we may remove any one form and divide
the remaining three forms into singleton classes whose aﬃne span does not contain that
form. However the complexity of this system is not at most 1: if we remove the form n1
then it is impossible to divide the remaining forms {n1 + n2, n1 + 2n2, n1 + 3n2} into two
classes such that n1 is not in the aﬃne linear span of any class. Thus the complexity
of this system is exactly two. The complexity of the system {n1, n1 + n2, n1 + 2n2}
is one, as is the complexity of the system {n1, n2, m − n1 − n2} for any ﬁxed m. The
complexity of the system {n, n + 2} is apparently undeﬁned, since if we remove the form
n it is impossible to partition the singleton class {n + 2} in any way such that n is
not contained in the aﬃne span of a class. In such cases we say that the complexity is
inﬁnite. The system {n, 2m − n}, m ﬁxed, arising from the Goldbach Conjecture has
inﬁnite complexity.

Roughly speaking, only systems of complexity one were understood before the recent
work [22, 23, 24]. Much of the theory in the complexity one case was worked out in a
paper of Balog [3], which built upon the techniques of Vinogradov.

Complexity is the most important measure of how diﬃcult it is to solve Questions 3.0.5
and 3.0.6. However there are some rather trivial examples of systems of complexity
greater than one for which Question 3.0.5 can be answered. For example just using the
fact that there are ≫ N/ log N primes less than N and the Cauchy-Schwarz inequality
it is possible to show that there are ≫ N 4/ log8 N quadruples (n1, n2, n3, n4) such that

30 BEN GREEN

all eight of the forms

{n1, n1 + n2, n1 + n3, n1 + n4, n1 + n2 + n3, n1 + n2 + n4, n1 + n3 + n4, n1 + n2 + n3 + n4}

are prime. This system has complexity 2.

The reason that complexity one systems have proved amenable to attack is that they
can be studied using harmonic analysis, and in particular the circle method of Hardy
and Littlewood. We are now going to discuss some ideas behind this method in a rather
unorthodox way. It turns out that this is the easiest (in fact so far the only) description
to generalize to systems of complexity 2 and higher. The following formulation of the
principle that ‘harmonic analysis governs systems of complexity 1’ is established in [24].

Proposition 3.0.7. Let N be a prime. Suppose that {ψ1, . . . , ψt} is a system of aﬃne-
linear forms of complexity 1. Suppose that f1, . . . , ft : Z/NZ → [−1, 1] are functions
and that |E⃗n∈(Z/N Z)d f1(ψ1(⃗n)) . . . ft(ψt(⃗n))| ⩾ δ. (3.1)

Then for each i ∈ [t] there is some r ∈ Z/NZ such that

|En∈Z/N Zfi(n)e(−rn/N)| ≫δ 1. (3.2)

In words, if the functions f1, . . . , ft behave in some way unexpectedly when evaluated
along the linear forms ψi, this phenomenon can be detected by evaluating the Fourier
coeﬃcients of the fi.

Proposition 3.0.7 is proved in two stages. The ﬁrst step is to establish a generalized von
Neumann theorem, which is a bound of the form

|E⃗n∈(Z/N Z)d f1(ψ1(⃗n)) . . . ft(ψt(⃗n))| ⩽ inf
i∈[t] ∥fi∥U 2.

Here ∥f ∥U 2 denotes the Gowers U 2-norm of f and is deﬁned by

∥f ∥4
U 2 := Ex,h1,h2∈Z/N Zf (x)f (x + h1)f (x + h2)f (x + h1 + h2).

Results of this type are proved using nothing more than a few applications of the
Cauchy-Schwarz inequality, although the notation can get quite complicated. A simple
example is given in the proof of [18, Proposition 1.9]. Foundational material on the
Gowers norms (including, for example, a proof that they are norms) may be found in
[46, Chapter 11] or [21, Chapter 5].

This ﬁrst step in the proof of Proposition 3.0.7 leads from the hypothesis (3.1) to the
conclusion that each ∥fi∥U 2 is at least δ. To obtain the conclusion (3.2), then, it suﬃces
to establish an Inverse Theorem for the Gowers U 2-norm, stating that if the U 2-norm
of f is large then f correlates with a linear phase.

The proof of this result is so short we give it here. Suppose that f : Z/NZ → [−1, 1] is
a function with ∥f ∥U 2 ⩾ δ. Deﬁne the Fourier transform ˆf : Z/NZ → C by

ˆf (r) := En∈Z/N Zf (n)e(−rn/N).

THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 31

Using orthogonality relations one may easily check that

∥ ˆf ∥4 := ( ∑

r∈Z/N Z | ˆf (r)|4)1/4 = ∥f ∥U 2. (3.3)

Thus ∥ ˆf ∥2
∞∥ ˆf ∥2
2 ⩾ ∥ ˆf ∥4
4 ⩾ δ4.
But by Parseval’s identity we have
∥ ˆf ∥2 = ∥f ∥2 ⩽ 1,

and so we conclude that ∥ ˆf ∥∞ ⩾ δ2.
That is, there is some r ∈ Z/NZ such that

|En∈Z/N Zf (n)e(−rn/N)| ⩾ δ2. (3.4)

We note that (3.3) also gives a converse result: if there is some r ∈ Z/NZ such that

|En∈Z/N Zf (n)e(−rn/N)| ⩾ δ

then ∥f ∥U 2 ⩾ δ.

Proposition 3.0.7 is a somewhat convincing way to formulate the idea that ‘harmonic
analysis can handle systems of complexity one’. For a variety of reasons, however, it is
not immediately applicable to an understanding of the quantity
∑ Λ(ψ1(⃗n)) . . . Λ(ψd(⃗n)) (3.5)

appearing in Dickson’s Conjecture. One obvious point is that the average in Proposition
3.0.7 is over (Z/NZ)d, rather than over [N]d or over the lattice points inside a convex
body. This is a purely technical distinction, and is dealt with in [24, Appendix C].

A more serious problem arises from consideration of how Proposition 3.0.7 might be
applied. There is certainly no mileage to be gained from applying it in the most na¨ıve
way, that is to say with f1 = · · · = ft = Λ. Indeed in that case condition (3.2) does hold
(with r = 0), and so we cannot rule out the possibility of (3.1) holding (and, of course,
Dickson’s Conjecture predicts that (3.1) does hold much of the time). To eliminate the
possibility of (3.2) holding with r = 0 we might split Λ = 1 + (Λ − 1), expand (3.5) as a
sum of 2t terms, and use Proposition 3.0.7 to show that all of the terms except the one
with f1 = · · · = ft = 1 are ‘negligible’. This also fails to work, for the simple reason
that those other terms may not be negligible. Indeed if they were then the arithmetic
constant in Dickson’s Conjecture would be simply 1 rather than the product β∞ ∏

p βp
reﬂecting the distribution of primes (mod 2), (mod 3) etc.

In all of the the work of the author and Tao on primes these issues are bypassed by
means of the so-called W -trick. The trick is easiest to describe in the context of our
paper [21] establishing the existence of arbitrarily long progressions of primes. Look
at the primes 2, 3, 5, 7, . . . . They are very irregularly distributed (mod 2). However if
one deletes the element 2 and rescales the remaining primes by the map x ↦→ (x − 1)/2
one ends up with the sequence 1, 2, 3, 5, 6, 8, . . . . This is now quite regularly distributed
(mod 2), because there are roughly the same number of primes congruent to 1(mod 4)
as there are primes congruent to 3(mod 4). Furthermore if one ﬁnds a long arithmetic

32 BEN GREEN

progression in the new sequence it translates immediately to a long progression in the
primes.

Unfortunately, however, this new sequence is not well-distributed (mod 3), as the only
element congruent to 1(mod 3) that it contains is 1. However we could pick out the
elements divisible by 3, that is to say 3, 6, 9, 15, . . . and divide through by 3 to obtain
the new sequence 1, 2, 3, 5, . . . . This is now well-distributed modulo both 2 and 3.

The process may be continued with the primes up to some threshold w(N). Choosing
w(N) to tend to inﬁnity with N, the resulting sequences have no appreciable biases in
small modulo small numbers.

It is in fact quite easy to formalise this idea and to see how it may be applied to quite
general problems such as (3.5). The sequences that result from the sieving process we
have just described are of the form

{n : W n + b is prime}

where W := 2 × 3 × · · · × w(N) (hence the name ‘W -trick’) and (b, W ) = 1. For
consideration of the weighted sum appearing in (3.5) it is rather natural to introduce
the functions
 Λb,W (n) := φ(W )
W Λ(W n + b),

which have average value roughly 1. Roughly speaking, the sum in (3.5) may be split
into φ(W )t sums of the form
∑ Λb1,W ( ˜ψ1(⃗n)) . . . Λbt,W ( ˜ψd(⃗n)) (3.6)

(for the details of this decomposition see [24, Chapter 5]). One might then attempt to
evaluate each of these by splitting

Λbi,W = 1 + (Λbi,W − 1)

and then apply Proposition 3.0.7 to show that all of the terms except that with f1 =
· · · = ft = 1 are negligible.

Such an approach is promising, but there is one serious additional problem. Proposition
3.0.7 only applied, as we stated it, to functions fi which are bounded by 1. The functions
Λbi,W − 1 are certainly not bounded by one. Indeed, the harmonic analysis argument
leading up to (3.4) relied on this boundedness in a rather essential way.

It turns out that there is a version of Proposition 3.0.7 which applies to functions which
are not necessarily bounded by 1; this is one of the main results of [24], and the key
idea was also an important component of our earlier work [21].

For simplicity let us think about the von Mangoldt function Λ itself, rather than the
‘W-tricked’ variants Λb,W . Let R = N γ, where γ ∈ (0, 1) is a real number, and let us
recall the discussion of §1, where we observed that

THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 33

1
(log R)2 Λ2
R(n) = ( ∑

d|n
d⩽R
 λGY
d )2

is a sensible majorant for the characteristic function of the primes between R and N,
where
 λGY
d := µ(d) log(R/d)
log R .

It follows the function
 ν(n) := 1
log N ( ∑

d|n
d⩽R
 λGY
d )2

essentially majorizes some multiple CγΛ(n) of the von Mangoldt function on the interval
[N] (where by essentially we mean that there may be problems when n ⩽ R or n is a
prime power, but these are highly unimportant exceptions). We note that the link we
have just made to the work of Goldston, Pintz and Yıldırım is by no means artiﬁcial;
indeed a crucial moment in the development of [21] occurred when Andrew Granville
drew our attention to [9].

The weights ν are much more ﬂexible than Λ, since it is possible to evaluate such sums
as En⩽N ν(n)ν(n + 2)

asymptotically by variants of the computations leading to (1.3). As in those computa-
tions the key feature is that by choosing the parameter γ to be small enough the number
of terms which result from expanding out the sums over d is small enough that error
terms do not dominate.

In fact (after an application of the W -trick discussed above and with an appropriate
choice of γ = γ(t, d)) the weights are suﬃciently ﬂexible that they may be shown to
satisfy two technical conditions called the linear forms and correlation conditions. These
conditions were introduced in [21, §3], and the variants of these conditions appropriate
for a discussion of Dickson’s Conjecture are given in [24, §6]. As a result of this the
weight ν qualiﬁes to be called pseudorandom.

As the reader may have guessed from the above discussion, it is possible to prove a
version of Proposition 3.0.7 in which the condition that the fi take values in [−1, 1] is
relaxed to a condition |fi(x)| ⩽ ν(x), where ν is a pseudorandom weight function. The
ﬁrst step is to establish ‘generalized von Neumann’-type results in which the functions
fi are bounded by ν, rather than just by 1. Speciﬁcally, one deduces from an assump-
tion (3.1) that each of the Gowers norms ∥fi∥U 2 is somewhat large. This is once again
accomplished by several applications of the Cauchy-Schwarz inequality, but the pres-
ence of the weight ν makes the details even more complicated. For a fully worked-out
example, see [21, §5]. Once this is done one must establish an inverse theorem for the
Gowers U 2-norm for functions f with |f (x)| ⩽ ν(x). As we remarked, some new ideas
are required here since the harmonic analysis argument leading up to (3.4) breaks down
if f is not bounded by one.

34 BEN GREEN

In fact this inverse theorem is deduced from the version with |fi(x)| ⩽ 1 by means of
the following decomposition result, which is [24, Proposition 10.3].

Lemma 3.0.8 (Decomposition). Suppose that ν : Z/NZ → R⩾0 is a pseudorandom
measure, and that f : Z/NZ → R is a function with |f (x)| ⩽ ν(x) for all x. Then we
may decompose f = f1 + f2
where |f1(x)| ⩽ 1 for all x and ∥f2∥U2 = o(1) as N → ∞.

We shall almost nothing about the proof of this result, but it is also one of the key
ingredients in [21]. For a discussion, see [43, §6]. For a broader discussion of the
‘energy-increment’ strategy used in the proof, which appears in many diﬀerent contexts
in additive combinatorics, see [45].

Suppose that |f (x)| ⩽ ν(x) and that ∥f ∥U 2 ⩾ δ. Applying Lemma 3.0.8, we see that
∥f1∥U 2 ⩾ δ/2. By the inverse theorem for the U 2-norm of bounded functions, there is
some r ∈ Z/NZ such that
 |En∈Z/N Zf1(n)e(−rn/N)| ⩾ δ2/4.

However by the converse of the inverse theorem and the fact that ∥f2∥U 2 = o(1) we see
that |En∈Z/N Zf2(n)e(−rn/N)| = o(1)
(Note that the proof of this converse result did not require f2 to be bounded by 1). By
the triangle inequality it follows that

|En∈Z/N Zf (n)e(−rn/N)| ⩾ δ2/4 − o(1) ⩾ δ2/8,

which concludes the ‘transference’ of the inverse theorem for the U 2-norm from functions
bounded by 1 to functions bounded by ν.

Let us take stock of our position. We have indicated a proof of Proposition 3.0.7 when
the functions fi are bounded by a pseudorandom weight ν, a fairly robust realisation
of the principle that harmonic analysis governs the behaviour of systems of complexity
one. We have split the von Mangoldt function Λ into functions Λb,W , and rewritten the
sum which interests us, namely (3.5), as a sum of expressions of the form (3.6). To
evaluate these we eﬀect the further splitting Λb,W = 1 + (Λb,W − 1), and hope to show
that any sum ∑ f1( ˜ψ1(⃗n)) . . . ft( ˜ψt(⃗n))

in which at least one fi equals Λb,W −1 is negligible. All of these functions are essentially
dominated by some pseudorandom weight ν of the type considered by Goldston and
Yıldırım, and so by our robust version of Proposition 3.0.7 it suﬃces to rule out the
possiblity that Λb,W − 1 correlates with a linear phase function; that is to say, we must
establish that |En⩽N (Λb,W (n) − 1)e(−rn/N)| = o(1). (3.7)

This estimate may be established in a fairly classical fashion using the ideas of Hardy,
Littlewood and Vinogradov. In [24] we proceed by ﬁrst eﬀecting some further decom-
positions, in keeping with our general philosophy that problems should be ‘transferred’

THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 35

to a situation where functions are bounded by 1. We skip the details (which may be
found in [24, §12]) and merely state that (3.7) can be deduced from the estimate

|En⩽N µ(n)e(−rn/N)| ≪A log−A N, (3.8)

for some suitably large A. That such an estimate holds (with any A) is a well-known
result of Davenport [5]. To prove it one may use the method of Type I/Type II sums dis-
cussed in §2. In fact, Propositon 2.3.1 is true with the von Mangoldt function Λ replaced
by the M¨obius function µ. The proof is almost the same, relying on a decomposition of
µ which is very similar to Vaughan’s decomposition of Λ.

The remarks following the statement of Proposition 2.3.1 are particularly relevant here.
We can hope that the method of Type I/II sums will be eﬀective in bounding (3.8)
unless r/N is approximately a/q, for some small q (that is, the method ought to be
successful in the ‘minor arc’ case). Luckily in the ‘major arc’ case one may approximate
e(−rn/N) by the sum of a few Dirichlet characters to modulus q. The resulting sums∑

n⩽N µ(n)χ(n) may then be estimating using standard techniques of analytic number
theory together with information about the non-existence of zeros near ℜs = 1 of the
L-functions L(s, χ): for details see [32, Prop 5.29].

This concludes our discussion of a proof of Dickson’s Conjecture for systems of com-
plexity one. As we have remarked, this result could also be obtained by a more classical
application of the circle method. However it turns out that large parts of our discussion
adapt very painlessly to systems of complexity s > 1, whereas this does not seem to be
the case for the classical techniques.

One has, for example, the following bound of generalized von Neumann type:

|E⃗n∈(Z/N Z)d f1(ψ1(⃗n)) . . . ft(ψt(⃗n))| ⩽ inf
i∈[t] ∥fi∥U s+1 (3.9)

for systems ψ1, . . . , ψt of complexity s, where ∥f ∥U k is the Gowers U k-norm of f and is
deﬁned by
 ∥f ∥2k
U k := Ex,h1,...,hk ∏

ω1,...,ωk∈{0,1} f (x + ω1h1 + · · · + ωkhk)

(with complex conjugates being taken of the terms with an odd number of his). This is
true even if the functions fi are only bounded by a pseudorandom weight ν. A statement
very close to (3.9) is proved in [24, Appendix C].

The decomposition result, Lemma 3.0.8, also adapts in a fairly painless manner.

The ﬁrst really serious issue that we encounter is in ﬁnding a generalization of the inverse
theorem for the U 2-norm. If f : Z/NZ → [−1, 1] is a function such that ∥f ∥U 3 ⩾ δ,
what can be said? The most immediate diﬃculty with attacking this statement is the
lack of a suitable formula generalizing the relation ∥f ∥U 2 = ∥ ˆf ∥4. A more decisive
problem is revealed by consideration of the function f (n) = e(n
2/N). One may check
that ∥f ∥U 3 = 1 (this is essentially a manifestation of the fact that the third derivative
of a quadratic is zero). With somewhat more eﬀort one may check that this f does
not have substantial correlation with a linear exponential e(rn/N). Thus an inverse

36 BEN GREEN

theorem for the U 3-norm must encode some kind of ‘higher harmonic analysis’ which
takes account of these quadratic phases as well as just linear ones. The situation is
further complicated by the existence of further examples, such as f (n) = e(n[n
√2]/N),
for which ∥f ∥U 3 is large, but for which f does not even exhibit genuine quadratic
behaviour. A full discussion of examples related to these may be found in [17].

It turns out that these two examples, f (n) = e(n
2/N) and f (n) = e(n[n
√2]/N), can
both be interpreted as objects living on a 2-step nilmanifold, that is to say a quotient
G/Γ where G is a 2-step nilpotent Lie group and Γ is a discrete and cocompact subgroup.
The archetypal example is the Heisenberg example in which

G = ( 1 R R
0 1 R
0 0 1
 ) and Γ = ( 1 Z Z
0 1 Z
0 0 1
 ) .

Quadratic polynomials appear quite naturally in such a group G, for instance in the
computation ( 1 α β
0 1 γ
0 0 1
 )n = ( 1 nα nβ+ 1
2 n(n−1)αγ
0 1 nγ
0 0 1
 ) .

Taking such a sequence of matrices and postmultiplying by elements of Γ so that all
of the entries lie between [−1/2, 1/2]3 (that is, reducing to a fundamental domain for
the action of Γ on G) one soon sees the appearance of the more complicated ‘bracket
quadratics’ γn[αn] too. A fuller discussion, with motivating remarks, may be found in
[17].

What is more, correlation with an example arising in this setting is the only way in
which a function f can have large U 3-norm. This is the inverse theorem for the U 3-
norm, proved in [22] building on ideas of Gowers [15]. It is conjectured that an analogous
result holds for the U s+1-norm in general, a conjecture we refer to as the Gowers Inverse
conjecture GI(s).

Conjecture 3.0.9 (Gowers inverse conjecture GI(s)). Suppose that f : Z/NZ → [−1, 1]
is a function and that ∥f ∥U s+1 ⩾ δ. Then there is an s-step nilmanifold G/Γ, a Lipschitz
function F : G/Γ → [−1, 1] and elements g ∈ G, x ∈ G/Γ such that

|En⩽N f (n)F (gnxΓ)| ≫δ 1.

The dimension and complexity of G/Γ and the Lipschitz constant of F are all Oδ(1).

The function n ↦→ F (gnxΓ) is called an s-step nilsequence. To state this conjecture
properly one must of course deﬁne the notion of ‘complexity’, and also assign a metric
to G/Γ so that the notion of Lipschitz constant may be properly formalised. A version
of the conjecture was ﬁrst formulated in [24, §8]. There, a metric on G/Γ was assigned
quite arbitrarily. With the beneﬁt of hindsight it is probably better to proceed as in our
more recent paper [25, §2], in which the notions of ‘complexity’ and ‘metric’ are both
developed from the notion of a Mal’cev basis for G/Γ.

The precise statements are not important in order to understand the philosophy which
lies behind Conjecture 3.0.9 and its interplay with the generalized von Neumann the-
orem (3.9): it seems as though the correct ‘harmonics’ with which to study systems
{ψ1, . . . , ψt} of complexity s are the s-step nilsequences.

THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 37

Conjecture 3.0.9 is known when s = 1, and we proved it earlier. Note that the linear
exponentials n ↦→ e(−rn/N) may easily be interpreted as 1-step nilsequences living on
the nilmanifold R/Z. As we stated, it is also known when s = 2, this being the main
result of [22]. Tao and I hope to report progress on the general case s ⩾ 3 in the near
future.

Assuming Conjecture 3.0.9, one may start to work through the proof of Dickson’s Con-
jecture in the complexity 1 case and attempt to generalise it to the complexity s sit-
uation. Replacing occurrences of linear exponentials e(−rn/N) by s-step nilsequences
F (gnxΓ), the argument runs with remarkably few changes. One fairly signiﬁcant extra
diﬃculty occurs in the proof of Lemma 3.0.8, where a ‘converse’ to the inverse conjecture
is required. Namely, one needs to know that if

|En⩽N f (n)F (gnxΓ)| ⩾ δ

for some s-step nilsequence F (gnxΓ) then

∥f ∥U s+1 ≫δ 1,

where the implied constant may also depend on the complexity of G/Γ and on the
Lipschitz constant of F . Such a result is already present in [22, §14], and a somewhat
more conceptual proof is given in [24, Appendix E]. Both of these appendices were based
on extensive conversations with members of the ergodic theory community.

By far the most serious obstacle is the last one, where we reduce to establishing a
generalization of (3.8) for nilsequences. In other words we seek the bound

|En⩽N µ(n)F (gnxΓ)| ≪A log−A N

for all A > 0, where F (gnxΓ) is an s-step nilsequence arising from some s-step nilman-
ifold G/Γ, and the implied constant may also depend on the complexity of G/Γ and
the Lipschitz constant of F . This bound is referred to as the M¨obius and Nilsequences
Conjecture MN(s). As we remarked, the conjecture MN(1) was essentially established
by Davenport. The case MN(2) was obtained in the paper [23]. The general case MN(s)
has recently been resolved by the authors and will appear in the short paper [26]; the
key technical ingredient in that proof is the main result of [25], which may be thought
of as a kind of generalization of the major-minor arc decomposition to nilsequences of
arbitrary step. The method of Type I/II sums is crucial once more.

The reader wishing to study any of this work might ﬁnd the following table helpful. Let
me once again emphasise that the purpose of this article has been to guide potential
readers through the papers [21, 22, 23, 24, 25] and [26]; we do not intend to suggest
that there is no other work going on in the subject!

[21], The primes contain arbitrarily long arithmetic progressions, independent of the
other papers except it contains the proof of Decomposition Lemma 3.0.8.

[22], An inverse theorem for the Gowers U 3-norm, with applications, proof of the GI(2)
conjecture.

38 BEN GREEN

[23], Quadratic Uniformity of the M¨obius function, proof of the MN(2) conjecture, to
be largely superceded by [26] but, unlike that paper, can be understood without [25].

[24], Linear Equations in primes, proof that the GI(s) and MN(s) conjectures together
imply Dickson’s conjecture for systems {ψ1, . . . , ψt} of complexity s. The discussion in
this article has been largely an exposition of some of the ideas in this paper.

[25], The Quantitative Behaviour of Polynomial Orbits on Nilmanifolds, key technical
ingredient for studying nilsequences

[26], The M¨obius and Nilsequences Conjectures, proof of MN(s) conjecture for all s,
heavily reliant on [25].
 References

[1] Problems from the ARCC Workshop “Gaps between primes”, ed. A. Kumchev, available at
http://www.aimath.org/WWN/primegaps/primegaps.pdf.
[2] M. Agwaral, N. Kayal and N. Saxena, PRIMES is in P, Ann. Math. 160 (2004), 781–793.
[3] A. Balog, Linear equations in primes, Mathematika 39 (1992), no. 2, 367–378.
[4] E. Bombieri and H. Davenport, Small diﬀerences between prime numbers, Proc. Roy. Soc. Ser. A
293 (1966), 1–18.
[5] H. Davenport, On some inﬁnite series involving arithmetical functions, II, Quart. J. Math. Oxford
8 (1937), 313–320.
[6] W. Duke, J. B. Friedlander and H. Iwaniec, Equidistribution of roots of a quadratic congruence to
prime moduli, Ann. of Math. (2) 141 (1995), no. 2, 423–441.
[7] P.D.T.A Elliott and H. Halberstam, A conjecture in prime number theory, Symposia Mathematica
4 (INDAM, Rome, 1968/69) 59–72, Academic Press, London.
[8] P. Erd˝os, The diﬀerence of consecutive primes, Duke Math. J. 6 (1940), 438–441.
[9] D. Goldston and C. Y. Yıldırım , Small gaps between primes, I, available at
http://www.arxiv.org/abs/math/0504336.
[10] D. A. Goldston, J. Pintz and C. Y. Yıldırım, Primes in tuples II, in preparation.
[11] D. A. Goldston, S. W. Graham, J. Pintz and C. Y. Yıldırım, Small gaps between primes or almost
primes, preprint available at http://www.arxiv.org/abs/math/0506067.
[12] D. A. Goldston, J. Pintz and C. Y. Yıldırım, The path to recent progress on small gaps between
primes, preprint available at http://www.arxiv.org/abs/math/0512436.
[13] D. A. Goldston, J. Pintz and C. Y. Yıldırım, Primes in tuples I, preprint available at
http://www.arxiv.org/abs/math/0508185.
[14] D. A. Goldston, Y. Motohashi, J. Pintz and C. Y. Yıldırım, Small gaps between primes exist,
preprint available at http://www.arxiv.org/abs/math/0505300.
[15] W. T. Gowers, A new proof of Szemer´edi’s theorem for arithmetic progressions of length four,
Geom. Funct. Anal. 8 (1998), no. 3, 529–551.
[16] A. Granville, A good new millenium for the primes, The Madrid Intelligencer (2006) pages 32–36.
Also available on the author’s webpage.
[17] B. J. Green, Generalizing the Hardy-Littlewood method for primes, Proceedings of the International
Congress of Mathematicians 2006 (Madrid), vol. 2,
[18] , Montr´eal Lecture notes on Quadratic Fourier Analysis, to appear in Proceedings of the
CMS-Clay School on Additive Combinatorics, Montr´eal 2006.
[19] , Long arithmetic progressions of primes, in Analytic Number Theory: A tribute to Gauss
and Dirichlet, CMI/AMS 2007.
[20] B. J. Green and T. C. Tao, Restriction theory of the Selberg sieve, with applications, Jour. Th.
Nombres Bordeaux 18 (2006), 147–182.

THREE TOPICS IN ADDITIVE PRIME NUMBER THEORY 39

[21] , The primes contain arbitrarily long arithmetic progressions, to appear in Ann. Math.,
preprint available at http://www.arxiv.org/abs/math/0404188.
[22] , An inverse theorem for the Gowers U 3-norm, with applications, to appear in Proc. Edin-
burgh Math. Soc, preprint available at http://www.arxiv.org/abs/math/0503014.
[23] , Quadratic Uniformity of the M¨obius function, to appear in Annales de l’Institut Fourier,
Grenoble, preprint available at http://www.arxiv.org/abs/math/0606087.
[24] , Linear Equations in primes, to appear in Ann. Math, preprint available at
http://www.arxiv.org/abs/math/0606088.
[25] , The Quantitative Behaviour of Polynomial Orbits on Nilmanifolds, preprint available at
http://www.arxiv.org/abs/0709.3562.
[26] , The M¨obius and Nilsequences Conjectures, in preparation.
[27] G. H. Hardy and J. E. Littlewood, unpublished manuscript, see [39].
[28] B. Host, Progressions arithm´etiques dans les nombres premiers, d’apr`es B. Green et T. Tao,
Seminaire Bourbaki,Mars 2005, 57eme annee, 2004-2005, no. 944.
[29] M. N. Huxley, On the diﬀerences of primes in arithmetical progressions, Acta Arith. 15 (1968/69),
367–392.
[30] , Small diﬀerences between consecutive primes II, Mathematika 24 (1977), 142–152.
[31] , An application of the Fouvry-Iwaniec theorem, Acta Arith. 43 (1984), 441–443.
[32] H. Iwaniec and E. Kowalski, Analytic number theory, AMS Colloq. Math. 53, Providence RI 2004.
[33] B. Kra, The Green-Tao theorem on arithmetic progressions in the primes: an ergodic point of
view, Bull. Amer. Math. Soc. (N.S.) 43 (2006), no. 1, 3–23.
[34] A. V. Kumchev, A. V. and D. I. Tolev, An invitation to additive prime number theory, Serdica
Math. J. 31 (2005), no. 1-2, 1–74.
[35] H. Maier, Small diﬀerences between prime numbers, Michigan Math. J. 35 (1988), 323–344.
[36] C. Mauduit et J. Rivat, Sur un probl´eme de Gelfond: la somme des chiﬀres des nombres premiers,
preprint.
[37] M. B. Nathanson, Additive number theory: The classical bases, Graduate Texts in Mathematics
164. Springer-Verlag, New York, 1996. xiv+342 pp.
[38] G. Z. Pilt’ai, On the size of the diﬀerence between consecutive primes, Issledovania po teorii chisel,
4 (1972), 73–79.
[39] R. A. Rankin, The diﬀerence between consecutive prime numbers. II, Proc. Cambridge Philos.
Soc. 36 (1940), 255–266.
[40] G. Ricci, Sull’andamento della diﬀerenza di numeri primi consecutivi, Riv. Mat. Univ. Parma 5
(1954), 3–54.
[41] K. Soundararajan, Small gaps between prime numbers: The work of Goldston-Pintz-Yıldırım, Bull.
Amer. Math. Soc. 44 (2007), 1–18.
[42] T. C. Tao, The dichotomy between structure and randomness, arithmetic progressions, and the
primes, Proceedings of the International Congress of Mathematicians, Madrid 2006, Vol. I., 581–
608.
[43] , Obstructions to uniformity, and arithmetic patterns in the primes Quarterly J. Pure Appl.
Math. 2 (2006), 199-217 [Special issue in honour of John H. Coates, Vol. 1 of 2]
[44] , Arithmetic progressions and the primes, El Escorial lectures, Collectanea Mathematica
(2006), Vol. Extra., 37-88. [Proceedings, 7th International Conference on Harmonic Analysis and
Partial Diﬀerential Equations]
[45] , Structure and randomness in combinatorics, submitted to FOCS (Foundations of Com-
puter Science) 2007.
[46] T. C. Tao and V. H. Vu, Additive Combinatorics, Cambridge Studies in Advanced Mathematics
105, CUP 2006.
[47] S. Uchiyama, On the diﬀerence between consecutive prime numbers, Acta Arith. 27 (1975), 153–
157.
[48] R. C. Vaughan, Sommes trigonom´etriques sur les nombres premiers, C. R. Acad. Sci. Paris S´er.
A-B 285 (1977), no. 16, A981–A983.

40 BEN GREEN

Centre for Mathematical Sciences, Wilberforce Road, Cambridge CB3 0WA, England

E-mail address: b.j.green@dpmms.cam.ac.uk
