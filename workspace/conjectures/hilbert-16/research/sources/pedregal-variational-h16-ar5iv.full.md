<!-- source: https://ar5iv.labs.arxiv.org/html/2103.07193 | converted from HTML -->

[2103.07193] A variational approach to Hilbert’s 16th problem within the framework of global analysis

# A variational approach to Hilbert’s 16th problem within the framework of global analysis Thanks: Departamento de Matemáticas, Universidad de Castilla-La Mancha, 13071 Ciudad Real, SPAIN. Supported by grants PID2023-151823NB-I00, and SBPLY/23/180225/000023

Pablo Pedregal Address: Universidad de Castilla-La Mancha Current address: Email address: [pablo.pedregal@uclm.es][1]

###### Abstract.

We focus on the second part of Hilbert’s 16th problem and provide an upper bound on the number of limit cycles that a polynomial, differential, planar system may have, depending exclusively on the degree n n of the system. Such a bound turns out to be a polynomial of degree 4 4 in n n. More specifically, if H ⁡ ( n) H(n) indicates the maximum number of limit cycles among planar, differential, polynomial systems of degree n n, then

 | H ⁡ ( n) ≤ 5 2 ​ n 4 − 23 2 ​ n 3 + 43 2 ​ n 2 − 37 2 ​ n + 7 ​ if n is even, and \displaystyle H(n)\leq\dfrac{5}{2}n^{4}-\dfrac{23}{2}n^{3}+\dfrac{43}{2}n^{2}-\dfrac{37}{2}n+7\,\,\,\,\mbox{if $n$ is even, and} |  |

 | H ⁡ ( n) ≤ 5 2 ​ n 4 − 23 2 ​ n 3 + 41 2 ​ n 2 − 33 2 ​ n + 6 ​ if n is odd. \displaystyle H(n)\leq\dfrac{5}{2}n^{4}-\dfrac{23}{2}n^{3}+\dfrac{41}{2}n^{2}-\dfrac{33}{2}n+6\,\,\,\,\mbox{if $n$ is odd}. |  |

For quadratic systems, we find H ⁡ ( 2) = 4 H(2)=4. Our proof is entirely variational and utilizes in a fundamental way tools and facts from global analysis to the point that no particular expertise in dynamical systems is necessary or required.

###### Key words and phrases:

Morse inequalities, invariant sets, Euler-Lagrange system, multiplicity

###### 2020 Mathematics Subject Classification

58E05, 58E30

## 1. Introduction and main result

This paper deals with planar differential systems of the form

(1.1) |  | x ′ ​ ( t) = P ⁡ ( x ⁡ ( t), y ⁡ ( t)), y ′ ​ ( t) = Q ⁡ ( x ⁡ ( t), y ⁡ ( t)). x^{\prime}(t)=P(x(t),y(t)),\quad y^{\prime}(t)=Q(x(t),y(t)). |  |

As soon as the two functions

 | P ⁡ ( x, y), Q ⁡ ( x, y): ℝ 2 → ℝ P(x,y),Q(x,y):\mathbb{R}^{2}\to\mathbb{R} |  |

are smooth, there is a unique smooth integral curve of the system passing through every point in ℝ 2 \mathbb{R}^{2}. This is a standard result that is studied in every first course in ODEs. Equilibria, i.e. points ( x 0, y 0) ∈ ℝ 2 (x_{0},y_{0})\in\mathbb{R}^{2} where both P P and Q Q simultaneously vanish, play a central role in the overall dynamics of such a system. Periodic solutions too deserve a special place concerning the global dynamics of the system.

###### Definition 1.1.

Every periodic solution of ( 1.1) that is isolated from other such solutions is called a limit cycle of the system.

We restrict attention in this paper to the case of planar, polynomial, differential systems for which the maximum of the degrees of both polynomials P ⁡ ( x, y) P(x,y) and Q ⁡ ( x, y) Q(x,y) is n n.

The problem we would like to address is the second part of Hilbert’s 16th problem [23], which in the version due to Smale [47], can be formulated as follows.

Consider the polynomial differential system ( 1.1) in ℝ 2 \mathbb{R}^{2}. Is there a bound K on the number of limit cycles of the form K ≤ n q K\leq n^{q} where n n is the maximum of the degrees of P P and Q Q, and q q is a universal constant ?

There have been some crucial contributions towards the solution of this problem. Some of them are indicated below at the end of this Introduction. As our approach has essentially nothing in common with those, we simply mention some additional ones here without further comment: [3], [10], [15], [18], [24], [25], [36], [37], [38], [45], [49]. There are also some important articles dealing with lower bounds for the number of limit cycles [12], [22], [28], as well as some other relevant results concerning this problem restricted to algebraic limit cycles [30], [31], [32], [54] among others; or about the possible configurations of those limit cycles [20], [33], [44], [50], [52]. There is such an abundance of relevant papers, that, to avoid dispersion, we have only mentioned those more familiar to the author in the final bibliographic section.

Our aim is the complete proof of the following central theorem.

###### Theorem 1.1.

Consider the polynomial differential system ( 1.1) of degree n > 1 n>1. Assume that:

1. (1)

P P and Q Q have no common non-trivial factor.

2. (2)

All of the connected components of the algebraic curve

 | P x + Q y = 0, P_{x}+Q_{y}=0, |  |

are homeomorphic to a straight line or to an oval (i.e. such curve has no singular points), and that there are M M of such components.

3. (3)

The polynomial system

(1.2) |  | P ⁡ ( P x ​ x + Q y ​ x) + Q ⁡ ( P x ​ y + Q y ​ y) = 0, P x + Q y = 0, \begin{array}[]{r}P(P_{xx}+Q_{yx})+Q(P_{xy}+Q_{yy})=0,\\ P_{x}+Q_{y}=0,\end{array} |  |

only has N N simple solutions (i.e. N N simple contact points of the vector field ( P, Q) (P,Q) with the curve P x + Q y = 0 P_{x}+Q_{y}=0).

Then an upper bound for the number H ⁡ ( n) H(n) of limit cycles that such a differential system ( 1.1) may have is

(1.3) |  | H ⁡ ( n) ≤ 1 + ( n − 1) 2 ​ ( M + N). H(n)\leq 1+(n-1)^{2}(M+N). |  |

Though this theorem can be used to find upper bounds for the number of limit cycles of special families of differential systems, or even for individual ones, upper bound ( 1.3) can serve, together with the classic results of Bezout and Harnack to relate parameters M M and N N to n n, to establish an upper bound for the number of limit cycles of such regular, planar, polynomial, differential system of degree n n only in terms of n n. On the other hand, the important hypotheses assumed in this statement are generic, in the sense that if they do not hold for a particular planar polynomial system, a small perturbation of P P and Q Q, without changing their degree, permits to have them. A standard genericity argument then may be utilized to extend bound ( 1.3) in Theorem 1.1 to arbitrary systems of degree n n, not complying with such conditions, in order to show the validity of the following general explicit upper bound furnishing an answer to Hilbert’s 16th problem ( [23]) and Smale’s 13th problem ( [47]).

###### Theorem 1.2.

An upper bound for the maximum number H ⁡ ( n) H(n) of limit cycles that a planar polynomial differential system of degree n > 1 n>1 can have is

 | H ⁡ ( n) ≤ 5 2 ​ n 4 − 23 2 ​ n 3 + 43 2 ​ n 2 − 37 2 ​ n + 7 ​ if n is even, and \displaystyle H(n)\leq\dfrac{5}{2}n^{4}-\dfrac{23}{2}n^{3}+\dfrac{43}{2}n^{2}-\dfrac{37}{2}n+7\,\,\,\,\mbox{if $n$ is even, and} |  |

 | H ⁡ ( n) ≤ 5 2 ​ n 4 − 23 2 ​ n 3 + 41 2 ​ n 2 − 33 2 ​ n + 6 ​ if n is odd. \displaystyle H(n)\leq\dfrac{5}{2}n^{4}-\dfrac{23}{2}n^{3}+\dfrac{41}{2}n^{2}-\dfrac{33}{2}n+6\,\,\,\,\mbox{if $n$ is odd}. |  |

The number H ⁡ ( n) H(n) is usually called the Hilbert number for polynomial differential systems of degree n n. This upper bound for H ⁡ ( n) H(n) yields a universal exponent q = 4 q=4 for the above version due to Smale.

Part of our job is to understand the role played by the following three pieces of information:

- •

the divergence curve

 | Div = Div ⁡ ( x, y) ≡ P x ​ ( x, y) + Q y ​ ( x, y) = 0; \operatorname{Div}=\operatorname{Div}(x,y)\equiv P_{x}(x,y)+Q_{y}(x,y)=0; |  |

- •

the set of contact points of the vector field ( P, Q) (P,Q) with the curve Div = 0 \operatorname{Div}=0 which are the solutions of system ( 1.2); and

- •

the role played by the factor ( n − 1) 2 (n-1)^{2} multiplying the sum M + N M+N in ( 1.3), and where it comes from.

### 1.1. Main corollaries of central theorem

It is a well-established fact that in counting limit cycles for planar, differential systems, the two components P P and Q Q can be assumed not to have non-trivial common factors. It is also well-known that, under small perturbations in the coefficients of P P and Q Q, the components of the algebraic curve Div = 0 \operatorname{Div}=0 become homeomorphic either to a straight line or to an oval, and that the number of contact points, understood as solutions of system ( 1.2), of the vector field ( P, Q) (P,Q) with the curve Div = 0 \operatorname{Div}=0, is finite, and they all are simple. We refer to this case as the generic situation. Given that the bound for the generic case is uniform on the degree n n of the system, showing that such an upper bound for the number of limit cycles of a polynomial differential system of degree n n extends to a non–generic vector field of the same degree n n is not a big deal. Such perturbation argument will be described in the final section. As indicated, it enables to extend bounds on generic differential systems of a certain degree to general systems of the same degree. Because of this remark, we will always take for granted those generic assumptions, knowing that they extend without trouble to the general situation.

Our principal, fundamental concern is to prove Theorem 1.1. If one assumes that it has been shown, then Theorem 1.2 in the generic case is easy to prove. This amounts to calculating the value of the two parameters M M and N N in this result in terms of the degree n n of the system.

To do so, we recall two classical theorems:

###### Theorem 1.3 (Bezout Theorem, [19]).

Let R ⁡ ( x, y) R(x,y) and S ⁡ ( x, y) S(x,y) be two polynomials with coefficients in ℝ \mathbb{R}. If both polynomials do not share a non-trivial common factor, then the algebraic system of equations

 | R ⁡ ( x, y) = S ⁡ ( x, y) = 0 R(x,y)=S(x,y)=0 |  |

has at most degree ( R) (R) degree ( S) (S) solutions.

###### Theorem 1.4 (Harnack Theorem, [21]).

The maximum number of connected components of an algebraic curve of degree k k is

- (a)

1 + ( k − 1) ​ ( k − 2) / 2 1+(k-1)(k-2)/2 if k k is even,

- (b)

( k − 1) ​ ( k − 2) / 2 (k-1)(k-2)/2 if k k is odd.

###### Proof of Theorem 1.2 based on Theorem 1.1.

We need to find an upper bound for the number N N of the solutions that system ( 1.2) may have when P P and Q Q are polynomials of at most degree n n. By Bezout’s theorem we have that

 | N ≤ 2 ​ ( n − 1) 2, N\leq 2(n-1)^{2}, |  |

because in the generic case we discard the possibility that the two equations of system ( 1.2) may have a non–trivial common factor. Note that the degree of the first equation in system ( 1.2) is 2 ​ n − 2 2n-2 while that of the second one is n − 1 n-1.

By Theorem 1.4 the number M M of components of Div = 0 \operatorname{Div}=0 satisfies

 | M ≤ 1 2 ​ ( n − 2) ​ ( n − 3) + 1, M\leq\frac{1}{2}(n-2)(n-3)+1, |  |

if n n is even, and

 | M ≤ 1 2 ​ ( n − 2) ​ ( n − 3), M\leq\frac{1}{2}(n-2)(n-3), |  |

if n n is odd. Note that k = n − 1 k=n-1.

The final number in the statement of the theorem is then a direct consequence of Theorem 1.1, i.e.

 | 1 + ( n − 1) 2 ​ ( N + M) ≤ 1 + ( n − 1) 2 ​ ( 1 2 ​ ( n − 2) ​ ( n − 3) + 1 + 2 ​ ( n − 1) 2) = 5 2 ​ n 4 − 23 2 ​ n 3 + 43 2 ​ n 2 − 37 2 ​ n + 7, \begin{array}[]{rl}1+(n-1)^{2}(N+M)\leq&1+(n-1)^{2}\left(\dfrac{1}{2}(n-2)(n-3)+1+2(n-1)^{2}\right)\\ =&\dfrac{5}{2}n^{4}-\dfrac{23}{2}n^{3}+\dfrac{43}{2}n^{2}-\dfrac{37}{2}n+7,\end{array} |  |

if n n is even, while

 | 1 + ( n − 1) 2 ​ ( N + M) ≤ 1 + ( n − 1) 2 ​ ( 1 2 ​ ( n − 2) ​ ( n − 3) + 2 ​ ( n − 1) 2) = 5 2 ​ n 4 − 23 2 ​ n 3 + 41 2 ​ n 2 − 33 2 ​ n + 6, \begin{array}[]{rl}1+(n-1)^{2}(N+M)\leq&1+(n-1)^{2}\left(\dfrac{1}{2}(n-2)(n-3)+2(n-1)^{2}\right)\\ =&\dfrac{5}{2}n^{4}-\dfrac{23}{2}n^{3}+\dfrac{41}{2}n^{2}-\dfrac{33}{2}n+6,\end{array} |  |

if n n is odd. This yields the numbers in the statement of Theorem 1.2 in the generic case. ∎

Two corollaries of Theorem 1.1 are worth stating. The first refers to quadratic differential systems which have attracted a lot of attention throughout the years as a training ground for novel ideas and techniques ( [3], [16], [17], [42], [43], [45], [48]).

###### Corollary 1.5.

If the divergence of a quadratic polynomial differential system ( 1.1) is constant or zero, then it has no limit cycles. Otherwise if the straight line Div = 0 \operatorname{Div}=0 of a quadratic polynomial differential system ( 1.1) has:

- (a)

either one or two contact points, then it cannot have more than 4 4 limit cycles.

- (b)

no contact points, then it has no limit cycles.

At any rate, H ⁡ ( 2) = 4 H(2)=4.

###### Proof.

The set Div = 0 \operatorname{Div}=0 for a quadratic polynomial differential system is either empty, a straight line, or the whole plane. If it is empty, i.e. if Div \operatorname{Div} is a non-zero constant, then the system has no limit cycles by Bendixon criterium (see for instance Theorem 7.10 of [14]). If it is the whole plane, the system is Hamiltonian and so it has no limit cycles. We assume that Div = 0 \operatorname{Div}=0 is a straight line. So using ( 1.3), we have

 | n = 2, M = 1, N ∈ { 0, 1, 2 }. n=2,\quad M=1,\quad N\in\{0,1,2\}. |  |

If N = 2 N=2, contact points are simple, and then

 | 1 + ( n − 1) 2 ​ ( M + N) = 1 + 1 + 2 = 4. 1+(n-1)^{2}(M+N)=1+1+2=4. |  |

If N = 1 N=1, the unique contact point has multiplicity two, and the upper bound is the same. If N = 0 N=0, then there are no contact points and the limit cycles cannot intersect the straight line Div = 0 \operatorname{Div}=0. Again by Bendixon criterium, the system has no limit cycles.

Since quadratic systems with four limit cycles are known ( [10], [45]), we conclude that indeed H ⁡ ( 2) = 4 H(2)=4. ∎

For Liénard systems ( [8], [29]), we have the following.

###### Corollary 1.6.

We consider the Liénard polynomial differential systems

(1.4) |  | x ˙ = P ⁡ ( x, y) = y − f ⁡ ( x), y ˙ = Q ⁡ ( x, y) = g ⁡ ( x), \dot{x}=P(x,y)=y-f(x),\quad\dot{y}=Q(x,y)=g(x), |  |

where p p is the degree of f f, and q q is the degree of g g. So n = max ⁡ { p, q } n=\max\{p,q\}. A system ( 1.4) cannot have more than

 | 1 + 2 ​ ( max ⁡ { p, q } − 1) 2 ​ ( p − 1) 1+2(\max\{p,q\}-1)^{2}(p-1) |  |

limit cycles.

###### Proof.

It is well known that a system ( 1.4) has at most p − 1 p-1 connected components because the curve

 | Div = f ′ ​ ( x) = 0 \operatorname{Div}=f^{\prime}(x)=0 |  |

corresponds to the critical values of the polynomial f f. Note that each component is a vertical straight line in the ( x, y) (x,y) –plane. System ( 1.2) becomes

 | ( y − f ⁡ ( x)) ​ f ′′ ​ ( x) = 0, f ′ ​ ( x) = 0, (y-f(x))f^{\prime\prime}(x)=0,\qquad f^{\prime}(x)=0, |  |

for differential system ( 1.4). If

 | f ′′ ​ ( x) = f ′ ​ ( x) = 0 f^{\prime\prime}(x)=f^{\prime}(x)=0 |  |

has a solution x 0 x_{0}, the vertical straight line x = x 0 x=x_{0} is formed by contact points, so it is invariant and we do not need to take it into account, because limit cycles cannot intersect such straight line. Therefore a connected component of the curve Div = 0 \operatorname{Div}=0 has one single contact point ( x 0, f ⁡ ( x 0)) (x_{0},f(x_{0})) for each zero x 0 x_{0} of the polynomial f ′ ​ ( x) f^{\prime}(x) such that f ′′ ​ ( x 0) ≠ 0 f^{\prime\prime}(x_{0})\neq 0. Using again ( 1.3), we have

 | n = max ⁡ { p, q }, M = N ≤ p − 1. n=\max\{p,q\},\quad M=N\leq p-1. |  |

Hence

 | 1 + ( n − 1) 2 ​ ( M + N) = 1 + 2 ​ ( max ⁡ { p, q } − 1) 2 ​ ( p − 1). 1+(n-1)^{2}(M+N)=1+2(\max\{p,q\}-1)^{2}(p-1). |  |

This completes the proof. ∎

### 1.2. Driving idea for the proof of Theorem 1.1

Our guiding principle for the proof of Theorem 1.1, expressed in a single sentence, is:

Limit cycles of the differential system ( 1.1) can be interpreted as zeros of the following functional associated with it in a natural way

(1.5) |  | E 0 ​ ( x, y) = ∫ 0 1 1 2 ​ ( P ⁡ ( x, y) ​ y ′ − Q ⁡ ( x, y) ​ x ′) 2 ​ 𝑑 t. E_{0}(x,y)=\int_{0}^{1}\frac{1}{2}(P(x,y)y^{\prime}-Q(x,y)x^{\prime})^{2}\,dt. |  |

Use then Morse’s inequalities to count them in terms of its critical paths.

Even if the following parallelism may be blamed as too naive, it may help some readers stay oriented about where we are heading. It is exactly a similar situation in dimension one. If we are interested in knowing how many real roots a single equation

 | f ⁡ ( x) = 0 f(x)=0 |  |

may posses, one possibility is to look for global minimizers of the function

 | g ⁡ ( x) = ( 1 / 2) ​ f ​ ( x) 2. g(x)=(1/2)f(x)^{2}. |  |

It is obvious that roots of the first correspond exactly to absolute minimizers of the second, given that g ≥ 0 g\geq 0 always. Critical points for g g are roots of

 | f ⁡ ( x) ​ f ′ ​ ( x) = 0; f(x)f^{\prime}(x)=0; |  |

and those not corresponding to absolute minimizers

 | f ⁡ ( x) ≠ 0, f(x)\neq 0, |  |

are zeros of f ′ ​ ( x) f^{\prime}(x). Morse’s inequalities in this simple context reduce just to classical Rolle’s theorem that yields the upper bound

 | #⁡ ( roots of f) ≤ 1 + #⁡ ( roots of f ′ ∖ roots of f). \#(\hbox{roots of $f$})\leq 1+\#(\hbox{roots of $f^{\prime}$}\setminus\hbox{roots of $f$}). |  |

Going back to our functional ( 1.5), note how every periodic solution of ( 1.1), suitably reparametrized in [0, 1] for normalization, is a zero of E 0 E_{0} in ( 1.5).

Our contribution consists in an attempt to rigorously show that the simple idea just expressed can be carried out to its fulfillment for the proof of Theorem 1.1.

Our work is organized in four main overall stages.

1. (1)

Describe and prepare the analytical setting around functional ( 1.5) for the legitimate use of Morse’s inequalities that permit to estimate absolute minimizers of a Morse functional in terms of the number of its critical points other than those absolute minimizers. This requires to work with a suitable perturbation E ϵ E_{\epsilon} of E 0 E_{0} in addition to determining the functional analytical scenario. As a consequence of Morse’s inequalities, we will be able to bound the number of connected components of sub-level sets { E ϵ ≤ a } \{E_{\epsilon}\leq a\} by the number of its critical points with critical value for E 0 E_{0} uniformly away from zero (with respect to ϵ \epsilon).

2. (2)

Identify suitable classes of paths where limit cycles of the original polynomial differential system ( 1.1) can be identified in a one-to-one manner with some of the connected components of sub-level sets { E ϵ ≤ a } \{E_{\epsilon}\leq a\}.

3. (3)

Examine carefully the form of the critical point equation for the relevant functional E ϵ E_{\epsilon} that comes from E 0 E_{0} by perturbation.

4. (4)

Count the number of critical paths of E ϵ E_{\epsilon} not associated with absolute minimizers of E 0 E_{0}, and check that an upper estimate, independent of ϵ \epsilon, on those is possible. This step is clearly divided in two main parts.

  1. (a)

Determine the possible asymptotic distinct behaviors of such branches of critical paths as ϵ ↘ 0 \epsilon\searrow 0.

  2. (b)

Derive an upper bound on the number of those possible branches converging to each such possible limit behavior.

This is a general, global description of our strategy. It may be important to have it in mind as we proceed to a much more detailed explanation. Since we will be moving at several levels of different generality, we will systematically used text within boxes, like the following one, to constantly establishing the parallelism with the application to Hilbert’s 16th problem:

Hilbert’s 16th problem In this way, readers will have a constant reference to the application of more abstract or more general principles to our main particular problem.

Our hope is to be able to apply the above simple principle and the corresponding program to our situation. The full path is, however, anything but simple or straightforward.

### 1.3. Final comments

Though very well-known to specialists, Hilbert’s 16th problem [23] may be not known to mathematicians working in other areas. As described above, we are interested in the second part of it which deals with the number of limit cycles of planar, polynomial differential systems of the form

 | x ′ = P ⁡ ( x, y), y ′ = Q ⁡ ( x, y), x^{\prime}=P(x,y),\quad y^{\prime}=Q(x,y), |  |

where both P P and Q Q are polynomials of two variables, and the possibility of providing an upper bound on them depending solely on the maximum degree n n of both P P and Q Q.

The history of such a problem along the XX-th century is one of the most fascinating situations in Mathematics one can look at. We will not spend time on this here as there are very good and reliable accounts; particularly [1], [2], [5], [11], [26], [27], [28], [34], [53], [46] are indispensable to learn and understand such history. It is also appropriate to recall that, according to Smale [47], except for the Riemann hypothesis, the second part of Hilbert’s 16th problem seems to be the most elusive of Hilbert’s problems. Aside from the various failed attempts to solve the problem, there are essentially two sources to examine this problem. Both [18], [25] claim the finiteness of the number of limit cycles for any planar, polynomial differential system without establishing a bound in terms of the degree of the system. Again according to Smale ( [47]), “these two papers have yet to be thoroughly digested by the mathematical community”.

Our contribution is written in a self-contained form for the most part of it. Proofs, though, of very classic results in Analysis which are part of the usual background for many non-linear analysts are not covered as they will, most likely, be accepted without discussion when invoked. A list of these includes:

- •

Morse inequalities.

- •

Basic concepts and facts of Linear and Non-Linear Functional Analysis.

- •

Some geometrical facts about planar curves.

A special place is reserved for a couple of classical results of Harnack and Bezout as they have already been used earlier. There are also some prerequisites that have been taken for granted as most of them belong to the initial training for master or doctorate students in Analysis:

- •

Basic concepts and results in differential systems.

- •

Regular dependence of solutions of ODE on initial conditions and parameters.

- •

Vector Sobolev spaces in one variable.

- •

Basic concepts of functionals defined on Hilbert spaces.

- •

Perturbation of differential systems.

- •

Basic topological concepts about planar algebraic curves.

The structure of the paper is a bit special with the goal in mind to facilitate understanding in the most transparent, affordable way. Material is presented in a form for which the global proof is grasped little by little. The strategy is made up of various inter-connected fundamental steps, some of which enclose important sub-steps. It is a non-trivial exercise to comprehend how the different pieces of the puzzle pretend to fit with each other. After all, one has to show that indeed they all do so together in a nice overall picture. Even so, we hope to have discovered the optimal way of explaining things to the point that even a well-motivated graduate student with a sound background in non-linear and global analysis, and variational techniques will be able to understand and appreciate the global proof. This way of presenting things also looks especially relevant given that some interested readers may not be that familiar with variational concepts and techniques which are at the bottom line of our approach. In this vein, the material in some sections may seem dispensable to some readers, yet it may be quite informative and clarifying to others. We are pretty sure that a senior researcher with a solid expertise in global analysis and variational methods will capture the main thread of the proof, as well as technical details of the various stages.

## 2. Strategy and organization

We will be moving at three levels.

1. (1)

Some of our ideas can be examined in an abstract setting without paying attention to the particular form of spaces or functionals.

2. (2)

Some others require to restrict attention to the special nature of spaces and functionals, and yet results enjoy a certain degree of generality.

3. (3)

Still others refer specifically to Hilbert’s problem.

We will therefore be moving from the general to the specific.

### 2.1. The abstract setting

Suppose we are working in a given Hilbert space 𝕃 \mathbb{L}. There is a certain important property ( P) (P) that some elements of 𝕃 \mathbb{L} enjoy, and we would like to test our ability to count them. Let ℙ ⊂ 𝕃 \mathbb{P}\subset\mathbb{L} be the subset of those elements 𝐱 \mathbf{x} of 𝕃 \mathbb{L} enjoying property ( P) (P).

Hilbert’s 16th problem 𝕃 \mathbb{L} is the class of parameterizations of closed (periodic) plane paths or curves with certain differentiability and integrability properties. The subset ℙ \mathbb{P} would stand for those parameterizations of limit cycles of our differential system ( 1.1).

###### Problem 2.1.

Find an upper bound for the cardinality of ℙ \mathbb{P} in terms of some of its defining features.

Since it does not look feasible to deal directly with ℙ \mathbb{P} in a quantitative way, we realize that there is a natural functional

 | E: 𝕃 → ℝ + E:\mathbb{L}\to\mathbb{R}^{+} |  |

with the remarkable property

(2.1) |  | 𝐱 ∈ ℙ ⟹ E ⁡ ( 𝐱) = 0. \mathbf{x}\in\mathbb{P}\Longrightarrow E(\mathbf{x})=0. |  |

Hence, we would like to explore the possibility of solving Problem 2.1 by counting how many zeroes E E may have in 𝕃 \mathbb{L}.

Hilbert’s 16th problem Functional E E is given in ( 1.5), namely E ⁡ ( 𝐮) = 1 2 ​ ∫ 0 1 ( P ⁡ ( x ⁡ ( t), y ⁡ ( t)) ​ y ′ ​ ( t) − Q ⁡ ( x ⁡ ( t), y ⁡ ( t)) ​ x ′ ​ ( t)) 2 ​ 𝑑 t, 𝐮 = ( x, y). E(\mathbf{u})=\frac{1}{2}\int_{0}^{1}(P(x(t),y(t))y^{\prime}(t)-Q(x(t),y(t))x^{\prime}(t))^{2}\,dt,\quad\mathbf{u}=(x,y). It is elementary to realize that E ⁡ ( 𝐮) = 0 E(\mathbf{u})=0 for any parametrization 𝐮 \mathbf{u} of a limit cycle of differential system ( 1.1) in the interval [0, 1] [0,1].

There is a standard way to deal with and count absolute minimizers of smooth, regular functionals. It is like a big, global Rolle’s theorem in infinite dimension as already indicated earlier.

###### Theorem 2.2 (Morse inequalities).

Let E: 𝕃 → ℝ E:\mathbb{L}\to\mathbb{R} be a 𝒞 2 \mathcal{C}^{2} -functional defined over a Hilbert space 𝕃 \mathbb{L}, which is bounded from below, coercive, enjoying the Palais-Smale property, and having a finite number of critical points, all of which are non-degenerate and of a finite index. Put M k M_{k} for the (finite) number of critical points of E E, for each fixed index k k. Then

 | M 0 ≥ 1, M 1 − M 0 ≥ − 1, M 2 − M 1 + M 0 ≥ 1, …, \displaystyle M_{0}\geq 1,\quad M_{1}-M_{0}\geq-1,\quad M_{2}-M_{1}+M_{0}\geq 1,\quad\dots, |  |

(2.2) |  | ∑ k = 0 ∞ ( − 1) k ​ M k = 1. \displaystyle\sum_{k=0}^{\infty}(-1)^{k}M_{k}=1. |  |

There is a number of fundamental concepts in this statement that need to be examined before its conclusion is utilized. To avoid breaking the thread of our discussion at this stage, let us ignore them for the time being and see how one could use this important result.

We are most interested in counting a selected set of the zeroes of a non-negative functional

 | E: 𝕃 → ℝ + E:\mathbb{L}\to\mathbb{R}^{+} |  |

that is assumed to comply with all of the requirements for Theorem 2.2 to be applied. In particular, zeroes of E E must be isolated. Those zeroes are part of the class of absolute minimizers of E E, which in turn is a subclass of the full set of local minimizers. The number of local minimizers is precisely M 0 M_{0}. Therefore, from ( 2.2), we find

 | M a ​ b ​ s + ( M 0 − M a ​ b ​ s) = M 0 = 1 + ∑ k = 1 ∞ ( − 1) k + 1 ​ M k ≤ 1 + ∑ k = 1 ∞ M k, M_{abs}+(M_{0}-M_{abs})=M_{0}=1+\sum_{k=1}^{\infty}(-1)^{k+1}M_{k}\leq 1+\sum_{k=1}^{\infty}M_{k}, |  |

if M a ​ b ​ s ≤ M 0 M_{abs}\leq M_{0} is the number of absolute minimizers. Finally

 | M a ​ b ​ s ≤ 1 + ∑ k = 1 ∞ M k + ( M 0 − M a ​ b ​ s). M_{abs}\leq 1+\sum_{k=1}^{\infty}M_{k}+(M_{0}-M_{abs}). |  |

The sum on the right-hand side is the number of all critical points of E E which are not global minimizers. If we let M c ​ r ​ i M_{cri} be the number of those critical points, we have the upper bound

(2.3) |  | M a ​ b ​ s ≤ 1 + M c ​ r ​ i. M_{abs}\leq 1+M_{cri}. |  |

For those situations for which we can handle an upper bound for M c ​ r ​ i M_{cri}, we would have an upper bound for M a ​ b ​ s M_{abs}, i.e. an upper bound on the number of zeroes of E E. That would solve Problem ( 2.1) assuming we could bound M c ​ r ​ i M_{cri} in terms of the defining features of ℙ \mathbb{P}.

### 2.2. Initial difficulties

When trying to use Theorem 2.2 in the initial Hilbert space 𝕃 \mathbb{L}, one may find many troubles. To begin with, even before turning our attention to functional E E, we realize that in fact infinitely many elements of 𝕃 \mathbb{L} identify a single element of ℙ \mathbb{P}. Said differently, we come to the conclusion that each element of ℙ \mathbb{P} is in fact represented by infinitely many continua of elements of 𝕃 \mathbb{L}, and thus it is not feasible to pretend utilizing Theorem 2.2 directly.

Hilbert’s 16th problem Limit cycles can be reparameterized in infinitely many ways, even if, for the sake of normalization, we impose 1 1 -periodicity. The situation is indeed dramatic as, in addition, parameterizations can cover the same limit cycles several times either counter- or clock-wise.

Fortunately, we may be able to identify a distinguished open subset 𝕀 \mathbb{I} of 𝕃 \mathbb{L} in which each element of ℙ \mathbb{P} has a unique continuous set of representatives. If we do not restrict attention to 𝕀 \mathbb{I} everything might be mixed up in a rather nasty way to the point of spoiling the neatness of property ( 2.1). Working in 𝕀 \mathbb{I} may still pose important difficulties, as each element of ℙ \mathbb{P} might still admit a whole continuum of representatives, but at least we envision the possibility of being able to use Morse inequalities in an appropriate way within 𝕀 \mathbb{I}. In fact, we realize that different elements of ℙ \mathbb{P} in Problem ( 2.1) correspond to disjoint components of the zero set { E = 0 } \{E=0\} in a suitable subset 𝕀 \mathbb{I}, and so our problem can be more clearly and specifically formulated as follows.

###### Problem 2.3.

Find an upper bound on the number of components of the zero set { E = 0 } \{E=0\} in 𝕀 \mathbb{I}, for a suitable subset 𝕀 ⊂ 𝕃 \mathbb{I}\subset\mathbb{L}. From this perspective, set ℙ \mathbb{P} can be identified with the set of these components.

The foundational result, restricting attention to subsets 𝕀 \mathbb{I}, upon which to start our approach is then a similar version of Theorem 2.2 which is valid precisely when attention is restricted to suitable subsets of Hilbert spaces. Recall that a subset 𝕀 \mathbb{I} of a Hilbert space 𝕃 \mathbb{L} is said to be invariant with respect to a 𝒞 1 \mathcal{C}^{1} -functional E E, if the flow of − E -E cannot leave 𝕀 \mathbb{I}, and there is no critical point of E E on the boundary ∂ 𝕀 \partial\mathbb{I}. We will be more precise below.

###### Theorem 2.4 (Morse inequalities for invariant sets).

Let E: 𝕃 → ℝ E:\mathbb{L}\to\mathbb{R} be a 𝒞 2 \mathcal{C}^{2} -functional defined over a Hilbert space 𝕃 \mathbb{L}, which is bounded from below, coercive, enjoying the Palais-Smale property, and having a finite number of critical points, all of which are non-degenerate and of a finite index. Let 𝕀 ⊂ 𝕃 \mathbb{I}\subset\mathbb{L} be open, topologically equivalent to a ball, and invariant under E E. Put M k ​ ( 𝕀) M_{k}(\mathbb{I}) for the (finite) number of critical points of E E in 𝕀 \mathbb{I}, for each fixed index k k. Then

 | M 0 ( 𝕀) ≥ 1, M 1 ( 𝕀) − M 0 ( 𝕀) ≥ − 1, M 2 ( 𝕀) − M 1 ( 𝕀) + M 0 ( 𝕀) ≥ 1, …, \displaystyle M_{0}(\mathbb{I})\geq 1,\quad M_{1}(\mathbb{I})-M_{0}(\mathbb{I})\geq-1,\quad M_{2}(\mathbb{I})-M_{1}(\mathbb{I})+M_{0}(\mathbb{I})\geq 1,\quad\dots, |  |

 | ∑ k = 0 ∞ ( − 1) k ​ M k ​ ( 𝕀) = 1. \displaystyle\sum_{k=0}^{\infty}(-1)^{k}M_{k}(\mathbb{I})=1. |  |

This statement ensures that our previous bound ( 2.3) is still valid

(2.4) |  | M a ​ b ​ s ​ ( 𝕀) ≤ 1 + M c ​ r ​ i ​ ( 𝕀) M_{abs}(\mathbb{I})\leq 1+M_{cri}(\mathbb{I}) |  |

when attention is restricted to an invariant set 𝕀 ⊂ 𝕃 \mathbb{I}\subset\mathbb{L} for the functional E E. If we can find an upper bound of M c ​ r ​ i ​ ( 𝕀) M_{cri}(\mathbb{I}) in terms of parameters determining ℙ \mathbb{P}, then we would have solved Problem 2.3. Note the important topological condition on 𝕀 \mathbb{I} in the statement. This is an indispensable requirement to preserve ( 2.3) in the same form ( 2.4). If 𝕀 \mathbb{I} is not topologically equivalent to a ball, then the bound is a bit different depending on topological invariants of 𝕀 \mathbb{I} like the Euler characteristic or the Betti numbers (check [9], [41]).

### 2.3. Troubles persist

But things may turn out to be not so easy yet because, even if we identify such an important candidate 𝕀 ⊂ 𝕃 \mathbb{I}\subset\mathbb{L}, when we turn our attention to functional E E, considered over 𝕃 \mathbb{L}, we might find that it is not expected to comply with requirements in Theorem 2.4.

Hilbert’s 16th problem In fact, functional E E in ( 1.5) does not comply with any of those requirements in Theorem 2.4 since, in particular, absolute minimizers for E E, even in a good candidate 𝕀 \mathbb{I}, might not be isolated, or we may have infinitely many of them. Though we will be much more precise later, we anticipate that the set 𝕀 ≡ 𝕆 d \mathbb{I}\equiv\mathbb{O}_{d}, d ∈ ℕ d\in\mathbb{N}, will be the set of smooth, non-singular parameterizations with (global) winding number equal to + 1 +1, but with a total number of full rounds of its unit, normalized tangent vector, regardless of whether they are run clock- or counterclock-wise, bounded by d d. Parameterizations in 𝕆 d \mathbb{O}_{d} of different limit cycles belong to different components (in 𝕆 d \mathbb{O}_{d}) of the zero set { E = 0 } \{E=0\} for E E as in ( 1.5) because limit cycles are isolated. Note that it we put 𝕆 \mathbb{O} for the class of non-singular parametrizations of planar curves with winding number + 1 +1, then (2.5) 𝕆 = ⋃ d ∈ ℕ 𝕆 d, \mathbb{O}=\bigcup_{d\in\mathbb{N}}\mathbb{O}_{d}, the union being a monotone increasing union of sets. Each parameterization of a limit cycle with winding number + 1 +1 belongs to 𝕆 \mathbb{O}, and hence to some 𝕆 p \mathbb{O}_{p} for a finite p p. The set ℙ \mathbb{P}, whose cardinality we would like to bound, is the increasing class of components of the zero set { E = 0 } \{E=0\} in 𝕆 d \mathbb{O}_{d} determined by limit cycles of our differential system ( 1.1). It is important to realize that there are, obviously, many other components in that zero set; for instance, the ones determined by closed curves that consist in running back and forth a piece of an integral curve of the system. However, if we could work in a Hilbert space where feasible parameterizations 𝐮 ⁡ ( t): [0, 1] → ℝ 2 \mathbf{u}(t):[0,1]\to\mathbb{R}^{2} are 𝒞 1 \mathcal{C}^{1} -, and restrict attention to non-singular closed curves | 𝐮 ′ ​ ( t) | > 0 ​ for all ​ t, |\mathbf{u}^{\prime}(t)|>0\hbox{ for all }t, with winding number + 1 +1, i.e. the class 𝕆 \mathbb{O}, then those parameterizations running back and forth a piece of an integral curve lie off 𝕆 \mathbb{O}. It is most relevant to discard them from our horizon. We will see the importance of working with a fixed, finite value for d d, as it introduces a certain “compactness” that is fundamental to discard undesirable behavior when identifying each limit cycle of ( 1.1) with a connected component of { E ϵ ≤ a } \{E_{\epsilon}\leq a\} in 𝕆 d \mathbb{O}_{d}.

The canonical alternative facing such an apparent dead-end is to enlarge our analytical scenario by the consideration of new ingredients. Specifically:

1. (1)

Another Hilbert space ℍ ⊂ 𝕃 \mathbb{H}\subset\mathbb{L} such that 𝕀 ⊂ ℍ \mathbb{I}\subset\mathbb{H}. Associated norms (coming from their respective inner products) are denoted by ∥ ⋅ ∥ ℍ \|\cdot\|_{\mathbb{H}} and ∥ ⋅ ∥ 𝕃 \|\cdot\|_{\mathbb{L}}, respectively. The norm ∥ ⋅ ∥ ℍ \|\cdot\|_{\mathbb{H}} is strictly finer (larger) than the restriction of ∥ ⋅ ∥ 𝕃 \|\cdot\|_{\mathbb{L}} to ℍ \mathbb{H}.

2. (2)

A perturbation E ϵ: ℍ → ℝ + E_{\epsilon}:\mathbb{H}\to\mathbb{R}^{+}, ϵ > 0 \epsilon>0, of E 0 = E E_{0}=E, must be setup so that E ϵ E_{\epsilon}, for each fixed ϵ \epsilon, and 𝕀 \mathbb{I} verify all assumptions in Theorem 2.4; in particular, 𝕀 \mathbb{I} must be invariant for E ϵ E_{\epsilon}, at least for sufficiently small ϵ \epsilon.

Hilbert’s 16th problem 𝕃 \mathbb{L} will be the class of paths with one derivative which is square-integrable, while ℍ \mathbb{H} will be the subset of 𝕃 \mathbb{L} of paths with two derivatives which are square-integrable. The perturbation of E = E 0 E=E_{0} given in ( 1.5) will be taken to be of the canonical form (2.6) E ϵ ​ ( 𝐮) = E 0 ​ ( 𝐮) + ϵ 2 ​ ‖ 𝐮 − 𝐯 0 ‖ 2 E_{\epsilon}(\mathbf{u})=E_{0}(\mathbf{u})+\frac{\epsilon}{2}\|\mathbf{u}-\mathbf{v}_{0}\|^{2} for a suitable smooth path 𝐯 0 \mathbf{v}_{0} to be chosen in an appropriate manner in such a way that the perturbation E ϵ E_{\epsilon} in ( 2.6) and 𝕀 ( = 𝕆 d) \mathbb{I}(=\mathbb{O}_{d}) comply with all assumptions in Theorem 2.4 in the Hilbert space ℍ \mathbb{H}. The norm here is the norm in ℍ \mathbb{H}. There are some advantages and disadvantages to working with E ϵ E_{\epsilon} in ℍ \mathbb{H}. One first important advantage has already been indicated in connection to complying with requirements in Theorem 2.4. As pointed out earlier, there are many components of the zero set { E = 0 } \{E=0\} in 𝕃 \mathbb{L} other than those associated with limit cycles. Every piece of an integral curve of our differential system ( 1.1) run forward and backwards would determine one such component (in 𝕃 \mathbb{L}), and thus we would have infinitely many. However, components of { E = 0 } \{E=0\} in ℍ \mathbb{H} are associated with 𝒞 1 \mathcal{C}^{1} -paths because paths in ℍ \mathbb{H} (the standard Sobolev space H 2 ​ ( [0, 1], ℝ 2) H^{2}([0,1];\mathbb{R}^{2})) are 𝒞 1 \mathcal{C}^{1}, and not just merely absolutely continuous. As an outcome of our results henceforth, we will see that the number of such components in 𝕆 d ⊂ ℍ \mathbb{O}_{d}\subset\mathbb{H} is finite if we stress that paths in 𝕆 d \mathbb{O}_{d} are to be 𝒞 1 \mathcal{C}^{1} - and non-singular with a vector derivative vanishing nowhere. In particular, approximation of paths in 𝕃 \mathbb{L}, which are just absolutely continuous, by non-singular paths in ℍ \mathbb{H}, which are 𝒞 1 \mathcal{C}^{1} -paths avoiding a vanishing derivative, is not possible with a uniformly bounded norm in ℍ \mathbb{H}.

If we succeed in the two above points, we can hence apply Theorem 2.4 to E ϵ E_{\epsilon} and 𝕀 \mathbb{I}, for each fixed ϵ \epsilon. The landscape of critical points for E ϵ E_{\epsilon} in 𝕀 \mathbb{I} may have, however, changed with respect to that of E 0 E_{0}, in a way hard to control. The zero set { E 0 = 0 } \{E_{0}=0\} in Problem 2.3 becomes disfigured with respect to perturbation E ϵ E_{\epsilon} since the zero set for this perturbation is, in general, empty, and so we need to focus rather on sub-level sets of the form { E 0 ≤ a } \{E_{0}\leq a\} for a a, positive and small. Note that

 | { E ϵ ≤ a } ⊂ { E 0 ≤ a }, { E 0 = 0 } ⊂ { E 0 ≤ a } \{E_{\epsilon}\leq a\}\subset\{E_{0}\leq a\},\quad\{E_{0}=0\}\subset\{E_{0}\leq a\} |  |

for every positive ϵ \epsilon and a a. It is clear that if

 | 𝐱 ∈ { E 0 = 0 }, E 0 ( 𝐱) = 0, \mathbf{x}\in\{E_{0}=0\},\quad E_{0}(\mathbf{x})=0, |  |

and a > 0 a>0, then, for ϵ \epsilon small enough,

 | 𝐱 ∈ { E ϵ ≤ a }. \mathbf{x}\in\{E_{\epsilon}\leq a\}. |  |

The same is correct for a finite subset ℙ ′ \mathbb{P}^{\prime} of elements of { E 0 = 0 } \{E_{0}=0\}. In addition, for such a fixed finite set ℙ ′ \mathbb{P}^{\prime} of elements of ℙ \mathbb{P}, there is always a value a ℙ ′ > 0 a_{\mathbb{P}^{\prime}}>0 such that the components of

 | { E ϵ ≤ a }, a < a ℙ ′, \{E_{\epsilon}\leq a\},\quad a<a_{\mathbb{P}^{\prime}}, |  |

identified by the elements of ℙ ′ \mathbb{P}^{\prime}, become disjoint for ϵ \epsilon small enough. In this way, if one can show that the number of connected components of { E ϵ ≤ a } \{E_{\epsilon}\leq a\} eventually becomes independent of a a for sufficiently small ϵ \epsilon, we would have a clear indication that the number of elements of ℙ \mathbb{P} is finite, and most possibly one could find the desired upper bound independent of a a and ϵ \epsilon. Though not explicitly written, in the previous discussion everything takes place in 𝕀 \mathbb{I} as our ambient space, so that sub-level sets are intersected always with 𝕀 \mathbb{I}.

Hilbert’s 16th problem Limit cycles of our polynomial differential system will identify distinguished components of the sub-level set { E ϵ ≤ a } ∩ 𝕆 d \{E_{\epsilon}\leq a\}\cap\mathbb{O}_{d} for every positive, sufficiently small, but fixed a a; every fixed, sufficiently large d d; and E ϵ E_{\epsilon} in ( 2.6) for ϵ \epsilon sufficiently small. However, more and more components of { E ϵ ≤ a } \{E_{\epsilon}\leq a\} in 𝕆 d \mathbb{O}_{d} may occur as a a and ϵ \epsilon become smaller and smaller, and d d larger and larger. If we fix a priori a finite subset ℙ ′ \mathbb{P}^{\prime} of those components determined by a selected finite number of limit cycles of system ( 1.1), there are always values a ℙ ′ > 0 a_{\mathbb{P}^{\prime}}>0, d ℙ ′ ∈ ℕ d_{\mathbb{P}^{\prime}}\in\mathbb{N}, such that the limit cycles corresponding to ℙ ′ \mathbb{P}^{\prime} determine, in a one-to-one manner, disjoint components of { E ϵ ≤ a } \{E_{\epsilon}\leq a\} in 𝕆 d \mathbb{O}_{d} for a < a ℙ ′ a<a_{\mathbb{P}^{\prime}}, d ≥ d ℙ ′ d\geq d_{\mathbb{P}^{\prime}}, given, and for every ϵ \epsilon sufficiently small (depending on a a). If there are values a 0 > 0 a_{0}>0, d 0 ∈ ℕ d_{0}\in\mathbb{N}, with the property that the finite number of components of { E ϵ ≤ a } \{E_{\epsilon}\leq a\} in 𝕆 d \mathbb{O}_{d}, for a < a 0 a<a_{0}, d ≥ d 0 d\geq d_{0}, for every ϵ \epsilon sufficiently small, does not change with a a or with d d, then that would make plausible the fact that our differential system has a finite number of limit cycles. Even more, if we are capable of finding an upper bound on such number of components of { E ϵ ≤ a } ∩ 𝕆 d \{E_{\epsilon}\leq a\}\cap\mathbb{O}_{d} for fixed, but arbitrarily small a a; fixed but arbitrarily large d d; and sufficiently small ϵ \epsilon; independently of a a, d d, and ϵ \epsilon, such a bound will stay as an upper bound for the number of limit cycles. A good way of clarifying all of these statements is to argue that (2.7) #( { E 0 = 0 } ∩ 𝕆 d) ≤ lim a ↘ 0 lim ϵ ↘ 0 #( { E ϵ ≤ a } ∩ 𝕆 d), \#(\{E_{0}=0\}\cap\mathbb{O}_{d})\leq\lim_{a\searrow 0}\lim_{\epsilon\searrow 0}\#(\{E_{\epsilon}\leq a\}\cap\mathbb{O}_{d}), for every (large) d ∈ ℕ d\in\mathbb{N}. #\#stands for the number of components of the corresponding set. Suppose that, through Morse inequalities, we can estimate the right-hand side in ( 2.7) by the number M c ​ r ​ i, a, ϵ, d M_{cri,a,\epsilon,d} of some critical paths in 𝕆 d \mathbb{O}_{d}. Since { 𝕆 d } \{\mathbb{O}_{d}\} is increasingly contained in 𝕆 \mathbb{O}, an upper estimate for M c ​ r ​ i, a, ϵ, d M_{cri,a,\epsilon,d} will lead to (2.8) #( { E 0 = 0 } ∩ 𝕆 d) ≤ lim a ↘ 0 lim ϵ ↘ 0 M c ​ r ​ i, a, ϵ, \#(\{E_{0}=0\}\cap\mathbb{O}_{d})\leq\lim_{a\searrow 0}\lim_{\epsilon\searrow 0}M_{cri,a,\epsilon}, where M c ​ r ​ i, a, ϵ M_{cri,a,\epsilon} are the number of corresponding critical paths in 𝕆 \mathbb{O}. Given that the left-hand side in ( 2.7) is increasing in d d as well, with limit #​ ℙ \#\mathbb{P} as d → ∞ d\to\infty (again by ( 2.5)), by ( 2.8) we see that #⁡ ( ℙ) ≤ lim a ↘ 0 lim ϵ ↘ 0 M c ​ r ​ i, a, ϵ \#(\mathbb{P})\leq\lim_{a\searrow 0}\lim_{\epsilon\searrow 0}M_{cri,a,\epsilon} A main point is then to show that ( 2.7) is correct.

### 2.4. Our guiding principle

We adopt the following standard definition. For the time being, we will take all properties in the statement blindly. We will clearly discuss them later at the right time, and with the necessary care.

###### Definition 2.1.

A functional E: ℍ → ℝ E:\mathbb{H}\to\mathbb{R} is called a Morse functional if it is 𝒞 2 \mathcal{C}^{2} -, non-negative, coercive, enjoys the Palais-Smale property, and has a finite number of critical points over each sub-level set { E ≤ c } \{E\leq c\} for each non-critical value c c, all of which are non-degenerate and with a finite index.

The point is to be able to setup, in a advantageous way, the perturbations E ϵ E_{\epsilon} to succeed in our goal of solving Problem 2.3.

###### Theorem 2.5.

Let E ϵ: ℍ → ℝ + E_{\epsilon}:\mathbb{H}\to\mathbb{R}^{+} be a family of smooth, non-negative, coercive functionals, with 0 ≤ E 0 ≤ E ϵ 0\leq E_{0}\leq E_{\epsilon}, and 𝕆 d \mathbb{O}_{d}, d ∈ ℕ d\in\mathbb{N}, an increasing family of open subsets of ℍ \mathbb{H}. As in ( 2.5), put

 | 𝕆 = ⋃ d ∈ ℕ 𝕆 d. \mathbb{O}=\bigcup_{d\in\mathbb{N}}\mathbb{O}_{d}. |  |

Suppose, in addition, that

1. (1)

E ϵ E_{\epsilon} is a Morse functional for positive ϵ \epsilon.

2. (2)

𝕆 d \mathbb{O}_{d} is invariant for all E ϵ E_{\epsilon} for all large d d, and all ϵ \epsilon.

3. (3)

For every d d, for a a sufficiently small, and ϵ \epsilon small enough (depending on a a):

  1. (a)

Each component of { E 0 = 0 } ∩ 𝕆 d \{E_{0}=0\}\cap\mathbb{O}_{d} identifies (is contained in), in a one-to-one manner, one component of { E ϵ ≤ a } ∩ 𝕆 d \{E_{\epsilon}\leq a\}\cap\mathbb{O}_{d}.

  2. (b)

Each component of { E ϵ ≤ a } ∩ 𝕆 d \{E_{\epsilon}\leq a\}\cap\mathbb{O}_{d} is topologically equivalent to a ball.

Then

(2.9) |  | #⁡ ( ℙ) ≤ 1 + lim a → 0 lim ϵ → 0 M c ​ r ​ i, ϵ, a, \#(\mathbb{P})\leq 1+\lim_{a\to 0}\lim_{\epsilon\to 0}M_{cri,\epsilon,a}, |  |

if M c ​ r ​ i, ϵ, a M_{cri,\epsilon,a} is the number of critical elements of E ϵ E_{\epsilon} in { E ϵ > a } ∩ 𝕆 \{E_{\epsilon}>a\}\cap\mathbb{O}.

###### Proof.

Pick up an arbitrary, finite subset ℙ ′ \mathbb{P}^{\prime} of ℙ \mathbb{P}. By hypothesis, we can find a a, sufficiently small and non-critical for E ϵ E_{\epsilon} 1 1 1 By Sard’s theorem, critical values of smooth functionals have measure zero. We will recall and utilize this fact later., and d d large enough (depending both on ℙ ′ \mathbb{P}^{\prime}), such that for ϵ \epsilon small enough, some of the components of { E ϵ ≤ a } \{E_{\epsilon}\leq a\} in 𝕆 d \mathbb{O}_{d} contain, at most, one and only one of the components identified by ℙ ′ \mathbb{P}^{\prime}. Moreover, for some b ϵ b_{\epsilon} sufficiently large, due to the coercivity of E ϵ E_{\epsilon} in ℍ \mathbb{H}, the big sub-level set { E ϵ ≤ b ϵ } \{E_{\epsilon}\leq b_{\epsilon}\} has a unique connected component which is topologically equivalent to a ball.

Let ℂ i, ϵ, d \mathbb{C}_{i,\epsilon,d}, i ∈ I i\in I, be the full set of disjoint components of { E ϵ ≤ a } \{E_{\epsilon}\leq a\} in 𝕆 d \mathbb{O}_{d}, some of which will correspond to those associated with the selected elements in ℙ ′ \mathbb{P}^{\prime}. Because components of sub-level sets are assumed to be topologically equivalent to a ball and invariant, and the intersection of invariant sets is still invariant, we can apply Theorem 2.4 to E ϵ E_{\epsilon} and each ℂ i, ϵ, d \mathbb{C}_{i,\epsilon,d}, separately for each i ∈ I i\in I, as well as in

 | ℂ ϵ, d = { E ϵ ≤ b ϵ } ∩ 𝕆 d, \mathbb{C}_{\epsilon,d}=\{E_{\epsilon}\leq b_{\epsilon}\}\cap\mathbb{O}_{d}, |  |

to find that

(2.10) |  | ∑ k ( − 1) k ​ M k ​ ( ℂ i, ϵ, d) = 1, ∑ k ( − 1) k ​ M k ​ ( ℂ ϵ, d) = 1, \sum_{k}(-1)^{k}M_{k}(\mathbb{C}_{i,\epsilon,d})=1,\quad\sum_{k}(-1)^{k}M_{k}(\mathbb{C}_{\epsilon,d})=1, |  |

for each i i. The sum in ( 2.4) is additive with respect to disjoint sets where it is considered, and hence

 | ∑ i ∑ k ( − 1) k M k ( ℂ i, ϵ, d) + ∑ k ( − 1) k M k ( ℂ ϵ, d ∖ ∪ i ℂ i, ϵ, d) = ∑ k ( − 1) k M k ( ℂ ϵ, d). \sum_{i}\sum_{k}(-1)^{k}M_{k}(\mathbb{C}_{i,\epsilon,d})+\sum_{k}(-1)^{k}M_{k}(\mathbb{C}_{\epsilon,d}\setminus\cup_{i}\mathbb{C}_{i,\epsilon,d})=\sum_{k}(-1)^{k}M_{k}(\mathbb{C}_{\epsilon,d}). |  |

We conclude, because of ( 2.10), that

 | #( I) + ∑ k ( − 1) k M k ( ℂ ϵ, d ∖ ∪ i ℂ i, ϵ, d) = 1. \#(I)+\sum_{k}(-1)^{k}M_{k}(\mathbb{C}_{\epsilon,d}\setminus\cup_{i}\mathbb{C}_{i,\epsilon,d})=1. |  |

From here, since, again by our hypotheses, each ℂ i, ϵ, d \mathbb{C}_{i,\epsilon,d} cannot contain more than one component of the zero set of E 0 E_{0},

 | #( ℙ ′) ≤ #( I) ≤ 1 + ∑ k M k ( ℂ ϵ, d ∖ ∪ i ℂ i, ϵ, d). \#(\mathbb{P}^{\prime})\leq\#(I)\leq 1+\sum_{k}M_{k}(\mathbb{C}_{\epsilon,d}\setminus\cup_{i}\mathbb{C}_{i,\epsilon,d}). |  |

The sum that remains is the total number of critical points of E ϵ E_{\epsilon} off the union of all the generalized components of { E ϵ ≤ a } ∩ 𝕆 d \{E_{\epsilon}\leq a\}\cap\mathbb{O}_{d}, which is certainly smaller than those in the set

 | { a < E ϵ ≤ b ϵ } ∩ 𝕆. \{a<E_{\epsilon}\leq b_{\epsilon}\}\cap\mathbb{O}. |  |

If we put M c ​ r ​ i, ϵ, a M_{cri,\epsilon,a} for such total number of critical points of E ϵ E_{\epsilon} in 𝕆 \mathbb{O} with critical value uniformly away from zero, i.e. the number of critical points of E ϵ E_{\epsilon} in the subset { a < E ϵ } ∩ 𝕆 \{a<E_{\epsilon}\}\cap\mathbb{O}, then we recover the upper bound

(2.11) |  | #⁡ ( ℙ ′) ≤ 1 + M c ​ r ​ i, ϵ, a. \#(\mathbb{P}^{\prime})\leq 1+M_{cri,\epsilon,a}. |  |

The arbitrariness of ℙ ′ \mathbb{P}^{\prime}, a a and ϵ \epsilon under the established conditions finishes the proof. ∎

If the number M c ​ r ​ i, ϵ, a M_{cri,\epsilon,a} admits further an upper bound M c ​ r ​ i M_{cri} independent of ϵ \epsilon and of a a, as they become small, respectively, in the appropriate order, in terms of the defining properties of ℙ \mathbb{P}, then the full subset ℙ \mathbb{P} of those special components of the level set { E 0 = 0 } \{E_{0}=0\} is finite and

 | #⁡ ( ℙ) ≤ 1 + M c ​ r ​ i. \#(\mathbb{P})\leq 1+M_{cri}. |  |

This is our desired goal in connection with Problem 2.3.

###### Problem 2.6.

Let E ϵ: ℍ → ℝ + E_{\epsilon}:\mathbb{H}\to\mathbb{R}^{+} be a perturbation of E 0 E_{0} with 0 ≤ E 0 ≤ E ϵ 0\leq E_{0}\leq E_{\epsilon}, and 𝕆 d ⊂ ℍ \mathbb{O}_{d}\subset\mathbb{H}, complying with the hypotheses in Theorem 2.5. Find an upper bound M c ​ r ​ i M_{cri} on the number of critical elements of E ϵ E_{\epsilon} in 𝕆 \mathbb{O} with critical value uniformly (with respect to ϵ \epsilon) away from zero, which is independent of ϵ \epsilon, i.e.

 | lim ϵ → 0 M c ​ r ​ i, ϵ, a ≤ M c ​ r ​ i \lim_{\epsilon\to 0}M_{cri,\epsilon,a}\leq M_{cri} |  |

for every fixed a a, sufficiently small.

Hilbert’s 16th problem To sum up, we have already given in ( 2.6) the form of the perturbations E ϵ E_{\epsilon} of E 0 E_{0}, the ambient space ℍ \mathbb{H}, and the subset 𝕆 d \mathbb{O}_{d} of smooth, non-singular parameterizations with winding number + 1 +1, and a maximum number d d of full rounds of the tangent vector in either sense. Our job consists of showing that all requirements in Theorem 2.5 are met, and then find the upper bound M c ​ r ​ i M_{cri} in Problem 2.6.

### 2.5. The general setting

As seen in the previous subsection, the clue to the success of our strategy is to be able to count the critical points of the smooth, perturbed functional E ϵ E_{\epsilon} with critical value uniformly away from zero, i.e. the critical points in the super-level set { a < E ϵ } ∩ 𝕆 \{a<E_{\epsilon}\}\cap\mathbb{O} with a > 0 a>0 fixed, small but otherwise arbitrary; and ϵ \epsilon arbitrarily small. To advance in this issue, one needs to understand the nature of critical points for E ϵ E_{\epsilon}, and this forces us to be more specific about the nature of spaces ℍ \mathbb{H}, 𝕃 \mathbb{L}, and functionals E = E 0 E=E_{0} and E ϵ E_{\epsilon}, as well as invariant sets 𝕆 d \mathbb{O}_{d}.

The class of functionals better known in Analysis are local, integral functionals of the standard form

 | E ⁡ ( 𝐮) = ∫ 0 1 F ⁡ ( t, 𝐮 ⁡ ( t), 𝐮 ′ ​ ( t), …, 𝐮 OPEN k) ​ ( t)) ​ 𝑑 t. E(\mathbf{u})=\int_{0}^{1}F(t,\mathbf{u}(t),\mathbf{u}^{\prime}(t),\dots,\mathbf{u}^{k)}(t))\,dt. |  |

We have just written E E as a one-dimensional functional because this is the situation we are interested in here. k k is the highest order of derivatives explicitly participating in the functional. We have also normalized the interval of integration to the unit interval [0, 1] [0,1]. We will restrict attention, to avoid such great generality, to the situation in which

(2.12) |  | E ⁡ ( 𝐮) = ∫ 0 1 F ⁡ ( t, 𝐮 ⁡ ( t), 𝐮 ′ ​ ( t)) ​ 𝑑 t E(\mathbf{u})=\int_{0}^{1}F(t,\mathbf{u}(t),\mathbf{u}^{\prime}(t))\,dt |  |

is a first-order, one-dimensional functional defined for planar paths

 | 𝐮 ⁡ ( t) = ( u 1 ​ ( t), u 2 ​ ( t)) \mathbf{u}(t)=(u_{1}(t),u_{2}(t)) |  |

belonging to a suitable Hilbert space, and for a certain integrand

 | F ⁡ ( t, 𝐮, 𝐯): [0, 1] × ℝ 2 × ℝ 2 → ℝ +. F(t,\mathbf{u},\mathbf{v}):[0,1]\times\mathbb{R}^{2}\times\mathbb{R}^{2}\to\mathbb{R}^{+}. |  |

The natural Hilbert space is

 | 𝕃 = H O 1 ​ ( [0, 1], ℝ 2) \mathbb{L}=H^{1}_{O}([0,1];\mathbb{R}^{2}) |  |

of periodic paths, 𝐮 ⁡ ( 0) = 𝐮 ⁡ ( 1) \mathbf{u}(0)=\mathbf{u}(1) (but this common value is undetermined), with a weak first derivative 𝐮 ′ ​ ( t) \mathbf{u}^{\prime}(t) which is square-integrable in the unit interval

 | ∫ 0 1 | 𝐮 ′ ​ ( t) | 2 ​ 𝑑 t < ∞. \int_{0}^{1}|\mathbf{u}^{\prime}(t)|^{2}\,dt<\infty. |  |

Hilbert’s 16th problem The integrand corresponding to ( 1.5) is (2.13) F ⁡ ( t, 𝐮, 𝐯) = 1 2 ​ ( 𝐯 ⋅ 𝐅 ⟂ ​ ( 𝐮)) 2, 𝐅 = ( P, Q), 𝐅 ⟂ = ( − Q, P). F(t,\mathbf{u},\mathbf{v})=\frac{1}{2}(\mathbf{v}\cdot\mathbf{F}^{\perp}(\mathbf{u}))^{2},\quad\mathbf{F}=(P,Q),\mathbf{F}^{\perp}=(-Q,P).

There is something wrong, from our perspective in this paper, with such integrand F F in ( 2.13) in the sense that corresponding functional E E in ( 2.12) does not comply with assumptions in Theorem 2.4, as announced earlier. One needs to perturb it and pass down to a better space of paths, namely

(2.14) |  | ℍ = H O 2 ​ ( [0, 1], ℝ 2), E ϵ ​ ( 𝐮) = E ⁡ ( 𝐮) + ϵ 2 ​ ‖ 𝐮 − 𝐯 0 ‖ ℍ 2. \mathbb{H}=H^{2}_{O}([0,1];\mathbb{R}^{2}),\quad E_{\epsilon}(\mathbf{u})=E(\mathbf{u})+\frac{\epsilon}{2}\|\mathbf{u}-\mathbf{v}_{0}\|^{2}_{\mathbb{H}}. |  |

H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}) is the space of paths with a weak second derivative 𝐮 ′′ ​ ( t) \mathbf{u}^{\prime\prime}(t) that is square-integrable

 | ∫ 0 1 | 𝐮 ′′ ​ ( t) | 2 ​ 𝑑 t < ∞, \int_{0}^{1}|\mathbf{u}^{\prime\prime}(t)|^{2}\,dt<\infty, |  |

which are periodic

 | 𝐮 ⁡ ( 0) = 𝐮 ⁡ ( 1), 𝐮 ′ ​ ( 0) = 𝐮 ′ ​ ( 1). \mathbf{u}(0)=\mathbf{u}(1),\quad\mathbf{u}^{\prime}(0)=\mathbf{u}^{\prime}(1). |  |

The specific path 𝐯 0 ​ ( t) ∈ ℍ \mathbf{v}_{0}(t)\in\mathbb{H} is to be chosen in an appropriate way to ensure that Theorem 2.4 can, this time, be applied to E ϵ E_{\epsilon} in ℍ \mathbb{H}. In this way, the perturbed functionals become of second order. These are of the general form

(2.15) |  | E ⁡ ( 𝐮) = ∫ 0 1 F ⁡ ( t, 𝐮 ⁡ ( t), 𝐮 ′ ​ ( t), 𝐮 ′′ ​ ( t)) ​ 𝑑 t. E(\mathbf{u})=\int_{0}^{1}F(t,\mathbf{u}(t),\mathbf{u}^{\prime}(t),\mathbf{u}^{\prime\prime}(t))\,dt. |  |

Hilbert’s 16th problem We will be working with the explicit perturbation E ϵ ​ ( 𝐮) = E 0 ​ ( 𝐮) + ϵ 2 ​ ∫ 0 1 [| 𝐮 ′′ ​ ( t) − 𝐯 0 ′′ ​ ( t) | 2 + | 𝐮 ′ ​ ( t) − 𝐯 0 ′ ​ ( t) | 2 + | 𝐮 ⁡ ( t) − 𝐯 0 ​ ( t) | 2] ​ 𝑑 t. E_{\epsilon}(\mathbf{u})=E_{0}(\mathbf{u})+\frac{\epsilon}{2}\int_{0}^{1}[|\mathbf{u}^{\prime\prime}(t)-\mathbf{v}^{\prime\prime}_{0}(t)|^{2}+|\mathbf{u}^{\prime}(t)-\mathbf{v}^{\prime}_{0}(t)|^{2}+|\mathbf{u}(t)-\mathbf{v}_{0}(t)|^{2}]\,dt.

In addition to this passage to second-order problems, there are three main issues worth realizing.

1. (1)

The choice for 𝕆 d \mathbb{O}_{d}. Recall that 𝕆 \mathbb{O} is the non-decreasing union of the 𝕆 d \mathbb{O}_{d} ’s.

Hilbert’s 16th problem Since our main concern is focused on limit cycles of planar, polynomial vector fields, we will consider the set 𝕆 d \mathbb{O}_{d} as the subset of H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}) of non-singular paths (or parameterizations) with winding number + 1 +1, and a maximum number d d of full rounds of the tangent vector in either sense. The concept of winding number goes back to Whitney [51] who formalized it and proved its main properties. The limit cycles we are interested in counting definitely have winding number +1 (run counter-clockwise). Our counting procedure will take place in 𝕆 d \mathbb{O}_{d}, which will be shown to be an open subset of H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}).

1. (2)

A main point in this part of our development is to understand how to set up and manipulate the equation for critical paths of integral functionals as the ones written above. It is something well-known that we are talking about systems of ODEs of order four.

2. (3)

The fact that the perturbed functionals E ϵ E_{\epsilon} are of the form ( 2.14) with a norm in ℍ \mathbb{H} which is finer than the norm in 𝕃 \mathbb{L}, carries us to face singularly-perturbed problems and their asymptotic behavior as ϵ → 0 \epsilon\to 0. This is a delicate area that asks for fine points in arguments.

### 2.6. The concrete setting, and the full program

We have already introduced the final ingredient to be specified in order to have a full description of the situation. The basic functional E = E 0 E=E_{0} is of the form ( 2.12)

 | F ⁡ ( t, 𝐮, 𝐯) = 1 2 ​ ( 𝐯 ⋅ 𝐅 ⟂ ​ ( 𝐮)) 2, E ⁡ ( 𝐮) = ∫ 0 1 1 2 ​ ( 𝐮 ′ ​ ( t) ⋅ 𝐅 ⟂ ​ ( 𝐮 ⁡ ( t))) 2 ​ 𝑑 t, F(t,\mathbf{u},\mathbf{v})=\frac{1}{2}(\mathbf{v}\cdot\mathbf{F}^{\perp}(\mathbf{u}))^{2},\quad E(\mathbf{u})=\int_{0}^{1}\frac{1}{2}(\mathbf{u}^{\prime}(t)\cdot\mathbf{F}^{\perp}(\mathbf{u}(t)))^{2}\,dt, |  |

if

 | 𝐅 ⁡ ( x, y) = ( P ⁡ ( x, y), Q ⁡ ( x, y)) \mathbf{F}(x,y)=(P(x,y),Q(x,y)) |  |

is the given polynomial planar field, and

 | 𝐅 ⟂ ​ ( x, y) = ( − Q ⁡ ( x, y), P ⁡ ( x, y)). \mathbf{F}^{\perp}(x,y)=(-Q(x,y),P(x,y)). |  |

It is pretty clear that if 𝐮 \mathbf{u} is a limit cycle, reparameterized in the unit interval for normalization, of the differential system ( 1.1) with right-hand side 𝐅 \mathbf{F}, then 𝐮 ∈ 𝕆 \mathbf{u}\in\mathbb{O} and E ⁡ ( 𝐮) = 0 E(\mathbf{u})=0. The type of perturbations that we will be dealing with is

 | E ϵ ​ ( 𝐮) = E ⁡ ( 𝐮) + ϵ 2 ​ ∫ 0 1 ( | 𝐮 ′′ ​ ( t) − 𝐯 0 ′′ ​ ( t) | 2 + | 𝐮 ′ ​ ( t) − 𝐯 0 ′ ​ ( t) | 2 + | 𝐮 ⁡ ( t) − 𝐯 0 ​ ( t) | 2) ​ 𝑑 t, E_{\epsilon}(\mathbf{u})=E(\mathbf{u})+\frac{\epsilon}{2}\int_{0}^{1}\left(|\mathbf{u}^{\prime\prime}(t)-\mathbf{v}^{\prime\prime}_{0}(t)|^{2}+|\mathbf{u}^{\prime}(t)-\mathbf{v}^{\prime}_{0}(t)|^{2}+|\mathbf{u}(t)-\mathbf{v}_{0}(t)|^{2}\right)\,dt, |  |

as indicated above, where the auxiliary path 𝐯 0 ∈ 𝕆 \mathbf{v}_{0}\in\mathbb{O} will be suitably chosen.

For the sake of readers not familiar with these facts, we include the following statement which have been mentioned earlier.

###### Proposition 2.7.

Paths in H 1 ​ ( [0, 1], ℝ 2) H^{1}([0,1];\mathbb{R}^{2}) are absolutely continuous. Paths in H 2 ​ ( [0, 1], ℝ 2) H^{2}([0,1];\mathbb{R}^{2}) are 𝒞 1 \mathcal{C}^{1} with a derivative 𝐮 ′ \mathbf{u}^{\prime} which is absolutely continuous.

###### Proof.

Note that

 | | 𝐮 ⁡ ( r) − 𝐮 ⁡ ( s) | ≤ ∫ s r | 𝐮 ′ ​ ( t) | ​ 𝑑 t ≤ r − s ​ ( ∫ 0 1 | 𝐮 ′ ​ ( t) | 2 ​ 𝑑 t) 1 / 2 |\mathbf{u}(r)-\mathbf{u}(s)|\leq\int_{s}^{r}|\mathbf{u}^{\prime}(t)|\,dt\leq\sqrt{r-s}\left(\int_{0}^{1}|\mathbf{u}^{\prime}(t)|^{2}\,dt\right)^{1/2} |  |

for 𝐮 ∈ H 1 ​ ( [0, 1], ℝ 2) \mathbf{u}\in H^{1}([0,1];\mathbb{R}^{2}). Hence 𝐮 \mathbf{u} is absolutely continuous. The same inequality replacing 𝐮 \mathbf{u} and 𝐮 ′ \mathbf{u}^{\prime} by 𝐮 ′ \mathbf{u}^{\prime} and 𝐮 ′′ \mathbf{u}^{\prime\prime}, respectively, when 𝐮 ∈ H 2 ​ ( [0, 1], ℝ 2) \mathbf{u}\in H^{2}([0,1];\mathbb{R}^{2}), shows the second part. ∎

At this stage, we are ready to specify the program we would like to cover to its fulfillment for the proof of our central result Theorem 1.1.

1. (1)

Show how to select auxiliary path 𝐯 0 \mathbf{v}_{0} to ensure that E ϵ E_{\epsilon} is eligible for Theorems 2.4 and 2.5. In particular,

  1. (a)

Argue that 𝕆 d \mathbb{O}_{d} is open and invariant for each E ϵ E_{\epsilon}, for d d large enough independently of ϵ \epsilon.

  2. (b)

For a a small, ϵ \epsilon, small enough, and every fixed d ∈ ℕ d\in\mathbb{N}:

    1. (i)

Components of { E ϵ ≤ a } ∩ 𝕆 d \{E_{\epsilon}\leq a\}\cap\mathbb{O}_{d} are topologically equivalent to a ball.

    2. (ii)

Components of { E 0 = 0 } ∩ 𝕆 d \{E_{0}=0\}\cap\mathbb{O}_{d} determine, in a one-to-one manner, components of { E ϵ ≤ a } ∩ 𝕆 d \{E_{\epsilon}\leq a\}\cap\mathbb{O}_{d}.

2. (2)

Determine the equation for critical paths for E 0 E_{0} and E ϵ E_{\epsilon}.

3. (3)

Find an upper bound for the critical paths of E ϵ E_{\epsilon} in 𝕆 \mathbb{O} with critical value uniformly away (with respect to ϵ \epsilon) from zero in the following way:

  1. (a)

Show that critical values of E ϵ E_{\epsilon} in 𝕆 \mathbb{O} uniformly away from zero (with respect to ϵ \epsilon) are such that E 0 E_{0} is also uniformly away from zero.

  2. (b)

Examine the possible asymptotic limits, as ϵ ↘ 0 \epsilon\searrow 0, of such families of critical paths with critical values uniformly away from zero, through the limit equation as in typical singularly-perturbed differential problems.

  3. (c)

For each asymptotic limit in the previous item, find an upper bound on the number of possible branches converging to each such limit.

Hilbert’s 16th problem As indicated earlier in several places, our specific family of functionals is given by (2.16) ∫ 0 1 1 2 ​ ( 𝐅 ⟂ ​ ( 𝐮 ⁡ ( t)) ⋅ 𝐮 ′ ​ ( t)) 2 ​ 𝑑 t + \displaystyle\int_{0}^{1}\frac{1}{2}(\mathbf{F}^{\perp}(\mathbf{u}(t))\cdot\mathbf{u}^{\prime}(t))^{2}\,dt+ ϵ 2 ​ ∫ 0 1 [| 𝐮 ′′ ​ ( t) − 𝐯 0 ′′ ​ ( t) | 2 + | 𝐮 ′ ​ ( t) − 𝐯 0 ′ ​ ( t) | 2 + | 𝐮 ⁡ ( t) − 𝐯 0 ​ ( t) | 2] ​ 𝑑 t \displaystyle\frac{\epsilon}{2}\int_{0}^{1}[|\mathbf{u}^{\prime\prime}(t)-\mathbf{v}^{\prime\prime}_{0}(t)|^{2}+|\mathbf{u}^{\prime}(t)-\mathbf{v}^{\prime}_{0}(t)|^{2}+|\mathbf{u}(t)-\mathbf{v}_{0}(t)|^{2}]\,dt where 𝐅 ⁡ ( x, y) = ( P ⁡ ( x, y), Q ⁡ ( x, y)), \displaystyle\mathbf{F}(x,y)=(P(x,y),Q(x,y)), 𝐅 ⟂ ​ ( x, y) = ( − Q ⁡ ( x, y), P ⁡ ( x, y)), 𝐮 = ( x, y). \displaystyle\mathbf{F}^{\perp}(x,y)=(-Q(x,y),P(x,y)),\quad\mathbf{u}=(x,y). We will be especially interested in showing the following: (1) show that E 0 ′ ​ ( 𝐮 ϵ) → 𝟎 ​ in ​ H 2 ​ ( [0, 1], ℝ 2) E^{\prime}_{0}(\mathbf{u}_{\epsilon})\to\mathbf{0}\hbox{ in }H^{2}([0,1];\mathbb{R}^{2}) for every branch of critical paths 𝐮 ϵ \mathbf{u}_{\epsilon} of E ϵ E_{\epsilon}, and that the numbers E 0 ​ ( 𝐮 ϵ) E_{0}(\mathbf{u}_{\epsilon}) are uniformly away from zero; (2) based on the important information of the previous item, make a full, concrete description of the possible limit behaviors of branches of critical paths 𝐮 ϵ \mathbf{u}_{\epsilon} in terms of features of the differential system ( 1.1); and (3) for each possible limit behavior of such branches in the previous item, argue that there cannot be more than ( n − 1) 2 (n-1)^{2} branches of critical, non-minimizer paths.

Note that singularly-perturbed problems for critical points, and not just for minimizers, are not usually treated. In addition, formal proofs of results for such perturbation problems, under periodicity conditions, are not easy to find. Most of the time in the literature, calculations are informal, even more so under periodic end-point conditions.

There is an additional, final simple step for our program to take care of a non-generic situation for a full proof of Theorem 1.2 (Subsection 5.10).

## 3. Abstract results

We gather in this section those results that can be shown in an abstract setting without specifying the nature of spaces or functionals. The fundamental result that is driving us in this section is Theorem 2.4 which we restate below.

There is even a more general statement than Theorem 2.4 that incorporates some fundamental topological invariants like the Euler characteristic, the Betti numbers, etc, and that can be stated in the context of infinite-dimensional manifolds ( [9], [39] - [41]). Since all that we need for our goal in this article is inequality ( 3.1) in Theorem 3.1 below, we will restrict attention to the situation in the statement, and forget about those more general cases. Our plan is then to define and discuss the concepts involved in Definition 2.1, which are mentioned in this statement of Theorem 3.1 in preparation to prove those conditions for a perturbation E ϵ E_{\epsilon} of a given initial functional E 0 E_{0}. Our discussion is intended right to the point with a minimal number of elements for a full and rigorous proof. Recall (Definition 2.1) that a functional E: ℍ → ℝ E:\mathbb{H}\to\mathbb{R} defined in a Hilbert space ℍ \mathbb{H} is called a Morse functional if:

- •

it is 𝒞 2 \mathcal{C}^{2} -, non-negative, coercive;

- •

it enjoys the Palais-Smale property;

- •

it has a finite number of critical points over each sub-level set { E ≤ c } \{E\leq c\} for each non-critical value c c, all of which are non-degenerate and with a finite index.

### 3.1. Morse inequalities

Morse inequalities in the full space ℍ \mathbb{H} (Theorem 2.2) is such a classical result that we will take it for granted without proof. In an infinite-dimensional setting, it can be found in several places, for instance, Corollary (6.5.10) of [4] or Theorem 4.3 of Chapter 1 in [9]. As a matter of fact, our above version of Morse inequalities restricted to an invariant set 𝕀 \mathbb{I} is not easy to find as such. Corollary (6.5.11) of [4] is a particular version of it when 𝕀 \mathbb{I} is an invariant ball in ℍ \mathbb{H}. The proof of this case in that reference [4], however, makes it very clear that the result is valid not just for a ball, but for a general invariant subset 𝕀 \mathbb{I} which is topologically equivalent to a ball.

###### Theorem 3.1.

Let E: ℍ → ℝ E:\mathbb{H}\to\mathbb{R} be a Morse functional (according to Definition 2.1) over a Hilbert space ℍ \mathbb{H}. Let 𝕀 \mathbb{I} be open, topologically equivalent to a ball, E E -invariant, and put M k ​ ( 𝕀) M_{k}(\mathbb{I}) for the (finite) number of critical points of E E in 𝕀 \mathbb{I}, for each fixed index k k. Then

 | M 0 ( 𝕀) ≥ 1, M 1 ( 𝕀) − M 0 ( 𝕀) ≥ − 1, M 2 ( 𝕀) − M 1 ( 𝕀) + M 0 ( 𝕀) ≥ 1, …, \displaystyle M_{0}(\mathbb{I})\geq 1,\quad M_{1}(\mathbb{I})-M_{0}(\mathbb{I})\geq-1,\quad M_{2}(\mathbb{I})-M_{1}(\mathbb{I})+M_{0}(\mathbb{I})\geq 1,\quad\dots, |  |

(3.1) |  | ∑ k = 0 ∞ ( − 1) k ​ M k ​ ( 𝕀) = 1. \displaystyle\sum_{k=0}^{\infty}(-1)^{k}M_{k}(\mathbb{I})=1. |  |

###### Proof.

If a set 𝕀 \mathbb{I} is invariant for a Morse functional E E, every concept or fact that depends exclusively on the flow of − E -E can be restricted to 𝕀 \mathbb{I} without change. On the other hand, since 𝕀 \mathbb{I} is topologically equivalent to a ball, all of its homology groups coincide with those of the full space ℍ \mathbb{H}. Since Morse inequalities depend on those topological invariants, they remain valid when restricted to such invariant sets. ∎

When a certain base functional E 0 E_{0} does not comply with the hypotheses of Theorem 3.1, there is a general, abstract procedure that permits to perturb it appropriately in such a way that the resulting perturbation E ϵ E_{\epsilon} turns out to be a Morse functional, i.e. all of above requirements in Definition 2.1 and Theorem 3.1 hold for E ϵ E_{\epsilon}. In addition, we would have to be convinced that the topology of sub-level sets { E 0 ≤ a } \{E_{0}\leq a\} for a a near the absolute minimum of E 0 E_{0} is not changed when we replace E 0 E_{0} by E ϵ E_{\epsilon}.

### 3.2. Main concepts

The statement of Theorem 3.1 based on Definition 2.1, involves the notion of Morse index for a non-degenerate critical point of a smooth functional defined on a Hilbert space. Unless otherwise explicitly stated, we will take, throughout this section, E: ℍ → ℝ E:\mathbb{H}\to\mathbb{R} to be a functional defined in an abstract Hilbert space ℍ \mathbb{H} with elements 𝐮 \mathbf{u}.

###### Definition 3.1.

1. (1)

E E is coercive if

 | E ⁡ ( 𝐮) → ∞ ​ as ​ ‖ 𝐮 ‖ → ∞. E(\mathbf{u})\to\infty\hbox{ as }\|\mathbf{u}\|\to\infty. |  |

2. (2)

E E is 𝒞 1 \mathcal{C}^{1} if for every 𝐮 ∈ ℍ \mathbf{u}\in\mathbb{H} there is a linear functional

 | E ′ ​ ( 𝐮): ℍ → ℝ E^{\prime}(\mathbf{u}):\mathbb{H}\to\mathbb{R} |  |

such that

 | 1 ‖ 𝐯 ‖ ​ ‖ E ⁡ ( 𝐯) − ⟨ E ′ ​ ( 𝐮), 𝐯 ⟩ − E ⁡ ( 𝐮) ‖ → 0 ​ as | 𝐯 | → 0. \frac{1}{\|\mathbf{v}\|}\|E(\mathbf{v})-\langle E^{\prime}(\mathbf{u}),\mathbf{v}\rangle-E(\mathbf{u})\|\to 0\hbox{ as }\|\mathbf{v}\|\to 0. |  |

The Riesz representation theorem implies that E ′ ​ ( 𝐮) ∈ ℍ E^{\prime}(\mathbf{u})\in\mathbb{H}.

3. (3)

An element 𝐮 ∈ ℍ \mathbf{u}\in\mathbb{H} is a critical point of a 𝒞 1 \mathcal{C}^{1} -functional E E if

 | E ′ ​ ( 𝐮) = 𝟎 ∈ ℍ. E^{\prime}(\mathbf{u})=\mathbf{0}\in\mathbb{H}. |  |

A real number c ∈ ℝ c\in\mathbb{R} is a critical value of E E if there is a critical point 𝐮 \mathbf{u}, E ′ ​ ( 𝐮) = 𝟎 E^{\prime}(\mathbf{u})=\mathbf{0}, such that c = E ⁡ ( 𝐮) c=E(\mathbf{u}).

4. (4)

E E is 𝒞 2 \mathcal{C}^{2} if it is 𝒞 1 \mathcal{C}^{1}, and for each 𝐮 ∈ ℍ \mathbf{u}\in\mathbb{H}, there is a bilinear, symmetric map

 | E ′′ ​ ( 𝐮): ℍ × ℍ → ℝ E^{\prime\prime}(\mathbf{u}):\mathbb{H}\times\mathbb{H}\to\mathbb{R} |  |

such that

 | 1 ‖ 𝐯 ‖ 2 ​ ‖ E ⁡ ( 𝐮) − E ′′ ​ ( 𝐮) ​ ( 𝐯, 𝐯) − ⟨ E ′ ​ ( 𝐮), 𝐯 ⟩ − E ⁡ ( 𝐮) ‖ → 0 ​ as | 𝐯 | → 0. \frac{1}{\|\mathbf{v}\|^{2}}\|E(\mathbf{u})-E^{\prime\prime}(\mathbf{u})(\mathbf{v},\mathbf{v})-\langle E^{\prime}(\mathbf{u}),\mathbf{v}\rangle-E(\mathbf{u})\|\to 0\hbox{ as }\|\mathbf{v}\|\to 0. |  |

Again by the Riesz representation theorem, one can interpret the Hessian E ′′ ​ ( 𝐮) E^{\prime\prime}(\mathbf{u}) as a linear map

 | E ′′ ​ ( 𝐮): ℍ → ℍ, ⟨ E ′′ ​ ( 𝐮) ​ 𝐯, 𝐰 ⟩ = E ′′ ​ ( 𝐮) ​ ( 𝐯, 𝐰). E^{\prime\prime}(\mathbf{u}):\mathbb{H}\to\mathbb{H},\quad\langle E^{\prime\prime}(\mathbf{u})\mathbf{v},\mathbf{w}\rangle=E^{\prime\prime}(\mathbf{u})(\mathbf{v},\mathbf{w}). |  |

Suppose E: ℍ → ℝ E:\mathbb{H}\to\mathbb{R} is a non-negative, coercive, 𝒞 2 \mathcal{C}^{2} -functional defined over a Hilbert space ℍ \mathbb{H}. Let 𝐮 ∈ ℍ \mathbf{u}\in\mathbb{H} be a critical point of E E, i.e. E ′ ​ ( 𝐮) = 𝟎 E^{\prime}(\mathbf{u})=\mathbf{0}.

###### Definition 3.2.

A critical point 𝐮 ∈ ℍ \mathbf{u}\in\mathbb{H} of E E is called non-degenerate is the self-adjoint operator E ′′ ​ ( 𝐮): ℍ → ℍ E^{\prime\prime}(\mathbf{u}):\mathbb{H}\to\mathbb{H} is invertible. Otherwise, 𝐮 \mathbf{u} is said to be degenerate. When the number of negative eigenvalues of E ′′ ​ ( 𝐮) E^{\prime\prime}(\mathbf{u}) is finite, such number is called the ( Morse) index of 𝐮 \mathbf{u}.

A main, indispensable condition for Morse theory to hold is the Palais-Smale condition. It enables the passage of typical arguments in finite dimension to an infinite-dimensional setting. For a general, smooth 𝒞 1 \mathcal{C}^{1} - functional E: ℍ → ℝ, E:\mathbb{H}\to\mathbb{R}, this important compactness property reads:

If for a sequence { 𝐮 j } \{\mathbf{u}_{j}\} we have that E ⁡ ( 𝐮 j) ≤ K E(\mathbf{u}_{j})\leq K for all j j and a fixed positive constant K K, and E ′ ​ ( 𝐮 j) → 𝟎 E^{\prime}(\mathbf{u}_{j})\to\mathbf{0} as j → ∞ j\to\infty, then a certain subsequence of { 𝐮 j } \{\mathbf{u}_{j}\} converges (strongly) in ℍ \mathbb{H}.

If E E is coercive, we can replace the boundedness of E E along the sequence { 𝐮 j } \{\mathbf{u}_{j}\} by the uniform boundedness of { 𝐮 j } \{\mathbf{u}_{j}\} in ℍ \mathbb{H}.

Though we have already talked about invariant sets of functionals in Theorem 3.1, for the sake of completeness we include here a more formal, precise definition. Suppose E: ℍ → ℝ E:\mathbb{H}\to\mathbb{R} is a 𝒞 2 \mathcal{C}^{2} -functional, and consider the steepest-descent flow 𝐗 \mathbf{X} of − E -E, i.e.

 | 𝐗 ′ ​ ( t, 𝐮) = − E ′ ​ ( 𝐗 ⁡ ( t, 𝐮)) ​ for ​ t > 0, 𝐗 ⁡ ( 0, 𝐮) = 𝐮. \mathbf{X}^{\prime}(t,\mathbf{u})=-E^{\prime}(\mathbf{X}(t,\mathbf{u}))\hbox{ for }t>0,\quad\mathbf{X}(0,\mathbf{u})=\mathbf{u}. |  |

The regularity assumed on E E implies that the flow is defined for every positive t t. For fixed positive t t, the mapping

 | 𝐗 ⁡ ( t, ⋅): ℍ → ℍ \mathbf{X}(t,\cdot):\mathbb{H}\to\mathbb{H} |  |

can be easily shown to be 𝒞 1 \mathcal{C}^{1}. This is standard.

###### Definition 3.3.

A connected open subset 𝕊 ⊂ ℍ \mathbb{S}\subset\mathbb{H} is said to be E E -invariant, for a 𝒞 2 \mathcal{C}^{2} -functional E E, if its boundary ∂ 𝕊 \partial\mathbb{S} does not contain a critical point of E E, and

 | 𝐗 ⁡ ( t, 𝕊) ⊂ 𝕊 \mathbf{X}(t,\mathbb{S})\subset\mathbb{S} |  |

for all positive t t. The intersection of E E -invariant sets is also E E -invariant. When one deals with one functional, we will simply talk about invariant sets.

Note that connected components of sublevel sets

 | { E ≤ c } = { 𝐮 ∈ ℍ: E ( 𝐮) ≤ c } \{E\leq c\}=\{\mathbf{u}\in\mathbb{H}:E(\mathbf{u})\leq c\} |  |

for a non-critical value c c are invariant. If they are intersected with an additional invariant set, they remain invariant.

### 3.3. Perturbation

Suppose we have two nested Hilbert spaces ℍ ⊂ 𝕃 \mathbb{H}\subset\mathbb{L} with associated norms (coming from their respective inner products) ∥ ⋅ ∥ ℍ \|\cdot\|_{\mathbb{H}} and ∥ ⋅ ∥ 𝕃 \|\cdot\|_{\mathbb{L}}, respectively. The norm ∥ ⋅ ∥ ℍ \|\cdot\|_{\mathbb{H}} is strictly finer (larger) than the restriction of ∥ ⋅ ∥ 𝕃 \|\cdot\|_{\mathbb{L}} to ℍ \mathbb{H}. We take as a fact that bounded sequences in ℍ \mathbb{H} are relatively compact in 𝕃 \mathbb{L}. The norm ∥ ⋅ ∥ \|\cdot\| always means ∥ ⋅ ∥ ℍ \|\cdot\|_{\mathbb{H}}.

Let E 0: 𝕃 → ℝ E_{0}:\mathbb{L}\to\mathbb{R} be a certain non-negative, 𝒞 2 \mathcal{C}^{2} -functional. It turns out that E 0 E_{0} is far from being a Morse functional so that Theorem 3.1 cannot be applied to it. Our intention is to perturb it through an additional term of the form

 | E ~ ϵ: ℍ → ℝ, E ~ ϵ ​ ( 𝐮) = E 0 ​ ( 𝐮) + ϵ 2 ​ ‖ 𝐮 ‖ ℍ 2 \tilde{E}_{\epsilon}:\mathbb{H}\to\mathbb{R},\quad\tilde{E}_{\epsilon}(\mathbf{u})=E_{0}(\mathbf{u})+\frac{\epsilon}{2}\|\mathbf{u}\|_{\mathbb{H}}^{2} |  |

and show that a choice 𝐯 0 ∈ ℍ \mathbf{v}_{0}\in\mathbb{H} is possible in such a way that the modified functional

 | E ϵ: ℍ → ℝ, E ϵ ​ ( 𝐮) = E 0 ​ ( 𝐮) + ϵ 2 ​ ‖ 𝐮 − 𝐯 0 ‖ ℍ 2 E_{\epsilon}:\mathbb{H}\to\mathbb{R},\quad E_{\epsilon}(\mathbf{u})=E_{0}(\mathbf{u})+\frac{\epsilon}{2}\|\mathbf{u}-\mathbf{v}_{0}\|_{\mathbb{H}}^{2} |  |

is a Morse functional for every positive ϵ \epsilon. As a matter of fact, we have plenty of freedom to choose 𝐯 0 \mathbf{v}_{0}. The success of this process requires the base functional E 0 E_{0} to comply with the two compactness properties that follow:

1. (1)

E 0 ′: ℍ → ℍ E^{\prime}_{0}:\mathbb{H}\to\mathbb{H} (regarded as defined in ℍ \mathbb{H}) is a (non-linear) compact operator:

 | 𝐮 j ⇀ 𝐮 ​ implies ​ E 0 ′ ​ ( 𝐮 j) → E 0 ′ ​ ( 𝐮). \mathbf{u}_{j}\rightharpoonup\mathbf{u}\hbox{ implies }E^{\prime}_{0}(\mathbf{u}_{j})\to E^{\prime}_{0}(\mathbf{u}). |  |

The sign ⇀ \rightharpoonup indicates weak convergence in ℍ \mathbb{H}, i.e.

 | ⟨ 𝐮 j, 𝐯 ⟩ → ⟨ 𝐮, 𝐯 ⟩ \langle\mathbf{u}_{j},\mathbf{v}\rangle\to\langle\mathbf{u},\mathbf{v}\rangle |  |

for every fixed 𝐯 ∈ ℍ \mathbf{v}\in\mathbb{H}.

2. (2)

For each 𝐮 ∈ ℍ \mathbf{u}\in\mathbb{H}, the self-adjoint, linear operator

 | E 0 ′′ ​ ( 𝐮): ℍ → ℍ E^{\prime\prime}_{0}(\mathbf{u}):\mathbb{H}\to\mathbb{H} |  |

is compact.

More specifically, we want to prove the two following results. Our starting point is the non-negative, 𝒞 2 \mathcal{C}^{2} -functional

 | E 0: ℍ ⊂ 𝕃 → ℝ E_{0}:\mathbb{H}\subset\mathbb{L}\to\mathbb{R} |  |

where the injection ℍ ↪ 𝕃 \mathbb{H}\hookrightarrow\mathbb{L} is compact.

###### Lemma 3.2.

Suppose E 0 ′: ℍ → ℍ E^{\prime}_{0}:\mathbb{H}\to\mathbb{H} is a compact operator, and let 𝕍 ⊂ ℍ \mathbb{V}\subset\mathbb{H} be an open subset. There is 𝐯 0 ∈ 𝕍 \mathbf{v}_{0}\in\mathbb{V} such that the perturbed functional

(3.2) |  | E ϵ ​ ( 𝐮) = E 0 ​ ( 𝐮) + ϵ 2 ​ ‖ 𝐮 − 𝐯 0 ‖ 2 E_{\epsilon}(\mathbf{u})=E_{0}(\mathbf{u})+\frac{\epsilon}{2}\|\mathbf{u}-\mathbf{v}_{0}\|^{2} |  |

is non-negative, coercive, 𝒞 2 \mathcal{C}^{2} -, complies with the Palais-Smale condition, and has a finite number (possibly depending on ϵ \epsilon and α \alpha) of non-degenerate critical points in every finite sub-level set of the form { E ϵ < α } \{E_{\epsilon}<\alpha\} for arbitrary non-critical value α \alpha.

###### Lemma 3.3.

Assume, in addition to the main assumption in Lemma 3.2, that for each 𝐮 ∈ ℍ \mathbf{u}\in\mathbb{H}, the linear, self-adjoint operator

 | E 0 ′′ ​ ( 𝐮): ℍ → ℍ E^{\prime\prime}_{0}(\mathbf{u}):\mathbb{H}\to\mathbb{H} |  |

is compact. Let E ϵ E_{\epsilon} be the perturbation in that lemma. Then for each positive ϵ \epsilon, every critical point of E ϵ E_{\epsilon} is non-degenerate and has a finite Morse index.

We can sum up these two fundamental facts into a single important, general statement.

###### Theorem 3.4.

Let ℍ ↪ 𝕃 \mathbb{H}\hookrightarrow\mathbb{L} be two nested Hilbert spaces with compact injection. Let

 | E 0: ℍ ⊂ 𝕃 → ℝ E_{0}:\mathbb{H}\subset\mathbb{L}\to\mathbb{R} |  |

be a non-negative, 𝒞 2 \mathcal{C}^{2} -functional such that the derivative operators

 | E 0 ′: ℍ → ℍ, E 0 ′′ ​ ( 𝐮): ℍ → ℍ E^{\prime}_{0}:\mathbb{H}\to\mathbb{H},\quad E^{\prime\prime}_{0}(\mathbf{u}):\mathbb{H}\to\mathbb{H} |  |

are compact, the second one for every fixed 𝐮 ∈ ℍ \mathbf{u}\in\mathbb{H}. Then for every open subset 𝕍 ⊂ ℍ \mathbb{V}\subset\mathbb{H}, there is 𝐯 0 ∈ 𝕍 \mathbf{v}_{0}\in\mathbb{V} such that the perturbed functional

(3.3) |  | E ϵ ​ ( 𝐮) = E 0 ​ ( 𝐮) + ϵ 2 ​ ‖ 𝐮 − 𝐯 0 ‖ 2 E_{\epsilon}(\mathbf{u})=E_{0}(\mathbf{u})+\frac{\epsilon}{2}\|\mathbf{u}-\mathbf{v}_{0}\|^{2} |  |

is a Morse functional.

For proving this main result, we need some preliminary abstract definitions and facts, which we state next for the sake of completeness, most of which can be found in the book of Berger [4], among others.

### 3.4. More concepts

Suppose that E: ℍ → ℝ E:\mathbb{H}\to\mathbb{R} is a smooth 𝒞 2 \mathcal{C}^{2} -functional defined in a Hilbert space ℍ \mathbb{H}. We shall use the following concepts in addition to the ones already introduced earlier.

- (i)

An element 𝐮 ∈ ℍ \mathbf{u}\in\mathbb{H} is called a regular point for a non-linear 𝒞 1 \mathcal{C}^{1} -operator 𝔽: ℍ → ℍ \mathbb{F}:\mathbb{H}\to\mathbb{H} if the linear operator

 | 𝔽 ′ ​ ( 𝐮): ℍ → ℍ \mathbb{F}^{\prime}(\mathbf{u}):\mathbb{H}\to\mathbb{H} |  |

is surjective. Otherwise, 𝐮 \mathbf{u} is called a singular point for 𝔽 \mathbb{F}. When 𝔽 \mathbb{F} is the derivative of a 𝒞 2 \mathcal{C}^{2} -functional E: ℍ → ℝ E:\mathbb{H}\to\mathbb{R}, then a critical point 𝐮 \mathbf{u} for E E is degenerate (respectively, non-degenerate) if it is singular (respectively, regular) for 𝔽 = E ′ \mathbb{F}=E^{\prime}. Note that in this case 𝔽 ′ = E ′′ \mathbb{F}^{\prime}=E^{\prime\prime} is a self-adjoint operator, and so it is surjective if and only if it is bijective, see Section 2.7 in [7], for instance. The image 𝔽 ⁡ ( 𝐮) \mathbb{F}(\mathbf{u}) of a singular point 𝐮 \mathbf{u} is called a singular value of 𝔽 \mathbb{F}.

- (ii)

A mapping 𝔽: ℍ → ℍ \mathbb{F}:\mathbb{H}\to\mathbb{H} is a non-linear Fredholm operator if its Fréchet derivative

 | 𝔽 ′ ​ ( 𝐮): ℍ → ℍ \mathbb{F}^{\prime}(\mathbf{u}):\mathbb{H}\to\mathbb{H} |  |

is a linear Fredholm map for each 𝐮 ∈ ℍ \mathbf{u}\in\mathbb{H}. The index of 𝔽 \mathbb{F} is defined to be the difference of the dimensions of the kernel and the cokernel of 𝔽 ′ ​ ( 𝐮) \mathbb{F}^{\prime}(\mathbf{u}). This index is independent of 𝐮 \mathbf{u}.

- (iii)

The functional E E is a Fredholm functional if E ′: ℍ → ℍ E^{\prime}:\mathbb{H}\to\mathbb{H} is a Fredholm mapping, i.e. if

 | E ′′ ​ ( 𝐮): ℍ → ℍ E^{\prime\prime}(\mathbf{u}):\mathbb{H}\to\mathbb{H} |  |

is a linear Fredholm map for each 𝐮 ∈ ℍ \mathbf{u}\in\mathbb{H}.

We state several interesting facts (page 100 in [4]).

###### Proposition 3.5.

The following statements hold.

- a)

Any diffeomorphism between Banach spaces is a Fredholm map of index zero.

- b)

If 𝔽 \mathbb{F} is a Fredholm map, and 𝔾 \mathbb{G} is a compact operator, then the sum 𝔽 + 𝔾 \mathbb{F}+\mathbb{G} is also Fredholm with the same index as 𝔽 \mathbb{F}.

We recall two additional classic results. The first one is the Inverse Function Theorem (page 113, [4]) for Banach spaces.

###### Theorem 3.6.

Let 𝔽 \mathbb{F} be a 𝒞 1 \mathcal{C}^{1} -mapping defined in a neighborhood of some point 𝐮 \mathbf{u} of a Banach space 𝕏 \mathbb{X}, with range in a Banach space 𝕐 \mathbb{Y}. If 𝔽 ′ ​ ( 𝐮) \mathbb{F}^{\prime}(\mathbf{u}) is a linear homeomorphism of 𝕏 \mathbb{X} onto 𝕐 \mathbb{Y}, then 𝔽 \mathbb{F} is a local homeomorphism of a neighborhood 𝐔 ⁡ ( 𝐮) \mathbf{U}(\mathbf{u}) of 𝐮 \mathbf{u} to a neighborhood of 𝔽 ⁡ ( 𝐮) \mathbb{F}(\mathbf{u}).

The second one is a version of Sard’s theorem for infinite-dimensional spaces (page 125 of [4]).

###### Theorem 3.7.

Let 𝔽 \mathbb{F} be a 𝒞 q \mathcal{C}^{q} -Fredholm mapping of a separable Banach space 𝕏 \mathbb{X} into a separable Banach space 𝕐 \mathbb{Y}. If q > max ( index 𝔽, 0) q>\max(\hbox{index }\mathbb{F},0), the set of singular values of 𝔽 \mathbb{F} are no-where dense (its closure has empty interior) in 𝕐 \mathbb{Y}.

The proof of Theorem 3.4, through Lemmas 3.2 and 3.3, will make use of Proposition 3.5, and Theorems 3.6 and 3.7, in addition to standard properties of compact operators.

### 3.5. Main proofs

We are now in a position to prove Lemma 3.2. We begin by checking that the perturbation E ϵ E_{\epsilon}, for fixed ϵ \epsilon, in ( 3.3) complies with the Palais-Smale property, regardless of how the vector 𝐯 0 \mathbf{v}_{0} is selected : if { 𝐮 j } \{\mathbf{u}_{j}\} is a sequence in ℍ \mathbb{H} such that

 | E ϵ ​ ( 𝐮 j) ​ is bounded, E ϵ ′ ​ ( 𝐮 j) → 𝟎, E_{\epsilon}(\mathbf{u}_{j})\hbox{ is bounded},\quad E^{\prime}_{\epsilon}(\mathbf{u}_{j})\to\mathbf{0}, |  |

then some subsequence of { 𝐮 j } \{\mathbf{u}_{j}\} converges in ℍ \mathbb{H}. Note that, since E ϵ E_{\epsilon} is coercive in ℍ \mathbb{H}, we can replace the boundedness of E ϵ E_{\epsilon} along the sequence { 𝐮 j } \{\mathbf{u}_{j}\} by the uniform boundedness of { 𝐮 j } \{\mathbf{u}_{j}\} in ℍ \mathbb{H}.

Note first that each E ϵ E_{\epsilon} is coercive for fixed ϵ \epsilon. On the other hand,

(3.4) |  | E ϵ ′ = E 0 ′ + ϵ ​ 𝟏 − ϵ ​ 𝐯 0, E^{\prime}_{\epsilon}=E_{0}^{\prime}+\epsilon\mathbf{1}-\epsilon\mathbf{v}_{0}, |  |

where 𝟏: ℍ → ℍ \mathbf{1}:\mathbb{H}\to\mathbb{H} is the identity operator.

Suppose { 𝐮 j } \{\mathbf{u}_{j}\} is uniformly bounded. Since E 0 ′ E^{\prime}_{0} is assumed to be compact, there is a subsequence 𝐮 j \mathbf{u}_{j} (not relabelled) such that

 | E 0 ′ ​ ( 𝐮 j) → 𝐮 ¯, 𝐮 ¯ ∈ ℍ. E^{\prime}_{0}(\mathbf{u}_{j})\to\overline{\mathbf{u}},\quad\overline{\mathbf{u}}\in\mathbb{H}. |  |

To check the Palais-Smale conditions, if E ε ′ ​ ( 𝐮 j) → 𝟎 E^{\prime}_{\varepsilon}(\mathbf{u}_{j})\to\mathbf{0}, due to ( 3.4), we have

 | ε ​ 𝐮 j = E ε ′ ​ ( 𝐮 j) − E 0 ′ ​ ( 𝐮 j) + ϵ ​ 𝐯 0 → − 𝐮 ¯ + ϵ ​ 𝐯 0 ​ as ​ j → ∞. \varepsilon\mathbf{u}_{j}=E^{\prime}_{\varepsilon}(\mathbf{u}_{j})-E_{0}^{\prime}(\mathbf{u}_{j})+\epsilon\mathbf{v}_{0}\to-\overline{\mathbf{u}}+\epsilon\mathbf{v}_{0}\hbox{ as }j\to\infty. |  |

Hence { 𝐮 j } \{\mathbf{u}_{j}\} converges strongly in ℍ \mathbb{H}. This is exactly the required property for each E ϵ E_{\epsilon}.

Consider now the functional

 | E ~ ϵ: ℍ → ℝ, E ~ ϵ ​ ( 𝐮) = E 0 ​ ( 𝐮) + ϵ 2 ​ ‖ 𝐮 ‖ 2. \tilde{E}_{\epsilon}:\mathbb{H}\to\mathbb{R},\quad\tilde{E}_{\epsilon}(\mathbf{u})=E_{0}(\mathbf{u})+\frac{\epsilon}{2}\|\mathbf{u}\|^{2}. |  |

Its derivative

 | 𝔽 ϵ ​ ( 𝐮) ≡ E ~ ϵ ′ ​ ( 𝐮) = ϵ ​ 𝐮 + E 0 ′ ​ ( 𝐮) \mathbb{F}_{\epsilon}(\mathbf{u})\equiv\tilde{E}^{\prime}_{\epsilon}(\mathbf{u})=\epsilon\mathbf{u}+E^{\prime}_{0}(\mathbf{u}) |  |

is the sum of a diffeomorphism, ϵ ​ 𝟏 \epsilon\mathbf{1}, and a compact operator, E 0 ′ E^{\prime}_{0}. By Proposition 3.5, this derivative is a Fredholm operator of index zero. By Theorem 3.7, the set of critical values of the derivative 𝔽 ϵ \mathbb{F}_{\epsilon}, that is

 | ℂ ϵ ≡ { 𝔽 ϵ ​ ( 𝐮) ∈ ℍ: 𝔽 ϵ ′ ​ ( 𝐮) = 𝟎 }, \mathbb{C}_{\epsilon}\equiv\{\mathbb{F}_{\epsilon}(\mathbf{u})\in\mathbb{H}:\mathbb{F}^{\prime}_{\epsilon}(\mathbf{u})=\mathbf{0}\}, |  |

is no-where dense. The union

 | ℂ ≡ ∪ ϵ > 0 ℂ ϵ \mathbb{C}\equiv\cup_{\epsilon>0}\mathbb{C}_{\epsilon} |  |

is thus a meager or first-category subset. Notice here that we can, without loss of generality, restrict attention to some appropriate sequence of values for ϵ \epsilon and work henceforth with such a sequence. For the sake of simplicity, we will keep using ϵ \epsilon without indicating explicitly { ϵ j } \{\epsilon_{j}\}, and hope that this will not create confusion. After all, our main perturbation argument is valid if applied to some sequence of functionals { E ϵ } \{E_{\epsilon}\} for some sequence of values for ϵ \epsilon converging to zero.

Since ℍ \mathbb{H} is a complete metric space, the classical Baire category theorem implies that ℂ \mathbb{C} has empty interior, and consequently, we can choose an element

 | 𝐯 0 ∈ 𝕍 ∖ ℂ, \mathbf{v}_{0}\in\mathbb{V}\setminus\mathbb{C}, |  |

with the properties claimed in the statement of the theorem, so that every solution 𝐮 \mathbf{u} of the family of equations

 | 𝔽 ϵ ​ ( 𝐮) + 𝐯 0 = 𝟎 \mathbb{F}_{\epsilon}(\mathbf{u})+\mathbf{v}_{0}=\mathbf{0} |  |

cannot be a singular point for none of the 𝔽 ϵ ′ \mathbb{F}^{\prime}_{\epsilon} s, i.e.

 | 𝔽 ϵ ′ ​ ( 𝐮) = E ~ 0 ′′ ​ ( 𝐮) \mathbb{F}^{\prime}_{\epsilon}(\mathbf{u})=\tilde{E}^{\prime\prime}_{0}(\mathbf{u}) |  |

is bijective, and so 𝐮 \mathbf{u} is non-degenerate. This argument implies indeed that the critical points of E ϵ E_{\epsilon} are non-degenerate, once 𝐯 0 \mathbf{v}_{0} has been chosen in this way and has been added to E ~ ϵ \tilde{E}_{\epsilon}, because

 | E ϵ ′′ ​ ( 𝐮) = E ~ ϵ ′′ ​ ( 𝐮). E^{\prime\prime}_{\epsilon}(\mathbf{u})=\tilde{E}^{\prime\prime}_{\epsilon}(\mathbf{u}). |  |

The Inverse Function Theorem 3.6 implies directly that non-degenerate critical points of a 𝒞 2 \mathcal{C}^{2} -functional E ϵ E_{\epsilon} are isolated.

Finally, we argue why the number of critical points in sets of the form { E ϵ ≤ α } \{E_{\epsilon}\leq\alpha\} is finite. Indeed, if we let α \alpha be a positive real number and assume that there is an infinite number { 𝐮 j } \{\mathbf{u}_{j}\} of critical points with

 | E ϵ ​ ( 𝐮 j) ≤ α, E ϵ ′ ​ ( 𝐮 j) = 𝟎, E_{\epsilon}(\mathbf{u}_{j})\leq\alpha,\quad E^{\prime}_{\epsilon}(\mathbf{u}_{j})=\mathbf{0}, |  |

the Palais-Smale condition for E ϵ E_{\epsilon} would ensure the existence of a suitable subsequence converging to some 𝐮 ¯ \overline{\mathbf{u}} which would be a critical, non-isolated point. This is a contradiction with the previous statement about the fact that the critical points are isolated, and so the number of such critical points has to be finite. This completes the proof of Lemma 3.2

The proof of Lemma 3.3 relies on the standard fact that eigenvalues of a linear, self-adjoint, compact operator in a Banach space, like E 0 ′′ ​ ( 𝐮) E^{\prime\prime}_{0}(\mathbf{u}), always has a sequence of (real) eigenvalues converging to zero (see, for instance, Chapter 6 of [7]). By differentiating in ( 3.4),

 | E ϵ ′′ ​ ( 𝐮) = E 0 ′′ ​ ( 𝐮) + ϵ ​ 𝟏, E^{\prime\prime}_{\epsilon}(\mathbf{u})=E^{\prime\prime}_{0}(\mathbf{u})+\epsilon\mathbf{1}, |  |

and hence eigenvalues of E ϵ ′′ ​ ( 𝐮) E^{\prime\prime}_{\epsilon}(\mathbf{u}) are eigenvalues of E 0 ′′ ​ ( 𝐮) E^{\prime\prime}_{0}(\mathbf{u}) plus ϵ \epsilon. The conclusion is that there cannot be an infinite number of negative eigenvalues.

Theorem 3.4 is then proved.

### 3.6. Perturbation and critical points

Let E 0: ℍ → ℝ E_{0}:\mathbb{H}\to\mathbb{R} be a 𝒞 1 \mathcal{C}^{1} -, convex functional, bounded from below E 0 ≥ M E_{0}\geq M for some M ∈ ℝ M\in\mathbb{R}, and let E: ℍ → ℝ + E:\mathbb{H}\to\mathbb{R}^{+} be a 𝒞 1 \mathcal{C}^{1} -, strictly convex functional. In most situations of interest, one would take

 | E ⁡ ( 𝐮) = 1 2 ​ ‖ 𝐮 ‖ 2 ​ or ​ E ​ ( 𝐮) = 1 2 ​ ‖ 𝐮 − 𝐯 0 ‖ 2 E(\mathbf{u})=\frac{1}{2}\|\mathbf{u}\|^{2}\hbox{ or }E(\mathbf{u})=\frac{1}{2}\|\mathbf{u}-\mathbf{v}_{0}\|^{2} |  |

for a fixed vector 𝐮 0 ∈ ℍ \mathbf{u}_{0}\in\mathbb{H}. We will consider the perturbed functional

 | E ϵ: ℍ → ℝ, E ϵ ​ ( 𝐮) = E 0 ​ ( 𝐮) + ϵ ​ E ​ ( 𝐮), E_{\epsilon}:\mathbb{H}\to\mathbb{R},\quad E_{\epsilon}(\mathbf{u})=E_{0}(\mathbf{u})+\epsilon E(\mathbf{u}), |  |

which turns out to be strictly convex for every positive ϵ \epsilon. As such it admits a unique minimizer 𝐮 ϵ \mathbf{u}_{\epsilon} which is determined as the unique solution of the critical point equation

 | E 0 ′ ​ ( 𝐮 ϵ) + ϵ ​ E ′ ​ ( 𝐮 ϵ) = 𝟎. E^{\prime}_{0}(\mathbf{u}_{\epsilon})+\epsilon E^{\prime}(\mathbf{u}_{\epsilon})=\mathbf{0}. |  |

This is standard.

###### Proposition 3.8.

In the situation just described, E 0 ′ ​ ( 𝐮 ϵ) → 𝟎 E^{\prime}_{0}(\mathbf{u}_{\epsilon})\to\mathbf{0} in ℍ \mathbb{H}.

###### Proof.

Let 𝐮 ∈ ℍ \mathbf{u}\in\mathbb{H} be an arbitrary vector. Because 𝐮 ϵ \mathbf{u}_{\epsilon} is a minimizer for E ϵ E_{\epsilon}, we have that

 | E 0 ​ ( 𝐮 ϵ) ≤ E ϵ ​ ( 𝐮 ϵ) = E 0 ​ ( 𝐮 ϵ) + ϵ ​ E ​ ( 𝐮 ϵ) ≤ E 0 ​ ( 𝐮) + ϵ ​ E ​ ( 𝐮). E_{0}(\mathbf{u}_{\epsilon})\leq E_{\epsilon}(\mathbf{u}_{\epsilon})=E_{0}(\mathbf{u}_{\epsilon})+\epsilon E(\mathbf{u}_{\epsilon})\leq E_{0}(\mathbf{u})+\epsilon E(\mathbf{u}). |  |

If we take limits in ϵ \epsilon, we conclude that

 | lim inf ϵ → 0 E 0 ​ ( 𝐮 ϵ) ≤ lim sup ϵ → 0 E 0 ​ ( 𝐮 ϵ) ≤ E 0 ​ ( 𝐮), \liminf_{\epsilon\to 0}E_{0}(\mathbf{u}_{\epsilon})\leq\limsup_{\epsilon\to 0}E_{0}(\mathbf{u}_{\epsilon})\leq E_{0}(\mathbf{u}), |  |

and the arbitrariness of 𝐮 \mathbf{u} leads to

 | inf ℍ E 0 ≤ lim inf ϵ → 0 E 0 ​ ( 𝐮 ϵ) ≤ lim sup ϵ → 0 E 0 ​ ( 𝐮 ϵ) ≤ inf ℍ E 0. \inf_{\mathbb{H}}E_{0}\leq\liminf_{\epsilon\to 0}E_{0}(\mathbf{u}_{\epsilon})\leq\limsup_{\epsilon\to 0}E_{0}(\mathbf{u}_{\epsilon})\leq\inf_{\mathbb{H}}E_{0}. |  |

Hence { 𝐮 ϵ } \{\mathbf{u}_{\epsilon}\} is minimizing for E 0 E_{0}, and because E o E_{o} is bounded from below, E 0 ′ ​ ( 𝐮 ϵ) → 𝟎 E^{\prime}_{0}(\mathbf{u}_{\epsilon})\to\mathbf{0} (even if ‖ 𝐮 ϵ ‖ → ∞ \|\mathbf{u}_{\epsilon}\|\to\infty). ∎

The convexity of the base functional E 0 E_{0} looks unavoidable in this proof to ensure the uniqueness of minimizers 𝐮 ϵ \mathbf{u}_{\epsilon}, yet a stronger result is possible with no reference to convexity. Recall that statements concerning ϵ → 0 \epsilon\to 0 exactly means that it holds along some sequence of values of ϵ \epsilon. This suffices for our purposes, as has been indicated earlier in this section.

###### Theorem 3.9.

Let E 0: ℍ → ℝ E_{0}:\mathbb{H}\to\mathbb{R} be a 𝒞 1 \mathcal{C}^{1} -functional, and let { 𝐮 ϵ } \{\mathbf{u}_{\epsilon}\} be a branch of critical points for the family of functionals

 | E ϵ ​ ( 𝐮) = E 0 ​ ( 𝐮) + ϵ 2 ​ ‖ 𝐮 − 𝐯 0 ‖ 2 E_{\epsilon}(\mathbf{u})=E_{0}(\mathbf{u})+\frac{\epsilon}{2}\|\mathbf{u}-\mathbf{v}_{0}\|^{2} |  |

for a fixed element 𝐯 0 ∈ ℍ \mathbf{v}_{0}\in\mathbb{H}, i.e.

(3.5) |  | E 0 ′ ​ ( 𝐮 ϵ) + ϵ ⁡ ( 𝐮 ϵ − 𝐯 0) = 𝟎 E_{0}^{\prime}(\mathbf{u}_{\epsilon})+\epsilon(\mathbf{u}_{\epsilon}-\mathbf{v}_{0})=\mathbf{0} |  |

for every positive ϵ \epsilon sufficiently small. Then:

1. (1)

E 0 ′ ​ ( 𝐮 ϵ) → 𝟎 E^{\prime}_{0}(\mathbf{u}_{\epsilon})\to\mathbf{0} in ℍ \mathbb{H} as ϵ → 0 \epsilon\to 0; and

2. (2)

there is no such branch with

(3.6) |  | E 0 ​ ( 𝐮 ϵ) → 0, E ϵ ​ ( 𝐮 ϵ) > a, E_{0}(\mathbf{u}_{\epsilon})\to 0,\quad E_{\epsilon}(\mathbf{u}_{\epsilon})>a, |  |

for a fixed value a > 0 a>0.

###### Proof.

The first observation is that the branch { 𝐮 ϵ } \{\mathbf{u}_{\epsilon}\} is differentiable with respect to ϵ \epsilon as a consequence of the differentiability of E 0 E_{0} and the smooth dependence of solutions of critical equations with respect to parameters. Let δ > 0 \delta>0 be fixed. Then

 | E δ ​ ( 𝐮 δ) − lim ϵ → 0 E ϵ ​ ( 𝐮 ϵ) = ∫ 0 δ d d ​ ϵ ​ [E ϵ ​ ( 𝐮 ϵ)] ​ 𝑑 ϵ. E_{\delta}(\mathbf{u}_{\delta})-\lim_{\epsilon\to 0}E_{\epsilon}(\mathbf{u}_{\epsilon})=\int_{0}^{\delta}\frac{d}{d\epsilon}[E_{\epsilon}(\mathbf{u}_{\epsilon})]\,d\epsilon. |  |

The differentiation (with respect to ϵ \epsilon) under the integral sign together with ( 3.5) leads immediately to

 | E δ ​ ( 𝐮 δ) − lim ϵ → 0 E ϵ ​ ( 𝐮 ϵ) = ∫ 0 δ 1 2 ​ ‖ 𝐮 ϵ − 𝐯 0 ‖ 2 ​ 𝑑 ϵ. E_{\delta}(\mathbf{u}_{\delta})-\lim_{\epsilon\to 0}E_{\epsilon}(\mathbf{u}_{\epsilon})=\int_{0}^{\delta}\frac{1}{2}\|\mathbf{u}_{\epsilon}-\mathbf{v}_{0}\|^{2}\,d\epsilon. |  |

We will express this identity in the form

(3.7) |  | lim ϵ → 0 [E 0 ​ ( 𝐮 ϵ) + ϵ 2 ​ ‖ 𝐮 ϵ − 𝐯 0 ‖ 2] + ∫ 0 δ 1 2 ​ ‖ 𝐮 ϵ − 𝐯 0 ‖ 2 ​ 𝑑 ϵ = E 0 ​ ( 𝐮 δ) + δ 2 ​ ‖ 𝐮 δ − 𝐯 0 ‖ 2. \lim_{\epsilon\to 0}\left[E_{0}(\mathbf{u}_{\epsilon})+\frac{\epsilon}{2}\|\mathbf{u}_{\epsilon}-\mathbf{v}_{0}\|^{2}\right]+\int_{0}^{\delta}\frac{1}{2}\|\mathbf{u}_{\epsilon}-\mathbf{v}_{0}\|^{2}\,d\epsilon=E_{0}(\mathbf{u}_{\delta})+\frac{\delta}{2}\|\mathbf{u}_{\delta}-\mathbf{v}_{0}\|^{2}. |  |

From this basic equality we will conclude the two claimed facts.

Since all terms involved in ( 3.7) are non-negative, we see that

 | lim ϵ → 0 ϵ 2 ​ ‖ 𝐮 ϵ − 𝐯 0 ‖ 2 ≤ E δ ​ ( 𝐮 δ). \lim_{\epsilon\to 0}\frac{\epsilon}{2}\|\mathbf{u}_{\epsilon}-\mathbf{v}_{0}\|^{2}\leq E_{\delta}(\mathbf{u}_{\delta}). |  |

On the other hand, ( 3.5) implies that both vectors E 0 ′ ​ ( 𝐮 ϵ) E^{\prime}_{0}(\mathbf{u}_{\epsilon}) and 𝐮 ϵ − 𝐯 0 \mathbf{u}_{\epsilon}-\mathbf{v}_{0} are co-linear and, in addition,

 | lim ϵ → 0 − 1 2 E 0 ′ ( 𝐮 ϵ) ⋅ ( 𝐮 ϵ − 𝐯 0) = lim ϵ → 0 ϵ 2 ∥ 𝐮 ϵ − 𝐯 0 ∥ 2 ≤ E δ ( 𝐮 δ). \lim_{\epsilon\to 0}-\frac{1}{2}E^{\prime}_{0}(\mathbf{u}_{\epsilon})\cdot(\mathbf{u}_{\epsilon}-\mathbf{v}_{0})=\lim_{\epsilon\to 0}\frac{\epsilon}{2}\|\mathbf{u}_{\epsilon}-\mathbf{v}_{0}\|^{2}\leq E_{\delta}(\mathbf{u}_{\delta}). |  |

Since the upper bound on the right-hand side is independent of ϵ \epsilon, if ‖ 𝐮 ϵ − 𝐯 0 ‖ \|\mathbf{u}_{\epsilon}-\mathbf{v}_{0}\| converges to infinity, then E 0 ′ ​ ( 𝐮 ϵ) E^{\prime}_{0}(\mathbf{u}_{\epsilon}) must converge necessarily to zero. If 𝐮 ϵ − 𝐯 0 \mathbf{u}_{\epsilon}-\mathbf{v}_{0} is uniformly bounded, then ( 3.5) clearly implies that E 0 ′ ​ ( 𝐮 ϵ) E^{\prime}_{0}(\mathbf{u}_{\epsilon}) converges to zero as well. At any rate, E 0 ′ ​ ( 𝐮 ϵ) → 𝟎 E^{\prime}_{0}(\mathbf{u}_{\epsilon})\to\mathbf{0} in ℍ \mathbb{H}.

Concerning our second point, suppose, seeking a contradiction, that we could find a branch of critical paths { 𝐮 ϵ } \{\mathbf{u}_{\epsilon}\}, complying with ( 3.5), for which ( 3.6) holds for some fixed a > 0 a>0. Then

 | 0 < a ≤ lim ϵ → 0 E ϵ ​ ( 𝐮 ϵ) = lim ϵ → 0 [E 0 ​ ( 𝐮 ϵ) + ϵ 2 ​ ‖ 𝐮 ϵ − 𝐯 0 ‖ 2] = lim ϵ → 0 ϵ 2 ​ ‖ 𝐮 ϵ − 𝐯 0 ‖ 2, 0<a\leq\lim_{\epsilon\to 0}E_{\epsilon}(\mathbf{u}_{\epsilon})=\lim_{\epsilon\to 0}\left[E_{0}(\mathbf{u}_{\epsilon})+\frac{\epsilon}{2}\|\mathbf{u}_{\epsilon}-\mathbf{v}_{0}\|^{2}\right]=\lim_{\epsilon\to 0}\frac{\epsilon}{2}\|\mathbf{u}_{\epsilon}-\mathbf{v}_{0}\|^{2}, |  |

and ( 3.7) leads to

 | a + ∫ 0 δ 1 2 ​ ‖ 𝐮 ϵ − 𝐯 0 ‖ 2 ​ 𝑑 ϵ ≤ E 0 ​ ( 𝐮 δ) + δ 2 ​ ‖ 𝐮 δ − 𝐯 0 ‖ 2. a+\int_{0}^{\delta}\frac{1}{2}\|\mathbf{u}_{\epsilon}-\mathbf{v}_{0}\|^{2}\,d\epsilon\leq E_{0}(\mathbf{u}_{\delta})+\frac{\delta}{2}\|\mathbf{u}_{\delta}-\mathbf{v}_{0}\|^{2}. |  |

If ‖ 𝐮 ϵ − 𝐯 0 ‖ 2 \|\mathbf{u}_{\epsilon}-\mathbf{v}_{0}\|^{2} tends to infinity (as ϵ → 0 \epsilon\to 0), then for some selected sequence of values for δ \delta tending to zero, we should have

 | δ 2 ​ ‖ 𝐮 δ − 𝐯 0 ‖ 2 ≤ ∫ 0 δ 1 2 ​ ‖ 𝐮 ϵ − 𝐯 0 ‖ 2 ​ 𝑑 ϵ. \frac{\delta}{2}\|\mathbf{u}_{\delta}-\mathbf{v}_{0}\|^{2}\leq\int_{0}^{\delta}\frac{1}{2}\|\mathbf{u}_{\epsilon}-\mathbf{v}_{0}\|^{2}\,d\epsilon. |  |

Taking this fact into the previous inequality, we realize that

 | a + δ 2 ​ ‖ 𝐮 δ − 𝐯 0 ‖ 2 ≤ E 0 ​ ( 𝐮 δ) + δ 2 ​ ‖ 𝐮 δ − 𝐯 0 ‖ 2, a+\frac{\delta}{2}\|\mathbf{u}_{\delta}-\mathbf{v}_{0}\|^{2}\leq E_{0}(\mathbf{u}_{\delta})+\frac{\delta}{2}\|\mathbf{u}_{\delta}-\mathbf{v}_{0}\|^{2}, |  |

and a ≤ E 0 ​ ( 𝐮 δ) a\leq E_{0}(\mathbf{u}_{\delta}) for some sequence of values δ \delta tending to zero. This is a contradiction with ( 3.6). If, on the other hand, ‖ 𝐮 ϵ − 𝐯 0 ‖ 2 \|\mathbf{u}_{\epsilon}-\mathbf{v}_{0}\|^{2} is uniformly bounded, then as before

 | 0 < a ≤ lim ϵ → 0 E ϵ ​ ( 𝐮 ϵ) = lim ϵ → 0 E 0 ​ ( 𝐮 ϵ) = 0, 0<a\leq\lim_{\epsilon\to 0}E_{\epsilon}(\mathbf{u}_{\epsilon})=\lim_{\epsilon\to 0}E_{0}(\mathbf{u}_{\epsilon})=0, |  |

which is again a contradiction. ∎

## 4. General results

We start specifying the nature of some ingredients of spaces and functionals for Hilbert’s 16th problem. As already indicated in a previous section, our basic Hilbert spaces are

 | 𝕃 = H O 1 ​ ( [0, 1], ℝ 2) \mathbb{L}=H^{1}_{O}([0,1];\mathbb{R}^{2}) |  |

of continuous, periodic paths, 𝐮 ⁡ ( 0) = 𝐮 ⁡ ( 1) \mathbf{u}(0)=\mathbf{u}(1), with a weak first derivative 𝐮 ′ ​ ( t) \mathbf{u}^{\prime}(t) which is square-integrable in the unit interval

 | ∫ 0 1 | 𝐮 ′ ​ ( t) | 2 ​ 𝑑 t < ∞; \int_{0}^{1}|\mathbf{u}^{\prime}(t)|^{2}\,dt<\infty; |  |

and

 | ℍ = H O 2 ​ ( [0, 1], ℝ 2) \mathbb{H}=H^{2}_{O}([0,1];\mathbb{R}^{2}) |  |

of 𝒞 1 \mathcal{C}^{1} -periodic paths with a weak second derivative 𝐮 ′′ ​ ( t) \mathbf{u}^{\prime\prime}(t) which is square-integrable

 | ∫ 0 1 | 𝐮 ′′ ​ ( t) | 2 ​ 𝑑 t < ∞, 𝐮 ⁡ ( 0) = 𝐮 ⁡ ( 1), 𝐮 ′ ​ ( 0) = 𝐮 ′ ​ ( 1). \int_{0}^{1}|\mathbf{u}^{\prime\prime}(t)|^{2}\,dt<\infty,\quad\mathbf{u}(0)=\mathbf{u}(1),\quad\mathbf{u}^{\prime}(0)=\mathbf{u}^{\prime}(1). |  |

There are three main points that require our attention:

1. (1)

Isolate an appropriate subset 𝕆 \mathbb{O} of H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}) in which the image set of paths in ℝ 2 \mathbb{R}^{2} are essentially identified with the paths themselves. Basically, we would like to avoid the possibility that such image sets are run more than once either counter- or clockwise.

2. (2)

Describe the differential systems that critical paths of local, integral functionals of first- and second-order ought to verify.

3. (3)

Establish the connection between critical paths of integral functionals under fixed end-point conditions and periodic conditions.

### 4.1. Some analytical preliminaries

We briefly state here some basic notions about spaces of functions with weak derivatives having suitable integrability properties, as well as recalling again concepts like the coercivity of a functional. It may be convenient to do so for some interested readers not familiar with these concepts. We refer to [7] for a main, accesible source in this regard, and much more related information.

The underlying natural Hilbert space for E ϵ E_{\epsilon} is

 | H 2 ( [0, 1]; ℝ 2) = { ( x, y): [0, 1] → ℝ 2: \displaystyle H^{2}([0,1];\mathbb{R}^{2})=\left\{(x,y):[0,1]\to\mathbb{R}^{2}:\right. |  |

 | ∫ 0 1 [x 2 + y 2 + ( x ′) 2 + ( y ′) 2 + ( x ′′) 2 + ( y ′′) 2] d t < ∞ }. \displaystyle\left.\int_{0}^{1}[x^{2}+y^{2}+(x^{\prime})^{2}+(y^{\prime})^{2}+(x^{\prime\prime})^{2}+(y^{\prime\prime})^{2}]\,dt<\infty\right\}. |  |

This is nothing but the classical Sobolev space of paths with square-integrable weak derivatives up to order two. The inner product in this space is

 | ⟨ ( x 1, y 1), ( x 2, y 2) ⟩ = ∫ 0 1 ( x 1 ​ x 2 + y 1 ​ y 2 + x 1 ′ ​ x 2 ′ + y 1 ′ ​ y 2 ′ + x 1 ′′ ​ x 2 ′′ + y 1 ′′ ​ y 2 ′′) ​ 𝑑 t, \langle(x_{1},y_{1}),(x_{2},y_{2})\rangle=\int_{0}^{1}(x_{1}x_{2}+y_{1}y_{2}+x^{\prime}_{1}x^{\prime}_{2}+y^{\prime}_{1}y^{\prime}_{2}+x^{\prime\prime}_{1}x^{\prime\prime}_{2}+y^{\prime\prime}_{1}y^{\prime\prime}_{2})\,dt, |  |

and the associated norm

 | ‖ ( x, y) ‖ 2 = ∫ 0 1 [x 2 + y 2 + ( x ′) 2 + ( y ′) 2 + ( x ′′) 2 + ( y ′′) 2] ​ 𝑑 t. \|(x,y)\|^{2}=\int_{0}^{1}[x^{2}+y^{2}+(x^{\prime})^{2}+(y^{\prime})^{2}+(x^{\prime\prime})^{2}+(y^{\prime\prime})^{2}]\,dt. |  |

Norms and inner products occurring henceforth are meant to be these. Paths in H 2 ​ ( [0, 1], ℝ 2) H^{2}([0,1];\mathbb{R}^{2}) have continuous first derivatives. Since parameterizations of limit cycles as integral curves of the corresponding polynomial differential system, suitably normalized to the unit interval, are 𝒞 ∞ \mathcal{C}^{\infty}, they belong to this space.

We recall that coercivity for a general functional E E defined in a Hilbert space ℍ \mathbb{H} means that

 | E ⁡ ( 𝐮) → + ∞ as ‖ 𝐮 ‖ → ∞ ​ with ​ 𝐮 ∈ ℍ. E(\mathbf{u})\to+\infty\quad\hbox{ as }\quad\|\mathbf{u}\|\to\infty\hbox{ with }\mathbf{u}\in\mathbb{H}. |  |

If a functional E 0 E_{0} defined in H 2 ​ ( [0, 1], ℝ 2) H^{2}([0,1];\mathbb{R}^{2}) is non-negative, the perturbation

 | E ϵ ​ ( 𝐮) = E 0 ​ ( 𝐮) + ϵ 2 ​ ‖ 𝐮 − 𝐯 0 ‖ 2 E_{\epsilon}(\mathbf{u})=E_{0}(\mathbf{u})+\frac{\epsilon}{2}\|\mathbf{u}-\mathbf{v}_{0}\|^{2} |  |

automatically becomes coercive for every positive ϵ \epsilon, and every fixed element 𝐯 0 \mathbf{v}_{0}.

Hilbert’s 16th problem To summarize in a compact form, and anticipate our analytical framework, we will concentrate on the family of functionals E ϵ: H O 2 ​ ( [0, 1], ℝ 2) → ℝ + E_{\epsilon}:H^{2}_{O}([0,1];\mathbb{R}^{2})\to\mathbb{R}^{+} where H O 2 ( [0, 1]; ℝ 2) = { 𝐮 ∈ H 2 ( [0, 1]; ℝ 2): 𝐮 ( 0) = 𝐮 ( 1), 𝐮 ′ ( 0) = 𝐮 ′ ( 1) }, \displaystyle H^{2}_{O}([0,1];\mathbb{R}^{2})=\{\mathbf{u}\in H^{2}([0,1];\mathbb{R}^{2}):\mathbf{u}(0)=\mathbf{u}(1),\mathbf{u}^{\prime}(0)=\mathbf{u}^{\prime}(1)\}, ⟨ 𝐮, 𝐯 ⟩ = ∫ 0 1 ( 𝐮 ⁡ ( t) ⋅ 𝐯 ⁡ ( t) + 𝐮 ′ ​ ( t) ⋅ 𝐯 ′ ​ ( t) + 𝐮 ′′ ​ ( t) ⋅ 𝐯 ′′ ​ ( t)) ​ 𝑑 t, \displaystyle\langle\mathbf{u},\mathbf{v}\rangle=\int_{0}^{1}(\mathbf{u}(t)\cdot\mathbf{v}(t)+\mathbf{u}^{\prime}(t)\cdot\mathbf{v}^{\prime}(t)+\mathbf{u}^{\prime\prime}(t)\cdot\mathbf{v}^{\prime\prime}(t))\,dt, ‖ 𝐮 ‖ 2 = ‖ 𝐮 ‖ H 2 ​ ( [0, 1], ℝ 2) 2 = ∫ 0 1 ( | 𝐮 ′′ ​ ( t) | 2 + | 𝐮 ′ ​ ( t) | 2 + | 𝐮 ⁡ ( t) | 2) ​ 𝑑 t, \displaystyle\|\mathbf{u}\|^{2}=\|\mathbf{u}\|^{2}_{H^{2}([0,1];\mathbb{R}^{2})}=\int_{0}^{1}\big(|\mathbf{u}^{\prime\prime}(t)|^{2}+|\mathbf{u}^{\prime}(t)|^{2}+|\mathbf{u}(t)|^{2}\big)\,dt, E 0 ​ ( 𝐮) = 1 2 ​ ∫ 0 1 ( 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐮 ′) 2 ​ 𝑑 t, \displaystyle E_{0}(\mathbf{u})=\frac{1}{2}\int_{0}^{1}(\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{u}^{\prime})^{2}\,dt, E ϵ ​ ( 𝐮) = E 0 ​ ( 𝐮) + ϵ 2 ​ ‖ 𝐮 ‖ 2 − ⟨ 𝐮, 𝐯 0 ⟩ + ϵ 2 ​ ‖ 𝐯 0 ‖ 2 = E 0 ​ ( 𝐮) + ϵ 2 ​ ‖ 𝐮 − 𝐯 0 ‖ 2, \displaystyle E_{\epsilon}(\mathbf{u})=E_{0}(\mathbf{u})+\frac{\epsilon}{2}\|\mathbf{u}\|^{2}-\langle\mathbf{u},\mathbf{v}_{0}\rangle+\frac{\epsilon}{2}\|\mathbf{v}_{0}\|^{2}=E_{0}(\mathbf{u})+\frac{\epsilon}{2}\|\mathbf{u}-\mathbf{v}_{0}\|^{2}, and 𝐮 = ( x, y), 𝐅 ( 𝐮) = ( P ( x, y), Q ( x, y)), 𝐅 ⟂ ​ ( 𝐮) = ( − Q ⁡ ( 𝐮), P ⁡ ( 𝐮)). \begin{array}[]{c}\mathbf{u}=(x,y),\quad\mathbf{F}(\mathbf{u})=(P(x,y),Q(x,y)),\\ \mathbf{F}^{\perp}(\mathbf{u})=(-Q(\mathbf{u}),P(\mathbf{u})).\end{array}

Once again, a fundamental fact for us to bear in mind is that paths in H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}) are 𝒞 1 \mathcal{C}^{1}, and convergence in H 2 ​ ( [0, 1], ℝ 2) H^{2}([0,1];\mathbb{R}^{2}) implies uniform convergence of first derivatives ( [7]). The following is a more precise statement of Proposition 2.7, that we will use for future reference.

###### Proposition 4.1.

Paths in H 2 ​ ( [0, 1], ℝ 2) H^{2}([0,1];\mathbb{R}^{2}) are 𝒞 1 \mathcal{C}^{1}. If 𝐮 j → 𝐮 \mathbf{u}_{j}\to\mathbf{u} in H 2 ​ ( [0, 1], ℝ 2) H^{2}([0,1];\mathbb{R}^{2}), then

 | 𝐮 j → 𝐮, 𝐮 j ′ → 𝐮 ′ \mathbf{u}_{j}\to\mathbf{u},\quad\mathbf{u}^{\prime}_{j}\to\mathbf{u}^{\prime} |  |

uniformly in [0, 1] [0,1].

### 4.2. Ambient set for our analysis

One fundamental ingredient of our analysis focuses on isolating a suitable increasing family of subsets

 | 𝕆 d ⊂ H O 2 ​ ( [0, 1], ℝ 2), d ∈ ℕ, \mathbb{O}_{d}\subset H^{2}_{O}([0,1];\mathbb{R}^{2}),\quad d\in\mathbb{N}, |  |

where images of paths cannot admit different reparameterizations covering such images more than once either counter- or clockwise. To make this idea rigorous, we will rely on important concepts and results in [51]. Though some of those are rather classical, for the sake of readers we state them here with some care.

###### Definition 4.1.

A planar, parametrized regular closed curve is a continuously differentiable mapping

 | 𝐮 ⁡ ( t): [0, 1] → ℝ 2 \mathbf{u}(t):[0,1]\to\mathbb{R}^{2} |  |

such that

 | 𝐮 ⁡ ( 0) = 𝐮 ⁡ ( 1), 𝐮 ′ ​ ( 0) = 𝐮 ′ ​ ( 1), | 𝐮 ′ ​ ( t) | > 0 ​ for all ​ t ∈ [0, 1]. \mathbf{u}(0)=\mathbf{u}(1),\mathbf{u}^{\prime}(0)=\mathbf{u}^{\prime}(1),\quad|\mathbf{u}^{\prime}(t)|>0\hbox{ for all }t\in[0,1]. |  |

Note how every parametrized regular curve belongs to H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}) according to Proposition 4.1.

For such a regular curve 𝐮 \mathbf{u}, we can consider the normalized tangent vector

 | 𝐧 ⁡ ( t) = 1 | 𝐮 ′ ​ ( t) | ​ 𝐮 ′ ​ ( t): [0, 1] → 𝕊. \mathbf{n}(t)=\frac{1}{|\mathbf{u}^{\prime}(t)|}\mathbf{u}^{\prime}(t):[0,1]\to\mathbb{S}. |  |

###### Definition 4.2.

1. (1)

The winding number of a regular curve 𝐮 \mathbf{u} is the total number of full turns, taking into account its sense, of the normalized tangent vector 𝐧 \mathbf{n} in the unit circle 𝕊 \mathbb{S} as t t runs in the unit interval.

2. (2)

The absolute winding number is the number of full turns, regardless of whether they are clock- or counterclockwise, that 𝐧 \mathbf{n} runs around 𝕊 \mathbb{S} as t t runs through [0, 1] [0,1].

In this way, a regular curve 𝐮 \mathbf{u} could have winding number + 1 +1, and yet its absolute winding number could be larger or even much larger. The point is that the tangent vector 𝐧 ⁡ ( t) \mathbf{n}(t) turns fully around as many times clockwise as counter-clockwise plus one.

The main result from [51] shows that two regular curves can be continuously deformed into each other if and only if they share the winding number.

###### Definition 4.3.

We put 𝕆 d \mathbb{O}_{d} for the subset of H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}) of regular curves with a nowhere-null tangent vector, winding number + 1 +1, and absolute winding number not greater than d d.

###### Proposition 4.2.

𝕆 d \mathbb{O}_{d} is an open subset of H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}).

###### Proof.

Note that convergence in H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}) implies uniform convergence of tangent vectors (Proposition 4.1). This is standard. ∎

The following fact may help in better understanding the absolute winding number of paths.

###### Proposition 4.3.

Suppose 𝐮 j ∈ ∂ 𝕆 d j \mathbf{u}_{j}\in\partial\mathbb{O}_{d_{j}} with d j → ∞ d_{j}\to\infty as j → ∞ j\to\infty, and that

 | 𝐮 j + δ ​ 𝐔 j ∈ ⋃ r > d j 𝕆 r \mathbf{u}_{j}+\delta\mathbf{U}_{j}\in\bigcup_{r>d_{j}}\mathbb{O}_{r} |  |

for all δ > 0 \delta>0 and j j large. Then { 𝐔 j } \{\mathbf{U}_{j}\} cannot converge strongly in H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}).

###### Proof.

Our main hypothesis means that 𝐔 j \mathbf{U}_{j}:

1. (1)

is capable of pushing 𝐮 j \mathbf{u}_{j} to run beyond full rounds in smaller and smaller subintervals of [0, 1] [0,1] (because d j → ∞ d_{j}\to\infty); and

2. (2)

𝐔 j \mathbf{U}_{j} must take on larger and larger values because the multiple δ \delta can be arbitrarily small.

The combined effect implies that { 𝐔 j } \{\mathbf{U}_{j}\} should develop concentration effects, and hence it cannot converge strongly in H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}). ∎

### 4.3. Critical paths of functionals

The object of this subsection is to derive and study the differential equations which must satisfy critical closed paths of local, integral functionals (like E ϵ E_{\epsilon}) in H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}). The proof uses standard ideas in the Calculus of Variations, but we include them because their understanding is crucial for our counting procedure. We first discuss first-order problems as a preliminary step to gain some familiarity with the underlying techniques, and then focus on second-order problems.

#### 4.3.1. First-order problems

Let

 | F ⁡ ( t, 𝐮, 𝐳): [0, 1] × ℝ 2 × ℝ 2 → ℝ F(t,\mathbf{u},\mathbf{z}):[0,1]\times\mathbb{R}^{2}\times\mathbb{R}^{2}\to\mathbb{R} |  |

be a ( 𝒞 ∞ CLOSE (\mathcal{C}^{\infty} -) function with respect to ( t, 𝐮, 𝐳) (t,\mathbf{u},\mathbf{z}), with partial derivatives F 𝐮 F_{\mathbf{u}}, F 𝐳 F_{\mathbf{z}}. The associated functional is

 | E ⁡ ( 𝐮) = ∫ 0 1 F ⁡ ( t, 𝐮 ⁡ ( t), 𝐮 ′ ​ ( t)) ​ 𝑑 t. E(\mathbf{u})=\int_{0}^{1}F(t,\mathbf{u}(t),\mathbf{u}^{\prime}(t))\,dt. |  |

It is important for us to understand the role played by end-point conditions when looking for critical paths of E E. Specifically, we will proceed in three successive steps:

1. (1)

the most general and standard situation is to look for critical paths under fixed end-point conditions, so that feasible paths 𝐮 ⁡ ( t) \mathbf{u}(t) are such that

 | 𝐮 ( t) ∈ H 𝐮 0, 𝐮 1 1 ( [0, 1]; ℝ 2) = { 𝐯 ∈ H 1 ( [0, 1]; ℝ 2): 𝐯 ( 0) = 𝐮 0, 𝐯 ( 1) = 𝐮 1 }, \mathbf{u}(t)\in H^{1}_{\mathbf{u}_{0},\mathbf{u}_{1}}([0,1];\mathbb{R}^{2})=\{\mathbf{v}\in H^{1}([0,1];\mathbb{R}^{2}):\mathbf{v}(0)=\mathbf{u}_{0},\mathbf{v}(1)=\mathbf{u}_{1}\}, |  |

for 𝐮 0, 𝐮 1 ∈ ℝ 2 \mathbf{u}_{0},\mathbf{u}_{1}\in\mathbb{R}^{2} arbitrary but fixed vectors;

2. (2)

in the second step we just take 𝐮 0 = 𝐮 1 \mathbf{u}_{0}=\mathbf{u}_{1}, a fixed vector, and admissible paths are

 | 𝐮 ⁡ ( t) ∈ H 𝐮 0 1 ​ ( [0, 1], ℝ 2) = { 𝐯 ∈ H 1 ​ ( [0, 1], ℝ 2): 𝐯 ⁡ ( 0) = 𝐯 ⁡ ( 1) = 𝐮 0 }; \mathbf{u}(t)\in H^{1}_{\mathbf{u}_{0}}([0,1];\mathbb{R}^{2})=\{\mathbf{v}\in H^{1}([0,1];\mathbb{R}^{2}):\mathbf{v}(0)=\mathbf{v}(1)=\mathbf{u}_{0}\}; |  |

3. (3)

in the final step we demand 𝐮 ⁡ ( 0) = 𝐮 ⁡ ( 1) \mathbf{u}(0)=\mathbf{u}(1) but this vector is free, and feasible paths are

 | 𝐮 ⁡ ( t) ∈ H O 1 ​ ( [0, 1], ℝ 2). \mathbf{u}(t)\in H^{1}_{O}([0,1];\mathbb{R}^{2}). |  |

Assume that

 | F 𝐮 ​ ( t, 𝐯, 𝐯 ′) F_{\mathbf{u}}(t,\mathbf{v},\mathbf{v}^{\prime}) |  |

belongs to L 1 ​ ( ( 0, 1), ℝ 2) L^{1}((0,1);\mathbb{R}^{2}) for every feasible 𝐯 \mathbf{v}, according to the situation considered.

###### Theorem 4.4.

Suppose that the functional

 | E ⁡ ( 𝐮) = ∫ 0 1 F ⁡ ( t, 𝐮 ⁡ ( t), 𝐮 ′ ​ ( t)) ​ 𝑑 t E(\mathbf{u})=\int_{0}^{1}F(t,\mathbf{u}(t),\mathbf{u}^{\prime}(t))\,dt |  |

admits a critical closed path 𝐮 ⁡ ( t): [0, 1] → ℝ 2 \mathbf{u}(t):[0,1]\to\mathbb{R}^{2} either in:

1. (1)

H 𝐮 0, 𝐮 1 1 ​ ( [0, 1], ℝ 2) H^{1}_{\mathbf{u}_{0},\mathbf{u}_{1}}([0,1];\mathbb{R}^{2}); or

2. (2)

H 𝐮 0 1 ​ ( [0, 1], ℝ 2) H^{1}_{\mathbf{u}_{0}}([0,1];\mathbb{R}^{2}); or

3. (3)

H O 1 ​ ( [0, 1], ℝ 2) H^{1}_{O}([0,1];\mathbb{R}^{2}).

Then the function F 𝐳 ​ ( t, 𝐮, 𝐮 ′) F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime}) is absolutely continuous in ( 0, 1) (0,1),

(4.1) |  | − d d ​ t F 𝐳 ( t, 𝐮, 𝐮 ′) + F 𝐮 ( t, 𝐮, 𝐮 ′) = 𝟎 for a.e. t in ( 0, 1), -\frac{d}{dt}F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime})+F_{\mathbf{u}}(t,\mathbf{u},\mathbf{u}^{\prime})=\mathbf{0}\,\,\,\hbox{for a.e. $t$ in }(0,1), |  |

and:

1. (1)

𝐮 ⁡ ( 0) = 𝐮 0 \mathbf{u}(0)=\mathbf{u}_{0}, 𝐮 ⁡ ( 1) = 𝐮 1 \mathbf{u}(1)=\mathbf{u}_{1}; or

2. (2)

𝐮 ⁡ ( 0) = 𝐮 ⁡ ( 1) = 𝐮 0 \mathbf{u}(0)=\mathbf{u}(1)=\mathbf{u}_{0}; or

3. (3)

the function F 𝐳 ​ ( t, 𝐮, 𝐮 ′) F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime}) is absolutely continuous in [0, 1] [0,1], i.e.

(4.2) |  | [F 𝐳 ​ ( t, 𝐮, 𝐮 ′)] t = 0 = 𝟎, [F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime})]_{t=0}=\mathbf{0}, |  |

respectively.

###### Proof.

Take

 | 𝐔 ∈ H 𝟎 1 ​ ( [0, 1], ℝ 2) = { 𝐯 ∈ H 1 ​ ( [0, 1], ℝ 2): 𝐯 ⁡ ( 0) = 𝐯 ⁡ ( 1) = 𝟎 }, \mathbf{U}\in H^{1}_{\mathbf{0}}([0,1];\mathbb{R}^{2})=\{\mathbf{v}\in H^{1}([0,1];\mathbb{R}^{2}):\mathbf{v}(0)=\mathbf{v}(1)=\mathbf{0}\}, |  |

in such a way that the combination 𝐮 + δ ​ 𝐔 \mathbf{u}+\delta\mathbf{U} is feasible for every real δ \delta if 𝐮 \mathbf{u} is (in each of the three situations considered). If 𝐮 \mathbf{u} is a critical closed path of E E, in any of the three cases, then

 | d d ​ δ ​ E ​ ( 𝐮 + δ ​ 𝐔) | δ = 0 = 0, \left.\frac{d}{d\delta}E(\mathbf{u}+\delta\mathbf{U})\right|_{\delta=0}=0, |  |

that is to say

 | d d ​ δ | δ = 0 ​ ∫ 0 1 F ⁡ ( t, 𝐮 ⁡ ( t) + δ ​ 𝐔 ​ ( t), 𝐮 ′ ​ ( t) + δ ​ 𝐔 ′ ​ ( t)) ​ 𝑑 t = 0. \left.\frac{d}{d\delta}\right|_{\delta=0}\int_{0}^{1}F(t,\mathbf{u}(t)+\delta\mathbf{U}(t),\mathbf{u}^{\prime}(t)+\delta\mathbf{U}^{\prime}(t))\,dt=0. |  |

This derivative has the form

(4.3) |  | ∫ 0 1 [F 𝐮 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) ⋅ 𝐔 ⁡ ( t) + F 𝐳 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) ⋅ 𝐔 ′ ​ ( t)] ​ 𝑑 t = 0. \int_{0}^{1}\left[F_{\mathbf{u}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\cdot\mathbf{U}(t)+F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\cdot\mathbf{U}^{\prime}(t)\right]\,dt=0. |  |

We consider the special subspace 𝕌 \mathbb{U} of variations 𝐔 \mathbf{U} defined by

 | 𝕌 = { 𝐔 ∈ H 1 ( [0, 1]; ℝ 2): 𝐔 ( 0) = 𝟎, 𝐔 ′ ∈ { 1 } ⟂ }, \mathbb{U}=\{\mathbf{U}\in H^{1}([0,1];\mathbb{R}^{2}):\mathbf{U}(0)=\mathbf{0},\mathbf{U}^{\prime}\in\{1\}^{\perp}\}, |  |

where { 1 } ⟂ \{1\}^{\perp} is the orthogonal complement, in L 2 ​ ( [0, 1], ℝ 2) L^{2}([0,1];\mathbb{R}^{2}), of the subspace generated by { 1 } \{1\}. Since these orthogonality conditions mean

 | ∫ 0 1 𝐔 ′ ​ ( t) ​ 𝑑 t = 𝐔 ⁡ ( 1) − 𝐔 ⁡ ( 0) = 𝟎, \int_{0}^{1}\mathbf{U}^{\prime}(t)\,dt=\mathbf{U}(1)-\mathbf{U}(0)=\mathbf{0}, |  |

we can also put

 | 𝕌 = { 𝐔 ∈ H 1 ​ ( [0, 1], ℝ 2): 𝐔 ⁡ ( 0) = 𝐔 ⁡ ( 1) = 𝟎 } = H 𝟎 1 ​ ( [0, 1], ℝ 2). \mathbb{U}=\{\mathbf{U}\in H^{1}([0,1];\mathbb{R}^{2}):\mathbf{U}(0)=\mathbf{U}(1)=\mathbf{0}\}=H^{1}_{\mathbf{0}}([0,1];\mathbb{R}^{2}). |  |

We also set

 | Ψ ⁡ ( t) = ∫ 0 t F 𝐮 ​ ( s, 𝐮 ⁡ ( s), 𝐮 ′ ​ ( s)) ​ 𝑑 s, \Psi(t)=\int_{0}^{t}F_{\mathbf{u}}(s,\mathbf{u}(s),\mathbf{u}^{\prime}(s))\,ds, |  |

a continuous, bounded function by hypothesis. For 𝐔 ∈ 𝕌 \mathbf{U}\in\mathbb{U}, an integration by parts in the first term of ( 4.3) yields

(4.4) |  | ∫ 0 1 [− Ψ ( t) ⋅ 𝐔 ′ ( t) + F 𝐳 ( t, 𝐮, 𝐮 ′) ⋅ 𝐔 ′ ( t)] d t = 0, \int_{0}^{1}\left[-\Psi(t)\cdot\mathbf{U}^{\prime}(t)+F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime})\cdot\mathbf{U}^{\prime}(t)\right]\,dt=0, |  |

because

 | Ψ ⁡ ( t) ​ 𝐔 ​ ( t) | 0 1 = 𝟎 \left.\Psi(t)\mathbf{U}(t)\right|_{0}^{1}=\mathbf{0} |  |

for test fields 𝐔 ∈ 𝕌 \mathbf{U}\in\mathbb{U}. Due to the arbitrariness of 𝐔 ∈ 𝕌 \mathbf{U}\in\mathbb{U}, according to ( 4.4) we conclude that

(4.5) |  | F 𝐳 ​ ( t, 𝐮, 𝐮 ′) − Ψ ⁡ ( t) = c ​ in ​ ( 0, 1), F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime})-\Psi(t)=c\hbox{ in }(0,1), |  |

with c c, a constant. In particular, since Ψ \Psi is absolutely continuous (it belongs to W 1, 1 ​ ( ( 0, 1) CLOSE; W^{1,1}((0,1); OPEN ℝ 2) \mathbb{R}^{2})), we know that F 𝐳 ​ ( t, 𝐮, 𝐮 ′) F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime}) must be absolutely continuous too in ( 0, 1) (0,1), and, as such, it cannot have jumps in ( 0, 1) (0,1), though it could possibly have at the endpoints. By differentiating once in ( 4.5) with respect to t t,

(4.6) |  | − d d ​ t ​ F 𝐳 ​ ( t, 𝐮, 𝐮 ′) + F 𝐮 ​ ( t, 𝐮, 𝐮 ′) = 0 ​ a.e. in ​ ( 0, 1). -\frac{d}{dt}F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime})+F_{\mathbf{u}}(t,\mathbf{u},\mathbf{u}^{\prime})=0\hbox{ a.e. in }(0,1). |  |

This covers end-point conditions for the two first situations.

For the case of periodic end-point conditions, we take the information in ( 4.6) back to ( 4.3) for a general

 | 𝐔 ∈ H O 1 ​ ( [0, 1], ℝ 2), \mathbf{U}\in H^{1}_{O}([0,1];\mathbb{R}^{2}), |  |

not necessarily belonging to 𝕌 \mathbb{U}. One integration by parts in the second term in ( 4.3) yields

 | ∫ 0 1 F 𝐳 ( t, 𝐮, 𝐮 ′) ⋅ 𝐔 ′ ( t) d t = − ∫ 0 1 d d ​ t F 𝐳 ( t, 𝐮, 𝐮 ′) ⋅ 𝐔 ( t) d t \displaystyle\int_{0}^{1}F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime})\cdot\mathbf{U}^{\prime}(t)\,dt=-\int_{0}^{1}\frac{d}{dt}F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime})\cdot\mathbf{U}(t)\,dt |  |

 | + [F 𝐳 ( t, 𝐮, 𝐮 ′)] t = 0 ⋅ 𝐔 ( 0). \displaystyle+[F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime})]_{t=0}\cdot\mathbf{U}(0). |  |

Recall the periodicity conditions for 𝐔 \mathbf{U}. In this way, the left-hand side of ( 4.3) becomes

 | ∫ 0 1 [− d d ​ t ​ F 𝐳 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) + F 𝐮 ​ ( t, 𝐮, 𝐮 ′)] ⋅ 𝐔 ⁡ ( t) ​ 𝑑 t \displaystyle\int_{0}^{1}\left[-\frac{d}{dt}F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})+F_{\mathbf{u}}(t,\mathbf{u},\mathbf{u}^{\prime})\right]\cdot\mathbf{U}(t)\,dt |  |

 | + [F 𝐳 ( t, 𝐮, 𝐮 ′)] t = 0 ⋅ 𝐔 ( 0). \displaystyle+[F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime})]_{t=0}\cdot\mathbf{U}(0). |  |

The integral here vanishes precisely by ( 4.6), and so we are only left with the contributions on the end-points. Hence, we obtain

(4.7) |  | [F 𝐳 ​ ( t, 𝐮, 𝐮 ′)] t = 0 ⋅ 𝐔 ⁡ ( 0) = 0. [F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime})]_{t=0}\cdot\mathbf{U}(0)=0. |  |

Since vector 𝐔 ⁡ ( 0) \mathbf{U}(0) can be chosen arbitrarily, we conclude that

(4.8) |  | [F 𝐳 ​ ( t, 𝐮, 𝐮 ′)] t = 0 = 𝟎. [F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime})]_{t=0}=\mathbf{0}. |  |

This completes the proof of Theorem 4.4. Note that this last condition implies that F 𝐳 ​ ( t, 𝐮, 𝐮 ′) F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime}) is absolutely continuous in the interval [0, 1] [0,1], including the endpoints. ∎

The following simple example is enlightening. Let

 | ϵ > 0, 𝐯 ⁡ ( t): ℝ → ℝ 2, P ⁡ ( 𝐮): ℝ 2 → ℝ, \epsilon>0,\quad\mathbf{v}(t):\mathbb{R}\to\mathbb{R}^{2},\quad P(\mathbf{u}):\mathbb{R}^{2}\to\mathbb{R}, |  |

be a positive number; a smooth, one-periodic path; and a polynomial in two variables, respectively. We would like to apply the previous main result to the integrand

 | F ⁡ ( t, 𝐮, 𝐳) = ϵ 2 ​ | 𝐳 − 𝐯 ⁡ ( t) | 2 + P ⁡ ( 𝐮). F(t,\mathbf{u},\mathbf{z})=\frac{\epsilon}{2}|\mathbf{z}-\mathbf{v}(t)|^{2}+P(\mathbf{u}). |  |

The corresponding functional is

 | E ⁡ ( 𝐮) = ∫ 0 1 [ϵ 2 ​ | 𝐮 ′ ​ ( t) − 𝐯 ⁡ ( t) | 2 + P ⁡ ( 𝐮 ⁡ ( t))] ​ 𝑑 t. E(\mathbf{u})=\int_{0}^{1}\left[\frac{\epsilon}{2}|\mathbf{u}^{\prime}(t)-\mathbf{v}(t)|^{2}+P(\mathbf{u}(t))\right]\,dt. |  |

In particular, we would like to clearly see the interplay between the two kinds of boundary conditions

 | 𝐮 ⁡ ( 0) = 𝐮 ⁡ ( 1) = 𝐩 \mathbf{u}(0)=\mathbf{u}(1)=\mathbf{p} |  |

for fixed vector 𝐩 \mathbf{p}, and

 | 𝐮 ⁡ ( 0) − 𝐮 ⁡ ( 1) = 𝟎. \mathbf{u}(0)-\mathbf{u}(1)=\mathbf{0}. |  |

Note that the differential system in the open interval ( 0, 1) (0,1) is exactly the same in both cases, according to Theorem 4.4. The crucial difference lies on the end-point condition: in the first case, end-point conditions are imposed directly on feasible paths; in the periodic situation, critical paths must be 𝒞 1 \mathcal{C}^{1} in the full interval [0, 1] [0,1]. Notice that this is so because

 | F 𝐳 = ϵ ⁡ ( 𝐳 − 𝐯 ⁡ ( t)) F_{\mathbf{z}}=\epsilon(\mathbf{z}-\mathbf{v}(t)) |  |

and 𝐯 \mathbf{v} is assumed to be smooth so that 𝐯 ⁡ ( 0) = 𝐯 ⁡ ( 1) \mathbf{v}(0)=\mathbf{v}(1).

#### 4.3.2. Second-order problems

The treatment of second-order problems is formally the same. We first concentrate on periodic boundary conditions, and then focus on end-point conditions afterwards, as understanding the interplay between both for second-order problems is relevant for us.

Let

 | F ⁡ ( t, 𝐮, 𝐳, 𝐙): [0, 1] × ℝ 2 × ℝ 2 × ℝ 2 → ℝ F(t,\mathbf{u},\mathbf{z},\mathbf{Z}):[0,1]\times\mathbb{R}^{2}\times\mathbb{R}^{2}\times\mathbb{R}^{2}\to\mathbb{R} |  |

be a ( 𝒞 ∞ CLOSE (\mathcal{C}^{\infty} -) function with respect to ( t, 𝐮, 𝐳, 𝐙) (t,\mathbf{u},\mathbf{z},\mathbf{Z}), with partial derivatives F 𝐮 F_{\mathbf{u}}, F 𝐳 F_{\mathbf{z}}, F 𝐙 F_{\mathbf{Z}}. Assume that

 | F 𝐮 ​ ( t, 𝐯, 𝐯 ′, 𝐯 ′′) F_{\mathbf{u}}(t,\mathbf{v},\mathbf{v}^{\prime},\mathbf{v}^{\prime\prime}) |  |

and

 | F 𝐳 ​ ( t, 𝐯, 𝐯 ′, 𝐯 ′′) − ∫ 0 t F 𝐮 ​ ( t, 𝐯, 𝐯 ′, 𝐯 ′′) ​ 𝑑 s F_{\mathbf{z}}(t,\mathbf{v},\mathbf{v}^{\prime},\mathbf{v}^{\prime\prime})-\int_{0}^{t}F_{\mathbf{u}}(t,\mathbf{v},\mathbf{v}^{\prime},\mathbf{v}^{\prime\prime})\,ds |  |

belong to L 1 ​ ( ( 0, 1), ℝ 2) L^{1}((0,1);\mathbb{R}^{2}) for every feasible

 | 𝐯 ∈ H O 2 ​ ( [0, 1], ℝ 2). \mathbf{v}\in H^{2}_{O}([0,1];\mathbb{R}^{2}). |  |

###### Theorem 4.5.

Suppose that the functional

 | E ⁡ ( 𝐮) = ∫ 0 1 F ⁡ ( t, 𝐮 ⁡ ( t), 𝐮 ′ ​ ( t), 𝐮 ′′ ​ ( t)) ​ 𝑑 t E(\mathbf{u})=\int_{0}^{1}F(t,\mathbf{u}(t),\mathbf{u}^{\prime}(t),\mathbf{u}^{\prime\prime}(t))\,dt |  |

admits a critical closed path

 | 𝐮: [0, 1] → ℝ 2 ​ in ​ H O 2 ​ ( [0, 1], ℝ 2). \mathbf{u}:[0,1]\to\mathbb{R}^{2}\hbox{ in }H^{2}_{O}([0,1];\mathbb{R}^{2}). |  |

Then the function

(4.9) |  | d d ​ t ​ F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) − F 𝐳 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) \frac{d}{dt}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})-F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime}) |  |

is absolutely continuous in [0, 1] [0,1], and

(4.10) |  | d d ​ t ( d d ​ t F 𝐙 ( t, 𝐮, 𝐮 ′, 𝐮 ′′) − F 𝐳 ( t, 𝐮, 𝐮 ′, 𝐮 ′′)) + F 𝐮 ( t, 𝐮, 𝐮 ′, 𝐮 ′′) = 𝟎 for a.e. t in ( 0, 1). \frac{d}{dt}\left(\frac{d}{dt}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})-F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\right)+F_{\mathbf{u}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})=\mathbf{0}\,\,\,\hbox{for a.e. $t$ in }(0,1). |  |

Moreover

(4.11) |  | [F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′)] t = 0 = 𝟎. [F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})]_{t=0}=\mathbf{0}. |  |

Brackets in ( 4.11) indicate the jump of the field inside at the time indicated (difference between t = 1 t=1, and t = 0 t=0), that is

 | [F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′)] t = 0 = \displaystyle[F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})]_{t=0}= | F 𝐙 ​ ( t, 𝐮 ⁡ ( t), 𝐮 ′ ​ ( t), 𝐮 ′′ ​ ( t)) | t = 1 − \displaystyle\left.F_{\mathbf{Z}}(t,\mathbf{u}(t),\mathbf{u}^{\prime}(t),\mathbf{u}^{\prime\prime}(t))\right|_{t=1^{-}} |  |

 |  | − F 𝐙 ​ ( t, 𝐮 ⁡ ( t), 𝐮 ′ ​ ( t), 𝐮 ′′ ​ ( t)) | t = 0 +. \displaystyle-\left.F_{\mathbf{Z}}(t,\mathbf{u}(t),\mathbf{u}^{\prime}(t),\mathbf{u}^{\prime\prime}(t))\right|_{t=0^{+}}. |  |

Notice that the integrability demanded on those combinations of partial derivatives of F F in the statement of Theorem 4.5 is equivalent to having

 | F 𝐮 ​ ( t, 𝐯, 𝐯 ′, 𝐯 ′′) ​ and ​ F 𝐳 ​ ( t, 𝐯, 𝐯 ′, 𝐯 ′′) F_{\mathbf{u}}(t,\mathbf{v},\mathbf{v}^{\prime},\mathbf{v}^{\prime\prime})\hbox{ and }F_{\mathbf{z}}(t,\mathbf{v},\mathbf{v}^{\prime},\mathbf{v}^{\prime\prime}) |  |

integrable for every feasible

 | 𝐯 ∈ H O 2 ​ ( [0, 1], ℝ 2). \mathbf{v}\in H^{2}_{O}([0,1];\mathbb{R}^{2}). |  |

We have however decided to keep the statement as it is for that is exactly the form in which those combinations of partial derivatives will occur in the proof. Our proof mimics that of Theorem 4.4.

###### Proof of Theorem 4.5.

Take

 | 𝐔 ∈ H O 2 ​ ( [0, 1], ℝ 2). \mathbf{U}\in H^{2}_{O}([0,1];\mathbb{R}^{2}). |  |

If 𝐮 \mathbf{u} is a critical closed path of E E, then

 | d d ​ δ ​ E ​ ( 𝐮 + δ ​ 𝐔) | δ = 0 = 0, \left.\frac{d}{d\delta}E(\mathbf{u}+\delta\mathbf{U})\right|_{\delta=0}=0, |  |

that is to say

 | d d ​ δ | δ = 0 ​ ∫ 0 1 F ⁡ ( t, 𝐮 ⁡ ( t) + δ ​ 𝐔 ​ ( t), 𝐮 ′ ​ ( t) + δ ​ 𝐔 ′ ​ ( t), 𝐮 ′′ ​ ( t) + δ ​ 𝐔 ′′ ​ ( t)) ​ 𝑑 t = 0. \left.\frac{d}{d\delta}\right|_{\delta=0}\int_{0}^{1}F(t,\mathbf{u}(t)+\delta\mathbf{U}(t),\mathbf{u}^{\prime}(t)+\delta\mathbf{U}^{\prime}(t),\mathbf{u}^{\prime\prime}(t)+\delta\mathbf{U}^{\prime\prime}(t))\,dt=0. |  |

This derivative has the form

(4.12) |  | ∫ 0 1 [F 𝐮 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) ⋅ 𝐔 ⁡ ( t) + F 𝐳 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) ⋅ 𝐔 ′ ​ ( t) + F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) ⋅ 𝐔 ′′ ​ ( t)] ​ 𝑑 t = 0. \int_{0}^{1}\left[F_{\mathbf{u}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\cdot\mathbf{U}(t)+F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\cdot\mathbf{U}^{\prime}(t)+F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\cdot\mathbf{U}^{\prime\prime}(t)\right]\,dt=0. |  |

We consider the special subspace 𝕌 \mathbb{U} of variations 𝐔 \mathbf{U} defined by

(4.13) |  | 𝕌 = { 𝐔 ∈ H O 2 ( [0, 1]; ℝ 2): 𝐔 ( 0) = 𝐔 ( 1) = 𝟎, 𝐔 ′′ ∈ { 1, t } ⟂ }, \mathbb{U}=\{\mathbf{U}\in H^{2}_{O}([0,1];\mathbb{R}^{2}):\mathbf{U}(0)=\mathbf{U}(1)=\mathbf{0},\mathbf{U}^{\prime\prime}\in\{1,t\}^{\perp}\}, |  |

where { 1, t } ⟂ \{1,t\}^{\perp} is the orthogonal complement, in L 2 ​ ( [0, 1], ℝ 2) L^{2}([0,1];\mathbb{R}^{2}), of the subspace generated by { 1, t } \{1,t\}. Since these orthogonality conditions mean

 | ∫ 0 1 𝐔 ′′ ​ ( t) ​ 𝑑 t = 𝐔 ′ ​ ( 1) − 𝐔 ′ ​ ( 0) = 𝟎, ∫ 0 1 t ​ 𝐔 ′′ ​ ( t) ​ 𝑑 t = 𝐔 ′ ​ ( 1) = 𝟎, \int_{0}^{1}\mathbf{U}^{\prime\prime}(t)\,dt=\mathbf{U}^{\prime}(1)-\mathbf{U}^{\prime}(0)=\mathbf{0},\quad\int_{0}^{1}t\mathbf{U}^{\prime\prime}(t)\,dt=\mathbf{U}^{\prime}(1)=\mathbf{0}, |  |

we can also put

 | 𝕌 = { 𝐔 ∈ H O 2 ​ ( [0, 1], ℝ 2): 𝐔 ⁡ ( 0) = 𝐔 ⁡ ( 1) = 𝐔 ′ ​ ( 0) = 𝐔 ′ ​ ( 1) = 𝟎 }. \mathbb{U}=\{\mathbf{U}\in H^{2}_{O}([0,1];\mathbb{R}^{2}):\mathbf{U}(0)=\mathbf{U}(1)=\mathbf{U}^{\prime}(0)=\mathbf{U}^{\prime}(1)=\mathbf{0}\}. |  |

We also set

 | Ψ ⁡ ( t) = ∫ 0 t F 𝐮 ​ ( s, 𝐮 ⁡ ( s), 𝐮 ′ ​ ( s), 𝐮 ′′ ​ ( s)) ​ 𝑑 s, \displaystyle\Psi(t)=\int_{0}^{t}F_{\mathbf{u}}(s,\mathbf{u}(s),\mathbf{u}^{\prime}(s),\mathbf{u}^{\prime\prime}(s))\,ds, |  |

 | Φ ⁡ ( t) = ∫ 0 t [− Ψ ⁡ ( s) + F 𝐳 ​ ( s, 𝐮 ⁡ ( s), 𝐮 ′ ​ ( s), 𝐮 ′′ ​ ( s))] ​ 𝑑 s, \displaystyle\Phi(t)=\int_{0}^{t}\left[-\Psi(s)+F_{\mathbf{z}}(s,\mathbf{u}(s),\mathbf{u}^{\prime}(s),\mathbf{u}^{\prime\prime}(s))\right]\,ds, |  |

two continuous, bounded functions by hypothesis. For 𝐔 ∈ 𝕌 \mathbf{U}\in\mathbb{U}, an integration by parts in the first term of ( 4.12) yields

 | ∫ 0 1 [− Ψ ( t) ⋅ 𝐔 ′ ( t) + F 𝐳 ( t, 𝐮, 𝐮 ′, 𝐮 ′′) ⋅ 𝐔 ′ ( t) + F 𝐙 ( t, 𝐮, 𝐮 ′, 𝐮 ′′) ⋅ 𝐔 ′′ ( t)] d t = 0, \int_{0}^{1}\left[-\Psi(t)\cdot\mathbf{U}^{\prime}(t)+F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\cdot\mathbf{U}^{\prime}(t)+F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\cdot\mathbf{U}^{\prime\prime}(t)\right]\,dt=0, |  |

because

 | Ψ ⁡ ( t) ​ 𝐔 ​ ( t) | 0 1 = 𝟎 \left.\Psi(t)\mathbf{U}(t)\right|_{0}^{1}=\mathbf{0} |  |

for test fields 𝐔 ∈ 𝕌 \mathbf{U}\in\mathbb{U}. A second integration by parts leads to

 | ∫ 0 1 [− Φ ⁡ ( t) + F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′)] ⋅ 𝐔 ′′ ​ ( t) ​ 𝑑 t = 0, \int_{0}^{1}\left[-\Phi(t)+F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\right]\cdot\mathbf{U}^{\prime\prime}(t)\,dt=0, |  |

again because

 | Φ ⁡ ( t) ​ 𝐔 ′ ​ ( t) | 0 1 = 𝟎 \left.\Phi(t)\mathbf{U}^{\prime}(t)\right|_{0}^{1}=\mathbf{0} |  |

if 𝐔 ∈ 𝕌 \mathbf{U}\in\mathbb{U}. Due to the arbitrariness of 𝐔 ∈ 𝕌 \mathbf{U}\in\mathbb{U}, according to ( 4.13) we conclude that

(4.14) |  | F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) − Φ ⁡ ( t) = c + C ​ t ​ in ​ ( 0, 1), F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})-\Phi(t)=c+Ct\hbox{ in }(0,1), |  |

with c c and C C constants. In particular, since Φ \Phi is absolutely continuous (it belongs to W 1, 1 ​ ( ( 0, 1) CLOSE; W^{1,1}((0,1); OPEN ℝ 2) \mathbb{R}^{2})), we know that F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime}) must be absolutely continuous too in ( 0, 1) (0,1), and as such, it cannot have jumps in ( 0, 1) (0,1), though it could possibly have at the endpoints. By differentiating once in ( 4.14) with respect to t t,

 | d d ​ t ​ F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) − F 𝐳 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) + Ψ ⁡ ( t) = C ​ a.e. in ​ ( 0, 1), \frac{d}{dt}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})-F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})+\Psi(t)=C\hbox{ a.e. in }(0,1), |  |

and even further

(4.15) |  | d d ​ t ​ ( d d ​ t ​ F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) − F 𝐳 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′)) + F 𝐮 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) = 0 ​ a.e. in ​ ( 0, 1). \frac{d}{dt}\left(\frac{d}{dt}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})-F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\right)+F_{\mathbf{u}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})=0\hbox{ a.e. in }(0,1). |  |

We take this information back to ( 4.12) for a general

 | 𝐔 ∈ H O 2 ​ ( [0, 1], ℝ 2), \mathbf{U}\in H^{2}_{O}([0,1];\mathbb{R}^{2}), |  |

not necessarily belonging to 𝕌 \mathbb{U}. One integration by parts in the second term in ( 4.12) yields

 | ∫ 0 1 F 𝐳 ( t, 𝐮, 𝐮 ′, 𝐮 ′′) ⋅ 𝐔 ′ ( t) d t = − ∫ 0 1 d d ​ t F 𝐳 ( t, 𝐮, 𝐮 ′, 𝐮 ′′) ⋅ 𝐔 ( t) d t \displaystyle\int_{0}^{1}F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\cdot\mathbf{U}^{\prime}(t)\,dt=-\int_{0}^{1}\frac{d}{dt}F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\cdot\mathbf{U}(t)\,dt |  |

 | + [F 𝐳 ( t, 𝐮, 𝐮 ′, 𝐮 ′′)] t = 0 ⋅ 𝐔 ( 0). \displaystyle+[F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})]_{t=0}\cdot\mathbf{U}(0). |  |

Recall the periodicity conditions for 𝐔 \mathbf{U}. Two such integrations by parts in the third term of ( 4.12) leads to

 | ∫ 0 1 F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) ⋅ 𝐔 ′′ ​ ( t) ​ 𝑑 t = \displaystyle\int_{0}^{1}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\cdot\mathbf{U}^{\prime\prime}(t)\,dt= | − ∫ 0 1 d d ​ t F 𝐙 ( t, 𝐮, 𝐮 ′, 𝐮 ′′) ⋅ 𝐔 ′ ( t) d t \displaystyle-\int_{0}^{1}\frac{d}{dt}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\cdot\mathbf{U}^{\prime}(t)\,dt |  |

 |  | + [F 𝐙 ( t, 𝐮, 𝐮 ′, 𝐮 ′′)] t = 0 ⋅ 𝐔 ′ ( 0) \displaystyle+[F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})]_{t=0}\cdot\mathbf{U}^{\prime}(0) |  |

 | = \displaystyle= | ∫ 0 1 d 2 d ​ t 2 ​ F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) ⋅ 𝐔 ⁡ ( t) ​ 𝑑 t \displaystyle\int_{0}^{1}\frac{d^{2}}{dt^{2}}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\cdot\mathbf{U}(t)\,dt |  |

 |  | − [d d ​ t F 𝐙 ( t, 𝐮, 𝐮 ′, 𝐮 ′′)] t = 0 ⋅ 𝐔 ( 0) \displaystyle-[\frac{d}{dt}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})]_{t=0}\cdot\mathbf{U}(0) |  |

 |  | + [F 𝐙 ( t, 𝐮, 𝐮 ′, 𝐮 ′′)] t = 0 ⋅ 𝐔 ′ ( 0). \displaystyle+[F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})]_{t=0}\cdot\mathbf{U}^{\prime}(0). |  |

In this way ( 4.12) becomes

 | ∫ 0 1 [d d ​ t ​ ( d d ​ t ​ F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) − F 𝐳 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′)) + F 𝐮 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′)] ⋅ 𝐔 ⁡ ( t) ​ 𝑑 t \displaystyle\int_{0}^{1}\left[\frac{d}{dt}\left(\frac{d}{dt}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})-F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\right)+F_{\mathbf{u}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\right]\cdot\mathbf{U}(t)\,dt |  |

 | − [d d ​ t F 𝐙 ( t, 𝐮, 𝐮 ′, 𝐮 ′′) − F 𝐳 ( t, 𝐮, 𝐮 ′, 𝐮 ′′)] t = 0 ⋅ 𝐔 ( 0) + [F 𝐙 ( t, 𝐮, 𝐮 ′, 𝐮 ′′)] t = 0 ⋅ 𝐔 ′ ( 0). \displaystyle-[\frac{d}{dt}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})-F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})]_{t=0}\cdot\mathbf{U}(0)+[F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})]_{t=0}\cdot\mathbf{U}^{\prime}(0). |  |

The integral here vanishes precisely by ( 4.15), and so we are only left with the contributions on the end-points. Hence, we obtain

(4.16) |  | [d d ​ t ​ F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) − F 𝐳 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′)] t = 0 ⋅ 𝐔 ⁡ ( 0) − [F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′)] t = 0 ⋅ 𝐔 ′ ​ ( 0) = 0. [\frac{d}{dt}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})-F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})]_{t=0}\cdot\mathbf{U}(0)-[F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})]_{t=0}\cdot\mathbf{U}^{\prime}(0)=0. |  |

Since vectors 𝐔 ′ ​ ( 0) \mathbf{U}^{\prime}(0) and 𝐔 ⁡ ( 0) \mathbf{U}(0) can be chosen arbitrarily, and independently of each other, because there is always a path

 | 𝐔 ∈ H O 2 ​ ( [0, 1], ℝ 2) \mathbf{U}\in H^{2}_{O}([0,1];\mathbb{R}^{2}) |  |

starting in a certain arbitrary vector of ℝ 2 \mathbb{R}^{2} and with any preassigned velocity, we conclude that

(4.17) |  | [F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′)] t = 0 = 𝟎, [F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})]_{t=0}=\mathbf{0}, |  |

and

(4.18) |  | [d d ​ t ​ F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) − F 𝐳 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′)] t = 0 = 𝟎. [\frac{d}{dt}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})-F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})]_{t=0}=\mathbf{0}. |  |

This completes the proof of Theorem 4.5. Note that this last condition implies that

 | d d ​ t ​ F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) − F 𝐳 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) \frac{d}{dt}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})-F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime}) |  |

is absolutely continuous in the interval [0, 1] [0,1], including the endpoints. ∎

### 4.4. End-point conditions

Second-order variational problems, like the one considered in Theorem 4.5, are typically studied under fixed, end-point conditions at end-points { 0, 1 } \{0,1\} up to one order less than the highest order explicitly participating in the functional. For second-order problems, end-point conditions would involve the four values

 | 𝐮 ⁡ ( 0), 𝐮 ⁡ ( 1), 𝐮 ′ ​ ( 0), 𝐮 ′ ​ ( 1). \mathbf{u}(0),\mathbf{u}(1),\quad\mathbf{u}^{\prime}(0),\mathbf{u}^{\prime}(1). |  |

Our periodicity conditions would demand

 | 𝐮 ⁡ ( 0) = 𝐮 ⁡ ( 1), 𝐮 ′ ​ ( 0) = 𝐮 ′ ​ ( 1), \mathbf{u}(0)=\mathbf{u}(1),\quad\mathbf{u}^{\prime}(0)=\mathbf{u}^{\prime}(1), |  |

but these two common values are unknown. There might be several vectors 𝐲 \mathbf{y} and 𝐳 \mathbf{z} for which critical paths for the same functional

 | E ⁡ ( 𝐮) = ∫ 0 1 F ⁡ ( t, 𝐮 ⁡ ( t), 𝐮 ′ ​ ( t), 𝐮 ′′ ​ ( t)) ​ 𝑑 t E(\mathbf{u})=\int_{0}^{1}F(t,\mathbf{u}(t),\mathbf{u}^{\prime}(t),\mathbf{u}^{\prime\prime}(t))\,dt |  |

for 𝐮 ∈ H 2 ​ ( [0, 1], ℝ 2) \mathbf{u}\in H^{2}([0,1];\mathbb{R}^{2}) under fixed end-point conditions

(4.19) |  | 𝐮 ⁡ ( 0) = 𝐮 ⁡ ( 1) = 𝐲, 𝐮 ′ ​ ( 0) = 𝐮 ′ ​ ( 1) = 𝐳, \mathbf{u}(0)=\mathbf{u}(1)=\mathbf{y},\quad\mathbf{u}^{\prime}(0)=\mathbf{u}^{\prime}(1)=\mathbf{z}, |  |

would also be critical paths for our system in Theorem 4.5 without imposing such end-point conditions but just periodicity. Those distinguished values for 𝐲 \mathbf{y} and 𝐳 \mathbf{z} would be such that condition ( 4.11) turns out to be correct.

Hilbert’s 16th problem We will be very much interested in being capable of counting how many such pairs ( 𝐲, 𝐳) (\mathbf{y},\mathbf{z}) there might be for our particular second-order perturbation E ϵ E_{\epsilon} of the basic, first-order functional E 0 E_{0}, as given in ( 2.16). Parallel versions of Theorem 4.5 taking into account specific end-point conditions will help us in counting branches of critical paths for our perturbed functional E ϵ E_{\epsilon}. See below.

More explicitly, the following versions of Theorem 4.5 take into account our discussion above concerning the role played by end-point conditions. To this end, we introduce the notation

 | H 𝐲, 𝐳 2 ( [0, 1]; ℝ 2) = { 𝐯 ∈ H 2 ( [0, 1]; ℝ 2): 𝐯 ( 0) = 𝐯 ( 1) = 𝐲, 𝐯 ′ ( 0) = 𝐯 ′ ( 1) = 𝐳 }, \displaystyle H^{2}_{\mathbf{y},\mathbf{z}}([0,1];\mathbb{R}^{2})=\{\mathbf{v}\in H^{2}([0,1];\mathbb{R}^{2}):\mathbf{v}(0)=\mathbf{v}(1)=\mathbf{y},\mathbf{v}^{\prime}(0)=\mathbf{v}^{\prime}(1)=\mathbf{z}\}, |  |

 | H 𝐲, 2 ( [0, 1]; ℝ 2) = { 𝐯 ∈ H 2 ( [0, 1]; ℝ 2): 𝐯 ( 0) = 𝐯 ( 1) = 𝐲, 𝐯 ′ ( 0) = 𝐯 ′ ( 1) }, \displaystyle H^{2}_{\mathbf{y},}([0,1];\mathbb{R}^{2})=\{\mathbf{v}\in H^{2}([0,1];\mathbb{R}^{2}):\mathbf{v}(0)=\mathbf{v}(1)=\mathbf{y},\mathbf{v}^{\prime}(0)=\mathbf{v}^{\prime}(1)\}, |  |

 | H, 𝐳 2 ( [0, 1]; ℝ 2) = { 𝐯 ∈ H 2 ( [0, 1]; ℝ 2): 𝐯 ( 0) = 𝐯 ( 1), 𝐯 ′ ( 0) = 𝐯 ′ ( 1) = 𝐳 }, \displaystyle H^{2}_{,\mathbf{z}}([0,1];\mathbb{R}^{2})=\{\mathbf{v}\in H^{2}([0,1];\mathbb{R}^{2}):\mathbf{v}(0)=\mathbf{v}(1),\mathbf{v}^{\prime}(0)=\mathbf{v}^{\prime}(1)=\mathbf{z}\}, |  |

for fixed vectors 𝐲, 𝐳 ∈ ℝ 2 \mathbf{y},\mathbf{z}\in\mathbb{R}^{2}. Note that

(4.20) |  | H 𝐲, 𝐳 2 ( [0, 1]; ℝ 2) = H 𝐲, 2 ( [0, 1]; ℝ 2) ∩ H, 𝐳 2 ( [0, 1]; ℝ 2), H^{2}_{\mathbf{y},\mathbf{z}}([0,1];\mathbb{R}^{2})=H^{2}_{\mathbf{y},}([0,1];\mathbb{R}^{2})\cap H^{2}_{,\mathbf{z}}([0,1];\mathbb{R}^{2}), |  |

and that this subspace can also be represented as

(4.21) |  | H 𝐲, 𝐲, 𝐳, 𝐳 2 ​ ( [0, 1], ℝ 2) H^{2}_{\mathbf{y},\mathbf{y},\mathbf{z},\mathbf{z}}([0,1];\mathbb{R}^{2}) |  |

if the subspace

 | H 𝐲 0, 𝐲 1, 𝐳 0, 𝐳 1 2 ​ ( [0, 1], ℝ 2) H^{2}_{\mathbf{y}_{0},\mathbf{y}_{1},\mathbf{z}_{0},\mathbf{z}_{1}}([0,1];\mathbb{R}^{2}) |  |

is given through

 | { 𝐯 ∈ H 2 ( [0, 1]; ℝ 2): 𝐯 ( 0) = 𝐲 0, 𝐯 ( 1) = 𝐲 1, 𝐯 ′ ( 0) = 𝐳 0, 𝐯 ′ ( 1) = 𝐳 1 }. \{\mathbf{v}\in H^{2}([0,1];\mathbb{R}^{2}):\mathbf{v}(0)=\mathbf{y}_{0},\mathbf{v}(1)=\mathbf{y}_{1},\mathbf{v}^{\prime}(0)=\mathbf{z}_{0},\mathbf{v}^{\prime}(1)=\mathbf{z}_{1}\}. |  |

###### Theorem 4.6.

Let integrand F F and corresponding functional E E be as in Theorem 4.5. Let 𝐲 ∈ ℝ 2 \mathbf{y}\in\mathbb{R}^{2} be a given vector. Suppose that 𝐮 \mathbf{u} is a critical path of E E over the class of feasible paths H 𝐲, 2 ​ ( [0, 1], ℝ 2) H^{2}_{\mathbf{y},}([0,1];\mathbb{R}^{2}) just introduced. Then the vector field

(4.22) |  | d d ​ t ​ F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) − F 𝐳 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) \frac{d}{dt}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})-F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime}) |  |

is absolutely continuous in ( 0, 1) (0,1),

(4.23) |  | d d ​ t ( d d ​ t F 𝐙 ( t, 𝐮, 𝐮 ′, 𝐮 ′′) − F 𝐳 ( t, 𝐮, 𝐮 ′, 𝐮 ′′)) + F 𝐮 ( t, 𝐮, 𝐮 ′, 𝐮 ′′) = 𝟎 a.e. t in ( 0, 1), \frac{d}{dt}\left(\frac{d}{dt}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})-F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\right)+F_{\mathbf{u}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})=\mathbf{0}\hbox{ a.e. $t$ in }(0,1), |  |

and

(4.24) |  | [F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′)] t = 0 = 𝟎. [F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})]_{t=0}=\mathbf{0}. |  |

Notice that the classes of feasible paths H 𝐲, 2 ​ ( [0, 1], ℝ 2) H^{2}_{\mathbf{y},}([0,1];\mathbb{R}^{2}), in this statement, and H 𝐲, 𝐳 2 ​ ( [0, 1], ℝ 2) H^{2}_{\mathbf{y},\mathbf{z}}([0,1];\mathbb{R}^{2}) are always subsets of H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}) for every 𝐲 \mathbf{y} and 𝐳 \mathbf{z}. In fact, if we add to H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}) a constraint fixing the starting (and final) vector 𝐲 \mathbf{y}, optimality yields a less restrictive set of conditions, which in this situation amounts to just loosing the continuity of the vector field in ( 4.22) across t = 0 t=0. Note the subtle difference between the statements of Theorems 4.5 and Theorem 4.6.

###### Proof of Theorem 4.6.

The proof is exactly the same, word by word, as that of Theorem 4.5. The only difference revolves around the discussion of ( 4.16). Under periodic conditions, without imposing a particular vector as starting vector (as we are doing here), ( 4.16) leads to the two vanishing jump conditions ( 4.17) and ( 4.18). However, if we insist in that the starting vector for paths is a given, specific vector 𝐲 \mathbf{y}, then feasible variations 𝐔 \mathbf{U} in ( 4.16) must comply with 𝐔 ⁡ ( 0) = 𝟎 \mathbf{U}(0)=\mathbf{0}, and so we are left with

 | [F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′)] t = 0 ⋅ 𝐔 ′ ​ ( 0) = 0. [F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})]_{t=0}\cdot\mathbf{U}^{\prime}(0)=0. |  |

The arbitrariness of 𝐔 ′ ​ ( 0) \mathbf{U}^{\prime}(0) (which can be chosen freely) leads to the first jump condition ( 4.17), but we have no longer ( 4.18). This translates into the continuity of the vector field ( 4.22) in the open interval ( 0, 1) (0,1), not including the end-points, precisely because we cannot rely on the corresponding jump condition across end-points. However the differential system ( 4.23) holds in ( 0, 1) (0,1) in both situations. ∎

We can also perform the same analysis in the subspace H, 𝐳 2 ( [0, 1]; ℝ 2) H^{2}_{,\mathbf{z}}([0,1];\mathbb{R}^{2}) in a similar manner.

###### Theorem 4.7.

Let the integrand F F and the corresponding functional E E be as in Theorem 4.5. Let 𝐳 ∈ ℝ 2 \mathbf{z}\in\mathbb{R}^{2} be a given vector. Suppose that 𝐮 \mathbf{u} is a critical path of E E over the class of feasible paths H, 𝐳 2 ( [0, 1]; ℝ 2) H^{2}_{,\mathbf{z}}([0,1];\mathbb{R}^{2}). Then the vector field

(4.25) |  | d d ​ t ​ F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) − F 𝐳 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) \frac{d}{dt}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})-F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime}) |  |

is absolutely continuous in [0, 1] [0,1], and

(4.26) |  | d d ​ t ( d d ​ t F 𝐙 ( t, 𝐮, 𝐮 ′, 𝐮 ′′) − F 𝐳 ( t, 𝐮, 𝐮 ′, 𝐮 ′′)) + F 𝐮 ( t, 𝐮, 𝐮 ′, 𝐮 ′′) = 𝟎 a.e. t in ( 0, 1), \frac{d}{dt}\left(\frac{d}{dt}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})-F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\right)+F_{\mathbf{u}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})=\mathbf{0}\hbox{ a.e. $t$ in }(0,1), |  |

Notice how the proof of this result is similar to the previous one. In fact, because of ( 4.20), Theorem 4.5 gathers the simultaneous effect of both Theorems 4.6 and 4.7. Namely, we have the following fundamental corollary.

###### Corollary 4.8.

Suppose

 | 𝐮: [0, 1] → ℝ 2 ​ in ​ H O 2 ​ ( [0, 1], ℝ 2) \mathbf{u}:[0,1]\to\mathbb{R}^{2}\hbox{ in }H^{2}_{O}([0,1];\mathbb{R}^{2}) |  |

is a critical path in Theorem 4.5. Put

(4.27) |  | 𝐲 = 𝐮 ⁡ ( 0) = 𝐮 ⁡ ( 1) ∈ ℝ 2, 𝐳 = 𝐮 ′ ​ ( 0) = 𝐮 ′ ​ ( 1) ∈ ℝ 2. \mathbf{y}=\mathbf{u}(0)=\mathbf{u}(1)\in\mathbb{R}^{2},\quad\mathbf{z}=\mathbf{u}^{\prime}(0)=\mathbf{u}^{\prime}(1)\in\mathbb{R}^{2}. |  |

Then 𝐮 \mathbf{u} is a critical path in Theorems 4.6 and 4.7, i.e. in the spaces

(4.28) |  | H 𝐲, 2 ( [0, 1]; ℝ 2), H, 𝐳 2 ( [0, 1]; ℝ 2), H^{2}_{\mathbf{y},}([0,1];\mathbb{R}^{2}),\quad H^{2}_{,\mathbf{z}}([0,1];\mathbb{R}^{2}), |  |

for the selection ( 4.27). Conversely, suppose that a certain path 𝐮 \mathbf{u} is simultaneously a critical path in the two spaces ( 4.28) for vectors 𝐲 \mathbf{y} and 𝐳 \mathbf{z} in ( 4.27). Then 𝐮 \mathbf{u} is also critical in Theorem 4.5.

We believe it is instructive to realize the underlying subspaces where variations are taken from in the three theorems mentioned in this corollary. To begin with, space H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}), where functional E E is regarded in Theorem 4.5, is itself a vector space, and hence variations can be taken in itself. However, for feasible paths in Theorems 4.6 and 4.7, spaces of admissible variations are

(4.29) |  | H 𝟎, 2 ( [0, 1]; ℝ 2) = { 𝐯 ∈ H 2 ( [0, 1]; ℝ 2): 𝐯 ( 0) = 𝐯 ( 1) = 𝟎, 𝐯 ′ ( 0) = 𝐯 ′ ( 1) }, \displaystyle H^{2}_{\mathbf{0},}([0,1];\mathbb{R}^{2})=\{\mathbf{v}\in H^{2}([0,1];\mathbb{R}^{2}):\mathbf{v}(0)=\mathbf{v}(1)=\mathbf{0},\mathbf{v}^{\prime}(0)=\mathbf{v}^{\prime}(1)\}, |  |

(4.30) |  | H, 𝟎 2 ( [0, 1]; ℝ 2) = { 𝐯 ∈ H 2 ( [0, 1]; ℝ 2): 𝐯 ( 0) = 𝐯 ( 1), 𝐯 ′ ( 0) = 𝐯 ′ ( 1) = 𝟎 }, \displaystyle H^{2}_{,\mathbf{0}}([0,1];\mathbb{R}^{2})=\{\mathbf{v}\in H^{2}([0,1];\mathbb{R}^{2}):\mathbf{v}(0)=\mathbf{v}(1),\mathbf{v}^{\prime}(0)=\mathbf{v}^{\prime}(1)=\mathbf{0}\}, |  |

Finally, it is possible to review the same analysis in the more restrictive subspace in ( 4.21) for fixed vectors 𝐲 \mathbf{y} and 𝐳 \mathbf{z}, and find the parallel statement that follows, whose proof can be very easily adapted from the previous ones. Note how as we place more demands on feasible paths, optimality turns back less regularity through end-points.

###### Theorem 4.9.

Let the integrand F F and the corresponding functional E E be as in Theorem 4.5. Let 𝐲, 𝐳 ∈ ℝ 2 \mathbf{y},\mathbf{z}\in\mathbb{R}^{2} be given vectors. Suppose that 𝐮 \mathbf{u} is a critical path of E E over the class of feasible paths in ( 4.20) or ( 4.21). Then the vector field

(4.31) |  | d d ​ t ​ F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) − F 𝐳 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) \frac{d}{dt}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})-F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime}) |  |

is absolutely continuous in ( 0, 1) (0,1), and

(4.32) |  | d d ​ t ( d d ​ t F 𝐙 ( t, 𝐮, 𝐮 ′, 𝐮 ′′) − F 𝐳 ( t, 𝐮, 𝐮 ′, 𝐮 ′′)) + F 𝐮 ( t, 𝐮, 𝐮 ′, 𝐮 ′′) = 𝟎 a.e. t in ( 0, 1). \frac{d}{dt}\left(\frac{d}{dt}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})-F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\right)+F_{\mathbf{u}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})=\mathbf{0}\hbox{ a.e. $t$ in }(0,1). |  |

### 4.5. Initial-value, Cauchy problems

Solutions whose existence is guaranteed by Theorems 4.4, in the case of first-order problems, or 4.9, for second-order problems, are not, in general, unique. To enforce such uniqueness, which will be a necessary ingredient of our counting procedure, we need to resort to standard initial-value Cauchy problems, and relate them to end-point conditions. The following propositions are very classical.

###### Proposition 4.10.

Consider the initial-value, Cauchy problem associated with the second-order differential system ( 4.1), under the same hypotheses as in Theorem 4.4,

(4.33) |  | − d d ​ t ​ F 𝐳 ​ ( t, 𝐮, 𝐮 ′) + F 𝐮 ​ ( t, 𝐮, 𝐮 ′) = 𝟎 ​ for ​ t ∈ ( 0, 1), 𝐮 ⁡ ( 0) = 𝐩, 𝐮 ′ ​ ( 0) = 𝐪, -\frac{d}{dt}F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime})+F_{\mathbf{u}}(t,\mathbf{u},\mathbf{u}^{\prime})=\mathbf{0}\hbox{ for }t\in(0,1),\quad\mathbf{u}(0)=\mathbf{p},\mathbf{u}^{\prime}(0)=\mathbf{q}, |  |

for arbitrary 𝐩, 𝐪 ∈ ℝ 2 \mathbf{p},\mathbf{q}\in\mathbb{R}^{2}. There is a unique solution map

 | 𝐮 ⁡ ( t, 𝐩, 𝐪): [0, 1] × ℝ 2 × ℝ 2 → ℝ 2 \mathbf{u}(t;\mathbf{p},\mathbf{q}):[0,1]\times\mathbb{R}^{2}\times\mathbb{R}^{2}\to\mathbb{R}^{2} |  |

which inherits the same smoothness as that of F F in all its variables.

A main point in our analysis will be concerned with counting how many pairs ( 𝐩, 𝐪) ∈ ℝ 2 × ℝ 2 (\mathbf{p},\mathbf{q})\in\mathbb{R}^{2}\times\mathbb{R}^{2} are capable of enforcing

 | 𝐮 ⁡ ( 0, 𝐩, 𝐪) = 𝐮 ⁡ ( 1, 𝐩, 𝐪), \mathbf{u}(0;\mathbf{p},\mathbf{q})=\mathbf{u}(1;\mathbf{p},\mathbf{q}), |  |

so that the corresponding solution 𝐮 ⁡ ( t, 𝐩, 𝐪) \mathbf{u}(t;\mathbf{p},\mathbf{q}) of the initial-value problem is, in fact, a continuous, 1 1 -periodic path.

A similar result holds for second-order, variational problems.

###### Proposition 4.11.

Consider the initial-value, Cauchy problem associated with the fourth-order differential system ( 4.32), under the same hypotheses as in Theorem 4.5,

(4.34) |  | d d ​ t ​ ( d d ​ t ​ F 𝐙 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) − F 𝐳 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′)) + F 𝐮 ​ ( t, 𝐮, 𝐮 ′, 𝐮 ′′) = 𝟎 ​ for ​ t ∈ ( 0, 1), \frac{d}{dt}\left(\frac{d}{dt}F_{\mathbf{Z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})-F_{\mathbf{z}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})\right)+F_{\mathbf{u}}(t,\mathbf{u},\mathbf{u}^{\prime},\mathbf{u}^{\prime\prime})=\mathbf{0}\hbox{ for }t\in(0,1), |  |

under the initial conditions

 | 𝐮 OPEN i) ( 0; 𝐩 0, 𝐩 1, 𝐩 2, 𝐩 3) = 𝐩 i, i = 0, 1, 2, 3. \mathbf{u}^{i)}(0;\mathbf{p}_{0},\mathbf{p}_{1},\mathbf{p}_{2},\mathbf{p}_{3})=\mathbf{p}_{i},\quad i=0,1,2,3. |  |

for arbitrary 𝐩 i ∈ ℝ 2 \mathbf{p}_{i}\in\mathbb{R}^{2}. There is a unique solution map

 | 𝐮 ⁡ ( t, 𝐩 0, 𝐩 1, 𝐩 2, 𝐩 3): [0, 1] × ℝ 2 × ℝ 2 × ℝ 2 × ℝ 2 → ℝ 2 \mathbf{u}(t;\mathbf{p}_{0},\mathbf{p}_{1},\mathbf{p}_{2},\mathbf{p}_{3}):[0,1]\times\mathbb{R}^{2}\times\mathbb{R}^{2}\times\mathbb{R}^{2}\times\mathbb{R}^{2}\to\mathbb{R}^{2} |  |

which inherits the same smoothness as that of F F in of all its variables.

Again, we will be interested in estimating how many four-tuples ( 𝐩 0, 𝐩 1, 𝐩 2, 𝐩 3) (\mathbf{p}_{0},\mathbf{p}_{1},\mathbf{p}_{2},\mathbf{p}_{3}) are capable of producing 1 1 -periodic solutions through the solution mapping of the corresponding initial-value problem, i.e. such that

 | 𝐮 OPEN i) ​ ( 0, 𝐩 0, 𝐩 1, 𝐩 2, 𝐩 3) = 𝐮 OPEN i) ​ ( 1, 𝐩 0, 𝐩 1, 𝐩 2, 𝐩 3) \mathbf{u}^{i)}(0;\mathbf{p}_{0},\mathbf{p}_{1},\mathbf{p}_{2},\mathbf{p}_{3})=\mathbf{u}^{i)}(1;\mathbf{p}_{0},\mathbf{p}_{1},\mathbf{p}_{2},\mathbf{p}_{3}) |  |

for both i = 0, 1 i=0,1.

For future reference, we formally adopt the following notation.

###### Definition 4.4.

The mapping

 | 𝐮 ⁡ ( t, 𝐩, 𝐪): [0, 1] × ℝ 2 × ℝ 2 → ℝ 2 \mathbf{u}(t;\mathbf{p},\mathbf{q}):[0,1]\times\mathbb{R}^{2}\times\mathbb{R}^{2}\to\mathbb{R}^{2} |  |

is the solution mapping for problem ( 4.33). The mapping

 | 𝐮 ⁡ ( t, 𝐩 0, 𝐩 1, 𝐩 2, 𝐩 3): [0, 1] × ℝ 2 × ℝ 2 × ℝ 2 × ℝ 2 → ℝ 2 \mathbf{u}(t;\mathbf{p}_{0},\mathbf{p}_{1},\mathbf{p}_{2},\mathbf{p}_{3}):[0,1]\times\mathbb{R}^{2}\times\mathbb{R}^{2}\times\mathbb{R}^{2}\times\mathbb{R}^{2}\to\mathbb{R}^{2} |  |

will designate the solution mapping for problem ( 4.34).

Hilbert’s 16th problem We will be using this same notation in the particular situation we are most interested in, i.e. for the differential law coming from examining optimality for our family of functionals E ϵ E_{\epsilon} as recalled in Section 4.1. Namely, 𝐮 ϵ ​ ( t, 𝐩 0, 𝐩 1, 𝐩 2, 𝐩 3) \mathbf{u}_{\epsilon}(t;\mathbf{p}_{0},\mathbf{p}_{1},\mathbf{p}_{2},\mathbf{p}_{3}) will designate the unique solution of the fourth-order differential problem in Proposition 4.11 for F ϵ ​ ( t, 𝐮, 𝐳, 𝐙) = 1 2 ​ ( 𝐳 ⋅ 𝐅 ⟂ ​ ( 𝐮)) 2 + ϵ 2 ​ ( | 𝐙 − 𝐯 0 ′′ ​ ( t) | 2 + | 𝐳 − 𝐯 0 ′ ​ ( t) | 2 + | 𝐮 − 𝐯 0 ​ ( t) | 2), F_{\epsilon}(t,\mathbf{u},\mathbf{z},\mathbf{Z})=\frac{1}{2}(\mathbf{z}\cdot\mathbf{F}^{\perp}(\mathbf{u}))^{2}+\frac{\epsilon}{2}\left(|\mathbf{Z}-\mathbf{v}^{\prime\prime}_{0}(t)|^{2}+|\mathbf{z}-\mathbf{v}^{\prime}_{0}(t)|^{2}+|\mathbf{u}-\mathbf{v}_{0}(t)|^{2}\right), where 𝐅 ⟂ ​ ( 𝐮) = ( − Q ⁡ ( 𝐮), P ⁡ ( 𝐮)), 𝐯 0 = ( X, Y). \mathbf{F}^{\perp}(\mathbf{u})=(-Q(\mathbf{u}),P(\mathbf{u})),\quad\mathbf{v}_{0}=(X,Y). 𝐯 0 \mathbf{v}_{0} is a certain fixed path suitably chosen as described in Section 3.

### 4.6. The shooting method

This is a mechanism that aims at solving an end-point-value problem through a typical initial-value, Cauchy one. What is important for us, as stressed in the preceding sections, is the fundamental distinction between an initial-value and an end-point-value problem in terms of uniqueness of solutions: under very reasonable regularity hypotheses for the differential problem, the solution of an initial-value problem is unique; however, this may not be so for an end-point-value version of it. We are very much in need of controlling the possible number of solutions of an end-point-value problem. We plan to do it through the corresponding initial-value version of the differential problem, as we explain below.

Suppose that

(4.35) |  | 𝐅 ⁡ ( t, 𝐱 ⁡ ( t), 𝐱 ′ ​ ( t), …, 𝐱 OPEN N − 1) ​ ( t), 𝐱 OPEN N) ​ ( t)) = 𝟎 t ∈ ( 0, 1), \mathbf{F}(t,\mathbf{x}(t),\mathbf{x}^{\prime}(t),\dots,\mathbf{x}^{N-1)}(t),\mathbf{x}^{N)}(t))=\mathbf{0}\quad t\in(0,1), |  |

is a certain differential system of order N N in m m unknowns

 | 𝐱 ⁡ ( t): [0, 1] → ℝ m, \mathbf{x}(t):[0,1]\to\mathbb{R}^{m}, |  |

for which we have uniqueness of solutions for every Cauchy problem for the initial conditions

(4.36) |  | 𝐱 ( 0) = 𝐱 0, 𝐱 ′ ( 0) = 𝐱 1, …, 𝐱 OPEN N − 1) ( 0) = 𝐱 N − 1, \mathbf{x}(0)=\mathbf{x}_{0},\mathbf{x}^{\prime}(0)=\mathbf{x}_{1},\dots,\mathbf{x}^{N-1)}(0)=\mathbf{x}_{N-1}, |  |

and vectors

 | 𝐱 0, 𝐱 1, …, 𝐱 N − 1 ∈ ℝ m. \mathbf{x}_{0},\mathbf{x}_{1},\dots,\mathbf{x}_{N-1}\in\mathbb{R}^{m}. |  |

###### Definition 4.5.

We denote by

 | 𝐱 ⁡ ( t, 𝐱 0, 𝐱 1, …, 𝐱 N − 1): [0, 1] × ℝ m × N → ℝ m \mathbf{x}(t;\mathbf{x}_{0},\mathbf{x}_{1},\dots,\mathbf{x}_{N-1}):[0,1]\times\mathbb{R}^{m\times N}\to\mathbb{R}^{m} |  |

such unique solution. Under suitable regularity assumptions on the mapping 𝐅 \mathbf{F} determining the differential law ( 4.35), such solution mapping 𝐱 \mathbf{x} inherits the corresponding smoothness through the standard smooth dependence on initial conditions for differential systems.

Whenever N = 2 ​ k N=2k is even, one may be interested in counting the number of periodic solutions where derivatives up to order k − 1 k-1 are glued at 0 0 and 1 1

(4.37) |  | 𝐱 OPEN j) ​ ( 0, 𝐱 0, 𝐱 1, …, 𝐱 N − 1) = 𝐱 OPEN j) ​ ( 1, 𝐱 0, 𝐱 1, …, 𝐱 N − 1) \mathbf{x}^{j)}(0;\mathbf{x}_{0},\mathbf{x}_{1},\dots,\mathbf{x}_{N-1})=\mathbf{x}^{j)}(1;\mathbf{x}_{0},\mathbf{x}_{1},\dots,\mathbf{x}_{N-1}) |  |

for j = 0, 1, …, k − 1 j=0,1,\dots,k-1. These are k k (non-linear) conditions on the N = 2 ​ k N=2k vectors

 | 𝐱 0, 𝐱 1, …, 𝐱 N − 1. \mathbf{x}_{0},\mathbf{x}_{1},\dots,\mathbf{x}_{N-1}. |  |

At this stage, the issue that we would like to emphasize is the analytic dependence on initial data. The following is a classical fact.

###### Proposition 4.12.

Suppose the mapping

 | 𝐅 ⁡ ( t, 𝐱 ⁡ ( t), 𝐱 ′ ​ ( t), …, 𝐱 OPEN N − 1) ​ ( t)): [0, 1] × ℝ N × m → ℝ m, \mathbf{F}(t,\mathbf{x}(t),\mathbf{x}^{\prime}(t),\dots,\mathbf{x}^{N-1)}(t)):[0,1]\times\mathbb{R}^{N\times m}\to\mathbb{R}^{m}, |  |

is analytic in all of its variables, and 1 1 -periodic in t t. Let

(4.38) |  | 𝐗 ⁡ ( t, 𝐱 0, 𝐱 1, …, 𝐱 N − 1): [0, 1] × ℝ N × m → ℝ m \mathbf{X}(t;\mathbf{x}_{0},\mathbf{x}_{1},\dots,\mathbf{x}_{N-1}):[0,1]\times\mathbb{R}^{N\times m}\to\mathbb{R}^{m} |  |

be the solution mapping of the differential system

 | 𝐗 OPEN N) ​ ( t) = 𝐅 ⁡ ( t, 𝐗 ⁡ ( t), 𝐗 ′ ​ ( t), …, 𝐗 N − 1 ​ ( t)), t ∈ [0, 1], \displaystyle\mathbf{X}^{N)}(t)=\mathbf{F}(t,\mathbf{X}(t),\mathbf{X}^{\prime}(t),\dots,\mathbf{X}^{N-1}(t)),\quad t\in[0,1], |  |

 | 𝐗 ⁡ ( t) ≡ 𝐗 ⁡ ( t, 𝐱 0, 𝐱 1, …, 𝐱 N − 1), \displaystyle\mathbf{X}(t)\equiv\mathbf{X}(t;\mathbf{x}_{0},\mathbf{x}_{1},\dots,\mathbf{x}_{N-1}), |  |

 | 𝐗 OPEN j) ( 0; 𝐱 0, 𝐱 1, …, 𝐱 N − 1) = 𝐱 j, j = 0, 1, …, N − 1. \displaystyle\mathbf{X}^{j)}(0;\mathbf{x}_{0},\mathbf{x}_{1},\dots,\mathbf{x}_{N-1})=\mathbf{x}_{j},\quad j=0,1,\dots,N-1. |  |

The mapping in ( 5.27) is analytic as well.

The relevance for us of this regularity can be described as follows. To make things more transparent, take N = 2 N=2, m = 1 m=1, so that we are talking about a second-order, scalar differential equation

 | X ′′ ​ ( t, p, q) = F ⁡ ( X ⁡ ( t, p, q), X ′ ​ ( t, p, q)) ​ in ​ [0, 1], \displaystyle X^{\prime\prime}(t;p,q)=F(X(t;p,q),X^{\prime}(t;p,q))\hbox{ in }[0,1], |  |

 | X ⁡ ( 0, p, q) = p, X ′ ​ ( 0, p, q) = q, \displaystyle X(0;p,q)=p,X^{\prime}(0;p,q)=q, |  |

and

 | F ⁡ ( P, Q): ℝ 2 → ℝ F(P,Q):\mathbb{R}^{2}\to\mathbb{R} |  |

is an analytic function of two variables. As we will see, this reduction does not mean a true simplification of the arguments, as we can apply the following ideas to a full general, vector, differential problem. As a consequence of Proposition 4.12, we can conclude that X ⁡ ( t, p, q) X(t;p,q) is an analytic function of all its variables. Define

 | G ⁡ ( p, q) = X ⁡ ( 1, p, q) − p. G(p,q)=X(1;p,q)-p. |  |

G G is clearly analytic. We are interested in the curve G = 0 G=0 in the p − q p-q -plane. By the classical implicit function theorem, the equation G ⁡ ( p, q) = 0 G(p,q)=0 determines q = q ⁡ ( p) q=q(p) in a unique, well-defined, smooth manner in a vicinity of every such pair ( p, q) (p,q) where G q ​ ( p, q) G_{q}(p,q) does not vanish. The point is that the solutions of the vector equation

 | ( G ⁡ ( p, q), G q ​ ( p, q)) = ( 0, 0) (G(p,q),G_{q}(p,q))=(0,0) |  |

are isolated by analyticity. Hence, even if

 | G q ​ ( p 0, q 0) = 0 G_{q}(p_{0},q_{0})=0 |  |

for a particular pair ( p 0, q 0) (p_{0},q_{0}), it suffices to move around a bit to find that for each p p not far from p 0 p_{0}, there is a unique q q such that

 | X ⁡ ( 1, p, q) = p. X(1;p,q)=p. |  |

In particular, for every pair ( p, q) (p,q) such that X ⁡ ( t, p, q) X(t;p,q) is a smooth, periodic function, there is, at most, a finite number of values of t t in X ⁡ ( t, p, q) X(t;p,q) for which there can possibly be more than one value for q q with

(4.39) |  | X ⁡ ( 1 + t, p, q) = X ⁡ ( t, p, q). X(1+t;p,q)=X(t;p,q). |  |

One can therefore always easily select values of t t for which there is a unique q q with the property in ( 4.39). We write a more general version of this discussion that is exactly tailored for our purposes. The argument behind is exactly the same.

###### Proposition 4.13.

In the situation of Proposition 4.12 for N = 4 N=4 and m = 2 m=2, let

 | 𝐗 ⁡ ( t, 𝐏 0, 𝐏 1, 𝐏 2, 𝐏 3) \mathbf{X}(t;\mathbf{P}_{0},\mathbf{P}_{1},\mathbf{P}_{2},\mathbf{P}_{3}) |  |

stand for the corresponding solution mapping. Suppose that

 | 𝐗 ⁡ ( t, 𝐩 0, 𝐩 1, 𝐩 2, 𝐩 3) \mathbf{X}(t;\mathbf{p}_{0},\mathbf{p}_{1},\mathbf{p}_{2},\mathbf{p}_{3}) |  |

is a certain, smooth, periodic solution. For every t ∈ [0, 1] t\in[0,1], except possibly for a finite number of values, there is a unique analytic mapping

 | ( 𝐏 2 ​ ( 𝐏, 𝐐), 𝐏 3 ​ ( 𝐏, 𝐐)) ∈ ℝ 2 × ℝ 2 (\mathbf{P}_{2}(\mathbf{P},\mathbf{Q}),\mathbf{P}_{3}(\mathbf{P},\mathbf{Q}))\in\mathbb{R}^{2}\times\mathbb{R}^{2} |  |

for each ( 𝐏, 𝐐) (\mathbf{P},\mathbf{Q}) in a neighborhood of

 | ( 𝐏 0, 𝐏 1) = ( 𝐗 ⁡ ( t, 𝐩 0, 𝐩 1, 𝐩 2, 𝐩 3), 𝐗 ′ ​ ( t, 𝐩 0, 𝐩 1, 𝐩 2, 𝐩 3)) (\mathbf{P}_{0},\mathbf{P}_{1})=(\mathbf{X}(t;\mathbf{p}_{0},\mathbf{p}_{1},\mathbf{p}_{2},\mathbf{p}_{3}),\mathbf{X}^{\prime}(t;\mathbf{p}_{0},\mathbf{p}_{1},\mathbf{p}_{2},\mathbf{p}_{3})) |  |

such that

 | 𝐗 ⁡ ( 0, 𝐏, 𝐐, 𝐏 2, 𝐏 3) = 𝐗 ⁡ ( 1, 𝐏, 𝐐, 𝐏 2, 𝐏 3) = 𝐏, \displaystyle\mathbf{X}(0;\mathbf{P},\mathbf{Q},\mathbf{P}_{2},\mathbf{P}_{3})=\mathbf{X}(1;\mathbf{P},\mathbf{Q},\mathbf{P}_{2},\mathbf{P}_{3})=\mathbf{P}, |  |

 | 𝐗 ′ ​ ( 0, 𝐏, 𝐐, 𝐏 2, 𝐏 3) = 𝐗 ′ ​ ( 1, 𝐏, 𝐐, 𝐏 2, 𝐏 3) = 𝐐. \displaystyle\mathbf{X}^{\prime}(0;\mathbf{P},\mathbf{Q},\mathbf{P}_{2},\mathbf{P}_{3})=\mathbf{X}^{\prime}(1;\mathbf{P},\mathbf{Q},\mathbf{P}_{2},\mathbf{P}_{3})=\mathbf{Q}. |  |

Even more explicitly, we have the following which we record for future reference.

###### Corollary 4.14.

Let

 | 𝐮 ¯ ​ ( t, 𝐩 0, 𝐩 1, 𝐩 2, 𝐩 3): [0, 1] × ℝ 2 × ℝ 2 × ℝ 2 × ℝ 2 → ℝ 2 \overline{\mathbf{u}}(t;\mathbf{p}_{0},\mathbf{p}_{1},\mathbf{p}_{2},\mathbf{p}_{3}):[0,1]\times\mathbb{R}^{2}\times\mathbb{R}^{2}\times\mathbb{R}^{2}\times\mathbb{R}^{2}\to\mathbb{R}^{2} |  |

be the mapping in Definition 4.4 and Proposition 4.11 for an integrand

 | F ⁡ ( t, 𝐮, 𝐳, 𝐙): [0, 1] × ℝ 2 × ℝ 2 × ℝ 2 → ℝ F(t,\mathbf{u},\mathbf{z},\mathbf{Z}):[0,1]\times\mathbb{R}^{2}\times\mathbb{R}^{2}\times\mathbb{R}^{2}\to\mathbb{R} |  |

in Theorem 4.5 which is analytic. Except for an isolated set of pairs ( 𝐩 0, 𝐪 0) (\mathbf{p}_{0},\mathbf{q}_{0}), there is a well-defined, analytic mapping

 | 𝐮 ⁡ ( t, 𝐩, 𝐪): [0, 1] × 𝔹 ρ ​ ( 𝐩 0) × 𝔹 ρ ​ ( 𝐪 0) → ℝ 2 \mathbf{u}(t;\mathbf{p},\mathbf{q}):[0,1]\times{\mathbb{B}}_{\rho}(\mathbf{p}_{0})\times{\mathbb{B}}_{\rho}(\mathbf{q}_{0})\to\mathbb{R}^{2} |  |

for respective neighborhoods 𝔹 ρ ​ ( 𝐩 0) {\mathbb{B}}_{\rho}(\mathbf{p}_{0}) and 𝔹 ρ ​ ( 𝐪 0) {\mathbb{B}}_{\rho}(\mathbf{q}_{0}) of 𝐩 0 \mathbf{p}_{0} and 𝐪 0 \mathbf{q}_{0}, furnishing the solution of ( 4.34) with

 | 𝐮 ⁡ ( 0, 𝐩, 𝐪) = 𝐮 ⁡ ( 1, 𝐩, 𝐪) = 𝐩, 𝐮 ′ ​ ( 0, 𝐩, 𝐪) = 𝐮 ′ ​ ( 1, 𝐩, 𝐪) = 𝐪 \mathbf{u}(0;\mathbf{p},\mathbf{q})=\mathbf{u}(1;\mathbf{p},\mathbf{q})=\mathbf{p},\quad\mathbf{u}^{\prime}(0;\mathbf{p},\mathbf{q})=\mathbf{u}^{\prime}(1;\mathbf{p},\mathbf{q})=\mathbf{q} |  |

for

 | ( 𝐩, 𝐪) ∈ 𝔹 ρ ​ ( 𝐩 0) × 𝔹 ρ ​ ( 𝐪 0). (\mathbf{p},\mathbf{q})\in{\mathbb{B}}_{\rho}(\mathbf{p}_{0})\times{\mathbb{B}}_{\rho}(\mathbf{q}_{0}). |  |

For the proof, simply use Proposition 4.13 to set

 | 𝐮 ⁡ ( t, 𝐩, 𝐪) = 𝐮 ¯ ​ ( t, 𝐩, 𝐪, 𝐩 2 ​ ( 𝐩, 𝐪), 𝐩 3 ​ ( 𝐩, 𝐪)), \mathbf{u}(t;\mathbf{p},\mathbf{q})=\overline{\mathbf{u}}(t;\mathbf{p},\mathbf{q},\mathbf{p}_{2}(\mathbf{p},\mathbf{q}),\mathbf{p}_{3}(\mathbf{p},\mathbf{q})), |  |

for ( 𝐩 2 ​ ( 𝐩, 𝐪), 𝐩 3 ​ ( 𝐩, 𝐪)) (\mathbf{p}_{2}(\mathbf{p},\mathbf{q}),\mathbf{p}_{3}(\mathbf{p},\mathbf{q})) the mapping in the statement of that proposition.

Hilbert’s 16th problem We will invoke Corollary 4.14 for the family of integrands written in the last framed statement F ϵ ​ ( t, 𝐮, 𝐳, 𝐙) = 1 2 ​ ( 𝐳 ⋅ 𝐅 ⟂ ​ ( 𝐮)) 2 + ϵ 2 ​ ( | 𝐙 − 𝐯 0 ′′ ​ ( t) | 2 + | 𝐳 − 𝐯 0 ′ ​ ( t) | 2 + | 𝐮 − 𝐯 0 ​ ( t) | 2), F_{\epsilon}(t,\mathbf{u},\mathbf{z},\mathbf{Z})=\frac{1}{2}(\mathbf{z}\cdot\mathbf{F}^{\perp}(\mathbf{u}))^{2}+\frac{\epsilon}{2}\left(|\mathbf{Z}-\mathbf{v}^{\prime\prime}_{0}(t)|^{2}+|\mathbf{z}-\mathbf{v}^{\prime}_{0}(t)|^{2}+|\mathbf{u}-\mathbf{v}_{0}(t)|^{2}\right), where 𝐅 ⟂ ​ ( 𝐮) = ( − Q ⁡ ( 𝐮), P ⁡ ( 𝐮)), 𝐯 0 = ( X, Y). \mathbf{F}^{\perp}(\mathbf{u})=(-Q(\mathbf{u}),P(\mathbf{u})),\quad\mathbf{v}_{0}=(X,Y). For each fixed, positive ϵ \epsilon, F ϵ F_{\epsilon} is analytic in all its variables provided the auxiliary path 𝐯 0 ​ ( t) \mathbf{v}_{0}(t) can be taken to be analytic as well. There is no problem with such a selection as has been described in Section 3.

### 4.7. Multiplicity

Consider the family of functions

(4.40) |  | f j ( r): I → ℝ, f j ( r) = ∫ J ρ j ( t) P ( u ( t, r)) d t, j = 1, 2, …, f_{j}(r):I\to\mathbb{R},\quad f_{j}(r)=\int_{J}\rho_{j}(t)P(u(t,r))\,dt,\quad j=1,2,\dots, |  |

where both I I and J J are closed, finite intervals, 0 ∈ J 0\in J, | J | = 1 |J|=1, u ⁡ ( t, r) u(t,r) is a certain given function, and P ⁡ ( x) P(x) is a polynomial of degree n n of a single variable x x. If the sequence of functions { ρ j } \{\rho_{j}\} is a sequence of mollifiers, or an approximation of the identity, in the sense

(4.41) |  | lim j → ∞ ∫ J ρ j ​ ( t) ​ F ​ ( t) ​ 𝑑 t = F ⁡ ( 0) \lim_{j\to\infty}\int_{J}\rho_{j}(t)F(t)\,dt=F(0) |  |

for every continuous F F, then we have the following interesting result. Recall that the main properties of the sequence { ρ j } \{\rho_{j}\} (in the one-dimensional case) are:

- •

smoothness: ρ j ∈ 𝒞 ∞ ​ ( J) \rho_{j}\in\mathcal{C}^{\infty}(J);

- •

small support:

 | J j ≡ supp ( w j) = [− α j, α j)] ⊂ J, α j ↘ 0; J_{j}\equiv\operatorname{supp}(w_{j})=[-\alpha_{j},\alpha_{j})]\subset J,\alpha_{j}\searrow 0; |  |

- •

non-negativeness and unit total mass:

 | ∫ J ρ j ​ ( t) ​ 𝑑 t = 1, ρ j ≥ 0. \int_{J}\rho_{j}(t)\,dt=1,\quad\rho_{j}\geq 0. |  |

The convergence properties associated with such a family of functions go well beyond ( 4.41). This is very classical material ( [7]).

###### Proposition 4.15.

Assume that the function

 | u ⁡ ( t, r): J × I → ℝ u(t,r):J\times I\to\mathbb{R} |  |

is smooth, and u ⁡ ( 0, r) u(0,r) is linear in r r. Then, for arbitrarily large j j, the family of functions in ( 4.40)

 | f j ( r): I → ℝ, f j ( r) = ∫ J ρ j ( t) P ( u ( t, r)) d t, j = 1, 2, …, f_{j}(r):I\to\mathbb{R},\quad f_{j}(r)=\int_{J}\rho_{j}(t)P(u(t,r))\,dt,\quad j=1,2,\dots, |  |

for a polynomial P ⁡ ( x) P(x) of degree n n, cannot have more than n n roots in I I.

###### Proof.

Suppose for every large j j, there are, at least, n + 1 n+1 roots (counting multiplicity) in I I for f j f_{j}. Then it is elementary to realize that there must be some r j ∈ I r_{j}\in I which is a root of the n n -th derivative

 | 0 = f j OPEN n) ​ ( r j) = ∫ J ρ j ​ ( t) ​ ∂ n ∂ r n | r = r j ​ P ​ ( u ⁡ ( t, r)) ​ 𝑑 t. 0=f_{j}^{n)}(r_{j})=\int_{J}\rho_{j}(t)\left.\frac{\partial^{n}}{\partial r^{n}}\right|_{r=r_{j}}P(u(t,r))\,dt. |  |

Differentiation under the integral sign is legitimate given the smoothness of all elements in a compact set. Let r j → r ∞ ∈ I r_{j}\to r_{\infty}\in I for some subsequence not relabeled. Then

(4.42) |  | 0 = lim j → ∞ ∫ J ρ j ​ ( t) ​ ∂ n ∂ r n | r = r j ​ P ​ ( u ⁡ ( t, r)) ​ 𝑑 t = ∂ n ∂ r n ​ P ​ ( u ⁡ ( 0, r ∞)). 0=\lim_{j\to\infty}\int_{J}\rho_{j}(t)\left.\frac{\partial^{n}}{\partial r^{n}}\right|_{r=r_{j}}P(u(t,r))\,dt=\frac{\partial^{n}}{\partial r^{n}}P(u(0,r_{\infty})). |  |

This is impossible for a non-trivial polynomial of degree n n under the linearity of u ⁡ ( 0, r) u(0,r) on r r.

Note that the convergence expressed in ( 4.42) is a consequence of writing the difference

 | ∫ J ρ j ​ ( t) ​ [∂ n ∂ r n ​ P ​ ( u ⁡ ( t, r j)) − ∂ n ∂ r n ​ P ​ ( u ⁡ ( 0, r ∞))] ​ 𝑑 t \int_{J}\rho_{j}(t)\left[\frac{\partial^{n}}{\partial r^{n}}P(u(t,r_{j}))-\frac{\partial^{n}}{\partial r^{n}}P(u(0,r_{\infty}))\right]\,dt |  |

in the form

 | ∫ J ρ j ​ ( t) ​ [∂ n ∂ r n ​ P ​ ( u ⁡ ( t, r j)) − ∂ n ∂ r n ​ P ​ ( u ⁡ ( t, r ∞))] ​ 𝑑 t + \displaystyle\int_{J}\rho_{j}(t)\left[\frac{\partial^{n}}{\partial r^{n}}P(u(t,r_{j}))-\frac{\partial^{n}}{\partial r^{n}}P(u(t,r_{\infty}))\right]\,dt+ |  |

 | ∫ J ρ j ​ ( t) ​ [∂ n ∂ r n ​ P ​ ( u ⁡ ( t, r ∞)) − ∂ n ∂ r n ​ P ​ ( u ⁡ ( 0, r ∞))] ​ 𝑑 t. \displaystyle\int_{J}\rho_{j}(t)\left[\frac{\partial^{n}}{\partial r^{n}}P(u(t,r_{\infty}))-\frac{\partial^{n}}{\partial r^{n}}P(u(0,r_{\infty}))\right]\,dt. |  |

Take into account the smoothness of u ⁡ ( t, r) u(t,r) and the boundedness of its derivatives up to order n n in J × I J\times I, and the fact that

 | ∫ J ρ j ​ ( t) ​ 𝑑 t = 1, for all ​ j, \int_{J}\rho_{j}(t)\,dt=1,\hbox{ for all }j, |  |

to use the Lebesgue dominated convergence principle for the first integral. This is standard. ∎

Hilbert’s 16th problem The particular form of the composition P ⁡ ( u ⁡ ( t, r)) P(u(t,r)) does not play a role in the previous proof. We have assumed that particular form under the influence of the structure of problems to be treated later in connection with Hilbert’s 16th problem.

The same proof es valid for the family of functions

(4.43) |  | f j ( r): I → ℝ, f j ( r) = ∫ J ρ j ( t) u ( t, r) d t, j = 1, 2, …, f_{j}(r):I\to\mathbb{R},\quad f_{j}(r)=\int_{J}\rho_{j}(t)u(t,r)\,dt,\quad j=1,2,\dots, |  |

where other ingredients are kept exactly the same.

###### Proposition 4.16.

Assume that the function

 | u ⁡ ( t, r): J × I → ℝ u(t,r):J\times I\to\mathbb{R} |  |

is smooth, and u ⁡ ( 0, r) u(0,r) is a non-trivial polynomial of degree n n in the variable r r. Then, for arbitrarily large j j, the family of functions in ( 4.43)

 | f j ( r): I → ℝ, f j ( r) = ∫ J ρ j ( t) u ( t, r) d t, j = 1, 2, …, f_{j}(r):I\to\mathbb{R},\quad f_{j}(r)=\int_{J}\rho_{j}(t)u(t,r)\,dt,\quad j=1,2,\dots, |  |

cannot have more than n n roots in I I.

We can even let the function u ⁡ ( t, 𝐫) u(t,\mathbf{r}) be the result of an asymptotic process depending on several variables ( t, 𝐫) (t,\mathbf{r})

 | f j ( 𝐫): I → ℝ, f j ( 𝐫) = ∫ J ρ j ( t) u j ( t, 𝐫) d t, j = 1, 2, …, f_{j}(\mathbf{r}):I\to\mathbb{R},\quad f_{j}(\mathbf{r})=\int_{J}\rho_{j}(t)u_{j}(t,\mathbf{r})\,dt,\quad j=1,2,\dots, |  |

provided we are allowed to modulate the mollifier ρ j \rho_{j} with respect to u j u_{j}. Recall that

 | J j = [− α j, α j], α j ↘ 0. J_{j}=[-\alpha_{j},\alpha_{j}],\quad\alpha_{j}\searrow 0. |  |

###### Proposition 4.17.

Let { u j ​ ( t, 𝐫) } \{u_{j}(t,\mathbf{r})\} be a sequence of smooth functions of several variables

 | ( t, 𝐫) ∈ J × I ⊂ ℝ × ℝ d. (t,\mathbf{r})\in J\times I\subset\mathbb{R}\times\mathbb{R}^{d}. |  |

1. (1)

For every subsequence k ⁡ ( j) k(j) sufficiently advanced,

 | lim j → ∞ ∫ J k ⁡ ( j) ρ k ⁡ ( j) ​ ( t) ​ u j ​ ( t, 𝐫) ​ 𝑑 t = lim j → ∞ u j ​ ( 0, 𝐫) \lim_{j\to\infty}\int_{J_{k(j)}}\rho_{k(j)}(t)u_{j}(t,\mathbf{r})\,dt=\lim_{j\to\infty}u_{j}(0,\mathbf{r}) |  |

for all 𝐫 \mathbf{r} in a compact set of I I.

2. (2)

For every subsequence k ⁡ ( j) k(j) sufficiently advanced,

 | lim j → ∞ ∫ 0 2 ​ α k ⁡ ( j) ρ k ⁡ ( j) ​ ( t) ​ u j ​ ( t, 𝐫) ​ 𝑑 t = lim j → ∞ u j ​ ( α k ⁡ ( j), 𝐫) \lim_{j\to\infty}\int_{0}^{2\alpha_{k(j)}}\rho_{k(j)}(t)u_{j}(t,\mathbf{r})\,dt=\lim_{j\to\infty}u_{j}(\alpha_{k(j)},\mathbf{r}) |  |

for all 𝐫 \mathbf{r} in a compact set of I I.

###### Proof.

The proof is straightforward after the ideas utilized in the proof of Proposition 4.15. For each j j fixed, we have

 | lim k → ∞ ∫ J ρ k ​ ( t) ​ u j ​ ( t, 𝐫) ​ 𝑑 t = u j ​ ( 0, 𝐫). \lim_{k\to\infty}\int_{J}\rho_{k}(t)u_{j}(t,\mathbf{r})\,dt=u_{j}(0,\mathbf{r}). |  |

For 𝐫 \mathbf{r} belonging to a given compact set, we can select k ⁡ ( j) k(j) sufficiently advanced (depending on j j and such compact set), so that

 | | ∫ J ρ k ⁡ ( j) ​ ( t) ​ u j ​ ( t, 𝐫) ​ 𝑑 t − u j ​ ( 0, 𝐫) | ≤ 1 j. \left|\int_{J}\rho_{k(j)}(t)u_{j}(t,\mathbf{r})\,dt-u_{j}(0,\mathbf{r})\right|\leq\frac{1}{j}. |  |

The second part is immediate under an easy change of variables, and the fact

 | lim k → ∞ ∫ J k ρ k ​ ( t) ​ [u j ​ ( s + α k, 𝐫) − u j ​ ( α k, 𝐫)] ​ 𝑑 t = 0, \lim_{k\to\infty}\int_{J_{k}}\rho_{k}(t)\left[u_{j}(s+\alpha_{k},\mathbf{r})-u_{j}(\alpha_{k},\mathbf{r})\right]\,dt=0, |  |

for every fixed j j, which is a consequence of the first statement. ∎

Hilbert’s 16th problem This final proposition has been tailored very precisely to be used later when dealing explicitly with Hilbert’s 16th problem.

## 5. Limit cycles for planar, polynomial, differential systems

In this principal section we focus on applying all of our previous abstract and general results to the following setting

 | ℍ = H O 2 ​ ( [0, 1], ℝ 2); \mathbb{H}=H^{2}_{O}([0,1];\mathbb{R}^{2}); |  |

𝕆 ⊂ H O 2 ​ ( [0, 1], ℝ 2) \mathbb{O}\subset H^{2}_{O}([0,1];\mathbb{R}^{2}) is the set of regular (with a no-where vanishing derivative) curves with winding number + 1 +1,

 | 𝕆 = ⋃ d ∈ ℕ 𝕆 d, \mathbb{O}=\bigcup_{d\in\mathbb{N}}\mathbb{O}_{d}, |  |

with 𝕆 d \mathbb{O}_{d}, the subset of 𝕆 \mathbb{O} with absolute winding number not greater than d d; and

 | E ϵ: ℍ → ℝ +, E ϵ ​ ( 𝐮) = ∫ 0 1 F ϵ ​ ( t, 𝐮 ⁡ ( t), 𝐮 ′ ​ ( t), 𝐮 ′′ ​ ( t)) ​ 𝑑 t, E_{\epsilon}:\mathbb{H}\to\mathbb{R}^{+},\quad E_{\epsilon}(\mathbf{u})=\int_{0}^{1}F_{\epsilon}(t,\mathbf{u}(t),\mathbf{u}^{\prime}(t),\mathbf{u}^{\prime\prime}(t))\,dt, |  |

where

 | F ϵ ​ ( t, 𝐮, 𝐳, 𝐙) = \displaystyle F_{\epsilon}(t,\mathbf{u},\mathbf{z},\mathbf{Z})= | 1 2 ​ ( 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐳) 2 + ϵ 2 ​ ( | 𝐙 | 2 + | 𝐳 | 2 + | 𝐮 | 2) \displaystyle\frac{1}{2}(\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{z})^{2}+\frac{\epsilon}{2}(|\mathbf{Z}|^{2}+|\mathbf{z}|^{2}+|\mathbf{u}|^{2}) |  |

 |  | + 𝐮 ⋅ 𝐯 0 ( t) + 𝐳 ⋅ 𝐯 0 ′ ( t) + 𝐙 ⋅ 𝐯 0 ′′ ( t). \displaystyle+\mathbf{u}\cdot\mathbf{v}_{0}(t)+\mathbf{z}\cdot\mathbf{v}^{\prime}_{0}(t)+\mathbf{Z}\cdot\mathbf{v}^{\prime\prime}_{0}(t). |  |

We can, therefore, write

 | E ϵ ​ ( 𝐮) = E 0 ​ ( 𝐮) + ϵ 2 ​ ‖ 𝐮 + 𝐯 0 ‖ H 2 ​ ( [0, 1], ℝ 2) 2 − ϵ 2 ​ ‖ 𝐯 0 ‖ H 2 ​ ( [0, 1], ℝ 2) 2, \displaystyle E_{\epsilon}(\mathbf{u})=E_{0}(\mathbf{u})+\frac{\epsilon}{2}\|\mathbf{u}+\mathbf{v}_{0}\|^{2}_{H^{2}([0,1];\mathbb{R}^{2})}-\frac{\epsilon}{2}\|\mathbf{v}_{0}\|^{2}_{H^{2}([0,1];\mathbb{R}^{2})}, |  |

(5.1) |  | E 0 ​ ( 𝐮) = ∫ 0 1 1 2 ​ ( 𝐅 ⟂ ​ ( 𝐮 ⁡ ( t)) ⋅ 𝐮 ′ ​ ( t)) 2 ​ 𝑑 t. \displaystyle E_{0}(\mathbf{u})=\int_{0}^{1}\frac{1}{2}(\mathbf{F}^{\perp}(\mathbf{u}(t))\cdot\mathbf{u}^{\prime}(t))^{2}\,dt. |  |

Since the quantity

 | − ϵ 2 ​ ‖ 𝐯 0 ‖ H 2 ​ ( [0, 1], ℝ 2) 2 -\frac{\epsilon}{2}\|\mathbf{v}_{0}\|^{2}_{H^{2}([0,1];\mathbb{R}^{2})} |  |

is independent of 𝐮 \mathbf{u}, a constant, we can ignore it, and regard

 | E ϵ ​ ( 𝐮) = E 0 ​ ( 𝐮) + ϵ 2 ​ ‖ 𝐮 − 𝐯 0 ‖ H 2 ​ ( [0, 1], ℝ 2) 2 E_{\epsilon}(\mathbf{u})=E_{0}(\mathbf{u})+\frac{\epsilon}{2}\|\mathbf{u}-\mathbf{v}_{0}\|^{2}_{H^{2}([0,1];\mathbb{R}^{2})} |  |

as our singular-perturbation of E 0 E_{0}. Note that we can write 𝐯 0 \mathbf{v}_{0} or − 𝐯 0 -\mathbf{v}_{0} for the auxiliary path just for notational convenience.

Theorem 2.5 is our guiding principle in this section. We restate it here for the convenience of readers, as we will refer to it often.

###### Theorem 5.1.

Let E ϵ: ℍ → ℝ + E_{\epsilon}:\mathbb{H}\to\mathbb{R}^{+} be a family of smooth, non-negative, coercive functionals, with 0 ≤ E 0 ≤ E ϵ 0\leq E_{0}\leq E_{\epsilon}, and 𝕆 d \mathbb{O}_{d}, d ∈ ℕ d\in\mathbb{N}, an increasing family of open subsets of ℍ \mathbb{H}. As in ( 2.5), put

 | 𝕆 = ⋃ d ∈ ℕ 𝕆 d. \mathbb{O}=\bigcup_{d\in\mathbb{N}}\mathbb{O}_{d}. |  |

Suppose, in addition, that

1. (1)

E ϵ E_{\epsilon} is a Morse functional for positive ϵ \epsilon.

2. (2)

𝕆 d \mathbb{O}_{d} is invariant for all E ϵ E_{\epsilon} if d d is large enough, and every ϵ > 0 \epsilon>0.

3. (3)

For every d d, for a a sufficiently small, and ϵ \epsilon small enough (depending on a a):

  1. (a)

Each component of { E 0 = 0 } ∩ 𝕆 d \{E_{0}=0\}\cap\mathbb{O}_{d} identifies (is contained in), in a one-to-one manner, one component of { E ϵ ≤ a } ∩ 𝕆 d \{E_{\epsilon}\leq a\}\cap\mathbb{O}_{d}.

  2. (b)

Each component of { E ϵ ≤ a } ∩ 𝕆 d \{E_{\epsilon}\leq a\}\cap\mathbb{O}_{d} is topologically equivalent to a ball.

Then

(5.2) |  | #⁡ ( ℙ) ≤ 1 + lim a → 0 lim ϵ → 0 M c ​ r ​ i, ϵ, a, \#(\mathbb{P})\leq 1+\lim_{a\to 0}\lim_{\epsilon\to 0}M_{cri,\epsilon,a}, |  |

if M c ​ r ​ i, ϵ, a M_{cri,\epsilon,a} is the number of critical elements of E ϵ E_{\epsilon} in { E ϵ > a } ∩ 𝕆 \{E_{\epsilon}>a\}\cap\mathbb{O}.

Recall that ℙ \mathbb{P} is the collection of connected components of the zero set { E 0 = 0 } \{E_{0}=0\} in 𝕆 \mathbb{O} (Problem 2.1) whose number we would like to count.

Theorem 3.4 is concerned with main assumption (1) in Theorem 5.1. Main properties of each 𝕆 d \mathbb{O}_{d} need to be addressed. Lemma 5.3 below will help us with the last main assumption (3) in Theorem 5.1. In addition, and this is probably the central part of our proof, we should be able to provide an upper bound for the number M c ​ r ​ i, ϵ, a M_{cri,\epsilon,a} of critical paths of { E ϵ ≥ a } ∩ 𝕆 \{E_{\epsilon}\geq a\}\cap\mathbb{O} independent of a > 0 a>0 small, and ϵ \epsilon sufficiently small.

The program we would like to cover consists then of the following important steps.

1. (1)

Prove that each individual 𝕆 d \mathbb{O}_{d} is invariant for each E ϵ E_{\epsilon}, for d d large enough, and that Morse inequalities are valid for E ϵ E_{\epsilon} in 𝕆 d \mathbb{O}_{d}.

2. (2)

Identification of components of { E 0 = 0 } \{E_{0}=0\} in 𝕆 d \mathbb{O}_{d} through components of { E ϵ ≤ a } ∩ 𝕆 d \{E_{\epsilon}\leq a\}\cap\mathbb{O}_{d} for a a small, d d large, and ϵ \epsilon small enough.

3. (3)

Show that those same components of { E ϵ ≤ a } ∩ 𝕆 d \{E_{\epsilon}\leq a\}\cap\mathbb{O}_{d} are topologically equivalent to a ball for a a small, d d large, and ϵ \epsilon small enough.

4. (4)

Argue that

 | E 0 ′: H O 2 ​ ( [0, 1], ℝ 2) → H O 2 ​ ( [0, 1], ℝ 2) E^{\prime}_{0}:H^{2}_{O}([0,1];\mathbb{R}^{2})\to H^{2}_{O}([0,1];\mathbb{R}^{2}) |  |

is compact.

5. (5)

For each fixed 𝐮 ∈ H O 2 ​ ( [0, 1], ℝ 2) \mathbf{u}\in H^{2}_{O}([0,1];\mathbb{R}^{2}), the linear, self-adjoint operator

 | E 0 ′′ ​ ( 𝐮): H O 2 ​ ( [0, 1], ℝ 2) → H O 2 ​ ( [0, 1], ℝ 2) E^{\prime\prime}_{0}(\mathbf{u}):H^{2}_{O}([0,1];\mathbb{R}^{2})\to H^{2}_{O}([0,1];\mathbb{R}^{2}) |  |

is compact as well.

6. (6)

Examine the differential system whose solutions are critical paths for E ϵ E_{\epsilon} and E 0 E_{0}.

7. (7)

Explore the possible asymptotic limits of branches of critical paths { 𝐮 ϵ } \{\mathbf{u}_{\epsilon}\} with arbitrarily small critical value a a uniformly away from zero with respect to ϵ \epsilon, of the previous, ϵ \epsilon -dependent, singularly-perturbed functional as ϵ ↘ 0 \epsilon\searrow 0.

8. (8)

For each of the possible previous asymptotic limits, find a suitable upper bound for the number of branches converging to each such limit.

9. (9)

Conclude with an upper bound for the number of limit cycles of a planar, polynomial, differential system of degree n n.

We will be covering all of these steps successively in the coming subsections, and constantly monitoring what we are achieving for a complete proof of Theorems 1.1 and 1.2.

### 5.1. Role played by 𝕆 d \mathbb{O}_{d}

The choice of the ambient set 𝕆 d \mathbb{O}_{d} will be of paramount importance for us. We cover several crucial aspects in the following subsections.

#### 5.1.1. Invariance of 𝕆 d \mathbb{O}_{d} under E ϵ E_{\epsilon}

This property means that the flow of − E ϵ -E_{\epsilon}, leading to smaller values of E ϵ E_{\epsilon}, cannot push paths in 𝕆 d \mathbb{O}_{d} to a larger value of d d. This looks intuitively pretty clear as such a behavior could only be favored by a much more erratic functional than E 0 E_{0}. Formally, we need to argue that the value of E ϵ E_{\epsilon} at a path 𝐮 ⁡ ( t) ∈ ∂ 𝕆 d \mathbf{u}(t)\in\partial\mathbb{O}_{d} decreases when we perturb 𝐮 ⁡ ( t) \mathbf{u}(t) locally in such a way that the resulting perturbation 𝐮 ~ ​ ( t) \tilde{\mathbf{u}}(t) lies back in 𝕆 d \mathbb{O}_{d}.

We will be using the compactness of the derivative mapping

 | E 0 ′ ​ ( 𝐮): H O 2 ​ ( [0, 1], ℝ 2) → H O 2 ​ ( [0, 1], ℝ 2), E^{\prime}_{0}(\mathbf{u}):H^{2}_{O}([0,1];\mathbb{R}^{2})\to H^{2}_{O}([0,1];\mathbb{R}^{2}), |  |

which means that the sequence { E 0 ′ ​ ( 𝐮 j) } \{E^{\prime}_{0}(\mathbf{u}_{j})\} always admits a subsequence converging strongly in H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}) whenever { 𝐮 j } \{\mathbf{u}_{j}\} is uniformly bounded in the same space. For the sake of organization, this property will be treated in the subsequent subsections.

###### Proposition 5.2.

Suppose the auxiliary path 𝐯 0 \mathbf{v}_{0} in ( 5.12) is smooth, and belongs to 𝕆 1 \mathbb{O}_{1} ( d = 1 d=1). Then 𝕆 d \mathbb{O}_{d} is invariant under E ϵ E_{\epsilon} for ϵ > 0 \epsilon>0, and every sufficiently large d ∈ ℕ d\in\mathbb{N} (independently of ϵ \epsilon).

###### Proof.

Suppose, seeking a contradiction, that we could find a subsequence of increasing values of d ∈ ℕ d\in\mathbb{N} with paths 𝐮 d ∈ ∂ 𝕆 d \mathbf{u}_{d}\in\partial\mathbb{O}_{d} such that − E 0 ′ ​ ( 𝐮 d) -E^{\prime}_{0}(\mathbf{u}_{d}) pushes 𝐮 d \mathbf{u}_{d} off 𝕆 d \mathbb{O}_{d}, for every such d d. Since functional E ϵ E_{\epsilon} is coercive, sub-level sets { E ϵ ≤ b ϵ } \{E_{\epsilon}\leq b_{\epsilon}\} for b ϵ b_{\epsilon} large enough are invariant (just as it was indicated in the proof of Theorem 2.5), and hence we can assume that the set of paths { 𝐮 d } \{\mathbf{u}_{d}\} is uniformly bounded. By the claimed compactness of the derivative operator (Lemma 5.6 below), for some subsequence if necessary, { E 0 ′ ​ ( 𝐮 d) } \{E^{\prime}_{0}(\mathbf{u}_{d})\} converges (strongly) in H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}) to some path. By Proposition 4.15, we conclude that the combination

 | 𝐮 d − δ ​ E 0 ′ ​ ( 𝐮 d) \mathbf{u}_{d}-\delta E^{\prime}_{0}(\mathbf{u}_{d}) |  |

cannot push 𝐮 d \mathbf{u}_{d} off 𝕆 d \mathbb{O}_{d} for arbitrary small values of δ \delta.

The effect of adding the perturbation

 | ϵ 2 ​ ‖ 𝐮 − 𝐯 0 ‖ 2 \frac{\epsilon}{2}\|\mathbf{u}-\mathbf{v}_{0}\|^{2} |  |

to E 0 E_{0} only enforces the behavior just described if 𝐯 0 \mathbf{v}_{0} is taken in 𝕆 1 \mathbb{O}_{1}, being this term a multiple of the (square of the) distance to an element of 𝕆 1 \mathbb{O}_{1}. This contradiction shows that 𝕆 d \mathbb{O}_{d} is in fact invariant for − E ϵ -E_{\epsilon} for all large d d.

The same argument also justifies that there cannot be a critical path of E ϵ E_{\epsilon} on ∂ 𝕆 d \partial\mathbb{O}_{d} since such possibility would force − E 0 ′ -E^{\prime}_{0} to point off 𝕆 d \mathbb{O}_{d} which has been discarded above. Indeed, if

(5.3) |  | E 0 ′ ​ ( 𝐮) + ϵ ⁡ ( 𝐮 − 𝐯 0) = 𝟎, 𝐮 ∈ ∂ 𝕆 d, E^{\prime}_{0}(\mathbf{u})+\epsilon(\mathbf{u}-\mathbf{v}_{0})=\mathbf{0},\mathbf{u}\in\partial\mathbb{O}_{d}, |  |

then the element

 | ϵ ⁡ ( 𝐮 − 𝐯 0) = − E 0 ′ ​ ( 𝐮) \epsilon(\mathbf{u}-\mathbf{v}_{0})=-E^{\prime}_{0}(\mathbf{u}) |  |

should point off 𝕆 d \mathbb{O}_{d} because 𝐮 − 𝐯 0 \mathbf{u}-\mathbf{v}_{0} does. But being equal to − E 0 ′ ​ ( 𝐮) -E^{\prime}_{0}(\mathbf{u}), this behavior has been discarded above, for large d d. Hence ( 5.3) is impossible for large d d. ∎

#### 5.1.2. Identification of components of { E 0 = 0 } \{E_{0}=0\}

Recall that

 | E 0 ​ ( 𝐮) = ∫ 0 1 1 2 ​ Z 2 ​ 𝑑 t, Z = P ⁡ ( x, y) ​ y ′ − Q ⁡ ( x, y) ​ x ′, 𝐮 = ( x, y). E_{0}(\mathbf{u})=\int_{0}^{1}\frac{1}{2}Z^{2}\,dt,\quad Z=P(x,y)y^{\prime}-Q(x,y)x^{\prime},\quad\mathbf{u}=(x,y). |  |

###### Lemma 5.3.

Let ℙ ′ \mathbb{P}^{\prime} be a finite subset of ℙ \mathbb{P}. There is a ⁡ ( ℙ ′) > 0 a(\mathbb{P}^{\prime})>0 and d ⁡ ( ℙ ′) ∈ ℕ d(\mathbb{P}^{\prime})\in\mathbb{N}, such that each component of { E 0 ≤ a } ∩ 𝕆 d \{E_{0}\leq a\}\cap\mathbb{O}_{d}, for a < a ⁡ ( ℙ ′) a<a(\mathbb{P}^{\prime}) and d ≥ d ⁡ ( ℙ ′) d\geq d(\mathbb{P}^{\prime}), contains at most a unique element of ℙ ′ \mathbb{P}^{\prime}.

###### Proof.

Given that ℙ ′ \mathbb{P}^{\prime} is finite, we can take d ⁡ ( ℙ ′) d(\mathbb{P}^{\prime}) large enough so that ℙ ′ ⊂ 𝕆 d \mathbb{P}^{\prime}\subset\mathbb{O}_{d} for d ≥ d ⁡ ( ℙ ′) d\geq d(\mathbb{P}^{\prime}). Suppose, seeking a contradiction, that we could find two distinct elements of ℙ ′ \mathbb{P}^{\prime} in the same component of { E 0 ≤ δ } ∩ 𝕆 d \{E_{0}\leq\delta\}\cap\mathbb{O}_{d} for every positive δ \delta, and some d d large. That would imply that for every such δ \delta, there is a continuous path

 | σ δ ​ ( s): [0, 1] → 𝕆 d, \sigma_{\delta}(s):[0,1]\to\mathbb{O}_{d}, |  |

joining two different components of { E 0 = 0 } \{E_{0}=0\} in ℙ ′ \mathbb{P}^{\prime} entirely contained in { E 0 ≤ δ } ∩ 𝕆 d \{E_{0}\leq\delta\}\cap\mathbb{O}_{d}.

Let 𝐊 \mathbf{K} be a compact set separating in the plane two different limit cycles in ℙ ′ \mathbb{P}^{\prime}. By continuity, σ δ \sigma_{\delta}, belonging to { E 0 ≤ δ } ∩ 𝕆 d \{E_{0}\leq\delta\}\cap\mathbb{O}_{d} and joining the two elements of ℙ ′ \mathbb{P}^{\prime}, must intersect 𝐊 \mathbf{K} at some point belonging to the image of a certain path 𝐮 δ ( = σ δ ( s δ), s δ ∈ [0, 1]) \mathbf{u}_{\delta}(=\sigma_{\delta}(s_{\delta}),s_{\delta}\in[0,1]) with E 0 ​ ( 𝐮 δ) ≤ δ E_{0}(\mathbf{u}_{\delta})\leq\delta. By the compactness of 𝐊 \mathbf{K}, there must be an accumulation point 𝐏 ∈ 𝐊 \mathbf{P}\in\mathbf{K} as δ → 0 \delta\to 0, which in this way does not belong to any of the limit cycles in ℙ ′ \mathbb{P}^{\prime}. We thus have that

 | E 0 ​ ( 𝐮 δ) ≤ δ, 𝐮 δ ​ ( 0) ∈ 𝐊, 𝐮 δ ​ ( 0) → 𝐏 ​ as ​ δ → 0, 𝐏 ∈ 𝐊, 𝐮 δ ∈ 𝕆 d. E_{0}(\mathbf{u}_{\delta})\leq\delta,\quad\mathbf{u}_{\delta}(0)\in\mathbf{K},\quad\mathbf{u}_{\delta}(0)\to\mathbf{P}\hbox{ as }\delta\to 0,\quad\mathbf{P}\in\mathbf{K},\quad\mathbf{u}_{\delta}\in\mathbb{O}_{d}. |  |

Put

 | Z δ ​ ( t) = P ⁡ ( 𝐮 δ) ​ y δ ′ − Q ⁡ ( 𝐮 δ) ​ x δ ′, 𝐮 δ = ( x δ, y δ), Z_{\delta}(t)=P(\mathbf{u}_{\delta})y^{\prime}_{\delta}-Q(\mathbf{u}_{\delta})x^{\prime}_{\delta},\quad\mathbf{u}_{\delta}=(x_{\delta},y_{\delta}), |  |

a concrete function of t t, and notice that Z δ → 0 Z_{\delta}\to 0 in L 2 ​ ( 0, 1) L^{2}(0,1), as δ → 0 \delta\to 0, precisely because E 0 ​ ( 𝐮 δ) → 0 E_{0}(\mathbf{u}_{\delta})\to 0. The path 𝐮 δ \mathbf{u}_{\delta} turns out to be the unique solution of the problem

 | P ⁡ ( X, Y) ​ Y ′ − Q ⁡ ( X, Y) ​ X ′ = Z δ ​ ( t) ​ in ​ [0, 1], ( X ⁡ ( 0), Y ⁡ ( 0)) = 𝐮 δ ​ ( 0). P(X,Y)Y^{\prime}-Q(X,Y)X^{\prime}=Z_{\delta}(t)\hbox{ in }[0,1],\quad(X(0),Y(0))=\mathbf{u}_{\delta}(0). |  |

By the indicated convergence of the right-hand side Z δ Z_{\delta}, the fact that 𝐮 δ ∈ 𝕆 d \mathbf{u}_{\delta}\in\mathbb{O}_{d} for all δ \delta and some fixed d d, and the convergence of 𝐮 δ ​ ( 0) \mathbf{u}_{\delta}(0), 𝐮 δ \mathbf{u}_{\delta} must converge to the unique solution 𝐮 = ( x, y) \mathbf{u}=(x,y) of

 | P ⁡ ( x, y) ​ y ′ − Q ⁡ ( x, y) ​ x ′ = 0 ​ in ​ [0, 1], ( x ⁡ ( 0), y ⁡ ( 0)) = 𝐏 ∈ 𝐊. P(x,y)y^{\prime}-Q(x,y)x^{\prime}=0\hbox{ in }[0,1],\quad(x(0),y(0))=\mathbf{P}\in\mathbf{K}. |  |

This is not possible since we would have E 0 ​ ( 𝐮) = 0 E_{0}(\mathbf{u})=0 and 𝐮 ⁡ ( 0) = 𝐏 \mathbf{u}(0)=\mathbf{P}, and there is no limit cycle starting at the set 𝐊 \mathbf{K}. This is the sought contradiction, and ends the proof.

Note that if we would allow the possibility that d d might grow indefinitely as δ → 0 \delta\to 0, the claimed convergence above would be wrong in general. This is, in fact, the main reason why one is forced to work on subsets 𝕆 d \mathbb{O}_{d} for fixed (though possibly large) d d. ∎

If we now realize that

(5.4) |  | { E 0 = 0 } ∩ 𝕆 d ⊂ { E ϵ ≤ a } ∩ 𝕆 d ⊂ { E 0 ≤ a } ∩ 𝕆 d, \{E_{0}=0\}\cap\mathbb{O}_{d}\subset\{E_{\epsilon}\leq a\}\cap\mathbb{O}_{d}\subset\{E_{0}\leq a\}\cap\mathbb{O}_{d}, |  |

for arbitrary a > 0 a>0, d ∈ ℕ d\in\mathbb{N}, and ϵ \epsilon sufficiently small (depending on a a), we see that for a a sufficiently small and every large d d, once we focus on an arbitrary finite subset ℙ ′ \mathbb{P}^{\prime}, components of the set on the left-hand side identify in a one-to-one manner components of the intermediate level set according to the above lemma.

#### 5.1.3. Components of { E ϵ ≤ a } ∩ 𝕆 d \{E_{\epsilon}\leq a\}\cap\mathbb{O}_{d} are topologically equivalent to a ball

Recall that this set includes all 1 1 -periodic, 𝒞 1 \mathcal{C}^{1} -, non-singular parameterizations of paths made up of pieces of integral curves with absolute winding number not greater than d d. In particular, limit cycles of our differential system admit a parametrization 𝐮 ⁡ ( t) \mathbf{u}(t) belonging to 𝕆 d \mathbb{O}_{d} for some d d. Because they are isolated from each other, different limit cycles of a finite subset belong to different connected components of { E 0 = 0 } ∩ 𝕆 d \{E_{0}=0\}\cap\mathbb{O}_{d} for some large enough d d.

Given any 1 1 -periodic path

 | 𝐮 ( t) ∈ 𝕆 d ∩ { E 0 = 0 }, \mathbf{u}(t)\in\mathbb{O}_{d}\cap\{E_{0}=0\}, |  |

the connected component determined by it corresponds to the various reparametrizations of 𝐮 ⁡ ( t) \mathbf{u}(t) of the form 𝐮 ⁡ ( σ ⁡ ( s)) \mathbf{u}(\sigma(s)) for a suitable class of functions σ ⁡ ( s) \sigma(s) to maintain it within 𝕆 d \mathbb{O}_{d}. More specifically, we consider

 | Λ = { σ ( s): [0, 1] → ℝ, σ ′, abs. continuous, σ ′ > 0, ∫ 0 1 σ ′ ( s) d s = 1 }. \Lambda=\left\{\sigma(s):[0,1]\to\mathbb{R},\sigma^{\prime},\hbox{abs. continuous},\sigma^{\prime}>0,\int_{0}^{1}\sigma^{\prime}(s)\,ds=1\right\}. |  |

Note that Λ \Lambda is a convex set. Recall that curves in 𝕆 \mathbb{O} are 𝒞 1 \mathcal{C}^{1} and cannot have a vanishing tangent vector, hence they can never turn around.

###### Lemma 5.4.

Let E 0 ​ ( 𝐮) = 0 E_{0}(\mathbf{u})=0, for 𝐮 ∈ H O 2 ​ ( [0, 1], ℝ 2) ∩ 𝕆 d \mathbf{u}\in H^{2}_{O}([0,1];\mathbb{R}^{2})\cap\mathbb{O}_{d}.

1. (1)

The component of { E 0 = 0 } \{E_{0}=0\} in 𝕆 d \mathbb{O}_{d} determined by 𝐮 \mathbf{u} is

 | Λ 𝐮 ≡ { 𝐮 ⁡ ( σ ⁡ ( s)): σ ∈ Λ }. \Lambda_{\mathbf{u}}\equiv\{\mathbf{u}(\sigma(s)):\sigma\in\Lambda\}. |  |

2. (2)

The set Λ 𝐮 \Lambda_{\mathbf{u}} is topologically equivalent to a ball.

###### Proof.

The first assertion is clear because winding and absolute winding numbers are not related to parameter dependence, but only on taken-on values of the normalized tangent vectors. For the second part, note that because Λ \Lambda is a convex set, it is topologically equivalent to a ball. Λ 𝐮 \Lambda_{\mathbf{u}}, being the image under a continuous mapping of Λ \Lambda, must also be topologically equivalent to a ball. ∎

We next treat the family of perturbed functionals E ϵ E_{\epsilon}.

###### Lemma 5.5.

Let ℂ d \mathbb{C}_{d} be a component of { E 0 = 0 } \{E_{0}=0\} in 𝕆 d \mathbb{O}_{d}, topologically equivalent to a ball, according to Lemma 5.4, which determines a unique component ℂ a, ϵ, d \mathbb{C}_{a,\epsilon,d} of { E ϵ ≤ a } ∩ 𝕆 d \{E_{\epsilon}\leq a\}\cap\mathbb{O}_{d} according to Lemma 5.3 and ( 5.4). For appropriate a a, d d and ϵ \epsilon, ℂ a, ϵ, d \mathbb{C}_{a,\epsilon,d} is topologically equivalent to a ball.

###### Proof.

Because ℂ d \mathbb{C}_{d} is smooth and topologically equivalent to a ball, a smooth one-to-one map 𝕋: ℍ → ℍ \mathbb{T}:\mathbb{H}\to\mathbb{H} can be found so that 𝕋 − 1 ​ ( ℂ d) \mathbb{T}^{-1}(\mathbb{C}_{d}) is smooth and convex. The composition functional E 0 ∘ 𝕋 E_{0}\circ\mathbb{T}, being smooth, non-negative, and with zero set 𝕋 − 1 ​ ( ℂ d) \mathbb{T}^{-1}(\mathbb{C}_{d}), is therefore convex in a vicinity of 𝕋 − 1 ​ ( ℂ d) \mathbb{T}^{-1}(\mathbb{C}_{d}). The sum

 | E ϵ ∘ 𝕋 ⁡ ( 𝐮) = E 0 ∘ 𝕋 ⁡ ( 𝐮) + ϵ 2 ​ ‖ 𝕋 ⁡ ( 𝐮) − 𝐯 0 ‖ 2 E_{\epsilon}\circ\mathbb{T}(\mathbf{u})=E_{0}\circ\mathbb{T}(\mathbf{u})+\frac{\epsilon}{2}\|\mathbb{T}(\mathbf{u})-\mathbf{v}_{0}\|^{2} |  |

might not be convex. Yet the two functionals

 | ϵ 2 ​ ‖ 𝕋 ⁡ ( 𝐮) − 𝐯 0 ‖ 2, ϵ 2 ​ ‖ 𝐮 − 𝐯 0 ‖ 2 \frac{\epsilon}{2}\|\mathbb{T}(\mathbf{u})-\mathbf{v}_{0}\|^{2},\quad\frac{\epsilon}{2}\|\mathbf{u}-\mathbf{v}_{0}\|^{2} |  |

share the same set of critical points (because 𝕋 \mathbb{T} is a one-to-one smooth map) which is the singleton { 𝐯 0 } \{\mathbf{v}_{0}\}. This in turn implies that the two level sets

 | { E ϵ ∘ 𝕋 ≤ a }, { E 0 ∘ 𝕋 + ϵ 2 ∥ 𝐮 − 𝐯 0 ∥ 2 ≤ a } \{E_{\epsilon}\circ\mathbb{T}\leq a\},\quad\{E_{0}\circ\mathbb{T}+\frac{\epsilon}{2}\|\mathbf{u}-\mathbf{v}_{0}\|^{2}\leq a\} |  |

are topologically equivalent. Since the functional in the second level set is convex for a a small, it is equivalent topologically equivalent to a ball; and hence so is the first. Finally

 | 𝕋 ( { E ϵ ∘ 𝕋 ≤ a }) = { E ϵ ≤ a } \mathbb{T}\left(\{E_{\epsilon}\circ\mathbb{T}\leq a\}\right)=\{E_{\epsilon}\leq a\} |  |

will be equivalent to a ball too. Everything takes place in 𝕆 d \mathbb{O}_{d}. ∎

### 5.2. The derivatives of E 0 E_{0}

Our initial calculations focus on looking at the first-order and second-order derivatives of the base functional E 0 E_{0}.

#### 5.2.1. The first derivative

For our functional E 0 E_{0}, it is easy to find an expression for

 | ⟨ E 0 ′ ​ ( 𝐮), 𝐔 ⟩, 𝐮, 𝐔 ∈ H O 2 ​ ( [0, 1], ℝ 2). \langle E^{\prime}_{0}(\mathbf{u}),\mathbf{U}\rangle,\quad\mathbf{u},\mathbf{U}\in H^{2}_{O}([0,1];\mathbb{R}^{2}). |  |

Indeed, by definition we have

(5.5) |  | ⟨ E 0 ′ ​ ( 𝐮), 𝐔 ⟩ = d d ​ τ | τ = 0 ​ E 0 ​ ( 𝐮 + τ ​ 𝐔). \langle E^{\prime}_{0}(\mathbf{u}),\mathbf{U}\rangle=\left.\frac{d}{d\tau}\right|_{\tau=0}E_{0}(\mathbf{u}+\tau\mathbf{U}). |  |

Since

 | E 0 ​ ( 𝐮 + τ ​ 𝐔) = 1 2 ​ ∫ 0 1 [𝐅 ⟂ ​ ( 𝐮 + τ ​ 𝐔) ⋅ ( 𝐮 ′ + τ ​ 𝐔 ′)] 2 ​ 𝑑 t, E_{0}(\mathbf{u}+\tau\mathbf{U})=\frac{1}{2}\int_{0}^{1}[\mathbf{F}^{\perp}(\mathbf{u}+\tau\mathbf{U})\cdot(\mathbf{u}^{\prime}+\tau\mathbf{U}^{\prime})]^{2}\,dt, |  |

then from ( 5.5) we have

(5.6) |  | ⟨ E 0 ′ ​ ( 𝐮), 𝐔 ⟩ = ∫ 0 1 ( 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐮 ′) ​ [( D ​ 𝐅 ⟂ ​ ( 𝐮) ​ 𝐔) ⋅ 𝐮 ′ + 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐔 ′] ​ 𝑑 t. \langle E^{\prime}_{0}(\mathbf{u}),\mathbf{U}\rangle=\int_{0}^{1}(\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{u}^{\prime})[(D\mathbf{F}^{\perp}(\mathbf{u})\mathbf{U})\cdot\mathbf{u}^{\prime}+\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{U}^{\prime}]\,dt. |  |

We are, therefore, seeking an element

 | 𝐯 ( = E 0 ′ ​ ( 𝐮)) ∈ H O 2 ​ ( [0, 1], ℝ 2) \mathbf{v}(=E^{\prime}_{0}(\mathbf{u}))\in H^{2}_{O}([0,1];\mathbb{R}^{2}) |  |

such that

 | 𝐯 ⋅ 𝐔 = ⟨ E 0 ′ ​ ( 𝐮), 𝐔 ⟩, \mathbf{v}\cdot\mathbf{U}=\langle E^{\prime}_{0}(\mathbf{u}),\mathbf{U}\rangle, |  |

that is to say

(5.7) |  | ∫ 0 1 ( 𝐯 ⋅ 𝐔 + 𝐯 ′ ⋅ 𝐔 ′ + 𝐯 ′′ ⋅ 𝐔 ′′) ​ 𝑑 t = ∫ 0 1 ( 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐮 ′) ​ [( D ​ 𝐅 ⟂ ​ ( 𝐮) ​ 𝐔) ⋅ 𝐮 ′ + 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐔 ′] ​ 𝑑 t \int_{0}^{1}(\mathbf{v}\cdot\mathbf{U}+\mathbf{v}^{\prime}\cdot\mathbf{U}^{\prime}+\mathbf{v}^{\prime\prime}\cdot\mathbf{U}^{\prime\prime})\,dt=\int_{0}^{1}(\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{u}^{\prime})[(D\mathbf{F}^{\perp}(\mathbf{u})\mathbf{U})\cdot\mathbf{u}^{\prime}+\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{U}^{\prime}]\,dt |  |

for every

 | 𝐔 ∈ H O 2 ​ ( [0, 1], ℝ 2). \mathbf{U}\in H^{2}_{O}([0,1];\mathbb{R}^{2}). |  |

There is a unique such 𝐯 \mathbf{v}, which turns out to be the minimizer (with respect to

 | OPEN 𝐔 ∈ H O 2 ​ ( [0, 1], ℝ 2)) \mathbf{U}\in H^{2}_{O}([0,1];\mathbb{R}^{2})) |  |

of the augmented functional

(5.8) |  | ∫ 0 1 [1 2 ​ | 𝐔 ′′ | 2 + 1 2 ​ | 𝐔 ′ | 2 + 1 2 ​ | 𝐔 | 2 − ( 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐮 ′) ​ [( D ​ 𝐅 ⟂ ​ ( 𝐮) ​ 𝐔) ⋅ 𝐮 ′ + 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐔 ′]] ​ 𝑑 t. \int_{0}^{1}[\frac{1}{2}|\mathbf{U}^{\prime\prime}|^{2}+\frac{1}{2}|\mathbf{U}^{\prime}|^{2}+\frac{1}{2}|\mathbf{U}|^{2}-(\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{u}^{\prime})[(D\mathbf{F}^{\perp}(\mathbf{u})\mathbf{U})\cdot\mathbf{u}^{\prime}+\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{U}^{\prime}]]\,dt. |  |

The existence of a unique minimizer for this problem, which is quadratic, is a direct consequence of the classical Lax-Milgram Theorem (see Corollary 5.8 of [7] for instance).

Therefore the equation for

 | 𝐯 = E 0 ′ ​ ( 𝐮) ∈ H O 2 ​ ( [0, 1], ℝ 2) \mathbf{v}=E^{\prime}_{0}(\mathbf{u})\in H^{2}_{O}([0,1];\mathbb{R}^{2}) |  |

will be the associated Euler-Lagrange system for the functional ( 5.8) as it is given by this last theorem

(5.9) |  | [𝐯 ′′] ′′ − [𝐯 ′ + ( 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐮 ′) ​ 𝐅 ⟂ ​ ( 𝐮)] ′ + 𝐯 + ( 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐮 ′) ​ 𝐮 ′ T ​ D ​ 𝐅 ⟂ ​ ( 𝐮) = 𝟎 ​ in ​ ( 0, 1). [\mathbf{v}^{\prime\prime}]^{\prime\prime}-[\mathbf{v}^{\prime}+(\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{u}^{\prime})\mathbf{F}^{\perp}(\mathbf{u})]^{\prime}+\mathbf{v}+(\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{u}^{\prime})\mathbf{u}^{\prime T}D\mathbf{F}^{\perp}(\mathbf{u})=\mathbf{0}\hbox{ in }(0,1). |  |

Its weak formulation is exactly ( 5.7).

#### 5.2.2. The second derivative

If, in general, we have a certain smooth, 𝒞 2 \mathcal{C}^{2} -functional E: ℍ → ℝ E:\mathbb{H}\to\mathbb{R} over a Hilbert space ℍ \mathbb{H} with derivative E ′: ℍ → ℍ E^{\prime}:\mathbb{H}\to\mathbb{H}, there are various ways to deal with the second derivative, but probably the best suited for our purposes is to consider the derivative

 | ⟨ E ′′ ​ ( 𝐮), ( 𝐔, 𝐔 ¯) ⟩ = d d ​ δ | δ = 0 ​ ⟨ E ′ ​ ( 𝐮 + δ ​ 𝐔), 𝐔 ¯ ⟩, \langle E^{\prime\prime}(\mathbf{u}),(\mathbf{U},\overline{\mathbf{U}})\rangle=\left.\frac{d}{d\delta}\right|_{\delta=0}\langle E^{\prime}(\mathbf{u}+\delta\mathbf{U}),\overline{\mathbf{U}}\rangle, |  |

where both vector fields 𝐔 \mathbf{U} and 𝐔 ¯ \overline{\mathbf{U}} belong to ℍ \mathbb{H}. In our situation, and in view of ( 5.6), we have

 | ⟨ E 0 ′′ ​ ( 𝐮), ( 𝐔, 𝐔 ¯) ⟩ = d d ​ δ | δ = 0 ∫ 0 1 ( 𝐅 ⟂ ( 𝐮 + δ 𝐔) ⋅ ( 𝐮 ′ + δ 𝐔 ′)) × [∇ 𝐅 ⟂ ​ ( 𝐮 + δ ​ 𝐔) ​ 𝐔 ¯ ⋅ ( 𝐮 ′ + δ ​ 𝐔 ′) + 𝐅 ⟂ ​ ( 𝐮 + δ ​ 𝐔) ⋅ 𝐔 ¯ ′] ​ d ​ t = ∫ 0 1 ( 𝐅 ⟂ ( 𝐮) ⋅ 𝐮 ′) [∇ 2 𝐅 ⟂ ( 𝐮): ( 𝐔, 𝐔 ¯, 𝐮 ′) + ∇ 𝐅 ⟂ ( 𝐮): ( 𝐔 ¯, 𝐔 ′) + ∇ 𝐅 ⟂ ( 𝐮): ( 𝐔, 𝐔 ¯ ′)] d t + ∫ 0 1 [∇ 𝐅 ⟂ ( 𝐮) 𝐔 ⋅ 𝐮 ′ + 𝐅 ⟂ ( 𝐮) ⋅ 𝐔 ′] × [∇ 𝐅 ⟂ ​ ( 𝐮) ​ 𝐔 ¯ ⋅ 𝐮 ′ + 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐔 ¯ ′] ​ d ​ t \begin{array}[]{rl}\langle E^{\prime\prime}_{0}(\mathbf{u}),(\mathbf{U},\overline{\mathbf{U}})\rangle=&\left.\displaystyle\frac{d}{d\delta}\right|_{\delta=0}\displaystyle\int_{0}^{1}(\mathbf{F}^{\perp}(\mathbf{u}+\delta\mathbf{U})\cdot(\mathbf{u}^{\prime}+\delta\mathbf{U}^{\prime}))\times\\ &\qquad\qquad[\nabla\mathbf{F}^{\perp}(\mathbf{u}+\delta\mathbf{U})\overline{\mathbf{U}}\cdot(\mathbf{u}^{\prime}+\delta\mathbf{U}^{\prime})+\mathbf{F}^{\perp}(\mathbf{u}+\delta\mathbf{U})\cdot\overline{\mathbf{U}}^{\prime}]\,dt\\ =&\displaystyle\int_{0}^{1}(\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{u}^{\prime})[\nabla^{2}\mathbf{F}^{\perp}(\mathbf{u}):(\mathbf{U},\overline{\mathbf{U}},\mathbf{u}^{\prime})+\nabla\mathbf{F}^{\perp}(\mathbf{u}):(\overline{\mathbf{U}},\mathbf{U}^{\prime})\\ &\qquad\qquad\qquad+\nabla\mathbf{F}^{\perp}(\mathbf{u}):(\mathbf{U},\overline{\mathbf{U}}^{\prime})]\,dt\\ &+\displaystyle\int_{0}^{1}[\nabla\mathbf{F}^{\perp}(\mathbf{u})\mathbf{U}\cdot\mathbf{u}^{\prime}+\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{U}^{\prime}]\times\\ &\qquad\qquad[\nabla\mathbf{F}^{\perp}(\mathbf{u})\overline{\mathbf{U}}\cdot\mathbf{u}^{\prime}+\mathbf{F}^{\perp}(\mathbf{u})\cdot\overline{\mathbf{U}}^{\prime}]\,dt\end{array} |  |

Through this long formula, we can understand, for such a 𝐮 \mathbf{u} given and fixed, the linear operator

 | E 0 ′′ ​ ( 𝐮): H O 2 ​ ( [0, 1], ℝ 2) → H O 2 ​ ( [0, 1], ℝ 2). E^{\prime\prime}_{0}(\mathbf{u}):H^{2}_{O}([0,1];\mathbb{R}^{2})\to H^{2}_{O}([0,1];\mathbb{R}^{2}). |  |

Let

 | 𝐔 ∈ H O 2 ​ ( [0, 1], ℝ 2) \mathbf{U}\in H^{2}_{O}([0,1];\mathbb{R}^{2}) |  |

be given. The image

 | 𝐕 = E 0 ′′ ​ ( 𝐮) ​ 𝐔 ∈ H O 2 ​ ( [0, 1], ℝ 2) \mathbf{V}=E^{\prime\prime}_{0}(\mathbf{u})\mathbf{U}\in H^{2}_{O}([0,1];\mathbb{R}^{2}) |  |

of 𝐔 \mathbf{U} under the linear map E 0 ′′ ​ ( 𝐮) E^{\prime\prime}_{0}(\mathbf{u}) is determined through the identity

(5.10) |  | ⟨ E 0 ′′ ​ ( 𝐮), ( 𝐔, 𝐔 ¯) ⟩ = ⟨ E 0 ′′ ​ ( 𝐮) ​ 𝐔, 𝐔 ¯ ⟩ = ⟨ 𝐕, 𝐔 ¯ ⟩ \langle E^{\prime\prime}_{0}(\mathbf{u}),(\mathbf{U},\overline{\mathbf{U}})\rangle=\langle E^{\prime\prime}_{0}(\mathbf{u})\mathbf{U},\overline{\mathbf{U}}\rangle=\langle\mathbf{V},\overline{\mathbf{U}}\rangle |  |

for all

 | 𝐔 ¯ ∈ H O 2 ​ ( [0, 1], ℝ 2). \overline{\mathbf{U}}\in H^{2}_{O}([0,1];\mathbb{R}^{2}). |  |

The element 𝐕 \mathbf{V} defined through ( 5.10) is the solution of a standard quadratic variational problem for which the weak form of its optimality condition is precisely ( 5.10).

### 5.3. Compactness

The calculations in the preceding subsection enable us to prove the following facts.

#### 5.3.1. Compactness of E 0 ′ E^{\prime}_{0}

###### Lemma 5.6.

Let { 𝐮 j } \{\mathbf{u}_{j}\} be a uniformly bounded sequence in H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}), and { 𝐯 j } \{\mathbf{v}_{j}\} the sequence of derivatives

 | 𝐯 j = E 0 ′ ​ ( 𝐮 j) ∈ H O 2 ​ ( [0, 1], ℝ 2) \mathbf{v}_{j}=E^{\prime}_{0}(\mathbf{u}_{j})\in H^{2}_{O}([0,1];\mathbb{R}^{2}) |  |

which are solutions of ( 5.9) for 𝐮 = 𝐮 j \mathbf{u}=\mathbf{u}_{j}. Then { 𝐯 j } \{\mathbf{v}_{j}\} is relatively compact in H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}).

###### Proof.

For the sake of notation, set

 | 𝐆 j ≡ ( 𝐅 ⟂ ​ ( 𝐮 j) ⋅ 𝐮 j ′) ​ 𝐅 ⟂ ​ ( 𝐮 j), 𝐇 j ≡ ( 𝐅 ⟂ ​ ( 𝐮 j) ⋅ 𝐮 j ′) ​ 𝐮 j ′ T ​ D ​ 𝐅 ⟂ ​ ( 𝐮 j). \mathbf{G}_{j}\equiv(\mathbf{F}^{\perp}(\mathbf{u}_{j})\cdot\mathbf{u}^{\prime}_{j})\mathbf{F}^{\perp}(\mathbf{u}_{j}),\quad\mathbf{H}_{j}\equiv(\mathbf{F}^{\perp}(\mathbf{u}_{j})\cdot\mathbf{u}^{\prime}_{j})\mathbf{u}^{\prime T}_{j}D\mathbf{F}^{\perp}(\mathbf{u}_{j}). |  |

If { 𝐮 j } \{\mathbf{u}_{j}\} is uniformly bounded in H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}), we know that a certain subsequence (not relabelled) of { 𝐮 j } \{\mathbf{u}_{j}\} converges weakly to some 𝐮 \mathbf{u} in H 2 ​ ( [0, 1], ℝ 2) H^{2}([0,1];\mathbb{R}^{2}). Set

 | 𝐆 ≡ ( 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐮 ′) ​ 𝐅 ⟂ ​ ( 𝐮), 𝐇 ≡ ( 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐮 ′) ​ 𝐮 ′ T ​ D ​ 𝐅 ⟂ ​ ( 𝐮). \mathbf{G}\equiv(\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{u}^{\prime})\mathbf{F}^{\perp}(\mathbf{u}),\quad\mathbf{H}\equiv(\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{u}^{\prime})\mathbf{u}^{\prime T}D\mathbf{F}^{\perp}(\mathbf{u}). |  |

If we put

 | 𝐯 j = E 0 ′ ​ ( 𝐮 j), 𝐯 = E 0 ′ ​ ( 𝐮), \mathbf{v}_{j}=E^{\prime}_{0}(\mathbf{u}_{j}),\quad\mathbf{v}=E^{\prime}_{0}(\mathbf{u}), |  |

then ( 5.7) implies

 | ∫ 0 1 [𝐯 j ′′ ⋅ 𝐔 ′′ + ( 𝐯 j ′ + 𝐆 j) ⋅ 𝐔 ′ + ( 𝐯 j + 𝐇 j) ⋅ 𝐔] ​ 𝑑 t = 0, \displaystyle\int_{0}^{1}[\mathbf{v}^{\prime\prime}_{j}\cdot\mathbf{U}^{\prime\prime}+(\mathbf{v}^{\prime}_{j}+\mathbf{G}_{j})\cdot\mathbf{U}^{\prime}+(\mathbf{v}_{j}+\mathbf{H}_{j})\cdot\mathbf{U}]\,dt=0, |  |

 | ∫ 0 1 [𝐯 ′′ ⋅ 𝐔 ′′ + ( 𝐯 ′ + 𝐆) ⋅ 𝐔 ′ + ( 𝐯 + 𝐇) ⋅ 𝐔] ​ 𝑑 t = 0, \displaystyle\int_{0}^{1}[\mathbf{v}^{\prime\prime}\cdot\mathbf{U}^{\prime\prime}+(\mathbf{v}^{\prime}+\mathbf{G})\cdot\mathbf{U}^{\prime}+(\mathbf{v}+\mathbf{H})\cdot\mathbf{U}]\,dt=0, |  |

for every

 | 𝐔 ∈ H O 2 ​ ( [0, 1], ℝ 2). \mathbf{U}\in H^{2}_{O}([0,1];\mathbb{R}^{2}). |  |

By substracting one from the other

 | ∫ 0 1 [( 𝐯 j ′′ − 𝐯 ′′) ⋅ 𝐕 ′′ + ( 𝐯 j ′ − 𝐯 ′ + 𝐆 j − 𝐆) ⋅ 𝐕 ′ + ( 𝐯 j − 𝐯 + 𝐇 j − 𝐇) ⋅ 𝐕] ​ 𝑑 t = 0 \int_{0}^{1}[(\mathbf{v}^{\prime\prime}_{j}-\mathbf{v}^{\prime\prime})\cdot\mathbf{V}^{\prime\prime}+(\mathbf{v}^{\prime}_{j}-\mathbf{v}^{\prime}+\mathbf{G}_{j}-\mathbf{G})\cdot\mathbf{V}^{\prime}+(\mathbf{v}_{j}-\mathbf{v}+\mathbf{H}_{j}-\mathbf{H})\cdot\mathbf{V}]\,dt=0 |  |

for every

 | 𝐔 ∈ H O 2 ​ ( [0, 1], ℝ 2). \mathbf{U}\in H^{2}_{O}([0,1];\mathbb{R}^{2}). |  |

We can take 𝐔 = 𝐯 j − 𝐯 \mathbf{U}=\mathbf{v}_{j}-\mathbf{v} to find that

 | ∫ 0 1 [| 𝐯 j ′′ − 𝐯 ′′ | 2 + ( 𝐯 j ′ − 𝐯 ′ + 𝐆 j − 𝐆) ⋅ ( 𝐯 j ′ − 𝐯 ′) + ( 𝐯 j − 𝐯 + 𝐇 j − 𝐇) ⋅ ( 𝐯 j − 𝐯)] ​ 𝑑 t = 0. \int_{0}^{1}[|\mathbf{v}^{\prime\prime}_{j}-\mathbf{v}^{\prime\prime}|^{2}+(\mathbf{v}^{\prime}_{j}-\mathbf{v}^{\prime}+\mathbf{G}_{j}-\mathbf{G})\cdot(\mathbf{v}^{\prime}_{j}-\mathbf{v}^{\prime})+(\mathbf{v}_{j}-\mathbf{v}+\mathbf{H}_{j}-\mathbf{H})\cdot(\mathbf{v}_{j}-\mathbf{v})]\,dt=0. |  |

This equality can be reorganized as

 | ∥ 𝐯 j − 𝐯 ∥ H 2 ​ ( [0, 1], ℝ 2) 2 = − ∫ 0 1 [( 𝐆 j − 𝐆) ⋅ ( 𝐯 j ′ − 𝐯 ′) + ( 𝐇 j − 𝐇) ⋅ ( 𝐯 j − 𝐯)] d t, \|\mathbf{v}_{j}-\mathbf{v}\|^{2}_{H^{2}([0,1];\mathbb{R}^{2})}=-\int_{0}^{1}[(\mathbf{G}_{j}-\mathbf{G})\cdot(\mathbf{v}^{\prime}_{j}-\mathbf{v}^{\prime})+(\mathbf{H}_{j}-\mathbf{H})\cdot(\mathbf{v}_{j}-\mathbf{v})]\,dt, |  |

Hence, by the standard Hölder inequality for integrals, we can also have

(5.11) |  | ‖ 𝐯 j − 𝐯 ‖ H 2 ​ ( [0, 1], ℝ 2) ≤ ‖ 𝐆 j − 𝐆 ‖ L 2 ​ ( [0, 1], ℝ 2) + ‖ 𝐇 j − 𝐇 ‖ L 2 ​ ( [0, 1], ℝ 2). \|\mathbf{v}_{j}-\mathbf{v}\|_{H^{2}([0,1];\mathbb{R}^{2})}\leq\|\mathbf{G}_{j}-\mathbf{G}\|_{L^{2}([0,1];\mathbb{R}^{2})}+\|\mathbf{H}_{j}-\mathbf{H}\|_{L^{2}([0,1];\mathbb{R}^{2})}. |  |

Since the weak convergence of 𝐮 j \mathbf{u}_{j} to 𝐮 \mathbf{u} in H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}) implies weak convergence up to second derivatives, by the classical Rellich–Kondrachov Theorem, which implies that the injection W 2, p ⊂ W 1, p W^{2,p}\subset W^{1,p} is always compact (see Theorem 9.16 in [7] for the case with first derivatives W 1, p ⊂ L p W^{1,p}\subset L^{p}), we conclude the convergences

 | 𝐆 j → 𝐆, 𝐇 j → 𝐇 \mathbf{G}_{j}\to\mathbf{G},\quad\mathbf{H}_{j}\to\mathbf{H} |  |

strongly in L 2 ​ ( [0, 1], ℝ 2) L^{2}([0,1];\mathbb{R}^{2}). The proof is then a direct consequence of ( 5.11). ∎

As a direct consequence of Lemma 5.6, we have:

###### Corollary 5.7.

The map

 | E 0 ′: H O 2 ​ ( [0, 1], ℝ 2) → H O 2 ​ ( [0, 1], ℝ 2) E^{\prime}_{0}:H^{2}_{O}([0,1];\mathbb{R}^{2})\to H^{2}_{O}([0,1];\mathbb{R}^{2}) |  |

is compact.

This compactness property is the only reason why the functional E 0 E_{0} has to be perturbed by a norm involving up to second derivatives. If we had just perturbed E 0 E_{0} up to first derivatives, we would not have the strong convergence of the vector fields 𝐆 j \mathbf{G}_{j} and 𝐇 j \mathbf{H}_{j} to 𝐆 \mathbf{G} and 𝐇 \mathbf{H}, respectively, in the proof of Lemma 5.6.

#### 5.3.2. Compactness of E 0 ′′ ​ ( 𝐮) E^{\prime\prime}_{0}(\mathbf{u})

Another main necessary ingredient is the compactness of the linear operator

 | E 0 ′′ ​ ( 𝐮): H O 2 ​ ( [0, 1], ℝ 2) → H O 2 ​ ( [0, 1], ℝ 2) E^{\prime\prime}_{0}(\mathbf{u}):H^{2}_{O}([0,1];\mathbb{R}^{2})\to H^{2}_{O}([0,1];\mathbb{R}^{2}) |  |

for each fixed 𝐮 \mathbf{u}.

The form ( 5.10) is especially suited to show the compactness we are after. Set

 | 𝐅 ¯ = ( 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐮 ′) ​ ∇ 2 𝐅 ⟂ ​ ( 𝐮): 𝐮 ′ + ∇ 𝐅 ⟂ ​ ( 𝐮) ​ 𝐮 ′ ⊗ ∇ 𝐅 ⟂ ​ ( 𝐮) ​ 𝐮 ′, 𝐆 ¯ = ∇ 𝐅 ⟂ ​ ( 𝐮) + 𝐅 ⟂ ​ ( 𝐮) ⊗ ∇ 𝐅 ⟂ ​ ( 𝐮) ​ 𝐮 ′, 𝐇 ¯ = ∇ 𝐅 ⟂ ​ ( 𝐮) + ∇ 𝐅 ⟂ ​ ( 𝐮) ​ 𝐮 ′ ⊗ 𝐅 ⟂ ​ ( 𝐮), 𝐉 ¯ = 𝐅 ⟂ ​ ( 𝐮) ⊗ 𝐅 ⟂ ​ ( 𝐮). \begin{array}[]{rl}\overline{\mathbf{F}}=&(\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{u}^{\prime})\nabla^{2}\mathbf{F}^{\perp}(\mathbf{u}):\mathbf{u}^{\prime}+\nabla\mathbf{F}^{\perp}(\mathbf{u})\mathbf{u}^{\prime}\otimes\nabla\mathbf{F}^{\perp}(\mathbf{u})\mathbf{u}^{\prime},\\ \overline{\mathbf{G}}=&\nabla\mathbf{F}^{\perp}(\mathbf{u})+\mathbf{F}^{\perp}(\mathbf{u})\otimes\nabla\mathbf{F}^{\perp}(\mathbf{u})\mathbf{u}^{\prime},\\ \overline{\mathbf{H}}=&\nabla\mathbf{F}^{\perp}(\mathbf{u})+\nabla\mathbf{F}^{\perp}(\mathbf{u})\mathbf{u}^{\prime}\otimes\mathbf{F}^{\perp}(\mathbf{u}),\\ \overline{\mathbf{J}}=&\mathbf{F}^{\perp}(\mathbf{u})\otimes\mathbf{F}^{\perp}(\mathbf{u}).\end{array} |  |

This choice is dictated so that

 | ⟨ E 0 ′′ ​ ( 𝐮), ( 𝐔, 𝐔 ¯) ⟩ = ∫ 0 1 [𝐅 ¯ ​ ( 𝐔, 𝐔 ¯) + 𝐆 ¯ ​ ( 𝐔 ′, 𝐔 ¯) + 𝐇 ¯ ​ ( 𝐔, 𝐔 ¯ ′) + 𝐉 ¯ ​ ( 𝐔 ′, 𝐔 ¯ ′)] ​ 𝑑 t. \langle E^{\prime\prime}_{0}(\mathbf{u}),(\mathbf{U},\overline{\mathbf{U}})\rangle=\int_{0}^{1}[\overline{\mathbf{F}}(\mathbf{U},\overline{\mathbf{U}})+\overline{\mathbf{G}}(\mathbf{U}^{\prime},\overline{\mathbf{U}})+\overline{\mathbf{H}}(\mathbf{U},\overline{\mathbf{U}}^{\prime})+\overline{\mathbf{J}}(\mathbf{U}^{\prime},\overline{\mathbf{U}}^{\prime})]\,dt. |  |

Exactly as in Lemma 5.6, one can show the following.

###### Lemma 5.8.

For fixed, given

 | 𝐮 ∈ H O 2 ​ ( [0, 1], ℝ 2), \mathbf{u}\in H^{2}_{O}([0,1];\mathbb{R}^{2}), |  |

the operator

 | 𝐔 ↦ 𝐕 = E 0 ′′ ​ ( 𝐮) ​ 𝐔 \mathbf{U}\mapsto\mathbf{V}=E^{\prime\prime}_{0}(\mathbf{u})\mathbf{U} |  |

is self-adjoint and compact.

###### Proof.

Assume { 𝐔 j } \{\mathbf{U}_{j}\} is bounded in H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}). In particular, and for reasons already pointed out earlier, 𝐔 j ′ → 𝐔 ′ \mathbf{U}^{\prime}_{j}\to\mathbf{U}^{\prime} uniformly for some

 | 𝐔 ∈ H O 2 ​ ( [0, 1], ℝ 2). \mathbf{U}\in H^{2}_{O}([0,1];\mathbb{R}^{2}). |  |

Let 𝐕 j \mathbf{V}_{j} and 𝐕 \mathbf{V} determined through ( 5.10), respectively. Then

 | ‖ 𝐕 j − 𝐕 ‖ 2 = ⟨ E 0 ′′ ​ ( 𝐮) ​ ( 𝐔 j − 𝐔), 𝐕 j − 𝐕 ⟩, \|\mathbf{V}_{j}-\mathbf{V}\|^{2}=\langle E^{\prime\prime}_{0}(\mathbf{u})(\mathbf{U}_{j}-\mathbf{U}),\mathbf{V}_{j}-\mathbf{V}\rangle, |  |

and

 | ‖ 𝐕 j − 𝐕 ‖ ≤ ‖ E 0 ′′ ​ ( 𝐮) ​ ( 𝐔 j − 𝐔) ‖. \|\mathbf{V}_{j}-\mathbf{V}\|\leq\|E^{\prime\prime}_{0}(\mathbf{u})(\mathbf{U}_{j}-\mathbf{U})\|. |  |

The key point is to realize, in the formulas above, that in E 0 ′′ ​ ( 𝐮) ​ ( 𝐔 j − 𝐔) E^{\prime\prime}_{0}(\mathbf{u})(\mathbf{U}_{j}-\mathbf{U}) only up to first derivatives of the differences 𝐔 j − 𝐔 \mathbf{U}_{j}-\mathbf{U} occur, and these converge strongly to zero. Hence

 | ‖ 𝐕 j − 𝐕 ‖ → 0. \|\mathbf{V}_{j}-\mathbf{V}\|\to 0. |  |

∎

### 5.4. What we have so far

At this stage, we have covered all ingredients to have the following statements. Recall the form of E 0 E_{0} in ( 5.1).

###### Theorem 5.9.

There is 𝐯 0 ∈ 𝕆 1 \mathbf{v}_{0}\in\mathbb{O}_{1} such that the perturbed functional

(5.12) |  | E ϵ ​ ( 𝐮) = E 0 ​ ( 𝐮) + ϵ 2 ​ ‖ 𝐮 − 𝐯 0 ‖ 2 E_{\epsilon}(\mathbf{u})=E_{0}(\mathbf{u})+\frac{\epsilon}{2}\|\mathbf{u}-\mathbf{v}_{0}\|^{2} |  |

is a Morse functional. The auxiliary path 𝐯 0 \mathbf{v}_{0} can be chosen as regular as it may be necessary.

After our work in the two preceding subsections, this result is a direct consequence of Theorem 3.4. There is nothing to be added.

We are also entitled to apply Theorem 5.1 to our particular situation and conclude the following.

###### Theorem 5.10.

Let ℙ \mathbb{P} be any arbitrary, finite subset of components of { E 0 = 0 } \{E_{0}=0\} in 𝕆 \mathbb{O}, and let M c ​ r ​ i, ϵ, a M_{cri,\epsilon,a} stand for the number of critical paths of E ϵ E_{\epsilon} in { E ϵ ≥ a } ∩ 𝕆 \{E_{\epsilon}\geq a\}\cap\mathbb{O}. Then

(5.13) |  | #⁡ ( ℙ) ≤ 1 + lim a → 0 lim ϵ → 0 M c ​ r ​ i, ϵ, a. \#(\mathbb{P})\leq 1+\lim_{a\to 0}\lim_{\epsilon\to 0}M_{cri,\epsilon,a}. |  |

The combination of Lemmas 5.3, Proposition 5.2, and Lemma 5.4, together with Theorem 5.9, imply, after Theorem 5.1, that for every finite subset ℙ \mathbb{P} of limit cycles of our initial planar, polynomial differential system ( 1.1), we have the upper bound ( 5.13). Our final fundamental job is to show that there is an upper bound M c ​ r ​ i M_{cri} for the right-hand side of ( 5.13), independent of a a and ϵ \epsilon, in terms of the degree n n of our initial differential system ( 1.1).

### 5.5. The equation for critical closed paths

The application of Theorem 4.5 to our situation where

 | F ⁡ ( t, 𝐮, 𝐳, 𝐙) = \displaystyle F(t,\mathbf{u},\mathbf{z},\mathbf{Z})= | 1 2 ​ ( 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐳) 2 + ϵ 2 ​ ( | 𝐙 | 2 + | 𝐳 | 2 + | 𝐮 | 2) \displaystyle\frac{1}{2}(\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{z})^{2}+\frac{\epsilon}{2}(|\mathbf{Z}|^{2}+|\mathbf{z}|^{2}+|\mathbf{u}|^{2}) |  |

 |  | + 𝐮 ⋅ 𝐯 0 ( t) + 𝐳 ⋅ 𝐯 0 ′ ( t) + 𝐙 ⋅ 𝐯 0 ′′ ( t) \displaystyle+\mathbf{u}\cdot\mathbf{v}_{0}(t)+\mathbf{z}\cdot\mathbf{v}^{\prime}_{0}(t)+\mathbf{Z}\cdot\mathbf{v}^{\prime\prime}_{0}(t) |  |

is our first key step. Note that we have dropped out the constant term

 | 1 2 ​ ϵ ​ ‖ 𝐯 0 ‖ 2 \frac{1}{2\epsilon}\|\mathbf{v}_{0}\|^{2} |  |

from E ϵ E_{\epsilon} as it does not play a role in what follows, and that for aesthetic purposes we have changed 𝐯 0 \mathbf{v}_{0} to − 𝐯 0 -\mathbf{v}_{0}. The partial derivatives required in the statement of that theorem are

 | F 𝐙 = ϵ ​ 𝐙 + 𝐯 0 ′′ ​ ( t), \displaystyle F_{\mathbf{Z}}=\epsilon\mathbf{Z}+\mathbf{v}^{\prime\prime}_{0}(t), |  |

 | F 𝐳 = ( 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐳) ​ 𝐅 ⟂ ​ ( 𝐮) + ϵ ​ 𝐳 + 𝐯 0 ′ ​ ( t), \displaystyle F_{\mathbf{z}}=(\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{z})\,\mathbf{F}^{\perp}(\mathbf{u})+\epsilon\mathbf{z}+\mathbf{v}^{\prime}_{0}(t), |  |

 | F 𝐮 = ( 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐳) ​ D ​ 𝐅 ⟂ ​ ( 𝐮) ​ 𝐳 + ϵ ​ 𝐮 + 𝐯 0 ​ ( t). \displaystyle F_{\mathbf{u}}=(\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{z})\,D\mathbf{F}^{\perp}(\mathbf{u})\mathbf{z}+\epsilon\mathbf{u}+\mathbf{v}_{0}(t). |  |

Equation ( 4.10) for critical closed paths in H O 2 ​ ( [0, 1], ℝ 2) H^{2}_{O}([0,1];\mathbb{R}^{2}) for E ϵ E_{\epsilon} coming from Theorem 4.5 involves the combination ( 4.9) which in our case is

(5.14) |  | d d ​ t ​ ( ϵ ​ 𝐮 ϵ ′′ ​ ( t) + 𝐯 0 ′′ ​ ( t)) − ( 𝐅 ⟂ ​ ( 𝐮 ϵ ​ ( t)) ⋅ 𝐮 ϵ ′ ​ ( t)) ​ 𝐅 ⟂ ​ ( 𝐮 ϵ ​ ( t)) − ϵ ​ 𝐮 ϵ ′ ​ ( t) − 𝐯 0 ′ ​ ( t), \frac{d}{dt}(\epsilon\mathbf{u}^{\prime\prime}_{\epsilon}(t)+\mathbf{v}^{\prime\prime}_{0}(t))-(\mathbf{F}^{\perp}(\mathbf{u}_{\epsilon}(t))\cdot\mathbf{u}^{\prime}_{\epsilon}(t))\,\mathbf{F}^{\perp}(\mathbf{u}_{\epsilon}(t))-\epsilon\mathbf{u}^{\prime}_{\epsilon}(t)-\mathbf{v}^{\prime}_{0}(t), |  |

which must be an absolutely continuous function in [0, 1] [0,1]. Its almost everywhere derivative ought to be, according to system ( 4.10),

(5.15) |  | − ( 𝐅 ⟂ ​ ( 𝐮 ϵ ​ ( t) ⋅ 𝐮 ϵ ′ ​ ( t)) ​ D ​ 𝐅 ⟂ ​ ( 𝐮 ϵ ​ ( t)) ​ 𝐮 ϵ ′ ​ ( t) − ϵ ​ 𝐮 ϵ ​ ( t) − 𝐯 0 ​ ( t) CLOSE. -(\mathbf{F}^{\perp}(\mathbf{u}_{\epsilon}(t)\cdot\mathbf{u}^{\prime}_{\epsilon}(t))\,D\mathbf{F}^{\perp}(\mathbf{u}_{\epsilon}(t))\mathbf{u}^{\prime}_{\epsilon}(t)-\epsilon\mathbf{u}_{\epsilon}(t)-\mathbf{v}_{0}(t). |  |

Here

 | 𝐮 ϵ ∈ H O 2 ​ ( [0, 1], ℝ 2) \mathbf{u}_{\epsilon}\in H^{2}_{O}([0,1];\mathbb{R}^{2}) |  |

is an arbitrary critical closed path of E ϵ E_{\epsilon}. In addition, from ( 4.11) we have

(5.16) |  | [ϵ ​ 𝐮 ϵ ′′ ​ ( t) + 𝐯 0 ′′ ​ ( t)] t = 0 = 𝟎. [\epsilon\mathbf{u}^{\prime\prime}_{\epsilon}(t)+\mathbf{v}^{\prime\prime}_{0}(t)]_{t=0}=\mathbf{0}. |  |

We need to examine these conditions carefully.

It is also important to stress how this result ensures much more regularity for those critical closed paths precisely because they are critical for a certain functional. Even though paths in our ambient space are just in H 2 ​ ( [0, 1], ℝ 2) H^{2}([0,1];\mathbb{R}^{2}), critical closed paths of our family of functionals are much more regular. By Theorem 4.5, the expression in ( 5.14) is absolutely continuous. Since the last three terms of ( 5.14) and 𝐯 0 ′′′ \mathbf{v}^{\prime\prime\prime}_{0} are continuous, we can conclude that 𝐮 ϵ \mathbf{u}_{\epsilon} is 𝒞 3 \mathcal{C}^{3} in [0, 1] [0,1]. Moreover, due to the fact that the derivative of ( 5.14) is equal to ( 5.15), again by Theorem 4.5, it follows that 𝐮 ϵ \mathbf{u}_{\epsilon} is even 𝒞 4 \mathcal{C}^{4} in [0, 1] [0,1] because all terms in ( 5.14), when differentiated with respect to t t, are continuous except possibly the first one 𝐮 ϵ ′′′ ​ ( t) \mathbf{u}^{\prime\prime\prime}_{\epsilon}(t), and such a derivative is equal to ( 5.15) which is continuous. Note how condition ( 5.16) is redundant with the above information.

###### Proposition 5.11.

Critical closed paths

 | 𝐮 ϵ ∈ H O 2 ​ ( [0, 1], ℝ 2) \mathbf{u}_{\epsilon}\in H^{2}_{O}([0,1];\mathbb{R}^{2}) |  |

of functional E ϵ E_{\epsilon} are 𝒞 ∞ \mathcal{C}^{\infty} in [0, 1] [0,1], and are solutions of the system

(5.17) |  | ϵ ⁡ ( 𝐮 ϵ ′′′′ − 𝐮 ϵ ′′ + 𝐮 ϵ) − d d ​ t ​ [( 𝐅 ⟂ ​ ( 𝐮 ϵ) ⋅ 𝐮 ϵ ′) ​ 𝐅 ⟂ ​ ( 𝐮 ϵ)] + ( 𝐅 ⟂ ​ ( 𝐮 ϵ) ⋅ 𝐮 ϵ ′) ​ ( 𝐮 ϵ ′) T ​ D ​ 𝐅 ⟂ ​ ( 𝐮 ϵ) \displaystyle\epsilon(\mathbf{u}^{\prime\prime\prime\prime}_{\epsilon}-\mathbf{u}^{\prime\prime}_{\epsilon}+\mathbf{u}_{\epsilon})-\frac{d}{dt}[(\mathbf{F}^{\perp}(\mathbf{u}_{\epsilon})\cdot\mathbf{u}^{\prime}_{\epsilon})\,\mathbf{F}^{\perp}(\mathbf{u}_{\epsilon})]+(\mathbf{F}^{\perp}(\mathbf{u}_{\epsilon})\cdot\mathbf{u}^{\prime}_{\epsilon})\,(\mathbf{u}^{\prime}_{\epsilon})^{T}D\mathbf{F}^{\perp}(\mathbf{u}_{\epsilon}) |  |

 | = − 𝐯 0 ′′′′ + 𝐯 0 ′′ − 𝐯 0 \displaystyle=-\mathbf{v}^{\prime\prime\prime\prime}_{0}+\mathbf{v}^{\prime\prime}_{0}-\mathbf{v}_{0} |  |

in the interval [0, 1] [0,1].

###### Proof.

Regularity conditions for 𝐮 ϵ \mathbf{u}_{\epsilon} have been discussed in the paragraph prior to the statement of the proposition. Equation ( 5.17) is a consequence, according to equation ( 4.10), of expressing the equality of the derivative of ( 5.14) with ( 5.15). A typical bootstrap argument yields the regularity claimed in the statement. ∎

System ( 5.17) is a key point for counting the critical closed paths of the functional E ϵ E_{\epsilon}. We are facing a singularly-perturbed, fourth-order ODE system ( 5.17) with periodic (unknown) boundary conditions. Our plan to count, and eventually find an upper bound for, the number of branches of solutions of ( 5.17) proceeds in two steps:

1. (1)

for a fixed such branch, understand its asymptotic behavior as ϵ ↘ 0 \epsilon\searrow 0, to count how many such different asymptotic behaviors there might be; and

2. (2)

for a fixed such asymptotic behavior, decide how many branches may converge to it.

To deal appropriately with this second point, we stick to the discussion in Section 4.4, and apply it to our particular situation here. The application of those ideas to our case leads to the following statements.

###### Proposition 5.12.

Critical closed paths

 | 𝐮 ϵ ∈ H 𝐲, 2 ( 0, 1]; ℝ 2) \mathbf{u}_{\epsilon}\in H^{2}_{\mathbf{y},}(0,1];\mathbb{R}^{2}) |  |

of functional E ϵ E_{\epsilon} are 𝒞 2 \mathcal{C}^{2} in [0, 1] [0,1], 𝒞 ∞ \mathcal{C}^{\infty} in ( 0, 1) (0,1), and are solutions of the fourth-order differential system

(5.18) |  | ϵ ⁡ ( 𝐮 ϵ ′′′′ − 𝐮 ϵ ′′ + 𝐮 ϵ) − d d ​ t ​ [( 𝐅 ⟂ ​ ( 𝐮 ϵ) ⋅ 𝐮 ϵ ′) ​ 𝐅 ⟂ ​ ( 𝐮 ϵ)] + ( 𝐅 ⟂ ​ ( 𝐮 ϵ) ⋅ 𝐮 ϵ ′) ​ ( 𝐮 ϵ ′) T ​ D ​ 𝐅 ⟂ ​ ( 𝐮 ϵ) \displaystyle\epsilon(\mathbf{u}^{\prime\prime\prime\prime}_{\epsilon}-\mathbf{u}^{\prime\prime}_{\epsilon}+\mathbf{u}_{\epsilon})-\frac{d}{dt}[(\mathbf{F}^{\perp}(\mathbf{u}_{\epsilon})\cdot\mathbf{u}^{\prime}_{\epsilon})\,\mathbf{F}^{\perp}(\mathbf{u}_{\epsilon})]+(\mathbf{F}^{\perp}(\mathbf{u}_{\epsilon})\cdot\mathbf{u}^{\prime}_{\epsilon})\,(\mathbf{u}^{\prime}_{\epsilon})^{T}D\mathbf{F}^{\perp}(\mathbf{u}_{\epsilon}) |  |

 | = − 𝐯 0 ′′′′ + 𝐯 0 ′′ − 𝐯 0 \displaystyle=-\mathbf{v}^{\prime\prime\prime\prime}_{0}+\mathbf{v}^{\prime\prime}_{0}-\mathbf{v}_{0} |  |

in the interval ( 0, 1) (0,1).

Recall that

 | H 𝐲, 2 ( [0, 1]; ℝ 2) = { 𝐯 ∈ H 2 ( [0, 1]; ℝ 2): 𝐯 ( 0) = 𝐯 ( 1) = 𝐲, 𝐯 ′ ( 0) = 𝐯 ′ ( 1) }. H^{2}_{\mathbf{y},}([0,1];\mathbb{R}^{2})=\{\mathbf{v}\in H^{2}([0,1];\mathbb{R}^{2}):\mathbf{v}(0)=\mathbf{v}(1)=\mathbf{y},\mathbf{v}^{\prime}(0)=\mathbf{v}^{\prime}(1)\}. |  |

We can also perform the same analysis in the more restrictive linear manifold

 | H 𝐲, 𝐳 2 ( [0, 1]; ℝ 2) = { 𝐯 ∈ H 2 ( [0, 1]; ℝ 2): 𝐯 ( 0) = 𝐯 ( 1) = 𝐲, 𝐯 ′ ( 0) = 𝐯 ′ ( 1) = 𝐳 } H^{2}_{\mathbf{y},\mathbf{z}}([0,1];\mathbb{R}^{2})=\{\mathbf{v}\in H^{2}([0,1];\mathbb{R}^{2}):\mathbf{v}(0)=\mathbf{v}(1)=\mathbf{y},\mathbf{v}^{\prime}(0)=\mathbf{v}^{\prime}(1)=\mathbf{z}\} |  |

for fixed vectors 𝐲 \mathbf{y} and 𝐳 \mathbf{z}, and find the parallel statements that follow, whose proofs can be very easily adapted from the previous ones. Note how, as we place more demands on feasible paths, optimality turns back less regularity through end-points.

###### Proposition 5.13.

Critical closed paths

 | 𝐮 ϵ ∈ H 𝐲, 𝐳 2 ​ ( [0, 1], ℝ 2) \mathbf{u}_{\epsilon}\in H^{2}_{\mathbf{y},\mathbf{z}}([0,1];\mathbb{R}^{2}) |  |

of functional E ϵ E_{\epsilon} are 𝒞 1 \mathcal{C}^{1} in [0, 1] [0,1], 𝒞 ∞ \mathcal{C}^{\infty} in ( 0, 1) (0,1), and are solutions of the fourth-order differential system

(5.19) |  | ϵ ⁡ ( 𝐮 ϵ ′′′′ − 𝐮 ϵ ′′ + 𝐮 ϵ) − d d ​ t ​ [( 𝐅 ⟂ ​ ( 𝐮 ϵ) ⋅ 𝐮 ϵ ′) ​ 𝐅 ⟂ ​ ( 𝐮 ϵ)] + ( 𝐅 ⟂ ​ ( 𝐮 ϵ) ⋅ 𝐮 ϵ ′) ​ ( 𝐮 ϵ ′) T ​ D ​ 𝐅 ⟂ ​ ( 𝐮 ϵ) \displaystyle\epsilon(\mathbf{u}^{\prime\prime\prime\prime}_{\epsilon}-\mathbf{u}^{\prime\prime}_{\epsilon}+\mathbf{u}_{\epsilon})-\frac{d}{dt}[(\mathbf{F}^{\perp}(\mathbf{u}_{\epsilon})\cdot\mathbf{u}^{\prime}_{\epsilon})\,\mathbf{F}^{\perp}(\mathbf{u}_{\epsilon})]+(\mathbf{F}^{\perp}(\mathbf{u}_{\epsilon})\cdot\mathbf{u}^{\prime}_{\epsilon})\,(\mathbf{u}^{\prime}_{\epsilon})^{T}D\mathbf{F}^{\perp}(\mathbf{u}_{\epsilon}) |  |

 | = − 𝐯 0 ′′′′ + 𝐯 0 ′′ − 𝐯 0 \displaystyle=-\mathbf{v}^{\prime\prime\prime\prime}_{0}+\mathbf{v}^{\prime\prime}_{0}-\mathbf{v}_{0} |  |

in the interval ( 0, 1) (0,1).

As in Definition 4.4, we introduce the following.

###### Definition 5.1.

The mapping

 | 𝐮 ϵ ​ ( t, 𝐩 0, 𝐩 1, 𝐩 2, 𝐩 3): [0, 1] × ℝ 2 × ℝ 2 × ℝ 2 × ℝ 2 → ℝ 2 \mathbf{u}_{\epsilon}(t;\mathbf{p}_{0},\mathbf{p}_{1},\mathbf{p}_{2},\mathbf{p}_{3}):[0,1]\times\mathbb{R}^{2}\times\mathbb{R}^{2}\times\mathbb{R}^{2}\times\mathbb{R}^{2}\to\mathbb{R}^{2} |  |

will designate the solution mapping for problem ( 5.19) under initial conditions

 | 𝐮 ϵ OPEN i) ( 0; 𝐩 0, 𝐩 1, 𝐩 2, 𝐩 3) = 𝐩 i, i = 0, 1, 2, 3. \mathbf{u}^{i)}_{\epsilon}(0;\mathbf{p}_{0},\mathbf{p}_{1},\mathbf{p}_{2},\mathbf{p}_{3})=\mathbf{p}_{i},\quad i=0,1,2,3. |  |

According to the shooting method in Section 4.6, and in particular as a consequence of Corollary 4.14, the following definition is legitimate.

###### Definition 5.2.

Let

 | ( 𝐩 0, 𝐪 0) ∈ ℝ 2 × ℝ 2 (\mathbf{p}_{0},\mathbf{q}_{0})\in\mathbb{R}^{2}\times\mathbb{R}^{2} |  |

be a given pair. For ( 𝐩, 𝐪) (\mathbf{p},\mathbf{q}) in a neighborhood of ( 𝐩 0, 𝐪 0) (\mathbf{p}_{0},\mathbf{q}_{0}), 𝐮 ⁡ ( t, 𝐩, 𝐪, ϵ) \mathbf{u}(t;\mathbf{p},\mathbf{q},\epsilon) will designate the unique periodic solution of system ( 5.19) such that

 | 𝐮 ⁡ ( 0, 𝐩, 𝐪, ϵ) = 𝐮 ⁡ ( 1, 𝐩, 𝐪, ϵ) = 𝐩, 𝐮 ′ ​ ( 0, 𝐩, 𝐪, ϵ) = 𝐮 ′ ​ ( 1, 𝐩, 𝐪, ϵ) = 𝐪. \mathbf{u}(0;\mathbf{p},\mathbf{q},\epsilon)=\mathbf{u}(1;\mathbf{p},\mathbf{q},\epsilon)=\mathbf{p},\quad\mathbf{u}^{\prime}(0;\mathbf{p},\mathbf{q},\epsilon)=\mathbf{u}^{\prime}(1;\mathbf{p},\mathbf{q},\epsilon)=\mathbf{q}. |  |

To check that this definition is meaningful, after the above-mentioned corollary, simply note that the perturbed integrand

 | F ⁡ ( t, 𝐮, 𝐳, 𝐙) = \displaystyle F(t,\mathbf{u},\mathbf{z},\mathbf{Z})= | 1 2 ​ ( 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐳) 2 + ϵ 2 ​ ( | 𝐙 | 2 + | 𝐳 | 2 + | 𝐮 | 2) \displaystyle\frac{1}{2}(\mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{z})^{2}+\frac{\epsilon}{2}(|\mathbf{Z}|^{2}+|\mathbf{z}|^{2}+|\mathbf{u}|^{2}) |  |

 |  | + 𝐮 ⋅ 𝐯 0 ( t) + 𝐳 ⋅ 𝐯 0 ′ ( t) + 𝐙 ⋅ 𝐯 0 ′′ ( t) \displaystyle+\mathbf{u}\cdot\mathbf{v}_{0}(t)+\mathbf{z}\cdot\mathbf{v}^{\prime}_{0}(t)+\mathbf{Z}\cdot\mathbf{v}^{\prime\prime}_{0}(t) |  |

for ϵ \epsilon fixed, is analytic in all its variables provided the auxiliary path 𝐯 0 ​ ( t) \mathbf{v}_{0}(t) can be chosen analytic as well. This is no restriction, as we have remarked in various occasions that there is plenty of choice to select 𝐯 0 \mathbf{v}_{0} from: it can be chosen analytic, and uniformly bounded.

### 5.6. Asymptotic behavior

For the sake of transparency, and to facilitate a few interesting computations, we recast system ( 5.17) or ( 5.19) in its two components

 | ( Z ​ Q) ′ + Z ⁡ ( − Q x ​ x ′ + P x ​ y ′) = − ϵ ​ α 1, ( Z ​ P) ′ + Z ⁡ ( Q y ​ x ′ − P y ​ y ′) = ϵ ​ α 2. \begin{array}[]{r}(ZQ)^{\prime}+Z(-Q_{x}x^{\prime}+P_{x}y^{\prime})=-\epsilon\alpha_{1},\\ (ZP)^{\prime}+Z(Q_{y}x^{\prime}-P_{y}y^{\prime})=\epsilon\alpha_{2}.\end{array} |  |

where

 | 𝐅 = ( P, Q), 𝐮 ϵ = ( x, y), 𝐯 0 = ( X, Y) \displaystyle\mathbf{F}=(P,Q),\quad\mathbf{u}_{\epsilon}=(x,y),\quad\mathbf{v}_{0}=(X,Y) |  |

 | Z ≡ 𝐅 ⟂ ​ ( 𝐮 ϵ) ⋅ 𝐮 ϵ ′ = P ⁡ ( x, y) ​ y ′ − Q ⁡ ( x, y) ​ x ′, \displaystyle Z\equiv\mathbf{F}^{\perp}(\mathbf{u}_{\epsilon})\cdot\mathbf{u}^{\prime}_{\epsilon}=P(x,y)y^{\prime}-Q(x,y)x^{\prime}, |  |

 | W ≡ 𝐅 ⁡ ( 𝐮 ϵ) ⋅ 𝐮 ϵ ′ = P ⁡ ( x, y) ​ x ′ + Q ⁡ ( x, y) ​ y ′, \displaystyle W\equiv\mathbf{F}(\mathbf{u}_{\epsilon})\cdot\mathbf{u}^{\prime}_{\epsilon}=P(x,y)x^{\prime}+Q(x,y)y^{\prime}, |  |

 | Div ≡ P x + Q y, α 1 = x ¯ ′′′′ − x ¯ ′′ + x ¯, α 2 = y ¯ ′′′′ − y ¯ ′′ + y ¯, \displaystyle\operatorname{Div}\equiv P_{x}+Q_{y},\quad\alpha_{1}=\overline{x}^{\prime\prime\prime\prime}-\overline{x}^{\prime\prime}+\overline{x},\quad\alpha_{2}=\overline{y}^{\prime\prime\prime\prime}-\overline{y}^{\prime\prime}+\overline{y}, |  |

with

 | x ¯ = x + X, y ¯ = y + Y. \overline{x}=x+X,\quad\overline{y}=y+Y. |  |

Note that Z 2 / 2 Z^{2}/2 is precisely the integrand for E 0 E_{0}, and recall that all close paths involved are 1 1 -periodic, 𝒞 ∞ \mathcal{C}^{\infty} and belong to 𝕆 \mathbb{O}, so that we can freely differentiate in t t as many times as needed. In particular, the two equations of the system of critical closed paths become

(5.20) |  | Z ′ ​ Q + Z ​ Div ⁡ y ′ = − ϵ ​ α 1, Z ′ ​ P + Z ​ Div ⁡ x ′ = ϵ ​ α 2. Z^{\prime}Q+Z\operatorname{Div}y^{\prime}=-\epsilon\alpha_{1},\quad Z^{\prime}P+Z\operatorname{Div}x^{\prime}=\epsilon\alpha_{2}. |  |

We manipulate the two equations in ( 5.20) in two ways:

1. (1)

multiply the first equation by Q Q, the second by P P, and add up the results to find

(5.21) |  | Z ′ ​ ( P 2 + Q 2) = − ϵ ⁡ ( α 1 ​ Q − α 2 ​ P) − Z ​ W ​ Div; Z^{\prime}(P^{2}+Q^{2})=-\epsilon(\alpha_{1}Q-\alpha_{2}P)-ZW\operatorname{Div}; |  |

2. (2)

then, multiply the first by P P, the second by Q Q, and subtract the results to have

 | Z 2 ​ Div = − ϵ ⁡ ( α 1 ​ P + α 2 ​ Q). Z^{2}\operatorname{Div}=-\epsilon(\alpha_{1}P+\alpha_{2}Q). |  |

We remind readers that we are searching for periodic solutions of this system for which E ϵ E_{\epsilon} is away from zero. Indeed, recall that in seeking an upper bound for the right-hand side in ( 5.13), a a is small, but kept fixed, when computing the inner limit

 | lim ϵ → 0 M c ​ r ​ i, ϵ, a. \lim_{\epsilon\to 0}M_{cri,\epsilon,a}. |  |

The second part of Theorem 3.9 ensures that there cannot be branches of critical paths { 𝐮 ϵ } \{\mathbf{u}_{\epsilon}\} with E 0 ​ ( 𝐮 ϵ) → 0 E_{0}(\mathbf{u}_{\epsilon})\to 0. We will therefore discard from our consideration those critical paths 𝐮 ϵ \mathbf{u}_{\epsilon} for which E 0 E_{0} is arbitrarily small. In particular, we do not need to consider asymptotic behaviors reducing to a point, and so, bearing in mind that equilibria of our polynomial, differential system are isolated and they could only be associated with critical closed paths of the kind we are not interested in (those with small value for E 0 E_{0}), we can further multiply ( 5.21) by Z Z and divide by P 2 + Q 2 P^{2}+Q^{2}, to have, taking into account the other equation,

 | ( Z 2) ′ = 2 ​ ϵ ​ ( α 1 ​ x ′ + α 2 ​ y ′). (Z^{2})^{\prime}=2\epsilon(\alpha_{1}x^{\prime}+\alpha_{2}y^{\prime}). |  |

Hence, system ( 5.17) can be written in the simplified, equivalent form

 | ( Z 2) ′ = 2 ​ ϵ ​ ( α 1 ​ x ′ + α 2 ​ y ′), Z 2 ​ Div = − ϵ ⁡ ( α 1 ​ P + α 2 ​ Q). (Z^{2})^{\prime}=2\epsilon(\alpha_{1}x^{\prime}+\alpha_{2}y^{\prime}),\quad Z^{2}\operatorname{Div}=-\epsilon(\alpha_{1}P+\alpha_{2}Q). |  |

To avoid confusion, we will rather write

(5.22) |  | ( Z ϵ 2) ′ = 2 ​ ϵ ​ ( α 1 ​ x ϵ ′ + α 2 ​ y ϵ ′), Z ϵ 2 ​ Div ϵ = − ϵ ⁡ ( α 1 ​ P ϵ + α 2 ​ Q ϵ). (Z_{\epsilon}^{2})^{\prime}=2\epsilon(\alpha_{1}x^{\prime}_{\epsilon}+\alpha_{2}y^{\prime}_{\epsilon}),\quad Z_{\epsilon}^{2}\operatorname{Div}_{\epsilon}=-\epsilon(\alpha_{1}P_{\epsilon}+\alpha_{2}Q_{\epsilon}). |  |

to stress the dependence on ϵ \epsilon of all quantities. Recall that

 | Z ϵ = 𝐅 ⟂ ​ ( 𝐮 ϵ) ⋅ 𝐮 ϵ ′, Div ϵ = div ⁡ 𝐅 ⁡ ( x ϵ, y ϵ), 𝐮 ϵ = ( x ϵ, y ϵ). Z_{\epsilon}=\mathbf{F}^{\perp}(\mathbf{u}_{\epsilon})\cdot\mathbf{u}^{\prime}_{\epsilon},\quad\operatorname{Div}_{\epsilon}=\operatorname{div}\mathbf{F}(x_{\epsilon},y_{\epsilon}),\quad\mathbf{u}_{\epsilon}=(x_{\epsilon},y_{\epsilon}). |  |

The first point in Theorem 3.9 informs us that in fact, along branches of critical paths ( x ϵ, y ϵ) (x_{\epsilon},y_{\epsilon}), we can neglect terms multiplied by ϵ \epsilon, and have that

 | ( Z ϵ 2) ′ → 0, Z ϵ 2 ​ Div ϵ → 0 (Z_{\epsilon}^{2})^{\prime}\to 0,\quad Z_{\epsilon}^{2}\operatorname{Div}_{\epsilon}\to 0 |  |

in L 2 ​ ( 0, 1) L^{2}(0,1). We record this fact in a formal statement.

###### Lemma 5.14.

Let ( x ϵ, y ϵ) (x_{\epsilon},y_{\epsilon}) be a branch of solutions of ( 5.22). For a suitable subsequence (not relabeled),

 | ( Z ϵ 2) ′ → 0, Z ϵ 2 ​ Div ϵ → 0, (Z_{\epsilon}^{2})^{\prime}\to 0,\quad Z_{\epsilon}^{2}\operatorname{Div}_{\epsilon}\to 0, |  |

in L 2 ​ ( 0, 1) L^{2}(0,1) and pointwise for a.e. t ∈ [0, 1] t\in[0,1].

Note how the L 2 L^{2} -convergence claimed in this statement forbids that Z ϵ 2 Z_{\epsilon}^{2} could converge to a non-constant function. We are therefore entitled to understand all possible asymptotic behaviors of critical closed paths

 | ( x ϵ, y ϵ) ∈ 𝕆 (x_{\epsilon},y_{\epsilon})\in\mathbb{O} |  |

through an analysis of the limit system

(5.23) |  | ( Z 2) ′ = 0, Z 2 ​ Div = 0, (Z^{2})^{\prime}=0,\quad Z^{2}\operatorname{Div}=0, |  |

setting ϵ = 0 \epsilon=0 in ( 5.22). The first equation in ( 5.23) implies that Z 2 = k 2 Z^{2}=k^{2} (note that here is crucial the L 2 L^{2} -convergence in Lemma 5.14), but since we are only interested in the asymptotic behavior for critical closed paths whose value for E 0 E_{0} stays away from zero, we discard the case k = 0 k=0. In this situation, the second equation in ( 5.23), implies Div = 0 \operatorname{Div}=0. We would like to understand the nature of solutions of the limit system

(5.24) |  | Z 2 = k 2 > 0, Div = 0. Z^{2}=k^{2}>0,\quad\operatorname{Div}=0. |  |

We write this system in the form, differentiating the second equation,

(5.25) |  | 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐮 ′ = ± k ≠ 0, ∇ Div ⁡ ( 𝐮) ⋅ 𝐮 ′ = 0. \mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{u}^{\prime}=\pm k\neq 0,\quad\nabla\operatorname{Div}(\mathbf{u})\cdot\mathbf{u}^{\prime}=0. |  |

This is an implicit, first-order system that becomes singular when the determinant

 | ∇ Div ⁡ ( 𝐮) ⋅ 𝐅 ⁡ ( 𝐮) \nabla\operatorname{Div}(\mathbf{u})\cdot\mathbf{F}(\mathbf{u}) |  |

of the matrix of the system

 | ( 𝐅 ⟂ ​ ( 𝐮) ∇ Div ⁡ ( 𝐮)) \begin{pmatrix}\mathbf{F}^{\perp}(\mathbf{u})\\ \nabla\operatorname{Div}(\mathbf{u})\end{pmatrix} |  |

vanishes. These singular points are precisely the contact points of our differential system over the curve Div = 0 \operatorname{Div}=0. The fact that

 | 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐮 ′ = ± k ≠ 0 \mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{u}^{\prime}=\pm k\neq 0 |  |

shows that 𝐮 ϵ \mathbf{u}_{\epsilon}, for ϵ \epsilon sufficiently small, can only turn around, changing + k +k by − k -k or viceversa, near those contact points. As a matter of fact, critical closed paths 𝐮 ϵ \mathbf{u}_{\epsilon} do have to turn around whenever one such point is reached and is a single root of system ( 1.2). To emphasize this point, we explicitly introduce the following.

###### Definition 5.3.

A point 𝐩 ∈ ℝ 2 \mathbf{p}\in\mathbb{R}^{2} is a single (or simple) contact point of our differential system, if

 | det ( 𝐅 ⟂ ​ ( 𝐮) ∇ Div ⁡ ( 𝐮)) \det\begin{pmatrix}\mathbf{F}^{\perp}(\mathbf{u})\\ \nabla\operatorname{Div}(\mathbf{u})\end{pmatrix} |  |

vanishes at 𝐮 = 𝐩 \mathbf{u}=\mathbf{p}, but it changes sign in every neighborhood of 𝐩 \mathbf{p} in Div = 0 \operatorname{Div}=0.

We can now establish in a precise way the role played by single, contact points.

###### Lemma 5.15.

Let 𝐮 ϵ = ( x ϵ, y ϵ) \mathbf{u}_{\epsilon}=(x_{\epsilon},y_{\epsilon}) be a branch of critical closed paths of E ϵ E_{\epsilon} such that E 0 ​ ( 𝐮 ϵ) E_{0}(\mathbf{u}_{\epsilon}) stays away from zero. Suppose that in a certain subinterval

 | [t ϵ −, t ϵ +] ⊂ [0, 1], t ϵ + − t ϵ − → 0, [t^{-}_{\epsilon},t^{+}_{\epsilon}]\subset[0,1],\quad t_{\epsilon}^{+}-t_{\epsilon}^{-}\to 0, |  |

we know that

 | | 𝐮 ϵ ′ ​ ( t ϵ ±) | → + ∞, 𝐮 ϵ ​ ( t ϵ ±) → 𝐩, |\mathbf{u}^{\prime}_{\epsilon}(t^{\pm}_{\epsilon})|\to+\infty,\quad\mathbf{u}_{\epsilon}(t^{\pm}_{\epsilon})\to\mathbf{p}, |  |

as ϵ → 0 \epsilon\to 0, where 𝐩 \mathbf{p} is a single, contact point of the system. Then 𝐮 ϵ \mathbf{u}_{\epsilon} must turn around at 𝐩 \mathbf{p} for ϵ \epsilon sufficiently small, in the sense

(5.26) |  | 𝐮 ϵ ′ ​ ( t ϵ −) | 𝐮 ϵ ′ ​ ( t ϵ −) | + 𝐮 ϵ ′ ​ ( t ϵ +) | 𝐮 ϵ ′ ​ ( t ϵ +) | → 𝟎 \frac{\mathbf{u}^{\prime}_{\epsilon}(t^{-}_{\epsilon})}{|\mathbf{u}^{\prime}_{\epsilon}(t^{-}_{\epsilon})|}+\frac{\mathbf{u}^{\prime}_{\epsilon}(t^{+}_{\epsilon})}{|\mathbf{u}^{\prime}_{\epsilon}(t^{+}_{\epsilon})|}\to\mathbf{0} |  |

as ϵ → 0 \epsilon\to 0.

[image: Refer to caption] Figure 1. Situation around a contact point: top, a multiple contact point; bottom, a single contact point.

###### Proof.

Figure 1 can help in understanding the situation. The single, contact point 𝐩 \mathbf{p} is the intersection of both axes. Keep in mind that

 | Z 2 = ( F ⟂ ​ ( 𝐮) ⋅ 𝐮 ′) 2 → k 2, Z → ± k, Z^{2}=(F^{\perp}(\mathbf{u})\cdot\mathbf{u}^{\prime})^{2}\to k^{2},\quad Z\to\pm k, |  |

a constant uniformly away from zero, as 𝐮 → 𝐩 \mathbf{u}\to\mathbf{p}. Z 2 Z^{2} must be continuous through 𝐩 \mathbf{p}, but Z Z might change sign abruptly. The possibility for 𝐮 \mathbf{u} to turn around at 𝐩 \mathbf{p}, jumping from k k to − k -k, is always there. The thing is that if 𝐩 \mathbf{p} is a single contact point, a simple solution of system ( 1.2), then this is the only possibility. Indeed, the only way for 𝐮 \mathbf{u} to cross over a contact point 𝐩 \mathbf{p} is for the inner product

 | 𝐅 ⟂ ​ ( 𝐮) ⋅ 𝐮 ′ ( = Z) \mathbf{F}^{\perp}(\mathbf{u})\cdot\mathbf{u}^{\prime}(=Z) |  |

to retain its sign as to avoid a jump discontinuity. This is impossible at a single, contact point (bottom picture of Figure 1 corresponding to a simple contact point), while it is coherent with a double (or even-order) contact point (top picture in the same figure). ∎

Our above discussion can be summarized in the following statement that classifies all possible asymptotic behaviors for critical closed paths.

###### Theorem 5.16.

Assume that all the components of the curve Div = 0 \operatorname{Div}=0 are topologically straight lines or ovals. The possible limit behaviors as ϵ → 0 \epsilon\to 0 of branches of critical closed paths of E ε E_{\varepsilon}, with critical value uniformly away from zero, can be necessarily identified with arcs of the connected components of the curve Div = 0 \operatorname{Div}=0 in one of the following possibilities:

- (a)

If the component is homeomorphic to a straight line, then

  - (a.1)

the limit behavior is an arc whose endpoints are two contact points and no additional contact point lies in its interior;

  - (a.2)

the limit behavior is an arc whose endpoints are one contact point and the infinity, and no additional contact point can be found in its interior;

  - (a.3)

the limit behavior is the whole component without contact points.

- (b)

If the component is homeomorphic to an oval, then

  - (b.1)

the limit behavior is an arc whose endpoints are two contact points and no additional contact point lies in its interior;

  - (b.2)

the limit behavior is an arc covering the full oval whose endpoints have to be a single contact point, and no additional contact point is to be found in the oval;

  - (b.3)

the limit behavior is the whole oval without contact points.

### 5.7. Multiplicity

We are concerned in this subsection about the possibility that various branches of the set of critical closed paths, for ϵ \epsilon positive, may coalesce into the same limit behavior as ϵ ↘ 0 \epsilon\searrow 0, and how they can possibly contribute to the number of critical paths. We will need to exploit very precisely the information that the number of any such group of critical paths share, at least locally, the same limit behavior as ϵ → 0 \epsilon\to 0.

As a consequence of Definition 5.2, and comments made after it, the set of possible singular pairs ( 𝐩, 𝐪) (\mathbf{p},\mathbf{q}) where maps

 | 𝐮 ⁡ ( t, 𝐩, 𝐪, ϵ) \mathbf{u}(t;\mathbf{p},\mathbf{q},\epsilon) |  |

are not well-defined because there might be more than one critical path with

 | 𝐮 ⁡ ( 0, 𝐩, 𝐪, ϵ) = 𝐮 ⁡ ( 1, 𝐩, 𝐪, ϵ) = 𝐩, 𝐮 ′ ​ ( 0, 𝐩, 𝐪, ϵ) = 𝐮 ′ ​ ( 1, 𝐩, 𝐪, ϵ) = 𝐪, \mathbf{u}(0;\mathbf{p},\mathbf{q},\epsilon)=\mathbf{u}(1;\mathbf{p},\mathbf{q},\epsilon)=\mathbf{p},\quad\mathbf{u}^{\prime}(0;\mathbf{p},\mathbf{q},\epsilon)=\mathbf{u}^{\prime}(1;\mathbf{p},\mathbf{q},\epsilon)=\mathbf{q}, |  |

is isolated, for each fixed ϵ \epsilon, as a consequence of analyticity. This is in fact the only reason to stress the analytic dependence of this map. For a given (countable) sequence of values for ϵ \epsilon, we can always find a certain point 𝐩 \mathbf{p} in the part of the curve Div = 0 \operatorname{Div}=0, with tangent vector 𝐪 \mathbf{q}, identifying the particular asymptotic limit we are focusing on, and away from any contact point of the system limiting the asymptotic behavior considered according to Theorem 5.16, in such a way that the family of maps

(5.27) |  | 𝐮 ⁡ ( t, 𝐲, 𝐳, ϵ): [0, 1] × 𝔹 ρ ​ ( 𝐩) × 𝔹 ρ ​ ( 𝐪) → ℝ 2 \mathbf{u}(t;\mathbf{y},\mathbf{z},\epsilon):[0,1]\times{\mathbb{B}}_{\rho}(\mathbf{p})\times{\mathbb{B}}_{\rho}(\mathbf{q})\to\mathbb{R}^{2} |  |

is well-defined, smooth (even analytic) in all variables ( t, 𝐲, 𝐳) (t,\mathbf{y},\mathbf{z}), for every value of ϵ \epsilon from the selected sequence, and some positive radius ρ \rho. The interesting point is that the domain of this family of maps can be taken independently of ϵ \epsilon, at least for a sequence of values of ϵ \epsilon converging to zero. We will not make the distinction between a countable set of values of ϵ \epsilon and the full continuum since this distinction is irrelevant for our purposes. Recall that, in addition to verifying ( 5.19) in Proposition 5.13, we also have

 | 𝐮 ⁡ ( 0, 𝐲, 𝐳, ϵ) = 𝐮 ⁡ ( 1, 𝐲, 𝐳, ϵ) = 𝐲, 𝐮 ′ ​ ( 0, 𝐲, 𝐳, ϵ) = 𝐮 ′ ​ ( 1, 𝐲, 𝐳, ϵ) = 𝐳, \mathbf{u}(0;\mathbf{y},\mathbf{z},\epsilon)=\mathbf{u}(1;\mathbf{y},\mathbf{z},\epsilon)=\mathbf{y},\quad\mathbf{u}^{\prime}(0;\mathbf{y},\mathbf{z},\epsilon)=\mathbf{u}^{\prime}(1;\mathbf{y},\mathbf{z},\epsilon)=\mathbf{z}, |  |

for

 | ( 𝐲, 𝐳) ∈ 𝔹 ρ ​ ( 𝐩) × 𝔹 ρ ​ ( 𝐪). (\mathbf{y},\mathbf{z})\in{\mathbb{B}}_{\rho}(\mathbf{p})\times{\mathbb{B}}_{\rho}(\mathbf{q}). |  |

We are going to proceed in two successive steps.

1. (1)

Suppose 𝐲 \mathbf{y} is kept fixed in a neighborhood of 𝐩 \mathbf{p}, so that we would work in the space H 𝐲, 2 ( 0, 1]; ℝ 2) H^{2}_{\mathbf{y},}(0,1];\mathbb{R}^{2}). How many critical paths of the perturbed functional E ϵ E_{\epsilon} could there be in this space, i.e. paths described in Proposition 5.12? We will show that there cannot be more than n − 1 n-1 such paths regardless of the value of 𝐲 \mathbf{y}. These n − 1 n-1 paths will correspond to our mapping 𝐮 ⁡ ( t, 𝐲, 𝐳, ϵ) \mathbf{u}(t;\mathbf{y},\mathbf{z},\epsilon) for suitable velocity vectors

 | 𝐳 = 𝐳 i ( 𝐲), i = 1, 2, …, n − 1, \mathbf{z}=\mathbf{z}_{i}(\mathbf{y}),\quad i=1,2,\dots,n-1, |  |

that is to say

(5.28) |  | 𝐮 i ( t; 𝐲, ϵ) ≡ 𝐮 ( t; 𝐲, 𝐳 i ( 𝐲), ϵ), i = 1, 2, …, n − 1, \mathbf{u}_{i}(t;\mathbf{y},\epsilon)\equiv\mathbf{u}(t;\mathbf{y},\mathbf{z}_{i}(\mathbf{y}),\epsilon),\quad i=1,2,\dots,n-1, |  |

are the critical paths in Proposition 5.12 for each fixed 𝐲 \mathbf{y}. The maps 𝐳 i ​ ( 𝐲) \mathbf{z}_{i}(\mathbf{y}) are again smooth due to the standard regularity dependence of solutions of differential problems on initial conditions.

2. (2)

For each given i = 1, 2, …, n − 1 i=1,2,\dots,n-1, how many values of 𝐲 \mathbf{y} in a neighborhood of 𝐩 \mathbf{p} can there be such that 𝐮 i ​ ( t, 𝐲, ϵ) \mathbf{u}_{i}(t;\mathbf{y},\epsilon) in ( 5.28) is one of the critical paths we are interested in counting, i. e. critical paths in Proposition 5.11? Again we will show that, for each i i, there are at most n − 1 n-1 such paths.

Our strategy is led by two main points.

1. (1)

We would like to replace vector variables 𝐲 \mathbf{y} and 𝐳 \mathbf{z} in ( 5.27) by single variables r r and s s, respectively, since our arguments will depend on facts that are only valid for polynomials of a single real variable.

2. (2)

Use the full power of being a critical path to localize arguments through suitable test paths, and reduce the counting procedure to a question about one-variable polynomials.

Since paths 𝐮 ⁡ ( t, 𝐲, 𝐳, ϵ) \mathbf{u}(t;\mathbf{y},\mathbf{z},\epsilon) will intersect the straight line

 | { 𝐩 + r ​ 𝐪 ⟂: r ∈ ℝ }, \{\mathbf{p}+r\mathbf{q}^{\perp}:r\in\mathbb{R}\}, |  |

at least for small ϵ \epsilon and small r r, due to the convergence to one of our asymptotic limits, by resetting the initial time t = 0 t=0 and reparametrizing the path conveniently around t = 0 t=0, we can replace 𝐲 \mathbf{y} by 𝐩 + r ​ 𝐪 ⟂ \mathbf{p}+r\mathbf{q}^{\perp} in the above discussion in such a way that we have a single variable r r to label the starting point of our critical paths. To make things easier, we will replace the unit interval [0, 1] [0,1] by [− 1 / 2, 1 / 2] [-1/2,1/2] in this section. In the same vein, in a neighborhood of 𝐪 \mathbf{q}, the velocity vector 𝐳 \mathbf{z} can be considered of the form 𝐪 + s ​ 𝐪 ⟂ \mathbf{q}+s\mathbf{q}^{\perp} for | s | |s| sufficiently small, possibly at the expense of changing slightly, through a linear reparametrization to transform appropriately the length of 𝐳 \mathbf{z} and without changing the feature of being critical for E ϵ E_{\epsilon}, the unit interval [− 1 / 2, 1 / 2] [-1/2,1/2] by [− S ϵ, S ϵ] [-S_{\epsilon},S_{\epsilon}] with S ϵ → 1 / 2 S_{\epsilon}\to 1/2 as ϵ → 0 \epsilon\to 0. This is not a problem as we will subsequently work in subintervals J ϵ J_{\epsilon} of small length around 0 0. In this way, we can assume, without loss of generality in our above discussion that

 | 𝐲 = 𝐩 + r ​ 𝐪 ⟂, 𝐳 = 𝐪 + s ​ 𝐪 ⟂, \displaystyle\mathbf{y}=\mathbf{p}+r\mathbf{q}^{\perp},\quad\mathbf{z}=\mathbf{q}+s\mathbf{q}^{\perp}, |  |

 | 𝐮 ⁡ ( t, r, s, ϵ) ≡ 𝐮 ⁡ ( t, 𝐩 + r ​ 𝐪 ⟂, 𝐪 + s ​ 𝐪 ⟂, ϵ), \displaystyle\mathbf{u}(t;r,s,\epsilon)\equiv\mathbf{u}(t;\mathbf{p}+r\mathbf{q}^{\perp},\mathbf{q}+s\mathbf{q}^{\perp},\epsilon), |  |

and so the two steps in our counting method will depend in both cases on single variables either r r or s s. More specifically, we can review the preceding two main successive stages in the following explicit manner.

1. (1)

Assume r r is given of size sufficiently small. How many values of s s could there possibly be so that 𝐮 ⁡ ( t, r, s, ϵ) \mathbf{u}(t;r,s,\epsilon) represent critical paths in Proposition 5.12? Argue that there cannot be more than n − 1 n-1, corresponding to the n − 1 n-1 smooth branches s i ​ ( r) s_{i}(r).

2. (2)

For each such branch s i ​ ( r) s_{i}(r), show that there cannot possibly be more than n − 1 n-1 values of r r such that

(5.29) |  | 𝐮 i ( t; r, ϵ) = 𝐮 ( t; r, s i ( r), ϵ), i = 1, 2, …, n − 1, \mathbf{u}_{i}(t;r,\epsilon)=\mathbf{u}(t;r,s_{i}(r),\epsilon),\quad i=1,2,\dots,n-1, |  |

are critical paths in Proposition 5.11, i.e. the paths we aim at counting.

If we can cover these two steps successfully, we will have our main result in this section. It may be interesting to realize that if some of the roots for r r or s s that we pretend to count correspond to the same critical path (because of the fact that paths belong to some 𝕆 d \mathbb{O}_{d} with d > 1 d>1), the bound we are claiming would still be valid for in that case there would be less distinct critical paths.

###### Theorem 5.17.

There cannot be more than ( n − 1) 2 (n-1)^{2} branches of critical closed paths in Proposition 5.11 converging to any of the possible asymptotic behaviors given in Theorem 5.16.

###### Proof.

As just indicated, we will proceed in two main successive steps: first, for fixed r r, try to understand critical paths 𝐮 ⁡ ( t, r, s, ϵ) \mathbf{u}(t;r,s,\epsilon) in Proposition 5.12 depending on s s; secondly, for each branch i i found in the previous step, make an attempt to examine critical paths 𝐮 i ​ ( t, r, ϵ) \mathbf{u}_{i}(t;r,\epsilon), given in ( 5.29), in Proposition 5.11. In both cases, critical paths make the derivative E ϵ ′ E^{\prime}_{\epsilon} vanish, through test paths

 | 𝐖 ϵ ∈ H O 2 ​ ( [0, 1], ℝ 2), \mathbf{W}_{\epsilon}\in H^{2}_{O}([0,1];\mathbb{R}^{2}), |  |

that will be appropriately chosen below in each situation. More explicitly

(5.30) |  | ⟨ E ϵ ′ ​ ( 𝐮 ⁡ ( r, s, ϵ)), 𝐖 ϵ ⟩ = ⟨ E 0 ′ ​ ( 𝐮 ⁡ ( r, s, ϵ)), 𝐖 ϵ ⟩ + ϵ ⁡ ⟨ 𝐮 ⁡ ( r, s, ϵ), 𝐖 ϵ ⟩ + ⟨ 𝐯 0, 𝐖 ϵ ⟩ \langle E^{\prime}_{\epsilon}(\mathbf{u}(r,s,\epsilon)),\mathbf{W}_{\epsilon}\rangle=\langle E^{\prime}_{0}(\mathbf{u}(r,s,\epsilon)),\mathbf{W}_{\epsilon}\rangle+\epsilon\langle\mathbf{u}(r,s,\epsilon),\mathbf{W}_{\epsilon}\rangle+\langle\mathbf{v}_{0},\mathbf{W}_{\epsilon}\rangle |  |

should vanish on critical paths. It is important to realize that such test paths 𝐖 ϵ \mathbf{W}_{\epsilon} can depend on ϵ \epsilon, since this will permit a flexibility that is very convenient to our purposes. As already remarked before, our strategy is to localize the vanishing of ( 5.30) through a judicious choice for 𝐖 ϵ \mathbf{W}_{\epsilon} so as to reduce the counting procedure essentially to an issue of roots of polynomials of a single variable. Let us once again insist in that ( 5.30) should vanish at critical paths 𝐮 ⁡ ( r, s, ϵ) \mathbf{u}(r,s,\epsilon) for every legitimate choice of test path 𝐖 ϵ \mathbf{W}_{\epsilon}.

The fundamental difference between those test paths 𝐖 ϵ \mathbf{W}_{\epsilon} in Propositions 5.11 and 5.12 is intimately related to the fact that in the first case 𝐖 ϵ \mathbf{W}_{\epsilon} must vanish for t = 0 t=0, while for the second they don’t have to. Recall that

 | 𝐮 ⁡ ( t, r, s, ϵ) ≡ 𝐮 ⁡ ( t, 𝐩 + r ​ 𝐪 ⟂, 𝐪 + s ​ 𝐪 ⟂, ϵ), 𝐮 ⁡ ( r, s, ϵ) = 𝐮 ⁡ ( t, r, s, ϵ), \mathbf{u}(t;r,s,\epsilon)\equiv\mathbf{u}(t;\mathbf{p}+r\mathbf{q}^{\perp},\mathbf{q}+s\mathbf{q}^{\perp},\epsilon),\quad\mathbf{u}(r,s,\epsilon)=\mathbf{u}(t;r,s,\epsilon), |  |

and that the test path 𝐖 ϵ \mathbf{W}_{\epsilon} can also depend eventually on ϵ \epsilon, as already emphasized. Before we reach the point where the difference for the test path 𝐖 ϵ \mathbf{W}_{\epsilon} must be taken into account, let us examine the explicit form of the derivative in ( 5.30).

If we recall formula ( 5.6), we can write explicitly the term

 | ⟨ E 0 ′ ​ ( 𝐮 ⁡ ( r, s, ϵ)), 𝐖 ϵ ⟩ \langle E^{\prime}_{0}(\mathbf{u}(r,s,\epsilon)),\mathbf{W}_{\epsilon}\rangle |  |

in the form

(5.31) |  | ∫ 0 1 ( 𝐅 ⟂ ​ ( 𝐮 ⁡ ( r, s, ϵ)) ⋅ 𝐮 ′ ​ ( r, s, ϵ)) ​ ( D ​ 𝐅 ⟂ ​ ( 𝐮 ⁡ ( r, s, ϵ)) ​ 𝐖 ϵ) ⋅ 𝐮 ′ ​ ( r, s, ϵ) ​ 𝑑 t \displaystyle\int_{0}^{1}(\mathbf{F}^{\perp}(\mathbf{u}(r,s,\epsilon))\cdot\mathbf{u}^{\prime}(r,s,\epsilon))(D\mathbf{F}^{\perp}(\mathbf{u}(r,s,\epsilon))\mathbf{W}_{\epsilon})\cdot\mathbf{u}^{\prime}(r,s,\epsilon)\,dt |  |

 | + ∫ 0 1 ( 𝐅 ⟂ ( 𝐮 ( r, s, ϵ)) ⋅ 𝐮 ′ ( r, s, ϵ)) 𝐅 ⟂ ( 𝐮 ( r, s, ϵ)) ⋅ 𝐖 ϵ ′] d t, \displaystyle+\int_{0}^{1}(\mathbf{F}^{\perp}(\mathbf{u}(r,s,\epsilon))\cdot\mathbf{u}^{\prime}(r,s,\epsilon))\mathbf{F}^{\perp}(\mathbf{u}(r,s,\epsilon))\cdot\mathbf{W}^{\prime}_{\epsilon}]\,dt, |  |

where primes indicate differentiation with respect to time t t. We will eventually take

(5.32) |  | 𝐖 ϵ ​ ( t) = χ ϵ ​ ( t) ​ 𝐖 ~ ϵ ​ ( t) \mathbf{W}_{\epsilon}(t)=\chi_{\epsilon}(t)\tilde{\mathbf{W}}_{\epsilon}(t) |  |

with { χ ϵ } \{\chi_{\epsilon}\}, a sequence of suitable mollifiers (recall Subsection 4.7), and 𝐖 ~ ϵ ​ ( t) \tilde{\mathbf{W}}_{\epsilon}(t), chosen later appropriately. Since the support J ϵ J_{\epsilon} of the mollifier χ ϵ \chi_{\epsilon} can be selected in such a way that the factor

 | 𝐅 ⟂ ​ ( 𝐮 ⁡ ( r, s, ϵ)) ⋅ 𝐮 ′ ​ ( r, s, ϵ), \mathbf{F}^{\perp}(\mathbf{u}(r,s,\epsilon))\cdot\mathbf{u}^{\prime}(r,s,\epsilon), |  |

which is the integrand for E 0 E_{0}, tends to be a constant k ϵ k_{\epsilon} uniformly away from zero, according to our discussion in Section 5.6, and, after all, we are interested in values of pairs ( r, s) (r,s) vanishing the derivative in ( 5.30), we realize that we can replace the previous form of the derivative (whose first term is written in ( 5.31)) by the expression

 | k ϵ ​ ∫ J ϵ [( D ​ 𝐅 ⟂ ​ ( 𝐮 ⁡ ( r, s, ϵ)) ​ 𝐖 ϵ) ⋅ 𝐮 ′ ​ ( r, s, ϵ) + 𝐅 ⟂ ​ ( 𝐮 ⁡ ( r, s, ϵ)) ⋅ 𝐖 ϵ ′] ​ 𝑑 t \displaystyle k_{\epsilon}\int_{J_{\epsilon}}[(D\mathbf{F}^{\perp}(\mathbf{u}(r,s,\epsilon))\mathbf{W}_{\epsilon})\cdot\mathbf{u}^{\prime}(r,s,\epsilon)+\mathbf{F}^{\perp}(\mathbf{u}(r,s,\epsilon))\cdot\mathbf{W}^{\prime}_{\epsilon}]\,dt |  |

 | + ϵ ⁡ ⟨ 𝐮 ⁡ ( r, s, ϵ), 𝐖 ϵ ⟩ + ⟨ 𝐯 0, 𝐖 ϵ ⟩. \displaystyle+\epsilon\langle\mathbf{u}(r,s,\epsilon),\mathbf{W}_{\epsilon}\rangle+\langle\mathbf{v}_{0},\mathbf{W}_{\epsilon}\rangle. |  |

Let us focus our attention on this integral

 | I ϵ = ∫ J ϵ [( D ​ 𝐅 ⟂ ​ ( 𝐮 ⁡ ( r, s, ϵ)) ​ 𝐖 ϵ) ⋅ 𝐮 ′ ​ ( r, s, ϵ) + 𝐅 ⟂ ​ ( 𝐮 ⁡ ( r, s, ϵ)) ⋅ 𝐖 ϵ ′] ​ 𝑑 t. I_{\epsilon}=\int_{J_{\epsilon}}[(D\mathbf{F}^{\perp}(\mathbf{u}(r,s,\epsilon))\mathbf{W}_{\epsilon})\cdot\mathbf{u}^{\prime}(r,s,\epsilon)+\mathbf{F}^{\perp}(\mathbf{u}(r,s,\epsilon))\cdot\mathbf{W}^{\prime}_{\epsilon}]\,dt. |  |

We can perform an integration by parts in the second term (note that contributions at end-points vanish) to find

 | I ϵ = ∫ J ϵ [( D ​ 𝐅 ⟂ ​ ( 𝐮 ⁡ ( r, s, ϵ)) ​ 𝐖 ϵ) ⋅ 𝐮 ′ ​ ( r, s, ϵ) − ( D ​ 𝐅 ⟂ ​ ( 𝐮 ⁡ ( r, s, ϵ)) ​ 𝐮 ′ ​ ( r, s, ϵ)) ⋅ 𝐖 ϵ] ​ 𝑑 t I_{\epsilon}=\int_{J_{\epsilon}}[(D\mathbf{F}^{\perp}(\mathbf{u}(r,s,\epsilon))\mathbf{W}_{\epsilon})\cdot\mathbf{u}^{\prime}(r,s,\epsilon)-(D\mathbf{F}^{\perp}(\mathbf{u}(r,s,\epsilon))\mathbf{u}^{\prime}(r,s,\epsilon))\cdot\mathbf{W}_{\epsilon}]\,dt |  |

or, by recalling ( 5.32),

 | I ϵ = \displaystyle I_{\epsilon}= | ∫ J ϵ χ ϵ ​ ( t) ​ [D ​ 𝐅 ⟂ ​ ( 𝐮 ⁡ ( r, s, ϵ)) T − D ​ 𝐅 ⟂ ​ ( 𝐮 ⁡ ( r, s, ϵ))] ​ 𝐮 ′ ​ ( r, s, ϵ) ⋅ 𝐖 ~ ϵ ​ 𝑑 t \displaystyle\int_{J_{\epsilon}}\chi_{\epsilon}(t)[D\mathbf{F}^{\perp}(\mathbf{u}(r,s,\epsilon))^{T}-D\mathbf{F}^{\perp}(\mathbf{u}(r,s,\epsilon))]\mathbf{u}^{\prime}(r,s,\epsilon)\cdot\tilde{\mathbf{W}}_{\epsilon}\,dt |  |

 | = \displaystyle= | − ∫ J ϵ χ ϵ ( t) Div ( 𝐮 ( r, s, ϵ)) 𝐮 ′ ( r, s, ϵ) ⟂ ⋅ 𝐖 ~ ϵ d t, \displaystyle-\int_{J_{\epsilon}}\chi_{\epsilon}(t)\operatorname{Div}(\mathbf{u}(r,s,\epsilon))\mathbf{u}^{\prime}(r,s,\epsilon)^{\perp}\cdot\tilde{\mathbf{W}}_{\epsilon}\,dt, |  |

where

 | 𝐮 ′ ​ ( r, s, ϵ) ⟂ = 𝐐𝐮 ′ ​ ( r, s, ϵ), 𝐐 = ( 0 − 1 1 0). \mathbf{u}^{\prime}(r,s,\epsilon)^{\perp}=\mathbf{Q}\mathbf{u}^{\prime}(r,s,\epsilon),\quad\mathbf{Q}=\begin{pmatrix}0&-1\\ 1&0\end{pmatrix}. |  |

The family of functions f ϵ ​ ( r, s) f_{\epsilon}(r,s) of two variables ( r, s) (r,s) we need to deal with is then, after an irrelevant change of sign,

(5.33) |  | f ϵ ​ ( r, s) ≡ \displaystyle f_{\epsilon}(r,s)\equiv | ∫ J ϵ χ ϵ ​ ( t) ​ Div ⁡ ( 𝐮 ⁡ ( r, s, ϵ)) ​ 𝐮 ′ ​ ( r, s, ϵ) ⟂ ⋅ 𝐖 ~ ϵ ​ 𝑑 t \displaystyle\int_{J_{\epsilon}}\chi_{\epsilon}(t)\operatorname{Div}(\mathbf{u}(r,s,\epsilon))\mathbf{u}^{\prime}(r,s,\epsilon)^{\perp}\cdot\tilde{\mathbf{W}}_{\epsilon}\,dt |  |

 |  | − ϵ k ϵ ​ ⟨ 𝐮 ⁡ ( r, s, ϵ), 𝐖 ϵ ⟩ − 1 k ϵ ​ ⟨ 𝐯 0, 𝐖 ϵ ⟩. \displaystyle-\frac{\epsilon}{k_{\epsilon}}\langle\mathbf{u}(r,s,\epsilon),\mathbf{W}_{\epsilon}\rangle-\frac{1}{k_{\epsilon}}\langle\mathbf{v}_{0},\mathbf{W}_{\epsilon}\rangle. |  |

We now focus on the first step of our program. Fix r r, small. For a family of critical paths 𝐮 ⁡ ( r, s, ϵ) \mathbf{u}(r,s,\epsilon), the family of functions in ( 5.33) should vanish according to our above discussion, and so a bound for the number of such roots in the variable s s will furnish an upper bound for the number of such critical paths 𝐮 ⁡ ( r, s, ϵ) \mathbf{u}(r,s,\epsilon). Recall that test path 𝐖 ϵ \mathbf{W}_{\epsilon} is the product in ( 5.32). It suffices to select the support of the mollifier

(5.34) |  | J ϵ = [0, 2 ​ α ​ ( ϵ)] J_{\epsilon}=[0,2\alpha(\epsilon)] |  |

in such a way that the product in ( 5.32) is indeed a feasible variation in Proposition 5.12. In particular, as recalled above, we ought to have

 | 𝐖 ϵ ​ ( 0) = χ ϵ ​ ( 0) ​ 𝐖 ~ ϵ ​ ( 0) = 𝟎. \mathbf{W}_{\epsilon}(0)=\chi_{\epsilon}(0)\tilde{\mathbf{W}}_{\epsilon}(0)=\mathbf{0}. |  |

This is guaranteed by the previous choice for the support of χ ϵ \chi_{\epsilon} in ( 5.34). Other than that, 𝐖 ~ ϵ ​ ( t) \tilde{\mathbf{W}}_{\epsilon}(t) can be chosen in an arbitrary way to our advantage, as well as α ⁡ ( ϵ) > 0 \alpha(\epsilon)>0.

On the other hand, consider the family of polynomials of a single variable s s, for each fixed r r, given by

(5.35) |  | P ϵ ​ ( s) = Div ⁡ [𝐩 + r ​ 𝐪 ⟂ + α ⁡ ( ϵ) ​ ( 𝐪 + s ​ 𝐪 ⟂)]. P_{\epsilon}(s)=\operatorname{Div}[\mathbf{p}+r\mathbf{q}^{\perp}+\alpha(\epsilon)(\mathbf{q}+s\mathbf{q}^{\perp})]. |  |

Let N ≤ n − 1 N\leq n-1 be the degree of such polynomials in the variable s s (recall that r r is being kept frozen here), and take

(5.36) |  | 𝐖 ~ ϵ ​ ( t) ≡ 1 α ​ ( ϵ) N ​ 𝐪 ⟂, 𝐖 ϵ = χ ϵ ​ ( t) ​ 𝐖 ~ ϵ. \tilde{\mathbf{W}}_{\epsilon}(t)\equiv\frac{1}{\alpha(\epsilon)^{N}}\mathbf{q}^{\perp},\quad\mathbf{W}_{\epsilon}=\chi_{\epsilon}(t)\tilde{\mathbf{W}}_{\epsilon}. |  |

Keep in mind that Div ⁡ ( x, y) \operatorname{Div}(x,y) is a polynomial of at most degree n − 1 n-1 in two variables. Assume that, for fixed r r, we could find at least N + 1 N+1 branches of values for s s that are roots of f ϵ f_{\epsilon} in ( 5.33), including possibly multiplicities, i.e.

 | f ϵ ( r, s j ( ϵ, r)) = 0, s = s j ( ϵ, r), j = 1, 2, …, N, N + 1. f_{\epsilon}(r,s_{j}(\epsilon,r))=0,\quad s=s_{j}(\epsilon,r),j=1,2,\dots,N,N+1. |  |

Because each f ϵ f_{\epsilon} is smooth, there would be a certain value s ⁡ ( ϵ) s(\epsilon), s ⁡ ( ϵ) → 0 s(\epsilon)\to 0, such that

 | ∂ N f ϵ ∂ s N ​ ( r, s ⁡ ( ϵ)) = 0 ​ for all ​ ϵ. \frac{\partial^{N}f_{\epsilon}}{\partial s^{N}}(r,s(\epsilon))=0\hbox{ for all }\epsilon. |  |

We have dropped the dependence of s s on r r here for the sake of notational simplicity. If we go back to our formula for f ϵ ​ ( r, s) f_{\epsilon}(r,s), and take into account that all functions involved are smooth and variables move in intervals where everything is bounded, we can take differentiation under the integral sign, and find that

 | 0 = \displaystyle 0= | ∫ J ϵ χ ϵ ​ ( t) ​ ∂ N ∂ s N | s = s ⁡ ( ϵ) ​ [Div ⁡ ( 𝐮 ⁡ ( r, s, ϵ)) ​ 𝐮 ′ ​ ( r, s, ϵ) ⟂ ⋅ 𝐖 ~ ϵ] ​ 𝑑 t \displaystyle\int_{J_{\epsilon}}\chi_{\epsilon}(t)\left.\frac{\partial^{N}}{\partial s^{N}}\right|_{s=s(\epsilon)}[\operatorname{Div}(\mathbf{u}(r,s,\epsilon))\mathbf{u}^{\prime}(r,s,\epsilon)^{\perp}\cdot\tilde{\mathbf{W}}_{\epsilon}]\,dt |  |

 |  | − ϵ k ϵ ​ ∂ N ∂ s N | s = s ⁡ ( ϵ) ​ ⟨ 𝐮 ⁡ ( r, s, ϵ), 𝐖 ϵ ⟩. \displaystyle-\frac{\epsilon}{k_{\epsilon}}\left.\frac{\partial^{N}}{\partial s^{N}}\right|_{s=s(\epsilon)}\langle\mathbf{u}(r,s,\epsilon),\mathbf{W}_{\epsilon}\rangle. |  |

For the second term, we can write, after several integrations by parts,

 | ⟨ 𝐮 ⁡ ( r, s, ϵ), 𝐖 ϵ ⟩ = \displaystyle\langle\mathbf{u}(r,s,\epsilon),\mathbf{W}_{\epsilon}\rangle= | ∫ J ϵ ∑ i = 0 2 𝐮 OPEN i) ​ ( t, r, s, ϵ) ⋅ 𝐖 ϵ OPEN i) ​ ( t) ​ 𝑑 t \displaystyle\int_{J_{\epsilon}}\sum_{i=0}^{2}\mathbf{u}^{i)}(t;r,s,\epsilon)\cdot\mathbf{W}_{\epsilon}^{i)}(t)\,dt |  |

 | = \displaystyle= | ∫ J ϵ χ ϵ ​ ( t) ​ ∑ i = 0 2 ( − 1) i ​ 𝐮 OPEN 2 ​ i) ​ ( t, r, s, ϵ) ⋅ 𝐖 ~ ϵ ​ ( t) ​ 𝑑 t. \displaystyle\int_{J_{\epsilon}}\chi_{\epsilon}(t)\sum_{i=0}^{2}(-1)^{i}\mathbf{u}^{2i)}(t;r,s,\epsilon)\cdot\tilde{\mathbf{W}}_{\epsilon}(t)\,dt. |  |

By the second part of Proposition 4.17, if α ⁡ ( ϵ) \alpha(\epsilon) is chosen sufficiently small, we can conclude that

(5.37) |  | ∂ N ∂ s N | s = s ⁡ ( ϵ) ​ [Div ⁡ ( 𝐮 ⁡ ( α ⁡ ( ϵ), r, s, ϵ)) ​ 𝐮 ′ ​ ( α ⁡ ( ϵ), r, s, ϵ) ⟂ ⋅ 𝐖 ~ ϵ] \displaystyle\left.\frac{\partial^{N}}{\partial s^{N}}\right|_{s=s(\epsilon)}[\operatorname{Div}(\mathbf{u}(\alpha(\epsilon);r,s,\epsilon))\mathbf{u}^{\prime}(\alpha(\epsilon);r,s,\epsilon)^{\perp}\cdot\tilde{\mathbf{W}}_{\epsilon}] |  |

 | − ϵ k ϵ ∂ N ∂ s N | s = s ⁡ ( ϵ) ∑ i = 0 2 ( − 1) i 𝐮 OPEN 2 ​ i) ( α ( ϵ); r, s, ϵ) ⋅ 𝐖 ~ ϵ → 0. \displaystyle-\frac{\epsilon}{k_{\epsilon}}\left.\frac{\partial^{N}}{\partial s^{N}}\right|_{s=s(\epsilon)}\sum_{i=0}^{2}(-1)^{i}\mathbf{u}^{2i)}(\alpha(\epsilon);r,s,\epsilon)\cdot\tilde{\mathbf{W}}_{\epsilon}\to 0. |  |

We would like to argue that this vanishing limit contradicts the choice of the degree for polynomials P ϵ ​ ( s) P_{\epsilon}(s) made in ( 5.35).

Again, because of smoothness,

 | OPEN 𝐮 ⁡ ( α ⁡ ( ϵ), r, s, ϵ)) = 𝐮 ⁡ ( 0, r, s, ϵ) + α ⁡ ( ϵ) ​ 𝐮 ′ ​ ( 0, r, s, ϵ) + α ​ ( ϵ) 2 ​ 𝐑 ​ ( t, r, s, ϵ), \displaystyle\mathbf{u}(\alpha(\epsilon);r,s,\epsilon))=\mathbf{u}(0;r,s,\epsilon)+\alpha(\epsilon)\mathbf{u}^{\prime}(0;r,s,\epsilon)+\alpha(\epsilon)^{2}\mathbf{R}(t;r,s,\epsilon), |  |

 | OPEN 𝐮 ′ ​ ( α ⁡ ( ϵ), r, s, ϵ)) = 𝐮 ′ ​ ( 0, r, s, ϵ) + α ⁡ ( ϵ) ​ 𝐮 ′′ ​ ( 0, r, s, ϵ) + α ​ ( ϵ) 2 ​ 𝐑 ′ ​ ( t, r, s, ϵ) \displaystyle\mathbf{u}^{\prime}(\alpha(\epsilon);r,s,\epsilon))=\mathbf{u}^{\prime}(0;r,s,\epsilon)+\alpha(\epsilon)\mathbf{u}^{\prime\prime}(0;r,s,\epsilon)+\alpha(\epsilon)^{2}\mathbf{R}^{\prime}(t;r,s,\epsilon) |  |

with bounded remainders

 | 𝐑 ⁡ ( t, r, s, ϵ), 𝐑 ′ ​ ( t, r, s, ϵ) \mathbf{R}(t;r,s,\epsilon),\quad\mathbf{R}^{\prime}(t;r,s,\epsilon) |  |

in the domain where variables move. Even more explicitly

 | OPEN 𝐮 ⁡ ( α ⁡ ( ϵ), r, s, ϵ)) = 𝐩 + r ​ 𝐪 ⟂ + α ⁡ ( ϵ) ​ ( 𝐪 + s ​ 𝐪 ⟂) + α ​ ( ϵ) 2 ​ 𝐑 ​ ( t, r, s, ϵ), \displaystyle\mathbf{u}(\alpha(\epsilon);r,s,\epsilon))=\mathbf{p}+r\mathbf{q}^{\perp}+\alpha(\epsilon)(\mathbf{q}+s\mathbf{q}^{\perp})+\alpha(\epsilon)^{2}\mathbf{R}(t;r,s,\epsilon), |  |

 | OPEN 𝐮 ′ ​ ( α ⁡ ( ϵ), r, s, ϵ)) = ( 𝐪 + s ​ 𝐪 ⟂) + α ⁡ ( ϵ) ​ 𝐮 ′′ ​ ( 0, r, s, ϵ) + α ​ ( ϵ) 2 ​ 𝐑 ′ ​ ( t, r, s, ϵ). \displaystyle\mathbf{u}^{\prime}(\alpha(\epsilon);r,s,\epsilon))=(\mathbf{q}+s\mathbf{q}^{\perp})+\alpha(\epsilon)\mathbf{u}^{\prime\prime}(0;r,s,\epsilon)+\alpha(\epsilon)^{2}\mathbf{R}^{\prime}(t;r,s,\epsilon). |  |

If we take these expressions into the partial derivatives in ( 5.37), and recall ( 5.36), we see that the first term becomes

 | ∂ N ∂ s N | s = s ⁡ ( ϵ) ​ 1 α ​ ( ϵ) N ​ [Div ⁡ ( 𝐩 + r ​ 𝐪 ⟂ + α ⁡ ( ϵ) ​ ( 𝐪 + s ​ 𝐪 ⟂) + α ​ ( ϵ) 2 ​ 𝐑 ​ ( t, r, s, ϵ))] \displaystyle\left.\frac{\partial^{N}}{\partial s^{N}}\right|_{s=s(\epsilon)}\frac{1}{\alpha(\epsilon)^{N}}[\operatorname{Div}(\mathbf{p}+r\mathbf{q}^{\perp}+\alpha(\epsilon)(\mathbf{q}+s\mathbf{q}^{\perp})+\alpha(\epsilon)^{2}\mathbf{R}(t;r,s,\epsilon))] |  |

 | [( 𝐪 + s ​ 𝐪 ⟂) ⟂ + α ⁡ ( ϵ) ​ 𝐮 ′′ ​ ( 0, r, s, ϵ) ⟂ + α ​ ( ϵ) 2 ​ 𝐑 ′ ​ ( t, r, s, ϵ) ⟂] ⋅ 𝐪 ⟂ \displaystyle[(\mathbf{q}+s\mathbf{q}^{\perp})^{\perp}+\alpha(\epsilon)\mathbf{u}^{\prime\prime}(0;r,s,\epsilon)^{\perp}+\alpha(\epsilon)^{2}\mathbf{R}^{\prime}(t;r,s,\epsilon)^{\perp}]\cdot\mathbf{q}^{\perp} |  |

or

 | ∂ N ∂ s N | s = s ⁡ ( ϵ) ​ 1 α ​ ( ϵ) N ​ [Div ⁡ ( 𝐩 + r ​ 𝐪 ⟂ + α ⁡ ( ϵ) ​ ( 𝐪 + s ​ 𝐪 ⟂) + α ​ ( ϵ) 2 ​ 𝐑 ​ ( t, r, s, ϵ))] \displaystyle\left.\frac{\partial^{N}}{\partial s^{N}}\right|_{s=s(\epsilon)}\frac{1}{\alpha(\epsilon)^{N}}[\operatorname{Div}(\mathbf{p}+r\mathbf{q}^{\perp}+\alpha(\epsilon)(\mathbf{q}+s\mathbf{q}^{\perp})+\alpha(\epsilon)^{2}\mathbf{R}(t;r,s,\epsilon))] |  |

 | [| 𝐪 | 2 + ( α ⁡ ( ϵ) ​ 𝐮 ′′ ​ ( 0, r, s, ϵ) ⟂ + α ​ ( ϵ) 2 ​ 𝐑 ′ ​ ( t, r, s, ϵ) ⟂) ⋅ 𝐪 ⟂]. \displaystyle[|\mathbf{q}|^{2}+(\alpha(\epsilon)\mathbf{u}^{\prime\prime}(0;r,s,\epsilon)^{\perp}+\alpha(\epsilon)^{2}\mathbf{R}^{\prime}(t;r,s,\epsilon)^{\perp})\cdot\mathbf{q}^{\perp}]. |  |

Because of the way the polynomials P ϵ P_{\epsilon} and their degree N N were selected in ( 5.35), on the one hand; and the freedom we have to choose α ⁡ ( ϵ) \alpha(\epsilon) converging to zero as rapidly as necessary, on the other, we see that the previous derivative will not vanish as ϵ → 0 \epsilon\to 0 since terms affected by a negative power of α ⁡ ( ϵ) \alpha(\epsilon) will vanish when differentiation is performed, while the coefficient corresponding to power s N s^{N} does not vanish, by our manner of choosing the degree N N in ( 5.35), and is independent of α ⁡ ( ϵ) \alpha(\epsilon) (and of ϵ \epsilon). The terms affected by the remainders 𝐑 \mathbf{R} will vanish too because of the presence of the higher power α ​ ( ϵ) 2 \alpha(\epsilon)^{2}. The second term in ( 5.37) does not spoil our argument because of the presence of ϵ \epsilon in front of it. This is easily checked. Note how the reason for the choice in ( 5.36) is to have that the additional variable s s in ( 𝐪 + s ​ 𝐪 ⟂) ⟂ ⋅ 𝐪 ⟂ (\mathbf{q}+s\mathbf{q}^{\perp})^{\perp}\cdot\mathbf{q}^{\perp} drops out.

This contradiction between ( 5.37) and polynomials in ( 5.35) enables us to conclude that there cannot be more than n − 1 n-1 branches of solutions

 | f ϵ ( r, s j ( ϵ, r)) = 0, j = 1, 2, …, n − 1. f_{\epsilon}(r,s_{j}(\epsilon,r))=0,\quad j=1,2,\dots,n-1. |  |

This is the end of the first step.

For the second step, fix one of those n − 1 n-1 branches

 | ( r, s j ​ ( r, ϵ)), 1 ≤ j ≤ n − 1, (r,s_{j}(r,\epsilon)),\quad 1\leq j\leq n-1, |  |

and put

(5.38) |  | 𝐮 j ​ ( t, r, ϵ) ≡ 𝐮 ⁡ ( t, r, s j ​ ( r, ϵ), ϵ), 𝐮 j ​ ( r, ϵ) = 𝐮 j ​ ( t, r, ϵ), \mathbf{u}_{j}(t;r,\epsilon)\equiv\mathbf{u}(t;r,s_{j}(r,\epsilon),\epsilon),\quad\mathbf{u}_{j}(r,\epsilon)=\mathbf{u}_{j}(t;r,\epsilon), |  |

for t ∈ [− 1 / 2, 1 / 2] t\in[-1/2,1/2], and small r r and ϵ \epsilon. We go back to the family of functions in ( 5.33) setting s = s j ​ ( r, ϵ) s=s_{j}(r,\epsilon), to define the smooth functions

(5.39) |  | f j, ϵ ​ ( r) = ∫ J ϵ χ ϵ ​ ( t) ​ Div ⁡ ( 𝐮 j ​ ( r, ϵ)) ​ 𝐮 j ′ ​ ( r, ϵ) ⟂ ⋅ 𝐖 ~ ϵ ​ 𝑑 t − ϵ k ϵ ​ ⟨ 𝐮 j ​ ( r, ϵ), 𝐖 ϵ ⟩ − 1 k ϵ ​ ⟨ 𝐯 0, 𝐖 ϵ ⟩. f_{j,\epsilon}(r)=\int_{J_{\epsilon}}\chi_{\epsilon}(t)\operatorname{Div}(\mathbf{u}_{j}(r,\epsilon))\mathbf{u}^{\prime}_{j}(r,\epsilon)^{\perp}\cdot\tilde{\mathbf{W}}_{\epsilon}\,dt-\frac{\epsilon}{k_{\epsilon}}\langle\mathbf{u}_{j}(r,\epsilon),\mathbf{W}_{\epsilon}\rangle-\frac{1}{k_{\epsilon}}\langle\mathbf{v}_{0},\mathbf{W}_{\epsilon}\rangle. |  |

This time however, since we are looking for critical paths in Proposition 5.11, the value of test paths

 | 𝐖 ϵ = χ ϵ ​ 𝐖 ~ ϵ \mathbf{W}_{\epsilon}=\chi_{\epsilon}\tilde{\mathbf{W}}_{\epsilon} |  |

need not vanish at t = 0 t=0, and hence mollifier χ ϵ \chi_{\epsilon} can be taken to be even and with support [− α ⁡ ( ϵ), α ⁡ ( ϵ)] [-\alpha(\epsilon),\alpha(\epsilon)] with α ⁡ ( ϵ) \alpha(\epsilon), as in the first step, at our disposal. Our goal is, again, to argue that for each fixed j j, the family of functions f j, ϵ ​ ( r) f_{j,\epsilon}(r) in ( 5.39) cannot have more than n − 1 n-1 branches of roots as ϵ → 0 \epsilon\to 0. If we succeed in showing this, our claim in the theorem will be proved.

Our job, after the first step, is now much easier. We follow exactly along the same lines. Consider the polynomial

 | P ⁡ ( r) = Div ⁡ ( 𝐩 + r ​ 𝐪 ⟂) P(r)=\operatorname{Div}(\mathbf{p}+r\mathbf{q}^{\perp}) |  |

whose degree N N is at most n − 1 n-1. Take, almost as above,

 | 𝐖 ~ ϵ ​ ( t) ≡ 𝐪 ⟂, 𝐖 ϵ = χ ϵ ​ ( t) ​ 𝐖 ~ ϵ. \tilde{\mathbf{W}}_{\epsilon}(t)\equiv\mathbf{q}^{\perp},\quad\mathbf{W}_{\epsilon}=\chi_{\epsilon}(t)\tilde{\mathbf{W}}_{\epsilon}. |  |

Suppose that there could be N + 1 N+1 roots r i, j ​ ( ϵ) r_{i,j}(\epsilon), converging to zero as ϵ → 0 \epsilon\to 0, of f j, ϵ f_{j,\epsilon}, i.e.

 | f j, ϵ ( r i, j ( ϵ)) = 0, i = 1, 2, …, N, N + 1. f_{j,\epsilon}(r_{i,j}(\epsilon))=0,\quad i=1,2,\dots,N,N+1. |  |

Recall that j j is fixed. Due to smoothness, there should be, at least, one root r j ​ ( ϵ) r_{j}(\epsilon) of the N N -th derivative

 | f j, ϵ OPEN N) ​ ( r j ​ ( ϵ)) = 0, r j ​ ( ϵ) → 0 ​ as ​ ϵ → 0. f^{N)}_{j,\epsilon}(r_{j}(\epsilon))=0,\quad r_{j}(\epsilon)\to 0\hbox{ as }\epsilon\to 0. |  |

Through ( 5.39), we can write

 | ∫ J ϵ χ ϵ ​ ( t) ​ d N d ​ r N | r = r j ​ ( ϵ) ​ Div ⁡ ( 𝐮 j ​ ( r, ϵ)) ​ 𝐮 j ′ ​ ( r, ϵ) ⟂ ⋅ 𝐖 ~ ϵ ​ 𝑑 t \displaystyle\int_{J_{\epsilon}}\chi_{\epsilon}(t)\left.\frac{d^{N}}{dr^{N}}\right|_{r=r_{j}(\epsilon)}\operatorname{Div}(\mathbf{u}_{j}(r,\epsilon))\mathbf{u}^{\prime}_{j}(r,\epsilon)^{\perp}\cdot\tilde{\mathbf{W}}_{\epsilon}\,dt |  |

 | − ϵ k ϵ ​ d N d ​ r N | r = r j ​ ( ϵ) ​ ⟨ 𝐮 j ​ ( r, ϵ), 𝐖 ϵ ⟩ = 0. \displaystyle-\frac{\epsilon}{k_{\epsilon}}\left.\frac{d^{N}}{dr^{N}}\right|_{r=r_{j}(\epsilon)}\langle\mathbf{u}_{j}(r,\epsilon),\mathbf{W}_{\epsilon}\rangle=0. |  |

We focus on the important first term, since the second is tackled as in the first step through the first part of Proposition 4.17, to conclude that its limit, as ϵ → 0 \epsilon\to 0, vanishes as well. In this case, by selecting α ⁡ ( ϵ) \alpha(\epsilon) appropriately, we conclude that

 | d N d ​ r N | r = r j ​ ( ϵ) ​ Div ⁡ ( 𝐮 j ​ ( 0, r, ϵ)) ​ 𝐮 j ′ ​ ( 0, r, ϵ) ⟂ ⋅ 𝐪 ⟂ → 0. \left.\frac{d^{N}}{dr^{N}}\right|_{r=r_{j}(\epsilon)}\operatorname{Div}(\mathbf{u}_{j}(0;r,\epsilon))\mathbf{u}^{\prime}_{j}(0;r,\epsilon)^{\perp}\cdot\mathbf{q}^{\perp}\to 0. |  |

But, taking into account ( 5.38),

 | 𝐮 j ( 0; r, ϵ)) = 𝐩 + r 𝐪 ⟂, 𝐮 j ′ ( 0; r, ϵ)) = 𝐪 + s j ( r, ϵ) 𝐪 ⟂, \mathbf{u}_{j}(0;r,\epsilon))=\mathbf{p}+r\mathbf{q}^{\perp},\quad\mathbf{u}^{\prime}_{j}(0;r,\epsilon))=\mathbf{q}+s_{j}(r,\epsilon)\mathbf{q}^{\perp}, |  |

and the previous derivative becomes

 | d N d ​ r N | r = r j ​ ( ϵ) ​ Div ⁡ ( 𝐩 + r ​ 𝐪 ⟂) ​ ( 𝐪 + s j ​ ( r, ϵ) ​ 𝐪 ⟂) ⟂ ⋅ 𝐪 ⟂ = | 𝐪 | 2 ​ d N d ​ r N | r = r j ​ ( ϵ) ​ P ​ ( r). \left.\frac{d^{N}}{dr^{N}}\right|_{r=r_{j}(\epsilon)}\operatorname{Div}(\mathbf{p}+r\mathbf{q}^{\perp})(\mathbf{q}+s_{j}(r,\epsilon)\mathbf{q}^{\perp})^{\perp}\cdot\mathbf{q}^{\perp}=|\mathbf{q}|^{2}\left.\frac{d^{N}}{dr^{N}}\right|_{r=r_{j}(\epsilon)}P(r). |  |

The condition

 | d N d ​ r N | r = r j ​ ( ϵ) ​ P ​ ( r) → 0 \left.\frac{d^{N}}{dr^{N}}\right|_{r=r_{j}(\epsilon)}P(r)\to 0 |  |

as ϵ → 0 \epsilon\to 0 is impossible for a true polynomial of degree N N. This is the contradiction, and the end of our proof. ∎

### 5.8. Another form to deal with asymptotic behaviors of critical paths

The localized way in which we have dealt with multiplicity in the previous section, permits to argue about our upper bound without Lemma 5.15.

By Lemma 5.14, we have that for sequences of critical paths

 | 𝐮 ϵ = ( x ϵ, y ϵ), \mathbf{u}_{\epsilon}=(x_{\epsilon},y_{\epsilon}), |  |

we know that

 | ( Z ϵ 2) ′ → 0, Z ϵ 2 ​ Div ϵ → 0. (Z_{\epsilon}^{2})^{\prime}\to 0,\quad Z_{\epsilon}^{2}\operatorname{Div}_{\epsilon}\to 0. |  |

Since we are interested in those families of critical paths for which Z ϵ 2 Z_{\epsilon}^{2} stays uniformly away from zero, we can conclude that

 | Div ϵ → 0, Z ϵ 2 − k ϵ 2 → 0, \operatorname{Div}_{\epsilon}\to 0,\quad Z_{\epsilon}^{2}-k_{\epsilon}^{2}\to 0, |  |

for a family of constants k ϵ k_{\epsilon}, uniformly away from zero. These two convergences suffice to go back to the beginning of Section 5.7, and start with the discussion there exactly in the same terms with limit point, and corresponding tangent vector,

 | 𝐩 ∈ { Div = 0 }, 𝐪, tangent to { Div = 0 } at 𝐩, \mathbf{p}\in\{\operatorname{Div}=0\},\quad\mathbf{q},\hbox{ tangent to }\{\operatorname{Div}=0\}\hbox{ at }\mathbf{p}, |  |

respectively, to conclude that there cannot be more than ( n − 1) 2 (n-1)^{2} critical paths

 | 𝐮 ϵ, i, j, i, j ∈ { 1, 2, …, n − 1 }, \mathbf{u}_{\epsilon,i,j},\quad i,j\in\{1,2,\dots,n-1\}, |  |

with

 | 𝐮 ϵ, i, j ​ ( 0) → 𝐩, 𝐮 ϵ, i, j ′ ​ ( 0) → 𝐪, \mathbf{u}_{\epsilon,i,j}(0)\to\mathbf{p},\quad\mathbf{u}^{\prime}_{\epsilon,i,j}(0)\to\mathbf{q}, |  |

regardless of the limit of their full images. If some of these images go over contact points, that would mean less critical paths. The maximum possible number is the one counted through Theorem 5.16, and this would lead to the same upper bound.

### 5.9. Counting method

Once we have proved all of the main preceding steps, it is easy to describe how to organize the counting procedure for an upper bound of the number M c ​ r ​ i M_{cri} in Problem 2.6. We will express our bound in terms of the following parameters, in addition to the degree n n of the system:

- •

M M: the number of connected components of the curve Div = 0 \operatorname{Div}=0;

- •

N N: the number of contact points of the differential system.

###### Theorem 5.18.

Under the assumptions and notation of Theorem 1.1 and Problem 2.6,

 | M c ​ r ​ i ≤ ( n − 1) 2 ​ ( M + N), M_{cri}\leq(n-1)^{2}(M+N), |  |

and so our differential system cannot have more than

 | 1 + ( n − 1) 2 ​ ( M + N) 1+(n-1)^{2}(M+N) |  |

limit cycles.

###### Proof.

From Theorem 5.16, we must compute the maximum number of limit behaviors which are contained in the components of the curve Div = 0 \operatorname{Div}=0.

Let L ≥ 0 L\geq 0 be the number of connected components of Div = 0 \operatorname{Div}=0 homeomorphic to a straight line. Assume that the connected component i i, for i ∈ { 0, 1, …, L }, i\in\{0,1,\ldots,L\}, contains x i ≥ 0 x_{i}\geq 0 contact points ( x 0 = 0 x_{0}=0 always). Then it can have at most x i + 1 x_{i}+1 limit behaviors. Therefore the number of limit critical closed paths contained in the components of Div = 0 \operatorname{Div}=0 homeomorphic to a straight line is at most L + ∑ i = 0 L x i. L+\sum_{i=0}^{L}x_{i}.

Let O ≥ 0 O\geq 0 be the number of connected components of Div = 0 \operatorname{Div}=0 homeomorphic to an oval. Suppose y j ≥ 0 y_{j}\geq 0 is the number of contact points in the j j -th component, for j ∈ { 0, 1, …, O } j\in\{0,1,\ldots,O\}. Note that y 0 = 0 y_{0}=0 always. Then we can have at most ∑ j = 0 O y j \sum_{j=0}^{O}y_{j} different limit behaviors, all of which are bounded.

In summary, the number of limit critical closed paths contained in the components of Div = 0 \operatorname{Div}=0 is at most

 | L + ∑ i = 0 L x i + ∑ j = 0 O y j ≤ M + N. L+\sum_{i=0}^{L}x_{i}+\sum_{j=0}^{O}y_{j}\leq M+N. |  |

By Theorem 5.17, each such possible limit behavior must be multiplied by the corresponding multiplicity factor ( n − 1) 2 (n-1)^{2}. Hence, we will have at most

 | 1 + ( n − 1) 2 ​ ( M + N) 1+(n-1)^{2}(M+N) |  |

critical closed paths of E ϵ E_{\epsilon} for every ϵ \epsilon sufficiently small. ∎

Note that in fact, the upper bound can be slightly improved to

 | 1 + ( n − 1) 2 ​ ( L + N) 1+(n-1)^{2}(L+N) |  |

where L L is the number of connected components of the curve Div = 0 \operatorname{Div}=0 homeomorphic to a line.

### 5.10. Non-generic situation

In this final section we treat the case of polynomial differential systems ( 1.1) for which either the curve Div = 0 \operatorname{Div}=0 has singular points, i.e. the system

(5.40) |  | P x ​ x + Q y ​ x = P x ​ y + Q y ​ y = 0, P x + Q y = 0 P_{xx}+Q_{yx}=P_{xy}+Q_{yy}=0,\quad P_{x}+Q_{y}=0 |  |

has some solutions; our initial differential system ( 1.1) has non-countable, infinitely many contact points, i.e. system ( 1.2) has a continuum of solutions; or there are multiple solutions to the same system. Note that equations ( 5.40) and ( 1.2) involve the partial derivatives of Div \operatorname{Div}. Our argument revolves around the idea that vector fields 𝐅 \mathbf{F} for such systems can be uniformly approximated by a sequence 𝐅 δ \mathbf{F}_{\delta} of non-singular polynomial vector fields without increasing the degree, and in such a way that the divergence curve for 𝐅 δ \mathbf{F}_{\delta} has no singularities, and finitely many simple contact points with system ( 1.1).

We can definitely apply our previous results to the family of functionals

 | E ϵ, δ ( 𝐮) = ∫ 0 1 \displaystyle E_{\epsilon,\delta}(\mathbf{u})=\int_{0}^{1} | [1 2 ( 𝐅 δ ⟂ ( 𝐮 ( t)) ⋅ 𝐮 ′ ( t)) 2 + ϵ 2 ( | 𝐮 ′′ ( t) | 2 + | 𝐮 ′ ( t) | 2 + | 𝐮 ( t) | 2) \displaystyle\left[\frac{1}{2}(\mathbf{F}^{\perp}_{\delta}(\mathbf{u}(t))\cdot\mathbf{u}^{\prime}(t))^{2}+\frac{\epsilon}{2}(|\mathbf{u}^{\prime\prime}(t)|^{2}+|\mathbf{u}^{\prime}(t)|^{2}+|\mathbf{u}(t)|^{2})\right. |  |

 |  | + ( 𝐮 ⁡ ( t) ⋅ 𝐯 δ ​ ( t) + 𝐮 ′ ​ ( t) ⋅ 𝐯 δ ′ ​ ( t) + 𝐮 ′′ ​ ( t) ⋅ 𝐯 δ ′′ ​ ( t)) \displaystyle\left.+(\mathbf{u}(t)\cdot\mathbf{v}_{\delta}(t)+\mathbf{u}^{\prime}(t)\cdot\mathbf{v}^{\prime}_{\delta}(t)+\mathbf{u}^{\prime\prime}(t)\cdot\mathbf{v}^{\prime\prime}_{\delta}(t))\right. |  |

 |  | 1 2 ​ ϵ ( | 𝐯 δ ′′ ( t) | 2 + | 𝐯 δ ′ ( t) | 2 + | 𝐯 δ ( t) | 2)] d t, \displaystyle\left.\frac{1}{2\epsilon}(|\mathbf{v}^{\prime\prime}_{\delta}(t)|^{2}+|\mathbf{v}^{\prime}_{\delta}(t)|^{2}+|\mathbf{v}_{\delta}(t)|^{2})\right]\,dt, |  |

where the dependence of the smooth paths 𝐯 δ \mathbf{v}_{\delta} on δ \delta is as regular as necessary. It is clear that the convergence

 | E ϵ, δ → E ϵ ​ as ​ δ → 0, E_{\epsilon,\delta}\to E_{\epsilon}\hbox{ as }\delta\to 0, |  |

takes place in the Haussdorf sense since parameter δ \delta is only involved in lower-order terms ( ϵ \epsilon is fixed in this argument).

Our first relevant observation is that the discussion in Subsection 2.4 is valid regardless of whether our initial differential system ( 1.1) is generic. This means that

 | H ( n) ≤ lim a → 0 lim ϵ → 0 #( { E ϵ ≤ a } ∩ 𝕆) H(n)\leq\lim_{a\to 0}\lim_{\epsilon\to 0}\#(\{E_{\epsilon}\leq a\}\cap\mathbb{O}) |  |

where, as usual

 | #( { E ϵ ≤ a } ∩ 𝕆) \#(\{E_{\epsilon}\leq a\}\cap\mathbb{O}) |  |

designates the number of connected components of the corresponding set. Because of the announced convergence E ϵ, δ → E ϵ E_{\epsilon,\delta}\to E_{\epsilon}, we would also have the convergence

 | { E ϵ, δ ≤ a } → { E ϵ ≤ a }, δ → 0, \{E_{\epsilon,\delta}\leq a\}\to\{E_{\epsilon}\leq a\},\quad\delta\to 0, |  |

in the Hausdorff distance for bounded sets. The operator #\#, number of connected components of sub-level sets, is lower semicontinuous with respect to this convergence, and hence

 | #( { E ϵ ≤ a } ∩ 𝕆) ≤ lim δ → 0 #( { E ϵ, δ ≤ a } ∩ 𝕆). \#(\{E_{\epsilon}\leq a\}\cap\mathbb{O})\leq\lim_{\delta\to 0}\#(\{E_{\epsilon,\delta}\leq a\}\cap\mathbb{O}). |  |

In this way,

 | H ( n) ≤ lim a → 0 lim ϵ → 0 #( { E ϵ ≤ a } ∩ 𝕆) ≤ lim a → 0 lim ϵ → 0 lim δ → 0 #( { E ϵ, δ ≤ a } ∩ 𝕆). H(n)\leq\lim_{a\to 0}\lim_{\epsilon\to 0}\#(\{E_{\epsilon}\leq a\}\cap\mathbb{O})\leq\lim_{a\to 0}\lim_{\epsilon\to 0}\lim_{\delta\to 0}\#(\{E_{\epsilon,\delta}\leq a\}\cap\mathbb{O}). |  |

If approximating polynomials 𝐅 δ \mathbf{F}_{\delta} are generic, all of our work implies that

 | lim a → 0 lim ϵ → 0 lim δ → 0 #( { E ϵ, δ ≤ a } ∩ 𝕆) ≤ C ( n) \lim_{a\to 0}\lim_{\epsilon\to 0}\lim_{\delta\to 0}\#(\{E_{\epsilon,\delta}\leq a\}\cap\mathbb{O})\leq C(n) |  |

where C ⁡ ( n) C(n) is our upper bound for generic polynomial vector fields of degree n n, and we have the same bound in terms of the degree of the system for a non-generic differential vector field 𝐅 \mathbf{F}.

Notice that we are not claiming anything about the relationship between limit cycles of 𝐅 \mathbf{F} and limit cycles of 𝐅 δ \mathbf{F}_{\delta}, and their relative positions, or of critical closed paths for E ϵ E_{\epsilon} and of E ϵ, δ E_{\epsilon,\delta}.

## References

- [1] V.I. Arnold, Loss of stability of self–oscillations close to resonance and versal deformations of equivariant vector fields, Funct. Anal. Appl. 11 (1977), 85–92.
- [2] V.I. Arnold, Geometric Methods in Theory of Ordinary Differential Equations, Springer–Verlag, New York, 1983.
- [3] R. Bamon, Quadratic vector fields in the plane have a finite number of limit cycles, Int. Hautes Études Sci. Publ. Math. 64 (1986), 111–142.
- [4] M.S. Berger, Nonlinearity and Functional Analysis, Academic Press, New York, 1977.
- [5] G. Binyamini, D. Novikov and S. Yakovenko, On the number of zeros of Abelian integrals, Invent. Math. 181 (2010), 227–289.
- [6] A. Braides, Γ \Gamma -convergence for beginners. Oxford Lecture Series in Mathematics and its Applications, 22. Oxford University Press, Oxford, 2002.
- [7] H. Brézis, Functional Analysis, Sobolev Spaces, and Partial Differential Equations, Universitext, Springer, 2010.
- [8] M. Caubergh, F. Dumortier, Hilbert’s 16th problem for classical Liénard equations of even degree. J. Differential Equations 244 (2008), no. 6, 1359–1394.
- [9] K-c. Chang, Infinite Dimensional Morse Theory and Multiple Solution Problems, Prog. Nonlin. Diff. Eq. Their Appl., 6, Birkhäuser, Boston, 1993.
- [10] L.S. Chen and M.S. Wang, The relative position, and the number, of limit cycles of a quadratic differential system, Acta Math. Sinica 22 (1979), 751–758.
- [11] C. Christopher and C. Li, Limit cycles of differential equations, Advanced Courses in Mathematics, CRM Barcelona, Birkhäuser Verlag, Basel, 2007.
- [12] C.J. Christopher and N.G. Lloyd, Polynomial systems: A lower bound for the Hilbert numbers, Proc. Royal Soc. London Ser. A450 (1995), 219–224.
- [13] G. Dal Maso, An introduction to Γ \Gamma -convergence. Progress in Nonlinear Differential Equations and their Applications, 8. Birkhäuser Boston, Inc., Boston, MA, 1993.
- [14] F. Dumortier, J. Llibre and J.C. Artés, Qualitative theory of planar differential systems, UniversiText, Springer–Verlag, New York, 2006.
- [15] H. Dulac, Sur les cycles limites, Bull. Soc. Math. France 51 (1923), 45–188.
- [16] F. Dumortier, M. El Morsalani, C. Rousseau, Hilbert’s 16th problem for quadratic systems and cyclicity of elementary graphics. Nonlinearity 9 (1996), no. 5, 1209–1261.
- [17] F. Dumortier, R. Roussarie, C. Rousseau, Hilbert’s 16th problem for quadratic vector fields. J. Differential Equations 110 (1994), no. 1, 86–133.
- [18] J. Écalle, Introduction aux fonctions analysables et preuve constructive de la conjecture de Dulac, Hermann, 1992.
- [19] W. Fulton, Algebraic Curves, Mathematics Lecture Note Series, W.A. Benjamin, 1974.
- [20] H. Giacomini, J. Llibre and M. Viano, On the nonexistence, existence and uniqueness of limit cycles, Nonlinearity 9 (1996), 501–516.
- [21] D.A. Gudkov, The topology of real projective algebraic varieties, Russian Math. Surveys 29:4 (1974), 1–79.
- [22] M. Han and J. Li, Lower bounds for the Hilbert number of polynomial systems, J. Diff. Eq. 252 (2012), 3278–3304.
- [23] D. Hilbert, Mathematische Probleme, Lecture, Second Internat. Congr. Math. (Paris, 1900), Nachr. Ges. Wiss. G”ottingen Math. Phys. KL. (1900), 253–297; English transl., Bull. Amer. Math. Soc. 8 (1902), 437–479; Bull. (New Series) Amer. Math. Soc. 37 (2000), 407–436.
- [24] Yu. Ilyashenko, Dulac’s memoir “On limit cycles” and related problems of the local theory of differential equations, Russian Math. Surveys 40 (1985), 1–49.
- [25] Yu. Ilyashenko, Finiteness theorems for limit cycles, Translations of Math. Monographs 94, Amer. Math. Soc., 1991.
- [26] Yu. Ilyashenko, Centennial history of Hilbert’s 16 16 th problem, Bull. (New Series) Amer. Math. Soc. 39 (2002), 301–354.
- [27] V. Kaloshin, Around the Hilbert–Arnol0d problem, On finiteness in differential equations and Diophantine geometry, CRM Monogr. Ser. 24, Amer. Math. Soc., Providence, RI, 2005, pp. 111–162.
- [28] J. Li, Hilbert’s 16 16 th problem and bifurcations of planar polynomial vector fields, Internat. J. Bifur. Chaos Appl. Sci. Engrg. 13 (2003), 47–106.
- [29] A. Lins, W. de Melo, C. C. Pugh, On Liénard’s equation. Geometry and topology (Proc. III Latin Amer. School of Math., Inst. Mat. Pura Aplicada CNPq, Rio de Janeiro, 1976), pp. 335–357. Lecture Notes in Math., Vol. 597, Springer, Berlin, 1977.
- [30] J. Llibre, Integrability of polynomial differential systems, Handbook of Differential Equations, Ordinary Differential Equations, Eds. A. Cañada, P. Drabek and A. Fonda, Elsevier (2004), pp. 437–533.
- [31] J. Llibre, R. Ramírez and N. Sadovskaia, On the 16 16 th Hilbert problem for algebraic limit cycles, J. Differential Equations 248 (2010), 1401–1409.
- [32] J. Llibre, R. Ramírez and N. Sadovskaia, On the 16th Hilbert problem for limit cycles on nonsingular algebraic curves, J. Differential Equations 250 (2010), 983–999.
- [33] J. Llibre and G. Rodríguez, Configurations of limit cycles and planar polynomial vector fields, J. of Differential Equations 198 (2004), 374–380.
- [34] N.G. Lloyd, Limit cycles of polynomial systems, some recent developments, in New Directions in Dynamical Systems, ed. T. Bedford & J. Swift, London Math. Soc. Lecture Notes, Vol. 127, 1988, pp. 192–234.
- [35] R.E. O’Malley, Singular Perturbation Methods for Ordinary Differential Equations, Appl. Math. Sciences 89, Springer–Verlag, New York, 1991.
- [36] I.G. Petrovskii and E.M. Landis, On the number of limit cycles of the equation d ​ y / d ​ x = P ⁡ ( x, y) / Q ⁡ ( x, y) dy/dx=P(x,y)/Q(x,y), where P P and Q Q are polynomials, Mat. Sb. N.S. 43 (1957), 149–168 (Russian), and Amer. Math. Soc. Transl. 14 (1960), 181–200.
- [37] I.G. Petrovskii and E.M. Landis, Corrections to the articles “On the number of limit cycles of the equation d ​ y / d ​ x = P ⁡ ( x, y) / Q ⁡ ( x, y) dy/dx=P(x,y)/Q(x,y), where P P and Q Q are polynomials” (Russian), Mat. Sb. N.S. 48 (1959), 255–263.
- [38] H. Poincaré, Sur les courbes définies par une équation différentielle, Oevres complètes, Vol. 1, 1928.
- [39] Rothe, E. H., Critical point theory in Hilbert space under general boundary conditions. J. Math. Anal. Appl. 11 (1965), 357–409.
- [40] Rothe, E. H., Critical point theory in Hilbert space under regular boundary conditions. J. Math. Anal. Appl. 36 (1971), 377–431.
- [41] Rothe, E. H., Morse theory in Hilbert space. Rocky Mountain J. Math. 3 (1973), 251–274.
- [42] C. Rousseau, Hilbert’s 16th problem for quadratic vector fields and cyclicity of graphics. Proceedings of the Second World Congress of Nonlinear Analysts, Part 1 (Athens, 1996). Nonlinear Anal. 30 (1997), no. 1, 437–445.
- [43] C. Rousseau, H. Zhu, PP-graphics with a nilpotent elliptic singularity in quadratic systems and Hilbert’s 16th problem. J. Differential Equations 196 (2004), no. 1, 169–208.
- [44] S. Schecter and F. Singer, A class of vertorfields on S 2 S^{2} that are topologically equivalent to polynomial vectorfields, J. Differential Equations 57 (1985), 406–435.
- [45] S. Shi, On limit cycles of plane quadratic systems, Sci. Sin. 25 (1982), 41–50.
- [46] S. Smale, Dynamics retrospective: great problems, attempts that failed. Nonlinear science: the next decade (Los Alamos, NM, 1990). Phys. D 51 (1991), no. 1-3, 267–273.
- [47] S. Smale, Mathematical problems for the next century, Math. Intelligencer 20 (1998), no. 2, 7–15.
- [48] B. Smits, Singular perturbations arising in Hilbert’s 16th problem for quadratic vector fields. ZAMM Z. Angew. Math. Mech. 78 (1998), no. 2, 133–136
- [49] J. Sotomayor, Curvas definidas por equaçoes diferenciais no plano (Portuguese), 13 13 th Brazilian Mathematics Colloquium, Instituto de Matemática Pura e Aplicada, Rio de Janeiro, 1981.
- [50] R. Sverdlove, Inverse problems for dynamical systems, J. Differential Equations 42 (1981), 72–105.
- [51] Whitney, H., On regular closed curves in the plane. Compositio Math. 4 (1937), 276–284.
- [52] R. Winkel, A transfer principle in the real plane from nonsingular algebraic curves to polynomial vector fields, Geom. Dedicata 79 (2000), 101–108.
- [53] S. Yakovenko, Quantitative theory of ordinary differential equations and the tangential Hilbert 16 16 th problem, On finiteness in differential equations and Diophantine geometry, CRM Monogr. Ser. 24, Amer. Math. Soc., Providence, RI, 2005, pp. 41–109,
- [54] X. Zhang, The 16 16 th Hilbert problem on algebraic limit cycles, J. Differential Equations 251 (2011), 1778–1789.

[◄][2][image: ar5iv homepage] [3]
[Feeling lucky?][4] [5]
[Conversion report][6]
[Report an issue][7]
[View original on arXiv][8] [►][9]


## Links

[1]: mailto:pablo.pedregal@uclm.es
[2]: /html/2103.07192
[3]: /
[4]: /feeling_lucky
[5]: /land_of_honey_and_milk
[6]: /log/2103.07193
[7]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2103.07193
[8]: https://arxiv.org/pdf/2103.07193
[9]: /html/2103.07194
