<!-- source: https://ar5iv.labs.arxiv.org/html/2301.00898 | converted from HTML -->

[2301.00898] Permutation Statistics in Conjugacy Classes of the Symmetric Group1footnote 11footnote 1This work was completed in part at the 2022 Graduate Research Workshop in Combinatorics, which was supported in part by NSF grant #1953985 and a generous award from the Combinatorics Foundation. ML was partially supported by J. A. Grochow’s NSF award CISE-2047756 and the University of Colorado Boulder, Department of Computer Science Summer Research Fellowship. MY was partially supported by the University of Denver’s Professional Research Opportunities for Faculty Fund 80369-145601. We wish to thank Sara Billey for suggesting excedances and Yan Zhuang for bringing [CJZ20] to our attention. We would also like to express our gratitude to Yan Zhuang for kindly alerting us to the arXiv paper of Hamaker and Rhoades [HR22], after seeing the first version of the present paper. Finally we thank Zach Hamaker for taking the time to explain the results of the Hamaker–Rhoades paper and its overlap with the present work.

# Permutation Statistics in Conjugacy Classes
of the Symmetric Group 1 1 1 This work was completed in part at the 2022 Graduate Research Workshop in Combinatorics, which was supported in part by NSF grant #1953985 and a generous award from the Combinatorics Foundation. ML was partially supported by J. A. Grochow’s NSF award CISE-2047756 and the University of Colorado Boulder, Department of Computer Science Summer Research Fellowship. MY was partially supported by the University of Denver’s Professional Research Opportunities for Faculty Fund 80369-145601. We wish to thank Sara Billey for suggesting excedances and Yan Zhuang for bringing [CJZ20] to our attention. We would also like to express our gratitude to Yan Zhuang for kindly alerting us to the arXiv paper of Hamaker and Rhoades [HR22], after seeing the first version of the present paper. Finally we thank Zach Hamaker for taking the time to explain the results of the Hamaker–Rhoades paper and its overlap with the present work.

Jesse Campion Loth Department of Mathematics, Simon Fraser University Michael Levet Department of Computer Science, University of Colorado Boulder Kevin Liu Department of Mathematics, University of Washington Eric Nathan Stucky Department of Information Technology & Sciences, Champlain College Sheila Sundaram Pierrepont School, Westport, CT, USA Mei Yin Department of Mathematics, University of Denver

###### Abstract

We introduce the notion of a *weighted inversion statistic*on the symmetric group, and examine its distribution on each conjugacy class. Our work generalizes the study of several common permutation statistics, including the number of inversions, the number of descents, the major index, and the number of excedances. As a consequence, we obtain explicit formulas for the first moments of several statistics by conjugacy class. We also show that when the cycle lengths are sufficiently large, the higher moments of arbitrary permutation statistics are independent of the conjugacy class. Fulman ( J. Comb. Theory Ser. A., 1998) previously established this result for major index and descents. We obtain these results, in part, by generalizing the techniques of Fulman (ibid.), and introducing the notion of permutation constraints. For permutation statistics that can be realized via *symmetric*constraints, we show that each moment is a polynomial in the degree of the symmetric group.

Keywords. permutation statistics, inversions, descents, excedances, weighted inversion statistic, moments, permutation constraints

2020 AMS Subject Classification. 05A05, 05E05, 60C05

## 1 Introduction

Let S n subscript 𝑆 𝑛 S_{n} denote the symmetric group of permutations on [n] = { 1, 2, …, n } delimited-[] 𝑛 1 2 … 𝑛 [n]=\{1,2,\dots,n\}. A statistic on S n subscript 𝑆 𝑛 S_{n} is a map X: S n → ℝ: 𝑋 → subscript 𝑆 𝑛 ℝ X:S_{n}\to\mathbb{R}. The *distribution*of X 𝑋 X on S n subscript 𝑆 𝑛 S_{n} is the function ( x k) k ∈ ℝ subscript subscript 𝑥 𝑘 𝑘 ℝ (x_{k})_{k\in\mathbb{R}}, where x k subscript 𝑥 𝑘 x_{k} is mapped to the number of permutations ω ∈ S n 𝜔 subscript 𝑆 𝑛 \omega\in S_{n} such that X ​ ( ω) = k 𝑋 𝜔 𝑘 X(\omega)=k, i.e., x k = | X − 1 ​ ( k) | subscript 𝑥 𝑘 superscript 𝑋 1 𝑘 x_{k}=|X^{-1}(k)|. Perhaps the best known statistics are the numbers of descents, the major index, and the inversion number of a permutation (see [Sta97, Sta99]).

We study the distributions of statistics on fixed conjugacy classes of S n subscript 𝑆 𝑛 S_{n}. These distributions are known exactly for some classical statistics: Gessel and Reutenauer [GR93, Theorems 5.3, 5.5, 6.1] gave a generating function for the joint distribution of descents and major index by conjugacy class. Brenti [Bre93] gave the generating function by conjugacy class for the excedance statistic in terms of the Eulerian polynomials. Some asymptotic results are also known: Fulman [Ful98] showed that descents and major index exhibit an asymptotically normal distribution on conjugacy classes with sufficiently large cycles. Kim and Lee [KL20] subsequently extended this result to any conjugacy class of S n subscript 𝑆 𝑛 S_{n}.

We focus on the properties of the moments of these distributions. Fulman [Ful98] showed that for partitions λ ⊢ n proves 𝜆 𝑛 \lambda\vdash n with each λ i > 2 ​ ℓ subscript 𝜆 𝑖 2 ℓ \lambda_{i}>2\ell, the ℓ ℓ \ell th moment for descents of the conjugacy class C λ subscript 𝐶 𝜆 C_{\lambda} is the same as for the entire symmetric group. In particular, this implies that the moments for descents and major index on a conjugacy class C λ subscript 𝐶 𝜆 C_{\lambda} are dependent only on the smaller part sizes of λ 𝜆 \lambda. Fulman provided two proofs of this – one using generating functions and the other a purely combinatorial proof that leveraged the structure of descent sets. This paper will establish similar dependence results for all permutation statistics, not just those with special descent structure.

Inspired by the combinatorial proof of [Ful98, Theorem 3], we define a framework that allows us to calculate the first moment for multiple families of permutation statistics. It turns out that the first moment for all these statistics is only dependent on the number of parts of size one and two in λ 𝜆 \lambda. The higher moments of these statistics are, in general, difficult to calculate explicitly. Remarkably, this framework allows us to show that the higher moments of all permutation statistics depend only on the small part sizes of λ 𝜆 \lambda.

Finally, we show that for a natural class of permutation statistics (see Theorem 7.26) that include inversions, permutation patterns, and excedances, these moments are polynomial in n 𝑛 n. Using these polynomiality results and data for small values of n 𝑛 n, we can explicitly calculate some higher moments of some permutation statistics. Gatez and Pierson [GP23] established the analogous result for a different generalization of permutation patterns. While our generalization and that of Gaetz and Pierson [GP23] agree for permutation patterns on certain conjugacy classes, it is not clear that they both capture the same family of permutation statistics.

Main results. In this paper, we study the uniform distribution of various permutation statistics on individual conjugacy classes. Our analysis of the uniform distribution of a very large class of permutation statistics is accomplished by the introduction of two notions: weighted inversion statistics (Section 4) and (symmetric) permutation constraints (Section 7) on S n subscript 𝑆 𝑛 S_{n}. In fact, the classically defined inversions, descents, and major index are specific instances of weighted inversion statistics. While the notion of a weighted inversion statistic is new, the notion of a permutation constraint can be traced back to [Ful98, Theorem 3]. The notion of a permutation constraint is quite powerful, allowing us to reason about arbitrary permutation statistics. Although symmetric constraints do not appear to include all weighted inversion statistics, they are still quite general, capturing inversions, permutation pattern statistics, and excedances.

We first examine the expected values of weighted inversion statistics on individual conjugacy classes, obtaining the following independence result.

###### Theorem 1.1.

Let λ = ( 1 a 1, 2 a 2, …, n a n) ⊢ n proves 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 𝑛 \lambda=(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}})\vdash n. The expected value of any weighted inversion statistic in the conjugacy class C λ subscript 𝐶 𝜆 C_{\lambda} indexed by λ 𝜆 \lambda depends only on n 𝑛 n, a 1 subscript 𝑎 1 a_{1}, and a 2 subscript 𝑎 2 a_{2}.

In the process of proving Theorem 1.1, we are able to derive explicit formulas for the expected values for several permutation statistics in individual conjugacy classes. See Table 1 for a summary of our results, as well as a comparison to the first moments of these statistics on the entire symmetric group.

statistic | λ = ( 1 a 1 ​ 2 a 2 ​ …) ⊢ n proves 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … 𝑛 \lambda=(1^{a_{1}}2^{a_{2}}\ldots)\vdash n | λ i ≥ 3 ​ ∀ i subscript 𝜆 𝑖 3 for-all 𝑖 \lambda_{i}\geq 3\ \forall i | λ = ( 1 a 1 ​ 2 a 2) 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 \lambda=(1^{a_{1}}2^{a_{2}}) | λ = ( 2 a 2) 𝜆 superscript 2 subscript 𝑎 2 \lambda=(2^{a_{2}}) | All of S n subscript 𝑆 𝑛 S_{n} |

des des \operatorname{des} | n 2 − n + 2 ​ a 2 − a 1 2 + a 1 2 ​ n superscript 𝑛 2 𝑛 2 subscript 𝑎 2 superscript subscript 𝑎 1 2 subscript 𝑎 1 2 𝑛 \frac{n^{2}-n+2a_{2}-a_{1}^{2}+a_{1}}{2n} | n − 1 2 𝑛 1 2 \frac{n-1}{2} | n 2 − a 1 2 2 ​ n superscript 𝑛 2 superscript subscript 𝑎 1 2 2 𝑛 \frac{n^{2}-a_{1}^{2}}{2n} | n 2 𝑛 2 \frac{n}{2} | n − 1 2 𝑛 1 2 \frac{n-1}{2} |

maj maj \operatorname{maj} | n 2 − n + 2 ​ a 2 − a 1 2 + a 1 4 superscript 𝑛 2 𝑛 2 subscript 𝑎 2 superscript subscript 𝑎 1 2 subscript 𝑎 1 4 \frac{n^{2}-n+2a_{2}-a_{1}^{2}+a_{1}}{4} | n ​ ( n − 1) 4 𝑛 𝑛 1 4 \frac{n(n-1)}{4} | n 2 − a 1 2 4 superscript 𝑛 2 superscript subscript 𝑎 1 2 4 \frac{n^{2}-a_{1}^{2}}{4} | n 2 4 superscript 𝑛 2 4 \frac{n^{2}}{4} | n 2 − n 4 superscript 𝑛 2 𝑛 4 \frac{n^{2}-n}{4} |

inv inv \operatorname{inv} | 3 ​ n 2 − n + 2 ​ a 2 − a 1 2 + a 1 − 2 ​ n ​ a 1 12 3 superscript 𝑛 2 𝑛 2 subscript 𝑎 2 superscript subscript 𝑎 1 2 subscript 𝑎 1 2 𝑛 subscript 𝑎 1 12 \frac{3n^{2}-n+2a_{2}-a_{1}^{2}+a_{1}-2na_{1}}{12} | n ​ ( 3 ​ n − 1) 12 𝑛 3 𝑛 1 12 \frac{n(3n-1)}{12} | ( 3 ​ n + a 1) ​ ( n − a 1) 12 3 𝑛 subscript 𝑎 1 𝑛 subscript 𝑎 1 12 \frac{(3n+a_{1})(n-a_{1})}{12} | n 2 4 superscript 𝑛 2 4 \frac{n^{2}}{4} | n 2 − n 4 superscript 𝑛 2 𝑛 4 \frac{n^{2}-n}{4} |

baj baj \operatorname{baj} | ( n + 1) ​ ( n 2 − n + 2 ​ a 2 − a 1 2 + a 1) 12 𝑛 1 superscript 𝑛 2 𝑛 2 subscript 𝑎 2 superscript subscript 𝑎 1 2 subscript 𝑎 1 12 \frac{(n+1)(n^{2}-n+2a_{2}-a_{1}^{2}+a_{1})}{12} | n ​ ( n 2 − 1) 12 𝑛 superscript 𝑛 2 1 12 \frac{n(n^{2}-1)}{12} | ( n + 1) ​ ( n 2 − a 1 2) 12 𝑛 1 superscript 𝑛 2 superscript subscript 𝑎 1 2 12 \frac{(n+1)(n^{2}-a_{1}^{2})}{12} | n 2 ​ ( n + 1) 12 superscript 𝑛 2 𝑛 1 12 \frac{n^{2}(n+1)}{12} | 1 4 ​ ( n + 1 3) 1 4 binomial 𝑛 1 3 \frac{1}{4}\binom{n+1}{3} |

baj − inv baj inv \operatorname{baj}-\operatorname{inv} | ( n − 2) ​ ( n 2 − n + 2 ​ a 2 − a 1 2 + a 1) 12 𝑛 2 superscript 𝑛 2 𝑛 2 subscript 𝑎 2 superscript subscript 𝑎 1 2 subscript 𝑎 1 12 \frac{(n-2)(n^{2}-n+2a_{2}-a_{1}^{2}+a_{1})}{12} | n ​ ( n − 1) ​ ( n − 2) 12 𝑛 𝑛 1 𝑛 2 12 \frac{n(n-1)(n-2)}{12} | ( n − 2) ​ ( n 2 − a 1 2) 12 𝑛 2 superscript 𝑛 2 superscript subscript 𝑎 1 2 12 \frac{(n-2)(n^{2}-a_{1}^{2})}{12} | n 2 ​ ( n − 2) 12 superscript 𝑛 2 𝑛 2 12 \frac{n^{2}(n-2)}{12} | 1 4 ​ ( n 3) 1 4 binomial 𝑛 3 \frac{1}{4}\binom{n}{3} |

cdes cdes \operatorname{cdes} | n 2 − n + 2 ​ a 2 − a 1 2 + 3 ​ a 1 − 2 2 ​ ( n − 1) superscript 𝑛 2 𝑛 2 subscript 𝑎 2 superscript subscript 𝑎 1 2 3 subscript 𝑎 1 2 2 𝑛 1 \frac{n^{2}-n+2a_{2}-a_{1}^{2}+3a_{1}-2}{2(n-1)} | ( n + 1) ​ ( n − 2) 2 ​ ( n − 1) 𝑛 1 𝑛 2 2 𝑛 1 \frac{(n+1)(n-2)}{2(n-1)} | n 2 − a 1 2 + 2 ​ a 1 − 2 2 ​ ( n − 1) superscript 𝑛 2 superscript subscript 𝑎 1 2 2 subscript 𝑎 1 2 2 𝑛 1 \frac{n^{2}-a_{1}^{2}+2a_{1}-2}{2(n-1)} | n 2 − 2 2 ​ ( n − 1) superscript 𝑛 2 2 2 𝑛 1 \frac{n^{2}-2}{2(n-1)} | n 2 𝑛 2 \frac{n}{2} |

exc ~ ~ exc \widetilde{\operatorname{exc}} | n + a 1 2 𝑛 subscript 𝑎 1 2 \frac{n+a_{1}}{2} | n 2 𝑛 2 \frac{n}{2} | n + a 1 2 = a 1 + a 2 𝑛 subscript 𝑎 1 2 subscript 𝑎 1 subscript 𝑎 2 \frac{n+a_{1}}{2}=a_{1}+a_{2} | n 2 = a 2 𝑛 2 subscript 𝑎 2 \frac{n}{2}=a_{2} | n + 1 2 𝑛 1 2 \frac{n+1}{2} |

exc, aexc exc aexc \operatorname{exc},\operatorname{aexc} | n − a 1 2 𝑛 subscript 𝑎 1 2 \frac{n-a_{1}}{2} | n 2 𝑛 2 \frac{n}{2} | n − a 1 2 = a 2 𝑛 subscript 𝑎 1 2 subscript 𝑎 2 \frac{n-a_{1}}{2}=a_{2} | n 2 = a 2 𝑛 2 subscript 𝑎 2 \frac{n}{2}=a_{2} | n − 1 2 𝑛 1 2 \frac{n-1}{2} |

cdasc, cddes cdasc cddes \operatorname{cdasc},\operatorname{cddes} | n − a 1 − 2 ​ a 2 6 𝑛 subscript 𝑎 1 2 subscript 𝑎 2 6 \frac{n-a_{1}-2a_{2}}{6} | n 6 𝑛 6 \frac{n}{6} | 0 0 | 0 0 | n − 2 6 𝑛 2 6 \frac{n-2}{6} |

cval, cpk cval cpk \operatorname{cval},\operatorname{cpk} | n − a 1 + a 2 3 𝑛 subscript 𝑎 1 subscript 𝑎 2 3 \frac{n-a_{1}+a_{2}}{3} | n 3 𝑛 3 \frac{n}{3} | n − a 1 2 = a 2 𝑛 subscript 𝑎 1 2 subscript 𝑎 2 \frac{n-a_{1}}{2}=a_{2} | n 2 = a 2 𝑛 2 subscript 𝑎 2 \frac{n}{2}=a_{2} | 2 ​ n − 1 6 2 𝑛 1 6 \frac{2n-1}{6} |

Table 1: Expected values of various statistics in the conjugacy class C λ subscript 𝐶 𝜆 C_{\lambda} and in S n subscript 𝑆 𝑛 S_{n}.

###### Remark 1.2.

The generating function, expected value, and variance of des des \operatorname{des} appear in Riordan [Rio14, p. 216], while the generating function and expected value of inv inv \operatorname{inv} are due to Rodrigues ( [Rod39, p. 237], [Sta97, Notes for Chapter 1]).

The Mahonian statistics maj and inv are equidistributed over S n subscript 𝑆 𝑛 S_{n} by MacMahon [Mac16], with a bijective proof via Foata’s second fundamental transformation [Foa68].

The Eulerian statistics exc and des are equidistributed over S n subscript 𝑆 𝑛 S_{n} [Mac04], [Sta97, Proposition 1.4.3] with a bijective proof via the first fundamental transformation [Rio14, FS70, Sta97].

When considering conjugacy classes where all cycles have length at least 3 3 3, we generalize the combinatorial algorithm of Fulman [Ful98, Theorem 3]. Precisely, we consider the notion of a permutation constraint, which allows us to specify values of a permutation for certain elements of the domain. We then analyze the structure of the corresponding directed graph (see Section 7). Remarkably, the notion of permutation constraint allows us to reason about arbitrary permutation statistics.

We now turn our attention to the higher moments of arbitrary permutation statistics. For a permutation statistic X 𝑋 X and a partition λ ⊢ n proves 𝜆 𝑛 \lambda\vdash n, denote 𝔼 λ ​ [X] subscript 𝔼 𝜆 delimited-[] 𝑋 \mathbb{E}_{\lambda}[X] to be the expected value of X 𝑋 X taken over the conjugacy class S n subscript 𝑆 𝑛 S_{n} indexed by λ 𝜆 \lambda.

###### Theorem 1.3.

Let X 𝑋 X be a permutation statistic that is realizable over a constraint set of size m 𝑚 m, and let k ≥ 1 𝑘 1 k\geq 1. If λ ⊢ n proves 𝜆 𝑛 \lambda\vdash n has all parts of size at least m ​ k + 1 𝑚 𝑘 1 mk+1, then 𝔼 λ ​ [X k] subscript 𝔼 𝜆 delimited-[] superscript 𝑋 𝑘 \mathbb{E}_{\lambda}[X^{k}] is independent of λ 𝜆 \lambda.

###### Remark 1.4.

As descents are weighted permutation statistics of size 2 2 2, our results in Table 1 and Theorem 1.3 imply [Ful98, Theorem 2] as a corollary.

In Section 7 we consider the class of permutation statistics realizable over symmetric constraint sets. Starting with a single symmetric constraint statistic on S n 0 subscript 𝑆 subscript 𝑛 0 S_{n_{0}}, one can construct its *symmetric extensions*to S n subscript 𝑆 𝑛 S_{n} with n ≥ 1 𝑛 1 n\geq 1. This class of permutation statistics is quite broad – including a number of well-studied statistics such as exc ~, exc, aexc ~ exc exc aexc \widetilde{\operatorname{exc}},\operatorname{exc},\operatorname{aexc} which have size 1 1 1; inv, cdasc, cddes, cval, cpk inv cdasc cddes cval cpk \operatorname{inv},\operatorname{cdasc},\operatorname{cddes},\operatorname{cval},\operatorname{cpk} which have size 2 2 2; and ile ile \mathrm{ile} which has size ≤ 3 absent 3 \leq 3. For a full account of these statistics, see Sections 4, 5, and 7, as well as [BS21].

###### Theorem 1.5.

Fix k, m ≥ 1 𝑘 𝑚 1 k,m\geq 1. Let ( λ n) subscript 𝜆 𝑛 (\lambda_{n}) be a sequence of partitions, where λ n ⊢ n proves subscript 𝜆 𝑛 𝑛 \lambda_{n}\vdash n and all parts of λ n subscript 𝜆 𝑛 \lambda_{n} have size at least m ​ k + 1 𝑚 𝑘 1 mk+1. Let ( X n) subscript 𝑋 𝑛 (X_{n}) be a symmetric extension of a symmetric permutation statistic X = X n 0 𝑋 subscript 𝑋 subscript 𝑛 0 X=X_{n_{0}} induced by a constraint set of size m 𝑚 m. There exists a polynomial p X ​ ( n) subscript 𝑝 𝑋 𝑛 p_{X}(n) depending only on X 𝑋 X such that p X ​ ( n) = 𝔼 λ n ​ [X n k] subscript 𝑝 𝑋 𝑛 subscript 𝔼 subscript 𝜆 𝑛 delimited-[] superscript subscript 𝑋 𝑛 𝑘 p_{X}(n)=\mathbb{E}_{\lambda_{n}}[X_{n}^{k}].

###### Remark 1.6.

In the proof of Theorem 1.5 (see Theorem 7.26), we are able to control both the degree and leading coefficient of these polynomials.

###### Remark 1.7.

After proving Theorem 1.5, we came across a result for permutation patterns due to Gaetz and Pierson [GP23, Theorem 1.2], who generalized a previous result of Gaetz and Ryba [GR20, Theorem 1.1(a)]. While Gaetz and Ryba utilized partition algebras and character polynomials to obtain their result, the proof technique employed by Gaetz and Pierson was purely combinatorial. In particular, the method of Gaetz and Pierson is quite similar to our techniques for establishing Theorem 1.5.

We show in Section 7 that permutation pattern statistics (in which we track the number of occurrences of a given permutation pattern within a specified permutation) are a special case of symmetric permutation constraint statistics – in fact, for infinitely many m 𝑚 m, there exists a permutation pattern that can be realized by a symmetric constraint set of size m 𝑚 m – but the latter is a more general class of statistics. Permutation patterns require that the constraints induce permutations on the occurrences of the pattern. For instance, an occurrence of the 213 213 213 -pattern in the permutation ω 𝜔 \omega is a triple x, y, z 𝑥 𝑦 𝑧 x,y,z that occurs in the order x ​ ⋯ ​ y ​ ⋯ ​ z 𝑥 ⋯ 𝑦 ⋯ 𝑧 x\cdots y\cdots z, with y < x < z 𝑦 𝑥 𝑧 y<x<z.

Our more general symmetric permutation constraint statistics, however, need not induce sub-permutations. For instance, we are able to specify triples x, y, z 𝑥 𝑦 𝑧 x,y,z such that y < x < z 𝑦 𝑥 𝑧 y<x<z and y 𝑦 y appears before both x 𝑥 x and z 𝑧 z, without specifying the relative ordering of x 𝑥 x and z 𝑧 z. With this in mind, a comparison of Theorem 1.5 and [GP23, Theorem 1.2] shows that these two results agree on permutation pattern statistics for conjugacy classes C λ subscript 𝐶 𝜆 C_{\lambda} where all parts have sufficiently large size.

###### Remark 1.8.

Theorem 1.5 has practical value in explicitly computing higher moments for individual conjugacy classes. Namely, if we compute 𝔼 ( n) ​ [X k] subscript 𝔼 𝑛 delimited-[] superscript 𝑋 𝑘 \mathbb{E}_{(n)}[X^{k}] for the class of n 𝑛 n -cycles in S n subscript 𝑆 𝑛 S_{n}, taken over deg ⁡ ( 𝔼 ( n) ​ [X k]) + 1 degree subscript 𝔼 𝑛 delimited-[] superscript 𝑋 𝑘 1 \deg(\mathbb{E}_{(n)}[X^{k}])+1 terms starting from n = m ​ k + 1 𝑛 𝑚 𝑘 1 n=mk+1, then we can use polynomial interpolation to obtain a closed form solution for 𝔼 ( n) ​ [X k] subscript 𝔼 𝑛 delimited-[] superscript 𝑋 𝑘 \mathbb{E}_{(n)}[X^{k}]. Moreover, in light of Theorem 1.3, this moment for full cycles is identical to 𝔼 λ ​ [X k] subscript 𝔼 𝜆 delimited-[] superscript 𝑋 𝑘 \mathbb{E}_{\lambda}[X^{k}], provided all parts of λ 𝜆 \lambda are at least m ​ k + 1 𝑚 𝑘 1 mk+1.

Further related work. There has been considerable work on constructing generating functions for permutation statistics.

It is well known, for instance, that the inversion and major index statistics admit the same distribution on the entire symmetric group, with the q 𝑞 q -factorial as the generating function. Permutations with the q 𝑞 q -factorial as their generating function are called Mahonian. A general account of Mahonian statistics can be found here [Foa77]. It is known that Mahonian statistics are asymptotically normal with mean ( n 2) / 2 binomial 𝑛 2 2 \binom{n}{2}/2 and variance [n ​ ( n − 1) ​ ( 2 ​ n + 5)] / 72 delimited-[] 𝑛 𝑛 1 2 𝑛 5 72 [n(n-1)(2n+5)]/72 [Foa77].

For a permutation ω 𝜔 \omega, let Des ​ ( ω) Des 𝜔 \text{Des}(\omega) be the set of descents in ω 𝜔 \omega (that is, the set of indices i 𝑖 i such that ω ​ ( i) > ω ​ ( i + 1) 𝜔 𝑖 𝜔 𝑖 1 \omega(i)>\omega(i+1)). Let d ​ ( ω):= | Des ​ ( ω) | + 1 assign 𝑑 𝜔 Des 𝜔 1 d(\omega):=|\text{Des}(\omega)|+1. The Eulerian polynomials as defined in [Sta97] serve as the generating functions for d ​ ( ω) 𝑑 𝜔 d(\omega) (see [Mac15, Rio14]). See [FS70] for a detailed treatment of the properties of Eulerian polynomials. It is known that d ​ ( ω) 𝑑 𝜔 d(\omega) is asymptotically normally distributed on S n subscript 𝑆 𝑛 S_{n}, with mean ( n + 1) / 2 𝑛 1 2 (n+1)/2 and variance ( n − 1) / 12 𝑛 1 12 (n-1)/12 under the condition that the number of i 𝑖 i -cycles vanishes asymptotically for all i 𝑖 i (an early reference is [Rio14, p. 216]; see also Fulman [Ful98], who in turn cites unpublished notes of Diaconis and Pitman [DP86]). We note that descents also have connections to sorting and the theory of runs in permutations [Knu98, Section 5], as well as to models of card shuffling [DMP95, BD92, DG19].

Outline of paper. We start in Section 2 by outlining necessary definitions and notation. In Section 3, we establish some results on the first moments of descents and major index that demonstrate some of the techniques that we apply in conjugacy classes of the symmetric group. In Sections 4 and 5, we establish results on first moments in conjugacy classes of the symmetric group, including Theorem 1.1 and Table 1. We then apply these results to the entire symmetric group in Section 6. We conclude in Section 7 by defining permutation constraint statistics and establishing general results on their moments in conjugacy classes.

## 2 Preliminaries

We outline some definitions and results that will be used throughout our work. We start with three well-known statistics.

###### Definition 2.1.

Let ω 𝜔 \omega be a permutation in the symmetric group S n subscript 𝑆 𝑛 S_{n}.

1. 1.

A *descent*of ω 𝜔 \omega is an index i ∈ [n − 1] 𝑖 delimited-[] 𝑛 1 i\in[n-1], such that ω ​ ( i) > ω ​ ( i + 1). 𝜔 𝑖 𝜔 𝑖 1 \omega(i)>\omega(i+1). We write

 | Des ⁡ ( ω) = { i: ω ​ ( i) > ω ​ ( i + 1) } Des 𝜔 conditional-set 𝑖 𝜔 𝑖 𝜔 𝑖 1 \operatorname{Des}(\omega)=\{i:\omega(i)>\omega(i+1)\} |  |

for the set of descents. We write des ⁡ ( ω):= | Des ⁡ ( ω) | assign des 𝜔 Des 𝜔 \operatorname{des}(\omega):=|\operatorname{Des}(\omega)| for the number of descents of ω 𝜔 \omega. Following [Ful98], we also denote d ​ ( ω):= des ⁡ ( ω) + 1 assign 𝑑 𝜔 des 𝜔 1 d(\omega):=\operatorname{des}(\omega)+1.

2. 2.

The *major index*maj ⁡ ( ω) maj 𝜔 \operatorname{maj}(\omega) of ω 𝜔 \omega is the sum of its descents:

 | maj ⁡ ( ω):= ∑ i ∈ Des ⁡ ( ω) i. assign maj 𝜔 subscript 𝑖 Des 𝜔 𝑖 \operatorname{maj}(\omega):=\sum_{i\in\operatorname{Des}(\omega)}i. |  |

3. 3.

An *inversion*of ω 𝜔 \omega is a pair of indices ( i, j) 𝑖 𝑗 (i,j) such that 1 ≤ i < j ≤ n 1 𝑖 𝑗 𝑛 1\leq i<j\leq n and ω ​ ( i) > ω ​ ( j) 𝜔 𝑖 𝜔 𝑗 \omega(i)>\omega(j). We write

 | Inv ⁡ ( ω) = { ( i, j): i < j, but ​ ω ​ ( i) > ω ​ ( j) } Inv 𝜔 conditional-set 𝑖 𝑗 formulae-sequence 𝑖 𝑗 but 𝜔 𝑖 𝜔 𝑗 \operatorname{Inv}(\omega)=\{(i,j):i<j,\text{ but }\omega(i)>\omega(j)\} |  |

for the set of inversions. The *inversion number*inv ⁡ ( ω):= | Inv ⁡ ( ω) | assign inv 𝜔 Inv 𝜔 \operatorname{inv}(\omega):=|\operatorname{Inv}(\omega)| is the number of inversions of ω 𝜔 \omega.

Denote by C λ subscript 𝐶 𝜆 C_{\lambda} the conjugacy class of the symmetric group S n subscript 𝑆 𝑛 S_{n} indexed by the integer partition λ 𝜆 \lambda of n 𝑛 n. The following fact is well known, e.g., [Sta97] (or [DF91]).

###### Proposition 2.2.

The order of the centralizer of an element of cycle type λ 𝜆 \lambda is z λ = ∏ i i a i ​ a i! subscript 𝑧 𝜆 subscript product 𝑖 superscript 𝑖 subscript 𝑎 𝑖 subscript 𝑎 𝑖 z_{\lambda}=\prod_{i}i^{a_{i}}a_{i}!, where λ 𝜆 \lambda has a i subscript 𝑎 𝑖 a_{i} parts equal to i, 𝑖 i, i ≥ 1 𝑖 1 i\geq 1. For λ ⊢ n proves 𝜆 𝑛 \lambda\vdash n, the order of the conjugacy class C λ subscript 𝐶 𝜆 C_{\lambda} is thus n! z λ 𝑛 subscript 𝑧 𝜆 \frac{n!}{z_{\lambda}}.

Throughout this paper, we will use Pr S n subscript Pr subscript 𝑆 𝑛 \operatorname{Pr}_{S_{n}} and Pr λ subscript Pr 𝜆 \operatorname{Pr}_{\lambda} to denote probabilities in S n subscript 𝑆 𝑛 S_{n} and C λ subscript 𝐶 𝜆 C_{\lambda} (with respect to the uniform measure). We similarly use 𝔼 S n subscript 𝔼 subscript 𝑆 𝑛 \mathbb{E}_{S_{n}} and 𝔼 λ subscript 𝔼 𝜆 \mathbb{E}_{\lambda} for expected values on the corresponding probability spaces.

## 3 Warm-up: first moments of descents and major index

Fulman [Ful98] previously determined the expected number of descents for all conjugacy classes of S n subscript 𝑆 𝑛 S_{n} without restriction to cycle types. In this section, we give an elementary, bijective proof for the expected number of descents in conjugacy classes where each cycle has length at least 3 3 3. While our result does not fully encompass that of Fulman, our technique of conjugating by an involution provides a much simpler bijective proof. Furthermore, we will employ this technique in subsequent sections (see Section 4.1).

###### Definition 3.1.

Let λ ⊢ n proves 𝜆 𝑛 \lambda\vdash n have all parts of size at least 2. Define:

 | τ i, j: C λ → C λ: subscript 𝜏 𝑖 𝑗 → subscript 𝐶 𝜆 subscript 𝐶 𝜆 \displaystyle\tau_{i,j}:C_{\lambda}\rightarrow C_{\lambda} |  |

 | τ i, j ​ ( ω) = ( i ​ j) ​ ω ​ ( i ​ j). subscript 𝜏 𝑖 𝑗 𝜔 𝑖 𝑗 𝜔 𝑖 𝑗 \displaystyle\tau_{i,j}(\omega)=(i\,j)\omega(i\,j). |  |

###### Lemma 3.2.

For any fixed i, j ∈ [n] 𝑖 𝑗 delimited-[] 𝑛 i,j\in[n] and λ 𝜆 \lambda, τ i, j subscript 𝜏 𝑖 𝑗 \tau_{i,j} is an involution on C λ subscript 𝐶 𝜆 C_{\lambda}.

###### Proof.

Since C λ subscript 𝐶 𝜆 C_{\lambda} is closed under conjugating by permutations, the map is certainly well defined. Also, applying it twice to any ω 𝜔 \omega gives ( i ​ j) ​ ( i ​ j) ​ ω ​ ( i ​ j) ​ ( i ​ j) = ω 𝑖 𝑗 𝑖 𝑗 𝜔 𝑖 𝑗 𝑖 𝑗 𝜔 (i\,j)(i\,j)\omega(i\,j)(i\,j)=\omega. ∎

Fulman previously established the following.

###### Theorem 3.3 ( [Ful98, Theorem 2]).

For a partition λ 𝜆 \lambda of n 𝑛 n with n i subscript 𝑛 𝑖 n_{i} i 𝑖 i -cycles, let C λ subscript 𝐶 𝜆 C_{\lambda} be the conjugacy class corresponding to λ 𝜆 \lambda. Then

1. 1.

𝔼 λ ​ [des] = n − 1 2 + n 2 − ( n 1 2) n subscript 𝔼 𝜆 delimited-[] des 𝑛 1 2 subscript 𝑛 2 binomial subscript 𝑛 1 2 𝑛 \mathbb{E}_{\lambda}[\operatorname{des}]=\frac{n-1}{2}+\frac{n_{2}-\binom{n_{1}}{2}}{n};

2. 2.

Fix k ≥ 0, 𝑘 0 k\geq 0, and assume all parts of λ 𝜆 \lambda have size at least 2 ​ k + 1 2 𝑘 1 2k+1. Then the k 𝑘 k th moments of des ⁡ ( ω) des 𝜔 \operatorname{des}(\omega) over C λ subscript 𝐶 𝜆 C_{\lambda} and over the full symmetric group S n subscript 𝑆 𝑛 S_{n} are equal, i.e.

 | 𝔼 λ ​ [des k] = 𝔼 S n ​ [des k]. subscript 𝔼 𝜆 delimited-[] superscript des 𝑘 subscript 𝔼 subscript 𝑆 𝑛 delimited-[] superscript des 𝑘 \mathbb{E}_{\lambda}[\operatorname{des}^{k}]=\mathbb{E}_{S_{n}}[\operatorname{des}^{k}]. |  |

###### Remark 3.4.

In [Ful98, Theorem 2], Fulman considered des ⁡ ( ω) des 𝜔 \operatorname{des}(\omega) for part (1) and d ​ ( ω) = des ⁡ ( ω) + 1 𝑑 𝜔 des 𝜔 1 d(\omega)=\operatorname{des}(\omega)+1 for part (2). This differs with Theorem 3.3, where we consider des ⁡ ( ω) des 𝜔 \operatorname{des}(\omega) in both parts (1) and (2).

Lemma 3.2 gives the following simple proof of the following restricted case of Theorem 3.3 (1). In fact, we will actually obtain the entirety of Theorem 3.3 (1) using generalizations of this technique in Section 4.

###### Observation 3.5.

Suppose that all part sizes of λ 𝜆 \lambda are at least 3 3 3. Then applying τ i, i + 1 subscript 𝜏 𝑖 𝑖 1 \tau_{i,i+1} gives a bijection between permutations in C λ subscript 𝐶 𝜆 C_{\lambda} with a descent at position i 𝑖 i, and those without.

###### Corollary 3.6.

Let λ ⊢ n proves 𝜆 𝑛 \lambda\vdash n such that each λ i ≥ 3 subscript 𝜆 𝑖 3 \lambda_{i}\geq 3. We have that:

 | 𝔼 λ ​ [des] = n − 1 2. subscript 𝔼 𝜆 delimited-[] des 𝑛 1 2 \mathbb{E}_{\lambda}[\operatorname{des}]=\frac{n-1}{2}. |  |

###### Proof.

The previous proposition gives us that the probability of having a descent at any position i 𝑖 i is 1 / 2 1 2 1/2. There are n − 1 𝑛 1 n-1 possible positions for a descent, so the result follows. ∎

## 4 Weighted inversion statistics

In this section, we consider *weighted inversion statistics*, which contain descents, major index, and the usual inversions as special cases. We will give an explicit formula for the mean on C λ subscript 𝐶 𝜆 C_{\lambda} of the indicator function of ( i, j) 𝑖 𝑗 (i,j) being an inversion. We then use this to derive a general formula for the expected value of any weighted inversion statistic on C λ subscript 𝐶 𝜆 C_{\lambda}. We start with definitions.

###### Definition 4.1.

Let ω ∈ S n 𝜔 subscript 𝑆 𝑛 \omega\in S_{n}, and let 1 ≤ i < j ≤ n 1 𝑖 𝑗 𝑛 1\leq i<j\leq n. Define I i, j subscript 𝐼 𝑖 𝑗 I_{i,j} to be the indicator function for an inversion at ( i, j) 𝑖 𝑗 (i,j), i.e., I i, j ​ ( ω) = 1 subscript 𝐼 𝑖 𝑗 𝜔 1 I_{i,j}(\omega)=1 if ω ​ ( i) > ω ​ ( j) 𝜔 𝑖 𝜔 𝑗 \omega(i)>\omega(j) and I i, j ​ ( ω) = 0 subscript 𝐼 𝑖 𝑗 𝜔 0 I_{i,j}(\omega)=0 otherwise.

A *weighted inversion statistic*in S n subscript 𝑆 𝑛 S_{n} is any statistic that can be expressed in the form ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) ​ I i, j subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 subscript 𝐼 𝑖 𝑗 \sum_{1\leq i<j\leq n}\text{wt}(i,j)I_{i,j}, where wt ​ ( i, j) ∈ ℝ wt 𝑖 𝑗 ℝ \text{wt}(i,j)\in\mathbb{R} for all i, j 𝑖 𝑗 i,j.

###### Remark 4.2.

Observe that descents, major index, and inversions are three examples of weighted inversion statistics. These can respectively be expressed as des ⁡ ( ω) = ∑ i = 1 n − 1 I i, i + 1 ​ ( ω) des 𝜔 superscript subscript 𝑖 1 𝑛 1 subscript 𝐼 𝑖 𝑖 1 𝜔 \operatorname{des}(\omega)=\sum_{i=1}^{n-1}I_{i,i+1}(\omega), maj ⁡ ( ω) = ∑ i = 1 n − 1 i ⋅ I i, i + 1 ​ ( ω) maj 𝜔 superscript subscript 𝑖 1 𝑛 1 ⋅ 𝑖 subscript 𝐼 𝑖 𝑖 1 𝜔 \operatorname{maj}(\omega)=\sum_{i=1}^{n-1}i\cdot I_{i,i+1}(\omega), and inv ⁡ ( ω) = ∑ 1 ≤ i < j ≤ n I i, j ​ ( ω) inv 𝜔 subscript 1 𝑖 𝑗 𝑛 subscript 𝐼 𝑖 𝑗 𝜔 \operatorname{inv}(\omega)=\sum_{1\leq i<j\leq n}I_{i,j}(\omega). In general, if X = ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) ​ I i, j 𝑋 subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 subscript 𝐼 𝑖 𝑗 X=\sum_{1\leq i<j\leq n}\text{wt}(i,j)I_{i,j} is a weighted inversion statistic, we can use linearity to express

 | 𝔼 λ ​ [X] = ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) ​ 𝔼 λ ​ [I i, j] = ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) ​ Pr λ ⁡ [I i, j = 1]. subscript 𝔼 𝜆 delimited-[] 𝑋 subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 subscript 𝔼 𝜆 delimited-[] subscript 𝐼 𝑖 𝑗 subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 subscript Pr 𝜆 subscript 𝐼 𝑖 𝑗 1 \mathbb{E}_{\lambda}[X]=\sum_{1\leq i<j\leq n}\text{wt}(i,j)\mathbb{E}_{\lambda}[I_{i,j}]=\sum_{1\leq i<j\leq n}\text{wt}(i,j)\operatorname{Pr}_{\lambda}[I_{i,j}=1]. |  | (4.1) |

Hence, if we can explicitly formulate 𝔼 λ ​ [I i, j] = Pr λ ⁡ [I i, j = 1] subscript 𝔼 𝜆 delimited-[] subscript 𝐼 𝑖 𝑗 subscript Pr 𝜆 subscript 𝐼 𝑖 𝑗 1 \mathbb{E}_{\lambda}[I_{i,j}]=\operatorname{Pr}_{\lambda}[I_{i,j}=1], then we can calculate 𝔼 λ ​ [X] subscript 𝔼 𝜆 delimited-[] 𝑋 \mathbb{E}_{\lambda}[X]. This approach also allows us to obtain similar results for other permutation statistics, such as excedances and cyclic descents.

### 4.1 Inversion indicator functions

In this subsection, we consider the expected value of I i, j subscript 𝐼 𝑖 𝑗 I_{i,j} in C λ subscript 𝐶 𝜆 C_{\lambda} for any λ = ( 1 a 1, 2 a 2, …, n a n) ⊢ n proves 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 𝑛 \lambda=(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}})\vdash n. Our main result will be an explicit formula in terms of n 𝑛 n, a 1 subscript 𝑎 1 a_{1}, a 2 subscript 𝑎 2 a_{2}, and the difference j − i − 1 𝑗 𝑖 1 j-i-1. Surprisingly, the expected value of I i, j subscript 𝐼 𝑖 𝑗 I_{i,j} depends on a 1 subscript 𝑎 1 a_{1} and a 2 subscript 𝑎 2 a_{2} but is independent of a 3, …, a n subscript 𝑎 3 … subscript 𝑎 𝑛 a_{3},\ldots,a_{n}, and depends on i 𝑖 i and j 𝑗 j through their difference j − i 𝑗 𝑖 j-i but not the actual values of i 𝑖 i and j 𝑗 j themselves.

One of our main tools will be applying the map τ i ​ j subscript 𝜏 𝑖 𝑗 \tau_{ij}, as introduced in Section 3. Observe that for ω ∈ C λ 𝜔 subscript 𝐶 𝜆 \omega\in C_{\lambda},

 | τ i ​ j ​ ( ω) ​ ( i) = { ω ​ ( j) if ω ​ ( j) ∉ { i, j } j if ω ​ ( j) = i i if ω ​ ( j) = j τ i ​ j ​ ( ω) ​ ( j) = { ω ​ ( i) if ω ​ ( i) ∉ { i, j } i if ω ​ ( i) = j j if ω ​ ( i) = i. formulae-sequence subscript 𝜏 𝑖 𝑗 𝜔 𝑖 cases 𝜔 𝑗 if ω ( j) ∉ { i, j } 𝑗 if ω ( j) = i 𝑖 if ω ( j) = j subscript 𝜏 𝑖 𝑗 𝜔 𝑗 cases 𝜔 𝑖 if ω ( i) ∉ { i, j } 𝑖 if ω ( i) = j 𝑗 if ω ( i) = i. \tau_{ij}(\omega)(i)=\begin{cases}\omega(j)&\text{ if $\omega(j)\notin\{i,j\}$}\\ j&\text{ if $\omega(j)=i$}\\ i&\text{ if $\omega(j)=j$}\end{cases}\qquad\tau_{ij}(\omega)(j)=\begin{cases}\omega(i)&\text{ if $\omega(i)\notin\{i,j\}$}\\ i&\text{ if $\omega(i)=j$}\\ j&\text{ if $\omega(i)=i$.}\end{cases} |  |

Motivated by the above cases, we partition C λ subscript 𝐶 𝜆 C_{\lambda} into five sets based on i 𝑖 i and j 𝑗 j:

 | Ω 1 i ​ j = { ω ∈ C λ: ω ​ ( i), ω ​ ( j) ∉ { i, j } }, Ω 2 i ​ j = { ω ∈ C λ: ω ​ ( i) = j, ω ​ ( j) = i }, Ω 3 i ​ j = { ω ∈ C λ: ω ​ ( i) = i, ω ​ ( j) = j }, Ω 4 i ​ j = { ω ∈ C λ: ω ​ ( i) = j, ω ​ ( j) ≠ i } ∪ { ω ∈ C λ: ω ​ ( i) ≠ j, ω ​ ( j) = i }, Ω 5 i ​ j = { ω ∈ C λ: ω ​ ( i) = i, ω ​ ( j) ≠ j } ∪ { ω ∈ C λ: ω ​ ( i) ≠ i, ω ​ ( j) = j }. formulae-sequence superscript subscript Ω 1 𝑖 𝑗 conditional-set 𝜔 subscript 𝐶 𝜆 𝜔 𝑖 𝜔 𝑗 𝑖 𝑗 formulae-sequence superscript subscript Ω 2 𝑖 𝑗 conditional-set 𝜔 subscript 𝐶 𝜆 formulae-sequence 𝜔 𝑖 𝑗 𝜔 𝑗 𝑖 formulae-sequence superscript subscript Ω 3 𝑖 𝑗 conditional-set 𝜔 subscript 𝐶 𝜆 formulae-sequence 𝜔 𝑖 𝑖 𝜔 𝑗 𝑗 formulae-sequence superscript subscript Ω 4 𝑖 𝑗 conditional-set 𝜔 subscript 𝐶 𝜆 formulae-sequence 𝜔 𝑖 𝑗 𝜔 𝑗 𝑖 conditional-set 𝜔 subscript 𝐶 𝜆 formulae-sequence 𝜔 𝑖 𝑗 𝜔 𝑗 𝑖 superscript subscript Ω 5 𝑖 𝑗 conditional-set 𝜔 subscript 𝐶 𝜆 formulae-sequence 𝜔 𝑖 𝑖 𝜔 𝑗 𝑗 conditional-set 𝜔 subscript 𝐶 𝜆 formulae-sequence 𝜔 𝑖 𝑖 𝜔 𝑗 𝑗 \begin{split}\Omega_{1}^{ij}&=\{\omega\in C_{\lambda}:\omega(i),\omega(j)\notin\{i,j\}\},\\ \Omega_{2}^{ij}&=\{\omega\in C_{\lambda}:\omega(i)=j,\omega(j)=i\},\\ \Omega_{3}^{ij}&=\{\omega\in C_{\lambda}:\omega(i)=i,\omega(j)=j\},\\ \Omega_{4}^{ij}&=\{\omega\in C_{\lambda}:\omega(i)=j,\omega(j)\neq i\}\cup\{\omega\in C_{\lambda}:\omega(i)\neq j,\omega(j)=i\},\\ \Omega_{5}^{ij}&=\{\omega\in C_{\lambda}:\omega(i)=i,\omega(j)\neq j\}\cup\{\omega\in C_{\lambda}:\omega(i)\neq i,\omega(j)=j\}.\end{split} |  | (4.2) |

Using the Law of Total Probability, we can decompose

 | Pr λ ⁡ [I i, j = 1] = ∑ k = 1 5 Pr λ ⁡ [ω ∈ Ω k i ​ j] ⋅ Pr λ ⁡ [I i, j ​ ( ω) = 1 ∣ ω ∈ Ω k i ​ j]. subscript Pr 𝜆 subscript 𝐼 𝑖 𝑗 1 superscript subscript 𝑘 1 5 ⋅ subscript Pr 𝜆 𝜔 superscript subscript Ω 𝑘 𝑖 𝑗 subscript Pr 𝜆 subscript 𝐼 𝑖 𝑗 𝜔 conditional 1 𝜔 superscript subscript Ω 𝑘 𝑖 𝑗 \begin{split}\operatorname{Pr}_{\lambda}[I_{i,j}=1]=\sum_{k=1}^{5}\operatorname{Pr}_{\lambda}[\omega\in\Omega_{k}^{ij}]\cdot\operatorname{Pr}_{\lambda}[I_{i,j}(\omega)=1\mid\omega\in\Omega_{k}^{ij}].\end{split} |  | (4.3) |

We can explicitly compute the quantities in this sum.

###### Lemma 4.3.

Let λ = ( 1 a 1, 2 a 2, …, n a n) ⊢ n proves 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 𝑛 \lambda=(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}})\vdash n, fix i < j 𝑖 𝑗 i<j in [n] delimited-[] 𝑛 [n], and define Ω k = Ω k i ​ j subscript Ω 𝑘 superscript subscript Ω 𝑘 𝑖 𝑗 \Omega_{k}=\Omega_{k}^{ij} as in ( 4.2). Then

1. 1.

Pr λ ⁡ [ω ∈ Ω 2] = 2 ​ a 2 n ​ ( n − 1), subscript Pr 𝜆 𝜔 subscript Ω 2 2 subscript 𝑎 2 𝑛 𝑛 1 \operatorname{Pr}_{\lambda}[\omega\in\Omega_{2}]=\frac{2a_{2}}{n(n-1)},

2. 2.

Pr λ ⁡ [ω ∈ Ω 3] = a 1 ​ ( a 1 − 1) n ​ ( n − 1), subscript Pr 𝜆 𝜔 subscript Ω 3 subscript 𝑎 1 subscript 𝑎 1 1 𝑛 𝑛 1 \operatorname{Pr}_{\lambda}[\omega\in\Omega_{3}]=\frac{a_{1}(a_{1}-1)}{n(n-1)},

3. 3.

Pr λ ⁡ [ω ∈ Ω 4] = 2 n − 1 ⋅ ( 1 − a 1 n − 2 ​ a 2 n), subscript Pr 𝜆 𝜔 subscript Ω 4 ⋅ 2 𝑛 1 1 subscript 𝑎 1 𝑛 2 subscript 𝑎 2 𝑛 \operatorname{Pr}_{\lambda}[\omega\in\Omega_{4}]=\frac{2}{n-1}\cdot\left(1-\frac{a_{1}}{n}-\frac{2a_{2}}{n}\right), and

4. 4.

Pr λ ⁡ [ω ∈ Ω 5] = 2 ​ a 1 n ⋅ ( 1 − a 1 − 1 n − 1). subscript Pr 𝜆 𝜔 subscript Ω 5 ⋅ 2 subscript 𝑎 1 𝑛 1 subscript 𝑎 1 1 𝑛 1 \operatorname{Pr}_{\lambda}[\omega\in\Omega_{5}]=\frac{2a_{1}}{n}\cdot\left(1-\frac{a_{1}-1}{n-1}\right).

###### Proof.

We proceed as follows.

1. 1.

We first note that if a 2 = 0 subscript 𝑎 2 0 a_{2}=0, then ω 𝜔 \omega has no 2 2 2 -cycles. As Ω 2 i ​ j superscript subscript Ω 2 𝑖 𝑗 \Omega_{2}^{ij} is precisely the set of permutations of C λ subscript 𝐶 𝜆 C_{\lambda} containing the 2 2 2 -cycle ( i ​ j) 𝑖 𝑗 (ij), we have that Pr λ ⁡ [ω ∈ Ω 2] = 0 subscript Pr 𝜆 𝜔 subscript Ω 2 0 \operatorname{Pr}_{\lambda}[\omega\in\Omega_{2}]=0, which agrees with the formula given.

If instead a 2 > 0 subscript 𝑎 2 0 a_{2}>0, then ( i ​ j) 𝑖 𝑗 (ij) forming a cycle implies that the remaining n − 2 𝑛 2 n-2 elements have cycle type ( 1 a 1, 2 a 2 − 1, …, n a n) superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 1 … superscript 𝑛 subscript 𝑎 𝑛 (1^{a_{1}},2^{a_{2}-1},\ldots,n^{a_{n}}). Then the probability that ( i ​ j) 𝑖 𝑗 (ij) forms a 2 2 2 -cycle is given by:

 | | C ( 1 a 1, 2 a 2 − 1, …, n a n) | | C ( 1 a 1, 2 a 2, …, n a n) | = 2 ​ a 2 n ​ ( n − 1), subscript 𝐶 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 1 … superscript 𝑛 subscript 𝑎 𝑛 subscript 𝐶 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 2 subscript 𝑎 2 𝑛 𝑛 1 \frac{|C_{(1^{a_{1}},2^{a_{2}-1},\ldots,n^{a_{n}})}|}{|C_{(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}})}|}=\frac{2a_{2}}{n(n-1)}, |  |

recalling that the formulas for the centralizer sizes are given by Proposition 2.2.

2. 2.

By definition, Ω 3 i ​ j superscript subscript Ω 3 𝑖 𝑗 \Omega_{3}^{ij} contains the permutations of C λ subscript 𝐶 𝜆 C_{\lambda} with fixed points at positions i 𝑖 i and j 𝑗 j. Thus, if a 1 ∈ { 0, 1 } subscript 𝑎 1 0 1 a_{1}\in\{0,1\}, then Pr λ ⁡ [ω ∈ Ω 3] = 0 subscript Pr 𝜆 𝜔 subscript Ω 3 0 \operatorname{Pr}_{\lambda}[\omega\in\Omega_{3}]=0, which agrees with the formula given.

If instead a 1 > 1 subscript 𝑎 1 1 a_{1}>1, then the probability that ( i) 𝑖 (i) and ( j) 𝑗 (j) form 1 1 1 -cycles is given by

 | | C ( 1 a 1 − 2, 2 a 2, …, n a n) | | C ( 1 a 1, 2 a 2, …, n a n) | = a 1 ​ ( a 1 − 1) n ​ ( n − 1). subscript 𝐶 superscript 1 subscript 𝑎 1 2 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 subscript 𝐶 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 subscript 𝑎 1 subscript 𝑎 1 1 𝑛 𝑛 1 \frac{|C_{(1^{a_{1}-2},2^{a_{2}},\ldots,n^{a_{n}})}|}{|C_{(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}})}|}=\frac{a_{1}(a_{1}-1)}{n(n-1)}. |  |

3. 3.

We first consider { ω ∈ C λ: ω ​ ( i) = j, ω ​ ( j) ≠ i } conditional-set 𝜔 subscript 𝐶 𝜆 formulae-sequence 𝜔 𝑖 𝑗 𝜔 𝑗 𝑖 \{\omega\in C_{\lambda}:\omega(i)=j,\omega(j)\neq i\}. Using the Law of Total Probability, we decompose Pr λ ⁡ [ω ​ ( i) = j, ω ​ ( j) ≠ i] subscript Pr 𝜆 𝜔 𝑖 𝑗 𝜔 𝑗 𝑖 \operatorname{Pr}_{\lambda}[\omega(i)=j,\omega(j)\neq i] into the sum of the following terms:

 | Pr λ ⁡ [i ​ is in a 1 cycle of ​ ω] ⋅ Pr λ ⁡ [ω ​ ( i) = j, ω ​ ( j) ≠ i | i ​ is in a 1 cycle of ​ ω], ⋅ subscript Pr 𝜆 𝑖 is in a 1 cycle of 𝜔 subscript Pr 𝜆 𝜔 𝑖 𝑗 𝜔 𝑗 conditional 𝑖 𝑖 is in a 1 cycle of 𝜔 \operatorname{Pr}_{\lambda}[i\text{ is in a 1 cycle of }\omega]\cdot\operatorname{Pr}_{\lambda}[\omega(i)=j,\omega(j)\neq i|i\text{ is in a 1 cycle of }\omega], |  |

 | Pr λ ⁡ [i ​ is in a 2 cycle of ​ ω] ⋅ Pr λ ⁡ [ω ​ ( i) = j, ω ​ ( j) ≠ i | i ​ is in a 2 cycle of ​ ω], ⋅ subscript Pr 𝜆 𝑖 is in a 2 cycle of 𝜔 subscript Pr 𝜆 𝜔 𝑖 𝑗 𝜔 𝑗 conditional 𝑖 𝑖 is in a 2 cycle of 𝜔 \operatorname{Pr}_{\lambda}[i\text{ is in a 2 cycle of }\omega]\cdot\operatorname{Pr}_{\lambda}[\omega(i)=j,\omega(j)\neq i|i\text{ is in a 2 cycle of }\omega], |  |

 | Pr λ ⁡ [i ​ is not in a 1 or 2 cycle of ​ ω] ⋅ Pr λ ⁡ [ω ​ ( i) = j, ω ​ ( j) ≠ i | i ​ is not in a 1 or 2 cycle of ​ ω]. ⋅ subscript Pr 𝜆 𝑖 is not in a 1 or 2 cycle of 𝜔 subscript Pr 𝜆 𝜔 𝑖 𝑗 𝜔 𝑗 conditional 𝑖 𝑖 is not in a 1 or 2 cycle of 𝜔 \operatorname{Pr}_{\lambda}[i\text{ is not in a 1 or 2 cycle of }\omega]\cdot\operatorname{Pr}_{\lambda}[\omega(i)=j,\omega(j)\neq i|i\text{ is not in a 1 or 2 cycle of }\omega]. |  |

The first two terms are 0, and hence we need only compute the third term. Observe that

 | Pr λ ⁡ [i ​ is in a 1 cycle of ​ ω] = | C ( 1 a 1 − 1, 2 a 2, …, n a n) | | C ( 1 a 1, 2 a 2, …, n a n) | = a 1 n. subscript Pr 𝜆 𝑖 is in a 1 cycle of 𝜔 subscript 𝐶 superscript 1 subscript 𝑎 1 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 subscript 𝐶 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 subscript 𝑎 1 𝑛 \operatorname{Pr}_{\lambda}[i\text{ is in a 1 cycle of }\omega]=\frac{|C_{(1^{a_{1}-1},2^{a_{2}},\ldots,n^{a_{n}})}|}{|C_{(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}})}|}=\frac{a_{1}}{n}. |  |

Using our result from (1),

 | Pr λ ⁡ [i ​ is in a 2 cycle of ​ ω] = ∑ k ≠ i Pr λ ⁡ [ω ​ ( i) = k, ω ​ ( k) = i] = 2 ​ a 2 n. subscript Pr 𝜆 𝑖 is in a 2 cycle of 𝜔 subscript 𝑘 𝑖 subscript Pr 𝜆 𝜔 𝑖 𝑘 𝜔 𝑘 𝑖 2 subscript 𝑎 2 𝑛 \operatorname{Pr}_{\lambda}[i\text{ is in a 2 cycle of }\omega]=\sum_{k\neq i}\operatorname{Pr}_{\lambda}[\omega(i)=k,\omega(k)=i]=\frac{2a_{2}}{n}. |  |

Hence, Pr λ ⁡ [i ​ is not in a 1 or 2 cycle of ​ ω] = 1 − a 1 n − 2 ​ a 2 n subscript Pr 𝜆 𝑖 is not in a 1 or 2 cycle of 𝜔 1 subscript 𝑎 1 𝑛 2 subscript 𝑎 2 𝑛 \operatorname{Pr}_{\lambda}[i\text{ is not in a 1 or 2 cycle of }\omega]=1-\frac{a_{1}}{n}-\frac{2a_{2}}{n}.

Finally, consider conjugation by ρ = ( i) ​ ( 1, 2, …, i − 1, i + 1, …, n) 𝜌 𝑖 1 2 … 𝑖 1 𝑖 1 … 𝑛 \rho=(i)(1,2,\ldots,i-1,i+1,\ldots,n) on the elements in Ω 4 subscript Ω 4 \Omega_{4}. Since ρ 𝜌 \rho acts by replacing each element of a cycle by its image under ρ 𝜌 \rho, it induces bijections among the sets

{ ω ∈ C λ: ω ​ ( i) = k, i ​ is not in a 1 or 2 cycle of ​ ω } conditional-set 𝜔 subscript 𝐶 𝜆 𝜔 𝑖 𝑘 𝑖 is not in a 1 or 2 cycle of 𝜔 \{\omega\in C_{\lambda}:\omega(i)=k,i\text{ is not in a $1$ or $2$ cycle of }\omega\}

for k ∈ [n] ∖ { i } 𝑘 delimited-[] 𝑛 𝑖 k\in[n]\setminus\{i\}. Hence, { ω ∈ C λ: i ​ is not in a 1 or 2 cycle of ​ ω } conditional-set 𝜔 subscript 𝐶 𝜆 𝑖 is not in a 1 or 2 cycle of 𝜔 \{\omega\in C_{\lambda}:i\text{ is not in a 1 or 2 cycle of }\omega\} decomposes into n − 1 𝑛 1 n-1 sets of the same size based on the image of i 𝑖 i.

We conclude that

 | Pr λ ⁡ [ω ​ ( i) = j, ω ​ ( j) ≠ i | i ​ is not in a 1 or 2 cycle of ​ ω] = 1 n − 1. subscript Pr 𝜆 𝜔 𝑖 𝑗 𝜔 𝑗 conditional 𝑖 𝑖 is not in a 1 or 2 cycle of 𝜔 1 𝑛 1 \operatorname{Pr}_{\lambda}[\omega(i)=j,\omega(j)\neq i|i\text{ is not in a 1 or 2 cycle of }\omega]=\frac{1}{n-1}. |  |

Combined, we have that

 | Pr λ ⁡ [ω ​ ( i) = j, ω ​ ( j) ≠ i] = 1 n − 1 ⋅ ( 1 − a 1 n − 2 ​ a 2 n). subscript Pr 𝜆 𝜔 𝑖 𝑗 𝜔 𝑗 𝑖 ⋅ 1 𝑛 1 1 subscript 𝑎 1 𝑛 2 subscript 𝑎 2 𝑛 \operatorname{Pr}_{\lambda}[\omega(i)=j,\omega(j)\neq i]=\frac{1}{n-1}\cdot\left(1-\frac{a_{1}}{n}-\frac{2a_{2}}{n}\right). |  |

Repeating this argument over { ω ∈ C λ: ω ​ ( i) ≠ j, ω ​ ( j) = i } conditional-set 𝜔 subscript 𝐶 𝜆 formulae-sequence 𝜔 𝑖 𝑗 𝜔 𝑗 𝑖 \{\omega\in C_{\lambda}:\omega(i)\neq j,\omega(j)=i\} and adding the two terms implies (3).

4. 4.

We similarly first consider { ω ∈ C λ: ω ​ ( i) = i, ω ​ ( j) ≠ j } conditional-set 𝜔 subscript 𝐶 𝜆 formulae-sequence 𝜔 𝑖 𝑖 𝜔 𝑗 𝑗 \{\omega\in C_{\lambda}:\omega(i)=i,\omega(j)\neq j\}. Then

 | Pr λ ⁡ [ω ​ ( i) = i, ω ​ ( j) ≠ j] = Pr λ ⁡ [ω ​ ( i) = i] ⋅ Pr λ ⁡ [ω ​ ( j) ≠ j | ω ​ ( i) = i] = a 1 n ⋅ ( 1 − Pr λ ⁡ [ω ​ ( j) = j | ω ​ ( i) = i]) = a 1 n ⋅ ( 1 − a 1 − 1 n − 1). subscript Pr 𝜆 𝜔 𝑖 𝑖 𝜔 𝑗 𝑗 ⋅ subscript Pr 𝜆 𝜔 𝑖 𝑖 subscript Pr 𝜆 𝜔 𝑗 conditional 𝑗 𝜔 𝑖 𝑖 ⋅ subscript 𝑎 1 𝑛 1 subscript Pr 𝜆 𝜔 𝑗 conditional 𝑗 𝜔 𝑖 𝑖 ⋅ subscript 𝑎 1 𝑛 1 subscript 𝑎 1 1 𝑛 1 \begin{split}\operatorname{Pr}_{\lambda}[\omega(i)=i,\omega(j)\neq j]&=\operatorname{Pr}_{\lambda}[\omega(i)=i]\cdot\operatorname{Pr}_{\lambda}[\omega(j)\neq j|\omega(i)=i]\\ &=\frac{a_{1}}{n}\cdot\left(1-\operatorname{Pr}_{\lambda}[\omega(j)=j|\omega(i)=i]\right)\\ &=\frac{a_{1}}{n}\cdot\left(1-\frac{a_{1}-1}{n-1}\right).\end{split} |  |

Repeating this argument over { ω ∈ C λ: ω ​ ( i) ≠ i, ω ​ ( j) = j } conditional-set 𝜔 subscript 𝐶 𝜆 formulae-sequence 𝜔 𝑖 𝑖 𝜔 𝑗 𝑗 \{\omega\in C_{\lambda}:\omega(i)\neq i,\omega(j)=j\} and adding this to the expression above implies the result. ∎

###### Remark 4.4.

The preceding lemma gives an explicit formula for Pr λ ⁡ [ω ∈ Ω 1] subscript Pr 𝜆 𝜔 subscript Ω 1 \operatorname{Pr}_{\lambda}[\omega\in\Omega_{1}] using 1 − ∑ k = 2 5 Pr ⁡ [ω ∈ Ω k] 1 superscript subscript 𝑘 2 5 Pr 𝜔 subscript Ω 𝑘 1-\sum_{k=2}^{5}\operatorname{Pr}[\omega\in\Omega_{k}]. We will not need this explicit formulation.

###### Lemma 4.5.

Let λ = ( 1 a 1, 2 a 2, …, n a n) ⊢ n proves 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 𝑛 \lambda=(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}})\vdash n, fix i < j 𝑖 𝑗 i<j in [n] delimited-[] 𝑛 [n], and define Ω k = Ω k i ​ j subscript Ω 𝑘 superscript subscript Ω 𝑘 𝑖 𝑗 \Omega_{k}=\Omega_{k}^{ij} as in ( 4.2). Then

1. 1.

Pr λ ⁡ [( i, j) ∈ Inv ⁡ ( ω) | ω ∈ Ω 1] = 1 2 subscript Pr 𝜆 𝑖 𝑗 conditional Inv 𝜔 𝜔 subscript Ω 1 1 2 \operatorname{Pr}_{\lambda}[(i,j)\in\operatorname{Inv}(\omega)|\omega\in\Omega_{1}]=\frac{1}{2},

2. 2.

Pr λ ⁡ [( i, j) ∈ Inv ⁡ ( ω) | ω ∈ Ω 2] = 1 subscript Pr 𝜆 𝑖 𝑗 conditional Inv 𝜔 𝜔 subscript Ω 2 1 \operatorname{Pr}_{\lambda}[(i,j)\in\operatorname{Inv}(\omega)|\omega\in\Omega_{2}]=1,

3. 3.

Pr λ ⁡ [( i, j) ∈ Inv ⁡ ( ω) | ω ∈ Ω 3] = 0 subscript Pr 𝜆 𝑖 𝑗 conditional Inv 𝜔 𝜔 subscript Ω 3 0 \operatorname{Pr}_{\lambda}[(i,j)\in\operatorname{Inv}(\omega)|\omega\in\Omega_{3}]=0,

4. 4.

Pr λ ⁡ [( i, j) ∈ Inv ⁡ ( ω) | ω ∈ Ω 4] = 1 2 + j − i − 1 2 ​ ( n − 2) subscript Pr 𝜆 𝑖 𝑗 conditional Inv 𝜔 𝜔 subscript Ω 4 1 2 𝑗 𝑖 1 2 𝑛 2 \operatorname{Pr}_{\lambda}[(i,j)\in\operatorname{Inv}(\omega)|\omega\in\Omega_{4}]=\frac{1}{2}+\frac{j-i-1}{2(n-2)}, and

5. 5.

Pr λ ⁡ [( i, j) ∈ Inv ⁡ ( ω) | ω ∈ Ω 5] = 1 2 − j − i − 1 2 ​ ( n − 2) subscript Pr 𝜆 𝑖 𝑗 conditional Inv 𝜔 𝜔 subscript Ω 5 1 2 𝑗 𝑖 1 2 𝑛 2 \operatorname{Pr}_{\lambda}[(i,j)\in\operatorname{Inv}(\omega)|\omega\in\Omega_{5}]=\frac{1}{2}-\frac{j-i-1}{2(n-2)}.

###### Remark 4.6.

A priori, it was not intuitively clear to us why:

 | Pr λ ⁡ [( i, j) ∈ Inv ⁡ ( ω) ∣ ω ∈ Ω 4] + Pr λ ⁡ [( i, j) ∈ Inv ⁡ ( ω) ∣ ω ∈ Ω 5] = 1. subscript Pr 𝜆 𝑖 𝑗 conditional Inv 𝜔 𝜔 subscript Ω 4 subscript Pr 𝜆 𝑖 𝑗 conditional Inv 𝜔 𝜔 subscript Ω 5 1 \operatorname{Pr}_{\lambda}[(i,j)\in\operatorname{Inv}(\omega)\mid\omega\in\Omega_{4}]+\operatorname{Pr}_{\lambda}[(i,j)\in\operatorname{Inv}(\omega)\mid\omega\in\Omega_{5}]=1. |  |

Prior to proving Lemma 4.5, we first highlight our intuition here. If k < i 𝑘 𝑖 k<i or k > j 𝑘 𝑗 k>j, then conjugating by ( i ​ j) 𝑖 𝑗 (ij) interchanges elements that have ( i, j) 𝑖 𝑗 (i,j) as an inversion to ones that do not. If i < k < j 𝑖 𝑘 𝑗 i<k<j, then we have to track choices for k 𝑘 k and “adjust” the probability from 1 / 2 1 2 1/2. The ( j − i − 1) / [2 ​ ( n − 2)] 𝑗 𝑖 1 delimited-[] 2 𝑛 2 (j-i-1)/[2(n-2)] term accounts for this. Precisely, in Ω 4 subscript Ω 4 \Omega_{4}, conjugating by ( i ​ j) 𝑖 𝑗 (ij) interchanges permutations that both have an inversion at ( i, j) 𝑖 𝑗 (i,j), and in Ω 5 subscript Ω 5 \Omega_{5}, conjugating by ( i ​ j) 𝑖 𝑗 (ij) interchanges permutations that both do not have an inversion at ( i, j) 𝑖 𝑗 (i,j).

###### Proof of Lemma 4.5.

1. 1.

Note that the map τ i ​ j subscript 𝜏 𝑖 𝑗 \tau_{ij} induces a bijection between the sets { ω ∈ Ω 1: ω ​ ( i) > ω ​ ( j) } conditional-set 𝜔 subscript Ω 1 𝜔 𝑖 𝜔 𝑗 \{\omega\in\Omega_{1}:\omega(i)>\omega(j)\} and { ω ∈ Ω 1: ω ​ ( i) < ω ​ ( j) } conditional-set 𝜔 subscript Ω 1 𝜔 𝑖 𝜔 𝑗 \{\omega\in\Omega_{1}:\omega(i)<\omega(j)\} that partition Ω 1 subscript Ω 1 \Omega_{1}. Hence, these two sets must have the same size, and we conclude (1).

2. 2.

This follows immediately from the definition of inversion and the images of i 𝑖 i and j 𝑗 j in the set Ω 2 subscript Ω 2 \Omega_{2}.

3. 3.

This follows immediately from the definition of inversion and the images of i 𝑖 i and j 𝑗 j in the set Ω 3 subscript Ω 3 \Omega_{3}.

4. 4.

Observe that we can partition

 | { ω ∈ C λ: ω ​ ( i) = j, ω ​ ( j) ≠ i } = ⨆ k ∉ { i, j } { ω ∈ C λ: ω ​ ( i) = j, ω ​ ( j) = k }. conditional-set 𝜔 subscript 𝐶 𝜆 formulae-sequence 𝜔 𝑖 𝑗 𝜔 𝑗 𝑖 subscript square-union 𝑘 𝑖 𝑗 conditional-set 𝜔 subscript 𝐶 𝜆 formulae-sequence 𝜔 𝑖 𝑗 𝜔 𝑗 𝑘 \{\omega\in C_{\lambda}:\omega(i)=j,\omega(j)\neq i\}=\bigsqcup_{k\notin\{i,j\}}\{\omega\in C_{\lambda}:\omega(i)=j,\omega(j)=k\}. |  |

Now consider conjugation by

 | ( i) ​ ( j) ​ ( 1, 2, …, i − 1, i + 1, …, j − 1, j + 1 ​ …, n) 𝑖 𝑗 1 2 … 𝑖 1 𝑖 1 … 𝑗 1 𝑗 1 … 𝑛 (i)(j)(1,2,\ldots,i-1,i+1,\ldots,j-1,j+1\ldots,n) |  |

on Ω 4 subscript Ω 4 \Omega_{4}. As in the proof of Lemma 4.3, this induces bijections among the sets { ω ∈ C λ: ω ​ ( i) = j, ω ​ ( j) = k } conditional-set 𝜔 subscript 𝐶 𝜆 formulae-sequence 𝜔 𝑖 𝑗 𝜔 𝑗 𝑘 \{\omega\in C_{\lambda}:\omega(i)=j,\omega(j)=k\} for each k ∈ [n] ∖ { i, j } 𝑘 delimited-[] 𝑛 𝑖 𝑗 k\in[n]\setminus\{i,j\}, and hence each of these disjoint sets has the same size. Additionally, τ i ​ j subscript 𝜏 𝑖 𝑗 \tau_{ij} induces a bijection between { ω ∈ C λ: ω ​ ( i) = j, ω ​ ( j) = k } conditional-set 𝜔 subscript 𝐶 𝜆 formulae-sequence 𝜔 𝑖 𝑗 𝜔 𝑗 𝑘 \{\omega\in C_{\lambda}:\omega(i)=j,\omega(j)=k\} and { ω ∈ C λ: ω ​ ( i) = k, ω ​ ( j) = i } conditional-set 𝜔 subscript 𝐶 𝜆 formulae-sequence 𝜔 𝑖 𝑘 𝜔 𝑗 𝑖 \{\omega\in C_{\lambda}:\omega(i)=k,\omega(j)=i\}. Combining these two observations, we see that grouping elements by the images of i 𝑖 i and j 𝑗 j partitions Ω 4 subscript Ω 4 \Omega_{4} into 2 ​ ( n − 2) 2 𝑛 2 2(n-2) sets of the same size. Observe that the images of i 𝑖 i and j 𝑗 j are sufficient for determining if ( i, j) ∈ Inv ⁡ ( w) 𝑖 𝑗 Inv 𝑤 (i,j)\in\operatorname{Inv}(w). When ω ​ ( i) = j 𝜔 𝑖 𝑗 \omega(i)=j, ω ​ ( j) 𝜔 𝑗 \omega(j) must be in { 1, 2, …, j − 1 } ∖ { i } 1 2 … 𝑗 1 𝑖 \{1,2,\ldots,j-1\}\setminus\{i\} to have an inversion at ( i, j) 𝑖 𝑗 (i,j). When ω ​ ( j) = i 𝜔 𝑗 𝑖 \omega(j)=i, ω ​ ( i) 𝜔 𝑖 \omega(i) must be in { i + 1, …, n } ∖ { j } 𝑖 1 … 𝑛 𝑗 \{i+1,\ldots,n\}\setminus\{j\} to have an inversion at ( i, j) 𝑖 𝑗 (i,j). Hence,

 | Pr λ ⁡ [( i, j) ∈ Inv ⁡ ( ω) | ω ∈ Ω 4] = ( j − 2) + ( n − i − 1) 2 ​ ( n − 2) = ( n − 2) + ( j − i − 1) 2 ​ ( n − 2) = 1 2 + j − i − 1 2 ​ ( n − 2). subscript Pr 𝜆 𝑖 𝑗 conditional Inv 𝜔 𝜔 subscript Ω 4 𝑗 2 𝑛 𝑖 1 2 𝑛 2 𝑛 2 𝑗 𝑖 1 2 𝑛 2 1 2 𝑗 𝑖 1 2 𝑛 2 \begin{split}\operatorname{Pr}_{\lambda}[(i,j)\in\operatorname{Inv}(\omega)|\omega\in\Omega_{4}]=\frac{(j-2)+(n-i-1)}{2(n-2)}=\frac{(n-2)+(j-i-1)}{2(n-2)}=\frac{1}{2}+\frac{j-i-1}{2(n-2)}.\end{split} |  |

5. 5.

We can again partition Ω 5 subscript Ω 5 \Omega_{5} into 2 ​ ( n − 2) 2 𝑛 2 2(n-2) sets of the same size based on the image of i 𝑖 i and j 𝑗 j. If ω ​ ( i) = i 𝜔 𝑖 𝑖 \omega(i)=i, ω ​ ( j) 𝜔 𝑗 \omega(j) must be in { 1, 2, …, i − 1 } 1 2 … 𝑖 1 \{1,2,\ldots,i-1\} to produce an inversion at ( i, j) 𝑖 𝑗 (i,j). If ω ​ ( j) = j 𝜔 𝑗 𝑗 \omega(j)=j, then ω ​ ( i) 𝜔 𝑖 \omega(i) must be in { j + 1, …, n } 𝑗 1 … 𝑛 \{j+1,\ldots,n\} to produce an inversion at ( i, j) 𝑖 𝑗 (i,j). Hence,

 | Pr λ ⁡ [( i, j) ∈ Inv ⁡ ( ω) | ω ∈ Ω 5] = ( i − 1) + ( n − j) 2 ​ ( n − 2) = ( n − 2) + ( 1 + i − j) 2 ​ ( n − 2) = 1 2 − j − i − 1 2 ​ ( n − 2). ∎ subscript Pr 𝜆 𝑖 𝑗 conditional Inv 𝜔 𝜔 subscript Ω 5 𝑖 1 𝑛 𝑗 2 𝑛 2 𝑛 2 1 𝑖 𝑗 2 𝑛 2 1 2 𝑗 𝑖 1 2 𝑛 2 \begin{split}\operatorname{Pr}_{\lambda}[(i,j)\in\operatorname{Inv}(\omega)|\omega\in\Omega_{5}]&=\frac{(i-1)+(n-j)}{2(n-2)}=\frac{(n-2)+(1+i-j)}{2(n-2)}=\frac{1}{2}-\frac{j-i-1}{2(n-2)}.\qed\end{split} |  |

We have now established explicit formulas for all of the quantities in ( 4.2). Combining these, we compute the expected value of I i, j subscript 𝐼 𝑖 𝑗 I_{i,j} on C λ subscript 𝐶 𝜆 C_{\lambda}.

###### Lemma 4.7.

Let λ = ( 1 a 1, 2 a 2, …, n a n) ⊢ n proves 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 𝑛 \lambda=(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}})\vdash n. For any i < j 𝑖 𝑗 i<j in [n] delimited-[] 𝑛 [n],

 | Pr λ ⁡ [I i, j = 1] = 1 2 + a 2 n ​ ( n − 1) − a 1 ​ ( a 1 − 1) 2 ​ n ​ ( n − 1) + ( j − i − 1) ⋅ n − n ​ a 1 − a 1 + a 1 2 − 2 ​ a 2 n ​ ( n − 1) ​ ( n − 2). subscript Pr 𝜆 subscript 𝐼 𝑖 𝑗 1 1 2 subscript 𝑎 2 𝑛 𝑛 1 subscript 𝑎 1 subscript 𝑎 1 1 2 𝑛 𝑛 1 ⋅ 𝑗 𝑖 1 𝑛 𝑛 subscript 𝑎 1 subscript 𝑎 1 superscript subscript 𝑎 1 2 2 subscript 𝑎 2 𝑛 𝑛 1 𝑛 2 \begin{split}\operatorname{Pr}_{\lambda}[I_{i,j}=1]=\frac{1}{2}+\frac{a_{2}}{n(n-1)}-\frac{a_{1}(a_{1}-1)}{2n(n-1)}+(j-i-1)\cdot\frac{n-na_{1}-a_{1}+a_{1}^{2}-2a_{2}}{n(n-1)(n-2)}.\end{split} |  |

###### Proof.

Define Ω k = Ω k i ​ j subscript Ω 𝑘 superscript subscript Ω 𝑘 𝑖 𝑗 \Omega_{k}=\Omega_{k}^{ij} as in ( 4.2). Starting with ( 4.3) and using Lemma 4.5, Pr λ ⁡ [I i, j = 1] subscript Pr 𝜆 subscript 𝐼 𝑖 𝑗 1 \operatorname{Pr}_{\lambda}[I_{i,j}=1] can be expressed as a sum of the following five terms:

1. (i)

Pr λ ⁡ [ω ∈ Ω 1] ⋅ 1 2 ⋅ subscript Pr 𝜆 𝜔 subscript Ω 1 1 2 \operatorname{Pr}_{\lambda}[\omega\in\Omega_{1}]\cdot\frac{1}{2},

2. (ii)

Pr λ ⁡ [ω ∈ Ω 2] ⋅ ( 1 2 + 1 2) ⋅ subscript Pr 𝜆 𝜔 subscript Ω 2 1 2 1 2 \operatorname{Pr}_{\lambda}[\omega\in\Omega_{2}]\cdot\left(\frac{1}{2}+\frac{1}{2}\right),

3. (iii)

Pr λ ⁡ [ω ∈ Ω 3] ⋅ ( 1 2 − 1 2) ⋅ subscript Pr 𝜆 𝜔 subscript Ω 3 1 2 1 2 \operatorname{Pr}_{\lambda}[\omega\in\Omega_{3}]\cdot\left(\frac{1}{2}-\frac{1}{2}\right),

4. (iv)

Pr λ ⁡ [ω ∈ Ω 4] ⋅ ( 1 2 + j − i − 1 2 ​ ( n − 2)) ⋅ subscript Pr 𝜆 𝜔 subscript Ω 4 1 2 𝑗 𝑖 1 2 𝑛 2 \operatorname{Pr}_{\lambda}[\omega\in\Omega_{4}]\cdot\left(\frac{1}{2}+\frac{j-i-1}{2(n-2)}\right), and

5. (v)

Pr λ ⁡ [ω ∈ Ω 5] ⋅ ( 1 2 − j − i − 1 2 ​ ( n − 2)) ⋅ subscript Pr 𝜆 𝜔 subscript Ω 5 1 2 𝑗 𝑖 1 2 𝑛 2 \operatorname{Pr}_{\lambda}[\omega\in\Omega_{5}]\cdot\left(\frac{1}{2}-\frac{j-i-1}{2(n-2)}\right).

We group terms with positive 1 / 2 1 2 1/2 coefficients, use the fact that C λ subscript 𝐶 𝜆 C_{\lambda} is a disjoint union of { Ω k } k = 1 5 superscript subscript subscript Ω 𝑘 𝑘 1 5 \{\Omega_{k}\}_{k=1}^{5}, and apply Lemma 4.3 to obtain

 | 1 2 ​ ∑ k = 1 5 Pr λ ⁡ [ω ∈ Ω k] + 1 2 ​ Pr λ ⁡ [ω ∈ Ω 2] − 1 2 ​ Pr λ ⁡ [ω ∈ Ω 3] + j − i − 1 2 ​ ( n − 2) ​ Pr λ ⁡ [ω ∈ Ω 4] − j − i − 1 2 ​ ( n − 2) ​ Pr λ ⁡ [ω ∈ Ω 5] = 1 2 + a 2 n ​ ( n − 1) − a 1 ​ ( a 1 − 1) 2 ​ n ​ ( n − 1) + j − i − 1 ( n − 1) ​ ( n − 2) ​ ( 1 − a 1 n − 2 ​ a 2 n) − a 1 ​ ( j − i − 1) n ​ ( n − 2) ​ ( 1 − a 1 − 1 n − 1). = 1 2 + a 2 n ​ ( n − 1) − a 1 ​ ( a 1 − 1) 2 ​ n ​ ( n − 1) + ( j − i − 1) ⋅ n − n ​ a 1 − a 1 + a 1 2 − 2 ​ a 2 n ​ ( n − 1) ​ ( n − 2). ∎ \begin{split}&\frac{1}{2}\sum_{k=1}^{5}\operatorname{Pr}_{\lambda}[\omega\in\Omega_{k}]+\frac{1}{2}\operatorname{Pr}_{\lambda}[\omega\in\Omega_{2}]-\frac{1}{2}\operatorname{Pr}_{\lambda}[\omega\in\Omega_{3}]+\frac{j-i-1}{2(n-2)}\operatorname{Pr}_{\lambda}[\omega\in\Omega_{4}]-\frac{j-i-1}{2(n-2)}\operatorname{Pr}_{\lambda}[\omega\in\Omega_{5}]\\ &=\frac{1}{2}+\frac{a_{2}}{n(n-1)}-\frac{a_{1}(a_{1}-1)}{2n(n-1)}+\frac{j-i-1}{(n-1)(n-2)}\left(1-\frac{a_{1}}{n}-\frac{2a_{2}}{n}\right)-\frac{a_{1}(j-i-1)}{n(n-2)}\left(1-\frac{a_{1}-1}{n-1}\right).\\ &=\frac{1}{2}+\frac{a_{2}}{n(n-1)}-\frac{a_{1}(a_{1}-1)}{2n(n-1)}+(j-i-1)\cdot\frac{n-na_{1}-a_{1}+a_{1}^{2}-2a_{2}}{n(n-1)(n-2)}.\qed\end{split} |  |

### 4.2 First moment

We now apply our results on 𝔼 λ ​ [I i, j] subscript 𝔼 𝜆 delimited-[] subscript 𝐼 𝑖 𝑗 \mathbb{E}_{\lambda}[I_{i,j}] to calculate 𝔼 λ ​ [X] subscript 𝔼 𝜆 delimited-[] 𝑋 \mathbb{E}_{\lambda}[X] for any weighted inversion statistic. We start with our main theorem on weighted inversion statistics.

###### Theorem 4.8.

Let λ = ( 1 a 1, 2 a 2, …, n a n) ⊢ n proves 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 𝑛 \lambda=(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}})\vdash n, and let X = ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) ​ I i, j 𝑋 subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 subscript 𝐼 𝑖 𝑗 X=\sum_{1\leq i<j\leq n}\text{wt}(i,j)I_{i,j} be a weighted inversion statistic. Also set α n ​ ( X):= ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) assign subscript 𝛼 𝑛 𝑋 subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 \alpha_{n}(X):=\sum_{1\leq i<j\leq n}\text{wt}(i,j), and β n ​ ( X):= ∑ 1 ≤ i < j ≤ n ( j − i − 1) ​ wt ​ ( i, j) assign subscript 𝛽 𝑛 𝑋 subscript 1 𝑖 𝑗 𝑛 𝑗 𝑖 1 wt 𝑖 𝑗 \beta_{n}(X):=\sum_{1\leq i<j\leq n}(j-i-1)\text{wt}(i,j). Then

 | 𝔼 λ ​ [X] = ( 1 2 + a 2 n ​ ( n − 1) − a 1 ​ ( a 1 − 1) 2 ​ n ​ ( n − 1)) ⋅ α n ​ ( X) + ( n − n ​ a 1 − a 1 + a 1 2 − 2 ​ a 2 n ​ ( n − 1) ​ ( n − 2)) ⋅ β n ​ ( X). subscript 𝔼 𝜆 delimited-[] 𝑋 ⋅ 1 2 subscript 𝑎 2 𝑛 𝑛 1 subscript 𝑎 1 subscript 𝑎 1 1 2 𝑛 𝑛 1 subscript 𝛼 𝑛 𝑋 ⋅ 𝑛 𝑛 subscript 𝑎 1 subscript 𝑎 1 superscript subscript 𝑎 1 2 2 subscript 𝑎 2 𝑛 𝑛 1 𝑛 2 subscript 𝛽 𝑛 𝑋 \mathbb{E}_{\lambda}[X]=\left(\frac{1}{2}+\frac{a_{2}}{n(n-1)}-\frac{a_{1}(a_{1}-1)}{2n(n-1)}\right)\cdot\alpha_{n}(X)+\left(\frac{n-na_{1}-a_{1}+a_{1}^{2}-2a_{2}}{n(n-1)(n-2)}\right)\cdot\beta_{n}(X). |  |

###### Proof.

Note that α n ​ ( X) subscript 𝛼 𝑛 𝑋 \alpha_{n}(X) and β n ​ ( X) subscript 𝛽 𝑛 𝑋 \beta_{n}(X) are independent of the partition λ 𝜆 \lambda. We start with ( 4.1) and apply Lemma 4.7 to see that 𝔼 λ ​ [X] subscript 𝔼 𝜆 delimited-[] 𝑋 \mathbb{E}_{\lambda}[X] is given by

 | ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) ​ Pr λ ⁡ [I i, j ​ ( ω) = 1] = ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) ​ ( 1 2 + a 2 n ​ ( n − 1) − a 1 ​ ( a 1 − 1) 2 ​ n ​ ( n − 1) + ( j − i − 1) ⋅ n − n ​ a 1 − a 1 + a 1 2 − 2 ​ a 2 n ​ ( n − 1) ​ ( n − 2)) = ( 1 2 + a 2 n ​ ( n − 1) − a 1 ​ ( a 1 − 1) 2 ​ n ​ ( n − 1)) ⋅ ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) + ( n − n ​ a 1 − a 1 + a 1 2 − 2 ​ a 2 n ​ ( n − 1) ​ ( n − 2)) ⋅ ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) ​ ( j − i − 1). ∎ subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 subscript Pr 𝜆 subscript 𝐼 𝑖 𝑗 𝜔 1 subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 1 2 subscript 𝑎 2 𝑛 𝑛 1 subscript 𝑎 1 subscript 𝑎 1 1 2 𝑛 𝑛 1 ⋅ 𝑗 𝑖 1 𝑛 𝑛 subscript 𝑎 1 subscript 𝑎 1 superscript subscript 𝑎 1 2 2 subscript 𝑎 2 𝑛 𝑛 1 𝑛 2 ⋅ 1 2 subscript 𝑎 2 𝑛 𝑛 1 subscript 𝑎 1 subscript 𝑎 1 1 2 𝑛 𝑛 1 subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 ⋅ 𝑛 𝑛 subscript 𝑎 1 subscript 𝑎 1 superscript subscript 𝑎 1 2 2 subscript 𝑎 2 𝑛 𝑛 1 𝑛 2 subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 𝑗 𝑖 1 \begin{split}&\sum_{1\leq i<j\leq n}\text{wt}(i,j)\operatorname{Pr}_{\lambda}[I_{i,j}(\omega)=1]\\ &=\sum_{1\leq i<j\leq n}\text{wt}(i,j)\left(\frac{1}{2}+\frac{a_{2}}{n(n-1)}-\frac{a_{1}(a_{1}-1)}{2n(n-1)}+(j-i-1)\cdot\frac{n-na_{1}-a_{1}+a_{1}^{2}-2a_{2}}{n(n-1)(n-2)}\right)\\ &=\left(\frac{1}{2}+\frac{a_{2}}{n(n-1)}-\frac{a_{1}(a_{1}-1)}{2n(n-1)}\right)\cdot\sum_{1\leq i<j\leq n}\text{wt}(i,j)+\left(\frac{n-na_{1}-a_{1}+a_{1}^{2}-2a_{2}}{n(n-1)(n-2)}\right)\cdot\sum_{1\leq i<j\leq n}\text{wt}(i,j)(j-i-1).\qed\end{split} |  |

###### Corollary 4.9.

Let λ = ( 1 a 1, 2 a 2, …, n a n) ⊢ n proves 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 𝑛 \lambda=(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}})\vdash n. The expected value of any weighted inversion statistic in S n subscript 𝑆 𝑛 S_{n} is independent of a 3, …, a n subscript 𝑎 3 … subscript 𝑎 𝑛 a_{3},\ldots,a_{n}.

We can apply the preceding theorem to obtain the expected number of some common statistics. Note that part (1) of the following corollary was previously established by Fulman [Ful98].

###### Corollary 4.10.

Let λ = ( 1 a 1, 2 a 2, …, n a n) ⊢ n proves 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 𝑛 \lambda=(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}})\vdash n, n ≥ 2 𝑛 2 n\geq 2. Then

1. 1.

𝔼 λ ​ [des] = 1 2 ​ n ​ ( n 2 − n + 2 ​ a 2 − a 1 2 + a 1) subscript 𝔼 𝜆 delimited-[] des 1 2 𝑛 superscript 𝑛 2 𝑛 2 subscript 𝑎 2 superscript subscript 𝑎 1 2 subscript 𝑎 1 \mathbb{E}_{\lambda}[\operatorname{des}]=\frac{1}{2n}\left(n^{2}-n+2a_{2}-a_{1}^{2}+a_{1}\right),

2. 2.

𝔼 λ ​ [maj] = 1 4 ​ ( n 2 − n + 2 ​ a 2 − a 1 2 + a 1), subscript 𝔼 𝜆 delimited-[] maj 1 4 superscript 𝑛 2 𝑛 2 subscript 𝑎 2 superscript subscript 𝑎 1 2 subscript 𝑎 1 \mathbb{E}_{\lambda}[\operatorname{maj}]=\frac{1}{4}\left(n^{2}-n+2a_{2}-a_{1}^{2}+a_{1}\right),

3. 3.

𝔼 λ ​ [inv] = 1 12 ​ ( 3 ​ n 2 − n + 2 ​ a 2 − a 1 2 + a 1 − 2 ​ n ​ a 1). subscript 𝔼 𝜆 delimited-[] inv 1 12 3 superscript 𝑛 2 𝑛 2 subscript 𝑎 2 superscript subscript 𝑎 1 2 subscript 𝑎 1 2 𝑛 subscript 𝑎 1 \mathbb{E}_{\lambda}[\operatorname{inv}]=\frac{1}{12}\left(3n^{2}-n+2a_{2}-a_{1}^{2}+a_{1}-2na_{1}\right).

In particular, in the case that a 1 = a 2 = 0 subscript 𝑎 1 subscript 𝑎 2 0 a_{1}=a_{2}=0, we have that 𝔼 λ ​ [des] = n − 1 2 subscript 𝔼 𝜆 delimited-[] des 𝑛 1 2 \mathbb{E}_{\lambda}[\operatorname{des}]=\frac{n-1}{2}, 𝔼 λ ​ [maj] = n ​ ( n − 1) 4 subscript 𝔼 𝜆 delimited-[] maj 𝑛 𝑛 1 4 \mathbb{E}_{\lambda}[\operatorname{maj}]=\frac{n(n-1)}{4}, and 𝔼 λ ​ [inv] = 3 ​ n 2 − n 12 subscript 𝔼 𝜆 delimited-[] inv 3 superscript 𝑛 2 𝑛 12 \mathbb{E}_{\lambda}[\operatorname{inv}]=\frac{3n^{2}-n}{12}.

###### Proof.

We use Theorem 4.8 for all three statistics X 𝑋 X.

1. 1.

The descent statistic des des \operatorname{des} is defined by wt ​ ( i, i + 1) = 1 wt 𝑖 𝑖 1 1 \text{wt}(i,i+1)=1 for i ∈ { 1, 2, …, n − 1 } 𝑖 1 2 … 𝑛 1 i\in\{1,2,\ldots,n-1\}, and wt ​ ( i, j) = 0 wt 𝑖 𝑗 0 \text{wt}(i,j)=0 otherwise. Hence α n ​ ( X) = subscript 𝛼 𝑛 𝑋 absent \alpha_{n}(X)= ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) = ( n − 1) subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 𝑛 1 \sum_{1\leq i<j\leq n}\text{wt}(i,j)=(n-1) and β n ​ ( X) = subscript 𝛽 𝑛 𝑋 absent \beta_{n}(X)= ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) ​ ( j − i − 1) = 0 subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 𝑗 𝑖 1 0 \sum_{1\leq i<j\leq n}\text{wt}(i,j)(j-i-1)=0. Then

 | 𝔼 λ ​ [des] = ( 1 2 + a 2 n ​ ( n − 1) − a 1 ​ ( a 1 − 1) 2 ​ n ​ ( n − 1)) ⋅ ( n − 1) = 1 2 ​ n ​ ( n 2 − n + 2 ​ a 2 − a 1 2 + a 1). subscript 𝔼 𝜆 delimited-[] des ⋅ 1 2 subscript 𝑎 2 𝑛 𝑛 1 subscript 𝑎 1 subscript 𝑎 1 1 2 𝑛 𝑛 1 𝑛 1 1 2 𝑛 superscript 𝑛 2 𝑛 2 subscript 𝑎 2 superscript subscript 𝑎 1 2 subscript 𝑎 1 \mathbb{E}_{\lambda}[\operatorname{des}]=\left(\frac{1}{2}+\frac{a_{2}}{n(n-1)}-\frac{a_{1}(a_{1}-1)}{2n(n-1)}\right)\cdot(n-1)=\frac{1}{2n}{\left(n^{2}-n+2a_{2}-a_{1}^{2}+a_{1}\right)}. |  |

2. 2.

The major index is defined by wt ​ ( i, i + 1) = i wt 𝑖 𝑖 1 𝑖 \text{wt}(i,i+1)=i and wt ​ ( i, j) = 0 wt 𝑖 𝑗 0 \text{wt}(i,j)=0 otherwise. Now α n ​ ( X) = subscript 𝛼 𝑛 𝑋 absent \alpha_{n}(X)= ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) = ( n 2) subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 binomial 𝑛 2 \sum_{1\leq i<j\leq n}\text{wt}(i,j)={n\choose 2} and β n ​ ( X) = subscript 𝛽 𝑛 𝑋 absent \beta_{n}(X)= ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) ​ ( j − i − 1) = 0 subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 𝑗 𝑖 1 0 \sum_{1\leq i<j\leq n}\text{wt}(i,j)(j-i-1)=0. Then

 | 𝔼 λ ​ [maj] = ( 1 2 + a 2 n ​ ( n − 1) − a 1 ​ ( a 1 − 1) 2 ​ n ​ ( n − 1)) ⋅ ( n 2) = 1 4 ​ ( n 2 − n + 2 ​ a 2 − a 1 2 + a 1). subscript 𝔼 𝜆 delimited-[] maj ⋅ 1 2 subscript 𝑎 2 𝑛 𝑛 1 subscript 𝑎 1 subscript 𝑎 1 1 2 𝑛 𝑛 1 binomial 𝑛 2 1 4 superscript 𝑛 2 𝑛 2 subscript 𝑎 2 superscript subscript 𝑎 1 2 subscript 𝑎 1 \mathbb{E}_{\lambda}[\operatorname{maj}]=\left(\frac{1}{2}+\frac{a_{2}}{n(n-1)}-\frac{a_{1}(a_{1}-1)}{2n(n-1)}\right)\cdot{n\choose 2}=\frac{1}{4}\left(n^{2}-n+2a_{2}-a_{1}^{2}+a_{1}\right). |  |

3. 3.

Finally, the inversion statistic is defined by wt ​ ( i, j) = 1 wt 𝑖 𝑗 1 \text{wt}(i,j)=1 for all i, j 𝑖 𝑗 i,j. Then α n ​ ( X) = subscript 𝛼 𝑛 𝑋 absent \alpha_{n}(X)= ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) = ( n 2) subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 binomial 𝑛 2 \sum_{1\leq i<j\leq n}\text{wt}(i,j)={n\choose 2}, and using the substitution k = j − i − 1 𝑘 𝑗 𝑖 1 k=j-i-1, we find that β n ​ ( X) = subscript 𝛽 𝑛 𝑋 absent \beta_{n}(X)= ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) ​ ( j − i − 1) subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 𝑗 𝑖 1 \sum_{1\leq i<j\leq n}\text{wt}(i,j)(j-i-1) is given by

 | ∑ 1 ≤ i < j ≤ n ( j − i − 1) = ∑ i = 1 n − 1 ∑ k = 0 n − i − 1 k = ∑ i = 1 n − 1 ( n − i 2) = ( n 3). subscript 1 𝑖 𝑗 𝑛 𝑗 𝑖 1 superscript subscript 𝑖 1 𝑛 1 superscript subscript 𝑘 0 𝑛 𝑖 1 𝑘 superscript subscript 𝑖 1 𝑛 1 binomial 𝑛 𝑖 2 binomial 𝑛 3 \begin{split}\sum_{1\leq i<j\leq n}(j-i-1)=\sum_{i=1}^{n-1}\sum_{k=0}^{n-i-1}k=\sum_{i=1}^{n-1}\binom{n-i}{2}=\binom{n}{3}.\end{split} |  |

Combined, we see that

 | 𝔼 λ ​ [inv] = ( 1 2 + a 2 n ​ ( n − 1) − a 1 ​ ( a 1 − 1) 2 ​ n ​ ( n − 1)) ⋅ ( n 2) + ( n − n ​ a 1 − a 1 + a 1 2 − 2 ​ a 2 n ​ ( n − 1) ​ ( n − 2)) ⋅ ( n 3) = 1 12 ​ ( 3 ​ n 2 − n + 2 ​ a 2 − a 1 2 + a 1 − 2 ​ n ​ a 1). ∎ subscript 𝔼 𝜆 delimited-[] inv ⋅ 1 2 subscript 𝑎 2 𝑛 𝑛 1 subscript 𝑎 1 subscript 𝑎 1 1 2 𝑛 𝑛 1 binomial 𝑛 2 ⋅ 𝑛 𝑛 subscript 𝑎 1 subscript 𝑎 1 superscript subscript 𝑎 1 2 2 subscript 𝑎 2 𝑛 𝑛 1 𝑛 2 binomial 𝑛 3 1 12 3 superscript 𝑛 2 𝑛 2 subscript 𝑎 2 superscript subscript 𝑎 1 2 subscript 𝑎 1 2 𝑛 subscript 𝑎 1 \begin{split}\mathbb{E}_{\lambda}[\operatorname{inv}]&=\left(\frac{1}{2}+\frac{a_{2}}{n(n-1)}-\frac{a_{1}(a_{1}-1)}{2n(n-1)}\right)\cdot{n\choose 2}+\left(\frac{n-na_{1}-a_{1}+a_{1}^{2}-2a_{2}}{n(n-1)(n-2)}\right)\cdot{n\choose 3}\\ &=\frac{1}{12}\left(3n^{2}-n+2a_{2}-a_{1}^{2}+a_{1}-2na_{1}\right).\qed\end{split} |  |

### 4.3 Baj

In this subsection, we consider the curious permutation statistic baj baj \operatorname{baj} that was introduced by Zabrocki [Zab03].

###### Definition 4.11 ( [Zab03]).

Let ω ∈ S n 𝜔 subscript 𝑆 𝑛 \omega\in S_{n}. Define

 | baj ⁡ ( ω) ≔ ∑ i ∈ Des ⁡ ( ω) i ​ ( n − i). ≔ baj 𝜔 subscript 𝑖 Des 𝜔 𝑖 𝑛 𝑖 \operatorname{baj}(\omega)\coloneqq\sum_{i\in\operatorname{Des}(\omega)}i(n-i). |  |

The statistic baj − inv baj inv \operatorname{baj}-\operatorname{inv} is the Coxeter length function restricted to coset representatives of the extended affine Weyl group of type A n − 1 subscript 𝐴 𝑛 1 A_{n-1} modulo translations by coroots. It has a nice generating function over the symmetric group, due to Stembridge and Waugh [SW98]. Furthermore, in [BKS20], using this generating function, a formula for the d 𝑑 d th cumulant is given [BKS20, Corollary 3.4], and it is shown that the asymptotic distribution of baj − inv baj inv \operatorname{baj}-\operatorname{inv} on S n subscript 𝑆 𝑛 S_{n} is normal.

Observe that baj baj \operatorname{baj} is a weighted inversion statistic for the choice wt ​ ( i, i + 1) = i ​ ( n − i) wt 𝑖 𝑖 1 𝑖 𝑛 𝑖 \text{wt}(i,i+1)=i(n-i) and wt ​ ( i, j) = 0 wt 𝑖 𝑗 0 \text{wt}(i,j)=0 for j ≠ i + 1 𝑗 𝑖 1 j\neq i+1. Using Theorem 4.8, we obtain the following.

###### Proposition 4.12.

Let λ = ( 1 a 1, 2 a 2, …, n a n) ⊢ n proves 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 𝑛 \lambda=(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}})\vdash n, n ≥ 2 𝑛 2 n\geq 2. Then

 | 𝔼 λ ​ [baj] = 1 12 ​ ( n + 1) ​ ( n 2 − n + 2 ​ a 2 − a 1 2 + a 1) = 1 3 ​ ( n + 1) ​ 𝔼 λ ​ [maj]. subscript 𝔼 𝜆 delimited-[] baj 1 12 𝑛 1 superscript 𝑛 2 𝑛 2 subscript 𝑎 2 superscript subscript 𝑎 1 2 subscript 𝑎 1 1 3 𝑛 1 subscript 𝔼 𝜆 delimited-[] maj \mathbb{E}_{\lambda}[\operatorname{baj}]=\frac{1}{12}(n+1)(n^{2}-n+2a_{2}-a_{1}^{2}+a_{1})=\frac{1}{3}(n+1)\mathbb{E}_{\lambda}[\operatorname{maj}]. |  |

### 4.4 Cyclic descents

Cyclic descents were introduced by Paola Cellini [Cel98]. While these are not weighted inversion statistics, a small adjustment of the methods of the previous subsections allows us to compute the first moment of cyclic descents on C λ subscript 𝐶 𝜆 C_{\lambda}.

###### Definition 4.13 ( [Cel98]).

The *cyclic descent set*of a permutation ω ∈ S n 𝜔 subscript 𝑆 𝑛 \omega\in S_{n} is defined to be the set

 | cDes ⁡ ( ω):= { 1 ≤ i ≤ n: ω ​ ( i) > ω ​ ( i + 1) ⊂ [n] }, assign cDes 𝜔 conditional-set 1 𝑖 𝑛 𝜔 𝑖 𝜔 𝑖 1 delimited-[] 𝑛 \operatorname{cDes}(\omega):=\{1\leq i\leq n:\omega(i)>\omega(i+1)\subset[n]\}, |  |

with the convention ω ​ ( n + 1):= ω ​ ( 1) assign 𝜔 𝑛 1 𝜔 1 \omega(n+1):=\omega(1). Let cdes ⁡ ( ω):= | cDes ⁡ ( ω) |. assign cdes 𝜔 cDes 𝜔 \operatorname{cdes}(\omega):=|\operatorname{cDes}(\omega)|.

###### Theorem 4.14.

Let λ = ( 1 a 1, 2 a 2, …, n a n) ⊢ n proves 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 𝑛 \lambda=(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}})\vdash n, n ≥ 2 𝑛 2 n\geq 2. Then

 | 𝔼 λ ​ [cdes] = n 2 + a 2 − ( a 1 2) n − 1 + a 1 − 1 n − 1, subscript 𝔼 𝜆 delimited-[] cdes 𝑛 2 subscript 𝑎 2 binomial subscript 𝑎 1 2 𝑛 1 subscript 𝑎 1 1 𝑛 1 \mathbb{E}_{\lambda}[\operatorname{cdes}]=\frac{n}{2}+\frac{a_{2}-\binom{a_{1}}{2}}{n-1}+\frac{a_{1}-1}{n-1}, |  |

and hence the expected value of cyclic descents is independent of the conjugacy class if a 1 = a 2 = 0 subscript 𝑎 1 subscript 𝑎 2 0 a_{1}=a_{2}=0.

###### Proof.

Writing J n subscript 𝐽 𝑛 J_{n} for the random variable which equals 1 if n ∈ cDes ⁡ ( ω) 𝑛 cDes 𝜔 n\in\operatorname{cDes}(\omega) and 0 otherwise, we have

 | 𝔼 λ ​ [cdes] = ∑ 1 ≤ i ≤ n − 1 Pr λ ⁡ [I i, i + 1 = 1] + Pr λ ⁡ [J n = 1] = 𝔼 λ ​ [des] + Pr λ ⁡ [J n = 1]. subscript 𝔼 𝜆 delimited-[] cdes subscript 1 𝑖 𝑛 1 subscript Pr 𝜆 subscript 𝐼 𝑖 𝑖 1 1 subscript Pr 𝜆 subscript 𝐽 𝑛 1 subscript 𝔼 𝜆 delimited-[] des subscript Pr 𝜆 subscript 𝐽 𝑛 1 \mathbb{E}_{\lambda}[\operatorname{cdes}]=\sum_{1\leq i\leq n-1}\operatorname{Pr}_{\lambda}[I_{i,i+1}=1]+\operatorname{Pr}_{\lambda}[J_{n}=1]\\ =\mathbb{E}_{\lambda}[\operatorname{des}]+\operatorname{Pr}_{\lambda}[J_{n}=1]. |  | (4.4) |

From Lemma 4.7 we have

 | Pr λ ⁡ [I 1, n = 1] = 1 2 + a 2 n ​ ( n − 1) − a 1 ​ ( a 1 − 1) 2 ​ n ​ ( n − 1) + n − n ​ a 1 − a 1 + a 1 2 − 2 ​ a 2 n ​ ( n − 1) = 1 2 + ( a 1 2) − a 2 − n ​ ( a 1 − 1) n ​ ( n − 1). subscript Pr 𝜆 subscript 𝐼 1 𝑛 1 1 2 subscript 𝑎 2 𝑛 𝑛 1 subscript 𝑎 1 subscript 𝑎 1 1 2 𝑛 𝑛 1 𝑛 𝑛 subscript 𝑎 1 subscript 𝑎 1 superscript subscript 𝑎 1 2 2 subscript 𝑎 2 𝑛 𝑛 1 1 2 binomial subscript 𝑎 1 2 subscript 𝑎 2 𝑛 subscript 𝑎 1 1 𝑛 𝑛 1 \operatorname{Pr}_{\lambda}[I_{1,n}=1]=\frac{1}{2}+\frac{a_{2}}{n(n-1)}-\frac{a_{1}(a_{1}-1)}{2n(n-1)}+\frac{n-na_{1}-a_{1}+a_{1}^{2}-2a_{2}}{n(n-1)}=\frac{1}{2}+\frac{\binom{a_{1}}{2}-a_{2}-n(a_{1}-1)}{n(n-1)}. |  |

Now n 𝑛 n is a cyclic descent if and only if ω ​ ( n) > ω ​ ( 1) 𝜔 𝑛 𝜔 1 \omega(n)>\omega(1), i.e., if and only if ( 1, n) 1 𝑛 (1,n) is *not*an inversion. Hence we have

 | Pr λ ⁡ [J n = 1] = 1 − Pr λ ⁡ [I 1, n = 1] = 1 2 + a 2 − ( a 1 2) + n ​ ( a 1 − 1) n ​ ( n − 1). subscript Pr 𝜆 subscript 𝐽 𝑛 1 1 subscript Pr 𝜆 subscript 𝐼 1 𝑛 1 1 2 subscript 𝑎 2 binomial subscript 𝑎 1 2 𝑛 subscript 𝑎 1 1 𝑛 𝑛 1 \begin{split}\operatorname{Pr}_{\lambda}[J_{n}=1]=1-\operatorname{Pr}_{\lambda}[I_{1,n}=1]=\frac{1}{2}+\frac{a_{2}-\binom{a_{1}}{2}+n(a_{1}-1)}{n(n-1)}.\end{split} |  | (4.5) |

From Corollary 4.10, we have

 | 𝔼 λ ​ [des] = n − 1 2 + a 2 − ( a 1 2) n. subscript 𝔼 𝜆 delimited-[] des 𝑛 1 2 subscript 𝑎 2 binomial subscript 𝑎 1 2 𝑛 \mathbb{E}_{\lambda}[\operatorname{des}]=\frac{n-1}{2}+\frac{a_{2}-\binom{a_{1}}{2}}{n}. |  | (4.6) |

Equation ( 4.4) now gives the result. ∎

## 5 Cyclic permutation statistics

In this section, we apply the techniques from Section 4 to the cases of several other permutation statistics that are not weighted inversion statistics. Such permutation statistics include cyclic descents and excedances. We call these cyclic permutation statistics, to reflect the fact that, in general, the value of the statistic can be read directly from the cycles in its cycle decomposition.

In particular, we show that, once again, the expected values depend on at most the number of fixed points and 2 2 2 -cycles in the cycle type.

### 5.1 Excedances

An *excedance*of ω 𝜔 \omega is any index i ∈ [n] 𝑖 delimited-[] 𝑛 i\in[n] such that ω ​ ( i) > i 𝜔 𝑖 𝑖 \omega(i)>i. A *weak excedance*of ω 𝜔 \omega is any index i ∈ [n] 𝑖 delimited-[] 𝑛 i\in[n] such that ω ​ ( i) ≥ i 𝜔 𝑖 𝑖 \omega(i)\geq i. An *anti-excedance*[BS21] of ω 𝜔 \omega is any index i ∈ [n] 𝑖 delimited-[] 𝑛 i\in[n] such that ω ​ ( i) < i 𝜔 𝑖 𝑖 \omega(i)<i. Clearly i 𝑖 i is an excedance of ω 𝜔 \omega if and only if ω ​ ( i) 𝜔 𝑖 \omega(i) is an anti-excedance of ω − 1 superscript 𝜔 1 \omega^{-1}, and conjugacy classes in S n subscript 𝑆 𝑛 S_{n} are closed with respect to taking inverses, so for any fixed conjugacy class, excedance and anti-excedance are equidistributed.

Let exc ⁡ ( ω) exc 𝜔 \operatorname{exc}(\omega) (respectively exc ~ ​ ( ω), aexc ⁡ ( ω) ~ exc 𝜔 aexc 𝜔 \widetilde{\operatorname{exc}}(\omega),\operatorname{aexc}(\omega)) denote the number of excedances (respectively weak excedances, anti-excedances) of the permutation ω 𝜔 \omega. While these are not weighted inversion statistics, the methods of Section 4 can be adapted to calculate their expected values in C λ subscript 𝐶 𝜆 C_{\lambda}.

###### Theorem 5.1.

Let λ = ( 1 a 1, 2 a 2, …, n a n) 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 \lambda=(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}}). Then

 | 𝔼 λ ​ [exc] = 1 2 ​ ( n − a 1) = 𝔼 λ ​ [aexc] ​ and ​ 𝔼 λ ​ [exc ~] = 1 2 ​ ( n + a 1). subscript 𝔼 𝜆 delimited-[] exc 1 2 𝑛 subscript 𝑎 1 subscript 𝔼 𝜆 delimited-[] aexc and subscript 𝔼 𝜆 delimited-[] ~ exc 1 2 𝑛 subscript 𝑎 1 \mathbb{E}_{\lambda}[\operatorname{exc}]=\frac{1}{2}(n-a_{1})=\mathbb{E}_{\lambda}[\operatorname{aexc}]\text{ and }\mathbb{E}_{\lambda}[\widetilde{\operatorname{exc}}]=\frac{1}{2}(n+a_{1}). |  |

###### Proof.

Express exc ⁡ ( ω) = ∑ j = 1 n I j ​ ( ω) exc 𝜔 superscript subscript 𝑗 1 𝑛 subscript 𝐼 𝑗 𝜔 \operatorname{exc}(\omega)=\sum_{j=1}^{n}I_{j}(\omega), where I j subscript 𝐼 𝑗 I_{j} is the indicator random variable on an excedance at position j 𝑗 j. Fixing j 𝑗 j, partition C λ subscript 𝐶 𝜆 C_{\lambda} into the two sets Ω 1 = { w ∈ C λ: ω ​ ( j) = j } subscript Ω 1 conditional-set 𝑤 subscript 𝐶 𝜆 𝜔 𝑗 𝑗 \Omega_{1}=\{w\in C_{\lambda}:\omega(j)=j\} and Ω 2 = { w ∈ C λ: ω ​ ( j) ≠ j } subscript Ω 2 conditional-set 𝑤 subscript 𝐶 𝜆 𝜔 𝑗 𝑗 \Omega_{2}=\{w\in C_{\lambda}:\omega(j)\neq j\}. Then

 | Pr λ ⁡ [I j = 1] = Pr λ ⁡ [ω ∈ Ω 1] ⋅ Pr λ ⁡ [I j ​ ( ω) = 1 | ω ∈ Ω 1] + Pr λ ⁡ [ω ∈ Ω 2] ⋅ Pr λ ⁡ [I j ​ ( ω) = 1 | ω ∈ Ω 2]. subscript Pr 𝜆 subscript 𝐼 𝑗 1 ⋅ subscript Pr 𝜆 𝜔 subscript Ω 1 subscript Pr 𝜆 subscript 𝐼 𝑗 𝜔 conditional 1 𝜔 subscript Ω 1 ⋅ subscript Pr 𝜆 𝜔 subscript Ω 2 subscript Pr 𝜆 subscript 𝐼 𝑗 𝜔 conditional 1 𝜔 subscript Ω 2 \operatorname{Pr}_{\lambda}[I_{j}=1]=\operatorname{Pr}_{\lambda}[\omega\in\Omega_{1}]\cdot\operatorname{Pr}_{\lambda}[I_{j}(\omega)=1|\omega\in\Omega_{1}]+\operatorname{Pr}_{\lambda}[\omega\in\Omega_{2}]\cdot\operatorname{Pr}_{\lambda}[I_{j}(\omega)=1|\omega\in\Omega_{2}]. |  |

Observe that Pr λ ⁡ [ω ∈ Ω 1] = a 1 n subscript Pr 𝜆 𝜔 subscript Ω 1 subscript 𝑎 1 𝑛 \operatorname{Pr}_{\lambda}[\omega\in\Omega_{1}]=\frac{a_{1}}{n} and Pr λ ⁡ [I j ​ ( ω) = 1 | ω ∈ Ω 1] = 0 subscript Pr 𝜆 subscript 𝐼 𝑗 𝜔 conditional 1 𝜔 subscript Ω 1 0 \operatorname{Pr}_{\lambda}[I_{j}(\omega)=1|\omega\in\Omega_{1}]=0. For Pr λ ⁡ [I j ​ ( ω) = 1 | ω ∈ Ω 2] subscript Pr 𝜆 subscript 𝐼 𝑗 𝜔 conditional 1 𝜔 subscript Ω 2 \operatorname{Pr}_{\lambda}[I_{j}(\omega)=1|\omega\in\Omega_{2}], we can partition

 | Ω 2 = ⨆ k ≠ j { w ∈ Ω 2: w ​ ( j) = k }. subscript Ω 2 subscript square-union 𝑘 𝑗 conditional-set 𝑤 subscript Ω 2 𝑤 𝑗 𝑘 \Omega_{2}=\bigsqcup_{k\neq j}\{w\in\Omega_{2}:w(j)=k\}. |  |

Conjugation by ( j) ​ ( 1, 2, …, j − 1, j + 1, …, n) 𝑗 1 2 … 𝑗 1 𝑗 1 … 𝑛 (j)(1,2,\ldots,j-1,j+1,\ldots,n) induces bijections among these sets, and thus they all must have the same size. Observe that in n − j 𝑛 𝑗 n-j of the n − 1 𝑛 1 n-1 sets, an excedance at j 𝑗 j occurs. Hence,

 | Pr λ ⁡ [I j = 1] = Pr λ ⁡ [ω ∈ Ω 2] ⋅ Pr λ ⁡ [I j ​ ( ω) = 1 | ω ∈ Ω 2] = ( 1 − a 1 n) ⋅ n − j n − 1. subscript Pr 𝜆 subscript 𝐼 𝑗 1 ⋅ subscript Pr 𝜆 𝜔 subscript Ω 2 subscript Pr 𝜆 subscript 𝐼 𝑗 𝜔 conditional 1 𝜔 subscript Ω 2 ⋅ 1 subscript 𝑎 1 𝑛 𝑛 𝑗 𝑛 1 \operatorname{Pr}_{\lambda}[I_{j}=1]=\operatorname{Pr}_{\lambda}[\omega\in\Omega_{2}]\cdot\operatorname{Pr}_{\lambda}[I_{j}(\omega)=1|\omega\in\Omega_{2}]=\left(1-\frac{a_{1}}{n}\right)\cdot\frac{n-j}{n-1}. |  |

For the excedance statistic, we conclude that

 | 𝔼 λ ​ [exc] = ∑ j = 1 n Pr λ ⁡ [I j = 1] = ∑ j = 1 n ( 1 − a 1 n) ⋅ n − j n − 1 = ( n − a 1 n) ⋅ 1 n − 1 ⋅ ( n 2) = 1 2 ​ ( n − a 1). subscript 𝔼 𝜆 delimited-[] exc superscript subscript 𝑗 1 𝑛 subscript Pr 𝜆 subscript 𝐼 𝑗 1 superscript subscript 𝑗 1 𝑛 ⋅ 1 subscript 𝑎 1 𝑛 𝑛 𝑗 𝑛 1 ⋅ 𝑛 subscript 𝑎 1 𝑛 1 𝑛 1 binomial 𝑛 2 1 2 𝑛 subscript 𝑎 1 \begin{split}\mathbb{E}_{\lambda}[\operatorname{exc}]=\sum_{j=1}^{n}\operatorname{Pr}_{\lambda}[I_{j}=1]=\sum_{j=1}^{n}\left(1-\frac{a_{1}}{n}\right)\cdot\frac{n-j}{n-1}=\left(\frac{n-a_{1}}{n}\right)\cdot\frac{1}{n-1}\cdot{n\choose 2}=\frac{1}{2}(n-a_{1}).\end{split} |  |

We have already noted that for every fixed conjugacy class C 𝐶 C, excedance and anti-excedance are equidistributed on C 𝐶 C. For the weak excedance statistic exc ~ ​ ( ω), ~ exc 𝜔 \mathrm{\widetilde{exc}}(\omega), by definition, the only change in the above argument is that Pr λ ⁡ [I ~ j ​ ( ω) = 1 | ω ∈ Ω 1] = 1 subscript Pr 𝜆 subscript ~ 𝐼 𝑗 𝜔 conditional 1 𝜔 subscript Ω 1 1 \operatorname{Pr}_{\lambda}[\widetilde{I}_{j}(\omega)=1|\omega\in\Omega_{1}]=1 where I ~ j subscript ~ 𝐼 𝑗 \widetilde{I}_{j} is the weak excedance indicator function. Hence

 | Pr λ ⁡ [I j ~ ​ ( ω) = 1] = Pr λ ⁡ [I j ​ ( ω) = 1] + a 1 n, subscript Pr 𝜆 ~ subscript 𝐼 𝑗 𝜔 1 subscript Pr 𝜆 subscript 𝐼 𝑗 𝜔 1 subscript 𝑎 1 𝑛 \operatorname{Pr}_{\lambda}[\widetilde{I_{j}}(\omega)=1]=\operatorname{Pr}_{\lambda}[I_{j}(\omega)=1]+\frac{a_{1}}{n}, |  | (5.1) |

and

 | 𝔼 λ ​ [exc ~] = 𝔼 λ ​ [exc] + a 1 = 1 2 ​ ( n + a 1). ∎ subscript 𝔼 𝜆 delimited-[] ~ exc subscript 𝔼 𝜆 delimited-[] exc subscript 𝑎 1 1 2 𝑛 subscript 𝑎 1 \mathbb{E}_{\lambda}[\widetilde{\operatorname{exc}}]=\mathbb{E}_{\lambda}[\operatorname{exc}]+a_{1}=\frac{1}{2}(n+a_{1}).\qed |  |

###### Corollary 5.2.

Let λ = ( 1 a 1, 2 a 2, …, n a n) 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 \lambda=(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}}). Then the expected values of exc, exc ~ exc ~ exc \operatorname{exc},\widetilde{\operatorname{exc}} and aexc aexc \operatorname{aexc} are independent of a 2, …, a n subscript 𝑎 2 … subscript 𝑎 𝑛 a_{2},\ldots,a_{n}. In particular, when a 1 = 0 subscript 𝑎 1 0 a_{1}=0, we have that 𝔼 λ ​ [exc] = 𝔼 λ ​ [aexc] = 𝔼 λ ​ [exc ~] = n 2 subscript 𝔼 𝜆 delimited-[] exc subscript 𝔼 𝜆 delimited-[] aexc subscript 𝔼 𝜆 delimited-[] ~ exc 𝑛 2 \mathbb{E}_{\lambda}[\operatorname{exc}]=\mathbb{E}_{\lambda}[\operatorname{aexc}]=\mathbb{E}_{\lambda}[\widetilde{\operatorname{exc}}]=\frac{n}{2}.

### 5.2 Cyclic double ascents and cyclic valleys

Several recent papers [CJZ20, BS21] consider statistics derived from the excedance statistic. In [CJZ20], the following statistics are defined for ω ∈ S n 𝜔 subscript 𝑆 𝑛 \omega\in S_{n}. The element i ∈ [n] 𝑖 delimited-[] 𝑛 i\in[n] is a

1. 1.

*cyclic valley*of ω 𝜔 \omega if ω − 1 ​ ( i) > i < ω ​ ( i) superscript 𝜔 1 𝑖 𝑖 𝜔 𝑖 \omega^{-1}(i)>i<\omega(i);

2. 2.

*cyclic peak*of ω 𝜔 \omega if ω − 1 ​ ( i) ​ < i > ​ ω ​ ( i) superscript 𝜔 1 𝑖 expectation 𝑖 𝜔 𝑖 \omega^{-1}(i)<i>\omega(i);

3. 3.

*cyclic double ascent*of ω 𝜔 \omega if ω − 1 ​ ( i) < i < ω ​ ( i) superscript 𝜔 1 𝑖 𝑖 𝜔 𝑖 \omega^{-1}(i)<i<\omega(i); and

4. 4.

*cyclic double descent*of ω 𝜔 \omega if ω − 1 ​ ( i) > i > ω ​ ( i) superscript 𝜔 1 𝑖 𝑖 𝜔 𝑖 \omega^{-1}(i)>i>\omega(i).

A cyclic double ascent (respectively, cyclic double descent) coincides with the *linked excedance*(respectively, *linked anti-excedance*) defined in [BS21]. We follow the notation of [CJZ20], and write cval ⁡ ( ω) cval 𝜔 \operatorname{cval}(\omega) (respectively, cpk ⁡ ( ω) cpk 𝜔 \operatorname{cpk}(\omega)) for the number of cyclic valleys (respectively, cyclic peaks) of ω 𝜔 \omega. Also write Cval ⁡ ( ω) Cval 𝜔 \operatorname{Cval}(\omega) (respectively, Cpk ⁡ ( ω) Cpk 𝜔 \operatorname{Cpk}(\omega)) for the *set*of cyclic valleys (respectively, cyclic peaks) of ω 𝜔 \omega. Clearly i 𝑖 i is a cyclic valley of ω 𝜔 \omega if either i 𝑖 i is the smaller letter in a 2-cycle, or if i 𝑖 i appears in a cycle of ω 𝜔 \omega of length at least 3. In the latter case the cycle containing i 𝑖 i must be of the form ( … ​ j ​ i ​ k ​ …) … 𝑗 𝑖 𝑘 … (\ldots j\,i\,k\ldots) for j > i < k 𝑗 𝑖 𝑘 j>i<k. Let ρ 𝜌 \rho be the reversing involution defined by ρ ​ ( i) = n + 1 − i 𝜌 𝑖 𝑛 1 𝑖 \rho(i)=n+1-i. Since the corresponding cycle of ρ ​ ω ​ ρ − 1 𝜌 𝜔 superscript 𝜌 1 \rho\,\omega\rho^{-1} is ( …, n + 1 − j, n + 1 − i, n + 1 − k, …) … 𝑛 1 𝑗 𝑛 1 𝑖 𝑛 1 𝑘 … (\ldots,n+1-j,\,n+1-i,\,n+1-k,\ldots), it follows that

 | i ∈ { 1, …, n − 1 } ​ is a cyclic valley of ​ ω ⇔ n + 1 − i ∈ { 2, …, n } ​ is a cyclic peak of ​ ρ ​ ω ​ ρ − 1, iff 𝑖 1 … 𝑛 1 is a cyclic valley of 𝜔 𝑛 1 𝑖 2 … 𝑛 is a cyclic peak of 𝜌 𝜔 superscript 𝜌 1 i\in\{1,\ldots,n-1\}\text{ is a cyclic valley of }\omega\iff n+1-i\in\{2,\ldots,n\}\text{ is a cyclic peak of }\rho\,\omega\rho^{-1}, |  |

and hence cyclic valleys and cyclic peaks are equidistributed over a fixed conjugacy class. The same argument shows that cyclic double descents and cyclic double ascents are equidistributed over a fixed conjugacy class.

The number of cyclic double ascents (respectively cyclic double descents) in a permutation ω 𝜔 \omega is denoted cdasc ⁡ ( ω) cdasc 𝜔 \operatorname{cdasc}(\omega) (respectively, cddes ⁡ ( ω) cddes 𝜔 \operatorname{cddes}(\omega)). Also, the *set*of cyclic double ascents (respectively cyclic double descents) in a permutation ω 𝜔 \omega is denoted Cdasc ⁡ ( ω) Cdasc 𝜔 \operatorname{Cdasc}(\omega) (respectively, Cddes ⁡ ( ω) Cddes 𝜔 \operatorname{Cddes}(\omega)).

Now observe that our methods apply to the statistics cdasc ⁡ ( ω) cdasc 𝜔 \operatorname{cdasc}(\omega), cval ⁡ ( ω) cval 𝜔 \operatorname{cval}(\omega) and cddes ⁡ ( ω) cddes 𝜔 \operatorname{cddes}(\omega), cpk ⁡ ( ω) cpk 𝜔 \operatorname{cpk}(\omega) as well. Let I j subscript 𝐼 𝑗 I_{j} be the indicator function for a cyclic double ascent at index j 𝑗 j and decompose cdasc ⁡ ( ω) = ∑ j = 2 n − 1 I j ​ ( ω) cdasc 𝜔 superscript subscript 𝑗 2 𝑛 1 subscript 𝐼 𝑗 𝜔 \operatorname{cdasc}(\omega)=\sum_{j=2}^{n-1}I_{j}(\omega). Let I j v subscript superscript 𝐼 𝑣 𝑗 I^{v}_{j} be the indicator function for a cyclic valley at j 𝑗 j, and write cval ⁡ ( ω) = ∑ j = 1 n − 1 I j v ​ ( ω) cval 𝜔 superscript subscript 𝑗 1 𝑛 1 subscript superscript 𝐼 𝑣 𝑗 𝜔 \operatorname{cval}(\omega)=\sum_{j=1}^{n-1}I^{v}_{j}(\omega). Define the sets

 | Ω 1 j = { ω ∈ C λ: j is in a 1 -cycle }, Ω 2 j = { ω ∈ C λ: j is in a 2 -cycle }, Ω 3 j = { ω ∈ C λ: j is not in a 1 -cycle or 2 -cycle }. formulae-sequence superscript subscript Ω 1 𝑗 conditional-set 𝜔 subscript 𝐶 𝜆 j is in a 1 -cycle formulae-sequence superscript subscript Ω 2 𝑗 conditional-set 𝜔 subscript 𝐶 𝜆 j is in a 2 -cycle superscript subscript Ω 3 𝑗 conditional-set 𝜔 subscript 𝐶 𝜆 j is not in a 1 -cycle or 2 -cycle \begin{split}\Omega_{1}^{j}&=\{\omega\in C_{\lambda}:\text{ $j$ is in a $1$-cycle}\},\\ \Omega_{2}^{j}&=\{\omega\in C_{\lambda}:\text{ $j$ is in a $2$-cycle}\},\\ \Omega_{3}^{j}&=\{\omega\in C_{\lambda}:\text{ $j$ is not in a $1$-cycle or $2$-cycle}\}.\end{split} |  | (5.2) |

Similar arguments as before imply the following results. First, we have the analogue of Lemma 4.3.

###### Lemma 5.3.

Let λ = ( 1 a 1, 2 a 2, …, n a n) ⊢ n proves 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 𝑛 \lambda=(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}})\vdash n, fix j ∈ [n] 𝑗 delimited-[] 𝑛 j\in[n], and define Ω k = Ω k j subscript Ω 𝑘 superscript subscript Ω 𝑘 𝑗 \Omega_{k}=\Omega_{k}^{j} as in ( 5.2). Then

1. 1.

Pr λ ⁡ [ω ∈ Ω 1] = a 1 n subscript Pr 𝜆 𝜔 subscript Ω 1 subscript 𝑎 1 𝑛 \operatorname{Pr}_{\lambda}[\omega\in\Omega_{1}]=\frac{a_{1}}{n},

2. 2.

Pr λ ⁡ [ω ∈ Ω 2] = 2 ​ a 2 n subscript Pr 𝜆 𝜔 subscript Ω 2 2 subscript 𝑎 2 𝑛 \operatorname{Pr}_{\lambda}[\omega\in\Omega_{2}]=\frac{2a_{2}}{n}, and

3. 3.

Pr λ ⁡ [ω ∈ Ω 3] = 1 − a 1 n − 2 ​ a 2 n subscript Pr 𝜆 𝜔 subscript Ω 3 1 subscript 𝑎 1 𝑛 2 subscript 𝑎 2 𝑛 \operatorname{Pr}_{\lambda}[\omega\in\Omega_{3}]=1-\frac{a_{1}}{n}-\frac{2a_{2}}{n}.

###### Proof.

The proof follows the same arguments as Lemma 4.3. ∎

###### Theorem 5.4.

Let λ = ( 1 a 1, 2 a 2, …, n a n) ⊢ n proves 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 𝑛 \lambda=(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}})\vdash n. Then

1. 1.

𝔼 λ ​ [cdasc] = n − a 1 − 2 ​ a 2 6 = 𝔼 λ ​ [cddes] subscript 𝔼 𝜆 delimited-[] cdasc 𝑛 subscript 𝑎 1 2 subscript 𝑎 2 6 subscript 𝔼 𝜆 delimited-[] cddes \mathbb{E}_{\lambda}[\operatorname{cdasc}]=\frac{n-a_{1}-2a_{2}}{6}=\mathbb{E}_{\lambda}[\operatorname{cddes}] and

2. 2.

𝔼 λ ​ [cval] = n − a 1 + a 2 3 = 𝔼 λ ​ [cpk]. subscript 𝔼 𝜆 delimited-[] cval 𝑛 subscript 𝑎 1 subscript 𝑎 2 3 subscript 𝔼 𝜆 delimited-[] cpk \mathbb{E}_{\lambda}[\operatorname{cval}]=\frac{n-a_{1}+a_{2}}{3}=\mathbb{E}_{\lambda}[\operatorname{cpk}].

###### Proof.

Fix j 𝑗 j and observe that if ω ∈ Ω 1 j ∪ Ω 2 j 𝜔 superscript subscript Ω 1 𝑗 superscript subscript Ω 2 𝑗 \omega\in\Omega_{1}^{j}\cup\Omega_{2}^{j}, then j 𝑗 j is not a cyclic double ascent of ω 𝜔 \omega. Also, j 𝑗 j is a cyclic valley of ω 𝜔 \omega only if ω ∈ Ω 2 j ∪ Ω 3 j 𝜔 superscript subscript Ω 2 𝑗 superscript subscript Ω 3 𝑗 \omega\in\Omega_{2}^{j}\cup\Omega_{3}^{j}. Hence, by the Law of Total Probability, we have

 | 𝔼 λ ​ [I j] subscript 𝔼 𝜆 delimited-[] subscript 𝐼 𝑗 \displaystyle\mathbb{E}_{\lambda}[I_{j}] | = ∑ k = 1 3 Pr λ ⁡ [ω ∈ Ω k j] ​ Pr λ ⁡ [I j ​ ( ω) = 1 | ω ∈ Ω k j] = Pr λ ⁡ [ω ∈ Ω 3 j] ​ Pr λ ⁡ [I j ​ ( ω) = 1 | ω ∈ Ω 3 j], absent superscript subscript 𝑘 1 3 subscript Pr 𝜆 𝜔 superscript subscript Ω 𝑘 𝑗 subscript Pr 𝜆 subscript 𝐼 𝑗 𝜔 conditional 1 𝜔 superscript subscript Ω 𝑘 𝑗 subscript Pr 𝜆 𝜔 superscript subscript Ω 3 𝑗 subscript Pr 𝜆 subscript 𝐼 𝑗 𝜔 conditional 1 𝜔 superscript subscript Ω 3 𝑗 \displaystyle=\sum_{k=1}^{3}\operatorname{Pr}_{\lambda}[\omega\in\Omega_{k}^{j}]\operatorname{Pr}_{\lambda}[I_{j}(\omega)=1|\omega\in\Omega_{k}^{j}]=\operatorname{Pr}_{\lambda}[\omega\in\Omega_{3}^{j}]\operatorname{Pr}_{\lambda}[I_{j}(\omega)=1|\omega\in\Omega_{3}^{j}], |  |

 | 𝔼 λ ​ [I j v] subscript 𝔼 𝜆 delimited-[] subscript superscript 𝐼 𝑣 𝑗 \displaystyle\mathbb{E}_{\lambda}[I^{v}_{j}] | = ∑ k = 1 3 Pr λ ⁡ [ω ∈ Ω k j] ​ Pr λ ⁡ [I j v ​ ( ω) = 1 | ω ∈ Ω k j] absent superscript subscript 𝑘 1 3 subscript Pr 𝜆 𝜔 superscript subscript Ω 𝑘 𝑗 subscript Pr 𝜆 subscript superscript 𝐼 𝑣 𝑗 𝜔 conditional 1 𝜔 superscript subscript Ω 𝑘 𝑗 \displaystyle=\sum_{k=1}^{3}\operatorname{Pr}_{\lambda}[\omega\in\Omega_{k}^{j}]\operatorname{Pr}_{\lambda}[I^{v}_{j}(\omega)=1|\omega\in\Omega_{k}^{j}] |  |

 |  | = Pr λ ⁡ [ω ∈ Ω 3 j] ​ Pr λ ⁡ [I j v ​ ( ω) = 1 | ω ∈ Ω 3 j] + Pr λ ⁡ [ω ∈ Ω 2 j] ​ Pr λ ⁡ [I j v ​ ( ω) = 1 | ω ∈ Ω 2 j]. absent subscript Pr 𝜆 𝜔 superscript subscript Ω 3 𝑗 subscript Pr 𝜆 subscript superscript 𝐼 𝑣 𝑗 𝜔 conditional 1 𝜔 superscript subscript Ω 3 𝑗 subscript Pr 𝜆 𝜔 superscript subscript Ω 2 𝑗 subscript Pr 𝜆 subscript superscript 𝐼 𝑣 𝑗 𝜔 conditional 1 𝜔 superscript subscript Ω 2 𝑗 \displaystyle=\operatorname{Pr}_{\lambda}[\omega\in\Omega_{3}^{j}]\operatorname{Pr}_{\lambda}[I^{v}_{j}(\omega)=1|\omega\in\Omega_{3}^{j}]+\operatorname{Pr}_{\lambda}[\omega\in\Omega_{2}^{j}]\operatorname{Pr}_{\lambda}[I^{v}_{j}(\omega)=1|\omega\in\Omega_{2}^{j}]. |  |

If we fix distinct i, k ∈ [n] ∖ { j } 𝑖 𝑘 delimited-[] 𝑛 𝑗 i,k\in[n]\setminus\{j\}, then conjugation by appropriate elements implies Pr λ ⁡ [ω ​ ( i) = j | ω ∈ Ω 2 j] = Pr λ ⁡ [ω ​ ( i) = j | ω ∈ Ω 3 j] = 1 n − 1 subscript Pr 𝜆 𝜔 𝑖 conditional 𝑗 𝜔 superscript subscript Ω 2 𝑗 subscript Pr 𝜆 𝜔 𝑖 conditional 𝑗 𝜔 superscript subscript Ω 3 𝑗 1 𝑛 1 \Pr_{\lambda}[\omega(i)=j|\omega\in\Omega_{2}^{j}]=\Pr_{\lambda}[\omega(i)=j|\omega\in\Omega_{3}^{j}]=\frac{1}{n-1} and Pr λ ⁡ [ω ​ ( i) = j ∧ ω ​ ( j) = k | ω ∈ Ω 3 j] = 1 ( n − 1) ​ ( n − 2) subscript Pr 𝜆 𝜔 𝑖 𝑗 𝜔 𝑗 conditional 𝑘 𝜔 superscript subscript Ω 3 𝑗 1 𝑛 1 𝑛 2 \Pr_{\lambda}[\omega(i)=j\wedge\omega(j)=k|\omega\in\Omega_{3}^{j}]=\frac{1}{(n-1)(n-2)}.

Now let i, j, k 𝑖 𝑗 𝑘 i,j,k be elements appearing in succession in a cycle of length at least 3. A cyclic double ascent at j 𝑗 j occurs if and only if i < j < k 𝑖 𝑗 𝑘 i<j<k, and hence there are a total of ( j − 1) ​ ( n − j) 𝑗 1 𝑛 𝑗 (j-1)(n-j) choices { i, k } 𝑖 𝑘 \{i,k\} that result in a cyclic double ascent at j ≠ 1, n 𝑗 1 𝑛 j\neq 1,n. A cyclic valley occurs if i > j < k 𝑖 𝑗 𝑘 i>j<k, and thus there are a total of ( n − j) ​ ( n − j − 1) 𝑛 𝑗 𝑛 𝑗 1 (n-j)(n-j-1) choices for { i, k } 𝑖 𝑘 \{i,k\} that result in a cyclic valley at j ≠ n 𝑗 𝑛 j\neq n. However, a cyclic valley also occurs at j 𝑗 j when ( i, j) 𝑖 𝑗 (i,j) is a 2-cycle with i > j 𝑖 𝑗 i>j. There are ( n − j) 𝑛 𝑗 (n-j) choices for i 𝑖 i in this case.

Combined with the preceding lemma, we see that

 | 𝔼 λ ​ [I j] subscript 𝔼 𝜆 delimited-[] subscript 𝐼 𝑗 \displaystyle\mathbb{E}_{\lambda}[I_{j}] | = ( 1 − a 1 n − 2 ​ a 2 n) ⋅ ( j − 1) ​ ( n − j) ( n − 1) ​ ( n − 2), absent ⋅ 1 subscript 𝑎 1 𝑛 2 subscript 𝑎 2 𝑛 𝑗 1 𝑛 𝑗 𝑛 1 𝑛 2 \displaystyle=\left(1-\frac{a_{1}}{n}-\frac{2a_{2}}{n}\right)\cdot\frac{(j-1)(n-j)}{(n-1)(n-2)}, |  |

 | 𝔼 λ ​ [I j v] subscript 𝔼 𝜆 delimited-[] subscript superscript 𝐼 𝑣 𝑗 \displaystyle\mathbb{E}_{\lambda}[I^{v}_{j}] | = ( 1 − a 1 n − 2 ​ a 2 n) ⋅ ( n − j − 1) ​ ( n − j) ( n − 1) ​ ( n − 2) + 2 ​ a 2 n ⋅ n − j n − 1. absent ⋅ 1 subscript 𝑎 1 𝑛 2 subscript 𝑎 2 𝑛 𝑛 𝑗 1 𝑛 𝑗 𝑛 1 𝑛 2 ⋅ 2 subscript 𝑎 2 𝑛 𝑛 𝑗 𝑛 1 \displaystyle=\left(1-\frac{a_{1}}{n}-\frac{2a_{2}}{n}\right)\cdot\frac{(n-j-1)(n-j)}{(n-1)(n-2)}+\frac{2a_{2}}{n}\cdot\frac{n-j}{n-1}. |  |

Summing over all j 𝑗 j gives

 | 𝔼 λ ​ [cdasc] subscript 𝔼 𝜆 delimited-[] cdasc \displaystyle\mathbb{E}_{\lambda}[\operatorname{cdasc}] | = ( 1 − a 1 n − 2 ​ a 2 n) ⋅ 1 ( n − 1) ​ ( n − 2) ⋅ ∑ j = 2 n − 1 ( j − 1) ​ ( n − j) = ( 1 − a 1 n − 2 ​ a 2 n) ⋅ n 6, absent ⋅ 1 subscript 𝑎 1 𝑛 2 subscript 𝑎 2 𝑛 1 𝑛 1 𝑛 2 superscript subscript 𝑗 2 𝑛 1 𝑗 1 𝑛 𝑗 ⋅ 1 subscript 𝑎 1 𝑛 2 subscript 𝑎 2 𝑛 𝑛 6 \displaystyle=\left(1-\frac{a_{1}}{n}-\frac{2a_{2}}{n}\right)\cdot\frac{1}{(n-1)(n-2)}\cdot\sum_{j=2}^{n-1}(j-1)(n-j)=\left(1-\frac{a_{1}}{n}-\frac{2a_{2}}{n}\right)\cdot\frac{n}{6}, |  |

 | 𝔼 λ ​ [cval] subscript 𝔼 𝜆 delimited-[] cval \displaystyle\mathbb{E}_{\lambda}[\operatorname{cval}] | = ( 1 − a 1 n − 2 ​ a 2 n) ⋅ 1 ( n − 1) ​ ( n − 2) ⋅ ∑ j = 1 n − 1 ( n − j − 1) ​ ( n − j) + 2 ​ a 2 n ​ ( n − 1) ⋅ ∑ j = 1 n − 1 ( n − j) absent ⋅ 1 subscript 𝑎 1 𝑛 2 subscript 𝑎 2 𝑛 1 𝑛 1 𝑛 2 superscript subscript 𝑗 1 𝑛 1 𝑛 𝑗 1 𝑛 𝑗 ⋅ 2 subscript 𝑎 2 𝑛 𝑛 1 superscript subscript 𝑗 1 𝑛 1 𝑛 𝑗 \displaystyle=\left(1-\frac{a_{1}}{n}-\frac{2a_{2}}{n}\right)\cdot\frac{1}{(n-1)(n-2)}\cdot\sum_{j=1}^{n-1}(n-j-1)(n-j)+\frac{2a_{2}}{n(n-1)}\cdot\sum_{j=1}^{n-1}(n-j) |  |

 |  | = ( 1 − a 1 n − 2 ​ a 2 n) ⋅ n 3 + a 2, absent ⋅ 1 subscript 𝑎 1 𝑛 2 subscript 𝑎 2 𝑛 𝑛 3 subscript 𝑎 2 \displaystyle=\left(1-\frac{a_{1}}{n}-\frac{2a_{2}}{n}\right)\cdot\frac{n}{3}+a_{2}, |  |

using the facts that ∑ j = 2 n − 1 ( j − 1) ​ ( n − j) = ( n 3) superscript subscript 𝑗 2 𝑛 1 𝑗 1 𝑛 𝑗 binomial 𝑛 3 \sum_{j=2}^{n-1}(j-1)(n-j)=\binom{n}{3} and ∑ j = 1 n − 1 ( n − j − 1) ​ ( n − j) = 2 ​ ( n 3). superscript subscript 𝑗 1 𝑛 1 𝑛 𝑗 1 𝑛 𝑗 2 binomial 𝑛 3 \sum_{j=1}^{n-1}(n-j-1)(n-j)=2\binom{n}{3}. This finishes the proof. ∎

These results confirm the fact that exc ⁡ ( ω) = cval ⁡ ( ω) + cdasc ⁡ ( ω) exc 𝜔 cval 𝜔 cdasc 𝜔 \operatorname{exc}(\omega)=\operatorname{cval}(\omega)+\operatorname{cdasc}(\omega).

## 6 First moments on S n subscript 𝑆 𝑛 S_{n} from conjugacy class

In this section, we consider connections between the first moments on conjugacy classes with those on all of S n subscript 𝑆 𝑛 S_{n}. Observe that the expected values of a statistic X 𝑋 X on individual conjugacy classes is related to the expected value on the entire symmetric group by the formula

 | 𝔼 S n ​ [X] = ∑ λ ⊢ n z λ − 1 ​ 𝔼 λ ​ [X], subscript 𝔼 subscript 𝑆 𝑛 delimited-[] 𝑋 subscript proves 𝜆 𝑛 superscript subscript 𝑧 𝜆 1 subscript 𝔼 𝜆 delimited-[] 𝑋 \mathbb{E}_{S_{n}}[X]=\sum_{\lambda\vdash n}z_{\lambda}^{-1}\mathbb{E}_{\lambda}[X], |  | (6.1) |

since the order of the conjugacy class indexed by λ 𝜆 \lambda is n! / z λ 𝑛 subscript 𝑧 𝜆 n!/z_{\lambda}.

In this section we analyse Equation ( 6.1) more carefully. The following identities will be useful.

###### Lemma 6.1.

Let λ = ( 1 a 1, 2 a 2, …, n a n) ⊢ n proves 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 𝑛 \lambda=(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}})\vdash n. The following identities hold:

1. 1.

∑ λ ⊢ n z λ − 1 = 1 subscript proves 𝜆 𝑛 superscript subscript 𝑧 𝜆 1 1 \sum_{\lambda\vdash n}z_{\lambda}^{-1}=1,

2. 2.

∑ λ ⊢ n z λ − 1 ​ a 1 = 1 subscript proves 𝜆 𝑛 superscript subscript 𝑧 𝜆 1 subscript 𝑎 1 1 \sum_{\lambda\vdash n}z_{\lambda}^{-1}a_{1}=1,

3. 3.

∑ λ ⊢ n z λ − 1 ​ a 1 2 = 2 subscript proves 𝜆 𝑛 superscript subscript 𝑧 𝜆 1 superscript subscript 𝑎 1 2 2 \sum_{\lambda\vdash n}z_{\lambda}^{-1}a_{1}^{2}=2, and

4. 4.

∑ λ ⊢ n z λ − 1 ​ a 2 = 1 / 2. subscript proves 𝜆 𝑛 superscript subscript 𝑧 𝜆 1 subscript 𝑎 2 1 2 \sum_{\lambda\vdash n}z_{\lambda}^{-1}a_{2}=1/2.

###### Proof.

1. 1.

This is the class equation for S n subscript 𝑆 𝑛 S_{n} [DF91], a consequence of the fact that n! = ∑ λ ⊢ n | C λ |. 𝑛 subscript proves 𝜆 𝑛 subscript 𝐶 𝜆 n!=\sum_{\lambda\vdash n}|C_{\lambda}|.

2. 2.

This is Burnside’s lemma for the symmetric group [DF91, Sta99].

3. 3.

Here we consider S n subscript 𝑆 𝑛 S_{n} acting on 2-subsets of [n] delimited-[] 𝑛 [n]. There is only one orbit, and a permutation fixes a 2-subset { i, j } 𝑖 𝑗 \{i,j\} if and only if either i, j 𝑖 𝑗 i,j are both fixed points, or i, j 𝑖 𝑗 i,j form a 2-cycle. Hence the number of 2-subsets fixed by a permutation of cycle type λ 𝜆 \lambda with a k subscript 𝑎 𝑘 a_{k} parts of length k 𝑘 k, is ( a 1 2) + a 2 binomial subscript 𝑎 1 2 subscript 𝑎 2 \binom{a_{1}}{2}+a_{2}, and Burnside’s lemma gives

 | ∑ λ ⊢ n z λ − 1 ​ ( ( a 1 2) + a 2) = 1. subscript proves 𝜆 𝑛 superscript subscript 𝑧 𝜆 1 binomial subscript 𝑎 1 2 subscript 𝑎 2 1 \sum_{\lambda\vdash n}z_{\lambda}^{-1}\left(\binom{a_{1}}{2}+a_{2}\right)=1. |  | (6.2) |

Similarly, by applying Burnside’s lemma to the action of S n subscript 𝑆 𝑛 S_{n} on the set [n] × [n] delimited-[] 𝑛 delimited-[] 𝑛 [n]\times[n] of ordered pairs ( i, j) 𝑖 𝑗 (i,j), which has two orbits { ( i, i): 1 ≤ i ≤ n } conditional-set 𝑖 𝑖 1 𝑖 𝑛 \{(i,i):1\leq i\leq n\} and { ( i, j): 1 ≤ i, j ≤ n, i ≠ j } conditional-set 𝑖 𝑗 formulae-sequence 1 𝑖 formulae-sequence 𝑗 𝑛 𝑖 𝑗 \{(i,j):1\leq i,j\leq n,i\neq j\}, and counting fixed points, we obtain

 | ∑ λ ⊢ n z λ − 1 ​ ( a 1 + 2 ​ ( a 1 2)) = 2 = ∑ λ ⊢ n z λ − 1 ​ a 1 2. subscript proves 𝜆 𝑛 superscript subscript 𝑧 𝜆 1 subscript 𝑎 1 2 binomial subscript 𝑎 1 2 2 subscript proves 𝜆 𝑛 superscript subscript 𝑧 𝜆 1 superscript subscript 𝑎 1 2 \sum_{\lambda\vdash n}z_{\lambda}^{-1}\left(a_{1}+2\binom{a_{1}}{2}\right)=2=\sum_{\lambda\vdash n}z_{\lambda}^{-1}a_{1}^{2}. |  | (6.3) |

4. 4.

Using ( 6.3) and the second identity also gives

 | ∑ λ ⊢ n 2 ​ z λ − 1 ​ ( a 1 2) = 1. subscript proves 𝜆 𝑛 2 superscript subscript 𝑧 𝜆 1 binomial subscript 𝑎 1 2 1 \sum_{\lambda\vdash n}2z_{\lambda}^{-1}\binom{a_{1}}{2}=1. |  | (6.4) |

The last identity now follows from ( 6.2) and ( 6.4).∎

It is now easy to compute the first moments of the preceding statistics over the whole symmetric group; see Table 1 for an overview of our results, as well as a comparison to the literature. Note that we are able to obtain the first moment over the whole symmetric group without knowledge of the generating function for the statistic. Recall the definitions of α n ​ ( X) = ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) subscript 𝛼 𝑛 𝑋 subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 \alpha_{n}(X)=\sum_{1\leq i<j\leq n}\text{wt}(i,j) and β n ​ ( X) = ∑ 1 ≤ i < j ≤ n ( j − i − 1) ​ wt ​ ( i, j) subscript 𝛽 𝑛 𝑋 subscript 1 𝑖 𝑗 𝑛 𝑗 𝑖 1 wt 𝑖 𝑗 \beta_{n}(X)=\sum_{1\leq i<j\leq n}(j-i-1)\text{wt}(i,j) for a weighted inversion statistic X = ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) ​ I i, j 𝑋 subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 subscript 𝐼 𝑖 𝑗 X=\sum_{1\leq i<j\leq n}\text{wt}(i,j)I_{i,j} from Theorem 4.8.

###### Proposition 6.2.

Let λ = ( 1 a 1, 2 a 2, …, n a n) ⊢ n proves 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … superscript 𝑛 subscript 𝑎 𝑛 𝑛 \lambda=(1^{a_{1}},2^{a_{2}},\ldots,n^{a_{n}})\vdash n, and let X = ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) ​ I i, j 𝑋 subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 subscript 𝐼 𝑖 𝑗 X=\sum_{1\leq i<j\leq n}\text{wt}(i,j)I_{i,j} be a weighted inversion statistic. Then

1. 1.

𝔼 S n ​ [X] = α n ​ ( X) 2 subscript 𝔼 subscript 𝑆 𝑛 delimited-[] 𝑋 subscript 𝛼 𝑛 𝑋 2 \mathbb{E}_{S_{n}}[X]=\frac{\alpha_{n}(X)}{2}, and

2. 2.

𝔼 λ ​ [X] = 𝔼 S n ​ [X] + f n X ​ ( a 1, a 2), subscript 𝔼 𝜆 delimited-[] 𝑋 subscript 𝔼 subscript 𝑆 𝑛 delimited-[] 𝑋 subscript superscript 𝑓 𝑋 𝑛 subscript 𝑎 1 subscript 𝑎 2 \mathbb{E}_{\lambda}[X]=\mathbb{E}_{S_{n}}[X]+f^{X}_{n}(a_{1},a_{2}), where f n X subscript superscript 𝑓 𝑋 𝑛 f^{X}_{n} is a polynomial of degree at most 2 2 2 in a 1 subscript 𝑎 1 a_{1} and a 2 subscript 𝑎 2 a_{2} such that

 | ∑ λ ⊢ n z λ − 1 ​ f n X ​ ( a 1, a 2) = 0. subscript proves 𝜆 𝑛 superscript subscript 𝑧 𝜆 1 subscript superscript 𝑓 𝑋 𝑛 subscript 𝑎 1 subscript 𝑎 2 0 \sum_{\lambda\vdash n}z_{\lambda}^{-1}f^{X}_{n}(a_{1},a_{2})=0. |  |

###### Proof.

Note first that Pr S n ⁡ [I i, j = 1] = 1 / 2 subscript Pr subscript 𝑆 𝑛 subscript 𝐼 𝑖 𝑗 1 1 2 \operatorname{Pr}_{S_{n}}[I_{i,j}=1]=1/2 for 1 ≤ i < j ≤ n 1 𝑖 𝑗 𝑛 1\leq i<j\leq n. The decomposition X = ∑ 1 ≤ i < j ≤ n wt ​ ( i, j) ​ I i, j 𝑋 subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 subscript 𝐼 𝑖 𝑗 X=\sum_{1\leq i<j\leq n}\text{wt}(i,j)I_{i,j} implies

 | 𝔼 S n ​ [X] = 1 2 ​ ∑ 1 ≤ i < j ≤ n wt ​ ( i, j). subscript 𝔼 subscript 𝑆 𝑛 delimited-[] 𝑋 1 2 subscript 1 𝑖 𝑗 𝑛 wt 𝑖 𝑗 \mathbb{E}_{S_{n}}[X]=\frac{1}{2}\sum_{1\leq i<j\leq n}\text{wt}(i,j). |  |

Although we can now conclude Part (2) as well, it is instructive to examine the different contributions to our expression for 𝔼 λ ​ [X] subscript 𝔼 𝜆 delimited-[] 𝑋 \mathbb{E}_{\lambda}[X] more carefully. Since β n ​ ( X) = ∑ 1 ≤ i < j ≤ n ( j − i − 1) ​ wt ​ ( i, j) subscript 𝛽 𝑛 𝑋 subscript 1 𝑖 𝑗 𝑛 𝑗 𝑖 1 wt 𝑖 𝑗 \beta_{n}(X)=\sum_{1\leq i<j\leq n}(j-i-1)\text{wt}(i,j), from Theorem 4.8 we obtain

 | 𝔼 λ ​ [X] subscript 𝔼 𝜆 delimited-[] 𝑋 \displaystyle\mathbb{E}_{\lambda}[X] | = ( 1 2 + a 2 n ​ ( n − 1) − a 1 ​ ( a 1 − 1) 2 ​ n ​ ( n − 1)) ​ α n ​ ( X) + ( n − n ​ a 1 − a 1 + a 1 2 − 2 ​ a 2 n ​ ( n − 1) ​ ( n − 2)) ​ β n ​ ( X) absent 1 2 subscript 𝑎 2 𝑛 𝑛 1 subscript 𝑎 1 subscript 𝑎 1 1 2 𝑛 𝑛 1 subscript 𝛼 𝑛 𝑋 𝑛 𝑛 subscript 𝑎 1 subscript 𝑎 1 superscript subscript 𝑎 1 2 2 subscript 𝑎 2 𝑛 𝑛 1 𝑛 2 subscript 𝛽 𝑛 𝑋 \displaystyle=\left(\frac{1}{2}+\frac{a_{2}}{n(n-1)}-\frac{a_{1}(a_{1}-1)}{2n(n-1)}\right)\alpha_{n}(X)+\left(\frac{n-na_{1}-a_{1}+a_{1}^{2}-2a_{2}}{n(n-1)(n-2)}\right)\beta_{n}(X) |  |

 |  | = α n ​ ( X) 2 + 1 n ​ ( n − 1) ​ ( a 2 − ( a 1 2)) ​ α n ​ ( X) + 1 n ​ ( n − 1) ​ ( n − 2) ​ ( n ​ ( 1 − a 1) + 2 ​ ( a 1 2) − 2 ​ a 2) ​ β n ​ ( X). absent subscript 𝛼 𝑛 𝑋 2 1 𝑛 𝑛 1 subscript 𝑎 2 binomial subscript 𝑎 1 2 subscript 𝛼 𝑛 𝑋 1 𝑛 𝑛 1 𝑛 2 𝑛 1 subscript 𝑎 1 2 binomial subscript 𝑎 1 2 2 subscript 𝑎 2 subscript 𝛽 𝑛 𝑋 \displaystyle=\frac{\alpha_{n}(X)}{2}+\frac{1}{n(n-1)}\left(a_{2}-\binom{a_{1}}{2}\right)\alpha_{n}(X)+\frac{1}{n(n-1)(n-2)}\left(n(1-a_{1})+2\binom{a_{1}}{2}-2a_{2}\right)\beta_{n}(X). |  |

The function f n ​ ( X) subscript 𝑓 𝑛 𝑋 f_{n}(X) is given by

 | f n ​ ( X) = 1 n ​ ( n − 1) ​ ( a 2 − ( a 1 2)) ​ α n ​ ( X) + 1 n ​ ( n − 1) ​ ( n − 2) ​ ( n ​ ( 1 − a 1) + 2 ​ ( a 1 2) − 2 ​ a 2) ​ β n ​ ( X). subscript 𝑓 𝑛 𝑋 1 𝑛 𝑛 1 subscript 𝑎 2 binomial subscript 𝑎 1 2 subscript 𝛼 𝑛 𝑋 1 𝑛 𝑛 1 𝑛 2 𝑛 1 subscript 𝑎 1 2 binomial subscript 𝑎 1 2 2 subscript 𝑎 2 subscript 𝛽 𝑛 𝑋 f_{n}(X)=\frac{1}{n(n-1)}\left(a_{2}-\binom{a_{1}}{2}\right)\alpha_{n}(X)+\frac{1}{n(n-1)(n-2)}\left(n(1-a_{1})+2\binom{a_{1}}{2}-2a_{2}\right)\beta_{n}(X). |  |

Now Lemma 6.1 guarantees that the two sums

 | ∑ λ ⊢ n z λ − 1 ​ ( 1 − a 1), ∑ λ ⊢ n z λ − 1 ​ ( a 2 − ( a 1 2)) subscript proves 𝜆 𝑛 superscript subscript 𝑧 𝜆 1 1 subscript 𝑎 1 subscript proves 𝜆 𝑛 superscript subscript 𝑧 𝜆 1 subscript 𝑎 2 binomial subscript 𝑎 1 2 \sum_{\lambda\vdash n}z_{\lambda}^{-1}(1-a_{1}),\ \ \sum_{\lambda\vdash n}z_{\lambda}^{-1}\left(a_{2}-\binom{a_{1}}{2}\right) |  |

vanish identically. Since α n ​ ( X) subscript 𝛼 𝑛 𝑋 \alpha_{n}(X) and β n ​ ( X) subscript 𝛽 𝑛 𝑋 \beta_{n}(X) are independent of λ 𝜆 \lambda, we obtain

 | ∑ λ ⊢ n z λ − 1 ​ f n ​ ( X) = 0 and ∑ λ ⊢ n z λ − 1 ​ 𝔼 λ ​ [X] = α n ​ ( X) 2, formulae-sequence subscript proves 𝜆 𝑛 superscript subscript 𝑧 𝜆 1 subscript 𝑓 𝑛 𝑋 0 and subscript proves 𝜆 𝑛 superscript subscript 𝑧 𝜆 1 subscript 𝔼 𝜆 delimited-[] 𝑋 subscript 𝛼 𝑛 𝑋 2 \sum_{\lambda\vdash n}z_{\lambda}^{-1}f_{n}(X)=0\quad\text{and}\quad\sum_{\lambda\vdash n}z_{\lambda}^{-1}\mathbb{E}_{\lambda}[X]=\frac{\alpha_{n}(X)}{2}, |  |

as claimed. ∎

Now let Y 𝑌 Y be any of the cyclic permutation statistics considered in Section 5. Arguments analogous to the above give us the following.

###### Proposition 6.3.

For any of the cyclic statistics Y 𝑌 Y from Section 5, the first moment on the conjugacy class C λ subscript 𝐶 𝜆 C_{\lambda} for each λ = ( 1 a 1, 2 a 2, …) ⊢ n proves 𝜆 superscript 1 subscript 𝑎 1 superscript 2 subscript 𝑎 2 … 𝑛 \lambda=(1^{a_{1}},2^{a_{2}},\ldots)\vdash n is of the form

 | 𝔼 λ ​ [Y] = 𝔼 S n ​ [Y] + g n ​ ( Y), subscript 𝔼 𝜆 delimited-[] 𝑌 subscript 𝔼 subscript 𝑆 𝑛 delimited-[] 𝑌 subscript 𝑔 𝑛 𝑌 \mathbb{E}_{\lambda}[Y]=\mathbb{E}_{S_{n}}[Y]+g_{n}(Y), |  |

where g n ​ ( Y) subscript 𝑔 𝑛 𝑌 g_{n}(Y) is some polynomial of degree at most 1 1 1 in a 1 subscript 𝑎 1 a_{1} and a 2 subscript 𝑎 2 a_{2} such that ∑ λ ⊢ n z λ − 1 ​ g n ​ ( Y) = 0. subscript proves 𝜆 𝑛 superscript subscript 𝑧 𝜆 1 subscript 𝑔 𝑛 𝑌 0 \sum_{\lambda\vdash n}z_{\lambda}^{-1}g_{n}(Y)=0. We have

1. 1.

𝔼 S n ​ [exc] = n − 1 2 subscript 𝔼 subscript 𝑆 𝑛 delimited-[] exc 𝑛 1 2 \mathbb{E}_{S_{n}}[\operatorname{exc}]=\frac{n-1}{2}, 𝔼 S n ​ [aexc] = n + 1 2 subscript 𝔼 subscript 𝑆 𝑛 delimited-[] aexc 𝑛 1 2 \mathbb{E}_{S_{n}}[\operatorname{aexc}]=\frac{n+1}{2},

2. 2.

𝔼 S n ​ [cdasc] = n − 2 6 = 𝔼 S n ​ [cddes] subscript 𝔼 subscript 𝑆 𝑛 delimited-[] cdasc 𝑛 2 6 subscript 𝔼 subscript 𝑆 𝑛 delimited-[] cddes \mathbb{E}_{S_{n}}[\operatorname{cdasc}]=\frac{n-2}{6}=\mathbb{E}_{S_{n}}[\operatorname{cddes}], and

3. 3.

𝔼 S n ​ [cval] = 2 ​ n − 1 6 = 𝔼 S n ​ [cpk] subscript 𝔼 subscript 𝑆 𝑛 delimited-[] cval 2 𝑛 1 6 subscript 𝔼 subscript 𝑆 𝑛 delimited-[] cpk \mathbb{E}_{S_{n}}[\operatorname{cval}]=\frac{2n-1}{6}=\mathbb{E}_{S_{n}}[\operatorname{cpk}].

###### Proof.

These follow as in Proposition 6.2, from Theorem 5.1 and Theorem 5.4, using Lemma 6.1. ∎

We conclude this section by noting that we can now also compute the variance of the statistic exc exc \operatorname{exc}, thanks to the following generating function derived in [CJZ20].

Recall that C λ subscript 𝐶 𝜆 C_{\lambda} denotes the conjugacy class in S n subscript 𝑆 𝑛 S_{n} indexed by the partition λ 𝜆 \lambda.

###### Proposition 6.4.

[CJZ20, Corollary 7] Let λ 𝜆 \lambda be a partition of n 𝑛 n with a 1 subscript 𝑎 1 a_{1} parts of size 1. Then

 | ∑ w ∈ C λ t exc ⁡ ( w) = ∑ i = 0 ⌊ ( n − a 1) / 2 ⌋ γ i ​ t i ​ ( 1 + t) n − a 1 − 2 ​ i, subscript 𝑤 subscript 𝐶 𝜆 superscript 𝑡 exc 𝑤 superscript subscript 𝑖 0 𝑛 subscript 𝑎 1 2 subscript 𝛾 𝑖 superscript 𝑡 𝑖 superscript 1 𝑡 𝑛 subscript 𝑎 1 2 𝑖 \sum_{w\in C_{\lambda}}t^{\operatorname{exc}(w)}=\sum_{i=0}^{\lfloor{(n-a_{1})/2}\rfloor}\gamma_{i}t^{i}(1+t)^{n-a_{1}-2i}, |  |

where γ i = 2 − n + a 1 + 2 ​ i ​ | { w ∈ C λ: cval ⁡ ( w) = i } | subscript 𝛾 𝑖 superscript 2 𝑛 subscript 𝑎 1 2 𝑖 conditional-set 𝑤 subscript 𝐶 𝜆 cval 𝑤 𝑖 \gamma_{i}=2^{-n+a_{1}+2i}|\{w\in C_{\lambda}:\operatorname{cval}(w)=i\}|.

From this we can compute, essentially by differentiating twice to get the generating function for exc 2 superscript exc 2 \operatorname{exc}^{2}, the second moment over the conjugacy class C λ subscript 𝐶 𝜆 C_{\lambda}:

 | 𝔼 λ ​ [exc 2] = ( n − a 1) ​ ( n − a 1 + 1) 4 − 1 2 ​ 𝔼 λ ​ [cval] = ( n − a 1) 2 4 + n − a 1 4 − n − a 1 + a 2 6, subscript 𝔼 𝜆 delimited-[] superscript exc 2 𝑛 subscript 𝑎 1 𝑛 subscript 𝑎 1 1 4 1 2 subscript 𝔼 𝜆 delimited-[] cval superscript 𝑛 subscript 𝑎 1 2 4 𝑛 subscript 𝑎 1 4 𝑛 subscript 𝑎 1 subscript 𝑎 2 6 \mathbb{E}_{\lambda}[\operatorname{exc}^{2}]=\frac{(n-a_{1})(n-a_{1}+1)}{4}-\frac{1}{2}\mathbb{E}_{\lambda}[\operatorname{cval}]=\frac{(n-a_{1})^{2}}{4}+\frac{n-a_{1}}{4}-\frac{n-a_{1}+a_{2}}{6}, |  |

and therefore the variance

 | Var λ ⁡ [exc] = 𝔼 λ ​ [exc 2] − ( n − a 1) 2 4 = n − a 1 − 2 ​ a 2 12. subscript Var 𝜆 exc subscript 𝔼 𝜆 delimited-[] superscript exc 2 superscript 𝑛 subscript 𝑎 1 2 4 𝑛 subscript 𝑎 1 2 subscript 𝑎 2 12 \operatorname{Var}_{\lambda}[\operatorname{exc}]=\mathbb{E}_{\lambda}[\operatorname{exc}^{2}]-\frac{(n-a_{1})^{2}}{4}=\frac{n-a_{1}-2a_{2}}{12}. |  |

Hence we obtain, using Lemma 6.1, the second moment over all of S n subscript 𝑆 𝑛 S_{n},

 | 𝔼 S n ​ [exc 2] = ( 3 ​ n − 2) ​ ( n + 1) 12, subscript 𝔼 subscript 𝑆 𝑛 delimited-[] superscript exc 2 3 𝑛 2 𝑛 1 12 \mathbb{E}_{S_{n}}[\operatorname{exc}^{2}]=\frac{(3n-2)(n+1)}{12}, |  |

and the variance over all of S n subscript 𝑆 𝑛 S_{n},

 | Var S n ⁡ [exc] = n − 2 12. subscript Var subscript 𝑆 𝑛 exc 𝑛 2 12 \operatorname{Var}_{S_{n}}[\operatorname{exc}]=\frac{n-2}{12}. |  |

## 7 Permutation constraints and higher moments

In this section, we examine permutation statistics that track permutations respecting a specified partial function. Somewhat surprisingly, this notion captures the entire class of permutation statistics. This formulation allows us to extend a technique of Fulman [Ful98, Theorem 3] to establish an independence result for the k 𝑘 k th moment ( k ≥ 1 𝑘 1 k\geq 1) across individual conjugacy classes of arbitrary permutation statistics, provided each part of the indexing permutation is sufficiently large. Fulman [Ful98, Corollary 5] established the analogous result for d ​ ( ω) 𝑑 𝜔 d(\omega) and maj maj \operatorname{maj}. In the symmetric case, we also show that these higher moments are polynomials in n 𝑛 n.

We first start by defining the notion of a permutation constraint statistic.

###### Definition 7.1.

Suppose we have a set of pairs K:= { ( i 1, j 1), ( i 2, j 2), …, ( i ℓ, j ℓ) } assign 𝐾 subscript 𝑖 1 subscript 𝑗 1 subscript 𝑖 2 subscript 𝑗 2 … subscript 𝑖 ℓ subscript 𝑗 ℓ K:=\{(i_{1},j_{1}),(i_{2},j_{2}),\dots,(i_{\ell},j_{\ell})\} with each i t ∈ [n], j t ∈ [n] formulae-sequence subscript 𝑖 𝑡 delimited-[] 𝑛 subscript 𝑗 𝑡 delimited-[] 𝑛 i_{t}\in[n],j_{t}\in[n]. We call this a (permutation) constraint and say it has size m 𝑚 m if K 𝐾 K contains m 𝑚 m pairs. Note that since K 𝐾 K is a set, repeated pairs are not allowed. We say ω ∈ S n 𝜔 subscript 𝑆 𝑛 \omega\in S_{n} satisfies K 𝐾 K if for each ( i t, j t) ∈ K subscript 𝑖 𝑡 subscript 𝑗 𝑡 𝐾 (i_{t},j_{t})\in K, ω ​ ( i t) = j t 𝜔 subscript 𝑖 𝑡 subscript 𝑗 𝑡 \omega(i_{t})=j_{t}. We say that K 𝐾 K is well-defined if all the i t ∈ [n] subscript 𝑖 𝑡 delimited-[] 𝑛 i_{t}\in[n] are distinct and all the j t ∈ [n] subscript 𝑗 𝑡 delimited-[] 𝑛 j_{t}\in[n] are distinct; note that some i t subscript 𝑖 𝑡 i_{t} may be equal to some j s subscript 𝑗 𝑠 j_{s}. Define the support of a constraint K 𝐾 K to be the set of all (distinct) i t subscript 𝑖 𝑡 i_{t} and j s subscript 𝑗 𝑠 j_{s}.

Given a constraint K 𝐾 K, construct the graph G ​ ( K) 𝐺 𝐾 G(K) on vertices [n] delimited-[] 𝑛 [n] by drawing an edge between each pair ( i t, j t) subscript 𝑖 𝑡 subscript 𝑗 𝑡 (i_{t},j_{t}). We say that K 𝐾 K is *acyclic of size m 𝑚 m*if K 𝐾 K is well-defined and G ​ ( K) 𝐺 𝐾 G(K) is acyclic with m 𝑚 m edges. Note that the graph constructed from a set of acyclic constraints will be a set of disconnected directed paths.

###### Example 7.2.

Consider the constraint K = { ( 1, 2), ( 2, 3) } 𝐾 1 2 2 3 K=\{(1,2),(2,3)\} of size 2 2 2. The permutation ( 1234) 1234 (1234) satisfies K 𝐾 K, as ( 1234) 1234 (1234) maps 1 ↦ 2 maps-to 1 2 1\mapsto 2 (specified by ( 1, 2) ∈ K 1 2 𝐾 (1,2)\in K) and 2 ↦ 3 maps-to 2 3 2\mapsto 3 (specified by ( 2, 3) ∈ K 2 3 𝐾 (2,3)\in K). Intuitively, permutations that satisfy K 𝐾 K contain 123 123 123 as a subsequence within the same cycle.

###### Example 7.3.

Consider the acyclic constraint K = { ( 1, 2), ( 2, 3), ( 3, 4) } 𝐾 1 2 2 3 3 4 K=\{(1,2),(2,3),(3,4)\} of size 3 3 3. The permutation ( 1234) 1234 (1234) satisfies K 𝐾 K. Now the graph arising from K 𝐾 K as in Definition 7.1 is acyclic – in particular, observe that the constraint ( 4, 1) ∉ K 4 1 𝐾 (4,1)\not\in K. Nonetheless, ( 1234) 1234 (1234) is a closed cycle. Thus, there may be cycles in the support of a constraint K 𝐾 K, even when K 𝐾 K is itself acyclic.

Permutation constraints induce statistics on S n subscript 𝑆 𝑛 S_{n}, which we formalize as follows.

###### Definition 7.4.

Let 𝒞 𝒞 \mathcal{C} be a set of permutation constraints. The *size*of 𝒞 𝒞 \mathcal{C}, denoted size ​ ( 𝒞) size 𝒞 \text{size}(\mathcal{C}), is the maximum of the sizes of the constraints in 𝒞 𝒞 \mathcal{C}. Note that while the size of a single constraint K ∈ 𝒞 𝐾 𝒞 K\in\mathcal{C} is simply its size as a set, this is not true for a set of constraints 𝒞 𝒞 \mathcal{C}.

###### Definition 7.5.

A weighted constraint statistic X 𝑋 X is any statistic which can be expressed in the form ∑ K ∈ 𝒞 wt ​ ( K) ​ I K subscript 𝐾 𝒞 wt 𝐾 subscript 𝐼 𝐾 \sum_{K\in\mathcal{C}}\text{wt}(K)I_{K} where 𝒞 𝒞 \mathcal{C} is a set of constraints, I K subscript 𝐼 𝐾 I_{K} is the indicator function that a permutation satisfies the constraint K 𝐾 K, and weights wt ​ ( K) ∈ ℝ ∖ { 0 } wt 𝐾 ℝ 0 \text{wt}(K)\in\mathbb{R}\setminus\{0\} for all K 𝐾 K. In this case, we say X 𝑋 X is *realizable*over 𝒞 𝒞 \mathcal{C}. If X 𝑋 X can be expressed in this form with wt ​ ( K) = 1 wt 𝐾 1 \text{wt}(K)=1 for all K ∈ 𝒞 𝐾 𝒞 K\in\mathcal{C}, then X 𝑋 X is the unweighted constraint statistic induced by 𝒞 𝒞 \mathcal{C}.

Note that in general, the decomposition ∑ K ∈ 𝒞 wt ​ ( K) ​ I K subscript 𝐾 𝒞 wt 𝐾 subscript 𝐼 𝐾 \sum_{K\in\mathcal{C}}\text{wt}(K)I_{K} is not unique. The *size*of a weighted constraint statistic X 𝑋 X is defined as

 | size ​ ( X) = min ⁡ { size ​ ( 𝒞) | X = ∑ K ∈ 𝒞 wt ​ ( K) ​ I K ​ for wt ​ ( K) ∈ ℝ ∖ { 0 } }. size 𝑋 conditional size 𝒞 𝑋 subscript 𝐾 𝒞 wt 𝐾 subscript 𝐼 𝐾 for wt 𝐾 ℝ 0 \text{size}(X)=\min\left\{\text{size}(\mathcal{C})\,\bigg{|}\,X=\sum_{K\in\mathcal{C}}\text{wt}(K)I_{K}\text{ for }\text{wt}(K)\in\mathbb{R}\setminus\{0\}\right\}. |  |

###### Remark 7.6.

It turns out that the class of weighted constraint statistics actually captures all permutation statistics. Fix n ≥ 1 𝑛 1 n\geq 1. For a permutation ω ∈ S n 𝜔 subscript 𝑆 𝑛 \omega\in S_{n}, consider its graph 𝒢 ω = { ( i, ω ​ ( i)): i ∈ [n] } subscript 𝒢 𝜔 conditional-set 𝑖 𝜔 𝑖 𝑖 delimited-[] 𝑛 \mathcal{G}_{\omega}=\{(i,\omega(i)):i\in[n]\}. The indicator for the constraint induced by 𝒢 ω subscript 𝒢 𝜔 \mathcal{G}_{\omega} is precisely the indicator function for the constraint specified by the permutation ω 𝜔 \omega. The class of weighted constraint statistics includes indicator functions for any single permutation, as well as ℝ ℝ \mathbb{R} -linear combinations of them. This in turn captures the algebra of functions from S n → ℝ → subscript 𝑆 𝑛 ℝ S_{n}\to\mathbb{R}.

In this section, we will establish independence results for higher moments of permutation statistics on individual conjugacy classes, provided all parts of the indexing partition are sufficiently large compared to the size of the statistic. Thus, when investigating an individual permutation statistic X 𝑋 X, it is of interest to exhibit *small*constraint sets that realize X 𝑋 X.

###### Remark 7.7.

Any unweighted constraint statistic X 𝑋 X can also be considered as a weighted constraint statistic. In general, the size of X 𝑋 X as an unweighted permutation constraint statistic may be different than when viewing it as a weighted constraint statistic, though we only consider the notion of size for weighted constraint statistics.

The above definitions are a little abstract and very general, so we first give a few familiar examples.

###### Example 7.8.

The number of fixed points is a constraint statistic of size 1 1 1. To see this, let 𝒞 fix subscript 𝒞 fix \mathcal{\mathcal{C}_{\text{fix}}} be the set of all constraints { { ( i, i) }: i = 1, …, n } conditional-set 𝑖 𝑖 𝑖 1 … 𝑛 \{\{(i,i)\}:i=1,\dots,n\}. Then we have

 | Fix ​ ( ω) = ∑ K ∈ 𝒞 fix I K ​ ( ω). Fix 𝜔 subscript 𝐾 subscript 𝒞 fix subscript 𝐼 𝐾 𝜔 \text{Fix}(\omega)=\sum_{K\in\mathcal{C}_{\text{fix}}}I_{K}(\omega). |  |

###### Example 7.9.

Let 𝒞 i, j subscript 𝒞 𝑖 𝑗 \mathcal{C}_{i,j} be the set of all constraints { { ( i, a), ( j, b) } \{\{(i,a),(j,b)\}: a > b } a>b\}. Then we may express des, maj des maj \operatorname{des},\operatorname{maj}, and inv inv \operatorname{inv} in terms of these, meaning that these are weighted constraint statistics of size at most 2 2 2 (and indeed, des des \operatorname{des} and inv inv \operatorname{inv} are unweighted). In particular define the following:

- •

𝒞 inv = ∪ 1 ≤ i < j ≤ n 𝒞 i, j subscript 𝒞 inv subscript 1 𝑖 𝑗 𝑛 subscript 𝒞 𝑖 𝑗 \mathcal{C}_{\text{inv}}=\cup_{1\leq i<j\leq n}\mathcal{C}_{i,j}, and

- •

𝒞 des = ∪ 1 ≤ i ≤ n − 1 𝒞 i, i + 1 subscript 𝒞 des subscript 1 𝑖 𝑛 1 subscript 𝒞 𝑖 𝑖 1 \mathcal{C}_{\text{des}}=\cup_{1\leq i\leq n-1}\mathcal{C}_{i,i+1}.

Then setting wt ​ ( { ( i, a), ( j, b) }):= i assign wt 𝑖 𝑎 𝑗 𝑏 𝑖 \text{wt}(\{(i,a),(j,b)\}):=i, we obtain

 | maj ⁡ ( ω) = ∑ K ∈ 𝒞 des wt ​ ( K) ​ I K ​ ( ω). maj 𝜔 subscript 𝐾 subscript 𝒞 des wt 𝐾 subscript 𝐼 𝐾 𝜔 \operatorname{maj}(\omega)=\sum_{K\in\mathcal{C}_{\text{des}}}\text{wt}(K)I_{K}(\omega). |  |

Similar formulas exist for des des \operatorname{des} and inv inv \operatorname{inv}. We can also obtain more general statistics such as cyclic descents. For example,

 | 𝒞 cdes = 𝒞 des ∪ 𝒞 n, 1. subscript 𝒞 cdes subscript 𝒞 des subscript 𝒞 𝑛 1 \mathcal{C}_{\operatorname{cdes}}=\mathcal{C}_{\operatorname{des}}\cup\mathcal{C}_{n,1}. |  |

Then in a similar manner to before we have that

 | cdes ⁡ ( ω) = ∑ K ∈ 𝒞 cdes I K ​ ( ω). cdes 𝜔 subscript 𝐾 subscript 𝒞 cdes subscript 𝐼 𝐾 𝜔 \operatorname{cdes}(\omega)=\sum_{K\in\mathcal{C}_{\operatorname{cdes}}}I_{K}(\omega). |  |

Note that these statistics actually have size equal to 2 2 2. This fact follows from our work on first moments, combined with Corollary 7.17 below.

We give another example of a weighted constraint statistic that is not a weighted inversion statistic: excedance.

###### Example 7.10.

Recall that an excedance is defined as an i ∈ [n] 𝑖 delimited-[] 𝑛 i\in[n] with ω ​ ( i) > i 𝜔 𝑖 𝑖 \omega(i)>i. We can define the corresponding set of constraints as follows:

 | 𝒞 exc = ∪ 1 ≤ i < j ≤ n { { ( i, j) } }. subscript 𝒞 exc subscript 1 𝑖 𝑗 𝑛 𝑖 𝑗 \mathcal{C}_{\operatorname{exc}}=\cup_{1\leq i<j\leq n}\{\{(i,j)\}\}. |  |

Then we have that

 | exc ⁡ ( ω) = ∑ K ∈ 𝒞 exc I K ​ ( ω). exc 𝜔 subscript 𝐾 subscript 𝒞 exc subscript 𝐼 𝐾 𝜔 \operatorname{exc}(\omega)=\sum_{K\in\mathcal{C}_{\operatorname{exc}}}I_{K}(\omega). |  |

###### Remark 7.11.

Note that weighted constraint statistics, even those that are realizable over constraints of size 2 2 2, are more general than weighted inversion statistics. Furthermore, permutation statistics realizable over constraints of size 3 3 3 already capture all 14 of the statistics from [BS21]. For instance, we will see below that the number of inversions between excedances where the greater excedance is *linked*(denoted ile) is realizable over symmetric constraints of size 3 3 3.

###### Example 7.12.

The number of inversions between excedances where the greater excedance is *linked*is defined [BS21] by

 | ile ​ ( ω):= #​ { ( i, j) ∈ [n] × [n]: i < j < ω ​ ( j) < ω ​ ( i) ​ and ​ ω − 1 ​ ( j) < j }. assign ile 𝜔 #conditional-set 𝑖 𝑗 delimited-[] 𝑛 delimited-[] 𝑛 𝑖 𝑗 𝜔 𝑗 𝜔 𝑖 and superscript 𝜔 1 𝑗 𝑗 \text{ile}(\omega):=\#\{(i,j)\in[n]\times[n]:i<j<\omega(j)<\omega(i)\text{ and }\omega^{-1}(j)<j\}. |  |

(Recall from Section 5.1 that the linked excedances of [BS21] coincide with the cyclic double ascents of [CJZ20].)

We are therefore counting occurrences of i < j 𝑖 𝑗 i<j with ω − 1 ​ ( j) < j < ω ​ ( j) < ω ​ ( i) superscript 𝜔 1 𝑗 𝑗 𝜔 𝑗 𝜔 𝑖 \omega^{-1}(j)<j<\omega(j)<\omega(i). This means we can define the following set of all constraints:

 | 𝒞 ile:= ∪ 1 ≤ i < j ≤ n { { ( i, a), ( j, b), ( k, j) }: k < j < b < a }. assign subscript 𝒞 ile subscript 1 𝑖 𝑗 𝑛 conditional-set 𝑖 𝑎 𝑗 𝑏 𝑘 𝑗 𝑘 𝑗 𝑏 𝑎 \mathcal{C}_{\text{ile}}:=\cup_{1\leq i<j\leq n}\{\{(i,a),(j,b),(k,j)\}:k<j<b<a\}. |  |

In a similar manner to before this gives

 | ile ​ ( ω) = ∑ K ∈ 𝒞 ile I K ​ ( ω). ile 𝜔 subscript 𝐾 subscript 𝒞 ile subscript 𝐼 𝐾 𝜔 \text{ile}(\omega)=\sum_{K\in\mathcal{C}_{\text{ile}}}I_{K}(\omega). |  |

###### Example 7.13.

[FZ90] The *Denert*statistic is defined by

 | den ​ ( ω):= #​ { 1 ≤ i < j ≤ n: ω ​ ( j) < ω ​ ( i) ≤ j } + #​ { 1 ≤ i < j ≤ n: ω ​ ( i) ≤ j < ω ​ ( j) } + #​ { 1 ≤ i < j ≤ n: j < ω ​ ( j) < ω ​ ( i) } assign den 𝜔 #conditional-set 1 𝑖 𝑗 𝑛 𝜔 𝑗 𝜔 𝑖 𝑗 #conditional-set 1 𝑖 𝑗 𝑛 𝜔 𝑖 𝑗 𝜔 𝑗 #conditional-set 1 𝑖 𝑗 𝑛 𝑗 𝜔 𝑗 𝜔 𝑖 \begin{split}\mathrm{den}(\omega):=&\,\#\{1\leq i<j\leq n:\omega(j)<\omega(i)\leq j\}\\ +&\,\#\{1\leq i<j\leq n:\omega(i)\leq j<\omega(j)\}\\ +&\,\#\{1\leq i<j\leq n:j<\omega(j)<\omega(i)\}\end{split} |  |

The statistic den den \mathrm{den} has the property that the joint distributions of the pairs ( exc, den) exc den (\operatorname{exc},\mathrm{den}) and ( des, maj) des maj (\operatorname{des},\operatorname{maj}) coincide. Such pairs are called Euler-Mahonian in the literature [FZ90].

Observe that den den \mathrm{den} may be realized as an unweighted constraint statistic induced by a constraint set of size 2, since we have

 | den ​ ( ω) = ∑ K ∈ 𝒞 den I K ​ ( ω) den 𝜔 subscript 𝐾 subscript 𝒞 den subscript 𝐼 𝐾 𝜔 \mathrm{den}(\omega)=\sum_{K\in\mathcal{C}_{\mathrm{den}}}I_{K}(\omega) |  |

for the set of constraints

 | 𝒞 den:= ∪ 1 ≤ i < j ≤ n { { ( i, a), ( j, b) }: b < a ≤ j } ⋃ ∪ 1 ≤ i < j ≤ n { { ( i, a), ( j, b) }: a ≤ j < b } ⋃ ∪ 1 ≤ i < j ≤ n { { ( i, a), ( j, b) }: j < b < a }. assign subscript 𝒞 den subscript 1 𝑖 𝑗 𝑛 subscript 1 𝑖 𝑗 𝑛 subscript 1 𝑖 𝑗 𝑛 conditional-set 𝑖 𝑎 𝑗 𝑏 𝑏 𝑎 𝑗 conditional-set 𝑖 𝑎 𝑗 𝑏 𝑎 𝑗 𝑏 conditional-set 𝑖 𝑎 𝑗 𝑏 𝑗 𝑏 𝑎 \begin{split}\mathcal{C}_{\mathrm{den}}:=&\cup_{1\leq i<j\leq n}\{\{(i,a),(j,b)\}:b<a\leq j\}\\ \bigcup&\cup_{1\leq i<j\leq n}\{\{(i,a),(j,b)\}:a\leq j<b\}\\ \bigcup&\cup_{1\leq i<j\leq n}\{\{(i,a),(j,b)\}:j<b<a\}.\end{split} |  |

We now give a relatively simple observation.

###### Proposition 7.14.

Let K 𝐾 K be a well-defined constraint of size m 𝑚 m. Then we have:

 | Pr S n ⁡ [ω ​ satisfies ​ K] = 1 n ​ ( n − 1) ​ ( n − 2) ​ … ​ ( n − m + 1). subscript Pr subscript 𝑆 𝑛 𝜔 satisfies 𝐾 1 𝑛 𝑛 1 𝑛 2 … 𝑛 𝑚 1 \operatorname{Pr}_{S_{n}}[\omega\text{ satisfies }K]=\frac{1}{n(n-1)(n-2)\dots(n-m+1)}. |  |

###### Proof.

Let K:= { ( i 1, j 1), ( i 2, j 2), …, ( i m, j m) } assign 𝐾 subscript 𝑖 1 subscript 𝑗 1 subscript 𝑖 2 subscript 𝑗 2 … subscript 𝑖 𝑚 subscript 𝑗 𝑚 K:=\{(i_{1},j_{1}),(i_{2},j_{2}),\dots,(i_{m},j_{m})\}, and suppose ω 𝜔 \omega satisfies K 𝐾 K. This means that we have ω ​ ( i t) = j t 𝜔 subscript 𝑖 𝑡 subscript 𝑗 𝑡 \omega(i_{t})=j_{t} for t = 1, …, m 𝑡 1 … 𝑚 t=1,\dots,m, which is possible since the constraint is well-defined. The number of permutations which satisfy these m 𝑚 m values is just the number of permutations on the remaining n − m 𝑛 𝑚 n-m symbols, which is ( n − m)! 𝑛 𝑚 (n-m)!. Therefore the probability of a random permutation satisfying K 𝐾 K is ( n − m)! / n! 𝑛 𝑚 𝑛 (n-m)!/n! as required. ∎

We are interested in the behavior of certain constraint statistics on fixed conjugacy classes. The key result of this section is the following, which says that for λ 𝜆 \lambda with all parts “large,” the probability of a permutation in C λ subscript 𝐶 𝜆 C_{\lambda} satisfying a constraint is only dependent on whether the constraint set is acyclic.

###### Lemma 7.15.

Let λ 𝜆 \lambda have all parts of size at least m + 1 𝑚 1 m+1, and let K 𝐾 K be a constraint of size m 𝑚 m. If K 𝐾 K is acyclic then we have

 | Pr λ ⁡ [ω ​ satisfies ​ K] = 1 ( n − 1) ​ ( n − 2) ​ … ​ ( n − m). subscript Pr 𝜆 𝜔 satisfies 𝐾 1 𝑛 1 𝑛 2 … 𝑛 𝑚 \displaystyle\operatorname{Pr}_{\lambda}[\omega\text{ satisfies }K]=\frac{1}{(n-1)(n-2)\dots(n-m)}. |  |

If K 𝐾 K is not acyclic then we have

 | Pr λ ⁡ [ω ​ satisfies ​ K] = 0. subscript Pr 𝜆 𝜔 satisfies 𝐾 0 \operatorname{Pr}_{\lambda}[\omega\text{ satisfies }K]=0. |  |

###### Proof.

We first note that if K 𝐾 K is not acyclic, then in order for ω 𝜔 \omega to satisfy K 𝐾 K, ω 𝜔 \omega must contain a cycle induced by constraints in K 𝐾 K. Since K 𝐾 K has size m 𝑚 m, then this cycle is of length at most m 𝑚 m. However we assumed ω 𝜔 \omega is of cycle type λ 𝜆 \lambda with all cycles of length at least m + 1 𝑚 1 m+1, so this is not possible.

Now suppose K 𝐾 K is acyclic. We fix n 𝑛 n and then prove this lemma by induction on m 𝑚 m. For m = 1 𝑚 1 m=1, we will show that

 | Pr λ ⁡ [ω ​ ( i 1) = j 1] = 1 n − 1. subscript Pr 𝜆 𝜔 subscript 𝑖 1 subscript 𝑗 1 1 𝑛 1 \operatorname{Pr}_{\lambda}[\omega(i_{1})=j_{1}]=\frac{1}{n-1}. |  |

This follows from the fact that conjugating by ( j 1 ​ k) subscript 𝑗 1 𝑘 (j_{1}\,k) for any k ≠ i 1, j 1 𝑘 subscript 𝑖 1 subscript 𝑗 1 k\neq i_{1},j_{1} maps from the set of ω 𝜔 \omega with ω ​ ( i 1) = j 1 𝜔 subscript 𝑖 1 subscript 𝑗 1 \omega(i_{1})=j_{1} to those with ω ​ ( i 1) = k 𝜔 subscript 𝑖 1 𝑘 \omega(i_{1})=k. Therefore this probability is the same for each j 1 ≠ i 1 subscript 𝑗 1 subscript 𝑖 1 j_{1}\neq i_{1}, and is zero for i 1 = j 1 subscript 𝑖 1 subscript 𝑗 1 i_{1}=j_{1} since λ 𝜆 \lambda is fixed point free. Therefore the probability is 1 / ( n − 1) 1 𝑛 1 1/(n-1) as required.

Assume the statement is true for m − 1 𝑚 1 m-1. Let A = { ( i 1, j 1), …, ( i m, j m) } 𝐴 subscript 𝑖 1 subscript 𝑗 1 … subscript 𝑖 𝑚 subscript 𝑗 𝑚 A=\{(i_{1},j_{1}),\dots,(i_{m},j_{m})\} be an acyclic constraint of size m 𝑚 m. Let λ ⊢ n proves 𝜆 𝑛 \lambda\vdash n have all parts of size at least m + 1 𝑚 1 m+1, and label the cycles of any permutation in C λ subscript 𝐶 𝜆 C_{\lambda} by c 1, …, c t subscript 𝑐 1 … subscript 𝑐 𝑡 c_{1},\dots,c_{t}. By Definition 7.4, we have

 | Pr λ ⁡ [ω ​ satisfies ​ A] subscript Pr 𝜆 𝜔 satisfies 𝐴 \displaystyle\operatorname{Pr}_{\lambda}[\omega\text{ satisfies }A] | = Pr λ ⁡ [⋀ ℓ = 1 m ω ​ ( i ℓ) = j ℓ] absent subscript Pr 𝜆 superscript subscript ℓ 1 𝑚 𝜔 subscript 𝑖 ℓ subscript 𝑗 ℓ \displaystyle=\operatorname{Pr}_{\lambda}\left[\bigwedge_{\ell=1}^{m}\omega(i_{\ell})=j_{\ell}\right] |  |

 |  | = Pr λ ⁡ [⋀ ℓ = 1 m − 1 ω ​ ( i ℓ) = j ℓ | ω ​ ( i m) = j m] ⋅ Pr λ ⁡ [ω ​ ( i m) = j m] absent ⋅ subscript Pr 𝜆 superscript subscript ℓ 1 𝑚 1 𝜔 subscript 𝑖 ℓ conditional subscript 𝑗 ℓ 𝜔 subscript 𝑖 𝑚 subscript 𝑗 𝑚 subscript Pr 𝜆 𝜔 subscript 𝑖 𝑚 subscript 𝑗 𝑚 \displaystyle=\operatorname{Pr}_{\lambda}\left[\bigwedge_{\ell=1}^{m-1}\omega(i_{\ell})=j_{\ell}\biggr{|}\,\omega(i_{m})=j_{m}\right]\cdot\operatorname{Pr}_{\lambda}[\omega(i_{m})=j_{m}] |  |

 |  | = 1 n − 1 ∑ h = 1 t Pr λ [⋀ ℓ = 1 m − 1 ( ω ( i ℓ) = j ℓ ∧ i m ∈ c h) | ω ( i m) = j m] \displaystyle=\frac{1}{n-1}\sum_{h=1}^{t}\operatorname{Pr}_{\lambda}\left[\bigwedge_{\ell=1}^{m-1}\biggr{(}\omega(i_{\ell})=j_{\ell}\land i_{m}\in c_{h}\biggr{)}\biggr{|}\,\omega(i_{m})=j_{m}\right] |  |

 |  | = 1 n − 1 ​ ∑ h = 1 t Pr λ ⁡ [⋀ ℓ = 1 m − 1 ω ​ ( i ℓ) = j ℓ | i m ∈ c h ∧ ω ​ ( i m) = j m] ⋅ Pr λ ⁡ [i m ∈ c h ∣ ω ​ ( i m) = j m]. absent 1 𝑛 1 superscript subscript ℎ 1 𝑡 ⋅ subscript Pr 𝜆 superscript subscript ℓ 1 𝑚 1 𝜔 subscript 𝑖 ℓ conditional subscript 𝑗 ℓ subscript 𝑖 𝑚 subscript 𝑐 ℎ 𝜔 subscript 𝑖 𝑚 subscript 𝑗 𝑚 subscript Pr 𝜆 subscript 𝑖 𝑚 conditional subscript 𝑐 ℎ 𝜔 subscript 𝑖 𝑚 subscript 𝑗 𝑚 \displaystyle=\frac{1}{n-1}\sum_{h=1}^{t}\operatorname{Pr}_{\lambda}\left[\bigwedge_{\ell=1}^{m-1}\omega(i_{\ell})=j_{\ell}\,\biggr{|}\,i_{m}\in c_{h}\land\omega(i_{m})=j_{m}\right]\cdot\operatorname{Pr}_{\lambda}[i_{m}\in c_{h}\mid\omega(i_{m})=j_{m}]. |  |

Notice that A ′:= { ( i 1, j 1), …, ( i m − 1, j m − 1) } assign superscript 𝐴 ′ subscript 𝑖 1 subscript 𝑗 1 … subscript 𝑖 𝑚 1 subscript 𝑗 𝑚 1 A^{\prime}:=\{(i_{1},j_{1}),\dots,(i_{m-1},j_{m-1})\} is an acyclic constraint of size m − 1 𝑚 1 m-1. Let λ ′ ​ ( h) superscript 𝜆 ′ ℎ \lambda^{\prime}(h) be the partition obtained by reducing the size of the h t ​ h superscript ℎ 𝑡 ℎ h^{th} part of λ 𝜆 \lambda by one. This is a partition of an ( n − 1) 𝑛 1 (n-1) -element set (though perhaps not [n − 1] delimited-[] 𝑛 1 [n-1]) with all parts of size at least m − 1 𝑚 1 m-1. It is then fairly straightforward to see that

 | Pr λ ⁡ [⋀ ℓ = 1 m − 1 ω ​ ( i ℓ) = j ℓ | i m ∈ c h ∧ ω ​ ( i m) = j m] = Pr λ ′ ​ ( h) ⁡ [ω ​ satisfies ​ A ′] = 1 ( n − 2) ​ ( n − 3) ​ … ​ ( n − m), subscript Pr 𝜆 superscript subscript ℓ 1 𝑚 1 𝜔 subscript 𝑖 ℓ conditional subscript 𝑗 ℓ subscript 𝑖 𝑚 subscript 𝑐 ℎ 𝜔 subscript 𝑖 𝑚 subscript 𝑗 𝑚 subscript Pr superscript 𝜆 ′ ℎ 𝜔 satisfies superscript 𝐴 ′ 1 𝑛 2 𝑛 3 … 𝑛 𝑚 \operatorname{Pr}_{\lambda}\left[\bigwedge_{\ell=1}^{m-1}\omega(i_{\ell})=j_{\ell}\,\biggr{|}\,i_{m}\in c_{h}\land\omega(i_{m})=j_{m}\right]=\operatorname{Pr}_{\lambda^{\prime}(h)}[\omega\text{ satisfies }A^{\prime}]=\frac{1}{(n-2)(n-3)\dots(n-m)}, |  |

where the last equality follows by the induction hypothesis. Note that the first term is n − 2 𝑛 2 n-2, as the probability is in S n − 1 subscript 𝑆 𝑛 1 S_{n-1}. Putting this altogether gives

 | Pr λ ⁡ [ω ​ satisfies ​ A] subscript Pr 𝜆 𝜔 satisfies 𝐴 \displaystyle\operatorname{Pr}_{\lambda}[\omega\text{ satisfies }A] | = 1 n − 1 ​ ∑ h = 1 t 1 ( n − 2) ​ ( n − 3) ​ … ​ ( n − m) ​ λ h n absent 1 𝑛 1 superscript subscript ℎ 1 𝑡 1 𝑛 2 𝑛 3 … 𝑛 𝑚 subscript 𝜆 ℎ 𝑛 \displaystyle=\frac{1}{n-1}\sum_{h=1}^{t}\frac{1}{(n-2)(n-3)\dots(n-m)}\frac{\lambda_{h}}{n} |  |

 |  | = 1 ( n − 1) ​ ( n − 2) ​ … ​ ( n − m). absent 1 𝑛 1 𝑛 2 … 𝑛 𝑚 \displaystyle=\frac{1}{(n-1)(n-2)\dots(n-m)}. |  |

This completes the inductive step and the proof. ∎

As a consequence, we obtain that for each k 𝑘 k, the k 𝑘 k th moment of these statistics is independent of conjugacy class, as long as the cycles are sufficiently long.

###### Theorem 7.16.

Let X 𝑋 X be a permutation statistic that is realizable over a constraint set of size m 𝑚 m, and fix k ≥ 1 𝑘 1 k\geq 1. If λ ⊢ n proves 𝜆 𝑛 \lambda\vdash n has all parts of size at least m ​ k + 1 𝑚 𝑘 1 mk+1, then 𝔼 λ ​ [X k] subscript 𝔼 𝜆 delimited-[] superscript 𝑋 𝑘 \mathbb{E}_{\lambda}[X^{k}] is independent of λ 𝜆 \lambda.

###### Proof.

Express X = ∑ P ∈ 𝒞 wt ​ ( P) ​ I P 𝑋 subscript 𝑃 𝒞 wt 𝑃 subscript 𝐼 𝑃 X=\sum_{P\in\mathcal{C}}\text{wt}(P)I_{P}, where size ​ ( 𝒞) = m size 𝒞 𝑚 \text{size}(\mathcal{C})=m. We start by decomposing the variable X k superscript 𝑋 𝑘 X^{k} into random indicator variables.

 | 𝔼 λ ​ [X k] subscript 𝔼 𝜆 delimited-[] superscript 𝑋 𝑘 \displaystyle\mathbb{E}_{\lambda}[X^{k}] | = ∑ P 1 ∈ 𝒞 ∑ P 2 ∈ 𝒞 … ​ ∑ P k ∈ 𝒞 ∏ i = 1 k wt ​ ( P i) ⋅ 𝔼 λ ​ [I P i] absent subscript subscript 𝑃 1 𝒞 subscript subscript 𝑃 2 𝒞 … subscript subscript 𝑃 𝑘 𝒞 superscript subscript product 𝑖 1 𝑘 ⋅ wt subscript 𝑃 𝑖 subscript 𝔼 𝜆 delimited-[] subscript 𝐼 subscript 𝑃 𝑖 \displaystyle=\sum_{P_{1}\in\mathcal{C}}\sum_{P_{2}\in\mathcal{C}}\dots\sum_{P_{k}\in\mathcal{C}}\prod_{i=1}^{k}\text{wt}(P_{i})\cdot\mathbb{E}_{\lambda}[I_{P_{i}}] |  |

 |  | = ∑ P 1 ∈ 𝒞 ∑ P 2 ∈ 𝒞 … ​ ∑ P k ∈ 𝒞 ( ∏ i = 1 k wt ​ ( P i)) ​ Pr λ ⁡ [⋀ i = 1 k ω ​ satisfies ​ P i]. absent subscript subscript 𝑃 1 𝒞 subscript subscript 𝑃 2 𝒞 … subscript subscript 𝑃 𝑘 𝒞 superscript subscript product 𝑖 1 𝑘 wt subscript 𝑃 𝑖 subscript Pr 𝜆 superscript subscript 𝑖 1 𝑘 𝜔 satisfies subscript 𝑃 𝑖 \displaystyle=\sum_{P_{1}\in\mathcal{C}}\sum_{P_{2}\in\mathcal{C}}\dots\sum_{P_{k}\in\mathcal{C}}\left(\prod_{i=1}^{k}\text{wt}(P_{i})\right)\operatorname{Pr}_{\lambda}\left[\bigwedge_{i=1}^{k}\omega\text{ satisfies }P_{i}\right]. |  |

We therefore continue by evaluating each of the individual probabilities in the sum.

Fix some tuple P 1, P 2, …, P k subscript 𝑃 1 subscript 𝑃 2 … subscript 𝑃 𝑘 P_{1},P_{2},\dots,P_{k}, and let Y 𝑌 Y be the union of all of these constraints excluding repeats. Write Y = { ( i 1, j 1), …, ( i s, j s) } 𝑌 subscript 𝑖 1 subscript 𝑗 1 … subscript 𝑖 𝑠 subscript 𝑗 𝑠 Y=\{(i_{1},j_{1}),\dots,(i_{s},j_{s})\}, noting that all the pairs are distinct. We split into three cases.

- •

Case 1: Suppose first that Y 𝑌 Y is not well defined. Then there must be some repeated i t subscript 𝑖 𝑡 i_{t} or j t subscript 𝑗 𝑡 j_{t}. Since we excluded repeats, there must be pairs of the form { ( i t, a), ( i t, b) } subscript 𝑖 𝑡 𝑎 subscript 𝑖 𝑡 𝑏 \{(i_{t},a),(i_{t},b)\} or { ( a, j t), ( b, j t) } 𝑎 subscript 𝑗 𝑡 𝑏 subscript 𝑗 𝑡 \{(a,j_{t}),(b,j_{t})\}. However ω ​ ( i t) 𝜔 subscript 𝑖 𝑡 \omega(i_{t}) and ω − 1 ​ ( j t) superscript 𝜔 1 subscript 𝑗 𝑡 \omega^{-1}(j_{t}) can only take one value, so the probability of Y 𝑌 Y being satisfied is zero.

- •

Case 2: Suppose instead that Y 𝑌 Y is not acyclic. Then by Lemma 7.15, we have that Pr λ ⁡ [w ​ satisfies ​ Y] = 0 subscript Pr 𝜆 𝑤 satisfies 𝑌 0 \operatorname{Pr}_{\lambda}[w\text{ satisfies }Y]=0.

- •

Case 3: Y 𝑌 Y is well defined, and no subsets of the values in ω ​ ( i 1) = j 1, ω ​ ( i 2) = j 2, …, ω ​ ( i s) = j s formulae-sequence 𝜔 subscript 𝑖 1 subscript 𝑗 1 formulae-sequence 𝜔 subscript 𝑖 2 subscript 𝑗 2 … 𝜔 subscript 𝑖 𝑠 subscript 𝑗 𝑠 \omega(i_{1})=j_{1},\omega(i_{2})=j_{2},\dots,\omega(i_{s})=j_{s} form a cycle. Then this is a set of acyclic constraints of size at most m ​ k 𝑚 𝑘 mk. By the previous proposition we therefore have that

 | Pr λ ⁡ [ω ​ satisfies ​ Y] = 1 ( n − 1) ​ ( n − 2) ​ … ​ ( n − s). subscript Pr 𝜆 𝜔 satisfies 𝑌 1 𝑛 1 𝑛 2 … 𝑛 𝑠 \operatorname{Pr}_{\lambda}[\omega\text{ satisfies }Y]=\frac{1}{(n-1)(n-2)\dots(n-s)}. |  |

In particular, none of these probabilities depend on the choice of λ 𝜆 \lambda, so the result follows. ∎

###### Corollary 7.17.

Let X 𝑋 X be a permutation statistic, and let λ ⊢ n proves 𝜆 𝑛 \lambda\vdash n. Suppose that 𝔼 λ ​ [X] subscript 𝔼 𝜆 delimited-[] 𝑋 \mathbb{E}_{\lambda}[X] depends on the number of parts of λ 𝜆 \lambda of size m 𝑚 m. Then any constraint set realizing X 𝑋 X must have size at least m 𝑚 m.

###### Remark 7.18.

Let 𝒞 𝒞 \mathcal{C} be a constraint set of size m 𝑚 m. Clearly, if we can express X = ∑ P ∈ 𝒞 I P 𝑋 subscript 𝑃 𝒞 subscript 𝐼 𝑃 X=\sum_{P\in\mathcal{C}}I_{P}, then any minimum-sized constraint set realizing X 𝑋 X has size at most m 𝑚 m.

The above corollary shows that calculating the first moment of X 𝑋 X even just on specific conjugacy classes allows us to obtain a lower bound on the size of X 𝑋 X. This approach allows us to explicitly calculate the size for many statistics.

Once we have determined the size of X 𝑋 X, we can then apply Theorem 7.16, so we see that information on the higher moments of X 𝑋 X can be obtained from the first moment, further highlighting the importance of the latter.

###### Remark 7.19.

It will be useful later to write the expectation 𝔼 λ ​ [X k] subscript 𝔼 𝜆 delimited-[] superscript 𝑋 𝑘 \mathbb{E}_{\lambda}[X^{k}] from Theorem 7.16 more explicitly in the unweighted case, so we do this.

Let 𝒜 𝒜 \mathcal{A} be the set of all the acyclic constraints from amongst the tuples P 1, …, P k subscript 𝑃 1 … subscript 𝑃 𝑘 P_{1},\dots,P_{k} in the sum. Let 𝒜 t subscript 𝒜 𝑡 \mathcal{A}_{t} be the set of all the acyclic constraints in 𝒜 𝒜 \mathcal{A} of size t 𝑡 t. Using the three previous cases, we may write the required expectation as

 | 𝔼 λ ​ [X k] subscript 𝔼 𝜆 delimited-[] superscript 𝑋 𝑘 \displaystyle\mathbb{E}_{\lambda}[X^{k}] | = ∑ P ∈ 𝒜 Pr λ ⁡ [ω ​ satisfies ​ P] absent subscript 𝑃 𝒜 subscript Pr 𝜆 𝜔 satisfies 𝑃 \displaystyle=\sum_{P\in\mathcal{A}}\operatorname{Pr}_{\lambda}[\omega\text{ satisfies }P] |  |

 |  | = ∑ t | 𝒜 t | ( n − 1) ​ ( n − 2) ​ … ​ ( n − t). absent subscript 𝑡 subscript 𝒜 𝑡 𝑛 1 𝑛 2 … 𝑛 𝑡 \displaystyle=\sum_{t}\frac{|\mathcal{A}_{t}|}{(n-1)(n-2)\dots(n-t)}. |  |

This number is independent of the choice of λ 𝜆 \lambda as long as it has parts of size at least m ​ k + 1 𝑚 𝑘 1 mk+1. Observe that taking X ​ ( ω) = maj ⁡ ( ω) 𝑋 𝜔 maj 𝜔 X(\omega)=\operatorname{maj}(\omega) or X ​ ( ω) = d ​ ( ω) = 1 + des ⁡ ( ω) 𝑋 𝜔 𝑑 𝜔 1 des 𝜔 X(\omega)=d(\omega)=1+\operatorname{des}(\omega) yields [Ful98, Theorem 2].

We continue by showing that when a statistic is *symmetric*, these moments are polynomial in n 𝑛 n. We now define this precisely.

###### Definition 7.20.

Let a 1, …, a n 0 ∈ [n] subscript 𝑎 1 … subscript 𝑎 subscript 𝑛 0 delimited-[] 𝑛 a_{1},\ldots,a_{n_{0}}\in[n]. A function f: { a 1, …, a n 0 } → [n]: 𝑓 → subscript 𝑎 1 … subscript 𝑎 subscript 𝑛 0 delimited-[] 𝑛 f:\{a_{1},\ldots,a_{n_{0}}\}\rightarrow[n] is *order-preserving*when a i < a j subscript 𝑎 𝑖 subscript 𝑎 𝑗 a_{i}<a_{j} if and only if f ​ ( a i) < f ​ ( a j) 𝑓 subscript 𝑎 𝑖 𝑓 subscript 𝑎 𝑗 f(a_{i})<f(a_{j}) for all i, j ∈ [n 0] 𝑖 𝑗 delimited-[] subscript 𝑛 0 i,j\in[n_{0}]. Note that any such function must be injective.

###### Definition 7.21.

Let 𝒞 𝒞 \mathcal{C} be a set of permutation constraints, and let X 𝑋 X be the unweighted constraint statistic induced by 𝒞 𝒞 \mathcal{C}. Take some P = { ( i 1, j 1) ​ … ​ ( i ℓ, j ℓ) } ∈ 𝒞 𝑃 subscript 𝑖 1 subscript 𝑗 1 … subscript 𝑖 ℓ subscript 𝑗 ℓ 𝒞 P=\{(i_{1},j_{1})\dots(i_{\ell},j_{\ell})\}\in\mathcal{C}. Let the distinct symbols amongst the i 1, …, i ℓ, j 1, …, j ℓ subscript 𝑖 1 … subscript 𝑖 ℓ subscript 𝑗 1 … subscript 𝑗 ℓ i_{1},\dots,i_{\ell},j_{1},\dots,j_{\ell} be 1 ≤ a 1 < a 2 < ⋯ < a n 0 ≤ n 1 subscript 𝑎 1 subscript 𝑎 2 ⋯ subscript 𝑎 subscript 𝑛 0 𝑛 1\leq a_{1}<a_{2}<\dots<a_{n_{0}}\leq n. If f ​ ( P):= { ( f ​ ( i 1), f ​ ( j 1)) ​ … ​ ( f ​ ( i ℓ), f ​ ( j ℓ)) } ∈ 𝒞 assign 𝑓 𝑃 𝑓 subscript 𝑖 1 𝑓 subscript 𝑗 1 … 𝑓 subscript 𝑖 ℓ 𝑓 subscript 𝑗 ℓ 𝒞 f(P):=\{(f(i_{1}),f(j_{1}))\dots(f(i_{\ell}),f(j_{\ell}))\}\in\mathcal{C} for all such choices of P ∈ 𝒞 𝑃 𝒞 P\in\mathcal{C} and order-preserving f: { a 1, …, a n 0 } → [n]: 𝑓 → subscript 𝑎 1 … subscript 𝑎 subscript 𝑛 0 delimited-[] 𝑛 f:\{a_{1},\ldots,a_{n_{0}}\}\rightarrow[n], then we say that X 𝑋 X is *symmetric*.

We start by examining how this definition relates to some familiar statistics.

- •

Inversions are symmetric: take any P = { ( a, b), ( c, d) } ∈ 𝒞 inv 𝑃 𝑎 𝑏 𝑐 𝑑 subscript 𝒞 inv P=\{(a,b),(c,d)\}\in\mathcal{C}_{\text{inv}} and any order preserving injection f: { a, b, c, d } → [n]: 𝑓 → 𝑎 𝑏 𝑐 𝑑 delimited-[] 𝑛 f:\{a,b,c,d\}\rightarrow[n]. Then we must have a < c, b > d formulae-sequence 𝑎 𝑐 𝑏 𝑑 a<c,b>d, so f ​ ( a) < f ​ ( c), f ​ ( b) > f ​ ( d) formulae-sequence 𝑓 𝑎 𝑓 𝑐 𝑓 𝑏 𝑓 𝑑 f(a)<f(c),f(b)>f(d). Therefore f ​ ( P) = { ( f ​ ( a), f ​ ( b)), ( f ​ ( c), f ​ ( d)) } ∈ 𝒞 inv 𝑓 𝑃 𝑓 𝑎 𝑓 𝑏 𝑓 𝑐 𝑓 𝑑 subscript 𝒞 inv f(P)=\{(f(a),f(b)),(f(c),f(d))\}\in\mathcal{C}_{\text{inv}}.

- •

Descents cannot be realized as symmetric constraint statistics using constraints of size 2 2 2. Let 𝒞 i, j subscript 𝒞 𝑖 𝑗 \mathcal{C}_{i,j} be as defined in Example 7.9. For example, take P = { ( 1, 5), ( 2, 4) } ∈ 𝒞 1, 2 ⊆ 𝒞 des 𝑃 1 5 2 4 subscript 𝒞 1 2 subscript 𝒞 des P=\{(1,5),(2,4)\}\,{\in\mathcal{C}_{1,2}}\subseteq\mathcal{C}_{\text{des}}. Let 1 < 3 < 4 < 5 1 3 4 5 1<3<4<5, with f ​ ( 1) = 1, f ​ ( 2) = 3, f ​ ( 4) = 4, f ​ ( 5) = 5 formulae-sequence 𝑓 1 1 formulae-sequence 𝑓 2 3 formulae-sequence 𝑓 4 4 𝑓 5 5 f(1)=1,f(2)=3,f(4)=4,f(5)=5. Then f ​ ( P) = { ( 1, 5), ( 3, 4) } ∈ 𝒞 1, 3 ⊈ 𝒞 des 𝑓 𝑃 1 5 3 4 subscript 𝒞 1 3 not-subset-of-or-equals subscript 𝒞 des f(P)=\{(1,5),(3,4)\}\,{\in\mathcal{C}_{1,3}}\not\subseteq\mathcal{C}_{\text{des}}. We may iterate on this argument, replacing ( 1, 5), ( 2, 4) 1 5 2 4 (1,5),(2,4) with arbitrary values respecting the same relative ordering. It is not clear whether descents can be realized using a symmetric constraint set of larger size.

- •

The number of inversions between excedances, as defined in [BS21], is symmetric. This is because the constraints for this statistic are exactly the ( a, b), ( c, d) 𝑎 𝑏 𝑐 𝑑 (a,b),(c,d) with a < c < d < b 𝑎 𝑐 𝑑 𝑏 a<c<d<b, so the images of these elements under an order-preserving f 𝑓 f will give another valid constraint.

Given a symmetric permutation constraint statistic on S n 0 subscript 𝑆 subscript 𝑛 0 S_{n_{0}}, there is also a natural way of extending this statistic to any S n subscript 𝑆 𝑛 S_{n}.

###### Definition 7.22.

Let X 𝑋 X be a symmetric permutation constraint statistic on S n 0 subscript 𝑆 subscript 𝑛 0 S_{n_{0}} induced by some 𝒞 𝒞 \mathcal{C} supported on [n 0] delimited-[] subscript 𝑛 0 [n_{0}]. Then for any S n subscript 𝑆 𝑛 S_{n}, we can define a symmetric permutation constraint statistic X n subscript 𝑋 𝑛 X_{n} on S n subscript 𝑆 𝑛 S_{n} by starting with the set of constraints 𝒞 𝒞 \mathcal{C} for X 𝑋 X and constructing the following set of constraints 𝒞 n subscript 𝒞 𝑛 \mathcal{C}_{n} for X n subscript 𝑋 𝑛 X_{n}.

- •

If n ≤ n 0 𝑛 subscript 𝑛 0 n\leq n_{0}, then let 𝒞 n subscript 𝒞 𝑛 \mathcal{C}_{n} contain all P ∈ 𝒞 𝑃 𝒞 P\in\mathcal{C} with support contained in [n] delimited-[] 𝑛 [n].

- •

If n > n 0 𝑛 subscript 𝑛 0 n>n_{0}, then let 𝒞 n subscript 𝒞 𝑛 \mathcal{C}_{n} contain all P ∈ 𝒞 𝑃 𝒞 P\in\mathcal{C}, as well as all f ​ ( P) 𝑓 𝑃 f(P) for all order-preserving functions f: [n 0] → [n]: 𝑓 → delimited-[] subscript 𝑛 0 delimited-[] 𝑛 f:[n_{0}]\rightarrow[n]. Note that we exclude repeated constraints in 𝒞 n subscript 𝒞 𝑛 \mathcal{C}_{n}.

Then by construction each X n subscript 𝑋 𝑛 X_{n} is symmetric. We call ( X n) subscript 𝑋 𝑛 (X_{n}) a *symmetric extension of X 𝑋 X*.

###### Example 7.23.

While the previous definition seems technical, there are several natural examples.

- •

Consider the constraint K = { ( 1, 2) } 𝐾 1 2 K=\{(1,2)\}, and define the statistic X 𝑋 X on S 2 subscript 𝑆 2 S_{2} by X = I K 𝑋 subscript 𝐼 𝐾 X=I_{K}. Then the ( X n) subscript 𝑋 𝑛 (X_{n}) are the excedance statistics.

- •

Fix ω ∈ S m 𝜔 subscript 𝑆 𝑚 \omega\in S_{m}. Let 𝒞 𝒞 \mathcal{C} be the constraints of size m 𝑚 m in S 2 ​ m subscript 𝑆 2 𝑚 S_{2m} that induce the permutation pattern statistic for ω 𝜔 \omega in S 2 ​ m subscript 𝑆 2 𝑚 S_{2m}. Then each statistic in ( X n) subscript 𝑋 𝑛 (X_{n}) is the number of appearances of the permutation pattern ω 𝜔 \omega for a given element in S n subscript 𝑆 𝑛 S_{n}. Note that choosing ω = ( 12) ∈ S 2 𝜔 12 subscript 𝑆 2 \omega=(12)\in S_{2} results in the usual inversion statistics on S n subscript 𝑆 𝑛 S_{n}.

###### Remark 7.24.

The preceding examples show that symmetric permutation constraint statistics are more general than permutation pattern statistics, as excedances cannot be expressed as a permutation pattern. See Remark 1.7 for more discussion, as well as a comparison of our work with that of Gaetz and Pierson [GP23].

###### Remark 7.25.

In general, it is necessary to consider symmetric extensions starting from some sufficiently large n 0 subscript 𝑛 0 n_{0}. Observe that both { ( 1, 2) } 1 2 \{(1,2)\} and { ( 1, 2), ( 2, 1) } 1 2 2 1 \{(1,2),(2,1)\} induce inv inv \operatorname{inv} on S 2 subscript 𝑆 2 S_{2}. However, the symmetric extension of { ( 1, 2) } 1 2 \{(1,2)\} yields the excedance statistic, while the symmetric extension of { ( 1, 2), ( 2, 1) } 1 2 2 1 \{(1,2),(2,1)\} realizes transpositions. In the preceding example, we see that the symmetric extension starting with the inversion statistic on S 4 subscript 𝑆 4 S_{4} results in the inversion statistics on all S n subscript 𝑆 𝑛 S_{n}.

With this definition in hand, we now show that when all parts of a partition are sufficiently large, the moments of any statistic constructed in this manner are given by a single polynomial dependent only on n 𝑛 n.

###### Theorem 7.26.

Fix k, m ≥ 1 𝑘 𝑚 1 k,m\geq 1. Let ( λ n) subscript 𝜆 𝑛 (\lambda_{n}) be a sequence of partitions, where λ n ⊢ n proves subscript 𝜆 𝑛 𝑛 \lambda_{n}\vdash n and all parts of λ n subscript 𝜆 𝑛 \lambda_{n} have size at least m ​ k + 1 𝑚 𝑘 1 mk+1. Let ( X n) subscript 𝑋 𝑛 (X_{n}) be a symmetric extension of a symmetric permutation statistic X = X n 0 𝑋 subscript 𝑋 subscript 𝑛 0 X=X_{n_{0}} induced by a constraint set of size m 𝑚 m. There exists a polynomial p X ​ ( n) subscript 𝑝 𝑋 𝑛 p_{X}(n) depending only on X 𝑋 X such that p X ​ ( n) = 𝔼 λ n ​ [X n k] subscript 𝑝 𝑋 𝑛 subscript 𝔼 subscript 𝜆 𝑛 delimited-[] superscript subscript 𝑋 𝑛 𝑘 p_{X}(n)=\mathbb{E}_{\lambda_{n}}[X_{n}^{k}].

###### Proof.

As in Theorem 7.16, it suffices to consider 𝒜 n = ⋃ i P n, i subscript 𝒜 𝑛 subscript 𝑖 subscript 𝑃 𝑛 𝑖 \mathcal{A}_{n}=\bigcup_{i}P_{n,i}, where the union runs over all well-defined acyclic k − limit-from 𝑘 k- tuples of constraints in X n subscript 𝑋 𝑛 X_{n}. Let 𝒜 n, t ⊆ 𝒜 n subscript 𝒜 𝑛 𝑡 subscript 𝒜 𝑛 \mathcal{A}_{n,t}\subseteq\mathcal{A}_{n} be the constraints of size t 𝑡 t. Note that each constraint P ∈ 𝒜 n 𝑃 subscript 𝒜 𝑛 P\in\mathcal{A}_{n} is a tuple of constraint, and multiple constraints may involve the same elements. Recall that the support of a constraint P = { ( i 1, j 1), …, ( i ℓ, j ℓ) } ∈ 𝒜 n 𝑃 subscript 𝑖 1 subscript 𝑗 1 … subscript 𝑖 ℓ subscript 𝑗 ℓ subscript 𝒜 𝑛 P=\{(i_{1},j_{1}),\dots,(i_{\ell},j_{\ell})\}\in\mathcal{A}_{n} is the set of distinct elements among the i 1, …, i ℓ, j 1, …, j ℓ subscript 𝑖 1 … subscript 𝑖 ℓ subscript 𝑗 1 … subscript 𝑗 ℓ i_{1},\dots,i_{\ell},j_{1},\dots,j_{\ell}. Define 𝒜 n, t, s ⊆ 𝒜 n, t subscript 𝒜 𝑛 𝑡 𝑠 subscript 𝒜 𝑛 𝑡 \mathcal{A}_{n,t,s}\subseteq\mathcal{A}_{n,t} be the constraints of size t 𝑡 t with support on s 𝑠 s elements, where acyclicity of elements in 𝒜 n, t subscript 𝒜 𝑛 𝑡 \mathcal{A}_{n,t} implies t + 1 ≤ s ≤ 2 ​ t 𝑡 1 𝑠 2 𝑡 t+1\leq s\leq 2t. Then we have from Remark 7.19 that

 | 𝔼 λ n ​ [X n k] = ∑ t = 1 m ​ k | 𝒜 n, t | ( n − 1) ​ ( n − 2) ​ … ​ ( n − t) = ∑ t = 1 m ​ k ( 1 ( n − 1) ​ ( n − 2) ​ … ​ ( n − t) ​ ∑ s = t + 1 2 ​ t | 𝒜 n, t, s |). subscript 𝔼 subscript 𝜆 𝑛 delimited-[] superscript subscript 𝑋 𝑛 𝑘 superscript subscript 𝑡 1 𝑚 𝑘 subscript 𝒜 𝑛 𝑡 𝑛 1 𝑛 2 … 𝑛 𝑡 superscript subscript 𝑡 1 𝑚 𝑘 1 𝑛 1 𝑛 2 … 𝑛 𝑡 superscript subscript 𝑠 𝑡 1 2 𝑡 subscript 𝒜 𝑛 𝑡 𝑠 \begin{split}\mathbb{E}_{\lambda_{n}}[X_{n}^{k}]&=\sum_{t=1}^{mk}\frac{|\mathcal{A}_{n,t}|}{(n-1)(n-2)\dots(n-t)}\\ &=\sum_{t=1}^{mk}\left(\frac{1}{(n-1)(n-2)\dots(n-t)}\sum_{s=t+1}^{2t}|\mathcal{A}_{n,t,s}|\right).\end{split} |  | (7.1) |

Now let 𝒜 n, t, s ′ ⊆ 𝒜 n, t, s superscript subscript 𝒜 𝑛 𝑡 𝑠 ′ subscript 𝒜 𝑛 𝑡 𝑠 \mathcal{A}_{n,t,s}^{\prime}\subseteq\mathcal{A}_{n,t,s} be the constraints that are supported on [s] delimited-[] 𝑠 [s]. Observe that when n < s 𝑛 𝑠 n<s, 𝒜 n, t, s ′ = ∅ superscript subscript 𝒜 𝑛 𝑡 𝑠 ′ \mathcal{A}_{n,t,s}^{\prime}=\emptyset, and since X n subscript 𝑋 𝑛 X_{n} is formed as the symmetric extension of X n 0 subscript 𝑋 subscript 𝑛 0 X_{n_{0}}, this 𝒜 n, t, s ′ superscript subscript 𝒜 𝑛 𝑡 𝑠 ′ \mathcal{A}_{n,t,s}^{\prime} is independent of n 𝑛 n for n ≥ s 𝑛 𝑠 n\geq s, so we call this common set 𝒜 t, s subscript 𝒜 𝑡 𝑠 \mathcal{A}_{t,s}. Furthermore, since X n subscript 𝑋 𝑛 X_{n} is symmetric, for n ≥ s 𝑛 𝑠 n\geq s, we can express

 | 𝒜 n, t, s = ⋃ f ⋃ P ∈ 𝒜 t, s f ​ ( P), subscript 𝒜 𝑛 𝑡 𝑠 subscript 𝑓 subscript 𝑃 subscript 𝒜 𝑡 𝑠 𝑓 𝑃 \mathcal{A}_{n,t,s}=\bigcup_{f}\bigcup_{P\in\mathcal{A}_{t,s}}f(P), |  |

where the first union is over all order-preserving f 𝑓 f. Now as each P 𝑃 P uses all elements of [s] delimited-[] 𝑠 [s] and each f 𝑓 f is determined by its image in [n] delimited-[] 𝑛 [n], we have that f 1 ​ ( P 1) = f 2 ​ ( P 2) subscript 𝑓 1 subscript 𝑃 1 subscript 𝑓 2 subscript 𝑃 2 f_{1}(P_{1})=f_{2}(P_{2}) can only occur if f 1 = f 2 subscript 𝑓 1 subscript 𝑓 2 f_{1}=f_{2} and P 1 = P 2 subscript 𝑃 1 subscript 𝑃 2 P_{1}=P_{2}. Then letting a t, s = | 𝒜 t, s | subscript 𝑎 𝑡 𝑠 subscript 𝒜 𝑡 𝑠 a_{t,s}=|\mathcal{A}_{t,s}|, we have that for n ≥ s 𝑛 𝑠 n\geq s,

 | | 𝒜 n, t, s | = ( n s) ​ a t, s, subscript 𝒜 𝑛 𝑡 𝑠 binomial 𝑛 𝑠 subscript 𝑎 𝑡 𝑠 |\mathcal{A}_{n,t,s}|={n\choose s}a_{t,s}, |  |

as there are ( n s) binomial 𝑛 𝑠 {n\choose s} order-preserving functions f: [s] → [n]: 𝑓 → delimited-[] 𝑠 delimited-[] 𝑛 f:[s]\to[n]. Letting I s ​ ( n) subscript 𝐼 𝑠 𝑛 I_{s}(n) be the indicator function for n ≥ s 𝑛 𝑠 n\geq s, we see that ( 7.1) can be rewritten as

 | 𝔼 λ n ​ [X n k] = ∑ t = 1 m ​ k ( 1 ( n − 1) ​ ( n − 2) ​ … ​ ( n − t) ​ ∑ s = t + 1 2 ​ t ( n s) ​ a t, s ​ I s ​ ( n)) = ∑ t = 1 m ​ k ∑ s = t + 1 2 ​ t ( n s) ​ a t, s ​ I s ​ ( n) ( n − 1) ​ ( n − 2) ​ … ​ ( n − t). subscript 𝔼 subscript 𝜆 𝑛 delimited-[] superscript subscript 𝑋 𝑛 𝑘 superscript subscript 𝑡 1 𝑚 𝑘 1 𝑛 1 𝑛 2 … 𝑛 𝑡 superscript subscript 𝑠 𝑡 1 2 𝑡 binomial 𝑛 𝑠 subscript 𝑎 𝑡 𝑠 subscript 𝐼 𝑠 𝑛 superscript subscript 𝑡 1 𝑚 𝑘 superscript subscript 𝑠 𝑡 1 2 𝑡 binomial 𝑛 𝑠 subscript 𝑎 𝑡 𝑠 subscript 𝐼 𝑠 𝑛 𝑛 1 𝑛 2 … 𝑛 𝑡 \begin{split}\mathbb{E}_{\lambda_{n}}[X_{n}^{k}]&=\sum_{t=1}^{mk}\left(\frac{1}{(n-1)(n-2)\dots(n-t)}\sum_{s=t+1}^{2t}{n\choose s}a_{t,s}I_{s}(n)\right)\\ &=\sum_{t=1}^{mk}\sum_{s=t+1}^{2t}{n\choose s}\frac{a_{t,s}I_{s}(n)}{(n-1)(n-2)\dots(n-t)}.\end{split} |  | (7.2) |

Observe that s ≥ t + 1 𝑠 𝑡 1 s\geq t+1, and when n ≥ s 𝑛 𝑠 n\geq s, we have that

 | ( n s) ⋅ 1 ( n − 1) ​ ( n − 2) ​ … ​ ( n − t) = 1 s! ⋅ n ​ ( n − 1) ​ ( n − 2) ​ … ​ ( n − s + 1) ( n − 1) ​ ( n − 2) ​ … ​ ( n − t) = 1 s! ⋅ n ​ ( n − t − 1) ​ … ​ ( n − s + 1) ⋅ binomial 𝑛 𝑠 1 𝑛 1 𝑛 2 … 𝑛 𝑡 ⋅ 1 𝑠 𝑛 𝑛 1 𝑛 2 … 𝑛 𝑠 1 𝑛 1 𝑛 2 … 𝑛 𝑡 ⋅ 1 𝑠 𝑛 𝑛 𝑡 1 … 𝑛 𝑠 1 \begin{split}\binom{n}{s}\cdot\frac{1}{(n-1)(n-2)\dots(n-t)}&=\frac{1}{s!}\cdot\frac{n(n-1)(n-2)\dots(n-s+1)}{(n-1)(n-2)\dots(n-t)}\\ &=\frac{1}{s!}\cdot n(n-t-1)\ldots(n-s+1)\end{split} |  |

is a polynomial in n 𝑛 n of degree s − t 𝑠 𝑡 s-t. Furthermore, λ n subscript 𝜆 𝑛 \lambda_{n} has all parts of size at least m ​ k + 1 > t 𝑚 𝑘 1 𝑡 mk+1>t, so n ≥ m ​ k + 1 > t 𝑛 𝑚 𝑘 1 𝑡 n\geq mk+1>t. When values of n 𝑛 n with t < n < s 𝑡 𝑛 𝑠 t<n<s are substituted, the above polynomial vanishes. Hence, we can rewrite ( 7.2) and omit the I s subscript 𝐼 𝑠 I_{s} indicator function to obtain

 | 𝔼 λ n ​ [X n k] = ∑ t = 1 m ​ k ∑ s = t + 1 2 ​ t a t, s s! ⋅ n ​ ( n − t − 1) ​ … ​ ( n − s + 1). subscript 𝔼 subscript 𝜆 𝑛 delimited-[] superscript subscript 𝑋 𝑛 𝑘 superscript subscript 𝑡 1 𝑚 𝑘 superscript subscript 𝑠 𝑡 1 2 𝑡 ⋅ subscript 𝑎 𝑡 𝑠 𝑠 𝑛 𝑛 𝑡 1 … 𝑛 𝑠 1 \begin{split}\mathbb{E}_{\lambda_{n}}[X_{n}^{k}]&=\sum_{t=1}^{mk}\sum_{s=t+1}^{2t}\frac{a_{t,s}}{s!}\cdot n(n-t-1)\ldots(n-s+1).\end{split} |  | (7.3) |

We conclude that ( 7.2) is a polynomial in n 𝑛 n of degree

 | max P ∈ 𝒜 2 ​ m ​ k ⁡ ( | supp ⁡ ( P) | − size ​ ( P)) ≤ m ​ k. ∎ subscript 𝑃 subscript 𝒜 2 𝑚 𝑘 supp 𝑃 size 𝑃 𝑚 𝑘 \max_{P\in\mathcal{A}_{2mk}}(|\operatorname{supp}(P)|-\text{size}(P))\leq mk.\qed |  |

###### Remark 7.27.

The proof of the preceding result gives a method for finding p X ​ ( n) subscript 𝑝 𝑋 𝑛 p_{X}(n), which we illustrate with an example. Consider the mean of the inversion statistic on conjugacy classes λ n subscript 𝜆 𝑛 \lambda_{n} with cycle lengths of at least 3 3 3, so that m = 2 𝑚 2 m=2 and k = 1 𝑘 1 k=1 in ( 7.3). In the summation of ( 7.2), the only nonzero values involve t = 2 𝑡 2 t=2, which implies s ∈ { 3, 4 } 𝑠 3 4 s\in\{3,4\}. Of the constraints in inv inv \operatorname{inv} using only values in the sets [3] delimited-[] 3 [3] and [4] delimited-[] 4 [4], we see that the acyclic ones that use all values are

 | 𝒜 2, 3 = { { ( 1, 3), ( 2, 1) }, { ( 1, 2), ( 3, 1) }, { ( 1, 3), ( 3, 2) }, { ( 2, 3), ( 3, 1) } }, subscript 𝒜 2 3 1 3 2 1 1 2 3 1 1 3 3 2 2 3 3 1 \mathcal{A}_{2,3}=\left\{\{(1,3),(2,1)\},\{(1,2),(3,1)\},\{(1,3),(3,2)\},\{(2,3),(3,1)\}\right\}, |  |

 | 𝒜 2, 4 = { { ( 1, 4), ( 2, 3) }, { ( 1, 4), ( 3, 2) }, { ( 1, 3), ( 4, 2) }, { ( 2, 4), ( 3, 1) }, { ( 2, 3), ( 4, 1) }, { ( 3, 2), ( 4, 1) } }. subscript 𝒜 2 4 1 4 2 3 1 4 3 2 1 3 4 2 2 4 3 1 2 3 4 1 3 2 4 1 \mathcal{A}_{2,4}=\left\{\{(1,4),(2,3)\},\{(1,4),(3,2)\},\{(1,3),(4,2)\},\{(2,4),(3,1)\},\{(2,3),(4,1)\},\{(3,2),(4,1)\}\right\}. |  |

Then ( 7.3) becomes

 | 𝔼 λ n ​ [inv] = 4 3! ⋅ n + 6 4! ⋅ n ​ ( n − 3) = 3 ​ n 2 − n 12, subscript 𝔼 subscript 𝜆 𝑛 delimited-[] inv ⋅ 4 3 𝑛 ⋅ 6 4 𝑛 𝑛 3 3 superscript 𝑛 2 𝑛 12 \mathbb{E}_{\lambda_{n}}[\operatorname{inv}]=\frac{4}{3!}\cdot n+\frac{6}{4!}\cdot n(n-3)=\frac{3n^{2}-n}{12}, |  |

which agrees with our Corollary 4.10. For higher moments, explicit description of acyclic constraints in terms of k 𝑘 k -tuples becomes significantly more complex, and this method becomes computationally very difficult.

In the case of certain statistics such as inversions, we can determine much more about the structure of this polynomial.

###### Proposition 7.28.

Let λ 𝜆 \lambda be a partition of n 𝑛 n with all parts of size at least 2 ​ k + 1 2 𝑘 1 2k+1. Then 𝔼 λ ​ [inv k] subscript 𝔼 𝜆 delimited-[] superscript inv 𝑘 \mathbb{E}_{\lambda}[\mathrm{inv}^{k}] is a polynomial in n 𝑛 n of degree 2 ​ k 2 𝑘 2k with leading coefficient 2 − 2 ​ k superscript 2 2 𝑘 2^{-2k}.

###### Proof.

The polynomiality follows from Theorem 7.26. From the proof of this Theorem we also have that

 | 𝔼 λ ​ [inv k] = ∑ t = 1 2 ​ k ∑ s = t + 1 2 ​ t a t, s s! ⋅ n ​ ( n − t − 1) ​ … ​ ( n − s + 1). subscript 𝔼 𝜆 delimited-[] superscript inv 𝑘 superscript subscript 𝑡 1 2 𝑘 superscript subscript 𝑠 𝑡 1 2 𝑡 ⋅ subscript 𝑎 𝑡 𝑠 𝑠 𝑛 𝑛 𝑡 1 … 𝑛 𝑠 1 \displaystyle\mathbb{E}_{\lambda}[\text{inv}^{k}]=\sum_{t=1}^{2k}\sum_{s=t+1}^{2t}\frac{a_{t,s}}{s!}\cdot n(n-t-1)\ldots(n-s+1). |  | (7.4) |

Recall that a t, s subscript 𝑎 𝑡 𝑠 a_{t,s} is the number k 𝑘 k -tuples { ( a, b), ( c, d) } 𝑎 𝑏 𝑐 𝑑 \{(a,b),(c,d)\} with a < c, b > d formulae-sequence 𝑎 𝑐 𝑏 𝑑 a<c,b>d that consist of t 𝑡 t distinct pairs and use exactly the elements in [s] delimited-[] 𝑠 [s]. The degree of this polynomial corresponds to when s − t ≤ 2 ​ k 𝑠 𝑡 2 𝑘 s-t\leq 2k is maximal. Note that s − t = 2 ​ k 𝑠 𝑡 2 𝑘 s-t=2k can occur only when s = 4 ​ k 𝑠 4 𝑘 s=4k and t = 2 ​ k 𝑡 2 𝑘 t=2k, so it suffices to show that a 2 ​ k, 4 ​ k subscript 𝑎 2 𝑘 4 𝑘 a_{2k,4k} is nonzero. Hence, we consider 2 ​ k 2 𝑘 2k distinct pairs using all elements in [4 ​ k] delimited-[] 4 𝑘 [4k].

There are ( 4 ​ k 4, 4, …, 4) binomial 4 𝑘 4 4 … 4 \binom{4k}{4,4,\dots,4} ways to partition [4 ​ k] delimited-[] 4 𝑘 [4k] into k 𝑘 k sets of four symbols. For each set of four symbols { a, b, c, d } 𝑎 𝑏 𝑐 𝑑 \{a,b,c,d\} suppose that a < b < c < d 𝑎 𝑏 𝑐 𝑑 a<b<c<d. Then there will be 6 6 6 ways to put this set into two pairs which relate to an inversion constraint, which are

 | { ( a, c), ( d, b) }, { ( a, d), ( b, c) }, { ( a, d), ( c, b) }, { ( b, c), ( d, a) }, { ( c, b), ( d, a) }, { ( b, d), ( c, a) }. 𝑎 𝑐 𝑑 𝑏 𝑎 𝑑 𝑏 𝑐 𝑎 𝑑 𝑐 𝑏 𝑏 𝑐 𝑑 𝑎 𝑐 𝑏 𝑑 𝑎 𝑏 𝑑 𝑐 𝑎 \{(a,c),(d,b)\},\,\{(a,d),(b,c)\},\,\{(a,d),(c,b)\},\,\{(b,c),(d,a)\},\,\{(c,b),(d,a)\},\,\{(b,d),(c,a)\}. |  |

Therefore in total we have a 2 ​ k, 4 ​ k = ( 4 ​ k 4, 4, …, 4) ​ 6 k = ( 4 ​ k)! / 4 k subscript 𝑎 2 𝑘 4 𝑘 binomial 4 𝑘 4 4 … 4 superscript 6 𝑘 4 𝑘 superscript 4 𝑘 a_{2k,4k}=\binom{4k}{4,4,\dots,4}6^{k}=(4k)!/4^{k}. Substituting this back into ( 7.4) gives a leading coefficient of 1 / 4 k 1 superscript 4 𝑘 1/4^{k} for the x 2 ​ k superscript 𝑥 2 𝑘 x^{2k} term as required. ∎

As an application, we can use polynomial interpolation on 2 ​ k + 1 2 𝑘 1 2k+1 values of n 𝑛 n to explicitly compute 𝔼 λ ​ [inv k] subscript 𝔼 𝜆 delimited-[] superscript inv 𝑘 \mathbb{E}_{\lambda}[\operatorname{inv}^{k}] when all parts of λ 𝜆 \lambda have size at least 2 ​ k + 1 2 𝑘 1 2k+1. The case of the second moment of inv inv \operatorname{inv} is given below.

###### Corollary 7.29.

Let λ 𝜆 \lambda be a partition of n 𝑛 n with all parts of size at least 5 5 5. Then

 | 𝔼 λ ​ [inv 2] = 1 16 ​ n 4 − 1 72 ​ n 3 − 1 80 ​ n 2 − 49 360 ​ n, subscript 𝔼 𝜆 delimited-[] superscript inv 2 1 16 superscript 𝑛 4 1 72 superscript 𝑛 3 1 80 superscript 𝑛 2 49 360 𝑛 \mathbb{E}_{\lambda}[\operatorname{inv}^{2}]=\frac{1}{16}n^{4}-\frac{1}{72}n^{3}-\frac{1}{80}n^{2}-\frac{49}{360}n, |  |

and consequently,

 | Var λ ⁡ [inv] = 1 36 ​ n 3 − 7 360 ​ n 2 − 49 360 ​ n. subscript Var 𝜆 inv 1 36 superscript 𝑛 3 7 360 superscript 𝑛 2 49 360 𝑛 \operatorname{Var}_{\lambda}[\operatorname{inv}]=\frac{1}{36}n^{3}-\frac{7}{360}n^{2}-\frac{49}{360}n. |  |

###### Proof.

We consider the conjugacy class C ( n) subscript 𝐶 𝑛 C_{(n)} corresponding to full cycles in S n subscript 𝑆 𝑛 S_{n}. Using code, we find the following values:

 | 𝔼 ( 5) ​ [inv 2] = 109 / 3, subscript 𝔼 5 delimited-[] superscript inv 2 109 3 \displaystyle\mathbb{E}_{(5)}[\operatorname{inv}^{2}]=109/3, |  |

 | 𝔼 ( 6) ​ [inv 2] = 1151 / 15, subscript 𝔼 6 delimited-[] superscript inv 2 1151 15 \displaystyle\mathbb{E}_{(6)}[\operatorname{inv}^{2}]=1151/15, |  |

 | 𝔼 ( 7) ​ [inv 2] = 2156 / 15, subscript 𝔼 7 delimited-[] superscript inv 2 2156 15 \displaystyle\mathbb{E}_{(7)}[\operatorname{inv}^{2}]=2156/15, |  |

 | 𝔼 ( 8) ​ [inv 2] = 247, subscript 𝔼 8 delimited-[] superscript inv 2 247 \displaystyle\mathbb{E}_{(8)}[\operatorname{inv}^{2}]=247, |  |

 | 𝔼 ( 9) ​ [inv 2] = 3977 / 10, subscript 𝔼 9 delimited-[] superscript inv 2 3977 10 \displaystyle\mathbb{E}_{(9)}[\operatorname{inv}^{2}]=3977/10, |  |

The result for 𝔼 λ ​ [inv 2] subscript 𝔼 𝜆 delimited-[] superscript inv 2 \mathbb{E}_{\lambda}[\operatorname{inv}^{2}] follows by polynomial interpolation, and Var λ ⁡ [inv] = 𝔼 λ ​ [inv 2] − ( 𝔼 λ ​ [inv]) 2 subscript Var 𝜆 inv subscript 𝔼 𝜆 delimited-[] superscript inv 2 superscript subscript 𝔼 𝜆 delimited-[] inv 2 \operatorname{Var}_{\lambda}[\operatorname{inv}]=\mathbb{E}_{\lambda}[\operatorname{inv}^{2}]-(\mathbb{E}_{\lambda}[\operatorname{inv}])^{2} then follows by direct calculation. ∎

###### Remark 7.30.

We compare Corollary 7.29 with Feller’s corresponding result for the full S n subscript 𝑆 𝑛 S_{n} [Fel68, p. 257, equations (6.1)-(6.3)]:

 | 𝔼 S n ​ [inv] = 1 4 ​ n ​ ( n − 1), subscript 𝔼 subscript 𝑆 𝑛 delimited-[] inv 1 4 𝑛 𝑛 1 \mathbb{E}_{S_{n}}[\operatorname{inv}]=\frac{1}{4}n(n-1), |  |

 | 𝔼 S n ​ [inv 2] = 1 16 ​ n 4 − 7 72 ​ n 3 + 5 48 ​ n 2 − 5 72 ​ n, subscript 𝔼 subscript 𝑆 𝑛 delimited-[] superscript inv 2 1 16 superscript 𝑛 4 7 72 superscript 𝑛 3 5 48 superscript 𝑛 2 5 72 𝑛 \mathbb{E}_{S_{n}}[\operatorname{inv}^{2}]=\frac{1}{16}n^{4}-\frac{7}{72}n^{3}+\frac{5}{48}n^{2}-\frac{5}{72}n, |  |

 | Var S n ⁡ [inv] = 1 72 ​ ( 2 ​ n 3 + 3 ​ n 2 − 5 ​ n). subscript Var subscript 𝑆 𝑛 inv 1 72 2 superscript 𝑛 3 3 superscript 𝑛 2 5 𝑛 \operatorname{Var}_{S_{n}}[\operatorname{inv}]=\frac{1}{72}(2n^{3}+3n^{2}-5n). |  |

We note that leading terms coincide.

## 8 Conclusion

In this paper, we investigated the distributions of various permutation statistics on individual conjugacy classes. We first introduced general notions of permutation statistics, including (i) weighted inversion statistics, which generalized inversions, major index, descents, and baj, and (ii) permutation constraints. We utilized the notion of permutation constraints to reason about arbitrary permutation statistics. Precisely, we showed that the higher moments are independent of the conjugacy class indexed by the partition λ ⊢ n proves 𝜆 𝑛 \lambda\vdash n, provided all parts of λ 𝜆 \lambda are sufficiently large. For permutation statistics realizable over symmetric constraints, we were further able to establish polynomiality for the higher moments on individual conjugacy classes indexed by λ ⊢ n proves 𝜆 𝑛 \lambda\vdash n, again provided that all parts of λ 𝜆 \lambda are sufficiently large. Our work leaves open several questions.

In Proposition 6.2, we showed that for any conjugacy class λ 𝜆 \lambda and a weighted inversion statistic X 𝑋 X, 𝔼 λ ​ [X] subscript 𝔼 𝜆 delimited-[] 𝑋 \mathbb{E}_{\lambda}[X] can be written as 𝔼 S n ​ [X] subscript 𝔼 subscript 𝑆 𝑛 delimited-[] 𝑋 \mathbb{E}_{S_{n}}[X] plus some error term f n X ​ ( a 1, a 2) superscript subscript 𝑓 𝑛 𝑋 subscript 𝑎 1 subscript 𝑎 2 f_{n}^{X}(a_{1},a_{2}), which is a degree 2 2 2 polynomial depending only on X 𝑋 X and a i subscript 𝑎 𝑖 a_{i} ( i = 1, 2 𝑖 1 2 i=1,2), the number of cycles of size i 𝑖 i in λ 𝜆 \lambda. As our independence results in Section 7 require that all parts of λ 𝜆 \lambda be sufficiently large, we suspect that Proposition 6.2 can be extended in the following manner.

###### Problem 8.1.

Show that 𝔼 λ ​ [X k] = 𝔼 S n ​ [X k] + f n X k ​ ( a 1, …, a 2 ​ k) subscript 𝔼 𝜆 delimited-[] superscript 𝑋 𝑘 subscript 𝔼 subscript 𝑆 𝑛 delimited-[] superscript 𝑋 𝑘 superscript subscript 𝑓 𝑛 superscript 𝑋 𝑘 subscript 𝑎 1 … subscript 𝑎 2 𝑘 \mathbb{E}_{\lambda}[X^{k}]=\mathbb{E}_{S_{n}}[X^{k}]+f_{n}^{X^{k}}(a_{1},\ldots,a_{2k}), where a i subscript 𝑎 𝑖 a_{i} is the number of cycles of length i 𝑖 i in λ 𝜆 \lambda, and f n X k superscript subscript 𝑓 𝑛 superscript 𝑋 𝑘 f_{n}^{X^{k}} is a polynomial of degree at most 2 ​ k 2 𝑘 2k, (necessarily) satisfying the condition

 | ∑ λ ⊢ n z λ − 1 ​ f n X k ​ ( a 1, …, a 2 ​ k) = 0. subscript proves 𝜆 𝑛 superscript subscript 𝑧 𝜆 1 superscript subscript 𝑓 𝑛 superscript 𝑋 𝑘 subscript 𝑎 1 … subscript 𝑎 2 𝑘 0 \sum_{\lambda\vdash n}z_{\lambda}^{-1}f_{n}^{X^{k}}(a_{1},\ldots,a_{2k})=0. |  |

Our technique in establishing Proposition 6.2 required detailed case analysis. Moving to even the second moment, the number of cases grows substantially. It would be of interest to find a tractable technique that easily extends to higher moments.

As we have not only an independence result, but also polynomiality on the higher moments of permutation statistics realizable over symmetric constraint sets, it seems plausible that such statistics admit a nice asymptotic distribution. In particular, a central limit theorem for descents on individual conjugacy classes is known [Ful98, Kim19, KL20]. We thus ask the following.

###### Problem 8.2.

Fix k, m ≥ 1 𝑘 𝑚 1 k,m\geq 1. Let ( X n) subscript 𝑋 𝑛 (X_{n}) be a symmetric extension of a symmetric permutation statistic of size m 𝑚 m. Let λ n subscript 𝜆 𝑛 \lambda_{n} be a partition of n 𝑛 n, with each part of size at least m ​ k + 1 𝑚 𝑘 1 mk+1. Establish a central limit theorem for ( X n) subscript 𝑋 𝑛 (X_{n}) on λ n subscript 𝜆 𝑛 \lambda_{n}.

While we have established that a number of statistics such as inv inv \operatorname{inv}, exc exc \operatorname{exc}, aexc aexc \operatorname{aexc}, cdasc, cdasc \text{cdasc}, and cddes are symmetric, we have been unable to show that any of the statistics in this paper are not symmetric. In particular, we do not have tractable conditions to show that a permutation statistic is not symmetric. Thus, we ask the following.

###### Problem 8.3.

Provide a characterization of when a permutation statistic is realizable over a symmetric constraint set.

In light of Theorem 7.26 and the fact that the first moment of cdes cdes \operatorname{cdes} is a rational function on any individual conjugacy class (Theorem 4.14), we have that the family ( cdes n) subscript cdes 𝑛 (\operatorname{cdes}_{n}) cannot be realized as the symmetric extension of any permutation statistic X 𝑋 X. We conjecture that no individual cdes m subscript cdes 𝑚 \operatorname{cdes}_{m} is itself symmetric. However, it is not clear how to establish this. Furthermore, we conjecture that des, maj, baj, des maj baj \operatorname{des},\operatorname{maj},\operatorname{baj}, and baj − inv baj inv \operatorname{baj}-\operatorname{inv} are not realizable over any symmetric permutation constraints or as the symmetric extensions of any permutation statistic.

Since our work in this paper establishes results for the Coxeter group of type A 𝐴 A, it is natural to ask the following.

###### Problem 8.4.

Extend the results of this paper to other Coxeter groups.

It is likely that the calculations would need to be updated to the setting of the given family of Coxeter groups being considered, but that the techniques in this paper might still apply. Ideally, one might hope for a general technique that can handle all Coxeter groups without redoing the calculations for each such family.

Given a statistic X 𝑋 X on the symmetric group S n subscript 𝑆 𝑛 S_{n}, the first moments 𝔼 λ ​ [X] subscript 𝔼 𝜆 delimited-[] 𝑋 \mathbb{E}_{\lambda}[X] are class functions, and may thus be interpreted as the character of a possibly virtual representation of S n subscript 𝑆 𝑛 S_{n}. Equation ( 6.1), which gives the first moment of X 𝑋 X on all of S n subscript 𝑆 𝑛 S_{n}, is then precisely the multiplicity of the trivial module in some (virtual) representation of S n subscript 𝑆 𝑛 S_{n}. Thus one could ask if there is a representation-theoretic interpretation of our results, beyond the connection with character polynomials as in [GP23].

###### Problem 8.5.

Investigate representation-theoretic interpretations of these results.

## References

- [BD92] Dave Bayer and Persi Diaconis. Trailing the dovetail shuffle to its lair. The Annals of Applied Probability, 2, 05 1992. [doi:10.1214/aoap/1177005705][1].
- [BKS20] Sara C. Billey, Matjaž Konvalinka, and Joshua P. Swanson. Asymptotic normality of the major index on standard tableaux. Adv. in Appl. Math., 113:101972, 36, 2020. [doi:10.1016/j.aam.2019.101972][2].
- [Bre93] Francesco Brenti. Permutation enumeration, symmetric functions, and unimodality. Pacific J. Math., 157(1):1–28, 1993. URL: [http://projecteuclid.org/euclid.pjm/1102634861][3].
- [BS21] Natasha Blitvić and Einar Steingrímsson. Permutations, moments, measures. Transactions of the American Mathematical Society, 374(08):5473–5508, 2021.
- [Cel98] Paola Cellini. Cyclic Eulerian elements. European J. Combin., 19(5):545–552, 1998. [doi:10.1006/eujc.1998.0218][4].
- [CJZ20] M. Crossan Cooper, William S. Jones, and Yan Zhuang. On the joint distribution of cyclic valleys and excedances over conjugacy classes of S n subscript 𝑆 𝑛 {S}_{n}. Adv. in Appl. Math., 115:101999, 15, 2020. [doi:10.1016/j.aam.2020.101999][5].
- [DF91] David S. Dummit and Richard M. Foote. Abstract Algebra. Prentice Hall, Inc., Englewood Cliffs, NJ, 1991.
- [DG19] Persi Diaconis and Ron Graham. 12. The Magic of Charles Sanders Peirce, pages 161–203. Princeton University Press, Princeton, 2019. [doi:10.1515/9780691194417-014][6].
- [DMP95] Persi Diaconis, Michael McGrath, and Jim Pitman. Riffle shuffles, cycles, and descents. Combinatorica, 15(1):11–29, mar 1995. [doi:10.1007/BF01294457][7].
- [DP86] Persi Diaconis and JW Pitman. Permutations, record values and random measures. Unpublished lecture notes, Statistics Department, University of California, Berkeley, 1986.
- [Fel68] William Feller. An Introduction to Probability Theory and Its Applications, volume 1. Wiley, January 1968. URL: [http://www.amazon.ca/exec/obidos/redirect?tag=citeulike04-20{&}path=ASIN/0471257087][8].
- [Foa68] Dominique Foata. On the Netto inversion number of a sequence. Proc. Amer. Math. Soc., 19:236–240, 1968. [doi:10.2307/2036179][9].
- [Foa77] Dominique Foata. Distributions eulériennes et mahoniennes sur le groupe des permutations. In Martin Aigner, editor, Higher Combinatorics, pages 27–49, Dordrecht, 1977. Springer Netherlands. [doi:10.1007/978-94-010-1220-1_2][10].
- [FS70] Dominique Foata and Marcel Paul Schützenberger. Théorie Géométrique des Polynômes Eulériens. Springer Berlin, Heidelberg, 1970. [doi:10.1007/BFb0060799][11].
- [Ful98] Jason Fulman. The distribution of descents in fixed conjugacy classes of the symmetric groups. J. Combin. Theory Ser. A, 84(2):171–180, 1998. [doi:10.1006/jcta.1998.2893][12].
- [FZ90] Dominique Foata and Doron Zeilberger. Denert’s permutation statistic is indeed Euler-Mahonian. Stud. Appl. Math., 83(1):31–59, 1990. [doi:10.1002/sapm199083131][13].
- [GP23] Christian Gaetz and Laura Pierson. Positivity of permutation pattern character polynomials. Advances in Applied Mathematics, 147:102507, 2023. [doi:10.1016/j.aam.2023.102507][14].
- [GR93] Ira M. Gessel and Christophe Reutenauer. Counting permutations with given cycle structure and descent set. Journal of Combinatorial Theory, Series A, 64(2):189–215, 1993. [doi:10.1016/0097-3165(93)90095-P][15].
- [GR20] Christian Gaetz and Christopher Ryba. Stable characters from permutation patterns. Selecta Mathematica, 27:1–13, 2020. [doi:10.1007/s00029-021-00692-9][16].
- [HR22] Zachary Hamaker and Brendon Rhoades. Characters of local and regular permutation statistics, 2022. [arXiv:2206.06567][17], [doi:10.48550/arXiv.2206.06567][18].
- [Kim19] Gene B. Kim. Distribution of descents in matchings. Annals of Combinatorics, 23:73–87, 2019. [doi:10.1007/s00026-019-00414-1][19].
- [KL20] Gene B. Kim and Sangchul Lee. Central limit theorem for descents in conjugacy classes of S n subscript 𝑆 𝑛 {S}_{n}. Journal of Combinatorial Theory, Series A, 169:105123, 2020. [doi:10.1016/j.jcta.2019.105123][20].
- [Knu98] Donald E. Knuth. The Art of Computer Programming, Volume 3: (2nd Ed.) Sorting and Searching. Addison Wesley Longman Publishing Co., Inc., USA, 1998.
- [Mac15] P. MacMahon. Combinatory analysis. Cambridge University Press, 1915.
- [Mac16] P. A. MacMahon. Two Applications of General Theorems in Combinatory Analysis: (1) To the Theory of Inversions of Permutations; (2) To the Ascertainment of the Numbers of Terms in the Development of a Determinant which has Amongst its Elements an Arbitrary Number of Zeros. Proc. London Math. Soc. (2), 15:314–321, 1916. [doi:10.1112/plms/s2-15.1.314][21].
- [Mac04] Percy A. MacMahon. Combinatory analysis. Vol. I, II (bound in one volume). Dover Phoenix Editions. Dover Publications, Inc., Mineola, NY, 2004. Reprint of ıt An introduction to combinatory analysis (1920) and ıt Combinatory analysis. Vol. I, II (1915, 1916).
- [Rio14] John Riordan. An Introduction to Combinatorial Analysis. Princeton University Press, Princeton, 2014. [doi:10.1515/9781400854332][22].
- [Rod39] M. Olinde Rodrigues. Note sur les inversions, ou dérangements produits dans les permutations. Journal De Mathématiques Pures et Appliquées, 1839.
- [Sta97] Richard P. Stanley. Enumerative Combinatorics. Vol. 1, volume 49 of Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge, 1997. With a foreword by Gian-Carlo Rota, Corrected reprint of the 1986 original. [doi:10.1017/CBO9780511805967][23].
- [Sta99] Richard P. Stanley. Enumerative Combinatorics. Vol. 2, volume 62 of Cambridge Studies in Advanced Mathematics. Cambridge University Press, Cambridge, 1999. With a foreword by Gian-Carlo Rota and appendix 1 by Sergey Fomin. [doi:10.1017/CBO9780511609589][24].
- [SW98] John R. Stembridge and Debra J. Waugh. A Weyl group generating function that ought to be better known. Indag. Math. (N.S.), 9(3):451–457, 1998. [doi:10.1016/S0019-3577(98)80012-8][25].
- [Zab03] Mike Zabrocki. A bijective proof of an unusual symmetric group generating function, 2003. [doi:10.48550/ARXIV.MATH/0310301][26].

[◄][27][image: ar5iv homepage] [28]
[Feeling lucky?][29] [30]
[Conversion report][31]
[Report an issue][32]
[View original on arXiv][33] [►][34]


## Links

[1]: https://doi.org/10.1214/aoap/1177005705
[2]: https://doi.org/10.1016/j.aam.2019.101972
[3]: http://projecteuclid.org/euclid.pjm/1102634861
[4]: https://doi.org/10.1006/eujc.1998.0218
[5]: https://doi.org/10.1016/j.aam.2020.101999
[6]: https://doi.org/10.1515/9780691194417-014
[7]: https://doi.org/10.1007/BF01294457
[8]: http://www.amazon.ca/exec/obidos/redirect?tag=citeulike04-20%7B&amp;%7Dpath=ASIN/0471257087
[9]: https://doi.org/10.2307/2036179
[10]: https://doi.org/10.1007/978-94-010-1220-1_2
[11]: https://doi.org/10.1007/BFb0060799
[12]: https://doi.org/10.1006/jcta.1998.2893
[13]: https://doi.org/10.1002/sapm199083131
[14]: https://doi.org/10.1016/j.aam.2023.102507
[15]: https://doi.org/10.1016/0097-3165(93)90095-P
[16]: https://doi.org/10.1007/s00029-021-00692-9
[17]: http://arxiv.org/abs/2206.06567
[18]: https://doi.org/10.48550/arXiv.2206.06567
[19]: https://doi.org/10.1007/s00026-019-00414-1
[20]: https://doi.org/10.1016/j.jcta.2019.105123
[21]: https://doi.org/10.1112/plms/s2-15.1.314
[22]: https://doi.org/10.1515/9781400854332
[23]: https://doi.org/10.1017/CBO9780511805967
[24]: https://doi.org/10.1017/CBO9780511609589
[25]: https://doi.org/10.1016/S0019-3577(98)80012-8
[26]: https://doi.org/10.48550/ARXIV.MATH/0310301
[27]: /html/2301.00897
[28]: /
[29]: /feeling_lucky
[30]: /land_of_honey_and_milk
[31]: /log/2301.00898
[32]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2301.00898
[33]: https://arxiv.org/abs/2301.00898
[34]: /html/2301.00899
