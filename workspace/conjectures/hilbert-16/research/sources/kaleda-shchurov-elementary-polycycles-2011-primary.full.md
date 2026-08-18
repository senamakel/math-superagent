<!-- source: https://arxiv.org/pdf/1102.1234 | converted from PDF -->

arXiv:1102.1234v5  [math.AT]  6 Feb 2013
HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN
HOMOLOGY OF STRUCTURED RING SPECTRA

JOHN E. HARPER AND KATHRYN HESS

Abstract. Working in the context of symmetric spectra, we describe and
study a homotopy completion tower for algebras and left modules over operads
in the category of modules over a commutative ring spectrum (e.g., structured
ring spectra). We prove a strong convergence theorem that for 0-connected
algebras and modules over a (−1)-connected operad, the homotopy completion
tower interpolates (in a strong sense) between topological Quillen homology
and the identity functor.
By systematically exploiting strong convergence, we prove several theo-
rems concerning the topological Quillen homology of algebras and modules
over operads. These include a theorem relating ﬁniteness properties of topo-
logical Quillen homology groups and homotopy groups that can be thought
of as a spectral algebra analog of Serre’s ﬁniteness theorem for spaces and
H.R. Miller’s boundedness result for simplicial commutative rings (but in re-
verse form). We also prove absolute and relative Hurewicz theorems and a
corresponding Whitehead theorem for topological Quillen homology. Further-
more, we prove a rigidiﬁcation theorem, which we use to describe completion
with respect to topological Quillen homology (or TQ-completion). The TQ-
completion construction can be thought of as a spectral algebra analog of
Sullivan’s localization and completion of spaces, Bousﬁeld-Kan’s completion
of spaces with respect to homology, and Carlsson’s and Arone-Kankaanrinta’s
completion and localization of spaces with respect to stable homotopy. We
prove analogous results for algebras and left modules over operads in un-
bounded chain complexes.
 1. Introduction

Associated to each non-unital commutative ring X is the completion tower aris-
ing in commutative ring theory

X/X 2 ← X/X 3 ← · · · ← X/X n ← X/X n+1 ← · · ·(1.1)

of non-unital commutative rings. The limit of the tower (1.1) is the completion
X ∧ of X, which is sometimes also called the X-adic completion of X. Here, X/X n

denotes the quotient of X in the underlying category by the image of the multi-
plication map X ⊗n−→X. In algebraic topology, algebraic K-theory, and derived
algebraic geometry, it is common to encounter objects that are naturally equipped
with algebraic structures more general than, for example, commutative rings, but
that share certain formal similarities with these classical algebraic structures. A
particularly useful and interesting class of such generalized algebraic structures are
those that can be described as algebras and modules over operads; see Fresse [20],
Goerss-Hopkins [26], Kriz-May [42], Mandell [51], and McClure-Smith [56].
These categories of (generalized) algebraic structures can often be equipped with
an associated homotopy theory, or Quillen model category structure, which allows

1

2 JOHN E. HARPER AND KATHRYN HESS

one to construct and calculate derived functors on the associated homotopy cate-
gory. In [59, II.5], Quillen deﬁnes “homology” in the general context of a model
category—now called Quillen homology—to be the left derived functor of abelian-
ization, if it exists. Quillen homology often behaves very much like the ordinary
homology of topological spaces, which it recovers as a special case. Quillen [60]
and Andr´e [1] originally developed and studied a particular case of Quillen’s no-
tion of homology for the special context of commutative rings, now called Andr´e-
Quillen homology. A useful introduction to Quillen homology is given in Goerss-
Schemmerhorn [28]; see also Goerss [24] and H.R. Miller [57] for a useful develop-
ment (from a homotopy viewpoint) in the case of augmented commutative algebras.
In this paper we are primarily interested in the topological analog of Quillen ho-
mology, called topological Quillen homology, for (generalized) algebraic structures
on spectra. The topological analog for commutative ring spectra, called topological
Andr´e-Quillen homology, was originally studied by Basterra [6]; see also Baker-
Gilmour-Reinhard [4], Baker-Richter [5], Basterra-Mandell [7, 8], Goerss-Hopkins
[25], Lazarev [46], Mandell [52], Richter [62], Rognes [63, 64] and Schwede [65, 67].

Basic Assumption 1.2. From now on in this paper, we assume that R is any com-
mutative ring spectrum; i.e., we assume that R is any commutative monoid object
in the category (SpΣ, ⊗S, S) of symmetric spectra [39, 68]. Here, the tensor product
⊗S denotes the usual smash product [39, 2.2.3] of symmetric spectra (Remark 4.31).

Remark 1.3. Among structured ring spectra we include many diﬀerent types of alge-
braic structures on spectra (resp. R-modules) including (i) associative ring spectra,
which we simply call ring spectra, (ii) commutative ring spectra, (iii) all of the
En ring spectra for 1 ≤ n ≤ ∞ that interpolate between these two extremes of
non-commutativity and commutativity, together with (iv) any generalized algebra
spectra (resp. generalized R-algebras) that can be described as algebras over op-
erads in spectra (resp. R-modules). It is important to note that the generalized
class of algebraic structures in (iv) includes as special cases all of the others (i)–
(iii). The area of stable homotopy theory that focuses on problems arising from
constructions involving diﬀerent types of structured ring spectra, their modules,
and their homotopy invariants, is sometimes called brave new algebra or spectral
algebra.

In this paper we describe and study a (homotopy invariant) spectral algebra
analog of the completion tower (1.1) arising in commutative ring theory. The tower
construction is conceptual and provides a sequence of reﬁnements of the Hurewicz
map for topological Quillen homology. More precisely, if O is an operad in R-
modules such that O[0] is trivial (i.e., O-algebras are non-unital ), we associate to
O itself a tower
 τ1O ← τ2O ← · · · ← τk−1O ← τkO ← · · ·

of (O, O)-bimodules, which for any O-algebra X induces the completion tower

τ1O ◦O (X) ← τ2O ◦O (X) ← · · · ← τk−1O ◦O (X) ← τkO ◦O (X) ← · · ·

of O-algebras whose limit is the completion X ∧ of X. There is a homotopy theory
of algebras over operads (Theorem 7.15) and this construction is homotopy invari-
ant if applied to coﬁbrant O-algebras. We sometimes refer to the completion tower
of a coﬁbrant replacement X c of X as the homotopy completion tower of X whose
homotopy limit is denoted X h∧. By construction, τ1O ◦O (X c) is the topological

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 3

Quillen homology TQ(X) of X. Hence the homotopy completion tower of X inter-
polates between TQ(X), which is the bottom term of the tower, and the homotopy
completion X h∧ of X.
By systematically exploiting the strong convergence properties of this tower
(Theorem 1.12 and its proof), we prove a selection of theorems concerning the
topological Quillen homology of structured ring spectra. We also prove analogous
results for left modules over operads (Deﬁnition 2.18). The ﬁrst main theorem in
this paper is the following ﬁniteness theorem for topological Quillen homology. It
can be thought of as a structured ring spectra analog of Serre’s ﬁniteness theorem
for spaces (e.g., for the homotopy groups of spheres) and H.R. Miller’s [57, 4.2]
boundedness result for simplicial commutative rings (but in reverse form); for a
related but diﬀerent type of ﬁniteness result in the algebraic context of augmented
commutative algebras over a ﬁeld of non-zero characteristic, see Turner [74]. The
TQ ﬁniteness theorem provides conditions under which topological Quillen homol-
ogy detects certain ﬁniteness properties.

Remark 1.4. In this paper, we say that a symmetric sequence X of symmetric spec-
tra is n-connected if each symmetric spectrum X[t] is n-connected. We say that an
algebra (resp. left module) over an operad is n-connected if the underlying sym-
metric spectrum (resp. symmetric sequence of symmetric spectra) is n-connected,
and similarly for operads.

Theorem 1.5 (TQ ﬁniteness theorem for structured ring spectra). Let O be an
operad in R-modules such that O[0] is trivial. Let X be a 0-connected O-algebra
(resp. left O-module) and assume that O, R are (−1)-connected and πkO[r], πkR
are ﬁnitely generated abelian groups for every k, r.
(a) If the topological Quillen homology groups πkTQ(X) (resp. πkTQ(X)[r])
are ﬁnite for every k, r, then the homotopy groups πkX (resp. πkX[r]) are
ﬁnite for every k, r.
(b) If the topological Quillen homology groups πkTQ(X) (resp. πkTQ(X)[r]) are
ﬁnitely generated abelian groups for every k, r, then the homotopy groups
πkX (resp. πkX[r]) are ﬁnitely generated abelian groups for every k, r.

Since the sphere spectrum S is (−1)-connected and πkS is a ﬁnitely generated
abelian group for every k, we obtain the following immediate corollary.

Corollary 1.6 (TQ ﬁniteness theorem for non-unital commutative ring spectra).
Let X be a 0-connected non-unital commutative ring spectrum. If the topologi-
cal Quillen homology groups πkTQ(X) are ﬁnite (resp. ﬁnitely generated abelian
groups) for every k, then the homotopy groups πkX are ﬁnite (resp. ﬁnitely gener-
ated abelian groups) for every k.

Remark 1.7. Since all of the theorems in this section apply to the special case of
non-unital commutative ring spectra, it follows that each theorem below specializes
to a corollary about non-unital commutative ring spectra, similar to the corollary
above. To avoid repetition, we usually leave the formulation to the reader.

We also prove the following Hurewicz theorem for topological Quillen homol-
ogy. It can be thought of as a structured ring spectra analog of Schwede’s [67,
5.3] simplicial algebraic theories result, Goerss’ [24, 8.3] algebraic result for aug-
mented commutative F2-algebras, Livernet’s [48, 2.13] rational algebraic result for
algebras over operads in non-negative chain complexes over a ﬁeld of characteristic

4 JOHN E. HARPER AND KATHRYN HESS

zero, and Chataur-Rodriguez-Scherer’s [12, 2.1] algebraic result for algebras over
coﬁbrant operads in non-negative chain complexes over a commutative ring. The
TQ Hurewicz theorem provides conditions under which topological Quillen homol-
ogy detects n-connected structured ring spectra. It also provides conditions under
which the ﬁrst non-trivial homotopy group agrees via the Hurewicz map with the
ﬁrst non-trivial topological Quillen homology group.

Theorem 1.8 (TQ Hurewicz theorem for structured ring spectra). Let O be an
operad in R-modules such that O[0] is trivial. Let X be a 0-connected O-algebra
(resp. left O-module), n ≥ 0, and assume that O, R are (−1)-connected.
(a) Topological Quillen homology TQ(X) is n-connected if and only if X is
n-connected.
(b) If topological Quillen homology TQ(X) is n-connected, then the natural
Hurewicz map πkX−→πkTQ(X) is an isomorphism for k ≤ 2n + 1 and
a surjection for k = 2n + 2.

Note that one implication of Theorem 1.8(a) follows from Theorem 1.8(b). We
also prove the following relative Hurewicz theorem for topological Quillen homology,
which we regard as the second main theorem in this paper. It can be thought of
as a structured ring spectra analog of the relative Hurewicz theorem for spaces. It
provides conditions under which topological Quillen homology detects n-connected
maps.

Theorem 1.9 (TQ relative Hurewicz theorem for structured ring spectra). Let O
be an operad in R-modules such that O[0] is trivial. Let f : X−→Y be a map of
O-algebras (resp. left O-modules) and n ≥ 0. Assume that O, R are (−1)-connected.
(a) If X, Y are 0-connected, then f is n-connected if and only if f induces an
n-connected map TQ(X)−→TQ(Y ) on topological Quillen homology.
(b) If X, Y are (−1)-connected and f is (n − 1)-connected, then f induces an
(n − 1)-connected map TQ(X)−→TQ(Y ) on topological Quillen homology.
(c) If f induces an n-connected map TQ(X)−→TQ(Y ) on topological Quillen
homology between (−1)-connected objects, then f induces an (n−1)-connected
map X h∧−→Y h∧ on homotopy completion.
(d) If topological Quillen homology TQ(X) is (n − 1)-connected, then homotopy
completion X h∧ is (n − 1)-connected.
Here, TQ(X)−→TQ(Y ), X h∧−→Y h∧ denote the natural induced zigzags in the cat-
egory of O-algebras (resp. left O-modules) with all backward facing maps weak
equivalences.

Remark 1.10. It is important to note Theorem 1.9(b) implies that the conditions
in Theorem 1.9(c) are satisﬁed if X, Y are (−1)-connected and f is n-connected.

As a corollary we obtain the following Whitehead theorem for topological Quillen
homology. It can be thought of as a structured ring spectra analog of Schwede’s
[67, 5.4] simplicial algebraic theories result, Goerss’ [24, 8.1] algebraic result for
augmented commutative F2-algebras, and Livernet’s [47] rational algebraic result
for algebras over Koszul operads in non-negative chain complexes over a ﬁeld of
characteristic zero. As a special case, it recovers Kuhn’s [43] result for non-unital
commutative ring spectra, and more generally, Lawson’s [45] original structured
ring spectra result (which is based on [32]). The TQ Whitehead theorem provides
conditions under which topological Quillen homology detects weak equivalences.

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 5

Corollary 1.11 (TQ Whitehead theorem for structured ring spectra). Let O be
an operad in R-modules such that O[0] is trivial. Let f : X−→Y be a map of O-
algebras (resp. left O-modules). Assume that O, R are (−1)-connected. If X, Y are
0-connected, then f is a weak equivalence if and only if f induces a weak equivalence
TQ(X) ≃ TQ(Y ) on topological Quillen homology.

Associated to the homotopy completion tower is the homotopy completion spec-
tral sequence, which goes from topological Quillen homology to homotopy comple-
tion (Theorem 1.12). It can be thought of as a structured ring spectra analog of
Quillen’s fundamental spectral sequence [60, 6.9] for commutative rings and the
corresponding spectral sequence studied by Goerss [24, 6.2] for augmented commu-
tative F2-algebras. As a special case, it recovers the spectral sequence in Minasian
[58] for non-unital commutative ring spectra. Under the conditions of Theorem
1.12(b), the homotopy completion spectral sequence is a second quadrant homo-
logically graded spectral sequence and arises from the exact couple of long exact
sequences associated to the homotopy completion tower and its homotopy ﬁbers;
this is the homotopy spectral sequence of a tower of ﬁbrations [9], reindexed as a
homologically graded spectral sequence. For ease of notational purposes, in Theo-
rem 1.12 and Remark 1.13, we regard such towers {As} of ﬁbrations as indexed by
the integers such that As = ∗ for each s < 0.
The third main theorem in this paper is the following strong convergence the-
orem for homotopy completion of structured ring spectra. It can be thought of
as a structured ring spectra analog of Johnson-McCarthy’s [41] rational algebraic
tower results for non-unital commutative diﬀerential graded algebras over a ﬁeld of
characteristic zero. As a special case, it recovers Kuhn’s [43] and Minasian’s [58]
tower results for non-unital commutative ring spectra. For a very restricted class of
coﬁbrant operads in simplicial sets, which they call primitive operads, McCarthy-
Minasian [54] describe a tower that agrees with the completion tower in the special
case of non-unital commutative ring spectra, but that is diﬀerent for most operads.

Theorem 1.12 (Homotopy completion strong convergence theorem). Let O be an
operad in R-modules such that O[0] is trivial. Let f : X−→Y be a map of O-algebras
(resp. left O-modules).

(a) If X is 0-connected and O, R are (−1)-connected, then the natural coaug-
mentation X ≃ X h∧ is a weak equivalence.
(b) If topological Quillen homology TQ(X) is 0-connected and O, R are (−1)-
connected, then the homotopy completion spectral sequence

E1
−s,t = πt−s(is+1O ◦h
τ1O (
TQ(X)
)) =⇒ πt−s(
X h∧)

resp. E1
−s,t[r] = πt−s((
is+1O ◦h
τ1O TQ(X)
)
[r]) =⇒ πt−s(X h∧[r])
, r ≥ 0,

converges strongly (Remark 1.13).
(c) If f induces a weak equivalence TQ(X) ≃ TQ(Y ) on topological Quillen ho-
mology, then f induces a weak equivalence X h∧ ≃ Y h∧ on homotopy com-
pletion.

Remark 1.13. By strong convergence of {Er} to π∗(X h∧) we mean that (i) for each
(−s, t), there exists an r such that Er
−s,t = E∞
−s,t and (ii) for each i, E∞
−s,s+i = 0
except for ﬁnitely many s. Strong convergence implies that for each i, {E∞
−s,s+i} is

6 JOHN E. HARPER AND KATHRYN HESS

the set of ﬁltration quotients from a ﬁnite ﬁltration of πi(X h∧); see, for instance,
Bousﬁeld-Kan [9, IV.5.6, IX.5.3, IX.5.4] and Dwyer [15].

Remark 1.14 (Connections with Goodwillie’s calculus of functors). Regard the ho-
motopy completion tower as a tower of functors on the category of O-algebras, and
consider the case when O[1] = I[1] (Deﬁnition 2.16). Then it follows easily that (i)
the bottom term (or ﬁrst stage) TQ of the tower is 1-excisive in the sense of [30, 44],
(ii) by Theorem 4.21(c), the n-th layer of the tower has the form O[n] ∧ L
Σn TQ
∧Ln,
and (iii) by the connectivity estimates in the proof of Theorem 1.8, the identity func-
tor and the n-th stage of the tower agree to order n in the sense of [30, 1.2]; more
precisely, they satisfy On(0, 1) as deﬁned in [30, 1.2]. Here, ∧
L
Σn , ∧
L are the total left
derived functors of ∧Σn , ∧, respectively. Properties (i)–(iii) illustrate that the ho-
motopy completion tower is the analog, in the context of O-algebras, of Goodwillie’s
Taylor tower of the identity functor. More precisely, according to [30, 1.6, proof of
1.8] and the results in [29] on cubical diagrams, it follows immediately from (i)–(iii)
that there are maps of towers (under the constant tower {id(−)
c}) of levelwise weak
equivalences of the form {Pnid(−)
c} → {PnτnO ◦O (−)
c} ← {τnO ◦O (−)
c} where
(−)
c denotes functorial coﬁbrant replacement (see Deﬁnition 3.13), and hence the
homotopy completion tower is weakly equivalent to the Taylor tower of the identity
functor on O-algebras, provided that the analogs of the appropriate constructions
and results in [29, 30] remain true in the category of O-algebras; this is the subject
of current work, and will not be further elaborated here (but see [44]).
Since in the calculation of the layers in (ii) the operad O plays a role analogous
to that of the Goodwillie derivatives of the identity functor (see [30, 44]), this sheds
some positive light on a conjecture of Arone-Ching [2] that an appropriate model of
the Goodwillie derivatives of the identity functor on O-algebras is weakly equivalent
as an operad to O itself.

The following relatively weak coﬁbrancy condition is exploited in the proofs of
the main theorems above. The statements of these theorems do not require this
coﬁbrancy condition since a comparison theorem (Theorem 3.26, Proposition 3.30)
shows that the operad O can always be replaced by a weakly equivalent operad O′

that satisﬁes this coﬁbrancy condition and such that the corresponding homotopy
completion towers are naturally weakly equivalent.

Coﬁbrancy Condition 1.15. If O is an operad in R-modules, consider the unit
map η : I−→O of the operad O (Deﬁnition 2.16) and assume that I[r]−→O[r] is a
ﬂat stable coﬁbration (Subsection 7.7) between ﬂat stable coﬁbrant objects in ModR
for each r ≥ 0.

Remark 1.16. This is the same as assuming that I[1]−→O[1] is a ﬂat stable coﬁ-
bration in ModR and O[r] is ﬂat stable coﬁbrant in ModR for each r ≥ 0. It can be
thought of as the structured ring spectra analog of the following coﬁbrancy condi-
tion: if X is a pointed space, assume that X is well-pointed; i.e., assume that the
unique map ∗ → X of pointed spaces is a coﬁbration.

Most operads appearing in homotopy theoretic settings in mathematics already
satisfy Coﬁbrancy Condition 1.15 and therefore require no replacement in the proofs
of the theorems. For instance, Coﬁbrancy Condition 1.15 is satisﬁed by every operad
in simplicial sets that is regarded as an operad in R-modules via adding a disjoint
basepoint and tensoring with R (Subsection 4.1).

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 7

In this paper, the homotopy groups π∗Y of a symmetric spectrum Y denote
the derived homotopy groups (or true homotopy groups) [68, 69]; i.e., π∗Y always
denotes the homotopy groups of a stable ﬁbrant replacement of Y , and hence of a
ﬂat stable ﬁbrant replacement of Y . See Schwede [69] for several useful properties
enjoyed by the true homotopy groups of a symmetric spectrum.

1.17. Organization of the paper. In Section 2 we recall some preliminaries on
algebras and modules over operads. The purpose of Section 3 is to describe homo-
topy completion (Deﬁnition 3.13) and TQ-completion, or less concisely, completion
with respect to topological Quillen homology (Deﬁnition 3.21) and to establish a
comparison theorem for homotopy completion towers (Theorem 3.26). In Section
4 we prove our main theorems, which involves a homotopical analysis of the com-
pletion tower. We establish several necessary technical results on the homotopical
properties of the forgetful functors in Section 5, and on simplicial structures and
the homotopical properties of the simplicial bar constructions in Section 6. The
results in these two sections lie at the heart of the proofs of the main theorems. The
purpose of Section 7 is to improve the main results in [31, 32] on model structures,
homotopy colimits and simplicial bar constructions from the context of operads
in symmetric spectra to the more general context of operads in R-modules. This
amounts to establishing certain technical propositions for R-modules suﬃcient for
the proofs of the main results in [31, 32] to remain valid in the more general context
of R-modules; these results play a key role in this paper. In Section 8 we observe
that the analogs of the main theorems stated above remain true in the context of
unbounded chain complexes over a commutative ring.

Acknowledgments. The authors would like to thank Greg Arone, Michael Ching,
Bill Dwyer, Emmanuel Farjoun, Rick Jardine, Nick Kuhn, Haynes Miller, and Ste-
fan Schwede for useful suggestions and remarks and Kristine Bauer, Mark Behrens,
Bjorn Dundas, Benoit Fresse, Paul Goerss, Tom Goodwillie, Jens Hornbostel,
Brenda Johnson, Tyler Lawson, Muriel Livernet, Ib Madsen, Mike Mandell, Randy
McCarthy, Jack Morava, and Charles Rezk for helpful comments. The ﬁrst author
is grateful to Jens Hornbostel and Stefan Schwede for a stimulating and enjoyable
visit to the Mathematisches Institut der Universit¨at Bonn in summer 2010, and to
Mark Behrens and Haynes Miller for a stimulating and enjoyable visit to the De-
partment of Mathematics at the Massachusetts Institute of Technology in summer
2011, and for their invitations which made this possible. The authors would like
to thank the anonymous referee for his or her detailed suggestions and comments,
which have resulted in a signiﬁcant improvement.

2. Preliminaries

The purpose of this section is to recall various preliminaries on algebras and
modules over operads. In this paper the following two contexts will be of pri-
mary interest. Denote by (ModR, ∧ , R) the closed symmetric monoidal category
of R-modules (Basic Assumption 1.2, Remark 7.5), and by (ChK, ⊗, K) the closed
symmetric monoidal category of unbounded chain complexes over K [38, 49]; here,
K is any commutative ring. Both categories have all small limits and colimits, and
the null object is denoted by ∗. It will be useful in this paper, both for establish-
ing certain results and for ease of notational purposes, to sometimes work in the
following more general context; see [50, VII] followed by [50, VII.7].

8 JOHN E. HARPER AND KATHRYN HESS

Basic Assumption 2.1. From now on in this section we assume that (C, ∧ , S)
is a closed symmetric monoidal category with all small limits and colimits. In
particular, C has an initial object ∅ and a terminal object ∗.

By closed we mean there exists a functor C
op × C−→C : (Y, Z) ↦−→ Map(Y, Z),
which we call the mapping object, which ﬁts into hom(X ∧ Y, Z) ∼= hom(X, Map(Y, Z))
isomorphisms natural in X, Y, Z, where hom denotes the set of morphisms in C. De-
ﬁne the sets n := {1, . . . , n} for each n ≥ 0, where 0 := ∅ denotes the empty set. If
T is a ﬁnite set, we denote by |T | the number of elements in T .

Deﬁnition 2.2. Let n ≥ 0.
• Σ is the category of ﬁnite sets and their bijections.
• A symmetric sequence in C is a functor A : Σop−→C. Denote by SymSeq
the category of symmetric sequences in C and their natural transformations.
• A symmetric sequence A is concentrated at n if A[r] = ∅ for all r ̸= n.

For a more detailed development of the material that follows, see [31, 33].

Deﬁnition 2.3. Consider symmetric sequences in C. Let A1, . . . , At ∈ SymSeq.
Their tensor product A1 ˇ⊗ · · · ˇ⊗At ∈ SymSeq is the left Kan extension of objectwise
smash along coproduct of sets

(Σop)
×t A1×···×At //

∐

  
 C
×t ∧ // C

Σop A1 ˇ⊗··· ˇ⊗At

left Kan extension // C

If X is a ﬁnite set and A is an object in C, we use the usual dot notation A · X
([50], [33, 2.3]) to denote the copower A·X deﬁned by A·X := ∐
X A, the coproduct
in C of |X| copies of A. Recall the following useful calculations for tensor products.

Proposition 2.4. Consider symmetric sequences in C. Let A1, . . . , At ∈ SymSeq
and R ∈ Σ, with r := |R|. There are natural isomorphisms

(A1 ˇ⊗ · · · ˇ⊗At)[R] ∼= ∐

π : R−→t
in Set
 A1[π−1(1)] ∧ · · · ∧ At[π−1(t)],

∼= ∐

r1+···+rt=r A1[r1] ∧ · · · ∧ At[rt] ·
Σr1 ×···×Σrt Σr(2.5)

Here, Set is the category of sets and their maps, and (2.5) displays the tensor
product (A1 ˇ⊗ · · · ˇ⊗At)[R] as a coproduct of Σr1 × · · · × Σrt-orbits. It will be con-
ceptually useful to extend the deﬁnition of tensor powers A ˇ⊗t to situations in which
the integers t are replaced by a ﬁnite set T .

Deﬁnition 2.6. Consider symmetric sequences in C. Let A ∈ SymSeq and R, T ∈
Σ. The tensor powers A ˇ⊗T ∈ SymSeq are deﬁned objectwise by

(A ˇ⊗∅)[R] := ∐

π : R−→∅
in Set
 S, (A ˇ⊗T )[R] := ∐

π : R−→T
in Set
 ⋀

t∈T A[π−1(t)] (T ̸= ∅).

Note that there are no functions π : R−→∅ in Set unless R = ∅. We will use the
abbreviation A ˇ⊗0 := A ˇ⊗∅.

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 9

Deﬁnition 2.7. Consider symmetric sequences in C. Let A, B, C ∈ SymSeq, and
r, t ≥ 0. The circle product (or composition product) A ◦ B ∈ SymSeq is deﬁned
objectwise by the coend

(A ◦ B)[r] := A ∧ Σ(B ˇ⊗−)[r] ∼= ∐

t≥0 A[t] ∧ Σt (B ˇ⊗t)[r].(2.8)

The mapping sequence Map
◦(B, C) ∈ SymSeq and the mapping object Map ˇ⊗(B, C) ∈
SymSeq are deﬁned objectwise by the ends

Map
◦(B, C)[t] := Map((B ˇ⊗t)[−], C)
Σ ∼= ∏

r≥0 Map((B ˇ⊗t)[r], C[r])
Σr ,

Map ˇ⊗(B, C)[t] := Map(B, C[t ∐ −])
Σ ∼= ∏

r≥0 Map(B[r], C[t + r])
Σr .

These mapping sequences and mapping objects ﬁt into isomorphisms

hom(A ◦ B, C) ∼= hom(A, Map
◦(B, C)),(2.9)
 hom(A ˇ⊗B, C) ∼= hom(A, Map ˇ⊗(B, C)),(2.10)

natural in symmetric sequences A, B, C. Here, the hom notation denotes the indi-
cated set of morphisms in SymSeq.

Proposition 2.11. Consider symmetric sequences in C.
(a) (SymSeq, ˇ⊗, 1) has the structure of a closed symmetric monoidal category
with all small limits and colimits. The unit for ˇ⊗ denoted “1” is the sym-
metric sequence concentrated at 0 with value S.
(b) (SymSeq, ◦, I) has the structure of a closed monoidal category with all small
limits and colimits. The unit for ◦ denoted “I” is the symmetric sequence
concentrated at 1 with value S. Circle product is not symmetric.

Deﬁnition 2.12. Let Z ∈ C. Deﬁne ˆZ ∈ SymSeq to be the symmetric sequence
concentrated at 0 with value Z.

The functor ˆ− : C−→SymSeq ﬁts into the adjunction ˆ− : C //SymSeq : Ev0oo
with left adjoint on top and Ev0 the evaluation functor deﬁned objectwise by
Ev0(B) := B[0]. Note that ˆ− embeds C in SymSeq as the full subcategory of
symmetric sequences concentrated at 0.

Deﬁnition 2.13. Consider symmetric sequences in C. Let O be a symmetric
sequence and Z ∈ C. The corresponding functor O : C−→C is deﬁned objectwise
by O(Z) := O ◦ (Z) := ∐t≥0O[t] ∧ Σt Z ∧t.

Proposition 2.14. Consider symmetric sequences in C. Let O, A ∈ SymSeq and
Z ∈ C. There are natural isomorphisms

̂O(Z) = ̂O ◦ (Z) ∼= O ◦ ˆZ, Ev0(O ◦ A) ∼= O ◦ (
Ev0(A)
).(2.15)

Proof. This follows from (2.8) and (2.5). □

Deﬁnition 2.16. Consider symmetric sequences in C. An operad in C is a monoid
object in (SymSeq, ◦, I) and a morphism of operads is a morphism of monoid objects
in (SymSeq, ◦, I).

Remark 2.17. If O is an operad, then the associated functor O : C → C is a monad.

10 JOHN E. HARPER AND KATHRYN HESS

Deﬁnition 2.18. Let O be an operad in C.
• A left O-module is an object in (SymSeq, ◦, I) with a left action of O and a
morphism of left O-modules is a map that respects the left O-module struc-
ture. Denote by LtO the category of left O-modules and their morphisms.
• A right O-module is an object in (SymSeq, ◦, I) with a right action of O
and a morphism of right O-modules is a map that respects the right O-
module structure. Denote by RtO the category of right O-modules and
their morphisms.
• An (O, O)-bimodule is an object in (SymSeq, ◦, I) with compatible left O-
module and right O-module structures and a morphism of (O, O)-bimodules
is a map that respects the (O, O)-bimodule structure. Denote by Bi(O,O)
the category of (O, O)-bimodules and their morphisms.
• An O-algebra is an algebra for the monad O : C−→C and a morphism of
O-algebras is a map in C that respects the O-algebra structure. Denote by
AlgO the category of O-algebras and their morphisms.

It follows easily from (2.15) that an O-algebra is the same as an object Z in C with
a left O-module structure on ˆZ, and if Z and Z ′ are O-algebras, then a morphism of
O-algebras is the same as a map f : Z−→Z ′ in C such that ˆf : ˆZ−→ ˆZ ′ is a morphism
of left O-modules. In other words, an algebra over an operad O is the same as a left
O-module that is concentrated at 0, and AlgO embeds in LtO as the full subcategory
of left O-modules concentrated at 0, via the functor ˆ− : AlgO−→LtO, Z ↦−→ ˆZ.
Deﬁne the evaluation functor Ev0 : LtO−→AlgO objectwise by Ev0(B) := B[0].

Proposition 2.19. Let O be an operad in C. There are adjunctions

C O◦(−)// AlgO,
U
oo SymSeq O◦− // LtO,
U
oo AlgO
 ˆ− // LtO,
Ev0
oo(2.20)

with left adjoints on top and U the forgetful functor. All small colimits exist in
AlgO and LtO, and both reﬂexive coequalizers and ﬁltered colimits are preserved
(and created) by the forgetful functors. All small limits exist in AlgO and LtO, and
are preserved (and created) by the forgetful functors.

Deﬁnition 2.21. Consider symmetric sequences in C. Let D be a small category,
and let X, Y ∈ SymSeqD. Denote by Map
◦(X, Y ) the indicated composition of
functors Dop×D−→SymSeq. The mapping sequence of D-shaped diagrams is deﬁned
by the end Map
◦(X, Y )
D ∈ SymSeq.

By the universal property of ends, it follows easily that for all O ∈ SymSeq, there
are isomorphisms
 homD(
O ◦ X, Y ) ∼= hom(O, Map
◦(X, Y )
D)
(2.22)

natural in O, X, Y and that Map
◦(X, Y )
D may be calculated by an equalizer in
SymSeq of the form

Map
◦(X, Y )
D ∼= lim
( ∏

α∈D Map
◦(Xα, Yα) //// ∏

(ξ : α→α′)∈D Map
◦(Xα, Yα′ ) )
.

Here, O ◦ X denotes the indicated composition of functors D−→SymSeq, the homD
notation on the left-hand side of (2.22) denotes the indicated set of morphisms
in SymSeqD, and the hom notation on the right-hand side of (2.22) denotes the
indicated set of morphisms in SymSeq.

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 11

Deﬁnition 2.23. Let D be a small category and X ∈ C
D (resp. X ∈ SymSeqD) a
D-shaped diagram. The endomorphism operad End(X) of X is deﬁned by

End(X) := Map
◦( ˆX, ˆX)
D (
resp. End(X) := Map
◦(X, X)
D)

with its natural operad structure; i.e., such that for each α ∈ D, the natural map
End(X)−→ Map
◦( ˆXα, ˆXα) (resp. End(X)−→ Map
◦(Xα, Xα)) is a morphism of
operads.

Let X be a D-shaped diagram in C (resp. SymSeq). It follows easily from (2.9)
and (2.22) that giving a map of operads m : O−→End(X) is the same as giving
Xα an O-algebra structure (resp. left O-module structure) for each α ∈ D, such
that X is a diagram of O-algebras (resp. left O-modules). Note that if D is the
terminal category (with exactly one object and no non-identity morphisms), then
End(X) ∼= Map
◦( ˆX, ˆX) (resp. End(X) ∼= Map
◦(X, X)), which recovers the usual
endomorphism operad of an object X in C (resp. SymSeq) [33, 42].

3. Homotopy completion and TQ-completion

The purpose of this section is to describe two notions of completion for structured
ring spectra: (i) homotopy completion (Deﬁnition 3.13) and (ii) TQ-completion, or
less concisely, completion with respect to topological Quillen homology (Deﬁnition
3.21). We will also establish a rigidiﬁcation theorem for derived TQ-resolutions
(Theorem 3.20), which is required to deﬁne TQ-completion, and we will prove
Theorem 3.26 which compares homotopy completion towers along a map of operads.
Let f : O−→O′ be a map of operads in R-modules. Recall that the change of
operads adjunction

AlgO
 f∗ // AlgO′
f ∗
oo (resp. LtO f∗ // LtO′
f ∗
oo )
(3.1)

is a Quillen adjunction with left adjoint on top and f ∗ the forgetful functor (more
accurately, but less concisely, also called the “restriction along f of the operad
action”) [31, 33]; note that this is a particular instance of the usual change of
monoids adjunction.

Remark 3.2. In this paper we always regard AlgO and LtO with the positive ﬂat
stable model structure (Theorem 7.15), unless otherwise speciﬁed.

Deﬁnition 3.3. Let f : O−→O′ be a map of operads in R-modules. Let X be
an O-algebra (resp. left O-module) and deﬁne the O-algebra O′ ◦h
O (X) (resp. left
O-module O′ ◦h
O X) by

O′ ◦h
O (X) := Rf ∗(Lf∗(X)) = Rf ∗(
O′ ◦L
O (X)
)

(
resp. O′ ◦h
O X := Rf ∗(Lf∗(X)) = Rf ∗(O′ ◦L
O X)
)
.

Here, Rf ∗, Lf∗ are the total right (resp. left) derived functors of f ∗, f∗, respectively.

Remark 3.4. Note that AlgI = ModR and LtI = SymSeq (since I is the initial
operad) and that for any map of operads f : O−→O′, there are weak equivalences

O′ ◦h
O (X) ≃ Lf∗(X) = O′ ◦L
O (X) (
resp. O′ ◦h
O X ≃ Lf∗(X) = O′ ◦L
O X)

12 JOHN E. HARPER AND KATHRYN HESS

in the underlying category AlgI (resp. SymSeq), natural in X; this follows from
the property that the forgetful functor to the underlying category preserves weak
equivalences.

The truncation functor τk : SymSeq−→SymSeq is deﬁned objectwise by

(τkX)[r] := { X[r], for r ≤ k,
∗, otherwise,

for each k ≥ 1. In other words, τkX is the symmetric sequence obtained by trun-
cating X above level k. Let O be an operad in R-modules such that O[0] = ∗. It
is easy to verify that the canonical map of operads O−→τ1O factors through each
truncation τkO, and hence gives rise to a commutative diagram of operads

{τkO} : τ1O τ2Ooo τ3Ooo · · ·oo

{O} :

OO
 O

OO EE ::

···

(3.5)

and (O, O)-bimodules. In other words, associated to each such operad O is a coaug-
mented tower {O}−→{τkO} of operads and (O, O)-bimodules, where {O} denotes
the constant tower with value O. This tower underlies the following deﬁnition of
completion for O-algebras and left O-modules, which plays a key role in this paper.

Remark 3.6. Let O be an operad in R-modules such that O[0] = ∗.

(i) The canonical maps τ1O−→O−→τ1O of operads factor the identity map.
(ii) Note that O[0] = ∗ and O[1] = I[1] if and only if τ1O = I, i.e., if and only
if the operad O agrees with the initial operad I at levels 0 and 1.

Deﬁnition 3.7. Let O be an operad in R-modules such that O[0] = ∗. Let X be
an O-algebra (resp. left O-module). The completion tower of X is the coaugmented
tower of O-algebras (resp. left O-modules)

{X}−→{τkO ◦O (X)} (
resp. {X}−→{τkO ◦O X})
(3.8)

obtained by applying − ◦O (X) (resp. − ◦O X) to the coaugmented tower (3.5).
The completion X ∧ of X is the O-algebra (resp. left O-module) deﬁned by

X ∧ := limAlgO
k (
τkO ◦O (X)
) (resp. X ∧ := lim
LtO
k (
τkO ◦O X))
,(3.9)

i.e., the limit of the completion tower of X. Here, {X} denotes the constant tower
with value X. Thus, completion deﬁnes a coaugmented functor on AlgO (resp.
LtO).

Remark 3.10. We often suppress the forgetful functors AlgτkO−→AlgO and LtτkO−→LtO
from the notation, as in (3.8).

3.11. Homotopy completion and topological Quillen homology. The pur-
pose of this subsection is to introduce homotopy completion (Deﬁnition 3.13) and
topological Quillen homology (Deﬁnition 3.15).
In this paper we will primarily be interested in a homotopy invariant version of
the completion functor, which involves the following homotopy invariant version of
the limit functor on towers.

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 13

Deﬁnition 3.12. Let M be a model category with all small limits and let D be
the category {0 ← 1 ← 2 ← · · · } with objects the non-negative integers and a
single morphism i ← j for each i ≤ j. Consider the category MD of D-shaped
diagrams (or towers) in M with the injective model structure [27, VI.1.1]. The
homotopy limit functor holim : Ho(MD)−→Ho(M) is the total right derived functor
of the limit functor lim : MD−→M.

We are now in a good position to deﬁne homotopy completion.

Deﬁnition 3.13. Let O be an operad in R-modules such that O[0] = ∗. Let X
be an O-algebra (resp. left O-module). The homotopy completion X h∧ of X is the
O-algebra (resp. left O-module) deﬁned by

X h∧ := holim
AlgO
k (
τkO ◦O (X c)
) (
resp. X h∧ := holim
LtO
k (
τkO ◦O X c))
,

the homotopy limit of the completion tower of the functorial coﬁbrant replacement
X c of X in AlgO (resp. LtO).

Remark 3.14. It is easy to check that if X is a coﬁbrant O-algebra (resp. coﬁ-
brant left O-module), then the weak equivalence X c−→X induces zigzags of weak
equivalences
 X h∧ ≃ holim
AlgO
k (
τkO ◦O (X)
) ≃ holim
AlgO
k (
τkO ◦h
O (X)
)

(
resp. X h∧ ≃ holim
LtO
k (
τkO ◦O X) ≃ holim
LtO
k (
τkO ◦h
O X))

in AlgO (resp. LtO), natural in X. Hence the homotopy completion X h∧ of a
coﬁbrant O-algebra (resp. coﬁbrant left O-module) X may be calculated by taking
the homotopy limit of the completion tower of X.

In this paper we consider topological Quillen homology of an O-algebra (resp.
left O-module) as an object in AlgO (resp. LtO) via the forgetful functor as follows.

Deﬁnition 3.15. If O is an operad in R-modules such that O[0] = ∗, and X is an
O-algebra (resp. left O-module), then the topological Quillen homology TQ(X) of
X is the O-algebra (resp. left O-module) τ1O ◦h
O (X) (resp. τ1O ◦h
O X).

In particular, when applied to a coﬁbrant O-algebra (resp. coﬁbrant left O-
module) X, the completion tower interpolates between topological Quillen homol-
ogy TQ(X) and homotopy completion X h∧.

3.16. TQ-completion. The purpose of this subsection is to introduce a second
naturally occurring notion of completion for structured ring spectra, called TQ-
completion, or less concisely, completion with respect to topological Quillen ho-
mology (Deﬁnition 3.21). Deﬁning TQ-completion requires the construction of a
rigidiﬁcation of the derived TQ-resolution (3.18) from a diagram in the homotopy
category to a diagram in the model category. This rigidiﬁcation problem is solved
in Theorem 3.20.
The TQ-completion construction is conceptual and can be thought of as a spec-
tral algebra analog of Sullivan’s [72, 73] localization and completion of spaces,
Bousﬁeld-Kan’s [9, I.4] completion of spaces with respect to homology, and Carls-
son’s [10, II.4] and Arone-Kankaanrinta’s [3, 0.1] completion and localization of
spaces with respect to stable homotopy.

14 JOHN E. HARPER AND KATHRYN HESS

Here is the idea behind the construction. We want to deﬁne TQ-completion X ∧
TQ
of a structured ring spectrum X to be the structured ring spectrum deﬁned by
(showing only the coface maps) the homotopy limit of

X ∧
TQ := holim∆( TQ(X) //// (TQ)
2(X) ////// (TQ)
3(X) · · · )

the cosimplicial resolution (or Godement resolution) with respect to the monad (or
triple) TQ. However, there are technical details that one needs to resolve in order
to make sense of this deﬁnition for TQ-completion. This is because TQ naturally
arises as a functor on the level of the homotopy categories, and to work with and
make sense of the homotopy limit holim∆ we need a point-set level construction of
the derived TQ-cosimplicial resolution (3.18), or more precisely, a construction on
the level of model categories. Successfully resolving this issue is the purpose of the
rest of this subsection, and amounts to solving a rigidiﬁcation problem (Theorem
3.20) for the derived cosimplicial resolution with respect to TQ.
Let O be an operad in R-modules such that O[0] = ∗. Then the canonical map
of operads f : O−→τ1O induces a Quillen adjunction as in (3.1) and hence induces
a corresponding adjunction

Ho(AlgO) Lf∗ // Ho(Algτ1O)
Rf ∗
oo (resp. Ho(LtO) Lf∗ // Ho(Ltτ1O)
Rf ∗
oo )
(3.17)

on the homotopy categories. Hence topological Quillen homology TQ is the monad
(or triple) on the homotopy category Ho(AlgO) (resp. Ho(LtO)) associated to the
derived adjunction (3.17). Denote by K the corresponding comonad (or cotriple)

id−→TQ (unit), id←−K (counit),

TQTQ−→TQ (multiplication), KK←−K (comultiplication),

on Ho(Algτ1O) (resp. Ho(Ltτ1O)). Then TQ = Rf ∗Lf∗ and K = Lf∗Rf ∗, and it
follows that for any O-algebra (resp. left O-module) X, the adjunction (3.17) deter-
mines a cosimplicial resolution of X with respect to topological Quillen homology
TQ of the form
 X // TQ(X) //// TQ
2(X) //////oo TQ
3(X) · · ·
oooo

(3.18)

This derived TQ-resolution can be thought of as encoding what it means for TQ(X)
to have the structure of a K-coalgebra. More precisely, the extra structure on
TQ(X) is the K-coalgebra structure on the underlying object Lf∗(X) of TQ(X).
One diﬃculty in working with the diagram (3.18) is that it lives in the homotopy
category Ho(AlgO) (resp. Ho(LtO)). The purpose of the rigidiﬁcation theorem
below is to construct a model of (3.18) that lives in AlgO (resp. LtO).
Consider any factorization of the canonical map f : O−→τ1O in the category of
operads as O g
−→ J1 h
−→ τ1O, a coﬁbration followed by a weak equivalence (Deﬁnition
5.47) with respect to the positive ﬂat stable model structure on ModR (Deﬁnition
7.10); it is easy to verify that such factorizations exist using a small object argument
(Proposition 5.48). The corresponding change of operads adjunctions have the form

AlgO
 g∗ // AlgJ1
g∗
oo h∗ // Algτ1O
h∗
oo (resp. LtO g∗ // LtJ1
g∗
oo h∗ // Ltτ1O
h∗
oo )
(3.19)
 HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 15

with left adjoints on top and g∗, h∗ the forgetful functors (more accurately, but less
concisely, also called the “restriction along g, h, respectively, of the operad action”).
These are Quillen adjunctions and since h is a weak equivalence it follows that the
(h∗, h∗) adjunction is a Quillen equivalence (Theorem 7.21). We defer the proof of
the following rigidiﬁcation theorem to Section 5 (just after Theorem 5.49).

Theorem 3.20 (Rigidiﬁcation theorem for derived TQ-resolutions). Let O be an
operad in R-modules such that O[0] = ∗. Assume that O[r] is ﬂat stable coﬁbrant in
ModR for each r ≥ 0. If X is a coﬁbrant O–algebra (resp. coﬁbrant left O-module)
and n ≥ 1, then there are weak equivalences (g∗g∗)
n(X) ≃ TQ
n(X) natural in such
X.

The following description of TQ-completion is closely related to [11] and [34].

Deﬁnition 3.21. Let O be an operad in R-modules such that O[0] = ∗. Assume
that O[r] is ﬂat stable coﬁbrant in ModR for each r ≥ 0. Let X be an O-algebra
(resp. left O-module). The TQ-completion (or completion with respect to topolog-
ical Quillen homology) X ∧
TQ of X is the O–algebra (resp. left O-module) deﬁned by
(showing only the coface maps) the homotopy limit of the cosimplicial resolution

X ∧
TQ := holim∆( (g∗g∗)(X c) //// (g∗g∗)
2(X c) ////// (g∗g∗)
3(X c) · · · )
(3.22)

(or Godement resolution) of the functorial coﬁbrant replacement X c of X in AlgO
(resp. LtO) with respect to the monad g∗g∗. Here, holim∆ is calculated in the
category of O–algebras (resp. left O-modules).

Remark 3.23. The (g∗g∗)-resolution can be thought of as encoding what it means for
TQ(X) to have the structure of a K-coalgebra. More precisely, the extra structure
on g∗g∗(X c) ≃ TQ(X) is the (g∗g∗)-coalgebra structure on the underlying object
g∗(X c) of g∗g∗(X c). In particular, the comonad (g∗g∗) provides a point-set model
for the derived comonad K that coacts on TQ(X) (up to a Quillen equivalence).
This point-set model of K is conjecturally related to the Koszul dual cooperad
associated to O (see, for instance, [13, 21, 23]).

It follows that the cosimplicial resolution in (3.22) provides a rigidiﬁcation of the
derived cosimplicial resolution (3.18). One of our motivations for introducing the
homotopy completion tower was its role as a potentially useful tool in analyzing
TQ-completion deﬁned above, but an investigation of these properties and the TQ-
completion functor will be the subject of other papers and will not be elaborated
here.

3.24. Comparing homotopy completion towers. The purpose of this subsec-
tion is to prove Theorem 3.26, which compares homotopy completion towers along
a map of operads.
Let g : O′−→O be a map of operads in R-modules, and for each O-algebra (resp.
left O-module) X, consider the corresponding O′-algebra (resp. left O′-module) X
given by forgetting the left O-action along the map g; here we have dropped the
forgetful functor g∗ from the notation. Consider the map ∅−→X in AlgO′ (resp.
LtO′) and use functorial factorization in AlgO′ (resp. LtO′) to obtain

∅−→X ′−→X,(3.25)

a coﬁbration followed by an acyclic ﬁbration.

16 JOHN E. HARPER AND KATHRYN HESS

In the next theorem we establish that replacing an operad O by a weakly equiv-
alent operad O′ changes the homotopy completion tower of X only up to natural
weak equivalence. In particular, the homotopy completion of X as an O′-algebra is
weakly equivalent to its homotopy completion as an O-algebra.

Theorem 3.26 (Comparison theorem for homotopy completion towers). Let g : O′−→O
be a map of operads in R-modules such that O′[0] = ∗ and O[0] = ∗. If X is an
O-algebra (resp. left O-module), then there are maps of towers

{X ′}

  
 {X ′}

(♯)
  
 // {X}

  
{τkO′ ◦O′ (X ′)} (∗) // {τkO ◦O′ (X ′)} (∗∗) // {τkO ◦O (X)}

(3.27)
 resp. {X ′}

  
 {X ′}

(♯)
  
 // {X}

  
{τkO′ ◦O′ X ′} (∗) // {τkO ◦O′ X ′} (∗∗) // {τkO ◦O X}

(3.28)

of O′-algebras (resp. left O′-modules), natural in X. If, furthermore, g is a weak
equivalence in the underlying category SymSeq, and X is ﬁbrant and coﬁbrant in
AlgO (resp. LtO), then the maps (∗) and (∗∗) are levelwise weak equivalences; here,
we are using the notation (3.25) to denote functorial coﬁbrant replacement of X as
an O′-algebra (resp. left O′-module).

Proof. It suﬃces to consider the case of left O-modules. The map of operads O′−→O
induces a commutative diagram of towers

{O′}

  
 // {O}

  
{τkO′} // {τkO}

(3.29)

of operads and (O′, O′)-bimodules; here, {O′} and {O} denote the constant towers
with values O′ and O, respectively.
Consider the map of towers (∗). Each map τkO′ ◦O′ X ′−→τkO ◦O′ X ′ in (∗) is
obtained by applying − ◦O′ X ′ to the map τkO′−→τkO. By (3.29), this map is
isomorphic to the composite τkO′ ◦O′ X ′ η
−→ τkO ◦τkO′ τkO′ ◦O′ ◦X ′ ∼= τkO ◦O′ X ′

where η : id−→τkO ◦τkO′ − is the unit map associated to the change of operads
adjunction LtτkO′ //LtτkOoo . If, furthermore, g is a weak equivalence in SymSeq,
then the map τkO′−→τkO is a weak equivalence, and since X ′ is coﬁbrant in LtO′
it follows from 7.21 and 7.23 that (∗) is a levelwise weak equivalence.
Consider the map of towers (∗∗) and the change of operads adjunction LtO′ // LtOoo .
The weak equivalence X ′−→X of left O′-modules in (3.25) has corresponding ad-
joint map ξ : O ◦O′ X ′−→X. Each map τkO ◦O′ X ′−→τkO ◦O X in (∗∗) is obtained
by applying τkO ◦O − to the map ξ. If, furthermore, g is a weak equivalence in
SymSeq, and X is ﬁbrant and coﬁbrant in LtO, then by 7.21 the map ξ is a weak
equivalence between coﬁbrant objects in LtO, and hence (∗∗) is a levelwise weak
equivalence. To ﬁnish the proof, it suﬃces to describe the map of towers (♯) in

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 17

(3.28). Each map X ′−→τkO ◦O′ X ′ is obtained by applying − ◦O′ X ′ to the map
O′−→τkO. □

We defer the proof of the following proposition to Section 5.

Proposition 3.30. Let O be an operad in R-modules such that O[0] = ∗. Then
there exists a map of operads g : O′−→O such that O′[0] = ∗, and
(i) g is a weak equivalence in the underlying category SymSeq,
(ii) O′ satisﬁes Coﬁbrancy Condition 1.15.

Later in this paper, we need the following observation that certain homotopy
limits commute with the forgetful functor.

Proposition 3.31. Let O be an operad in R-modules. Consider any tower B0 ←
B1 ← B2 ← · · · of O-algebras (resp. left O-modules). There are natural zigzags

U holim
AlgO
k Bk ≃ holimk U Bk (resp. U holim
LtO
k Bk ≃ holimk U Bk)

of weak equivalences. Here, U is the forgetful functor (2.20).

Proof. This follows from the dual of [32, proof of 3.15], together with the observation
that the forgetful functor U preserves weak equivalences and that ﬁbrant towers
are levelwise ﬁbrant. □

4. Homotopical analysis of the completion tower

The purpose of this section is to prove the main theorems stated in the intro-
duction (Theorems 1.5, 1.8, 1.9, and 1.12). The unifying approach behind each of
these theorems is to systematically exploit induction “up the homotopy comple-
tion tower” together with explicit calculations of the layers in terms of simplicial
bar constructions (Theorem 4.21 and Proposition 4.36). An important property of
these layer calculations, which we fully exploit in the proofs of the main theorems,
is that the simplicial bar constructions are particularly amenable to systematic
connectivity and ﬁniteness estimates (Propositions 4.30, 4.32, and 4.43–4.47).
The ﬁrst step to proving the main theorems is to establish conditions under
which the homotopy completion tower of X converges strongly to X. This is ac-
complished in Theorem 1.12, which necessarily is the ﬁrst of the main theorems to
be proved. Establishing strong convergence amounts to verifying that the connec-
tivity of the natural maps from X into each stage of the tower increase as you go up
the tower, and verifying this essentially reduces to understanding the implications
of the connectivity estimates in Propositions 4.30 and 4.32 when studied in the
context of the calculations in Propositions 4.13 and 4.28 (see Proposition 4.33).
The upshot of strong convergence is that to calculate πiX for a ﬁxed i, one only
needs to calculate πi of a (suﬃciently high but) ﬁnite stage of the tower. Having to
only go “ﬁnitely high up the tower” to calculate πiX, together with the explicit layer
calculations in Theorem 4.21 and Proposition 4.36, are the key technical properties
underlying our approach to the main theorems. For instance, our approach to the
TQ ﬁniteness theorem (Theorem 1.5) is to (i) start with an assumption about the
ﬁniteness properties of πi of TQ-homology (which is the bottom stage of the tower),
(ii) to use explicit calculations of the layers of the tower to prove that these same
ﬁniteness properties are inherited by πi of the layers, and (iii) to conclude that
these ﬁniteness properties are inherited by πi of each stage of the tower. Strong

18 JOHN E. HARPER AND KATHRYN HESS

convergence of the homotopy completion tower then ﬁnishes the proof of the TQ
ﬁniteness theorem. It is essentially in this manner that we systematically exploit
induction “up the homotopy completion tower” to prove each of the main theorems
stated in the introduction.

4.1. Simplicial bar constructions and the homotopy completion tower.
Recall that R is any commutative ring spectrum (Basic Assumption 1.2) and that
(ModR, ∧ , R) denotes the closed symmetric monoidal category of R-modules (Def-
inition 7.4). Denote by S (resp. S∗) the category of simplicial sets (resp. pointed

simplicial sets). There are adjunctions S (−)+ //S∗
U
oo R⊗G0 //ModR,oo with left adjoints on

top and U the forgetful functor (see Proposition 7.2 for the tensor product ⊗ nota-
tion together with (7.8)). The functor R⊗G0 is left adjoint to “evaluation at 0”; the
notation agrees with Subsection 7.7 and [39, after 2.2.5]. Note that if X ∈ ModR
and K ∈ S∗, then there are natural isomorphisms X ∧ K ∼= X ∧ (R⊗G0K) in ModR;
in other words, taking the objectwise smash product of X with K (as pointed
simplicial sets) is the same as taking the smash product of X with R⊗G0K (as
R-modules).
Recall the usual realization functor on simplicial R-modules and simplicial sym-
metric sequences; see also [27, IV.1, VII.1].

Deﬁnition 4.2. Consider symmetric sequences in ModR. The realization func-
tors | − | for simplicial R-modules and simplicial symmetric sequences are deﬁned
objectwise by the coends

| − | : sModR−→ModR, X ↦−→ |X| := X ∧ ∆∆[−]+ ,

| − | : sSymSeq−→SymSeq, X ↦−→ |X| := X ∧ ∆∆[−]+ .

Proposition 4.3. The realization functors ﬁt into adjunctions

sModR
 |−| // ModR,oo sSymSeq |−| // SymSeq,oo(4.4)

with left adjoints on top.

Proof. Consider the case of R-modules (resp. symmetric sequences). Using the
universal property of coends, it is easy to verify that the functor given objectwise
by Map(R⊗G0∆[−]+, Y ) is a right adjoint of | − |. □

The following is closely related to [27, IV.1.7] and [18, X.2.4]; see also [14, A]
and [36, Chapter 18].

Proposition 4.5. Let f : X−→Y be a morphism of simplicial R-modules. If f
is a monomorphism (resp. objectwise weak equivalence), then |f | : |X|−→|Y | is a
monomorphism (resp. weak equivalence).

Proof. This is veriﬁed exactly as in [32, proof of 4.8, 4.9], except using (ModR, ∧ , R)
instead of (SpΣ, ⊗S, S). □

The following is closely related to [18, X.1.3].

Proposition 4.6. Consider symmetric sequences in R-modules.
(a) If X, Y are simplicial R-modules, then there is a natural isomorphism
|X ∧ Y | ∼= |X| ∧ |Y |.

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 19

(b) If X, Y are simplicial symmetric sequences, then there are natural isomor-
phisms |X ˇ⊗Y | ∼= |X| ˇ⊗|Y | and |X ◦ Y | ∼= |X| ◦ |Y |.
(c) If O is a symmetric sequence, and B is a simplicial symmetric sequence,
then there is a natural isomorphism |O[k] ∧ Σk B ˇ⊗k| ∼= O[k] ∧ Σk |B| ˇ⊗k for
every k ≥ 2.
Here, smash products, tensor products and circle products of simplicial objects are
deﬁned objectwise.

Remark 4.7. If X ∈ sS∗, denote by |X| := X ∧ ∆∆[−]+ the realization of X. There
is a natural isomorphism X ×∆ ∆[−] ∼= |X|.

Proof of Proposition 4.6. Consider part (a). Let X, Y be simplicial objects in S∗.
By Remark 4.7, together with [27, IV.1.4], there is a natural isomorphism |X ×
Y | ∼= |X| × |Y |. Since realization | − | : sS∗−→S∗ is a left adjoint it commutes with
colimits, and thus there is a natural isomorphism |X ∧ Y | ∼= |X| ∧ |Y |. Let X, Y
be simplicial R-modules and recall that X ∧ Y ∼= X⊗RY . It follows that there are
natural isomorphisms |X ∧ Y | ∼= colim
( |X|⊗|Y | |X|⊗|R|⊗|Y |oooo ) ∼= |X| ∧ |Y |.

Parts (b) and (c) follow from part (a), together with the property that realization
| − | is a left adjoint and hence commutes with colimits. □

Remark 4.8. Let O be an operad in R-modules. It follows easily from Proposition
4.6 that if X is a simplicial O-algebra (resp. simplicial left O-module), then the
realization of its underlying simplicial object |X| has an induced O-algebra (resp.
left O-module) structure; it follows that realization of the underlying simplicial
objects induces functors | − | : sAlgO−→AlgO and | − | : sLtO−→LtO.

Remark 4.9. In this paper we use the notation Bar, as in Proposition 4.10 below,
to denote the simplicial bar construction (with respect to circle product) deﬁned in
[32, 5.30].

Proposition 4.10. Let O−→O′ be a morphism of operads in R-modules. Let X be a
coﬁbrant O-algebra (resp. coﬁbrant left O-module). If the simplicial bar construction
Bar(O, O, X) is objectwise coﬁbrant in AlgO (resp. LtO), then the natural map

| Bar(O′, O, X)| ≃
−−→ O′ ◦O (X) (resp. | Bar(O′, O, X)| ≃
−−→ O′ ◦O X)

is a weak equivalence.

Proof. This follows easily from Theorem 7.25 and its proof. □

The following theorem illustrates some of the good properties of the (positive)
ﬂat stable model structures (Section 7). We defer the proof to Section 5.

Theorem 4.11. Let O be an operad in R-modules such that O[r] is ﬂat stable
coﬁbrant in ModR for each r ≥ 0.
(a) If j : A−→B is a coﬁbration between coﬁbrant objects in AlgO (resp. LtO),
then j is a positive ﬂat stable coﬁbration in ModR (resp. SymSeq).
(b) If A is a coﬁbrant O-algebra (resp. coﬁbrant left O-module) and O[0] = ∗,
then A is positive ﬂat stable coﬁbrant in ModR (resp. SymSeq).

If X is an O-algebra (resp. left O-module), then under appropriate coﬁbrancy
conditions the coaugmented tower {| Bar(O, O, X)|}−→{| Bar(τkO, O, X)|} obtained
by applying | Bar(−, O, X)| to the coaugmented tower (3.5), provides a weakly
equivalent “fattened version” of the completion tower of X.

20 JOHN E. HARPER AND KATHRYN HESS

Coﬁbrancy Condition 4.12. If O is an operad in R-modules, assume that O[r]
is ﬂat stable coﬁbrant in ModR for each r ≥ 0.

Proposition 4.13. Let O be an operad in R-modules such that O[0] = ∗. Assume
that O satisﬁes Coﬁbrancy Condition 4.12. If X is a coﬁbrant left O-module, then
in the following commutative diagram of towers in LtO

{| Bar(O, O, X)|}

≃
  
 // {| Bar(τkO, O, X)|}

≃
  
{X} // {τkO ◦O X},

the vertical maps are levelwise weak equivalences.

Remark 4.14. It follows from Remark 4.8 that this diagram is a diagram of towers
of left O-modules.

Proof. Since X is a coﬁbrant left O-module, by Theorem 4.11 the simplicial bar con-
struction Bar(O, O, X) is objectwise coﬁbrant in LtO, and Proposition 4.10 ﬁnishes
the proof. □

4.15. Homotopy ﬁber sequences and the homotopy completion tower.
The purpose of this subsection is to prove Theorem 1.12(c). We begin by introduc-
ing the following useful notation. For each k ≥ 0, the functor ik : SymSeq−→SymSeq
is deﬁned objectwise by
 (ikX)[r] := { X[k], for r = k,
∗, otherwise.

In other words, ikX is the symmetric sequence concentrated at k with value X[k].

Proposition 4.16. Let O be an operad in R-modules such that O[0] = ∗. Let X be
an O-algebra (resp. left O-module) and k ≥ 2. Then the left-hand pushout diagram

ikO ⊂ //

  
 τkO

  
∗ // τk−1O
 | Bar(ikO, O, X)|

  
 (∗) // | Bar(τkO, O, X)|

  
∗ // | Bar(τk−1O, O, X)|

(4.17)

in RtO induces the right-hand pushout diagram in AlgI (resp. SymSeq). The map
(∗) is a monomorphism, the left-hand diagram is a pullback diagram in Bi(O,O), and
the right-hand diagram is a pullback diagram in AlgO (resp. LtO).

Proof. It suﬃces to consider the case of left O-modules. The right-hand diagram is
obtained by applying | Bar(−, O, X)| to the left-hand diagram. Since the forgetful
functor RtO−→SymSeq preserves colimits, the left-hand diagram is also a pushout
diagram in SymSeq. It follows from the adjunction (2.9) that applying Bar(−, O, X)
to the left-hand diagram gives a pushout diagram of simplicial symmetric sequences.
Noting that the realization functor | − | is a left adjoint and preserves monomor-
phisms (4.3, 4.5), together with the fact that pullbacks in Bi(O,O) and LtO are
calculated in the underlying category, ﬁnishes the proof. □

Proposition 4.18. Let O be an operad in R-modules such that O[0] = ∗, and let
k ≥ 2.
 HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 21

(a) The canonical maps ikO−→O−→ikO in Rtτ1O factor the identity map.
(b) The functors ikO ◦τ1O (−) : Algτ1O−→AlgO and ikO ◦τ1O − : Ltτ1O−→LtO
preserve weak equivalences between coﬁbrant objects, and hence the total
left derived functors ikO ◦h
τ1O (−) and ikO ◦h
τ1O − exist [17, 9.3, 9.5].

Proof. Part (a) is clear. To prove part (b), it suﬃces to consider the case of left τ1O-
modules. Let B−→B′ be a weak equivalence between coﬁbrant objects in Ltτ1O.
By part (a) there is a retract of maps of the form

ikO ◦τ1O B

(∗)
  
 // O ◦τ1O B

(∗∗)
  
 // ikO ◦τ1O B

(∗)
  
ikO ◦τ1O B′ // O ◦τ1O B′ // ikO ◦τ1O B′

in SymSeq. Since O ◦τ1O − : Ltτ1O−→LtO is a left Quillen functor (induced by the
canonical map τ1O−→O of operads), we know that (∗∗) is a weak equivalence and
hence (∗) is a weak equivalence. □

The following theorem illustrates a few more of the good properties of the (pos-
itive) ﬂat stable model structures (Section 7). We defer the proof to Section 6.

Theorem 4.19. Let f : O−→O′ be a morphism of operads in R-modules such that
O[0] = ∗. Assume that O satisﬁes Coﬁbrancy Condition 1.15. Let Y be an O-algebra
(resp. left O-module) and consider the simplicial bar construction Bar(O′, O, Y ).
(a) If Y is positive ﬂat stable coﬁbrant in ModR (resp. SymSeq), then Bar(O′, O, Y )
is Reedy coﬁbrant in sAlgO′ (resp. sLtO′ ).
(b) If Y is positive ﬂat stable coﬁbrant in ModR (resp. SymSeq), then | Bar(O′, O, Y )|
is coﬁbrant in AlgO′ (resp. LtO′).

Proposition 4.20. Let O be an operad in R-modules such that O[0] = ∗. Assume
that O satisﬁes Coﬁbrancy Condition 1.15. If X is a coﬁbrant O-algebra (resp.
coﬁbrant left O-module), then | Bar(τ1O, O, X)| is coﬁbrant in Algτ1O (resp. Ltτ1O).

Proof. This follows from Theorems 4.19 and 4.11. □

Next we explicitly calculate the k-th layer of the homotopy completion tower.

Theorem 4.21. Let O be an operad in R-modules such that O[0] = ∗. Assume that
O satisﬁes Coﬁbrancy Condition 1.15. Let X be an O-algebra (resp. left O-module),
and let k ≥ 2.
(a) There is a homotopy ﬁber sequence of the form

ikO ◦h
τ1O (
TQ(X)
)
−→τkO ◦h
O (X)−→τk−1O ◦h
O (X)
(resp. ikO ◦h
τ1O TQ(X)−→τkO ◦h
O X−→τk−1O ◦h
O X)

in AlgO (resp. LtO), natural in X.
(b) If X is coﬁbrant in AlgO (resp. LtO), then there are natural weak equiva-
lences

| Bar(ikO, O, X)| ≃ ikO ◦τ1O (| Bar(τ1O, O, X)|) ≃ ikO ◦h
τ1O (
TQ(X)
)

(resp. | Bar(ikO, O, X)| ≃ ikO ◦τ1O | Bar(τ1O, O, X)| ≃ ikO ◦h
τ1O TQ(X)
).

22 JOHN E. HARPER AND KATHRYN HESS

(c) If X is coﬁbrant in AlgO (resp. LtO) and O[1] = I[1], then there are natural
weak equivalences

O[k] ∧ Σk | Bar(I, O, X)|∧k ≃ ikO ◦h
τ1O (
TQ(X)
)

(
resp. O[k] ∧ Σk | Bar(I, O, X)| ˇ⊗k ≃ ikO ◦h
τ1O TQ(X)
)
.

For useful material related to homotopy ﬁber sequences, see [27, II.8, II.8.20].

Proof. It suﬃces to consider the case of left O-modules. Consider part (a). It
is enough to treat the special case where X is a coﬁbrant left O-module. By
Proposition 4.16 there is a homotopy ﬁber sequence of the form

| Bar(ikO, O, X)|−→| Bar(τkO, O, X)|−→| Bar(τk−1O, O, X)|(4.22)

in LtO, natural in X. By Proposition 4.13 we know that (4.22) has the form

| Bar(ikO, O, X)|−→τkO ◦h
O X−→τk−1O ◦h
O X.

Since the right O-action map ikO ◦ O−→ikO factors as ikO ◦ O−→ikO ◦ τ1O−→ikO,
there are natural isomorphisms

Bar(ikO, O, X) ∼= ikO ◦τ1O Bar(τ1O, O, X)(4.23)

of simplicial left O-modules. Applying the realization functor to (4.23), it follows
from Proposition 4.6, Proposition 4.20, Theorem 4.11, and Proposition 4.13, that
there are natural weak equivalences

| Bar(ikO, O, X)| ≃ ikO ◦τ1O | Bar(τ1O, O, X)| ≃ ikO ◦h
τ1O TQ(X)(4.24)

which ﬁnishes the proof of part (a). Part (b) follows from the proof of part (a)
above.
Consider part (c). Proceed as in the proof of part (a) above, and assume fur-
thermore that O[1] = I[1]. It follows from (2.8) that

ikO ◦ | Bar(I, O, X)| ≃ O[k] ∧ Σk | Bar(I, O, X)| ˇ⊗k

from which we can conclude, by applying the second equivalence in (4.24), since
τ1O = I (Deﬁnition 2.16). □

Proposition 4.25. Let O be an operad in R-modules such that O[0] = ∗. As-
sume that O satisﬁes Coﬁbrancy Condition 1.15. Let f : X−→Y be a map between
coﬁbrant objects in AlgO (resp. LtO). If the induced map | Bar(τ1O, O, X)| ≃
−−→
| Bar(τ1O, O, Y )| is a weak equivalence, then the induced map | Bar(τkO, O, X)| ≃
−−→
| Bar(τkO, O, Y )| is a weak equivalence for each k ≥ 2.

Proof. It suﬃces to consider the case of left O-modules. Consider the

| Bar(ikO, O, X)|

  
 // | Bar(τkO, O, X)|

  
 // | Bar(τk−1O, O, X)|

  
| Bar(ikO, O, Y )| // | Bar(τkO, O, Y )| // | Bar(τk−1O, O, Y )|

(4.26)

commutative diagram in SymSeq. It follows from Theorem 4.21 that the left-hand
vertical map is a weak equivalence for each k ≥ 2. If k = 2, then the right-hand
vertical map is a weak equivalence by assumption, hence by Proposition 4.16 and
induction on k, the middle vertical map is a weak equivalence for each k ≥ 2. □

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 23

Proof of Theorem 1.12(c). It suﬃces to consider the case of left O-modules. By
Theorem 3.26 and Propositions 3.30 and 3.31, we can suppose that O satisﬁes
Coﬁbrancy Condition 1.15. We can restrict to the following special case. Let
f : X−→Y be a map of left O-modules between coﬁbrant objects in LtO such that
the induced map τ1O◦OX−→τ1O◦OY is a weak equivalence. We need to verify that
the induced map f∗ : τkO ◦O X−→τkO ◦O Y is a weak equivalence for each k ≥ 2.
We know by Theorem 4.11 that X, Y are positive ﬂat stable coﬁbrant in SymSeq. If
k = 1, the map f∗ is a weak equivalence by assumption, and hence the induced map
| Bar(τ1O, O, X)|−→| Bar(τ1O, O, Y )| is a weak equivalence by Proposition 4.13. It
follows from Propositions 4.25 and 4.13 that f∗ is a weak equivalence for each k ≥ 2,
which ﬁnishes the proof. □

4.27. Strong convergence of the homotopy completion tower. The pur-
pose of this subsection is to prove Theorem 1.12(a). For each k ≥ 0, the functor
(−)
>k : SymSeq−→SymSeq is deﬁned objectwise by

(X >k)[r] := { X[r], for r > k,
∗, otherwise.

Proposition 4.28. Let O be an operad in R-modules such that O[0] = ∗. Let X be
an O-algebra (resp. left O-module) and k ≥ 1. Then the left-hand pushout diagram

O>k

  
 ⊂ // O

  
∗ // τkO
 | Bar(O>k, O, X)|

  
 (∗) // | Bar(O, O, X)|

  
∗ // | Bar(τkO, O, X)|

(4.29)

in RtO induces the right-hand pushout diagram in AlgI (resp. SymSeq). The map
(∗) is a monomorphism, the left-hand diagram is a pullback diagram in Bi(O,O), and
the right-hand diagram is a pullback diagram in AlgO (resp. LtO).

Proof. It suﬃces to consider the case of left O-modules. The right-hand diagram
is obtained by applying | Bar(−, O, X)| to the left-hand diagram, and exactly the
same argument used in the proof of Proposition 4.16 allows to conclude. □

The following two propositions are well known in stable homotopy theory. For
the convenience of the reader, we have included short homotopical proofs in the
context of symmetric spectra; see also [40, 4.3]. We defer the proof of the second
proposition to Section 5.

Proposition 4.30. Let f : X−→Y be a morphism of simplicial symmetric spectra
(resp. simplicial R-modules). Let k ∈ Z.
(a) If Y is objectwise k-connected, then |Y | is k-connected.
(b) If f is objectwise k-connected, then |f | : |X|−→|Y | is k-connected.

Proof. Consider part (b) for the case of symmetric spectra. We need to verify that
the realization |f | : |X|−→|Y | is k-connected. By exactly the same argument as
in the proof of [32, 9.21], it follows from a ﬁltration of degenerate subobjects (see
also [40, 4.3]) that the induced map Dfn : DXn−→DYn on degenerate subobjects
is k-connected for each n ≥ 1. Using exactly the same argument as in the proof
of [32, 4.8], it then follows from the skeletal ﬁltration of realization that |f | is k-
connected. Part (a) follows from part (b) by considering the map ∗−→Y . The case

24 JOHN E. HARPER AND KATHRYN HESS

of R-modules reduces to the case of symmetric spectra by applying the forgetful
functor. □

Remark 4.31. It is important to note (Basic Assumption 1.2), particularly in Propo-
sition 4.32 below, that the tensor product ⊗S denotes the usual smash product of
symmetric spectra [39, 2.2.3]. For notational convenience, in this paper we use the
smash product notation ∧ to denote the smash product of R-modules (Deﬁnition
7.4), since the entire paper is written in this context. In particular, in the special
case when R = S, the two agree ∧ = ⊗S.

Proposition 4.32. Consider symmetric sequences in R-modules. Let m, n ∈ Z
and t ≥ 1. Assume that R is (−1)-connected.

(a) If X, Y are symmetric spectra such that X is m-connected and Y is n-
connected, then X⊗
L
SY is (m + n + 1)-connected.
(b) If X, Y are R-modules such that X is m-connected and Y is n-connected,
then X ∧
L Y is (m + n + 1)-connected.
(c) If X, Y are R-modules with a right (resp. left) Σt-action such that X is
m-connected and Y is n-connected, then X ∧
L
Σt Y is (m + n + 1)-connected.
(d) If X, Y are symmetric sequences such that X is m-connected and Y is n-
connected, then X ˇ⊗
LY is (m + n + 1)-connected.
(e) If X, Y are symmetric sequences with a right (resp. left) Σt-action such
that X is m-connected and Y is n-connected, then X ˇ⊗
L
Σt Y is (m + n + 1)-
connected.

Here, ⊗L
S, ∧
L, ∧
L
Σt , ˇ⊗L, and ˇ⊗L
Σt are the total left derived functors of ⊗S, ∧, ∧Σt ,
ˇ⊗, and ˇ⊗Σt respectively.

Proposition 4.33. Let O be an operad in R-modules such that O[0] = ∗. As-
sume that O satisﬁes Coﬁbrancy Condition 4.12. Let X be a coﬁbrant O-algebra
(resp. coﬁbrant left O-module) and k ≥ 1. If O, R are (−1)-connected and X is
0-connected, then | Bar(τkO, O, X)| is 0-connected and both | Bar(O>k, O, X)| and
| Bar(ik+1O, O, X)| are k-connected.

Proof. This follows from Theorem 4.11 and Propositions 4.30 and 4.32. □

The following Milnor type short exact sequences are well known in stable homo-
topy theory (for a recent reference, see [16]); they can be established as a conse-
quence of [9, IX].

Proposition 4.34. Consider any tower B0 ← B1 ← B2 ← · · · of symmetric
spectra (resp. R-modules). There are natural short exact sequences

0 → lim1
k πi+1Bk → πi holimk Bk → limk πiBk → 0.

Proof of Theorem 1.12(a). It suﬃces to consider the case of left O-modules. By
Theorem 3.26 and Propositions 3.30 and 3.31, we can restrict to operads O satisfying
Coﬁbrancy Condition 1.15. It is enough to treat the following special case. Let X
be a 0-connected, coﬁbrant left O-module. We need to verify that the natural coaug-
mentation X ≃ holimk X−→ holimk(τkO ◦O X) is a weak equivalence. By Proposi-
tion 4.13 it suﬃces to verify that holimk | Bar(O, O, X)|−→ holimk | Bar(τkO, O, X)|

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 25

is a weak equivalence. Consider the commutative diagram

πi holimk | Bar(O, O, X)|

∼=   
 (∗) // πi holimk | Bar(τkO, O, X)|

(∗′′)
  
limk πi| Bar(O, O, X)| (∗′) // limk πi| Bar(τkO, O, X)|

for each i. Since lim
1
k πi+1| Bar(O, O, X)| = 0, the left-hand vertical map is an
isomorphism by Proposition 4.34. We need to show that the map (∗) is an iso-
morphism, hence it suﬃces to verify that (∗′) and (∗′′) are isomorphisms. First
note that Propositions 4.28 and 4.33 imply that (∗′) is an isomorphism. Similarly,
by Propositions 4.16 and 4.33, it follows that for each k ≥ 1 the induced map
πi| Bar(τk+1O, O, X)|−→πi| Bar(τkO, O, X)| is an isomorphism for i ≤ k and a sur-
jection for i = k + 1; in particular, for each ﬁxed i the tower of abelian groups
{πi| Bar(τkO, O, X)|} is eventually constant. Hence lim
1
k πi+1| Bar(τkO, O, X)| = 0
and by Proposition 4.34 the map (∗′′) is an isomorphism which ﬁnishes the proof. By
the argument above, note that for each k ≥ 1 the natural maps πiX−→πi(τkO◦OX)
and πi(τk+1O ◦O X)−→πi(τkO ◦O X) are isomorphisms for i ≤ k and surjections for
i = k + 1; we sometimes refer to this as the strong convergence of the homotopy
completion tower. □

4.35. On n-connected maps and the homotopy completion tower. The pur-
pose of this subsection is to prove Theorems 1.8, 1.9, and 1.12(b).

Proposition 4.36. Let O be an operad in R-modules such that O[0] = ∗. Assume
that O satisﬁes Coﬁbrancy Condition 1.15. Let X be a coﬁbrant O-algebra (resp.
coﬁbrant left O-module) and k ≥ 2. There are natural weak equivalences

| Bar(ikO, O, X)| ≃ | Bar(ikO, τ1O, | Bar(τ1O, O, X)|)|.(4.37)

Below we give a simple conceptual proof of this proposition using derived func-
tors. An anonymous referee has suggested an alternate proof working directly with
(bi)simplicial bar constructions, for which the interested reader may jump directly
to Remark 4.39. The following proposition is an easy exercise in commuting certain
left derived functors and homotopy colimits; we defer the proof to Section 5.

Proposition 4.38. Let O be an operad in R-modules such that O[0] = ∗. Let k ≥ 2.
If B is a simplicial τ1O-algebra (resp. simplicial left τ1O-module), then there is a
zigzag of weak equivalences

ikO ◦h
τ1O (
hocolim
Algτ1O
∆op B) ≃ hocolim
AlgO
∆op ikO ◦h
τ1O (B)
(resp. ikO ◦h
τ1O hocolim
Ltτ1O
∆op B ≃ hocolim
LtO
∆op ikO ◦h
τ1O B)

natural in B.

Proof of Proposition 4.36. It suﬃces to consider the case of left O-modules. For
notational ease, deﬁne B := | Bar(τ1O, O, X)|. By Theorems 4.21 and 7.27, Propo-
sition 4.38, Proposition 4.20 and Theorem 7.26, there are natural weak equivalences

| Bar(ikO, O, X)| ≃ ikO ◦h
τ1O B ≃ ikO ◦h
τ1O hocolim
Ltτ1 O
∆op Bar(τ1O, τ1O, B)

≃ hocolim
LtO
∆op ikO ◦h
τ1O Bar(τ1O, τ1O, B) ≃ hocolim
LtO
∆op ikO ◦τ1O Bar(τ1O, τ1O, B)

≃ hocolim
LtO
∆op Bar(ikO, τ1O, B) ≃ | Bar(ikO, τ1O, B)|.

26 JOHN E. HARPER AND KATHRYN HESS
 □

Remark 4.39. Here is an alternate proof of Proposition 4.36 that was suggested
by an anonymous referee. It suﬃces to consider the case of left O-modules. For
notational ease, deﬁne B := | Bar(ikO, τ1O, τ1O)|. The right-hand side of (4.37) is
isomorphic to | Bar(B, O, X)| (they are both realizations of a bisimplicial symmetric
sequence). Noting that the natural map B−→ikO of right τ1O-modules (and hence
of right O-modules) is a weak equivalence ([32, 8.4, 8.3]), together with Theorem
4.11 and Proposition 4.5, it follows that | Bar(B, O, X)|−→| Bar(ikO, O, X)| is a
weak equivalence, which ﬁnishes the proof.

Proof of Theorem 1.8. It suﬃces to consider the case of left O-modules. By The-
orem 3.26 and Propositions 3.30 and 3.31, we can restrict to operads O satisfying
Coﬁbrancy Condition 1.15. It is enough to treat the special case where X is a
coﬁbrant left O-module.
Consider part (a). Assume that τ1O ◦O X is n-connected. Then | Bar(τ1O, O, X)|
is n-connected by 4.13, hence by Proposition 4.36, together with Theorem 4.11
and Propositions 4.30 and 4.32, it follows that | Bar(ik+1O, O, X)| is ((k + 1)n + k)-
connected for each k ≥ 1. Hence it follows from 4.16 and 4.13 that for each k ≥ 1 the
natural maps πi(τk+1O ◦O X)−→πi(τkO ◦O X) are isomorphisms for i ≤ (k + 1)n + k
and surjections for i = (k + 1)(n + 1). In particular, for each i ≤ 2n + 1 the tower
{πi(τkO ◦O X)} is a tower of isomorphisms, and since τ1O ◦O X is n-connected,
it follows that each stage in the tower {τkO ◦O X} is n-connected. Since X is
0-connected by assumption, it follows from strong convergence of the homotopy
completion tower (proof of Theorem 1.12(a)) that the map πiX−→πi(τkO ◦O X) is
an isomorphism for every i ≤ k. Hence taking k suﬃciently large (k ≥ n) veriﬁes
that X is n-connected.
Conversely, assume that X is n-connected. Then by Theorem 4.11 and Propo-
sitions 4.30 and 4.32, it follows that | Bar(τkO, O, X)| is n-connected and both
| Bar(O>k, O, X)| and | Bar(ik+1O, O, X)| are ((k + 1)n + k)-connected for each
k ≥ 1. It follows from 4.16, 4.28, and 4.13 that for each k ≥ 1 the natu-
ral maps πiX−→πi(τkO ◦O X) and πi(τk+1O ◦O X)−→πi(τkO ◦O X) are isomor-
phisms for i ≤ (k + 1)n + k and surjections for i = (k + 1)(n + 1). Consequently,
πiX−→πi(τ1O◦OX) is an isomorphism for i ≤ 2n+1 and a surjection for i = 2n+2.
Since X is n-connected, it follows that τ1O ◦O X is n-connected.
Consider part (b). Assume that τ1O ◦O X is n-connected. Then it follows from
the proof of part (a) above that πiX−→πi(τ1O◦OX) is an isomorphism for i ≤ 2n+1
and a surjection for i = 2n + 2. □

Proof of Theorem 1.12(b). The homotopy completion spectral sequence is the ho-
motopy spectral sequence [9] associated to the tower of ﬁbrations (of ﬁbrant ob-
jects) of a ﬁbrant replacement (Deﬁnition 3.12) of the homotopy completion tower,
reindexed as a (second quadrant) homologically graded spectral sequence. Strong
convergence (Remark 1.13) follows immediately from the ﬁrst part of the proof of
Theorem 1.8 by taking n = 0. □

We defer the proof of the following to Section 5.

Proposition 4.40. Consider symmetric sequences in R-modules. Let f : X−→Z
be a map between (−1)-connected objects in ModR (resp. SymSeq). Let m ∈ Z,
n ≥ −1, and t ≥ 1. Assume that R is (−1)-connected.

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 27

(a) If X, Z are ﬂat stable coﬁbrant and f is n-connected, then X ∧t−→Z ∧t (resp.
X ˇ⊗t−→Z ˇ⊗t) is n-connected.
(b) If B ∈ ModRΣ
op
t (resp. B ∈ SymSeqΣ
op
t ) is m-connected, X, Z are posi-
tive ﬂat stable coﬁbrant and f is n-connected, then B ∧ Σt X ∧t−→B ∧ Σt Z ∧t

(resp. B ˇ⊗Σt X ˇ⊗t−→B ˇ⊗Σt Z ˇ⊗t) is (m + n + 1)-connected.

Proposition 4.41. Let n ∈ Z. If {Ak}−→{Bk} is a map of towers in symmet-
ric spectra (resp. R-modules) that is levelwise n-connected, then the induced map
holimk Ak−→ holimk Bk is (n − 1)-connected.

Proof. This follows from the short exact sequences in Proposition 4.34. □

Proof of Theorem 1.9. It suﬃces to consider the case of left O-modules. By The-
orem 3.26 and Propositions 3.30 and 3.31, we can restrict to operads O satisfying
Coﬁbrancy Condition 1.15.
We ﬁrst prove part (c), where it is enough to consider the following special
case. Let X−→Y be a map of left O-modules between coﬁbrant objects in LtO
such that the induced map τ1O ◦O X−→τ1O ◦O Y is an n-connected map between
(−1)-connected objects. Consider the corresponding commutative diagram (4.26)
in SymSeq. If k = 2, then the right-hand vertical map is n-connected by Proposition
4.13. It follows from Proposition 4.36, Proposition 4.20, and Propositions 4.32, 4.40,
and 4.30 that the left-hand vertical map is n-connected for each k ≥ 2. Hence by
Proposition 4.16 and induction on k, the middle vertical map is n-connected for
each k ≥ 2, and Proposition 4.41 ﬁnishes the proof of part (b).
Consider part (b). It is enough to consider the following special case. Let X−→Y
be an (n − 1)-connected map of left O-modules between (−1)-connected coﬁbrant
objects in LtO. Consider the corresponding commutative diagram (4.26) in SymSeq.
It follows from Propositions 4.32, 4.40, and 4.30 that the right-hand vertical map
is (n − 1)-connected for k = 2, and hence by Proposition 4.13 the induced map
τ1O ◦O X−→τ1O ◦O Y is (n − 1)-connected.
Consider part (a). Proceeding as above for part (c), we know that for each k ≥ 1
the induced map τkO ◦O X−→τkO ◦O Y is n-connected, and hence the bottom
horizontal map in the
 πiX //

  
 πiY

  
πi(τkO ◦O X) // πi(τkO ◦O Y )

commutative diagram is an isomorphism for every i < n and a surjection for i = n.
Since X, Y are 0-connected by assumption, it follows from strong convergence of
the homotopy completion tower (proof of Theorem 1.12(a)) that the vertical maps
are isomorphisms for k ≥ i, and hence the top horizontal map is an isomorphism
for every i < n and a surjection for i = n. Part (b) implies the converse.
Consider part (d). By arguing as in the proof of Theorem 1.8, it follows that
the layers of the homotopy completion tower are (n − 1)-connected. Hence by
Proposition 4.34 the homotopy limit of this tower is (n−1)-connected, which ﬁnishes
the proof. □

4.42. Finiteness and the homotopy completion tower. The purpose of this
subsection is to prove Theorem 1.5. The following homotopy spectral sequence for

28 JOHN E. HARPER AND KATHRYN HESS

a simplicial symmetric spectrum is well known; for a recent reference, see [18, X.2.9]
and [40, 4.3].

Proposition 4.43. Let Y be a simplicial symmetric spectrum. There is a natural
homologically graded spectral sequence in the right-half plane such that

E2
p,q = Hp(πq(Y )) =⇒ πp+q(|Y |)

Here, πq(Y ) denotes the simplicial abelian group obtained by applying πq levelwise
to Y .

The following ﬁniteness properties for realization will be useful.

Proposition 4.44. Let Y be a simplicial symmetric spectrum. Let m ∈ Z. Assume
that Y is levelwise m-connected.
(a) If πkYn is ﬁnite for every k, n, then πk|Y | is ﬁnite for every k.
(b) If πkYn is a ﬁnitely generated abelian group for every k, n, then πk|Y | is a
ﬁnitely generated abelian group for every k.

Proof. This follows from Proposition 4.43. □

Recall the following Eilenberg-Moore type spectral sequences; for a recent refer-
ence, see [18, IV.4–IV.6].

Proposition 4.45. Let t ≥ 1. Let X, Y be R-modules with a right (resp. left) Σt-
action. There is a natural homologically graded spectral sequence in the right-half
plane such that
 E2
p,q = Tor
π∗R[Σt]
p,q (π∗X, π∗Y ) =⇒ πp+q(X ∧
L
Σt Y ).

Here, R[Σt] is the group algebra spectrum and ∧
L
Σt is the total left derived functor
of ∧Σt .

The following proposition, which is well known to the experts, will be needed
in the proof of Proposition 4.47 below; since it is a key ingredient in the proof of
Theorem 1.5, and since we are unaware of an appropriate reference in literature,
we give a concise homotopy theoretic proof in Section 5.

Proposition 4.46. Let A be any monoid object in (ChZ, ⊗, Z). Let M, N be un-
bounded chain complexes over Z with a right (resp. left) action of A. Let m ∈ Z.
Assume that A is (−1)-connected, M, N are m-connected, and HkM, HkA are
ﬁnitely generated abelian groups for every k.
(a) If HkN is ﬁnite for every k, then Hk(M ⊗
L
AN ) is ﬁnite for every k.
(b) If HkN is a ﬁnitely generated abelian group for every k, then Hk(M ⊗
L
AN )
is a ﬁnitely generated abelian group for every k.
Here, ⊗
L
A is the total left derived functor of ⊗A.

Proposition 4.47. Let t ≥ 1. Let X, Y be R-modules with a right (resp. left)
Σt-action. Let m ∈ Z. Assume that R is (−1)-connected, X, Y are m-connected,
and πkX, πkR are ﬁnitely generated abelian groups for every k.
(a) If πkY is ﬁnite for every k, then πk(X ∧
L
Σt Y ) is ﬁnite for every k.
(b) If πkY is a ﬁnitely generated abelian group for every k, then πk(X ∧
L
Σt Y )
is a ﬁnitely generated abelian group for every k.
Here, ∧
L
Σt is the total left derived functor of ∧Σt .

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 29

Proof. Part (a) follows from Propositions 4.45 and 4.46, and the proof of part (b)
is similar. □

Proof of Theorem 1.5. It suﬃces to consider the case of left O-modules. By The-
orem 3.26 and Propositions 3.30 and 3.31, we can restrict to operads O satisfying
Coﬁbrancy Condition 1.15. We ﬁrst prove part (a), for which it suﬃces to consider
the following special case. Let X be a coﬁbrant left O-module such that τ1O ◦O X is
0-connected and πi(τ1O ◦O X) is objectwise ﬁnite for every i. Consider the coﬁber
sequences

| Bar(ikO, O, X)| // | Bar(τkO, O, X)| // | Bar(τk−1O, O, X)|

in SymSeq. We know by Proposition 4.13 that πi| Bar(τ1O, O, X)| is objectwise
ﬁnite for every i, hence by Proposition 4.36, Proposition 4.20, and Propositions
4.44 and 4.47, πi| Bar(ikO, O, X)| is objectwise ﬁnite for every i. By Proposition
4.16 and induction on k, it follows that πi| Bar(τkO, O, X)| is objectwise ﬁnite for
every i and k. Hence by the ﬁrst part of the proof of Theorem 1.8 (by taking
n = 0) it follows easily that πi(X h∧) is objectwise ﬁnite for every i. If furthermore
X is 0-connected, then by Theorem 1.12(a) the natural coaugmentation X ≃ X h∧

is a weak equivalence which ﬁnishes the proof of part (a). The proof of part (b) is
similar. □

5. Homotopical analysis of the forgetful functors

The purpose of this section is to prove Theorem 4.11 together with several closely
related technical results on the homotopical properties of the forgetful functors. We
will also prove Theorem 3.20 and Propositions 3.30, 4.32, 4.40, and 4.46, each of
which uses constructions or results established below in Section 5. It will be useful
to work in the following context.

Basic Assumption 5.1. From now on in this section we assume that (C, ∧ , S)
is a closed symmetric monoidal category with all small limits and colimits. In
particular, C has an initial object ∅ and a terminal object ∗.

In some of the propositions that follow involving homotopical properties of O-
algebras and left O-modules, we will explicitly assume the following.

Homotopical Assumption 5.2. If O is an operad in C, assume that
(i) C is a coﬁbrantly generated model category in which the generating coﬁbra-
tions and acyclic coﬁbrations have small domains [70, 2.2], and that with
respect to this model structure (C, ∧ , S) is a monoidal model category [70,
3.1]; and
(ii) the following model structure exists on AlgO (resp. LtO): the model struc-
ture on AlgO (resp. LtO) has weak equivalences and ﬁbrations created by
the forgetful functor U (2.20); i.e., the weak equivalences are the underlying
weak equivalences and the ﬁbrations are the underlying ﬁbrations.

Remark 5.3. The main reason for working in the generality of a monoidal model
category (C, ∧ ) is because when we start oﬀ with arguments using the properties
of a particular monoidal model category, say, (ModR, ∧ ), we are naturally led
to need the corresponding results in the diagram category (SymSeq, ˇ⊗), and in
the diagram category (SymArray, ˜⊗) (e.g., Proposition 5.54). So working in the
generality of a monoidal model category allows us to give a single proof that works

30 JOHN E. HARPER AND KATHRYN HESS

for several diﬀerent contexts. For instance, we also use the results in this section
in the contexts of both symmetric spectra and unbounded chain complexes, even
when proving the main theorems only in the context of symmetric spectra (e.g., in
the proof of Proposition 4.46).

Deﬁnition 5.4. Consider symmetric sequences in C. A symmetric array in C is
a symmetric sequence in SymSeq; i.e., a functor A : Σop−→SymSeq. Denote by
SymArray := SymSeqΣ
op the category of symmetric arrays in C and their natural
transformations.

Recall from [31] the following proposition.

Proposition 5.5. Let O be an operad in C, A ∈ AlgO (resp. A ∈ LtO), and Y ∈ C
(resp. Y ∈ SymSeq). Consider any coproduct in AlgO (resp. LtO) of the form
A ∐ O ◦ (Y ) (resp. A ∐ (O ◦ Y )). There exists a symmetric sequence OA (resp.
symmetric array OA) and natural isomorphisms

A ∐ O ◦ (Y ) ∼= ∐

q≥0 OA[q] ∧ Σq Y ∧q (
resp. A ∐ (O ◦ Y ) ∼= ∐

q≥0 OA[q] ˇ⊗Σq Y ˇ⊗q)

in the underlying category C (resp. SymSeq). If q ≥ 0, then OA[q] is naturally
isomorphic to a colimit of the form

OA[q] ∼= colim
( ∐

p≥0 O[p + q] ∧ Σp A
∧p ∐

p≥0 O[p + q] ∧ Σp (O ◦ (A))
∧p
d1
oo d0oo )
,

resp. OA[q] ∼= colim
( ∐

p≥0 O[p + q] ∧ Σp A ˇ⊗p ∐

p≥0 O[p + q] ∧ Σp (O ◦ A) ˇ⊗p
d1
oo d0oo )
,

in C
Σ
op
q (resp. SymSeqΣ
op
q ), with d0 induced by operad multiplication and d1 induced
by the left O-action map m : O ◦ (A)−→A (resp. m : O ◦ A−→A).

Remark 5.6. Other possible notations for OA include UO(A) or U(A); these are
closer to the notation used in [19, 51] and are not to be confused with the forgetful
functors. It is interesting to note—although we will not use it in this paper—that
in the context of O-algebras the symmetric sequence OA has the structure of an
operad; it parametrizes O-algebras under A and is sometimes called the enveloping
operad for A.

Proposition 5.7. Let O be an operad in C and let q ≥ 0. Then the functor
O(−)[q] : AlgO−→C
Σ
op
q (resp. O(−)[q] : LtO−→SymSeqΣ
op
q ) preserves reﬂexive co-
equalizers and ﬁltered colimits.

Proof. This follows from Proposition 2.19 and [33, 5.7]. □

Proposition 5.8. Let O be an operad in C and A an O-algebra. For each q ≥ 0,
O ˆA[q] is concentrated at 0 with value OA[q]; i.e., O ˆA[q] ∼= ̂OA[q].

Proof. This follows from Proposition 5.5, together with (2.5) and (2.15). □

Deﬁnition 5.9. Let i : X−→Y be a morphism in C (resp. SymSeq) and t ≥ 1.
Deﬁne Qt
0 := X ∧t (resp. Qt
0 := X ˇ⊗t) and Qt
t := Y ∧t (resp. Qt
t := Y ˇ⊗t). For 0 <

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 31

q < t deﬁne Qt
q inductively by the left-hand (resp. right-hand) pushout diagrams

Σt ·Σt−q ×Σq X ∧(t−q) ∧ Qq
q−1

i∗
  
 pr∗ // Qt
q−1

  
Σt ·Σt−q ×Σq X ∧(t−q) ∧ Y ∧q // Qt
q
 Σt ·Σt−q×Σq X ˇ⊗(t−q) ˇ⊗Qq
q−1

i∗
  
 pr∗ // Qt
q−1

  
Σt ·Σt−q×Σq X ˇ⊗(t−q) ˇ⊗Y ˇ⊗q // Qt
q

in C
Σt (resp. SymSeqΣt ). We sometimes denote Qt
q by Qt
q(i) to emphasize in the
notation the map i : X−→Y . The maps pr∗ and i∗ are the obvious maps induced
by i and the appropriate projection maps.

The following proposition is proved in [31] and is closely related to a similar
construction in [19]; for other approaches to these types of ﬁltrations compare
[22, 70].

Proposition 5.10. Let O be an operad in C, A ∈ AlgO (resp. A ∈ LtO), and
i : X−→Y in C (resp. SymSeq). Consider any pushout diagram in AlgO (resp.
LtO) of the form
 O ◦ (X) f //

id◦(i)
  
 A

j
  
O ◦ (Y ) // B.
 resp. O ◦ X f //

id◦i
  
 A

j
  
O ◦ Y // B.

(5.11)

The pushout in (5.11) is naturally isomorphic to a ﬁltered colimit of the form

B ∼= colim
( A0 j1 //A1 j2 //A2 j3 // · · ·) in the underlying category C (resp. SymSeq),
with A0 := OA[0] ∼= A and At deﬁned inductively by pushout diagrams in C (resp.
SymSeq) of the form

OA[t] ∧ Σt Qt
t−1

id∧Σt i∗
  
 f∗ // At−1

jt
  
OA[t] ∧ Σt Y ∧t ξt // At
 resp. OA[t] ˇ⊗Σt Qt
t−1

id ˇ⊗Σt i∗
  
 f∗ // At−1

jt
  
OA[t] ˇ⊗Σt Y ˇ⊗t ξt // At

(5.12)

We are now in a good position to prove Theorem 4.11.

Proof of Theorem 4.11. It suﬃces to consider the case of left O-modules. Consider
part (a). Let i : X−→Y be a generating coﬁbration in SymSeq with the positive
ﬂat stable model structure, and consider the pushout diagram

O ◦ X //

  
 Z0

i0
  
O ◦ Y // Z1

(5.13)

in LtO. Assume Z0 is coﬁbrant in LtO; let’s verify that i0 is a positive ﬂat stable coﬁ-
bration in SymSeq. Let A := Z0. By Proposition 5.10, we know Z1 is naturally iso-

morphic to a ﬁltered colimit of the form Z1 ∼= colim
(A0 j1 //A1 j2 //A2 j3 //· · ·)

in the underlying category SymSeq, and hence it suﬃces to verify each jt is a pos-
itive ﬂat stable coﬁbration in SymSeq. By the construction of jt in Proposition

32 JOHN E. HARPER AND KATHRYN HESS

5.10, it is enough to check that each id ˇ⊗Σt i∗ in (5.12) is a positive ﬂat stable coﬁ-
bration in SymSeq. The generating coﬁbrations in SymSeq with the positive ﬂat
stable model structure have coﬁbrant domains, and by Proposition 7.37 we know
that i∗ is a coﬁbration between coﬁbrant objects in SymSeqΣt with the positive ﬂat
stable model structure. We need therefore only show that id ˇ⊗Σt i∗ is a ﬂat stable
coﬁbration in SymSeq.
Suppose p : C−→D is a ﬂat stable acyclic ﬁbration in SymSeq. We want to verify
id ˇ⊗Σt i∗ has the left lifting property with respect to p. Consider any such lifting
problem; we want to verify that the corresponding solid commutative diagram

Qt
t−1

i∗   
 // Map ˇ⊗(OA[t], C)

(∗)
  
Y ˇ⊗t //
 88

Map ˇ⊗(OA[t], D)

(5.14)

in SymSeqΣ
op
t has a lift. We know that i∗ is a ﬂat stable coﬁbration in SymSeqΣ
op
t ,
hence it is enough to verify that (∗) is a ﬂat stable acyclic ﬁbration in SymSeq.
By Proposition 5.16 below, OA[t] is ﬂat stable coﬁbrant in SymSeq, hence we
know that (∗) has the desired property by [33, 6.1], which ﬁnishes the argu-
ment that i0 is a positive ﬂat stable coﬁbration in SymSeq. Consider a sequence

Z0 i0 // Z1 i1 //Z2 i2 //· · · of pushouts of maps as in (5.13), and let Z∞ :=
colimk Zk. Consider the naturally occurring map i∞ : Z0−→Z∞, and assume Z0 is
coﬁbrant in LtO. By the argument above, we know this is a sequence of positive
ﬂat stable coﬁbrations in SymSeq, hence i∞ is a positive ﬂat stable coﬁbration in
SymSeq. Since every coﬁbration A−→B in LtO is a retract of a (possibly transﬁ-
nite) composition of pushouts of maps as in (5.13), starting with Z0 = A, where
A is assumed to be coﬁbrant in LtO, ﬁnishes the proof of part (a). Part (b) fol-
lows from part (a) by taking A = O ◦ ∅, together with the natural isomorphism
O ◦ ∅ ∼= ̂O[0]. □

5.15. Homotopical analysis of the OA constructions. The purpose of this
subsection is to prove the following proposition, which we used in the proof of
Theorem 4.11. It provides a homotopical analysis of the OA constructions, and
a key ingredient in its proof is a ﬁltration of OA (Proposition 5.36). We will also
prove Proposition 5.17 and Theorem 5.18, which are analogs of Proposition 5.16 and
Theorem 4.11, respectively. These analogous results are applicable to a general class
of monoidal model categories, but at the cost of requiring stronger assumptions.
The following proposition is motivated by [51, 13.6].

Proposition 5.16. Let O be an operad in R-modules such that O[r] is ﬂat stable
coﬁbrant in ModR for each r ≥ 0. If A is a coﬁbrant O-algebra (resp. coﬁbrant
left O-module), then OA[r] is ﬂat stable coﬁbrant in ModR (resp. SymSeq) for each
r ≥ 0.

The following proposition is closely related to [51, 13.6].

Proposition 5.17. Let O be an operad in C. Suppose that Homotopical Assumption
5.2 is satisﬁed, and assume that O[r] is coﬁbrant in C
Σ
op
r for each r ≥ 0. If A is a
coﬁbrant O-algebra (resp. coﬁbrant left O-module), then OA[r] is coﬁbrant in C
Σ
op
r
(resp. SymSeqΣ
op
r ) for each r ≥ 0.

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 33

Theorem 5.18. Let O be an operad in C. Suppose that Homotopical Assumption
5.2 is satisﬁed, and assume that O[r] is coﬁbrant in C
Σ
op
r for each r ≥ 0.

(a) If j : A−→B is a coﬁbration between coﬁbrant objects in AlgO (resp. LtO),
then j is a coﬁbration in the underlying category C (resp. SymSeq).
(b) If A is a coﬁbrant O-algebra (resp. coﬁbrant left O-module), then A is
coﬁbrant in the underlying category C (resp. SymSeq).

Proof. It suﬃces to consider the case of left O-modules. Consider part (a). This
follows exactly as in the proof of Theorem 4.11, except using Proposition 5.17
instead of Proposition 5.16, and replacing the lifting problem (5.14) with a lifting
problem of the form

∅ //

  
 Map ˇ⊗(Y ˇ⊗t, C)

(∗)
  
OA[t] //
 44

Map ˇ⊗(Qt
t−1, C) ×Map ˇ⊗(Qt
t−1,D) Map ˇ⊗(Y ˇ⊗t, D)

in SymSeqΣ
op
t . Part (b) follows from part (a) by taking A = O ◦ ∅, together with
the natural isomorphism O ◦ ∅ ∼= ̂O[0], since O[0] is coﬁbrant in C. □

When working with certain arguments involving left modules over an operad,
we are naturally led to replace (C, ∧ , S) with (SymSeq, ˇ⊗, 1) as the underlying
closed symmetric monoidal category. In particular, we will consider symmetric
sequences in (SymSeq, ˇ⊗, 1), i.e., symmetric arrays (Deﬁntion 5.4), together with
the corresponding tensor product and circle product. To avoid notational confusion,
we will use ˜⊗ to denote the tensor product of symmetric arrays and ˜◦ to denote the
circle product of symmetric arrays. We summarize their structure and properties
in the following propositions.

Proposition 5.19. Consider symmetric sequences in C. Let A1, . . . , At and A, B
be symmetric arrays in C. Then the tensor product A1 ˜⊗ · · · ˜⊗At ∈ SymArray and
the circle product A ˜◦ B ∈ SymArray satisfy objectwise the natural isomorphisms

(A1 ˜⊗ · · · ˜⊗At)[r] ∼= ∐

r1+···+rt=r A1[r1] ˇ⊗ · · · ˇ⊗At[rt] ·
Σr1 ×···×Σrt Σr,(5.20)
 (A ˜◦ B)[r] ∼= ∐

t≥0 A[t] ˇ⊗Σt (B ˜⊗t)[r].(5.21)

Deﬁnition 5.22. Consider symmetric sequences in C. Let Z ∈ SymSeq. Deﬁne ˜Z ∈
SymArray to be the symmetric array such that ˜Z[t] ∈ SymSeqΣ
op
t is concentrated
at 0 with value Z[t]; i.e., ˜Z[t] := ̂Z[t] and hence ˜Z[t][0] = Z[t].

The adjunction immediately below Deﬁnition 2.12 induces objectwise the adjunc-
tion ˜− : SymSeq //SymArray : Ev0oo with left adjoint on top and Ev0 the functor
deﬁned objectwise by Ev0(B)[t] := Ev0(B[t]) = B[t][0]; i.e., Ev0(B) = B[−][0].
Note that ˜− embeds SymSeq in SymArray as a full subcategory.

34 JOHN E. HARPER AND KATHRYN HESS

Proposition 5.23. Consider symmetric sequences in C. Let O, A, B ∈ SymSeq
and X, Y ∈ SymArray. There are natural isomorphisms

̃A ˇ⊗B ∼= ˜A ˜⊗ ˜B, ̃A ◦ B ∼= ˜A ˜◦ ˜B, Ev0( ˜O ˜◦ Y ) ∼= O ◦ Ev0(Y ),(5.24)
 Ev0(X ˜⊗Y ) ∼= Ev0(X) ˇ⊗Ev0(Y ), Ev0(X ˜◦ Y ) ∼= Ev0(X) ◦ Ev0(Y ).(5.25)

Proposition 5.26. Consider symmetric sequences in C.
(a) (SymArray, ˜⊗, ˜1) is a closed symmetric monoidal category with all small
limits and colimits. The unit for ˜⊗, denoted “ ˜1”, is the symmetric array
concentrated at 0 with value the symmetric sequence 1.
(b) (SymArray, ˜◦ , ˜I) is a closed monoidal category with all small limits and
colimits. The unit for ˜◦ , denoted “ ˜I”, is the symmetric array concentrated
at 1 with value the symmetric sequence 1. Circle product is not symmetric.

Since all of the statements and constructions in earlier sections that were previ-
ously described in terms of (C, ∧ , S) are equally true for (SymSeq, ˇ⊗, 1), we will cite
and use the appropriate statements and constructions without further comment.

Proposition 5.27. Consider symmetric sequences in C.
(a) If O is an operad in C, then ˜O is an operad in SymSeq.
(b) If A is a left O-module, then ˜A is a left ˜O-module.
(c) There are adjunctions

SymArray ˜O ˜◦ − // Lt ˜O,
U
oo LtO
 ˜− // Lt ˜O,
Ev0
oo Op(C) ˜− // Op(SymSeq)
Ev0
oo(5.28)
 with left adjoints on top, U the forgetful functor and Ev0 the functor deﬁned
objectwise by Ev0(B)[t] := Ev0(B[t]) = B[t][0], i.e., Ev0(B) = B[−][0].
Here, Op(C) denotes the category of operads in C, and similarly for Op(SymSeq).

The following two propositions are exercises left to the reader. They will be
needed in the proof of Proposition 5.31 below.

Proposition 5.29. Let O be an operad in C and A a left O-module. For each q, r ≥
0, ˜O ˜A[q][r] is concentrated at 0 with value OA[q][r] (see (5.5)); i.e., ˜O ˜A[q] ∼= ̃OA[q].

Proposition 5.30. Consider symmetric sequences in C. Let B be a symmetric
sequence (resp. symmetric array) and r, t ≥ 0. There are natural isomorphisms

B[t] ∼= (∐

q≥0
 ̂B[q] ˇ⊗Σq I ˇ⊗q)[t] (
resp. B[t][r] ∼= (∐

q≥0
 ˜B[q] ˜⊗Σq ˆI ˜⊗q)
[r][t]).

Here, ˆI is the symmetric array concentrated at 0 with value I.

The following will be needed in the proof of Proposition 5.36 below.

Proposition 5.31. Let O be an operad in C, A ∈ AlgO (resp. A ∈ LtO), Y ∈ C
(resp. Y ∈ SymSeq) and q ≥ 0. Consider any coproduct in AlgO (resp. LtO) of the
form A ∐ O ◦ (Y ) (resp. A ∐ (O ◦ Y )). There are natural isomorphisms

OA∐O◦(Y )[q] ∼= ∐

p≥0 OA[p + q] ∧ Σp Y ∧p, OO◦(Y )[q] ∼= ∐

p≥0 O[p + q] ∧ Σp Y ∧p

(
resp. OA∐(O◦Y )[q] ∼= ∐

p≥0 OA[p + q] ˇ⊗Σp Y ˇ⊗p, OO◦Y [q] ∼= ∐

p≥0 O[p + q] ∧ Σp Y ˇ⊗p)

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 35

in C
Σ
op
q (resp. SymSeqΣ
op
q ). In particular, there are natural isomorphisms

OO◦(∅)[q] ∼= O[q] (resp. OO◦∅[q] ∼= ̂O[q])
(5.32)

in C
Σ
op
q (resp. SymSeqΣ
op
q ).

Proof. Consider the left-hand natural isomorphisms. Since the case for left O-
modules is more involved, it is useful to consider ﬁrst the case of O-algebras. Let A
be an O-algebra and Y ∈ C. Let Z ∈ SymSeq, and consider the corresponding left
O-module ˆA and the corresponding symmetric sequence ˆY . It follows easily from
Proposition 5.5 and [31, proof of 4.7] that there are natural isomorphisms

ˆA ∐ (O ◦ ˆY ) ∐ (O ◦ Z) ∼= ∐

q≥0 O ˆA∐(O◦ ˆY )[q] ˇ⊗Σq Z ˇ⊗q,(5.33)
 ˆA ∐ (O ◦ ˆY ) ∐ (O ◦ Z) ∼= ∐

q≥0
(∐

p≥0 O ˆA[p + q] ˇ⊗Σp ˆY ˇ⊗p) ˇ⊗Σq Z ˇ⊗q,(5.34)

in the underlying category SymSeq. Comparing (5.33) with (5.34) and taking Z = I,
together with Proposition 5.8 and Proposition 5.30, gives a natural isomorphism of
symmetric sequences of the form

OA∐O◦(Y )[q] ∼= ∐

p≥0 OA[p + q] ∧ Σp Y ∧p, q ≥ 0,

which ﬁnishes the proof of the left-hand natural isomorphisms for the case of O-
algebras.
Consider the case of left O-modules. Let A be a left O-module and Y ∈ SymSeq.
Let Z ∈ SymArray and consider the corresponding operad ˜O in SymSeq, the corre-
sponding left ˜O-module ˜A and the corresponding symmetric array ˜Y . Arguing as
above, by Proposition 5.5 there is a natural isomorphism
∐

q≥0 ˜O ˜A∐( ˜O ˜ ˜Y )[q] ˜⊗Σq Z ˜⊗q ∼= ∐

q≥0
(∐

p≥0 ˜O ˜A[p + q] ˜⊗Σp ˜Y ˜⊗p) ˜⊗Σq Z ˜⊗q,(5.35)

in the underlying category SymArray. By (5.35) and taking Z = ˆI, together with
Proposition 5.29 and Proposition 5.30, gives a natural isomorphism of symmetric
arrays of the form
(OA∐O◦Y [q])[r] ∼= (∐

p≥0 OA[p + q] ˇ⊗Σp Y ˇ⊗p)
[r], q, r ≥ 0,

which ﬁnishes the proof of the left-hand natural isomorphisms for the case of left
O-modules. The proof of the right-hand natural isomorphisms is similar. □

The following ﬁltrations are motivated by [51, 13.7] and generalize the ﬁltered
colimit construction of the form

B ∼= OB[0] ∼= colim
(OA[0] j1 // A1 j2 //A2 j3 //· · · )

in Proposition 5.10 to a ﬁltered colimit construction of OB[r] for each r ≥ 0; for
other approaches to these types of ﬁltrations compare [22, 70].

Proposition 5.36. Let O be an operad in C, A ∈ AlgO (resp. A ∈ LtO), and
i : X−→Y in C (resp. SymSeq). Consider any pushout diagram in AlgO (resp.

36 JOHN E. HARPER AND KATHRYN HESS

LtO) of the form 5.11. For each r ≥ 0, OB[r] is naturally isomorphic to a ﬁltered
colimit of the form

OB[r] ∼= colim
( O0
A[r] j1 // O1
A[r] j2 // O2
A[r] j3 // · · · )
(5.37)

in C
Σ
op
r (resp. SymSeqΣ
op
r ), with O0
A[r] := OA[r] and Ot
A[r] deﬁned inductively by
pushout diagrams in C
Σ
op
r (resp. SymSeqΣ
op
r ) of the form

OA[t + r] ∧ Σt Qt
t−1

id∧Σt i∗
  
 f∗ // Ot−1
A [r]

jt
  
OA[t + r] ∧ Σt Y ∧t ξt // Ot
A[r]
 resp. OA[t + r] ˇ⊗Σt Qt
t−1

id ˇ⊗Σt i∗
  
 f∗ // Ot−1
A [r]

jt
  
OA[t + r] ˇ⊗Σt Y ˇ⊗t ξt // Ot
A[r]

(5.38)

Proof. It suﬃces to consider the case of left O-modules. The argument is a gen-
eralization of the proof given in [31, 4.20] for the case r = 0, hence it is enough
to describe the constructions and arguments needed for future reference and for
a reader of [31, 4.20] to be able to follow the proof. It is easy to verify that the
pushout in (5.11) may be calculated by a reﬂexive coequalizer in LtO of the form

B ∼= colim
( A ∐ (O ◦ Y ) A ∐ (O ◦ X) ∐ (O ◦ Y )
ioo
 f
oo ).(5.39)

The maps i and f are induced by maps id ◦ i∗ and id ◦ f∗, which ﬁt into the
commutative diagram

A ∐ (
O ◦ (X ∐ Y )
)

i    f
  
 O ◦ (A ∐ X ∐ Y )oo
 id◦i∗   
 id◦f∗
  
 O ◦ (
(O ◦ A) ∐ X ∐ Y )d0oo
 d1
oo
 id◦i∗    id◦f∗
  
A ∐ (O ◦ Y ) O ◦ (A ∐ Y )oo O ◦ (
(O ◦ A) ∐ Y )d0oo
 d1
oo

(5.40)

in LtO, with rows reﬂexive coequalizer diagrams, and maps i∗ and f∗ in SymSeq
induced by i : X−→Y and f : X−→A in SymSeq. Here we have used the same
notation for both f and its adjoint (2.20). Applying O(−)[r] to (5.39) and (5.40), it
follows from Proposition 5.7 that OB[r] may be calculated by a reﬂexive coequalizer

OB[r] ∼= colim
( OA∐(O◦Y )[r] OA∐(O◦X)∐(O◦Y )[r]
ioo
 f
oo )
(5.41)
 OA∐(O◦(X∐Y ))[r]

i    f
  
 OO◦(A∐X∐Y )[r]oo
      
 OO◦((O◦A)∐X∐Y )[r]oooo
      
OA∐(O◦Y )[r] OO◦(A∐Y )[r]oo OO◦((O◦A)∐Y )[r]oooo

(5.42)

in SymSeqΣ
op
r of the form (5.41), and that the maps i and f in (5.41) ﬁt into
the commutative diagram (5.42) in SymSeqΣ
op
r , with rows reﬂexive coequalizer di-
agrams. By (5.41), OB[r] may be calculated by the colimit of the left-hand column

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 37

of (5.42) in SymSeqΣ
op
r . By (5.42) and Proposition 5.31, f induces maps f q,p that
make the diagrams

OA∐(O◦(X∐Y ))[r] ∼= ∐

q≥0
 ∐

p≥0

( )

f
  
 (OA[p + q + r] ˇ⊗Σp×Σq X ˇ⊗p ˇ⊗Y ˇ⊗q)
inq,poo
 f q,p
  
OA∐(O◦Y )[r] ∼= ∐

t≥0

( ) (
OA[q + r] ˇ⊗Σq Y ˇ⊗q)
inqoo

in SymSeqΣ
op
r commute. Similarly, i induces maps iq,p that make the diagrams

OA∐(O◦(X∐Y ))[r] ∼= ∐

q≥0
 ∐

p≥0

( )

i
  
 (OA[p + q + r] ˇ⊗Σp×Σq X ˇ⊗p ˇ⊗Y ˇ⊗q)
inq,poo
 iq,p
  
OA∐(O◦Y )[r] ∼= ∐

t≥0

( ) (OA[p + q + r] ˇ⊗Σp+q Y ˇ⊗(p+q))
inp+qoo

in SymSeqΣ
op
r commute.
We can now describe more explicitly what it means to give a cone in SymSeqΣ
op
r
out of the left-hand column of (5.42). Let ϕ : OA∐(O◦Y )[r]−→· be a morphism in
SymSeqΣ
op
r and deﬁne ϕq := ϕinq. Then ϕi = ϕf if and only if the diagrams

OA[p + q + r] ˇ⊗Σp×Σq X ˇ⊗p ˇ⊗Y ˇ⊗q

iq,p
  
 f q,p // OA[q + r] ˇ⊗Σq Y ˇ⊗q

ϕq
  
OA[p + q + r] ˇ⊗Σp+q Y ˇ⊗(p+q) ϕp+q // ·

(5.43)

commute for every p, q ≥ 0. Since iq,0 = id and f q,0 = id, it is suﬃcient to consider
q ≥ 0 and p > 0.
The next step is to reconstruct the colimit of the left-hand column of (5.42)
in SymSeqΣ
op
r via a suitable ﬁltered colimit in SymSeqΣ
op
r . The diagrams (5.43)
suggest how to proceed. Deﬁne O0
A[r] := OA[r] and for each t ≥ 1 deﬁne Ot
A[r] by
the pushout diagram (5.38) in SymSeqΣ
op
r . The maps f∗ and i∗ are induced by the
appropriate maps f q,p and iq,p. Arguing exactly as in [31, proof of 4.20] for the
case r = 0, it is easy to use the diagrams (5.43) to verify that (5.37) is satisﬁed. □

The following proposition is the key result used to prove Proposition 5.17.

Proposition 5.44. Let O be an operad in C. Suppose that Homotopical Assumption
5.2 is satisﬁed.
(a) If j : A−→B is a coﬁbration in AlgO (resp. LtO) such that OA[r] is coﬁ-
brant in C
Σ
op
r (resp. SymSeqΣ
op
r ) for each r ≥ 0, then OA[r]−→OB[r] is a
coﬁbration in C
Σ
op
r (resp. SymSeqΣ
op
r ) for each r ≥ 0.
(b) If j : A−→B is an acyclic coﬁbration in AlgO (resp. LtO) such that OA[r]
is coﬁbrant in C
Σ
op
r (resp. SymSeqΣ
op
r ) for each r ≥ 0, then OA[r]−→OB[r]
is an acyclic coﬁbration in C
Σ
op
r (resp. SymSeqΣ
op
r ) for each r ≥ 0.

38 JOHN E. HARPER AND KATHRYN HESS

Proof. It suﬃces to consider the case of left O-modules. We ﬁrst prove part (a). Let
i : X−→Y be a generating coﬁbration in SymSeq, and consider a pushout diagram
of the form (5.13) in LtO. Assume OZ0[r] is coﬁbrant in SymSeqΣ
op
r for each r ≥ 0;
let’s verify that OZ0 [r]−→OZ1[r] is a coﬁbration in SymSeqΣ
op
r for each r ≥ 0. Deﬁne
A := Z0, and let r ≥ 0. By 5.36 we know that OZ1 [r] is naturally isomorphic to a

ﬁltered colimit of the form OZ1 [r] ∼= colim
( O0
A[r] j1 //O1
A[r] j2 //O2
A[r] j3 //· · ·)

in SymSeqΣ
op
r , hence it is enough to verify each jt is a coﬁbration in SymSeqΣ
op
r . By
the construction of jt in Proposition 5.36, we need only show that each id ˇ⊗Σt i∗ in
(5.38) is a coﬁbration in SymSeqΣ
op
r . Suppose p : C−→D is an acyclic ﬁbration in
SymSeqΣ
op
r . We need to verify that id ˇ⊗Σt i∗ has the left lifting property with respect
to p. Consider any such lifting problem; we want to verify that the corresponding
solid commutative diagram

∅ //

  
 Map ˇ⊗(Y ˇ⊗t, C)

(∗)
  
OA[t + r] //
 44

Map ˇ⊗(Qt
t−1, C) ×Map ˇ⊗(Qt
t−1,D) Map ˇ⊗(Y ˇ⊗t, D)

in SymSeq(Σt×Σr )op has a lift. By assumption, OA[t + r] is coﬁbrant in SymSeqΣ
op
t+r ,
hence OA[t + r] is coﬁbrant in SymSeq(Σt×Σr )op , and it is enough to check that (∗)
is an acyclic ﬁbration in SymSeq. We know that i∗ is a coﬁbration in SymSeq by
[33, 7.19], hence we know that (∗) has the desired property by [33, 6.1], which
ﬁnishes the argument that OZ0[r]−→OZ1 [r] is a coﬁbration in SymSeqΣ
op
r for each
r ≥ 0. Consider a sequence Z0 //Z1 // Z2 // · · · of pushouts of maps
as in (5.13). Assume OZ0[r] is coﬁbrant in SymSeqΣ
op
r for each r ≥ 0. De-
ﬁne Z∞ := colimk Zk, and consider the natural map Z0−→Z∞. We know from
above that OZ0[r] //OZ1 [r] //OZ2 [r] //· · · is a sequence of coﬁbrations in
SymSeqΣ
op
r , hence OZ0 [r]−→OZ∞ [r] is a coﬁbration in SymSeqΣ
op
r . Since every coﬁ-
bration A−→B in LtO is a retract of a (possibly transﬁnite) composition of pushouts
of maps as in (5.13), starting with Z0 = A, and OA[r] is coﬁbrant in SymSeqΣ
op
r for
each r ≥ 0, the proof of part (a) is complete. The proof of part (b) is similar. □

Proof of Proposition 5.17. This follows from Proposition 5.44(a) by taking A =
O ◦ (∅) (resp. A = O ◦ ∅), together with (5.32) and the assumption that O[r] is
coﬁbrant in C
Σ
op
r for each r ≥ 0. □

The following proposition is the key result used to prove Proposition 5.16.

Proposition 5.45. Let O be an operad in R-modules.

(a) If j : A−→B is a coﬁbration in AlgO (resp. LtO) such that OA[r] is ﬂat sta-
ble coﬁbrant in ModR (resp. SymSeq) for each r ≥ 0, then OA[r]−→OB[r]
is a positive ﬂat stable coﬁbration in ModR (resp. SymSeq) for each r ≥ 0.
(b) If j : A−→B is an acyclic coﬁbration in AlgO (resp. LtO) such that OA[r]
is ﬂat stable coﬁbrant in ModR (resp. SymSeq) for each r ≥ 0, then
OA[r]−→OB[r] is a positive ﬂat stable acyclic coﬁbration in ModR (resp.
SymSeq) for each r ≥ 0.

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 39

Proof. It suﬃces to consider the case of left O-modules. Consider part (a). Let
i : X−→Y be a generating coﬁbration in SymSeq with the positive ﬂat stable model
structure, and consider a pushout diagram of the form (5.13) in LtO. Assume OZ0 [r]
is ﬂat stable coﬁbrant in SymSeq for each r ≥ 0; let’s verify that OZ0[r]−→OZ1 [r] is
a positive ﬂat stable coﬁbration in SymSeq for each r ≥ 0. Deﬁne A := Z0, and let
r ≥ 0. By Proposition 5.36, OZ1 [r] is naturally isomorphic to a ﬁltered colimit of

the form OZ1[r] ∼= colim
(O0
A[r] j1 //O1
A[r] j2 // O2
A[r] j3 // · · ·) in SymSeq, hence
it is enough to verify each jt is a positive ﬂat stable coﬁbration in SymSeq. By
the construction of jt in Proposition 5.36, we need only check that each id ˇ⊗Σt i∗
in (5.38) is a positive ﬂat stable coﬁbration in SymSeq. By Proposition 7.37, i∗ is
a coﬁbration between coﬁbrant objects in SymSeqΣt with the positive ﬂat stable
model structure. It is thus enough to verify that id ˇ⊗Σt i∗ is a ﬂat stable coﬁbration
in SymSeq.
Suppose p : C−→D is a ﬂat stable acyclic ﬁbration in SymSeq. We want to show
that id ˇ⊗Σt i∗ has the left lifting property with respect to p. By assumption OA[t+r]
is ﬂat stable coﬁbrant in SymSeq, hence by exactly the same argument used in the
proof of Theorem 4.11, id ˇ⊗Σt i∗ has the left lifting property with respect to p,
which ﬁnishes the argument that OZ0[r]−→OZ1 [r] is a positive ﬂat stable coﬁbra-
tion in SymSeq for each r ≥ 0. Consider a sequence Z0 //Z1 //Z2 // · · · of
pushouts of maps as in (5.13), deﬁne Z∞ := colimk Zk, and consider the naturally
occurring map Z0−→Z∞. Assume OZ0 [r] is ﬂat stable coﬁbrant in SymSeq for each
r ≥ 0. By the argument above we know that OZ0 [r] //OZ1[r] // OZ2[r] // · · ·
is a sequence of positive ﬂat stable coﬁbrations in SymSeq, hence OZ0 [r]−→OZ∞ [r]
is a positive ﬂat stable coﬁbration in SymSeq. Noting that every coﬁbration A−→B
in LtO is a retract of a (possibly transﬁnite) composition of pushouts of maps as
in (5.13), starting with Z0 = A, together with the assumption that OA[r] is ﬂat
stable coﬁbrant in SymSeq for each r ≥ 0, ﬁnishes the proof of part (a). Con-
sider part (b). By arguing exactly as in part (a), except using generating acyclic
coﬁbrations instead of generating coﬁbrations, it follows that OA[r]−→OB[r] is a
monomorphism and a weak equivalence in SymSeq; for instance, this follows from
exactly the same argument used in the proof of Proposition 7.19. Noting by part
(a) that OA[r]−→OB[r] is a positive ﬂat stable coﬁbration in SymSeq ﬁnishes the
proof. □

Proof of Proposition 5.16. This follows from Proposition 5.45(a) by taking A =
O ◦ (∅) (resp. A = O ◦ ∅), together with (5.32) and the assumption that O[r] is ﬂat
stable coﬁbrant in ModR for each r ≥ 0. □

5.46. Homotopical analysis of OA for coﬁbrant operads. The purpose of this
subsection is to prove Theorem 3.20. We will also prove Theorems 5.49, 5.50, and
5.51 (resp. Propositions 5.55 and 5.56), which are analogs of Theorem 4.11 (resp.
Proposition 5.16). These analogous results, for operads in R-modules and operads
in a general class of monoidal model categories, require strong assumptions on the
(maps of) operads involved, that allow us to replace arguments involving ﬁltrations
of OA with lifting arguments involving maps of endomorphism operads of diagrams.
In the next results, we need to work with operads satisfying good lifting proper-
ties, as speciﬁed by the deﬁnition below.

40 JOHN E. HARPER AND KATHRYN HESS

Deﬁnition 5.47. Suppose that C satisﬁes Homotopical Assumption 5.2(i). A mor-
phism of operads in C is a ﬁbration (resp. weak equivalence) of operads if the under-
lying morphism of symmetric sequences is a ﬁbration (resp. weak equivalence) in
the corresponding projective model stucture on SymSeq. A coﬁbration of operads
in C is a morphism of operads that satisﬁes the left lifting property with respect to
all ﬁbrations of operads that are weak equivalences. An operad O in C is coﬁbrant
if the unique map from the initial operad to O is a coﬁbration of operads.

While we have found it convenient to use model category terminology in the
deﬁnition above, none of the results in this paper require a model structure to exist
on the category of operads in C, and we will not establish one in this paper. The
following proposition was used in Subsection 3.16.

Proposition 5.48. Let f : O−→O′ be a map of operads in C. Suppose that C
satisﬁes Homotopical Assumption 5.2(i). Then f has a functorial factorization in

the category of operads as O g
−→ J h
−→ O′, a coﬁbration followed by a weak equivalence
which is also a ﬁbration (Deﬁnition 5.47).

Proof. Consider symmetric sequences in C. Since C satisﬁes Homotopical Assump-
tion 5.2(i), it is easy to verify, using the corresponding adjunctions (Gp, Evp) in
(7.9), that the diagram category SymSeq also satisﬁes Homotopical Assumption
5.2(i). Consider the free-forgetful adjunction F : SymSeq //Op : Uoo with left ad-
joint on top and U the forgetful functor; here, Op denotes the category of operads.
It is easy to verify that the functor F can be constructed by a ﬁltered colimit of
the form

F (A) ∼= colim
(
I → I ∐ A → I ∐ A ◦ (I ∐ A) → I ∐ A ◦ (I ∐ A ◦ (I ∐ A)) → . . . )

in the underlying category SymSeq; this useful description appears in [61]. Since
the forgetful functor U commutes with ﬁltered colimits, it follows from [70, Remark
2.4] that the smallness conditions required in [70, Lemma 2.3] are satisﬁed, and the
(possibly transﬁnite) small object argument described in the proof of [70, Lemma
2.3] ﬁnishes the proof. □

The following theorem is motivated by [61, 4.1.14].

Theorem 5.49. Let g : O−→O′ be a coﬁbration of operads in C. Suppose that O, O′

and C satisfy Homotopical Assumption 5.2.

(a) If i : X−→Z is a coﬁbration in AlgO′ (resp. LtO′ ), and X is coﬁbrant in
the underlying category C (resp. SymSeq), then i is a coﬁbration in AlgO
(resp. LtO).
(b) If the forgetful functor AlgO−→C (resp. LtO−→SymSeq) preserves coﬁbrant
objects, and Y is a coﬁbrant O′-algebra (resp. coﬁbrant left O′-module), then
Y is coﬁbrant in AlgO (resp. LtO).

Proof. It suﬃces to consider the case of left O′-modules. Consider part (b). Let Y
be a coﬁbrant left O′-module. The map ∅−→Y in LtO factors functorially in LtO
as ∅ → X p
−→ Y a coﬁbration followed by an acyclic ﬁbration; here, ∅ denotes an
initial object in LtO. We ﬁrst want to show there exists a left O′-module structure

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 41

on X such that p is a map in LtO′ . Consider the solid commutative diagram

O

g   
 // End(X p
−→ Y )

(∗)
  
 (∗∗) // Map
◦(X, X)

(id,p)
  
O′ m //

m 99

Map
◦(Y, Y ) (p,id) // Map
◦(X, Y )

in SymSeq such that the right-hand square is a pullback diagram. It is easy to
verify that the maps (∗) and (∗∗) are morphisms of operads. By assumption, X
is coﬁbrant in SymSeq, hence we know that (id, p) is an acyclic ﬁbration by [33,
6.2], and therefore (∗) is an acyclic ﬁbration in SymSeq. Since g is a coﬁbration of
operads, there exists a morphism of operads m that makes the diagram commute.

It follows that the composition O′ m
−→ End(X p
−→ Y ) (∗∗)
−−→ Map
◦(X, X) of operad
maps determines a left O′-module structure on X such that p is a morphism of
left O′-modules. To ﬁnish the proof, we need to show that Y is coﬁbrant in LtO.
Consider the solid commutative diagram

∅

  
 // X

p
  
Y
 ξ ??
 Y

in LtO′ , where ∅ denotes an initial object in LtO′ . Since Y is coﬁbrant in LtO′ , and p
is an acyclic ﬁbration, this diagram has a lift ξ in LtO′ . In particular, Y is a retract
of X in LtO′ , and hence in LtO. Noting that X is coﬁbrant in LtO ﬁnishes the proof
of part (b). Part (a) can be established exactly as in the proof of Theorem 5.50(a),
by replacing the map I−→O with the map O−→O′. □

Proof of Theorem 3.20. It suﬃces to consider the case of left O-modules. Since X
is coﬁbrant in LtO and g∗ is a left Quillen functor, g∗(X) is coﬁbrant in LtJ1 and
hence by 7.21 and 7.23 it follows that g∗g∗(X) ≃ TQ(X). To iterate the argument,
it suﬃces to verify that the right Quillen functor g∗ preserves coﬁbrant objects:
this follows from Theorem 5.49 and Theorem 4.11. □

The following theorem is closely related to [61, 4.1.15].

Theorem 5.50. Let O be a coﬁbrant operad in C. Suppose that Homotopical As-
sumption 5.2 is satisﬁed.

(a) If i : X−→Z is a coﬁbration in AlgO (resp. LtO), and X is coﬁbrant in
the underlying category C (resp. SymSeq), then i is a coﬁbration in the
underlying category C (resp. SymSeq).
(b) If Y is a coﬁbrant O-algebra (resp. coﬁbrant left O-module), then Y is
coﬁbrant in the underlying category C (resp. SymSeq).
(c) If the unit S is coﬁbrant in C, then O[r] is coﬁbrant in C
Σ
op
r for each r ≥ 0.

Proof. The proof of this result is very similar to that of the previous theorem. It
suﬃces to consider the case of left O-modules. Consider part (a). Let i : X−→Z
be a coﬁbration in LtO. The map i factors functorially in the underlying category
SymSeq as X j
−→ Y p
−→ Z, a coﬁbration followed by an acyclic ﬁbration. We want

42 JOHN E. HARPER AND KATHRYN HESS

ﬁrst to show there exists a left O-module structure on Y such that j and p are maps
in LtO. Consider the solid commutative diagram

I

  
 // End(X j
−→ Y p
−→ Z)

(∗)
  
 (∗∗) // Map
◦(Y, Y )

(j,p)
  
O m //

m
 99

End(X i
−→ Z) // Map
◦(X, Y ) ×Map◦(X,Z) Map
◦(Y, Z)

in SymSeq such that the right-hand square is a pullback diagram. It is easy to
verify that the maps (∗) and (∗∗) are morphisms of operads. By assumption, X is
coﬁbrant in SymSeq, hence we know that the pullback corner map (j, p) is an acyclic
ﬁbration by [33, 6.2], and therefore (∗) is an acyclic ﬁbration in SymSeq. Since O
is a coﬁbrant operad, the map I−→O is a coﬁbration of operads, and there exists
a morphism of operads m that makes the diagram commute. It follows that the

composition O m
−→ End(X j
−→ Y p
−→ Z) (∗∗)
−−→ Map
◦(Y, Y ) of operad maps determines
a left O-module structure on Y such that j and p are morphisms of left O-modules.
To ﬁnish the proof, we need to show that i is a coﬁbration in SymSeq. Consider
the solid commutative diagram
 X

i   
 j // Y
 p
  
Z
 ξ >>
 Z

in LtO. Since i is a coﬁbration and p is an acyclic ﬁbration in LtO, the diagram has
a lift ξ in LtO. In particular, i is a retract of j in LtO, and hence in the underlying
category SymSeq. Noting that j is a coﬁbration in SymSeq ﬁnishes the proof of
part (a). Part (b) follows immediately from [32, proof of 10.2], which uses a similar
argument; it is also a special case of Theorem 5.49(b). Consider part (c). By
assumption, the unit S is coﬁbrant in C, hence the map ∅−→I is a coﬁbration in
SymSeq and therefore O ◦ ∅−→O ◦ I is a coﬁbration in LtO. Hence O ∼= O ◦ I is a
coﬁbrant left O-module, and part (b) ﬁnishes the proof. □

Theorem 5.51. Let O be a coﬁbrant operad in R-modules with respect to the pos-
itive ﬂat stable model structure.

(a) O[r] is ﬂat stable coﬁbrant in ModRΣ
op
r for each r ≥ 0.
(b) If i : X−→Z is a coﬁbration in AlgO (resp. LtO), and X is ﬂat stable
coﬁbrant in the underlying category ModR (resp. SymSeq), then i is a ﬂat
stable coﬁbration in the underlying category ModR (resp. SymSeq).

Proof. Since every ﬂat stable ﬁbration in SymSeq is a positive ﬂat stable ﬁbration in
SymSeq, it follows that O is also a coﬁbrant operad in R-modules with respect to the
ﬂat stable model structure. The proof of Theorem 5.50 ﬁnishes the argument. □

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 43

Proposition 5.52. Let O be an operad in C and A ∈ AlgO (resp. A ∈ LtO).
Consider the pushout diagram in LtO (resp. Lt ˜O) of the form

O ◦ ∅ //

  
 ˆA

j
  
O ◦ I // ˆA ∐ (O ◦ I)
 resp. ˜O ˜◦ ∅ //

  
 ˜A

j
  
˜O ˜◦ ˆI // ˜A ∐ ( ˜O ˜◦ ˆI)

(5.53)

There are natural isomorphisms OA[t] ∼= ( ˆA ∐ (O ◦ I)
)
[t] (resp. OA[t][r] ∼= ( ˜A ∐
( ˜O ˜◦ ˆI)
)
[r][t]) for each r, t ≥ 0. Here, ˆI is the symmetric array concentrated at 0
with value I.

Proof. This follows from Propositions 5.5, 5.8, 5.29, and 5.30. □

Proposition 5.54. Let O be a coﬁbrant operad in C. Suppose that O, ˜O and C
satisfy Homotopical Assumption 5.2. If i : X−→Z is a coﬁbration in Lt ˜O such that
X is coﬁbrant in the underlying category SymArray, then i is a coﬁbration in the
underlying category SymArray.

Proof. This proof is similar to that of Theorem 5.50, except for the following vari-
ation on the lifting argument. Let i : X−→Z be a coﬁbration in Lt ˜O. The map i

factors functorially in the underlying category SymArray as X j
−→ Y p
−→ Z, a coﬁbra-
tion followed by an acyclic ﬁbration. We need to show there exists a left ˜O-module
structure on Y such that j and p are maps in Lt ˜O. Consider the solid diagram

End(X j
−→ Y p
−→ Z)

(∗)
  
 (∗∗) // Map ˜◦ (Y, Y )

(j,p)
  
˜O m //

m
 99

End(X i
−→ Z) // Map ˜◦ (X, Y ) ×Map ˜◦ (X,Z) Map ˜◦ (Y, Z)

in SymArray, such that the square is a pullback diagram. It is easy to verify that
the maps (∗) and (∗∗) are morphisms of operads. Since X is coﬁbrant in SymArray,
the pullback corner map (j, p) is an acyclic ﬁbration in SymArray by [33, 6.2], and
therefore (∗) is as well. We need to show there exists a map of operads m that
makes the diagram commute. By the right-hand adjunction in (5.28), it is enough
to show there exists a map m of operads in C that makes the corresponding diagram

Ev0(
End(X j
−→ Y p
−→ Z)
)

Ev0(∗)
  
O m //

m
 77

Ev0(
End(X i
−→ Z)
)

of operads in C commute. Since O is a coﬁbrant operad in C, the desired lift m
exists. It follows that the composition (∗∗)m of operad maps determines a left
˜O-module structure on Y such that j and p are morphisms of left ˜O-modules. To
ﬁnish the proof, we need to show that i is a coﬁbration in SymArray, which follows
exactly as in the proof of Theorem 5.50. □

44 JOHN E. HARPER AND KATHRYN HESS

Proposition 5.55. Let O be a coﬁbrant operad in C. Suppose that O, ˜O and C
satisfy Homotopical Assumption 5.2. If the unit S is coﬁbrant in C, and A is an
O-algebra (resp. left O-module) that is coﬁbrant in the underlying category C (resp.
SymSeq), then OA[r] is coﬁbrant in C
Σ
op
r (resp. SymSeqΣ
op
r ) for each r ≥ 0.

Proof. This follows from Proposition 5.52, Theorem 5.50, and Proposition 5.54. □

Proposition 5.56. Let O be a coﬁbrant operad in R-modules with respect to the
positive ﬂat stable model structure. If A is an O-algebra (resp. left O-module) that
is ﬂat stable coﬁbrant in ModR (resp. SymSeq), then OA[r] is ﬂat stable coﬁbrant
in ModRΣ
op
r (resp. SymSeqΣ
op
r ) for each r ≥ 0.

Proof. Since every ﬂat stable ﬁbration in SymSeq is a positive ﬂat stable ﬁbration in
SymSeq, it follows that O is also a coﬁbrant operad in R-modules with respect to the
ﬂat stable model structure. The proof of Proposition 5.55 ﬁnishes the argument. □

5.57. Proofs. The purpose of this short subsection is to prove Propositions 3.30,
4.32, 4.38, 4.40, and 4.46.

Proof of Proposition 3.30. This follows from a small object argument together with
an analysis of the functor F appearing in F : SymSeq //Op : Uoo the free-forgetful
adjunction with left adjoint on top and U the forgetful functor; here, Op denotes
the category of operads. It is easy to verify that the functor F can be constructed
by a ﬁltered colimit of the form

F (A) ∼= colim
(
I → I ∐ A → I ∐ A ◦ (I ∐ A) → I ∐ A ◦ (I ∐ A ◦ (I ∐ A)) → . . . )

in the underlying category SymSeq; this useful description appears in [61]. Using
this description of F , it is easy to verify that the unit map I−→O′ of the operad O′

constructed in the small object argument satisﬁes the desired property in Coﬁbrancy
Condition 1.15. □

Proof of Proposition 4.32. For a recent reference of part (a) in the context of sym-
metric spectra, see [68]. Consider part (b). It is enough to treat the special case
where X, Y are furthermore ﬁbrant and coﬁbrant in the category of R-modules with
the ﬂat stable model structure. Let R′−→R be a coﬁbrant replacement in the cate-
gory of monoids in (SpΣ, ⊗S, S) with the ﬂat stable model structure [33, 70]. Since
the sphere spectrum S is ﬂat stable coﬁbrant in SpΣ, we know by Theorem 5.18(a)
that R′ is ﬂat stable coﬁbrant in the underlying category SpΣ, and it follows from
[31, 32] by arguing as in the proof of Theorem 3.26 that there are natural weak equiv-
alences X ∧ LY = X(⊗S)
L
RY ≃ X ′(⊗S)
L
R′ Y ′ ≃ | Bar
⊗S (X ′, R′, Y ′)| = |B|. Here,
X ′−→X and Y ′−→Y are functorial ﬂat stable coﬁbrant replacements in the cat-
egory of right (resp. left) R′-modules. Denote by B the indicated simplicial bar
construction with respect to ⊗S. We need to verify that |B| is (m+n+1)-connected.
We know by Theorem 5.18(b) that X ′, Y ′ are ﬂat stable coﬁbrant in the underlying
category SpΣ, hence it follows from part (a) that B is objectwise (m + n + 1)-
connected and Proposition 4.30 ﬁnishes the proof for part (b). Part (c) is veriﬁed
exactly as in the proof of part (b) above, except using the group algebra spectrum
R[Σt] instead of R. Part (d) follows easily from part (b) together with (2.5). Part
(e) follows easily from parts (d) and (c) together with (2.5). □

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 45

Proof of Proposition 4.38. It suﬃces to consider the case of simplicial left τ1O-
modules. Consider the map ∅−→B in sLtτ1O, and use functorial factorization in
sLtτ1O [32, 3.6] to obtain ∅−→Bc−→B, a coﬁbration followed by an acyclic ﬁbration.
By Proposition 4.18 and [32, 5.6], there is a retract of the form

|ikO ◦τ1O Bc|

(∗)
  
 // |O ◦τ1O Bc|

(∗∗)
  
 // |ikO ◦τ1O Bc|

(∗)
  
ikO ◦τ1O colim
Ltτ1 O
∆op Bc // O ◦τ1O colim
Ltτ1 O
∆op Bc // ikO ◦τ1O colim
Ltτ1 O
∆op Bc

in SymSeq. Since Bc is coﬁbrant in sLtτ1O, the proof of [32, 3.15] implies that
O ◦τ1O Bc is coﬁbrant in sLtO. It follows therefore from [32, 5.24] that (∗∗) is a
weak equivalence, hence (∗) is also a weak equivalence. We know from [32, 3.12]
that Bc is objectwise coﬁbrant in Ltτ1O, hence there are natural weak equivalences
ikO ◦τ1O Bc ≃ ikO ◦h
τ1O Bc ≃ ikO ◦h
τ1O B. It follows that there are natural weak
equivalences

ikO ◦h
τ1O hocolim
Ltτ1O
∆op B ≃ ikO ◦h
τ1O hocolim
Ltτ1 O
∆op Bc ≃ ikO ◦h
τ1O colim
Ltτ1O
∆op Bc

≃ ikO ◦τ1O colim
Ltτ1O
∆op Bc ≃ |ikO ◦τ1O Bc| ≃ hocolim
LtO
∆op ikO ◦τ1O Bc

≃ hocolim
LtO
∆op ikO ◦h
τ1O Bc ≃ hocolim
LtO
∆op ikO ◦h
τ1O B

which ﬁnishes the proof; here we have used 7.26. □

Proof of Proposition 4.40. Consider part (a) and the case of R-modules. The map
f factors functorially in ModR with the ﬂat stable model structure as X g
−→ Y h
−→
Z a coﬁbration followed by an acyclic ﬁbration, and hence the map f ∧t fac-

tors as X ∧t g∧t
−−→ Y ∧t h∧t
−−→ Z ∧t. Since smashing with a ﬂat stable coﬁbrant R-
module preserves weak equivalences, h∧t is a weak equivalence, and hence it is
enough to check that g∧t is n-connected. We argue by induction on t. Using
the pushout diagrams in Deﬁnition 5.9 (see, for instance, [31, 4.15]) together with
the natural isomorphisms Y ∧t/Qt
t−1 ∼= (Y /X)
∧t, it follows that each of the maps
X ∧t−→Qt
1−→Qt
2−→ · · · −→Qt
t−1−→Y ∧t is at least n-connected, which ﬁnishes the
proof for the case of R-modules. The case of symmetric sequences is similar. Con-
sider part (b). This follows by proceeding as in the proof of part (a), except using
the positive ﬂat stable model structure, together with part (a) and Propositions
7.17, 7.18, 7.35, and 4.32. □

Propositions 5.58, 5.59, and 5.60 will be needed for the proof of Proposition 4.46
below. The following homotopy spectral sequence for a simplicial unbounded chain
complex is well known; for a recent reference, see [75, 5.6].

Proposition 5.58. Let Y be a simplicial unbounded chain complex over K. There
is a natural homologically graded spectral sequence in the right-half plane such that

E2
p,q = Hp(Hq(Y )) =⇒ Hp+q(|Y |)

Here, Hq(Y ) denotes the simplicial K-module obtained by applying Hq levelwise to
Y , and K is any commutative ring.

Proposition 5.59. Let Y be a simplicial unbounded chain complex over Z. Let
m ∈ Z. Assume that Y is levelwise m-connected.

46 JOHN E. HARPER AND KATHRYN HESS

(a) If HkYn is ﬁnite for every k, n, then Hk|Y | is ﬁnite for every k.
(b) If HkYn is a ﬁnitely generated abelian group for every k, n, then Hk|Y | is
a ﬁnitely generated abelian group for every k.

Proof. This follows from Proposition 5.58. □

Recall the following Eilenberg-Moore type spectral sequences; for a recent refer-
ence, see [75, 5.7].

Proposition 5.60. Let t ≥ 1. Let A, B be unbounded chain complexes over K
with a right (resp. left) Σt-action. There is a natural homologically graded spectral
sequence in the right-half plane such that

E2
p,q = Tor
K[Σt]
p,q (H∗A, H∗B) =⇒ Hp+q(A⊗L
Σt B).

Here, K is any commutative ring, (ChK, ⊗, K) denotes the closed symmetric monoidal
category of unbounded chain complexes over K, K[Σt] is the group algebra, and ⊗
L
Σt
is the total left derived functor of ⊗Σt .

Proof of Proposition 4.46. Consider part (a). It is enough to treat the special
case where M, N are furthermore coﬁbrant in the category of right (resp. left)
A-modules. Let A′−→A be a coﬁbrant replacement in the category of monoids
in (ChZ, ⊗, Z) with the model structure of [70]. Since Z is coﬁbrant in ChZ, we
know by Theorem 5.18(a) that A′ is coﬁbrant in the underlying category ChZ,
and it follows easily by arguing as in the proof of Theorem 3.26 that there are
natural weak equivalences M ⊗
L
AN ≃ M ′⊗L
A′N ′ ≃ | Bar
⊗(M ′, A′, N ′)| = |B|. Here,
M ′−→M and N ′−→N are functorial coﬁbrant replacements in the category of right
(resp. left) A′-modules. Denote by B the indicated simplicial bar construction with
respect to ⊗. We need to verify that Hk(|B|) is ﬁnite for every k. We know by
Theorem 5.18(b) that M ′, N ′ are coﬁbrant in the underlying category ChZ, hence
it follows from Proposition 5.60 (with t = 1) that Hk(Bn) is ﬁnite for every k and
n, and Proposition 5.59 ﬁnishes the proof for part (a). Part (b) is similar. □

6. Homotopical analysis of the simplicial bar constructions

The purpose of this section is to prove Theorem 4.19 together with several closely
related technical results on simplicial structures and the simplicial bar construc-
tions. The results established here lie at the heart of the proofs of the main theorems
in this paper.

6.1. Simplicial structure on AlgO and LtO. The purpose of this subsection
is to describe the simplicial structure on AlgO (resp. LtO) and to prove several
related results. The key technical results of this subsection are Proposition 6.11 and
Theorem 6.18. They are used in the proof of Theorem 4.19 to construct skeletal
ﬁltrations in AlgO′ (resp. LtO′ ) of realizations (Deﬁnition 4.2) of the simplicial bar
constructions (Proposition 4.10).
Consider symmetric sequences in R-modules, and let O ∈ SymSeq, X in ModR
(resp. SymSeq), and K ∈ S. Deﬁne ν to be the natural map

O ◦ (X) ∧ K+ ν
−−→ O ◦ (X ∧ K+) (resp. (O ◦ X) ∧ K+ ν
−−→ O ◦ (X ∧ K+)
)

in ModR (resp. SymSeq) induced by the natural maps K−→K ×t in S for t ≥ 0;
these are the diagonal maps for t ≥ 1 and the constant map for t = 0. Here, S
denotes the category of simplicial sets. The construction of the tensor product below

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 47

is motivated by [18, VII.2.10]. Simplicial structures in the context of symmetric
spectra have also been exploited in [37, 68]; see also [2, 55].

Deﬁnition 6.2. Let O be an operad in R-modules, X an O-algebra (resp. left
O-module), and K a simplicial set. Deﬁne the tensor product X ˙⊗K in AlgO (resp.
LtO) by the reﬂexive coequalizer

X ˙⊗K := colim
( O ◦ (X ∧ K+) O ◦ (O ◦ (X) ∧ K+)

d1
oo d0oo )
(6.3)
 (resp. X ˙⊗K := colim
( O ◦ (X ∧ K+) O ◦ ((O ◦ X) ∧ K+)

d1
oo d0oo ))
(6.4)

in AlgO (resp. LtO), with d0 induced by operad multiplication m : O ◦ O−→O and
the map ν, while d1 is induced by the left O-action map m : O ◦ (X)−→X (resp.
m : O ◦ X−→X).

Let O be an operad in R-modules, consider X, Y in ModR (resp. SymSeq), K ∈ S,
and recall the isomorphisms

homModR (X ∧ K+, Y ) ∼= homModR(X, Map(K+, Y ))(6.5) (
resp. homSymSeq(X ∧ K+, Y ) ∼= homSymSeq(X, Map(K+, Y ))
)
(6.6)

natural in X, K, Y . Here, we are using the useful shorthand notation Map(K+, −)
to denote Map(R⊗G0K+, −); see, just above 4.2. If Y is an O-algebra (resp. left
O-module), then Map(K+, Y ) has an O-algebra (resp. left O-module) structure
induced by m : O ◦ (Y )−→Y (resp. m : O ◦ Y −→Y ). The next proposition is a
formal argument left to the reader. We will use it below in several proofs.

Proposition 6.7. Let O be an operad in R-modules. Let X ∈ SymSeq, Y ∈ LtO,
and K ∈ S. If f : X ∧ K+−→Y is a map in SymSeq, then the diagram

(O ◦ X) ∧ K+

ν   
 id◦f ∧ id// (
O ◦ Map(K+, Y )
) ∧ K+ ν // O ◦ (
Map(K+, Y ) ∧ K+)

id◦ev
  
O ◦ (X ∧ K+) id◦f // O ◦ Y

in SymSeq commutes. Here, ev denotes the evaluation map, and we have used the
same notation for both f and its adjoint (6.6).

The following proposition will be useful.

Proposition 6.8. Let O be an operad in R-modules. Let X, Y be O-algebras (resp.
left O-modules) and K a simplicial set. There are isomorphisms

homAlgO(X ˙⊗K, Y ) ∼= homAlgO (X, Map(K+, Y ))
(
resp. homLtO(X ˙⊗K, Y ) ∼= homLtO (X, Map(K+, Y ))
)

natural in X, K, Y .

Proof. It suﬃces to consider the case of left O-modules. We need to verify that spec-
ifying a map X ˙⊗K−→Y in LtO is the same as specifying a map X−→ Map(K+, Y )

48 JOHN E. HARPER AND KATHRYN HESS

in LtO, and that the resulting correspondence is natural. Suppose f : X ˙⊗K−→Y
is a map of left O-modules, and consider the corresponding commutative diagram

X ˙⊗K

f   
 O ◦ (X ∧ K+)

  

oo
 f

xxqqqqqqqqqqqq O ◦ (
(O ◦ X) ∧ K+)

  

d1
oo d0oo

Y O ◦ Y
moo O ◦ O ◦ Y
id◦m
oo m◦idoo

(6.9)

in LtO with rows reﬂexive coequalizer diagrams. Using the same notation for both
f : O ◦ (X ∧ K+)−→Y in LtO and its adjoints f : X ∧ K+−→Y in SymSeq (2.20)
and f : X−→Map(K+, Y ) in SymSeq (6.6), it follows easily from (6.9) and Propo-
sition 6.7 that the diagram

(O ◦ X) ∧ K+

id◦f ∧ id   
 m ∧ id // X ∧ K+ f ∧ id // Map(K+, Y ) ∧ K+

ev

  

(
O ◦ Map(K+, Y )
) ∧ K+

ν   
O ◦ (
Map(K+, Y ) ∧ K+) id◦ev // O ◦ Y m // Y

in SymSeq commutes, which implies that f : X−→Map(K+, Y ) is a map of left
O-modules. Conversely, suppose f : X−→Map(K+, Y ) is a map of left O-modules,
and consider the corresponding map f : X ∧ K+−→Y in SymSeq. We need to verify
that the adjoint map f : O ◦ (X ∧ K+)−→Y in LtO induces a map f : X ˙⊗K−→Y
in LtO. Applying O ◦ − to the commutative diagram in Proposition 6.7, it follows
that f d0 = f d1, which ﬁnishes the proof. □

Deﬁnition 6.10. Let O be an operad in R-modules. The realization functors
| − |AlgO : sAlgO−→AlgO and | − |LtO : sLtO−→LtO for simplicial O-algebras and sim-
plicial left O-modules are deﬁned objectwise by the coends

X ↦−→ |X|AlgO := X ˙⊗∆∆[−]+ , X ↦−→ |X|LtO := X ˙⊗∆∆[−]+ .

Recall that the realization functors |−| in Deﬁnition 4.2 are the left adjoints in the
adjunctions (4.4) with right adjoints the functors Map(∆[−]+, −). The following
proposition is closely related to [18, VII.3.3]; see also [2, A].

Proposition 6.11. Let O be an operad in R-modules and X a simplicial O-algebra
(resp. simplicial left O-module). The realization functors ﬁt into adjunctions

sAlgO
 |−|AlgO// AlgO,oo sLtO
 |−|LtO // LtO,oo(6.12)
 sAlgO
 |−| // AlgO,oo sLtO
 |−| // LtO,oo(6.13)

with left adjoints on top and right adjoints the functors Map(∆[−]+, −). In partic-
ular, there are isomorphisms |X| ∼= |X|AlgO in AlgO (resp. |X| ∼= |X|LtO in LtO),
natural in X.

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 49

Proof. It suﬃces to consider the case of left O-modules. Let X be a simplicial left
O-module. Verifying (6.12) follows easily from 6.8 and the universal property of
coends. Consider (6.13). Suppose f : |X|−→Y is a map of left O-modules, and
consider the corresponding left-hand commutative diagram

O ◦ |X| ∼= |O ◦ X|

id◦f   
 |m| // |X|

f
  
O ◦ Y m // Y
 O ◦ X

(∗)   
 m // X

f
  
Map(∆[−]+, O ◦ Y ) (id,m)// Map(∆[−]+, Y )

in SymSeq. Using the same notation for both f : |X|−→Y in SymSeq and its
adjoint f : X−→Map(∆[−]+, Y ) in sSymSeq (4.4), we know by (4.4) that the left-
hand diagram commutes if and only if its corresponding right-hand diagram in
sSymSeq commutes. Since the map (∗) factors in sSymSeq as O ◦ X id◦f
−−−→ O ◦
Map(∆[−]+, Y )−→ Map(∆[−]+, O ◦ Y ), the proof is complete. □

Proposition 6.14. Let O be an operad in R-modules. Let X, Y be O-algebras (resp.
left O-modules) and K, L simplicial sets. Then
(a) the functor X ˙⊗− : S−→AlgO (resp. X ˙⊗− : S−→LtO) commutes with all
colimits and there are natural isomorphisms X ˙⊗ ∗ ∼= X,
(b) there are isomorphisms X ˙⊗(K × L) ∼= (X ˙⊗K) ˙⊗L, natural in X, K, L.

Proof. It suﬃces to consider the case of left O-modules. Part (a) follows easily from
(6.4) and (2.20). Part (b) follows easily from the Yoneda lemma by verifying there
are natural isomorphisms homLtO(
(X ˙⊗K) ˙⊗L, Y ) ∼= homLtO (
X ˙⊗(K × L), Y )
; this
involves several applications of Proposition 6.8, together with the observation that
the natural isomorphism Map(K+, Map(L+, Y )) ∼= Map(K+ ∧ L+, Y ) in SymSeq
respects the left O-module structures. □

Deﬁnition 6.15. Let O be an operad in R-modules. Let X, Y be O-algebras (resp.
left O-modules). The mapping space Hom(X, Y ) ∈ S is deﬁned objectwise by

Hom(X, Y )n := homAlgO(X ˙⊗∆[n], Y ) (
resp. Hom(X, Y )n := homLtO (X ˙⊗∆[n], Y )
)
.

Proposition 6.16. Let O be an operad in R-modules. Then the category of O-
algebras and the category of left O-modules are simplicial categories (in the sense
of [27, II.2.1]), where the mapping space functor is that of Deﬁnition 6.15.

Proof. This follows from Propositions 6.8 and 6.14, together with [27, II.2.4]. □

Proposition 6.17. Let O be an operad in R-modules. Consider AlgO (resp. LtO)
with the model structure of Theorem 7.15 or 7.16.
(a) If j : K−→L is a coﬁbration in S, and p : X−→Y is a ﬁbration in AlgO
(resp. LtO), then Map(L+, X) //Map(K+, X) ×Map(K+,Y ) Map(L+, Y )
is a ﬁbration in AlgO (resp. LtO) that is an acyclic ﬁbration if either j or
p is a weak equivalence.
(b) If j : A−→B is a coﬁbration in AlgO (resp. LtO), and p : X−→Y is a
ﬁbration in AlgO (resp. LtO), then the pullback corner map is a ﬁbra-
tion Hom(B, X) // Hom(A, X) ×Hom(A,Y ) Hom(B, Y ) in S that is an
acyclic ﬁbration if either j or p is a weak equivalence.

50 JOHN E. HARPER AND KATHRYN HESS

Proof. Consider the case of left O-modules with the positive ﬂat stable model struc-
ture. Part (a) follows from the proof of Proposition 6.21, and part (b) follows from
part (a) together with [27, II.3.13]. The case of O-algebras with the positive ﬂat
stable model structure is similar. Consider the case of O-algebras or left O-modules
with the positive stable model structure. This follows by exactly the same argument
as above together with the fact that R⊗G0(−)+ applied to a coﬁbration in S gives
a coﬁbration in ModR with the stable model structure (Section 7 and [68]). □

The following theorem states that the simplicial structure respects the model
category structure; this has also been observed in the context of symmetric spectra
in [37, 68]; see also [2, 18, 55].

Theorem 6.18. Let O be an operad in R-modules. Consider AlgO (resp. LtO) with
the model structure of Theorem 7.15 or 7.16. Then AlgO (resp. LtO) is a simplicial
model category with the mapping space functor of Deﬁnition 6.15.

Proof. This follows from Propositions 6.16 and 6.17, together with [27, II.3.13]. □

6.19. Homotopical analysis of the simplicial bar constructions. The pur-
pose of this subsection is to prove Theorem 4.19. This will require that we establish
certain homotopical properties of the tensor product (Proposition 6.21) and circle
product (Theorem 6.22 and Proposition 6.23) constructions arising in the descrip-
tion of the degenerate subobjects (Proposition 6.25).

Proposition 6.20. Consider symmetric sequences in R-modules. Let A, B be sym-
metric sequences.

(a) f : X−→Y is a ﬂat stable coﬁbration in ModR and X0 ∼=
−−→ Y0 is an iso-
morphism if and only if f is a positive ﬂat stable coﬁbration in ModR.
(b) f : X−→Y is a ﬂat stable coﬁbration in SymSeq and X[r]0 ∼=
−−→ Y [r]0 is
an isomorphism for each r ≥ 0, if and only if f is a positive ﬂat stable
coﬁbration in SymSeq.
(c) If X, Y ∈ ModR, then there is a natural isomorphism (X ∧ Y )0 ∼= X0 ∧ R0Y0.
(d) If X, Y ∈ ModR and Y0 = ∗, then (X ∧ Y )0 = ∗.
(e) If B[r]0 = ∗ for each r ≥ 0, then (A ˇ⊗B)[r]0 = ∗ for each r ≥ 0.
(f) If A[0]0 = ∗ = B[r]0 for each r ≥ 0, then (A ◦ B)[r]0 = ∗ for each r ≥ 0.
(g) If A[r]0 = ∗ for each r ≥ 0, then (A ◦ B)[r]0 = ∗ for each r ≥ 0.

Proof. Parts (a) and (b) follow from 7.34. The remaining parts are an easy exercise
left to the reader. □

Proposition 6.21. Consider symmetric sequences in R-modules, and consider
SymSeq with the positive ﬂat stable model structure.
(a) If i : K−→L is a ﬂat stable coﬁbration in SymSeq, and j : A−→B is a
coﬁbration in SymSeq, then L ˇ⊗A ∐K ˇ⊗A K ˇ⊗B //L ˇ⊗B is a coﬁbration
in SymSeq that is an acyclic coﬁbration if either i or j is a weak equivalence.
(b) If j : A−→B is a ﬂat stable coﬁbration in SymSeq, and p : X−→Y is a ﬁbra-
tion in SymSeq, then Map ˇ⊗(B, X) // Map ˇ⊗(A, X) ×Map ˇ⊗(A,Y ) Map ˇ⊗(B, Y )
is a ﬁbration in SymSeq that is an acyclic ﬁbration if either j or p is a weak
equivalence.
(c) If j : A−→B is a coﬁbration in SymSeq, and p : X−→Y is a ﬁbration in
SymSeq, then Map ˇ⊗(B, X) //Map ˇ⊗(A, X) ×Map ˇ⊗(A,Y ) Map ˇ⊗(B, Y ) is

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 51

a ﬂat stable ﬁbration in SymSeq that is a ﬂat stable acyclic ﬁbration if
either j or p is a weak equivalence.

Proof. Consider part (a). Suppose i : K−→L is a ﬂat stable coﬁbration in SymSeq
and j : A−→B is a coﬁbration in SymSeq. The pushout corner map is a ﬂat stable
coﬁbration in SymSeq by [33, 6.1], hence by Proposition 6.20 it suﬃces to ver-
ify the pushout corner map (L ˇ⊗A)[r]0 ∐
(K ˇ⊗A)[r]0(K ˇ⊗B)[r]0 //(L ˇ⊗B)[r]0 is an
isomorphism for each r ≥ 0. We can therefore conclude by (2.5) together with
Proposition 6.20. The other cases are similar. Parts (b) and (c) follow from part
(a) and the natural isomorphisms (2.10). □

Theorem 6.22. Consider symmetric sequences in R-modules, and consider SymSeq
with the positive ﬂat stable model structure.

(a) If i : K−→L is a map in SymSeq such that K[r]−→L[r] is a ﬂat stable
coﬁbration in ModR for each r ≥ 1, and j : A−→B is a coﬁbration between
coﬁbrant objects in SymSeq, then L ◦ A ∐
K◦A K ◦ B //L ◦ B is a coﬁ-
bration in SymSeq that is an acyclic coﬁbration if either i or j is a weak
equivalence.
(b) If i : K−→L is a map in SymSeq such that K[r]−→L[r] is a ﬂat stable
coﬁbration in ModR for each r ≥ 0, K[0]0 ∼=
−−→ L[0]0 is an isomorphism,
and B is a coﬁbrant object in SymSeq, then the map K ◦ B−→L ◦ B is a
coﬁbration in SymSeq that is an acyclic coﬁbration if i is a weak equivalence.

Proof. Consider part (a). Suppose K[t]−→L[t] is a ﬂat stable coﬁbration in ModR
for each t ≥ 1, and j : A−→B is a coﬁbration between coﬁbrant objects in SymSeq.
We want to verify each L[t] ∧ Σt A ˇ⊗t ∐K[t] ∧ Σt A ˇ⊗t K[t] ∧ Σt B ˇ⊗t //L[t] ∧ Σt B ˇ⊗t

is a coﬁbration in SymSeq. If t = 0, this map is an isomorphism. Let t ≥ 1.
Consider any acyclic ﬁbration p : X−→Y in SymSeq. We want to show that the
pushout corner map has the left lifting property with respect to p. Consider any
such lifting problem; we want to verify that the corresponding solid commutative
diagram
 A ˇ⊗t

  
 // Map(L[t], X)

(∗)
  
B ˇ⊗t //
 44

Map(K[t], X) ×Map(K[t],Y ) Map(L[t], Y )

in SymSeqΣt has a lift. We know that the left-hand vertical map is a coﬁbration
in SymSeqΣt by Proposition 7.17, hence it suﬃces to verify that the map (∗)[r]
is a positive ﬂat stable acyclic ﬁbration in ModR for each r ≥ 0. By considering
symmetric sequences concentrated at 0, Proposition 6.21 ﬁnishes the argument for
this case. The other cases are similar. Consider part (b). Suppose K[t]−→L[t] is a
ﬂat stable coﬁbration in ModR for each t ≥ 0, K[0]0 ∼=
−−→ L[0]0 is an isomorphism,
and B is a coﬁbrant object in SymSeq. We need to check that each induced map
K[t] ∧ Σt B ˇ⊗t−→L[t] ∧ Σt B ˇ⊗t is a coﬁbration in SymSeq. The proof of part (a)
implies this for t ≥ 1, and Proposition 6.20 implies this for t = 0. The other case
is similar. □

52 JOHN E. HARPER AND KATHRYN HESS

Proposition 6.23. Let O be an operad in R-modules such that O[0] = ∗, and
let η : I−→O be its unit map. Assume that I[r]−→O[r] is a ﬂat stable coﬁbration
between ﬂat stable coﬁbrant objects in ModR for each r ≥ 0.

(a) If i : K−→L is a map in SymSeq such that K[r]−→L[r] is a ﬂat sta-
ble coﬁbration in ModR for each r ≥ 1, then the pushout corner map(
L ◦ I ∐K◦I K ◦ O)
[r] // (L ◦ O)[r] is a ﬂat stable coﬁbration in ModR
for each r ≥ 0.
(b) If t ≥ 1, then the induced map (I ˇ⊗t)[r]−→(O ˇ⊗t)[r] is a ﬂat stable coﬁbration
in ModRΣt for each r ≥ 0.

Proof. Consider part (b). The induced map is an isomorphism for 0 ≤ r ≤ t − 1
and the case for r ≥ t follows from Proposition 7.34 by arguing as in the proof of
Proposition 7.17. Consider part (a). We need to verify that each

L[t] ∧ Σt (I ˇ⊗t)[r] ∐K[t] ∧ Σt (I ˇ⊗t)[r] K[t] ∧ Σt (O ˇ⊗t)[r] // L[t] ∧ Σt (O ˇ⊗t)[r]

is a ﬂat stable coﬁbration in ModR. If t = 0, this map is an isomorphism. Let
t ≥ 1, and let p : X−→Y be a ﬂat stable acyclic ﬁbration in ModR. We need to
show that the pushout corner map has the left lifting property with respect to p.
Consider any such lifting problem; we want to verify that the corresponding solid
commutative diagram

(I ˇ⊗t)[r]

  
 // Map(L[t], X)

(∗)
  
(O ˇ⊗t)[r] //
 44

Map(K[t], X) ×Map(K[t],Y ) Map(L[t], Y )

in ModRΣt has a lift. The left-hand vertical map is a ﬂat stable coﬁbration in
ModRΣt by part (b), hence it suﬃces to verify the map (∗) is a ﬂat stable acyclic
ﬁbration in ModR. By assumption, each K[t]−→L[t] is a ﬂat stable coﬁbration in
ModR, which ﬁnishes the proof. □

Deﬁnition 6.24. Let O be an operad in R-modules, t ≥ 1 and n ≥ 0.

• Cubet is the category with objects the vertices (v1, . . . , vt) ∈ {0, 1}t of the
unit t-cube. There is at most one morphism between any two objects, and
there is a morphism (v1, . . . , vt)−→(v′
1, . . . , v′
t) if and only if vi ≤ v′
i for each
1 ≤ i ≤ t. In particular, Cubet is the category associated to a partial order
on the set {0, 1}t.
• The punctured cube pCubet is the full subcategory of Cubet with all objects
except the terminal object (1, . . . , 1) of Cubet.
• Deﬁne the functor w : pCubet−→SymSeq objectwise by

w(v1, . . . , vt) := c1 ◦ · · · ◦ ct with ci := { I, for vi = 0,
O, for vi = 1,

and with morphisms induced by the unit map η : I−→O.
• If X is an object in sModR or sSymSeq, denote by DXn ⊂ Xn the degenerate
subobject [32, 9.12] of Xn.

The following proposition gives a useful construction of degenerate subobjects.

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 53

Proposition 6.25. Let O be an operad in R-modules, Y an O-algebra (resp. left O-
module) and N a right O-module. Let t ≥ 1 and n ≥ 0. Deﬁne X := Bar(N, O, Y )
and Qt := colimpCubet (N ◦ w), and consider the induced maps η∗ : Q0 := ∗−→N
and η∗ : Qt−→N ◦ O◦t.

(a) The inclusion map DXn−→Xn is isomorphic to the map Qn ◦ (Y ) η∗◦(id)
−−−−→

N ◦ O◦n ◦ (Y ) (resp. Qn ◦ Y η∗◦id
−−−→ N ◦ O◦n ◦ Y ).
(b) The induced map η∗ : Qn+1−→N ◦ O◦(n+1) is isomorphic to the pushout
corner map (N ◦O◦n◦I)∐(Qn◦I)(Qn◦O)−→N ◦O◦(n+1) induced by η : I−→O
and η∗ : Qn−→N ◦ O◦n.

Proof. It suﬃces to consider the case of left O-modules. Consider part (a). It
follows easily from [32, 9.23], together with the fact that − ◦ Y : SymSeq−→SymSeq
commutes with colimits (2.9), that there are natural isomorphisms

DX0 = ∗, DX1 ∼= N ◦ I ◦ Y,

DX2 ∼= (N ◦ O ◦ I ◦ Y ) ∐(N ◦I◦I◦Y ) (N ◦ I ◦ O ◦ Y )
∼= (
(N ◦ O ◦ I) ∐(N ◦I◦I) (N ◦ I ◦ O)
) ◦ Y, . . . ,

DXt ∼= colimpCubet (N ◦ w ◦ Y ) ∼= (
colimpCubet (N ◦ w)
) ◦ Y

in SymSeq. Consider part (b). Since − ◦ B : SymSeq−→SymSeq commutes with
colimits for each B ∈ SymSeq, it follows easily that the colimit Qn+1 may be
computed inductively using pushout corner maps. □

Theorem 6.26. Let O be an operad in R-modules such that O[0] = ∗, Y an O-
algebra (resp. left O-module) and N a right O-module, and consider the unit map
η : I−→O. Assume that I[r]−→O[r] is a ﬂat stable coﬁbration between ﬂat stable
coﬁbrant objects in ModR for each r ≥ 0 and that N [r] is ﬂat stable coﬁbrant in
ModR for each r ≥ 0. Let X := Bar(N, O, Y ). If Y is positive ﬂat stable coﬁbrant
in ModR (resp. SymSeq) and N [0]0 = ∗, then the inclusion maps

∗−→DXn−→Xn, ∗−→| Bar(N, O, Y )|,

are positive ﬂat stable coﬁbrations in ModR (resp. SymSeq) for each n ≥ 0. In
particular, the simplicial bar construction Bar(N, O, Y ) is Reedy coﬁbrant in sModR
(resp. sSymSeq) with respect to the positive ﬂat stable model structure.

Proof. It suﬃces to consider the case of left O-modules. Consider Proposition 6.25;
let’s verify that the left-hand induced maps

∗−→Qn[r]−→(N ◦ O◦n)[r], Qn[0]0 = ∗ = (N ◦ O◦n)[0]0(6.27)

are ﬂat stable coﬁbrations in ModR for each n, r ≥ 0 and that the right-hand rela-
tions are satisﬁed for each n ≥ 0. It is easy to check this for n = 0, and by induction
on n, the general case follows from Propositions 6.23 and 6.25. By assumption, Y
is positive ﬂat stable coﬁbrant in SymSeq, hence by Proposition 6.25 and Theorem
6.22, the inclusion maps ∗−→DXn−→Xn are positive ﬂat stable coﬁbrations in
SymSeq for each n ≥ 0. Since DXn and Xn are positive ﬂat stable coﬁbrant in
SymSeq for each n ≥ 0, we know by 7.34 that the relations DXn[r]0 = ∗ = Xn[r]0
are satisﬁed for each n, r ≥ 0. It then follows easily from the skeletal ﬁltration
of realization [32, 9.11, 9.16], together with Proposition 6.20, that | Bar(N, O, Y )|
is positive ﬂat stable coﬁbrant in SymSeq. It is easy to check that the natural
map DXn−→Xn is isomorphic to the natural map LnX−→Xn described in [27,

54 JOHN E. HARPER AND KATHRYN HESS

VII.1.8]. Hence, in particular, we have veriﬁed that X is Reedy coﬁbrant [27,
VII.2.1] in sSymSeq. □

Proposition 6.28. Let O be an operad in R-modules, Y an O-algebra (resp. left
O-module) and N a right O-module. Consider SymSeq with the ﬂat stable model
structure. Assume that the unit map I−→O is a coﬁbration between coﬁbrant objects
in SymSeq and that N is coﬁbrant in SymSeq. If Y is ﬂat stable coﬁbrant in
ModR (resp. SymSeq), then | Bar(N, O, Y )| is ﬂat stable coﬁbrant in ModR (resp.
SymSeq).

Proof. Argue as in the proof of Theorem 6.26. □

Proof of Theorem 4.19. It suﬃces to consider the case of left O-modules. Consider
part (a). This follows as in the proof of Theorem 6.26, except using the skeletal
ﬁltration in [27, VII.3.8], Proposition 6.25 and Theorem 6.22, together with the fact
that O′ ◦ − : SymSeq−→LtO′ is a left Quillen functor and hence preserves both col-
imiting cones and coﬁbrations. Part (b) follows immediately from part (a) together
with Proposition 6.11, Theorem 6.18, and [27, VII.3.4]. □

7. Model structures

The purpose of this section is to prove Theorems 7.15, 7.16, and 7.21, together
with Theorems 7.25, 7.26, and 7.27 which improve the main results in [31, 32]
from operads in symmetric spectra to the more general context of operads in R-
modules. Our approach to this generalization, which is motivated by Hornbostel
[37], is to establish only the necessary minimum of technical propositions for R-
modules needed for the proofs of the main results as described in [31, 32] to remain
valid in the more general context of R-modules.

7.1. Smash products and R-modules. Denote by (SpΣ, ⊗S, S) the closed sym-
metric monoidal category of symmetric spectra [39, 68]. To keep this section as
concise as possible, from now on we will freely use the notation from [31, Section
2] which agrees (whenever possible) with [39].
The following is proved in [39, 2.1] and states that tensor product in the category
S
Σ inherits many of the good properties of smash product in the category S∗.

Proposition 7.2. (S
Σ, ⊗, S0) has the structure of a closed symmetric monoidal
category. All small limits and colimits exist and are calculated objectwise. The unit
S0 ∈ S
Σ is given by S0[n] = ∗ for each n ≥ 1 and S0[0] = S0.

There are two naturally occurring maps S⊗S−→S and S0−→S in S
Σ that give
S the structure of a commutative monoid in (S
Σ, ⊗, S0). Furthermore, for any sym-
metric spectrum X, there is a naturally occurring map m : S⊗X−→X endowing
X with a left action of S in (S
Σ, ⊗, S0). The following is proved in [39, 2.2] and
provides a useful interpretation of symmetric spectra.

Proposition 7.3. Deﬁne the category Σ′ := ∐n≥0Σn, a skeleton of Σ.
(a) The sphere spectrum S is a commutative monoid in (S
Σ, ⊗, S0).
(b) The category of symmetric spectra is equivalent to the category of left S-
modules in (S
Σ, ⊗, S0).
(c) The category of symmetric spectra is isomorphic to the category of left S-
modules in (S
Σ
′
∗ , ⊗, S0).

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 55

In this paper we will not distinguish between these equivalent descriptions of
symmetric spectra.

Deﬁnition 7.4. Let R be a commutative monoid in (SpΣ, ⊗S, S) (Basic Assump-
tion 1.2). A left R-module is an object in (SpΣ, ⊗S, S) with a left action of R and
a morphism of left R-modules is a map in SpΣ that respects the left R-module
structure. Denote by ModR the category of left R-modules and their morphisms.

The smash product X ∧ Y ∈ ModR of left R-modules X and Y is deﬁned by

X ∧ Y := colim
( X⊗SY X⊗SR⊗SY
m⊗idoo
 id⊗m
oo ) ∼= colim
( X⊗Y X⊗R⊗Y
m⊗idoo
 id⊗m
oo )

the indicated colimit. Here, m denotes the indicated R-action map and since R
is a commutative monoid in (SpΣ, ⊗S, S), a left action of R on X determines a
right action m : X⊗SR−→X, which gives X the structure of an (R, R)-bimodule.
Hence the smash product X ∧ Y of left R-modules, which is naturally isomorphic
to X⊗RY , has the structure of a left R-module.

Remark 7.5. Since R is commutative, we usually drop the adjective “left” and
simply refer to the objects of ModR as R-modules.

The following is an easy consequence of [39, 2.2].

Proposition 7.6. (ModR, ∧ , R) has the structure of a closed symmetric monoidal
category. All small limits and colimits exist and are calculated objectwise.

7.7. Model structures on R-modules. The material below intentionally paral-
lels [31, Section 4], except that we work in the more general context of R-modules
instead of symmetric spectra. We need to recall just enough notation so that we can
describe and work with the (positive) ﬂat stable model structure on R-modules, and
the corresponding projective model structures on the diagram categories SymSeq
and SymSeqG of R-modules, for G a ﬁnite group. The functors involved in such a
description are easy to understand when deﬁned as the left adjoints of appropriate
functors, which is how they naturally arise in this context.
For each m ≥ 0 and subgroup H ⊂ Σm, denote by l : H−→Σm the inclusion of
groups and deﬁne the evaluation functor evm : S
Σ−→S
Σm
∗ objectwise by evm(X) :=

Xm. There are adjunctions S∗ //S
H
limH
oo Σm·H −//S
Σm
∗
l∗
oo // S
Σevm
oo with left adjoints on top.

Deﬁne G
H
m : S∗−→S
Σ to be the composition of the three top functors, and deﬁne
limH evm : S
Σ−→S∗ to be the composition of the three bottom functors; we have
dropped the restriction functor l∗ from the notation. It is easy to check that if
K ∈ S∗, then G
H
m(K) is the object in S
Σ that is concentrated at m with value
Σm ·H K. Consider the forgetful functors SpΣ−→S
Σ and ModR−→SpΣ. It follows
from Proposition 7.3 that there are adjunctions

S
Σ
 S⊗− //
 SpΣoo R⊗S −// ModRoo , S
Σ
 R⊗− // ModRoo ,(7.8)

with left adjoints on top; the latter adjunction is the composition of the former ad-
junctions. For each p ≥ 0, deﬁne the evaluation functor Evp : SymSeq−→ModR ob-
jectwise by Evp(A) := A[p], and for each ﬁnite group G, consider the forgetful func-

tor SymSeqG−→SymSeq. There are adjunctions ModR
 Gp // SymSeq
Evp
oo G·− // SymSeqGoo

56 JOHN E. HARPER AND KATHRYN HESS

with left adjoints on top. It is easy to check that if X ∈ ModR, then Gp(X) is the
symmetric sequence concentrated at p with value X · Σp. Putting it all together,
there are adjunctions

S∗
 GH
m // S
Σ
limH evm
oo R⊗− // ModRoo Gp // SymSeq
Evp
oo G·− // SymSeqGoo(7.9)

with left adjoints on top. We are now in a good position to describe several use-
ful model structures. It is proved in [71] that the following two model category
structures exist on R-modules.

Deﬁnition 7.10.
(a) The ﬂat stable model structure on ModR has weak equivalences the stable
equivalences, coﬁbrations the retracts of (possibly transﬁnite) compositions
of pushouts of maps

R⊗G
H
m∂∆[k]+−→R⊗G
H
m∆[k]+ (m ≥ 0, k ≥ 0, H ⊂ Σm subgroup),

and ﬁbrations the maps with the right lifting property with respect to the
acyclic coﬁbrations.
(b) The positive ﬂat stable model structure on ModR has weak equivalences
the stable equivalences, coﬁbrations the retracts of (possibly transﬁnite)
compositions of pushouts of maps

R⊗G
H
m∂∆[k]+−→R⊗G
H
m∆[k]+ (m ≥ 1, k ≥ 0, H ⊂ Σm subgroup),

and ﬁbrations the maps with the right lifting property with respect to the
acyclic coﬁbrations.

Remark 7.11. In the sets of maps above, it is important to note that H varies over
all subgroups of Σm. For ease of notation purposes, we have followed Schwede [68]
in using the term ﬂat (e.g., ﬂat stable model structure) for what is called R (e.g.,
stable R-model structure) in [39, 66, 71].

Several useful properties of the ﬂat stable model structure are summarized in
the following two propositions, which are consequences of [39, 5.3, 5.4] as indicated
below; see also [68]. These properties are used in several sections of this paper.

Proposition 7.12. Consider ModR with the ﬂat stable model structure. If Z ∈
ModR is coﬁbrant, then the functor − ∧ Z : ModR−→ModR preserves (i) weak equiv-
alences and (ii) monomorphisms.

Proposition 7.13. If B ∈ ModR and X−→Y is a ﬂat stable coﬁbration in ModR,
then B ∧ X−→B ∧ Y in ModR is a monomorphism.

Proof of Proposition 7.12. Part (i) is the R-module analog of [39, 5.3.10]. It can
also be veriﬁed as a consequence of [39, 5.3.10] by arguing exactly as in the proof
of [31, 4.29(b)]. Part (ii) follows from the R-module analog of [39, 5.3.7]; see, [39,
proof of 5.4.4] or [68]. □

Proof of Proposition 7.13. This follows from the R-module analog of [39, 5.3.7]; see,
[39, proof of 5.4.4] or [68]. □

The stable model structure on ModR is deﬁned by ﬁxing H in Deﬁnition 7.10(a)
to be the trivial subgroup. This is one of several model category structures that is
proved in [39] to exist on R-modules. The positive stable model structure on ModR

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 57

is deﬁned by ﬁxing H in Deﬁnition 7.10(b) to be the trivial subgroup. This model
category structure is proved in [53] to exist on R-modules. It follows immediately
that every (positive) stable coﬁbration is a (positive) ﬂat stable coﬁbration.
These model structures on R-modules enjoy several good properties, including
that smash products of R-modules mesh nicely with each of the model structures
deﬁned above. More precisely, each model structure above is coﬁbrantly generated,
by generating coﬁbrations and acyclic coﬁbrations with small domains, and with
respect to each model structure (ModR, ∧ , R) is a monoidal model category.
If G is a ﬁnite group, it is easy to check that the diagram categories ModRG,
SymSeq and SymSeqG inherit corresponding projective model category structures,
where the weak equivalences (resp. ﬁbrations) are the maps that are underlying
objectwise weak equivalences (resp. objectwise ﬁbrations). We refer to these model
structures by the names above (e.g., the positive ﬂat stable model structure on
SymSeqG). Each of these model structures is coﬁbrantly generated by generating
coﬁbrations and acyclic coﬁbrations with small domains. Furthermore, with respect
to each model structure (SymSeq, ⊗, 1) is a monoidal model category; this is proved
in [33].

7.14. Model structures on O-algebras and left O-modules. The purpose of
this subsection is to prove the following two theorems. These generalizations are
motivated by Hornbostel [37] and improve the corresponding results in [31, 1.1, 1.3]
from operads in symmetric spectra to the more general context involving operads in
R-modules and play a key role in this paper. An important ﬁrst step in establishing
these theorems was provided by the characterization given by Schwede [68] of ﬂat
stable coﬁbrations in ModR in terms of objects with an R0-action; see Proposition
7.34 below for the needed generalization of this.

Theorem 7.15 (Positive ﬂat stable model structure on AlgO and LtO). Let O be
an operad in R-modules. Then the category of O-algebras (resp. left O-modules)
has a model category structure with weak equivalences the stable equivalences (resp.
objectwise stable equivalences) and ﬁbrations the maps that are positive ﬂat stable
ﬁbrations (resp. objectwise positive ﬂat stable ﬁbrations) in the underlying category
of R-modules (Deﬁnition 7.10(b)).

Theorem 7.16 (Positive stable model structure on AlgO and LtO). Let O be an
operad in R-modules. Then the category of O-algebras (resp. left O-modules) has
a model category structure with weak equivalences the stable equivalences (resp.
objectwise stable equivalences) and ﬁbrations the maps that are positive stable ﬁ-
brations (resp. objectwise positive stable ﬁbrations) in the underlying category of
R-modules (Deﬁnition 7.10(b) and below Proposition 7.13).

We defer the proof of the following two propositions to Subsection 7.28.

Proposition 7.17. Let B ∈ ModRΣ
op
t (resp. B ∈ SymSeqΣ
op
t ) and t ≥ 1. If
i : X−→Y is a coﬁbration between coﬁbrant objects in ModR (resp. SymSeq) with
the positive ﬂat stable model structure, then
(a) X ∧t−→Y ∧t (resp. X ˇ⊗t−→Y ˇ⊗t) is a coﬁbration between coﬁbrant objects
in ModRΣt (resp. SymSeqΣt ) with the positive ﬂat stable model structure,
which is a weak equivalence if i is a weak equivalence,
(b) the map B ∧ Σt Qt
t−1−→B ∧ Σt Y ∧t (resp. B ˇ⊗Σt Qt
t−1−→B ˇ⊗Σt Y ˇ⊗t) is a
monomorphism.

58 JOHN E. HARPER AND KATHRYN HESS

Proposition 7.18. Let G be a ﬁnite group and consider ModR, ModRG, ModRGop,
SymSeq, SymSeqG, and SymSeqGop, each with the ﬂat stable model structure.

(a) If B ∈ ModRGop (resp. B ∈ SymSeqGop), then the functor

B ∧ G− : ModRG−→ModR (
resp. B ˇ⊗G− : SymSeqG−→SymSeq)

preserves weak equivalences between coﬁbrant objects, and hence its total
left derived functor exists.
(b) If Z ∈ ModRG (resp. Z ∈ SymSeqG) is coﬁbrant, then the functor

− ∧ GZ : ModRGop−→ModR (
resp. − ˇ⊗GZ : SymSeqGop−→SymSeq)

preserves weak equivalences.

Proposition 7.19. Let O be an operad in R-modules, A ∈ AlgO (resp. A ∈ LtO),
and i : X−→Y a generating acyclic coﬁbration in ModR (resp. SymSeq) with the
positive ﬂat stable model structure. Consider any pushout diagram in AlgO (resp.
LtO) of the form (5.11). Then j is a monomorphism and a weak equivalence in
ModR (resp. SymSeq).

Proof. It suﬃces to consider the case of left O-modules. This is veriﬁed exactly as
in [31, proof of 4.4], except using (ModR, ∧ , R) and Propositions 7.17, 7.18 instead
of (SpΣ, ⊗S, S) and [31, 4.28, 4.29], respectively. □

Proof of Theorem 7.15. Consider SymSeq and ModR, both with the positive ﬂat
stable model structure. We will prove that the model structure on LtO (resp. AlgO)
is created by the middle (resp. left-hand) free-forgetful adjunction in (2.20).
Deﬁne a map f in LtO to be a weak equivalence (resp. ﬁbration) if U (f ) is a weak
equivalence (resp. ﬁbration) in SymSeq. Similarly, deﬁne a map f in AlgO to be a
weak equivalence (resp. ﬁbration) if U (f ) is a weak equivalence (resp. ﬁbration)
in ModR. Deﬁne a map f in LtO (resp. AlgO) to be a coﬁbration if it has the left
lifting property with respect to all acyclic ﬁbrations in LtO (resp. AlgO).
Consider the case of LtO. We want to verify the model category axioms (MC1)-
(MC5) in [17]. Arguing exactly as in [31, proof of 1.1], this reduces to the veriﬁcation
of Proposition 7.19. By construction, the model category is coﬁbrantly generated.
Argue similarly for the case of AlgO by considering left O-modules concentrated at
0. □

Proof of Theorem 7.16. Consider SymSeq and ModR, both with the positive stable
model structure. We will prove that the model structure on LtO (resp. AlgO) is
created by the middle (resp. left-hand) free-forgetful adjunction in (2.20).
Deﬁne a map f in LtO to be a weak equivalence (resp. ﬁbration) if U (f ) is a weak
equivalence (resp. ﬁbration) in SymSeq. Similarly, deﬁne a map f in AlgO to be a
weak equivalence (resp. ﬁbration) if U (f ) is a weak equivalence (resp. ﬁbration)
in ModR. Deﬁne a map f in LtO (resp. AlgO) to be a coﬁbration if it has the left
lifting property with respect to all acyclic ﬁbrations in LtO (resp. AlgO).
The model category axioms are veriﬁed exactly as in the proof of Theorem 7.15;
this reduces to the veriﬁcation of Proposition 7.19. □

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 59

7.20. Relations between homotopy categories. The purpose of this subsection
is to prove the following theorem. This generalization improves the corresponding
result in [31, 1.4] from operads in symmetric spectra to the more general context
involving operads in R-modules. It plays a key role in this paper.

Theorem 7.21 (Comparing homotopy categories). Let O be an operad in R-
modules and let AlgO (resp. LtO) be the category of O-algebras (resp. left O-
modules) with the model structure of Theorem 7.15 or 7.16. If f : O−→O′ is a map
of operads, then the adjunctions f∗ : AlgO //AlgO′ : f ∗oo and f∗ : LtO // LtO′ : f ∗oo
are Quillen adjunctions with left adjoints on top and f ∗ the forgetful functor. If
furthermore, f is an objectwise stable equivalence, then the adjunctions are Quillen
equivalences, and hence induce equivalences on the homotopy categories.

First we make the following observation.

Proposition 7.22. Consider ModR and SymSeq with the positive ﬂat stable model
structure. If W ∈ ModR (resp. W ∈ SymSeq) is coﬁbrant, then the functor
− ◦ (W ) : SymSeq−→ModR (resp. − ◦ W : SymSeq−→SymSeq) preserves weak equiv-
alences.

Proof. It suﬃces to consider the case of symmetric sequences. This is veriﬁed
exactly as in [31, proof of 5.3], except using (ModR, ∧ , R) and Propositions 7.17,
7.18 instead of (SpΣ, ⊗S, S) and [31, 4.28, 4.29], respectively. □

Proposition 7.23. Let f : O−→O′ be a map of operads in R-modules and consider
AlgO (resp. LtO) with the positive ﬂat stable model structure. If Z ∈ AlgO (resp.
Z ∈ LtO) is coﬁbrant and f is a weak equivalence in the underlying category SymSeq
with the positive ﬂat stable model structure, then the natural map Z−→f ∗f∗Z is a
weak equivalence in AlgO (resp. LtO).

Proof. It suﬃces to consider the case of left O-modules. This is veriﬁed exactly as
in [31, proof of 5.2], except using (ModR, ∧ , R) and Propositions 7.17, 7.18, 7.22
instead of (SpΣ, ⊗S, S) and [31, 4.28, 4.29, 5.3], respectively. □

Proof of Theorem 7.21. This is veriﬁed exactly as in [31, proof of 1.4], except using
(ModR, ∧ , R) and Proposition 7.23 instead of (SpΣ, ⊗S, S) and [31, 5.2], respec-
tively. □

7.24. Homotopy colimits and simplicial bar constructions. The following
theorems play a key role in this paper. They improve the corresponding results
in [32] from operads in symmetric spectra to the more general context involving
operads in R-modules, and are veriﬁed exactly as in the proof of [32, 1.10, 1.6, 1.8],
respectively.

Theorem 7.25. Let f : O−→O′ be a morphism of operads in R-modules. Let X be
an O-algebra (resp. left O-module) and consider AlgO (resp. LtO) with the model
structure of Theorem 7.15 or 7.16. If the simplicial bar construction Bar(O, O, X) is
objectwise coﬁbrant in AlgO (resp. LtO), then there is a zigzag of weak equivalences
Lf∗(X) ≃ | Bar(O′, O, X)| in the underlying category, natural in such X. Here, Lf∗
is the total left derived functor of f∗.

60 JOHN E. HARPER AND KATHRYN HESS

Theorem 7.26. Let O be an operad in R-modules. If X is a simplicial O-algebra
(resp. simplicial left O-module), then there are zigzags of weak equivalences

U hocolim
AlgO
∆op X ≃ |U X| ≃ hocolim∆op U X
(resp. U hocolim
LtO
∆op X ≃ |U X| ≃ hocolim∆op U X)

natural in X. Here, U is the forgetful functor, sAlgO (resp. sLtO) is equipped with
the projective model structure inherited from the model structure of Theorem 7.15
or 7.16.

Theorem 7.27. Let O be an operad in R-modules. If X is an O-algebra (resp. left
O-module), then there is a zigzag of weak equivalences in AlgO (resp. LtO)

X ≃ hocolim
AlgO
∆op Bar(O, O, X) (resp. X ≃ hocolim
LtO
∆op Bar(O, O, X)
)

natural in X. Here, sAlgO (resp. sLtO) is equipped with the projective model struc-
ture inherited from the model structure of Theorem 7.15 or 7.16.

7.28. Flat stable coﬁbrations. The purpose of this subsection is to prove Propo-
sitions 7.17 and 7.18. This requires several calculations (7.33 and 7.36) together
with a characterization of ﬂat stable coﬁbrations (Proposition 7.34). This charac-
terization is motivated by the characterization given in Schwede [68], in terms of
left R0–modules, of ﬂat stable coﬁbrations in ModR.
Since R is a commutative monoid in (SpΣ, ⊗S, S), it follows that R0 is a com-
mutative monoid in (S∗, ∧ , S0). In particular, by [33, 2.4] we can regard R0 as a
commutative monoid in (S
Σn
∗ , ∧ , S0) with the trivial Σn-action.

Deﬁnition 7.29. Let n ≥ 0. A left R0-module is an object in (S
Σn
∗ , ∧ , S0) with a
left action of R0 and a morphism of left R0-modules is a map in S
Σn
∗ that respects
the left R0-module structure. Denote by R0 − S
Σn
∗ the category of left R0-modules
and their morphisms.

For each n ≥ 0, there is an adjunction S
Σn
∗
 R0 ∧ −// R0 − S
Σn
∗oo with left adjoint on
top. It is proved in [71] that the following model category structure exists on left
Σn-objects in pointed simplicial sets.

Deﬁnition 7.30. Let n ≥ 0.
• The mixed Σn-equivariant model structure on S
Σn
∗ has weak equivalences
the underlying weak equivalences of simplicial sets, coﬁbrations the retracts
of (possibly transﬁnite) compositions of pushouts of maps

Σn/H · ∂∆[k]+−→Σn/H · ∆[k]+ (k ≥ 0, H ⊂ Σn subgroup),

and ﬁbrations the maps with the right lifting property with respect to the
acyclic coﬁbrations.

Furthermore, it is proved in [71] that this model structure is coﬁbrantly generated
by generating coﬁbrations and acyclic coﬁbrations with small domains, and that the
coﬁbrations are the monomorphisms. It is easy to prove that the category R0 − S
Σn
∗
inherits a corresponding model structure created by the free-forgetful adjunction
above Deﬁnition 7.30, and that furthermore the diagram category of (Σop
r × G)-
shaped diagrams in R0 − S
Σn
∗ appearing in the following proposition inherits a
corresponding projective model structure. This proposition, whose proof is left to
the reader, will be needed for identifying ﬂat stable coﬁbrations in SymSeqG.

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 61

Proposition 7.31. Let G be a ﬁnite group and consider any n, r ≥ 0. The diagram
category (
R0 − S
Σn
∗ )Σ
op
r ×G inherits a corresponding model structure from the mixed
Σn-equivariant model structure on S
Σn
∗ . The weak equivalences (resp. ﬁbrations)
are the underlying weak equivalences (resp. ﬁbrations) in S
Σn
∗ .

Deﬁnition 7.32. Deﬁne R ∈ ModR such that Rn := Rn for n ≥ 1 and R0 := ∗.
The structure maps are the naturally occurring ones such that there exists a map
of R-modules i : R−→R satisfying in = id for each n ≥ 1.

The following calculation, which follows easily from [31, 2.9], will be needed for
characterizing ﬂat stable coﬁbrations in SymSeqG.

Calculation 7.33. Let G be a ﬁnite group. Let m, p ≥ 0, H ⊂ Σm a subgroup,
and K a pointed simplicial set. Recall from (7.9) the functors Gp and G
H
m. Deﬁne
X := G · Gp(R⊗G
H
mK) ∈ SymSeqG. Here, X is obtained by applying the indicated
functors in (7.9) to K. Then for r = p we have

(R ∧ X[r])n ∼= { G · (
Σn ·Σn−m×Σm Rn−m ∧ (Σm/H · K)
) · Σp for n > m,
∗ for n ≤ m,

X[r]n ∼=
 



 G · (
Σn ·Σn−m×Σm Rn−m ∧ (Σm/H · K)
) · Σp for n > m,
G · (
R0 ∧ (Σm/H · K)
) · Σp for n = m,
∗ for n < m,

and for r ̸= p we have X[r] = ∗ = R ∧ X[r].

The following characterization of ﬂat stable coﬁbrations in SymSeqG is motivated
by the characterization given in Schwede [68] of ﬂat stable coﬁbrations in ModR.
It improves the corresponding characterization given in [31, 6.6] from the context
of (SpΣ, ⊗S, S) to the more general context of (ModR, ∧ , R).

Proposition 7.34. Let G be a ﬁnite group.
(a) A map f : X−→Y in SymSeqG with the ﬂat stable model structure is a
coﬁbration if and only if the induced maps

X[r]0−→Y [r]0, r ≥ 0, n = 0,

(R ∧ Y [r])n ∐(R ∧ X[r])n X[r]n−→Y [r]n, r ≥ 0, n ≥ 1,

are coﬁbrations in (
R0 − S
Σn
∗ )Σ
op
r ×G with the model structure in 7.31.
(b) A map f : X−→Y in SymSeqG with the positive ﬂat stable model structure
is a coﬁbration if and only if the maps X[r]0−→Y [r]0, r ≥ 0, are isomor-
phisms, and the induced maps

(R ∧ Y [r])n ∐(R ∧ X[r])n X[r]n−→Y [r]n, r ≥ 0, n ≥ 1,

are coﬁbrations in (
R0 − S
Σn
∗ )Σ
op
r ×G with the model structure in 7.31.

Proof. This is veriﬁed exactly as in [31, proof of 6.6], except using (ModR, ∧ , R),
Proposition 7.31 and Calculation 7.33 instead of (SpΣ, ⊗S, S), [31, 6.3] and [31,
6.5], respectively. □

Proof of Proposition 7.18. It suﬃces to consider the case of symmetric sequences.
Consider part (b). This is veriﬁed exactly as in [31, proof of 4.29(b)], except using
(ModR, ∧ , R) and the map g∗ obtained by applying the indicated functors in (7.9),

62 JOHN E. HARPER AND KATHRYN HESS

instead of (SpΣ, ⊗S, S) and the map g∗ obtained by applying the indicated functors
in [31, (4.1)], respectively. Consider part (a). This is veriﬁed exactly as in [31,
proof of 4.29(a)], except using (ModR, ∧ , R) instead of (SpΣ, ⊗S, S). □

Proposition 7.35. Let G be a ﬁnite group. If B ∈ ModRGop (resp. B ∈ SymSeqGop ),
then the functor B ∧ G− : ModRG−→ModR (resp. B ˇ⊗G− : SymSeqG−→SymSeq)
sends coﬁbrations in ModRG (resp. SymSeqG) with the ﬂat stable model structure
to monomorphisms.

Proof. It suﬃces to consider the case of symmetric sequences. This is veriﬁed
exactly as in [31, proof of 6.11], except using (ModR, ∧ , R) and the map g∗ obtained
by applying the indicated functors in (7.9), instead of (SpΣ, ⊗S, S) and the map g∗
obtained by applying the indicated functors in [31, (4.1)], respectively. □

The following calculation, which follows easily from [31, 2.9] and (2.5), will be
needed in the proof of Proposition 7.17 below.

Calculation 7.36. Let k, m, p ≥ 0, H ⊂ Σm a subgroup, and t ≥ 1. Let the map
g : ∂∆[k]+−→∆[k]+ be a generating coﬁbration for S∗ and deﬁne X−→Y in SymSeq
to be the induced map g∗ : Gp(R⊗G
H
m∂∆[k]+) //Gp(R⊗G
H
m∆[k]+) . Here, the
map g∗ is obtained by applying the indicated functors in (7.9) to the map g. For
r = tp we have the calculation

(
(Y ˇ⊗t)[r])
n ∼=
 



 Σn ·Σn−tm×H×t Rn−tm ∧ (∆[k]×t)+ · Σtp for n > tm,
Σtm ·H×t R0 ∧ (∆[k]×t)+ · Σtp for n = tm,
∗ for n < tm,
(
R ∧ (Y ˇ⊗t)[r])
n ∼= { Σn ·Σn−tm×H×t Rn−tm ∧ (∆[k]×t)+ · Σtp for n > tm,
∗ for n ≤ tm,

(
Qt
t−1[r])

n ∼=
 



 Σn ·Σn−tm×H×t Rn−tm ∧ ∂(∆[k]×t)+ · Σtp for n > tm,
Σtm ·H×t R0 ∧ ∂(∆[k]×t)+ · Σtp for n = tm,
∗ for n < tm,
(
R ∧ Qt
t−1[r])

n ∼= { Σn ·Σn−tm×H×t Rn−tm ∧ ∂(∆[k]×t)+ · Σtp for n > tm,
∗ for n ≤ tm,

and for r ̸= tp we have (Y ˇ⊗t)[r] = ∗ = R ∧ (Y ˇ⊗t)[r] and Qt
t−1[r] = ∗ = R ∧ Qt
t−1[r].

Proof of Proposition 7.17. It suﬃces to consider the case of symmetric sequences.
Consider part (a). This is veriﬁed exactly as in [31, proof of 4.28(a)], except using
(ModR, ∧ , R), the map g∗ obtained by applying the indicated functors in (7.9),
Proposition 7.34, and Calculation 7.36 instead of (SpΣ, ⊗S, S) the map g∗ obtained
by applying the indicated functors in [31, (4.1)], [31, 6.6 and 6.15], respectively.
The acyclic coﬁbration assertion follows immediately from [33, 7.19]. Consider part
(b). This is veriﬁed exactly as in [31, proof of 4.28(b)], except using (ModR, ∧ , R)
and Proposition 7.35 instead of (SpΣ, ⊗S, S) and [31, 6.11], respectively. □

The following will be needed in other sections of this paper.

Proposition 7.37. Let t ≥ 1. If i : X−→Y is a generating coﬁbration in ModR
(resp. SymSeq) with the positive ﬂat stable model structure, then Qt
t−1−→Y ∧t (resp.
Qt
t−1−→Y ˇ⊗t) is a coﬁbration between coﬁbrant objects in ModRΣt (resp. SymSeqΣt )
with the positive ﬂat stable model structure.

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 63

Proof. It suﬃces to consider the case of symmetric sequences. This follows imme-
diately from the proof of Proposition 7.17. □

8. Operads in chain complexes over a commutative ring

The purpose of this section is to observe that the main results of this paper
remain true in the context of unbounded chain complexes over a commutative
ring, provided that the desired model category structures exist on algebras (resp.
left modules) over operads O and τkO. Since the constructions and proofs of the
theorems are essentially identical to the arguments above in the context of R-
modules, modulo the obvious changes, the arguments are left to the reader.

Basic Assumption 8.1. From now on in this section, we assume that K is any
commutative ring.

Denote by (ChK, ⊗, K) the closed symmetric monoidal category of unbounded
chain complexes over K [38, 49].

Homotopical Assumption 8.2. If O is an operad in ChK, assume that the fol-
lowing model structure exists on Alg ˜O (resp. Lt ˜O) for ˜O = O and ˜O = τkO for each
k ≥ 1: the model structure on Alg ˜O (resp. Lt ˜O) has weak equivalences the homology
isomorphisms (resp. objectwise homology isomorphisms) and ﬁbrations the maps
that are dimensionwise surjections (resp. objectwise dimensionwise surjections).

Coﬁbrancy Condition 8.3. If O is an operad in ChK, consider the unit map
η : I−→O of the operad O and assume that I[r]−→O[r] is a coﬁbration ([32, 3.1])
between coﬁbrant objects in ChΣ
op
r
K for each r ≥ 0.

If K is any ﬁeld of characteristic zero, then Homotopical Assumption 8.2 and
Coﬁbrancy Condition 8.3 are satisﬁed by every operad in ChK (see [33, 35]). In the
case of algebras over operads, if K is any commutative ring and O′ is any non-Σ
operad in ChK, then it is proved in [33, 35] that the corresponding operad O = O′ ·Σ
satisﬁes Homotopical Assumption 8.2.
The following is a commutative rings version of Deﬁnitions 3.13 and 3.15.

Deﬁnition 8.4. Let O be an operad in ChK such that O[0] = ∗. Assume that
O satisﬁes Homotopical Assumption 8.2. Let X be an O-algebra (resp. left O-
module). The homotopy completion X h∧ of X is the O-algebra (resp. left O-module)
deﬁned by X h∧ := holim
AlgO
k (
τkO ◦O (X c)
) (resp. X h∧ := holim
LtO
k (
τkO ◦O X c)
)
the homotopy limit of the completion tower of the functorial coﬁbrant replacement
X c of X in AlgO (resp. LtO). The Quillen homology complex (or Quillen homology
object) Q(X) of X is the O-algebra τ1O ◦h
O (X) (resp. left O-module τ1O ◦h
O X).

The following is a commutative rings version of Theorem 1.5.

Theorem 8.5. Let O be an operad in ChK such that O[0] is trivial. Assume that
O satisﬁes Homotopical Assumption 8.2 and Coﬁbrancy Condition 8.3. Let X be a
0-connected O-algebra (resp. left O-module) and assume that O is (−1)-connected
and HkO[r], U K are ﬁnitely generated abelian groups for every k, r.
(a) If the Quillen homology groups HkQ(X) (resp. HkQ(X)[r]) are ﬁnite for
every k, r, then the homology groups HkX (resp. HkX[r]) are ﬁnite for
every k, r.

64 JOHN E. HARPER AND KATHRYN HESS

(b) If the Quillen homology groups HkQ(X) (resp. HkQ(X)[r]) are ﬁnitely
generated abelian groups for every k, r, then the homology groups HkX
(resp. HkX[r]) are ﬁnitely generated abelian groups for every k, r.
Here, U denotes the forgetful functor from commutative rings to abelian groups.

The following is a commutative rings version of Theorem 1.8.

Theorem 8.6. Let O be an operad in ChK such that O[0] is trivial. Assume that
O satisﬁes Homotopical Assumption 8.2 and Coﬁbrancy Condition 8.3. Let X be
a 0-connected O-algebra (resp. left O-module), n ≥ 0, and assume that O is (−1)-
connected.
(a) The Quillen homology complex Q(X) is n-connected if and only if X is
n-connected.
(b) If the Quillen homology complex Q(X) is n-connected, then the natural
Hurewicz map HkX−→HkQ(X) is an isomorphism for k ≤ 2n + 1 and a
surjection for k = 2n + 2.

The following is a commutative rings version of Theorem 1.9.

Theorem 8.7. Let O be an operad in ChK such that O[0] is trivial. Assume
that O satisﬁes Homotopical Assumption 8.2 and Coﬁbrancy Condition 8.3. Let
f : X−→Y be a map of O-algebras (resp. left O-modules) and n ≥ 0. Assume that
O is (−1)-connected.
(a) If X, Y are 0-connected, then f is n-connected if and only if f induces an
n-connected map Q(X)−→Q(Y ) on Quillen homology complexes.
(b) If X, Y are (−1)-connected and f is (n − 1)-connected, then f induces an
(n − 1)-connected map Q(X)−→Q(Y ) on Quillen homology complexes.
(c) If f induces an n-connected map Q(X)−→Q(Y ) on Quillen homology com-
plexes between (−1)-connected objects, then f induces an (n − 1)-connected
map X h∧−→Y h∧ on homotopy completion.
(d) If the Quillen homology complex Q(X) is (n − 1)-connected, then homotopy
completion X h∧ is (n − 1)-connected.
Here, Q(X)−→Q(Y ), X h∧−→Y h∧ denote the natural induced zigzags in the cat-
egory of O-algebras (resp. left O-modules) with all backward facing maps weak
equivalences.

The following is a commutative rings version of Theorem 1.12.

Theorem 8.8. Let O be an operad in ChK such that O[0] is trivial. Assume
that O satisﬁes Homotopical Assumption 8.2 and Coﬁbrancy Condition 8.3. Let
f : X−→Y be a map of O-algebras (resp. left O-modules).
(a) If X is 0-connected and O is (−1)-connected, then the natural coaugmenta-
tion X ≃ X h∧ is a weak equivalence.
(b) If the Quillen homology complex Q(X) is 0-connected and O is (−1)-connected,
then the homotopy completion spectral sequence

E1
−s,t = Ht−s(is+1O ◦h
τ1O (Q(X)
)) =⇒ Ht−s(X h∧)

resp. E1
−s,t[r] = Ht−s((
is+1O ◦h
τ1O Q(X)
)
[r]) =⇒ Ht−s(
X h∧[r]), r ≥ 0,

converges strongly.

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 65

(c) If f induces a weak equivalence Q(X) ≃ Q(Y ) on Quillen homology com-
plexes, then f induces a weak equivalence X h∧ ≃ Y h∧ on homotopy com-
pletion.
 References

[1] M. Andr´e. Homologie des alg`ebres commutatives. Springer-Verlag, Berlin, 1974. Die
Grundlehren der mathematischen Wissenschaften, Band 206.
[2] G. Arone and M. Ching. Operads and chain rules for the calculus of functors. Ast´erisque,
(338):vi+158, 2011.
[3] G. Arone and M. Kankaanrinta. A functorial model for iterated Snaith splitting with ap-
plications to calculus of functors. In Stable and unstable homotopy (Toronto, ON, 1996),
volume 19 of Fields Inst. Commun., pages 1–30. Amer. Math. Soc., Providence, RI, 1998.
[4] A. Baker, H. Gilmour, and P. Reinhard. Topological Andr´e-Quillen homology for cellular
commutative S-algebras. Abh. Math. Semin. Univ. Hambg., 78(1):27–50, 2008.
[5] A. Baker and B. Richter, editors. Structured ring spectra, volume 315 of London Mathematical
Society Lecture Note Series. Cambridge University Press, Cambridge, 2004.
[6] M. Basterra. Andr´e-Quillen cohomology of commutative S-algebras. J. Pure Appl. Algebra,
144(2):111–143, 1999.
[7] M. Basterra and M. A. Mandell. Homology and cohomology of E∞ ring spectra. Math. Z.,
249(4):903–944, 2005.
[8] M. Basterra and M. A. Mandell. Homology of En ring spectra and iterated T HH. Algebr.
Geom. Topol., 11(2):939–981, 2011.
[9] A. K. Bousﬁeld and D. M. Kan. Homotopy limits, completions and localizations. Lecture
Notes in Mathematics, Vol. 304. Springer-Verlag, Berlin, 1972.
[10] G. Carlsson. Equivariant stable homotopy and Sullivan’s conjecture. Invent. Math.,
103(3):497–525, 1991.
[11] G. Carlsson. Derived completions in stable homotopy theory. J. Pure Appl. Algebra,
212(3):550–577, 2008.
[12] D. Chataur, J. L. Rodr´ıguez, and J. Scherer. Realizing operadic plus-constructions as nulli-
ﬁcations. K-Theory, 33(1):1–21, 2004.
[13] M. Ching. Bar-cobar duality for operads in stable homotopy theory. J. Topol., 5(1):39–80,
2012.
[14] D. Dugger and D. C. Isaksen. Topological hypercovers and A1-realizations. Math. Z.,
246(4):667–689, 2004.
[15] W. G. Dwyer. Strong convergence of the Eilenberg-Moore spectral sequence. Topology,
13:255–265, 1974.
[16] W. G. Dwyer, J. P. C. Greenlees, and S. Iyengar. Duality in algebra and topology. Adv.
Math., 200(2):357–402, 2006.
[17] W. G. Dwyer and J. Spali´nski. Homotopy theories and model categories. In Handbook of
algebraic topology, pages 73–126. North-Holland, Amsterdam, 1995.
[18] A. D. Elmendorf, I. Kriz, M. A. Mandell, and J. P. May. Rings, modules, and algebras
in stable homotopy theory, volume 47 of Mathematical Surveys and Monographs. American
Mathematical Society, Providence, RI, 1997. With an appendix by M. Cole.
[19] A. D. Elmendorf and M. A. Mandell. Rings, modules, and algebras in inﬁnite loop space
theory. Adv. Math., 205(1):163–228, 2006.
[20] B. Fresse. Lie theory of formal groups over an operad. J. Algebra, 202(2):455–511, 1998.
[21] B. Fresse. Koszul duality of operads and homology of partition posets. In Homotopy theory:
relations with algebraic geometry, group cohomology, and algebraic K-theory, volume 346 of
Contemp. Math., pages 115–215. Amer. Math. Soc., Providence, RI, 2004.
[22] B. Fresse. Modules over operads and functors, volume 1967 of Lecture Notes in Mathematics.
Springer-Verlag, Berlin, 2009.
[23] V. Ginzburg and M. Kapranov. Koszul duality for operads. Duke Math. J., 76(1):203–272,
1994.
[24] P. G. Goerss. On the Andr´e-Quillen cohomology of commutative F2-algebras. Ast´erisque,
(186):169, 1990.
[25] P. G. Goerss and M. J. Hopkins. Andr´e-Quillen (co)-homology for simplicial algebras over
simplicial operads. In Une d´egustation topologique [Topological morsels]: homotopy theory

66 JOHN E. HARPER AND KATHRYN HESS

in the Swiss Alps (Arolla, 1999), volume 265 of Contemp. Math., pages 41–85. Amer. Math.
Soc., Providence, RI, 2000.
[26] P. G. Goerss and M. J. Hopkins. Moduli spaces of commutative ring spectra. In Structured
ring spectra, volume 315 of London Math. Soc. Lecture Note Ser., pages 151–200. Cambridge
Univ. Press, Cambridge, 2004.
[27] P. G. Goerss and J. F. Jardine. Simplicial homotopy theory, volume 174 of Progress in
Mathematics. Birkh¨auser Verlag, Basel, 1999.
[28] P. G. Goerss and K. Schemmerhorn. Model categories and simplicial methods. In Interactions
between homotopy theory and algebra, volume 436 of Contemp. Math., pages 3–49. Amer.
Math. Soc., Providence, RI, 2007.
[29] T. G. Goodwillie. Calculus. II. Analytic functors. K-Theory, 5(4):295–332, 1991/92.
[30] T. G. Goodwillie. Calculus. III. Taylor series. Geom. Topol., 7:645–711 (electronic), 2003.
[31] J. E. Harper. Homotopy theory of modules over operads in symmetric spectra. Algebr. Geom.
Topol., 9(3):1637–1680, 2009.
[32] J. E. Harper. Bar constructions and Quillen homology of modules over operads. Algebr. Geom.
Topol., 10(1):87–136, 2010.
[33] J. E. Harper. Homotopy theory of modules over operads and non-Σ operads in monoidal
model categories. J. Pure Appl. Algebra, 214(8):1407–1434, 2010.
[34] K. Hess. A general framework for homotopic descent and codescent.
arXiv:1001.1556v3 [math.AT], 2010.
[35] V. Hinich. Homological algebra of homotopy algebras. Comm. Algebra, 25(10):3291–3323,
1997. Erratum: arXiv:math/0309453 [math.QA].
[36] P. S. Hirschhorn. Model categories and their localizations, volume 99 of Mathematical Surveys
and Monographs. American Mathematical Society, Providence, RI, 2003.
[37] J. Hornbostel. Preorientations of the derived motivic multiplicative group.
arXiv:1005.4546 [math.KT], 2011.
[38] M. Hovey. Model categories, volume 63 of Mathematical Surveys and Monographs. American
Mathematical Society, Providence, RI, 1999.
[39] M. Hovey, B. Shipley, and J. H. Smith. Symmetric spectra. J. Amer. Math. Soc., 13(1):149–
208, 2000.
[40] J. F. Jardine. Generalized ´etale cohomology theories, volume 146 of Progress in Mathematics.
Birkh¨auser Verlag, Basel, 1997.
[41] B. Johnson and R. McCarthy. Deriving calculus with cotriples. Trans. Amer. Math. Soc.,
356(2):757–803 (electronic), 2004.
[42] I. Kriz and J. P. May. Operads, algebras, modules and motives. Ast´erisque, (233):iv+145pp,
1995.
[43] N. J. Kuhn. Localization of Andr´e-Quillen-Goodwillie towers, and the periodic homology of
inﬁnite loopspaces. Adv. Math., 201(2):318–378, 2006.
[44] N. J. Kuhn. Goodwillie towers and chromatic homotopy: an overview. In Proceedings of the
Nishida Fest (Kinosaki 2003), volume 10 of Geom. Topol. Monogr., pages 245–279. Geom.
Topol. Publ., Coventry, 2007.
[45] T. Lawson. The plus-construction, Bousﬁeld localization, and derived completion. J. Pure
Appl. Algebra, 214(5):596–604, 2010.
[46] A. Lazarev. Cohomology theories for highly structured ring spectra. In Structured ring spectra,
volume 315 of London Math. Soc. Lecture Note Ser., pages 201–231. Cambridge Univ. Press,
Cambridge, 2004.
[47] M. Livernet. Homotopie rationnelle des alg`ebres sur une op´erade. PhD thesis, Universit´e
Louis Pasteur (Strasbourg I), 1998.
Available at http://www.math.univ-paris13.fr/~livernet/.
[48] M. Livernet. On a plus-construction for algebras over an operad. K-Theory, 18(4):317–337,
1999.
[49] S. Mac Lane. Homology. Classics in Mathematics. Springer-Verlag, Berlin, 1995. Reprint of
the 1975 edition.
[50] S. Mac Lane. Categories for the working mathematician, volume 5 of Graduate Texts in
Mathematics. Springer-Verlag, New York, second edition, 1998.
[51] M. A. Mandell. E∞ algebras and p-adic homotopy theory. Topology, 40(1):43–94, 2001.
[52] M. A. Mandell. Topological Andr´e-Quillen cohomology and E∞ Andr´e-Quillen cohomology.
Adv. Math., 177(2):227–279, 2003.

HOMOTOPY COMPLETION AND TOPOLOGICAL QUILLEN HOMOLOGY 67

[53] M. A. Mandell, J. P. May, S. Schwede, and B. Shipley. Model categories of diagram spectra.
Proc. London Math. Soc. (3), 82(2):441–512, 2001.
[54] R. McCarthy and V. Minasian. On triples, operads, and generalized homogeneous functors.
arXiv:math/0401346v1 [math.AT], 2004.
[55] J. E. McClure, R. Schw¨anzl, and R. Vogt. T HH(R) ∼= R ⊗ S1 for E∞ ring spectra. J. Pure
Appl. Algebra, 121(2):137–159, 1997.
[56] J. E. McClure and J. H. Smith. A solution of Deligne’s Hochschild cohomology conjecture. In
Recent progress in homotopy theory (Baltimore, MD, 2000), volume 293 of Contemp. Math.,
pages 153–193. Amer. Math. Soc., Providence, RI, 2002.
[57] H. R. Miller. The Sullivan conjecture on maps from classifying spaces. Ann. of Math. (2),
120(1):39–87, 1984. Correction: Ann. of Math. (2), 121(3):605-609, 1985.
[58] V. Minasian. Andr´e-Quillen spectral sequence for T HH. Topology Appl., 129(3):273–280,
2003.
[59] D. Quillen. Homotopical algebra. Lecture Notes in Mathematics, No. 43. Springer-Verlag,
Berlin, 1967.
[60] D. Quillen. On the (co-) homology of commutative rings. In Applications of Categorical
Algebra (Proc. Sympos. Pure Math., Vol. XVII, New York, 1968), pages 65–87. Amer. Math.
Soc., Providence, R.I., 1970.
[61] C. Rezk. Spaces of Algebra Structures and Cohomology of Operads. PhD thesis, MIT, 1996.
Available at http://www.math.uiuc.edu/~rezk/.
[62] B. Richter. An Atiyah-Hirzebruch spectral sequence for topological Andr´e-Quillen homology.
J. Pure Appl. Algebra, 171(1):59–66, 2002.
[63] J. Rognes. Galois extensions of structured ring spectra. Stably dualizable groups. Mem. Amer.
Math. Soc., 192(898):viii+137, 2008.
[64] J. Rognes. Topological logarithmic structures. In New topological contexts for Galois theory
and algebraic geometry (BIRS 2008), volume 16 of Geom. Topol. Monogr., pages 401–544.
Geom. Topol. Publ., Coventry, 2009.
[65] S. Schwede. Spectra in model categories and applications to the algebraic cotangent complex.
J. Pure Appl. Algebra, 120(1):77–104, 1997.
[66] S. Schwede. S-modules and symmetric spectra. Math. Ann., 319(3):517–532, 2001.
[67] S. Schwede. Stable homotopy of algebraic theories. Topology, 40(1):1–41, 2001.
[68] S. Schwede. An untitled book project about symmetric spectra. 2007,2009. Available at:
http://www.math.uni-bonn.de/people/schwede/.
[69] S. Schwede. On the homotopy groups of symmetric spectra. Geom. Topol., 12(3):1313–1344,
2008.
[70] S. Schwede and B. Shipley. Algebras and modules in monoidal model categories. Proc. London
Math. Soc. (3), 80(2):491–511, 2000.
[71] B. Shipley. A convenient model category for commutative ring spectra. In Homotopy theory:
relations with algebraic geometry, group cohomology, and algebraic K-theory, volume 346 of
Contemp. Math., pages 473–483. Amer. Math. Soc., Providence, RI, 2004.
[72] D. Sullivan. Geometric topology. Part I. Massachusetts Institute of Technology, Cambridge,
Mass., 1971. Localization, periodicity, and Galois symmetry, Revised version.
[73] D. Sullivan. Genetics of homotopy theory and the Adams conjecture. Ann. of Math. (2),
100:1–79, 1974.
[74] J. M. Turner. On simplicial commutative algebras with vanishing Andr´e-Quillen homology.
Invent. Math., 142(3):547–558, 2000.
[75] C. A. Weibel. An introduction to homological algebra, volume 38 of Cambridge Studies in
Advanced Mathematics. Cambridge University Press, Cambridge, 1994.

Department of Mathematics, University of Western Ontario, London, Ontario, N6A
5B7, Canada

MATHGEOM, ´Ecole Polytechnique F´ed´erale de Lausanne, CH-1015 Lausanne, Switzer-
land
E-mail address: john.edward.harper@gmail.com

MATHGEOM, ´Ecole Polytechnique F´ed´erale de Lausanne, CH-1015 Lausanne, Switzer-
land
E-mail address: kathryn.hess@epfl.ch
