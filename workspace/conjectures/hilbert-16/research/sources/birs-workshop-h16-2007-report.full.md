<!-- source: https://www.birs.ca/workshops/2007/07w5021/report07w5021.pdf | converted from PDF -->

Mathematical developments around Hilbert’s 16th problem

Christiane Rousseau (Universit´e de Montr´eal)

March 12–16 2007

1 Overview of the Field

In his famous lecture of the 1900 International Congress of Mathematicians, David Hilbert stated a list of 23
problems with deep signiﬁcance for the advance of mathematical science. There has been intensive research
on these problems throughout the 20th century. Hilbert’s 16th problem called “Problem of the topology of
algebraic curves and surfaces” is one of the few problems which is still completely open. This problem
has two parts. The ﬁrst part asks for the relative positions of closed ovals of an algebraic curve given by
the set of points which are solutions of a polynomial equation P (x, y) = 0. The maximum number was
given by Harnack. As for the relative positions, even if this is a purely algebraic problem, there has been
little progress on the general case, while there is progress for small values of the degree of the polynomial P
(degree less or equal to 7). The workshop “Mathematical developments around Hilbert’s 16th problem”, held
in BIRS on March 12-16 2007, focused on the second part of the problem which is a problem in ordinary
differential equations, but with the components of the vector ﬁeld given by polynomials, or equivalently by
an algebraic Pfaff form. The second part of Hilbert’s 16th problem asks for the maximal number H(n) and
relative positions of limit cycles of planar polynomial (real) vector ﬁelds of a given degree n. This problem,
opened for more than a century, has been at the center of many developments in differential equations. The
main difﬁculty of Hilbert’s problem is that, although a polynomial vector ﬁeld is an algebraic object, its
trajectories are not algebraic. In the neighbourhood of singular points they may not even be analytic. The
fascination of Hilbert’s 16th problem comes from the fact that it sits at the conﬂuence of analysis, algebra,
geometry and even logic.

As mentioned above, Hilbert’s 16th problem, second part, is completely open. It was mentioned in
Hilbert’s lecture that the problem “may be attacked by the same method of continuous variation of coefﬁ-
cients... ”. Even if the problem was stated as early as 1900 it was only in 1987 that Ecalle and Ilyashenko
proved independently that a polynomial vector ﬁeld has a ﬁnite number of limit cycles. Both proofs are a
real “tour de force” and each requires a 300 pages volume. The idea is to compactify the phase space to the
Poincar´e disk. Then, as limit cycles are isolated periodic solutions, if there were an inﬁnity of them, they
would need to accumulate on a graphic (also called polycycle). By blowing up the singularities it is possi-
ble to limit oneself to graphics with hyperbolic or semi-hyperbolic (one nonzero eigenvalue) singularities.
For such a graphic one studies the return map in the neighborhood of the graphic and shows that it is not
oscillating.

While the result of Ecalle and Ilyashenko shows that each individaul polynomial vector ﬁeld has a ﬁnite
number of limit cycles it is impossible to derive from it any uniform estimate on the number of limit cycles.
Approaches to an accurate estimate H(n) have come from two sides. On the one hand there is the construction
of bounds from below. The best lower bound is of the order H(n) ≥ Cn2 ln n. Such a bound was found

1
 2

by Christopher and Lloyd [3] through the construction of polynomial vector ﬁelds of degree n with such a
number of limit cycles. This is done with a mixture of bifurcation methods and use of symmetries. So far,
the only approaches from above are of the form H(n) < ∞ also called “Existential part of Hilbert’s 16th
problem” or also “Finiteness part of Hilbert’s 16th problem”. An important contribution is this direction is
the program started in 1991 by Dumortier-Roussarie-Rousseau [7] and reducing the proof that H(2) < ∞
to the proof that 121 graphics have ﬁnite cyclicity. The program followed an idea of Roussarie [17] that,
compactifying both the phase space and the space of coefﬁcients, the global ﬁniteness would follow from
local ﬁniteness. Indeed limit cycles can only accumulate in the product of phase space times parameter space
on limit periodic sets. It hence sufﬁces to show that each limit periodic set has ﬁnite cyclicity (i.e. can give
rise to a ﬁnite number of limit cycles) inside the family of vector ﬁelds for which ﬁniteness is expected. This
idea of Roussarie is very powerful and has given rise to intense research on developing methods to prove the
ﬁnite cyclicity of limit periodic sets.

There exists many variants of Hilbert’s 16th problem. Several of them consists in addressing Hilbert’s
question for a simpler class of polynomial equations. In all cases the sub-questions mentioned above are
also considered namely bounds from below for the number of limit cycles and also the ﬁniteness problem.
Among the subfamilies considered are Abel equations, classical Li´enard equations and generalized Li´enard
equations.

A very important variant of Hilbert’s problem is the “tangential” or “inﬁnitesimal part” of Hilbert’s 16th
problem. This problem is related to the birth of limit cycles by perturbation of an integrable system with
an annulus of periodic solutions. Under the perturbations usually only a ﬁnite number of periodic solutions
remain. When the integrable system is Hamiltonian, then the number of limit cycles appearing in a small
perturbation of the system is obtained by counting the number of zeroes of Abelian integrals, at least as long
as one remains far from polycycles. The subject is very active and has been covered and discussed widely
during the workshop.

It is more than a century that Hilbert’s problem was stated and we do not yet know if there exists a
uniform upper bound for the number of limit cycles of degree n. Specialists tend to believe that such a bound
exists and all efforts are in this direction. It is tempting here to mention Khovanskii’s theory of fewnomials.
Indeed the essence of Hilbert’s problem is that, although the trajectories of a polynomial vector ﬁeld are not
algebraic, the algebraic nature of the system should leave its footprints and imply ﬁniteness properties. The
theory of fewnomials applied to Pfaff forms is remarkable in that aspect. It proves non-oscillating properties
of separating solutions of Pfaff forms, which in itself is a spectacular demonstration that the phase curves
“know” they have some kind of algebraic nature. Moreover the method of Khovanskii is extremely powerful
for proving existence of upper bounds on the number of solutions of equations or systems of equations.

The developments around Hilbert’s 16th problem and those on complex dynamics, in particular Fatou and
Julia sets, had long developed in parallel, although they share some common problematics and methods of
solutions. On purpose, researchers representing both groups had been invited together. In particular Adrien
Douady had been invited to the workshop. He passed away between the time that the workshop was planned
and the effective time of the workshop. His heritage is immense and his far reaching ideas have had an
inﬂuence far outside his own ﬁeld of complex dynamics. In particular it is his idea and the thesis of Lavaurs
which made possible to identify the space of modules for unfoldings of parabolic points.

2 Theme and plenary lectures

The workshop brought together researchers making signiﬁcant contributions to domains of differential equa-
tions related to Hilbert’s 16th problem. The focus was put on the following subjects:

(i) singularities of differential equations and complex foliations, and related normal forms,

(ii) bifurcations of differential equations and ﬁnite cyclicity problems,

(iii) algebro-geometric techniques in differential equations.
 3

In order to present an overview of the most signiﬁcant directions the workshop started with invited lec-
tures given by Robert Roussarie, Pavao Marde´siˇc, Vadim Kaloshin, Jean-Christophe Yoccoz and Abdelraouf
Mourtada with the purpose of describing the principal breakthroughs or main directions in the subject.

The lecture of Robert Roussarie enlightened the importance of the study of singular perturbed systems
in the study of Hilbert’s 16th problem. A brilliant demonstration of this is given in the recent paper [6]
of Dumortier–Panazzolo–Roussarie where they give a counter-example to the celebrated conjecture of Lins
Neto-Pugh-de Melo on the number of limit cycles of classical Li´enard equations stating that a classical
Li´enard system of degree 2n or 2n + 1 has at most n limit cycles. As this conjecture was cited by Smale in
his list of problems at the beginning of the twentieth century, it is also called Smale’s conjecture. The study
of singular perturbed systems is likely to bring new conjectures on the maximum number of limit cycles for
polynomial vector ﬁelds. Indeed, it is possible by perturbation of such systems to create exponentially small
regions in parameter space in which we observe more limit cycles than those which can be created by the
standard bifurcation techniques.

The expository lecture of Pavao Marde´siˇc focused on techniques and difﬁculties of what is called the
inﬁnitesimal and tangential Hilbert 16-th problem, namely the number of zeroes of Abelian integrals and
the number of limit cycles that can be created by perturbing a Hamiltonian vector ﬁeld. Pavao Marde´siˇc
distinguished between the “tangential Hilbert 16-th problem” which is strictly limited to the study of the
number of zeroes of Abelian integrals and the “inﬁnitesimal Hilbert 16-th problem” which is concerned with
the number of limit cycles that can be created by perturbation of a polynomial Hamiltonian system. The
lecture started with the celebrated ﬁniteness result of Varchenko-Khovanskii, stating for any integer N the
existence of a uniform bound for the number of zeroes of Abelian integrals of forms of a degree ≤ N over
ovals of a Hamiltonian of degree ≤ n. The idea of the proof is to use the Picard-Fuchs equations satisﬁed
by Abelian integrals and to ﬁnish the proof by a special study in the neighborhood of the polycycles. Among
the recent signiﬁcant generalizations we ﬁnd the results of Mourtada and Novikov, both highlights of this
workshop. An important property of Abelian integrals is the Chebychev property which allows to give a
bound on the number of zeros of the Abelian integrals based only on the dimension of the vector space of
these. A geometric explanation of the Chebychev properties of elliptic envelopes was given, coming from the
fact that the Picard-Fuchs is 2-dimensional because the homology group is 2-dimensional. The generalization
for Hamiltonians of higher was discussed with known examples and counter-examples and open problems.

To make the link with algebraic dynamical systems Jean-Christophe Yoccoz lectured on the recent
results of Buff and Cheritat on the geometry and size of Siegel disks of quadratic polynomials which allow
them in particular to ﬁnd parameters for which the corresponding Julia set has positive Lebesgue measure.
He concentrated on the case where the multiplier λ of the quadratic polynomial P (z) = λz + z2 is of the
form λ = exp(2πiα) where α is a Liouvillian irrational number and he showed the limiting process which
leads to the existence of a Julia set with positive Lebesgue measure.

The lecture of Aldelraouf Mourtada summarized his immense work spread over several years to prove
the ﬁnite cyclicity of hyperbolic polycycles in compact families of analytic vector ﬁelds on the sphere S2,
including the introduction of several algebras of quasi-analytic functions and the use of the theory of fewno-
mials of Khovanskii. The work was started many years ago with the generic case of an attracting or repelling
polycycle. The proof sketched at the workshop included the case where the polycycle is an accumulation of
cycles (it is the boundary of an annulus of periodic solutions). The ideas of this proof are then used to extend
the result of Khovanski-Varchenko about Abelian integrals, to the neighbourhood of hyperbolic polycycles.
And this gives rise to the following general result: let H be a Morse polynomial of degree d + 1 which is
generic at inﬁnity (but maybe with multiple critical values). Then there exist a number N (d) (depending only
on d), such that every perturbation of dH (of degree d and with non vanishing Abelian integrals) has at most
N (d) limit cycles on the real plane.

The lecture of Vadim Kaloshin reported on recent breakthroughs in the restricted or planar 3-body prob-
lem. Among the problems discussed where the Hausdorff dimension of oscillatory motions, and the Arnold
diffusion. In private conversations, Vadim Kaloshin also discussed recent ideas on embedding planar poly-
nomial vector ﬁelds in Hamiltonian vector ﬁelds of dimension 4 with the hope of using Floer homology to
obtain new lower bounds for H(n).
 4

3 Presentation highlights

3.1 The role of singular perturbations in Hilbert’s 16th problem

After more than a century of work on Hilbert’s 16th problem and long lasting conjectures on the maximum
number of limit cycles for some special classes of polynomial systems it became very clear only recently that
the study of slow-fast systems is going to be one of the keys in the estimation of uniform upper bounds for
the number of limit cycles. Robert Roussarie explained the recent example of Daniel Pannazolo of a classical
Li´enard system providing a negative answer to Smale’s system. What is particularly remarkable in that case
is that no “classical method” allows to track this polynomial system with 5 limit cycles where only 4 were
expected by the conjecture. It gives a new light on the long standing conjecture that H(2) = 4. And it makes
the link with the remark of Joan Carlos Art´es, Jaume Llibre and Dana Schlomiuk [1] that a corner of the
bifurcation diagram of quadratic systems is a very degenerate slow-fast system.

3.2 The role of the study of singularities in Hilbert’s 16th problem

A group of lectures dealt with the study of singularities of analytic vector ﬁelds. This study is one of the
most basic and fundamental part of the subject as the singularities are the organizing centers of the foliations.
Among the study of singularities lies the problem of the center, which is fundamental in the context of
Hilbert’s 16th problem. The lecture of Emmanuel Paul sat in that context, where he discussed the Galoisian
reducibility for a germ of quasi-homogeneous foliation.

Singularities of Fuchsian systems. The lecture of Caroline Lambert illustrated the link between the unfold-
ings of the conﬂuent hypergeometric equation and that of the Riccati equation unfolding a saddle-node. In
this lecture she showed how to cover all parameter values in the conﬂuence from the hypergeometric equation
to the conﬂuent hypergeometric equation. In particular she was the ﬁrst to identify the parametric resurgence
phenomenon in this context and explain it. She could completely calculate the unfolding of the Martinet-
Ramis modulus for a Riccati equation unfolding a saddle-node of codimension 1. Rodica Costin discussed
the linearization of nonlinear perturbations of Fuchsian systems.

Moduli of analytic classiﬁcation of families unfolding resonant singularities. This was discussed by the
group of lectures of Lo¨ıc Teyssier (modulus space for germs of families unfolding saddle-nodes of codi-
mension k), Javier Ribon (analytic classiﬁcation of unfoldings of resonant diffeomorphisms) and Christiane
Rousseau (analytic classiﬁcation of unfoldings of resonant diffeomorphisms and moduli spaces in the codi-
mension 1 case). The moduli of analytic classiﬁcation of resonant singularities have been a tool in Ecalle’s
proof that limit cycles of an analytic vector ﬁeld cannot accumulate on a polycycle. Later. in the paper [5].
the Martinet-Ramis modulus of a saddle-node was used as a tool to prove the ﬁnite cyclicity of some graphics
of the DRR program [7]. While these graphics were generic, it became clear that to tackle the same kind of
questions for graphics which can produce an annulus of periodic solutions, then it was necessary to control
the behaviour in the parameter to be able to control the number of limit cycles which can appear in a pertur-
bation. Christiane Rousseau presented her joint work with Colin Christopher where they determine the space
of moduli of germs of generic 1-parameter families unfolding a diffeomorphism with a parabolic ﬁxed point.
It is the ﬁrst time that a space of moduli can be determined for a family of dynamical systems. In the same
spirit the lecture of Lo¨ıc Teyssier explored the higher codimension case for unfolding of saddle-node vector
ﬁelds. The description was based on the decomposition of a neighborhood of the singularities in sectors over
which the space of leaves is given by C. Now a complete modulus of analytic equivalence or conjugacy has
been given for a family unfolding the codimension k saddle-node and all the machinery is ready for attacking
the description of the space of moduli. Javier Ribon discussed a complete system of analytic invariants for
a germ of one-parameter family of diffeomorphisms unfolding a diffeomorphism with a parabolic point. His
results complete and extend those of [13]. In particular they are valid for any codimension and the family
need not be generic. Better criteria for deciding the analytic conjugacy of two such families are given.

Topology of leaves of analytic foliations on Stein manifolds. This was the topic of the lecture of Tanya
Firsova. Her theorem stated that, for a generic singular foliation of a Stein manifold, all leaves except possibly

5

a countable number are topological disks and the rest are topological cylinders. This result is likely to open a
new domain in analytic foliations.

3.3 Algebraic dynamical systems

The trend on algebraic dynamical systems and iteration of rational maps, started with the lecture of Jean-
Christophe Yoccoz and was followed by the lecture of Alexey Glutsyuk presenting that the horospheric lam-
ination of the orbit space of a rational function is topologically transitive, provided that the rational function
under consideration does not belong to an explicit list of exceptions.

3.4 o-minimal structures and Hilbert’s 16th problem

o-minimal structures have been studied for several years in conjunction with Hilbert’s 16th problem. This
comes from the fact that the properties of quasi-analytic solutions of analytic ordinary differential are well
captured by the language of algebra and logic, in the same way as they can be studied by the theory of fewno-
mials of Khovanskii. For instance it is well known that the non-spiraling leaves of real analytic foliations of
codimension 1 all belong to the same o-minimal structure. Some specialists of o-minimal sructures had to
cancel their coming to BIRS. Nevertheless the subject was represented at the workshop. As a follow-up to the
lecture of Abdelraouf Mourtada, the lecture of Reinhard Sch¨afke, discussed how non-oscillating trajectories
of real analytic vector ﬁelds sit inside o-minimal structures and explained that, under certain assumptions,
such a trajectory generates an o-minimal and model complete structure together with the analytic functions.
The proof uses the asymptotic theory of irregular singular ordinary differential equations in order to establish
a quasi-analyticity result from which the main theorem follows. An application was given of an inﬁnite fam-
ily of o-minimal structures such that any two of them do admit a common extension, and also an example of
non-oscillating trajectory of a real analytic vector ﬁeld in dimension 5 that is not deﬁnable in any o-minimal
extension of the reals.

3.5 Extension of the Varchenko-Khovanskii theorem to the Darboux integrable case

Dmitry Novikov presented a beautiful extension of the Varchenko-Khovanskii theorem to the Darboux in-
tegrable case, yielding a bound on the number of zeroes of Abelian integrals in the latter case. The tools
introduced for the proof of this result introduced new perspectives in tangential Hilbert’s 16th problem as the
classical tools for studying Abelian integrals do not work when we switch from a Hamiltonian system to a
Darboux integrable one. In particular the Pontrjagin-Melnikov integrals in that case have no natural extension
to the complex domain.

3.6 Results for particular classes of polynomial vector ﬁelds in the spirit of Hilbert’s
16th problem.

A special emphasis was put on special subclasses of polynomial vector ﬁelds for which Hilbert’s 16th problem
is much studied.

Quadratic vector ﬁelds. They have been studied very systematically by Joan Carlos Art´es, Jaume Llibre
and Dana Schlomiuk for several years. They now have a complete bifurcation diagrams of quadratic systems
with a weak focus of order greater or equal to 2 [1] and they start attacking the case of a weak focus of
order 1. Their study of the quadratic systems with weak order of order 2 has enlightened some corners of
the bifurcation diagram which they conjecture will produce the larger number of limit cycles in the family
of quadratic vector ﬁelds. For their work they mix algebro-geometric techniques with numerical simulations
and Joan Carlos Art´es lectured on the numerous phase portraits expected for a system with a weak focus of
order 1.

Classical Li´enard systems. The recent work of Freddy Dumortier and Magdalena Caubergh shows the
existence of a uniform explicit bound for the number of limit cycles of a classical Li´enard system of degree n

6

as long as one stays in a compact subsetof the parameter space, far from the singular perturbed system. The
ﬁniteness part of Hilbert’s 16th problem for this subfamily is thus reduced to the proof of the ﬁnite cyclicity
of the graphics in the singular perturbed systems.
The question of the number of critical periods of a polynomial vector ﬁeld with a center is often studied
in parallel and in the same spirit as the questions on the number of limit cycles of a polynomial vector ﬁeld.
Freddy Dumortier presented recent results with Peter De Maesschalck on the period function of the classical
Li´enard systems. Here again the problem of the existence of a uniform bound is reduced to the study of
slow-fast systems.

Unicity of a limit cycle of a vector ﬁeld and unicity of the critical period in an annulus of periodic
solutions surrounding a center. A number of results in this direction were presented. Jordi Villadelprat
discussed the period fonction of quadratic centers. Li´enard systems were discussed Jaume Llibre. An appli-
cation of results in Li´enard equations to a predator-prey system was discussed in the lecture of Huaiping Zhu.
Abel equations were discussed by Armengol Gasull and Rafel Prohens Sastre.

4 Recent Developments and Open Problems

The most important developments in the last years around Hilbert’s 16th problem are the following:

4.1 The role of singular perturbations for tracking additional limit cycles.

The techniques of geometric singular perturbation theory become more and more sophisticated and permit
now to treat problems where the slow manifold has a large number of local extrema and there are several
breaking parameters.
In this context an open problem stated by Roussarie is the following: what can be said of the number and
type of ﬁxed points of a composition of applications of the form

Ri(x) = αi + x
ri

with x > 0 and α1 ∈ R and ri > 0? Such compositions have been studied locally by Mourtada in the
case where αi ∼ 0 and for x close to 0. The new global problem appears naturally in singular perturbations
problem. Although very simple to state, very little is known on this problem. It seems easier to expect lower
bounds, but any result on bounds from below or bounds from above would be welcome.
Several ﬁniteness problems for subfamilies of polynomial vector ﬁelds in the spirit of Hilbert’s 16th
problem have been reduced to conjectures on slow-fast systems.
While the methods are becoming more sophisticated it remains the case that precise results on the number
of limit cycles are much harder to get when there is more than one limit cycle. This comes from the fact that
the analysis must be pushed to a much ﬁner level in order to be able to conclude

4.2 The recent progress in the tangential (inﬁnitesimal) Hilbert’s 16th problem.

The generalization by D. Novikov of the ﬁniteness result of Varchenko-Khovanskii for zeroes of Abelian
integrals to the case of a perturbation of an integrable foliation of Darboux type is a real breakthrough.
Varchenko-Khovanskii’s theorem states for any integer N the existence of a uniform bound for the number
of zeroes of Abelian integrals of forms of a degree ≤ N over ovals of a Hamiltonian of degree ≤ n. The
generalized theorem by Novikov states the existence of such a bound when one replaces a Hamiltonian
foliation by an integrable foliation of Darboux type. Such a foliation has a ﬁrst integral of the form ∏ P αi
i ,
where the Pi are bivariate polynomials such that the algebraic curves Pi = 0 are invariant for the foliation.
The existence of the uniform bound depends only on the degree of the rational form deﬁning the foliation and
the degree of the pertubation. The difﬁculty of the proof comes from the fact that the Abelian integrals do not
satisfy any more a Picard-Fuchs equation. Also the level curves of the ﬁrst integral are no more nice Riemann
surfaces on which it is possible to extend the Abelian integrals. The method used for the proof is a clever
application of Khovanskii theory. As in the case of the Khovanskii-Varchenko theorem it uses a special study
of the asymptotic expansion of the Abelian integrals in the neighborhood of the polycycles. One difﬁculty is

7

that these extensions can have small denominators. However a solution can be found using the fact that the
singular points in the corners of the polycycles are integrable.
This result opens the new ﬁeld of the study of Abelian integrals appearing in the perturbations of Darboux
integrable systems in several directions. The bound obtained by Novikov is not explicit. Also it is only
obtained under generic conditions on the ﬁrst integral. Two natural generalizations are in the direction of
obtaining explicit bounds under more precise conditions and to generalize to the limit cases of generalized
Darboux integrable systems: these occur when two or more algebraic invariant curves coallesce.

4.3 The ﬁrst space of modulus for a germ of analytic family of vector ﬁelds unfolding
a resonant singularity is identiﬁed.

While it is already known for some years that the Ecalle-Voronin modulus of a germ of diffeomorphism with
a parabolic ﬁxed point or the Martinet-Ramis modulus of a saddle-node can be unfolded to yield a modulus
for the unfolded system, the dependence of the unfolded modulus on the parameter was completely open.
This came from the fact that no construction of this modulus could make a full turn in the parameter. All
constructions yield to multiple descriptions of the modulus for some values of the parameter. The key for
understanding the dependence on the parameter was to express that these two descriptions yielded the same
dynamics. This “compatibility condition” ensures then that the unfolded modulus was 1/2-summable in the
parameter.
This result opens many questions. Several of them are concerned with the generalization to higher codi-
mension. Others concern the applications. For instance what can we say of the indifferent ﬁxed points which
are born by perturbation of a parabolic ﬁxed point. It is certainly interesting to also consider applications to
problems of ﬁnite cyclicity of graphics not satisfying a genericity condition.

The fruitful interactions of the studies of polynomial vector ﬁelds and algebraic dynamical systems. The
common thread between these two domains is the fact that the singularities organize the dynamics. Moreover
the study of singularities of 2-dimensional vector ﬁelds can sometimes be reduced to the study of singularities
of 1-dimensional dynamical systems. Although the workshop produced no speciﬁc output on this particular
item, all participants appreciated the fruitful discussions between the two ﬁelds.

The reduction of the ﬁniteness part of Hilbert’s 16th problem for classical Li´enard equations to the
study of singular perturbations in this family. Classical Li´enard equations are ones for which the tools of
singular perturbations work quite efﬁciently. The reduction performed by Freddy Dumortier and Magdalena
Caubergh opens the hope that a proof of uniform ﬁnte cyclicity be given soon, at least for degrees not too
high.

The better understanding of the leaves of the foliation of a saddle-node. The lecture of Lo¨ıc Teyssier
was particularly impressive with his programming of the leaves in the neighborhood of a saddle-node or an
unfolding of a saddle-node. In particular he illustrated in a brilliant way how the leaves near a hyperbolic
point could have both a node or saddle behaviour depending in which direction we approach the singular
point. Examples of his drawings appear in Figures 1 and 2.

5 Outcome of the Meeting

The meeting was a real success. This was the opinion of al participants. Most of them really appreciated
the broad sense given to the theme and the wide spectrum of expertises. The mixing of specialists from
different areas permitted animated discussions and mixing of ideas during the workshop. Several talks have
been absolutely exceptional in quality, in particular the plenary talks which played the role of presenting a
mature view of the state of the subject. Moreover several participants were hearing for the ﬁrst time the
details of some of the new signiﬁcant results of the subject. Some students and young researchers attended
the workshop and could discuss and exchange with the senior researchers. Two students: Tanya Firsova and
Caroline Lambert gave lectures. Moreover several subgroups used the opportunity to start new work.
 8

|y|
 x
 Figure 1: Modulus of a leaf a vector ﬁeld unfolding a saddle node. The drawing justiﬁes the terms “node
type” (on the left of the ﬁgure) and “saddle type” (on the right) qualifying the singular points.

|y|
 x
 Figure 2: Another view of the same leaf.
 9

While there has been important developments around Hilbert’s 16th problem in the last years, it is clear
that no complete solution is expected in the near future and there is a consensus that new ideas are still needed
in order to make a breakthrough towards a complete solution.

6 Appendix: list of participants and titles of lectures

• Waldo Arriagada-Silva (Montreal)

• Joan C. Art´es (UAB, Barcelona): Quadratic vectors ﬁelds of codimension 1

• Patrick Bonckaert (Hasselt University): Invariant manifolds close to linear non-hyperbolic singulari-
ties

• Magdalena Caubergh (Hasselt University): Large Amplitude Limit Cycles for Li´enard systems

• Rodica Costin (Ohio State): Nonlinear perturbations of Fuchsian systems: linearization criteria and
classiﬁcation

• Freddy Dumortier (Hasselt University): The period function of classical Li´enard equations

• Remy Etoua (Montrea)

• Tanya Firsova (Toronto): Topology of leaves of analytic foliations on Stein manifolds

• Armengol Gasull (UAB Barcelona): Some results on periodic orbits for Abel-type equations

• Alexey Glutsyuk (ENS, Lyon): On density of horospheres in dynamical laminations

• Vadim Kaloshin (Penn. State): Oscillatory motions and instabilities for the planar 3-body problem

• Caroline Lambert (Montreal): Conﬂuence of the hypergeometric equation and Riccati equation

• Jaume Llibre (UAB, Barcelona): On the limit cycles of the Li´enard differential systems

• Pavao Mardesic (Dijon): Inﬁnitesimal and tangential 16-th Hilbert problem

• Abdelraouf Mourtada (Dijon): Hilbert’s 16th problem for hyperbolic polycycles and extension of
Khovanskii-Varchenko theorem to algebraic polycycles

• Dmitry Novikov (Weizmann): Extension of the Varchenko-Khovanskii theorem to the integrable case

• Emmanuel Paul (Toulouse): Galoisian reducibility for a germ of quasi-homogeneous foliation

• Rafel Prohens Sastre(Illes Balears, Spain): On the number of limit cycles of some systems on the
cylinder

• Javier Rib´on (IMPA): Analytic classiﬁcation of unfoldings of resonant diffeomorphisms

• Robert Roussarie (Dijon): Slow-fast systems and Sixteenth Hilbert’s Problem

• Christiane Rousseau (Montr´eal): The space of modules of unfoldings of germs of generic diffeomor-
phisms with a parabolic point

• Reinhard Schfke (Strasbourg): Quasi-analytic solutions of analytic ordinary differential equations and
o-minimal Structures

• Loc Teyssier (Strasbourg): Conﬂuence of singular points in a family of holomorphic vector ﬁelds

• Jordi Villadelprat (Universitat Rovira i Virgili,Spain): A new result on the period function of quadratic
reversible centers

• Jean-Christophe Yoccoz (ENS, Paris): Siegel disks and Julia sets of quadratic polynomials, according
to X.Buff and A.Chritat

• Huaiping Zhu (York): Bifurcation of limit cycles from a Nilpotent Center in a Near-Hamiltonian System

10

References

[1] J.C. Artes, J. Llibre and D. Schlomiuk, The geometry of quadratic differential systems with a weak focus
of second order, Internat. J. Bifur. Chaos Appl. Sci. Engrg. 16 (2006), 3127–3194.

[2] X. Buff and A. Cheritat, Ensembles de Julia quadratiques de mesure de Lebesgue strictement positive, C.
R. Math. Acad. Sci. Paris 341 (2005), 669–674.

[3] C. Christopher and N. Lloyd, Polynomial systems: a lower bound for the Hilbert numbers, Proc. Roy.
Soc. London Ser. A 450 (1995), 219–224.

[4] C. Christopher and C. Rousseau, The moduli space of unfoldings of germs of generic diffeomorphisms
with a paraolic point, Preprint 2007.

[5] F. Dumortier, Y. Ilyashenko, and C. Rousseau, Normal forms near a saddle-node and applications to the
ﬁnite cyclicity of graphics, Ergod. Theor. Dyn. Systems 22 (2002), 783–818.

[6] F. Dumortier. D. Panazzolo and R. Roussarie, More limit cycles than expected in Li´enard equations,
preprint.

[7] F. Dumortier, R. Roussarie, and C. Rousseau, Hilbert’s 16-th problem for quadratic vector ﬁelds, J.
Differential Equations 110 (1994), 86–133.

[8] A. A. Glutsyuk, “Conﬂuence of singular points and nonlinear Stokes phenomenon”, Trans. Moscow
Math. Soc., 62 (2001), 49–95.

[9] D. Hilbert, Mathematische Probleme (lecture), The Second International Congress of Mathematicians,
Paris 1900, Nachr. Ges.Wiss. G¨ottingen Math.-Phys Kl. 1900, 253–297.

[10] Yu. Ilyashenko, Dulac’s memoir ”On limit cycles“ and related topics of the theory of differential equa-
tions, Uspekhi Matematicheskikh Nauk 40 (1985), 41–70.

[11] Yu Ilyashenko, Nonlinear Stokes phenomena Advances in Soviet Mathematics, 14, American Mathe-
matical Society, (1993), 1-55.

[12] Yu Ilyashenko and S. Yakovenko, Finite cyclicity of elementary polycycles, American Mathematical
Society Translations, series 2 165, 1995, 21-95.

[13] P. Mardeˇsi´c, R. Roussarie and C. Rousseau, “Modulus of analytic classiﬁcation for unfoldings of generic
parabolic diffeomorphisms”, Moscow Mathematical Journal, 4 (2004), 455–502.

[14] J. Martinet and J.-P. Ramis, Probl`emes de modules pour des ´equations diff´erentielles non lin´eaires du
premier ordre, Publ. Math., Inst. Hautes Etud. Sci. 55 (1982), 63–164.

[15] D. Novikov, On limit cycles appearing by polynomial perturbation of Darbouxian integrable systems,
preprint.

[16] J.-P. Rolin, F. Sanz and R. Sch¨afke, Quasianalytic solutions of differential equations and o-minimal
structures, preprint.

[17] R. Roussarie, A note on ﬁnite cyclicity and Hilbert’s 16th problem, in Dynamical Systems, Valparaiso
1986 (R Bam´on et al. eds.), Lecture Notes in Math. 1331, Springer-Verlag, Berlin-Heidelberg-New York
1998, 161–168.

[18] C. Rousseau and L. Teyssier, Analytical moduli for unfoldings of saddle-node vector-ﬁelds, preprint,
2007.

[19] L. Teyssier, “ ´Equation homologique et cycles asymptotiques d’une singularit´e nœud-col”, Bulletin des
Sciences Math´ematiques, vol. 128, 3 (2004), 167–187.

[20] L. Teyssier, “Analytical classiﬁcation of singular saddle-node vector ﬁelds”, Journal of Dynamical and
Control Systems, vol. 10, 4 (2004), 577–605.
