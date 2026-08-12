<!-- source: https://arxiv.org/pdf/1604.06554 | converted from PDF -->

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES

DEDICATED TO IRA GESSEL FOR HIS RETIREMENT

OLIVIER BERNARDI

Abstract. We establish general counting formulas and bijections for deformations
of the braid arrangement. Precisely, we consider real hyperplane arrangements such
that all the hyperplanes are of the form xi − xj = s for some integer s. Classical
examples include the braid, Catalan, Shi, semiorder and Linial arrangements, as well
as graphical arrangements. We express the number of regions of any such arrange-
ment as a signed count of decorated plane trees. The characteristic and coboundary
polynomials of these arrangements also have simple expressions in terms of these
trees.
We then focus on certain “well-behaved” deformations of the braid arrangement
that we call transitive. This includes the Catalan, Shi, semiorder and Linial ar-
rangements, as well as many other arrangements appearing in the literature. For
any transitive deformation of the braid arrangement we establish a simple bijection
between regions of the arrangement and a set of labeled plane trees deﬁned by local
conditions. This answers a question of Gessel.

1. Introduction

In this article we establish enumerative and bijective results about classical families
of hyperplane arrangements. Speciﬁcally, we consider real hyperplane arrangements
made of a ﬁnite number of hyperplanes of the form

Hi,j,s = {(x1, . . . , xn) ∈ Rn | xi − xj = s},

with i, j ∈ {1, . . . , n} and s ∈ Z. We shall call them deformations of the braid ar-
rangement. In particular, given an integer n and a ﬁnite set of integers S, the S-braid
arrangement in dimension n, denoted AS(n), is the arrangement made of the hy-
perplanes Hi,j,s for all 1 ≤ i < j ≤ n and all s ∈ S. Classical examples include
the braid, Catalan, Shi, semiorder, and Linial arrangements, which correspond to
S = {0}, {−1, 0, 1}, {0, 1}, {−1, 1}, and {1} respectively. These arrangements are
represented1 in Figure 1. We refer the reader to [34] or [41] for an introduction to the
general theory of hyperplane arrangements.

Date: June 15, 2021.
This work was partially supported by NSF grant DMS-1400859. Part of it was completed while vis-
iting the MIT in the Spring 2016. Many thanks to Ira Gessel for suggesting this problem and providing
many valuable inputs, and to Sam Hopkins and Alexander Postnikov for interesting discussions. We
are also grateful to an anonymous referee for suggesting additional references and making many other
valuable comments.
1Here and later, the arrangements are represented by drawing their intersection with the hyperplane
H0 = {(x1, . . . , xn) | x1 + . . . + xn = 0}, which is orthogonal to all the hyperplanes of any deformation
of the braid arrangement. 1arXiv:1604.06554v4  [math.CO]  12 Jun 2021
2 OLIVIER BERNARDI

x1

x2 x3
Catalan: S = {−1, 0, 1}
 x1

x2 x3
Shi: S = {0, 1}
 x1

x2 x3
Semiorder: S = {−1, 1}
 x1

x2 x3
Linial: S = {1}

x1

x2 x3
Braid: S = {0}
 Figure 1. The braid, Catalan, Shi, semiorder, and Linial arrangements
in dimension n = 3 (seen from the direction (1, 1, 1)).

There is an extensive literature on counting regions of deformations of the braid
arrangement, starting with the work of Shi [38, 39]. Important seminal results on this
enumerative question were established by Stanley [43, 40], Postnikov and Stanley [37],
and Athanasiadis [6, 5]. Since then, the subject has become quite popular among
combinatorialists, and many beautiful counting formulas and bijections were discovered
for various families of arrangements; see in particular [7, 10, 7, 11, 1, 3, 15, 23, 19, 25,
27, 26, 31] (see also Section 2 for additional references).
About a decade ago, an interesting pattern was observed by Ira Gessel. In an unpub-
lished manuscript, Gessel obtained an equation for the generating function of labeled
binary trees counted according to ascents and descents along left or right edges2. By
specializing his equation, Gessel observed (based on known results for arrangements)
that each of the ﬁve classical arrangements families AS deﬁned above (braid, Catalan,
Shi, semi-order, Linial) can be associated to a simple family BS of binary trees (char-
acterized by some ascent and descent conditions), in such a way that the regions of
AS(n) are equinumerous to trees with n nodes in BS (see Section 2.3). This opened
the question of explaining these mysterious enumerative identities between regions of
arrangements and binary trees; and attempts at answering this question were made for
instance in [15, 19].
It is the goal of this paper to explain that Gessel’s observation is not a mere coinci-
dence, but rather the manifestation of a more general theory which uniﬁes and extends
many previous results. This paper has two parts. The ﬁrst part gives enumerative
results which apply to every deformation of the braid arrangement. The second part
establishes bijections for every deformations of the braid arrangement satisfying a cer-
tain transitivity condition. In the rest of this introduction, we give a detailed outline
of the paper and a preview of our results.
In the ﬁrst part of the paper (Section 2 to 7), we deal with arbitrary deformations
of the braid arrangement. For any such arrangement in dimension n, we express the
number of regions as a signed count of some (decorated, labeled, k-ary) trees with
n nodes, that we call boxed trees. These results are given in Section 3 for the case
of S-braid arrangements (Theorem 3.4), and in Section 4 for the general case (Theo-
rem 4.2). When the arrangement satisfy the transitivity condition, our counting result
simpliﬁes greatly and the regions are shown to be equinumerous to a family of (labeled,
plane) trees satisfying certain ascent and descent conditions (Theorems 3.8 and 4.6).

2Gessel’s result was then rederived in two diﬀerent ways by Kalikow [28] and Drake [17].

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 3

In Section 5, we generalize the previous counting results by expressing the character-
istic polynomial and coboundary polynomial (equivalently, Tutte polynomial) of any
deformation of the braid arrangement in terms of boxed trees (Theorem 5.2). In Sec-
tion 6, we use the preceding expressions in terms of boxed trees in order to establish
equations for the generating function of the number of regions, and more generally for
the generating function of coboundary polynomials. We thereby recover and extend
many known results.
All the proofs for our counting results are gathered in Section 7. The proof is
inspired by statistical mechanics considerations (although some of the arguments can
alternately be interpreted in light of the ﬁnite ﬁeld method), and has three steps which
could informally be described as follows:
• at the ﬁrst step (Lemma 7.1) we express the coboundary polynomials of the
arrangements as a signed count of some decorated graphs (directly encoding
the central subarrangements),
• at the second step (Lemma 7.3) we express the generating function of these
decorated graphs in terms of a 1-dimensional gas model (by using a version of
Mayers’ theory of cluster integrals),
• at the third step (Lemma 7.5) we rearrange the information about the gas
model conﬁgurations in order to encode them in terms of boxed trees.
In the second part of the paper (Section 8), we establish bijections for regions of
transitive deformations of the braid arrangement. These are arrangements made up
of hyperplanes Hi,j,s, where the triples (i, j, s) satisfy certain conditions (see Deﬁni-
tion 4.3). Examples of transitive arrangements include the S-braid arrangements for
S ⊆ {−1, 0, 1}, or S an interval containing 1, and the G-Shi arrangement for any
graph G. As mentioned earlier, for transitive arrangements our enumerative result
simpliﬁes and the regions are found to be equinumerous to some simple families of
(labeled, plane) trees. In Section 8 we establish, for every transitive arrangement, a
direct bijection between the regions of the arrangement and the corresponding family
of trees (Theorem 8.8). Our bijection is surprising explicit: given a tree it is very
simple to determine all the linear inequalities that deﬁne the corresponding region of
the arrangement. In order to illustrate this fact, we now present the bijection in the
case of the Linial arrangement, which is illustrated in Figure 2.

Example 1.1. The regions of the Linial arrangement A{1}(n) are in bijection with the
set T{1}(n) of binary trees with n labeled node satisfying the following condition: for
all node u ∈ [n] having at least one child which is a node, the rightmost such child v is
such that v < u.
The bijection Ψ associates to any tree T in T{1}(n), the region ρ(T ) of A{1}(n) made
of the points (x1, . . . , xn) satisfying the following inequalities for all 1 ≤ i < j ≤ n:
xi − xj < 1 if and only if either drift(i) ≤ drift(j) or drift(i) = drift(j) + 1 and i
appears before j in the postﬁx order of T , where drift(v) is the number of ancestors of
v (including v) which are right-children. See Figure 2 for the case n = 3.

In the case of the Catalan arrangement A{−1,0,1}(n) (and the generalization A[−m..m](n))
our bijection builds on a classical construction. In the case of the Shi arrangement
A{0,1}(n) (and the generalization A[−m+1..m](n)) our bijection is a close relative to a
bijection of Athanasiadis and Linusson [11]; see Section 9.1. But already in the case

4 OLIVIER BERNARDI
x1
 x3x2

u v
) u > v

and

u ) u > v
v
 2

(a) (b)

3

1 2
 1 2 3

3 12
1
 3
 3 2 1

3
2 1
3 2 1

Figure 2. (a) The condition deﬁning the trees in T{1}(n). (b) The
bijection Ψ between the regions of the Linial arrangement A{1}(3) and
the trees in T{1}(3).

of the Linial arrangement A{1}(n), no direct bijection was known between the regions
of A{1}(n) and other combinatorial objects3 (although several families of trees where
known to be equinumerous to the regions of A{1}(n) [37, 36, 35]). We give short direct
proofs of our bijective results in Section 8.2 in the case of the Catalan, Shi, semiorder
and Linial arrangements. However, in the general case, we only prove surjectivity of
our mapping and conclude to bijectivity by invoking the counting results established
in the ﬁrst part of the paper.
In Section 9, we explain the relation between the trees described in Example 1.1 and
the local binary search trees which were known to be equinumerous to the regions of
A{1}(n), and we conclude with some remarks and open questions.

2. Definitions and known results

In this section we set our notation about arrangements and trees, and we recall some
known counting results for the regions of the deformations of the braid arrangement.

3The bijections in [15, 19] are not deﬁned on the regions themselves, but rather on some combina-
torial objects, called gain graphs without broken circuit, which are known to be equinumerous to the
regions by a non-bijective argument (Zaslavsky formula [46] allows to express the number of regions as
a signed count of gain graphs, and after a suitable sign-reversing involution, one is left with the gain
graphs without broken circuit).

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 5

2.1. Basic deﬁnitions.
A real hyperplane arrangement in dimension n is a set A of aﬃne hyperplanes of Rn. For
instance, the braid arrangement A{0}(n) is the set {Hi,j,0}1≤i<j≤n of (n
2) hyperplanes.

The regions of A are connected components of Rn \ ⋃

H∈A H. We denote by rA the

number of regions. For instance, it is easy to see that rA{0}(n) = n!.
We denote N = {0, 1, 2, . . .}. For a, b ∈ Z, we denote [a..b] = {i ∈ Z | a ≤ i ≤ b},
and [b] = [1..b]. For a set S, we denote by |S| the cardinality. For a ring R, we denote
by R[t] and R[[t]] respectively the set of polynomials and formal power series in t with
coeﬃcients in R. We extend the notation to several variables so that R[y][[t1, t2]] is the
set of formal power series in t1, t2 with coeﬃcients in R[y]. For G(t) ∈ R[[t]], we denote
by [tk]G(t) the coeﬃcient of tk in G.

2.2. Labeled plane trees.
A tree is a ﬁnite connected acyclic graph. A rooted plane tree is a tree with a vertex
distinguished as the root, together with an ordering of the children of each vertex. A
vertex in a rooted plane tree is a leaf if it has no children, and a node otherwise. We
think of the children of a node u of a rooted plane tree as being “ordered from left
to right”, and we adopt this convention in all our ﬁgures. For a child v of u we call
left siblings of v the children of u (including leaves) which are on the left of v, that is,
smaller than v in the ordering of the children of u.
We denote by T the set of rooted plane trees with labeled nodes (if the tree has n
nodes, then the nodes have distinct labels in [n], while the leaves are not labeled). We
denote by T (m) the set of (m + 1)-ary trees in T (i.e. the trees such that every node
has m + 1 children). We also denote by T (m)(n) the set of trees with n nodes in T (m).
A tree in T (2)(13) is represented in Figure 3(a). For a non-root node v of T ∈ T , we
denote by parent(v) the parent of v, and lsib(v) the number of left-siblings of v. We
compare nodes of T according to their labels, so that u < v means that the label of u
is less than the label of v.
 3
 6
 8

41

5

2

1
 7 4

12

13

(b)
 11
 9
 10

3
 6
 8

41

5

2

1
 7 4

12

13

(a)
 11
 9
 10

Figure 3. (a) A (rooted plane node-labeled) tree in T (2)(13). (b) A
S-boxed tree for S = {−1, 2} (note for instance that −1 ∈ S imposes
that if a box contains both a node u and its middle child v, then u > v).

6 OLIVIER BERNARDI

2.3. Known counting results about deformed braid arrangements.
As mentioned in the introduction, it has been observed by Gessel, that for every set
S ⊆ {−1, 0, 1}, the regions of the S-braid arrangement AS(n) are equinumerous to a
certain family of trees in T (1)(n). Up to symmetry, we only need to consider the braid,
Catalan, Shi, semiorder, and Linial arrangements, which are represented in Figure 1.
We now describe the corresponding families of trees (see Figure 4). A non-root node v
of a tree T ∈ T (1) is called left node (resp. right node) if lsib(v) = 0 (resp. lsib(v) = 1).
Here are the identities that Gessel observed (based on known counting results about
hyperplane arrangements, and a new formula he established for trees in T (1)(n) counted
according to the number of left and right ascents and descents):

• The regions of the Catalan arrangement A{−1,0,1}(n) are equinumerous to the
trees in T (1)(n).
• The regions of the Shi arrangement A{0,1}(n) are equinumerous to the trees in
T (1)(n) such that
(i) for every right node v, parent(v) > v.
• The regions of the semiorder arrangement A{−1,1} are equinumerous to the
trees in T (1)(n) such that
(ii) for every left node v, if the right-sibling of v is a leaf then parent(v) > v.
• The regions of the Linial arrangement A{1}(n) are equinumerous to the trees
in T (1)(n) such that
(iii) for every left node v, parent(v) > v, and for every right node v, parent(v) <
v.

Based on these observations, Gessel raised the question of ﬁnding a uniform, possibly
bijective, explanation of these ﬁve correspondences between arrangements and binary
trees (see [20] or [23, Section 1]). It is the goal of this paper to provide such an
explanation (and more). Let us mention however that the family of trees that will
appear in the framework of the current paper for the Linial arrangement is not given
by the Condition (iii), but instead by the Condition (iii’) represented in Figure 4. The
bijective link between Conditions (iii) and (iii’) is explained in Section 9.2. In fact,
Condition (iii’) is simply the combination of Conditions (i) and (ii). The fact that the
family of trees associated to the intersection A{1}(n) = A{0,1}(n) ∩ A{−1,1}(n) is the
intersection of the family of trees associated to A{0,1}(n) and A{−1,1}(n) is an instance
of a general feature of the theory developed in the present paper (see Remark 3.10).
Let us now recall the relevant references for the identities observed above, and some
natural generalizations. First, observe that T (1)(n) has cardinality n!Cat(n)! = (2n)!
(n+1)! ,
because there are Cat(n) binary trees with n nodes and n! ways of labeling their nodes.
More generally, T (m)(n) has cardinality ((m+1)n)!
(mn+1)! . On the other hand, it is classical

that the m-Catalan arrangement A[−m..m](n) has ((m+1)n)!
(mn+1)! regions (see e.g. [43, Section
4]). We will recall a bijective proof of this fact in Section 8.1.
Next, observe that the number of trees in T (1)(n) satisfying Condition (i) is (n+1)n−1

because these trees are easily seen to be in bijection with Cayley trees with n+1 vertices.
The fact that the number of regions of the Shi arrangement A{0,1}(n) is also (n + 1)n−1

was ﬁrst established by Shi [38]. In fact, Shi further showed that for all m the number

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 7u v u
v

(i) (ii) (iii)

) u > v) u > v u v
) u > v u ) u < v
 (iii')=(i)+(ii)

vand u v
) u > v u ) u > v
vand

Figure 4. The conditions (i), (ii), (iii) appearing in the literature for
the classes of trees equinumerous to the regions of the Shi, semiorder and
Linial arrangements. The characterization (iii’) proved in this paper for
the Linial arrangement appears to be new (see Section 9.2 for a bijection
between (iii) and (iii’)). Nodes are represented by labeled discs, while
leaves are represented by black dots (here, the nature of some vertices
is left unspeciﬁed).

of regions of the m-Shi arrangement A[−m+1..m](n) is (mn + 1)n−1, which is the number
of m-parking functions of size n. Since then, at least two distinct bijective proofs of
this fact have been given [11, 40], besides non-bijective proofs [37, 15, 9]. We discuss
these bijections further in Section 9.1. As we will see, (mn + 1)n−1 is also the number
of trees in T (m)(n) such that if a node v is the right-most child of a node u, then u > v
(this generalizes (i)).
The identity between the regions of the semiorder arrangement and the trees in
T (1)(n) satisfying Condition (ii) is equivalent to a result of Chandon [14]. More gener-
ally, the m-semiorder arrangement A[−m..m]\{0}(n) has regions equinumerous to trees
in T (m)(n) such that if a node v is the leftmost child of a node u, and all its siblings are
leaves, then u > v (this generalizes (ii)). This fact is easily deduced from the generating
function equation given in [37, Theorem 7.1].
Lastly, the identity between the regions of the Linial arrangement and the counting
sequence of the trees in T (1)(n) satisfying (iii) was conjectured by Linial and Ravid, and
proved in [37] and independently in [6] by equating two generating functions. However,
as mentioned above, the family of trees which appear naturally in our framework are
characterized by Condition (iii’) instead of Condition (iii). More generally, the m-
Linial arrangement A[−m+1..m]\{0}(n) has regions equinumerous to the subset of trees
in T (m)(n) such that if a node v is the right-most child of a node u, then u > v, and
moreover, if a node v is the leftmost child of a node u, and all its siblings are leaves,
then u > v (this generalizes (iii’)).
Although we cannot give an exhaustive bibliography about the enumerative study of
deformations of the braid arrangement, we should mention a few additional references
which are relevant to the present article. Formulas for the number of regions of several
additional deformations of the braid arrangements (for instance A[−ℓ..m](n) for ℓ ≥
−1) are given in [37]. The characteristic and coboundary polynomials of some of the
arrangements above have been computed in [9, 1]. In a diﬀerent direction, several
deformations of the braid arrangements associated to a graph G = ([n], E) have been
considered in the literature. The most classical is the G-graphical arrangement made
of the hyperplanes Hi,j,0, for all {i, j} ∈ E. Another important example is the G-
Shi arrangement considered for instance in [3, 11]. This arrangement is made of the

8 OLIVIER BERNARDI

hyperplanes Hi,j,0 for all i, j ∈ [n], and Hi,j,1 for all {i, j} ∈ E with i < j (so that it is
the braid arrangement if G has no edge, and the Shi arrangement if G = Kn). In yet
another direction, several authors have considered deformed braid arrangements with
hyperplanes Hi,j,s for generic, non-integer values of s (see e.g. [37, 40, 41, 27]), but we
will not consider such situations here.

3. Counting regions of S-braid arrangements

In this section we present our counting results for the regions of S-braid arrange-
ments. Throughout this section, S is a ﬁnite set of integers, m = max(|s|, s ∈ S), and
n is a non-negative integer.
We start with the deﬁnition of S-boxed trees (Deﬁnition 3.3), and then express the
number of regions of AS(n) as a signed count of S-boxed trees (Theorem 3.4). Then
we restrict our attention to transitive sets S (Deﬁnition 3.5) and for them we express
the number of regions of AS(n) as an unsigned count of trees (Theorem 3.8).
In order to deﬁne S-boxed trees, we ﬁrst need to deﬁne S-cadet sequences.

Deﬁnition 3.1. • Let T be a tree in T , and let u be a node. If one of the children
of u is a node, we call the rightmost such child the cadet-node of u, and denote
it by cadet(u).
4

• A cadet sequence is a non-empty sequence (v1, . . . , vk) of nodes such that for
all i in [k − 1], vi+1 = cadet(vi).
• A S-cadet sequence is a cadet sequence (v1, . . . , vk) such that for all 1 ≤ i <

j ≤ k, if
 j∑

p=i+1 lsib(vp) ∈ S ∪ {0} then vi < vj, and if −
 j∑

p=i+1 lsib(vp) ∈ S then

vi > vj.

Note that an S-cadet sequence (v1, . . . , vk) of T ∈ T (m) satisﬁes in particular lsib(vj) ∈
[0..m] \ {s ∈ S | − s ∈ S} for all j ∈ [2..k].

Example 3.2. Let T ∈ T (m).
• For S = [−m..m], the S-cadet sequences of T contain a single vertex.
• For S = [−ℓ..m] with 0 ≤ ℓ ≤ m, the S-cadet sequences of T are the cadet
sequences (v1, . . . , vk) satisfying v1 < v2 < · · · < vk and lsib(vp) ∈ [ℓ + 1..m] for
all p ∈ [2..k].
• For S = [−ℓ..m] \ {0} with 0 ≤ ℓ ≤ m, the S-cadet sequences of T are the cadet
sequences (v1, . . . , vk) satisfying v1 < v2 < · · · < vk and lsib(vp) ∈ {0}∪[ℓ+1..m]
for all p ∈ [2..k].
• For S = {−2, 0, 1, 2}, the S-cadet sequences of T have size at most 2, and the
S-cadet sequences of size 2 are of the form (v1, v2) with lsib(v2) = 1 and v1 < v2.

Deﬁnition 3.3. A boxed tree is a pair (T, B), where T is in T , and B is a set of cadet
sequences partitioning the set of nodes of T (that is, every node of T is contained in
exactly one cadet sequence in B). The pair (T, B) is an S-boxed tree if T ∈ T (m), and

4The term cadet is used here in its genealogical meaning of youngest heir.

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 9

B contains only S-cadet sequences. We denote by US(n) the set of S-boxed trees with
n nodes.

We represent boxed trees as trees decorated with boxes partitioning the nodes into
cadet sequences, as in Figure 3(b). We can now state the main result of this section.

Theorem 3.4. Let S be a ﬁnite set of integers and n be a positive integer. The number
of regions of the hyperplane arrangement AS(n) is

(3.1) rS(n) = ∑

(T,B)∈US (n)
(−1)
n−|B|.

The proof of Theorem 3.4 is delayed to Section 7. We will now give a simpler
expression for rS(n) in the cases where the set S is “well-behaved”. More precisely, we
now introduce the notion of transitivity for a set S, which implies a drastic simpliﬁcation
of the deﬁnition of S-cadet-sequences (Lemma 3.11), and allows one to deﬁne a simple
sign reversing involution on S-boxed trees.

Deﬁnition 3.5. A set S of integers is called transitive if it satisﬁes the following
conditions for all integers s, t /∈ S:
• if st > 0, then s + t /∈ S,
• if s > 0 and t ≤ 0, then s − t /∈ S and t − s /∈ S.

Example 3.6. • All the subsets of {−1, 0, 1} are transitive.
• All the intervals of integers containing 1 are transitive.
• Sets of the form S = I \ kZ, where I is an interval containing 1 are transitive.
• Sets S such that [−⌊m/2⌋..⌊m/2⌋] ⊆ S ⊆ [−m..m] for some m are transitive.
• A set S such that {−s, s ∈ S} = S is transitive if and only if the set of positive
integers not in S is closed under addition (equivalently, 0 together with the
positive integer not in S form what is called a numerical semigroup; see [4] for
references on numerical semigroups).
• A set S such that [m] ⊆ S ⊆ [−m..m] is transitive if and only if the set of
negative integers not in S is closed under addition.

Deﬁnition 3.7. We denote by TS(n) the set of trees T in T (m)(n) such that all nodes
u, v satisfying cadet(u) = v further satisﬁes the following:
Condition(S): if lsib(v) /∈ S ∪ {0} then u < v, and if − lsib(v) /∈ S then u > v.

Theorem 3.8. If S is transitive, then regions of the hyperplane arrangement AS(n)
are equinumerous to the trees in TS(n).

Example 3.9. • T[−m..m](n) = T (m)(n).
• T[−m+1..m](n) is the set of trees in T (m)(n), such that any non-root node having
no right-sibling (not even leaves) is less than its parent.
• T[m](n) is the set of trees in T (m)(n), such that such that any cadet-node v is
less than its parent.
• More generally, for 0 ≤ ℓ ≤ m, T[−ℓ..m](n) is the set of trees in T (m)(n), such
that any cadet-node v having more than ℓ left-sibling is less than its parent.
And T[−ℓ..m]\{0}(n) is the set of trees in T (m)(n), such that any cadet-node v
having either no left sibling or more than ℓ left-siblings is less than its parent.

10 OLIVIER BERNARDI

Remark 3.10. For any sets S, S′ ⊂ Z, TS(n) ∩ TS′(n) = TS∩S′(n). For instance the set
T{1}(n) of trees associated to Linial arrangement, is the intersection of the set of trees
T{0,1}(n) associated to the Shi arrangement, and the set of trees T{−1,1}(n) associated
to the semiorder arrangement.
Moreover, each element s ∈ [−m..m] \ S gives a simple condition for trees in TS(n):
for s > 0 the condition is that a cadet node with s left siblings is greater than its
parent, while for s ≤ 0 the condition is that a cadet node with −s left siblings is less
than its parent. This is represented in Figure 5.

) u < v

Condition for s 2 [m ] n S

u

vs
 ) u > v
u

vs
Condition for −s 2 [−m:: 0] n S

Figure 5. Conditions for trees to be in TS(n). Each element s ∈
[−m..m] \ S imposes one condition.

Theorem 3.8 is an easy consequence of Theorem 3.4 and the following lemma.

Lemma 3.11. Suppose that the set S is transitive. In this case, a cadet sequence
(v1, . . . , vk) is an S-cadet sequence if and only if for all i ∈ [k − 1],
(*) if lsib(vi+1) ∈ S ∪ {0} then vi < vi+1, and if − lsib(vi+1) ∈ S then vi > vi+1.

Proof. It is clear that the condition (*) is necessary. We now prove that it is suﬃcient,
by induction on k. The case k = 1 is trivial. Now suppose that k > 1 and γ =
(v1, . . . , vk) satisﬁes (*). Since γ′ = (v1, . . . , vk−1) satisﬁes (*), it is an S-cadet sequence.
Hence we only need to check that for all i ∈ [k − 1],

(**) if
 k∑

p=i+1 lsib(vp) ∈ S ∪{0} then vi < vk, and if −
 k∑

p=i+1
lsib(vp) ∈ S then vi > vk.

The case i = k − 1 of (**) is directly given by (*). We now consider i ∈ [k − 2], and con-
sider several cases. Suppose ﬁrst that vi < vk−1 < vk. In this case, − ∑k−1
p=i+1 lsib(vp) /∈
S (since γ′ is an S-cadet sequence), − lsib(vk) /∈ S (since γ satisﬁes (*)), hence
− ∑k
p=i+1 lsib(vp) /∈ S (since S is transitive), hence Condition (**) holds for i. The
case vi > vk−1 > vk is treated similarly. Suppose next that vi > vk−1 < vk. In this
case, ∑k−1
p=i+1 lsib(vp) /∈ S ∪ {0} (since γ′ is an S-cadet sequence), − lsib(k) /∈ S (since
γ satisﬁes (*)), hence ∑k
p=i+1 lsib(vp) /∈ S ∪ {0} and − ∑k
p=i+1 lsib(vp) /∈ S (since S
is transitive), hence Condition (**) holds for i. The case vi < vk−1 > vk is treated
similarly. Thus Condition (**) holds for all i, and γ is an S-cadet sequence. □

Proof of Theorem 3.8. Let T ∈ T (m)(n), and let v = cadet(u). We claim that that u
and v can be in the same box of an S-boxed tree (T, B) if and only if u and v do not
satisfy Condition(S) of Deﬁnition 3.7. Indeed, by Lemma 3.11, in the case u < v (resp.
u > v) the vertices u and v can be in the same box if and only if − lsib(v) /∈ S (resp.
lsib(v) /∈ S ∪ {0}), and this holds if and only if Condition(S) does not hold.

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 11

For a tree T in T (m)(n), we denote BT = {B | (T, B) ∈ US(n)}. By Theorem 3.4,

(3.2) rS(n) = ∑

T ∈TS (n)
 ∑

B∈BT (−1)
n−|B| + ∑

T ∈T (m)(n)\TS (n)
 ∑

B∈BT (−1)
n−|B|.

By the above claim, for all T in TS, BT contain a single element because every node
of T must be in a diﬀerent box. Thus the ﬁrst sum of (3.2) contributes |TS(n)|. We
now prove that the second sum is 0 using a sign reversing involution. For a tree
T ∈ T (m)(n) \ TS(n), we pick the smallest vertex v = cadet(u) such that Condition(S)
does not hold, and deﬁne an involution ϕ on BT as follows:
• if u and v are in the same box of B, then ϕ(B) is obtained by splitting the box
containing them between u and v,
• if u and v are in diﬀerent boxes of B, then ϕ(B) is obtained by merging these
boxes.
Lemma 3.11 ensures that ϕ(B) ∈ BT in the second situation. Since ϕ is an involution
on BT changing the number of boxes by ±1, we get ∑
B∈BT (−1)n−|B| = 0. Hence the
second sum in (3.2) contributes 0. □

4. General deformations of the braid arrangement

In this section we extend the results of Section 3 to general deformations of the braid
arrangement. We ﬁx a positive integer N and an (N
2 )-tuple of ﬁnite sets of integers
S = (Sa,b)1≤a<b≤N . The arrangement in RN made of the hyperplanes

Ha,b,s = {(x1, . . . , xN ) ∈ RN | xa − xb = s},

for all 1 ≤ a < b ≤ N and all s ∈ Sa,b is called S-braid arrangement, and is denoted
AS. Note that if Sa,b = S for all a, b, then AS = AS(N ).
We will now extend Theorem 3.4 to S-braid arrangements. Let m = max(|s|, s ∈
∪Sa,b). For 1 ≤ a < b ≤ N , we denote Sb,a = Sa,b, S−
a,b = {s ≥ 0 | − s ∈ Sa,b}, and
S−
b,a = {s > 0 | s ∈ Sa,b} ∪ {0}.

Deﬁnition 4.1. A cadet sequence (v1, . . . , vk) of T ∈ T (m)(N ) is an S-cadet sequence

if for all 1 ≤ i < j ≤ k,
 j∑

p=i+1 lsib(vp) /∈ S−
vi,vj . An S-boxed tree is a boxed tree (T, B)

with T ∈ T (m)(N ), and B containing only S-cadet sequences. We denote by US the
set of S-boxed trees.

Theorem 4.2. The number of regions of the hyperplane arrangement AS is

(4.1) rS = ∑

(T,B)∈US(−1)
n−|B|.

The condition ∑j
p=i+1 lsib(vp) /∈ S−
vi,vj is equivalent to: if ∑j
p=i+1 lsib(vp) ∈ Svi,vj ∪

{0} then vi < vj, and if −
∑j
p=i+1 lsib(vp) ∈ Svi,vj then vi > vj. In particular, if
Sa,b = S for all a, b, then US = US(N ). Hence Theorem 4.2 generalizes Theorem 3.4.
Theorem 4.2 will be extended in the next section and its proof is delayed to Section 7.
We now generalize Theorem 3.8 to S-braid arrangements.

12 OLIVIER BERNARDI

Deﬁnition 4.3. The tuple S is said transitive if for all distinct integers a, b, c ∈ [N ]
the following condition holds: if s /∈ S−
a,b and t /∈ S−
b,c, then s + t /∈ S−
a,c.

It is easy to see that if Sa,b = S for all a, b ∈ [N ], then S is transitive if and only if
S is transitive.

Example 4.4. If for all a, b ∈ [N ], [−⌊m/2⌋ .. ⌊m/2⌋] ⊆ Sa,b ⊆ [−m..m], then S is
transitive.

Deﬁnition 4.5. We denote by TS the set of trees T in T (m)(N ) such that any pair of
nodes u, v such that cadet(u) = v satisﬁes lsib(v) ∈ S−
u,v.

Theorem 4.6. If S = (Sa,b)1≤a<b≤N is transitive, then the regions of AS are equinu-
merous to the trees in TS.

Remark 4.7. The condition lsib(v) /∈ S−
u,v is equivalent to: if lsib(v) /∈ Su,v ∪ {0} then
u < v, and if − lsib(v) ∈ Su,v then u > v. In particular, if Sa,b = S for all a, b ∈ [N ],
then TS = TS(N ). Hence Theorem 4.6 generalizes Theorem 3.8.

Example 4.8. Let G = ([N ], E) be a graph and let S, S′ be two ﬁnite sets of integers.
Let G(S, S′) be the tuple S = (Sa,b)1≤a<b≤N deﬁned by Sa,b = S if {a, b} ∈ E and
Sa,b = S′ otherwise. Several cases are represented in Figure 6.
(1) For S = {−1, 0, 1} and S′ = {0, 1}, the tuple S = G(S, S′) is transitive for any
graph G, and TS is the set of trees in T (1)(N ) such that if a node v is the right
child of u, then either {u, v} ∈ E or u > v (or both).
(2) For S = {−1, 0, 1} and S′ = {0}, the tuple S = G(S, S′) is transitive for any
graph G, and TS is the set of trees in T (1)(N ) such that if a node v is the right
child of u, then {u, v} ∈ E.
(3) For S = {0, 1} and S′ = {0}, the tuple S = G(S, S′) is transitive for any graph
G, and TS is the set of trees in T (1)(N ) such that if a node v is the right child
of u, then {u, v} ∈ E and u > v.
(4) For S = {0, 1} and S′ = {−1, 0}, the tuple S = G(S, S′) is transitive for any
graph G, and TS is the set of trees in T (1)(N ) such that if a node v is the right
child of u, then either ({u, v} ∈ E and u > v) or ({u, v} /∈ E and u < v).

x1

x2 x3

S = {−1; 0; 1}, S ′ = {0; 1} S = {−1; 0; 1}, S ′ = {0} S = {0; 1}, S ′ = {0}, S = {0; 1}, S ′ = {−1; 0}

x1

x2 x3
 x1

x2 x3
 x1

x2 x3

Figure 6. Some transitive deformations of the braid arrangement.
These arrangements have the form AG(S,S′), where G is the graph having
vertex set [3] and edges {1, 2} and {1, 3}.

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 13

Proof of Theorem 4.6. Given Theorem 4.2, we only need to prove that if S = (Sa,b)1≤a<b≤n
is transitive, then

(4.2) ∑

(T,B)∈US(−1)
|B| = |TS|.

The proof of (4.2) is almost identical to that of Theorem 3.8, except that Lemma 3.11
is replaced by the following claim: if S is transitive, a cadet sequence (v1, . . . , vk) of
T ∈ T (m)(N ) is a S-cadet sequence if and only if for all i ∈ [k − 1], lsib(vi+1) /∈ S−
vi,vi+1.
Proof of the claim: It is clear that lsib(vi+1) /∈ S−
vi,vi+1 is necessary. We now prove
that it is suﬃcient, by induction on k. The case k = 1 is trivial. Now suppose
that k > 1, and γ = (v1, . . . , vk) is cadet sequence such that for all i ∈ [k − 1],
lsib(vi+1) /∈ S−
vi,vi+1. We want to prove that γ is a S-cadet sequence. By the induction
hypothesis, γ′ = (v1, . . . , vk−1) is a S-cadet sequence, so we only need to prove that
for all i ∈ [k − 1], ∑k
p=i+1 lsib(vp) /∈ S−
vi,vk . This is true by hypothesis for i = k − 1.
Moreover, for i ∈ [k − 1], ∑k−1
p=i+1 lsib(vp) /∈ S−
i,k−1 (since γ′ is a S-cadet sequence), and

lsib(vk) /∈ S−
k−1,k (by hypothesis), hence ∑k
p=i+1 lsib(vp) /∈ S−
i,k (since S is transitive).
Hence γ is a S-cadet sequence. This proves the claim.
One can then deﬁne a sign reversing involution on S-boxed trees showing (4.2), exactly
as in the proof of Theorem 3.8. □

5. Characteristic and coboundary polynomials of the deformations of
the braid arrangement

In this section we reﬁne our preceding counting results by expressing the character-
istic and coboundary polynomials of deformed braid arrangements in terms of boxed
trees.
5.1. Characteristic and coboundary polynomials.
For a hyperplane arrangement A ⊂ Rn, we denote by χA(q) its characteristic poly-
nomial of A, and by PA(q, y) its coboundary polynomial. Recall from [16] that the
coboundary polynomial is deﬁned by

PA(q, y) = ∑

B⊆A, ∩H∈BH̸=∅ qdim(∩H∈BH)(y − 1)
|B|,

and that χA(q) = PA(q, 0).
The characteristic polynomial χA contains a lot of information about the arrange-
ment A. In particular, by a result of Zaslavsky [46], the number of regions rA and the
number of relatively bounded 5 regions bA are evaluations of χA(q):

rA = (−1)
nχA(−1),(5.1)
 bA = (−1)
rank(A)χA(1),

where rank(A) is the dimension of the vector space generated by the vectors normal to
the hyperplanes of A. The characteristic polynomial is also equivalent to the Poincar´e

5A region of A is relatively bounded if its intersection with the subspace generated by the vectors
normal to the hyperplanes of A is bounded.

14 OLIVIER BERNARDI

polynomial of the cohomology ring of the complexiﬁcation of A; see [33]. The cobound-
ary polynomial is equivalent to the Tutte polynomial TA(x, y) of A (that is, the Tutte
polynomial of the semi-matroid associated with A, in the sense of Ardila [1, 2]):

TA(x, y) = (y − 1)
− rank(A)PA((x − 1)(y − 1), y).

5.2. Expressing the coboundary polynomial in terms of boxed trees.
In order to express the coboundary polynomials of deformed braid arrangements in
terms of boxed trees, we will consider arrangements of all dimensions. Let ̂S =
(Sa,b)1≤a≤b≤N be an (N +1
2 )-tuple of ﬁnite sets, let m = max(|s|, s ∈ ∪Sa,b), and
let n = (n1, . . . , nN ) ∈ NN . We denote |n| = n1 + . . . + nN , and

V (n) = {(a, i) | a ∈ [N ], i ∈ [na]}.

We endow V (n) with the lexicographical order, that is, we denote (a, i) < (b, j) if
either a < b, or a = b and i < j. For u = (a, i) and v = (b, j) ∈ V (n), we denote
Su,v = Sv,u = Sa,b, and if u < v we denote S−
u,v = {s ≥ 0 | − s ∈ Sa,b} and S−
v,u =
{s > 0 | s ∈ Sa,b} ∪ {0}. Lastly, we deﬁne ÂS(n) as the arrangement in R|n| with
hyperplanes Hu,v,s = {(xw)w∈V (n) | xu − xv = s},

for all u < v in V (n) and all s ∈ Su,v.
Note that ÂS(n) identiﬁes with the arrangement ÂS(n), where

(5.2) ̂S(n) = (S′
u,v)1≤u<v≤|n|

with S′
u,v = Sa,b for all u ∈
 [
1 +
 a−1∑

i=1 ni ..
 a∑

i=1 ni
]
 and v ∈
 [

1 +
 b−1∑

i=1 ni ..
 b∑

i=1 ni
]
. For

instance, ÂS(1, 1, . . . , 1) = ÂS, and ÂS(n1, 0, . . . , 0) = AS1,1(n1). We now describe
boxed trees related to the arrangement ÂS(n).
• We denote by T (m)(n) the set of rooted plane (m + 1)-ary trees with |n| nodes
labeled with distinct labels in V (n).
• A cadet sequence (v1, . . . , vk) of T ∈ T (m)(n) is admissible if vi < vi+1 for all
i ∈ [k − 1] such that lsib(vi+1) = 0. A boxed tree (T, B) is admissible if all
the sequences in B are admissible. We denote by U (m)(n) the set of admissible
boxed trees (T, B) with T ∈ T (m)(n).
• The ̂S-energy of a cadet sequence (v1, . . . , vk) of T is the number of pairs {i, j}
with 1 ≤ i < j ≤ k, such that ∑j
p=i+1 lsib(vp) ∈ S−
vi,vj .
6 The ̂S-energy of a
boxed tree (T, B) ∈ U (m)(n), denoted energŷS(T, B), is the sum of the energies
of the cadet sequences in B.
• We denote by ÛS(n) the set of boxed trees (T, B) ∈ U (m)(n) such that energŷS(T, B) =
0.

6The terminology energy used here is related to the interpretation of the current counting problem
(about the coboundary polynomial of arrangements) in terms of a gas model which will be introduced
in Section 7.
 DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 15

Note that any boxed tree in ÛS(n) is admissible. Moreover, ÛS(n1, 0, . . . , 0) =
US1,1(n1), and ÛS(1, 1, . . . , 1) = US, where S = (Sa,b)1≤a<b≤N .
We denote by T̂S(n) the set of trees T in T (m)(n) such that any pair of nodes u, v
such that cadet(u) = v satisﬁes lsib(v) ∈ S−
u,v. Note that T̂S(n1, 0, . . . , 0) = TS1,1(n1),
and T̂S(1, 1, . . . , 1) = TS, where S = (Sa,b)1≤a<b≤N . We say that ̂S is multi-transitive if
̂S(n) is transitive (in the sense of Deﬁnition 4.3) for all n ∈ NN . Note that for N = 1
̂S is multi-transitive if and only if S1,1 is transitive.

Example 5.1. If for all a, b ∈ [N ], [−⌊m/2⌋ .. ⌊m/2⌋] ⊆ Sa,b ⊆ [−m..m], then ̂S is multi-
transitive. Also, if Sa,a is transitive for all a ∈ [N ], and Sa,b = [−m..m] for all a < b,
then ̂S is multi-transitive.

We can now express the coboundary polynomial of the arrangements. Given inde-
terminates t1, . . . , tN , we denote t = (t1, . . . , tN ), tn = ∏N
a=1 tna
a , and n! = ∏N
a=1 na!.
We denote
 P̂S(q, y, t) = ∑

n∈NN PÂS(n)(q, y) tn

n! ,(5.3)
 χ̂S(q, t) = ∑

n∈NN χÂS(n)(q) tn

n! ,(5.4)
 R̂S(t) = ∑

n∈NN rÂS(n) tn

n! ,(5.5)

In the above deﬁnition, we adopt the convention PÂS(0,...,0)(q, y) = 1 (coboundary
polynomial of the empty semi-matroid). By (5.1), χ̂S(q, t) = P̂S(q, 0, t) and R̂S(t) =
χ̂S(−1, −t), where −t = (−t1, . . . , −tN ).

Theorem 5.2. Let ̂S = (Sa,b)1≤a≤b≤N be an (N +1
2 )-tuple of ﬁnite sets of integers, and
let m = max(|s|, s ∈ ∪Sa,b). Then P̂S(q, y, t) is related to boxed trees by

(5.6) P̂S(q, y, t) =
 

 ∑

n∈NN
 tn

n!
 ∑

(T,B)∈U (m)(n)(−1)
|B|yenergŷS(T,B)




−q
 .

In particular,

(5.7) χ̂S(q, t) = R̂S(−t)
−q,

and

(5.8) R̂S(t) = ∑

n∈NN
 tn

n!
 ∑

(T,B)∈ÛS(n)(−1)
|n|−|B|.

Moreover, if ̂S is multi-transitive, then

(5.9) R̂S(t) = ∑

n∈NN
 tn

n! |T̂S(n)|.

16 OLIVIER BERNARDI

Note that Equation (5.8) implies Theorem 3.4 (for S = S1,1) by extracting the
coeﬃcient of tn
1 t0
2 . . . t0
N , and Theorem 4.2 by extracting the coeﬃcient of t1t2 · · · tN .
Several applications of Theorem 5.2 are given in Section 6.

5.3. Remarks about the case of graphical arrangements (case m = 0).
In this subsection we consider the special case m = 0 of Theorem 5.2 which corresponds
to graphical arrangements, in order to highlight how our results are related to some
known results about graph colorings and acyclic orientations.
Remember that the G-graphical arrangement associated to a (simple, undirected)
graph G = ([n], E) is the n-dimensional arrangement A(G) made of the hyperplanes
Hi,j,0 for all {i, j} ∈ E. It follows easily from the deﬁnitions that the number of
regions of A(G) is the number of acyclic orientations of G7. Also, as we now recall,
the characteristic and coboundary polynomials of A(G) are related to the colorings of
G. Recall that the partition function of the Potts model on G, is the unique bivariate
polynomial PG(q, y) such that for all positive integer q,

PG(q, y) = ∑

f :V →[q] ymono(f ),

where the sum is over all possible colorings of the vertices in q colors, and mono(f ) is
the number of edges of G with both endpoints of the same color. The specialization
χG(q) = PG(q, 0) counting the proper colorings of G in q colors is called chromatic
polynomial of G. It is known [16] that for any graph G, the coboundary polynomial
PA(G)(q, y) is equal to PG(q, y), and in particular the characteristic polynomial χA(G)(q)
is equal to the chromatic polynomial χG(q).
We can now interpret the case m = 0 of Theorem 5.2 in terms of graphs. Let
̂S = (Sa,b)1≤a≤b≤N be a tuple such that each set Sa,b is either empty or equal to {0}.
Note that ÂS(n) is the G-graphical arrangement for the graph G = ĜS(n) with vertex
set V (n) and edges {u, v} for all u = (a, i) and v = (b, j) such that Sa,b = {0}.
Moreover, the boxed trees in U (0)(n) are simply paths with boxes partitioning the
vertices, such that in each box the vertices are in increasing order. Hence U (0)(n) can
simply be interpreted as the set of ordered set partitions of V (n). Lastly, the ̂S-energy
of a subset U of V (n) is the number of edges of ĜS(n) induced by U (that is, edges
of ĜS(n) with both endpoints in U ). So the right-hand side of (5.6) counts ordered
partitions of V (n) according to the number of edges it induces.

Example 5.3. Consider the case N = 2, S1,1 = S22 = ∅ and S1,2 = {0}. In this
case, G = ĜS(n1, n2) is the complete bipartite graph Kn1,n2. Hence, for a subset U of
V (n1, n2) containing k1 vertices of the form (1, i) and k2 vertices of the form (2, i), the

7In this natural correspondence, the direction of the edge (i, j) indicates which side of the hyper-
planes Hi,j,0 the region is, or equivalently the inequality between the coordinates xi and xj.

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 17

number of edges of G induced by U is k1k2. Thus (5.6) gives

∑

(n1,n2)∈N2PKn1,n2 (q, y) t
n1
1 t
n2
2
n1!n2! =
 


 ∑

(n1,n2)∈N2
 t
n1
1 tn2
2
n1!n2!
 ∑

(U1,...,Ur )
ordered partition of V (n1,n2)
 r∏

i=1 yenergŷS(Ui)





−q

=
 

 1

1 + ∑
(k1,k2)∈N2\{(0,0)}
yk1k2 t
k1
1 t
k2
2
k1!k2!
 



−q

=
 

 ∑

(k1,k2)∈N2

yk1k2tk1
1 tk2
2
k1!k2!
 



q
 ,

where the second equality directly follows basic generating function principles upon
interpreting ordered set partitions as labeled sequences of sets (see [18, Chapter 2]).

Now, for an arbitrary graph G = ([N ], E), we consider ̂S = (Sa,b)1≤a≤b≤N with
Sa,a = {0} for all a ∈ [N ], and for a < b, Sa,b = {0} if {a, b} ∈ E and Sa,b = ∅
otherwise. Then, (5.7) gives

(5.10) χG(q) = [t1t2 · · · tN ]R̂S(−t)
−q = (−1)
N [t1t2 · · · tN ]R̂S(t)−q.

This equation relates the proper colorings of G (left-hand side) to the acyclic orienta-
tions of induced subgraphs of G (right-hand side). For instance, it gives (−1)N χG(−1) =
[t1t2 · · · tN ]R̂S(t) which is the number of regions of ÂS(1,1,...,1) = A(G), or equivalently
the number of acyclic orientations of G. This is precisely the interpretation of χG(−1)
given by Stanley in [42]. More generally, for U = {u1, . . . , uk} ⊆ [N ], the coeﬃcient
[tu1tu2 · · · tuk ]R̂S(t) is by deﬁnition the number of regions of the G[U ]-graphical ar-
rangement, where G[U ] is the subgraph of G induced by U . Thus [tu1tu2 · · · tuk ]R̂S(t)
is the number of acyclic orientations of G[U ]. Using this interpretation, one can recover
from (5.10) the interpretation of (−1)N χ(−q) given in [42] (it counts the total number
of acyclic orientations induced on the blocks of an ordered set partition of length q of
the vertices of G).
For the readers with some familiarity with the theory of heaps (see for instance [45,
29]), we mention an interpretation of (5.10) in this context. Consider the heap structure
associated to the graph G: the pieces are the vertices of G, and two pieces overlap if
they correspond to adjacent vertices. In this context, R̂S(t) can be interpreted as the
generating function of the heaps of pieces associated to G (where the variable ti counts
the number of pieces associated to the vertex i of G). Indeed, the regions of ÂS(n) are
in one-to-one correspondence with the acyclic orientations of ĜS(n), which are in one-
to-one correspondence with the heaps having ni pieces associated to the vertex i of G.
Hence, by [45, Proposition 5.3], I(t) := R̂S(−t)−1 is the generating function of trivial
heaps, or equivalently, independent sets of G (that is, sets of non-adjacent vertices).
Thus, through the theory of heaps (5.10) becomes transparent: it simply expresses
the fact that a proper q-coloring of G is a q-tuple of independent sets partitioning
the vertices. More generally, we get a simple expression for the generating function of

18 OLIVIER BERNARDI

chromatic polynomials χ̂S(q, t):

χ̂S(q, t) = I(t)
q =
 

 ∑

U ⊆[N ], independent set of G
 ∏

i∈U ti




q
 .

6. Generating functions

In this section, we use Theorem 5.2 in order to give equations for the generating
functions P̂S(q, y, t), χ̂S(q, t), and R̂S(t). These equations simply translate the decom-
position of boxed trees obtained by deleting the box containing the root.
6.1. A universal generating function equation.
Let ̂S = (Sa,b)1≤a≤b≤N be an (N +1
2 )-tuple of ﬁnite sets, and let m = max(|s|, s ∈ ∪Sa,b).
In order to characterize the generating functions associated to the arrangements ÂS(n),
we need to deﬁne some combinatorial structures encoding admissible cadet sequences
for trees in T (m)(n).

Deﬁnition 6.1. A (m, N )-conﬁguration of size k ∈ NN , is a pair γ = ((d1, . . . , d|k|−1), (u1, . . . , u|k|))
such that {u1, . . . , u|k|} = V (k), d1, . . . , d|k|−1 ∈ [0..m], and if di = 0 then ui < ui+1.
We denote by |γ| = k the size of γ. The width of γ is wid(γ) = d1+· · ·+d|k|−1+m+1,
and the ̂S-energy of γ, denoted energŷS(γ), is the number of pairs {i, j} with 1 ≤ i <
j ≤ |k| such that ∑j−1
p=i dp ∈ S−
ui,uj .

Remark 6.2. To an admissible cadet sequence (v1, . . . , vk) of a tree T ∈ T (m)(n), we
associate an (m, N )-conﬁguration γ = ((d1, . . . , dk−1), (u1, . . . , uk)) deﬁned as follows.
Denoting k = (k1, . . . , kN ) with ka = |{i ∈ [na] | (a, i) ∈ {v1, . . . , vk}}|, we set
• di = lsib(vi+1) for all i ∈ [k − 1],
• (u1, . . . , uk) is the unique order-preserving relabeling of (v1, . . . , vk) in V (k).
It is clear that γ is an (m, N )-conﬁguration of size k, and that energŷS(γ) is the ̂S-
energy of the cadet sequence (v1, . . . , vk). Moreover, wid(γ) is the number of children
of v1, . . . , vk which are neither in {v2, . . . , vk} nor right-siblings of v2, . . . , vk.

For k ∈ NN , we denote by C(m)(k) the set of (m, N )-conﬁgurations of size k, and
we denote by ĈS(k) the subset of conﬁgurations having ̂S-energy 0. We also denote

C(m,N ) = ⋃

k̸=(0,...,0) C(m)(k) and ĈS = ⋃

k̸=(0,...,0) ĈS(k), where the unions are over non-zero

tuples in NN . Finally, we denote

Γ̂S(x, y, t) = ∑

γ∈C(m,N ) x
wid(γ)yenergyS (γ) t|γ|

|γ|! ,

and
 Γ̂S(x, t) = Γ̂S(x, 0, t) = ∑

γ∈ĈS
 xwid(γ) t|γ|

|γ|! .

We now state the general form of the generating function equation.

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 19

Theorem 6.3. The generating function of coboundary polynomials P̂S(q, y, t) (deﬁned
by (5.3)) is equal to ̃P̂S(y, t)−q, where ̃P̂S(y, t) is the unique series in Q[y][[t1 . . . , tN ]]
satisfying

(6.1) ̃P̂S(y, t) = 1 − Γ̂S( ̃P̂S(y, t), y, t).

In particular, the generating function of regions R̂S(t) (deﬁned by (5.5)) is the unique
series in Q[[t1, . . . , tN ]] satisfying

(6.2) R̂S(t) = 1 − Γ̂S(R̂S(t), −t).

Example 6.4. Let N = 2 and S1,1 = [−2..2], S1,2 = [−1..2], and S2,2 = {−2, 0, 1, 2}.
Then we have m = 2 and CS = {γ1, γ2, γ3, γ4, γ5}, where γ1 = ((), (v1)), γ2 = ((), (v2))
γ3 = ((1), (v2, v3)), γ4 = ((2), (v1, v2)), and γ5 = ((2, 1), (v1, v2, v3)) with v1 = (1, 1),
v2 = (2, 1), v3 = (2, 2). Thus Γ̂S(x, t) = (t1 + t2)x3 + t2
2x4/2 + t1t2x5 + t1t2
2x6/2 and

R̂S(t) = 1 + (t1 + t2)R̂S(t)
3 − t
2
2R̂S(t)4/2 − t1t2R̂S(t)
5 + t1t2
2R̂S(t)
6/2.

This gives

R̂S(t) = 1 + t1 + t2 + 3 t12 + 5 t1t2 + 5/2 t22 + 12 t13 + 28 t12t2 + 25 t1t22 + 17/2 t23 + . . . .

Proof. By Theorem 5.2, P̂S(q, y, t) = ̃P̂S(y, t)−q for

̃P̂S(y, t) := ∑

n∈NN
 tn

n!
 ∑

(T,B)∈U (m)(n)
(−1)
|B|yenergŷS(T,B).

We now consider the decomposition boxed trees (T, B) ∈ U (m)(n) for |n| > 0. Consider
the cadet sequence β = (v1, . . . , vk) ∈ B containing the root v1 of T . By Remark 6.2,
we can associate to β an (m, N )-conﬁguration γ. Deleting the vertices v1, . . . , vk of T
and the right-siblings of v2, . . . , vk−1 (which, by deﬁnition, are leaves), gives a sequence
of wid(γ) subtrees. Hence, the class U (m,N ) = ⋃n∈NN U (m)(n) admits the following
recursive equation
 U (m,N ) = 1 + ∑

γ∈C(m,N ){γ} ⋆ Seqwid(γ)(U (m,N )),

where ⋆ denotes the product, and Seqℓ denotes the ℓ-sequences construction for labeled
combinatorial classes (see e.g. [18, Chapter 2]). This gives

̃P̂S(y, t) = 1 + ∑

γ∈C(m,N )
 (

−yenergŷS(γ) t|γ|

|γ|!
 )
 × ( ̃P̂S(y, t))wid(γ) ,

which is (6.1). Moreover, (6.1) implies (6.2), because (5.1) gives R̂S(t) = ̃P̂S(0, −t). □

20 OLIVIER BERNARDI

6.2. Generating functions for S-braid arrangements (case N=1).
In this subsection, we explore in more details the case of S-braid arrangements (case
N = 1 of Theorem 6.3). When S is transitive we obtain simpler equations for the
generating function of regions. We then recover and extend several classical results.
For a set of integers S, we denote CS = C(S). Hence, CS is the set of pairs γ =
((d1, . . . , dk−1), (v1, . . . , vk)) such that
• {v1, . . . , vk} = [k],
• d1, . . . , dk−1 ∈ [0..m], where m = max(|s|, s ∈ S)
• for all 0 ≤ i < j ≤ k either vi < vj and − ∑j−1
p=i dp /∈ S, or vi > vj and
∑j−1
p=i dp /∈ S ∪ {0}.

Equation (6.2) then gives the following characterization of RS(t) = ∑

n≥0 rAS (n) tn

n! :

(6.3) RS(t) = 1 − ΓS(RS(t), −t),

where ΓS(x, t) = ∑

γ∈CS xwid(γ) t|γ|

|γ|! .

Example 6.5. For S = [−3..3] \ {−2, 1}, we have m = 3 and CS = {γk, k ≥ 1} ∪
{γ′}, where γk = ((2, 2, . . . , 2), (1, 2, . . . , k)) and γ′ = ((1), (2, 1)). Thus ΓS(x, t) =
∑k≥1 tk x2k+2
k! + t2x5/2 = x2(etx2 − 1) + t2x5/2 and

RS(t) = 1 + RS(t)
2(1 − e
−tRS (t)2) − t2RS(t)
5/2.

Next, we give an expression for ΓS(x, t) when S is transitive. For k > 1 we denote
by Sk the set of permutations of [k]. For π ∈ Sk, we let asc(π) = {i ∈ [k − 1] | π(i) <
π(i + 1)} and des(π) = {i ∈ [k − 1] | π(i) > π(i + 1)} be the number of ascents and
descents of π respectively. We denote

Λ(u, v, t) =
 ∞∑

k=1
 ∑

π∈Sk u
asc(π)vdes(π) tk

k! .

This is the generating function of the homogeneous Eulerian polynomials. Clearly,
Λ(u, u, t) = t
1−tu and Λ(u, 0, t) = etu−1
u . More generally, it is known [13] that

(6.4) Λ(u, v, t) = etu − etv

u etv − v etu .

Proposition 6.6. If S ⊆ Z is transitive, and m = max(|s|, s ∈ S) then

(6.5) ΓS(x, t) = xm+1Λ(µ(x), ν(x), t),

where µ(x) = ∑

−d∈[−m..0]\S xd, and ν(x) = ∑

d∈[m]\S xd. Thus, RS(t) is the unique solution

of

(6.6) RS(t) = 1 − RS(t)m+1Λ(µ(RS(t)), ν(RS(t)), −t).

Example 6.7. For S = [−m..m], we have µ(x) = ν(x) = 0. Hence ΓS(x, t) = txm+1,
and RS(t) = 1 + t RS(t)m+1.

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 21

Proof. Lemma 3.11 gives a simple characterization of CS. Namely γ = ((d1, . . . , dk−1), (u1, . . . , uk))
is in CS if and only if u1, . . . , uk is a permutation of [k], and for all i ∈ [k −1], di ∈ [0..m]
and either (vi < vi+1 and −di /∈ S) or (vi > vi+1 and di /∈ S ∪ {0}). Thus, for each
ascent i of the permutation u1, . . . , uk, −di is in [−m..0] \ S, and for each descent i, di
is in [m] \ S. This gives (6.5). □

Let us ﬁrst consider the special case [m] ⊆ S. Equation (6.8) below is [37, Theorem
9.1] of Postnikov and Stanley.

Corollary 6.8. If [m] ⊆ S ⊂ [−m..m] and {s < 0, s /∈ S} is closed under addition,
then

(6.7) RS(t) = 1 + RS(t)
m+1 1 − e−t µ(RS (t))

µ(RS(t)) ,

where µ(x) = ∑

−d∈[−m..0]\S xd. In particular, if S = [−ℓ..m] with ℓ ∈ [−1..m − 1], then

(6.8) RS(t)m−ℓ = exp (
t RS(t)m+1 − RS(t)ℓ+1

RS(t) − 1
 ) .

Proof. A set S satisfying the assumptions is transitive. Moreover ν(x) = 0 so that
Λ(µ(x), ν(x), t) = etµ(x)−1
µ(x) . Thus (6.6) gives (6.7). In the particular case S = [−ℓ..m]

we also have µ(x) = xm+1−xℓ+1
x−1 , and (6.7) readily gives (6.8). □

In the special case S = −S, we recover [43, Theorem 2.3] of Stanley and [43, Theorem
2.4] (written in a slightly diﬀerent form) which is credited to Athanasiadis.

Corollary 6.9 ([43]). If S ⊆ Z satisﬁes 0 ∈ S, {−s, s ∈ S} = S, and N \ S is closed
under addition, then for all n > 0,

(6.9) rAS (n) = (n − 1)![xn−1]
 

1 + x ∑

d∈[0..m]∩S(x + 1)d



n
 .

where m = max(|s|, s ∈ S). Moreover,

(6.10) RS\{0}(t) = RS(1 − e−t).

Proof. A set S satisfying the assumptions is transitive. Moreover, µ(x) = ν(x), so that
(6.6) becomes

(6.11) RS(t) = 1 + t RS(t)m+1

1 + t ν(RS(t)) ,

where ν(x) = ∑
d∈[m]\S xd. This gives ˜R(t) = tΘ( ˜R(t)), where ˜R(t) = RS(t) − 1 and
Θ(x) = (x + 1)m+1 − x ν(x + 1) = 1 + x ∑
d∈[0..m]∩S(x + 1)d. Hence, Lagrange inversion
formula gives (6.9). Moreover, S \ {0} is also transitive, and

ΓS\{0}(x, t) = x
m+1Λ(ν(x) + 1, ν(x), t) = xm+1 et − 1
1 − (et − 1)ν(x) = ΓS(x, e
t − 1).

22 OLIVIER BERNARDI

Thus (6.6) becomes
 RS\{0}(t) = 1 + (1 − e−t) RS\{0}(t)m+1

1 + (1 − e−t) ν(RS\{0}(t)) .

Comparing this equation with (6.11) gives (6.10). □

6.3. Generating functions for transitive arrangements in the case N > 1.
In this subsection, we return to the general case N ≥ 1 and consider several transitive
arrangements.

Theorem 6.10. Suppose ̂S = (Sa,b)1≤a≤b≤N is multi-transitive. Let Γ1(x, t), . . . , ΓN (x, t)
be the series deﬁned by the system of linear equations
(6.12)

Γa(x, t) = Λ(µa,a(x), νa,a(x), ta) ·
 (
1 +
 a−1∑

b=1 νb,a(x)Γb(x, t) +
 N∑

b=a+1 µa,b(x)Γb(x, t)

)
 ,

where Λ is deﬁned by (6.4), and for all 1 ≤ a ≤ b ≤ N , µa,b(x) = ∑
−d∈[−m..0]\Sa,b xd,

and νa,b(x) = ∑
d∈[m]\Sa,b xd. Then Γ̂S(x, t) = xm+1 ∑N
a=1 Γa(x, t) so that

R̂S(t) = 1 − R̂S(t)m+1 N∑

a=1 Γa(R̂S(t), −t).

Proof. Let ĈS,a be the set of conﬁgurations γ = ((d1, . . . , dk−1), (v1, . . . , vk)) ∈ ĈS such
that v1 has the form (a, i) for some i. We claim that Γa(x, t) is the generating function
of conﬁgurations in ĈS,a. More precisely,

Γa(x, t) = ∑

γ∈ĈS
 xwid(γ)−m−1 t|γ|

|γ|! .

Indeed, ĈS,a has a simple description (see proof of Theorem 4.6), and (6.12) simply
translates the decomposition of conﬁgurations in ĈS,a, at the ﬁrst p ∈ [k] such that vp
has the form (b, j) with b ̸= a (the term 1 in (6.12) corresponds to the case where there
is no such p). □

As an illustration of Theorem 6.10, we treat two examples inspired by [22].

Example 6.11. Suppose ﬁrst that Sa,a = {−1, 0, 1} for all a ∈ [N ] and Sa,b = {−1, 0}

for all 1 ≤ a < b ≤ N . Then (6.12) reads Γa(x, t) = ta(1 +
 a−1∑

b=1 xΓb(x, t)). This gives

Γa(x, t) = ∑

k>0 xk−1 ∑

1≤i1<i2<···<ik=a
 k∏

j=1 tij , so that

Γ̂S(x, t) = x ∑

k>0 x
k ∑

1≤i1<i2<···<ik≤N
 n∏

j=1 tij = x
 ( N∏

a=1 1 + tax
)
 − x.

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 23

Thus, (6.6) gives

(6.13) R̂S(t) =
 N∏

a=1
 1
1 − taR̂S(t) .

Now consider ̂S
′ = (S′
a,b)1≤a≤b≤N with S′
a,a = {0} for all a ∈ [N ] and S′
a,b = {0, 1}

for all 1 ≤ a < b ≤ N . Equation (6.12) reads Γa(x, t) = ta
1 − tax (1 +
 N∑

b=a+1 xΓb(x, t)).

hence Γa(x, t) = ∑

k>0 xk−1 ∑

a=i1≤i2≤···≤ik≤N
 k∏

j=1 tij , and

Γ̂S
′(x, t) = x ∑

k>0 xk ∑

1≤i1≤i2≤···≤ik≤N
 n∏

j=1 tij = x
 ( N∏

a=1
 1
1 − tax
 )
 − x.

Thus, (6.6) gives

(6.14) R̂S
′(t) =
 N∏

a=1 1 + taR̂S
′(t).

Note that (6.13) and (6.14) imply that R̂S(t) and R̂S
′(t) are symmetric functions in
(t1, . . . , tN ), which is not obvious from the deﬁnition. This is a special case of a result
proved in [22]. In fact, it follows from (5.9) that R̂S(t) = 1+B(1, 1, 0, 1, t) and R̂S
′(t) =
1 + B(1, 1, 1, 0, t) for the series B(u1, u2, v1, v2, t) considered in [22] which counts trees
in ⋃n∈NN T (1)(n) according to certain ascent and descent statistics. Accordingly, (6.13)
and (6.14) are special cases of the equation given for B(u1, u2, v1, v2, t) in [22].

We now state the extensions of Corollary 6.9 to N > 1.

Corollary 6.12. Suppose that ̂S = (Sa,b)1≤a≤b≤N is multi-transitive, and that for all
1 ≤ a ≤ b ≤ N , the set Sa,b contains 0 and satisﬁes {−s, s ∈ Sa,b} = Sa,b. Then for
all n ̸= (0, . . . , 0),

rÂS(n) = [t
n]
 (( N∑

a=1 ta
) ( N∏

b=1 gb(t)
nb−1)
 det(
δi,j gi(t) − tj ∂gi(t)
∂tj
 )

i,j∈[N ]
)
 ,

where ga(t) = 1 +
 N∑

b=1 tb ∑

d∈[0..m]∩Sa,b
 (
1 +
 N∑

c=1 tc
)d, and δi,j is the Kronecker delta.

Example 6.13. Let N = 2 and let ̂S = (Sa,b)1≤a≤b≤2 with S1,1 = S2,2 = {−1, 0, 1} and
S1,2 = {0}. Then g1(t1, t2) := 1 + t1(2 + t1 + t2) + t2, g2(t1, t2) := 1 + t2(2 + t1 + t2) + t1,
the determinant is (1 + t1 + t2)(1 − t2
1 − t2
2) and Corollary 6.12 gives

rÂS(n1,n2) = [tn1
1 t
n2
2 ] ((t1 + t2)(1 + t1 + t2)(1 − t
2
1 − t
2
2) g1(t1, t2)
n1−1 g2(t1, t2)n2−1) .

Corollary 6.12 is an application of the multivariate Lagrange inversion formula [21,
24] that we now recall for the readers’ convenience.

24 OLIVIER BERNARDI

Lemma 6.14 (Lagrange inversion formula). Let t = (t1, . . . , tN ) be indeterminates. Let
g1(t), . . . , gN (t) be series in C[[t]] with non-zero constant terms. Let f1(t), . . . , fN (t) be
the unique series in C[[t]] such that for all i ∈ [N ] fi(t) = tigi(f1(t), . . . , fN (t)). Then
for all a ∈ [N ] and for all tuples n = (n1, . . . , nN ) ∈ NN ,

[t
n]fa(t) = [t
n]
 (
ta ·
 ( N∏

b=1 gb(t)nb−1)
 · det
(δi,j gi(t) − tj ∂gi(t)
∂tj
 )
i,j∈[N ]
)
 .

Proof of Corollary 6.12. Since for all a ∈ [N ], Λ(µa,a(x), νa,a(x), ta) = ta
1−taνa,a(x) ,

Equation (6.12) can be rewritten as Γa(x, t) = ta(1 + ∑N
b=1 νa,b(x)Γb(x, t)). Hence,
denoting R(t) = R̂S(t) − 1 and Ra(t) = −R̂S(t)m+1Γa(R̂S(t), −t), we get

R(t) =
 N∑

a=1 Ra(t), and for all a ∈ [N ], Ra(t) = ta ga(R1(t), . . . , RN (t)),

where

ga(r1, . . . , rN ) = (
1+
 N∑

c=1 rc
)m+1−
 N∑

b=1 rb νa,b
(
1+
 N∑

c=1 rc
) = 1+
 N∑

b=1 rb ∑

d∈[0..m]∩Sa,b

(1+
 N∑

c=1 rc
)d.

Applying Lemma 6.14 gives the result. □

Corollary 6.15. Suppose that ̂S = (Sa,b)1≤a≤b≤N is multi-transitive, and that for some
a ∈ [N ], Sa,a contains 0 and satisﬁes {−s, s ∈ Sa,a} = Sa,a. Let ̂S′ be the same tuple
as ̂S except Sa,a is replaced by Sa,a \ {0}. Then,

R̂S
′(t) = R̂S(t1, . . . , ta−1, 1 − e
−ta, ta+1, . . . , tN ).

Proof. Let Γ1(x, t), . . . , ΓN (x, t) be the series satisfying (6.12) for the tuple ̂S and
Γ′
1(x, t), . . . , Γ′
N (x, t) their analogues for ̂S′. As in the proof of Corollary 6.9, we
get for all i ∈ [N ] Γ′
i(x, t) = Γ′
i(x, t′), where t′ = (t1, . . . , ta−1, eta − 1, ta+1, . . . , tN ).
Thus Γ̂S
′(x, t) = Γ̂S(x, t′), and Γ̂S
′(x, −t) = Γ̂S(x, −t′′), for t′′ = (t1, . . . , ta−1, 1 −
e−ta, ta+1, . . . , tN ). Hence (6.2) implies R̂S′(t) = R̂S(t′′). □

Corollary 6.16. Suppose that ̂S = (Sa,b)1≤a≤b≤N is multi-transitive, and that for all
a < b, Sa,b = S for some set S containing 0 and such that {−s, s ∈ S} = S. Then

Γ̂S(x, t) = xm+1 ∆(x, t)
1 − ν(x)∆(x, t) ,

where ∆(x, t) =
 N∑

a=1
 Λ(µa(x), νa(x), ta)
1 + ν(x)Λ(µa(x), νa(x), ta) , µa(x) = ∑

−d∈[−m..0]\Sa,a xd, νa(x) =

∑

d∈[m]\Sa,a xd, and ν(x) = ∑

d∈[m]\S xd.

Example 6.17. Let N = 2 and ̂S = (Sa,b)1≤a≤b≤2 with S1,1 = {−1, 0, 1}, S2,2 = {0, 1}
and S1,2 = {0}. Then with the notation of Corollary 6.16, we have ν(x) = x, ∆(x, t) =

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 25

t1
1 + t1x + et2x − 1
x + (et2x − 1)x and

Γ̂S(x, t) = − x (2 t1xet2x − t1x + et2x − 1)

t1xet2x − t1x − 1 .

Proof. Equation (6.12) can be rewritten as

Γa(x, t) = Λ(µa(x), νa(x), ta)(1 + ν(x)(Γ̂S(x, t)/xm+1 − Γa(x, t)).

Thus Γa(x, t) = Λ(µa(x), νa(x), ta)
1 + ν(x)Λ(µa(x), νa(x), ta) (1 + ν(x)Γ̂S(x, t)/xm+1), and

Γ̂S(x, t) = xm+1 N∑

a=1 Γa(x, t) = ∆(x, t) (x
m+1 + ν(x)Γ̂S(x, t)).
 □

Remark 6.18. Our results for the number of regions of a multi-transitive arrangement
ÂS(n) have been derived from (5.8) using the decomposition of boxed trees in ÛS(n).
They could alternately be obtained from (5.9) using the decomposition of trees in T̂S(n).
When Sa,b = −Sa,b for all a, b ∈ [N ] one can simply use the decomposition obtained by
deleting the root. In the general case, the decomposition would correspond to deleting
all the vertices in the longest cadet sequence starting at the root.

7. Proofs

As explained above, Theorem 5.2 implies Theorems 3.4 and Theorems 4.2. It re-
mains to prove Theorem 5.2. The proof breaks into three steps corresponding to Lem-
mas 7.1, 7.3, and 7.5 below.
We ﬁrst express the coboundary polynomial of any deformation of the braid arrange-
ment as a weighted count of graphs. We denote by Gn the set of graphs (without loops
nor multiple edges) with vertex set [n].

Lemma 7.1. Let n ∈ N, and let S = (Su,v)1≤u<v≤n be an (n
2)-tuple of ﬁnite sets of
integers, and let m = max(|s|, s ∈ ∪Su,v). The coboundary polynomial of AS is

PAS(q, y) = ∑

G∈Gn(y − 1)
e(G)qc(G)|WS(G)|,

where e(G) and c(G) are the number of edges and connected components of G respec-
tively, and WS(G) is the set of tuples (x1, . . . , xn) ∈ Zn such that
• for all edge {u, v} of G with u < v, xu − xv is in Su,v,
• for all vertex v of G such that v is smallest in its connected component, xv = 0.

Example 7.2. Let n = 3 and S1,2 = S1,3 = {−2, 1} and S2,3 = {−2, −1, 1}. Let G be
the graph with vertex set [3] and edges {1, 2} and {2, 3}. Then
WS(G) = {(0, −1, −2), (0, −1, 0), (0, −1, 1), (0, 2, 1), (0, 2, 3), (0, 2, 4)}.

26 OLIVIER BERNARDI

Proof. To a subarrangement B ⊆ AS, we associate the graph GB ∈ Gn with arcs {u, v}
for all u < v such that there exists s ∈ Su,v such that Ha,b,s ∈ B. We say that B is
central if ∩H∈BH ̸= ∅. If B is central, for each edge {u, v} of GB, with u < v, there
is a unique value s ∈ Su,v such that Hu,v,s ∈ B, and we denote this value B(u, v). We
also denote B(v, u) = −B(u, v). Clearly, a point (x1, . . . , xn) is in ⋂H∈B H if and only
if for any path v1, v2, . . . , vk in GB,

xv1 − xvk =
 k−1∑

i=1 B(vi, vi+1).

Hence, there is a unique point xB = (x1, . . . , xn) in ⋂H∈B H such that xv = 0 for all
v ∈ [n] such that v is the smallest vertex in its connected component of GB. Moreover,
dim(
⋂H∈B H) = c(GB). Note also that xB is in WS(GB), and that B is uniquely
determined by the pair (GB, xB). Lastly, any pair (G, x) where G ∈ Gn and x ∈ WS(G)
comes from a central subarrangement B. Thus,

PAS(q, y) = ∑

B⊆AS central(y − 1)
|B|qdim(
⋂H∈B H)

= ∑

(G,x), G∈Gn, x∈WS(G)
(y − 1)
e(G)qc(G)

= ∑

G∈Gn(y − 1)
e(G)qc(G)|WS(G)|.
 □

Our second step relates the generating function P̂S(q, y, t) of coboundary polynomi-
als, to a generating function ẐS(δ, y, t) of tuples of integers. We ﬁx N > 0 and an (N +1
2 )-
tuple ̂S = (Sa,b)1≤a<b≤N of ﬁnite sets of integers. As before, m = max(|s|, s ∈ ∪Sa,b)
and for n ∈ NN and u, v ∈ V (n) with u = (a, i), v = (b, j) and u < v, we denote
Su,v = Sa,b, Sv,u = Sa,b, S−
u,v = {s ≥ 0 | − s ∈ Sa,b}, and S−
v,u = {s > 0 | s ∈ Sa,b} ∪ {0}.
For a positive integer δ, and n ∈ NN , we denote

ẐS,n(δ, y) = ∑

x=(xv)v∈V (n)∈[δ]|n| yenergŷS(x),

where energŷS(x) is number of pairs (u, v) ∈ V (n)2, with u < v, such that xu − xv ∈
Su,v. For instance, the ̂S-energy of the tuple x in Figure 7 is 1. By convention, we set
ẐS,(0,...,0)(δ, y) = 1.

Lemma 7.3. The generating functions P̂S(q, y, t) and

ẐS(δ, y, t) = ∑

n∈NN ẐS,n(δ, y) tn

n! ,

are related by

(7.1) 1
q log(P̂S(q, y, t)) = lim
δ→∞ 1
δ log(ẐS(δ, y, t)).

Equation (7.1) is to be understood as an identity for formal power series in t1, . . . , tN :

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 27

1 6
2  = 22
ρ1 ρ2 ρ3 ρ4

1 42 5 33 4 2
1

Figure 7. Let δ = 22, N = 2, and n = (6, 4). In the ﬁgure, the tu-
ple x = (x1,1, . . . , x1,6, x2,1, . . . , x2,4) = (4, 13, 19, 13, 15, 3, 15, 21, 7, 12)
is represented by indicating a “round-particle” labeled i in position x1,i
for all i ∈ [6], and a “square-particle” labeled i in position x2,i for
all i ∈ [4]. For ̂S = (Sa,b)1≤a≤b≤N with S1,1 = S2,2 = {−1, 2} and
S1,2 = {−1, 0, 2}, the ̂S-energy is energŷS(x) = 1, given by the pair
{(1, 5), (2, 1)} (because x1,5 − x2,1 = 0 ∈ S(1,5),(2,1) = {−1, 0, 2}). The
tuple x has four runs ρ1, . . . , ρ4.

• the limit is taken coeﬃcient by coeﬃcient in t1, . . . , tN ,
• for a series in formal power series A(t1, . . . , tN ) such that A(0, . . . , 0) = 1, we
denote by log(A(t)) the formal power series ∑∞
n=1 (−1)n−1(A(t)−1)n
n .

Proof. Let Gn be the set of graphs with vertex set V (n), and let G(N ) = ⋃n∈NN Gn.
For G ∈ Gn, we denote by ŴS(G) the set of tuples (xv)v∈V (n) ∈ Z|n| such that
• for all edge {u, v} of G with u < v, xu − xv ∈ Su,v,
• for all vertex v of G which is smallest in its connected component, xv = 0.
Recall that the arrangement ÂS(n) identiﬁes with the arrangement ÂS(n), where the

tuple ̂S(n) is given by (5.2). Up to this identiﬁcation, Lemma 7.1 gives

PÂS(n)(q, y) = ∑

G∈Gn(y − 1)
e(G)qc(G)|ŴS(G)|,

hence

(7.2) P̂S(q, y, t) = ∑

n∈NN
 tn

n!
 ∑

G∈Gn(y − 1)
e(G)qc(G)|ŴS(G)|.

We now apply the multivariate exponential formula. We think of G(N ) as the combi-
natorial class of graphs with N types of vertices, with the vertices of each type being
well-labeled (that is, the na vertices of type a have distinct labels in [na]). The size
of G ∈ Gn is n = (n1, . . . , nN ) and the weight of G is (y − 1)e(G)qc(G)|ŴS(G)|. The
weight is multiplicative over connected components (and unchanged by order preserv-
ing relabeling of the vertices of each type). Hence the multivariate exponential formula
applies (see e.g. [44]), and taking the logarithm of P̂S(q, y, t) amounts to selecting the
connected graphs in G(N ). This gives,

(7.3) 1
q log(P̂S(q, y, t)) = ∑

n∈NN
 tn

n!
 ∑

G∈Gn connected(y − 1)
e(G)|ŴS(G)|.

28 OLIVIER BERNARDI

Next, observe that

|ẐS,n(δ, y)| = ∑

(xv)v∈V (n)∈[δ]|n|
 ∏

u,v∈V (n), u<v
 (1 + (y − 1) · 1xu−xv∈Su,v ) ,

= ∑

(xv)v∈V (n)∈[δ]|n|
 ∑

G∈Gn(y − 1)
e(G)
 

 ∏

{u,v} edge of G, u<v 1xu−xv∈Su,v
 

 ,

= ∑

G∈Gn(y − 1)
e(G)|ŴS,δ(G)|,

where 1 is the indicator function, and ŴS,δ(G) is the set of tuples (xv)v∈V (n) ∈ [δ]|n|

such that for all edge {u, v} of G with u < v, xu − xv ∈ Su,v. The graph weight (y −
1)e(G)|ŴS,δ(G)| is multiplicative over connected components, hence by the multivariate
exponential formula,

log(ẐS,δ(t)) = log
 

 ∑

n∈NN
 tn

n!
 ∑

G∈Gn(y − 1)
e(G)|ŴS,δ(G)|



 ,

= ∑

n∈NN
 tn

n!
 ∑

G∈Gn, connected(y − 1)
e(G)|ŴS,δ(G)|.(7.4)

It only remains to prove that for any connected graph G ∈ Gn,

(7.5) lim
δ→∞ 1
δ |ŴS,δ(G)| = |ŴS(G)|.

It is easy to see that, the tuples in ŴS,δ(G) are translations of tuples in ŴS(G), and
the number of translations is of order δ. More precisely,

ŴS,δ(G) = {(xv+θ)v∈V (n) | (xv)v∈V (n) ∈ ŴS(G), and 1−min(xv)v∈V (n) ≤ θ ≤ δ−max(xv)v∈V (n)}.

The tuples above are all distinct, and for any (xv)v∈V (n) ∈ ŴS(G), max(xv)v∈V (n) −
min(xv)v∈V (n) ≤ m · |n|. Thus

(δ − m · |n|) |ŴS(G)| ≤ |ŴS,δ(G)| ≤ δ |ŴS(G)|.

This shows (7.5), and completes the proof. □

Remark 7.4. The proof of Lemma 7.3 is reminiscent of Mayers’ theory of cluster inte-
grals (see e.g. [12, 30, 32]). In this perspective, the right-hand side of (7.1) corresponds
to the pressure of the inﬁnite volume limit of a discrete gas model (where particles of
type a and b interacts according to a soft-core potential of shape Sa,b, and energy of in-
teraction y). Alexander Postnikov also pointed out to the author that Lemma 7.3 could
alternatively be obtained by using the ﬁnite ﬁeld method pioneered by Athanasiadis [6]
and adapted to the calculation of coboundary polynomials in [1]. However, the situa-
tion of deformed braid arrangement is distinguished by the fact that the parameter q
appears merely as an exponent of the generating function P̂S(q, y, t); see (5.7). This
fact, which is a direct consequence of Lemma 7.1 and already appears in [43, Theorem
1.2], allows one to focus the remaining analysis on a single value of q, namely +∞.

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 29

Our last step, relates the generating function ẐS(δ, y, t) of point conﬁgurations to
the generating function of boxed trees.

Lemma 7.5. Let
ÛS(y, t) = ∑

n∈NN
 tn

n!
 ∑

(T,B)∈U (m)(n)
(−1)
|B|yenergŷS(T,B),

and U •
̂S(y, t) = ∑

n∈NN
 tn

n!
 ∑

(T,B)∈U (m)
S (n)

(|B| + leaf(T ))(−1)
|B|yenergŷS(T,B),

where leaf(T ) is the number leaves of T . For all n ∈ NN , and for all δ > m · |n|,

(7.6) ẐS,n(δ, y) = [t
n]ÛS(y, t)
−δ−m−2U •
̂S(y, t).

We will use a counting result about tuples of plane trees. We recall that the preﬁx
order of the vertices of a rooted plane tree is the total order for which any vertex v is
less than its children and all the descendants of v are less than the right siblings of v.

Claim 7.6. Let α, w1 . . . , wr be positive integers. Let τ (α; w1, . . . , wr) be the set of
tuples (T1, . . . , Tα), where T1, . . . , Tα are rooted plane trees, and Tα has a marked vertex,
such that, denoting ci,1, . . . , ci,ki the number of children of the nodes of Ti in preﬁx order,
one has
 (c1,1, . . . , c1,k1, c2,1, . . . , c2,k2, . . . , cα,1, . . . , cα,kα) = (w1, . . . , wr).

Then,
 |τ (α; w1, . . . , wr)| = (
α + w1 + · · · + wr
r
 )
.

Proof. The proof is represented in Figure 8. Let P be the set of lattice paths on Z
starting at 0, and having every step greater or equal to −1. Let P−1 be the set of paths
in P ending at −1, and let P +
−1 ⊂ P−1 be the subset of paths remaining non-negative
until the last step. Recall that the map φ which associates to a rooted plane tree T
the path P with steps c1 − 1, c2 − 1, . . . , cn − 1 where c1, . . . , cn are the number of
children of the vertices of T taken in preﬁx order is a bijection between rooted plane
trees and P +
−1 (see e.g. [44, Chapter 5.3]). Moreover by the cycle lemma, there is a
n-to-1 correspondence between the paths with n steps in P−1 and the paths with n
steps in P +
−1. Thus the map φ induces a bijection between P−1 and rooted plane trees
with a marked vertex.
Now let P(α; w1, . . . , wr) be the set of path in P having α+w1 +. . .+wr −r steps −1,
and r non-negative steps w1 − 1, . . . , wr − 1 in this order. Clearly, |P(α; w1, . . . , wr)| =(α+w1+···+wr
r ), and paths in P(α; w1, . . . , wr) ends at −α. We consider the decompo-
sition of paths in P(α; w1, . . . , wr) at the ﬁrst time they reach −1, −2, . . . , −α + 1, as
represented in Figure 8. This gives a bijection between P(α; w1, . . . , wr) and the set
of tuples (P1, . . . , Pα) such that P1, . . . , Pα−1 ∈ P +
−1, Pα ∈ P−1 and there is a total
of α + w1 + . . . + wr − r steps −1, and r non-negative steps w1, . . . , wr in this order.
Combining this decomposition with φ gives a bijection between P(α; w1, . . . , wr) and
τ (α; w1, . . . , wr), thereby proving the claim. □

30 OLIVIER BERNARDI
P1
 P2 P4P3P3 ˚

Figure 8. A path P in P(4; 2, 2, 1, 3, 2, 4, 1, 2, 4), and its decomposition
into four paths P1, . . . , P4 with P1, P2, P3 ∈ P +
−1, and P4 in P−1. Here
the vertical direction corresponds to the value of the path, while the
horizontal direction represents time.

Proof of Lemma 7.5. We will relate both sides of (7.6) to the generating function of
(m, N )-conﬁgurations (see Deﬁnition 6.1). Let (T, B) ∈ U (m)
S (n). We associate to
(T, B) a rooted plane tree R obtained by contracting each box into a node. More
precisely, if β = (v1, . . . , vk) is a cadet sequence in B, then we delete all the right
siblings of the nodes v2, . . . , vk (these are leaves of T ) and contract the edges (vi, vi+1)
of all i ∈ [k − 1]. If β corresponds to the pth node of R in preﬁx order of R, we denote
Lp = {v1, . . . , vk} and we denote by γp the (m, N )-conﬁguration corresponding to β
in the sense of Remark 6.2. Clearly, the boxed tree (T, B) is uniquely determined by
the triple (R, (γ1, . . . , γ|B|), (L1, . . . , L|B|)). Hence, the boxed trees (T, B) ∈ U (m)
S are
in bijection with triples (R, (γ1, . . . , γn), (L1, . . . , Ln)), where

• R is a rooted plane tree, and n is the number of nodes of R,
• γ1, . . . , γn are (m, N )-conﬁgurations of width child(v1), . . . , child(vn) respec-
tively, where v1, . . . , vn are the nodes of R in preﬁx order, and child(v) is the
number of children of the node v (including leaves),
• and (L1, . . . , Ln) is a set partition of V (|γ1| + · · · + |γn|) such that for all p ∈ [n],
|γp| = (kp,1, . . . , kp,N ), where kp,a = |{i | (a, i) ∈ Lp}|.

Lastly, there are (|γ1| + · · · + |γn|)!
∏n
p=1 |γp|!

ways to choose the set partition (L1, . . . , Ln). Hence

US(y, t) = ∑

R∈R
 ∏

v node of R
 

− ∑

γ∈C(m,N ) | wid(γ)=child(v) yenergyS(γ) t|γ|

|γ|!
 

 ,

where R is the set of rooted plane trees and C(m,N ) is the set of (m, M )-conﬁgurations.
Similarly,

U •
S(y, t) = ∑

R∈R v(R) ∏

v node of R
 

− ∑

γ∈C(m,N ) | wid(γ)=child(v) yenergyS(γ) t|γ|

|γ|!
 

 ,

where v(R) is the number of vertices of R.

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 31

Next, we express ẐS,n(δ, y) in terms of (m, N )-conﬁgurations. Let n ∈ NN , and let

x = (xv)v∈V (n) ∈ [δ]|n|. Intuitively, we think of each coordinate xv as the position of
a particle in the space [δ], and we will distinguish runs which are groups of particles
that are close to one another. This is represented in Figure 7. Let v′
1, . . . , v′
|n| ∈ V (n)
be deﬁned by {v′
1, . . . , v′
|n|} = V (n), and the conditions xv′
i ≤ xv′
i+1, and if xv′
i = xv′
i+1
then v′
i < v′
i+1. We denote di = xv′
i+1 − xv′
i for all i ∈ [|n| − 1], and adopt the
convention d0 = d|n| = ∞. A run of x is a subsequence ρ = (v′
i, v′
i+1, . . . , v′
j), with
1 ≤ i ≤ j ≤ |n|, such that di−1 > m, dj > m, and for all i ≤ p < j, dp ≤ m. We deﬁne
the position of ρ as pos(ρ) = xv′
i, the width of ρ as wid(ρ) = xv′
j − xv′
i + m + 1, the
labels of ρ as lab(ρ) = {v′
i, . . . , v′
j}, and the size of ρ as |ρ| = k = (k1, . . . , kN ) where
ka = |{i | (a, i) ∈ lab(ρ)}|. For instance, the tuple x represented in Figure 7 has four
runs having position 3, 7, 12, and 19 respectively, width 4, 3, 6, and 5 respectively,
and size (2, 0), (0, 1), (3, 2), and (1, 1) respectively. Lastly, the conﬁguration of ρ is
conﬁg(ρ) = ((di, di+1, . . . , dj−1), (ui, . . . , uj)), where (ui, . . . , uj) is the unique order
preserving relabeling of (v′
i, . . . , v′
j) in V (k). For instance, in Figure 7, conﬁg(ρ3) =
((1, 0, 2, 0), ((2, 2), (1, 1), (1, 2), (1, 3), (2, 1))). Note that γ = conﬁg(ρ) is in C(m)(k), and
wid(ρ) = wid(γ). Moreover it is easy to see that

energŷS(x) =
 r∑

i=1 energŷS(conﬁg(ρi)),

where ρ1, . . . , ρr are the runs of x (because pairs of particles at distance greater than
m do not contribute to the ̂S-energy). Moreover, the tuple x is completely determined
by the positions, labels, and conﬁgurations of its runs ρ1, . . . , ρr. The conﬁgurations of
the runs are arbitrary, and given the conﬁgurations γ1, . . . , γr of the runs there are
(δ + m + r − wid(γ1) − . . . − wid(γr)
r
 )

ways to choose the positions (p1, . . . , pr) ∈ [δ]r (since the only constraints are pi +
wid(γi) ≤ pi+1 for all i ∈ [r − 1], and pr + wid(γr) ≤ δ + m + 1). Also, there are
n!
∏r
i=1 |γi|! ways to choose the labels. Thus,

(7.7)

ẐS,n(δ, y) = n!
 ∞∑

r=0
 ∑

γ1,...,γr ∈C(m,N )

|γ1|+···+|γr |=n
 (δ + m + r − wid(γ1) − · · · − wid(γr)
r
 ) r∏

i=1
 yenergŷS(γi)

|γi|! .

In order to prove (7.6), we will now consider negative values of δ. Let us denote
Polr(x) = x(x−1)···(x−r+1)
r! . This is a polynomial in x, such that for all x ∈ N, (x
r) =
Polr(x). Let
(7.8)

̃ẐS,n(δ, y) = n!
 ∞∑

r=0
 ∑

γ1,...,γr ∈C(m,N )

|γ1|+···+|γr |=n
 Polr (δ + m + r − wid(γ1) − · · · − wid(γr))
 r∏

i=1
 yenergŷS(γi)

|γi|! .

32 OLIVIER BERNARDI

This is a polynomial in δ and y which coincides with ẐS,n(δ, y) for all integer δ > m·|n|,

because any γ ∈ C(m,N ) satisﬁes wid(γ) − 1 ≤ m · |γ|. It remains to prove that for all δ,

(7.9) ̃ẐS,n(δ, y) = [tn]ÛS(y, t)
−δ−m−2U •
̂S(y, t).

We observe that both sides of (7.9) are polynomials in δ. Indeed, ÛS(y, (0, . . . , 0)) = 1,
hence the series

ÛS(y, t)
−δ = exp(−δ log(US(y, t)) = exp
 

δ ∑

k≥1
 (1 − US(t))k

k
 



has coeﬃcients which are polynomial in δ. Thus, in order to prove (7.9), it suﬃces
to prove it for inﬁnitely many values of δ ∈ C. Let α be a positive integer, let δ =
−m − 1 − α, and let
 ̃ẐS(δ, y, t) = ∑

n∈NN
 tn

n! ̃ẐS,n(δ, y).

We have

̃ẐS(δ, y, t) =
 ∞∑

r=0
 ∑

γ1,...,γr∈C(m,N ) Polr (r − 1 − α − wid(γ1) − · · · − wid(γr))
 r∏

i=1
 yenergŷS(γi)t|γi|

|γi|!

=
 ∞∑

r=0
 ∑

γ1,...,γr∈C(m,N )(−1)
r(
α + wid(γ1) + · · · + wid(γr)
r
 ) r∏

i=1
 yenergŷS(γi)t|γi|

|γi|! .

Using Claim 7.6 gives

̃ẐS(δ, y, t) =
 ∞∑

r=0(−1)
r ∑

γ1,...,γr∈C(m,N ) τ (α; wid(γ1), . . . , wid(γr))
 r∏

i=1
 yenergŷS(γi)t|γi|

|γi|!

=
 

 ∑

R∈R
 ∏

v node of R − ∑

γ∈C(m,N ), wid(γ)=child(v)
 yenergŷS(γ)t|γ|

|γ|!
 



α−1

×
 

 ∑

R∈R v(R) ∏

v node of R − ∑

γ∈C(m,N ), wid(γ)=child(v)
 yenergŷS(γ)t|γ|

|γ|!
 



= ÛS(y, t)−δ−m−2U •
̂S(y, t).

for all δ ≤ −m − 2. Thus, ̃ẐS(δ, y, t) = ÛS(y, t)
−δ−m−2U •
̂S(y, t) for all δ ∈ C, and
extracting the coeﬃcient of tn gives (7.9). □

We can now complete the proof of Theorem 5.2. By Lemma 7.5,

lim
δ→∞
 ẐS,δ(δ, y, t)

ÛS(y, t)−δ−m−2U •
̂S(y, t) = 1,

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 33

where the limit is taken coeﬃcient by coeﬃcient in t. Thus, by Lemma 7.3,
1
q log(P̂S(q, y, t)) = lim
δ→∞ 1
δ log(ẐS,δ(δ, y, t))

= lim
δ→∞ −δ − m − 2
δ log (ÛS(y, t)
) + lim
δ→∞ 1
δ log (U •
̂S(y, t)
)

+ lim
δ→∞ log
 ( ẐS,δ(δ, y, t)

ÛS(y, t)−δ−m−2U •
̂S(y, t)
 )

= − log(ÛS(y, t)).

Hence,

P̂S(q, y, t) = (ÛS(y, t))
−q =
 

 ∑

n∈NN
 tn

n!
 ∑

(T,B)∈U (m)(n)
(−1)
|B|yenergŷS(T,B)



−q
 .

This gives (5.6), and setting y = 0 gives (5.8). Lastly, in the case where ̂S is multi-
transitive, (5.9) follows from (5.8) via (4.2).

8. A simple bijection for regions of transitive deformations of the
braid arrangement

In this section we present a simple bijection between regions of the arrangement AS
and the trees in TS(n) for any transitive tuple S. We ﬁrst recall a bijection between the
regions of A(m)(n) and labeled parenthesis systems in Subsection 8.1, and combine it
with a convenient bijection between parenthesis systems and trees. Then, we treat the
cases of the Shi, semiorder and Linial arrangements in Subsection 8.2, before treating
the general case in Subsection 8.3.

8.1. Preliminary: bijection between regions of A[−m..m](n) and T (m)(n).
We ﬁrst recall a classical encoding of the regions of A[−m..m](n) by labeled, non-nesting,
parenthesis systems. An example is represented in Figure 9.
A m-parenthesis system of size n is a word w on the alphabet {α, β} with n letters
α and mn letters β, such that no preﬁx of w contains more β’s than m times the
number of α’s. It is well known that there are Cat(m)(n) = ((m+1)n)!
n!(mn+1)! m-parenthesis
systems of size n, and that such words bijectively encode rooted plane (m + 1)-ary trees
with n nodes (see e.g. [44, Chapter 5.3]). A m-sketch of size n is a word ˜w obtained
from a parenthesis system w by replacing the ith letter α by the letter απ(i) for some
permutation π of [n]. We denote by ˜D(m)(n) the set of m-sketches of size n. Clearly,
| ˜D(m)(n)| = n!Cat
(m)(n) = ((m+1)n)!
(mn+1)! = |T (m)(n)|. We now describe bijections between

the regions of A[−m..m](n), and the sets ˜D(m)(n) and T (m)(n). The case m = 1, n = 3
is represented in Figures 10 and 13.
We ﬁrst need to annotate our sketches. Let A(m)(n) be the alphabet made of the
(m + 1)n letters {α(s)
i | i ∈ [n], s ∈ [0..m]}. We call α-letters the letters α(0)
i for i ∈ [n],
and β-letters the letters α(s)
i for i ∈ [n], s ∈ [m]. For a word ˆw on the alphabet A(m)(n),
we say that the letter α(s)
i is active in ˆw if s < m, and α(s)
i appears in ˆw but α(s+1)
i does

34 OLIVIER BERNARDI

not. The annotation of a sketch ˜w = ˜w1 · · · ˜w(m+1)n is the word ˆw = ˆw1 · · · ˆw(m+1)n
obtained by applying the following rule for p = 1, 2, . . . , (m + 1)n: if ˜wp = αi then
set ˆwp = α(0)
i , while if ˜wp = β then set ˆwp = α(s+1)
i , where α(s)
i is the ﬁrst active
letter in ˆw1 · · · ˆwp−1 (it is easy to see that there is always such a letter). We denote
by D(m)(n) the set of annotated m-sketches of size n. It is easy to see that a word
ˆw = ˆw1 · · · ˆw(m+1)n is in D(m)(n) if and only if
(a) { ˆw1, . . . , ˆw(m+1)n} = A(m)(n),

(b) for all i ∈ [n] and all s ∈ [m], the letter α(s−1)
i appears before α(s)
i ,
(c) for all i, j ∈ [n] and all s, t ∈ [m], if α(s−1)
i appears before α(t−1)
j , then α(s)
i
appears before α(t)
j .

x 1

x 3 x 2

( x 1; x 2; x 3)

x 3 x 1 x 2x 3 x 2x 1+1x 3+1 x 2+1
 3 1 2

 (0)
3  (0)
1  (1)
3  (1)
1  (0)
2  (1)
2

˙ 1

Figure 9. The mapping σ1 associating an annotated 1-sketch to any
point (x1, . . . , xn) in Rn\⋃H∈A[−1..1](n) H. Graphically, the annotated 1-
sketch ˆw = ˆw1 · · · ˆw2n is represented by a set of non-nesting parentheses
on 2n-points corresponding to the letters. More precisely, if the letters
α(0)
i to α(1)
i are in position p and q of ˆw, then parenthesis labeled i goes
from the pth point to the qth point.

We now associate an annotated m-sketch of size n to each region of A[−m..m](n).
Let x = (x1, . . . , xn) be a point in Rn \ ⋃H∈A[−m..m](n) H. Observe that the condition
x /∈ ⋃H∈A[−m..m](n) H is equivalent to the fact that the numbers {xi + s | i ∈ [n], s ∈
[0..m]} are all distinct. We deﬁne z1, . . . , z(m+1)n by the conditions z1 < . . . < z(m+1)n
and {z1, . . . , z(m+1)n} = {xi + s | i ∈ [n], s ∈ [0..m]}. Then, we deﬁne σm(x) =

ˆw1 ˆw2 · · · ˆw(m+1)n, where ˆwp = α(s)
i if zp = xi + s. Here are basic properties of the
mapping σm.
(i) For any x /∈ ⋃H∈A[−m..m](n) H, the word σm(x) is an annotated m-sketch. In-
deed, it clearly satisﬁes the conditions (a), (b), (c).
(ii) The mapping σm is constant over each region of A[−m..m](n). Indeed, the order
of the numbers {xi + s | i ∈ [n], s ∈ [0..m]} cannot change when x moves
continuously inside Rn \ ⋃H∈A[−m..m](n) H.
(iii) The sketch σm(x) identiﬁes the region containing x. Indeed, for all i, j ∈ [n],
and all s ∈ [0..m], xi−xj < s if α(0)
i appears before α(s)
j in σm(x) and xi−xj > s
otherwise.

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 35

(iv) For any annotated m-sketch ˆw = ˆw1 · · · ˆw(m+1)n, there exists x ∈ Rn\
⋃H∈A[−m..m](n) H

such that σ(x) = ˆw. Indeed, one can simultaneously deﬁne x ∈ σ−1( ˆw) and
z1, . . . , z(m+1)n by applying the following rules for p = 1, 2, . . . , (m + 1)n: if

ˆwp = α(0)
i , then set zp = zp−1 + 1/2p (with z0 = 0) and set xi = zp, while if
ˆwp = α(s)
i with s ̸= 0, then set zp = xi + s.
Properties (i) and (ii) show that σm is a mapping from the regions of A[−m..m](n) to
D(m)(n). Properties (iii) and (iv) imply that σm is a bijection. In particular, this shows
that A[−m..m](n) has ((m+1)n)!
(mn+1)! regions. The bijection σ1 is represented in Figure 10.
Note that (iii) gives the inverse bijection σ−1
m in terms of inequality, while (iv) gives an
explicit point in σ−1
m ( ˆw).
Next, we describe a bijection φm between D(m)(n) and the set T (m)(n) of (m+1)-ary
trees with labeled nodes8. Let T be a rooted plane tree. We deﬁne the drift of a vertex
v of T as drift(v) = lsib(u1) + · · · + lsib(uk), where u0, u1, . . . , uk = v are the vertices
on the path from the root u0 to v. We deﬁne the total order ≺T on vertices of T by
setting u ≺T v if either drift(u) < drift(v), or drift(u) = drift(v) and u appears before
v in the postﬁx order of T (recall that the postﬁx order is the order of appearance of
the vertices when turning counterclockwise around the tree starting at the root). The
order ≺T is represented in Figure 11(a).
Let ˜T (n) be the set of rooted plane trees, with (at most n) nodes labeled with
distinct numbers in [n], and some special leaves called buds (see Figure 12). If T
has some buds, we call ﬁrst bud the least bud of T for the order ≺T . Let ˆw =
ˆw1 . . . ˆw(m+1)n ∈ D(m)(n), and let ˆwp = ˆw1 . . . ˆwp be its preﬁx of length p. We de-
ﬁne the trees ˜φm( ˆw0), . . . , ˜φm( ˆw(m+1)n) ∈ ˜T (n) as follows:
• ˜φm( ˆw0) is the tree with one bud and no other vertex,
• if p > 0 and ˆwp = α(s)
i with s > 0, then ˜φm( ˆwp) is obtained from ˜φ( ˆwp−1) by
replacing its ﬁrst bud by a (non-bud) leaf,
• if p > 0 and ˆwp = α(0)
i , then ˜φm( ˆwp) is obtained from ˜φ( ˆwp−1) by replacing its
ﬁrst bud by a node labeled i with m + 1 children, all of them buds.
The trees ˜φ( ˆwp) are represented in Figure 12. It is clear, by induction on p, that
˜φm( ˆwp) has 1 + m nα − nβ buds, where nα and nβ are respectively the number of α-
letters and β-letters in ˆwp. In particular ˜φm( ˆwp) has at least one bud, so that ˜φm is
well deﬁned, and ˜φm( ˆw) has exactly one bud. We denote by φm( ˆw) the tree in T (m)(n)
obtained from ˜φm( ˆw) by replacing its bud by a leaf; see Figure 11(b). Before showing
that φm is a bijection, we describe the inverse mapping ψm. Let T ∈ T (m)(n) and let
u0 ≺T u1 ≺T · · · ≺T u(m+1)n be the vertices of T (T has n nodes and mn + 1 leaves).
Let ψm(T ) be the word ˆw = ˆw1 . . . ˆw(m+1)n deﬁned as follows: for all p ∈ [(m + 1)n], if

up is the (s + 1)st child of the node i, then ˆwp = α(s)
i .

8Of course, any classical bijection between m-parenthesis systems and (m + 1)-ary trees induces a
bijection between D(m)(n) and T (m)(n) (by sending labels from the parentheses to the nodes). The
non-classical bijection φm is chosen because it is well adapted to the “non-nesting” nature of annotated
sketches.

36 OLIVIER BERNARDI
x1
 x3x2
 1 2 31 3 2

3 1 2 2 1 3

2 3 13 2 1

3 21 2 31

1 23 1 32

2 133 12
 1 23 1 32
 2 313 21
 3 12 2 13

1 23 1 32
 2 31

2 133 12

3 21
 1 32
 2 313 21
 1 23
 3 12 2 13

B
 A
 B
 A A
 AA
 B
 B
 B

B

A

A

A
 A+B

B
 B
 B

B

A+B
 A+B A+B

A+BA+B

A+B

A A

A

Figure 10. The Catalan arrangement A{−1,0,1}(3), and the annotated
1-sketches corresponding to each region. The sketches marked A are
Shi maximal, the sketches marked B are semiorder maximal, and those
marked both A and B are Linial maximal.

Proposition 8.1. The mapping φm is a bijection between D(m)(n) and T (m)(n). The
inverse mapping is ψm. Moreover, for ˆw ∈ D(m)(n), if the letter following α(s)
i in ˆw is
α(t)
j , then the (s + 1)st child of the node i in T = φm( ˆw) is the node j if t = 0, and a
leaf otherwise.

Proof. First note that for all T ∈ T (m)(n), the word ψm(T ) clearly satisﬁes the prop-
erties (a), (b), (c) of annotated m-sketches. Hence ψm is a mapping from T (m)(n) to
D(m)(n).
 DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 37

3 1 4 2
5 1
 3
 5
4 2

˚ 1postx order

(a) (b)

c
 h
 gg
 m p

l

f
 e
 k
 o

p
 sq
 r

o

k
 j
 i

d

a
 nj

b
 Figure 11. (a) The order ≺T for this binary tree T is a ≺T
b ≺T c ≺T d ≺T · · · ≺T s. (b) The annotated 1-sketch ˆw =
α(0)
3 α(0)
1 α(1)
3 α(0)
5 α(0)
4 α(1)
1 α(1)
5 α(1)
4 α(0)
2 α(1)
2 , and the associated tree φ1( ˆw) ∈
T (1)(5).

3 1
 3
 1
 3
 1
 3
 5 1
 3
 5
4

1
 3
 5
4 1
 3
 5
4 1
 3
 5
4 2
 1
 3
 5
4

1
 3
 5
4 2

 (0)
3  (0)
1

 (1)
5  (1)
4  (0)
2  (1)
2

 (1)
3  (0)
5  (0)
4  (1)
1

Figure 12. The trees ˜φm( ˆw0), . . . , ˜φm( ˆw(m+1)n) for ˆw =
α(0)
3 α(0)
1 α(1)
3 α(0)
5 α(0)
4 α(1)
1 α(1)
5 α(1)
4 α(0)
2 α(1)
2 . Buds are represented by
triangles, and leaves by dots.

Next we give an alternative description of ψm. Let T ∈ T (m)(n), and let u0 ≺T
u1 ≺T · · · ≺T u(m+1)n be its vertices. Let ˜ψm(T ) be the word ˜w = ˜w1 . . . ˜w(m+1)n,
where ˜wp = αi if up−1 is the node labeled i, and ˜wp = β if up−1 is a leaf. We now
show that ˆw = ψm(T ) is the annotation of ˜w = ˜ψm(T ). It is easy to see that for
all q ∈ [0..(m + 1)n], if the vertex uq is a node, then uq+1 is its ﬁrst child. Now let
p ∈ [(m + 1)n] such that ˆwp = α(0)
i for some i ∈ [n]. In this case up is the ﬁrst child of
the node i, hence up−1 is the node i and ˜wp = αi. Suppose now that p ∈ [(m + 1)n] is
such that ˆwp = α(s)
i for some s ∈ [m], i ∈ [n]. In this case up is not a ﬁrst child, thus
up−1 is a leaf and ˜wp = β. This proves that ˆw = ψm(T ) is indeed the annotation of
˜w = ˜ψm(T ).

38 OLIVIER BERNARDI

Next we prove that ψm ◦ φm = Id and φm ◦ ψm = Id. Let ˆw ∈ T (m)(n), and let ˆwp be
the preﬁx of length p. Let T = φ( ˆw), and let T p = ˜φm( ˆwp). We claim that the order in
which the non-bud vertices are created in the sequence ˜φm( ˆw0), ˜φm( ˆw1) . . . , ˜φm( ˆw(m+1)n), φm( ˆw)
is the same as the order ≺T . Indeed, for all p ∈ [(m+1)n] the order ≺T p on the vertices
of T p coincide with the order ≺T . So the ﬁrst bud of T p is less than any bud of T p+1 for
the order ≺T . This establish the claim. From the claim, and the alternative description
of ψm it follows directly that ψm ◦ φm( ˆw) = ˆw. And since |D(m)(n)| = |T (m)(n)|, φm
and ψm are inverse bijections.
Lastly, suppose that for ˆw ∈ D(m)(n) we have ˆwp = α(s)
i and ˆwp+1 = α(t)
j . In this
case, up is the (s + 1)st child of the node i (by deﬁnition of ψm) and up is the node j
if s = 0 and a leaf otherwise (by deﬁnition of ˜ψm). □

Let Φm = φm ◦ σm be the bijection from the the regions of A[−m..m](n) to T (m)(n),
and let Ψm = σ−1
m ◦ ψm its inverse.

Lemma 8.2. For T ∈ T (m)(n), Ψm(T ) is the region of A[−m..m](n) made of the points
x = (x1, . . . , xn) satisfying the following inequalities for all distinct integers i, j ∈ [n],
and all s ∈ [0..m]: xi − xj < s if i ≺T v where v is the (s + 1)st child of the node j,
and xi − xj > s otherwise.

Proof. Let x ∈ Ψm(T ) = ψm(σ−1
m (T ). By Property (iii) of σm, xi − xj < s if and only
if α(0)
i appears before α(s)
j in ˆw = ψm(T ). By deﬁnition of ψm, this happens if and only
if u ≺T v, where u is the ﬁrst child of the node i. Moreover, since u ̸= v and u is the
successor of i in the ≺T order, this happens if and only if i ≺T v. □

8.2. Bijections for the Shi, semiorder, and Linial arrangements.
In this section we give a bijection between the regions of AS(n), and the trees in TS for
all S ⊆ {−1, 0, 1}. Up to symmetry, the interesting cases are S = {−1, 0, 1} (Catalan
arrangement), S = {0, 1} (Shi arrangement), S = {−1, 1} (semiorder arrangement),
S = {1} (Linial arrangement), and S = {0} (braid arrangement). We already treated
the case S = {−1, 0, 1} in the previous Section. For the Shi arrangements our bijection
can be seen as a relative to [11] as discussed in Section 9.1. The bijection for the
semiorder and Linial arrangements seem to be new.
The basic idea of our bijection for the Shi, semiorder, and Linial arrangements is
to think of regions in these arrangements as union of regions of the Catalan arrange-
ment. Then we will choose a canonical representative among these regions, so as to
identify regions of the Shi, semiorder and Linial arrangements with certain canonical
1-sketches. We show that the bijection φ1 between D(1)(n) and T (1)(n) induces bijec-
tions between the canonical 1-sketches for A{0,1}(n), A{−1,1}(n), and A{1}(n) and the
trees in T{0,1}(n), T{−1,1}(n), and T{1}(n) respectively. This is represented in Figure 13.
Moreover, the bijections induced by Φ1 = φ1 ◦ σ1 between regions and trees have simple
inverses.

Deﬁnition 8.3. Let ˆw and ˆw′ be annotated 1-sketches of size n. We say that ˆw and
ˆw′ are related by a Shi move if ˆw′ is obtained from ˆw by swapping two consecutive
letters α(1)
i and α(0)
j with i < j. We say that ˆw and ˆw′ are related by a semiorder move

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 39

if ˆw′ is obtained from ˆw by swapping two consecutive letters α(0)
i and α(0)
j and also two

consecutive letters α(1)
i and α(1)
j (for the same pair {i, j}). We say that ˆw and ˆw′ are
related by a Linial move if they are related by either a Shi or semiorder move. Lastly,
we say that ˆw and ˆw′ are Shi equivalent (resp. semiorder equivalent, Linial equivalent)
if one can be obtained from the other by performing a series of Shi (resp. semiorder,
Linial) moves.

Let ˆw, ˆw′ ∈ D(1)(n) be annotated 1-sketches. Let ρ = σ−1( ˆw) and ρ′ = σ−1( ˆw′)
be the regions of A{−1,0,1}(n) corresponding to ˆw and ˆw′. Observe that ˆw and ˆw′ are

related by the Shi move swapping α(0)
i and α(1)
j if and only if the regions ρ and ρ′ are
separated only by the hyperplane Hi,j,−1 = {xi − xj = −1}. Thus, ˆw and ˆw′ are Shi
equivalent if and only if one can go from ρ to ρ′ only crossing hyperplanes of the forms
Hi,j,−1 for i < j. In other words, ˆw and ˆw′ are Shi equivalent if and only if ρ and ρ′ are
contained in the same region of the Shi arrangement A{0,1}(n). Similarly, ˆw and ˆw′ are

related by the semiorder move swapping α(0)
i and α(0)
j (and α(1)
i and α(1)
j ) if and only if
the regions ρ to ρ′ are separated only by the hyperplane Hi,j,0 = {xi −xj = 0}. Thus, ˆw
and ˆw′ are semiorder equivalent if and only if ρ and ρ′ are contained in the same region
of the semiorder arrangement A{−1,1}(n). Also, ˆw and ˆw′ are Linial equivalent if and
only if ρ and ρ′ are contained in the same region of the Linial arrangement A{1}(n).
To summarize:

Lemma 8.4. Let ˆw and ˆw′ be annotated 1-sketches of size n, and let ρ = σ−1( ˆw) and
ρ′ = σ−1( ˆw′) be the regions of A{−1,0,1}(n) corresponding to ˆw and ˆw′. The annotated
1-sketches ˆw and ˆw′ are Shi (resp. semiorder, Linial) equivalent if and only if ρ and ρ′

are contained in the same region of A{0,1}(n) (resp. A{−1,1}(n), A{1}(n)).

We consider the lexicographic order ≺ on D(1)(n) given by the following order on
the alphabet: α(1)
1 ≺ α(1)
2 ≺ · · · ≺ α(1)
n ≺ α(0)
1 ≺ α(0)
2 ≺ · · · ≺ α(0)
n . We say that an
annotated 1-sketch ˆw is Shi locally-maximal (resp. semiorder locally-maximal, Linial
locally-maximal ) if it is larger than any 1-sketch obtained from ˆw by a single Shi (resp.
semiorder, Linial) move. We say that an annotated 1-sketch ˆw is Shi maximal (resp.
semiorder maximal, Linial maximal ) if it is larger than any Shi (resp. semiorder, Linial)
equivalent 1-sketch. The maximal 1-sketches are indicated in Figure 10.
On the one hand, Lemma 8.4 implies that regions of A{0,1}(n) (resp. A{−1,1}(n),
A{1}(n)) are in bijection with Shi (resp. semiorder, Linial) maximal 1-sketches in
D(1)(n). On the other hand, locally-maximal 1-sketches are easy to characterize. The
following result shows that the two notions actually coincide.

Lemma 8.5. An annotated 1-sketch ˆw ∈ D(1)(n) is Shi (resp. semiorder, Linial)
maximal if and only if it is Shi (resp. semiorder, Linial) locally-maximal.

Before proving Lemma 8.5 we explore its consequences.

Corollary 8.6. The mapping Ψ1 = Φ
−1
1 between T (1)(n) and the regions of A{−1,0,1}(n)
induces a bijection Ψ{0,1} (resp. Ψ{−1,1}, Ψ{1}) between the trees in T{0,1}(n) (resp.
T{−1,1}(n), T{1}(n)) and the regions of A{0,1}(n) (resp. A{−1,1}(n), A{1}(n)).

40 OLIVIER BERNARDI

(1) For T ∈ T{0,1}(n) the region Ψ{0,1}(T ) is deﬁned by the following inequalities
for all 1 ≤ i < j ≤ n: xi − xj < 0 iﬀ i ≺T j (that is to say, node i is less than
node j for the ≺T order), and xi − xj < 1 iﬀ i ≺T v, where v is the right child
of j.
(2) For T ∈ T{−1,1}(n) the region Ψ{−1,1}(T ) is deﬁned by the following inequalities
for all 1 ≤ i < j ≤ n: xi − xj > −1 iﬀ j ≺T u, and xi − xj < 1 iﬀ i ≺T v,
where u is the right child of i and v is the right child of j.
(3) For T ∈ T{1}(n) the region Ψ{1}(T ) is deﬁned by the following inequalities for
all 1 ≤ i < j ≤ n: xi − xj < 1 iﬀ i ≺T v, where v is the right child of j.

Corollary 8.6 is illustrated in Figure 13.

Remark 8.7. The method used above works just as well for the braid arrangement: the
induced bijection is between the regions of A{0}(n) and the binary trees with no right
child. These trees (which look like paths) are the ones near the origin in Figure 13 (note
that they are a subsets of the Shi trees). Of course, such a machinery is unnecessary
for this simple case, which could be treated with m = 0, but it illustrates the fact
that arrangements corresponding to small values of m are embedded in the bijective
framework corresponding to larger values of m.

Proof of Corollary 8.6. It is clear that an annotated 1-sketch ˆw is Shi locally-maximal
if and only if for all i ∈ [n] the letter α(1)
i is not followed by a letter α(0)
j with j > i. By
Proposition 8.1, this means that ˆw is Shi locally-maximal if and only if for all i ∈ [n]
the right child of the node i in T = φ1( ˆw) is not a node j with j > i. In other words,
ˆw is Shi locally-maximal if and only if φ1( ˆw) is in T{0,1}.
Similarly, an annotated 1-sketch ˆw is semiorder locally-maximal if and only if for all
i ∈ [n] the letters α(0)
i and α(1)
i are not followed by the letters α(0)
j and α(1)
j respectively,

with j > i. Note that if α(0)
i is followed by α(0)
j and α(1)
i is followed by a β-letter, then

this letter is necessarily α(1)
j . Thus, by Proposition 8.1, ˆw is semiorder locally-maximal
if and only if no node i ∈ [n] of T has both a left child which is a node j > i and a
right child which is a leaf. Thus, ˆw is semiorder locally-maximal if and only if φ1( ˆw) is
in T{−1,1}.
Lastly, an annotated 1-sketch ˆw is Linial locally-maximal if and only if it is both
Shi locally-maximal and semiorder locally-maximal. Thus ˆw is Linial locally-maximal
if and only if φ1( ˆw) is in T{0,1} ∩ T{−1,1} = T{1}.
Moreover, the description of the bijection ΨS is immediate from Lemma 8.2 as the
inequalities deﬁning the region ΨS(T ) are a subset of the inequalities deﬁning the region
Ψ1(T ) (the inequalities of the form xi − xj < s or xi − xj > s for i < j and s ∈ S). □

Proof of Lemma 8.5. We ﬁrst treat the case of the Shi arrangement. Let ˆw = ˆw1 · · · ˆw2n
and ˆw′ = ˆw′
1 · · · ˆw′
2n be two 1-sketches. Suppose that ˆw and ˆw′ are Shi equivalent. It is
easy to see (by induction on the number of Shi moves), that
(a) for all i, j ∈ [n], α(0)
i appears before α(0)
j in ˆw if and only if α(0)
i appears before

α(0)
j in ˆw′,

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 41
x1
 x3x2
 1

2

3

3

1

2
 2

3

1
 2

1

3

1

3

2
 3

2

1
 1
 32

1
 23
 2
 31

3
 21
 3
 12
 2
 13

1
 2

3

1
 3

2
 2
 1

3

2
 3

1

3
 2

1

3
 3

3

3
 1

2
 1

2
 3
 2

1
 3

3

1
 2
 1

3
 2
 2

3
 1

3

2
 1
 1
 2
 3

1
 3
 2

3
 1
 2
 2
 1
 3

2
 3
 1

3
 2
 1

B
 B
 A+B
 B
 A+B
 A

A

B

B B
 B
 B

A+B
 BA+B

A+B

A
 B

A
 B

A

A
 B

A+B A

A A

A+B

Figure 13. The Catalan arrangement A{−1,0,1}(3), and the labeled bi-
nary trees corresponding to each region. The trees marked A (including
those denoted A+B) are in bijection with the regions of the Shi arrange-
ment A{0,1}(3). The trees marked B (including those denoted A+B) are
in bijection with the regions of the semiorder arrangement A{−1,1}(3).
The trees marked A + B are in bijection with the regions of the Linial
arrangement A{1}(3).

(b) for all i > j ∈ [n], α(1)
i appears before α(0)
j in ˆw if and only if α(1)
i appears

before α(0)
j in ˆw′.
Now suppose that ˆw is Shi locally-maximal and ˆw′ is Shi maximal. We want to show
ˆw = ˆw′. Suppose by contradiction that they are diﬀerent, and let p ∈ [2n] be such that
ˆwp ̸= ˆw′
p and ˆwk = ˆw′
k for all k ∈ [p − 1]. Since ˆw ≺ ˆw′, either

42 OLIVIER BERNARDI

(i) ˆwp = α(1)
i and ˆw′
p = α(1)
j with i < j,

(ii) ˆwp = α(0)
i and ˆw′
p = α(0)
j with i < j,

(iii) ˆwp = α(1)
i and ˆw′
p = α(0)
j for some i, j.

However case (i) is impossible for 1-sketches: if ˆwk = ˆw′
k for all k ∈ [p − 1], ˆwp = α(1)
i
and ˆw′
p = α(1)
j then i = j. Moreover case (ii) is impossible by (a). Hence (iii) holds.

Let q > p be such that ˆwq = α(0)
j . By (a) and (b), we must have ˆwq−1 = α(1)
k with
k < j. But this contradicts the fact that ˆw is Shi locally-maximal. Hence ˆw = ˆw′ as
wanted.
Next, we treat the case of the semiorder arrangement. Given ˆw ∈ D1(n), we say
that i, j ∈ [n] are ˆw-exchangeable if in ˆw the letters α(0)
i and α(0)
j are separated only

by α-letters, and α(1)
i and α(1)
j are separated only by β-letters. Let ˆw, ˆw′ ∈ D(1)(n) be
two semiorder equivalent 1-sketches. It is easy to see that ˆw′ is obtained from ˆw by
replacing the letters α(0)
i and α(1)
i by α(0)
π(i) and α(1)
π(i) for a permutation π of [n] such
that for all i ∈ [n], i and π(i) are ˆw-exchangeable. Now suppose that ˆw is semiorder
locally-maximal and ˆw′ is semiorder maximal. We want to show ˆw = ˆw′. Suppose
by contradiction that they are diﬀerent, and let p ∈ [2n] be such that ˆwp ̸= ˆw′
p and
ˆwk = ˆw′
k for all k ∈ [p − 1]. Since ˆw ≺ ˆw′, either (i), (ii) or (iii) holds. However (i) is
impossible as before, and (iii) is impossible because the parenthesis systems underlying
ˆw and ˆw′ are equal. Hence, (ii) holds. By the remark above, i, j are ˆw-equivalent.
Hence denoting ˆwp+d = α(0)
j , we get that for all c ∈ [d] the letter ˆwp+c has the form

α(0)
ic for some ic which is ˆw-exchangeable with i. Since ˆw is locally maximal, we have
i > i1 > · · · > id = j. This contradicts i < j, hence ˆw = ˆw′ as wanted.
Lastly, we treat the case of the Linial arrangement. Let ˆw, ˆw′ ∈ D(1)(n) be two
Linial equivalent 1-sketches. It is easy to see that (b) holds. Suppose now that ˆw is
Linial locally-maximal and ˆw′ is Linial maximal. We want to show ˆw = ˆw′. Suppose by
contradiction that they are diﬀerent, and let p ∈ [2n] be such that ˆwp ̸= ˆw′
p and ˆwk = ˆw′
k
for all k ∈ [p − 1]. Since ˆw ≺ ˆw′, either (i), (ii) or (iii) holds. However (i) is impossible
as before, so that ˆw′
p = α(0)
j for some j ∈ [n]. Let d > 0 such that ˆwp+d = α(0)
j .

Suppose ﬁrst that ˆwp, ˆwp+1, . . . , ˆwp+d are all α-letters. We denote ˆwp+c = α(0)
ic for all
c ∈ [0..d]. In this case, i0 < id = j (since ˆw ≺ ˆw′), hence taking the least index ic we
have ic < ic+1 and ic < j. Since ˆw is Linial locally-maximal, the letter following α(1)
ic
has the form α(0)
k with k < ic (otherwise it would be α(1)
ic+1 or α(0)
k with k > ic and one

could do an increasing Linial move) Lastly, since k < ic, j and α(0)
k is between α(1)
ic and

α(1)
j in ˆw, property (b) implies that α(0)
k is between α(1)
ic and α(1)
j in ˆw′. Hence α(0)
ic
appears before α(0)
j in ˆw′. We reach a contradiction. It remains to treat the case where

{ ˆwp, ˆwp+1, . . . , ˆwp+d−1} contains a β-letter. Let α(1)
i be the last β-letter before α(0)
j in

ˆw, and let α(0)
i0 be the letter following α(1)
i . By (b), we have i < j. Moreover, since ˆw

is Linial locally-maximal, i0 < i. Since i0 < j and all the letters between α(0)
i0 and α(0)
j

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 43

are α-letters, the same reasoning as before leads to a contradiction. Hence ˆw = ˆw′ as
wanted. □

8.3. General bijection for transitive deformation of the braid arrangement.
In this section we generalize the strategy adopted in Section 8.3 in order to establish bi-
jections between regions of arbitrary transitive deformations of the braid arrangement,
and trees.
We ﬁx a positive integer N and an (N
2 )-tuple of ﬁnite sets of integers S = (Si,j)1≤i<j≤N .
Recall that AS is the arrangement in RN made of the hyperplanes Hi,j,s for all 1 ≤
i < j ≤ N and all s ∈ Si,j. Recall also that when S is transitive, the regions of AS are
equinumerous to the trees TS deﬁned in Deﬁnition 4.5. For T ∈ TS, we denote by ΨS(T )
the set of points (x1, . . . , xN ) satisfying the following inequalities for all 1 ≤ i < j ≤ N
and s ∈ Si,j:
• for s ≥ 0, xi − xj < s if the node i is less than the (s + 1)st child of the node j
in the ≺T order, and xi − xj > s otherwise,
• for s < 0, xi − xj > s if the node j is less than the (−s + 1)st child of the node
i in the ≺T order, and xi − xj < s otherwise.
Our goal is to establish the following result.

Theorem 8.8. If S = (Si,j)1≤i<j≤N is transitive (see Deﬁnition 4.3), then ΨS is a
bijection between the set TS of trees and the regions of AS.

Remark 8.9. The bijections ΨS are compatible with reﬁnements of arrangements. In-
deed AS
′ is a reﬁnement of AS if and only if S′ = (S′
i,j)1≤i<j≤N , with Si,j ⊆ S′
i,j for all
i, j. In this case, TS ⊆ TS
′, and for all T ∈ TS, ΨS
′(T ) ⊆ ΨS(T ).

Our strategy to prove Theorem 8.8 is the same as in Section 8.2. Let m = max(|s|, s ∈
∪Sa,b), so that TS is a subarrangement of A[−m..m](N ). We will think of regions of AS as
equivalence class of regions of A[−m..m](N ), and the bijection Φm deﬁned in Section 8.1
will induce a bijection ΦS between regions of AS and TS.

Deﬁnition 8.10. Let ˆw, ˆw′ be annotated m-sketches of size N . Let i, j ∈ [N ] with
i < j, and let s ∈ [−m..m]. We say that ˆw and ˆw′ are related by a (i, j, s)-move if
for all k ∈ [0..m] ∩ [−s..m − s] the pair of letters {α(k)
i , α(s+k)
j } are consecutive in ˆw,
and ˆw′ is obtained from ˆw by swapping each of these pairs of letters. A S-move is any
(i, j, s)-move with 1 ≤ i < j ≤ N , and s /∈ Si,j. We say that ˆw and ˆw′ are S-equivalent
if one can be obtained from the other by performing a series of S-moves.

Example 8.11. Let m = 1. The Shi moves deﬁned in Section 8.2 are all the (i, j, −1)-
moves, and the semiorder moves are all the (i, j, 0)-moves. Hence the Shi (resp.
semiorder, Linial) moves are the S-moves for the tuple S = (Si,j)1≤i<j≤N with Si,j =
{0, 1} (resp. Si,j = {−1, 1}, Si,j = {1}) for all 1 ≤ i < j ≤ N .

We consider the following order ≺ on the alphabet A(m)(N ): α(s)
i ≺ α(t)
j if either
s > t, or s = t and i < j. We now consider the lexicographic order ≺ on D(m)(n)
corresponding the order ≺ on the letters. An annotated m-sketch ˆw ∈ D(m)(n) is S-
locally-maximal if it is greater than any m-sketch obtained from ˆw by a single S-move.

44 OLIVIER BERNARDI

It is S-maximal if it is greater than any S-equivalent m-sketch. Lastly, a region ρ of
A[−m..m](N ) is said S-maximal if the annotated m-sketch σm(ρ) is S-maximal. We now
establish two easy lemmas.

Lemma 8.12. Each region of AS contains a unique S-maximal region of A[−m..m](N ).

Proof. Let ˆw, ˆw′ ∈ D(m)(N ), and let ρ = σ−1
m ( ˆw) and ρ′ = σ−1
m ( ˆw′) be the associated
regions of A[−m..m](n). It is clear that ˆw are ˆw′ are related by a (i, j, s)-move (for
1 ≤ i < j ≤ N , and s ∈ [−m..m]) if and only if the regions ρ and ρ′ are separated only
by the hyperplane Hi,j,s. Thus ˆw and ˆw′ are S-equivalent if and only if ρ and ρ′ are in
the same regions of AS. Thus, for in any region R of AS, exactly one of the regions ρ
of A[−m..m](N ) contained in R is S-maximal. □

Lemma 8.13. Let ˆw ∈ D(m)(n). The sketch ˆw is S-locally-maximal if and only if the
tree φm( ˆw) is in TS. In other words, φm induces a bijection between S-locally-maximal
regions of A[−m..m](N ) and TS.

Proof. Let ˆw ∈ D(m)(n) and let T = φm( ˆw). For 0 ≤ i < j ≤ n, and s ∈ [m], a
(i, j, s)-moves on ˆw is possible and gives an annotated m-sketch ˆw′ ≻ ˆw if and only if
in ˆw the letter α(s)
j is immediately followed by α(0)
i , and for all t ∈ [s + 1..m], the letters

α(t)
j and α(t−s)
i are consecutive. By deﬁnition of annotations, this holds if and only if

the letter α(s)
j is immediately followed by α(0)
i , and for all t ∈ [s + 1..m], the letters α(t)
j
is immediately followed by a β-letter. By Proposition 8.1, this holds if and only if in
the tree T the node i is the (s + 1)st child of the node j, and the right siblings of i are
leaves (so that i = cadet(j) and lsib(i) = s).
Similarly, for 0 ≤ i < j ≤ n, and s ∈ [−m..0], a (i, j, s)-moves on ˆw is possible and
gives an annotated m-sketch ˆw′ ≻ ˆw if and only if in ˆw the letter α(−s)
i is immediately
followed by α(0)
j and for all t ∈ [−s + 1..m], the letters α(t)
i is immediately followed by
a β-letter. By Proposition 8.1, this holds if and only if in the tree T the node j is the
(s + 1)st child of the node i, and the right siblings of j are leaves (so that j = cadet(i)
and lsib(j) = −s).
Thus ˆw is S-locally-maximal if and only if the tree T satisﬁes the following property
for all 0 ≤ i < j ≤ n: if i = cadet(j) then lsib(i) ∈ Si,j ∪ {0}, and if j = cadet(i) then
− lsib(j) ∈ Si,j. This holds if and only if T is in TS. □

We now complete the proof of Theorem 8.8. From Lemma 8.2, it is clear that for
any tree T ∈ T (m)(N ), ΨS(T ) is the region of AS containing the region Ψm(T ) of
A[−m..m](N ). Hence, by Lemma 8.13, the mapping ΨS is a surjection between the
trees in TS and the regions of AS containing at least one S-locally-maximal region
of A[−m..m](N ). And since any S-maximal region is S-locally-maximal, Lemma 8.13
ensures that ΨS is a surjection between the trees in TS and the regions of AS (all this
holds even if S is not transitive). Now assuming that S is transitive, Theorem 4.6,
ensures that the regions of AS are equinumerous to the trees in TS, so ΨS is actually
a bijection.
 DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 45

9. Concluding remarks

We conclude with some additional links to the literature and some open questions.

9.1. Bijections for the Shi arrangement.
We now explain how our bijection Ψ{0,1} for the Shi arrangement A{0,1}(n) relates
to the existing bijections described in [11] and [40] between regions of A{0,1}(n) and
parking functions of size n. The correspondence is represented in Figure 14. Recall
that a parking function of size n is a n-tuple (p1, . . . , pn) of integers in [0..n − 1] such
that for all k ∈ [n], k ≤ |{i ∈ [n] | pi < k}|.

x1
 x3
x2
 x1
 x3x2
 0 1 1 0 1 0

1 0 2

0 1 2 0 2 1

0 0 1

0 0 2 0 2 0
0 0 0

1 0 1

1 0 0 2 0 1
 1 1 0

2 1 01 2 0

2 0 0
 x1
 x3x2
 1 1 0 1 0 0

0 1 0

0 0 0 0 0 1

1 0 1

2 0 0 2 0 1
2 1 0

1 2 0

0 2 0 0 0 2
 1 0 2

0 1 20 1 1

0 2 1

(b) Athanasiadis-Linusson labeling (c) Pak-Stanley labeling(a) Bijection 	 f 0 ; 1g

3
 3

3
 2

21
 2
 3
 3

1
 2

3

3

2
 1
 3
 2
 3

2 1 3 1

2

3
 1

3
2
 3
 1

2
 2

2
 1
 1

2

3

3
 1
 2
 3

1 1

3
 2

3
 2
 1

1
 3
1

1

1
 1 1
 1

1
1
 1
 11

1
 1

1
 1
 1
 1

2

2
 2 2
 2
 2

2

2

2

2

2

2
 2
 3

3

3

3
 3
 3
 3
 3
3 3

3

3

3 3

3
 2

2
 Figure 14. The bijection Ψ{0,1}, the Athanasiadis-Linusson labeling
and the Pak-Stanley labeling.

The ﬁrst bijection discovered for the Shi arrangement is the so-called Pak-Stanley
labeling of the regions described in [40] (and earlier in [43, Section 5] where Igor Pak is
credited for suggesting the labeling in the case m = 1, without proof). This bijection
associates to a region ρ of A{0,1}(n) the parking function (p1, . . . , pn), where for all
i ∈ [n], pi = |{k ∈ [i − 1] | xk < xi}| + |{k ∈ [i + 1..n] | xk + 1 < xi}| ,
where (x1, . . . , xn) is any point in the region ρ. This is represented in Figure 14(b). It
follows directly from the deﬁnition of Ψ{0,1} that for any tree T ∈ T{0,1}(n), the Pak-
Stanley labeling of the region ρ = Ψ{0,1}(T ) is the parking function λ1(T ) = (p1, . . . , pn)
given by

pi = |{k ∈ [i−1] | node k ≺T node i}| + |{k ∈ [i+1..n] | right child of node k ≼T node i}|.

Another bijection for the Shi arrangement was established by Athanasiadis and Li-
nusson in [11]. This bijection has two steps. The ﬁrst step associates to each region
ρ of A{0,1}(n) a diagram δ(ρ). The second step associates to the diagram δ(ρ) a par-
tition function that we call Athanasiadis-Linusson labeling of ρ. A reader familiar
with [11] will have no diﬃculty seeing that the diagram δ(ρ) is closely related to the
Shi-maximal 1-sketch that we associated to ρ in Section 8.2. This induces a corre-
spondence between our bijection and the Athanasiadis-Linusson labeling that we now

46 OLIVIER BERNARDI

state (the easy proof is omitted). For T ∈ T{0,1}(n), the Athanasiadis-Linusson labeling
of the region ρ = Ψ{0,1}(T ) is the parking function λ2(T ) = (p1, . . . , pn) obtained as
follows. For all i ∈ [n], we consider the path of vertices v1, v2, . . . , vℓ, where v1 is the
node i, vℓ is a leaf, and vk+1 is the right child of vk for all k ∈ [ℓ − 1]. Then, pi is the
number of leaves greater than vℓ for the ≺T order. This is represented in Figure 14(c).
It is not very hard to see that the correspondence λ2 is a bijection, and this is why
the bijection in [11] can be considered a close relative of Ψ{0,1}. However, it is less clear
why the correspondence λ1 is a bijection.

9.2. Regions of the Linial arrangements and binary search trees.
We now discuss the Linial arrangement A{1}(n). Stanley had conjectured that the
regions of A{1}(n) were equinumerous to binary search trees with n nodes, that is, trees
in T (1)(n) satisfying the Condition (iii) of Figure 4. This fact was proved independently
in [37] and [6]. In [37, 35] Postnikov and Stanley listed several combinatorial classes
equinumerous to the regions of A{1}(n), and some bijections between them. But, up
to now, no bijection was known between these classes and the regions of A{1}(n).
We remedy to this situation by giving bijections between regions of A{1}(n), the set
T{1}(n) (which was not in the list), and the set B(n) of binary search trees with n nodes
(which was in the list). The bijection between the regions of A{1}(n) and T{1}(n) was
established in Section 8.2 (see also Figure 2). We now describe a recursive bijection θ,
represented in Figure 15, between T{1}(n) and B(n).
T 2
T 1
 T 4

T 6
 T 7
  ( T i2)

 ( T i1)
  ( T i3)

T 3

T 5  ( T i4)
  ( T j1)



v 1 v i 1
 v i 2
 v i 3
 v i 4
 v 8

v j 1

v j 2

v j 3

v 2 v 3
v 4 v 5
v 6 v 7 v 8
  ( T j3)
  ( T j2)

u v
⇒ u > v u ⇒ u < v
vand
u v
⇒ u > v u ⇒ u > v
vand

T ∈ T{1}( n )  ( T ) ∈ B( n )

Figure 15. The recursive bijection θ from T{1}(n) to B(n). In this
example, exactly two of the trees θ(Tj1), θ(Tj2), θ(Tj3) have no node,
while the third tree is θ(Tp) for the only integer p ∈ {1, 2, 4, 6, 7} such
that Tp has at least one node, and the root of θ(Tp) is less than vp.

For the tree τ0 ∈ T{1}(0) made of one leaf, we deﬁne θ(τ0) = τ0 ∈ B(0). We now
consider n > 0 and suppose that θ is a well deﬁned bijection from T{1}(k) to B(k) for all
k < n. By extension, we may assume that θ is deﬁned on all order-preserving relabeling

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 47

of trees in T{1}(k) for all k < n (with θ preserving the set of labels). Let T be a tree in
T{1}(n), and let v1 be its root. Let v2, v3, . . . , vk+1 be deﬁned by vi+1 = cadet(vi) for
all i ∈ [k], and the fact that both children of vk+1 are leaves. For i ∈ [k], let Ti be the
subtree of T rooted at the child of vi which is not vi+1; see Figure 15. We denote by I
the subset of [k] such that either Ti is a reduced to a leaf which is the left child of vi,
or the root of θ(Ti) is a node which is greater than vi. Let i1 < · · · < ia = k + 1 be the
elements of I ∪ {k + 1} and let k + 1 = j1 > · · · > jb be the elements of [k + 1] \ I. We
then deﬁne θ(T ) as follows:
• vi1 is the root,
• for all p ∈ [a − 1], the node vip has right child vip+1 and left child the root of
the subtree θ(Tip),
• for all p ∈ [b], the node vjp has left child vjp+1 (or a leaf for p = b), and left
child the root of the subtree θ(Tjp).
It is easy to see that θ(T ) is in B(n) (since v1 > v2 > · · · > vk). It is also easy to see, by
induction on n, that θ is a bijection (one of the useful observations to invert θ is that
θ transforms subtrees Tj which are right leaves into subtrees which are right leaves).
The bijection θ is applied to a tree in T{1}(10) in Figure 16.

9

8
1 7 5
3 2
10 46
 7 3
 2

4

6 5
9 1
8

10
θ

Figure 16. The bijection θ from T{1}(n) to B(n).

9.3. Open questions.
The braid arrangement is associated to the root system An−1, in the sense that the
hyperplane have the form < α, x >= 0 for the positive roots α of An−1. The (de-
formations of) arrangements corresponding to other root systems are known to share
some of the properties of (deformations of) the braid arrangement (see e.g. [8, 37, 39]).
Thus, a natural question is whether the results of the present paper can be extended to
this more general setting. Another direction for future research is to use the bijections
presented here in order to obtain more reﬁned counting formulas for the regions of
deformed braid arrangements, by taking into account additional parameters of these
regions (in the spirit of e.g. [40, 3]). We now state two open questions.
It was shown in Section 8.3, that when the tuple S is not transitive, the mapping
ΨS still gives a surjection between the trees in TS and the regions of AS. Indeed, ΨS
gives a bijection between the subset of trees corresponding to S-maximal regions and
the regions of AS.

48 OLIVIER BERNARDI

Question 9.1. For a non-transitive tuple S, is it possible to characterize a subset ̃TS of
TS in bijection with the regions of AS via ΨS?

Let us consider for example the non-transitive set S = {−2, 0, 2}. The set T{−2,0,2}(n)
contains all the trees in T (2)(n) such that if the rightmost child of any node v is a leaf,
then the middle child is also a leaf. However, because A{−2,0,2}(n) is just a dilation of
the Catalan arrangement A{1,0,1}(n), we know that the regions of A{−2,0,2}(n) are in
bijection with the set T (1)(n), or equivalently, the set ̃T{−2,0,2}(n) of trees in T{−2,0,2}(n)
such that the middle child of any node is a leaf. In general, one could hope to ﬁnd the
desired subset ̃TS of TS either starting from the counting formulas in terms of boxed-
trees (Theorem 4.2) and applying some sign-reversing involutions, or by using more
direct bijective considerations.
A related problem is to ﬁnd a more illuminating proof of our bijective results (The-
orem 8.8). In the case of the Shi, semiorder, and Linial arrangement we gave a direct
proof involving Lemma 8.5 showing that locally-maximal regions are maximal. The ar-
gument given there can actually be extended to the m-Shi, m-semiorder and m-Linial
arrangements discussed in Section 2.3. However it is unclear whether such an approach
would work in the general case (hence removing the need of using Theorem 4.6).

Question 9.2. Is there a direct, preferably geometric, proof that S-locally-maximal
regions are S-maximal whenever S is transitive?

Acknowledgements: We thank the referees for several helpful suggestions. We thank
Priyavrat Deshpande and Krishna Menon for pointing out a mistake in Section 8.1.

References

[1] F. Ardila. Computing the Tutte polynomial of a hyperplane arrangement. Paciﬁc J. Math.,
230(1):1–26, 2007.
[2] F. Ardila. Semimatroids and their Tutte polynomials. Revista Colombiana de Matem´aticas,
41(1):39–66, 2007.
[3] D. Armstrong and B. Rhoades. The Shi arrangement and the Ish arrangement. Trans. Amer.
Math. Soc., 364(3):1509–1528, 2012.
[4] A. Assi and P.A. Garc´ıa-S´anchez. Numerical Semigroups and Applications. Springer, 2016.
[5] C.A. Athanasiadis. Algebraic combinatorics of graph spectra, subspace arrangements and Tutte
polynomials. PhD thesis, MIT, 1996.
[6] C.A. Athanasiadis. Characteristic polynomials of subspace arrangements and ﬁnite ﬁelds. Adv.
Math., 122(2):193–233, 1996.
[7] C.A. Athanasiadis. On free deformations of the braid arrangement. European J. Combin., 19:7–18,
1998.
[8] C.A. Athanasiadis. Extended Linial hyperplane arrangements for root systems and a conjecture
of Postnikov and Stanley. J. Algebraic Combin., 10:207–225, 1999.
[9] C.A. Athanasiadis. Deformations of Coxeter hyperplane arrangements and their characteristic
polynomials. In Arrangements – Tokyo 1998, Adv. Stud. Pure Math. 27, pages 1–26, 2000.
[10] C.A. Athanasiadis. Generalized Catalan numbers, Weyl groups and arrangements of hyperplanes.
Bull. London Math. Soc., 36(3):294–302, 2004.
[11] C.A. Athanasiadis and S. Linusson. A simple bijection for the regions of the Shi arrangement of
hyperplanes. Discrete Math., 204(1):27–39, 1999.
[12] O. Bernardi. Solution to a combinatorial puzzle arising from Mayer’s theory of cluster integrals.
S´em. Lothar. Combin., 59, 2008.

DEFORMATIONS OF THE BRAID ARRANGEMENT AND TREES 49

[13] L. Carlitz and R. Scoville. Generalized Eulerian numbers: combinatorial applications. J. Reine
Angew. Math., 265:110–137, 1974.
[14] J. L. Chandon, J. Lemaire, and J. Pouget. D´enombrement des quasi-ordres sur un ensemble ﬁni.
Math. Inform. Sci. Humaines, 62, 62:61–80, 1978.
[15] S. Corteel, D. Forge, and V. Ventos. Bijections between aﬃne hyperplane arrangements and valued
graphs. European J. Combin., 50:30–37, 2015.
[16] H.H. Crapo. The Tutte polynomial. Aequationes Math., 3:211–229, 1969.
[17] B. Drake. An inversion theorem for labeled trees and some limits of areas under lattice paths. PhD
thesis, Brandeis University, 2008.
[18] P. Flajolet and R. Sedgewick. Analytic combinatorics. Cambridge University Press, 2009.
[19] D. Forge. Linial arrangements and local binary search trees. ArXiv preprint: 1411.7834, 2014.
[20] I.M. Gessel. Problems in enumerative combinatorics. Personal communication.
[21] I.M. Gessel. A combinatorial proof of the multivariable Lagrange inversion formula. J. Combin.
Theory Ser. A, 45(2), 1987.
[22] I.M. Gessel. Counting labeled binary trees by ascents and descents. Preprint, 2016.
[23] I.M. Gessel, S. Griﬃn, and V. Tewari. Labeled plane binary trees and Schur-positivity. ArXiv
preprint:1706.03055, 2017.
[24] I.J. Good. Generalizations to several variables of Lagrange’s expansion, with applications to sto-
chastic processes. Proc. Cambridge Philos. Soc., 56:367–380, 1960.
[25] P. Headley. On a family of hyperplane arrangements related to the aﬃne Weyl groups. J. Algebraic
Combin., 6(4):331–338, 1997.
[26] S. Hopkins and D. Perkinson. Orientations, semiorders, arrangements, and parking functions.
Electron. J. Combin., 19(4), 2012. Paper #P8.
[27] S. Hopkins and D. Perkinson. Bigraphical arrangements. Trans. Amer. Math. Soc., 368:709–725,
2016.
[28] L.H. Kalikow. Symmetries in trees and parking functions. Discrete Math., 256(3):719–741, 2002.
[29] C. Krattenthaler. The theory of heaps and the Cartier-Foata monoid. Appendix to the electronic
republication of Probl`emes combinatoires de commutation et r´earrangements, by P. Cartier and
D. Foata., 2006.
[30] P. Leroux. Enumerative problems inspired by Mayer’s theory of cluster integrals. Electron. J.
Combin., 11, 2006.
[31] E. Leven, B. Rhoades, and A.T. Wilson. Bijections for the Shi and Ish arrangements. European
Journal of Combinatorics, 39:1–23, 2014.
[32] J.E. Mayer and M.G. Mayer. Statistical Mechanics. Wiley, 1940.
[33] P. Orlik and L. Solomon. Combinatorics and topology of complements of hyperplanes. Invent.
Math., 56(2):167–189, 1980.
[34] P. Orlik and H. Terao. Arrangements of Hyperplanes. Springer-Verlag, 1992.
[35] A. Postnikov. Enumeration in algebra and geometry. PhD thesis, MIT, 1997.
[36] A. Postnikov. Intransitive trees. J. Combin. Theory, Ser. A, 77:360–366, 1997.
[37] A. Postnikov and R. Stanley. Deformations of Coxeter hyperplane arrangements. J. Combin. The-
ory Ser. A, 2000:544–597, 2000.
[38] J.Y. Shi. The Kazhdan-Lusztig Cells in Certain Aﬃne Weyl Groups, volume 1179 of Lecture Notes
in Mathematics. Springer-Verlag, 1986.
[39] J.Y. Shi. Sign types corresponding to an aﬃne Weyl group. J. London Math. Soc., 35(2):56–74,
1987.
[40] R. P. Stanley. Hyperplane arrangements, parking functions and tree inversions. In Progress in
Mathematics, volume 161, 1998.
[41] R. P. Stanley. An introduction to hyperplane arrangements. In Lecture notes, IAS/Park City
Mathematics Institute, 2004.
[42] R.P. Stanley. Acyclic orientations of graphs. Discrete Math., 5:171–178, 1973.
[43] R.P. Stanley. Hyperplane arrangements, interval orders and trees. Proc. Nat. Acad. Sci.,
93(6):2620–2625, 1996.
[44] R.P. Stanley. Enumerative combinatorics, volume 2. Cambridge University Press, 1999.

50 OLIVIER BERNARDI

[45] X. G. Viennot. Heaps of pieces. I. Basic deﬁnitions and combinatorial lemmas. Lecture Notes in
Math., 1234. Springer, 1986.
[46] T. Zaslavsky. Facing up to arrangements: Face-count formulas for partitions of space by hyper-
planes. Mem. Amer. Math. Soc., 154(1), 1975.

Olivier Bernardi, Brandeis University, 415 South Street, Waltham, MA 02453, USA.
