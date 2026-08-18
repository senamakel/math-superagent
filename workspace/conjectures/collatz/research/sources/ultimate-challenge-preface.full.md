<!-- source: https://www.ams.org/bookstore/pspdf/mbk-78-pref.pdf | converted from PDF -->

Preface

The 3x + 1 problem, also known as the Collatz problem, is a notorious unsolved
problem in arithmetic. Consider the operation on positive integers x given by: if
x is odd, multiply it by 3 and add 1; while if x is even, divide it by 2. The 3x +1
problem asks whether, starting from any positive integer x, repeating this operation
over and over will eventually reach the number 1. The answer appears to be “yes”
for all such x but this has never been proved. Despite its simple appearance, this
problem is believed to be extraordinarily diﬃcult.

A goal of this book is to report on what is known about the problem. It is
divided into ﬁve parts. This book contains two introductory papers on the problem,
three survey papers on the problem’s connections to various ﬁelds, two papers de-
voted to stochastic models and computational results for the problem, six reprinted
papers of historical interest, and a paper which giving an annotated bibliography
of work on this problem up to 2000. We now describe in more detail the papers
appearing in this volume.

PART I. Overview and Introduction. Part I of this volume contains two
introductory papers on the 3x +1 problem.

(1) Jeﬀrey C. Lagarias, The 3x +1 problem: an overview ([15]).

This paper gives a brief review of the 3x + 1 problem, its history, its connection
to various ﬁelds of mathematics, and its current status. It discusses generalizations
of the problem, and describes areas for mathematical research that it impacts. It
summarizes current “world record” on various aspects of the problem. It formulates
some directions for future research. Finally it discusses whether or not this problem
is a good mathematical problem.

(2) Jeﬀrey C. Lagarias, The 3x +1 problem and its generalizations,American
Math. Monthly 92 (1985), 3–23 ([14]).

This paper describes the 3x+1 problem and related problems. It presents, with
proofs, basic results on the behavior of iterates modulo powers of 2, and shows that
most integers n iterate to some value less than n. It formulates basic conjectures
on trajectories and cycles, all of them still unsolved. It focuses on number theoretic
aspects of the problem. Although this paper only covers work through 1984, it
is still up to date as an introduction to the basic features of the problem. This
reprinted version includes minor corrections and updates the reference citations.

ix

xPR E F A C E

PART II. Three Survey Papers. Part II of this volume presents three cur↩
rent survey papers on aspects of work on the x ⇁ problem.

↼↽ Marc Chamberland, A x ⇁ survey: number theory and dynamical systems
↼♭3♯↽.

This paper reports on research progress in various directions on the x⇁ prob↩
lem covering the period  through . It includes number theory results and
dynamical systems results, as well as other connections. It emphasizes the problem
viewed as a dynamical system, and discusses generalizations to dynamical systems
on larger spaces. This paper is a revised and extended version of the author’s earlier
survey paper ♭2♯, written in the Catalan language.

↼↽ Keith R. Matthews, Generalized x ⇁ mappings: Markov chains and
ergodic theory ↼♭19♯↽.

This paper summarizes work on Markov chain models for iterating generalized
x ⇁  maps, much of it due to the author. These models supply heuristics for the
behavior of iteration of a general class of functions that include the x ⇁  function.
It contains many interesting examples whose limiting behavior under iteration is
not understood, even on a conjectural level. This is a potentially fruitful area for
further research.

↼↽ Maurice Margenstern and Pascal Michel,Generalized x ⇁ functions and
the theory of computation ↼♭18♯↽.

This paper surveys the appearance of ↼x ⇁↽ −like functions in mathemati↩
cal logic and in the theory of computation. In  John Conway ♭5♯ exhibited
ax ⇁ ↩like function that gives an undecidable computational problem, and he
later ↼♭6♯↽ expanded on this construction to show how to formulate any computer
program using such functions, presented as a programming language FRACTRAN.
Other x ⇁ ↩like functions have been used to show that various “small” Turing
machines, those with few states and small alphabets, which are not known to be
universal computers, nevertheless can encode some apparently dicult problems.

PART III. Stochastic Modelling and Computation Papers. Part III of
this volume presents two papers on mathematical modelling and empirical results
from large computations.

↼↽ Alex Kontorovich and Jerey C. Lagarias,Stochastic models for the x ⇁
problem and related problems ↼♭13♯↽.

This paper reports on various stochastic models for the behavior of x ⇁  iter↩
ates and for comparison, results on iterates for the x ⇁  function. A remarkable
feature of the x ⇁  map is that, although the iteration is deterministic, the best
models for the behavior of the iteration are probabilistic. Such stochastic mod↩
els make predictions about the behavior for iterating a “generic” integer, and also
make predictions about the extreme behavior of some integers that may be ob↩
served. These models include random walk models for forward iteration, branching
processes and branching random walk models for backwards iteration. A third set

PREFACE xi

of branching process models can model the growth of 3x+1 trees, viewed 3-adically.

(7) Tomas Olivera e Silva, Empirical veriﬁcation of the3x +1 conjecture and
related conjectures([20]).

This paper reports on the latest computations of the 3x + 1 problem, and
some related functions. In particular the 3x + 1 conjecture is veriﬁed for all n 
5.764 × 1018 . Results of the computations include tests of some of the predictions
of the stochastic models above. It is an interesting challenge to write eﬃcient
progams to verify the 3x + 1 Conjecture to some bound and also collect statistics
on the conjecture.

PART IV. Reprinted Early Papers. Part IV of this volume presents six
early papers of historical interest, in chronological order. These papers are short,
easy to read, and most are hard to obtain in their original source. We provide
an editorial commentary after each paper, including additional references and bio-
graphical information.

(8)H.S.M. Coxeter, Cyclic sequences and frieze patterns: The Fourth Felix
Behrend Memorial Lecture, Vinculum 8 (1971), 4–7 ([7]).

This paper is the written version of a 1970 lecture, which was published in 1971
in Vinculum, the journal of the Mathematical Association of Victoria (Australia).
To my knowledge it is the earliest published paper that explicitly states the 3x +1
problem. It presents the problem at the end of the lecture as “mathematical gos-
sip.” Coxeter oﬀers a $50.00 prize for its solution. The main subject of the paper,
cyclic sequences and frieze patterns, is of interest in its own right.

(9) John H. Conway, Unpredictable iterations,in:Proc. 1972 Number Theory
Conference (Univ. Colorado, Boulder, Colo., 1972), Univ. Colorado, Boulder,
Colo. 1972, pp. 49–52 ([5]).

This 1972 paper, from the proceedings of a number theory conference held
at the University of Colorado, shows that a generalization of the 3x + 1 problem
is undecidable. Conway later used this encoding to design a computer language
FRACTRAN for universal computation using multiplication of fractions, see paper
(13) below.

(10) C. J. Everett, Iteration of the number theoretic functionf (2n)= n,
f (2n +1) = 3n +2, Advances in Math. 25 (1977), 42–45. ([9]).

This 1977 paper gives an elegant proof of a basic result showing that almost
positive integers n iterate to a smaller value under action iteration of the 3x+1 func-
tion. A similar result was independently obtained in 1976 by Riho Terras [21 ], [22 ].

(11) Richard K. Guy, Don’t try to solve these problems!,American Math.
Monthly 90 (1983), 35–41 ([10]).

This 1983 paper, written for the Unsolved Problems column of the American
Mathematical Monthly, presents a potpourri of 3x + 1-like problems, including the
original problem. True to its name, so far none of the four problems formulated

xii PREFACE

there have been solved.

(12) Lothar Collatz, On the motivation and origin of the(3n +1) problem
(Chinese), J. Qufu Normal University, Natural Science Edition [Qufu shi fan da
xue xue bao] 12 (1986), No. 3, 9–11 ([4]).

This 1986 paper, written in Chinese, is the only paper of Lothar Collatz that
discusses his work on the 3x + 1 problem. It is based on a talk that Collatz gave
at Qufu Normal University, Qufu, Shandong, China. Here we present an English
translation of this paper, using Collatz’s original illustrations.

(13) John H. Conway, FRACTRAN. A simple universal programming language
for arithmetic,In: Open Problems in Communication and Computation (T. M.
Cover and B. Gopinath, Eds.), Springer-Verlag: New York 1987, pp. 3-27 ([6]).

This 1987 paper of Conway expands on his 1972 paper to show how to encode
any computational problem in terms of iteration of a suitable 3x + 1-like function.
The programming language name FRACTRAN is a pun on FORTRAN (The IBM
Mathematical Formula Translating System). This is not the only pun in this paper.

PART V. Annotated Bibliography. Part V of this volume an an annotated
bibliography of work on the 3x + 1 problem and related iteration problems, from
1963-1999.

(14) Jeﬀrey C. Lagarias, The 3x +1 problem. An annotated bibliography ↼↩
↽ ([16 ]).

This bibliography attempts to be relatively complete over the period cited. It
includes a number of papers from the “prehistory” of the problem, in the 1960’s. It
also covers many papers appearing in unusual places, not covered by Mathematical
Reviews or Zentralblatt f¨ur Mathematik. It groups papers on the problem into
ten year subintervals. The growth of the number of papers in these time intervals,
which total 8, 34, 52 and 103 papers, respectively, show increasing eﬀort devoted
to the 3x + 1 problem and generalizations. A follow-up bibliography, currently
covering the period 2000–2009 ([17 ]) is posted on the math arXiv.

Book Title: The Ultimate Challenge. The results known about the 3x +1
problem strongly suggest that it does not ﬁt in the scope of classical “structural”
mathematics. Instead it seems to lie in a wilderness between the well-organized
part of mathematical knowledge, typiﬁed by the subjects covered in the volumes
of Bourbaki, and the boundary of undecidable problems, those problems that can
encode the action of a universal computer. The title does not assert the problem
is “ultimate” in its importance. Rather, “ultimate challenge” refers to the contrast
between the simplicity of the statement of the problem and the apparent diﬃ-
culty (perhaps impossibility) of resolving the problem. The papers in this volume
give ample warning that the problem shows no sign of being solvable at present.
Remember, not all challenges need to be accepted!

Epigraphs: References. The statement of G. C. J. Jacobi is taken from a
letter to Legendre written in 1830, published in 1875 in Borchardt [1, p. 272]

REFERENCES xiii

Il est vrai que M. Fourier avait l’opinion que le but principal de
math´ematiques ´etait l’utitlit´e publique et l’explications des ph´enom`es
naturels; mais un philosophe comme lui aurait dˆu savoir que le but
unique de la science, c’est l’honneur de l’esprit humain, et que sous
ce titre, une question des nombres vaut autant qu’une question du
syst`eme du monde.

The statement of D. Hilbert is taken from a 1931 paper on foundations on
mathematics (Hilbert [ , p. 486]).

Es ist schon an sich merkw¨urdig und philosophich bedeutsam, dass
die ersten und einfachsten Fragen ´uber die Zahlen 1,2,3, ... so
tieﬂegende Schwierigkeiten bieten. Diese Schwierigkeiten m¨ussen
¨uberwunden werden.

The statement of P. Erd˝os was made in conversation, sometime after publication
of the 1985 survey paper ([]).

Acknowledgments. I think Gerasimos Ladas for encouragement to prepare
a volume on this topic. I thank Andreas Blass, Mark Conger, Alex Kontorovich,
Stephen R. Miller, Chris Xiu and Mike Zieve for various forms of assistance in
this project. The three survey papers in this volume, and that of T. Oliveira e
Silva, have been peer-reviewed. I thank the anonymous reviewers for their eﬀorts.
I thank Sergei Gelfand for his positive suggestions about the title and production
of this volume. During the period of this work I received support from NSF Grants
DMS-0500555 and DMS-0801029.
 Jeﬀrey C. Lagarias
Ann Arbor, Michigan
August 2010

References

[1] C. W. Borchardt, Editor, Correspondence mathematique entre Legendre et Jacobi, J. reine
Angew. Math. 80 (1875), 205–279.
[2] M. Chamberland, Una actualizachio del problema 3 x +1 [An update on the 3 x +1 problem]
(Catalan), Butlletı Societat Catalana de Matem‘atiques 18 (2003), No.1, 19–45.
[3] M. Chamberland, A 3 x + 1 survey: number theory and dynamical systems, paper in this
volume.
[4] L. Collatz, On the motivation and origin of the (3n + 1)- problem (Chinese), J. Qufu Normal
University, Natural Science Edition [Qufu shi fan da xue xue bao] 12 (1986), No. 3, 9–11.
[Translation included in this volume]
[5] J. H. Conway, Unpredictable Iterations, Proc. 1972 Number Theory Conference (Univ. Col-
orado, Boulder, Colo., 1972 ), pp. 49–52. Univ. Colorado, Boulder, Colo. 1972.
[6] J. H. Conway, FRACTRAN: A Simple Universal Computing Language for Arithmetic, In:
Open Problems in Communication and Computation (T. M. Cover and B. Gopinath, Eds.),
Springer-Verlag: New York 1987, pp. 3-27 [Reprinted in this volume]
[7] H. S. M. Coxeter, Cyclic sequences and frieze patterns: The Fourth Felix Behrend Memorial
Lecture), Vinculum 8 (1971), 4–7. [Reprinted in this volume]
[8] P. Erd˝os, Private communication with J. C. Lagarias.
[9] C. J. Everett, Iteration of the number theoretic functionf (2n)= n, f (2n +1) = 3 n +2,
Advances in Math. 25 (1977), 42–45. [Reprinted in this volume]
[10] R. K. Guy, Don’t try to solve theseproblems!, American Math. Monthly 90 (1983), 35–41.
[Reprinted in this volume]
[11] R. K. Guy, Conway’s prime-producing machine, Math. Magazine 56 (1983), no. 1, 26–33.

xiv PREFACE

[12] D. Hilbert, Die Grundlagen der elementaren Zahlentheorie, Math. Annalen 104 (1931), 484–
494. [English Translation: Chap. 17 of P. Mancosu, From Brouwer to Hilbert. The debate on
the foundations of mathematics in the ’s,Oxford Univ. Press: New York 1998]
[13] A.V. Kontorovich and J. C. Lagarias, Stochastic models for the 3x + 1 problem and 5 x +1
problems, paper in this volume.
[14] J. C. Lagarias, The 3 x + 1 problem and its generalizations, Amer. Math. Monthly 92 (1985),
3–23. [Reprinted with corrections in this volume].
[15] J. C. Lagarias, The 3 x + 1 problem: an overview, paper in this volume.
[16] J. C. Lagarias, The 3x + 1 Problem: An Annotated Bibliography (1963-1999), paper in this
volume.
[17] J. C. Lagarias, The 3 x + 1 Problem: An Annotated Bibliography, II (2000-2009),
arXiv:math/0608208.
[18] P. Michel and M. Margenstern, Generalized 3 x + 1 functions and the theory of computation,
paper in this volume.
[19] K. R. Matthews, Generalized 3x + 1 mappings: Markov chains and ergodic theory, paper in
this volume.
[20] T. Oliveira e Silva, Empirical veriﬁcation of the 3 x + 1 and related conjectures, paper in this
volume.
[21] R. Terras, A stopping time problem on the positive integers, Acta Arithmetica 30 (1976),
241–252.
[22] R. Terras, On the existence of a density, Acta Arithmetica 35 (1979), 101–102.
