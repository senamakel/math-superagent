<!-- source: https://arxiv.org/html/0910.1944v1 | converted from HTML -->

1Introduction

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:0910.1944v1 [math.NT] 11 Oct 2009

Stochastic Models for the 3 ​ x + 1 3x+1 and 5 ​ x + 1 5x+1 Problems

Alex V. Kontorovich ***AVK received support from an NSF Postdoc, grant DMS 0802998.

Department of Mathematics

Brown University

Providence, RI

alexk@math.brown.edu

Jeffrey C. Lagarias † † † JCL received support from NSF Grants DMS-0500555 and DMS-0801029.

Department of Mathematics

University of Michigan

Ann Arbor, MI 48109-1109

lagarias@umich.edu

(October 7, 2009)

Abstract

This paper discusses stochastic models for predicting the long-time behavior of the trajectories of orbits of the 3 ​ x + 1 3x+1 problem and, for comparison, the 5 ​ x + 1 5x+1 problem. The stochastic models are rigorously analyzable, and yield heuristic predictions (conjectures) for the behavior of 3 ​ x + 1 3x+1 orbits and 5 ​ x + 1 5x+1 orbits.

## 1 Introduction

The 3 ​ x + 1 3x+1 problem concerns the following operation on integers: if an integer is odd “multiply by three and add one,” while if it is even “divide by two.” This operation is given by the Collatz function

 | C ⁡ ( n) = { 3 ​ n + 1 if ​ n ≡ 1 ( mod 2), n 2 if ​ n ≡ 0 ( mod 2). C(n)=\left\{\begin{array}[]{cl}3n+1&\mbox{if}~n\equiv 1~~(\bmod~2)~,\\ \\ \displaystyle\frac{n}{2}&\mbox{if}~~n\equiv 0~~(\bmod~2)~.\end{array}\right. |  | (1.1) |

The 3 ​ x + 1 3x+1 problem concerns what happens if one iterates this operation starting from a given positive integer n n. The unsolved 3 ​ x + 1 3x+1 Problem or Collatz problem is to prove (or disprove) that such iterations always eventually reach the number 1 1 (and therefter cycle, taking values 1, 4, 2, 1 1,4,2,1). This problem goes under many other names, including: Syracuse Problem, Hasse’s Algorithm, Kakutani’s Problem and Ulam’s Problem.

The 3 ​ x + 1 3x+1 Conjecture has now been verified for all n ≤ 5.67 × 10 18 n\leq 5.67\times 10^{18} by computer experiments [31].

### 1.1 3 ​ x + 1 3x+1 Function

There are a number of different functions that encode the 3 ​ x + 1 3x+1 problem, which proceed through the iteration at different speeds. The following two functions prove to be more convenient for probabilistic analysis than the Collatz function. The first of these is the 3 ​ x + 1 3x+1 function T ⁡ ( n) T(n) (or 3 ​ x + 1 3x+1 map)

 | T ⁡ ( n) = { 3 ​ n + 1 2 if ​ n ≡ 1 ( mod 2), n 2 if ​ n ≡ 0 ( mod 2). T(n)=\left\{\begin{array}[]{cl}\displaystyle\frac{3n+1}{2}&\mbox{if}~~n\equiv 1~~(\bmod~2)~,\\ \\ \displaystyle\frac{n}{2}&\mbox{if}~~n\equiv 0~~(\bmod~2)~.\end{array}\right. |  | (1.2) |

This function divides out one power of 2 2, after an odd input is encountered; it is defined on the domain of all integers.

The second function, the accelerated 3 ​ x + 1 3x+1 function U ⁡ ( n) U(n), is defined on the domain of all odd integers, and removes all powers of 2 2 at each step. It is given by

 | U ⁡ ( n) = 3 ​ n + 1 2 ord 2 ​ ( 3 ​ n + 1), U(n)=\frac{3n+1}{2^{{\rm ord}_{2}(3n+1)}}, |  | (1.3) |

in which ord 2 ​ ( n) {\rm ord}_{2}(n) counts the number of powers of 2 2 dividing n n. The function U ⁡ ( n) U(n) was studied by Crandall [14] in 1978.

The long-term dynamics under iteration of the 3 ​ x + 1 3x+1 map has proved resistant to rigorous analysis. It is conjectured that there is a finite positive constant C C so that all trajectories eventually enter and stay in the region − C ≤ n ≤ C. -C\leq n\leq C. In particular, there are finitely many periodic orbits and all trajectories eventually enter one of these periodic orbits. On the domain of positive integers it is conjectured there is is a single periodic orbit { 1, 2 } \{1,2\}; this is part of the 3 ​ x + 1 3x+1 Conjecture. On the domain of negative integers, the known periodic orbits are the three orbits { − 1 } \{-1\}, { − 5, − 7, − 10 } \{-5,-7,-10\} and { − 17, − 25, − 37, − 55, − 82, − 41, − 61, − 91, − 136, − 68, − 34 } \{-17,-25,-37,-55,-82,-41,-61,-91,-136,-68,-34\}.

### 1.2 5 ​ x + 1 5x+1 Problem

For comparison purposes, we also consider the 5 ​ x + 1 5x+1 problem, which concerns iterates of the Collatz 5 ​ x + 1 5x+1 function

 | C 5 ​ ( n) = { 5 ​ n + 1 if ​ n ≡ 1 ( mod 2), n 2 if ​ n ≡ 0 ( mod 2). C_{5}(n)=\left\{\begin{array}[]{cl}5n+1&\mbox{if}~n\equiv 1~~(\bmod~2)~,\\ \\ \displaystyle\frac{n}{2}&\mbox{if}~~n\equiv 0~~(\bmod~2)~.\end{array}\right. |  | (1.4) |

For this function we also have analogues of the other two functions above. We define the 5 ​ x + 1 5x+1 function T 5 ​ ( n) T_{5}(n) (or 5 ​ x + 1 5x+1 map), given by

 | T 5 ​ ( n) = { 5 ​ n + 1 2 if ​ n ≡ 1 ( mod 2), n 2 if ​ n ≡ 0 ( mod 2). T_{5}(n)=\left\{\begin{array}[]{cl}\displaystyle\frac{5n+1}{2}&\mbox{if}~~n\equiv 1~~(\bmod~2)~,\\ \\ \displaystyle\frac{n}{2}&\mbox{if}~~n\equiv 0~~(\bmod~2)~.\end{array}\right. |  | (1.5) |

It is defined on the set of all integers.

The second function, the accelerated 5 ​ x + 1 5x+1 function U 5 ​ ( n) U_{5}(n), is defined on the domain of all odd integers, and removes all powers of 2 2 at each step. It is given by

 | U 5 ​ ( n) = 5 ​ n + 1 2 o ​ r ​ d 2 ​ ( 5 ​ n + 1), U_{5}(n)=\frac{5n+1}{2^{ord_{2}(5n+1)}}, |  | (1.6) |

in which o ​ r ​ d 2 ​ ( n) ord_{2}(n) counts the number of powers of 2 2 dividing n n.

The long-term dynamics under iteration of the 5 ​ x + 1 5x+1 map on the integers is conjecturally quite different from the 3 ​ x + 1 3x+1 map. It is conjectured that a density one set of integers belong to divergent trajectories, ones with | T ( k) ​ ( n) | → ∞ |T^{(k)}(n)|\to\infty. It is also conjectured that there are a finite number of periodic orbits, which include the orbits { 1, 3, 8, 4, 2 } \{1,3,8,4,2\} and { 13, 33, 83, 208, 104, 52, 26 } \{13,33,83,208,104,52,26\} on the positive integers and the orbit { − 1, − 2 } \{-1,-2\} on the negative integers. An infinite number of trajectories eventually enter one of these orbits, but the set of all integers entering each of these orbits is believed to have density zero.

### 1.3 Stochastic models

This paper is concerned with probabilistic models for the behavior of the 3 ​ x + 1 3x+1 function iterates, and for comparison, the 5 ​ x + 1 5x+1 function iterates. The absence of rigorous analysis of the long-term behavior under iteration of these functions provides one motivation to formulate probabilistic models of the behavior of the 3 ​ x + 1 3x+1 map and 5 ​ x + 1 5x+1 map. These models can make predictions that can be compared to empirical data, which, by uncovering discrepancies, may lead to the discovery of new hidden regularities in their behavior under iterations. Note that both the 3 ​ x + 1 3x+1 map and the 5 ​ x + 1 5x+1 map have the positive integers and negative integers as invariant subsets; thus their dynamics can be studied separately on these domains. The original problems concern their dynamics restricted to the positive integers.

Here we survey what is known about iteration of these maps, in frameworks which have a probabilistic interpretation. A great deal is known about the initial behavior of the iteration of the 3 ​ x + 1 3x+1 map and 5 ​ x + 1 5x+1 map; such results are summarized in § 2 and § 7, respectively. Here some models for the 5 ​ x + 1 5x+1 problem are new, developed in parallel with models in Lagarias and Weiss [23]. The major unsolved questions have to do with the behavior of long term aspects of the iterations. It is here that stochastic models have an important role to play. We present models for forward iteration of the map which are of random walk or Markov process type, and models for backwards iteration of the map, which are branching processes or branching random walks. Such models can address how the iteration behaves for a randomly selected input value n n. More sophisticated models address behavior of “extremal” input values. Analysis of these latter models typically uses some variant of the theory of large deviations.

We are interested in using these stochastic models to explore similarities and differences between the iteration behavior of the 3 ​ x + 1 3x+1 and 5 ​ x + 1 5x+1 functions. There are many similarities which are exact parallels, listed in the concluding § 11. The main differences are: in short term iteration on the integers ℤ {{Z}}, 3 ​ x + 1 3x+1 iterates tend to get smaller, while 5 ​ x + 1 5x+1 iterates tend to get larger (in absolute value). For long term iteration it is conjectured that all 3 ​ x + 1 3x+1 trajectories eventually enter finite cycles; it is conjectured that almost all 5 ​ x + 1 5x+1 trajectories diverge. Stochastic models permit making some quantitative versions of this behavior. These include the following (conjectural) predictions.

1. 1.

The number of integers 1 ≤ n ≤ x 1\leq n\leq x whose 3 ​ x + 1 3x+1 forward orbit reaches 1 1 is about x η 3 + o ⁡ ( 1) x^{\eta_{3}+o(1)}, where η 3 = 1. \eta_{3}=1.

2. 2.

Restricting to those integers 1 ≤ n ≤ x 1\leq n\leq x whose 3 ​ x + 1 3x+1 map forward orbit includes 1 1, the trajectories of most such n n reach 1 1 after about 6.95212 ​ log ⁡ n 6.95212\log n steps.

3. 3.

Only finitely many 3 ​ x + 1 3x+1 map trajectories starting at x x reach 1 1 after more than ( γ 3 + ϵ) ​ log ⁡ x (\gamma_{3}+\epsilon)\log x steps, while infinitely many positive x x reach 1 1 after more than ( γ 3 − ϵ) ​ log ⁡ x (\gamma_{3}-\epsilon)\log x steps, where γ 3 ≈ 41.67765 \gamma_{3}\approx 41.67765.

4. 4.

The number of integers 1 ≤ n ≤ x 1\leq n\leq x whose 5 ​ x + 1 5x+1 map forward orbit includes 1 1 is about x η 5 + o ⁡ ( 1) x^{\eta_{5}+o(1)}, where η 5 ≈ 0.65049. \eta_{5}\approx 0.65049.

5. 5.

Restricting to those integers 1 ≤ n ≤ x 1\leq n\leq x whose 5 ​ x + 1 5x+1 map forward orbit includes 1 1, the trajectories of most such n n reach 1 1 after about 9.19963 ​ log ⁡ n 9.19963\log n steps.

6. 6.

Only finitely many 5 ​ x + 1 5x+1 map trajectories starting at x x reach 1 1 after more than ( γ 5 + ϵ) ​ log ⁡ x (\gamma_{5}+\epsilon)\log x steps, while infinitely many positive x x reach 1 1 after more than ( γ 5 − ϵ) ​ log ⁡ x (\gamma_{5}-\epsilon)\log x steps, where γ 5 ≈ 84.76012 \gamma_{5}\approx 84.76012.

In the case of the 3 ​ x + 1 3x+1 map, extensive numerical evidence supports these predictions. There has been much less computational testing of the 5 ​ x + 1 5x+1 map, and the predictions above are less tested in these cases.

We also survey a number of rigorous results that fit in this framework: these results describe aspects of the initial part of the iteration. These include symbolic dynamics for accelerated iteration, given in § 6, which were used by Kontorovich and Sinai [18] to show that suitably scaled versions of initial trajectories converge in a limit to geometric Brownian motion. These also include results on Benford’s law for the initial base B digits of the initial iterates of the functions above, given in § 9.

### 1.4 Contents of the paper

In § 2 through § 6 we first consider the 3 ​ x + 1 3x+1 function. Then in § 7 and § 8 we give comparison results for the 5 ​ x + 1 5x+1 problem. In § 9 and § 10 we give results on Benford’s law and for 2 2 -adic generalizations, in parallel for both the 3 ​ x + 1 3x+1 function and 5 ​ x + 1 5x+1 function.

In § 2 we discuss the iteration of the 3 ​ x + 1 3x+1 map. We describe its symbolic dynamics, and formulate several statistics of orbits, which will be studied via stochastic models in later sections. We state various rigorously proved results about these statistics. For a given starting value n n, these statistics include the λ \lambda -stopping time σ λ ​ ( n) \sigma_{\lambda}(n), the total stopping time σ ∞ ​ ( n), \sigma_{\infty}(n), the maximum excursion value t ⁡ ( n) t(n), and counting functions N k ​ ( n) N_{k}(n) and N k ∗ ​ ( n) N_{k}^{\ast}(n), for the number of backward iterates at depth k k of a given integer a a, with the latter only counting iterates that are not divisible by 3 3. We also review what has been rigorously proved about these statistics, and give tables of empirical results known about these statistics, found by large scale computations. Further data appears in the paper of Oliveira e Silva [31] (in this volume).

In § 3 we discuss stochastic models for a single orbit under forward iteration of the 3 ​ x + 1 3x+1 map. These include a multiplicative random product model (MRP model) and a logarithmic rescaling giving an additive random walk model taking unequal steps (BRW model), which has a negative drift. These models predict that all orbits converge to a bounded set, and that the total stopping time σ ∞ ​ ( n) \sigma_{\infty}(n) for the 3 ​ x + 1 3x+1 map of a random starting point n n should be about 6.95212 ​ log ⁡ n 6.95212\log n steps, and as n → ∞ n\to\infty have a Gaussian distribution around this value, with standard deviation proportional to log ⁡ n \sqrt{\log n}.

In § 4 we discuss models for extreme values of the total stopping time of the 3 ​ x + 1 3x+1 map. We introduce a repeated random walk model (RRW model) which produces a random trajectory separately for each integer n n. We present results obtained using the theory of large deviations which rigorously determine behavior in this model of a statistic which is an analogue of the scaled total stopping time γ ⁡ ( n):= σ ∞ ​ ( n) log ⁡ n \gamma(n):=\frac{\sigma_{\infty}(n)}{\log n}. The model predicts that the limit superior of these values should be a constant γ R ​ R ​ W ≈ 41.67765 \gamma_{RRW}\approx 41.67765, which is larger than the average value 6.95212 6.95212 this variable takes. This prediction agrees fairly well with the empirical data given in § 2.

In § 5 we survey results concerning forward iteration of the accelerated 3 ​ x + 1 3x+1 map. These include a complete description of its symbolic dynamics. We also show that a suitable scaling limit of these trajectories is a geometric Brownian motion, and discuss the equidistribution of various images via entropy.

In § 6 we describe stochastic models simulating backward iteration of the 3 ​ x + 1 3x+1 function. These models grow random labelled trees, whose levels describe branching random walks. These models give exact answers for the expected number of leaves at a given depth k k, analogous to the number of integers having total stopping time k k, and also predict the extremal behavior of the scaled total stopping time function γ ⁡ ( n):= σ ∞ ​ ( n) log ⁡ n \gamma(n):=\frac{\sigma_{\infty}(n)}{\log n}. It yields a prediction for the limit superior of these values to be γ B ​ P ≈ 41.677647 \gamma_{BP}\approx 41.677647, the same value as for the repeated random walk process above.

In § 7 and § 8 we present analogous results for the 5 ​ x + 1 5x+1 map. Much less empirical study has been made for iteration of the 5 ​ x + 1 5x+1 function, so there is less empirical data available for comparison.

In § 7 we define 5 ​ x + 1 5x+1 statistics of orbits. These are analogues of the 3 ​ x + 1 3x+1 statistics given in § 3, but some require modification to reflect the fact that 5 ​ x + 1 5x+1 orbits grow on average. We also review what is known rigorously about the behavior of this function; in particular the symbolic dynamics of the forward iteration of the 5 ​ x + 1 5x+1 map is exactly the same as that for the 3 ​ x + 1 3x+1 map. The statistics introduced include a reverse analogue of the stopping time, the λ + \lambda^{+} -stopping time σ λ + ​ ( n) \sigma_{\lambda}^{+}(n), and also the total stopping time σ ∞ ​ ( n, T 5) \sigma_{\infty}(n;T_{5}), Since most trajectories are believed to be unbounded, the total stopping time is believed to take the value + ∞ +\infty for almost all initial conditons. In place of the maximum excursion value, we consider the minimum excursion value t − ​ ( n) t^{-}(n)!

In § 8 we present results on stochastic models for the 5 ​ x + 1 5x+1 iteration. These include repeated random walk models for the forward iteration of this function, paralleling results of § 4; the convergence to Brownian motion of appropriately scaled trajectories, paralleling results of § 5; and branching random walk models for inverse iteration, paralleling results of § 6. In the latter case we present some new results. The most interesting results of the analysis of these models is the prediction that the number of integers below x x which iterate under the 5 ​ x + 1 5x+1 to 1 1 should be about x δ 5 + o ⁡ ( 1) x^{\delta_{5}+o(1)} with δ 5 ≈ 0.65041 \delta_{5}\approx 0.65041, and that all integers below x x that eventually iterate to 1 1 necessarily do it in at most ( γ 5, B ​ P + o ⁡ ( 1)) ​ log ⁡ x (\gamma_{5,BP}+o(1))\log x steps, where γ 5, B ​ P ≈ 84.76012 \gamma_{5,BP}\approx 84.76012.

In § 9 we discuss another property of 3 ​ x + 1 3x+1 iterates and 5 ​ x + 1 5x+1 iterates: Benford’s law. In this context “Benford’s law” asserts that the distribution of the initial decimal digits of numbers in a trajectory { T ( k) ​ ( n): 1 ≤ k ≤ m } \{T^{(k)}(n):1\leq k\leq m\} approaches a particular non-uniform probability distribution, the Benford distribution, in which an initial digit less than k k occurs with probability log 10 ⁡ k \log_{10}k, so that 1 1 is the most likely initial digit. We summarize results showing that most initial starting values of both the 3 ​ x + 1 3x+1 map and the 5 ​ x + 1 5x+1 map have initial iterates exhibiting Benford-like behavior; this property holds for any fixed finite set of initial iterates.

In § 10 we review results on the extensions to the domain of 2 2 -adic integers ℤ 2 {{Z}}_{2} of the functions T 3 ​ ( n) T_{3}(n) and T 5 ​ ( n) T_{5}(n). These functions have the pleasant property that their definition makes sense 2 2 -adically, and each function has a unique continuous 2 2 -adic extension, which we denote T ~ 3: ℤ 2 → ℤ 2 \tilde{T}_{3}:{{Z}}_{2}\to{{Z}}_{2} and T ~ 5: ℤ 2 → ℤ 2 \tilde{T}_{5}:{{Z}}_{2}\to{{Z}}_{2}, respectively. These extended maps are measure-preserving for the 2 2 -adic Haar measure, and are ergodic in a very strong sense. The interesting feature is that at the level of 2 2 -adic extensions the 3 ​ x + 1 3x+1 map and 5 ​ x + 1 5x+1 map are identical maps from the perspective of measure theory. They are both topologically and measurably conjugate to the full shift on the 2 2 -adic integers, hence they are topologically and measurably conjugate to each other! Thus their dynamics are “the same.” This contrasts with the great difference between these maps view on the domain of integers.

In § 11 we present concluding remarks, summarizing this paper, comparing properties under iteration of the 3 ​ x + 1 3x+1 map and 5 ​ x + 1 5x+1 map. The short-run behavior under iteration of these maps have some strong similarities. However all evidence indicates that the long-run behavior of iteration for the 3 ​ x + 1 3x+1 map and the 5 ​ x + 1 5x+1 map on the integers ℤ {{Z}} is very different. We also list a set of insights and topics for further investigation.

#### Notation.

For convenience, when comparing the 3 ​ x + 1 3x+1 maps with the corresponding 5 ​ x + 1 5x+1 maps, we may write C 3 ​ ( n), T 3 ​ ( n), U 3 ​ ( n) C_{3}(n),T_{3}(n),U_{3}(n) in place of C ⁡ ( n), T ⁡ ( n), U ⁡ ( n) C(n),T(n),U(n) above.

#### Acknowledgments.

The authors thank Steven J. Miller for a careful reading of and many corrections to an earlier draft of this manuscript. AVK wishes to thank the hospitality of Dorian Goldfeld and Columbia University during this project.

## 2 The 3 ​ x + 1 3x+1 Function: Symbolic Dynamics and Orbit Statistics

In this section we consider the 3 ​ x + 1 3x+1 map T ⁡ ( n) T(n). We recall basic properties of its symbolic dynamics. We also define several different statistics for describing its behavior on individual trajectories, and summarize what is rigorously proved about these statistics. In later sections we will present probabilistic models which are intended to model the behavior of these statistics.

### 2.1 3 ​ x + 1 3x+1 Symbolic Dynamics: Parity Sequence

The behavior of the map T ⁡ ( n) T(n) under iteration is completely described by the parities of the successive iterates.

###### Definition 2.1

(i) For a function T: ℤ → ℤ T:{{Z}}\to{{Z}} and input value n ∈ ℤ n\in{{Z}} define the parity sequence of n n to be

 | S ⁡ ( n):= ( n ( mod 2), T ⁡ ( n) ( mod 2), T ( 2) ​ ( n) ( mod 2), …) S(n):=(n~(\bmod~2),T(n)~(\bmod~2),T^{(2)}(n)~(\bmod~2),...) |  | (2.7) |

in which T ( k) ​ ( n) T^{(k)}(n) denotes the k k -th iterate, so that T ( 2) ​ ( n):= T ⁡ ( T ⁡ ( n)) T^{(2)}(n):=T(T(n)). This is an infinite vector of zeros and ones.

(ii) For k ≥ 1 k\geq 1 its k k -truncated parity sequence is a vector giving the initial segment of k k terms of S ⁡ ( n) S(n), i.e.

 | S [k] ​ ( n):= ( n ( mod 2), T ⁡ ( n) ( mod 2), T ( 2) ​ ( n) ( mod 2), ⋯, T ( k − 1) ​ ( n) ( mod 2)). S^{[k]}(n):=(n~(\bmod~2),T(n)~(\bmod~2),T^{(2)}(n)~(\bmod~2),\cdots,T^{(k-1)}(n)~(\bmod~2)). |  | (2.8) |

A basic result on the iteration is as follows.

###### Theorem 2.1

(Parity Sequence Symbolic Dynamics) The k k -truncated parity sequence S [k] ​ ( n) S^{[k]}(n) of the first k k iterates of the 3 ​ x + 1 3x+1 map T ⁡ ( x) T(x) is periodic in n n with period 2 k 2^{k}. Each of the 2 k 2^{k} possible 0 − 1 0-1 vectors occurs exactly once in the initial segment 1 ≤ n ≤ 2 k 1\leq n\leq 2^{k}.

#### Proof.

This result is due to Terras [38] in 1976 and Everett [16] in 1977. A proof is given as Theorem B in Lagarias [21].

An immediate consequence is that an integer n n is uniquely determined by the parity sequence S ⁡ ( n) S(n) of its forward orbit. To see this, note that any two distinct integers fall in different residue classes ( mod 2 k) (\bmod~2^{k}) for large enough k k, so will have different parity sequences. The parity sequence thus provides a symbolic dynamics which keeps track of the orbit. Taken on the integers, only countably many different parity sequences occur out of the uncountably many possible infinite 0 − 1 0-1 sequences.

### 2.2 3 ​ x + 1 3x+1 Stopping Time Statistics: λ \lambda -stopping times

The initial statistic we consider is the number of iteration steps needed to observe a fixed amount of decrease of size in the iterate.

###### Definition 2.2

For fixed λ > 0 \lambda>0 the λ \lambda -stopping time σ λ ​ ( n) \sigma_{\lambda}(n) of a map T: ℤ → ℤ T:{{Z}}\to{{Z}} from input n n is the minimal value of k ≥ 0 k\geq 0 such that T ( k) ​ ( n) < λ ​ n T^{(k)}(n)<\lambda n, e.g.

 | σ λ ​ ( n):= inf { k ≥ 0: T ( k) ​ ( n) n < λ }. \sigma_{\lambda}(n):=\inf\left\{k\geq 0:\frac{T^{(k)}(n)}{n}<\lambda\right\}. |  | (2.9) |

If no such value k k exists, we set σ λ ​ ( n) = + ∞. \sigma_{\lambda}(n)=+\infty.

This notion for λ = 1 \lambda=1 was introduced in 1976 by Terras [38] who called it the stopping time, and denoted it σ ⁡ ( n) \sigma(n). The more general λ \lambda -stopping time is interesting in the range 0 < λ ≤ 1 0<\lambda\leq 1; it satisfies σ λ ​ ( n) = 0 \sigma_{\lambda}(n)=0 for all λ > 1 \lambda>1.

Terras [38] studied the set of numbers having stopping time at most k k, denoted

 | S 1 ​ ( k):= { n: σ 1 ​ ( n) ≤ k }. S_{1}(k):=\{n:~\sigma_{1}(n)\leq k\}. |  | (2.10) |

He used Theorem 2.1 to show ( [38], [39]) that this set of integers has a natural density, as defined below, and that this density approaches 1 1 as k → ∞ k\to\infty.

Later this result was generalized. Rawsthorne [32] in 1985 introduced the case of general λ \lambda, and Borovkov and Pfeifer [10, Theorem 2] in 2000 considered criteria with several stopping time conditions.

There are several notions of density of a set Σ \Sigma of the natural numbers ℕ = { 1, 2, 3, … } {{N}}=\{1,2,3,...\}. The lower asymptotic density 𝔻 ¯ ​ ( Σ) \underline{{{D}}}(\Sigma) is defined for all infinite sets Σ \Sigma, and is given by

 | 𝔻 ¯ ​ ( Σ):= lim inf t → ∞ 1 t ​ | { n ∈ Σ: n ≤ t } |. \underline{{{D}}}(\Sigma):=\liminf_{t\to\infty}\frac{1}{t}|\{n\in\Sigma:~n\leq t\}|. |  | (2.11) |

The assertion that an infinite set Σ ⊂ ℕ \Sigma\subset{{N}} of natural numbers has a natural density 𝔻 ⁡ ( Σ) {{D}}(\Sigma) is the assertion that the following limit exists:

 | 𝔻 ⁡ ( Σ):= lim t → ∞ 1 t ​ | { n ∈ Σ: n ≤ t } |. {{D}}(\Sigma):=\lim_{t\to\infty}\frac{1}{t}|\{n\in\Sigma:~n\leq t\}|. |  | (2.12) |

Sets with a natural density automatically have 𝔻 ​ ( Σ) = 𝔻 ¯ ​ ( Σ). {{D}}(\Sigma)=\underline{{{D}}}(\Sigma).

###### Theorem 2.2

( λ \lambda -Stopping Time Natural Density)

(i) For the 3 ​ x + 1 3x+1 map T ⁡ ( n) T(n), and any fixed 0 < λ ≤ 1 0<\lambda\leq 1 and k ≥ 1 k\geq 1, the set S λ ​ ( k) S_{\lambda}(k) of integers having λ \lambda -stopping time at most k k has a well-defined natural density 𝔻 ​ ( S λ ​ ( k)) {{D}}(S_{\lambda}(k)).

(ii) For λ \lambda fixed and k → ∞ k\to\infty, this natural density satisfies

 | 𝔻 ​ ( S λ ​ ( k)) → 1. {{D}}(S_{\lambda}(k))\to 1. |  | (2.13) |

In particular, the set of numbers with finite λ \lambda -stopping time has natural density 1 1.

#### Proof.

For the special case λ = 1 \lambda=1, that is the stopping time, this is the basic result of Terras [38], [39], obtained also by Everett [16]. A proof for λ = 1 \lambda=1 is given as Theorem A in Lagarias [21]. The idea is that by Theorem 2.1, each arithmetic progression ( mod 2 k) (\bmod~2^{k}) has iterates that multiply by a certain pattern of 1 2 \frac{1}{2} or 3 2 \frac{3}{2} for the first k k steps. A certain subset of the 2 k 2^{k} -arithmetic progressions ( mod 2 k) (\bmod 2^{k}) will have the product of these numbers fall below λ \lambda, and these arithmetic progressions give the density. To see that the density goes to 1 1 as k → ∞ k\to\infty, one must show that most arithmetic progressions ( mod 2 k) (\bmod 2^{k}) have a product smaller than one. Theorem 2.1 says that all products occur equally likely, and since the geometric mean of these products is ( 3 4) 1 2 < 1 \left(\frac{3}{4}\right)^{\frac{1}{2}}<1, one can establish that such a decrease occurs for all but an exponentially small set of patterns, of size O ⁡ ( 2 0.94995 ​ k) O(2^{0.94995k}) out of 2 k 2^{k} possible patterns. One can show a similar result for decrease by a factor of any fixed λ \lambda, and a proof of natural density for general λ > 0 \lambda>0 is given in Borovkov and Pfeifer [10, Theorem 3].

The results above are rigorous results, and therefore we have no compelling need to find stochastic models to model the behavior of stopping times. Nevertheless stochastic models intended to analyze other statistics produce in passing models for stopping time distributions. In § 3.1 we present such a model, which gives an interpretation of these stopping time densities as exact probabilities of certain events.

#### Remark.

The analysis in Theorem 2.2 treats λ \lambda as fixed. In fact one can also prove rigorous results which allow λ \lambda to vary slowly (as a function of n n), under the restriction that λ ≤ log 2 ⁡ n. \lambda\leq\log_{2}n.

### 2.3 3 ​ x + 1 3x+1 Stopping Time Statistics: Total Stopping Times

The following concept concerns the speed at which positive integers iterate to 1 1 under the map T T, assuming they eventually get there.

###### Definition 2.3

The total stopping time σ ∞ ​ ( n) \sigma_{\infty}(n) for iteration of the 3 ​ x + 1 3x+1 map T ⁡ ( n) T(n) is defined for positive integers n n by

 | σ ∞ ​ ( n):= inf { k ≥ 0: T ( k) ​ ( n) = 1 }. \sigma_{\infty}(n):=\inf\{k\geq 0:~T^{(k)}(n)=1\}. |  |

We set σ ∞ ​ ( n) = + ∞ \sigma_{\infty}(n)=+\infty if no finite k k has this property.

The 3 ​ x + 1 3x+1 Conjecture asserts that all positive integers have a finite total stopping time.

Concerning lower bounds for this statistic, there are some rigorous results. First, since each step decreases n n by at most a factor of 2 2, we trivially have

 | σ ∞ ​ ( n) ≥ log ⁡ n log ⁡ 2 ≈ 1.4426 ​ log ⁡ n. \sigma_{\infty}(n)\geq\frac{\log n}{\log 2}\approx 1.4426\log n. |  |

The strongest result on the existence of integers having a large total stopping time is the following result of Applegate and Lagarias [5, Theorem 1.1].

###### Theorem 2.3

(Lower Bound for 3 ​ x + 1 3x+1 Total Stopping Times) There are infinitely many n n whose total stopping time satisfies

 | σ ∞ ​ ( n) ≥ ( 29 29 ​ log ⁡ 2 − 14 ​ log ⁡ 3) ​ log ⁡ n ≈ 6.14316 ​ log ⁡ n. \sigma_{\infty}(n)\geq\left(\frac{29}{29\log 2-14\log 3}\right)\log n\approx 6.14316\log n. |  | (2.14) |

Nothing has been rigorously proved about either the average size of the total stopping time, or about upper bounds for the total stopping time (since such would imply the main conjecture!). This provides motivation to study stochastic models for this statistic, to make guesses how it may behave.

The various stochastic models discussed in § 3, as well as empirical evidence given below, suggest that the size of this statistic will always be proportional to log ⁡ n \log n. This motivates the following definition.

###### Definition 2.4

For n ≥ 1 n\geq 1 the scaled total stopping time γ ∞ ​ ( n) \gamma_{\infty}(n) of the 3 ​ x + 1 3x+1 function is given by

 | γ ∞ ​ ( n):= σ ∞ ​ ( n) log ⁡ n. \gamma_{\infty}(n):=\frac{\sigma_{\infty}(n)}{\log n}. |  | (2.15) |

This value will be finite for all positive n n only if the 3 ​ x + 1 3x+1 conjecture is true.

A stochastic model in § 3 makes strong predictions about the distribution of scaled total stopping times: they should have a Gaussian distribution with mean

 | μ:= ( 1 2 ​ log ⁡ 4 3) − 1 ≈ 6.95212 \mu:=\left(\frac{1}{2}\log\frac{4}{3}\right)^{-1}\approx 6.95212 |  |

and variance

 | σ:= 1 2 ​ log ⁡ 3 ​ ( 1 2 ​ log ⁡ 4 3) 3 2, \sigma:=\frac{1}{2}\log 3\left(\frac{1}{2}\log\frac{4}{3}\right)^{\frac{3}{2}}, |  |

cf. Theorem 3.2. In particular, half of all integers ought to have a total stopping time σ ∞ ​ ( n) ≥ μ ​ log ⁡ n ≈ 6.95212 ​ log ⁡ n. \sigma_{\infty}(n)\geq\mu\log n\approx 6.95212\log n. It seems scandalous that there is no unconditional proof that infinitely many n n have a stopping time at least this large, compared to the bound ( 2.14) in Theorem 2.3 above!

We next define a limiting constant associated with extremal values of the scaled total stopping time for the 3 ​ x + 1 3x+1 map.

###### Definition 2.5

The 3 ​ x + 1 3x+1 scaled stopping constant is the quantity

 | γ = γ 3:= lim sup n → ∞ γ ∞ ​ ( n) = lim sup n → ∞ σ ∞ ​ ( n) log ⁡ n. \gamma=\gamma_{3}:=\limsup_{n\to\infty}\gamma_{\infty}(n)=\limsup_{n\to\infty}\frac{\sigma_{\infty}(n)}{\log n}. |  | (2.16) |

We now give empirical data about these extremal values. Table 1 presents empirical data on record holders for the function γ ∞ ​ ( n) \gamma_{\infty}(n), compiled by Roosendaal [33]. This table also includes data on another statistic called the ones-ratio (or completeness), taken from Roosendaal [33, Completeness and Gamma Records]. The function ones ( n n) counts the number of odd iterates of the 3 ​ x + 1 3x+1 function to reach 1 1 starting from n n (including 1 1), and

 | ones-ratio ​ ( n):= ones ​ ( n) / σ ∞ ​ ( n). \mbox{ones-ratio}(n):=\mbox{ones}(n)/\sigma_{\infty}(n). |  | (2.17) |

Table 1 shows that the function γ ⁡ ( n) \gamma(n) is not a monotone increasing function of the ones-ratio, compare rows 9 and 10. The values with question marks mean that all intermediate values have not been searched, so these values are not known to be record holders.

k k | #k-th record ​ n k \mbox{\#k-th record}~~n_{k} | σ ∞ ​ ( n k) \sigma_{\infty}(n_{k}) | o ​ n ​ e ​ s ones ( n k n_{k}) | o ​ n ​ e ​ s − r ​ a ​ t ​ i ​ o ones-ratio | γ ∞ ​ ( n k) \gamma_{\infty}(n_{k}) |

1 | 3 | 5 | 2 | 0.400000 | 4.551196 |

2 | 7 | 11 | 5 | 0.454545 | 5.652882 |

3 | 9 | 13 | 6 | 0.461358 | 5.916555 |

4 | 27 | 70 | 41 | 0.585714 | 21.238915 |

5 | 230 631 | 278 | 164 | 0.589928 | 22.512720 |

6 | 626 331 | 319 | 189 | 0.592476 | 23.899366 |

7 | 837 799 | 329 | 195 | 0.592705 | 24.122828 |

8 | 1 723 519 | 349 | 207 | 0.593123 | 24.303826 |

9 | 3 732 423 | 374 | 222 | 0.593583 | 24.714906 |

10 | 5 649 499 | 384 | 228 | 0.593750 | 24.699176 |

11 | 6 649 279 | 416 | 248 | 0.596154 | 26.479917 |

12 | 8 400 511 | 429 | 256 | 0.596737 | 26.907006 |

13 | 63 728 127 | 592 | 357 | 0.603041 | 32.943545 |

14 | 3 743 559 068 799 | 966 | 583 | 0.603520 | 33.366656 |

15 | 100 759 293 214 567 | 1134 | 686 | 0.604938 | 35.169600 |

?16 | 104 899 295 810 901 231 | 1404 | 850 | 0.605413 | 35.823841 |

?17 | 268 360 655 214 719 480 367 | 1688 | 1022 | 0.605450 | 35.885221 |

?18 | 6 852 539 645 233 079 741 799 | 1840 | 1115 | 0.605978 | 36.595864 |

?19 | 7 219 136 416 377 236 271 195 | 1848 | 1120 | 0.606061 | 36.716918 |

Table 1: Record Values for γ ∞ ​ ( n) \gamma_{\infty}(n) and for ones-ratio(n).

In § 4 we present a stochastic model which makes a prediction for the extremal value of γ \gamma. A quite different model is discussed in § 7, which makes exactly the same prediction! For both models the analogue of the constant γ:= lim sup γ ∞ ​ ( n) \gamma:=\limsup\gamma_{\infty}(n) exists and equals a constant which numerically is approximately 41.677647 41.677647, with corresponding ones-ratio of about 0.609091 0.609091. Compare these predictions with the data in Table 1.

### 2.4 3 ​ x + 1 3x+1 Size Statistics: Maximum Excursion Values

Another interesting statistic is the maximum value attained in a trajectory, which we call the maximum excursion value.

###### Definition 2.6

The maximum excursion value t ⁡ ( n) t(n) is the maximum value occurring in the forward iteration of the integer n n, i.e.

 | t ( n):= max ( T ( k) ( n): k ≥ 0), t(n):=\max(T^{(k)}(n):~k\geq 0), |  | (2.18) |

with t ⁡ ( n) = + ∞ t(n)=+\infty if the trajectory is divergent.

The quantity t ⁡ ( n) t(n) will be finite for all n n if and only if there are no divergent trajectories for the 3 ​ x + 1 3x+1 problem (but does not exclude the possibility of as yet unknown loops).

We define the following extremal statistic for maximum excursions.

###### Definition 2.7

Let the 3 ​ x + 1 3x+1 maximum excursion ratio be given by

 | ρ ⁡ ( n):= log ⁡ t ⁡ ( n) log ⁡ n. \rho(n):={\log t(n)\over\log n}. |  | (2.19) |

Then the 3 ​ x + 1 3x+1 maximum excursion constant is the quantity

 | ρ:= lim sup n → ∞ ρ ⁡ ( n) = lim sup n → ∞ log ⁡ t ⁡ ( n) log ⁡ n. \rho:=\limsup_{n\to\infty}\rho(n)=\limsup_{n\to\infty}\frac{\log t(n)}{\log n}. |  | (2.20) |

k k | #k-th record ​ n k ∗ \mbox{\#k-th record}~n_{k}^{\ast} | t ⁡ ( n k ∗) t(n_{k}^{\ast}) | r ⁡ ( n k ∗) r(n_{k}^{\ast}) | ρ ⁡ ( n k ∗) \rho(n_{k}^{\ast}) |

1 | 2 | 2 | 0.500 | 1.000 |

2 | 3 | 8 | 0.889 | 1.893 |

3 | 7 | 26 | 0.531 | 1.674 |

4 | 15 | 80 | 0.356 | 1.618 |

5 | 27 | 4 616 | 6.332 | 2.560 |

6 | 255 | 6 560 | 0.101 | 1.586 |

7 | 447 | 19 682 | 0.099 | 1.620 |

8 | 639 | 20 782 | 0.051 | 1.539 |

9 | 703 | 125 252 | 0.253 | 1.792 |

10 | 1 819 | 638 468 | 0.193 | 1.781 |

11 | 4 255 | 3 405 068 | 0.188 | 1.800 |

12 | 4 591 | 4 076 810 | 0.193 | 1.805 |

13 | 9 663 | 13 557 212 | 0.145 | 1.790 |

14 | 20 895 | 25 071 632 | 0.057 | 1.712 |

15 | 26 623 | 53 179 010 | 0.075 | 1.746 |

16 | 31 911 | 60 506 432 | 0.059 | 1.728 |

17 | 60 975 | 296 639 576 | 0.080 | 1.771 |

18 | 77 671 | 785 412 368 | 0.130 | 1.819 |

19 | 113 383 | 1 241 055 674 | 0.097 | 1.799 |

20 | 138 367 | 1 399 161 680 | 0.073 | 1.779 |

21 | 159 487 | 8 601 188 876 | 0.338 | 1.861 |

22 | 270 271 | 12 324 038 948 | 0.169 | 1.858 |

23 | 665 215 | 26 241 642 656 | 0.059 | 1.789 |

24 | 704 511 | 28 495 741 760 | 0.057 | 1.788 |

25 | 1 042 431 | 45 119 577 824 | 0.042 | 1.770 |

Table 2: Seeds n n giving record heights for 3 ​ x + 1 3x+1 maximum excursion value t ⁡ ( n) t(n).[image: Refer to caption] Figure 2.1: A plot of n n versus the maximal excursion ratio ρ ⁡ ( n) \rho(n) for 3 ≤ n ≤ 1 042 431 3\leq n\leq 1\,042\,431 and odd, cf. ( 2.19). The only seeds n n in this range with ρ ⁡ ( n) > 2 \rho(n)>2 are n = 27, 31, 41, 47, 55, n=27,~31,~41,~47,~55, and 63 63 (which all look at this scale as if they are on the y y -axis).

n n | t ⁡ ( n) t(n) | r ⁡ ( n) r(n) | ρ ⁡ ( n) \rho(n) |

27 | 4 616 | 6.332 | 2.560 |

319 804 831 | 707 118 223 359 971 240 | 6.914 | 2.099 |

1 410 123 943 | 3 562 942 561 397 226 080 | 1.792 | 2.028 |

3 716 509 988 199 | 103 968 231 672 274 974 522 437 732 | 7.527 | 2.070 |

9 016 346 070 511 | 126 114 763 591 721 667 597 212 096 | 1.551 | 2.015 |

1 254 251 874 774 375 | 1 823 036 311 464 280 263 720 932 141 024 | 1.159 | 2.004 |

1 980 976 057 694 848 447 | 32 012 333 661 096 566 765 082 938 647 132 369 010 | 8.158 | 2.050 |

Table 3: Values of n n for which the maximal excursion ratio ρ ⁡ ( n) = log ⁡ t ⁡ ( n) log ⁡ n > 2 \rho(n)={\log t(n)\over\log n}>2 (equivalently, r ⁡ ( n) = t ⁡ ( n) / n 2 > 1 r(n)=t(n)/n^{2}>1), culled from Oliveira e Silva’s [31, Table 8] record t ⁡ ( n) t(n) values.

The maximal excursion constant will be + ∞ +\infty if there is a divergent trajectory. The fact that the logarithmic scaling used in defining this constant is the “correct” scaling is justified by empirical data given in Oliveira e Silva [31] (in this volume) and by the predictions of the stochastic model given in § 3. As explained in § 4.3, the stochastic model prediction for the maximum excursion constant is ρ = 2. \rho=2.

In Table 2 we give the set of initial champion values for the maximum excursion, extracted from data of Oliveira e Silva [30]. For comparison we give for each the ratio r ⁡ ( n):= t ⁡ ( n) n 2 r(n):=\frac{t(n)}{n^{2}} and the value of the maximal excursion ratio ρ ⁡ ( n) = log ⁡ t ⁡ ( n) log ⁡ n. \rho(n)={\log t(n)\over\log n}. It is also useful to examine the larger table to 10 18 10^{18} given in Oliveira e Silva [31].

While record values of t ⁡ ( n) t(n) have received tremendous computational attention, there has not been a substantial amount of effort put into congregating those n n with large ρ ⁡ ( n) \rho(n) (the difference being that the former seeks seeds n n with large values of t ⁡ ( n) t(n), whereas the latter seeks large values of t ⁡ ( n) t(n) relative to the size of n n). We have computed that the only seeds n < 10 6 n<10^{6} for which ρ ⁡ ( n) > 2 \rho(n)>2 are: n ∈ { 27, 31, 41, 47, 55, 63 } n\in\{27,31,41,47,55,63\}, cf. Figure 2.1.

Nevertheless, some “large” values of ρ ⁡ ( n) \rho(n) already appear in tables of large t ⁡ ( n) t(n) ’s. In Table 3 we extract from a table of t ⁡ ( n) t(n) champions computed by Oliveira e Silva [31] the subset of seeds n n for which ρ ⁡ ( n) > 2 \rho(n)>2, i.e.

 | r ⁡ ( n) = t ⁡ ( n) n 2 > 1. r(n)=\frac{t(n)}{n^{2}}>1. |  |

Only seven such values appear. This data seems to (however weakly) support Conjecture 4.2.

### 2.5 3 ​ x + 1 3x+1 Count Statistics: Inverse Iterate Counts

In considering backwards iteration of the 3 ​ x + 1 3x+1 function, we can ask: given an integer a a how many numbers n n have T ( k) ​ ( n) = a T^{(k)}(n)=a, that is, iterate forward to a a after exactly k k iterations?

The set of backwards iterates of a given number a a can be pictured as a tree; we call these 3 ​ x + 1 3x+1 trees and describe their structure in § 6. Here N k ​ ( a) N_{k}(a) counts the number of leaves at depth k k of a tree with root node a a, and N k ∗ ​ ( a) N_{k}^{\ast}(a) counts the number of leaves in a pruned 3 ​ x + 1 3x+1 tree, in which all nodes with label n ≡ 0 ( mod 3) n\equiv 0~(\bmod~3) have been removed. The definitions are as follows.

###### Definition 2.8

(1) Let N k ​ ( a) N_{k}(a) count the number of integers that forward iterate under the 3 ​ x + 1 3x+1 map T ⁡ ( n) T(n) to a a after exactly k k iterations, i.e.

 | N k ​ ( a):= | { n: T ( k) ​ ( n) = a } |. N_{k}(a):=|\{n:~T^{(k)}(n)=a\}|. |  | (2.21) |

(2) Let N k ∗ ​ ( a) N_{k}^{\ast}(a) count the number of integers not divisible by 3 3 that forward iterate under the 3 ​ x + 1 3x+1 map T ⁡ ( n) T(n) to a a after exactly k k iterations, i.e.

 | N k ∗ ( a):= | { n: T ( k) ( n) = a, n ≢ 0 ( mod 3) } |. N_{k}^{*}(a):=|\{n:~T^{(k)}(n)=a,~n\not\equiv 0(\bmod~3)\}|. |  | (2.22) |

The case a = 1 a=1 is of particular interest, since the quantities then count integers that iterate to 1 1. We set

 | N k:= N k ​ ( 1), N k ∗:= N k ∗ ​ ( 1). N_{k}:=N_{k}(1),~~~~~~~N_{k}^{\ast}:=N_{k}^{\ast}(1). |  |

The secondary quantity N k ∗ ​ ( a) N_{k}^{\ast}(a) is introduced because it is somewhat more convenient for analysis. It satisfies the monotonicity properties N k ∗ ​ ( a) ≤ N k + 1 ∗ ​ ( a) N_{k}^{\ast}(a)\leq N_{k+1}^{\ast}(a) and

 | N k ∗ ​ ( m) ≤ N k ​ ( a) ≤ ∑ j = 0 k N j ∗ ​ ( m) ≤ ( k + 1) ​ N k ∗ ​ ( a). N_{k}^{\ast}(m)\leq N_{k}(a)\leq\sum_{j=0}^{k}N_{j}^{\ast}(m)\leq(k+1)N_{k}^{\ast}(a). |  |

We have the trivial exponential upper bound

 | N k ​ ( a) ≤ 2 k. N_{k}(a)\leq 2^{k}. |  | (2.23) |

since each number has at most 2 2 preimages. We are interested in the exponential growth rate of N k ​ ( a) N_{k}(a).

###### Definition 2.9

(1) For a given a a the 3 ​ x + 1 3x+1 tree growth constant δ 3 ​ ( a) \delta_{3}(a) is given by

 | δ 3 ​ ( a):= lim sup k → ∞ 1 k ​ ( log ⁡ N k ​ ( a)). \delta_{3}(a):=\limsup_{k\to\infty}\frac{1}{k}\left(\log N_{k}(a)\right). |  | (2.24) |

(2) The 3 ​ x + 1 3x+1 universal tree growth constant is δ = δ 3 = δ 3 ​ ( 1). \delta=\delta_{3}=\delta_{3}(1).

The constant δ 3 ​ ( a) \delta_{3}(a) exists and is finite, as follows from the upper bound ( 2.23). It is easy to prove unconditionally that δ 3 ​ ( 3 ​ a) = 0, \delta_{3}(3a)=0, because the only preimages of a number 3 ​ a 3a are 2 k ​ 3 ​ a 2^{k}3a and N k ​ ( 3 ​ a) = 1 N_{k}(3a)=1 for all k ≥ 1 k\geq 1. The interesting case is when a ≢ 0 ( mod 3) a\not\equiv 0~(\bmod~3).

Applegate and Lagarias [2] determined by computer the maximal and minimal number of leaves in pruned 3 ​ x + 1 3x+1 trees of depth k k for k ≤ 30 k\leq 30. The maximal and minimal number of leaves in such trees at level k k is given by

 | N k +:= max { N k ∗ ( a): a ( mod 3 k + 1) with a ≢ 0 ( mod 3) } N_{k}^{+}:=\max\{N_{k}^{\ast}(a):~a~(\bmod~3^{k+1})~\mbox{with}~a\not\equiv 0~(\bmod~3)\} |  |

and

 | N k −:= min { N k ∗ ( a): a ( mod 3 k + 1) with a ≢ 0 ( mod 3) }, N_{k}^{-}:=\min\{N_{k}^{\ast}(a):~a~(\bmod~3^{k+1})~\mbox{with}~a\not\equiv 0~(\bmod~3)\}, |  |

respectively. Counts for the number of leaves in maximum and minimum size trees of various depths k k are given in the following table, taken from Applegate and Lagarias ( [2], [4]). It is known that the average number of leaves at depth k k (averaged over a a) is proportional to ( 4 3) k \left(\frac{4}{3}\right)^{k}, therefore in Table 4 below we include the value ( 4 3) k (\frac{4}{3})^{k} and the scaled statistics

 | D k ±:= N k ± ​ ( 4 3) − k. D_{k}^{\pm}:=N_{k}^{\pm}\left(\frac{4}{3}\right)^{-k}. |  |

This table also gives the number of distinct types of trees of each depth (there are some symmetries which speed up the calculation).

k k | # tree types \begin{array}[]{c}\mbox{\# tree types}\end{array} | N k − N_{k}^{-} | N k + N_{k}^{+} | ( 4 3) k \left(\frac{4}{3}\right)^{k} | D k − D_{k}^{-} | D k + D_{k}^{+} |

1 | 4 | 1 | 2 | 1.33 | 0.750 | 1.500 |

2 | 8 | 1 | 3 | 1.78 | 0.562 | 1.688 |

3 | 14 | 1 | 4 | 2.37 | 0.422 | 1.688 |

4 | 24 | 2 | 6 | 3.16 | 0.633 | 1.898 |

5 | 42 | 2 | 8 | 4.21 | 0.475 | 1.898 |

6 | 76 | 3 | 10 | 5.62 | 0.534 | 1.780 |

7 | 138 | 4 | 14 | 7.49 | 0.534 | 1.869 |

8 | 254 | 5 | 18 | 9.99 | 0.501 | 1.802 |

9 | 470 | 6 | 24 | 13.32 | 0.451 | 1.802 |

10 | 876 | 9 | 32 | 17.76 | 0.507 | 1.802 |

11 | 1638 | 11 | 42 | 23.68 | 0.465 | 1.774 |

12 | 3070 | 16 | 55 | 31.57 | 0.507 | 1.742 |

13 | 5766 | 20 | 74 | 42.09 | 0.475 | 1.758 |

14 | 10850 | 27 | 100 | 56.12 | 0.481 | 1.782 |

15 | 20436 | 36 | 134 | 74.83 | 0.481 | 1.791 |

16 | 38550 | 48 | 178 | 99.77 | 0.481 | 1.784 |

17 | 72806 | 64 | 237 | 133.03 | 0.481 | 1.782 |

18 | 137670 | 87 | 311 | 177.38 | 0.490 | 1.753 |

19 | 260612 | 114 | 413 | 236.50 | 0.482 | 1.746 |

20 | 493824 | 154 | 548 | 315.34 | 0.488 | 1.738 |

21 | 936690 | 206 | 736 | 420.45 | 0.490 | 1.751 |

22 | 1778360 | 274 | 988 | 560.60 | 0.489 | 1.762 |

23 | 3379372 | 363 | 1314 | 747.47 | 0.486 | 1.758 |

24 | 6427190 | 484 | 1744 | 996.62 | 0.486 | 1.750 |

25 | 12232928 | 649 | 2309 | 1328.83 | 0.488 | 1.738 |

26 | 23300652 | 868 | 3084 | 1771.77 | 0.490 | 1.741 |

27 | 44414366 | 1159 | 4130 | 2362.36 | 0.491 | 1.748 |

28 | 84713872 | 1549 | 5500 | 3149.81 | 0.492 | 1.746 |

29 | 161686324 | 2052 | 7336 | 4199.75 | 0.489 | 1.747 |

30 | 308780220 | 2747 | 9788 | 5599.67 | 0.491 | 1.748 |

Table 4: Normalized extreme values for 3 ​ x + 1 3x+1 trees of depth k k

Applegate and Lagarias [2, Theorem 1.1] proved the following result by an easy induction using this table.

###### Theorem 2.4

( 3 ​ x + 1 3x+1 Tree Sizes) For any fixed a ≢ 0 ( mod 3) a\not\equiv 0~(\bmod~3) and for all sufficiently large k k,

 | ( 1.302053) k ≤ N k ∗ ​ ( a) ≤ ( 1.358386) k. (1.302053)^{k}\leq N_{k}^{\ast}(a)\leq(1.358386)^{k}. |  | (2.25) |

In consequence, for any a ≢ 0 ( mod 3) a\not\equiv 0(\bmod~3),

 | log ⁡ ( 1.302053) ≤ δ 3 ​ ( a) ≤ log ⁡ ( 1.358386). \log(1.302053)\leq\delta_{3}(a)\leq\log(1.358386). |  | (2.26) |

We describe probabilistic models for 3 ​ x + 1 3x+1 inverse iterates in § 6. The models are Galton-Watson processes for the number of leaves in the tree, and branching random walks for the sizes of the labels in the tree. The model prediction is that δ 3 ​ ( a) = log ⁡ ( 4 3) \delta_{3}(a)=\log\left(\frac{4}{3}\right) for all a ≢ 0 ( mod 3) a\not\equiv 0~(\bmod~3).

### 2.6 3 ​ x + 1 3x+1 Count Statistics: Total Inverse Iterate Counts

In considering backwards iteration of the 3 ​ x + 1 3x+1 function from an integer a a, complete data is the set of integers that contain a a in their forward orbit. The 3 ​ x + 1 3x+1 problem concerns exactly this question for a = 1 a=1. The following function describes this set.

###### Definition 2.10

Given an integer a a, the inverse iterate counting function π a ​ ( x) \pi_{a}(x) counts the number of integers n n with | n | ≤ x |n|\leq x that contain a a in their forward orbit under the 3 ​ x + 1 3x+1 function. That is,

 | π a ​ ( x):= #⁡ { n: | n | ≤ x ​ and ​ T ( k) ​ ( n) = a ​ for some ​ k ≥ 0 }. \pi_{a}(x):=\#\{n:~|n|\leq x~~\mbox{and }~T^{(k)}(n)=a~~\mbox{for~some}~k\geq 0\}. |  | (2.27) |

It is possible to obtain rigorous lower bounds for this counting function. For a ≡ 0 ( mod 3) a\equiv 0~(\bmod~3) the set of inverse iterates is exactly { 2 k ​ a: k ≥ 0 } \{2^{k}a:~k\geq 0\} and π a ​ ( x) = ⌊ log 2 ⁡ ( 2 ​ x | a |) ⌋ \pi_{a}(x)=\lfloor\log_{2}(\frac{2x}{|a|})\rfloor grows logarithmically. If a ≢ 0 ( mod 3) a\not\equiv 0~(\bmod~3) then π a ​ ( x) \pi_{a}(x) satisfies a bound π a ​ ( x) > x c \pi_{a}(x)>x^{c} for some positive c c, as was first shown by Crandall [14] in 1978. The strongest method currently known to obtain lower bounds on π a ​ ( x) \pi_{a}(x) was initiated by Krasikov [19] in 1989, and extended in [3], [20]. It gives the following result.

###### Theorem 2.5

(Inverse Iterate Lower Bound) For each a ≢ 0 ( mod 3) a\not\equiv~0~(\bmod~3), there is a positive constant x 0 ​ ( a) x_{0}(a) such that for all x ≥ x 0 ​ ( a) x\geq x_{0}(a),

 | π a ​ ( x) ≥ x 0.84. \pi_{a}(x)\geq x^{0.84}. |  | (2.28) |

#### Proof.

This is proved in Krasikov and Lagarias [20]. The proof uses systems of difference inequalities ( mod 3 k) (\bmod~3^{k}), analyzed in Applegate and Lagarias [3], and by increasing k k one gets better exponents. The exponent above was obtained by computer calculation using k = 9 k=9.

The following statistics measure the size of the inverse iterate set in the sense of fractional dimension.

###### Definition 2.11

Given an integer a a, the upper and lower 3 ​ x + 1 3x+1 growth exponents for a a are given by

 | η 3 + ​ ( a):= lim sup x → ∞ log ⁡ π a ​ ( x) log ⁡ x, \eta_{3}^{+}(a):=\limsup_{x\to\infty}\frac{\log\pi_{a}(x)}{\log x}, |  |

and

 | η 3 − ​ ( a):= lim inf x → ∞ log ⁡ π a ​ ( x) log ⁡ x. \eta_{3}^{-}(a):=\liminf_{x\to\infty}\frac{\log\pi_{a}(x)}{\log x}. |  |

If these quantities are equal, we define the 3 ​ x + 1 3x+1 growth exponent η 3 ​ ( a) \eta_{3}(a) to be η 3 ​ ( a) = η 3 + ​ ( a) = η 3 − ​ ( a) \eta_{3}(a)=\eta_{3}^{+}(a)=\eta_{3}^{-}(a).

We clearly have η 3 ​ ( a) = 0 \eta_{3}(a)=0 if a ≡ 0 ( mod 3) a\equiv 0~~(\bmod~3). For the remaining values Applegate and Lagarias made the following conjecture.

###### Conjecture 2.1

( 3 ​ x + 1 3x+1 Growth Exponent Conjecture) For all integers a ≢ 0 ( mod 3) a\not\equiv 0~(\bmod~3), the 3 ​ x + 1 3x+1 growth exponent η 3 ​ ( a) \eta_{3}(a) exists, with

 | η 3 ​ ( a) = 1. \eta_{3}(a)=1. |  | (2.29) |

The truth of the 3 ​ x + 1 3x+1 Conjecture would imply that η 3 ​ ( 1) = 1 \eta_{3}(1)=1; however it does not seem to determine η 3 ​ ( a) \eta_{3}(a) for all such a a. Applegate and Lagarias [2, Conjecture A] made the stronger conjecture that for each a ≢ 0 ( mod 3) a\not\equiv 0~(\bmod~3) π a ​ ( x) \pi_{a}(x) grows linearly, i.e. there is a constant c a > 0 c_{a}>0 such that π a ​ ( x) > c a ​ x \pi_{a}(x)>c_{a}x holds for all x ≥ 1 x\geq 1.

Note that Theorem 2.5 shows that η 3 − ​ ( a) ≥ 0.84 \eta_{3}^{-}(a)\geq 0.84 when a ≢ 0 ( mod 3). a\not\equiv 0~(\bmod~3). Thus the lower bound in Conjecture 2.1 thus seems approachable. A stochastic model in § 6.5 makes the prediction that η 3 ​ ( a) = 1 \eta_{3}(a)=1.

## 3 3 ​ x + 1 3x+1 Forward Iteration: Random Product and Random Walk Models

In this section we formulate stochastic models intended to predict the behavior of iterations of the 3 ​ x + 1 3x+1 map T ⁡ ( n) T(n) on a “random” starting value n n. These models are exactly analyzable. We describe results obtained for these models, which can be viewed as predictions for the “average” behavior of the 3 ​ x + 1 3x+1 function.

### 3.1 Multiplicative Random Product Model and λ \lambda -stopping times

Recall that the λ \lambda -stopping time is defined (see ( 2.9)) by

 | σ λ ​ ( n):= inf { k ≥ 0: T ( k) ​ ( n) n < λ }. \sigma_{\lambda}(n):=\inf\{k\geq 0:\frac{T^{(k)}(n)}{n}<\lambda\}. |  |

Rawsthorne [32] and Borovkov and Pfeifer [10] obtained a probabilistic interpretation of the λ \lambda -stopping time, as follows. They consider a stochastic model which studies the random products

 | Y k:= X 1 X 2 ⋯ X k, Y_{k}:=X_{1}X_{2}\cdots X_{k}, |  |

in which the X i X_{i} are each independent identically distributed (i.i.d.) random variables X i X_{i} having the discrete distribution

 | X i = { 3 2 with probability ​ 1 2, 1 2 with probability ​ 1 2. X_{i}=\left\{\begin{array}[]{cl}\displaystyle\frac{3}{2}&\mbox{with~probability}~~\frac{1}{2},\\ \\ \displaystyle\frac{1}{2}&\mbox{with~probability}~~\frac{1}{2}.\\ \end{array}\right. |  |

We call this the 3 ​ x + 1 3x+1 multiplicative random product ( 3 ​ x + 1 3x+1 MRP) model.

This model does not include the choice of the starting value of the iteration, which would correspond to X 0 X_{0}; the random variable Y k Y_{k} really models the ratio T ( k) ​ ( X 0) X 0 \frac{T^{(k)}(X_{0})}{X_{0}}. They define for λ > 0 \lambda>0 the λ \lambda -stopping time random variable

 | V λ ​ ( ω):= inf { k: Y k ≤ λ }, V_{\lambda}(\omega):=\inf\{k:~Y_{k}\leq\lambda\}, |  | (3.30) |

where ω = ( X 1, X 2, X 3, …) \omega=(X_{1},X_{2},X_{3},\dots) denotes a sequence of random variables as above. This random vector ω \omega will model the effect of choosing a random starting value n = X 0 n=X_{0} in iteration of the 3 ​ x + 1 3x+1 map.

This stochastic model can be used to exactly describe the density of λ \lambda -stopping times, as follows. Let ℙ ⁡ [E] {{P}}[E] denote the probability of an event E E.

###### Theorem 3.1

( λ \lambda -Stopping Time Density Formula) For the 3 ​ x + 1 3x+1 function T ⁡ ( n) T(n) the natural density 𝔻 ​ ( S λ ​ ( k)) {{D}}(S_{\lambda}(k)) for integers having λ \lambda -stopping time at most k k is given exactly by the formula

 | 𝔻 ( S λ ( k)) = ℙ [V λ ( ω) ≤ k], {{D}}(S_{\lambda}(k))={{P}}[V_{\lambda}(\omega)\leq k], |  | (3.31) |

in which V λ V_{\lambda} is the λ \lambda -stopping time random variable in the 3 ​ x + 1 3x+1 multiplicative random product (MRP) model.

#### Proof.

In 1985 Rawsthorne [32, Theorem 1] proved a weaker version of this result, with 𝔻 ​ ( S λ ​ ( k)) {{D}}(S_{\lambda}(k)) replaced by the lower asymptotic density 𝔻 ¯ ​ ( S λ ​ ( k)) \underline{{{D}}}(S_{\lambda}(k)). The result, using natural density, is a special case of Borovkov and Pfeifer [10, Theorem 3].

It is natural to apply the 3 ​ x + 1 3x+1 MPR model with an initial condition added, which is a proxy for the expected behavior of the total stopping time. To do this we must allow variable λ \lambda (as a function of n n), in a range of parameters where there is no rigorous proof that the model behavior agrees with that of iteration of the map T ⁡ ( n) T(n), namely for λ = α ​ log ⁡ n \lambda=\alpha\log n with various α > 1 \alpha>1. What is missing is a result saying that it accurately matches the behavior of iteration of the 3 ​ x + 1 3x+1 map.

The behavior of the resulting probabilistic model is rigorously analyzable, as we discuss in the next subsection, cf. Theorem 3.2 below.

### 3.2 Additive Random Walk Model and Total Stopping Times

The 3 ​ x + 1 3x+1 iteration takes x 0 = n x_{0}=n and x k = T ( k) ​ ( n). x_{k}=T^{(k)}(n). In studying the iteration, it is often more convenient to use a logarithmic scale and set y k = log ⁡ x k y_{k}=\log x_{k} (natural logarithm) so that

 | y k = log ⁡ x k:= log ⁡ T ( k) ​ ( n). y_{k}=\log x_{k}:=\log T^{(k)}(n). |  |

Then we have

 | y k + 1 = { y k + log ⁡ 3 2 + e k if ​ x ≡ 1 ( mod 2), y k + log ⁡ 1 2 if ​ x ≡ 0 ( mod 2), y_{k+1}=\left\{\begin{array}[]{cl}y_{k}+\log\frac{3}{2}+e_{k}&\mbox{if}~x\equiv 1~~(\bmod~2)~,\\ \\ y_{k}+\log\frac{1}{2}&\mbox{if}~~x\equiv 0~~(\bmod~2)~,\end{array}\right. |  | (3.32) |

with

 | e k:= log ⁡ ( 1 + 1 3 ​ x k). e_{k}:=\log\left(1+\frac{1}{3x_{k}}\right). |  | (3.33) |

Here e k e_{k} is small as long as | x k | |x_{k}| is large.

Theorem 2.1 implies that if an integer is drawn at random from [1, 2 k] [1,2^{k}] then its k k -truncated parity sequence will be uniformly distributed in { 0, 1 } k \{0,1\}^{k}. In consequence, equations ( 3.32) and ( 3.33) show that the quantities log ⁡ T ( k) ​ ( n) \log T^{(k)}(n) (natural logarithm) can be modeled by a random walk starting at initial position y 0 = log ⁡ n y_{0}=\log n and taking steps of size log ⁡ 3 2 \log\frac{3}{2} if the parity value is odd, and log ⁡ 1 2 \log\frac{1}{2} if it is even.

The MRP model considered before is converted to an additive model by making a logarithmic change of variable, taking new random variables W k:= log ⁡ X k. W_{k}:=\log X_{k}. The additive model considers the random variables Z k Z_{k} which are a sum of random variables

 | Z k:= Z 0 + log ⁡ Y k = Z 0 + W 1 + W 2 + ⋯ + W k. Z_{k}:=Z_{0}+\log Y_{k}=Z_{0}+W_{1}+W_{2}+\cdots+W_{k}. |  |

Here Z 0 Z_{0} is a specified initial starting point, and Z k Z_{k} is the result of a (biased) random walk, taking steps of size either log ⁡ 3 2 \log\frac{3}{2} or log ⁡ 1 2 \log\frac{1}{2} with equal probability. In terms of these variables, the λ \lambda -stopping time random variable above is

 | V λ ​ ( ω) = inf { k: Z k − Z 0 ≤ log ⁡ λ }. V_{\lambda}(\omega)=\inf\{k:Z_{k}-Z_{0}\leq\log\lambda\}. |  |

We consider the approximation of this iteration process by the following stochastic model, which we term the 3 ​ x + 1 3x+1 Biased Random Walk Model ( 3 ​ x + 1 3x+1 BRW Model). For an integer n ≥ 1 n\geq 1 it separately makes a random walk which takes steps of size log ⁡ 1 2 \log\frac{1}{2} half the time and log ⁡ 3 2 \log\frac{3}{2} half the time. We can write such a random variable as

 | ξ k:= − log ⁡ 2 + δ k ​ log ⁡ 3, \xi_{k}:=-\log 2+\delta_{k}\log 3, |  |

in which δ k \delta_{k} are independent Bernoulli zero-one random variables. The random walk positions { Z k: k ≥ 0 }, \{Z_{k}:k\geq 0\}, are then random variables having starting value Z 0 = log ⁡ n Z_{0}=\log n, and with

 | Z k:= Z 0 + ξ 1 + ξ 2 + ⋯ + ξ k. Z_{k}:=Z_{0}+\xi_{1}+\xi_{2}+\cdots+\xi_{k}. |  |

The Z k Z_{k} define a biased random walk, whose expected drift μ \mu is given by

 | μ:= E [ξ k)] = − log 2 + 1 2 log 3 = 1 2 log ( 3 4) ≈ − 0.14384. \mu:=E[\xi_{k})]=-\log 2+\frac{1}{2}\log 3=\frac{1}{2}\log\left(\frac{3}{4}\right)\approx-0.14384. |  | (3.34) |

The variance σ \sigma of each step is given by

 | σ:= Var ⁡ [ξ k] = 1 2 ​ log ⁡ 3 ≈ 0.54930. \sigma:={\rm Var}[\xi_{k}]=\frac{1}{2}\log 3\approx 0.54930. |  |

In the addive model we associate to a random walk a total stopping time random variable

 | S ∞ ( n):= min { k > 0: Z k ≤ 0, given Z 0 = log n }, S_{\infty}(n):=\min\{k>0:Z_{k}\leq 0,~\mbox{given}~Z_{0}=\log n\}, |  |

which detects when the walk first crosses 0 0 (this corresponds in the multiplicative model to reaching 1 1). The expected number of steps to reach a nonpositive value starting from Z 0 = log ⁡ n Z_{0}=\log n is

 | E ⁡ [S ∞ ​ ( n)] = 1 | μ | ​ log ​ a = 1 1 2 ​ log ⁡ ( 4 3) ​ log ​ n ≈ 6.95212 ​ log ​ n. E[S_{\infty}(n)]=\frac{1}{|\mu|}\log a=\frac{1}{\frac{1}{2}\log(\frac{4}{3})}\log n\approx 6.95212\log n. |  |

As noted in § 2, Borovkov and Pfeifer [10] consider the multiplicative stochastic model obtained by exponentiation of the positions of the biased random walk above, from a given starting value X 0 = e n 0 X_{0}=e^{n_{0}}. They conclude the following result [10, Theorem 5].

###### Theorem 3.2

( 3 ​ X + 1 3X+1 BRW Gaussian Limit Distribution) In the Biased Random Walk Model, for each fixed n ≥ 2 n\geq 2 define the normalized random variable

 | Z ∞ ​ ( n):= S ∞ ​ ( n) − 1 μ ​ log ⁡ n μ − 3 2 ​ σ ​ log ⁡ n, Z_{\infty}(n):=\frac{S_{\infty}(n)-\frac{1}{\mu}\log n}{\mu^{-\frac{3}{2}}\sigma\sqrt{\log n}}, |  |

which has cumulative distribution function P n ( x):= Prob [Z ∞ ( n) < x] P_{n}(x):={\rm Prob}[Z_{\infty}(n)<x]. Here μ = | 1 2 ​ log ⁡ 3 4 | \mu=|\frac{1}{2}\log\frac{3}{4}|, and σ = 1 2 ​ log ⁡ 3 \sigma=\frac{1}{2}\log 3. Then for each fixed real x x, allowing n n to vary, one has

 | P n ( x):= Prob [Z ∞ ( n) < x] ⟶ Φ ( x), a s n → ∞, P_{n}(x):={\rm Prob}[Z_{\infty}(n)<x]\longrightarrow\Phi(x),~~~{as}~~n\to\infty, |  |

where Φ ⁡ ( x) = 1 2 ​ π ​ ∫ − ∞ x e − 1 2 ​ t 2 ​ 𝑑 t \Phi(x)=\frac{1}{\sqrt{2\pi}}\int_{-\infty}^{x}e^{-\frac{1}{2}t^{2}}dt is the cumulative distribution function of the standard normal distribution N ⁡ ( 0, 1) N(0,1).

Borovkov and Pfeifer note further that the rate of convergence of the normalized distribution P n ​ ( x) P_{n}(x) with fixed n n to the limiting normal distribution as n → ∞ n\to\infty is uniform in x x, but is quite slow. They assert that for all n ≥ 2 n\geq 2 and all − ∞ < x < ∞ -\infty<x<\infty,

 | | P n ​ ( x) − Φ ⁡ ( x) | = O ⁡ ( ( log ⁡ n) − 1 2), |P_{n}(x)-\Phi(x)|=O\left((\log n)^{-\frac{1}{2}}\right), |  | (3.35) |

where the implied constant in the O-symbol is absolute.

[image: Refer to caption] x 0 ∈ [0.95 × 10 6, 1.05 × 10 6)[image: Refer to caption] n = 10 6 {\includegraphics[width]{BPPic11.pdf}\atop x_{0}\ \in\ [0.95\times 10^{6},\ 1.05\times 10^{6})}\qquad{\includegraphics[width]{BPPic12.pdf}\atop n\ =\ 10^{6}}

[image: Refer to caption] x 0 ∈ [1.95 × 10 6, 2.05 × 10 6)[image: Refer to caption] n = 2 × 10 6 {\includegraphics[width]{BPPic21.pdf}\atop x_{0}\ \in\ [1.95\times 10^{6},\ 2.05\times 10^{6})}\qquad{\includegraphics[width]{BPPic22.pdf}\atop n\ =\ 2\times 10^{6}}

[image: Refer to caption] x 0 ∈ [3.5 × 10 6, 4.5 × 10 6)[image: Refer to caption] n = 4 × 10 6 {\includegraphics[width]{BPPic31.pdf}\atop x_{0}\ \in\ [3.5\times 10^{6},\ 4.5\times 10^{6})}\qquad{\includegraphics[width]{BPPic32.pdf}\atop n\ =\ 4\times 10^{6}}

Figure 3.2: Histograms for σ ∞ ​ ( x 0) / ln ⁡ x 0 \sigma_{\infty}(x_{0})/\ln x_{0} and its stochastic analog T ⁡ ( n) / ln ⁡ n T(n)/\ln n with fitted density. Taken from Borovkov-Pfeifer [10].

They also propose a better approximation to the distribution of the total stopping time of a random integer of size near n n, reflecting the fact that it is nonnegative random variable. They assert that the rescaled variable

 | Y ∞ ​ ( n):= S ∞ ​ ( n) log ⁡ n Y_{\infty}(n):=\frac{S_{\infty}(n)}{\log n} |  |

should have a good second order approximation given by the nonnegative random variable Y ~ ​ ( n) \tilde{Y}(n) having the distribution function

 | Ψ n ​ ( x) = C n ​ log ⁡ n σ ​ ∫ 0 x 1 2 ​ π ​ t 3 ​ e − ( μ ​ t − 1) 2 ​ log ⁡ n 2 ​ σ 2 ​ t ​ 𝑑 t, x > 0. \Psi_{n}(x)=C_{n}\frac{\sqrt{\log n}}{\sigma}\int_{0}^{x}\frac{1}{\sqrt{2\pi t^{3}}}e^{-\frac{(\mu t-1)^{2}\log n}{2\sigma^{2}t}}dt,~~x>0. |  |

in which C n C_{n} is a normalizing constant ( [10, eqn. (25)]).

They view the random variable S ∞ ​ ( n) S_{\infty}(n) as providing a model for the total stopping time σ ∞ ​ ( n) \sigma_{\infty}(n) of the 3 ​ x + 1 3x+1 function, where one compares the ensemble of values { σ ∞ ​ ( n): x ≤ n ≤ c 1 ​ x } \{\sigma_{\infty}(n):x\leq n\leq c_{1}x\} with c 1 > 1 c_{1}>1 fixed with independent samples of values S ∞ ​ ( n) S_{\infty}(n). The result above (with error term O ⁡ ( 1 log ⁡ n) O\left(\frac{1}{\sqrt{\log n}}\right)) predicts that for any ϵ > 0 \epsilon>0 the number of values that do not satisfy

 | ( 1 μ − 1 ( log ⁡ x) 1 2 − ϵ) ​ log ⁡ x ≤ σ ∞ ​ ( n) ≤ ( 1 μ + 1 ( log ⁡ x) 1 2 − ϵ) ​ log ⁡ x \left(\frac{1}{\mu}-\frac{1}{(\log x)^{\frac{1}{2}-\epsilon}}\right)\log x\leq\sigma_{\infty}(n)\leq\left(\frac{1}{\mu}+\frac{1}{(\log x)^{\frac{1}{2}-\epsilon}}\right)\log x |  |

is o ⁡ ( x) o(x), as x → ∞ x\to\infty. They compare the distribution of Y ~ ​ ( n) \tilde{Y}(n) with numerical data σ ∞ ​ ( n) log ⁡ n \frac{\sigma_{\infty}(n)}{\log n} for the 3 ​ x + 1 3x+1 function for n ≈ 10 6 n\approx 10^{6} and find fairly good agreement.

## 4 3 ​ x + 1 3x+1 Forward Iteration: Large Deviations and Extremal Trajectories

Lagarias and Weiss [23] formulated and studied stochastic models which are intended to give predictions for the extremal behavior of iteration of the 3 ​ x + 1 3x+1 map T ⁡ ( n) T(n).

### 4.1 3 ​ X + 1 3X+1 Repeated Random Walk Model

Lagarias and Weiss studied the following Repeated Random Walk Model ( 3 ​ x + 1 3x+1 RRW Model). For each integer n ≥ 1 n\geq 1, independently run a 3 ​ x + 1 3x+1 biased random walk model trial with starting value Z 0, n = log ⁡ n Z_{0,n}=\log n. That is, generate an infinite sequence of independent random walks { Z k, n: k ≥ 0 } \{Z_{k,n}:k\geq 0\}, with one walk generated for each value of n n. The model data is the countable set of random variables

 | ω:= { Z k, n: n ≥ 1, k ≥ 0 }, \omega:=\{Z_{k,n}:~n\geq 1,~k\geq 0\}, |  | (4.36) |

in which the initial starting points Z 0, n:= log ⁡ n Z_{0,n}:=\log n are deterministic, and all other random variables stochastic. From this data, one can form random variables that are functions of ω \omega, corresponding to the total stopping times and the maximum excursion values above.

The 3 ​ x + 1 3x+1 RRW model is exactly analyzable, and makes predictions for the value of the scaled stopping time constant, and for the maximum excursion constant. A subtlety of the RRW model is the fact that there are exponentially many trials with inputs of a given length j j, namely for those n n with e j ≤ n < e j + 1 e^{j}\leq n<e^{j+1}, which have initial condition j ≤ Z 0, n < j + 1 j\leq Z_{0,n}<j+1, so that the theory of large deviations becomes relevant to the analysis.

### 4.2 3 ​ x + 1 3x+1 RRW Model Prediction: Extremal Total Stopping Times

The 3 ​ x + 1 3x+1 RRW model can be used to produce statistics analogous to the scaled total stopping time γ ∞ ​ ( n) \gamma_{\infty}(n) and the 3 ​ x + 1 3x+1 scaled stopping time constant γ \gamma, cf. ( 2.15) and ( 2.16).

For a given trial ω \omega it yields an infinite sequence of total stopping time random variables

 | S ∞ ​ ( ω):= ( S ∞ ​ ( 1), S ∞ ​ ( 2), S ∞ ​ ( 3), …, S ∞ ​ ( n), …), S_{\infty}(\omega):=(S_{\infty}(1),S_{\infty}(2),S_{\infty}(3),\dots,S_{\infty}(n),\dots), |  |

where S ∞ ​ ( n) S_{\infty}(n) is computed using the individual random walk ℛ n {\cal R}_{n}. Thus we can compute the scaled statistics S ∞ ​ ( n) log ⁡ n \frac{S_{\infty}(n)}{\log n} for n ≥ 2 n\geq 2, and set

 | γ ⁡ ( ω):= lim sup n → ∞ S ∞ ​ ( n) log ⁡ n. \gamma(\omega):=\limsup_{n\to\infty}\frac{S_{\infty}(n)}{\log n}. |  |

as a stochastic analogue of the quantity γ \gamma.

The 3 ​ x + 1 3x+1 RRW model has the following asymptotic limiting behavior for this statistic, given by Lagarias and Weiss [23, Theorem 2.1].

###### Theorem 4.1

( 3 ​ x + 1 3x+1 RRW Scaled Stopping Time Constant) For the 3 ​ x + 1 3x+1 RRW model, with probability one the scaled stopping time

 | γ ⁡ ( ω):= lim sup n → ∞ S ∞ ​ ( n) log ⁡ n \gamma(\omega):=\limsup_{n\to\infty}\frac{S_{\infty}(n)}{\log n} |  |

is finite and equals a constant

 | γ R ​ R ​ W ≈ 41.677647, \gamma_{RRW}\approx 41.677647, |  |

which is the unique real number γ > ( 1 2 ​ log ⁡ 4 3) − 1 ≈ 6.952 \gamma>\left(\frac{1}{2}\log\frac{4}{3}\right)^{-1}\approx 6.952 of the fixed point equation

 | γ ​ g ​ ( 1 γ) = 1. \gamma~g\left(\frac{1}{\gamma}\right)=1. |  | (4.37) |

Here the rate function g ⁡ ( a) g(a) is given by

 | g ⁡ ( a):= sup θ ∈ ℝ ( θ ​ a − log ⁡ M R ​ R ​ W ​ ( θ)), g(a):=\sup_{\theta\in{{R}}}\left(\theta a-\log M_{RRW}(\theta)\right), |  | (4.38) |

in which

 | M R ​ R ​ W ​ ( θ):= 1 2 ​ ( 2 θ + ( 2 3) θ) M_{RRW}(\theta):=\frac{1}{2}\left(2^{\theta}+\left(\frac{2}{3}\right)^{\theta}\right) |  | (4.39) |

is a moment generating function associated to the random walk.

Lagarias and Weiss also obtain a density result on the number of n n getting values close to the extremal constant, as follows ( [23, Theorem 2.2]).

###### Theorem 4.2

( 3 ​ x + 1 3x+1 RRW Scaled Stopping Time Distribution) For the 3 ​ x + 1 3x+1 RRW model, and for any constant α \alpha satisfying

 | ( 1 2 ​ log ⁡ 4 3) − 1 < α < γ R ​ R ​ W, \left(\frac{1}{2}\log\frac{4}{3}\right)^{-1}<\alpha<\gamma_{RRW}, |  | (4.40) |

one has the bound

 | E ⁡ [| { n ≤ x: S ∞ ​ ( n) log ⁡ n ≥ α } |] ≤ ( 1 − α ​ g ​ ( 1 α)) − 1 ​ x 1 − α ​ g ​ ( 1 / α). E\left[|\{n\leq x:~\frac{S_{\infty}(n)}{\log n}\geq\alpha\}|\right]\leq\left(1-\alpha~g\left(\frac{1}{\alpha}\right)\right)^{-1}x^{1-\alpha g(1/\alpha)}. |  | (4.41) |

In the reverse direction, for any ϵ > 0 \epsilon>0 this expected value satisfies

 | E ⁡ [| { n ≤ x: S ∞ ​ ( n) log ⁡ n ≥ α } |] ≥ x 1 − α ​ g ​ ( 1 / α) − ϵ E\left[|\{n\leq x:~\frac{S_{\infty}(n)}{\log n}\geq\alpha\}|\right]\geq x^{1-\alpha g(1/\alpha)-\epsilon} |  | (4.42) |

for all sufficiently large x ≥ x 0 ​ ( ϵ). x\geq x_{0}(\epsilon).

This theorem says that not only is there an upper bound γ R ​ R ​ W \gamma_{RRW} on the asymptotic limiting value of the stopping ratio, but the set of n n for which one gets a value above α \alpha becomes very sparse (in the logarithmic sense) as α \alpha approaches γ R ​ R ​ W \gamma_{RRW} from below. Theorem 4.2 is analogous to obtaining a multifractal spectrum for this problem. This result is well-suited for comparison with experimental data on 3 ​ x + 1 3x+1 iterates.

This analysis suggest the following prediction, which we state as a conjecture.

###### Conjecture 4.1

( 3 ​ x + 1 3x+1 Scaled Stopping Constant Conjecture) The 3 ​ x + 1 3x+1 scaled stopping constant γ \gamma is finite and is given by

 | γ = γ R ​ R ​ W ≈ 41.677647. \gamma=\gamma_{RRW}\approx 41.677647. |  | (4.43) |

The large deviations model does more than predict an extremal value, it also predicts that the numbers that approach the extremal value must have a trajectory of iterates whose graph have a specified shape, which is a linear function when properly scaled. In Figure 4.3 we graph the set of scaled points

 | { ( k log ⁡ n, log ⁡ T ( k) ​ ( n) log ⁡ n): 0 ≤ k ≤ σ ∞ ​ ( n) }. \left\{\left(\frac{k}{\log n},\frac{\log T^{(k)}(n)}{\log n}\right):0\leq k\leq\sigma_{\infty}(n)\right\}. |  |

The predicted large deviations extremal trajectory in this scaling has graph a straight line connecting the points ( 0, 1) (0,1) and ( γ R ​ R ​ W, 0) (\gamma_{RRW},0). Figure 4.3 shows the scaled trajectories with starting seeds n k n_{k} taken from Table 1, i.e. those with record values for γ ∞ ​ ( n) \gamma_{\infty}(n). Compare to Lagarias and Weiss [23, Figure 3].

Figure 4.3: Scaled trajectories of n k n_{k} maximizing γ ⁡ ( n) \gamma(n) for record values from Table 1 (thin for 1 ≤ k ≤ 10 1\leq k\leq 10; regular for 11 ≤ k ≤ 15 11\leq k\leq 15; thick for 16 ≤ k ≤ 19 16\leq k\leq 19), plotted against the predicted trajectory.

### 4.3 3 ​ x + 1 3x+1 RRW Model Prediction: Maximum Excursion Constant

For the 3 ​ x + 1 3x+1 RRW Stochastic Model, an appropriate statistic for a single trial that corresponds to the maximum excursion value is

 | t ( n; ω):= sup ( e Z k, n: k ≥ 0). t(n;\omega):=\sup(e^{Z_{k,n}}:k\geq 0). |  |

The 3 ​ x + 1 3x+1 RRW model behavior for extremal behavior of maximum excursions t ⁡ ( n, ω) t(n;\omega) is given in the following result [23, Theorem 2.3].

###### Theorem 4.3

( 3 ​ x + 1 3x+1 RRW Maximum Excursion Constant) For the 3 ​ x + 1 3x+1 RRW model, with probability one the quantities t ⁡ ( n, ω) t(n,\omega) are finite for every n ≥ 1 n\geq 1. In addition, with probability one the random quantity

 | ρ ⁡ ( ω):= lim sup n → ∞ log ⁡ t ⁡ ( n, ω) log ⁡ n = lim sup n → ∞ ( sup k ≥ 0 Z k, n log ⁡ n) \rho(\omega):=\limsup_{n\to\infty}\frac{\log t(n;\omega)}{\log n}=\limsup_{n\to\infty}\left(\sup_{k\geq 0}\frac{Z_{k,n}}{\log n}\right) |  | (4.44) |

equals the constant

 | ρ R ​ R ​ W = 2. \rho_{RRW}=2. |  | (4.45) |

Lagarias and Weiss also prove [23, Theorem 2.4] a result permitting a quantitative comparison with data.

###### Theorem 4.4

( 3 ​ x + 1 3x+1 RRW Maximum Excursion Density Function) For the 3 ​ x + 1 3x+1 RRW model, for any fixed 0 < α < 1 0<\alpha<1, the expected value

 | E ⁡ [| { n ≤ x: log ⁡ t ⁡ ( n, ω) log ⁡ n ≥ 2 − α } |] = x α ⁡ ( 1 − o ⁡ ( 1)), E\left[|\{n\leq x:~\frac{\log t(n;\omega)}{\log n}\geq 2-\alpha\}|\right]=x^{\alpha(1-o(1))}, |  | (4.46) |

as x → ∞ x\to\infty.

These theorems suggest formulating the following conjecture.

###### Conjecture 4.2

The 3 ​ x + 1 3x+1 maximum excursion constant ρ \rho defined in ( 2.20) is finite and is given by

 | ρ = 2. \rho=2. |  | (4.47) |

The large deviations model also makes a prediction on the graphs of the trajectories achieving maximum excursion, when plotted as the scaled data points

 | { ( k log ⁡ n, log ⁡ T ( k) ​ ( n) log ⁡ n): 0 ≤ k ≤ σ ∞ ​ ( n) }. \left\{\left(\frac{k}{\log n},{\log T^{(k)}(n)\over\log n}\right):~0\leq k\leq\sigma_{\infty}(n)\right\}. |  |

It asserts that extremal large deviation trajectories should approximate two line segments, the first with vertices ( 0, 1) (0,1) to ( 7.645, 2) (7.645,2) and then from this vertex to ( 21.55, 0). (21.55,0). The slope of the first line segment is 3 4 ​ log ⁡ 3 − log ⁡ 2 ≈ 0.1308 \frac{3}{4}\log 3-\log 2\approx 0.1308 and that of the second line segment is ( 1 2 ​ log ⁡ 3 4) − 1 ≈ − 0.1453 (\frac{1}{2}\log\frac{3}{4})^{-1}\approx-0.1453. This prediction is shown as a dotted black line in Figure 4.4; it shows substantial agreement with the empirical evidence.

Figure 4.4: Scaled trajectories of seeds n n from Table 3, plotted against the predicted trajectory. The trajectory of n = 27 n=27 is thin, while the others are thick.

### 4.4 3 ​ x + 1 3x+1 RRW Model: Critique

The 3 ​ x + 1 3x+1 repeated random walk model has the feature that random walks for different n n are independent. However the actual 3 ​ x + 1 3x+1 map certainly has a great deal of dependency built in, due to the fact that trajectories coalesce under forward iteration. For example, trajectories of numbers 8 ​ n + 4 8n+4 and 8 ​ n + 5 8n+5 always coalesce after 3 3 iterations of T T. After coalescence, the trajectories are completely correlated. In fact, the 3 ​ x + 1 3x+1 Conjecture predicts that all trajectories of positive integers n n reach the orbit { 1, 2 } \{1,2\} and then cycle, whence they all should coalesce into exactly two classes, namely those that reach 1 1 in an odd number of iterations of T T, and those that reach this orbit under an even number of iterations.

For this reason, it is not apparent a priori whether the prediction in Conjecture 4.1 above of the constant γ = γ R ​ R ​ W \gamma=\gamma_{RRW} is reasonable. Our faith in Conjecture 4.1 relies on the fact that first, the same prediction is made using a branching random walk model that incorporates dependency in the model, see Theorem 6.4 in § 6, and second, on comparison with empirical data in Table 1.

## 5 3 ​ x + 1 3x+1 Accelerated Forward Iteration : Brownian Motion

Now we consider the accelerated 3 ​ x + 1 3x+1 function U U. Recall that U U is defined on odd integers, and removes all powers of 2 2 in one fell swoop. Iterates of the accelerated function U U are of course equivalent (from the point of view of the main conjecture) to those of T T, but there are some subtle differences which make studying both points of view appealing.

For an odd integer n n, we let 𝔬 ⁡ ( n) {o}(n) count the number of powers of 2 2 dividing 3 ​ n + 1 3n+1, so that

 | 𝔬 ⁡ ( n):= ord 2 ​ ( 3 ​ n + 1). {o}(n):={\rm ord}_{2}(3n+1). |  | (5.48) |

Then the accelerated 3 ​ x + 1 3x+1 function U U is given by:

 | U ⁡ ( n):= 3 ​ n + 1 2 𝔬 ⁡ ( n). U(n):={3n+1\over 2^{{o}(n)}}. |  | (5.49) |

In analogy with the (truncated) parity sequence, cf. Definition 2.1, we make the following definition, giving a symbolic dynamics for the accelerated 3 ​ x + 1 3x+1 map.

###### Definition 5.1

(i) For an odd integer n n, define the 𝔬 {o} -sequence of n n to be

 | V ⁡ ( n):= ( 𝔬 1 ​ ( n), 𝔬 2 ​ ( n), 𝔬 3 ​ ( n), …) V(n):=({o}_{1}(n),{o}_{2}(n),{o}_{3}(n),\dots) |  | (5.50) |

where

 | 𝔬 k ​ ( n):= 𝔬 ⁡ ( U ( k) ​ ( n)), {o}_{k}(n):={o}(U^{(k)}(n)), |  |

and U ( k) ​ ( n) U^{(k)}(n) denotes the k k -th iterate of U U, as usual. This is an infinite vector of positive integers.

(ii) For k ≥ 1 k\geq 1 the k k -truncated 𝔬 {o} -sequence of n n is:

 | V [k] ​ ( n):= ( 𝔬 1 ​ ( n), 𝔬 2 ​ ( n), …, 𝔬 k ​ ( n)) V^{[k]}(n):=({o}_{1}(n),{o}_{2}(n),\dots,{o}_{k}(n)) |  | (5.51) |

i.e. a vector giving the initial segment of k k terms of V ⁡ ( n) V(n).

###### Definition 5.2

For an odd integer n n and k ≥ 1 k\geq 1, let the k k -size 𝔰 k ​ ( n) {s}_{k}(n) be the sum of the entries in V [k] ​ ( n) V^{[k]}(n), that is

 | 𝔰 k ​ ( n):= 𝔬 1 ​ ( n) + 𝔬 2 ​ ( n) + ⋯ + 𝔬 k ​ ( n). {s}_{k}(n):={o}_{1}(n)+{o}_{2}(n)+\cdots+{o}_{k}(n). |  |

### 5.1 The Structure Theorem

Notice that U ⁡ ( n) U(n) is not only odd, but is also relatively prime to 3 3. Hence we lose no generality by restricting the domain for U U from ℤ {{Z}} to the (more natural) set Π \Pi of positive integers prime to 2 2 and 3 3, i.e.

 | Π:= { n ∈ ℤ: gcd ⁡ ( n, 6) = 1 }. \Pi:=\{n\in{{Z}}:\gcd(n,6)=1\}. |  | (5.52) |

Moreover, Π \Pi is the disjoint union of Π ( 1) \Pi^{(1)} and Π ( 5) \Pi^{(5)}, where Π ( ε) \Pi^{(\varepsilon)} consists of positive integers congruent to ε ( mod 6) \varepsilon~(\bmod~6), ε = 1 \varepsilon=1 or 5 5.

###### Definition 5.3

Given ε = 1 \varepsilon=1 or 5 5, k ≥ 1 k\geq 1, and a vector ( 𝔬 1, …, 𝔬 k) ({o}_{1},\dots,{o}_{k}) of positive integers, let

 | Σ ( ε) ​ ( 𝔬 1, …, 𝔬 k) \Sigma^{(\varepsilon)}({o}_{1},\dots,{o}_{k}) |  |

be the set of all n ∈ Π ( ε) n\in\Pi^{(\varepsilon)} with V [k] ​ ( n) = ( 𝔬 1, …, 𝔬 k) V^{[k]}(n)=({o}_{1},\dots,{o}_{k}).

The result analogous to Theorem 2.1 is given by Sinai [35] and Kontorovich-Sinai [18].

###### Theorem 5.1

(Structure Theorem for 𝔬 {o} Symbolic Dynamics) Fix ε = 1 \varepsilon=1 or 5 5, and let n ∈ Π ( ε) n\in\Pi^{(\varepsilon)}.

(i) The k k -truncated 𝔬 {o} -sequence V [k] ​ ( n) V^{[k]}(n) of the first k k iterates of the accelerated map U ⁡ ( n) U(n) is periodic in n n. Its period is 6 ⋅ 2 𝔰 6\cdot 2^{{s}}, where

 | 𝔰 = 𝔰 k ​ ( n) = 𝔬 1 ​ ( n) + 𝔬 2 ​ ( n) + ⋯ + 𝔬 k ​ ( n). {s}={s}_{k}(n)={o}_{1}(n)+{o}_{2}(n)+\cdots+{o}_{k}(n). |  |

(ii) For any k ≥ 1 k\geq 1 and 𝔰 ≥ k {s}\geq k, each of the ( 𝔰 − 1 k − 1) \left({{s}-1\atop k-1}\right) possible vectors ( 𝔬 1, ⋯, 𝔬 k) ({o}_{1},\cdots,{o}_{k}) with 𝔬 j ≥ 1 {o}_{j}\geq 1 and 𝔬 1 + ⋯ + 𝔬 k = 𝔰 {o}_{1}+\cdots+{o}_{k}={s} occurs exactly once as V [k] ​ ( n) V^{[k]}(n) for some n ∈ Π ( ε) n\in\Pi^{(\varepsilon)} in the initial segment 1 ≤ n < 6 ⋅ 2 𝔰 1\leq n<6\cdot 2^{{s}}.

(iii) The least element n 0 ∈ Σ ( ε) ​ ( 𝔬 1, …, 𝔬 k) n_{0}\in\Sigma^{(\varepsilon)}({o}_{1},\dots,{o}_{k}) satisfies n 0 < 6 ⋅ 2 𝔰 n_{0}<6\cdot 2^{{s}}; moreover

 | Σ ( ε) ​ ( 𝔬 1, …, 𝔬 k) = { 6 ⋅ 2 𝔰 ⋅ m + n 0 } m = 0 ∞. \Sigma^{(\varepsilon)}({o}_{1},\dots,{o}_{k})=\bigg\{6\cdot 2^{{s}}\cdot m+n_{0}\bigg\}_{m=0}^{\infty}. |  |

#### Proof.

This is proved as part one of the Structure Theorem in Kontorovich-Sinai [18]. Here (iii) follows immediately from (i) and (ii).

Again one easily shows that an integer n n is uniquely determined by the 𝔬 {o} -sequence V ⁡ ( n) V(n) of its forward U U -orbit.

Moreover, the following result shows that the image under the iterated map U ( k) U^{(k)} of n ∈ Σ ( ε) ​ ( 𝔬 1, …, 𝔬 k) n\in\Sigma^{(\varepsilon)}({o}_{1},\dots,{o}_{k}) is also a nice arithmetic progression!

###### Theorem 5.2

(Iterated Structure Theorem) Fix ε = 1 \varepsilon=1 or 5 5, k ≥ 1 k\geq 1, a vector ( 𝔬 1, ⋯, 𝔬 k) ({o}_{1},\cdots,{o}_{k}), and let 𝔰 = 𝔬 1 + ⋯ + 𝔬 k {s}={o}_{1}+\cdots+{o}_{k}. Suppose 1 ≤ n 0 < 6 ⋅ 2 𝔰 1\leq n_{0}<6\cdot 2^{{s}} is the least element of Σ ( ε) ​ ( 𝔬 1, …, 𝔬 k) \Sigma^{(\varepsilon)}({o}_{1},\dots,{o}_{k}). Then there is a δ k = 1 \delta_{k}=1 or 5 5 and an r k ∈ { 0, 1, 2, …, 3 k − 1 } r_{k}\in\{0,1,2,\dots,3^{k}-1\}, both depending only on ε \varepsilon and ( 𝔬 1, …, 𝔬 k) ({o}_{1},\dots,{o}_{k}), such that, for each positive integer m m,

 | U ( k) ​ ( 6 ⋅ 2 𝔰 ⋅ m + n 0) = 6 ​ ( 3 k ⋅ m + r k) + δ k. U^{(k)}(6\cdot 2^{{s}}\cdot m+n_{0})=6(3^{k}\cdot m+r_{k})+\delta_{k}. |  | (5.53) |

Moreover, δ k \delta_{k} is determined by the congruence

 | δ k ≡ 2 𝔬 k ( mod 3). \delta_{k}\equiv 2^{{o}_{k}}(\bmod~3). |  | (5.54) |

#### Proof.

This is part two of the Structure Theorem in Kontorovich-Sinai [18]. Note that m m is the same number on both sides of ( 5.53); this equation says that an arithmetic progression with common difference 6 ⋅ 2 𝔰 6\cdot 2^{{s}} mapped under U ( k) U^{(k)} to one with common difference 6 ⋅ 3 k 6\cdot 3^{k}.

### 5.2 Probability Densities

We first tweak the notion of natural density defined in ( 2.12) on subsets of the natural numbers, by restricting to just elements of our domain Π \Pi. For a subset Σ ⊂ Π \Sigma\subset\Pi, let the Π \Pi -natural density be

 | 𝔻 Π ( Σ):= lim t → ∞ 3 t | { n ∈ Σ: n ≤ t } | = lim t → ∞ | { n ∈ Σ: n ≤ t } | | { n ∈ Π: n ≤ t } |, {{D}}_{\Pi}(\Sigma):=\lim_{t\to\infty}\frac{3}{t}\left|\bigg\{n\in\Sigma:n\leq t\bigg\}\right|=\lim_{t\to\infty}{\left|\bigg\{n\in\Sigma:n\leq t\bigg\}\right|\over\left|\bigg\{n\in\Pi:n\leq t\bigg\}\right|}, |  |

provided that the limit exists. (The factor 3 3 appears because Π \Pi contains two residue classes modulo 6 6.)

For a vector ( 𝔬 1, …, 𝔬 k) ({o}_{1},\dots,{o}_{k}), let

 | Σ ⁡ ( 𝔬 1, …, 𝔬 k):= Σ ( 1) ​ ( 𝔬 1, …, 𝔬 k) ∪ Σ ( 5) ​ ( 𝔬 1, …, 𝔬 k). \Sigma({o}_{1},\dots,{o}_{k}):=\Sigma^{(1)}({o}_{1},\dots,{o}_{k})\ \cup\ \Sigma^{(5)}({o}_{1},\dots,{o}_{k}). |  |

Recall that a random variable X X is geometrically distributed with parameter 0 < ρ < 1 0<\rho<1 if

 | ℙ [X = m] = ρ m − 1 ( 1 − ρ) for m = 1, 2, 3, … {{P}}[X=m]=\rho^{m-1}(1-\rho)\qquad\qquad\mbox{ for $m=1,2,3,\dots$ } |  |

###### Theorem 5.3

(Geometric Distribution)

(1) The sets Σ ⁡ ( 𝔬 1, …, 𝔬 k) \Sigma({o}_{1},\dots,{o}_{k}) have a Π \Pi -natural density given by

 | 𝔻 Π ( Σ ( 𝔬 1, …, 𝔬 k)) = 2 − 𝔰 = 2 − 𝔬 1 ⋅ 2 − 𝔬 2 ⋯ 2 − 𝔬 k. {{D}}_{\Pi}\left(\Sigma({o}_{1},\dots,{o}_{k})\right)=2^{-{s}}=2^{-{o}_{1}}\cdot 2^{-{o}_{2}}\cdots 2^{-{o}_{k}}. |  | (5.55) |

(2) This natural density matches the probability density of the distribution for independent geometrically distributed random variables ( 𝔭 1, …, 𝔭 k) ({p}_{1},...,{p}_{k}) with parameter ρ = 1 2 \rho=\frac{1}{2}, which have

 | μ 𝔬:= 𝔼 ⁡ [𝔭 j] = 2, and σ 𝔬:= V ​ a ​ r ​ [𝔭 j] = 2. \mu_{{o}}:={{E}}[{p}_{j}]=2,\qquad\mbox{ and }\qquad\sigma_{{o}}:=Var[{p}_{j}]=2. |  |

That is,

 | ℙ ⁡ [( 𝔭 1 = 𝔬 1, …, 𝔭 k = 𝔬 k)] = 𝔻 Π ​ ( Σ ⁡ ( 𝔬 1, …, 𝔬 k)). {{P}}[({p}_{1}={o}_{1},\dots,{p}_{k}={o}_{k})]={{D}}_{\Pi}\left(\Sigma({o}_{1},\dots,{o}_{k})\right). |  | (5.56) |

#### Proof.

(1) The existence of a natural density is automatic, since these sets are finite unions of arithmetic progressions. For ε = 1 \varepsilon=1 or 5 5, we easily compute from Theorem 5.1 that

 | 𝔻 Π ​ ( Σ ( ε) ​ ( 𝔬 1, …, 𝔬 k)) = 3 ⋅ 1 6 ⋅ 2 𝔬 1 + ⋯ + 𝔬 k = 1 2 ⋅ 2 − 𝔰, {{D}}_{\Pi}\left(\Sigma^{(\varepsilon)}({o}_{1},\dots,{o}_{k})\right)=3\cdot\frac{1}{6\cdot 2^{{o}_{1}+\cdots+{o}_{k}}}=\frac{1}{2}\cdot 2^{-{s}}, |  |

and hence ( 5.55) follows.

(2) The identity ( 5.56) is immediate from independence and ( 5.55).

We now deduce the following result.

###### Theorem 5.4

(Central Limit Theorem) For the accelerated 3 ​ x + 1 3x+1 map U U, with symbolic iterates ( 𝔬 1, 𝔬 2, …) ({o}_{1},{o}_{2},\dots), the scaled ordinates satisfy

 | lim k → ∞ 𝔻 Π [n: 𝔬 1 ​ ( n) + ⋯ + 𝔬 k ​ ( n) − μ 𝔬 ​ k σ 𝔬 ​ k < a] = 1 2 ​ π ∫ − ∞ a e − u 2 / 2 d u. \lim_{k\to\infty}{{D}}_{\Pi}\left[n:{{o}_{1}(n)+\cdots+{o}_{k}(n)-\mu_{{o}}k\over\sqrt{\sigma_{{o}}k}}<a\right]={1\over\sqrt{2\pi}}\int_{-\infty}^{a}e^{-u^{2}/2}du. |  |

#### Proof.

This follows immediately from the argument above and the Central Limit Theorem for geometrically distributed random variables.

Compare the above to Theorem 3.2. The rate of convergence is again quite slow (this feature is shared by Borovkov-Pfeifer; see ( 3.35)).

### 5.3 Brownian Motion

Consider some starting value x 0 = n ∈ Π x_{0}=n\in\Pi, denote its iterates by x k:= U ( k) ​ ( x 0) x_{k}:=U^{(k)}(x_{0}), and take logarithms y k:= log ⁡ x k y_{k}:=\log x_{k}. As in ( 3.32), the multiplicative behavior of U U is converted via logarithms to an additive behavior. Normalize the above by

 | ω k:= y k − y 0 − k ​ log ⁡ ( 3 4) 2 ​ k ​ log ⁡ 2. \omega_{k}:={y_{k}-y_{0}-k\log(\frac{3}{4})\over\sqrt{2k}\log 2}. |  | (5.57) |

Then we have the following scaling limits for “random” accelerated trajectories, chosen in the sense of density.

###### Theorem 5.5

(Geometric Brownian Motion Increments) Fix a partition of the interval [0, 1] [0,1] as 0 = t 0 < t 1 < ⋯ < t r = 1 0=t_{0}<t_{1}<\cdots<t_{r}=1. Given an integer k k, set k j = ⌊ t j ​ k ⌋ k_{j}=\lfloor t_{j}k\rfloor, with j = 1, …, r j=1,\dots,r. Then for any a j < b j a_{j}<b_{j},

 | 𝔻 Π [x 0: a j < ω k j − ω k j − 1 < b j, for all j = 1, 2, …, r] → ∏ j = 1 r ( Φ ( b j) − Φ ( a j)), {{D}}_{\Pi}\left[x_{0}:a_{j}<{\omega_{k_{j}}-\omega_{k_{j-1}}}<b_{j},\mbox{ for all }j=1,2,\dots,r\right]\quad\to\quad\prod_{j=1}^{r}\bigg(\Phi(b_{j})-\Phi(a_{j})\bigg), |  |

as k → ∞ k\to\infty, where recall that Φ ⁡ ( a) \Phi(a) is the cumulative distribution function for the standard normal distribution:

 | Φ ( a) = 1 2 ​ π ∫ − ∞ a e − u 2 / 2 d u. \Phi(a)={1\over\sqrt{2\pi}}\int_{-\infty}^{a}e^{-u^{2}/2}du. |  |

#### Proof.

This appears as Theorem 5 in Kontorovich-Sinai [18]. See Figure 5.5.

Figure 5.5: A sample path of the 3 ​ x + 1 3x+1 map. Here we took the starting value x 0 = 123 456 789 135 791 113 151 719 x_{0}=123\,456\,789\,135\,791\,113\,151\,719, computed 150 150 iterates of U U, and plotted ω k \omega_{k}.

The interpretation of the above result is that the paths of the accelerated 3 ​ x + 1 3x+1 map, when properly scaled, approach those of a geometric Brownian motion, that is, a stochastic process whose logarithm is a Brownian motion, or a Weiner process.

#### Remark.

There are in fact two limits taken in the above theorem, whose order is highly non-interchangeable! The first limit is hidden inside the definition of density, that is, first we take the limit as x → ∞ x\to\infty of the set of all x 0 < x x_{0}<x satisfying the given condition with the number k k of iterates of U U fixed, and only then do we let k → ∞ k\to\infty. If x 0 x_{0} were to be fixed and k k allowed to grow, there would be nothing stochastic at all happening, since we believe the 3 ​ x + 1 3x+1 Conjecture!

#### Remark.

The drift, as given in ( 5.57), is log ⁡ ( 3 4) ≈ − 0.28768 \log(\frac{3}{4})\approx-0.28768. Compare this to ( 3.34), where the drift of the Biased Random Walk model is computed to be 1 2 ​ log ⁡ ( 3 4) ≈ − 0.14384 \frac{1}{2}\log(\frac{3}{4})\approx-0.14384. While it is not surprising that the accelerated map U U should have a more aggressive pull to the origin, it is curious that it is exactly twice as fast (on an exponential scale) as the 3 ​ x + 1 3x+1 function T T.

#### Remark.

Given that the drift of the (logarithm of the) accelerated 3 ​ x + 1 3x+1 function U U is μ = log ⁡ ( 3 4) \mu=\log(\frac{3}{4}), one expects that the typical total stopping time of a seed n n is roughly

 | 1 | μ | ​ log ⁡ n ≈ 3.476 ​ log ⁡ n. {1\over|\mu|}\log n\approx 3.476\log n. |  |

### 5.4 Entropy

###### Definition 5.4

The entropy of a random variable X X taking values in [M]:= { 1, 2, …, M } [M]:=\{1,2,\dots,M\} is given by

 | H:= − ∑ m = 1 M ℙ [X = m] log ℙ [X = m]. H:=-\sum_{m=1}^{M}{{P}}[X=m]\log{{P}}[X=m]. |  |

The following facts are classical:

1. (i)

If X X is distributed uniformly in [M] [M] then H = log ⁡ M H=\log M.

2. (ii)

The entropy H H is maximized by the uniform distribution.

The first is an elementary exercise, while the second is proved easily using, e.g., Lagrange’s multiplier method.

In light of Theorem 5.2, for any fixed k ≥ 1 k\geq 1, the value 0 ≤ r k ≤ 3 k − 1 0\leq r_{k}\leq 3^{k}-1 is a function of the values ε \varepsilon and ( 𝔬 1, …, 𝔬 k) ({o}_{1},\dots,{o}_{k}), and hence has a natural density. For a fixed 𝔯 ∈ [0, 3 k − 1] {r}\in[0,3^{k}-1] we write

 | 𝔻 Π [x 0: r k ( x 0) = 𝔯] to mean ∑ ( 𝔬 1, …, 𝔬 k), ε ∈ { 1, 5 } r k ​ ( ε, 𝔬 1, …, 𝔬 k) = 𝔯 𝔻 Π [Σ ( ε) ( 𝔬 1, …, 𝔬 k)]. {{D}}_{\Pi}[x_{0}:r_{k}(x_{0})={r}]\qquad\mbox{ to mean }\qquad\sum_{({o}_{1},\dots,{o}_{k}),\ \varepsilon\in\{1,5\}\atop r_{k}(\varepsilon,{o}_{1},\dots,{o}_{k})={r}}{{D}}_{\Pi}[\Sigma^{(\varepsilon)}({o}_{1},\dots,{o}_{k})]. |  |

One might hope that r k r_{k} (which is a deterministic function but can be thought of as a “random variable”) is close to being uniformly distributed in { 0, 1, …, 3 k − 1 } \{0,1,\dots,3^{k}-1\}; then one could attempt to “bootstrap” iterations of U U to one-another to have better quantitative control on various asymptotic densities with k k not too large. Were this to be the case, the entropy (defined for this using 𝔻 Π {{D}}_{\Pi} in place of ℙ {{P}}) would be log ⁡ 3 k = k ​ log ⁡ 3 \log 3^{k}=k\log 3.

###### Theorem 5.6

(Entropy of r k r_{k}) There is some constant c > 0 c>0 such that the entropy H H of r k r_{k} satisfies:

 | H ≥ k ​ log ⁡ 3 − c ​ log ⁡ k. H\geq k\log 3-c\log k. |  |

#### Proof.

This statement is Theorem 5.1 in Sinai [35].

The function r k r_{k} in Theorem 5.2 is accompanied by the residue class δ k ∈ { 1, 5 } \delta_{k}\in\{1,5\}, which satisfies, cf. ( 5.54),

 | δ k ≡ 2 𝔬 k ( mod 3). \delta_{k}\equiv 2^{{o}_{k}}(\bmod 3). |  |

It follows immediately from the fact that 𝔬 k {o}_{k} is geometrically distributed with parameter 1 / 2 1/2, that

 | 𝔻 Π [x 0: δ k ( x 0) = 1] = 𝔻 Π [x 0: 𝔬 k is even ] = 1 3, {{D}}_{\Pi}[x_{0}:\delta_{k}(x_{0})=1]={{D}}_{\Pi}[x_{0}:{o}_{k}\mbox{ is even }]=\frac{1}{3}, |  |

and hence of course, 𝔻 Π [x 0: δ k ( x 0) = 5] = 2 3 {{D}}_{\Pi}[x_{0}:\delta_{k}(x_{0})=5]=\frac{2}{3}.

Moreover, if r k r_{k} is uniformly distributed, then so are the digits h k ​ ( j) ∈ { 0, 1, 2 } h_{k}(j)\in\{0,1,2\} in its 3 3 -adic expansion:

 | r k = h k ​ ( k − 1) ⋅ 3 k − 1 + h k ​ ( k − 2) ⋅ 3 k − 2 + ⋯ + h k ​ ( 1) ⋅ 3 + h k ​ ( 0). r_{k}=h_{k}(k-1)\cdot 3^{k-1}+h_{k}(k-2)\cdot 3^{k-2}+\cdots+h_{k}(1)\cdot 3+h_{k}(0). |  |

Note that only the first few leading digits h k ​ ( k − 1), h k ​ ( k − 2), …, h k ​ ( k − t) h_{k}(k-1),h_{k}(k-2),\dots,h_{k}(k-t) are needed to specify that location of r k / 3 k r_{k}/3^{k}, to within an error of 1 / 3 t 1/3^{t}.

###### Theorem 5.7

(Joint Uniform Distribution) The joint distributions of ( r k / 3 k, δ k) (r_{k}/3^{k},\delta_{k}) converge weakly to the uniform distribution, that is, for any fixed t ≥ 1 t\geq 1 and 𝔥 1, …, 𝔥 t ∈ { 0, 1, 2 } {h}_{1},\dots,{h}_{t}\in\{0,1,2\}, as k → ∞ k\to\infty,

 | 𝔻 Π [x 0: h k ( k − 1) = 𝔥 1, h k ( k − 2) = 𝔥 2, …, h k ( k − t) = 𝔥 t, δ k ( x 0) = 1] → 1 3 t ⋅ 1 3, {{D}}_{\Pi}[x_{0}:h_{k}(k-1)={h}_{1},h_{k}(k-2)={h}_{2},\dots,h_{k}(k-t)={h}_{t},\delta_{k}(x_{0})=1]\to{1\over 3^{t}}\cdot{1\over 3}, |  |

and

 | 𝔻 Π [x 0: h k ( k − 1) = 𝔥 1, h k ( k − 2) = 𝔥 2, …, h k ( k − t) = 𝔥 t, δ k ( x 0) = 5] → 1 3 t ⋅ 2 3. {{D}}_{\Pi}[x_{0}:h_{k}(k-1)={h}_{1},h_{k}(k-2)={h}_{2},\dots,h_{k}(k-t)={h}_{t},\delta_{k}(x_{0})=5]\to{1\over 3^{t}}\cdot{2\over 3}. |  |

#### Proof.

This appears as Theorem 1 in Sinai [36]. See also [37].

## 6 3 ​ x + 1 3x+1 Backwards Iteration: 3 ​ x + 1 3x+1 Trees

One can also model backwards iteration of the 3 ​ x + 1 3x+1 map T ⁡ ( x) T(x).

Backwards iteration is described by a tree of inverse iterates, and there are either one or two inverse iterates. Here

 | T ( − 1) ​ ( n) = { { 2 ​ n } if ​ n ≡ 0, 1 ( mod 3), { 2 ​ n, 2 ​ n − 1 3 } if ​ n ≡ 2 ( mod 3). T^{(-1)}(n)=\left\{\begin{array}[]{cl}\{2n\}&\mbox{if}~n\equiv 0,1~(\bmod~3),\\ \\ \{2n,\frac{2n-1}{3}\}&\mbox{if}~~n\equiv 2(\bmod~3).\end{array}\right. |  |

Starting from a root node labelled a a we can grow an infinite tree 𝒯 ⁡ ( a) {\cal T}(a) of all the inverse iterates of a a. Each node in the tree is labelled by its associated 3 ​ x + 1 3x+1 function value. To a node labelled n n we add either one or two (directed) edges from the elements of T − 1 ​ ( n) T^{-1}(n) to n n, and we label these two edges by the value of this element.

### 6.1 Pruned 3 ​ x + 1 3x+1 Trees

Next we note that any a ≡ 0 ( mod 3) a\equiv 0~(\bmod~3) has exactly one inverse iterate, which itself is 0 ( mod 3) 0~(\bmod~3). Thus if a ≡ 0 ( mod 3) a\equiv 0~(\bmod~3) the set of inverse iterates forms a single branch that never divides. However if a ≢ 0 ( mod 3) a\not\equiv 0~(\bmod~3) then the tree grows exponentially in size. It is convenient therefore to restrict to numbers a ≢ 0 ( mod 3) a\not\equiv 0~(\bmod~3) and furthermore to prune such a tree to remove all nodes n ≡ 0 ( mod 3) n\equiv 0~(\bmod~3). This produces an (infinite depth) pruned tree 𝒯 ∗ ​ ( a) {{\cal T}}^{\ast}(a) which is described by inverse iterates of the modified map

 | T ~ ( − 1) ​ ( n) = { { 2 ​ n } if ​ n ≡ 1, 4, 5 ​ or ​ 7 ( mod 9), { 2 ​ n, 2 ​ n − 1 3 } if ​ n ≡ 2 ​ or ​ 8 ( mod 9), \tilde{T}^{(-1)}(n)=\left\{\begin{array}[]{cl}\{2n\}&\mbox{if}~n\equiv 1,4,5~\mbox{or}~7~(\bmod~9),\\ \\ \{2n,\frac{2n-1}{3}\}&\mbox{if}~~n\equiv 2~\mbox{or}~8~(\bmod~9),\end{array}\right. |  | (6.58) |

applied starting with root node labelled n 0:= a n_{0}:=a. The pruning operation is depicted in Figure 6.6, with root node assigned depth 0 0.

16 1 1 2 4 4 5 8 2 1 | 64 5 10 20 6 3 32 16 8 4 | 5 20 10 64 8 16 4 32 |

(i) 𝒯 4 ​ ( 1) {\cal T}_{4}(1) | (ii) 𝒯 4 ​ ( 4) {\cal T}_{4}(4) | (iii) 𝒯 4 ∗ ​ ( 4) {\cal T}_{4}^{*}(4) |

Figure 6.6: 3 ​ x + 1 3x+1 trees 𝒯 k ​ ( a) {\cal T}_{k}(a) and “pruned” 3 ​ x + 1 3x+1 tree 𝒯 k ∗ ​ ( a) {\cal T}_{k}^{*}(a), with k = 4 k=4.

We obtain a reduced tree 𝒯 ¯ ∗ ​ ( a) {\overline{{\cal T}}}^{\ast}(a) obtained by labelling each node with the ( mod 2) (\bmod~2) residue class of the 3 ​ x + 1 3x+1 value assigned to that node. (One may also think of this as labelling the directed edge leaving this node, with the exception of the root node.)

We let 𝒯 k ∗ ​ ( a) {{\cal T}}_{k}^{\ast}(a) denote the pruned tree with root node n 0 = a n_{0}=a, cut off at depth k k, and we let 𝒯 ¯ k ∗ ​ ( a) {\overline{{\cal T}}}_{k}^{\ast}(a) denote the same tree, keeping only the node labels ( mod 2), (\bmod~2), for all nodes except the root node, where no data is kept. Let N ∗ ​ ( k, a) N^{\ast}(k;a) count the number of depth k k leaves in this tree. Then we have

 | N ∗ ( k, a):= | { n: n ≢ 0 ( mod 3) and T ( k) ( n) = a } |. N^{\ast}(k,a):=|\{n:~n\not\equiv 0~(\bmod~3)~\mbox{and}~~T^{(k)}(n)=a\}|. |  | (6.59) |

We have N ∗ ​ ( k, a) ≤ 2 k N^{\ast}(k,a)\leq 2^{k} as a consequence of the fact that each 3 ​ x + 1 3x+1 tree has at most two upward branches at each node.

The following result gives information on the sizes of depth k k trees over all possible tree types ( [23, Theorem 3.1]).

###### Theorem 6.1

(Structure of Pruned 3 ​ x + 1 3x+1 Trees)

(1) For k ≥ 1 k\geq 1 and a ≢ 0 ( mod 3) a\not\equiv 0~(\bmod~3), the structure of the pruned level k k tree 𝒯 ¯ k ∗ ​ ( a) {\overline{{\cal T}}}_{k}^{\ast}(a), and hence the number N ∗ ​ ( k, a) N^{\ast}(k,a), is completely determined by a ( mod 3 k + 1) a~(\bmod~3^{k+1}).

(2) There are 2 ⋅ 3 k 2\cdot 3^{k} residue classes a ( mod 3 k + 1) a~(\bmod~3^{k+1}) with a ≢ 0 ( mod 3) a\not\equiv 0~(\bmod~3). For these

 | ∑ a ( mod 3 k + 1) m ≢ 0 ( mod 3) N ∗ ​ ( k, a) = 2 ⋅ 4 k. \sum_{{a~(\bmod~3^{k+1})}\atop{m\not\equiv 0~(\bmod~3)}}N^{\ast}(k,a)=2\cdot 4^{k}. |  | (6.60) |

It follows that if a residue class a ( mod 3 k + 1) a~(\bmod~3^{k+1}) with a ≢ 0 ( mod 3) a\not\equiv 0(\bmod~3) is picked with the uniform distribution, the expected number of leaves in the random tree 𝒯 ¯ k ∗ ​ ( a) {\overline{{\cal T}}}_{k}^{\ast}(a) is exactly ( 4 3) k \left(\frac{4}{3}\right)^{k}.

We now consider the complete set of numbers having total stopping time k k. Set

 | N k:= | { n: σ ∞ ​ ( n) = k } |. N_{k}:=|\{n:~\sigma_{\infty}(n)=k\}|. |  | (6.61) |

Recall from § 2.5 that N k = N k ​ ( 1) N_{k}=N_{k}(1), where N k ​ ( a) N_{k}(a) counts the number of integers that iterate to a a after exactly k k iterations of the 3 ​ x + 1 3x+1 map T T. We defined there the 3 ​ x + 1 3x+1 tree growth constants

 | δ 3 ​ ( a):= lim sup k → ∞ 1 k ​ log ⁡ N k ​ ( a). \delta_{3}(a):=\limsup_{k\to\infty}\frac{1}{k}\log N_{k}(a). |  |

Theorem 6.1 suggests the following conjecture for these tree growth constants, made by Lagarias and Weiss [23].

###### Conjecture 6.1

For each a ≢ 0 ( mod 3) a\not\equiv 0~(\bmod~3), the 3 ​ x + 1 3x+1 tree growth constant δ 3 ​ ( a) \delta_{3}(a) is given by

 | δ 3 ​ ( a) = log ⁡ ( 4 3). \delta_{3}(a)=\log\left(\frac{4}{3}\right). |  | (6.62) |

Applegate and Lagarias [2] determined by computer the maximal and minimal number of leaves in 3 ​ x + 1 3x+1 trees of depth k k for k ≥ 30 k\geq 30. The maximal and minimal number of leaves in such trees at level k k is given by

 | N k +:= max { N k ∗ ( a): a ( mod 3 k + 1) with a ≢ 0 ( mod 3) }. N_{k}^{+}:=\max\{N_{k}^{\ast}(a):~a~(\bmod~3^{k+1})~\mbox{with}~a\not\equiv 0~(\bmod~3)\}. |  |

and

 | N k − = min { N k ∗ ( a): a ( mod 3 k + 1) with a ≢ 0 ( mod 3) }, N_{k}^{-}=\min\{N_{k}^{\ast}(a):~a~(\bmod~3^{k+1})~\mbox{with}~a\not\equiv 0~(\bmod~3)\}, |  |

respectively. Figure 6.7 pictures maximal and minimal trees for depth k = 5 k=5. (Circled nodes indicate an omitted inverse iterate under T − 1 T^{-1} that is ≡ 0 ( mod 3) \equiv 0~(\bmod~3).)

112 74 224 14 37 56 28 7 | 35 23 7 11 17 26 13 53 80 40 20 |

(i) 𝒯 5 ∗ ​ ( 7) {\cal T}_{5}^{*}(7) attains N − ​ ( 5) = 2 N^{-}(5)=2 | (ii) 𝒯 5 ∗ ​ ( 20) {\cal T}_{5}^{*}(20) attains N + ​ ( 5) = 8 N^{+}(5)=8 |

Figure 6.7: Maximal and Minimal depth 5 pruned 3 ​ x + 1 3x+1 Trees

The data on these counts N ± ​ ( k) N_{\pm}(k) was presented already in § 2.5, cf. Table 4. Based on this data, Applegate and Lagarias [4, Conjecture C] formulated the following strengthened conjecture, which implies Conjecture 6.1.

###### Conjecture 6.2

The maximal and minimal number of leaves of 3 ​ x + 1 3x+1 trees satisfy, as k → ∞ k\to\infty,

 | N k − = ( 3 4) k + o ⁡ ( k) N_{k}^{-}=\left(\frac{3}{4}\right)^{k+o(k)} |  | (6.63) |

 | N k + = ( 3 4) k + o ⁡ ( k). N_{k}^{+}=\left(\frac{3}{4}\right)^{k+o(k)}. |  | (6.64) |

### 6.2 3 ​ x + 1 3x+1 Backwards Stochastic Models: Branching Random Walks

Lagarias and Weiss [23] formulated stochastic models for the growth of 3 ​ x + 1 3x+1 trees that were multi-type branching processes. Such models grow a random tree, with nodes marked as several different kinds of individuals. In this case the number of nodes of each type at each depth k k (also called generation k k) can be viewed as the output of the branching process. The particular branching processes they used are multi-type Galton-Watson processes.

Lagarias and Weiss also modeled the size of preimages of elements in a (pruned) 3 ​ x + 1 3x+1 tree. This size is specified by a real number attached to each node. Branching process models which attach to each node in the tree a real number giving the position of those individuals on a line, according to some (possibly random) rule, are models called multi-type branching random walks. Here the location of the individuals on the line give the random walk aspect; offspring nodes at level k k are shifted in position from their parent ancestor at level k − 1 k-1 by a point process. The process starts with a root node giving a single progenitor at level 0 0 (generation 0 0).

Lagarias and Weiss defined a hierarchy of branching random walk models, which they denoted ℬ ⁡ [3 j] {\cal B}[3^{j}], for each j ≥ 0 j\geq 0. These branching random walk models, having several kinds of individuals, model the backwards iteration viewed ( mod 3 j) ~(\bmod~3^{j}). The model for j = 0 j=0 is simpler than the other models.

3 ​ x + 1 3x+1 Branching Random walk ℬ ⁡ [3 0] {\cal B}[3^{0}]. There is one type of individual. With probability 2 3 \frac{2}{3} an individual has a single offspring located at a position shifted by log ⁡ 2 \log 2 on the line from its progenitor, and with probability 1 3 \frac{1}{3} it has two offspring located at positions shifted log ⁡ 2 \log 2 and log ⁡ 2 3 \log\frac{2}{3} on the line from their progenitor. If the progenitor is in generation (or depth) k − 1 k-1, the offspring are in generation k k. The tree is grown from a single individual at generation 0 0, with specified location log ⁡ a \log a.

The more general models for j ≥ 1 j\geq 1 are given as follows.

3 ​ x + 1 3x+1 Branching Random walk ℬ ⁡ [3 j], ( j ≥ 1) {\cal B}[3^{j}],(j\geq 1). There are p = 2 ⋅ 3 j − 1 p=2\cdot 3^{j-1} types of individuals, indexed by residue classes a ( mod 3 j) a~(\bmod~3^{j}) with a ≢ 0 ( mod 3) a\not\equiv 0~(\bmod~3). The distribution of offspring of an individual of type a ( mod 3 j) a~(\bmod~3^{j}), at any given depth k k in the branching, is determined as follows: Regard a ( mod 3 j) a~(\bmod~3^{j}) labelling a node at depth d − 1 d-1. Regard it as being, with probability 1 3 \frac{1}{3} each, one of the three possible residue classes a ~ ( mod 3 j + 1) \tilde{a}~(\bmod~3^{j+1}) consistent with it. The tree (of depth 1 1) with a ~ \tilde{a} as root node, given by ( T ∗) − 1 ​ ( a ~) (T^{\ast})^{-1}(\tilde{a}) has either one or two progeny, at depth 1 1 and their node labels are well-defined classes ( mod 3 j) (\bmod~3^{j}), either 2 ​ a ~ 2\tilde{a} or, if it legally occurs, 2 ​ a ~ − 1 3 ( mod 3 j) \frac{2\tilde{a}-1}{3}(\bmod~3^{j}). The branching random walk then produces an individual of type 2 ​ a ~ 2\tilde{a} at generation k + 1 k+1 whose position is additively shifted by log ⁡ 2 \log 2 from that of the generation k k progenitor node, plus, if legal, another labelled 2 ​ a ~ − 1 3 \frac{2\tilde{a}-1}{3}, which is shifted in position by log ⁡ ( 2 3) \log(\frac{2}{3}) on the line from that of the generation k k -node. The tree is grown from a single individual at depth 0 0, with specified type and location log ⁡ a \log a.

In these models, the behavior of the random walk part of the model can be completely reconstructed from knowing the type of each node. This is a very special property of these branching random walk models, which does not hold for general branching random walks.

In such models, one may think of the nodes as representing individuals, with individuals at level k k being children of a particular individual at level k − 1 k-1; the random walk aspect indicates position in space of these individuals.

Let ω \omega denote a single realization of such a branching random walk ℬ ⁡ [3 j] {\cal B}[3^{j}] which starts from a single individual ω 0, 1 \omega_{0,1} of type 1 ( mod 3 j) 1~(\bmod~3^{j}) at depth 0 0, with initial position labeled log ⁡ a \log a. Here ω \omega describes a particular infinite tree. We let N k ​ ( ω) N_{k}(\omega) denote the number of individuals at level k k of the tree. We let S ⁡ ( ω k, j) S(\omega_{k},j) denote the position of the j j -th individual at level k k in the tree, for 1 ≤ j ≤ N k ​ ( ω) 1\leq j\leq N_{k}(\omega).

These models are all supercritical branching processes in the following very strong sense. In every random realization ω \omega, the number of nodes at level d d grows exponentially in d d, and there are no extinction events.

Lagarias and Weiss [23] observed that the predictions of these models stabilized for all j ≥ 1 j\geq 1, as far as the behavior of asymptotic statistics related to 3 ​ x + 1 3x+1 trees is concerned. This is illustrated in the following theorems.

### 6.3 3 ​ x + 1 3x+1 Backwards Model Prediction: Tree Sizes

Concerning the number of nodes N k ​ ( ω) N_{k}(\omega) in a realized tree at depth k k, Lagarias and Weiss proved the following result [23, Corollary 3.1].

###### Theorem 6.2

( 3 ​ x + 1 3x+1 Stochastic Tree Size) For all j ≥ 0 j\geq 0, a realization ω \omega of a tree grown in the 3 ​ x + 1 3x+1 branching random walk model ℬ ⁡ [3 j] {\cal B}[3^{j}] has

 | lim k → ∞ 1 k ( log N k ( ω)) = log ( 4 3), for almost every ω. \lim_{k\to\infty}\frac{1}{k}\left(\log N_{k}(\omega)\right)=\log\left(\frac{4}{3}\right),~~~~\mbox{ for almost every $\omega$.} |  | (6.65) |

This result only uses the Galton-Watson structure built into the process ℬ ⁡ [3 j]. {\cal B}[3^{j}]. Its prediction is consistent with the rigourous results on average tree size for pruned 3 ​ x + 1 3x+1 trees given in Theorem 6.1, and it also supports Conjecture 6.1.

### 6.4 3 ​ x + 1 3x+1 Backwards Model Prediction: Extremal Total Stopping Times

Next, as a statistic that corresponds to an extremal trajectory, consider the first birth in generation k k, which is the leftmost individual on the line at depth k k in the branching random walk. Denote the location of this individual by L k ∗ ​ ( ω) L_{k}^{\ast}(\omega), for a given realization ω \omega of the random walk. Lagarias and Weiss [23, Theorem 3.4] proved the following result.

###### Theorem 6.3

(Asymptotic First Birth Location) For any 3 ​ x + 1 3x+1 branching random walk model ℬ ⁡ [3 j] {\cal B}[3^{j}] with j ≥ 2 j\geq 2, there is a constant β B ​ P \beta_{BP} such that for all j ≥ 0 j\geq 0, the branching random walk ℬ ⁡ [3 j] {\cal B}[3^{j}] has asymptotic first birth (leftmost birth)

 | lim k → ∞ L k ∗ ( ω) = β B ​ P for almost every ω. \lim_{k\to\infty}L_{k}^{\ast}(\omega)=\beta_{BP}~~~~~\mbox{ for almost every $\omega$. } |  | (6.66) |

This constant β B ​ P ≈ 0.02399 \beta_{BP}\approx 0.02399 is determined uniquely by the properties that it is the unique β > 0 \beta>0 that satisfies

 | g ~ ​ ( β) = 0 \tilde{g}(\beta)=0 |  | (6.67) |

where

 | g ~ ​ ( a):= − s ​ u ​ p θ ≤ 0 ​ ( a ​ θ − log ⁡ M B ​ P ​ ( θ)). \tilde{g}(a):=-sup_{\theta\leq 0}\left(a\theta-\log M_{BP}(\theta)\right). |  | (6.68) |

Here M B ​ P ​ ( θ) M_{BP}(\theta) is the branching process moment generating function

 | M B ​ P ​ ( θ):= 2 θ + 1 3 ​ ( 2 3) θ. M_{BP}(\theta):=2^{\theta}+\frac{1}{3}(\frac{2}{3})^{\theta}. |  | (6.69) |

Since the first birth individual at depth k k corresponds to taking k k iterations to reach the root node, we can define a branching process scaled stopping limit γ B ​ P ​ ( ω) \gamma_{BP}(\omega). This is the BP model’s prediction for the scaled stopping constant γ \gamma from ( 2.16), defined by

 | γ B ​ P ​ ( ω):= lim sup k → ∞ k L k ∗ ​ ( ω). \gamma_{BP}(\omega):=\limsup_{k\to\infty}\frac{k}{L_{k}^{\ast}(\omega)}. |  |

Theorem 6.3 implies that this value is constant (almost surely independent of ω \omega), and takes the value

 | γ B ​ P = ( β B ​ P) − 1. \gamma_{BP}=(\beta_{BP})^{-1}. |  | (6.70) |

Note that since β B ​ P ≈ 0.02399 \beta_{BP}\approx 0.02399, we have 1 / β B ​ P ≈ 41.7 1/\beta_{BP}\approx 41.7. At this point we have two completely different predictions for the scaled stopping constant γ \gamma, one from the RRW model (cf. Theorem 4.1) which approximates forward iterations, and another from the BP models which estimate backwards iterations. Applegate and Lagarias then prove [23, Theorem 4.1] the following striking identity.

###### Theorem 6.4

( 3 ​ x + 1 3x+1 Random Walk-Branching Random Walk Duality) The 3 ​ x + 1 3x+1 repeated random walk (RRW) stochastic model scaled stopping time limit γ R ​ R ​ W \gamma_{RRW} and the 3 ​ x + 1 3x+1 branching random walk (BP) model ℬ ⁡ [3 j] {\cal B}[3^{j}] with j ≥ 0 j\geq 0, scaled stopping time limit γ B ​ P \gamma_{BP} are identical! I.e.,

 | γ R ​ R ​ W = γ B ​ P. \gamma_{RRW}=\gamma_{BP}. |  | (6.71) |

#### Proof.

This is a consequence [23] of an identity relating the moment generating functions associated to the two models, which is M B ​ P ​ ( θ) = M R ​ R ​ W ​ ( θ + 1) M_{BP}(\theta)=M_{RRW}(\theta+1); compare ( 4.39) and ( 6.69).

#### Remark.

Recall the critique of the RRW model given in § 4.4, that various trajectories coalesce in their forward iterates. But the BP models, by their tree construction, completely take into account the dependence caused by coalescing trajectories! Since both models predict the same exact value for γ \gamma, it appears the critique has been thwarted off.

### 6.5 3 ​ x + 1 3x+1 Backwards Model Prediction: Total Preimage Counts

We next consider what the branching process models have to say about the number of integers below x x that eventually iterate to a given integer a a.

The following result gives, for the simplest branching random walk model, an almost sure asymptotic of the number of inverse iterates of size below a given bound ( [23, Theorem 4.2]).

###### Theorem 6.5

(Stochastic Inverse Iterate Counts) For a realization ω \omega of the branching random walk ℬ ⁡ [1] {\cal B}[1], let I ∗ ​ ( t, ω) I^{\ast}(t;\omega) count the number of progeny located at positions S ⁡ ( ω k, j) ≤ x S(\omega_{k,j})\leq x, i.e.

 | I ∗ ( x; ω):= #{ ω k, j: S ( ω k, j) ≤ x, for any k ≥ 1, 1 ≤ j ≤ N k ( ω) }. I^{\ast}(x;\omega):=\#\{\omega_{k,j}:S(\omega_{k,j})\leq x,\mbox{for~any}~~k\geq 1,~1\leq j\leq N_{k}(\omega)\}. |  | (6.72) |

Then the asymptotic estimate

 | I ∗ ​ ( x, ω) = x 1 + o ⁡ ( 1) ​ as ​ x → ∞ I^{\ast}(x;\omega)=x^{1+o(1)}~~~\mbox{as}~~x\to\infty |  | (6.73) |

holds almost surely.

The model statistic I ∗ ​ ( x, ω) I^{\ast}(x;\omega) functions as a proxy for the function π a ​ ( x) \pi_{a}(x), where log ⁡ a \log a gives the position of the root node of the branching random walk. This result is the stochastic analogue of Conjecture 2.1 about the 3 ​ x + 1 3x+1 growth exponent.

## 7 The 5 ​ x + 1 5x+1 Function: Symbolic Dynamics and Orbit Statistics

We now turn for comparison to the 5 ​ x + 1 5x+1 iteration. Some features of the dynamics of this iteration are similar to that of the 3 ​ x + 1 3x+1 problem, and some are different. Here the dynamics of iteration in the long run are expected to be quite different globally from the 3 ​ x + 1 3x+1 problem; most trajectories are expected to diverge. In this section we formulate several orbit statistics for this map, some the same as for the 3 ​ x + 1 3x+1 map, and some changed. We review basic results on them.

### 7.1 5 ​ x + 1 5x+1 Forward Iteration: Symbolic Dynamics

The basic features of the 5 ​ x + 1 5x+1 problem are similar to the 3 ​ x + 1 3x+1 problem. We introduce the parity sequence

 | S 5 ​ ( n):= ( n ( mod 2), T 5 ​ ( n) ( mod 2), T 5 ( 2) ​ ( n) ( mod 2), …). S_{5}(n):=(n~(\bmod~2),T_{5}(n)~(\bmod~2),T_{5}^{(2)}(n)~(\bmod~2),...). |  | (7.74) |

The symbolic dynamics is similar to the 3 ​ x + 1 3x+1 map: all finite initial symbol sequences of length k k occur, each one for a single residue class ( mod 2 k) (\bmod~2^{k}).

###### Theorem 7.1

( 5 ​ x + 1 5x+1 Parity Sequence Symbolic Dynamics) The k k -truncated parity sequence S 5 [k] ​ ( n) S_{5}^{[k]}(n) of the first k k iterates of the 5 ​ x + 1 5x+1 map T ⁡ ( x) T(x) is periodic in n n with period 2 k 2^{k}. Each of the 2 k 2^{k} possible 0 − 1 0-1 vectors occurs exactly once in the initial segment 1 ≤ n ≤ 2 k 1\leq n\leq 2^{k}.

#### Proof.

The proof of this result exactly parallels that of Theorem 2.1.

As before, the parity sequence of an orbit of x 0 x_{0} uniquely determines x 0 x_{0}.

Analysis of this recursion, assuming even and odd iterates are equally likely, as prescribed by Theorem 7.1, we find the logarithms of iterates grow in size on the average.

### 7.2 5 ​ x + 1 5x+1 Forward Iteration: λ + \lambda^{+} - Stopping Times

Most 5 ​ x + 1 5x+1 iteration sequences grow on average, rather than shrinking on average. An appropriate notion of stopping time for this situation is as follows.

###### Definition 7.1

For fixed λ ≥ 1 \lambda\geq 1, the λ + \lambda^{+} -stopping time σ λ + ​ ( n) \sigma_{\lambda}^{+}(n) of a map T 5: ℤ → ℤ T_{5}:{{Z}}\to{{Z}} for input n n is the minimal value of k ≥ 0 k\geq 0 such that T 5 ( k) ​ n > λ ​ n T_{5}^{(k)}{n}>\lambda n, e.g.

 | σ λ + ​ ( n):= inf { k ≥ 0: T 5 ( k) ​ ( n) n > λ }. \sigma_{\lambda}^{+}(n):=\inf\{k\geq 0:\frac{T_{5}^{(k)}(n)}{n}>\lambda\}. |  | (7.75) |

If no such value k k exists, we set σ λ + ​ ( n) = + ∞. \sigma_{\lambda}^{+}(n)=+\infty.

One now has the following result, which parallels Theorem 2.2 for the 3 ​ x + 1 3x+1 map, except that here iterates grow in size rather than shrink in size.

###### Theorem 7.2

( λ + \lambda^{+} -Stopping Time Natural Density)

(i) For the 5 ​ x + 1 5x+1 map T 5 ​ ( n) T_{5}(n), and fixed λ ≥ 1 \lambda\geq 1 and k ≥ 1 k\geq 1, the set S λ + ​ ( k) S_{\lambda}^{+}(k) of integers having λ + \lambda^{+} -stopping time at most k k has a well-defined natural density 𝔻 ⁡ ( S λ + ​ ( k)) {{D}}(S_{\lambda}^{+}(k)).

(ii) This natural density satisfies

 | lim k → ∞ 𝔻 ⁡ ( S λ + ​ ( k)) = 1. \lim_{k\to\infty}{{D}}(S_{\lambda}^{+}(k))=1. |  | (7.76) |

In particular, the set of numbers with finite λ + \lambda^{+} -stopping time has natural density 1 1.

#### Proof.

Claim (i) follows using the Parity Sequence Theorem 7.1. Here the set is a finite union of arithmetic progressions ( mod 2 k) (\bmod~2^{k}), except a finite number of initial elements may be omitted from each such progression.

The result (ii) can be established by a similar argument to that used for the 3 ​ x + 1 3x+1 problem in Theorem 2.2.

Here we note a surprise: there are infinitely many exceptional integers n n that have λ + \lambda^{+} -stopping time equal to + ∞ +\infty! This occurs because the 5 ​ x + 1 5x+1 problem has a periodic orbit { 1, 3, 8, 4, 2 } \{1,3,8,4,2\}, and infinitely many positive seeds n 0 n_{0} eventually enter this orbit, e.g. n 0 = 2 4 ​ k − 1 5 n_{0}=\frac{2^{4k}-1}{5} for any k ≥ 2 k\geq 2. All of these integers have σ λ + ​ ( n 0) = + ∞. \sigma_{\lambda}^{+}(n_{0})=+\infty. Nevertheless Theorem 7.2 asserts that such integers have natural density zero.

### 7.3 5 ​ x + 1 5x+1 Stopping Time Statistics: Total Stopping Times

The 5 ​ x + 1 5x+1 problem has a finite orbit containing 1 1, and we may define total stopping time as for the 3 ​ x + 1 3x+1 function.

###### Definition 7.2

For n ≥ 1 n\geq 1 the total stopping time σ ∞ ​ ( n, T 5) \sigma_{\infty}(n;T_{5}) of the 5 ​ x + 1 5x+1 function is given by

 | σ ∞ ​ ( n, T 5):= inf { k ≥ 1: T 5 ( k) ​ ( n) = 1 }. \sigma_{\infty}(n;T_{5}):=\inf\{k\geq 1:~T_{5}^{(k)}(n)=1\}. |  | (7.77) |

We set σ ∞ ​ ( n, T 5) = + ∞ \sigma_{\infty}(n;T_{5})=+\infty if no finite k k has this property.

Here we expect that the vast majority of positive n n will belong to divergent trajectories, and only a small minority of n n have a well-defined finite value σ ∞ ​ ( n, T 5) < ∞ \sigma_{\infty}(n;T_{5})<\infty. It is an open problem to prove that even a single trajectory (such as that emanating from the starting seed n 0 = 7 n_{0}=7) is divergent!

The best we can currently show unconditionally is a lower bound on the size of the extremal total stopping time that grows proportionally to log ⁡ n \log n.

###### Theorem 7.3

(Lower Bound for 5 ​ x + 1 5x+1 Total Stopping Times) There are infinitely many n n whose total stopping time satisfies

 | σ ∞ ​ ( n, T 5) ≥ ( log ⁡ 2 + log ⁡ 5 ( log ⁡ 2) 2) ​ log ⁡ n ≈ 4.79253 ​ log ⁡ n. \sigma_{\infty}(n,T_{5})\geq\left(\frac{\log 2+\log 5}{(\log 2)^{2}}\right)\log n\approx 4.79253\log n. |  | (7.78) |

#### Proof.

The Parity Sequence Theorem 6.2 implies there is at least one odd number n k n_{k} with 1 ≤ n k < 2 k 1\leq n_{k}<2^{k} whose first k − 1 k-1 iterates are also odd, so that T 5 ( k) ​ ( n k) ≥ ( 5 2) k ​ n k. T_{5}^{(k)}(n_{k})\geq(\frac{5}{2})^{k}n_{k}. Since a single step can divide by at most 2 2, we necessarily have (using log ⁡ n k ≤ k ​ log ⁡ 2 \log n_{k}\leq k\log 2),

 | σ ∞ ​ ( n k, T 5) log ⁡ n k ≥ k log ⁡ n k + ( k ​ log ⁡ 5 2 + log ⁡ n k log ⁡ 2) ​ 1 log ⁡ n k ≥ 2 log ⁡ 2 + log ⁡ 5 2 ( log ⁡ 2) 2 ≈ 4.79253. \frac{\sigma_{\infty}(n_{k},T_{5})}{\log n_{k}}\geq\frac{k}{\log n_{k}}+\left(\frac{k\log\frac{5}{2}+\log n_{k}}{\log 2}\right)\frac{1}{\log n_{k}}\geq\frac{2}{\log 2}+\frac{\log\frac{5}{2}}{(\log 2)^{2}}\approx 4.79253. |  |

We do not know if these numbers n k n_{k} have a finite total stopping time.

The methods of Applegate and Lagarias [4] for 3 ​ x + 1 3x+1 trees can potentially be applied to this problem, to further improve this lower bound, and to establish it for numbers n n having a finite total stopping time.

An interesting challenge is whether one can show for each c > 0 c>0 that only a density zero set of n n have σ ∞ ​ ( n, T 5) log ⁡ n < c \frac{\sigma_{\infty}(n;T_{5})}{\log n}<c. A stochastic model in § 8.9 predicts that all but finitely many trajectories having σ ∞ ​ ( n) > 85 ​ log ⁡ n \sigma_{\infty}(n)>85\log n will necessarily have σ ∞ ​ ( n) = + ∞ \sigma_{\infty}(n)=+\infty, so establishing this for c = 85 c=85 would be consistent with the prediction that only a density zero set of n n have 1 1 in their forward orbit under T 5 T_{5}.

### 7.4 5 ​ x + 1 5x+1 Size Statistics: Minimum Excursion Values

In the topsy-turvy world of the 5 ​ x + 1 5x+1 problem, since most trajectories get large, our substitute for the maximum excursion constant is the following reversed notion.

###### Definition 7.3

For an integer n n the minimal excursion value t − ​ ( n) t^{-}(n) of the 5 ​ x + 1 5x+1 function is given by

 | t − ​ ( n):= inf { | T 5 ( k) ​ ( n) |: k ≥ 0 }. t^{-}(n):=\inf\{|T_{5}^{(k)}(n)|:k\geq 0\}. |  | (7.79) |

We have t − ​ ( 0) = 0 t^{-}(0)=0, while infinitely many n n will have minimum excursion value equal to 1 1.

###### Definition 7.4

For n ≥ 1 n\geq 1 the minimal excursion constant ρ 5 − ​ ( n) \rho_{5}^{-}(n) of the 5 ​ x + 1 5x+1 function is given by

 | ρ 5 − ​ ( n):= lim inf n → ∞ log ⁡ t − ​ ( n) log ⁡ n. \rho_{5}^{-}(n):=\liminf_{n\to\infty}\frac{\log t^{-}(n)}{\log n}. |  | (7.80) |

We now immediately have the following result.

###### Theorem 7.4

The 5 ​ x + 1 5x+1 minimum excursion constant is given by

 | ρ 5 − = 0. \rho_{5}^{-}=0. |  | (7.81) |

#### Proof.

The inverse orbit of n = 1 n=1 for T 5 T_{5} contains { 2 j: j ≥ 1 } \{2^{j}:j\geq 1\}, whence t − ​ ( 2 j) = 1 t^{-}(2^{j})=1.

We state this easy result as a theorem, because it has the remarkable feature, among all the constants associated to these 3 ​ x + 1 3x+1 and 5 ​ x + 1 5x+1 maps, of being unconditionally proved! It also has the interesting feature that the stochastic models below make an incorrect prediction in this case, cf. Theorem 8.4.

### 7.5 5 ​ x + 1 5x+1 Count Statistics: 5 ​ x + 1 5x+1 Tree Sizes

In considering backwards iteration of the 5 ​ x + 1 5x+1 function, we can ask: given an integer a a how many numbers n n iterate forward to a a after exactly k k iterations, that is, T 5 ( k) ​ ( n) = a T_{5}^{(k)}(n)=a?

The set of backwards iterates of a given number a a can again be pictured as a tree; we call these 5 ​ x + 1 5x+1 trees. Now N k ​ ( a) N_{k}(a) counts the number of leaves at depth k k of the tree with root node a a, and N k ∗ N_{k}^{\ast} counts the number of leaves in a pruned 5 ​ x + 1 5x+1 tree, which is one from which all nodes with label n ≡ 0 ( mod 5) n\equiv 0~(\bmod~5) have been removed. The definitions are as follows.

###### Definition 7.5

(1) Let N k ​ ( a, T 5) N_{k}(a;T_{5}) count the number of integers that forward iterate under the 5 ​ x + 1 5x+1 map T 5 ​ ( n) T_{5}(n) to a a after exactly k k iterations, i.e.

 | N k ​ ( a, T 5):= | { n: T 5 ( k) ​ ( n) = a } |. N_{k}(a;T_{5}):=|\{n:~T_{5}^{(k)}(n)=a\}|. |  | (7.82) |

(2) Let N k ∗ ​ ( a, T 5) N_{k}^{\ast}(a;T_{5}) count the number of integers not divisible by 5 5 that forward iterate under the 5 ​ x + 1 5x+1 map T 5 ​ ( n) T_{5}(n) to a a after exactly k k iterations, i.e.

 | N k ∗ ( a; T 5):= | { n: T 5 ( k) ( n) = a, n ≢ 0 ( mod 5) } |. N_{k}^{\ast}(a;T_{5}):=|\{n:~T_{5}^{(k)}(n)=a,~n\not\equiv 0(\bmod~5)\}|. |  | (7.83) |

The case a = 1 a=1 is of particular interest, since the quantities then count integers that iterate to 1 1, and in this case we let

 | N k, 5:= N k ​ ( 1, T 5), N k, 5 ∗:= N k ∗ ​ ( 1, T 5). N_{k,5}:=N_{k}(1;T_{5}),~~~~~~~N_{k,5}^{\ast}:=N_{k}^{\ast}(1;T_{5}). |  |

###### Definition 7.6

(1) For a given a a the 5 ​ x + 1 5x+1 tree growth constant δ 5 ​ ( a) \delta_{5}(a) for a a is given by

 | δ 5 ​ ( a):= lim sup k → ∞ 1 k ​ ( log ⁡ N k ​ ( a, T 5)). \delta_{5}(a):=\limsup_{k\to\infty}\frac{1}{k}\left(\log N_{k}(a;T_{5})\right). |  | (7.84) |

(2) The 5 ​ x + 1 5x+1 tree growth constant δ 5 = δ 5 ​ ( 1). \delta_{5}=\delta_{5}(1).

The constant δ 5 ​ ( a) \delta_{5}(a) exists and is finite, as follows from the same upper bound as in ( 2.23).

The following result gives information on the sizes of depth k k pruned 5 ​ x + 1 5x+1 trees over all possible tree types.

###### Theorem 7.5

(Structure of Pruned 5 ​ x + 1 5x+1 Trees)

(1) For k ≥ 1 k\geq 1 and a ≢ 0 ( mod 5) a\not\equiv 0(\bmod~5), the structure of the pruned level k k tree 𝒯 ¯ k ∗ ​ ( a) {\overline{{\cal T}}}_{k}^{\ast}(a), and hence the number N k ∗ ​ ( a, T 5) N_{k}^{\ast}(a;T_{5}), is completely determined by a ( mod 5 k + 1) a~(\bmod~5^{k+1}).

(2) There are 4 ⋅ 5 k 4\cdot 5^{k} residue classes a ( mod 5 k + 1) a~(\bmod~5^{k+1}) with a ≢ 0 ( mod 5) a\not\equiv 0~(\bmod~5). For these

 | ∑ a ( mod 5 k + 1) a ≢ 0 ( mod 5) N k ∗ ​ ( a, T 5) = 4 ⋅ 6 k. \sum_{{a~(\bmod~5^{k+1})}\atop{a\not\equiv 0~(\bmod~5)}}N_{k}^{\ast}(a;T_{5})=4\cdot 6^{k}. |  | (7.85) |

It follows that if a residue class a ( mod 5 k + 1) a~(\bmod~5^{k+1}) with a ≢ 0 ( mod 5) a\not\equiv 0(\bmod~5) is picked with the uniform distribution, the expected number of leaves in the random tree 𝒯 ¯ k ∗ ​ ( a) {\overline{{\cal T}}}_{k}^{\ast}(a) is exactly ( 6 5) k \left(\frac{6}{5}\right)^{k}.

#### Proof.

This result is shown by a method exactly similar to the 3 ​ x + 1 3x+1 tree case ( [23, Theorem 3.1]). We omit details.

Theorem 7.5 suggests the following conjecture.

###### Conjecture 7.1

For each a ≢ 0 ( mod 5) a\not\equiv 0~(\bmod~5), the 5 ​ x + 1 5x+1 tree growth constant δ 5 ​ ( a) \delta_{5}(a) is given by

 | δ 5 ​ ( a) = log ⁡ ( 6 5). \delta_{5}(a)=\log\left(\frac{6}{5}\right). |  | (7.86) |

Compare this conjecture with the prediction of Theorem 8.7.

### 7.6 5 ​ x + 1 5x+1 Count Statistics: Total Inverse Iterate Counts

In considering backwards iteration of the 5 ​ x + 1 5x+1 function from an integer a a, the complete data is the set of integers that contain a a in their forward orbit. The following function describes this set.

###### Definition 7.7

Given an integer a a, the inverse iterate counting function π a, 5 ​ ( x) \pi_{a,5}(x) counts the number of integers n n with | n | ≤ x |n|\leq x that contain a a in their forward orbit under the 3 ​ x + 1 3x+1 function. That is

 | π a, 5 ( x):= #{ n: | n | ≤ x such that some T 5 ( k) ( n) = a, k ≥ 0 }. \pi_{a,5}(x):=\#\{n:~|n|\leq x~~\mbox{such~that~some}~T_{5}^{(k)}(n)=a,~k\geq 0\}. |  | (7.87) |

The inverse tree methods for the 3 ​ x + 1 3x+1 problem carry over to the 5 ​ x + 1 5x+1 problem, so that one can obtain a result qualitatively of the following type, by similar proofs.

###### Theorem 7.6

(Inverse Iterate Lower Bound) There is a positive constant c 1 c_{1} such that the following holds. For each a ≢ 0 ( mod 5) a\not\equiv~0~(\bmod~5), there is some x 0 ​ ( a) x_{0}(a) such that for all x ≥ x 0 ​ ( a) x\geq x_{0}(a),

 | π a, 5 ​ ( x) ≥ x c 1. \pi_{a,5}(x)\geq x^{c_{1}}. |  | (7.88) |

The following statistics measure the size of the inverse iterate set in the sense of fractional dimension.

###### Definition 7.8

Given an integer a a, the upper and lower 5 ​ x + 1 5x+1 growth exponents for a a are given by

 | η 5 + ​ ( a):= lim sup x → ∞ log ⁡ π a, 5 ​ ( x) log ⁡ x, \eta_{5}^{+}(a):=\limsup_{x\to\infty}\frac{\log\pi_{a,5}(x)}{\log x}, |  |

and

 | η 5 − ​ ( a):= lim inf x → ∞ log ⁡ π a, 5 ​ ( x) log ⁡ x. \eta_{5}^{-}(a):=\liminf_{x\to\infty}\frac{\log\pi_{a,5}(x)}{\log x}. |  |

If these quantities are equal, we define the 5 ​ x + 1 5x+1 growth exponent η 5 ​ ( a) \eta_{5}(a) to be η 5 ​ ( a) = η 5 + ​ ( a) = η 5 − ​ ( a) \eta_{5}(a)=\eta_{5}^{+}(a)=\eta_{5}^{-}(a).

In parallel with conjectures for the 3 ​ x + 1 3x+1 map, we formulate the following conjecture.

###### Conjecture 7.2

( 5 ​ x + 1 5x+1 Growth Exponent Conjecture) For all integers a ≢ 0 ( mod 5) a\not\equiv 0~(\bmod~5), the 3 ​ x + 1 3x+1 growth exponent η 5 ​ ( a) \eta_{5}(a) exists, and takes a constant value η 5 \eta_{5} independent of a a. This value satisfies

 | η 5 < 1. \eta_{5}<1. |  | (7.89) |

The stochastic models discussed in § 8 suggest that the constant η 5 \eta_{5} exists and takes a value strictly smaller than 1 1. There is some controversy concerning the conjectured value of the constant. In § 8 we present a repeated random walk model and a branching random walk model that both suggest the value η 5 ≈ 0.649 \eta_{5}\approx 0.649. A different branching random walk model formulated by Volkov [40] suggests the value η 5 ≈ 0.678 \eta_{5}\approx 0.678. Lower bounds toward this conjecture can be rigorously established, cf. Theorem 7.6 above. We have not bothered to determine c 1 c_{1} in ( 7.88), though we suspect it is well below either of the above predictions, and hence cannot distinguish between them.

## 8 5 ​ x + 1 5x+1 Function: Stochastic Models and Results

We now discuss stochastic models for the 5 ​ x + 1 5x+1 problem paralleling those for the 3 ​ x + 1 3x+1 problem. These include random walk models for forward iteration of the 5 ​ x + 1 5x+1 map, analysis of the accelerated 5 ​ x + 1 5x+1 map, and branching random walks for the backwards iteration of the 5 ​ x + 1 5x+1 map.

### 8.1 5 ​ x + 1 5x+1 Forward Iteration: Multiplicative Random Product Model

Concerning forward iteration, we may formulate a multiplicative random product model parallel to that in § 3. Consider the random products

 | Y k:= X 1 X 2 ⋯ X k, Y_{k}:=X_{1}X_{2}\cdots X_{k}, |  |

in which the X i X_{i} are each independent identically distributed (i.i.d.) random variables X i X_{i} having the discrete distribution

 | X i = { 5 2 with probability ​ 1 2, 1 2 with probability ​ 1 2. X_{i}=\left\{\begin{array}[]{cl}\displaystyle\frac{5}{2}&\mbox{with~probability}~~\frac{1}{2},\\ \\ \displaystyle\frac{1}{2}&\mbox{with~probability}~~\frac{1}{2}.\\ \end{array}\right. |  |

We call this the 5 ​ x + 1 5x+1 multiplicative random product (MRP) model.

As before, this model does not include the choice of starting value of the iteration, which would correspond to X 0 X_{0}; the random variable Y k Y_{k} really models the ratio T 5 ( k) ​ ( X 0) X 0 \frac{T_{5}^{(k)}(X_{0})}{X_{0}}. We define for λ + ≥ 1 \lambda^{+}\geq 1 the λ + \lambda^{+} -stopping time random variable

 | V λ + ​ ( ω):= inf { k: Y k ≥ λ }. V_{\lambda}^{+}(\omega):=\inf\{k:~Y_{k}\geq\lambda\}. |  | (8.90) |

where ω = ( X 1, X 2, X 3, ⋯) \omega=(X_{1},X_{2},X_{3},\cdots) denotes a sequence of random variables as above. This random vector ω \omega models the change in size of a random starting value n = X 0 n=X_{0} that occurs on iteration of the 5 ​ x + 1 5x+1 map.

This stochastic model can be used to exactly account for the density of λ + \lambda^{+} -stopping times, as follows.

###### Theorem 8.1

( λ + \lambda^{+} -Stopping Time Density Formula) For the 5 ​ x + 1 5x+1 map T 5 ​ ( n) T_{5}(n) and any fixed λ > 1 \lambda>1, the natural density 𝔻 ​ ( S λ ​ ( k)) {{D}}(S_{\lambda}(k)) for integers having λ + \lambda^{+} -stopping time at most k k is given exactly by the formula

 | 𝔻 ( S λ + ( k)) = ℙ [V λ + ( ω) ≤ k], {{D}}(S_{\lambda}^{+}(k))={{P}}[V_{\lambda}^{+}(\omega)\leq k], |  | (8.91) |

in which V λ + V_{\lambda}^{+} is the λ + \lambda^{+} -stopping time random variable in the multiplicative random product (MRP) model.

#### Proof.

This follows by a parallel argument to that in Borovkov and Pfeifer [10, Theorem 3] for the 3 ​ x + 1 3x+1 problem.

Theorem 8.1 is the stochastic model parallel of Theorem 7.2.

### 8.2 5 ​ x + 1 5x+1 Forward Iteration: Additive Random Walk Model

We next formulate additive random walk models, obtained after logarithmic rescaling of the 5 ​ x + 1 5x+1 iteration. The 5 ​ x + 1 5x+1 iteration takes x 0 = n x_{0}=n and x k = T 5 ( k) ​ ( n). x_{k}=T_{5}^{(k)}(n). Using a logarithmic rescaling with y k = log ⁡ x k y_{k}=\log x_{k} (natural logarithm) we have

 | y k = log ⁡ x k:= log ⁡ T ( k) ​ ( n). y_{k}=\log x_{k}:=\log T^{(k)}(n). |  |

Then we have

 | y k + 1 = { y k + log ⁡ 5 2 + e k if ​ x ≡ 1 ( mod 2), y k + log ⁡ 1 2 if ​ x ≡ 0 ( mod 2), y_{k+1}=\left\{\begin{array}[]{cl}y_{k}+\log\frac{5}{2}+e_{k}&\mbox{if}~x\equiv 1~~(\bmod~2),\\ \\ y_{k}+\log\frac{1}{2}&\mbox{if}~~x\equiv 0~~(\bmod~2),\end{array}\right. |  | (8.92) |

with

 | e k:= log ⁡ ( 1 + 1 5 ​ x k). e_{k}:=\log\left(1+\frac{1}{5x_{k}}\right). |  | (8.93) |

Here e k e_{k} is small as long as | x k | |x_{k}| is large.

We approximate the deterministic process above with the following random walk model with unequal size steps. We take random variables

 | W k:= − log ⁡ 2 + δ k ​ log ⁡ 5, W_{k}:=-\log 2+\delta_{k}\log 5, |  |

in which δ k \delta_{k} are i.i.d. Bernoulli random variables. The random walk positions { Z k: k ≥ 0 }, \{Z_{k}:k\geq 0\}, are then random variables having starting value Z 0 = log ⁡ m Z_{0}=\log m, for some fixed initial condition m > 1 m>1, and with

 | Z k = Z 0 + W 1 + W 2 + ⋯ + W k. Z_{k}=Z_{0}+W_{1}+W_{2}+\cdots+W_{k}. |  |

The Z k Z_{k} define a biased random walk, whose expected drift μ \mu is given by

 | μ:= E [W k)] = − log 2 + 1 2 log 5 = 1 2 log ( 5 4) ≈ 0.11157. \mu:=E[W_{k})]=-\log 2+\frac{1}{2}\log 5=\frac{1}{2}\log\left(\frac{5}{4}\right)\approx 0.11157. |  |

The variance σ \sigma of each step is given by

 | σ:= Var ⁡ [W k] = 1 2 ​ log ⁡ 5 ≈ 0.80472. \sigma:={\rm Var}[W_{k}]=\frac{1}{2}\log 5\approx 0.80472. |  |

Call this random walk the 5 ​ x + 1 5x+1 Biased Random Walk Model ( 5 ​ x + 1 5x+1 BRW Model).

Since the mean of this random walk is positive, this biased random walk has a positive drift. This positive drift implies that a random trajectory diverges with probability one.

###### Theorem 8.2

For the 5 ​ x + 1 5x+1 BRW model, with probability one, a trajectory { Z k: k ≥ 0 } \{Z_{k}:k\geq 0\} diverges to + ∞ +\infty.

#### Proof.

This is an elementary fact about random walks with positive drift.

This result implies that a generic trajectory has total stopping time equal to + ∞ +\infty. That is, starting from Z 0 = log ⁡ n Z_{0}=\log n, the probability ℙ ⁡ [E n] {{P}}[E_{n}] of the event E n E_{n} that for some k ≥ 1 k\geq 1, the total stopping time condition Z k ≤ 0 Z_{k}\leq 0 is satisfied, is strictly smaller than 1 1, i.e., ℙ ⁡ [E n] < 1 {{P}}[E_{n}]<1. It is positive but decreases to 0 0 as n n increases to + ∞ +\infty. (To not confuse this fact with Theorem 8.2, even if Z k Z_{k} dips below 0 0, it charges back up to infinity, almost surely.)

To obtain a result parallel to those of § 3 on the average behavior of numbers n n having a finite total stopping time, one needs to condition on the set of n n that have a finite total stopping time. This appears an approachable problem, but requires a more complicated analysis than that given in [23] or Borovkov and Pfeifer [10].

### 8.3 5 ​ x + 1 5x+1 Forward Iteration: Repeated Random Walk Model

Next, paralleling § 4, we formulate a 5 ​ x + 1 5x+1 Repeated Random Walk (RRW) model as follows. A model trial is the countable set of random variables

 | ω:= { Z k, n: k ≥ 0, n ≥ 1 }, \omega:=\{Z_{k,n}:k\geq 0,n\geq 1\}, |  | (8.94) |

having initial condition Z 0, n = log ⁡ n Z_{0,n}=\log n, with the individual random walks being 5 ​ x + 1 5x+1 biased random walks, as above. In the following subsections we consider other predictions that RRW model makes for various statistics.

###### Theorem 8.3

For the 5 ​ x + 1 5x+1 RRW model, with probability one, for every n ≥ 1 n\geq 1 the trajectory { Z k, n: k ≥ 0 } \{Z_{k,n}:k\geq 0\} diverges to + ∞ +\infty.

#### Proof.

This follows immediately from Theorem 8.2, since the complement of this event is a countable union of measure zero events.

One might misinterpret the above as suggesting that the 5 ​ x + 1 5x+1 RRW model predicts that all trajectories are unbounded. Of course this is an incorrect prediction. The 5 ​ x + 1 5x+1 iteration has some finite cycles, and furthermore there are infinite number of integers that eventually enter one of these cycles. The stochastic model above cannot account for such bounded trajectories! Instead we interpret the stochastic model prediction to be that a density one set of integers lie on unbounded trajectories.

This should make you very worried about relying on stochastic models to predict that 3 ​ x + 1 3x+1 trajectories decay! There could potentially be a set of measure zero escaping to infinity, which the model simply cannot see. Such a pathological trajectory is the heart and soul of the 3 ​ x + 1 3x+1 problem, and root cause of its difficulty!

### 8.4 5 ​ x + 1 5x+1 RRW Model Prediction: Minimum Excursion Constant

The 5 ​ x + 1 5x+1 RRW model has the following analogues of minimal excursion values and of the minimum excursion constant.

###### Definition 8.1

For a realization ω = { Z k, n: k ≥ 0, n ≥ 1 } \omega=\{Z_{k,n}:k\geq 0,n\geq 1\} of the 5 ​ x + 1 5x+1 RRW model, the minimal excursion value t − ​ ( n, ω) t^{-}(n,\omega) is given, for each n ≥ 1 n\geq 1, by

 | t − ​ ( n, ω):= inf { e Z k, n: k ≥ 0 }. t^{-}(n,\omega):=\inf\{e^{Z_{k,n}}:k\geq 0\}. |  | (8.95) |

Theorem 8.3 implies that with probability one the value t − ​ ( n, ω) t^{-}(n,\omega) is well-defined and strictly positive.

###### Definition 8.2

For a realization ω \omega of the 5 ​ x + 1 5x+1 RRW model, the minimum excursion constant ρ 5 − ​ ( ω) \rho_{5}^{-}(\omega) is given by

 | ρ 5 − ​ ( ω):= lim inf n → ∞ log ⁡ t − ​ ( n, ω) log ⁡ n. \rho_{5}^{-}(\omega):=\liminf_{n\to\infty}\frac{\log t^{-}(n,\omega)}{\log n}. |  | (8.96) |

Now a large deviations analysis yields the following result.

###### Theorem 8.4

( 5 ​ x + 1 5x+1 RRW Minimum Excursion Constant) For the 5 ​ x + 1 5x+1 RRW model, with probability one the quantities t − ​ ( n, ω) t^{-}(n,\omega) are finite for every n ≥ 1 n\geq 1. In addition, with probability one the random quantity

 | ρ 5, R ​ R ​ W − ​ ( ω):= lim inf n → ∞ log ⁡ t − ​ ( n, ω) log ⁡ n = lim inf n → ∞ ( inf k ≥ 0 Z k, n log ⁡ n) \rho_{5,RRW}^{-}(\omega):=\liminf_{n\to\infty}\frac{\log t^{-}(n;\omega)}{\log n}=\liminf_{n\to\infty}\left(\inf_{k\geq 0}\frac{Z_{k,n}}{\log n}\right) |  | (8.97) |

equals the constant

 | ρ 5, R ​ R ​ W − = 1 − 1 θ ∗ ≈ − 1.86466, \rho_{5,RRW}^{-}=1-\frac{1}{\theta^{\ast}}\approx-1.86466, |  | (8.98) |

in which θ ∗ ≈ 0.3490813 \theta^{\ast}\approx 0.3490813 is the larger of the two real roots of the equation M 5, R ​ R ​ W ​ ( θ) = 1 M_{5,RRW}(\theta)=1, where M 5, R ​ R ​ W ​ ( θ):= 1 2 ​ ( 2 θ + ( 2 5) θ) M_{5,RRW}(\theta):=\frac{1}{2}\left(2^{\theta}+(\frac{2}{5})^{\theta}\right) is a moment generating function associated to the random walk.

#### Proof.

This is proved by a large deviations argument similar to that used for the maximum excursion constant for the 3 ​ x + 1 3x+1 problem in Lagarias and Weiss [23, Theorem 2.3]. We sketch the main computation. We estimate the probability P ⁡ ( r, H, x) P(r,H,x) on a single trial starting at log ⁡ x \log x of having

 | − Z r ​ log ⁡ x, log ⁡ x ≥ H ​ log ⁡ x. -Z_{r\log x,\log x}\geq H\log x. |  |

We define a a by the condition H = a ​ r H=ar and find that the probability is given by Chernoff’s bound as

 | P ⁡ ( r, H, x) = exp ⁡ ( − g 5, R ​ R ​ W ​ ( a) ​ r ​ log ⁡ x ⁡ ( 1 + o ⁡ ( 1)) CLOSE, P(r,H,x)=\exp\left(-g_{5,RRW}(a)r\log x(1+o(1)\right), |  |

in which

 | g 5, R ​ R ​ W ​ ( a):= sup θ ∈ ℝ ( a ​ θ − log ⁡ M 5, R ​ R ​ W ​ ( θ)) g_{5,RRW}(a):=\sup_{\theta\in{{R}}}\left(a\theta-\log M_{5,RRW}(\theta)\right) |  | (8.99) |

is a large deviations rate function, which is the Legendre transform of the logarithm of the moment generating function OPEN M 5, R ​ R ​ W ​ ( θ) = 1 2 ​ ( 2 θ + 5 2) θ) M_{5,RRW}(\theta)=\frac{1}{2}\left(2^{\theta}+\frac{5}{2})^{\theta}\right). The repeated random walk makes x x trials 1 ≤ n ≤ x 1\leq n\leq x so the probability of a success over these trials is x ​ P ​ ( r, H, x) xP(r,H,x), and we want this to be at least x ϵ x^{\epsilon}, so that a success occurs infinitely often as x → ∞. x\to\infty. (We also will let ϵ → 0 \epsilon\to 0, so we set it equal to zero in what follows.) We want therefore to maximize H = a ​ r H=ar subject to the constraint that g 5, R ​ R ​ W ​ ( a) ​ r ≤ 1 g_{5,RRW}(a)r\leq 1. To maximize we may take g ⁡ ( a) ​ r = 1 g(a)r=1, whence r = 1 g ⁡ ( a) r=\frac{1}{g(a)} can be used to eliminate the variable r r. We now have the maximization problem to maximize H:= a g 5, R ​ R ​ W ​ ( a) H:=\frac{a}{g_{5,RRW}(a)} over 0 < a < ∞. 0<a<\infty. One finds an extremality condition for maximization which yields

 | H ∗ = 1 θ ⁡ ( a ∗), H^{\ast}=\frac{1}{\theta(a^{\ast})}, |  |

where a ∗ a^{\ast} achieves the maximum, and θ ∗ \theta^{\ast} is the corresponding value in the Legendre transform. Uniqueness of the maximum follows from convexity properties of the function log ⁡ M R ​ R ​ W ​ ( θ) \log M_{RRW}(\theta). Detailed error estimates are also needed to verify that this the maximum gives the dominant contribution.

This constant ρ 5, R ​ R ​ W − \rho_{5,RRW}^{-} found in Theorem 8.4 is negative, i.e. the minimum excursion in the model reaches a real number much smaller than 1 1! As a prediction for the 5 ​ x + 1 5x+1 problem, this disagrees with the exact answer for minimum excursion constant for the 5 ​ x + 1 5x+1 problem ρ 5 − = 0 \rho_{5}^{-}=0 given in Theorem 7.4.

We view this inaccurate prediction as stemming from the discrepancy that the 5 ​ x + 1 5x+1 function takes only values on the integer lattice, and that its additive correction term is not accounted for in this stochastic model. That is, the stochastic model will not necessarily make good predictions on behavior of an orbit once an orbit reaches a small value, e.g. | x | < C |x|<C for any fixed constant C C. We may hope that the 5 ​ x + 1 5x+1 model still makes an accurate prediction concerns the question: how many integers reach some small value, for example reaching the interval | x | < C |x|<C.

### 8.5 5 ​ x + 1 5x+1 RRW Model Prediction: Total Stopping Time Counts

We can interpret the false prediction above for minimum excursions in a constructive way: as soon as a 5 ​ x + 1 5x+1 trajectory achieves a size e Z k, n < 1 e^{Z_{k,n}}<1, it enters a periodic orbit. Therefore this condition can be treated as a “stopping time” condition that detects when a trajectory reaches the value 1 1.

###### Theorem 8.5

( 5 ​ x + 1 5x+1 RRW Total Stopping Time Counts) For the 5 ​ x + 1 5x+1 RRW model and for a given ω \omega, let

 | S ∞ ​ ( ω):= { n ≥ 1: e Z k, n < 1 ​ holds for some ​ k ≥ 1 }. S_{\infty}(\omega):=\{n\geq 1:~~e^{Z_{k,n}}<1~\mbox{holds~for some}~~k\geq 1\}. |  |

Collect those seeds n n whose trajectory according to ω \omega “reaches 1”. Let π 5 ​ ( ⋅, ω) \pi_{5}(\,\cdot\,;\omega) denote the corresponding counting function,

 | π 5 ​ ( x, ω):= #⁡ { 1 ≤ n ≤ x: n ∈ S ∞ ​ ( ω) }. \pi_{5}(x;\omega):=\#\{1\leq n\leq x:n\in S_{\infty}(\omega)\}. |  |

Then

 | lim x → ∞ log ⁡ π 5 ​ ( x, ω) log ⁡ x = η 5, R ​ R ​ W, for almost every ω. \lim_{x\to\infty}\frac{\log\pi_{5}(x;\omega)}{\log x}=\eta_{5,RRW},\qquad\mbox{ for almost every }\omega. |  |

Here η 5, R ​ R ​ W ≈ 0.65049 \eta_{5,RRW}\approx 0.65049 is given by η 5, R ​ R ​ W = 1 − θ 5, R ​ R ​ W \eta_{5,RRW}=1-\theta_{5,RRW} where θ 5, R ​ R ​ W ≈ 0.34951 \theta_{5,RRW}\approx 0.34951 is the unique positive solution to the equation

 | M 5, R ​ R ​ W ​ ( θ):= 1 2 ​ ( 2 θ + ( 5 2) θ) = 1. M_{5,RRW}(\theta):=\frac{1}{2}\left(2^{\theta}+\left(\frac{5}{2}\right)^{\theta}\right)=1. |  | (8.100) |

#### Proof.

This can be proved by a large deviations model similar in nature to those considered in Lagarias and Weiss [23, Theorem 2.4]. We sketch the main estimate. For k = r ​ log ⁡ x k=r\log x, consider the probability P ⁡ ( r, x) P(r,x) that for a single random walk e Z k, log ⁡ x < 1. e^{Z_{k,\log x}}<1. Since we make x x draws for 1 ≤ n ≤ x 1\leq n\leq x in the repeated random walk, the expected number of such individuals satisfying this property will be x ​ P ​ ( r, x) xP(r,x). This probability is estimated using Chernoff’s bound to be

 | P ⁡ ( r, x) = exp ⁡ ( − g 5, R ​ R ​ W ​ ( a) ​ r ​ log ⁡ x ⁡ ( 1 + o ⁡ ( 1)) CLOSE, P(r,x)=\exp\left(-g_{5,RRW}(a)r\log x(1+o(1)\right), |  |

where a = 1 r a=\frac{1}{r}, and g 5, R ​ R ​ W g_{5,RRW} is the large deviations rate function ( 8.99) in Theorem 8.4. We now maximize this probability over r r. To do this we eliminate r r using r = 1 a r=\frac{1}{a}, so we want to determine

 | τ 5, R ​ R ​ W:= min 0 ≤ a < ∞ ⁡ g 5, R ​ R ​ W ​ ( a) a. \tau_{5,RRW}:=\min_{0\leq a<\infty}{\frac{g_{5,RRW}(a)}{a}}. |  |

Then we obtain x ​ P ​ ( r, x) ≤ x 1 − τ 5, R ​ R ​ W + o ⁡ ( 1) xP(r,x)\leq x^{1-\tau_{5,RRW}+o(1)} for all r r, with equality holding for r = 1 a ∗ r=\frac{1}{a^{\ast}} where a ∗ a^{\ast} be the value that attains the maximum of f ⁡ ( a):= g 5, R ​ R ​ W ​ ( a) a f(a):=\frac{g_{5,RRW}(a)}{a} taken on the positive half-line. The extremality conditions for the minimum leads to the condition M R ​ R ​ W ​ ( θ ⁡ ( a ∗)) = 1, M_{RRW}(\theta(a^{\ast}))=1, where θ \theta is the Legendre transform variable, and also to the identity

 | τ 5, R ​ R ​ W = g 5, R ​ R ​ W ​ ( a ∗) a ∗ = θ ⁡ ( a ∗):= θ 5, R ​ R ​ W. \tau_{5,RRW}=\frac{g_{5,RRW}(a^{\ast})}{a^{\ast}}=\theta(a^{\ast}):=\theta_{5,RRW}. |  |

The strict convexity of the function log ⁡ M R ​ R ​ W ​ ( θ) \log M_{RRW}(\theta) is used to get a unique minimum, with η 5, R ​ R ​ W = 1 − τ 5, R ​ R ​ W \eta_{5,RRW}=1-\tau_{5,RRW}. For a rigorous proof, one must control various error estimates to show the dominant contribution to the probability comes from a small region near a ∗ a^{\ast}.

#### Remark.

The value of θ 5, R ​ R ​ W \theta_{5,RRW} in the minimization problem in the proof of Theorem 8.5 turns out to be identical to that in the maximization problem that is needed for proving Theorem 8.4.

### 8.6 5 ​ x + 1 5x+1 Accelerated Forward Iteration: Brownian Motion.

Kontorovich and Sinai [18] extended the Structure Theorem (that is, Theorems 5.1 and 5.2) and the consequences on the Central Limit Theorem (Theorem 5.4) and geometric Brownian motion (Theorem 5.5) to a class of functions which they called ( d, g, h) (d,g,h) -maps. The case d = 2 d=2, g = 5 g=5, and h = 1 h=1 corresponds to the accelerated 5 ​ x + 1 5x+1 function, U 5 ​ ( n) U_{5}(n).

The analogous distribution and Central Limit Theorems are proved in the same way, leading to the following.

###### Theorem 8.6

(Geometric Brownian Motion) The rescaled paths of the accelerated 5 ​ x + 1 5x+1 map are those of a geometric Brownian motion with drift log ⁡ ( 5 4) \log(\frac{5}{4}). By this we mean the following.

For an initial seed x 0 x_{0} which is relatively prime to both 2 2 and 5 5, denote its iterates by x k:= U 5 ( k) ​ ( x 0) x_{k}:=U_{5}^{(k)}(x_{0}), let y k:= log ⁡ x k y_{k}:=\log x_{k} and define the scaled variable

 | ω k:= y k − y 0 − k ​ log ⁡ ( 5 4) 2 ​ k ​ log ⁡ 2. \omega_{k}:={y_{k}-y_{0}-k\log(\frac{5}{4})\over\sqrt{2k}\log 2}. |  |

Partition the interval [0, 1] [0,1] as 0 = t 0 < t 1 < ⋯ < t r = 1 0=t_{0}<t_{1}<\cdots<t_{r}=1, and set k j = ⌊ t j ​ k ⌋ k_{j}=\lfloor t_{j}k\rfloor. Then for any a j < b j a_{j}<b_{j}, j = 1, …, r j=1,\dots,r,

 | lim k → ∞ ℙ [x 0: a j < ω k j − ω k j − 1 < b j, for all j = 1, 2, …, r] = ∏ j = 1 r ( Φ ( b j) − Φ ( a j)), \lim_{k\to\infty}{{P}}\left[x_{0}:a_{j}<{\omega_{k_{j}}-\omega_{k_{j-1}}}<b_{j},\mbox{ for all }j=1,2,\dots,r\right]=\prod_{j=1}^{r}\bigg(\Phi(b_{j})-\Phi(a_{j})\bigg), |  |

where Φ ⁡ ( a) \Phi(a) is the cumulative distribution function for the standard normal distribution.

#### Proof.

This is a consequence of Theorem 5 in Kontorovich-Sinai [18].

#### Remark.

The accelerated drift, log ⁡ ( 5 4) \log(\frac{5}{4}), is again double that of the Biased Random Walk model, which predicts a drift of 1 2 ​ log ⁡ ( 5 4) \frac{1}{2}\log(\frac{5}{4}). A zero-mean, unit-variance Wiener process W t W_{t} satisfies the “law of iterated logs” almost surely, that is:

 | lim sup t → ∞ | W t | 2 ​ t ​ log ⁡ log ⁡ t = 1, \limsup_{t\to\infty}{|W_{t}|\over\sqrt{2t\log\log t}}=1, |  |

with probability 1 1. Hence the drift being positive implies that almost every 5 ​ x + 1 5x+1 trajectory escapes to infinity (yet we emphasize again that we do not know how to prove this for a single given trajectory!).

### 8.7 5 ​ x + 1 5x+1 Backwards Stochastic Models: Branching Random Walks

We next formulate branching random walks to model the 5 ​ x + 1 5x+1 iteration in exact analogy with the 3 ​ x + 1 3x+1 models. We denote these models ℬ ⁡ [5 j] {\cal B}[5^{j}] for j ≥ 0 j\geq 0.

5 ​ x + 1 5x+1 Branching Random walk ℬ ⁡ [5 0] {\cal B}[5^{0}]. There is one type of individual. With probability 4 5 \frac{4}{5} an individual has a single offspring located at a position shifted by log ⁡ 2 \log 2 on the line from its progenitor, and with probability 1 5 \frac{1}{5} it has two offspring located at positions shifted log ⁡ 2 \log 2 and log ⁡ 2 5 \log\frac{2}{5} on the line from their progenitor. If the progenitor is in generation k − 1 k-1, the offspring are in generation k k. The tree is grown from a single individual in generation 0 0, the root, with specified initial location log ⁡ a \log a.

The more general models for j ≥ 1 j\geq 1 are given as follows.

5 ​ x + 1 5x+1 Branching Random walk ℬ ⁡ [5 j], ( j ≥ 1) {\cal B}[5^{j}],(j\geq 1). There are p = 4 ⋅ 5 j − 1 p=4\cdot 5^{j-1} types of individuals, indexed by residue classes a ( mod 5 j) a~(\bmod~5^{j}) with a ≢ 0 ( mod 5) a\not\equiv 0~(\bmod~5). The distribution of offspring of an individual of type a ( mod 5 j) a~(\bmod~5^{j}), at any given generation (or depth) k k in the branching, is determined as follows: Suppose a ( mod 5 j) a~(\bmod~5^{j}) is the type of a node at depth k − 1 k-1. Now regard it as being, with probability 1 5 \frac{1}{5} each, one of the five possible residue classes a ~ ( mod 5 j + 1) \tilde{a}~(\bmod~5^{j+1}) consistent with its class ( mod 5 j) (\bmod~5^{j}). A tree of depth 1 1 having a ~ \tilde{a} as root node, then has either one or two progeny, at depth 1 1, given by ( T ∗) − 1 ​ ( a ~) (T^{\ast})^{-1}(\tilde{a}), whose node labels are well-defined classes ( mod 5 j) (\bmod~5^{j}), either 2 ​ a ~ 2\tilde{a} or, if it legally occurs, 2 ​ a ~ − 1 3 ( mod 5 j) \frac{2\tilde{a}-1}{3}(\bmod~5^{j}). The branching random walk then produces an individual of type 2 ​ a ~ 2\tilde{a} at generation k k whose position is additively shifted by log ⁡ 2 \log 2 from that of the generation k − 1 k-1 progenitor node of type a ~ \tilde{a} plus, if legal, another node of type 2 ​ a ~ − 1 5 ( mod 5 j) \frac{2\tilde{a}-1}{5}(\bmod~5^{j}), which is shifted in position by log ⁡ ( 2 5) \log(\frac{2}{5}) on the line from that of the generation k − 1 k-1 -node. The tree is grown from a single individual at depth 0 0, with specified type and location log ⁡ a \log a.

Just as in the 3 ​ x + 1 3x+1 branching random walk models, the behavior of the random walk part of the model can completely reconstructed from knowing the type of each node.

For the rest of this section, let ω \omega denote a single realization of such a branching random walk ℬ ⁡ [5 j] {\cal B}[5^{j}] which starts from a single individual ω 0, 1 \omega_{0,1} of type 1 ( mod 5 j) 1~(\bmod~5^{j}) at depth 0 0, with initial position label log ⁡ | a | \log|a|. Here ω \omega describes a particular infinite tree. We let N k ​ ( ω) N_{k}(\omega) denote the number of individuals at level k k of the tree. We let S ⁡ ( ω k, j) S(\omega_{k},j) denote the position of the j j -th individual at level k k in the tree, for 1 ≤ j ≤ N k ​ ( ω) 1\leq j\leq N_{k}(\omega).

These models are supercritical branching processes exactly as for the 3 ​ x + 1 3x+1 case: In every random realization ω \omega, the number of nodes at level d d grows exponentially in d d, and there are no extinction events.

In terms of growth of trees of inverse iterates, these models will accurately represent certain features of 5 ​ x + 1 5x+1 trees, and not others. They might accurately describe tree sizes. However these branching random walks very likely do not accurately model positions of inverse iterates of the 5 ​ x + 1 5x+1 in certain crucial ways. Namely, individuals whose branching walk position is negative (corresponding to a 5 ​ x + 1 5x+1 iteration value x x falling in the interval ( 0, 1) (0,1)) are where the correction term e k e_{k} in ( 8.93) in the 5 ​ x + 1 5x+1 iteration becomes significant, breaking the size connection of the model iterates and the 5 ​ x + 1 5x+1 iterates.

We now give some quantities of the trees associated to a realization ω \omega of the branching random walk ℬ ⁡ [5 j] {\cal B}[5^{j}]. We let N k:= N k ​ ( ω) N_{k}:=N_{k}(\omega) denote the number of individuals in generation k k, and let { ω k, i: 1 ≤ i ≤ N k ​ ( ω) } \{\omega_{k,i}:1\leq i\leq N_{k}(\omega)\} denote the set of all individuals in generation i i, ordered by their branching random walk locations on the line, denoted

 | L ⁡ ( ω k, 1) ≤ L ⁡ ( ω k, 2) ≤ ⋯ ≤ L ⁡ ( ω k, N k). L(\omega_{k,1})\leq L(\omega_{k,2})\leq\cdots\leq L(\omega_{k,N_{k}}). |  |

The size of the element ω k, i \omega_{k,i}, viewed as analogues of the 5 ​ x + 1 5x+1 iterates, is the exponentiated quantity

 | Z k, i:= e L ⁡ ( ω k, i). Z_{k,i}:=e^{L(\omega_{k,i})}. |  | (8.101) |

The branching random walk has the property that the sizes of most individuals in a tree will tend to get larger. (This initially seems rather surprising, but note that if a forward orbit is unbounded, then necessarily all backward orbits leading to it must be unbounded as well!) We are interested in individuals whose size under the 5 ​ x + 1 5x+1 iteration is around a given value x x. The tree models will detect individuals whose size is larger than x x.

In the following subsections we address for the 5 ​ x + 1 5x+1 branching random walk models the following questions.

1. What is the exponential growth rate of the quantities N k ​ ( ω) N_{k}(\omega), as a function of k k?

2. What is the maximum level k k that has some individual Z k, i ≤ x ​? Z_{k,i}\leq x? This requires analyzing the size of the first birth location L ⁡ ( ω k, 1) L(\omega_{k,1}).

3. How does the total number of individuals π 5 ​ ( x, ω) \pi_{5}(x;\omega) in the 5 ​ x + 1 5x+1 ttree having location Z k, i ≤ x Z_{k,i}\leq x grow as a function of x x?

### 8.8 Backwards Iteration Prediction: 5 ​ x + 1 5x+1 Tree Counts

The size of 5 ​ x + 1 5x+1 trees can be estimated for these models ℬ ⁡ [5 j] {\cal B}[5^{j}], as follows.

###### Theorem 8.7

( 5 ​ x + 1 5x+1 Stochastic Tree Size) For all j ≥ 0 j\geq 0 a realization ω \omega of a tree grown in the 5 ​ x + 1 5x+1 branching random walk model ℬ ⁡ [5 j] {\cal B}[5^{j}] satisfies

 | lim k → ∞ 1 k ​ ( log ⁡ N k ​ ( ω)) = log ⁡ ( 6 5), almost surely. \lim_{k\to\infty}\frac{1}{k}\left(\log N_{k}(\omega)\right)=\log\left(\frac{6}{5}\right),~~~~\mbox{almost ~surely.} |  | (8.102) |

#### Proof.

This is proved in exactly similar fashion to the 3 ​ x + 1 3x+1 stochastic model case in Lagarias and Weiss [23, Corollary 3.1]

This result only uses the Galton-Watson process branching structure built into the branching random walk ℬ ⁡ [5 j]. {\cal B}[5^{j}]. It does not depend on the sizes of the iterates.

The conclusion of Theorem 8.7, viewed as a prediction of the growth behavior of 5 ​ x + 1 5x+1 trees, is consistent with the rigourous results on average tree size for pruned 5 ​ x + 1 5x+1 trees given in Theorem 7.5.

### 8.9 Backwards Iteration Prediction: Extremal Finite Total Stopping Times

As indicated above, most integers for the 5 ​ x + 1 5x+1 map will not have a finite total stopping time. However it is of interest to analyze the small subset of integers that do have a total stopping time; these are exactly the integers in the tree of inverse iterates of a = 1 a=1. We analyze what is the maximum generation k k that contains an individual having size e L ⁡ ( ω k, i) ≤ x. e^{L(\omega_{k,i})}\leq x.

Denote the location of this first birth individual in generation k k by L k ∗ ​ ( ω):= L ⁡ ( ω k, 1) L_{k}^{\ast}(\omega):=L(\omega_{k,1}), for a given realization ω \omega of the random walk.

###### Theorem 8.8

(Asymptotic 5 ​ x + 1 5x+1 First Birth Location) There is a constant β 5, B ​ P \beta_{5,BP} such that, for all j ≥ 1 j\geq 1, the branching random walk model ℬ ⁡ [3 j] {\cal B}[3^{j}] has asymptotic first birth (leftmost birth)

 | lim k → ∞ 1 k ​ L k ∗ ​ ( ω) = β 5, B ​ P a. s. \lim_{k\to\infty}\frac{1}{k}L_{k}^{\ast}(\omega)=\beta_{5,BP}~~~~~\mbox{a.~s.} |  | (8.103) |

This constant β 5, B ​ P ≈ 0.01179816 \beta_{5,BP}\approx 0.01179816 is determined uniquely by the properties that it is the unique constant with β > 0 \beta>0 that satisfies

 | g ¯ 5, B ​ P ​ ( β) = 0, \overline{g}_{5,BP}(\beta)=0, |  | (8.104) |

where

 | g ¯ 5, B ​ P ​ ( a) \displaystyle\overline{g}_{5,BP}(a) | : ⁣ = \displaystyle:= | − sup θ ≤ 0 ( a θ − log ( 2 θ + 1 5 ( 2 5) θ)). \displaystyle-\sup_{\theta\leq 0}\left(a\theta-\log\left(2^{\theta}+\frac{1}{5}(\frac{2}{5})^{\theta}\right)\right). |  | (8.105) |

Figure 8.8: A plot of a a versus g ¯ 5, B ​ P ​ ( a) \bar{g}_{5,BP}(a), in the range log ⁡ ( 2 / 5) < a < 1 6 ​ log ⁡ ( 64 / 5) \log(2/5)<a<\frac{1}{6}\log(64/5). Figure 8.9: A plot of a a versus θ ∗ \theta^{*}, in the range log ⁡ ( 2 / 5) < a < 1 6 ​ log ⁡ ( 64 / 5) \log(2/5)<a<\frac{1}{6}\log(64/5).

#### Proof.

This is proved by an argument analogous to the 3 ​ x + 1 3x+1 case analyzed in Lagarias and Weiss [23, Theorem 3.4], cf. Theorem 6.3. Here we use a branching process (inverse) moment generating function

 | M 5, B ​ P ​ ( θ):= 2 θ + 1 5 ​ ( 2 5) θ. M_{5,BP}(\theta):=2^{\theta}+\frac{1}{5}\left(\frac{2}{5}\right)^{\theta}. |  | (8.106) |

in computing the rate function g ¯ 5, B ​ P ​ ( a) \overline{g}_{5,BP}(a). We note that g ¯ 5, B ​ P ​ ( a) \overline{g}_{5,BP}(a) is increasing for log ⁡ 2 5 < a < 1 6 ​ log ⁡ 64 5 \log\frac{2}{5}<a<\frac{1}{6}\log\frac{64}{5}, (see Figure 8.8) and on this range the value θ ∗:= θ ⁡ ( a) \theta^{*}:=\theta(a) achieving the extremum in ( 8.105) is an increasing function of a a, reaching the value θ = 0 \theta=0 at the upper endpoint (see Figure 8.9). We have g ¯ 5, B ​ P ​ ( a) = log ⁡ ( 6 5) \overline{g}_{5,BP}(a)=\log(\frac{6}{5}) for 1 6 ​ log ⁡ 64 5 ≤ a < ∞ \frac{1}{6}\log\frac{64}{5}\leq a<\infty.

Now one defines a branching random walk stopping limit

 | γ 5, B ​ P ​ ( ω):= lim sup k → ∞ k L k ∗ ​ ( ω). \gamma_{5,BP}(\omega):=\limsup_{k\to\infty}\frac{k}{L_{k}^{\ast}(\omega)}. |  |

Theorem 8.8 implies that this value is constant almost surely, equaling a value γ 5, B ​ P \gamma_{5,BP} given by

 | γ 5, B ​ P = 1 β 5, B ​ P ≈ 84.76012. \gamma_{5,BP}=\frac{1}{\beta_{5,BP}}\approx 84.76012. |  | (8.107) |

One can show the constants γ 5, B ​ P \gamma_{5,BP} and γ 5, R ​ R ​ W \gamma_{5,RRW} agree, just as for the 3 ​ x + 1 3x+1 stochastic models.

###### Theorem 8.9

( 5 ​ x + 1 5x+1 Random Walk-Branching Random Walk Duality) The 5 ​ x + 1 5x+1 repeated random walk (RRW) scaled stopping time limit γ 5, R ​ R ​ W \gamma_{5,RRW} and the branching random walk stopping limit γ 5, B ​ P \gamma_{5,BP} for the 5 ​ x + 1 5x+1 branching random walk (BP) model ℬ ⁡ [5 j] {\cal B}[5^{j}] with j = 0 j=0, are related by

 | γ 5, R ​ R ​ W = γ 5, B ​ P. \gamma_{5,RRW}=\gamma_{5,BP}. |  | (8.108) |

#### Proof.

This result is proved using a relation between moment generating functions

 | M 5, B ​ P ​ ( θ) = M 5, R ​ R ​ W ​ ( θ + 1), M_{5,BP}(\theta)=M_{5,RRW}(\theta+1), |  |

compare ( 8.100) and ( 8.105). It is identical in spirit to the proof in Lagarias and Weiss [23, Theorem 4.1].

The analogue of this result applied to the 5 ​ x + 1 5x+1 problem would be the following heuristic prediction: For any constant γ > γ 5, B ​ P \gamma>\gamma_{5,BP} all but finitely many trajectories having total stopping time σ ∞ ​ ( n) > γ ​ log ⁡ n \sigma_{\infty}(n)>\gamma\log n necessarily have σ ∞ ​ ( n) = + ∞ \sigma_{\infty}(n)=+\infty. We could take γ = 85 \gamma=85, for example.

### 8.10 Backwards Iteration Prediction: Total Preimage Counts

The following result gives, for the simplest branching random walk model ℬ ⁡ [5 0] {\cal B}[5^{0}], an almost sure asymptotic for the number of inverse iterates of size below a given bound.

###### Theorem 8.10

(Stochastic Inverse Iterate Counts) For a realization ω \omega of the branching random walk ℬ ⁡ [1] {\cal B}[1], let I ∗ ​ ( t, ω) I^{\ast}(t;\omega) count the number of progeny located at positions Z ⁡ ( ω k, j) ≤ x Z(\omega_{k,j})\leq x, i.e.

 | I ∗ ( x; ω):= #{ ω k, j: Z ( ω k, j) ≤ x, for any k ≥ 1, 1 ≤ j ≤ N k ( ω) }. I^{\ast}(x;\omega):=\#\{\omega_{k,j}:Z(\omega_{k,j})\leq x,\mbox{for~any}~~k\geq 1,~1\leq j\leq N_{k}(\omega)\}. |  | (8.109) |

This quantity satsfies with probability one the asymptotic estimate

 | I ∗ ​ ( x, ω) = x η 5, B ​ P + o ⁡ ( 1) ​ as ​ x → ∞, I^{\ast}(x;\omega)=x^{\eta_{5,BP}+o(1)}~~~\mbox{as}~~x\to\infty, |  | (8.110) |

in which η 5, B ​ P ≈ 0.650919 \eta_{5,BP}\approx 0.650919 is the maximum value of f ⁡ ( a):= 1 a ​ g ¯ 5, B ​ P ​ ( a) f(a):=\frac{1}{a}{\overline{g}_{5,BP}(a)} taken over the interval 0 ≤ a < 1 6 ​ log ⁡ 64 5 0\leq a<\frac{1}{6}\log\frac{64}{5}.

#### Proof.

This is proved by a large deviations argument similar to that used in Lagarias and Weiss [23, Theorem 4.2]. One counts the number of progeny at level k k for each level k k satisfying the bound, by estimating the probability that a random leaf satisfies the appropriate large deviations bound. One shows that this number peaks for k ≈ θ 5, B ​ P ​ log ⁡ x k\approx\theta_{5,BP}\log x, where θ 5, B ​ P = 1 a ∗ ≈ 9.19963, \theta_{5,BP}=\frac{1}{a^{\ast}}\approx 9.19963, where a ∗ ≈ 0.1087 a^{\ast}\approx 0.1087 is the value of a a achieving the maximum above. One shows that the right side is an upper bound for all levels k k, and that the sum total of levels k > 100 ​ log ⁡ x k>100\log x contribute negligibly to the sum.

The model statistic I ∗ ​ ( x, ω) I^{\ast}(x;\omega) functions as a proxy for the 5 ​ x + 1 5x+1 count function π a ∗ ​ ( x) \pi_{a}^{\ast}(x), where log ⁡ | a | \log|a| gives the position of the root node of the branching random walk. This result is the stochastic analogue of Conjecture 2.1 about the 3 ​ x + 1 3x+1 growth exponent. The argument above also makes the prediction is that the levels k k at which the bulk of the members of π a ​ ( x) \pi_{a}(x) occur has k ≈ 1 a ∗ ​ log ⁡ x k\approx\frac{1}{a^{\ast}}\log x.

#### Remark.

An entirely different set of branching random walk models has been developed by S. Volkov [40] to model the 5 ​ x + 1 5x+1 problem. Volkov models counting all non-divergent trajectories of the 5 ​ x + 1 5x+1 problem, which are those which enter some finite cycle, and denotes the number of these below x x by Q ⁡ ( x) Q(x). Thus π 5 ​ ( x) ≤ Q ​ ( x) \pi_{5}(x)\leq Q(x), and conjecturally these should be of similar orders of growth. It is expected there are finitely many cycles, and each should absorb roughly the same number of integers below x x, in the sense of the exponent in the power of x x involved.

Volkov’s branching process stochastic models grow a complete binary tree, rather than a tree that may have either one or two branches from each node, as in the models above. He suggests that the 5 ​ x + 1 5x+1 problem can be modeled by such trees, using an unusual encoding of the iterates (some edges encode several iteration steps of the inverse Collatz function). In order to do this, his node weights are chosen differently than above. He arrives at a predicted exponent η 5, B ​ P ∗ ≈ 0.678, \eta_{5,BP}^{\ast}\approx 0.678, which differs from the prediction η 5, B ​ P ≈ 0.650919 \eta_{5,BP}\approx 0.650919 made in Theorem 8.10 above. The empirical data Volkov presents seems insufficient to discriminate between these two predicted exponents. It would be interesting for this problem to be investigated further.

## 9 Benford’s Law for 3 ​ x + 1 3x+1 and 5 ​ x + 1 5x+1 Maps

Another curious statistic satisfied by the 3 ​ x + 1 3x+1 function was discovered by Kontorovich and Miller [17]: Benford’s Law.

In the late 1800s, Newcomb [29] noticed a surprising fact while perusing tables of logarithms: certain pages were significantly more worn than others. Numbers whose logarithm started with 1 were being referenced more frequently than other digits. Instead of observing one-ninth (about 11%) of entries having a leading digit of 1, as one would expect if the digits 1, 2, …, 9 1,2,\dots,9 were equally likely, over 30% of the entries had leading digit 1, and about 70% had leading digit less than 5. Since log 10 ⁡ 2 ≈ 0.301 \log_{10}2\approx 0.301 and log 10 ⁡ 5 ≈ 0.699 \log_{10}5\approx 0.699, Newcomb speculated that the probability of observing a digit less than k k was log 10 ⁡ k \log_{10}k. This logarithmic phenomenon became known as Benford’s Law after Benford [6] collected and in 1938 popularized extensive empirical evidence of this distribution in diverse data sets.

Benford’s law seems to hold for many sequences of numbers generated by dynamical systems having an “expanding” property, see Berger et al [7] and Miller and Takloo-Bighash [28, Chap. 9]. Benford behavior has been empirically observed for initial digits of the first iterates of the 3 ​ x + 1 3x+1 map or accelerated 3 ​ x + 1 3x+1 map for a randomly chosen initial number n n. Here we survey some rigorous theorems quantifying this statement, for initial iterates. Similar Benford results can be proved for the 5 ​ x + 1 5x+1 function.

We emphasize that the Benford law behavior quantifed here concerns behavior on a fixed finite set of initial iterates of these maps. Indeed, the 3 ​ x + 1 3x+1 conjecture predicts that Benford behavior cannot hold for the full infinite set of forward iterates, since conjecturally they become periodic! However it remains possible that a strong form of Benford behavior could hold on (infinite) divergent orbits of the 5 ​ x + 1 5x+1 problem.

### 9.1 Benford’s Law and Uniform Distribution of Logarithms

To make Benford’s law precise, we say that the mantissa function ℳ ⁡ ( n) ∈ [1, 10) {\cal M}(n)\in[1,10) is the leading entry of n n in “scientific notation”, that is, n = ℳ ⁡ ( n) ⋅ 10 ⌊ log 10 ⁡ n ⌋ n={\cal M}(n)\cdot 10^{{\lfloor\log_{10}n\rfloor}}. Benford’s law concerns the distribution of leading digit of the mantissa, while one can also consider the distribution of the lower order digits of the mantissa.

###### Definition 9.1

An infinite sequence { n 1, n 2, …, n k, … } \{n_{1},n_{2},\dots,n_{k},\dots\} satisfies the strong Benford’s Law (to base 10 10) if the logarithmic digit frequency holds for any order digits in the mantissa. That is, for any a ∈ [1, 10) a\in[1,10),

 | lim x → ∞ #⁡ { k ≤ x: ℳ ⁡ ( n k) < a } x = log 10 ( a). \lim_{x\to\infty}{\#\{k\leq x:{\cal M}(n_{k})<a\}\over x}=\log_{10}(a). |  | (9.111) |

The strong version of Benford’s law is well known to be equivalent to uniform distribution mod 1 \bmod~1 of the base 10 logarithms of the numbers in the sequence, cf. Diaconis [15, Theorem 1].

###### Theorem 9.1

(Strong Benford Law Criterion) A sequence { n 1, n 2, … } \{n_{1},n_{2},\dots\} satisfies the strong Benford’s Law (or “is strong Benford”) to base 10 10 if and only if the sequence { log 10 ⁡ n 1, log 10 ⁡ n 2, … } \{\log_{10}n_{1},\log_{10}n_{2},\dots\} is equidistributed ( mod 1) (\bmod~1), that is, for any a ∈ [0, 1) a\in[0,1),

 | lim x → ∞ #⁡ { k ≤ x: log 10 ⁡ n k ( mod 1) < a } x = a. \lim_{x\to\infty}{\#\{k\leq x:\log_{10}n_{k}(\bmod~1)<a\}\over{x}}=a. |  | (9.112) |

The definition and theorem above extend to expansions in any integer base B ≥ 2 B\geq 2. This result suggests the following general definition of strong Benford’s Law to any real base B > 1 B>1.

###### Definition 9.2

Let B > 1 B>1 be a real number. A sequence { n 1, n 2, …, n k, … } \{n_{1},n_{2},\dots,n_{k},\dots\} satisfies the strong Benford’s Law to base B B if and only if the sequence { log B ⁡ ( n 1), log B ⁡ ( n 2), … } \{\log_{B}(n_{1}),\log_{B}(n_{2}),...\} is uniformly distributed modulo one.

This definition is equivalent to the earlier one for integers expanded in a radix expansion to any base B > 1 B>1. One can similarly define the mantissa function to any real base B > 1 B>1, extending Definition 9.1.

Benford’s Law is stated for infinite sequences. However one can obtain approximate results that apply to finite sequences { x 1, x 2, …, x k } \{x_{1},x_{2},...,x_{k}\}, by using the following discrepancy measure of approximation to uniform distribution of such sequences.

###### Definition 9.3

Given a finite set 𝒴 = { y 1, …, y k } {\cal Y}=\{y_{1},\dots,y_{k}\} of size k k, for each 0 ≤ a < 1 0\leq a<1, set

 | 𝒟 ( 𝒴; a):= #⁡ { j ≤ k: y j ( mod 1) < a } k − a. {\cal D}({\cal Y};a):={\#\{j\leq k:y_{j}(\bmod~1)<a\}\over k}-a. |  |

The discrepancy 𝒟 ⁡ ( 𝒴) {\cal D}({\cal Y}) is defined by

 | 𝒟 ⁡ ( 𝒴):= sup 0 ≤ a < 1 𝒟 ⁡ ( 𝒴, a) − inf 0 ≤ a < 1 𝒟 ⁡ ( 𝒴, a). {\cal D}({\cal Y}):=\sup_{0\leq a<1}{\cal D}({\cal Y};a)-\inf_{0\leq a<1}{\cal D}({\cal Y};a). |  |

One always has 𝒟 ⁡ ( 𝒴) ≤ 1 {\cal D}({\cal Y})\leq 1. The smallest possible discrepancy of a finite set 𝒴 {\cal Y} is 𝒟 ⁡ ( 𝒴) = 1 / k {\cal D}({\cal Y})=1/k, attained by equally spaced elements y j = j k, 1 ≤ j ≤ k y_{j}=\frac{j}{k},~1\leq j\leq k.

A small discrepancy indicates that the set 𝒴 {\cal Y} is close to equidistributed modulo 1 1. In particular, for an infinite sequence 𝒳 = { x j: j ≥ 1 } {\cal X}=\{x_{j}:j\geq 1\}, if 𝒳 k = { x j: 1 ≤ j ≤ k } {\cal X}_{k}=\{x_{j}:1\leq j\leq k\} then 𝒳 {\cal X} is uniformly distributed ( mod 1) (\bmod~1) if and only if the discrepancies 𝒟 ⁡ ( 𝒳 k) → 0 {\cal D}({\cal X}_{k})\to 0 as k → ∞ k\to\infty.

### 9.2 Benford’s Law for 3 ​ x + 1 3x+1 Function Iterates

Kontorovich and Miller [17] considered iterates of the accelerated 3 ​ x + 1 3x+1 function U ⁡ ( n) U(n). Fix an odd integer n = n 0 n=n_{0}, and let { n 1, n 2, … } \{n_{1},n_{2},\dots\} be the sequence of iterates from the starting seed n 0 ∈ Π n_{0}\in\Pi, where Π \Pi consists of all positive integers relatively prime to 6 6. The main 3 ​ x + 1 3x+1 conjecture asserts that this sequence is eventually periodic, and hence it is impossible for ( 9.112) to hold!

The following was their interpretation of (weak) “Benford behavior” for the 3 ​ x + 1 3x+1 function:

###### Theorem 9.2

For x 0 = n ∈ Π x_{0}=n\in\Pi, denote its accelerated 3 ​ x + 1 3x+1 iterates by x k:= U ( k) ​ ( x 0) x_{k}:=U^{(k)}(x_{0}). Now set y k:= log 10 ⁡ x k y_{k}:=\log_{10}x_{k} and define the shifted variables

 | ω k:= y k − y 0 − k ​ log 10 ⁡ ( 3 4). \omega_{k}:={y_{k}-y_{0}-k\log_{10}\left(\frac{3}{4}\right)}. |  |

Then, for any a ∈ [0, 1) a\in[0,1),

 | lim k → ∞ 𝔻 Π [x 0: ω k ( mod 1) < a] = a. \lim_{k\to\infty}{{D}}_{\Pi}\bigg[x_{0}:~\omega_{k}(\bmod~1)<a\bigg]=a. |  |

#### Proof.

This is established as Theorem 5.3 in Kontorovich and Miller [17].

Arguably, the normalization from y k y_{k} to ω k \omega_{k} in Theorem 9.2 makes the above result only an approximation to “true” Benford behavior, which should be that 𝔻 Π [x 0: y k ( mod 1) < a] → a {{D}}_{\Pi}[x_{0}:~y_{k}~(\bmod~1)<a]\to a as k → ∞ k\to\infty.

Lagarias and Soundararajan [22] were able to use the non-accelerated 3 ​ x + 1 3x+1 function T T to show another approximation to Benford behavior, as follows.

###### Theorem 9.3

(Approximate Strong Benford’s Law for 3 ​ x + 1 3x+1 Map) Let B > 1 B>1 be any integer base. Then for a given N ≥ 1 N\geq 1 and each X ≥ 2 N X\geq 2^{N}, most initial starting values x 0 x_{0} in 1 ≤ x 0 ≤ X 1\leq x_{0}\leq X have first N N initial 3 ​ x + 1 3x+1 iterates { x k: 1 ≤ k ≤ N } \{x_{k}:1\leq k\leq N\} that satisfy the discrepancy bound

 | 𝒟 ⁡ ( { log B ⁡ x k ​ ( m ​ o ​ d ​ 1): 1 ≤ k ≤ N }) ≤ 2 ​ N − 1 36. {\cal D}\left(\{\log_{B}x_{k}(mod~1):1\leq k\leq N\}\right)\leq 2N^{-\frac{1}{36}}. |  | (9.113) |

The exceptional set ℰ ⁡ ( X, B) {\cal E}(X,B) of initial seeds x 0 x_{0} in 1 ≤ x 0 ≤ X 1\leq x_{0}\leq X that do not satisfy the bound has cardinality

 | | ℰ ⁡ ( X, B) | ≤ c ⁡ ( B) ​ N − 1 36 |{\cal E}(X,B)|\leq c(B)N^{-\frac{1}{36}} |  | (9.114) |

where c ⁡ ( B) c(B) is a positive constant depending only on the base B B.

#### Proof.

This is established as Theorem 2.1 in Lagarias and Soundararajan [22].

### 9.3 Benford’s Law for 5 ​ x + 1 5x+1 Function Iterates

The 5 ​ x + 1 5x+1 map also exhibits similar “Benford” behavior for its iterates. The results of [17] apply to general ( d, g, h) (d,g,h) -Maps, in particular, to the 5 ​ x + 1 5x+1 function, giving a direct analogue of Theorem 9.2.

The method of proof in [22] of Theorem 9.3 should also extend to give qualitatively similar results in the 5 ​ x + 1 5x+1 case. This proof relied on the Parity Sequence Theorem for the 3 ​ x + 1 3x+1 map which has an exact analogue for the 5 ​ x + 1 5x+1 map. The proof in [22] also used some Diophantine approximation results for the transcendental number α 3:= log 2 ⁡ 3 \alpha_{3}:=\log_{2}3, and qualitatively similar Diophantine approximation results are valid for α 5:= log 2 ⁡ 5 \alpha_{5}:=\log_{2}5 needed in the 5 ​ x + 1 5x+1 case.

These rigorous results concern only the initial iterates of 5 ​ x + 1 5x+1 trajectories. However since the 5 ​ x + 1 5x+1 map conjecturally has divergent orbits, it seems a plausible guess that a strong form of Benford behavior might hold on all infinite divergent orbits of the 5 ​ x + 1 5x+1 map.

## 10 2-Adic Extensions of 3 ​ x + 1 3x+1 and 5 ​ x + 1 5x+1 Maps

What happens if we put these probabilistic models in a more general context? We can obtain a perfect set of symbolic dynamics if we extend the domain of these maps to the 2 2 -adic integers. Such extensions are possible for both the 3 ​ x + 1 3x+1 map T 3 ​ ( x) T_{3}(x) and the 5 ​ x + 1 5x+1 map T 5 ​ ( x) T_{5}(x).

###### Theorem 10.1

The 3 ​ x + 1 3x+1 map T 3 T_{3} and the 5 ​ x + 1 5x+1 map T 5 T_{5} extend continuously from maps on the integers to maps on the 2 2 -adic integers ℤ 2 {{Z}}_{2}, viewing ℤ {{Z}} as a dense subset of ℤ 2 {{Z}}_{2}. Denoting the extensions by T ~ 3 \tilde{T}_{3} and T ~ 5 \tilde{T}_{5}, respectively, these maps have the following properties.

(i) Both maps T ~ 3 \tilde{T}_{3} and T ~ 5 \tilde{T}_{5} are homeomorphisms of ℤ 2 {{Z}}_{2} to itself.

(ii) Both maps T ~ 3 \tilde{T}_{3} and T ~ 5 \tilde{T}_{5} are measure-preserving maps on ℤ 2 {{Z}}_{2} for the standard 2 2 -adic measure μ 2 \mu_{2} on ℤ 2 {{Z}}_{2}.

(iii) Both maps T ~ 3 \tilde{T}_{3} and T ~ 5 \tilde{T}_{5} are strongly mixing with respect to the measure μ 2 \mu_{2}, hence ergodic.

#### Proof.

For the 3 ​ x + 1 3x+1 map, properties (i)-(iii) are stated in Lagarias [21, Theorem K]. The property of strong mixing is an ergodic-theoretic notion explained there. Akin [1] gives another proof of these facts for the 3 ​ x + 1 3x+1 map.

For the 5 ​ x + 1 5x+1 map, properties (i)-(iii) may be established by proofs similar to the 3 ​ x + 1 3x+1 map case. This is based on the fact that an analogue of Theorem 2.1 holds for the symbolic dynamics of iterating the 5 ​ x + 1 5x+1 map. It is also a corollary of results of Bernstein and Lagarias [9, Sect. 4], whose results imply that (i)-(iii) hold more generally for all a ​ x + b ax+b -maps. Here the a ​ x + b ax+b map T a, b T_{a,b} is

 | T a, b ​ ( x):= { a ​ x + b 2 if ​ x ≡ 1 ( mod 2), x 2 if ​ x ≡ 0 ( mod 2), T_{a,b}(x):=\left\{\begin{array}[]{cl}\displaystyle\frac{ax+b}{2}&\mbox{if}~~x\equiv 1~~(\bmod~2),\\ \\ \displaystyle\frac{x}{2}&\mbox{if}~~x\equiv 0~~(\bmod~2),\end{array}\right. |  |

where a a and b b are odd integers.

A much stronger ergodicity result is valid for the 2 2 -adic extensions of these maps. Define the 2 2 -adic shift map S: ℤ 2 → ℤ 2 S:{{Z}}_{2}\to{{Z}}_{2} to be the 2 2 -to- 1 1 map given for α = ∑ j = 0 ∞ a j ​ 2 j =. a 0 ​ a 1 ​ a 2 ​ … \alpha=\sum_{j=0}^{\infty}a_{j}2^{j}=.a_{0}a_{1}a_{2}..., with each a j = 0 a_{j}=0 or 1 1, by

 | S ( α) = S (. a 0 a 1 a 2 ⋯):=. a 1 a 2 a 3 ⋯ S(\alpha)=S(.a_{0}a_{1}a_{2}\cdots):=.a_{1}a_{2}a_{3}\cdots |  |

That is,

 | S ⁡ ( α) = { α − 1 2 if ​ α ≡ 1 ( mod 2) α 2 if ​ α ≡ 0 ( mod 2). S(\alpha)=\left\{\begin{array}[]{cl}\displaystyle\frac{\alpha-1}{2}&\mbox{if}~~\alpha\equiv 1~~(\bmod~2)\\ \\ \displaystyle\frac{\alpha}{2}&\mbox{if}~~\alpha\equiv 0~~(\bmod~2).\end{array}\right. |  | (10.115) |

This map has the 2 2 -adic measure as Haar measure, and is mixing in the strongest sense.

###### Theorem 10.2

The 2 2 -adic extensions T ~ 3 \tilde{T}_{3} of the 3 ​ x + 1 3x+1 map and T ~ 5 \tilde{T}_{5} of the 5 ​ x + 1 5x+1 map are each topologically conjugate to the 2 2 -adic shift map, by a conjugacy map Φ 3 \Phi_{3}, resp. Φ 5 \Phi_{5}. That is, these maps are homeomorphisms of ℤ 2 {{Z}}_{2} with Φ 3 − 1 ∘ T ~ 3 ∘ Φ 3 = S \Phi_{3}^{-1}\circ\tilde{T}_{3}\circ\Phi_{3}=S and 𝑂𝑃𝐸𝑁 Φ 5 − 1 ∘ ( ~ ​ T) 5 ∘ Φ 5 = S \Phi_{5}^{-1}\circ\tilde{(}T)_{5}\circ\Phi_{5}=S.

(1) The maps Φ j \Phi_{j}, j = 3 j=3 or 5 5, are solenoidal, i.e. for each n ≥ 1 n\geq 1 they have the property

 | x ≡ y ( mod 2 n) ⟶ Φ j ​ ( x) ≡ Φ j ​ ( y) ( mod 2 n). x\equiv y~(\bmod~2^{n})\longrightarrow\Phi_{j}(x)\equiv\Phi_{j}(y)~(\bmod~2^{n}). |  |

(2) The inverses of these conjugacy maps are explicitly given by

 | Φ j − 1 ​ ( α):= ∑ k = 0 ∞ ( T j ( k) ​ ( α) ( mod 2)) ​ 2 k, \Phi_{j}^{-1}(\alpha):=\sum_{k=0}^{\infty}\left(T_{j}^{(k)}(\alpha)~(\bmod~2)\right)2^{k}, |  |

for j = 3 j=3 or 5 5, and the residue ( mod 2) (\bmod~2) is taken to be 0 0 or 1 1.

#### Proof.

These results follow from Bernstein and Lagarias [9, Sect. 3, 4], where results are proved for a general class of mappings including both the 3 ​ x + 1 3x+1 map and 5 ​ x + 1 5x+1 map.

Theorem 10.2 immediately gives the following corollary.

###### Corollary 10.1

The 2 2 -adic extensions T ~ 3 \tilde{T}_{3} of the 3 ​ x + 1 3x+1 map and T ~ 5 \tilde{T}_{5} of the 5 ​ x + 1 5x+1 map are topologically conjugate and metrically conjugate maps.

The corollary shows that from the viewpoint of extensions to the 2 2 -adic integers, the 3 ​ x + 1 3x+1 maps and the 5 ​ x + 1 5x+1 maps have identical ergodic theory properties, i.e. they are both conjugate to the shift map. That is, their symbolic dynamics is “the same” in the topological sense, and their dynamics is also identical in the measure-theoretic sense.

The original 3 ​ x + 1 3x+1 problem (resp. 5 ​ x + 1 5x+1 problem) concerns their behavior when restricted to the dense set ℤ {{Z}} inside ℤ 2 {{Z}}_{2}. This set ℤ {{Z}} is countable, so has 2 2 -adic measure zero, so the general properties of ergodic theory allow no conclusion to be drawn about behavior of iteration on these maps on ℤ {{Z}}. Indeed empirical data and the stochastic models above show that the dynamics of iteration of the 3 ​ x + 1 3x+1 map and 5 ​ x + 1 5x+1 map are “not the same” on ℤ {{Z}}.

To conclude, we remark that the two accelerated functions U 3 U_{3} and U 5 U_{5} also make sense 2 2 -adically, in a restricted domain. Let ℤ 2 × = { α ∈ ℤ 2: α ≡ 1 ( mod 2) } {{Z}}_{2}^{\times}=\{\alpha\in{{Z}}_{2}:~\alpha\equiv 1~(\bmod~2)\}. We have U 3: ℤ 2 × → ℤ 2 × ∪ { 0 } U_{3}:{{Z}}_{2}^{\times}\to{{Z}}_{2}^{\times}\cup\{0\} (in the latter case we set U ⁡ ( − 1 3) = 0 U(-\frac{1}{3})=0.) and U 5: ℤ 2 × → ℤ 2 × ∪ { 0 } U_{5}:{{Z}}_{2}^{\times}\to{{Z}}_{2}^{\times}\cup\{0\} (in the latter case we set U ⁡ ( − 1 5) = 0 U(-\frac{1}{5})=0.) It might prove worthwhile to find invariant measures for these functions, and to study their ergodic-theoretic behavior.

## 11 Concluding Remarks

We have presented results on stochastic models simulating aspects of the behavior of the 3 ​ x + 1 3x+1 function and 5 ​ x + 1 5x+1 problems. These models resulted in specific predictions about various statistics of the orbits of these functions under iteration, which can be tested empirically. The experimental tests done so far have generally been consistent with these predictions.

### 11.1 Comparisons

We compare and contrast the behavior of these two maps under iteration. The 3 ​ x + 1 3x+1 map and 5 ​ x + 1 5x+1 map are similar in the following dimensions.

1. 1.

(Symbolic dynamics) The allowed symbolic dynamics of even and odd iterates is the same for the 3 ​ x + 1 3x+1 and 5 ​ x + 1 5x+1 maps. Every finite symbol sequence is legal.

2. 2.

(Periodic orbits on the integers) Conjecturally, both the 3 ​ x + 1 3x+1 map and 5 ​ x + 1 5x+1 maps have a finite number of distinct periodic orbits on the domain ℤ {{Z}}.

3. 3.

(Periodic orbits on rational numbers with odd denominator) Every possible symbolic dynamics for a periodic orbit is the periodic orbit for some rational starting point, for both the 3 ​ x + 1 3x+1 map and 5 ​ x + 1 5x+1 map. That is, extensions of the maps T 3 T_{3} and T 5 T_{5} to rational numbers with odd denominator each have 2 p 2^{p} periodic orbits of period p p, for each p ≥ 1 p\geq 1. Here the period p p may not be the minimal period of the orbit, so a period k k orbit is also counted as a period p = k ​ n p=kn orbit for each k ≥ 1 k\geq 1.

4. 4.

(Benford Law behavior) Both the initial 3 ​ x + 1 3x+1 function iterates of a random starting point, and the initial 5 ​ x + 1 5x+1 iterates of a random starting point, with high probability exhibit strong Benford law behavior to any integer base B ≥ 2 B\geq 2.

5. 5.

( 2 2 -adic extensions) The 2 2 -adic extensions of the two maps are topologically and metrically conjugate. Therefore they have the same dynamics in the topological sense, and in the ergodic theory sense, on the domain ℤ 2 {{Z}}_{2}.

The main differences between the 3 ​ x + 1 3x+1 maps and 5 ​ x + 1 5x+1 maps concerns the change in size of their interates.

1. 1.

(Short-term behavior of iterates) For the 3 ​ x + 1 3x+1 map, the initial steps of most orbits shrink in size, while for the 5 ​ x + 1 5x+1 map most orbits expand in size. This is rigorously quantified in § 2 and § 7.

2. 2.

(Long-term behavior of iterates) The 3 ​ x + 1 3x+1 and 5 ​ x + 1 5x+1 conjecturally differ greatly in their long-term behavior of orbits on the integers. For the 3 ​ x + 1 3x+1 map, conjecturally all orbits are bounded. For the 5 ​ x + 1 5x+1 map, conjecturally a density one set of integers have unbounded orbits.

It is the long term behavior of iterates where all the difficulties connected with the 3 ​ x + 1 3x+1 and 5 ​ x + 1 5x+1 function lie.

### 11.2 Insights

Comparison of the results of these stochastic models, combined with deterministic results, deliver certain insights in understanding the 3 ​ x + 1 3x+1 and 5 ​ x + 1 5x+1 problem, and suggest topics for further work.

First, the 2 2 -adic results indicate that the differences in of the dynamics of the 3 ​ x + 1 3x+1 map T 3 T_{3} and 5 ​ x + 1 5x+1 map on the integers are invisible at the level of measure theory. Therefore these differences must depend in some way on number-theoretic features inside the integers ℤ {{Z}}.

Second, the behavior of the iteration of these function of in ℤ {{Z}}, viewed inside the 2 2 -adic framework, must be encoded in the specific properties of the conjugacy maps Φ 3 \Phi_{3} and Φ 5 \Phi_{5} identifying these maps with the 2 2 -adic shift map. Here we note that there is an explicit formula for the 3 ​ x + 1 3x+1 conjugacy map, obtained by Bernstein [8], and there is an analogous formula for the 5 ​ x + 1 5x+1 conjugacy map as well. These conjugacy maps have an intricate structure, detailed in [9], which might be worthy of further investigation.

Third, we observe that the ergodic behavior of the 2 2 -adic extensions is exactly the behavior that served as a framework to formulate the random walk models presented in § 3, § 5, and § 7. These random walk models yield information by combining these model iterations with estimates of the size of iterates in the standard absolute value on the real line ℝ {{R}}. That is, they use information from an archimedean norm, rather than the non-archimedean norm on the 2 2 -adic integers. Perhaps one needs to consider models that incorporate both norms at once, e.g. functions on ℝ × ℤ 2 {{R}}\times{{Z}}_{2}.

Fourth, a suitable maximal domain, larger than ℤ {{Z}}, on which to understand the difference between the 3 ​ x + 1 3x+1 map T 3 T_{3} dynamics and the 5 ​ x + 1 5x+1 map T 5 T_{5} dynamics appears to be the domain

 | ℚ ( 2):= ℚ ∩ ℤ 2, {{Q}}_{(2)}:={{Q}}\cap{{Z}}_{2}, |  |

i.e. the set of rational numbers that are 2 2 -adic integers. The set ℚ ( 2) {{Q}}_{(2)} is exactly the set of rational numbers having an odd denominator, and both T 3 T_{3} and T 5 T_{5} leave the set ℚ ( 2) {{Q}}_{(2)} invariant. This set includes all periodic orbits of both T 3 T_{3} and T 5 T_{5}, and from the viewpoint of existence of periodic orbits, these two maps are the same on ℚ ( 2). {{Q}}_{(2)}. The difference in the dynamics of these maps on ℤ {{Z}} seems to have something to do with the distribution of these periodic orbits. Viewing ℚ ( 2) {{Q}}_{(2)} as having the topology induced from the 2 2 -adic topology, one may conjecture that T 3 T_{3} and T 5 T_{5} are not topologically conjugate mappings on this domain.

Fifth, the 5 ​ x + 1 5x+1 map exhibits various “exceptional” behaviors. Although almost all of its integer orbits (conjecturally) diverge, nevertheless there exists an infinite exceptional set of integers that have eventually periodic orbits. The density (fractional dimension) of such integers is predicted (conjecturally) to be a constant δ 5 ≈ 0.649 \delta_{5}\approx 0.649, solving a large deviations functional equation. This seems a hard problem to resolve rigorously. Now, for the 3 ​ x + 1 3x+1 map, a similar prediction is made by the models for the growth constant g = 1 g=1. It too is the solution of a large deviations functional equation. We currently know that 1 ≥ g ≥ 0.84 1\geq g\geq 0.84. This analogy suggests that rigorously proving that the growth constant δ 3 = 1 \delta_{3}=1 may turn out to be a much harder problem than it seems at first glance.

Sixth, we note that there are extensions of the maps for backwards iteration to larger domains, to the invertible 3 3 -adic integers ℤ 3 ∗ {{Z}}_{3}^{\ast} for the 3 ​ x + 1 3x+1 map, and to the invertible 5 5 -adic integers ℤ 5 ∗ {{Z}}_{5}^{\ast} for the 5 ​ c + 1 5c+1 map. In effect the branching random walk models may fruitfully be extended to allowing root node labels that are invertible 3 3 -adic integers (resp. 5-adic integers), and this provides enough information to grow the entire infinite tree. Various interesting properties of the extended 3 ​ x + 1 3x+1 trees obtained this way have been obtained, cf. [4]. This is a topic worth further investigation.

## References

- [1] Ethan Akin, Why is the 3 ​ x + 1 3x+1 Problem Hard?, In: Chapel Hill Ergodic Theory Workshops (I. Assani, Ed.), Contemp. Math. vol 356, Amer. Math. Soc. 2004, pp. 1–20.
- [2] D. Applegate and J. C. Lagarias, Density Bounds for the 3 ​ x + 1 3x+1 Problem I. Tree-Search Method, Math. Comp., 64 (1995), 411–426.
- [3] D. Applegate and J. C. Lagarias, Density Bounds for the 3 ​ x + 1 3x+1 Problem II. Krasikov Inequalities, Math. Comp., 64 (1995), 427–438.
- [4] D. Applegate and J. C. Lagarias, On the distribution of 3 ​ x + 1 3x+1 trees, Experimental Mathematics 4 (1995), 101–117.
- [5] D. Applegate and J. C. Lagarias, Lower bounds for the for the total stopping time of 3 ​ x + 1 3x+1 iterates, Math. Comp. 72 (2003), 1035–1049.
- [6] F. Benford, *The law of anomalous numbers*, Proceedings of the American Philosophical Society 78 (1938), 551-572.
- [7] A. Berger, L. Bunimovich and T. Hill, One-dimensional dynamical systems and Benford’s law, Trans. Amer. Math. Soc. 357 (2005), 197–219.
- [8] D. J. Bernstein, A non-iterative 2 2 -adic statement of the 3 ​ x + 1 3x+1 Conjecture, Proc. Amer. Math. Soc. 121 (1994), 405–408.
- [9] D. J. Bernstein and J. C. Lagarias, The 3 ​ x + 1 3x+1 Conjugacy Map, Canadian J. Math. 48 (1996), 1154–1169.
- [10] K. Borovkov and D. Pfeifer, Estimates for the Syracuse problem via a probabilistic model, Theory of Probability and its Applications 45, No. 2 (2000), 300–310.
- [11] R. N. Buttsworth and K. R. Matthews, On some Markov matrices arising from the generalized Collatz mapping, Acta Arithmetica 55 (1990), 43–57.
- [12] M. Chamberland, An update on the 3 ​ x + 1 3x+1 problem, (Catalan), Butlettí Societat Catalana de Matemàtiques 18 (2003), No.1, 19–45.
- [13] J. H. Conway, Unpredictable Iterations, Proc. 1972 Number Theory Conference (Univ. Colorado, Boulder, Colo., 1972 ), pp. 49–52. Univ. Colorado, Boulder, Colo. 1972.
- [14] R. E. Crandall, On the ‘3x+1’ problem, Math. Comp. 32 (1978), 1281–1292.
- [15] P. Diaconis, The distribution of leading digits and uniform distribution ( mod 1) (\bmod~1), Ann. Prob. 5 (1977), 72–81.
- [16] C. J. Everett, Iteration of the number theoretic function f ⁡ ( 2 ​ n) = n, f ⁡ ( 2 ​ n + 1) = 3 ​ n + 2 f(2n)=n,f(2n+1)=3n+2, Advances in Math. 25 (1977), 42–45.
- [17] A. V. Kontorovich and S. J. Miller, Benford’s law, values of L L -functions, and the 3 ​ x + 1 3x+1 problem, Acta Arithmetica 120 (2005), 269–297.
- [18] A. V. Kontorovich and Ya. G. Sinai, Structure Theorem for ( d, g, h) (d,g,h) -maps, Bull. Braz. Math. Soc. (N.S.) 33 (2002), 213–224.
- [19] I. Krasikov, How many numbers satisfy the 3 ​ x + 1 3x+1 Conjecture?, Internatl. J. Math. & Math. Sci. 12 (1989), 791–796.
- [20] I. Krasikov and J. C. Lagarias, Bounds for the 3 ​ x + 1 3x+1 problem using difference inequalities, Acta Arithmetica 109 (2003), no. 3, 237–258.
- [21] J. C. Lagarias, The 3 ​ x + 1 3x+1 problem and its generalizations, Amer. Math. Monthly 92 (1985), 3–23.
- [22] J. C. Lagarias and K. Soundararajan, Benford’s Law for the 3 ​ x + 1 3x+1 Function, J. London Math. Soc. 74 (2006), 289–303.
- [23] J. C. Lagarias and A. Weiss, The 3 ​ x + 1 3x+1 Problem: Two Stochastic Models, Annals of Applied Probability 2 (1992), 229–261.
- [24] G. M. Leigh, A Markov process underlying the generalized Syracuse algorithm, Acta Arithmetica 46 (1986), 125–143.
- [25] K. R. Matthews, The generalized 3 ​ x + 1 3x+1 mapping: Markov chains and ergodic theory, this volume.
- [26] K. R. Matthews and A. M. Watts, A generalization of Hasse’s generalization of the Syracuse algorithm, Acta. Arithmetica 43 (1984), 167–175.
- [27] K. R. Matthews and A. M. Watts, A Markov approach to the generalized Syracuse algorithm, Acta Arithmetica 45 (1985), 29–42.
- [28] S. J. Miller and R. Takloo-Bighash, An Invitation to Modern Number Theory, Princeton University Press: Princeton 2006.
- [29] S. Newcomb, Note on the frequency of use of the different digits in natural numbers, Amer. J. Math. 4 (1881), 39-40.
- [30] T. Oliveira e Silva, Maximum excursion and stopping time record-holders for the 3 ​ x + 1 3x+1 problem: Computational results, Math. Comp. 68 (1999) No. 1, 371-384.
- [31] T. Oliveira e Silva, Empirical verification of the 3 ​ x + 1 3x+1 conjecture and related conjectures, in this volume.
- [32] D. W. Rawsthorne, Imitation of an iteration, Math. Mag. 58 (1985), 172–176.
- [33] E. Roosendaal, On the 3x+1 problem, website on distributed search for 3 ​ x + 1 3x+1 records, http://www.ericr.nl/wondrous
- [34] A. Shwartz and A. Weiss, Large deviations for performance analysis. Queues, communications and computing With an appendix by Robert J. Vanderbei. Stochastic Modelling Series, Chapman & Hall: London 1995.
- [35] Ya. G. Sinai, Statistical ( 3 ​ X + 1) (3X+1) -Problem, Dedicated to the memory of Jürgen K. Moser. Comm. Pure Appl. Math. 56 No. 7 (2003), 1016–1028.
- [36] Ya. G. Sinai, Uniform distribution in the ( 3 ​ x + 1) (3x+1) problem, Moscow Math. Journal 3 (2003), No. 4, 1429–1440. (S. P. Novikov 65-th birthday issue).
- [37] Ya. G. Sinai, A theorem about uniform distribution, Commun. Math. Phys. 252 (2004), 581–588. (F. Dyson birthday issue)
- [38] R. Terras, A stopping time problem on the positive integers, Acta Arith. 30 (1976), 241–252.
- [39] R. Terras, On the existence of a density, Acta Arith. 35 (1979), 101–102.
- [40] S. Volkov, A probabilistic model for the 5 ​ k + 1 5k+1 problem and related problems, Stochastic Processes and Applications 116 (2006), 662–674.
- [41] S. Wagon, The Collatz Problem, Math. Intelligencer 7, No. 1 (1985), 72–76.
- [42] G. J. Wirsching, On the combinatorial structure of 3 ​ x + 1 3x+1 predecessor sets, Discrete Math. 148 (1996), No. 3, 265–286.
- [43] G. J. Wirsching, The dynamical system generated by the 3 ​ n + 1 3n+1 function, Lecture Notes in Math. No. 1681, Springer-Verlag: Berlin 1998.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
