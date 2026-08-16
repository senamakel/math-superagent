<!-- source: https://arxiv.org/pdf/2401.16210 | converted from PDF -->

arXiv:2401.16210v1  [math.CO]  29 Jan 2024
The Non-Cancelling Intersections
Conjecture

Antoine Amarilli

LTCI, T´el´ecom Paris,
Institut Polytechnique de Paris

a3nm@a3nm.net

Mika¨el Monet

Universit´e de Lille, CNRS, Inria, UMR 9189 - CRIStAL, F-59000 Lille, France

mikael.monet@inria.fr

Dan Suciu

University of Washington

suciu@cs.washington.edu

In this note, we present a conjecture on intersections of set families, and
a rephrasing of the conjecture in terms of principal downsets of Boolean
lattices. The conjecture informally states that, whenever we can express
the measure of a union of sets in terms of the measure of some of their
intersections using the inclusion-exclusion formula, then we can express the
union as a set from these same intersections via the set operations of disjoint
union and subset complement. We also present a partial result towards
establishing the conjecture.

Acknowledgements. We thank Louis Jachiet for helpful discussions on the problem,
and for having found the counterexample to a stronger version of the conjecture that is
mentioned at the end of Section 7. This work was done in part while the authors were
visiting the Simons Institute for the Theory of Computing.

1. Introduction

We present in this note a conjecture on intersection lattices of set families, which can be
equivalently stated on the Boolean lattice. The original motivation for the conjecture

1

comes from a problem in database theory about the existence of certain circuit repre-
sentations for probabilistic query evaluation (see [Monet, 2020a]), but in this note we
present the conjecture as a purely abstract claim without any database prerequisites.
A positive answer to this abstract conjecture implies a positive answer to the database
theory conjecture.
The conjecture can be understood in terms of the inclusion-exclusion formula. Con-
sider a family of sets S1, . . . , Sn. The inclusion-exclusion formula can be used to express
a quantity on the union S1 Y ¨ ¨ ¨ Y Sn (e.g., the cardinality, or the value of some mea-
sure) as a function of the intersections of the Si. In general, some of these intersections
may in fact be identical: we can in fact deﬁne the intersection lattice of the set fam-
ily to represent the possible intersections that can be obtained. Further, we can have
cancellations, i.e., some of the possible intersections may end up having a coeﬃcient of
zero in the inclusion-exclusion formula, due to cancellations. Thus, in the general case,
inclusion-exclusion allows us to express the measure of S1 Y ¨ ¨ ¨ Y Sn in terms of the
measure of the intersections I1, . . . , Im that have a non-zero coeﬃcient.
Our conjecture asks whether, in this case, one can obtain the set S1 Y ¨ ¨ ¨ Y Sn
from the intersections I1, . . . , Im, using the set operations of disjoint union and subset-
complement. If this is true, then it implies in particular the inclusion-exclusion formu-
lation, provided that our measure is additive in the sense that the measure of S ‚
Y S1

(where ‚
Y denotes disjoint union and
 ‚
z subset complement, as per Deﬁnition 3.1) is the
sum of the measure of S and of S1. Obtaining such a set expression can sometimes be
done simply by re-ordering the inclusion-expression formula: for instance, if we write
|X Y Y | “ |X| ` |Y | ´ |X X Y |, we can reorder to |X Y Y | “ |X| ´ |X X Y | ` |Y |, and

then express X Y Y “ pX
 ‚
z pX X Y qq ‚
Y Y . However, in general, it is unclear whether
such an expression can be obtained. Before continuing, let us give a ﬁrst toy example.

Example 1.1. Consider the set family F “ tS1, S2, S3u with S1 “ ta, b, du, S2 “
ta, b, c, eu, S3 “ ta, c, f u. Then:

|S1 Y S2 Y S3| “ |S1| ` |S2| ` |S3|

´ p|S1 X S2| ` |S1 X S3| ` |S2 X S3|q

` |S1 X S2 X S3|.

Since we have S1 X S3 “ S1 X S2 X S3, we obtain

|S1 Y S2 Y S3| “ |ta, b, du| ` |ta, b, c, eu| ` |ta, c, f u| ´ |ta, bu| ´ |ta, cu|.

The non-cancelling intersections are the ones that remain, i.e., ta, b, du, ta, b, c, eu,
ta, c, f u, ta, bu, and ta, cu, while tau (“ S1 X S3 “ S1 X S2 X S3) is a cancelling term.

Then, we can express S1 Y S2 Y S3 “ ta, b, c, d, e, f u with “`pta, b, du
 ‚
z ta, buq ‚
Y

ta, b, c, eu
˘ ‚
z ta, cu
‰ ‚
Y ta, c, f u: the reader can easily check that each ‚
Y (resp., each
‚
z) is a valid disjoint union (resp., subset complement), and that we have only used
the non-cancelling intersections. Note that this is not the only valid expression, for

2

instance we can also obtain the union with the expression rta, b, du
 ‚
z ta, busY rta, b, c, eu
 ‚
z
ta, cus Y ta, c, f u.

Our results imply that it is always possible when there are no cancellations (Fact 4.8),
or exactly one cancellation (in the equivalent formulation on Boolean lattices, Theo-
rem 6.2), but in general it seem challenging to do so while avoiding those intersections
which cancel out. The goal of this note is to present the current status of our eﬀorts
in attacking the conjecture, in particular showcasing some equivalent formulations, pre-
senting examples, and establishing a very partial result. After presenting preliminaries
in Section 2, we formally state the conjecture and give examples in Section 3. We show in
Section 4 that it suﬃces to study the conjecture on speciﬁc intersection lattices, which
we call tight, where informally the set family ensures that every possible intersection
contains exactly one element that is “speciﬁc” to this intersection (in the sense that it
is present precisely in this intersection and in larger intersections). We use this in Sec-
tion 5 to give an alternative formulation: instead of working with intersection lattices,
we can work with downsets on the Boolean lattice. We show that this is equivalent to
the original conjecture. The hope is that the setting of the Boolean lattice can be more
convenient to work with, as its structure is more restricted, and we can deﬁne quantities
such as the Euler characteristic that seem useful in understanding the structure of the
problem.
We next present in Section 6 a partial result that we can show in the context of the
Boolean lattice. In the rephrased problem, we must express a downset of that lattice
using disjoint union and subset complement on principal downsets spanned by elements
which do not “cancel out” in the sense of having non-zero M¨obius value. Our result
establishes that the rephrased conjecture is true when there is one single node of the
downset that has such value; this non-trivially extends the fact that the result is true
when no such nodes exist (Lemma 5.7), but falls short of the goal as in general many
such zeroes can occur.
We conclude in Section 7 with further questions and directions on the conjecture. We
point out that the conjecture can be strengthened, in two diﬀerent ways, to restrict the
shape of the disjoint-union and subset-complement expressions: we also do not know the
status of these stronger conjectures. We brieﬂy report on an unsuccessful experimental
search for counterexamples. We also hint at an incomplete proof of another partial result
where we can avoid more than one zero, provided the targeted downset satisﬁes a certain
decomposability condition.

2. Preliminaries

For a set S we write 2S its powerset. In this work, by family of sets, or simply set family,
we always mean a ﬁnite set of (not necessarily ﬁnite) sets. We generally use cursive
letters to denote set families, uppercase letters to denote sets, and lowercase letters for
elements of sets. For a set family F (resp., non-empty set family F) we write Ť F
(resp., Ş F) for ŤXPF X (resp., ŞXPF X). For a set X and two functions f, g : X Ñ Z,

3

we write f ` g (resp., f ´ g) the function deﬁned by pf ` gqpxq def
“ f pxq ` gpxq (resp.,
pf ´ gqpxq def
“ f pxq ´ gpxq) for all x P X.

Posets. Recall that a poset P “ pA, ďq is a pair consisting of a set A and a binary
partial order relation ď over A that is reﬂexive, antisymmetric and transitive. By slight
abuse of notation, we may write x P P to mean x P A (and U Ď P to mean U Ď A).
A greatest (resp., least) element of P is an element x P P such that for all x1 P P
we have x1 ď x (resp., x ď x1). When such an element exists it is unique, and we then
denote it by ˆ1 (resp., ˆ0). We may write ˆ0P , ˆ1P to avoid confusion when multiple posets
are involved.
For G Ď A, we deﬁne the upset of P generated by G (also called an order ﬁlter ),
denoted ÒP pGq, by ÒP pGq def
“ tx P P | Dy P G s.t. y ď xu. We also deﬁne the downset
generated by G (also called an order ideal), denoted ÓP pGq, by ÓP pGq def
“ tx P P |
Dy P G s.t. x ď yu. Note that ÒP pHq “ÓP pHq “ H. An upset (resp., a downset)
of P is a subset of P of the form ÒP pGq (resp., ÓP pGq) for G Ď A. When |G| “ 1 we
call ÒP pGq (resp., ÓP pGq) a principal upset (resp., principal downset), and by slight
abuse of notation we sometimes write ÒP pxq for x P P to mean ÒP ptxuq (resp., ÓP pxq
to mean ÓP ptxuq).
Two posets P1 “ pA1, ď1q and P2 “ pA2, ď2q are isomorphic if there exists a bijec-
tion h : A1 Ñ A2 such that for all x, y P P1 we have x ď1 y iﬀ hpxq ď2 hpyq. When this
is the case we write P1 » P2.

Lattices. A poset P “ pA, ďq is a meet semilattice if, for every x, y P P , there exists z P
P such that: (1) z ď x and z ď y; and (2) for every z1 P P such that z1 ď x and z1 ď y,
we have z1 ď z. This element z is then unique and is called the meet of x and y, and
written x ^ y. We similarly deﬁne join semilattices in the expected way, with the join
denoted x _ y, and then lattices as posets that are both a meet semilattice and a join
semilattice.
We recall that a ﬁnite join (resp., meet) semilattice that has a least (resp., greatest)
element is a lattice (see, e.g., [Stanley, 2011, Proposition 3.3.1]). We also recall the
property that in a meet semilattice L, the intersection of two principal downsets ÓL pxq
and ÓL pyq generated by x, y P L is the principal downset generated by x ^ y; the dual
property holds about principal upsets in join semilattices with the join operation.
For a set S we writeBS the Boolean lattice over S, by which we mean the lat-
tice p2S, Ďq, where join corresponds to set union and meet to set intersection.

Deﬁnition 2.1. A set family F is called trivial if it is empty or if there is X P F such
that Ť F “ X, and non-trivial otherwise.

We deﬁne the standard notion of intersection lattice of a non-trivial set family:

Deﬁnition 2.2 ([Stanley, 2011], Section 3.7.2). Let F be a non-trivial set family. For T Ď
F, T ‰ H, we deﬁne: ST def
“ Ş T . We also deﬁne SH def
“ Ť F with a slight abuse of
notation as SH depends on the underlying set family F.

4

Deﬁne the posetLF “ pA, Ďq, where A def
“ tST | T Ď Fu. Then one can check
thatLF is a meet semilattice whose meet operation is set intersection. We callLF the
intersection lattice of F. We say that a lattice L is an intersection lattice if it is of
the formLF for some non-trivial set family F. (Note that we might haveLF1 “LF2
for F1 ‰ F2.)

Remark 2.3. Every ﬁnite lattice L “ pA, ďq is isomorphic to some intersection lattice.
Indeed, deﬁne F def
“ tÓL ptU uq | U P A, U ‰ ˆ1Lu, i.e., the set of principal downsets of
L except ÓL ptˆ1Luq (as otherwise F is trivial). Then one can easily check that L »LF ,
since ÓL ptU uqX ÓL ptV uq “ÓL pU ^L V q for U, V P A.

Such a lattice L “LF has a ˆ0, which is SF “ Ş F, and a ˆ1, which is SH “ Ť F.
Notice that ˆ1 ‰ ˆ0 because F is non-trivial. Since L is a ﬁnite meet-semilattice that has
a ˆ1, we know that L is also a join-semilattice by the property mentioned above, but for
the purpose of this note we will not need to know what the join operation corresponds
to. Note that by deﬁnition ST1YT2 “ ST1 X ST2 for any T1, T2 Ď F. Observe that we may
have ST1 “ ST2 with T1 ‰ T2, in which case ST1 “ ST2 “ ST1YT2.

Example 2.4. Figure 1 shows the Hasse diagrams of the various intersection lattices
deﬁned next. (Ignore for now the integer annotations next to the nodes and the fact that
some nodes are colored.)

L1. The intersection lattice L1 of (the non-trivial set family containing) S1 “ tn P N |
n ” 0 pmod 2qu, S2 “ tn P N | n ” 0 pmod 3qu, and S3 “ tn P N | n ” 0
pmod 12qu is shown in Figure 1a.

L2. The intersection lattice L2 of S1 “ ta, du, S2 “ tb, du, and S3 “ tc, du is shown in
Figure 1b. This example illustrates that an intersection lattice is not necessarily
distributive.

L3. The intersection lattice L3 of S1 “ ta, bu, S2 “ ta, cu, S3 “ tb, cu, and S4 “ tdu is
shown in Figure 1c.

L4. The intersection lattice L4 of S1 “ ta, c, d, gu, S2 “ ta, b, d, f u, S3 “ ta, b, c, eu, and
S4 “ ta, hu is shown in Figure 1d. Observe that L3 and L4 are isomorphic.

Finally, another intersection lattice L5 is depicted in Figure 2 (ignore for now the tree).

In an intersection lattice L “LF , for every x P ˆ1, the set of elements of L in
which x occurs is the principal upset of L generated by minLpxq def
“ StXPF |xPXu. Note
that minLpxq ‰ ˆ1 because F is non-trivial. In particular we have the following:

Fact 2.5. Let L be an intersection lattice and U P L. Then we have U “ Ť U 1PL
U 1ĎU tx P ˆ1 |

U 1 “ minLpxqu, and this union is disjoint.
 5

tn P N | n ” 0 pmod 2q or n ” 0 pmod 3qu

tn P N | n ” 0 pmod 2qu tn P N | n ” 0 pmod 3qu

tn P N | n ” 0 pmod 6qu

tn P N | n ” 0 pmod 12qu
 1

´1 ´1

1

0

(a) Lattice L1
 ta, b, c, du

ta, du tb, du tc, du

tdu
 1

´1 ´1 ´1

2

(b) Lattice L2

ta, b, c, du
 tduta, bu

tau
 ta, cu

tbu
 tb, cu

tcu

H
 1
 ´1´1

1

´1´1

1 1

0

(c) Lattice L3
 ta, b, c, d, e, f, g, hu
 ta, huta, c, d, gu

ta, du
 ta, b, d, f u

ta, cu
 ta, b, c, eu

ta, bu

tau
 1
 ´1´1

1

´1´1

1 1

0

(d) Lattice L4

Figure 1: Hasse diagrams of the intersection lattices from Example 2.4. The integer
value besides each node n is µLpn, ˆ1q and is computed top-down following Def-
inition 2.6. The orange nodes are the non-cancelling non-trivial intersections.

M¨obius inversion formula and inclusion-exclusion. We now introduce the M¨obius func-
tion on ﬁnite posets.

Deﬁnition 2.6. Let P “ pA, ďq be a ﬁnite poset. The M¨obius function of P is the
function µP with value in Z and domain the set of pairs px, yq P A ˆ A such that x ď y,
deﬁned, for each y P A, by induction over the elements x such that x ď y:

• µP py, yq def
“ 1;

• µP px, yq def
“ ´ ř
xăzďy µP pz, yq.1

Proposition 2.7 (M¨obius inversion formula; see, e.g., Prop. 3.7.1 of [Stanley, 2011]).
Let P “ pA, ďq be a ﬁnite poset, and let f, g : A Ñ R. Then we have:

gpxq “ ÿ

yďx f pyq for all x P P if and only if f pxq “ ÿ

yďx µP py, xqgpyq for all x P P.

One important application of the M¨obius inversion formula is in determining the
measure of a union of sets from the measure of some of their intersections. For our
purposes, given a set S, what we call a measure on 2S is a function ξ : 2S Ñ R which
is nonnegative (i.e., ξpU q ě 0 for all U P 2S), which satisﬁes ξpHq “ 0, and which is
additive under countable disjoint unions, i.e., for any countable collection tEku8
k“1 of

1The M¨obius function is traditionally deﬁned with µP px, yq def
“ ´ ř

xďzăy µP px, zq, but the two deﬁni-
tions are equivalent [Rota, 1964, Proposition 3]. We use this version as it simpliﬁes our presentation.

6

abb1cc1dee1f f 1gg1 1

abb1d ´1 abc1f 1 ´1 ab1c1e1 ´1 ag1 ´1ab1cf ´1abce ´1ag ´1
 ab1 2 ac1 1ab 2ac 1
 a 0
 ‚
Y

‚
z

‚
Y

‚
z

‚
Y

‚
z

‚
Y

‚
z

‚
Y

‚
z

‚
Y

‚
z

abce ab
 abc1f 1
 ac1
 ag
 ac
 ab1cf
 ab1
 ag1
 ab
 abb1d
 ab1
ab1c1e1

abb1cc1dee1f f 1gg1

ce

abcec1f 1
 bcef 1

abcef 1g
bef 1g

abb1cef f 1g

bcef f 1g

abcef f 1gg1

cef f 1gg1

abb1cdef f 1gg1

bcdef f 1gg1

Figure 2: A tight intersection lattice of seven sets, and a witnessing tree showing that it
does not violate the conjecture. For brevity we omit curly braces and commas
when writing sets, i.e., ab stands for ta, bu.

7

pairwise disjoint subsets of S, we have ξ `Ť8
k“1 Ek˘ “ ř8
k“1 ξpEkq. In particular, ξ is
completely determined by the images of the singleton sets txu for x P S.

Proposition 2.8. Let L be an intersection lattice, and let ξ be a measure on 2
ˆ1. Then
we have ξpˆ1q “ ´ ÿ

U PL
U ‰ˆ1
 µLpU, ˆ1qξpU q. (1)

Proof. This is a known result but, to be self-contained, we reproduce the proof from
[Stanley, 2011] (end of Section 3.7, page 304). Let us deﬁne two functions f, g : L Ñ
R. For U P L, let gpU q def
“ ξpU q, and deﬁne f pU q to be the measure of all elements
of U which belong to no U 1 Ĺ U , i.e., f pU q def
“ ξptx P ˆ1 | minLpxq “ U uq. Observe
that gpU q “ ř U 1PL
U 1ďU f pU 1q for all U P L, by additivity of ξ and using Fact 2.5. Therefore

by Proposition 2.7 we have that f pˆ1q “ řU PL µLpU, ˆ1qgpU q. But notice that gpˆ1q “ ξpˆ1q
and that f pˆ1q “ ξpHq (because L “LF for some F non-trivial), so that f pˆ1q “ 0.
Therefore indeed ξpˆ1q “ ´ řU PL
U ‰ˆ1 µLpU, ˆ1qξpU q.

We point out that the above proposition can fail if the underlying set family F is
trivial2: this is the reason why we always work with non-trivial families of sets.

Example 2.9. For the lattices L1, L2, L3, L4, L5 from Example 2.4, the values µLipU, ˆ1q
for all elements U P Li are shown next to the corresponding nodes in Figures 1 and 2.

This motivates the following deﬁnitions.

Deﬁnition 2.10. Let L be an intersection lattice. We call ˆ1 the trivial intersection. We
deﬁne the non-trivial intersections of L, denoted NTIpLq, by

NTIpLq def
“ tU P L | U ‰ ˆ1u,

and we deﬁne the non-cancelling, non-trivial intersections (or simply non-cancelling
intersections) of L, denoted NCIpLq, by

NCIpLq def
“ tU P L | U ‰ ˆ1 and µLpU, ˆ1q ‰ 0u.

In other words, the non-cancelling intersections are those intersections that do not can-
cel in the inclusion-exclusion formula, i.e., those U such that ξpU q occur in Equation (1)
with non-zero coeﬃcient.
Last, we will also need the following application of the M¨obius inversion formula,
which is another formulation of the inclusion-exclusion principle.

Proposition 2.11. Let S be a ﬁnite set, and let f, g :BS Ñ R. Then we have gpXq “řX 1PBS
XĎX 1 f pX 1q for all X PBS if and only if f pXq “ řX 1PBS
XĎX 1 p´1q|X 1|´|X|gpX 1q for all

X PBS.

2Take for instance F “ tta, bu, tauu.
 8

This result can be obtained by observing that µBS pX, Y q “ p´1q|Y |´|X| for X Ď Y as
shown in [Stanley, 2011, Example 3.8.1] and using the dual form of the M¨obius inversion
formula [Stanley, 2011, Proposition 3.7.2].

3. The Non-Cancelling Intersections Conjecture

In this section we state the conjecture and illustrate it with a few toy examples. We adapt
to our context notation and terminology from [Hirsch and McLean, 2017] for disjoint
unions and subset complements.

Deﬁnition 3.1. For two sets S, T , the disjoint union S ‚
Y T equals S Y T if S X T “ H,
else it is undeﬁned. We generalize the disjoint union operator to more than two operands

in the expected way. The subset complement S
 ‚
z T equals SzT if T Ď S, else it is
undeﬁned.

Notice that
 S ‚
Y T “ U iﬀ U
 ‚
z S “ T iﬀ U
 ‚
z T “ S. (2)

Deﬁnition 3.2. Let F be a set family. The partial dot-algebra generated by F, de-
noted ‚pFq, is the smallest (for inclusion) set family of subsets of 2
Ť F which contains
H as well as all the sets of F and is closed under disjoint union and subset complement.
Formally, it is deﬁned inductively by:

1. First base case: H P ‚pFq;

2. Second base case: for each X P F, we have X P ‚pFq;

3. Induction: for each X1, X2 P ‚pFq, if X1 ‚
Y X2 (resp., X1
 ‚
z X2) is well-deﬁned,

then we have X1 ‚
Y X2 P ‚pFq (resp., X1
 ‚
z X2 P ‚pFq).

Note that when F is not empty, then item (1) is redundant as it follows from (2) and

(3): taking any X P F, we have X P ‚pFq by item (2), and X
 ‚
z X “ H P ‚pFq by
item (3).
Furthermore, observe that ‚pFq is always ﬁnite because F is. What we call a witness-
ing tree of X P ‚pFq is a rooted ordered tree whose leaves are annotated with H or with

elements of F and whose internal nodes are annotated with either ‚
Y or
 ‚
z (with the node

being binary if it is is annotated with
 ‚
z), with the expected semantics. Obviously, we
have X P ‚pFq if and only if such a witnessing tree exists.

Example 3.3. Let F1 “ tta, du, tb, eu, ta, b, cuu. Then ‚pF1q “ F1 Y tH, ta, b, d, euu.
Let F2 “ tta, cu, tb, cu, tcuu. Then we have ‚pF2q “ 2ta,b,cu. Two trees T0, T 1
0 which
witness that ta, b, cu P ‚pF2q are shown in Figure 3.

We are now ready to state the conjecture.

9

‚
Y

‚
z

ta, cu tcu
 tb, cu

ta, b, cu

tau

(a) Tree T0
 ‚
Y

‚
z

ta, cu tcu
 ‚
z

tb, cu tcu
 tcu

ta, b, cu

tau tbu

(b) Tree T 1
0

‚
Y

‚
z

ta, c, d, gu ta, cu
 ‚
z

ta, b, d, f u ta, du
 ‚
z

ta, b, c, eu ta, bu
 ta, hu

ta, b, c, d, e, f, g, hu

td, gu tb, f u tc, eu

(c) Tree T1

‚
Y

‚
z

‚
Y

‚
z

‚
Y

‚
z

ta, c, d, gu ta, cu

ta, b, c, eu

ta, bu

ta, hu

ta, du

ta, b, d, f u

ta, b, c, d, e, f, g, hu

td, gu

ta, b, c, d, e, gu

tc, d, e, gu

ta, c, d, e, g, hu

tc, e, g, hu

(d) Tree T 1
1
 ‚
Y

‚
z

‚
Y

‚
z

‚
Y

‚
z

ta, bu tbu
 tb, cu
 tcu
 tdu
 tau
ta, cu

ta, b, c, du

tau

ta, b, cu

ta, bu

ta, b, du

tb, du

(e) Tree T2

Figure 3: Various witnessing trees. The sets that internal nodes correspond to are shown
in orange.
 10

Conjecture 3.4 (NCI conjecture, formulation I). For every intersection lattice L, we
have ˆ1 P ‚pNCIpLqq.

In other words, the conjecture states that, given any non-trivial set family, we can
always express the union of the sets by starting with the set intersections that do not
cancel in the inclusion-exclusion formula and applying the disjoint union and subset
complement operators.

Example 3.5. Continuing Example 2.4, the nodes corresponding to sets of NCIpLiq are
colored in orange in Figure 1: they are the nodes diﬀerent from ˆ1 with a non-zero value
of the M¨obius function. We show next that ˆ1 P ‚pNCIpLiqq for all of them.

L1. We have ˆ1 “ tn P N | n ” 0 pmod 2q or n ” 0 pmod 3qu “ rtn P N | n ” 0

pmod 2qu
 ‚
z tn P N | n ” 0 pmod 6qus ‚
Y tn P N | n ” 0 pmod 3qu.

L2. We have ˆ1 “ ta, b, c, du “ rta, du
 ‚
z tdus ‚
Y rtb, du
 ‚
z tdus ‚
Y rtc, dus.

L3. We have ˆ1 “ ta, b, c, du “ tau ‚
Y tbu ‚
Y tcu ‚
Y tdu.

L4. Two trees T1, T 1
1 which witness that ˆ1 P ‚pNCIpL4qq can be found in Figure 3.

L5. A witnessing tree for L5 can be found in Figure 2.

The motivation for the conjecture is to understand whether the inclusion-exclusion
formula can be understood using the Boolean operations of disjoint union and subset
complement. Speciﬁcally, let F be a non-trivial set family, consider its intersection
latticeLF , recall that ˆ1 “ Ť F, and let ξ be a measure on 2
ˆ1. We know that the mea-
sure of ˆ1 can be obtained from the measure of the non-cancelling intersections, namely,
Proposition 2.8 expresses the measure ξpˆ1q of the set ˆ1 as an arithmetic combination of
the measures ξpSq with S P NCIpLq. The conjecture says that we can also express the
set ˆ1 from the sets S with S P NCIpLq using the Boolean operations of disjoint union
and subset complement.

Dual version: non-cancelling unions conjecture. We end this section by presenting a
dual version of the NCI conjecture that focuses on unions instead of intersections, and
that we call the non-cancelling unions (NCU) conjecture. Call a set family F co-trivial
if it is empty or if there is X P F such that X “ Ş F, and non-co-trivial otherwise.
Deﬁne the union latticeUF of a non-co-trivial set family F as follows: let RH def
“ Ş F

and RT def
“ Ť T for T Ď F, T ‰ H, andUF def
“ ptRT | T Ď Fu, Ďq. ThenUF is a
lattice whose join operation corresponds to set union, has a greatest element ˆ1 “ Ť F
and a least element ˆ0 “ Ş F that are distinct. A lattice is a union lattice if it is of the
formUF for some non-co-trivial set family. Analogously to Proposition 2.8, it is easy to
show that for a union lattice L and measure ξ on 2
ˆ1, we have

ξpˆ0q “ ´ ÿ

U PL
U ‰ˆ0
 µLpˆ0, U qξpU q. (3)

11

Deﬁne then the non-cancelling (non-trivial) unions of L as

NCUpLq def
“ tU P L | U ‰ ˆ0, µLpˆ0, U q ‰ 0u.

The non-cancelling unions conjecture is then:

Conjecture 3.6 (NCU conjecture). For every union lattice L, we have ˆ0 P ‚pNCUpLqq.

Notice here that the deﬁnition of the dot-algebra is unchanged: we still use disjoint
complement and disjoint union. Informally again, this is stating that, given a set fam-
ily, we can always express their intersection by applying the disjoint union and subset
complement operations to the set unions that do not cancel in the (“union form” of the)
inclusion-exclusion formula.
We show in Appendix A that, unsurprisingly, the NCI and NCU conjectures are in fact
equivalent. We decided to focus on the intersections version of the conjecture because
inclusion-exclusion is most often presented in “intersection form”.

4. Simplifying to Tight Intersection Lattices

In this section we show that the NCI conjecture can be studied without loss of generality
on intersection lattices satisfying a certain tightness condition, that we deﬁne next.
Intuitively, an intersection lattice L is tight if for every U P L, U ‰ ˆ1, there is exactly
one element x P ˆ1 such that minLpxq “ U . We also deﬁne the notion of an intersection
lattice being full, which will be useful in the next section.

Deﬁnition 4.1. An intersection lattice L is full if for every U P L, U ‰ ˆ1, we have tx P
ˆ1 | minLpxq “ U u ‰ H.3 The lattice L is in addition called tight if for every U P L, U ‰
ˆ1, we have |tx P ˆ1 | minLpxq “ U u| “ 1.

For instance, the intersection lattices L2 and L4 from Figure 1 and L5 from Figure 2
are tight (hence full), L1 is full but not tight, and L3 is not full (hence not tight). Note
that if an intersection lattice L “LF is tight, then ˆ1 is ﬁnite, i.e., the sets in F are
themselves ﬁnite: this can be seen by applying Fact 2.5 with U “ ˆ1. We then claim that
we can reformulate the NCI conjecture as follows:

Conjecture 4.2 (NCI conjecture, formulation II). For every tight intersection lattice L,
we have ˆ1 P ‚pNCIpLqq.

We prove this in two steps. First, we show that for every intersection lattice L, there
exists a tight intersection lattice L1 that is isomorphic to L.

Lemma 4.3. For every intersection lattice L, there exists a tight intersection lattice L1

such that L » L1.

3Note that tx P ˆ1 | minLpxq “ ˆ1u “ H because F is non-trivial.

12

Proof. It suﬃces to observe that the intersection lattice constructed in Remark 2.3 (call
it L1) is tight. Indeed, letting U P Lztˆ1Lu, corresponding to ÓL ptU uq in L1, we have
that tx P ˆ1L1 | minL1pxq “ÓL ptU uqu “ tU u.

Second, we show that, for two isomorphic intersection lattices L, L1 such that L1 is
full, then ˆ1L1 P ‚pNCIpL1qq implies ˆ1L P ‚pNCIpLqq.

Lemma 4.4. Let L, L1 be isomorphic intersection lattices such that L1 is full and such
that ˆ1L1 P ‚pNCIpL1qq. Then we have ˆ1L P ‚pNCIpLqq.

Proof. Let h : L Ñ L1 be an isomorphism. Since L1 is full, for U 1 P L1, U 1 ‰
ˆ1L1, let αU 1 be an element of tx1 P ˆ1L1 | minL1px1q “ U 1u. Deﬁne g : ˆ1L Ñ ˆ1L1

by gpxq def
“ αhpminLpxqq for x P ˆ1L. Note that g is not necessarily injective. For x1 P ˆ1L1

let g´1px1q def
“ tx P ˆ1L | gpxq “ x1u, and for X 1 Ď ˆ1L1 let g´1pX 1q def
“ Ťx1PX 1 g´1px1q.
From Fact 2.5 and because L1 is full it is easy to see that (:) for every U 1 P L1 we
have g´1pU 1q “ h´1pU 1q. In particular we have g´1pˆ1L1q “ ˆ1L. Hence, it is enough
to prove that for all X 1 P ‚pNCIpL1qq we have g´1pX 1q P ‚pNCIpLqq. We show this
by induction on NCIpL1q. The ﬁrst base case is when X 1 “ H. But then observe
that g´1pX 1q “ H, and that H P ‚pNCIpLqq by deﬁnition. The second base case
is when X 1 P NCIpL1q. But then g´1pX 1q P NCIpLq as well by (:) and because h is
an isomorphism so clearly µL1pX 1, ˆ1L1q “ µLph´1pX 1q, ˆ1Lq. The ﬁrst inductive case
is when X 1 “ X 1
1
 ‚
Y X 1
2 with X 1
1, X 1
2 P ‚pNCIpL1qq. By induction hypothesis we
have g´1pX 1
1q, g´1pX 1
2q P ‚pNCIpLqq. Moreover clearly g´1pX 1
1q X g´1pX 1
2q “ H since X 1
1
and X 1
2 are disjoint. So indeed g´1pX 1q “ g´1pX 1
1q ‚
Y g´1pX 1
2q P ‚pNCIpLqq. The second

inductive case is when X 1 “ X 1
1
 ‚
z X 1
2 with X 1
1, X 1
2 P ‚pNCIpL1qq. By induction hypothe-
sis again we have g´1pX 1
1q, g´1pX 1
2q P ‚pNCIpLqq. Moreover clearly g´1pX 1
2q Ď g´1pX 1
1q

since X 1
2 Ď X 1
1. So indeed g´1pX 1q “ g´1pX 1
1q
 ‚
z g´1pX 1
2q P ‚pNCIpLqq. This concludes
the proof.

This indeed proves that the two formulations are equivalent. We illustrate this last
construction in the following example.

Example 4.5. Consider the intersection lattices L3 and L4 from Figure 1, the isomor-
phism h : L3 Ñ L4 deﬁned following their drawings, and αU 1 for U 1 P L4 U 1 ‰ ˆ1L4 being
the only element in tx1 P ˆ1L4 | minL4px1q “ U 1u (since L4 is tight). Then we have, for
instance, g´1pdq “ tau, g´1paq “ g´1pf q “ H. Moreover, consider the tree T 1
1 from Fig-
ure 3d witnessing that ˆ1L4 P ‚pNCIpL4qq. Applying g´1 to every node of this tree yields
the tree T2 from Figure 3e that witnesses ˆ1L4 P ‚pNCIpL4qq. By contrast, consider the
expression tau ‚
Y tbu ‚
Y tcu ‚
Y tdu that also witnesses ˆ1L3 P ‚pNCIpL3qq. This expression
cannot be translated through h into a tree for L4 as, e.g., the operation tbu ‚
Y tcu would
translate to ta, cu ‚
Y ta, bu in L4, which is not valid.

In fact we claim that, when L is a full intersection lattice, any tree T witnessing
that ˆ1 P ‚pNCIpLqq must use all of the sets in NCIpLq. (This is not the case of the
expression tau ‚
Y tbu ‚
Y tcu ‚
Y tdu for L3 for instance, but L3 is not full.) In a sense, this

13

means that the full intersection lattices are the hardest cases for the NCI conjecture. We
formalize and state a stronger claim (on the non-trivial intersections instead of only the
non-cancelling ones) in the remaining of this section.

Deﬁnition 4.6. Let F be a set family, X P ‚pFq and T a tree witnessing this. For a
leaf ℓ of T , the polarity of ℓ in T , denoted polT pℓq, is 1 if the number of times we take

the right edge of a
 ‚
z node in the path from the root of T of ℓ is even; and ´1 otherwise.
The multiplicity of U P F Y tHu in T is then

multT pU q def
“ ÿ

ℓ leaf of T
of the form U
 polT pℓq.

In other words, if we see each U P F Y tHu as a variable and see T as an arithmetic

expression over these variables (by replacing ‚
Y nodes by ` and
 ‚
z nodes by ´), then the
multiplicity of U in T is the coeﬃcient of the corresponding variable once we develop
this expression and factorize. We then have:

Proposition 4.7. Let L be a full intersection lattice such that ˆ1 P ‚pNTIpLqq, and T a
tree witnessing this. Then we have multT pU q “ ´µLpU, ˆ1q for every U P NTIpLq.

Since Proposition 4.7 will not be strictly needed to establish our main results, we defer
its proof to Appendix B. (We include this proposition as we think that it is relevant to
motivate the conjecture.) Notice that Proposition 4.7 can be false if we do not impose
intersection lattices to be full, see e.g., the expression for L3 given in Example 3.5.
Furthermore, one can show that for any tight intersection lattice L we have ‚pNTIpLqq “
2
ˆ1L. In other words, intuitively, if we use the non-trivial intersections instead of the
non-canceling intersections in the conjecture, then we can achieve all possible sets of
elements:

Fact 4.8. For every tight intersection lattice L we have ‚pNTIpLqq “ 2
ˆ1L.

Proof. Generalizing from tight intersection lattices, we will show that the result holds
more generally when we assume that for every U P L, U ‰ ˆ1, there is at most one
element x P ˆ1 such that minLpxq “ U . Let L be an intersection lattice satisfying this
weaker condition. We proceed by induction on the downsets of L, showing the following
by induction on 0 ď n ă |L|: for any downset D of L containing n nodes, letting XD Ď ˆ1
be the set of elements introduced at nodes of D, formally, tx P ˆ1 | minLpxq P Du, then
we have ‚pDq “ 2XD . Note that, when taking this claim with n “ |L| ´ 1, then the only
downset D of L containing |L| ´ 1 nodes is the downset D containing all intersections
except SH, i.e., precisely NTIpLq, and then XD “ ˆ1, so this claim with n “ |L| ´ 1 is the
result we want to show.
The base case is n “ 0, i.e., the downset D “ H. Then XD “ H and ‚pHq “ tHu “
2XD and we are done.
For the induction case, let D be a downset containing at least one node, let U be some
maximal node of D, and let D1 “ DztU u. The ﬁrst case is then there is no element

14

introduced at U , i.e., U “ ŤU 1PL,U 1ĹU U 1, then we have XD “ XD1, and the induction
hypothesis gives us that ‚pD1q “ 2XD1 “ 2XD , which concludes because ‚pDq Ě ‚pD1q
(as D1 Ď D) and clearly ‚pDq Ď 2XD . Let us thus focus on the second case, where there
is an element x introduced at U .
We ﬁrst show that txu P ‚pDq. Indeed, by deﬁnition we have U P ‚pDq because U P D.
Further, all elements of U except x were introduced below U and in D1, and therefore
we have that U ztxu Ď XD1. Hence, by induction hypothesis, we have U ztxu P ‚pD1q, so
U ztxu P ‚pDq because D1 Ď D. From U P ‚pDq and U ztxu P ‚pDq we deduce txu P ‚pDq.
Now let us show that ‚pDq “ 2XD . Pick Y P 2XD . If x R Y , then Y P 2XD1 , so by
induction hypothesis Y P ‚pD1q, hence Y P ‚pDq, so we conclude immediately. If x P Y ,
let Y 1 “ Y ztxu. We have Y 1 P 2XD1 , so by induction hypothesis we have Y 1 P ‚pD1q hence
Y 1 P ‚pDq. Further, we have established in the previous paragraph that txu P ‚pDq. We
conclude that Y P ‚pDq. Thus, we have shown the inductive claim ‚pDq “ 2XD .
We have concluded the induction, which as we explained establishes the claim.

By Proposition 4.7, in a tree T which witnesses that ˆ1 P ‚pNTIpLqq for a full intersection
lattice L, the multiplicity of a cancelling intersection is zero. Intuitively, we can see this
as suggesting that we do not really need such intersections, and so that the NCI conjecture
should morally be true. In addition notice that, for a measure ξ on 2
ˆ1, applying ξ to T

(and replacing ‚
Y nodes by ` and
 ‚
z nodes by ´) and then factoring gives back exactly
Equation (1) according to Proposition 4.7.

5. Alternative Formulation: Dot-Algebra of Non-Cancelling
Principal Downsets in the Boolean Lattice

In this section we give an alternative formulation of the conjecture which is about the
Boolean lattice. It will in particular use results from the previous section. As the
structure of the Boolean lattice is “simpler”, the hope is that the alternative formulation
of the conjecture may be easier to attack. We present the alternative formulation and
show that it is equivalent in Section 5.1, and show in Section 5.2 some useful properties
that we can deduce from this alternative formulation.

5.1. The NCPD conjecture

For S ﬁnite, we call a conﬁguration ofBS, or simply conﬁguration when clear from
context, a subset ofBS. Since conﬁgurations are in particular set families, we will
generally denote them with cursive letters.
We start by deﬁning what we call generalized M¨obius functions, that are parameterized
by a conﬁguration, and that take only one argument.

Deﬁnition 5.1. Let S ﬁnite and C ĎBS a conﬁguration. We deﬁne the (generalized)

15

H 0

0 0 1 0 2 0 3 0

01 0 02 0 03 0 12 0 13 ´1 23 ´1

012 0 013 1 023 0 123 1

0123 0

Figure 4: Visual representation of the conﬁguration C from Example 5.2 and of its as-
sociated M¨obius function ˆµBS,C beside each node. Here, C consists of all the
colored nodes.

M¨obius function ˆµBS,C :BS Ñ Z associated to C by top-down induction by:

ˆµBS,CpXq def
“
 #
1 ´ řXĹX 1 ˆµBS,CpX 1q if X P C
´ řXĹX 1 ˆµBS,CpX 1q if X R C .

In particular, the value ˆµBS,CpSq is 0 if S R C, and 1 if S P C.

Example 5.2. Let C be the conﬁguration

tt0u, t1u, t0, 1u, t0, 3u, t1, 2u, t1, 3u, t0, 1, 3u, t1, 2, 3uu

ofBt0,1,2,3u. We have depicted in Figure 4 this conﬁguration and its associated M¨obius
function.

Next, we deﬁne the non-cancelling principal downsets of such a conﬁguration.

Deﬁnition 5.3. Let S ﬁnite and C a conﬁguration of BS. The set of non-cancelling
principal downsets ofBS with respect to C, denoted NCPDBS pCq, is deﬁned by

NCPDBS pCq def
“ tÓBS pXq | X PBs, ˆµBS,CpXq ‰ 0u.

(Recall that we write ÓBS pXq for ÓBS ptXuq.)

Note that the elements of NCPDBS pCq are subsets ofBS. The notation might appear
heavy at ﬁrst sight, e.g., using subscripts in ˆµBS,C and NCPDBS to always recall which
Boolean lattice we are considering. This will however help to avoid confusion in later
proofs, when multiple Boolean lattices and conﬁgurations will be involved.
We are now ready to state the alternative formulation, which we call for convenience
the NCPD conjecture.
 16

Conjecture 5.4 (NCPD conjecture). For every ﬁnite S, for every conﬁguration I ofBS
that is a downset ofBS, we have that I P ‚pNCPDBS pIqq.

We point out that, if we do not ask the conﬁguration to be a downset ofBS then the
statement is false, i.e., there exists a ﬁnite S and conﬁguration C ofBS such that C R
‚pNCPDBS pCqq: see Section 7.
We prove in the remaining of this section that this conjecture is equivalent to the NCI
conjecture. We start with a general-purpose lemma that gives a correspondence between
both formulations:

Lemma 5.5. Let S be a ﬁnite set and let I be a downset ofBS of the form I “ ÓBS pFq

for F a non-trivial set family. For X P F let X 1 def
“ ÓBS pXq (which is 2X ), and let F 1 def
“
tX 1 | X P Fu. Note that F 1 is non-trivial as well, and let then L be its intersection
lattice. Then we have NCPDBS pIq “ NCIpLq.

The proof of this lemma is tedious and we defer it to Appendix C. We then show each
direction of the equivalence in turn.

NCI conjecture (formulation I) ùñ NCPD conjecture. Assume Conjecture 3.4 to
be true, let I be a conﬁguration ofBS for some ﬁnite set S, assume that I is a downset,
and let us show that I P ‚pNCPDBS pIqq. If I is empty this is clear because then we have
‚pNCPDBS pIqq “ ‚pHq “ tHu. If I is a principal downset ofBS this is also clear, because
in that case we have that ˆµBS,IpXq for X PBS equals 1 if I “ÓBS pXq and 0 otherwise, so
assume that I is not empty and is not a principal downset. Then I is of the form ÓBS pFq
for some non-trivial set family F. Let then L be the intersection lattice constructed
from S and F as in Lemma 5.5. By this Lemma we have that NCPDBS pIq “ NCIpLq.
By the hypothesis of Conjecture 3.4 being true we have ˆ1L P ‚pNCIpLqq, but ˆ1L is I so
indeed I P ‚pNCPDBS pIqq.

NCPD conjecture ùñ NCI conjecture (formulation II). Assume now that Con-
jecture 5.4 is true, let F be a non-trivial set family such that the intersection lat-
tice L “LF is tight, and let us show that ˆ1L P ‚pNCIpLqq. For X P F let X 1 def
“ 2X , and
let F 1 def
“ tX 1 | X P Fu. Note that F 1 is non-trivial as well, so let us consider L1 “LF 1.
For T Ď F, let T 1 be the corresponding subset of F 1, i.e., T 1 “ tX 1 | X P T u, and
vice versa. Then observe that for T Ď F, T ‰ H we have ST 1 “ 2ST , so that L » L1.
Moreover we have that L1 is full: indeed it is clear that for T Ď F, T ‰ H we have
ST P tX P ˆ1L1 | minL1pXq “ ST 1u.4 Deﬁne now S “ ˆ1L (which is ﬁnite because L
is tight), and let I be the downset ofBS that is ÓBS pFq. Observe then that L1 is
exactly the intersection lattice that we would obtain from the construction described in
Lemma 5.5 applied on S and F, so that NCPDBS pIq “ NCIpL1q by that lemma. Since
Conjecture 5.4 is true by hypothesis we have I P ‚pNCPDBS pIqq, hence I P ‚pNCIpL1qq.

4But note that L
1 is never tight: indeed we have, e.g., tX P ˆ1L1 | minL1 pXq “ ˆ0L1 u “ tˆ0L, Hu.

17

But I “ tY PBS | DX P F, Y Ď Xu by deﬁnition, which is equal to Ť F 1, which
is ˆ1L1 by deﬁnition. Therefore ˆ1L1 P ‚pNCIpL1qq. This implies ˆ1L P ‚pNCIpLqq as well by
Lemma 4.4.

5.2. Useful facts

We now present useful facts about the NCPD formulation of the conjecture that motivate
its introduction.
First, we observe that the generalized M¨obius functions are linear (in their parameters)
under disjoint union and subset complement.

Fact 5.6. Let S ﬁnite and C1, C2 be two conﬁgurations ofBS such that C1 ‚
Y C2 (resp.,

C1
 ‚
z C2) is well deﬁned. Then ˆµBS,C1 ‚
YC2 “ ˆµBS,C1 ` ˆµBS,C2 (resp., ˆµBS,C1‚
zC2 “ ˆµBS,C1 ´

ˆµBS,C2).

Proof. One can simply check by top-down induction that for all X PBS we have
ˆµBS,C1 ‚
YC2 pXq “ ˆµBS,C1pXq ` ˆµBS,C2pXq (resp., ˆµBS,C1‚
zC2pXq “ ˆµBS,C1pXq ´ ˆµBS,C2pXq).

Second, we show that, if we allow any principal downset in the dot algebra, then we
can build any conﬁguration: this is the analogue of Fact 4.8. In fact we will use the
following stronger result:5

Lemma 5.7. Let C be a conﬁguration ofBS (for S ﬁnite), and let

AC def
“ tÓBS ptXuq | X P ÓBS pCqu.

Then we have C P ‚pACq.

Proof. By induction on the size of ÓBS pCq. The base case is when | ÓBS pCq| “ 0, which
can only happen when C is H. Then clearly C P ‚pACq as AC “ H and ‚pHq “ tHu.
For the inductive case, assume the claim is true for all C1 with | ÓBS pC1q| ď n, and
let us show it is true for C with | ÓBS pCq| “ n ` 1. Let X P C be maximal, and

consider C1 def
“ CztXu. Then | ÓBS pC1q| ď n, hence by induction hypothesis we have
C1 P ‚pAC1q. But it is clear that AC1 Ď AC, so that C1 P ‚pACq as well. Moreover,
consider C1 def
“ ÓBS ptXuqztXu. By induction hypothesis and for the same reasons we

have C1 P ‚pACq. Then C1 ‚
Y pÓBS ptXuq
 ‚
z C1q is a valid expression witnessing that C P
‚pACq.

Third, we show that all instances of the NCPD conjecture are already “full”, in the
sense that an analogous version of Proposition 4.7 automatically holds for them (whereas
we saw that Proposition 4.7 might be false for intersection lattices that are not full).
Let PDpBSq be the set of principal downsets ofBS, i.e., PDpBSq def
“ tÓBS pXq | X PBSu.
We show:

5In this lemma and its proof we correctly use the notation ÓBS ptXuq for X PBS instead of ÓBS pXq
to avoid confusion.
 18

Proposition 5.8. Let S ﬁnite and I be a conﬁguration ofBS that is a downset and T
a tree witnessing that I P ‚pPDpBSqq. Then we have multT pÓBS pXqq “ ˆµBS,I pXq for
every X PBS.

Proof. It is routine to show by (bottom-up) induction on T that, for every node n P T ,
letting Cn be the corresponding conﬁguration represented by the subtree of T rooted at n
we have that multTnpÓBS pXqq “ ˆµBS,CnpXq for every X PBS; this in particular uses the
linearity of generalized M¨obius functions under disjoint unions and subset complements.
Applying this claim to the root of T gives the claim.

Last, we establish a connection between the generalized M¨obius function of a conﬁg-
uration C and the Euler characteristic of C, that will be crucial in the next section.

Deﬁnition 5.9. Let C be a set family of ﬁnite sets. We deﬁne the Euler characteristic
of C, denoted epCq, by epCq def
“ řXPCp´1q|X|.

Proposition 5.10. Let S ﬁnite and C a conﬁguration ofBS. Then we have ˆµBS,CpXq “
p´1q|X| ˆ epCX ÒBS pXqq for every X PBS.

Proof. Deﬁne f, g :BS Ñ Z by f pXq def
“ ˆµBS,CpXq and gpXq “ 1 if X P C and 0
otherwise. Observe then that, by deﬁnition of ˆµBS,C we have gpXq “ řX 1PBS
XĎX 1 f pX 1q for

all X PBS. Then by Proposition 2.11 we have that f pXq “ řX 1PBS
XĎX 1 p´1q|X 1|´|X|gpX 1q

for all X PBS, i.e.,
 ˆµBS,CpXq “ ÿ

X 1PBS
XĎX 1
 p´1q
|X 1|´|X|gpX 1q

“ ÿ

X 1PCXÒBS pXqp´1q
|X 1|´|X|

“ p´1q
|X| ˆ ÿ

X 1PCXÒBS pXqp´1q
|X 1|

“ p´1q
|X| ˆ epCX ÒBS pXqq

for all X PBS, which is what we wanted to show.

Connections between the M¨obius function and the Euler characteristic have already
been shown, for instance see Philip Hall’s theorem [Rota, 1964, Proposition 6 and The-
orem 3]. As far as we can tell, however, the connection from Proposition 5.10 seems
new.

6. Partial result on NCPD: avoiding a given zero

In this section we present a partial result on the NCPD conjecture intuitively saying that
we can “avoid” any given non-trivial zero. We ﬁrst deﬁne what these are.

19

Deﬁnition 6.1. Let I be a downset ofBS. We deﬁne the non-trivial zeros of I, de-
noted NTZBS pIq, by
 NTZBS pIq def
“ tZ P I | ˆµBS,IpZq “ 0u.

By opposition, the trivial zeros of I are the elements Z PBSzI such that ˆµBS,I pZq “ 0
(notice that these form an upset ofBS).

Observe that if I does not have non-trivial zeros, i.e., NTZBS pIq “ H, then we have
indeed that I P ‚pNCPDBS pIqq, that is, the NCPD conjecture holds, as can be seen by
taking C “ I in Lemma 5.7. So we can focus on downsets I having as least one such
non-trivial zero.
The partial result that we show in this section is that, for any given such non-trivial
zero Z, if we are allowed to use all the non-trivial principal downsets except the one
generated by Z, then we can construct I. Formally we will prove the following:

Theorem 6.2. Let I be a downset ofBS such that NTZBS pIq is not empty, and let Z P
NTZBS pIq. Then we have I P ‚ptÓBS pXq | X P IztZuuq.

The proof reuses and extends some ideas and notions from [Monet, 2020a]. We ﬁrst
deﬁne some of these notions in Section 6.1, in particular the notion of adjacent pairs and
certain equivalence classes. In Section 6.2 we show what we call the lifting lemma, and
show adjacent pairs can be simulated with principal downsets. We combine everything
in Section 6.3 to prove Theorem 6.2.

6.1. Adjacent pairs

Deﬁnition 6.3. An adjacent pair ofBS is a conﬁguration P of the form tX, X
 ‚
z txuu
(with X PBS and x P X).

Deﬁnition 6.4. Let A be a set of adjacent pairs ofBS, and let C, C1 be two conﬁgurations
ofBS. We then write C „„„⊲
+ A C1 when there exists an adjacent pair P P A such that
C1 “ C ‚
Y P. Similarly we write C „„„⊲
-A C1 whenever C1 „„„⊲
+A C (i.e., when there exists P P A

such that C1 “ C
 ‚
z P), and write C „„„⊲
˘ A C1 when C „„„⊲
+A C1 or C „„„⊲
-A C1. Observe that „„„⊲
˘A

is symmetric. We write „„„⊲
˘A ˚ the reﬂexive transitive closure of „„„⊲
˘A , and write »A the
induced equivalence relation.

In other words, we have C »A C1 when we can go from C to C1 by iteratively (1)
adding an adjacent pair from A to the current conﬁguration if the pair is disjoint from
the conﬁguration; or (2) removing an adjacent pair from A to the current conﬁguration
if the pair was included in the conﬁguration.

Deﬁnition 6.5. For a subset G ofBS, deﬁne the set of allowed adjacent pairs ofBS
relative to G, denoted APBS pGq, by

APBS pGq def
“ tP | P is an adjacent pair ofBS and P Ď Gu.

20

Deﬁnition 6.6. For S ﬁnite, deﬁne the undirected graph GS with vertex set 2S whose
edges are all adjacent pairs ofBS. A subset G ofBS is connected if it is a connected
set of nodes in GS.

The goal of this section is to establish the following proposition:

Proposition 6.7. Let G be a connected subset ofBS, and C1, C2 two conﬁgurations that
are included in G. We have epC1q “ epC2q if and only if C1 »APBS pGq C2.

This result already appears in [Monet, 2020a, Proposition 6.1], but only when G is
the whole Boolean lattice, i.e., when6 we have G “ 2S. Observe that the “if” di-
rection in Proposition 6.7 is trivial, since adding or removing an adjacent pair (with
disjoint union or subset complement) does not modify the Euler characteristic. Hence
we need to prove the “only if” direction. To this end, we reproduce the following lemma
from [Monet, 2020a]:

Lemma 6.8 (Lemma 5.10 of [Monet, 2020a]). Let C be a conﬁguration ofBS, and
X ‰ X 1 be two subsets of S such that there is a simple path P of the form X “
X0 ´ ¨ ¨ ¨ ´ Xn`1 “ X 1 from X to X 1 in GS with n ě 0 and Xi R C for 1 ď i ď n. Then
we have the following:

Erasing. If p´1q|X| ‰ p´1q|X 1| (i.e., n is even) and tX, X 1u Ď C then, deﬁning C1 by

C1 def
“ CztX, X 1u, we have C „„„„„„„„⊲

˘APBS pP q ˚ C1. We say that we go from C to C1 by
erasing X and X 1.

Teleporting. If p´1q|X| “ p´1q|X 1| (i.e., n is odd) and X P C and X 1 R C then, deﬁning C1

by C1 def
“ pCztXuq Y tX 1u, we have C „„„„„„„„⊲

˘APBS pP q ˚ C1. We say that we go from C to C1

by teleporting X to X 1.

Proof. We only explain the erasing part, as teleporting works similarly. Let n “ 2i.
For 0 ď j ă i, do the following: add the adjacent pair tX2j`1, X2j`2u and remove the
adjacent pair tX2j, X2j`1u. Finally, remove the adjacent pair tX2i, X2i`1u.

Teleporting is illustrated in Figure 5 (adapted from [Monet, 2020a]).
We will also reuse the fetching lemma from [Monet, 2020a], extending it to connected
subsets ofBS (instead of the full Boolean lattice). Given the right circumstances, this
lemma fetches for us two sets X, X 1 P C and a suitable path so that we can erase X and
X 1. Formally:

Lemma 6.9 (Fetching lemma, slightly extending Lemma 5.11 of [Monet, 2020a]). Let G
be a subset ofBS and C Ď G a conﬁguration such that |C| ‰ |epCq|. Then there exist
X, X 1 P C with p´1q|X| ‰ p´1q|X 1| and a simple path X “ X0 ´ ¨ ¨ ¨ ´ Xn`1 “ X 1 from X
to X 1 in GS (hence with n even) with all nodes in this path being in G such that Xi R C
for 1 ď i ď n.

6We will actually only use this result when G is a downset ofBS, but we still prove this more general
version for completeness and because it is not much more complicated.

21

X0 X1 X2 X3 X4

X0 X1 X2 X3 X4

X0 X1 X2 X3 X4

X0 X1 X2 X3 X4

X0 X1 X2 X3 X4

„„„„„„„„⊲

´APBS pP q

„„„„„„„„⊲

`APBS pP q

„„„„„„„„⊲

´APBS pP q

„„„„„„„„⊲

`APBS pP q
X0

X0 X1 X2

X2

X2 X3 X4

X4

Figure 5: Imagine that the path at the top occurs in GS for some conﬁguration C ofBS
(in orange), and let P “ tX0, . . . , X4u. The consecutive orange conﬁgurations
ofBS are obtained by single steps of the transformation. The total transfor-
mation illustrates what is called teleporting in Lemma 6.8: we go from C to C1

in the bottom path by teleporting X1 to X4.

Proof. Since |C| ‰ |epCq|, there exist X 2, X 3 P C with p´1q|X 2| ‰ p´1q|X 3|. Let X 2 “
X 2
0 ´ ¨ ¨ ¨ ´ X 2
m`1 “ X 3 be an arbitrary simple path from X 2 to X 3 in GS with all
nodes being in G (such a path clearly exists because G is a connected subset of GS).
Now, let k1 def
“ maxp0 ď j ď m | p´1q
|X 2
j | “ p´1q|X 2| and X 2
j P Cq, and then let

k2 def
“ minpk1 ă j ď m ` 1 | p´1q
|X 2
j | “ p´1q|X 3| and X 2
j P Cq, which are well-deﬁned.
Then we can take X to be X 2
k1 and X 1 to be X 2
k2, which satisfy the desired property.

With these in place we are ready to prove Proposition 6.7.

Proof of Proposition 6.7. As mentioned above, we only need to prove the “only if” part
of the statement. Starting from C1, we repeatedly use the fetching lemma and Erasing
until we obtain a conﬁguration C1
1 Ď G such that C1
1 »APBS pGq C1 and |C1
1| “ epC1
1q. We
do the same with C2, obtaining C1
2 Ď G with C1
2 »APBS pGq C2 and |C1
2| “ epC1
2q. If C1
1 “ C1
2
we are done. Otherwise, let n def
“ |C1
1zC1
2|, which is ą 0 because |C1
1| “ |C1
2|. We build
by induction a sequence of conﬁgurations C1
1 “ C2
0 , . . . , C2
n “ C1
2 that are all included
in G and that satisfy (1) C2
i »APBS pGq C2
i`1 for all 0 ď i ď n ´ 1 and (2) |C2
i | “ epC2
i q
and |C2
i zC1
2| “ n ´ i for all 0 ď i ď n. It is clear that this indeed implies the claim.
As C2
0 satisﬁes condition (2), it is enough to explain how to build C2
i`1 from C2
i for i ă n,
and then to argue that the C2
n from this construction is indeed equal to C1
2. We have
|C2
i zC1
2| “ n ´ i ą 1 by induction hypothesis, so there exists X 1 P C2
i zC1
2 and X 2 P C1
2zC2
i
(because |C2
i | “ epC2
i q “ epC1
1q “ |C1
1| “ |C1
2|). Let X 1 “ X 1
0 ´ ¨ ¨ ¨ ´ X 1
m`1 “ X 2 be
an arbitrary simple path from X 1 to X 2 in GS with all nodes being in G (such a path

22

exists because G is a connected subset of GS, and m is odd and ě 1). Observe that
all nodes X 1
k with k odd are not in C2
i Y C1
2, because |C2
i | “ epC2
i q| and |C1
2| “ epC1
2q .

Now, let k1 def
“ maxp0 ď j ď m | X 1
j P C2
i zC1
2q, and then let k2 def
“ minpk1 ă j ď m ` 1 |

X 1
j P C1
2zC2
i q, which are well-deﬁned. Deﬁne C2
i`1 def
“ C2
i ztXk1u Y tXk2u. Notice that C2
i`1
satisﬁes condition (2), so all we need to show is that C2
i »APBS pGq C2
i`1. We know the
following: for a node X 1
k with k1 ă k ă k2, if k is odd then X 1
k R C2
i Y C1
2, and if k is even
then either X 1
k P C2
i X C1
2 or X 1
k R C2
i Y C1
2. If there is no node X 1
k with k1 ă k ă k2, k even
such that X 1
k P C2
i , then we can simply use Lemma 6.8 to teleport Xk1 to Xk2 and we are
done. Otherwise, let X 1
ℓ1, . . . , X 1
ℓm with m ě 1 be all the nodes with k1 ă ℓp ă k2 even
that are in C2
i , in order, i.e., ℓ1 ă . . . ă ℓm. Then we can successively teleport X 1
ℓm to
X 1
k2, X 1
ℓm´1 to X 1
ℓm, and so on, until we teleport X 1
ℓ1 to X 1
ℓ2 and ﬁnally we teleport X 1
k1
to X 1
ℓ1, thus obtaining C2
i`1 as promised. It is then clear that C2
n is C1
2, because we
have |C2
nzC1
2| “ 0 by condition (2), and |C2
n| “ |C1
2| by construction. This concludes the
proof.

6.2. Lifting lemma and simulating adjacent pairs with principal downsets

A simple, yet important component of the proof of Theorem 6.2 will be what we call the
lifting lemma. We ﬁrst state and prove it before giving intuition.

Lemma 6.10 (Lifting lemma). Let Z PBS and A Ď ÒBS pZq. Let IA def
“ tÓBS pXq X

ÒBS pZq | X P Au and I 1
A def
“ tÓBS pXq | X P Au. Then, for any C P ‚pIAq, deﬁning the
conﬁguration liftBS,ZpCq def
“ tX PBS | X Y Z P Cu,

we have that liftBS,ZpCq P ‚pI 1
Aq.

Proof. This is shown by induction on C P ‚pIAq. The ﬁrst base case is when C “ H,
but then we have liftBS,ZpCq “ H as well, which is in ‚pI 1
Aq by deﬁnition. The
second base case is when C “ ÓBS pXq X ÒBS pZq for some X in A. In this case, it
is easy to show that liftBS,ZpCq “ ÓBS pXq; this uses in particular that set union
is the join operation of the latticeBS. But then this implies liftBS,ZpCq P ‚pI 1
Aq

indeed. For the inductive case, we focus on ‚
Y as
 ‚
z works similarly. Let C1, C2 P ‚pIAq
such that C def
“ C1 ‚
Y C2 is well-deﬁned, and let us show that liftBS,ZpCq P ‚pI 1
Aq.
By induction hypothesis we have that liftBS,Z pC1q P ‚pI 1
Aq and liftBS,ZpC2q P ‚pI 1
Aq.
Now, observe that liftBS,ZpC1q ‚
Y liftBS,ZpC2q is well deﬁned, and furthermore that we
have liftBS ,ZpC1 ‚
Y C2q “ liftBS,ZpC1q ‚
Y liftBS,ZpC2q. This implies liftBS,ZpCq P
‚pI 1
Aq as wanted, and concludes the proof.

The intuition behind the lifting lemma is the following. Notice that ÒBS pZq is iso-

morphic to the Boolean latticeBS1 with S1 def
“ SzZ. Consider a witnessing tree T 1

representing a conﬁguration C ofBS1 that is formed from principal downsets ofBS1.
Consider the “lifted tree” T 1 that is obtained from T by replacing every leaf of T of the

23

form ÓBS1 pXq for X Ď S1 by the principal downset ofBS that is ÓBS pX Y Zq. The lift-
ing lemma says that the obtained tree T 1 is valid (i.e., the internal nodes are well-deﬁned
disjoint unions and subset complements) and that it represents the conﬁguration ofBS
that is liftBS ,ZpCq.
This lemma will have two uses in the proof of Theorem 6.2. The ﬁrst is that said proof
will work by ﬁrst constructing a conﬁguration in the principal upset generated by the
non-trivial zero Z that is ﬁxed in the theorem statement, and then this lemma will be
used to “lift” the result to the whole Boolean latticeBS. The second use of this lemma
is that it helps us show that adjacent pairs can be simulated by principal downsets, while
avoiding the principal downset that is at the bottom. We explain this second use in the
following lemma.

Lemma 6.11. Let P “ tX, X
 ‚
z txuu be an adjacent pair ofBS. Then we have P P
‚ptÓBS pY q | H Ĺ Y Ď Xuq.

In this statement, pay attention that the principal downset ÓBS pHq is not in the base
set of the dot-algebra.7 In other words, we are allowed to use any principal downset that
is generated by an element that is below X and strictly above H inBS. The reason is
that in the proof of Theorem 6.2, Z will correspond to H here and it generates the only
downset we are not allowed to use. We now prove Lemma 6.11.

Proof of Lemma 6.11. Clearly, it suﬃces to show the claim in the case that X “ S. To

this end, it is enough to show that we haveBS
 ‚
z P P ‚ptÓBS pY q | H Ĺ Y Ď Xuq:

indeed we can then obtain P as ÓBS pSq
 ‚
z pBS
 ‚
z Pq. Let C1 be the conﬁguration tX PBS | txu Ď X Ĺ Su. Using Lemma 5.7 appropriately we have that C1 P ‚ptÓBS pY q X
ÒBS ptxuq | txu Ď Y Ĺ Suq. We now use the lifting lemma (invoked with Z “ txu)
to obtain that liftBS,txupC1q P ‚ptÓBS pY q | txu Ď Y Ĺ Suq, hence in particular
liftBS,txupC1q P ‚ptÓBS pY q | H Ĺ Y Ď Suq. But notice that liftBS,txupC1q is actuallyBSzP, which concludes the proof.

6.3. Proof of Theorem 6.2

We now prove Theorem 6.2. Fix the ﬁnite set S and the conﬁguration I that is a
downset ofBS such that NTZBS pIq is not empty, and let Z P NTZBS pIq. By Proposi-
tion 5.10 we have ˆµBS,IpZq “ p´1q|Z| ˆ epI X ÒBS pZqq, therefore epI X ÒBS pZqq “ 0.
We now instantiate Proposition 6.7 with G “ C1 “ I X ÒBS pZq and C2 “ H to ob-
tain I X ÒBS pZq »APBS pIXÒBS pZqq H. This gives us a left-linear tree T for I X ÒBS pZq
with disjoint unions and subset complements and whose leaves are adjacent pairs from
APBS pI XÒBS pZqq. Next we use Lemma 6.11 to simulate, in ÒBS pZq, each such adjacent
pair using the principal downsets of ÒBS pZq, except the one generated by Z (thanks
to the fact that H Ĺ Y in the statement of the lemma). Therefore, we obtain that
I X ÒBS pZq P ‚ptÓBS pXq X ÒBS pZq | X P I, Z Ĺ Xuq. We now use Lemma 6.10
to obtain that liftBS,ZpI X ÒBS pZqq P ‚ptÓBS pXq | X P IztZuuq. Notice that

7Recall that to alleviate the notation we write ÓBS pHq to mean ÓBS ptHuq, which is then tHu.

24

liftBS,ZpI X ÒBS pZqq X ÒBS pZq “ I X ÒBS pZq, i.e., restricted to ÒBS pZq we have
the correct conﬁguration, and we now only need to “ﬁx” what is outside.
Now let C1
1 “ liftBS,Z pI X ÒBS pZqqzpI X ÒBS pZqq and C1
2 “ IzpI X ÒBS pZqq. We use
Lemma 5.7 to obtain that C1
1 is in ‚ptÓBS pXq | X P C1
1uq, and likewise for C1
2. Observe
that C1
1 and C1
2 only consist of elements outside of ÒBS pZqq, in particular C1
1, C1
2 Ď IztZu,
so that C1
1 and C1
2 are in ‚ptÓBS pXq | X P IztZuuq. Finally we can obtain I with the

expression pliftBS ,ZpI X ÒBS pZqq
 ‚
z C1
1q ‚
Y C1
2, which is in ‚ptÓBS pXq | X P IztZuuq by
what precedes. This concludes the proof.

7. Extensions, Variants and Counterexample Search

In this section we present a generalization of Theorem 6.2 that we believe to be true,
present variants of the conjectures, and talk about our experimental search for coun-
terexamples.

Extension of Theorem 6.2. We sketch here a proposed generalization that allows us
to avoid not one single zero, but subsets of zeros while requiring that the lattice has a
certain structure. We ﬁrst deﬁne a few notions.

Deﬁnition 7.1. Let I be a downset ofBS. For X PBS, the non-trivial covering zeros
of X relative to I are

NTCZBS,IpXq def
“ tZ P NTZBS pIq | X Ĺ Z and there is no Z 1 P NTZBS pIq s.t. X Ĺ Z 1 Ĺ Zu.

In other words, NTCZBS,IpXq simply consists of the minimal non-trivial zeros of I that
are strictly above X. Observe that we have NTCZBS,IpXq “ H whenever X R I. We
now deﬁne k-decomposable downsets.

Deﬁnition 7.2. A conﬁguration I ofBS that is a downset is called k-decomposable if
for every X PBS we have |NTCZBS,IpXq| ď k.

This intuitively means that, in every upset, there are at most two non-trivial covering
zeroes. We believe that the following is true, but have not completely formalized the
proof.

Conjecture 7.3. For every ﬁnite S, for every conﬁguration I ofBS that is a 2-
decomposable downset ofBS, we have that I P ‚pNCPDBS pIqq.

Proof sketch. For an element X PBS, let IX def
“ tÓBS pY q X ÒBS pXq | Y P ÒBS pXq,
ˆµBS,IpY q ‰ 0u. The idea of the proof would be to show by top-down induction onBS
that for every X PBS, we have I X ÒBS pXq P ‚pIX q. Applying this claim to X “ H
yields the desired result. To show this, we use similar tools to those developed for the
proof of Theorem 6.2, extended with an accounting of Euler characteristics of diverse
sets of conﬁgurations. It does not seem that the proposed proof would directly generalize
to the general case, or indeed to 3-decomposable conﬁgurations.

25

Strengthenings. We present here two possible orthogonal ways in which we can
strengthen the conjecture; we do not know whether the stronger conjectures are true,
nor whether they are equivalent to the original conjecture.
First, in view of Proposition 4.7, we could require that the non-trivial intersections
are only used positively or only negatively depending on the sign of their M¨obius value.
Indeed, Proposition 4.7 implies that, on tight intersection lattices, the non-trivial inter-
sections have total multiplicity equal to their M¨obius value, but they may be used both
positively and negatively. Likewise, in view of Proposition 5.8, we could require that the
principal downsets are only used positively and negatively.
Second, we do not know if the witnessing trees can be required to be left-linear, i.e.,
whether we can obtain ˆ1 (for the NCI conjecture) or the desired conﬁguration (for the
NCPD conjecture) by a series of operations where, at each step, we add a (disjoint) non-
trivial intersection (or principal downset), or subtract one (which must be a subset). For
instance, this formulation does not allow us to express a disjoint union of two conﬁgura-
tions themselves obtained with more complex witnessing trees. This stronger conjecture
is the topic of the question asked in [Amarilli, 2019] (up to replacing upsets by downsets
and to working in general lattices instead of only on Boolean lattices). This question also
explains why the conjecture is false if asked about general DAGs (instead of lattices),
and shows that the conjecture can be true for so-called crown-free lattices.
We note that the construction for the proof of Theorem 6.2 (or the one that we have
in mind for Conjecture 7.3) does not satisfy either of these strengthenings. However, the
proof of Fact 4.8 can be adjusted to satisfy the left-linear condition.

Counterexample search. We have implemented a search for counterexamples of the NCI
conjecture. We consider Sperner families [Monet, 2020b], which give all sets of subsets
of a base set of n elements that are non-equivalent (i.e., that are not the same up to
permuting the elements). We have checked in a brute-force fashion that the conjecture
holds up to n “ 5, i.e., on all intersection lattices such that ˆ1 has cardinality at most 5.
Unfortunately, already for n “ 6 there are intersection lattices that are too large for the
computation to ﬁnish suﬃciently quickly. We also generated random intersection lattices
over larger sets of elements, but could not ﬁnd a counterexample (assuming that our code
is correct). The code checks the strong version of the NCI conjecture in the previous
terminology, i.e., it searches for left-linear trees and requires the non-trivial intersections
to be used precisely with the right polarity. The code is available as-is [Amarilli, 2023].
We have also improved the implementation to search for solutions on each lattice using
a SAT-solver rather than a brute-force search: this speeds up the computation but also
did not yield any counterexample.
We had also implemented, earlier, a search for counterexamples of an alternative
phrasing of the NCPD conjecture: see [Amarilli et al., 2020]. This also illustrates that
the NCPD conjecture is false if the conﬁguration to reach is not a downset; see Figure 4
of [Amarilli et al., 2020] (up to reversing directions, i.e., considering downsets instead of
upsets).
 26

References

[Amarilli, 2019] Amarilli, A. (2019). Lighting up all elements of a poset
by toggling upsets. Theoretical Computer Science Stack Exchange.
URL:https://cstheory.stackexchange.com/q/45679 (version: 2019-10-12).

[Amarilli, 2023] Amarilli, A. (2023). Code. https://gitlab.com/Gruyere/mobius-unions-differences/-

[Amarilli et al., 2020] Amarilli, A., Jachiet, L., and Monet, M. (2020). Which sets can
be expressed as disjoint union and subset complement without m¨obius cancellations?
https://mikael-monet.net/share/note.pdf. Unpublished.

[Hirsch and McLean, 2017] Hirsch, R. and McLean, B. (2017). Disjoint-union partial
algebras. Log. Methods Comput. Sci., 13(2).

[Monet, 2020a] Monet, M. (2020a). Solving a special case of the intensional vs exten-
sional conjecture in probabilistic databases. In PODS.

[Monet, 2020b] Monet, M. (2020b). Sperner families generator.
https://gitlab.com/Gruyere/sperner-families-generator.

[Rota, 1964] Rota, G.-C. (1964). On the foundations of combinatorial theory I. Theory
of M¨obius functions. Zeitschrift f¨ur Wahrscheinlichkeitstheorie und verwandte Gebiete,
2(4).

[Stanley, 2011] Stanley, R. P. (2011). Enumerative Combinatorics: Volume 1. 2nd
edition.
 27

A. Proofs for Section 3 (The Non-Cancelling Intersections
Conjecture)

We show in this section that the NCI and NCU conjectures are equivalent. We only sketch
the proofs as details are easy to ﬁll.

Deﬁnition A.1. Let F be a set family. For S P 2
Ť F , let dualF pSq def
“ p
Ť FqzS, and
for T Ď F let dualF pT q def
“ tdualF pXq | X P T u.

Observe then that F is non-trivial if and only if dualF pFq is non-co-trivial.

Fact A.2. Let L “LF be an intersection lattice, and let L2 be the union latticeUdualF pF q
of dualF pFq, but with the order reversed. Then we have L » L2.

Proof sketch. One can check that the function that sends ˆ1L to ˆ1L2 (“ ˆ0UdualF pF q)
and ST “ Ş T for T Ď F, T ‰ H to RdualF pT q “ Ť dualF pT q is an isomorphism
between L and L2. This uses the following two simple facts:

1. For any sets A, B, C with B Y C Ď A we have AzB Ď AzC if and only if C Ď B.

2. For a set A and set family T we have ŞXPT AzX “ Az Ť T .

The dual version of this fact also holds, i.e., for a union lattice L “UF , letting L2 be
the intersection latticeLdualF pF q of dualF pFq but with the order reversed, we have L »
L2. (This uses point (1) above and the dual of point (2), namely, ŤXPT AzX “ Az Ş T .)
We can then show that the NCU conjecture implies the NCI conjecture as follows.
Let L “LF be an intersection lattice, and let L1 def
“UdualF pF q be the union lat-
tice of dualF pFq. Using Fact A.2 and [Rota, 1964, Proposition 3], it is routine to
show by induction on ‚pNCUpL1qq the following claim (:): for every R P ‚pNCUpL1qq
we have dualF pRq P ‚pNCIpLqq. Since the NCU conjecture holds we have ˆ0L1 P ‚pNCUpL1qq,
hence by (:) we have dualF pˆ0L1 q P ‚pNCIpLqq. But observe that ˆ0L1 “ ŞXPF dualF pXq
by deﬁnition, which is equal to Ť Fz Ť F “ H by Item (2) above. So dualF pˆ0L1q “ Ť F,
and this is ˆ1L, so indeed ˆ1L P NCIpLq.
We can show that the NCI conjecture implies the NCU conjecture in the same way,
using the dual version of Fact A.2. This completes the proof.

B. Proofs for Section 4 (Simplifying to Tight Intersection
Lattices)

Proposition 4.7. Let L be a full intersection lattice such that ˆ1 P ‚pNTIpLqq, and T a
tree witnessing this. Then we have multT pU q “ ´µLpU, ˆ1q for every U P NTIpLq.

Proof. For U P L, U ‰ ˆ1, let αU be an element of tx P ˆ1 | minLpxq “ U u. We ﬁrst
deﬁne, for each X Ď ˆ1, a function ˇµL,X : L Ñ Z, and state three useful properties of these

functions. The function ˇµL,X for X Ď ˆ1 is deﬁned by ˇµL,Xpˆ1q def
“ 0, and, for U P NTIpLq,

28

by ˇµL,XpU q def
“ 1 ´ ř U 1PL
U ĹU 1 ˇµL,XpU 1q if αU P X, and ˇµL,XpU q def
“ ´ ř U 1PL
U ĹU 1 ˇµL,XpU 1q

if αU R X.
The three properties are:

1. We have ˇµL,HpU q “ 0 for U P L.

2. For every U P NTIpLq we have ˇµL,ˆ1pU q “ ´µLpU, ˆ1q.

3. For X1, X2 Ď ˆ1 such that X1 X X2 “ H (resp., such that X2 Ď X1) we have
ˇµL,X1 ‚
YX2 “ ˇµL,X1 ` ˇµL,X2 (resp., ˇµL,X1‚
zX2 “ ˇµL,X1 ´ ˇµL,X2).

4. For U P NTIpLq and U 1 P L, the value ˇµL,U pU 1q is 1 if U 1 “ U and 0 otherwise.

These can all easily be established by top-down induction on L. Now for a node n P T ,
let Xn be the subset of ˆ1 represented by the subtree of T rooted at n. We show by bottom-
up induction on T that for every node n of T and U P NTIpLq we have multTnpU q “
ˇµL,XnpU q. This will indeed imply the result by applying it to the root of T and using
item (2), since we then have that Xn “ ˆ1. The base case, when n is a leaf of T , follows
from item (4) and item (1), while the inductive case, when n is an internal node of T ,
follows from (3).

C. Proofs for Section 5 (Alternative Formulation: Dot-Algebra
of Non-Cancelling Principal Downsets in the Boolean
Lattice)

Lemma 5.5. Let S be a ﬁnite set and let I be a downset ofBS of the form I “ ÓBS pFq

for F a non-trivial set family. For X P F let X 1 def
“ ÓBS pXq (which is 2X ), and let F 1 def
“
tX 1 | X P Fu. Note that F 1 is non-trivial as well, and let then L be its intersection
lattice. Then we have NCPDBS pIq “ NCIpLq.

Proof. Observe that ˆ1L “ I. For T Ď F, we write T 1 for the corresponding subset of F 1,
i.e., T 1 “ tX 1 | X P T u, and vice versa. For T Ď F, T ‰ H let XT def
“ Ş T . We show
that the following hold:

1. For T 1 Ď F 1, T 1 ‰ H we have ST 1 “ ÓBS pXT q.

2. Let L1 be the lattice ptXT | T Ď F, T ‰ Hu Y tˆ1L1u, ďL1q where ˆ1L1 is a fresh
element and Y ďL1 ˆ1L1 for all Y P L1 and XT1 ďL1 XT2 for T1, T2 Ď F if XT1 Ď XT2.
Then L » L1 via the isomorphism that sends ˆ1L to ˆ1L1 and ST 1 for T 1 Ď F 1, T 1 ‰ H
to XT .

3. For every Y PBS, if Y is of the form XT then ˆµBS,IpY q “ ´µLpST 1, ˆ1Lq, otherwise
ˆµBS,IpY q “ 0.
 29

Notice that Item (3) together with Item (1) implies that NCPDBS pIq “ NCIpLq, which

is what we need to prove. Item (1) follows from the chain of trivialities ST 1 def
“ Ş T 1 def
“
ŞX 1PT 1 X 1 “ ŞXPT 2X “ 2
Ş T def
“ 2XT def
“ ÓBS pXT q, and Item (2) is easy to prove using
Item (1). For Item (3), we show that ˆµBS,I is as claimed. For Y PBS, Y R I, it is clear
that ˆµBS,IpY q “ 0, by deﬁnition of ˆµBS,I and because I is a downset, so we can focus
on Y P I. We show by top-down induction on I that ˆµBS,I is as claimed on I. The base
case is when Y is a maximal element of I, i.e., Y “ X for some maximal X P F. Then we
have ˆµBS,IpY q “ 1 “ ´µLpX 1q indeed. The inductive case is when Y is not a maximal

element of I. Let TY def
“ tX P F | Y Ď Xu, which is non-empty. Notice the following
fact (:): we have Y Ď XTY , and more speciﬁcally we have Y Ď XT for T Ď F, T ‰ H
if and only if T Ď TY . We then distinguish two cases.

• The ﬁrst case is when Y “ XTY . We have ˆµBS,IpY q “ 1 ´ ř
Y ĹY 1 ˆµBS,IpY 1q by
deﬁnition. Now by what precedes, if Y 1 R I then ˆµBS,IpY 1q “ 0, and by induction
hypothesis if Y 1 is not of the form XT then ˆµBS,IpY 1q “ 0. Hence, we have
ˆµBS,IpY q “ 1 ´ ř Y ĹY 1
Y 1“XT ˆµBS,IpXT q, and the suitable T are the subsets of TY

by (:), i.e., ˆµBS,IpY q “ 1 ´ řY 1PtXT |T ĎTY uztY u ˆµBS,IpXT q. Now, by induction
hypothesis, we have ˆµBS,IpXT q “ ´µLpST 1, ˆ1Lq for all T Ď TY such that XT ‰ Y ,
therefore ˆµBS,IpY q “ 1 ` řY 1PtXT |T ĎTY uztY u µLpST 1, ˆ1Lq. Now by Item (2) this
is equal to 1 ` ř U PL
U ‰ˆ1L
ST 1
Y ĹU
 µLpU, ˆ1Lq, which is equal to ř U PL
ST 1
Y ĹU µLpU, ˆ1Lq, which is

´µLpST 1
Y q by deﬁnition. So indeed ˆµBS,IpY q “ ´µLpST 1
Y q.

• The second case is when Y ‰ XTY . Then, the nodes of I in the principal upset
of Y minus tY u consists of the nodes of I in the principal upset of XTY , and
of nodes that are not of the form XT by (:) and that are strict supersets of Y .
By induction hypothesis, the ˆµBS,I-value of the latter is zero. So ˆµBS,I pY q “
1 ´ řXTY ĎY 1 ˆµBS,IpY 1q “ 1 ´ ˆµBS,IpXTY q ´ řXTY ĹY 1 ˆµBS,IpY 1q, but by deﬁnition
of ˆµBS,I we have ˆµBS,I pXTY q “ 1 ´ řXTY ĹY 1 ˆµBS,I pY 1q, so indeed ˆµBS,IpY q “ 0.
This concludes the proof.
 30
