<!-- source: https://arxiv.org/pdf/math/0611322 | converted from PDF -->

arXiv:math/0611322v1  [math.DS]  10 Nov 2006
ON THE GENESIS OF SYMBOLIC DYNAMICS
AS WE KNOW IT

ETHAN M. COVEN AND ZBIGNIEW H. NITECKI

Abstract. We trace the beginning of symbolic dynamics—the study of the
shift dynamical system—as it arose from the use of coding to study recurrence
and transitivity of geodesics. It is our assertion that neither Hadamard’s 1898
paper, nor the Morse-Hedlund papers of 1938 and 1940, which are normally
cited as the ﬁrst instances of symbolic dynamics, truly present the abstract
point of view associated with the subject today. Based in part on the evidence
of a 1941 letter from Hedlund to Morse, we place the beginning of symbolic
dynamics in a paper published by Hedlund in 1944.

Symbolic dynamics, in the modern view [LM95, Kit98], is the dynamical study
of the shift automorphism on the space of bi-inﬁnite sequences of symbols, or its
restriction to closed invariant subsets. In this note, we attempt to trace the begin-
nings of this viewpoint. While various schemes for symbolic coding of geometric
and dynamic phenomena have been around at least since Hadamard (or Gauss: see
[KU05]), and the two papers by Morse and Hedlund entitled “Symbolic dynamics”
[MH38, MH40] are often cited as the beginnings of the subject, it is our view that
the speciﬁc, abstract version of symbolic dynamics familiar to us today really began
with a paper,“Sturmian minimal sets” [Hed44], published by Hedlund a few years
later. The outlines of the story are familiar, and involve the study of geodesic ﬂows
on surfaces, speciﬁcally their recurrence and transitivity properties; this note takes
as its focus a letter from Hedlund to Morse, written between their joint papers
and Hedlund’s, in which his intention to turn the subject into a part of topology is
explicit.
1 This letter is reproduced on page 6.
Our focus here is rather narrow, even when it comes to coding geodesic ﬂows.
A recent survey by Katok and Ugarcovici [KU05] distinguishes two approaches to
such coding: a geometric method, which is our subject, and a second, going back
to Gauss and associated with Artin, Koebe and Nielsen which can be regarded
as more arithmetic in nature. We do not propose to consider the latter in detail.
The survey [KU05] discusses technical details of both approaches as well as their
subsequent development in recent years.
The beginnings of symbolic dynamics are often traced back to Hadamard’s 1898
study of geodesics on surfaces of negative curvature [Had98]. In Part II of this work
(§20), Hadamard gives a coding for the (free homotopy classes of) closed geodesics,
essentially as words (up to cyclic permutation) in generators of the fundamental
group, and in Part III (§37) he shows that each word corresponds to a unique

2000 Mathematics Subject Classiﬁcation. Primary 37B10; Secondary 01A60.
Key words and phrases. Symbolic dynamics, shift automorphism, recurrence, transitivity, min-
imal set, geodesics.
1In the interest of full disclosure, we should indicate our possible bias: Hedlund was the ﬁrst
author’s dissertation director and hired the second author in his ﬁrst job.

1

2 ETHAN M. COVEN AND ZBIGNIEW H. NITECKI

closed geodesic. He then goes on to study unbounded geodesics and in Part VI
(§56) shows that the initial conditions at a point which determine geodesics staying
in a bounded region form a perfect, nowhere dense closed set (which is the closure
of the conditions yielding closed geodesics).
There are several respects in which Hadamard’s paper does not really qualify as a
beginning for symbolic dynamics. First, his coding is limited to ﬁnite words, coding
closed geodesics; he does not appear to envision a coding system encompassing
other geodesics. The bounded, non-periodic geodesics he produces in Part VI are,
in passing, seen as determined by a sequence of closed geodesics, but this is not
explicitly related to their coding. Furthermore, Part II of the paper (where the
coding is formulated), entitled “Consid´erations d’Analysis situs”, is presented as
follows: Ayant reconnu, dans les num´eros pr´ec´edents, l’existence de surfaces
`a courbures oppos´ees et `a connexion quelconque, nous avons `a rap-
peler les principes qui gouvernent l’´etude des lignes trac´ees sur de
telles surfaces: principes pos´es par M. Jordan dans un M´emoire
bien connu (2).
Footnote (2) (“Ce journal, an´ee 1866”) refers to the second of two back-to-back
papers published 33 years before Hadamard in the Journal de Math´ematiques Pures
et Appliqu´es by Jordan [Jor66b, Jor66a]: the ﬁrst concerns the role of fundamental
contours in determining the homeomorphism type of a surface, and the second
presents the notion of a “class” of contours (i.e., free homotopy class) subsequently
used by Hadamard in [Had98]. Jordan’s notation is that adopted by Hadamard,
and he hints at the representation of curves by words (with positive or negative
exponents). Finally, it should be noted that in Hadamard’s study, the point of
view is geometric rather than dynamic: geodesics are regarded as oriented curves,
and there appears no explicit sense of a “geodesic ﬂow”; in particular Hadamard’s
symbolic coding is static in nature.
In an important paper [Bir12] published in 1912 (and based on a presentation to
the American Mathematical Society in 1909), G. D. Birkhoﬀ analyzes the behavior
of recurrent trajectories in a dynamical system deﬁned by a system of ordinary
diﬀerential equations. The word “recurrent” here corresponds to what we now call
“minimal”.
2 A collection M of trajectories of a dynamical system is minimal if
every element of M has all elements of M in its α-and ω-limit sets; Birkhoﬀ calls
any trajectory belonging to a minimal set “recurrent”. He proves that recurrence (in
this sense) is equivalent to (what we now call) almost-periodicity: for any ε > 0 there
exists a length T such that the whole trajectory is contained in an ε-neighborhood
of any segment of length T . Obvious examples of minimal sets are equilibria and
closed orbits; Birkhoﬀ also notes the example of dense lines on a torus, and calls a
recurrent motion continuous if the corresponding minimal set forms a continuum
of some dimension. The a priori possibility of discontinuous recurrent trajectories
is illustrated by the suspension of a nontransitive homeomorphism of the circle
with irrational rotation number, and Birkhoﬀ asks whether discontinuous recurrent
trajectories can occur in analytical dynamical systems.
Morse, in his 1917 dissertation under Birkhoﬀ (published as [Mor21a] and [Mor21b])
establishes the existence of recurrent geodesics of discontinuous type on surfaces of
negative curvature and negative Euler characteristic. He considers the bounded

2What we now call recurrent is called stable in the sense of Poisson.

GENESIS OF SYMBOLIC DYNAMICS 3

region S obtained by cutting oﬀ any inﬁnite “funnels” using closed geodesics,
and codes the geodesics entirely contained in S by recording the order in which
they cross a family of transversals (“normal segments”) that cut S into a simply-
connected region—in eﬀect lifting the geodesic to the hyperbolic plane. He then
shows that this coding distinguishes geodesics in S, and by constructing the “Morse
sequence” (discovered earlier and independently by Thue [Thu12]) proves the ex-
istence of discontinuous recurrent geodesics. Furthermore, he shows by symbolic
methods that every closed geodesic in S is a limit of discontinuous recurrent ones.
Since Hadamard had shown that every geodesic in S is a limit of closed geodesics,
it follows that the recurrent geodesics of discontinuous type are dense in the set of
all geodesics contained in S. Despite the closer connection with dynamical ideas,
the point of view in these papers remains geometric: geodesics are still regarded as
curves rather than trajectories, and the coding is used to establish that a geodesic
is recurrent (in his sense) and not closed.
In 1920, Birkhoﬀ published a study [Bir20] setting forth a number of ways that
the behavior of a dynamical system with two degrees of freedom can be studied
by means of the successive intersections of orbits with a transverse surface; strictly
speaking, such a surface of section is not entirely transverse to the ﬂow, as it is
bounded by closed orbits, but its interior is transverse to the ﬂow. The general
setup had been formulated by Poincar´e in [Poi97, vol. III, Chap. 27], as a means of
studying periodic and homoclinic orbits in celestial mechanics. Birkhoﬀ had used
the same setup in a limited way for similar purposes in 1917 ([Bir17]). In Chapters
5 and 6 of [Bir20], Birkhoﬀ goes beyond the study of periodic orbits to study, in
some abstraction, the behavior of the “Poincar´e map”, deﬁning α- and ω-limit sets,
minimal sets and his related notion of recurrence, as well as transitivity.
In 1924, Artin published a brief but inﬂuential paper [Art24] in which he shows
that the orbit space of the group of linear fractional transformations with integer
coeﬃcients acting on the hyperbolic plane (in the half-plane model) has a dense
geodesic (in fact, the set of these has full measure). His proof involves a coding of
geodesics via the continued fraction expansion of their “endpoints at inﬁnity” on
the real line. (His term for transitivity is “quasiergodicity”.)
In 1927, in the ﬁrst of his papers on mapping classes [Nie27], Nielsen formulates a
similar coding geometrically, in terms of the fundamental group, to study the axes of
hyperbolic transformations on surfaces obtained as quotients of the hyperbolic disc
by a Fuchsian group. Nielsen’s approach has some similarities to Morse’s coding of
geodesics via transverse segments, but the dynamics that comes in is that of the
Fuchsian group acting on the universal covering.
In his 1927 book, Dynamical Systems [Bir27], a broad survey of work on dynami-
cal systems (primarily of mechanical origin), Birkhoﬀ included Chapter 7, “General
Theory of Dynamical Systems”, which sets forth the notions of wandering and non-
wandering orbits, central motions, minimal sets, and transitivity in the general
context of the ﬂow generated by a system of diﬀerential equations. Much of this
reﬂected ideas formulated earlier in his 1912 paper [Bir12].
In 1935, Birkhoﬀ summed up his work on dynamics in a long paper [Bir35],
“crowned” and published by the Pontiﬁcal Academy of Sciences. Chapter 3, a study
of behavior near a hyperbolic periodic orbit, is based on a detailed examination of
the dynamics of a Poincar´e map for a transverse section. By symbolic methods

4 ETHAN M. COVEN AND ZBIGNIEW H. NITECKI

that, several decades later, were modiﬁed and used by Smale to prove the “Smale-
Birkhoﬀ” theorem and to construct the “horseshoe”, Birkhoﬀ demonstrates the
existence of highly complicated “ﬁrst return” behavior for periodic orbits near any
orbit homoclinic to a hyperbolic periodic orbit or, more generally, belonging to a
loop of heteroclinic connections.
This work forms the background to two papers by Morse and Hedlund, entitled
“Symbolic Dynamics” [MH38, MH40], published in 1938 and 1940, respectively.
Hedlund, in his dissertation written under Morse in 1929 [Hed32a, Hed32b] had
proved the existence of a length-minimizing closed geodesic in each free homotopy
class for any Riemmannian metric on the torus; Morse [Mor24] had proved the
same result for surfaces of higher genus. Hedlund went on to study geodesics on
surfaces [Hed35b, Hed35a, Hed36b, Hed36a], in particular proving the ergodicity of
the geodesic ﬂow on a closed surface of constant negative curvature [Hed35b], using
Nielsen’s symbolic coding [Nie27], and transitivity of the horocycle ﬂow [Hed36a].
In 1939 he published a survey of results on the dynamics of geodesic ﬂows [Hed39],
in which he formulates seven types of transitivity, elaborating on Birkhoﬀ’s def-
initions in [Bir27]: these include our notion of topological transitivity (“regional
transitivity”, which he notes is equivalent to the existence of a dense trajectory),
topological mixing (“permanent regional transitivity”), ergodicity (“metric tran-
sitivity”) and mixing (“mixture”) as well as hybrids of topological and ergodic
notions of transitivity. He quotes theorems establishing many of these properties
for geodesic ﬂows on surfaces of constant negative curvature, as well as an example
of a topologically mixing but non-ergodic geodesic ﬂow. At the end of the article
he plugs the work he had started with Morse in [MH38]:

The development of a symbolic theory apart from its dynamical
signiﬁcance has recently been begun by Morse and the author (cf.
Morse [4]). This initial work includes an extensive analysis of transi-
tive symbolic trajectories. The full scope of these symbolic methods
in dynamics is yet to be determined.

The ﬁrst of the Morse-Hedlund papers [MH38] sets forth a general theory of
what we now call shift spaces, focusing on recurrence and transitivity properties of
sequences. The motivation in the introduction refers primarily to geodesic ﬂows on
surfaces of negative curvature, but after that the treatment is quite abstract. The
authors’ view of the place of their study in dynamics as a whole is stated as follows
[MH38, pp. 816-817]:

Symbolic dynamics as the authors conceive it forms one of the three
divisions
(1) representation theory,
(2) symbolic dynamics,
(3) existence of space forms,
of the whole theory. The representation theory is concerned with
the conditions on space forms under which trajectories admit a one-
to-one symbolic representation in terms of which the recurrence or
transitivity of the trajectory can be determined. These conditions
will involve the Poincar´e fundamental group of the space and dif-
ferential conditions such as that of uniform instability (cf. Morse

GENESIS OF SYMBOLIC DYNAMICS 5

[4]
3, p. 64). In (3) one is concerned with the existence of space
forms satisfying the conditions discovered in (1). The questions
involved are rather deep extensions of the Hilbert, Koebe theory
of spaces of negative curvature (cf. Hilbert [1]
4, and Koebe [1]
5).
A simple typical theorem is that there exists no two-dimensional
Riemannian manifold of the topological type of the torus satisfying
the condition of uniform geodesic instability. The bearing of such
studies on questions of topological and metric transitivity will be
made clear in later papers.
Clearly, Morse and Hedlund view their paper as initiating a new branch of the the-
ory of dynamical systems. However, it does not seem to us that the shift dynamical
system is as yet considered as an object of study.
Beginning with a ﬁnite alphabet, Morse and Hedlund deﬁne an I-trajectory to
be a two-sided indexed sequence of letters; a symbolic element E(r, a) is an I-
trajectory a = ...a−1a0a1... together with a choice of a distinguished position r on
it. The space of all symbolic elements is given the metric

d(E(r, a), E(s, b) = 1
m
when ar−m...ar+m and bs−m...bs+m are the longest symmetric words centered on
the distinguished positions which agree termwise (elements whose distinguished
positions have diﬀerent values are at inﬁnite distance). They establish that this
gives the space of symbolic elements the topology of a Cantor set. The space of
I-trajectories is given the metric

[a, b] = lim sup
n→∞ 1
2n + 1
 n∑

−n δ(ai, bi)

(where δ(ai, bi) = 1 or 0, as ai and bi are the same or diﬀerent) which they view as an
analogue of the sup metric on functions, as used by Besicovitch in his treatment of
almost-periodic functions [Bes32]—in fact, their notation closely follows his. They
deﬁne an I-trajectory a to be almost periodic if for every ε > 0 the iterates Dr of
the shift automorphism which satisfy

[Dr(a), a] < ε

form a relatively dense set of integers (that is, there is an integer N such that any
set of N consecutive integers intersects the set). Note that this is stronger than
what we now call almost-periodicity, as there is a uniformity condition involved.
They consider subsets of the space of trajectories deﬁned by admissible blocks;
their admissibility rules appear to be of ﬁnite type, although they state a family
of conditions [MH38, p. 823] which are far more restrictive, and appear to be
motivated by Nielsen’s formalism, to which they explicitly refer as an example.
Again, they show that the subspace so deﬁned has the topology of a Cantor set.
They then study limit trajectories and minimal sets of trajectories from a symbolic
point of view, and present the Morse sequence. The last 60% of the paper (pp. 833-
864) is taken up with a number of functions that measure the “speed” of recurrence;
these need not occupy us in detail here. It should be noted that, despite the

3This reference is our [Mor21a].
4[Hil01]
5[Koe31]

6 ETHAN M. COVEN AND ZBIGNIEW H. NITECKI

dynamical background, and the appearance of the shift automorphism in two places
(pp. 817 and 822), it is used in a way analogous to Besicovitch’s use of translations
to study almost-periodic functions (in fact, as we have noted, their notation is the
same); there is no sense of a dynamical system generated by iteration of the shift.
Morse and Hedlund’s second paper [MH40] concerns a speciﬁc class of subshifts,
which they explain characterize the geodesics on a ﬂat torus. These are built on
an alphabet of two symbols and are deﬁned by the condition that for each symbol,
any two maximal blocks of consecutive appearances of the symbol diﬀer in length
by at most one. At the end of their previous paper, they had noted the relation
of this condition to the Sturm Separation Theorem concerning the distribution of
zeroes of the solution of the diﬀerential equation

y′′ + f (x)y = 0

where f (x) is periodic with period one: one symbol represents the locations of
zeroes, the other the locations of integers (it is assumed without loss of general-
ity that the solution has no integer zeroes). They call such trajectories Sturmian
trajectories. This paper is a detailed algebraic study of various combinatorial func-
tions that characterize a Sturmian trajectory. Again, there is no explicit dynamical
system here.
The journal lists [MH40] as received June 19, 1939. Two years later, Hedlund
wrote to Morse as follows: Charlottesville, Virginia
June 7, 1941
Dear Marston:
As you probably know, a number of topologists are becoming
interested in a study of the structure of the orbits obtained when
a topological transformation is iterated on a space X, say a
separable metric space. They term an orbit the set T n(x),
n = ... − 1, 0, +1, +2, ..., where x is a point of X, deﬁne a point x
to be periodic if there exists an integer m > 0 such that
tm(x) = x, and deﬁne apoint x to be almost periodic if there
exists a sequence of integers n1 < n2 < ... such that
limi→∞ T ni(x) = x. This last deﬁnition is of course the well
known property of (positive) stability in the sense of Poisson and
the term almost periodic is somewhat of a misnomer. These
topologists are not in the least aware that there is an immmense
amount of material in dynamics which they should know and they
will probably rediscover such interesting things as minimal sets,
recurrent motions, minimal centers of attraction, central motions,
transitivity, permanent regional transitivity, etc., in the not too
distant future. For example, in the last issue of Mathematical
Reviews (see page 179, review of a paper of Schweigert) Ayres
comments that Schweigert has an interesting example for which
the periodic points are everywhere dense in a space, but not all
the points of the space are periodic. Now this is such a common
occurrence in dynamics that we scarcely wonder at it any more.
But I wonder if it is their fault that these things are not better
known. For a person who hasn’t dealt considerably with these

GENESIS OF SYMBOLIC DYNAMICS 7

matters it might be a hard task to dig the material out of the
literature. One reason is perhaps that in dynamics we deal largely
with ﬂows, whereas the topologists deal with the discrete case of a
single transformation and its iterates. Though the two are not
essentially diﬀerent, it seems to me that something should be done
about this situation. Yet I hesitate about publishing material
which can onlybe [sic] considered a rehash of mathematics which
is well known ( to at least a dozen people ).

However, one simple example occurs to me which might make for
more awareness concerning the results of dynamics. Let M be the
space of symbolic elements of our ﬁrst paper on symbolic
dynamics and let T be the transformation which shifts the index
by one, say to the right. Here is a topological transformation
which ought to be complex enough to suit the heart of even the
most pathological topologist. The periodic trajectories are
everywhere dense; the non-periodic recurrent trajectories are
everywhere dense; there are transitive trajectories and they form a
residual set; the non-periodic, non-recurrent, non-transitive
trajectories which are stable in the sense of Poisson are
everywhere dense; there are trajectories asymptotic to almost
anything; the transformation is permanently regionally transitive.
What do you think of giving them this example on which to
chew? In view of what we have avaible[sic] in SDI, it should not
occupy much space.

Though the preceding example is a good one, it has one defect.
The space M is, as we showed, compact, perfect, and totally
disconnected. The last property of being totally disconnected
should not be essential to the situation and is not characteristic of
classical dynamical systems, where the underlying spaces are
manifolds. The space M is disconnected because the metric which
we chose to topologize the space assumes only discrete values.
Would it be possible to topologize the space in some other fashion
so that it becomes say a continuum (compact, connected space)? I
began thinking of this last night and the answer hasn’t occurred
to me yet. It should be possible to deﬁne a non-trivial metric in
the space M of elements such that it goes to zero as larger and
larger blocks with center at the preferred symbol become identical
and yet such that M is connected. It may be necessary to identify
a denumerable set of elements in pairs, but that would not be
objectionable. I should think that almost any sort of a space
might be obtained with the proper choice of metric, and the whole
problem seems interesting.

If all this is of interest to you, I will be glad to learn your
reactions.
 As ever,

G A H

8 ETHAN M. COVEN AND ZBIGNIEW H. NITECKI

Several features of this letter deserve comment. The ﬁrst thing that strikes one is
the penultimate paragraph, in which Hedlund wonders whether by a diﬀerent choice
of metric the space of symbolic elements could be made connected. Of course, on
closer reading this is modiﬁed by the comment that this might be accomplished by
identifying a countable number of pairs of points. Anachronistically, one could view
this as a precursor of the construction of Markov partitions [Par66, Ber67, AW67,
AW70]. Of course, the fact that the shift space itself has the topology of a Cantor
set is these days taken for granted, and not viewed as problematic: the coding
is a map from an initially given dynamical system to the shift dynamical system.
Second, Hedlund is fully aware of the idea of a discrete dynamical system, and sees
it as fundamentally equivalent to the idea of a ﬂow. He is also completely aware of
the interplay of topological and dynamical features of the system, something that
is not clear in the earlier joint papers. Finally, the implied distinction between
dynamics and topology has been somewhat erased in more recent years.
Perhaps a comment on the interests of “a number of topologists” mentioned in
the ﬁrst sentence of Hedlund’s letter is in order. A search of the Mathematical
Reviews (which began only a year before Hedlund’s letter, in 1940) and Zentral-
blatt (begun about ten years earlier) of that period reveals a large number of works
concerning periodic and ﬁxedpoint behavior of iterated transformations on man-
ifolds and metric spaces. Of course, there were some more sophisticated precur-
sors: Brouwer’s characterization of ﬁxedpoint-free transformations of the plane (the
“Brouwer translation theorem” [Bro12]), Denjoy’s work on ﬂows on the torus or,
equivalently, diﬀeomorphisms of the circle [Den32b, Den32a], (see also [vK35]), and
the work of Fatou [Fat06, Fat19, Fat20] and Julia [Jul18] on iteration of rational
functions.
Hedlund’s reference to “the last issue of Mathematical Reviews” may give the
impression that his acquaintance with the work of “some topologists” was second-
hand. The paper trail suggests otherwise. The review in question, a one-paragraph
review of [Sch40] by Ayres: Math. Rev. 2, 179b (MR 3198), begins by referring to a
paper by Hall and Schweigert [HS38] which is being generalized by Schweigert in the
paper under review. Hall was no stranger to Hedlund. A paper by Hall and Kelley
[HK41] which appears in Hedlund’s bibliography to [Hed44], was published in 1941,
based on a presentation to the American Mathematical Society in September 1939.
This paper concerns variants of periodicity for an iterated self-homeomorphism of
a compact metric space, including uniform and non-uniform versions of almost-
periodicity. Hall and Kelley formulate the notion of a minimal set (which they call
“irreducibly ﬁxed”) and show that this is equivalent to every orbit being dense,
and that either such a set is a single periodic orbit, or every orbit in it is almost
periodic. In a footnote, they acknowledge that “It has been pointed out to the
authors that...[these results]...are precisely analogous to certain results of G. D.
Birkhoﬀ for continuous ﬂows...” In an earlier footnote, they achnowledge

This paper was started when the authors were in residence at the
University of Virginia, the ﬁrst named author as a National Re-
search Fellow.

Recall that Hedlund’s letter was written in Charlottesville, Virginia, where he had
joined the University of Virginia faculty in 1939.
In any case, it appears that Morse failed to respond to Hedlund’s letter in any
substantial way. Hedlund wrote a new article, “Sturmian Minimal Sets” [Hed44],

GENESIS OF SYMBOLIC DYNAMICS 9

submitted to the journal in January, 1944. The minimal sets of the title are ad-
dressed in the second half of the paper. Hedlund begins boldly, explicitly intro-
ducing the notion of an orbit (note: not “trajectory”) and semi-orbit for a discrete
dynamical system. He formulates discrete dynamical system versions of the def-
initions in [Bir27] of α- and ω-limit sets, invariant sets, minimal sets, recurrent
orbit (in the sense of being contained in a minimal set), and almost-periodic or-
bit, and notes the equivalence of the last two notions. Then he comments that
the dual terminology “recurrent” and “almost periodic” for equivalent notions is
redundant; he argues that the latter is the better terminology for this notion, and
suggests that “recurrent” be saved for “Poisson stable” (our current meaning of
“recurrent”). He then repeats the deﬁnitions of symbolic trajectory and symbolic
element from [MH38], and introduces a modiﬁed version of the metric on symbolic
elements (replacing m with m + 1, so that elements which agree only at the dis-
tinguished position are at distance 1), noting that this gives the space of symbolic
elements the topology of a Cantor set—apparently abandoning his concerns in the
letter about this.
Then, signiﬁcantly, Hedlund introduces the shift map S and proves that it is a
one-to-one, continuous transformation of the space of symbolic elements to itself.
He notes that the symbolic trajectories are in one-to-one correspondence with the
orbits of S, with periodic trajectories corresponding to periodic orbits, and recalls
the existence of the Morse sequence and Sturmian minimal trajectories of [MH40]
as examples of almost-periodic non-periodic orbits. He then proceeds to construct
Sturmian minimal sets by coding orbits of a rotation of the circle by β radians, where
β is an irrational multiple of π, using a partition into arcs of length β and 2π − β,
respectively.
6 He associates to each orbit two symbolic elements, corresponding to
making the atoms of the partition right- or left-open. He proceeds to prove ﬁrst
that the symbolic sequences which arise this way correspond to almost-periodic
orbits of the rotation, and then that this corresponds to being minimal under S.
He proves that the minimal set (for S) so obtained is compact, perfect and totally
disconnected, and contains a pair of doubly asymptotic orbits. He then deﬁnes
the notion of an orbit-preserving transformation with respect to a given discrete
dynamical system (this is our notion of a self-conjugacy) and proves that in his
minimal sets it is not always possible to ﬁnd an orbit-preserving transformation
taking one orbit in the set to an arbitrarily designated second orbit in the set. He
attributes the corresponding question for ﬂows to Birkhoﬀ. He deﬁnes a notion of
almost-periodicity for a transformation (as opposed to a single orbit) and shows
that the restriction of S to his minimal sets does not have this property. However,
he then deﬁnes a notion of local almost-periodicity, and shows that his minimal sets
do have this property. Finally, he deﬁnes a minimal set to be powerfully minimal
if it is minimal under all nonzero iterates of the discrete dynamical system, and
proves that his minimal set has this property.
While the focus in this paper is on a speciﬁc class of minimal sets (the “Sturmian”
ones), Hedlund’s letter suggests that these are now a case study for a more general,
abstract study of minimal sets and dynamical properties of the discrete dynamical
system deﬁned by S on the space of symbolic elements, and thus open the door to
the branch of topological dynamics we now call “symbolic dynamics”.

6Hedlund here works with translation on the real line, but his coding depends only on the mod
1 positions of points.

10 ETHAN M. COVEN AND ZBIGNIEW H. NITECKI

References

[Art24] Emil Artin, Ein mechanisches System mit quasiergodischen Bahnen, Abhandlungen des
mathematisches Seminar, Universit¨at Hamburg (1924), 170–175, Reprinted in [Art65,
pp. 499-504].
[Art65] , Collected papers, Springer-Verlag, 1965, edited by Serge Lang and John Tate.
[AW67] Roy Adler and Benjamin Weiss, Entropy, a complete metric invariant for automor-
phisms of the torus, Proceedings, National Academy of Sciences 57 (1967), 1573–1576.
[AW70] , Similarity of automorphisms of the torus, Memoirs, American Mathematical
Society 98 (1970).
[Ber67] Kenneth Berg, On the conjugacy problem for K-systems, Ph.D. thesis, University of
Minnesota, 1967.
[Bes32] A. S. Besicovitch, Almost periodic functions, Cambridge University Press, 1932, Dover
Reprint, 1954.
[Bir12] George David Birkhoﬀ, Quelques th´eor`emes sur le mouvement des syst`emes dy-
namiques, Bulletin de la Soci´et´e Math´ematique de France 40 (1912), 305–323, Reprinted
in [Bir50, vol. 1, pp. 654-672].
[Bir17] , Dynamical systems with two degrees of freedom, Transactions, American Math-
ematical Society 18 (1917), 199–300, Reprinted in [Bir50, vol. 2, pp. 1-102].
[Bir20] , Surface transformations and their dynamical applications, Acta Mathematica
43 (1920), 1–119, Reprinted in [Bir50, vol. 2, pp. 111-229].
[Bir27] , Dynamical systems, AMS Colloquium Publications, vol. IX, American Mathe-
matical Society, 1927, Reissued, revised, 1966.
[Bir35] , Nouvelles recherches sur les syst`emes dynamiques, Memoriae Pont. Acad. Sci.
Novi Lyndaei 1 (1935), 85–216, Reprinted in [Bir50, vol. 2, pp. 530-661].
[Bir50] , Collected mathematical papers, American Mathematical Society, 1950, Dover
reprint, 1968.
[Bro12] L. E. J. Brouwer, Beweis des ebenen Translationssatz, Mathematische Annalen 72
(1912), 37–54, Reprinted in [Bro76, vol. 2, pp. 250-268].
[Bro76] , Collected works, North-Holland, 1976, Edited by Hans Freudenthal.
[Den32a] Arnaud Denjoy, Sur les caract´eristiques `a la surface du tore, Comptes Rendus, Acad.
Sci. Paris 194 (1932), 830–833, 2014–2016.
[Den32b] , Sur les courbes d´eﬁnies par les ´equations diﬀ´erentielles `a la surface du tore,
Journal de Math´ematiques Pures et Appliqu´es 11 (1932), 5–8.
[Fat06] P. Fatou, Sur les solutions uniformes de certaines ´equations fonctionnelles, Comptes
Rendus, Acad. Sci. Paris 143 (1906), 546–548.
[Fat19] , Sur les ´equations fonctionnelles, Bulletin de la Soci´et´e Math´ematique de France
47 (1919), 161–271.
[Fat20] , Sur les ´equations fonctionnelles, Bulletin de la Soci´et´e Math´ematique de France
48 (1920), 33–94, 208–314.
[Had98] Jacques Hadamard, Les surfaces `a courbures oppos´ees et leur lignes geodesiques, Journal
de Math´ematiques Pures et Appliqu´es 4 (1898), 27–73, Reprinted in [Had68, vol. 2, pp.
729-775].
[Had68] , Oeuvres de Jacques Hadamard, Centre National de la Recherche Scientiﬁque,
1968.
[Hed32a] Gustav Hedlund, Geodesics on a two-dimensional Riemannian manifold with periodic
coeﬃcients, Annals of Mathematics 33 (1932), 719–739.
[Hed32b] , Poincar´e’s rotation number and Morse’s type number, Transactions, American
Mathematical Society 34 (1932), 75–97.
[Hed35a] , A metrically transitive group deﬁned by the modular group, American Journal
of Mathematics 57 (1935), 668–678.
[Hed35b] , On the metrical transitivity of the geodesics on closed surfaces of constant
negative curvature, Annals of Mathematics 35 (1935), 787–808.
[Hed36a] , Fuchsian groups and transitive horocycles, Duke J. of Math. 2 (1936), 530–542.
[Hed36b] , Two-dimensional manifolds and transitivity, Annals of Mathematics 37 (1936),
534–542.
[Hed39] , The dynamics of geodesic ﬂows, Bulletin, American Mathematical Society 451
(1939), 241–260.
 GENESIS OF SYMBOLIC DYNAMICS 11

[Hed44] , Sturmian minimal sets, American Journal of Mathematics 66 (1944), 605–620.
[Hil01] David Hilbert, ¨Uber Fl¨achen kinstanter Gausscher Kr¨ummung, Transactions, American
Mathematical Society 2 (1901), 87–99.
[HK41] D. W. Hall and J. L. Kelley, Periodic types of transformations, Duke J. of Math. 8
(1941), 625–630.
[HS38] D. W. Hall and G. E. Schweigert, Properties of invariant sets under pointwise periodic
homeomorphisms, Duke J. of Math. 4 (1938), 719–724.
[Jor66a] Camille Jordan, Contours trac´es sur les surfaces, Journal de Math´ematiques Pures et
Appliqu´es 11 (1866), 110–130.
[Jor66b] , La d´eformation des surfaces, Journal de Math´ematiques Pures et Appliqu´es
11 (1866), 105–109.
[Jul18] Gaston Julia, M´emoire sur l’it´eration des fonctions rationnelles, Journal de
Math´ematiques Pures et Appliqu´es 4 (1918), 47–245.
[Kit98] Bruce P. Kitchens, Symbolic dynamics: One-sided, two-sided and countable state
Markov shifts, Springer, 1998.
[Koe31] P. Koebe, Riemannsche Mannigfaltigkeiten und nichteuklidische Raumforme, Stizungs-
berichte der Preussishcen Akademie der Wissenschaften (1927;1928; 1929; 1930; 1931),
345–442; 414–457; 304–364, 505–541; 506–534.
[KU05] Svetlana Katok and Ilie Ugarcovici, Symbolic dynamics for the modular surface and
beyond, To appear, Bulletin of American Mathematical Society, 2005.
[LM95] Douglas Lind and Brian Marcus, An introduction to symbolic dynamics and coding,
Cambridge University Press, 1995.
[MH38] Marston Morse and Gustav Hedlund, Symbolic dynamics, American Journal of Mathe-
matics 60 (1938), 815–866, Reprinted in [Mor81, pp. 443-494].
[MH40] , Symbolic dynamics II. Sturmian trajectories, American Journal of Mathematics
62 (1940), 1–42.
[Mor21a] Marston Morse, A one-to-one representation of geodesics on a surface of negative cur-
vature, American Journal of Mathematics 43 (1921), 33–51, Reprinted in [Mor81, pp.
1-20].
[Mor21b] , Recurrent geodesics on a surface of negative curvature, Transactions, American
Mathematical Society 22 (1921), 84–100, Reprinted in [Mor81, pp. 21-38].
[Mor24] , A fundamental class of geodesics on any closed surface of genus greater than
one, Transactions, American Mathematical Society 26 (1924), 25–60.
[Mor81] , Selected papers, Springer-Verlag, 1981, Edited by Raoul Bott.
[Nie27] Jakob Nielsen, Untersuchungen zur Topologie der geschlossenen zweiseitigen Fl¨achen,
Acta Mathematica 50 (1927), 189–358, English translation by J. Stillwell, [Nie86, vol.
1, pp. 223-341].
[Nie86] , Collected mathematical papers, Birkh¨auser, 1986, edited by Vagn Lundsgaard
Hansen.
[Par66] William Parry, Symbolic dynamics and transformations of the unit interval, Transac-
tions, American Mathematical Society 122 (1966), 368–378.
[Poi97] Henri Poincar´e, Les m´ethodes nouvelles de la m´ecanique c´eleste, Guthier-Villars, 1892,
1893, 1897, Dover reprint, 1957; also republished by Blanchard, Paris, 1987.
[Sch40] G. E. Schweigert, A note on the limit of orbits, Bulletin, American Mathematical Society
46 (1940), 963–969.
[Thu12] Axel Thue, ¨Uber die gegenseitige Lage gleicher Teile gewisser Zeichenreihen, Kristiana
(Oslo) Videnskapsselskapets Skrifter (1912), no. 1, 1–67, Reprinted in [Thu77, pp. 413-
477].
[Thu77] , Selected mathematical papers of Axel Thue, Universitetsforlaget, 1977, edited
by Trygve Nagell.
[vK35] E. R. van Kampen, The topological transformations of a simple closed curve into itself,
American Journal of Mathematics 57 (1935), 142–152.

Department of Mathematics, Wesleyan University, Middletown CT
E-mail address: ecoven@wesleyan.edu

Department of Mathematics, Tufts University, Medford, MA 02155, USA
E-mail address: zbigniew.nitecki@tufts.edu
