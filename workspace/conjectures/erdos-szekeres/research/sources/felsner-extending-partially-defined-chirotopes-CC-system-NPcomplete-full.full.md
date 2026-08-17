<!-- source: https://export.arxiv.org/pdf/math/0504430v1.pdf | converted from PDF -->

arXiv:math/0504430v1  [math.CO]  21 Apr 2005NP-completeness of Partial Chirotope Extendibility

Patrick Baier

November 10, 2018

Abstract

In the monograph “Axioms and Hulls” (1992) [2] Donald Knuth
studies some axiomatizations of geometric situations. The structures
described by one of the axiom systems are called CC-systems. Knuth
proves that it is NP-complete to decide, whether a partially deﬁned
CC-system can be extended to a complete CC-system. The aim of this
note is to show that Knuth’s proof of this result also implies that it is
NP-complete to decide the extendability of partially deﬁned chirotopes.

Together with Stefan Felsner I’ve been interested in the question, whether
partially given signotopes are extendable (cf. [1] for signotopes). Through
a talk of Bernd G¨artner in Berlin we learned about a proof for the NP-
completeness of chirotope extendibility by Falk Tschirschnitz [3, 4]. Re-
marks of Ileana Streinu and Stefan Felsner brought my attention to an NP-
completeness proof of Knuth [2]. In fact, the work of Knuth implies that it
is NP-complete to decide the extendability of partially deﬁned chirotopes.
The aim of this note is to make the connections clear.
Knuth deﬁnes CC-systems as a boolean function of all ordered triples
of a given ﬁnite groundset (whose elements are usually referred to as points)
following ﬁve Axioms, where an expression of the form pqr means that the
value associated with (p, q, r) is true (p. 3-4)1:

Axiom 1: pqr =⇒ qrp (cyclic symmetry)
Axiom 2: pqr =⇒ ¬ prq (antisymmetry)
Axiom 3: pqr ∨ prq (nondegeneracy)
Axiom 4: tqr ∧ ptr ∧ pqt =⇒ pqr (interiority)
Axiom 5: tsp ∧ tsq ∧ tsr ∧ tpq ∧ tqr =⇒ tpr (transitivity)
Axiom 5’: tps ∧ tqs ∧ trs ∧ tpq ∧ tqr =⇒ tpr (dual transitivity)
(Each of these axioms is to be read with an implied quantiﬁcation “for all

1Page numbers always refer to Knuth’s monograph [2].

1

pairwise distinct points”). Axiom 5’ is a dual version of Axiom 5, Knuth
shows that they imply each other (p. 5).
A pre-CC-system is analogously deﬁned by Axioms 1, 2, 3 and 5
(p. 11). As to show the equivalence of Axioms 5 and 5’ we do only need
Axioms 1, 2 and 3 we can equally deﬁne pre-CC-systems by using Axiom
5’ instead of Axiom 5. Uniform chirotopes are deﬁned by Axioms 1, 2,
3 and the so-called Grassmann-Pl¨ucker-Relations (GPR) stating that
for pairwise distinct points t, p, q, r, s the set

{(tpq ∧ trs) ∨ (tqp ∧ tsr);

(trp ∧ tqs) ∨ (tpr ∧ tsq); (1)

(tps ∧ tqr) ∨ (tsp ∧ trq)}

contains both values true and false.
Given a pre-CC-system, for an arbitrary point t Knuth considers the as-
sociated tournament, which is a complete directed graph on all points except
for t deﬁned by the relation p → q iﬀ tpq (p. 7). A tournament is called
vortex-free iﬀ the graphs shown beneath are not contained as subgraphs
(p. 11-12). Knuth now gives the statement of the following

Lemma 1. A pre-CC-system is characterized by the fact that each associated
tournament is vortex-free.

Proof. This simply follows from the observation that the forbidden sub-
graphs correspond exactly with the structures excluded by Axioms 5 (left
picture) and 5’ (right picture), where the tournament associated with t is
to be considered, p, q, r correspond to the triangle points in clockwise order
and s corresponds to the point in the middle of the respective ﬁgure.2

At this point we can observe the following simple equivalence:

2According to the duality of Axioms 5 and 5’ it would in fact be enough to exclude one
of the pictured subgraphs. The existence of one forbidden structure implies the existence
of the other (in a tournament associated with a diﬀerent point). We explicitly exclude
both structures because it simpliﬁes the proof of the following lemma.

2

Lemma 2. The uniform chirotopes are exactly the pre-CC-systems.

Proof. Given Axioms 1, 2, 3 we have to show the equivalence of Axiom 5
(or equivalenty 5 and 5’) and the GPR:
First let Axiom 5 be violated. That means we have tsp ∧ tsq ∧ tsr ∧ tpq ∧
tqr ∧ trp for some ﬁve pairwise distinct points. One can easily check that
the GPR aren’t fulﬁlled (all three values in (1) become false).
For the other direction suppose the GPR are not fulﬁlled. Using Lemma 1
we want to show the existence of a forbidden subgraph. We have two con-
sider two main cases: (a) All three values of (1) are true. This happens if,
e. g. in either of the three expressions the left part of the ∨-expression is
true, i. e. tpq ∧trs∧trp∧tqs∧tps∧tqr. Regarding the tournament associated
with t, this gives us a subgraph of the form of the right picture, where p, q, r
are the triangle points in clockwise order and s is the middle point. Instead
of examining all eight cases, where all three values in the GPR become true,
we can observe that we can generate all these possibilities from the above
mentioned example by sequentially performing an operation, which consists
of inverting two disjoint arcs. Looking at the eﬀect of this operation on
the tournament associated with t, we observe that a forbidden subgraph is
always transformed in another forbidden subgraph. Thus starting with the
one special case examined above the existence of forbidden subgraphs in all
eight cases follows. (b) All three values of (1) are false. This is the case, if
e. g. tpq ∧ tsr ∧ trp ∧ tsq ∧ tsp ∧ tqr. As tournament associated with t we
now get the subgraph shown to the left, where again p, q, r are the triangle
points in clockwise order and s is the middle point. In the same way as in
part (a) we can avoid examining each of the eight conﬁgurations that can
occur in this case.

The NP-completeness proof for the extendibility of CC-systems consists
mainly of two steps (p. 19-23). In the ﬁrst step it is shown to be NP-
complete to decide, whether a directed graph can be extended to a vortex-
free tournament by reducing 3SAT (via some steps) to this problem (p. 19-
22). As a corollary (p. 22-23) NP-completeness for CC-systems is obtained
by using a construction yielding a CC-system (on n points) starting with an
arbitrary vortex-free tournament (on n − 1 points) such that this vortex-free
tournament is associated with the additional point. Thus, starting with a
set of deﬁned triples (obeying Axioms 1 and 2), all of which have a point t
in common, following the same rule as used for the deﬁnition of associated
tournaments (p → q iﬀ tpq) we obtain a directed graph on all points except
for t. This graph can be extended to a vortex-free tournament iﬀ the given

3

set of deﬁned triples can be extended to a CC-system. With these results of
Knuth it is very easy to show the following:

Theorem. The problem of deciding, whether a boolean function deﬁned on
a subset of the set of all triples of a given groundset can be extended to a
chirotope (or equivalently pre-CC-system), is NP-complete.

Proof. We use the reduction of Knuth. If the given 3SAT instance is not
satisﬁable, then there is no completion of the digraph to a vortex-free tour-
nament and, hence, no completion of the given triples to a pre-CC-system.
If, however, the given 3SAT instance is satisﬁable, then there is a com-
pletion to a vortex-free tournament. Following Knuth we can construct a
CC-system, this tournament being associated with one of its nodes. As ev-
ery CC-system is a pre-CC-system we have found an extension of the given
partial pre-CC-system.

References

[1] S. Felsner and H. Weil: Sweeps, Arrangements and Signotopes,
Discr. Appl. Math. 109 (2001), 67-94.

[2] D. E. Knuth: Axioms and Hulls, Lecture Notes Comput. Sci. 606,
Springer-Verlag, 1992.

[3] Falk Tschirschnitz: LP-related Properties of Polytopes with Few
Facets, PhD thesis, ETH Z¨urich, No. 15179, 2003,
http://e-collection.ethbib.ethz.ch/show?type=diss&nr=15179.

[4] Falk Tschirschnitz: Testing extendability for partial chirotopes is
np-complete., CCCG (2001), 165-168,
http://compgeo.math.uwaterloo.ca/∼cccg01/proceedings/long/
tschirsc-48015.ps.gz.
 4
