<!-- source: https://arxiv.org/pdf/2103.06203 | converted from PDF -->

arXiv:2103.06203v2  [math.NT]  18 Oct 2022
THE RELATIVE BOGOMOLOV CONJECTURE FOR FIBERED
PRODUCTS OF ELLIPTIC CURVES

LARS K ¨UHNE

Abstract. We deduce an analogue of the Bogomolov conjecture for non-
degenerate subvarieties in ﬁbered products of families of elliptic curves from
the author’s recent theorem on equidistribution in families of abelian varieties.
This generalizes results of DeMarco and Mavraki and improves certain results
of Manin-Mumford type proven by Masser and Zannier to results of Bogomolov
type, yielding the ﬁrst results of this type for subvarieties of relative dimension
> 1 in families of abelian varieties with trivial trace.

In a previous article [20], the author has established an analogue of the equidis-
tribution conjecture for degenerate subvarieties in families of abelian varieties and
deduced uniform versions of the Manin-Mumford and the Bogomolov conjecture
for algebraic curves embedded in their Jacobian. In this article, we discuss an-
other application of the same equidistribution result [20, Theorem 1], which has
been the original motivation for the author’s work on equidistribution. It should
also be remarked that since the preprint [20] appeared, more general equidistri-
bution results have been obtained by Gauthier [16] as well as Yuan and Zhang
[34].
Pink has suggested a generalization [29, Conjecture 6.2] of the Manin-Mumford
conjecture for families of abelian varieties. The following conjecture is nothing
but the Bogomolov-type analogue of this conjecture, which was also proposed as
[11, Conjecture 1.2]. We also remark that it overlaps with a conjecture already
proposed in Zhang’s 1998 ICM talk [36, Section 4]. Throughout this article, the
subﬁeld K ⊂ Q ⊂ C is a number ﬁeld and S is an irreducible algebraic variety
over K. The variety S serves as the base of a family π : A ! S of abelian
varieties. Furthermore, we assume being given an immersion ι : A ֒! PN
K into
projective space and a Weil height hO(1) associated with the ample line bundle

2010 Mathematics Subject Classiﬁcation. 11G50 (primary), and 14K15, 14G40 (secondary).
The author was supported by an Ambizione Grant of the Swiss National Science Foundation
during the early stages of this project. He also received funding from the European Union
Horizon 2020 research and innovation programme under the Marie Sklodowska-Curie grant
agreement No. 101027237. 1

2 LARS K ¨UHNE

O(1) on PN
K.
1 For each closed point x ∈ A, we set

̂hι(x) = lim
k!∞
 (hO(1)(ι ◦ [n
k](x))
n2k
 ) .

As [n] preserves the proper ﬁbers of π, this is just the ordinary N´eron-Tate height
of x with respect to (the symmetric part of) the line bundle ι
∗O(1)|Aπ(x) on the
abelian variety Aπ(x).
Relative Bogomolov Conjecture (RBC). Let X be an irreducible sub-
variety X ⊂ A such that π(X) = S. Assume that X is not a subvariety of
codimension ≤ dim(S) in any horizontal torsion coset Y ⊂ A. Then, there
exists some ε(X) > 0 such that the set

{closed point x ∈ X | ̂hι(x) < ε(X)}

is not Zariski-dense.
The notion of horizontal torsion coset, which morally is the analogue of an
abelian subvariety translated by a torsion point, demands a formal deﬁnition:
Let S′ ! S be a generically ﬁnite map and τ : S′ ! AS′ a torsion section of
the base change πS′ : AS′ ! S′. For each subvariety X ⊆ AS′, we deﬁne its
translate X + τ to be the image of X ×S′ τ (S′) under the (ﬁberwise) addition
AS′ ×S′ AS′ ! AS′. An irreducible variety X ⊆ A is called a horizontal torsion
coset if there exists a generically ﬁnite map S′ ! S, an S′-ﬂat subgroup scheme
B ⊆ AS′, and a torsion section τ : S′ ! AS′ such that the translate B + τ ⊆ AS′
projects onto X.
It should be noted that (RBC) is independent of the chosen immersion ι :
A ֒! PN
K, which is not completely trivial as ̂hι appears in its statement. Let
ι, ι
′ : A ֒! PN
K be two projective immersions and write η for the generic point of S.
Then there exists a positive integer k such that both (ι
∗O(1)⊗k ⊗ (ι
′)∗O(1)⊗−1)|η
and (ι
∗O(1)⊗−1⊗(ι
′)∗O(1)⊗k)|η are ample. There exists thus an open dense subset
U ⊆ S such that both (ι
∗O(1)⊗k ⊗ (ι
′)∗O(1)⊗−1)|s and (ι
∗O(1)⊗−1 ⊗ (ι
′)∗O(1)⊗k)|s
are ample for all s ∈ U. Since ̂hι and ̂hι′ restrict to the usual N´eron-Tate heights
on ﬁbers, it follows that
 k−1 · ̂hι(x) ≤ ̂hι′(x) ≤ k · ̂hι(x)

for all closed points x ∈ π−1(U). As it clearly suﬃces to prove (RBC) for the
restriction X|U ⊆ A|U , this shows the independence of (RBC) from the chosen
immersion ι.
The main result of our article concerns (RBC), and is a generalization of [9,
Theorem 1.4]. As usual, (RBC) implies Manin-Mumford type results in the
same relative settings. It has been already mentioned that the Manin-Mumford
analogue of (RBC) was proposed by Pink [29, Conjecture 6.2]. For dim(X) = 1,
results related to Pink’s conjecture have been obtained by Masser and Zannier

1Not every family of abelian varieties π : A ! S admits a projective immersion even if
S does (compare [30, Chapter XII]), but we can always ﬁnd a proper closed subset Z ⊊ S
such that A \ π−1(Z) is quasi-projective (e.g. by spreading out from the generic point of
S), take an immersion ι : A \ π−1(Z) ֒! PN
K, and obtain again a canonical height function
̂hι : (A \ π−1(Z))(Q) ! R≥0. Theorem 1 still makes sense in this setting as (RBC) is invariant
under passing to Zariski-dense open subsets of S. In particular, the Manin-Mumford part of
the theorem holds for general families π : A ! S even without the existence of a projective
immersion.
 THE RELATIVE BOGOMOLOV CONJECTURE 3

[23], but no result of relative Manin-Mumford type seems to have been known
for subvarieties X ⊂ A of relative dimension > 1 up to now.
2 It should be
remarked that [9] uses the relative Manin-Mumford conjecture [22] in order to
prove (RBC). While this article was in preparation, DeMarco and Mavraki [8]
were able to remove this dependence and to generalize their previous work; an
essential new ingredient is the separation of holomorphic and anti-holomorphic
terms that is also used here (compare our Section 9 below with the ﬁrst step in
[8, Subsection 8.2]) and which has been ﬁrst introduced by Andr´e, Corvaja, and
Zannier (see [1, Subsection 5.2]). Our proof, which includes the case considered in
[9], also avoids a dependence on the relative Manin-Mumford conjecture so that
we obtain it instead as a genuine corollary in all cases under consideration. For
general curves X ⊂ A deﬁned over Q, the relative Manin-Mumford conjecture
has been proven recently by Masser and Zannier [24, Theorem 1.7].

Theorem 1. (RBC) is true if A is the ﬁbered product E1 ×S E2 ×S · · · ×S Eg of
families of elliptic curves Ei ! S (1 ≤ i ≤ g) over a base variety S.

The reader may note that we include the case of isotrivial families in the the-
orem. Furthermore, Theorem 1 immediately implies (RBC) in the slightly more
general situation that the ﬁber A|η over the generic point η of S is isogeneous to a
ﬁbered product of families of elliptic curves. The proof of Theorem 1 constitutes
the content of Sections 1 to 15. For further details on the structure of the proof,
we refer the reader to Section 4.
It is a reasonable ﬁrst guess that the equidistribution result [20, Theorem 1]
implies (RBC) in general just as the classical Bogomolov conjecture can be proven
by means of equidistribution. Unfortunately, the analogy with the classical case
leads one astray here. The Ullmo-Zhang approach [31, 35] to the Bogomolov
conjecture does not transfer well to the relative setting because the Faltings-
Zhang map

A
n −! A
n−1, (x1, x2, . . . , xn) ↦−! (x1 − x2, . . . , xn−1 − xn),

has only an S-ﬁbered analogue that is too weak for a reproduction of the argu-
ments used in [35, Section 4]. In short, we cannot subtract points in two diﬀerent
ﬁbers as there is no group structure on the total space. One can still subtract
points contained in the same ﬁber, and this gives rise to the uniform results
obtained in [12, 13, 20]. Here, we can prove our Theorem 1 by making use of
the additional product structure available on E1 ×S · · · ×S Eg, but our argument
deﬁnitely breaks down for generically simple families A ! S. Besides the au-
thor’s recent equidistribution result, essential tools for the proof of Theorem 1
are Andr´e’s theorem [2] on the normality of the monodromy group in admissible
variations of mixed Hodge structures and the Ax-Schanuel conjecture for mixed
Shimura varieties proven by Gao [15].
Finally, let us mention that by the argument given in [11], one can easily see
that (RBC) implies a uniform version of the Bogomolov conjecture for curves of
arbitrary genus g ≥ 2 whose Jacobian is a product of elliptic curves. In other
words, one can partially recover the author’s previous result [20, Theorem 2].
Likewise, the result of DeMarco, Krieger, and Ye [7], which answered a question

2While this article was in revision, Gao and Habegger have announced a general proof of
the relative Manin-Mumford conjecture.

4 LARS K ¨UHNE

of Bogomolov and Tschinkel [4], can be already deduced from the case of (RBC)
proven here. However, the results of [20] and their improvement by Yuan [33]
present substantially more general cases, in which (RBC) remains widely open.
Notation and conventions. Algebraic Geometry (General). Denote by k an
arbitrary ﬁeld. A k-variety is a reduced separated scheme of ﬁnite type over k.
By a subvariety of a k-variety we mean a reduced closed subscheme. A subvariety
is determined by its underlying topological space and we frequently identify both.
Furthermore, X sm denotes the smooth locus of X.
Generic sequences. Let X be an algebraic k-variety. If X is irreducible, we say
that a sequence (xi) ∈ X N of closed points is X-generic if none of its subsequences
is contained in a proper algebraic subvariety of X. Note that a sequence is X-
generic if and only if it converges to the generic point of X in the Zariski topology.
If the irreducible variety X can be inferred from context, we simply say generic
instead of X-generic.
Continuity and smoothness. We use C 0 as an abbreviation for continuous. For
any topological space X, C 0(X) denotes the real-valued continuous functions on
X and C 0
c (X) the real-valued continuous functions on X having compact support.
Analytiﬁcation. For a number ﬁeld K ⊂ C and a K-variety X, we write X(C)
for the complex analytic space associated with XC.
Complex spaces. Let M be a reduced complex (analytic) space (e.g., the
analytic space X(C) associated with a K-variety X). Recall that this means
that M is locally biholomorphic to a closed analytic subvariety V in a complex
domain U ⊂ Cn. A C ∞-form ω on M is a diﬀerential form on the smooth locus
M sm of M with the following extension property: M can be covered by local
charts V ⊂ U ⊂ Cn as above such that for each chart the diﬀerential form ω|V sm
is the restriction of a C ∞-diﬀerential form on U. There are also well-deﬁned
linear operators d, ∂, ∂ on the C ∞-diﬀerential forms on M. For each local chart
V ⊂ U ⊂ Cn, these are simply the restrictions of the operators of the same name
on Cn.
Moduli spaces of elliptic curves. We write Y (N) for the moduli stack over Q
parameterizing elliptic curves with level N structure ([26, Section 13.1]). This
is a smooth quasi-projective variety if N ≥ 3 ([19, Corollary 4.7.2]). For each
N ≥ 1, we write ξN : E(N) ! Y (N) for the universal family of elliptic curves
with level N structure.
Siegel upper half-space. We write Hg for the Siegel upper half-space of degree
g, considered as a complex manifold.

1. Setting-up the proof of Theorem 1

As in the statement of the theorem, let S be a base variety, let Ej ! S
(1 ≤ j ≤ g) be families of elliptic curves, and set

π : A = E1 ×S · · · ×S Eg ! S.

Furthermore, let X ⊆ A be a subvariety of dimension d, for which we want to
prove (RBC). We start by making some additional assumptions for the proof of
the theorem in Section 2 and introduce coordinates in Section 3. Following this,
we give an overview of the main argument in Section 4.

THE RELATIVE BOGOMOLOV CONJECTURE 5

2. Reductions

(i) In our proof, we suppose that the conclusion of (RBC) is false and show
that its main assumption cannot hold under this assumption. This means our
goal is to show that there exists a horizontal torsion coset Y ⊆ A such that X
is a subvariety of codimension ≤ dim(S) in Y . In the sequel, we can hence work
with an X-generic sequence (xi) ∈ X N such that ̂hι(xi) ! 0.

(ii) We can assume that g = d + 1. In fact, if

dim(A) − dim(S) = g < d + 1 = dim(X) + 1,

then codimA(X) < dim(S) + 1 so that the assumption of (RBC) is not satisﬁed.
If g > d + 1, we choose a projection

ϕ : A ! Ej1 × Ej2 × · · · × Ejd+1, 1 ≤ j1 < j2 < · · · < jd+1 ≤ g.

It clearly suﬃces to prove (RBC) for ϕ(X).
(iii0) We can also make the following assumption: For any ﬁbered product

π′ : A
′ = E′
1 ×S′ E′
2 ×S′ · · · ×S′ E′
g′ ! S′

of families of elliptic curves E′
j ! S′ (1 ≤ j ≤ g′ ≤ g) and any commutative
diagram

(1) A A
′

S S′

ϕ

π π′

with ϕ a ﬁberwise homomorphism, we have

(2) dim(ϕ(X)) ≥ dim(X) − (g − g′)

with equality if and only if dim(A) = dim(A
′).
In fact, the special case dim(A) = dim(A
′) is trivial as then ϕ is a ﬁberwise
isogeny and g = g′. Thus, we may suppose that there exist such π′ : A
′ ! S′

and ϕ : A ! A
′ with dim(A
′) < dim(A) and

(3) dim(ϕ(X)) ≤ dim(X) − (g − g′).

By an induction on dim(A), we can also assume that (RBC) is already proven
for the family π′ : A
′ ! S′. The sequence ϕ(xi) is ϕ(X)-generic and satisﬁes
̂hι′(ϕ(xi)) ! 0 for any immersion ι
′ : A
′ ֒! PN ′. Therefore ϕ(X) has to violate
the assumption in (RBC), which means that there exists a horizontal torsion
coset Y ′ ⊆ A
′ containing ϕ(X) and satisfying

dim(Y ′) − dim(ϕ(X)) ≤ dim(S′).

Using the inequality (3), we infer further that

dim(Y ′) − dim(X) + (g − g′) ≤ dim(S′).

The irreducible components of ϕ−1(Y ′) are horizontal torsion cosets. We can
pick such an irreducible component Y containing X and notice that

dim(Y ) ≤ dim(Y ′) + dim(S) − dim(S′) + (g − g′).

Combining the last two inequalities, we obtain

dim(Y ) − dim(X) ≤ dim(S).

6 LARS K ¨UHNE

This is a violation of the assumption in (RBC) for X ⊆ A, and thus there is
nothing left to prove.
(iii) Before continuing with our reductions, let us point out some consequences
of the previous assumption. For each 1 ≤ k ≤ g, we write

pr̂k : ∏g
j=1 Ej −! ∏g
j=1,j̸=k Ej

for the standard projection. The images pr̂k(X), 1 ≤ k ≤ g, have then all
dimension dim(X). In fact, we have a commutative square

A = ∏g
j=1 Ej ∏g
j=1,j̸=k Ej

S S

pr̂k

as in (1) above so that (2) implies

dim(pr̂k(X)) > dim(X) − 1.

and thus dim(pr̂k(X)) = dim(X).
A further consequence of the previous reduction is that X is non-degenerate.
In fact, if X were degenerate, then [14, Theorem 1.1 (i)] would produce a new
family π′ : A
′ ! S′ and a ﬁberwise homomorphism ϕ : A ։ A
′ ﬁlling a diagram
(1) but violating the constraint (2) on the dimension of ϕ(X).
Even more, all the images pr̂k(X), 1 ≤ k ≤ g, are non-degenerate as well.
Indeed, assume that this is not the case. Then, [14, Theorem 1.1 (i)] supplies a
commuting diagram

A = ∏g
j=1 Ej ∏g
j=1,j̸=k Ej ∏g′

j=1 E′
j

S S S′

pr̂k ϕ

with ﬁberwise homomorphisms along the upper row and such that

dim(ϕ(pr̂k(X))) < dim(pr̂k(X)) − (g − 1 − g′).

Using our assumption, we deduce conversely from (2) that

dim(ϕ(pr̂k(X))) > dim(X) − (g − g′).

A combination of these two inequalities yields

dim(pr̂k(X)) − (g − 1 − g′) ≥ dim(X) − (g − g′) + 2,

which is equivalent to the absurdity

dim(X) = dim(pr̂k(X)) ≥ dim(X) + 1.

This proves our claim about the non-degeneracy of pr̂k(X), 1 ≤ k ≤ g.
For the convenience of the reader, let us brieﬂy summarize the assumptions
that we can and do tacitly assume in the following:

(i) there exists an X-generic sequence (xi) ∈ X N such that ̂hι(xi) ! 0,
(ii) dim(A) − dim(S) = g = d + 1 = dim(X) + 1,
(iii) X is non-degenerate, and every projection pr̂k(X), 1 ≤ k ≤ g, is non-
degenerate and has dimension dim(X).

THE RELATIVE BOGOMOLOV CONJECTURE 7

We continue with imposing two further restrictions on the family π : A ! S.
(iv) First, we can assume without loss of generality that it is a subfamily of the
g-fold self-product of the universal family ξN : E(N) ! Y (N), N ≥ 3. There
exists a classifying map c : S ! Y (1)g (of algebraic stacks) such that

A E(1)g

S Y (1)g

ϕ

c

is a cartesian square, and we consider its pullback

A
′ = A ×S S′ E(N)g

S′ = S ×Y (1) Y (N) Y (N)g

ϕ′

c′

along Y (N) ! Y (1). As S′ ! S is ﬁnite, it clearly suﬃces to prove (RBC) for
the subvariety X ′ = X ×S S′ ⊆ A
′. Consider the induced subfamily π′ : ϕ′(A) !
c′(S). Assuming that (RBC) holds for this subfamily, we obtain as above that
there exists a horizontal torsion coset Y ′′ ⊆ ϕ′(A
′) with the property that

dim(Y ′′) − dim(ϕ′(X ′)) ≤ dim(c′(S′)).

The preimage Y ′ = (ϕ′)−1(Y ′′) is evidently a horizontal torsion coset of dimension
dim(Y ′′) + dim(S′) − dim(c(S′)) containing X, and furthermore

dim(Y ′) − dim(X ′) ≤ dim(Y ′′) + dim(S′) − dim(c′(S′)) − dim(ϕ′(X ′)) ≤ dim(S′)

this is again contradicting the assumption of (RBC) for X ′ ⊂ A
′ and hence also
for X ⊂ A. We can and do hence assume that A = E(N)g|S for some S ⊆ Y (N)g

where N ≥ 3 is ﬁxed once and for all in the sequel.
(v) Second, we can use our free choice of the immersion ι : A ֒! PN
K in the
statement of (RBC) to guarantee that

ι = (σ ◦ (ι0 × · · · × ι0))|S
where ι0 : E(N) ֒! PN0
K is an arbitrary projective immersion such that ι
∗
0O(1) is
ﬁberwise symmetric and σ : PN0
K × · · · × PN0
K ֒! PN
K is the Segre embedding.

3. Coverings and coordinates

We recall the following commutative diagram, whose horizontal rows are uni-
versal coverings:
 (C × H1)g E(N)g(C)

Hg
1 Y (N)g(C).

Γ = (Z
2 ⋊ Γ(N))g umixed

̃π ξN × · · · × ξN

Γ(N)g upure

The covering transformations of upure (resp. umixed) are given by the group Γ(N)g

(resp. (Z
2 ⋊ Γ(N))g) where

Γ(N) = {(a b
c d
) ∈ SL2(Z) ∣
∣
∣
∣
 (
a b
c d
) ≡ (1 0
0 1
) (mod N)}

8 LARS K ¨UHNE

acts on Z
2 through its standard representation. This identiﬁcation is such that
the group element
((m1
n1
 ) , (
a1 b1
c1 d1
) , . . . , (
mg
ng
 ) , (
ag bg
cg dg
)) ∈ (Z
2 ⋊ Γ(N))g

sends (z1, . . . , zg, τ1, . . . , τg) ∈ (C × H1)g to
(z1 + m1 + n1τ1
c1τ1 + d1 , . . . , zg + mg + ngτg
cgτg + dg , a1τ1 + b1
c1τ1 + d1 , . . . , agτg + bg
cgτg + dg
 )

(compare e.g. [3, Section 8.8]).
On the complex manifold (C × H1)g, we have the global holomorphic standard
coordinates zl, τl (1 ≤ l ≤ g) and their complex-conjugates zl, τ l. In addition,
we deﬁne 2g real-analytic functions

xl, yl : (C × H1)g −! R, 1 ≤ l ≤ g,

by demanding zl = xl + τlyl.
The preimage u
−1
pure(S) (resp. u
−1
mixed(X)) decomposes into irreducible analytic
components of dimension dim(S) (resp. dim(X)), on which the group Γ(N)g

(resp. (Z
2 ⋊ Γ(N))g) acts transitively. Due to the absence of elliptic ﬁxed points
on Y (N) (see e.g. [10, Exercise 2.3.7]), the map upure (resp. umixed) is ´etale and
these components coincide with the connected components of u
−1
pure(S) (resp.
u
−1
mixed(X)) in the euclidean topology. In the sequel, we keep ﬁxed an irreducible
component ̃X of X. Its image ̃S = ̃π( ̃X) is then an analytic component of the
preimage of S.
 4. Overview of the proof

For convenience of the reader, we brieﬂy expose the main lines of the argument
employed for the proof of Theorem 1 in the following sections. In Section 5,
we use the product structure and the equidistribution results of [20] to obtain
diﬀerential-geometric conditions on ̃X. These conditions appear as real-analytic
diﬀerential equations (9), which can be written down explicitly in local charts of
̃X and the local coordinates introduced in Section 3 above.
A natural way to exploit these is to use monodromy, to wit, the fact that the
stabilizer Stab( ̃X) ⊆ (Z
2 ⋊ Γ(N))g is rather large. This largeness follows by
Hodge-theoretic techniques, which are exposed in Sections 6 to 8. Besides rather
explicit computations, we make use of a theorem of Andr´e [2, Theorem 1] on the
normality of the algebraic monodromy group. Unfortunately, the equations (9)
are invariant under monodromy so that a direct application of monodromy fails;
this failure is not really surprising since the Betti form, which gives rise to these
equations, is invariant under monodromy.
To the rescue comes an important idea of Andr´e, Corvaja, and Zannier [1,
Subsection 5.2] that allows us to actually take advantage of the fact that the real-
analytic equations (9) contain both holomorphic and anti-holomorphic terms. In
short, we replace ̃X and (9) with ̃X × ̃X and a new set of real-analytic diﬀerential
equations (19). This is the content of Section 9.
Following a computation of the transformation behavior of (19) under mon-
odromy (Section 10) and a ﬁnal technical preparation in Section 11, we use

THE RELATIVE BOGOMOLOV CONJECTURE 9

explicit elements of the algebraic monodromy group to prove ﬁrst that – un-
der the assumptions of (RBC) – all factors are isogeneous (Sections 12 and 13).
With this at our disposal, we then deduce a linear equation (27) on ̃X in the
coordinates z1, . . . , zn. Gao’s mixed Ax-Schaunel theorem [15] enables us then
to conclude the proof of Theorem 1 (Section 15).

5. Equidistribution

Let us start with deﬁning the equilibrium measure. The (1, 1)-form

(4) i
Im(τj) (dzj − yjdτj) ∧ (dzj − yjdτ j)

on (C ×H1)g is (Z
2 ⋊ Γ(N))g-invariant (see [12, Lemma 2.6]) and hence descends
to a (1, 1)-form αj on A(C). We deﬁne the (1, 1)-form

β =
 g∑

j=1 αi

and consider its d-fold exterior power

(5) β∧d = d! ·
 g∑

j=1 α′
j, α′
j = α1 ∧ · · · ∧ αj−1 ∧ αj+1 ∧ · · · ∧ αg.

Up to multiplication with some (strictly) positive real number, this coincides with
the smooth closed (1, 1)-form on A(C) provided by [13, Lemma 2.6] (compare
also the proofs of [20, Lemmas 7 and 11]). By Theorem [20, Theorem 1] (and its
proof), there exists some kX > 0 such that

(6) 1
#O(xi)
 ∑

x∈O(xi) f (x) −! kX
 ∫

X(C) f β∧d, i ! ∞,

for every continuous function f ∈ C 0
c (X)(C). Note that each α′
j|X(C), 1 ≤ j ≤ g,
is non-zero as pr̂j(X) is non-degenerate by the reductions in Section 2 above.
For given integers n1, . . . , ng > 0, we consider the homomorphism

ϕ : E1 ×S · · · ×S Eg −! E1 ×S · · · ×S Eg, (x1, . . . , xg) ↦−! ([n1]x1, . . . , [ng]xg),

and set Y = ϕ(X). We claim that (ϕ∗β|Y )∧d is real-proportional to (β|X)∧d. As ϕ
is ´etale, there exists a non-empty open subset U ⊆ X(C) such that the restriction
ϕ|U : U ! ϕ(U) is a biholomorphism. Writing yi = ϕ(xi), the sequence (yi) is
Y -generic and satisﬁes ̂hι(yi) ! 0. By the above argument applied to Y instead
of X, we have hence

(7) 1
#O(yi)
 ∑

y∈O(yi) g(y) −! kY
 ∫

Y (C) gβ∧d, i ! ∞,

for every g ∈ C0
c (Y (C)). For any continuous function f ∈ C0
c (U), there exists a
(unique) continuous function g ∈ C0
c (ϕ(U)) such that f = g ◦ ϕ. As ϕ(O(xi)) =
O(yi), we have
 1
#O(xi)
 ∑

x∈O(xi) f (x) = 1
#O(yi)
 ∑

y∈O(yi) g(y)

10 LARS K ¨UHNE

in this situation. Hence the limits in (6) and (7) are equal, which means that

kX
 ∫
X(C) f β∧d = kY
 ∫
X(C) f (ϕ∗β)∧d

for any f ∈ C0
c (V ). Varying the test function f , we infer that kX(β|V )∧d =
kY (ϕ∗β|V )∧d. Since β has real-analytic coeﬃcients, this completes the proof of
the claim.
As ϕ∗αj = n
2
j αj, we have

ϕ∗α′
j = (∏

k∈{1,...,g},k̸=j n
2
k) · α′
j

for every j ∈ {1, . . . , g}. Thus, we have

(ϕ∗β|X(C))∧d = d! ·
 g∑

j=1(∏

k∈{1,...,g},k̸=j n
2
k) · α′
j|X(C)

and hence the (d, d)-forms

g∑

j=1 α′
j|X(C) and
 g∑

j=1(∏

k∈{1,...,g},k̸=j n
2
k) · α′
j|X(C)

are proportional by a positive real constant, which depends on n1, . . . , ng.
We claim that all (d, d)-forms α′
j|X(C), j ∈ {1, . . . , g}, are pairwise proportional
up to positive real constants. In fact, choosing for example n1 = n2 = · · · =
ng−1 = 1 and ng = 2 yields that

g∑

j=1 α′
j|X(C) and
 g−1∑

j=1 α′
j|X(C) + 1
4 · α′
g|X(C)

are proportional by a real positive constant. Rewriting this proportionality, we
obtain that g−1∑

j=1 α′
j|X(C) and α′
g|X(C)

are proportional by a positive real constant. (Note that the positivity of the
volume forms α′
j|X(C), 1 ≤ j ≤ g, is used here to ensure that these proportionality
factors are (strictly) positive.) This implies that also

g∑

j=1 α′
j|X(C) and α′
g|X(C)

are proportional by a positive real constant. We obtain similarly that each
α′
j|X(C), j ∈ {1, . . . , g − 1}, is proportional to ∑g
j=1 α′
j|X(C), whence our claim.
For later reference, let us choose reals r1, . . . , rg > 0 such that

r1α′
1|X(C) = r2α′
2|X(C) = · · · = rgα′
g|X(C).

This constitutes a diﬀerential-geometric restriction on the analytic subset
X(C) of E(N)(C). Pulling these back along umixed, we obtain similar restrictions
on ̃X ⊂ (C ⋊ H1)g. Let us spell these out in terms of a general local chart

χ : B1(0)d = {(w1, . . . , wd) ∈ Cd | max{|w1|, |w2|, . . . , |wd|} < 1} −! ̃X.

THE RELATIVE BOGOMOLOV CONJECTURE 11

For each function f on ̃X, we simply write f (resp. ∂f /∂wm, ∂f /∂wm) instead
of f ◦ χ (resp. ∂(f ◦ χ)/∂wm, ∂(f ◦ χ)/∂wm). With this notation, the (1, 1)-form
(χ ◦ umixed)∗αj, j ∈ {1, . . . , d}, on B1(0)d equals

i
Im(τj)
 ( d∑

m=1
 [ ∂zj
∂wm − Im(zj)
Im(τj) ∂τj
∂wm
 ] dwm
)
 ∧
 ( d∑

m=1
 [ ∂zj
∂wm − Im(zj)
Im(τj) ∂τj
∂wm
 ]
dwm
)
 .

Consequently, the (d, d)-form (χ ◦ umixed)∗α′
j, j ∈ {1, . . . , d}, on B1(0)d equals

(8) i
d
∏

k∈{1,...,g},k̸=j Im(τk) |det(Aj)|
2 w1 ∧ w1 ∧ · · · ∧ wd ∧ wd

with
 Aj = ( ∂zl
∂wm − Im(zl)
Im(τl) ∂τl
∂wm
 )

l∈{1,...,g},l̸=j
m∈{1,...,d} .

Therefore, the equality rjα′
j|X = rkα′
k|X, j, k ∈ {1, . . . , g}, implies

(9) rj(τj − τ j)3 det(Bj) det(Cj) = rk(τk − τ k)3 det(Bk) det(Ck)

on B1(0)d where we set

Bj = (
(τl − τ l) · ∂zl
∂wm − (zl − zl) · ∂τl
∂wm
 )
l∈{1,...,g},l̸=j
m∈{1,...,d} ,

and
 Cj = (
(τl − τ l) · ∂zl
∂wm − (zl − zl) · ∂τ l
∂wm
 )

l∈{1,...,g},l̸=j
m∈{1,...,d}
for each j ∈ {1, . . . , g}.

6. A variation of mixed Hodge structures on X(C)

In this section, we decorate the complex analytic space X(C) with a variation
of mixed Z-Hodge structures. We refer to [27, Subsection 14.4.1] for basic deﬁni-
tions concerning (admissible) variations of mixed Z-Hodge structures on complex
analytic spaces.
As a starting point, we endow the family E(N)(C) with a variation H ′ =
(VZ, F•, W•) of mixed Z-Hodge structures following Deligne [6, Section 10]: The
Z-modules

VZ,x = {(l, n) ∈ Lie(E(N)ξN(x))(C) × Z | expξN (x)(l) = [n](x)}

are naturally the stalks of a local system VZ on E(N)(C) having Z-rank 3.
Furthermore, the Lie group exponential yields an exact sequence

0 −! ξ∗
N(R1ξN,∗ZE(N)(C))∨ −! VZ −! ZE(N)(C) −! 0

of Z-local systems on E(N)(C). (We write ZE(N)(C) for the locally constant sheaf
with stalk Z on E(N)(C).) We use this to deﬁne the weight ﬁltration as

W0 = VZ, W−1 = ξ∗
N(R1ξN,∗ZE(N)(C))∨, W−2 = 0.

Writing V = VZ ⊗ OE(N)(C) for the associated holomorphic vector bundle, we
note that the stalk-wise projections VZ,x ! Lie(E(N)ξN(x))(C) extend to a map

φ : V ! ξ∗
NLie(E(N))(C)

12 LARS K ¨UHNE

of OE(N)(C)-sheaves where Lie(E(N))(C) is the sheaf on Y (N)(C) having stalks
Lie(E(N)x), x ∈ Y (N)(C). We use this to deﬁne the Hodge ﬁltration

F1 = 0, F0 = ker(φ), F−1 = V,

so that we obtain a mixed Hodge structure of type {(0, 0), (−1, 0), (0, −1)}.
The induced mixed Q-Hodge structure HQ = (VQ, F•, W•,Q) can also be de-
scribed in terms of Shimura theory. For this, we note that E(N)(C) is one of
the connected components of the mixed Shimura variety associated to the datum
(G
2
a,Q ⋊ GL2,Q, C × H1) where GL2,Q acts on G
2
a,Q via its standard representation
(compare [28, Chapter 10]) and the neat open compact subgroup

K(N) = {((m
n
 ) , (
a b
c d
)) ∈ ̂Z
2 × GL2(̂Z) ∣
∣
∣
∣
 (
a b
c d
) ≡ (
1 0
0 1
) (mod N)} ;

see [28, Section 0.6] for the deﬁnition of neatness in adelic groups and the proof
that K(N), N ≥ 3, is neat. The mixed Q-Hodge structure H ′
Q is then induced
in the standard way ([28, Propositions 1.7 and 1.10]) from the representation

(10) G
2
a,Q ⋊ GL2,Q = (GL2,Q G
2
a
0 1
 ) ֒! GL3,Q.

Writing pri : E(N)g ! E(N) for the projection to the i-th factor, we endow
E(N)g(C) with the variation H = ⊕g
j=1 pr∗
j H ′ of mixed Z-Hodge structures.
The base change HQ can again be interpreted in Shimura-theoretic terms as aris-
ing from the g-fold product of the representation in (10). This allows to invoke a
result of Wildeshaus [32, Theorem II.2.2] implying that H is an admissible vari-
ation of mixed Z-Hodge structures. Finally, the restriction H|X(C) is the desired
admissible variation of mixed Z-Hodge structures on X(C). (By deﬁnition (see
e.g. [27, Deﬁnition 14.49]), admissibility is trivially perserved by passing to ana-
lytic subvarieties.) In the following, we write H|X instead of H|X(C) to simplify
our notation. We also write Hx for the mixed Hodge structure associated with
a point x ∈ X(C).

7. The generic Mumford-Tate group of H|X

Write MT(H|X) for the generic Mumford-Tate group of H|X. It is clear
that MT(H|X) ⊆ (G
2
a,Q ⋊ GL2,Q)g – both from the explicit description and the
Shimura-theoretic formulation. There exists a countable union Z ⊆ X(C) of
proper analytic subvarieties such that MT(H|X) = MT(Hx) for all x ∈ X(C) \Z
and that, for all points x ∈ X(C), we have MT(Hx) ⊆ MT(H|X); we refer the
reader to [2, Section 4] or [25, Section 6] for details.
Analogous results are true for the generic Mumford-Tate group MT(H−1|X) ⊆
GL
g
2,Q of the variation H−1|X = W−1/W−2(H|X) of pure Z-Hodge structures
of weight −1. There is an evident surjective homomorphism MT(H|X) ։
MT(H−1|X ) between the generic Mumford-Tate groups; we hence determine
MT(H−1|X ) ﬁrst. Its structure is mostly related to the presence or absence
of generic isogenies between the factors of A = ∏g
j=1 Ej.
For this reason, we make a further assumption to simplify our notation: Write
η for the generic point of S. In the sequel, we may and do assume that there
exist integers i1 = 1 < i2 < · · · < ip+1 = g + 1

THE RELATIVE BOGOMOLOV CONJECTURE 13

such that the elliptic curves

Eiq,η, Eiq+1,η, . . . , Eiq+1−1,η

are isogeneous for each 1 ≤ q ≤ p, and the elliptic curves

Ei1,η, Ei2,η, . . . , Eip,η

are pairwise non-isogeneous. Set also gq = iq+1 − iq for each q ∈ {1, . . . , p}. For
the proof of Theorem 1, we can even assume that

Eiq,η = Eiq+1,η = · · · = Eiq+1−1,η

for each 1 ≤ q ≤ p. We also assume that there exists a p′ ∈ {0, . . . , p} such that
the families Ei1 ! S, Ei2 ! S, . . . , Eip′ ! S

are non-isotrivial, and the families

Eip′+1 ! S, Eip′+2 ! S, . . . , Eip ! S

are constant. (In particular, all families are constant if p′ = 0 and non-isotrivial
if p′ = p.) We set g′ = ip′+1 − 1 and Acst × S = Eg′+1 ×S · · · ×S Eg. For any
suﬃciently generic point s ∈ S(C) (i.e., s is not contained in a countable union
of proper analytic subvarieties of S(C)), the elliptic curves

Ei1,s, Ei2,s, . . . , Eip,s

are pairwise non-isogeneous and none of the curves

Ei1,s, Ei2,s, . . . , Eip′ ,s

has complex multiplication. Using [21, Theorems B.53 and B.72], we obtain for
every point x ∈ π−1(s) that

(11) MT(H−1,x) = Gm(∆g1(SL2,Q) × · · · × ∆gp′ (SL2,Q) × Hg(Acst)) ⊆ GL
g
2,Q

where ∆k : SL2,Q ! SLk
2,Q, k ∈ Z
>0, denotes the diagonal map and Hg(Acst)
is the Hodge group of Acst, which we do not need to determine here. As s is
suﬃciently generic, the subgroup in (11) equals the generic Mumford-Tate group
MT(H−1|X ).
For each x ∈ X, we let Ux denote the unipotent radical of MT(Hx). By [2,
Lemma 2.(c)], the sequence

1 Ux MT(Hx) MT(H−1,x) 1

is exact. We claim that dim(Ux) = 2g = 2 ∑p
q=1 gq for a suﬃciently general
x ∈ X(C). This leads immediately to
(12)

MT(Hx) = Gm
 p′
∏

q=1
 (
G
2gq
a,Q ⋊ SL2,Q) × (G
2(g−g′)
a,Q ⋊ Hg(Acst)) ⊆ (G
2
a,Q ⋊ GL2,Q)g

by comparing dimensions; here each copy of SL2 acts on the respective additive
group G
2gq
a,Q = G
2
a,Q×· · ·×G
2
a,Q diagonally on each factor G
2
a,Q. Similarly, Hg(Acst)

acts on G
2(g−g′)
a,Q but we do not need to specify this action further. Again, it follows
that the generic Mumford-Tate group MT(H|X) is the group in (12).

14 LARS K ¨UHNE

The remaining claim follows by applying [2, Proposition 1] for the mixed Hodge
structure Hx at a suﬃciently general point

(13) x = (x1, . . . , xg) ∈ X ⊂ E1 ×S · · · ×S Eg = A

such that the elliptic curves E(N)ξN(xiq ), 1 ≤ q ≤ p, are pairwise non-isogeneous.
We can freely assume that, as (13) varies, the generic rank of

(14) rankRq (Rqxiq + · · · + Rqxiq+1−1), Rq = End(E(N)ξN(xiq )),

equals iq+1 − iq = gq; for otherwise X would be contained in a proper horizontal
torsion coset of A, which contradicts the assumption made in the statement of
(RBC). This allows us to choose (13) further such that, for all q ∈ {1, . . . , p},
the rank in (14) is gq.
We invoke the said proposition from [2] for the 1-motive [u : Z
g ! Aπ(x)] where

u : (n1, n2, . . . , ng) ↦−! (n1x1, n2x2, . . . , ngxg).

The Zariski closure of u(Z
g) is Aπ(x) by our assumptions (14). Furthermore, we
have End(Aπ(x)) = Rg1×g1
1 × · · · × Rgp×gp
p .

so that

(15) HomEndQ(Aπ(x))(EndQ(Aπ(x)) · u(Z
g), H1(Aπ(x), Q))

=
 p∏

q=1 HomRq,Q(Rq,Q · uq(Z
gq), H1(Aπ(x), Q))

where uq : Z
gq ! Eiq × Eiq+1 × · · · × Eiq+1−1 = Egq
iq , 1 ≤ q ≤ p, is deﬁned by

uq(niq, niq+1, . . . , niq+1−1) = (niqxiq , niq+1xiq+1, . . . , niq+1−1xiq+1−1).

If the elliptic curve E(N)ξN (xiq ), q ∈ {1, . . . , p}, has no complex multiplication,
then (14) implies

HomRq,Q(Rq,Q · uq(Z
gq ), H1(Aπ(x), Q)) ≈ HomQgq ×gq (Q
gq×gq · uq(Z
gq ), (Q
2)gp)

≈ HomQ(Q · uq(Z
gq), Q
2)

≈ HomQ(Q
gp, Q
2) ≈ Q
2gp.

Similarly, if the elliptic curve E(N)ξN(xiq ), q ∈ {1, . . . , p}, has complex multipli-
cation, then

HomRq,Q(Rq,Q · uq(Z
gq), H1(Aπ(x), Q)) ≈ Hom
R
gq ×gq
q,Q (Rgq×gq
q,Q · uq(Z
gq), Rgq
q,Q)

≈ HomRq,Q(Rq,Q · uq(Z
gq ), Rq,Q)

≈ HomRq,Q(Rgp
q,Q, Rq,Q) ≈ Rgq
q,Q ≈ Q
2gq

by (14). Thus the Q-dimension of (15) is 2g. By Andr´e’s proposition, the
dimension of Ux equals the Q-dimension of the linear space (15), whence (12).
Finally, let us note that the generic derived Mumford-Tate group is

(16) MTder(H|X) =
 p′
∏

q=1
 (
G
2gq
a,Q ⋊ SL2,Q) × (G
2(g−g′)
a,Q ⋊ Hg(Acst))der.

THE RELATIVE BOGOMOLOV CONJECTURE 15

In fact, it is a normal subgroup of MT(H|X). Furthermore, its normal subgroup

G = MTder(H|X) ∩
 ( p′
∏

q=1
 (
G
2gq
a,Q ⋊ SL2,Q) × {e}
)

projects surjectively onto

MTder(H−1,x) = ∆g1(SL2,Q) × · · · × ∆gp′ (SL2,Q) = SLp′
2,Q ⊆ SLg′
2,Q = (GLg′
2,Q)der.

The following lemma, which is also of use in the next section, yields (16).

Lemma 2. Let G ⊆ ∏p′

q=1(G
2gq
a,Q ⋊ SL2,Q) be a normal Q-algebraic subgroup pro-

jecting onto SLp′
2,Q. Then, we have G = ∏p′

q=1(G
2gq
a,Q ⋊ SL2,Q).

Proof. We ﬁrst consider the case p′ = 1 and write g instead of g1. Note that for
every (v1, . . . , vg) ∈ (Q
2)g

and every (w1, . . . , wg, γ) ∈ (Q
2)g ⋊ SL2(Q),
the conjugate
(
v1, . . . , vg, (
1 0
0 1
)) · (w1, . . . , wg, γ) · (
v1, . . . , vg, (
1 0
0 1
))−1

equals (v1 − γ(v1) + w1, . . . , vg − γ(vg) + wg, γ).

Choose now a γ = (
a b
c d
) ∈ SL2(Q) such that

(17) (1 0
0 1

) − (a b
c d
) = (1 − a −b
−c 1 − d
)

is invertible; an explicit admissible choice would be a = d = 0 and b = −c = 1.
By assumption, there exists some

(w1, . . . , wg, γ) ∈ G(Q).

Moreover, the normality of G(Q) implies that

(v1 − γ(v1) + w1, . . . , vg − γ(vg) + wg, γ) ∈ G(Q)

for all (v1, . . . , vg) ∈ (Q
2)g. The invertibility of (17) implies that the preimage
of γ ∈ SL2(Q) in G(Q) ⊆ Q2g ⋊ SL2(Q) is of (algebraic) dimension 2g as each of
the maps Q
2 −! Q2 : vi ↦−! vi − γ(vi), i ∈ {1, . . . , g},
is surjective. This means that the quotient map q : G
2g
a,Q ⋊SL2,Q ! SL2,Q restricts
to a surjective homomorphism q|G : G ! SL2,Q whose kernel is of dimension 2g.
This is only possible if G = G
2g
a,Q ⋊ SL2,Q, whence the assertion of the lemma in
case p = 1.
The general case p > 1 can be proven similarly, working with a lifting of
(γ, . . . , γ) ∈ SL2(Q2)p in G(Q) and using the above argument in parallel on each
of the p factors. This shows that the kernel of q|G : G ! SLp
2,Q is of dimension
∑p
q=1 2(iq+1 − iq) = 2g, which forces again the asserted equality. □

16 LARS K ¨UHNE

8. The monodromy of H|X

Let x0 ∈ X(C) be a suﬃciently general point such that MT(Hx0) = MT(H|X)
and let Mon(H|X) ⊆ MT(H|X)(Q) denote the (ordinary) monodromy group at
x0 of the local system Vg
Z underlying H|X. We write Mon
alg(H|X) ⊆ MT(H|X)
for the connected component of its Q-algebraic closure (i.e., the (connected)
algebraic monodromy group of H|X with base point x0 in [2]). By [2, Theorem
1], the group Monalg(H|X) (resp. Mon
alg(H−1|X)) is a Q-normal subgroup of
MT
der(H|X) (resp. MTder(H−1|X)). (Note that the notion of “good” variation of
mixed Hodge structures used in [2] agrees with that of an admissible variation of
mixed Hodge structures. In fact, the latter notion is even trivially stronger than
the former, but a result of Kashiwara [18, Theorem 4.5.2] allows also to prove
the converse implication.)
In [17], it is proven that Mon
alg(H−1|X) = SLp′
2,Q in our situation (see the proof
of Equation (10) in loc.cit.). As the natural map Monalg(H|X) ! Monalg(H−1|X)
is evidently surjective, we infer from another use of Lemma 2 that Mon
alg(H|X)
projects onto ∏p′

q=1(G
2gq
a,Q ⋊ SL2,Q).
Consider again the connected component ̃X of u
−1
mixed(X) from Section 3 and its
stabilizer Stab( ̃X) under the action of (Z
2 ⋊Γ(N))g on (C ×H1)g. Both Stab( ̃X)
and Mon(H|X) are canonically subgroups of (Z
2 ⋊ Γ(N))g, and in fact they are
equal to each other. This seems well-known, but we include the argument here
for lack of reference and convenience of the reader. For this purpose, we choose
an arbitrary lifting ̃x0 ∈ ̃X of the point x0 ∈ X(C). If γ ∈ StabΓ( ̃X), then there
exists a path ̃φ : [0, 1] ! ̃X with ̃φ(0) = ̃x0 and ̃φ(1) = γ · ̃x0. Through transport
along the Z-local system ̃Vg
Z = u
∗
mixed(Vg
Z), the path ̃φ induces a Z-linear map

(18) Vg
Z,x0 = ̃Vg
Z,̃x0 −! ̃Vg
Z,γ·̃x0 = Vg
Z,x0,

which can be seen to equal γ ∈ MT(Hx) by unraveling deﬁnitions. Thus γ ∈
Mon(H|X). If conversely g ∈ Mon(H|X) is induced by a path φ : [0, 1] ! X
with φ(0) = φ(1) = x, then the lifting ̃γ : [0, 1] ! ̃X with ̃φ(0) = ̃x0 yields a
point ̃φ(1) = γ · ̃x0 for some γ ∈ (Z
2 ⋊ Γ(N))g . Considering again (18), we
infer γ = g. This means that the intersection g ̃X ∩ ̃X is non-empty. As both ̃X
and g ̃X are connected components of u
−1
mixed(X), we infer that actually ̃X = g ̃X,
whence g ∈ Stab( ̃X).

9. Separating holomorphic and anti-holomorphic terms

The (Z
2 ⋊ Γ(N))-invariance of the (1, 1)-form in (4) implies that, for every
local chart χ : B1(0)d ! ̃X and every γ ∈ Stab( ̃X), the equations (9) associated
with the charts χ : B1(0)d ! ̃X and γ ◦ χ : B1(0)d ! ̃X are equivalent. In
order to extract non-trivial information from monodromy, we pass to the product
̃X × ̃X ⊂ (C × H1)2g and exploit the fact that both holomorphic and anti-
holomorphic terms appear in (9). The author owes this important idea to [1,
Subsection 5.2].
 THE RELATIVE BOGOMOLOV CONJECTURE 17

We write pri : ̃X × ̃X ! ̃X, i ∈ {1, 2}, for the projection to the i-th factor.
On ̃X × ̃X, we consider the holomorphic functions

z♯
l = zl ◦ pr1, τ ♯
l = τl ◦ pr1, 1 ≤ l ≤ g,

and the antiholomorphic functions

z♭
l = zl ◦ pr2, τ ♭
l = τ l ◦ pr2, 1 ≤ l ≤ g.

We next deduce from the equations (9) on ̃X new equations constraining the
analytic subvariety ̃X × ̃X. These equations actually change under the product
action of (Z
2 ⋊Γ(N))2g on (C×H1)2g, so that we can use the action of Stab( ̃X)×
Stab( ̃X) to obtain non-trivial information. Let χ1 : B1(0)d ! ̃X (resp. χ2 :
B1(0)d ! ̃X) be a chart with local coordinates w♯
1, . . . , w♯
d (resp. w♭
1, . . . , w♭
d) on
B1(0)d. To increase readability, we write here f (resp. ∂f /∂w♯
m, ∂f /∂w♭
m) instead
of f ◦ (χ1, χ2) (resp. ∂(f ◦ (χ1, χ2))/∂w♯
m, ∂(f ◦ (χ1, χ2))/∂w♭
m) for functions f
on ̃X × ̃X. For each j ∈ {1, . . . , g}, we set

B′
j =
 (
(τ ♯
l − τ ♭
l) · ∂z♯
l
∂w♯
m − (z♯
l − z♭
l) · ∂τ ♯
l
∂w♯
m
 )
l∈{1,...,g},l̸=j
m∈{1,...,d}
 ,

and
 C′
j = (
(τ ♯
l − τ ♭
l) · ∂z♭
l
∂w♭
m − (z♯
l − z♭
l ) · ∂τ ♭
l
∂w♭
m
 )

l∈{1,...,g},l̸=j
m∈{1,...,d} .

(Note that ∂z♯
l /∂w♯
m and ∂τ ♯
l /∂w♯
m (resp. ∂z♭
l /∂w♭
m = ∂z♭
l/∂w♭
m and ∂τ ♭
l /∂w♭
m =
∂τ ♭
l /∂w♭
m) are holomorphic (resp. antiholomorphic) functions on B1(0)d×B1(0)d.)
We claim that, for every choice of charts χi : B1(0)d ! ̃X (i ∈ {1, 2}), the
product chart (χ1, χ2) : B1(0)d × B1(0)d ! ̃X × ̃X,

satisﬁes the relations
(19)
rj(τ ♯
j − τ ♭
j)3 det(B′
j) det(C′
j) = rk(τ ♯
k − τ ♭
k)3 det(B′
k) det(C′
k), j, k ∈ {1, . . . g},

on B1(0)d × B1(0)d. With this aim in mind, we consider the set

R = ⋃

(χ1,χ2)(χ1(0), χ2(0))

where (χ1 : B1(0)d ! ̃X, χ2 : B1(0)d ! ̃X)

ranges through all pairs of charts on ̃X such that χ1 × χ2 satisﬁes the relation
(19) at (0, 0). The following three statements are equivalent:
(1) (̃x1, ̃x2) ∈ R.
(2) There exists a pair of charts (χ1 : B1(0)d ! ̃X, χ2 : B1(0)d ! ̃X) such
that (̃x1, ̃x2) ∈ im(χ1 × χ2) and (19) is satisﬁed at (χ1, χ2)−1(̃x1, ̃x2).
(3) For every pair of charts (χ1 : B1(0)d ! ̃X, χ2 : B1(0)d ! ̃X) such that
(̃x1, ̃x2) ∈ im(χ1 × χ2), the equation (19) is satisﬁed at (χ1, χ2)−1(̃x1, ̃x2).

18 LARS K ¨UHNE

Indeed, the implications (3) ⇒ (2) and (2) ⇒ (1) are trivial and the implication
(1) ⇒ (3) follows from the fact that (19) is independent under transformations of
the local coordinates w♯
1, . . . , w♯
d, w♭
1, . . . , w♭
d. From these equivalences, we deduce
that R is locally cut out by a real-analytic equation. We also see that our above
claim amounts to R = ̃X × ̃X.
Since ̃X × ̃X is irreducible (as a complex-analytic subset of (C × H1)2g), it
suﬃces hence to show that R contains a non-empty open subset of ̃X × ̃X. For
this purpose, we consider an arbitrary point (̃x, ̃x) ∈ ̃X × ̃X on the diagonal. Let
χ : B1(0)d ! ̃X be a chart such that χ(0) = ̃x. By the above equivalences, the
real-analytic set (χ, χ)−1(R) ⊆ B1(0)d × B1(0)d coincides with

R(χ,χ) = {
(w♯
1, . . . , w♯
d, w♭
1, . . . , w♭
d) ∈ B1(0)d × B1(0)d
∣
∣
∣ (χ × χ) satisﬁes (19) at (w♯
1, . . . , w♯
d, w♭
1, . . . , w♭
d)} .

Writing (·) : B1(0)d ! B1(0)d for the component-wise complex conjugation, the
set (idB1(0)d × (·))−1(R(χ,χ)) is a complex -analytic subset of B1(0)d × B1(0)d as
can be seen by inspecting (19); this relies on the following elementary fact: If
f (w1, . . . , wd) = ∑

i1,...,id ai1,...,idwi1
1 · · · wid
d is a holomorphic function on B1(0)d,
then f (w1, . . . , wd) = ∑

i1,...,id ai1,...,idwi1
1 · · · wid
d is holomorphic as well. Further-
more, the fact that the chart χ satisﬁes the previous equation (9) implies imme-
diately that

∆skew = {(w1, . . . , wd, w1, . . . , wd) | (w1, . . . , wd) ∈ B1(0)d}

⊆ (idB1(0)d × (·))−1(R(χ,χ));

in fact, plugging in the local coordinates (w1, . . . , wd, w1, . . . , wd) into the equa-
tion (19) for the chart (χ × χ) yields the original equation (9) for the chart χ
back. As the smallest complex-analytic set of B1(0)d × B1(0)d containing ∆skew
is B1(0)d × B1(0)d, we infer that

(idB1(0)d × (·))−1(R(χ,χ)) = B1(0)d × B1(0)d

and hence R(χ,χ) = B1(0)d × B1(0)d, whence R = ̃X × ̃X. In other words, the
equations (19) are satisﬁed on all of ̃X × ̃X.

10. Enter monodromy

Let χi : B1(0)d ! ̃X, i ∈ {1, 2}, two local charts and γ ∈ Stab( ̃X). As
γ( ̃X) = ̃X, the composite γ ◦ χ1 : B1(0)d ! ̃X is a local chart of ̃X as well.
Writing
 γ = ((m1
n1
 ) , (
a1 b1
c1 d1
) , . . . , (
mg
ng
 ) , (
ag bg
cg dg
)) ,

we note that

zl ◦ γ = zl + ml + nlτl
clτl + dl and τl ◦ γ = alτl + bl
clτl + dl , l ∈ {1, . . . , g},

as functions on ̃X. We infer that

z♯
l ◦ (γ, id) = z♯
l + ml + nlτ ♯
l
clτ ♯
l + dl and τ ♯
l ◦ (γ, id) = alτ ♯
l + bl
clτ ♯
l + dl , l ∈ {1, . . . , g},

THE RELATIVE BOGOMOLOV CONJECTURE 19

as functions on ̃X × ̃X. We also need the derivatives

∂(z♯
l ◦ (γ, id))

∂w♯
m = 1

(clτ ♯
l + dl) ·
 ( ∂z♯
l
∂w♯
m + nl · ∂τ ♯
l
∂w♯
m
 )
 − cl(z♯
l + ml + nlτ ♯
l )

(clτ ♯
l + dl)2 · ∂τ ♯
l
∂w♯
m

and ∂(τ ♯
l ◦ (γ, id))

∂w♯
m = 1

(clτ ♯
l + dl)2 · ∂τ ♯
l
∂w♯
m
on B1(0)d × B1(0)d. With this preparation, we can compute the equations (19)
for the chart (γ ◦ χ1, χ2) : B1(0)d × B1(0)d −! ̃X × ̃X;
these are

(20)

rj
 (ajτ ♯
j + bj
cjτ ♯
j + dj − τ ♭
j
)3 det(B′′
j ) det(C′′
j ) = rk
 ( akτ ♯
k + bk
ckτ ♯
k + dk − τ ♭
k
)3 det(B′′
k) det(C′′
k),

j, k ∈ {1, . . . g},

with the (d × d)-matrices

(B′′
j )l∈{1,...,g},l̸=j
m∈{1,...,d} and (C′′
j )l∈{1,...,g},l̸=j
m∈{1,...,d}
where

(B′′
j )lm =
 ( alτ ♯
l + bl
clτ ♯
l + dl − τ ♭
l
 )
·
( 1

(clτ ♯
l + dl) ·
 [ ∂z♯
l
∂w♯
m + nl · ∂τ ♯
l
∂w♯
m
 ]
 − cl(z♯
l + ml + nlτ ♯
l )

(clτ ♯
l + dl)2 · ∂τ ♯
l
∂w♯
m
 )

−
 ( z♯
l + ml + nlτ ♯
l
clτ ♯
l + dl − z♭
l
 )
 · 1
(clτ ♯
l + dl)2 · ∂τ ♯
l
∂w♯
m

and
 (C′′
j )lm =
 ( alτ ♯
l + bl
clτ ♯
l + dl − τ ♭
l
)
 · ∂z♭
l
∂w♭
m −
 ( z♯
l + ml + nlτ ♯
l
clτ ♯
l + dl − z♭
l
 )
 · ∂τ ♭
l
∂w♭
m .

In summary, each pair (χ1, χ2) of charts χi : B1(0)d ! ̃X, i ∈ {1, 2}, does not
only satisfy the equation (19), but also the equations (20) for all γ ∈ Stab( ̃X).
Moreover, we can consider each of these equations at each point of B1(0)d×B1(0)d

as an algebraic equation on γ ∈ Stab( ̃X), giving a C-algebraic hypersurface
of MT(H|X) containing the Q-rational points Mon(H|X) = Stab( ̃X). By [5,
Corollary AG.14.6], this hypersurface contains also the algebraic monodromy
group Monalg(H|X), which is the Q-algebraic closure of these Q-rational points.
We infer that each pair (χ1, χ2) satisﬁes (20) for all γ ∈ Mon
alg(H|X)(Q).

11. A non-vanishing determinant

We make a ﬁnal reduction before we start exploiting the equations (20) ob-
tained in the last section. To be precise, we show that we can assume the
following: For each chart

χ0 : B1(0)d −! ̃X, w = (w1, . . . , wd) ↦−! (zl ◦ χ0(w), τl ◦ χ0(w))1≤l≤g ,

20 LARS K ¨UHNE

the determinant

(21) det
 


( ∂(zl ◦ χ0)
∂wm
 )
l∈{1,...,g−1}
m∈{1,...,d}
 



is a non-zero holomorphic function on B1(0)d. Note that this condition holds for
every chart if and only if it holds for a single one.
For each ﬁnite map S′ ! S, note that (RBC) for a subvariety X in a family
π : A ! S is equivalent to (RBC) for the subvariety XS′ = X ×S S′ in the family
πS′ : A ×S S′ ! S′. Furthermore, (RBC) for a subvariety X ⊆ A is equivalent
to (RBC) for any translate X + τ ⊆ A by a torsion section τ : S ! A. By
assumption, S is a subvariety of Y (N) and A = E(N)|S.
Let q = (s1/t1, . . . , sg/tg) ∈ Q
g be given with gcd(si, ti) = 1 for all i ∈
{1, . . . , g}, we set N′ = lcm(t1, . . . , tg, N), so that all torsion points of or-
der lcm(t1, . . . , tg) in the generic ﬁber E(N′)ηY (N′) extend to torsion sections
Y (N′) ! E(N′). Writing ξN′/N : E(N′) ! E(N) for the standard covering and
setting X ′
q = ξ−1
N′/N(X), the analytic variety ̃X is also a connected component of
u
−1
mixed(X ′
q). Thus, there exists a torsion section τ : Y (N′) ! E(N′) such that
the translate

̃Xq =
 {(
zi + si
ti · τi, τi
)

1≤i≤g ∈ (C × H1)g ∣
∣
∣
∣
∣ (zi, τi)1≤i≤g ∈ ̃X
}

is a connected component of u
−1
mixed(X ′
q + τ ).
For a ﬁxed local chart

χ0 : B1(0)d −! ̃X, w ↦−! (zi ◦ χ0(w), τi ◦ χ0(w))1≤i≤g ,

each of its translates

χ0,q : B1(0)d −! ̃Xq, w ↦−! (
zi ◦ χ0(w) + si
ti · τi, τi ◦ χ0(w))
1≤i≤g ,

is a chart of ̃Xq. As (RBC) for X ′
q is equivalent to (RBC) for X by the above
remarks, it suﬃces to prove that the determinant (21) is a non-zero holomorphic
function for a single chart χ0,q (q ∈ Q
g). If this would not be the case, then

det
 


(∂(zl ◦ χ0)
∂wm + sl
tl · ∂(τl ◦ χ0)
∂wm
 )

l∈{1,...,g−1}
m∈{1,...,d}
 

 (w) = 0

for all (s1/t1, · · · , sg/tg) ∈ Q
g and all w ∈ B1(0)d. By continuity, this means

det
 


(∂(zl ◦ χ0)
∂wm + ul · ∂(τl ◦ χ0)
∂wm
 )
l∈{1,...,g−1}
m∈{1,...,d}
 

 (w) = 0

for all (u1, . . . , ug) ∈ Rg and all w ∈ B1(0)d. In particular, we can take

ul = −Im(zl ◦ χ0)
Im(τl ◦ χ0) (w), 1 ≤ l ≤ g,

THE RELATIVE BOGOMOLOV CONJECTURE 21

so that

(22) det
 


(∂(zl ◦ w0)
∂wm − Im(zl)
Im(τl) · ∂(τl ◦ χ0)
∂wm
 )

l∈{1,...,g−1}
m∈{1,...,d}
 

 (w) = 0

for all w ∈ B1(0)d. Comparing with (8), we infer that α′
1 = 0, which is a clear
contradiction to the non-degeneracy of pr̂1(X).
In summary, we can use without loss of generality that (21) is a non-zero
holomorphic function for each chart χ : B1(0)d ! ̃X and a ﬁxed j0 ∈ {1, . . . , g}.

12. Proof that p′ = 0 or p′ = p

We claim that either all the families π : Ei ! S are constant (i.e., p′ = 0)
or non-constant (i.e., p′ = p). For this purpose, assume that p′ ≥ 1 so that the
family E1 = · · · = Ei2−1 ! S is non-isotrivial and that the family Eip = · · · =
Eg ! S is constant.
From Section 8, we know that Mon
alg(H|X) ⊆ (G
2
a,Q⋊SL2,Q)g projects onto the
ﬁrst p′ factors ∏p′

q=1(G
2gq
a,Q ⋊ SL2,Q), which gives rise to a surjective map between
their Q-points. For every integer N, there hence exists an element

γ = ((
m1
n1
 ) , (
a1 b1
c1 d1
) , . . . , (
mg
ng
 ) , (
ag bg
cg dg
)) ∈ Mon
alg(H|X)(Q)

with al = 1, bl = N, cl = 0, dl = 1, ml = 0, nl = 0
for all 1 ≤ l ≤ ip′+1 − 1. Since the families El (ip′+1 ≤ l ≤ g) are trivial, we have
furthermore al = 1, bl = 0, cl = 0, dl = 1
for all ip′+1 ≤ l ≤ g. Let us additionally ﬁx a chart χ0 : B1(0)d ! ̃X. Specializing
to the chart (γ ◦ χ0, χ0) : B1(0)d × B1(0)d ! ̃X × ̃X, equation (20) for j = 1 and
k = g becomes

(23) r1(τ ♯
1 + N − τ ♭
1)3 det(B′′
1) det(C′′
1) = rg(τ ♯
g − τ ♭
g)3 det(B′′
g) det(C′′
g)

with
 B′′
j =
 (
(τ ♯
l + bl − τ ♭
l ) · ∂z♯
l
∂w♯
m − (z♯
l − z♭
l ) · ∂τ ♯
l
∂w♯
m
 )
l∈{1,...,g},l̸=j
m∈{1,...,d}
and
 C′′
j = (
(τ ♯
l + bl − τ ♭
l ) · ∂z♭
l
∂w♭
m − (z♯
l − z♭
l ) · ∂τ ♭
l
∂w♭
m
 )

l∈{1,...,g},l̸=j
m∈{1,...,d} .

We can consider the diﬀerence between the left-hand and the right-hand side of
(23) as a polynomial over the ring of (real-analytic) functions on B1(0)d × B1(0)d

and indeterminate N. As this polynomial vanishes for each integer, it has to
vanish identically. Expanding the left-hand side of the equation for the term of
highest order in N, we note that its term of highest degree in N is

r1
 g∏

l=ip′+1(τ ♯
l − τ ♭
l)2 · det
 




( ∂z♯
l
∂w♯
m
 )
 l∈{2,...,g}
m∈{1,...,d}



 det
 


( ∂z♭
l
∂w♭
m
 )
 l∈{2,...,g}
m∈{1,...,d}


 N 2ip′+1−1

22 LARS K ¨UHNE

by our assumption on the non-vanishing of (21). However, the leading term on
the right-hand side has degree ≤ 2(ip′+1−1) = 2ip′+1−2. From this contradiction,
we conclude that p′ = 0 or p′ = p. Note that by our assumptions in Section 2,
p′ = 0 implies dim(S) = 0. This means that A is just an abelian variety, for
which (RBC) is proven in [35]. We hence concentrate on the case p′ = p in the
following.
 13. Existence of generic isogenies

In this section, we prove that the generic ﬁbers Ei,η (1 ≤ i ≤ g) are all
isogeneous (i.e., p = 1) in the remaining case that all families Ei ! S (1 ≤ i ≤ g)
are non-isotrivial (i.e., p′ = p). Let Mq, 1 ≤ q ≤ p, be arbitrary integers and set

Niq = Niq+1 = · · · = Niq+1−1 = Mq

for all 1 ≤ q ≤ p. Again by the results from Section 8, we know that Mon
alg(H|X) =
∏p
q=1(G
2gq
a,Q ⋊ SL2,Q) (diagonally embedded in (G
2
a,Q ⋊ SL2,Q)g). Thus, there exists
an element

γ = ((
m1
n1
 ) , (
a1 b1
c1 d1
) , . . . , (
mg
ng
 ) , (
ag bg
cg dg
)) ∈ Mon
alg(H|X)(Q)

with al = 1, bl = Nl, cl = 0, dl = 1, ml = 0, nl = 0
for all 1 ≤ l ≤ g. Since there is nothing to prove if p = 1, we can assume that
there exists k ∈ {i2, . . . , i3 − 1}. Specializing again to the chart (γ ◦ χ0, χ0) :
B1(0)d × B1(0)d ! ̃X × ̃X, the equation (20) for j = 1 and k as here becomes

(24) r1(τ ♯
1 + N1 − τ ♭
1)3 det(B′′
1) det(C′′
1) = rk(τ ♯
k + Nk − τ ♭
k)3 det(B′′
k) det(C′′
k)

with the (d × d)-matrices

B′′
j =
 (
(τ ♯
l + Nl − τ ♭
l) · ∂z♯
l
∂w♯
m − (z♯
l − z♭
l) · ∂τ ♯
l
∂w♯
m
 )
l∈{1,...,g},l̸=j
m∈{1,...,d}
and
 C′′
j = (
(τ ♯
l + Nl − τ ♭
l) · ∂z♭
l
∂w♭
m − (z♯
l − z♭
l) · ∂τ ♭
l
∂w♭
m
 )

l∈{1,...,g},l̸=j
m∈{1,...,d} .

The diﬀerence of both sides in (24) can be considered as a multivariate polynomial
in the variables Mq = Niq = · · · = Niq+1−1, 1 ≤ q ≤ p, of total degree ≤ (2d + 3),
which has to vanish identically because its evaluations for all (M1, . . . , Mp) ∈ Z
p

vanish. In fact, the sum of its terms of highest degree 2d + 3 is

r1 det
 




( ∂z♯
l
∂w♯
m
 )
 l∈{2,...,g}
m∈{1,...,d}



 det
 

( ∂z♭
l
∂w♭
m
 )
 l∈{2,...,g}
m∈{1,...,d}


 · M1
 g∏

l=1 N 2
l

− rk det
 




( ∂z♯
l
∂w♯
m
 )
l∈{1,...,g},l̸=k
m∈{1,...,d}
 


 det
 


( ∂z♭
l
∂w♭
m
 )

l∈{1,...,g},l̸=k
m∈{1,...,d}
 

 · M2
 g∏

l=1 N 2
l .

THE RELATIVE BOGOMOLOV CONJECTURE 23

Since the two terms contain diﬀerent monomials in M1, . . . , Mp, their coeﬃcients
must vanish. As in the previous section, the vanishing of the ﬁrst coeﬃcient
yields a contradiction to the non-vanishing of (21), whence p = 1. Recall that
this implies E1 = E2 = · · · = Eg
by the assumptions made in Subsection 7. Our assumptions on S from Section
2 imply furthermore that S is the diagonal of E(N)g in this case.

14. Existence of a linear equation on zl| ̃X (1 ≤ l ≤ g).

In this section, we deduce a linear equation governing the restrictions of the
functions zl, 1 ≤ l ≤ g, to ̃X. For each integer N, there exists an element

γ = ((
m1
n1
 ) , (
a1 b1
c1 d1
) , . . . , (
mg
ng
 ) , (
ag bg
cg dg
)) ∈ Mon
alg(H|X)(Q)

with al = 1, bl = N, cl = 0, dl = 1, ml = 0, nl = 0
for all 1 ≤ l ≤ g. Specializing again to the chart

(γ ◦ χ0, χ0) : B1(0)d × B1(0)d ! ̃X × ̃X,

the equations (20) become

(25) rj(τ ♯
j + N − τ ♭
j)3 det(B′′
j ) det(C′′
j ) = rk(τ ♯
k + N − τ ♭
k)3 det(B′′
k) det(C′′
k),

j, k ∈ {1, . . . , g},

with the (d × d)-matrices

B′′
j =
 (
(τ ♯
l + N − τ ♭
l) · ∂z♯
l
∂w♯
m − (z♯
l − z♭
l ) · ∂τ ♯
l
∂w♯
m
 )

l∈{1,...,g},l̸=j
m∈{1,...,d}
and
 C′′
j = (
(τ ♯
l + N − τ ♭
l) · ∂z♭
l
∂w♭
m − (z♯
l − z♭
l) · ∂τ ♭
l
∂w♭
m
 )

l∈{1,...,g},l̸=j
m∈{1,...,d} .

Regarding again the diﬀerence of both sides of (25) as a polynomial in the
indeterminate N with coeﬃcients in the ring of (real-analytic) functions on
B1(0)d × B1(0)d and considering the term of highest degree, we obtain

rj det
 




( ∂z♯
l
∂w♯
m
 )
l∈{1,...,g},l̸=j
m∈{1,...,d}
 


 det
 


( ∂z♭
l
∂w♭
m
 )

l∈{1,...,g},l̸=j
m∈{1,...,d}
 



= rk det
 




( ∂z♯
l
∂w♯
m
 )
l∈{1,...,g},l̸=k
m∈{1,...,d}
 


 det
 

( ∂z♭
l
∂w♭
m
 )

l∈{1,...,g},l̸=k
m∈{1,...,d}
 



Specializing to the diagonal B1(0)d ⊂ B1(0)d × B1(0)d, this yields

rj
 ∣
∣
∣
∣det (
( ∂zl
∂wm )l∈{1,...,g},l̸=j
m∈{1,...,d}
 )∣
∣
∣
∣

2 = rk
 ∣
∣
∣
∣det (( ∂zl
∂wm )
l∈{1,...,g},l̸=k
m∈{1,...,d}
 )∣
∣
∣
∣
2

24 LARS K ¨UHNE

for the chart χ0 : B1(0)d ! ̃X. As both determinants are holomorphic functions
on B1(0)d, this implies

(26) r1/2
j det (
( ∂zl
∂wm )l∈{1,...,g},l̸=j
m∈{1,...,d}
 ) = uj,k · r1/2
k det (( ∂zl
∂wm )
l∈{1,...,g},l̸=k
m∈{1,...,d}
 )

for some uj,k ∈ S1 = {z ∈ C | |z| = 1}. Since the determinant (21) does not
vanish, we can specialize (26) to k = g and obtain

det ( ∂zl
∂wm )l∈{1,...,g},l̸=j
m∈{1,...,d}
det ( ∂zl
∂wm )l∈{1,...,g−1}
m∈{1,...,d}
 = uj,g · r1/2
g
r1/2
j

for each j ∈ {1, . . . , g − 1}. Setting fj = (−1)(g−l−1)uj,gr1/2
g /r1/2
j ∈ C× for
j ∈ {1, . . . , g − 1}, we can use Kramer’s rule to obtain

f1
 




 ∂z1
∂w1
∂z1
∂w2
· · ·
∂z1
∂wd
 



 + f2
 




 ∂z2
∂w1
∂z2
∂w2
· · ·
∂z2
∂wd
 



 + · · · + fg−1
 





 ∂zg−1
∂w1
∂zg−1
∂w2
· · ·
∂zg−1
∂wd
 




 =
 





 ∂zg
∂w1
∂zg
∂w2
· · ·
∂zg
∂wd
 






on B1(0)d. Therefore, we obtain

∂
∂wm (f1z1 + f2z2 + · · · + fg−1zg−1 + zg) = 0, 1 ≤ m ≤ d,

for all m ∈ {1, . . . , d}. In conclusion, we obtain a non-trivial linear equation

(27) f1z1 + f2z2 + · · · + fgzg = b, b ∈ C,

valid on all of ̃X by real-analytic continuation.

15. Completion of the proof of Theorem 1

By Section 13, the variety S is the diagonal in Y (N)g and hence a special
Shimura subvariety. Thus by [15, Section 3.3], the bi-algebraic closure X biZar of
X as deﬁned in [15] is the minimal horizontal torsion coset containing X. It is
therefore our goal to prove that dim(X biZar) ≤ g by means of the Ax-Schanuel
conjecture for mixed Shimura varieties; in fact, this contradicts the assumption
in (RBC). For this purpose, we set

Y = {(̃x, x) ∈ ̃X × X(C) | umixed(̃x) = x} ⊆ (H1 × C)g × E(N)g(C).

The mixed Ax-Schanuel conjecture in the form of [15, Theorem 1.1] yields

dim(X biZar) ≤ dim(Y Zar) − dim(Y )

where Y Zar is the Zariski closure of Y in (P1(C) × C)g × E(N)g(C). Writing
H ⊂ Cg for the linear hypersurface determined by (27) and ∆(P1(C)) for the
diagonal in P1(C), the analytic variety Y is contained in the algebraic subset

(∆(H1) × H) × X ⊂ (P1(C) × C)g × E(N)g(C).

It follows that
 dim(Y Zar) ≤ 1 + (g − 1) + dim(X) = dim(X) + g.

THE RELATIVE BOGOMOLOV CONJECTURE 25

As dim(Y ) = dim(X), we conclude that

dim(X biZar) ≤ dim(Y Zar) − dim(Y ) ≤ g,

which concludes our proof of Theorem 1.
Acknowledgements: The author thanks Laura DeMarco, Ziyang Gao, Philipp
Habegger, Myrto Mavraki, and Fabien Pazuki for their advice, discussion and
encouragement. Finally, he thanks the anonymous referee for their attentive
reading and their many suggestions that helped to improve the exposition sub-
stantially. He also thanks Jakob Stix for pointing out some inaccuracies in the
article.
 References

[1] Y. Andr´e, P. Corvaja, and U. Zannier. The Betti map associated to a section of an abelian
scheme. Invent. Math., 222(1):161–202, 2020.
[2] Yves Andr´e. Mumford-Tate groups of mixed Hodge structures and the theorem of the
ﬁxed part. Compositio Math., 82(1):1–24, 1992.
[3] Christina Birkenhake and Herbert Lange. Complex abelian varieties, volume 302 of
Grundlehren der Mathematischen Wissenschaften [Fundamental Principles of Mathemat-
ical Sciences]. Springer-Verlag, Berlin, second edition, 2004.
[4] Fedor Bogomolov, Hang Fu, and Yuri Tschinkel. Torsion of elliptic curves and unlikely
intersections. In Geometry and physics. Vol. I, pages 19–37. Oxford Univ. Press, Oxford,
2018.
[5] Armand Borel. Linear algebraic groups, volume 126 of Graduate Texts in Mathematics.
Springer-Verlag, New York, second edition, 1991.
[6] Pierre Deligne. Th´eorie de Hodge. III. Inst. Hautes ´Etudes Sci. Publ. Math., (44):5–77,
1974.
[7] Laura DeMarco, Holly Krieger, and Hexi Ye. Uniform Manin-Mumford for a family of
genus 2 curves. Ann. of Math. (2), 191(3):949–1001, 2020.
[8] Laura DeMarco and Niki Myrto Mavraki. Elliptic surfaces and intersections of adelic R-
divisors,. to appear in J. Eur. Math. Soc.
[9] Laura DeMarco and Niki Myrto Mavraki. Variation of canonical height and equidistribu-
tion. Amer. J. Math., 142(2):443–473, 2020.
[10] Fred Diamond and Jerry Shurman. A ﬁrst course in modular forms, volume 228 of Grad-
uate Texts in Mathematics. Springer-Verlag, New York, 2005.
[11] Vesselin Dimitrov, Ziyang Gao, and Philipp Habegger. A consequence of the relative
Bogomolov conjecture. to appear in J. of Number Theory.
[12] Vesselin Dimitrov, Ziyang Gao, and Philipp Habegger. Uniform bound for the number of
rational points on a pencil of curves. Int. Math. Res. Not. IMRN, (2):1138–1159, 2021.
[13] Vesselin Dimitrov, Ziyang Gao, and Philipp Habegger. Uniformity in Mordell-Lang for
curves. Ann. of Math. (2), 194(1):237–298, 2021.
[14] Ziyang Gao. Generic rank of Betti map and unlikely intersections. Compos. Math.,
156(12):2469–2509, 2020.
[15] Ziyang Gao. Mixed Ax-Schanuel for the universal abelian varieties and some applications.
Compos. Math., 156(11):2263–2297, 2020.
[16] Thomas Gauthier. Good height functions on quasi-projective varieties: equidistribution
and applications in dynamics. arXiv e-prints, page arXiv:2105.02479, May 2021.
[17] Philipp Habegger and Jonathan Pila. Some unlikely intersections beyond Andr´e-Oort.
Compos. Math., 148(1):1–27, 2012.
[18] Masaki Kashiwara. A study of variation of mixed Hodge structure. Publ. Res. Inst. Math.
Sci., 22(5):991–1024, 1986.
[19] Nicholas M. Katz and Barry Mazur. Arithmetic moduli of elliptic curves, volume 108 of
Annals of Mathematics Studies. Princeton University Press, Princeton, NJ, 1985.
[20] Lars K¨uhne. Equidistribution in Families of Abelian Varieties and Uniformity. arXiv e-
prints, page arXiv:2101.10272, January 2021.

26 LARS K ¨UHNE

[21] James D. Lewis. A survey of the Hodge conjecture, volume 10 of CRM Monograph Series.
American Mathematical Society, Providence, RI, second edition, 1999. Appendix B by B.
Brent Gordon.
[22] David Masser and Umberto Zannier. Torsion points on families of squares of elliptic curves.
Math. Ann., 352(2):453–484, 2012.
[23] David Masser and Umberto Zannier. Torsion points on families of products of elliptic
curves. Adv. Math., 259:116–133, 2014.
[24] David Masser and Umberto Zannier. Torsion points, Pell’s equation, and integration in
elementary terms. Acta Math., 225(2):227–313, 2020.
[25] J. S. Milne. Shimura varieties and moduli. In Handbook of moduli. Vol. II, volume 25 of
Adv. Lect. Math. (ALM), pages 467–548. Int. Press, Somerville, MA, 2013.
[26] Martin Olsson. Algebraic spaces and stacks, volume 62 of American Mathematical Society
Colloquium Publications. American Mathematical Society, Providence, RI, 2016.
[27] Chris A. M. Peters and Joseph H. M. Steenbrink. Mixed Hodge structures, volume 52 of
Ergebnisse der Mathematik und ihrer Grenzgebiete. 3. Folge. A Series of Modern Surveys
in Mathematics [Results in Mathematics and Related Areas. 3rd Series. A Series of Modern
Surveys in Mathematics]. Springer-Verlag, Berlin, 2008.
[28] Richard Pink. Arithmetical compactiﬁcation of mixed Shimura varieties. Bonner Mathe-
matische Schristen [Bonn Mathematical Publications], 209. Universit¨at Bonn Mathematis-
ches Institut, Bonn, 1990. Dissertation, Rheinische Friedrich-Wilhelms-Universit¨at Bonn,
Bonn, 1989.
[29] Richard Pink. A common generalization of the conjectures of Andr´e-Oort, Manin-
Mumford, and Mordell-Lang. available from http://www.math.ethz.ch/~pink, 04 2005.
[30] Michel Raynaud. Faisceaux amples sur les sch´emas en groupes et les espaces homog`enes.
Lecture Notes in Mathematics, Vol. 119. Springer-Verlag, Berlin-New York, 1970.
[31] Emmanuel Ullmo. Positivit´e et discr´etion des points alg´ebriques des courbes. Ann. of
Math. (2), 147(1):167–179, 1998.
[32] J¨org Wildeshaus. Realizations of polylogarithms, volume 1650 of Lecture Notes in Mathe-
matics. Springer-Verlag, Berlin, 1997.
[33] Xinyi Yuan. Arithmetic bigness and a uniform Bogomolov-type result, August 2021.
[34] Xinyi Yuan and Shou-Wu Zhang. Adelic line bundles over quasi-projective varieties. arXiv
e-prints, page arXiv:2105.13587, May 2021.
[35] Shou-Wu Zhang. Equidistribution of small points on abelian varieties. Ann. of Math. (2),
147(1):159–165, 1998.
[36] Shou-Wu Zhang. Small points and Arakelov theory. In Proceedings of the International
Congress of Mathematicians, Vol. II (Berlin, 1998), number Extra Vol. II, page 217–225,
1998.
Email address: lk@math.ku.dk

Institut for Matematiske Fag, Universitetsparken 5, 2100 København Ø, Den-
mark
