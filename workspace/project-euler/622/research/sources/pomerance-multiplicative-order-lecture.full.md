<!-- source: https://math.dartmouth.edu/~carlp/ordertalk.pdf | converted from PDF -->

The multiplicative order mod n,

on average

Carl Pomerance, Dartmouth College
Hanover, New Hampshire, USA

(Joint work with: Michel Balazard, P¨ar Kurlberg)

Perfect shuﬄes

Suppose you take a deck of 52 cards, cut it in half, and
perfectly shuﬄe it (with the bottom card staying on the
bottom).

If this is done 8 times, the deck returns to the order it was in
before the ﬁrst shuﬄe.

But, if you include the 2 jokers, so there are 54 cards, then it
takes 52 shuﬄes, while a deck of 50 cards takes 21 shuﬄes.

What’s going on?
 1

For an odd number n, let l(n) = l2(n) denote the mutliplicative
order of 2 in (Z/nZ)×. Note that

l(51) = 8, l(53) = 52, l(49) = 21.

In fact, it is not hard to prove that the number of perfect
shuﬄes to return a deck of 2n cards to it’s initial order is
l(2n − 1).

(Number the cards 0 to 2n − 1, with 0 the bottom card. Then
a perfect shuﬄe takes a card in position i and sends it to
2i mod 2n − 1.)
 2

This function l(n) (= the multiplicative order of 2 mod n)
appears to be very erratic and diﬃcult to get hold of. It is of
interest not only in card shuﬄing, but in computing the periods
of certain pseudo-random number generators, and in other
cryptographic contexts.

Further, as a basic and ubiquitous number-theoretic function it
seems interesting to study l(n), and more generally la(n) (the
order of a in (Z/nZ)×) from a statistical viewpoint.

What is it normally?

What is it on average?
 3

One elementary result that goes back to Gauss and Carmichael
is that la(n) | λ(n).

Here λ(n) is the order of the largest cyclic subgroup in (Z/nZ)×

and is deﬁned by

λ([m, n]) = [λ(m), λ(n)], λ(pα) = ϕ(pα)

for odd primes p and pα = 2 or 4, and λ(2α) = 2α−2 for α ≥ 3.

For λ, we do have results about it’s normal and average order,
and they are a far cry from a possible ﬁrst guess, the normal
and average orders of ϕ.
 4

Erd˝os, P, Schmutz: On a set of asymptotic density 1,

λ(n) = n/(log n)log log log n+A+o(1)

for a certain explicit positive constant A.

Erd˝os, P, Schmutz: As x → ∞,

1
x
 ∑

n≤x λ(n) = x
log x exp
 ((B + o(1)) log log x
log log log x
 )

for a certain explicit positive constant B.
 5

Further, we know (assuming the Generalized Riemann
Hypothesis for the Galois closures of Kummerian ﬁelds) that for
most n coprime to a, we have λ(n)/la(n) small. (Results of Li,
Kurlberg, and Li & P.)

Thus, one has
 la(n) = n/(log n)log log log n+A+o(1)

for almost all n coprime to a.

Clearly the average order of λ(n), which is of greater
magnitude than n/ log n, is much larger than the normal order,
so the average is determined by a thin set of numbers with
abnormally large values of λ. Thus, it is unclear what is
happening with the average order of la(n).
 6

After some numerical experiments, V. I. Arnold recently
concluded that on average la(n) is Can/ log n, and he gave a
heuristic argument for this based on the physical principle of
turbulence. This is in the paper

Number-theoretical turbulence in Fermat–Euler arithmetics and
large Young diagrams geometry statistics, Journal of Fluid
Mechanics 7 (2005), S4–S50.

It also was the subject of one the Chern Lectures he gave at
UC Berkeley in 2007.
 7

Arnold writes in the abstract:

“Many stochastic phenomena in deterministic mathematics had
been discovered recently by the experimental way, imitating
Kolmogorov’s semi-empirical methods of discovery of the
turbulence laws. From the deductive mathematics point of view
most of these results are not theorems, being only descriptions
of several millions of particular observations. However, I hope
that they are even more important than the formal deductions
from the formal axioms, providing new points of view on
diﬃcult problems where no other approaches are that eﬃcient.”

And he asserts that his expression Can/ log n for the average
order of la(n) is in fact supported by billions of experiments.

8

I think we should be a bit suspicious!

First, iterated logarithms grow so slowly that they are diﬃcult
to detect numerically.

Second, Arnold did not seem to investigate any of the
(admittedly scant) literature dealing with la(n). In fact, there
are interesting papers on the subject going back to Romanoﬀ
(who proved that the sum of 1/(nla(n)) for n coprime to a is
convergent), with later papers by Erd˝os, P, Pappalardi, Li,
Kurlberg, Murty, Rosen, Silverman, Saidak, Moree, Luca,
Shparlinski, and others.
 9

But. . .

It’s good to have outsiders investigate a ﬁeld, and if they were
expected to ﬁrst read the literature thoroughly, it might
dampen the fresh insight they might bring.

And, his conjecture that the average order of l(n) grows like
n/ log n is supported on one side by Hooley’s GRH-conditional
proof of Artin’s conjecture. Thus, assuming the GRH, a
positive proportion of primes p have l(p) = p − 1, so that just
the contribution of primes to the sum of l(n) gives an average
order that is ≫ n/ log n. And perhaps composites do not
contribute too much.

However. . .
 10

Shparlinski (2007): Let |a| > 1. Assuming the GRH, there is
some Ca > 0 with

1
x
 ∑

n≤x
(a,n)=1
 la(n) ≫ x
log x exp (
Ca(log log log x)3/2) .

(On some dynamical systems in ﬁnite ﬁelds and residue rings,
Discrete and continuous dynamical systems, Series A 17
(2007), 901–917.)

And he suggests that with more work, the exponent “3/2”
might possibly be replaced with “2”.
 11

Balazard, Kurlberg, P: Let |a| > 1. Assuming the GRH,

1
x
 ∑

n≤x
(a,n)=1
 la(n) = x
log x exp
 ((B + o(1)) log log x
log log log x
 )
 .

Here “B” is the same constant that appears in the average
order of λ(n), namely

B = e−γ ∏

p
 (

1 − 1
(p − 1)2(p + 1)
)
 = 0.3453720641 . . . .

In particular, the upper bound in the theorem holds
unconditionally.
 12

The proof is a bit intense, borrowing heavily from the structure
of the proof in Erd˝os, P, & Schmutz of the corresponding
result for λ(n).

However, the following lemma is also used:

Kurlberg & P (2005): For 1 ≤ y ≤ log x/ log log x

{p ≤ x : la(p) < p/y} ≪ π(x)
y .

This result follows essentially from the the Hooley GRH
conditional proof of Artin’s primitive-root conjecture.
(Pappalardi (1996) had this result in a wider range for y, but it
has been retracted. Kurlberg (2003) had this result in the
range y ≤ (log x)1−ε.)
 13

Probably better suited for presentation in a talk is a proof of
the following result from Balazard, Kurlberg, & P:

Assume the GRH. The average order of l(p) is 159
160cp, where

c = ∏

p
 (

1 − p
p3 − 1
)
 .

(Note that 159
160c = 0.57236022 . . . , so that on average,
l(p) > 4
7p.)

Luca (2002) has shown that for averaging the orders of all
elements of (Z/pZ)×, this statistic has average order cp.
 14

For an odd prime p, let i(p) = (p − 1)/l(p), namely the index of
the subgroup ⟨2⟩ in (Z/pZ)×. Let z be some parameter tending
to inﬁnity that we will specify later. We have

∑

p≤x l(p) = ∑

p≤x
i(p)≤z
 l(p) + ∑

p≤x
i(p)>z
 l(p) = A + B,

say. Further, if z ≤ log x/ log log x, then the Kurlberg–P lemma
implies
 B ≪ x
z · π(x)
z = xπ(x)
z2 ,

which is o(xπ(x)) provided z → ∞. (A trivial argument shows
that B < xπ(x)/z, which is good enough for our purposes.)

15

Now, for the main term A we might use known results for the
distribution of primes p where i(p) is ﬁxed at some number, but
it seems simpler to use an inclusion–exclusion:

A = ∑

p≤x
i(p)≤z
(p − 1) ∑

uv|i(p)
 µ(v)
u .

We write this as C − D, where in C we drop the condition
i(p) ≤ z, but assume uv ≤ z, while in D we assume that i(p) > z
and uv ≤ z.

For D we majorize trivially (replace µ(v) with 1) and use the
Kurlberg–P lemma. For z < i(p) < z2, we get xπ(x)/z1−o(1) and
for i(p) ≥ z2, we get xπ(x)(log log x)/z.
 16

This leaves the main term

C = ∑

p≤x
(p − 1) ∑

uv|i(p)
uv≤z
 µ(v)
u = ∑

uv≤z
 µ(v)
u
 ∑

p≤x
uv|i(p)
(p − 1).

For a given value of uv ≤ z, we can compute the inner sum by
partial summation and a GRH-conditional result in Hooley,
getting
 xπ(x)
2uvϕ(uv) + O
 ( x2

log2 x
)

if 8 ∤ uv and twice this if 8 | uv. (If z ≤ (log x)1/7, say, we have
this unconditionally, but we needed the GRH to estimate the
error term D.)
 17

Thus, the main term is

C = 1
2xπ(x)
 






 ∑

uv≤z
 µ(v)
u2vϕ(uv) + ∑

uv≤z
8|uv
 µ(v)
u2vϕ(uv)






 + O
 (x2z log z
log2 x
 )
 .

So we see that a convenient choice of z is say (log x)1/2. For
the main term, we consider the expressions as inﬁnite sums,
estimate the errors in truncation, and then rewrite the inﬁnite
sums as Euler products. We get:

1
π(x)
 ∑

2<p≤x l(p) = 159
320cx + O
 ( x

(log x)1/2−ε
)
 .
 □

18
