<!-- source: https://ar5iv.labs.arxiv.org/html/1503.01168 | converted from HTML -->

[1503.01168] On the Number of ON Cells in Cellular Automata

# On the Number of ON Cells in Cellular Automata

N. J. A. Sloane

The OEIS Foundation Inc.,

11 South Adelaide Ave., Highland Park, NJ 08904, USA

Email: [njasloane@gmail.com][1]

March 3, 2015

To Ron Graham, commemorating his 80th birthday,
and 47 years of friendship

###### Abstract

If a cellular automaton (CA) is started with a single ON cell, how many cells will be ON after n n generations? For certain “odd-rule” CAs, including Rule 150, Rule 614, and Fredkin’s Replicator, the answer can be found by using the combination of a new transformation of sequences, the run length transform, and some delicate scissor cuts. Several other CAs are also discussed, although the analysis becomes more difficult as the patterns become more intricate.

## 1 Introduction

When confronted with a number sequence, the first thing is to try to conjecture a rule or formula, and then (the hard part) prove that the formula is correct. This article had its origin in the study of one such sequence, 1, 8, 8, 24, 8, 64, 24, 112, 8, 64, 64, 192, … 1,8,8,24,8,64,24,112,8,64,64,192,\ldots ( [A160239][2] 1 1 1 Six-digit numbers prefixed by A refer to entries in [16].), although several similar sequences will also be discussed.

These sequences arise from studying how activity spreads in cellular automata (for background see [2, 5, 8, 11, 14, 17, 20, 21, 23, 24, 26]). If we start with a single ON cell, how many cells will be ON after n n generations? The sequence above arises from the CA known as Fredkin’s Replicator [13]. In 2014, Hrothgar sent the author a manuscript [10] studying this CA, and conjectured that the sequence satisfied a certain recurrence. One of the goals of the present paper is to prove that this conjecture is correct—see ( 31).

In Section 2 we discuss a general class (the “odd-rule” CAs) to which Fredkin’s Replicator belongs, and in § 3 we introduce an operation on number sequences (the “run length transform”) which helps in understanding the resulting sequences. Fredkin’s Replicator, which is based on the Moore neighborhood, is the subject of § 4, and § 5 analyzes another odd-rule CA, based on the von Neumann neighborhood with a center cell. Although these two CAs are similar, different techniques are required for establishing the recurrences. Both proofs involve making scissor cuts to dissect the configuration of ON cells into recognizable pieces.

Section 6 discusses some other CAs in one, two, and three dimensions where it is possible to find a formula, and some for which no formula is presently known. In dimension one, Stephen Wolfram’s well-known list [17, 24, 26] of 256 different CAs based on a three-celled neighborhood gives rise to just seven interesting sequences (§ 6.1). Other two-dimensional CAs are discussed in §§ 6.2, 6.3, and the three-dimensional analog of Fredkin’s Replicator in § 6.4. The final section (§ 7) gives some additional properties of the run length transform. For many further examples of cellular automata sequences, see [2] and [16] (the index to [16] lists nearly 200 such sequences).

[image: Refer to caption]

Figure 1: Some two-dimensional neighborhoods (Figs. (i) and (iv) are three and five cells wide, respectively).

## 2 Odd-rule CAs

We consider cellular automata whose cells form a d d -dimensional cubic lattice ℤ d \mathbb{Z}^{d}, where d d is 1, 2, or 3. Each cell is either ON or OFF, and an ON cell with center at the lattice point u = ( u 1, u 2, …, u d) ∈ ℤ d u=(u_{1},u_{2},\ldots,u_{d})\in\mathbb{Z}^{d} will be identified with the monomial x u = x 1 u 1 x 2 u 2 ⋯ x d u d x^{u}=x_{1}^{u_{1}}x_{2}^{u_{2}}\cdots x_{d}^{u_{d}}, which we regard as an element of the ring of Laurent polynomials ℛ = GF ⁡ ( 2) ​ [x 1, x 1 − 1, …, x d, x d − 1] {\cal{R}}=\GF(2)[x_{1},x_{1}^{-1},\ldots,x_{d},x_{d}^{-1}] with mod 2 coefficients. The state of the CA is specified by giving the formal sum S S of all its ON cells. As long as only finitely many cells are ON, S S is indeed a polynomial in the variables x i x_{i} and x i − 1 x_{i}^{-1}, and is therefore an element of ℛ {\cal{R}}. We write u ∈ S u\in S to indicate that u u is ON, i.e., that x u x^{u} is a monomial in S S.

In most of this paper we will focus on what may be called “odd-rule” CAs. An odd-rule CA is defined by specifying a neighborhood of the cell at the origin, given by an element F ∈ ℛ F\in{\cal{R}} listing the cells in the neighborhood. A typical example is the Moore neighborhood in ℤ 2 \mathbb{Z}^{2}, which consists of the eight cells surrounding the cell at the origin in the square grid (see Fig. 1 (ix)), and is specified by

 | F \displaystyle F | := 1 x ​ y + 1 y + x y + 1 x + x + y x + y + x ​ y \displaystyle\penalty\ :=\penalty\ \frac{1}{xy}+\frac{1}{y}+\frac{x}{y}+\frac{1}{x}+x+\frac{y}{x}+y+xy |  |

 |  | = ( 1 x + 1 + x) ​ ( 1 y + 1 + y) − 1 ∈ ℛ = GF ⁡ ( 2) ​ [x, x − 1, y, y − 1]. \displaystyle\penalty\ =\penalty\ \left(\frac{1}{x}+1+x\right)\left(\frac{1}{y}+1+y\right)-1\penalty\ \in\penalty\ {\cal{R}}=\GF(2)[x,x^{-1},y,y^{-1}]. |  | (1) |

The neighborhood of an arbitrary cell u u is obtained by shifting F F so it is centered at u u, that is, by the product x u ​ F ∈ ℛ x^{u}F\in{\cal{R}}. Given F F, the corresponding odd-rule CA is defined by the rule that the cell at u u is ON at generation n + 1 n+1 if it is the neighbor of an odd number of cells that were ON at generation n n, and is otherwise OFF.

Our goal is to find a n ​ ( F) a_{n}(F), the number of ON cells at the n n th generation when the CA is started in generation 0 with a single ON cell at the origin. For odd-rule CAs there is a simple formula. The number of nonzero terms in an element P ∈ ℛ P\in{\cal{R}} will be denoted by | P | |P|.

###### Theorem 1.

For an odd-rule CA with neighborhood F F, the state at generation n n is equal to F n F^{n}, and a n ​ ( F) = | F n | a_{n}(F)=|F^{n}|.

###### Proof.

We use induction on n n. By definition, the initial state is 1 = F 0 1=F^{0}, and a 0 ​ ( F) = 1 a_{0}(F)=1. The ON cell at the origin turns ON all the cells in F F, so the state at generation 1 is F F itself, and a 1 ​ ( F) = | F | a_{1}(F)=|F|. Suppose the state at generation n n is F n F^{n}. An ON cell w ∈ F n w\in F^{n} will affect a cell u u if and only if u u is in the neighborhood of w w, that is, if and only if u ∈ w ​ F u\in wF. For u u to be turned ON, there must be an odd number of cells w ∈ F n w\in F^{n} with u ∈ w ​ F u\in wF. Since the coefficients in ℛ {\cal{R}} are evaluated mod 2, u u will be turned ON if and only if u ∈ ∑ w ∈ F n w ​ F = F ​ ∑ w ∈ F n w = F. F n = F n + 1 u\in\sum_{w\in F^{n}}wF=F\sum_{w\in F^{n}}w=F.F^{n}=F^{n+1}. So F n + 1 F^{n+1} is precisely the state at generation n + 1 n+1, and a n + 1 ​ ( F) = | F n + 1 | a_{n+1}(F)=|F^{n+1}|. ∎

## 3 The run length transform

We define an operation on number sequences, the “run length transform”. For an integer n ≥ 0 n\geq 0, let ℒ ⁡ ( n) {\cal{L}}(n) denote the list of the lengths of the maximal runs of 1s in the binary expansion of n n. For example, since the binary expansion of 55 is 110111, containing runs of 1s of lengths 2 and 3, ℒ ⁡ ( 55) = [2, 3] {\cal{L}}(55)=[2,3]. ℒ ⁡ ( 0) {\cal{L}}(0) is the empty list, and ℒ ⁡ ( n) {\cal{L}}(n) for n = 1, …, 12 n=1,\ldots,12 is respectively [1], [1], [2], [1], [1, 1], [2], [3], [1], [1, 1], [1, 1], [1, 2], [2] [1],[1],[2],[1],[1,1],[2],[3],[1],[1,1],[1,1],[1,2],[2] ( [A245562][3]).

Definition. The run length transform of a sequence [S n, n ≥ 0] [S_{n},n\geq 0] is the sequence [T n, n ≥ 0] [T_{n},n\geq 0] given by

 | T n = ∏ i ∈ ℒ ⁡ ( n) S i. T_{n}\penalty\ =\penalty\ \prod_{i\in{\cal{L}}(n)}S_{i}. |  | (2) |

Note that T n T_{n} depends only on the lengths of the runs of 1s in the binary expansion of n n, not on the order in which they appear. For example, since ℒ ⁡ ( 11) = [1, 2] {\cal{L}}(11)=[1,2] and ℒ ⁡ ( 13) = [2, 1] {\cal{L}}(13)=[2,1], T 11 = T 13 = S 1 ​ S 2 T_{11}=T_{13}=S_{1}S_{2}. Also T 0 = 1 T_{0}=1 (the empty product), so the value of S 0 S_{0} is never used, and will usually be taken to be 1. Further properties and additional examples of the run length transform will be given in § 7. See especially Table 4, which shows how the transformed sequence has a natural division into blocks.

Define the height ht ⁡ ( P) \height(P) of an element P ∈ ℛ P\in{\cal{R}} to be the maximal value of | e i | |e_{i}| in any monomial x 1 e 1 ⋯ x d e d x_{1}^{e_{1}}\cdots x_{d}^{e_{d}} in P P. If ht ⁡ ( P) = h \height(P)=h, the cells in P P are contained in a d d -dimensional cube centered at the origin with edges that are 2 ​ h + 1 2h+1 cells long. Note that ht ⁡ ( P ​ Q) ≤ ht ⁡ ( P) + ht ⁡ ( Q) \height(PQ)\leq\height(P)+\height(Q) and ht ⁡ ( P k) = k ​ ht ⁡ ( P) \height(P^{k})=k\height(P).

The second property that makes odd-rule CAs easier to analyze than most is the following.

###### Theorem 2.

If ht ⁡ ( F) ≤ 1 \height(F)\leq 1, then [a n ​ ( F), n ≥ 0] [a_{n}(F),n\geq 0] is the run length transform of the subsequence

 | [a 0 ​ ( F), a 1 ​ ( F), a 3 ​ ( F), a 7 ​ ( F), a 15 ​ ( F), …, a 2 k − 1 ​ ( F), …]. [a_{0}(F),a_{1}(F),a_{3}(F),a_{7}(F),a_{15}(F),\ldots,a_{2^{k}-1}(F),\ldots]. |  | (3) |

###### Proof.

The proof depends on the identity sometimes called the Freshman’s Dream, which in its simplest form states that ( x + y) 2 ≡ x 2 + y 2 (x+y)^{2}\equiv x^{2}+y^{2} mod 2, and more generally that for P ⁡ ( x 1, x 1 − 1, …) ∈ ℛ P(x_{1},x_{1}^{-1},\ldots)\in{\cal{R}},

 | P ​ ( x 1, x 1 − 1, …) 2 k = P ⁡ ( x 1 2 k, x 1 − 2 k, …), P(x_{1},x_{1}^{-1},\ldots)^{2^{k}}\penalty\ =\penalty\ P(x_{1}^{2^{k}},x_{1}^{-2^{k}},\ldots), |  | (4) |

for any integer k ≥ 0 k\geq 0, and in particular that | P ​ ( x 1, x 1 − 1, …) 2 k | = | P | |P(x_{1},x_{1}^{-1},\ldots)^{2^{k}}|=|P|. Suppose first that the binary expansion of n n contains exactly two runs of 1s, separated by one or more 0s, say

 | n = 111 ⋯ 1 ⏞ m 1 ​ 00 ⋯ 0 ⏞ m 2 ​ 111 ⋯ 1 ⏞ m 3, m 1, m 2, m 3 ≥ 1, n\penalty\ =\penalty\ \overbrace{111\cdots 1}^{m_{1}}\overbrace{00\cdots 0}^{m_{2}}\overbrace{111\cdots 1}^{m_{3}},\quad m_{1},m_{2},m_{3}\geq 1, |  |

i.e.,

 | n = ( 2 m 1 − 1) ​ 2 m 2 + m 3 + ( 2 m 3 − 1), n\penalty\ =\penalty\ (2^{m_{1}}-1)2^{m_{2}+m_{3}}+(2^{m_{3}}-1), |  |

with ℒ ⁡ ( n) = [m 1, m 3] {\cal{L}}(n)=[m_{1},m_{3}]. Then

 | F n = ( F 2 m 1 − 1) 2 m 2 + m 3 ​ F 2 m 3 − 1 = P 2 m 2 + m 3 ​ Q ​ (say), F^{n}\penalty\ =\penalty\ (F^{2^{m_{1}}-1})^{2^{m_{2}+m_{3}}}F^{2^{m_{3}}-1}\penalty\ =\penalty\ P^{2^{m_{2}+m_{3}}}Q\mbox{\penalty\ (say)}, |  | (5) |

where P:= F 2 m 1 − 1 P:=F^{2^{m_{1}}-1}, Q:= F 2 m 3 − 1 Q:=F^{2^{m_{3}}-1}. Equation ( 5) states that F n F^{n} is a sum of copies of Q Q centered at the cells of of P 2 m 2 + m 3 P^{2^{m_{2}+m_{3}}}. By the Freshman’s Dream, P 2 m 2 + m 3 P^{2^{m_{2}+m_{3}}} is a polynomial in the variables x i ± 2 m 2 + m 3 x_{i}^{\pm 2^{m_{2}+m_{3}}}, so the cells in P 2 m 2 + m 3 P^{2^{m_{2}+m_{3}}} are separated by at least 2 m 2 + m 3 2^{m_{2}+m_{3}}. Also, | P 2 m 2 + m 3 | = | P | |P^{2^{m_{2}+m_{3}}}|=|P|. On the other hand, since ht ⁡ ( F) ≤ 1 \height(F)\leq 1, ht ⁡ ( Q) ≤ 2 m 3 − 1 \height(Q)\leq 2^{m_{3}}-1, and since

 | 2 ​ ( 2 m 3 − 1) + 1 < 2 m 3 + 1 ≤ 2 m 2 + m 3 2(2^{m_{3}}-1)+1\penalty\ <\penalty\ 2^{m_{3}+1}\penalty\ \leq\penalty\ 2^{m_{2}+m_{3}} |  |

the copies of Q Q in F n F^{n} are disjoint from each other, and so | F n | = | P | ​ | Q | |F^{n}|=|P||Q|, or in other words

 | a n ​ ( F) = a 2 m 1 − 1 ​ ( F) ​ a 2 m 3 − 1 ​ ( F) = ∏ i ∈ ℒ ⁡ ( n) a 2 i − 1 ​ ( F). a_{n}(F)\penalty\ =\penalty\ a_{2^{m_{1}}-1}(F)\penalty\ a_{2^{m_{3}}-1}(F)\penalty\ =\penalty\ \prod_{i\in{\cal{L}}(n)}a_{2^{i}-1}(F). |  |

It is straightforward to generalize this argument to the case when there are more than two runs of 1s in the binary expansion of n n, and to establish that for any n n,

 | a n ​ ( F) = ∏ i ∈ ℒ ⁡ ( n) a 2 i − 1 ​ ( F), a_{n}(F)\penalty\ =\penalty\ \prod_{i\in{\cal{L}}(n)}a_{2^{i}-1}(F), |  | (6) |

thus completing the proof. ∎

In several interesting cases the subsequence ( 3) satisfies a three-term linear recurrence, in which case there is also a simple recurrence for the run length transform.

###### Theorem 3.

Suppose the sequence [S n, n ≥ 0] [S_{n},n\geq 0] is defined by the recurrence S n + 1 = c 2 ​ S n + c 3 ​ S n − 1, n ≥ 1 S_{n+1}=c_{2}S_{n}+c_{3}S_{n-1},n\geq 1, with S 0 = 1 S_{0}=1, S 1 = c 1 S_{1}=c_{1}. Then its run length transform [T n, n ≥ 0] [T_{n},n\geq 0] satisfies the recurrence

 | T 2 ​ t = T t, T 4 ​ t + 1 = c 1 ​ T t, T 4 ​ t + 3 = c 2 ​ T 2 ​ t + 1 + c 3 ​ T t, T_{2t}=T_{t},\quad T_{4t+1}=c_{1}T_{t},\quad T_{4t+3}=c_{2}T_{2t+1}+c_{3}T_{t}, |  | (7) |

for t > 0 t>0, with T 0 = 1 T_{0}=1.

###### Proof.

T 2 ​ t = T t T_{2t}=T_{t} is immediate from the definition of the run length transform, since ℒ ⁡ ( 2 ​ n) = ℒ ⁡ ( n) {\cal{L}}(2n)={\cal{L}}(n). The binary expansion of 4 ​ t + 1 4t+1 ends in 01 01, so T 4 ​ t + 1 = T t ​ S 1 = c 1 ​ T t T_{4t+1}=T_{t}S_{1}=c_{1}T_{t}. If t = 2 k − 1 t=2^{k}-1 for some k ≥ 1 k\geq 1 then T 4 ​ t + 3 = S k + 2 = c 2 ​ S k + 1 + c 3 ​ S k T_{4t+3}=S_{k+2}=c_{2}S_{k+1}+c_{3}S_{k}, T 4 ​ t + 1 = c 1 ​ S k T_{4t+1}=c_{1}S_{k}, T 2 ​ t + 1 = S k + 1 T_{2t+1}=S_{k+1}, implying

 | T 4 ​ t + 3 = c 2 ​ T 2 ​ t + 1 + c 3 ​ T t. T_{4t+3}=c_{2}T_{2t+1}+c_{3}T_{t}. |  | (8) |

On the other hand, if t t has a zero in its binary expansion, say t = i ​.2 k + 1 + ( 2 k − 1), k ≥ 0 t=i.2^{k+1}+(2^{k}-1),k\geq 0, then T 4 ​ t + 3 = T i ​ S k + 2 = T i ​ ( c 2 ​ S k + 1 + c 3 ​ S k) T_{4t+3}=T_{i}S_{k+2}=T_{i}(c_{2}S_{k+1}+c_{3}S_{k}), T 4 ​ t + 1 = T i ​ c 1 ​ S k T_{4t+1}=T_{i}c_{1}S_{k}, T 2 ​ t + 1 = T i ​ S k + 1 T_{2t+1}=T_{i}S_{k+1}, and again ( 8) follows. ∎

## 4 Fredkin’s Replicator

The cellular automaton known as Fredkin’s Replicator [7, 8, 15] is the two-dimensional odd-rule CA defined by the Moore neighborhood F F shown in Fig. 1 (ix) and Eq. ( 2). (This is the eight-neighbor totalistic Rule 52428 in the Wolfram numbering scheme [17, 24, 26].)

[image: Refer to caption]

Figure 2: Generations 0 through 8 of the evolution of Fredkin’s Replicator. ON cells are black, OFF cells are white.

We study the evolution of this CA when it is started at generation 0 with a single ON cell at the origin. Generations 0 through 8 are shown in Fig. 2. The name of this CA comes from the fact that any configuration of ON cells will be replicated eight times at some later stage. For example, generation 1 is replicated eight times at generation 5. Although distinctive, the name is not especially appropriate, since by ( 4) any odd-rule CA has a similar replication property. Let a n ​ ( F) = a n a_{n}(F)=a_{n} denote the number of ON cells at the n n th generation. The initial values of a n a_{n} are shown in Table 1.

Table 1: Number of ON cells at n n th generation of Fredkin’s Replicator ( [A160239][2]).

 | n a n 0 𝟏 1 𝟖 2 − 3 8 𝟐𝟒 4 − 7 8 64 24 𝟏𝟏𝟐 8 − 15 8 64 64 192 24 192 112 𝟒𝟏𝟔 16 − 31 8 64 64 192 64 512 192 896 24 192 192 576 112 896 416 𝟏𝟕𝟐𝟖 32 − 63 8 64 64 192 64 512 192 896 64 512 512 1536 … \begin{array}[]{c|rrrrrrrrrrrrrrrr}n&&&&&&&a_{n}\\ \hline\cr 0&\mathbf{1}\\ 1&\mathbf{8}\\ 2-3&8&\mathbf{24}\\ 4-7&8&64&24&\mathbf{112}\\ 8-15&8&64&64&192&24&192&112&\mathbf{416}\\ 16-31&8&64&64&192&64&512&192&896&24&192&192&576&112&896&416&\mathbf{1728}\\ 32-63&8&64&64&192&64&512&192&896&64&512&512&1536&\ldots\end{array} |  |

Since ht ⁡ ( F) = 1 \height(F)=1, we know from Theorem 2 that [a n, n ≥ 0] [a_{n},n\geq 0] is the run length transform of the subsequence [b n = a 2 n − 1, n ≥ 0] = 1, 8, 24, 112, 416, 1728, … [b_{n}=a_{2^{n}-1},n\geq 0]=1,8,24,112,416,1728,\ldots (shown in bold in Table 1; it will turn out to be [A246030][4]). The main result of this section is the identification of this subsequence.

###### Theorem 4.

The sequence [b n, n ≥ 0] [b_{n},n\geq 0] satisfies the recurrence

 | b n + 1 = 2 ​ b n + 8 ​ b n − 1, w ​ i ​ t ​ h ​ b 0 = 1, b 1 = 8. b_{n+1}\penalty\ =\penalty\ 2b_{n}+8b_{n-1},\penalty\ {\mbox{w}ith\penalty\ }b_{0}=1,b_{1}=8. |  | (9) |

###### Proof.

Let G n:= F n G_{n}:=F^{n}, H n:= G 2 n − 1 = F 2 n − 1 H_{n}:=G_{2^{n}-1}=F^{2^{n}-1}. (Figure 2 shows G 0 = H 0 G_{0}=H_{0}, G 1 = H 1 G_{1}=H_{1}, G 2 G_{2}, G 3 = H 2 G_{3}=H_{2}, G 4 G_{4}, G 5 G_{5}, G 6 G_{6}, G 7 = H 3 G_{7}=H_{3}, and G 8 G_{8}.) By definition,

 | H n + 1 = F 2 n ​ H n, H_{n+1}\penalty\ =\penalty\ F^{2^{n}}H_{n}, |  | (10) |

and, from Theorem 1, a n = | G n | a_{n}=|G_{n}|, b n = | H n | b_{n}=|H_{n}|.

Since F F has diameter 3, the nonzero terms x i ​ y j x^{i}y^{j} in H n H_{n} satisfy

 | − ( 2 n − 1) ≤ i, j ≤ 2 n − 1, -(2^{n}-1)\penalty\ \leq i,j\leq 2^{n}-1, |  | (11) |

so we can write

 | H n = ∑ i = − ( 2 n − 1) 2 n − 1 ∑ j = − ( 2 n − 1) 2 n − 1 H n ​ ( i, j) ​ x i ​ y j, H_{n}\penalty\ =\penalty\ \sum_{i=-(2^{n}-1)}^{2^{n}-1}\,\sum_{j=-(2^{n}-1)}^{2^{n}-1}H_{n}(i,j)x^{i}y^{j}, |  | (12) |

where the coefficient H n ​ ( i, j) ∈ GF ⁡ ( 2) H_{n}(i,j)\in\GF(2) gives the state of the cell ( i, j) (i,j) at generation n n.

From ( 10) and ( 4), H n + 1 H_{n+1} is the sum (in ℛ {\cal{R}}) of eight copies of H n H_{n}, translated by 2 n 2^{n} in each of the N, NW, W, SW, S, SE, E, and NE directions. That is, for n ≥ 1 n\geq 1,

 | H n + 1 ​ ( i, j) \displaystyle H_{n+1}(i,j) | = H n ​ ( i, j − 2 n) + H n ​ ( i − 2 n, j − 2 n) + H n ​ ( i − 2 n, j) + H n ​ ( i − 2 n, j + 2 n) \displaystyle\penalty\ =\penalty\ H_{n}(i,j-2^{n})+H_{n}(i-2^{n},j-2^{n})+H_{n}(i-2^{n},j)+H_{n}(i-2^{n},j+2^{n}) |  |

 |  | + H n ​ ( i, j + 2 n) + H n ​ ( i + 2 n, j + 2 n) + H n ​ ( i + 2 n, j) + H n ​ ( i + 2 n, j − 2 n), \displaystyle\penalty\ \penalty\ +H_{n}(i,j+2^{n})+H_{n}(i+2^{n},j+2^{n})+H_{n}(i+2^{n},j)+H_{n}(i+2^{n},j-2^{n}), |  | (13) |

where we adopt the convention that H n ​ ( i, j) = 0 H_{n}(i,j)=0 unless i i and j j satisfy ( 11). Also,

 | H 0 ​ ( 0, 0) = 1, H 0 ​ ( i, j) = 0 ​ for ​ ( i, j) ≠ ( 0, 0), H_{0}(0,0)=1,\penalty\ \penalty\ H_{0}(i,j)=0\mbox{\penalty\ for\penalty\ }(i,j)\neq(0,0), |  | (14) |

and H 1 ​ ( i, j) = 0 H_{1}(i,j)=0 except for

 | H 1 ​ ( 0, 1) \displaystyle H_{1}(0,1) | = H 1 ​ ( − 1, 1) = H 1 ​ ( − 1, 0) = H 1 ​ ( − 1, − 1) \displaystyle=H_{1}(-1,1)=H_{1}(-1,0)=H_{1}(-1,-1) |  |

 |  | = H 1 ​ ( 0, − 1) = H 1 ​ ( 1, − 1) = H 1 ​ ( 1, 0) = H 1 ​ ( 1, 1) = 1. \displaystyle=H_{1}(0,-1)=H_{1}(1,-1)=H_{1}(1,0)=H_{1}(1,1)=1. |  | (15) |

By construction, H n H_{n} is preserved by the action of the dihedral group of order 8 (the symmetry group of the square), generated by the action of ( x, y) ↔ ( y, x) (x,y)\leftrightarrow(y,x) and ( x, y) ↔ ( 1 x, y) (x,y)\leftrightarrow(\frac{1}{x},y). We study H n H_{n} by breaking it up into the central cell, the four parts on the axes, and the four quadrants.

The central cell. The central cell H n ​ ( 0, 0) = 1 H_{n}(0,0)=1 if n = 0 n=0, and (as a consequence of the 8-fold symmetry) is 0 for n > 0 n>0. The axial parts. We define X n X_{n} ( n ≥ 1 n\geq 1) to be the portion of H n H_{n} that lies on the positive x x -axis, but normalized so that its center is at the origin:

 | X n:= 1 x 2 n − 1 ​ ∑ i = 1 2 n − 1 H n ​ ( i, 0) ​ x i. X_{n}\penalty\ :=\penalty\ \frac{1}{x^{2^{n-1}}}\,\sum_{i=1}^{2^{n}-1}H_{n}(i,0)x^{i}. |  | (16) |

For example, X 1 = 1, X 2 = 1 x + x, X 3 = 1 x 3 + 1 x + x + x 3 X_{1}=1,X_{2}=\frac{1}{x}+x,X_{3}=\frac{1}{x^{3}}+\frac{1}{x}+x+x^{3}. From ( 4) it follows by induction that, for n ≥ 2 n\geq 2,

 | X n = ∑ i = 0 2 n − 2 − 1 ( x − ( 2 ​ i + 1) + x 2 ​ i + 1) = ( 1 x + x) 2 n − 1 − 1. X_{n}\penalty\ =\penalty\ \sum_{i=0}^{2^{n-2}-1}\left(x^{-(2i+1)}+x^{2i+1}\right)\penalty\ =\penalty\ \left(\frac{1}{x}+x\right)^{2^{n-1}-1}. |  | (17) |

Similarly, the portion of H n H_{n} that lies on the negative x x -axis, normalized so that its center is at the origin, is

 | X ~ n:= x 2 n − 1 ​ ∑ i = 1 2 n − 1 H n ​ ( − i, 0) ​ x − i = ( 1 x + x) 2 n − 1 − 1 = X n. \widetilde{X}_{n}\penalty\ :=\penalty\ x^{2^{n-1}}\,\sum_{i=1}^{2^{n}-1}H_{n}(-i,0)x^{-i}\penalty\ =\penalty\ \left(\frac{1}{x}+x\right)^{2^{n-1}-1}\penalty\ =\penalty\ X_{n}. |  | (18) |

Likewise, the normalized portions of H n H_{n} on the positive and negative y y -axes are

 | Y n = Y n ~ = ( 1 y + y) 2 n − 1 − 1. Y_{n}\penalty\ =\penalty\ \widetilde{Y_{n}}\penalty\ =\penalty\ \left(\frac{1}{y}+y\right)^{2^{n-1}-1}. |  | (19) |

The four quadrants. Next, define I n \I_{n} for n ≥ 1 n\geq 1 to consist of the portion of H n H_{n} lying in the first quadrant, again normalized so that its center is at the origin:

 | I n:= 1 ( x ​ y) 2 n − 1 ​ ∑ i = 1 2 n − 1 ∑ j = 1 2 n − 1 H n ​ ( i, j) ​ x i ​ y j. \I_{n}\penalty\ :=\penalty\ \frac{1}{(xy)^{2^{n-1}}}\,\sum_{i=1}^{2^{n}-1}\sum_{j=1}^{2^{n}-1}H_{n}(i,j)x^{i}y^{j}. |  | (20) |

Similarly, we define

 | II n \displaystyle\II_{n} | := ( x y) 2 n − 1 ​ ∑ i = 1 2 n − 1 ∑ j = 1 2 n − 1 H n ​ ( − i, j) ​ x − i ​ y j, \displaystyle\penalty\ :=\penalty\ \left(\frac{x}{y}\right)^{2^{n-1}}\,\sum_{i=1}^{2^{n}-1}\sum_{j=1}^{2^{n}-1}H_{n}(-i,j)x^{-i}y^{j}, |  |

 | III n \displaystyle\III_{n} | := ( x ​ y) 2 n − 1 ​ ∑ i = 1 2 n − 1 ∑ j = 1 2 n − 1 H n ​ ( − i, − j) ​ x − i ​ y − j, \displaystyle\penalty\ :=\penalty\ (xy)^{2^{n-1}}\,\sum_{i=1}^{2^{n}-1}\sum_{j=1}^{2^{n}-1}H_{n}(-i,-j)x^{-i}y^{-j}, |  |

 | IV n \displaystyle\IV_{n} | := ( y x) 2 n − 1 ​ ∑ i = 1 2 n − 1 ∑ j = 1 2 n − 1 H n ​ ( i, − j) ​ x i ​ y − j. \displaystyle\penalty\ :=\penalty\ \left(\frac{y}{x}\right)^{2^{n-1}}\,\sum_{i=1}^{2^{n}-1}\sum_{j=1}^{2^{n}-1}H_{n}(i,-j)x^{i}y^{-j}. |  | (21) |

Assembling the parts, we see that, for n ≥ 1 n\geq 1, H n = H_{n}=

 | ( y / x) 2 n − 1 ​ II n + y 2 n − 1 ​ Y n + ( x ​ y) 2 n − 1 ​ I n + ( 1 / x) 2 n − 1 ​ X ~ n + 0 + x 2 n − 1 ​ X n + ( x ​ y) − 2 n − 1 ​ III n + y − 2 n − 1 ​ Y ~ n + ( x / y) 2 n − 1 ​ IV n \displaystyle\begin{matrix}&\penalty\ &(y/x)^{2^{n-1}}\II_{n}&+&y^{2^{n-1}}Y_{n}&+&(xy)^{2^{n-1}}\I_{n}\\ &+&(1/x)^{2^{n-1}}\penalty\ \widetilde{X}_{n}&+&0&+&\penalty\ \penalty\ x^{2^{n-1}}\penalty\ X_{n}\\ &+&(xy)^{-2^{n-1}}\III_{n}&+&y^{-2^{n-1}}\widetilde{Y}_{n}&+&(x/y)^{2^{n-1}}\IV_{n}\end{matrix} |  |

which we write as a matrix

 | H n = [II n Y n I n X ~ n 0 X n III n Y ~ n IV n], \displaystyle H_{n}\penalty\ =\penalty\ \begin{bmatrix}\II_{n}&Y_{n}&\I_{n}\\ \widetilde{X}_{n}&0&X_{n}\\ \III_{n}&\widetilde{Y}_{n}&\IV_{n}\end{bmatrix}, |  | (22) |

where it is to be understood that the blocks are to be shifted by the appropriate amounts (that is, the I n \I_{n} in the top right corner is to be multiplied by ( x ​ y) 2 n − 1 (xy)^{2^{n-1}}, and so on). By summing the eight translated copies of H n H_{n}, as in ( 4), we obtain

 | H n + 1 = [II n Y n I n + II n Y n I n + II n Y n I n X ~ n 0 X n + X ~ n 0 X n + X ~ n 0 X n II n + III n Y n + Y ~ n I n + III n + IV n Y ~ n II n + III n + IV n Y n + Y ~ n I n + IV n X ~ n 0 X n 0 X ~ n 0 X n II n + III n Y n + Y ~ n I n + II n + IV n Y n I n + II n + III n Y n + Y ~ n I n + IV n X ~ n 0 X n + X ~ n 0 X n + X ~ n 0 X n III n Y ~ n III n + IV n Y ~ n III n + IV n Y ~ n IV n]. \displaystyle H_{n+1}=\begin{bmatrix}\II_{n}&Y_{n}&\I_{n}+\II_{n}&Y_{n}&\I_{n}+\II_{n}&Y_{n}&\I_{n}\\ \widetilde{X}_{n}&0&X_{n}+\widetilde{X}_{n}&0&X_{n}+\widetilde{X}_{n}&0&X_{n}\\ \II_{n}+\III_{n}&Y_{n}+\widetilde{Y}_{n}&\I_{n}+\III_{n}+\IV_{n}&\widetilde{Y}_{n}&\II_{n}+\III_{n}+\IV_{n}&Y_{n}+\widetilde{Y}_{n}&\I_{n}+\IV_{n}\\ \widetilde{X}_{n}&0&X_{n}&0&\widetilde{X}_{n}&0&X_{n}\\ \II_{n}+\III_{n}&Y_{n}+\widetilde{Y}_{n}&\I_{n}+\II_{n}+\IV_{n}&Y_{n}&\I_{n}+\II_{n}+\III_{n}&Y_{n}+\widetilde{Y}_{n}&\I_{n}+\IV_{n}\\ \widetilde{X}_{n}&0&X_{n}+\widetilde{X}_{n}&0&X_{n}+\widetilde{X}_{n}&0&X_{n}\\ \III_{n}&\widetilde{Y}_{n}&\III_{n}+\IV_{n}&\widetilde{Y}_{n}&\III_{n}+\IV_{n}&\widetilde{Y}_{n}&\IV_{n}\end{bmatrix}. |  | (23) |

Using ( 18) and ( 19), we have

 | II n + 1 = [II n Y n I n + II n X n 0 0 II n + III n 0 I n + III n + IV n], I n + 1 = [I n + II n Y n I n 0 0 X n II n + III n + IV n 0 I n + IV n], \displaystyle\II_{n+1}=\begin{bmatrix}\II_{n}&Y_{n}&\I_{n}+\II_{n}\\ X_{n}&0&0\\ \II_{n}+\III_{n}&0&\I_{n}+\III_{n}+\IV_{n}\end{bmatrix},\penalty\ \penalty\ \I_{n+1}=\begin{bmatrix}\I_{n}+\II_{n}&Y_{n}&\I_{n}\\ 0&0&X_{n}\\ \II_{n}+\III_{n}+\IV_{n}&0&\I_{n}+\IV_{n}\end{bmatrix}, |  | (24) |

 | III n + 1 = [II n + III n 0 I n + II n + IV n X n 0 0 III n Y n III n + IV n], IV n + 1 = [I n + II n + III n 0 I n + IV n 0 0 X n III n + IV n Y n IV n], \displaystyle\III_{n+1}=\begin{bmatrix}\II_{n}+\III_{n}&0&\I_{n}+\II_{n}+\IV_{n}\\ X_{n}&0&0\\ \III_{n}&Y_{n}&\III_{n}+\IV_{n}\end{bmatrix},\penalty\ \penalty\ \IV_{n+1}=\begin{bmatrix}\I_{n}+\II_{n}+\III_{n}&0&\I_{n}+\IV_{n}\\ 0&0&X_{n}\\ \III_{n}+\IV_{n}&Y_{n}&\IV_{n}\end{bmatrix}, |  | (25) |

By adding these four matrices we find that I n + 1 + II n + 1 + III n + 1 + IV n + 1 = 0 \I_{n+1}+\II_{n+1}+\III_{n+1}+\IV_{n+1}=0 for n ≥ 1 n\geq 1. This identity is also true for n = 0 n=0, and we conclude that

 | I n + II n + III n + IV n = 0, n ≥ 1, \I_{n}+\II_{n}+\III_{n}+\IV_{n}=0,\quad n\geq 1, |  | (26) |

and so

 | II n + 1 = [II n Y n I n + II n X n 0 0 II n + III n 0 II n], I n + 1 = [I n + II n Y n I n 0 0 X n I n 0 I n + IV n], \displaystyle\II_{n+1}=\begin{bmatrix}\II_{n}&Y_{n}&\I_{n}+\II_{n}\\ X_{n}&0&0\\ \II_{n}+\III_{n}&0&\II_{n}\end{bmatrix},\penalty\ \penalty\ \I_{n+1}=\begin{bmatrix}\I_{n}+\II_{n}&Y_{n}&\I_{n}\\ 0&0&X_{n}\\ \I_{n}&0&\I_{n}+\IV_{n}\end{bmatrix},\penalty\ \penalty\  |  | (27) |

etc., and finally that, for n ≥ 1 n\geq 1,

 | H n + 1 = [II n Y n I n + II n Y n I n + II n Y n I n X n 0 0 0 0 0 X n II n + III n 0 II n Y n I n 0 I n + IV n X n 0 X n 0 X n 0 X n II n + III n 0 III n Y n IV n 0 I n + IV n X n 0 0 0 0 0 X n III n Y n III n + IV n Y n III n + IV n Y n IV n]. \displaystyle H_{n+1}=\begin{bmatrix}\II_{n}&Y_{n}&\I_{n}+\II_{n}&Y_{n}&\I_{n}+\II_{n}&Y_{n}&\I_{n}\\ X_{n}&0&0&0&0&0&X_{n}\\ \II_{n}+\III_{n}&0&\II_{n}&Y_{n}&\I_{n}&0&\I_{n}+\IV_{n}\\ X_{n}&0&X_{n}&0&X_{n}&0&X_{n}\\ \II_{n}+\III_{n}&0&\III_{n}&Y_{n}&\IV_{n}&0&\I_{n}+\IV_{n}\\ X_{n}&0&0&0&0&0&X_{n}\\ \III_{n}&Y_{n}&\III_{n}+\IV_{n}&Y_{n}&\III_{n}+\IV_{n}&Y_{n}&\IV_{n}\end{bmatrix}. |  | (28) |

In ( 28) we see that H n + 1 H_{n+1} contains a copy of H n H_{n} at its center. The four corner blocks together with two copies each of X n X_{n} and Y n Y_{n} form another, “deconstructed”, copy of H n H_{n}.

Suppose n ≥ 2 n\geq 2, and consider the blocks [I n + II n ⁡ Y n ​ I n + II n ⁡ Y n] [\I_{n}+\II_{n}\penalty\ Y_{n}\penalty\ \I_{n}+\II_{n}\penalty\ Y_{n}] in the top row of ( 28). Using ( 27) these blocks can be expanded to give

 | [I n − 1 0 II n − 1 Y n − 1 I n − 1 0 II n − 1 Y n − 1 X n − 1 0 X n − 1 0 X n − 1 0 X n − 1 0 IV n − 1 0 III n − 1 Y n − 1 IV n − 1 0 III n − 1 Y n − 1]. \displaystyle\begin{bmatrix}\I_{n-1}&0&\II_{n-1}&Y_{n-1}&\I_{n-1}&0&\II_{n-1}&Y_{n-1}\\ X_{n-1}&0&X_{n-1}&0&X_{n-1}&0&X_{n-1}&0\\ \IV_{n-1}&0&\III_{n-1}&Y_{n-1}&\IV_{n-1}&0&\III_{n-1}&Y_{n-1}\end{bmatrix}. |  | (29) |

The central three columns (columns 3, 4, and 5) give a copy of H n − 1 H_{n-1}, and columns 7, 8, and 1, in that order, give another copy. We get two further copies of H n − 1 H_{n-1} from the analogous blocks in each of the other three sides of ( 28), so in total H n + 1 H_{n+1} contains as many ON cells as are in two copies of H n H_{n} plus eight copies of H n − 2 H_{n-2}. This implies ( 9) for n ≥ 2 n\geq 2. Equation ( 9) is certainly true for n = 1 n=1, so this completes the proof of the theorem. ∎

[image: Refer to caption]

Figure 3: Dissection of H 4 H_{4} into pieces that can be reassembled to give two copies of H 3 H_{3} and eight copies of H 2 H_{2}, illustrating ( 9) in the case n = 3 n=3.

The characteristic polynomial of ( 9) is x 2 − 2 ​ x − 8 = ( x + 2) ​ ( x − 4) x^{2}-2x-8=(x+2)(x-4), and it follows that

 | b n = 5.4 n + ( − 2) n + 1 3, n ≥ 0. b_{n}\penalty\ =\penalty\ \frac{5.4^{n}+(-2)^{n+1}}{3},\penalty\ n\geq 0. |  | (30) |

In geometric terms, the proof of Theorem 4 shows that H n + 1 H_{n+1} can be dissected into pieces that can be reassembled to give two copies of H n H_{n} and eight copies of H n − 1 H_{n-1}. Figure 3 shows this dissection in the case of H 4 H_{4}. The central dashed square (colored red in the online version) encloses a copy of H 3 H_{3}. The smaller dashed squares on the four sides (colored blue) enclose copies of H 2 H_{2}. The four pairs of vertical parallel lines (colored green) enclose copies of Y 3 Y_{3}, and the four pairs of horizontal parallel lines (also green) enclose copies of X 3 X_{3}. The four corners (outside the parallel lines) are, reading counter-clockwise from the top right corner, respectively I 3 \I_{3}, II 3 \II_{3}, III 3 \III_{3}, and IV 3 \IV_{3}, and combine with two copies each of X 3 X_{3} and Y 3 Y_{3} to give the second copy of H 3 H_{3}. Along the top edge, the figure is divided into seven pieces, as in the top row of ( 28). By taking the fifth, sixth, and third pieces in that order gives another copy of H 2 H_{2}, and three further copies are obtained from the other edges of the figure.

From Theorem 3 and ( 9), we see that a n a_{n} is given by the recurrence

 | a 2 ​ t = a t, a 4 ​ t + 1 = 8 ​ a t, a 4 ​ t + 3 = 2 ​ a 2 ​ t + 1 + 8 ​ a t, a_{2t}=a_{t},\quad a_{4t+1}=8a_{t},\quad a_{4t+3}=2a_{2t+1}+8a_{t}, |  | (31) |

for t > 0 t>0, with a 0 = 1 a_{0}=1, as conjectured by Hrothgar [10].

## 5 The centered von Neumann neighborhood

In this section we analyze the two-dimensional odd-rule CA defined by the five-celled neighborhood

 | F = 1 x + 1 + x + 1 y + y ∈ ℛ = GF ⁡ ( 2) ​ [x, x − 1, y, y − 1] F\penalty\ =\penalty\ \frac{1}{x}+1+x+\frac{1}{y}+y\penalty\ \in\penalty\ {\cal{R}}=\GF(2)[x,x^{-1},y,y^{-1}] |  | (32) |

shown in Fig. 1 (vi), and consisting of the von Neumann neighborhood together with its center. (This is the five-neighbor totalistic Rule 614.) We use the same notation as in the previous section, except that now F F is defined by ( 32) instead of ( 2).

The initial values of [a n, n ≥ 0] [a_{n},n\geq 0] are

 | 𝟏, 𝟓, 5, 𝟏𝟕, 5, 25, 17, 𝟔𝟏, 5, 25, 25, 85, 17, 85, 61, 𝟐𝟏𝟕, … \mathbf{1},\mathbf{5},5,\mathbf{17},5,25,17,\mathbf{61},5,25,25,85,17,85,61,\mathbf{217},\ldots |  |

( [A072272][5]), which we know from Theorem 2 is the run length transform of the subsequence [b n, n ≥ 0] = 1, 5, 17, 61, 217, 773, 2753, … [b_{n},n\geq 0]=1,5,17,61,217,773,2753,\ldots, shown in bold ( [A007483][6]). Generations 0 through 8 are shown in Fig. 4, and Figs. 5 and 6 show generation 31.

[image: Refer to caption]

Figure 4: Generations 0 through 8 of the odd-rule CA defined by the centered von Neumann neighborhood. Generations 0, 1, 3, 7 show H 0 H_{0}, H 1 H_{1}, H 2 H_{2}, H 3 H_{3} respectively.

[image: Refer to caption]

Figure 5: Generation 31 ( H 5 H_{5}), showing dissection into central copy of H 3 H_{3} (inside red dashed line) and four “haystacks” N 5 N_{5}, W 5 W_{5}, S 5 S_{5}, E 5 E_{5} (each enclosed by blue dashed line).

[image: Refer to caption]

Figure 6: Another view of generation 31 ( H 5 H_{5}) showing dissection of haystack N 5 N_{5} into three smaller haystacks N 4 N_{4}, W 4 W_{4}, E 4 E_{4} (each enclosed in green dashed line) and two still smaller haystacks N 3 N_{3} and S 3 S_{3} (inside blue dashed lines).

###### Theorem 5.

The sequence [b n, n ≥ 0] [b_{n},n\geq 0] satisfies the recurrence

 | b n + 1 = 3 ​ b n + 2 ​ b n − 1, with ​ b 0 = 1, b 1 = 5. b_{n+1}\penalty\ =\penalty\ 3b_{n}+2b_{n-1},\penalty\ \mbox{\penalty\ with\penalty\ }b_{0}=1,b_{1}=5. |  | (33) |

###### Proof.

As in the proof of Theorem 4, H n = F 2 n − 1 H_{n}=F^{2^{n}-1}, b n = | H n | b_{n}=|H_{n}|, and again H n H_{n} is preserved under the action of a dihedral group of order 8. The first step in the proof is to show that for n ≥ 2 n\geq 2, H n H_{n} can be dissected into a central copy of H n − 2 H_{n-2} and four disjoint pentagonal or “haystack”-shaped regions (see Fig. 5 for the dissection of H 5 H_{5}). The four haystacks in H n H_{n} will be denoted by N n N_{n}, W n W_{n}, S n S_{n}, and E n E_{n}, according to the direction in which they point (a precise definition will be given below). They are equivalent under the action of the dihedral group. Algebraically, we will show that

 | H n = H n − 2 + y 2 n − 1 ​ N n + x − 2 n − 1 ​ W n + y − 2 n − 1 ​ S n + x 2 n − 1 ​ E n, H_{n}\penalty\ =\penalty\ H_{n-2}+y^{2^{n-1}}N_{n}+x^{-2^{n-1}}W_{n}+y^{-2^{n-1}}S_{n}+x^{2^{n-1}}E_{n}, |  | (34) |

where the five polynomials on the right are disjoint (i.e., have no monomials in common with each other).

Once we have established ( 34), the second step in the proof will be to show that each haystack can be dissected into five smaller haystacks (see Fig. 6 for the dissection of N 5 N_{5}). In particular, we will show that for n ≥ 3 n\geq 3,

 | N n = y 2 n − 2 ​ N n − 1 + x − 2 n − 2 ​ W n − 1 + x 2 n − 2 ​ E n − 1 + N n − 2 + y − 2 n − 3 ​ S n − 2, N_{n}\penalty\ =\penalty\ y^{2^{n-2}}N_{n-1}+x^{-2^{n-2}}W_{n-1}+x^{2^{n-2}}E_{n-1}+N_{n-2}+y^{-2^{n-3}}S_{n-2}, |  | (35) |

where again the polynomials on the right are disjoint. Let ν n:= | N n | = | W n | = | S n | = | E n | \nu_{n}:=|N_{n}|=|W_{n}|=|S_{n}|=|E_{n}|. Then ( 35) implies ν n = 3 ​ ν n − 1 + 2 ​ ν n − 2 \nu_{n}=3\nu_{n-1}+2\nu_{n-2}. From ( 34) we have b n = b n − 2 + 4 ​ ν n b_{n}=b_{n-2}+4\nu_{n}, so

 | b n + 1 − 3 ​ b n − 2 ​ b n − 1 = b n − 1 − 3 ​ b n − 2 − 2 ​ b n − 3 = ⋯ = either ​ b 3 − 3 ​ b 2 − 2 ​ b 1 ​ or ​ b 2 − 3 ​ b 1 − 2 ​ b 0, b_{n+1}-3b_{n}-2b_{n-1}=b_{n-1}-3b_{n-2}-2b_{n-3}=\cdots=\mbox{\penalty\ either\penalty\ }b_{3}-3b_{2}-2b_{1}\mbox{\penalty\ or\penalty\ }b_{2}-3b_{1}-2b_{0}, |  |

and each of the last two expressions evaluates to zero. This will complete the proof of ( 33). It is worth remarking that these dissections are of a different nature from the dissection in the previous section. There it was necessary to make some non-obvious cuts through the contiguous blocks of ON cells, as shown by the parallel (green) lines in the corners of Fig. 3. In contrast, in the present proof, the dissections are carried out by “tearing” along the obvious “perforations”, rather like tearing apart a block of postage stamps.

Now to the details. It follows from the definition (see the sequence of successive states in Fig. 4) that H n H_{n} is a diamond-shaped configuration with extreme points ( ± ( 2 n − 1), 0) (\pm(2^{n}-1),0), ( 0, ± ( 2 n − 1)) (0,\pm(2^{n}-1)). Also, for n ≥ 2 n\geq 2, H n H_{n} contains a copy of H n − 2 H_{n-2} at its center, surrounded by a layer, at least one cell wide, of OFF cells. This follows from the identity

 | H n − H n − 2 = F 2 n − 1 − F 2 n − 2 − 1 = H n − 2 ​ ( 1 + H 2 2 n − 2), H_{n}-H_{n-2}\penalty\ =\penalty\ F^{2^{n}-1}-F^{2^{n-2}-1}\penalty\ =\penalty\ H_{n-2}(1+H_{2}^{2^{n-2}}), |  |

upon checking that the right-hand side contains no monomials x i ​ y j x^{i}y^{j} with | i | + | j | ≤ 2 n − 2 |i|+|j|\leq 2^{n-2}. The buffer layer of OFF cells around the central H n − 2 H_{n-2} consists of the cells x i ​ y j x^{i}y^{j} with | i | + | j | = 2 n − 2 |i|+|j|=2^{n-2}.

We define the n n th North haystack to be

 | N n:= H n − 2 ​ T N 2 n − 2, n ≥ 2, N_{n}\penalty\ :=\penalty\ H_{n-2}\,T_{N}^{2^{n-2}},\penalty\ n\geq 2, |  | (36) |

where T N:= 1 / x + 1 + x + y T_{N}:=1/x+1+x+y is the four-celled North-pointing triangle shown in Fig. 1 (iii). Similarly, the West, South, and East haystacks are

 | W n:= H n − 2 ​ T W 2 n − 2, S n:= H n − 2 ​ T S 2 n − 2, E n:= H n − 2 ​ T E 2 n − 2, W_{n}\penalty\ :=\penalty\ H_{n-2}\,T_{W}^{2^{n-2}},\penalty\ S_{n}\penalty\ :=\penalty\ H_{n-2}\,T_{S}^{2^{n-2}},\penalty\ E_{n}\penalty\ :=\penalty\ H_{n-2}\,T_{E}^{2^{n-2}}, |  | (37) |

where T W:= 1 / x + 1 / y + 1 + y T_{W}:=1/x+1/y+1+y is a West-pointing version of T N T_{N}, and similarly for T S T_{S} and T E T_{E}. (The simple expressions in ( 36) and ( 37) were guessed by computing the actual haystacks in H 3 H_{3} to H 6 H_{6} and using Maple to factor them in ℛ {\cal{R}}.) The haystack N n N_{n} has the property that all its cells are on or inside the convex hull of the five cells x i ​ y j x^{i}y^{j} with ( i, j) (i,j) equal to

 | ( 0, 2 n − 1 − 1), ( − 2 n − 1 + 1, 0), ( − 2 n − 2, − 2 n − 2 + 1), ( 2 n − 2 − 2 n − 2 + 1), ( − 2 n − 1 + 1, 0). (0,2^{n-1}-1),(-2^{n-1}+1,0),(-2^{n-2},-2^{n-2}+1),(2^{n-2}-2^{n-2}+1),(-2^{n-1}+1,0). |  | (38) |

To see this, consider what happens to N n N_{n} one generation later: it becomes

 | F ​ N n = ( F ​ T N) 2 n − 2, FN_{n}\penalty\ =\penalty\ (FT_{N})^{2^{n-2}}, |  | (39) |

using the Freshman’s Dream ( 4), where F ​ T n FT_{n} is the six-celled configuration

 | y 2 + 1 x 2 + 1 x ​ y + 1 y + x y + x 2. y^{2}+\frac{1}{x^{2}}+\frac{1}{xy}+\frac{1}{y}+\frac{x}{y}+x^{2}. |  |

From ( 39), F ​ N n FN_{n} is this configuration with the cells moved 2 n − 2 2^{n-2} steps apart, and the cells ( 38) lie just inside it.

Note that the point ( 0, 0) (0,0) is in the interior of N n N_{n} at the intersection of the vertical line through the apex and the horizontal line joining the most Western and Eastern points. The powers of x x and y y in ( 34) and ( 35) are needed in order to translate the haystacks into their correct positions. Since we now know the boundaries of all the terms on the right side of ( 34), we can check that these five polynomials are indeed disjoint. We must still check that ( 34) is an identity. Using the Freshman’s Dream, this reduces to checking the identity

 | H 2 = 1 + y 2 ​ T N + x − 2 ​ T W + y − 2 ​ T S + x 2 ​ T E, H_{2}\penalty\ =\penalty\ 1+y^{2}T_{N}+x^{-2}T_{W}+y^{-2}T_{S}+x^{2}T_{E}, |  |

which is true. This completes the proof that ( 34) is a proper dissection of H n H_{n}. The correctness of the dissection ( 35) is verified in a similar way; we omit the details. ∎

## 6 Other Cellular Automata

### 6.1 The 256 one-dimensional rules

There are 256 possible CAs based on the one-dimensional three-celled neighborhood shown in Fig. 1 (i). These are the CAs labeled Rule 0 through Rule 255 in the Wolfram numbering scheme [17, 24, 26]. As usual we assume the automaton is started with a single ON cell, and let a n a_{n} denote the number of ON cells after n n generations. Illustrations of the initial generations of all 256 CAs are shown on pages 54–56 of [26]. Many of these sequences were analyzed in [23]; see also [22]. If we eliminate those in which some a n a_{n} is infinite, or the sequence [a n, n ≥ 0] [a_{n},n\geq 0] is trivial (essentially linear), or is a duplicate of one of the others, we are left with just seven sequences:

- •

Rule 18 (or Rule 90; Rule 182 is very similar): a n = 2 wt ⁡ ( n) a_{n}=2^{\wt(n)} (Gould’s sequence [A001316][7]), where wt ⁡ ( n) \wt(n) is the number of 1s in the binary expansion of n n. This is the run length transform of the powers of 2.

- •

Rule 22: a n = 2 wt ⁡ ( n) a_{n}=2^{\wt(n)} if n n even, 3.2 wt ⁡ ( n) − 1 3.2^{\wt(n)-1} if n n odd ( [A071044][8]).

- •

Rule 30: The behavior appears chaotic, even when started with a single ON cell [22, 26]. The sequence, [A070952][9], has roughly linear growth, but it seems likely that there is no simpler way to obtain it than by its definition.

- •

Rule 62: a n + 7 = a n + 4 + a n + 3 − a n a_{n+7}=a_{n+4}+a_{n+3}-a_{n} with initial terms 1, 3, 3, 6, 5, 8, 9 1,3,3,6,5,8,9 ( [A071047][10]).

- •

Rule 110: Although the initial behavior is chaotic, it is an astonishing fact, pointed out by Wolfram [26, p. 39], that after about three thousand terms all the irregularities disappear. By using the Salvy-Zimmermann gfun package in Maple [18], we find that the sequence, [A071049][11], satisfies a linear recurrence of order 469: for n ≥ 2854 n\geq 2854,

 | a n + 469 = − a n + 453 + a n + 256 + a n + 240 + a n + 229 + a n + 213 − a n + 16 − a n. a_{n+469}\penalty\ =\penalty\ -a_{n+453}+a_{n+256}+a_{n+240}+a_{n+229}+a_{n+213}-a_{n+16}-a_{n}. |  | (40) |

This recurrence is far nicer than it initially appears: the coefficients are palindromic, and its characteristic polynomial is the product of 25 irreducible factors.

- •

Rule 126: a n = 2 wt ⁡ ( n) + 1 a_{n}=2^{\wt(n)+1}, except we must subtract 1 if n = 2 k − 1 n=2^{k}-1 for some k k ( [A071051][12]).

- •

Rule 150: This is the odd-rule CA defined by the three-celled neighborhood. The sequence [a n, n ≥ 0] [a_{n},n\geq 0] ( [A071053][13]) was analyzed by Wolfram [23] (see also [9], [19]). In the notation of the present paper [a n, n ≥ 0] [a_{n},n\geq 0] is the run length transform of the Jacobstahl sequence [A001045][14]. Theorems 1 and 2 were suggested by reading Sillke’s analysis [19].

### 6.2 Other odd-rule CAs

In this section we discuss the odd-rule CAs defined by the height-one neighborhoods in Fig. 1. (The height-two neighborhood of Fig. 1 (iv) is discussed in the last section of the paper.) Table 2 summarizes the results. The first column specifies the neighborhood F F in Fig. 1, a n ​ ( F) a_{n}(F) is the number of ON cells at generation n n, b n ​ ( F) b_{n}(F) denotes the sequence of which a n ​ ( F) a_{n}(F) is the run length transform, and the fourth column gives a generating function (g.f.) for b n ​ ( f) b_{n}(f). For Fig. (iii), Fib n + 2 \Fib_{n+2} denotes a Fibonacci number. The g.f. for (vii), found by Doron Zeilberger [3], is

 | ( 1 + 2 ​ x) ​ ( 1 + x − x 2 + x 3 + 2 ​ x 5) 1 − 3 ​ x − 3 ​ x 2 + x 3 + 6 ​ x 4 − 10 ​ x 5 + 8 ​ x 6 − 8 ​ x 7. \frac{\left(1+2\,x\right)\left(1+x-x^{2}+x^{3}+2\,{x}^{5}\right)}{1-3\,x-3\,{x}^{2}+{x}^{3}+6\,x^{4}-10\,x^{5}+8\,{x}^{6}-8\,{x}^{7}}\,. |  | (41) |

An expanded version of this table, analyzing all the sequences arising from odd-rule CAs defined by height-one neighborhoods on the square grid, will be published elsewhere [4].

Table 2: Odd-rule CAs defined by height-1 neighborhoods F F in Fig. 1.

 | F a n ​ ( F) b n ​ ( F) g.f. Notes (i) A ​ 071053 ¯ A ​ 001045 ¯ 1 + 2 ​ x 1 − x − 2 ​ x 2 Rule 150, § ​ 6.1 (ii) A ​ 048883 ¯ A ​ 000244 ¯ 1 1 − 3 ​ x a n = 3 wt ⁡ ( n) (iii) A ​ 253064 ¯ A ​ 087206 ¯ 1 + 2 ​ x 1 − 2 ​ x − 4 ​ x 2 b n = 2 n ​ Fib n + 2 (v) A ​ 102376 ¯ A ​ 000302 ¯ 1 1 − 4 ​ x a n = 4 wt ⁡ ( n) (vi) A ​ 072272 ¯ A ​ 007483 ¯ 1 + 2 ​ x 1 − 3 ​ x − 2 ​ x 2 § ​ 5 (vii) A ​ 253069 ¯ A ​ 253070 ¯ ( 41) (viii) A ​ 246039 ¯ A ​ 246038 ¯ ( 1 + 2 ​ x) ​ ( 1 + 2 ​ x + 4 ​ x 2) 1 − 3 ​ x − 8 ​ x 3 − 8 ​ x 4 (ix) A ​ 160239 ¯ A ​ 246030 ¯ 1 + 6 ​ x 1 − 2 ​ x − 8 ​ x 2 Fredkin Replicator, § ​ 4 (x) A ​ 246035 ¯ A ​ 139818 ¯ 1 + 6 ​ x − 8 ​ x 2 ( 1 − x) ​ ( 1 + 2 ​ x) ​ ( 1 − 4 ​ x) Squares of entries from (i) \begin{array}[]{|c|c|c|c|c|}\hline\cr F&a_{n}(F)&b_{n}(F)&\mbox{g.f.}&\mbox{Notes}\\ \hline\cr\mbox{(i)}&\hrefhttp://oeis.org/A071053&\hrefhttp://oeis.org/A001045&\frac{1+2x}{1-x-2x^{2}}&\mbox{Rule\penalty\ 150},\penalty\ \lx@sectionsign\ref{Sec61}\\ \mbox{(ii)}&\hrefhttp://oeis.org/A048883&\hrefhttp://oeis.org/A000244&\frac{1}{1-3x}&a_{n}=3^{\wt(n)}\\ \mbox{(iii)}&\hrefhttp://oeis.org/A253064&\hrefhttp://oeis.org/A087206&\frac{1+2x}{1-2x-4x^{2}}&b_{n}=2^{n}\Fib_{n+2}\\ \mbox{(v)}&\hrefhttp://oeis.org/A102376&\hrefhttp://oeis.org/A000302&\frac{1}{1-4x}&a_{n}=4^{\wt(n)}\\ \mbox{(vi)}&\hrefhttp://oeis.org/A072272&\hrefhttp://oeis.org/A007483&\frac{1+2x}{1-3x-2x^{2}}&\lx@sectionsign\ref{SecVN}\\ \mbox{(vii)}&\hrefhttp://oeis.org/A253069&\hrefhttp://oeis.org/A253070&(\ref{Eqviigf})&\\ \mbox{(viii)}&\hrefhttp://oeis.org/A246039&\hrefhttp://oeis.org/A246038&\frac{(1+2x)(1+2x+4x^{2})}{1-3x-8x^{3}-8x^{4}}&\\ \mbox{(ix)}&\hrefhttp://oeis.org/A160239&\hrefhttp://oeis.org/A246030&\frac{1+6x}{1-2x-8x^{2}}&\mbox{Fredkin\penalty\ Replicator},\penalty\ \lx@sectionsign\ref{SecFR}\\ \mbox{(x)}&\hrefhttp://oeis.org/A246035&\hrefhttp://oeis.org/A139818&\frac{1+6x-8x^{2}}{(1-x)(1+2x)(1-4x)}&\mbox{Squares\penalty\ of\penalty\ entries\penalty\ from\penalty\ (i)}\\ \hline\cr\end{array} |  |

### 6.3 Further two-dimensional CAs

If we drop the “odd-rule” definition, the number of CAs grows astronomically—there are 2 512 2^{512} based on the Moore neighborhood alone. Pages 171–175 of [26] show many examples of the subset of “totalistic” rules, in which the next state of a cell depends only on its present state and the total number of ON cells surrounding it. All of these are potential sources of sequences. In a few cases it is possible to analyze the sequence, but usually it seems that no formula or recurrence exists. In this section we give three examples: one that can be analyzed, one that might be analyzable with further research, and one (typical of the majority) where the state diagrams are aesthetically appealing but finding a formula seems hopeless. All three are totalistic rules, the first two being based on the von Neumann neighborhood (Fig. 1 (v)), and the third on the Moore neighborhood (Fig. 1 (ix)).

The first example is the Rule 750 automaton, in which an OFF cell turns ON if an odd number of its four neighbors are ON, and once a cell is ON it stays ON [26, p. 925]. This CA is a hybrid of the “odd-rule” CAs studied above and the “once a cell is ON it stays ON” rules studied in [2]. Here it is convenient to call the initial ON cell generation 1 (rather than 0). The numbers of ON cells in the first few generations ( [A169707][15]) are given in Table 3.

Table 3: Number of ON cells at n n th generation of CA defined by Rule 750.

 | n a n 1 1 2 − 3 5 9 4 − 7 21 25 37 57 8 − 15 85 89 101 121 149 169 213 281 16 − 31 341 345 357 377 405 425 469 … \begin{array}[]{c|rrrrrrrrr}n&&&a_{n}\\ \hline\cr 1&1\\ 2-3&5&9\\ 4-7&21&25&37&57\\ 8-15&85&89&101&121&149&169&213&281\\ 16-31&341&345&357&377&405&425&469&\ldots\end{array} |  |

The evolution of this CA is similar to several that were studied in [2]: at generation 2 k 2^{k}, for k ≥ 2 k\geq 2, the structure is enclosed in a diamond-shaped region, which is saturated in the sense that no additional interior cells can ever be turned ON, and contains a 2 k = ( 4 k + 1 − 1) / 3 a_{2^{k}}=(4^{k+1}-1)/3 ON cells. Then in generations 2 k + 1 2^{k}+1 to 2 k + 1 − 1 2^{k+1}-1, the structure grows outwards from the four vertices of the diamond, and the first half of the growth that follows generation 2 k 2^{k} is the same as the the growth that followed generation 2 k − 1 2^{k-1}. Figure 7 shows generation 20 = 2 4 + 4 20=2^{4}+4, where we can see that 16 cells have grown out of each vertex. Pictures of generations 16 = 2 3 + 4 16=2^{3}+4 and 36 = 2 5 + 4 36=2^{5}+4 show exactly the same growth from the vertices (although with different numbers of ON cells in the central diamond).

[image: Refer to caption]

Figure 7: Generation 20 of CA defined by Rule 750, showing 341 + 4 ​ ( 1 + 3 + 5 + 7) = 405 341+4(1+3+5+7)=405 ON cells, illustrating ( 43).

The successive numbers of ON cells added to a vertex in the generations from 2 k 2^{k} to 2 k + 1 − 1 2^{k+1}-1 are 0, 1, 3, 5, 7, 5, 11, 17, 15, 5, … 0,1,3,5,7,5,11,17,15,5,\ldots, which form the initial terms v 0, v 1, v 2, … v_{0},v_{1},v_{2},\ldots of a sequence ( [A151548][16]) encountered in [2]. The v i v_{i} have generating function

 | x 1 + x + 4 ​ x 2 ​ ∏ r = 1 ∞ ( 1 + x 2 r − 1 + 2 ​ x 2 r). \frac{x}{1+x}\penalty\ +\penalty\ 4\,x^{2}\,\prod_{r=1}^{\infty}(1+x^{2^{r}-1}+2x^{2^{r}}). |  | (42) |

Then, for k ≥ 0 k\geq 0 and 0 ≤ m < 2 k 0\leq m<2^{k}, we have

 | a 2 k + m = 4 k + 1 − 1 3 + 4 ​ ∑ i = 0 m v i. a_{2^{k}+m}\penalty\ =\penalty\ \frac{4^{k+1}-1}{3}\penalty\ +\penalty\ 4\sum_{i=0}^{m}v_{i}. |  | (43) |

Bearing in mind the warning in the first sentence of this paper, we must admit that we have not written out a complete proof that ( 43) is correct. However, there should be no difficulty in filling in the details: as the automaton evolves from generation 2 k 2^{k} to 2 k + 1 2^{k+1}, the structure has a natural dissection into polygonal pieces.

The second example is more speculative: this is the Rule 493 automaton [26, p. 173], [A246333][17]. The binary expansions of 493 and 750 differ in just four places, so it is not surprising that this is similar to the previous example. Now an ON cell stays ON unless exactly zero or four of its neighbors are ON, in which case it turns OFF, and an OFF cell turns ON unless exactly two of its neighbors are ON. Assuming here that we start with a single ON cell at generation 0, in the even-numbered generations the number of ON cells is finite ( [A246334][18]):

 | 1, 5, 17, 29, 61, 73, 109, 157, 229, 241, 277, 329, 429, 477, 573, 633, 861, …, 1,5,17,29,61,73,109,157,229,241,277,329,429,477,573,633,861,\ldots, |  |

while in the odd-numbered generations the number of OFF cells is finite ( [A246335][19]):

 | 1, 5, 9, 21, 25, 37, 57, 85, 89, 101, 121, 165, 169, 213, 217, 317, 321, 333, …. 1,5,9,21,25,37,57,85,89,101,121,165,169,213,217,317,321,333,\ldots. |  |

The reason for hoping this automaton might be analyzable is that the latter sequence agrees with the sequence in Table 3 up though the eleventh term, 121, after which the sequences diverge. Even the respective states are the same up through the sixth term, 37, although to see this one has to work with the negatives—in the photographer’s sense, interchanging black and while cells—and then rotating the result by 45 degrees. This needs further investigation.

[image: Refer to caption]

Figure 8: Generation 15 of CA defined by eight-neighbor Rule 780.

The third example in the eight-neighbor Rule 780 ( [A246310][20]), in which a cell turns ON if one or four of its neighbors in ON, and otherwise turns OFF. Although the initial generations are simple enough, already by generation 15 (Fig. 8) the structure is extremely complicated. Is there a recurrence? Is the five-neighbor analog ( [A253086][21]) any easier to understand?

### 6.4 The three-dimensional analog of Fredkin’s Replicator

The three-dimensional Moore neighborhood, that is, the 3 × 3 × 3 3\times 3\times 3 cube without its center cell, gives rise to the sequence 1, 26, 26, 124, 26, 676, 124, 1400, … 1,26,26,124,26,676,124,1400,\ldots ( [A246031][22]), which by Theorem 2 is the run length transform of the subsequence

 | 1, 26, 124, 1400, 10000, 89504, 707008, 5924480, 47900416, 393069824, 3189761536, 25963397888, … 1,26,124,1400,10000,89504,707008,5924480,47900416,393069824,3189761536,25963397888,\ldots |  | (44) |

( [A246032][23]), computed by Roman Pearce and Michael Monagan. Doron Zeilberger [3] has found a generating function, a rational function with numerator of degree 10 10 and denominator of degree 11 11, as well as a proof that it is correct.

## 7 Further remarks about run length transforms

Block structure. It is a surprising fact that the growth sequences of many CAs have a natural division into blocks of successive lengths ( 1,) 1, 2, 4, 8, 16, 32, … (1,)1,2,4,8,16,32,\ldots. This is true even for some CAs that are defined on lattices other than ℤ d \mathbb{Z}^{d} [2]. Some of these examples are explained by the fact that the run length transform always has this property—the division into blocks of the run length transform [T n, n ≥ 0] [T_{n},n\geq 0] of an arbitrary sequence S = [1, A, B, C, D, …] S=[1,A,B,C,D,\ldots] is shown in Table 4. Table 1 above gives a concrete example. The first half of each row is given by A A times the beginning of the [T n] [T_{n}] sequence itself.

Table 4: The run length transform [T n, n ≥ 0] [T_{n},n\geq 0] of a sequence S = [1, A, B, C, D, …] S=[1,A,B,C,D,\ldots], showing the division into blocks of sizes 1, 1, 2, 4, 8, 16, … 1,1,2,4,8,16,\ldots.

 | n T n 0 1 1 A 2 − 3 A B 4 − 7 A A 2 B C 8 − 15 A A 2 A 2 A ​ B B A ​ B C D 16 − 31 A A 2 A 2 A ​ B A 2 A 3 A ​ B A ​ C B A ​ B A ​ B B 2 C A ​ C D E 32 − 63 A A 2 A 2 A ​ B A 2 A 3 A ​ B A ​ C … \begin{array}[]{c|rrrrrrrrrrrrrrrr}n&&&&&&&T_{n}\\ \hline\cr 0&1\\ 1&A\\ 2-3&A&B\\ 4-7&A&A^{2}&B&C\\ 8-15&A&A^{2}&A^{2}&AB&B&AB&C&D\\ 16-31&A&A^{2}&A^{2}&AB&A^{2}&A^{3}&AB&AC&B&AB&AB&B^{2}&C&AC&D&E\\ 32-63&A&A^{2}&A^{2}&AB&A^{2}&A^{3}&AB&AC&\ldots&&&&\end{array} |  |

Further examples. We briefly mention four additional examples of run length transforms. The run length transform of 0, 1, 2, 3, 4, … 0,1,2,3,4,\ldots is 1, 1, 1, 2, 1, 1, 2, 3, 1, … 1,1,1,2,1,1,2,3,1,\ldots ( [A227349][24]), which gives the product of the lengths of runs of 1s in the binary representation of n n. The primes, prefixed by 1, give 1, 2, 2, 3, 2, 4, 3, 5, 2, … 1,2,2,3,2,4,3,5,2,\ldots ( [A246029][25]). The squares give 1, 1, 1, 4, 1, 1, 4, 9, … 1,1,1,4,1,1,4,9,\ldots ( [A246595][26]). The powers of 2 give 1, 2, 2, 4, 2, 4, 4, 8, 2, … 1,2,2,4,2,4,4,8,2,\ldots, 2 wt ⁡ ( n) 2^{\wt(n)} ( [A001316][7], already mentioned in § 6.1).

Graphs. The graphs of run length transforms are usually highly irregular, as one expects from Table 4. The partial sums of these sequences are naturally smoother, and generally have a family resemblance, with a bumpy appearance somewhat similar to what is seen in the Tagaki curve [1], [12]. The partial sums of the four examples in the previous paragraph are [A253083][27], [A253081][28], [A253082][29], [A006046][30], respectively, and the partial sums of the sequences arising from Fredkin’s Replicator, the sequence in Sect. 5, and the Rule 150 sequence in Sect. 6 are respectively [A245542][31], [A253908][32], [A134659][33]. 2 2 2 The “graph” button in [16] makes it easy to compare these graphs. However, it is not clear how the growth rate of the original sequence affects the “bumpiness” of the partial sums. The latter sequence is discussed in [6], and it would be interesting to see if the methods of that paper can be applied to the other six sequences. Also, is there any direct connection between the limiting form of these graphs for large n n and the Tagaki curve?

The generalized run length transform. There are analogs of Theorem 2 which apply to larger neighborhoods, although they are more complicated and not as useful. The following is a version which applies when the neighborhood F F has height at most 2. Whereas in Theorem 2, a n ​ ( F) a_{n}(F) was expressed as a product of terms from the subsequence a m ​ ( F) a_{m}(F) where the binary expansion of m m contained no zeros, now we need the values a m ​ ( F) a_{m}(F) where m m is any number whose binary expansion begins and ends with 1 and does not contain any pair of adjacent zeros. These are the numbers ( [A247648][34])

 | 1, 3, 5, 7, 11, 13, 15, 21, 23, 27, 29, 31, 43, 45, 47, 53, 55, 59, 61, 63, …. 1,3,5,7,11,13,15,21,23,27,29,31,43,45,47,53,55,59,61,63,\ldots. |  | (45) |

Suppose for simplicity that the binary expansion of n n has the form

 | n = ∗ ∗ ⋯ ∗ ⏞ m 1 ​ 00 ⋯ 0 ⏞ m 2 ​ ∗ ∗ ⋯ ∗ ⏞ m 3, m 1, m 3 ≥ 1, m 2 ≥ 2, n\penalty\ =\penalty\ \overbrace{\ast\ast\cdots\ast}^{m_{1}}\overbrace{00\cdots 0}^{m_{2}}\overbrace{\ast\ast\cdots\ast}^{m_{3}},\quad m_{1},m_{3}\geq 1,m_{2}\geq 2, |  |

where the asterisks indicate strings of 0s and 1s that begin and end with 1s and do not contain any pair of adjacent zeros. If the first such string represents N 1 N_{1} and the second N 2 N_{2}, then a n ​ ( F) = a N 1 ​ ( F) ​ a N 2 ​ ( F) a_{n}(F)=a_{N_{1}}(F)a_{N_{2}}(F). There is an analogous expression in the general case, expressing a n ​ ( F) a_{n}(F) as a product of terms a m ​ ( F) a_{m}(F) where m m belongs to ( 45).

To illustrate, suppose F F is the five-celled one-dimensional neighborhood shown in Fig. 1 (iv), with height 2. The initial values of a n ​ ( F) a_{n}(F) are given in Table 5, with a m ​ ( F) a_{m}(F) for m m in ( 45) shown in bold. For example, the binary expansion of 167 is 10100111, so the generalized run length transform tells us that a 167 ​ ( F) = a 5 ​ ( F) ​ a 7 ​ ( F) = 17.19 = 323 a_{167}(F)=a_{5}(F)a_{7}(F)=17.19=323. It follows from the generalized run length transform property that in each row of the table, the first one-eighth of the terms coincide with 5 times the beginning of the sequence itself.

Table 5: Number of ON cells at n n th generation of of odd-rule one-dimensional CA defined by a 5-celled neighborhood ( [A247649][35]).

 | n a n 0 𝟏 1 𝟓 2 − 3 5 𝟕 4 − 7 5 𝟏𝟕 7 𝟏𝟗 8 − 15 5 25 17 𝟏𝟗 7 𝟑𝟏 19 𝟐𝟓 16 − 31 5 25 25 35 17 𝟔𝟏 19 𝟕𝟏 … \begin{array}[]{c|rrrrrrrrr}n&&&a_{n}\\ \hline\cr 0&\mathbf{1}\\ 1&\mathbf{5}\\ 2-3&5&\mathbf{7}\\ 4-7&5&\mathbf{17}&7&\mathbf{19}\\ 8-15&5&25&17&\mathbf{19}&7&\mathbf{31}&19&\mathbf{25}\\ 16-31&5&25&25&35&17&\mathbf{61}&19&\mathbf{71}&\ldots\end{array} |  |

The bold-faced entries in Table 5 form [A253085][36], and we end with one last question: is there an independent characterization of this sequence? An affirmative answer might make the generalized run length transform a lot more interesting. Much remains to be done in this subject!

## Postscript, March 2015

After seeing an initial version of this paper, Doron Zeilberger observed that it is possible to use Theorems 1 and 2 to automate calculation of sequences giving the number of ON cells in odd-rule CAs, and in the case of height-one neighborhoods, to find and rigorously prove the correctness of generating functions for the sequences of which they are the run length transforms. Details will appear elsewhere [3, 4].

## Acknowledgments

Theorems 1 and 2 were suggested by reading Torsten Sillke’s paper [19]. Thanks to Hrothgar for sending a copy of [10]. Figures 2 – 8 were produced with the help of the CellularAutomaton command in Mathenatica [25]. Kellen Myers showed me how to make an animated gif with Mathematica. Thanks to Roman Pearce and Michael Monagan for computing the initial terms of sequence ( 44). Stephen Wolfram, Todd Rowland, and Hrothgar provided helpful comments on the manuscript.

## References

- [1] P. C. Allaart and K. Kawamura, The Takagi function: a survey, Real Analysis Exchange, 3 7 (2011/12), 1Ð-54; [http://arxiv.org/abs/1110.1691][37].
- [2] D. Applegate, O. E. Pol, and N. J. A. Sloane, The toothpick sequence and other sequences from cellular automata, Congress. Numerant., 2 06 (2010), 157–191; [http://arxiv.org/abs/1004.3036][38].
- [3] S. B. Ekhad, N. J. A. Sloane, and D. Zeilberger, A meta-algorithm for creating fast algorithms for counting ON cells in odd-rule cellular automata, Preprint, March 2015.
- [4] S. B. Ekhad, N. J. A. Sloane, and D. Zeilberger, “Odd-rule” cellular automata on the square grid, Preprint, March 2015.
- [5] D. Eppstein, Growth and decay in Life-like cellular automata, 2009; [http://arxiv.org/abs/0911.2890][39].
- [6] S. Finch, P. Sebah, and Z.-Q. Bai, Odd entries in Pascal’s trinomial triangle, 2008; [http://arxiv.org/abs/0802.2654][40].
- [7] E. Fredkin, Digital mechanics, an informational process based on reversible universal cellular automata, in Cellular Automata, Theory and Experiment, ed. H. Gutowitz, MIT Press, 1990, pp. 254–270.
- [8] E. Fredkin, Digital Mechanics (Working Draft), 2000; [http://64.78.31.152/wp-content/uploads/2012/08/digital_mechanics_book.pdf][41].
- [9] H. Havermann et al., Entry [A071053][13] in [16], 2002–present.
- [10] Hrothgar, Notes on a replicating automaton, Preprint, July 2014.
- [11] J. Kari, Theory of cellular automata: a survey, Theoret. Comput. Sci., 3 34 (2005), 3-Ð33.
- [12] J. C. Lagarias, The Takagi function and its properties, in Functions in Number Theory and Their Probabilistic Aspects, ed. K. Matsumoto et al., RIMS Lecture Notes, vol. B 34, Res. Inst. Math. Sci., Kyoto, 2012, pp. 153–189; [http://arxiv.org/abs/1112.4205][42].
- [13] J. Layman et al., Entry [A160239][2] in [16], 2009–present.
- [14] O. Martin, A. M. Odlyzko, and S. Wolfram, Algebraic properties of cellular automata, Comm. Math. Phys., 9 3 (1984), 219–258.
- [15] S. Mitra and S. Kumar, Fractal replication in time-manipulated one-dimensional cellular automata, Complex Systems, 1 6 (2006), 191–207.
- [16] The OEIS Foundation Inc., The On-Line Encyclopedia of Integer Sequences, 1996–present; [https://oeis.org][43].
- [17] N. H. Packard and S. Wolfram, Two-dimensional cellular automata, J. Statist. Phys., 3 8 (1985), 901–946.
- [18] B. Salvy and P. Zimmermann, GFUN: a Maple package for the manipulation of generating and holonomic functions in one variable, ACM Transactions on Mathematical Software, 2 0 (1994), 163–177.
- [19] T. Sillke, Odd trinomials: t ⁡ ( n) = ( 1 + x + x 2) n t(n)=(1+x+x^{2})^{n}, 2004; [http://www.mathematik.uni-bielefeld.de/~sillke/PUZZLES/trinomials][44].
- [20] D. Singmaster, On the cellular automaton of Ulam and Warburton, M500 Magazine of the Open University, No. 1 95 (December 2003), pp. 2–7; [https://oeis.org/A079314/a079314.pdf][45].
- [21] S. M. Ulam, On some mathematical problems connected with patterns of growth of figures, in Mathematical Problems in the Biological Sciences, ed. R. E. Bellman, Proc. Sympos. Applied Math., Vol. 1 4, Amer. Math. Soc., 1962, pp. 215–224.
- [22] E. W. Weisstein, MathWorld, Entries for Rules 30, 90, 110, 150, 182, etc.; [http://mathworld.wolfram.com/][46], 2004–present.
- [23] S. Wolfram, Statistical mechanics of cellular automata, Rev. Mod. Phys., 5 5 (1983), 601–644.
- [24] S. Wolfram, Universality and complexity in cellular automata ( Cellular Automata, Los Alamos, 1983), Physica D, 1 0 (1984, 1Ð-35.
- [25] S. Wolfram, The Mathematica Book, Cambridge University Press and Wolfram Research, Inc., NY, 2000.
- [26] S. Wolfram, A New Kind of Science, Wolfram Media, Champaign, IL, 2002.

2010 Mathematics Subject Classification: Primary 11B85, 37B15.

*Keywords: *Automata sequences, cellular automata, Moore neighborhood, von Neumann neighborhood, odd-rule cellular automata, run length transform, Fredkin Replicator, Rule 110, Rule 150

[◄][47][image: ar5iv homepage] [48]
[Feeling lucky?][49] [50]
[Conversion report][51]
[Report an issue][52]
[View original on arXiv][53] [►][54]


## Links

[1]: mailto:njasloane@gmail.com
[2]: http://oeis.org/A160239
[3]: http://oeis.org/A245562
[4]: http://oeis.org/A246030
[5]: http://oeis.org/A072272
[6]: http://oeis.org/A007483
[7]: http://oeis.org/A001316
[8]: http://oeis.org/A071044
[9]: http://oeis.org/A070952
[10]: http://oeis.org/A071047
[11]: http://oeis.org/A071049
[12]: http://oeis.org/A071051
[13]: http://oeis.org/A071053
[14]: http://oeis.org/A001045
[15]: http://oeis.org/A169707
[16]: http://oeis.org/A151548
[17]: http://oeis.org/A246333
[18]: http://oeis.org/A246334
[19]: http://oeis.org/A246335
[20]: http://oeis.org/A246310
[21]: http://oeis.org/A253086
[22]: http://oeis.org/A246031
[23]: http://oeis.org/A246032
[24]: http://oeis.org/A227349
[25]: http://oeis.org/A246029
[26]: http://oeis.org/A246595
[27]: http://oeis.org/A253083
[28]: http://oeis.org/A253081
[29]: http://oeis.org/A253082
[30]: http://oeis.org/A006046
[31]: http://oeis.org/A245542
[32]: http://oeis.org/A253908
[33]: http://oeis.org/A134659
[34]: http://oeis.org/A247648
[35]: http://oeis.org/A247649
[36]: http://oeis.org/A253085
[37]: https://arxiv.org/pdf/1110.1691
[38]: https://arxiv.org/pdf/1004.3036
[39]: https://arxiv.org/pdf/0911.2890
[40]: https://arxiv.org/pdf/0802.2654
[41]: http://64.78.31.152/wp-content/uploads/2012/08/digital_mechanics_book.pdf
[42]: https://arxiv.org/pdf/1112.4205
[43]: https://oeis.org
[44]: http://www.mathematik.uni-bielefeld.de/~sillke/PUZZLES/trinomials
[45]: https://oeis.org/A079314/a079314.pdf
[46]: http://mathworld.wolfram.com/
[47]: /html/1503.01167
[48]: /
[49]: /feeling_lucky
[50]: /land_of_honey_and_milk
[51]: /log/1503.01168
[52]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1503.01168
[53]: https://arxiv.org/pdf/1503.01168
[54]: /html/1503.01169
