<!-- source: https://www.wisdom.weizmann.ac.il/~yakov/thebook.pdf | converted from PDF -->

LECTURES ON ANALYTIC
DIFFERENTIAL EQUATIONS

Yulij Ilyashenko

Sergei Yakovenko

Cornell University, Ithaca, U.S.A.,

Moscow State University,

Steklov Institute of Mathematics, Moscow

Independent University of Moscow, Russia

E-mail address: yulijs@mccme.ru

Weizmann Institute of Science, Rehovot, Israel

E-mail address: sergei.yakovenko@weizmann.ac.il

WWW page: http://www.wisdom.weizmann.ac.il/~yakov

Graduate Studies in Mathematics
2008; 625 pp; hardcover
Volume: 86
ISBN-10: 0-8218-3667-6
ISBN-13: 978-0-8218-3667-5
List Price: US$ 79
Member Price: US$ 63
Order Code: GSM/86

2000 Mathematics Subject Classiﬁcation. Primary 34A26, 34C10;
Secondary 14Q20, 32S65, 13E05

About the book: from the Publisher

The book combines the features of a graduate-level textbook with those
of a research monograph and survey of the recent results on analysis and
geometry of diﬀerential equations in the real and complex domain. As a
graduate textbook, it includes self-contained, sometimes considerably sim-
pliﬁed demonstrations of several fundamental results, which previously ap-
peared only in journal publications (desingularization of planar analytic vec-
tor ﬁelds, existence of analytic separatrices, positive and negative results on
the Riemann-Hilbert problem, Ecalle-Voronin and Martinet-Ramis moduli,
solution of the Poincar´e problem on the degree of an algebraic separatrix,
etc.). As a research monograph, it explores in a systematic way the alge-
braic decidability of local classiﬁcation problems, rigidity of holomorphic
foliations, etc. Each section ends with a collection of problems, partly in-
tended to help the reader to gain understanding and experience with the
material, partly drafting demonstrations of the more recent results surveyed
in the text.

The exposition of the book is mostly geometric, though the algebraic
side of the constructions is also prominently featured. On several occasions
the reader is introduced to adjacent areas, such as intersection theory for
divisors on the projective plane or geometric theory of holomorphic vector
bundles with meromorphic connections. The book provides the reader with
the principal tools of the modern theory of analytic diﬀerential equations
and intends to serve as a standard source for references in this area.

Readership

Graduate students and research mathematicians interested in analysis
and geometry of diﬀerential equations in real and complex domain.

Ordering information: Visit the AMS online bookstore

Draft version is available online

The draft posted on this site is really outdated, with many inaccura-
cies, sloppy phrases and even errors. Besides, a number of sections had been
added or modiﬁed. It sole purpose is to give an idea what appears in the
printed book.

Do not quote this draft to avoid misleading enumeration of pages,
theorems and deﬁnitions.

Contents

Preface ix

Chapter I. Normal forms and desingularization 1

1. Analytic diﬀerential equations in the complex domain 1

2. Holomorphic foliations and their singularities 13

3. Formal ﬂows and embedding theorem 29

4. Formal normal forms 40

5. Holomorphic normal forms 61

6. Finitely generated groups of conformal germs 81

7. Holomorphic invariant manifolds 105

8. Desingularization in the plane 112

Chapter II. Singular points of planar analytic vector ﬁelds 143

9. Planar vector ﬁelds with characteristic trajectories 143

10. Algebraic decidability of local problems and center-focus
alternative 158

11. Holonomy and ﬁrst integrals 177

12. Zeros of parametric families of analytic functions
and small amplitude limit cycles 198

13. Quadratic vector ﬁelds and the Bautin theorem 222

14. Complex separatrices of holomorphic foliations 231

Chapter III. Local and global theory of linear systems 253

15. General facts about linear systems 253

16. Local theory of regular singular points and applications 263

vii

viii Contents

17. Global theory of linear systems: holomorphic vector bundles
and meromorphic connexions 283

18. Riemann–Hilbert problem 310

19. Linear nth order diﬀerential equations 327

20. Irregular singularities and the Stokes phenomenon 348

Appendix: Demonstration of Sibuya theorem 362

Chapter IV. Functional moduli of analytic classiﬁcation of resonant
germs and their applications 371

21. Nonlinear Stokes phenomenon for parabolic and resonant germs
of holomorphic self-maps 371

22. Complex saddles and saddle-nodes 401

23. Nonlinear Riemann–Hilbert problem 425

24. Nonaccumulation theorem for hyperbolic polycycles 438

Chapter V. Global properties of complex polynomial foliations 463

25. Algebraic leaves of polynomial foliations on the complex
projective plane P2 464

Appendix: Foliations with invariant lines and algebraic leaves of
foliations from the class Ar 493

26. Perturbations of Hamiltonian vector ﬁelds and zeros of Abelian
integrals 499

27. Topological classiﬁcation of complex linear foliations 537

28. Global properties of generic polynomial foliations of the complex
projective plane P2 558

First aid 589

A. Crash course on functions of several complex variables 589

B. Elements of the theory of Riemann surfaces. 593

Bibliography 597

Preface

The branch of mathematics which deals with ordinary diﬀerential equations
can be roughly divided into two large parts, qualitative theory of diﬀeren-
tial equations and the dynamical systems theory. The former mostly deals
with systems of diﬀerential equations on the plane, the latter concerns mul-
tidimensional systems (diﬀeomorphisms on two-dimensional manifolds and
ﬂows in dimension greater than two and up to inﬁnity). The former can
be considered as a relatively orderly world, while the latter is the realm of
chaos.

A key problem, in some sense a paradigm inﬂuencing the development
of dynamical systems theory from its origins, is the problem of turbulence:
how a deterministic nature of a dynamical system can be compatible with
its apparently chaotic behavior. This problem was studied by the precursors
and founding fathers of the dynamical systems theory: L. Landau, H. Hopf,
A. Kolmogorov, V. Arnold, S. Smale, D. Ruelle and F. Takens. Currently
this is one of the principal challenges on the crossroad between mathemat-
ics, physics and computer science. Dynamical systems theory heavily uses
methods and tools from topology, diﬀerential geometry, probability, func-
tional analysis and other branches of mathematics.

The qualitative theory of diﬀerential equations is mostly associated with
autonomous systems on the plane and closely related to analytic theory of
ordinary diﬀerential equations. The principal theme is investigation of local
and global topological properties of phase portraits on the plane. One of the
main problems of the whole area is Hilbert’s sixteenth problem, the question
on the number and position of limit cycles of a polynomial vector ﬁeld on the
plane. In a very broad sense this can be assessed as the question: to which

ix

x Preface

extent properties of polynomials deﬁning a diﬀerential equation are inherited
by its absolutely transcendental (and sometimes very weird) solutions.

Another major part of analytic theory of diﬀerential equations is the
linear theory. Here the key problem is Hilbert’s twenty-ﬁrst problem, also
known as the Riemann–Hilbert problem, which has a long dramatic history
and was solved “only yesterday”. Discussion of this problem constitutes an
important part of this book.

The qualitative theory of diﬀerential equations was essentially created in
the works by H. Poincar´e who discovered that diﬀerential equations belong
not only to the realm of analysis, but also to geometry. Deriving geomet-
ric properties of solutions directly from the equations deﬁning them, was
his principal idea. These ideas were further developed in each of the two
branches separately, but their present appearance looks very diﬀerent.

Diﬀerential equations brought into existence such areas of mathematics
as topology and Lie groups theory. In turn, the analytic theory of diﬀerential
equations is not a closed area, but rather provides a source of applications
and motivation for other disciplines. In this book we stress using complex
analysis, algebraic geometry and topology of vector bundles, with some other
interesting links brieﬂy outlined at the appropriate places.

On the frontier between diﬀerential equations and the singularity theory,
lies the notion of a normal form, one of the central concepts of this book. The
ﬁrst chapter contains the basics of formal and analytic normal form theory.
The tools developed in this chapter are systematically used throughout the
book. The study of phase portraits of composite singular points requires
elaboration of the blowing-up technique, another classical tool known for
over a century. The famous Bendixson desingularization theorem is proved
in our textbook by transparent methods.

A new approach to local problems of analysis, based on the notion of
algebraic and analytic solvability, was suggested by V. Arnold and R. Thom
around forty years ago. In Chapter II we treat from this point of view
the local theory of singular points of planar vector ﬁelds. It is proved that
the stability problem and the problem of topological classiﬁcation of planar
vector ﬁelds are algebraically solvable in all cases except for the center/focus
dichotomy. This dichotomy is algebraically unsolvable, as is proved in the
same chapter. Besides these topics, the chapter contains local analysis of
singular points of holomorphic foliations: the proof of the C. Camacho–
P. Sad theorem on existence of analytic separatrices through singular points,
integrability via the local holonomy group as discovered by J.-F. Mattei and
R. Moussu, and demonstration of the Bautin theorem on small limit cycles
of quadratic vector ﬁelds.

Preface xi

The third chapter deals with the linear theory. Somewhat paradoxically,
application of normal forms of nonlinear systems to investigation of linear
systems considerably simpliﬁes exposition of many classical results. The
chapter contains a succinct derivation of some positive and negative results
on solvability of the Riemann–Hilbert problem.

Chapter IV deals with a new direction in the theory of normal forms,
the functional moduli of analytic classiﬁcation of resonant singularities. The
main working tool used in this study is an almost complex structure and
quasiconformal maps. The latter already played a revolutionizing role in the
nearby theory of holomorphic dynamics. The main basic facts from these
theories are brieﬂy summarized in this chapter. The chapter ends with
the proof of the “easy version” of the ﬁniteness theorem for limit cycles of
analytic vector ﬁelds, with an additional assumption that all singular points
are hyperbolic saddles. The proof illustrates the power of using local normal
forms in the solution of problems of a global nature.

Chapter V is concerned with the global theory of polynomial diﬀeren-
tial equations on the real and complex plane, bridging between algebraic,
“almost algebraic” and essentially transcendental questions.

The chapter begins with the solution of the Poincar´e problem on the
maximal degree which can have an algebraic solution of a polynomial dif-
ferential equation (a relatively recent spectacular result due to D. Cerveau,
A. Lins Neto and M. Carnicer). The second section focuses on the interac-
tion between the theory of Riemann surfaces and global theory of diﬀerential
equations. We describe the topology of stratiﬁcation of the complex pro-
jective plane by level curves of a generic bivariate polynomial, including
derivation of the Picard–Lefschetz formulas for the Gauss–Manin connex-
ion. This is the main working tool for deriving certain inequalities for the
number of zeros of complete Abelian integrals, a question very closely re-
lated to Hilbert’s sixteenth problem. Finally, we discuss generic properties
of complex foliations that are very often drastically diﬀerent from their real
counterparts. For instance, ﬁniteness of limit cycles on the real plane is
in sharp contrast with a typically inﬁnite number of the complex limit cy-
cles, and the structural stability of real phase portraits counters rigidity of
a generic complex foliation.

Some basic facts from complex analysis in several variables frequently
used in the book, are recalled in the Appendix.

Almost all sections are ended by the problem lists. Together with easy
problems, sometimes called exercises, the lists contain diﬃcult ones, lying
on the frontier of the current research.

The book was not intended to serve as a comprehensive treatise on the
whole analytic theory of ordinary diﬀerential equations. The selection of

xii Preface

topics was based on the personal taste of the authors and restricted by
the size of the book. We do not even mention such classical areas as the
theory of Riccati and Painlev´e equations, the Malmquist theorem, integral
representations and transformations. We omit completely the diﬀerential
Galois theory, resurgent functions introduced by Ecalle and the fewnomial
theory invented by A. Khovansky. Nevertheless, the subjects covered in the
book constitute in our opinion a connected whole revolving around few key
problems that play an organizing role in the development of the entire area.

Exposition of each topic begins with basic deﬁnitions and reaches the
present-day level of research on many occasions. Traditionally, the proofs of
many results of analytic theory of diﬀerential equations are very technically
involved. Whenever available, we tried to preface formulas by motivations
and avoid as much as possible all cumbersome and nonrevealing computa-
tions.

The book is primarily aimed at graduate students and professionals look-
ing for a quick and gentle initiation into this subject. Yet experts in the area
will ﬁnd here several results whose complete exposition was never published
before in books. On the other hand, undergraduate students should be able
to read at least some parts of the book and get introduced into the beautiful
area that occupies a central position in modern mathematics.

* * *

The idea to write this book, especially the chapter on linear systems,
was to a large extent inspired by the recent dramatic achievements by our
dear friend and colleague Andrei Bolibruch, who solved one of the most
challenging problems of analytic theory of ordinary diﬀerential equations,
the Riemann-Hilbert problem. Andrei read several ﬁrst drafts of this chapter
and his comments and remarks were extremely helpful.

On November 11, 2003, at the age 53, after a long and diﬃcult struggle,
Andrei Andreevich Bolibruch succumbed to the grave disease. This book
is a posthumous tribute to his mathematical talents, artistic vision and
impeccable taste with which he always chose problems and solved them.

* * *

When the work on this book (which took a much longer time than ini-
tially expected) was essentially over, another similar treatise appeared. In
2006 Henryk ˙Zo l¸adek published the fundamental monograph [ ˙Zo l06] titled
very tellingly “The Monodromy Group”. The scope of both books is surpris-
ingly similar, though the symmetric diﬀerence is also very large. Yet most
of the subjects which simultaneously occur in the two books are treated in
rather diﬀerent ways. This gives a reader a rare opportunity to choose the

Preface xiii

exposition that is closer to his/her heart: the mathematics can be the same
but our ways of speaking about it diﬀer.

* * *

Acknowledgements. Many people helped us in diﬀerent ways to im-
prove the manuscript. Our colleagues F. Cano, D. Cerveau, C. Christopher,
A. Glutsyuk, L. Gavrilov, J. Llibre, C. Li, F. Loray, V. Kostov, V. Katsnel-
son, Y. Yomdin explained us delicate points of mathematical constructions
and gave useful advices concerning the exposition.

We are grateful to all those who read preliminary versions of separate sec-
tions and spotted endless errors and typos, among them T. Golenishcheva-
Kutuzova, Yu. Kudryashov, A. Klimenko, D. Ryzhov and M. Prokhorova.
Needless to say, the responsibility for all remaining errors is entirely ours.

The AMS editorial staﬀ was extremely patient and helpful in bringing
the manuscript to its ﬁnal form, including computer graphics. Our profound
gratitude goes to Luann Cole, Lori Nero and especially to Sergei Gelfand
for wise application of moderate physical pressure to ensure the delivery of
the book.

Last but not least, we are immensely grateful to Dmitry Novikov who
assisted us on all stages of the preparation of the manuscript. Without long
discussions with him the book would certainly look very diﬀerent.

During the preparation of the book Yulij Ilyashenko was supported by
the grants NSF no. 0100404 and no. 0400495. Sergei Yakovenko is incumbent
of The Gershon Kekst Professorial Chair. His research was supported by the
Israeli Science Foundation grant no. 18-00/1 and the Minerva Foundation.

Bibliography

[AB60] L. Ahlfors and L. Bers, Riemann’s mapping theorem for variable metrics, Ann.
of Math. (2) 72 (1960), 385–404. MR0115006 (22 #5813)

[AB94] D. V. Anosov and A. A. Bolibruch, The Riemann-Hilbert problem, Vieweg
Publ., Braunschweig, 1994. MR 95d:32024

[AGV85] V. I. Arnold, S. M. Guse˘ın-Zade, and A. N. Varchenko, Singularities of diﬀer-
entiable maps., vol. I. The classiﬁcation of critical points, caustics and wave
fronts, Birkh¨auser Boston Inc., Boston, Mass., 1985. MR 86f:58018

[AGV88] , Singularities of diﬀerentiable maps, vol. II, Monodromy and asymp-
totics of integrals, Birkh¨auser Boston Inc., Boston, MA, 1988. MR 89g:58024

[AI85] V. I. Arnold and Yu. S. Ilyashenko, Ordinary diﬀerential equations, Dynamical
systems—I, Encyclopaedia of Mathematical Sciences, vol. 1, Springer, Berlin,
1985, translated from Current problems in mathematics. Fundamental direc-
tions, Vol. 1, 7–149, VINITI, Moscow, 1985, pp. 1–148. MR 87e:34049

[ALGM73] A. A. Andronov, E. A. Leontovich, I. I. Gordon, and A. G. Ma˘ıer, Qualitative
theory of second-order dynamic systems, Halsted Press (A division of John
Wiley & Sons), New York-Toronto, Ont., 1973. MR 50 #2619

[And62] A. F. Andreev, On Frommer’s method of studying a singular point of a ﬁrst-
order diﬀerential equation, Vestnik Leningrad. Univ. 17 (1962), no. 1, 5–21.
MR 25 #5228

[And65a] , On the number of operations used in Frommer’s method for investiga-
tion of a singular point of a diﬀerential equation, Diﬀerencial
′nye Uravnenija
1 (1965), 1155–1176. MR 32 #5972

[And65b] , Remarks on a paper of S. Lefschetz, Diﬀerencial
′nye Uravnenija 1
(1965), 199–203. MR 33 #2865

[Arn69] V. I. Arnold, Remarks on singularities of ﬁnite codimension in complex dy-
namical systems, Functional Anal. Appl. 3 (1969), no. 1, 1–5. MR 41 #4573

[Arn70a] , Algebraic unsolvability of the problem of Ljapunov stability and the
problem of the topological classiﬁcation of the singular points of an analytic
system of diﬀerential equations, Funkcional. Anal. i Priloˇzen. 4 (1970), no. 3,
1–9. MR 42 #7989
 597

598 Bibliography

[Arn70b] , Local problems of analysis, Vestnik Moskov. Univ. Ser. I Mat. Meh.
25 (1970), no. 2, 52–56. MR 43 #633

[Arn78] , Ordinary diﬀerential equations, MIT Press, Cambridge, Mass., 1978.
MR 58 #22707

[Arn83] , Geometrical methods in the theory of ordinary diﬀerential equations,
Springer-Verlag, New York, 1983. MR 84d:58023

[Arn92] , Ordinary diﬀerential equations, Springer-Verlag, Berlin, 1992. MR
93b:34001

[Arn97] , Mathematical methods of classical mechanics, Graduate Texts in
Mathematics, vol. 60, Springer-Verlag, New York, 1997, Corrected reprint
of the second (1989) edition. MR1345386 (96c:70001)

[Arn04] , Arnold’s problems, Springer-Verlag, Berlin, 2004, Translated and re-
vised edition of the 2000 Russian original, With a preface by V. Philippov, A.
Yakivchik and M. Peters. MR2078115 (2005c:58001)

[AVL91] D. V. Alekseevski˘ı, A. M. Vinogradov, and V. V. Lychagin, Basic ideas
and concepts of diﬀerential geometry, Geometry, I, Encyclopaedia Math. Sci.,
vol. 28, Springer, Berlin, 1991, pp. 1–264. MR 95i:53001b

[Bau39] N. Bautin, Du nombre de cycles limites naissant en cas de variation des co-
eﬃcients d’un ´etat d’´equilibre du type foyer ou centre, C. R. (Doklady) Acad.
Sci. URSS (N. S.) 24 (1939), 669–672. MR 2,49a

[Bau54] N. N. Bautin, On the number of limit cycles which appear with the variation
of coeﬃcients from an equilibrium position of focus or center type, American
Math. Soc. Translation 1954 (1954), no. 100, 19. MR 15,527h

[BBI01] D. Burago, Yu. Burago, and S. Ivanov, A course in metric geometry, Graduate
Studies in Mathematics, vol. 33, American Mathematical Society, Providence,
RI, 2001. MR1835418 (2002e:53053)

[BC93] M. Berthier and D. Cerveau, Quelques calculs de cohomologie relative, Ann.
Sci. ´Ecole Norm. Sup. (4) 26 (1993), no. 3, 403–424. MR1222279 (94k:32053)

[BCLN96] M. Berthier, D. Cerveau, and A. Lins Neto, Sur les feuilletages analytiques
r´eels et le probl`eme du centre, J. Diﬀerential Equations 131 (1996), no. 2,
244–266. MR 98a:58128

[BD00] P. Bonnet and A. Dimca, Relative diﬀerential forms and complex polynomials,
Bull. Sci. Math. 124 (2000), no. 7, 557–571. MR 1 793 909

[Bel79] G. R. Belitski˘ı, Normal~nye formy, invarianty i lokal~nye oto-
braˇeni˜ (Normal forms, invariants and local maps), “Naukova Dumka”,
Kiev, 1979, in Russian. MR 81h:58014

[Ben01] I. Bendixson, Sur les courbes d´eﬁnies par des ´equations diﬀ´erentielles, Acta
Math. 24 (1901), 1–88.

[Bib79] Yu. N. Bibikov, Local theory of nonlinear analytic ordinary diﬀerential equat-
ions, Lecture Notes in Mathematics, vol. 702, Springer-Verlag, Berlin, 1979.
MR 83a:34004

[BL88] J. Bernstein and V. Lunts, On nonholonomic irreducible D-modules, Invent.
Math. 94 (1988), no. 2, 223–243. MR958832 (90b:58247)

[BLL97] M. Belliart, I. Liousse, and F. Loray, Sur l’existence de points ﬁxes attractifs
pour les sous-groupes de Aut(C,0), C. R. Acad. Sci. Paris S´er. I Math. 324
(1997), no. 4, 443–446. MR1440964 (98c:58134)

Bibliography 599

[BM94] M. Berthier and R. Moussu, R´eversibilit´e et classiﬁcation des centres nilpo-
tents, Ann. Inst. Fourier (Grenoble) 44 (1994), no. 2, 465–494. MR1296740
(95h:58103)
[Bol92] A. A. Bolibruch, Suﬃcient conditions for the positive solvability of the
Riemann-Hilbert problem, Mat. Zametki 51 (1992), no. 2, 9–19, 156. MR
93g:34007
[Bol94] , On an analytic transformation to the standard Birkhoﬀ form, Trudy
Mat. Inst. Steklov. 203 (1994), 33–40. MR 97c:34066
[Bol00] , Fuchsian diﬀerential equations and holomorphic vector bundles, Mod-
ern lecture courses, Moscow Center for Continuous Mathematical Education,
Moscow, 2000, (Russian).
[Bon99] P. Bonnet, Description of the module of relatively exact 1-forms modulo a
polynomial f on C2, Preprint no. 184, Laboratoire de Topologie, Universit´e
de Bourgogne, Dijon, 1999.
[Bru71] N. N. Brushlinskaya, A ﬁniteness theorem for families of vector ﬁelds in the
neighborhood of a singular point of Poincar´e type, Funkcional. Anal. i Priloˇzen.
5 (1971), no. 3, 10–15. MR 45 #8920
[BV89] D. G. Babbitt and V. S. Varadarajan, Local moduli for meromorphic diﬀeren-
tial equations, Ast´erisque (1989), no. 169-170, 217. MR1014083 (91e:32017)
[Can97] J. Cano, Construction of invariant curves for singular holomorphic vector
ﬁelds, Proc. Amer. Math. Soc. 125 (1997), no. 9, 2649–2650. MR 97j:32027
[Car38] H. Cartan, Sur le premier probl`eme de Cousin, C. R. Acad. Sci. Paris 207
(1938), 558–560.
[Car94] M. Carnicer, The Poincar´e problem in the nondicritical case, Ann. of Math.
(2) 140 (1994), no. 2, 289–294. MR1298714 (95k:32031)
[CC03] A. Candel and L. Conlon, Foliations. I, II, Graduate Studies in Mathemat-
ics, vol. 23, 60, American Mathematical Society, Providence, RI, 2000, 2003.
MR1732868 (2002f:57058), MR1994394 (2004e:57034)
[CG93] L. Carleson and T. W. Gamelin, Complex dynamics, Universitext: Tracts in
Mathematics, Springer-Verlag, New York, 1993. MR 94h:30033
[Cha86] M. Chaperon, C k-conjugacy of holomorphic ﬂows near a singularity, Inst.
Hautes ´Etudes Sci. Publ. Math. (1986), no. 64, 143–183. MR 88m:58161
[Chi89] E. M. Chirka, Complex analytic sets, Mathematics and its Applications (Soviet
Series), vol. 46, Kluwer, Dordrecht, 1989. MR 92b:32016
[CKP76] C. Camacho, N. H. Kuiper, and J. Palis, La topologie du feuilletage d’un champ
de vecteurs holomorphes pr`es d’une singularit´e, C. R. Acad. Sci. Paris S´er. A-B
282 (1976), no. 17, Ai, A959–A961. MR 54 #1301
[CKP78] , The topology of holomorphic ﬂows with singularity., Publ. Math., Inst.
Hautes Etud. Sci. 48 (1978), 5–38 (English).
[CL00] C. Christopher and J. Llibre, Integrability via invariant algebraic curves for
planar polynomial diﬀerential systems, Ann. Diﬀerential Equations 16 (2000),
no. 1, 5–19. MR1768817 (2001g:34001)
[CLN91] D. Cerveau and A. Lins Neto, Holomorphic foliations in CP(2) having an
invariant algebraic curve, Ann. Inst. Fourier (Grenoble) 41 (1991), no. 4, 883–
903. MR1150571 (93b:32050)
[CLNS84] C. Camacho, A. Lins Neto, and P. Sad, Topological invariants and equidesin-
gularization for holomorphic vector ﬁelds, J. Diﬀerential Geom. 20 (1984),
no. 1, 143–174. MR772129 (86d:58080)

600 Bibliography

[CLO97] D. Cox, J. Little, and D. O’Shea, Ideals, varieties, and algorithms, second ed.,
Undergraduate Texts in Mathematics, Springer-Verlag, New York, 1997, An
introduction to computational algebraic geometry and commutative algebra.
MR 97h:13024

[CLP07] Colin Christopher, Jaume Llibre, and Jorge Vit´orio Pereira, Multiplicity of
invariant algebraic curves in polynomial vector ﬁelds, Paciﬁc J. Math. 229
(2007), no. 1, 63–117. MR2276503

[CNR00] A. Capani, G. Niesi, and L. Robbiano, CoCoA, a system for doing computations
in commutative algebra, Available from ftp://cocoa.dima.unige.it, 2000,
version 4.0.

[CS82] C. Camacho and P. Sad, Invariant varieties through singularities of holomor-
phic vector ﬁelds, Ann. of Math. (2) 115 (1982), no. 3, 579–595. MR 83m:58062

[CW79] Lan Sun Chen and Ming Shu Wang, The relative position, and the number, of
limit cycles of a quadratic diﬀerential system, Acta Math. Sinica 22 (1979),
no. 6, 751–758. MR559742 (81g:34031)

[DFN85] B. A. Dubrovin, A. T. Fomenko, and S. P. Novikov, Modern geometry—
methods and applications. Part II, Graduate Texts in Mathematics, vol. 104,
Springer-Verlag, New York, 1985, The geometry and topology of manifolds.
MR807945 (86m:53001)

[Dul08] H. Dulac, D´etermination and int´egration d’une certaine classe d’´equations
diﬀ´erentielles ayant pour point singulier un centre, Bull. Sci. Math., S´er. 2 32
(1908), no. 1, 230–252.

[Dul23] , Sur les cycles limites, Bull. Soc. Math. France 51 (1923), 45–188.

[Dum77] F. Dumortier, Singularities of vector ﬁelds on the plane, J. Diﬀerential Equat-
ions 23 (1977), no. 1, 53–106. MR 58 #31276

[Dum93] , Techniques in the theory of local bifurcations: blow-up, normal forms,
nilpotent bifurcations, singular perturbations, Bifurcations and periodic orbits
of vector ﬁelds (Montreal, PQ, 1992), NATO Adv. Sci. Inst. Ser. C Math.
Phys. Sci., vol. 408, Kluwer Acad. Publ., Dordrecht, 1993, pp. 19–73. MR
94j:58123

[Ebe07] W. Ebeling, Functions of several complex variables and their singularities,
Graduate Studies in Mathematics, vol. 83, American Mathematical Society,
Providence, RI, 2007. MR2319634

[Eca85] J. Ecalle, Les fonctions r´esurgentes. Tome III, Publications Math´ematiques
d’Orsay, vol. 85, Universit´e de Paris-Sud, D´epartement de Math´ematiques,
Orsay, 1985. MR852210 (87k:32009)

[Eca92] J. Ecalle, Introduction aux fonctions analysables et preuve constructive de la
conjecture de Dulac, Hermann, Paris, 1992. MR 97f:58104

[Edw79] R. E. Edwards, Fourier series. A modern introduction. Vol. 1, second ed.,
Graduate Texts in Mathematics, vol. 64, Springer-Verlag, New York, 1979.
MR 80j:42001

[EISV93] P. M. Elizarov, Yu. S. Ilyashenko, A. A. Shcherbakov, and S. M. Voronin,
Finitely generated groups of germs of one-dimensional conformal mappings,
and invariants for complex singular points of analytic foliations of the complex
plane, Nonlinear Stokes phenomena, Adv. Soviet Math., vol. 14, Amer. Math.
Soc., Providence, RI, 1993, pp. 57–105. MR 94e:32055

[Eli88] P. M. Elizarov, The orbital topological classiﬁcation of analytic diﬀerential
equations in a neighborhood of a degenerate elementary singular point in the

Bibliography 601

two-dimensional complex plane, Trudy Sem. Petrovsk. (1988), no. 13, 137–165,
257. MR961432 (90b:58198)

[FG02] K. Fritzsche and H. Grauert, From holomorphic functions to complex mani-
folds, Graduate Texts in Mathematics, vol. 213, Springer-Verlag, New York,
2002. MR1893803 (2003g:32001)

[Fir06] T. Firsova, Topology of analytic foliations in C2. The Kupka-Smale property,
Proceedings of the Steklov Institute, vol. 254, 2006, pp. 152–168.

[FLLL89] W. W. Farr, Chengzhi Li, I. S. Labouriau, and W. F. Langford, Degenerate
Hopf bifurcation formulas and Hilbert’s 16th problem, SIAM J. Math. Anal.
20 (1989), no. 1, 13–30. MR 90g:58085

[FM98] I. Feldman and A. Markus, On some properties of factorization indices, Inte-
gral Equations Operator Theory 30 (1998), no. 3, 326–337. MR 99f:47023

[For91] O. Forster, Lectures on Riemann surfaces, Springer-Verlag, New York, 1991.
MR 93h:30061

[Fra96] J. P. Fran¸coise, Successive derivatives of a ﬁrst return map, application to the
study of quadratic vector ﬁelds, Ergodic Theory Dynam. Systems 16 (1996),
no. 1, 87–96. MR1375128 (97a:58131)

[FY97] J.-P. Francoise and Y. Yomdin, Bernstein inequalities and applications to an-
alytic geometry and diﬀerential equations, J. Funct. Anal. 146 (1997), no. 1,
185–205. MR 98h:34009c

[Gan59] F. R. Gantmacher, The theory of matrices. Vols. 1, 2, Chelsea Publishing Co.,
New York, 1959. MR 21 #6372c

[Gav98] L. Gavrilov, Petrov modules and zeros of Abelian integrals, Bull. Sci. Math.
122 (1998), no. 8, 571–584. MR 99m:32043

[Gav05] Lubomir Gavrilov, Higher order Poincar´e-Pontryagin functions and iterated
path integrals, Ann. Fac. Sci. Toulouse Math. (6) 14 (2005), no. 4, 663–682.
MR2188587 (2006i:34074)

[GH78] P. Griﬃths and J. Harris, Principles of algebraic geometry, Wiley-Interscience
[John Wiley & Sons], New York, 1978, Pure and Applied Mathematics. MR
80b:14001

[GI06] A. Glutsyuk and Yu. Ilyashenko, Restricted inﬁnitesimal Hilberts Sixteenth
Problem, Doklady Mathematics 73 (2006), no. 2, 185–189.

[GI07] , Restricted Version of the Inﬁnitesimal Hilbert 16th Problem, Moscow
Math. J. 7 (2007), no. 2, 281–325.

[GK60] I. C. Gohberg and M. G. Kre˘ın, Systems of integral equations on a half line with
kernels depending on the diﬀerence of arguments, Amer. Math. Soc. Transl.
(2) 14 (1960), 217–287. MR 22 #3954

[GK06] T. Golenishcheva-Kutuzova, A generic analytic foliation in C2 has inﬁnitely
many cylindrical leaves, Proceedings of the Steklov Institute, vol. 254, 2006,
pp. 180–183.

[GLCP96] J.-M. Gambaudo, P. Le Calvez, and ´E. P´ecou, Une g´en´eralisation d’un
th´eor`eme de Naishul, C. R. Acad. Sci. Paris S´er. I Math. 323 (1996), no. 4,
397–402. MR1408775 (97h:58096)

[Glu06] A. A. Glutsyuk, An explicit formula for period determinant, Annales de
l’institut Fourier 56 (2006), no. 4, 887–917.

[GM88] X. G´omez-Mont, The transverse dynamics of a holomorphic ﬂow, Ann. of
Math. (2) 127 (1988), no. 1, 49–92. MR924673 (89d:32049)

602 Bibliography

[GM89] , Unfoldings of holomorphic foliations, Publ. Mat. 33 (1989), no. 3,
501–515. MR1038486 (91d:32026)

[GR65] R. Gunning and H. Rossi, Analytic functions of several complex variables,
Prentice-Hall Inc., Englewood Cliﬀs, N.J., 1965. MR 31 #4927

[Gra62] H. Grauert, ¨Uber Modiﬁkationen und exzeptionelle analytische Mengen, Math.
Ann. 146 (1962), 331–368. MR0137127 (25 #583)

[Gro62] D. M. Grobman, Topological classiﬁcation of neighborhoods of a singularity in
n-space, Mat. Sb. (N.S.) 56 (98) (1962), 77–94. MR 25 #2270

[Guc72] J. Guckenheimer, Hartman’s theorem for complex ﬂows in the Poincar´e do-
main, Compositio Math. 24 (1972), 75–82. MR 46 #920

[Har82] P. Hartman, Ordinary diﬀerential equations, second (reprinted) ed.,
Birkh¨auser, Boston, Mass., 1982.

[Her63] M. Herv´e, Several complex variables. Local theory, Published for the Tata Insti-
tute of Fundamental Research, Bombay by Oxford University Press, London,
1963. MR 27 #1616

[Hil00] D. Hilbert, Mathematical problems, Bull. Amer. Math. Soc. (N.S.) 37 (2000),
no. 4, 407–436, Reprinted from Bull. Amer. Math. Soc. 8 (1902), 437–479.

[HKM61] M. Hukuhara, T. Kimura, and T. Matuda, Equations diﬀ´erentielles ordinaires
du premier ordre dans le champ complexe, Publications of the Mathemati-
cal Society of Japan, 7. The Mathematical Society of Japan, Tokyo, 1961.
MR0124549 (23 #A1861)

[H¨or00] L. H¨ormander, An introduction to complex analysis in several variables, 2nd
ed., North Holland, 2000.

[HRT99] H. Hauser, J.-J. Risler, and B. Teissier, The reduced Bautin index of planar
vector ﬁelds, Duke Math. J. 100 (1999), no. 3, 425–445. MR 2001f:34054

[Ily69] Yu. S. Ilyashenko, Vozniknovenie predel~nyh ciklov pro vozmuwenii
uravneni˜ dw/dz = −Rz/Rw, gde R(z, w)—mnogoqlen (Appearance of limit
cycles by perturbation of the equation dw/dz = −Rz/Rw, where R(z, w) is a
polynomial ), Mat. Sbornik (New Series) 78 (120) (1969), no. 3, 360–373.

[Ily72a] , Algebraic unsolvability and almost algebraic solvability of the problem
for the center-focus, Funkcional. Anal. i Priloˇzen. 6 (1972), no. 3, 30–37. MR
47 #3749

[Ily72b] , Foliations by analytic curves, Mat. Sb. (N.S.) 88 (130) (1972), 558–
577. MR 47 #503

[Ily77] , Remarks on the topology of the singular points of analytic diﬀeren-
tial equations in a complex domain, and Ladis’ theorem, Funkcional. Anal. i
Priloˇzen. 11 (1977), no. 2, 28–38, 95. MR 56 #755

[Ily78] , Topology of phase portraits of analytic diﬀerential equations on a com-
plex projective plane, Trudy Sem. Petrovsk. (1978), no. 4, 83–136. MR524528
(84k:58164)

[Ily79a] , Divergence of series that reduce an analytic diﬀerential equation to
linear normal form at a singular point, Funktsional. Anal. i Prilozhen. 13
(1979), no. 3, 87–88. MR 82d:34007

[Ily79b] , Global and local aspects of the theory of complex diﬀerential equations,
Proceedings of the International Congress of Mathematicians, Helsinki, 1978
(Berlin), vol. 2, Springer–Verlag, 1979, pp. 821–826.

Bibliography 603

[Ily84] , Limit cycles of polynomial vector ﬁelds with nondegenerate singular
points on the real plane, Functional Anal. Appl. 18 (1984), no. 3, 199–209.
MR757247 (86a:34054)

[Ily85] , Dulac’s memoir “On limit cycles” and related questions of the local
theory of diﬀerential equations, Uspekhi Mat. Nauk 40 (1985), no. 6(246),
41–78, 199. MR 87j:34052

[Ily91] , Finiteness theorems for limit cycles, American Mathematical Society,
Providence, RI, 1991. MR 92k:58221

[Ily02] Yu. Ilyashenko, Centennial history of Hilbert’s 16th problem, Bull. Amer.
Math. Soc. (N.S.) 39 (2002), no. 3, 301–354 (electronic). MR1898209
(2003c:34001)

[Ily04] Yu. S. Ilyashenko, Three gems in the theory of linear diﬀerential equations
(in the work of A. A. Bolibrukh), Uspekhi Mat. Nauk 59 (2004), no. 6(360),
73–84. MR2138468 (2006j:34015)

[Inc44] E. L. Ince, Ordinary Diﬀerential Equations, Dover Publications, New York,
1944. MR 6,65f

[IY91] Yu. Ilyashenko and S. Yakovenko, Finitely smooth normal forms of local fam-
ilies of diﬀeomorphisms and vector ﬁelds, Uspekhi Mat. Nauk 46 (1991),
no. 1(277), 3–39, 240. MR 92i:58165

[IY95] , Finite cyclicity of elementary polycycles in generic families, Con-
cerning the Hilbert 16th problem, Amer. Math. Soc., Providence, RI, 1995,
pp. 21–95. MR 96f:34042

[IY96] , Counting real zeros of analytic functions satisfying linear ordinary
diﬀerential equations, J. Diﬀerential Equations 126 (1996), no. 1, 87–105. MR
97a:34010

[Kal03] V. Kaloshin, The existential Hilbert 16-th problem and an estimate for cyclic-
ity of elementary polycycles, Invent. Math. 151 (2003), no. 3, 451–512.
MR1961336 (2004e:34054)

[Kel67] A. Kelley, The stable, center-stable, center, center-unstable, unstable mani-
folds, J. Diﬀerential Equations 3 (1967), 546–570. MR 36 #4096

[Kho91] A. Khovanskii, Fewnomials, American Mathematical Society, Providence, RI,
1991. MR 92h:14039

[Kle95] O. Kleban, Order of the topologically suﬃcient jet of a smooth vector ﬁeld on
the real plane at a singular point of ﬁnite multiplicity, Concerning the Hilbert
16th problem, Amer. Math. Soc. Transl. Ser. 2, vol. 165, Amer. Math. Soc.,
Providence, RI, 1995, pp. 131–153. MR 96d:58095

[Kos92] V. P. Kostov, Fuchsian linear systems on CP 1 and the Riemann-Hilbert prob-
lem, C. R. Acad. Sci. Paris S´er. I Math. 315 (1992), no. 2, 143–148. MR
94a:34007

[KP06] I. A. Khovanskaya (Pushkar
′), The weakened inﬁnitesimal Hilbert 16th prob-
lem, Tr. Mat. Inst. Steklova 254 (2006), no. Nelinein. Anal. Diﬀer. Uravn.,
215–246. MR2301007

[Kra97] I. S. Krasil
′shchik, Calculus over commutative algebras: a concise user guide,
Acta Appl. Math. 49 (1997), no. 3, 235–248, Algebraic aspects of diﬀerential
calculus. MR 1 603 164

[KY96] A. Khovanskii and S. Yakovenko, Generalized Rolle theorem in Rn and C, J.
Dynam. Control Systems 2 (1996), no. 1, 103–123. MR 97f:26016

604 Bibliography

[Lad77] N. N. Ladis, Topological equivalence of hyperbolic linear systems,
Diﬀerencial
′nye Uravnenija 13 (1977), no. 2, 255–264, 379–380. MR 58 #1396
[Lad79] , The integral curve of a complex homogeneous equation,
Diﬀerentsial
′nye Uravneniya 15 (1979), no. 2, 246–251, 380. MR527325
(80d:34009)
[Lef56] S. Lefschetz, On a theorem of Bendixson, Bol. Soc. Mat. Mexicana (2) 1 (1956),
13–27. MR 18,481g
[Lef68] , On a theorem of Bendixson, J. Diﬀerential Equations 4 (1968), 66–
101. MR 36 #2879
[Lev80] B. Ja. Levin, Distribution of zeros of entire functions, revised ed., Transla-
tions of Mathematical Monographs, vol. 5, American Mathematical Society,
Providence, R.I., 1980. MR 81k:30011
[Lor99] F. Loray, Cinq le¸cons sur la structure transverse d’une singularit´e de feuil-
letage holomorphe en dimension 2 complexe, vol. 1, Cursos de integraci´on y
monograf´ıas de la Red Europea “Singularidades de ecuaciones diferenciales y
foliaciones”, Tordesillas, 1999.
[Lor06] , A preparation theorem for codimension-one foliations, Ann. of Math.
(2) 163 (2006), no. 2, 709–722. MR2199230
[LR03] F. Loray and J. C. Rebelo, Minimal, rigid foliations by curves on CPn, J. Eur.
Math. Soc. (JEMS) 5 (2003), no. 2, 147–201. MR1985614
[Mar91] P. Mardeˇsi´c, An explicit bound for the multiplicity of zeros of generic Abelian
integrals, Nonlinearity 4 (1991), no. 3, 845–852. MR1124336 (92h:58163)
[Med06] N. B. Medvedeva, On the analytic solvability of the problem of distinguishing
between center and focus, Trudy Mat. Inst. Steklov. 256 (2006), 7–93.
[Mil99] J. Milnor, Dynamics in one complex variable, Friedr. Vieweg & Sohn, Braun-
schweig, 1999, Introductory lectures. MR1721240 (2002i:37057)
[Mir95] R. Miranda, Algebraic curves and Riemann surfaces, Graduate Studies in
Mathematics, vol. 5, American Mathematical Society, Providence, RI, 1995.
MR1326604 (96f:14029)
[MM80] J.-F. Mattei and R. Moussu, Holonomie et int´egrales premi`eres, Ann. Sci.
´Ecole Norm. Sup. (4) 13 (1980), no. 4, 469–523. MR 83b:58005
[MMJR97] P. Mardeˇsi´c, L. Moser-Jauslin, and C. Rousseau, Darboux linearization and
isochronous centers with a rational ﬁrst integral, J. Diﬀerential Equations 134
(1997), no. 2, 216–268. MR1432095 (98h:34061)
[Mou82] R. Moussu, Une d´emonstration g´eom´etrique d’un th´eor`eme de Lyapunov-
Poincar´e, Bifurcation, ergodic theory and applications (Dijon, 1981),
Ast´erisque, vol. 98, Soc. Math. France, Paris, 1982, pp. 216–223. MR 85g:58012
[Mou98] , Sur l’existence d’int´egrales premi`eres holomorphes, Ann. Scuola
Norm. Sup. Pisa Cl. Sci. (4) 26 (1998), no. 4, 709–717. MR1648570 (99i:32040)
[MR83] J. Martinet and J.-P. Ramis, Classiﬁcation analytique des ´equations
diﬀ´erentielles non lin´eaires r´esonnantes du premier ordre, Ann. Sci. ´Ecole
Norm. Sup. (4) 16 (1983), no. 4, 571–621 (1984). MR740592 (86k:34034)
[Mum76] D. Mumford, Algebraic geometry. I, Springer-Verlag, Berlin, 1976, Complex
projective varieties, Grundlehren der Mathematischen Wissenschaften, No.
221. MR0453732 (56 #11992)
[Na˘ı81] V. A. Na˘ıshul
′, Topological equivalence of diﬀerential equations in C
2 and
CP 2, Vestnik Moskov. Univ. Ser. I Mat. Mekh. (1981), no. 4, 8–11, 84.
MR631498 (83g:34042)

Bibliography 605

[Na˘ı82] , Topological invariants of analytic and area-preserving mappings and
their application to analytic diﬀerential equations in C
2 and CP 2, Trudy
Moskov. Mat. Obshch. 44 (1982), 235–245. MR656288 (84f:58092)

[Nak94] I. Nakai, Separatrices for nonsolvable dynamics on C, 0, Ann. Inst. Fourier
(Grenoble) 44 (1994), no. 2, 569–599. MR1296744 (95j:58124)

[NN57] A. Newlander and L. Nirenberg, Complex analytic coordinates in almost com-
plex manifolds, Ann. of Math. (2) 65 (1957), 391–404. MR0088770 (19,577a)

[Nov02] D. Novikov, Modules of Abelian integrals and Picard-Fuchs systems, Nonlin-
earity 15 (2002), no. 5, 1435–1444.

[NS60] V. V. Nemytskii and V. V. Stepanov, Qualitative theory of diﬀerential equat-
ions, Princeton Mathematical Series, No. 22, Princeton University Press,
Princeton, N.J., 1960, Reprinted by Dover Publications in 1989. MR0121520
(22 #12258)

[NY99] D. Novikov and S. Yakovenko, Trajectories of polynomial vector ﬁelds and
ascending chains of polynomial ideals, Ann. Inst. Fourier (Grenoble) 49 (1999),
no. 2, 563–609. MR 2001h:32054

[NY01] , Redundant Picard-Fuchs system for Abelian integrals, J. Diﬀerential
Equations 177 (2001), no. 2, 267–306. MR 1 876 646

[NY03] , Quasialgebraicity of Picard–Vessiot ﬁelds, Mosc. Math. J. 3 (2003),
no. 2, 551–591.

[NY04] , Lectures on meromorphic ﬂat connections, Normal forms, bifurcations
and ﬁniteness problems in diﬀerential equations, NATO Sci. Ser. II Math.
Phys. Chem., vol. 137, Kluwer Acad. Publ., Dordrecht, 2004, pp. 387–430.
MR2085816 (2005f:34255)

[OB96] L. Ortiz Bobadilla, Topological equivalence of linear autonomous equations in
C m with Jordan blocks, Trans. Moscow Math. Soc. 57 (1996), 67–91. MR
99a:58127

[Otr54] N. F. Otrokov, On the number of limit cycles of a diﬀerential equation in the
neighborhood of a singular point, Mat. Sbornik N.S. 34(76) (1954), 127–144.
MR0063506 (16,130f)

[Per01] L. Perko, Diﬀerential equations and dynamical systems, third ed., Texts in
Applied Mathematics, vol. 7, Springer-Verlag, New York, 2001. MR1801796
(2001k:34001)

[Pet96] I. G. Petrowsky, Selected works. Part II; diﬀerential equations and probability
theory, Classics of Soviet Mathematics, vol. 5, Gordon and Breach Publishers,
Amsterdam, 1996. MR1677648 (99m:01106b)

[Pha67] F. Pham, Introduction `a l’´etude topologique des singularit´es de Landau,
M´emorial des Sciences Math´ematiques, Fasc. 164, Gauthier-Villars ´Editeur,
Paris, 1967. MR0229263 (37 #4837)

[PL55] I. G. Petrovski˘ı and E. M. Landis, On the number of limit cycles of the equation
dy/dx = P (x, y)/Q(x, y), where P and Q are polynomials of 2nd degree, Mat.
Sb. N.S. 37(79) (1955), 209–250. MR 17,364d

[PL57] , On the number of limit cycles of the equation dy/dx =
P (x, y)/Q(x, y), where P and Q are polynomials, Mat. Sb. N.S. 43(85) (1957),
149–168. MR 19,746c

[Ple64] J. Plemelj, Problems in the sense of Riemann and Klein, Interscience Pub-
lishers John Wiley & Sons Inc. New York-London-Sydney, 1964, Interscience
Tracts in Pure and Applied Mathematics, No. 16. MR 30 #5008

606 Bibliography

[PM01] R. P´erez-Marco, Total convergence or general divergence in small divisors,
Comm. Math. Phys. 223 (2001), no. 3, 451–464. MR 2003d:37063

[PMY94] R. P´erez Marco and J.-C. Yoccoz, Germes de feuilletages holomorphes `a
holonomie prescrite, Ast´erisque (1994), no. 222, 7, 345–371, Complex ana-
lytic methods in dynamical systems (Rio de Janeiro, 1992). MR 96b:58090

[Poi90] H. Poincar´e, Sur le probl`eme des trois corps et les ´equations de la dynamique,
Acta Math. XIII (1890), 1–270.

[Pon34] L. Pontryagin, On dynamical systems close to hamiltonian ones, Zh. Exp. &
Theor. Phys. 4 (1934), no. 8, 234–238.

[PS70a] J. Palis and S. Smale, Structural stability theorems, Global Analysis (Proc.
Sympos. Pure Math., Vol. XIV, Berkeley, Calif., 1968), Amer. Math. Soc.,
Providence, R.I., 1970, pp. 223–231. MR 42 #2505

[PS70b] C. Pugh and M. Shub, Linearization of normally hyperbolic diﬀeomorphisms
and ﬂows, Invent. Math. 10 (1970), 187–198. MR 44 #1055

[Pus97] I. A. Pushkar
′, A multidimensional generalization of Il′yashenko’s theorem on
abelian integrals, Funktsional. Anal. i Prilozhen. 31 (1997), no. 2, 34–44, 95.
MR 98k:58183

[Rou89] R. Roussarie, Cyclicit´e ﬁnie des lacets et des points cuspidaux, Nonlinearity 2
(1989), no. 1, 73–117. MR980858 (90m:58169)

[Rou98] , Bifurcation of planar vector ﬁelds and Hilbert’s sixteenth problem,
Birkh¨auser Verlag, Basel, 1998. MR 99k:58129

[RY97] N. Roytwarf and Y. Yomdin, Bernstein classes, Ann. Inst. Fourier (Grenoble)
47 (1997), no. 3, 825–858. MR 98h:34009a

[Sad87] P. Sad, Central eigenvalues of complex saddle-nodes, Dynamical systems and
bifurcation theory (Rio de Janeiro, 1985), Pitman Res. Notes Math. Ser., vol.
160, Longman Sci. Tech., Harlow, 1987, pp. 387–397. MR907900 (88k:58133)

[Sav82] V. I. Savel
′ev, Zero-type imbedding of a sphere into complex surfaces, Vest-
nik Moskov. Univ. Ser. I Mat. Mekh. (1982), no. 4, 28–32, 85. MR671883
(84d:32007)

[Sch93] D. Schlomiuk, Algebraic and geometric aspects of the theory of polynomial
vector ﬁelds, Bifurcations and periodic orbits of vector ﬁelds (Montreal, PQ,
1992), NATO Adv. Sci. Inst. Ser. C Math. Phys. Sci., vol. 408, Kluwer Acad.
Publ., Dordrecht, 1993, pp. 429–467. MR 95a:34042

[Sch04] , Aspects of planar polynomial vector ﬁelds: global versus local, real
versus complex, analytic versus algebraic and geometric, Normal forms, bifur-
cations and ﬁniteness problems in diﬀerential equations, NATO Sci. Ser. II
Math. Phys. Chem., vol. 137, Kluwer Acad. Publ., Dordrecht, 2004, pp. 471–
509. MR2085818 (2005f:34081)

[Sei68] A. Seidenberg, Reduction of singularities of the diﬀerential equation A dy =
B dx, Amer. J. Math. 90 (1968), 248–269. MR 36 #3762

[Sha92] B. V. Shabat, Introduction to complex analysis. Part II, Translations of Math-
ematical Monographs, vol. 110, American Mathematical Society, Providence,
RI, 1992, Functions of several variables, Translated from the third (1985)
Russian edition by J. S. Joel. MR1192135 (93g:32001)

[Sha94] I. R. Shafarevich, Basic algebraic geometry. 1, second ed., Springer-Verlag,
Berlin, 1994, Varieties in projective space, Translated from the 1988 Russian
edition and with notes by Miles Reid. MR 95m:14001

Bibliography 607

[Shc82] A. A. Shcherbakov, Density of the orbit of a pseudogroup of conformal map-
pings and generalization of the Khuda˘ı-Verenov theorem, Vestnik Moskov.
Univ. Ser. I Mat. Mekh. (1982), no. 4, 10–15, 84. MR671879 (84m:30015)

[Shc84] , Topological and analytic conjugation of noncommutative groups of
germs of conformal mappings, Trudy Sem. Petrovsk. (1984), no. 10, 170–196,
238–239. MR778885 (86g:58083)

[Shc86] , Complex limit cycles of the equation dw/dz = Pn/Qn, Uspekhi Mat.
Nauk 41 (1986), no. 1(247), 211–212. MR832430 (87j:58077)

[Shc06] , Dynamics of local groups of conformal mappings and generic prop-
erties of diﬀerential equations on C2, Trudy Mat. Inst. Steklov. 256 (2006),
103–120.

[Shi80a] Song Ling Shi, A concrete example of the existence of four limit cycles for
plane quadratic systems, Sci. Sinica 23 (1980), no. 2, 153–158. MR 81f:34037

[Shi80b] , A concrete example of the existence of four limit cycles for plane
quadratic systems, Sci. Sinica 23 (1980), no. 2, 153–158. MR574405 (81f:34037)

[Sib62] Y. Sibuya, Simpliﬁcation of a system of linear ordinary diﬀerential equations
about a singular point, Funkcial. Ekvac. 4 (1962), 29–56. MR 27 #2694

[Sib90] , Linear diﬀerential equations in the complex domain: problems of ana-
lytic continuation, American Mathematical Society, Providence, RI, 1990. MR
92a:34010

[Siu77] Y.-T. Siu, Every Stein subvariety admits a Stein neighborhood, Invent. Math.
38 (1976/77), no. 1, 89–100. MR0435447 (55 #8407)

[ˇSoˇs72] A. N. ˇSoˇsita˘ıˇsvili, Bifurcations of topological type of singular points of vector
ﬁelds that depend on parameters, Funkcional. Anal. i Priloˇzen. 6 (1972), no. 2,
97–98. MR 45 #6036

[ˇSoˇs75] , The bifurcation of the topological type of the singular points of vector
ﬁelds that depend on parameters, Trudy Sem. Petrovsk. (1975), no. Vyp. 1,
279–309. MR 57 #17724

[SRO98] A. A. Shcherbakov, E. Rosales-Gonz´alez, and L. Ortiz-Bobadilla, Countable
set of limit cycles for the equation dw/dz = Pn(z, w)/Qn(z, w), J. Dynam.
Control Systems 4 (1998), no. 4, 539–581. MR1662926 (99m:58150)

[SZ02] E. Str´o˙zyna and H. ˙Zo l¸adek, The analytic and formal normal form for the
nilpotent singularity, J. Diﬀerential Equations 179 (2002), no. 2, 479–537.
MR1885678 (2003g:37091)

[Tak71] F. Takens, Partially hyperbolic ﬁxed points, Topology 10 (1971), 133–147. MR
46 #6399

[Tak01] , Forced oscillations and bifurcations, Global analysis of dynamical sys-
tems, Inst. Phys., Bristol, 2001, Reprint from Comm. Math. Inst. Rijksuniv.
Utrecht, No. 3-1974, 1974, pp. 1–61. MR 2002i:37081

[Tam92] I. Tamura, Topology of foliations: an introduction, Translations of Mathemat-
ical Monographs, vol. 97, American Mathematical Society, Providence, RI,
1992, Translated from the 1976 Japanese edition and with an afterword by
Kiki Hudson, With a foreword by Takashi Tsuboi. MR1151624 (93c:57021)

[Tit39] E. Titchmarsh, The theory of functions, Oxford University Press, 1939.

[Tre83] A. Treibich, Un r´esultat de Plemelj, Mathematics and physics (Paris,
1979/1982), Birkh¨auser Boston, Boston, MA, 1983, pp. 307–312. MR
87c:32016

608 Bibliography

[Tri90] S. I. Trifonov, Divergence of Dulac’s series, Mat. Sb. 181 (1990), no. 1, 37–56.
MR1048829 (91k:58109)

[Tsu59] M. Tsuji, Potential theory in modern function theory, Maruzen Co. Ltd.,
Tokyo, 1959. MR 22 #5712

[Van89] A. Vanderbauwhede, Centre manifolds, normal forms and elementary bifur-
cations, Dynamics reported, Vol. 2, Dynam. Report. Ser. Dynam. Systems
Appl., vol. 2, Wiley, Chichester, 1989, pp. 89–169. MR 90g:58092

[Var84] V. S. Varadarajan, Lie groups, Lie algebras, and their representations, Gradu-
ate Texts in Mathematics, vol. 102, Springer-Verlag, New York, 1984, Reprint
of the 1974 edition. MR 85e:22001

[Var89] A. N. Varchenko, Critical values and the determinant of periods, Russian Math.
Surveys 44 (1989), no. 4, 209–210 (English. Russian original).

[Var96] V. S. Varadarajan, Linear meromorphic diﬀerential equations: a modern point
of view, Bull. Amer. Math. Soc. (N.S.) 33 (1996), no. 1, 1–42. MR 96h:34011

[vdD88] L. van den Dries, Alfred Tarski’s elimination theory for real closed ﬁelds, J.
Symbolic Logic 53 (1988), no. 1, 7–19. MR 89h:01040

[vdE79] A. van den Essen, Reduction of singularities of the diﬀerential equation Ady =
Bdx, ´Equations diﬀ´erentielles et syst`emes de Pfaﬀ dans le champ complexe
(Sem., Inst. Rech. Math. Avanc´ee, Strasbourg, 1975), Lecture Notes in Math.,
vol. 712, Springer, Berlin, 1979, pp. 44–59. MR 82m:34007

[vdPS03] M. van der Put and M. F. Singer, Galois theory of linear diﬀerential equations,
Grundlehren der Mathematischen Wissenschaften, vol. 328, Springer-Verlag,
Berlin, 2003. MR1960772 (2004c:12010)

[VK75] A. M. Vinogradov and I. S. Krasil
′ˇsˇcik, What is Hamiltonian formalism?,
Uspehi Mat. Nauk 30 (1975), no. 1(181), 173–198. MR 58 #31235

[VR04] Kleptsyn V. and B. Rabinovich, Analytic classiﬁcation of Fuchsian singular
points, Matem. Zametki 76 (2004), no. 3, 372–383.

[War83] F. Warner, Foundations of diﬀerentiable manifolds and Lie groups, Springer-
Verlag, New York, 1983, Corrected reprint of the 1971 edition. MR 84k:58001

[Was87] W. Wasow, Asymptotic expansions for ordinary diﬀerential equations, Dover
Publications Inc., New York, 1987, Reprint of the 1976 edition. MR 88i:34003

[Wel80] R. O. Wells, Jr., Diﬀerential analysis on complex manifolds, second ed.,
Graduate Texts in Mathematics, vol. 65, Springer-Verlag, New York, 1980.
MR608414 (83f:58001)

[Wol96] Wolfram Research, Inc., Mathematica, Champaign, Illinois, 1996, Version 3.0.

[Yak95] S. Yakovenko, A geometric proof of the Bautin theorem, Concerning the Hilbert
16th problem, Amer. Math. Soc., Providence, RI, 1995, pp. 203–219. MR
96j:34056

[Yak00] , On zeros of functions from Bernstein classes, Nonlinearity 13 (2000),
no. 4, 1087–1094. MR 2001e:30008

[Yak02] , Bounded decomposition in the Brieskorn lattice and Pfaﬃan Picard–
Fuchs systems for Abelian integrals, Bull. Sci. Math 126 (2002), no. 7, 535–
554.

[Yak05] , Quantitative theory of ordinary diﬀerential equations and the tangen-
tial Hilbert 16th problem, On ﬁniteness in diﬀerential equations and Diophan-
tine geometry, CRM Monogr. Ser., vol. 24, Amer. Math. Soc., Providence, RI,
2005, pp. 41–109. MR2180125 (2006g:34062)

Bibliography 609

[Yak06] , Oscillation of linear ordinary diﬀerential equations: on a theorem of
A. Grigoriev, J. Dyn. Control Syst. 12 (2006), no. 3, 433–449. MR2233029

[Yoc88] J.-C. Yoccoz, Lin´earisation des germes de diﬀ´eomorphismes holomorphes de
(C, 0), C. R. Acad. Sci. Paris S´er. I Math. 306 (1988), no. 1, 55–58. MR
89i:58123

[Yoc95] , Th´eor`eme de Siegel, nombres de Bruno et polynˆomes quadratiques,
Ast´erisque (1995), no. 231, 3–88, Petits diviseurs en dimension 1. MR
96m:58214

[Yom99] Y. Yomdin, Global ﬁniteness properties of analytic families and algebra of their
Taylor coeﬃcients, The Arnoldfest (Toronto, ON, 1997), Amer. Math. Soc.,
Providence, RI, 1999, pp. 527–555. MR 1 733 591

[ˇZiˇz61] A. B. ˇZiˇzˇcenko, Homology groups of algebraic varieties, Izv. Akad. Nauk SSSR
Ser. Mat. 25 (1961), 765–788. MR0136615 (25 #83)

[ ˙Zo l94] H. ˙Zo l¸adek, Quadratic systems with center and their perturbations, J. Diﬀer-
ential Equations 109 (1994), no. 2, 223–273. MR 95b:34047

[ ˙Zo l06] , The monodromy group, Instytut Matematyczny Polskiej Akademii
Nauk. Monograﬁe Matematyczne (New Series) [Mathematics Institute of the
Polish Academy of Sciences. Mathematical Monographs (New Series)], vol. 67,
Birkh¨auser Verlag, Basel, 2006. MR2216496
