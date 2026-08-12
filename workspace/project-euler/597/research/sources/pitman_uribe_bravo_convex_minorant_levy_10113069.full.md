<!-- source: https://arxiv.org/pdf/1011.3069 | converted from PDF -->

arXiv:1011.3069v3  [math.PR]  30 Jul 2012
The Annals of Probability
2012, Vol. 40, No. 4, 1636–1674
DOI: 10.1214/11-AOP658
c⃝ Institute of Mathematical Statistics, 2012

THE CONVEX MINORANT OF A L´EVY PROCESS

By Jim Pitman1 and Ger´onimo Uribe Bravo2

University of California, Berkeley

We oﬀer a uniﬁed approach to the theory of convex minorants
of L´evy processes with continuous distributions. New results include
simple explicit constructions of the convex minorant of a L´evy process
on both ﬁnite and inﬁnite time intervals, and of a Poisson point pro-
cess of excursions above the convex minorant up to an independent
exponential time. The Poisson–Dirichlet distribution of parameter 1
is shown to be the universal law of ranked lengths of excursions of
a L´evy process with continuous distributions above its convex mino-
rant on the interval [0, 1].

1. Introduction. We present simple explicit constructions of the convex
minorant of a L´evy process with continuous distributions on both ﬁnite
and inﬁnite time intervals, and of a Poisson point process of excursions of
the L´evy process above its convex minorant. These constructions bridge
a number of gaps in the literature by relating combinatorial approaches to
ﬂuctuation theory of random walks related to the cycle structure of random
permutations, dating back to the 1950s [cf. Andersen (1950, 1953a, 1953b,
1954); Spitzer (1956)], some features of which were extended to interval
partitions associated with the convex minorant of Brownian motion and
Brownian bridge by Suidan (2001a, 2001b) and Balabdaoui and Pitman
(2009), and results previously obtained for the convex minorants of Brownian
motion by Groeneboom (1983) and Pitman (1983), and for L´evy processes
by Nagasawa (2000) and Bertoin (2000). In particular, we gain access to the
excursions above the convex minorant, which were previously treated only
in the Brownian case by Groeneboom (1983) and Pitman (1983).

Received November 2010; revised February 2011.
1Supported in part by NSF Grant DMS-08-06118.
2Supported by a postdoctoral fellowship from UC MexUS—CoNaCyt and NSF Grant
DMS-08-06118.
MSC2010 subject classiﬁcation. 60G51.
Key words and phrases. L´evy processes, convex minorant, uniform stick-breaking, ﬂuc-
tuation theory, Vervaat transformation.

This is an electronic reprint of the original article published by the
Institute of Mathematical Statistics in The Annals of Probability,
2012, Vol. 40, No. 4, 1636–1674. This reprint diﬀers from the original in
pagination and typographic detail. 1

2 J. PITMAN AND G. URIBE BRAVO

Our work is part of a larger initiative to understand the convex mino-
rant of processes with exchangeable increments. The case of discrete time is
handled in Abramson and Pitman (2011), while Brownian motion is given
a more detailed study in Pitman and Ross (2010). Our joint ﬁndings are
summarized in Abramson et al. (2011).

1.1. Statement of results. Let X be a L´evy process. The following hy-
pothesis is used throughout the paper:

(CD) For all t > 0, Xt has a continuous distribution, meaning that for each
x ∈ R, P(Xt = x) = 0.

It is suﬃcient to assume that Xt has a continuous distribution for some t > 0.
Equivalently [Sato (1999), Theorem 27.4, page 175] X is not a compound
Poisson process with drift.
The convex minorant of a function f on an interval [0, t] or [0, ∞) is the
greatest convex function c satisfying c ≤ f . We shall only consider func-
tions f which are c`adl`ag, meaning that limh→0+ f (t + h) = f (t) and that
limh→0− f (t − h) exists; the latter limit will be denoted f (t−).
First properties of the convex minorant of a L´evy process, established in
Section 2 and which partially overlap with the Markovian study of convex
minorants in Lachieze-Rey (2009), are:

Proposition 1. Let X be a L´evy process which satisﬁes (CD) and C
the convex minorant of X on [0, t]. The following conditions hold almost
surely:

1. The open set O = {s ∈ (0, t) : Cs < Xs ∧ Xs−} has Lebesgue measure t.
2. For every component interval (g, d) of O, the jumps that X might have
at g and d have the same sign. When X has unbounded variation on ﬁnite
intervals, both jumps are zero.
3. If (g1, d1) and (g2, d2) are diﬀerent component intervals of O, then
their slopes diﬀer
 Cd1 − Cg1
d1 − g1 ̸= Cd2 − Cg2
d2 − g2 .

Let I be the set of connected components of O; we shall also call them
excursion intervals. Associated with each excursion interval (g, d) are the
vertices g and d, the length d − g, the increment Cd − Cg and the slope
(Cd − Cg)/(d − g).
Our main result is a simple description of the lengths and increments
of the excursion intervals of the convex minorant. Indeed, we will consider
a random ordering of them which uncovers a remarkable probabilistic struc-
ture.
 THE CONVEX MINORANT OF A L´EVY PROCESS 3

Theorem 1. Let (Ui) be a sequence of uniform random variables on
(0, t) independent of the L´evy process X which satisﬁes (CD). Let (g1, d1),
(g2, d2), . . . be the sequence of distinct excursion intervals which are succes-
sively discovered by the sequence (Ui). Consider another i.i.d. sequence (Vi)
of uniform random variables on (0, 1) independent of X, and construct the
associated uniform stick-breaking process L by

L1 = tV1 and for i ≥ 1 Li+1 = Vi+1(t − Si),

where
 S0 = 0 and for i ≥ 1 Si = L1 + · · · + Li.

Under hypothesis (CD), the following equality in distribution holds:

((di − gi, Cdi − Cgi), i ≥ 1) d
= ((Li, XSi − XSi−1), i ≥ 1).

The Poisson–Dirichlet distribution of parameter one is the law of the
decreasing rearrangement of the sequence L when t = 1. Theorem 1 implies
that the Poisson–Dirichlet distribution of parameter 1 is the universal distri-
bution of the ranked lengths of excursions intervals of the convex minorant of
a L´evy process with continuous distributions on [0, 1]. What diﬀers between
each L´evy process is the distribution of the order in which these lengths
appear, that is, the law of the composition of of [0, 1] induced by the lengths
of excursion intervals when they are taken in order of appearance. Using
Theorem 1 we can form a composition of [0, 1] with that law in the following
way. For each pair (Li, XSi − XSi−1) we generate a slope by dividing the
second coordinate, the increment, by the ﬁrst, the length, and then create
a composition of [0, 1] by arranging the sequence L in order of increasing
associated slope.
Note that the second sequence of Theorem 1 can also be constructed
as follows: given a uniform stick-breaking process L, create a sequence Yi
of random variables which are conditionally independent given L and such
that the law of Yi given L is that of XLi (X independent of L). Then

((Li, Yi) : i ≥ 1) d
= ((Li, XSi − XSi−1), i ≥ 1).

Theorem 1 provides a way to perform explicit computations. For example,
the intensity measure νt of the point process Ξt with atoms at

{(d − g, Cd − Cg) : (g, d) is an excursion interval}

is given by

νt(A) = E(∑

i 1(di−gi,Cdi −Cgi )∈A
)

= E(∑

i 1(Li,Xdi −Xgi )∈A
) = ∫ t

0
 ∫ 1A(l, x) 1
l P(Xl ∈ dx) dl.

4 J. PITMAN AND G. URIBE BRAVO

[This follows conditioning on L and then using the intensity measure of L
obtained by size-biased sampling; cf. formula (6) in Pitman and Yor (1997).]
We now apply Theorem 1 to fully describe the convex minorant of the
Cauchy process as ﬁrst done in Bertoin (2000). Let X be a Cauchy process
characterized by
 F (x) := P(X1 ≤ x) = 1/2 + arctan(x)/π.

Let C be the convex minorant of X on [0, 1] and D its right-hand derivative,

Dt = lim
h→0+ Ct+h − Ct
h .

Consider
 Ix = inf{t ≥ 0 : Dt > x} for x ∈ R.

Note that P(Xt < xt) = F (x) and that therefore, in the setting of Theorem 1,
the slopes (Cdi − Cgi)/(di − gi) are independent of the lengths di − gi. Also,
let T be a Gamma subordinator such that

E(e
−qTt) = ( 1
1 + q
 )t.

Corollary 1. 1. The symmetric Cauchy process is characterized by the
independence of lengths and slopes of excursions intervals on [0, 1].

2. (Ix, x ∈ R) and (TF (x)/T1, x ∈ R) have the same law.

Item 2 is due to Bertoin (2000), who used a technique allowing only the
study of the convex minorant of a Cauchy process on [0, 1].
Integrating Theorem 1, we obtain a description of the convex minorant
considered on the random interval [0, Tθ] where Tθ is a exponential random
variable of parameter θ independent of X.

Corollary 2. Let T be exponential of parameter θ and independent
of the L´evy process X which satisﬁes (CD). Let ΞT be the point process
with atoms at lengths and increments of excursion intervals of the convex
minorant of X on [0, T ]. Then ΞT is a Poisson point process with intensity

µθ(dt, dx) = e
−θt dt
t P(Xt ∈ dx).

By conditioning on T (which essentially reduces to inverting Laplace
transforms and underlies the analysis of the relationship between the Gamma
subordinator and the Poisson–Dirichlet distribution), we see that Theorem 1
can be deduced from Corollary 2. The latter can be deduced from the analy-
sis of the independence of pre- and post-minimum processes of a L´evy process
run until an independent exponential time found in Greenwood and Pitman

THE CONVEX MINORANT OF A L´EVY PROCESS 5

(1980). These relationships are discussed in Section 4, where we also explain
the results on ﬂuctuation theory for L´evy processes which are found in the lit-
erature and which can be deduced from our analysis of the convex minorant.
From Theorem 1 we can also derive the behavior of the convex minorant
of X on [0, ∞) as described for a Brownian motion by Groeneboom (1983)
and Pitman (1983) and for a L´evy process by Nagasawa (2000). Let Ξ∞
be the point process of lengths of excursion interval and increments of the
convex minorant on [0, ∞).

Corollary 3. The quantity l = lim inft→∞ Xt/t belongs to (−∞, ∞]
and is almost surely constant if and only if the convex minorant of X on
[0, ∞) is almost surely ﬁnite. In this case, under (CD), Ξ∞ is a Poisson
point process with intensity

µ∞(dt, dx) = 1x<lt
t P(Xt ∈ dx) dt.

Recall, for example, Kyprianou [(2006), Example 7.2], the strong law of
large numbers for L´evy processes, which says that if the expectation of X1
is deﬁned, then
 lim
t→∞ Xt
t = E(X1) almost surely.

Hence, if E(X −
1 ) < ∞, we can apply the second part of Corollary 3 with
l = E(X1). In the remaining case when E(X −
1 ) = E(X +
1 ) = ∞, let ν be the
L´evy measure of X and ν+ its right-tail given by

ν+(y) = ν((y, ∞)).

Erickson (1973) provides the necessary and suﬃcient for −∞ < l, which
implies that, actually, l = ∞,
∫

(−∞,0)
 |y|
ν+(|y|) ν(dy) < ∞

(see also Doney (2007), page 39, for a proof).
While it seems natural to ﬁrst study the convex minorant of a L´evy process
on [0, ∞), as was the approach of previous authors, the description of the
convex minorant with inﬁnite horizon is less complete, as it is necessarily
restricted to slopes a < l.
As another application, we can use the stick-breaking representation of
Theorem 1 to study the absolute continuity of the location and the value of
the minimum of the L´evy process on [0, 1]. Let

X t = min
s≤t Xs and ρt be such that Xρt ∧ Xρt− = X t.

(Recall that under (CD), the minimum of a L´evy process on [0, t] is attained
at an almost surely unique place ρt, as deduced from Theorem 1 since P(Xt =
0) = 0.)

6 J. PITMAN AND G. URIBE BRAVO

Theorem 2. Let X be a L´evy process such that 0 is regular for both
half-lines (−∞, 0) and (0, ∞). Then:

1. The distribution of ρ1 is equivalent to Lebesgue measure on [0, 1].
2. If Xt has an absolutely continuous distribution for each t > 0, then the
distribution of (ρ1, X 1) is equivalent to Lebesgue measure on (0, 1] × (0, ∞).
3. If Xt has an absolutely continuous distribution for each t > 0, then the
distribution of (X 1, X1 −X 1) is equivalent to Lebesgue measure on (−∞, 0)×
(0, ∞).

Chaumont (2010) also analyzes absolute continuity properties for the
supremum of a L´evy process on a ﬁxed interval using excursion theory for
the reﬂected L´evy process. The densities provided by Theorem 2 (more im-
portantly, the fact that they are almost surely positive) provide one way to
construct bridges of the L´evy process X conditioned to stay positive. With
these bridges, we can prove a generalization of Vervaat’s theorem relating the
Brownian bridge and the normalized Brownian excursion [Vervaat (1979),
Theorem 1] to a fairly general class of L´evy processes. Details are provided
in Uribe Bravo (2011).
Our next results will only consider convex minorants on a ﬁxed interval,
which we take to be [0, 1].
Theorem 1 gives a construction of the convex minorant by means of sam-
pling the L´evy process at the random, but independent, times of a uniform
stick-breaking process. Our second proof of it, which does not rely on ﬂuc-
tuation theory and gives insight into the excursions of X above its convex
minorant, depends on the use of the following path transformation. Let u
be an element of the excursion set O, and let (g, d) be the excursion interval
which contains u. We then deﬁne a new stochastic process X u = (X u
t )t≤1 by

X u
t =
 



 Xu+t − Xu, 0 ≤ t < d − u,
Cd − Cg + Xg+t−(d−u) − Xu, d − u ≤ t ≤ d − g,
Cd − Cg + Xt−(d−g), d − g ≤ t < d,
Xt, d ≤ t ≤ 1.

(1)

The idea for such a deﬁnition is that the graph of the convex minorant
of X u on [d−g, 1] can be obtained from the graph of C by removing (g, d) and
closing up the gap adjusting for continuity, while on [0, d− g], X u goes from 0
to Cd − Cg. (Property 2 of Proposition 1 is essential for the transformation to
work like this; see Figure 2.) A schematic picture of the path transformation
is found in Figure 1 for a typical Brownian motion path.
Theorem 1 then follows from the following invariance result. Indeed, by
applying the following path transformation recursively, we can obtain a size-
biased sample of the excursion intervals. In particular, the excursion interval
containing an independent uniform variable has a uniform length, which
begins to explain the stick-breaking process appearing in Theorem 1.

THE CONVEX MINORANT OF A L´EVY PROCESS 7

Fig. 1. Visualization of the path transformation X ↦→ X u applied to a Brownian motion
seen from its convex minorant.

Fig. 2. Visualization of the path transformation X ↦→ X u applied to a c`adl`ag path not
satisfying property 2 of Proposition 1.

Theorem 3. If U is a uniform on (0, 1) and independent of X and
hypothesis (CD) holds, the pairs (U, X) and (d − g, X U ) have the same law.

Proof of Theorem 3 will be based on the analogous random walk result
proved by Abramson and Pitman (2011) as well as analysis on Skorohod
space. Abraham and Pitman’s discrete time result is an exact invariance
property for a similar transformation applied to the polygonal approxima-
tion X n of X given by X n
t = X[nt]/n(⌈nt⌉/n − t) + X⌈nt⌉/n([nt]/n); that this
approximation does not converge in Skorohod space to X makes the passage
to the limit technical, although it simpliﬁes considerably for L´evy processes
with unbounded variation, and particularly so for L´evy processes with con-
tinuous sample paths. The discrete time result is combinatorial in nature
and related to permutations of the increments. Indeed, the discrete time
result is based on the fact that for a random walk S with continuous jump
distribution, the probability that S lies strictly above the line from (0, 0) to
(n, Sn) on {0, . . . , n} is known to be 1/n, and conditionally on this event,
the law of S can be related to a Vervaat-type transform of S. Hence, it
is not only possible to verify by combinatorial reasoning that the faces of
the convex minorant have the same law as the cycle lengths of a uniform
random permutation when both are placed in decreasing order, but also to
characterize the path fragments on top of each excursion interval.
Theorem 3 actually gives a much stronger result than Theorem 1 since
it grants access to the behavior of X between vertex points of the convex

8 J. PITMAN AND G. URIBE BRAVO

minorant. To see this, consider the Vervaat transformation: for each t > 0
and each c`adl`ag function f , let ρt = ρt(f ) be the location of the last mini-
mum f (t) of f on [0, t] and deﬁne

Vtf (s) = f (ρt + s mod t) − f (t) for s ∈ [0, t].

This path transformation was introduced in Vervaat (1979) for the Brownian
bridge; its connection to L´evy processes was further studied for stable L´evy
processes by Chaumont (1997), for spectrally positive L´evy processes in
Miermont (2001), and more general L´evy processes by Fourati (2005).
For each excursion interval (g, d) of O, associate an excursion e(g,d) given
by
 e
(g,d)(s) = Xg+s − Cg+s for s ∈ [0, d − g];

note that e(g,d)(0) is positive if Xg > Cg. Finally, recalling the setting of
Theorem 1, let K i be Knight’s bridge,

K i
s = X(Si−1+t) − XSi−1 − s XSi − XSi−1
Li , s ∈ [0, Li]

[the name is proposed because of remarkable universality theorems proven
for K i in Knight (1996)].

Theorem 4. The following equality in distribution holds under (CD):

((di − gi, Cdi − Cgi, e
(gi,di)), i ≥ 1) d
= ((Li, XSi − XSi−1, VLi(K i)), i ≥ 1).(2)

Note that the increment Cd − Cg cannot be obtained from the path frag-
ment e(g,d) when X jumps at g or d. This does not happen if X has un-
bounded variation, thanks to Proposition 1.
The same remark of Theorem 1 holds, namely, the intensity measure of
the right-hand side of (2), seen as a point process, admits the expression

E(∑

i 1(Li,XSi −XSi−1 ,VLi (K i))∈A
) = ∫ 1

0
 ∫ ∫ 1A(l, x, e) 1
l κl(dx, de) dl

in terms of the law of X, where the measure κl is the joint law of Xl and
the Vervaat transform Vl of (Xt − tXl/l, t ∈ [0, l]). The measure κl is related
to L´evy processes conditioned to stay positive [introduced in generality in
Chaumont and Doney (2005)] in Uribe Bravo (2011).
This document is organized as follows: we ﬁrst study the basic proper-
ties of the convex minorant of a L´evy process of Proposition 1 in Section 2.
Then, examples of the qualitative behaviors of the convex minorants are
given in Section 3. Next, we turn to the description of the process of lengths
and slopes of excursion intervals up to an independent exponential time in

THE CONVEX MINORANT OF A L´EVY PROCESS 9

Section 4, where we also discuss how this implies the description of the con-
vex minorant to a deterministic and ﬁnite time and on an inﬁnite horizon.
Section 4 also explains the relationship between this work and the literature
on ﬂuctuation theory for L´evy processes. Section 5 is devoted to the abso-
lute continuity of the location and time of the minimum of a L´evy process
with a proof of Theorem 2. Finally, we pass to the invariance of the path
transformation (1) for L´evy processes stated as Theorem 3, in Section 6 and
to the description of the excursions above the convex minorant implied by
Theorem 4 in Section 7.

2. Basic properties of the convex minorant on a ﬁnite interval. In this
section we will prove Proposition 1. Let X = (Xt, t ∈ [0, 1]) be a L´evy process
and consider its convex minorant C on [0, 1] as well as the lower semicon-
tinuous regularization X l of X given by X l = X ∧ X− [with the convention
X−(0) = X0 = 0].

2.1. Property 1 of Proposition 1. We will ﬁrst be concerned with the
measure of
 P = {t ∈ [0, 1] : X l = C}.

A ﬁrst observation is that P does not vary under changes in the drift of X.
We now prove that P has Lebesgue measure zero almost surely. Indeed,
it suﬃces to see that for each t ∈ (0, 1), t /∈ P almost surely. If X has
unbounded variation, Rogozin (1968) proves that

lim inf
h→0+ Xh
h = −∞ almost surely (a.s.)

[see, however, the more recent proof at Vigon (2002)], and so by the Markov
property at each ﬁxed time t, we get

lim inf
h→0+ Xt+h − Xt
h = −∞ and lim sup
h→0+
 Xt+h − Xt
h = ∞ a.s.

However, at any τ ∈ P, we have

lim inf
h→0+ Xτ +h − Xτ
h ≥ D(τ ) > −∞ a.s.,

where D is the right-hand derivative of C. If X has bounded variation, the
proof is similar, except that, according to Bertoin [(1996), Proposition 4,
page 81], we get
 lim
h→0+ Xt+h − Xt
h = d

almost surely, where d is the drift coeﬃcient. We then see that if t ∈ P ∩
(0, 1), then D(t) = d; the inequality D(t) ≤ d follows from the preceding

10 J. PITMAN AND G. URIBE BRAVO

display, and by time reversal we also obtain d ≤ C ′
−(t). Taking away the
drift, we see that t then should be a place where the minimum is achieved.
However, t is almost surely not a time when the minimum is reached: deﬁning

˜Xs = { Xt+s − Xt, if s ≤ 1 − t,
X1 − Xt + Xs−(1−t), if 1 − t ≤ s ≤ 1,

we know that ˜X has the same law as X. Note that the minimum of X
is reached at t if and only if ˜X remains above zero, which happens with
positive probability only when 0 is irregular for (−∞, 0). Hence, t does not
belong to P almost surely whenever 0 is regular for (−∞, 0). If this is not
the case, then 0 is regular for (0, ∞) since X is nonatomic, and applying
same argument to the time reversed process (X(1−t)− − X1, t ≤ 1) we see
then that t /∈ P almost surely in this remaining case.

2.2. Property 2 of Proposition 1. We will now show that for an excursion
interval (g, d) of X above C, the jumps of X at g and d, denoted ∆Xg
and ∆Xd, satisfy ∆Xg∆Xd ≥ 0. We ﬁrst prove that, thanks to (CD), X
does not have jumps of both signs on the two endpoints of an excursion. The
proof depends on diﬀerent arguments for bounded and unbounded variation:
with unbounded variation, actually no jumps occur at the endpoints.
If X has unbounded variation, we again use Rogozin’s result:

lim inf
h→0+ Xh
h = −∞ and lim sup
h→0+
 Xh
h = ∞,

and adapt Millar’s proof of his Proposition 2.4 [Millar (1977)] to see that X
is continuous on {X l = C}. Indeed, for every ε > 0, let J ε
1 , J ε
2 , . . . be the
jumps of X with size greater than ε in absolute value. Then the strong
Markov property applied at J ε
i implies that

lim inf
h→0+ XJ ε
i +h − XJ ε
i
h = −∞ and lim sup
h→0+
 XJ ε
i +h − XJ ε
i
h = ∞.

Hence, at any random time T which is almost surely a jump time of X, we
get
 lim inf
h→0+ XT +h − XT
h = −∞;

however, if t ∈ {X l = C}, we see that

lim inf
h→0+ Xt+h − Xt
h ≥ D(t) > −∞.

Suppose now that X has bounded variation but inﬁnite L´evy measure.
Since our problem (jumping to or from the convex minorant) is invariant
under addition of drift, we can assume that the drift coeﬃcient of X is zero,

THE CONVEX MINORANT OF A L´EVY PROCESS 11

and so
 lim
h→0+ Xh
h = 0

by Bertoin (1996), Proposition 4, page 81. We will now prove that almost
surely, for every component (g, d) of {C < X l}, we have

∆Xg∆Xd ≥ 0.(3)

The argument is similar to the unbounded variation case: at any random
time T which is almost surely a jump time of X, we have

lim
h→0+ XT +h − XT
h = 0.

We deduce that if the slope of C on the interval (g, d) is strictly positive,
then ∆Xg ≥ 0, and so Xg− = Cg. By time-reversal, we see that if the slope
of C is strictly negative on (g, d), then ∆Xd ≤ 0 and so Xd = Cd. Note
that C only has nonzero slopes. Indeed, a zero slope would mean that the
inﬁmum of X is attained at least twice, a possibility, that is, ruled out by
Proposition 2.2 of Millar (1977) under assumption (CD).

2.3. Property 3 of Proposition 1. We now see that, almost surely, all
excursion intervals of X above its convex minorant have diﬀerent slopes.
A diﬀerent argument is given for bounded and unbounded variation pro-
cesses.
When X has unbounded variation on compact sets, let C t denote the
convex minorant of X on [0, t] so that C = C 1. Note that C t and C agree
up to some random time, which we call τt; for every ﬁxed t ∈ (0, 1), τt
cannot equal t as Ct < X l
t almost surely, as proved in Section 2.1. We will
ﬁrst prove that, almost surely, for every t ∈ (0, 1) ∩ Q, whenever the post t
process touches a line that extends C t linearly outwards from one of the
excursion intervals of C t, it crosses it downwards. To see that this is enough,
suppose that there were two excursion intervals, (g1, d1) and (g2, d2), with
the same associated slope. Then there would exist t ∈ (g2, d2) ∩ Q such that
g1 < d1 ≤ τt < t. If the post t process touches the linear extension of the
convex minorant over the interval (g1, d1) it must cross it downwards. This
should occur at d2, which contradicts Cd2 = X l
d2 .
To prove the claim that the post t process crosses the extended lines
downwards for each ﬁxed t ∈ (0, 1), let Li(s) = αi + βis be the lines extending
the segments of C t (using any ordering which makes the αi and βi random
variables). Let

Ti = inf{s ≥ 0 : X l
t+s − Xt ≤ αi − Xt + βi(t + s)}.

Hence Ti is a stopping time for the ﬁltration Ft+s = σ(Xr : r ≤ t + s), s ≥ 0,
with respect to which Xt+s − Xt, s ≥ 0, is a L´evy process. If X jumps be-
low Li at time Ti, then the excursion interval of C containing t cannot
have slope βi (and incidentally, βi is not a slope of C). Since X has inﬁnite

12 J. PITMAN AND G. URIBE BRAVO

variation, Rogozin’s result quoted above gives

lim inf
h→0+ XTi+h − Xti
h = −∞.

Hence, if X is continuous at Ti then X goes below Li immediately after Ti
and βi cannot be a slope of C. We have seen, however, that in the unbounded
variation case, X does not jump at the vertices of excursion intervals.
When X has bounded variation, the argument is similar except in a few
places. Suppose the drift of X is zero. We ﬁrst use

lim
h↓0+ Xt+h − Xt
h = 0

to prove that for every t ∈ (0, 1), whenever the post t process touches a linear
extension Li of C t on an excursion interval with positive slope, by a jump,
it crosses it downwards: this is clear if X is continuous at Ti or if it jumps
into Li at Ti. However, X cannot reach Li from the left and jump away
at Ti by quasi-continuity of L´evy processes. By time reversal, we handle the
case of negative slopes, and therefore there are no two excursions above the
convex minorant with the same slope almost surely by the same arguments
as in the unbounded variation case. Again, note that slopes of C are nonzero
since under (CD) the minimum of X is attained only once by Proposition 2.2
of Millar (1977).

3. Examples.

3.1. L´evy processes of bounded variation. Consider a L´evy process X
with paths of bounded variation on compact sets and zero drift such that 0
is regular for (0, ∞) but irregular for (−∞, 0). Then the cumulative mini-
mum of X is piecewise constant and decreases by jumps; that is, X reaches
a new minimum by jumping downwards. It follows that the convex minorant
of X on any ﬁnite interval has a ﬁnite number of segments of negative slopes
until it reaches the minimum of X, and all the excursions above the convex
minorant end by a jump (and begin continuously). However, since the min-
imum is attained at a jump time, say at ρ, then limt→0(Xρ+t − Xρ)/t = 0,
and since Xρ+· − Xρ visits (0, ∞) on any neighborhood of 0, there cannot
be a segment of the convex minorant with slope zero, nor a ﬁrst segment
with positive slope. Hence 0 is an accumulation point for positive slopes.

3.2. The convex minorant of a Cauchy process.

Proof of Corollary 1. Let X be a symmetric Cauchy process, such
that
 F (x) := P(X1 ≤ x) = 1/2 + arctan(x)/π.

Since
 E(e
iuXt) = e
−t|u|,

THE CONVEX MINORANT OF A L´EVY PROCESS 13

we see that X is 1-selfsimilar, which means that Xt has the same law as tX1
for every t ≥ 0.
If Ξ1 is the point process of lengths and increments of excursions intervals
for the convex minorant on [0, 1], its intensity measure ν1 has the following
form:
 ν1(dl, dx) = 1
l P(Xl ∈ dx) dl.

Therefore, the intensity ˜ν1 of the point process of lengths and slopes of
excursions intervals for the convex minorant on [0, 1], say ˜Ξ1, factorizes as

˜ν1(dl, ds) = 1
l P(X1 ∈ ds) dl.

Let Y1, Y2, . . . be an i.i.d. sequence of Cauchy random variables independent
of L; recall that F is their distribution function. From the analysis of the
point process Ξ1 in the forthcoming proof of Lemma 1, the above factor-
ization of the intensity measure ˜ν1 implies that ˜Ξ1 has the law of the point
process with atoms
 {(Li, Yi) : i ≥ 1};(4)
otherwise said: lengths and slopes are independent for the Cauchy process.
In the converse direction, we see that if lengths and slopes are independent
then X is a 1-selfsimilar L´evy process. Indeed, using Theorem 1, we see that
XL1/L1 and L1 are independent. Let G be the law of XL1/L1. Independence
of L1 and XL1/L1 implies that Xt/t has law G for almost all t ∈ (0, 1), so
that G = F . As the law of Xt/t is weakly continuous, we see that Xt/t has
law F for all t ∈ (0, 1) and the independence and homogeneity of increments
of X implies that Xt/t has law F for all t. However, it is known that a 1-
selfsimilar L´evy process is a symmetric Cauchy process, although perhaps
seen at a diﬀerent speed. See Theorem 14.15 and Example 14.17 of Sato
(1999).
We ﬁnish the proof by identifying the law of (Ix, x ∈ R). Informally, Ix
is the time in which the convex minorant of X on [0, 1] stops using slopes
smaller than x. We then see that I has the same law as

˜I =
 ( ∞∑

i=1 Li1Yi≤x, x ∈ R
)
.

In contrast, if Ui, i ≥ 1, is an i.i.d. sequence of uniform random variables on
(0, 1) independent of L, the process (Tt/T1, t ∈ [0, 1]) has the representation
( ∞∑

i=1 Li1Ui≤t, t ∈ [0, 1]

)
.

With the explicit choice Ui = F (Yi), we obtain the result. □

As a consequence of Corollary 1, we see that the set C = {t ∈ [0, 1] : Ct =
Xt ∧ Xt−} is perfect.

14 J. PITMAN AND G. URIBE BRAVO

3.3. The convex minorant of stable processes. Let C be the convex mi-
norant of the L´evy process X on [0, 1]. We now point out a dichotomy
concerning the set of slopes

S = { Cd − Cg
d − g : (g, d) is an excursion interval}
,

when X is a stable L´evy process of index α ∈ (0, 2] characterized either by
the scaling property
 Xst d
= s1/αXt, s > 0,

or the following property of its characteristic function:

|E(e
iuXt )| = e
−tc|u|α.

Corollary 4. When α ∈ (1, 2], S has no accumulation points, and
S ∩ (a, ∞) and S ∩ (−∞, −a) are almost surely inﬁnite for all a > 0. If α ∈
(0, 1], then S is dense in R+, R−, or R depending on if X is a subordinator,
−X is a subordinator or neither condition holds.

Proof. When α ∈ (1, 2], Fourier inversion implies that X1 admits a con-
tinuous and bounded density which is strictly positive. We now make an
intensity measure computation for a < b:

E(#S ∩ (a, b)) = ∫ 1

0
 ∫ b

a
 1
t P(Xt/t ∈ (a, b)) dt.

Using the scaling properties of X, we see that near t = 0, the integrand is
asymptotic to ct−1/α where c is the density of X1 at zero. Since

E(#S ∩ (a, b)) < ∞

for all a < b, then S does not contain accumulation points in R.
If a > 0, a similar argument implies that

E(#S ∩ (a, ∞)) = ∞

since P(X1 > 0) > 0. Unfortunately, this does not imply that #S ∩ (a, ∞) =
∞ almost surely. However, from Theorem 1, we see that S ∩ [a, ∞) has the
same law as ∑

i≥1 1
Yi≥aL1−1/α
i ,

where L and Y are independent, and Yi has the same law as X1. Since
1 − 1/α > 0 and Li → 0, we see that Yi ≥ aL1−1/α
i inﬁnitely often, implying
that #S ∩ (a, ∞) = ∞ almost surely.
We have already dealt with the Cauchy case, which corresponds to α = 1,
so consider α ∈ (0, 1). Arguing as before, we see that

#S ∩ (a, b) d
= ∑

i≥1 1
Yi∈L1−1/α
i (a,b).

THE CONVEX MINORANT OF A L´EVY PROCESS 15

Since 1 − 1/α < 0, we see that Yi ∈ L1−1/α
i (a, b) inﬁnitely often as long as
P(X1 ∈ (a, b) > 0). Finally, recall that the support of the law of X1 is R+, R−
or R depending on if X is a subordinator, −X is a subordinator or neither
condition holds. □

4. Splitting at the minimum and the convex minorant up to an indepen-
dent exponential time. In this section, we analyze the relationship between
Theorem 1 and Corollary 2 and how they link with well-known results of the
ﬂuctuation theory of L´evy processes. We also give a proof of Corollary 3.
We will ﬁrst give a proof of Corollary 2 and show how it leads to a proof
of Theorem 1. While the implication is based on very well-known results of
ﬂuctuation theory, it is insuﬃcient to prove the more general Theorem 4.
Our proof of Theorem 4 is independent of the results of this section.
Let X denote a L´evy process with continuous distributions, C its con-
vex minorant on an interval [0, T ] (which can be random), X l the lower-
semicontinuous regularization of X given by X l
t = Xt ∧ Xt− and O = {s ≤
T : Cs < X l
s} is the open set of excursions from the convex minorant on
[0, T ]. Thanks to Proposition 1 on the basic properties of the convex mi-
norant, proved in Section 2, we see that the point process of lengths and
increments of excursion intervals are equivalently obtained by the following
construction, taken from Nagasawa [(2000), Chapter XI]: deﬁne

X a
t = Xt − at and X a
t = min
s≤t X a
s

as well as
 ρa = sup{s ≤ T : X a
t ∧ X a
t− = X a
t } and ma = X l
ρa.

The idea behind such deﬁnitions is that if a ↦→ ρa jumps at a, it is because
the convex minorant on [0, t] begins using the slope a at ρa− and ends using
it at ρa, while the value of the convex minorant at the beginning of this
interval is ma−, and at the end it is ma. For every ﬁxed a, we know that X a

reaches its minimum only once almost surely. However, at a random a at
which ρa jumps, the minimum is reached twice, since we know that slopes
are used only once on each excursion interval. From this analysis, we see
that
 Cρa = X l
ρa = ma

and obtain the following important relationship:

ΞT is the point process {(ρa − ρ
a−, ma − ma−) : ρ
a− < ρa}.

We characterize the two-dimensional process (ρ, m) with the help of the
following results. First of all, according to Millar’s analysis of the behavior
of a L´evy process at its inﬁmum [cf. Millar (1977), Proposition 2.4], if 0 is

16 J. PITMAN AND G. URIBE BRAVO

irregular for (−∞, 0) then, since 0 is regular for (0, ∞), X a
ρa = X a
ρa almost
surely for each ﬁxed a; cf. also the ﬁnal part of Section 2.2. With this pre-
liminary, Theorem 5 and Lemma 6 from Bertoin [(1996), Chapter VI] can
be written as follows:

Theorem 5. Let T be exponential with parameter θ and independent
of X. For each ﬁxed a ∈ R, there is independence between the processes

(X a
(t+ρa)∧T − ma, t ≥ 0) and (X a
t∧ρa , t ≥ 0).

Furthermore,

E(exp(−αρ
a + β(ma − aρ
a)))
(5)
 = exp(− ∫ ∞

0
 ∫ 0

−∞(1 − e
−αt+βx) e−θt

t P(Xt − at ∈ dx) dt).

Formula (5) was proved initially by Peˇcerski˘ı and Rogozin (1969). Later,
Greenwood and Pitman (1980) showed how to deduce it by splitting at
the minimum of the trajectory of a L´evy process up to an independent
exponential time, a theme which was retaken by Bertoin (1996) to produce
the independence assertion of the previous theorem.

Proof of Corollary 2. The proof follows [Nagasawa (2000)]. We
ﬁrst show that (ρ, m) is a process with independent increments. Let a < b.
Note that ρb − ρa is the last time that t such that Xρa+t − ma − bt reaches
its minimum, so that Theorem 5 implies the independence of ρa+b − ρa and
σ(X·∧ρa ); denote the latter σ-ﬁeld as F a. Also, note that mb − ma is the
minimum of X(ρa+t)∧T − ma − bt, t ≥ 0. Hence there is also independence
between mb − ma and F a. Finally, note that if a′ ≤ a, (ρa′, ma′) are F a

measurable since ρa′ is the last time that X·∧ρa − a′· reaches its minimum
on [0, ρa], and ma′ is the value of this minimum.
From the above paragraph, we see that the point process of jumps of
(ρ, m), that is, Ξ, is a Poisson random measure: this would follow from
(a bidimensional extension of) Theorem 2 and Corollary 2 in Gihman and
Skorohod [(1975), Chapter IV.1, pages 263–266] which aﬃrm that the jump
process of a stochastically continuous process with independent increments
on R+ is a Poisson random measure on R+ × R+. To show that (ρ, m) is
stochastically continuous, we show that it has no ﬁxed discontinuities; this
follows because for every ﬁxed a ∈ R, the minimum of X a is reached at an
unique point almost surely, which implies that, for every ﬁxed a, almost
surely, neither ρ nor m can jump at a. To compute the intensity measure ν
of ΞT , note that the pair (ρa, ma) can be obtained from ΞT as

(ρa, ma) = ∑

(u,v)∈I
Cv −Cu≤a(v−u)
(v − u, Cv − Cu).(6)
 THE CONVEX MINORANT OF A L´EVY PROCESS 17

The above equality contains the nontrivial assertion that the additive process
(ρ, m) has no deterministic component or, stated diﬀerently, that it is the
sum of its jumps. For the process ρ, this follows because
∑

(u,v)∈I
Cv −Cu≤a(v−u)
(v − u) = Leb(O ∩ {t ≤ T : C ′
t ≤ a})

which, since Leb(O) = T and C ′ is nondecreasing, gives
∑

(u,v)∈I
Cv−Cu≤a(v−u)
(v − u) = sup{t ≤ T : C ′
t ≤ a} = ρ
a.

To discuss the absence of drift from m, let mC be the signed measure which
assigns each interval (u, v) the quantity Cv − Cu. (Because C ′ is nondecreas-
ing, it is trivial to prove the existence of such a signed measure, to give
a Hahn decomposition of it and to see that it is absolutely continuous with
respect to Lebesgue measure.) Then
∑

(u,v)∈I
Cv −Cu≤a(v−u)
(Cv − Cu) = mC(O ∩ {t ≤ T : C ′
t ≤ a})

= mC({t ≤ T : C ′
t ≤ a}) = Cρa = X l
ρa = ma.

From (6), we get

E(exp(−αρa + βma)) = exp(− ∫ ∞

0
 ∫ at

−∞(1 − e
−αt+βx)ν(dt, dx)
),

while from the Peˇcerski˘ı–Rogozin formula (5), we obtain

E(exp(−αρ
a + βma))

= exp(− ∫ ∞

0
 ∫ 0

−∞(1 − e
−(α−aβ)t+βx) e−θt

t P(Xt − at ∈ dx) dt)

= exp(− ∫ ∞

0
 ∫ at

−∞(1 − e
−αt+βx) e−θt

t P(Xt ∈ dx) dt)

giving
 ν(dt, dx) = e−θt

t P(Xt ∈ dx) dt. □

We now remark on the equivalence between Theorem 1 and Corollary 2
and how either of them implies Corollary 3.
Let L be an uniform stick-breaking sequence and X a L´evy process with
continuous distributions which are independent. Let S be the partial sum

18 J. PITMAN AND G. URIBE BRAVO

sequence associated to L, and consider the point process ˜Ξt with atoms at

{(tLi, XtSi − XtSi−1 )}.

Lemma 1. If T an exponential random variable of parameter θ indepen-
dent of (X, L), ˜ΞT is a Poisson point process with intensity

µθ(dt, dx) = e−θt

t dt P(Xt ∈ dx).(7)

Proof. We recall the relationship between the Gamma subordinator
and the stick-breaking process, which was found by McCloskey in his unpub-
lished PhD thesis [McCloskey (1965)] and further examined and extended
by Perman, Pitman and Yor (1992). Recall that a Gamma process is a sub-
ordinator (Γt, t ≥ 0) characterized by the Laplace exponent

E(e
−qΓt) = ( θ
θ + q
 )t = exp(−t ∫ ∞

0 (1 − e
−qx) e−θx

x dx);

the law of Γ1 is exponential of parameter θ. It is well known that (Γt/Γ1, t ≤
1) is independent of Γ1. Also, it was proved [McCloskey (1965); Perman,
Pitman and Yor (1992)] that the size-biased permutation of the jumps of
(Γt/Γ1, t ∈ [0, 1]) has the same law as the stick-breaking process on [0, 1].
Hence if L is a stick-breaking process independent of the exponential T of
parameter θ, then the point process with atoms at {T L1, T L2, . . .} has the
same law as the point process with atoms at the jumps of a Gamma subor-
dinator (of parameter θ) on [0, 1] or, equivalently, a Poisson point process
with intensity e−θx/x dx.
If S is the partial sum sequence associated to L, conditionally on T = t
and L = (l1, l2, . . .), (XT Si − XT Si−1, i ≤ 1) are independent and the law of
XT Si − XT Si−1 is that of Xtli . We deduce that the point process with atoms
{(T Li, XT Si − XT Si−1), i ≥ 1} is a Poisson point process with the inten-
sity µθ of (7), as shown, for example, in Kallenberg [(2002), Proposition 12.3,
page 228] using the notion of randomization of point processes. □

Lemma 1 shows how Theorem 1 implies Corollary 2.
Conversely, if we assume Corollary 2, we know that ˜ΞT has the same law
as the point process of lengths and increments of excursions intervals on the
interval [0, T ]. However, if Ξt is the point process of lengths and increments
of excursion intervals on [0, t], then
∫ ∞

0 θe
−θtE(e
−Ξtf ) dt = E(e
−˜ΞT f ) = ∫ ∞

0 θe
−θtE(e
−˜Ξtf ) dt

which implies that
 E(e
−Ξtf ) = E(e
−˜Ξtf )

for continuous and nonnegative f . However, this implies the identity in law
between Ξt and ˜Ξt, giving Theorem 1.

THE CONVEX MINORANT OF A L´EVY PROCESS 19

Let us pass to the proof of Corollary 3. Abramson and Pitman show the
discrete time analog using a Poisson thinning procedure.

Proof of Corollary 3. Suppose l = lim inf t→∞ Xt/t ∈ (−∞, ∞]. Then
there exists a ∈ R and T > 0 such that Xt > at for all t > T . If C T is the
convex minorant of X on [0, T ], and ρa is the ﬁrst instant at which the
derivative of C T is greater than a, then the convex function

˜Ct = { C T , if t < ρa,
C T
Ta + a(t − T ), if t ≥ ρa,

lies below the path of X on [0, ∞), implying C ∞, the convex minorant of X
on [0, ∞), is ﬁnite for every point of [0, ∞).
Conversely, if C ∞ is ﬁnite on [0, ∞), for any t > 0 we can let a =
limh→0+(Ct+h − Ct)/h ∈ R and note that lim inf s→∞ Xs/s ≥ a.
From Erickson (1973) we see that, actually, limt→∞ Xt/t exists and it is
ﬁnite if and only if E(|X1|) < ∞ and E(X1) = l. Note that the right-hand
derivative of C ∞ is never strictly greater than l. This derivative cannot
equal l: if l = ∞ this is clear while if l < ∞, it follows from the fact that
the zero mean L´evy process Xt − lt visits (−∞, 0) [as can be proved, e.g.,
by embedding a random walk and using, for example, by Chung and Fuchs
(1951); Chung and Ornstein (1962)]. However, the derivative also surpasses
any level a < l. This follows from the deﬁnitions of l and C ∞: if the derivative
of C ∞ were always less than l − ε, since Xt eventually stays above every line
of slope l − ε/2, we would be able to construct a convex function greater
than C ∞ and below the path of X.
If a < l, let La be the last time the derivative of C ∞ is smaller than a.
Then for t > La, we see that

C La = C t = C ∞ on [0, La].

We will now work with C Tθ , where Tθ is exponential of parameter θ and
independent of X. Then on the set {La < Tθ}, which has probability tending
to 1 as θ → 0, we have C La = C Tθ = C ∞ on [0, La]. Recall, however, that
if Ξθ is a Poisson point process with intensity

µθ(dt, dx) = e−θt

t P(Xt ∈ dx) dt,

then Ξθ has the law of the lengths and increments of excursions of X
above C Tθ by Corollary 2. We deduce that for every a < l the restriction
of Ξθ to {(t, x) : x < at} converges in law as θ → 0 to the point process with
atoms at the lengths and increments of excursions of X above C ∞ with
slope less than a. Hence, the excursions of X above C ∞ with slopes < a
form a Poisson point process with intensity
1x<at
t P(Xt ∈ dx) dt.

It suﬃces then to increase a to l to obtain the stated description of Ξ∞. □

20 J. PITMAN AND G. URIBE BRAVO

Basic to the analysis of this section has been the independence result for
the pre and post minimum processes up to an independent exponential time
as well as the Peˇcerski˘ı and Rogozin formula stated in Theorem 5. Theo-
rem 5 is the building block for the ﬂuctuation theory presented in Bertoin
[(1996), Chapter VI] and is obtained there using the local time for the L´evy
process reﬂected at its cumulative minimum process. In the following sec-
tions, we will reobtain Theorem 1 and Corollaries 2 and 3 appealing only
to the basic results of the convex minorant of Section 2 (and without the
use of local time). In particular, this implies the ﬁrst part of Theorem 5,
from which the full theorem follows as shown by Bertoin (1996). Indeed,
assuming Theorem 4, if T is exponential with parameter θ and independent
of X, if ρa is the last time X l
t − at reaches its minimum on [0, T ], and ma is
the value of this minimum, we see that

(X a
(t+ρa)∧T − ma, t ≥ 0)

can be obtained from the Poisson point process of excursions of X above its
convex minorant with slopes > a, while

(X a
t∧ρa , t ≥ 0)

is obtained from the excursions with slopes ≤ a. Since the process of excur-
sions (up to an independent time) is a Poisson point process, we obtain the
independence of the pre and post minimum processes.
Here is another example of how the description of the convex minorant
up to an independent exponential time leads to a basic result in ﬂuctua-
tion theory: according to Rogozin’s criterion for regularity of half-lines, 0 is
irregular for (0, ∞) if and only if
∫ 1

0 P(Xt ≤ 0)/t dt < ∞.(8)

To see how this might be obtained from Corollary 2, we note that the prob-
ability that X does not visit (0, ∞) on some (0, ε) is positive if and only if
the convex minorant up to Tθ has positive probability of not having negative
slopes. By Theorem 2 this happens if and only if
∫ ∞

0 P(Xt ≤ 0)e
−θt/t dt < ∞,

which is of course equivalent to (8).

5. Absolute continuity of the minimum and its location.

Proof of Theorem 2. Since 0 is regular for both half-lines, the L´evy
process X satisﬁes assumption (CD), and we can apply Theorem 1.
Let L be an uniform stick-breaking process independent of X, and deﬁne
its partial sum and residual processes S and R by

S0 = 0, Si+1 = Si + Li+1 and Ri = 1 − Si.

THE CONVEX MINORANT OF A L´EVY PROCESS 21

Set
 ∆i = XSi − XSi−1.

Then the time of the minimum of the L´evy process X on [0, 1], has the same
law as
 ρ =
 ∞∑

i=1 Li1∆i<0,

while the minimum of X on [0, 1] (denoted X 1) and X1 − X 1 have the same
laws as ∞∑

i=1 ∆i1∆i<0 and
 ∞∑

i=1 ∆i1∆i>0.

The basic idea of the proof is to decompose these sums at a random index J ;
in the case of ρ, into

ΣJ =
 J∑

i=1 Li1∆i<0 and ΣJ =
 ∞∑

i=J+1 Li1∆i<0.(9)

The random index (actually a stopping time for the sequence ∆) is chosen
so that ΣJ and ΣJ are both positive, and (RJ , ΣJ ) has a joint density,
which is used to provide a density for Σ using the conditional independence
between ΣJ and ΣJ given RJ .
Let I be any stopping time for the sequence ∆ which is ﬁnite almost surely.
We ﬁrst assert that the sequence (∆I+i−1)i≥1 has both nonnegative and
strictly negative terms if 0 is regular for both half-lines. Indeed, if 0 is regular
for (−∞, 0), this implies that the convex minorant of X has a segment of
negative slope almost surely, which implies the existence of i such that ∆i < 0
almost surely. If 0 is regular for (0, ∞), a time-reversal assertion proves also
the existence of nonnegative terms in the sequence ∆. On the other hand,
conditionally on I = i and L1 = l1, . . . , Li = li, the sequence (∆i−1+j, j ≥ 1)
has the same law as the sequence ∆ but obtained from the L´evy process
X(1−l1−···−li)t,t≥0 which shares the same regularity as X, which implies the
assertion.

1. Let I and J be deﬁned by

I = min{i ≥ 1 : ∆i ≥ 0} and J = min{j ≥ I : ∆j < 0}.

By the preceding paragraph, we see that I and J are both ﬁnite almost
surely. Hence, the two sums ΣJ and ΣJ of (9) are both in the interval (0, 1)
and we have
 ρ = ΣJ + ΣJ .

We now let
 f (t) = P(Xt ≤ 0)

22 J. PITMAN AND G. URIBE BRAVO

which will allow us to write the density of (ΣJ , RJ ); this follows from the
computation

P(J = j, L1 ∈ dl1, . . . , Lj ∈ dlj)

=
 j−1∑

i=1
 ∏

k<i f (lk) ∏

i≤k<j(1 − f (lk))f (lj)P(L1 ∈ l1, . . . , Lj ∈ lj)

valid for j ≥ 2. For 2 ≤ i < j, let

gi,j(l1, . . . , lj) = (l1, . . . , li−1, li, . . . , lj−2, l1 + · · · + li + lj, 1 − li − · · · − lj),

and deﬁne
 g1,2(l1, l2) = (l2, 1 − l2 − l2)

as well as
 g1,j(l1, . . . , lj) = (l1, . . . , lj−2, lj, 1 − l1 − · · · − lj)

for j ≥ 3. Then gi,j is an invertible linear transformation on Rj, and so if B
is a Borel subset of Rj of Lebesgue measure zero, then g−1
i,j (B) also has
Lebesgue measure zero. If A is a Borel subset of R2 with Lebesgue measure
zero, we get

P((ΣJ , RJ ) ∈ A) ≤
 ∞∑

j=2
 j−2∑

i=1 P((L1, . . . , Lj) ∈ g−1
i,j (Rj−2 × A)) = 0.

Hence, there exists a function g which serves as a joint density of (ΣJ , RJ ).
We can then let
 gr(l) = g(l, r)
∫ g(l′, r) dl′

be a version of the conditional density of ΣJ given RJ = r.
Using the construction of the stick breaking process and the independence
of increments of X we deduce that

˜L = (LJ+i
RJ , i ≥ 1
)

is independent of (Li∧J , ∆i∧J , i ≥ 1) and has the same law as L. Further-
more, the sequence (∆J+i, i ≥ 1) is conditionally independent of (Li∧J , ∆i∧J )
given RJ .
We therefore obtain the decomposition

ρ = ΣJ + RJ ρ
J ,

where
 ρ
J =
 ∞∑

i=1
 Li+J
RJ 1∆i+J <0 = ΣJ

RJ .

THE CONVEX MINORANT OF A L´EVY PROCESS 23

Since ρJ is a function of ˜L, (∆J+i, i ≥ 1) and RJ , then ρJ and ΣJ are condi-
tionally independent given RJ . Hence gRJ is also a version of the conditional
density of ΣJ given RJ and ρJ , and we can then write

P(ρ ∈ dt) = dt ∫ gr(t − ry)P(RJ ∈ dr, ρ
J ∈ dy)(10)

on {J < ∞}.
Finally, it remains to see that the density for ρ displayed in equation (10)
is positive on (0, 1). We remark that the density of (RJ , ΣJ ) is positive on

{(r, σ) : 0 < σ < 1 − r < 1}.

Indeed, taking r, σ as in the preceding display, we have the explicit compu-
tation
 P(J = 2, ΣJ ∈ dσ, RJ ∈ dr)

= P(∆1 > 0, ∆2 < 0, L2 ∈ dσ, 1 − L1 − L2 ∈ dr)

= (1 − f (1 − σ − r))f (σ)10<σ<1−r<1 1
1 − σ − r dr dσ.

On the other hand, given t ∈ (0, 1), P(RJ < 1 − t) > 0. Indeed,

P(RJ < 1 − t) ≥ P(RJ < 1 − t, J = 2)

= ∫ ∫ P(∆1 ≥ 0, ∆2 < 0, L1 ∈ dl1, 1 − L1 − L2 ∈ dl2)1l2≤1−t

= ∫ ∫ (1 − f (l1))f (1 − l1 − l2) 1
1 − l1 10<l2<1−l11l2<1−t

> 0,

since f and 1 − f are strictly positive on (0, 1) since 0 is regular for both half
lines and so the support of the law of Xt is R for all t > 0. Going back to
equation (10), we see that, given t ∈ (0, 1), on the set {(r, y) : 0 < r < 1 − t}
we have t − ry < t < 1 − r, and so the density gr(t − ry) is positive. Hence
the integral in equation (10) is positive.
2. The proof of absolute continuity of the time and value of the minimum
of X on [0, 1] is similar, except that further hypotheses are needed.
First, the value of the minimum of X on [0, 1] has the same distribution
as
 m :=
 ∞∑

i=1 ∆i1∆i≤0.

Since the law of Xt is absolutely continuous with respect to Lebesgue mea-
sure for all t > 0, we have

(ρ, m) = (ΣJ , mJ ) + (RJ ρ
J , mJ ),

24 J. PITMAN AND G. URIBE BRAVO

where
 mJ = ∑

i≤J ∆i1∆i<0 and mJ =
 ∞∑

i=1 ∆J+i1∆J +i>0.

We now prove that:

(a) (ρJ , mJ ) has a conditional density with respect to RJ ;
(b) (ρJ , mJ ) and (ρJ , mJ ) are conditionally independent given RJ .

The second assertion follows from our previous analysis of conditional inde-
pendence in the sequences L and ∆. The ﬁrst assertion follows from the fact
that (ΣJ , RJ , ∆J ) admit a density on {J = j}, by a computation similar to
the one for (ΣJ , RJ )

P(J = j, L1 ∈ dl1, . . . , Lj ∈ dlj, ∆1 ∈ dx1, . . . , ∆j ∈ dxj)

=
 j−1∑

i=1 1x1....,xi−1<0,xi,...,xj−1>0,xj<0P(Xl1 ∈ dx1) · · · P(Xlj ∈ dxj)

× P(L1 ∈ dl1, . . . , Li ∈ dlj)

so that on {J = j}, (L1, . . . , LJ , ∆1, . . . , ∆J ) admit a density with respect to
Lebesgue measure, and since (∆J , RJ , ∆J ) is the image under a surjective
linear map of the former variables, the latter admit a joint density. Let fr
be a version of the conditional density of (ΣJ , ∆J ) given RJ = r. We then
get
 P(ρ ∈ dt, m ∈ dx)
(11)
 = dt dx ∫ fr(t − rs, x − y)P(ρ
J ∈ ds, mJ ∈ dy, RJ ∈ dr).

Regarding the equivalence of the law of (ρ, m) and Lebesgue measure on
(0, 1) × (−∞, 0), note that a version of the density of (RJ , ρJ , mJ ) is positive
on
 {(r, s, x) : 0 ≤ r + s ≤ 1, x < 0}.

Indeed, we have, for example,

P(∆1 < 0, ∆2 > 0, RI ∈ dr, ΣI ∈ ds, mI ∈ dx)

= P(Xs ∈ dx)(1 − f (1 − r − s)) 1
1 − s 10≤r+s≤11x≤0.

Since the law of (ρJ , mJ , RJ ), by analogy with the case of ρ, is seen to charge
the set {(s, y, r) : t < 1 − r, x < y}, we conclude that the expression for the
joint density of (ρ, m) given in equation (11) is strictly positive.
3. The proof of the absolute continuity of (X 1, X1 − X 1) follows the same
method of proof, starting with the fact that these random variables have the

THE CONVEX MINORANT OF A L´EVY PROCESS 25

same joint law as
 (∆−, ∆+) =
 ∞∑

i=1 ∆i(1∆i<0, 1∆i>0),

which we can again decompose at the random index

I = min{i ≥ 1 : there exist j, j ≤ i such that ∆j < 0, ∆j′ > 0}

into
 (∆−, ∆+) = (∆−
I , ∆+
I ) + (∆−,I , ∆+,I),

where
 (∆−
I , ∆−
I ) = ∑

i≤I ∆i(1∆i<0, 1∆i>0).

Since:

(a) (RI , ∆−
I , ∆+
I ) have a joint density which can be taken positive on
(0, 1) × (−∞, 0) × (0, ∞), and
(b) (∆−
I , ∆+
I ) and (∆−,I , ∆+,I) are conditionally independent given RI ,

we see that (∆−, ∆+) admit a joint density which can be taken positive on
(−∞, 0) × (0, ∞). □

6. An invariant path transformation for L´evy processes. The aim of
this section is to prove Theorem 3. This will be done (almost) by ap-
plying the continuous mapping theorem to the embedded random walk
(Xk/n, k = 0, . . . , n) and a continuous function on Skorohod space. The ar-
gument’s technicalities are better isolated by focusing ﬁrst on some special
cases in which the main idea stands out. Therefore, we ﬁrst comment on the
case when X has continuous sample paths, then we handle the case when X
has paths of unbounded variation on compact intervals, to ﬁnally settle the
general case.
We rely on a discrete version of Theorem 3, which was discovered by
Abramson and Pitman (2011). Let Sn = (Sn
t , t ∈ [0, n]) be the process ob-
tained by interpolating between the values of n steps of a random walks
which jumps every 1/n, and let C n be its convex minorant. Let V n
0 , V n
1 , . . . , V n
k
be the endpoints of the segments deﬁning the convex minorant C n. Let Un
be uniform on {1/n, . . . , 1}. Since there exists an unique j such that

Un ∈ (V n
j , V n
j+1],

let us deﬁne
 gn = V n
j and dn = V n
j+1

26 J. PITMAN AND G. URIBE BRAVO

as the excursion interval of Sn above C n which straddles Un. Mimicking the
deﬁnition of the path transformation (1), let us deﬁne

Sn,Un
t =
 



 Sn
Un+t − Sn
Un, if 0 ≤ t ≤ dn − Un,
Sn
dn − Sn
Un + Sn
gn+t−(dn−Un) − Sn
gn, if dn − Un ≤ t ≤ dn − gn,
Sn
dn + Sn
t−(dn−gn), if dn − gn ≤ t ≤ dn,
Sn
t , if dn ≤ t.

Theorem 6 [Abramson and Pitman (2011)]. If the distribution function
of Sn
1/n is continuous, then the pairs

(Un, Sn) and (dn − gn, Sn,Un)

have the same law.

To prove Theorem 3 we will use Theorem 6 with the random walk obtained
by sampling our L´evy process X at points of the form 1/n and take the limit
as n → ∞. The details are a bit technical in general but simplify considerably
when X is continuous or when it reaches its convex minorant continuously.
The main tool for the passage to the limit is a lemma regarding approxi-
mation of the endpoints of the interval of the convex minorant that contains
a given point. Let f : [0, 1] → R be a c`adl`ag function which starts at zero and
is left continuous at 1 and c its convex minorant. Let also f l = f ∧ f− be the
lower semicontinuous regularization of f , and deﬁne with it the excursion
set away from the convex minorant O = {c < f l}. For all u belonging to
the open set O we can deﬁne the quantities g < u < d as the left and right
endpoints of the excursion interval of O that contains u. We deﬁne the slope
of c at u as the quantity
 mu = c(d) − c(g)
d − g = c
′(u).

The notations gu(f ), du(f ) and mu(f ) will be preferred when the function f
or the point u are not clear from context. We will ﬁrst be interested in
continuity properties of the quantities gu, du and mu when varying the
function f .
Recall that a sequence fn in the space of c`adl`ag functions on [0, 1] con-
verges to f in the Skorohod J1 topology if there exist a sequence of increas-
ing homeomorphisms from [0, 1] into itself such that fn − f ◦ λn converges
uniformly to 0 on [0, 1].

Lemma 2. If:

1. f is continuous at u;
2. u ∈ O;
 THE CONVEX MINORANT OF A L´EVY PROCESS 27

3. the function

f l(t) − d − t
d − g f l(g) + t − g
d − g f l(d) for t ∈ [0, 1]

is zero only on {g, d};
4. fn → f in the Skorohod J1 topology and un → u, then

gun(fn) → gu(f ), dun(fn) → du(f ) and mun(fn) → mu(f ).

The proof is presented in Section 6.3. We now pass to the analysis of the
particular cases when our L´evy process X has continuous paths, or when it
reaches its convex minorant continuously.

6.1. Brownian motion with drift. In this subsection, we will prove The-
orem 3 when X is a (nondeterministic) L´evy process with continuous paths,
that is, a (nonzero multiple of) Brownian motion with drift.
Let f be a continuous function on [0, 1], and consider the continuous
function ϕuf given by

ϕuf (t) =
 



 f (u + t) − f (u), if 0 ≤ d − u,
f (d) − f (u) + f (g + t − (d − u)) − f (g),
if d − u ≤ t ≤ d − g,
f (d) − f (g) + f (t − (d − g)), if d − g ≤ t ≤ d,
f (t), if t ≤ d.

(12)

If f , fn, u and un satisfy the hypotheses of Lemma 2 (which implies that
fn → f uniformly), then g(fn) → g(f ) and d(fn) → d(f ). Therefore, it is
simple to verify that (u, f ) ↦→ (d − g, ϕuf ) is continuous at (u, f ) when the
space of continuous functions on [0, 1] is equipped with the uniform norm.
When X is a L´evy process with continuous paths and distributions, that
is, a Brownian motion with drift, consider its polygonal approximation with
step 1/n obtained by setting

X n
k/n = Xk/n for k ∈ {0, 1, . . . , n}

and extending this deﬁnition by linear interpolation on [0, 1]. Then X n → X
uniformly on [0, 1]; it is at this point that the continuity of the paths of X is
important. Now, if U is uniform on [0, 1] and independent of X, and we set
Un = n⌈U/n⌉, then (dn − gn, ϕUnX n) → (d − g, ϕU X). However, Theorem 6
says that (Un, X n) and (dn − gn, ϕUnX n) have the same law. We conclude
that (U, X) and (d − g, ϕU X) have the same law, which is the conclusion of
Theorem 3 in this case.

6.2. Absence of jumps at the convex minorant. In this subsection, we
will prove Theorem 3 when X is a L´evy process of unbounded variation on
compact sets [which automatically satisﬁes (CD)]. We now let f be a c`adl`ag
function on [0, 1] and let c stand for its convex minorant. We will suppose

28 J. PITMAN AND G. URIBE BRAVO

that f is continuous on the set {c = f l}, which holds whenever f is the
typical trajectory of X, thanks to 2 of Proposition 1.
Again, for all u ∈ {c < f } = {c < f ∧ f−} = O we deﬁne g and d as the
left and right endpoints of the excursion interval that contains u. Since f
has jumps, its polygonal approximation does not converge to it in Skorohod
space, but if we deﬁne
 fn(t) = f ([nt]/n),

then fn converges in the Skorohod J1 topology to f as n → ∞; cf. Billingsley
(1999), Chapter 2, Lemma 3, page 127. This will called the piecewise con-
stant approximation to f with span 1/n and is the way we will choose to
approximate a L´evy process when it has jumps. The ﬁrst complication in this
case is that the discrete invariant path transformation was deﬁned for the
polygonal approximation and not for the piecewise constant approximation
to our L´evy process. For this reason, we will have to deﬁne a more ﬂexible
path transformation than in the continuous case: for u1 < u2 < u3 ∈ (0, 1),
we deﬁne ϕu1,u2,u3f by

ϕu1,u2,u3f (t) =
 



 f (u2 + t) − f (u2), 0 ≤ t < u3 − u2,
f (u3) − f (u2) + f (u1 + t − (u3 − u2)) − f (u1),
u3 − u2 ≤ t ≤ u3 − u1,
f (u3) − f (u1) + f (t − (u3 − u1)),
u3 − u1 ≤ t < u3,
f (t), u3 ≤ t.

(13)

The path transformation ϕu of (12) corresponds to ϕg,u,d. We are interested
in ϕg,U,dX, which will be approximated by ϕ˜gn,Un, ˜dnX n where ˜gn and ˜dn are
the left and right endpoints of the excursion of the polygonal approximation
to X of span 1/n which contains Un = ⌈U n⌉/n, and X n is the piecewise
constant approximation to X with span 1/n. We are forced to use both
the vertices of the convex minorant of the polygonal approximation and
the piecewise constant approximation, since X n → X (in the Skorohod J1
topology), but with (˜gn, ˜dn) we can deﬁne a nice invariant transformation:
Theorem 6 asserts that

(Un, ϕ˜gn,Un, ˜dnX n) and ( ˜dn − ˜gn, X n)

have the same law. Indeed, Theorem 6 is an assertion about the increments
of a random walk and the polygonal and piecewise approximations to X of
span 1/n are constructed from the same increments.
Lemma 2 tells us that (˜gn, ˜dn) → (d, g). It is therefore no surprise that

ϕ˜gn,Un, ˜dnX n → ϕg,U,dX,

telling us that (U, X) and (d − g, ϕg,U,dX) have the same law whenever X
satisﬁes (CD) and has unbounded variation on ﬁnite intervals. Convergence
follows from the following continuity assertion:

THE CONVEX MINORANT OF A L´EVY PROCESS 29

Lemma 3. If f is continuous at (u1, u2, u3), fn → f in the Skorohod J1
topology, and un
i → ui for i = 1, 2, 3, then

ϕun
1 ,un
2 ,un
3 fn → ϕu1,u2,u3f.

Lemma 3 is an immediate consequence of the following convergence cri-
terion found in Ethier and Kurtz (1986), Proposition III.6.5, page 125.

Proposition 2. A sequence fn of c`adl`ag functions on [0, 1] converges
to f in the Skorohod J1 topology if and only if for every sequence (tn) ⊂ [0, 1]
converging to t:

1. |fn(tn) − f (t)| ∧ |fn(tn) − f (t−)| → 0;
2. if |fn(tn) − f (t)| → 0, tn ≤ sn → t, then |fn(sn) − f (t)| → 0;
3. if |fn(tn) − f (t−)| → 0, sn ≤ tn and sn → t, then |fn(sn) − f (t)| → 0.

In particular, we see that if f is continuous at t, then fn(tn) → f (t). The
above criterion is clearly necessary for convergence since if fn → f , then there
exist a sequence (λn, n ∈ N) of increasing homeomorphisms of [0, 1] into itself
such that fn − f ◦ λn converges to zero uniformly. If tn → t, then fn(tn) will
be close to either f (t−) or f (t) depending on if λn(tn) < t or λn(tn) ≥ t. By
using the above criterion, we focus on the real problem for continuity for the
transformation ϕu1,u2,u3, namely, that nothing wrong happens at u3 − u2,
u3 − u1 and u3.

Proof of Lemma 3. Let us prove that for every t ∈ [0, 1], the conditions
of Proposition 2 hold for ϕun
1 ,un
2 ,un
3 fn and ϕu1,u2,u3f .
Let λn be increasing homeomorphisms of [0, 1] into itself such that

fn − f ◦ λn → 0

uniformly. We proceed by cases.

t < u3. Eventually t < un
3 , so that ϕun
1 ,un
2 ,un
3 fn(t) = fn(t) and ϕu1,u2,u3f (t) =
f (t). Since fn and f satisfy the conditions of Proposition 2 at time t, the
same holds for their images under the path transformation.
t < u3 − u2. Eventually t < un
3 − un
2 so that

ϕu1,u2,u3f (t) = f (u2 +t)−f (u2) and ϕun
1 ,un
2 ,un
3 f n(t) = f n(un
2 +t)−f n(u
n
2 ).

Since f is continuous at u2, Proposition 2 implies that f n(un
2 ) → f (u), so
that ϕun
1 ,un
2 ,un
3 f n(t) can be made arbitrarily close to either ϕu1,u2,u3f (t) or
ϕu1,u2,u3f (t−) depending on if

un + tn < λ−1
n (u + t) or un + tn ≥ λ−1
n (u + t).

t ∈ (u3 − u2, u3) \ {u3 − u1} is analogous to the preceding case. For t ∈
{u3 − u2, u3 − u1, u3} set

v1 = u3 − u2, v2 = u3 − u1 and v3 = u3.

30 J. PITMAN AND G. URIBE BRAVO

Since f is continuous at u3, condition 3 gives

fn(un
i ) → f (ui) for i = 1, 2, 3,

and so
 ϕu1,u2,u3f (vn
i ) → ϕu1,u2,u3f (vi) for i = 1, 2, 3. □

6.3. The general case. In this subsection, we prove Theorem 3 for a L´evy
process X under the sole assumption (CD).
The challenge to overcome in the remaining case, in which X can jump
into and out of the convex minorant, is to show how one can handle the
jumps; although a result in the vein of Lemma 3 will play a prominent
role in our analysis, a more careful inspection of how gn diﬀers from g is
needed in order to sort the following problem: in general, the operation of
rearranging pieces of c`adl`ag paths is not continuous and depends sensitively
on the points at which the rearrangement is made. A simple example helps
to clarify this: consider f = 1[1/3,1] + 1[2/3,1], so that if u1 = 1/3, u2 = 1/2
and u3 = 2/3, we have ϕu1,u2,u3f = 1[1/6,1] + 1[2/3,1]. Note that if un
1 → u1
and un
1 ∈ (0, 1/2), then

ϕun
1 ,u2,u3f = { 1[1/6,1] + 1[1/6+1/3−un
1 ,1], if un
1 ∈ (0, 1/3],
1[1/6,1] + 1[1−un
1 ,1], if un
1 ∈ [1/3, 1/2).

We conclude that ϕun
1 ,u2,u3f → ϕu1,u2,u3f if and only if un
1 ≥ 1/3 eventually.
Let f : [0, 1] → R be a c`adl`ag function which starts at zero and c its convex
minorant on [0, 1]. Let also f l = f ∧ f− be the lower semicontinuous regular-
ization of f . As before, the component intervals of the open set O = {c < f l}
are called the excursion intervals of f , and that for u ∈ O, (g, d) is the ex-
cursion interval that contains u.
We ﬁrst give the proof of Lemma 2; the proof depends on another lemma
with a visual appeal, which is to be complemented with Figure 3.

Lemma 4. If for a c`adl`ag function f : [0, 1] → R:

1. there exist closed intervals A and B in [0, 1] such that inf B − sup A > 0
and
2. there exists δ > 0 and

h < δ inf B − sup A
inf B ∨ (1 − sup A)

such that
 f > δ on [0, 1] \ A ∪ B and min
x∈A∪B f l(x) < h,

then for all u ∈ (sup A, inf B),

gu ∈ A, du ∈ B and mu ≤ h
inf B − sup A .

THE CONVEX MINORANT OF A L´EVY PROCESS 31

Fig. 3. Visual content of Lemma 4.

Proof. This assertion can be checked by cases. We consider 3 possible
positions for gu and three other for du : gu < inf A, gu ∈ A and gu ∈ (sup A, u)
and similarly du ∈ (u, inf B), du ∈ B and du > sup B. We number each from 1
to 3 and write Ci,j for the corresponding case. We trivially discard the cases

C1,1, C1,3, C3,1, C3,3

for each one would force c(g) to be above the zero slope line through (0, δ),
hence to pass above g on A and B. The case C2,1 would force c (hence f ) to
be above δ on B while C3,2 would force f to be above δ on A, hence both are
discarded. We ﬁnally discard the case C2,3 (and by a similar argument C3,2)
because of our choice of h, since a line from a point of A× [0, h] to [sup B, 1]×
[δ, ∞) passes above h on B. □

Proof of Lemma 2. Set u ∈ {c < f l}, and write g and d for gu(f )
and du(f ) so that g < u < d. Recall that c is linear on (gu(f ), du(f )). By
considering instead

t ↦→ f (t) − d − t
d − g f l(g) + t − g
d − g f l(d) and

t ↦→ fn(t) − d − t
d − g f l(g) + t − g
d − g f l(d),

our assumptions allow us to reduce to the case

f l(g) = f l(d) = 0 and f l > 0 on [0, 1] \ {g, d}.

We will now consider the case 0 < g < d < 1, the cases g = 0 or d = 1 being
handled similarly.
For every
 ε < g ∧ (1 − d) ∧ d − g
2

32 J. PITMAN AND G. URIBE BRAVO

we can deﬁne

δ(ε) = inf{f (t) : t ∈ [0, g − ε] ∪ [g + ε, d − ε] ∪ [d + ε, 1]}

= min{f l(t) : t ∈ [0, g − ε] ∪ [g + ε, d − ε] ∪ [d + ε, 1]}.

Then δ(ε) > 0 for ε > 0 and δ(ε) → 0 as ε → 0. Since g < u < d, we can
choose ε small enough so that

u ∈ (g + ε, d − ε).

Since fn → f , there exists a sequence of increasing homeomorphisms λn of
[0, 1] converging uniformly to the identity such that

fn − f ◦ λn
converges uniformly to zero. (If f is continuous, λn can be taken equal to
the identity function.)
Also, given hn eventually bounded away from 0,

min{f l(t) : t ∈ (g − ε, g + ε)} < hn and min{f l(t) : t ∈ (d − ε, d + ε)} < hn
for large enough n. Hence

min{f l
n(t) : t ∈ (λ
−1
n (g − ε), λ
−1
n (g + ε))} < hn
and
 min{f l
n(t) : t ∈ (λ
−1
n (d − ε), λ
−1
n (d + ε))} < hn
for large enough n. The particular hn we will consider is

hn = δ(ε) λ−1
n (d − ε) − λ−1
n (g + ε)
λ−1
n (d − ε) ∨ (1 − λ
−1
n (g + ε))

→ δ(ε) (d − g − 2ε)
((d − ε) ∨ (1 − g − ε)) > 0

which is eventually positive. Since f > δ(ε) on [0, g − ε] ∪ [g + ε, d − ε] ∪
[d + ε, 1], then

fn > δ on [0, λ
−1
n (g − ε)] ∪ [λ
−1
n (g + ε), λ
−1
n (d − ε)] ∪ [λ
−1
n (d + ε), 1],

and Lemma 4 now tells us that

gun(fn) ∈ (λ−1
n (g − ε), λ
−1
n (g + ε)),

dun(fn) ∈ (λ−1
n (d − ε), λ
−1
n (d + ε))

and
 mun(gn) ≤ hn/(λn(d − ε) − λn(g + ε)),

so that eventually

gun(fn) ∈ (g − 2ε, g + 2ε), dun(fn) ∈ (d − 2ε, d + 2ε) and

mun(fn) ≤ 2δ/(d − ε) ∨ (1 − g − ε). □

THE CONVEX MINORANT OF A L´EVY PROCESS 33

Remark. In the context of the above proof, if we suppose that f (g−) =
c(g) < f (g) and f (d−) = c(d), then for hn eventually bounded away from
zero, we actually have
 min{f l(t) : t ∈ [g − ε, g)} < hn

for large enough n, and so we get

gun(fn) < λ
−1
n (g).

This remark is crucial to the proof of Theorem 3.

Remark. Let cn be the convex minorant of fn. Under the hypotheses of
Lemma 2, we can actually deduce that if tn → g, then cn(tn) → c(g), while
if tn → d, then cn(tn) → c(d). This is because of the following result about
convergence of convex functions.

Proposition 3. If cn and c are convex functions on [0, 1], for some
a ∈ (0, 1) we have cn(a) → c(a), and if the two sequences (cn(0)) and (cn(1))
are bounded, then for every sequence an → a we have cn(an) → c(a).

Proof. If an ≤ a, we can use the inequalities

cn(an) ≤ cn(a) an
a + cn(0) a − an
a
and
 cn(an) ≥ cn(a) 1 − a
1 − an + cn(1) a − an
1 − an .

We get an analogous pair of inequalities when an ≥ a, which allows us to
conclude that the sequence (cn(a) − cn(an)) goes to zero. □

Given u1 < u2 < u3, we now deﬁne a new c`adl`ag function ψu1,u2,u3f as
follows:

ψu1,u2,u3f (t) =
 



 f (u2 + t) − f (u2), 0 ≤ t < u3 − u2,
c(u3) − c(u1) + f (u1 + t − (u3 − u2)) − f (u2),
u3 − u2 ≤ t ≤ u3 − u1,
c(u3) − c(u1) + f (t − (u3 − u1)), u3 − u1 ≤ t < u3,
f (t), u3 ≤ t.

The diﬀerence with the path transformations of (12) and (13) is that we now
use the convex minorant c instead of only the function f . This has the eﬀect
of choosing where to place the jumps that f might make as it approaches its
convex minorant. Note, however, that ψu1,u2,u3f = ϕu1,u2,u3f if f = c at u1
and u3.

34 J. PITMAN AND G. URIBE BRAVO

Our next task will be to analyze the continuity of f ↦→ ψg,u,df on Sko-
rohod space, with special emphasis on the approximations we will use. For
every n, fn and ˜fn will be the piecewise constant and polygonal approxima-
tions to f with span 1/n, we set un = ⌈nu⌉/n, and

gn = gun(fn), dn = dun(fn), ˜gn = gun( ˜fn) and ˜dn = dun( ˜fn).

Lemma 5. Under the hypotheses of Lemma 2, if either

f (g) = c(g) and f (d) = c(d) or f (g−) = c(g) and f (d−) = c(d),

then
 ψ˜gn,un, ˜dnfn → ψg,u,df

in the Skorohod J1 topology.

Proof. Since we have already analyzed what happens when f is con-
tinuous at g and d, the essence of the argument will be illustrated when

f (g) = c(g) < f (g−) and f (d) = c(d) < f (d−).

As in the proof of Lemma 3, we verify that for every t ∈ [0, 1], the conditions
of Proposition 2 hold for ψ˜gn,un, ˜dnfn and ψd,u,gf at time t.
Let λn be a sequence of increasing homeomorphisms of [0, 1] such that

fn − f ◦ λn → 0

uniformly. The crucial part of the argument is to use the remarks after
Lemma 2 from which we deduce that

λ−1
n (g) ≤ gn and λ−1
n (d) ≤ dn.

Since fn is the piecewise constant approximation to f , then λ−1
n must eventu-
ally take g and d to [ng]/n and [nd]/n. But comparing the convex minorants
of the piecewise constant and polygonal approximations to f with span 1/n
leads to
 gn − 1/n ≤ ˜gn and dn − 1/n ≤ ˜dn

so that
 λ−1
n (g) ≤ ˜gn and λ−1
n (d) ≤ ˜dn.

Again using the remarks after the proof of Proposition 13, we see that

cn(˜gn) → c(g) and cn( ˜dn) → c(d).

The conditions of Proposition 2 can now be veriﬁed at times t ∈ [0, 1] \
d − u, d as in the proof of Lemma 13, while for t ∈ {d − u, d}, the proof is
similar and hence will be illustrated when t = d − g. Since fn − f ◦ λn → 0
uniformly, the jump of f at g is approximated by the jump of fn at λ−1
n (g).

THE CONVEX MINORANT OF A L´EVY PROCESS 35

We reduce to cases by taking subsequences: when tn > ˜dn − un for all n,
then tn + un > λ−1
n (d) so that

ψ˜gn,un, ˜dnf (tn) → f (d) − f (g) + f (g) − f (u) = f (d) − f (u).

On the other hand, when tn ≤ dn − un for all n, we see that

ψ˜gn,un, ˜dnf (tn) is close to f (d−) − f (u) or f (d) − f (u)

depending on if
 tn + un < λ
−1
n (d) or tn + un ≥ λ−1
n (d).

Hence, the conditions of Proposition 2 are satisiﬁed at t = d − u. □

We ﬁnally proceed to the proof of Theorem 3.

Proof of Theorem 3. Thanks to Proposition 1, X almost surely sat-
isﬁes the conditions of Lemma 5 at U . Hence, (dn − gn, ψ˜gn,Un, ˜dn(X n)) con-
verges in law to (d − g, ψd,U,gX) thanks to Lemmas 2 and 5, as well as the
continuous mapping theorem. Since (Un, X n) converges in law to (U, X) and
the laws of (Un, X n) and (dn − gn, ψ˜gn,Un, ˜dn(Xn)) are equal by Theorem 6,
then (U, X) and (d − g, X U ) have the same law. □

7. Excursions above the convex minorant on a ﬁxed interval. In this
section we will prove Theorem 4, which states the equality in law between
two sequences. We recall the setting: X is a L´evy process such that Xt has
a continuous distribution for every t > 0, C is its convex minorant on [0, 1],
X l = X ∧ X− is the lower semicontinuous regularization of X, O = {C <
X l} is the excursion set, I is the set of excursion intervals of O, for each
(g, d) ∈ I , and we let e(g,d) be the excursion associated to (g, d) given by

e
(g,d)
s = X(g+s)∧d − C(g+s)∧d.

We ordered the excursion intervals to state Theorem 1 by sampling them
with an independent sequence of uniform random variables on [0, t].
The ﬁrst sequence of interest is

((di − gi, Cdi − Cgi, e
(gi,di)), i ≥ 1).

The second sequence is obtained with the aid of an independent stick-
breaking process and the Vervaat transformation. Recall that Vtf stands
for the Vervaat transform of f on [0, t]. Let V1, V2, . . . be an i.i.d. sequence
of uniform random variables on (0, 1), and construct

L1 = V1, Ln = Vn(1 − V1) · · · (1 − Vn−1) and Si = L1 + · · · + Li.

This sequence helps us to break up the paths of X into the independent
pieces Y i, i = 1, 2, . . . given by

Y i
t = XSi−1+t − XSi−1, 0 ≤ t ≤ Li,

36 J. PITMAN AND G. URIBE BRAVO

from which we can deﬁne the sequence of Knight bridges,

K i
t = Y i
t − t
Li Y i
Li, 0 ≤ t ≤ Li.

Our second sequence is

((Li, XSi − XSi−1, VLi(K i)), i ≥ 1).

To prove the equality in law, we will use Theorem 3 to obtain a pro-
cess ˜X which has the same law as X, as well as a stick-breaking sequence ˜L
independent of ˜X such that, with analogous notation, the pointwise equality

((di − gi, Cdi − Cgi, e
(gi,di)), i ≥ 1) = ((Li, ˜X ˜Si − ˜X ˜Si−1, V ˜Li( ˜K i)), i ≥ 1)

holds. This proves Theorem 4.
Let us start with the construction of ˜X and ˜L. Apart from our original
L´evy process X, consider an i.i.d. sequence of uniform random variables
U1, U2, . . . independent of X. Consider ﬁrst the connected component (g1, d1)
of {C < X ∧ X−} which contains U1 and let X 1 be the result of applying
the path transformation of Theorem 3 to X at the points g1, U1 and d1. We
have then seen that ˜V1 = d1 − g1 is uniform on [0, 1] and independent of X 1.
Set ˜S0 = 0 and ˜L1 = ˜V1.
Consider now the convex minorant C 1 of

Z 1 = X 1
˜L1+· − X 1
˜L1

on [0, 1 − ˜L1]: we assert that it is obtainable from the graph of C by eras-
ing the interval (g1, d1) and closing up the gap, arranging for continuity.
Formally, we assert the equality

C 1
t = { Ct, if t ∈ [0, g1),
Ct−g1+d1 − (Cd1 − Cg1), if t ∈ [g1, 1 − ˜L1].

Note that C 1 is continuous on [0, 1 − ˜L1] by construction and it is convex
by a simple analysis. To see that C 1 is the convex minorant of Z 1, we only
need to prove that at g1 it coincides with Z 1
g1 ∧ Z 1
g1−; cf. Figure 2 to see how
it might go wrong. If Xd1 = Cd1 , then

Z 1
g1 = Xd1 − (Cd1 − Cg1) = Cg1 = C 1
d1,

while if Xd1− = C(d1) < Xd1 , then property 2 of Proposition 1 implies that
Xg1− = C(g1) and

Z 1
d1− = X 1
d1− − X 1
˜L1 = Cd1 − Cg1 + Xg1− − (Cd1 − Cg1) = Cg1 = C 1
g1.

Let (g2, d2) be the connected component of {C 1 < Z 1} ⊂ [0, 1 − ˜L1] that
contains U2(1 − ˜L1) and deﬁne

˜L2 = d2 − g2, ˜V2 = d2 − g2
1 − ˜V1

THE CONVEX MINORANT OF A L´EVY PROCESS 37

as well as the process X 2 which will be the concatenation of X 1 on [0, ˜V1]
as well as the path transformation of Z 1 on [0, 1 − ˜V1]; that is, Z 1 trans-
formed according to the path transformation of Theorem 3 with parame-
ters g2, U2(1 − ˜L1), d2. From Theorem 3 and the independence of

Z 2 = X 1
·+ ˜V1 − X 1
˜V1 and X 1
·∧ ˜V1
we see that:

1. X 2 has the same law as X 1;
2. ˜V1 and ˜V2 are independent of X 2, and ˜V2 is independent of ˜V1 and has
an uniform distribution on (0, 1);
3. the convex minorant C 2 of Z 2 on [0, 1 − ˜L1 − ˜L2] is obtained from C 1 by
deleting the interval (g2, d2) and closing up the gap arranging for continuity.

Now it is clear how to continue the recursive procedure to obtain, at step n
a sequence ˜V1, . . . , ˜Vn and a process X n such that if ˜Ln = ˜Vn(1− ˜Vn−1) · · · (1−
˜V1) and ˜Sn = ˜L1 + · · · + ˜Ln; then:

1. X n has the same law as X.
2. X n, ˜V1, . . . , ˜Vn are independent an the latter n variables are uniform
on (0, 1).
3. Let C n is the convex minorant of

Z n = X n
˜Sn+· − X n
˜Sn

on [0, 1 − ˜Sn]. Then C n is obtained from C n−1 by removing the selected
interval (gn, dn) and closing up the gap arranging for continuity.
4. X n coincides with X n−1 on [0, ˜Sn−1].

From property 4 above, it is clear that X n converges pointwise on [0, 1]
almost surely: it clearly does on [0, 1) and X n
1 = X1. Also, we see that ˜X
has the same law as X and that it is independent of V1, V2, . . . , which is an
i.i.d. sequence of uniform random variables.

Acknowledgments. Josh Abramson and Nathan Ross provided valuable
input to the present work, not only through enlightening discussions, but
also by providing access to their recent work on convex minorants.
We gladly thank the anonymous referee for his expeditious revision.

REFERENCES

Abramson, J. and Pitman, J. (2011). Concave majorants of random walks and related
Poisson processes. Combinatorics Probab. Comput. 20 651–682.
Abramson, J., Pitman, J., Ross, N. and Uribe Bravo, G. (2011). Convex minorants of
random walks and L´evy processes. Electron. Commun. Probab. 16 423–434. MR2831081
Andersen, E. S. (1950). On the frequency of positive partial sums of a series of random
variables. Mat. Tidsskr. B 1950 33–35. MR0039939

38 J. PITMAN AND G. URIBE BRAVO

Andersen, E. S. (1953a). On sums of symmetrically dependent random variables. Skand.
Aktuarietidskr. 36 123–138. MR0060173
Andersen, E. S. (1953b). On the ﬂuctuations of sums of random variables. Math. Scand.
1 263–285. MR0058893
Andersen, E. S. (1954). On the ﬂuctuations of sums of random variables. II. Math.
Scand. 2 195–223. MR0068154
Balabdaoui, F. and Pitman, J. (2009). The distribution of the maximal diﬀerence be-
tween Brownian bridge and its concave majorant. Bernoulli 17 466–483. MR2798000
Bertoin, J. (1996). L´evy Processes. Cambridge Tracts in Mathematics 121. Cambridge
Univ. Press, Cambridge. MR1406564
Bertoin, J. (2000). The convex minorant of the Cauchy process. Electron. Comm. Probab.
5 51–55 (electronic). MR1747095
Billingsley, P. (1999). Convergence of Probability Measures, 2nd ed. Wiley, New York.
MR1700749
Chaumont, L. (1997). Excursion normalis´ee, m´eandre et pont pour les processus de L´evy
stables. Bull. Sci. Math. 121 377–403. MR1465814
Chaumont, L. (2010). On the law of the supremum of L´evy processes. Available at
http://arxiv.org/abs/1011.4151.
Chaumont, L. and Doney, R. A. (2005). On L´evy processes conditioned to stay positive.
Electron. J. Probab. 10 948–961 (electronic). MR2164035
Chung, K. L. and Fuchs, W. H. J. (1951). On the distribution of values of sums of
random variables. Mem. Amer. Math. Soc. 1951 12. MR0040610
Chung, K. L. and Ornstein, D. (1962). On the recurrence of sums of random variables.
Bull. Amer. Math. Soc. 68 30–32. MR0133148
Doney, R. A. (2007). Fluctuation Theory for L´evy Processes. Lecture Notes in Math.
1897. Springer, Berlin. MR2320889
Erickson, K. B. (1973). The strong law of large numbers when the mean is undeﬁned.
Trans. Amer. Math. Soc. 185 371–381. MR0336806
Ethier, S. N. and Kurtz, T. G. (1986). Markov Processes: Characterization and Con-
vergence. Wiley, New York. MR0838085
Fourati, S. (2005). Vervaat et L´evy. Ann. Inst. H. Poincar´e Probab. Statist. 41 461–478.
MR2139029
Gihman, ˘I. ¯I. and Skorohod, A. V. (1975). The Theory of Stochastic Processes. II.
Springer, New York. MR0375463
Greenwood, P. and Pitman, J. (1980). Fluctuation identities for L´evy processes and
splitting at the maximum. Adv. in Appl. Probab. 12 893–902. MR0588409
Groeneboom, P. (1983). The concave majorant of Brownian motion. Ann. Probab. 11
1016–1027. MR0714964
Kallenberg, O. (2002). Foundations of Modern Probability, 2nd ed. Springer, New
York.MR1876169
Knight, F. B. (1996). The uniform law for exchangeable and L´evy process bridges.
Ast´erisque 236 171–188. MR1417982
Kyprianou, A. E. (2006). Introductory Lectures on Fluctuations of L´evy Processes with
Applications. Springer, Berlin.
Lachieze-Rey, R. (2009). Concave majorant of stochastic processes and Burgers turbu-
lence. J. Theor. Probab. To appear. DOI:10.1007/S10959-011-0354-7.
McCloskey, J. W. (1965). A model for the distribution of individuals by species in an
environment. Ph.D. thesis, Michigan State Univ., Ann Anbor, MI. MR2615013
Miermont, G. (2001). Ordered additive coalescent and fragmentations associated to Levy
processes with no positive jumps. Electron. J. Probab. 6 33 pp. (electronic). MR1844511

THE CONVEX MINORANT OF A L´EVY PROCESS 39

Millar, P. W. (1977). Zero–one laws and the minimum of a Markov process. Trans.
Amer. Math. Soc. 226 365–391. MR0433606
Nagasawa, M. (2000). Stochastic Processes in Quantum Physics. Monographs in Mathe-
matics 94 355–388. Birkh¨auser, Basel. MR1739699
Peˇcerski˘ı, E. A. and Rogozin, B. A. (1969). The combined distributions of the random
variables connected with the ﬂuctuations of a process with independent increments.
Teor. Veroyatn. Primen. 14 431–444. MR0260005
Perman, M., Pitman, J. and Yor, M. (1992). Size-biased sampling of Poisson point
processes and excursions. Probab. Theory Related Fields 92 21–39. MR1156448
Pitman, J. W. (1983). Remarks on the convex minorant of Brownian motion. In Seminar
on Stochastic Processes, 1982 (Evanston, IL, 1982). Progress in Probability Statist. 5
219–227. Birkh¨auser, Boston, MA. MR0733673
Pitman, J. and Ross, N. (2010). The greatest convex minorant of Brownian mo-
tion, meander, and bridge. Probab. Theory Related Fields. To appear. DOI:10.1007/
S00440-011-0385-0.
Pitman, J. and Yor, M. (1997). The two-parameter Poisson–Dirichlet distribution de-
rived from a stable subordinator. Ann. Probab. 25 855–900. MR1434129
Rogozin, B. A. (1968). The local behavior of processes with independent increments.
Teor. Veroyatn. Primen. 13 507–512. MR0242261
Sato, K.-i. (1999). L´evy Processes and Inﬁnitely Divisible Distributions. Cambridge Stud.
Adv. Math. 68. Cambridge Univ. Press, Cambridge. MR1739520
Spitzer, F. (1956). A combinatorial lemma and its application to probability theory.
Trans. Amer. Math. Soc. 82 323–339. MR0079851
Suidan, T. M. (2001a). Convex minorants of random walks and Brownian motion. Teor.
Veroyatn. Primen. 46 498–512. MR1978665
Suidan, T. M. (2001b). A one-dimensional gravitationally interacting gas and the convex
minorant of Brownian motion. Uspekhi Mat. Nauk 56 73–96. MR1861441
Uribe Bravo, G. (2011). Bridges of L´evy processes conditioned to stay positive. Available
at http://arxiv.org/abs/1101.4184.
Vervaat, W. (1979). A relation between Brownian bridge and Brownian excursion. Ann.
Probab. 7 143–149. MR0515820
Vigon, V. (2002). Votre L´evy rampe-t-il? J. Lond. Math. Soc. (2) 65 243–256. MR1875147

Department of Statistics
University of California, Berkeley
367 Evans Hall
Berkeley, California 94720-3860
USA
E-mail: pitman@stat.Berkeley.edu
geronimo@matem.unam.mx
