<!-- source: https://arxiv.org/pdf/2009.05000 | converted from PDF -->

PRIMES IN SHORT INTERVALS: HEURISTICS AND
CALCULATIONS

ANDREW GRANVILLE AND ALLYSA LUMLEY

Dedicated to the memory of Lord Cherwell †

Abstract. We formulate, using heuristic reasoning, conjectures for the range of the
number of primes in intervals of length y around x, where y ≪ (log x)
2. In particular
we conjecture that the maximum grows surprisingly slowly as y ranges from log x to
(log x)
2. We will exhibit the available data, showing that it somewhat supports our
conjectures, though not so well that there may not be room for some modiﬁcations.

1. Introduction

We are interested in estimating the maximum and minimum number of primes in a
length y sub-interval of (x, 2x], denoted by

M (x, y) := max
X∈(x,2x] π(X + y) − π(X) and m(x, y) := min
X∈(x,2x] π(X + y) − π(X),

respectively, so that

m(x, y) ≤ π(X + y) − π(X) ≤ M (x, y) whenever x < X ≤ 2x,

and these bounds cannot be improved (by deﬁnition). It is widely believed that
m(x, y) = 0 for y ≪ (log x)
2 though we do not know the precise value of the implicit
constant. However there has been little study of how m(x, y) subsequently grows, or
of how M (x, y) behaves for y ≪ (log x)
2+o(1). In this article we will conjecture a series
of guesstimates for M (x, y) and m(x, y) in diﬀerent ranges, comparing these estimates
to what relevant data we can compute, and discussing some of the issues that prevent
us from being too conﬁdent of these guesses.
The starting point for our investigations came from a comparison of two known
observations:
Based on the (conjectured) size of admissible sets we believe that there exists a
constant c > 0 such that M (x, y) ∼ y
log y

† Lord Cherwell’s scientiﬁc advice to Winston Churchill during the second world war led to the
development support and subsequent unveiling of several extraordinary military innovations. Partly
as a consequence of Cherwell’s status, scientiﬁc research, even in pure mathematics, was never so
encouraged as after the war. In 1956, Cherwell returned to Oxford University to pursue his earlier
interests, writing a paper with E.M. Wright on conjectures about the distribution of prime tuples,
and another on primes in short intervals, before his death in 1957.
Thanks are due to James Maynard for some helpful remarks on both the content and the exposi-
tion, to Kevin Ford and Drew Sutherland for making various data available, as well as to the three
anonymous referees for their helpful comments. 1arXiv:2009.05000v3  [math.NT]  3 May 2021
2 ANDREW GRANVILLE AND ALLYSA LUMLEY

for y ≤ c log x, as long as y → ∞ as x → ∞ (see sections 1.1, 4.1, 8.1 and 9.1). On
the other hand, based on a modiﬁcation of Cram´er’s probabilistic model [3] for the
distribution of primes (which in turn is based on Gauss’s observation that the primes
have density 1
log x around x), we believe that

M (x, y) ∼ σ+(A) y
log x

for y = (log x)A with A > 2, for some constant σ+(A) > 1, for which σ+(A) → 1
+ as
A → ∞ (see sections 1.5, 3.1, and 7.2).
Therefore it seems that in both ranges, M (x, y) is roughly linear in y: In particular,

M (x, y) ∼ y
log log x for y a little smaller than log x,

whereas, if c+ := σ+(2) then

M (x, y) ∼ c+ y
log x for y a little bigger than (log x)
2.

If true then M (x, y) has quite diﬀerent slopes, 1
log log x vs. c+
log x, in these two diﬀerent
ranges, and so there is a substantial change in behaviour of M (x, y) as y grows from
around log x to slightly beyond (log x)
2. Our main goal is to investigate what happens
in-between, though also to give heuristic support for the claims above.
At the end-points of this in-between interval, the above claims suggest that

M (x, log x) ∼ log x
log log x whereas M (x, (log x)
2) ≍ log x,

so M (x, y) does not seem to get much bigger as y grows from log x to (log x)
2; indeed
it grows by only a factor of log log x. This is very diﬀerent from before and after this
interval: As y goes from 1 to log x we expect M (x, y) to grow by a factor of ≍ log x
log log x ,
and as y goes from (log x)
2 to (log x)
3 to grow by a similar factor of ≍ log x (and indeed
for any subsequent interval of multiplicative length log x). This does not seem to have
been previously observed.
Based on an appropriate heuristic we conjecture that if 1 < A < 2 then

M (x, (log x)A) ∼ 1
2 − A · log x
log log x ;

more precisely that if log x ≤ y = o((log x)
2) then

M (x, y) ∼ log x

log ( (log x)2

y ) . (1)

We will provide data with x up to 10
12 to support this claim, though it should be noted
that although this is as far as we have been able to compute, these x are still small
enough that secondary terms are likely to have a signiﬁcant impact (see sections 1.2,
8.3, 9.2). For this reason we also look at

M (x, 2y)/M (x, y)

PRIMES IN SHORT INTERVALS: HEURISTICS AND CALCULATIONS 3

because we expect that, as x → ∞ this looks much like 1 in this range, and 2 outside
this range. However we will compare the data for this ratio to a more precise conjecture.
In this article we will argue that there are four ranges of y in each of which we expect
diﬀerent behaviour for M (x, y), namely:

y ≪ log x; log x ≪ y = o(log x)
2; y ≍ (log x)2; and y/(log x)
2 → ∞ with y ≤ x.

We will present these separately in the introduction though there is signiﬁcant overlap
in the theory; and when it comes to presenting data for a given value of x up to which
we can compute, it is often unclear where one y-interval should end and the next begin.

1.1. Guesstimates for very short intervals: y ≪ log x. We believe that if y ≤ log x
then
 M (x, y) ∼ y
log y (2)

provided x, y → ∞. We will now formulate a more precise conjecture than this for
y ≤ (1 − o(1)) log x: A set of integers A is admissible if for every prime p there is a
residue class mod p that does not contain any element from the set (otherwise A is
inadmissible). Let S(y) denote the maximum size of an admissible set A which is a
subset of [1, y],
1 so that
 M (x, y) ≤ S(y) if x ≥ y

(for if X < p1 < · · · < pk ≤ X +y are primes then {p1 −X, . . . , pk −X} is an admissible
set). We believe that if y ≤ (1 − o(1)) log x then
2

M (x, y) = S(y). (3)

These two conjectures are consistent since it is believed that S(y) ∼ y
log y . The data
seems to conﬁrm the conjecture (3) for x = 10
k for k = 9, 10, 11 and 12:

1We say that A, and any translate of A, has length ≤ y.
2The “o(1)” here can be interpreted as saying that for any ﬁxed ϵ > 0, if x is suﬃciently large then
(3) holds for all y ≤ (1 − ϵ) log x.

4 ANDREW GRANVILLE AND ALLYSA LUMLEY

0 5 10 15 20 25 30 35 40
y

2

4

6

8

10M(109,y)
M (109, y)

M (109, y)

S(y)

log 109

0 10 20 30 40
y

2

4

6

8

10

12M(1010,y)
M (1010, y)

M (1010, y)

S(y)

log 1010

0 10 20 30 40 50
y

2

4

6

8

10

12M(1011,y)
M (1011, y)

M (1011, y)

S(y)

log 1011

0 10 20 30 40 50
y

2

4

6

8

10

12

14M(1012,y)
M (1012, y)

M (1012, y)

S(y)

log 1012

Figure 1. M (x, y) vs. S(y) for x = 10
k, k = 9, . . . , 12 and y ≤ 2 log x.
We observe that M (x, y) = S(y) up to the dashed line at y = log x

In these graphs, for each y (the horizontal axis), a colored-in dot represents M (x, y), and
an empty box represents the value of S(y). In this data, it appears that M (x, y) = S(y)
for y up to about 3
2 log x, and then M (x, y) is at worst a little less than S(y) for
y between 3
2 log x and 2 log x, for these values of x. Although we do believe that
M (x, y) = S(y) for all y ≤ (1 − ϵ) log x, for all suﬃciently large x, and perhaps even
for all y ≤ log x for all x, we do not believe that this should be so for y > (1 + ϵ) log x
and that the data we see here is an artiﬁce of the relatively small values of x we can
compute with. Indeed, if we are wrong about this, if M (x, y) = S(y) for a sequence of
x, y with y > (1 + ϵ) log x and x arbitrarily large, then this would contradict the key
conjecture in section 1.2.
More discussion of this heuristic in section 4, as well as in sections 8.1 and 9.1

1.2. Intermediate length intervals: log x ≤ y = o((log x)2). In this range we be-
lieve that (1) holds:

M (x, y) ∼ L(x, y) where L(x, y) := log x

log ( (log x)2

y ).

PRIMES IN SHORT INTERVALS: HEURISTICS AND CALCULATIONS 5

However, when comparing this prediction to the data, it is not obvious how to interpret
“o((log x)
2)” for a given x-value. We have made the rather arbitrary choice of 1
2(log x)
2

as the upper bound for the y-range. We have also taken 1
2 log x as a lower bound
which reﬂects our uncertainty as to whether things can really be predicted so precisely,
though we have marked log x with a dashed line.

0 50 100 150 200
y

5

10

15

20

25

30M(109,y)
M (109, y)
 M (109, y)

L(109, y)

log 109

0 50 100 150 200 250
y

5

10

15

20

25

30M(1010,y)
M (1010, y)
 M (1010, y)

L(1010, y)

log 1010

0 50 100 150 200 250 300
y

5

10

15

20

25

30

35M(1011,y)
M (1011, y)
 M (1011, y)

L(1011, y)

log 1011

0 50 100 150 200 250 300 350 400
y

5

10

15

20

25

30

35

40M(1012,y)
M (1012, y)
 M (1012, y)

L(1012, y)

log 1012

Figure 2. M (x, y) vs.L(x, y) for x = 10
k, k = 9, . . . , 12 and 1
2 log x ≤
y ≤ 1
2(log x)
2. Dashed line at y = log x, which is the end of the range of
the M (x, y) = S(y) conjecture.

Here, for each y (the horizontal axis), a colored-in dot represents M (x, y), and the
continuous curve L(x, y) (our prediction in (1)). Our prediction and the data seem
to co-incide at y = log x (where the dashed line is), and again at a point that seems
to be slowly increasing (towards 1
2(log x)
2) as x grows. The graph indicates that our
prediction provides a pretty good approximation to the data in the whole range, though
it is concave up whereas the data itself appears to yield a curve that is concave down.
We have no explanation for that.

1.3. The maximum on longer intervals: y ≍ (log x)
2. Here we mean that y =
t(log x)
2 for some ﬁxed value of t. In this range we will need to deﬁne two implicit
functions to formulate our conjectures for m(x, y) and M (x, y): For every given t > 0

6 ANDREW GRANVILLE AND ALLYSA LUMLEY

consider the equation u(log u − log t − 1) + t = 1.
We will show that for every t > 0 there is a unique solution u+(t) with u+(t) > t. If
0 < t < 1 there is no solution in u ∈ (0, t), so we let u−(t) = 0. If t > 1 then there
is a unique solution u−(t) with 0 < u−(t) < t. We believe that there exist constants
c−, c+ > 0 such that if y = t(log x)
2 then

m(x, y) ∼ u−(c−t) log x and M (x, y) ∼ u+(c+t) log x. (4)

We will see at the end of section 3 that c± are constants that can be deﬁned in terms
of sieving intervals. We know that c+ ≥ 1.015 . . . and c− ≤ eγ
2 = 0.890536 . . . , and
perhaps both of these inequalities should be equalities.
3 Here is the data for M (x, y)
in this range:

200 300 400 500 600 700 800
t(log 109)2

20

30

40

50

60

70

80

90M(109,t(log109)2)
M (109, t(log 109)2)

M (109, t(log 109)2)
u+(1.015t) log 109

200 400 600 800 1000
t(log 1010)2

20

30

40

50

60

70

80

90

100M(1010,t(log1010)2)
M (1010, t(log 1010)2)

M (1010, t(log 1010)2)
u+(1.015t) log 1010

200 400 600 800 1000 1200
t(log 1011)2

40

60

80

100M(1011,t(log1011)2)
M (1011, t(log 1011)2)

M (1011, t(log 1011)2)
u+(1.015t) log 1011

200 400 600 800 1000 1200 1400
t(log 1012)2

40

60

80

100

120M(1012,t(log1012)2)
M (1012, t(log 1012)2)

M (1012, t(log 1012)2)
u+(1.015t) log 1012

Figure 3. M (x, y) vs. u+(1.015t) log x where y = t(log x)
2

. for x = 10
k, k = 9, . . . , 12 and 1
3(log x)
2 ≤ y ≤ 2(log x)
2.

Here, for each y (the horizontal axis), a colored-in dot represents M (x, y), and the
red curve represents our prediction u+(1.015t) log x where y = t(log x)
2. It appears
that this prediction is too large by a factor of about 35% (and if c+ is larger than 1.015

3We will assume that c+ = 1.015 . . . and c− = 0.8905 . . . throughout for the purpose of comparing
our conjectures to our data. We will explain the signiﬁcance of 1.015 . . . at the end of section 3.

PRIMES IN SHORT INTERVALS: HEURISTICS AND CALCULATIONS 7

then the red curve will be even further above the data). However we believe this is a
consequence of only calculating up to x = 10
12 and hopefully the data will get closer
to our curve the larger x gets.
4 In this range for y it is already well-known that data
for the minimum does not yet satisfy the standard conjectures:

1.4. The minimum on longer intervals: y ≍ (log x)
2. The prediction (4) implies
that if c−t < 1 then m(x, t(log x)
2) = 0 but not if c−t > 1. That is, we conjecture the
following lower bound for the maximal gap between consecutive primes:

max
x<pn≤2x pn+1 − pn ∼ c−1
− (log x)
2 ≥ 2e
−γ(log x)
2;

and it is feasible that we have equality here. This is larger than Cram´er’s original
conjecture (that this maximal gap is ∼ (log x)2). As we will discuss, Cram´er’s reasoning
is ﬂawed by failing to take account of divisibility by small primes (a point originally
made by the ﬁrst author back in [9] and recently re-iterated by the in-depth analysis
of Banks, Ford and Tao in [1].) However the data does not really support either
conjecture, as the largest gap between consecutive primes that has been found is about
.9206(log x)
2 (a shortfall of around 22% from 2e
−γ ≈ 1.1229 · · · ).

pn pn+1 − pn (pn+1 − pn)/ log2 pn
113 14 .6264
1327 34 .6576
31397 72 .6715
370261 112 .6812
2010733 148 .7026
20831323 210 .7395
25056082087 456 .7953
2614941710599 652 .7975
19581334192423 766 .8178
218209405436543 906 .8311
1693182318746371 1132 .9206
Figure 4. (Known) record-breaking gaps between primes

In [1] Banks, Ford and Tao graphed how the maximal gap between primes grows,
as compared to the proposed asymptotics 2e
−γ(log x)2, (log x)2 and the more precise
(log x)(log x − log log x). In section 9.5 we discuss the heuristic justiﬁcation for these
conjectures and variants. All such heuristics seem to suggest that the maximal gap
between consecutive primes up to x should grow like log x(a log x + b log log x + c) for
some constants a, b, c. The only possibilities for a seem to be a = 1 or 2e
−γ, though
there are many possible guesses for b and c. Here we graph 2e−γ(log x)
2 and (log x)
2

4One referee asks whether we expect that u+(c+t) log x ≥ M (x, t(log x)2) will persist for larger x;
we have no idea how to make predictions that are this precise, and doubt the value of trying to do so
given how far out our predictions currently are from the data!

8 ANDREW GRANVILLE AND ALLYSA LUMLEY

as well as the best ﬁt functions of the form log x(a log x + b log log x + c) where a = 1
or 2e
−γ.
5

0 250 500 750 1000 1250 1500 1750
log x

0

500

1000

1500

2000primegaps
max
pn  x pn+1   pn

2e
−log x

log x
max
pn ≤x pn ⇁   pn

log x   
 log x(log x)   
 log x

2e
−log x   5 log x(log x) + 6 log x

Figure 5. max
pn≤x(pn+1 − pn) vs. Conjectured approximations

The data for the largest gap between consecutive primes is substantially smaller than
our two predictions. No one has suggested a good reason for this shortfall, though in
appendix A we explain how at least some of this shortfall is due to the use of asymptotic
estimates for primes and sieves, for relatively small values.
In Figure 5, we have also graphed the best ﬁt to the data of curves of the form
log x(a log x + b log log x + c) with a = 1 and 2e
−γ, and the ﬁt is tight. This suggests
that we should be looking harder at possible secondary terms and reasons why they
might occur.

If (4) really does hold then m(x, y) ∼ u−(c−t) log x for y = t(log x)
2, where u−(c−t) =
0 when c−t ≤ 1, but u−(c−t) > 0 for c−t > 1. It is of interest to compare this prediction
for m(x, y) to the data, and we will assume that c− = eγ
2 = 0.8905 . . . for the purpose
of comparison:

5One referee correctly feels that it is inappropriate to try to ﬁt a justiﬁcation to the data but, who
knows, perhaps some enterprising future researcher will see a clearly good reason for our favourite
candidate, log x(2e
−ﬂ log x − 5 log log x + 6).

PRIMES IN SHORT INTERVALS: HEURISTICS AND CALCULATIONS 9

200 300 400 500 600 700 800
t(log 109)2

0

2

4

6

8

10

12

14

16m(109,t(log109)2)
m(109, t(log 109)2)

m(109, t(log 109)2)
u  (c  t) log 109

3/4(log 109)2

200 400 600 800 1000
t(log 1010)2

0

2

4

6

8

10

12

14

16

18m(1010,t(log1010)2)
m(1010, t(log 1010)2)

m(1010, t(log 1010)2)
u  (c  t) log 1010

3/4(log 1010)2

200 400 600 800 1000 1200
t(log 1011)2

0

2

4

6

8

10

12

14

16

18m(1011,t(log1011)2)
m(1011, t(log 1011)2)

m(1011, t(log 1011)2)
u  (c  t) log 1011

3/4(log 1011)2

200 400 600 800 1000 1200 1400
t(log 1012)2

0

2

4

6

8

10

12

14

16

18

20m(1012,t(log1012)2)
m(1012, t(log 1012)2)

m(1012, t(log 1012)2)
u  (c  t) log 1012

3/4(log 1012)2

Figure 6. m(x, y) vs. u−(0.8905t) log x where y = t(log x)
2

. for x = 10
k, k = 9, . . . , 12 and 1
3(log x)
2 ≤ y ≤ 2(log x)
2.

For these values of x it appears that the smallest y for which m(x, y) > 0 is at about
y = 3
4(log x)
2, which is signiﬁcantly smaller than in the prediction (though the ratio
y/(log x)
2 appears to be growing slowly with x). This conﬁrms what we saw in the
previous two ﬁgures when studying max
pn≤x(pn+1 − pn). We plotted the maximum M (x, y)

vs our prediction in this same range in Figure 3 and that data there appears to have
a similar shape to our prediction. However it is not obvious here whether the data for
the minimum, m(x, y), has a similar shape to our prediction.
We now compare our predictions for both the maxima and the minima with the data
in the range 1
3(log x)
2 ≤ y ≤ 2(log x)2, on the same graph, to get a better sense of how
well these ﬁt:

10 ANDREW GRANVILLE AND ALLYSA LUMLEY

200 300 400 500 600 700 800
y

0

20

40

60

80
 M↼
9; y↽vs m↼
9; y↽

m(109; y )

y= log(109)
u + (c+ t )log109

u Γ (cΓ t )log109

M(109; y )

200 400 600 800 1000
y

0

20

40

60

80

100
 M↼
10; y↽vs m↼
10; y↽

m(1010 ; y )

y= log(1010 )
u + (c+ t )log1010

u Γ (cΓ t )log1010

M(1010 ; y )

200 400 600 800 1000 1200
y

0

20

40

60

80

100
 M↼
11; y↽vs m↼
11; y↽

m(1011 ; y )

y= log(1011 )
u + (c+ t )log1011

u Γ (cΓ t )log1011

M(1011 ; y )

200 400 600 800 1000 1200 1400
y

0

20

40

60

80

100

120
 M↼
12; y↽vs m↼
12; y↽

m(1012 ; y )

y= log(1012 )
u + (c+ t )log1012

u Γ (cΓ t )log1012

M(1012 ; y )

Figure 7. u−(c−t) log x vs m(x, y) vs. y
log x vs. M (x, y) vs u+(c+t) log x
in ascending order, where y = t(log x)
2 for x = 10
k, k = 9, . . . , 12 and
. 1
3(log x)
2 ≤ y ≤ 2(log x)
2.

We do not know what conclusions to draw from this data!

1.5. Long intervals: y/(log x)
2 → ∞. We believe that there exist continuous func-
tions 0 < σ−(A) < 1 < σ+(A) for which σ−(A), σ+(A) → 1 as A → ∞, such that if
y/(log x)
2 → ∞ then

m(x, y) ∼ σ−(A) y
log x and M (x, y) ∼ σ+(A) y
log x (5)

writing y = (log x)
A. Moreover we should take

c− = σ−(2) and c+ = σ+(2)

above. We will obtain these conjectures from a discussion of sieve theory.
At ﬁrst sight these conjectures seem to be inconsistent with Selberg’s result that

π(x + y) − π(x) ∼ y
log x

for almost all x, assuming that y/(log x)
2 → ∞ (which he proved assuming the Riemann
Hypothesis). However the “almost all” in the statement allows for exceptions and in

PRIMES IN SHORT INTERVALS: HEURISTICS AND CALCULATIONS 11

1984, Maier [15] exhibited, for all A > 2, constants δ+(A), δ−(A) > 0 for which there
is an inﬁnite sequence of integers x+ and x− with

m(x−, y−) ≲ δ−(A) y−
log x− and M (x+, y+) ≳ δ+(A) y+
log x+
where y± = (log x±)A. As far as we know it could be that σ−(A) = δ−(A) and
σ+(A) = δ+(A) for each A, as we will discuss in sections 2.2 and 3.

1.6. Another statistic. The data in sections 1.1 and 1.2 seem to support our con-
jectures for M (x, y) in the range y = o((log x)
2), but the data in sections 1.3 and 1.4
for larger y are less encouraging. For this reason it seems appropriate to return to the
question of how M (x, y) grows as a function of y in the range y ≍ (log x)
2, and so we
examine the ratio r+(x, y) := M (x, 2y)/M (x, y).
Our asymptotic predictions suggest that this looks like 2 + o(1) if y ≤ 1
2 log x and if
y/(log x)
2 → ∞, and 1 + o(1) if log x ≤ y = o((log x)
2). For y ≍ (log x)2 our prediction
for M (x, y) is more complicated; indeed if y = t(log x)
2 then we predict that this looks
like ρ+(t) := u+(2c+t)/u+(c+t)
and we now compare this new statistic to the data:

0 50 100 150 200 250 300 350 400
t(log 109)2

1.3

1.4

1.5

1.6

1.7r+(109,t(log109)2)
r+(10
9, t(log 10
9)
2)
 r+(109, t(log 109)2)

ρ+(t)

0 100 200 300 400 500
t(log 1010)2

1.3

1.4

1.5

1.6

1.7r+(1010,t(log1010)2)
r+(10
10, t(log 10
10)
2)
 r+(1010, t(log 1010)2)

ρ+(t)

0 100 200 300 400 500 600
t(log 1011)2

1.3

1.4

1.5

1.6

1.7

1.8r+(1011,t(log1011)2)
r+(10
11, t(log 10
11)
2)
 r+(1011, t(log 1011)2)

ρ+(t)

0 100 200 300 400 500 600 700
t(log 1012)2

1.3

1.4

1.5

1.6

1.7r+(1012,t(log1012)2)
r+(10
12, t(log 10
12)
2)
 r+(1012, t(log 1012)2)

ρ+(t)

Figure 8. M (10
k, 2y)/M (10
k.y) for k = 9, . . . , 12 and y ≤ (log(10k))
2.

12 ANDREW GRANVILLE AND ALLYSA LUMLEY

We can see the shape of our prediction looks correct but it is a little on the low side.
What is encouraging is that the ﬁt seems to get better as k grows.

1.7. Summary of conjectures. We now recall in one place the conjectures given
above:
Fix ϵ > 0. If x is suﬃciently large and y ≤ (1 − ϵ) log x then

M (x, y) = S(y).

A weaker conjecture claims if y ≤ (1 − o(1)) log x and y → ∞ as x → ∞ then

M (x, y) ∼ y
log y .

If log x ≤ y = o((log x)
2) then

M (x, y) ∼ L(x, y) where L(x, y) := log x

log ( (log x)2

y ).

We conjecture that there exist constants c−, c+ > 0 such that if y = t(log x)
2 then

m(x, y) ∼ u−(c−t) log x and M (x, y) ∼ u+(c+t) log x,

and we even have tentative guesses about the values of c− and c+. Moreover this
suggests that max
x<pn≤2x pn+1 − pn ∼ c−1
− (log x)
2.

Finally for any ﬁxed A > 2 we believe that there exist continuous functions σ−(A) <
1 < σ+(A) such that if y = (log x)
A then

m(x, y) ∼ σ−(A) y
log x and M (x, y) ∼ σ+(A) y
log x.

2. Some historical comparisons

2.1. Best results known for small and large gaps between consecutive primes.
Following up the 2013 breakthrough by Yitang Zhang [24] on small gaps between
primes, Maynard [17] and Tao [22] proved that there are shortish intervals that contain
m primes for any ﬁxed m. Their remarkable work implies that there exists a constant
c > 0 such that for each y ≥ 2 we have

M (x, y) ≥ c log y if x is suﬃciently large,

which unfortunately is far smaller than what is conjectured here, in all ranges of y.
However, before Zhang’s work we could only say, for y ≪ log x, that M (x, y) ≥ 1, and
after Zhang only that M (x, y) ≥ 2, so these latest eﬀorts are signiﬁcant leap forward
in our understanding. 6

6In [19] Maynard asks similar questions for integers that are the sum of two squares. He proved
unconditionally the remarkably strong result that there are intervals (X, X + y] which contain ≫
y
(log x)1 / 2 + y1=10 integers that are the sum of two squares for all y ≥ 1. This is still much smaller than
what is probably the truth for y ≪ (log x)
c but it is at least a power of y, as we might conjecture, so
far closer to the truth than what is known unconditionally about primes.

PRIMES IN SHORT INTERVALS: HEURISTICS AND CALCULATIONS 13

Similarly Ford, Green, Konyagin, Maynard and Tao [6], following up on [5, 18],
recently showed that

m(x, y) = 0 for some y ≫ log x log log x log log log log x
log log log x ,

and they believe their technique (which consists of looking only at divisibility by small
primes) can be extended no further than y as large as (log x)(log log x)2+o(1) which is
far smaller than what is conjectured (here and previously).

2.2. Unusual distribution of primes in intervals. As discussed in section 1.5,
Maier [15] proved that there can be surprisingly few or many primes in an interval of
length (log x)A with A > 2. His proof can be easily modiﬁed to express his result in
terms of certain sieving constants: Deﬁne

S(x, y, z) := #{n ∈ (x, x + y] : (n, P (z)) = 1}

where P (z) := ∏
p≤z p, and let

S+(y, z) := max
x S(x, y, z) and S−(y, z) := min
x S(x, y, z).

For each ﬁxed u ≥ 1 we deﬁne

σ+(u) : = lim sup
z→∞ S+(zu, z)
∕{ ∏

p≤z
 (1 − 1
p
 ) · zu}

and σ−(u) : = lim inf
z→∞ S−(zu, z)
∕{ ∏

p≤z
 (
1 − 1
p
 ) · zu}.

We will discuss what we know about the constants σ−(u) and σ+(u) in the next section,
although we state here that we believe that both the limsup’s and the liminf’s are
actually limits so that

S+(zu, z) ∼ σ+(u) ∏

p≤z
 (1 − 1
p
 ) · zu and S−(zu, z) ∼ σ−(u) ∏

p≤z
 (
1 − 1
p
) · zu. (6)

Maier’s proof in [15] can be modiﬁed to show that for y = (log x)
A and z = ϵ log x
we have M (x, y) ≥ {1 + ox→∞(1)}S+(y, z) · e
γ log z
log x
which implies that there exist arbitrarily large x (= x+) for which

M (x, y) ≥ {1 + o(1)}σ+(A) y
log x .

Analogously that there are arbitrarily large x (= x−) for which

m(x, y) ≤ {1 + o(1)}σ−(A) y
log x .

If, as we believe, (6) holds then these estimates are true for all x. In (5) we have
conjectured that these bounds are “best possible”; paraphrasing, we are postulating
that Maier’s observation about the eﬀect of small prime factors is the key issue in
estimating the extreme number of primes in intervals with lengths signiﬁcantly longer

14 ANDREW GRANVILLE AND ALLYSA LUMLEY

than (log x)
2. In fact our conjectures come from ﬁrstly sieving by small primes, and
secondly looking at the tail probabilities of the binomial distribution that comes from
a probabilistic model which takes account of divisibility by small primes.
We will study in Appendix B how well some (relatively small) data for the full
distribution compares to reality.

3. Sieve methods and their limitations

Let A be a set of integers (of size y) to be sieved (in our case the integers in the
interval (X, X + y]), such that

#{a ∈ A : d|a} = g(d)
d X + r(A, d)

where g(d) is a multiplicative function, which is more-or-less 1 on average over primes
p in short intervals (in our case each g(p) = 1), and the error terms r(A, d) are small
on average (in our case each |r(A, d)| ≤ 1). The goal in sieve theory is to give upper
and lower bounds for
 S(A, z) := {n ∈ A : (n, P (z)) = 1}.

This equals G(z)y “on average” where G(z) := ∏
p≤z(1 − g(p)
p ). In 1965, Jurkat and
Richert [14] showed that if y = zu then

(f (u) + o(1)) · G(z)y ≤ S(A, z) ≲ F (u) · G(z)y, (7)

where f (u) = eγ(ω(u) − ρ(u)
u ) and F (u) = eγ(ω(u) + ρ(u)
u ), and ρ(u) and ω(u) are
the Dickman-de Bruijn and Buchstab functions, respectively. One can deﬁne these
functions directly by
 f (u) = 0 and F (u) = 2eγ

u for 0 < u ≤ 2

(in fact F (u) = 2eγ
u also for 2 < u ≤ 3) and

f (u) = 1
u
 ∫ u−1

1 F (t)dt and F (u) = 2e
γ

u + 1
u
 ∫ u−1

2 f (t)dt for all u ≥ 2.

Iwaniec [13] and Selberg [21] showed that this result is “best possible” by noting that
the sets A
± = {n ≤ x : λ(n) = ∓1}

where λ(n) is Liouville’s function (so that λ(
∏
p pep) = (−1)
∑p ep) satisfy the above
hypotheses, with

S(A
−, z) ∼ f (u) · G(z)#A
− and S(A
+, z) ∼ F (u) · G(z)#A
+. (8)

Since our question (bounding S(x, y, z)) is an example of this linear sieve we deduce
that f (u) ≤ σ−(u) ≤ 1 ≤ σ+(u) ≤ F (u),

PRIMES IN SHORT INTERVALS: HEURISTICS AND CALCULATIONS 15

and we expect that all of these inequalities are strict. However, in [11], it is shown that
if there are inﬁnitely many “Siegel zeros”,7 then, in fact,

σ−(u) = f (u) and σ+(u) = F (u) for all u ≥ 1.

Given that eliminating Siegel zeros seems like an intractable problem for now, we are
stuck. However in this paper we are allowed to guess at the truth, though we know
too few interesting examples to even take an educated guess as to the true values of
σ−(u) and σ+(u). It is useful to note the following:

Lemma 1. σ+(u) is non-increasing, σ−(u) is non-decreasing, and σ+(u), σ−(u) → 1
as u → ∞

Proof of Lemma 1. Select x so that S(x, zB, z) = S+(zB, z) is attained. For A < B,
partition the interval (x, x + zB] into zB−A disjoint subintervals of length zA, and select
the subinterval with #{n ∈ (X, X + zA] : (n, P (z)) = 1} maximal. Therefore

S+(zA, z) ≥ max
X=x+jzA

0≤j≤zB−A−1
 #{n ∈ (X, X + zA] : (n, P (z)) = 1}

≥ 1
zB−A #{n ∈ (x, x + zB] : (n, P (z)) = 1} = S+(zB, z)
zB−A ,

so that σ+(A) ≥ σ+(B). The analogous proof, with the inequalities reversed, yields
the result for σ−.
The fundamental lemma of the small sieve (see, eg, [8]) gives that

S(x, zu, z) = {1 + O(u
−u)} ∏

p≤z
 (
1 − 1
p
 ) · zu

so that σ+(u), σ−(u) = 1 + O(u
−u) = 1 + ou→∞(1). □

3.1. Best bounds known. In Maier’s paper he used the well-known fact that for all
u ≥ 1,
 #{n ≤ zu : (n, P (z)) = 1} ∼ ω(u) zu

log z
where ω(u) is the Buchstab function, deﬁned by ω(u) = 1
u for 1 ≤ u ≤ 2, and (uω(u))
′ =
ω(u − 1) for all u ≥ 2. By Lemma 1 we have

σ+(A) = max
B≥A σ+(B) ≥ e
γ max
B≥A ω(B),

and, similarly, σ−(A) ≤ eγ minB≥A ω(B). For all we know, it could be that

σ+(A) = e
γ max
B≥A ω(B).

That is, it could be that the most extreme example of sieving an interval, S(x, zA, z),
occurs where |x| < zO(1), that is when x is very small, but there is little evidence that
there are no other intervals with even more extreme behaviour.

7That is, putative counterexamples to the Generalized Riemann Hypothesis, the most egregious
that cannot be ruled out by current methods.

16 ANDREW GRANVILLE AND ALLYSA LUMLEY

In [16], Maier and Stewart noted one could obtain smaller upper bounds for σ−(A)
for small A. Their idea was to construct a sieve based on the ideas used to prove that
there are long gaps between primes: Fix 2 > u > 1. One ﬁrst sieves the interval [1, x]
where x = zu with the primes in (z1/v, z] where 1 ≤ v ≤ 1
u−1. The integers left are
the z1/v-smooth integers up to x, and the integers of the form mp ≤ x for some prime
p ∈ (z, x] (note that m ≤ x/p < x/z = zu−1 ≤ z1/v). The number of these is

ψ(zu, z1/v) + ∑

z<p≤x
 [x
p
 ] ≲ xρ(uv) + x ∑

z<p≤zu
 1
p ∼ x(ρ(uv) + log u).

Next we sieve “greedily” with the primes ≤ z1/v so that the number of integers left is

≲ ∏

p≤z1/v
 (1 − 1
p
 ) · x(ρ(uv) + log u) ∼ v(ρ(uv) + log u)e
−γx
log z

We now select v = vu ∈ [1, 1
u−1] to minimize ru(v) := v(ρ(uv) + log u). Since

ru(v)
′ = ρ(uv) + log u + uvρ
′(uv) = ρ(uv) + log u − ρ(uv − 1),

we select vu so that r′
u(vu) = 0. If u = 1 + 1/∆ with 1/∆ = o(1) then

vu ∼ log ∆
log log ∆ and so ru(vu) ∼ log ∆
∆ log log ∆ .

On the other hand if we use the Buchstab function then we cannot obtain a constant
smaller than e
γ/2. Thus for 1 ≤ A ≤ 2, we have

σ−(A) ≤ min{e
γ/2, rA(vA)}

In [16] this argument is extended to show that rA(vA) is the minimum exactly when
1 ≤ A ≤ 1.50046 . . . . Unfortunately we are only really interested in σ−(A) for A ≥ 2
in this article.
Now ω′(u) changes sign in every interval of length 1, so ω(u) has lots of minima and
maxima, which occur whenever ω(u) = ω(u − 1) (since uω′(u) = ω(u − 1) − ω(u)).
Nonetheless its global minimum occurs at u = 2 so that σ−(2) ≤ e
γω(2) = eγ
2 (and we
saw earlier that the linear sieve bounds give σ−(2) ≥ 0). We are most interested in
σ+(2), which is bounded below by e
γ maxB≥2 ω(B). This maximum occurs at B ≈ 2.75
with ω(B) ≈ 0.57, so that σ+(2) ≥ 1.015 . . . (and we saw earlier that the linear sieve
bounds give σ+(2) ≤ eγ = 1.78107 . . . )
In section 1.3 we have c+ = σ+(2)

and took this to be equal to 1.015 . . . in our computations as this is the best lower
bound known on σ+(2). Similarly in section 1.4 we have

c− = σ−(2)

and took this to be equal to eγ
2 in our model as this is the best upper bound known on
σ−(2). It could be that these are equalities, but there is little evidence either way.

PRIMES IN SHORT INTERVALS: HEURISTICS AND CALCULATIONS 17

4. Very short intervals (y ≤ log x)

If a set of integers A is inadmissible then there exists a prime p which divides n + a
for some a ∈ A, for each integer n, and so obstructs these from all being simultaneously
prime, once n is suﬃciently large. On the other hand, Hardy and Littlewood’s prime
k-tuplets conjecture [12] states that if A is an admissible set then there are inﬁnitely
many integers n for which n+a is prime for every a ∈ A, and this seems to be supported
by an accumulation of evidence.
We are interested in π(n, n + y], the number of primes in intervals (n, n + y] of length
y (with y small compared to n), particularly the minimum, m(x, y), and the maximum,
M (x, y), as n varies between x and 2x. If the primes in (n, n + y] are {n + a : a ∈ A}
with n > y, then A is an admissible set, say of size k, and therefore

π(n, n + y] := π(n + y) − π(n) = k ≤ S(y),

where S(y) is the maximum size of an admissible set A of length y. Moreover this
implies that if the prime k-tuplets conjecture holds then

max
n≥y π(n, n + y] = S(y).

How large is S(y)? One can show that the primes in (y, 2y] yield an admissible set and
so S(y) ≳ y
log y (by the prime number theorem). It is believed that

S(y) ∼ y
log y

but the best upper bound known is S(y) ≲ 2y
log y (by the upper bound in (7)), and this
upper bound seems unlikely to be signiﬁcantly improved in the foreseable future (as we
again run into the Siegel zero obstruction). Calculations support the believed size of
S(y). One interesting theorem, due to Hensley and Richards, is that if y is suﬃciently
large then S(y) > π(y) and so, if the prime k-tuplets conjecture is true then for all
suﬃciently large y there exist inﬁnitely many intervals of length y that have more
primes than the initial interval [1, y]. The known values of S(y) and bounds, can be
found on http://math.mit.edu/∼primegaps/ and from there we see that S(3432) ≥
481 > π(3432) = 480. Therefore we believe that there are inﬁnitely many intervals of
length 3432 containing exactly 481 primes, more than the 480 primes ≤ 3432 found at
“the start”. However, ﬁnding such an interval (via methods based on this discussion)
involves ﬁnding a prime 481-tuple, which would be an extraordinary challenge unless
one is very lucky.
So assuming the prime k-tuplets conjecture we know that maxn≥y π(n, n + y] = S(y)
for ﬁxed y, and we might expect that M (x, y) = S(y) for y which (slowly) grows with
x. In sections 4.1 and 8.1 we present two quite diﬀerent heuristics to suggest that

M (x, y) = S(y) for all y ≤ {1 − o(1)} log x; (9)

and we saw, in section 2.1, that this is well supported by the data that we have.
By a simple sieving argument Westzynthius showed in the 1930s that for any constant
C > 0 there exist intervals [x, x + C log x] which do not contain any primes. This

18 ANDREW GRANVILLE AND ALLYSA LUMLEY

argument is easily modiﬁed to show that for any c > 0

m(x, c log x) := min
X∈(x,2x](π(X + c log x) − π(X)) = 0 if x is suﬃciently large.

We will give two theoretical justiﬁcations for our prediction (9), supporting the
conclusions we have drawn from the data represented in the graphs above. The ﬁrst is
explained in the next section and relies on guessing at what point a given admissible set
yields roughly as many prime k-tuplets as conjectured. The second a more traditional
approach is explained in section 8.1, developing the Gauss-Cram´er heuristic (given in
section 6) so that it takes account of divisibility by small primes.

4.1. An explicit prime k-tuplets conjecture. For a given admissible set of linear
forms bjn + aj, j = 1, . . . , k, Hardy and Littlewood [12] conjectured that

#{x < n ≤ 2x : Each bjn+aj is prime} ∼ ∏

p
 (1− 1
p
 )−k(1− ω(p)
p
 )· x
(log x)k , (10)

where ω(p) is the number of n (mod p) for which p divides ∏k
j=1(bjn + aj).
8 We wish
to know for what x are the two sides of (10) equal up to a small factor, and for what
x can we obtain a good lower bound on the right-hand side.
This conjecture is known to be true as x → ∞ for k = 1 (where we may assume that
1 ≤ a ≤ b − 1). There is a lot of data on primes in arithmetic progression and these
all suggest that (10) holds uniformly for all x ≥ bϵ for any ﬁxed ϵ > 0.
9

Let A be an admissible set of size k = S(y) ∼ αy
log y (where we believe α = 1), a subset
of the positive integers ≤ y. Since there are ≪ y
(log y)2 integers in S(y) that are < y
log y
(by the sieve), we deduce that Q := ∏
a∈A a = e
(α+o(1))y = k(1+o(1))k. Now ω(p) = k for
all p ≥ y (since no two elements of A can be in the same congruence class mod p), so
that ∏

p>y
 (
1 − 1
p
 )−k(
1 − ω(p)
p
 ) = ∏

p>y
 (
1 − 1
p
)−k(
1 − k
p
 ) = e
−o(k2/y).

Otherwise 1 ≤ ω(p) ≤ min{k, p − 1} so that

e
o(k) = ( log 2y
log k
 )k ≫ ∏

y≥p>k
 (1 − 1
p
 )−k(1 − ω(p)
p
 ) ≥ e
−o(k).

For the primes ≤ k we have p − 1 ≥ ω(p) ≥ 1 and so

1 ≥ ∏

p≤k
 (1 − ω(p)
p
 ) ≥ 1
∕ ∏

p≤k p = e
−k+o(k).

8Here admissible can be deﬁned to be those k-tuples for which every ω(p) < p. A set A is admissible
if and only if the set {n + a : a ∈ A} of linear forms is admissible.
9Surprisingly there is no way known to try to prove this. The best we know how to obtain, assuming
the Generalized Riemann Hypothesis, is that if k = 1 then (10) holds for all x ≥ b1+ﬄ, though this
can be obtained “on average” unconditionally. Linnik’s Theorem implies that there exists a constant
λ such that one can obtain a lower bound on the left-hand side of (10) once x ≫ b
˘ (and so there is a
prime ≪ b
˘ +1 in each reduced residue class mod b). In 2011, Xylouris [23] showed that we can take
λ = 4, the smallest λ known-to-date

PRIMES IN SHORT INTERVALS: HEURISTICS AND CALCULATIONS 19

Therefore, by Mertens’ theorem, we have

∏

p
 (1 − 1
p
 )−k(1 − ω(p)
p
 ) = (eO(1) log k)
k.

So there exists a constant C > 0 such that the right-hand side of (10) is ≥ 1 when
(C log k)
kx > (log x)
k. This certainly happens when x = kck for any ﬁxed c > 1; that
is, x > Q
1+ϵ. One might guess that there is an error term in (10) of size x1/2+o(1), in
which case we must take c > 2, that is x > Q
2+ϵ, to guarantee that the left-hand side
of (10) is positive.
Now if #{x < n ≤ 2x : Each n + a is prime, for each a ∈ A} ≥ 1 then M (x, y) =
S(y). From the above we might guess this holds when x > Q
1+ϵ where Q = e(1+o(1))y;
that is, if y ≤ (1 − o(1)) log x. Indeed we only need the above heuristic discussion to be
roughly correct “on average” over all such admissible sets, to support the conjecture
in (9).10
 5. Cram´er’s heuristic

Gauss noted from calculations of the primes up to 3 million, that the density of
primes at around x is about 1
log x. Cram´er used this as his basis for a heuristic to
make predictions about the distribution of primes: Consider an inﬁnite sequence of
independent random variables (Xn)n≥3 for which

Prob(Xn = 1) = 1
log n and Prob(Xn = 0) = 1 − 1
log n.

By determining what properties are true with probability 1 + o(1) for the sequence of
0’s and 1’s given by X3, X4, . . . , Cram´er suggested that such properties must also be
true of the sequence 1, 0, 1, 0, 1, 0, 0, 0, 1, . . . of 0’s and 1’s which is characteristic of the
odd prime numbers. For example, if N is suﬃciently large then

SN :=
 N∑

n=3 Xn

has mean ∫ N
2 dt
log t + O(1) and roughly the same variance, which suggests the conjecture

that π(N ) = ∫ N
2 dt
log t + O(N 1/2+o(1)); it is known that this conjecture is equivalent to
the Riemann Hypothesis. So for this particular statistic, Cram´er’s heuristic makes an
important prediction and it can be applied to many other problems to make equally
suggestive predictions.
However Cram´er’s heuristic does have an obvious ﬂaw: Since it treats all the random
variables as independent, we have Prob(Xn = Xn+1 = 1) ≈ 1
(log n)2 , so that

E
( N −1∑

n=3 XnXn+1
) = ∫ N

2
 dt
(log t)2 + O(N 1/2+o(1))

10This reasoning suggests that even if we are pessimistic then we would simply change the range
in (9) to y ≤ (c + o(1)) log x for some constant c ∈ (0, 1).

20 ANDREW GRANVILLE AND ALLYSA LUMLEY

with probability 1 + o(1), which, Cram´er’s heuristic suggests, implies that there are
inﬁnitely many prime pairs n, n + 1. But we have seen this is not so as {0, 1} is an
inadmissible set. More dramatically this heuristic would even suggest that M (x, y) = y
for all values of y ≤ {1 + o(1)} log x. From the previous section we know that this is
false because M (x, y) ≤ S(y), as every π(n, n + y] is restricted by those integers that
are divisible by “small” primes, that is primes ≤ y1+o(1). This heuristic also suggests
that the primes are equi-distributed amongst all of the residue classes modulo a given
integer q, rather than just the reduced classes.
It therefore makes sense to modify Cram´er’s probabilistic model for the primes to
take account of divisibility by “small” primes. The obvious way to proceed is to begin
by sieving out the integers n that are divisible by a prime p ≤ z (perhaps with z = y),
and then to apply an appropriate modiﬁcation of Cram´er’s model to the remaining
integers, that is the integers that have no prime factor ≤ z. The number of such
integers up to x is
 ∼ κx where κ = κ(z) := ∏

p≤z
 (
1 − 1
p
 )

if z = xo(1), and so the density of primes amongst such integers is 1
κ log x. We therefore
proceed as follows:
Deﬁne P = P (z) := ∏
p≤z p so that κ(z) = φ(P )
P . We consider an inﬁnite sequence of
independent random variables (Xn)n≥3 for which Xn = 0 if (n, P ) > 1; and

Prob(Xn = 1) = 1
κ log n and Prob(Xn = 0) = 1 − 1
κ log n if (n, P ) = 1.

With this model we can again accurately predict the prime number theorem (and the
Riemann Hypothesis), as well as asymptotics for primes in arithmetic progressions, for
prime pairs, and even for admissible prime k-tuplets (with k ≤ z). Moreover, this
will allow us to obtain our predictions for maximal and minimal values of π(x, x + y]
(including the prediction for y ≪ log x that we already deduced from assuming enough
uniformity in the prime k-tuplets conjecture in section 4.1).
If n ∈ (x, 2x] with (n, P ) = 1 then Prob(Xn = 1) = 1
L + O( 1
L log x) where L := κ log x,
so for convenience we will work with a model where each Prob(Xn = 1) = 1
L . There
are, say, N integers in (X, X + y] that are coprime to P where, a priori, N could be
any number between 0 and y (though we can reﬁne that to 0 ≤ N ≤ S+(y, z) ≪ y
log z
by the sieve). We now develop a model where L and N are ﬁxed:

6. The maxima and minima of a binomial distribution

Suppose that we have a sequence of independent, identically distributed random
variables X1, . . . , XN with

P(Xn = 1) = 1
L and P(Xn = 0) = 1 − 1
L,

where L is large. Let Y := ∑

n≤N Xn.

PRIMES IN SHORT INTERVALS: HEURISTICS AND CALCULATIONS 21

Then Y is a binomially distributed random variable, which is often denoted B(N, 1
L ).

Proposition 1. Suppose that N ≪ L log x, and that L → ∞ as x → ∞. If k− =
k−(N, L, x) is the largest integer for which

P(Y < k−) ≤ 1
x
then
 k− =
 { 0 if N ≤ {1 + o(1)}L log x;
{δ−(λ) + o(1)} N
L if N = {λ + o(1)}L log x with λ > 1;

where δ− = δ−(t) is the smallest positive solution to δ(log δ − 1) + 1 = 1/t.
If k+ = k+(N, L, x) is the smallest integer for which

P(Y ≥ k+) ≤ 1
x .

then
 k+ =
 



 N if N ≤ log x
log L;
{1 + o(1)} log x

log ( L log x
N ) if log x
log L ≤ N = o(L log x);

{δ+(λ) + o(1)} N
L if N = {λ + o(1)}L log x with λ > 0;

where δ+ = δ+(t) is the largest positive solution to δ(log δ − 1) + 1 = 1/t. We observe
that k− ≤ k+ ≪ log x if N ≪ L log x.

Proof. From the independent binomial distributions we deduce that if 0 ≤ k ≤ N then

P(Y = k) = P( ∑

n≤N Xn = k) = (
N
k
 )( 1
L
)k(
1 − 1
L
)N −k.

Therefore P(Y = N ) = 1/L
N and this is > 1/x provided N ≤ log x
log L .
Also P(Y = 0) = (1 − 1
L )
N = e
−N/L+O(N/L2) which is > 1
x for N ≤ {L + O(1)} log x.11

We now estimate the terms in our formula for P(Y = k):
(
N
k
 ) = N k

k!
 k−1∏

i=0
 (
1 − i
N
 ) = N k

(k/e)k kO(1) exp ( k−1∑

i=0 O( i
N
 ))

= N k

(k/e)k exp (
O( k2

N + log k)).

by Stirling’s formula. We also have (1 − 1
L)N −k = exp(− N
L + O( k
L + N
L2 )), and so

P(Y = k) = ( eN
kL
 )k exp ( − N
L + O( k2

N + log k + k
L + N
L2
 ))

Therefore if N = o(L log x) and k = o(log x) then k2/N ≤ k = o(log x) so that

P(Y = k) = ( eN
kL
 )kxo(1),

11To be more precise we obtain N ≤ log x
− log(1− 1
L ) = (L − 1
2 − 1
12L + O( 1
L 2 )) log x.

22 ANDREW GRANVILLE AND ALLYSA LUMLEY

and this equals x−1+o(1) if and only if

k ∼ log x
log( L log x
N )

Finally we deal with the range N = λL log x with λ > 0. If k = δλ log x with δ > 0
then, by the above estimate,

P(Y = k) = ( eλ log x
k
 )k exp ( − λ log x + O( log x
L
 )) = 1/x
λ(1−δ log(e/δ))+o(1),

which equals 1/x1+o(1) if δ = δ±(λ) so that λ(1 − δ log(e/δ)) = 1. □

Remark. There are well-known bounds on the tail of the binomial distribution (see,
e.g., [4]) which can be used to obtain this last result:

1
√
8k(1 − k
N ) exp (
−N D
( k
N
 ∣
∣
∣
∣ 1
L
)) ≤
 {
P(Y ≤ k) if k ≤ N
L
P(Y ≥ k) if k ≥ N
L ≤ exp (−N D( k
N
 ∣
∣
∣
∣ 1
L
))

where
 D(a|p) := a log a
p + (1 − a) log 1 − a
1 − p
which is called the relative entropy in some circles (this clean upper bound can be
obtained by an application of Hoeﬀding’s inequality); the two cases are equivalent since
if k ≥ N
L then D(1 − a|1 − p) = D(a|p). Using these inequalities we would determine
δ = δ(t, L) from the functional equation

L D
( δ
L
∣
∣
∣
∣ 1
L
) = 1
t
 (
1 + O( log log x
log x
 )),

which is slightly diﬀerent, but yields δ(t, L) = δ(t) + O( 1
log δ(t) ( 1
L + log log x
log x )), a negligible
diﬀerence in the ranges we are concerned about.

7. Asymptotics

In section 1.3 we used the solutions u = u− ∈ (0, t) and u = u+ ∈ (t, ∞) to

u(log u − log t − 1) + t = 1

where u(t) = tδ(t), and δ = δ− ∈ (0, 1) and δ = δ+ ∈ (1, ∞) are the solutions to

f (δ) := 1 − δ log(e/δ) = 1
t .

To verify these claims, we note that f (0) = 1, f (1) = 0 and f (∞) = ∞ We have
df
dδ = log δ so f (as a function of δ) has its minimum f (1) = 0 with f ′′(δ) > 0 for all
δ > 0. Therefore there exists a unique δ− ∈ (0, 1) with f (δ−) = 1/t for all t > 1 and no
such δ− otherwise. Moreover δ−(t) is an increasing function with limit 1. Also, there
exists a unique δ+ > 1 with f (δ+) = 1/t for all t > 0. Moreover δ+(t) is a decreasing
function with limit 1.

PRIMES IN SHORT INTERVALS: HEURISTICS AND CALCULATIONS 23

We will now show that u+(t) is increasing in t > 0 and u−(t) is increasing in t ≥ 1
Diﬀerentiating f (δ) = 1
t we obtain log δ · dδ
dt = − 1
t2 . Therefore

d
dt log u(t) = d
dt log tδ = 1
δ dδ
dt + 1
t = 1
t − 1
t2δ log δ = tδ log δ − 1
t2δ log δ = δ − 1
tδ log δ > 0

for all δ > 0.
We can be more precise about the limits:

7.1. Estimates as t → ∞. Write δ = 1 + θ so that

1 − 1/t = (1 + θ)(1 − log(1 + θ)) = 1 − θ2

2 + θ3

6 − θ4

12 + . . .

Therefore θ = ± 21/2

t1/2 + 1
3t ± 1
9(2t)3/2 + O( 1
t2 ) as t → ∞, so that

u+(t) = tδ+(t) = t + (2t)
1/2 + 1
3 + 1
9 · 23/2t1/2 + O(1
t )

u−(t) = tδ−(t) = t − (2t)
1/2 + 1
3 − 1
9 · 23/2t1/2 + O(1
t ),

for large t. So if t is large and N = tL log x then, in Proposition 1,

k± = (
t ± (2t)1/2 + 1
3 − O( 1
t1/2
 )) log x as t → ∞.

7.2. Approximating the normal distribution. A random variable given as the sum
of enough independent binomial distributions tends to look like the normal distribution,
at least at the center of the distribution. However since we are looking here at tail
probabilities, the explicit meaning of “enough” is larger than we are used to. To be
speciﬁc, Y has mean µ := N
L and variance σ2 = N
L (1 − 1
L ), and we expect Y will
eventually be normally distributed with these parameters. If so, then

P(Y < µ − τ σ), P(Y > µ + τ σ) ≈ 1
√2π
 ∫ ∞

τ e−t2/2dt ∼ e−τ 2/2

τ √2π

and if this is ≈ 1/x then τ ∼ √2 log x. Therefore τ σ ∼ (2 N
L log x)1/2. Writing N =
λL log x we have τ σ ∼ (2λ)
1/2 log x. Therefore we might expect the maximum and
minimum values of Y to be (λ ± (2λ)
1/2 + o(1)) log x. We see from section 7.1 that this
is correct as λ → ∞ (but not for ﬁxed λ).
We can see this issue more simply: If k = κN/L with κ > 1 then the binomial
distribution gives

Prob(Y ≥ k) ≍ (
1 − 1
L
)N (N
k
 ) 1
(L − 1)k = exp ( − N
L (κ(log κ − 1) + 1 + o(1))
)

and the normal distribution (with the same mean and variance) gives

Prob(Y ≥ k) = exp ( − N
L ( 1
2(κ − 1)
2 + o(1))
)

and the main terms here are only the same when κ → 1
+.

24 ANDREW GRANVILLE AND ALLYSA LUMLEY

7.3. Estimates as t → 0
+. In the other direction we obtain estimates for δ±(t) as t
gets smaller.
If t → 0
+ then we deduce from δ+(log δ+ − 1) + 1 = 1/t that

δ+(t) = 1/t

log ( 1/t
e log 1/t) (1 + O( log log 1/t
(log 1/t)2
 )) (11)

so that
 u+(t) = tδ+(t) = 1
log(1/t)
(
1 + O( log log 1/t
log 1/t
 ))

and therefore
 k+ ∼ u+(t) log x ∼ log x
log(1/t) as t → 0
+.

Combining this with the second estimate for k+ in Proposition 1, we deduce that k+(N )
is a continuous function in N in the range of Proposition 1.
If t → 1
+ then writing t = 1 + η with η > 0 small and δ− = 1/B, we deduce from
δ−(1 − log δ−) + 1 = 1/t that 1+log B
B = η + O(η2) and so

1/δ− = B = (1/η) log(1/η)(
1 + O( log log 1/η
log 1/η
 ))
.

This implies that
 u−(t) = tδ−(t) = η
log(1/η)
(
1 + O( log log 1/η
log 1/η
 ))

and therefore
 k− ∼ u−(t) log x ∼ (t − 1) log x
log( 1
t−1) as t → 1
+,

which → 0 as t → 1
+. This suggests that k− = 0 for N < {1 − o(1)}L log x but grows
like N − L log x
L log N
N −L log x
for a small range near L log x which we denote by L log x < N < {1 + o(1)}L log x.

8. Applying the modified Cram´er heuristic

Here is the general set-up. For some z ≤ y deﬁne P = P (z) := ∏
p≤z p so that
P (z) = e
(1+o(1))z by the prime number theorem. For S(x, y, z) := #{n ∈ (x, x + y] :
(n, P (z)) = 1} (as in section 2.2) we deﬁne

I(N ) = {X ∈ (x, 2x] : S(X, y, z) = N }.

for each integer N in the range 0 ≤ N ≤ S+(y, z). Our heuristic is that the values

π(X, X + y] for X ∈ I(N ),

are distributed like the binomially distributed random variable

B(N, 1
L ) where L = φ(P )
P log x.

PRIMES IN SHORT INTERVALS: HEURISTICS AND CALCULATIONS 25

We therefore use Proposition 1 (with x there equal to #I(N )) to predict the value of

MN (x, y) := max
X∈I(N ) π(X, X + y]

for each N with I(N ) non-empty. From these predictions we obtain our predictions for

M (x, y) = max
N MN (x, y).

One can work out the details of this heuristic to make precise conjectures provided
we can get a good estimate for log #I(N ). This is not diﬃcult when z ≤ ϵ log x: For
each m, 0 ≤ m ≤ P − 1 we have

S(X, y, z) = S(m, y, z) whenever X ≡ m (mod P (z)),

since (X + j, P ) = (m + j, P ) for all j. Moreover these intervals (X, X + y] with
X ≡ m (mod P (z)) are all disjoint so can be considered to be independent. Therefore
if N = S(m, y, z) then P = P (z) ≤ xϵ+o(1) and so

#I(N ) ≥ #{X ∈ (x, 2x] : X ≡ m (mod P (z))} = x/P + O(1) ≥ x1−ϵ+o(1).

Hence, when z is this small, the answer given by our heuristic depends only on the
extreme values, S−(y, z) and S+(y, z).
Getting a good estimate for log #I(N ) is not straightforward if z (and therefore y) is
signiﬁcantly larger than log x. However one expects our heuristic to be more accurate
the larger z is, so we have to ﬁnd the right balance in our selection of z.

8.1. Very short intervals (y ≪ log x). If y ≤ η log x with 0 < η < 1
2 small, then the
above discussion suggests taking z = y. Hence S+(y, z) = S+(y, y) = S(y). For each
m (mod P ) we apply Proposition 1 with

N = S(m, y, y), L = φ(P )
P log x, and x replaced by x1−η.

For given L and x, one obtains the largest value of k+ in Proposition 1, when N is as
large as possible. This happens here when N = S(y), which we believe is ∼ y
log y and
know is no more than twice this. Now L ≍ log x
log y and Proposition 1 then implies that
k+ = N = S(y) as long as S(y) ≤ (1 − η + o(1)) log x
log L, which should be true for any
ﬁxed η < 1
2 (and at worst for η < 1
3).
This supports the conjecture (9) in a range like y ≤ ( 1
2 − o(1)) log x. What about
for larger y?

8.2. Larger y with a diﬀerent choice of intervals. For larger y, say log x ≪ y <
(log x)A with A > 2, we need to decide how to select our value for z. One might guess
that the right way to do so is to take z = y.12 That is, to sieve the intervals of length
y with all of the primes ≤ z = y, and then apply the modiﬁed Cram`er model. In this
case the sets {j ∈ [1, y] : (X + j, P ) = 1} are probably diﬀerent for every X ∈ (x, 2x]
(certainly they do not repeat periodically as in the earlier subsection), which seems

12We do not wish to sieve with primes larger than the length of the interval, since any larger
primes cannot divide more than one element in an interval of length y, so cannot be helpful in a sieve
argument.

26 ANDREW GRANVILLE AND ALLYSA LUMLEY

diﬃcult to cope with. However we do not need to understand these sets so precisely,
we only need to understand their size, that is, to have good estimates for log #I(N )
for each N , but even this seems to be out of reach. Therefore this is the less desirable
option (though we work through some of the details in Appendix C). In general, we do
not know how to get good estimates for log #I(N ) whenever z is substantially larger
than log x.
These (for now insurmountable) issues, suggest that we should proceed as before,
with a smallish value of z, so as to recover the sieved sets repeating predictably. There-
fore we pre-sieve the intervals of length y with all of the primes ≤ z := ϵ log x, and then
apply the modiﬁed Cram`er model. There might be a substantial diﬀerence when siev-
ing with the primes ≤ z, as opposed to y, though we hope not. If there is a substantial
diﬀerence then this needs further investigation.

8.3. Larger y; Predictions by pre-sieving up to z = o(log x). We pre-sieve with
the primes up to z = ϵ log x where ϵ → 0 very slowly as x → ∞. In this case we have
seen that we may cut to the chase by taking

N+ = S+(y, z) =: e−γ y
log z c+ and L = φ(P )
P log x ∼ e−γ log x
log log x

Prediction: Pre-sieving up to z = ϵ log x: If log x ≪ y = o((log x)
2) then

M (x, y) = min {S+(y, z), {1 + o(1)} log x

log ( (log x)2

y )
 }
.

If y = λ(log x)
2 with λ > 0 then

M (x, y) ∼ u+(λc+)log x and m(x, y) ∼ u−(λc−)log x.

If y ≍ log x then this might predict that M (x, y) = S+(y, z) > S(y) which is
obviously false (though not by much) – in this range it therefore makes sense to sieve
up to z = y, which will assure the feasible prediction M (x, y) = S(y) (as we work out
in Appendix C).
If λ is large and y = λ(log x)
2 then

u+(λc+) = λc+ + √
2λc+ + O(1),

and so M (x, λ(log x)
2) ∼ c+ y
log x as λ → ∞; and analogously m(x, λ(log x)2) ∼ c− y
log x .

Deduction from the predictions of Proposition 1. We apply Proposition 1 to predict,
for each 0 ≤ j ≤ P − 1 where P = P (z),

Mj(x, y) := max
X∈(x,2x]
X≡j (mod P ) π(X + y) − π(X)

and then we guess that M (x, y) = maxj Mj(x, y). We observe that

#{X ∈ (x, 2x] : X ≡ j (mod P )} = x
P + O(1) = x1−o(1)

for each j, so we apply Proposition 1 to a set of this size, and the result follows directly.
The analogous proof works for m(x, y). □

PRIMES IN SHORT INTERVALS: HEURISTICS AND CALCULATIONS 27

9. Which choices should we make?

We will now distill these discussions, which each yield slightly diﬀerent predictions.

9.1. Very short intervals (y ≪ log x). In section 1.1, we predicted that if y ≤ c log x
then M (x, y) = S(y). This was conﬁrmed by one heuristic in section 4.1, and by a very
diﬀerent heuristic in section 8.1, giving us some conﬁdence in this conclusion.
From all three discussions it is not obvious what explicit constant one should take
in place of the inexplicit “c”. Our guess is that for any ϵ > 0 one has

M (x, y) = S(y) for y ≤ (1 − ϵ) log x,

if x is suﬃciently large, as well

M (x, y) ∼ log x
log log x for (1 − ϵ) log x ≤ y ≤ (1 + o(1)) log x.

The “o(1)” is inexplicit and our methods do not pinpoint the transition more accurately.
The data represented in ﬁgure 1 appear to more-or-less conﬁrm these predictions.
However these small x-values do suggest that c > 1 which we do not believe, since that
would force contradictions to our predictions for M (x, y) for larger y.

9.2. Intermediate length intervals (log x ≤ y = o((log x)
2)). In the range log x ≤
y = o((log x)2) we have predicted (1) no matter whether we presieve up to z or up to
y. One can revisit the heuristic arguments above to try to get a more accurate approx-
imation: By (11) we believe that if y = λ(log x)
2 with λ → 0 then

M (x, y) is better approximated by log x

log ( 1/λ
e log 1/λ ) .

However the data for this prediction is no more compelling then for the less precise
prediction L(x, y) in this range, presumably because x is so small.

9.3. Comparatively long intervals (y/(log x)
2 → ∞ with y ≤ x). Here we write
y = (log x)
A with A ≥ 2 and understanding that if A = 2 then y/(log x)2 → ∞. If (6)
holds then Proposition 1 suggests that

M (x, y) ∼ σ+(A) y
log x and m(x, y) ∼ σ−(A) y
log x

which is what we believe.
If we were to pre-sieve up to y then Proposition 1 suggests that one should make a
similar prediction but with σ+(A) replaced by

max
x<X≤2x #{j ≤ y : (X + j, P (y)) = 1}
∕ φ(P (y))
P (y) y.

(and σ−(A) by the analogous expression with the min). However we have no idea how
to study this ratio in this restricted range for X.

28 ANDREW GRANVILLE AND ALLYSA LUMLEY

9.4. Longish intervals (y ≍ (log x)2). In section 1.3 we saw that if y = λ(log x)
2

then we should expect that
 M (x, y) ∼ u+(c+λ) · log x

Now u+(c+λ) ∼ c+λ as λ → ∞ and so M (x, y) ∼ c+ y
log x. This implies, letting λ → ∞
and comparing this prediction to that in the last subsection, that c+ = σ+(2).
Following the same heuristic but now focusing on the minimum we see that if y =
λ(log x)
2 then we should expect that

m(x, y) ∼ u−(c−λ) · log x

for some constant c− > 0. This analogously yields that c− = σ−(2).

9.5. More precise guesses for the maximal gap between primes. We can be
more precise about our prediction for gaps between primes using the footnote in the
proof of Proposition 1. The estimate there N ≤ (L − 1
2 + o(1)) log x with L = φ(P )
P log x
which would suggest that

max
x<pn≤2x pn+1 − pn ≈ c−1
− log x( log x − 1
2 P
φ(P )
) ≈ c−1
− log x( log x − 1
2 log log x)
.

Here P = P (z) and c− depend on z.
Cadwell [2] presented a variant of Cram´er’s model. He took the viewpoint that
certain aspects of the distribution of H := π(2x) − π(x) primes in (x, 2x] can be
assumed to be like the distribution of H randomly selected integers in (x, 2x]. He very
elegantly proved that the expected largest gap has length x
H+1 ( 1
1 + 1
2 + · · · + 1
H+1). This
can be used to predict that
13

max
x<pn≤2x pn+1 − pn ≈ log(4x/e)(log x − log log x + γ).

It is not clear how to incorporate divisibility by small primes into this argument,
particularly working only with those intervals with an unexpectedly small number of
integers left unsieved.
There are some similarities in these two conjectural formulas but it is not clear which
to choose and on what basis. We did see in Figure 5 that the data suggests that one
should subtract a larger multiple of log log x in the formulas above but we have not
found a believable heuristic to do so, though ﬁnding a way to combine the two heuristics
would be a good start.

10. Short arithmetic progressions

We can proceed similarly with the distribution of π(qy; q, a), the number of primes
among the smallest y positive integers in the arithmetic progression ≡ a (mod q), as
we vary over reduced residue classes a (mod q) and where y is small compared to q.
As before we sieve out with the primes ≤ z (that do not divide q) before trying to ﬁnd

13Cadwell’s conjecture of log x(log x − log log x) for the largest prime gap ≤ x was brieﬂy mentioned
in section 1.4. However since x/π(x) is more accurately approximated by log x−1, a famous correction
of Legendre’s prediction by Gauss, he should have deduced (log x−1)(log x−log log x) from his model!
Here we are looking at gaps in (x, 2x] rather than up to x, which explains the diﬀerence in the constants.

PRIMES IN SHORT INTERVALS: HEURISTICS AND CALCULATIONS 29

primes. If Pq(z) := ∏
p≤z, p∤q p then the probability that a random such integer of size
q1+o(1) is prime is
 ∼ qPq(z)
φ(qPq(z)) 1
log q
Now the number of unsieved integers in such an interval of length y is expected to
be φ(Pq(z))
Pq(z) y,

and so the “expected” number of primes is

∼ q
φ(q) y
log q

(which is what suggested by the prime number theorem for arithmetic progressions).
This set up allows us to proceed much as in the questions about primes on short
intervals. We shall explore this in detail, with copious calculations, in a subsequent
article.

Appendix A. The largest prime gap conjecture in computing range

In section 1.4, particularly in ﬁgure 5, we saw that our predictions for max
pn≤x(pn+1 −pn)

appear to be signiﬁcantly too large. The technique we used to make our prediction
involves several asymptotic predictions for the distribution of primes and for the sieve
and so any of these may be suﬃciently far out for small integers that this might have
led to the diﬀerence from the data that we have seen. Our belief is that the main issue
is the sieving and not the probabilistic argument and so we test that in this section.
We take an example near to the upper limit of what is currently computable:
We take log x = 40: The largest prime gap up to x is 1248 immediately following
218034721194214273. The Cram´er prediction is 1600 and ours is 1797. We follow the
argument in this paper:
We want to determine the maximal gap y which should be (at a ﬁrst guess) around
(log x)2 = 1600 (at least according to Cram´er), so we will now study sieving all intervals
of length 1600 with the primes ≤ z = 1
2 log x = 20. Deﬁne P = P (20) and

R(n) := #{X (mod P ) : S(X, y, z) = n} where n =: cn φ(P )
P y.

In the notation of Proposition 1, we want N = n to be as large as possible so that
k− = 0 where L = φ(P )
P log x and x (there) equals R(n)x/P here. Proposition 1 then
suggests that we should take N ∼ L log(R(n)x/P ). Referee #3 observed that the
proof of Proposition 1 indicates that replacing L in this formula by 1
− log(1− 1
L ) is more
accurate, and indeed is about 7.5% better for this value of L. This then suggests that

y ≈ max
n 37
cn (23.91 + log R(n)).

as log(x/P ) ≈ 23.91 (where we had “40”, which is log x, instead of “37”, before the
referee’s suggestion). We can easily determine this function for each n on a computer,

30 ANDREW GRANVILLE AND ALLYSA LUMLEY

and from this we obtain a prediction of y = 1420,14 signiﬁcantly smaller than either
previous prediction, but still unaccountably larger than the truth. The data for each
n is given in the following:

n R(n) 37
cn (23.91 + log R(n))

234 24 1040.2
235 784 1169.0
236 6392 1244.0
237 32404 1300.3
238 123540 1345.4
239 342796 1378.1
240 737536 1401.0
241 1263416 1415.3
242 1714444 1420.8
243 1841372 1417.6
244 1569650 1405.9
245 1075420 1386.3
246 594076 1359.0
247 265624 1324.2
248 95356 1281.8
249 28584 1233.1
250 6652 1175.8
251 1320 1113.2
252 268 1051.9
253 32 972.3

Figure 9. Data when y = 1420

We see that there are about 1.71 million intervals mod P (20) of length 1420 which
contain exactly 242 integers that are coprime to P (20). The probabilistic argument
then suggests that some of the corresponding intervals in (x, 2x] contain no primes at
all. If instead we work with P (25) then our prediction reduces a little but not much,
and indeed we tried all the obvious possibilities but could not manipulate the variables
to construct a prediction that would reduce 1420 to anywhere near the truth, namely
1248.
 Appendix B. Is the model valid?

B.1. A ﬁrst example, x = 10
8, y = 340, z = 11. For x = 10
8 we are going to study
the distribution of primes in intervals of length y = 340 ≈ (log x)
2, which lie between
x and 2x, grouping them according to the value of S(X, y, z) where z = 11.
A quick calculation reveals that S(X, 340, 11) takes each value between 68 and 73.
Let C(N ) := #{m (mod P ) : S(m, y, z) = N }. As discussed in section 8, we have
S(X, y, z) = S(m, y, z) whenever X ≡ m (mod P (z)), so that

I(N ) = ⋃

m∈C(N )
{X ∈ (x, 2x] : X ≡ m (mod P )},

14It was y = 1536 before the referee’s intervention.

PRIMES IN SHORT INTERVALS: HEURISTICS AND CALCULATIONS 31

and therefore #I(N ) = x
P #C(N ) + O(P ). A simple calculation yields that P (11) =
2310 with
 #C(68) = 28, #C(69) = 228, #C(70) = 784,

#C(71) = 820, #C(72) = 386, #C(73) = 64.

For each N ∈ [68, 73] we deﬁne, for each integer h,

I(N, h) := {X ∈ I(N ) : π(X + y) − π(X) = h}.

Then we create the bar graph where the column rooted at h on the vertical axis has
height #I(N, h).
We wish to compare this to our assumptions, and to the binomial distribution.
The ﬁrst thing we might want to look at is how the sieving eﬀects the probability of
being prime. Thus if µ(N ) is the calculated mean number of primes in an interval
in I(N ), then we are interested in the probability of an unsieved integer being prime,
namely 1/L(N ) where L(N ) = N/µ(N ). In our model we would take L = φ(P )
P log x =
3.82767 . . . ; but to compare this to small data we need to be more precise, noting that
a better approximation to
 x
π(2x) − π(x) is given by log 4x/e,

and using this we have L = φ(P )
P log 4x/e = 3.90794 . . . Our data yields

L(68) = 3.8665 . . . , L(69) = 3.8847 . . . , L(70) = 3.8977 . . . ,

L(71) = 3.9133 . . . , L(72) = 3.9265 . . . , L(73) = 3.9418 . . . ,

which are all reasonably close to L (no more than about 1% out). The L-values here
appear to be growing, more or less linearly, which deserves an explanation. A ‘best ﬁt’
approximation yields that L(N ) ≈ L + 0.01478(N − 70.69).
Next we compare what the binomial distribution predicts to the actual counts for
primes when S(X, y, z) = N . Here N runs from 68 to 73 and we graph I(N, h)
compared to the prediction
 (
N
h
 ) 1
Lh
 (
1 − 1
L
)N −h

from the binomial distribution. We also mark the mean µ(N ) number of primes in
these intervals, as well as mN (x, y), MN (x, y), the minimum and maximum number of
primes in such intervals, and m(x, y), M (x, y), the global minimum and maximum.

32 ANDREW GRANVILLE AND ALLYSA LUMLEY

0 5 10 15 20 25 30 35
h

0

20000

40000

60000

80000

100000

120000

140000I(68,h)
I↼; h↽
 µ(68)=17.587

M (108, 340)

m(108, 340)
mN (108, 340)

MN (108, 340)

I(68, h)

0 5 10 15 20 25 30 35
h

0.0

0.2

0.4

0.6

0.8

1.0

1.2I(69,h)
Θ10 I (69; h)
 µ(69)=17.762

M (10 , 340)

m(10 , 340)
mN (10 , 340)

MN (10 , 340)

I(69, h)

0 5 10 15 20 25 30 35
h

0.0

0.5

1.0

1.5

2.0

2.5

3.0

3.5

4.0I(70,h)
Θ10 I (70; h)
 µ(70)=17.959

M (10 , 340)

m(10 , 340)
mN (10 , 340)

MN (10 , 340)

I(70, h)

0 5 10 15 20 25 30 35
h

0.0

0.5

1.0

1.5

2.0

2.5

3.0

3.5

4.0I(71,h)
Θ10 I (71; h)
 µ(71)=18.143

M (10 , 340)

m(10 , 340)
mN (10 , 340)

MN (10 , 340)

I(71, h)

0 5 10 15 20 25 30 35
h

0.00

0.25

0.50

0.75

1.00

1.25

1.50

1.75

2.00I(72,h)
Θ10 I (72; h)
 µ(72)=18.337

M (10 , 340)

m(10 , 340)
mN (10 , 340)

MN (10 , 340)

I(72, h)

0 5 10 15 20 25 30 35
h

0

50000

100000

150000

200000

250000

300000I(73,h)
I↼; h↽
 µ(73)=18.519

M (108, 340)

m(108, 340)
mN (108, 340)

MN (108, 340)

I(73, h)

Figure 10. Testing the distributions, h vs I(N, h), for each N in our range.

In each case we see that our prediction has the same basic shape as the data (a Bell
curve) but is wider than the data, with less density around the mean. We can analyze
this by simply looking at the mean and variance compared to what is expected from
our model.
 PRIMES IN SHORT INTERVALS: HEURISTICS AND CALCULATIONS 33

N : 68 69 70 71 72 73

Expected mean: 17.40 17.66 17.91 18.17 18.42 18.68

Actual mean: 17.59 17.76 17.96 18.14 18.34 18.52

Expected variance: 12.95 13.14 13.33 13.52 13.71 13.90

Actual variance: 10.82 10.93 11.06 11.17 11.25 11.34

Although both the actual and expected means increase with N we see that the
actual mean increases more slowly than the expected. More striking is that the actual
variance, that is the variance given by the data, is far smaller than in our prediction.
According to Montgomery and Soundararajan [20] we should have

2x∑

X=x(ψ(X + y) − ψ(X) − y)
2k ∼ yk · ∫ 2x

t=x
 ( log e−γt
2πy + 1)kdt

for log x ≤ y ≤ x1/2k. Therefore the variance here (for the primes) is, more-or-less

y
x(log x)2 · ∫ 2x

t=x
 ( log e
−γt
2πy + 1)
dt = y
log x · log 2e−γ x
πy
log x .

Thus a ﬁrst approximation gives mean y
log x ≈ 18.46 and variance ≈ 11.586. If we
replace log x by log 4x/e (since this gives a more accurate description of the density
of primes in [x, 2x]) then we get ≈ 18.08 and ≈ 11.11, respectively. This corresponds
very well to the data.

B.2. A second example, x = 10
8, y = 500, z = 17. Here S(X, 500, 17) takes each
value between 84 and 97. Now P (17) = 510510 and the C-values are given by

h 84 85 86 87 88 89 90

#C(h) 52 576 3764 15836 47186 91432 125688

h 91 92 93 94 95 96 97

#C(h) 115800 70096 29428 8050 1520 212 28

We see that there are very few such intervals for the outlying h-values, and indeed the
data for these h-values does not conform to the patterns that we observe.
We have that L = φ(P (z))
P (z) log(4x/e) = 3.39513 . . . and our data yields the following
L-values to four decimal places

h 84 85 86 87 88 89 90

L(h) 3.3853 3.3805 3.3845 3.3843 3.3873 3.3906 3.3938

h 91 92 93 94 95 96 97

L(h) 3.3974 3.4011 3.4043 3.4062 3.4082 3.4156 3.4450

34 ANDREW GRANVILLE AND ALLYSA LUMLEY

Again it is usually within 1-2% of the true L-value, but is slightly increasing. Our best
linear approximation is L(N ) ≈ L + .003054(N − 90.09). The corresponding graphs
are given by

0 10 20 30 40
h

0

2000

4000

6000

8000

10000

12000I(85,h)
I↼; h↽
 µ(85)=25.145

M (108, 500)

m(108, 500)
mN (108, 500)

MN (108, 500)

I(85, h)

0 10 20 30 40
h

0

10000

20000

30000

40000

50000

60000

70000I(86,h)
I↼; h↽
 µ(86)=25.410

M (108, 500)

m(108, 500)
mN (108, 500)

MN (108, 500)

I(86, h)

0 10 20 30 40
h

0

50000

100000

150000

200000

250000

300000I(87,h)
I↼; h↽
 µ(87)=25.707

M (108, 500)

m(108, 500)
mN (108, 500)

MN (108, 500)

I(87, h)

0 10 20 30 40
h

0

200000

400000

600000

800000I(88,h)
I↼; h↽
 µ(88)=25.980

M (108, 500)

m(108, 500)
mN (108, 500)

MN (108, 500)

I(88, h)

0 10 20 30 40
h

0.00

0.25

0.50

0.75

1.00

1.25

1.50

1.75I(89,h)
Θ10 I (89; h)
 µ(89)=26.250

M (10 , 500)

m(10 , 500)
mN (10 , 500)

MN (10 , 500)

I(89, h)

0 10 20 30 40
h

0.0

0.5

1.0

1.5

2.0

2.5I(90,h)
Θ10 I (90; h)
 µ(90)=26.519

M (10 , 500)

m(10 , 500)
mN (10 , 500)

MN (10 , 500)

I(90, h)

0 10 20 30 40
h

0.0

0.5

1.0

1.5

2.0I(91,h)
Θ10 I (91; h)
 µ(91)=26.786

M (10 , 500)

m(10 , 500)
mN (10 , 500)

MN (10 , 500)

I(91, h)

0 10 20 30 40
h

0.0

0.2

0.4

0.6

0.8

1.0

1.2

1.4I(92,h)
Θ10 I (92; h)
 µ(92)=27.050

M (10 , 500)

m(10 , 500)
mN (10 , 500)

MN (10 , 500)

I(92, h)

0 10 20 30 40
h

0

100000

200000

300000

400000

500000

600000I(93,h)
I↼; h↽
 µ(93)=27.319

M (108, 500)

m(108, 500)
mN (108, 500)

MN (108, 500)

I(93, h)

0 10 20 30 40
h

0

20000

40000

60000

80000

100000

120000

140000

160000I(94,h)
I↼; h↽
 µ(94)=27.597

M (108, 500)

m(108, 500)
mN (108, 500)

MN (108, 500)

I(94, h)

0 10 20 30 40
h

0

5000

10000

15000

20000

25000

30000I(95,h)
I↼; h↽
 µ(95)=27.875

M (108, 500)

m(108, 500)
mN (108, 500)

MN (108, 500)

I(95, h)

0 10 20 30 40
h

0

500

1000

1500

2000

2500

3000

3500

4000I(96,h)
I↼; h↽
 µ(96)=28.106

M (108, 500)

m(108, 500)
mN (108, 500)

MN (108, 500)

I(96, h)

Figure 11. Testing the distributions, h vs I(N, h), for 85 ≤ N ≤ 96.

h 85 86 87 88 89 90 91 92 93 94 95 96

Data Mean 25.15 25.42 25.71 25.99 26.25 26.52 26.79 27.06 27.32 27.60 27.88 28.11

Exp Mean 25.04 25.33 25.62 25.92 26.21 26.51 26.80 27.1 27.39 27.69 27.98 28.28

Data Var 15.26 15.21 15.29 15.44 15.56 15.67 15.80 15.94 16.02 16.18 16.32 16.20

Exp Var 17.71 17.91 18.12 18.32 18.51 18.71 18.91 19.10 19.30 19.50 19.70 19.88

PRIMES IN SHORT INTERVALS: HEURISTICS AND CALCULATIONS 35

Replacing log x by log 4x/e as i the ﬁrst example the overall expected mean is
26.5858 . . . and the new expected variance is 15.8003 . . . , which again is a pretty good
ﬁt with this data.
The data in this appendix makes a compelling case that one should develop a dif-
ferent model, stemming from the binomial distribution, but in which the Xn are not
independent. Instead, their dependence must imply that the number of primes in short
intervals of length y between x and 2x satisﬁes the normal distribution with the vari-
ance predicted by Montgomery and Soundararajan, and then perhaps we might see
what this new model might give for tail probabilities. We would thus revise our pre-
dictions for M (x, y), m(x, y) and the largest gaps between consecutive primes.15 We
hope to return to this key topic in a further paper.

Appendix C. Pre-sieving intervals of length y by the primes up to y

Fix x and y, let P = P (y) and assume that S(y) ∼ y
log y . Recall that I(N ) = {X ∈
(x, 2x] : S(X, y, y) = N }, where 0 ≤ N ≤ S(y), and let #I(N ) =: xθN . Now

max
N #I(N ) ≥ x/(S(y) + 1) ≥ x/y ≥ x1−o(1),

so there exist N -values for which θN = 1+o(1). It is not hard to show that S(X, y, y) =
φ(P )
P y + O(y1/2+o(1)) for almost all X mod P ; but we cannot assume that the distribu-
tion of #I(N ) is comparable in the restricted interval X ∈ (x, 2x], with the distribution
in the much larger set [0, P ).
We will use Proposition 1 with L = φ(P )
P log x ∼ e−γ log x
log y and x (there) equal to
#I(N ) to predict the values of

MN (x, y) := max{π(X, X + y] : x < X ≤ 2x and S(X, y, y) = N }

for each N with I(N ) non-empty. From these predictions we obtain our predictions for

M (x, y) = max
N MN (x, y).

In section 8.1, the independence hypothesis of Proposition 1 was satisﬁed as the
intervals were disjoint. Here the intervals in I(N ) might overlap, so we replace I(N )
by I ′(N ), the largest subset of I(N ) of disjoint intervals. Evidently #I(N ) ≥ #I ′(N ) ≥
#I(N )/y so #I ′(N ) = xθN /yO(1); the yO(1)-factor is irrelevant in applying Proposition
1 when θN > 0.
We will focus our heuristic on those integers N for which θN = 1 + o(1) (working
with other N will only aﬀect our heuristic in the range with Y ≪ log x, as we discuss
in a footnote). Therefore we let N∗ = N∗(x, y) be the largest integer N for which
θN = 1 + o(1) and c∗ := cN∗, where we deﬁne cN by N =: cN φ(P )
P y for each N .

15Though hopefully only in the secondary terms, so as not to invalidate the conjectures in this
paper!

36 ANDREW GRANVILLE AND ALLYSA LUMLEY

Predictions, by pre-sieving up to y: If log x ≪ y ≤ (eγ/c∗) log x then
16

M (x, y) ∼ c∗ · e−γ y
log y .

If (eγ/c∗) log x ≤ y = o((log x)
2) then

M (x, y) ∼ log x

log( (log x)2

y ).

Finally if y = λ(log x)
2 with λ > 0 then

M (x, y) ∼ max
N cN δ+(cN λ/θN ) · y
log x.

If λ is large and y = λ(log x)
2 then

cN δ+(cN λ/θN ) = cN +
 √ 2θN cN
λ + O( 1
λ
)
,

and so M (x, λ(log x)2) ∼ c† y
log x as λ → ∞ where c† = maxN cN where the maximum
is taken over all those cN with θN ≫ 1.
These predictions are substantially more complicated than those obtained when pre-
sieving up to ϵ log x. By Occam’s razor, we choose to follow the other path though it is
feasible that both will yield the same prediction if only we could at least partly resolve
the relevant sieve questions (that is, determine the values of c†, c∗ and maxN {cN : cN ≤
uθN } for each u > 0).

Deduction of the above predictions from Proposition 1. Evidently ∑

N #I(N ) = x, each
N ≤ S(y) and
∑

N N #I(N ) = y#{n ∈ (x, 2x] : (n, P ) = 1} + O(y2) ∼ φ(P )
P xy,

so that #{n ∈ (X, X + y] : (n, P ) = 1} averages ∼ φ(P )
P y over all X ∈ (x, 2x]. We can
restrict attention in both sums to those N with θN = 1 + o(1) with only a negligible
error term, and so by taking the average over such N we deduce that c∗ ≥ 1.
We take the largest subset of the intervals in I(N ) that begin at least y apart (so
there are #I(N )yO(1) such intervals). We can employ Proposition 1 with L ∼ e
−γ log x
log y ,

16Had we included N -values for which θN < 1 in our calculation then instead we would have
predicted that M (x, y) ∼ cN · e−ﬂ y
log y in the range log x ≪ y ≤ (θN /cN )eﬂ log x where cN is chosen
as large as possible so that cN y ≤ eﬂ θN log x. This makes sense since y is ﬁxed, and our job is to
select the optimal N -value. However, if θN < 1 then this new prediction leads to complications: At
the smallest x-value in this range we have the prediction M (x, y) ∼ θN log x
log y , whereas the next range

begins with the prediction M (x, y) ∼ log x
log y . Since there can be no discontinuity in these predictions
that means that there must be at least one other (x, y)-range with a diﬀerent N -value in-between, etc.
Because this gets so complicated we made the choice to make the simplifying assumption (Occam’s
razor) that we select from those N with θN = 1 + o(1) in our heuristic.

PRIMES IN SHORT INTERVALS: HEURISTICS AND CALCULATIONS 37

so that log L ∼ log log x. This yields that

MN (x, y) ∼
 



 N if N ≤ log #I(N )
log log x ;
log #I(N )

log ( L log #I(N )
N ) if log #I(N )
log log x ≤ N = o(L log #I(N ));

δ+(λ) N
L if N = λL log #I(N ) with λ > 0.

The ﬁrst range is cN y ≲ e
γθN log x, and therefore the maximum occurs when N = N ∗

provided y ≤ c−1
∗ e
γ log x. For those N with θN < 1 the ﬁrst range might be applicable
for larger y. However for these y the predicted value of MN ∗(x, y) in the second range
will be larger than those MN (x, y). Obtaining the results in the other two ranges is
straightforward. □

References

[1] William Banks, Kevin Ford and Terence Tao, Large prime gaps and probabilistic models,
(preprint).
[2] J.H. Cadwell, Large intervals between consecutive primes, Math. Comp. 25 (1971), 909–913.
[3] Harald Cram´er, On the order of magnitude of the diﬀerence between consecutive prime numbers,
Acta Arithmetica. 2 (1936), 23–46.
[4] William Feller, An introduction to probability theory and its applications, Vol. II. (2nd ed.) Wiley,
New York, 1971
[5] Kevin Ford, Ben Green, Sergei Konyagin and Terence Tao, Large gaps between consecutive prime
numbers, Ann. of Math. 183 (2016), 935–974.
[6] Kevin Ford, Ben Green, Sergei Konyagin, James Maynard, and Terence Tao, Long gaps between
primes, J. Amer. Math. Soc. 31 (2018), 65–105.
[7] John Friedlander and Andrew Granville, Limitations to the equi-distribution of primes. I, Ann.
of Math. 129 (1989), 363–382.
[8] J.B. Friedlander and H. Iwaniec, Opera de Cribro, AMS Colloquium Publications 57 American
Mathematical Society, 2010.
[9] Andrew Granville, Harald Cram´er and the distribution of prime numbers, Harald Cram´er Sym-
posium (Stockholm, 1993). Scand. Actuar. J. 1 (1995), 12–28.
[10] Andrew Granville, Primes in intervals of bounded length, Bull. Amer. Math. Soc. 52 (2015),
171–222.
[11] Andrew Granville, Sieving intervals and Siegel zeros, (preprint)
[12] G. H. Hardy and J. E. Littlewood, Some problems of “Partitio Numerorum”, III: On the expres-
sion of a number as a sum of primes, Acta Math. 44 (1923), 1–70.
[13] Henryk Iwaniec, On the problem of Jacobsthal, Demonstratio Math. 11 (1978), 225–231.
[14] W.B. Jurkat and H.-E. Richert, An improvement of Selberg’s sieve method. I. Acta Arith. 11
(1965), 217–240.
[15] Helmut Maier, Primes in short intervals, Michigan Math. J. 32 (1985), 221–225.
[16] Helmut Maier, and Cam L. Stewart, On intervals with few prime numbers, J. Reine Angew. Math.
608 (2007), 183–199.
[17] James Maynard, Small gaps between primes, Ann. of Math. 181 (2015), 383–413.
[18] James Maynard, Large gaps between primes, Ann. of Math. 183 (2016), 915–933.
[19] James Maynard, Sums of two squares in short intervals, arXiv:1910.13384
[20] Hugh L. Montgomery and K. Soundararajan Primes in short intervals, Comm. Math. Phys. 252
(2004), 589–617.
[21] A. Selberg, Sieve methods, ch. 36 of Collected Works, Vol I, Springer-Verlag, New York 1989.
published originally as: Proc. Sympos. Pure Math 20 (1971), 311–351.

38 ANDREW GRANVILLE AND ALLYSA LUMLEY

[22] Terence Tao, Polymath8b: Bounded intervals with many primes, af-
ter Maynard, Blog note. https://terrytao.wordpress.com/2013/11/19/
polymath8b-bounded-intervals-with-many-primes-after-maynard/
[23] Triantafyllos Xylouris, ¨Uber die Nullstellen der Dirichletschen L-Funktionen und die kleinste
Primzahl in einer arithmetischen Progression, Ph.D. thesis, Universit¨at Bonn, Mathematisches
Institut, Bonner Mathematische Schriften 404 (2011), 110pp.
[24] Yitang Zhang, Bounded gaps between primes, Ann. of Math. 179 (2014), 1121–1174.

D´epartment de Math´ematiques et Statistique, Universit´e de Montr´eal, CP 6128
succ Centre-Ville, Montr´eal, QC H3C 3J7, Canada.
Email address: andrew@dms.umontreal.ca

Centre recherche math´ematiques, Universit´e de Montr´eal, CP 6128 succ Centre-
Ville, Montr´eal, QC H3C 3J7, Canada.
Email address: lumley@crm.umontreal.ca
