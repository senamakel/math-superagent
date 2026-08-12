<!-- source: https://inria.hal.science/hal-05002249/document | converted from PDF -->

HAL Id: hal-05002249

https://inria.hal.science/hal-05002249v3

Submitted on 4 Nov 2025

HAL is a multi-disciplinary open access archive
for the deposit and dissemination of scientific re-
search documents, whether they are published or not.
The documents may come from teaching and research
institutions in France or abroad, or from public or pri-
vate research centers.
 L’archive ouverte pluridisciplinaire HAL, est des-
tinée au dépôt et à la diffusion de documents scien-
tifiques de niveau recherche, publiés ou non, émanant
des établissements d’enseignement et de recherche
français ou étrangers, des laboratoires publics ou
privés.

Distributed under a Creative Commons CC BY-ND 4.0 - Attribution - No Derivative Works - International
License

Primal and dual approaches for the chamber enumeration of
real hyperplane arrangements

Jean-Pierre Dussault, Jean Charles Gilbert, Baptiste Plaquevent-Jourdain

To cite this version:

Jean-Pierre Dussault, Jean Charles Gilbert, Baptiste Plaquevent-Jourdain. Primal and dual approaches for
the chamber enumeration of real hyperplane arrangements. Inria - Paris; Université de Sherbrooke (Québec,
Canada). 2025, pp.40. ⟨hal-05002249v3⟩

PRIMAL AND DUAL APPROACHES FOR THE CHAMBER ENUMERATION OF
REAL HYPERPLANE ARRANGEMENTS

J.-P. DUSSAULT∗, J.CH. GILBERT† , AND B. PLAQUEVENT-JOURDAIN‡

Abstract. The hyperplane arrangement problem appears in various theoretical and applied mathematical contexts.
This paper focuses on the enumeration of the chambers of an arrangement, a task that most often requires algebraic
or numerical computation. Among the recent numerical methods, Rada and ˇCern´y’s recursive algorithm outperforms
previous approches, by relying on a speciﬁc tree structure and on linear optimization. This paper presents modiﬁcations
and improvements to this algorithm. It also introduces a dual approach solely grounded on matroid circuits and its
associated concepts of stem vectors, thus reducing or avoiding the need to solve linear optimization problems. Along
the way, some theoretical properties of arrangements, including some of their various stem vector sets, are recalled or
proved with an analytic viewpoint. It is shown, in particular, that the set of the chambers of an aﬃne arrangement is
located between those of two related linear arrangements. This leads to compact forms of the algorithms, which solve less
subproblems. The proposed methods have been implemented in Julia and their eﬃciency is assessed on various instances
of arrangements; for the best of them, this eﬃciency manifests itself by speedup ratios in the range [1.72, 22.87] with an
average value of 9.10. The developed code also lists the bounded chambers when the arrangement is in linear general
position.

Key words. Duality, hyperplane arrangement, matroid circuit, Motzkin’s alternative, Schl¨aﬂi’s bound, stem vector,
system of strict linear inequalities, tree algorithm, Winder’s formula.

MSC codes. 05B35, 05C05, 14N20, 49N15, 52B40, 52C35, 52C40, 90C05.

1. Introduction. A hyperplane of Rn is a set of the form H := {x ∈ Rn : vTx = τ }, where v ∈ Rn,
τ ∈ R and vTx = ∑n
i=1 vixi denotes the Euclidean scalar product of v and x. For v1, . . . , vp ∈ Rn and
τ1, . . . , τp ∈ R, consider the collection of hyperplanes Hi := {x ∈ Rn : vT
i x = τi} for i ∈ [1 : p] (this is
our notation for the set of the ﬁrst p positive integers). The connected parts of the complement of their
union, that is Rn \ (∪
p
i=1Hi), are open polyhedrons, called chambers or cells. Hyperplane arrangements
is the name given to the discipline that describes the layout of these hyperplanes [53, 24]. Its study
started at least in the 19th century [51, 48, 54] and has continued until the present with theoretical
contributions [59, 1, 56, 39], algorithmic developments [21, 33, 45, 18] as well as applications in statistics
and geometry [31, 7], to mention a few; see also the references therein. Hyperplane arrangements
can also be stated with complex numbers [38] and they are useful in the analysis of hypergeometric
functions [2], as well as in cosmology and particle physics [42, 23]. A powerful tool to study arrangements
is the characteristic polynomial, which contains much information and provides one way of computing
the number of (bounded) chambers (see for instance [10, 59, 3, 53]).
This paper focuses on the numerical enumeration of the chambers of an arrangement. Several
approaches have been designed for that purpose. The algorithm of Bieri and Nef [5] recursively sweeps
the space with hyperplanes, decreasing the dimension of the current space in order to explore ar-
rangements in aﬃne spaces of smaller dimension. Edelsbrunner, O’Rourke and Seidel [22] proceed
incrementally, by adding one hyperplane at a time; their approach is geometric, using tools described
by Gr¨unbaum [29, 30]; they thus design algorithms with some optimal complexity properties. The ap-
proach of Avis, Fukuda and Sleumer [4, 52] starts with an arbitrary chamber and moves from chamber
to neighboring chamber, using a “reverse search paradigm”, thanks to the connectivity of the graph
structure of the chambers. Rada and ˇCern´y [45] use an eﬃcient tree, called the S-tree below, obtained

∗D´epartement d’Informatique, Fac. des Sciences, Univ. de Sherbrooke, Qu´ebec, Canada
Jean-Pierre.Dussault@Usherbrooke.ca, ORCID 0000-0001-7253-7462
†Inria Paris, 2 rue Simone Iﬀ, CS 42112, 75589 Paris Cedex 12, France
D´epartement de Math´ematiques, Fac. des Sciences, Univ. de Sherbrooke, Qu´ebec, Canada
Jean-Charles.Gilbert@inria.fr, ORCID 0000-0002-0375-4663
‡D´epartement de Math´ematiques, Fac. des Sciences, Univ. de Sherbrooke, Qu´ebec, Canada
Inria Paris, 2 rue Simone Iﬀ, CS 42112, 75589 Paris Cedex 12, France
Baptiste.Plaquevent-Jourdain@USherbrooke.ca, ORCID 0000-0001-7055-4568

2 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

by adding hyperplanes incrementally, like in [22]. This tree algorithm possesses various interesting
properties such as output-polynomiality, meaning that each individual chamber is obtained in polyno-
mial time, and compactness, meaning that the required memory storage is low. See also [12] and its
references.
Several pieces of software have been developed to deal with arrangements: polymake [35], Sage-
math [55], Macaulay2 [28], OSCAR [40] and isf.m [16, 15], the last one being limited to linear arrange-
ments, those whose hyperplanes contain the origin. Some related works, such as the package Counting-
Chambers.jl [8], focus on the use of combinatorial symmetries, alongside the deletion-restriction para-
digm (see also [58]), to deal with arrangements with underlying symmetries and many more hyperplanes.
Similar considerations also appear in TOPCOM [46, 47] and yield very good results on particular instances.
Improvements to Rada and ˇCern´y’s algorithm are proposed and benchmarked in [18], for linear
arrangements. The authors ﬁrst present heuristics to bypass some computations. Then, they introduce
a dual approach based on Gordan’s theorem of the alternative [26], by introducing the notion of stem
vector, which turned out to be identical to that of signed circuit of a vector matroid associated with
the arrangement. These modiﬁcations allow the authors to signiﬁcantly reduce the number of linear
optimization problems (LOPs) to solve, therefore lowering the computing time, or even to completely
remove the need of linear optimization. This paper extends the scope of [18] to arrangements with
hyperplanes not necessarily containing the origin. We shall see that the heuristics introduced in [18]
have natural extensions in this general case. The same is true for the dual approach, which is here
grounded on Motzkin’s alternative [37]; this one is indeed naturally associated with aﬃne arrangements.
These modiﬁcations are numerically compared in the penultimate section of the paper.
This contribution is organized as follows. Section 2 presents some notation used throughout the pa-
per as well as Motzkin’s theorem of the alternative [37], crucial in this paper, which contributes to both
theoretical and algorithmic aspects. Section 3 starts with the introduction of the concept of hyperplane
arrangement (section 3.1). Then, it gives conditions ensuring symmetry properties (section 3.2). Next,
section 3.3 introduces the notion of stem vector, gives its properties and shows how the stem vectors
can be used to detect the infeasibility of sign vectors (covering test of proposition 3.9). In section 3.4,
the role and interest of the augmented matrix are discussed. It is shown, in particular, that the sign
vector set of an aﬃne arrangement is located between the sign vector sets of two linear arrangements.
The formulas giving upper bounds on the number of chambers are also recalled, those that are reached
when the arrangements are in general position, since this information intervenes in the understanding
of some test problems. Finally, in section 3.5, the identiﬁcation of the bounded chambers with the
set of asymmetric sign vectors is shown to hold when the arrangement is in linear general position, so
that the algorithms presented in this paper also list the bounded chambers, which is of interest in the
domains covered in [2, 42, 23].
The rest of the paper focuses on algorithmic issues. Section 4 ﬁrst describes the algorithm of [45],
its recursion process and its use of linear optimization. Then, we adapt the heuristic ideas proposed
in [18] to aﬃne arrangements, which improves the eﬃciency of the previous algorithm. Section 5 focuses
on dual algorithms, which use the stem vectors and often require less computing time. Section 6 shows
how a compact form of the algorithms can be constructed, taking advantage of the fact that only
half of the symmetric sign vectors need to be computed. Often, this technique also allows the compact
algorithms to save computing time. Finally, section 7 presents the instances used to test the algorithms,
their features and some numerical results.
Our presentation is more based on linear algebra and (convex) analysis rather than on discrete
geometry or algebra. More speciﬁcally, the notion of circuit of a vector matroid and the duality
concepts of convex analysis are prominent in sections 3, 5 and 6. In the companion report [19], new
proofs to known results are proposed with these points of view. This allows the readers with an analytic
leaning to have easier access to these results.
This paper is an abridged version of the more detailed report [19].

PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 3

2. Background. This section begins with a paragraph on the notation and recalls Motzkin the-
orem of the alternative.
One denotes by Z, N and R the sets of integers, nonnegative integers and real numbers and one
sets N∗ := N \ {0} and R∗ := R \ {0} (r ∈ R is said to be positive if r > 0 and nonnegative if r ⩾ 0).
For two integers n1 ⩽ n2, [n1 : n2] := {n1, . . . , n2} is the set of the integers between n1 and n2. We
denote by Rn
+ := {x ∈ Rn : x ⩾ 0} and Rn
++ := {x ∈ Rn : x > 0} the nonnegative and positive
orthants, where the inequalities apply componentwise. For a set S, one denotes by |S| its cardinality,
by Sc its complement in a set that will be clear from the context and by SJ , for an index set J ⊆ N∗,
the set of vectors, whose elements are in S and are indexed by the indices in J. The vector e denotes
the vector of all ones, whose size depends on the context. The Hadamard product of u and v ∈ Rn

is the vector u · v ∈ Rn, whose ith component is uivi. The sign function sgn : R → R is deﬁned
by sgn(t) = +1 if t > 0, sgn(t) = −1 if t < 0 and sgn(0) = 0. The sign of a vector x is deﬁned
componentwise: sgn(x)i = sgn(xi) for all i. For u ∈ Rn, |u| ∈ Rn is the vector deﬁned by |u|i = |ui|
for all i ∈ [1 : n]. The dimension of a vector space E is denoted by dim(E). The range space of a
matrix A ∈ Rm×n is denoted by R(A), its null space by N (A), its rank by rank(A) := dim R(A)
and its nullity by null(A) := dim N (A) = n − rank(A), thanks to the rank-nullity theorem. The
ith row (resp. column) of A is denoted by Ai,: (resp. A:,i). Transposition operates after a row and/or
column selection: AT
i,: is a short notation for (Ai,:)
T for instance. The vertical concatenation of matrices
A ∈ Rn1×m and B ∈ Rn2×m is denoted by [A; B] ∈ R(n1+n2)×m. For u ∈ Rn, Diag(u) ∈ Rn×n is the
square diagonal matrix with Diag(u)i,i = ui. The orthogonal of a subspace Z ⊆ Rn is denoted by
Z ⊥ := {x ∈ Rn : xTz = 0, for all z ∈ Z}.
This article makes extensive use of the so-called (there have been many contributors) Motzkin
theorem of the alternative [37] [32, theorem 3.17], abbreviated as Motzkin’s alternative below, whose
following simpliﬁed expression is appropriate for our purpose (the general version also includes aﬃne
equalities and non strict aﬃne inequalities). Let us write it as an equivalence, rather than an alternative:
for a matrix A ∈ Rm×n and a vector a ∈ Rm,

(2.1) ∃ x ∈ Rn : Ax > a ⇐⇒ ∄ α ∈ Rm
+ \ {0} : ATα = 0, a
Tα ⩾ 0.

Gordan’s theorem of the alternative [26, 1873] is recovered when a = 0:

(2.2) ∃ x ∈ Rn : Ax > 0 ⇐⇒ ∄ α ∈ Rm
+ \ {0} : ATα = 0.

The latter equivalence satisﬁes the needs in [18] because the inequality systems encountered in that
paper are homogeneous.

3. Hyperplane arrangements.

3.1. Presentation. Let n ∈ N∗. A hyperplane of Rn is a set of the form H := {x ∈ Rn : vTx = τ },
where v ∈ Rn and τ ∈ R. This hyperplane H is said to be proper if v ̸= 0 and improper otherwise.
A proper hyperplane H partitions Rn into three subsets: H itself and its negative and positive open
halfspaces, respectively deﬁned by

H − := {x ∈ Rn : vTx < τ } and H + := {x ∈ Rn : vTx > τ }.

If H is improper and τ = 0, then H = Rn and H − = H + = ∅. If H is improper and τ ̸= 0, then
H = ∅ and H + = Rn or ∅, while H − = (H +)
c.
A hyperplane arrangement is a collection of p ∈ N∗ hyperplanes Hi := {x ∈ Rn : vT
i x = τi}, for
i ∈ [1 : p], where v1, . . . , vp ∈ Rn and τ1, . . . , τp ∈ R. It is denoted by A(V, τ ), where V := [v1 · · · vp] ∈
Rn×p is the matrix made of the vectors vi’s and τ := [τ1; . . . ; τp] ∈ Rp×1. The arrangement A(V, τ )
is said to be proper if V has no zero column (i.e., its hyperplanes are proper) and improper otherwise
(in proposition 4.4, a construction may yield a harmless improper arrangement, which is the reason
why we introduce this concept). The arrangement is said to be linear if τ = 0 and aﬃne in general

4 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

(therefore, a linear arrangement is just a particular aﬃne arrangement). The arrangement is said to be
centered if all the hyperplanes have a point in common [3], which is the case if and only if τ ∈ R(V T)
(proposition 3.2).
Whilst a proper hyperplane divides Rn into two nonempty open halfspaces, a proper hyperplane
arrangement splits Rn into nonempty polyhedral convex open sets, called chambers, which are the
nonempty sets of the form

(3.1) C(I+, I−) := (∩i∈I+ H +
i ) ∩ (∩i∈I− H −
i ),

where (I+, I−) is in the set B([1 : p]) of the bipartitions (i.e., the partitions into two subsets) of [1 : p].
When C(I+, I−) ̸= ∅ for all the bipartitions (I+, I−) ∈ B([1 : p]), the arrangement A(V, τ ) is said to
be complete.
These chambers are in one-to-one correspondence with the sign vector set

(3.2) S(V, τ ) := {s ∈ {±1}
p : s · (V Tx − τ ) > 0 for some x ∈ Rn},

where “·” denotes the Hadamard product. This correspondence is given by the bijection (see [19] and
the references therein)

(3.3) φ : (I+, I−) ∈ B([1 : p]) ↦→ s ∈ {±1}
p, where si = { +1 if i ∈ I+
−1 if i ∈ I−.

This is illustrated in ﬁgure 3.1 by three elementary examples that will accompany us throughout the
paper. Enumerating the chambers or, equivalently, the sign vector set S(V, τ ), is the problem at hand

−−−
 +−−
 +−+

−++

H1
 H2
0
 H3

+−+

+−−−−−

−+−

−++ +++
 H1
 H2
 H3

0
 +−−
 +−+

−++
 +++

++−

−+−

−−−
 H1
 H2

H3

0
 +++

−+−
 −−+

Fig. 3.1. Arrangements in R2 speciﬁed by the hyperplanes H1 := {x ∈ R2 : x1 = 0}, H2 := {x ∈ R2 : x2 = 0},
H3(left) := {x ∈ R2 : x1 + x2 = 0}, H3(middle) := {x ∈ R2 : x1 + x2 = 1} and H3(right) := {x ∈ R2 :
x1 + x2 = −1}. The origin is contained in all the hyperplanes but in H3(middle) and H3(right), so that the arrangement
in the left-hand side is linear with 6 chambers and the other ones are aﬃne with 7 chambers.

in this paper. A sign vector s ∈ {±1}p in S(V, τ ) is said to be feasible, while it said to be infeasible if
it is in the complementary set S(V, τ )
c := {±1}
p \ S(V, τ ).

For s ∈ S(V, τ ), a point x verifying the system of strict inequalities in (3.2) is called a witness point
of s [45]. It is often more convenient to work with these sign vectors s ∈ {±1}p rather than with the
bipartitions (I+, I−) of [1 : p] and we shall do so in the rest of the paper.

3.2. Symmetry properties. Hyperplane arrangements beneﬁt from a myriad of properties [53,
59, 1, 39]. In this section, we focus on the symmetry properties that play an important role in the
design and understanding of the algorithms. We consider an arrangement A(V, τ ) with V ∈ Rn×p of
rank r and τ ∈ Rp.
Now that the chambers C(I+, I−) have been identiﬁed by the feasible sign vectors, we are led to
the introduction of the notion of symmetry, which naturally presents itself in {±1}
p.

PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 5

Definitions 3.1 (symmetric sign vector set). A set of sign vectors S ⊆ {±1}
p with p ∈ N∗ is
said to be symmetric if −S = S; otherwise, it is said asymmetric. For a given set S ⊆ {±1}
p, one says
that s ∈ {±1}
p is symmetric in S if ±s ∈ S.

When S(V, τ ) is symmetric, only half of it needs to be computed. Using the deﬁnition (3.2) of S(V, τ ),
it follows immediately [19] that

(3.4) S(V, 0) is symmetric.

The next proposition shows that this symmetry property occurs for S(V, τ ) if and only if A(V, τ ) is
centered.

Proposition 3.2 (symmetry characterization). Let A(V, τ ) be a proper arrangement. Then, the
following properties are equivalent:
(i) S(V, τ ) is symmetric,
(ii) τ ∈ R(V T),
(iii) the arrangement is centered.

Proof. [(i) ⇒ (ii)] One can decompose τ as follows:

(3.5a) τ = τ 0 + V T ˆx,

where τ 0 ∈ N (V ) and ˆx ∈ Rn. We pursue by contraposition, assuming that τ 0 ̸= 0. Hence I := {i ∈
[1 : p] : τ 0
i ̸= 0} is nonempty. Deﬁne s ∈ {±1}
p by

(3.5b) sI := sgn(τ 0
I ),

while sI c is deﬁned below in order to get

s /∈ S(V, τ ) and − s ∈ S(V, τ ).

These properties suﬃce to prove the implication “(i) ⇒ (ii)”. Set SI := Diag(sI ).
To prove that s /∈ S(V, τ ), whatever sI c ∈ {±1}
I c is, observe that αI := |τ 0
I | ∈ RI
+ \ {0} veriﬁes

V : ,I SI αI = 0 and (τ 0
I )TSI αI = ∥τ 0
I ∥
2
2 ⩾ 0.

By Motzkin’s alternative (2.1) with A = SI V T
:,I and a = SI τ 0
I , this is equivalent to

∄ x ∈ Rn : SI V T
: ,I x > SI τ 0
I .

Hence, whatever sI c ∈ {±1}
I c is, there is no x ∈ Rn such that s · (V Tx − τ 0) > 0. Now, using (3.5a),
we see that there is no x ∈ Rn such that s · (V Tx − τ ) > 0, which proves s /∈ S(V, τ ).
Let us now show that −s ∈ S(V, τ ), for some sI c to specify. Observe that there is no αI ∈ RI
+ \ {0}
such that −V : ,I SI αI = 0 and − |τ 0
I |
TαI ⩾ 0

because the last inequality, with αI ⩾ 0 and |τ 0
I | > 0, implies that αI = 0. By Motzkin’s alternative
(2.1) with A = −SI V T
: ,I and a = −|τ 0
I | = −SI τ 0
I , this is equivalent to

(3.5c) ∃ x ∈ Rn : −SI V T
: ,I x > −SI τ 0
I .

Since the columns of V are nonzero, a small perturbation of x can maintain (3.5c) and ensures that the
components of V T
: ,I cx are nonzero (see [19] or use, for example, [18, lemma 2.6] with the zero vector and
the distinct vi’s with i ∈ I c). Next, choosing sI c := − sgn(V T
: ,I c x) and setting SI c := Diag(sI c) lead to

(3.5d) − SI cV T
: ,I cx > 0 = −SI cτ 0
I c.

6 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

Thanks to (3.5c) and (3.5d), there is an x ∈ Rn such that −s · (V Tx − τ 0) > 0. Now, using (3.5a), we
see that there is an x ∈ Rn such that −s · (V Tx − τ ) > 0, which proves that −s ∈ S(V, τ ).
[(ii) ⇔ (iii)] Property (ii) is equivalent to the existence of ˆx ∈ Rn such that V T ˆx = τ , which is
itself equivalent to the fact that the hyperplanes have the point ˆx in common, which means that the
arrangement is centered.
[(ii) ⇒ (i)] Let ˆx ∈ Rn be such that V T ˆx = τ . If s ∈ S(V, τ ), then s · (V Tx − τ ) > 0 for some
x ∈ Rn. It follows that −s · (V T(2ˆx − x) − τ ) = −s · (V T(−x) + τ ) > 0, implying that −s ∈ S(V, τ ).

It is short to prove that (see [19])

(3.6) S(V, −τ ) = −S(V, τ ).

Let us deﬁne the symmetric and asymmetric parts of S(V, τ ) by

(3.7) Ss(V, τ ) := S(V, τ ) ∩ S(V, −τ ) and Sa(V, τ ) := S(V, τ ) \ Ss(V, τ ).

Clearly, by (3.6), ±s ∈ S(V, τ ) when s ∈ Ss(V, τ ), while −s /∈ S(V, τ ) when s ∈ Sa(V, τ ). This justifes
the names given to Ss(V, τ ) and Sa(V, τ ). One also observes that (see [19])

(3.8) Ss(V, −τ ) = −Ss(V, τ ) = Ss(V, τ ) and Sa(V, −τ ) = −Sa(V, τ ).

Proposition 3.3 (symmetry in S(V, τ )).
1) S(V, 0) ⊆ S(V, τ ), with equality if and only if S(V, τ ) is symmetric,
2) Ss(V, τ ) = S(V, 0).

Proof. 1a) Let us ﬁrst show that S(V, 0) ⊆ S(V, τ ). Let s ∈ S(V, 0), so that s · (V Tx) > 0 for some
x ∈ Rn. Then, s · (V T(tx) − τ ) > 0 for t large enough, implying that s ∈ S(V, τ ).
2) [⊆] If s ∈ Ss(V, τ ), one has ±s ∈ S(V, τ ) and there are points x and ˜x such that s · (V Tx − τ ) > 0
and −s · (V T ˜x − τ ) > 0. After adding these inequalities side by side, one gets s · (V T(x − ˜x)) > 0, i.e.,
s ∈ S(V, 0). [⊇] By point 1a, with τ and −τ .
1b) If S(V, 0) = S(V, τ ), S(V, τ ) is symmetric since S(V, 0) is by (3.4). Conversely, if S(V, τ ) is
symmetric, then S(V, τ ) = −S(V, τ ) = S(V, −τ ) by (3.6), so that S(V, τ ) = Ss(V, τ ); next S(V, τ ) =
S(V, 0) follows from point 2.

Some of the properties stated above can be symbolically represented like in ﬁgure 3.2; see proposi-
tion 3.10(1) below for the role of the set S([V ; τ T], 0).
 S([V ; τ T], 0)

S(V, 0) Sa(V, τ )

Sa(V, −τ )

S(V, τ )

Fig. 3.2. Symbolic representation of the sets S(V, 0), S(V, τ ), Sa(V, τ ) and S([V ; τ T], 0), respecting (3.6), (3.7), (3.8)
and propositions 3.3 and 3.10. The horizontal dashed line aims at representing the reﬂection between a sign vector s
and its opposite −s: S(V, 0) and S([V ; τ T], 0) are symmetric in the sense of deﬁnition 3.1.

3.3. Stem vectors. As mentioned in the introduction, stem vectors are useful to reduce the num-
ber of linear optimization problems to solve in the algorithms enumerating the chambers of hyperplane
arrangements; see section 5. The notion of stem vector was rediscovered in [18] for a linear arrangement
A(V, 0) (a similar notion is indeed presented in [60, § 6.2] under the name of signed circuit) and it is
extended in this section to an aﬃne arrangement A(V, τ ) (when the arrangement is not centered, the
set of stem vectors is a proper subset of the signed circuit set, see propositions 3.2 and 3.8). It is based

PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 7

on the notion of circuit of the vector matroid formed by the columns of V and its subsets of linearly
independent columns. Stem vectors are useful to determine algebraically the complement

S(V, τ )c := {±1}
p \ S(V, τ )

of the sign vector set S(V, τ ) in {±1}p. Indeed, as we shall see, a stem vector is a particular sign vector
in {±1}
J for some J ⊆ [1 : p] of minimal size ensuring proposition 3.9 below. This one tells us that a
sign vector s is in S(V, τ )c if and only if sJ is a stem vector for some J ⊆ [1 : p]. This property is used
throughout sections 5 and 6. It also results immediately that, knowing the stem vectors, it is possible
to generate completely S(V, τ )c (by the crude dual algorithm 5.1). Here are the details.
Recall that a circuit of the vector matroid deﬁned by the columns of V ∈ Rn×p and its subsets of
linear independent columns [41, proposition 1.1.1] is formed of the indices of a set of columns of V that
are linearly dependent, whose strict subsets are the indices of linearly independent columns of V [41,
proposition 1.3.5(iii)]. In compact mathematical terms, the collection C(V ) of the circuits associated
with the matrix V ∈ Rn×p is deﬁned by

(3.9) C(V ) := {J ⊆ [1 : p] : J ̸= ∅, null(V : ,J ) = 1, null(V : ,J0) = 0 for all J0 ⊊ J},

where “null” denotes the nullity (i.e., the dimension of the null space) and “⊊” denotes strict inclusion.
The stem vectors are deﬁned from the circuits of V , with the desire to validate proposition 3.9 below.
Recall that, with our notation, a sign vector σ ∈ {±1}
J for some J := {j1, . . . , j|J|} ⊆ [1 : p] is a vector
(σj1, . . . , σj|J| ) where the σj’s are in {−1, +1}.
Recall that an index set J ⊆ [1 : p] verifying null(V : ,J ) = 1 is not necessarily a circuit of V .
Nevertheless, such an index set contains a unique circuit, as guaranteed by the following lemma (see [18,
proposition 3.11], for instance).

Lemma 3.4 (matroid circuit detection). Suppose that I ⊆ [1 : p] is such that null(V : ,I ) = 1 and
that α ∈ N (V : ,I ) \ {0}. Then, J := {i ∈ I : αi ̸= 0} is a matroid circuit of V and the unique one
included in I.

Definitions 3.5 (stem vector). A stem vector of the arrangement A(V, τ ) is a sign vector σ ∈
{±1}
J for some J ⊆ [1 : p] satisfying

(3.10) { J ∈ C(V ),
σ = sgn(η) for some η ∈ RJ verifying η ∈ N (V : ,J ) \ {0} and τ T
J η ⩾ 0.

A stem vector is said to be symmetric if τ T
J η = 0 and asymmetric otherwise (these properties do not
depend on the chosen vector η, as shown in remark 3.6(3) below). We denote respectively by

(3.11) S(V, τ ), Ss(V, τ ) and Sa(V, τ ) := S(V, τ ) \ Ss(V, τ )

the sets of stem vectors, symmetric stem vectors and asymmetric stem vectors of the arrangement
A(V, τ ). We denote by J : S(V, τ ) → C(V ) the map that associates with a stem vector σ ∈ {±1}J its
circuit J := J(σ).

These deﬁnitions deserve some explanations and comments.

Remarks 3.6. 1) When the arrangement is linear (i.e., τ = 0), one recovers deﬁnition 3.9 in [18].
2) The circuits are deﬁned from V , while the stem vectors are deﬁned from (V, τ ); the latter depend
on τ , which is not the case of the former. In particular, the condition “τ T
J η ⩾ 0” in (3.10) makes the stem
vectors diﬀerent from the signed circuits of V . The stem vector set S(V, τ ) is not the set S([V ; τ T], 0)
of the signed circuits of [V ; τ T] either (this will be clariﬁed by (3.18)1 and in ﬁgure 3.3).
3) A calculation method from C(V ). One can associate with a circuit J ∈ C(V ), either one asym-
metric stem vector or two symmetric stem vectors (there are no other possibilities). Take indeed a
circuit J ∈ C(V ). Then, by (3.9), null(V : ,J ) = 1 and any η ∈ N (V : ,J ) \ {0} has no zero component
(since null(V : ,J0) = 0 for all J0 ⊊ J). Therefore, sgn(η) ∈ {±1}J for any η ∈ N (V : ,J ) \ {0}. Now, there
may be two complementary cases.

8 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

(a) Either τJ ∈ N (V : ,J )
⊥, in which case τ T
J η = 0 for all η ∈ N (V : ,J ) and, according to (3.10), there are
two symmetric and opposite stem vectors associated with J, namely ± sgn(η0) for some arbitrary
η0 ∈ N (V : ,J ) \ {0}.
(b) Or τJ /∈ N (V : ,J )
⊥, in which case τ T
J η ̸= 0 for some η ∈ N (V : ,J ) and, actually, for all η ∈
N (V : ,J )\{0} since null(V : ,J ) = 1. In this case, there is a single asymmetric stem vector associated
with J, namely sgn(η+), for some η+ ∈ N (V : ,J ) such that τ T
J η+ > 0.
We have shown, in particular, that the symmetry (resp. asymmetry) property of a stem vector does
not depend on the choice of η ∈ N (V : ,J ) \ {0} (resp. satisfying τ T
J η > 0).
4) The stem vectors may have diﬀerent sizes, because the circuits may have diﬀerent sizes.
5) The sets S(V, τ ), Ss(V, τ ) and Sa(V, τ ) are neither vector spaces nor groups. However, given a
stem vector σ ∈ {±1}J , one can consider −σ as the opposite of σ in {±1}J , so that −σ ∈ {±1}
J (with
the same J). With this meaning given to −σ, one deﬁnes

(3.12) − S(V, τ ) := {−σ ∈ {±1}
J : σ ∈ S(V, τ ) and J := J(σ)}.

Proposition 3.7(1) below claims that σ ∈ Ss(V, τ ) when ±σ ∈ S(V, τ ), which justiﬁes a posteriori the
qualiﬁer “symmetric” given to the stem vectors in Ss(V, τ ).
6) A matrix V ∈ Rn×p of rank r has at most ( p
r+1
) circuits and this bound is reached if and only
if the columns of V are in linear general position (deﬁnition 3.13 below) [14]; in that case, the circuits
are exactly the selections of r + 1 columns of V . Since there are 1 or 2 stem vectors per circuit, there
are at most between ( p
r+1) and 2( p
r+1
) stem vectors. These numbers can be exponential in p.

It is easy to see that (see [19])

(3.13) − S(V, τ ) = S(V, −τ ) and − Sa(V, τ ) = Sa(V, −τ ).

Here are some more properties of the stem vectors, which are direct consequences of their deﬁnition.
The properties stated in proposition 3.7 can be symbolically represented like in ﬁgure 3.3. In the next
proposition, we use the symbol “ ·∪ ” for the disjoint union of sets.

S(V, 0)

Sa(V, τ )

Sa(V, −τ )

S(V, τ )

Ss(V, τ )

S0(V, τ )

S([V ; τ T], 0)

Fig. 3.3. Symbolic representation of the sets S(V, τ ), Ss(V, τ ), Sa(V, τ ), S(V, 0), S0(V, τ ), deﬁned by (3.19),
and S([V ; τ T], 0), respecting propositions 3.7 and 3.12. The horizontal dashed line aims at representing the reﬂexion
between a stem vector σ and its opposite −σ: Ss(V, τ ), S(V, 0), S0(V, τ ) and S([V ; τ T], 0) are symmetric in the sense
that −Ss(V, τ ) = Ss(V, τ ), −S(V, 0) = S(V, 0), −S0(V, τ ) = S0(V, τ ) and −S([V ; τ T], 0) = S([V ; τ T], 0). By proposi-
tions 3.8 and 3.12, the diagram simpliﬁes when τ ∈ R(V T), since then Sa(V, τ ) = Sa(V, −τ ) = S0(V, τ ) = ∅ and there
is only one set left.

Proposition 3.7 (stem vector properties). Let V ∈ Rn×p and τ ∈ Rp. Then,
1) S(V, τ ) ∩ S(V, −τ ) = Ss(V, τ ) = Ss(V, −τ ),
2) S(V, τ ) ∪ S(V, −τ ) = S(V, 0),
3) Ss(V, τ ) ·∪ Sa(V, τ ) ·∪ Sa(V, −τ ) = S(V, τ ) ·∪ Sa(V, −τ ) = S(V, 0).

Proof. 1) The last equality can be deduced from the ﬁrst one, so that only the latter needs to be
proved.
[⊆] Let σ ∈ S(V, τ ) ∩ S(V, −τ ). Then, on the one hand, σ = sgn(η) ∈ {±1}
J for some J ∈ C(V )
and some η ∈ N (V : ,J ) \ {0} verifying τ T
J η ⩾ 0 and, on the other hand, −σ = sgn(˜η) ∈ {±1}
J (the
same J, see remark 3.6(5)) for some ˜η ∈ N (V : ,J ) \ {0} verifying τ T
J ˜η ⩾ 0. Since null(V : ,J ) = 1 by (3.9),

PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 9

˜η = αη for some α ∈ R∗. Then, −σ = sgn(˜η) = sgn(α) sgn(η) = sgn(α)σ shows that sgn(α) = −1, so
that 0 ⩽ τ T
J ˜η = α(τ T
J η). Hence τ T
J η ⩽ 0, so that τ T
J η = 0 and σ is symmetric.
[⊇] Since Ss(V, τ ) ⊆ S(V, τ ), it suﬃces to show that Ss(V, τ ) ⊆ S(V, −τ ) or −Ss(V, τ ) ⊆ S(V, τ )
by (3.13). If σ ∈ Ss(V, τ ) and J := J(σ), one has J ∈ C(V ), σ = sgn(η) for some η ∈ N (V : ,J ) \ {0}
verifying τ T
J η = 0. Then, clearly, −σ = sgn(−η) with −η ∈ N (V : ,J ) \ {0} verifying τ T
J (−η) = 0.
Therefore, −σ ∈ S(V, τ ).
2) [⊆] It suﬃces to show that S(V, τ ) ⊆ S(V, 0) for an arbitrary τ , which is quite clear since a
stem vector σ := sgn(η) ∈ S(V, τ ) with J := J(σ) must satisfy one more property (namely τ T
J η ⩾ 0)
than those in S(V, 0).
[⊇] Let σ ∈ S(V, 0) and J = J(σ). Then, σ := sgn(η) ∈ {±1}
J for some η ∈ N (V : ,J ) \ {0}. We
see that σ ∈ S(V, τ ) if τ T
J η > 0, σ ∈ S(V, −τ ) if τ T
J η < 0 and both sets S(V, τ ) ∩ S(V, −τ ) = Ss(V, τ )
if τ T
J η = 0.
3) Let us ﬁrst show that the sets in the left-hand side are disjoint. The sets Ss(V, τ ) and Sa(V, τ )
are disjoint by their deﬁnition. By point 1, Ss(V, −τ ) = Ss(V, τ ), so that Ss(V, τ ) and Sa(V, −τ ) are
disjoint by their deﬁnition. Next, one cannot ﬁnd an s ∈ Sa(V, τ ) ∩ Sa(V, −τ ), since s would be in
Ss(V, τ ) by point 1, which is in contradiction with s ∈ Sa(V, τ ).
Now, the ﬁrst equality follows from S(V, τ ) = Ss(V, τ ) ·∪ Sa(V, τ ) and the second equality follows
from Ss(V, τ ) ∪ Sa(V, τ ) = S(V, τ ), Ss(V, τ ) ∪ Sa(V, −τ ) = Ss(V, −τ ) ∪ Sa(V, −τ ) = S(V, −τ ) and
point 2.

In complement to the characterizations of the centered arrangements in proposition 3.2 (by the
symmetry of S(V, τ )), the following characterization is given in terms of the absence of asymmetric
stem vector. For a proof, see [19].

Proposition 3.8 (centered arrangement and symmetric stem vector set). For an aﬃne hyper-
plane arrangement, the following properties are equivalent:
(i) the arrangement is centered,
(ii) all the stem vectors are symmetric.

The following proposition extends naturally [18, proposition 3.10] to the aﬃne arrangements con-
sidered in this paper. The possibility of having the equivalence (3.14) was a certiﬁcate for the ap-
propriateness of the proposed deﬁnition 3.5 of stem vector. The role of this equivalence is important
in the design of algorithms having a dual aspect, like those developed in section 5. The proof of the
proposition is grounded on duality, via Motzkin’s alternative (2.1).

Proposition 3.9 (covering test). For s ∈ {±1}
p,

(3.14) s ∈ S(V, τ )
c ⇐⇒ sJ ∈ S(V, τ ) for some J ⊆ [1 : p].

Proof. [⇒] Take s ∈ S(V, τ )c. Our goal is to show that the index set J ⊆ [1 : p] in the right-hand
side of (3.14) can be determined as one satisfying the following two properties:

{x ∈ Rn : sj(vT
j x − τj) > 0 for all j ∈ J} = ∅,(3.15a)
 ∀ J0 ⊊ J, {x ∈ Rn : sj(vT
j x − τj) > 0 for all j ∈ J0} ̸= ∅.(3.15b)

To show that a J satisfying (3.15a) and (3.15b) exists, let us start with J = [1 : p], which veriﬁes
(3.15a), since s ∈ S(V, τ )
c. Next, remove one index j from [1 : p] if (3.15a) holds for J = [1 : p] \ {j}.
Pursuing the elimination of indices j in this way, one ﬁnally obtain an index set J satisfying (3.15a)
and {x ∈ Rn : sj(vT
j x − τj) > 0 for all j ∈ J \ {j0}} ̸= ∅ for all j0 ∈ J. Then, (3.15b) clearly holds.
We claim that, for a J satisfying (3.15a) and (3.15b), sJ is a stem vector, which will conclude the
proof of the implication.
To show that sJ , with J verifying (3.15a)-(3.15b), is a stem vector, we stick to deﬁnition 3.5 and
start by showing that J is a matroid circuit. By (3.15a), J ̸= ∅. Next, by Motzkin’s alternative (2.1)

10 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

with A := Diag(sJ )V T
: ,J and a := sJ · τJ , (3.15a) and (3.15b) are respectively equivalent to

∃ α ∈ RJ
+ \ {0} such that V : ,J (sJ · α) = 0, τ T
J (sJ · α) ⩾ 0,(3.15c)
 ∀ J0 ⊊ J, ∄ α′ ∈ RJ0
+ \ {0} such that V : ,J0 (sJ0 · α′) = 0, τ T
J0(sJ0 · α′) ⩾ 0.(3.15d)

From these properties, one deduces that α > 0 (α ⩾ 0 by (3.15c) and α has no zero component
since otherwise (3.15d) would not hold) and that null(V : ,J ) ⩾ 1 (sJ · α ∈ N (V : ,J ) \ {0}). To show
that null(V : ,J ) = 1, we proceed by contradiction. Suppose that there is a nonzero α′′ ∈ RJ that
is not colinear with α and that veriﬁes V : ,J (sJ · α′′) = 0. Since α and α′′ are nonzero and not
colinear, they have at least two components and one can ﬁnd r ∈ R such that β := α′′ − rα ∈ RJ

has at least one positive and one negative component (take for instance r := (r1 + r2)/2, where
r1 := max{r ∈ R : rα ⩽ α′′} < r2 := min{r ∈ R : α′′ ⩽ rα}). One can also assume that

(3.15e) τ T
J (sJ · β) ⩾ 0,

otherwise replace β by −β (one can check below that this sign inversion has no unpleasant impact on the
reasoning). Now, set t := 1/ max{−βj/αj : j ∈ J}, which is positive, and J0 := {j ∈ J : αj + tβj > 0},
so that J \ J0 = {j ∈ J : αj + tβj = 0}. Using the fact that β has positive components and the
deﬁnition of t, we see that ∅ ̸= J0 ⊊ J. Let us introduce α′ := α + tβ ⩾ 0, which veriﬁes α′
j > 0 for
j ∈ J0 ̸= ∅ and α′
j = 0 for j ∈ J \ J0 ̸= ∅. Therefore,

V : ,J0 (sJ0 · α′
J0 )

= V : ,J (sJ · α′) [α′
J\J0 = 0]

= V : ,J (sJ · α) + t V : ,J (sJ · β) [α′ := α + tβ]

= tV : ,J (sJ · α′′) − rt V : ,J (sJ · α) [V : ,J (sJ · α) = 0, β = α′′ − rα]

= 0 [V : ,J (sJ · α′′) = V : ,J (sJ · α) = 0]

and
 τ T
J0 (sJ0 · α′
J0 ) = τ T
J (sJ · α′) [α′
J\J0 = 0]

= τ T
J (sJ · α) + t τ T
J (sJ · β) [α′ := α + tβ]

⩾ 0 [τ T
J (sJ · α) ⩾ 0, (3.15e), t > 0].

These last two outcomes are in contradiction with (3.15d), as expected.
To show that J ∈ C(V ) deﬁned by (3.9), we still have to prove that V : ,J0 is injective when J0 ⊊ J.
Equivalently, it suﬃces to show that any β ∈ N (V : ,J ) with some zero component vanishes. We proceed
by contradiction. If there is a β ∈ N (V : ,J )\{0} with a zero component, sJ ·α and β would be two linearly
independent vectors in N (V : ,J ) (since sJ · α has no zero component), contradicting null(V : ,J ) = 1.
Now, since sJ = sgn(sJ · α), since sJ · α ∈ N (V : ,J ) and τ T
J (sJ · α) ⩾ 0 by (3.15c) and since J is a
matroid circuit of V , sJ is a stem vector (deﬁnition 3.5).
[⇐] Since sJ is a stem vector, it reads sJ := sgn(η) ∈ {±1}
J for some J ∈ C(V ) and some η ∈ RJ

satisfying V : ,J η = 0 and τ T
J η ⩾ 0. Then, α := sJ · η = |η| is in RJ
+ \ {0} and veriﬁes V : ,J (sJ · α) = 0
and τ T
J (sJ · α) ⩾ 0. By Motzkin’s alternative (2.1), there is no x ∈ Rn such that sJ · (V T
: ,J x − τJ ) > 0.
Hence, there is certainly no x ∈ Rn such that s · (V Tx − τ ) > 0. This means that s ∈ S(V, τ )c.

We say that s ∈ S(V, τ )
c covers a sign vector σ ∈ {±1}J for some J ⊆ [1 : p] if sJ = σ. Given a set
of stem vecors S, checking whether a sign vector s covers some σ ∈ S is called below a covering test.
This operation is an essential step of the dual algorithms of section 5.

3.4. Augmented matrix. According to deﬁnition 3.2, verifying whether s ∈ S(V, τ ) amounts to
checking whether there is an x ∈ Rn such that s · (V Tx − τ ) > 0 or, equivalently [58], whether there is
a pair (x, ξ) ∈ Rn × R such that

s · ([V ; τ T]T[x; ξ]) > 0 and ξ = −1.

PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 11

The ﬁrst condition above reads s ∈ S([V ; τ T], 0) and refers to the linear arrangement in Rn+1 governed
by the augmented matrix [V ; τ T]. This presentation of the problem shows that there must be links
between the following sign vector sets and between the following stem vector sets

S(V, 0), S(V, τ ) and S([V ; τ T], 0),(3.16a)
 S(V, 0), S(V, τ ) and S([V ; τ T], 0).(3.16b)

For example, we already know the inclusions S(V, 0) ⊆ S(V, τ ) and S(V, τ ) ⊆ S(V, 0) from proposi-
tions 3.3(1) and 3.7(2).
This section aims at identifying and recalling a few properties where the augmented matrix [V ; τ T]
intervenes, which are useful for designing the algorithms in section 6. In section 3.4.1, some links
between the sets in (3.16a) are highlighted. Section 3.4.2 establishes some connections between the
circuits of V and [V ; τ T], as well as between the stem vector sets in (3.16b). We also recall the
deﬁnitions of arrangements in linear and aﬃne general positions.
Viewing an aﬃne arrangement in x ∈ Rn as the intersection of a linear arrangement in (x, ξ) ∈ Rn+1

with the aﬃne space {(x, ξ) ∈ Rn+1 : ξ = −1} is called the method of coning in [39, deﬁnition 1.15].

3.4.1. Sign vectors of the augmented matrix. Recall the deﬁnition of Ss(V, τ ) and Sa(V, τ )
in (3.7) and the properties (3.8). In the next proposition, we use the symbol “ ·∪ ” for the disjoint union
of sets. Point 4 of this proposition was already given by Winder [58, last formula of page 817] and
proved by a geometric argument; hence, the presented analytic approach brings another point of view.

Proposition 3.10 (properties with S([V ; τ T], 0)). Let A(V, τ ) be an arrangement with V ∈ Rn×p

and τ ∈ Rp. Then, the following properties hold.
1) S(V, τ ) ∩ S(V, −τ ) = S(V, 0) ⊆ S(V, τ ) ⊆ S([V ; τ T], 0) = S(V, τ ) ∪ S(V, −τ ).
2) S(V, τ )
c ∪ S(V, −τ )c = S(V, 0)c ⊇ S(V, τ )
c ⊇ S([V ; τ T], 0)
c = S(V, τ )c ∩ S(V, −τ )
c.
3) S(V, 0) ·∪ Sa(V, τ ) ·∪ Sa(V, −τ ) = S([V ; τ T], 0).
4) 2|S(V, τ )| = |S(V, 0)| + |S([V ; τ T], 0)|.
5) 2|S(V, τ )
c| = |S(V, 0)c| + |S([V ; τ T], 0)c|.

Proof. 1) The ﬁrst equality repeats proposition 3.3(2), using (3.7), the ﬁrst inclusion repeats propo-
sition 3.3(1) and the second inclusion is straightforward: if s ∈ S(V, τ ), one has s · (V Tx − τ ) > 0 for
some x ∈ Rn or s · ([V ; τ T]T[x; −1]) > 0, implying that s ∈ S([V ; τ T], 0).
Consider now the last equality. [⊆] Let s ∈ S([V ; τ T], 0), so that s · (V Tx + τ ξ) > 0 for some
(x, ξ) ∈ Rn × R. By homogeneity, it follows that s ∈ S(V, τ ) if ξ < 0, that s ∈ S(V, −τ ) if ξ > 0 and
that s ∈ S(V, 0) = S(V, τ ) ∩ S(V, −τ ) if ξ = 0. [⊇] By the second inclusion, S(V, τ ) ⊆ S([V ; τ T], 0) and
S(V, −τ ) = −S(V, τ ) ⊆ −S([V ; τ T], 0) = S([V ; τ T], 0).
2) Take the complement of the sets in point 1.
3) Let us ﬁrst show that the sets are disjoint. By (3.7) and proposition 3.3(2), one has Sa(V, τ ) =
S(V, τ ) \ S(V, 0), so that S(V, 0) ∩ Sa(V, τ ) = ∅. The same reasoning with −τ instead of τ yields
S(V, 0) ∩ Sa(V, −τ ) = ∅. Finally,

Sa(V, τ ) ∩ Sa(V, −τ ) = [S(V, τ ) ∩ S(V, 0)c] ∩ [S(V, −τ ) ∩ S(V, 0)
c]

= [S(V, τ ) ∩ S(V, −τ )] ∩ S(V, 0)c

= S(V, 0) ∩ S(V, 0)c

= ∅.

Consider now the identity:

S(V, 0) ∪ Sa(V, τ ) ∪ Sa(V, −τ ) = S(V, 0) ∪ [S(V, τ ) ∩ S(V, 0)c] ∪ [S(V, −τ ) ∩ S(V, 0)c]

= S(V, 0) ∪ S(V, τ ) ∪ S(V, −τ )

= S([V ; τ T], 0) [point 1].

12 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

4) The identity results from

|S([V ; τ T], 0)| = |S(V, τ )| + |S(V, −τ )| − |S(V, τ ) ∩ S(V, −τ )| [point 1]

= 2|S(V, τ )| − |S(V, 0)| [(3.6), (3.7), proposition 3.3(2)].

5) Each set in point 4 is a part of {±1}p of cardinality 2
p. Hence, the identity in point 4 gives

2(2
p − |S(V, τ )
c|) = (2
p − |S(V, 0)
c|) + (2p − |S([V ; τ T], 0)c|).

Point 5 follows after subtracting 2p+1 from both sides.

3.4.2. Circuits and stem vectors of the augmented matrix. The next propositions highlight
connections between the circuits and the stem vectors of V and those of the augmented matrix [V ; τ T].
Recall from proposition 3.2 that an arrangement is centered if and only if τ ∈ R(V T). Note also that

rank([V ; τ T]) = { rank(V ) if τ ∈ R(V T)
rank(V ) + 1 otherwise,
(3.17a)
 null([V ; τ T]) = { null(V ) if τ ∈ R(V T)
null(V ) − 1 otherwise.
(3.17b)

The formula of rank([V ; τ T]) is clear and the one of null([V ; τ T]) can be deduced from (3.17a) by the
rank-nullity theorem.

Proposition 3.11 (circuits of V and [V ; τ T]). Let V ∈ Rn×p and τ ∈ Rp. Then, the following
properties are equivalent:
(i) C(V ) = C([V ; τ T]),
(ii) C(V ) ⊆ C([V ; τ T]),
(iii) τ ∈ R(V T), meaning that that the arrangement A(V, τ ) is centered.

Proof. [(i) ⇒ (ii)] Clear.
[(ii) ⇒ (iii)] Let J ∈ C(V ). Then, null(V : ,J ) = 1 by (3.9). By assumption, J ∈ C([V ; τ T]), so that
null([V ; τ T] : ,J ) = 1, as well. By (3.17b), τJ ∈ R(V T
: ,J ) = N (V : ,J )
⊥. According to remark 3.6(3.a), the
stem vectors associated with J are symmetric. Since J is arbitrary in C(V ), one has S(V, τ ) = Ss(V, τ ),
implying that the arrangement is centered (proposition 3.8).
[(iii) ⇒ (i)] Let J ⊆ [1 : p] and J0 ⊊ J. When τ ∈ R(V T), one has τJ ∈ R(V T
: ,J ) and τJ0 ∈ R(V T
: ,J0 ),
so that (3.17b) yields

null([V ; τ T] : ,J ) = null(V : ,J ) and null([V ; τ T] : ,J0) = null(V : ,J0).

It follows that null([V ; τ T] : ,J ) = 1 and null([V ; τ T] : ,J0 ) = 0 for all J0 ⊊ J if and only if null(V : ,J ) = 1
and null(V : ,J0 ) = 0 for all J0 ⊊ J. In other words, J ∈ C([V ; τ T]) if and only if J ∈ C(V ). We have
shown that C([V ; τ T]) = C(V ).

The implication (ii) ⇒ (i) of lemma 3.11 is not based on the fact that one would always have
C(V ) ⊇ C([V ; τ T]), which is not true. As a counter-example, take V = [
1 0 1 1
0 1 1 1] and τ T = [0 0 1 2],
in which case one has C(V ) = {{3, 4}, {1, 2, 3}, {1, 2, 4}}, while C([V ; τ T]) = {{1, 2, 3, 4}}. Actually,
the property C(V ) ⊇ C([V ; τ T]), which is therefore weaker than those in lemma 3.11, has various
other equivalent interesting formulations, including Ss(V, τ ) = S([V ; τ T], 0), as shown by the following
proposition. Recall ﬁgure 3.3 for a symbolic representation of the stem vector sets.

Proposition 3.12 (stem vectors of A(V, τ ) and A([V ; τ T], 0)). Consider an arrangement A(V, τ ).
Then,

(3.18) Sa(V, τ ) ∩ S([V ; τ T], 0) = ∅ and Ss(V, τ ) ⊆ S([V ; τ T], 0),

with equality in the last inclusion if the arrangement is centered. More precisely, the following properties
are equivalent:
 PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 13

(i) Ss(V, τ ) = S([V ; τ T], 0),
(ii) Ss(V, τ ) ⊇ S([V ; τ T], 0),
(iii) C(V ) ⊇ C([V ; τ T]),
(iv) τJ ∈ R(V T
: ,J ), for all J ∈ C([V ; τ T]).

Proof. 1) [(3.18)1] Let σ ∈ S([V ; τ T], 0) and J := J(σ). Then, σ = sgn(η) for some η ∈
N ([V ; τ T] : ,J ) \ {0}. This η veriﬁes η ∈ N (V : ,J ) \ {0} and τ T
J η = 0. It follows that σ /∈ Sa(V, τ ),
either because J /∈ C(V ) or because J ∈ C(V ), in which case σ ∈ Ss(V, τ ) by the properties of η.
[(3.18)2] Let σ ∈ Ss(V, τ ) and J := J(σ). Then, J ∈ C(V ) and σ = sgn(η) for some η ∈
N (V : ,J ) \ {0} verifying τ T
J η = 0. It follows that η ∈ N ([V ; τ T] : ,J ) \ {0}. To show that σ ∈ S([V ; τ T], 0),
one still has to verify that J ∈ C([V ; τ T]) (deﬁnition 3.9). First, J ̸= ∅, since J ∈ C(V ). Next,
null([V ; τ T] : ,J ) = 1, since η ∈ N ([V ; τ T] : ,J ) \ {0} and null([V ; τ T] : ,J ) ⩽ null(V : ,J ) = 1 (because
J ∈ C(V )). Finally, for all J0 ⊊ J, one has null([V ; τ T] : ,J0) = 0, since null([V ; τ T] : ,J0) ⩽ null(V : ,J0) = 0
(because J ∈ C(V )).
2) Suppose now that the arrangement A(V, τ ) is centered (or τ ∈ R(V T)) and let us show that
Ss(V, τ ) ⊇ S([V ; τ T], 0), Let σ ∈ S([V ; τ T], 0) and J := J(σ). Then, J ∈ C([V ; τ T]) and σ = sgn(η)
for some η ∈ N ([V ; τ T] : ,J ) \ {0}. Then, η ∈ N (V : ,J ) \ {0} and τ T
J η = 0. We see that it suﬃces now to
observe that J ∈ C(V ), which results from the implication (iii) ⇒ (i) of proposition 3.11.
3) Consider now the equivalences (i)-(iv).
[(i) ⇔ (ii)] By (3.18)2.
[(ii) ⇒ (iii)] Let J ∈ C([V ; τ T]). By remark 3.6(3.a), there is a stem vector σ ∈ {±1}
J that is in
S([V ; τ T], 0), hence in Ss(V, τ ) by (ii). This latter fact implies that J ∈ C(V ).
[(iii) ⇒ (iv)] Let J ∈ C([V ; τ T]). By (iii), J ∈ C(V ), so that null([V ; τ T] : ,J ) = null(V : ,J ) (these
nullities = 1). Then, (3.17b) implies that τJ ∈ R(V T
: ,J ).
[(iv) ⇒ (ii)] Let σ ∈ S([V ; τ T], 0) and J := J(σ). Then σ = sgn(η) for some η ∈ N ([V ; τ T] : ,J )\{0}.
Then, η ∈ N (V : ,J ) \ {0} and τ Tη = 0, so that it suﬃces to show that J ∈ C(V ). This property follows
from J ∈ C([V ; τ T] : ,J ), since J ∈ C([V ; τ T]), from C([V ; τ T] : ,J ) = C(V : ,J ), by τJ ∈ R(V T
: ,J ) and the
implication (iii) ⇒ (i) of proposition 3.11, and from C(V : ,J ) ⊆ C(V ).

Recall (3.12)2. In the algorithm of section 6.3, it will be interesting to partition S([V ; τ T], 0) in
Ss(V, τ ) and S0(V, τ ), where

(3.19) S0(V, τ ) := S([V ; τ T], 0) \ Ss(V, τ ).

Let us conclude this section by recalling the notions of general positions, which are used in (3.21)-
(3.23), in the next section and in the description of the test problems. Note that the ﬁrst expressions
in deﬁnitions 3.13 and 3.14 are geometric in nature (they are given in terms of hyperplanes), while the
second ones have an algebraic/analytic ﬂavor (they make use of the rank). Proofs of their equivalences
are given in [19] and in the references thereof.

Definition 3.13 (linear general position). Let be given V ∈ Rn×p of rank r, without zero column.
The linear arrangement A(V, 0) is (or the columns of V are) said to be in linear general position if the
following equivalent properties hold

∀ I ⊆ [1 : p] : dim(∩i∈I H 0
i ) = n − min(|I|, r),

∀ I ⊆ [1 : p] : rank(V : ,I ) = min(|I|, r),

where H 0
i := {x ∈ Rn : V T
: ,ix = 0} for i ∈ [1 : p].

Definition 3.14 (aﬃne general position). Let be given V ∈ Rn×p of rank r, without zero column.
The aﬃne arrangement A(V, τ ) is said to be in aﬃne general position if the following equivalent

14 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

properties hold

∀ I ⊆ [1 : p] : { ∩i∈I Hi ̸= ∅ and dim(∩i∈I Hi) = n − |I| if |I| ⩽ r
∩i∈I Hi = ∅ if |I| ⩾ r + 1,

∀ I ⊆ [1 : p] : { rank(V : ,I ) = min(|I|, r)
rank([V ; τ T] : ,I ) = min(|I|, r + 1).

Observe that the conditions deﬁning linear general position are included in those deﬁning aﬃne
general position, so that the former are weaker than the latter. The arrangement in the left-hand side
pane of ﬁgure 3.1 is in linear general position, while those in the middle and right-hand side panes are
in aﬃne general position. See also the arrangement in example 3.16, which is in linear general position
but not in aﬃne general position.
To conclude this section, let us recall a few cardinality estimates that will be used several times.
For a matrix V ∈ Rn×p of rank r without zero column, Schl¨aﬂi’s bound [51, p. 211] reads

(3.21) |S(V, 0)| ⩽ 2 ∑

i∈[0 : r−1]
 (p − 1
i
 ),

with equality if and only if A(V, 0) is in linear general position [58, 1966, corollary] (see also [17, § 4.2.1]).
One also has, for τ ∈ Rp:

(3.22) |S(V, τ )| ⩽ ∑

i∈[0 : r]
 (p
i
),

with equality if and only if A(V, τ ) is in aﬃne general position [10][59, (5.7)1] (see also [19, (3.38)]). If
the arrangement is in aﬃne general position, one has [19]

(3.23) |Sa(V, τ )| = (p − 1
r
 ).

3.5. Chamber boundedness. Evaluating the number of bounded chambers of a hyperplane ar-
rangement has long been achieved using various approaches. It has been shown that if the arrangement
A(V, τ ), with V ∈ Rn×p and τ ∈ Rp, is in aﬃne general position and if rank(V ) = n, then the number
of bounded chambers is (p−1
n ), which is the value in right-hand side of (3.23). This formula is attributed
to Buck [10, 1943] in [59], who uses a geometric argument and the Euler characteristic. Zaslavsky [59]
derives the number of relatively bounded chamber (i.e., bounded in R(V )) by using the characteristic
polynomial (see also [53, proposition 2.4]). In contrast, the approach followed below to identify (not
just to count) the bounded chambers uses convex analysis tools, which are more direct and simpler for
readers who are familiar with these techniques.
We show by the following proposition that, if the arrangement is in linear general position (a weaker
assumption than the aﬃne general position) and if rank(V ) = n, the bounded chambers are exactly
those whose sign vectors are asymmetric. In this case, the bounded chambers are listed in the set
Sa(V, τ ) of asymmetric sign vectors, a set that is computed by the algorithms described in sections 4-6.
As a by-product, when the arrangement is also in aﬃne general position, one recovers the number of
bounded chambers thanks to (3.23). Identifying the bounded chambers of an arrangement is useful in
the analysis of hypergeometric functions [2], as well as in cosmology and particle physics [42, 23].
The chamber associated with a sign vector s ∈ {±1}
p is denoted by Cτ (s) := {x ∈ Rn : s · (V Tx −
τ ) > 0}. Its asymptotic cone [49, 34] is given by

(3.24) Cτ (s)∞ = {d ∈ Rn : s · (V Td) ⩾ 0},

whose interior is

(3.25) int Cτ (s)
∞ = {d ∈ Rn : s · (V Td) > 0} = C0(s).

PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 15

Proposition 3.15 (chamber boundedness). Let A(V, τ ) be a proper arrangement.
1) If rank(V ) < n, then none of the chambers are bounded.
2) For s ∈ S(V, τ ), one has

Cτ (s) is bounded =⇒ C0(s) = ∅ ⇐⇒ s ∈ Sa(V, τ )

and the ﬁrst implication is an equivalence if rank(V ) = n and the arrangement is in linear general
position.

Proof. Set r := rank(V ).
1) Let s ∈ S(V, τ ) and x ∈ Cτ (s). Since r < n, one can ﬁnd a d ∈ R(V )
⊥ \ {0} = N (V T) \ {0}.
Then, x + Rd ⊆ Cτ (s), which shows that the chamber Cτ (s) is unbounded.
2) If Cτ (s) is bounded, then Cτ (s)∞ = {0} [49, theorem 8.4][34, proposition 2.2.3]. By (3.25),
C0(s) = ∅.
Let us now prove the equivalence by contraposition: C0(s) ̸= ∅ if and only if there is a d ∈ Rn

such that s · ((V T)d) > 0, meaning that s ∈ S(V, 0) or, equivalenlty, s /∈ Sa(V, τ ).
Consider ﬁnally the reciprocal of the ﬁrst implication. Assume that C0(s) = ∅, that r = n and that
the arrangement is in linear general position. To show that the chamber Cτ (s) is bounded, it suﬃces to
prove that its asymtotic cone Cτ (s)
∞, given by (3.24), reduces to {0} [49, 34]. For this goal, let us take a
direction d ∈ Rn satisfying s · (V Td) ⩾ 0. We have to show that d = 0. Set I := {i ∈ [1 : p] : sivT
i d = 0},
so that

(3.26) sI · (V T
: ,I d) = 0 and sI c · (V T
: ,I cd) > 0.

We examine two complementary cases.
r [|I| ⩽ r] Since the arrangement is in linear general position, rank(V : ,I ) = |I|, meaning that V : ,I is
injective or that V T
: ,I is surjective. Then, one can ﬁnd p ∈ Rn such that sI ·(V T
: ,I p) > 0. Now, taking
t > 0 suﬃciently small and using (3.26), one gets s · (V T(d + tp)) > 0, contradicting C0(s) = ∅.
r [|I| > r] In this case, by the linear general position of the arrangement and r = n, V T
: ,I is injective,
so that sI · (V T
: ,I d) = 0 by (3.26)1 readily implies that d = 0, as desired.

Example 3.16 (bounded chambers with only linear general position). Consider the
arrangement A(V, τ ) deﬁned by

V = [
1 0 1 −1
0 1 1 1

] ,

τ T = [
0 0 1 1
] .
 −+++

−+−+ +++−
 H2++−−−+−−
 +−+−−−−− +−−−−−−+
 ++++
H1H3 H4

This arrangement is in linear general position but not in aﬃne general position. The number of bounded
chambers is 2, which is not the value (3
2
) = 3 given in the right-hand side of (3.23), but is indeed the
number of asymmetric sign vectors, as claimed by proposition 3.15, which are (−1, +1, −1, −1) and
(+1, +1, −1, −1).

4. Chamber computation - Primal approaches. This section starts the algorithmic part of
the paper, which focuses on the computation of the sign vector set S ≡ S(V, τ ), deﬁned by (3.2),
of the considered arrangement A(V, τ ). The bijection φ, deﬁned by (3.3), establishes a one-to-one
correspondence between these sign vectors and the chambers of the arrangement. In this section, we
assume that the arrangement is proper, which means that V has only nonzero columns:

(4.1) ∀ j ∈ [1 : p] : V : ,j ̸= 0.

16 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

Many algorithms have been designed to list the chambers of an arrangement (see the introduction).
Most of them adopt a primal strategy, in the sense that they focus on the realization of the inequality
system s · (V Tx − τ ) > 0 in (3.2), by trying to compute witness points x ∈ Rn. Section 4.1 describes the
S-tree mechanism of [45], while section 4.2 adapts to aﬃne arrangements some of the enhancements
brought to this algorithm in [18], which deals with linear arrangements.

4.1. Primal S-tree algorithm. For k ∈ [1 : p], deﬁne the partial sign vector set Sk ⊆ {±1}k and
its complement S c
k in {±1}
k by

(4.2) Sk ≡ Sk(V, τ ) := S(V:,[1 : k], τ[1 : k]) and S c
k := {±1}
k \ Sk.

Hence, Sk is the sign vector set of the arrangement associated with the matrix V:,[1 : k] ∈ Rn×k and
the vector τ[1 : k] ∈ Rk. Let us denote by vi the ith column of V , by τi the ith component of τ and
by Hi := {x ∈ Rn : vT
i x = τi} the ith hyperplane. The S-tree is a tree structure, whose k level
contains the sign vectors in Sk. Therefore, in addition to its empty root, the complete S-tree has p
levels and the bottom one is Sp = S(V, τ ). The ﬁrst level is S1 = {+1, −1}, because the inequalities
(+1)(vT
1 x+ − τ1) > 0 and (−1)(vT
1 x− − τ1) > 0 are satisﬁed by the following two witness points,
positioned on either side of the hyperplane H1:

(4.3) x+ := (τ1 + 1)v1/∥v1∥2 and x− := (τ1 − 1)v1/∥v1∥
2.

The level k + 1 is obtained by considering the additional pair (vk+1, τk+1) ∈ Rn × R, which deﬁnes
the hyperplane Hk+1. It can be constructed from the level k as follows. By the general assumption
(4.1), every node s ∈ Sk may have one or two children, namely (s, +1) and/or (s, −1). Geometrically,
there are two children if and only if the chamber associated with s is divided into two parts by the
hyperplane Hk+1, but this geometric view is not easy to detect algebraically in terms of sign vectors (see
below). Figure 4.1 shows the three levels of the S-tree corresponding to the arrangement in the middle
pane of ﬁgure 3.1. Now, instead of searching the children of every s ∈ Sk in order to obtain Sk+1, the

−+

++ +− −+ −−

++−+++ +−+ +−− −++ −+− −−+ −−−

Fig. 4.1. S-tree of the arrangement in the middle pane of ﬁgure 3.1. The gray node is actually absent from the
tree, since there is no chamber associated with s = (−1, −1, +1) (no x such that s · (V Tx − τ ) > 0).

S-tree will be constructed by a depth-ﬁrst search [45], in order to avoid having to keep Sk in memory,
which can be large. In this approach, at most p nodes along a path from the root node to a leaf node
must be stored at a time. Note that, in the case of a linear arrangement (i.e., with τ = 0) or, more
generally, a centered arrangement (i.e., with τ ∈ R(V T)), S(V, τ ) is symmetric (proposition 3.2) and
only half of the sign vectors must be computed.
In the algorithm descriptions, it is assumed that the problem data (V, τ ) is known and we do not
repeat this data on entry of the functions. A function can modify its arguments. Let us now outline
the algorithm exploring the S-tree, called p stree (algorithm 4.1, “p” for “primal”), which uses for
this purpose a recursive procedure called p stree rec (algorithm 4.2).

Algorithm 4.1 (p stree). // primal S-tree algorithm [45]

1. p stree rec(+1, x+) // x+ given by (4.3)1
2. p stree rec(−1, x−) // x− given by (4.3)2

Algorithm 4.2 (p stree rec(s ∈ {±1}
k, x ∈ Rn)).
It is assumed that x is a witness point for s.

PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 17

1. if (k = p)
2. Output s and return // s is a leaf of the S-tree; end the recursion
3. endif
4. if (vT
k+1x = τk+1)
5. p stree rec((s, +1), x + εvk+1) // (s, +1) ∈ Sk+1
6. p stree rec((s, −1), x − εvk+1) // (s, −1) ∈ Sk+1
7. return
8. endif
9. sk+1 := sgn(vT
k+1x − τk+1) // (s, sk+1) ∈ Sk+1
10. p stree rec((s, sk+1), x)
11. if ((s, −sk+1) is feasible with witness point ˜x)
12. p stree rec((s, −sk+1), ˜x) // (s, −sk+1) ∈ Sk+1
13. endif

The algorithm p stree executes the recursive algorithm p stree rec for constructing the descen-
dants of the nodes “+1” and “−1” of the ﬁrst level of the S-tree. For its part, the algorithm p stree rec
constructs the descendants of a node s ∈ Sk, knowing a witness point, that is a point x ∈ Rn in the
chamber associated with s, hence si(vT
i x − τi) > 0 for i ∈ [1 : k]. Let us examine its instructions.
r If k = p (instructions 1..3), the node s is a leaf of the S-tree and has no child. Then, p stree rec just
outputs s (it prints or stores s, depending on the user’s wish) and returns to the calling procedure.
r Instructions 4..8 consider the case when x is exactly in the hyperplane Hk+1 (in section 4.2.2, the
mechanism used in that case will also be applied when x is suﬃciently closed to Hk+1): then s has
two children (s, ±1), since, for an easily computable suﬃciently small ε > 0, xε
± := x±εvk+1 satisﬁes
si(vT
i xε
± − τi) > 0, for all i ∈ [1 : k] and ±(vT
k+1xε
± − τk+1) > 0.
r In the sequel vT
k+1x ̸= τk+1, so that sk+1 := sgn(vT
k+1x − τk+1) ∈ {±1} and (s, sk+1) ∈ Sk+1 with
witness point x. The instructions 9..10 deal with that situation, asking to compute the descendants
of (s, sk+1).
r Instructions 11..13 examine whether (s, −sk+1) is also a child of s, which amounts to determining
whether the following system has a solution ˜x ∈ Rn (see below how this can be done):

(4.4) { si(vT
i ˜x − τi) > 0, for i ∈ [1 : k]
−sk+1(vT
k+1 ˜x − τk+1) > 0.

If this is the case, the descendants of (s, −sk+1) are searched using p stree rec.

To determine whether the strict inequalities (4.4) are compatible, one can, like in [45], recast the
problem as a linear optimization problem (LOP) and check whether its optimal value is negative. The
linear optimization problem reads

(4.5)
 min(x,α)∈Rn×R α
s.t. si(vT
i x − τi) + α ⩾ 0, for i ∈ [1 : k]
−sk+1(vT
k+1x − τk+1) + α ⩾ 0
α ⩾ −1.

This optimization problem is feasible (by taking an arbitrary x ∈ Rn and α ∈ R suﬃciently large) and
bounded (i.e., its optimal value is bounded below, here by −1), so that it has a solution [6, theorem 19.1].
Denote it by (¯x, ¯α). It is clear that (4.4) is feasible if and only if ¯α < 0. This equivalence can then be
used as a feasibility criterion for (4.4). One can ﬁnd in [19] a discussion on the possibility to detect
whether (s, −sk+1) is a symmetric sign vector in Sk+1 (in the sense of deﬁnition 3.1) by an optimization
technique.
For future reference, we quote in a proposition an observation, which is deduced from the algorithm.

Proposition 4.3 (binary S-tree). Let A(V, τ ) be a proper arrangement. Then, each node of the
S-tree that is not a leaf has one or two children.

18 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

The next proposition characterizes the sign vectors of Sk that have two children in Sk+1. In its
statement, Pk+1 : Rn → Hk+1 − Hk+1 denotes the orthogonal projector on the subspace v⊥
k+1 that is
parallel to the aﬃne space Hk+1; while ˆxk+1 := τk+1vk+1/∥vk+1∥2 is the unique point in N (Pk+1) ∩
Hk+1. We also denote by Pk+1 the transformation matrix of the projector, so that Pk+1 V : ,[1 : k] can be
viewed as the product of two matrices. Note that in (4.6b), ˜V := Pk+1 V : ,[1 : k] may have zero columns,
in which case, by its deﬁnition (3.2), the set S( ˜V , ˜τ ) will be nonempty if the corresponding components
of ˜τ do not vanish. The proof of the proposition is given in [19].

Proposition 4.4 (two child criterion). Let V ∈ Rn×p, s ∈ {±1}
k for some k ∈ [1 : p − 1] and ˆxk+1
be the unique point in N (Pk+1) ∩ Hk+1. Then,

(s, +1) and (s, −1) ∈ Sk+1
⇐⇒ ∃ x ∈ Rn : si(vT
i x − τi) > 0, for i ∈ [1 : k], and vT
k+1x − τk+1 = 0(4.6a)
 ⇐⇒ s ∈ S(Pk+1 V : ,[1 : k], τ[1 : k] − V T
: ,[1 : k] ˆxk+1).(4.6b)

The next proposition improves and extends to aﬃne arrangement proposition 4.6 in [18]. Its proof
and other properties of algorithm 4.1 are given in [19]. We denote by vect{v1, . . . , vk} the vector space
spanned by the vectors v1, . . . , vk.

Proposition 4.5 (incrementation). Let V = [v1 · · · vp] ∈ Rn×p and τ ∈ Rp.
1) If s ∈ S c
k, then (s, ±1) ∈ S c
k+1. Consequently, |S c
k+1| ⩾ 2|S c
k|.
2) If vk+1 /∈ vect{v1, . . . , vk}, then, (s, ±1) ∈ Sk+1 for all s ∈ Sk, |Sk+1| = 2|Sk| and |S c
k+1| = 2|S c
k|.
3) If vk+1 ∈ vect{v1, . . . , vk}, V : ,[1 : k+1] has no zero column, Hk+1 ̸= Hi for i ∈ [1 : k], and rk :=
dim vect{v1, . . . , vk}, then |Sk+1| ⩾ |Sk| + 2rk−1.

4.2. Preventing some computations. The main computation cost of algorithm 4.1 comes from
solving the LOPs (4.5) at some inner nodes. This section describes three ways of bypassing LOPs. They
are adapted from [18], where only linear arrangements are considered, and are identiﬁed by the letters
A, B and C (the letters appearing in the section titles), which will also be used to label more eﬃcient
variants of algorithm 4.1. These variants signiﬁcantly speed up the algorithm by reducing the numbers
of LOPs to solve.

4.2.1. A - Rank of the arrangement. Instead of starting the S-tree with the two nodes of
S1 = {+1, −1}, like in algorithm 4.1, one can start it with the 2r nodes of Sr = {±1}r, by considering
ﬁrst a selection of r := rank(V ) linearly independent vectors whose S-tree is easy to construct without
having to solve any LOP. Here are the details.
Numerically, r linearly independent vectors can be found by a QR factorization of V :

V P = QR,

with P ∈ {0, 1}p×p is a permutation matrix, Q ∈ Rn×n is orthogonal and R ∈ Rn×p is upper triangular
with R[r+1 : n], : = 0. To simplify the presentation, let us assume that P is the identity matrix, in
which case the ﬁrst r vectors v1, . . . , vr (or columns of V ) are linearly independent, and let us note
Vr := V : ,[1 : r], Qr := Q : ,[1 : r] and Rr := R[1 : r],[1 : r]. By proposition 4.5(2),

Sr = {±1}
r.

To launch the recursive algorithm 4.2, one still need to compute a witness point xs associated with
any s ∈ Sr. For this purpose, one computes a point ˆx ∈ ∩r
i=1Hi, hence verifying V T
r ˆx = τ[1 : r], by
ˆx := Vr(V T
r Vr)−1τ[1 : r]. Next, for any s ∈ {±1}r, one computes ds := QrR−T
r s ∈ Rn. Let us show that
xs := ˆx + ds is a witness point of the considered s. One has

V T
r xs − τ[1 : r] = V T
r [Vr(V T
r Vr)−1τ[1 : r] + QrR−T
r s] − τ[1 : r] = (QrRr)TQrR−T
r s = s.

Therefore, s · (V T
r xs − τ[1 : r]) = s · s = e > 0, as desired.

PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 19

4.2.2. B - Handling of a hyperplane proximity. In the description of algorithm 4.2, it is
shown why a witness point x of a sign vector s ∈ Sk that belongs to Hk+1, i.e., vT
k+1x = τk+1, allows
the algorithm to certify that both (s, +1) and (s, −1) are in Sk+1, without having to solve a LOP. We
show with the next proposition that this is still true when x is near Hk+1, in the sense (4.7). Note
that this proximity to Hk+1 is measured by strict inequalities, which is more stable with respect to
numerical perturbations than an equality.

Proposition 4.6 (two children without LOP). Let s ∈ Sk and x ∈ Rn verifying s · (V T
:,[1 : k]x −
τ[1 : k]) > 0. Suppose that vk+1 ̸= 0 and

(4.7) max
sivT
i vk+1>0 τi − vT
i x
vT
i vk+1
︸ ︷︷ ︸
=: tmin
 < τk+1 − vT
k+1x
||vk+1||2
︸ ︷︷ ︸
=: t0
 < min
sivT
i vk+1<0 τi − vT
i x
vT
i vk+1
︸ ︷︷ ︸
=: tmax
 .

Then, for t− ∈ (tmin, t0), x− := x + t−vk+1 is a witness point of (s, −1) and, for t+ ∈ (t0, tmax),
x+ := x + t+vk+1 is a witness point of (s, +1).

Proof. Note ﬁrst that, in (4.7), the arguments of the maximum are negative and the arguments of
the minimum are positive; therefore, both inequalities are veriﬁed if vT
k+1x = τk+1 (t0 = 0), that is,
when x ∈ Hk+1. Now, one has, for i ∈ [1 : k],

si(vT
i (x + tvk+1) − τi) > 0 ⇐⇒
 



 t < si(τi−vT
i x)
sivT
i vk+1 if sivT
i vk+1 < 0
t ∈ R if sivT
i vk+1 = 0

t > si(τi−vT
i x)
sivT
i vk+1 if sivT
i vk+1 > 0.

Since the conditions imposed on t in the right-hand side of the equivalence above are satisﬁed by any
t ∈ (tmin, tmax), it follows that x± are witness points of s. One has

t > t0 := τk+1−vT
k+1x
||vk+1||2 ⇐⇒ vT
k+1(x + tvk+1) − τk+1 > 0,

t < t0 := τk+1−vT
k+1x
||vk+1||2 ⇐⇒ vT
k+1(x + tvk+1) − τk+1 < 0.

Since t+ (resp. t−) veriﬁes the condition in the left-hand side of the ﬁrst (resp. second) equivalence
above, it follows that x+ (resp. x−) is a witness point of (s, +1) (resp. (s, −1)).

4.2.3. C - Choosing the order of the vectors. Every inner node of the S-tree has one or two
children and this number is sometimes detected in algorithm 4.2 by solving a LOP, which is a time-
consuming operation. Therefore, a way of decreasing the computation time is to reduce the number
of inner nodes of the S-tree. This property can be obtained by choosing wisely the order in which the
pairs (vi, τi), or hyperplanes Hi, are taken into account when constructing the branches of the S-tree
(this order can be diﬀerent from one branch to another), with the goal of placing the nodes with a
single child close to the root of the tree. This strategy has been investigated in [18, § 5.2.4.C] and we
adapt the heuristic to the present context of aﬃne arrangements.
Denote by Ts := {i
s
1, . . . , is
k} the set of the indices of the hyperplanes selected to reach node s (Ts
depends on s). At this node, the algorithm must choose the next hyperplane to consider, whose index
is among the index set T c
s := [1 : p] \ Ts. With the goal of preventing, as much as possible, the node s
from having two children, a natural idea is to ignore the indices of T c
s , for which proposition 4.6 ensures
two children. In the remaining index set, denote it by T b
s , the chosen index is the one maximizing the
quantity |vT
i x − τi|/∥[vi; τi]∥ for i ∈ T b
s (x is the witness point associated by the algorithm with the
current node s), since the larger this quantity is, the further x is from the chosen hyperplane, which
should increase the chances that s will have only one child.
Note that proposition 4.5 is no longer valid when the order in which the hyperplanes are considered
is not identical for all the nodes of an S-tree level.

20 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

5. Chamber computation - Dual approaches. The enumeration of the chambers of an arrange-
ment A(V, τ ) can be tackled by an approach diﬀerent from those presented in section 4 (algorithm 4.1
and its improvements A, B and C), sometimes (or always) replacing optimization phases by algebra
techniques. More speciﬁcally, we say that an algorithm has a dual aspect when it uses the concept
of stem vector (deﬁnition 3.5) and the covering test of proposition 3.9. Such a dual approach was
introduced in [18, §§ 5.2.2-5.2.3] for linear arrangements.
This section also assumes (4.1), that is, V has no zero column.

5.1. Algorithms using all the stem vectors. Proposition 3.9 establishes a link between the
infeasible sign vectors, those in S(V, τ )
c, and the stem vectors. This section presents two algorithms that
start with the computation of the complete stem vector set S(V, τ ); a plain algorithm for computing
this set is given in [19]; it can be demanding in computing time. The ﬁrst algorithm uses these stem
vectors to compute S(V, τ )
c, from which the feasible sign vector set S(V, τ ) = {±1}
p \ S(V, τ )
c can be
deduced (section 5.1.1). The second method computes S(V, τ ) like in the primal S-tree algorithm of
section 4.1, but without solving linear optimization problems and without computing witness points
(section 5.1.2).

5.1.1. Crude dual algorithm. The algorithm described in this section, algorithm 5.1, is a
“crude” way of obtaining the sign vector set S(V, τ ) from the stem vector set S(V, τ ). It uses the charac-
terization of proposition 3.9. For each stem vector σ ∈ S(V, τ ) with associated circuit J = J(σ) ⊆ [1 : p],
the algorithm generates all the infeasible sign vectors s ∈ S(V, τ )
c satisfying sJ = σ and sJ c ∈ {±1}
J c.
This generation is made by the function stem to infeas sign vectors in a straightforward man-
ner (the precise computation is not detailed). Once S(V, τ )
c is computed, S(V, τ ) is obtained by
{±1}
p \ S(V, τ )c.
This stem to infeas sign vectors function can produce duplicated sign vectors, which justiﬁes
the cleaning operation in line 5 (this one could be done simultaneously with the union in line 4). For
example, with V = [1, 1, 1] and τ T = [1, 0, 1], the stem vectors (1, −1) ∈ {±1}
{1,2} and (−1, 1) ∈
{±1}
{2,3} produce the same infeasible sign vector (1, −1, 1).

Algorithm 5.1 (crude dual(S)). // crude dual algorithm
1. Sc = ∅ // initialization of S(V, τ )
c

2. stem vectors(Ss, Sa) // see [19]
3. for σ ∈ Ss ∪ Sa do
4. Sc = Sc ∪ stem to infeas sign vectors(σ, p)
5. Remove duplicates in Sc
6. endfor
7. S := {±1}p \ Sc

Despite its simplicity, algorithm 5.1 is usually not very attractive. Indeed, each stem vector σ ∈
{±1}
J produces the exponential number 2
|J c| of sign vectors s with sJ c ∈ {±1}J c . As a result, for
large p, the algorithm handles a large amount of data, which can take much computing time.

5.1.2. Dual S-tree algorithm. Another possibility is to use the S-tree structure introduced in
section 4.1. Here is the main idea. Assume that a sign vector s in Sk has been computed (the set Sk is
deﬁned by (4.2)). Then, algorithm 4.2 determines whether (s, sk+1) belongs to Sk+1, for sk+1 ∈ {±1}.
As explained in the description of algorithm 4.2, the belonging of (s, sk+1) to Sk+1 can be revealed
by solving a linear optimization problem. Algorithm 5.2–5.3 below does this diﬀerently. It uses the
computed stem vector set S(V, τ ) and is based on the fact that, for all k ∈ [2 : p]:

S(V : ,[1 : k], τ[1 : k]) = {σ ∈ S(V, τ ) : J(σ) ⊆ [1 : k]}.

Therefore, according to proposition 3.9, to determine whether (s, sk+1) is in Sk+1, it suﬃces to see
whether it covers a stem vector σ ∈ S(V, τ ) such that J(σ) ⊆ [1 : k + 1]. If so (s, sk+1) ∈ S c
k+1 and any

PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 21

˜s ∈ {±1}p, extending (s, sk+1) by ±1, will be in S(V, τ )c, so that the S-tree may be pruned at (s, sk+1).
Otherwise (s, sk+1) ∈ Sk+1 and the recursive exploration of the S-tree is pursued below (s, sk+1).

Algorithm 5.2 (d stree). // dual S-tree algorithm
1. stem vectors(Ss, Sa) // see [19]
2. d stree rec(∅,Ss ∪ Sa)

Algorithm 5.3 (d stree rec(s ∈ {±1}
k,S)).
1. if (k = p)
2. Output s and return // s is a leaf of the S-tree; end the recursion
3. endif
4. if ((s, +1) covers a stem vector of S)
5. d stree rec((s, −1),S)
6. else
7. d stree rec((s, +1),S)
8. if ((s, −1) does not cover a stem vector of S)
9. d stree rec((s, −1),S)
10. endif
11. endif

Here are some explanations and observations on the recursive algorithm 5.3.
r If the test in line 4 holds, proposition 3.9 tells us that (s, +1) is an infeasible sign vector for the
arrangement A(V : ,[1 : k+1], τ[1 : k+1]). This has two consequences:
– there is no point in exploring the descendants of (s, +1) in the S-tree, which explains why there
is no recursive call to d stree rec((s, +1),S) in that case and
– (s, −1) is necessarily a feasible sign vector for the arrangement A(V : ,[1 : k+1], τ[1 : k+1]) since each
node of the S-tree has at least one child (proposition 4.3), which explains why there is a call to
d stree rec((s, −1),S) in line 5.
r Line 7 is justiﬁed since, at that point, (s, +1) is a feasible sign vector for the arrangementA(V : ,[1 : k+1],
τ[1 : k+1]).
r Line 9 is justiﬁed since, at that point, (s, −1) is a feasible sign vector for the arrangementA(V : ,[1 : k+1],
τ[1 : k+1]).
r The algorithm does not use witness points, unlike the primal S-tree algorithm 4.1–4.2.
Let us emphasize the fact that algorithm 5.2 does not require to solve linear optimization problems.
While this might look enticing, since the LOPs are the main cost of the primal S-tree algorithm 4.1,
one must be aware of two facts. First, the computation of all the circuits of V can be time-consuming
(for instance, the algorithm presented in [19] requires the exploration of a tree, whose nodes at level k
may have up to p − k descendants). Second, determining whether a sign vector covers a stem vector
may not be very fast when the number of stem vectors is large, which is usually the case when p is
large (see remark 3.6(6)) [43].

5.2. Algorithms using some stem vectors. Instead of computing the stem vectors exhaus-
tively, which is generally a time-consuming task, one can get a few stem vectors from the optimal dual
variables of some linear optimization problems (LOPs) encountered in algorithm 4.1, those that are
associated with an infeasible sign vector. This technique is described in section 5.2.1. Then, one can
design a kind of primal-dual algorithm for computing S(V, τ ). This one builds the S-tree, but, in order
to save running time, it makes use of the stem vectors collected during its construction to prune some
unfruitful branches of the S-tree, which avoids having to solve some LOPs. This algorithm is presented
in section 5.2.2.

5.2.1. Getting stem vectors from linear optimization. In line 11 of algorithm 4.2, one has
to decide whether (s, −sk+1) is in Sk+1 and it is suggested, after the description of the algorithm, to

22 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

determine this belonging by solving the linear optimization problem (LOP) (4.5). The Lagrangian dual
of this problem [6, 25, 18] reads

(5.1)
 max(λ,µ)∈Rk+1×R ∑
i∈[1 : k] λisiτi − λk+1sk+1τk+1 − µ
s.t. λ ⩾ 0
µ ⩾ 0∑
i∈[1 : k] λisivi = λk+1sk+1vk+1∑
i∈[1 : k+1] λi + µ = 1,

where λ ∈ Rk+1 is the dual variable associated with the ﬁrst k + 1 constraints of (4.5) and µ the dual
variable associated with its last constraint.
The next proposition gives conditions ensuring that a circuit of V can be obtained from a speciﬁc
solution to the dual problem (5.1) when (s, −sk+1) /∈ Sk+1. We denote by val (4.5) (resp. val (5.1)) the
optimal value of the primal (resp. dual) optimization problem (4.5) (resp. (5.1)). By strong duality in
linear optimization [6, 25] and the fact that problem (4.5) has a solution, one has val (4.5) = val (5.1).

Proposition 5.4 (matroid circuit detection from optimization).
1) Problem (5.1) has a solution, say (λ, µ) ∈ Rk+1
+ × R+.
2) If s ∈ Sk and (s, −sk+1) /∈ Sk+1, then val (4.5) ⩾ 0, λk+1 > 0 and µ = 0.
3) If, in addition, (λ, µ) is an extreme point of the feasible set of (5.1), then
r J := {i ∈ [1 : k + 1] : λi > 0} ∈ C(V ),
r if val (4.5) = 0, ±(s, −sk+1)J are the two stem vectors associated with J,
r if val (4.5) > 0, (s, −sk+1)J is the unique stem vector associated with J.

Proof. 1) By strong duality in linear optimization [50, 6, 25], the fact that the primal problem (4.5)
has a solution implies that the dual problem (5.1) has also a solution, say (λ, µ).
2) Suppose that s ∈ Sk and that (s, −sk+1) /∈ Sk+1. Let (x, α) be a solution to (4.5) (α = val (4.5)
is uniquely determined). Let us show that

(5.2a) λk+1 > 0 and µ = 0.

The optimal multiplier µ is associated with the constraint α ⩾ −1 of the optimization problem (4.5),
which is inactive (α ⩾ 0 when (s, −sk+1) /∈ Sk+1), so that it vanishes. We show that λk+1 > 0 by
contradiction, assuming that λk+1 = 0. Then, strong duality would imply that 0 ⩽ α = val (4.5) =
val (5.1) = ∑

i∈[1 : k] λisiτi, while the third constraint of (5.1) would read ∑

i∈[1 : k] λisivi = 0. Since
λ[1 : k] ̸= 0 by the fourth constraint in (5.1), λk+1 = 0 and µ = 0, it would follow from Motzkin’s
alternative (2.1) that there is no x ∈ Rn such that si(vT
i x − τi) > 0, for i ∈ [1 : k], which is in
contradiction with the assumption s ∈ Sk.
3) Let I := {i ∈ [1 : k], λi > 0}. By assumption and µ = 0, (λ, 0) is an extreme point of the feasible
set of problem (5.1), which implies that the vectors [11, 50, 25]

(5.2b) {(
sivi
1
 )
i∈I , (−sk+1vk+1
1
 )} are linearly independent,

where we used the fact that λk+1 > 0 and µ = 0 by (5.2a).
One can deduce from this property that the vectors

(5.2c) {sivi}i∈I are linearly independent.

Suppose indeed that ∑
i∈I αisivi = 0 for some real numbers (αi)i∈I . It suﬃces to show that these
numbers vanish and we do so in two steps.
r We ﬁrst show by contradiction that ∑
i∈I αi = 0. If this were not the case, one could ﬁnd t ∈ R such
that ∑

i∈I (λi + tαi) + λk+1 = 0. Now, using the third constraint of problem (5.1), we would have
that η := ((λi + tαi)i∈I , λk+1) is in the null space of the nonsingular matrix whose columns are the
vectors in (5.2b), which would imply that η = 0, in contradiction with λk+1 > 0 imposed by (5.2a).

PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 23

r Using ∑

i∈I αi = 0 and ∑

i∈I αisivi = 0, we have that the vector ((αi)i∈I , 0) is in the null space of
the nonsingular matrix whose columns are the vectors in (5.2b). Hence all the αi’s vanish.
Now, set J := {i ∈ [1 : k + 1] : λi > 0}, which is I ∪ {k + 1} by the deﬁnition of I and (5.2a), and
introduce the diagonal matrix D ∈ RJ×J deﬁned by Di,i = si if i ∈ I and Dk+1,k+1 = −sk+1. Using
(5.2c), we see that null(V : ,J D) = 1.

By the third constraint of (5.1), we have that λJ ∈ N (V : ,J D) \ {0}. Since λJ > 0, proposition 3.4 tells
us that J is a circuit of V : ,J D, hence a circuit of V .
Since η := DλJ ∈ N (V : ,J ) \ {0} is such that τ T
J η = val (4.5), we see that the number of stem
vectors associated with J is governed by val (4.5), as described in remark 3.6(3). In addition, sgn(η) =
(s, −sk+1)J , because λJ > 0, showing that (s, −sk+1)J is a stem vector.

A solution to problem (5.1) that is an extreme point of its feasible set can be obtained by the
dual-simplex algorithm [50]. Note that, since λk+1 > 0, k + 1 always belongs to the selected circuit J
of V .

5.2.2. Primal-dual S-tree algorithm. Proposition 5.4(3) shows how circuits and their associ-
ated stem vectors can be obtained when the S-tree primal algorithm 4.1 solves a LOP (4.5) with an
appropriate solver and observes that the sign vector (s, −sk+1) is infeasible. Now, with the partial list
of stem vectors so computed, which grows throughout the iterations, the algorithm can detect some
infeasible sign vectors by using proposition 3.9, like in the crude dual algorithm 5.1 or in the S-tree dual
algorithm 5.2, but without having to solve a LOP. In practice, this technique saves much computing
time. Here is this primal-dual S-tree algorithm, based on the just presented idea, which has many
similarities with the primal S-tree algorithm 4.1.

Algorithm 5.5 (pd stree). // primal-dual S-tree algorithm
1. S = ∅
2. pd stree rec(+1, x+, S) // x+ given by (4.3)1
3. pd stree rec(−1, x−, S) // x− given by (4.3)2

Algorithm 5.6 (pd stree rec(s ∈ {±1}k, x ∈ Rn, S)).
It is assumed that x is a witness point for s.
1. if (k = p)
2. Output s and return // s is a leaf of the S-tree; end the recursion
3. endif
4. if (vT
k+1x = τk+1)
5. pd stree rec((s, +1), x + εvk+1, S) // (s, +1) ∈ Sk+1
6. pd stree rec((s, −1), x − εvk+1, S) // (s, −1) ∈ Sk+1
7. return
8. endif
9. sk+1 := sgn(vT
k+1x − τk+1) // (s, sk+1) ∈ Sk+1
10. pd stree rec((s, sk+1), x, S)
11. if ((s, −sk+1) covers a stem vector of S)
12. return
13. elseif ((s, −sk+1) is feasible with witness point ˜x)
14. pd stree rec((s, −sk+1), ˜x, S) // (s, −sk+1) ∈ Sk+1
15. else
16. Add one or two stem vectors to S
17. endif

We only comment some instructions of the primal-dual S-tree algorithm 5.5 that diﬀer from those
of the primal S-tree algorithm 4.1.

24 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

r Unlike algorithm 5.2, which computes all the stem vectors at ﬁrst, algorithm 5.5 initializes the list of
stem vectors S to the empty set in line 1. This list is next gradually ﬁlled by algorithm 5.6 in line 16.
r For more eﬃciency, one could adapt lines 4..6 of algorithm 5.6 by using the improvement described
in section 4.2.2.
r Lines 11..12 are new with respect to algorithm 4.1. They are used to check whether (s, −sk+1) ∈ S c
k+1,
using the stem vectors collected in S and proposition 3.9, without having to solve a LOP.
r Lines 15..16 are also new with respect to algorithm 4.1. They use proposition 5.4(3) to detect a new
circuit, hence one or two new stem vectors, which are put in S. For this, it is necessary to solve the
LOP in line 13 by a method computing an extreme point of the dual feasible set of this problem.
Algorithm 5.5 can be improved by introducing the modiﬁcations A, B and C of sections 4.2.1–4.2.3.

6. Compact version of the algorithms. All the algorithms computing the sign vector set
S(V, τ ) presented so far, except algorithm 5.1, recursively construct the S-tree introduced in algo-
rithm 4.1, whose sign vectors form the set (recall the deﬁnition (4.2) of Sk(V, τ ))

(6.1) T (V, τ ) := ⋃

k∈[1 : p] Sk(V, τ ).

When the arrangement is not centered (equivalently, τ /∈ R(V T)), some sets Sk(V, τ ) are asymmetric
(proposition 3.2), so that the sign vectors of the two subtrees T +(V, τ ) := {s ∈ T (V, τ ) : s1 = +1} and
T −(V, τ ) := {s ∈ T (V, τ ) : s1 = −1} of the S-tree, rooted at the nodes {+1} and {−1}, respectively,
are not opposite to each other. Therefore, one cannot just compute T +(V, τ ) or T −(V, τ ) to get all
T (V, τ ) (recall that when the arrangement is centered, S(V, τ ) = S(V, 0) and only half of the sign
vectors needs to be computed [18]). Nevertheless, these two subtrees have some opposite sign vectors,
the symmetric ones, those in T (V, 0) = ∪k∈[1 : p]Sk(V, 0). The set of asymmetric sign vectors in T (V, τ )
is denoted by Ta(V, τ ) := ⋃

k∈[1 : p] Sa,k(V, τ ),

where Sa,k(V, τ ) := Sk(V, τ ) \ Ss,k(V, τ ) and Ss,k(V, τ ) := Sk(V, τ ) ∩ Sk(V, −τ ); see (3.7). Therefore, it
is natural to look for a way to avoid as much as possible repeating the costly operations (linear opti-
mization problems or stem vector coverings) common to the construction of the two subtrees T +(V, τ )
and T −(V, τ ). The goal of this section is to propose algorithms having that property; they can have a
primal or dual nature.

6.1. The compact S-tree. For an arrangement A(V, τ ), with V ∈ Rn×p and τ ∈ Rp, and for
k ∈ [1 : p], we denote the arrangement associated with the ﬁrst k columns of V and the ﬁrst k components
of τ by Ak(V, τ ) := A(V:,[1 : k], τ[1 : k]).

By proposition 3.10 (see also ﬁgure 3.2), we have that

Sk(V, 0) ⊆ Sk(V, τ ) ⊆ Sk([V ; τ T], 0) = Sk(V, τ ) ∪ Sk(V, −τ ),(6.2a)
 Sk([V ; τ T], 0) \ Sk(V, 0) = Sa,k(V, τ ) ·∪ Sa,k(V, −τ ).(6.2b)

The algorithms described in this section are based on the following considerations. By (3.7), the
set T (V, τ ) of the feasible sign vectors of the S-tree can be written T (V, 0) ·∪ Ta(V, τ ). Taking the
intersection with T +(V, τ ) and T −(V, τ ) provides a partition of T (V, τ ) into four sets:

(6.3) T (V, 0) ∩ T +(V, τ ), Ta(V, τ ) ∩ T +(V, τ ), T (V, 0) ∩ T −(V, τ ), Ta(V, τ ) ∩ T −(V, τ ).

Since

(6.4) T (V, 0) ∩ T −(V, τ ) = −[T (V, 0) ∩ T +(V, τ )],

PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 25

only two sets must be computed to be able to retrieve all the sign vectors of T (V, τ ), namely the union
of the ﬁrst two sets of the partition (6.3) and the last one:

T +(V, τ ) and Ta(V, τ ) ∩ T −(V, τ ).

The principle of the algorithms described in this section consists in computing the subtree T +(V, τ )
rooting at s1 = +1 and in grafting to it the subtrees of

−[Ta(V, τ ) ∩ T −(V, τ )],

which is in Ta(V, −τ ). This forms what we call the compact S-tree. More precisely, if s ∈ Sk(V, 0) ∩
T +(V, τ ) and (−s, sk+1) ∈ Sa,k+1(V, τ ) ∩ T −(V, τ ) for some sk+1 ∈ {±1}, the subtree of T −(V, τ )
rooting at (−s, sk+1) is grafted at s in the compact tree (with its sign vectors multiplied by −1, so that
(s, −sk+1) can be a child of s). As a result, the nodes of the level k of the compact S-tree are in one
of the sets

(6.5) Sk(V, 0), Sa,k(V, τ ) or Sa,k(V, −τ ).

Eventually, a sign vector s ∈ Sa(V, −τ ) must be multiplied by −1 to get it in −Sa(V, −τ ) = Sa(V, τ ) ⊆
S(V, τ ). This principle is illustrated in ﬁgure 6.1. Housekeeping is done by attaching a ﬂag s to each

+− −−−+
 −−−−+−−+++−−+−++++ ++−

++
 +++ ++−

++ +−

+
 +−+ +−−

+ −
 −−−+++ +++ ++−

++ +−

+
 +−+ +−−+−+ +−− −++ −+− −−+

++ +− −+ −−

+ −

Fig. 6.1. Standard S-trees (left) and compact S-trees (right) of the arrangements in the middle pane (above, compare
with ﬁgure 4.1) and the right-hand side pane (below) of ﬁgure 3.1. The sign vectors in the white boxes are in T (V, 0),
those in the blue/gray boxes are in Sa(V, τ ) and the one in the blue/gray box with bold edges is in Sa(V, −τ ); this last
sign vector must be multiplied by −1 to get a sign vector in −Sa(V, −τ ) = Sa(V, τ ) ⊆ S(V, τ ).

node s of the resulting tree, in order to specify which of the sign vector sets listed in (6.5) s belongs.
As claimed in point 5 of the next proposition, the grafting process does not introduce nodes with two
diﬀerent ﬂags: if (s, sk+1) ∈ −[Sa,k+1(V, τ ) ∩ T −(V, τ )] is grafted to the compact S-tree, then (s, sk+1)
is not in T +(V, τ ).
The proof of the next proposition is given in [19].

Proposition 6.1 (compact S-tree). Let k ∈ [1 : p−1] and let s ∈ Sk(V, 0) ·∪Sa,k(V, τ ) ·∪Sa,k(V, −τ )
be a sign vector of the compact S-tree. Set S +
k (V, τ ) := Sk(V, τ ) ∩ T +(V, τ ).
1) If s ∈ Sk(V, 0), one child of s in the compact S-tree is in Sk+1(V, 0).
2) If s ∈ Sa,k(V, τ ), the children of s in the compact S-tree are in Sa,k+1(V, τ ).
3) If s ∈ Sa,k(V, −τ ), the children of s in the compact S-tree are in Sa,k+1(V, −τ ).
4) If (s, sk+1) ∈ −[Sa,k+1(V, τ ) ∩ T −(V, τ )] with sk+1 ∈ {±1}, then (s, sk+1) /∈ T +(V, τ ).
5) Level k of the compact S-tree is formed of S +
k (V, τ ) ·∪ (−[Sa,k(V, τ ) ∩ T −(V, τ )]).

6.2. Compact primal S-tree algorithm. In accordance with the presentation of section 6.1,
the compact primal S-tree algorithm, whose reasoned description is given below, ignores the subtree
T −(V, τ ) rooting at {−1}, constructs the subtree T +(V, τ ) rooting at {+1} and grafts to it the opposite

26 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

of the sign vectors in the subtrees of Ta(V, τ ) ∩ T −(V, τ ). Let us describe this algorithm. Its formal
statement is given afterwards.
The algorithm identiﬁes each node at level k of the compact S-tree by a triplet (s, x, s ), where
s ∈ {±1}k is the sign vector of the node, x is a witness point and s ∈ {−1, 0, +1} is a ﬂag specifying
to which sign set s belongs. More speciﬁcally,

(6.6)
 



 s ∈ Sk(V, 0), x is a witness point for s in Ak(V, 0) if s = 0,
s ∈ Sa,k(V, τ ), x is a witness point for s in Ak(V, τ ) if s = +1,
s ∈ Sa,k(V, −τ ), x is a witness point for s in Ak(V, −τ ) if s = −1.

The ﬂag s is used below as a scalar, hence s s is the vector whose ith component is s si. The
initialization of the algorithm is done as follows.

0. Take s1 = +1 ∈ S1(V, 0) and v1 as witness point for s1 in A1(V, 0).

Consider now a node at level k of the compact S-tree, which is speciﬁed by a triplet (s, x, s ) satisfying
(6.6). We just have to specify how the algorithm determines the children of that node.

1. Suppose that s ∈ Sk(V, 0) with x as witness point in Ak(V, 0), i.e., s = 0.

Using proposition 4.6 with τ = 0, the algorithm can detect whether s has two easily computable
children in A(V, 0) and can ﬁnd associated witness points. If such is the case, the algorithm pursues
recursively from (s, +1) and (s, −1) in ∈ Sk+1(V, 0) (hence s = 0), with appropriate witness points.
It returns afterwards.

Otherwise, vT
k+1x ̸= 0, implying that (s, sk+1) ∈ Sk+1(V, 0) for sk+1 := sgn(vT
k+1x) and that the
algorithm can pursue recursively from (s, sk+1) with x as witness point in Ak+1(V, 0).

Now, the algorithm has to specify to what set (s, −sk+1) belongs: Sk+1(V, 0), Sa,k+1(V, τ ), Sa,k+1
(V, −τ ) or Sk+1([V ; τ T], 0)c (there are no other possibilities, see proposition 3.10 and ﬁgure 3.2).
For this purpose, the compact primal S-tree algorithm starts by solving the LOP (4.5) with τ = 0,
to see whether (s, −sk+1) ∈ Sk+1(V, 0). Denote by (x0, α0) a solution to this LOP.

1.1. If α0 < 0, then (s, −sk+1) ∈ Sk+1(V, 0) and the algorithm pursues recursively from (s, −sk+1)
with x0 as witness point in Ak+1(V, 0).
1.2. Otherwise, (s, −sk+1) /∈ Sk+1(V, 0) and the algorithm determines whether (s, −sk+1) ∈ Sk+1
([V ; τ T], 0) by solving the following LOP, which is similar to (4.5) with τ = 0, but for the
arrangement A([V ; τ T], 0) instead of A(V, 0):

(6.7)
 min(x,ξ,α)∈Rn×R×R α
s.t. si(vT
i x + τiξ) + α ⩾ 0, for i ∈ [1 : k]
−sk+1(vT
k+1x + τk+1ξ) + α ⩾ 0
α ⩾ −1.

Denote by (x1, ξ1, α1) a solution to this problem.
1.2.1. If α1 ⩾ 0, then (s, −sk+1) /∈ Sk+1([V ; τ T], 0), hence (s, −sk+1) /∈ Sk+1(V, τ ) ∪ Sk+1
(V, −τ ) by (6.2a) and (s, −sk+1) can be discarded from the generated compact tree.
1.2.2. Otherwise, α1 < 0 and (s, −sk+1) ∈ Sk+1([V ; τ T], 0) \ Sk+1(V, 0) = Sa,k+1(V, τ ) ·∪
Sa,k+1(V, −τ ) by (6.2b). Note that one cannot have ξ1 = 0 in that case, since then one
would have (s, −sk+1) ∈ Sk+1(V, 0), which is excluded in the considered case. There-
fore,
– either ξ1 < 0 and (s, −sk+1) ∈ Sa,k+1(V, τ ), by (6.7), with −x1/ξ1 as witness point
in Ak+1(V, τ ),
– or ξ1 > 0 and (s, −sk+1) ∈ Sa,k+1(V, −τ ), by (6.7), with x1/ξ1 as witness point in
Ak+1(V, −τ ).
In these last two cases, the algorithm can pursue recursively from (s, −sk+1).

PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 27

2. Suppose that s ∈ Sa,k(V, τ ) with x as witness point in Ak(V, τ ), i.e., s = +1.

Using proposition 4.6, the algorithm can detect whether s has two easily computable children in
A(V, τ ) and can ﬁnd associated witness points. If such is the case, the algorithm pursues recursively
from (s, +1) and (s, −1) in ∈ Sa,k+1(V, τ ) (hence s = +1), with appropriate witness points. It
returns afterwards.

Otherwise, vT
k+1x ̸= τk+1, implying that (s, sk+1) ∈ Sa,k+1(V, τ ) for sk+1 := sgn(vT
k+1x − τk+1) and
that the algorithm can pursue recursively from (s, sk+1) with x as witness point in Ak+1(V, τ ) and
s = +1.

Now, the algorithm has to determine whether (s, −sk+1) is infeasible or is in Sa,k+1(V, τ ) (there
are no other possibilities: (s, −sk+1) /∈ Sk+1(V, 0) since s /∈ Sk(V, 0) in the present case). For this
purpose, the algorithm solves (4.5). Let (x2, α2) be a solution.

– If α2 < 0, then (s, −sk+1) ∈ Sa,k+1(V, τ ) and the compact algorithm can pursue recursively from
(s, −sk+1) with x2 as witness point in Ak+1(V, τ ) and s = +1.
– Otherwise, (s, −sk+1) is infeasible in Ak+1(V, τ ) and the algorithm can prune the compact S-tree
at that node.

3. The last case, when s ∈ Sa,k(V, −τ ), with x as witness point in Ak(V, −τ ), i.e., s = −1, is similar
to case 2 and is detailed in [19].

One can now present schematically the compact form of the primal S-tree algorithm 4.1. To
shorten its statement and the one of the next algorithm 6.7, we introduce the following two functions:
output s, which outputs sign vectors of S(V, τ ) at a leaf of the compact S-tree (its behavior is more
complex than for the standard algorithms and depends on the type s of the leaf node s, see (6.6)), and
c p two children, which detects whether s has the two children that are given by proposition 4.6; if
this is the case, it pursues the compact S-tree construction at (s, ±1) and returns true; otherwise, it
returns false.

Algorithm 6.2 (output s(s, s )).
It is assumed that s ∈ {±1}p and that s ∈ {−1, 0, +1}.
1. if ( s = 0)
2. output ±s // s ∈ S(V, 0)
3. else
4. output s s // s ∈ Sa(V, s τ )
5. endif

Algorithm 6.3 (c p two children(s, x, s )).
It is assumed that s ∈ {±1}k and that (s, x, s ) satisﬁes (6.6).
1. if (vT
k+1x ≃ s τk+1) // two easy children in Ak+1(V, s τ )
2. c p stree rec((s, +1), x + t+vk+1, s ) for some t+ ∈ (t0, tmax)
3. c p stree rec((s, −1), x + t−vk+1, s ) for some t− ∈ (tmin, t0)
4. return true
5. else
6. return false
7. endif

We have chosen to present the cases when s = ±1 jointly in lines 22..25, to save space. An expanded
presentation is given in [19].

Algorithm 6.4 (c p stree). Let be given V ∈ Rn×p and τ ∈ Rp.
1. c p stree rec(+1, v1, 0)

28 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

Algorithm 6.5 (c p stree rec(s, x, s )).
It is assumed that s ∈ {±1}k and that (s, x, s ) satisﬁes (6.6).
1. if (k = p) // s is a leaf of the compact S-tree
2. output s(s, s )
3. return
4. endif
5. if (c p two children(s, x, s )) // two easy children in Ak+1(V, s τ )
6. return
7. endif
8. sk+1 := sgn(vT
k+1x − s τk+1) // (s, sk+1) ∈ Sk+1(V, s τ )
9. c p stree rec((s, sk+1), x, s )
10. if ( s = 0) // s ∈ Sk(V, 0) with x as witness point in Ak(V, 0)
11. Solve (4.5) with τ = 0; let (x0, α0) be a solution
12. if (α0 < 0) // (s, −sk+1) ∈ Sk+1(V, 0)
13. c p stree rec((s, −sk+1), x0, 0)
14. else // here (s, −sk+1) /∈ Sk+1(V, 0), check if it ∈ Sk+1([V ; τ T], 0)
15. Solve (6.7); let (x1, ξ1, α1) be a solution // here ξ1 ̸= 0
16. if (α1 < 0) // (s, −sk+1) ∈ Sa,k+1(V, − sgn(ξ1)τ )
17. c p stree rec((s, −sk+1), x1/|ξ1|, − sgn(ξ1))
18. endif
19. endif
20. return
21. endif // here s ∈ {±1}, hence s ∈ Sa,k(V, s τ )
22. Solve (4.5) with τ ↷ s τ ; let (x2, α2) be a solution
23. if (α2 < 0) // (s, −sk+1) ∈ Sa,k+1(V, s τ )
24. c p stree rec((s, −sk+1), x2, s )
25. endif

Observe that, as claimed by proposition 6.1(2-3), once s ∈ Sa,k(V, τ ) (resp. s ∈ Sa,k(V, −τ )), its
descendants in the compact S-tree are all in Sa,l(V, τ ) (resp. Sa,l(V, −τ )) for some l ∈ [k + 1 : p]. In
these cases, the compact algorithm solves at most one LOP per sign vector (in step 22), like in the
standard version of the algorithm, which solves at most one LOP in T +(V, τ ) or T −(V, τ ), not both
since an asymmetric sign vector only appears in one of these subtrees. When s ∈ Sk(V, 0) has one
child in Sa,k+1(V, ±τ ), the compact algorithm solves at most two LOPs (in steps 11 and 15), like in
the standard algorithm (one LOP in T ±(V, τ ) to accept the child in Sa,k+1(V, τ ) and one in T ∓(V, τ )
to reject a child in Sa,k+1(V, τ )). The only sign vectors at which the compact algorithm solves less
LOPs than the standard algorithm are those in S(V, 0) with two symmetric children. In this case, the
compact algorithm solves at most a single LOP (in step 11), while the standard algorithm solves at
most two LOPs (one in each subtree T +(V, τ ) and T −(V, τ )). Therefore, the compact algorithm 6.4 is
all the more advantageous with respect to the standard algorithm 4.1 as |T (V, 0)|/|T (V, τ )| is large (it
is always ⩽ 1); see [43, Appendix A].

6.3. Compact primal-dual S-tree algorithm. We have proposed in section 5 several ways of
using the stem vectors, in order to avoid having to solve all or part of the LOPs of the standard primal
S-tree algorithm 4.1. Most of them have a compact form. In this section, however, in order to make
the presentation short, we only consider a compact version of the primal-dual S-tree algorithm 5.5.
The statement of the algorithm is immediate as soon as we know how it collects the stem vectors and
how it uses them. This is essentially what we clarify in this section, leaving a more detailed description
to [19].
As shown in section 5, stem vectors can be used to detect sign vectors that are not in S(V, τ ), using
proposition 3.9. Our goal in this section is to apply this technique to construct the compact primal-dual

PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 29

S-tree, by “dualizing” the compact primal S-tree algorithm 6.4 (we have found this approach easier
than “compacting” the standard primal-dual S-tree algorithm 5.5). The principle is as follows. Recall
the deﬁnitions (3.11) and (3.19) of Ss(V, τ ), Sa(V, τ ) and S0(V, τ ). The algorithm manages subsets ˜Ss
of Ss(V, τ ), ˜Sa of Sa(V, τ ) and ˜S0 of S0(V, τ ), named collectors, which are initially empty and are
progressively ﬁlled during the iterations (this is explained below). Then, each group of statements in

Algorithm 6.5 Algorithm 6.8
Lines Lines Sign vector set Stem vector set Collectors

11..14 11..19 Sk+1(V, 0) S(V, 0) ˜Ss ∪ ˜Sa ∪ (− ˜Sa)
15..18 20..27 Sk+1([V ; τ T], 0) S([V ; τ T], 0) ˜Ss ∪ ˜S0
22..25 30..39 Sa,k+1(V, s τ ) S(V, s τ ) ˜Ss ∪ ( s ˜Sa)

Table 6.1
Corresponding lines in algorithms 6.5 and 6.8.

algorithm 6.5 (the lines given by the ﬁrst column of table 6.1), dealing with a LOP and its consequences,
is replaced by other lines in algorithm 6.8 (those given by the second column of table 6.1). These latter
lines are organized as follows.
r So as to avoid having to solve certain LOPs, a covering test is run to see whether the sign vector
(s, −sk+1) is in the set in the third column of table 6.1 (recall deﬁnition (4.2)). Appropriate stem
vectors must be used to realize that operation, namely those in the collectors in the ﬁfth column
of table 6.1, which are contained in the sets in the fourth column of table 6.1 (see propositions 3.7
and 3.12, and ﬁgure 3.3).
r If the covering test succeeds (i.e., (s, −sk+1) covers an appropriate stem vector), then (s, −sk+1) is
not in the sign vector set in the third column of table 6.1 (proposition 3.9) and the compact S-tree
is pruned.
r Otherwise, because there is no equality between the stem vector sets in the fourth column of table 6.1
and their collectors in the ﬁfth column of table 6.1, a LOP is solved like in algorithm 6.4.
r If this LOP has a negative optimal value, (s, −sk+1) is in the sign vector set in the third column of
table 6.1 and the recursion is proceeded from that node.
r Otherwise, one or two stem vectors are added to the appropriate collectors in the ﬁfth column of
table 6.1.
This yields the following algorithm. One ﬁrst adapts the c p two children algorithm 6.3, so that it
calls the appropriate procedures of the present framework.

Algorithm 6.6 (c pd two children(s, x, s )).
It is assumed that s ∈ {±1}k and (s, x, s ) satisﬁes (6.6).
1. if (vT
k+1x ≃ s τk+1) // two easy children in Ak+1(V, s τ )
2. c pd stree rec((s, +1), x + t+vk+1, s ) for some t+ ∈ (t0, tmax)
3. c pd stree rec((s, −1), x + t−vk+1, s ) for some t− ∈ (tmin, t0)
4. return true
5. else
6. return false
7. endif

We can now present the result of the adaptation of algorithm 6.4 along the principle described above.

Algorithm 6.7 (c pd stree). Let be given V ∈ Rn×p and τ ∈ Rp.
1. ˜Ss = ∅, ˜Sa = ∅, ˜S0 = ∅ // initial empty collectors
2. c pd stree rec(+1, v1, 0, ˜Ss, ˜Sa, ˜S0)

30 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

Algorithm 6.8 (c pd stree rec(s, x, s , ˜Ss, ˜Sa, ˜S0)).
It is assumed that s ∈ {±1}
k, that (x, s, s ) satisﬁes (6.6) and that ˜Ss ⊆ Ss(V, τ ), ˜Sa ⊆
Sa(V, τ ), ˜S0 ⊆ S0(V, τ ).
1. if (k = p) // s is a leaf of the compact S-tree
2. output s(s, s )
3. return
4. endif
5. if (c pd two children(s, x, s )) // two easy children in Ak+1(V, s τ )
6. return
7. endif
8. sk+1 := sgn(vT
k+1x − s τk+1) // (s, sk+1) ∈ Sk+1(V, s τ )
9. c pd stree rec((s, sk+1), x, s , ˜Ss, ˜Sa, ˜S0)
10. if ( s = 0) // s ∈ Sk(V, 0) with x as witness point in Ak(V, 0)
11. if ((s, −sk+1) does not cover a stem vector of ˜Ss ∪ ˜Sa ∪ (− ˜Sa))
12. Solve (4.5) with τ = 0; let (x0, α0) be a solution
13. if (α0 < 0) // (s, −sk+1) ∈ Sk+1(V, 0)
14. c pd stree rec((s, −sk+1), x0, 0, ˜Ss, ˜Sa, ˜S0)
15. return
16. else
17. Add two or one stem vectors to ˜Ss or ˜Sa, respectively
18. endif
19. endif // here (s, −sk+1) /∈ Sk+1(V, 0), check if it ∈ Sk+1([V ; τ T], 0)
20. if ((s, −sk+1) does not cover a stem vector of ˜Ss ∪ ˜S0)
21. Solve (6.7); let (x1, ξ1, α1) be a solution // here ξ1 ̸= 0
22. if (α1 < 0) // (s, −sk+1) ∈ Sa,k+1(V, − sgn(ξ1)τ )
23. c pd stree rec((s, −sk+1), x1/|ξ1|, − sgn(ξ1), ˜Ss, ˜Sa, ˜S0)
24. else
25. Add two stem vectors to ˜Ss or ˜S0
26. endif
27. endif
28. return
29. endif // here s ∈ {±1}, hence s ∈ Sa,k(V, s τ )
30. if ((s, −sk+1) does not cover a stem vector of ˜Ss ∪ ( s ˜Sa))
31. Solve (4.5) with τ ↷ s τ ; let (x2, α2) be a solution
32. if (α2 < 0) // (s, −sk+1) ∈ Sa,k+1(V, s τ )
33. c pd stree rec((s, −sk+1), x2, s , ˜Ss, ˜Sa, ˜S0)
34. else
35. Add two or one stem vectors to ˜Ss or ˜Sa, respectively
36. endif
39. endif

7. Numerical results. The goal of this section is to assess the eﬃciency of a selection of algo-
rithms among those introduced in sections 4, 5 and 6. Section 7.1 lists and brieﬂy describes the chosen
hyperplane arrangement instances. The considered algorithms are speciﬁed in section 7.2. Section 7.3
details and discusses the results of this evaluation.

7.1. Arrangement instances. This section describes the hyperplane arrangements that form the
test bed for the evaluation of the selected algorithms presented in the next section. These arrangements
A(V, τ ) are speciﬁed by their matrix V ∈ Rn×p and vector τ ∈ Rp (see section 3.1). One always has
p > n and r := rank(V ) = n. We gather them into two groups; the ﬁrst contains aﬃne arrangements

PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 31

that are not centered; the other contains only centered or even linear arrangements. The instance
features are given in table 7.1. More is said on these problems in [19].
Aﬃne arrangements. The given four problems are aﬃne and not centered. Three of them are also
examined in [45]. Their linear versions, obtained by setting τ = 0, were considered in [18]. Random
numbers are generated with the Julia function rand.
r rand-n-p: V and τ are randomly generated in [−5, +5]. These are the test cases named Randomly
generated arrangements in [45] and denoted by “p,n,0” in their table.
r srand-n-p-q: One has V : ,[1 : n] = In and each of the remaining p − n columns has q nonzero random
integer elements, randomly positioned. Each element of τ[n+1 : p] has a 1/2 probability of being a
random integer; it vanishes otherwise; τ[1 : n] = 0. Random integers are taken in [−10 : +10] \ {0}.
r 2d-n-p: The matrix V is such that: V[1 : 2],[1 : n−2] = 0 and V[3 : n],[n−1 : p] = 0. Its remaining elements
and τ are randomly generated integers in [−20 : +20] [18]. These instances can be shown to generalize
those of the Asymptotically worst arrangements in [45], denoted by “r p,n” in their table.
r ratio-n-p-t: V : ,[1 : n], τ[1 : n] are randomly generated in [−50 : +50] and t ∈ [0, 10]. Then, the
remaining columns of [V ; τ T] can either be random with probability 1 − t/10 or randomly generated
linear combinations in [−4 : +4] of the previous vectors. One recovers problem rand-n-p when t = 0.
These test cases are also named Randomly generated arrangements in [45] and denoted by “p,n,t/10”
in their table.
Centered arrangements. The arrangements deﬁned by problem perm-n, taken from [45], are cen-
tered but not linear, the others, taken from [9, 18], are linear. In the experiments, the solvers are run
without allowing them to take advantage of the symmetry of S(V, τ ).
r perm-n: This problem refers to the hyperplane arrangements that are called permutahedron and
denoted similarly in [45] (actually, in [45], perm-d is perm-n with n = d − 1 and the declared values
of |S(V, τ )| is half ours): one has p = n(n + 1)/2, V : ,[1 : n] is the identity matrix and V : ,[n+1 : p] is a
Coxeter matrix [44] (each column is of the form ei − ej for some i < j in [1 : n], where ek is the kth
basis vector of Rn). The vector τ is deﬁned by τi = 1 for i ∈ [1 : n] and τi = 0 for i ∈ [n + 1 : p].
Since (1, . . . , 1) belongs to all the hyperplanes, the arrangement is centered.
r threshold-n refers to the threshold arrangements in [9, § 6.2]: for n ⩾ 2, each column of V is formed
of the components of (1, w) where w ∈ Rn−1 are all the vectors of {0, 1}
n−1 (hence p = 2
n−1) and
τ = 0. This arrangement appears in the study of neural networks [57].
r resonance-n refers to the resonance arrangements in [9, § 6.3]: the columns of V are all the nonzero
vectors with components in {0, 1} (hence p = 2
n − 1) and τ = 0. See [36] for applications.
r crossplt-n refers to the cross-polytope arrangements in [9, § 6.4]: for n ⩾ 2, each column of V
is formed of the components of (1, w) where w ∈ Rn−1 are all the ±ei for i ∈ [1 : n − 1] (hence
p = 2(n − 1)) and τ = 0.
r demicube-n refers to the demicube arrangements in [9, § 6.6]: the columns of V are the components
of (1, w) where w ∈ {w′ ∈ {0, 1}
n−1 : ∑

i w′
i is odd} and τ = 0.

Remarks 7.1 (on table 7.1).
1) As expected, the randomly generated arrangements rand-* are in aﬃne general position (deﬁni-
tion 3.14). This is revealed in table 7.1 by a number |Ss(V, τ )|/2 + |Sa(V, τ )| of circuits of V (5th
and 6th columns, see remark 3.6(3)) that reaches its maximum (4th column), see remark 3.6(6);
by a number |S([V ; τ T], 0)|/2 of circuits of [V ; τ T] (7th column, see [18, after deﬁnition 3.9]) that
reaches its maximum (8th column), see remark 3.6(6); and by a number |S(V, τ )| of sign vectors
(9th column) that reaches its upper bound (10th column), given by (3.22).
2) Half the number of stem vectors of the linear arrangement A([V ; τ T], 0) (7th column) is also the
number |C([V ; τ T])| of circuits of [V ; τ T] (see [18, after deﬁnition 3.9]) and we see that this one is
unrelated to the number of circuits of V (sum of columns 5 and 6). This conﬁrms the observation
made after proposition 3.11, according to which neither C(V ) ⊆ C([V ; τ T]) nor C([V ; τ T]) ⊆ C(V )

32 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

Circuits Stem vectors Stem vectors
of V of A(V, τ ) of A([V ; τ T], 0) Chambers

Problems n p Bound |Ss|/2 |Sa| |S|/2 Bound |S(V, τ )| Bound

rand-5-10 5 10 210 0 210 120 120 638 638
rand-4-11 4 11 462 0 462 462 462 562 562
rand-6-12 6 12 792 0 792 495 495 2510 2510
rand-5-13 5 13 1716 0 1716 1716 1716 2380 2380
rand-7-14 7 14 3003 0 3003 2002 2002 9908 9908
rand-7-15 7 15 6435 0 6435 5005 5005 16384 16384
rand-8-16 8 16 11440 0 11440 8008 8008 39203 39203
rand-9-17 9 17 19448 0 19448 12376 12376 89846 89846

srand-8-20-2 8 20 167960 56 321 987 184756 36225 263950
srand-8-20-4 8 20 167960 1185 70650 94534 184756 213467 263950
srand-8-20-6 8 20 167960 20413 123909 105345 184756 245396 263950

2d-5-20 5 20 38760 0 680 2380 77520 1232 21700
2d-6-20 6 20 77520 1 559 1808 125970 2176 60460
2d-7-20 7 20 125970 0 443 1365 167960 3840 137980
2d-8-20 8 20 167960 0 364 1001 184756 6784 263950

ratio-5-20-7 5 20 38760 97 33945 61452 77520 15136 21700
ratio-5-20-9 5 20 38760 23514 10954 23514 77520 11325 21700
ratio-6-20-7 6 20 77250 238 76595 120663 125970 59519 60640
ratio-6-20-9 6 20 77250 345 71861 106115 125970 53795 60460
ratio-7-20-7 7 20 125970 125 123792 159956 167960 135063 137980
ratio-7-20-9 7 20 125970 154 123731 159636 167960 135038 137980

perm-5 5 15 5005 197 0 197 5005 720 2942
perm-6 6 21 116280 1172 0 1172 116280 5040 43400
perm-7 7 28 3108105 8018 0 8018 3108105 40320 795188
perm-8 8 36 94143280 62814 0 62814 94143280 362880 17463696

threshold-4 4 8 56 20 0 20 56 104 128
threshold-5 5 16 8008 1348 0 1348 8008 1882 3882
threshold-6 6 32 3365856 353616 0 353616 3365856 94572 412736

resonance-4 4 15 3003 638 0 638 3003 370 940
resonance-5 5 31 736281 100091 0 100091 736281 11292 63862
resonance-6 6 63 553270671 ∗ 0 ∗ 553270671 1066044 14137242

crossplt-6 6 10 120 10 0 10 120 454 764
crossplt-7 7 12 495 15 0 15 495 1394 2972
crossplt-8 8 14 2002 21 0 21 2002 4246 11624
crossplt-9 9 16 8008 28 0 28 8008 12866 45638
crossplt-10 10 18 31824 36 0 36 31824 38854 179692
crossplt-11 11 20 125970 45 0 45 125970 117074 709044
crossplt-12 12 22 497420 55 0 55 497420 352246 2802584
crossplt-13 13 24 1961256 66 0 66 1961256 1058786 11092764

demicube-5 5 8 28 6 0 6 28 146 198
demicube-6 6 16 11440 460 0 460 11440 3756 9888
demicube-7 7 32 10518300 324640 0 324640 10518300 291558 1885298

Table 7.1
Description of the 42 considered arrangements; the ﬁrst column gives the problem names; the next two columns
specify the dimensions of V ∈ Rn×p; the 4th column gives the upper bound on the number of circuits of V , using remark
3.6(6) with r = n; by remark 3.6(3), it is also an upper bound on |Ss|/2 + |Sa|, where |Ss| (resp. |Sa|) is the number
of symmetric (resp. asymmetric) stem vectors (deﬁnition 3.5) of the arrangement A(V, τ ); |Ss|/2 and |Sa| are given in
columns 5 and 6; columns 7 and 8 give half the number of stem vectors of the arrangement A([V ; τ T], 0) and its upper
bound also derived from remark 3.6(6) with r = n for the linear arrangements and r = n + 1 for the others; the last
two columns give the number |S(V, τ )| of chambers of the arrangement A(V, τ ) and its upper bound given by (3.21) with
r = n for the linear arrangements and by (3.22) with r = n for the others; the symbol “∗” indicates that the stem vectors
of A(V, τ ) and A([V ; τ T], 0) could not be determined due to excessive computing time

PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 33

must hold.

7.2. Assessed algorithms. In the next section, the following algorithms have been evaluated on
the problem instances listed in the previous section. These algorithms are identiﬁed by the following
labels.
RC: the original RC algorithm [45].
P: the primal S-tree algorithm 4.1.
PD: the primal-dual S-tree algorithm 5.5.
D: the dual S-tree algorithm 5.2.
RCC: the compact version of the RC algorithm (see below).
PC: the compact primal S-tree algorithm 6.4.
PDC: the compact primal-dual S-tree algorithm 6.7.
DC: the compact version of the D algorithm (see below).
The algorithms P, PD, PC and PDC beneﬁt from the enhancements A (section 4.2.1), B (section 4.2.2)
and C (section 4.2.3). By want of space, the algorithms RC, RCC and DC have not been presented in
sections 4 and 6. Brieﬂy, algorithm RC is algorithm 4.2 (with its header 4.1) without its steps 4-8;
algorithm RCC is algorithm 6.5 (with its header 6.4) without its steps 5-7; algorithm DC is obtained
from algorithm 5.2 using the compaction principles described in section 6.
When used to solve the centered problems listed in the previous section, these algorithms do not
take advantage of the symmetry of the sign vector sets S(V, τ ) (proposition 3.2), so that it is really those
presented in section 7.3.1 that have been evaluated in the next section. Nevertheless, the algorithms
run faster by taking this symmetry into account, that is, by deciding from the start to compute only
half of the sign vectors (see [19, § 7.3.3]).

7.3. Numerical results. To evaluate the algorithms listed in the previous section, we have im-
plemented them in a Julia code named isf.jl [20], which extends the Matlab code isf.m [16, 15], from
linear to general aﬃne arrangements. The implementation has been done in Julia (version 1.8.5) on a
MacBookPro18,2/10cores (parallelism is not implemented however) with the system macOS Monterey,
version 12.6.1.
All the solvers, but D and DC, need to solve linear optimization problems (LOPs). The linear
optimization solver used in the Julia code is Gurobi. This one appears to be more eﬃcient than the
Matlab solver Linprog used in [16, 15]. Since the improvement is obtained by a reduction of the number
of LOPs, which are solved much faster in the Julia version, we observe a less important improvement
(wrt the RC algorithm) in computing time in the present study (Julia code) than reported in [18].
The main computational burden of the “pure primal” variants P and PC is the solution of the
LOPs while, for the “pure dual” variants D and DC, it is the computation of the stem vectors and their
use in the covering tests. These are not comparable. Therefore, counting the number of LOPs or the
number of covering tests is not a relevant criterion for comparing the solvers. For this reason, we rely
on computing time. Since the RC algorithm was shown in [45] to have better performance in time than
earlier methods, a comparison is often made with the RC algorithm. Since this algorithm is implemented
in Python, we avoid biases due to the programming language by making the comparison with our Julia
version of the RC algorithm, which can be easily simulated from algorithm 4.1, as mentioned above.
For ease of reading, the comparison of the solvers’ eﬃciency is carried out by using performance
proﬁles [13] (tables with precise numbers are also given in the appendix of [15]): these are curves in
a graph with the relative eﬃciency on the x-axis (sometimes in logarithmic scale) and a percentage
of problems on the y-axis. There is one graph per performance, which is the computing time in our
case, and there is one curve per solver in that graph: a point (e, f ) of the curve of a solver tells us
that the eﬃciency of this solver is never worse than e times that of the best solver (this one depends
on the considered problem) on a fraction f of the problems. As a result, the solver with the highest
curve, if any, can be legitimately considered as the most eﬃcient one, while the ranking of the other
solvers by the position of their curve in the graph should be taken with caution [27]. The performance

34 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

proﬁles only depend on the relative performance of the solvers, that is, for a particular problem, their
performance divided by the one of the best solver for that problem. Therefore, taking the computing
time or the computing time per chamber as performance yield the same performance proﬁles.

7.3.1. Standard solvers. Let us ﬁrst compare the standard solvers RC, P, PD and D with each
other, on the selected arrangements described in table 7.1. The comparison is made on the computing
times reported in table A.1 and the associated performance proﬁles are given in ﬁgure 7.1.

Fig. 7.1. Performance proﬁles of the RC, P, PD and D algorithms, for the computing time

One observes that the PD algorithm is generally the most eﬃcient one when the computing time is
taken as a reference (it has the “highest” curve in ﬁgure 7.1). The speedup with respect to the RC algo-
rithm can reach 14.74: this can be observed in table A.1 (PD algorithm on the instance resonance-5)
or on ﬁgure 7.1 (by the abscissa of the rightmost change in the curve of the RC algorithm, whose relative
performance is there given relatively to the PD algorithm).

7.3.2. Compact solvers. To show the interest of the compact versions of the algorithms, intro-
duced in section 6, we compare each solver RC, P, PD and D to its compact version RCC, PC, PDC
and DC. The computing times are given in table A.2 and the performance proﬁles are shown in ﬁg-
ure 7.2. Recall that, by construction of the compact versions, the improvement ratios are bounded
above by 2, approximately.
We observe indeed on table A.2 that the compact versions generally improve their standard version
on the computing time, particularly for the PDC solver, for which the mean (resp. median) improvement
is 1.51 (resp. 1.50). The improvement bound 2 is obtained by DC on the instances perm-7, resonance-5
and demicube-7. This improvement can also be observed on ﬁgure 7.2, with more ambiguity, since it
is not indicated which algorithm is the best for each problem instance (for example the x-axis larger
than 2 for the performance proﬁles D vs. DC is not due to a performance of DC that is 2.27 times better
than D on some problem, but the opposite: it is D that is 2.27 times faster than DC on some problem).
Nevertheless, algorithm AC generally outperforms algorithm A when A = RC, P or PD (their curve is
higher).
The performance proﬁles of ﬁgure 7.3 compares the most eﬀective solver, namely PDC, to the RC
solver. The former shows a speedup that can reach 22.87 (see table A.2, RC/PDC column).
For a comparison between the compact algorithms and the algorithms only generating half of
S(V, τ ) = S(V, 0) for the centered instances, see [19].

8. Conclusion. This paper deals with the enumeration of the chambers of a hyperplane arrange-
ment. It brings improvements to a recursive algorithm proposed by Rada and ˇCern´y, and proposes a
family of new algorithms having, to various extents, dual aspects based on the Motzkin alternative,

PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 35

 Fig. 7.2. Performance proﬁles of the RC vs. RCC, P vs. PC, PD vs. PDC and D vs. DC algorithms, for the computing
time; the dashed lines refer to the compact versions of the algorithms

matroid circuits and the introduced notion of stem vector. Most algorithms are grounded on a tree of
sign vectors, whose leaves are in a one-to-one correspondence with the chambers of the arrangement.
Compact versions of the algorithms are also presented, which aim at reducing the size of the sign vector
tree, in order to avoid duplicating costly identical operations like solving linear optimization problems
and covering tests. The most eﬃcient method of this algorithm anthology is the one that includes
primal and dual ingredients, and uses the compact form of the tree, which has been named PDC in the
paper. The speedup it provides, with respect to Rada- ˇCern´y’s algorithm, much depends on the features
of the considered arrangement, in particular its dimensions, and ranges between 1.72 and 22.87, with
a mean value of 9.10.
These algorithms are grounded on a theory that is presented before their introduction. This one
includes the structure of the sign vector sets and the stem vector sets, in particular conditions for their
symmetry, their connectivity, their full cardinality and much more.
Numerous aspects of the presented algorithms can be further improved or developed, covering both
conceptual and implementation aspects. Let us mention a few topics. (i) The linear optimization
problems could be solved approximately, hence saving computation time when the tested sign vector
is feasible. (ii) The way stem vectors are computed, stored and used could be improved, with speciﬁc
structures designed for that purpose. (iii) In case the arrangements present combinatorial symmetries,
the approaches presented in [47, 8] should increase signiﬁcantly the algorithm performances. (iv) The
proposed approaches could be extended to compute the chambers of the hyperplane arrangement and
subarrangements, those recursively included in the hyperplane intersections of any smaller dimension.

36 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

Fig. 7.3. Performance proﬁles of the RC vs. PDC solvers, for the computing time

Appendix A. Tables with numerical results.
This appendix gives the tables with the detailed numerical results, comparing the solvers selected
in section 7.2, on which the performance proﬁles of ﬁgures 7.1, 7.2 and 7.3 are based. Comments on
these results can be found in section 7.3. Table A.1 deals with the standard algorithms and table A.2
is related to the compact versions of these algorithms.

Acknowledgments. We thank Miroslav Rada and Michal ˇCern´y for providing us with their code
and problem instances, presented in [45].

Funding. The ﬁrst author’s research was partially supported by NSERC grant OGP0005491. The
third author was partially supported by a Mitacs-Inria grant.

REFERENCES

[1] M. Aguiar and S. Mahajan, Topics in Hyperplane Arrangements, no. 226 in Mathematical Surveys and Mono-
graphs, American Mathematical Society, Providence, RI, 2017. [doi].
[2] K. Aomoto and M. Kita, Theory of Hypergeometric Functions, Springer Monographs in Mathematicss, Springer-
Verlag, Tokyo, 2011. [doi].
[3] C. Athanasiadis, Characteristic polynomials of subspace arrangements and ﬁnite ﬁelds, Advances in Mathematics,
122 (1996), pp. 193–233. [doi].
[4] D. Avis and K. Fukuda, A pivoting algorithm for convex hulls and vertex enumeration of arrangements and
polyhedra, Discrete & Computational Geometry, 8 (1992), pp. 295–313. [doi].
[5] H. Bieri and W. Nef, A recursive sweep-plane algorithm, determining all cells of a ﬁnite division of Rd, Computing,
28 (1982), pp. 189–198. [doi].
[6] J. Bonnans, J. Gilbert, C. Lemar´echal, and C. Sagastiz´abal, Numerical Optimization – Theoretical and
Practical Aspects (second edition), Universitext, Springer Verlag, Berlin, 2006. [authors] [editor] [doi].
[7] M.-C. Brandenburg, J. De Loera, and C. Meroni, The best ways to slice a polytope, Mathematics of Computa-
tion, 94 (2025), pp. 1003–1042. [doi].
[8] T. Brysiewicz, H. Eble, and L. K¨uhne, Enumerating chambers of hyperplane arrangements with symmetry,
Preprint 14, Max-Planck-Institut f¨ur Mathematik in den Naturwissenschaften, Leipzig, 2021.
[9] T. Brysiewicz, H. Eble, and L. K¨uhne, Computing characteristic polynomials of hyperplane arrangements with
symmetries, Discrete & Computational Geometry, 70 (2023), pp. 1356–1377. [doi].
[10] R. Buck, Partition of space, American Mathematical Monthly, 50 (1943), pp. 541–544. [doi].
[11] V. Chv´atal, Linear Programming, W.H. Freeman and Company, New York, 1983.
[12] A. Deza and L. Pournin, A linear optimization oracle for zonotope computation, Computational Geometry:
Theory and Applications, 100 (2022). [doi].
[13] E. Dolan and J. Mor´e, Benchmarking optimization software with performance proﬁles, Mathematical Program-
ming, 91 (2002), pp. 201–213. [doi].
[14] G. D´osa, I. Szalkai, and C. Laflamme, The maximum and minimum number of circuits and bases of matroids,
Pure Mathematics and Applications, 15 (2006), pp. 383–392.

PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 37

[15] J.-P. Dussault, J. Gilbert, and B. Plaquevent-Jourdain, ISF and BDIFFMIN – Pieces of software uploaded
on SoftwareHeritage, 2023. [hal-04124994].
[16] J.-P. Dussault, J. Gilbert, and B. Plaquevent-Jourdain, ISF and BDIFFMIN - Matlab functions for central
hyperplane arrangements and the computation of the B-diﬀerential of the componentwise minimum of two
aﬃne vector functions, tech. report, 2023. [hal-04102933] [github].
[17] J.-P. Dussault, J. Gilbert, and B. Plaquevent-Jourdain, On the B-diﬀerential of the componentwise minimum
of two aﬃne vector functions – The full report, research report, 2024. [hal-03872711].
[18] J.-P. Dussault, J. Gilbert, and B. Plaquevent-Jourdain, On the B-diﬀerential of the componentwise minimum
of two aﬃne vector functions, Mathematical Programming Computation, 17 (2025), pp. 1–52. [hal-04048393]
[doi] [view-only].
[19] J.-P. Dussault, J. Gilbert, and B. Plaquevent-Jourdain, Primal and dual approaches for the chamber enu-
meration of real hyperplane arrangements – The full report, research report, 2025. [hal-05002239v2].
[20] J.-P. Dussault, J. Gilbert, and B. Plaquevent-Jourdain, IncSignFeas.jl (isf): Julia functions for the enumer-
ation of the chambers of hyperplane arrangements, (2025). [hal-05238721].
[21] H. Edelsbrunner, Algorithms in Combinatorial Geometry, vol. 10 of EATCS Monographs on Theoretical Computer
Science, Springer-Verlag, Berlin, 1987. [doi].
[22] H. Edelsbrunner, J. O’Rourke, and R. Seidel, Constructing arrangements of lines and hyperplanes with appli-
cations, SIAM Journal on Control, 15 (1986), pp. 341–363. [doi].
[23] C. Fevola, G. Pimentel, A.-L. Sattelberger, and T. Westerdijk, Algebraic approaches to cosmological inte-
grals, Le Matematiche, 80 (2025), pp. 303–324. [doi] [pdf].
[24] S. Forcey, Book review: “Topics in Hyperplane Arrangements by Marcelo Aguiar and Swapneel Mahajan”, Bulletin
of the American Mathematical Society, 56 (2019), pp. 367–372. [doi].
[25] J. Gilbert, Fragments d’Optimisation Diﬀ´erentiable – Th´eorie et Algorithmes, Lecture Notes (in French) of courses
given at ENSTA and at Paris-Saclay University, Saclay, France, 2021. [hal-03347060].
[26] P. Gordan, ¨Uber die Auﬂ¨osung linearer Gleichungen mit reelen Coeﬃcienten, Mathematische Annalen, 6 (1873),
pp. 23–28.
[27] N. Gould and J. Scott, A note on performance proﬁles for benchmarking software, ACM Transactions on Math-
ematical Software, 43 (2016). [doi].
[28] D. R. Grayson and M. E. Stillman, Macaulay2, a software system for research in algebraic geometry. Available
at http://www2.macaulay2.com.
[29] B. Gr¨unbaum, Convex polytopes. With the cooperation of Victor Klee, M.A. Perles and G.C. Shephard, no. 16 in
Pure and Applied Mathematics, Interscience Publishers John Wiley & Sons, New York, 1967.
[30] B. Gr¨unbaum, Arrangements and Spreads, no. 10 in Conference Board of the Mathematical Sciences Regional
Conference Series in Mathematics, AMS, Providence, RI, 1972.
[31] J. Gu and R. Koenker, Nonparametric maximum likelihood methods for binary response models with random
coeﬃcients, Journal of the American Statistical Association, 117 (2022), pp. 732–751. [doi].
[32] O. G¨uler, Foundations of Optimization, no. 258 in Graduate Texts in Mathematics, Springer, 2010. [doi].
[33] D. Halperin and M. Sharir, Arrangements, in Handbook of Discrete and Computational Geometry (third edition),
J. Goodman, J. O’Rourke, and C. T´oth, eds., Discrete Mathematics its Applications, CRC Press - Taylor &
Francis Group, 2018, pp. 723–762.
[34] J.-B. Hiriart-Urruty and C. Lemar´echal, Fundamentals of Convex Analysis, Grundlehren Text Editions,
Springer, Berlin, 2001. [doi].
[35] L. Kastner and M. Panizzut, Hyperplane arrangements in polymake, tech. report, 2020. [arXiv:2003.w13548].
[36] L. K¨uhne, The universality of the resonance arrangement and its Betti numbers, tech. report, 2023. [doi].
[37] T. Motzkin, Beitr¨age zur Theorie der linearen Ungleichungen. University Basel Dissertation, Jerusalem, Israel,
1936.
[38] P. Orlik and L. Solomon, Combinatorics and topology of complements of hyperplanes, Inventiones Mathematicae,
56 (1980), pp. 167–189, https://doi.org/10.1007/BF01392549.
[39] P. Orlik and H. Terao, Arrangements of Hyperplanes, no. 300 in Grundlehren der mathematischen Wis-
senschaften, Springer, 1992.
[40] Oscar, Open source computer algebra research system, version 0.15.0-dev, 2024. https://www.oscar-system.org.
[41] J. Oxley, Matroid theory (second edition), no. 21 in Oxford Graduate Texts in Mathematics, Oxford University
Press, Oxford, 2011. [doi].
[42] A. Pfister and A.-L. Sattelberger, Diﬀerential equations for moving hyperplane arrangements, Le Matematiche,
80 (2025), pp. 409–429. [doi] [pdf].
[43] B. Plaquevent-Jourdain, Robust Methods for Complementarity Problems - A Detour Through Hyperplane Ar-
rangements, PhD thesis, Sorbonne Universit´e (ED 386), Paris, France; Universit´e de Sherbrooke, Sherbrooke,
Qu´ebec, Canada, 2025. [tel-05253903].
[44] A. Postnikov and R. Stanley, Deformations of Coxeter hyperplane arrangements, Journal of Combinatorial
Theory – Series A, 91 (2000), pp. 544–597. [doi].
[45] M. Rada and M. ˇCern´y, A new algorithm for enumeration of cells of hyperplane arrangements and a comparison
with Avis and Fukuda’s reverse search, SIAM Journal on Discrete Mathematics, 32 (2018), pp. 455–473. [doi].
[46] J. Rambau, Topcom: Triangulations of point conﬁgurations and oriented matroids, in Proceedings of the Interna-
tional Congress of Mathematical Software, 2002. http://www.zib.de/PaperWeb/abstracts/ZR-02-17.

38 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

[47] J. Rambau, Symmetric lexicographic subset reverse search for the enumeration of circuits, cocircuits, and triangu-
lations up to symmetry, Draft 2, 2023.
[48] S. Roberts, On the ﬁgures formed by the intercepts of a system of straight lines in a plane, and on analogous
relations in space of three dimensions, Proc. London Math. Soc., 19 (1888), pp. 405–422. [doi].
[49] R. Rockafellar, Convex Analysis, no. 28 in Princeton Mathematics Ser., Princeton University Press, Princeton,
New Jersey, 1970.
[50] R. Saigal, Linear Programming – A Modern Integrated Analysis, Kluwer Academic Publisher, Boston, 1995.
[51] L. Schl¨afli, Theorie der vielfachen Kontinuit¨at (in German), in Gesammelte mathematische Abhandlugen, Band
1, Springer, Basel, 1950, pp. 168–387. [doi].
[52] N. Sleumer, Output-sensitive cell enumeration in hyperplane arrangements, in Algorithm theory-SWAT’98 (Stock-
holm), no. 1432 in Lecture Notes in Comput. Sci., Springer, Berlin, 1998, pp. 300–309. [doi].
[53] R. Stanley, An introduction to hyperplane arrangements, in Geometric Combinatorics, E. Miller, V. Reiner, and
B. Sturmfels, eds., vol. 13 of IAS/Park City Mathematics Series, 2007, pp. 389–496. [doi].
[54] J. Steiner, Einige Gesetze ¨uber die Theilung der Ebene und des Raumes, Journal f¨ur die Reine und Angewandte
Mathematik, 1 (1826), pp. 349–364. [doi].
[55] The Sage Developers, SageMath, the Sage Mathematics Software System, 2023. https://www.sagemath.org.
[56] M. L. Vergnas, Matro¨ıdes orientables, C. R. Acad. Sci. Paris, S´erie A-B, 280 (1975), pp. A61–A64.
[57] W. Wenzel, N. Ay, and F. Pasemann, Hyperplane arrangements separating arbitrary vertex classes in n-cubes,
Acta Applicandae Mathematicae, 25 (2000), pp. 284–306. [doi].
[58] R. Winder, Partitions of N-space by hyperplanes, SIAM Journal on Applied Mathematics, 14 (1966), pp. 811–818.
[doi].
[59] T. Zaslavsky, Facing up to Arrangements: Face-Count Formulas for Partitions of Space by Hyperplanes, Memoirs
of the American Mathematical Society, Volume 1, Issue 1, Number 154 (1975). [doi].
[60] G. Ziegler, Lectures on Polytopes, no. 152 in Graduate Texts in Mathematics, Springer Verlag, New York, 1995.

PRIMAL AND DUAL APPROACHES FOR HYPERPLANE ARRANGEMENTS 39

RC P PD D
Problems time time RC/P time RC/PD time RC/D

rand-5-10 0.77 0.41 1.86 0.44 1.77 0.27 2.83
rand-4-11 0.92 0.57 1.61 0.57 1.63 0.33 2.77
rand-6-12 3.06 1.90 1.62 1.98 1.54 1.22 2.52
rand-5-13 3.78 2.19 1.72 2.10 1.80 1.47 2.58
rand-7-14 13.03 7.54 1.73 8.18 1.59 5.38 2.42
rand-7-15 21.73 12.96 1.68 14.02 1.55 11.76 1.85
rand-8-16 49.56 29.89 1.66 32.91 1.51 31.68 1.56
rand-9-17 108.98 66.71 1.63 77.29 1.41 78.34 1.39

srand-8-20-2 59.84 17.11 3.50 9.53 6.28 26.70 2.24
srand-8-20-4 336.51 178.63 1.88 204.83 1.64 1072.47 0.31
srand-8-20-6 395.54 221.02 1.79 287.96 1.37 1153.47 0.34

2d-5-20 6.14 2.75 2.24 1.31 4.68 1.98 3.10
2d-6-20 10.19 4.88 2.09 2.25 4.53 3.35 3.05
2d-7-20 17.12 7.72 2.22 3.41 5.02 5.78 2.96
2d-8-20 29.61 13.27 2.23 6.15 4.81 9.11 3.25

ratio-5-20-7 35.74 20.19 1.77 18.55 1.93 42.24 0.85
ratio-5-20-9 27.43 18.93 1.45 13.78 1.99 24.97 1.10
ratio-6-20-7 129.74 72.83 1.78 84.99 1.53 205.06 0.63
ratio-6-20-9 104.57 70.26 1.49 68.38 1.53 176.81 0.59
ratio-7-20-7 242.07 175.11 1.38 197.37 1.23 547.52 0.44
ratio-7-20-9 254.94 159.50 1.60 203.40 1.25 572.61 0.45

perm-5 1.88 0.78 2.40 0.26 7.08 0.81 2.33
perm-6 17.00 5.19 3.27 1.72 9.91 7.32 2.32
perm-7 168.28 40.10 4.20 13.08 12.87 131.85 1.28
perm-8 1846.22 356.08 5.18 126.72 14.57 3531.08 0.52

threshold-4 0.16 0.08 1.91 0.07 2.30 0.05 2.94
threshold-5 5.21 2.48 2.10 1.60 3.25 1.95 2.68
threshold-6 470.96 141.18 3.34 84.63 5.57 2789.56 0.17

resonance-4 1.15 0.33 3.51 0.09 12.11 0.40 2.90
resonance-5 71.41 13.67 5.23 4.85 14.74 151.63 0.47
resonance-6 13280.92 1768.95 7.51 1949.89 6.81 ∞ 0.00

crossplt-6 0.61 0.21 2.90 0.06 9.78 0.28 2.21
crossplt-7 2.07 0.55 3.75 0.21 9.93 0.80 2.60
crossplt-8 6.74 1.60 4.22 0.71 9.56 2.66 2.54
crossplt-9 21.54 4.56 4.72 2.18 9.89 8.48 2.54
crossplt-10 66.43 12.62 5.26 6.61 10.05 27.11 2.45
crossplt-11 205.28 34.66 5.92 20.15 10.19 86.08 2.38
crossplt-12 633.94 94.78 6.69 61.17 10.36 271.62 2.33
crossplt-13 2024.43 275.18 7.36 199.72 10.14 862.09 2.35

demicube-5 0.18 0.05 3.69 0.01 12.89 0.07 2.57
demicube-6 9.55 3.67 2.60 1.97 4.85 3.66 2.61
demicube-7 1446.10 397.24 3.64 275.51 5.25 8800.60 0.16

Mean 3.06 5.78 1.85
Median 2.24 4.83 2.33

Table A.1
Computing times (in seconds) for the standard algorithms listed in section 7.2; for each algorithm A := P, PD or D,
the column labeled “RC/A” gives the time(RC)/time(A) ratio; the sign “∞” means that the instance was not solvable in
a reasonable amount of time; for each instance, the number in bold indicates the most eﬃcient code

40 J.-P. DUSSAULT, J.CH. GILBERT, B. PLAQUEVENT-JOURDAIN

RCC PC PDC DC
Problems time RC/RCC time P/PC RC/PC time PD/PDC RC/PDC time D/DC RC/DC

rand-5-10 0.55 1.41 0.34 1.23 2.28 0.35 1.26 2.22 0.24 1.15 3.26
rand-4-11 0.78 1.18 0.48 1.18 1.91 0.44 1.28 2.08 0.32 1.04 2.88
rand-6-12 2.13 1.44 1.36 1.39 2.25 1.33 1.49 2.30 1.00 1.22 3.07
rand-5-13 3.08 1.22 1.90 1.15 1.99 1.65 1.27 2.30 1.34 1.09 2.81
rand-7-14 8.44 1.54 5.34 1.41 2.44 5.43 1.51 2.40 4.39 1.22 2.96
rand-7-15 15.72 1.38 9.73 1.33 2.23 9.48 1.48 2.29 10.08 1.17 2.16
rand-8-16 33.64 1.47 20.60 1.45 2.41 21.30 1.54 2.33 19.63 1.61 2.52
rand-9-17 70.40 1.55 44.31 1.51 2.46 47.77 1.62 2.28 50.46 1.55 2.16

srand-8-20-2 52.01 1.15 16.13 1.06 3.71 7.46 1.28 8.02 23.16 1.15 2.58
srand-8-20-4 268.80 1.25 138.23 1.29 2.43 142.14 1.44 2.37 609.39 1.76 0.55
srand-8-20-6 306.79 1.29 161.72 1.37 2.45 183.17 1.57 2.16 875.37 1.32 0.45

2d-5-20 6.11 1.01 3.30 0.83 1.86 1.45 0.91 4.23 2.90 0.68 2.12
2d-6-20 10.11 1.01 5.62 0.87 1.81 2.25 1.00 4.53 4.71 0.71 2.16
2d-7-20 16.96 1.01 8.82 0.88 1.94 3.48 0.98 4.92 7.91 0.73 2.16
2d-8-20 29.35 1.01 16.73 0.79 1.77 6.76 0.91 4.38 12.51 0.73 2.37

ratio-5-20-7 33.66 1.06 18.40 1.10 1.94 14.73 1.26 2.43 96.88 0.44 0.37
ratio-5-20-9 23.55 1.16 16.38 1.16 1.67 10.00 1.38 2.74 24.87 1.00 1.10
ratio-6-20-7 112.70 1.15 65.69 1.11 1.97 58.17 1.46 2.23 216.23 0.95 0.60
ratio-6-20-9 107.79 0.97 60.75 1.16 1.72 50.83 1.35 2.06 205.07 0.86 0.51
ratio-7-20-7 207.24 1.17 148.76 1.18 1.63 140.43 1.41 1.72 648.28 0.84 0.37
ratio-7-20-9 213.10 1.20 138.95 1.15 1.83 145.71 1.40 1.75 722.24 0.79 0.35

perm-5 1.79 1.05 0.71 1.10 2.63 0.17 1.52 10.78 0.62 1.30 3.02
perm-6 15.94 1.07 4.84 1.07 3.51 1.00 1.71 16.98 5.70 1.28 2.98
perm-7 161.40 1.04 38.25 1.05 4.40 7.53 1.74 22.34 65.81 2.00 2.56
perm-8 1841.24 1.00 341.56 1.04 5.41 77.46 1.64 23.84 1876.56 1.88 0.98

threshold-4 0.10 1.49 0.06 1.26 2.41 0.04 1.78 4.09 0.04 1.26 3.69
threshold-5 4.47 1.17 1.96 1.26 2.65 0.86 1.86 6.03 1.52 1.28 3.44
threshold-6 457.37 1.03 131.09 1.08 3.59 58.63 1.44 8.03 1672.58 1.67 0.28

resonance-4 1.07 1.07 0.30 1.10 3.85 0.09 1.04 12.63 0.33 1.21 3.51
resonance-5 68.90 1.04 12.68 1.08 5.63 3.12 1.55 22.87 75.40 2.01 0.95
resonance-6 13029.76 1.02 1580.98 1.12 8.40 1322.73 1.47 10.04 ∞ — 0.00

crossplt-6 0.45 1.35 0.15 1.37 3.99 0.04 1.74 17.02 0.19 1.45 3.20
crossplt-7 1.49 1.40 0.49 1.12 4.20 0.11 1.84 18.29 0.62 1.28 3.32
crossplt-8 4.87 1.39 1.40 1.14 4.80 0.39 1.81 17.33 2.11 1.26 3.20
crossplt-9 15.71 1.37 3.92 1.16 5.50 1.15 1.90 18.78 6.88 1.23 3.13
crossplt-10 49.32 1.35 10.74 1.17 6.18 3.40 1.95 19.55 21.71 1.25 3.06
crossplt-11 153.09 1.34 28.15 1.23 7.29 10.39 1.94 19.76 69.40 1.24 2.96
crossplt-12 477.79 1.33 76.21 1.24 8.32 32.03 1.91 19.79 224.67 1.21 2.82
crossplt-13 1510.30 1.34 209.32 1.31 9.67 105.22 1.90 19.24 709.71 1.21 2.85

demicube-5 0.11 1.55 0.05 1.07 3.94 0.01 1.19 15.34 0.06 1.24 3.19
demicube-6 7.72 1.24 2.99 1.23 3.19 1.10 1.79 8.68 2.80 1.31 3.41
demicube-7 1364.33 1.06 326.89 1.22 4.42 161.08 1.71 8.98 4421.79 1.99 0.33

Mean 1.22 1.17 3.54 1.51 9.10 1.23 2.15
Median 1.19 1.16 2.54 1.50 5.47 1.23 2.57

Table A.2
Computing times (in seconds) for the compact algorithms listed in section 7.2; for each algorithm A = RC, P, PD,
or D, the columns labeled “A/AC” (resp. “RC/AC”) give the ratios time(A)/time(AC) (resp. time(RC)/time(AC)); the
ratios time(A)/time(AC) are approximately upper bounded by 2; the sign “∞” means that the instance was not solvable
in a reasonable amount of time; for each instance, the number in bold indicates the most eﬃcient code, i.e., the one with
the highest ratios time(RC)/time(AC)
