<!-- source: https://library.slmath.org/books/Book52/files/22last.pdf | converted from PDF -->

Combinatorial and Computational Geometry
MSRI Publications
Volume 52, 2005

Two Proofs for Sylvester’s Problem
Using an Allowable Sequence of Permutations

HAGIT LAST

Abstract. The famous Sylvester’s problem is: Given ﬁnitely many non-
collinear points in the plane, do they always span a line that contains
precisely two of the points? The answer is yes, as was ﬁrst shown by Gallai
in 1944. Since then, many other proofs and generalizations of the problem
appeared. We present two new proofs of Gallai’s result, using the powerful
method of allowable sequences.

1. Introduction

Sylvester [1893] raised the following problem: Given ﬁnitely many noncollinear
points in the plane, do they always span a simple line (that is, a line that contains
precisely two of the points)? The answer is yes, as was ﬁrst shown by Gallai
[1944].
By duality, the former question is equivalent to the question: Given ﬁnitely
many straight lines in the plane, not all passing through the same point, do they
always determine a simple intersection point (a point that lies on precisely two
of the lines)?
A natural generalization is to ﬁnd a lower bound on the number of simple
lines (or simple points, in the dual version). The dual version of this question
can be generalized to pseudolines. The best lower bound [Csima and Sawyer
1993] states that an arrangement of n pseudolines in the plane determines at
least 6n/13 simple points. The conjecture [Borwein and Moser 1990] is that
there are at least n/2 simple points for n ̸= 7, 13. For the history of Sylvester’s
problem, with its many proofs and generalizations, see [Borwein and Moser 1990;
Nilakantan 2005].
This paper presents two new proofs of Gallai’s result using allowable se-
quences. A proof of Gallai’s result using allowable sequences was given recently
by Nilakantan [2005], but it diﬀers from the two given here.

433

434 HAGIT LAST

The notion of allowable sequences was introduced by Goodman and Pollack
[1980]. It has proved to be a very eﬀective tool in discrete and computational
geometry; for a broad discussion see [Goodman and Pollack 1993]. Here is a
short description of the notion.
Let S be a set of n points in the plane, let L be the set of the lines spanned
by S, and let {k1, k2, . . . , km} be the m diﬀerent slopes of the lines according to
a ﬁxed coordinate system. We choose a directed line l in the plane with a point
P on it, such that l does not contain any point of S and is not orthogonal to any
line in L.
Here is the construction of Al,P (S), the allowable sequence of permutations
of a point set S, according to the directed line l and the point P : We label
the points of S according to their orthogonal projection on l and we get the
ﬁrst permutation π0 = 1, . . . , n. Let l rotate counterclockwise around P by
180◦ and look at the orthogonal projections of the labeled points of S on l as
it rotates. A new permutation arises whenever l passes through a direction
orthogonal to one of the slopes k1, k2, . . . , km. It follows that along the course of
this rotation, beside π0, we will get m diﬀerent permutations: π1, . . . , πm. Deﬁne
Al,P (S) = {π0, π1, π2, . . . , πm}.
For each 1 ≤ i ≤ m, whenever l passes through a direction orthogonal to ki,
the new permutation that arises diﬀers from the previous one by reversing the
order of the consecutive elements whose corresponding points of S lie on a line
of slope ki. Such reversed consecutive elements are called a reversed substring.
If t lines in L have a slope equal to ki, the permutation that corresponds to ki
has t disjoint reversed substrings. A reversed substring of length 2 is called a
simple switch. A simple switch corresponds to a simple line.
Three important properties of Al,P (S) are:

1. Al,P (S) is a sequence of permutations of the elements {1, 2, . . . , n}, where n
is the cardinality of S.
2. The ﬁrst permutation is π0 = 1, . . . , n − 1, n, and the last is πm = n, n −
1, . . . , 1. Here m is the number of diﬀerent slopes of the lines spanned by S.
If the points of S are not collinear, then m > 1 (actually m ≥ n − 1, as was
proved in [Scott 1970]).
3. In the course of the sequence of permutations, every pair i < j switches exactly
once and so each permutation diﬀers from the previous one by reversing at
least one increasing substring. Only increasing substrings are reversed.

For example, if πi = 1, 7, 2, 4, 6, 3, 5, then N1 = 1, 7, N2 = 2, 4, N3 = 2, 4, 6,
and N4 = 3, 5 are its increasing substrings, and so πi+1 is obtained from πi by
reversing the order of one or more of these substrings.
For the convenience of writing the proofs in Section 2, we would like to assume
that in each step only one increasing substring is reversed. We can arrange this
by replacing each permutation that contains t reversed substrings by t permuta-
tions, as we reverse a single substring at a time. The length of the new sequence

TWO PROOFS FOR SYLVESTER’S PROBLEM 435

of permutations, A, is the cardinality of L and satisﬁes the condition that each
permutation diﬀers from the previous one by reversing a single increasing sub-
string.
 2. The Proofs

Let S be a set of n noncollinear points in the plane. We will show the existence
of a simple spanned line by proving that A contains a permutation with a simple
switch. Assume, for a contradiction, that each reversed substring has length at
least 3.
Since S is a set of noncollinear points, then A has length greater than 2, with
π0 = 1, 2, . . . , n and πm = n, n − 1, . . . , 1 (m > 1).
For 1 ≤ r ≤ m, denote by Jr the reversed substring of πr and denote by Ir
the increasing substring of πr−1 which is reversed at πr. Jr and Ir consist of the
same set of elements, in Jr the elements are in decreasing order and in Ir they
are in increasing order. For example, if π1 = 1, 2, 5, 4, 3, π2 = 5, 2, 1, 4, 3, then,
I2 = 1, 2, 5, J2 = 5, 2, 1.
For Jr = a1, a2, . . . , ak−1, ak, we will refer to a2, . . . , ak−1 as its internal ele-
ments. By our assumption, every Ir as well as every Jr has an internal element.

Proof 1. We show that an internal element of a reversed substring cannot
change its location before a simple switch occurs.
For every 0 ≤ k ≤ m and every element 1 ≤ a ≤ n, denote by Tk(a) the
location of the element a in πk. For example, Tm(n − 1) = 2.
If Tk(a) ̸= Tk−1(a), we say that JK changed the location of the element a. If
Tk(a) > Tk−1(a), we say that a moves to the right at πk.
A reversed substring, Jr, is centrally symmetric, if it is symmetric around
the middle of the permutation. For example, If π1 = 1, 2, 3, 6, 5, 4, 7, 8, 9, then
J1 = 6, 5, 4 is centrally symmetric.
Let s be the smallest number such that Js changes the location of an element
which was an internal element in Jt for t < s. Such s must exist, otherwise, all
internal elements of J1 are already on their ﬁnal positions at πm. This means
that J1 is centrally symmetric. But then J2 cannot be centrally symmetric and
so its internal elements must later change their locations in order to be on their
ﬁnal positions at πm.
Let a be an internal element of Jt with t < s, such that Js changes the location
of a. Without loss of generality, Ts(a) > Tt(a). Since a moves to the right, there
exist b, c such that a, b, c are consecutive elements of πs−1 and a < b < c. Since
a is an internal element of Jt, there are d, e such that d, a, e are consecutive
elements of πt and d > a > e.
Let πl, t < l < s − 1, be the ﬁrst permutation in which b is the right neighbor
of a. Then there exist f, g such that a, b, f, g are consecutive elements of πl and
a < b > f > g. Since Ts−1(a) = Tl(a), it follows that Ts−1(c) = Tl(f ). That
means that before a moves to the right at πs, f needs to change its location. But

436 HAGIT LAST

f is an internal element in Jl and so, no Jd, l < d < s, can change the location of
f (otherwise, it contradicts the deﬁnition of s). We conclude that such s cannot
exist, which leads a contradiction. ˜

Second proof. A substring of three consecutive elements x, y, z in a permuta-
tion is called a bad triplet if x < z but x, y, z are not in an increasing order.
Let πl be the last permutation that contains a bad triplet x, y, z. Such πl
exists because π1 has a bad triplet but πm does not. For example, if π1, πm are
π1 = 1, 4, 3, 2, 5, 6, πm = 6, 5, 4, 3, 2, 1, then π1 has two bad triplets 1, 4, 3 and
3, 2, 5. πm is in decreasing order, so it contains no bad triplet.
To get a contradiction, we show here that at least one of the permutations
that follows πl contains a bad triplet.
Suppose that none of the permutations that follows πl contains a bad triplet.
Then either x or z (but not both) are elements of Jl+1. Assume that x ∈ Jl+1
(similar arguments can be used for the case z ∈ Jl+1).
We deﬁne the closed interval [a, b]d to be the part of the permutation πd that
contains the consecutive elements between a and b including a and b. Example,
for πd : 6, 3, 2, 1, 5, 4 [3, 5]d = 3, 2, 1, 5.
We now consider two cases:

Case 1: x, y ∈ Jl+1.
Then x is the right neighbor of y in Jl+1, and Jl+1 contains at least one more
element to the right of x. Let a be the rightmost element of Jl+1 and b its left
neighbor. Then z > x ≥ b > a, from which follows that b, a, z are consecutive
elements of πl+1 satisfying b > a < z and b < z, which means that b, a, z is a
bad triplet.

Case 2: x ∈ Jl+1, y /∈ Jl+1.
Let s = min{k | k > l + 1 and x ∈ Jk is not the leftmost element in Jk}. Such
s exists since z > x and z, x are not yet reversed at πl+1. Denote by c the left
neighbor of x in Js. Then x, c are consecutive elements of πs−1 and x < c.
Let t = max{k | k < s and x ∈ Jk}. Note that since x is an element of Jl+1
and l + 1 < s, such t exists and satisﬁes l + 1 ≤ t < s. Also, note that since x is
the leftmost element of Jl+1, x is the leftmost element in Jt.
Let a, b be the two right neighbors of x in Jt. Then x, a, b are three consecutive
elements of πt and x > a > b.
Since x /∈ Jr for t < r < s, it follows that in order for c to be the right neighbor
of x in πs−1, c must switch with b ﬁrst, and then with a, in permutations between
t and s. So there exists r, t < r < s, such that c, b ∈ Jr and there exists q,
r < q < s, such that c, a ∈ Jq.
We claim that for every j satisfying t ≤ j < s, [x, b]j contains no increasing
substring of length greater than 2. Also, the three rightmost elements in [x, b]j
are in decreasing order.
We will prove it by induction. For j = t the claim holds. By the induction
hypothesis, the three rightmost elements in [x, b]j−1 are in decreasing order and

TWO PROOFS FOR SYLVESTER’S PROBLEM 437

Ij ̸⊂ [x, b]j−1. Since, in addition, x /∈ Ij, it follows that if Ij contains elements
of [x, b]j−1, it must contain b only. If it does, the three rightmost elements of Jj
are the three rightmost elements of [x, b]j and are in decreasing order.
Any increasing substring in [x, b]j can consist of only two elements, each of
which belongs to a diﬀerent reversed substring involving b. This completes the
proof of the claim. By the deﬁnition of r, for every j satisfying r ≤ j < s we have
c ∈ [x, b]j, but by the above claim, Ij ̸⊂ [x, b]j−1, which implies that c cannot
switch with a in a permutation that precedes πs. So q as deﬁned above cannot
exist: a contradiction. ˜

Acknowledgments

We thank Gil Kalai and Rom Pinchasi for useful discussions.

References

[Borwein and Moser 1990] P. Borwein and W. O. J. Moser, “A survey of Sylvester’s
problem and its generalizations”, Aequationes Math. 40:2-3 (1990), 111–135.

[Csima and Sawyer 1993] J. Csima and E. T. Sawyer, “There exist 6n/13 ordinary
points”, Discrete Comput. Geom. 9:2 (1993), 187–202.

[Goodman and Pollack 1980] J. E. Goodman and R. Pollack, “On the combinatorial
classiﬁcation of nondegenerate conﬁgurations in the plane”, J. Combin. Theory Ser.
A 29:2 (1980), 220–235.

[Goodman and Pollack 1993] J. E. Goodman and R. Pollack, “Allowable sequences
and order types in discrete and computational geometry”, pp. 103–134 in New
trends in discrete and computational geometry, edited by J. Pach, Algorithms and
Combinatorics 10, Springer-Verlag, Berlin, 1993.

[Nilakantan 2005] N. Nilakantan, “On some extremal problems in combinatorial geom-
etry”, pp. 477–492 in Combinatorial and computational geometry, edited by J. E.
Goodman et al., Math. Sci. Res. Inst. Publ. 52, Cambridge U. Press, New York,
2005.

[Scott 1944] P. R. Scott, “Solution to Problem 4065”, Amer. Math. Monthly 51 (1944),
169–171.

[Scott 1970] P. R. Scott, “On the sets of directions determined by n points”, Amer.
Math. Monthly 77 (1970), 502–505.

[Sylvester 1893] J. J. Sylvester, “Mathematical question 11851”, Educational Times
46 (1893), 156.

Hagit Last
Institute of Mathematics
The Hebrew University
91904 Jerusalem
Israel
hagitl@math.huji.ac.il
