<!-- source: https://www.ams.org/bookstore/pspdf/mbk-78-prev.pdf | converted from PDF -->

The 3x +1 Problem: An Overview

Jeﬀrey C. Lagarias

1. Introduction

The 3x + 1 problem concerns the following innocent seeming arithmetic pro-
cedure applied to integers: If an integer x is odd then “multiply by three and add
one”, while if it is even then “divide by two”. This operation is described by the
Collatz function
 C(x)=
 ⎧
⎪⎨

⎪⎩
 3x +1 if x ≡ 1(mod 2),

x
2 if x ≡ 0(mod 2).

The 3x+1 problem, which is often called the Collatz problem, concerns the behavior
of this function under iteration, starting with a given positive integer n.

3x +1 Conjecture. Starting from any positive integer n, iterations of the
function C(x) will eventually reach the number 1. Thereafter iterations will cycle,
taking successive values 1, 4, 2, 1, ....

This problem goes under many other names, including the Syracuse problem,
Hasse’s algorithm, Kakutani’s problem and Ulam’s problem.

A commonly used reformulation of the 3x + 1 problem iterates a diﬀerent func-
tion, the 3x +1 function,given by

T (x)=
 ⎧
⎪⎪⎨

⎪⎪⎩
 3x +1
2 if x ≡ 1(mod 2),

x
2 if x ≡ 0(mod 2).

From the viewpoint of iteration the two functions are simply related; iteration of
T (x) simply omits some steps in the iteration of the Collatz function C(x). The
relation of the 3x + 1 function T (x) to the Collatz function C(x)is that:

T (x)=
 ⎧
⎨

⎩
 C(C(x)) if x ≡ 1(mod 2) ,

C(x)if x ≡ 0(mod 2) .

As it turns out, the function T (x) proves more convenient for analysis of the problem
in a number of signiﬁcant ways, as ﬁrst observed independently by Riho Terras ([88],
[89]) and by C. J. Everett [27].
 1 c⃝2010 American Mathematical Society

3

2 JEFFREY C. LAGARIAS

The 3x + 1 problem has fascinated mathematicians and non-mathematicians
alike. It has been studied by mathematicians, physicists, and computer scientists.
It remains an unsolved problem, which appears to be extremely dicult.

This paper aims to address two questions:

(1) What can mathematics currently say about this problem?

(2) How can this problem be hard, when it is so easy to state?

To address the ﬁrst question, this overview discusses the history of work on the
problem. Then it describes generalizations of the problem, and lists the dierent
ﬁelds of mathematics on which the problem impinges. It gives a brief summary of
the current strongest results on the problem.

Besides the results summarized here, this volume contains more detailed surveys
of mathematicians’ understanding of the 3x + 1 problem and its generalizations.
These cover both rigorously proved results and heuristic predictions made using
probabilistic models. The book includes several survey articles, it reprints sev-
eral early papers on the problem, with commentary, and it presents an annotated
bibliography of work on the problem and its generalizations.

To address the second question, let us remark ﬁrst that the true level of dif-
ﬁculty of any problem can only be determined when (and if) it is solved. Thus
there can be no deﬁnitive answer regarding its diculty. The track record on the
3x + 1 problem so far suggests that this is an extraordinarily dicult problem,
completely out of reach of present day mathematics. Here we will only say that
part of the diculty appears to reside in an inability to analyze the pseudorandom
nature of successive iterates ofT (x), which could conceivably encode very dicult
computational problems. We elaborate on this answer inΣ7.

Is the 3x+ 1 problem an important problem? Perhaps not for its individual
sake, where it merely stands as a challenge. It seems to be a prototypical example
of an extremely simple to state, extremely hard to solve, problem. A middle of the
road viewpoint is that this problem is representative of a large class of problems,
concerning the behavior under iteration of maps that are expanding on part of
their domain and contracting on another part of their domain. This general class
of problems is of deﬁnite importance, and is currently of great interest as an area
of mathematical (and physical) research; for some perspective, see Hasselblatt and
Katok [ ]. Progress on general methods of solution for functions in this class
would be extremely signiﬁcant.

This overview describes where things currently stand on the 3x + 1 problem
and how it relates to various ﬁelds of mathematics. For a detailed introduction to
the problem, see the following paper of Lagarias [] (in this volume). InΣ2we
give some history of the problem; this presents some new information beyond that
given in []. Then inΣ3 we give a ﬂavor of the behavior of the 3x + 1 iteration.
In Σ4 we discuss various frameworks for generalizing the problem; typically these
concern iterations of functions having a similar appearance to the 3x+ 1 function.
In Σ5 we review areas of research: these comprise dierent ﬁelds of mathematics and
computer science on which this problem impinges. InΣ6 we summarize the current
best results on the problem in various directions. InΣ7 we discuss the hardness of
the 3x +1 problem. InΣ8 we describe some research directions for future progress.

4 THE 3 x + 1 PROBLEM: AN OVERVIEW 3

In Σ we address the question. “Is the x⇁  problem a good problem⋆” In the
concluding sectionΣ we oer some advice on working on x ⇁ ↩related problems◃

. History and Background

The x ⇁  problem circulated by word of mouth for many years◃ It is generally
attributed to Lothar Collatz◃ He has stated ↼♭♯↽ that he took lecture courses in
 with Edmund Landau and Fritz von Lettenmeyer in GΥ ottingen↪ and courses
in  with Oskar Perron in Munich and with Issai Schur in Berlin↪ the latter
course including some graph theory◃ He was interested in graphical representations
of iteration of functions◃ In his notebooks in the ’s he formulated questions on
iteration of arithmetic functions of a similar kind ↼cf◃ ♭↪ p◃ ♯↽◃ Collatz is said
by others to have circulated the problem orally at the International Congress of
Mathematicians in Cambridge↪ Mass◃ in ◃ Several people whose names were
subsequently associated with the problem gave invited talks at this International
Congress↪ including H◃ S◃ M◃ Coxeter↪ S◃ Kakutani↪ and S◃ Ulam◃ Collatz ♭ ♯↼in
this volume↽ states that he described the x ⇁  problem to Helmut Hasse in 
when they were colleagues at the University of Hamburg◃ Hasse was interested in
the problem↪ and wrote about it in lecture notes in  ↼♭ ♯↽◃ Another claimant
to having originated the x ⇁  problem is Bryan Thwaites ♭ ♯↪ whoassertsthathe
came up with the problem in ◃ Whatever is its true origin↪ the x ⇁  problem
was already circulating at the University of Cambridge in the late ’s↪ according
to John H◃ Conway and to Richard Guy ♭  ♯◃

There was no published mathematical literature about the x ⇁  problem un↩
til the early ’s◃ This may have been↪ in part↪ because the ’s was a period
dominated by Bourbaki↩style mathematics◃ The Bourbaki viewpoint emphasized
complete presentations of theories with rich internal structure↪ which interconnect
with other areas of core mathematics ↼see Mashaal ♭ ♯↽◃ In contrast↪ the x ⇁
problem initially appears to be an isolated problem unrelated to the rest of mathe↩
matics◃ Another obstacle was the diculty in proving interesting results about the
x ⇁  iteration◃ The results that could be proved appeared pathetically weak↪ so
that it could seem damaging to one’s professional reputation to publish them◃ In
some mathematical circles it might have seemed in bad taste even to show interest
in such a problem↪ which appears dηeclassηe◃

During the ’s↪ various problems related to the x ⇁  problem appeared in
print↪ typically as unsolved problems◃ This included one of the original problems
of Collatz from the ’s↪ which concerned the behavior under iteration of the
function
 U ↼n↽/ n, U ↼n ⇁↽ /  n ⇁ ,U ↼n ⇁↽ /  n ⇁ .

The function U ↼n↽ deﬁnes a permutation of the integers↪ and the question con↩
cerns whether the iterates of the valuen /  form an inﬁnite set◃ This problem
was raised by Murray Klamkin ♭ ♯ in  ↼see Lagarias ♭ ↪ p◃ ♯↽↪ and remains
unsolved◃ Another such problem was posed by Ramond Queneau↪ a founder of
the French mathematical↩literary group Oulipo ↼Ouvroir de littηerature potentielle↽↪
which concerns allowable rhyming patterns generalizing those used in poems by the
↩th century troubadour↪ Arnaut Daniel◃ This problem turns out to be related to
a↼x ⇁ ↽↩like function whose behavior under iteration is exactly analyzable↪ see

54 JEFFREY C. LAGARIAS

Roubaud [  ]. Concerning the 3x+ 1 problem itself, during the 1960’s large com-
putations were done testing the truth of the conjecture. These reportedly veriﬁed
the conjecture for alln  109 .
To my knowledge, the 3 x + 1 problem ﬁrst appeared in print in 1971, in the
written version of a 1970 lecture by H. S. M. Coxeter [ ] (in this volume). It
was presented there “as a piece of mathematical gossip.” In 1972 it appeared in six
dierent publications, including a Scientiﬁc American column by Martin Gardner
[] that gave it wide publicity. Since then there has been a steady stream of work
on it, now amounting to several hundred publications.
Stanislaw Ulam was one of many who circulated the problem; the name “Ulam’s
problem” has been attached to it in some circles. He was a pioneer in ergodic
theory and very interested in iteration of functions and their study by computer;
he formulated many problem lists (e.g. [ ], []). A collaborator, Paul Stein [ ,
p. 104], wrote about Ulam:
Stan was not a number theorist, but he knew many number-theoretical
facts. As all who knew him well will remember, it was Stan’s par-
ticular pleasure to pose dicult, though simply stated, questions
in many branches of mathematics. Number theory is a ﬁeld par-
ticularly vulnerable to the “Ulam treatment,” and Stan proposed
more than his share of hard questions; not being a professional in
the ﬁeld, he was under no obligation to answer them.
Ulam’s long term collaborator C. J. Everett [ ] wrote one of the early papers
about the 3x + 1 problem in 1977.
The 3x + 1 problem can also be formulated in the backwards direction, as that
of determining the smallest setS0 of integers containing 1 which is closed under
theanemaps x  2x and 3x +2  2x + 1, where the latter map may only
be applied to inputs 3x+ 2 whose output 2x + 1 will be an integer. The 3x +1
conjecture then asserts thatS0 will be the set of all positive integers. This connects
the 3x + 1 problem with problems on sets of integers which are closed under the
action of ane maps. Problems of this sort were raised by Isard and Zwicky []
in 1970. In 1970-1971 David Klarner began studying sets of integers closed under
iteration of ane maps, leading to joint work with Richard Rado [ ], published in
1974. Interaction of Klarner and Paul Erd˝os at the University of Reading in 1971
led to the formulation of a (solved) Erd˝os prize problem: Does the smallest setS1 of
integers containing 1 and closed under the ane mapsx  2x +1,x  3x +1 and
x  6x + 1 have a positive (lower asymptotic) density? This setS1 was proved to
have zero density by D. J. Crampin and A. J. W. Hilton (unpublished), according
to Klarner [ ]. The solvers collectedΘ 10 from Erd˝os ([ ]). Later Klarner [ ,
p. 47] formulated a revised problem:
Klarner’s Integer Sequence Problem◃ Does the smallest set of integersS2
containing1 and closed under the aπne mapsx  2x, x  3x +2 and x  6x +3
have a positive ↼lower asymptotic↽ density⋆
This problem remains unsolved; see the paper of Guy [] (in this volume) and
accompanying editorial commentary.
Much early work on the problem appeared in unusual places, some of it in
technical reports, some in problem journals. The annotated bibliography given in
this book [] covers some of this literature, see also its sequel [ ]. Although

6 THE 3 x + 1 PROBLEM: AN OVERVIEW 5

Figure ◃ Trajectory of n = 649 plotted on standard vertical scale

the problem began life as a curiosity, its general connection with various other
areas of mathematics, including number theory, dynamical systems and theory of
computation, have made it a respectable topic for mathematical research. A number
of very well known mathematicians have contributed results on it, including John
H. Conway [ ] and Yakov G. Sinai [ ], [ ].

. 3x +1 Sampler

The fascination of the 3x + 1 problem involves its simple deﬁnition and the
apparent complexity of its behavior under iteration: there seems to be no simple
relation between the input value n and the iterates of n. Exploration of its structure
has led to the formulation of a web of subsidiary conjectures about the behavior of
iterates of the 3x + 1 function and generalizations; these include conjectures (C1)–
(C5) listed in Σ8. Many of these conjectures seem to be extremely diﬃcult problems
as well, and their exploration has led to much further research. Since other papers
in this volume give much more information on this complexity, here we give only a
brief sampler of 3x + 1 function behavior.

.. Plots of Trajectories. By the √√∐⌊̃̂√}√↓of x under a function T,we
mean the forward orbit of x, that is, the sequence of its forward iterates
(x, T(x),T
(2)(x),T
(3)(x), ...). Figure 1 displays the 3x + 1-function iterates of
n = 649 plotted on a standard scale. We see an irregular series of increases and
decreases, leading to the name “hailstone numbers” proposed by Hayes [ ], as
hailstones form by repeated upward and downward movements in a thunderhead.
To gain insight into a problem it helps to choose an appropriate scale for pic-
turing it. Here it is useful to view long trajectories on a logarithmic scale, i.e.,
to plot log T
(k )(n)versus k. Figure 2 displays the iterates of n0 = 100 10
35  on
such a scale. Using this scale we see a decrease at a certain geometric rate to the
value of 1, indicated by the trajectory having roughly a constant slope. This is
characteristic of most long trajectories. As explained in Σ3.3 a probabilistic model
predicts that most trajectories plotted on a logarithmic scale will stay close to a
line of constant slope − 1
2 log 3
4 − 0.14384, thus taking about 6.95212 log n steps

76 JEFFREY C. LAGARIAS

Figure 2. Trajectory ofn0 /  ﬀ ˇ
35  plotted on a logarith↩
mic vertical scale◃ The dotted line is a probability model prediction
for a “random” trajectory for this sizeN ◃

to reach ◃ This line is pictured as the dotted line in Figure ◃ This trajectory
takes  steps to reachn / ↪ while the probabilistic model predicts about 
steps will be taken◃
On the other hand↪ plots of trajectories suggest that iterations of the x ⇁
function also seem to exhibit pseudo↩random features↪ i◃e◃ the successive iterates
of a random starting value seem to increase or decrease in an unpredictable man↩
ner◃ From this perspective there are some regularities of the iteration that appear
↼only↽ describable as statistical in nature. they are assertions about the majority
of trajectories in ensembles of trajectories rather than about individual trajectories◃

.. Patterns. Close examination of the iterates of the x ⇁  function T↼x↽
for dierent starting values reveals a myriad of internal patterns◃ A simple pattern
is that the initial iterates ofn / m − are

T(k )↼
m − ↽ /  k ˇ
m − k − , for  k  m.

In particular↪T(m )↼
m − ↽ /  m − , this example shows that the iteration can
sometimes reach values arbitrarily larger than the initial value↪ either on an absolute
or a relative scale↪ even if↪ as conjectured↪ the iterates eventually reach ◃ Other
patterns include the appearance of occasional large clusters of consecutive numbers
which all take exactly the same number of iterations to reach the value ◃ Some of
these patterns are easy to analyze↪ others are more elusive◃
Table  presents data on iterates of the x ⇁  function T↼x↽forn / N0 ⇁ m↪
  m / j ⇁ k  ↪ with

n0 /  ﬀ ˇ35  / , , , , , , , , , , , , .

Here ﬃ⎧ ↼n↽ denotes the⊔≀⊔⊣↕ ∫⊔≀√√⟩\} ⊔⟩⇕⌉for n↪ which counts the number of
iterates of the x⇁ ↩functionT↼x↽ needed to reach  starting fromn↪ counting
n as the ↩th iterate◃ This number is the same as the number of even numbers
appearing in the trajectory of the Collatz function before ﬁrst reaching ◃

8 THE 3 x + 1 PROBLEM: AN OVERVIEW 7

Table 1. Values of total stopping time  π (n)for n = n0 +10j + k, with
n0 := 100 ˇ1035  =31, 415, 926, 535, 897, 932, 384, 626, 433, 832, 795, 028, 800.

j =0 j =1 j =2 j =3 j =4 j =5 j =6 j =7 j =8 j =9
k =0 529 529 529 678 529 529 846 529 846 846
k =1 659 659 529 678 659 529 846 529 529 529
k =2 846 529 659 529 529 529 659 846 529 659
k =3 846 529 659 846 659 529 659 846 529 659
k =4 659 659 659 846 678 529 846 846 846 659
k =5 659 659 846 846 678 529 529 529 846 659
k =6 659 529 659 846 678 846 529 846 659 846
k =7 529 529 659 846 659 659 529 846 659 529
k =8 529 678 659 846 529 846 529 529 846 846
k =9 529 678 659 659 529 529 529 529 659 846

We observe that the total stopping time function takes only a few diﬀerent
values, namely: 529, 654, 678 and 846, and these four values occur intermixed in
a somewhat random-appearing way, but with some regularities. Note that around
n0  3.14× 1037 the predicted “average size” of a trajectory is 6.95212 log n0 	 600.
In the data here we also observe “jumps” of size between the occurring values on
the order of 100.

This is not a property of just this starting value. In Table 2 we give similar
data for blocks of 100 near n =10
35 and 10
36 , respectively. Again we observe that
there are also four or ﬁve values occurring, but now they are diﬀerent values. In
this table we present data on two other statistics: the ̃√̃√√̃{̂↓statistic gives the
count of these number of occurrences of each value, and the 1\√∐√]}statistic denotes
the fraction of odd iterates occurring in the given trajectory up to and including
when 1 is reached. It is an experimental fact that all sequences in the table having
the same total stopping time also have the same 1-ratio. In the ﬁrst two blocks
the value  π (n) = 481 (resp. 351) that occurs with frequency 1 is that for the
intial value n =1035 (resp. n =10
36 ) in the given interval; these initial values
are unusual in being divisible by a high power of 2. Probabilistic models for the
3x + 1-function iteration predict that even and odd iterates will initially occur with
equal frequency, so we may anticipate the 1-ratio values to be relatively close to
0.5.
 Table 2 Values of total stopping time, their frequencies, and 1-ratio for
(a) 10
35  n  1035 + 99, (b) 1036  n  1036 + 99, (c) n0  n  n0 + 99.

(a) 10
35 (b) 10
36 (c) n0
 π (n) freq. 1-ratio  π (n) freq. 1-ratio  π (n) freq. 1-ratio
481 1 0.47817 351 1 0.41594 529 38 0.48204
508 19 0.48622 467 72 0.46895 654 28 0.51138
573 49 0.50261 508 21 0.48228 678 7 0.51474
592 10 0.50675 519 6 0.48554 846 27 0.53782
836 21 0.54306
 98 JEFFREY C. LAGARIAS

The data in Table 2 suggests the following heuristic: asn increases only a few
values of ﬀ (n ) locally occur over short intervals; there is then a slow variation in
which values of ﬀ (n ) occur. However these local values are separated from each
other by relatively large “jumps” in size. We stress that this is a purely empirical
observation, nothing like this is rigorously proved! Our heuristic did not quantify
what is a “short interval” and it did not quantify what “relatively large jumps”
should mean. Even the existence of ﬁnite values for ﬀ (n ) in the tables presumes
the 3x + 1 conjecture is true for all numbers in the table.

3.3. Probabilistic Models. A challenging feature of the 3x+1 problem is the
huge gap between what can be observed about its behavior in computer experiments
and what can be rigorously proved. Attempts to understand and predict features
of empirical experimentation have led to the following curious outcome:the use
of probabilistic models to describe a deterministic processThis gives another
theme of research on this problem: the construction and analysis of probabilistic
and stochastic models for various aspects of the iteration process.
A basic probabilistic model of iterates of the 3x +1 functionT (x)proposesthat
most trajectories for 3x + 1 iterates have equal numbers of even and odd iterates,
and that the parity of successive iterates behave in some sense like independent
coin ﬂips. A key observation of Terras [88] and Everett [27], leading to this model,
is that the initial iterates of the 3x+ 1 function have this property (see Lagarias
[58, Lemma B]).) This probabilistic model suggests that most trajectories plotted
on a logarithmic vertical scale should appear close to a straight line having negative
slope equal to− 1
2 log 3
4 − 0◃14384↪and should thus take about 6◃95212 logn steps
to reach 1.
The corresponding behavior of iterates of the Collatz functionC (x)is more
complicated. The allowed patterns of even and odd Collatz function iterates always
have an even iterate following each odd iterate. Probabilistic models taking this
into account are more complicated to formulate and analyze than that for the
3x + 1 function; this is a main reason for studying the 3x+ 1 function rather than
the Collatz function. Use of the probabilistic model above allows the heuristic
inference that Collatz iterates will be even about two-thirds of the time.
A variety of fairly complicated stochastic models, many of which are rigorously
analyzable (as probability models), have now been formulated to model various
aspects of these iterations, see Kontorovich and Lagarias [56] (in this volume).
Rigorous results for such models lead to heuristic predictions for the statistical
behavior of iterates of the generalized 3x + 1 map. Themodel abovepredicts
the behavior of “most” trajectories. A small number of trajectories may exhibit
quite dierent behavior. One may consider those trajectories that that seem to
oer maximal value of some iterate ofT (⌋ )(n )compared to n . Here a probabilistic
model (see [56, Sec. 4.3] in this volume) predicts that the statistic

(n ):= log(max⌋ ﬃ1 ⌊T (⌋ )(n )
⌋

logn
as n 
 should have (n )  2+ o(1) for all suciently largen . Figure 3.3
oers a plot of the trajectory, for the valuen 1 = 1980976057694878447↪ which
attains the largest value of the statistic(n )over 1  n  1018 ; this value was
found by Oliveira e Silva [76, Table 6] (in this volume). This example has(n 1)
2◃04982. Probabilistic models suggest that the extremal trajectories of this form

10
 .

THE 3 x + 1 PROBLEM: AN OVERVIEW 9

Figure ◃ Extremal trajectory n1 = 1980976057694878447 given
in Oliveira e Silva’s Table 6.

will approach a characteristic shape which consists of two line segments, one of
length 7.645 log n steps of slope about 0.1308 up to the maximal value of about
2log n, the second of about 13.905 log n steps of slope about −0.1453 to 0, taking
21.55 log n steps in all. This shape is indicated by the dotted lines on Figure 3.3
for comparison purposes.
Another prediction of such stochastic models, relevant to the 3x +1 conejcture,
is that the number of iterations required for a positive integer n to iterate to 1
under the 3x + 1 function T(x) isatmost41.677647 log n (see [62 ], [56 , Sect. 4]).
In particular such models predict, in a quantitative form, that there will be no
divergent trajectories.

These stochastic models can be generalized to model the behavior of many
generalized 3x + 1 functions, and they make qualitatively diﬀerent predictions de-
pending on the function. For example, such models predict that no orbit of iteration
of the 3x + 1 function “escapes to inﬁnity” (divergent trajectory). However for the
5x +1 ̃√{̂√]}{given by

T5(x)=
 ≡
≤≤↦
≤≤→
 5x +1
2 if x π 1(mod 2),

x
2 if x π 0(mod 2),

similar stochastic models predict that almost all orbits should “escape to inﬁnity”
([56 , Sect. 8]). These predictions are supported by experimental computer evidence,
but it remains an unsolved problem to prove that there exists even one trajectory
for the 5x + 1 problem that “escapes to inﬁnity”.

There remains considerable research to be done on further developing stochastic
models. The experiments on the 3x + 1 iteration reported above in Σ3.2 exhibit
some patterns not yet explained by stochastic models. In particular, the behaviors
of total stopping times observed in Tables 1 and 2, and the heuristic presented
there, have not yet been justiﬁed by suitable stochastic models.
 1110 JEFFREY C. LAGARIAS

4. Generalized x ⇁ functions

The original work on the x ⇁  problem viewed it as a problem in number
theory◃ Much of the more recent work views it as an example of a special kind
of discrete dynamical system↪ as exempliﬁed by the lecture notes volume of G◃
J◃ Wirsching ♭95 ♯◃ As far as generalizations are concerned↪ a very useful class
of functions has proved to be the set of generalized Collatz functions which are
deﬁned below◃ These possess both number↩theoretical and dynamic properties, the
number↩theoretic properties have to do with the existence ofp↩adic extensions of
these maps for various primesp◃

At present the x ⇁  problem is most often viewed as a discrete dynamical
system of an arithmetical kind◃ It can then be treated as a special case↪ within the
framework of a general class of such dynamical systems◃ But what should be the
correct degree of generality in such a class⋆

There is signiﬁcant interest in exploring the behavior of dynamical systems of an
arithmetic nature↪ since these may be viewed as “toy models” of more complicated
dynamical systems arising in mathematics and physics◃ There are a wide variety
of interesting arithmetic dynamical systems◃ The book of Silverman ♭82 ♯ studies
the iteration of algebraic maps on algebraic varieties◃ The book of Schmidt ♭81 ♯
considers dynamical systems of algebraic origin↪ meaningZ d↩actions on compact
metric groups↪ using ergodic theory and symbolic methods◃ The book of Fursten↩
berg ♭30 ♯ considers various well structured arithmetical dynamical systems, for a
further development see Glasner ♭34 ♯◃ The generalized x ⇁  functions studied in
this book provide another distinct type of arithmetic discrete dynamical system◃

We present a taxonomy of several classes of functions which represent successive
generalizations of the x ⇁  function◃ The simplest generalization of the x ⇁
function is the x⇁ k function↪ which is deﬁned fork ﬃ or ↼mod↽↪by

T3,k ↼x↽/
 ⎧
⎪⎪⎨

⎪⎪⎩
 x ⇁ k
 ifx ﬃ ↼mod ↽ ,

x
 ifx ﬃ ↼mod ↽ .

The generalization of the x⇁  conjecture to this situation is twofold. ﬁrst↪ that
under iteration every orbit becomes eventually periodic↪ and second↪ that there are
only a ﬁnite number of cycles ↼periodic orbits↽◃ This class of functions occurs in
the study of cycles of the x⇁  function ↼Lagarias ♭59♯↽◃ Note that the x⇁
functionT↼x↽ can be extended to be well deﬁned on the set of all rational numbers
having odd denominator↪ and a rescaling of anyT↩orbit of such a rational number
r / n
k to clear its denominatork will give an orbit of the mapT3,k ◃ Thus↪ integer
cycles of the x ⇁ k function correspond to rational cycles of the x ⇁  function
having denominator k◃

To further generalize↪ letd   be a ﬁxed integer and consider the function
deﬁned for integer inputsx by

↼◃↽ f ↼x↽/ aix ⇁ bi
d ifx ﬃ i ↼mod d↽,   i  d − ,

12 THE 3 x + 1 PROBLEM: AN OVERVIEW 11

where –↼ai,bi↽.ﬃ i ﬃ d − ˝ is a collection of integer pairs◃ Such a function is
calledadmissibleif the integer pairs ↼ai,bi↽ satisfy the condition

↼◃↽ iai ⇁ bi ﬀ ↼mod d↽for ﬃ i ﬃ d − .

This condition is necessary and sucient for the mapf ↼x↽ to take integers to
integers◃ These functionsf ↼x↽ have been calledgeneralized Collatz functions,or
RCW Afunctions↼Residue↩Class↩Wise Ane functions↽◃ Generalized Collatz func↩
tions have the nice feature that they have a unique continuous extension to the space
Zd of d↩adic integers in the sense of Mahler ♭♯◃
An important subclass of generalized Collatz functions are those ofrelatively
prime type◃ These are the subclass of generalized Collatz functions for which

↼◃↽ gcd↼a0a1 ˇˇˇad− 1 ,d↽/  .

This class includes the x⇁ function T↼x↽ but not the Collatz functionC↼x↽itself◃
It includes the x⇁  function T5 ↼x↽↪ which as mentioned above appears to have
quite dierent long↩term dynamics on the integersZ than does the x⇁  function◃
Functions in this class have the additional property that their unique extension to
the d↩adic integersZd has the d↩adic Haar measure as an invariant measure◃ This
permits ergodic theory methods to be applied to their study↪ see the survey paper
of Matthews ♭↪ Thm◃ ◃♯ ↼in this volume↽ for many examples◃
As a ﬁnal generalization↪ one may consider the class of integer↩valued func↩
tions↪ which when restricted to residue classes ↼modd↽ are given by a polynomial
Pi↼x↽ for each classi ↼mod d↽. Members of this class of functions have arisen in
several places in mathematics◃ They are now widely calledquasi↩polynomial func↩
tionsor quasi↩polynomials◃ Quasi↩polynomials appear in commutative algebra and
algebraic geometry↪ in describing the Hilbert functions of certain semigroups↪ in
a well known theorem of Serre↪ see Bruns and Herzog ♭↪ pp◃ –♯ and Bruns
and Ichim ♭ ♯◃ In another direction↪ functions that count the number of lattice
points inside dilated rational polyhedra have been shown to be quasi↩polynomial
functions ↼on the positive integers↽↪ starting with work of Ehrhart ♭ ♯↪ see Beck
and Robins ♭♯ and Barvinok ♭↪ Chap◃ ♯◃ They also have recently appeared in
dierential algebra in connection withq↩holonomic sequences↪ see Garoufalidis ♭ ♯◃
Such functions were introduced in group theory by G◃ Higman in  ♭ ♯ under
the name PORC functions ↼polynomial on residue class functions↽◃ Higman’s mo↩
tivating problem was the enumeration ofp↩groups↪ cf◃ Evseev ♭ ♯◃ The class of all
quasi↩polynomial functions is closed under addition and pointwise multiplication↪
and forms a commutative ring under these operations◃
We arrive at the following taxonomy of function classes of increasing generality.

–x ⇁  function T↼x↽˝ – x ⇁ k functionsT3,k↼x↽˝

– generalized Collatz functions of relatively prime type˝

– generalized Collatz functions˝

– quasi↩polynomial functions˝.

For applications in mathematical logic↪ it has proved useful to further widen
the deﬁnition of generalized Collatz functions to allowpartially deﬁned functions◃
Such functions are obtained by dropping the admissibility condition ↼◃↽, they map
integers to rational numbers having denominator dividingd◃ If a non↩integer value
is encountered↪ then one cannot iterate such a function further◃ In this circumstance

1312 JEFFREY C. LAGARIAS

we adopt the convention that if a non-integer iteration value is encountered, the
calculation stops in a special “undeﬁned” state. This framework allows the encoding
of partially-deﬁned (recursive) functions. One can use this convention to also deﬁne
composition of partially deﬁned functions.

◃ Research Areas

Work on the 3 x + 1 problem cuts across many ﬁelds of mathematics. Six basic
areas of research on the problem are: (1)number theory: analysis of periodic or-
bits of the map; (2)dynamical systems: behavior of generalizations of the 3x +1
map; (3)ergodic theory: invariant measures for generalized maps; (4)theory of com-
putation: undecidable iteration problems; (5)stochastic processes and probability
theory: models yielding heuristic predictions for the behavior of iterates; and (6)
computer science: algorithms for computing iterates and statistics, and explicit
computations. We treat these in turn.

(1) Number Theory

The connection with number theory is immediate: the 3x+1 problem is a
problem in arithmetic, whence it belongs to elementary number theory. Indeed it
is classiﬁed as an unsolved problem in number theory by R. K. Guy [ ,Problem
E16]. The study of cycles of the 3x +1 map leads to problems involving exponential
Diophantine equations. The powerful work of Baker and Masser–WΥustholz on lin-
ear forms in logarithms gives information on the non-existence of cycles of various
lengths having speciﬁed patterns of even and odd iterates. A class of generalized
3x + 1 functions has been deﬁned in a number theory framework, in which arith-
metic operations on the domain of integers are replaced with such operations on
the ring of integers of an algebraic number ﬁeld, or by function ﬁeld analogues such
as a polynomial ring with coecients in a ﬁnite ﬁeld. Number-theoretic results are
surveyed in the papers of Lagarias [] and Chamberland [ ] in this volume.

(2) Dynamical Systems

The theory of iscrete dynamical systems concern the behavior of functions under
iteration; that of continuous dynamical systems concern ﬂows or solutions to dier-
ential equations. The 3x + 1 problem can be viewed as iterating a map, therefore it
is a discrete dynamical system on the state spaceZ . Thisviewpointwastaken in
Wirsching [ ]. The important operation for iteration iscomposition of functions.
One can formulate iteration and composition questions in the general context of
universal algebra, cf. Lausch and Nobauer [ , Chap. 4.5]. In the taxonomy above,
the classes of generalized 3x + 1 functions, and quasi-polynomial functions are each
closed under addition and composition of functions. The iteration properties of
the ﬁrst three classes of functions above have been studied, in connection with the
3x + 1 problem and the theory of computation. However the iteration of general
quasi-polynomial functions remains an unexplored research area.
Viewing the problem this way suggests that it would be useful in the study
of the 3x+ 1 function to obtain dynamical systems on larger domains, including
the real numbersR and the complex numbers C. Other extensions include deﬁning
analogous functions on the ringZ 2 of 2-adic integers, or, for generalized 3x+1

14 THE 3 x + 1 PROBLEM: AN OVERVIEW 13

maps↪ on a ring ofd↩adic integers↪ for a value ofd determined by the function◃
When one considers generalized x ⇁  functions on larger domains↪ a wide variety
of behaviors can occur◃ These topics are considered in the papers of Chamberland
♭11♯ and Matthews ♭67♯ in this volume◃ For a general framework on topological
dynamics see Akin ♭1♯◃

↼↽ Ergodic Theory

The connection with ergodic theory arises as an outgrowth of the dynamical
systems viewpoint↪ but adds the requirement of the presence of an invariant mea↩
sure◃ It was early observed that there are ﬁnitely additive measures which are
preserved by the x⇁  map on the integers◃ Extensions of generalized x⇁  func↩
tions tod↩adic integers lead to maps invariant under standard measures ↼countably
additive measures↽◃ For example↪ the ↼unique continuous↽ extension of the x⇁
map to the ↩adic integers has ↩adic measure as an invariant measure↪ and the map
is ergodic with respect to this measure◃ Ergodic theory topics are considered in the
surveys of Matthews ♭67♯ and Kontorovich and Lagarias ♭56♯ in this volume◃ An
interesting open problem is to classify all invariant measures for generalized x ⇁
functions on thed↩adic integers◃

↼↽ Mathematical Logic and the Theory of Computation

The connection to logic and the theory of computation starts with the result
of Conway that there is a generalized x ⇁  function whose iteration can simulate
a universal computer◃ Conway ♭16♯ exhibited an unsolvable iteration problem for
a particular generalized x ⇁  function. starting with a given input which is a
positive integern↪ decide whether or not some iterate of this map with this input is
ever a power of ◃ In this connection note that the x ⇁  problem can be reformu↩
lated as asserting that↪ starting from any positive integern↪ some iterateC(k )↼n↽
of the Collatz function ↼or of the x⇁  function↽ is a power of ◃ It turns out
that iteration of x⇁ ↩like functions had already been considered in understanding
the power of some logical theories even in the late ’s, these involved partially
deﬁned functions taking integers to integers ↼with undeﬁned output for some in↩
tegers↽↪ cf◃ Isard and Zwicky ♭51♯◃ More recently such functions have arisen in
studying the computational power of “small” Turing machines↪ that are too small
to encode a universal computer◃ These topics are surveyed in the paper of Michel
and Margenstern ♭68♯ in this volume◃

↼↽ Probability Theory and Stochastic Processes

A connection to probability theory and stochastic processes arises when one
attempts to model the behavior of the x ⇁  iteration on large sets of integers◃
This leads to heuristic probabilistic models for the iteration↪ which allow predic↩
tions of its behavior◃ Some authors have argued that the iteration can be viewed as
a kind of pseudo↩random number generator↪ viewing the input as being given by a
probability distribution↪ and then asking how this probability distribution evolves
under iteration◃ In the reverse direction↪ one can study trees of inverse iterates ↼the
inverse map is many↩to↩one↪ giving rise to a unary↩binary tree of inverse iterates↽◃
Here one can ask for facts about the structure of such trees whose root node is
an integer picked from some probability distribution◃ One can model this by a

1514 JEFFREY C. LAGARIAS

stochastic model corresponding to random tree growth, e.g. a branching random
walk. These topics are surveyed in the paper of Kontorovich and Lagarias [ ]in
this volume.

(6)Computer Science: Machine Models, Parallel and Distributed Computation

In 1987 Conway [ ] (in this volume) formalized the Fractran model of compu-
tation as a universal computer model, based on his earlier work related to the 3x +1
problem. This computational model is related to the register machine (or counter
machine) model of Marvin Minsky ([], [, Sect. 11.1]). Both these machine
models have recently been seen as relevant for developing models of computation
using chemical reaction networks, and to biological computation, see Soloveichik et
al [] and Cook et al. [ ].
The necessity to make computer experiments to test the 3x + 1 conjecture, and
to explore various properties and patterns of the 3x + 1 iteration, leads to other
questions in computation. One has the research problem of developing ecient
algorithms for computing on a large scale, using either parallel computers or a dis-
tributed computer system. The 3x + 1 conjecture has been tested to a very large
value ofn, see the paper of Oliveira e Silva [ ] in this volume. The computational
method used in [ ] to obtain record results can be parallelized. Various large
scale computations for the 3x + 1 problem have used distributed computing, cf.
Roosendaal [].
 ◃ Current Status

We give a brief summary of the current status of the problem, which further
elaborates answers to the two questions raised in the introduction.

◃◃ Where does research currently stand on the 3x +1 problem⋆
The 3x + 1 problem remains unsolved, and a solution remains unapproachable at
present. To quote a still valid dictum of Paul Erd˝os ([ , p. 3]) on the problem:

“Mathematics is not yet ready for such problems.”

Research has established various “world records”, all of which rely on large
computer calculations (together with various theoretical developments).

(W1) The 3x + 1 conjecture has now been veriﬁed for alln¡ 20 × 258
5.7646 × 1018 (Oliveira e Silva [] (in this volume)).
(W2) The trivial cycleı1, 2℘ is the only cycle of the 3x + 1 function on the
positive integers having period length less than 10, 439, 860, 591. It is also
the only cycle containing less than 6, 586, 818, 670 odd integers (Eliahou
[, Theorem 3.2]
 ).
(W3) Inﬁnitely many positive integersn take at least 6.143 logn steps to reach
1 under iteration of the 3x + 1 functionT(x) (Applegate and Lagarias
[]).

⎪T⟨⟩∫ \⊓⇕⌊⌉∇ ⟩∫ ⊔⟨⌉ ⌊≀⊓\⌈ ⇐∈∞ ,′⇒ }⟩⊑⌉\ ⟩\ ∪24 ⇔ T⊣⌊↕⌉ ∈⊎↙ T⟨⌉ ∫⇕⊣↕↕⌉∇ ⊑⊣↕⊓⌉∫ ⟩\ T⊣⌊↕⌉ ∈ ⊣∇⌉
\≀⊒ ∇⊓↕⌉⌈ ≀⊓⊔ ⌊† ⊔⟨⌉ ⌋≀⇕√⊓⊔⊣⊔⟩≀\∫ ⟩\ ⟩⊔⌉⇕ ⇐W∞⇒ ⊣⌊≀⊑⌉↙

16 THE 3 x + 1 PROBLEM: AN OVERVIEW 15

↼W↽ The positive integern with the largest currently known value ofC↪such
that it takesC logn iterations of the x ⇁  function T↼x↽toreach ↪ is
n / , , , , , , ,  with C 	 . ↼Roosendaal ♭↪
x ⇁  Completeness and Gamma records♯↽◃
↼W↽ The number of integers   n  X that iterate to  is at leastX 0.84 ↪for
all suciently largeX ↼Krasikov and Lagarias ♭♯↽◃
There has also been considerable progress made on showing the nonexistence
of various kinds of periodic points for the x ⇁  function↪ see Brox ♭♯ and Simons
and de Weger ♭  ♯◃ These bounds are based on number↩theoretic methods involving
Diophantine approximation◃

.. Where does research stand on generalizations of the x ⇁ prob↩
lem⋆ It has proved fruitful to view the x⇁  problem as a special case of wider
classes of functions◃ These function classes appear naturally as the correct level
of generality for basic results on iteration, this resulted in the taxonomy of func↩
tion classes given inΣ◃ There are some general results for these classes and many
unsolved problems◃
The x ⇁ k problem seems to be the correct level of generality for studying
rational cycles of the x⇁  function ↼♭ ♯↽◃ There are extensive results on cycles
of the x⇁  function↪ and the methods generally apply to the x ⇁ k function as
well↪ see the survey of Chamberland ♭ ♯ ↼in this volume↽◃
The class of generalized x ⇁  functions of relatively prime type is a very
natural class from the ergodic theory viewpoint↪ since this is the class on which the
d↩adic extension of the function hasd↩adic Haar measure as an invariant measure◃
The paper of Matthews ♭ ♯ ↼in this volume↽ reports general ergodicity results and
raises many questions about such functions◃
The class of generalized Collatz functions has the property that all functions
in it have a unique continuous extension to the domain ofd↩adic integersZd ◃This
general class is known to contain undecidable iteration problems↪ as discussed in the
paper of Michel and Margenstern ♭♯ ↼in this volume↽◃ The dynamics of general
functions in this class is only starting to be explored, many interesting examples are
given in the paper of Matthews ♭♯ ↼in this volume↽◃ An interesting area worthy of
future development is that of determining the existence and structure of invariant
Borel measures for such functions onZd ↪ and determining whether there is some
relation of their structure to undecidability of the associated iteration problem◃

.. How can this be a hard problem, when it is so easy to state⋆ Our
answer is that there are two dierent mechanisms yielding hard problems↪ either or
both of which may apply to the x ⇁  problem◃ The ﬁrst is “pseudorandomness”,
this involves a connection with ergodic theory◃ The second is “non↩computability”◃
Both of these are discussed in detail in this volume◃
The “ergodicity” connection has been independently noted by a number of
people↪ see for example Lagarias ♭ ♯ ↼in this volume↽ and Akin ♭♯◃ The unique
continuous extension of the x⇁ map T↼x↽ to the ↩adic integersZ2 gives a function
which is known to be ergodic in a strong sense↪ with respect to the ↩adic measure◃
It is topologically and metrically conjugate to the shift map↪ which is a maximum
entropy map◃ The iterates of the shift function are completely unpredictable in

1716 JEFFREY C. LAGARIAS

the ergodic theory sense. Given a random starting point, predicting the parity of
the n -th iterate for anyn is a “coin ﬂip” random variable. The 3x + 1 problem
concerns the behavior of iterating this function on the set of integersZ, which is a
dense subset ofZ2 , having 2-adic measure zero. The diculty is then in ﬁnding and
understanding non-random regularities in the iterates when restricted toZ.Various
probabilistic models are discussed in the paper of Kontorovich and Lagarias [56]
(in this volume). Empirical evidence seems to indicate that the 3x + 1 function on
the domain Z retains the “pseudorandomness” property on its initial iterates until
the iterates enter a periodic orbit. This supports the 3x + 1 conjecture and at the
same time deprives us of any obvious mechanism to prove it, since mathematical
arguments exploit the existence of structure, rather than its absence.
A connection of a generalized Collatz function to “non-computability” was
made by Conway [ 16] (in this volume), as already mentioned. Conway’s undecid-
ability result indicates that the 3x+ 1 problem could be close to the unsolvability
threshold. It is currently unknown whether the 3x +1 problem is itself undecidable,
however no method is currently known to approach this question. The survey of
Michel and Margenstern [68] (in this volume) describes many results on generalized
3x + 1 functions that exhibit undecidable or dicult-to-decide iteration problems.
The 3x +1 function might conceivably belong to a smaller class of generalized 3x+1
functions that evade undecidability results that encode universal computers. Even
so, it conceivably might encode an undecidable problem, arising by another (un-
known) mechanism. As an example, could the following question be undecidable:
“Is there any positive integern such that T (k )(n ) > 1for 1 k  100 logn ?”

7. Hardness of the 3x +1 problem

Our viewpoint on hard problems has evolved since 1900, starting with Hilbert’s
program in logic and proof theory and beneﬁting from developments in the theory
of computation. Starting in the 1920’s, Emil Post uncovered great complexity in
studying some very simple computational problems, now called “Post Tag Systems”.
A ⋂∐˜ √↓√√̃⌉ in the classTS (θ↪ ) consists of a set of rules for transforming words
using letters from an alphabetA = –a1 ↪ ◃◃◃↪ aμ ˝ ofθ symbols, a deletion number (or
shift number)  1, and a set ofθ production rules

aj  w j := aj, 0aj, 1 ˇˇˇaj,n | ↪ 1  j  θ↪

in which the output w j is a ﬁnite string (or word) of lengthn j in the alphabet
A. Starting from an initial stringS a Tag system looks at the leftmost symbol of
S ,call itaj , then attaches to the right end of the string the wordw j , and ﬁnally
deletes the ﬁrst symbols of the resulting stringSw j , thus obtaining a new string
S . Here the “tag” is the set of symbolsw j attached to the end of the word, and the
iteration halts if a word of length less than is encountered. The[∐⌈√]{˜ √√}̂⌈̃⌉is
the question of deciding whether for an arbitrary initial wordS , iteration eventually
reaches the empty word. The √̃∐̂[∐̂]⌈]√↓ √√}̂⌈̃⌉is that of deciding whether, given
words S and ˜S , starting from wordS will ever produce word˜S under iteration. The
halting problem is a special case of the reachability problem. Post [78] reports that
in 1920–1921 he found a complete decision procedure
† for the caseθ =2 ↪ =2,
i.e. the classT (2↪2). He then tried to solve the caseθ =2 ↪ > 2, without success.

† P≀∫⊔ ⌈⟩⌈ \≀⊔ √⊓⌊↕⟩∫⟨ ⟨⟩∫ √∇≀≀{↙ A ⌈⌉⌋⟩∫⟩≀\ √∇≀⌋⌉⌈⊓∇⌉ {≀∇ ⌊≀⊔⟨ √∇≀⌊↕⌉⇕∫ ⟩∫ ≀⊓⊔↕⟩\⌉⌈ ⟩\ ⌈⌉
M≀↕ ∪73⊎↙

18 THE 3 x + 1 PROBLEM: AN OVERVIEW 17

He reported ♭78 ↪ p◃ ♯ that the special case` / , / with A / ı, ℘ and the
two production rules

↼◃↽ ρν w0 / ,  ρν w1 / 

already seemed to be an intractable problem◃ We shall term this problem

Post’s Original Tag Problem. Is there a recursive decision procedure for
the halting problem for the Tag system in T↼, ↽ given by the rules  ρν  and
 ρν ?
Leaving this question aside↪ Post considered the parameter range`¿ , /◃ He
wrote ♭78 ↪ p◃ ♯.
For a while the case / ,` ¿  seemed to be more promising↪
since it seemed to oer a greater chance of a ﬁnitely graded series
of problems◃ But when this possibility was explored in the early
summer of ↪ it rather led to an overwhelming confusion of
classes of cases↪ with the solution of the corresponding problem
depending more and more on problems of ordinary number theory◃
Since it had been our hope that the known diculties of number
theory would↪ as it were↪ be dissolved in the particularities of this
more primitive form of mathematics↪ the solution of the general
problem of “tag” appeared hopeless↪ and with it our entire program
of the solution of ﬁniteness problems◃

Discouraged by this↪ Post reversed course and went on to obtain a “Normal Form
Theorem” ↼♭77 ♯↽↪ published in the ’s↪ showing that a general logical problem
could be reduced to a form slightly more complicated than Tag Systems◃ In 
Marvin Minsky ♭ 70 ♯ proved that Post Tag Systems were undecidable problems in
general◃ In the next few years Hao Wang ♭94♯↪ J◃ Cocke and M◃ Minsky ♭13 ♯and
S◃ Ju◃ Maslov ♭66♯ independently showed undecidability for the subclass of Post
Tag Systems consisting of those with / ↪ thus showing that Post was right to
quit trying to solve problems in that class◃ At present the recursive solvability or
unsolvability in the classT↼,↽ remains open for all¿ ◃ Post’s original tag
problem↪ which is the halting problem for one special function inT↼, ↽↪ is still
unsolved↪ see Lisbeth De Mol ♭72 ♯↪ ♭74↪ p◃ ♯↪ and for further work ♭73♯↪ ♭75♯◃
Recently de Mol showed that the x⇁ problem can be encoded as a reachability
problem for a tag system inT↼, ↽ ↼♭74 ↪ Theorem ◃♯↽◃ This tag system encodes
the x ⇁  function↪ and the reachability problem is.
x ⇁ Tag Problem. Consider the tag system TC in T↼, ↽ with alphabet
A / ı, , ℘, deletion number  / , and production rules

 ρν ,  ρν ,  ρν .

For each n  , if one starts from the conﬁguration S / n , will the tag system
iteration for TC always reach state ˜S / ?
In  Kurt GΥodel ♭35 ♯ showed the existence of undecidable problems. he
showed that certain propositions were undecidable in any logical system com↩
plicated enough to include elementary number theory◃ This result showed that
Hilbert’s proof theory program could not be carried out◃ Developments in the the↩
ory of computation showed that one of GΥodel’s incompleteness results corresponded
to the unsolvability of the halting problem for Turing machines◃ This was based on

1918 JEFFREY C. LAGARIAS

the existence of a universal Turing machine, that could simulate any computation,
and in his 1937 foundational paper Alan Turing [] already showed one could be
constructed of a not very large size.

We now have a deeper appreciation of exactly how simple a problem can be
and still simulate a universal computer. Amazingly simple problems of this sort
have been found in recent years. Some of these involve cellular automata, a model
of computation developed by John von Neumann and Stansilaw M. Ulam in the
1950’s. One of these problems concerns the possible behavior of a very simple one-
dimensional nearest neighbor cellular automaton, Rule 110, using a nomenclature
introduced by Wolfram [ ], []. This rule was conjectured by Wolfram to give a
universal computer ([, Table 15], [, pp. 575–577]). It was proved to be weakly
universal by M. Cook (see Cook [ ], []). Here weakly universal means that the
initial conﬁguration of the cellular automaton is required to be ultimately periodic,
rather than ﬁnite. Another is John H. Conway’s game of “Life,” ﬁrst announced in
1970 in Martin Gardner’s column in Scientiﬁc American (Gardner [ ]), which is
a two-dimensional cellular automaton, having nearest neighbor interaction rules of
a particularly simple nature. Its universality as a computer was later established,
seeBerkelamp, Conwayand Guy[ , Chap. 25]. Further remarks on the size of
universal computers are given in the survey of Michel and Margenstern [ ] (in this
volume).

There are, however, reasons to suspect that the 3x + 1 function is not compli-
cated enough to be universal, i.e. to allow the encoding of a universal computer in
its input space. First of all, it is so simple to state that there seems very little room
in it to encode the elementary operations needed to create a universal computer.
Second, the 3x+ 1 conjecture asserts that the iteration halts on the domain of all
positive integer inputs, so for each integern, the valueF (n) of the largest integer
observed before visiting 1 is recursive. To encode a universal computer, one needs
to represent all recursive functions, including functions that grow far faster than
any given recursive functionF (n). It is hard to image how one can encode it here as
a question about the iteration, without enlarging the domain of inputs. Third, the
3x + 1 function possesses the feature that there is a nice (ﬁnitely additive) invari-
ant measure on the integers, with respect to which it is completely mixing under
iteration. This is the measure that assigns mass
1
2n to each complete arithmetic
progression (mod 2
n ), for eachn  1. This fundamental observation was made in
1976 by Terras [], and independently by Everett [] in 1977, see Lagarias [,
Theorem B] for a precise statement. This “mixing property” seems to ﬁght against
the amount of organization needed to encode a universal computer in the inputs.
We should caution that this observation by itself does not rule out the possibility
that, despite this mixing property, a universal computer could be encoded in a very
thin set of input values (of “measure zero”), compatible with an invariant measure.
It just makes it seem dicult to do. Indeed, the 1972 encoding of a universal com-
puter in the iteration of a certain generalized 3x+ 1 function found by Conway [ ]
(in this volume) has the undecidability encoded in the iteration of a very thin set
of integers. However Conway’s framework is dierent from the 3x + 1 problem in
that the halting function he considers is partially deﬁned.

Even if iteration of the 3x + 1 function is not universal, it could still potentially
be unsolvable. Abstractly, there may exist in an axiomatic system statements
F (n) for a positive integer predicate, such thatF (1),F (2),F (3), ... areprovablein

20 THE 3 x + 1 PROBLEM: AN OVERVIEW 19

the system for all integern↪ but the statement ↼n↽F ↼n↽ is not provable within
the system◃ For example↪ one can letF ↼n↽ encode a statement that there is no
contradiction in a system obtainable by a proof of length at mostn◃ If the system
is consistent↪ thenF ↼↽,F ↼↽, ... will all individually be provable◃ The statement
↼n↽F ↼n↽ then encodes the consistency of the system◃ But the consistency of a
system suciently complicated to include elementary number theory cannot be
proved within the system↪ according to GΥodel’s second incompleteness theorem◃
The pseudo↩randomness or “mixing” behavior of the x ⇁  function also seems
to make it extremely resistant to analysis◃ If one could rigorously show a su↩
cient amount of mixing is guaranteed to occur↪ in a controlled number of iterations
in terms of the input sizen↪ then one could settle part of the x ⇁  conjecture↪
namely prove the non↩existence of divergent trajectories◃ Here we have the funda↩
mental diculty of proving in eect that the iterations actually do have an explicit
pseudo↩random property◃ Besides this diculty↪ there remains a second fundamen↩
tal diculty. solving the number↩theoretic problem of ruling out the existence of an
enormously long non↩trivial cycle of the x ⇁  function◃ This problem also seems
unapproachable at present by known methods of number theory◃ However the ﬁ↩
nite cycles problem does admit proof of partial results↪ showing the nonexistence
of non↩trivial cycles having particular patterns of even and odd iterates◃
A currently active and important general area of research concerns the con↩
struction of pseudo↩random number generators. these are deterministic recipes
that produce apparently random outputs ↼see Knuth ♭ ↪ Chap◃ ♯↽◃ More pre↩
cisely↪ one is interested in methods that take as inputn truly random bits and
deterministically produce as outputn ⇁  “random↩looking” bits◃ These bits are to
be “random↩looking” in the sense that they appear random with respect to a given
family of statistical tests↪ and the output is then said to be pseudo↩random with
respect to this family of tests◃ Deciding whether pseudo↩random number generators
exist for statistical tests in various complexity classes is now seen as a fundamental
question in computer science↪ related to theP / NP probem↪ see for example Gol↩
dreich ♭♯↪ ♭♯◃ It may be that resolving the issue of the pseudo↩random character
of iterating the x ⇁  problem will require shedding light on the general existence
problem for pseudo↩random number generators◃
All we can say at present is that the x ⇁  problem appears very hard indeed◃
It now seems less surprising than it might have once seemed that a problem as
simple↩looking as this one could be genuinely dicult↪ and inaccessible to known
methods of attack◃
 . Future Prospects

We observe ﬁrst that further improvements are surely possible on the “world
records” ↼W↽–↼W↽ above◃ In particular↪ concerning ↼W↽↪ it seems scandalous
that it is not known whether or not there are inﬁnitely many positive integersn
which iterate to  under the x ⇁ map T↼x↽ and take at least the “average”
number 2
log 4 /3 logn 	 . logn steps to do so◃ Here the stochastic models for
the x ⇁  iteration predict that at least half of all positive integers should have
this propertyω These “world records” are particularly worth improving if they can
shed more light on the problem◃ This could be the case for world record ↼↽↪ where
there is an underlying structure for obtaining lower bounds on the exponent↪ which
involves an inﬁnite family of nonlinear programs of increasing complexity ↼♭♯↽◃

2120 JEFFREY C. LAGARIAS

Analysis of the 3x+ 1 problem has resulted in the formulation of a large set of
“easier” problems. At ﬁrst glance some of these seem approachable, but they also
remain unsolved, and are apparently dicult. As samples, these include:
(C1) (Finite Cycles Conjecture)Does the 3x + 1 function have ﬁnitely many
cycles (i.e. ﬁnitely many purely periodic orbits on the integers)? This is
conjectured to be the case.
(C2) (Divergent Trajectories Conjecture-1)Does the 3x + 1 function have a
divergent trajectory, i.e., an integer starting value whose iterates are un-
bounded? This is conjecturednot to be the case.
(C3) (Divergent Trajectories Conjecture-2)Does the 5x + 1 function have a
divergent trajectory? This is conjectured to be the case.
(C4) (Inﬁnite Permutations-Periodic Orbits Conjecture) If a generalized Collatz
function permutes the integers and is not globally of ﬁnite order, is it
true that it has only ﬁnitely many periodic orbits? The original Collatz
functionU (n ), which is a permutation, was long ago conjectured to have
ﬁnitely many cycles. A conjecture of this kind, imposing extra conditions
on the permutation, was formulated by Venturini [93, p. 303 top].
(C5) (Inﬁnite Permutations-Zero Density Conjecture) If a generalized Collatz
function permutes the integers, is it true that every orbit has a (natural)
density? Under some extra hypotheses one may conjecture that all such
orbits have density zero; compare Venturini [93, Sec. 6].

Besides these conjectures, there also exist open problems which may be more
accessible. One of the most intriguing of them concerns establishing lower bounds
for the number  1(x) of integers less thanx that get to 1 under the 3x + 1 iteration.
As mentioned earlier it is known ([57]) that there is a positive constantc0 such
that  1(x) >c 0 x0.84 ◃
It remainsanopenproblem to show that foreach> 0 there exists a positive
constantc() such that  1(x) >c ()x1− π◃
Many other speciﬁc, but dicult, conjectures for study can be found in the papers
in this volume, starting with the problems listed in Guy [40].
We now raise some further research directions, related to the papers in this
volume. A ﬁrst research direction is to extend the class of functions for which the
Markov models of Matthews [ 67] can be analyzed. Matthews shows that the class of
generalized 3x + 1 functions of relatively prime type ([67, Sec. 2]) is analyzable. He
formulates some conjectures for exploration. It would be interesting to characterize
the possibled-adic invariant measures for arbitrary generalized Collatz functions.
It may be necessary to restrict to subclasses of such functions in order to obtain
nice characterizations.
A second research direction concerns the class of generalized 3x + 1 functions
whose iterations extended to the set ofd-adic integers are ergodic with respect to
the d-adic measure, cf. Matthews [67, Sec. 6]).
Research Problem. Does the class of generalized Collatz functions of rela-
tively prime type contain a function which is ergodic with respect to the standard
d-adic measure, whose iterations can simulate a universal computer? Speciﬁcially,
could it have an unsolvable iteration problem of the form: “Given positive integers

22 THE 3 x + 1 PROBLEM: AN OVERVIEW 21

↼n, m↽ as input, does there existk such that thek-th iterateT(k )↼n↽ equalsm?”
Or does ergodicity of the iteration preclude the possibility of simulating universal
computation?
A third research direction concerns the fact that generalized Collatz functions
have now been found in many other mathematical structures↪ especially if one
generalizes further to integer↩valued functions that are piecewise polynomial on
residue classes ↼ modd↽◃ These functions are the quasi↩polynomial functions noted
above↪ and they show up in a number of algebraic contexts↪ particularly in counting
lattice points in various regions◃ It may prove worthwhile to study the iteration
of various special classes of quasi↩polynomial functions arising in these algebraic
contexts◃
At this point in time↪ in view of the intractability of problems ↼C↽–↼C↽ it
also seems a sensible task to formulate a new collection of even simpler “toy prob↩
lems”↪ which may potentially be approachable◃ These may involve either changing
the problem or importing it into new contexts◃ For example↪ there appear to be
accessible open problems concerning variants of the problem acting on ﬁnite rings
↼Hicks et al◃ ♭ ♯↽◃ Another promising recent direction is the connection of these
problems with generating sets for multiplicative arithmetical semigroups↪ noted by
Farkas ♭ ♯◃ This has led to a family of more accessible problems↪ where various re↩
sults can be rigorously established ↼♭♯↽◃ Here signiﬁcant unsolved problems remain
concerning the structure of such arithmetical semigroups◃ Finally it may prove
proﬁtable to continue the study↪ initiated by Klarner and Rado ♭♯↪ of sets of in↩
tegers ↼or integer vectors↽ closed under the action of a ﬁnitely generated semigroup
of ane maps◃
 . Is the x ⇁ problem a “good” problem⋆

There has been much discussion of what constitutes a good mathematical prob↩
lem◃ We can not do better than to recall the discussion of Hilbert ♭ ♯inhis famous
 problem list◃ On the importance of problems he said ↼♭ ↪ p◃ ♯↽.
The deep signiﬁcance of certain problems for the advance of math↩
ematical science in general↪ and the important role they play in
the work of the individual investigator↪ are not to be denied◃ As
long as a branch of science oers an abundance of problems↪ so
long is it alive, a lack of problems foreshadows extinction or the
cessation of independent development◃ Just as every human un↩
dertaking pursues certain objects↪ so also mathematical research
requires its problems◃ It is also by the solution of problems that
the investigator tests the temper of his steel, he ﬁnds new methods
and new outlooks↪ and gains a wider and freer horizon◃

Hilbert puts forward three criteria that a good mathematical problem ought to
satisfy.
It is dicult and often impossible to judge the value of a problem
correctly in advance, for the ﬁnal award depends upon the gain
which science obtains from the problem◃ Nevertheless we can ask
whether there are general criteria which mark a good mathematical
problem◃ An old French mathematician said. “A mathematical
theory is not to be considered complete until you have made it so
 2322 JEFFREY C. LAGARIAS

clear that you can explain it to the ﬁrst man that you meet on the
street.” This clearness and ease of comprehension, here insisted
on for a mathematical theory, I should still more demand for a
mathematical problem if it is to be perfect; for what is clear and
easily comprehended attracts, the complicated repels us.
Moreover a mathematical problem should be dicult in order
to entice us, but not completely inaccessible, lest it mock at our
eorts. It should be to us a guide post on the mazy paths to hidden
truths, and ultimately a reminder of our pleasure in its successful
solution.

From the viewpoint of the Hilbert criteria for a good problem, we see that:

(1) The 3x + 1 problem is a clear, simply stated problem;

(2) The 3x + 1 problem is a dicult problem;

(3) The 3x + 1 problem initially seems accessible, in that it possesses a fairly
intricate internal structure.
But – and it is a big “but” – the evidence so far suggests that obtaining a proof
of the 3x+1 problem is inaccessible! Not only does this goal appear inaccessible, but
various simpliﬁed conjectures derived from it appear to be completely inaccessible
in their turn, leading to a regress to formulation of a series of simpler and simpler
inaccessible problems, namely conjectures (C1)–(C5) listed inΣ8.
We conclude that the 3x + 1 problem comes close to being a “perfect” problem
in the Hilbert sense. However it seems to fail the last of Hilbert’s requirements: It
mocks our eorts! It is possible to work hard on this problem to no result. It is
deﬁnitely a dangerous problem! It could well be that the 3x + 1 problem remains
out of human reach. But maybe not. Who knows?

10. Working on the 3x +1 probem

Whether or not the 3x + 1 problem is a “good” problem, it is not going away,
due to its extreme accessibility. It oers a large and tantalizing variety of patterns
in computer experiments. This problem stands as a mathematical challenge for the
21-st century.
In working on this problem, the most cautious advice, following Richard Guy
[40]is:
Don’t try to solve these problemsω
But, as Guy said [40, p. 35], some of you may be already scribbling, in spite of the
warning!

We also note that Paul Erd˝os said, in conversation, about its diculty ([25]):

“Hopeless. Absolutely hopeless.”

In Erd˝os-speak, this means that there are no known methods of approach which
gave any promise of solving the problem. For other examples of Erd˝os’s use of the
term “hopeless” see ErdΥos and Graham [26 , pp. 1, 27, 66, 105].
At this point we may recall further advice of David Hilbert [49, p. 442] about
problem solving:

24 THE 3 x + 1 PROBLEM: AN OVERVIEW 23

If we do not succeed in solving a mathematical problem↪ the rea↩
son frequently consists in our failure to recognize the more general
standpoint from which the problem before us appears only as a
single link in a chain of related problems◃ After ﬁnding this stand↩
point↪ not only is this problem frequently more accessible to our
investigation↪ but at the same time we come into possession of a
method that is applicable to related problems◃

The quest for generalization cuts in two directions↪ for Hilbert also says ♭49 ↪ p◃ ♯.
He who seeks for methods without having a deﬁnite problem in
mind seeks for the most part in vain◃

Taking this advice into account↪ researchers have treated many generalizations
of the x ⇁  problem↪ which are reported on in this volume◃ One can consider
searching for general methods that apply to a large variety of related iterations◃
Such general methods as are known give useful information↪ and answer some ques↩
tions about iterates of the x⇁  function◃ Nevertheless it is fair to say that they
do not begin to answer the central question.
What is the ultimate fate under iteration of such maps over all time⋆
My personal viewpointisthatthe x ⇁  problem is somewhat dangerous↪ and
that it is prudent not to focus on resolving the x⇁  conjecture as an immediate
goal◃ Rather↪ one might ﬁrst look for more structure in the problem◃ Also one
might proﬁtably view the problem as a “test case”↪ to which one may from time
to time apply new results arising from the ongoing development of mathematics◃
When new theories and new methods are discovered↪ the x ⇁ problem may be
used as a testbed to assess their power↪ whenever circumstances permit◃
To conclude↪ let us remind ourselves↪ following Hilbert ♭49↪ p◃ ♯.
The mathematicians of past centuries were accustomed to devote
themselves to the solution of dicult particular problems with pas↩
sionate zeal◃ They knew the value of dicult problems◃

The x ⇁  problem stands before us as a beautifully simple question◃ It is hard
to resist exploring its structure◃ We should not exclude it from the mathematical
universe just because we are unhappy with its diculty◃ It is a fascinating and
addictive problem◃

Acknowledgments. I am grateful to Michael Zieve and Steven J◃ Miller each
for detailed readings and corrections◃ Marc Chamberland↪ Alex Kontorovich↪ and
Keith R◃ Matthews also made many helpful comments◃ I thank Andreas Blass for
useful comments on incompleteness results and algebraic structures◃ The author
was supported by NSF Grants DMS↩ and DMS↩◃

References

[1] E. Akin, ⋂[̃ ˜̃{̃√∐⌈ √}√}⌈}˜↓ }̃ ̂↓{∐⌉]̂∐⌈ √↓√√̃⌉√∕ Graduate Studies in Mathematics 1.,
American Mathetmatical Society,Providence, RI 1993.
[2] E. Akin, Why is the 3 § + 1 Problem Hard?, In: [∐√̃⌈ ∮]⌈⌈ 〉√˜}̂]̂ ⋂[̃}√↓ ⋁}√⌋√[}√√ (I.
Assani, Ed.), Contemp. Math. vol 356, Amer. Math. Soc. 2004, pp. 1–20.
[3] D. Applegate and J. C. Lagarias, Lowe r bounds for the total stopping time of 3 § + 1 iterates,
Math. Comp. 72 (2003), 1035–1049.
[4] D. Applegate and J. C. Lagarias (2006), The 3 § +1 semigroup, J. Number Theory 177 (2006),
146–159.
 2524 JEFFREY C. LAGARIAS

[5] A. Barvinok, Integer Points in Polyhedra, European Math.Soc. Publishing, ETH, ZΥ urich
2008.
[6] M. Beck and S. Robins, Computing the continuous discretely◃ Integer↩point enumeration in
polyhedraΓ Springer: New York 2007.
[7] E.R.Berlekamp, J.H.Conwayand R. K.Guy, Winning Ways for Your Mathematical Plays↪
Volume  ↼Second Revised Edition↽ A. K. Peters, Ltd. 2004.
[8] T. Brox, Collatz cycles with few descents, Acta Arithmetica92 (2000), 181–188.
[9] W. Bruns and J. Herzog, Cohen↩Macaulay rings , Cambridge Univ. Press: Cambridge 1993.
[10] W. Bruns and B. Ichim, On the coecients of Hilbert quasipolynomials, Proc. Amer. Math.
Soc. 135 (2007), No. 5, 1305-1308.
[11] M. Chamberland, A 3 x + 1 Survey: Number theory and dynam ical systems, in this volume.
[12] V. Chvatal, D. Klarner and D. E. Knuth, Selected combinatorial research problems, Stanford
Computer Science Dept. Technical Report STAN-CS-72-292 June 1972, 31 pages.
[13] J. Cocke and M. Minsky, Universality of tag systems with P = 2, Journal of the ACM 11,
(1964), No. 1, 15–20.
[14] L. Collatz, Letter to Michael E. Mays, dated 17 Sept. 1980.
[15] L. Collatz, On the motivation and origin of the (3n + 1)- problem (Chinese), J. Qufu Normal
University, Natural Science Edition [Qufu shi fan da xue xue bao]12 (1986), No. 3, 9–11.
[16] J. H. Conway, Unpredictable Iterations, Proc. 1972 Number Theory Conference (Univ. Col-
orado, Boulder, Colo., 1972 ), pp. 49–52. Univ. Colorado, Boulder, Colo. 1972.
[17] J. H. Conway, FRACTRAN: A Simple Universal Computing Language for Arithmetic, In:
Open Problems in Communication and Computation (T.M.Cover andB.Gopinath,Eds.),
Springer-Verlag: New York 1987, pp. 3-27 [Reprinted in this volume]
[18] M. Cook, Universality in elementary cellular automata, Complex Systems 15 (2004), 1–40.
[19] M. Cook, A concrete view of rule 110 computation, T. Neary, D. Woods, A. K. Seda and N.
Murphy (Eds.), Proceedings International Workshop on The Complexity of Simple Programs
↼CSP ↽ , EPCTS (Electronic Proceedings in Theoretical Computer Science) 1 (2009),
31–55.
[20] M. Cook, D. Soloveichik, E. Winfree and J. B ruck, Programmability of Chemical Reaction
Networks, to appear in a Festschrift for Grzegorz Rozenberg, Springer-Verlag.
[21] Necia Grant Cooper (Ed), From Cardinals to Chaos◃ Reﬂections on the life and legacy of
Stanslaw Ulam , Cambridge Univ. Press: Cambridge 1989 [Reprint of Los Alamos Science,
Vol. 15.]
[22] H. S. M. Coxeter, Cyclic sequences and frieze patterns: The Fourth Felix Behrend Memorial
Lecture), Vinculum 8 (1971), 4–7. [Reprinted in this volume]
[23] L. Ehrhart, Sur un probl‘eme de geom etrie diophantienne lineaire. II. Syst‘emes diophantiens
lineaires, J. Reine Angew. Math. 227 (1967), 25–49.
[24] S. Eliahou, The 3x +1 problem: new lower bounds on nontrivial cycle lengths, Discrete Math.
118 (1993), 45–56.
[25] P. Erd˝os, Private communication with J. C. Lagarias.
[26] Paul Erd˝os and R. L. Graham, Old and new problems and results in combinatorial num↩
ber theory Monographie No. 28 de L’Enseignement Math ematique, Kundig: Geneva 1980.
(Chapter 1 appeared in: Enseign. Math. 25 (1979), no. 3-4, 325–344. )
[27] C. J. Everett, Iteration of the number theoretic functionf (2n)= n, f (2n +1 ) = 3 n +2,
Advances in Math. 25 (1977), 42–45.
[28] A. Evseev, Higman’s PORC conjecture for a family of groups, Bull. London Math. Soc. 40
(2008), 405–414.
[29] H. M. Farkas, Variants of the 3N + 1 conjecture and multiplicative semigroups, in:Geometry↪
spectral theory↪ groups↪ and dynamics, pp. 121–127, Contemp. Math. Vol 387, Amer. Math.
Soc.: Providence, RI 2005.
[30] H. Furstenberg, Recurrence in ergodic theory and combinatorial number theory↪ Princeton
University Press, Princeton, NJ 1981.
[31] M. Gardner, Mathematical Games, Scientiﬁc American 223 (1970) Number 4 (October),
120–123.
[32] M. Gardner, Mathematical Games, Scientiﬁc American 226 (1972) Number 6 (June), 114–
118.
[33] S. Garoufalidis, The degree of aq-holonomic sequence is a quadratic quasi-polynomial, eprint:
arxiv..v

26 THE 3 x + 1 PROBLEM: AN OVERVIEW 25

♭♯ E◃ Glasner↪Ergodic Theory via joinings, Mathematical Surveys and Monographs↪ Vol◃ ↪
American Mathematical Society↪ Providence↪ RI↪ ◃
♭♯ K◃ GΥodel↪ ΥUber formal unentscheidbare SΥatzes der Principia Mathematica und verwandter
Systeme I↪ ♭On formally undecidable propositions ofPrincipia mathematica and related sys↩
tems I♯ MΥonatshefte fΥur Mathematik und Physik 28 ↼↽↪ –◃ ↼English translation in
♭36↪ p◃ –♯◃↽
♭♯ K◃ GΥodel↪ Collected Works, Volume I. Publications 1929–1936, S◃ Feferman et al◃ ↼Eds◃↽ ↪
Oxford University Press. New York ◃
♭♯ O◃ Goldreich↪Foundations of cryptography. Basic tools. Cambridge University Press. Cam↩
bridge ◃
♭♯ O◃ Goldreich↪A Primer on Pseudorandom Generators, University Lecture Series↪ No◃ ↪
American Math◃ Society. Providence↪ RI ◃
♭♯ K◃ Greenberg↪ Integer valued functions on the integers↪ Math◃ Medley17 ↼↽↪ –◃
♭♯ R◃ K◃ Guy↪ Don’t try to solve these problemsω↪ American Math◃ Monthly 90 ↼↽↪ –◃
♭Reprinted in this volume♯
♭♯ R◃ K◃ Guy↪ Conway’s prime↩producing machine↪ Math◃ Magazine 56 ↼↽↪ no◃ ↪ –◃
♭♯ R◃ K◃ Guy↪ Unsolved Problems in Number Theory. Third Edition. Problem Books in Mathe↩
matics↪ Springer↩Verlag. New York ◃
♭♯ R◃ K◃ Guy↪ private communication↪ ◃
♭♯ H◃ Hasse↪Unsolved Problems in Elementary Number Theory ↪ Lectures at University of Maine
↼Orono↽↪ Spring ↪ Mimeographied notes◃
♭♯ B◃ Hasselblatt and A◃ B◃ Katok↪ Introduction to the modern theory of dynamical systems,
Cambridge Univ◃ Press↪ Cambridge ◃
♭♯ B◃ Hayes↪ Computer recreations. The ups and downs of hailstone numbers↪ Scientiﬁc Ameri↩
can 250 ↪ No◃ ↪ ↼↽↪ –◃
♭♯ K◃ Hicks↪ G◃ L◃ Mullen↪ J◃ L◃ Yucas and R◃ Zavislak↪ A Polynomial Analogue of the  N ⇁
Problem⋆↪ American Math◃ Monthly 115 ↼↽↪ No◃ ↪ –◃
♭♯ G◃ Higman↪ Enumerating p↩groups II. Problems whose solution is PORC↪ Proc◃ London Math◃
Soc◃ 10 ↼↽↪ –◃
♭♯ D◃ Hilbert↪ Mathematische Probleme↪ GΥottinger Nachrichten ↼↽ –◃ Reprinted in.
Archiv der Mathematik und Physik↪ rd Ser◃ 1 ↼↽ ↩ and ↩◃ ↼English translation.
Mathematical Problems↪ Bull◃ Amer◃ Math◃ Soc◃ 8 ↼↽ –◃ Reprinted in. Mathemati-
cal Developments Arising From Hilbert Problems ↪ Proc◃ Symp◃ Pure Math◃ Volume ↪ AMS.
Providence ↪ pp◃ ↩◃↽
♭♯ A◃ J◃ W◃ Hilton↪ private communication↪ ◃
♭♯ S◃ D◃ Isard and H◃ M◃ Zwicky↪ Three open questions in the theory of one↩symbol Smullyan
systems↪ SIGACT News↪ Issue No◃ ↪ ↪ –◃
♭♯ M◃ Klamkin↪ Problem  − ⎪↪SIAMReview 5 ↼↽↪ –◃
♭♯ D◃ A◃ Klarner↪ A sucient condition for certain semigroups to be free↪ Journal of Algebra74
↼↽↪ –◃
♭♯ D◃ A◃ Klarner and R◃ Rado↪ Arithmetic propert ies of certain recursively deﬁned sets↪ Paciﬁc
J◃ Math◃ 53 ↼↽↪ No◃ ↪ –◃
♭♯ D◃ E◃ Knuth↪ The Art of Computer Programming. Vol 2. Seminumerical Algorithms. Second
Edition. Addison↩Wesley. Reading↪ MA ◃
♭♯ A◃V◃ Kontorovich and J◃ C◃ Lagarias↪ Stochastic models for the x ⇁  problem and general↩
izations↪ paper in this volume◃
♭♯ I◃ Krasikov and J◃ C◃ Lagarias↪ Bounds for the x ⇁  problem using dierence inequalities↪
Acta Arith◃ 109 ↼↽↪ no◃ ↪ –◃
♭♯ J◃ C◃ Lagarias↪ The x ⇁  problem and its generalizations↪ Amer◃ Math◃ Monthly 92 ↼↽↪
–◃ ♭Reprinted with corrections in this volume♯◃
♭♯ J◃ C◃ Lagarias↪ The set of rational cycles for the x ⇁  problem↪ Acta Arithmetica 56 ↼↽↪
–◃
♭♯ J◃ C◃ Lagarias↪ The x⇁  Problem. An Annotated Bibliography ↼↩↽↪ paper in this
volume◃
♭♯ J◃ C◃ Lagarias↪ The x ⇁  Problem. An Annotated Bibliography↪ II ↼↩↽↪
⊣∇X⟩⊑¬⇕⊣⊔⟨∝′̸′∀∈′∀◃
♭♯ J◃ C◃ Lagarias and A◃ Weiss↪ The  x ⇁  problem. Two stochastic models↪ Annals of Applied
Probability2 ↼↽↪ –◃
 2726 JEFFREY C. LAGARIAS

[63] H. Lausch and W. NΥ obauer, Algebra of Polynomials, North-Holland Publ. Co.: Amsterdam
1973.
[64] K. Mahler, Lectures on diophantine approximations◃ Part I◃ g↩adic number and Roth’s the↩
orem . Prepared from notes of R. P. Bambah of lectures given at Univ. of Notre Dame in the
Fall of 1957, Univ. of Notre Dame Press, Notre Dame, Ind. 1961, xi+188pp.
[65] M. Mashaal, Bourbaki. A Secret Society of Mathematicians◃ (Translated from 2002 French
original by A. Pierrehumbert) American Math. Society, Providence RI 2006.
[66] S. Ju. Maslov, On E. L. Post’s “tag problem” (Russian), Trudy Mat. Inst. Steklov 72 91964),
57–68. [English translation: American Math. Soc.Translations, Series 2, Vol. 97 (1970), 1–14.]
[67] K. R. Matthews, Generalized 3 x + 1 mappings: Markov chains and ergodic theory, paper in
this volume.
[68] P. Michel and M. Margenstern, Generalized 3 x + 1 functions and the theory of computation,
paper in this volume.
[69] S. J. Miller and R. Takloo-Bighash,An invitation to modern number theory↪ Princeton Uni-
versity Press: Princeton NJ 2006.
[70] M. Minsky, Recursive unsolvability of Post’s problem of tag and other topics in the theory of
Turing machines, Annals of Mathematics 74 (1961), 437–455.
[71] M. Minsky, Computation. Finite and Inﬁnite Machines , Prentice-Hall, Inc: Engelwood Clis,
NJ 1967.
[72] L. De Mol, Closing the circle: An analysis of Emil Post’s Early Work, Bull. Symbolic Logic
12 (2006), No. 2, 267–289.
[73] L. De Mol, Study of limits of solvability in tag systems, pp. 170–181 in: J. Durand-Lose,
M. Margenstern (Eds.), Machines↪ Computations↪ Universality↪ MCU  , Lecture Notes
in Computer Science, vol. 4664, Springer-Verlag: New York 2007.
[74] L. De Mol, Tag systems and Collatz-like functions, Theoretical Computer Science290 (2008),
92–101.
[75] L. De Mol, On the boundaries of solvability and unsolvability in tag systems. Theoretical
and experimental results., in: T. Neary, D. Woods, A. K. Seda and N. Murphy (Eds.),
Proceedings International Workshop on The Complexity of Simple Programs ↼CSP ↽ ,
EPCTS (Electronic Proceedings in Theoretical Computer Science) 1 (2009), 56–66.
[76] T. Oliveira e Silva, Empirical veriﬁcation of the 3x + 1 and related conjectures, paper in this
volume.
[77] E. L. Post, Formal reductions of the general combinatorial decision problem, Amer. J. Math.
65 (1943), 197–215.
[78] E. L. Post, Absolutely unsolvable problems and relatively undecidable propositions- account
of an anticipation, in: M. Davis, Ed.,The Undecidable◃ Basic Papers on Undecidable Propo↩
sitions↪ Unsolvable Problems and Computable Functions↪ Raven Press: New York 1965.
(Reprint: Dover Publications, 2004).
[79] Eric Roosendaal, On the 3x + 1 problem, web document, available at:
http.▹▹www.ericr.nl▹wondrous▹index.html
[80] J. Roubaud, Un probleme combinatoire posepar poesie lyrique des troubadours,
Matematiques et Sciences Humaines 27 Autumn 1969, 5–12.
[81] Klaus Schmidt, Dynamical Systems of Algebraic Origin . Progress in Math., 128. BirkhΥauser
Verlag: Basel 1995.
[82] J. Silverman,The Arithmetic of Dynamical Systems◃ Springer-Verlag: New York 2007.
[83] J. Simons and B. de Weger, Theoretical and computational bounds for m -cycles of the 3n +1
problem, Acta Arithmetica 117 (2005), 51–70.
[84] Ya. G. Sinai, Statistical (3X + 1)-Problem, Dedicated to the memory of JΥ urgen K. Moser.
Comm. Pure Appl. Math. 56 No. 7 (2003), 1016–1028.
[85] Ya. G. Sinai, Uniform distribution in the (3x + 1) problem, Moscow Math. Journal 3 (2003),
No. 4, 1429–1440. (S. P. Novikov 65-th birthday issue).
[86] D. Soloveichik, M. Cook E. Winfree and J. Bruck, Computation with ﬁnite stochastic chemical
reaction networks, Natural Computing 7 (2008), 615–633.
[87] Paul R. Stein, Iteration of maps, strange attractors, and number theory-an Ulamian pot-
pourri, pp. 91–106 in [21].
[88] R. Terras, A stopping time problem on the positive integers, Acta Arithmetica30 (1976),
241–252.
[89] R. Terras, On the existence of a density, Acta Arithmetica35 (1979), 101–102.

28 THE 3 x + 1 PROBLEM: AN OVERVIEW 27

♭♯ B◃ Thwaites↪ My conjecture↪ Bull◃ Inst◃ Math◃ Appl◃21 ↼↽↪ –◃
♭♯ A◃ M◃ Turing↪ On computable numbers↪ with an application to the Entschidungsproblem↪
Proc◃ London Math◃ Soc◃ 42 ↼↽↪ –◃ Corrections↪43 ↼↽↪ –◃
♭♯ S◃ Ulam↪ Problems in Modern Mathematics,John Wiley and Sons. New York ◃
♭♯ G◃ Venturini↪ On a generalization of the x⇁ problem↪ Adv◃ Appl◃ Math◃ 19 ↼↽↪ –◃
♭♯ Hao Wang↪ Tag systems and lag systems↪ Math◃ Annalen 152 ↼↽↪ –◃
♭♯ G◃ J◃ Wirsching↪The Dynamical System Generated by then ⇁ Function↪ Lecture Notes in
Math◃ No◃ ↪ Springer↩Verlag. Berlin ◃
♭♯ S◃ Wolfram↪ Statistical mechanics of cellular automata↪ Rev◃ Mod◃ Phys◃55 ↼↽↪ ↩◃↩
♭♯ S◃ Wolfram↪ Universality and complexity and cellular automata↪ Physica C 10 ↼↽↪ –◃
♭♯ S◃ Wolfram↪ Theory and Applications of Cellular Automata,World Scientiﬁc. Singapore
◃
♭♯ S◃ Wolfram↪ Cellular Automata and Complexity: Collected Papers,Westview Press. Perseus
Books Group ◃

Department of Mathematics, University of Michigan, Ann Arbor, MI 48109-1109
E-mail address. ⌈∐˜∐√]∐√√⌉]̂[∕̃̂√
 29
