<!-- source: https://dms.umontreal.ca/~andrew/PDF/VisibleLatticePts.pdf | converted from PDF -->

VISIBILITY IN THE PLANE

SUKUMAR DAS ADHIKARI AND ANDREW GRANVILLE

Abstract. We ﬁnd the size of the smallest subset of the set of integer lattice points, such that
every element of a given rectangular grid is visible from our subset, which in particular answers
a question of Paul Erd˝os et al.
 1. Introduction

If D ≥ 2 we say that a ∈ Z
D is visible from b ∈ Z
D if there is no element of Z
D on the
straight line segment in-between a and b. One immediately deduces that (a, b) is visible
from (c, d) if and only if gcd(c − a, d − b) = 1, and, more generally, that a is visible from
b if and only if the gcd of the co-ordinates of a-b equals 1. We say that A ⊂ Z
D is visible
from B ⊂ Z
D if, for each point a ∈ A there is some b ∈ B such that a is visible from b.
In this paper we are interested in the size of the smallest B ⊂ ZD such that A ⊂ Z
D is
visible from B. Research to date has focussed on the cases where A is the set of integer
lattice points inside a cube with all sides equal and parallel to the axes (in two dimensions
this is one of the list of problems compiled by (L. & W.) Moser, see also [6] (Section 10.4)
and [9] (Problem F4)), or where A is the set of integer lattice points inside a rectangular
cube with all sides parallel to the axes (see [11]). Herein we give an asymptotic formula
for the size of that set B:

Theorem 1. For every integer D ≥ 2, for any A ⊂ Z
D which is the set of lattice points
inside a rectangular box ⊂ R
D with all sides parallel to the axes and of shortest side length
N ≥ 2, the smallest B ⊂ Z
D such that A is visible from B has size

(1) = {1 + oN →∞(1)} ζ(D) log N
log log N ,

where ζ(D) = ∑
n≥1 1/n
D is the Riemann zeta-function. Moreover A is visible from some
B(A) ⊂ {1, 2, . . . , N }D ⊂ A of this size.

In fact we obtain upper and lower bounds of the correct order of magnitude for all
N ≥ 2: This restriction is necessary, since if A = {(m, 1) : 1 ≤ m ≤ M } is visible from
some B ⊂ A then |B| ≥ (M −1)/2. The restriction is unnecessary if we allow the elements

Thanks are due to the astute referee for several useful remarks and observations, to Iosif Polterovich
for some helpful remarks on the geometric problem in section 6, and to Anand Ramakrishnan for ﬁnding
a typographic error. 1

2 SUKUMAR DAS ADHIKARI AND ANDREW GRANVILLE

of B to be close to A, though not necessarily a subset; in our example A is visible from
the singleton set {(1, 0)}.
From Theorem 1 we immediately deduce

Corollary 2. The smallest subset of Z
D from which {1, 2, . . . , N }D is visible, has size (1)
for each integer D ≥ 2.

Theorem 1 follows from two stronger results. Let

RD(N ) := {1, 2, . . . , N } × ZD−1.

The ﬁrst gives the lower bound in Theorem 1 since {1, 2, . . . , N }
D ⊂ A:

Proposition 3. Fix integer D ≥ 2. If {1, 2, . . . , N }
D is visible from S ⊂ Z
D then S has
size ≥ {1 − oN →∞(1)} ζ(D) log N
log log N .

A more diﬃcult result gives the upper bound in Theorem 1, since A ⊂ RD(N ):

Proposition 4. Fix integer D ≥ 2. There exists a subset S of {1, 2, . . . , N }
D of size

≤ {1 + oN →∞(1)} ζ(D) log N
log log N ,

such that RD(N ) is visible from S.

(Henceforth, for notational convenience, we will replace “= {1 − oN →∞(1)}” by “∼” ,
“≥ {1 − oN →∞(1)}” by “≳” , and “≤ {1 − oN →∞(1)}” by “≲”.)
For an arbitrary compact, convex set S ⊂ R
D, one can ask for the size of the smallest
B ⊂ Z
D such that S ∩ Z
D is visible from B. If one can ﬁnd rectangular boxes A−, A+,
with sides parallel to the axes such that A− ⊂ S ⊂ A+ then the smallest such B has size
in the range

(2) LD(N−) ≲ |B| ≲ LD(N+), where LD(x) = ζ(D) log x
log log x
where N± is the shortest side length of A±, by Theorem 1, provided N− ≥ 2. We also
have B ⊂ S. This yields an asymptotic provided N− ≥ N 1−o(1)
+ which will be the case
unless S is oriented in a peculiar fashion. In particular if H is any ﬁxed convex shape
then the smallest set of lattice points from which all of N H is visible has size

∼ LD(N ).

If M is a D-by-D matrix with integer entries of determinant ±1 then a ∈ Z
D is visible
from b ∈ Z
D if and only if M a ∈ Z
D is visible from M b ∈ ZD (as is easily proven), so the
orientation of S can be adjusted by a suitable invertible linear transformation without
aﬀecting visibility. For this reason one might guess that, in general, the smallest B from
which the lattice points of S are visible, has size (1) where N ≥ 1 is the smallest 1-
dimensional thickness of S. However this is far from true, even in two dimensions, as we
show in the following results, which are proved in Section 6.

VISIBILITY 3

For a given compact, convex set S ⊂ R
2, let P and Q be two points that are furthest
apart in S, and let α(S) be the slope of the line between them.
Let N+(S) be the distance between P and Q; and then let N−(S) be the smallest
number such that every point in S lies within a distance N−(S) of the line joining P and
Q (that is, N−(S) is the 1-dimensional thickness of S).
1 Let L(x) = L2(x).

Theorem 5. Fix α ∈ R.
If α ∈ Q then for all compact, convex sets S ⊂ R2 with α(S) = α, the smallest set of
lattice points from which A = S ∩ Z
2 is visible has size ∼ L(N−).
If α ̸∈ Q then there exist arbitrarily large compact, convex sets S ⊂ R2 with α(S) = α
and N− = 1, such that the smallest set of lattice points from which A = S ∩ Z2 is visible
has size ≳ 1
4L(N+).

(In the asymptotic results here, and in Theorems 6, 7 and 8, we have oN+→∞(1).)
For any α that is not too well approximable by rationals we can get close upper and
lower bounds on the size of B: Let p1
q1 , p2
q2 , p3
q3 , . . .

be the convergents in the continued fraction for α.

Theorem 6. Suppose that α ∈ R \ Q such that the convergents for α satisfy log qj+1 ∼
log qj as j → ∞. (This includes, for example, all irrational, algebraic α, by Roth’s
theorem). If S ⊂ R
2 is a compact, convex set with α(S) = α, and B is the smallest set of
lattice points from which A = S ∩ Z
2 is visible, then
1
2L(N+) + 1
2L(N−) ≳ |B| ≳ 1
3 L(N+) + 2
3 L(N−).

Note that the upper and lower bounds here diﬀer by a factor of at most 3/2.
Rather more generally we can prove that |B| is roughly of size L(N+) unless α is very-
well approximable by rationals.

Theorem 7. Suppose that α ∈ R \ Q. For any given compact, convex set S ⊂ R
2 with
α(S) = α, let B(S) be the smallest set of lattice points from which A = S ∩ Z
2 is visible.
We have |B(S)| ≫ L(N+) for all such S if and only if log qj+1 ≪ log qj.

Theorems 5, 6 and 7 are all extreme cases of a more general understanding of the
size of B(S), which we now give. First though we must “normalize” our convex set: By
translation we may assume that P is “close” to the origin and by reﬂections that the line
joining P and Q has slope in [0, 1] (it is easy to see that by reﬂections the line is in the
positive quadrant; moreover if its slope is > 1 then we can reﬂect S in x = y so that the
slope is in [0, 1]). Next by the linear transformation x → x, y → y + x we see that we
may assume that the slope α of the line joining P and Q satisﬁes 1 ≤ α ≤ 2 (and hence

1It may be that there is more than one choice of P and Q and hence neither α(S) nor N−(S) are
uniquely deﬁned. Nonetheless the subsequent results work no matter which choice we make.

4 SUKUMAR DAS ADHIKARI AND ANDREW GRANVILLE

p1
q1 = 1). Such a compact set S, and the accompanying lattice points A = S ∩ Z
2, are
called “normalized”.

Theorem 8. Let A be a normalized set of lattice points (inside a closed, compact subset
of R
2). We can determine |B(A)| up to a factor 2, as follows:
If i ≥ 1 and q2
i ≤ N+/N− < qiqi+1

(3) L(N−qi) ≳ |B(A)| ≳ 1
2 L(N−qi).

If i ≥ 2 and qi−1qi ≤ N+/N− < q2
i then

(4) L(N+/qi) ≳ |B(A)| ≳ 1
2 L(N+/qi).

It would be worthwhile to generalize this result to higher dimensions, though one faces
the diﬃculty of having to work with simultaneous approximations. It would be interesting
to get an asymptotic for |B| here, something that we have been unable to do.
It had been shown that if {1, 2, . . . , N }D is visible from B then |B| > L2(N )/2ζ(2)
when D = 2 by Abbott [1] in 1974, |B| ≫ LD(N ) when D ≥ 3 by Adhikari and Chen
[4] (see also [6]) in 1999, and the correct bound |B| ≳ LD(N ) for all D ≥ 2 by Chen and
Cheng [7] in 2003, by an argument similar to ours.
Abbott [1] also proved that {1, 2, . . . , N }
D is visible from a set of size < 4 log N if N
is suﬃciently large, when D = 2, using a greedy construction. Adhikari and Chen [4]
obtained ≪ LD(N ) when D ≥ 3, which was improved to ≲ LD−1(N ) by Chen and Cheng
[7]. In Corollary 2 we obtain ≲ LD(N ) for all D ≥ 2.
Erd˝os, Gruber and Hammer, in their monograph [8], remark: “Abbott’s proof is an exis-
tence proof and gives no indication how to construct small subsets from which any point of
the set is visible. It would be of interest to construct such subsets of cardinality O(log N )”.
In 1996 Adhikari and Balasubramanian [3] did more than this by explicitly constructing
a set of size ≪ log N log log log N/ log log N from which {1, 2, . . . , N }
2 is visible2 (see also
[2]). The sets that we produce in Corollary 2 are not explicitly constructed; rather we
can use “almost all” sets inside a certain (constructible) class of sets of points. However,
by slightly modifying Adhikari and Chen’s method we show explicitly, in Section 4, how
to ﬁnd a set of size

(5) ∼ 1
(1 − ζ ∗(D − 1)) log N
log log N where ζ ∗(s) = ∑

p
 1
ps

from which {1, 2, . . . , N }D is visible, for each D ≥ 3.
Finally we can ask a rather more general question: For any set S ⊂ Z
D let v(S) be the
size of the smallest set of lattice points from which S is visible. What is

νD(N ) := max
S⊂ZD, |S|=N v(S) ?

We prove the following result:

2Their implicit constant can be made explicit using [5].

VISIBILITY 5

Theorem 9. Fix D ≥ 2. If N is suﬃciently large then

ζ(D)
D log N
log log N ≲ νD(N ) ≲ log N
log(1 + 1/(ζ(D) − 1)).

It would be good to close the gap between the upper and lower bounds here.

2. Lower bounds

Proof of Proposition 3 for D = 2. This is proved by using the Chinese Remainder
Theorem. Suppose that {1, 2, . . . , N }2 is visible from S0 ⊂ Z
2.

Let p1 = 2, p2 = 3, . . . be the sequence of primes. For each k, 1 ≤ k ≤ K we select i, j
(mod pk) so as to maximize the size of the set

{(u, v) ∈ Sk−1 : u ≡ i (mod pk) and v ≡ j (mod pk)}.

Call these values ik, jk and let Tk be this set. By deﬁnition |Tk| ≥ |Sk−1|/p
2
k. Let Sk =
Sk−1 \ Tk so that |Sk| ≤ (1 − 1/p
2
k)|Sk−1| and hence we have, by induction, that

|Sk| ≤
 k∏

j=1(1 − 1/p2
j ) · |S0| = ( 1
ζ(2) + O ( 1
pk log pk
 )) |S0|.

We select K so that p2
K ∼ |S0|/ζ(2), which implies that K = o((
√
|S0|) and |SK| ≤
|S0|/ζ(2) + o(
√|S0|).

Next write SK = {(iK+ℓ, jK+ℓ) : 1 ≤ ℓ ≤ |SK|}, and let r = K + |SK| which, by the
above, is ≤ |S0|/ζ(2) + o(
√
|S0|). Now let m = ∏
p≤pr p, and x and y be the least positive
residues (mod m) satisfying

x ≡ ik (mod pk) and y ≡ jk (mod pk) for 1 ≤ k ≤ r,

which is possible by the Chinese Remainder Theorem.

We see that (x, y) is invisible from each s ∈ S0 for if (u, v) ∈ S0 then there exists k, 1 ≤
k ≤ r such that u ≡ ik ≡ x (mod pk) and v ≡ jk ≡ y (mod pk), so that pk|gcd(u−x, y−v).
Hence (by the deﬁnition of S0), N < max{x, y} ≤ m = r(1+o(1))r by the prime number
theorem, and so r ≥ (1 + o(1)) log N/ log log N , from which the result follows.

Proof of Proposition 3 for D ≥ 3. We proceed analogously to the proof of the lower
bound for D = 2: For the primes pk with pD
k ≤ (1/ζ(D))|S0| we select the most popular
residue class in Sk−1 for (ik, jk, . . . , ℓk) (mod pk). For the larger primes we select one
point in Sk per prime. The result follows by an analogous calculation.

6 SUKUMAR DAS ADHIKARI AND ANDREW GRANVILLE

3. More greediness: The proof of Theorem 9

The lower bound follows by assuming S ⊃ {1, 2, . . . , M }D with M = [N 1/D], and
applying Proposition 3.
To get the upper bound, suppose that we are given a set S of N points in ZD. We now
construct a point from which > N/ζ(D) of these N points are visible:
Fix y > N 1/(D−1). Select the residue class (a1,1, a1,2, . . . , a1,D) (mod 2) containing the
fewest elements of S; so that it contains ≤ |S|/2
D elements. Let S1 equal S minus these
elements. The points in S1 are visible from any point in our residue class, at least if we
only consider the prime 2. Now we select the residue class (a2,1, a2,2, . . . , a2,D) (mod 3)
containing the fewest elements of S1, and deﬁne S2 analogously, and keep on going with
this construction for all primes p ≤ y. Hence there is some residue class mod m = ∏
p≤y p
such that every element of Sk, where k = π(y), is visible from any point in our residue class,
at least if we only consider the primes ≤ y. Now, for each prime p > y, the proportion of
elements of our residue class which do not see some element of Sk because of the prime
p is ≤ |Sk|/pD. Hence the proportion of elements of our residue class which do not see
some element of Sk because of some prime p > y is ≤ ∑
p>y |Sk|/p
D ≤ N ∑

n>y 1/n
D ≤
N/yD−1 < 1; in other words there are points in our residue class from which Sk is visible.
Select any such point and note that |Sk| ≥ N ∏
p≤y(1 − 1/p
D) > N/ζ(D).
The idea then is to start with a set S of N points, select a point P1 from which the
most elements of S are visible, and then repeat the process on the set S1 = S \ P1. After
selecting k points at most N (1 − 1/ζ(D))
k points of S are not visible from at least one of
P1, P2, . . . , Pk. The result follows.

4. First upper bounds: The construction yielding (5)

(We more-or-less follow the proof of [4].) Let

S := {(2, 2, . . . , , 2)} ∪ {(a1, a2, . . . , ak, 1) : 1 ≤ aj ≤ M } ,

with k = D−1. Notice that every point with Dth co-ordinate 1 is visible from (2, 2, . . . , , 2).
Moreover, the number of points in S \ {(2, 2, . . . , , 2)} from which (x1, x2, . . . , xD) is invis-
ible, when xD > 1, is

≤ ∑

1≤a1,a2,...,ak≤M
 ∑

p prime, p|(xD −1)
p|(xj −aj ) for 1≤j≤k
 1 = ∑

p prime
p|(xD−1)
 k∏

j=1
 M∑

aj =1
p|(xj −aj )
 1 ≤ ∑

p≤y(N )
 ( M
p + 1)k ,

where y = y(N ) = {1 + o(1)} log N denotes the largest prime for which ∏
p≤y p < N , since
M/p + 1 is a decreasing function in p. If we expand this last term using the binomial
theorem then, for each j ≥ 2, we get an upper bound

≤
 k−2∑

i=0
 ( k
k − i
)
ζ ∗(k − i)M k−i + kM (log log y + O(1)) + π(y).

VISIBILITY 7

Selecting M so that M k = (1 + ϵ)π(y)/(1 − ζ ∗(k)), the above is ≤ ζ ∗(k)M k + π(y) +
Ok(M k−1) < M k, and so there must be an element of S from which (x1, x2, . . . , xD) is
visible. The result follows letting ϵ → 0. Note that S is explicitly given as claimed.

5. More difficult upper bounds: Proposition 4

We believe that {1, 2, . . . , N }2 should be visible from a rectangular set of the shape
{
(i, j) : 1 ≤ i ≤ k, 1 ≤ j ≤ {ζ(2) + o(1)} log N
k log log N
 } .

To prove this one needs to show that for every n, r ≤ N there exists i and j in these ranges
for which gcd(n − i, r − j) = 1. Handling the possible “small” common prime factors is
a straightforward technical issue, but we have been unable to handle the possibility of
a grand co-incidence of large prime factors. A straightforward heuristic suggests that
such a co-incidence is extremely unlikely so, although we cannot rule it out, we can do
so “on average”. In other words if we keep the same choice of j’s and instead select the
“rows” i at random (in a suitable sense) then a grand co-incidence of large prime factors
can be ruled out, and we have a set B that gives us the upper bound in Corollary 2 for
D = 2. Indeed this construction is also suitable for the upper bounds in Theorem 1 and
for Proposition 4 for D = 2, and is easily generalized to also obtain these results for all
D ≥ 3.
Let ω(m) denote the number of distinct prime factors of integer m. Fix C > ζ(2), and
let
 k = [log log N ], y = C log N
k log log N and z = [1
2 log log log N ]

with m = ∏
p≤y p and R = ∏
p≤z p, so that R = o(k), and 2k ≤ m
k ≤ e
O(ky) = N o(1). We
will show that R2(N ) is visible from S = {(ij, l) : 1 ≤ j ≤ k, 1 ≤ l ≤ y}, for various
choices of i1, i2, . . . , ik ∈ {1, 2, . . . , N }.

Lemma 1. Suppose that N is large and y, z, m and R are as above. Suppose that n is
an integer ≤ N with gcd(n, R) = d. The number of integers in an interval of length y
that are coprime with n is

≥ y
 



φ(d)
d − ∑

z<p≤y
p|n
 1
p




 − 2
ω(d) − ω(n).

Proof. The number of integers in a given interval of length y that are divisible by g is
y/g + rg where |rg| ≤ 1. Therefore, by inclusion-exclusion, the number of integers in a
given interval of length y that are coprime with d is
∑

g|d µ(g) ( y
g + rg
) = φ(d)
d y + ∑

g|d µ(g)rg ≥ φ(d)
d y − 2
ω(d).

8 SUKUMAR DAS ADHIKARI AND ANDREW GRANVILLE

To get a lower bound on the number coprime to n we simply bound the number of integers
in the interval divisible by prime factors of n that are > z: This is ≤ y/p + 1 if z < p ≤ y
and ≤ 1 if p > y. The result follows.

Proof of Proposition 4 for D = 2. We will show that there are o((N/m)k) k-tuples of
integers (i1, i2, . . . , ik), with each ij ≤ N and ij ≡ j (mod m), such that there exists an
integer n for which gcd(n − ij, l) > 1 for every integer l in some given interval of length
y. Then, for almost all of the k-tuples of integers (i1, i2, . . . , ik) with each ij ≤ N and
ij ≡ j (mod m), for every integer n ≤ N and every integer r, there exists an integer
l, 1 ≤ l ≤ y such that gcd(n − ij, r − l) = 1. In other words, R2(N ) is visible from
S = {(ij, l) : 1 ≤ j ≤ k, 1 ≤ l ≤ y}, as claimed.
So, for a given integer n, suppose that gcd(n − ij, l) > 1 for every integer l in some
given interval of length y. By Lemma 1, with d = gcd(n − ij, R), this implies that

(6) ω(n − ij) ≥ y
 



φ(d)
d − ∑

z<p≤y
p|(n−ij )
 1
p
 



 − 2
ω(d) ≥ y
 



 φ(d)
d − ∑

z<p≤y
p|(n−ij )
 1
p + o(1)





 .

Now suppose that we are given a k-tuple of integers (i1, i2, . . . , ik) with each ij ≤ N and
ij ≡ j (mod m). Let J be the set of j, 1 ≤ j ≤ k for which ∑

z<p≤y, p|(n−ij ) 1/p ≥ 1/ log z,

so that ω(n − ij) ≥ ( φ(d)
d + o(1)
) y if j ̸∈ J, by (6). Now

|J|
log z ≤
 k∑

j=1
 ∑

p|(n−ij )
z<p≤y
 1
p = ∑

z<p≤y
 1
p #{j : 1 ≤ j ≤ k and j ≡ ij ≡ n (mod p)}

≤ ∑

z<p≤y
 1
p
 ( k
p + 1) ≤ k ∑

z<p≤y
 1
p2 + ∑

z<p≤y
 1
p ≪ k
z log z ,

so that |J| ≪ k/z.
Now ﬁx J ⊂ {1, 2, . . . , k} with |J| ≪ k/z. A famous result of Hardy and Ramanujan
states that the number of integers ≤ N with exactly r distinct prime factors is

≪ N
log N (log log N + O(1))
r−1

(r − 1)! .

Hence the number of k-tuples of integers (i1, i2, . . . , ik) with each ij ≤ N and ij ≡ j
(mod m), such that gcd(n − ij, l) > 1 for every integer l in some given interval of length
y, and where the set of j, 1 ≤ j ≤ k for which ∑
z<p≤y, p|(n−ij ) 1/p ≥ 1/ log z is precisely

VISIBILITY 9

J, is less than N to the power

∑

1≤j≤k
d=gcd(n−j,R)
j̸∈J
 (
1 − C
k
 ( φ(d)
d + o(1)
)) + ∑

j∈J 1

= k − C
k
 ∑

1≤j≤k
d=gcd(n−j,R)
 φ(d)
d + o(1) = k − C
k
 ( k
R + O(1)
) ∑

1≤j≤R
d=gcd(n−j,R)
 φ(d)
d + o(1).

= k − C
R
 ∑

d|R φ(R/d)φ(d)
d + o(1) = k − C ∏

p≤z
 1
p
 (
p − 1 + 1 − 1
p
 ) + o(1)(7)
 = k − C ∏

p≤z
 (
1 − 1
p2
 ) + o(1) = k − C
ζ(2) + o(1)

Now the number of possible such sets J is ≤ 2
k < N o(1). Therefore, since C > ζ(2), the
number of k-tuples of integers (i1, i2, . . . , ik) with each ij ≤ N and ij ≡ j (mod m) such
that there exists an integer n for which gcd(n − ij, l) > 1 for every integer l in some given
interval of length y, is
 ≤ N · N k−C/ζ(2)+o(1) = o((N/m)
k),

since m
k ≤ N o(1), which was the result stated at the start of the proof.

Sketch of the proof of Proposition 4 for D ≥ 3. Keep k, z, m and R as above.
Consider the sets

S = {(ij, x2, x3, . . . , xD) : 1 ≤ j ≤ k, 1 ≤ xi ≤ y}, where y := ( C log N
k log log N
 ) 1
D−1 .

The analogy to Lemma 1 is that for any given integers v2, . . . , vD the number of elements
(x2, x3, . . . , xD), with each xi an integer in [1, y], for which (n, x2 − v2, x3 − v3, . . . , xD −
vD) = 1, is
 ≥ yD−1
 


∏

p|d
 (
1 − 1
pD−1
 ) − o(1)



 − ω(n).

One proves this, analogously, by noting that the number of such elements for which
gcd(n, x2 − v2, x3 − v3, . . . , xD − vD) is divisible by d is (y/d + O(1))
D−1 = (y/d)
D−1 +
O((y/d)D−2) if d ≤ y; moreover this number of elements is ≤ (y/d + 1)
D−1 ≤ (2y/d)
D−1

if d ≤ y, and ≤ 1 if d > y. In the calculation one majorizes the additional term
2
D−1 ∑

z<p≤y, p|n 1/p
D−1 ≪D 1/z = o(1), which simpliﬁes the subsequent argument since
the (analogy to the) set J is now empty.

10 SUKUMAR DAS ADHIKARI AND ANDREW GRANVILLE

Hence in place of (7) we obtain

= k − C
R
 ∑

d|R φ(R/d) ∏

p|d
 (
1 − 1
pD−1
 ) + o(1)

= k − C ∏

p≤z
 1
p
 (
p − 1 + 1 − 1
pD−1
 ) + o(1) = k − C
ζ(D) + o(1),

and the rest of the proof goes through analogously taking C > ζ(D).

6. Irrational orientation in 2-dimensions

In this section we will prove Theorem 8, which shows that the visibility properties of
thin convex bodies that are irrationally oriented, are quite diﬀerent from the visibility
properties of thin convex bodies that are rationally oriented.
We begin with a lemma that shows that we need only study visibility for the lattice
points inside rectangular boxes

Lemma 10. For any bounded, closed convex body A ⊂ R
2 there exist rectangular boxes
B1 ⊂ A ⊂ B2, with parallel sides, such that each side length in B1 is one-third the length
of the parallel side in B2.

Remark: Hadwiger [10] showed that for any bounded, closed convex body A ⊂ R
d there
exist such rectangular boxes B1 ⊂ A ⊂ B2 with Vol(B2) ≤ d!dd Vol(B1). On the other
hand if A is a sphere then one can easily show that one must have Vol(B2) ≥ d
d/2 Vol(B1).
It remains to determine the “best possible” constant in d-dimensions.

Proof. Select two points of A at maximal distance from one another, say P1 and P2, and
draw a line L between them. On each side of L, ﬁnd a point at maximal distance from
L. Call these two points Q1 and Q2. Let B2 be the box with two sides parallel to L
going through Q1 and Q2, and then two sides perpendicular to L going through P1 and
P2; evidently A ⊂ B2 by convexity.
Let Lj be the line perpendicular to L going through Qj, for j = 1, 2, and then let Rj
be the intersection point of L and Lj. The triangle formed by Pi, Qj, Rj lies inside A by
convexity. Let Pi,j be the point one-third of the way between Pi and Rj; and then let
Qi,j be the point on the line joining Pi and Qj such that the line joining Pi,j and Qi,j is
perpendicular to L. Note that the distance between Pi,j and Qi,j is one third the distance
between Qj and Rj, by similarity. Hence the rectangle, Si,j, with one side the segment
of L between Pi,j and Rj, and a second side the line segment between Pi,j and Qi,j, lies
in A, by convexity. Next we join the rectangles S1,j and S2,j, to get a new rectangle
which lies inside A: This contains Sj, one side of which is the middle third of the line
segment between P1 and P2, and has width one third of the distance between Qj and Rj,
in the direction of Qj. (That this lies inside S1,j ∪ S2,j follows since P1,j is one third of
the way between P1 and Rj, so at most one third of the way between P1 and P2). Then
B1 = S1 ∪ S2.
 VISIBILITY 11

Proposition 11. Let A be a normalized set of lattice points with the notation of Theorem
8, and let B ⊂ Z
2 be the smallest set of lattice points from which A is visible. If N− ≥
N 1−o(1)
+ then |B| ∼ L(N+). So, now assume that N− ≤ N 1−ϵ
+ , and select i, j ≥ 1 so that
N+/N− ∈ [qj−1q2
j , qjq2
j+1) ∩ [qi−1qi, qiqi+1). We have the following lower bounds:
(i) If N+/N− ∈ [qj−1q2
j , q2
j qj+1) then |B| ≳ L(N−qj); and
(ii) If N+/N− ∈ [q2
j qj+1, qjq2
j+1) then |B| ≳ L(N+/qjqj+1).
And we have the following upper bounds:
(iii) If N+/N− ∈ [qi−1qi, q2
i ) then |B| ≲ L(N+/qi); and
(iv) If N+/N− ∈ [q2
i , qiqi+1) then |B| ≲ L(N−qi).

Proof: By deﬁnition N− ≤ N+. One can deduce from the proof of Lemma 10 that
there exist squares B′
1, B′
2 with sides parallel to the axes, of side lengths N−/2 and N+,
respectively, such that B′
1 ⊂ B1 ⊂ A ⊂ B2 ⊂ B′
2. It follows from Theorem 1 that the
smallest set B from which all of A is visible, satisﬁes L(N−) ≲ |B| ≲ L(N+). In particular
if N− ≥ N 1−o(1)
+ then |B| ∼ L(N+).
Therefore, henceforth, we may assume that N− ≤ N 1−ϵ
+ . Moreover, via the construction
in Lemma 10, and since A is normalized, we may assume, up to a bounded factor in each
dimension, that we are studying the lattice points inside the region

(8) T = Tα(N+, N−) := {0 ≤ x, y ≤ N+ : |y − αx| ≤ N−},

where 1 ≤ α ≤ 2.
The convergents of a continued fraction satisfy several properties. First p2k+1/q2k+1 → α
from below, and p2k/q2k → α from above, as k → ∞. We will show that |α − pi
qi | ≍ 1
qiqi+1 :
One has that | pi
qi − pi−1
qi−1 | = 1
qi−1qi . We deduce the upper bound |α− pi
qi | ≤ | pi
qi − pi+1
qi+1 | = 1
qiqi+1 ,
and then the lower bound |α − pi
qi | ≥ | pi
qi − pi+1
qi+1 | − |α − pi+1
qi+1 | ≥ 1
qiqi+1 − 1
qi+1qi+2 ≥ 1
2qiqi+1 ,
since there exists an integer ai ≥ 1 such that qi+2 = aiqi+1 + qi ≥ qi+1 + qi ≥ 2qi.

Lower bounds: In the proof of Proposition 3 for D = 2, we saw that for any ﬁnite set of
lattice points, S, there exist integers 1 ≤ a, b ≤ m = ∏
p≤y p such that any lattice point
(x, y) ∈ Z
2 with x ≡ a (mod m) and y ≡ b (mod m) is invisible from S. Here π(y) = r
where r ∼ |S|/ζ(2).
We will suppose p/q = pi/qi and Q = qi+1 for some i, and assume that

(9) m
N+ ≪ ∣
∣
∣
∣α − p
q
 ∣
∣
∣
∣ ≤ N−
qm .

The distance between the consecutive numbers mn(p − qα), n ∈ Z is precisely m|qα − p|
which is ≤ N−, so at least two such multiples lie within a distance N− of αb − a. For
such a multiple, (a + mnp, b + mnq) is invisible from S by the discussion in the previous
paragraph, and |(a + mnp) − α(b + mnq)| ≤ N−. Now

|a + mnp|, |α(b + mnq)| ≪ mn|αq| ≪ |αb − a|
|p − qα| · |q| ≪ m
|p/q − α| ≪ N+

12 SUKUMAR DAS ADHIKARI AND ANDREW GRANVILLE

using (9) and the bounded range for α, so that (a + mnp, b + mnq) ∈ Tα(N+, N−).
Now |α − p/q| ≍ 1/qQ. Hence the above construction works provided (9) holds, that is

m ≪ M− := min {
QN−, N+
qQ
 } ,

and therefore, taking m as large as possible in this range,

|B| ≳ ζ(2)r ∼ ζ(2) y
log y ∼ L(m) ∼ L(M−).

Upper bounds: We make a unitary linear transformation on the region Tα(N+, N−), so
that visibility is preserved:
 X = qiy − pix, Y = qi−1y − pi−1x,

Then X = qi(y − αx) − (pi − αqi)x so that

|X| ≤ qi|y − αx| − |pi − αqi|x ≤ qiN− + N+
qi+1

By Proposition 4 we deduce that |B| ≲ L(qiN− + N+
qi+1 ).

Deduction of Theorem 8: We compare the upper and lower bounds of Proposition 11:
Suppose that N+/N− ∈ [q2
i , qiqi+1) ∩ [qj−1q2
j , q2
j qj+1). In this range qiqi+1 ≥ qj−1q2
j >
qj−1qj, and so i ≥ j. If i = j then |B| ∼ L(N−qj) (note that, in this case qi+1 ≥ qiqi−1).
If i ≥ j + 1 then q2
j qj+1 ≥ q2
i ≥ q2
j+1 so that q2
j ≥ qj+1, and thus (N−qj)
4 ≥ N 4
−q2
j qj+1 ≥
N 3
−N+ ≥ N 4
−q2
i , so that L(N−qj) ≳ 1
2L(N−qi). Hence by (i) and (iv) we have (3).
If N+/N− ∈ [q2
i , qiqi+1) ∩ [q2
j qj+1, qjq2
j+1) then qiqi+1 ≥ q2
j qj+1 > qjqj+1, so that i ≥ j +1.
If qj+1 < q2
j N 2
− then N 3
+ > (N−q2
j qj+1)3(qj+1q2
j N 2
−) = N−(qjqj+1)4, whence (N+/qjqj+1)4 >
N+N− ≥ (N−qi)
2. If qj+1 ≥ q2
j N 2
− then (N+/qjqj+1)
2 ≥ N 2
−N 2
+/q3
j+1 ≥ N 4
−q4
i /q3
j+1 ≥
N 4
−qi ≥ N−qi. Hence we recover (3) from (ii) and (iv).
If N+/N− ∈ [qi−1qi, q2
i ) ∩ [q2
j qj+1, qjq2
j+1) then q2
i > q2
j qj+1 ≥ q2
j so that i ≥ j + 1. Now
N−q2
j qj+1 ≥ N+ and so (N−qj)
2 ≥ N−N+/qj+1 ≥ N−N+/qi ≥ N+/qi. Hence we have (4)
by (i) and (iii).
If N+/N− ∈ [qi−1qi, q2
i ) ∩ [q2
j qj+1, qjq2
j+1) then q2
i > q2
j qj+1 ≥ q2
j so that i ≥ j + 1. Now
(N+/qjqj+1)
2 ≥ N−N+/qj+1 ≥ N−N+/qi ≥ N+/qi, we recover (4) from (ii) and (iii).
We can be more precise for small N+/N− (≤ q2
2): If N+/N− ≤ q2 then |B| ∼ L(N−);
and if q2 ≤ N+/N− < q2
2 then |B| ∼ L(N+/q2).

Before deducing Theorems 5, 6 and 7, we should note that act of “normalizing” S, that
is applying the map α → 1 + 1/α if α > 1, has little eﬀect on the convergents pj/qj:

Deduction of Theorem 5: If α ∈ Q we simply perform an invertible linear transforma-
tion (with integer coeﬃcients) to obtain a new convex body with α = 0, and then apply
Theorem 1. If α ̸∈ Q apply Theorem 8 with N+ = q2
i .

VISIBILITY 13

Deduction of Theorem 6: Since qk+1 = q1+o(1)
k , Proposition 11 gives us that if N− ≤
N 1−ϵ
+ , N+/N− = q3+o(1)
j and N+/N− = q2+o(1)
i then |B| ≳ L(N−qj) ∼ 1
3L(N+) + 2
3L(N−)
and |B| ≲ L(N−qi) ∼ 1
2L(N+) + 1
2L(N−). The result follows.

Deduction of Theorem 7: If log N− ≫ log N+ then |B(A)| ≍ L(N+) by Theorem 8;
so henceforth we will assume log N− = o(log N+). Now if log qj ≥ c log qj+1 for all j ≥ 2
then, in the ﬁrst case of Theorem 8 we have N−qi ≥ N−(qiqi+1) c
c+1 ≥ N−(N+/N−) c
c+1 , and
N+/qi ≥ N−qi−1 ≥ N−qc
i ≥ N−(N+/N−)
c/2 in the second case, so that |B(A)| ≫ L(N+).
Now suppose that log qj = o(log qj+1) for some inﬁnite sequence of integers j, let N− = 1
and N+ = qj+1, so the ﬁrst case of Theorem 8 yields that |B(A)| ≲ L(qj) = o(L(qj+1)) =
o(L(N+)).
 References

[1] H. L. Abbott, Some results in combinatorial Geometry, Discrete Mathematics 9, 199–204 (1974).
[2] S. D. Adhikari, Some questions regarding visibility of integer lattice points in IRd, Proceedings of
the Session in Analytic Number Theory and Diophantine Equations (Bonn, January – June 2002)
(Eds. D. R. Heath-Brown and B. Z. Moroz), Bonner Mathematische Schriften, Nr. 360.
[3] S. D. Adhikari and R. Balasubramanian, On a question regarding visibility of lattice points, Math-
ematika 43, 155–158 (1996).
[4] S. D. Adhikari and Yong-Gao Chen, On a question regarding visibility of lattice points-II, Acta
Arithmetica 89, no. 3, 279–282 (1999).
[5] S. D. Adhikari and Yong-Gao Chen, On a question regarding visibility of lattice points-III, Discrete
Mathematics, 259, no. 1-3, 251–256 (2002).
[6] Peter Brass, William Moser and J´anos Pach, Research Problems in Discrete Geometry, Springer,
2005.
[7] Y. -G. Chen and L. -F. Cheng, Visibility of lattice points, Acta Arithmetica 107, no. 3, 203–207
(2003).
[8] P. Erd˝os, P. M. Gruber and J. Hammer, Lattice Points, Pitman Monographs and Surveys in Pure
and Applied Mathematics 39, John Wiley and Sons, New York, 1989.
[9] Richard K. Guy, Unsolved Problems in Number Theory, Third Edition, Springer, 2004.
[10] H. Hadwiger, Volumsch¨atzung f¨ur die einen Eik¨orper ¨uberdeckenden und unterdeckenden Parallelo-
tope, Elem. Math. 10, 122–124 (1955).
[11] Joshua Laison and Michelle Schick, Seeing dots: visibility of lattice points, Math. Mag., 80, no. 4,
274–282 (2007).

Sukumar Das Adhikari (adhikari@mri.ernet.in),
Harish-Chandra Research Institute,
Chhatnag Road, Jhusi, Allahabad 211019, India.

Andrew Granville (andrew@dms.umontreal.ca),
D´epartment de Math´ematiques et de Statistique,

14 SUKUMAR DAS ADHIKARI AND ANDREW GRANVILLE

Universit´e de Montr´eal, C. P. 6128,
Succ. Centre-Ville, Montr´eal, QC H3C 3J7, Canada.
