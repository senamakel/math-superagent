<!-- source: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S144618110000300X | converted from PDF -->

ANZIAMJ. 48(2006), 151-164

COMPUTER SOLUTION TO THE 17-POINT
ERDOS-SZEKERES PROBLEM

GEORGE SZEKERES
1 and LINDSAY PETERS3 2

In memory of Paul Erdos

(Received 25 April, 2006; revised 15 October, 2006)

Abstract

We describe a computer proof of the 17-point version of a conjecture originally made by
Klein-Szekeres in 1932 (now commonly known as the "Happy End Problem") that a planar
configuration of 17 points, no 3 points collinear, always contains a convex 6-subset. The
proof makes use of a combinatorial model of planar configurations, expressed in terms
of signature functions satisfying certain simple necessary conditions. The proof is more
general than the original conjecture as the signature functions examined represent a larger
set of configurations than those which are realisable. Three independent implementations of
the computer proof have been developed, establishing that the result is readily reproducible.

2000 Mathematics subject classification: primary 52C10.
Keywords and phrases: Erdos-Szekeres problem, Ramsey theory, convex polygons and
polyhedra, generalized convexity.
 1. Introduction

One of the early interests of Paul Erdos, one that had a strong influence on his later
work in combinatorial geometry and Ramsey theory, was the following problem of
Esther Klein-Szekeres: Is it true that for k > 1

(Pk) Every planar set of n > 2*~
2 points (in general position, no 3 points collinear)
contains a subset of k points which form a convex ifc-gon (denoted a convex
k-subsei).

'(deceased), School of Mathematics, University of NSW, Sydney NSW 2052, Australia.
2Pacific Knowledge Systems, Australian Technology Park, Eveleigh NSW 1430, Australia;
e-mail: l.peters@pks.com.au.
© Australian Mathematical Society 2006, Serial-fee code 1446-1811/06

151

https://doi.org/10.1017/S144618110000300X Published online by Cambridge University Press

152 George Szekeres and Lindsay Peters [2]

(Qk) There exists a planar configuration of 2
k~
2 points which contains no convex
^-subset.

For k = 2, 3 and 4 both statements are trivially true (for k = 4 by a simple argument
by the proposer herself) but already k = 5 presents difficulties. When the problem
was posed (in 1932) it was not even clear that for any k > 4 there exists an n = n{k)
such that a set of n points in the plane always contains a convex subset of k points,
but the question was soon settled in the affirmative by Erdos and Szekeres [3].
Nowadays the proof of existence of  such an n presents no difficulties and is a simple
exercise in Ramsey theory. The following argument is from van Lint and Wilson, [9,
page 26]. Number the points of the configuration from 1 to n in an arbitrary manner,
and provide each triangle abc, a < b < c, with a signature + or —  according to the
(anticlockwise or clockwise) orientation of the abc. It is easily seen that a non-convex
quadrilateral always contains triangles of both kinds. On the other hand by Ramsey,
if n is sufficiently large, the configuration contains a ^-subset K with all its triangles
having the same signature. Hence all quadrilaterals of K are convex and therefore K
itself is convex. If n o(k) + 1 denotes the smallest n such that any planar configuration
of size n contains a convex ^-subset, the conjectures (P k) and {Qk) together assert that
no(k) =  2
k~
2.
At the time when the conjectures (P k) and (Qk) were proposed they seemed to be
a hazardous extrapolation from a few trivial and not very convincing cases, but a few
years later Makai and Turan verified that indeed 9 points always contain a convex
pentagon. As far as we know this proof has never appeared in print but some of us
who knew of its existence saw in it modest support for the belief that (P k) is true for
all k. (See Morris and Soltan [7], Kalbfleisch etal. [5] and Bonnice [1] for proofs for
9 points.) Many years later Erdos and Szekeres [4] produced an explicit example of
2
k~
2 points which contained no convex  k-gon, thereby confirming the truth of (Qk) for
all k > 1. This construction showed at any rate that no(k) > 2
k~
2. For recent results
on the upper bound for no(k) see Toth and Valtr [8].
The main result of the present paper is a computer proof of no(6) = 16, that is, 17
points in the plane always contain a convex 6-subset, further strengthening the general
validity of (P k).
 2. Combinatorial convexity

To carry out the computer proof of no(6) = 16 we shall need a combinatorial de-
scription of n-point configurations in the plane and a suitable combinatorial definition
of convexity. Neither of these is unique and  a judicious selection is vital for the suc-
cess of the quite formidable computer search. As in Section 1, we shall make use of
signatures of triangles, but the numbering of points upon which the signatures depend

https://doi.org/10.1017/S144618110000300X Published online by Cambridge University Press

[3] Computer solution to the 17-point Erdos-Szekeres problem 153

will not be arbitrary but restricted to specific choices for a given configuration. In fact
the conceptual freedom afforded by an arbitrary numbering offers no advantages for
the demands of computerisation.
Let F n be the set of configurations P = {p\,..., p n] of n points in the (x, y)
coordinate plane. By rotating any given configuration we can assume that the x axis
is neither perpendicular nor parallel to any of the Q) edges of the configuration and
so the points /?, will have different x coordinates. Indeed, we assume that the points

p, are ordered in terms of increasing *-coordinate. Assuming that no three points are
on a line, every ordered triple (/?,, p}, pk),l < i < j < k < n, is then oriented either
clockwise or anticlockwise, imparting a signature a(i, j , k) = — or + to the triples
according to their orientation.
More formally let Tn be the set of ordered triples (i, j , k) of Sn = [1,2,... ,n]
and En the set of signature functions

on Tn. Then every P e F n induces a signature function a e En (strictly speaking an
equivalence class of such functions, depending on the x direction) and we regard P
as a geometrical realisation of this a.
To define a convex it-gon we make use of "cups" and "caps" as defined by Chung
and Graham [2]. After some experimentation we found them to be the most effective
for the computer search ahead. An ordered set

Q, i = [aQ, au ..., a,] , 1 < a0 < a x < ••• < a , <n, t- = + o r - ,

will be called a £ -chain of length i > 1 if CT(OM_2, aM_i,aM) = £ for all 2 < ix < /. In
particular, [a0, a\\ is a £ -chain of length 1 for both £ = 4- and —. Here C+,, represents
what Chung and Graham call an (i + l)-cup and C_,, an (i + l)-cap; we shall use
either of these names, whichever is more convenient.

DEFINITION. A ^-subset is called convex relative to o if it is the union of a cup-cap
pair with common endpoints, that is, C+,, (J C-j, C+,, = [a0, alt..., a,], C_j =
[bo,b\,...,bj] with total length i + j = k, a = a 0 = b 0, a,- = bj = b, and

We will adopt this definition of convexity for a, whether or not a is induced by
some P e F n. Note that only triples formed by consecutive members of the chain were
required to have the same signature, but if a is induced by a geometric configuration
then of course all ordered triples of the chain have the same signature. We have chosen
a weakest possible condition for £-chains so that they should represent Chung-Graham
cups and caps whenever a is induced by some P G F n, where the points are ordered in
terms of increasing x-coordinate. We can then ask whether the combinatorial version
of (P k) is valid for arbitrary a, that is,

https://doi.org/10.1017/S144618110000300X Published online by Cambridge University Press

154 George Szekeres and Lindsay Peters [4]

{,Pa,k) If « > 2*~
2 then relative to any o e £„ there is a convex ^-subset of Sn.
As before, the existence of such an n  is established by the Ramsey argument of  van
Lint and Wilson. The conjecture (P a,k) is considerably stronger than (Pk) since only
a small fraction of signature functions have a geometrical realisation. If o is induced
by some P  €  Fn and abed, 1 < a  <b<c<d<n, is  a convex quadrilateral then
writing
 0\ = 0(a,  b, c), 02=o(a,b,d),

0 3 =  0(a,c,d),  04 =  0(b,c,d),

we must have
 0\ =  02, 03 =  04- (2-1)

Similarly if abed is a concave quadrilateral, that is, a triangle abd with c inside the
triangle, or a triangle acd with b inside it, then we must have

O\ =  -0 4, CT 2 =  CT 3. (2.2 )

These are easily verified by examining all possible 4-point configurations in the plane.
Consequently the realisable signature functions are restricted to one of the (mutually
exclusive) conditions (2.1) and (2.2) which must then be satisfied by all 4-subsets of S n.
This gives 8 possibilities (out of 16) for the signature values of any quadrilateral:

0\ 02 03 04

$ %  %  -%  (2.3)

where £ =  + or —.  We denote by E* the subset of those  o 6  £„ which satisfy one of
the geometric constraints (2.1) or (2.2) for all 4-subsets of Sn.
Of course if  (Pa,k) is true for all 0 e S n then it is also true for those special 0
for which all 4-subsets of Sn belong to the 8 classes listed in (2.3). Therefore (/*„,*)
implies the much weaker conjecture

(P*k) Ifn > 2
k~
2 then relative to any given 0 e E* there exists a convex fc-subset.

Of course (Pk) is an immediate consequence of (P*k) and it is natural to ask
whether the two are actually equivalent. In other words, are the conditions (2.3) not
only necessary but sufficient for 0 to be induced by some P  e F nl The answer is
no, and Knuth ([6, Figure 1, page 26]) shows an example of a 9-point non-realisable
configuration satisfying (2.3). Hence (P*k) remains a stronger conjecture than (Pk).

https://doi.org/10.1017/S144618110000300X Published online by Cambridge University Press

[5] Computer solution to the 17-point Erdos-Szekeres problem 155

At first sight, it looks fairly unlikely that (P a,k) should be true. Yet (P aA) is true
for all a € E5, that is, 55 always contains a convex 4-subset. For suppose that all
4-subsets of S 5 are non-convex. Then assuming cr(l, 2, 3) = + , each of the following
implications follows from the preceding one:

(123)+ -> (235)- -* (245)- -> (124)
+ -> (134)+ - • (345)" - * (234)
+ -> (123)",

where we have used the simplified notation  (ijk)* to denote o{i, j , k) = £.
For example, if (235)+ then [1, 2, 3, 5] is a 4-cup and the 4-subset 1235 is convex,
contrary to assumption. Similarly in the second step if (245)+ then [2, 3, 5] and
[2, 4, 5] are a 3-cup and 3-cap respectively and so the 4-subset 2345 is convex, again
contrary to assumption. The other steps are variants of the first two. We end up
with (123)~, contradicting the original assumption. It follows that S5 must contain a
convex 4-subset.
This demonstration has the merit of being purely combinatorial (no reference to
geometrical constraints), and it paves the way for a computer proof of (Pa,s) in
Section 3 and (P*6) in Section 4. In particular, (Pa,s) is true, a much stronger result
than that of Makai and Turan. Its main interest is that, perhaps against expectations,
(Pa,k) is true in the first non-trivial case k = 5.
The proof of (P* 6) was much more time consuming than that of (P ff,5), hardly
surprising since it implies the validity of (P 6), that is, the 17-point conjecture. It
would be of great interest to also verify (P^), but at present this seems to be out of
reach.
The algorithm described in Sections 3 and 4 has been implemented independently
by each of the authors, and more recently, also by B. McKay.

3. Computer proof of (Pff,s)

THEOREM 1. For every a e E 9 there is a convex 5-subset ofSg.

Take an arbitrary a e E9 over S9 = (1, 2, ... , 9}. Every such a is represented as
a state of an array Am = {a\,... ,am] of triples, of size m — Q = 84, and where
each element a, takes the value + or —. That is, if i corresponds to the triple abc,
then a, = a{a, b, c). Here Am is introduced simply as a computational convenience,
and in particular, during the search we will incrementally assign elements of Am. A
partially assigned Am therefore represents a subset of E9.
The ordering of the elements of Am is not important, and so we choose

ax = a(l , 2, 3), a 2 = a(l , 2, 4), a 3 = a(l , 3, 4), ..., a M = a(J, 8, 9). (3.1)

As there are 2
m possible states of the array, a simple exhaustive search is of course
not feasible and it is necessary to organise the search more efficiently. Whilst the

https://doi.org/10.1017/S144618110000300X Published online by Cambridge University Press

156 George Szekeres and Lindsay Peters [6]

following algorithm is not the simplest that can be used for the n = 9 case, it is
described here as it is able to be extended to deal with the n = 17 case.
Let abcde be any (ordered) set of five points of S 9. It forms a convex 5-subset if and
only if its Q = 10 triples satisfy one of the four relations (termed convex relations):

Ri : a(abc)  =  o{bed) =  a(cde), R2 : a(abc)  =  o(bee) =  —a(ade),

R3 : a(abd)  =  a(bde) =  —a(ace), R4 (d) (d) {b)

Signatures that do not satisfy any of the relations (3.2) are termed concave.
The total number of convex relations on S9 is therefore 4 x Q = 504. The
hypothesis that for any 9 points there is at least one convex 5-subset is therefore
equivalent to the hypothesis that every (fully-assigned) state of the 84-element array
Am must satisfy at least one of these 504 relations.
Consider now E 5 which is the set of signature functions on 5 points only. An
arbitrary a e S5 is represented as a state of Q = 10 elements, hence there are 2
10

possible signature functions in S 5. A straightforward calculation will verify that 700
of these are convex. Denoting £2 c E 5 as the subset of concave signature functions
of E 5, we therefore have \Q\ = 1024 - 700 = 324.
Denote the signature functions in Q by {co\,..., coi24}, where for fixed i, the 10
triples representing co, (in the same order as in (3.1)) are denoted {o>(1, ... , coii0}. The
ordering of the concave signature functions themselves is not important.
The hypothesis that every state of Am satisfies at least one of the 504 convex
relations is therefore equivalent to the hypothesis that no state of Am can consist of
signature functions wholly assigned from Q. for every 5-subset in S9.
Let Us = [u\, u 2, «3, u4, u5] denote the collection of contiguous 5-subsets in S 9:

M, =[1,2 , 3, 4, 5], u2 = [2, 3, 4, 5, 6], ... , u5 = [5, 6, 7, 8, 9]. (3.3)

We say that a signature function (or more simply, a signature) in £2 is assigned to a
5-subset in U5 if it is assigned to the elements of Am corresponding to that 5-subset.
That is, the restriction of a to u; is a translation of that signature. We note that
if a signature in £1 is assigned to some uj, 1 < j < 4, then the possible choices
for assignment to uJ+i  are reduced as uj and uj+i share the 4 points [j + 1, j + 2,
7+3,7+4 } and so share Q = 4 triples. Hence for each co, e £2 we define its
compatible subset as the set of signatures &>/ € ft such that

W;i = &>,4, con = co n, con =  co,9, COM =  coi10- (3.4)

A simple computer search verifies that each compatible subset contains no more
than 27 signatures.
In brief, the algorithm performs an exhaustive search by successively assigning the
signatures in Q to the triples corresponding to the Uj under the assumption that the

https://doi.org/10.1017/S144618110000300X Published online by Cambridge University Press

[7] Computer solution to the 17-point Erdos-Szekeres problem 157

hypothesis is false. That is, we assume that each state of Am is able to be assigned
from signatures in Q, and show this leads to a contradiction in every case.
The algorithm relies on two key observations:

(1) The ordering of 5-subsets in (3.3) ensures that for a given signature, its compat-
ible subset does not depend on j , that is, on whether that signature has been assigned
to Mi, M2. «3 or «4- Hence the compatible subsets for each signature in Q need only be
calculated once, prior to the search itself.
(2) A partially assigned state of Am can force further assignments, thereby eliminat-
ing large numbers of possible configurations from the search.

To illustrate the second observation, consider some partially assigned state of Am,
that is, not all elements are assigned + or —.  We assume that the partially assigned
state does not yet satisfy any of the convex relations, that is, if all three elements
of Am corresponding to some convex relation in (3.2) are assigned, then that relation
is not satisfied. We now note that assigning one more element of Am may necessarily
determine the values of some other elements due to the assumption that none of the
convex relations (3.2) are satisfied. For example, if o(abc) = a (bed) = + then
o(cde) must necessarily take the value —  to avoid the first relation in (3.2). These
other assigned elements may, in turn, determine the values of further elements, and so
on recursively.
In this way, the assignment of a signature from £2 to the elements of Am corre-
sponding to some uj may cause further elements of Am to be necessarily assigned,
further restricting the choices of compatible signatures to um for m > j , and hence
reducing the number of subsequent configurations required to be examined.
Furthermore, an element of Am necessarily assigned by considering one convex
relation may cause some other convex relation to be satisfied, eliminating from the
search all configurations represented by this partial assignment to Am.
In this way, contradictions are generated with relatively few assignments needing
to be made from Q. In fact, the computer search indicates that the only 5-subsets that
ever need to be assigned are (in order) u\,u2, and M3 (the forced assignments involve
points 8 and 9).
The details of the algorithm are now described. It will terminate when a fully
assigned state is found with no contradiction, or alternatively, when all possible
configurations have led to a contradiction.

ALGORITHM  1. Step 1. Suppose we have a partial assignment of Am obtained
by an assignment to uu ..., uj for some j < 5 by elements of Q. (Initially we
simply assign the first element of Q to u t for some fixed ordering of elements of fi).
Check convex relations (3.2) to see if a contradiction has been reached or if o(ijk)
for some unassigned triple (i, j , k) is forced to avoid satisfying one of the convex
relations. Repeat this step (that is, re-checking all the convex relations when a new

https://doi.org/10.1017/S144618110000300X Published online by Cambridge University Press

158 George Szekeres and Lindsay Peters [8]

element is necessarily assigned) until no more elements are necessarily assigned, or a
contradiction is reached.
Step 2. If there is no contradiction found in the previous step, we have shown that
the current assignments to uu ..., Uj do not cause any of the convex relations to be
satisfied. Check whether Am is now completely assigned. If it  is, we have found a state
where no convex relation is satisfied, and the search terminates with a counterexample
found to Theorem 1. If it isn't completely assigned, move to the next configuration to
be checked as follows. If  co is currently assigned to Uj, assign the first possible element
of the compatible subset for co to uj+1 and go to Step 1. We note that there could be
triples in uj+{ that have ah-eady been necessarily assigned, restricting the choices from
the compatible subset for co as mentioned above. If there are no remaining choices
for assignments to uj+l, we have derived a contradiction by the current assignments
to«i,...,« j and so we go to Step 3.
Step 3. If there was a contradiction found in Steps 1 or 2 we have shown that
irrespective of the possible assignments of the remaining unassigned elements of Am,
the current assignments touu ..., uj will necessarily cause one of the convex relations
to be satisfied. Move to the next configuration to be checked as follows:
Step 4. Restore the state of  Am to what it was prior to u s having its current assignment.
Assign the next possible element to uj, that is, the next possible element of the
compatible subset of the element assigned to w ;_i if j > 1, or the next element of Q
if j = 1, and go to Step 1. If there are no remaining choices for assignments to Uj
we have derived a contradiction by the current assignments to Ui, ..., w;_i and so if
j > 1 we decrement j and repeat this step. If j = 1 and there are no remaining
choices from fi to u\ the search terminates with all possible states having led to a
contradiction.

Some notes on efficiency

• In Step 1, when some new element  is assigned, only the convex relations involving
the new element need to be checked, and not the complete list of  504 relations. Hence
for each element a{ of Am, the set of relations involving at are stored prior to the
commencement of the search.
• We can take advantage of the linearity of the convex relations by only assigning
half of the possible elements of  £1 to u\, for example, those elements for which  a.\ = +.

Using a 1.5 GHz workstation, the search terminates at Step 4 in less than one
second, establishing Theorem 1.

4. Computer proof of (P*  6)

THEOREM 2.  For every a e S*7 there is a convex 6-subset ofSn.

https://doi.org/10.1017/S144618110000300X Published online by Cambridge University Press

[9] Computer solution to the 17-point Erdos-Szekeres problem 159

The description of the 17-point proof will focus on the required extensions to the
proof given above for the 9-point case. Unless indicated otherwise, the various entities
(Am, ft and so on) will be denoted by the same symbols as their 9-point counterparts.
The number of elements m in Am required to represent a signature in En over 517
is now ('3
7) = 680. Let abcdef be any (ordered) set of six points of 5 n . They form
a convex 6-subset if and only if its (*) = 20 triples satisfy one of the eight convex
relations:
 Rx : a(abc) = a (bed) = o(cde) = a(def),
R2 : o(abc) = a(bcd) = o(cdf) = -a(aef),
/?3 : o(abc) = a  (bee) = a(cef) = —a(adf),
R4 : a(abd) = a(bde) = o(def) = -a(acf),
R5 : o(acd) = a(cde) = a(def) = -o(abf),
R6 : o(abc) = a(bcf) = -o(ade) = -o(def),
R7 : a(abd) = a(bdf) = -a (ace) = -a(cef),
/?8 : a(acd) = a(cdf) = -o(abe) = -o(bef).

The total number of convex relations on Sn is therefore 8 x ('6
7) = 99,008. A
straightforward calculation verifies that |ft| = 184, 556 where ft is now the set of
concave signatures on S6.
Let Ui2 = {wi, M2, ... , M12}  denote the contiguous 6-subsets in 5 n :

K, = [1, 2,... , 6], «2 = [2, 3,... , 7], ... , M,2 = [12, 13,... , 17]. (4.2)

Ideally we would attempt to assign all signatures from ft to the 6-subsets in order
to establish (Pa,6)- To date however, this has not been achieved due to the large
number of signatures and consequent time required. However, by restricting the
concave signatures to those satisfying the geometric conditions, the search is readily
performed. We therefore define ft* c ft to be those concave signatures which satisfy
relations in (2.3) for all 4-subsets in 56.
As before, we note that if a signature in ft* is assigned to the elements of Am
corresponding to a 6-subset un then the possible choices for assignment to M;+I are
reduced as M; and uj+i share the 5 points {j + 1,... , j + 5} and so share Q = 10
triples. A simple computer search verifies that |ft*| = 892 and that for each signature
in ft*, its compatible subset contains no more than 18 signatures.
Two of the steps described in Algorithm  1 now need to be extended, as follows.

Extension to Algorithm 1, Step 1 In the 9-point case, we checked the convex rela-
tions to see if any other elements of Am are necessarily assigned, or if a contradiction
is reached. Now however, we not only check the convex relations (4.1) but also

https://doi.org/10.1017/S144618110000300X Published online by Cambridge University Press

160 George Szekeres and Lindsay Peters [10]

the geometric conditions (2.3). If all four triples corresponding to a 4-subset of Si7
are assigned, but neither of the geometric conditions (2.1) or (2.2) is satisfied, then
a contradiction has been reached. If two or three of the triples corresponding to a
quadrilateral are assigned, then it could be that one or two of the remaining triples
must necessarily be assigned to avoid a contradiction. For example, suppose <j\  and a4
are both assigned +, with o2 and <r3 unassigned. In this case, the only way to satisfy
one of the geometric conditions (2.1) and (2.2) is if a 2 and a3 are both assigned +.

Extension to Algorithm 1, Step 2 In the 9-point case, j never exceeded 3, which is
why the definition (3.3) sufficed. We now find however that j will reach its maximum
value of 12. That is, there are combinations of signatures assigned to u\, ..., ul2
which do not generate any contradictions. In this situation, we perform up to three
more types of checks:

The Uu check: We extend the U\ 2 to U^ by including another 6-subset

MI3 = [9,13,14,15,16,17].

We have arbitrarily chosen point 9, but any point from 1 to 11 would have sufficed.
We now check all signatures to w t3 compatible with the one assigned to un in the
sense that they must agree on the 10 triples they have in common. As the triples shared
between w12 and M13 are different to those shared between Uj and uj+i, 1 < j < 11, a.
second compatible subset is pre-calculated for each signature in £2*, in readiness for
assignments to u i3. We could extend these selected 6-subsets still further, but this was
not found to be necessary in practice. If an assignment is made to «i3 that still does
not lead to a contradiction, we go to the next step.
The one-bit check: We pick the first unassigned element a t of Am and arbitrarily
assign it to +. We then perform the checks in Algorithm 1, Step  1 as described above
(that is, both the convex and geometric checks). If a contradiction is generated, we
restore the state of Am to what it was before assigning ai and now check the —  as-
signment. If a contradiction is also generated we know that the current assignments
to Mi, ... , Mo necessarily lead to a contradiction, and we can proceed to Algorithm 1,
Step 3. If either assignment to a t did not lead to a contradiction, we restore the state
of Am to what it was before that assignment, and pick the next unassigned element
of Am. If we exhaust all unassigned elements of Am without generating a contradiction
we proceed to the next step.
The two-bit check: This is similar to the one-bit check except that instead of pick-
ing just one unassigned element of Am, we pick the first pair of unassigned elements.
There are now four assignments to check (++, H—, —h ), and if all lead to
a contradiction, we can again proceed to Algorithm 1, Step 3. If any of the four
assignments do not lead to a contradiction, we pick another pair of unassigned ele-
ments, and so on. It was found that the two-bit check always succeeded in generating

https://doi.org/10.1017/S144618110000300X Published online by Cambridge University Press

[11] Computer solution to the 17-pointErdos-Szekeres problem 161

a contradiction at this point in the search.
Whilst the two-bit check by itself would generate a contradiction to any combination
of signatures that the one-bit check had generated a contradiction for (and so subsumes
the one-bit check), the number of pairwise checks means that this step is much slower
to execute and so it is more efficient to do the one-bit check first.

The number of partial signatures that survived the (713 check was 20,312,212. The
number that survived the one bit check was 23,339.
There is evidently a certain arbitrariness in the three strategies above, and various
combinations of these strategies or others will suffice to check those few combinations
of signatures that do not lead to a contradiction when assigned to ux,..., M12. For
example, one of the authors (Szekeres) used a three-bit check instead of the £/13 check
for those signatures that had slipped through the one- and two-bit checks. (In his
implementation, B. McKay used a more efficient variation of the one-bit check in
place of the two-bit check).
The algorithm described above is amenable to parallel execution, as each assign-
ment of a signature from Q* to u i can be done independently of any other assignment
to Mj. For example, one could have up to |£2*|/2 = 446 independent processes, each
evaluating one of the possible assignments to Mi. Using modest computing platforms
(less than 2 GHz workstations) the time required to generate a contradiction from
just one assignment to ui took between one hour and twenty hours, depending on the
particular assignment. The total computing time to establish contradictions for all
446 assignments to U\, and thus establish Theorem 2, was approximately 3,000 GHz
hours, that is, 1,500 hours of computing time using processors of up to 2 GHz.

5. Proof of (Qltk)

In this section we shall prove the corresponding combinatorial (and weaker) version

of(G»):

(Q*a k) If n = 2
k~
2 there exists a a e E* which contains no convex ^-subset.

We present this partly for completeness, and partly to show how the new combina-
torial setting simplifies the original construction [4] if we don't insist on realisability.

LEMMA 1. Given i+j=m-2>2,  there exists a a e £/«-2s over  {1 ("!'*)}
which admits neither a C +il of length i nor a C-j of length j .

The statement is trivially true (empty) when i = 1 or j = 1, hence we may assume
that i > 1 and j > 1. Also we may assume that there exists a O\ € S/m-3x over
V.-i)
' (7:0)

https://doi.org/10.1017/S144618110000300X Published online by Cambridge University Press

162 George Szekeres and Lindsay Peters [12]

which admits neither a C+,, nor a C_;_! and a a2 e £/—3\ over

K
m-3

which admits neither a C+,,_i nor a C_,r Extend these two signature functions to the
whole set {l,... ,  (™~f)} by setting

Now suppose there is a C+i, = [fc0. • •• > &;]> then we must have k0 < k\ <
and ki > (™~j
3) since a2 does not admit a C+,,-_i. Let /x > 1 be such that

1 < fc*-i < - 2

then CT(A: M_!, k^, fc M+i) = —  by definition, contrary to the assumption that C+,, is a
cup. Similarly, suppose there is a C_,, = [k0, ..., kj] then we must have

and a(/:u_!, /:„, fcv+i) = + for suitable v > (7_,
3)> by definition, again a contradiction.
The extended signature function satisfies die constraints (2.3). For instance, if
1 < i\ < '2 < '3 < tf~i) < U then a(iu i2, i*) = o(i u /3, i4) = a(i 2, h, i*) = - and
(2.3) is satisfied irrespective of the value of a(i\, i 2, J3). Similarly for the other two
cases, hence a € SL, V
1,1-1/
To construct o e SJ-2 which does not admit a convex fc-subset we proceed as
follows: Let p r = £L 0 C~
2) for 0 < r < k - 2 so that p0 = 1, Pi_ 2 = 2
k~
2. Let
o-7 e S^_ 2) over P, = {/?,_, + 1 pM + (*T 2) = pj), 0 < j < k- 2, be such
that according to Lemma 1 it admits neither a C +J+i nor a C_,*_;_i. Setting Po = {1},
P*_2 = {2*~2}, then Uylo i s a partition of 5 = {1, 2, ... , 2
k~
2}.
Define n : 5 —»• {0, 1,...,/ : —  2} to be the projection 7r(r) = i if r 6 P,. We can
now extend the signature cr, to the whole of 5 by setting

a(kuk2,k3) =
 i, k2, k3),
 <n(k2) <n(k3),
< n(k2) = n(k3),
= n(k2) = n(k3)

https://doi.org/10.1017/S144618110000300X Published online by Cambridge University Press

[13] Computer solution to the 17-point Erdos-Szekeres problem 163

We show that this a does not admit a convex  fc-subset, that is, a pair of chains C+|M
C_ .5 with common endpoints and r + s = k. For suppose C + r = [a,a\, ..., a r_i, b]
and C-tS = {a,b\,..., as-U b] with n(a) = i, n(b) = j , i < j . If i = j then by
construction r + s < k  — 2 < k. If / < j , then 7r(fcM) = j for all 0 < \i < s and

i =  n(a) = 7r(fli) = • • • = n-(a,,) < 7r(av+i) < < 7r(ar_i) < y

fo r som e v < j . Henc e r< i + (j  — i ) =  j,s< k — j — l, r +  s< k — l<k .
Next  we verify that the conditions (2.3) hold for a. Take  any 4-subset {&i, £2, &3, &4},
nv — n(kv), v = 1,... , 4, so that n\ < 7r2 < 7r3 < 7r4. We may assume it\ < n^,
otherwise the points kv would all be in the same P, and by construction would satisfy
(2.3). Suppose that n\ < n2 <  TT3 < 7r4. Then

o(k\, k2, k4) =  <j{k\, k3, k4) — o(k2, k3, k4) = +

by definition, and (2.3) is satisfied. Similarly if it\ < n2 < n3 = n 4 then

a(ku k2, k3) =  a(Jkuk2, k4) = +, a(k u k3, k4) = o{k2, k3, k4) = - .

Finally if 7Ti < n2 = n 3 = JT4 then o(k\, k2, k3) = a(k u k2, k4) = a(k\, k3, k4) = -,
and in all cases (2.3) is satisfied. Thus a € SJ-*-

Acknowledgements

The authors gratefully acknowledge the assistance of B. McKay in independently
implementing and verifying  the algorithm presented in Section 4, and for his assistance
in the preparation of this article.
 References

[1] W. E.  Bonnice, "On convex polygons determined  by a finite planar set", Amer. Math. Monthly 81
(1974)749-752.
[2] F. R. K. Chung and R. L. Graham, "Forced convex n-gons in the plane", Discrete Comput. Geom.
19 (1998) 367-371, Special Issue.
[3] P. Erdos and G. Szekeres, "A combinatorial problem in geometry", Compositio Math. 2 (1935)

[4] P. Erdos and G. Szekeres, "On some extremum problems  in elementary geometry", Ann. Univ. Sci.
Budapest. Eotvds Sect. Math. 3-4 (1961) 53-63.
[5] J. D. Kalbfleisch, J. G. Kalbfleisch and R. G. Stanton, "A combinatorial problem on convex regions",
in 7970 Proc. Louisiana Con}, on Combinatorics, Graph Theory and Computing, (Louisiana State
Univ., Baton Rouge, 1970) 180-188.
[6] D. E. Knuth, Axioms and Hulls (Springer, Heidelberg, 1992).

https://doi.org/10.1017/S144618110000300X Published online by Cambridge University Press

164 George Szekeres and Lindsay Peters [14]

[7] W. Morris and V. Soltan, "The Erdos-Szekeres problem on points in convex position. A survey",
Bull. Amer. Math. Soc. (N.S.) 37 (2000) 437-458.
[8] G. Toth and P. Valtr, "The Erdos-Szekeres theorem: upper bounds and related results", in Com-
binatorial and computational geometry, Math. Sci. Res. Inst. Publ. 52, (Cambridge Univ. Press,
Cambridge, 2005) 557-568.
[9] R. M. Wilson and J. H. van Lint, A Course in Combinatorics (Cambridge Univ. Press, New York,
1992).

https://doi.org/10.1017/S144618110000300X Published online by Cambridge University Press
