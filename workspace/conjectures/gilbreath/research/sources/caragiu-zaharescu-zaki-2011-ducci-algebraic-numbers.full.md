<!-- source: https://www.fq.math.ca/Papers1/49-1/CaragiuZaharescuZaki.pdf | converted from PDF -->

ON DUCCI SEQUENCES WITH ALGEBRAIC NUMBERS

MIHAI CARAGIU, ALEXANDRU ZAHARESCU, AND MOHAMMAD ZAKI

Abstract. In this paper we study the iterated absolute values of diﬀerences between con-
secutive elements of a periodic sequence of real algebraic numbers.

1. introduction

Many interesting mathematical problems and conjectures revolve around what came to be
known as the Ducci game. Namely, if d ≥ 3 is an integer, the traditional Ducci iteration is a
map D : Zd → Zd

given by D(x0, x1, . . . , xd−1) = (|x0 − x1|, |x1 − x2|, . . . , |xd−1 − x0|). (1)
The origins of the problem may be traced back to Professor E. Ducci of Italy, who is credited
in a 1937 article [8] with the discovery of the fact that the repeated application of D in the
case d = 4 eventually leads to the null vector. Indeed, what makes this iteration even more
interesting is the fact that if (and only if) d is a power of 2, the repeated application of D
eventually leads to the null d-tuple. If d is not a power of 2, the dynamics induced by D
always leads into cycles with the interesting property that the components of each d-tuple in
a cycle are either 0 or some constant c (which is the same for all the d-tuples in the cycle), in
which case it turns out that the Ducci map is essentially (up to a constant) a binary iteration
D : Fd
2 → Fd
2 D(u0, u1, . . . , ud−1) = (u0 + u1, u1 + u2, . . . , ud−1 + u0). (2)
The map D holds the key for the Ducci iteration in the case of integers, and is ultimately
responsible for the lengths of the Ducci cycles (see [1, 4, 5, 7, 9, 10, 16]). The fact that the
iteration eventually reaches the null d-tuple if d = 2k has a particularly simple explanation.
Indeed, if one identiﬁes an n-tuple (u0, u1, . . . , ud−1) with the polynomial

u(X) =
 d−1∑

j=0 ujX j ∈ F2[X]/(X d − 1),

one easily sees (2) as the multiplication by 1 + X −1 = 1 + X d−1 ∈ F2[X]/(X d − 1). Since
(
1 + X −1)d = (1 + X −1)2k = 0 ∈ F2[X]/(X d − 1),

it turns out that after d iterations we get a d-tuple with even entries, after 2d iterations we
get a d-tuple with entries divisible by 4, etc. Thus their entries become divisible by higher and
higher powers of 2. On the other hand, regardless of the choice of the initial d-tuple, the set of
vectors generated in the Ducci process is bounded. Putting all of this together, the conclusion
of the special case d = 2k follows, since an integer that is divisible by a power of 2 greater
than its absolute value must necessarily be zero. The Ducci game can also be played over the
rationals (in which case the same type of behavior at the limit holds for D : Qd → Qd). Ducci

34 VOLUME 49, NUMBER 1

ON DUCCI SEQUENCES WITH ALGEBRAIC NUMBERS

games in a p-adic setting have been considered in which the transition rule is the multiplication
by a p-adic polynomial f (x) ∈ Zp[x]/(xd − 1). Thus in [6] it is shown that the probability that
a randomly chosen f (x) generates a p-adic Ducci game with the property that the iterates
converge to the zero element of Z p[x]/(xd − 1) in the p-adic metric no matter the initial input,
is p−t, where t is the largest factor of d that is not divisible by p.
The Ducci iteration over the integers generated many outstanding problems [7] involving
the lengths of the cycles, the asymptotic growth of the number of cycles with distinct lengths,
and problems related to generalizations of the Ducci map to other mappings incorporating
various “weights”. Another interesting problem is in estimating the length of the Ducci game,
that is the number of iterations needed in order to reach the limit cycle (see [3, 14, 17] for
special case d = 4).
Fix a positive integer d, and consider the evolution function D : Rd → Rd deﬁned by
D(a1, . . . , ad) = (a′
1, . . . , a′
d), where

a′
k = |ak − ak+1| for 1 ≤ k ≤ d − 1, and a′
d = |ad − a1|.

Alternatively, instead of the ﬁnite sequence a1, . . . , ad, one can work with an inﬁnite periodic
sequence (a1, a2, . . .), where the components are deﬁned by

ak = ak+d, for k ≥ 1. (3)

In that case the evolution function is deﬁned by D(a1, a2, . . .) = (a′
1, a′
2, . . .), with

a
′
k = |ak − ak+1|, for k ≥ 1. (4)

We note in passing that this is the same map which appears in the well-known conjecture
of Gilbreath (see [11, 13, 15]). While Gilbreath’s conjecture is wide open, the periodicity of
the sequence in the Ducci game allows one to understand the behavior of iterates of D in the
long run.
Let X = (x1, . . . , xd) ∈ Rd, and consider the iterates Dn(x1, . . . , xd), n ∈ N. In [2], Brown
and Merzel proved that the sequence (Dn(X))n∈N eventually stabilizes around one particular
cycle, and then converges to this cycle as n tends to inﬁnity. Given a positive integer d,
X ∈ Rd, we denote by EX the set of limit points of the inﬁnite sequence (Dn(X))n∈N. It is
easy to see that for any X ∈ Rd, EX is a compact subset of Rd. It is proved in [2] that for any
X ∈ Rd, EX is ﬁnite, and the restriction D|EX of D to EX is a bijection of EX onto itself.
It is also proved in [2] that the restriction D|EX consists of exactly one cycle. Moreover, the
iterates Dn(X) converge to this cycle, in the sense that we have a partition of N as a ﬁnite
union of arithmetic progressions having the same modulus, in such a way that the elements of
EX are in one-to-one correspondence with these arithmetic progressions, and Dn(X) converges
as n → ∞ along each such arithmetic progression to the corresponding element of EX . Thus,
if L is the cardinality of EX and V1, . . . , VL are the elements of EX , then after a rearrangement
of V1, . . . , VL, one has
 lim
m→∞ Dj+mL(X) = Vj, for each 1 ≤ j ≤ L. (5)

In the present paper, we consider the behavior of the iterates Dn(X) in the case when all
the components of X are algebraic numbers. We know from [2] that these iterates approach
a cycle as n → ∞, and we are interested to see how fast they converge to this cycle. Let us
remark that there are cases when after ﬁnitely many iterates one already obtains a cycle. For

FEBRUARY 2011 35

THE FIBONACCI QUARTERLY

example, if d = 3 and X = (1, √2, 3
√2 − 2), then

D(X) = (
√2 − 1, 2
√2 − 2, 3
√2 − 3),

D2(X) = (
√2 − 1, √2 − 1, 2
√2 − 2),

D3(X) = (0, √2 − 1, √2 − 1),

D4(X) = (
√2 − 1, 0, √2 − 1),

D5(X) = (
√2 − 1, √2 − 1, 0),

and
 D6(X) = (0, √2 − 1, √2 − 1) = D3(X),

so we obtain a cycle of length 3.
For another example, let us choose now, still in the case d = 3, X = (1, θ, θ2), where θ is
the positive root of the equation x2 + x − 1 = 0, that is, θ = −1+√5
2 . Then

D(X) = (1 − θ, θ − θ2, 1 − θ2) = θ(θ, θ2, 1),

D2(X) = θ2(θ2, 1, θ),

and
 D3(X) = θ3(1, θ, θ2).

More generally,
 Dn(X) =
 



θn(1, θ, θ2), if n ≡ 0 (mod 3),
θn(θ, θ2, 1), if n ≡ 1 (mod 3),
θn(θ2, 1, θ), if n ≡ 2 (mod 3).

This is an example where the limiting cycle consists of the point (0, 0, 0) only, and is not
obtained after ﬁnitely many iterates. Also note that here the convergence is exponentially
fast.
We will show that for any X with algebraic components, the convergence of the iterates
Dn(X) to the corresponding limiting cycle cannot be faster than exponential, unless we are in
a case when the cycle is already obtained after ﬁnitely many iterates.

Theorem 1.1. Let X ∈ Rd. Let V1, . . . , VL ∈ EX satisfying (5). Assume that all the compo-
nents of X are algebraic numbers. Then one of the following holds true.

(i) There exists an m0 ∈ N such that

Dj+mL(X) = Vj,

for all m ≥ m0.
(ii) There exist positive constants C1, C2 depending only on X such that

∥Dj+mL(X) − Vj∥ ≥ C1e
−C2m

for all m ∈ N.

36 VOLUME 49, NUMBER 1

ON DUCCI SEQUENCES WITH ALGEBRAIC NUMBERS

2. Proof of Theorem 1.1

We start with the following lemma.

Lemma 2.1. Given a positive integer d ≥ 1, let X, Y ∈ Rd. Then,

∥D(X) − D(Y )∥ ≤ 2 ∥X − Y ∥ ,

where ∥.∥ denotes the Euclidean norm on Rd.

Proof. Let X = (x1, . . . , xd) and Y = (y1, . . . , yd). Then,

∥D(X) − D(Y )∥
2 = (|x1 − x2| − |y1 − y2|)2 + · · · + (|xd − x1| − |yd − y1|)
2 .

Now, for each 1 ≤ j ≤ d,

||xj − xj+1| − |yj − yj+1|| ≤ |xj − yj| + |xj+1 − yj+1|.

Therefore,

(|x1 − x2| − |y1 − y2|)2 + (|x2 − x3| − |y2 − y3|)
2 + · · · + (|xd − x1| − |yd − y1|)2

≤ 2 (|x1 − y1|
2 + |x2 − y2|
2 + |x2 − y2|
2 + |x3 − y3|
2 + · · · + |xd − yd|
2 + |x1 − y1|
2)

= 4 ∥x − y∥
2 .

This proves Lemma 2.1. □

The above lemma says that the map D is 2-Lipschitzian. Let us remark that there is no
λ < 1 for which D is λ-Lipschitzian, since otherwise D will be a contraction, and then for each
X ∈ Rd, the sequence of iterates (Dn(X))n∈N will converge to the unique ﬁxed point of D.
But this is simply not the case as we have seen in the ﬁrst example from the introduction.
Let us note that for any X ∈ Rd all the components of Dn(X) are nonnegative if n ≥ 1. Let
M be the maximum of the components of D(X). By the deﬁnition of D, it is easy to see that
for all n ≥ 1, all the components of Dn(X) are real numbers belonging to [0, M ], so Dn(X) ∈
[0, M ]d for all n ≥ 1. This shows that the set EX of limit points of the sequence (Dn(X))n∈N
is nonempty. For any Y = (y1, . . . , yd) ∈ [0, ∞)d we denote by M (Y ) the maximum of the
components of Y . Observe that the maximum component function M is a continuous function.
Also (M (Dn(X)))n≥1 is a non-increasing sequence of nonnegative numbers, so it converges to
M0. It follows from [2] that for any element a ∈ EX, each component of a equals either 0 or
M0.

Proof of Theorem 1.1: There are two main ideas in the proof of the theorem. The ﬁrst one
is that, although the absolute value function |.| is built into the deﬁnition of the map D, we
may still write the iterates Dn(X) as linear combinations of the components of X with integer
coeﬃcents, and provide bounds for these coeﬃcents. The second idea is to multiply all the
components of X by a ﬁxed positive integer b to make them algebraic integers, and use the fact
that the absolute value of the norm of any nonzero algebraic integer is at least one, in order
to show that the iterates Dn(X) stay away from the limiting cycle EX, unless they belong to
EX. There is, however, a nontrivial diﬃculty in this approach, coming from the fact that we
don’t know whether or not the components of the elements of EX are algebraic. As we will
see below, this diﬃculty of not knowing whether M0 is algebraic or not can be overcome by
employing an argument which avoids using M0 in the proof.
To start the proof, let K be a number ﬁeld which contains all the components of X =
(a1, . . . , ad). Let [K : Q] denote as usual the degree of K over Q. Denote by OK the ring of

FEBRUARY 2011 37

THE FIBONACCI QUARTERLY

integers of K. From [2], we know that if L is the cardinality of EX and V1, . . . , VL are the
elements of EX, then after a rearrangement of V1, . . . , VL, one has

lim
m→∞ Dj+mL(X) = Vj, for each 1 ≤ j ≤ L. (6)

Next, observe that
∥
∥
∥Dj+(m+1)L(X) − Dj+mL(X)
∥
∥
∥ ≤ ∥
∥
∥Dj+(m+1)L(X) − Vj∥
∥
∥ + ∥
∥Dj+mL(X) − Vj∥
∥ .

By applying Lemma 2.1 repeatedly, we ﬁnd that
∥
∥
∥Dj+(m+1)L(X) − Vj∥
∥
∥ ≤ 2 ∥
∥
∥Dj+(m+1)L−1(X) − Vj−1∥
∥
∥

. . .

≤ 2
L ∥
∥Dj+mL(X) − Vj−L∥
∥

= 2
L ∥
∥Dj+mL(X) − Vj∥
∥ .

Thus, ∥
∥
∥Dj+(m+1)L(X) − Dj+mL(X)
∥
∥
∥ ≤ (2
L + 1) ∥
∥Dj+mL(X) − Vj∥
∥ .

Let Y = Dj+(m+1)L(X) − Dj+mL(X). So, ∥Y ∥ ≤ (2L + 1) ∥
∥Dj+mL(X) − Vj∥
∥.
Next, ﬁx a positive integer b such that ba1, . . . , bad ∈ OK . Denote Dn(X) = (a1,n, . . . , ad,n)
for all n. In particular, a1,0 = a1, . . . , ad,0 = ad. By induction on n, one ﬁnds that ba1,n, . . . , bad,n ∈
OK for all n. In order to see this, it is enough to note that, for any n and any 1 ≤ r ≤ d,
ar,n+1 = ar,n − ar+1,n or ar,n+1 = ar+1,n − ar,n. Thus, bar,n+1 ∈ OK.
Also, by induction on n, each ar,n, r = 1, . . . , d can be written as

ar,n = c1,r,na1 + c2,r,na2 + · · · + cd,r,nad

with c1,r,n, . . . , cd,r,n ∈ Z, and max{|c1,r,n|, . . . , |cd,r,n|} ≤ 2n.
We write Y = (h1, . . . , hd). Then for each 1 ≤ r ≤ d, hr = ar,j+(m+1)L − ar,j+mL. On one
hand, we know that bhr = bar,j+(m+1)L − bar,j+mL ∈ OK . On the other hand,
hr = (c1,r,j+(m+1)L − c1,r,j+mL)a1 + · · · + (cd,r,j+(m+1)L − cd,r,j+mL)ad.
Therefore,

|hr| ≤ (|c1,r,j+(m+1)L| + |c1,r,j+mL|)|a1| + · · · + (|cd,r,j+(m+1)L| + |cd,r,j+mL|)|ad|

≤ (2
j+(m+1)L + 2
j+mL)(|a1| + · · · + |ad|).

Next, for any embedding σ of K into C, we have that σ(hr) = (c1,r,j+(m+1)L −c1,r,j+mL)σ(a1)+
· · · + (cd,r,j+(m+1)L − cd,r,j+mL)σ(ad). Thus, as above we ﬁnd that

|σ(hr)| ≤ (2
j+(m+1)L + 2
j+mL)(|σ(a1)| + · · · + |σ(ad)|).

It follows that
 |σ(bhr)| ≤ b(2
j+(m+1)L + 2
j+mL)(|σ(a1)| + · · · + |σ(ad)|).

Let R = (2j+(m+1)L + 2j+mL) max
σ |σ(a1)| + · · · + |σ(ad)|, where the maximum is taken over
all the embeddings σ of K into C. Then

|σ(bhr)| ≤ bR,

for all embeddings σ.

38 VOLUME 49, NUMBER 1

ON DUCCI SEQUENCES WITH ALGEBRAIC NUMBERS

Now, for each r ∈ {1, . . . , d}, we distinguish two cases. Either hr = 0 in which case
NK/Q(bhr) = 0, or hr ̸= 0, and then |NK/Q(bhr)| ≥ 1 since bhr ∈ OK is nonzero. In the second
case we further deduce that |bhr| ≥ 1
(bR)[K:Q]−1 ,

and so |hr| ≥ 1
b[K:Q]R[K:Q]−1 .

Next, if hr = 0 for all 1 ≤ r ≤ d, then Y = 0, and hence

Dj+mL(X) = Dj+(m+1)L(X).

In this case it follows that

Dj+mL(X) = Dj+(m+1)L(X) = Dj+(m+2)L(X) = . . . .

Therefore, Dj+mL(X) belongs to EX, and then it must coincide with Vj. Note that if this
holds for one particular pair (j, m), then Dn(X) belongs to EX for any n ≥ j + mL, and then
one is on case (i) of the theorem. The other alternative is when there is no pair (j, m) for
which Dj+mL(X) ∈ EX . In this second case, we have that for any choice of j and m, at least
one component hr of the corresponding Y is nonzero. Then the Euclidean norm of Y satisﬁes

∥Y ∥ =
 

 ∑

1≤j≤d |hj|
2



 1
2 ≥ |hr| ≥ 1
b[K:Q]R[K:Q]−1 .

Since ∥Y ∥ ≤ (2L + 1) ∥
∥Dj+mL(X) − Vj∥
∥, we have that
∥
∥Dj+mL(X) − Vj∥
∥ ≥ 1
(2L + 1)b[K:Q]−1R[K:Q]−1 .

In this case we conclude the
 ∥Dj+mL(X) − Vj∥ ≥ C1e
−C2m

for all pairs (j, m), for some positive constants C1 and C2 depending on X only. This completes
the proof of Theorem 1.1. □

3. Comments

The value of the exponent C2 which is achieved by our proof above is

C2 = (log 2) ([K : Q] − 1) L.

As was pointed out by the referee, when M0 is algebraic, Roth’s Theorem (see p. 304 in [12])
gives C2 = (log 2) (2 + ϵ) L for any ϵ. Here one uses the fact that the height of hr is bounded
by a constant times 2mL. It may be interesting to ask if one can obtain the optimal value for
the exponent C2 in the main result.
One may also ask whether the fact that the convergence of the Ducci iterates to the corre-
sponding limiting cycle cannot be faster than exponential unless the limit cycle is eﬀectively
reached holds in general for all X with arbitrary real components.

4. Acknowledgement

The authors are grateful to the referee for many useful comments and suggestions.

FEBRUARY 2011 39

THE FIBONACCI QUARTERLY
 References

[1] F. Breuer, E. Lotter, and B. van der Merwe, Ducci-sequences and cyclotomic polynomials, Finite Fields
Appl., 13.2 (2007), 293–304.
[2] R. Brown and J. L. Merzel, Limiting behavior in Ducci sequences, Period. Math. Hungar., 47.1-2 (2003),
45–50.
[3] R. Brown and J. L. Merzel, The length of Ducci’s four-number game, Rocky Mountain J. Math., 37.1
(2007), 45–65.
[4] N. J. Calkin, J. G. Stevens, and D. M. Thomas, A characterization for the length of cycles of the N-number
game, The Fibonacci Quarterly, 43.1 (2005), 53–59.
[5] J. P. Campbell, Reviews, Mathematics Magazine, 69.4 (1996), 311–313.
[6] M. Caragiu and N. Baxter, A note on p-adic Ducci games, JP J. Algebra Number Theory Appl., 8.1
(2007), 115–120.
[7] M. Chamberland and D. M. Thomas, The N-number Ducci game, J. Diﬀerence Equations and Applica-
tions, 10.3 (2004), 339–342.
[8] C. Ciamberlini and A. Marengoni, Su una interessante curiosita numerica, Periodiche di Matematiche,
Ser. 4, 17 (1937), 25–30.
[9] C. I. Cobeli, M. Crˆa¸smaru, and A. Zaharescu, A cellular automaton on a torus, Portugal. Math., 57.3
(2000), 311–323.
[10] A. Ehrlich, Periods in Ducci’s N-number game of diﬀerences, The Fibonacci Quarterly, 28.4 (1990),
302–305.
[11] R. K. Guy, Unsolved Problems in Number Theory, Third edition, Problem Books in Mathematics,
Springer-Verlag, New York, (2004), 42–43.
[12] M. Hindry and J. H. Silvermann, Diophantine Geometry. An Introduction, Graduate Texts in Mathemat-
ics, Vol. 201, Springer-Verlag, New York, 2000.
[13] R. B. Killgrove and K. E. Ralston, On a conjecture concerning the primes, Math. Tables Aids Comput.,
13 (1959), 121–122.
[14] A. Ludington-Young, Length of the N-number game, The Fibonacci Quarterly, 28.3 (1990), 259–265.
[15] A. M. Odlyzko, Iterated absolute values of diﬀerences of consecutive primes, Math. Comp., 61.203 (1993),
373–380.
[16] B. Thwaites, Two conjectures or how to win £1100, Mathematical Gazette, 80 (1996), 35–36.
[17] W. A. Webb, The length of the four-number game, The Fibonacci Quarterly, 20.1 (1982), 33–35.

MSC2010: 11B85

Department of Mathematics, Ohio Northern University, 525 S Main Street, Ada, Ohio 45810
E-mail address: m-caragiu1@onu.edu

Institute of Mathematics of the Romanian Academy, P.O.Box 1-764, Bucharest 014700, Ro-
mania, and Department of Mathematics, University of Illinois at Urbana-Champaign, 1409 W.
Green Street, Urbana, IL 61801
E-mail address: zaharesc@math.uiuc.edu

Department of Mathematics, Ohio Northern University, 525 S Main Street, Ada, Ohio 45810
E-mail address: m-zaki@onu.edu

40 VOLUME 49, NUMBER 1
