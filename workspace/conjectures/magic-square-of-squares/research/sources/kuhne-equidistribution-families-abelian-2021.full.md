<!-- source: https://arxiv.org/pdf/2101.10272 | converted from PDF -->

arXiv:2101.10272v4  [math.NT]  23 Dec 2024
EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES
AND UNIFORMITY

LARS K ¨UHNE

Abstract. Using equidistribution techniques from Arakelov theory as well as
recent results obtained by Dimitrov, Gao, and Habegger, we deduce uniform
results on the Manin-Mumford and the Bogomolov conjecture. For each given
integer g ≥ 2, we prove that the number of torsion points lying on a smooth
complex algebraic curve of genus g embedded into its Jacobian is uniformly
bounded. Complementing recent works of Dimitrov, Gao, and Habegger, we
obtain a rather uniform version of the Mordell conjecture as well. In particular,
the number of rational points on a smooth algebraic curve deﬁned over a
number ﬁeld can be bounded solely in terms of its genus and the Mordell-Weil
rank of its Jacobian.

Throughout this article, K is a number ﬁeld and S is a smooth, geometri-
cally irreducible algebraic variety over K. The variety S serves as the base of
a family π : A ! S of abelian varieties (i.e., A is an abelian scheme over S).
We furthermore assume that we are given an arbitrary immersion ι : A ֒! PN
K.
Note that such an immersion need not exist and it does not if the base S is not
quasi-projective.
For a quasi-projective variety X over K and an archimedean place ν of K,
we denote by X an
Cν the complex (analytic) space Cν-analytic space associated
with XCν (see [32] for this notion). For each archimedean place ν ∈ Σ∞(K), a
closed point x ∈ A yields a 0-cycle Oν(x) = (x ⊗K Cν)an on the Cν-analytic
space A
an
Cν associated with A. Given an irreducible subvariety X ⊆ A, we call a
sequence (xi) ∈ X N of closed points X-generic if none of its inﬁnite subsequences
is contained in a proper algebraic subvariety of X. Note that a sequence is X-
generic if and only if it converges to the generic point of X in the Zariski topology.
Our ﬁrst aim is to state an analogue of the equidistribution conjecture for
abelian varieties that takes its place within the given relative setting π : A !
S. For this purpose, we have to introduce a generalization of the N´eron-Tate
height. We refer to Section 1 for details and only sketch the basic deﬁnitions
here. The line bundle O(1) on PN
OK can be endowed with C ∞-hermitian metrics
at the inﬁnite places Σ∞(K) (e.g. Fubini-Study metrics), so that we obtain a
C ∞-hermitian line bundle O(1) on PN
OK . In this way, we obtain an associated
Arakelov height hO(1) for subvarieties of PN
K. We remark that our height is the
top arithmetic intersection number divided by the degree as this deﬁnition is well-
adapted to Zhang’s inequalities [95, Theorem 5.2] and Yuan’s bigness theorem

2010 Mathematics Subject Classiﬁcation. 11G50 (primary), and 11G30, 14G05, 14G40,
14H40 (secondary). 1

2 LARS K ¨UHNE

[93]. Other articles, most prominently [21], deﬁne the height as the top arithmetic
intersection number.
Throughout this article, we work with a ﬁxed integer n ≥ 2. For each irre-
ducible subvariety X ⊆ A and every integer k ≥ 0, we write Xk for ι([n
k](X))
and X k for its Zariski-closure in PN
K. We then deﬁne

(1) ̂h(X) = lim sup
k!∞
 ( hO(1)(X k)
n2k
 )
 ∈ [0, ∞].

As [n] preserves the ﬁbers of π, the limit superior in (1) specializes to an ordinary
N´eron-Tate height if X is completely contained in such a ﬁber ([38, Theorem
11.18]). In this case, the limit superior can be replaced by a limit. In particular,
the limit process is well-behaved for closed points in A.
For each archimedean place ν ∈ Σ∞(K) and every non-empty simply con-
nected open U ⊆ San
Cν , there exists by [19, Proposition B.2] a real-analytic iso-
morphism a : A
an
Cν |U −! (R/Z)2 dim(A/S) × U
that restricts to a group homomorphism in the ﬁber over each point of U. The
induced map b = pr1 ◦ a : A
an
Cν |U −! (R/Z)2 dim(A/S)

is unique up to post-composition with an automorphism of (R/Z)2 dim(A/S). For
a geometrically irreducible subvariety X ⊆ A with π(X) = S and every point
x ∈ (X sm)an
Cν ∩ π−1(U), we deﬁne rankBetti(X, x), the Betti rank of X at x, as the
R-dimension of
 db(TR,xX an
Cν ) ⊆ Tb(x)(R/Z)2 dim(A/S) = R2 dim(A/S).

The subvariety X ⊆ A is called non-degenerate if and only if there exists a point
x0 ∈ (X sm)an
Cν ∩ π−1(U) such that rankBetti(X, x0) = 2 dim(X). It is easy to see
that these deﬁnitions depend neither on the choice of U nor a. A priori, whether
a subvariety is non-degenerate or not may depend on the choice of archimedean
place ν, but this is not the case by Gao’s algebraic characterization of degenerate
subvarieties [23, Theorem 1.1]. Further below, we exclusively work with a ﬁxed
archimedean place ν and, for the purposes of this article, degeneratedness could
be also simply understood as with respect to this place.
With these preparations, we can state the ﬁrst conjecture studied in this arti-
cle.
Relative equidistribution conjecture (REC). Let X ⊆ A be a non-
degenerate geometrically irreducible subvariety. For each place ν ∈ Σ∞(K), there
exists a measure µν on X an
Cν with the following property: If (xi) is an X-generic
subsequence of closed points in X such that ̂h(xi) ! ̂h(X), then

(2) 1
#Oν(xi)
 ∑

x∈Oν (xi) f (x) −! ∫

X an
Cν f µν, i ! ∞,

for every compactly supported continuous function f : X an
Cν ! R.

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 3

If the base variety S in (REC) is a single point, the conjecture specializes to
the classical equidistribution conjecture, which is a result of Szpiro, Ullmo, and
Zhang [86] if the place ν is archimedean. In addition, Yuan’s bigness theorem
[93] implies (REC) in the case of non-archimedean places ν ∈ Σf (K). The non-
degeneracy condition is always satisﬁed in the classical case, but some condition
is deﬁnitely needed in the general case. Indeed, if X is the total space of a
trivial family A = A0 × P1
Q whose ﬁber is an abelian variety A0 over Q, then
one can easily pick an inﬁnite sequence of torsion points in the ﬁber over each
q ∈ P1(Q). For each of these sequences, the Galois orbits of their elements are all
contained in the same ﬁber. Combining them, one can obtain generic sequences
of closed points in A whose averaged Galois orbits cannot converge weakly to any
ﬁxed measure. Indeed, one has complete control over the associated pushforward
measures on P1(Q).
The author cannot rule out that (REC) is empty if ̂h(X) > 0, as there may be
no non-degenerate subvariety X ⊂ A enjoying an X-generic sequence (xi) with
̂h(xi) ! ̂h(X) > 0. However, there are plenty of non-degenerate subvarieties
X ⊆ A containing a Zariski-dense set of torsion points, namely all non-degenerate
subvarieties X with dim(X) = dim(A) − dim(S). A well-studied example are
the sections of families of elliptic curves [12]. In stark contrast to the case
dim(S) = 0, these do not all necessarily come from subgroup schemes of A, all
of which can be formally seen to have zero height. By the following theorem,
the said non-degenerate subvarieties also satisfy ̂h(X) = 0 and hence provide
non-trivial examples of (REC). To simplify our exposition, we avoid the more
technical case of non-archimedean places ν ∈ Σf (K). In the following, the symbol
ν hence always denotes an archimedean place.

Theorem 1. Let X ⊆ A be a geometrically irreducible subvariety with π(X) = S
that is non-degenerate and contains an X-generic subsequence (xi) of points with
̂h(xi) ! 0. Then, we have

̂h(X) = lim
k!∞
 ( hO(1)(X k)

n2k
 )
 = 0

and, for each archimedean place ν ∈ Σ∞(K), there exists a measure µν on X an
Cν
such that (2) holds for every continuous function f : X an
Cν ! R with compact
support.

This theorem generalizes a result of DeMarco and Mavraki [17, Corollary 1.2],
though we impose an additional compact support assumption on the test func-
tions here and restrict to archimedean places. In fact, their result amounts to
the special case where A is a ﬁber product of elliptic families over S and X is the
image of a section of π : A ! S. (Related results can be found in [12].) Their
proof relies on results of Silverman [80, 81, 82] controlling the local N´eron-Tate
height on X near the boundary X \ X where X is the Zariski closure of X in a
certain compactiﬁcation of A. Silverman’s explicit results allow to verify directly

4 LARS K ¨UHNE

that the restriction of the limit N´eron-Tate height to X can be identiﬁed with a
semipositive Arakelov height on X (see [17, Theorem 1.1]). Let us mention that
our height ̂h(X) coincides with their height hP (B).
If dim(X) ≥ 2, this approach seems less feasible as the N´eron-Tate local heights
generally exhibit singularities on compactiﬁcations (e.g., on toroidal compactiﬁ-
cations). Unfortunately, the appearance of these singularities does not seem to be
well-recorded in the literature. The degeneration of the archimedean N´eron-Tate
local heights and their singularities in the case X = A is however well-understood
[8, 9].
Independent from the present work of the author, Yuan and Zhang have re-
cently proven a more comprehensive equidistribution result [92, Theorems 5.4.3
and 6.2.3], which supersedes the above theorem and conﬁrms the conjecture
(REC) more generally for bounded test functions f : X an
Cν ! R. In addition,
Gauthier has also proven a more general equidistribution result [28, Theorem 2],
and both these results cover also non-archimedean places. They also establish
the existence of the measure µν independently from the existence of a sequence
(xi) as in Theorem 1, which our shorter proof does not. However, it is a feature
of our proof as well that the measure µν is the same for any other sequence (x
′
i)
satisfying the conditions of the theorem.
Let us brieﬂy describe the strategy employed in the proof of Theorem 1. The
main idea is to apply equidistribution techniques not directly to any canonical
limit height, but instead to the standard projective heights hO(1) on the subvariety
X k ⊆ PN
K for some suﬃciently large k. For technical reasons, we actually work
with the Zariski closure Y k ⊂ PN
K × PN
K of the graph of the map [n
k]|X : X !
[n
k](X). This circumvents the problem that [n
k]|X may not be an isomorphism.
For the description of our method here, we simply assume that we are in this case
and continue with X k instead of Y k. The X-generic sequence (xi) determines an
X k-generic sequence (x
(k)
i ) by setting x
(k)
i = ι([n
k](xi)).
For equidistribution, we have to control the following two quantities:
(i) the projective height hO(1)(X k), and

(ii) the limit superior lk := lim supi!∞(hO(1)(x
(k)
i )/n
2k).
By means of Zhang’s inequalities [95, Theorem 5.2], it is easy to get some control
on (i) once one controls (ii): The projective height of any point on X k is non-
negative, whence hO(1)(X k) ≥ 0. In the other direction, we have

hO(1)(X k) ≤ lkn
2k

as (x
(k)
i ) is an X k-generic sequence.
Thus it suﬃces to control (ii). Here again, it is clear that lk ≥ 0 so that we
are only in need of an upper bound. For a ﬁxed integer k ≥ 1, we derive such an
estimate in Lemma 18 from a bound on

(3)
 ∣
∣
∣
∣
∣hO(1)(x
(k)
i )

n2k − ̂h(xi)
∣
∣
∣
∣
∣

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 5

that is uniform in i ≥ 1. To explain the origin of such a bound, let us choose an
arbitrary immersion κ : S ֒! PM
K of the base variety and an associated projective
height h on S. Using a result of Manin and Zarhin [54], which we invoke in the
more recent version of [79, Corollary 7.4], the quantity (3) is bounded from above
by c1 · n
−2k max{1, h(π(xi))}
where the constant c1 > 0 depends neither on i nor on k (Lemma 16). This
bound tends to 0 uniformly in i as soon as h(π(xi)) can be uniformly bounded
for all i ≥ 1. This is precisely what a height bound due to Dimitrov, Gao,
and Habegger [19, Theorem 1.6] provides (Theorem 17). These estimates give
us an equidistribution result for (x
(k)
i ) on X k – up to a certain error term that
reﬂects our incomplete control on both (i) and (ii). This translates directly to a
near-equidistribution result for (xi) on X. With suﬃcient bookkeeping, all error
terms can be seen to disappear as k ! ∞, and we obtain (2) asymptotically.
It should be mentioned that a previous article [49] of the author contains
an asymptotic approach in order to prove the equidistribution conjecture for
semiabelian varieties, which does not follow directly from Yuan’s equidistribution
theorem [93]. Apart from the general idea to extend the reach of Yuan’s theorem
through asymptotics and additional arguments tailored to the speciﬁc situation
at hand, the approach here is rather orthogonal to the one in [49]. In fact, the
canonical heights on semiabelian varieties extend well to the boundary of good
compactiﬁcations. Yuan’s theorem can hence be applied, although it does not
yield anything if the chosen compactiﬁcation of the given semiabelian variety
has strictly negative height, which generally cannot be avoided. In contrast,
the conditions of Yuan’s theorem are violated here because the canonical heights
have singularities in general. This accounts for the fact that all arguments in [49]
invoke canonical heights, whereas only approximating projective heights are used
in this article. As a consequence, the common intersection of both arguments is
rather narrow, although the initial idea is identical.
A particular feature of the classical equidistribution conjecture is its close rela-
tion with the Bogomolov conjecture. In fact, Ullmo [87] and Zhang [97] deduced
the Bogomolov conjecture from the equidistribution conjecture. Our applica-
tion of Theorem 1 follows their footsteps. In contrast to the classical setting of
[87, 97], it is necessary in our relative setting to establish that the subvarieties
used are non-degenerate so that it is legitimate to use our equidistribution re-
sult. For this, a consequence [23, Theorem 1.3] (see also the corrigendum [25])
of Gao’s work on the mixed Ax-Schanuel conjecture [24] is a crucial ingredient
that yields immediately what is needed.
The main consequence of our approach being able to work with families of
abelian varieties instead of single ones is that it allows us to improve classical re-
sults of Manin-Mumford and Bogomolov type to uniform results. As a ﬁrst strik-
ing consequence we obtain the following strong version of the Manin-Mumford
conjecture. Note that the uniformity in the genus has not been achieved by any
of the other methods proposed up to the present day [41, 72, 74, 87]. However,

6 LARS K ¨UHNE

uniformity has been achieved under additional restrictions on the Jacobian in
a few particular cases. In the special case that Jac(C) polarized by the theta
divisor ΘC is the self-product of a polarized elliptic curve, the assertion of the
theorem below was proven by David and Philippon [13, Th´eor`eme 1.13]. There
is also a noteworthy result of DeMarco, Krieger, and Ye [16, Theorem 1.1]. They
showed a similar assertion for complex algebraic curves whose Jacobian is an
abelian surface admitting real multiplication by the real quadratic order of dis-
criminant 4 (compare Section 9 of [16]). Apart from these results, the author is
only aware of a result due to Dimitrov, Gao, and Habegger [19, Proposition 8.1],
which requires C to be deﬁned over a number ﬁeld and Jac(C) to have suﬃciently
large “modular height”. We discuss their work in detail further below.

Theorem 2 (uniform Manin-Mumford conjecture). For each g ≥ 2, there exists
an integer c2(g) ≥ 1 such that the following assertion is true: For every smooth
proper genus g curve C deﬁned over C and every divisor D of degree 1 on C, we
have #(ιD(C) ∩ Tors(Jac(C))) ≤ c2(g)

where ιD : C −! Jac(C), q ↦−! [q] − D,

is the Abel-Jacobi embedding sending D to the identity in Jac(C).

Whereas the number of torsion points on ιD(C) ⊆ Jac(C) is uniformly bounded
by the theorem, there can be no uniform bound on their order, even under the
additional restriction D = [p] with a closed point p ∈ C (see [16, Section 9.5] for
a counterexample to such a strengthening).
We actually show a stronger Bogomolov-type result in this article. To state it,
we need to introduce some additional terminology. Details are given at the end of
this introduction. We restrict ourselves to moduli over Q. For an integer n ≥ 3,
let Ag,n denote the ﬁne moduli space of principally polarized abelian varieties
with level n structure and write πg,n : Bg,n ! Ag,n for the associated universal
family of abelian varieties. By Mg,n we denote the ﬁne moduli space of smooth
proper genus g curves with a Jacobi structure of level n. We let τg,n : Mg,n ! Ag,n
be the Torelli map with level n structure. Both Ag,n and Bg,n as well as Mg,n are
actually quasi-projective varieties over Q, and τg,n : Mg,n ! Ag,n is a morphism
between Q-varieties.
For every s ∈ Mg,n(Q), all points q ∈ Cg,n,s(Q) and any divisor D of de-
gree 1 on Cg,n,s, the diﬀerence [q] − D can be considered as a Q-point of the
Jacobian Jac(Cg,n,s), which is canonically a subvariety of Bg,n. Having chosen
an immersion ι : Bg,n ֒! PN
Q , we can hence assign a height ̂h([q] − D) to this
diﬀerence.

Theorem 3 (uniform Bogomolov conjecture). Let g ≥ 2 and n ≥ 3 be integers,
and let ι : Bg,n ֒! PN
Q be an immersion. There exist constants c3 = c3(g, n, ι),
c4 = c4(g, n, ι) > 0 for which the following assertion is true: For each s ∈

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 7

Mg,n(Q) and every divisor D of degree 1 on the curve Cg,n,s, we have

(4) # {
q ∈ Cg,n,s(Q) ∣
∣
∣ ̂h([q] − D) ≤ c3} < c4.

In Section 4, we deduce this theorem from Proposition 26, which is an analogue
assertion on more general families of smooth proper algebraic curves of genus g
instead of universal ones. Let us remark that conversely this proposition could
be also easily deduced from Theorem 3. However, the proposition is amenable
to a proof by induction on the dimension of the base and we rely on this fact for
our proof.
A related uniform bound on the essential height minima of smooth algebraic
curves of a ﬁxed genus g has been published recently by Wilms [91, Corollary 1.5].
However, it seems not yet to imply our proposition because a uniform treatment
of points of height below the essential minimum is needed. More recently, Looper,
Silverman, and Wilms [53] have obtained a proof of the function ﬁeld case of
Theorems 2 and 3 with explicit constants, using the same approach as in [91].
In any case, the methods used in their approach and the one here seem rather
disjoint. Wilms’ argument uses explicit height computations and comparisons in
the setting of Jacobian embeddings, whereas our Proposition 26 is not restricted
to this setting. It should also be said that we opted for a simpler proof at the cost
of introducing some additional assumptions in the proposition (e.g., the existence
of a principal polarization). The reader interested in the most general result is
referred to meanwhile ﬁnished work of Gao, Ge, and the author [27].
Our Theorem 3 should be also compared with a recent result by Dimitrov,
Gao, and Habegger [19, Proposition 7.1]. In the setting of the theorem, they
proved that there exist constants c5 = c5(g, n, ι), c6 = c6(g, n, ι), c7 = c7(g, n, ι),
c8 = c8(g, n, ι) > 0, a projective compactiﬁcation Ag,n of Ag,n, and an ample line
bundle M on Ag,n with an associated Weil height hM : Ag,n(Q) ! R such that
the following is true: For each s ∈ Mg,n(Q) such that hM (τg,n(s)) ≥ c5, there
exists a ﬁnite subset Ξs ⊆ Cg,n,s(Q) of cardinality ≤ c6 such that

(5) # {
q ∈ Cg,n,s(Q) ∣
∣
∣ ̂h(q − p) ≤ c7 · hM (τg,n(s))} < c8

for all p ∈ Cg,n,s(Q)\Ξs. (It should be said that [19] uses a speciﬁc compactication
endowed with an ample line bundle, but this is immaterial by [90, Proposition
2.3].) Whenever the “modular height” hM (τg,n(s)) is large enough, this implies
a uniform bound on #(ι[p](C) ∩ Tors(Jac(C))). However, the argument in [19]
yields nothing if hM (τg,n(s)) < c5.
It has been already implicit in [18, 19, 20] that a combination of the cardinality
bounds in (4) and (5) can be used to obtain a uniform version of the Mordell-Lang
conjecture [20, Conjecture 1.1] through R´emond’s explicit versions of Mumford’s
[60, 75] and Vojta’s inequality [76, 89] (see [18, Section 2]). As a question, it
seems to be originally due to Mazur (see the question on [56, p. 234] as well as
the discussion on [57, p. 223]).

8 LARS K ¨UHNE

Theorem 4 (uniform Mordell-Lang conjecture). For each g ≥ 2, there exists a
constant c9(g) > 0 such that the following assertion is true: For every smooth
proper genus g curve C, every divisor D of degree 1 on C, and every subgroup
Γ ⊂ Jac(C)(C) of ﬁnite rank ̺, we have

(6) #(ιD(C) ∩ Γ) ≤ c9(g)1+̺

where ιD : C −! Jac(C), q ↦−! [q] − D,
is an Abel-Jacobi embedding.

The choice Γ = Tors(Jac(C)) leads back to Theorem 2. Choosing instead
Γ = Jac(C)(K) for a smooth algebraic curve C deﬁned over K with Mordell-
Weil rank ̺, we obtain the rather uniform bound

#C(K) ≤ c10(g)1+̺

on the number of rational points. A weaker bound

#C(K) ≤ c11(g, [K : Q])1+̺

has been already obtained by Dimitrov, Gao, and Habegger [19]. It is not sur-
prising that their proof rests on (5). Furthermore, Stoll [85] used the Chabauty-
Coleman method [10, 11] to prove a bound of the form

(7) #C(K) ≤ c12(g, [K : Q])

if C is a hyperelliptic curve of genus g with Mordell-Weil rank ̺ ≤ (g − 3).
The condition that C is a hyperelliptic curve was lifted later by Katz, Rabinoﬀ,
and Zureick-Brown [44]. Without any assumption on the Mordell-Weil rank ̺,
they also obtained a uniform bound on the number of K-rational torsion points
contained in ιD(C), which was already superseded by the results of [19]. The
bounds in [44, 85] are very explicit and rather small. In contrast, it seems still
an open problem to prove that the constant c9(g) in our theorem is eﬀectively
computable.
We do not give a deduction of Theorem 4 from the cardinality bounds (4)
and (5) since there would be nothing to add to [18, 19, 20] or [71]. In fact, the
proof is a straightforward adjustment of the proof of [19, Proposition 8.1] from
[19, Proposition 7.1]. The reader can ﬁnd this adapted proof in [20, Section
2.4] and consult [20, Section 3] for the specialization argument from C to Q. In
fact, a combination of (4) and (5) yields the assertion of Proposition 2.5 in loc.
cit. unconditionally (i.e., without assuming the relative Bogomolov conjecture).
This renders the proof of Conjecture 1.1 in loc. cit., which corresponds to our
Theorem 4, unconditional. The proof rests on previous work of (in chronological
order) Mumford [60], Vojta [89], Bombieri [5], Faltings [21], R´emond [75, 76], as
well as Dimitrov, Gao, and Habegger [18, 19]. Furthermore, Gao has meanwhile
written a comprehensive survey [26].
The author’s original motivation to prove Theorem 1 was the relative Bogo-
molov conjecture [20, Conjecture 1.2], which is the Bogomolov-type analogue of

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 9

Pink’s relative Manin-Mumford conjecture [73, Conjecture 6.2] and is also re-
lated to a conjecture in Zhang’s ICM talk [98]. In fact, Theorem 1 can be used
to aﬃrm this conjecture for all subvarieties in ﬁbered products of elliptic families,
generalizing [17, Theorem 1.4]. The reader can ﬁnd details in the separate article
[50].
Finally, it should be said that the results of both Bogomolov type as well as of
Mordell-Lang type presented here have been extended beyond curves in a recent
joint work with Gao and Ge [27]. In the case of curves, Yuan [92] also obtained
improved versions of our Theorems 2 and 3 by a diﬀerent approach.
Notation and conventions. General. For two terms a and b, we write a ≪ b
if there exists a positive real number c such that a ≤ c · b. If c depends on some
data, say an algebraic variety X, we write a ≪X b etc. We use ≫ similarly.
In each of the following sections, we may suppress the dependence of constants
on some basic data for readability. Where this is done, it is indicated at the
beginning of the respective section.
Number ﬁelds. Throughout this article, we let K denote a number ﬁeld with
integer ring OK. In addition, Σf (K) (resp. Σ∞(K)) is the set of non-archimedean
(resp. archimedean) places, and we set Σ(K) = Σf (K) ∪ Σ∞(K). By Cν is de-
noted a completion of an algebraic closure K ν of Kν, and by pν the residue
characteristic of Cν. For all ν ∈ Σf (K), the absolute value | · |ν on Cν is normal-
ized such that |pν|ν = p−[Kν:Qpν ]
ν . We use the standard absolute values on R and
C for the archimedean places. This normalization leads to an additional factor

δν =
 {
2 if ν is complex archimedean,
1 otherwise,

in some identities.
Algebraic geometry (General). Denote by k an arbitrary ﬁeld. A k-variety
is a separated, reduced scheme of ﬁnite type over k. By a subvariety of a k-
variety we mean a closed reduced subscheme. A subvariety is determined by
its underlying topological space and we frequently identify both. The tangent
bundle of a k-variety X is written T X and its ﬁber over a point x ∈ X is denoted
by TxX. Furthermore, X sm denotes the smooth locus of X. If X is an irreducible
k-variety, we write ηX for its generic point.
For a non-negative integer d and a k-variety X, a d-cycle on X is a ﬁnite
formal sum ∑r
i=1 ni[Zi] where each ni is an integer and each Zi is a k-irreducible
subvariety of X having dimension d.
For a map f : X ! Y between algebraic varieties and a point y ∈ Y with
residue ﬁeld k(y), we write Xy for the ﬁber X ×Y Spec(k(y)) over y. We use a
similar notation for S-points y ∈ Y (S), S an arbitrary scheme.
Generic sequences. Let X be an irreducible algebraic k-variety. We say that
a sequence (xi) ∈ X N of closed points is X-generic if none of its subsequences is
contained in a proper algebraic subvariety of X. If the variety X can be inferred
from context, we simply say generic instead of X-generic.

10 LARS K ¨UHNE

Line bundles and intersection theory. For line bundles L1, L2, . . . , Ld on a
proper algebraic variety X of dimension d over a ﬁeld k, we use the intersection
numbers L1 · L2 · · · Ld ∈ Z
deﬁned by Kleiman [45] and Snapper [83] (see [47, Section VI.2] for a good
introduction). These coincide with the numbers

deg(c1(L1) ∩ c1(L2) · · · ∩ c1(Ld) ∩ [X]) ∈ Z

in the terminology of [22]. If {M1, M2, . . . , Mr} = {L1, L2, . . . , Ld} and each Mi
occurs precisely ni times among L1, L2, . . . , Ld, we set

M n1
1 · M n2
2 · · · M nr
r := L1 · L2 · · · Ld.

A similar notation is used for the arithmetic intersection numbers deﬁned in
Subsection 1.2. Furthermore, we write degL(X) for L
d.
The group law of Picard groups of line bundles, as well as of their arithmetic
analogue introduced in Subsection 1.1, is written additively.
Continuous functions. We use C 0 as an abbreviation for continuous. For
any topological space X, C 0(X) denotes the real-valued continuous functions
on X and C 0
c (X) the real-valued continuous functions on X having compact
support. We use the analogous notation C ∞ for the real-valued smooth functions
on complex spaces that are introduced below.
Tangent spaces. For each diﬀerentiable or real-analytic manifold M we denote
by T M its tangent bundle. The ﬁber of T M over x ∈ M is denoted TxM.
Let M be a complex manifold (e.g., (X sm)an
Cν for an algebraic variety X over
K and some ν ∈ Σ∞(K)). To M is associated its real tangent bundle TRM and
its holomorphic tangent bundle T 1,0
C M (e.g., the analytiﬁcation (T X)an of the
tangent bundle of a smooth complex algebraic variety X). The reader is referred
to [33, Section 0.2] and [42, Section 1.2] for details.
Complex spaces. Let M be a reduced complex (analytic) space (e.g., X an
Cν for
a K-variety X and some ν ∈ Σ∞(K)). Recall that this means that M is locally
biholomorphic to a closed analytic subvariety V of a complex domain U ⊂ Cn.
A function f on M is smooth if, for each such suﬃciently small local chart, it
is the restriction of a smooth function on U. We write C ∞(M) for the smooth
real-valued functions on M. In the same way, we use local charts to deﬁne
plurisubharmonic functions on M as restrictions of plurisubharmonic functions.
Similarly, a smooth form ω on M is a diﬀerential form on the smooth locus
M sm of M with the following extension property: M can be covered by local
charts V ⊂ U ⊂ Cn as above such that for each chart the diﬀerential form ω|V sm
is the restriction of a C ∞-diﬀerential form on U. There are also well-deﬁned
linear operators d and dc = i/2π(∂ − ∂) on the C ∞-diﬀerential forms on M.
1 For
each local chart V ⊂ U ⊂ Cn, these are simply the restrictions of the operators
of the same name on Cn. Recall that for every reduced complex space M of

1Note that there are diﬀerent deﬁnitions of d
c in the literature. Many texts on Arakelov
theory (e.g. [38, 59, 84]) use d
c = i/4π(∂ − ∂).

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 11

dimension d and every smooth (d, d)-form ω, the integral ∫

M ω is well-deﬁned
by classic work of Lelong [51]. In fact, this integral is by deﬁnition the ordinary
integral ∫

M sm ω over a(n in general non-compact) complex manifold M sm, whose
ﬁniteness is proven in [51].
We remark that the usual rules for integration on complex manifolds still
apply for reduced complex spaces and we use them without further comment.
In particular, let f : M ! N be a ﬁnite branched holomorphic covering of pure
order q (see [39, Chapter C] for deﬁnitions) between reduced complex analytic
spaces of (necessarily the same) dimension d: Let η (resp. η′) be a smooth (d, d)-
form on M (resp. N) such that η = f ∗η′. Then,

(8) ∫

M η = ∫

M sm η = ∫

M sm∩f −1(N sm) η = q ∫
N sm∩f (M sm) η′ = q ∫

N sm η′ = q ∫

N η′.

Here, the equalities follow from the deﬁnitions, discarding or adding a null set,
and the ordinary substitution rule in the smooth setting.
Moduli spaces of abelian varieties. We work with certain moduli functors on
schemes over Q. Note that for every abelian schemes π : A ! S, there exists
a dual abelian scheme A
∨ by [65, Corollary 6.8].2 With a scheme S over Q,
we associate similar to [65, Deﬁnition 7.2] the set Ag,d,n(S) consisting of triples
(π, λ, σ) where

(i) π : A ! S is an abelian scheme of relative dimension g;
(ii) λ : A ! A
∨ is a polarization ([31, Deﬁnition 27.280]) of degree d2 (i.e.,
λ∗OA is locally free of rank d2);
(iii) σ : A[n] ∼
−! (Z/nZ)2g
S is an isomorphism of ﬁnite ﬂat group schemes
over S that respects the sympletic structures on both sides. Here A[n]
is endowed with the symplectic structure induced by the Weil pairing
whereas (Z/nZ)2g
S is endowed with the standard sympletic structure.3

In the obvious way, this assignment is functorial. If n ≥ 3, it is a smooth quasi-
projective variety (see [65, Theorem 7.9] and the “lemma of Serre” [78]). The
associated universal family of abelian varieties is written πg,d,n : Bg,d,n ! Ag,d,n.
In [67, Theorem 2.1.11], it is deduced from the results of [65] that the functor
Ag,d,n is still a smooth Deligne–Mumford stack over Q. We write Ag,n, Bg,n, πg,n
instead of Ag,1,n, Bg,1,n, πg,1,n.
The kernel ker(λ) of any polarization λ : A ! A
∨ of degree d2 is a ﬁnite
locally free group scheme ([31, Corollary 27.177]). If S is connected, there exists
a unique tuple
 ∆ = (δ1, . . . , δg)

2Note that [65, Chapters 6 and 7] work only with locally noetherian schemes. However,
this can be dropped as every abelian scheme is the base change of an abelian scheme over a
Z-algebra of ﬁnite type (compare [63, footnote on p. 76]).
3Note that the level structure in [65] disregards sympletic structures. We do not follow this
here as the sympletic structure ﬁts with the Jacobi structures used for moduli of curves in [14].

12 LARS K ¨UHNE

with positive integers δi satisfying δi | δi+1 (1 ≤ i < g) such that, for every
geometric point s of S, the kernel of λs : As ! A
∨
s is isomorphic to the constant
group scheme ∏g
i=1(Z/δiZ)2
s. This follows, for example, by combining [68, Lemma
2.1.9], [61, Corollary of Theorem 1] and [63, Proposition 1]. Necessarily, we have
d = δ1 · δ2 · · · δg. We call ∆ the type of the polarization.
For any ∆ as above, we deﬁne Ag,∆,n as the subfunctor of Ag,d,n comprising
triples (π, λ, σ) such that the polarization λ is of a given type ∆. As the type
of a polarization is locally constant by the above, this induces a partition of
Ag,d,n into open substacks Ag,∆,n. As Ag,d,n is a smooth quasi-projective variety
over Q if n ≥ 3, each Ag,∆,n is a smooth quasiprojective variety over Q as
well. These varieties are of particular interest for us as their associated complex
analytic spaces Aan
g,∆,n,C have a complex uniformization by the Siegel modular
upper half-space

Hg = {
τ ∈ Cg×g ∣
∣ τ = τ t and Im(τ ) ∈ Rg×g positive deﬁnite}

of degree g. Recall that Hg is endowed with a standard action of Sp2g(Z). In fact,
the complex manifold Aan
g,∆,n,C is the quotient of Hg by the subgroup Γ∆∩Γ(N) ⊆
Sp2g(Z) where

Γ∆ = {
A ∈ Sp2g(Z) | A ( 0g×g diag(∆)
diag(∆) 0g×g
 ) At = ( 0g×g diag(∆)
diag(∆) 0g×g
 )}

and Γ(N) is the kernel of the reduction Sp2g(Z) ! Sp2g(Z/NZ). The universal
family over Aan
g,∆,n,C descends from the universal family πg,∆ : Ag,∆ ! Hg of
complex abelian varieties with polarization type ∆ over the Siegel modular upper
half-space deﬁned in [4, Section 8.1]. Furthermore, a line bundle Lg,∆ ! Ag,∆
inducing the given polarization is constructed in [4, Section 8.7].
Moduli spaces of curves and the Torelli map. Let Mg,n denote the moduli
stack over Q parameterizing geometrically irreducible smooth projective curves
with Jacobi structure of level n (as in [14, (5.14)]) and write π′
g,n : Cg,n ! Mg,n
for the universal family over Mg,n. If n ≥ 3, Mg,n is a smooth quasi-projective
variety (again by Serre’s lemma [78]). Associating to a curve its Jacobian induces
a morphism τg,n : Mg,n ! Ag,n of stacks, the Torelli map with level n structure
(compare [70]).
 1. Heights

In this section, we brieﬂy review heights and their basic properties as we
need them. We closely follow the notations introduced in [49, Section 2], and
we refer to there for a detailed exposition of arithmetic intersection theory [30]
in the setting needed here. Primary sources for arithmetic intersection theory
include [7, 21, 30, 37, 38, 93, 95, 96]. Furthermore, we mention the introductory
textbooks [59, 84].
Recall that K is a number ﬁeld with integer ring OK. We consider a ﬂat,
integral, projective OK-scheme X of relative dimension d over OK. Its generic

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 13

ﬁber X ⊆ PN
K is an irreducible, projective K-variety. In this setting, we say that
X is a OK-model of X.

1.1. Hermitian line bundles on arithmetic varieties. A C ∞-hermitian line
bundle L on X is a collection (L, {∥·∥ν}ν∈Σ∞(K)) consisting of a line bundle L on
X and a C ∞-hermitian metric ∥ · ∥ν : Lan
Cν ! R for each ν ∈ Σ∞(K). If Kν = R,
we assume additionally that the ν-metric is invariant under Gal(Cν/Kν) (i.e.,
under complex conjugation on X an
Cν ). We say that L is vertically semipositive if
L is relatively nef with respect to X ! Spec(OK) (i.e., its restriction to every
ﬁber is nef) and each C ∞-hermitian metric ∥ · ∥ν, ν ∈ Σ∞(K), is semipositive
(i.e., its associated Chern form is semipositive
4).
Two hermitian line bundles L and M are called isometric if there is an iso-
morphism L ≈ M preserving the metrics at all archimedean places. The arith-
metic Picard group ̂PicC ∞(X) is the set of isometry classes of C ∞-hermitian line
bundles on X. For L, M ∈ ̂PicC ∞(X), we deﬁne L + M, −L as elements of
̂PicC ∞(X) in the obvious way, obtaining a group structure on ̂PicC ∞(X). Given a
morphism f : Y ! X of ﬂat, integral, projective OK-schemes, we deﬁne similarly
the pullback f ∗L ∈ ̂PicC ∞(Y) of any L ∈ ̂PicC ∞(X).
The notion of vertical semipositivity introduced above descends to the isomor-
phism classes in ̂PicC ∞(X). It further extends to ̂PicC ∞(X)Q = ̂PicC ∞(X) ⊗Z Q.
The elements of ̂PicC ∞(X)Q are called the C ∞-hermitian Q-line bundles on X.
Every C ∞-hermitian line bundle L on X gives rise to a metrized line bundle
LK on X. Such line bundles are called algebraically metrized (see [49, Section
2.5] for details). In addition, the metrized line bundle LK is vertically semiposi-
tive in the sense of [49, Section 2.5] if L is so in the sense introduced above. (We
do not claim the converse implication.) Furthermore, we note that LK is verti-
cally integrable in the sense of [49, Section 2.5] for every C ∞-hermitian line bun-
dle L on X. In fact, we can always write L as a diﬀerence (L+O(k)|X)−O(k)|X
with O(k) being the C ∞-hermitian line bundle on PN
OK deﬁned below. For suﬃ-
ciently large integers k, both terms are semipositive because O(k) is ample and
the metric on O(k) is strictly positive.
Let us deﬁne the basic C ∞-hermitian line bundles that we use in this work.
We consider the line bundle O(1) on PN
OK where N is a positive integer. For
each archimedean place ν ∈ Σ∞(K), we endow the holomorphic line bundle
O(1)an
Cν on PN
Cν with the Fubini-Study metric ∥ · ∥FS,ν (see [88, Subsection 3.3.2]
for a deﬁnition). The Fubini-Study metric is smooth, so that we obtain a C ∞-
hermitian line bundle O(1) = (O(1), {∥·∥FS,ν}ν) ∈ ̂PicC ∞(PN
OK ). For every integer
k, we set O(k) := k · O(1). We write O instead of O(0). As the Chern form ωFS
of the Fubini-Study metric is a strictly positive C ∞-hermitian form, each O(k)
is vertically semipositive if k ≥ 1. Note that we suppress the dimension N here,
as it will be always clear from context. On a biprojective space PN1
OK × PN2
OK ,

4The reference [49] contains a typo (a superﬂuous dd
c) in the deﬁnition of semipositivity.

14 LARS K ¨UHNE

we consider the C ∞-hermitian line bundles O(k1, k2) = pr∗
1O(k1) + pr∗
2O(k2) ∈
̂PicC ∞(PN1
OK × PN2
OK ) where pri : PN1
OK × PN2
OK ! PNi
OK , i ∈ {1, 2}, is the projection to
the i-th factor and k1, k2 are arbitrary integers.
Consider next the C ∞-hermitian line bundle (OX, {| · |ν}) where the hermitian
metrics | · |ν, ν ∈ Σ∞(K), are the trivial metrics. For a place ν ∈ Σ∞(K) and
a Gal(Cν/Kν)-invariant function f ∈ C ∞(X an
Cν ), we deﬁne furthermore O(f ) =
(OX, {∥ · ∥ν}) by setting ∥ · ∥ν = e
−f | · |ν and ∥ · ∥µ = | · |µ for all places µ ∈
Σ∞(K) \ {ν}. For a general L ∈ ̂PicC ∞(X), we set L(f ) = L + O(f ).

1.2. Arithmetic intersection numbers. Given L1, . . . , Ld′+1 ∈ ̂PicC ∞(X),
an arithmetic intersection number

(9) L1 · L2 · · · Ld′+1 · Z ∈ R

is deﬁned in [49, Section 2.6] for every d′-cycle Z on X. To simplify our notation,
we write just L1 · L2 · · · Ld+1
if additionally d = d′ and Z = [X]. Note that the deﬁnition of (9) in [49] relies on
Gubler’s theory of local heights [36, 37, 38]. As we only work with C ∞-hermitian
line bundles on arithmetic varieties, the “global” approach as in [7, 30, 84] would
be suﬃcient as well, and both approaches yield the same intersection numbers
([38, Remark 11.24]).
For convenience of the reader, we brieﬂy recall some properties of arithmetic
intersection numbers as a lemma.

Lemma 5. Let L1, . . . , Ld+1, L′
1 ∈ ̂PicC ∞(X) be vertically integrable.
(a) (Multilinearity) We have

(L1 + L′
1) · L2 · · · Ld+1 = L1 · L2 · · · Ld+1 + L′
1 · L2 · · · Ld+1.

(b) (Commutativity) For any permutation σ : {1, . . . , d + 1} ! {1, . . . , d + 1},

Lσ(1) · Lσ(2) · · · Lσ(d+1) = L1 · L2 · · · Ld+1.

Proof. These are just the ﬁrst two assertions from [49, Lemma 2.3]. □

We conclude with a further observation: Let ν ∈ Σ∞(K) be an archimedean
prime and let f ∈ C ∞(X an
Cν ). For all i ∈ {1, . . . , d + 1} and

L1 = (L1, {∥ · ∥1,ν}), . . . , Ld+1−i = (Ld+1−i, {∥ · ∥d+1−i,ν}) ∈ ̂PicC ∞(X),

we have

(10) L1 · L2 · · · Ld+1−i · OX(f )i

= δν
 ∫

X an
Cν f (ddcf )i−1 ∧ c1(∥ · ∥1,ν) ∧ c1(∥ · ∥2,ν) ∧ · · · ∧ c1(∥ · ∥d+1−i,ν)

by [49, Equation (2.3) in Subsection 2.6]5.

5Note that this equation contains a typo on its left-hand side, which should be read as
L1 · L2 · · · Ld+1−i · OX(f )
i.

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 15

Lemma 5 (a) allows to linearly extend the deﬁnition of the arithmetic inter-
section number to all elements of ̂PicC ∞(X)Q.

1.3. Heights. Let L = (L, {∥ · ∥ν}ν∈Σ∞(K)) ∈ ̂PicC ∞(X) be a C ∞-hermitian
line bundle on X. Assume that the generic ﬁber L = LK is ample. For each
irreducible subvariety Y ⊂ X of dimension d′, its Zariski closure Y in X is a ﬂat,
irreducible OK-scheme of relative dimension d′ (see e.g. [52, Proposition 4.3.9 and
Corollary 4.3.14]). Using the arithmetic intersection numbers introduced in the
last subsection, we deﬁne the height

hL(Y ) = (L|Y)d′+1

[K : Q](d′ + 1) degL(Y ) .

We can make this deﬁnition more explicit if Y is a closed point x ∈ X. Writing
x for the closure of x in X, the above deﬁnition simpliﬁes to

hL(x) = L|x
[K(x) : Q]

in this case. For every non-zero rational section s of L such that x ∩|div(s)| = ∅,
this equals

(11) hL(x) = 1
[K(x) : Q]
 

log #(L|x/(s|x)) − ∑

ν∈Σ∞(K)
 ∑

y∈Oν (x) δν log ∥s(y)∥ν


 .

1.4. Arithmetic volumes and Minkowski’s Theorem. Let

L = (L, {∥ · ∥ν}ν∈Σ∞(K))

be a C∞-hermitian line bundle on X. For each integer N ≥ 0, we consider the
isomorphism

VN,R = H 0(X, L⊗N ) ⊗Z R −! ∏

ν∈Σ∞(K) H 0(XCν , L⊗N
Cν ).

Indeed, this generalizes a well-known isomorphism from Minkowski’s geometry of
numbers (compare [66, Section I.5]).6 For each ν ∈ Σ∞(K), we can additionally
endow H 0(XCν , L⊗N
Cν ) with a sup-norm by setting

∥s∥(∞)
ν = max
x∈X an
Cν {∥s(x)∥⊗N
ν }

for every s ∈ H 0(X, L⊗N ). By restriction, we obtain a seminorm
7 on VN,R. With
these seminorms, we can deﬁne the unit ball

BN = {s ∈ VN,R | ∀ν ∈ Σ∞(K) : ∥s∥(∞)
ν ≤ 1}.

6Note that we only have one factor for each complex archimedean place on the right-hand
side here, so there is no action via complex conjugation in contrast to [66].
7This is indeed only a seminorm as the following example, suggested by the referee shows.
If K = Q(
√
2), X = OK, L = OX, then ∥√
2 ⊗ 1 − 1 ⊗ √
2∥∞
ν = ∥0∥∞
ν = 0 for one archimedean
place ν ∈ Σ∞(K).

16 LARS K ¨UHNE

We let volN (·) be the unique Haar measure on VN,R such that the induced quotient
measure on VN,R/VN,Z has total mass 1. The arithmetic volume of L ∈ ̂PicC ∞(X)
is deﬁned by
 ̂volχ(L) = lim sup
N !∞ log volN (BN )
N d+1/(d + 1)! .

By [43, Corollary 3.2.2], we have ̂volχ(L) < ∞.
Arithmetic volumes enter our proof of Theorem 1 through the construction
of global sections with small supremum norms via Minkowski’s Theorem. We
summarize this in the following lemma.

Lemma 6. Let ν ∈ Σ∞(K) and a real ε > 0 be given. Assume that the generic
ﬁber L = LK is nef and big. Then, there exists an integer N0 and a non-zero
section s ∈ H 0(X, L⊗N0) such that

δν log ∥s∥(∞)
ν ≤
 (

− ̂volχ(L)
(d + 1)Ld + ε
)
 N0

and
 log ∥s∥(∞)
µ ≤ 0

for all other µ ∈ Σ∞(K) \ {ν}.

Proof. This is a well-known consequence of Minkowski’s Second Theorem [6,
Theorem C.2.11]. See e.g. [49, Lemma 2.7] for a deduction in the slightly more
general setting of adelically metrized line bundles. □

2. The Equilibrium measure

In this section, we describe – up to a proportionality factor appearing in
Lemma 25 below – the equilibrium measure µν postulated in Theorem 1, estab-
lishing also some essential lemmas for its proof in the next section. In contrast to
the rest of the article, we work here with a smooth, irreducible complex variety S,
a family π : A ! S of complex abelian varieties of relative dimension g, an irre-
ducible subvariety X ⊆ A of dimension d such that π(X) = S, and an immersion
ι : A ֒! PN
C . Notationally, we identify the complex-analytic spaces associated
with complex algebraic varieties with their sets of complex-valued points.
We assume throughout this section that the line bundle ι
∗O(1) is ﬁberwise
symmetric (i.e., ι
∗O(1)|s is a symmetric line bundle on A|s for every s ∈ S(C)).
In addition, we let

∆ = (δ1, δ2, . . . , δg) ∈ Z
g, δi | δi+1 (1 ≤ i < g),

denote the type of the polarization λ : A ! A
∨ induced by ι
∗O(1).
All constants, whether implicit or explicit, are allowed to depend on the data
introduced so far without further mention.

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 17

Let ωFS denote the Fubini-Study form on PN (C). For each integer k ≥ 0, we
consider the (1, 1)-form
 αk = (ι ◦ [n
k])∗ωFS
n2k

on A(C). Note that αk+l = ([n
l]
∗αk)/n
2l for all integers k, l ≥ 0.

Lemma 7. There exists a semipositive, smooth, closed (1, 1)-form β on A(C)
such that, for every irreducible subvariety X ⊆ A of dimension d and every
compactly supported continuous function f : X(C) ! R, we have

(12) lim
k!∞
 ∫
X(C) f α∧d
k = ∫

X(C) f β∧d.

Furthermore, [n]∗β = n
2 · β.

In the next section, we prove that, for a non-degenerate subvariety X, the
measure β∧d on X(C) is indeed proportional to the equilibrium measure µν in
Theorem 1.

Proof. To ease notation, we write L instead of ι
∗O(1) and ∥ · ∥ : L(C) ! R≥0 for
the hermitian metric induced by the Fubini-Study metric on O(1).
By the theorem of the cube ([64, Corollary 3 on p. 59]), we have L|⊗n2
π−1(s) ≈
[n]
∗L|π−1(s) for every point s ∈ S(C). A suﬃciently general version of the seesaw
theorem ([31, Theorem 24.66]) implies that L
⊗n2 ⊗ [n]
∗L
⊗−1 is the pullback of a
line bundle on S. Hence, every point s0 ∈ S(C) has a Zariski-open neighborhood
U ⊆ S such that there exists an isomorphism ψ1 : L|⊗n2
π−1(U ) ! [n]∗L|π−1(U ).

For each integer k ≥ 0, this induces further an isomorphism ψk : L|⊗n2k
π−1(U ) !
[n
k]
∗L|π−1(U ). We obtain a smooth hermitian metric ∥ · ∥k : L(C)|π−1(U ) ! R≥0

by demanding

(13) ∥s∥n2k
k = [n
k]
∗∥ψk ◦ s
⊗n2k∥

for every meromorphic section s of L(C)|π−1(U ) where

[n
k]
∗∥ · ∥ : [n
k]∗L(C) −! R≥0

denotes the pullback of the metric ∥ · ∥ on L(C) along [n
k]. Let K ⊆ U(C)
be a compact neighborhood of s0. The function ∥s∥2/∥s∥1 : π−1(K) ! R>0 is
independent of the chosen meromorphic section s. Since it is continuous, it is
uniformly bounded. A version of Tate’s limiting argument (compare the proof
of [96, Theorem 2.2]) shows that there exists a (unique) hermitian metric ∥ · ∥∞
on L(C)|π−1(K) such that ∥s∥k/∥s∥∞ ! 1 uniformly on π−1(K) as k ! ∞.
Let V ⊂ A(C) be an open set such that V ⊂ π−1(K). By choosing V small
enough, we can assure that there exists a holomorphic section s of L(C) over V
such that (− log ∥s∥k) is uniformly bounded on V for all k ≥ 1. Then, we have

ddc(− log ∥s∥k) = n
−2kddc(− log([n
k]
∗∥ψk(s
⊗n2k )∥)) = αk|V .

18 LARS K ¨UHNE

Set β|V = ddc(− log ∥s∥∞). The uniform convergence ∥s∥k ! ∥s∥∞ implies by
[15, Corollary 1.6]8 that, for any continuous function f : X(C) ! R with compact
support in V , we have

(14) ∫

X(C) f α∧d
k −! ∫

X(C) f (β|V )∧d, k ! ∞.

We claim that the currents β|V constructed in this way for varying V glue to a
(1, 1)-current β on A. For this purpose, it suﬃces to show that a diﬀerent choice
of ψ1 gives rise to the same current β|V . In fact, any other choice is of the form
φ · ψ1 where φ is a non-zero holomorphic function on π−1(U). By compactness,
the function φ has to be constant on any ﬁber of π. The argument from [96]
shows that the quotient of the two respective limit metrics is |φ|1/n2. Thus, the
uniqueness of β|V follows from the calculation

ddc log |φ|1/n2 = 1
2n2 · (ddc log φ + ddc log φ) = 0.

A straightforward partition of unity argument allows to deduce (12). Further-
more, the homogeneity relation [n]
∗β = n
2 · β follows from (13).
It remains to verify that β is a smooth diﬀerential form. Each point s0 ∈ S(C)
has a simply connected open neighborhood U ⊆ S(C) such that there exists a
holomorphic map c : U ! Hg for which A(C)|U is the pullback of the family
πg,∆ : Ag,∆ ! Hg. Write ϕ : A(C)|U ! Ag,∆ for the associated map. Recall that
Lg,∆ is the line bundle on Ag,∆ constructed in [4, Section 8.7]. By [4, Theorem
2.2.3], the restrictions of ϕ∗L
⊗2
g,∆ and L(C)⊗2 are isomorphic as the associated
Appell-Humbert data agree [4, Corollary 2.3.7 and Lemma 8.7.1]. As above, we
can shrink U to assume that ϕ∗L
⊗2
g,∆ ≈ L(C)⊗2|U . It is hence suﬃcient to show
that Lg,∆ can be endowed with a smooth hermitian metric ∥ · ∥g,∆ such that

(15) (Lg,∆, ∥ · ∥g,∆)⊗n2 ≈ [n]
∗(Lg,∆, ∥ · ∥g,∆)

as hermitian line bundles. In fact, this relation characterizes ∥ · ∥g,∆ up to a
positive constant by [96, Theorem 2.2 (b)], so that it produces the same Chern
form as the metric ∥·∥∞ constructed above. Endow the trivial line bundle OCg×Hg
with the smooth hermitian metric ∥ · ∥0 given by setting

∥f ∥0 = e
−πIm(z)tIm(τ )−1Im(z)|f |

for every function f deﬁned on an arbitrary open of Cg × Hg. From the explicit
automorphy factors describing Lg,∆ (see [4, Section 8.7]), it is easy to read oﬀ

8This statement also requires that log(−∥s∥∞) is plurisubharmonic. However, this is auto-
matic by [46, Theorem 2.9.14 (iii)]. Furthermore, the cited result is stated only for complex
manifolds so we have to apply it for V instead of X(C). By [51], integration along V ∩ X(C)
deﬁnes a closed positive current T on V . Therefore, [15, Corollary 1.6] implies the weak
convergence dd
c(− log ∥s∥k)
∧d ∧ T −! dd
c(− log ∥s∥∞)
∧d ∧ T,

which yields (14).

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 19

that ∥ · ∥0 descends to a metric ∥ · ∥g,∆ on Lg,∆. Furthermore, the isomorphism
(OCg×Hg, ∥ · ∥0)⊗n2 = [n]
∗(OCg×Hg, ∥ · ∥0) descends to (15). □

The next lemma gives an alternative characterization of the degeneracy locus
of X in terms of the (1, 1)-form β just constructed. For this purpose, we recall the
notion of Betti rank for smooth points x ∈ X sm(C) of an irreducible subvariety
X ⊆ A: Choose an open subset π(x) ∈ U ⊆ S(C) such that there exists a
real-analytic isomorphism

(16) a : A(C)|U −! (R/Z)2g × U

that restricts to a group homomorphism on each ﬁber over U and set

(17) b = pr1 ◦ a : A(C)|U −! (R/Z)2g.

We deﬁne the Betti rank of X at x as the rank of the real-analytic map b at x,
to wit rankBetti(X, x) = dimR(db(TR,xX(C))).

It is easy to see that rankBetti(X, x) depends neither on the choice of U nor a.

Lemma 8. For each x ∈ X sm(C), we have rankBetti(X, x) = 2 dim(X) if and
only if (β|∧ dim(X)
X )x ̸= 0.

This lemma renders the statement of [19, Proposition 2.7] more precise, which
is crucial for some of our arguments below.

Proof. Let U ⊆ S(C) be an open subset containing π(x) such that we have an
isomorphism as in (16). There exists an open subset V ⊂ A(C) containing x and
a holomorphic map l : V ! Cg × Hg such that 2 · β|V = l∗ω where ω is the
(1, 1)-form

ω = i (
dz − dτ · Im(τ )−1 · Im(z))t ∧ Im(τ )−1 (dz − dτ · Im(τ )−1 · Im(z))

and z = (z1, . . . , zg)t and τ = (τij)1≤i,j≤g are the standard coordinates on Cg ×Hg
(see [19, Lemma 2.3] and the proof of Lemma 7 above). We can additionally
arrange l such that the restriction b|V : A(C)|V ! (R/Z)2g from (17) lifts to a
map b = (b1, . . . , b2g)t : A(C)|V ! R2g such that

(18) z = (τ , diag(∆)) · b, diag(∆) =
 


δ1 . . . δg


 ,

(compare [4, Section 8.1] and [19, Proposition B.2]). We use z and τ also for
the respective functions induced on A(C)|V through pullback along l, abusing
notation slightly. Taking the imaginary part of (18), we obtain

Im(zj) =
 g∑

k=1 Im(τjk)bk.

20 LARS K ¨UHNE

In terms of matrices, 

 b1
· · ·
bg
 

 = Im(τ )−1 · Im(z).

We infer that

2 · β|V = i
 

dz − dτ
 

 b1
· · ·
bg
 






t
 ∧ Im(τ )−1
 

dz − dτ
 

 b1
· · ·
bg
 





 .

Choose a C-analytic chart

χ : B1(0)d = {(w1, . . . , wd) ∈ Cd | max{|w1|, . . . , |wd|} < 1} −! X sm(C) ∩ V

such that χ(0) = x. For every function f on X(C), we simply write f (resp.
∂f /∂wl, ∂f /∂wl) instead of f ◦ χ (resp. ∂(f ◦ χ)/∂wl, ∂(f ◦ χ)/∂wl). Consider
the (g × d)-matrix
 J =
 ( ∂zj
∂wl −
 g∑

k=1
 ∂τjk
∂wl · bk
)
1≤j≤g
1≤l≤d
 .

of (complex-valued) real-analytic functions on B1(0)d. It is easy to compute that

2 · χ
∗β = i(J · dw)t ∧ (Im(τ )−1J · dw) = i(dw)t ∧ (J tIm(τ )−1J · dw).

As (J tIm(τ )−1J )(0) ∈ Cd×d is a semipositive Hermitian matrix, there exists a
unitary matrix U ∈ Cd×d such that J t · Im(τ )−1 · J = U · D · U t with D ∈ Rd×d

a diagonal matrix having real entries

d1 ≥ d2 ≥ · · · ≥ dr > dr+1 = · · · = dd = 0

(see e.g. [77, Theorem 10.13]). In local coordinates v1, . . . , vd such that w = U ·v,
we have dw = U · dv and hence

2 · (χ
∗β)0 = i
 r∑

j=1 dj · dvj ∧ dvj.

We infer that (β|∧d
X )x ̸= 0 is equivalent to r = d. As Im(τ )−1 is a (strictly)
positive symmetric matrix, this is equivalent to J (0) having maximal rank d.
To relate the matrix J (0) ∈ Cg×d to the Betti rank, we notice that rankBetti(X, x)
is the rank of the matrix

B =
 





 ∂b1
∂w1 ∂b1
∂w2 · · · ∂b1
∂wd ∂b1
∂w1 ∂b1
∂w2 · · · ∂b1
∂wd
∂b2
∂w1 ∂b2
∂w2 · · · ∂b2
∂wd ∂b2
∂w1 ∂b2
∂w2 · · · ∂b2
∂wd
· · · · · · · · · · · · · · · · · · · · · · · ·
∂b2g
∂w1 ∂b2g
∂w2 · · · ∂b2g
∂wd ∂b2g
∂w1 ∂b2g
∂w2 · · · ∂b2g
∂wd
 




 (0) ∈ C2g×2d.

Taking derivatives in (18), we obtain

∂zj
∂wl =
 g∑

k=1
 ∂τjk
∂wl · bk +
 g∑

k=1 τjk · ∂bk
∂wl + δj · ∂bg+j
∂wl

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 21

and
 0 = ∂zj
∂wl =
 g∑

k=1 τjk · ∂bk
∂wl + δj · ∂bg+j
∂wl

for all j ∈ {1, . . . , g} and l ∈ {1, . . . , d}. These equations imply that
(
τ (0) diag(∆)
τ (0) diag(∆)
) · B = (
J (0) 0g×d
0g×d J (0)
) .

As (
τ (0) diag(∆)
τ (0) diag(∆)
) ∈ C2g×2g is invertible, we conclude

rankBetti(X, x) = rank(B) = 2 · rank(J (0)),

ﬁnishing the proof. □

We continue with establishing degree bounds for non-degenerate subvarieties.
We let X k ⊂ PN
C denote the Zariski closure of ι([n
k](X)). Furthermore, we
consider the graph Γk ⊂ A×A of [n
k]|X : X ! [n
k](X) and the Zariski closure Y k
of (ι×ι)(Γk) in PN
C ×PN
C . We write O(k1, k2) for the line bundle pr∗
1O(k1)⊗pr∗
2O(k2)
on PN
C × PN
C where pri : PN
C × PN
C ! PN
C , i ∈ {1, 2}, is the projection to the i-th
factor.

Lemma 9. If X is non-degenerate, then degO(1,1)(Y k) ≫ n
2kd for all integers
k ≥ 1.

Proof. Let U ⊆ S(C) be a non-empty relatively compact open subset (i.e., a
non-empty open subset whose closure in the euclidean topology is compact). As
X is non-degenerate, we have ∫

π−1(U )∩X(C) β∧d > 0 (compare [19, Proposition 2.7]
or Lemma 8 below). By Lemma 7 above, we deduce thus that
∫

π−1(U )∩X(C) α∧d
k > c13

for some constant c13 > 0 and all integers k ≫ 1. We recall that algebraic
Chern classes and analytic Chern forms on proper complex algebraic varieties are
compatible (i.e., yield the some intersection numbers) and refer to the paragraph
before the proof of [48, Lemma 29] for details. This allows us to compute the
degree of Y k by integration. Using the semipositivity of α0 and αk, we obtain in
this way that
 degO(1,1)(Y k) = ∫

X(C)
 (
α0 + n
2kd · αk)∧d

> n
2kd ∫

X(C) α∧d
k

≥ n
2kd ∫
π−1(U )∩X(C) α∧d
k

> c13 · n
2kd. □

22 LARS K ¨UHNE

We also need a converse bound, whose proof is purely algebraic.

Lemma 10. For each integer k ≥ 1, we have

degO(1,1)(Y k) ≤ degO(n2k,1)(Y k) ≪ n
2kd.

This is proven similar to [19, Section 4.2] and we refer to there for some parts
of the proof that run parallel to our argument.

Proof. The ﬁrst inequality is a direct consequence of Kleiman’s criterion [45,
Theorem III.2.1], using the fact that O(n
2k − 1, 0) is evidently nef. Therefore, we
concentrate on proving the second one in the following.
Recall that X (resp. Y k) is constructed as a closed subvariety of PN
C (resp.
PN
C × PN
C ). Choosing a projective immersion κ : S ֒! PM
C , we can consider X
(resp. Y k) also as a subvariety of PN
C × PM
C (resp. PN
C × PM
C × PN
C ). We do so in
the remainder of this proof. Write C[Y (1), Y (2), Y (3)] for the multi-homogeneous
coordinate ring of PN
C × PM
C × PN
C . From the proof of the related [19, Proposition
4.3], we extract the following fact: For each integer k ≥ 1, there exist multi-
homogeneous polynomials

pi(Y (1), Y (2), Y (3)) ∈ C[Y (1), Y (2), Y (3)], 1 ≤ i ≤ N,

with multi-degrees (δ(i)
1 , δ(i)
2 , 1) such that δ(i)
1 , δ(i)
2 ≪ n
2k and such that Y k is an
irreducible component of

(19) V (p1) ∩ · · · ∩ V (pN ) ∩ (X × PN
C ) ⊆ PN
C × PM
C × PN
C .

We use this to bound the degree of Y k. For this purpose, we also use the basic
notations and results from [22]. By [22, Examples 1.9.3 and 8.3.7], the Chow
ring A
∗(PN
C × PM
C × PN
C ) is of the form

Z[H1]/([H1]N +1) ⊗ Z[H2]/([H2]M +1) ⊗ Z[H3]/([H3]N +1)

where Hi, 1 ≤ i ≤ 3, is the preimage of an arbitrary hyperplane along the i-th
projection. Intersecting with generic hyperplanes, we infer that

(20) [V (pi)] = δ(i)
1 · [H1] + δ(i)
2 · [H2] + [H3], 1 ≤ i ≤ N,

and that we can write

(21) [X × PN
C ] = ∑

j+k=M +N −d aj,k · ([H1]j ⊗ [H2]
k ⊗ [H3]
0).

with non-negative integers aj,k.
We claim next that there exists a chain of irreducible subvarieties

Wi ⊆ PN
C × PM
C × PN
C , 0 ≤ i ≤ N,

satisfying the following properties
(i) W0 = X × PN
C ,
(ii) WN = Y k,
(iii) dim(Wi) = d + (N − i),

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 23

(iv) there exist non-negative integers a
(i)
j,k,l ≪i n
2(i−l)k such that

[Wi] = ∑

j+k+l=M +N +i−d a
(i)
j,k,l · [H1]j ⊗ [H2]
k ⊗ [H3]
l.

Before proving the claim, let us show that it is suﬃcient to derive the second
degree bound of the lemma. Indeed, [Y k] = [WN ] implies that degO(n2k ,1)(Y k)
equals the degree of the 0-cycle

(n
2k · [H1] + [H3])d · ∑

j+k+l=M +2N −d a
(N )
j,k,l · ([H1]
j ⊗ [H2]
k ⊗ [H3]l),

which expands as
( d∑

j=0
 (
d
j
)
n
2jka
(N )
N −j,M,N −d+j
)
 [H1]N ⊗ [H2]
M ⊗ [H3]
N .

Hence, the bounds in (iv) for i = N imply that

degO(n2k,1)(Y k) =
 d∑

j=0
 (
d
j
)
n
2jka
(N )
N −j,M,N −d+j ≪ n
2kd.

Therefore, we ﬁnish with the proof of the above claim. Starting with W0 =
X ×PN
C , we choose the Wi iteratively. Assuming that Wi, 0 ≤ i < N, has already
been chosen, we let Wi+1 be the unique irreducible component of Wi ∩ V (pi+1)
containing Y k. The intersection Wi ∩ V (pi+1) is non-empty because it contains
Y k. By Krull’s principal ideal theorem, this means that either Wi ∩V (pi+1) = Wi
and hence Wi = Wi+1 or dim(Wi+1) = dim(Wi) − 1. In particular, the dimension
drops at most by 1 in each step. As WN has to contain Y k by construction and
is contained itself in (19), of which Y k is an irreducible component, we also know
that (ii) WN = Y k. From dim(W0) = d + N and the fact that Y k = WN has
dimension d, we conclude that the dimension has to drop by 1 in each step and
(iii) holds. We prove (iv) inductively. The base case i = 0 is just (21). So assume
that we have already proven that

[Wi] = ∑

j+k+l=M +N +i−d a
(i)
j,k,l · [H1]j ⊗ [H2]
k ⊗ [H3]l

with integers a
(i)
j,k,l ≪i n
2(i−l)k. We consider the intersection product [Wi] ·
[V (pi+1)] as deﬁned in [22, Chapter 8]. As Wi+1 is a proper component of the
intersection, it is one of its distinguished varieties by [22, Lemma 7.1]. By [22,
Proposition 7.1 (a)], it contributes a positive multiple of its class [Wi+1] to the
intersection product. As the tangent bundle on multiprojective spaces is globally
generated, each other distinguished variety contributes a non-negative cycle to
the intersection product ([22, Corollary 12.2 (a)]). In terms of Chow classes, this
means that we can write
 [Wi] · [V (pi+1)] = [Wi+1] + E

24 LARS K ¨UHNE

with E ∈ A
M +N +i+1−d(PN
C × PM
C × PN
C )≥0 a non-negative Chow class. It is hence
suﬃcient to express [Wi] · [V (pi+1)] with coeﬃcients bounded as in (iv). A simple
calculation in the Chow ring using (20) yields that [Wi] · [V (pi+1)] equals
∑

j+k+l=M +N +i+1−d b
(i+1)
j,k,l · [H1]
j ⊗ [H2]k ⊗ [H3]
l

with b
(i+1)
j,k,l = δ(i)
1 a
(i)
j−1,k,l + δ(i)
2 a
(i)
j,k−1,l + a
(i)
j,k,l−1 ≪i+1 n
2(i+1−l)k,

which completes the proof. □

We complement Lemma 7 with a further, rather trivial estimate.

Lemma 11. For every smooth, compactly supported 2i-form γ on X(C), we have
∫
X(C) α∧(d−i)
k ∧ γ ≪γ 1.

Proof. Let U ⊂ S(C) be a (non-empty) open subset (in the euclidean topology)
such that there exists a real-analytic isomorphism a : A(C)|U ! (R/Z)2g × U as
in (16). Let u1, . . . , u2g be the pullback of the standard real-analytic coordinates
on (R/Z)2g to (R/Z)2g × U. Similarly, we assume that U is small enough such
that there exists a system of local real-analytic coordinates on U as well and we
write u′
1, . . . , u′
2s for its pullback to (R/Z)2g × U along the second projection.
Using these real-analytic coordinates on A(C)|U , we can write

α0|π−1(U ) = ∑

1≤i<j≤2g gi,jdui ∧ duj + ∑

1≤i≤2s hidu′
i ∧ γi

for 1-forms γi and smooth complex-valued functions gi,j, hi on A(C)|U .
By a partition of unity argument, we can assume that the support of γ is a
compact subset K contained in π−1(U). By compactness, we have

sup
x∈K {max{|gi,j(x)|, |hi(x)|}} ≪K 1.

As [n]
∗dui = n · dui (1 ≤ i ≤ 2g) and [n]∗du′
i = du′
i (1 ≤ i ≤ 2s), we immediately
see that the coeﬃcients of the diﬀerential form

α∧(d−i)
k ∧ γ = n
−2k(d−i)([n
k]∗α∧(d−i)
0 ∧ γ)

are ≪K,γ 1 on K, and the assertion of the lemma follows. □

In conclusion of this section, we state four simple lemmas for use in Section 4.
For any variety Y over S, we write Y [n] for the n-fold ﬁber product Y ×S · · ·×S Y .
In addition, we let π[n] denote the projection A
[n] ! S and, for an immersion
ι : A ֒! PN
C , we set

(22) ι
[n] = σ ◦ (ι × · · · × ι)|A[n] : A
[n] = A ×S · · · ×S A ֒−! PNn
C

where σ : PN
C × · · · × PN
C ֒! PNn
C , Nn = (N + 1)n − 1, is the Segre embedding.

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 25

Lemma 12. Let X, Y ⊂ A be irreducible subvarieties such that π(X) = π(Y ) =
S. Assume that X is non-degenerate. Then, there exists a non-empty Zariski-
open set U ⊆ S such that X ×U Y is a non-degenerate irreducible subvariety of
A ×U A.

Proof. Write η for the generic point of S. As X and Y are irreducible, so are
Xη and Yη (compare [34, (0.2.1.8)]). Hence, the generic ﬁber (X ×S Y )η is
irreducible. Again by loc. cit., there is a unique irreducible component Z ⊆
X ×S Y intersecting (X ×S Y )η. Hence, there exists an open dense subset U ⊆ S
such that X ×U Y is irreducible. To prove that X ×U Y is non-degenerate, we
may and do assume U = S in the sequel. Furthermore, we set s = dim(S),
d = dim(X), and d′ = dim(Y ).
Let U ⊆ S(C) be a non-empty simply connected open. Then there exists a
real-analytic isomorphism
a : A(C)|U −! (R/Z)2g × U

that is ﬁberwise also a homomorphism of real Lie groups. Furthermore, set

b = pr1 ◦ a : A(C)|U −! (R/Z)2g.

For each integer n ≥ 1, we set

b
[n] = b ×S · · · ×S b : A
[n](C)|U −! (R/Z)2gn.

By generic smoothness, we may pick a smooth point x ∈ X(C) (resp. y ∈ Y (C))
for the morphism π|X : X ! S (resp. π|Y : Y ! S). This implies

(23) dπ(TR,xX(C)) = TR,sS(C) = dπ(TR,yY (C)).

We may additionally assume that

(24) dimR(db(TR,xX(C))) = rankBetti(X, x) = 2d

as the points satisfying this condition are real-analytically dense in X(C). Com-
puting tangent space dimensions, one can check that z := (x, y) ∈ (X ×S Y )sm(C).
We claim that

rankBetti(Z, z) = dimR(db(TR,zZ(C))) = 2 dim(Z) = 2(d + d′ − s)

with s = dim(S). For the proof, we complete a basis t1, . . . , t2(d−s) ∈ TR,xXs(C)
of the “vertical” tangent vectors to a basis t1, . . . , t2d of the full tangent space
TR,xX(C). By our choice of x, the vectors

db(t1), . . . , db(t2d) ∈ TR,b(x)(R/Z)2g = R2g

are R-linearly independent. Let furthermore t
′
1, . . . , t
′
2(d′−s) ∈ TR,yYs(C) be a
basis of the “vertical” tangent vectors of Y at y. Using (23), we can also pick
tangent vectors t
′′
2(d−s)+1, . . . , t
′′
2d ∈ TR,yY (C) such that

dπ(ti) = dπ(t
′′
i ), 2(d − s) + 1 ≤ i ≤ 2d.

We notice that the “vertical” tangent vectors

(25) (ti, 0) ∈ (TR,xX ×TR,sS TR,yY )(C) = TR,zZ(C), 1 ≤ i ≤ 2(d − s),

26 LARS K ¨UHNE

and

(26) (0, t
′
i) ∈ (TR,xX ×TR,sS TR,yY )(C) = TR,zZ(C), 1 ≤ i ≤ 2(d′ − s),

form a basis of the space TR,zZs(C), and together with the vectors

(27) (ti, t
′′
i ) ∈ (TR,xX ×TR,sS TR,yY )(C) = TR,zZ(C), 2(d − s) + 1 ≤ i ≤ 2d,

they form a basis of TR,zZ(C). As b
[2] = b×S b, it is easy to see that the images of
the 2(d + d′ − s) tangent vectors in (25), (26) and (27) under db
[2] are R-linearly
independent. In fact, if

2(d−s)∑

i=1 ai · (db(ti), 0) +
 2(d′−s)∑

i=1 a
′
i · (0, db(t
′
i)) +
 2d∑

i=2(d−s)+1 ai · (db(ti), db(t
′′
i )) = 0

is an R-linear equation, then

a1 · db(t1) + · · · + a2d · db(t2d) = 0.

By (24), it follows that a1 = · · · = a2d = 0
and thus also a
′
1 = · · · = a
′
2(d′−s) = 0. □

Lemma 12 has the following immediate consequence: If X ⊂ A is non-
degenerate, then so is any ﬁbered power X [n] ⊂ A
[n], n ≥ 1. The following
lemma provides more detailed information.

Lemma 13. Let n ≥ 1 be an arbitrary integer. If

rankBetti(X, x) = 2 dim(X)

for a smooth point x ∈ X(C) of the restriction π|X : X ! S, then the diagonal
embedding (x, . . . , x) ∈ A
[n](C) of x is a smooth point of X [n] such that

rankBetti(Z, (x, . . . , x)) = 2 dim(X [n]) = 2(n dim(X) − (n − 1) dim(S))

where Z ⊆ X [n] is the unique irreducible component containing (x, . . . , x).

Proof. Computing dimensions of tangent spaces, we note ﬁrst that X [n] is smooth
at (x, . . . , x). Hence, there is a unique irreducible component Z ⊆ X [n] containing
(x, . . . , x).
The remaining parts of the lemma follow from an argument similar to the one
given for Lemma 12 above. In fact, setting y = x and z = (x, x) in its proof, we
can take ti = t
′′
i (i ∈ {2(d − s) + 1, . . . , 2d}). This already yields the lemma in
the case n = 2.
In the general case, let t1, . . . , t2d be a basis of the tangent space TR,xX(C)
such that t1, . . . , t2(d−s) ∈ TR,xXs(C) form a basis of the “vertical” tangent space.
We set z = (x, . . . , x). The “vertical” tangent vectors

(28) (0, . . . ,
 j-th position
#
ti , . . . , 0) ∈ TR,zX [n](C), 1 ≤ i ≤ 2(d − s), 1 ≤ j ≤ n,

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 27

form a basis of the space TR,zX [n]
s (C), and together with the vectors

(29) (ti, ti, . . . , ti) ∈ TR,zX(C)n, 2(d − s) + 1 ≤ i ≤ 2d,

they form a basis of TR,zX [n](C). As b
[n] = b ×S · · · ×S b, one can check as above
that the images of the 2((d − s)n + s) tangent vectors in (28) and (29) under
db
[n] are R-linearly independent. □

Furthermore, we note that non-degeneracy is preserved under isogenies.

Lemma 14. Let π′ : A
′ ! S be another family of complex abelian varieties and
q : A ! A
′ a ﬁberwise isogeny over S. If X ⊆ A is a non-degenerate irreducible
subvariety, then so is its image q(X) ⊆ A
′.

Proof. Choose a simply connected open U ⊆ S(C) as well as Betti maps

b : (A ∩ π−1(U))(C) −! (R/Z)2g

and b
′ : (A
′ ∩ π−1(U))(C) −! (R/Z)2g.
As X is non-degenerate, we may pick a point x0 ∈ X(C) such that

dimR(db(TR,x0X(C))) = rankBetti(X, x0) = 2 dim(X).

As the Betti map is compatible with the ﬁberwise group structures, there exists
an isogeny q′ : (R/Z)2g ! (R/Z)2g such that

(A ∩ π−1(U))(C) (R/Z)2g

(A
′ ∩ π−1(U))(C) (R/Z)2g

b

q q′

b′

commutes. We infer that

db
′(TR,q(x0)q(X)(C)) = db
′(dq(TR,x0X(C))) = dq′(db(TR,x0X(C))).

As dq′ is an R-linear isomorphism, this implies

dimR(db
′(TR,q(x0)q(X)(C))) = dimR(db(TR,x0X(C))) = 2 dim(X) = 2 dim(q(X)).

Hence q(X) is non-degenerate. □

We conclude this section with establishing the non-proportionality of two vol-
ume forms derived from the Betti form. These forms appear naturally in the
proof of Proposition 27 below. For each integer n ≥ 1, we write β[n] for the
(1, 1)-form deﬁned for π[n] : A
[n] ! S in Lemma 7. For a given integer m ≥ 2,
we deﬁne the map

∆0 : A
[m] −! A
[m−1],

(x1, x2, . . . , xm) ↦−! (x1 − x2, x2 − x3, . . . , xm−1 − xm),

and set ∆ = ∆0 ×S idA : A
[m] ×S A −! A
[m−1] ×S A.

28 LARS K ¨UHNE

We call two volumes forms α1, α2 proportional if there exists a real number c ̸= 0
such that α1 = c · α2.

Lemma 15. Let m ≥ 2 be an arbitrary integer and X ⊆ A be an irreducible
subvariety of dimension d > dim(S) with π(X) = S. If X is non-degenerate,
then the diﬀerential forms

(β[m+1])∧ dim(X [m+1]) and (∆
∗β[m])∧ dim(X [m+1])

do not restrict to proportional volume forms on X [m+1].

Proof. As X is non-degenerate, there exists a smooth point x ∈ X of the mor-
phism π|X : X ! S such that rankBetti(X, x) = 2 dim(X). Using Lemma 13, we
infer that rankBetti(Z, p) = 2 dim(X [m+1])

for the diagonally embedded point p = (x, x, . . . , x) ∈ X [(m+1)],sm(C) and the
unique irreducible component Z ⊆ X [m+1] containing p. Lemma 8 implies con-
sequently that (β[m+1])∧ dim(X [m+1])
p ̸= 0.
In contrast, there exists a non-zero “vertical” tangent vector t ∈ TR,xXπ(x) by
assumption. Hence, we obtain a non-zero tangent vector

((t, . . . , t), 0) ∈ TR,(x,...,x)X [m]
π(x)(C) ×TR,π(x)S TR,xXπ(x)(C) ⊂ TR,pX [m+1](C)

that is annihilated by d∆. This means that

ker((d∆)p) ∩ TR,pX [m+1](C) ̸= {0}

and thus (∆
∗β[m])∧ dim(X [m+1])
p = 0, which concludes the proof. □

3. Proof of Theorem 1

As in the statement of the theorem, let S be a smooth, geometrically irreducible
variety over a number ﬁeld K, π : A ! S an abelian scheme, ι : A ֒! PN
K
an immersion, X ⊂ A a non-degenerate geometrically irreducible subvariety of
dimension d over K such that π(X) = S. We also choose an arbitrary immersion
κ : S ֒! PM
K of the base. We set h(x) = hO(1)(ι(x)) for each closed point x ∈ A
and similarly h(s) = hO(1)(κ(s)) for each closed point s ∈ S. In this section, all
of the constants depend implicitly on the data introduced so far. We exclusively
note further dependencies. Finally, we let (xi) ∈ X N be an X-generic sequence
such that ̂h(xi) ! 0 as i ! ∞.

3.1. Convergence of heights. We ﬁrst note a comparison between the asymp-
totic “height” ̂h and the ordinary projective height h. This comparison is in fact
well-known and could be derived from the explicit estimates in [54], whose proof
involves Mumford’s algebraic theta functions [62, 63]. A general result, appli-
cable beyond families of abelian varieties, was provided by Silverman [79]. We
state our own version here, which does not require that ι
∗O(1)|A is symmetric.

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 29

Lemma 16. There exist constants c14, c15 > 0 such that

|̂h(x) − h(x)| ≤ c14 · max{1, h(π(x))} + c15 · ̂h(x)1/2 · max{1, h(π(x))}1/2

for all x ∈ A(Q).

Proof. By induction on dim(S), it suﬃces to prove the estimate for all x ∈
π−1(U) where U ⊆ S is a Zariski-open. We can hence assume that ι
∗O(1)|A is
the line bundle associated with a relative eﬀective (Cartier) divisor D ⊂ A as
deﬁned in [1, Tag 056P]. We consider the decomposition 2 · D = Dsym + Danti
into a symmetric divisor Dsym = D + [−1]∗D and an anti-symmetric divisor
Danti = D − [−1]∗D. Both Dsym and Danti are relative eﬀective Cartier divisors.
As in [79], we consider some associated ordinary Weil height functions hDsym and
hDanti. (These height functions are only unique up to some bounded function
on A(Q) and we make an arbitrary choice here.) Furthermore, we let ̂hDsym
and ̂hDanti be the ﬁberwise N´eron-Tate heights as in loc. cit. We can assume
that h = hDsym + hDanti. In contrast, ̂hι = ̂hDsym is forced upon us by our
normalizations.
Applying [79, Corollary 7.4] to both Dsym and Danti separately, we get a con-
stant c16 > 0 such that

(30) |̂hDsym(x) − hDsym(x)| + |̂hDanti(x) − hDanti(x)| ≤ c16 · max{1, h(π(x))}.

To prove the lemma, it hence remains to bound |̂hDanti(x)|. As the line bundle
O(Danti) is algebraically equivalent to the trivial line bundle over the generic
point of S, it is so over a Zariski-open U ⊆ S as well. As we are in an induction
on the dimension of S, we may hence assume that O(Danti) ∈ Pic0(A/S)(S). By
[65, Corollary 6.8], we know that Pic
0(A/S) is represented by the relative dual
abelian variety A
∨ so that O(Danti) corresponds to a section σ∨ : S ! A
∨. As in
[65, Section 6.2], the relatively ample line bundle O(1)|A deﬁnes a polarization
Λ(O(1)|A) : A ! A
∨, which is a ﬁnite surjective map. Passing once more to a
Zariski-dense open U ⊆ S if necessary, we can assume that σ∨ = Λ(O(1)|A) ◦ σ
for some section σ : S ! A. Write B(·, ·) for the bilinear form associated with
the ﬁberwise N´eron-Tate height ̂h. By [6, Proposition 9.3.6 and Corollary 9.3.7]
and the Cauchy-Schwarz inequality, we have

|̂hDanti(x)| = |B(x, (σ ◦ π)(x))|

≤ B(x, x)1/2 · B((σ ◦ π)(x), (σ ◦ π)(x))1/2

≤ 4 · ̂h(x)1/2 · ̂h(σ ◦ π(x))1/2.

for all x ∈ A(Q). As κ
∗O(1) is ample on S, standard height estimates in combi-
nation with (30) yield a constant c17 > 0 such that

̂h(σ(s)) = ̂hDsym(σ(s)) ≤ hDsym(σ(s)) + c16 · max{1, h(s)}

≤ c17 · max{1, h(s)}

30 LARS K ¨UHNE

for all s ∈ S(Q). In summary, we obtain

|̂hDanti(x)| ≤ c18 · ̂h(x)1/2 · max{1, h(π(x))}1/2

for some constant c18, which in combination with (30) yields the assertion. □

We can also recall the following central result from [19].

Theorem 17. There exists a constant c19 > 0 such that

h(π(xi)) < c19 max{1, ̂h(xi)}

for all but ﬁnitely many i ∈ N.

Proof. Taking into account that (xi) is X-generic, this is [18, Theorem B.1]
applied to the symmetric line bundle O(1)|A ⊗ [−1]∗O(1)|A. □

Our next lemma is a rather straightforward consequence.

Lemma 18. For each integer k ≥ 0, set x
(k)
i = ι([n
k](xi)) and

lk = n
−2k · lim sup
i!∞
 (hO(1)(x
(k)
i )) .

Then, lk ∈ [0, ∞) for each integer k ≥ 0. Furthermore, limk!∞(lk) = 0.

Proof. Note that (1) implies ̂h(xi) = n
−2k̂h([n
k](xi)) for all integers i, k ≥ 0. For
suﬃciently large integers i, we thus have
∣
∣
∣
∣
∣
̂h(xi) − hO(1)(x
(k)
i )
n2k
 ∣
∣
∣
∣
∣ = |̂h([n
k](xi)) − h([n
k](xi))|
n2k

≤ c14 · max{1, h(π(xi))} + c15 · ̂h(x)1/2 · max{1, h(π(xi))}1/2

n2k

≤ c20 · max{1, ̂h(xi)}
n2k ,

where we used Lemma 16 for the ﬁrst inequality and Theorem 17 for the second
one. As limi!∞ ̂h(xi) = 0 by assumption, the assertion follows immediately. □

Recall that X k ⊂ PN
K is the Zariski closure of ι([n
k](X)). Let Γk ⊂ A × A be
the graph of [n
k]|X, and let Y k ⊂ PN
K × PN
K be the Zariski closure of (ι × ι)(Γk).
We notice that projection to the ﬁrst (resp. second) factor induces a surjective,
birational map ψ1 : Y k ! X 0 (resp. a surjective map ψ2 : Y k ! X k). (Note
that X 0 is just the Zariski closure of ι(X) ⊂ PN
K.) We write y(k)
i for the point
(ι(xi), x
(k)
i ) = (ι(xi), ι([n
k](xi))) ∈ Y k.

Lemma 19. For all integers k ≥ 0, we have

0 ≤ hO(1)(X k) ≤ n
2klk.

For any integers k, k1, k2 ≥ 0, we have

0 ≤ hO(k1,k2)(Y k) ≤ k1l0 + k2n
2klk.

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 31

Proof. The proof of the lemma is a straightforward application of Zhang’s succes-
sive minima [95, Theorem 5.2]. Each point of X k (resp. Y k) has a non-negative
height with respect to O(1) (resp. O(k1, k2)). Hence the heights of X k and Y k are
non-negative as well. In addition, the sequence (x
(k)
i ) (resp. (y(k)
i )) is X k-generic
(resp. Y k-generic). Using Zhang’s inequalities, we deduce hence

hO(1)(X k) ≤ lim inf
i!∞
 (hO(1)(x
(k)
i )) ≤ lim sup
i!∞
 (hO(1)(x
(k)
i )) = n
2kℓk

and similarly

hO(k1,k2)(Y k) ≤ lim sup
i!∞
 (hO(k1,k2)(y(k)
i ))

≤ k1 · lim sup
i!∞
 (hO(1)(ι(xi))) + k2 · lim sup
i!∞
 (
hO(1)(x
(k)
i ))

= k1ℓ0 + k2n
2kℓk. □

By Lemma 18, this proves already the ﬁrst part of Theorem 1, namely that

̂h(X) = lim
k!∞
 ( hO(1)(X k)
n2k
 )
 = 0.

3.2. Reductions. Before continuing with the equidistribution part of the proof,
we make some reductions.
Furthermore, we can assume that ι
∗O(1)|A is symmetric (i.e., [−1]∗O(1)|A ≈
O(1)|A). Composing the immersion

ι × (ι ◦ [−1]) : A ֒! PN
K × PN
K

with the Segre embedding, we obtain an immersion ι
′ : A ֒! P(N +1)2−1
K . As
the line bundle (ι
′)∗O(1) is isomorphic to ι
∗O(1) ⊗ [−1]∗ι
∗O(1), it is ﬁberwise
symmetric. In addition, we have

lim
k!∞
 ( hO(1)(ι
′([n
k](xi)))

n2k
 )
 = ̂h(xi) + ̂h(−xi) = 2̂h(xi) −! 0, i ! ∞,

by [40, Proposition B.2.4 (b)]. Replacing ι with ι
′, we can assume that ι
∗O(1)|A
is ﬁberwise symmetric.
Additionally, we can assume that ι
∗O(1) is ﬁberwise of type (δ1, δ2, . . . , δg) ∈ Z
g

with δ1 ≥ 3 and δi | δi+1 (1 ≤ i < g). In fact, we are allowed to replace

ι : A ֒! PN
K with ν ◦ ι : A ֒! P(N+3
N )−1
K where ν : PN
K ֒! P(N+3
N )−1
K is the Veronese
embedding of degree 3. As (ν ◦ ι)∗O(1) ≈ ι
∗O(1)⊗3, the immersion ν ◦ ι satisﬁes
this additional assumption.9

In the sequel, we consider functions f ∈ C 0
c (X an
Cν ) as in the statement of
Theorem 1. We need additionally that f is Gal(Cν/Kν)-invariant, which we

9We remark that the pullback of the Fubini-Study metric on P(
N +3
N )−1
C by the Veronese
embedding is not the same as the Fubini-Study metric on PN
C , but that the associated heights
̂hι and ̂hν◦ι coincide on closed points.

32 LARS K ¨UHNE

can simply assume by enlarging K such that Cν = Kν. The assertion of the
theorem only becomes stronger in this way. Approximating f uniformly by
smooth functions, we can assume without loss of generality that f ∈ C ∞
c (X an
Cν ).
In fact, Theorem 1 for smooth test functions f ∈ C ∞
c (X an
Cν ) already implies
µν(X an
Cν ) ≤ 1 as the left-hand side in (2) is always ≤ 1. Therefore, the right-
hand side in (2) is continuous in the test function f with respect to the uniform
topology. This allows us to replace general continuous test functions with smooth
ones in the course of proving Theorem 1.
10

3.3. Equidistribution. We extend f by zero to a smooth function f! on X an
0,Cν
and set fk = f! ◦ ψan
1,Cν ∈ C ∞
c (Y an
k,Cν ) for each integer k ≥ 1 where the map
ψ1 : Y k ! X 0 is deﬁned as in the paragraph before Lemma 19.
In the following, we write Yk for the Zariski closure of Y k in PN
OK × PN
OK and
O(1, 1; k, λ), λ ∈ [0, 1], for the C ∞-hermitian line bundle

O(1, 1)|Yk + O(λn
2kfk) ∈ ̂PicC ∞(Yk).

Let further µk be the measure on Y an
k,Cν given by the restriction of the (d, d)-form

(pr∗
1ωFS + pr∗
2ωFS)∧d

n2kd

where pri : PN
Cν × PN
Cν ! PN
Cν , i ∈ {1, 2}, is the projection to the i-th factor.

Lemma 20. Assume that λ ∈ [0, 1]. Then, there exists a constant c21 = c21(f ) >
0 such that
∣
∣
∣
∣
∣
hO(1,1;k,λ)(Y k) − hO(1,1)(Y k) − δνλn
2k(d+1)

[K : Q] degO(1,1)(Y k)
 ∫

Y an
k,Cν fkµk
∣
∣
∣
∣
∣ ≤ c21 · |λ|2n
2k.

for every integer k ≥ 0.

Proof. We note ﬁrst that

hO(1,1;k,λ)(Y k) = O(1, 1; k, λ)d+1

[K : Q](d + 1) degO(1,1)(Y k).

by deﬁnition and that Lemma 5 (a,b) provides an expansion

O(1, 1; k, λ)d+1 =
 d+1∑

j=0
 (
d + 1
j
 ) · (O(1, 1)|Yk)d+1−j · O(λn
2kfk)j.

Again by the deﬁnition of the height, we have

(O(1, 1)|Yk)d+1

[K : Q](d + 1) degO(1,1)(Y k) = hO(1,1)(Y k),

10In fact, additional estimates show that µν(X an
Cν ) = 1 (compare [28, 94]), but µν (X an
Cν ) ≤ 1
is enough for us.

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 33

and from (10) we infer that

(O(1, 1)|Yk)d · O(λn
2kfk)

[K : Q] degO(1,1)(Y k) = δνλn
2k(d+1)

[K : Q] degO(1,1)(Y k)
 ∫

Y an
k,Cν fkµk.

Since degO(1,1)(Y k) ≫ n
2kd by Lemma 21 below, the assertion of the lemma boils
down to the estimate
∣
∣
∣
∣
∣
 d+1∑

j=2
 (
d + 1
j
 )(O(1, 1)|Yk )d+1−j · O(λn
2kfk)j∣
∣
∣
∣
∣ ≪f |λ|2n
2k(d+1).

Using (10) a second time, we obtain

(O(1, 1)|Yk)d+1−j · O(λn
2kfk)j

= δνλjn
2kj ∫

Y an
k,Cν fk(ddcfk)∧(j−1) ∧ (pr∗
1ωFS + pr∗
2ωFS)∧(d+1−j)

for each j ∈ {2, . . . , d+1}. By the substitution rule (8), the integral above equals
∫

X an
Cν f (ddcf )∧(j−1) ∧ (ι
∗ωFS + (ι ◦ [n
k])∗ωFS)∧(d+1−j),

which is ≪f n
2k(d+1−j) by Lemma 11. As λ ∈ [0, 1] by assumption, the lemma
follows immediately. □

The next lemma gives us also a good control on the degree of Y k.

Lemma 21. For each integer k ≥ 0,

n
2kd ≪ degO(1,1)(Y k) ≤ degO(n2k,1)(Y k) ≪ n
2kd.

Proof. This is just a combination of Lemmas 9 and 10. □

To formulate the next lemma, we introduce the supremum

l := sup
k≥0{lk}.

Note that l ∈ [0, ∞) by Lemma 18.

Lemma 22. For every integer k ≥ 0, we have

̂volχ(O(1, 1; k, λ)) − O(1, 1; k, λ)d+1 ≫f,l −|λ|2n
2(d+1)k.

The proof of this lemma uses Ikoma’s version of Yuan’s bigness theorem [93].

Proof. Let σ = σ(f ) be a constant such that f (x) + σ ≥ 0 for all x ∈ X an
Cν . We
set
 O(1, 1; k, λ, σ) := O(1, 1; k, λ) + O(λn
2kσ) = O(1, 1)|Yk + O(λn
2k(fk + σ))

and note that
̂volχ(O(1, 1; k, λ)) − O(1, 1; k, λ)d+1 = ̂volχ(O(1, 1; k, λ, σ)) − O(1, 1; k, λ, σ)d+1

34 LARS K ¨UHNE

(e.g. by [49, Lemmas 2.2 (d)11 and 2.5 (a)] and (10)). It hence suﬃces to bound
the diﬀerence on the right-hand side from below.
Since ωFS is a strictly positive (1, 1)-form and f! has compact support, there
exists some rational constant q = q(f ) > 0 such that the (1, 1)-form

q · ωFS + ddcf!

on X an
0,Cν is strictly positive. Consequently, the (1, 1)-form

q · pr∗
1ωFS + ddcfk

on Y an
k,Cν is semipositive.
Applying Ikoma’s version [43, Theorem 3.5.3 and Remark 3.5.4] of Yuan’s
bigness theorem to the decomposition
(
O(1, 1)|Yk + qλn
2k · O(1, 0)|Yk + O(λn
2k(fk + σ))) − qλn
2k · O(1, 0)|Yk,

of O(1, 1; k, λ, σ), we obtain that ̂volχ(O(1, 1; k, λ, σ)) is bounded from below by
(
O(1, 1)|Yk + qλn
2k · O(1, 0)|Yk + O(λn
2k(fk + σ)))d+1

−(d+1) (
O(1, 1)|Yk + qλn
2k · O(1, 0)|Yk + O(λn
2k(fk + σ)))d·(
qλn
2k · O(1, 0)|Yk
) .

By Lemma 5 (a), subtracting O(1, 1; k, λ, σ)d+1 from the above expression results
in

(31) −
 d+1∑

i=2
 (d + 1
i
 ) (
O(1, 1)|Yk + qλn
2k · O(1, 0)|Yk + O(λn
2k(fk + σ)))d+1−i

· ((−qλn
2k) · O(1, 0)|Yk
 )i .

We claim that the absolute value of (31) is ≪f,ℓ |λ|2n
2(d+1)k. For this purpose,
we expand the intersection number
(
O(1, 1)|Yk + qλn
2k · O(1, 0)|Yk + O(λn
2k(fk + σ)))d+1−i · (qλn
2k · O(1, 0)|Yk
)i

and estimate the intersection number

(32) (O(1, 1)|Yk )j1 ·(qλn
2k ·O(1, 0)|Yk)j2 ·(O(λn
2k(fk +σ)))j3, j1 +j2 +j3 = d+1,

in the general term of this expansion. Note that only intersection numbers with
j2 ≥ 2 appear here, so we may assume this freely in the following. If j3 ≥ 1, then

11One of the referees has kindly pointed out to us that this lemma cites a result from [15],
for which the numbering in the electronic version on the author’s webpage is diﬀerent from the
printed version. It is meant to cite Lemma 9.3 in the electronic version, which corresponds to
Lemma 10.2 in the printed version.
We also remark that the lemma is stated for semipositive line bundles, but extends because of
multilinearity.
 EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 35

(32) equals

qj2(λn
2k)j2+j3 ∫

Y an
k,Cν (fk + σ)(pr∗
1ωFS + pr∗
2ωFS)∧j1 ∧ (pr∗
1ωFS)∧j2 ∧ (ddcfk)∧(j3−1)

by (10). In the case j3 = 1, Lemma 21 implies immediately that this is ≪f n
2kd.
For the remaining case j3 ≥ 2, we recall the notation αk = (ι ◦ [n
k])∗ωFS/n
2k

from Section 2. Using the substitution formula, we can rewrite the above term
as qj2(λn
2k)j2+j3 ∫

X an
Cν (f! + σ)(α0 + n
2kαk)∧j1 ∧ α∧j2
0 ∧ (ddcf!)∧(j3−1),

whose absolute value is ≪f |λ|2n
2(d+1)k by Lemma 11 and our assumption λ ∈
[0, 1]. In summary, the absolute value of the corresponding terms in (31) is
≪f |λ|2n
2(d+1)k.
It remains to ﬁnd similar estimates for (32) if j3 = 0. This term becomes then

(O(1, 1)|Yk)j · (qλn
2k · O(1, 0)|Yk)(d+1)−j.

It is easy to see that the intersection numbers

(33) (O(1, 1)|Yk )j · (O(n
2k, 0)|Yk)(d+1)−j, 0 ≤ j ≤ (d − 1),

are non-negative. In fact, this follows from the recursive formula for the Arakelov
height as both O(1, 0) and O(1, 1) are globally generated by sections having
norm ≤ 1 everywhere (compare the proof of [95, Lemma 5.3 (i)]). It is hence
suﬃcient to ﬁnd an upper bound. With a similar argument and using Lemma
5 (a), each of the intersection numbers in (33) can be bounded from above by
(O(n
2k, 1)|Yk)(d+1).
In order to bound this arithmetic intersection number, let us note that Lemma
19 implies that
 hO(n2k,1)(Y k) = (O(n
2k, 1)|Yk )d+1

[K : Q](d + 1) degO(n2k,1)(Y k)

≤ n
2k(l0 + lk).

Combining this with the upper degree bound from Lemma 21, we infer that

(O(n
2k, 1)|Yk)(d+1) ≪ n
2(d+1)k(l0 + lk) ≤ 2n
2(d+1)kl.

Retracing the above estimates,we conclude the proof. □

With these preparations, we can already bring the proof of Theorem 1 close
to its end.

Lemma 23. We have

lim sup
i!∞
 ∣
∣
∣
∣
∣
∣
 1
#Oν(xi)
 ∑

y∈Oν (xi) f (y) − n
2kd

degO(1,1)(Y k)
 ∫
Y an
k,Cν fkµk
∣
∣
∣
∣
∣
∣ −! 0

as k ! ∞.

36 LARS K ¨UHNE

Proof. Choose some λ ∈ (0, 1] as well as some ε > 0.
In the following, we write

O(1, 1; k, λ) = (O(1, 1)|Yk , {∥ · ∥µ}µ∈Σ∞(K)).

By Lemma 6, there exists some positive integer N0 and a non-zero section s ∈
H 0(Yk, O(1, 1)⊗N0) such that

δν · log ∥s(x)∥1/N0
ν
[K : Q] ≤ − ̂volχ(O(1, 1; k, λ))
[K : Q](d + 1)(O(1, 1)|Y k)d + ε

for every point x ∈ (Y k \ |div(s)|)an
Cν and

log ∥s(x)∥µ ≤ 0

for every place µ ∈ Σ∞(K) \ {ν} and all points x ∈ (Y k \ |div(s)|)an
Cµ. Using
Lemmas 21 and 22, we infer that there exists some constant c22 = c22(f, l) > 0
such that
 δν · log ∥s(x)∥1/N0
ν
[K : Q] ≤ −hO(1,1;k,λ)(Y k) + c22 · λ2n
2k + ε

for every point x ∈ (Y k \ |div(s)|)an
Cν . Using Lemmas 19 and 20, we deduce that

δν · log ∥s(x)∥1/N0
ν
[K : Q] ≤ − δνλn
2k(d+1)

[K : Q] degO(1,1)(Y k)
 ∫
Y an
k,Cν fkµk + c23 · λ2n
2k + ε.

for some constant c23 = c23(f, l) > 0 and all x ∈ (Y k \ |div(s)|)an
Cν . Through (11),
we can use this to obtain the lower global bound

hO(1,1;k,λ)(x) ≥ λn
2k(d+1)

[K : Q] degO(1,1)(Y k)
 ∫
Y an
k,Cν fkµk − c23 · λ2n
2k − ε

for all closed points x ∈ Y k \|div(s)|. (We suppress δν where it is possible because
of δν ≥ 1.) Expanding the left-hand side of this equation, we thus obtain

(34) hO(1,1)(x) + 1
[K : Q]
 

 λn
2k

#Oν(x)
 ∑

y∈Oν (x) fk(y) − λn
2k(d+1)

degO(1,1)(Y k)
 ∫
Y an
k,Cν fkµk




≥ −c23 · λ2n
2k − ε

for all closed points x ∈ Y k \ |div(s)|. Since (xi) ∈ X N is a generic sequence,
there exists some integer i0 such that y(k)
i = (ι(xi), ι([n
k](xi))) /∈ |div(s)| for all
i ≥ i0. By deﬁnition of ℓk,

n
−2k · lim sup
i!∞
 (hO(1,1)(y(k)
i )) ≤ n
−2k · lim sup
i!∞
 (
hO(1)(ι(xi))) + n
−2k lim sup
i!∞
 (hO(1)(x
(k)
i ))

≤ n
−2k · ℓ0 + ℓk.

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 37

After canceling [K : Q]
−1λn
2k in (34), we obtain thus

lim inf
i!∞
 

 1
#Oν(xi)
 ∑

y∈Oν (xi) f (y) − n
2kd

degO(1,1)(Y k)
 ∫
Y an
k,Cν fkµk




≥ −c24 · (λ + λ−1n
−2kl0 + λ−1lk) − λ−1[K : Q]ε

for some constant c24 = c24(f, l) > 0. Working with −f instead of f in our
above reasoning, we obtain similarly

lim sup
i!∞
 

 1
#Oν(xi)
 ∑

y∈Oν (xi) f (y) − n
2kd

degO(1,1)(Y k)
 ∫
Y an
k,Cν fkµk




≤ c24 · (λ + λ−1n
−2kl0 + λ−1lk) + λ−1[K : Q]ε

In summary, we infer that

(35) lim sup
i!∞
 ∣
∣
∣
∣
∣
∣
 1
#Oν(xi)
 ∑

y∈Oν (xi) f (y) − n
2kd

degO(1,1)(Y k)
 ∫

Y an
k,Cν fkµk
∣
∣
∣
∣
∣
∣

≤ c24 · (λ + λ−1n
−2kl0 + λ−1lk) + λ−1[K : Q]ε.

Given ε0 > 0, set
 λ = min { ε0
3c24 , 1}

and
 ε = ε0λ
3[K : Q] = min{ε2
0/3c24, ε0}
3[K : Q] .

By Lemma 18, there also exists an integer k0(ε0) such that

n
−2kl0 + lk < ε0λ/3c24 = min{ε2
0/9c2
24, ε0/3c24}

for all k ≥ k0(ε0). The right-hand side in (35) is less than ε0 if k ≥ k0(ε0),
whence the assertion of the lemma. □

Let us next establish the asymptotics of the integrals appearing in the last
lemma.

Lemma 24. As k ! ∞, we have
∫
Y an
k,Cν fkµk −! ∫

X an
Cν f β∧d

where β is the smooth (1, 1)-form on X an
Cν introduced in Lemma 7.

Proof. By the substitution rule, we have
∫

Y an
k,Cν fkµk = n
−2kd ∫

X an
Cν f (ι
∗ωFS + (ι ◦ [n
k])∗ωFS)∧d .

The assertion follows immediately from Lemmas 7 and 11. □

38 LARS K ¨UHNE

So far, we have only established (in Lemma 21) and needed the following
degree inequalities:

0 < lim inf
k!∞
 (degO(1,1)(Y k)
n2kd
 )
 ≤ lim sup
k!∞
 ( degO(1,1)(Y k)
n2kd
 )
 < ∞.

Having almost proven equidistribution in Lemma 23 above, we can show that
the middle inequality is in fact an equality.12

Lemma 25. The limit

(36) k = lim
k!∞
 ( degO(1,1)(Y k)
n2kd
 )

exists in (0, ∞).

Proof. As X is non-degenerate, Lemma 8 guarantees that there exists f ∈
C ∞
c (X an
Cν ) such that ∫

X an
Cν f β∧d > 0. Applying Lemma 23 with this test func-
tion, we obtain an integer k0(ε) such that
∣
∣
∣
∣
∣ n
2k′d

degO(1,1)(Y k′)
 ∫

Y an
k′,Cν fk′µk′ − n
2kd

degO(1,1)(Y k)
 ∫
Y an
k,Cν fkµk
∣
∣
∣
∣
∣ ≤ ε

for all k, k′ ≥ k0(ε). As both integrals converge to the same (strictly) positive
limit by Lemma 24, we infer that
( n
2kd

degO(1,1)(Y k)
 )

k

is a Cauchy sequence and hence converges to some real number in [0, ∞). This
shows that the limit (36) exists at least in (0, ∞]. However, the convergence to
∞ is precluded by Lemma 21. □

There is not much left to complete the proof of Theorem 1: Setting µν =
k
−1 · β∧d, we have
 n
2kd

degO(1,1)(Y k)
 ∫
Y an
k,Cν fkµk −! ∫

X an
Cν f µν

as k ! ∞. The theorem is thus an immediate consequence of Lemma 23.

12This would also follow from [29, Proposition 13], but it seems noteworthy that equidistri-
bution can be also used to prove this assertion and so we follow this approach. Furthermore,
this choice makes our argument more self-contained and less technical.

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 39

4. Proof of Theorems 2 and 3

Except for Proposition 27 and its proof, π : A ! S denotes a principally
polarized abelian scheme of relative dimension g over a quasi-projective Q-variety
S. We also ﬁx an immersion κ : S ֒! PN
Q . (In contrast to the other parts of
this article, we do not assume a priori that S is smooth in this section, as we
can easily reduce to this case in the proofs below.) In this section, all of the
constants can depend on the data introduced so far without further mention. We
exclusively keep track of additional dependencies.
We let c : S ! Ag,1 be the classifying map such that

(37)
 A Bg,1

S Ag,1

cB

π πg,1

c

is cartesian. Furthermore, we consider the base change c′
B such that the square

A ×Bg,1 Bg,3 Bg,3

A Bg,1

c′
B

cB

is cartesian; here, Bg,3 ! Bg,1 is the forgetful functor. Recall that Bg,3 is a
quasi-projective variety over Q by [65, Theorem 7.9] and the “lemma of Serre”
[78]. It is also smooth by a result of Grothendieck [69, Theorem 2.4.1].
With the next proposition, we prove a more general result than Theorem 3,
which is additionally amenable to a proof by induction on dim(S).

Proposition 26. Let S be an irreducible, quasi-projective variety over Q, π :
A ! S a principally polarized abelian scheme of relative dimension g, ι : A ֒! PN
Q
an immersion, and C ⊆ A an irreducible subvariety such that π(C) = S. Assume
that(i) for every geometric point s of S, the ﬁber Cs ⊂ As is a smooth projective
curve of genus ≥ 2;
(ii) for every geometric point s of S, the variety Cs −Cs ⊆ As is not contained
in a proper torsion coset of As;
(iii) the map c′
B restricts to a generically ﬁnite map on C ×Bg,1 Bg,3.
Then, there exist constants c25 = c25(C, ι) > 0 and c26 = c26(C, ι) > 0 such that

(38) #{x ∈ Cs(Q) | ̂h(x) < c25} ≤ c26

for all s ∈ S(Q).

Before giving the proof of this proposition, let us indicate how to deduce the
uniform Manin-Mumford and the uniform Bogomolov conjecture from it.

40 LARS K ¨UHNE

Proof of Theorem 2 using Theorem 3. By a specialization argument due to Masser
[55] (see [20, Section 3]), it is enough to prove Theorem 2 for smooth proper genus
g curves C deﬁned over Q. In this case, it follows immediately from Theorem 3,
which is deduced below. □

Proof of Theorem 3 using Proposition 26. We ﬁrst reduce the assertion to the
case where D = [p] for a point p ∈ Cg,n,s(Q). Assume Theorem 3 is already
proven in this special case for constants c′
3(g, n, ι) and c′
4(g, n, ι). We claim that
Theorem 3 then holds in the general case as well with slightly altered constants

c3(g, n, ι) = c′
3(g, n, ι)
4 and c4(g, n, ι) = c′
4(g, n, ι).

To prove this, we may assume that there exists some p ∈ Cg,n,s(Q) such that

̂h([p] − D) ≤ c3(g, n, ι);

for otherwise there is nothing to prove. For every point q ∈ Cg,n,s(Q) in the set
(4), we have

̂h([q] − [p]) ≤ 2̂h([q] − D) + 2̂h(D − [p]) ≤ 4 · c3(g, n, ι) = c′
3(g, n, ι)

by the parallelogram law for the N´eron-Tate height [40, Theorem B.5.1 (c)].
By assumption, there are at most c′
4(g, n, ι) such points. This completes the
reduction. Hence we may and do assume that D = [p] for some p ∈ Cg,n,s(Q) in
the sequel.
Let g ≥ 2 and n ≥ 3 be ﬁxed integers. Consider the Torelli map (with level
structure) τg,n : Mg,n ! Ag,n and the universal family π′
g,n : Cg,n ! Mg,n. We
deﬁne the pullback family

(39) A = (τg,n ◦ π′
g,n)∗Bg,n −! S = Cg,n.

Consider the injective Cg,n-morphism

ϕg,n : Cg,n ×Mg,n Cg,n −! A, (p, q) ↦−! [q] − [p] ∈ Ap.

As the family πg,n : Bg,n ! Ag,n is projective, so is its pullback (39) by [35,
Proposition 5.5.5 (iii)]. By [35, Proposition 5.3.4 (ii) and Th´eor`eme 5.5.3 (i)], S
is quasi-projective over Q as π′
g,n is projective and Mg,n is quasi-projective. For
the same reason, the variety Bg,n is quasi-projective over Q and we can choose
an immersion ι : Bg,n ֒! PN
Q .
Let C be an irreducible component of the subvariety ϕg,n(Cg,n ×Mg,n Cg,n) ⊆ A,
which evidently satisﬁes condition (i) of Proposition 26. As the Jacobian As
represents Pic0(Cs), it is generated by Cs − Cs. Hence (ii) is satisﬁed as well.
Condition (iii) follows from the Torelli theorem [3, Section VI.3] (see also [70,
Lemma 1.11]) and the fact that, for each curve Y of genus ≥ 2, the subvariety
Y − Y ⊆ Jac(Y ) has dimension 2. Applying the proposition to each irreducible
component C individually, we obtain Theorem 3. □

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 41

In the sequel, we work with a ﬁxed number ﬁeld K and a ﬁxed archimedean
place ν ∈ Σ(K). Therefore, we write ZC for the base change Z ×K Cν and Z(C)
for the complex analytic space Z an
Cν . In addition, we write µ and O(x) instead
of µν and Oν(x), respectively. Recall the (1, 1)-form β on A(C) from Lemma 7.
Furthermore, we use the notations A
[n], X [n], π[n], and ι
[n] as in Section 2. We
write η for the generic point of the base variety S.
Instead of proving Proposition 26 directly, we ﬁrst reduce to another proposi-
tion that is easier to work with.

Proposition 27. Let K be a number ﬁeld and ν an archimedean place of K.
Consider a smooth, geometrically irreducible, quasi-projective variety S over K,
a principally polarized abelian scheme π : A ! S of relative dimension g, an
immersion ι : A ֒! PN
K, and a geometrically irreducible subvariety C ⊆ A such
that π(C) = S and dim(C) = dim(S) + 1.
Assume that the generic stabilizer StabAη (Cη) is trivial and that C [m′] ⊆ A
[m′]

is a non-degenerate geometrically irreducible subvariety for some integer m
′ ≥
2. Then, there exists an algebraic subvariety Z ⊊ S of codimension ≥ 1 and
constants c27 = c27(C, ι, m
′), c28 = c28(C, ι, m
′) > 0 such that

(40) #{x ∈ Cs(Q) | ̂h(x) < c27} ≤ c28

for all s ∈ S \ Z(Q).

Let us start with the reduction.

Proof of Proposition 26 using Proposition 27. Using an induction on s = dim(S),
it clearly suﬃces to prove (40) for all x ∈ U(Q) in a dense open subset U ⊆ S.
In particular, we can assume that S is smooth in the following. Furthermore, we
may and do assume that A, S, π, ι, and κ are all deﬁned over a number ﬁeld K.
The case dim(S) = 0 reduces to the classical Bogomolov conjecture [87, 97], but
our proof actually contains this case as well, by specializing to the argument of
[97, Section 4] with some unnecessary modiﬁcations.
Choose some m
′ ≥ dim(S). As the generic ﬁber C [m′]
η is irreducible, we may
shrink S to ensure that C [m′] is irreducible. (Recall that the irreducible com-
ponents of C [m′] meeting the generic ﬁber π−1(η) are in a one-to-one with the
irreducible components of C [m′]
η . Compare [34, (0.2.1.8)].) By [23, Theorem 1.3
(i)]13, the ﬁbered self-product C [m′] is non-degenerate.
Writing η for the generic point of S, the stabilizer Stab(Cη) of Cη in Aη is
a ﬁnite torsion subgroup. In fact, each element of the stabilizer induces a non-
trivial automorphism of Cη. By Hurwitz Theorem [58, Theorem III.3.9], there
are only ﬁnitely many such automorphisms since Cη has genus ≥ 2.
The isogeny Aη ։ Aη/Stab(Cη) extends from the generic ﬁber to some dense
open set U ⊆ S. After shrinking S, we may assume that there exists an abelian

13In a previous version of this paper, the stronger result [23, Theorem 1.3 (ii)] was used,
which missed a condition that is actually violated in the situation here. The reader is referred
to the corrigendum [25].

42 LARS K ¨UHNE

S-scheme π′ : A
′ ! S and an isogeny q : A ! A
′. Furthermore, the image
C ′ = q(C) still has the property that C ′
s is a projective, irreducible curve for
each geometric point s of S, although it is not necessarily smooth anymore. By
construction, the stabilizer of C ′
η in A
′
η is trivial, and the subvariety

(C ′)[m′] = (q × · · · × q)(C [m′]) ⊆ (A
′)[m′]

is non-degenerate by Lemma 14.
After shrinking S further, we can also assume that there exists a dual isogeny
q′ : A
′ ! A such that q ◦ q′ = [deg(qη)]A′ and q′ ◦ q = [deg(qη)]A. The pullback
(q′)∗ι
∗O(1) along the ﬁnite map q′ is relatively ample with respect to π′ : A
′ ! S
by [1, Tags 01VJ and 0892 (b)], so there exist positive integers a, b such that
the b-th power of the line bundle (q′)∗ι
∗O(1) ⊗ (π′)∗κ
∗O(a) is very ample by [1,
Tag 0892 (a)]. Write ι
′ : A
′ ֒! PN ′
K for an associated projective immersion by
means of a basis of its global sections. From the functoriality of the ﬁberwise
N´eron-Tate height, it is easy to see that, for every point x ∈ A
′(Q),

(41) ̂hι′(q(x)) = b · ̂h(q′(q(x))) = b · deg(qη)2 · ̂h(x)

where we set ̂hι′(x) = limk!∞(hO(1)(ι
′([n
k](x)))/n
2k). The subvariety C ′ ⊆ A
′

satisﬁes the assumptions of Proposition 27. Shrinking S further, we may hence
assume that #{x ∈ C ′
s(Q) | ̂hι′(x) < c27} ≤ c28
for all s ∈ S(Q). The assertion of Proposition 26 follows from (41). □

Proof of Proposition 27. Our ﬁrst goal is to prove that, if the assertion of the
proposition is violated, there exists a Zariski-dense sequence (xi) ∈ C N of closed
points such that ̂h(xi) ! 0. In this case, there exists a Zariski-dense sequence
(sk) ∈ S(Q)N such that the sets

Σk := {
x ∈ Csk(Q) | ̂h(x) < (k + 1)−1}

satisfy #Σk ! ∞ as k ! ∞. Out of this, we can construct a sequence (xi) ∈
C N of closed points whose elements are the closed points corresponding to the
rational points ⋃∞
k=0 Σk ⊆ C(Q).
We next show by induction that such a sequence (xi) is either Zariski-dense
in C N or there is nothing left to prove. In fact, suppose that there exists a
Zariski-closed subset Z ⊊ C containing all elements of the sequence (xi). Then,
Z contains also Σk for any k ≥ 0. As (sk) is Zariski-dense, we have π(Z) = S. By
reasons of dimension, the generic ﬁber Zη is a ﬁnite union of closed points in the
generic ﬁber Cη. Depriving S of a codimension ≥ 1 subset, we can hence assume
that each geometric ﬁber Zs consists of closed points whose number is uniformly
bounded. But this implies that #Σk is uniformly bounded for inﬁnitely many
k ≥ 0, which is a contradiction. The claim follows.
We continue with describing the setting for our equidistribution argument,
following Ullmo [87] and Zhang [97]. For given integers m ≥ 2 and m
′ ≥ 1, we

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 43

deﬁne the map

∆0 : A
[mm′] −! A
[(m−1)m′],

(x1, x2, . . . , xm) ↦−! (x1 − x2, x2 − x3, . . . , xm−1 − xm),

with each xi, 1 ≤ i ≤ m, indicating an element of A
[m′]. In addition, we set

∆ = ∆0 ×S idA[m′] : A
[mm′] ×S A
[m′] −! A
[(m−1)m′] ×S A
[m′].

The triviality of Stab(Cη) implies that Stab(C [m′]
η ) = Stab(Cη)m′ is trivial
as well. Thus, we can apply [2, Lemma 4.1] for C [m′]
η , obtaining some integer
m0 > 0 such that ∆0|C[mm′]
η : C [mm′]
η ! ∆0(C [mm′])η is birational for all m ≥ m0.

Consequently, there exists a Zariski-open subset V ⊆ C [(m+1)m′] such that ∆|V :
V ! ∆(V ) is an isomorphism onto an open subset ∆(V ) of ∆(C [(m+1)m′]).
For an arbitrary bijection ϕ = (ϕ1, . . . , ϕ(m+1)m′) : N ! N(m+1)m′ , the sequence

yi = (xϕ1(i), xϕ2(i), . . . , xϕ(m+1)m′ (i)) ∈ C (m+1)m′

is again Zariski-dense and satisﬁes ̂hι[(m+1)m′](yi) ! 0. Using [97, Lemma 4.1], we
may even assume that (yi) is Zariski-generic by passing to a subsequence. The
image sequence (∆(yi)) is then also Zariski-generic in ∆(C [(m+1)m′]). Further-
more, we can assume that yi /∈ V for all i ∈ N.
For each integer n ≥ 1, we write β[n] for the (1, 1)-form deﬁned for π[n] : A
[n] !
S in Lemma 7. After shrinking S, both C [(m+1)m′] and ∆(C [(m+1)m′]) are non-
degenerate by Lemmas 12 and 13. Therefore, Theorem 1 (and its proof) applies
to the sequences (yi) and (∆(yi)). For all functions f ∈ C0
c (C [(m+1)m′](C)) and
g ∈ C0
c (∆(C [(m+1)m′])(C)), we get

(42) 1
#O(yi)
 ∑

z∈O(yi) f (z) −! ∫
C[(m+1)m′](C) f µ1

where µ1 = k
−1
C[(m+1)m′] · (β[(m+1)m′])|∧((m+1)m′+s)
C[(m+1)m′]
and

(43) 1
#O(∆(yi))
 ∑

z∈O(∆(yi)) g(z) −! ∫

∆(C[(m+1)m′])(C) gµ2

where µ2 = k
−1
∆(C[(m+1)m′]) · (β[mm′])|∧((m+1)m′ +s)
∆(C[(m+1)m′])
as i ! ∞. We abuse notation and consider µ1 and µ2 as volume forms in the
sequel.
Every f ∈ C 0
c (V (C)) can be written as f = g ◦ ∆ for some g ∈ C 0
c (∆(V )(C))).
Applying (42) and (43) to f and g respectively, we obtain
∫

C[(m+1)m′](C) f µ1 = ∫
∆(C[(m+1)m′])(C) gµ2 = ∫

C[(m+1)m′](C) f ∆
∗µ2

44 LARS K ¨UHNE

for all f ∈ C 0
c (V (C)). Note that the substitution rule used here applies indeed
also for singular analytic spaces (see the remark in our subsection on Notations
and Conventions above). We infer that µ1 and ∆
∗µ2 coincide on V (C). As they
are real-analytic and V (C) is dense in C [(m+1)m′](C), this implies µ1 = ∆
∗µ2.
This contradicts Lemma 15. Hence, the assertion of the proposition has to hold
true. □

Acknowledgements: The author thanks Laura DeMarco, Gabriel Dill, Ziyang
Gao, Thomas Gauthier, Philipp Habegger, Myrto Mavraki, Fabien Pazuki, Harry
Schmidt, Robert Wilms, Xinyi Yuan for advice, comments, discussions, and en-
couragement. In particular, he thanks Laura DeMarco for informing him about
Gauthier and Vigny’s result [29, Proposition 13], Xinyi Yuan for sharing the
preprint [92], and Thomas Gauthier for sharing his preprint [28]. Furthermore,
he thanks Thomas Gauthier and Xinyi Yuan for pointing out an error in the
author’s previous proof of Lemma 23 and the original version of Theorem 1. Fi-
nally, he thanks the three referees for their good advice and many comments,
which have substantially contributed to both the mathematical and expository
quality of this article.
Funding: The author acknowledges ﬁnancial support of the Swiss National
Science Foundation through an Ambizione Grant in the early stage of this project.
The author also received funding from the European Union Horizon 2020 research
and innovation programme under the Marie Sklodowska-Curie grant agreement
No. 101027237.
 References

[1] The Stacks Project. http://stacks.math.columbia.edu, 2015.
[2] Ahmed Abbes. Hauteurs et discr´etude (d’apr`es L. Szpiro, E. Ullmo et S. Zhang).
Ast´erisque, (245):Exp. No. 825, 4, 141–166, 1997. S´eminaire Bourbaki, Vol. 1996/97.
[3] Enrico Arbarello, Maurizio Cornalba, Phillip A. Griﬃths, and Joe Harris. Geometry of
algebraic curves. Vol. I, volume 267 of Grundlehren der Mathematischen Wissenschaften.
Springer-Verlag, New York, 1985.
[4] Christina Birkenhake and Herbert Lange. Complex abelian varieties, volume 302 of
Grundlehren der Mathematischen Wissenschaften. Springer-Verlag, Berlin, second edi-
tion, 2004.
[5] Enrico Bombieri. The Mordell conjecture revisited. Ann. Scuola Norm. Sup. Pisa Cl. Sci.
(4), 17(4):615–640, 1990.
[6] Enrico Bombieri and Walter Gubler. Heights in Diophantine geometry, volume 4 of New
Mathematical Monographs. Cambridge University Press, Cambridge, 2006.
[7] Jean-Benoˆıt Bost, Henri Gillet, and Christophe Soul´e. Heights of projective varieties and
positive Green forms. J. Amer. Math. Soc., 7(4):903–1027, 1994.
[8] Jos´e Ignacio Burgos Gil, David Holmes, and Robin De Jong. Singularities of the biexten-
sion metric for families of abelian varieties. Forum Math. Sigma, 6:e12, 2018.
[9] Jos´e Ignacio Burgos Gil, J¨urg Kramer, and Ulf K¨uhn. The singularities of the invariant
metric on the Jacobi line bundle. In Recent advances in Hodge theory, volume 427 of
London Math. Soc. Lecture Note Ser., pages 45–77. Cambridge Univ. Press, Cambridge,
2016.
[10] Claude Chabauty. Sur les points rationnels des courbes alg´ebriques de genre sup´erieur `a
l’unit´e. C. R. Acad. Sci. Paris, 212:882–885, 1941.

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 45

[11] Robert F. Coleman. Eﬀective Chabauty. Duke Math. J., 52(3):765–770, 1985.
[12] Pietro Corvaja, Julian Demeio, David Masser, and Umberto Zannier. On the torsion values
for sections of an elliptic scheme. J. Reine Angew. Math., 782:1–41, 2022.
[13] Sinnou David and Patrice Philippon. Minorations des hauteurs normalis´ees des sous-
vari´et´es des puissances des courbes elliptiques. Int. Math. Res. Pap. IMRP, (3):Art. ID
rpm006, 113, 2007.
[14] Pierre Deligne and David Mumford. The irreducibility of the space of curves of given
genus. Inst. Hautes ´Etudes Sci. Publ. Math., (36):75–109, 1969.
[15] Jean-Pierre Demailly. Monge-Amp`ere operators, Lelong numbers and intersection theory.
In Complex analysis and geometry, Univ. Ser. Math., pages 115–193. Plenum, New York,
1993.
[16] Laura DeMarco, Holly Krieger, and Hexi Ye. Uniform Manin-Mumford for a family of
genus 2 curves. Ann. of Math. (2), 191(3):949–1001, 2020.
[17] Laura DeMarco and Niki M Mavraki. Variation of canonical height and equidistribution.
Amer. J. Math., 142(2):443–473, 2020.
[18] Vesselin Dimitrov, Ziyang Gao, and Philipp Habegger. Uniform bound for the number of
rational points on a pencil of curves. Int. Math. Res. Not. IMRN, (2):1138–1159, 2021.
[19] Vesselin Dimitrov, Ziyang Gao, and Philipp Habegger. Uniformity in Mordell-Lang for
curves. Ann. of Math. (2), 194(1):237–298, 2021.
[20] Vesselin Dimitrov, Ziyang Gao, and Philipp Habegger. A consequence of the relative
Bogomolov conjecture. J. Number Theory, 230:146–160, 2022.
[21] Gerd Faltings. Diophantine approximation on abelian varieties. Ann. of Math. (2),
133(3):549–576, 1991.
[22] William Fulton. Intersection theory, volume 2 of Ergebnisse der Mathematik und ihrer
Grenzgebiete (3). Springer-Verlag, Berlin, second edition, 1998.
[23] Ziyang Gao. Generic rank of Betti map and unlikely intersections. Compos. Math.,
156(12):2469–2509, 2020.
[24] Ziyang Gao. Mixed Ax-Schanuel for the universal abelian varieties and some applications.
Compos. Math., 156(11):2263–2297, 2020.
[25] Ziyang Gao. Corrigendum: Generic rank of Betti map and unlikely intersections. Compos.
Math., 157(12):2747–2748, 2021.
[26] Ziyang Gao. Recent developments of the Uniform Mordell-Lang Conjecture. arXiv e-prints,
page arXiv:2104.03431, April 2021.
[27] Ziyang Gao, Tangli Ge, and Lars K¨uhne. The Uniform Mordell-Lang Conjecture. arXiv
e-prints, page arXiv:2105.15085, May 2021.
[28] Thomas Gauthier. Good height functions on quasi-projective varieties: equidistribution
and applications in dynamics. arXiv e-prints, page arXiv:2105.02479, May 2021.
[29] Thomas Gauthier and Gabriel Vigny. The Geometric Dynamical Northcott and Bogo-
molov Properties. arXiv e-prints, page arXiv:1912.07907, December 2019.
[30] Henri Gillet and Christophe Soul´e. Arithmetic intersection theory. Inst. Hautes ´Etudes
Sci. Publ. Math., (72):93–174 (1991), 1990.
[31] Ulrich G¨ortz and Torsten Wedhorn. Algebraic geometry II: Cohomology of schemes—
with examples and exercises. Springer Studium Mathematik—Master. Springer Spektrum,
Wiesbaden, 2023.
[32] Hans Grauert, Thomas Peternell, and Reinhold Remmert, editors. Several complex vari-
ables. VII, volume 74 of Encyclopaedia of Mathematical Sciences. Springer-Verlag, Berlin,
1994. Sheaf-theoretical methods in complex analysis.
[33] Phillip Griﬃths and Joseph Harris. Principles of algebraic geometry. Wiley Classics Li-
brary. John Wiley & Sons, Inc., New York, 1994. Reprint of the 1978 original.
[34] Alexander Grothendieck. ´El´ements de g´eom´etrie alg´ebrique. I. Le langage des sch´emas.
Inst. Hautes ´Etudes Sci. Publ. Math., (4):228, 1960.

46 LARS K ¨UHNE

[35] Alexander Grothendieck. ´El´ements de g´eom´etrie alg´ebrique. II. ´Etude globale ´el´ementaire
de quelques classes de morphismes. Inst. Hautes ´Etudes Sci. Publ. Math., (8):222, 1961.
[36] Walter Gubler. Heights of subvarieties over M -ﬁelds. In Arithmetic geometry (Cortona,
1994), Sympos. Math., XXXVII, pages 190–227. Cambridge Univ. Press, Cambridge, 1997.
[37] Walter Gubler. Local heights of subvarieties over non-Archimedean ﬁelds. J. Reine Angew.
Math., 498:61–113, 1998.
[38] Walter Gubler. Local and canonical heights of subvarieties. Ann. Sc. Norm. Super. Pisa
Cl. Sci. (5), 2(4):711–760, 2003.
[39] Robert C. Gunning. Introduction to holomorphic functions of several variables. Vol. II.
The Wadsworth & Brooks/Cole Mathematics Series. Wadsworth & Brooks/Cole Advanced
Books & Sostware, Monterey, CA, 1990. Local theory.
[40] Marc Hindry and Joseph H. Silverman. Diophantine geometry, volume 201 of Graduate
Texts in Mathematics. Springer-Verlag, New York, 2000.
[41] Ehud Hrushovski. The Manin-Mumford conjecture and the model theory of diﬀerence
ﬁelds. Ann. Pure Appl. Logic, 112(1):43–115, 2001.
[42] Daniel Huybrechts. Complex geometry. Universitext. Springer-Verlag, Berlin, 2005.
[43] Hideaki Ikoma. Boundedness of the successive minima on arithmetic varieties. J. Algebraic
Geom., 22(2):249–302, 2013.
[44] Eric Katz, Joseph Rabinoﬀ, and David Zureick-Brown. Uniform bounds for the number of
rational points on curves of small Mordell-Weil rank. Duke Math. J., 165(16):3189–3240,
2016.
[45] Steven L. Kleiman. Toward a numerical theory of ampleness. Ann. of Math. (2), 84:293–
344, 1966.
[46] Maciej Klimek. Pluripotential theory, volume 6 of London Mathematical Society Mono-
graphs. New Series. The Clarendon Press, Oxford University Press, New York, 1991.
Oxford Science Publications.
[47] J´anos Koll´ar. Rational curves on algebraic varieties, volume 32 of Ergebnisse der Mathe-
matik und ihrer Grenzgebiete (3). Springer-Verlag, Berlin, 1996.
[48] Lars K¨uhne. The bounded height conjecture for semiabelian varieties. Compos. Math.,
156(7):1405–1456, 2020.
[49] Lars K¨uhne. Points of small height on semiabelian varieties. J. Eur. Math. Soc. (JEMS),
24(6):2077–2131, 2022.
[50] Lars K¨uhne. The relative Bogomolov conjecture for ﬁbered products of elliptic curves. J.
Reine Angew. Math., 795:243–270, 2023.
[51] Pierre Lelong. Int´egration sur un ensemble analytique complexe. Bull. Soc. Math. France,
85:239–262, 1957.
[52] Qing Liu. Algebraic geometry and arithmetic curves, volume 6 of Oxford Graduate Texts
in Mathematics. Oxford University Press, Oxford, 2002. Translated from the French by
Reinie Ern´e, Oxford Science Publications.
[53] Nicole Looper, Joseph Silverman, and Robert Wilms. A uniform quantitative Manin-
Mumford theorem for curves over function ﬁelds. arXiv e-prints, page arXiv:2101.11593,
January 2021.
[54] Yuri I. Manin and Yuri G. Zarhin. Height on families of abelian varieties. Mat. Sb. (N.S.),
89(131):171–181, 349, 1972.
[55] David Masser. Specializations of ﬁnitely generated subgroups of abelian varieties. Trans.
Amer. Math. Soc., 311(1):413–424, 1989.
[56] Barry Mazur. Arithmetic on curves. Bull. Amer. Math. Soc. (N.S.), 14(2):207–259, 1986.
[57] Barry Mazur. Abelian varieties and the Mordell-Lang conjecture. In Model theory, algebra,
and geometry, volume 39 of Math. Sci. Res. Inst. Publ., pages 199–227. Cambridge Univ.
Press, Cambridge, 2000.

EQUIDISTRIBUTION IN FAMILIES OF ABELIAN VARIETIES 47

[58] Rick Miranda. Algebraic curves and Riemann surfaces, volume 5 of Graduate studies in
Mathematics. American Mathematical Society, Providence, RI, 1995.
[59] Atsushi Moriwaki. Arakelov geometry, volume 244 of Translations of Mathematical Mono-
graphs. American Mathematical Society, Providence, RI, 2014. Translated from the 2008
Japanese original.
[60] David Mumford. A remark on Mordell’s conjecture. Amer. J. Math., 87:1007–1016, 1965.
[61] David Mumford. Families of abelian varieties. In Algebraic Groups and Discontinuous
Subgroups (Proc. Sympos. Pure Math., Boulder, Colo., 1965), pages 347–351. Amer. Math.
Soc., Providence, R.I., 1966.
[62] David Mumford. On the equations deﬁning abelian varieties. I. Invent. Math., 1:287–354,
1966.
[63] David Mumford. On the equations deﬁning abelian varieties. II. Invent. Math., 3:75–135,
1967.
[64] David Mumford. Abelian varieties. Tata Institute of Fundamental Research studies in
Mathematics, No. 5. Published for the Tata Institute of Fundamental Research, Bombay,
1970.
[65] David Mumford, John Fogarty, and Frances Kirwan. Geometric invariant theory, vol-
ume 34 of Ergebnisse der Mathematik und ihrer Grenzgebiete (2). Springer-Verlag, Berlin,
third edition, 1994.
[66] J¨urgen Neukirch. Algebraic number theory, volume 322 of Grundlehren der Mathematis-
chen Wissenschasten. Springer-Verlag, Berlin, 1999. Translated from the 1992 German
original and with a note by Norbert Schappacher, With a foreword by G. Harder.
[67] Martin Olsson. Compactiﬁcations of moduli of abelian varieties: an introduction. In Cur-
rent developments in algebraic geometry, volume 59 of Math. Sci. Res. Inst. Publ., pages
295–348. Cambridge Univ. Press, Cambridge, 2012.
[68] Martin C. Olsson. Compactifying moduli spaces for abelian varieties, volume 1958 of Lec-
ture Notes in Mathematics. Springer-Verlag, Berlin, 2008.
[69] Frans Oort. Finite group schemes, local moduli for abelian varieties, and lifting problems.
Compositio Math., 23:265–296, 1971.
[70] Frans Oort and Joseph Steenbrink. The local Torelli problem for algebraic curves. In
Journ´ees de G´eometrie Alg´ebrique d’Angers, Juillet 1979/Algebraic Geometry, Angers,
1979, pages 157–204. Sijthoﬀ & Noordhoﬀ, Alphen aan den Rijn—Germantown, Md.,
1980.
[71] Fabien Pazuki. Bornes sur le nombre de points rationnels des courbes: en quˆete
d’uniformit´e. In Arithmetic, geometry, cryptography and coding theory, volume 770 of
Contemp. Math., pages 253–266. Amer. Math. Soc., [Providence], RI, 2021. With an ap-
pendix by Sinnou David and Patrice Philippon.
[72] Jonathan Pila and Umberto Zannier. Rational points in periodic analytic sets and the
Manin-Mumford conjecture. Atti Accad. Naz. Lincei Cl. Sci. ﬁs. Mat. Natur. Rend. Lincei
(9) Mat. Appl., 19(2):149–162, 2008.
[73] Richard Pink. A common generalization of the conjectures of Andr´e-Oort, Manin-
Mumford, and Mordell-Lang. available from http://www.math.ethz.ch/~pink, 04 2005.
[74] Michel Raynaud. Courbes sur une vari´et´e ab´elienne et points de torsion. Invent. Math.,
71(1):207–233, 1983.
[75] Ga¨el R´emond. D´ecompte dans une conjecture de Lang. Invent. Math., 142(3):513–545,
2000.
[76] Ga¨el R´emond. In´egalit´e de Vojta en dimension sup´erieure. Ann. Scuola Norm. Sup. Pisa
Cl. Sci. (4), 29(1):101–151, 2000.
[77] Steven Roman. Advanced linear algebra, volume 135 of Graduate Texts in Mathematics.
Springer, New York, second edition, 2005.

48 LARS K ¨UHNE

[78] Jean-Pierre Serre. Rigidit´e du foncteur de jacobi d’´echelon n ≥ 3 (appendice `a l’expos´e
17). In S´eminaire Henri Cartan, 13i`eme ann´ee: 1960/61. Familles d’espaces complexes et
fondements de la g´eom´etrie analytique. Fasc. 1 et 2: Exp. 1–21, 2i`eme ´edition, corrig´ee.
´Ecole Normale Sup´erieure, pages Fasc. 1 (Exp. 1–13), ii+148 pp.; Fasc. 2 (Exp. 14–21),
ii+11. Secr´etariat math´ematique, Paris, 1962.
[79] Joseph H. Silverman. Arithmetic distance functions and height functions in Diophantine
geometry. Math. Ann., 279(2):193–216, 1987.
[80] Joseph H. Silverman. Variation of the canonical height on elliptic surfaces. I. Three ex-
amples. J. Reine Angew. Math., 426:151–178, 1992.
[81] Joseph H. Silverman. Variation of the canonical height on elliptic surfaces. II. Local ana-
lyticity properties. J. Number Theory, 48(3):291–329, 1994.
[82] Joseph H. Silverman. Variation of the canonical height on elliptic surfaces. III. Global
boundedness properties. J. Number Theory, 48(3):330–352, 1994.
[83] Ernst Snapper. Polynomials associated with divisors. J. Math. Mech., 9:123–139, 1960.
[84] Christophe Soul´e. Lectures on Arakelov geometry, volume 33 of Cambridge studies in
Advanced Mathematics. Cambridge University Press, Cambridge, 1992. With the collabo-
ration of D. Abramovich, J.-F. Burnol and J. Kramer.
[85] Michael Stoll. Uniform bounds for the number of rational points on hyperelliptic curves
of small Mordell-Weil rank. J. Eur. Math. Soc. (JEMS), 21(3):923–956, 2019.
[86] Lucien Szpiro, Emmanuel Ullmo, and Shou-Wu Zhang. ´Equir´epartition des petits points.
Invent. Math., 127(2):337–347, 1997.
[87] Emmanuel Ullmo. Positivit´e et discr´etion des points alg´ebriques des courbes. Ann. of
Math. (2), 147(1):167–179, 1998.
[88] Claire Voisin. Hodge theory and complex algebraic geometry. I, volume 76 of Cambridge
studies in Advanced Mathematics. Cambridge University Press, Cambridge, english edi-
tion, 2007. Translated from the French by Leila Schneps.
[89] Paul Vojta. Siegel’s theorem in the compact case. Ann. of Math. (2), 133(3):509–548,
1991.
[90] Paul Vojta. Integral points on subvarieties of semiabelian varieties. II. Amer. J. Math.,
121(2):283–313, 1999.
[91] Robert Wilms. Degeneration of Riemann theta functions and of the Zhang-Kawazumi
invariant with applications to a uniform Bogomolov conjecture. arXiv e-prints, page
arXiv:2101.04024, January 2021.
[92] Xinyi Yuan. Arithmetic bigness and a uniform Bogomolov-type result. to appear in Ann.
Math. (2).
[93] Xinyi Yuan. Big line bundles over arithmetic varieties. Invent. Math., 173(3):603–649,
2008.
[94] Xinyi Yuan and Shou-Wu Zhang. Adelic line bundles over quasi-projective varieties. arXiv
e-prints, page arXiv:2105.13587, May 2021.
[95] Shou-Wu Zhang. Positive line bundles on arithmetic varieties. J. Amer. Math. Soc.,
8(1):187–221, 1995.
[96] Shou-Wu Zhang. Small points and adelic metrics. J. Algebraic Geom., 4(2):281–300, 1995.
[97] Shou-Wu Zhang. Equidistribution of small points on abelian varieties. Ann. of Math. (2),
147(1):159–165, 1998.
[98] Shou-Wu Zhang. Small points and Arakelov theory. In Proceedings of the International
Congress of Mathematicians, Vol. II (Berlin, 1998), number Extra Vol. II, pages 217–225,
1998.
Email address: lars.kuehne@ucd.ie

UCD School of Mathematics and Statistics, University College Dublin, Belfield,
Dublin 4, Ireland
