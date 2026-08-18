<!-- source: https://ar5iv.labs.arxiv.org/html/2111.02635 | converted from HTML -->

[2111.02635] The + ⁢ 3 x 1 Problem: An Overview

Reference. The Ultimate Challenge: The 3 ​ x + 1 3x+1 Problem. Edited by Jeffrey C. Lagarias. American Mathematical Society, Providence, RI, 2010, pp. 3–29.

# The 3 ​ x + 1 3x+1 Problem: An Overview

Jeffrey C. Lagarias Address: Department of Mathematics, University of Michigan, Ann Arbor, MI 48109-1043 Email address: [lagarias@umich.edu][1]

## 1. Introduction

The 3 ​ x + 1 3x+1 problem concerns the following innocent seeming arithmetic procedure applied to integers: If an integer x x is odd then “multiply by three and add one”, while if it is even then “divide by two”. This operation is described by the Collatz function

 | C ⁡ ( x) = { 3 ​ x + 1 if ​ x ≡ 1 ( mod 2), x 2 if ​ x ≡ 0 ( mod 2). C(x)=\left\{\begin{array}[]{cl}3x+1&\mbox{if}~x\equiv 1~~(\bmod~2),\\ \\ \displaystyle\frac{x}{2}&\mbox{if}~~x\equiv 0~~(\bmod~2).\end{array}\right. |  |

The 3 ​ x + 1 3x+1 problem, which is often called the Collatz problem, concerns the behavior of this function under iteration, starting with a given positive integer n n.

3 ​ x + 1 3x+1 Conjecture. Starting from any positive integer n n, iterations of the function C ⁡ ( x) C(x) will eventually reach the number 1 1. Thereafter iterations will cycle, taking successive values 1, 4, 2, 1, … 1,4,2,1,....

This problem goes under many other names, including the Syracuse problem, Hasse’s algorithm, Kakutani’s problem and Ulam’s problem.

A commonly used reformulation of the 3 ​ x + 1 3x+1 problem iterates a different function, the 3 ​ x + 1 3x+1 function, given by

 | T ⁡ ( x) = { 3 ​ x + 1 2 if ​ x ≡ 1 ( mod 2), x 2 if ​ x ≡ 0 ( mod 2). T(x)=\left\{\begin{array}[]{cl}\displaystyle\frac{3x+1}{2}&\mbox{if}~x\equiv 1~~(\bmod~2),\\ \\ \displaystyle\frac{x}{2}&\mbox{if}~~x\equiv 0~~(\bmod~2).\end{array}\right. |  |

From the viewpoint of iteration the two functions are simply related; iteration of T ⁡ ( x) T(x) simply omits some steps in the iteration of the Collatz function C ⁡ ( x) C(x). The relation of the 3 ​ x + 1 3x+1 function T ⁡ ( x) T(x) to the Collatz function C ⁡ ( x) C(x) is that:

 | T ⁡ ( x) = { C ⁡ ( C ⁡ ( x)) if ​ x ≡ 1 ( mod 2), C ⁡ ( x) if ​ x ≡ 0 ( mod 2). T(x)=\left\{\begin{array}[]{cl}C(C(x))&\mbox{if}~x\equiv 1~~(\bmod~2)~,\\ \\ C(x)&\mbox{if}~~x\equiv 0~~(\bmod~2)~.\end{array}\right. |  |

As it turns out, the function T ⁡ ( x) T(x) proves more convenient for analysis of the problem in a number of significant ways, as first observed independently by Riho Terras ( [88], [89]) and by C. J. Everett [27].

The 3 ​ x + 1 3x+1 problem has fascinated mathematicians and non-mathematicians alike. It has been studied by mathematicians, physicists, and computer scientists. It remains an unsolved problem, which appears to be extremely difficult.

This paper aims to address two questions:

1. (1)

What can mathematics currently say about this problem?

2. (2)

How can this problem be hard, when it is so easy to state?

To address the first question, this overview discusses the history of work on the problem. Then it describes generalizations of the problem, and lists the different fields of mathematics on which the problem impinges. It gives a brief summary of the current strongest results on the problem.

Besides the results summarized here, this volume contains more detailed surveys of mathematicians’ understanding of the 3 ​ x + 1 3x+1 problem and its generalizations. These cover both rigorously proved results and heuristic predictions made using probabilistic models. The book includes several survey articles, it reprints several early papers on the problem, with commentary, and it presents an annotated bibliography of work on the problem and its generalizations.

To address the second question, let us remark first that the true level of difficulty of any problem can only be determined when (and if) it is solved. Thus there can be no definitive answer regarding its difficulty. The track record on the 3 ​ x + 1 3x+1 problem so far suggests that this is an extraordinarily difficult problem, completely out of reach of present day mathematics. Here we will only say that part of the difficulty appears to reside in an inability to analyze the pseudorandom nature of successive iterates of T ⁡ ( x) T(x), which could conceivably encode very difficult computational problems. We elaborate on this answer in §7.

Is the 3 ​ x + 1 3x+1 problem an important problem? Perhaps not for its individual sake, where it merely stands as a challenge. It seems to be a prototypical example of an extremely simple to state, extremely hard to solve, problem. A middle of the road viewpoint is that this problem is representative of a large class of problems, concerning the behavior under iteration of maps that are expanding on part of their domain and contracting on another part of their domain. This general class of problems is of definite importance, and is currently of great interest as an area of mathematical (and physical) research; for some perspective, see Hasselblatt and Katok [45]. Progress on general methods of solution for functions in this class would be extremely significant.

This overview describes where things currently stand on the 3 ​ x + 1 3x+1 problem and how it relates to various fields of mathematics. For a detailed introduction to the problem, see the following paper of Lagarias [58] (in this volume). In §2 we give some history of the problem; this presents some new information beyond that given in [58]. Then in §3 we give a flavor of the behavior of the 3 ​ x + 1 3x+1 iteration. In §4 we discuss various frameworks for generalizing the problem; typically these concern iterations of functions having a similar appearance to the 3 ​ x + 1 3x+1 function. In §5 we review areas of research: these comprise different fields of mathematics and computer science on which this problem impinges. In §6 we summarize the current best results on the problem in various directions. In §7 we discuss the hardness of the 3 ​ x + 1 3x+1 problem. In §8 we describe some research directions for future progress. In §9 we address the question: “Is the 3 ​ x + 1 3x+1 problem a good problem?” In the concluding section §10 we offer some advice on working on 3 ​ x + 1 3x+1 -related problems.

## 2. History and Background

The 3 ​ x + 1 3x+1 problem circulated by word of mouth for many years. It is generally attributed to Lothar Collatz. He has stated ( [14]) that he took lecture courses in 1929 with Edmund Landau and Fritz von Lettenmeyer in Göttingen, and courses in 1930 with Oskar Perron in Munich and with Issai Schur in Berlin, the latter course including some graph theory. He was interested in graphical representations of iteration of functions. In his notebooks in the 1930’s he formulated questions on iteration of arithmetic functions of a similar kind (cf. [58, p. 3]). Collatz is said by others to have circulated the problem orally at the International Congress of Mathematicians in Cambridge, Mass. in 1950. Several people whose names were subsequently associated with the problem gave invited talks at this International Congress, including H. S. M. Coxeter, S. Kakutani, and S. Ulam. Collatz [15] (in this volume) states that he described the 3 ​ x + 1 3x+1 problem to Helmut Hasse in 1952 when they were colleagues at the University of Hamburg. Hasse was interested in the problem, and wrote about it in lecture notes in 1975 ( [44]). Another claimant to having originated the 3 ​ x + 1 3x+1 problem is Bryan Thwaites [90], who asserts that he came up with the problem in 1952. Whatever is its true origin, the 3 ​ x + 1 3x+1 problem was already circulating at the University of Cambridge in the late 1950’s, according to John H. Conway and to Richard Guy [43].

There was no published mathematical literature about the 3 ​ x + 1 3x+1 problem until the early 1970’s. This may have been, in part, because the 1960’s was a period dominated by Bourbaki-style mathematics. The Bourbaki viewpoint emphasized complete presentations of theories with rich internal structure, which interconnect with other areas of core mathematics (see Mashaal [65]). In contrast, the 3 ​ x + 1 3x+1 problem initially appears to be an isolated problem unrelated to the rest of mathematics. Another obstacle was the difficulty in proving interesting results about the 3 ​ x + 1 3x+1 iteration. The results that could be proved appeared pathetically weak, so that it could seem damaging to one’s professional reputation to publish them. In some mathematical circles it might have seemed in bad taste even to show interest in such a problem, which appears déclassé.

During the 1960’s, various problems related to the 3 ​ x + 1 3x+1 problem appeared in print, typically as unsolved problems. This included one of the original problems of Collatz from the 1930’s, which concerned the behavior under iteration of the function

 | U ⁡ ( 2 ​ n) = 3 ​ n, U ⁡ ( 4 ​ n + 1) = 3 ​ n + 1, U ⁡ ( 4 ​ n + 3) = 3 ​ n + 2. U(2n)=3n,~U(4n+1)=3n+1,~U(4n+3)=3n+2. |  |

The function U ⁡ ( n) U(n) defines a permutation of the integers, and the question concerns whether the iterates of the value n = 8 n=8 form an infinite set. This problem was raised by Murray Klamkin [52] in 1963 (see Lagarias [58, p. 3]), and remains unsolved. Another such problem was posed by Ramond Queneau, a founder of the French mathematical-literary group Oulipo (Ouvroir de littérature potentielle), which concerns allowable rhyming patterns generalizing those used in poems by the 12-th century troubadour, Arnaut Daniel. This problem turns out to be related to a ( 3 ​ x + 1) (3x+1) -like function whose behavior under iteration is exactly analyzable, see Roubaud [80]. Concerning the 3 ​ x + 1 3x+1 problem itself, during the 1960’s large computations were done testing the truth of the conjecture. These reportedly verified the conjecture for all n ≤ 10 9 n\leq 10^{9}.

To my knowledge, the 3 ​ x + 1 3x+1 problem first appeared in print in 1971, in the written version of a 1970 lecture by H. S. M. Coxeter [22] (in this volume). It was presented there “as a piece of mathematical gossip.” In 1972 it appeared in six different publications, including a Scientific American column by Martin Gardner [32] that gave it wide publicity. Since then there has been a steady stream of work on it, now amounting to several hundred publications.

Stanislaw Ulam was one of many who circulated the problem; the name “Ulam’s problem” has been attached to it in some circles. He was a pioneer in ergodic theory and very interested in iteration of functions and their study by computer; he formulated many problem lists (e.g. [92], [21]). A collaborator, Paul Stein [87, p. 104], wrote about Ulam:

Stan was not a number theorist, but he knew many number-theoretical facts. As all who knew him well will remember, it was Stan’s particular pleasure to pose difficult, though simply stated, questions in many branches of mathematics. Number theory is a field particularly vulnerable to the “Ulam treatment,” and Stan proposed more than his share of hard questions; not being a professional in the field, he was under no obligation to answer them.

Ulam’s long term collaborator C. J. Everett [27] wrote one of the early papers about the 3 ​ x + 1 3x+1 problem in 1977.

The 3 ​ x + 1 3x+1 problem can also be formulated in the backwards direction, as that of determining the smallest set S 0 S_{0} of integers containing 1 1 which is closed under the affine maps x ↦ 2 ​ x x\mapsto 2x and 3 ​ x + 2 ↦ 2 ​ x + 1 3x+2\mapsto 2x+1, where the latter map may only be applied to inputs 3 ​ x + 2 3x+2 whose output 2 ​ x + 1 2x+1 will be an integer. The 3 ​ x + 1 3x+1 conjecture then asserts that S 0 S_{0} will be the set of all positive integers. This connects the 3 ​ x + 1 3x+1 problem with problems on sets of integers which are closed under the action of affine maps. Problems of this sort were raised by Isard and Zwicky [51] in 1970. In 1970-1971 David Klarner began studying sets of integers closed under iteration of affine maps, leading to joint work with Richard Rado [54], published in 1974. Interaction of Klarner and Paul Erdős at the University of Reading in 1971 led to the formulation of a (solved) Erdős prize problem: Does the smallest set S 1 S_{1} of integers containing 1 1 and closed under the affine maps x ↦ 2 ​ x + 1, x ↦ 3 ​ x + 1 x\mapsto 2x+1,x\mapsto 3x+1 and x ↦ 6 ​ x + 1 x\mapsto 6x+1 have a positive (lower asymptotic) density? This set S 1 S_{1} was proved to have zero density by D. J. Crampin and A. J. W. Hilton (unpublished), according to Klarner [53]. The solvers collected £ ​ 10 \pounds 10 from Erdős ( [50]). Later Klarner [53, p. 47] formulated a revised problem:

Klarner’s Integer Sequence Problem. Does the smallest set of integers S 2 S_{2} containing 1 1 and closed under the affine maps x ↦ 2 ​ x, x ↦ 3 ​ x + 2 x\mapsto 2x,x\mapsto 3x+2 and x ↦ 6 ​ x + 3 x\mapsto 6x+3 have a positive (lower asymptotic) density?

This problem remains unsolved; see the paper of Guy [40] (in this volume) and accompanying editorial commentary.

Much early work on the problem appeared in unusual places, some of it in technical reports, some in problem journals. The annotated bibliography given in this book [60] covers some of this literature, see also its sequel [61]. Although the problem began life as a curiosity, its general connection with various other areas of mathematics, including number theory, dynamical systems and theory of computation, have made it a respectable topic for mathematical research. A number of very well known mathematicians have contributed results on it, including John H. Conway [16] and Yakov G. Sinai [84], [85].

## 3. 3 ​ x + 1 3x+1 Sampler

The fascination of the 3 ​ x + 1 3x+1 problem involves its simple definition and the apparent complexity of its behavior under iteration: there seems to be no simple relation between the input value n n and the iterates of n n. Exploration of its structure has led to the formulation of a web of subsidiary conjectures about the behavior of iterates of the 3 ​ x + 1 3x+1 function and generalizations; these include conjectures (C1)–(C5) listed in §8. Many of these conjectures seem to be extremely difficult problems as well, and their exploration has led to much further research. Since other papers in this volume give much more information on this complexity, here we give only a brief sampler of 3 ​ x + 1 3x+1 function behavior.

### 3.1. Plots of Trajectories

By the trajectory of x x under a function T T, we mean the forward orbit of x x, that is, the sequence of its forward iterates
( x, T ⁡ ( x), T ( 2) ​ ( x), T ( 3) ​ ( x), …) (x,T(x),T^{(2)}(x),T^{(3)}(x),...). Figure 3.1 displays the 3 ​ x + 1 3x+1 -function iterates of n = 649 n=649 plotted on a standard scale. We see an irregular series of increases and decreases, leading to the name “hailstone numbers” proposed by Hayes [46], as hailstones form by repeated upward and downward movements in a thunderhead.

Figure 3.1. Trajectory of n = 649 n=649 plotted on standard vertical scale

To gain insight into a problem it helps to choose an appropriate scale for picturing it. Here it is useful to view long trajectories on a logarithmic scale, i.e., to plot log ⁡ T ( k) ​ ( n) \log T^{(k)}(n) versus k k. Figure 3.2 displays the iterates of n 0 = 100 ​ ⌊ π ​ 10 35 ⌋ n_{0}=100\lfloor\pi 10^{35}\rfloor on such a scale. Using this scale we see a decrease at a certain geometric rate to the value of 1 1, indicated by the trajectory having roughly a constant slope. This is characteristic of most long trajectories. As explained in §3.3 a probabilistic model predicts that most trajectories plotted on a logarithmic scale will stay close to a line of constant slope − 1 2 ​ log ⁡ 3 4 ∼ − 0.14384, -\frac{1}{2}\log\frac{3}{4}\sim-0.14384, thus taking about 6.95212 ​ log ⁡ n 6.95212\log n steps to reach 1 1. This line is pictured as the dotted line in Figure 3.2. This trajectory takes 529 529 steps to reach n = 1 n=1, while the probabilistic model predicts about 600 600 steps will be taken.

Figure 3.2. Trajectory of n 0 = 100 ​ ⌊ π ⋅ 10 35 ⌋ n_{0}=100\lfloor\pi\cdot 10^{35}\rfloor plotted on a logarithmic vertical scale y = log ⁡ T ( x) ​ ( n 0) y=\log T^{(x)}(n_{0}) (natural logarithm), x x an integer. The dotted line is a probability model prediction for a “random” trajectory for this size N N.

On the other hand, plots of trajectories suggest that iterations of the 3 ​ x + 1 3x+1 function also seem to exhibit pseudo-random features, i.e. the successive iterates of a random starting value seem to increase or decrease in an unpredictable manner. From this perspective there are some regularities of the iteration that appear (only) describable as statistical in nature: they are assertions about the majority of trajectories in ensembles of trajectories rather than about individual trajectories.

### 3.2. Patterns

Close examination of the iterates of the 3 ​ x + 1 3x+1 function T ⁡ ( x) T(x) for different starting values reveals a myriad of internal patterns. A simple pattern is that the initial iterates of n = 2 m − 1 n=2^{m}-1 are

 | T ( k) ​ ( 2 m − 1) = 3 k ⋅ 2 m − k − 1, for ​ 1 ≤ k ≤ m. T^{(k)}(2^{m}-1)=3^{k}\cdot 2^{m-k}-1,~~\mbox{for}~1\leq k\leq m. |  |

In particular, T ( m) ​ ( 2 m − 1) = 3 m − 1 T^{(m)}(2^{m}-1)=3^{m}-1; this example shows that the iteration can sometimes reach values arbitrarily larger than the initial value, either on an absolute or a relative scale, even if, as conjectured, the iterates eventually reach 1 1. Other patterns include the appearance of occasional large clusters of consecutive numbers which all take exactly the same number of iterations to reach the value 1 1. Some of these patterns are easy to analyze, others are more elusive.

Table 2.1 presents data on iterates of the 3 ​ x + 1 3x+1 function T ⁡ ( x) T(x) for n = n 0 + m n=n_{0}+m, 0 ≤ m = 10 ​ j + k ≤ 99 0\leq m=10j+k\leq 99, with

 | n 0 = 100 ​ ⌊ π ⋅ 10 35 ⌋ = 31,415,926,535,897, 932, 384, 626, 433, 832, 795, 028, 800. n_{0}=100\lfloor\pi\cdot 10^{35}\rfloor=31,415,926,535,897,932,384,626,433,832,795,028,800. |  |

Here σ ∞ ​ ( n) \sigma_{\infty}(n) denotes the total stopping time for n n, which counts the number of iterates of the 3 ​ x + 1 3x+1 -function T ⁡ ( x) T(x) needed to reach 1 1 starting from n n, counting n n as the 0 0 -th iterate. This number is the same as the number of even numbers appearing in the trajectory of the Collatz function before first reaching 1 1.

 | j = 0 j=0 | j = 1 j=1 | j = 2 j=2 | j = 3 j=3 | j = 4 j=4 | j = 5 j=5 | j = 6 j=6 | j = 7 j=7 | j = 8 j=8 | j = 9 j=9 |

k = 0 k=0 | 529 | 529 | 529 | 678 | 529 | 529 | 846 | 529 | 846 | 846 |

k = 1 k=1 | 659 | 659 | 529 | 678 | 659 | 529 | 846 | 529 | 529 | 529 |

k = 2 k=2 | 846 | 529 | 659 | 529 | 529 | 529 | 659 | 846 | 529 | 659 |

k = 3 k=3 | 846 | 529 | 659 | 846 | 659 | 529 | 659 | 846 | 529 | 659 |

k = 4 k=4 | 659 | 659 | 659 | 846 | 678 | 529 | 846 | 846 | 846 | 659 |

k = 5 k=5 | 659 | 659 | 846 | 846 | 678 | 529 | 529 | 529 | 846 | 659 |

k = 6 k=6 | 659 | 529 | 659 | 846 | 678 | 846 | 529 | 846 | 659 | 846 |

k = 7 k=7 | 529 | 529 | 659 | 846 | 659 | 659 | 529 | 846 | 659 | 529 |

k = 8 k=8 | 529 | 678 | 659 | 846 | 529 | 846 | 529 | 529 | 846 | 846 |

k = 9 k=9 | 529 | 678 | 659 | 659 | 529 | 529 | 529 | 529 | 659 | 846 |

Table 2.1. Values of total stopping time σ ∞ ​ ( n) \sigma_{\infty}(n) for n = n 0 + 10 ​ j + k, n=n_{0}+10j+k, with n 0:= 100 ​ ⌊ π ⋅ 10 35 ⌋ = 31,415,926,535,897, 932, 384, 626, 433, 832, 795, 028, 800. n_{0}:=100\lfloor\pi\cdot 10^{35}\rfloor=31,415,926,535,897,932,384,626,433,832,795,028,800.

We observe that the total stopping time function takes only a few different values, namely: 529, 659, 678 and 846, and these four values occur intermixed in a somewhat random-appearing way, but with some regularities. Note that around n 0 ∼ 3.14 × 10 37 n_{0}\sim 3.14\times 10^{37} the predicted “average size” of a trajectory is 6.95212 ​ log ⁡ n 0 ≈ 600 6.95212\log n_{0}\approx 600. In the data here we also observe “jumps” of size between the occurring values on the order of 100 100.

This is not a property of just this starting value. In Table 2.2 we give similar data for blocks of 100 100 near n = 10 35 n=10^{35} and 10 36 10^{36}, respectively. Again we observe that there are also four or five values occurring, but now they are different values. In this table we present data on two other statistics: the frequency statistic gives the count of these number of occurrences of each value, and the 1 1 -ratio statistic denotes the fraction of odd iterates occurring in the given trajectory up to and including when 1 1 is reached. It is an experimental fact that all sequences in the table having the same total stopping time also have the same 1 1 -ratio. In the first two blocks the value σ ∞ ​ ( n) = 481 \sigma_{\infty}(n)=481 (resp. 351 351) that occurs with frequency 1 1 is that for the intial value n = 10 35 n=10^{35} (resp. n = 10 36 n=10^{36}) in the given interval; these initial values are unusual in being divisible by a high power of 2 2. Probabilistic models for the 3 ​ x + 1 3x+1 -function iteration predict that even and odd iterates will initially occur with equal frequency, so we may anticipate the 1 1 -ratio values to be relatively close to 0.5 0.5.

 | (a) 10 35 10^{35} |  |  | (b) 10 36 10^{36} |  |  | (c) n 0 n_{0} |  |

σ ∞ ​ ( n) \sigma_{\infty}(n) | freq. | 1 1 -ratio | σ ∞ ​ ( n) \sigma_{\infty}(n) | freq. | 1 1 -ratio | σ ∞ ​ ( n) \sigma_{\infty}(n) | freq. | 1 1 -ratio |

481 | 1 | 0.47817 | 351 | 1 | 0.41594 | 529 | 38 | 0.48204 |

508 | 19 | 0.48622 | 467 | 72 | 0.46895 | 659 | 28 | 0.51138 |

573 | 49 | 0.50261 | 508 | 21 | 0.48228 | 678 | 7 | 0.51474 |

592 | 10 | 0.50675 | 519 | 6 | 0.48554 | 846 | 27 | 0.53782 |

836 | 21 | 0.54306 |  |  |  |  |  |  |

Table 2.2 Values of total stopping time, their frequencies, and 1 1 -ratio for

(a) 10 35 ≤ n ≤ 10 35 + 99 10^{35}\leq n\leq 10^{35}+99, (b) 10 36 ≤ n ≤ 10 36 + 99 10^{36}\leq n\leq 10^{36}+99, (c) n 0 ≤ n ≤ n 0 + 99 n_{0}\leq n\leq n_{0}+99.

The data in Table 2.2 suggests the following heuristic: as n n increases only a few values of σ ∞ ​ ( n) \sigma_{\infty}(n) locally occur over short intervals; there is then a slow variation in which values of σ ∞ ​ ( n) \sigma_{\infty}(n) occur. However these local values are separated from each other by relatively large “jumps” in size. We stress that this is a purely empirical observation, nothing like this is rigorously proved! Our heuristic did not quantify what is a “short interval” and it did not quantify what “relatively large jumps” should mean. Even the existence of finite values for σ ∞ ​ ( n) \sigma_{\infty}(n) in the tables presumes the 3 ​ x + 1 3x+1 conjecture is true for all numbers in the table.

### 3.3. Probabilistic Models

A challenging feature of the 3 ​ x + 1 3x+1 problem is the huge gap between what can be observed about its behavior in computer experiments and what can be rigorously proved. Attempts to understand and predict features of empirical experimentation have led to the following curious outcome: the use of probabilistic models to describe a deterministic process! This gives another theme of research on this problem: the construction and analysis of probabilistic and stochastic models for various aspects of the iteration process.

A basic probabilistic model of iterates of the 3 ​ x + 1 3x+1 function T ⁡ ( x) T(x) proposes that most trajectories for 3 ​ x + 1 3x+1 iterates have equal numbers of even and odd iterates, and that the parity of successive iterates behave in some sense like independent coin flips. A key observation of Terras [88] and Everett [27], leading to this model, is that the initial iterates of the 3 ​ x + 1 3x+1 function have this property (see Lagarias [58, Lemma B]).) This probabilistic model suggests that most trajectories plotted on a logarithmic vertical scale should appear close to a straight line having negative slope equal to − 1 2 ​ log ⁡ 3 4 ∼ − 0.14384, -\frac{1}{2}\log\frac{3}{4}\sim-0.14384, and should thus take about 6.95212 ​ log ⁡ n 6.95212\log n steps to reach 1 1.

The corresponding behavior of iterates of the Collatz function C ⁡ ( x) C(x) is more complicated. The allowed patterns of even and odd Collatz function iterates always have an even iterate following each odd iterate. Probabilistic models taking this into account are more complicated to formulate and analyze than that for the 3 ​ x + 1 3x+1 function; this is a main reason for studying the 3 ​ x + 1 3x+1 function rather than the Collatz function. Use of the probabilistic model above allows the heuristic inference that Collatz iterates will be even about two-thirds of the time.

A variety of fairly complicated stochastic models, many of which are rigorously analyzable (as probability models), have now been formulated to model various aspects of these iterations, see Kontorovich and Lagarias [56] (in this volume). Rigorous results for such models lead to heuristic predictions for the statistical behavior of iterates of the generalized 3 ​ x + 1 3x+1 map. The model above predicts the behavior of “most” trajectories. A small number of trajectories may exhibit quite different behavior. One may consider those trajectories that that seem to offer maximal value of some iterate of T ( k) ​ ( n) T^{(k)}(n) compared to n n. Here a probabilistic model (see [56, Sec. 4.3] in this volume) predicts that the statistic

 | ρ ⁡ ( n):= log ⁡ ( max k ≥ 1 ⁡ ( T ( k) ​ ( n)) CLOSE log ⁡ n \rho(n):=\frac{\log(\max_{k\geq 1}\left(T^{(k)}(n)\right)}{\log n} |  |

as n → ∞ n\to\infty should have ρ ⁡ ( n) ≤ 2 + o ⁡ ( 1) \rho(n)\leq 2+o(1) for all sufficiently large n n. Figure 3.3 offers a plot of the trajectory, for the value n 1 = 1980976057694878447, n_{1}=1980976057694878447, which attains the largest value of the statistic ρ ⁡ ( n) \rho(n) over 1 ≤ n ≤ 10 18 1\leq n\leq 10^{18}; this value was found by Oliveira e Silva [76, Table 6] (in this volume). This example has ρ ⁡ ( n 1) ≈ 2.04982 \rho(n_{1})\approx 2.04982. Probabilistic models suggest that the extremal trajectories of this form will approach a characteristic shape which consists of two line segments, one of length 7.645 ​ log ⁡ n 7.645\log n steps of slope about 0.1308 0.1308 up to the maximal value of about 2 ​ log ⁡ n 2\log n, the second of about 13.905 ​ log ⁡ n 13.905\log n steps of slope about − 0.1453 -0.1453 to 0, taking 21.55 ​ log ⁡ n 21.55\log n steps in all. This shape is indicated by the dotted lines on Figure 3.3 for comparison purposes.

Figure 3.3. Extremal trajectory n 1 = 1980976057694878447 n_{1}=1980976057694878447 given in Oliveira e Silva’s Table 6.

Another prediction of such stochastic models, relevant to the 3 ​ x + 1 3x+1 conejcture, is that the number of iterations required for a positive integer n n to iterate to 1 1 under the 3 ​ x + 1 3x+1 function T ⁡ ( x) T(x) is at most 41.677647 ​ log ⁡ n 41.677647\log n (see [62], [56, Sect. 4]). In particular such models predict, in a quantitative form, that there will be no divergent trajectories.

These stochastic models can be generalized to model the behavior of many generalized 3 ​ x + 1 3x+1 functions, and they make qualitatively different predictions depending on the function. For example, such models predict that no orbit of iteration of the 3 ​ x + 1 3x+1 function “escapes to infinity” (divergent trajectory). However for the 5 ​ x + 1 5x+1 function given by

 | T 5 ​ ( x) = { 5 ​ x + 1 2 if ​ x ≡ 1 ( mod 2), x 2 if ​ x ≡ 0 ( mod 2), T_{5}(x)=\left\{\begin{array}[]{cl}\displaystyle\frac{5x+1}{2}&\mbox{if}~x\equiv 1~~(\bmod~2),\\ \\ \displaystyle\frac{x}{2}&\mbox{if}~~x\equiv 0~~(\bmod~2),\end{array}\right. |  |

similar stochastic models predict that almost all orbits should “escape to infinity” ( [56, Sect. 8]). These predictions are supported by experimental computer evidence, but it remains an unsolved problem to prove that there exists even one trajectory for the 5 ​ x + 1 5x+1 problem that “escapes to infinity”.

There remains considerable research to be done on further developing stochastic models. The experiments on the 3 ​ x + 1 3x+1 iteration reported above in §3.2 exhibit some patterns not yet explained by stochastic models. In particular, the behaviors of total stopping times observed in Tables 2.1 and 2.2, and the heuristic presented there, have not yet been justified by suitable stochastic models.

## 4. Generalized 3 ​ x + 1 3x+1 functions

The original work on the 3 ​ x + 1 3x+1 problem viewed it as a problem in number theory. Much of the more recent work views it as an example of a special kind of discrete dynamical system, as exemplified by the lecture notes volume of G. J. Wirsching [95]. As far as generalizations are concerned, a very useful class of functions has proved to be the set of generalized Collatz functions which are defined below. These possess both number-theoretical and dynamic properties; the number-theoretic properties have to do with the existence of p p -adic extensions of these maps for various primes p p.

At present the 3 ​ x + 1 3x+1 problem is most often viewed as a discrete dynamical system of an arithmetical kind. It can then be treated as a special case, within the framework of a general class of such dynamical systems. But what should be the correct degree of generality in such a class?

There is significant interest in exploring the behavior of dynamical systems of an arithmetic nature, since these may be viewed as “toy models” of more complicated dynamical systems arising in mathematics and physics. There are a wide variety of interesting arithmetic dynamical systems. The book of Silverman [82] studies the iteration of algebraic maps on algebraic varieties. The book of Schmidt [81] considers dynamical systems of algebraic origin, meaning ℤ d {\mathbb{Z}}^{d} -actions on compact metric groups, using ergodic theory and symbolic methods. The book of Furstenberg [30] considers various well structured arithmetical dynamical systems; for a further development see Glasner [34]. The generalized 3 ​ x + 1 3x+1 functions studied in this book provide another distinct type of arithmetic discrete dynamical system.

We present a taxonomy of several classes of functions which represent successive generalizations of the 3 ​ x + 1 3x+1 function. The simplest generalization of the 3 ​ x + 1 3x+1 function is the 3 ​ x + k 3x+k function, which is defined for k ≡ 1 k\equiv 1 or 5 ( mod 6) 5~(\bmod 6), by

 | T 3, k ​ ( x) = { 3 ​ x + k 2 if ​ x ≡ 1 ( mod 2), x 2 if ​ x ≡ 0 ( mod 2). T_{3,k}(x)=\left\{\begin{array}[]{cl}\displaystyle\frac{3x+k}{2}&\mbox{if}~x\equiv 1~~(\bmod~2)~,\\ \\ \displaystyle\frac{x}{2}&\mbox{if}~~x\equiv 0~~(\bmod~2)~.\end{array}\right. |  |

The generalization of the 3 ​ x + 1 3x+1 conjecture to this situation is twofold: first, that under iteration every orbit becomes eventually periodic, and second, that there are only a finite number of cycles (periodic orbits). This class of functions occurs in the study of cycles of the 3 ​ x + 1 3x+1 function (Lagarias [59]). Note that the 3 ​ x + 1 3x+1 function T ⁡ ( x) T(x) can be extended to be well defined on the set of all rational numbers having odd denominator, and a rescaling of any T T -orbit of such a rational number r = n k r=\frac{n}{k} to clear its denominator k k will give an orbit of the map T 3, k T_{3,k}. Thus, integer cycles of the 3 ​ x + k 3x+k function correspond to rational cycles of the 3 ​ x + 1 3x+1 function having denominator k k.

To further generalize, let d ≥ 2 d\geq 2 be a fixed integer and consider the function defined for integer inputs x x by

(4.1) |  | f ⁡ ( x) = a i ​ x + b i d ​ if ​ x ≡ i ( mod d), 0 ≤ i ≤ d − 1, f(x)=\frac{a_{i}x+b_{i}}{d}~~~\mbox{if}~~x\equiv i~~(\bmod~d),~~0\leq i\leq d-1, |  |

where { ( a i, b i): 0 ≤ i ≤ d − 1 } \{(a_{i},b_{i}):0\leq i\leq d-1\} is a collection of integer pairs. Such a function is called admissible if the integer pairs ( a i, b i) (a_{i},b_{i}) satisfy the condition

(4.2) |  | i a i + b i ≡ 0 ( mod d) for 0 ≤ i ≤ d − 1. ia_{i}+b_{i}\equiv 0~~(\bmod~d)~~~\mbox{for}~~0\leq i\leq d-1. |  |

This condition is necessary and sufficient for the map f ⁡ ( x) f(x) to take integers to integers. These functions f ⁡ ( x) f(x) have been called generalized Collatz functions, or R ​ C ​ W ​ A RCWA functions (Residue-Class-Wise Affine functions). Generalized Collatz functions have the nice feature that they have a unique continuous extension to the space ℤ d {\mathbb{Z}}_{d} of d d -adic integers in the sense of Mahler [64].

An important subclass of generalized Collatz functions are those of relatively prime type. These are the subclass of generalized Collatz functions for which

(4.3) |  | gcd ( a 0 a 1 ⋯ a d − 1, d) = 1. \gcd(a_{0}a_{1}\cdots a_{d-1},d)=1. |  |

This class includes the 3 ​ x + 1 3x+1 function T ⁡ ( x) T(x) but not the Collatz function C ⁡ ( x) C(x) itself. It includes the 5 ​ x + 1 5x+1 function T 5 ​ ( x) T_{5}(x), which as mentioned above appears to have quite different long-term dynamics on the integers ℤ {\mathbb{Z}} than does the 3 ​ x + 1 3x+1 function. Functions in this class have the additional property that their unique extension to the d d -adic integers ℤ d {\mathbb{Z}}_{d} has the d d -adic Haar measure as an invariant measure. This permits ergodic theory methods to be applied to their study, see the survey paper of Matthews [67, Thm. 6.2] (in this volume) for many examples.

As a final generalization, one may consider the class of integer-valued functions, which when restricted to residue classes ( mod d) (\bmod\,d) are given by a polynomial P i ​ ( x) P_{i}(x) for each class i ( mod d). i~(\bmod\,d). Members of this class of functions have arisen in several places in mathematics. They are now widely called quasi-polynomial functions or quasi-polynomials. Quasi-polynomials appear in commutative algebra and algebraic geometry, in describing the Hilbert functions of certain semigroups, in a well known theorem of Serre, see Bruns and Herzog [9, pp. 174–175] and Bruns and Ichim [10]. In another direction, functions that count the number of lattice points inside dilated rational polyhedra have been shown to be quasi-polynomial functions (on the positive integers), starting with work of Ehrhart [23], see Beck and Robins [6] and Barvinok [5, Chap. 18]. They also have recently appeared in differential algebra in connection with q q -holonomic sequences, see Garoufalidis [33]. Such functions were introduced in group theory by G. Higman in 1960 [48] under the name PORC functions (polynomial on residue class functions). Higman’s motivating problem was the enumeration of p p -groups, cf. Evseev [28]. The class of all quasi-polynomial functions is closed under addition and pointwise multiplication, and forms a commutative ring under these operations.

We arrive at the following taxonomy of function classes of increasing generality:

 | { 3 ​ x + 1 ​ function ​ T ​ ( x) } \displaystyle\{3x+1~\mbox{function}~T(x)\} | ⊂ \displaystyle\subset | { 3 ​ x + k ​ functions ​ T 3, k ​ ( x) } \displaystyle\{3x+k~\mbox{functions}~T_{3,k}(x)\} |  |

 |  | ⊂ \displaystyle\subset | { generalized Collatz functions of relatively prime type } \displaystyle\{\mbox{generalized Collatz ~functions~of~relatively~prime~type}\} |  |

 |  | ⊂ \displaystyle\subset | { generalized Collatz functions } \displaystyle\{\mbox{generalized Collatz~functions}\} |  |

 |  | ⊂ \displaystyle\subset | { quasi-polynomial functions }. \displaystyle\{\mbox{quasi-polynomial ~functions}\}. |  |

For applications in mathematical logic, it has proved useful to further widen the definition of generalized Collatz functions to allow partially defined functions. Such functions are obtained by dropping the admissibility condition ( 4.2); they map integers to rational numbers having denominator dividing d d. If a non-integer value is encountered, then one cannot iterate such a function further. In this circumstance we adopt the convention that if a non-integer iteration value is encountered, the calculation stops in a special “undefined” state. This framework allows the encoding of partially-defined (recursive) functions. One can use this convention to also define composition of partially defined functions.

## 5. Research Areas

Work on the 3 ​ x + 1 3x+1 problem cuts across many fields of mathematics. Six basic areas of research on the problem are: (1) number theory: analysis of periodic orbits of the map; (2) dynamical systems: behavior of generalizations of the 3 ​ x + 1 3x+1 map; (3) ergodic theory: invariant measures for generalized maps; (4) theory of computation: undecidable iteration problems; (5) stochastic processes and probability theory: models yielding heuristic predictions for the behavior of iterates; and (6) computer science: algorithms for computing iterates and statistics, and explicit computations. We treat these in turn.

(1) Number Theory

The connection with number theory is immediate: the 3 ​ x + 1 3x+1 problem is a problem in arithmetic, whence it belongs to elementary number theory. Indeed it is classified as an unsolved problem in number theory by R. K. Guy [42, Problem E16]. The study of cycles of the 3 ​ x + 1 3x+1 map leads to problems involving exponential Diophantine equations. The powerful work of Baker and Masser–Wüstholz on linear forms in logarithms gives information on the non-existence of cycles of various lengths having specified patterns of even and odd iterates. A class of generalized 3 ​ x + 1 3x+1 functions has been defined in a number theory framework, in which arithmetic operations on the domain of integers are replaced with such operations on the ring of integers of an algebraic number field, or by function field analogues such as a polynomial ring with coefficients in a finite field. Number-theoretic results are surveyed in the papers of Lagarias [58] and Chamberland [11] in this volume.

(2) Dynamical Systems

The theory of discrete dynamical systems concern the behavior of functions under iteration; that of continuous dynamical systems concern flows or solutions to differential equations. The 3 ​ x + 1 3x+1 problem can be viewed as iterating a map, therefore it is a discrete dynamical system on the state space ℤ {\mathbb{Z}}. This viewpoint was taken in Wirsching [95]. The important operation for iteration is composition of functions. One can formulate iteration and composition questions in the general context of universal algebra, cf. Lausch and Nobauer [63, Chap. 4.5]. In the taxonomy above, the classes of generalized 3 ​ x + 1 3x+1 functions, and quasi-polynomial functions are each closed under addition and composition of functions. The iteration properties of the first three classes of functions above have been studied, in connection with the 3 ​ x + 1 3x+1 problem and the theory of computation. However the iteration of general quasi-polynomial functions remains an unexplored research area.

Viewing the problem this way suggests that it would be useful in the study of the 3 ​ x + 1 3x+1 function to obtain dynamical systems on larger domains, including the real numbers ℝ {\mathbb{R}} and the complex numbers ℂ {\mathbb{C}}. Other extensions include defining analogous functions on the ring ℤ 2 {\mathbb{Z}}_{2} of 2 2 -adic integers, or, for generalized 3 ​ x + 1 3x+1 maps, on a ring of d d -adic integers, for a value of d d determined by the function. When one considers generalized 3 ​ x + 1 3x+1 functions on larger domains, a wide variety of behaviors can occur. These topics are considered in the papers of Chamberland [11] and Matthews [67] in this volume. For a general framework on topological dynamics see Akin [1].

(3) Ergodic Theory

The connection with ergodic theory arises as an outgrowth of the dynamical systems viewpoint, but adds the requirement of the presence of an invariant measure. It was early observed that there are finitely additive measures which are preserved by the 3 ​ x + 1 3x+1 map on the integers. Extensions of generalized 3 ​ x + 1 3x+1 functions to d d -adic integers lead to maps invariant under standard measures (countably additive measures). For example, the (unique continuous) extension of the 3 ​ x + 1 3x+1 map to the 2 2 -adic integers has 2 2 -adic measure as an invariant measure, and the map is ergodic with respect to this measure. Ergodic theory topics are considered in the surveys of Matthews [67] and Kontorovich and Lagarias [56] in this volume. An interesting open problem is to classify all invariant measures for generalized 3 ​ x + 1 3x+1 functions on the d d -adic integers.

(4) Mathematical Logic and the Theory of Computation

The connection to logic and the theory of computation starts with the result of Conway that there is a generalized 3 ​ x + 1 3x+1 function whose iteration can simulate a universal computer. Conway [16] exhibited an unsolvable iteration problem for a particular generalized 3 ​ x + 1 3x+1 function: starting with a given input which is a positive integer n n, decide whether or not some iterate of this map with this input is ever a power of 2 2. In this connection note that the 3 ​ x + 1 3x+1 problem can be reformulated as asserting that, starting from any positive integer n n, some iterate C ( k) ​ ( n) C^{(k)}(n) of the Collatz function (or of the 3 ​ x + 1 3x+1 function) is a power of 2 2. It turns out that iteration of 3 ​ x + 1 3x+1 -like functions had already been considered in understanding the power of some logical theories even in the late 1960’s; these involved partially defined functions taking integers to integers (with undefined output for some integers), cf. Isard and Zwicky [51]. More recently such functions have arisen in studying the computational power of “small” Turing machines, that are too small to encode a universal computer. These topics are surveyed in the paper of Michel and Margenstern [68] in this volume.

(5) Probability Theory and Stochastic Processes

A connection to probability theory and stochastic processes arises when one attempts to model the behavior of the 3 ​ x + 1 3x+1 iteration on large sets of integers. This leads to heuristic probabilistic models for the iteration, which allow predictions of its behavior. Some authors have argued that the iteration can be viewed as a kind of pseudo-random number generator, viewing the input as being given by a probability distribution, and then asking how this probability distribution evolves under iteration. In the reverse direction, one can study trees of inverse iterates (the inverse map is many-to-one, giving rise to a unary-binary tree of inverse iterates). Here one can ask for facts about the structure of such trees whose root node is an integer picked from some probability distribution. One can model this by a stochastic model corresponding to random tree growth, e.g. a branching random walk. These topics are surveyed in the paper of Kontorovich and Lagarias [56] in this volume.

(6) Computer Science: Machine Models, Parallel and Distributed Computation

In 1987 Conway [17] (in this volume) formalized the Fractran model of computation as a universal computer model, based on his earlier work related to the 3 ​ x + 1 3x+1 problem. This computational model is related to the register machine (or counter machine) model of Marvin Minsky ( [70], [71, Sect. 11.1]). Both these machine models have recently been seen as relevant for developing models of computation using chemical reaction networks, and to biological computation, see Soloveichik et al [86] and Cook et al. [20].

The necessity to make computer experiments to test the 3 ​ x + 1 3x+1 conjecture, and to explore various properties and patterns of the 3 ​ x + 1 3x+1 iteration, leads to other questions in computation. One has the research problem of developing efficient algorithms for computing on a large scale, using either parallel computers or a distributed computer system. The 3 ​ x + 1 3x+1 conjecture has been tested to a very large value of n n, see the paper of Oliveira e Silva [76] in this volume. The computational method used in [76] to obtain record results can be parallelized. Various large scale computations for the 3 ​ x + 1 3x+1 problem have used distributed computing, cf. Roosendaal [79].

## 6. Current Status

We give a brief summary of the current status of the problem, which further elaborates answers to the two questions raised in the introduction.

### 6.1. Where does research currently stand on the 3 ​ x + 1 3x+1 problem?

The 3 ​ x + 1 3x+1 problem remains unsolved, and a solution remains unapproachable at present. To quote a still valid dictum of Paul Erdős ( [58, p. 3]) on the problem:

“Mathematics is not yet ready for such problems.”

Research has established various “world records”, all of which rely on large computer calculations (together with various theoretical developments).

1. (W1)

The 3 ​ x + 1 3x+1 conjecture has now been verified for all n < 20 × 2 58 ≈ 5.7646 × 10 18 n<20\times 2^{58}\approx 5.7646\times 10^{18} (Oliveira e Silva [76] (in this volume)).

2. (W2)

The trivial cycle { 1, 2 } \{1,2\} is the only cycle of the 3 ​ x + 1 3x+1 function on the positive integers having period length less than 10,439,860,591 10,439,860,591. It is also the only cycle containing less than 6,586,818,670 6,586,818,670 odd integers (Eliahou [24, Theorem 3.2] ***This number is the bound ( 21, 0) (21,0) given in [24, Table 2]. The smaller values in Table 2 are now ruled out by the computations in item (W1) above.).

3. (W3)

Infinitely many positive integers n n take at least 6.143 ​ log ⁡ n 6.143\log n steps to reach 1 1 under iteration of the 3 ​ x + 1 3x+1 function T ⁡ ( x) T(x) (Applegate and Lagarias [3]).

4. (W4)

The positive integer n n with the largest currently known value of C C, such that it takes C ​ log ⁡ n C\log n iterations of the 3 ​ x + 1 3x+1 function T ⁡ ( x) T(x) to reach 1 1, is n = 7,219,136,416,377, 236, 271, 195 n=7,219,136,416,377,236,271,195 with C ≈ 36.7169 C\approx 36.7169 (Roosendaal [79, 3 ​ x + 1 3x+1 Completeness and Gamma records]).

5. (W5)

The number of integers 1 ≤ n ≤ X 1\leq n\leq X that iterate to 1 1 is at least X 0.84 X^{0.84}, for all sufficiently large X X (Krasikov and Lagarias [57]).

There has also been considerable progress made on showing the nonexistence of various kinds of periodic points for the 3 ​ x + 1 3x+1 function, see Brox [8] and Simons and de Weger [83]. These bounds are based on number-theoretic methods involving Diophantine approximation.

### 6.2. Where does research stand on generalizations of the 3 ​ x + 1 3x+1 problem?

It has proved fruitful to view the 3 ​ x + 1 3x+1 problem as a special case of wider classes of functions. These function classes appear naturally as the correct level of generality for basic results on iteration; this resulted in the taxonomy of function classes given in §3. There are some general results for these classes and many unsolved problems.

The 3 ​ x + k 3x+k problem seems to be the correct level of generality for studying rational cycles of the 3 ​ x + 1 3x+1 function ( [59]). There are extensive results on cycles of the 3 ​ x + 1 3x+1 function, and the methods generally apply to the 3 ​ x + k 3x+k function as well, see the survey of Chamberland [11] (in this volume).

The class of generalized 3 ​ x + 1 3x+1 functions of relatively prime type is a very natural class from the ergodic theory viewpoint, since this is the class on which the d d -adic extension of the function has d d -adic Haar measure as an invariant measure. The paper of Matthews [67] (in this volume) reports general ergodicity results and raises many questions about such functions.

The class of generalized Collatz functions has the property that all functions in it have a unique continuous extension to the domain of d d -adic integers ℤ d {\mathbb{Z}}_{d}. This general class is known to contain undecidable iteration problems, as discussed in the paper of Michel and Margenstern [68] (in this volume). The dynamics of general functions in this class is only starting to be explored; many interesting examples are given in the paper of Matthews [67] (in this volume). An interesting area worthy of future development is that of determining the existence and structure of invariant Borel measures for such functions on ℤ d {\mathbb{Z}}_{d}, and determining whether there is some relation of their structure to undecidability of the associated iteration problem.

### 6.3. How can this be a hard problem, when it is so easy to state?

Our answer is that there are two different mechanisms yielding hard problems, either or both of which may apply to the 3 ​ x + 1 3x+1 problem. The first is “pseudorandomness”; this involves a connection with ergodic theory. The second is “non-computability”. Both of these are discussed in detail in this volume.

The “ergodicity” connection has been independently noted by a number of people, see for example Lagarias [58] (in this volume) and Akin [2]. The unique continuous extension of the 3 ​ x + 1 3x+1 map T ⁡ ( x) T(x) to the 2 2 -adic integers ℤ 2 {\mathbb{Z}}_{2} gives a function which is known to be ergodic in a strong sense, with respect to the 2 2 -adic measure. It is topologically and metrically conjugate to the shift map, which is a maximum entropy map. The iterates of the shift function are completely unpredictable in the ergodic theory sense. Given a random starting point, predicting the parity of the n n -th iterate for any n n is a “coin flip” random variable. The 3 ​ x + 1 3x+1 problem concerns the behavior of iterating this function on the set of integers ℤ {\mathbb{Z}}, which is a dense subset of ℤ 2 {\mathbb{Z}}_{2}, having 2 2 -adic measure zero. The difficulty is then in finding and understanding non-random regularities in the iterates when restricted to ℤ {\mathbb{Z}}. Various probabilistic models are discussed in the paper of Kontorovich and Lagarias [56] (in this volume). Empirical evidence seems to indicate that the 3 ​ x + 1 3x+1 function on the domain ℤ {\mathbb{Z}} retains the “pseudorandomness” property on its initial iterates until the iterates enter a periodic orbit. This supports the 3 ​ x + 1 3x+1 conjecture and at the same time deprives us of any obvious mechanism to prove it, since mathematical arguments exploit the existence of structure, rather than its absence.

A connection of a generalized Collatz function to “non-computability” was made by Conway [16] (in this volume), as already mentioned. Conway’s undecidability result indicates that the 3 ​ x + 1 3x+1 problem could be close to the unsolvability threshold. It is currently unknown whether the 3 ​ x + 1 3x+1 problem is itself undecidable, however no method is currently known to approach this question. The survey of Michel and Margenstern [68] (in this volume) describes many results on generalized 3 ​ x + 1 3x+1 functions that exhibit undecidable or difficult-to-decide iteration problems. The 3 ​ x + 1 3x+1 function might conceivably belong to a smaller class of generalized 3 ​ x + 1 3x+1 functions that evade undecidability results that encode universal computers. Even so, it conceivably might encode an undecidable problem, arising by another (unknown) mechanism. As an example, could the following question be undecidable: “Is there any positive integer n n such that T ( k) ​ ( n) > 1 T^{(k)}(n)>1 for 1 ≤ k ≤ 100 ​ log ⁡ n 1\leq k\leq 100\log n?”

## 7. Hardness of the 3 ​ x + 1 3x+1 problem

Our viewpoint on hard problems has evolved since 1900, starting with Hilbert’s program in logic and proof theory and benefiting from developments in the theory of computation. Starting in the 1920’s, Emil Post uncovered great complexity in studying some very simple computational problems, now called “Post Tag Systems”. A Tag system in the class T ​ S ​ ( μ, ν) TS(\mu,\nu) consists of a set of rules for transforming words using letters from an alphabet 𝒜 = { a 1, …, a μ } {\mathcal{A}}=\{a_{1},...,a_{\mu}\} of μ \mu symbols, a deletion number (or shift number) ν ≥ 1 \nu\geq 1, and a set of μ \mu production rules

 | a j ↦ w j:= a j, 0 a j, 1 ⋯ a j, n j, 1 ≤ j ≤ μ, a_{j}\mapsto w_{j}:=a_{j,0}a_{j,1}\cdots a_{j,n_{j}},~~~1\leq j\leq\mu, |  |

in which the output w j w_{j} is a finite string (or word) of length n j n_{j} in the alphabet 𝒜 {\mathcal{A}}. Starting from an initial string S S a Tag system looks at the leftmost symbol of S S, call it a j a_{j}, then attaches to the right end of the string the word w j w_{j}, and finally deletes the first ν \nu symbols of the resulting string S ​ w j Sw_{j}, thus obtaining a new string S ′ S^{\prime}. Here the “tag” is the set of symbols w j w_{j} attached to the end of the word, and the iteration halts if a word of length less than ν \nu is encountered. The halting problem is the question of deciding whether for an arbitrary initial word S S, iteration eventually reaches the empty word. The reachability problem is that of deciding whether, given words S S and S ~ \tilde{S}, starting from word S S will ever produce word S ~ \tilde{S} under iteration. The halting problem is a special case of the reachability problem. Post [78] reports that in 1920--1921 he found a complete decision procedure † † † Post did not publish his proof. A decision procedure for both problems is outlined in de Mol [73]. for the case μ = 2, ν = 2 \mu=2,\nu=2, i.e. the class T ⁡ ( 2, 2) T(2,2). He then tried to solve the case μ = 2, ν > 2 \mu=2,\nu>2, without success. He reported [78, p. 372] that the special case μ = 2, ν = 3 \mu=2,\nu=3 with 𝒜 = { 0, 1 } {\mathcal{A}}=\{0,1\} and the two production rules

(7.4) |  | 0 ↦ w 0 = 00, 1 ↦ w 1 = 1101 0\mapsto w_{0}=00,~~~1\mapsto w_{1}=1101 |  |

already seemed to be an intractable problem. We shall term this problem

Post’s Original Tag Problem. Is there a recursive decision procedure for the halting problem for the Tag system in T ⁡ ( 2, 3) T(2,3) given by the rules 0 ↦ 00 0\mapsto 00 and 1 ↦ 1101 1\mapsto 1101?

Leaving this question aside, Post considered the parameter range μ > 2, ν = 2 \mu>2,\nu=2. He wrote [78, p. 373]:

For a while the case ν = 2, μ > 2 \nu=2,\,\mu>2 seemed to be more promising, since it seemed to offer a greater chance of a finitely graded series of problems. But when this possibility was explored in the early summer of 1921, it rather led to an overwhelming confusion of classes of cases, with the solution of the corresponding problem depending more and more on problems of ordinary number theory. Since it had been our hope that the known difficulties of number theory would, as it were, be dissolved in the particularities of this more primitive form of mathematics, the solution of the general problem of “tag” appeared hopeless, and with it our entire program of the solution of finiteness problems.

Discouraged by this, Post reversed course and went on to obtain a “Normal Form Theorem” ( [77]), published in the 1940’s, showing that a general logical problem could be reduced to a form slightly more complicated than Tag Systems. In 1961 Marvin Minsky [70] proved that Post Tag Systems were undecidable problems in general. In the next few years Hao Wang [94], J. Cocke and M. Minsky [13] and S. Ju. Maslov [66] independently showed undecidability for the subclass of Post Tag Systems consisting of those with ν = 2 \nu=2, thus showing that Post was right to quit trying to solve problems in that class. At present the recursive solvability or unsolvability in the class T ⁡ ( 2, ν) T(2,\nu) remains open for all ν > 2 \nu>2. Post’s original tag problem, which is the halting problem for one special function in T ⁡ ( 2, 3) T(2,3), is still unsolved, see Lisbeth De Mol [72], [74, p. 93], and for further work [73], [75].

Recently de Mol showed that the 3 ​ x + 1 3x+1 problem can be encoded as a reachability problem for a tag system in T ⁡ ( 3, 2) T(3,2) ( [74, Theorem 2.1]). This tag system encodes the 3 ​ x + 1 3x+1 function, and the reachability problem is:

3 ​ x + 1 3x+1 Tag Problem. Consider the tag system T C T_{C} in T ⁡ ( 3, 2) T(3,2) with alphabet 𝒜 = { 0, 1, 2 } {\mathcal{A}}=\{0,1,2\}, deletion number ν = 2 \nu=2, and production rules

 | 0 ↦ 12, 1 ↦ 0, 2 ↦ 000. 0\mapsto 12,\,1\mapsto 0,\,2\mapsto 000. |  |

For each n ≥ 1 n\geq 1, if one starts from the configuration S = 0 n S=0^{n}, will the tag system iteration for T C T_{C} always reach state S ~ = 0 \tilde{S}=0?

In 1931 Kurt Gödel [35] showed the existence of undecidable problems: he showed that certain propositions were undecidable in any logical system complicated enough to include elementary number theory. This result showed that Hilbert’s proof theory program could not be carried out. Developments in the theory of computation showed that one of Gödel’s incompleteness results corresponded to the unsolvability of the halting problem for Turing machines. This was based on the existence of a universal Turing machine, that could simulate any computation, and in his 1937 foundational paper Alan Turing [91] already showed one could be constructed of a not very large size.

We now have a deeper appreciation of exactly how simple a problem can be and still simulate a universal computer. Amazingly simple problems of this sort have been found in recent years. Some of these involve cellular automata, a model of computation developed by John von Neumann and Stansilaw M. Ulam in the 1950’s. One of these problems concerns the possible behavior of a very simple one-dimensional nearest neighbor cellular automaton, Rule 110, using a nomenclature introduced by Wolfram [96], [97]. This rule was conjectured by Wolfram to give a universal computer ( [98, Table 15], [99, pp. 575–577]). It was proved to be weakly universal by M. Cook (see Cook [18], [19]). Here weakly universal means that the initial configuration of the cellular automaton is required to be ultimately periodic, rather than finite. Another is John H. Conway’s game of “Life,” first announced in 1970 in Martin Gardner’s column in Scientific American (Gardner [31]), which is a two-dimensional cellular automaton, having nearest neighbor interaction rules of a particularly simple nature. Its universality as a computer was later established, see Berkelamp, Conway and Guy [7, Chap. 25]. Further remarks on the size of universal computers are given in the survey of Michel and Margenstern [68] (in this volume).

There are, however, reasons to suspect that the 3 ​ x + 1 3x+1 function is not complicated enough to be universal, i.e. to allow the encoding of a universal computer in its input space. First of all, it is so simple to state that there seems very little room in it to encode the elementary operations needed to create a universal computer. Second, the 3 ​ x + 1 3x+1 conjecture asserts that the iteration halts on the domain of all positive integer inputs, so for each integer n n, the value F ⁡ ( n) F(n) of the largest integer observed before visiting 1 1 is recursive. To encode a universal computer, one needs to represent all recursive functions, including functions that grow far faster than any given recursive function F ⁡ ( n) F(n). It is hard to imagine how one can encode it here as a question about the iteration, without enlarging the domain of inputs. Third, the 3 ​ x + 1 3x+1 function possesses the feature that there is a nice (finitely additive) invariant measure on the integers, with respect to which it is completely mixing under iteration. This is the measure that assigns mass 1 2 n \frac{1}{2^{n}} to each complete arithmetic progression ( mod 2 n) (\bmod~2^{n}), for each n ≥ 1 n\geq 1. This fundamental observation was made in 1976 by Terras [88], and independently by Everett [27] in 1977, see Lagarias [58, Theorem B] for a precise statement. This “mixing property” seems to fight against the amount of organization needed to encode a universal computer in the inputs. We should caution that this observation by itself does not rule out the possibility that, despite this mixing property, a universal computer could be encoded in a very thin set of input values (of “measure zero”), compatible with an invariant measure. It just makes it seem difficult to do. Indeed, the 1972 encoding of a universal computer in the iteration of a certain generalized 3 ​ x + 1 3x+1 function found by Conway [16] (in this volume) has the undecidability encoded in the iteration of a very thin set of integers. However Conway’s framework is different from the 3 ​ x + 1 3x+1 problem in that the halting function he considers is partially defined.

Even if iteration of the 3 ​ x + 1 3x+1 function is not universal, it could still potentially be unsolvable. Abstractly, there may exist in an axiomatic system statements F ⁡ ( n) F(n) for a positive integer predicate, such that F ⁡ ( 1), F ⁡ ( 2), F ⁡ ( 3), … F(1),F(2),F(3),... are provable in the system for all integer n n, but the statement ( ∀ n) ​ F ​ ( n) (\forall n)\,F(n) is not provable within the system. For example, one can let F ⁡ ( n) F(n) encode a statement that there is no contradiction in a system obtainable by a proof of length at most n n. If the system is consistent, then F ⁡ ( 1), F ⁡ ( 2), … F(1),F(2),... will all individually be provable. The statement ( ∀ n) ​ F ​ ( n) (\forall n)\,F(n) then encodes the consistency of the system. But the consistency of a system sufficiently complicated to include elementary number theory cannot be proved within the system, according to Gödel’s second incompleteness theorem.

The pseudo-randomness or “mixing” behavior of the 3 ​ x + 1 3x+1 function also seems to make it extremely resistant to analysis. If one could rigorously show a sufficient amount of mixing is guaranteed to occur, in a controlled number of iterations in terms of the input size n n, then one could settle part of the 3 ​ x + 1 3x+1 conjecture, namely prove the non-existence of divergent trajectories. Here we have the fundamental difficulty of proving in effect that the iterations actually do have an explicit pseudo-random property. Besides this difficulty, there remains a second fundamental difficulty: solving the number-theoretic problem of ruling out the existence of an enormously long non-trivial cycle of the 3 ​ x + 1 3x+1 function. This problem also seems unapproachable at present by known methods of number theory. However the finite cycles problem does admit proof of partial results, showing the nonexistence of non-trivial cycles having particular patterns of even and odd iterates.

A currently active and important general area of research concerns the construction of pseudo-random number generators: these are deterministic recipes that produce apparently random outputs (see Knuth [55, Chap. 3]). More precisely, one is interested in methods that take as input n n truly random bits and deterministically produce as output n + 1 n+1 “random-looking” bits. These bits are to be “random-looking” in the sense that they appear random with respect to a given family of statistical tests, and the output is then said to be pseudo-random with respect to this family of tests. Deciding whether pseudo-random number generators exist for statistical tests in various complexity classes is now seen as a fundamental question in computer science, related to the P = N ​ P P=NP probem, see for example Goldreich [37], [38]. It may be that resolving the issue of the pseudo-random character of iterating the 3 ​ x + 1 3x+1 problem will require shedding light on the general existence problem for pseudo-random number generators.

All we can say at present is that the 3 ​ x + 1 3x+1 problem appears very hard indeed. It now seems less surprising than it might have once seemed that a problem as simple-looking as this one could be genuinely difficult, and inaccessible to known methods of attack.

## 8. Future Prospects

We observe first that further improvements are surely possible on the “world records” (W1)–(W5) above. In particular, concerning (W3), it seems scandalous that it is not known whether or not there are infinitely many positive integers n n which iterate to 1 1 under the 3 ​ x + 1 3x+1 map T ⁡ ( x) T(x) and take at least the “average” number 2 log ⁡ 4 / 3 ​ log ⁡ n ≈ 6.95212 ​ log ⁡ n \frac{2}{\log 4/3}\log n\approx 6.95212\log n steps to do so. Here the stochastic models for the 3 ​ x + 1 3x+1 iteration predict that at least half of all positive integers should have this property! These “world records” are particularly worth improving if they can shed more light on the problem. This could be the case for world record (W5), where there is an underlying structure for obtaining lower bounds on the exponent, which involves an infinite family of nonlinear programs of increasing complexity ( [57]).

Analysis of the 3 ​ x + 1 3x+1 problem has resulted in the formulation of a large set of “easier” problems. At first glance some of these seem approachable, but they also remain unsolved, and are apparently difficult. As samples, these include:

1. (C1)

( Finite Cycles Conjecture) Does the 3 ​ x + 1 3x+1 function have finitely many cycles (i.e. finitely many purely periodic orbits on the integers)? This is conjectured to be the case.

2. (C2)

( Divergent Trajectories Conjecture-1) Does the 3 ​ x + 1 3x+1 function have a divergent trajectory, i.e., an integer starting value whose iterates are unbounded? This is conjectured not to be the case.

3. (C3)

( Divergent Trajectories Conjecture-2) Does the 5 ​ x + 1 5x+1 function have a divergent trajectory? This is conjectured to be the case.

4. (C4)

( Infinite Permutations-Periodic Orbits Conjecture) If a generalized Collatz function permutes the integers and is not globally of finite order, is it true that it has only finitely many periodic orbits? The original Collatz function U ⁡ ( n) U(n), which is a permutation, was long ago conjectured to have finitely many cycles. A conjecture of this kind, imposing extra conditions on the permutation, was formulated by Venturini [93, p. 303 top].

5. (C5)

( Infinite Permutations-Zero Density Conjecture) If a generalized Collatz function permutes the integers, is it true that every orbit has a (natural) density? Under some extra hypotheses one may conjecture that all such orbits have density zero; compare Venturini [93, Sec. 6].

Besides these conjectures, there also exist open problems which may be more accessible. One of the most intriguing of them concerns establishing lower bounds for the number π 1 ​ ( x) \pi_{1}(x) of integers less than x x that get to 1 1 under the 3 ​ x + 1 3x+1 iteration. As mentioned earlier it is known ( [57]) that there is a positive constant c 0 c_{0} such that

 | π 1 ​ ( x) > c 0 ​ x 0.84. \pi_{1}(x)>c_{0}x^{0.84}. |  |

It remains an open problem to show that for each ϵ > 0 \epsilon>0 there exists a positive constant c ⁡ ( ϵ) c(\epsilon) such that

 | π 1 ​ ( x) > c ⁡ ( ϵ) ​ x 1 − ϵ. \pi_{1}(x)>c(\epsilon)x^{1-\epsilon}. |  |

Many other specific, but difficult, conjectures for study can be found in the papers in this volume, starting with the problems listed in Guy [40].

We now raise some further research directions, related to the papers in this volume. A first research direction is to extend the class of functions for which the Markov models of Matthews [67] can be analyzed. Matthews shows that the class of generalized 3 ​ x + 1 3x+1 functions of relatively prime type ( [67, Sec. 2]) is analyzable. He formulates some conjectures for exploration. It would be interesting to characterize the possible d d -adic invariant measures for arbitrary generalized Collatz functions. It may be necessary to restrict to subclasses of such functions in order to obtain nice characterizations.

A second research direction concerns the class of generalized 3 ​ x + 1 3x+1 functions whose iterations extended to the set of d d -adic integers are ergodic with respect to the d d -adic measure, cf. Matthews [67, Sec. 6]).

Research Problem. Does the class of generalized Collatz functions of relatively prime type contain a function which is ergodic with respect to the standard d d -adic measure, whose iterations can simulate a universal computer? Specificially, could it have an unsolvable iteration problem of the form: “Given positive integers ( n, m) (n,m) as input, does there exist k k such that the k k -th iterate T ( k) ​ ( n) T^{(k)}(n) equals m m?” Or does ergodicity of the iteration preclude the possibility of simulating universal computation?

A third research direction concerns the fact that generalized Collatz functions have now been found in many other mathematical structures, especially if one generalizes further to integer-valued functions that are piecewise polynomial on residue classes ( mod d) (\bmod~d). These functions are the quasi-polynomial functions noted above, and they show up in a number of algebraic contexts, particularly in counting lattice points in various regions. It may prove worthwhile to study the iteration of various special classes of quasi-polynomial functions arising in these algebraic contexts.

At this point in time, in view of the intractability of problems (C1)–(C5) it also seems a sensible task to formulate a new collection of even simpler “toy problems”, which may potentially be approachable. These may involve either changing the problem or importing it into new contexts. For example, there appear to be accessible open problems concerning variants of the problem acting on finite rings (Hicks et al. [47]). Another promising recent direction is the connection of these problems with generating sets for multiplicative arithmetical semigroups, noted by Farkas [29]. This has led to a family of more accessible problems, where various results can be rigorously established ( [4]). Here significant unsolved problems remain concerning the structure of such arithmetical semigroups. Finally it may prove profitable to continue the study, initiated by Klarner and Rado [54], of sets of integers (or integer vectors) closed under the action of a finitely generated semigroup of affine maps.

## 9. Is the 3 ​ x + 1 3x+1 problem a “good” problem?

There has been much discussion of what constitutes a good mathematical problem. We cannot do better than to recall the discussion of Hilbert [49] in his famous 1900 problem list. On the importance of problems he said ( [49, p. 437]):

The deep significance of certain problems for the advance of mathematical science in general, and the important role they play in the work of the individual investigator, are not to be denied. As long as a branch of science offers an abundance of problems, so long is it alive; a lack of problems foreshadows extinction or the cessation of independent development. Just as every human undertaking pursues certain objects, so also mathematical research requires its problems. It is also by the solution of problems that the investigator tests the temper of his steel; he finds new methods and new outlooks, and gains a wider and freer horizon.

Hilbert puts forward three criteria that a good mathematical problem ought to satisfy:

It is difficult and often impossible to judge the value of a problem correctly in advance; for the final award depends upon the gain which science obtains from the problem. Nevertheless we can ask whether there are general criteria which mark a good mathematical problem. An old French mathematician said: “A mathematical theory is not to be considered complete until you have made it so clear that you can explain it to the first man that you meet on the street.” This clearness and ease of comprehension, here insisted on for a mathematical theory, I should still more demand for a mathematical problem if it is to be perfect; for what is clear and easily comprehended attracts, the complicated repels us.

Moreover a mathematical problem should be difficult in order to entice us, but not completely inaccessible, lest it mock at our efforts. It should be to us a guide post on the mazy paths to hidden truths, and ultimately a reminder of our pleasure in its successful solution.

From the viewpoint of the Hilbert criteria for a good problem, we see that:

(1) The 3 ​ x + 1 3x+1 problem is a clear, simply stated problem;

(2) The 3 ​ x + 1 3x+1 problem is a difficult problem;

(3) The 3 ​ x + 1 3x+1 problem initially seems accessible, in that it possesses a fairly intricate internal structure.

But – and it is a big “but” – the evidence so far suggests that obtaining a proof of the 3 ​ x + 1 3x+1 problem is inaccessible! Not only does this goal appear inaccessible, but various simplified conjectures derived from it appear to be completely inaccessible in their turn, leading to a regress to formulation of a series of simpler and simpler inaccessible problems, namely conjectures (C1)–(C5) listed in §8.

We conclude that the 3 ​ x + 1 3x+1 problem comes close to being a “perfect” problem in the Hilbert sense. However it seems to fail the last of Hilbert’s requirements: It mocks our efforts! It is possible to work hard on this problem to no result. It is definitely a dangerous problem! It could well be that the 3 ​ x + 1 3x+1 problem remains out of human reach. But maybe not. Who knows?

## 10. Working on the 3 ​ x + 1 3x+1 problem

Whether or not the 3 ​ x + 1 3x+1 problem is a “good” problem, it is not going away, due to its extreme accessibility. It offers a large and tantalizing variety of patterns in computer experiments. This problem stands as a mathematical challenge for the 21-st century.

In working on this problem, the most cautious advice, following Richard Guy [40] is:

Don’t try to solve these problems!

But, as Guy said [40, p. 35], some of you may be already scribbling, in spite of the warning!

We also note that Paul Erdős said, in conversation, about its difficulty ( [25]):

“Hopeless. Absolutely hopeless.”

In Erdős-speak, this means that there are no known methods of approach which gave any promise of solving the problem. For other examples of Erdős’s use of the term “hopeless” see Erdös and Graham [26, pp. 1, 27, 66, 105].

At this point we may recall further advice of David Hilbert [49, p. 442] about problem solving:

If we do not succeed in solving a mathematical problem, the reason frequently consists in our failure to recognize the more general standpoint from which the problem before us appears only as a single link in a chain of related problems. After finding this standpoint, not only is this problem frequently more accessible to our investigation, but at the same time we come into possession of a method that is applicable to related problems.

The quest for generalization cuts in two directions, for Hilbert also says [49, p. 442]:

He who seeks for methods without having a definite problem in mind seeks for the most part in vain.

Taking this advice into account, researchers have treated many generalizations of the 3 ​ x + 1 3x+1 problem, which are reported on in this volume. One can consider searching for general methods that apply to a large variety of related iterations. Such general methods as are known give useful information, and answer some questions about iterates of the 3 ​ x + 1 3x+1 function. Nevertheless it is fair to say that they do not begin to answer the central question:

What is the ultimate fate under iteration of such maps over all time?

My personal viewpoint is that the 3 ​ x + 1 3x+1 problem is somewhat dangerous, and that it is prudent not to focus on resolving the 3 ​ x + 1 3x+1 conjecture as an immediate goal. Rather, one might first look for more structure in the problem. Also one might profitably view the problem as a “test case”, to which one may from time to time apply new results arising from the ongoing development of mathematics. When new theories and new methods are discovered, the 3 ​ x + 1 3x+1 problem may be used as a testbed to assess their power, whenever circumstances permit.

To conclude, let us remind ourselves, following Hilbert [49, p. 438]:

The mathematicians of past centuries were accustomed to devote themselves to the solution of difficult particular problems with passionate zeal. They knew the value of difficult problems.

The 3 ​ x + 1 3x+1 problem stands before us as a beautifully simple question. It is hard to resist exploring its structure. We should not exclude it from the mathematical universe just because we are unhappy with its difficulty. It is a fascinating and addictive problem.

#### Acknowledgments.

I am grateful to Michael Zieve and Steven J. Miller each for detailed readings and corrections. Marc Chamberland, Alex Kontorovich, and Keith R. Matthews also made many helpful comments. The figures are due to Alex Kontorovich, adapted from work on [56]. I thank Andreas Blass for useful comments on incompleteness results and algebraic structures. The author was supported by NSF Grants DMS-0500555 and DMS-0801029.

## References

- [1] E. Akin, The general topology of dynamical systems, Graduate Studies in Mathematics 1., American Mathetmatical Society,Providence, RI 1993.
- [2] E. Akin, Why is the 3 ​ x + 1 3x+1 Problem Hard?, In: Chapel Hill Ergodic Theory Workshops (I. Assani, Ed.), Contemp. Math. vol 356, Amer. Math. Soc. 2004, pp. 1–20.
- [3] D. Applegate and J. C. Lagarias, Lower bounds for the total stopping time of 3 ​ x + 1 3x+1 iterates, Math. Comp. 72 (2003), 1035–1049.
- [4] D. Applegate and J. C. Lagarias (2006), The 3 ​ x + 1 3x+1 semigroup, J. Number Theory 177 (2006), 146–159.
- [5] A. Barvinok, Integer Points in Polyhedra, European Math.Soc. Publishing, ETH, Zürich 2008.
- [6] M. Beck and S. Robins, Computing the continuous discretely. Integer-point enumeration in polyhedra¡ Springer: New York 2007.
- [7] E. R. Berlekamp, J. H. Conway and R. K. Guy, Winning Ways for Your Mathematical Plays, Volume 4 (Second Revised Edition) A. K. Peters, Ltd. 2004.
- [8] T. Brox, Collatz cycles with few descents, Acta Arithmetica 92 (2000), 181–188.
- [9] W. Bruns and J. Herzog, Cohen-Macaulay rings, Cambridge Univ. Press: Cambridge 1993.
- [10] W. Bruns and B. Ichim, On the coefficients of Hilbert quasipolynomials, Proc. Amer. Math. Soc. 135 (2007), No. 5, 1305-1308.
- [11] M. Chamberland, A 3 ​ x + 1 3x+1 Survey: Number theory and dynamical systems, pp. 57–78 in: The Ultimate Challenge: The 3 ​ x + 1 3x+1 Problem. Edited by Jeffrey C. Lagarias. American Mathematical Society, Providence, RI, 2010.
- [12] V. Chvatal, D. Klarner and D. E. Knuth, Selected combinatorial research problems, Stanford Computer Science Dept. Technical Report STAN-CS-72-292 June 1972, 31 pages.
- [13] J. Cocke and M. Minsky, Universality of tag systems with P = 2 P=2, Journal of the ACM 11, (1964), No. 1, 15–20.
- [14] L. Collatz, Letter to Michael E. Mays, dated 17 Sept. 1980.
- [15] L. Collatz, On the motivation and origin of the ( 3 ​ n + 1) (3n+1) - problem (Chinese), J. Qufu Normal University, Natural Science Edition [Qufu shi fan da xue xue bao] 12 (1986), No. 3, 9–11. [English translation pp. 241–247 in: The Ultimate Challenge: The 3 ​ x + 1 3x+1 Problem. Edited by Jeffrey C. Lagarias. American Mathematical Society, Providence, RI, 2010.].
- [16] J. H. Conway, Unpredictable Iterations, Proc. 1972 Number Theory Conference (Univ. Colorado, Boulder, Colo., 1972 ), pp. 49–52. Univ. Colorado, Boulder, Colo. 1972.
- [17] J. H. Conway, FRACTRAN: A Simple Universal Computing Language for Arithmetic, In: Open Problems in Communication and Computation (T. M. Cover and B. Gopinath, Eds.), Springer-Verlag: New York 1987, pp. 3-27 [Reprinted pp. 249–264 in: The Ultimate Challenge: The 3 ​ x + 1 3x+1 Problem. Edited by Jeffrey C. Lagarias. American Mathematical Society, Providence, RI, 2010.]
- [18] M. Cook, Universality in elementary cellular automata, Complex Systems 15 (2004), 1–40.
- [19] M. Cook, A concrete view of rule 110 computation, T. Neary, D. Woods, A. K. Seda and N. Murphy (Eds.), Proceedings International Workshop on The Complexity of Simple Programs (CSP 2008), EPCTS (Electronic Proceedings in Theoretical Computer Science) 1 (2009), 31–55.
- [20] M. Cook, D. Soloveichik, E. Winfree and J. Bruck, Programmability of Chemical Reaction Networks, to appear in a Festschrift for Grzegorz Rozenberg, Springer-Verlag.
- [21] Necia Grant Cooper (Ed), From Cardinals to Chaos. Reflections on the life and legacy of Stanslaw Ulam, Cambridge Univ. Press: Cambridge 1989 [Reprint of Los Alamos Science, Vol. 15.]
- [22] H. S. M. Coxeter, Cyclic sequences and frieze patterns: The Fourth Felix Behrend Memorial Lecture), Vinculum 8 (1971), 4–7. [Reprinted in this volume]
- [23] L. Ehrhart, Sur un problème de géométrie diophantienne linéaire. II. Systèmes diophantiens linéaires, J. Reine Angew. Math. 227 (1967), 25–49.
- [24] S. Eliahou, The 3 ​ x + 1 3x+1 problem: new lower bounds on nontrivial cycle lengths, Discrete Math. 118 (1993), 45–56.
- [25] P. Erdős, Private communication with J. C. Lagarias.
- [26] Paul Erdős and R. L. Graham, Old and new problems and results in combinatorial number theory Monographie No. 28 de L’Enseignement Mathématique, Kundig: Geneva 1980. (Chapter 1 appeared in: Enseign. Math. 25 (1979), no. 3-4, 325–344. )
- [27] C. J. Everett, Iteration of the number theoretic function f ⁡ ( 2 ​ n) = n, f ⁡ ( 2 ​ n + 1) = 3 ​ n + 2 f(2n)=n,f(2n+1)=3n+2, Advances in Math. 25 (1977), 42–45.
- [28] A. Evseev, Higman’s PORC conjecture for a family of groups, Bull. London Math. Soc. 40 (2008), 405–414.
- [29] H. M. Farkas, Variants of the 3 ​ N + 1 3N+1 conjecture and multiplicative semigroups, in: Geometry, spectral theory, groups, and dynamics, pp. 121–127, Contemp. Math. Vol 387, Amer. Math. Soc.: Providence, RI 2005.
- [30] H. Furstenberg, Recurrence in ergodic theory and combinatorial number theory, Princeton University Press, Princeton, NJ 1981.
- [31] M. Gardner, Mathematical Games, Scientific American 223 (1970) Number 4 (October), 120–123.
- [32] M. Gardner, Mathematical Games, Scientific American 226 (1972) Number 6 (June), 114–118.
- [33] S. Garoufalidis, The degree of a q q -holonomic sequence is a quadratic quasi-polynomial, eprint: arxiv:1005.4580v1
- [34] E. Glasner, Ergodic Theory via joinings, Mathematical Surveys and Monographs, Vol. 101, American Mathematical Society, Providence, RI, 2003.
- [35] K. Gödel, Über formal unentscheidbare Sätzes der Principia Mathematica und verwandter Systeme I, [On formally undecidable propositions of Principia mathematica and related systems I] Mönatshefte für Mathematik und Physik 28 (1931), 173–198. (English translation in [36, p. 144–195].)
- [36] K. Gödel, Collected Works, Volume I. Publications 1929–1936, S. Feferman et al. (Eds.) , Oxford University Press: New York 1986.
- [37] O. Goldreich, Foundations of cryptography. Basic tools. Cambridge University Press: Cambridge 2001.
- [38] O. Goldreich, A Primer on Pseudorandom Generators, University Lecture Series, No. 55, American Math. Society: Providence, RI 2010.
- [39] K. Greenberg, Integer valued functions on the integers, Math. Medley 17 (1989), 1–10.
- [40] R. K. Guy, Don’t try to solve these problems!, American Math. Monthly 90 (1983), 35–41. [Reprinted in pp. 231–239: The Ultimate Challenge: The 3 ​ x + 1 3x+1 Problem. Edited by Jeffrey C. Lagarias. American Mathematical Society, Providence, RI, 2010.
- [41] R. K. Guy, Conway’s prime-producing machine, Math. Magazine 56 (1983), no. 1, 26–33.
- [42] R. K. Guy, Unsolved Problems in Number Theory. Third Edition. Problem Books in Mathematics, Springer-Verlag: New York 2004.
- [43] R. K. Guy, private communication, 2009.
- [44] H. Hasse, Unsolved Problems in Elementary Number Theory, Lectures at University of Maine (Orono), Spring 1975, Mimeographied notes.
- [45] B. Hasselblatt and A. B. Katok, Introduction to the modern theory of dynamical systems, Cambridge Univ. Press, Cambridge 1995.
- [46] B. Hayes, Computer recreations: The ups and downs of hailstone numbers, Scientific American 250, No. 1, (1984), 10–16.
- [47] K. Hicks, G. L. Mullen, J. L. Yucas and R. Zavislak, A Polynomial Analogue of the 3 ​ N + 1 3N+1 Problem?, American Math. Monthly 115 (2008), No. 7, 615–622.
- [48] G. Higman, Enumerating p p -groups II: Problems whose solution is PORC, Proc. London Math. Soc. 10 (1960), 566–582.
- [49] D. Hilbert, Mathematische Probleme, Göttinger Nachrichten (1900) 253–297. Reprinted in: Archiv der Mathematik und Physik, 3rd Ser. 1 (1901) 44-63 and 213-237. (English translation: Mathematical Problems, Bull. Amer. Math. Soc. 8 (1902) 437–479. Reprinted in: Mathematical Developments Arising From Hilbert Problems, Proc. Symp. Pure Math. Volume 28, AMS: Providence 1976, pp. 1-34.)
- [50] A. J. W. Hilton, private communication, 2010.
- [51] S. D. Isard and H. M. Zwicky, Three open questions in the theory of one-symbol Smullyan systems, SIGACT News, Issue No. 7, 1970, 11–19.
- [52] M. Klamkin, Problem 63 − 13 ∗ 63-13^{\ast}, SIAM Review 5 (1963), 275–276.
- [53] D. A. Klarner, A sufficient condition for certain semigroups to be free, Journal of Algebra 74 (1982), 40–48.
- [54] D. A. Klarner and R. Rado, Arithmetic properties of certain recursively defined sets, Pacific J. Math. 53 (1974), No. 2, 445–463.
- [55] D. E. Knuth, The Art of Computer Programming. Vol 2. Seminumerical Algorithms. Second Edition. Addison-Wesley: Reading, MA 1981.
- [56] A.V. Kontorovich and J. C. Lagarias, Stochastic models for the 3 ​ x + 1 3x+1 problem and generalizations, pp. 131–188 in: The Ultimate Challenge: The 3 ​ x + 1 3x+1 Problem. Edited by Jeffrey C. Lagarias. American Mathematical Society, Providence, RI, 2010.
- [57] I. Krasikov and J. C. Lagarias, Bounds for the 3 ​ x + 1 3x+1 problem using difference inequalities, Acta Arith. 109 (2003), no. 3, 237–258.
- [58] J. C. Lagarias, The 3 ​ x + 1 3x+1 problem and its generalizations, Amer. Math. Monthly 92 (1985), 3–23. [Reprinted with corrections in pp. 31–55 in: The Ultimate Challenge: The 3 ​ x + 1 3x+1 Problem. Edited by Jeffrey C. Lagarias. American Mathematical Society, Providence, RI, 2010. ]
- [59] J. C. Lagarias, The set of rational cycles for the 3 ​ x + 1 3x+1 problem, Acta Arithmetica 56 (1990), 33–53.
- [60] J. C. Lagarias, The 3 ​ x + 1 3x+1 Problem: An Annotated Bibliography (1963-1999), pp. 267–341 in: The Ultimate Challenge: The 3 ​ x + 1 3x+1 Problem. Edited by Jeffrey C. Lagarias. American Mathematical Society, Providence, RI, 2010, pp. 3–29.
- [61] J. C. Lagarias, The 3 ​ x + 1 3x+1 Problem: An Annotated Bibliography, II (2000-2009), arXiv:math/0608208.
- [62] J. C. Lagarias and A. Weiss, The 3 ​ x + 1 3x+1 problem: Two stochastic models, Annals of Applied Probability 2 (1992), 229–261.
- [63] H. Lausch and W. Nöbauer, Algebra of Polynomials, North-Holland Publ. Co.: Amsterdam 1973.
- [64] K. Mahler, Lectures on diophantine approximations. Part I. g g -adic number and Roth’s theorem. Prepared from notes of R. P. Bambah of lectures given at Univ. of Notre Dame in the Fall of 1957, Univ. of Notre Dame Press, Notre Dame, Ind. 1961, xi+188pp.
- [65] M. Mashaal, Bourbaki: A Secret Society of Mathematicians. (Translated from 2002 French original by A. Pierrehumbert) American Math. Society, Providence RI 2006.
- [66] S. Ju. Maslov, On E. L. Post’s “tag problem” (Russian), Trudy Mat. Inst. Steklov 72 91964), 57–68. [English translation: American Math. Soc. Translations, Series 2, Vol. 97 (1970), 1–14.]
- [67] K. R. Matthews, Generalized 3 ​ x + 1 3x+1 mappings: Markov chains and ergodic theory, pp. 70–103 in: The Ultimate Challenge: The 3 ​ x + 1 3x+1 Problem. Edited by Jeffrey C. Lagarias. American Mathematical Society, Providence, RI, 2010.
- [68] P. Michel and M. Margenstern, Generalized 3 ​ x + 1 3x+1 functions and the theory of computation, pp. 105–128 in: The Ultimate Challenge: The 3 ​ x + 1 3x+1 Problem. Edited by Jeffrey C. Lagarias. American Mathematical Society, Providence, RI, 2010. paper in this volume.
- [69] S. J. Miller and R. Takloo-Bighash, An invitation to modern number theory, Princeton University Press: Princeton NJ 2006.
- [70] M. Minsky, Recursive unsolvability of Post’s problem of tag and other topics in the theory of Turing machines, Annals of Mathematics 74 (1961), 437–455.
- [71] M. Minsky, Computation: Finite and Infinite Machines, Prentice-Hall, Inc: Engelwood Cliffs, NJ 1967.
- [72] L. De Mol, Closing the circle: An analysis of Emil Post’s Early Work, Bull. Symbolic Logic 12 (2006), No. 2, 267–289.
- [73] L. De Mol, Study of limits of solvability in tag systems, pp. 170–181 in: J. Durand-Lose, M. Margenstern (Eds.), Machines, Computations, Universality, MCU 2007, Lecture Notes in Computer Science, vol. 4664, Springer-Verlag: New York 2007.
- [74] L. De Mol, Tag systems and Collatz-like functions, Theoretical Computer Science 290 (2008), 92–101.
- [75] L. De Mol, On the boundaries of solvability and unsolvability in tag systems. Theoretical and experimental results., in: T. Neary, D. Woods, A. K. Seda and N. Murphy (Eds.), Proceedings International Workshop on The Complexity of Simple Programs (CSP 2008), EPCTS (Electronic Proceedings in Theoretical Computer Science) 1 (2009), 56–66.
- [76] T. Oliveira e Silva, Empirical verification of the 3 ​ x + 1 3x+1 and related conjectures, pp. 189–207 in: The Ultimate Challenge: The 3 ​ x + 1 3x+1 Problem. Edited by Jeffrey C. Lagarias. American Mathematical Society, Providence, RI, 2010, pp. 3–29.
- [77] E. L. Post, Formal reductions of the general combinatorial decision problem, Amer. J. Math. 65 (1943), 197–215.
- [78] E. L. Post, Absolutely unsolvable problems and relatively undecidable propositions- account of an anticipation, in: M. Davis, Ed., The Undecidable. Basic Papers on Undecidable Propositions, Unsolvable Problems and Computable Functions, Raven Press: New York 1965. (Reprint: Dover Publications, 2004).
- [79] Eric Roosendaal, On the 3 ​ x + 1 3x+1 problem, web document, available at:
http://www.ericr.nl/wondrous/index.html
- [80] J. Roubaud, Un probléme combinatoire posé par poésie lyrique des troubadours, Matématiques et Sciences Humaines 27 Autumn 1969, 5–12.
- [81] Klaus Schmidt, Dynamical Systems of Algebraic Origin. Progress in Math., 128. Birkhäuser Verlag: Basel 1995.
- [82] J. Silverman, The Arithmetic of Dynamical Systems. Springer-Verlag: New York 2007.
- [83] J. Simons and B. de Weger, Theoretical and computational bounds for m m -cycles of the 3 ​ n + 1 3n+1 problem, Acta Arithmetica 117 (2005), 51–70.
- [84] Ya. G. Sinai, Statistical ( 3 ​ X + 1) (3X+1) -Problem, Dedicated to the memory of Jürgen K. Moser. Comm. Pure Appl. Math. 56 No. 7 (2003), 1016–1028.
- [85] Ya. G. Sinai, Uniform distribution in the ( 3 ​ x + 1) (3x+1) problem, Moscow Math. Journal 3 (2003), No. 4, 1429–1440. (S. P. Novikov 65-th birthday issue).
- [86] D. Soloveichik, M. Cook E. Winfree and J. Bruck, Computation with finite stochastic chemical reaction networks, Natural Computing 7 (2008), 615–633.
- [87] Paul R. Stein, Iteration of maps, strange attractors, and number theory-an Ulamian potpourri, pp. 91–106 in [21].
- [88] R. Terras, A stopping time problem on the positive integers, Acta Arithmetica 30 (1976), 241–252.
- [89] R. Terras, On the existence of a density, Acta Arithmetica 35 (1979), 101–102.
- [90] B. Thwaites, My conjecture, Bull. Inst. Math. Appl. 21 (1985), 35–41.
- [91] A. M. Turing, On computable numbers, with an application to the Entschidungsproblem, Proc. London Math. Soc. 42 (1937), 230–265. Corrections, 43 (1937), 544–546.
- [92] S. Ulam, Problems in Modern Mathematics, John Wiley and Sons: New York 1964.
- [93] G. Venturini, On a generalization of the 3 ​ x + 1 3x+1 problem, Adv. Appl. Math. 19 (1997), 295–305.
- [94] Hao Wang, Tag systems and lag systems, Math. Annalen 152 (1963), 65–74.
- [95] G. J. Wirsching, The Dynamical System Generated by the 3 ​ n + 1 3n+1 Function, Lecture Notes in Math. No. 1681, Springer-Verlag: Berlin 1998.
- [96] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys. 55 (1983), 601-644.-
- [97] S. Wolfram, Universality and complexity and cellular automata, Physica C 10 (1984), 1–35.
- [98] S. Wolfram, Theory and Applications of Cellular Automata, World Scientific: Singapore 1987.
- [99] S. Wolfram, Cellular Automata and Complexity: Collected Papers, Westview Press: Perseus Books Group 1994.

[◄][2][image: ar5iv homepage] [3]
[Feeling lucky?][4] [5]
[Conversion report][6]
[Report an issue][7]
[View original on arXiv][8] [►][9]


## Links

[1]: mailto:lagarias@umich.edu
[2]: /html/2111.02634
[3]: /
[4]: /feeling_lucky
[5]: /land_of_honey_and_milk
[6]: /log/2111.02635
[7]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2111.02635
[8]: https://arxiv.org/pdf/2111.02635
[9]: /html/2111.02636
