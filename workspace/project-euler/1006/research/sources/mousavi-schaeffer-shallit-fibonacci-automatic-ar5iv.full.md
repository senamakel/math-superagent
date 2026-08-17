<!-- source: https://ar5iv.labs.arxiv.org/html/1406.0670 | converted from HTML -->

[1406.0670] Decision Algorithms for Fibonacci-Automatic Words, with Applications to Pattern Avoidance

# Decision Algorithms for Fibonacci-Automatic Words, with Applications to Pattern Avoidance

Chen Fei Du Thanks: School of Computer Science, University of Waterloo, Waterloo, ON N2L 3G1, Canada;
cfdu@uwaterloo.ca, sh2mousa@uwaterloo.ca, shallit@uwaterloo.ca. Hamoon Mousavi Luke Schaeffer Thanks: Computer Science and Artificial Intelligence Laboratory, The Stata Center, MIT Building 32, 32 Vassar Street, Cambridge, MA 02139 USA; lrschaeffer@gmail.com. Jeffrey Shallit

###### Abstract

We implement a decision procedure for answering questions about a class of infinite words that might be called (for lack of a better name) “Fibonacci-automatic”. This class includes, for example, the famous Fibonacci word 𝐟 = 01001010 ⋯ {\bf f}=01001010\cdots, the fixed point of the morphism 0 → 01 0\rightarrow 01 and 1 → 0 1\rightarrow 0. We then recover many results about the Fibonacci word from the literature (and improve some of them), such as assertions about the occurrences in 𝐟 \bf f of squares, cubes, palindromes, and so forth. As an application of our method we prove a new result: there exists an aperiodic infinite binary word avoiding the pattern x ​ x ​ x R xxx^{R}. This is the first avoidability result concerning a nonuniform morphism proven purely mechanically.

## 1 Decidability

As is well-known, the logical theory Th ⁡ ( ℕ, +) \Th({\mathbb{N}},+), sometimes called Presburger arithmetic, is decidable [62, 63]. Büchi [18] showed that if we add the function V k ​ ( n) = k e V_{k}(n)=k^{e}, for some fixed integer k ≥ 2 k\geq 2, where e = max { i: k i | n } e=\max\{i\ :\ k^{i}\,|\,n\}, then the resulting theory is still decidable. This theory is powerful enough to define finite automata; for a survey, see [17].

As a consequence, we have the following theorem (see, e.g., [73]):

###### Theorem 1.

There is an algorithm that, given a proposition phrased using only the universal and existential quantifiers, indexing into one or more k k -automatic sequences, addition, subtraction, logical operations, and comparisons, will decide the truth of that proposition.

Here, by a k k -automatic sequence, we mean a sequence 𝐚 \bf a computed by deterministic finite automaton with output (DFAO) M = ( Q, Σ k, Δ, δ, q 0, κ) M=(Q,\Sigma_{k},\Delta,\delta,q_{0},\kappa). Here Σ k:= { 0, 1, …, k − 1 } \Sigma_{k}:=\{0,1,\ldots,k-1\} is the input alphabet, Δ \Delta is the output alphabet, and outputs are associated with the states given by the map κ: Q → Δ \kappa:Q\rightarrow\Delta in the following manner: if ( n) k (n)_{k} denotes the canonical expansion of n n in base k k, then 𝐚 ⁡ [n] = κ ⁡ ( δ ⁡ ( q 0, ( n) k)) {\bf a}[n]=\kappa(\delta(q_{0},(n)_{k})). The prototypical example of an automatic sequence is the Thue-Morse sequence 𝐭 = t 0 t 1 t 2 ⋯ {\bf t}=t_{0}t_{1}t_{2}\cdots, the fixed point (starting with 0 0) of the morphism 0 → 01 0\rightarrow 01, 1 → 10 1\rightarrow 10.

It turns out that many results in the literature about properties of automatic sequences, for which some had only long and involved proofs, can be proved purely mechanically using a decision procedure. It suffices to express the property as an appropriate logical predicate, convert the predicate into an automaton accepting representations of integers for which the predicate is true, and examine the automaton. See, for example, the recent papers [2, 44, 46, 45, 47]. Furthermore, in many cases we can explicitly enumerate various aspects of such sequences, such as subword complexity [25].

Beyond base k k, more exotic numeration systems are known, and one can define automata taking representations in these systems as input. It turns out that in the so-called Pisot numeration systems, addition is computable [42, 43], and hence a theorem analogous to Theorem 1 holds for these systems. See, for example, [16]. It is our contention that the power of this approach has not been widely appreciated, and that many results, previously proved using long and involved ad hoc techniques, can be proved with much less effort by phrasing them as logical predicates and employing a decision procedure. Furthermore, many enumeration questions can be solved with a similar approach.

We have implemented a decision algorithm for one such system; namely, Fibonacci representation. In this paper we report on our results obtained using this implementation. We have reproved many results in the literature purely mechanically, as well as obtained new results, using this implementation.

The paper is organized as follows. In Section 2, we briefly recall the details of Fibonacci representation. In Section 3 we report on our mechanical proofs of properties of the infinite Fibonacci word; we reprove many old results and we prove some new ones. In Section 4 we apply our ideas to prove results about the finite Fibonacci words. In Section 5 we study a special infinite word, the Rote-Fibonacci word, and prove many properties of it, including a new avoidability result. In Section 6 we look briefly at another sequence, the Fibonacci analogue of the Thue-Morse sequence. In Section 7 we apply our methods to another avoidability problem involving additive squares. In Section 8 we report on mechanical proofs of some enumeration results. Some details about our implementation are given in the last section.

## 2 Fibonacci representation

Let the Fibonacci numbers be defined, as usual, by F 0 = 0 F_{0}=0, F 1 = 1 F_{1}=1, and F n = F n − 1 + F n − 2 F_{n}=F_{n-1}+F_{n-2} for n ≥ 2 n\geq 2. (We caution the reader that some authors use a different indexing for these numbers.)

It is well-known, and goes back to Ostrowski [59], Lekkerkerker [55], and Zeckendorf [74], that every non-negative integer can be represented, in an essentially unique way, as a sum of Fibonacci numbers ( F i) i ≥ 2 (F_{i})_{i\geq 2}, subject to the constraint that no two consecutive Fibonacci numbers are used. For example, 43 = F 9 + F 6 + F 2 43=F_{9}+F_{6}+F_{2}. Also see [19, 38].

Such a representation can be written as a binary string a 1 a 2 ⋯ a n a_{1}a_{2}\cdots a_{n} representing the integer ∑ 1 ≤ i ≤ n a i ​ F n + 2 − i \sum_{1\leq i\leq n}a_{i}F_{n+2-i}. For example, the binary string 10010001 10010001 is the Fibonacci representation of 43 43.

For w = a 1 a 2 ⋯ a n ∈ Σ 2 ∗ w=a_{1}a_{2}\cdots a_{n}\in\Sigma_{2}^{*}, we define [a 1 a 2 ⋯ a n] F:= ∑ 1 ≤ i ≤ n a i F n + 2 − i [a_{1}a_{2}\cdots a_{n}]_{F}:=\sum_{1\leq i\leq n}a_{i}F_{n+2-i}, even if a 1 a 2 ⋯ a n a_{1}a_{2}\cdots a_{n} has leading zeroes or consecutive 1 1 ’s. By ( n) F (n)_{F} we mean the canonical Fibonacci representation for the integer n n, having no leading zeroes or consecutive 1 1 ’s. Note that ( 0) F = ϵ (0)_{F}=\epsilon, the empty string. The language of all canonical representations of elements of ℕ {\mathbb{N}} is ϵ + 1 ​ ( 0 + 01) ∗ \epsilon+1(0+01)^{*}.

Just as Fibonacci representation is the analogue of base- k k representation, we can define the notion of Fibonacci-automatic sequence as the analogue of the more familiar notation of k k -automatic sequence [28, 4]. We say that an infinite word 𝐚 = ( a n) n ≥ 0 {\bf a}=(a_{n})_{n\geq 0} is Fibonacci-automatic if there exists an automaton with output M = ( Q, Σ 2, q 0, δ, κ, Δ) M=(Q,\Sigma_{2},q_{0},\delta,\kappa,\Delta) that a n = κ ⁡ ( δ ⁡ ( q 0, ( n) F)) a_{n}=\kappa(\delta(q_{0},(n)_{F})) for all n ≥ 0 n\geq 0. An example of a Fibonacci-automatic sequence is the infinite Fibonacci word,

 | 𝐟 = f 0 f 1 f 2 ⋯ = 01001010 ⋯ {\bf f}=f_{0}f_{1}f_{2}\cdots=01001010\cdots |  |

which is generated by the following 2-state automaton:

q 0 / 𝟶 q_{0}/{\tt 0} q 1 / 𝟷 q_{1}/{\tt 1} 0 1 0 Figure 1: Canonical Fibonacci representation DFAO generating the Fibonacci word

To compute f i f_{i}, we express i i in canonical Fibonacci representation, and feed it into the automaton. Then f i f_{i} is the output associated with the last state reached (denoted by the symbol after the slash). Another characterization of Fibonacci-automatic sequences can be found in [72].

A basic fact about Fibonacci representation is that addition can be performed by a finite automaton. To make this precise, we need to generalize our notion of Fibonacci representation to r r -tuples of integers for r ≥ 1 r\geq 1. A representation for ( x 1, x 2, …, x r) (x_{1},x_{2},\ldots,x_{r}) consists of a string of symbols z z over the alphabet Σ 2 r \Sigma_{2}^{r}, such that the projection π i ​ ( z) \pi_{i}(z) over the i i ’th coordinate gives a Fibonacci representation of x i x_{i}. Notice that since the canonical Fibonacci representations of the individual x i x_{i} may have different lengths, padding with leading zeroes will often be necessary. A representation for ( x 1, x 2, …, x r) (x_{1},x_{2},\ldots,x_{r}) is called canonical if it has no leading [0, 0, … ​ 0] [0,0,\ldots 0] symbols and the projections into individual coordinates have no occurrences of 11 11. We write the canonical representation as ( x 1, x 2, …, x r) F (x_{1},x_{2},\ldots,x_{r})_{F}. Thus, for example, the canonical representation for ( 9, 16) (9,16) is [0, 1] ​ [1, 0] ​ [0, 0] ​ [0, 1] ​ [0, 0] ​ [1, 0] [0,1][1,0][0,0][0,1][0,0][1,0].

Thus, our claim about addition in Fibonacci representation is that there exists a deterministic finite automaton (DFA) M add M_{\rm add} that takes input words of the form [0, 0, 0] ∗ ​ ( x, y, z) F [0,0,0]^{*}(x,y,z)_{F}, and accepts if and only if x + y = z x+y=z. Thus, for example, M add M_{\rm add} accepts [0, 0, 1] ​ [1, 0, 0] ​ [0, 1, 0] ​ [1, 0, 1] [0,0,1][1,0,0][0,1,0][1,0,1], since the three strings obtained by projection are 0101, 0010, 1001 0101,0010,1001, which represent, respectively, 4 4, 2 2, and 6 6 in Fibonacci representation. This result is apparently originally due to Berstel [6]; also see [7, 40, 41, 1].

Since this automaton does not appear to have been given explicitly in the literature and it is essential to our implementation, we give it here. The states of M add M_{\rm add} are Q = { 0, 1, 2, …, 16 } Q=\{0,1,2,\ldots,16\}, the input alphabet is Σ 2 × Σ 2 × Σ 2 \Sigma_{2}\times\Sigma_{2}\times\Sigma_{2}, the final states are F = { 1, 7, 11 } F=\{1,7,11\}, the initial state is q 0 = 1 q_{0}=1, and the transition function δ \delta is given below. The automaton is incomplete, with any unspecified transitions going to a non-accepting dead state that transitions to itself on all inputs. This automaton actually works even for non-canonical expansions having consecutive 1 1 ’s; an automaton working only for canonical expansions can easily be obtained by intersection with the appropriate regular languages. The state 0 0 is a “dead state” that can safely be ignored.

 | [0,0,0] | [0,0,1] | [0,1,0] | [0,1,1] | [1,0,0] | [1,0,1] | [1,1,0] | [1,1,1] |

0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

1 | 1 | 2 | 3 | 1 | 3 | 1 | 0 | 3 |

2 | 4 | 5 | 6 | 4 | 6 | 4 | 7 | 6 |

3 | 0 | 8 | 0 | 0 | 0 | 0 | 0 | 0 |

4 | 5 | 0 | 4 | 5 | 4 | 5 | 6 | 4 |

5 | 0 | 0 | 0 | 0 | 0 | 0 | 9 | 0 |

6 | 2 | 10 | 1 | 2 | 1 | 2 | 3 | 1 |

7 | 8 | 11 | 0 | 8 | 0 | 8 | 0 | 0 |

8 | 3 | 1 | 0 | 3 | 0 | 3 | 0 | 0 |

9 | 0 | 0 | 5 | 0 | 5 | 0 | 4 | 5 |

10 | 0 | 0 | 9 | 0 | 9 | 0 | 12 | 9 |

11 | 6 | 4 | 7 | 6 | 7 | 6 | 13 | 7 |

12 | 10 | 14 | 2 | 10 | 2 | 10 | 1 | 2 |

13 | 0 | 15 | 0 | 0 | 0 | 0 | 0 | 0 |

14 | 0 | 0 | 0 | 0 | 0 | 0 | 16 | 0 |

15 | 0 | 3 | 0 | 0 | 0 | 0 | 0 | 0 |

16 | 0 | 0 | 0 | 0 | 0 | 0 | 5 | 0 |

Table 1: Transition table for M add M_{\rm add} for Fibonacci addition

We briefly sketch a proof of the correctness of this automaton. States can be identified with certain sequences, as follows: if x, y, z x,y,z are the identical-length strings arising from projection of a word that takes M add M_{\rm add} from the initial state 1 1 to the state t t, then t t is identified with the integer sequence ( [x ​ 0 n] F + [y ​ 0 n] F − [z ​ 0 n] F) n ≥ 0 ([x0^{n}]_{F}+[y0^{n}]_{F}-[z0^{n}]_{F})_{n\geq 0}. With this correspondence, we can verify the following table by a tedious induction. In the table L n L_{n} denotes the familiar Lucas numbers, defined by L n = F n − 1 + F n + 1 L_{n}=F_{n-1}+F_{n+1} for n ≥ 0 n\geq 0 (assuming F − 1 = 1 F_{-1}=1). If a sequence ( a n) n ≥ 0 (a_{n})_{n\geq 0} is the sequence identified with a state t t, then t t is accepting iff a 0 = 0 a_{0}=0.

state | sequence |

1 | 0 |

2 | ( − F n + 2) n ≥ 0 (-F_{n+2})_{n\geq 0} |

3 | ( F n + 2) n ≥ 0 (F_{n+2})_{n\geq 0} |

4 | ( − F n + 3) n ≥ 0 (-F_{n+3})_{n\geq 0} |

5 | ( − F n + 4) n ≥ 0 (-F_{n+4})_{n\geq 0} |

6 | ( − F n + 1) n ≥ 0 (-F_{n+1})_{n\geq 0} |

7 | ( F n) n ≥ 0 (F_{n})_{n\geq 0} |

8 | ( F n + 1) n ≥ 0 (F_{n+1})_{n\geq 0} |

9 | ( − L n + 2) n ≥ 0 (-L_{n+2})_{n\geq 0} |

10 | ( − 2 ​ F n + 2) n ≥ 0 (-2F_{n+2})_{n\geq 0} |

11 | ( − F n) n ≥ 0 (-F_{n})_{n\geq 0} |

12 | ( − 2 ​ F n + 1) n ≥ 0 (-2F_{n+1})_{n\geq 0} |

13 | ( L n + 1) n ≥ 0 (L_{n+1})_{n\geq 0} |

14 | ( − 3 ​ F n + 2) n ≥ 0 (-3F_{n+2})_{n\geq 0} |

15 | ( 2 ​ F n + 1) n ≥ 0 (2F_{n+1})_{n\geq 0} |

16 | ( − 2 ​ F n − 3 ​ L n) n ≥ 0 (-2F_{n}-3L_{n})_{n\geq 0} |

Table 2: Identification of states with sequences

Note that the state 0 0 actually represents a set of sequences, not just a single sequence. The set corresponds to those representations that are so far “out of synch” that they can never “catch up” to have x + y = z x+y=z, no matter how many digits are appended.

###### Remark 2.

We note that, in the spirit of the paper, this adder itself can, in principle, be checked mechanically (in Th ⁡ ( ℕ, 0) \Th({\mathbb{N}},0), of course!), as follows:

First we show the adder 𝒜 \cal A is specifying a function of x x and y y. To do so, it suffices to check that

 | ∀ x ​ ∀ y ​ ∃ z ​ 𝒜 ​ ( x, y, z) \forall x\ \forall y\ \exists z\ {\cal A}(x,y,z) |  |

and

 | ∀ x ​ ∀ y ​ ∀ z ​ ∀ z ′ ​ 𝒜 ​ ( x, y, z) ∧ 𝒜 ⁡ ( x, y, z ′) ⟹ z = z ′. \forall x\ \forall y\ \forall z\ \forall z^{\prime}\ {\cal A}(x,y,z)\wedge{\cal A}(x,y,z^{\prime})\implies z=z^{\prime}. |  |

The first predicate says that there is at least one sum of x x and y y and the second says that there is at most one.

If both of these are verified, we know that 𝒜 \cal A computes a function A = A ⁡ ( x, y) A=A(x,y).

Next, we verify associativity, which amounts to checking that

 | ∀ x ​ ∀ y ​ ∀ z ​ A ​ ( A ⁡ ( x, y), z) = A ⁡ ( x, A ⁡ ( y, z)). \forall x\ \forall y\ \forall z\ A(A(x,y),z)=A(x,A(y,z)). |  |

We can do this by checking that

 | ∀ x ​ ∀ y ​ ∀ z ​ ∀ w ​ ∀ r ​ ∀ s ​ ∀ t ⁡ ( 𝒜 ⁡ ( x, y, r) ∧ 𝒜 ⁡ ( r, z, t) ∧ 𝒜 ⁡ ( y, z, s)) ⟹ 𝒜 ⁡ ( x, s, t). \forall x\ \forall y\ \forall z\ \forall w\ \forall r\ \forall s\ \forall t\ ({\cal A}(x,y,r)\ \wedge\ {\cal A}(r,z,t)\ \wedge\ {\cal A}(y,z,s))\ \implies\ {\cal A}(x,s,t). |  |

Finally, we ensure that 𝒜 \cal A is an adder by induction. First, we check that ∀ x ​ A ​ ( x, 0) = x \forall x\ A(x,0)=x, which amounts to

 | ∀ x ​ ∀ y ​ 𝒜 ​ ( x, 0, y) ⇔ x = y. \forall x\ \forall y\ {\cal A}(x,0,y)\iff x=y. |  |

Second, we check that if A ⁡ ( x, 1) = y A(x,1)=y then x < y x<y and there does not exist z z such that x < z < y x<z<y. This amounts to

 | ∀ x, y, 𝒜 ⁡ ( x, 1, y) ⟹ ( ( x < y) ∧ ¬ ∃ ⁡ z ⁡ ( x < z) ∧ ( z < y)). \forall x,y,{\cal A}(x,1,y)\implies((x<y)\ \wedge\ \neg\exists z\ (x<z)\ \wedge\ (z<y)). |  |

This last condition shows that A ⁡ ( x, 1) = x + 1 A(x,1)=x+1. By associativity A ⁡ ( x, y + 1) = A ⁡ ( x, A ⁡ ( y, 1)) = A ⁡ ( A ⁡ ( x, y), 1) = A ⁡ ( x, y) + 1 A(x,y+1)=A(x,A(y,1))=A(A(x,y),1)=A(x,y)+1. By induction, A ⁡ ( x, y) = A ⁡ ( x, 0) + y = x + y A(x,y)=A(x,0)+y=x+y, so we are done.

Another basic fact about Fibonacci representation is that, for canonical representations containing no two consecutive 1 1 ’s or leading zeroes, the radix order on representations is the same as the ordinary ordering on ℕ {\mathbb{N}}. It follows that a very simple automaton can, on input ( x, y) F (x,y)_{F}, decide whether x < y x<y.

Putting this all together, we get the analogue of Theorem 1:

###### Procedure 3 (Decision procedure for Fibonacci-automatic words).

Input: m, n ∈ ℕ m,n\in{\mathbb{N}}, m m DFAOs witnessing Fibonacci-automatic words 𝐰 1, 𝐰 2, …, 𝐰 m {\bf w}_{1},{\bf w}_{2},\dots,{\bf w}_{m}, a first-order proposition with n n free variables φ ⁡ ( v 1, v 2, …, v n) \varphi(v_{1},v_{2},\dots,v_{n}) using constants and relations definable in Th ( ℕ, 0, 1, +) \Th({\mathbb{N}},0,1,+) and indexing into 𝐰 1, 𝐰 2, …, 𝐰 m {\bf w}_{1},{\bf w}_{2},\dots,{\bf w}_{m}.
Output: DFA with input alphabet Σ 2 n \Sigma_{2}^{n} accepting { ( k 1, k 2, …, k n) F: φ ⁡ ( k 1, k 2, …, k n) ​ holds } \{(k_{1},k_{2},\dots,k_{n})_{F}\;:\;\varphi(k_{1},k_{2},\dots,k_{n})\text{ holds}\}.

We remark that there was substantial skepticism that any implementation of a decision procedure for Fibonacci-automatic words would be practical, for two reasons:

- •

first, because the running time is bounded above by an expression of the form

 | 2 2. ​. ​. 2 p ⁡ ( N) 2^{2^{\mathinner{\mkern 1.0mu\raise 1.0pt\vbox{\kern 7.0pt\hbox{.}}\mkern 2.0mu\raise 4.0pt\hbox{.}\mkern 2.0mu\raise 7.0pt\hbox{.}\mkern 1.0mu}^{2^{p(N)}}}} |  |

where p p is a polynomial, N N is the number of states in the original automaton specifying the word in question, and the number of exponents in the tower is one less than the number of quantifiers in the logical formula characterizing the property being checked.

- •

second, because of the complexity of checking addition (15 states) compared to the analogous automaton for base- k k representation (2 states).

Nevertheless, we were able to carry out nearly all the computations described in this paper in a matter of a few seconds on an ordinary laptop.

## 3 Mechanical proofs of properties of the infinite Fibonacci word

Recall that a word x x, whether finite or infinite, is said to have period p p if x ⁡ [i] = x ⁡ [i + p] x[i]=x[i+p] for all i i for which this equality is meaningful. Thus, for example, the English word 𝚊𝚕𝚏𝚊𝚕𝚏𝚊 {\tt alfalfa} has period 3 3. The exponent of a finite word x x, written exp ⁡ ( x) \exp(x), is | x | / P |x|/P, where P P is the smallest period of x x. Thus exp ⁡ ( 𝚊𝚕𝚏𝚊𝚕𝚏𝚊) = 7 / 3 \exp({\tt alfalfa})=7/3.

If 𝐱 \bf x is an infinite word with a finite period, we say it is ultimately periodic. An infinite word 𝐱 \bf x is ultimately periodic if and only if there are finite words u, v u,v such that x = u ​ v ω x=uv^{\omega}, where v ω = v v v ⋯ v^{\omega}=vvv\cdots.

A nonempty word of the form x ​ x xx is called a square, and a nonempty word of the form x ​ x ​ x xxx is called a cube. More generally, a nonempty word of the form x n x^{n} is called an n n ’th power. By the order of a square x ​ x xx, cube x ​ x ​ x xxx, or n n ’th power x n x^{n}, we mean the length | x | |x|.

The infinite Fibonacci word 𝐟 = 01001010 ⋯ = f 0 f 1 f 2 ⋯ {\bf f}=01001010\cdots=f_{0}f_{1}f_{2}\cdots can be described in many different ways. In addition to our definition in terms of automata, it is also the fixed point of the morphism φ ⁡ ( 0) = 01 \varphi(0)=01 and φ ⁡ ( 1) = 0 \varphi(1)=0. This word has been studied extensively in the literature; see, for example, [5, 7].

In the next subsection, we use our implementation to prove a variety of results about repetitions in 𝐟 \bf f.

### 3.1 Repetitions

###### Theorem 4.

The word 𝐟 \bf f is not ultimately periodic.

###### Proof.

We construct a predicate asserting that the integer p ≥ 1 p\geq 1 is a period of some suffix of 𝐟 \bf f:

 | ( p ≥ 1) ∧ ∃ n ​ ∀ i ≥ n ​ 𝐟 ​ [i] = 𝐟 ⁡ [i + p]. (p\geq 1)\ \wedge\ \exists n\ \forall i\geq n\ {\bf f}[i]={\bf f}[i+p]. |  |

(Note: unless otherwise indicated, whenever we refer to a variable in a predicate, the range of the variable is assumed to be ℕ = { 0, 1, 2, … } {\mathbb{N}}=\{0,1,2,\ldots\}.) From this predicate, using our program, we constructed an automaton accepting the language

 | L = 0 ∗ ​ { ( p) F: ( p ≥ 1) ∧ ∃ n ​ ∀ i ≥ n ​ 𝐟 ​ [i] = 𝐟 ⁡ [i + p] }. L=0^{*}\ \{(p)_{F}\ :\ (p\geq 1)\ \wedge\ \exists n\ \forall i\geq n\ {\bf f}[i]={\bf f}[i+p]\}. |  |

This automaton accepts the empty language, and so it follows that 𝐟 {\bf f} is not ultimately periodic.

Here is the log of our program:

```

p >= 1 with 4 states, in 60ms
 i >= n with 7 states, in 5ms
  F[i] = F[i + p] with 12 states, in 34ms
   i >= n => F[i] = F[i + p] with 51 states, in 15ms
    Ai i >= n => F[i] = F[i + p] with 3 states, in 30ms
     p >= 1 & Ai i >= n => F[i] = F[i + p] with 2 states, in 0ms
      En p >= 1 & Ai i >= n => F[i] = F[i + p] with 2 states, in 0ms
overall time: 144ms
```

The largest intermediate automaton during the computation had 63 states.

A few words of explanation are in order: here “ F ” refers to the sequence 𝐟 \bf f, and “ E ” is our abbreviation for ∃ \exists and “ A ” is our abbreviation for ∀ \forall. The symbol “ => ” is logical implication, and “ & ” is logical and. ∎

From now on, whenever we discuss the language accepted by an automaton, we will omit the 0 ∗ 0^{*} at the beginning.

We recall an old result of Karhumäki [53, Thm. 2]:

###### Theorem 5.

𝐟 \bf f contains no fourth powers.

###### Proof.

We create a predicate for the orders of all fourth powers occurring in 𝐟 \bf f:

 | ( n > 0) ∧ ∃ i ​ ∀ t < 3 ​ n ​ 𝐟 ​ [i + t] = 𝐟 ⁡ [i + n + t]. (n>0)\ \wedge\ \exists i\ \forall t<3n\ {\bf f}[i+t]={\bf f}[i+n+t]. |  |

The resulting automaton accepts nothing, so there are no fourth powers.

```

n > 0 with 4 states, in 46ms
 t < 3 * n with 30 states, in 178ms
  F[i + t] = F[i + t + n] with 62 states, in 493ms
   t < 3 * n => F[i + t] = F[i + t + n] with 352 states, in 39ms
    At t < 3 * n => F[i + t] = F[i + t + n] with 3 states, in 132ms
     Ei At t < 3 * n => F[i + t] = F[i + t + n] with 2 states, in 0ms
      n > 0 & Ei At t < 3 * n => F[i + t] = F[i + t + n] with 2 states, in 0ms
overall time: 888ms
```

∎

The largest intermediate automaton in the computation had 952 states.

Next, we move on to a description of the orders of squares occurring in 𝐟 \bf f. An old result of Séébold [71] (also see [52, 39]) states

###### Theorem 6.

All squares in 𝐟 \bf f are of order F n F_{n} for some n ≥ 2 n\geq 2. Furthermore, for all n ≥ 2 n\geq 2, there exists a square of order F n F_{n} in 𝐟 \bf f.

###### Proof.

We create a predicate for the lengths of squares:

 | ( n > 0) ∧ ∃ i ​ ∀ t < n ​ 𝐟 ​ [i + t] = 𝐟 ⁡ [i + n + t]. (n>0)\ \wedge\ \exists i\ \forall t<n\ {\bf f}[i+t]={\bf f}[i+n+t]. |  |

When we run this predicate, we obtain an automaton that accepts exactly the language 10 ∗ 10^{*}. Here is the log file:

```

n > 0 with 4 states, in 38ms
 t < n with 7 states, in 5ms
  F[i + t] = F[i + t + n] with 62 states, in 582ms
   t < n => F[i + t] = F[i + t + n] with 92 states, in 12ms
    At t < n => F[i + t] = F[i + t + n] with 7 states, in 49ms
     Ei At t < n => F[i + t] = F[i + t + n] with 3 states, in 1ms
      n > 0 & Ei At t < n => F[i + t] = F[i + t + n] with 3 states, in 0ms
overall time: 687ms
```

∎

The largest intermediate automaton had 236 states.

We can easily get much, much more information about the square occurrences in 𝐟 \bf f. The positions of all squares in 𝐟 \bf f were computed by Iliopoulos, Moore, and Smyth [52, § 2], but their description is rather complicated and takes 5 pages to prove. Using our approach, we created an automaton accepting the language

 | { ( n, i) F: ( n > 0) ∧ ∀ t < n ​ 𝐟 ​ [i + t] = 𝐟 ⁡ [i + n + t] }. \{(n,i)_{F}\ :\ (n>0)\ \wedge\ \forall t<n\ {\bf f}[i+t]={\bf f}[i+n+t]\}. |  |

This automaton has only 6 states and efficiently encodes the orders and starting positions of each square in 𝐟 \bf f. During the computation, the largest intermediate automaton had 236 states. Thus we have proved

###### Theorem 7.

The language

 | { ( n, i) F: there is a square of order n beginning at position i in f } \{(n,i)_{F}\ :\ \text{there is a square of order $n$ beginning at position $i$ in {\bf f}}\} |  |

is accepted by the automaton in Figure 2.

Figure 2: Automaton accepting orders and positions of all squares in 𝐟 \bf f

Next, we examine the cubes in 𝐟 \bf f. Evidently Theorem 6 implies that any cube in 𝐟 \bf f must be of order F n F_{n} for some n n. However, not every order occurs.

###### Theorem 8.

The cubes in 𝐟 \bf f are of order F n F_{n} for n ≥ 4 n\geq 4, and a cube of each such order occurs.

###### Proof.

We use the predicate

 | ( n > 0) ∧ ∃ i ​ ∀ t < 2 ​ n ​ 𝐟 ​ [i + t] = 𝐟 ⁡ [i + n + t]. (n>0)\ \wedge\ \exists i\ \forall t<2n\ {\bf f}[i+t]={\bf f}[i+n+t]. |  |

When we run our program, we obtain an automaton accepting exactly the language ( 100) ​ 0 ∗ (100)0^{*}, which corresponds to F n F_{n} for n ≥ 4 n\geq 4.

```

n > 0 with 4 states, in 34ms
 t < 2 * n with 16 states, in 82ms
  F[i + t] = F[i + t + n] with 62 states, in 397ms
   t < 2 * n => F[i + t] = F[i + t + n] with 198 states, in 17ms
    At t < 2 * n => F[i + t] = F[i + t + n] with 7 states, in 87ms
     Ei At t < 2 * n => F[i + t] = F[i + t + n] with 5 states, in 1ms
      n > 0 & Ei At t < 2 * n => F[i + t] = F[i + t + n] with 5 states, in 0ms
overall time: 618ms
```

∎

The largest intermediate automaton had 674 states.

Next, we encode the orders and positions of all cubes. We build a DFA accepting the language

 | { ( n, i) F: ( n > 0) ∧ ∀ t < 2 ​ n ​ 𝐟 ​ [i + t] = 𝐟 ⁡ [i + n + t] }. \{(n,i)_{F}\ :\ (n>0)\ \wedge\ \forall t<2n\ {\bf f}[i+t]={\bf f}[i+n+t]\}. |  |

###### Theorem 9.

The language

 | { ( n, i) F: there is a cube of order n beginning at position i in f } \{(n,i)_{F}\ :\ \text{there is a cube of order $n$ beginning at position $i$ in {\bf f}}\} |  |

is accepted by the automaton in Figure 3.

Figure 3: Automaton accepting orders and positions of all cubes in 𝐟 \bf f

Finally, we consider all the maximal repetitions in 𝐟 \bf f. Let p ⁡ ( x) p(x) denote the length of the least period of x x. If 𝐱 = a 0 a 1 ⋯ {\bf x}=a_{0}a_{1}\cdots, by 𝐱 [i.. j] {\bf x}[i..j] we mean a i a i + 1 ⋯ a j a_{i}a_{i+1}\cdots a_{j}. Following Kolpakov and Kucherov [54], we say that 𝐟 [i.. i + n − 1] {\bf f}[i..i+n-1] is a maximal repetition if

- (a)

p ( 𝐟 [i.. i + n − 1]) ≤ n / 2 p({\bf f}[i..i+n-1])\leq n/2;

- (b)

p ( 𝐟 [i.. i + n − 1]) < p ( 𝐟 [i.. i + n]) p({\bf f}[i..i+n-1])<p({\bf f}[i..i+n]);

- (c)

If i > 0 i>0 then p ( 𝐟 [i.. i + n − 1]) < p ( 𝐟 [i − 1.. i + n − 1]) p({\bf f}[i..i+n-1])<p({\bf f}[i-1..i+n-1]).

###### Theorem 10.

The factor 𝐟 [i.. i + n − 1] {\bf f}[i..i+n-1] is a maximal repetition of 𝐟 \bf f iff ( n, i) F (n,i)_{F} is accepted by the automaton depicted in Figure 4.

Figure 4: Automaton accepting occurrences of maximal repetitions in 𝐟 \bf f

An antisquare is a nonempty word of the form x ​ x ¯ x\overline{x}, where x ¯ \overline{x} denotes the complement of x x ( 1 1 ’s changed to 0 0 ’s and vice versa). Its order is | x | |x|. For a new (but small) result we prove

###### Theorem 11.

The Fibonacci word 𝐟 \bf f contains exactly four antisquare factors: 01, 10, 1001, 01,10,1001, and 10100101 10100101.

###### Proof.

The predicate for having an antisquare of length n n is

 | ∃ i ​ ∀ k < n ​ 𝐟 ​ [i + k] ≠ 𝐟 ⁡ [i + k + n]. \exists i\ \forall k<n\ {\bf f}[i+k]\not={\bf f}[i+k+n]. |  |

When we run this we get the automaton depicted in Figure 5, specifying that the only possible orders are 1 1, 2 2, and 4 4, which correspond to words of length 2 2, 4 4, and 8 8.

Figure 5: Automaton accepting orders of antisquares in 𝐟 \bf f

Inspection of the factors of these lengths proves the result. ∎

### 3.2 Palindromes and antipalindromes

We now turn to a characterization of the palindromes in 𝐟 \bf f. Using the predicate

 | ∃ i ​ ∀ j < n ​ 𝐟 ​ [i + j] = 𝐟 ⁡ [i + n − 1 − j], \exists i\ \forall j<n\ {\bf f}[i+j]={\bf f}[i+n-1-j], |  |

we specify those lengths n n for which there is a palindrome of length n n. Our program then recovers the following result of Chuan [27]:

###### Theorem 12.

There exist palindromes of every length ≥ 0 \geq 0 in 𝐟 \bf f.

We could also characterize the positions of all nonempty palindromes. The resulting 21-state automaton is not particularly enlightening, but is included here to show the kind of complexity that can arise.

Figure 6: Automaton accepting orders and positions of all nonempty palindromes in 𝐟 \bf f

Although the automaton in Figure 6 encodes all palindromes, more specific information is a little hard to deduce from it. For example, let’s prove a result of Droubay [36]:

###### Theorem 13.

The Fibonacci word 𝐟 \bf f has exactly one palindromic factor of length n n if n n is even, and exactly two palindromes of length n n if n n odd.

###### Proof.

First, we obtain an expression for the lengths n n for which there is exactly one palindromic factor of length n n.

 | ∃ i ⁡ ( ∀ t < n ​ 𝐟 ​ [i + t] = 𝐟 ⁡ [i + n − 1 − t]) ∧ ∀ j ⁡ ( ∀ s < n ​ 𝐟 ​ [j + s] = 𝐟 ⁡ [j + n − 1 − s]) ⟹ ( ∀ u < n ​ 𝐟 ​ [i + u] = 𝐟 ⁡ [j + u]) \exists i\ (\forall t<n\ {\bf f}[i+t]={\bf f}[i+n-1-t])\ \wedge\ \\ \forall j\ (\forall s<n\ {\bf f}[j+s]={\bf f}[j+n-1-s])\implies(\forall u<n\ {\bf f}[i+u]={\bf f}[j+u]) |  |

The first part of the predicate asserts that 𝐟 [i.. i + n − 1] {\bf f}[i..i+n-1] is a palindrome, and the second part asserts that any palindrome 𝐟 [j.. j + n − 1] {\bf f}[j..j+n-1] of the same length must in fact be equal to 𝐟 [i.. i + n − 1] {\bf f}[i..i+n-1].

When we run this predicate through our program we get the automaton depicted below in Figure 7.

Figure 7: Automaton accepting lengths with exactly one palindrome

It may not be obvious, but this automaton accepts exactly the Fibonacci representations of the even numbers. The easiest way to check this is to use our program on the predicate ∃ i ​ n = 2 ​ i \exists i\ n=2i and verify that the resulting automaton is isomorphic to that in Figure 7.

Next, we write down a predicate for the existence of exactly two distinct palindromes of length n n. The predicate asserts the existence of two palindromes 𝐱 [i.. i + n − 1] {\bf x}[i..i+n-1] and 𝐱 [j.. j + n − 1] {\bf x}[j..j+n-1] that are distinct and for which any palindrome of the same length must be equal to one of them.

 | ∃ i ​ ∃ j ⁡ ( ∀ t < n ​ 𝐟 ​ [i + t] = 𝐟 ⁡ [i + n − 1 − t]) ∧ ( ∀ s < n ​ 𝐟 ​ [j + s] = 𝐟 ⁡ [j + n − 1 − s]) ∧ ( ∃ m < n ​ 𝐟 ​ [i + m] ≠ 𝐟 ⁡ [j + m]) ∧ ( ∀ u ⁡ ( ∀ k < n ​ 𝐟 ​ [u + k] = 𝐟 ⁡ [u + n − 1 − k]) ⟹ ( ( ∀ l < n ​ 𝐟 ​ [u + l] = 𝐟 ⁡ [i + l]) ∨ ( ∀ p < n ​ 𝐟 ​ [u + p] = 𝐟 ⁡ [j + p]))) \exists i\ \exists j\ (\forall t<n\ {\bf f}[i+t]={\bf f}[i+n-1-t])\ \wedge\ (\forall s<n\ {\bf f}[j+s]={\bf f}[j+n-1-s])\ \wedge\ \\ (\exists m<n\ {\bf f}[i+m]\not={\bf f}[j+m])\ \wedge\ \\ (\forall u(\forall k<n\ {\bf f}[u+k]={\bf f}[u+n-1-k])\implies((\forall l<n\ {\bf f}[u+l]={\bf f}[i+l])\ \vee\ (\forall p<n\ {\bf f}[u+p]={\bf f}[j+p]))) |  |

Again, running this through our program gives us an automaton accepting the Fibonacci representations of the odd numbers. We omit the automaton. ∎

The prefixes are factors of particular interest. Let us determine which prefixes are palindromes:

###### Theorem 14.

The prefix 𝐟 [0.. n − 1] {\bf f}[0..n-1] of length n n is a palindrome if and only if n = F i − 2 n=F_{i}-2 for some i ≥ 3 i\geq 3.

###### Proof.

We use the predicate

 | ∀ i < n ​ 𝐟 ​ [i] = 𝐟 ⁡ [n − 1 − i] \forall i<n\ {\bf f}[i]={\bf f}[n-1-i] |  |

obtaining an automaton accepting ϵ + 1 + 10 ​ ( 10) ∗ ​ ( 0 + 01) \epsilon+1+10(10)^{*}(0+01), which are precisely the representations of F i − 2 F_{i}-2. ∎

Next, we turn to the property of “mirror invariance”. We say an infinite word 𝐰 \bf w is mirror-invariant if whenever x x is a factor of 𝐰 \bf w, then so is x R x^{R}. We can check this for 𝐟 \bf f by creating a predicate for the assertion that for each factor x x of length n n, the factor x R x^{R} appears somewhere else:

 | ∀ i ≥ 0 ∃ j such that 𝐟 [i.. i + n − 1] = 𝐟 [j.. j + n − 1] R. \forall i\geq 0\ \exists j\text{ such that }{\bf f}[i..i+n-1]={\bf f}[j..j+n-1]^{R}. |  |

When we run this through our program we discover that it accepts the representations of all n ≥ 0 n\geq 0. Here is the log:

```

t < n with 7 states, in 99ms
 F[i + t] = F[j + n - 1 - t] with 264 states, in 7944ms
  t < n => F[i + t] = F[j + n - 1 - t] with 185 states, in 89ms
   At t < n => F[i + t] = F[j + n - 1 - t] with 35 states, in 182ms
    Ej At t < n => F[i + t] = F[j + n - 1 - t] with 5 states, in 2ms
     Ai Ej At t < n => F[i + t] = F[j + n - 1 - t] with 3 states, in 6ms
overall time: 8322ms
```

Thus we have proved:

###### Theorem 15.

The word 𝐟 {\bf f} is mirror invariant.

An antipalindrome is a word x x satisfying x = x R ¯ x=\overline{x^{R}}. For a new (but small) result, we determine all possible antipalindromes in 𝐟 \bf f:

###### Theorem 16.

The only nonempty antipalindromes in 𝐟 \bf f are 01 01, 10 10, ( 01) 2 (01)^{2}, and ( 10) 2 (10)^{2}.

###### Proof.

Let us write a predicate specifying that 𝐟 [i.. i + n − 1] {\bf f}[i..i+n-1] is a nonempty antipalindrome, and further that it is a first occurrence of such a factor:

 | ( n > 0) ∧ ( ∀ j < n ​ 𝐟 ​ [i + j] ≠ 𝐟 ⁡ [i + n − 1 − j]) ∧ ( ∀ i ′ < i ​ ∃ j < n ​ 𝐟 ​ [i ′ + j] ≠ 𝐟 ⁡ [i + j]). (n>0)\ \wedge\ (\forall j<n\ {\bf f}[i+j]\not={\bf f}[i+n-1-j])\ \wedge\ (\forall i^{\prime}<i\ \exists j<n\ {\bf f}[i^{\prime}+j]\not={\bf f}[i+j]). |  |

When we run this through our program, the language of ( n, i) F (n,i)_{F} satisfying this predicate is accepted by the following automaton:

Figure 8: Automaton accepting orders and positions of first occurrences of nonempty antipalindromes in 𝐟 \bf f

It follows that the only ( n, i) (n,i) pairs accepted are ( 2, 0), ( 2, 1), ( 4, 3), ( 4, 4) (2,0),(2,1),(4,3),(4,4), corresponding, respectively, to the strings 01 01, 10 10, ( 01) 2 (01)^{2}, and ( 10) 2 (10)^{2}. ∎

### 3.3 Special factors

Next we turn to special factors. It is well-known (and we will prove it in Theorem 57 below), that 𝐟 {\bf f} has exactly n + 1 n+1 distinct factors of length n n for each n ≥ 0 n\geq 0. This implies that there is exactly one factor x x of each length n n with the property that both x ​ 0 x0 and x ​ 1 x1 are factors. Such a factor is called right-special or sometimes just special. We can write a predicate that expresses the assertion that the factor 𝐟 [i.. i + n − 1] {\bf f}[i..i+n-1] is the unique special factor of length n n, and furthermore, that it is the first occurrence of that factor, as follows:

 | ( ∀ i ′ < i ​ ∃ s < n ​ 𝐟 ​ [i ′ + s] ≠ 𝐟 ⁡ [i + s]) ∧ ∃ j ​ ∃ k ⁡ ( ( ∀ t < n ​ 𝐟 ​ [j + t] = 𝐟 ⁡ [i + t]) CLOSE OPEN ∧ ( ∀ u < n ​ 𝐟 ​ [k + u] = 𝐟 ⁡ [i + u]) ∧ ( 𝐟 ⁡ [j + n] ≠ 𝐟 ⁡ [k + n])). (\forall i^{\prime}<i\ \exists s<n\ {\bf f}[i^{\prime}+s]\not={\bf f}[i+s])\ \wedge\ \exists j\ \exists k\ ((\forall t<n\ {\bf f}[j+t]={\bf f}[i+t])\\ \wedge\ (\forall u<n\ {\bf f}[k+u]={\bf f}[i+u])\ \wedge\ ({\bf f}[j+n]\not={\bf f}[k+n])). |  |

###### Theorem 17.

The automaton depicted below in Figure 9 accepts the language

 | { ( i, n) F: the factor 𝐟 [i.. i + n − 1] is the first occurrence of the unique special factor of length n }. \{(i,n)_{F}\ :\ \text{the factor }{\bf f}[i..i+n-1]\text{ is the first occurrence of the unique special factor of length $n$}\}. |  |

Figure 9: Automaton accepting first positions and lengths of special factors in 𝐟 \bf f

Furthermore it is known (e.g., [60, Lemma 5]) that

###### Theorem 18.

The unique special factor of length n n is 𝐟 [0.. n − 1] R {\bf f}[0..n-1]^{R}.

###### Proof.

We create a predicate that says that if a factor is special then it matches 𝐟 [0.. n − 1] R {\bf f}[0..n-1]^{R}. When we run this we discover that all lengths are accepted. ∎

### 3.4 Least periods

We now turn to least periods of factors of 𝐟 {\bf f}; see [67] and [37] and [34, Corollary 4].

Let P P denote the assertion that n n is a period of the factor 𝐟 [i.. j] {\bf f}[i..j], as follows:

 | P ⁡ ( n, i, j) \displaystyle P(n,i,j) | = \displaystyle= | 𝐟 [i.. j − n] = 𝐟 [i + n.. j] \displaystyle{\bf f}[i..j-n]={\bf f}[i+n..j] |  |

 |  | = \displaystyle= | ∀ t ​ with i ≤ t ≤ j − n we have ​ 𝐟 ​ [t] = 𝐟 ⁡ [t + n]. \displaystyle\forall\ t\ \text{ with $i\leq t\leq j-n$ we have }{\bf f}[t]={\bf f}[t+n]. |  |

Using this, we can express the predicate L ​ P LP that n n is the least period of 𝐟 [i.. j] {\bf f}[i..j]:

 | L ​ P ​ ( n, i, j) = P ⁡ ( n, i, j) ​ and ​ ∀ n ′ ​ with ​ 1 ≤ n ′ < n ​ ¬ P ⁡ ( n ′, i, j). LP(n,i,j)=P(n,i,j)\text{ and }\forall n^{\prime}\text{ with }1\leq n^{\prime}<n\ \neg P(n^{\prime},i,j). |  |

Finally, we can express the predicate that n n is a least period as follows

 | L ⁡ ( n) = ∃ i, j ≥ 0 ​ with 0 ≤ i + n ≤ j − 1 ​ L ​ P ​ ( n, i, j). L(n)=\exists i,j\geq 0\text{ with $0\leq i+n\leq j-1$ }LP(n,i,j). |  |

Using an implementation of this, we can reprove the following theorem of Saari [67, Thm. 2]:

###### Theorem 19.

If a word w w is a nonempty factor of the Fibonacci word, then the least period of w w is a Fibonacci number F n F_{n} for n ≥ 2 n\geq 2. Furthermore, each such period occurs.

###### Proof.

We ran our program on the appropriate predicate and found the resulting automaton accepts 10 + 10^{+}, corresponding to F n F_{n} for n ≥ 2 n\geq 2. ∎

Furthermore, we can actually encode information about all least periods. The automaton depicted in Figure 10 accepts triples ( n, p, i) (n,p,i) such that p p is a least period of 𝐟 [i.. i + n − 1] {\bf f}[i..i+n-1].

Figure 10: Automaton encoding least periods of all factors in 𝐟 \bf f

We also have the following result, which seems to be new.

###### Theorem 20.

Let n ≥ 1 n\geq 1, and define ℓ ⁡ ( n) \ell(n) to be the smallest integer that is the least period of some length- n n factor of 𝐟 \bf f. Then ℓ ⁡ ( n) = F j \ell(n)=F_{j} for j ≥ 1 j\geq 1 if L j − 1 ≤ n ≤ L j + 1 − 2 L_{j}-1\leq n\leq L_{j+1}-2, where L j L_{j} is the j j ’th Lucas number defined in Section 2.

###### Proof.

We create an automaton accepting ( n, p) F (n,p)_{F} such that (a) there exists at least one length- n n factor of period p p and (b) for all length- n n factors x x, if q q is a period of x x, then q ≥ p q\geq p. This automaton is depicted in Figure 11 below.

Figure 11: Automaton encoding smallest period over all length- n n factors in 𝐟 \bf f

The result now follows by inspection and the fact that ( L j − 1) F = 10 ​ ( 01) ( j − 2) / 2 (L_{j}-1)_{F}=10(01)^{(j-2)/2} if j ≥ 2 j\geq 2 is even, and 100 ​ ( 10) ( j − 3) / 2 100(10)^{(j-3)/2} if j ≥ 3 j\geq 3 is odd. ∎

### 3.5 Quasiperiods

We now turn to quasiperiods. An infinite word 𝐚 \bf a is said to be quasiperiodic if there is some finite nonempty word x x such that 𝐚 {\bf a} can be completely “covered” with translates of x x. Here we study the stronger version of quasiperiodicity where the first copy of x x used must be aligned with the left edge of 𝐰 \bf w and is not allowed to “hang over”; these are called aligned covers in [26]. More precisely, for us 𝐚 = a 0 a 1 a 2 ⋯ {\bf a}=a_{0}a_{1}a_{2}\cdots is quasiperiodic if there exists x x such that for all i ≥ 0 i\geq 0 there exists j ≥ 0 j\geq 0 with i − n < j ≤ i i-n<j\leq i such that a j a j + 1 ⋯ a j + n − 1 = x a_{j}a_{j+1}\cdots a_{j+n-1}=x, where n = | x | n=|x|. Such an x x is called a quasiperiod. Note that the condition j ≥ 0 j\geq 0 implies that, in this interpretation, any quasiperiod must actually be a prefix of 𝐚 \bf a.

The quasiperiodicity of the Fibonacci word 𝐟 \bf f was studied by Christou, Crochemore, and Iliopoulos [26], where we can (more or less) find the following theorem:

###### Theorem 21.

A nonempty length- n n prefix of 𝐟 \bf f is a quasiperiod of 𝐟 \bf f if and only if n n is not of the form F n − 1 F_{n}-1 for n ≥ 3 n\geq 3.

In particular, the following prefix lengths are not quasiperiods: 1 1, 2 2, 4 4, 7 7, 12 12, and so forth.

###### Proof.

We write a predicate for the assertion that the length- n n prefix is a quasiperiod:

 | ∀ i ≥ 0 ​ ∃ j ​ with ​ i − n < j ≤ i ​ such that ​ ∀ t < n ​ 𝐟 ​ [t] = 𝐟 ⁡ [j + t]. \forall i\geq 0\ \exists j\text{ with }i-n<j\leq i\text{ such that }\forall t<n\ {\bf f}[t]={\bf f}[j+t]. |  |

When we do this, we get the automaton in Figure 12 below. Inspection shows that this DFA accepts all canonical representations, except those of the form 1 ​ ( 01) ∗ ​ ( ϵ + 0) 1(01)^{*}(\epsilon+0), which are precisely the representations of F n − 1 F_{n}-1.

Figure 12: Automaton accepting lengths of prefixes of 𝐟 \bf f that are quasiperiods

∎

### 3.6 Unbordered factors

Next we look at unbordered factors. A word y y is said to be a border of x x if y y is both a nonempty proper prefix and suffix of x x. A word x x is bordered if it has at least one border. It is easy to see that if a word y y is bordered iff it has a border of length ℓ \ell with 0 < ℓ ≤ | y | / 2 0<\ell\leq|y|/2.

###### Theorem 22.

The only unbordered nonempty factors of 𝐟 \bf f are of length F n F_{n} for n ≥ 2 n\geq 2, and there are two for each such length. For n ≥ 3 n\geq 3 these two unbordered factors have the property that one is a reverse of the other.

###### Proof.

We can express the property of having an unbordered factor of length n n as follows

 | ∃ i ​ ∀ j, 1 ≤ j ≤ n / 2, ∃ t < j ​ 𝐟 ​ [i + t] ≠ 𝐟 ⁡ [i + n − j + t]. \exists i\ \forall j,1\leq j\leq n/2,\ \exists t<j\ {\bf f}[i+t]\not={\bf f}[i+n-j+t]. |  |

Here is the log:

```

j >= 1 with 4 states, in 155ms
 2 * j <= n with 16 states, in 91ms
  j >= 1 & 2 * j <= n with 21 states, in 74ms
   t < j with 7 states, in 17ms
    F[i + t] != F[i + n - j + t] with 321 states, in 10590ms
     t < j & F[i + t] != F[i + n - j + t] with 411 states, in 116ms
      Et t < j & F[i + t] != F[i + n - j + t] with 85 states, in 232ms
       j >= 1 & 2 * j <= n => Et t < j & F[i + t] != F[i + n - j + t] with 137 states, in 19ms
        Aj j >= 1 & 2 * j <= n => Et t < j & F[i + t] != F[i + n - j + t] with 7 states, in 27ms
         Ei Aj j >= 1 & 2 * j <= n => Et t < j & F[i + t] != F[i + n - j + t] with 3 states, in 0ms
overall time: 11321ms
```

The automaton produced accepts the Fibonacci representation of 0 0 and F n F_{n} for n ≥ 2 n\geq 2.

Next, we make the assertion that there are exactly two such factors for each appropriate length. We can do this by saying there is an unbordered factor of length n n beginning at position i i, another one beginning at position k k, and these factors are distinct, and for every unbordered factor of length n n, it is equal to one of these two. When we do this we discover that the representations of all F n F_{n} for n ≥ 2 n\geq 2 are accepted.

Finally, we make the assertion that for any two unbordered factors of length n n, either they are equal or one is the reverse of the other. When we do this we discover all lengths except length 1 1 are accepted. (That is, for all lengths other than F n F_{n}, n ≥ 2 n\geq 2, the assertion is trivially true since there are no unbordered factors; for F 2 = 1 F_{2}=1 it is false since 0 0 and 1 1 are the unbordered factors and one is not the reverse of the other; and for all larger F i F_{i} the property holds.) ∎

### 3.7 Recurrence, uniform recurrence, and linear recurrence

We now turn to various questions about recurrence. A factor x x of an infinite word 𝐰 \bf w is said to be recurrent if it occurs infinitely often. The word 𝐰 \bf w is recurrent if every factor that occurs at least once is recurrent. A factor x x is uniformly recurrent if there exists a constant c = c ⁡ ( x) c=c(x) such that any factor 𝐰 [i.. i + c] {\bf w}[i..i+c] is guaranteed to contain an occurrence of x x. If all factors are uniformly recurrent then 𝐰 \bf w is said to be uniformly recurrent. Finally, 𝐰 {\bf w} is linearly recurrent if the constant c ⁡ ( x) c(x) is O ⁡ ( | x |) O(|x|).

###### Theorem 23.

The word f is recurrent, uniformly recurrent, and linearly recurrent.

###### Proof.

A predicate for all length- n n factors being recurrent:

 | ∀ i ≥ 0 ​ ∀ j ≥ 0 ​ ∃ k > j ​ ∀ t < n ​ 𝐟 ​ [i + t] = 𝐟 ⁡ [k + t]. \forall i\geq 0\ \forall j\geq 0\ \exists k>j\ \forall t<n\ {\bf f}[i+t]={\bf f}[k+t]. |  |

This predicate says that for every factor z = 𝐟 [i.. i + n − 1] z={\bf f}[i..i+n-1] and every position j j we can find another occurrence of z z beginning at a position k > j k>j. When we run this we discover that the representations of all n ≥ 0 n\geq 0 are accepted. So 𝐟 \bf f is recurrent.

A predicate for uniform recurrence:

 | ∀ i ​ ∃ ℓ ​ ∀ j ​ ∃ s, j ≤ s ≤ j + l − n ​ ∀ p < n ​ 𝐟 ​ [s + p] = 𝐟 ⁡ [i + p]. \forall i\ \exists\ell\ \forall j\ \exists s,\ j\leq s\leq j+l-n\ \forall p<n\ {\bf f}[s+p]={\bf f}[i+p]. |  |

Once again, when we run this we discover that the representations of all n ≥ 0 n\geq 0 are accepted. So 𝐟 \bf f is uniformly recurrent.

A predicate for linear recurrence with constant C C:

 | ∀ i ​ ∀ j ​ ∃ s, j ≤ s ≤ j + C ​ n ​ ∀ p < n ​ 𝐟 ​ [s + p] = 𝐟 ⁡ [i + p]. \forall i\ \forall j\ \exists s,\ j\leq s\leq j+Cn\ \forall p<n\ {\bf f}[s+p]={\bf f}[i+p]. |  |

When we run this with C = 4 C=4, we discover that the representations of all n ≥ 0 n\geq 0 are accepted (but, incidentally, not for C = 3 C=3). So 𝐟 \bf f is linearly recurrent. ∎

###### Remark 24.

We can decide the property of linear recurrence for Fibonacci-automatic words even without knowing an explicit value for the constant C C. The idea is to accept those pairs ( n, t) (n,t) such that there exists a factor of length n n with two consecutive occurrences separated by distance t t. Letting S S denote the set of such pairs, then a sequence is linearly recurrent iff lim sup ( n, t) ∈ S t / n < ∞ \limsup_{(n,t)\in S}t/n<\infty, which can be decided using an argument like that in [70, Thm. 8]. However, we do not know how to compute, in general, the exact value of the lim sup \limsup for Fibonacci representation (which we do indeed know for base- k k representation), although we can approximate it arbitrarily closely.

### 3.8 Lyndon words

Next, we turn to some results about Lyndon words. Recall that a nonempty word x x is a Lyndon word if it is lexicographically less than all of its nonempty proper prefixes. 1 1 1 There is also a version where “prefixes” is replaced by “suffixes”. We reprove some recent results of Currie and Saari [34] and Saari [68].

###### Theorem 25.

Every Lyndon factor of 𝐟 \bf f is of length F n F_{n} for some n ≥ 2 n\geq 2, and each of these lengths has a Lyndon factor.

###### Proof.

Here is the predicate specifying that there is a factor of length n n that is Lyndon:

 | ∃ i ​ ∀ j, 1 ≤ j < n, ∃ t < n − j ⁡ ( ∀ u < t ​ 𝐟 ​ [i + u] = 𝐟 ⁡ [i + j + u]) ∧ 𝐟 ⁡ [i + t] < 𝐟 ⁡ [i + j + t]. \exists i\ \forall j,1\leq j<n,\ \exists t<n-j\ (\forall u<t\ {\bf f}[i+u]={\bf f}[i+j+u])\ \wedge\ {\bf f}[i+t]<{\bf f}[i+j+t]. |  |

When we run this we get the representations 10 ∗ 10^{*}, which proves the result. ∎

###### Theorem 26.

For n ≥ 2 n\geq 2, every length- n n Lyndon factor of 𝐟 \bf f is a conjugate of 𝐟 [0.. n − 1] {\bf f}[0..n-1].

###### Proof.

Using the predicate from the previous theorem as a base, we can create a predicate specifying that every length- n n Lyndon factor is a conjugate of 𝐟 [0.. n − 1] {\bf f}[0..n-1]. When we do this we discover that all lengths except 1 1 are accepted. (The only lengths having a Lyndon factor are F n F_{n} for n ≥ 2 n\geq 2, so all but F 2 F_{2} have the desired property.) ∎

### 3.9 Critical exponents

Recall from Section 3 that exp ⁡ ( w) = | w | / P \exp(w)=|w|/P, where P P is the smallest period of w w. The critical exponent of an infinite word 𝐱 \bf x is the supremum, over all factors w w of 𝐱 \bf x, of exp ⁡ ( w) \exp(w).

A classic result of [56] is

###### Theorem 27.

The critical exponent of 𝐟 \bf f is 2 + α 2+\alpha, where α = ( 1 + 5) / 2 \alpha=(1+\sqrt{5})/2.

Although it is known that the critical exponent is computable for k k -automatic sequences [70], we do not yet know this for Fibonacci-automatic sequences (and more generally Pisot-automatic sequences). However, with a little inspired guessing about the maximal repetitions, we can complete the proof.

###### Proof.

For each length n n, the smallest possible period p p of a factor is given by Theorem 20. Hence the critical exponent is given by lim j → ∞ ( L j + 1 − 2) / F j \lim_{j\rightarrow\infty}(L_{j+1}-2)/F_{j}, which is 2 + α 2+\alpha. ∎

We can also ask the same sort of questions about the initial critical exponent of a word 𝐰 \bf w, which is the supremum over the exponents of all prefixes of 𝐰 \bf w.

###### Theorem 28.

The initial critical exponent of 𝐟 \bf f is 1 + α 1+\alpha.

###### Proof.

We create an automaton M ice M_{\rm ice} accepting the language

 | L = { ( n, p) F: 𝐟 [0.. n − 1] has least period p }. L=\{(n,p)_{F}\ :\ {\bf f}[0..n-1]\text{ has least period }p\}. |  |

It is depicted in Figure 13 below. From the automaton, it is easy to see that the least period of the prefix of length n ≥ 1 n\geq 1 is F j F_{j} for j ≥ 2 j\geq 2 and F j + 1 − 1 ≤ n ≤ F j + 2 − 2 F_{j+1}-1\leq n\leq F_{j+2}-2. Hence the initial critical exponent is given by lim sup j → ∞ ( F j + 2 − 2) / F j \limsup_{j\rightarrow\infty}(F_{j+2}-2)/F_{j}, which is 1 + α 1+\alpha.

Figure 13: Automaton accepting least periods of prefixes of length n n

∎

### 3.10 The shift orbit closure

The shift orbit closure of a sequence 𝐱 \bf x is the set of all sequences 𝐭 \bf t with the property that each prefix of 𝐭 \bf t appears as a factor of 𝐱 \bf x. Note that this set can be much larger than the set of all suffixes of 𝐱 \bf x.

The following theorem is well known [14, Prop. 3, p. 34]:

###### Theorem 29.

The lexicographically least sequence in the shift orbit closure of 𝐟 \bf f is 0 ​ 𝐟 0{\bf f}, and the lexicographically greatest is 1 ​ 𝐟 1{\bf f}.

###### Proof.

We handle only the lexicographically least, leaving the lexicographically greatest to the reader.

The idea is to create a predicate P ⁡ ( n) P(n) for the lexicographically least sequence 𝐛 = b 0 b 1 b 2 ⋯ {\bf b}=b_{0}b_{1}b_{2}\cdots which is true iff b n = 1 b_{n}=1. The following predicate encodes, first, that b n = 1 b_{n}=1, and second, that if one chooses any length-( n + 1 n+1) factor t t of 𝐟 \bf f, then b 0 ⋯ b n b_{0}\cdots b_{n} is equal or lexicographically smaller than t t.

 | ∃ j ​ 𝐟 ​ [j + n] = 1 ∧ ∀ k ⁡ ( ( ∀ s ≤ n ​ 𝐟 ​ [j + s] = 𝐟 ⁡ [k + s]) ∨ CLOSE ( ∃ i ≤ n s. t. 𝐟 [j + i] < 𝐟 [k + i] ∧ ( ∀ t < i 𝐟 [j + t] = 𝐟 [k + t]))) \exists j\ {\bf f}[j+n]=1\ \wedge\ \forall k\ ((\forall s\leq n\ {\bf f}[j+s]={\bf f}[k+s])\ \vee\ \\ (\exists i\leq n\ {\text{s}.t.}\ {\bf f}[j+i]<{\bf f}[k+i]\ \wedge\ (\forall t<i\ {\bf f}[j+t]={\bf f}[k+t]))) |  |

When we do this we get the following automaton, which is easily seen to generate the sequence 0 ​ 𝐟 0{\bf f}.

Figure 14: Automaton accepting lexicographically least sequence in shift orbit closure of 𝐟 {\bf f}

∎

### 3.11 Minimal forbidden words

Let 𝐱 {\bf x} be an infinite word. A finite word z = a 0 ⋯ a n z=a_{0}\cdots a_{n} is said to be minimal forbidden if z z is not a factor of 𝐱 \bf x, but both a 1 ⋯ a n a_{1}\cdots a_{n} and a 0 ⋯ a n − 1 a_{0}\cdots a_{n-1} are [33].

We can characterize all minimal forbidden words as follows: we create an automaton accepting the language

 | { ( i, n) F: 𝐟 [i.. i + n − 1] 𝐟 ⁡ [n] ¯ is not a factor of 𝐟 and 𝐟 [i + 1.. i + n − 1] 𝐟 ⁡ [n] ¯ is a factor and i is as small as possible }. \{(i,n)_{F}\ :\ {\bf f}[i..i+n-1]\,\overline{{\bf f}[n]}\text{ is not a factor of $\bf f$ and }\\ {\bf f}[i+1..i+n-1]\,\overline{{\bf f}[n]}\text{ is a factor }\text{and }i\text{ is as small as possible }\}. |  |

When we do so we find the words accepted are

 | [1, 1] ​ ( [0, 0] ​ [1, 1]) ∗ ​ ( ϵ + [0, 0]). [1,1]([0,0][1,1])^{*}(\epsilon+[0,0]). |  |

This corresponds to the words

 | 𝐟 ⁡ [F n − 1..2 ​ F n − 3] ​ 𝐟 ⁡ [2 ​ F n − 2] ¯ {\bf f}[F_{n}-1..2F_{n}-3]\,\overline{{\bf f}[2F_{n}-2]} |  |

for n ≥ 3 n\geq 3. The first few are

 | 11,000, 10101, 00100100, 1010010100101, …. 11,000,10101,00100100,1010010100101,\ldots. |  |

### 3.12 Grouped factors

Cassaigne [23] introduced the notion of grouped factors. A sequence 𝐚 = ( a i) i ≥ 0 {\bf a}=(a_{i})_{i\geq 0} has grouped factors if, for all n ≥ 1 n\geq 1, there exists some position m = m ⁡ ( n) m=m(n) such that 𝐚 [m.. m + ρ ( n) + n − 2] {\bf a}[m..m+\rho(n)+n-2] contains all the ρ ⁡ ( n) \rho(n) length- n n blocks of 𝐚 \bf a, each block occurring exactly once. One consequence of his result is that the Fibonacci word has grouped factors.

We can write a predicate for the property of having grouped factors, as follows:

 | ∀ n ≥ 1 ∃ m, s ≥ 0 ∀ i ≥ 0 ∃ j s.t. m ≤ j ≤ m + s and 𝐚 [i.. i + n − 1] = 𝐚 [j.. j + n − 1] and ∀ j ′, m ≤ j ′ ≤ m + s, j ≠ j ′ we have 𝐚 [i.. i + n − 1] ≠ 𝐚 [j ′.. j ′ + n − 1]. \forall n\geq 1\quad\exists m,s\geq 0\quad\forall i\geq 0\\ \exists j\text{ s.t. }m\leq j\leq m+s\text{ and }{\bf a}[i..i+n-1]={\bf a}[j..j+n-1]\text{ and }\\ \forall j^{\prime},\ m\leq j^{\prime}\leq m+s,\quad j\not=j^{\prime}\text{ we have }{\bf a}[i..i+n-1]\not={\bf a}[j^{\prime}..j^{\prime}+n-1]. |  |

The first part of the predicate says that every length- n n block appears somewhere in the desired window, and the second says that it appears exactly once.

(This five-quantifier definition can be viewed as a response to the question of Homer and Selman [51], “…in what sense would a problem that required at least three alternating quantifiers to describe be natural?”)

Using this predicate and our decision method, we verified that the Fibonacci word does indeed have grouped factors.

## 4 Mechanical proofs of properties of the finite Fibonacci words

Although our program is designed to answer questions about the properties of the infinite Fibonacci word 𝐟 \bf f, it can also be used to solve problems concerning the finite Fibonacci words ( X n) (X_{n}), defined as follows:

 | X n = { ϵ, if n = 0; 1, if n = 1; 0, if n = 2; X n − 1 ​ X n − 2, if n > 2. X_{n}=\begin{cases}\epsilon,&\text{if $n=0$};\\ 1,&\text{if $n=1$};\\ 0,&\text{if $n=2$};\\ X_{n-1}X_{n-2},&\text{if $n>2$}.\end{cases} |  |

Note that | X n | = F n |X_{n}|=F_{n} for n ≥ 1 n\geq 1. (We caution the reader that there exist many variations on this definition in the literature, particularly with regard to indexing and initial values.) Furthermore, we have φ ⁡ ( X n) = X n + 1 \varphi(X_{n})=X_{n+1} for n ≥ 1 n\geq 1.

Our strategy for the the finite Fibonacci words has two parts:

- (i)

Instead of phrasing statements in terms of factors, we phrase them in terms of occurrences of factors (and hence in terms of the indices defining a factor).

- (ii)

Instead of phrasing statements about finite Fibonacci words, we phrase them instead about all length- n n prefixes of 𝐟 \bf f. Then, since X i = 𝐟 [0.. F i − 1] X_{i}={\bf f}[0..F_{i}-1], we can deduce results about the finite Fibonacci words by considering the case where n n is a Fibonacci number F i F_{i}.

To illustrate this idea, consider one of the most famous properties of the Fibonacci words, the almost-commutative property: letting η ( a 1 a 2 ⋯ a n) = a 1 a 2 ⋯ a n − 2 a n a n − 1 \eta(a_{1}a_{2}\cdots a_{n})=a_{1}a_{2}\cdots a_{n-2}a_{n}a_{n-1} be the map that interchanges the last two letters of a string of length at least 2 2, we have

###### Theorem 30.

X n − 1 ​ X n = η ⁡ ( X n ​ X n − 1) X_{n-1}X_{n}=\eta(X_{n}X_{n-1}) for n ≥ 2 n\geq 2.

We can verify this, and prove even more, using our method.

###### Theorem 31.

Let x = 𝐟 [0.. i − 1] x={\bf f}[0..i-1] and y = 𝐟 [0.. j − 1] y={\bf f}[0..j-1] for i > j > 1 i>j>1. Then x ​ y = η ⁡ ( y ​ x) xy=\eta(yx) if and only if i = F n i=F_{n}, j = F n − 1 j=F_{n-1} for n ≥ 3 n\geq 3.

###### Proof.

The idea is to check, for each i > j > 1 i>j>1, whether

 | 𝐟 [0.. i − 1] 𝐟 [0.. j − 1] = η ( 𝐟 [0.. j − 1] 𝐟 [0.. i − 1]). {\bf f}[0..i-1]{\bf f}[0..j-1]=\eta({\bf f}[0..j-1]{\bf f}[0..i-1]). |  |

We can do this with the following predicate:

 | ( i > j) ∧ ( j ≥ 2) ∧ ( ∀ t, j ≤ t < i, 𝐟 [t] = 𝐟 [t − j]) ∧ ( ∀ s ≤ j − 3 ​ 𝐟 ​ [s] = 𝐟 ⁡ [s + i − j]) ∧ ( 𝐟 ⁡ [j − 2] = 𝐟 ⁡ [i − 1]) ∧ ( 𝐟 ⁡ [j − 1] = 𝐟 ⁡ [i − 2]). (i>j)\ \wedge\ (j\geq 2)\ \wedge\ (\forall t,\ j\leq t<i,\ {\bf f}[t]={\bf f}[t-j])\ \wedge\\ (\forall s\leq j-3\ {\bf f}[s]={\bf f}[s+i-j])\ \wedge\ ({\bf f}[j-2]={\bf f}[i-1])\ \wedge\ ({\bf f}[j-1]={\bf f}[i-2]). |  |

The log of our program is as follows:

```

i > j with 7 states, in 49ms
 j >= 2 with 5 states, in 87ms
  i > j & j >= 2 with 12 states, in 3ms
   j <= t with 7 states, in 3ms
    t < i with 7 states, in 17ms
     j <= t & t < i with 19 states, in 6ms
      F[t] = F[t - j] with 16 states, in 31ms
       j <= t & t < i => F[t] = F[t - j] with 62 states, in 31ms
        At j <= t & t < i => F[t] = F[t - j] with 14 states, in 43ms
         i > j & j >= 2 & At j <= t & t < i => F[t] = F[t - j] with 12 states, in 9ms
          s <= j - 3 with 14 states, in 72ms
           F[s] = F[s + i - j] with 60 states, in 448ms
            s <= j - 3 => F[s] = F[s + i - j] with 119 states, in 14ms
             As s <= j - 3 => F[s] = F[s + i - j] with 17 states, in 58ms
              i > j & j >= 2 & At j <= t & t < i => F[t] = F[t - j] & As s <= j - 3 => F[s] = F[s + i - j] with 6 states, in 4ms
               F[j - 2] = F[i - 1] with 20 states, in 34ms
                i > j & j >= 2 & At j <= t & t < i => F[t] = F[t - j] & As s <= j - 3 => F[s] = F[s + i - j] & F[j - 2] = F[i - 1] with 5 states, in 1ms
                 F[j - 1] = F[i - 2] with 20 states, in 29ms
                  i > j & j >= 2 & At j <= t & t < i => F[t] = F[t - j] & As s <= j - 3 => F[s] = F[s + i - j] & F[j - 2] = F[i - 1] & F[j - 1] = F[i - 2] with 5 states, in 1ms
overall time: 940ms
```

The resulting automaton accepts [1, 0] ​ [0, 1] ​ [0, 0] + [1,0][0,1][0,0]^{+}, which corresponds to i = F n i=F_{n}, j = F n − 1 j=F_{n-1} for n ≥ 4 n\geq 4. ∎

An old result of Séébold [71] is

###### Theorem 32.

If u ​ u uu is a square occurring in 𝐟 \bf f, then u u is conjugate to some finite Fibonacci word.

###### Proof.

Assertion conj ⁡ ( i, j, k, ℓ) \conj(i,j,k,\ell) means 𝐟 [i.. j] {\bf f}[i..j] is a conjugate of 𝐟 [k.. ℓ] {\bf f}[k..\ell] (assuming j − i = ℓ − k j-i=\ell-k)

 | conj ( i, j, k, ℓ):= ∃ m 𝐟 [i.. i + ℓ − m] = 𝐟 [m.. ℓ] and 𝐟 [i + ℓ − m + 1.. j] = 𝐟 [k.. m − 1]. \conj(i,j,k,\ell):=\exists m\ {\bf f}[i..i+\ell-m]={\bf f}[m..\ell]\text{ and }{\bf f}[i+\ell-m+1..j]={\bf f}[k..m-1]. |  |

Predicate:

 | ( 𝐟 [i.. i + n − 1] = 𝐟 [i + n.. i + 2 n − 1]) ⟹ conj ( i, i + n − 1, 0, n − 1) ({\bf f}[i..i+n-1]={\bf f}[i+n..i+2n-1])\implies\conj(i,i+n-1,0,n-1) |  |

This asserts that any square u ​ u uu of order n n appearing in 𝐟 \bf f is conjugate to 𝐟 [0.. n − 1] {\bf f}[0..n-1]. When we implement this, we discover that all lengths are accepted. This makes sense since the only lengths corresponding to squares are F n F_{n}, and for all other lengths the base of the implication is false. ∎

We now reprove an old result of de Luca [35]. Recall that a primitive word is a non-power; that is, a word that cannot be written in the form x n x^{n} where n n is an integer ≥ 2 \geq 2.

###### Theorem 33.

All finite Fibonacci words are primitive.

###### Proof.

The factor 𝐟 [i.. j] {\bf f}[i..j] is a power if and only if there exists d d, 0 < d < j − i + 1 0<d<j-i+1, such that 𝐟 [i.. j − d] = 𝐟 [i + d.. j] {\bf f}[i..j-d]={\bf f}[i+d..j] and 𝐟 [j − d + 1.. j] = 𝐟 [i.. i + d − 1] {\bf f}[j-d+1..j]={\bf f}[i..i+d-1]. Letting pow ⁡ ( i, j) \pow(i,j) denote this predicate, the predicate

 | ¬ pow ⁡ ( 0, n − 1) \neg\pow(0,n-1) |  |

expresses the claim that the length- n n prefix 𝐟 [0.. n − 1] {\bf f}[0..n-1] is primitive. When we implement this, we discover that the prefix of every length is primitive, except those prefixes of length 2 ​ F n 2F_{n} for n ≥ 4 n\geq 4. ∎

A theorem of Chuan [27, Thm. 3] states that the finite Fibonacci word X n X_{n}, for n ≥ 5 n\geq 5, is the product of two palindromes in exactly one way: where the first factor of length F n − 1 − 2 F_{n-1}-2 and the second of length F n − 2 + 2 F_{n-2}+2. (Actually, Chuan claimed this was true for all Fibonacci words, but, for example, for 010 010 there are evidently two different factorizations of the form ( ϵ) ​ ( 010) (\epsilon)(010) and ( 010) ​ ϵ (010)\epsilon.) We can prove something more general using our method, by generalizing:

###### Theorem 34.

If the length- n n prefix 𝐟 [0.. n − 1] {\bf f}[0..n-1] of 𝐟 \bf f is the product of two (possibly empty) palindromes, then ( n) F (n)_{F} is accepted by the automaton in Figure 15 below.

Figure 15: Automaton accepting lengths of prefixes that are the product of two palindromes

Furthermore, if the length- n n prefix 𝐟 [0.. n − 1] {\bf f}[0..n-1] of 𝐟 \bf f is the product of two (possibly empty) palindromes in exactly one way, then ( n) F (n)_{F} is accepted by the automaton in Figure 16 below.

Figure 16: Automaton accepting lengths of prefixes that are the product of two palindromes in exactly one way

Evidently, this includes all n n of the form F j F_{j} for j ≥ 5 j\geq 5.

###### Proof.

For the first, we use the predicate

 | ∃ p ≤ n ⁡ ( ( ∀ t < p ​ 𝐟 ​ [t] = 𝐟 ⁡ [p − 1 − t]) ∧ ( ∀ u < n − p ​ 𝐟 ​ [p + u] = 𝐟 ⁡ [n − 1 − u])). \exists p\leq n\ \left((\forall t<p\ {\bf f}[t]={\bf f}[p-1-t])\ \wedge\ (\forall u<n-p\ {\bf f}[p+u]={\bf f}[n-1-u])\right). |  |

For the second, we use the predicate

 | OPEN ∃ p ≤ n ⁡ ( ( ∀ t < p ​ 𝐟 ​ [t] = 𝐟 ⁡ [p − 1 − t]) ∧ ( ∀ u < n − p ​ 𝐟 ​ [p + u] = 𝐟 ⁡ [n − 1 − u]))) ∧ ( ∀ q ≤ n ⁡ ( ( ∀ m < q ​ 𝐟 ​ [m] = 𝐟 ⁡ [q − 1 − m]) ∧ ( ∀ v < n − q ​ 𝐟 ​ [q + v] = 𝐟 ⁡ [n − 1 − v])) ⟹ p = q). \exists p\leq n\ ((\forall t<p\ {\bf f}[t]={\bf f}[p-1-t])\ \wedge\ (\forall u<n-p\ {\bf f}[p+u]={\bf f}[n-1-u])))\ \wedge\ \\ (\forall q\leq n\ ((\forall m<q\ {\bf f}[m]={\bf f}[q-1-m])\ \wedge\ (\forall v<n-q\ {\bf f}[q+v]={\bf f}[n-1-v]))\implies p=q). |  |

∎

A result of Cummings, Moore, and Karhumäki [30] states that the borders of the finite Fibonacci word 𝐟 [0.. F n − 1] {\bf f}[0..F_{n}-1] are precisely the words 𝐟 [0.. F n − 2 ​ k − 1] {\bf f}[0..F_{n-2k}-1] for 2 ​ k < n 2k<n. We can prove this, and more:

###### Proof.

Consider the pairs ( n, m) (n,m) such that 1 ≤ m < n 1\leq m<n and 𝐟 [0.. m − 1] {\bf f}[0..m-1] is a border of 𝐟 [0.. n − 1] {\bf f}[0..n-1]. Their Fibonacci representations are accepted by the automaton below in Figure 17.

Figure 17: Automaton encoding borders of prefixes of 𝐟 \bf f

We use the predicate

 | ( n > m) ∧ ( m ≥ 1) ∧ ∀ i < m ​ 𝐟 ​ [i] = 𝐟 ⁡ [n − m + i]. (n>m)\ \wedge\ (m\geq 1)\ \wedge\ \forall i<m\ {\bf f}[i]={\bf f}[n-m+i]. |  |

By following the paths with first coordinate of the form 10 + 10^{+} we recover the result of Cummings, Moore, and Karhumäki as a special case. ∎

## 5 Avoiding the pattern x ​ x ​ x R xxx^{R} and the Rote-Fibonacci word

In this section we show how to apply our decision method to an interesting and novel avoidance property: avoiding the pattern x ​ x ​ x R xxx^{R}. An example matching this pattern in English is a factor of the word bepepper, with x = 𝚎𝚙 x={\tt ep}. Here, however, we are concerned only with the binary alphabet Σ 2 = { 0, 1 } \Sigma_{2}=\{0,1\}.

Although avoiding patterns with reversal has been considered before (e.g., [64, 10, 32, 9]), it seems our particular problem has not been studied.

If our goal is just to produce some infinite word avoiding x ​ x ​ x R xxx^{R}, then a solution seems easy: namely, the infinite word ( 01) ω (01)^{\omega} clearly avoids x ​ x ​ x R xxx^{R}, since if | x | = n |x|=n is odd, then the second factor of length n n cannot equal the first (since the first symbol differs), while if | x | = n |x|=n is even, the first symbol of the third factor of length n n cannot be the last symbol of x x. In a moment we will see that even this question seems more subtle than it first appears, but for the moment, we’ll change our question to

Are there infinite aperiodic binary words avoiding x ​ x ​ x R xxx^{R}?

To answer this question, we’ll study a special infinite word, which we call the Rote-Fibonacci word. (The name comes from the fact that it is a special case of a class of words discussed in 1994 by Rote [66].) Consider the following transducer T T:

q 0 q_{0} q 1 q_{1} 0 / 00, 1 / 0 0 / 11, 1 / 1 Figure 18: Transducer converting Fibonacci words to Rote-Fibonacci words

This transducer acts on words by following the transitions and outputting the concatenation of the outputs associated with each transition. Thus, for example, the input 01001 01001 gets transduced to the output 00100110 00100110.

###### Theorem 35.

The Rote-Fibonacci word

 | 𝐫 = 001001101101100100110110110010010011011001001001101100100100 ⋯ = r 0 r 1 r 2 ⋯ {\bf r}=001001101101100100110110110010010011011001001001101100100100\cdots=r_{0}r_{1}r_{2}\cdots |  |

has the following equivalent descriptions:

0. As the output of the transducer T T, starting in state 0 0, on input 𝐟 \bf f.

1. As τ ​ ( h ω ​ ( a)) \tau(h^{\omega}(a)) where h h and τ \tau are defined by

 | h ⁡ ( a) \displaystyle h(a) | = a ​ b 1 \displaystyle=ab_{1} | τ ⁡ ( a) = 0 \displaystyle\quad\tau(a)=0 |  |

 | h ⁡ ( b) \displaystyle h(b) | = a \displaystyle=a | τ ⁡ ( b) = 1 \displaystyle\quad\tau(b)=1 |  |

 | h ⁡ ( a 0) \displaystyle h(a_{0}) | = a 2 ​ b \displaystyle=a_{2}b | τ ⁡ ( a 0) = 0 \displaystyle\quad\tau(a_{0})=0 |  |

 | h ⁡ ( a 1) \displaystyle h(a_{1}) | = a 0 ​ b 0 \displaystyle=a_{0}b_{0} | τ ⁡ ( a 1) = 1 \displaystyle\quad\tau(a_{1})=1 |  |

 | h ⁡ ( a 2) \displaystyle h(a_{2}) | = a 1 ​ b 2 \displaystyle=a_{1}b_{2} | τ ⁡ ( a 2) = 1 \displaystyle\quad\tau(a_{2})=1 |  |

 | h ⁡ ( b 0) \displaystyle h(b_{0}) | = a 0 \displaystyle=a_{0} | τ ⁡ ( b 0) = 0 \displaystyle\quad\tau(b_{0})=0 |  |

 | h ⁡ ( b 1) \displaystyle h(b_{1}) | = a 1 \displaystyle=a_{1} | τ ⁡ ( b 1) = 0 \displaystyle\quad\tau(b_{1})=0 |  |

 | h ⁡ ( b 2) \displaystyle h(b_{2}) | = a 2 \displaystyle=a_{2} | τ ⁡ ( b 2) = 1 \displaystyle\quad\tau(b_{2})=1 |  |

2. As the binary sequence generated by the following DFAO, with outputs given in the states, and inputs in the Fibonacci representation of n n.

a / 𝟶 a/{\tt 0} b 1 / 𝟶 b_{1}/{\tt 0} a 1 / 𝟷 a_{1}/{\tt 1} b 0 / 𝟶 b_{0}/{\tt 0} b / 𝟷 b/{\tt 1} a 0 / 𝟶 a_{0}/{\tt 0} a 2 / 𝟷 a_{2}/{\tt 1} b 2 / 𝟷 b_{2}/{\tt 1} 0 1 0 1 0 0 0 1 0 0 1 0 Figure 19: Canonical Fibonacci representation DFAO generating the Rote-Fibonacci word

3. As the limit, as n → ∞ n\rightarrow\infty, of the sequence of finite Rote-Fibonacci words ( R n) n (R_{n})_{n} defined as follows: R 0 = 0 R_{0}=0, R 1 = 00 R_{1}=00, and for n ≥ 3 n\geq 3

 | R n = { R n − 1 ​ R n − 2, if n ≡ 0 (mod 3); R n − 1 ​ R n − 2 ¯, if n ≡ 1, 2 (mod 3). R_{n}=\begin{cases}R_{n-1}R_{n-2},&\text{ if $n\equiv 0$ (mod 3);}\\ R_{n-1}\overline{R_{n-2}},&\text{ if $n\equiv 1,2$ (mod 3).}\end{cases} |  |

4. As the sequence obtained from the Fibonacci sequence 𝐟 = f 0 f 1 f 2 ⋯ = 0100101001001 ⋯ {\bf f}=f_{0}f_{1}f_{2}\cdots=0100101001001\cdots as follows: first, change every 0 0 to 1 1 and every one to 0 0 in 𝐟 {\bf f}, obtaining 𝐟 ¯ = 𝟏𝟎𝟏𝟏𝟎𝟏𝟎𝟏𝟏𝟎𝟏𝟏𝟎 ⋯ \overline{\bf f}=1011010110110\cdots. Next, in 𝐟 ¯ \overline{\bf f} change every second 1 1 that appears to − 1 -1 (which we write as 1 ¯ {\overline{1}} for clarity): 10 1 ¯ 10 1 ¯ 01 1 ¯ 01 1 ¯ 0 ⋯ 10{\overline{1}}10{\overline{1}}01{\overline{1}}01{\overline{1}}0\cdots. Now take the running sum of this sequence, obtaining 1101100100100 ⋯ 1101100100100\cdots, and finally, complement it to get 𝐫 \bf r.

5. As ρ ​ ( g ω ​ ( a)) \rho(g^{\omega}(a)), where g g and ρ \rho are defined as follows

 | g ⁡ ( a) \displaystyle g(a) | = a ​ b ​ c ​ a ​ b \displaystyle=abcab\quad | ρ ⁡ ( a) = 0 \displaystyle\rho(a)=0 |  |

 | g ⁡ ( b) \displaystyle g(b) | = c ​ d ​ a \displaystyle=cda\quad | ρ ⁡ ( b) = 0 \displaystyle\rho(b)=0 |  |

 | g ⁡ ( c) \displaystyle g(c) | = c ​ d ​ a ​ c ​ d \displaystyle=cdacd\quad | ρ ⁡ ( c) = 1 \displaystyle\rho(c)=1 |  |

 | g ⁡ ( d) \displaystyle g(d) | = a ​ b ​ c \displaystyle=abc\quad | ρ ⁡ ( d) = 1 \displaystyle\rho(d)=1 |  |

###### Proof.

( 0) ⇔ ( 3) (0)\iff(3): Let T 0 ​ ( x) T_{0}(x) (resp., T 1 ​ ( x) T_{1}(x)) denote the output of the transducer T T starting in state q 0 q_{0} (resp., q 1 q_{1}) on input x x. Then a simple induction on n n shows that T 0 ​ ( X n + 1) = R n T_{0}(X_{n+1})=R_{n} and T 1 ​ ( X n + 1) = R n ¯ T_{1}(X_{n+1})=\overline{R_{n}}. We give only the induction step for the first claim:

 | T 0 ​ ( X n + 1) \displaystyle T_{0}(X_{n+1}) | = T 0 ​ ( X n ​ X n − 1) \displaystyle=T_{0}(X_{n}X_{n-1}) |  |

 |  | = { T 0 ​ ( X n) ​ T 0 ​ ( X n − 1), if | X n | is even; T 0 ​ ( X n) ​ T 1 ​ ( X n − 1), if | X n | is odd; \displaystyle=\begin{cases}T_{0}(X_{n})T_{0}(X_{n-1}),&\text{if $|X_{n}|$ is even};\\ T_{0}(X_{n})T_{1}(X_{n-1}),&\text{if $|X_{n}|$ is odd};\end{cases} |  |

 |  | = { R n − 1 ​ R n − 2, if n ≡ 0 (mod 3); R n − 1 ​ R n − 2 ¯, if n ≢ 0 (mod 3); \displaystyle=\begin{cases}R_{n-1}R_{n-2},&\text{if $n\equiv 0$ (mod 3)};\\ R_{n-1}\overline{R_{n-2}},&\text{if $n\not\equiv 0$ (mod 3)};\end{cases} |  |

 |  | = R n. \displaystyle=R_{n}. |  |

Here we have used the easily-verified fact that | X n | = F n |X_{n}|=F_{n} is even iff n ≡ 0 n\equiv 0 (mod 3 3).

( 1) ⇔ ( 3) (1)\iff(3): we verify by a tedious induction on n n that for n ≥ 0 n\geq 0 we have

 | τ ​ ( h n ​ ( a)) \displaystyle\tau(h^{n}(a)) | = τ ⁡ ( h n + 1 ​ ( a)) = R n \displaystyle=\tau(h^{n+1}(a))=R_{n} |  |

 | τ ⁡ ( h n ​ ( a i)) \displaystyle\tau(h^{n}(a_{i})) | = τ ⁡ ( h n + 1 ​ ( b i)) = { R i, if n ≡ i (mod 3); R i ¯, if n ≢ i (mod 3). \displaystyle=\tau(h^{n+1}(b_{i}))=\begin{cases}R_{i},&\text{if $n\equiv i$ (mod 3)};\\ \overline{R_{i}},&\text{if $n\not\equiv i$ (mod 3)}.\end{cases} |  |

( 2) ⇔ ( 4) (2)\iff(4): Follows from the well-known transformation from automata to morphisms and vice versa (see, e.g., [50]).

( 3) ⇔ ( 4) (3)\iff(4): We define some transformations on sequences, as follows:

- •

C ⁡ ( x) C(x) denotes x ¯ \overline{x}, the complement of x x;

- •

s ⁡ ( x) s(x) denotes the sequence arising from a binary sequence x x by changing every second 1 1 to − 1 -1;

- •

a ⁡ ( x) a(x) denotes the running sum of the sequence x x; that is, if x = a 1 a 2 a 3 ⋯ x=a_{1}a_{2}a_{3}\cdots then a ⁡ ( x) a(x) is a 1 ( a 1 + a 2) ( a 1 + a 2 + a 3) ⋯ a_{1}(a_{1}+a_{2})(a_{1}+a_{2}+a_{3})\cdots.

Note that

 | a ⁡ ( s ⁡ ( x ​ y)) = { a ⁡ ( s ⁡ ( x)) ​ a ​ ( s ⁡ ( y)), if | x | 1 even; a ⁡ ( s ⁡ ( x)) ​ C ​ ( a ⁡ ( s ⁡ ( y))), if | x | 1 odd. a(s(xy))=\begin{cases}a(s(x))\ a(s(y)),&\text{if $|x|_{1}$ even};\\ a(s(x))\ C(a(s(y))),&\text{if $|x|_{1}$ odd}.\end{cases} |  |

Then we claim that C ⁡ ( R n) = a ⁡ ( s ⁡ ( C ⁡ ( X n + 2))) C(R_{n})=a(s(C(X_{n+2}))). This can be verified by induction on n n. We give only the induction step:

 | a ⁡ ( s ⁡ ( C ⁡ ( X n + 2))) \displaystyle a(s(C(X_{n+2}))) | = a ⁡ ( s ⁡ ( C ⁡ ( X n + 1) ​ C ​ ( X n))) \displaystyle=a(s(C(X_{n+1})C(X_{n}))) |  |

 |  | = { a ⁡ ( s ⁡ ( C ⁡ ( X n + 1))) ​ a ​ ( s ⁡ ( C ⁡ ( X n))), if C ​ ( X n + 1) 1 even; a ⁡ ( s ⁡ ( C ⁡ ( X n + 1))) ​ C ​ ( a ⁡ ( s ⁡ ( C ⁡ ( X n)))), if C ​ ( X n + 1) 1 odd; \displaystyle=\begin{cases}a(s(C(X_{n+1})))\ a(s(C(X_{n}))),&\text{ if $C(X_{n+1})_{1}$ even};\\ a(s(C(X_{n+1})))\ C(a(s(C(X_{n})))),&\text{ if $C(X_{n+1})_{1}$ odd};\end{cases} |  |

 |  | = { C ⁡ ( R n − 1) ​ C ​ ( R n − 2), if n ≡ 0 (mod 3); C ⁡ ( R n − 1) ​ R n − 2, if n ≢ 0 (mod 3); \displaystyle=\begin{cases}C(R_{n-1})\ C(R_{n-2}),&\text{ if $n\equiv 0$ (mod 3)};\\ C(R_{n-1})\ R_{n-2},&\text{ if $n\not\equiv 0$ (mod 3)};\end{cases} |  |

 |  | = R n. \displaystyle=R_{n}. |  |

( 3) ⇔ ( 5) (3)\iff(5): Define γ \gamma by

 | γ ⁡ ( a) \displaystyle\gamma(a) | = γ ⁡ ( a 0) = a \displaystyle=\gamma(a_{0})=a |  |

 | γ ⁡ ( b 0) \displaystyle\gamma(b_{0}) | = γ ⁡ ( b 1) = b \displaystyle=\gamma(b_{1})=b |  |

 | γ ⁡ ( a 1) \displaystyle\gamma(a_{1}) | = γ ⁡ ( a 2) = c \displaystyle=\gamma(a_{2})=c |  |

 | γ ⁡ ( b) \displaystyle\gamma(b) | = γ ⁡ ( b 2) = d. \displaystyle=\gamma(b_{2})=d. |  |

We verify by a tedious induction on n n that for n ≥ 0 n\geq 0 we have

 | g n ​ ( a) \displaystyle g^{n}(a) | = γ ⁡ ( h 3 ​ n ​ ( a)) = γ ⁡ ( h 3 ​ n ​ ( a 0)) \displaystyle=\gamma(h^{3n}(a))=\gamma(h^{3n}(a_{0})) |  |

 | g n ​ ( b) \displaystyle g^{n}(b) | = γ ⁡ ( h 3 ​ n ​ ( b 0)) = γ ⁡ ( h 3 ​ n ​ ( b 1)) \displaystyle=\gamma(h^{3n}(b_{0}))=\gamma(h^{3n}(b_{1})) |  |

 | g n ​ ( c) \displaystyle g^{n}(c) | = γ ⁡ ( h 3 ​ n ​ ( a 1)) = γ ⁡ ( h 3 ​ n ​ ( a 2)) \displaystyle=\gamma(h^{3n}(a_{1}))=\gamma(h^{3n}(a_{2})) |  |

 | g n ​ ( d) \displaystyle g^{n}(d) | = γ ⁡ ( h 3 ​ n ​ ( b)) = γ ⁡ ( h 3 ​ n ​ ( b 2)). \displaystyle=\gamma(h^{3n}(b))=\gamma(h^{3n}(b_{2})). |  |

∎

###### Corollary 36.

The first differences Δ ​ 𝐫 \Delta{\bf r} of the Rote-Fibonacci word 𝐫 \bf r, taken modulo 2 2, give the complement of the Fibonacci word f ¯ \overline{f}, with its first symbol omitted.

###### Proof.

Note that if 𝐱 = a 0 a 1 a 2 ⋯ {\bf x}=a_{0}a_{1}a_{2}\cdots is a binary sequence, then Δ ⁡ ( C ⁡ ( 𝐱)) = − Δ ⁡ ( 𝐱) \Delta(C({\bf x}))=-\Delta({\bf x}). Furthermore Δ ( a ( x)) = a 1 a 2 ⋯ \Delta(a(x))=a_{1}a_{2}\cdots. Now from the description in part 4, above, we know that 𝐫 = C ⁡ ( a ⁡ ( s ⁡ ( C ⁡ ( 𝐟)))) {\bf r}=C(a(s(C({\bf f})))). Hence Δ ⁡ ( 𝐫) = Δ ⁡ ( C ⁡ ( a ⁡ ( s ⁡ ( C ⁡ ( 𝐟))))) = − Δ ⁡ ( a ⁡ ( s ⁡ ( C ⁡ ( 𝐟)))) = dr ⁡ ( − s ⁡ ( C ⁡ ( 𝐟))) \Delta({\bf r})=\Delta(C(a(s(C({\bf f})))))=-\Delta(a(s(C({\bf f}))))=\dr(-s(C({\bf f}))), where dr \dr drops the first symbol of its argument. Taking the last result modulo 2 2 gives the result. ∎

We are now ready to prove our avoidability result.

###### Theorem 37.

The Rote-Fibonacci word 𝐫 \bf r avoids the pattern x ​ x ​ x R xxx^{R}.

###### Proof.

We use our decision procedure to prove this. A predicate is as follows:

 | ∃ i ​ ∀ t < n ⁡ ( 𝐫 ⁡ [i + t] = 𝐫 ⁡ [i + t + n]) ∧ ( 𝐫 ⁡ [i + t] = 𝐫 ⁡ [i + 3 ​ n − 1 − t]). \exists i\ \forall t<n\ ({\bf r}[i+t]={\bf r}[i+t+n])\ \wedge\ ({\bf r}[i+t]={\bf r}[i+3n-1-t]). |  |

When we run this on our program, we get the following log:

```

t < n with 7 states, in 36ms
 R[i + t] = R[i + t + n] with 245 states, in 1744ms
  R[i + t] = R[i + 3 * n - 1 - t] with 1751 states, in 14461ms
   R[i + t] = R[i + t + n] & R[i + t] = R[i + 3 * n - 1 - t] with 3305 states, in 565ms
    t < n => R[i + t] = R[i + t + n] & R[i + t] = R[i + 3 * n - 1 - t] with 2015 states, in 843ms
     At t < n => R[i + t] = R[i + t + n] & R[i + t] = R[i + 3 * n - 1 - t] with 3 states, in 747ms
      Ei At t < n => R[i + t] = R[i + t + n] & R[i + t] = R[i + 3 * n - 1 - t] with 2 states, in 0ms
overall time: 18396ms
```

Then the only length n n accepted is n = 0 n=0, so the Rote-Fibonacci word 𝐫 \bf r contains no occurrences of the pattern x ​ x ​ x R xxx^{R}. ∎

We now prove some interesting properties of 𝐫 \bf r.

###### Theorem 38.

The minimum q ⁡ ( n) q(n) over all periods of all length- n n factors of the Rote-Fibonacci word is as follows:

 | q ⁡ ( n) = { 1, if 1 ≤ n ≤ 2; 2, if n = 3; F 3 ​ j + 1, if j ≥ 1 and L 3 ​ j ≤ n < L 3 ​ j + 2; L 3 ​ j + 1, if j ≥ 1 and L 3 ​ j + 2 ≤ n < L 3 ​ j + 2 + F 3 ​ j − 2; F 3 ​ j + 2 + L 3 ​ j, if j ≥ 2 and L 3 ​ j + 2 + F 3 ​ j − 2 ≤ n < L 3 ​ j + 2 + F 3 ​ j − 1; 2 ​ F 3 ​ j + 2, if L 3 ​ j + 2 + F 3 ​ j − 1 ≤ n < L 3 ​ j + 3. q(n)=\begin{cases}1,&\text{if $1\leq n\leq 2$;}\\ 2,&\text{if $n=3$;}\\ F_{3j+1},&\text{if $j\geq 1$ and $L_{3j}\leq n<L_{3j+2}$;}\\ L_{3j+1},&\text{if $j\geq 1$ and $L_{3j+2}\leq n<L_{3j+2}+F_{3j-2}$;}\\ F_{3j+2}+L_{3j},&\text{if $j\geq 2$ and $L_{3j+2}+F_{3j-2}\leq n<L_{3j+2}+F_{3j-1}$;}\\ 2F_{3j+2},&\text{if $L_{3j+2}+F_{3j-1}\leq n<L_{3j+3}$}.\end{cases} |  |

###### Proof.

To prove this, we mimic the proof of Theorem 20. The resulting automaton is displayed below in Figure 20.

Figure 20: Automaton accepting least periods of prefixes of length n n

∎

###### Corollary 39.

The critical exponent of the Rote-Fibonacci word is 2 + α 2+\alpha.

###### Proof.

An examination of the cases in Theorem 38 show that the words of maximum exponent are those corresponding to n = L 3 ​ j + 2 − 1 n=L_{3j+2}-1, p = F 3 ​ j + 1 p=F_{3j+1}. As j → ∞ j\rightarrow\infty, the quantity n / p n/p approaches 2 + α 2+\alpha from below. ∎

###### Theorem 40.

All squares in the Rote-Fibonacci word are of order F 3 ​ n + 1 F_{3n+1} for n ≥ 0 n\geq 0, and each such order occurs.

###### Proof.

We use the predicate

 | ( n ≥ 1) ∧ ∃ i ​ ∀ j < n ⁡ ( 𝐫 ⁡ [i + j] = 𝐫 ⁡ [i + j + n]). (n\geq 1)\ \wedge\ \exists i\ \forall j<n\ ({\bf r}[i+j]={\bf r}[i+j+n]). |  |

The resulting automaton is depicted in Figure 21. The accepted words correspond to F 3 ​ n + 1 F_{3n+1} for n ≥ 0 n\geq 0.

Figure 21: Automaton accepting orders of squares in the Rote-Fibonacci word

∎

We now turn to problems considering prefixes of the Rote-Fibonacci word 𝐫 \bf r.

###### Theorem 41.

A length- n n prefix of the Rote-Fibonacci word 𝐫 \bf r is an antipalindrome iff n = F 3 ​ i + 1 − 3 n=F_{3i+1}-3 for some i ≥ 1 i\geq 1.

###### Proof.

We use our decision method on the predicate

 | ∀ j < n ​ 𝐫 ​ [j] ≠ 𝐫 ⁡ [n − 1 − j]. \forall j<n\ {\bf r}[j]\not={\bf r}[n-1-j]. |  |

The result is depicted in Figure 22. The only accepted expansions are given by the regular expression ϵ + 1 ​ ( 010101) ∗ ​ 0 ​ ( 010 + 101000) \epsilon+1(010101)^{*}0(010+101000), which corresponds to F 3 ​ j + 1 − 3 F_{3j+1}-3. We use the predicate

 | OPEN ( n ≥ 1) ∧ ∃ i ​ ∀ j < n ​ 𝐫 ​ [i + j] = 𝐫 ⁡ [i + j + n]). (n\geq 1)\ \wedge\ \exists i\ \forall j<n\ {\bf r}[i+j]={\bf r}[i+j+n]). |  |

The resulting automaton is depicted in Figure 22. The accepted words correspond to F 3 ​ n + 1 F_{3n+1} for n ≥ 0 n\geq 0.

Figure 22: Automaton accepting lengths of antipalindrome prefixes in the Rote-Fibonacci word

∎

###### Theorem 42.

A length- n n prefix of the Rote-Fibonacci word is an antisquare if and only if n = 2 ​ F 3 ​ k + 2 n=2F_{3k+2} for some k ≥ 1 k\geq 1.

###### Proof.

The predicate for having an antisquare prefix of length n n is

 | ∀ k < n ​ 𝐫 ​ [i + k] ≠ 𝐫 ⁡ [i + k + n]. \forall k<n\ {\bf r}[i+k]\not={\bf r}[i+k+n]. |  |

When we run this we get the automaton depicted in Figure 23.

Figure 23: Automaton accepting orders of antisquares that are prefixes of 𝐟 \bf f

∎

###### Theorem 43.

The Rote-Fibonacci word has subword complexity 2 ​ n 2n.

###### Proof.

Follows from Corollary 36 together with [66, Thm. 3]. ∎

###### Theorem 44.

The Rote-Fibonacci word is mirror invariant. That is, if z z is a factor of 𝐫 \bf r then so is z R z^{R}.

###### Proof.

We use the predicate

 | ∀ i ​ ∃ j ​ ∀ t < n ​ 𝐫 ​ [i + t] = 𝐫 ⁡ [j + n − 1 − t]. \forall i\ \exists j\ \forall t<n\ {\bf r}[i+t]={\bf r}[j+n-1-t]. |  |

The resulting automaton accepts all n n, so the conclusion follows. The largest intermediate automaton has 2300 states and the calculation took about 6 seconds on a laptop. ∎

###### Corollary 45.

The Rote-Fibonacci word avoids the pattern x ​ x R ​ x R xx^{R}x^{R}.

###### Proof.

Suppose x ​ x R ​ x R xx^{R}x^{R} occurs in 𝐫 \bf r. Then by Theorem 44 we know that ( x ​ x R ​ x R) R = x ​ x ​ x R (xx^{R}x^{R})^{R}=xxx^{R} occurs in 𝐟 \bf f. But this is impossible, by Theorem 37. ∎

As it turns out, the Rote-Fibonacci word has (essentially) appeared before in several places. For example, in a 2009 preprint of Monnerot-Dumaine [57], the author studies a plane fractal called the “Fibonacci word fractal”, specified by certain drawing instructions, which can be coded over the alphabet S, R, L S,R,L by taking the fixed point g ω ​ ( a) g^{\omega}(a) and applying the coding γ ⁡ ( a) = S \gamma(a)=S, γ ⁡ ( b) = R \gamma(b)=R, γ ⁡ ( c) = S \gamma(c)=S, and γ ⁡ ( d) = L \gamma(d)=L. Here S S means “move straight one unit”, “ R R ” means “right turn one unit” and “ L L ” means “left turn one unit”.

More recently, Blondin Massé, Brlek, Labbé, and Mendès France studied a remarkable sequence of words closely related to 𝐫 \bf r [11, 12, 13]. For example, in their paper “Fibonacci snowflakes” [11] they defined a certain sequence q i q_{i} which has the following relationship to g g: let ξ ⁡ ( a) = ξ ⁡ ( b) = L \xi(a)=\xi(b)=L, ξ ⁡ ( c) = ξ ⁡ ( d) = R \xi(c)=\xi(d)=R. Then

 | R ​ ξ ​ ( g n ​ ( a)) = q 3 ​ n + 2 ​ L. R\xi(g^{n}(a))=q_{3n+2}L. |  |

### 5.1 Conjectures and open problems about the Rote-Fibonacci word

In this section we collect some conjectures we have not yet been able to prove. We have made some progress and hope to completely resolve them in the future.

###### Conjecture 46.

Every infinite binary word avoiding the pattern x ​ x ​ x R xxx^{R} has critical exponent ≥ 2 + α \geq 2+\alpha.

###### Conjecture 47.

Let z z be a finite nonempty primitive binary word. If z ω z^{\omega} avoids x ​ x ​ x R xxx^{R}, then | z | = 2 ​ F 3 ​ n + 2 |z|=2F_{3n+2} for some integer n ≥ 0 n\geq 0. Furthermore, z z is a conjugate of the prefix 𝐫 ⁡ [0..2 ​ F 3 ​ n + 2 − 1] {\bf r}[0..2F_{3n+2}-1], for some n ≥ 0 n\geq 0. Furthermore, for n ≥ 1 n\geq 1 we have that z z is a conjugate of y ​ y ¯ y\overline{y}, where y = τ ​ ( h 3 ​ n ​ ( a)) y=\tau(h^{3n}(a)).

We can make some partial progress on this conjecture, as follows:

###### Theorem 48.

Let k ≥ 1 k\geq 1 and define n = 2 ​ F 3 ​ k + 2 n=2F_{3k+2}. Let z = 𝐫 [0.. n − 1] z={\bf r}[0..n-1]. Then z ω z^{\omega} contains no occurrence of the pattern x ​ x ​ x R xxx^{R}.

###### Proof.

We have already seen this for k = 0 k=0, so assume k ≥ 1 k\geq 1.

Suppose that z ω z^{\omega} does indeed contain an occurrence of x ​ x ​ x R xxx^{R} for some | x | = ℓ > 0 |x|=\ell>0. We consider each possibility for ℓ \ell and eliminate them in turn.

Case I: ℓ ≥ n \ell\geq n.

There are two subcases:

Case Ia: n | / ℓ n{\,|\kern-4.5pt/}\,\ell: In this case, by considering the first n n symbols of each of the two occurrences of x x in x ​ x ​ x R xxx^{R} in z ω z^{\omega}, we see that there are two different cyclic shifts of z z that are identical. This can only occur if 𝐫 [0.. n − 1] {\bf r}[0..n-1] is a power, and we know from Theorem 40 and Corollary 39 that this implies that n = 2 ​ F 3 ​ k + 1 n=2F_{3k+1} or n = 3 ​ F 3 ​ k + 1 n=3F_{3k+1} for some k ≥ 0 k\geq 0. But 2 ​ F 3 ​ k + 1 ≠ 2 ​ F 3 ​ k ′ + 2 2F_{3k+1}\not=2F_{3k^{\prime}+2} and 3 ​ F 3 ​ k + 1 ≠ 2 ​ F 3 ​ k ′ + 2 3F_{3k+1}\not=2F_{3k^{\prime}+2} provided k, k ′ > 0 k,k^{\prime}>0, so this case cannot occur.

Case Ib: n | ℓ n\ |\ \ell: Then x x is a conjugate of z e z^{e}, where e = ℓ / n e=\ell/n. By a well-known result, a conjugate of a power is a power of a conjugate; hence there exists a conjugate y y of z z such that x = y e x=y^{e}. Then x R = y e x^{R}=y^{e}, so x x and hence y y is a palindrome. We can now create a predicate that says that some conjugate of 𝐫 [0.. n − 1] {\bf r}[0..n-1] is a palindrome:

 | ∃ i < n ∧ ( ∀ j < n ​ cmp ⁡ ( i + j, n + i − 1 − j)) \exists i<n\ \wedge\ (\forall j<n\ \cmp(i+j,n+i-1-j)) |  |

where

 | cmp ⁡ ( k, k ′):= ( ( ( k < n) ∧ ( k ′ < n)) ⟹ ( 𝐫 ⁡ [k] = 𝐫 ⁡ [k ′])) ∧ ( ( ( k < n) ∧ ( k ′ ≥ n)) ⟹ ( 𝐫 ⁡ [k] = 𝐫 ⁡ [k ′ − n])) ∧ ( ( ( k ≥ n) ∧ ( k ′ < n)) ⟹ ( 𝐫 ⁡ [k − n] = 𝐫 ⁡ [k ′])) ∧ ( ( ( k ≥ n) ∧ ( k ′ ≥ n)) = > ( 𝐫 ⁡ [k − n] = 𝐫 ⁡ [k ′ − n])). \cmp(k,k^{\prime}):=(((k<n)\ \wedge\ (k^{\prime}<n))\implies({\bf r}[k]={\bf r}[k^{\prime}]))\ \wedge\ \\ (((k<n)\ \wedge\ (k^{\prime}\geq n))\implies({\bf r}[k]={\bf r}[k^{\prime}-n]))\ \wedge\ \\ (((k\geq n)\ \wedge\ (k^{\prime}<n))\implies({\bf r}[k-n]={\bf r}[k^{\prime}]))\ \wedge\ \\ (((k\geq n)\ \wedge\ (k^{\prime}\geq n))=>({\bf r}[k-n]={\bf r}[k^{\prime}-n])). |  |

When we do this we discover the only n n with Fibonacci representation of the form 10010 i 10010^{i} accepted are those with i ≡ 0, 2 i\equiv 0,2 (mod 3 3), which means that 2 ​ F 3 ​ k + 2 2F_{3k+2} is not among them. So this case cannot occur.

Case II: ℓ < n \ell<n.

There are now four subcases to consider, depending on the number of copies of z z needed to “cover” our occurrence of x ​ x ​ x R xxx^{R}. In Case II. j j, for 1 ≤ j ≤ 4 1\leq j\leq 4, we consider j j copies of z z and the possible positions of x ​ x ​ x R xxx^{R} inside that copy.

Because of the complicated nature of comparing one copy of x x to itself in the case that one or both overlaps a boundary between different copies of z z, it would be very helpful to be able to encode statements like 𝐫 ⁡ [k mod n] = 𝐫 ⁡ [ℓ mod n] {\bf r}[k\bmod n]={\bf r}[\ell\bmod n] in our logical language. Unfortunately, we cannot do this if n n is arbitrary. So instead, we use a trick: assuming that the indices k, k ′ k,k^{\prime} satisfy 0 ≤ k, k ′ < 2 ​ n 0\leq k,k^{\prime}<2n, we can use the cmp ⁡ ( k, k ′) \cmp(k,k^{\prime}) predicate introduced above to simulate the assertion 𝐫 ⁡ [k mod n] = 𝐫 ⁡ [k ′ mod n] {\bf r}[k\bmod n]={\bf r}[k^{\prime}\bmod n]. Of course, for this to work we must ensure that 0 ≤ k, k ′ < 2 ​ n 0\leq k,k^{\prime}<2n holds.

The cases are described in Figure 24. We assume that that | x | = ℓ |x|=\ell and x ​ x ​ x R xxx^{R} begins at position i i of z ω z^{\omega}. We have the inequalities i < n i<n and ℓ < n \ell<n which apply to each case. Our predicates are designed to compare the first copy of x x to the second copy of x x, and the first copy of x x to the x R x^{R}.

[image: Refer to caption] Figure 24: Cases of the argument

Case 1: If x ​ x ​ x R xxx^{R} lies entirely within one copy of z z, it also lies in 𝐫 \bf r, which we have already seen cannot happen, in Theorem 37. This case therefore cannot occur.

Case 2: We use the predicate

 | ∃ i ​ ∃ ℓ ⁡ ( i + 3 ​ ℓ ≥ n) ∧ ( i + 3 ​ ℓ < 2 ​ n) ∧ ( ∀ j < ℓ ​ cmp ⁡ ( i + j, i + ℓ + j)) ∧ ( ∀ k < ℓ ​ cmp ⁡ ( i + k, i + 3 ​ ℓ − 1 − k)) \exists i\ \exists\ell\ (i+3\ell\geq n)\ \wedge\ (i+3\ell<2n)\ \wedge\ (\forall j<\ell\ \cmp(i+j,i+\ell+j))\ \wedge\ (\forall k<\ell\ \cmp(i+k,i+3\ell-1-k)) |  |

to assert that there is a repetition of the form x ​ x ​ x R xxx^{R}.

Case 3: We use the predicate

 | OPEN ∃ i ​ ∃ ℓ ⁡ ( i + 3 ​ ℓ ≥ 2 ​ n) ∧ ( i + 3 ​ ℓ < 3 ​ n) ∧ ( ∀ j < ℓ ​ cmp ⁡ ( i + j, i + ℓ + j − n)) ∧ ( ∀ k < ℓ ​ cmp ⁡ ( i + k, i + 3 ​ ℓ − 1 − k − n))). \exists i\ \exists\ell\ (i+3\ell\geq 2n)\ \wedge\ (i+3\ell<3n)\ \wedge\ (\forall j<\ell\ \cmp(i+j,i+\ell+j-n))\ \wedge\ (\forall k<\ell\ \cmp(i+k,i+3\ell-1-k-n))). |  |

Case 4: We use the predicate

 | ∃ i ​ ∃ ℓ ⁡ ( i + 3 ​ ℓ ≥ 3 ​ n) ∧ ( i + 3 ​ ℓ < 4 ​ n) ∧ ( ∀ j < ℓ ​ cmp ⁡ ( i + j, i + ℓ + j − n)) ∧ ( ∀ k < ℓ ​ cmp ⁡ ( i + k, i + 3 ​ ℓ − 1 − k − 2 ​ n)). \exists i\ \exists\ell\ (i+3\ell\geq 3n)\ \wedge\ (i+3\ell<4n)\ \wedge\ (\forall j<\ell\ \cmp(i+j,i+\ell+j-n))\ \wedge\ (\forall k<\ell\ \cmp(i+k,i+3\ell-1-k-2n)). |  |

When we checked each of the cases 2 through 4 with our program, we discovered that n = 2 ​ F 3 ​ k + 2 n=2F_{3k+2} is never accepted. Actually, for cases (2)–(4) we had to employ one additional trick, because the computation for the predicates as stated required more space than was available on our machine. Here is the additional trick: instead of attempting to run the predicate for all n n, we ran it only for n n whose Fibonacci representation was of the form 10010 ∗ 10010^{*}. This significantly restricted the size of the automata we created and allowed the computation to terminate. In fact, we propagated this condition throughout the predicate.

We therefore eliminated all possibilities for the occurrence of x ​ x ​ x R xxx^{R} in z ω z^{\omega} and so it follows that no x ​ x ​ x R xxx^{R} occurs in z ω z^{\omega}. ∎

###### Open Problem 49.

How many binary words of length n n avoid the pattern x ​ x ​ x R xxx^{R}? Is it polynomial in n n or exponential? How about the number of binary words of length n n avoiding x ​ x ​ x R xxx^{R} and simultaneously avoiding ( 2 + α) (2+\alpha) -powers?

Consider finite words of the form x ​ x ​ x R xxx^{R} having no proper factor of the form w ​ w ​ w R www^{R}.

###### Conjecture 50.

For n = F 3 ​ k + 1 n=F_{3k+1} there are 4 4 such words of length n n. For n = F 3 ​ k + 1 ± F 3 ​ k − 2 n=F_{3k+1}\pm F_{3k-2} there are 2 2 such words. Otherwise there are none.

For k ≥ 3 k\geq 3 the 4 4 words of length n = F 3 ​ k + 1 n=F_{3k+1} are given by 𝐫 [p i.. p i + n − 1] {\bf r}[p_{i}..p_{i}+n-1], i = 1, 2, 3, 4 i=1,2,3,4, where

 | ( p 1) F \displaystyle(p_{1})_{F} | = 1000 ​ ( 010) k − 3 ​ 001 \displaystyle=1000(010)^{k-3}001 |  |

 | ( p 2) F \displaystyle(p_{2})_{F} | = 10 ​ ( 010) k − 2 ​ 001 \displaystyle=10(010)^{k-2}001 |  |

 | ( p 3) F \displaystyle(p_{3})_{F} | = 1001000 ​ ( 010) k − 3 ​ 001 \displaystyle=1001000(010)^{k-3}001 |  |

 | ( p 4) F \displaystyle(p_{4})_{F} | = 1010 ​ ( 010) k − 2 ​ 001 \displaystyle=1010(010)^{k-2}001 |  |

For k ≥ 3 k\geq 3 the 2 2 words of length n = F 3 ​ k + 1 − F 3 ​ k − 2 n=F_{3k+1}-F_{3k-2} are given by 𝐫 [q i.. q i + n − 1] {\bf r}[q_{i}..q_{i}+n-1], i = 1, 2 i=1,2, where

 | ( q 1) F \displaystyle(q_{1})_{F} | = 10 ​ ( 010) k − 3 ​ 001 \displaystyle=10(010)^{k-3}001 |  |

 | ( q 2) F \displaystyle(q_{2})_{F} | = 10000 ​ ( 010) k − 3 ​ 001 \displaystyle=10000(010)^{k-3}001 |  |

For k ≥ 3 k\geq 3 the 2 2 words of length n = F 3 ​ k + 1 + F 3 ​ k − 2 n=F_{3k+1}+F_{3k-2} are given by 𝐫 [s i.. s i + n − 1] {\bf r}[s_{i}..s_{i}+n-1], i = 1, 2 i=1,2, where

 | ( s 1) F \displaystyle(s_{1})_{F} | = 10 ​ ( 010) k − 3 ​ 001 \displaystyle=10(010)^{k-3}001 |  |

 | ( s 2) F \displaystyle(s_{2})_{F} | = 1000 ​ ( 01) k − 2 ​ 001 \displaystyle=1000(01)^{k-2}001 |  |

## 6 Other sequences

In this section we briefly apply our method to some other Fibonacci-automatic sequences, obtaining several new results.

Consider a Fibonacci analogue of the Thue-Morse sequence

 | 𝐯 = ( v n) n ≥ 0 = 0111010010001100010111000101 ⋯ {\bf v}=(v_{n})_{n\geq 0}=0111010010001100010111000101\cdots |  |

where v n v_{n} is the sum of the bits, taken modulo 2 2, of the Fibonacci representation of n n. This sequence was introduced in [72, Example 2, pp. 12–13].

We recall that an overlap is a word of the form a ​ x ​ a ​ x ​ a axaxa where x x may be empty; its order is defined to be | a ​ x | |ax|. Similarly, a super-overlap is a word of the form a ​ b ​ x ​ a ​ b ​ x ​ a ​ b abxabxab; an example of a super-overlap in English is the word tingalingaling with the first letter removed.

###### Theorem 51.

The only squares in 𝐯 \bf v are of order 4 4 and F n F_{n} for n ≥ 2 n\geq 2, and a square of each such order occurs. The only cubes in 𝐯 \bf v are the strings 000 000 and 111 111. The only overlaps in 𝐯 \bf v are of order F 2 ​ n F_{2n} for n ≥ 1 n\geq 1, and an overlap of each such order occurs. There are no super-overlaps in 𝐯 \bf v.

###### Proof.

As before. We omit the details. ∎

We might also like to show that 𝐯 \bf v is recurrent. The obvious predicate for this property holding for all words of length n n is

 | ∀ i ​ ∃ j ⁡ ( ( j > i) ∧ ( ∀ t ⁡ ( ( t < n) ⟹ ( 𝐯 ⁡ [i + t] = 𝐯 ⁡ [j + t])))). \forall i\ \exists j\ ((j>i)\wedge(\forall t\ ((t<n)\implies({\bf v}[i+t]={\bf v}[j+t])))). |  |

Unfortunately, when we attempt to run this with our prover, we get an intermediate NFA of 1159 states that we cannot determinize within the available space.

Instead, we rewrite the predicate, setting k:= j − i k:=j-i and u:= i + t u:=i+t. This gives

 | ∀ i ​ ∃ j ⁡ ( j > i) ∧ ∀ k ​ ∀ u ⁡ ( ( k ≥ 1) ∧ ( i = j + k) ∧ ( u ≥ i) ∧ ( u < n + i)) ⟹ 𝐯 ⁡ [u] = 𝐯 ⁡ [u + k]. \forall i\ \exists j\ (j>i)\wedge\forall k\ \forall u\ ((k\geq 1)\wedge(i=j+k)\wedge(u\geq i)\wedge(u<n+i))\implies{\bf v}[u]={\bf v}[u+k]. |  |

When we run this we discover that 𝐯 \bf v is indeed recurrent. Here the computation takes a nontrivial 814007 ms, and the largest intermediate automaton has 625176 states. This proves

###### Theorem 52.

The word 𝐯 \bf v is recurrent.

Another quantity of interest for the Thue-Morse-Fibonacci word 𝐯 \bf v is its subword complexity ρ 𝐯 ​ ( n) \rho_{\bf v}(n). It is not hard to see that it is linear. To obtain a deeper understanding of it, let us compute the first difference sequence d ⁡ ( n) = ρ 𝐯 ​ ( n + 1) − ρ 𝐯 ​ ( n) d(n)=\rho_{\bf v}(n+1)-\rho_{\bf v}(n). It is easy to see that d ⁡ ( n) d(n) is the number of words w w of length n n with the property that both w ​ 0 w0 and w ​ 1 w1 appear in 𝐯 \bf v. The natural way to count this is to count those i i such that t:= 𝐯 [i.. i + n − 1] t:={\bf v}[i..i+n-1] is the first appearance of that factor in 𝐯 \bf v, and there exists a factor 𝐯 [k.. k + n] {\bf v}[k..k+n] of length n + 1 n+1 whose length- n n -prefix equals t t and whose last letter 𝐯 ⁡ [k + n] {\bf v}[k+n] differs from 𝐯 ⁡ [i + n] {\bf v}[i+n].

 | ( ∀ j < i ​ ∃ t < n ​ 𝐯 ​ [i + t] ≠ 𝐯 ⁡ [j + t]) ∧ ( ∃ k ⁡ ( ∀ u < n ​ 𝐯 ​ [i + u] = 𝐯 ⁡ [k + u]) ∧ 𝐯 ⁡ [i + n] ≠ 𝐯 ⁡ [k + n]). (\forall j<i\ \exists t<n\ {\bf v}[i+t]\not={\bf v}[j+t])\ \wedge\ (\exists k\ (\forall u<n\ {\bf v}[i+u]={\bf v}[k+u])\wedge{\bf v}[i+n]\not={\bf v}[k+n]). |  |

Unfortunately the same blowup appears as in the recurrence predicate, so once agin we need to substitute, resulting in the predicate

 | ( ∀ j < i ​ ∃ k ≥ 1 ​ ∃ v ⁡ ( i = j + k) ∧ ( v ≥ j) ∧ ( v < n + j) ∧ 𝐯 ⁡ [u] ≠ 𝐯 ⁡ [u + k]) ∧ ( ∃ l > i ​ 𝐯 ​ [i + n] ≠ 𝐯 ⁡ [l + n]) ∧ ( ∀ k ′ ​ ∀ u ′ ​ ( k ′ ≥ 1) ∧ ( l = i + k ′) ∧ ( u ′ ≥ i) ∧ ( v ′ < n + i) ⟹ 𝐯 ⁡ [k ′ + u ′] = 𝐯 ⁡ [u ′]). (\forall j<i\ \exists k\geq 1\ \exists v\ (i=j+k)\wedge(v\geq j)\wedge(v<n+j)\wedge{\bf v}[u]\not={\bf v}[u+k])\wedge\\ (\exists l>i\ {\bf v}[i+n]\not={\bf v}[l+n])\wedge\\ (\forall k^{\prime}\ \forall u^{\prime}\ (k^{\prime}\geq 1)\wedge(l=i+k^{\prime})\wedge(u^{\prime}\geq i)\wedge(v^{\prime}<n+i)\implies{\bf v}[k^{\prime}+u^{\prime}]={\bf v}[u^{\prime}]). |  |

From this we obtain a linear representation of rank 46 46. We can now consider all vectors of the form u ​ { M 0, M 1 } ∗ u\{M_{0},M_{1}\}^{*}. There are only finitely many and we can construct an automaton out of them computing d ⁡ ( n) d(n).

###### Theorem 53.

The first difference sequence ( d ⁡ ( n)) n ≥ 0 (d(n))_{n\geq 0} of the subword complexity of 𝐯 \bf v is Fibonacci-automatic, and is accepted by the following machine.

Figure 25: Automaton computing d ⁡ ( n) d(n)

## 7 Combining two representations and avoidability

In this section we show how our decidability method can be used to handle an avoidability question where two different representations arise.

Let x x be a finite word over the alphabet ℕ ∗ = { 1, 2, 3 ​ … } {\mathbb{N}}^{*}=\{1,2,3\ldots\}. We say that x x is an additive square if x = x 1 ​ x 2 x=x_{1}x_{2} with | x 1 | = | x n | |x_{1}|=|x_{n}| and ∑ x 1 = ∑ x 2 \sum x_{1}=\sum x_{2}. For example, with the usual association of 𝚊 = 1 {\tt a}=1, 𝚋 = 2 {\tt b}=2, and so forth, up to 𝚣 = 26 {\tt z}=26, we have that the English word baseball is an additive square, as base and ball both sum to 27 27.

An infinite word 𝐱 {\bf x} over ℕ ∗ {\mathbb{N}}^{*} is said to avoid additive squares if no factor is an additive square. It is currently unknown, and a relatively famous open problem, whether there exists an infinite word over a finite subset of ℕ ∗ {\mathbb{N}}^{*} that avoids additive squares [15, 61, 49].., although it is known that additive cubes can be avoided over an alphabet of size 4 4 [24]. (Recently this was improved to alphabet size 3 3; see [65].)

However, it is easy to avoid additive squares over an infinite subset of ℕ ∗ {\mathbb{N}}^{*}; for example, any sequence that grows sufficiently quickly will have the desired property. Hence it is reasonable to ask about the lexicographically least sequence over ℕ ∗ {\mathbb{N}}^{*} that avoids additive squares. Such a sequence begins

 | 1213121421252131213412172 ⋯, 1213121421252131213412172\cdots, |  |

but we do not even know if this sequence is unbounded.

Here we consider the following variation on this problem. Instead of considering arbitrary sequences, we start with a sequence 𝐛 = b 0 b 1 b 2 ⋯ {\bf b}=b_{0}b_{1}b_{2}\cdots over ℕ + {\mathbb{N}}^{+} and from it construct the sequence S ( 𝐛) = a 1 a 2 a 3 ⋯ S({\bf b})=a_{1}a_{2}a_{3}\cdots defined by

 | 𝐚 ⁡ [i] = 𝐛 ⁡ [ν 2 ​ ( i)] {\bf a}[i]={\bf b}[\nu_{2}(i)] |  |

for i ≥ 1 i\geq 1, where ν 2 ​ ( i) \nu_{2}(i) is the exponent of the largest power of 2 2 dividing i i. (Note that 𝐚 {\bf a} and 𝐛 {\bf b} are indexed differently.) For example, if 𝐛 = 123 ⋯ {\bf b}=123\cdots, then 𝐚 = 1213121412131215 ⋯ {\bf a}=1213121412131215\cdots, the so-called “ruler sequence”. It is known that this sequence is squarefree and is, in fact, the lexicographically least sequence over ℕ ∗ {\mathbb{N}}^{*} avoiding squares [48].

We then ask: what is the lexicographically least sequence avoiding additive squares that is of the form S ⁡ ( 𝐛) S({\bf b})? The following theorem gives the answer.

###### Theorem 54.

The lexicographically least sequence over ℕ ∖ { 0 } {\mathbb{N}}\setminus\{0\} of the form S ⁡ ( 𝐛) S({\bf b}) that avoids additive squares is defined by 𝐛 ⁡ [i]: = F i + 2 {\bf b}[i]\mathrel{\mathop{:}}=F_{i+2}.

###### Proof.

First, we show that 𝐚: = S ⁡ ( 𝐛) = ∏ k = 1 ∞ 𝐛 ⁡ [ν 2 ​ ( k)] = ∏ k = 1 ∞ F ν 2 ​ ( k) + 2 {\bf a}\mathrel{\mathop{:}}=S({\bf b})=\prod_{k=1}^{\infty}{\bf b}[\nu_{2}(k)]=\prod_{k=1}^{\infty}F_{\nu_{2}(k)+2} avoids additive squares.

For m, n, j ∈ ℕ m,n,j\in{\mathbb{N}}, let A ⁡ ( m, n, j) A(m,n,j) denote the number of occurrences of j j in ν 2 ​ ( m + 1), …, ν 2 ​ ( m + n) \nu_{2}(m+1),\dots,\nu_{2}(m+n).

(a): Consider two consecutive blocks of the same size say a i + 1 ⋯ a i + n a_{i+1}\cdots a_{i+n} and a i + n + 1 ⋯ a i + 2 ​ n a_{i+n+1}\cdots a_{i+2n}. Our goal is to compare the sums ∑ i < j ≤ i + n a j \sum_{i<j\leq i+n}a_{j} and ∑ i + n < j ≤ i + 2 ​ n a j \sum_{i+n<j\leq i+2n}a_{j}.

First we prove

###### Lemma 55.

Let m, j ≥ 0 m,j\geq 0 and n ≥ 1 n\geq 1 be integers. Let A ⁡ ( m, n, j) A(m,n,j) denote the number of occurrences of j j in ν 2 ​ ( m + 1), …, ν 2 ​ ( m + n) \nu_{2}(m+1),\ldots,\nu_{2}(m+n). Then for all m, m ′ ≥ 0 m,m^{\prime}\geq 0 we have | A ⁡ ( m ′, n, j) − A ⁡ ( m, n, j) | ≤ 1 |A(m^{\prime},n,j)-A(m,n,j)|\leq 1.

###### Proof.

We start by observing that the number of positive integers ≤ n \leq n that are divisible by t t is exactly ⌊ n / t ⌋ \lfloor n/t\rfloor. It follows that the number B ⁡ ( n, j) B(n,j) of positive integers ≤ n \leq n that are divisible by 2 j 2^{j} but not by 2 j + 1 2^{j+1} is

 | B ⁡ ( n, j) = ⌊ n 2 j ⌋ − ⌊ n 2 j + 1 ⌋. B(n,j)=\lfloor{n\over{2^{j}}}\rfloor-\lfloor{n\over{2^{j+1}}}\rfloor. |  | (1) |

Now from the well-known identity

 | ⌊ x ⌋ + ⌊ x + 1 2 ⌋ = ⌊ 2 ​ x ⌋, \lfloor x\rfloor+\lfloor x+{1\over 2}\rfloor=\lfloor 2x\rfloor, |  |

valid for all real numbers x x, substitute x = n / 2 j + 1 x=n/2^{j+1} to get

 | ⌊ n 2 j + 1 ⌋ + ⌊ n 2 j + 1 + 1 2 ⌋ = ⌊ n 2 j ⌋, \lfloor{n\over{2^{j+1}}}\rfloor+\lfloor{n\over{2^{j+1}}}+{1\over 2}\rfloor=\lfloor{n\over{2^{j}}}\rfloor, |  |

which, combined with ( 1), shows that

 | B ⁡ ( n, j) = ⌊ n 2 j + 1 + 1 2 ⌋. B(n,j)=\lfloor{n\over{2^{j+1}}}+{1\over 2}\rfloor. |  |

Hence

 | n 2 j + 1 − 1 2 ≤ B ⁡ ( n, j) < n 2 j + 1 + 1 2. {n\over{2^{j+1}}}-{1\over 2}\leq B(n,j)<{n\over{2^{j+1}}}+{1\over 2}. |  | (2) |

Now the number of occurrences of j j in ν 2 ​ ( m + 1), …, ν 2 ​ ( m + n) \nu_{2}(m+1),\ldots,\nu_{2}(m+n) is A ⁡ ( m, n, j) = B ⁡ ( m + n, j) − B ⁡ ( m, j) A(m,n,j)=B(m+n,j)-B(m,j). From ( 2) we get

 | n 2 j + 1 − 1 < A ⁡ ( m, n, j) < n 2 j + 1 + 1 {n\over{2^{j+1}}}-1<A(m,n,j)<{n\over{2^{j+1}}}+1 |  | (3) |

for all m ≥ 0 m\geq 0. Since A ⁡ ( m, n, j) A(m,n,j) is an integer, the inequality ( 3) implies that | A ⁡ ( m ′, n, j) − A ⁡ ( m, n, j) | ≤ 1 |A(m^{\prime},n,j)-A(m,n,j)|\leq 1 for all m, m ′ m,m^{\prime}. ∎

Note that for all i, n ∈ ℕ i,n\in{\mathbb{N}}, we have ∑ k = i i + n − 1 𝐚 ⁡ [k] = ∑ j = 0 ⌊ log 2 ⁡ ( i + n) ⌋ A ⁡ ( i, n, j) ​ F j + 2 \sum_{k=i}^{i+n-1}{\bf a}[k]=\sum_{j=0}^{\left\lfloor\log_{2}(i+n)\right\rfloor}A(i,n,j)F_{j+2}, so for adjacent blocks of length n n, ∑ k = i + n i + 2 ​ n − 1 𝐚 ⁡ [k] − ∑ k = i i + n − 1 𝐚 ⁡ [k] = ∑ j = 0 ⌊ log 2 ⁡ ( i + 2 ​ n) ⌋ ( A ⁡ ( i + n, n, j) − A ⁡ ( i, n, j)) ​ F j + 2 \sum_{k=i+n}^{i+2n-1}{\bf a}[k]-\sum_{k=i}^{i+n-1}{\bf a}[k]=\sum_{j=0}^{\left\lfloor\log_{2}(i+2n)\right\rfloor}(A(i+n,n,j)-A(i,n,j))F_{j+2}. Hence, 𝐚 [i.. i + 2 n − 1] {\bf a}[i\ldotp\ldotp i+2n-1] is an additive square iff ∑ j = 0 ⌊ log 2 ⁡ ( i + 2 ​ n) ⌋ ( A ⁡ ( i + n, n, j) − A ⁡ ( i, n, j)) ​ F j + 2 = 0 \sum_{j=0}^{\left\lfloor\log_{2}(i+2n)\right\rfloor}(A(i+n,n,j)-A(i,n,j))F_{j+2}=0, and by above, each A ⁡ ( i + n, n, j) − A ⁡ ( i, n, j) ∈ { − 1, 0, 1 } A(i+n,n,j)-A(i,n,j)\in\{-1,0,1\}.

The above suggests that we can take advantage of “unnormalized” Fibonacci representation in our computations. For Σ ⊆ ℤ \Sigma\subseteq{\mathbb{Z}} and w ∈ Σ ∗ w\in\Sigma^{*}, we let the unnormalized Fibonacci representation ⟨ w ⟩ u ​ F \left\langle w\right\rangle_{uF} be defined in the same way as ⟨ w ⟩ F \left\langle w\right\rangle_{F}, except over the alphabet Σ \Sigma.

In order to use Procedure 3, we need two auxiliary DFAs: one that, given i, n ∈ ℕ i,n\in{\mathbb{N}} (in any representation; we found that base 2 works), computes ⟨ A ⁡ ( i + n, n, _) − A ⁡ ( i, n, _) ⟩ u ​ F \left\langle A(i+n,n,\_)-A(i,n,\_)\right\rangle_{uF}, and another that, given w ∈ { − 𝟷, 𝟶, 𝟷 } ∗ w\in\{{\tt-1},{\tt 0},{\tt 1}\}^{*}, decides whether ⟨ w ⟩ u ​ F = 0 \left\langle w\right\rangle_{uF}=0. The first task can be done by a 6-state (incomplete) DFA M add22F M_{\text{add22F}} that accepts the language { z ∈ ( Σ 2 2 × { − 𝟷, 𝟶, 𝟷 }) ∗: ∀ j ⁡ ( π 3 ​ ( z) ​ [j] = A ⁡ ( ⟨ π 1 ​ ( z) ⟩ 2 + ⟨ π 2 ​ ( z) ⟩ 2, ⟨ π 2 ​ ( z) ⟩ 2, j) − A ⁡ ( ⟨ π 1 ​ ( z) ⟩ 2, ⟨ π 2 ​ ( z) ⟩ 2, j)) } \{z\in(\Sigma_{2}^{2}\times\{{\tt-1},{\tt 0},{\tt 1}\})^{*}\;:\;\forall j(\pi_{3}(z)[j]=A(\left\langle\pi_{1}(z)\right\rangle_{2}+\left\langle\pi_{2}(z)\right\rangle_{2},\left\langle\pi_{2}(z)\right\rangle_{2},j)-A(\left\langle\pi_{1}(z)\right\rangle_{2},\left\langle\pi_{2}(z)\right\rangle_{2},j))\}. The second task can be done by a 5-state (incomplete) DFA M 1uFisZero M_{\text{1uFisZero}} that accepts the language { w ∈ { − 𝟷, 𝟶, 𝟷 } ∗: ⟨ w ⟩ u ​ F = 0 } \{w\in\{{\tt-1},{\tt 0},{\tt 1}\}^{*}\;:\;\left\langle w\right\rangle_{uF}=0\}.

We applied a modified Procedure 3 to the predicate n ≥ 1 ​ and ​ ∃ w ⁡ ( 𝚊𝚍𝚍𝟸𝟸𝙵 ⁡ ( i, n, w) ​ and ​ 𝟷 ​ 𝚞 ​ 𝙵 ​ 𝚒 ​ 𝚜 ​ 𝚉 ​ 𝚎 ​ 𝚛 ​ 𝚘 ​ ( w)) n\geq 1\and\exists w({\tt add22F}(i,n,w)\and{\tt 1uFisZero}(w)) and obtained as output a DFA that accepts nothing, so 𝐚 {\bf a} avoids additive squares.

Next, we show that 𝐚 {\bf a} is the lexicographically least sequence over ℕ ∖ { 0 } {\mathbb{N}}\setminus\{0\} of the form S ⁡ ( 𝐛) S({\bf b}) that avoids additive squares.

Note that for all 𝐱, 𝐲 ∈ ℕ ∖ { 0 } {\bf x},{\bf y}\in{\mathbb{N}}\setminus\{0\}, S ⁡ ( 𝐱) < S ⁡ ( 𝐲) S({\bf x})<S({\bf y}) iff 𝐱 < 𝐲 {\bf x}<{\bf y} in the lexicographic ordering. Thus, we show that if any entry 𝐛 ⁡ [s] {\bf b}[s] with 𝐛 ⁡ [s] > 1 {\bf b}[s]>1 is changed to some t ∈ [1, 𝐛 ⁡ [s] − 1] t\in[1,{\bf b}[s]-1], then 𝐚 = S ⁡ ( 𝐛) {\bf a}=S({\bf b}) contains an additive square using only the first occurrence of the change at 𝐚 ⁡ [2 s − 1] {\bf a}[2^{s}-1]. More precisely, we show that for all s, t ∈ ℕ s,t\in{\mathbb{N}} with t ∈ [1, F s + 2 − 1] t\in[1,F_{s+2}-1], there exist i, n ∈ ℕ i,n\in{\mathbb{N}} with n ≥ 1 n\geq 1 and i + 2 ​ n < 2 s + 1 i+2n<2^{s+1} such that either ( 2 s − 1 ∈ [i, i + n − 1] 2^{s}-1\in[i,i+n-1] and ∑ k = i + n i + 2 ​ n − 1 𝐚 ⁡ [k] − ∑ k = i i + n − 1 𝐚 ⁡ [k] + t = 0 \sum_{k=i+n}^{i+2n-1}{\bf a}[k]-\sum_{k=i}^{i+n-1}{\bf a}[k]+t=0) or ( 2 s − 1 ∈ [i + n, i + 2 ​ n − 1] 2^{s}-1\in[i+n,i+2n-1] and ∑ k = i + n i + 2 ​ n − 1 𝐚 ⁡ [k] − ∑ k = i i + n − 1 𝐚 ⁡ [k] − t = 0 \sum_{k=i+n}^{i+2n-1}{\bf a}[k]-\sum_{k=i}^{i+n-1}{\bf a}[k]-t=0).

Setting up for a modified Procedure 3, we use the following predicate, which says “ r r is a power of 2 2 and changing 𝐚 ⁡ [r − 1] {\bf a}[r-1] to any smaller number results in an additive square in the first 2 ​ r 2r positions”, and six auxiliary DFAs. Note that all arithmetic and comparisons are in base 2.

 |  | 𝚙𝚘𝚠𝙾𝚏𝟸 ⁡ ( r) ​ and ​ ∀ t ⁡ ( ( t ≥ 1 ​ and ​ t < r ​ and ​ 𝚌𝚊𝚗𝚘𝚗𝙵𝚒𝚋 ​ ( t)) → ∃ i ​ ∃ n ⁡ ( n ≥ 1 ​ and ​ i + 2 ​ n < 2 ​ r ​ and CLOSE CLOSE \displaystyle{\tt powOf2}(r)\and\forall t((t\geq 1\and t<r\and{\tt canonFib}(t))\rightarrow\exists i\exists n(n\geq 1\and i+2n<2r\and{} |  |

 |  | ( ( i < r ​ and ​ r ≤ i + n ​ and ​ ∀ w ⁡ ( 𝚊𝚍𝚍𝟸𝟸𝙵 ⁡ ( i, n, w) → ∀ x ⁡ ( 𝚋𝚒𝚝𝙰𝚍𝚍 ⁡ ( t, w, x) → 𝟸 ​ 𝚞 ​ 𝙵 ​ 𝚒 ​ 𝚜 ​ 𝚉 ​ 𝚎 ​ 𝚛 ​ 𝚘 ​ ( x)))) ∨ CLOSE \displaystyle\quad((i<r\and r\leq i+n\and\forall w({\tt add22F}(i,n,w)\rightarrow\forall x({\tt bitAdd}(t,w,x)\rightarrow{\tt 2uFisZero}(x))))\vee{} |  |

 |  | ( i + n < r and r ≤ i + 2 n and ∀ w ( 𝚊𝚍𝚍𝟸𝟸𝙵 ( i, n, w) → ∀ x ( 𝚋𝚒𝚝𝚂𝚞𝚋 ( t, w, x) → 𝟸 𝚞 𝙵 𝚒 𝚜 𝚉 𝚎 𝚛 𝚘 ( x))))))). \displaystyle\quad\hphantom{(}(i+n<r\and r\leq i+2n\and\forall w({\tt add22F}(i,n,w)\rightarrow\forall x({\tt bitSub}(t,w,x)\rightarrow{\tt 2uFisZero}(x))))))). |  |

 | L ⁡ ( M powOf2) \displaystyle L(M_{\text{powOf2}}) | = { w ∈ Σ 2 ∗: ∃ n ⁡ ( w = ( 2 n) 2) }. \displaystyle=\{w\in\Sigma_{2}^{*}\;:\;\exists n(w=(2^{n})_{2})\}. |  |

 | L ⁡ ( M canonFib) \displaystyle L(M_{\text{canonFib}}) | = { w ∈ Σ 2 ∗: ∃ n ⁡ ( w = ( n) F) }. \displaystyle=\{w\in\Sigma_{2}^{*}\;:\;\exists n(w=(n)_{F})\}. |  |

 | L ⁡ ( M bit(Add/Sub)) \displaystyle L(M_{\text{bit(Add/Sub)}}) | = { z ∈ ( Σ 2 × { − 𝟷, 𝟶, 𝟷 } × { − 𝟷, 𝟶, 𝟷, 𝟸 }) ∗: ∀ i ⁡ ( π 1 ​ ( z) ​ [i] ± π 2 ​ ( z) ​ [i] = π 3 ​ ( z) ​ [i]) }. \displaystyle=\{z\in(\Sigma_{2}\times\{{\tt-1},{\tt 0},{\tt 1}\}\times\{{\tt-1},{\tt 0},{\tt 1},{\tt 2}\})^{*}\;:\;\forall i(\pi_{1}(z)[i]\pm\pi_{2}(z)[i]=\pi_{3}(z)[i])\}. |  |

 | L ⁡ ( M 2uFisZero) \displaystyle L(M_{\text{2uFisZero}}) | = { w ∈ { − 𝟷, 𝟶, 𝟷, 𝟸 } ∗: ⟨ w ⟩ u ​ F = 0 }. \displaystyle=\{w\in\{{\tt-1},{\tt 0},{\tt 1},{\tt 2}\}^{*}\;:\;\left\langle w\right\rangle_{uF}=0\}. |  |

We applied a modified Procedure 3 to the above predicate and auxiliary DFAs and obtained as output M powOf2 M_{\text{powOf2}}, so 𝐚 {\bf a} is the lexicographically least sequence over ℕ ∖ { 0 } {\mathbb{N}}\setminus\{0\} of the form S ⁡ ( 𝐛) S({\bf b}) that avoids additive squares. ∎

## 8 Enumeration

Mimicking the base- k k ideas in [25], we can also mechanically enumerate many aspects of Fibonacci-automatic sequences. We do this by encoding the factors having the property in terms of paths of an automaton. This gives the concept of Fibonacci-regular sequence as previously studied in [3]. Roughly speaking, a sequence ( a ⁡ ( n)) n ≥ 0 (a(n))_{n\geq 0} taking values in ℕ {\mathbb{N}} is Fibonacci-regular if the set of sequences

 | { ( a ( [x w] F) w ∈ Σ 2 ∗: x ∈ Σ 2 ∗ } \{(a([xw]_{F})_{w\in\Sigma_{2}^{*}}\ :\ x\in\Sigma_{2}^{*}\} |  |

is finitely generated. Here we assume that a ⁡ ( [x ​ w] F) a([xw]_{F}) evaluates to 0 0 if x ​ w xw contains the string 11 11. Every Fibonacci-regular sequence ( a ⁡ ( n)) n ≥ 0 (a(n))_{n\geq 0} has a linear representation of the form ( u, μ, v) (u,\mu,v) where u u and v v are row and column vectors, respectively, and μ: Σ 2 → ℕ d × d \mu:\Sigma_{2}\rightarrow{\mathbb{N}}^{d\times d} is a matrix-valued morphism, where μ ⁡ ( 0) = M 0 \mu(0)=M_{0} and μ ⁡ ( 1) = M 1 \mu(1)=M_{1} are d × d d\times d matrices for some d ≥ 1 d\geq 1, such that

 | a ⁡ ( n) = u ⋅ μ ⁡ ( x) ⋅ v a(n)=u\cdot\mu(x)\cdot v |  |

whenever [x] F = n [x]_{F}=n. The rank of the representation is the integer d d. As an example, we exhibit a rank- 6 6 linear representation for the sequence a ⁡ ( n) = n + 1 a(n)=n+1:

 | u \displaystyle u | = [1 2 2 3 3 2] \displaystyle=[1\ 2\ 2\ 3\ 3\ 2] |  |

 | M 0 \displaystyle M_{0} | = [1 1 0 0 0 0 0 0 0 0 0 0 0 1 0 1 1 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0] \displaystyle=\left[\begin{array}[]{cccccc}1&1&0&0&0&0\\ 0&0&0&0&0&0\\ 0&1&0&1&1&0\\ 0&0&1&1&1&1\\ 0&0&0&0&0&0\\ 0&0&0&0&0&0\end{array}\right] |  |

 | M 1 \displaystyle M_{1} | = [0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 1 0 0] \displaystyle=\left[\begin{array}[]{cccccc}0&0&0&0&0&0\\ 1&0&0&0&0&0\\ 0&0&0&0&0&0\\ 0&0&0&0&0&0\\ 0&0&1&1&0&0\\ 0&0&0&1&0&0\end{array}\right] |  |

 | v \displaystyle v | = [1 0 0 0 0 0] T. \displaystyle=[1\ 0\ 0\ 0\ 0\ 0]^{T}. |  |

This can be proved by a simple induction on the claim that

 | u ⋅ μ ⁡ ( x) = [x F + 1 ​ ( 1 ​ x) F + 1 ​ ( 10 ​ x) F − x F ​ ( 100 ​ x) F − x F ​ ( 101 ​ x) F − ( 1 ​ x) F ​ ( 1001 ​ x) F − ( 101 ​ x) F] u\cdot\mu(x)=[x_{F}+1\ (1x)_{F}+1\ (10x)_{F}-x_{F}\ (100x)_{F}-x_{F}\ (101x)_{F}-(1x)_{F}\ (1001x)_{F}-(101x)_{F}] |  |

for strings x x.

Recall that if 𝐱 \bf x is an infinite word, then the subword complexity function ρ 𝐱 ​ ( n) \rho_{\bf x}(n) counts the number of distinct factors of length n n. Then, in analogy with [25, Thm. 27], we have

###### Theorem 56.

If 𝐱 \bf x is Fibonacci-automatic, then the subword complexity function of 𝐱 \bf x is Fibonacci-regular.

Using our implementation, we can obtain a linear representation of the subword complexity function for 𝐟 \bf f. To do so, we use the predicate

 | { ( n, i) F: ∀ i ′ < i 𝐟 [i.. i + n − 1] ≠ 𝐟 [i ′.. i ′ + n − 1] }, \{(n,i)_{F}\ :\ \forall i^{\prime}<i\ {\bf f}[i..i+n-1]\not={\bf f}[i^{\prime}..i^{\prime}+n-1]\}, |  |

which expresses the assertion that the factor of length n n beginning at position i i has never appeared before. Then, for each n n, the number of corresponding i i gives ρ 𝐟 ​ ( n) \rho_{\bf f}(n). When we do this for 𝐟 \bf f, we get the following linear representation ( u ′, μ ′, v ′) (u^{\prime},\mu^{\prime},v^{\prime}) of rank 10 10:

 | u ′ \displaystyle u^{\prime} | = [0 0 0 1 0 0 0 0 0 0] \displaystyle=[0\ 0\ 0\ 1\ 0\ 0\ 0\ 0\ 0\ 0] |  |

 | M 0 ′ \displaystyle M^{\prime}_{0} | = [0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 1 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0] \displaystyle=\left[\begin{array}[]{ccccccccccc}0&1&1&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0\\ 1&0&0&0&0&0&0&0&0&0\\ 0&0&0&1&0&0&0&0&0&0\\ 1&0&0&0&0&1&0&0&0&0\\ 0&0&0&0&0&0&0&1&0&0\\ 0&0&0&0&0&1&0&1&0&0\\ 0&0&0&0&0&1&0&1&0&0\\ 1&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&1&0&0\end{array}\right] |  |

 | M 1 ′ \displaystyle M^{\prime}_{1} | = [0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0] \displaystyle=\left[\begin{array}[]{ccccccccccc}0&0&0&0&1&0&0&0&0&1\\ 0&0&0&0&0&0&0&0&1&0\\ 0&0&0&0&0&0&1&0&0&0\\ 0&0&0&0&0&0&1&0&1&0\\ 0&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&1&0&0&0\\ 0&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&1&0&0&1\\ 0&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0\end{array}\right] |  |

 | v ′ \displaystyle v^{\prime} | = [1 0 1 1 1 1 1 1 1 1] T \displaystyle=[1\ 0\ 1\ 1\ 1\ 1\ 1\ 1\ 1\ 1]^{T} |  |

To show that this computes the function n + 1 n+1, it suffices to compare the values of the linear representations ( u, μ, v) (u,\mu,v) and ( u ′, μ ′, v ′) (u^{\prime},\mu^{\prime},v^{\prime}) for all strings of length ≤ 10 + 6 = 16 \leq 10+6=16 (using [8, Corollary 3.6]). After checking this, we have reproved the following classic theorem of Morse and Hedlund [58]:

###### Theorem 57.

The subword complexity function of 𝐟 \bf f is n + 1 n+1.

We now turn to a result of Fraenkel and Simpson [39]. They computed the exact number of squares appearing in the finite Fibonacci words X n X_{n}; this was previously estimated by [29].

There are two variations: we could count the number of distinct squares in X n X_{n}, or what Fraenkel and Simpson called the number of “repeated squares” in X n X_{n} (i.e., the total number of occurrences of squares in X n X_{n}).

To solve this using our approach, we generalize the problem to consider any length- n n prefix of X n X_{n}, and not simply the prefixes of length F n F_{n}.

We can easily write down predicates for these. The first represents the number of distinct squares in 𝐟 [0.. n − 1] {\bf f}[0..n-1]:

 | L ds:= { ( n, i, j) F: ( j ≥ 1) and ( i + 2 j ≤ n) and 𝐟 [i.. i + j − 1] = 𝐟 [i + j.. i + 2 j − 1] and ∀ i ′ < i 𝐟 [i ′.. i ′ + 2 j − 1] ≠ 𝐟 [i.. i + 2 j − 1] }. L_{\rm ds}:=\{(n,i,j)_{F}\ :\ (j\geq 1)\text{ and }(i+2j\leq n)\text{ and }{\bf f}[i..i+j-1]={\bf f}[i+j..i+2j-1]\\ \text{ and }\forall i^{\prime}<i\ {\bf f}[i^{\prime}..i^{\prime}+2j-1]\not={\bf f}[i..i+2j-1]\}. |  |

This predicate asserts that 𝐟 [i.. i + 2 j − 1] {\bf f}[i..i+2j-1] is a square occurring in 𝐟 [0.. n − 1] {\bf f}[0..n-1] and that furthermore it is the first occurrence of this particular string in 𝐟 [0.. n − 1] {\bf f}[0..n-1].

The second represents the total number of occurrences of squares in 𝐟 [0.. n − 1] {\bf f}[0..n-1]:

 | L dos:= { ( n, i, j) F: ( j ≥ 1) and ( i + 2 j ≤ n) and 𝐟 [i.. i + j − 1] = 𝐟 [i + j.. i + 2 j − 1] }. L_{\rm dos}:=\{(n,i,j)_{F}\ :\ (j\geq 1)\text{ and }(i+2j\leq n)\text{ and }{\bf f}[i..i+j-1]={\bf f}[i+j..i+2j-1]\}. |  |

This predicate asserts that 𝐟 [i.. i + 2 j − 1] {\bf f}[i..i+2j-1] is a square occurring in 𝐟 [0.. n − 1] {\bf f}[0..n-1].

We apply our method to the second example, leaving the first to the reader. Let b ⁡ ( n) b(n) denote the number of occurrences of squares in 𝐟 [0.. n − 1] {\bf f}[0..n-1]. First, we use our method to find a DFA M M accepting L dos L_{\rm dos}. This (incomplete) DFA has 27 states.

Next, we compute matrices M 0 M_{0} and M 1 M_{1}, indexed by states of M M, such that ( M a) k, l (M_{a})_{k,l} counts the number of edges (corresponding to the variables i i and j j) from state k k to state l l on the digit a a of n n. We also compute a vector u u corresponding to the initial state of M M and a vector v v corresponding to the final states of M M. This gives us the following linear representation of the sequence b ⁡ ( n) b(n): if x = a 1 a 2 ⋯ a t x=a_{1}a_{2}\cdots a_{t} is the Fibonacci representation of n n, then

 | b ( n) = u M a 1 ⋯ M a t v, b(n)=uM_{a_{1}}\cdots M_{a_{t}}v, |  | (4) |

which, incidentally, gives a fast algorithm for computing b ⁡ ( n) b(n) for any n n.

Now let B ⁡ ( n) B(n) denote the number of square occurrences in the finite Fibonacci word X n X_{n}. This corresponds to considering the Fibonacci representation of the form 10 n − 2 10^{n-2}; that is, B ⁡ ( n + 1) = b ⁡ ( [10 n − 1] F) B(n+1)=b([10^{n-1}]_{F}). The matrix M 0 M_{0} is the following 27 × 27 27\times 27 array

 | [1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0] \left[\begin{array}[]{ccccccccccccccccccccccccccc}1&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0\\ 1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0\\ 1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1\\ 1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&1&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0\\ 0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0\\ 1&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0\\ 1&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&1&0&0&1&0\\ 0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&1&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0\\ 1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&1&0&0&1&0\\ 0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1\\ 0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&0&1&1&0&0&0&0&0&0\end{array}\right] |  | (5) |

and has minimal polynomial

 | X 4 ​ ( X − 1) 2 ​ ( X + 1) 2 ​ ( X 2 − X − 1) 2. X^{4}(X-1)^{2}(X+1)^{2}(X^{2}-X-1)^{2}. |  |

It now follows from the theory of linear recurrences that there are constants c 1, c 2, …, c 8 c_{1},c_{2},\ldots,c_{8} such that

 | B ⁡ ( n + 1) = ( c 1 ​ n + c 2) ​ α n + ( c 3 ​ n + c 4) ​ β n + c 5 ​ n + c 6 + ( c 7 ​ n + c 8) ​ ( − 1) n B(n+1)=(c_{1}n+c_{2})\alpha^{n}+(c_{3}n+c_{4})\beta^{n}+c_{5}n+c_{6}+(c_{7}n+c_{8})(-1)^{n} |  |

for n ≥ 3 n\geq 3, where α = ( 1 + 5) / 2 \alpha=(1+\sqrt{5})/2, β = ( 1 − 5) / 2 \beta=(1-\sqrt{5})/2 are the roots of X 2 − X − 1 X^{2}-X-1. We can find these constants by computing B ⁡ ( 4), B ⁡ ( 5), …, B ⁡ ( 11) B(4),B(5),\ldots,B(11) (using Eq. ( 4)) and then solving for the values of the constants c 1, …, c 8 c_{1},\ldots,c_{8}.

When we do so, we find

 | c 1 \displaystyle c_{1} | = 2 5 \displaystyle={2\over 5}\quad\quad | c 2 \displaystyle c_{2} | = − 2 25 ​ 5 − 2 \displaystyle={-{2\over{25}}}\sqrt{5}-2 |  |

 | c 3 \displaystyle c_{3} | = 2 5 \displaystyle={2\over 5}\quad\quad | c 4 \displaystyle c_{4} | = 2 25 ​ 5 − 2 \displaystyle={{2\over{25}}}\sqrt{5}-2 |  |

 | c 5 \displaystyle c_{5} | = 1 \displaystyle=1\quad\quad | c 6 \displaystyle c_{6} | = 1 \displaystyle=1 |  |

 | c 7 \displaystyle c_{7} | = 0 \displaystyle=0\quad\quad | c 8 \displaystyle c_{8} | = 0 \displaystyle=0 |  |

A little simplification, using the fact that F n = ( α n − β n) / ( α − β) F_{n}=(\alpha^{n}-\beta^{n})/(\alpha-\beta), leads to

###### Theorem 58.

Let B ⁡ ( n) B(n) denote the number of square occurrences in X n X_{n}. Then

 | B ⁡ ( n + 1) = 4 5 ​ n ​ F n + 1 − 2 5 ​ ( n + 6) ​ F n − 4 ​ F n − 1 + n + 1 B(n+1)={4\over 5}nF_{n+1}-{2\over 5}(n+6)F_{n}-4F_{n-1}+n+1 |  |

for n ≥ 3 n\geq 3.

This statement corrects a small error in Theorem 2 in [39] (the coefficient of F n − 1 F_{n-1} was wrong; note that their F F and their Fibonacci words are indexed differently from ours), which was first pointed out to us by Kalle Saari.

In a similar way, we can count the cube occurrences in X n X_{n}. Using analysis exactly like the square case, we easily find

###### Theorem 59.

Let C ⁡ ( n) C(n) denote the number of cube occurrences in the Fibonacci word X n X_{n}. Then for n ≥ 3 n\geq 3 we have

 | C ⁡ ( n) = ( d 1 ​ n + d 2) ​ α n + ( d 3 ​ n + d 4) ​ β n + d 5 ​ n + d 6 C(n)=(d_{1}n+d_{2})\alpha^{n}+(d_{3}n+d_{4})\beta^{n}+d_{5}n+d_{6} |  |

where

 | d 1 \displaystyle d_{1} | = 3 − 5 10 \displaystyle={{3-\sqrt{5}}\over{10}}\quad\quad | d 2 \displaystyle d_{2} | = 17 50 ​ 5 − 3 2 \displaystyle={{17}\over{50}}\sqrt{5}-{3\over 2} |  |

 | d 3 \displaystyle d_{3} | = 3 + 5 10 \displaystyle={{3+\sqrt{5}}\over{10}}\quad\quad | d 4 \displaystyle d_{4} | = − 17 50 ​ 5 − 3 2 \displaystyle=-{{17}\over{50}}\sqrt{5}-{3\over 2} |  |

 | d 5 \displaystyle d_{5} | = 1 \displaystyle=1\quad\quad | d 6 \displaystyle d_{6} | = − 1. \displaystyle=-1. |  |

We now turn to a question of Chuan and Droubay. Let us consider the prefixes of 𝐟 \bf f. For each prefix of length n n, form all of its n n shifts, and let us count the number of these shifts that are palindromes; call this number d ⁡ ( n) d(n). (Note that in the case where a prefix is a power, two different shifts could be identical; we count these with multiplicity.)

Chuan [27, Thm. 7, p. 254] proved

###### Theorem 60.

For i > 2 i>2 we have d ⁡ ( F i) = 0 d(F_{i})=0 iff i ≡ 0 ​ ( mod ​ 3) i\equiv 0\ ({\rm mod}\ 3).

###### Proof.

Along the way we actually prove a lot more, characterizing d ⁡ ( n) d(n) for all n n, not just those n n equal to a Fibonacci number.

We start by showing that d ⁡ ( n) d(n) takes only three values: 0 0, 1 1, and 2 2. To do this, we construct an automaton accepting the language

 | { ( n, i) F: ( 0 ≤ i < n) ∧ 𝐟 [i.. n − 1] 𝐟 [0.. i − 1] is a palindrome }. \{(n,i)_{F}\ :\ (0\leq i<n)\ \wedge\ {\bf f}[i..n-1]{\bf f}[0..i-1]\text{ is a palindrome }\}. |  |

From this we construct the linear representation ( u, M 0, M 1, v) (u,M_{0},M_{1},v) of d ⁡ ( n) d(n) as discussed above; it has rank 27 27.

The range of c c is finite if the monoid ℳ = ⟨ M 0, M 1 ⟩ {\cal M}=\langle M_{0},M_{1}\rangle is finite. This can be checked with a simple queue-based algorithm, and ℳ \cal M turns out to have cardinality 151 151. From these a simple computation proves

 | { u ​ M ​ v: M ∈ ℳ } = { 0, 1, 2 }, \{uMv\ :\ M\in{\cal M}\}=\{0,1,2\}, |  |

and so our claim about the range of c c follows.

Now that we know the range of c c we can create predicates P 0 ​ ( n), P 1 ​ ( n), P 2 ​ ( n) P_{0}(n),P_{1}(n),P_{2}(n) asserting that (a) there are no length- n n shifts that are palindromes (b) there is exactly one shift that is a palindrome and (c) more than one shift is a palindrome, as follows:

 | P 0: ¬ ∃ i, ( 0 ≤ i < n), 𝐟 [i.. n − 1] 𝐟 [0.. i − 1] is a palindrome P_{0}:\neg\exists i,(0\leq i<n),{\bf f}[i..n-1]{\bf f}[0..i-1]\text{ is a palindrome } |  |

 | P 1: ∃ i, ( 0 ≤ i < n), 𝐟 [i.. n − 1] 𝐟 [0.. i − 1] is a palindrome and ¬ ∃ j ≠ i ( 0 ≤ j < n), 𝐟 [j.. n − 1] 𝐟 [0.. j − 1] P_{1}:\exists i,(0\leq i<n),{\bf f}[i..n-1]{\bf f}[0..i-1]\text{ is a palindrome and }\neg\exists j\not=i(0\leq j<n),{\bf f}[j..n-1]{\bf f}[0..j-1] |  |

 | P 2: ∃ i, j, 0 ≤ i < j < n 𝐟 [i.. n − 1] 𝐟 [0.. i − 1] and 𝐟 [j.. n − 1] 𝐟 [0.. j − 1] are both palindromes P_{2}:\exists i,j,0\leq i<j<n{\bf f}[i..n-1]{\bf f}[0..i-1]\text{ and }{\bf f}[j..n-1]{\bf f}[0..j-1]\text{ are both palindromes } |  |

For each one, we can compute a finite automaton characterizing the Fibonacci representations of those n n for which d ⁡ ( n) d(n) equals, respectively, 0 0, 1 1, and 2 2.

For example, we computed the automaton corresponding to P 0 P_{0}, and it is displayed in Figure 26 below.

Figure 26: Automaton accepting lengths of prefixes for which no shifts are palindromes

By tracing the path labeled 10 ∗ 10^{*} starting at the initial state labeled 18 18, we see that the “finality” of the states encountered is ultimately periodic with period 3 3, proving Theorem 60. ∎

To finish this section, we reprove a result of Kolpakov and Kucherov [54]. Recalling the definition of maximal repetition from Section 3.1, they counted the number mr ⁡ ( F n) \mr(F_{n}) of occurrences of maximal repetitions in the prefix of 𝐟 \bf f of length F n F_{n}:

###### Theorem 61.

For n ≥ 5 n\geq 5 we have mr ⁡ ( F n) = 2 ​ F n − 2 − 3 \mr(F_{n})=2F_{n-2}-3.

###### Proof.

We create an automaton for the language

 | { ( n, i, j) F: 0 ≤ i ≤ j < n and 𝐟 [i.. j] is a maximal repetition of 𝐟 [0.. n − 1] }, \{(n,i,j)_{F}\ :\ 0\leq i\leq j<n\text{ and }{\bf f}[i..j]\text{ is a maximal repetition of }{\bf f}[0..n-1]\}, |  |

using the predicate

 | ( i ≤ j) ∧ ( j < n) ∧ ∃ p ​ with ​ 1 ≤ p ≤ ( j + 1 − i) / 2 ​ such that ( ( ∀ k ≤ j − i − p ​ 𝐟 ​ [i + k] = 𝐟 ⁡ [i + k + p]) ∧ CLOSE ( i ≥ 1) ⟹ ( ∀ q ​ with ​ 1 ≤ q ≤ p ​ ∃ ℓ ≤ j − i − q + 1 ​ 𝐟 ​ [i − i + ℓ] ≠ 𝐟 ⁡ [i − 1 + ℓ + q]) ∧ OPEN ( j + 1 ≤ n − 1) ⟹ ( ∀ r ​ with ​ 1 ≤ r ≤ p ​ ∃ m ≤ j + 1 − r − i ​ 𝐟 ​ [i + m] ≠ 𝐟 ⁡ [i + m + r])). (i\leq j)\ \wedge\ (j<n)\ \wedge\ \exists p\text{ with }1\leq p\leq(j+1-i)/2\text{ such that }\\ ((\forall k\leq j-i-p\ {\bf f}[i+k]={\bf f}[i+k+p])\ \wedge\ \\ (i\geq 1)\implies(\forall q\text{ with }1\leq q\leq p\ \exists\ell\leq j-i-q+1\ {\bf f}[i-i+\ell]\not={\bf f}[i-1+\ell+q])\ \wedge\ \\ (j+1\leq n-1)\implies(\forall r\text{ with }1\leq r\leq p\ \exists m\leq j+1-r-i\ {\bf f}[i+m]\not={\bf f}[i+m+r])). |  |

Here the second line of the predicate specifies that there is a period p p of 𝐟 [i.. j] {\bf f}[i..j] corresponding to a repetition of exponent at least 2 2. The third line specifies that no period q q of 𝐟 [i − 1.. j] {\bf f}[i-1..j] (when this makes sense) can be ≤ p \leq p, and the fourth line specifies that no period r r of 𝐟 [i.. j + 1] {\bf f}[i..j+1] (when j + 1 ≤ n − 1 j+1\leq n-1) can be ≤ p \leq p.

From the automaton we deduce a linear representation ( u, μ, v) (u,\mu,v) of rank 59. Since ( F n) F = 10 n − 2 (F_{n})_{F}=10^{n-2}, it suffices to compute the minimal polynomial of M 0 = μ ⁡ ( 0) M_{0}=\mu(0). When we do this, we discover it is X 4 ​ ( X 2 − X − 1) ​ ( X − 1) 2 ​ ( X + 1) 2 X^{4}(X^{2}-X-1)(X-1)^{2}(X+1)^{2}. It follows from the theory of linear recurrences that

 | mr ⁡ ( F n) = e 1 ​ α n + e 2 ​ β n + e 3 ​ n + e 4 + ( e 5 ​ n + e 6) ​ ( − 1) n \mr(F_{n})=e_{1}\alpha^{n}+e_{2}\beta^{n}+e_{3}n+e_{4}+(e_{5}n+e_{6})(-1)^{n} |  |

for constants e 1, e 2, e 3, e 4, e 5, e 6 e_{1},e_{2},e_{3},e_{4},e_{5},e_{6} and n ≥ 6 n\geq 6. When we solve for e 1, …, e 6 e_{1},\ldots,e_{6} by using the first few values of mr ⁡ ( F n) \mr(F_{n}) (computed from the linear representation or directly) we discover that e 1 = ( 3 ​ 5 − 5) / 5 e_{1}=(3\sqrt{5}-5)/5, e 2 = ( − 3 ​ 5 − 5) / 5 e_{2}=(-3\sqrt{5}-5)/5, e 3 = e 5 = e 6 = 0 e_{3}=e_{5}=e_{6}=0, and e 4 = − 3 e_{4}=-3. From this the result immediately follows. ∎

In fact, we can prove even more.

###### Theorem 62.

For n ≥ 0 n\geq 0 the difference mr ⁡ ( n + 1) − mr ⁡ ( n) \mr(n+1)-\mr(n) is either 0 0 or 1 1. Furthermore there is a finite automaton with 10 states that accepts ( n) F (n)_{F} precisely when mr ⁡ ( n + 1) − mr ⁡ ( n) = 1 \mr(n+1)-\mr(n)=1.

###### Proof.

Every maximal repetition 𝐟 [i.. j] {\bf f}[i..j] of 𝐟 [0.. n − 1] {\bf f}[0..n-1] is either a maximal repetition of 𝐟 [0.. n] {\bf f}[0..n] with j ≤ n − 1 j\leq n-1, or is a maximal repetition with j = n − 1 j=n-1 that, when considered in 𝐟 [0.. n] {\bf f}[0..n], can be extended one character to the right to become one with j = n j=n. So the only maximal repetitions of 𝐟 [0.. n] {\bf f}[0..n] not (essentially) counted by mr ⁡ ( n) \mr(n) are those such that

 | 𝐟 [i.. n] is a maximal repetition of 𝐟 [0.. n] and 𝐟 [i.. n − 1] is not a maximal repetition of 𝐟 [0.. n − 1]. {\bf f}[i..n]\text{ is a maximal repetition of }{\bf f}[0..n]\text{ and }\\ {\bf f}[i..n-1]\text{ is {\it not\/} a maximal repetition of }{\bf f}[0..n-1]. |  | (6) |

We can easily create a predicate asserting this latter condition, and from this obtain the linear representation of mr ⁡ ( n + 1) − mr ⁡ ( n) \mr(n+1)-\mr(n):

 | u \displaystyle u | = [0 0 0 0 0 1 0 0 0 0 0 0] \displaystyle=[0\ 0\ 0\ 0\ 0\ 1\ 0\ 0\ 0\ 0\ 0\ 0\ ] |  |

 | μ ⁡ ( 0) \displaystyle\mu(0) | = [0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0] \displaystyle=\left[\begin{array}[]{cccccccccccc}0&0&0&0&0&0&0&0&0&1&0&0\\ 0&0&0&0&0&0&0&0&0&0&1&0\\ 0&0&0&1&0&0&0&0&0&1&0&0\\ 0&0&0&0&0&0&0&1&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&1&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&1&0\\ 0&0&0&0&1&0&0&0&0&0&0&0\\ 0&0&0&0&1&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&1\\ 0&0&0&0&0&0&1&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&1&0&0\end{array}\right] |  |

 | μ ⁡ ( 1) \displaystyle\mu(1) | = [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0] \displaystyle=\left[\begin{array}[]{cccccccccccc}0&0&0&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&1&0&0&0\\ 0&1&1&0&0&0&0&0&0&0&0&0\\ 1&1&0&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&0&0&0&0\\ 0&1&1&0&0&0&0&0&0&0&0&0\\ 0&0&0&0&0&0&0&0&1&0&0&0\end{array}\right] |  |

 | v \displaystyle v | = [0 0 0 0 1 0 0 0 1 0 0 1] \displaystyle=[0\ 0\ 0\ 0\ 1\ 0\ 0\ 0\ 1\ 0\ 0\ 1] |  |

We now use the trick we previously used for the proof of Theorem 60; the monoid generated by μ ⁡ ( 0) \mu(0) and μ ⁡ ( 1) \mu(1) has size 61 61 and for each matrix M M in this monoid we have u ​ M ​ v ∈ { 0, 1 } uMv\in\{0,1\}. It follows that mr ⁡ ( n + 1) − mr ⁡ ( n) ∈ { 0, 1 } \mr(n+1)-\mr(n)\in\{0,1\} for all n ≥ 0 n\geq 0.

Knowing this, we can now build an automaton accepting those n n for which there exists an i i for which ( 6) holds. When we do so we get the automaton depicted below in Figure 27.

Figure 27: Automaton accepting ( n) F (n)_{F} such that mr ⁡ ( n + 1) − mr ⁡ ( n) = 1 \mr(n+1)-\mr(n)=1

∎

## 9 Abelian properties

Our decision procedure does not apply, in complete generality, to abelian properties of infinite words. This is because there is no obvious way to express assertions like ψ ⁡ ( x) = ψ ⁡ ( x ′) \psi(x)=\psi(x^{\prime}) for two factors x, x ′ x,x^{\prime} of an infinite word. (Here ψ: Σ ∗ → ℕ | Σ | \psi:\Sigma^{*}\rightarrow{\mathbb{N}}^{|\Sigma|} is the Parikh map that sends a word to the number of occurrences of each letter.) Indeed, in the 2 2 -automatic case it is provable that there is at least one abelian property that is inexpressible [69, §5.2].

However, the special nature of the Fibonacci word 𝐟 \bf f allows us to mechanically prove some assertions involving abelian properties. In this section we describe how we did this.

By an abelian square of order n n we mean a factor of the form x ​ x ′ xx^{\prime} where ψ ⁡ ( x) = ψ ⁡ ( x ′) \psi(x)=\psi(x^{\prime}), where n = | x | n=|x|. In a similar way we can define abelian cubes and higher powers.

We start with the elementary observation that 𝐟 \bf f is defined over the alphabet { 0, 1 } \{0,1\}. Hence, to understand the abelian properties of a factor x x it suffices to know | x | |x| and | x | 0 |x|_{0}. Next, we observe that the map that sends n n to a n:= | 𝐟 [0.. n − 1] | 0 a_{n}:=|{\bf f}[0..n-1]|_{0} (that is, the number of 0 0 ’s in the length- n n prefix of 𝐟 \bf f), is actually synchronized (see [22, 20, 21, 47]). That is, there is a DFA accepting the Fibonacci representation of the pairs ( n, a n) (n,a_{n}). In fact we have the following

###### Theorem 63.

Suppose the Fibonacci representation of n n is e 1 e 2 ⋯ e i e_{1}e_{2}\cdots e_{i}. Then a n = [e 1 e 2 ⋯ e i − 1] F + e i a_{n}=[e_{1}e_{2}\cdots e_{i-1}]_{F}+e_{i}.

###### Proof.

First, we observe that an easy induction on m m proves that | X m | 0 = F m − 1 |X_{m}|_{0}=F_{m-1} for m ≥ 2 m\geq 2. We will use this in a moment.

The theorem’s claim is easily checked for n = 0, 1 n=0,1. We prove it for F m + 1 ≤ n < F m + 2 F_{m+1}\leq n<F_{m+2} by induction on m m. The base case is m = 1 m=1, which corresponds to n = 1 n=1.

Now assume the theorem’s claim is true for m − 1 m-1; we prove it for m m. Write ( n) F = e 1 e 2 ⋯ e m (n)_{F}=e_{1}e_{2}\cdots e_{m}. Then, using the fact that 𝐟 [0.. F m + 2 − 1] = X m + 2 = X m + 1 X m {\bf f}[0..F_{m+2}-1]=X_{m+2}=X_{m+1}X_{m}, we get

 | | 𝐟 [0.. n − 1] | 0 \displaystyle|{\bf f}[0..n-1]|_{0} | = | 𝐟 [0.. F m + 1 − 1] | 0 + | 𝐟 [F m + 1.. n − 1] | 0 \displaystyle=|{\bf f}[0..F_{m+1}-1]|_{0}+|{\bf f}[F_{m+1}..n-1]|_{0} |  |

 |  | = | X m + 1 | 0 + | 𝐟 [0.. n − 1 − F m + 1] | 0 \displaystyle=|X_{m+1}|_{0}+|{\bf f}[0..n-1-F_{m+1}]|_{0} |  |

 |  | = F m + | 𝐟 [0.. n − 1 − F m + 1 | 0 \displaystyle=F_{m}+|{\bf f}[0..n-1-F_{m+1}|_{0} |  |

 |  | = F m + [e 2 ⋯ e m − 1] F + e m \displaystyle=F_{m}+[e_{2}\cdots e_{m-1}]_{F}+e_{m} |  |

 |  | = [e 1 ⋯ e m − 1] F + e m, \displaystyle=[e_{1}\cdots e_{m-1}]_{F}+e_{m}, |  |

as desired. ∎

In fact, the synchronized automaton for ( n, a n) F (n,a_{n})_{F} is given in the following diagram:

Figure 28: Automaton accepting ( n, a n) F (n,a_{n})_{F}

Here the missing state numbered 2 2 is a “dead” state that is the target of all undrawn transitions.

The correctness of this automaton can be checked using our prover. Letting ZC ⁡ ( x, y) \zc(x,y) denote 1 1 if ( x, y) F (x,y)_{F} is accepted, it suffices to check that

1. 1.

∀ x ​ ∃ y ​ ZC ⁡ ( x, y) = 1 \forall x\ \exists y\ \zc(x,y)=1 (that is, for each x x there is at least one corresponding y y accepted);

2. 2.

∀ x ​ ∀ y ​ ∀ z ⁡ ( ZC ⁡ ( x, y) = ZC ⁡ ( x, z)) ⟹ y = z \forall x\ \forall y\ \forall z\ (\zc(x,y)=\zc(x,z))\implies y=z (that is, for each x x at most one corresponding y y is accepted);

3. 3.

∀ x ​ ∀ y ⁡ ( ( ZC ⁡ ( x, y) = 1) ∧ ( 𝐟 ⁡ [x] = 1)) ⟹ ( ZC ⁡ ( x + 1, y + 1) = 1) \forall x\ \forall y\ ((\zc(x,y)=1)\ \wedge\ ({\bf f}[x]=1))\implies(\zc(x+1,y+1)=1);

4. 4.

∀ x ​ ∀ y ⁡ ( ( ZC ⁡ ( x, y) = 1) ∧ ( 𝐟 ⁡ [x] = 0)) ⟹ ( ZC ⁡ ( x + 1, y) = 1) \forall x\ \forall y\ ((\zc(x,y)=1)\ \wedge\ ({\bf f}[x]=0))\implies(\zc(x+1,y)=1);

Another useful automaton computes, on input n, i, j n,i,j the function

 | FAB ( n, i, j):= | 𝐟 [i.. i + n − 1] | 0 − | 𝐟 [j.. j + n − 1] | 0 = a i + n − a i − a j + n + a j. \fab(n,i,j):=|{\bf f}[i..i+n-1]|_{0}-|{\bf f}[j..j+n-1]|_{0}=a_{i+n}-a_{i}-a_{j+n}+a_{j}. |  |

From the known fact that the factors of 𝐟 \bf f are “balanced” we know that FAB \fab takes only the values − 1, 0, 1 -1,0,1. This automaton can be deduced from the one above. However, we calculated it by “guessing” the right automaton and then verifying the correctness with our prover.

The automaton for FAB ⁡ ( n, i, j) \fab(n,i,j) has 30 states, numbered from 1 1 to 30 30. Inputs are in Σ 2 3 \Sigma_{2}^{3}. The transitions, as well as the outputs, are given in the table below.

q q | [0, 0, 0] [0,0,0] | [0, 0, 1] [0,0,1] | [0, 1, 0] [0,1,0] | [0, 1, 1] [0,1,1] | [1, 0, 0] [1,0,0] | [1, 0, 1] [1,0,1] | [1, 1, 0] [1,1,0] | [1, 1, 1] [1,1,1] | τ ⁡ ( q) \tau(q) |

1 | 1 | 2 | 3 | 4 | 4 | 5 | 6 | 7 | 0 |

2 | 8 | 1 | 9 | 3 | 3 | 4 | 10 | 6 | 0 |

3 | 11 | 12 | 1 | 2 | 2 | 13 | 4 | 5 | 0 |

4 | 14 | 11 | 8 | 1 | 1 | 2 | 3 | 4 | 0 |

5 | 15 | 11 | 16 | 1 | 1 | 2 | 3 | 4 | 1 |

6 | 17 | 18 | 8 | 1 | 1 | 2 | 3 | 4 | − 1 -1 |

7 | 19 | 18 | 16 | 1 | 1 | 2 | 3 | 4 | 0 |

8 | 1 | 2 | 3 | 4 | 4 | 20 | 6 | 21 | 0 |

9 | 11 | 12 | 1 | 2 | 2 | 22 | 4 | 20 | 0 |

10 | 18 | 23 | 1 | 2 | 2 | 13 | 4 | 5 | − 1 -1 |

11 | 1 | 2 | 3 | 4 | 4 | 5 | 24 | 25 | 0 |

12 | 8 | 1 | 9 | 3 | 3 | 4 | 26 | 24 | 0 |

13 | 16 | 1 | 27 | 3 | 3 | 4 | 10 | 6 | 1 |

14 | 1 | 2 | 3 | 4 | 4 | 20 | 24 | 28 | 0 |

15 | 2 | 13 | 4 | 5 | 5 | 20 | 25 | 28 | − 1 -1 |

16 | 2 | 13 | 4 | 5 | 5 | 20 | 7 | 21 | − 1 -1 |

17 | 3 | 4 | 10 | 6 | 6 | 21 | 24 | 28 | 1 |

18 | 3 | 4 | 10 | 6 | 6 | 7 | 24 | 25 | 1 |

19 | 4 | 5 | 6 | 7 | 7 | 21 | 25 | 28 | 0 |

20 | 15 | 14 | 16 | 8 | 8 | 1 | 9 | 3 | 1 |

21 | 19 | 17 | 16 | 8 | 8 | 1 | 9 | 3 | 0 |

22 | 16 | 8 | 27 | 9 | 9 | 3 | 29 | 10 | 1 |

23 | 9 | 3 | 29 | 10 | 10 | 6 | 26 | 24 | 1 |

24 | 17 | 18 | 14 | 11 | 11 | 12 | 1 | 2 | − 1 -1 |

25 | 19 | 18 | 15 | 11 | 11 | 12 | 1 | 2 | 0 |

26 | 18 | 23 | 11 | 12 | 12 | 30 | 2 | 13 | − 1 -1 |

27 | 12 | 30 | 2 | 13 | 13 | 22 | 5 | 20 | − 1 -1 |

28 | 19 | 17 | 15 | 14 | 14 | 11 | 8 | 1 | 0 |

29 | 18 | 23 | 1 | 2 | 2 | 22 | 4 | 20 | − 1 -1 |

30 | 16 | 1 | 27 | 3 | 3 | 4 | 26 | 24 | 1 |

Table 3: Automaton to compute FAB \fab

Once we have guessed the automaton, we can verify it as follows:

1. 1.

∀ i ​ ∀ j ​ FAB ⁡ [0] ​ [i] ​ [j] = 0 \forall i\ \forall j\ \fab[0][i][j]=0. This is the basis for an induction.

2. 2.

Induction steps:

  - •

∀ i ​ ∀ j ​ ∀ n ⁡ ( 𝐟 ⁡ [i + n] = 𝐟 ⁡ [j + n]) ⟹ ( FAB ⁡ [n] ​ [i] ​ [j] = FAB ⁡ [n + 1] ​ [i] ​ [j]) \forall i\ \forall j\ \forall n\ ({\bf f}[i+n]={\bf f}[j+n])\implies(\fab[n][i][j]=\fab[n+1][i][j]).

  - •

∀ i ​ ∀ j ​ ∀ n ⁡ ( ( 𝐟 ⁡ [i + n] = 0) ∧ ( 𝐟 ⁡ [j + n] = 1)) ⟹ ( ( ( FAB ⁡ [n] ​ [i] ​ [j] = − 1) ∧ ( FAB ⁡ [n + 1] ​ [i] ​ [j] = 0)) ∨ ( ( FAB ⁡ [n] ​ [i] ​ [j] = 0) ∧ ( FAB ⁡ [n + 1] ​ [i] ​ [j] = 1))) \forall i\ \forall j\ \forall n\ (({\bf f}[i+n]=0)\wedge({\bf f}[j+n]=1))\implies(((\fab[n][i][j]=-1)\wedge(\fab[n+1][i][j]=0))\vee((\fab[n][i][j]=0)\wedge(\fab[n+1][i][j]=1)))

  - •

∀ i ​ ∀ j ​ ∀ n ⁡ ( ( 𝐟 ⁡ [i + n] = 0) ∧ ( 𝐟 ⁡ [j + n] = 1)) ⟹ ( ( ( FAB ⁡ [n] ​ [i] ​ [j] = 1) ∧ ( FAB ⁡ [n + 1] ​ [i] ​ [j] = 0)) ∨ ( ( FAB ⁡ [n] ​ [i] ​ [j] = 0) ∧ ( FAB ⁡ [n + 1] ​ [i] ​ [j] = − 1))) \forall i\ \forall j\ \forall n\ (({\bf f}[i+n]=0)\wedge({\bf f}[j+n]=1))\implies(((\fab[n][i][j]=1)\wedge(\fab[n+1][i][j]=0))\vee((\fab[n][i][j]=0)\wedge(\fab[n+1][i][j]=-1))).

As the first application, we prove

###### Theorem 64.

The Fibonacci word 𝐟 \bf f has abelian squares of all orders.

###### Proof.

We use the predicate

 | ∃ i ⁡ ( FAB ⁡ [n] ​ [i] ​ [i + n] = 0). \exists i\ (\fab[n][i][i+n]=0). |  |

The resulting automaton accepts all n ≥ 0 n\geq 0. The total computing time was 141 ms. ∎

Cummings and Smyth [31] counted the total number of all occurrences of (nonempty) abelian squares in the Fibonacci words X i X_{i}. We can do this by using the predicate

 | ( k > 0) ∧ ( i + 2 ​ k ≤ n) ∧ ( FAB ⁡ [k] ​ [i] ​ [i + k] = 0), (k>0)\wedge(i+2k\leq n)\wedge(\fab[k][i][i+k]=0), |  |

using the techniques in Section 8 and considering the case where n = F i n=F_{i}.

When we do, we get a linear representation of rank 127 that counts the total number w ⁡ ( n) w(n) of occurrences of abelian squares in the prefix of length n n of the Fibonacci word.

To recover the Cummings-Smyth result we compute the minimal polynomial of the matrix M 0 M_{0} corresponding to the predicate above. It is

 | x 4 ​ ( x − 1) ​ ( x + 1) ​ ( x 2 + x + 1) ​ ( x 2 − 3 ​ x + 1) ​ ( x 2 − x + 1) ​ ( x 2 + x − 1) ​ ( x 2 − x − 1). x^{4}(x-1)(x+1)(x^{2}+x+1)(x^{2}-3x+1)(x^{2}-x+1)(x^{2}+x-1)(x^{2}-x-1). |  |

This means that w ⁡ ( F n) w(F_{n}), that is, w w evaluated at 10 n − 2 10^{n-2} in Fibonacci representation, is a linear combination of the roots of this polynomial to the n n ’th power (more precisely, the ( n − 2) (n-2) th, but this detail is unimportant). The roots of the polynomial are

 | − 1, 1, ( − 1 ± i ​ 3) / 2, ( 3 ± 5) / 2, ( 1 ± i ​ 3) / 2, ( − 1 ± 5) / 2, ( 1 ± 5) / 2. -1,1,(-1\pm i\sqrt{3})/2,(3\pm\sqrt{5})/2,(1\pm i\sqrt{3})/2,(-1\pm\sqrt{5})/2,(1\pm\sqrt{5})/2. |  |

Solving for the coefficients as we did in Section 8 we get

###### Theorem 65.

For all n ≥ 0 n\geq 0 we have

 | w ⁡ ( F n) = c 1 ​ ( 3 + 5 2) n + c 1 ​ ( 3 − 5 2) n + c 2 ​ ( 1 + 5 2) n + c 2 ​ ( 1 − 5 2) n + c 3 ​ ( 1 + i ​ 3 2) n + c 3 ¯ ​ ( 1 − i ​ 3 2) n + c 4 ​ ( − 1 + i ​ 3 2) n + c 4 ¯ ​ ( − 1 − i ​ 3 2) n + c 5 ​ ( − 1) n, w(F_{n})=c_{1}\left({{3+\sqrt{5}}\over 2}\right)^{n}+c_{1}\left({{3-\sqrt{5}}\over 2}\right)^{n}+c_{2}\left({{1+\sqrt{5}}\over 2}\right)^{n}+c_{2}\left({{1-\sqrt{5}}\over 2}\right)^{n}+\\ c_{3}\left({{1+i\sqrt{3}}\over 2}\right)^{n}+\overline{c_{3}}\left({{1-i\sqrt{3}}\over 2}\right)^{n}+c_{4}\left({{-1+i\sqrt{3}}\over 2}\right)^{n}+\overline{c_{4}}\left({{-1-i\sqrt{3}}\over 2}\right)^{n}+c_{5}(-1)^{n}, |  |

where

 | c 1 \displaystyle c_{1} | = 1 / 40 \displaystyle=1/40 |  |

 | c 2 \displaystyle c_{2} | = − 5 / 20 \displaystyle=-\sqrt{5}/20 |  |

 | c 3 \displaystyle c_{3} | = ( 1 − i ​ 3) / 24 \displaystyle=(1-i\sqrt{3})/24 |  |

 | c 4 \displaystyle c_{4} | = i ​ 3 / 24 \displaystyle=i\sqrt{3}/24 |  |

 | c 5 \displaystyle c_{5} | = − 2 / 15, \displaystyle=-2/15, |  |

and here x ¯ \overline{x} denotes complex conjugate. Here the parts corresponding to the constants c 3, c 4, c 5 c_{3},c_{4},c_{5} form a periodic sequence of period 6.

Next, we turn to what is apparently a new result. Let h ⁡ ( n) h(n) denote the total number of distinct factors (not occurrences of factors) that are abelian squares in the Fibonacci word X n X_{n}.

In this case we need the predicate

 | ( k ≥ 1) ∧ ( i + 2 ​ k ≤ n) ∧ ( FAB ⁡ [k] ​ [i] ​ [i + k] = 0) ∧ ( ∀ j < i ⁡ ( ∃ t < 2 ​ k ​ ( 𝐟 ⁡ [j + t] ≠ 𝐟 ⁡ [i + t]))). (k\geq 1)\wedge(i+2k\leq n)\wedge(\fab[k][i][i+k]=0)\wedge(\forall j<i\ (\exists t<2k\ ({\bf f}[j+t]\not={\bf f}[i+t]))). |  |

We get the minimal polynomial

 | x 4 ​ ( x + 1) ​ ( x 2 + x + 1) ​ ( x 2 − 3 ​ x + 1) ​ ( x 2 − x + 1) ​ ( x 2 + x − 1) ​ ( x 2 − x − 1) ​ ( x − 1) 2. x^{4}(x+1)(x^{2}+x+1)(x^{2}-3x+1)(x^{2}-x+1)(x^{2}+x-1)(x^{2}-x-1)(x-1)^{2}. |  |

Using the same technique as above we get

###### Theorem 66.

For n ≥ 2 n\geq 2 we have h ⁡ ( n) = a 1 ​ c 1 n + ⋯ + a 10 ​ c 10 n h(n)=a_{1}c_{1}^{n}+\cdots+a_{10}c_{10}^{n} where

 | a 1 \displaystyle a_{1} | = ( − 2 + 5) / 20 \displaystyle=(-2+\sqrt{5})/20 |  |

 | a 2 \displaystyle a_{2} | = ( − 2 − 5) / 20 \displaystyle=(-2-\sqrt{5})/20 |  |

 | a 3 \displaystyle a_{3} | = ( 5 − 5) / 20 \displaystyle=(5-\sqrt{5})/20 |  |

 | a 4 \displaystyle a_{4} | = ( 5 + 5) / 20 \displaystyle=(5+\sqrt{5})/20 |  |

 | a 5 \displaystyle a_{5} | = 1 / 30 \displaystyle=1/30 |  |

 | a 6 \displaystyle a_{6} | = − 5 / 6 \displaystyle=-5/6 |  |

 | a 7 \displaystyle a_{7} | = ( 1 / 12) − i ​ 3 / 12 \displaystyle=(1/12)-i\sqrt{3}/12 |  |

 | a 8 \displaystyle a_{8} | = ( 1 / 12) + i ​ 3 / 12 \displaystyle=(1/12)+i\sqrt{3}/12 |  |

 | a 9 \displaystyle a_{9} | = ( 1 / 6) + i ​ 3 / 12 \displaystyle=(1/6)+i\sqrt{3}/12 |  |

 | a 10 \displaystyle a_{10} | = ( 1 / 6) − i ​ 3 / 12 \displaystyle=(1/6)-i\sqrt{3}/12 |  |

and

 | c 1 \displaystyle c_{1} | = ( 3 + 5) / 2 \displaystyle=(3+\sqrt{5})/2 |  |

 | c 2 \displaystyle c_{2} | = ( 3 − 5) / 2 \displaystyle=(3-\sqrt{5})/2 |  |

 | c 3 \displaystyle c_{3} | = ( 1 + 5) / 2 \displaystyle=(1+\sqrt{5})/2 |  |

 | c 4 \displaystyle c_{4} | = ( 1 − 5) / 2 \displaystyle=(1-\sqrt{5})/2 |  |

 | c 5 \displaystyle c_{5} | = − 1 \displaystyle=-1 |  |

 | c 6 \displaystyle c_{6} | = 1 \displaystyle=1 |  |

 | c 7 \displaystyle c_{7} | = ( 1 / 2) + i ​ 3 / 2 \displaystyle=(1/2)+i\sqrt{3}/2 |  |

 | c 8 \displaystyle c_{8} | = ( 1 / 2) − i ​ 3 / 2 \displaystyle=(1/2)-i\sqrt{3}/2 |  |

 | c 9 \displaystyle c_{9} | = ( − 1 / 2) + i 3 / 2 \displaystyle=(-1/2)+i\sqrt{3}/2 |  |

 | c 10 \displaystyle c_{10} | = ( − 1 / 2) − i 3 / 2. \displaystyle=(-1/2)-i\sqrt{3}/2. |  |

For another new result, consider counting the total number a ⁡ ( n) a(n) of distinct factors of length 2 ​ n 2n of the infinite word 𝐟 \bf f that are abelian squares.

This function is rather erratic. The following table gives the first few values:

n n | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 |

a ⁡ ( n) a(n) | 1 | 3 | 5 | 1 | 9 | 5 | 5 | 15 | 3 | 13 | 13 | 5 | 25 | 9 | 15 | 25 | 1 | 27 | 19 | 11 |

We use the predicate

 | ( n ≥ 1) ∧ ( FAB ⁡ [n] ​ [i] ​ [i + n] = 0) ∧ ( ∀ j < i ⁡ ( ∃ t < 2 ​ n ​ ( 𝐟 ⁡ [j + t] ≠ 𝐟 ⁡ [i + t]))). (n\geq 1)\wedge(\fab[n][i][i+n]=0)\wedge(\forall j<i\ (\exists t<2n\ ({\bf f}[j+t]\not={\bf f}[i+t]))). |  |

to create the matrices and vectors.

###### Theorem 67.

a ⁡ ( n) = 1 a(n)=1 infinitely often and a ⁡ ( n) = 2 ​ n − 1 a(n)=2n-1 infinitely often. More precisely a ⁡ ( n) = 1 a(n)=1 iff ( n) F = 1 (n)_{F}=1 or ( n) F = ( 100) i ​ 101 (n)_{F}=(100)^{i}101 for i ≥ 0 i\geq 0, and a ⁡ ( n) = 2 ​ n − 1 a(n)=2n-1 iff ( n) F = 10 i (n)_{F}=10^{i} for i ≥ 0 i\geq 0.

###### Proof.

For the first statement, we create a DFA accepting those ( n) F (n)_{F} for which a ⁡ ( n) = 1 a(n)=1, via the predicate

 | ∀ i ​ ∀ j ⁡ ( ( FAB ⁡ [n] ​ [i] ​ [i + n] = 0) ∧ ( FAB ⁡ [n] ​ [j] ​ [j + n] = 0)) ⟹ ( ∀ t < 2 ​ n ​ ( 𝐟 ⁡ [j + t] = 𝐟 ⁡ [i + t])). \forall i\ \forall j\ ((\fab[n][i][i+n]=0)\wedge(\fab[n][j][j+n]=0))\implies(\forall t<2n\ ({\bf f}[j+t]={\bf f}[i+t])). |  |

The resulting 6 6 -state automaton accepts the set specified.

For the second result, we first compute the minimal polynomial of the matrix M 0 M_{0} of the linear representation. It is x 5 ​ ( x − 1) ​ ( x + 1) ​ ( x 2 − x − 1) x^{5}(x-1)(x+1)(x^{2}-x-1). This means that, for n ≥ 5 n\geq 5, we have a ⁡ ( F n) = c 1 + c 2 ​ ( − 1) n + c 3 ​ α n + c 4 ​ β n a(F_{n})=c_{1}+c_{2}(-1)^{n}+c_{3}\alpha^{n}+c_{4}\beta^{n} where, as usual, α = ( 1 + 5) / 2 \alpha=(1+\sqrt{5})/2 and β = ( 1 − 5) / 2 \beta=(1-\sqrt{5})/2. Solving for the constants, we determine that a ⁡ ( F n) = 2 ​ F n − 1 a(F_{n})=2F_{n}-1 for n ≥ 2 n\geq 2, as desired.

To show that these are the only cases for which a ⁡ ( n) = 2 ​ n − 1 a(n)=2n-1, we use a predicate that says that there are not at least three different factors of length 2 ​ n 2n that are not abelian squares. Running this through our program results in only the cases previously discussed. ∎

Finally, we turn to abelian cubes. Unlike the case of squares, some orders do not appear in 𝐟 \bf f.

###### Theorem 68.

The Fibonacci word 𝐟 \bf f contains, as a factor, an abelian cube of order n n iff ( n) F (n)_{F} is accepted by the automaton below.

Figure 29: Automaton accepting orders of abelian cubes in 𝐟 \bf f

Theorem 63 has the following interesting corollary.

###### Corollary 69.

Let h: { 0, 1 } ∗ → Δ ∗ h:\{0,1\}^{*}\rightarrow\Delta^{*} be an arbitrary morphism such that h ⁡ ( 01) ≠ ϵ h(01)\not=\epsilon. Then h ⁡ ( 𝐟) h({\bf f}) is an infinite Fibonacci-automatic word.

###### Proof.

From Theorem 63 we see that there is a predicate ZC ⁡ ( n, n ′) \zc(n,n^{\prime}) which is true if n ′ = | 𝐟 [0.. n − 1] | 0 n^{\prime}=|{\bf f}[0..n-1]|_{0} and false otherwise, and this predicate can be implemented as a finite automaton taking the inputs n n and n ′ n^{\prime} in Fibonacci representation.

Suppose h ⁡ ( 0) = w h(0)=w and h ⁡ ( 1) = x h(1)=x. Now, to show that h( f) is Fibonacci-automatic, it suffices to show that, for each letter a ∈ Δ a\in\Delta, the language of “fibers”

 | L a = { ( n) F: ( h ⁡ ( 𝐟)) ​ [n] = a } L_{a}=\{(n)_{F}:(h({\bf f}))[n]=a\} |  |

is regular.

To see this, we write a predicate for the n n in the definition of L a L_{a}, namely

 | ∃ q ​ ∃ r 0 ​ ∃ r 1 ​ ∃ m ⁡ ( q ≤ n < q + | h ⁡ ( 𝐟 ⁡ [m]) |) ∧ ZC ⁡ ( m, r 0) ∧ ( r 0 + r 1 = m) ∧ ( r 0 ​ | w | + r 1 ​ | x | = q) ∧ ( ( 𝐟 ⁡ [m] = 0 ∧ w ⁡ [n − q] = a) ∨ ( 𝐟 ⁡ [m] = 1 ∧ x ⁡ [n − q] = a)). \exists q\ \exists r_{0}\ \exists r_{1}\ \exists m\ (q\leq n<q+|h({\bf f}[m])|)\ \wedge\ \zc(m,r_{0})\ \wedge\ (r_{0}+r_{1}=m)\wedge\\ (r_{0}|w|+r_{1}|x|=q)\ \wedge\ (({\bf f}[m]=0\ \wedge\ w[n-q]=a)\ \vee\ ({\bf f}[m]=1\ \wedge\ x[n-q]=a)). |  |

Notice that the predicate looks like it uses multiplication, but this multiplication can be replaced by repeated addition since | w | |w| and | x | |x| are constants here.

Unpacking this predicate we see that it asserts the existence of m m, q q, r 0 r_{0}, and r 1 r_{1} having the meaning that

- •

the n n ’th symbol of h( f) lies inside the block h ⁡ ( 𝐟 ⁡ [m]) h({\bf f}[m]) and is in fact the ( n − q) (n-q) ’th symbol in the block (with the first symbol being symbol 0)

- •

𝐟 [0.. m − 1] {\bf f}[0..m-1] has r 0 r_{0} 0’s in it

- •

𝐟 [0.. m − 1] {\bf f}[0..m-1] has r 1 r_{1} 1’s in it

- •

the length of h ( 𝐟 [0.. m − 1]) h({\bf f}[0..m-1]) is q q

Since everything in this predicate is in the logical theory ( ℕ, +, <, F) ({\mathbb{N}},+,<,F) where F F is the predicate for the Fibonacci word, the language L a L_{a} is regular. ∎

###### Remark 70.

Notice that everything in this proof goes through for other numeration systems, provided the original word has the property that the Parikh vector of the prefix of length n n is synchronized.

## 10 Details about our implementation

Our program is written in JAVA, and was developed using the Eclipse development environment. 2 2 2 Available from http://www.eclipse.org/ide/. We used the dk.brics.automaton package, developed by Anders Møller at Aarhus University, for automaton minimization. 3 3 3 Available from http://www.brics.dk/automaton/. Maple 15 was used to compute characteristic polynomials. 4 4 4 Available from http://www.maplesoft.com. The GraphViz package was used to display automata. 5 5 5 Available from http://www.graphviz.org.

Our program consists of about 2000 lines of code. We used Hopcroft’s algorithm for DFA minimization.

A user interface is provided to enter queries in a language very similar to the language of first-order logic. The intermediate and final result of a query are all automata. At every intermediate step, we chose to do minimization and determinization, if necessary. Each automaton accepts tuples of integers in the numeration system of choice. The built-in numeration systems are ordinary base- k k representations and Fibonacci base. However, the program can be used with any numeration system for which an automaton for addition and ordering can be provided. These numeration system-specific automata can be declared in text files following a simple syntax. For the automaton resulting from a query it is always guaranteed that if a tuple t t of integers is accepted, all tuples obtained from t t by addition or truncation of leading zeros are also accepted. In Fibonacci representation, we make sure that the accepting integers do not contain consecutive 1 1 ’s.

The program was tested against hundreds of different test cases varying in simplicity from the most basic test cases testing only one feature at a time, to more comprehensive ones with many alternating quantifiers. We also used known facts about automatic sequences and Fibonacci word in the literature to test our program, and in all those cases we were able to get the same result as in the literature. In a few cases, we were even able to find small errors in those earlier results.

The source code and manual will soon be available for free download.

## 11 Acknowledgments

We thank Kalle Saari for bringing our attention to the small error in [39]. We thank Narad Rampersad and Michel Rigo for useful suggestions.

Eric Rowland thought about the proof of Theorem 54 with us in 2010, and was able to prove at that time that the word 1213121512131218 ⋯ 1213121512131218\cdots avoids additive squares. We acknowledge his prior work on this problem and thank him for allowing us to quote it here.

## References

- [1] C. Ahlbach, J. Usatine, C. Frougny, and N. Pippenger. Efficient algorithms for Zeckendorf arithmetic. Fibonacci Quart. 51 (2013), 249–256.
- [2] J.-P. Allouche, N. Rampersad, and J. Shallit. Periodicity, repetitions, and orbits of an automatic sequence. Theoret. Comput. Sci. 410 (2009), 2795–2803.
- [3] J.-P. Allouche, K. Scheicher, and R. F. Tichy. Regular maps in generalized number systems. Math. Slovaca 50 (2000), 41–58.
- [4] J.-P. Allouche and J. Shallit. Automatic Sequences: Theory, Applications, Generalizations. Cambridge University Press, 2003.
- [5] J. Berstel. Mots de Fibonacci. Séminaire d’Informatique Théorique, LITP 6-7 (1980–81), 57–78.
- [6] J. Berstel. Fonctions rationnelles et addition. In M. Blab, editor, Théorie des Langages, École de printemps d’informatique théorique, pp. 177–183. LITP, 1982.
- [7] J. Berstel. Fibonacci words—a survey. In G. Rozenberg and A. Salomaa, editors, The Book of L, pp. 13–27. Springer-Verlag, 1986.
- [8] J. Berstel and C. Reutenauer. Noncommutative Rational Series with Applications, Vol. 137 of Encylopedia of Mathematics and Its Applications. Cambridge University Press, 2011.
- [9] B. Bischoff, J. D. Currie, and D. Nowotka. Unary patterns with involution. Internat. J. Found. Comp. Sci. 23 (2012), 1641–1652.
- [10] B. Bischoff and D. Nowotka. Pattern avoidability with involution. In WORDS 2011, pp. 65–70, 2011. Available at http://rvg.web.cse.unsw.edu.au/eptcs/content.cgi?WORDS2011.
- [11] A. Blondin Massé, S. Brlek, A. Garon, and S. Labbé. Two infinite families of polyominoes that tile the plane by translation in two distinct ways. Theoret. Comput. Sci. 412 (2011), 4778–4786.
- [12] A. Blondin Massé, S. Brlek, S. Labbé, and M. Mendès France. Fibonacci snowflakes. Ann. Sci. Math. Québec 35 (2011), 141–152.
- [13] A. Blondin Massé, S. Brlek, S. Labbé, and M. Mendès France. Complexity of the Fibonacci snowflake. Fractals 20 (2012), 257–260.
- [14] J.-P. Borel and F. Laubie. Quelques mots sur la droite projective réelle. J. Théorie Nombres Bordeaux 5 (1993), 23–51.
- [15] T. C. Brown and A. R. Freedman. Arithmetic progressions in lacunary sets. Rocky Mountain J. Math. 17 (1987), 587–596.
- [16] V. Bruyère and G. Hansel. Bertrand numeration systems and recognizability. Theoret. Comput. Sci. 181 (1997), 17–43.
- [17] V. Bruyère, G. Hansel, C. Michaux, and R. Villemaire. Logic and p p -recognizable sets of integers. Bull. Belgian Math. Soc. 1 (1994), 191–238. Corrigendum, Bull. Belg. Math. Soc. 1 (1994), 577.
- [18] J. R. Büchi. Weak secord-order arithmetic and finite automata. Zeitschrift für mathematische Logik und Grundlagen der Mathematik 6 (1960), 66–92. Reprinted in S. Mac Lane and D. Siefkes, eds., The Collected Works of J. Richard Büchi, Springer-Verlag, 1990, pp. 398–424.
- [19] L. Carlitz. Fibonacci representations. Fibonacci Quart. 6 (1968), 193–220.
- [20] A. Carpi and V. D’Alonzo. On the repetitivity index of infinite words. Internat. J. Algebra Comput. 19 (2009), 145–158.
- [21] A. Carpi and V. D’Alonzo. On factors of synchronized sequences. Theoret. Comput. Sci. 411 (2010), 3932–3937.
- [22] A. Carpi and C. Maggi. On synchronized sequences and their separators. RAIRO Inform. Théor. App. 35 (2001), 513–524.
- [23] J. Cassaigne. Sequences with grouped factors. In Developments in Language Theory III, pp. 211–222. Aristotle University of Thessaloniki, 1998.
- [24] J. Cassaigne, J. Currie, L. Schaeffer, and J. Shallit. Avoiding three consecutive blocks of the same size and same sum. Preprint, 2013.
- [25] E. Charlier, N. Rampersad, and J. Shallit. Enumeration and decidable properties of automatic sequences. Internat. J. Found. Comp. Sci. 23 (2012), 1035–1066.
- [26] M. Christou, M. Crochemore, and C. S. Iliopoulos. Quasiperiodicities in Fibonacci strings. To appear in Ars Combinatoria. Preprint available at http://arxiv.org/abs/1201.6162, 2012.
- [27] W.-F. Chuan. Symmetric Fibonacci words. Fibonacci Quart. 31 (1993), 251–255.
- [28] A. Cobham. Uniform tag sequences. Math. Systems Theory 6 (1972), 164–192.
- [29] M. Crochemore. An optimal algorithm for computing the repetitions in a word. Inform. Process. Lett. 12 (1981), 244–250.
- [30] L. J. Cummings, D. Moore, and J. Karhumäki. Borders of Fibonacci strings. J. Combin. Math. Combin. Comput. 20 (1996), 81–87.
- [31] L. J. Cummings and W. F. Smyth. Weak repetitions in strings. J. Combin. Math. Combin. Comput. 24 (1997), 33–48.
- [32] J. D. Currie. Pattern avoidance with involution. Available at http://arxiv.org/abs/1105.2849, 2011.
- [33] J. D. Currie, N. Rampersad, and K. Saari. Suffix conjugates for a class of morphic subshifts. In J. Karhumäki, A. Lepistö, and L. Zamboni, editors, WORDS 2013, Vol. 8079 of Lecture Notes in Computer Science, pp. 95–106. Springer-Verlag, 2013.
- [34] J. D. Currie and K. Saari. Least periods of factors of infinite words. RAIRO Inform. Théor. App. 43 (2009), 165–178.
- [35] A. de Luca. A combinatorial property of the Fibonacci words. Inform. Process. Lett. 12 (1981), 193–195.
- [36] X. Droubay. Palindromes in the Fibonacci word. Inform. Process. Lett. 55 (1995), 217–221.
- [37] D. D. A. Epple and J. Siefken. Collapse: a Fibonacci and Sturmian game. Available at http://www.siefkenj.com/tmp/Fibonacci-4.pdf, 2014.
- [38] A. S. Fraenkel. Systems of numeration. Amer. Math. Monthly 92 (1985), 105–114.
- [39] A. S. Fraenkel and J. Simpson. The exact number of squares in Fibonacci words. Theoret. Comput. Sci. 218 (1999), 95–106.
- [40] C. Frougny. Linear numeration systems of order two. Inform. Comput. 77 (1988), 233–259.
- [41] C. Frougny. Fibonacci representations and finite automata. IEEE Trans. Inform. Theory 37 (1991), 393–399.
- [42] C. Frougny. Representations of numbers and finite automata. Math. Systems Theory 25 (1992), 37–60.
- [43] C. Frougny and B. Solomyak. On representation of integers in linear numeration systems. In M. Pollicott and K. Schmidt, editors, Ergodic Theory of ℤ d {\mathbb{Z}}^{d} Actions (Warwick, 1993–1994), Vol. 228 of London Mathematical Society Lecture Note Series, pp. 345–368. Cambridge University Press, 1996.
- [44] D. Goc, D. Henshall, and J. Shallit. Automatic theorem-proving in combinatorics on words. In N. Moreira and R. Reis, editors, CIAA 2012, Vol. 7381 of Lecture Notes in Computer Science, pp. 180–191. Springer-Verlag, 2012.
- [45] D. Goc, H. Mousavi, and J. Shallit. On the number of unbordered factors. In A.-H. Dediu, C. Martin-Vide, and B. Truthe, editors, LATA 2013, Vol. 7810 of Lecture Notes in Computer Science, pp. 299–310. Springer-Verlag, 2013.
- [46] D. Goc, K. Saari, and J. Shallit. Primitive words and Lyndon words in automatic and linearly recurrent sequences. In A.-H. Dediu, C. Martin-Vide, and B. Truthe, editors, LATA 2013, Vol. 7810 of Lecture Notes in Computer Science, pp. 311–322. Springer-Verlag, 2013.
- [47] D. Goc, L. Schaeffer, and J. Shallit. The subword complexity of k k -automatic sequences is k k -synchronized. In M.-P. Béal and O. Carton, editors, DLT 2013, Vol. 7907 of Lecture Notes in Computer Science, pp. 252–263. Springer-Verlag, 2013.
- [48] M. Guay-Paquet and J. Shallit. Avoiding squares and overlaps over the natural numbers. Discrete Math. 309 (2009), 6245–6254.
- [49] L. Halbeisen and N. Hungerbühler. An application of Van der Waerden’s theorem in additive number theory. INTEGERS: Elect. J. of Combin. Number Theory 0 (2000), #A7. http://www.integers-ejcnt.org/vol0.html.
- [50] C. Holton and L. Q. Zamboni. Directed graphs and substitutions. Theory Comput. Systems 34 (2001), 545–564.
- [51] S. Homer and A. L. Selman. Computability and Complexity Theory. Springer-Verlag, 2nd edition, 2011.
- [52] C. S. Iliopoulos, D. Moore, and W. F. Smyth. A characterization of the squares in a Fibonacci string. Theoret. Comput. Sci. 172 (1997), 281–291.
- [53] J. Karhumäki. On cube-free ω \omega -words generated by binary morphisms. Disc. Appl. Math. 5 (1983), 279–297.
- [54] R. Kolpakov and G. Kucherov. On maximal repetitions in words. In G. Ciobanu and G. Păun, editors, Fundamentals of Computation Theory: FCT ’99, Vol. 1684 of Lecture Notes in Computer Science, pp. 374–385. Springer-Verlag, 1999.
- [55] C. G. Lekkerkerker. Voorstelling van natuurlijke getallen door een som van getallen van Fibonacci. Simon Stevin 29 (1952), 190–195.
- [56] F. Mignosi and G. Pirillo. Repetitions in the Fibonacci infinite word. RAIRO Inform. Théor. App. 26 (1992), 199–204.
- [57] A. Monnerot-Dumaine. The Fibonacci word fractal. Published electronically at http://hal.archives-ouvertes.fr/hal-00367972/fr/, 2009.
- [58] M. Morse and G. A. Hedlund. Symbolic dynamics II. Sturmian trajectories. Amer. J. Math. 62 (1940), 1–42.
- [59] A. Ostrowski. Bemerkungen zur Theorie der Diophantischen Approximationen. Abh. Math. Sem. Hamburg 1 (1922), 77–98,250–251. Reprinted in Collected Mathematical Papers, Vol. 3, pp. 57–80.
- [60] G. Pirillo. Fibonacci numbers and words. Discrete Math. 173 (1997), 197–207.
- [61] G. Pirillo and S. Varricchio. On uniformly repetitive semigroups. Semigroup Forum 49 (1994), 125–129.
- [62] M. Presburger. Über die Volständigkeit eines gewissen Systems der Arithmetik ganzer Zahlen, in welchem die Addition als einzige Operation hervortritt. In Sparawozdanie z I Kongresu matematyków krajów slowianskich, pp. 92–101, 395. Warsaw, 1929.
- [63] M. Presburger. On the completeness of a certain system of arithmetic of whole numbers in which addition occurs as the only operation. Hist. Phil. Logic 12 (1991), 225–233.
- [64] N. Rampersad and J. Shallit. Words avoiding reversed subwords. J. Combin. Math. Combin. Comput. 54 (2005), 157–164.
- [65] M. Rao. On some generalizations of abelian power avoidability. Preprint, 2013.
- [66] G. Rote. Sequences with subword complexity 2 ​ n 2n. J. Number Theory 46 (1994), 196–213.
- [67] K. Saari. Periods of factors of the Fibonacci word. In WORDS 07, 2007.
- [68] K. Saari. Lyndon words and Fibonacci numbers. J. Combin. Theory. Ser. A 121 (2014), 34–44.
- [69] L. Schaeffer. Deciding properties of automatic sequences. Master’s thesis, University of Waterloo, 2013.
- [70] L. Schaeffer and J. Shallit. The critical exponent is computable for automatic sequences. Internat. J. Found. Comp. Sci. 23 (2012), 1611–1626.
- [71] P. Séébold. Propriétés combinatoires des mots infinis engendrés par certains morphismes (Thèse de 3 e 3^{\rm e} cycle). PhD thesis, Université P. et M. Curie, Institut de Programmation, Paris, 1985.
- [72] J. O. Shallit. A generalization of automatic sequences. Theoret. Comput. Sci. 61 (1988), 1–16.
- [73] J. Shallit. Decidability and enumeration for automatic sequences: a survey. In A. A. Bulatov and A. M. Shur, editors, CSR 2013, Vol. 7913 of Lecture Notes in Computer Science, pp. 49–63. Springer-Verlag, 2013.
- [74] E. Zeckendorf. Représentation des nombres naturels par une somme de nombres de Fibonacci ou de nombres Lucas. Bull. Soc. Roy. Liège 41 (1972), 179–182.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/1406.0669
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/1406.0670
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1406.0670
[7]: https://arxiv.org/pdf/1406.0670
[8]: /html/1406.0671
