<!-- source: https://arxiv.org/html/2507.11008v1 | converted from HTML -->

A lemma on a finite union-closed family of finite sets and its applications

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2507.11008v1 [math.CO] 15 Jul 2025

# A lemma on a finite union-closed family of finite sets and its applications

Ze-Chun Hu Affiliation: College of Mathematics, Sichuan University, Chengdu 610065, China Yi-Ding Shi Affiliation: College of Mathematics, Sichuan University, Chengdu 610065, China Qian-Qian Zhou Note: Corresponding author: qianqzhou@yeah.net Affiliation: College of Science, Tianjin University of Technology, Tianjin 300384, China

Abstract In this note, we will give a lemma on a finite union-closed family of finite sets, and several applications of its.

Key words The union-closed sets conjecture, Frankl’s conjecture, Nagel’s conjecture

Mathematics Subject Classification (2010) 03E05, 05A05

## 1 Introduction and the lemma

A family 𝒜 \mathcal{A} of sets is union-closed if for any A, B ∈ 𝒜 A,B\in\mathcal{A}, it holds that A ∪ B ∈ 𝒜 A\cup B\in\mathcal{A}. For simplicity, denote n = | ∪ A ∈ ℱ A | n=|\cup_{A\in\mathcal{F}}A| and m = | ℱ | m=|\mathcal{F}|. Hereafter, for any set A A, | A | |A| denotes the cardinal number of A A.

In 1979, Peter Frankl (cf. [14, 17]) conjectured that for any finite union-closed family of finite sets, other than the family consisting only of the empty set, there exists an element that belongs to at least half of the sets in the family.

If a union-closed family ℱ \mathcal{F} contains a set with one element or two elements, then Frankl’s conjecture holds for ℱ \mathcal{F} ( [16]). This result was extended by Poonen ( [13]). In addition, the author in [13] proved that Frankl’s conjecture holds if n ≤ 7 n\leq 7 or m ≤ 28 m\leq 28, and proved an equivalent lattice formulation of Frankl’s conjecture. Bošnjak and Marković ( [1]) proved that Frankl’s conjecture holds if n ≤ 11 n\leq 11. Vučković and Zivković ( [19]) gave a computer assisted proof that Frankl’s conjecture is true if n ≤ 12 n\leq 12, which together with Faro’s result ( [11]) (see also Roberts and Simposon [15]) implies that Frankl’s conjecture holds if m ≤ 50 m\leq 50. For more progress on Frankl’s conjecture, we refer to [2], [5], [6], [7], [8], [9], [10], [12], [18] and the references therein.

Let M n = { 1, 2, ⋯, n } M_{n}=\{1,2,\cdots,n\} and ℱ ⊂ 2 M n = { A: A ⊂ M n } \mathcal{F}\subset 2^{M_{n}}=\{A:A\subset M_{n}\} with ∪ A ∈ ℱ A = M n \cup_{A\in\mathcal{F}}A=M_{n}. Suppose that ℱ \mathcal{F} is union-closed. For any k = 1, 2, ⋯, n k=1,2,\cdots,n, denote ℳ k = { A ∈ 2 M n: | A | = k }. \mathcal{M}_{k}=\{A\in 2^{M_{n}}:|A|=k\}. Define

 | T ⁡ ( ℱ) = inf { 1 ≤ k ≤ n: ℱ ∩ ℳ k ≠ ∅ }. T(\mathcal{F})=\inf\{1\leq k\leq n:\mathcal{F}\cap\mathcal{M}_{k}\neq\emptyset\}. |  |

Then 1 ≤ T ⁡ ( ℱ) ≤ n 1\leq T(\mathcal{F})\leq n. By virtue of T ⁡ ( ℱ) T(\mathcal{F}), Cui and Hu [3] introduced two stronger versions of Frankl’s conjecture, one of which is as follows:

S S -Frankl’s conjecture: If n ≥ 2 n\geq 2 and T ⁡ ( ℱ) ≥ 2 T(\mathcal{F})\geq 2, then there exist at least two elements in M n M_{n} which belong to at least half of the sets in ℱ \mathcal{F}.

Fix i ∈ { 1, 2, ⋯, n } i\in\{1,2,\cdots,n\}. Define

 | 𝒢:= { A \ { i }: A ∈ ℱ }. \displaystyle\mathcal{G}:=\{A\backslash\{i\}:A\in\mathcal{F}\}. |  |

Suppose that n ≥ 2 n\geq 2 and j ∈ { 1, 2, ⋯, n } \ { i } j\in\{1,2,\cdots,n\}\backslash\{i\}. Denote

 | 𝒢 j:= { A ∈ 𝒢: j ∈ A }, 𝒢 / j:= { A ∈ 𝒢: j ∉ A }. \displaystyle\mathcal{G}_{j}:=\{A\in\mathcal{G}:j\in A\},\ \mathcal{G}_{/j}:=\{A\in\mathcal{G}:j\notin A\}. |  |

Similarly define ℱ j \mathcal{F}_{j} and ℱ / j \mathcal{F}_{/j}. Now we can state the main lemma.

###### Lemma 1.1

If | 𝒢 j | | 𝒢 | ≥ c \frac{|\mathcal{G}_{j}|}{|\mathcal{G}|}\geq c for some constant c ∈ ( 0, 1] c\in(0,1], then | ℱ j | | ℱ | ≥ 1 1 + 2 ​ ( 1 − c) / c \frac{|\mathcal{F}_{j}|}{|\mathcal{F}|}\geq\frac{1}{1+2(1-c)/c}.

The proof will be given in Section 2 and some applications will be presented in Section 3.

## 2 Proof of Lemma 1.1

We will use the following elementary inequality. Its proof is obvious.

###### Lemma 2.1

Suppose that a, b, c, d a,b,c,d are four positive numbers satisfying

 | b a ≥ k, and ​ d c ≥ k, \frac{b}{a}\geq k,\ \mbox{and}\ \frac{d}{c}\geq k, |  |

for some positive constant k k. Then b + d a + c ≥ k \frac{b+d}{a+c}\geq k.

Proof of Lemma 1.1. Define

 | x = | { A ∈ ℱ, i ∉ A, j ∈ A } ∩ { B \ { i }: B ∈ ℱ, i, j ∈ B } |, \displaystyle x=|\{A\in\mathcal{F},i\notin A,j\in A\}\cap\{B\backslash\{i\}:B\in\mathcal{F},i,j\in B\}|, |  |

 | y = | { A ∈ ℱ, i ∉ A, j ∉ A } ∩ { B \ { i }: B ∈ ℱ, i ∈ B, j ∉ B } |. \displaystyle y=|\{A\in\mathcal{F},i\notin A,j\notin A\}\cap\{B\backslash\{i\}:B\in\mathcal{F},i\in B,j\notin B\}|. |  |

Then 0 ≤ x ≤ | 𝒢 j |, 0 ≤ y ≤ | 𝒢 / j | 0\leq x\leq|\mathcal{G}_{j}|,0\leq y\leq|\mathcal{G}_{/j}|, and

 | | ℱ j | | ℱ | = | 𝒢 j | + x | 𝒢 j | + | 𝒢 / j | + x + y. \displaystyle\frac{|\mathcal{F}_{j}|}{|\mathcal{F}|}=\frac{|\mathcal{G}_{j}|+x}{|\mathcal{G}_{j}|+|\mathcal{G}_{/j}|+x+y}. |  | (2.1) |

By the assumption that | 𝒢 j | | 𝒢 | ≥ c \frac{|\mathcal{G}_{j}|}{|\mathcal{G}|}\geq c, i.e.,

 | | 𝒢 j | | 𝒢 j | + | 𝒢 / j | ≥ c, \frac{|\mathcal{G}_{j}|}{|\mathcal{G}_{j}|+|\mathcal{G}_{/j}|}\geq c, |  |

we get that

 | | 𝒢 / j | ≤ 1 − c c ​ | 𝒢 j |, \displaystyle|\mathcal{G}_{/j}|\leq\frac{1-c}{c}|\mathcal{G}_{j}|, |  |

which together with the fact that 0 ≤ y ≤ | 𝒢 / j | 0\leq y\leq|\mathcal{G}_{/j}| implies

 | | 𝒢 j | | 𝒢 j | + | 𝒢 / j | + y ≥ 1 1 + 2 ​ ( 1 − c) / c. \displaystyle\frac{|\mathcal{G}_{j}|}{|\mathcal{G}_{j}|+|\mathcal{G}_{/j}|+y}\geq\frac{1}{1+2(1-c)/c}. |  | (2.2) |

Without loss of generality, we can assume that x > 0 x>0, then x x = 1 ≥ 1 1 + 2 ​ ( 1 − c) / c \frac{x}{x}=1\geq\frac{1}{1+2(1-c)/c}. Hence by ( 2.1), ( 2.2) and Lemma 2.1, we get

 | | ℱ j | | ℱ | ≥ 1 1 + 2 ​ ( 1 − c) / c. \frac{|\mathcal{F}_{j}|}{|\mathcal{F}|}\geq\frac{1}{1+2(1-c)/c}. |  |

The proof is complete.

## 3 Applications

In this section, we will give several applications of Lemma 1.1.

### 3.1 The equivalence of Frankl’s conjecture and Nagel’s conjecture

By permuting the elements of the ground set { 1, 2, ⋯, n } \{1,2,\cdots,n\}, we can assume that

 | | { F ∈ ℱ: 1 ∈ F } | ≥ | { F ∈ ℱ: 2 ∈ F } | ≥ ⋯ ≥ | { F ∈ ℱ: n ∈ F } |. \displaystyle|\{F\in\mathcal{F}:1\in F\}|\geq|\{F\in\mathcal{F}:2\in F\}|\geq\cdots\geq|\{F\in\mathcal{F}:n\in F\}|. |  | (3.1) |

Then Frankl’s conjecture says that

 | | { F ∈ ℱ: 1 ∈ F } | ≥ 1 2 ​ | ℱ |. |\{F\in\mathcal{F}:1\in F\}|\geq\frac{1}{2}|\mathcal{F}|. |  |

Nagel [12] introduced the following conjecture (we call it Nagel’s conjecure):

Nagel’s conjecture: For any k ∈ { 1, 2, ⋯, n } k\in\{1,2,\cdots,n\}, it holds that

 | | { F ∈ ℱ: k ∈ F } | ≥ 1 2 k − 1 + 1 ​ | ℱ |. \displaystyle|\{F\in\mathcal{F}:k\in F\}|\geq\frac{1}{2^{k-1}+1}|\mathcal{F}|. |  | (3.2) |

Obviously, Nagel’s conjecture implies Frankl’s conjecture. Das and Wu [4] proved that Nagel’s conjecture is true for k ≥ 3 k\geq 3 and for k = 2 k=2 under some additional condition.

By Lemma 1.1, we have the following result.

###### Proposition 3.1

Frankl’s conjecture is equivalent to Nagel’s conjecture.

Proof. It is enough to show the necessity. Suppose that Frankl’s conjecture is true. Then for the ℱ \mathcal{F} above, we have that

 | | { F ∈ ℱ: 1 ∈ F } | ≥ 1 2 ​ | ℱ |. |\{F\in\mathcal{F}:1\in F\}|\geq\frac{1}{2}|\mathcal{F}|. |  |

Without of loss of generality, we assume that n ≥ 2 n\geq 2. Define

 | 𝒢:= { A \ { 1 }: A ∈ ℱ }. \mathcal{G}:=\{A\backslash\{1\}:A\in\mathcal{F}\}. |  |

Then 𝒢 \mathcal{G} is a union-closed family of sets satisfying ⋃ A ∈ 𝒢 A = { 2, 3, ⋯, n } \bigcup_{A\in\mathcal{G}}A=\{2,3,\cdots,n\}. By the assumption, we know that there exists i ∈ { 2, 3, ⋯, n } i\in\{2,3,\cdots,n\} such that

 | | { A ∈ 𝒢: i ∈ A } | ≥ 1 2 ​ | 𝒢 |. |\{A\in\mathcal{G}:i\in A\}|\geq\frac{1}{2}|\mathcal{G}|. |  |

Then by Lemma 1.1, we get that

 | | { A ∈ ℱ: i ∈ A } | ≥ 1 1 + 2 ​ ( 1 − 1 / 2) 1 / 2 ​ | ℱ | = 1 3 ​ | ℱ | = 1 2 2 − 1 + 1 ​ | ℱ |, |\{A\in\mathcal{F}:i\in A\}|\geq\frac{1}{1+\frac{2(1-1/2)}{1/2}}|\mathcal{F}|=\frac{1}{3}|\mathcal{F}|=\frac{1}{2^{2-1}+1}|\mathcal{F}|, |  |

which together with ( 3.1) implies that

 | | { F ∈ ℱ: 2 ∈ F } | ≥ 1 2 2 − 1 + 1 ​ | ℱ |, \displaystyle|\{F\in\mathcal{F}:2\in F\}|\geq\frac{1}{2^{2-1}+1}|\mathcal{F}|, |  |

i.e., ( 3.2) holds for k = 2 k=2.

Notice that

 | 1 1 + 2 ​ ( 1 − 1 2 k − 1 + 1) 1 2 k − 1 + 1 = 1 2 k + 1 = 1 2 ( k + 1) − 1 + 1. \frac{1}{1+\frac{2(1-\frac{1}{2^{k-1}+1})}{\frac{1}{2^{k-1}+1}}}=\frac{1}{2^{k}+1}=\frac{1}{2^{(k+1)-1}+1}. |  |

Then by the reduction method, we can get that for any k = 3, …, n k=3,\ldots,n, ( 3.2) holds. Hence Nagel’s conjecture is true. The proof is complete.

### 3.2 A complement to [12, Lemma 2.4]

At first, we recall [12, Lemma 2.4] as follows:

###### Lemma 3.2

(Nagel) For any A ∈ ℱ A\in\mathcal{F} with | A | ≥ 1 |A|\geq 1, and any x ∈ A x\in A, it holds

 | | { F ∈ ℱ: x ∈ F } | ≥ 1 2 | A | − 1 + 1 ​ | ℱ |. |\{F\in\mathcal{F}:x\in F\}|\geq\frac{1}{2^{|A|-1}+1}|\mathcal{F}|. |  |

If | A | = 1 |A|=1, then 1 2 | A | − 1 + 1 = 1 2 \frac{1}{2^{|A|-1}+1}=\frac{1}{2} and thus the inequality in Lemma 3.2 is the best in this case. If | A | ≥ 2 |A|\geq 2, we have the following result which can be regarded as a complement to Lemma 3.2.

###### Proposition 3.3

For any A ∈ ℱ A\in\mathcal{F} with | A | ≥ 2 |A|\geq 2, there exists y ∈ A y\in A such that

 | | { F ∈ ℱ: y ∈ F } | ≥ 1 2 | A | − 2 + 1 ​ | ℱ |. \displaystyle|\{F\in\mathcal{F}:y\in F\}|\geq\frac{1}{2^{|A|-2}+1}|\mathcal{F}|. |  | (3.3) |

Proof. If | A | = 2 |A|=2, it is well known that there exists one element y ∈ A y\in A such that

 | | { F ∈ ℱ: y ∈ F } | ≥ 1 2 ​ | ℱ |, |\{F\in\mathcal{F}:y\in F\}|\geq\frac{1}{2}|\mathcal{F}|, |  |

i.e., ( 3.3) holds in this case.

If | A | = 3 |A|=3, we express A A as { x 1, x 2, x 3 } \{x_{1},x_{2},x_{3}\}. Define

 | 𝒢:= { B \ { x 1 }: B ∈ ℱ }. \mathcal{G}:=\{B\backslash\{x_{1}\}:B\in\mathcal{F}\}. |  |

Then 𝒢 \mathcal{G} is a finite union-closed family with ⋃ B ∈ 𝒢 B = { 1, 2, ⋯, n } \ { x 1 } \bigcup_{B\in\mathcal{G}}B=\{1,2,\cdots,n\}\backslash\{x_{1}\} and { x 2, x 3 } ∈ 𝒢 \{x_{2},x_{3}\}\in\mathcal{G}. Thus there exists k ∈ { 2, 3 } k\in\{2,3\} such that

 | | { B ∈ 𝒢: x k ∈ B } | ≥ 1 2 ​ | 𝒢 |. |\{B\in\mathcal{G}:x_{k}\in B\}|\geq\frac{1}{2}|\mathcal{G}|. |  |

Then by Lemma 1.1, we get that

 | | { B ∈ ℱ: x k ∈ B } | ≥ 1 1 + 2 ​ ( 1 − 1 2) / 1 2 ​ | ℱ | = 1 3 ​ | ℱ | = 1 2 3 − 2 + 1 ​ | ℱ |, |\{B\in\mathcal{F}:x_{k}\in B\}|\geq\frac{1}{1+2(1-\frac{1}{2})/\frac{1}{2}}|\mathcal{F}|=\frac{1}{3}|\mathcal{F}|=\frac{1}{2^{3-2}+1}|\mathcal{F}|, |  |

i.e., ( 3.3) holds in this case.

For | A | ≥ 4 |A|\geq 4, by the reduction method, we can easily obtain the result.

### 3.3 About S S -Frankl’s conjecture

It is easy to know that S S -Frankl’s conjecture implies Frankl’s conjecture. Similar to the result in Gilmer [6], we can ask the following question:

Question 1. If n ≥ 2 n\geq 2, are there two positive constants c 1, c 2 c_{1},c_{2} with c 1 ≥ c 2 c_{1}\geq c_{2} such that there exist two elements i, j ∈ { 1, 2, ⋯, n } i,j\in\{1,2,\cdots,n\} such that

 | | ℱ i | | ℱ | ≥ c 1, and ​ | ℱ j | | ℱ | ≥ c 2 ​? \frac{|\mathcal{F}_{i}|}{|\mathcal{F}|}\geq c_{1},\ \mbox{and}\ \frac{|\mathcal{F}_{j}|}{|\mathcal{F}|}\geq c_{2}? |  |

###### Remark 3.4

(i) By virtue of Subsection 3.1, we conjecture that the best possible general result is that c 1 = 1 2, c 2 = 1 3 c_{1}=\frac{1}{2},c_{2}=\frac{1}{3}.

(ii) If T ⁡ ( ℱ) = 2 T(\mathcal{F})=2, then by Lemma 1.1 or Proposition 3.3, we can take c 1 = 1 2, c 2 = 1 3 c_{1}=\frac{1}{2},c_{2}=\frac{1}{3}.

(iii) S-Frankl’s conjecture is equivalent to that if T ⁡ ( ℱ) ≥ 2 T(\mathcal{F})\geq 2, then we can take c 1 = c 2 = 1 2 c_{1}=c_{2}=\frac{1}{2}.

(iv) By the result in Liu [10], we can take c 1 = 0.38234 c_{1}=0.38234. Then by Lemma 1.1, we can take c 2 = 1 1 + 2 ​ ( 1 − 0.38234) / 0.38234 ≈ 0.23635 c_{2}=\frac{1}{1+2(1-0.38234)/0.38234}\approx 0.23635.

Acknowledgments

This work was supported by National Natural Science Foundation of China (Grant Nos. 12171335, 12301603).

## References

- [1] Bošnjak I., Marković P.: The 11-element case of Frankl’s conjecture, Electron. J. Combin. 15(1), #88, 17 pp. (2008)
- [2] Bruhn H., Schaudt O.: The journey of the union-closed sets conjecture, Graphs Comb. 31(6), 2043-2074 (2015)
- [3] Cui Z., Hu Z.-C.: Two stronger versions of the union-closed sets conjecture, Adv. Math. (China) 50(6), 829-851 (2021)
- [4] Das S., Wu S.: Frequent elements in union-closed set families, arXiv:2412.03862 (2024)
- [5] Ellis D., Ivan M.-R., Leader I.: Small sets in union-closed families, arXiv:2201.11484 (2022)
- [6] Gilmer J.: A constant lower bound for the union-closed conjecture, arXiv:2211.09055 (2022)
- [7] Hu Z.-C., Li S.-L.: The 6-element case of S 1 S_{1} -Frankl conjecture (I), J. Sichuan Univ. (Natural Sci. Edi.), 57(1), 11-26 (2020)
- [8] Kabela A., Polák M., Teska J.: The number of abundant elements in union-closed families without small sets, arXiv:2212.09279v2 (2023)
- [9] Karpas I.: Two results on union-closed families, arXiv:1708.01434 (2017)
- [10] Liu J.B.: Improving the lower bound for the union-closed sets conjecture via conditional IID coupling, arXiv:2306.08824v1 (2023)
- [11] Lo Faro G.: Union-closed sets conjecture: improved bounds, J. Comb. Math. Comb. Comput. 16, 97-102 (1994)
- [12] Nagel N.: Notes on the union closed sets conjecture, arXiv:2208.03803v2 (2023)
- [13] Poonen B.: Union-closed families, J. Comb. Theory, Ser. A 59(2), 253-268 (1992)
- [14] Rival I. (Ed.): Graphs and Order, Reidel, Dordrecht/Boston (1985)
- [15] Roverts I., Simpson J.: A note on the union-closed sets conjecture, Austral. J. Comb. 47, 265-267 (2010)
- [16] Sarvate D.G., Renaud J.-C.: On the union-closed sets conjecture, Ars Combin. 27, 149-154 (1989)
- [17] Stanley R. P., Enumerative Combinatorics, Vol. I, Wadsworth & Brooks/Cole, Belmont, CA (1986)
- [18] Studer L.: An asymptotic version of Frankl’s conjecture. Amer. Math. Monthly 128(7), 652-654 (2021)
- [19] Vučković B., Zivković M.: The 12-element case of Frankl’s conjecture, IPSI BgD Transactions on Internet Research, 13(1), 765-71 (2017)


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
