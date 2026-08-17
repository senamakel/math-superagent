<!-- source: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v23i3p23/pdf | converted from PDF -->

New Conjectures For Union-Closed Families

Jonad Pulaj

Dept. of Optimization
Zuse Institute Berlin
Takusstraße 7
14195 Berlin
Germany

pulaj@zib.de
 Annie Raymond

Dept. of Mathematics
University of Washington
Box 354350
Seattle, WA 98195
United States

raymonda@uw.edu
 Dirk Theis

Inst. of Computer Science
University of Tartu
Juhan Liivi 2
50409 Tartu
Estonia

dirk.theis@ut.ee

Submitted: Dec 1, 2015; Accepted: Jul 27, 2016; Published: Aug 5, 2016
Mathematics Subject Classiﬁcations: 05D05, 90C27

Abstract

The Frankl conjecture, also known as the union-closed sets conjecture, states
that in any ﬁnite non-empty union-closed family, there exists an element in at least
half of the sets. From an optimization point of view, one could instead prove that 2a
is an upper bound to the number of sets in a union-closed family on a ground set of
n elements where each element is in at most a sets for all a, n ∈ N+. Similarly, one
could prove that the minimum number of sets containing the most frequent element
in a (non-empty) union-closed family with m sets and n elements is at least m
2 for
any m, n ∈ N+. Formulating these problems as integer programs, we observe that
the optimal values we computed do not vary with n. We formalize these observations
as conjectures, and show that they are not equivalent to the Frankl conjecture while
still having wide-reaching implications if proven true. Finally, we prove special cases
of the new conjectures and discuss possible approaches to solve them completely.

1 Introduction

The union-closed sets conjecture is a celebrated open problem in combinatorics which
was popularized by Frankl in the late 1970’s [Fra83], and is thus often referred to as the
Frankl conjecture. Before stating the conjecture, we need a few deﬁnitions. Throughout
this paper, we think of a family of sets or set system F = (E(F), S(F)) as being a
collection S(F) of distinct sets S such that every set S ⊆ E(F) where E(F) is the
ground set of elements. In general, we let E(F) = {1, . . . , n} =: [n]. A family of sets is
said to be union-closed if and only if the union of two sets of the family is also a set of
the family.

Conjecture 1 (Frankl, 1979). In a union-closed family F such that S(F) ̸= {∅}, there
exists an element of E(F) that is in at least half of the sets of S(F).

the electronic journal of combinatorics 23(3) (2016), #P3.23 1

Since 1979, the conjecture has attracted the attention of both lattice theorists as well
as combinatorial probabilists, and, more recently, computer scientists. To the best of
our knowledge, this is the ﬁrst time the problem is investigated through combinatorial
optimization. After deﬁning a few more concepts, we give an overview of the literature
and present our contributions.
Let m(F) and n(F) be respectively the numbers of sets and elements of a family
F, i.e., m(F) = |S(F)| and n(F) = |E(F)|. Moreover, let me(F) be the number of
sets in F containing some element e ∈ E(F). Let the degree of F, denoted by a(F),
be the maximum number of sets in F containing any element of E(F), that is, a(F) =
maxe∈E(F ) me(F). Let e∗(F) be an arbitrary element of maximum degree, i.e., any of
possibly many elements in E(F) contained in a(F) sets. For example, if F is such that
E(F) = [3] and S(F) = {{1, 2, 3}, {1, 2}, {1, 3}, ∅}, then F is union-closed, m(F) = 4,
n(F) = 3, m1(F) = 3, m2(F) = 2, m3(F) = 2, a(F) = 3 and e∗(F) = 1. Since 3
4 ⩾ 1
2,
the Frankl conjecture holds for F.

1.1 A bit of history

Conjecture 1 is known to hold for certain speciﬁc families. For example, it has long been
known that the conjecture is trivially true for any family F containing a singleton or
a pair, i.e., when there exists S ∈ S(F) such that |S| = 1 or 2, or when the average
size of the sets, 1
m(F ) ∑
S∈S(F ) |S|, is greater or equal to n(F )
2 . Another early result is the
following:

Theorem 2 (Roberts, 1992). The inequality m(F) < 4n(F)−1 holds for any union-closed
family F that is a minimum counterexample to the Frankl conjecture.

The above results and a few others allowed the conjecture to be proven for increasing
values of m and n over time ([SR89], [SR90], [Far94b], [Poo92], [GY98], [Rob92]). The
current status is as follows:

Theorem 3 (Roberts and Simpson, 2010). The Frankl conjecture is true for any family
F with m(F) ⩽ 46.

Theorem 4 (Boˇsnjak and Markovi´c, 2008). The Frankl conjecture is true for any family
F with n(F) ⩽ 11.

More recently, Vuˇckovi´c and ˇZivkovi´c announced the following result which is still
unpublished.

Theorem 5 (Vuˇckovi´c and ˇZivkovi´c, 2012). The Frankl conjecture is true for any family
F such that n(F) ⩽ 12 and m(F) ⩽ 50.

Thus the conjecture is still open for m(F) ⩾ 51 and n(F) ⩾ 13. A breakthrough in
the ﬁeld is the following result from Reimer [Rei03].

Theorem 6. For any union-closed family F, 1
m(F ) ∑
S∈S(F ) |S|, the average size of sets,
is at least 1
2 log2(m(F)).

the electronic journal of combinatorics 23(3) (2016), #P3.23 2

We now turn our attention to three important results which are quite useful for the
purposes of this paper. Firstly, Balla, Bollob´as and Eccles recently proved that the Frankl
conjecture holds for families F containing at least 2
3 of the sets in the power set of n(F).

Theorem 7 (Balla, Bollob´as & Eccles, 2013). The union-closed conjecture holds for any
family F where m(F) ⩾ 2
32
n(F ).

Even more recently, Eccles strengthened this result by proving a stability version in
[Ecc15]. Secondly, instead of proving the Frankl conjecture, one could instead try to prove
that any union-closed family contains an element present in at least some fraction of the
sets, just as Knill did in the following theorem.

Theorem 8 (Knill, 1994). In any union-closed family F, there always exists an element
present in at least m(F )−1
log2 m(F ) sets, that is, a(F) ⩾ m(F )−1
log2 m(F ) .

W´ojcik improved this result slightly in [W´oj99], but, amazingly, still no constant frac-
tion is known. Thirdly, Bruhn and Schaudt in [BS14] observed the following corollary to
Reimer’s theorem and the bounds from [VZ12].

Theorem 9 (Bruhn & Schaudt, 2013). Let F be any union-closed family F such that
2
n(F )−1 < m(F) ⩽ 2
n(F ). Then a(F) ⩾ 6
13 · m(F), i.e., there exists an element in a least
6
13 of the sets of the family.

Many other results have been discovered throughout the years. For a more complete
history of the problem, we refer the reader to the following excellent survey [BS14]. Finally,
we note that Timothy Gowers recently led a polymath project, FUNC, on this topic.

1.2 Our contributions

In this paper, we examine the Frankl conjecture through a diﬀerent lens by viewing it as
an optimization problem. Indeed, we can rewrite Conjecture 1 either as a maximization
or minimization problem, depending on whether we ﬁx m(F) or a(F).

Conjecture 10 (Maximization Version). For any positive integer a, let

F (a) = {F|F is a union-closed family, S(F) ̸= ∅ and a(F) ⩽ a}.

Then maxF∈F (a) m(F) ⩽ 2a for all a ∈ N+.

Conjecture 11 (Minimization Version). For any positive integer m, let

G (m) = {F|F is a union-closed family, S(F) ̸= ∅ and m(F) = m}.

Then minF∈G (m) a(F) ⩾ m
2 for all m ∈ N+.

the electronic journal of combinatorics 23(3) (2016), #P3.23 3

Note that the conjectures 1, 10 and 11 are equivalent since there exists a counterex-
ample to the original Frankl conjecture if and only if there exists a union-closed family F
such that m(F) > 0 and a(F) < m(F )
2 .
In Section 2.1, we model the optimization versions of the Frankl conjecture as integer
programs for a ﬁxed n (the number of elements in E(F) for all families F considered). In
Proposition 12, we discuss some of the properties of the optimal values of said programs.
Then in Section 2.2, we present computational results for the models. We observe that
the optimal values we computed do not vary as n increases, i.e.,

max
F∈F (a):
n(F )=n m(F) = max
F∈F (a):
n(F )=n+1 m(F)

and
 min
F∈G (m):
n(F )=n a(F) = min
F∈G (m):
n(F )=n+1 a(F)

for n ⩾ log2(a). We did not expect this and this is not necessary for the Frankl conjecture
to hold. We formally present these two observations as conjectures and prove that they
are equivalent. However, these new conjectures do not imply the Frankl conjecture, and
conversely, the Frankl conjecture does not imply these two new conjectures. Still, in
Section 2.3, we discuss some of the important implications the new conjectures have on
the Frankl conjecture. Notably, proving these conjectures would prove Conjecture 1 for
inﬁnitely many values of |S(F)| = m. Moreover, their proof would yield that there always
exists an element in 6
13 of the sets of a union-closed family, and would thus achieve the ﬁrst
known constant bound for the percentage of sets containing some element in any union-
closed family. Finally, in Section 3, we prove a restricted version of the new conjectures
using an observation of Falgas-Ravry in [FR11] and discuss the importance of twin sets,
which we deﬁne as sets that diﬀer only in one element.

2 The Frankl Integer Problems and Two New Conjectures

2.1 Modeling the Frankl optimization problems

For any positive integers a, n, let

F (n, a) = {F ∈ F (a)|n(F) = n}.

Then proving that maxF∈F (n,a) m(F) ⩽ 2a for all possible n, a would prove Conjecture 10
(and thus the original conjecture). Fix n, a, and let f (n, a) = maxF∈F (n,a) m(F). Then
we can ﬁnd f (n, a) by solving the following integer program

the electronic journal of combinatorics 23(3) (2016), #P3.23 4

f (n, a) = max ∑

S∈Sn xS

such that xU + xT ⩽ 1 + xS ∀T ∪ U = S ∈ Sn
∑

S∈Sn:e∈S xS ⩽ a ∀e ∈ [n]

xS ∈ {0, 1} ∀S ∈ Sn,

where Sn is the power set of [n], and the variable xS for any set S ∈ Sn is 1 if S is in
the family, and 0 otherwise. Thus, we maximize the number of sets while ensuring the
family is union-closed (through the ﬁrst constraint) and that a(F) ⩽ a holds (through
the second constraint), i.e., we calculate f (n, a).
Similarly, let G (n, m) = {F ∈ G (m)|n(F) = n}

for any positive integers m and large enough n. Then, it is easy to see that proving that
minF∈G (n,m) a(F) ⩾ m
2 for all large enough n and m would prove Conjecture 11. Fix n, m,
and let g(n, m) = minF∈G (n,m) a(F) for m ⩾ 2. Then we can ﬁnd g(n, m) by solving the
following integer program

g(n, m) = min ∑

S∈Sn:1∈S xS

such that xU + xT ⩽ 1 + xS ∀T ∪ U = S ∈ Sn
∑

S∈Sn:i∈S xS ⩾ ∑

S∈Sn:j∈S xS ∀1 ⩽ i ⩽ j ⩽ n

∑

S∈Sn xS = m

xS ∈ {0, 1} ∀S ∈ Sn,

where the variables xS are as before. The second constraint says that element 1 is the
element contained in the most number of sets in the family, so we are minimizing the
maximum number of sets containing the most frequent element while enforcing that the
family is union-closed (through the ﬁrst constraint) and has m sets (through the third
constraint).
Most work done on the Frankl conjecture has been from the g(n, m) point of view,
not f (n, a). Moreover, in [Ren91] and [Ren95], Renaud deﬁned ϕ(m) to be the minimum
number of sets containing the most frequent element in a family among all union-closed
families on m sets. Some of the properties he proves for ϕ(m) are not unlike those we will
prove for g(n, m).
Note moreover that there are values of a, m, n for which f (n, a) and g(n, m) have trivial
solutions that do not interest us. For example, it is clear that f (n, a) = 2
n if a ⩾ 2
n−1.

the electronic journal of combinatorics 23(3) (2016), #P3.23 5

Indeed, the power set of n, Sn, is union-closed, and there are 2n sets in Sn where each
element is in exactly 2n−1 sets. It is thus a trivially optimal solution for f (n, a). It is also
clear that g(n, m) has trivially no solution if m > 2
n. Indeed, even if we take all of the
2
n sets in Sn, we would have less sets than the number of sets required by the program.
We ﬁrst study a few properties of the functions f and g for non-trivial values of a, m, n.

Proposition 12. The following properties hold.

1. The function f is non-decreasing in n, that is, f (n, a) ⩽ f (n + 1, a) for every
a, n ∈ N+ such that n ⩾ ⌈log2 a⌉ + 1.

2. The function g is non-increasing in n, that is, g(n, m) ⩾ g(n + 1, m) for every
m, n ∈ N
+ such that n ⩾ ⌈log2 m⌉.

3. The function f is strictly increasing in a, that is, f (n, a) < f (n, a + 1) for every
a, n ∈ N
+ such that n > ⌈log2 a⌉ + 1.

4. The function g is non-decreasing in m, that is, g(n, m) ⩽ g(n, m + 1) for every
m, n ∈ N
+ such that n ⩾ ⌈log2 m⌉.

5. We have that g(n, f (n, a)) = a for all a, n ∈ N
+ such that n > ⌈log2 a⌉ + 1.

6. We have that f (n, g(n, m)) ⩾ m for all m, n ∈ N
+ such that n ⩾ ⌈log2 m⌉.

Proof.

1. Fix a, n and suppose f (n, a) = m. Take a family F that is optimal, i.e., a family
F ∈ F (n, a) such that m(F) = m. Add an element n + 1 to the family such that
this element is exactly in the same sets as some other element e of the family. Then
this augmented family is still union-closed, and every element of it is still in at most
a sets. Thus, f (n + 1, a) ⩾ m = f (n, a).

2. Just as for (1), we clone an element.

3. Fix a, n and suppose f (n, a) = m. Take a family F that is optimal (as before).
Then add to this family one of the largest sets that is not already present in the
family, i.e., a set in Sn\S(F) containing as many elements as possible. This is
always possible if f (n, a) < 2
n (note that this is the case if a < 2
n−1 since we cannot
take all of Sn then). The new family we built has m + 1 sets and is still union-
closed since taking the union of any other set with the added set will give either
the new set itself or a greater set (which is present in the family by construction).
Moreover, every element in this new family is present in at most a + 1 sets. Thus,
f (n, a + 1) ⩾ m + 1 = f (n, a) + 1.

4. Fix m, n and suppose g(n, m + 1) = a. Take a family F that is optimal (as before).
Remove the smallest set of the family, i.e., one of the sets in S(F) with the least
number of elements. The family is still union-closed since the set that was removed

the electronic journal of combinatorics 23(3) (2016), #P3.23 6

was not the union of any other two sets since they would have to be smaller. More-
over, this new family has m sets and every element is still there at most a times, so
g(n, m) ⩽ a = g(n, m + 1).

5. Fix a, n and suppose that f (n, a) = m. Thus m is the maximum number of sets in
any union-closed family F on n elements with a(F) ⩽ a. Because m ⩽ 2
n, g(n, m)
is feasible. Certainly, this implies that g(n, m) = g(n, f (n, a)) ⩽ a. Suppose that
g(n, f (n, a)) = a′ < a. Then f (n, a
′) ⩾ m. Since we have already shown that the
function f strictly increases in a when n > ⌈log2 a⌉ + 1, this is a contradiction.

6. Suppose that g(n, m) = a. Then n ⩾ ⌈log2 m⌉, else g(n, m) would be infeasible.
Thus, the most frequent element in a union-closed family with n elements and m sets
is present in a least a sets. Certainly, this means that f (n, a) = f (n, g(n, m)) ⩾ m.

2.2 Computations and Conjectures

We computed f (n, a) and g(n, m) for diﬀerent values with the mixed-integer commercial
solver IBM ILOG CPLEX version 12.4. For the source code to generate the .lp ﬁles, see
http://www.math.washington.edu/∼raymonda/frankl.py. Table 1 contains some of the
results we obtained.

Table 1: Values of f (n, a) and g(n, m) (respectively left and right)

a\n 1 2 3 4 5 6 7 8
1 2 2 2 2 2 2 2 2
2 2 4 4 4 4 4 4 4
3 2 4 5 5 5 5 5 5
4 2 4 8 8 8 8 8 8
5 2 4 8 9 9 9 9 9
6 2 4 8 10 10 10 10 10
7 2 4 8 12 12 12 12 12
8 2 4 8 16 16 16 16 16
9 2 4 8 16 17 17 17 17
10 2 4 8 16 18 18 18 18
11 2 4 8 16 19 19 19 19
12 2 4 8 16 21 21 21 21
13 2 4 8 16 23 23 23 23
14 2 4 8 16 25 25 25 25
15 2 4 8 16 27 27 27 27
16 2 4 8 16 32 32 32 32
 m\n 1 2 3 4 5 6 7 8

2 1 1 1 1 1 1 1 1
3 - 2 2 2 2 2 2 2
4 - 2 2 2 2 2 2 2
5 - - 3 3 3 3 3 3
6 - - 4 4 4 4 4 4
7 - - 4 4 4 4 4 4
8 - - 4 4 4 4 4 4
9 - - - 5 5 5 5 5
10 - - - 6 6 6 6 6
11 - - - 7 7 7 7 7
12 - - - 7 7 7 7 7
13 - - - 8 8 8 8 8
14 - - - 8 8 8 8 8
15 - - - 8 8 8 8 8
16 - - - 8 8 8 8 8

A clear pattern emerges: For any n ⩾ ⌈log2 a⌉ + 1, that is, for any non-trivial value
of n when a is ﬁxed, f (n, a) takes the same value as n increases. Similarly, for any

the electronic journal of combinatorics 23(3) (2016), #P3.23 7

n ⩾ ⌈log2 m⌉, that is, for any non-trivial value of n when m is ﬁxed, g(n, m) takes the
same value as n increases.
To the best of our knowledge, this has never been observed before. We formulate these
observations as conjectures.

Conjecture 13 (f -conjecture). Fix a ∈ N
+. Then f (n, a) = f (n + 1, a) for every n ∈ N+

such that n ⩾ ⌈log2 a⌉ + 1.

Conjecture 14 (g-conjecture). Fix m ∈ N
+. Then g(n, m) = g(n + 1, m) for every
n ∈ N+ such that n ⩾ ⌈log2 m⌉.

We checked these conjectures computationally up to n = 9 for all non-trivial values of
a for f (n, a) and up to n = 8 for all non-trivial values of m for g(n, m) (see Appendix).
We ﬁrst show that these two conjectures are equivalent.

Theorem 15. We have that f (n, a) = f (n + 1, a) for every a, n ∈ N
+ such that n ⩾
⌈log2 a⌉ + 1 if and only if g(n′, m) = g(n′ + 1, m) for every m, n
′ ∈ N+, m ⩾ 2 such that
n′ ⩾ ⌈log2 m⌉.

Proof. Suppose that g(n′, m) = g(n′ + 1, m) for every m, n
′ ∈ N+, m ⩾ 2 such that
n′ ⩾ ⌈log2 m⌉. Pick an arbitrary a ∈ N
+ and choose any n ∈ N
+ such that n ⩾ ⌈log2 a⌉ +
1. By Proposition 12(5), we know that there exists m such that g(n, m) = a, namely
m := f (n, a). Let m
∗ be the greatest number for which g(n, m
∗) = a. By deﬁnition,
it follows that f (n, a) ⩽ m
∗. Moreover, f (n, a) ⩾ m∗ since f (n, g(n, m
∗)) ⩾ m∗ by
Proposition 12(6). Thus, f (n, a) = m
∗ for any n ⩾ ⌈log2 a⌉ + 1.
Suppose that f (n, a) = f (n + 1, a) for every a, n ∈ N
+ such that n ⩾ ⌈log2 a⌉ + 1.
Pick an arbitrary m ⩾ 2, and choose any n
′ ⩾ ⌈log2 m⌉. If there exists a such that
f (n
′, a) = m, then, by Proposition 12(5), g(n′, m) = g(n′, f (n′, a)) = a. Therefore,
g(n
′, m) = g(n′ + 1, m) for all n
′ ⩾ ⌈log2 m⌉. If there does not exists a such that f (n
′, a) =
m, then, by Proposition 12(6), f (n′, g(n
′, m)) = m + b, b > 0, and g(n′, m) = g(n′, m + b).
Then g(n
′, m + b) =: a′ for all n′ since f (n′(g(n′, m + b)) = m + b, which brings us back
to the ﬁrst case. Therefore, g(n′, m) = g(n
′, m
′ + b) = a′ for all n
′ ⩾ ⌈log2 m⌉.

The two conjectures are thus equivalent: proving one would prove the other. Another
way to view the f -conjecture is as follows: to construct an optimal solution for f (n, a),
ﬁrst construct an optimal solution for f (⌈log2 a⌉ + 1, a), and make n − ⌈log2 a⌉ − 1 copies
of some element, i.e., put these new elements in the same sets as the original element,
or if you prefer, put these new elements in none of the sets. If the f -conjecture is true,
such families would be optimal for f (n, a). Note though that there can also be other
optimal families: the conjecture simply states that families obtained through this process
are optimal. The same idea can be applied to the g-conjecture.
Note that these conjectures are diﬀerent from the Frankl conjecture. For one thing,
even if the f - and g-conjectures hold, one would still need to show that f (⌈log2 a⌉+1, a) ⩽
2a for every a or that g(⌈log2 m⌉, m) ⩾ m
2 for all m to prove the Frankl conjecture;
therefore the f - and g-conjectures do not imply the Frankl conjecture. Moreover, the

the electronic journal of combinatorics 23(3) (2016), #P3.23 8

Frankl conjecture does not immediately imply the f - and g-conjectures. Certainly, if the
Frankl conjecture is true, then
 max
n f (n, a) ⩽ 2a

for all a ∈ N
+, else the Frankl conjecture would not be true; however, how the function
f (n, a) behaves for diﬀerent n for a ﬁxed a is irrelevant. Certainly, one can easily observe
that the Frankl conjecture implies that the function f has to stabilize at some point as
n increases since, by Proposition 12(1), f (n, a) ⩽ f (n + 1, a), and since f (n, a) ∈ N by
deﬁnition. However, the Frankl conjecture does not imply that the function f should be
stable immediately as n ⩾ ⌈log2 a⌉ + 1, that is, as soon as there are enough elements for
there to be at least a sets containing an element e. Similarly, if the Frankl conjecture is
true, then
 min
n⩾⌈log2 m⌉ g(n, m) ⩾ m
2

for all m ∈ N
+, and so again one can observe that the g function has to stabilize at
some point as n increases since we show in Proposition 12(2) that g(n, m) ⩾ g(n + 1, m).
But again, the Frankl conjecture does not imply that the function g has to stabilize
immediately when n ⩾ ⌈log2 m⌉, that is, as soon as there are enough elements for there
to be at least m sets in the power set of n.
Therefore, the f - and g-conjectures do not imply the Frankl conjecture and the latter
does not imply the former two either. Still, proving the f - and g-conjectures would have
wide-reaching implications for the Frankl conjecture.

2.3 Consequences of the f - and g-conjectures on the Frankl conjecture

Note that if the f - and g-conjectures are true, then proving the union-closed sets conjec-
ture for large families, i.e., families such that m ⩾ 2
n−1 +1 would be enough to prove it for
all families. Such a proof does not yet exist, however, combining the f - and g-conjectures
with Theorem 7 would already go a long way towards solving the Frankl conjecture.

Theorem 16. If the f - and g-conjectures hold, then Conjecture 11 holds for all m for
which there exists i ∈ N
+ such that 2
32
i ⩽ m ⩽ 2
i.

Proof. Let m be such that 2
32
i ⩽ m ⩽ 2
i for some i. If g(n, m) < m
2 for some n ⩾ ⌈log2 m⌉,
then we have a counterexample: a union-closed family on n elements and m sets where
every element is in less than half of the sets. By the g-conjecture, since i ⩾ ⌈log2 m⌉,
g(n, m) = g(i, m) < m
2 . However, by Theorem 7, g(i, m) ⩾ m
2 since m ⩾ 2
32
i. Thus, we
have obtained a contradiction and g(n, m) ⩾ m
2 for all n ⩾ ⌈log2 m⌉.

This would mean that Conjecture 11 would hold for about 2
3 of all possible values of
m. Recall that Conjecture 11 is equivalent to the Frankl conjecture, and so Theorem 16
could be reformulated in such terms.

the electronic journal of combinatorics 23(3) (2016), #P3.23 9

Another nice consequence of the f - and g-conjectures would be that there would ﬁnally
be a known constant fraction of sets containing e
∗(F), the most frequent element in F,
in any union-closed family F.

Theorem 17. If the f - and g-conjectures hold, then any union-closed family on m sets
contains an element in at least 6
13m sets of the family.

Proof. By Theorem 9, we know that g(⌈log2 m⌉, m) ⩾ 6
13m for any m ∈ N+. By the
g-conjecture, we know that g(n, m) ⩾ 6
13m for all n ⩾ ⌈log2 m⌉. Therefore, we know that
any family on m sets contains an element in at least 6
13m sets of the family.

Thus, from our point of view, studying the f - and g-conjectures oﬀers new ways of
attacking the Frankl conjecture, in addition to being interesting in and of itself. Hence,
the new conjectures warrant a closer examination.

3 Towards Proving the New Conjectures

3.1 Twin sets and a partial proof of the new conjectures

As noted before in Theorem 15, the f - and g-conjectures are equivalent, so from now on,
we will focus only on the f -conjecture. We now introduce a new idea: twin sets.

Deﬁnition 18. We call two sets S1, S2 with n > |S1| > |S2| twin sets if |S1△S2| = 1. We
call S1 the big twin and S2 the little twin. Moreover, we call the element e = S1△S2 the
twin diﬀerence of S1 and S2.

Twin sets play an important role in proving the f -conjecture as made clear by the
following lemma.

Lemma 19. Suppose that the f -conjecture is not true and that there exists values of n
and a with n ⩾ ⌈log2 a⌉ + 1 such that f (n, a) < f (n + 1, a). Then every optimal solution
of f (n + 1, a) is such that every element is a twin diﬀerence for at least one pair of sets.

Proof. Suppose that for f (n + 1, a) =: m there exists an optimal solution for which there
exists an element that is not a twin diﬀerence. Then removing this element (from every
set containing it) will leave all of the sets distinct, and the family will still be union-closed,
but with n elements. In that case, we know that f (n, a) ⩾ m = f (n + 1, a), and since
f (n, a) ⩽ f (n + 1, a) by Proposition 12(1), we obtain f (n, a) = f (n + 1, a) as in the
conjecture, a contradiction.

Therefore we only need to focus on the case where every optimal solution for some
f (n, a) is such that every element is a twin diﬀerence. Using Lemma 19 and an observation
from Falgas-Ravry [FR11], we can prove the f -conjecture for the cases when n > a.

Theorem 20. We have that f (n − 1, a) = f (n, a) for all n > a.

the electronic journal of combinatorics 23(3) (2016), #P3.23 10

Proof. First assume f (n − 1, a) < f (n, a) for some n > a. By Lemma 19, every element in
any optimal solution of f (n, a) is a twin diﬀerence of at least one pair of sets. This implies
that any optimal solution for n elements contains no two elements that are exactly in the
same sets. Indeed, such elements would not be twin diﬀerences. We can thus apply the
same construction as in [FR11]. Order the elements [n] by decreasing frequency. Observe
now that for all elements 1 ⩽ i < j ⩽ n, there exists Sij such that i ∈ Sij and j ̸∈ Sij.
For 2 ⩽ j ⩽ n, let Sj = ∪
j−1
i=1 Sij, and let Sn+1 = [n]. Note that the Sj’s are all distinct
since [1, j − 1] ⊆ Sj and j ̸∈ Sj. Since the most frequent element, element 1, is in at least
these n sets of the family, we have that a ⩾ n, which is a contradiction.

First note that the Falgas-Ravry construction can also be applied to the function g to
prove that g(n, m) = g(n + 1, m) for all n ⩾ m − 1. Furthermore, observe that having
no two elements in exactly the same sets is a much weaker constraint than having each
element being a twin diﬀerence. Therefore, it might be possible to improve this result.

3.2 Models with twins and some computations

Since we are interested in union-closed families in which every element is a twin diﬀerence,
we can modify the models from section 2.1 so that they only consider such families.
Additionally, we will not count the set with every element as a possible big twin (that
we will call trivial twin) as this case also yields that f (n + 1, a) = f (n, a). Indeed, if an
element e is the twin diﬀerence only of the trivial twin and [n]\{e}, then we can remove e
and replace the set [n]\{e} (now a set with all n − 1 elements identical to the trivial twin)
with the biggest set missing from the family (for example, the ﬁrst set missing in the
lexicographic order using any ordering of the elements). This new family is union-closed
by the same argument as in Proposition 12(3), and each element is still in at most a sets,
and so here again we have that f (n + 1, a) = f (n, a).
Enforcing that each element is a non-trivial twin diﬀerence for some pair of sets is
easily done in our f - and g-programs by introducing the variable ze
S for every S ∈ Sn
and e ∈ [n], which is zero if at least one of S and S ∪ e is absent from the family. This
of course makes the program much larger. Luckily, ze
S can be a continuous non-negative
variable. Indeed, by adding the constraints ze
S ⩽ xS and ze
S ⩽ xS∪e, we ensure that the
twin variable is zero if S or S ∪e is missing. We also add the constraint ∑ S̸∋e,
|S|̸=n−1 ze
S ⩾ 1 for

every e ∈ [n], which ensures each element is a non-trivial twin diﬀerence. We let ft(n, a)
and gt(n, m) be the optimal values of the programs for f (n, a) and g(n, m) with the new
variables and constraints. We present in Table 2 computational results for ft(n, a) and
gt(n, m).
From Theorem 20, we know that everything past the main diagonal for ft(n, a) is
infeasible. Similarly, everything past the lower diagonal for gt(n, m) is infeasible.
The fact that ft(n, a) decreases as n increases appears counterintuitive at ﬁrst, but
on second thought it makes sense. If there are more elements, each forced to be a twin
diﬀerence, then there will be more distinct unions of sets. Therefore the risk of violating
the a-limit increases, and so the number of allowable sets decreases. If one could prove

the electronic journal of combinatorics 23(3) (2016), #P3.23 11

Table 2: Non-trivial values of ft(n, a) and gt(n, m) (respectively left and right)
a\n 1 2 3 4 5 6 7 8
1 − − − − − − − −
2 − − − − − − −
3 − − − − − −
4 8 − − − − −
5 8 − − − −
6 10 9 − − −
7 12 11 10 − −
8 16 13 12 11 −
9 15 14 13 12
10 18 16 15 14
11 19 19 17 16
12 21 20 20 18
13 23 22 21 21
14 25 24 23 22
15 27 25 25 24
16 32 28 26 26
 m\n 1 2 3 4 5 6 7
1 − − − − − − −
2 − − − − − − −
3 − − − − − −
4 2 − − − − −
5 4 − − − −
6 4 5 − − −
7 4 5 6 − −
8 4 5 6 7 −
9 6 6 7 8
10 6 7 7 8
11 7 7 8 8
12 7 8 8 9
13 8 8 9 9
14 8 9 9 10
15 8 9 10 10
16 8 10 10 11

that, then the f -conjecture would be proven, and thus the g-conjecture as well. Another
idea pointing in a similar direction is the following.

Lemma 21. For a ﬁxed a, the minimum number of twin pairs for any element in an
optimal union-closed family for f (n, a) is bounded above by 2(a − n + 1). In particular,
this upper bound decreases as n increases.

Proof. Order the elements by decreasing frequency. Let tF be the minimum number of
twin pairs for any element in an optimal family F for f (n, a). If tF ⩾ 1, then, by the
Falgas-Ravry observation presented in Theorem 20, there exists a set Sj with [1, j−1] ⊆ Sj
and j ̸∈ Sj for every 2 ⩽ j ⩽ n, as well as the set Sn+1 = [n]. Note that, for element
1, these sets can only be big twins (since 1 is in all of these sets). Suppose u of these
sets are big twins for element 1. Then there exists at least tF − u other sets that are big
twins for element 1. Thus element 1 is in at least n + tF − u sets. Moreover, element 2
will be in at least u − 1 of the small twins for element 1, and it is in n − 1 sets among
the Sj’s (which are distinct from these small twins). Therefore, element 2 is in at least
n − 1 + u − 1 sets. Therefore, a ⩾ max{n + tF − u, n + u − 2} ⩾ n − 1 + tF
2 . This implies
that tF ⩽ 2(a − n + 1). Thus, for a ﬁxed a, as n increases, the potential number of twins
in an optimal family decreases.

Some of the properties in Proposition 12 for f and g also hold for ft and gt.

the electronic journal of combinatorics 23(3) (2016), #P3.23 12

Proposition 22. The following properties hold.

1. We have that ft(n, a) < ft(n, a + 1) if a < 2
n−1.

2. We have that gt(n, ft(n, a)) = a for all a and n.

3. We have that ft(n, gt(n, m)) ⩾ m for all m and n.

Proof.

1. Suppose ft(n, a) = m. Take a family F that is optimal. Then add to this family
one of the greatest set, i.e., a set containing as many elements as possible or lexico-
graphically greatest for some ordering of the elements, that is not already present
in the family. This is always possible since ft(n, a) < 2
n. This new family is still
union-closed, and moreover there are still twins for each element since we did not
remove any set. Each element is now in at most a + 1 sets, so this family is valid
for ft(n, a + 1), so ft(n, a + 1) ⩾ ft(n, a) + 1.

2. Suppose that ft(n, a) = m. This means the maximum number of sets in a union-
closed family such that every element is in at most a sets and such that each el-
ement is a non-trivial twin diﬀerence is m. Certainly, this means that gt(n, m) =
gt(n, ft(n, a)) ⩽ a since we’re minimizing and the previous family is valid here.
Suppose now that gt(n, ft(n, a)) = a′ < a. Then ft(n, a
′) ⩾ m. Since ft is strictly
increasing in a by (1), this is a contradiction.

3. Suppose that gt(n, m) = a. This means that there exists a family on m sets where
each element is a twin diﬀerence and is also present in at most a sets. Thus,
this family is valid for ft(n, a), and so ft(n, a) = ft(n, gt(n, m)) ⩾ m since we are
maximizing.

3.3 Number of twin pairs

Another direction worth investigating would be to prove that if f (n, a) < f (n + 1, a), then
every element is the diﬀerence of an increasingly large number of twins. At some point,
this ceases to be possible (trivially, an element cannot be the twin diﬀerence of more than
a twin pairs), and so we would reach a contradiction.

Theorem 23. If f (n, a) < f (n + 1, a), then every element in a f (n + 1, a)-optimal family
is the diﬀerence of at least two pairs of twin sets.

Proof. Suppose that f (n, a) = m and f (n + 1, a) = m + k for some k > 0. Then we
know that any optimal solution for f (n + 1, a) must be such that every element is a twin
diﬀerence, otherwise we could remove that element and get an m + k union-closed family
spanning n elements such that none is in more than a sets, and so f (n, a) ⩾ m + k, a
contradiction. Now let

k′ := min
e∈[n+1] |{S ∈ F|e ̸∈ S, e ∪ S ∈ F and F is an optimal family for f (n + 1, a)}|,

the electronic journal of combinatorics 23(3) (2016), #P3.23 13

i.e., k′ is the minimum number of twin pairs for which an element is a twin diﬀerence in
an optimal solution for fn+1(a).
We now show that k ⩽ k′. Suppose not. Let e′ and F ′ be an element and a family
such that e
′ is a twin diﬀerence for k′ twin pairs. Remove e
′ from F ′, and remove the k′

sets that are now duplicated. Call this new family F ′′. What remains is a union-closed
family of m + k − k′ sets on n elements. So m = f (n, a) ⩾ m + k − k′, which implies that
k ⩽ k′.
Now suppose that k = k′. Notice then that there must exist e
′′ such that e
′′ is contained
in a sets of F ′ that must still be contained in a sets of F ′′. If not, each element of the
new family F ′′ would be contained in at most a − 1 sets of F ′′, and so we would have that
f (n, a−1) ⩾ m+k−k′ = m, which is a contradiction on the fact that f (n, a−1) < f (n, a).
Thus if k = k′, then there exists e
′′ such that |{S ∈ F ′|S ∋ e
′′}| = a and such that e
′′

is never contained in a set of the family that does not contain e
′. Indeed, if there existed
S′ ∈ F ′ such that e
′ ̸∈ S′ and e′′ ∈ S′, then for any set S′′ ∈ F such that S′′ ∪ e
′ ∈ F as
well, i.e. twin sets with diﬀerence e
′, then one of S′ ∪ S′′ and S′ ∪ (S′′ ∪ e
′) will disappear
in F ′′ and so e
′′ would be present a − 1 times, a contradiction.
Thus {S ∈ F ′|S ∋ e′′} ⊆ {S ∈ F ′|S ∋ e
′} and since |{S ∈ F ′|S ∋ e
′′}| = a, then
|{S ∈ F ′|S ∋ e′}| = a as well and {S ∈ F ′|S ∋ e′′} = {S ∈ F ′|S ∋ e′} which is a
contradiction of the fact that e′ and e
′′ are twin diﬀerences for some sets. Since they are
copies of each other, we can remove either one of them without creating duplicate sets.
Thus, k < k′, and so if k′ = 1, then k ⩽ 0, and then f (n, a) ⩾ f (n + 1, a).

Note that this also means that if we remove any element from such a solution, and
remove a copy of every duplicated set created, what remains is never an optimal solution
for f (n, a).

4 Conclusion

As we have seen, a complete proof of the new conjectures has far-reaching implications:
the Frankl conjecture would hold for about 2
3 of all possible cases, and we could show
that there always exists an element in 6
13 of the sets of a union-closed family. Therefore
we believe our new conjectures merit additional attention. In order to encourage further
progress in this direction, we conclude with a few open problems of interest.

1. Show that f (n, a) = f (n + 1, a) for smaller values of n, i.e., for values of n < a.

2. Show that if f (n, a) < f (n + 1, a), each element is a twin diﬀerence for even more
sets. As noted, at some point, this clearly implies that the solutions is not optimal
or even feasible.

3. Find a constant upper bound for ft(n + 1, a) − ft(n, a). Since we know f (n, a) stops
growing after n = a, this would provide a ﬁrst constant lower bound for the number
of sets containing the most frequent element in a union-closed family.

the electronic journal of combinatorics 23(3) (2016), #P3.23 14

Acknowledgements

The authors wish to thank the two anonymous referees for their helpful comments.

5 Appendix

In the following tables for f (n, a) and g(n, m), we remove unnecessary columns, i.e. the
columns for which the values of f (n, a) and g(n, m) are trivial.

Table 3: Values of f (n, a)

a\n 1 2 3 4 5 6 7 8 9
1 2 2 2 2 2 2 2 2 2
2 4 4 4 4 4 4 4 4
3 5 5 5 5 5 5 5
4 8 8 8 8 8 8 8
5 9 9 9 9 9 9
6 10 10 10 10 10 10
7 12 12 12 12 12 12
8 16 16 16 16 16 16
9 17 17 17 17 17
10 18 18 18 18 18
11 19 19 19 19 19
12 21 21 21 21 21
13 23 23 23 23 23
14 25 25 25 25 25
15 27 27 27 27 27
16 32 32 32 32 32
17 33 33 33 33
18 34 34 34 34
19 35 35 35 35
20 36 36 36 36
21 38 38 38 38
22 40 40 40 40
23 41 41 41 41
24 43 42 42 42
25 45 45 45 45
26 47 47 47 47
27 49 49 49 49
28 52 52 52 52
29 53 53 53 53
30 56 56 56 56
31 58 58 58 58
32 64 64 64 64
 a\n 7 8 9
33 65 65 65
34 66 66 66
35 67 67 67
36 68 68 68
37 69 69 69
38 71 71 71
39 72 72 72
40 74 74 74
41 75 75 75
42 77 77 77
43 79 79 79
44 80 80 80
45 82 82 82
46 83 83 83
47 85 85 85
48 88 88 88
49 89 89 89
50 91 91 91
51 93 93 93
52 95 95 95
53 98 98 98
54 99 99 99
55 101 101 101
56 104 104 104
57 105 105 105
58 108 108 108
59 110 110 110
60 113 113 113
61 115 115 115
62 118 118 118
63 121 121 121
64 128 128 128
 a\n 8 9
65 129 129
66 130 130
67 131 131
68 132 132
69 133 133
70 134 134
71 136 136
72 137 137
73 139 139
74 140 140
75 142 142
76 144 144
77 145 145
78 146 146
79 147 147
80 149 149
81 150 150
82 152 152
83 154 154
84 156 156
85 157 157
86 158 158
87 160 160
88 162 162
89 164 164
90 166 166
91 168 168
92 170 170
93 171 171
94 173 173
95 175 175
96 176 176
 a\n 8 9
97 179 179
98 180 180
99 182 182
100 184 184
101 186 186
102 188 188
103 189 189
104 192 192
105 194 194
106 196 196
107 198 198
108 200 200
109 202 202
110 204 204
111 206 206
112 209 209
113 211 211
114 214 214
115 216 216
116 220 220
117 221 221
118 224 224
119 226 226
120 229 229
121 231 231
122 233 233
123 236 236
124 240 240
125 242 242
126 245 245
127 248 248
128 256 256

the electronic journal of combinatorics 23(3) (2016), #P3.23 15

Table 4: Values of g(n, m)

m\n 1 2 3 4 5 6 7 8

2 1 1 1 1 1 1 1 1
3 2 2 2 2 2 2 2
4 2 2 2 2 2 2 2
5 3 3 3 3 3 3
6 4 4 4 4 4 4
7 4 4 4 4 4 4
8 4 4 4 4 4 4
9 5 5 5 5 5
10 6 6 6 6 6
11 7 7 7 7 7
12 7 7 7 7 7
13 8 8 8 8 8
14 8 8 8 8 8
15 8 8 8 8 8
16 8 8 8 8 8
17 9 9 9 9
18 10 10 10 10
19 11 11 11 11
20 12 12 12 12
21 12 12 12 12
22 13 13 13 13
23 13 13 13 13
24 14 14 14 14
25 14 14 14 14
26 15 15 15 15
27 15 15 15 15
28 16 16 16 16
29 16 16 16 16
30 16 16 16 16
31 16 16 16 16
32 16 16 16 16
 m\n 6 7 8
33 17 17 17
34 18 18 18
35 19 19 19
36 20 20 20
37 21 21 21
38 21 21 21
39 22 22 22
40 22 22 22
41 23 23 23
42 24 24 24
43 24 24 24
44 25 25 25
45 25 25 25
46 26 26 26
47 26 26 26
48 27 27 27
49 27 27 27
50 28 28 28
51 28 28 28
52 28 28 28
53 29 29 29
54 30 30 30
55 30 30 30
56 30 30 30
57 31 31 31
58 31 31 31
59 32 32 32
60 32 32 32
61 32 32 32
62 32 32 32
63 32 32 32
64 32 32 32
 m\n 7 8
65 33 33
66 34 34
67 35 35
68 36 36
69 37 37
70 38 38
71 38 38
72 39 39
73 40 40
74 40 40
75 41 41
76 42 42
77 42 42
78 43 43
79 43 43
80 44 44
81 45 45
82 45 45
83 46 46
84 47 47
85 47 47
86 48 48
87 48 48
88 48 48
89 49 49
90 50 50
91 50 50
92 51 51
93 51 51
94 52 52
95 52 52
96 53 53
 m\n 7 8
97 53 53
98 53 53
99 54 54
100 55 55
101 55 55
102 56 56
103 56 56
104 56 56
105 57 57
106 58 58
107 58 58
108 58 58
109 59 59
110 59 59
111 60 60
112 60 60
113 60 60
114 61 61
115 61 61
116 62 62
117 62 62
118 62 62
119 63 63
120 63 63
121 63 63
122 64 64
123 64 64
124 64 64
125 64 64
126 64 64
127 64 64
128 64 64

References

[Abe00] T. Abe. Strong semimodular lattices and Frankl’s conjecture. Algebra
Universalis, 44:379–382, 2000.

[AN98] T. Abe and B. Nakano. Frankl’s conjecture is true for modular lattices.
Graphs and Combinatorics, 14:305–311, 1998.

[AN00] T. Abe and B. Nakano. Lower semimodular types of lattices: Frankl’s
conjecture holds for lower quasi-semimodular lattices. Graphs and Combi-
natorics, 16:1–16, 2000.

[Bal11] I. Balla. Minimum densities of union-closed families. arXiv:1106.0369,
e-print, 2011.

the electronic journal of combinatorics 23(3) (2016), #P3.23 16

[BBE13] I. Balla, B. Bollob´as, and T. Eccles. Union-closed families of sets. Journal
of Combinatorial Theory (Series A), 120(3):531–544, 2013.

[BCST13] H. Bruhn, P. Charbit, O. Schaudt, and J. A. Telle. The graph formulation
of the union-closed sets conjecture. arXiv:1212.4175, to appear in European
Journal of Combinatorics.

[BM08] I. Boˇsnjak and P. Markovi´c. The 11-element case of Frankl’s conjecture.
The Electronic Journal of Combinatorics, 15(1):R88, 2008.

[BS12] H. Bruhn and O. Schaudt. The union-closed sets conjecture almost holds
for almost all random bipartite graphs. arXiv:1302.7141, to appear in
European Journal of Combinatorics.

[BS14] H. Bruhn and O. Schaudt. The journey of the union-closed sets conjecture.
arXiv:1309.3297, preprint, 2014.

[CMS09] G. Czedli, M. Mar´oti, and E.T. Schmidt. On the scope of averaging for
Frankl’s conjecture. Order, 26:31–48, 2009.

[Cze09] G. Czedli. On averaging Frankl’s conjecture for large union-closed sets.
Journal of Combinatorial Theory (Series A), 116(3):724–729, 2009.

[Doh01] K. Dohmen. A new perspective on the union-closed sets conjecture. Ars
Combinatorica, 58:183–185, 2001.

[Ecc15] T. Eccles. A stability result for the union-closed size problem. Combina-
torics, Probability and Computing, 25:399–418, 2015.

[EZ97] M. El-Zahar. A graph-theoretic version of the union-closed sets conjecture.
Journal of Graph Theory, 26:155–163, 1997.

[Far94a] G. L. Faro. A note on the union-closed conjecture. Journal of the Australian
Mathematical Society (Series A), 57:230–236, 1994.

[Far94b] G. L. Faro. Union-closed sets conjecture: improved bounds. Journal
of Combinatorial Mathematics and Combinatorial Computing, 16:97–102,
1994.

[FR11] V. Falgas-Ravry. Minimal weight in union-closed families. Electronic Jour-
nal of Combinatorics, 18(1):P95, 2011.

[Fra83] P. Frankl. On the trace of ﬁnite sets. Journal of Combinatorial Theory
(Series A), 34:41–45, 1983.

[GY98] W. Gao and H. Yu. Note on the union-closed sets conjecture. Ars Combi-
natorica, 49:280–288, 1998.

[JV99] R.T. Johnson and T.P. Vaughan. On union-closed families. Journal of
Combinatorial Theory (Series A), 85:112–119, 1999.

[Kni94] E. Knill. Graph generated union-closed families of sets. E-print,
arXiv:math/9409215, 1994.

the electronic journal of combinatorics 23(3) (2016), #P3.23 17

[LMBRCS08] B. Llano, J.J. Montellano-Ballesteros, E. Rivera-Campo, and R. Strausz.
On conjectures of Frankl and El-Zahar. Journal of Graph Theory, 57:344–
352, 2008.

[LRS12] U. Leck, I.T. Roberts, and J. Simpson. Minimizing the weight of the
union-closure of families of two-sets. Australasian Journal of Combina-
torics, 52:67–73, 2012.

[MVZ12] F. Mari´c, B. Vuˇckovi´c, and M. ˇZivkovi´c. Formalizing Frankl’s conjecture:
F C-families. In Johan Jeuring, JohnA. Campbell, Jacques Carette, Gabriel
Reis, Petr Sojka, Makarius Wenzel, and Volker Sorge, editors, Intelligent
Computer Mathematics, volume 7362 of Lecture Notes in Computer Sci-
ence, pages 248–263. Springer Berlin Heidelberg, 2012.

[Mor06] R. Morris. FC-families, and improved bounds for Frankl’s conjecture. Eu-
ropean Journal of Combinatorics, 27:269–282, 2006.

[NS93] R.M. Norton and D.G. Sarvate. A note on the union-closed sets conjecture.
Journal of Australian Mathematical Society (Series A), 55:411–413, 1993.

[Poo92] B. Poonen. Union-closed families. Journal of Combinatorial Theory (Series
A), 59(1):253–268, 1992.

[Rei00] J. Reinhold. Frankl’s conjecture is true for lower semimodular lattices.
Graphs and Combinatorics, 16:115–116, 2000.

[Rei03] D. Reimer. An average set size theorem. Combinatorics, probability and
computing, 12(1):89–93, 2003.

[Ren91] J.-C. Renaud. Is the union-closed sets conjecture the best possible? Journal
of the Australian Mathematical Society (Series A), 51:276–283, 1991.

[Ren95] J.-C. Renaud. A second approximation to the boundary function on union-
closed collections. Ars Combinatorica, 41:177–188, 1995.

[RF93] J.-C. Renaud and L.F. Fitina. On union-closed sets and Conway’s sequence.
Bulleting of the Australian Mathematical Society, 47:321–332, 1993.

[Rob92] I. Roberts. The union-closed conjecture. Technical Report 2/92, Curtin
University of Technology, 1992.

[RS10] I. Roberts and J. Simpson. A note on the union-closed families of ﬁnite
sets. Australasian Journal of Combinatorics, 47:129–145, 2010.

[SR89] D.G. Sarvate and J.-C. Renaud. On the union-closed sets conjecture. Ars
Combinatoria, 27:149–154, 1989.

[SR90] D.G. Sarvate and J.-C. Renaud. Improved bounds for the union-closed sets
conjecture. Ars Combinatoria, 29:181–185, 1990.

[Vau02] T.P. Vaughan. Families implying the Frankl conjecture. European Journal
of Combinatorics, 23:851–860, 2002.

[Vau04] T.P. Vaughan. Three-sets in a union-closed family. Journal of Combinato-
rial Mathematics and Combinatorial Computing, 49:73–84, 2004.

the electronic journal of combinatorics 23(3) (2016), #P3.23 18

[VZ12] B. Vuˇckovi´c and M. ˇZivkovi´c. The 12 element case of Frankl’s conjecture.
Preprint, 2012.

[W´oj92] P. W´ojcik. Density of union-closed families. Discrete Mathematics, 105:259–
267, 1992.

[W´oj99] P. W´ojcik. Union-closed families of sets. Discrete Mathematics, 199:173–
182, 1999.

the electronic journal of combinatorics 23(3) (2016), #P3.23 19
