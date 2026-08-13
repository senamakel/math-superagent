<!-- source: https://ar5iv.labs.arxiv.org/html/1308.3133 | converted from HTML -->

[1308.3133] Intersections of multiplicative translates of 3 -adic Cantor sets

# Intersections of multiplicative translates of
3 3 -adic Cantor sets Thanks: The first author received support from an NSF Graduate Research Fellowship. The second author received support from NSF grants DMS-0801029 and DMS-1101373.

William Abram and Jeffrey C. Lagarias Address: Department of Mathematics and Computer Science, Hillsdale College, Hillsdale, MI 49242-1205,USA Email address: [wabram@hillsdale.edu][1] Address: Department of Mathematics, University of Michigan, Ann Arbor, MI 48109-1043,USA Email address: [lagarias@umich.edu][2]

Date: August 13, 2013

###### Abstract.

Motivated by a question of Erdős, this paper considers questions concerning the discrete dynamical system on the 3 3 -adic integers ℤ 3 \mathbb{Z}_{3} given by multiplication by 2 2. Let the 3 3 -adic Cantor set Σ 3, 2 ¯ \Sigma_{3,\bar{2}} consist of all 3 3 -adic integers whose expansions use only the digits 0 0 and 1 1. The exceptional set ℰ ⁡ ( ℤ 3) \mathcal{E}(\mathbb{Z}_{3}) is the set of all elements of ℤ 3 \mathbb{Z}_{3} whose forward orbits under this action intersects the 3 3 -adic Cantor set Σ 3, 2 ¯ \Sigma_{3,\bar{2}} infinitely many times. It has been shown that this set has Hausdorff dimension at most 1 2 \frac{1}{2} and it has been conjectured that it has Hausdorff dimension 0 0. Approaches to upper bounds on the Hausdorff dimensions of these sets leads to study of intersections of multiplicative translates of Cantor sets by powers of 2 2. More generally, this paper studies the structure of finite intersections of general multiplicative translates S = Σ 3, 2 ¯ ∩ 1 M 1 ​ Σ 3, 2 ¯ ∩ ⋯ ∩ 1 M n ​ Σ 3, 2 ¯ S=\Sigma_{3,\bar{2}}\cap\frac{1}{M_{1}}\Sigma_{3,\bar{2}}\cap\cdots\cap\frac{1}{M_{n}}\Sigma_{3,\bar{2}} by integers 1 < M 1 < M 2 < ⋯ < M n 1<M_{1}<M_{2}<\cdots<M_{n}. These sets are describable as sets of 3 3 -adic integers whose 3 3 -adic expansions have one-sided symbolic dynamics given by a finite automaton. As a consequence, the Hausdorff dimension of such a set is always of the form log 3 ⁡ ( β) \log_{3}(\beta) where β \beta is an algebraic integer. This paper gives a method to determine the automaton for given data ( M 1, …, M n) (M_{1},...,M_{n}). Experimental results indicate that the Hausdorff dimension of such sets depends in a very complicated way on the integers M 1, …, M n M_{1},...,M_{n}.

## 1. Introduction

We study the following problem. Let the 3 3 -adic Cantor set Σ 3:= Σ 3, 2 ¯ \Sigma_{3}:=\Sigma_{3,\bar{2}} be the subset of all 3 3 -adic integers whose 3 3 -adic expansions consist of digits 0 0 and 1 1 only. This set is a well-known fractal having Hausdorff dimension dim H ( Σ 3) = log 3 ⁡ 2 ≈ 0.630929 \dim_{H}(\Sigma_{3})=\log_{3}2\approx 0.630929. By a multiplicative translate of such a Cantor set we mean a multiplicatively rescaled set r ​ Σ 3 = { r ​ x: x ∈ Σ 3 } r\Sigma_{3}=\{rx:x\in\Sigma_{3}\}, where we restrict to r = p q ∈ ℚ × r=\frac{p}{q}\in{\mathbb{Q}}^{\times} being a rational number that is 3 3 -integral, meaning that 3 3 does not divide q q, In this paper we study sets given as finite intersections of such multiplicative translates:

 | C ⁡ ( r 1, r 2, ⋯, r n):= ⋂ i = 1 n 1 r i ​ Σ 3, C(r_{1},r_{2},\cdots,r_{n}):=\bigcap_{i=1}^{n}\frac{1}{r_{i}}\Sigma_{3}, |  | (1.1) |

where now each 1 r i \frac{1}{r_{i}} is 3 3 -integral. These sets are fractals and our object is to obtain bounds on their Hausdorff dimensions. Our motivation for studying this problem arose from a problem of Erdős [8] which is described in Section 1.1.

In principle the Hausdorff dimensions of sets C ⁡ ( r 1, r 2, ⋯, r n) C(r_{1},r_{2},\cdots,r_{n}) are explicitly computable in a closed form. This comes about as follows. We show each such set has the property that the 3 3 -adic expansions of all the members of C ⁡ ( r 1, r 2, ⋯, r n) C(r_{1},r_{2},\cdots,r_{n}) are characterizable as the output labels of all infinite paths in a labeled finite automaton which start from a marked initial vertex. General sets of such path labels associated to a finite automaton form symbolic dynamical systems that we call path sets and which we study in [1]. The sets C ⁡ ( r 1, r 2, ⋯, r n) C(r_{1},r_{2},\cdots,r_{n}) are then p p -adic path set fractals (with p = 3 p=3), using terminology we introduced in [2]. These sets are collections of all p p -adic numbers whose p p -adic expansions have digits described by the labels along infinite paths according to a digit assignment map taking path labels in the graph to p p -adic digits. In [2, Theorem 2.10] we showed that a p p -adic path set fractal is any set Y Y in ℤ p {\mathbb{Z}}_{p} constructed by a p p -adic analogue of a real number graph-directed fractal construction, as given in Mauldin and Williams [16]. This geometric object Y Y is given as the set-valued fixed point of a dilation functional equation using a set of p p -adic affine maps, cf. [2, Theorem 2.6]. We showed in [2, Theorem 1.4] that the if X X is a p p -adic path set fractal then any multiplicative translate r ​ X rX by a p p -integral rational number r r is also a p p -adic path set fractal. In addition p p -adic path set fractals are closed under set intersection, a property they inherit from path sets, see [1, Theorem 1.2]. Since the 3 3 -adic Cantor set is a 3 3 -adic path set fractal, the full shift on two symbols, these closure properties immediately imply that every set C ⁡ ( r 1, r 2, …, r n) C(r_{1},r_{2},...,r_{n}) is a 3 3 -adic path set fractal.

In [2, Theorem 1.1] we showed that the Hausdorff dimension of a p p -adic path set fractal X X is directly computable from the adjacency matrix of a suitable presentation X X. One has

 | dim H ( X) = log p ⁡ β, \dim_{H}(X)=\log_{p}\beta, |  |

in which β \beta is the spectral radius ρ ⁡ ( 𝐀) \rho(\mathbf{A}) of the adjacency matrix 𝐀 \mathbf{A} of a finite automaton which gives a suitable presentation of the given path set; see Section 2. This spectral radius coincides with the Perron eigenvalue ( [13, Definition 4.4.2]) of the nonnegative integer matrix 𝐀 ≠ 0 \mathbf{A}\neq 0, which is the largest real eigenvalue β ≥ 0 \beta\geq 0 of 𝐀 \mathbf{A}. For adjacency matrices of graphs containing at least one directed cycle, which are nonnegative integer matrices, the Perron eigenvalue is necessarily a real algebraic integer, and also has β ≥ 1. \beta\geq 1. In the case at hand we know a priori that 1 ≤ β ≤ 2. 1\leq\beta\leq 2. Everything here is algorithmically effective, as discussed in Sections 2 and 3.

This paper presents theoretical and experimental results about these sets. In Section 3 we give an algorithm to compute an efficient presentation of the underlying path set of 𝒞 ⁡ ( 1, M) \mathcal{C}(1,M) for integers M ≥ 1 M\geq 1, which is simpler than the general constructions given in [1], [2]. We extend this method to 𝒞 ⁡ ( 1, M 1, M 2, …, M n) \mathcal{C}(1,M_{1},M_{2},...,M_{n}). We give a complete analysis of the structure of the resulting path set presentations for two infinite families 𝒞 ⁡ ( 1, M k) \mathcal{C}(1,M_{k}) of integers { M k: k ≥ 1 } \{M_{k}:k\geq 1\} whose 3 3 -adic expansions take an especially simple form. These examples exhibit rather complicated automata in the presentations. We experimentally use the algorithm for 𝒞 ⁡ ( 1, M 1, M 2, …, M n) \mathcal{C}(1,M_{1},M_{2},...,M_{n}) to compute various examples indicating that the automata depend in an extremely complicated way on 3 3 -adic arithmetic properties of M M. This complexity is reflected in the behavior of the Hausdorff dimension function, and leads to many open questions.

### 1.1. Motivation: Erdős problem

Erdős [8] conjectured that for every n ≥ 9 n\geq 9, the ternary expansion of 2 n 2^{n} contains the ternary digit 2 2. A weak version of this conjecture asserts that there are finitely many n n such that the ternary expansion of 2 n 2^{n} consists of 0 0 ’s and 1 1 ’s. Both versions of this conjecture appear difficult.

In [11] the second author proposed a 3 3 -adic generalization of this problem, as follows. Let ℤ 3 \mathbb{Z}_{3} denote the 3 3 -adic integers, and let a 3 3 -adic integer α \alpha have 3 3 -adic expansion

 | ( α) 3:= ( ⋯ a 2 a 1 a 0) 3 = a 0 + a 1 ⋅ 3 + a 2 ⋅ 3 2 + ⋯, with all a i ∈ { 0, 1, 2 }. (\alpha)_{3}:=(\cdots a_{2}a_{1}a_{0})_{3}=a_{0}+a_{1}\cdot 3+a_{2}\cdot 3^{2}+\cdots,~~\mbox{with all}~~a_{i}\in\{0,1,2\}. |  |

###### Definition 1.1.

The 3 3 -adic exceptional set ℰ ⁡ ( ℤ 3) \mathcal{E}(\mathbb{Z}_{3}) is defined by

 | ℰ ⁡ ( ℤ 3):= { λ ∈ ℤ 3: for infinitely many n ≥ 0 the expansion ( 2 n ​ λ) 3 omits the digit 2 }. \mathcal{E}(\mathbb{Z}_{3}):=\{\lambda\in\mathbb{Z}_{3}:\text{for infinitely many $n\geq 0$ the expansion $(2^{n}\lambda)_{3}$ omits the digit $2$}\}. |  |

The weak version of Erdős’s conjecture above is equivalent to the assertion that ℰ ⁡ ( ℤ 3) \mathcal{E}(\mathbb{Z}_{3}) does not contain the integer 1 1.

The exceptional set seems an interesting object in its own right. It is forward invariant under multiplication by 2 2, and one may expect it to be a very small set in terms of measure or dimension. At present it remains possible that the ℰ ⁡ ( ℤ 3) \mathcal{E}(\mathbb{Z}_{3}) is a countable set, or even that it consists of the single element { 0 }. \{0\}. In 2009 the second author put forward the following conjecture asserting that the exceptional set is small in the sense of Hausdorff dimension ( [11, Conjecture 1.7]).

###### Conjecture 1.2.

(Exceptional Set Conjecture) The 3 3 -adic exceptional set ℰ ⁡ ( ℤ 3) \mathcal{E}(\mathbb{Z}_{3}) has Hausdorff dimension zero, i.e.

 | dim H ( ℰ ⁡ ( ℤ 3)) = 0. \dim_{H}(\mathcal{E}(\mathbb{Z}_{3}))=0. |  | (1.2) |

As limited evidence in favor of this conjecture, the paper [11] showed that the Hausdorff dimension of ℰ ⁡ ( ℤ 3) \mathcal{E}(\mathbb{Z}_{3}) is at most 1 2, \frac{1}{2}, as explained below. That paper initiated a strategy to obtain upper bounds for dim H ( ℰ ⁡ ( ℤ 3)) \dim_{H}(\mathcal{E}(\mathbb{Z}_{3})) based on the containment relation

 | ℰ ⁡ ( ℤ 3) ⊆ ⋂ k = 1 ∞ ℰ ( k) ​ ( ℤ 3), \mathcal{E}(\mathbb{Z}_{3})\subseteq\bigcap_{k=1}^{\infty}\mathcal{E}^{(k)}(\mathbb{Z}_{3}), |  | (1.3) |

where

 | ℰ ( k) ​ ( ℤ 3):= { λ ∈ ℤ 3: at least k values of ( 2 n ​ λ) 3 omit the digit 2 }. \mathcal{E}^{(k)}(\mathbb{Z}_{3}):=\{\lambda\in\mathbb{Z}_{3}:\text{at least $k$ values of $(2^{n}\lambda)_{3}$ omit the digit 2}\}. |  | (1.4) |

These sets form a nested family

 | Σ 3, 2 ¯ = ℰ ( 1) ​ ( ℤ 3) ⊇ ℰ ( 2) ​ ( ℤ 3) ⊇ ℰ ( 3) ​ ( ℤ 3) ⊇ ⋯ \Sigma_{3,\bar{2}}=\mathcal{E}^{(1)}(\mathbb{Z}_{3})\supseteq\mathcal{E}^{(2)}(\mathbb{Z}_{3})\supseteq\mathcal{E}^{(3)}(\mathbb{Z}_{3})\supseteq\cdots |  |

The containment relation ( 1.3) immediately implies inequalities relating the Hausdorff dimension of these sets, namely

 | dim H ( ℰ ⁡ ( ℤ 3)) ≤ Γ, \dim_{H}(\mathcal{E}(\mathbb{Z}_{3}))\leq\Gamma, |  | (1.5) |

where Γ \Gamma is defined by

 | Γ:= lim k → ∞ dim H ( ℰ ( k) ​ ( ℤ 3)). \Gamma:=\lim_{k\to\infty}\dim_{H}(\mathcal{E}^{(k)}(\mathbb{Z}_{3})). |  | (1.6) |

The inequality ( 1.5) raises the subsidiary problem of obtaining upper bounds for Γ \Gamma, which in turn requires obtaining bounds for the individual dim H ( ℰ ( k) ​ ( ℤ 3)) \dim_{H}(\mathcal{E}^{(k)}(\mathbb{Z}_{3})). We note the possibility that dim H ( ℰ ⁡ ( ℤ 3)) < Γ \dim_{H}(\mathcal{E}(\mathbb{Z}_{3}))<\Gamma may hold.

The analysis of the sets ℰ ( k) ​ ( ℤ 3) \mathcal{E}^{(k)}(\mathbb{Z}_{3}) for k ≥ 2 k\geq 2 leads to the study of particular sets of the kind ( 1.1) considered in this paper. We have

 | ℰ ( k) ​ ( ℤ 3) = ⋃ 0 ≤ m 1 < … < m k 𝒞 ⁡ ( 2 m 1, …, 2 m k). \mathcal{E}^{(k)}(\mathbb{Z}_{3})=\bigcup_{0\leq m_{1}<\ldots<m_{k}}\mathcal{C}(2^{m_{1}},\ldots,2^{m_{k}}). |  | (1.7) |

We next give a simplification, showing that for the purposes of computing Hausdorff dimension we may, without loss of generality, restrict this set union to subsets having m 1 = 0 m_{1}=0 so that 2 m 1 = 1. 2^{m_{1}}=1.

###### Definition 1.3.

The restricted 3 3 -adic exceptional set ℰ 1 ​ ( ℤ 3) \mathcal{E}_{1}(\mathbb{Z}_{3}) is given by

 | ℰ 1 ​ ( ℤ 3):= { λ ∈ ℤ 3: for n = 0 and infinitely many other n, ( 2 n ​ λ) 3 omits the digit 2 }. \mathcal{E}_{1}(\mathbb{Z}_{3}):=\{\lambda\in\mathbb{Z}_{3}:\text{for $n=0$ and infinitely many other $n$, $(2^{n}\lambda)_{3}$ omits the digit $2$}\}. |  |

It is easy to see that

 | ℰ ⁡ ( ℤ 3) = ⋃ n = 0 ∞ 1 2 n ​ ℰ 1 ​ ( ℤ 3). \mathcal{E}(\mathbb{Z}_{3})=\bigcup_{n=0}^{\infty}\frac{1}{2^{n}}\mathcal{E}_{1}(\mathbb{Z}_{3}). |  |

Since the right side is a countable union of sets we obtain

 | dim H ( ℰ ⁡ ( ℤ 3)) = sup n ≥ 0 ( dim H ( 1 2 n ​ ℰ 1 ​ ( ℤ 3))) = dim H ( ℰ 1 ​ ( ℤ 3)). \dim_{H}(\mathcal{E}(\mathbb{Z}_{3}))=\sup_{n\geq 0}\Big(\dim_{H}(\frac{1}{2^{n}}\mathcal{E}_{1}(\mathbb{Z}_{3}))\Big)=\dim_{H}(\mathcal{E}_{1}(\mathbb{Z}_{3})). |  |

and we also have ℰ 1 ​ ( ℤ 3) ⊂ Σ 3, 2 ¯ \mathcal{E}_{1}(\mathbb{Z}_{3})\subset\Sigma_{3,\bar{2}}. Now set

 | ℰ 1 ( k) ​ ( ℤ 3):= { λ ∈ Σ 3, 2 ¯: for at least k values of n ≥ 0, ( 2 n ​ λ) 3 omits the digit 2 }. \mathcal{E}_{1}^{(k)}(\mathbb{Z}_{3}):=\{\lambda\in\Sigma_{3,\bar{2}}:\text{for at least $k$ values of $n\geq 0$, $(2^{n}\lambda)_{3}$ omits the digit 2}\}. |  |

For 0 < m 1 < m 2 < ⋯ < m k 0<m_{1}<m_{2}<\cdots<m_{k} we have the set identities

 | 𝒞 ⁡ ( 2 m 1, …, 2 m k) = 1 2 m 1 ​ 𝒞 ​ ( 1, 2 m 2 − m 1, …, 2 m k − m 1). \mathcal{C}(2^{m_{1}},\ldots,2^{m_{k}})=\frac{1}{2^{m_{1}}}\mathcal{C}(1,2^{m_{2}-m_{1}},\ldots,2^{m_{k}-m_{1}}). |  |

These identities yield ℰ ( k) ​ ( ℤ 3) = ⋃ n = 0 ∞ 2 − n ​ ℰ 1 ( k) ​ ( ℤ 3). \mathcal{E}^{(k)}(\mathbb{Z}_{3})=\bigcup_{n=0}^{\infty}2^{-n}\mathcal{E}_{1}^{(k)}(\mathbb{Z}_{3}). Again, since this is a countable union of sets, we obtain the equality

 | dim H ( ℰ ( k) ​ ( ℤ 3)) = sup k ≥ 1 ( dim H ( 2 − n ​ ℰ 1 ( k) ​ ( ℤ 3)) = dim H ( ℰ 1 ( k) ​ ( ℤ 3)) CLOSE \dim_{H}(\mathcal{E}^{(k)}(\mathbb{Z}_{3}))=\sup_{k\geq 1}\Big(\dim_{H}(2^{-n}\mathcal{E}_{1}^{(k)}(\mathbb{Z}_{3})\Big)=\dim_{H}(\mathcal{E}_{1}^{(k)}(\mathbb{Z}_{3})) |  |

asserted above. It also follows that

 | Γ = lim k → ∞ dim H ( ℰ 1 ( k) ​ ( ℤ 3)). \Gamma=\lim_{k\to\infty}\dim_{H}(\mathcal{E}_{1}^{(k)}(\mathbb{Z}_{3})). |  | (1.8) |

We now have

 | ℰ 1 ( k) ​ ( ℤ 3) = ⋃ 0 ≤ m 1 < … < m k − 1 𝒞 ⁡ ( 1, 2 m 1, …, 2 m k − 1). \mathcal{E}_{1}^{(k)}(\mathbb{Z}_{3})=\bigcup_{0\leq m_{1}<\ldots<m_{k-1}}\mathcal{C}(1,2^{m_{1}},\ldots,2^{m_{k-1}}). |  | (1.9) |

The right side of this expression is a countable union of sets, so we have

 | dim H ( ℰ 1 ( k) ​ ( ℤ 3)) = sup 0 ≤ m 1 < … < m k − 1 ( dim H ( 𝒞 ⁡ ( 1, 2 m 1, …, 2 m k − 1))). \dim_{H}(\mathcal{E}_{1}^{(k)}(\mathbb{Z}_{3}))=\sup_{0\leq m_{1}<\ldots<m_{k-1}}\Big(\dim_{H}\big(\mathcal{C}(1,2^{m_{1}},\ldots,2^{m_{k-1}})\big)\Big). |  | (1.10) |

Upper bounds for the right side of this formula are obtained by bounding above the Hausdorff dimensions of all the individual sets 𝒞 ⁡ ( 1, 2 m 1, …, 2 m k − 1) \mathcal{C}(1,2^{m_{1}},\ldots,2^{m_{k-1}}), of the form (1.1). Lower bounds may be obtained by determining the Hausdorff dimension of specific individual sets 𝒞 ⁡ ( 1, 2 m 1, …, 2 m k − 1) \mathcal{C}(1,2^{m_{1}},\ldots,2^{m_{k-1}}). By this means the second author [11, Theorem 1.6 (ii)] obtained the upper bound

 | Γ ≤ dim H ( ℰ ( 2) ​ ( ℤ 3)) = dim H ( ℰ 1 ( 2) ​ ( ℤ 3)) ≤ 1 2, \Gamma\leq\dim_{H}(\mathcal{E}^{(2)}(\mathbb{Z}_{3}))=\dim_{H}(\mathcal{E}_{1}^{(2)}(\mathbb{Z}_{3}))\leq\frac{1}{2}, |  | (1.11) |

and using ( 1.5) we conclude that

 | dim H ( ℰ ⁡ ( ℤ 3)) ≤ 1 2. \dim_{H}(\mathcal{E}({\mathbb{Z}}_{3}))\leq\frac{1}{2}. |  | (1.12) |

### 1.2. Generalized exceptional set problem

We are interested in obtaining improved upper bounds on dim H ( ℰ ⁡ ( ℤ 3)) \dim_{H}(\mathcal{E}(\mathbb{Z}_{3})). To progress further with the approach above, one needs a better understanding of the structure of sets 𝒞 ⁡ ( 1, 2 m 1, …, 2 m k) \mathcal{C}(1,2^{m_{1}},...,2^{m_{k}}), with the hope to obtain uniform bounds on their Hausdorff dimension.

One approach to upper bounding the exceptional set is to relax its defining conditions to allow arbitrary positive integers M M in place of powers of 2 2. Since the 3 3 -adic Cantor set Σ 3, 2 ¯ \Sigma_{3,\bar{2}} is forward invariant under multiplication by 3 3, we will restrict to integers M ≢ 0 ( mod 3) M\not\equiv 0\,(\bmod\,3).

For application to the exceptional set ℰ ⁡ ( ℤ 3) \mathcal{E}(\mathbb{Z}_{3}), the discussion in Section 1.1 indicates that it suffices to consider the restricted family of sets 𝒞 ⁡ ( 1, M 1, …, M n) \mathcal{C}(1,M_{1},\ldots,M_{n}), i.e. taking M 0 = 1 M_{0}=1. We define a relaxed version of the restricted 3 3 -adic exceptional set, as follows.

###### Definition 1.4.

The 3 3 -adic generalized exceptional set is the set

 | ℰ ⋆ ( ℤ 3):= { λ ∈ ℤ 3: there are infinitely many M ≥ 1, M ≢ 0 ( mod 3), including M = 1, \mathcal{E}_{\star}(\mathbb{Z}_{3}):=\{\lambda\in\mathbb{Z}_{3}:\text{there are infinitely many $M\geq 1$, $M\not\equiv 0~(\bmod\,3)$, including \text{$M=1$}, } |  |

 | such that the 3 -adic expansion ( M λ) 3 omits the digit 2 }. \text{such that the $3$-adic expansion}~(M\lambda)_{3}\text{ omits the digit $2$}\}. |  |

When considering intersective sets C ⁡ ( 1, M 1, …, M n) C(1,M_{1},\ldots,M_{n}), we can then further restrict to require all M i ≡ 1 ( mod 3) M_{i}\equiv 1~(\bmod\,3), since any M ≡ 2 ( mod 3) M\equiv 2~(\bmod\,3) has C ⁡ ( 1, M) = { 0 }. C(1,M)=\{0\}. We have ℰ 1 ​ ( ℤ 3) ⊂ ℰ ⋆ ​ ( ℤ 3) ⊂ Σ 3, 2 ¯ \mathcal{E}_{1}(\mathbb{Z}_{3})\subset\mathcal{E}_{\star}(\mathbb{Z}_{3})\subset\Sigma_{3,\bar{2}} and therefore

 | dim H ( ℰ ⁡ ( ℤ 3)) = dim H ( ℰ 1 ​ ( ℤ 3)) ≤ dim H ( ℰ ⋆ ​ ( ℤ 3)). \dim_{H}(\mathcal{E}(\mathbb{Z}_{3}))=\dim_{H}(\mathcal{E}_{1}(\mathbb{Z}_{3}))\leq\dim_{H}(\mathcal{E}_{\star}(\mathbb{Z}_{3})). |  | (1.13) |

Thus upper bounds for the Hausdorff dimension of the generalized exceptional set yield upper bounds for that of the exceptional set.

###### Problem 1.5.

(Generalized Exceptional Set Problem ) Determine upper and lower bounds for the Hausdorff dimension of the generalized exceptional set ℰ ⋆ ​ ( ℤ 3) \mathcal{E}_{\star}(\mathbb{Z}_{3}). In particular, determine whether dim H ( ℰ ⋆ ​ ( ℤ 3)) = 0 \dim_{H}(\mathcal{E}_{\star}(\mathbb{Z}_{3}))=0 or dim H ( ℰ ⋆ ​ ( ℤ 3)) > 0 \dim_{H}(\mathcal{E}_{\star}(\mathbb{Z}_{3}))>0 holds.

We next define a family of sets in parallel to ℰ 1 ( k) ​ ( ℤ 3) \mathcal{E}_{1}^{(k)}({\mathbb{Z}}_{3}) above. We define

 | ℰ ⋆ ( k) ( ℤ 3):= { λ ∈ ℤ 3: there exist 1 = M 1 < M 2 < ⋯ < M k, with all M i ≡ 1 ( mod 3), \mathcal{E}_{\star}^{(k)}(\mathbb{Z}_{3}):=\{\lambda\in\mathbb{Z}_{3}:\text{there exist \, $1=M_{1}<M_{2}<\cdots<M_{k}$, \,with all $M_{i}\equiv\,1(\bmod\,3)$}, |  |

 | such that the 3 -adic expansion ( M i λ) 3 omits the digit 2 }. \quad\quad\text{such that the $3$-adic expansion}~(M_{i}\lambda)_{3}\text{ omits the digit $2$}\}. |  |

Then in parallel to the case above, we have

 | ℰ ⋆ ( k) ​ ( ℤ 3) = ⋃ 1 = M 1 < … < M k − 1 M i ≡ 1 ( mod 3) 𝒞 ⁡ ( 1, M 1, …, M k − 1). \mathcal{E}_{\star}^{(k)}(\mathbb{Z}_{3})=\bigcup_{{1=M_{1}<\ldots<M_{k-1}}\atop{M_{i}\equiv 1(\bmod~3)}}\mathcal{C}(1,M_{1},\ldots,M_{k-1}). |  |

In consequence we have the inclusion

 | ℰ ⋆ ​ ( ℤ 3) ⊆ ⋂ k = 1 ∞ ℰ ⋆ ( k) ​ ( ℤ 3). \mathcal{E}_{\star}(\mathbb{Z}_{3})\subseteq\bigcap_{k=1}^{\infty}\mathcal{E}_{\star}^{(k)}(\mathbb{Z}_{3}). |  |

This inclusion yields the bound

 | dim H ( ℰ ⋆ ​ ( ℤ 3)) ≤ Γ ∗, \dim_{H}(\mathcal{E}_{\star}(\mathbb{Z}_{3}))\leq\Gamma_{*}, |  | (1.14) |

where we define

 | Γ ⋆:= lim k → ∞ dim H ( ℰ ⋆ ( k) ​ ( ℤ 3)). \Gamma_{\star}:=\lim_{k\to\infty}\dim_{H}(\mathcal{E}_{\star}^{(k)}(\mathbb{Z}_{3})). |  | (1.15) |

As far as we know it is possible that dim H ( ℰ ⋆ ​ ( ℤ 3)) < Γ ∗ \dim_{H}(\mathcal{E}_{\star}(\mathbb{Z}_{3}))<\Gamma_{*} may occur.

The second author [11, Theorem 1.6] obtained the upper bound

 | Γ ∗ ≤ dim H ( ℰ ⋆ ( 2) ​ ( ℤ 3)) ≤ 1 2, \Gamma_{\ast}\leq\dim_{H}(\mathcal{E}_{\star}^{(2)}(\mathbb{Z}_{3}))\leq\frac{1}{2}, |  | (1.16) |

which in fact yielded ( 1.11).

Our interest in the generalized exceptional set problem stemmed from the fact that if it were true that dim H ( ℰ ⋆ ​ ( ℤ 3)) = 0 \dim_{H}(\mathcal{E}_{\star}(\mathbb{Z}_{3}))=0, then the Exceptional Set Conjecture 1.2 would follow. However a main result of our investigation establishes that this does not hold: we obtain the lower bounds

 | Γ ⋆ ≥ dim H ( ℰ ⋆ ​ ( ℤ 3)) ≥ 1 2 ​ log 3 ​ 2 ≈ 0.315464, \Gamma_{\star}\geq\dim_{H}(\mathcal{E}_{\star}(\mathbb{Z}_{3}))\geq\frac{1}{2}\log_{3}2\approx 0.315464, |  |

see Theorem 1.9 below. This inconvenient fact limits the upper bounds attainable on dim H ( ℰ ⁡ ( ℤ 3)) \dim_{H}(\mathcal{E}(\mathbb{Z}_{3})) via the relaxed problem.

### 1.3. Algorithmic Results

We study the size of intersections of multiplicative translates of the 3 3 -adic Cantor set Σ 3:= Σ 3, 2 ¯ \Sigma_{3}:=\Sigma_{3,\bar{2}}, as measured by Hausdorff dimension. We study the sets

 | 𝒞 ⁡ ( 1, M 1, …, M n):= Σ 3, 2 ¯ ∩ 1 M 1 ​ Σ 3, 2 ¯ ∩ ⋯ ∩ 1 M n ​ Σ 3, 2 ¯. \mathcal{C}(1,M_{1},\ldots,M_{n}):=\Sigma_{3,\bar{2}}\cap\frac{1}{M_{1}}\Sigma_{3,\bar{2}}\cap\cdots\cap\frac{1}{M_{n}}\Sigma_{3,\bar{2}}. |  |

where 1 < M 1 < ⋯ < M n 1<M_{1}<\cdots<M_{n} are positive integers. As remarked above, via results in [1], [2] these sets have a nice description, with their members having p p -adic expansions describable by finite automata, which permits effective computation of their Hausdorff dimension. These results are reviewed in Section 2, and the necessary definitions for presentations of a path set used in the following theorem appear there.

###### Theorem 1.6.

(Dimension of C ⁡ ( 1, M 1, …, M n) C(1,M_{1},...,M_{n}))

(1) There is a terminating algorithm that takes as input any finite set of integers
1 ≤ M 1 < … < M n 1\leq M_{1}<\ldots<M_{n}, and gives as output a labeled directed graph 𝒢 = ( G, ℒ) \mathcal{G}=(G,\mathcal{L}) with a marked starting vertex v 0 v_{0}, which is a presentation of a path set X = X ⁡ ( 1, M 1, M 2, ⋯, M n) X=X(1,M_{1},M_{2},\cdots,M_{n}) describing the 3 3 -adic expansions of the elements of the space

 | 𝒞 ⁡ ( 1, M 1, …, M n):= Σ 3 ∩ 1 M 1 ​ Σ 3 ∩ … ∩ 1 M n ​ Σ 3. \mathcal{C}(1,M_{1},...,M_{n}):=\Sigma_{3}\cap\frac{1}{M_{1}}\Sigma_{3}\cap\ldots\cap\frac{1}{M_{n}}\Sigma_{3}. |  |

This presentation is right-resolving and all vertices are reachable from the marked vertex. The graph G G has at most ∏ i = 1 n ( 1 + ⌊ 1 2 ​ M i ⌋) \prod_{i=1}^{n}(1+\lfloor\frac{1}{2}M_{i}\rfloor) vertices.

(2) The topological entropy β \beta of the path set X X is the Perron eigenvalue of the adjacency matrix A A of the directed graph G G. It is a real algebraic integer satisfying 1 ≤ β ≤ 2 1\leq\beta\leq 2. Furthermore the Hausdorff dimension

 | dim H ( 𝒞 ⁡ ( 1, M 1, …, M n)) = log 3 ⁡ β. \dim_{H}(\mathcal{C}(1,M_{1},...,M_{n}))=\log_{3}\beta. |  |

This dimension falls in the interval [0, log 3 ⁡ 2] [0,\log_{3}2].

This construction is quite explicit in the special case 𝒞 ⁡ ( 1, M) \mathcal{C}(1,M). In that case already the associated graphs G G can be very complicated, and there exist examples where the graph has an arbitrarily large number of strongly connected components, cf. [3].

We have computed Hausdorff dimensions of many examples of such intersections. In the process we have found some infinite families of integers where the graph structures are analyzable, see Section 4 and [3]. From the viewpoint of fractal constructions, the sets constructed give specific interesting examples of graph-directed fractals, which appear to have structure depending on the integers ( M 1,.., M n) (M_{1},..,M_{n}) in an intricate way.

### 1.4. Hausdorff dimension results: Two infinite families

There are some simple properties of the 3 3 -adic expansion of M M (which coincides with the ternary expansion of M M, read backwards) which restrict the Hausdorff dimension of sets 𝒞 ⁡ ( 1, M). \mathcal{C}(1,M). We begin with some simple restrictions on the Hausdorff dimension which can be read off from the 3 3 -adic expansion of M M; this coincides with the ternary expansion of M M, written ( M) 3 (M)_{3}, written backwards, where we write the ternary expansion

 | ( M) 3:= ( a k a k − 1 ⋯ a 1 a 0) 3, f o r M = ∑ j = 0 k a j 3 j. (M)_{3}:=(a_{k}a_{k-1}\cdots a_{1}a_{0})_{3},\quad\quad{for}\quad M=\sum_{j=0}^{k}a_{j}3^{j}. |  |

If the first nonzero 3 3 -adic digit a 0 = 2 a_{0}=2, then 𝒞 ⁡ ( 1, M) = { 0 } \mathcal{C}(1,M)=\{0\}, whence its Hausdorff dimension dim H ( 𝒞 ⁡ ( 1, M)) = 0 \dim_{H}(\mathcal{C}(1,M))=0. On the other hand, if the positive integers M 1, …, M k M_{1},...,M_{k} all all digits a j = 0 a_{j}=0 or a j = 1 a_{j}=1 in their 3 3 -adic expansions, then the Hausdorff dimension dim H ( 𝒞 ⁡ ( 1, M 1, M 2, …, M k)) \dim_{H}(\mathcal{C}(1,M_{1},M_{2},...,M_{k})) must be positive.

We have found several infinite families of integers having ternary expansions of a simple form, whose path set presentations have a regular structure in the family parameter k k, that permits their Hausdorff dimension to be determined. The simplest family takes M 1 = 3 k = ( 10 k) 3 M_{1}=3^{k}=(10^{k})_{3}. In this trivial case 𝒞 ⁡ ( 1, 3 k) = Σ 3, 2 ¯ \mathcal{C}(1,3^{k})=\Sigma_{3,\bar{2}}, whence

 | dim H ( 𝒞 ⁡ ( 1, M k)) = log 3 ⁡ 2 ≈ 0.630929. \dim_{H}(\mathcal{C}(1,M_{k}))=\log_{3}2\approx 0.630929. |  | (1.17) |

In Section 4 we analyze two other infinite families in detail, as follows. The first of these families is L k = 1 2 ​ ( 3 k − 1) = ( 1 k) 3 L_{k}=\frac{1}{2}(3^{k}-1)=(1^{k})_{3}, for k ≥ 1 k\geq 1.

###### Theorem 1.7.

(Infinite Family L k = 1 2 ​ ( 3 k − 1) L_{k}=\frac{1}{2}(3^{k}-1))

(1) Let L k = 1 2 ​ ( 3 k − 1) = ( 1 k) 3 L_{k}=\frac{1}{2}(3^{k}-1)=(1^{k})_{3}. The path set presentation ( 𝒢, v 0) ({\mathcal{G}},v_{0}) for the path set X ⁡ ( 1, L k) X(1,L_{k}) underlying 𝑂𝑃𝐸𝑁 𝒞 ⁡ ( 1, L k)) \mathcal{C}(1,L_{k})) has exactly k k vertices and is strongly connected.

(2) For every k ≥ 1 k\geq 1,

 | dim H ( 𝒞 ⁡ ( 1, L k) = dim H 𝒞 ⁡ ( 1, ( 1 k) 3) = log 3 ⁡ β k CLOSE, \dim_{H}(\mathcal{C}(1,L_{k})=\dim_{H}\mathcal{C}(1,(1^{k})_{3})=\log_{3}\beta_{k}, |  |

where β k \beta_{k} is the unique real root greater than 1 1 of λ k − λ k − 1 − 1 = 0 \lambda^{k}-\lambda^{k-1}-1=0.

(3) For all k ≥ 3 k\geq 3 there holds

 | dim H ( 𝒞 ⁡ ( 1, L k)) = log 3 ⁡ k k + O ⁡ ( log ⁡ log ⁡ ( k) k). \dim_{H}\Big(\mathcal{C}(1,L_{k})\Big)=\frac{\log_{3}k}{k}+O\left(\frac{\log\log(k)}{k}\right). |  |

The Hausdorff dimension of the set dim H ( 𝒞 ⁡ ( 1, L k)) \dim_{H}(\mathcal{C}(1,L_{k})) is positive but approaches 0 0 as k → ∞ k\to\infty. This result is proved in Section 4.2.

Secondly, we consider the family N k = 3 k + 1 = ( 10 k − 1 ​ 1) 3 N_{k}=3^{k}+1=(10^{k-1}1)_{3}. Our main results concern this family.

###### Theorem 1.8.

(Infinite Family N k = 3 k + 1 N_{k}=3^{k}+1)

(1) Let N k = 3 k + 1 = ( 10 k − 1 ​ 1) 3 N_{k}=3^{k}+1=(10^{k-1}1)_{3}. The path set presentation ( 𝒢, v 0) ({\mathcal{G}},v_{0}) for the path set X ⁡ ( 1, N k) X(1,N_{k}) underlying 𝒞 ⁡ ( 1, N k) \mathcal{C}(1,N_{k}) has exactly 2 k 2^{k} vertices and is strongly connected.

(2) For every integer k ≥ 1 k\geq 1, there holds

 | dim H ( 𝒞 ⁡ ( 1, N k)) = dim H 𝒞 ⁡ ( 1, ( 10 k − 1 ​ 1) 3) = log 3 ⁡ ( 1 + 5 2) ≈ 0.438018. \dim_{H}(\mathcal{C}(1,N_{k}))=\dim_{H}\mathcal{C}(1,(10^{k-1}1)_{3})=\log_{3}\bigg(\frac{1+\sqrt{5}}{2}\bigg)\approx 0.438018. |  |

Here the Hausdorff dimension is constant as k → ∞ k\to\infty. Theorem 1.8 is a direct consequence of results established in Section 4.3 (Theorem 4.4 and Proposition 4.5).

We also include results on multiple intersections of sets in the two infinite families above in Section 4.4. It is easy to see that for each infinite family above, the Hausdorff dimensions of arbitrarily large intersections are always positive. We give some lower bounds on the dimension; Theorem 4.8 gives multiple intersections that establish Γ ⋆ ≥ 1 2 ​ log 3 ​ 2. \Gamma_{\star}\geq\frac{1}{2}\log_{3}2.

In a sequel [3] we analyze a third infinite family P k = ( 20 k − 1 ​ 1) 3 = 2 ⋅ 3 k + 1 P_{k}=(20^{k-1}1)_{3}=2\cdot 3^{k}+1, whose underlying path set graphs exhibit much more complicated behavior; they have an unbounded number of strongly connected components as k → ∞ k\to\infty.

### 1.5. Hausdorff dimension results: exceptional sets

In addition we are able to combine graphs in the infinite family 𝒞 ⁡ ( 1, N k) \mathcal{C}(1,N_{k}) in such a way to get 𝒞 ⁡ ( 1, M 1, M 2, …, M n) \mathcal{C}(1,M_{1},M_{2},...,M_{n}) with distinct M k ≡ 1 ( mod 3) M_{k}\equiv 1~(\bmod\,3) which have Hausdorff dimension further bounded away from zero.

In Section 5.1 we establish the following lower bound on the Hausdorff dimension of the generalized exceptional set. We are indebted to A. Bolshakov for observing this result, which improves on Theorem 4.8.

###### Theorem 1.9.

The generalized exceptional set ℰ ⋆ \mathcal{E}_{\star} satisfies

 | dim H ( ℰ ⋆) ≥ 1 2 ​ log 3 ​ 2 ≈ 0.315464. \dim_{H}(\mathcal{E}_{\star})\geq\frac{1}{2}\log_{3}2\approx 0.315464. |  |

In fact,

 | dim H ( { λ ∈ Σ 3, 2 ¯: N 2 ​ k + 1 ​ λ ∈ Σ 3, 2 ¯ ​ for all ​ k ≥ 1 }) ≥ 1 2 ​ log 3 ​ 2. \dim_{H}(\{\lambda\in\Sigma_{3,\bar{2}}:\,N_{2k+1}\lambda\in\Sigma_{3,\bar{2}}\,\,\mbox{for all}\,k\geq 1\})\geq\frac{1}{2}\log_{3}2. |  |

This result is an immediate corollary of Theorem 5.1. The proof strongly uses the fact that the integers N 2 ​ k + 1 N_{2k+1} have only two nonzero 3 3 -adic digits.

In Section 5.2 we give numerical improvements on the lower bounds in [11] for small k k for the Hausdorff dimension of the enclosing sets ℰ ( k) ​ ( ℤ 3) \mathcal{E}^{(k)}(\mathbb{Z}_{3}) that upper bound that of the exceptional set ℰ ⁡ ( ℤ 3) \mathcal{E}(\mathbb{Z}_{3}). These improvements come via explicit examples.

### 1.6. Extensions of Results

The results of this paper show that the Generalized Exceptional Set ℰ ∗ ​ ( ℤ 3) \mathcal{E}_{*}({\mathbb{Z}}_{3}) has positive Hausdorff dimension. Theorem 1.9 shows that to make further progress on the Exceptional Set Conjecture one cannot relax the problem to consider general integers M M; it will be necessary to consider a smaller class on integers that have some special properties in common with the integers 2 k 2^{k}.

In a sequel [3] we investigate another approach towards the Exceptional Set Conjecture. Let n 3 ​ ( M) n_{3}(M) denote the number of nonzero 3 3 digits of M M. It asks whether the dim H 𝒞 ⁡ ( 1, M) \dim_{H}\mathcal{C}(1,M) necessarily decreases to 0 0 as n 3 ​ ( M) → ∞ n_{3}(M)\to\infty. It is a known fact that the number of nonzero ternary digits in ( 2 n) 3 (2^{n})_{3} goes to infinity as n → ∞ n\to\infty, i.e. for each k ≥ 2 k\geq 2 there are only finitely many n n with ( 2 n) 3 (2^{n})_{3} having at most k k nonzero ternary digits. This result was first established in 1971 by Senge and Straus, see [18], and a quantitative version of this assertion follows from results of C. L. Stewart [20, Theorem 1]. It follows that if it were true that dim H 𝒞 ⁡ ( 1, M) → 0 \dim_{H}\mathcal{C}(1,M)\to 0 as n 3 ​ ( M) → ∞ n_{3}(M)\to\infty, then the Exceptional Set Conjecture would follow.

This paper and its sequel [3] study the Hausdorff dimension of these sets in the special case of multiplicative translates of 3 3 -adic Cantor sets, but one may also consider many more complicated path set fractals in the sense of [2] in place of the Cantor set. The algorithmic methods of this paper apply to p p -adic numbers for any prime p p and to the g g -adic numbers considered by Mahler [14] for any integer g ≥ 2 g\geq 2.

### 1.7. Overview

Section 2 reviews properties of p p -adic path sets and their symbolic dynamics, drawing on [1] and [2]. The general framework of these papers includes intersections of multiplicative translates of 3 3 -adic Cantor sets as a special case. Section 2 also states a formula for computing the Hausdorff dimension of such sets. Section 3 of this paper gives algorithmic constructions and proves Theorem 1.6. It also presents examples. Section 4 studies two infinite families of intersections of 3 3 -adic Cantor sets and proves Theorems 1.7 and 1.8. Section 5 gives applications, which include the lower bound on the Hausdorff dimension of the generalized exceptional set ℰ ⋆ ​ ( ℤ 3) \mathcal{E}_{\star}(\mathbb{Z}_{3}) and lower bounds on dim H ( ℰ ( k) ​ ( ℤ 3)) \dim_{H}(\mathcal{E}^{(k)}(\mathbb{Z}_{3})) for small k k.

### 1.8. Notation

The notation ( m) 3 (m)_{3} means either the base 3 3 expansion of the positive integer m m, or else the 3 3 -adic expansion of ( m) 3 (m)_{3}. In the 3 3 -adic case this expansion is to be read right to left, so that it is compatible with the ternary expansion. That is, α = ∑ j = 0 ∞ a j ​ 3 j \alpha=\sum_{j=0}^{\infty}a_{j}3^{j} would be written ( ⋯ a 2 a 1 a 0) 3 (\cdots a_{2}a_{1}a_{0})_{3}.

## 2. Symbolic Dynamics and Graph-Directed Constructions

### 2.1. Symbolic Dynamics, Graphs and Finite Automata

The constructions of this paper are based on the fact that the points in intersections of multiplicative translates of 3 3 -adic Cantor sets have 3 3 -adic expansions that are describable in terms of allowable paths generated by finite directed labeled graphs . We use symbolic dynamics on certain closed subsets of the one-sided shift space Σ = 𝒜 ℕ \Sigma={\mathcal{A}}^{{\mathbb{N}}} with fixed symbol alphabet 𝒜 {\mathcal{A}}, which for our application will be specialized to 𝒜 = { 0, 1, 2 } {\mathcal{A}}=\{0,1,2\}. A basic reference for directed graphs and symbolic dynamics, which we follow, is Lind and Marcus [13].

By a graph we mean a finite directed graph, allowing loops and multiple edges. A labeled graph is a graph assigning labels to each directed edge; these labels are drawn from a finite symbol alphabet. A labeled directed graph can be interpreted as a finite automaton in the sense of automata theory. In our applications to 3 3 -adic digit sets, the labels are drawn from the alphabet 𝒜 = { 0, 1, 2 }. {\mathcal{A}}=\{0,1,2\}. In a directed graph, a vertex is a source if all directed edges touching that vertex are outgoing; it is a sink if all directed edges touching that edge are incoming. A vertex is essential if it is neither a source nor a sink, and is called stranded otherwise. A graph is *essential*if all of its vertices are essential. A graph G G is strongly connected if for each two vertices i, j i,j there is a directed path from i i to j j. We let S ​ C ​ ( G) SC(G) denote the set of strongly connected component subgraphs of G G.

We use some basic facts from Perron-Frobenius theory of nonnegative matrices. The Perron eigenvalue ( [13, Definition 4.4.2]) of a nonnegative real matrix 𝐀 ≠ 0 \mathbf{A}\neq 0 is the largest real eigenvalue β ≥ 0 \beta\geq 0 of 𝐀 \mathbf{A}. A nonnegative matrix is irreducible if for each row and column ( i, j) (i,j) some power 𝐀 m {\bf A}^{m} has ( i, j) (i,j) -th entry nonzero. A nonnegative matrix 𝐀 {\bf A} is primitive if some power 𝐀 k {\bf A}^{k} for an integer k ≥ 1 k\geq 1 has all entries positive; primitivity implies irreducibility but not vice versa. The Perron-Frobenius theorem, [13, Theorem 4.2.3] for an irreducible nonnegative matrix 𝐀 {\bf A} states that:

1. (1)

The Perron eigenvalue β \beta is geometrically and algebraically simple, and has an everywhere positive eigenvector 𝐯. {\bf v}.

2. (2)

All other eigenvalues μ \mu have | μ | ≤ β |\mu|\leq\beta, so that β = σ ⁡ ( 𝐀) \beta=\sigma({\bf A}), the spectral radius of 𝐀 {\bf A}.

3. (3)

Any other everywhere positive eigenvector must be a positive mulitiple of 𝐯 {\bf v}.

For a general nonnegative real matrix 𝐀 ≠ 0 \mathbf{A}\neq 0, the Perron eigenvalue need not be simple, but it still equals the spectral radius σ ⁡ ( 𝐀) \sigma(\bf{A}) and it has at least one everywhere nonnegative eigenvector.

We apply this theory to adjacency matrices of graphs. A (vertex-vertex) adjacency matrix 𝐀 = 𝐀 G {\bf A}={\bf A}_{G} of the directed graph G G has entry a i ​ j a_{ij} counting the number of directed edges from vertex i i to vertex j j. The adjacency matrix is irreducible if and only if the associated graph is strongly connected, and we also call the graph irreducible in this case. Here primitivity of the adjacency matrix of a directed graph G G is equivalent to the graph being strongly connected and aperiodic, i.e. the greatest common divisor of its (directed) cycle lengths is 1 1. For an adjacency matrix of a graph containing at least at least one directed cycle, its Perron eigenvalue is necessarily a real algebraic integer β ≥ 1 \beta\geq 1 (see Lind [12] for a characterization of these numbers).

### 2.2. p p -Adic path sets, sofic shifts and p p -adic path set fractals

Our basic objects are special cases of the following definition. A pointed graph is a pair ( 𝒢, v) ({\mathcal{G}},v) consisting of a directed labeled graph 𝒢 = ( G, ℰ) {\mathcal{G}}=(G,\mathcal{E}) and a marked vertex v v of 𝒢 {\mathcal{G}}. Here G G is a (directed) graph and ℰ \mathcal{E} is an assignment of labels ( e, ℓ) = ( v 1, v 2, ℓ) (e,\ell)=(v_{1},v_{2},\ell) to the edges of G G, where every edge gets a unique label, and no two triples are the same (but multiple edges and loops are permitted otherwise).

###### Definition 2.1.

Given a pointed graph ( 𝒢, v) ({\mathcal{G}},v) its associated *path set*𝒫 = X 𝒢 ​ ( v) ⊂ 𝒜 ℕ {\mathcal{P}}=X_{\mathcal{G}}(v)\subset{\mathcal{A}}^{{\mathbb{N}}} is the set of all infinite one-sided symbol sequences ( x 0, x 1, x 2, …) ∈ 𝒜 ℕ (x_{0},x_{1},x_{2},...)\in{\mathcal{A}}^{{\mathbb{N}}}, giving the successive labels of all one-sided infinite walks in 𝒢 \mathcal{G} issuing from the distinguished vertex v v. Many different ( 𝒢, v) (\mathcal{G},v) may give the same path set 𝒫 {\mathcal{P}}, and we call any such ( 𝒢, v) (\mathcal{G},v) a *presentation*of 𝒫 {\mathcal{P}}.

An important class of presentations have the following extra property. We say that a directed labeled graph 𝒢 = ( G, v) {\mathcal{G}}=(G,v) is right-resolving if for each vertex of 𝒢 {\mathcal{G}} all directed edges outward have distinct labels. (In automata theory 𝒢 {\mathcal{G}} is called a deterministic automaton.) One can show that every path set has a right-resolving presentation.

Note that the labeled graph 𝒢 {\mathcal{G}} without a marked vertex determines a one-sided sofic shift in the sense of symbolic dynamics, as defined in [1]. This sofic shift comprises the set union of the path sets at all vertices of 𝒢 {\mathcal{G}}. Path sets are closed sets in the shift topology, but are in general non-invariant under the one-sided shift operator. Those path sets 𝒫 {\mathcal{P}} that are invariant are exactly the one-sided sofic shifts [1, Theorem 1.4].

We study the path set concept in symbolic dynamics in [1]. The collection of path sets X:= X ( 𝒢, v 0) X:=X_{({\mathcal{G}},v_{0})} in a given alphabet is closed under finite union and intersection ( [1]). The symbolic dynamics analogue of Hausdorff dimension is topological entropy. The topological entropy of a path set H t ​ o ​ p ​ ( X) H_{top}(X) is given by

 | H t ​ o ​ p ​ ( X):= lim sup n → ∞ 1 n ​ log ⁡ N n ​ ( X), H_{top}(X):=\limsup_{n\to\infty}\frac{1}{n}\log N_{n}(X), |  |

where N n ​ ( X) N_{n}(X) counts the number of distinct blocks of symbols of lengh n n appearing in elements of X X. The topological entropy is easy to compute for right-resolving presentation. By [1, Theorem 1.13], it is

 | H t ​ o ​ p ​ ( X) = log ⁡ β H_{top}(X)=\log\beta |  | (2.1) |

where β \beta is the Perron eigenvalue of the adjacency matrix 𝐀 = 𝐀 G {\bf A}={\bf A}_{G} of the underlying directed graph G G of 𝒢 {\mathcal{G}}, e.g. the spectral radius of 𝐀 {\bf A}.

### 2.3. p p -Adic Symbolic Dynamics and Graph Directed Constructions

We now suppose 𝒜 = { 0, 1, 2, …, p − 1 } {\mathcal{A}}=\{0,1,2,...,p-1\}. We can view the elements of a path set X X on this alphabet geometrically as describing the digits in the p p -adic expansion of a p p -adic integer. This is done using a map ϕ: 𝒜 ℕ → ℤ p \phi:{\mathcal{A}}^{{\mathbb{N}}}\to{\mathbb{Z}}_{p}. from symbol sequences into ℤ p {\mathbb{Z}}_{p}. We call the resulting image set K = ϕ ⁡ ( X) K=\phi(X) a *p p -adic path set fractal*. Such sets are studied in [2], where they are related to graph-directed fractal constructions. The class of p p -adic path set fractals is closed under p p -adic addition and multiplication by rational numbers r ∈ ℚ r\in{\mathbb{Q}} that lie in ℤ p {\mathbb{Z}}_{p} ( [2]).

It is possible to compute the Hausdorff dimension of a p p -adic path set fractal directly from a suitable presentation of the underlying path set X = X 𝒢 ​ ( v) X=X_{{\mathcal{G}}}(v). We will use the following result.

###### Proposition 2.2.

Let p p be a prime, and K K a set of p p -adic integers whose allowable p p -adic expansions are described by the symbolic dynamics of a p p -adic path set X K X_{K} on symbols 𝒜 = { 0, 1, 2, ⋯, p − 1 } \mathcal{A}=\{0,1,2,\cdots,p-1\}. Let ( 𝒢, v 0) (\mathcal{G},v_{0}) be a presentation of this path set that is right-resolving.

(1) The map ϕ p: ℤ p → [0, 1] \phi_{p}:\mathbb{Z}_{p}\rightarrow[0,1] taking α = ∑ k = 0 ∞ a k ​ p k ∈ ℤ p \alpha=\sum_{k=0}^{\infty}{a_{k}p^{k}}\in\mathbb{Z}_{p} to the real number with base p p expansion ϕ p ​ ( α):= ∑ k = 0 ∞ a k p k + 1 \phi_{p}(\alpha):=\sum_{k=0}^{\infty}\frac{a_{k}}{p^{k+1}} is a continuous map, and the image of K K under this map, K ′:= ϕ p ​ ( K) ⊂ [0, 1] K^{\prime}:=\phi_{p}(K)\subset[0,1], is a graph-directed fractal in the sense of Mauldin-Williams.

(2) The Hausdorff dimension of the p p -adic path set fractal K K is

 | dim H ( K) = dim H ( K ′) = log p ⁡ β, \dim_{H}(K)=\dim_{H}(K^{\prime})=\log_{p}\beta, |  | (2.2) |

where β \beta is the spectral radius of the adjacency matrix 𝐀 {\bf A} of G G.

###### Proof.

These results are proved in [2, Section 2]. ∎

In this paper we treat the case p = 3 p=3 with 𝒜 = { 0, 1, 2 } {\mathcal{A}}=\{0,1,2\}. The 3 3 -adic Cantor set is a 3 3 -adic path set fractal, so these general properties above guarantee that the intersection of a finite number of multiplicative translates of 3 3 -adic Cantor sets will itself be a 3 3 -adic path set fractal K K, generated from an underlying path set.

To do calculations with such sets we will need algorithms for converting presentations of a given p p -adic path set to presentations of new p p -adic path sets derived by the operations above. The p p -adic arithmetic operations are treated in [2] and union and intersection are treated in [1].

## 3. Structure of Intersection Sets 𝒞 ⁡ ( 1, M 1, M 2, …, M n CLOSE \mathcal{C}(1,M_{1},M_{2},...,M_{n})

We show that the sets C ⁡ ( 1, M 1, …, M n) C(1,M_{1},\ldots,M_{n}) consist of those 3 3 -adic integers whose 3 3 -adic expansions are describable as path sets X ⁡ ( 1, M 1, ⋯, M n) X(1,M_{1},\cdots,M_{n}). We also present an algorithm which when given the data ( M 1, …, M n) (M_{1},...,M_{n}) as input produces as output a presentation 𝒢 = ( G, v 0) {\mathcal{G}}=(G,v_{0}) of the path set X ⁡ ( 1, M 1, …, M n) X(1,M_{1},\ldots,M_{n}).

### 3.1. Constructing a path set presentation X ⁡ ( 1, M) X(1,M)

We describe an algorithmic procedure to obtain a path set presentation X ⁡ ( 1, M) X(1,M) for the 3 3 -adic expansions of elements in 𝒞 ⁡ ( 1, M) \mathcal{C}(1,M). Since 𝒞 ⁡ ( 1, 3 j ​ M) = 𝒞 ⁡ ( 1, M) \mathcal{C}(1,3^{j}M)=\mathcal{C}(1,M), we may reduce to the case M ≢ 0 ( mod 3) M\not\equiv 0~(\bmod~3) and since 𝒞 ⁡ ( 1, M) = { 0 } \mathcal{C}(1,M)=\{0\} if M ≡ 2 ( mod 3) M\equiv 2~(\bmod\,3) it suffices to consider the case M ≡ 1 ( mod 3) M\equiv 1\,(\bmod\,3).

###### Theorem 3.1.

For M ≥ 1 M\geq 1, with M ≡ 1 ( mod 3) M\equiv 1~(\bmod\,3), the set 𝒞 ⁡ ( 1, M) = Σ 3 ∩ 1 M ​ Σ 3 \mathcal{C}(1,M)=\Sigma_{3}\cap\frac{1}{M}\Sigma_{3} has 3 3 -adic expansions given by a path set X ⁡ ( 1, M) X(1,M) which has an algorithmically computable path set presentation ( 𝒢, v 0) (\mathcal{G},v_{0}), in which the vertices v m v_{m} are labeled with a subset of the integers 0 ≤ m ≤ ⌊ 1 2 ​ M ⌋ 0\leq m\leq\lfloor\frac{1}{2}M\rfloor, always including m = 0 m=0, and of cardinality at most ⌊ M 2 ⌋ \lfloor\frac{M}{2}\rfloor. This presentation is right-resolving, connected and essential.

###### Proof.

The labeled graph 𝒢 = ( G, ℒ) \mathcal{G}=(G,\mathcal{L}) will have path labels drawn from { 0, 1 } \{0,1\} and the vertices v j v_{j} of the underlying directed graph G G will be labeled by a subset of the integers j j satisfying 0 ≤ N ≤ M + 1. 0\leq N\leq M+1. The marked vertex v 0 v_{0} corresponds to N = 0 N=0 and is the starting vertex of the algorithm.

The idea is simple. Suppose that

 | α:= ∑ j = 0 ∞ a j ​ 3 j ∈ Σ 3 ∩ 1 M ​ Σ 3. \alpha:=\sum_{j=0}^{\infty}a_{j}3^{j}\in\Sigma_{3}\cap\frac{1}{M}\Sigma_{3}. |  |

Here all a j ∈ { 0, 1 } a_{j}\in\{0,1\} and in addition

 | M ​ α = ∑ j = 0 ∞ b j ​ 3 j ∈ Σ 3. M\alpha=\sum_{j=0}^{\infty}b_{j}3^{j}\in\Sigma_{3}. |  |

Suppose the first n n digits

 | α n = ∑ j = 0 n − 1 a j ​ 3 j, \alpha_{n}=\sum_{j=0}^{n-1}a_{j}3^{j}, |  |

are chosen. Since M ≡ 1 ( mod 3) M\equiv 1~(\bmod\,3) this uniquely specifies the first n n digits of

 | M ​ α n:= ∑ j = 0 m + n − 1 b j ( n) ​ 3 j, M\alpha_{n}:=\sum_{j=0}^{m+n-1}b_{j}^{(n)}3^{j}, |  |

namely

 | b j ( n) = b j ​ for 0 ≤ j ≤ n − 1, b_{j}^{(n)}=b_{j}\,\,\mbox{for}\quad 0\leq j\leq n-1, |  |

which have b j ∈ { 0, 1 }, b_{j}\in\{0,1\}, for 0 ≤ j ≤ n − 1. 0\leq j\leq n-1. Here the remaining digits b n + k ( n) b_{n+k}^{(n)} for 1 ≤ k ≤ m 1\leq k\leq m are unrestricted, with

 | m = ⌊ log 3 ⁡ M ⌋ + 1. m=\lfloor\log_{3}M\rfloor+1. |  |

We have followed a path in the graph G corresponding to edges labeled ( a 0, a 1, …, a n − 1) (a_{0},a_{1},...,a_{n-1}). The vertex we arrive at after these steps will be labeled by the value of the “carry-digit” part of β n \beta_{n}, which is

 | N = ∑ j = n m + n − 1 b j ( n) ​ 3 j − n. N=\sum_{j=n}^{m+n-1}b_{j}^{(n)}3^{j-n}. |  |

The value of the bottom 3 3 -adic digit b n ( n) b_{n}^{(n)} of N N will determine the allowable exit edges from vertex v N v_{N}, and the label of the vertices reached. The requirement is that the next digit a n a_{n} satisfy

 | a n + b n ( n) ≡ 0, 1 ( mod 3) a_{n}+b_{n}^{(n)}\equiv 0,1(\bmod\,3) |  | (3.1) |

If such a value is chosen, then we will be able to create a valid α n + 1 \alpha_{n+1} and β n + 1:= M ​ α n + 1 \beta_{n+1}:=M\alpha_{n+1} will have

 | b n ( n + 1) = a n + b n ( n) ( mod 3). b_{n}^{(n+1)}=a_{n}+b_{n}^{(n)}~(\bmod\,3). |  |

There always exists at least one exit edge from each reachable vertex v N v_{N}, since for b n ( n) = 0 b_{n}^{(n)}=0 the admissible a n = 0, 1 a_{n}=0,1; for b n ( n) = 1 b_{n}^{(n)}=1 the only admissible a n = 0 a_{n}=0, and for b n ( n) = 2 b_{n}^{(n)}=2 the only admissible a n = 1 a_{n}=1, in order that the next digits a n + 1, b n + 1 a_{n+1},b_{n+1} both belong to { 0, 1 } \{0,1\}.

The important point is that the vertex label N N is all that must be remembered to decide on an admissible exit edge in the next step, since its bottom digit determines the allowable exit edge values a ⊂ { 0, 1 } a\subset\{0,1\} by requiring

 | a + N ≡ 0, 1 ( mod 3), a+N\equiv 0,1\,~(\bmod\,3), |  | (3.2) |

and for an exit edge labeled a a one can determine the new vertex label v N ′ v_{N^{\prime}} as

 | N ′:= ⌊ N + M ​ a 3 ⌋. N^{\prime}:=\lfloor\frac{N+Ma}{3}\rfloor. |  | (3.3) |

To the graph G G one adds a directed edge for each allowable value a n = 0 a_{n}=0 or 1 1 from N N to N ′ N^{\prime} labeled by a n a_{n}.

Now one sees that the are only finitely many vertices v N v_{N} that can be reached from the vertex v 0 v_{0}. One proves by induction on the number of steps n n taken that any reachable vertex v N v_{N} has vertex label.

 | 0 ≤ N ≤ ⌊ M 2 ⌋. 0\leq N\leq\lfloor\frac{M}{2}\rfloor. |  |

This holds for the initial vertex, while for the induction step, we obtain from ( 3.3) that

 | N ′ ≤ N + M ​ a 3 ≤ M / 2 + M 3 ≤ M 2. N^{\prime}\leq\frac{N+Ma}{3}\leq\frac{M/2+M}{3}\leq\frac{M}{2}. |  |

Thus the process of constructing the graph will halt.

It is easily seen that the presentation 𝒢 = ( G, v 0) \mathcal{G}=(G,v_{0}) obtained this way has the desired properties.

1. (1)

The graph G G is right-resolving because there every vertex has exit edges with distinct edge-labels by construction.

2. (2)

The graph G G is essential because every vertex has at least one admissible exit edge, as shown above.

3. (3)

The graph is connected since we include in it only vertices reachable from v 0 v_{0}.

Since G G is essential, 𝒢 \mathcal{G} is a presentation of a certain 3 3 -adic path set via the correspondence taking infinite walks beginning at the v 0 v_{0} -state in 𝒢 \mathcal{G} to words in the edges traversed. Denote this path set X 𝒢, 0 X_{\mathcal{G},0}.

It remains to prove that this is the path set X ⁡ ( 1, M) X(1,M) corresponding to 𝒞 ⁡ ( 1, M) \mathcal{C}(1,M), which is the claim that

 | X 𝒢, 0 = X ⁡ ( 1, M). X_{\mathcal{G},0}=X(1,M). |  |

To prove the claim, let Φ: X 𝒢, 0 → ℤ 3 \Phi:X_{\mathcal{G},0}\rightarrow\mathbb{Z}_{3} be the map

 | ⋯ a 2 a 1 a 0 ↦ ∑ k = 0 ∞ a k 3 k. \cdots a_{2}a_{1}a_{0}\mapsto\sum_{k=0}^{\infty}{a_{k}3^{k}}. |  |

Φ \Phi is clearely an injection. Φ ⁡ ( X 𝒢, 0) ⊂ 𝒞 ⁡ ( 1, M) \Phi(X_{\mathcal{G},0})\subset\mathcal{C}(1,M): Since ⋯ a 2 a 1 a 0 ∈ X 𝒢, 0 \cdots a_{2}a_{1}a_{0}\in X_{\mathcal{G},0} is a word in the full shift on { 0, 1 } \{0,1\}, Φ ( ⋯ a 2 a 1 a 0) = ∑ k = 0 ∞ a k 3 k \Phi(\cdots a_{2}a_{1}a_{0})=\sum_{k=0}^{\infty}{a_{k}3^{k}} omits the digit 2, so that Φ ⁡ ( X 𝒢, 0) ⊂ Σ 3 \Phi(X_{\mathcal{G},0})\subset\Sigma_{3}. But the algorithm was constructed specifically so that, given a path π = a l a l − 1 ⋯ a 2 a 1 a 0 \pi=a_{l}a_{l-1}\cdots a_{2}a_{1}a_{0} in 𝒢 \mathcal{G} originating at 0, there is an edge labeled a l + 1 ∈ { 0, 1 } a_{l+1}\in\{0,1\} from the terminal vertex t ⁡ ( π) t(\pi) if and only if each digit of the 3-adic expansion of M ⋅ ( ∑ k = 0 l + 1 c k ​ 3 k) M\cdot\big(\sum_{k=0}^{l+1}{c_{k}3^{k}}\big) which cannot be altered by any potential ( l + 2) (l+2) nd digit is either 0 or 1. This shows both that Φ ⁡ ( X 𝒢, 0) ⊂ 1 M ​ Σ 3 \Phi(X_{\mathcal{G},0})\subset\frac{1}{M}\Sigma_{3} and 𝒞 ⁡ ( 1, M) ⊂ Φ ⁡ ( X 𝒢, 0) \mathcal{C}(1,M)\subset\Phi(X_{\mathcal{G},0}), so that Φ | Φ − 1 ​ ( 𝒞 ​ ( 1, M)): X 𝒢, 0 → 𝒞 ⁡ ( 1, M) \Phi|_{\Phi^{-1}(\mathcal{C}(1,M))}:X_{\mathcal{G},0}\rightarrow\mathcal{C}(1,M) is a bijection. Assigning the appropriate metric to X 𝒢, 0 X_{\mathcal{G},0} makes Φ \Phi an isomorphism in a now obvious way, proving the claim. ∎

We obtain an algorithm to construct 𝒢 = ( G, v 0) \mathcal{G}=(G,v_{0}) based on the construction above.

Algorithm A (Algorithmic Construction of Path Set Presentation X ⁡ ( 1, M) X(1,M)).

1. (1)

(Initial Step) Start with initial marked vertex v 0 v_{0}, and initial vertex set I 0:= { v 0 } I_{0}:=\{v_{0}\}. Add an exit edge with edge label 0 0 giving a self-loop to v 0 v_{0}, and add another exit edge with edge label 1 1 going to new vertex v m v_{m} with vertex label m:= ⌊ M / 3 ⌋, m:=\lfloor M/3\rfloor, Add these two edges and their labels to form (labeled) edge table E 1 E_{1}. Form the new vertex set I 1:= { v m } I_{1}:=\{v_{m}\}, and go to Recursive Step with j = 1 j=1.

2. (2)

(Recursive step) Given value j j, a nonempty new vertex set I j I_{j} of level j j vertices, a current vertex set V j V_{j} and current edge set E j E_{j}. At step j + 1 j+1 determine all allowable exit edge labels from vertices v N v_{N} in I j I_{j}, using the criterion ( 3.2), and compute vertices reachable by these exit edges, with reachable vertex labels computed by update equation ( 3.3). Add these new edges and their labels to current edge set to make updated current edge set E j + 1 E_{j+1}. Collect all vertices reached that are not in current vertex set V j V_{j} into a new vertex set I j + 1 I_{j+1}. Update current vertex set V j + 1 = V j ∪ I j + 1. V_{j+1}=V_{j}\cup I_{j+1}. Go to test step.

3. (3)

(Test step). If the current vertex set I j + 1 I_{j+1} is empty, halt, with the complete presentation 𝒢 = ( G, v 0) {\mathcal{G}}=(G,v_{0}) given by sets V j + 1, E j + 1 V_{j+1},E_{j+1}. If I j + 1 I_{j+1} is nonempty, reset j ↦ j + 1 j\mapsto j+1 and go to Recursive Step.

The correctness of the algorithm follows from the discussion above.

### 3.2. Constructing a path set presentation X ⁡ ( 1, M 1, …, M n) X(1,M_{1},\ldots,M_{n})

Given integers 1 ≤ M 1 < … < M n 1\leq M_{1}<\ldots<M_{n}, we now have a way to construct graph presentations of the path sets X ⁡ ( 1, M i) X(1,M_{i}) for each i i. Since

 | X ⁡ ( 1, M 1, …, M n) = ⋂ i = 1 n X ⁡ ( 1, M i), X(1,M_{1},\ldots,M_{n})=\bigcap_{i=1}^{n}X(1,M_{i}), |  |

we need to know how to combine these graphs.

Recall the following definition from Lind and Marcus [13]:

###### Definition 3.2.

Let 𝒢 1 \mathcal{G}_{1} and 𝒢 2 \mathcal{G}_{2} be labeled graphs with the same alphabet 𝒜 \mathcal{A}, and let their underlying graphs be G 1 = ( 𝒱 1, ℰ 1) G_{1}=(\mathcal{V}_{1},\mathcal{E}_{1}) and G 2 = ( 𝒱 2, ℰ 2) G_{2}=(\mathcal{V}_{2},\mathcal{E}_{2}). The label product 𝒢 1 ⋆ 𝒢 2 \mathcal{G}_{1}\star\mathcal{G}_{2} of 𝒢 1 \mathcal{G}_{1} and 𝒢 2 \mathcal{G}_{2} has underlying graph G G with vertex set 𝒱 = 𝒱 1 × 𝒱 2 \mathcal{V}=\mathcal{V}_{1}\times\mathcal{V}_{2}, edge set ℰ = { ( e 1, e 2) ∈ ℰ 1 × ℰ 2: e 1 ​ and ​ e 2 ​ have the same labels } \mathcal{E}=\{(e_{1},e_{2})\in\mathcal{E}_{1}\times\mathcal{E}_{2}:e_{1}\text{ and }e_{2}\text{ have the same labels}\}.

In [1, Proposition 4.3], we show that if ( 𝒢 i, v i) (\mathcal{G}_{i},v_{i}) is a graph presentation of the path set 𝒫 i \mathcal{P}_{i}, then ( 𝒢 1 ⋆ 𝒢 2, ( v 1, v 2)) (\mathcal{G}_{1}\star\mathcal{G}_{2},(v_{1},v_{2})) is a graph presentation for 𝒫 1 ∩ 𝒫 2 \mathcal{P}_{1}\cap\mathcal{P}_{2}. It follows that we can form a presentation of 𝒞 ⁡ ( 1, M 1, ⋯, M n) \mathcal{C}(1,M_{1},\cdots,M_{n}) as the label product

 | ( 𝒢, v) = ( 𝒢 1 ⋆ 𝒢 2 ⋆ ⋯ ⋆ 𝒢 n, ( v 1, v 2, …, v n)), (\mathcal{G},v)=(\mathcal{G}_{1}\star\mathcal{G}_{2}\star\cdots\star\mathcal{G}_{n},(v_{1},v_{2},\ldots,v_{n})), |  |

where ( 𝒢 i, v i) (\mathcal{G}_{i},v_{i}) is the presentation of 𝒞 ⁡ ( 1, M i) \mathcal{C}(1,M_{i}) just constructed.

###### Theorem 3.3.

For 1 < M 1 < M 2 < ⋯ < M n 1<M_{1}<M_{2}<\cdots<M_{n}, with all M i ≡ 1 ( mod 3) M_{i}\equiv 1~(\bmod\,3), the set

 | OPEN 𝒞 ⁡ ( 1, M 1, M 2, ⋯, M n)) = ⋂ i = 1 n 𝒞 ⁡ ( 1, M i) = Σ 3 ∩ ( ⋂ i = 1 n 1 M i ​ Σ 3), \mathcal{C}(1,M_{1},M_{2},\cdots,M_{n}))=\bigcap_{i=1}^{n}\mathcal{C}(1,M_{i})=\Sigma_{3}\cap(\bigcap_{i=1}^{n}\frac{1}{M_{i}}\Sigma_{3}), |  |

has 3 3 -adic expansions of its elements given by a path set X ⁡ ( 1, M 1, M 2, ⋯, M n) X(1,M_{1},M_{2},\cdots,M_{n}). This path set has an algorithmically computable presentation ( 𝒢, v 𝟎) (\mathcal{G},v_{\bf 0}), in which the vertices v 𝐍 v_{\bf{N}} are labeled with a subset of integer vectors 𝐍 = ( N 1, N 2, …, N n) {\bf{N}}=(N_{1},N_{2},...,N_{n}) with 0 ≤ N i ≤ 1 2 ​ M i 0\leq N_{i}\leq\frac{1}{2}M_{i}, always including the zero vector 𝟎 \bf{0}. The presentation has at most ∏ i = 1 n ( 1 + ⌊ 1 2 ​ M i ⌋) \prod_{i=1}^{n}(1+\lfloor\frac{1}{2}M_{i}\rfloor) vertices in the underlying graph. This presentation is right-resolving, connected and essential.

###### Proof.

The presentation is obtained by recursively applying the label product construction to the presentations 𝒞 ⁡ ( 1, M i) \mathcal{C}(1,M_{i}), see Algorithm B below. Each step preserves the properties of the presentation graph being right-resolving, connected and essential. The number of states of the label product construction is at most the product of the number of states in the two presentations being constructed. By Theorem 3.1, the presentation of 𝒞 ⁡ ( 1, M i) \mathcal{C}(1,M_{i}) has at most ( 1 + ⌊ 1 2 ​ M ⌋) (1+\lfloor\frac{1}{2}M\rfloor) vertices. The bound given follows by induction on the successive label product constructions. ∎

Algorithm B (Algorithmic Construction of Path Set Presentation X ⁡ ( 1, M 1, …, M n) X(1,M_{1},...,M_{n}).

1. (1)

(Initial Step) Construct presentations 𝒢 i = ( G i, ℒ i) \mathcal{G}_{i}=(G_{i},{\mathcal{L}}_{i}) for X ⁡ ( 1, M i) X(1,M_{i}) to 𝒞 ⁡ ( 1, M i) \mathcal{C}(1,M_{i}) for 1 ≤ i ≤ n 1\leq i\leq n, using Algorithm A. Apply the label product construction to form ℋ 2:= 𝒢 1 ⋆ 𝒢 2 \mathcal{H}_{2}:=\mathcal{G}_{1}\star\mathcal{G}_{2}.

2. (2)

For 2 ≤ i ≤ n − 1 2\leq i\leq n-1, apply the label product construction to form

 | ℋ i + 1 = ℋ i ⋆ 𝒢 i + 1. \mathcal{H}_{i+1}=\mathcal{H}_{i}\star\mathcal{G}_{i+1}. |  |

Halt when ℋ n \mathcal{H}_{n} is computed.

### 3.3. Path Set Characterization of 𝒞 ⁡ ( 1, M 1, …, M n) \mathcal{C}(1,M_{1},...,M_{n})

From Theorem 3.3 we easily derive the following result.

###### Theorem 3.4.

For any integers 1 ≤ M 1 < … < M n 1\leq M_{1}<\ldots<M_{n}, let

 | 𝒞 ⁡ ( 1, M 1, …, M n):= Σ 3 ∩ 1 M 1 ​ Σ 3 ∩ … ∩ 1 M n ​ Σ 3. \mathcal{C}(1,M_{1},\ldots,M_{n}):=\Sigma_{3}\cap\frac{1}{M_{1}}\Sigma_{3}\cap\ldots\cap\frac{1}{M_{n}}\Sigma_{3}. |  |

This is the set of all 3 3 -adic integers λ ∈ Σ 3 \lambda\in\Sigma_{3} such that M j ​ λ M_{j}\lambda omits the digit 2 2 in its 3 3 -adic expansion. Then:

(1) The complete set of the 3 3 -adic expansions of numbers in the set 𝒞 ⁡ ( 1, M 1, …, M n) \mathcal{C}(1,M_{1},\ldots,M_{n}), is a path set in the alphabet 𝒜 = { 0, 1, 2 }. {\mathcal{A}}=\{0,1,2\}.

(2) The Hausdorff dimension of 𝒞 ⁡ ( 1, M 1, …, M n) \mathcal{C}(1,M_{1},\ldots,M_{n}) is log 3 ⁡ β \log_{3}\beta, where log ⁡ β \log\beta is the topological entropy of this path set. Here β \beta necessarily satisfies 1 ≤ β ≤ 2 1\leq\beta\leq 2, and β \beta is a Perron number, i.e. it is a real algebraic integer β ≥ 1 \beta\geq 1 such that all its other algebraic conjugates satisfy | σ ⁡ ( β) | < β. |\sigma(\beta)|<\beta.

###### Proof.

Theorem 3.3 gives an explicit construction of a presentation ( 𝒢, v) ({\mathcal{G}},v) showing that 𝒞 ⁡ ( 1, M 1 ​ …, M n) \mathcal{C}(1,M_{1}\ldots,M_{n}) is a p p -adic path set.

By Proposition 2.2 the Hausdorff dimension of 𝒞 ⁡ ( 1, M 1 ​ …, M n) \mathcal{C}(1,M_{1}\ldots,M_{n}) is log 3 ⁡ β \log_{3}\beta, where β \beta is the spectral radius of the adjacency matrix A A of the underlying graph G G. Since A A is a 0-1 matrix, by Perron-Frobenius theory the spectral radius equals the maximal eigenvalue in absolute value, which is necessarily a positive real number β \beta. It is a solution to a monic polynomial over ℤ \mathbb{Z}, so that β \beta is necessarily an algebraic integer. By construction, the sum of the entries of any row in A A is either 1 or 2, so that we also have 1 ≤ β ≤ 2 1\leq\beta\leq 2. ∎

###### Remark 3.5.

The adjacency matrix A A in the sets above need not be irreducible. Example 3.3 below presents a graph 𝒞 ⁡ ( 1, 19) \mathcal{C}(1,19) having a reducible matrix A A. Here the underlying graph 𝒢 {\mathcal{G}} has two strongly connected components.

Combining the results above establishes Theorem 1.6.

###### Proof of Theorem 1.6.

(1) This follows from Theorem 3.1 and Theorem 3.3, with the algorithm for constructing a the presentation of the path set X ⁡ ( 1, M 1, M 2, ⋯, M n) X(1,M_{1},M_{2},\cdots,M_{n}) given by combining Algorithm A and Algorithm B.

(2) This follows from Theorem 3.4. ∎

### 3.4. Examples

We present several examples of path set presentations.

###### Example 3.1.

The 3 3 -adic Cantor set Σ 3 = 𝒞 ⁡ ( 1) = 𝒞 ⁡ ( 1, 1) \Sigma_{3}=\mathcal{C}(1)=\mathcal{C}(1,1) has a path set presentation ( 𝒢, v 0) ({\mathcal{G}},v_{0}) pictured in Figure 3.1. It is the full shift on two symbols, and the initial vertex is the vertex labeled 0 0. The underlying graph G G of 𝒢 {\mathcal{G}} is a double cover of a one vertex graph with two symbols. The advantage of the graph G G pictured is that a path for it is completely determined by the set of vertex symbols that it passes through.

-80,-40)(80,40) 20pt0 n11n00 20pt1
FIGURE 3.1. Path set presentation of Cantor shift Σ 3 = 𝒞 ⁡ ( 1) \Sigma_{3}=\mathcal{C}(1). The marked vertex is 0 0.

###### Example 3.2.

A path set presentation of 𝒞 ⁡ ( 1, 7) \mathcal{C}(1,7), with 7 = ( 21) 3 7=(21)_{3} is shown in Figure 3.2. The vertex labeled 0 0 is the marked initial state.

-80,-50)(80,150) 20pt0 20pt1 n21 n101 n10 n00
FIGURE 3.2. Path set presentation of 𝒞 ⁡ ( 1, 7) \mathcal{C}(1,7). The marked vertex is 0 0.

The graph in Figure 3.2 has adjacency matrix

 | 𝐀 = ( 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟏 𝟏 𝟏 𝟎 𝟎 𝟎), \bf{A}=\left(\begin{array}[]{cccc}1&1&0&0\\ 0&0&1&0\\ 0&0&1&1\\ 1&0&0&0\\ \end{array}\right), |  |

which has Perron-Frobenius eigenvalue β = 1 + 5 2 \beta=\frac{1+\sqrt{5}}{2}, so

 | dim H ( 𝒞 ⁡ ( 1, 7)) = log 3 ⁡ ( 1 + 5 2) ≈ 0.438018. \dim_{H}(\mathcal{C}(1,7))=\log_{3}\left(\frac{1+\sqrt{5}}{2}\right)\approx 0.438018. |  |

###### Example 3.3.

A path set presentation of 𝒞 ⁡ ( 1, 19) \mathcal{C}(1,19), with 19 = ( 201) 3 19=(201)_{3}, is shown in Figure 3.3. The node labeled 0 0 is the marked initial state.

-100,-165)(100,160) 20pt0 20pt1 n211n20 n201 n221 n1001 n100 n20 n00 n211 n10
FIGURE 3.3. Path set presentation of 𝒞 ⁡ ( 1, 19) \mathcal{C}(1,19). The marked vertex is 0 0.

The graph in Figure 3.3 has adjacency matrix

 | 𝐀 = ( 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎), \bf{A}=\left(\begin{array}[]{cccccccc}1&1&0&0&0&0&0&0\\ 0&0&1&1&0&0&0&0\\ 0&0&0&0&1&0&0&0\\ 0&0&0&0&0&1&0&0\\ 0&0&0&0&1&0&1&0\\ 0&0&0&1&0&0&0&0\\ 0&0&0&0&0&1&0&1\\ 1&0&0&0&0&0&0&0\\ \end{array}\right), |  |

which has Perron eigenvalue β ≈ 1.465571 \beta\approx 1.465571, so

 | dim H ( 𝒞 ⁡ ( 1, 19)) = log 3 ⁡ β ≈ 0.347934. \dim_{H}(\mathcal{C}(1,19))=\log_{3}\beta\approx 0.347934. |  |

###### Example 3.4.

We consider implementation of the algorithm for 𝒞 ⁡ ( 1, 7, 19) \mathcal{C}(1,7,19). We start from the presentations of 𝒞 ⁡ ( 1, 7) \mathcal{C}(1,7) and 𝒞 ⁡ ( 1, 19) \mathcal{C}(1,19) in Example 3.1. Taking the label product gives us a presentation of 𝒞 ⁡ ( 1, 7, 19) \mathcal{C}(1,7,19), which is shown in Figure 3.4.

-50,-45)(50,155) 20pt0 q2-201 q10-221 q10-1001 q1-100 q0-10 q0-00 20pt1
FIGURE 3.4. Path set presentation of 𝒞 ⁡ ( 1, 7, 19) \mathcal{C}(1,7,19). The marked vertex is 0 0.

This graph G G for 𝒞 ⁡ ( 1, 7, 19) \mathcal{C}(1,7,19) has adjacency matrix 𝐀 \bf{A} given by:

 | 𝐀 = ( 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎). \bf{A}=\left(\begin{array}[]{cccccc}1&1&0&0&0&0\\ 0&0&1&0&0&0\\ 0&0&0&1&0&0\\ 0&0&0&1&1&0\\ 0&0&0&0&0&1\\ 1&0&0&0&0&0\\ \end{array}\right). |  |

The Perron eigenvalue β ≈ 1.46557 \beta\approx 1.46557 of this matrix is the largest real root of λ 6 − 2 ​ λ 5 + λ 4 − 1 = 0 \lambda^{6}-2\lambda^{5}+\lambda^{4}-1=0: The Hausdorff dimension of 𝒞 ⁡ ( 1, 7, 19) \mathcal{C}(1,7,19) is then

 | dim H ( 𝒞 ⁡ ( 1, 7, 19)) = log 3 ⁡ β ≈ 0.347934. \dim_{H}(\mathcal{C}(1,7,19))=\log_{3}\beta\approx 0.347934. |  | (3.4) |

###### Example 3.5.

The set 𝒞 ⁡ ( 1, 43) \mathcal{C}(1,43), with N = 43 = ( 1121) 3 N=43=(1121)_{3} has M ≡ 1 ( mod 3) M\equiv\,1\,(\bmod\,3), but nevertheless has Hausdorff dimension 0 0. A presentation of the path set associated to 𝒞 ⁡ ( 1, 43) \mathcal{C}(1,43) is given in Figure 3.5.

-80,-15)(80,105) 20pt0 q1121 q2011 q200 q1211 q20 q120q1211 q1201 q120 q2011
FIGURE 3.5. Path set presentation of 𝒞 ⁡ ( 1, 43) \mathcal{C}(1,43). The marked vertex is 0 0.

The graph in Figure 3.5 has four strongly connected components, with vertex sets { 0 }, { 112 }, { 2,120,201, 20 }, \{0\},\{112\},\{2,120,201,20\}, and { 12,121 } \{12,121\} respectively, each of whose underlying path sets have Hausdorff dimension 0 0.

## 4. Infinite Families

### 4.1. Basic Properties

We have the following simple result, showing the influence of the digits in the 3 3 -adic expansion of M M on the size of the set 𝒞 ⁡ ( 1, M) \mathcal{C}(1,M) and 𝒞 ⁡ ( 1, M 1, M 2, ⋯, M k) \mathcal{C}(1,M_{1},M_{2},\cdots,M_{k}).

###### Theorem 4.1.

(1) If the smallest nonzero 3 3 -adic digit in the 3 3 -adic expansion of the positive integer M M is 2 2, then 𝒞 ⁡ ( 1, M) = { 0 } \mathcal{C}(1,M)=\{0\}, and

 | dim H ( 𝒞 ⁡ ( 1, M)) = 0. \dim_{H}(\mathcal{C}(1,M))=0. |  | (4.1) |

(2) If positive integers M 1, M 2, …, M n ∈ Σ 3 M_{1},M_{2},...,M_{n}\in\Sigma_{3} all have the property that their 3 3 -adic expansions ( M i) 3 (M_{i})_{3} (equivalently their ternary expansions) contain only digits 0 0 and 1 1, then

 | dim H ( 𝒞 ⁡ ( 1, M 1, M 2, …, M n)) > 0. \dim_{H}(\mathcal{C}(1,M_{1},M_{2},...,M_{n}))>0. |  | (4.2) |

#### Remark.

For neither (1) or (2) does the converse hold. The example M = 43 = ( 1121) 3 M=43=(1121)_{3} has dim H ( 𝒞 ⁡ ( 1, M)) = 0 \dim_{H}(\mathcal{C}(1,M))=0, but its 3 3 -adic expansion has smallest digit 1 1. The example M = 64 = ( 2101) 3 M=64=(2101)_{3} has dim H ( 𝒞 ⁡ ( 1, M)) > 0 \dim_{H}(\mathcal{C}(1,M))>0, but its 3 3 -adic expansion has a digit 2 2.

###### Proof.

of Theorem 4.1. (1) Suppose the smallest nonzero 3 3 -adic digit in the 3 3 -adic expansion of the positive integer M M is 2 2. Then the graph presentation of the path set X ⁡ ( 1, M) X(1,M) associated to 𝒞 ⁡ ( 1, M) \mathcal{C}(1,M) constructed using Algorithm A consists of only the node labeled 0 0 and the self-loop labeled 0 0 at this node (i.e. 𝒞 ⁡ ( 1, M) = { 0 } \mathcal{C}(1,M)=\{0\}), whence dim H ( 𝒞 ⁡ ( 1, M)) = 0 \dim_{H}(\mathcal{C(}1,M))=0. This holds because the smallest nonzero digit of M ​ N MN for any N ∈ Σ 3 N\in\Sigma_{3} is 2 2, so that M ​ N ∉ Σ 3 MN\notin\Sigma_{3}.

(2) Suppose M 1, …, M n ∈ Σ 3 M_{1},\ldots,M_{n}\in\Sigma_{3} are positive integers so that all of their 3 3 -adic expansions have only the digits 0 0 and 1 1. For each M i M_{i}, let m i m_{i} be the largest nonzero ternary position of M i M_{i} (i.e. M i = 3 m i + M_{i}=3^{m_{i}}+*lower order terms*). Then in the graph presentation constructed for X ⁡ ( 1, M i) X(1,M_{i}) by Algorithm A, the walk starting at the origin, then moving along an edge labeled 1 1 (which exists since ( M i) 3 (M_{i})_{3} omits the digit 2 2), then moving along m i m_{i} consecutive edges labeled 0 0, is a directed cycle at 0 0. Since the edge labeled 0 0 is a loop at 0 0, if we let m = max 1 ≤ i ≤ n ⁡ m i m=\max_{1\leq i\leq n}m_{i}, then the graph presentation the path set X ⁡ ( 1, M 1, …, M j) X(1,M_{1},...,M_{j}) of 𝒞 ⁡ ( 1, M 1, …, M n) \mathcal{C}(1,M_{1},\ldots,M_{n}) has a directed cycle at 0 0 of length m + 1 m+1 given by first traversing the edge labeled 1 1, then traversing m m consecutive edges labeled 0 0. This cycle and plus the loop of length one at 0 0 are distinct directed cycles at 0 0. It follows that the associated path set has positive topological entropy, and hence 𝒞 ⁡ ( 1, M 1, …, M n) \mathcal{C}(1,M_{1},\ldots,M_{n}) has positive Hausdorff dimension by [2, Theorem 3.1 (iii)]. ∎

### 4.2. The family L k = ( 1 k) 3 = 1 2 ​ ( 3 k − 1) L_{k}=(1^{k})_{3}=\frac{1}{2}(3^{k}-1).

The path set presentations ( 𝒢, v 0) (\mathcal{G},v_{0}) of the sets 𝒞 ⁡ ( 1, L k) \mathcal{C}(1,L_{k}) are particularly simple to analyze.

###### Theorem 4.2.

(1) For k ≥ 1 k\geq 1, and L k = 1 2 ​ ( 3 k − 1) L_{k}=\frac{1}{2}(3^{k}-1), there holds

 | dim H ( 𝒞 ⁡ ( 1, L k)) = log 3 ⁡ β k, \dim_{H}(\mathcal{C}(1,L_{k}))=\log_{3}\beta_{k}, |  | (4.3) |

where β k \beta_{k} is the unique real root greater than 1 1 of

 | λ k − λ k − 1 − 1 = 0. \lambda^{k}-\lambda^{k-1}-1=0. |  | (4.4) |

(2) For k ≥ 6 k\geq 6, the values β k \beta_{k} satisfy the bounds

 | 1 + log ⁡ k k − 2 ​ log ⁡ log ​ k k ≤ β k ≤ 1 + log ⁡ k k. 1+\frac{\log k}{k}-\frac{2\log\log k}{k}\leq\beta_{k}\leq 1+\frac{\log k}{k}. |  | (4.5) |

Then for all k ≥ 3 k\geq 3,

 | dim H ( 𝒞 ⁡ ( 1, L k)) = log 3 ⁡ k k + O ⁡ ( log ⁡ log ⁡ k log ⁡ k). \dim_{H}(\mathcal{C}(1,L_{k}))=\frac{\log_{3}k}{k}+O\Big(\frac{\log\log k}{\log k}\Big). |  | (4.6) |

Path set | Perron eigenvalue | Hausdorff dim |

𝒞 ⁡ ( 1, L 1) \mathcal{C}(1,L_{1}) | 2.000000 2.000000 | 0.630929 0.630929 |

𝒞 ⁡ ( 1, L 2) \mathcal{C}(1,L_{2}) | 1.618033 1.618033 | 0.438018 0.438018 |

𝒞 ⁡ ( 1, L 3) \mathcal{C}(1,L_{3}) | 1.465571 1.465571 | 0.347934 0.347934 |

𝒞 ⁡ ( 1, L 4) \mathcal{C}(1,L_{4}) | 1.380278 1.380278 | 0.293358 0.293358 |

𝒞 ⁡ ( 1, L 5) \mathcal{C}(1,L_{5}) | 1.324718 1.324718 | 0.255960 0.255960 |

𝒞 ⁡ ( 1, L 6) \mathcal{C}(1,L_{6}) | 1.285199 1.285199 | 0.228392 0.228392 |

𝒞 ⁡ ( 1, L 7) \mathcal{C}(1,L_{7}) | 1.255423 1.255423 | 0.207052 0.207052 |

𝒞 ⁡ ( 1, L 8) \mathcal{C}(1,L_{8}) | 1.232055 1.232055 | 0.189948 0.189948 |

𝒞 ⁡ ( 1, L 9) \mathcal{C}(1,L_{9}) | 1.213150 1.213150 | 0.175877 0.175877 |

TABLE 4.1. Hausdorff dimensions of 𝒞 ⁡ ( 1, L k) \mathcal{C}(1,L_{k}) (to six decimal places)

We first analyze the structure of the directed graph ( 𝒢, v 0) (\mathcal{G},v_{0}) in this presentation.

###### Proposition 4.3.

For L k = ( 1 k) 3 = 1 2 ​ ( 3 k − 1) L_{k}=(1^{k})_{3}=\frac{1}{2}(3^{k}-1) the path set 𝒞 ⁡ ( 1, L k) \mathcal{C}(1,L_{k}) has a presentation ( 𝒢, v 0) ({\mathcal{G}},v_{0}) given by Algorithm A which has exactly k k vertices. The vertices v m v_{m} have labels m = 0 m=0 and m = ( 1 j) 3 m=(1^{j})_{3}, for 1 ≤ j ≤ k − 1 1\leq j\leq k-1. The underlying directed graph G G is strongly connected and primitive.

###### Proof.

The presentation ( 𝒢, v 0) (\mathcal{G},v_{0}) of 𝒞 ⁡ ( 1, L k) \mathcal{C}(1,L_{k}) has an underlying directed graph G G having k k vertices V n V_{n} with N = 0 N=0 and N = ( 1 j) 3 N=(1^{j})_{3} for 1 ≤ j ≤ k − 1 1\leq j\leq k-1. The vertex v 0 v_{0} has two exit edges labeled 0 0 and 1 1, and all other vertices have a unique exit edge labeled 0 0. The edges form a self-loop at 0 0 labeled 0 0, and a directed k k -cycle, whose vertex labels are

 | 0 → ( 1 k − 1) 3 → ( 1 k − 2) 3 → ⋯ ( 1 2) 3 → ( 1) 3 → 0, 0\to(1^{k-1})_{3}\to(1^{k-2})_{3}\to\cdots(1^{2})_{3}\to(1)_{3}\to 0, |  |

This cycle certifies strong connectivity of the graph G G, and in it all edge labels are 0 0 except the edge 0 → ( 1 k − 1) 3 0\to(1^{k-1})_{3} labeled 1 1. Primitivity follows because it has a cycle of length 1 1 at vertex ( 0) 3 (0)_{3}. ∎

###### Proof of Theorem 4.2.

(1) By appropriate ordering of the vertices, the adjacency matrix 𝐀 \bf{A} of 𝒢 \mathcal{G} is the k × k k\times k matrix

 | 𝐀 = ( 𝟏 𝟏 𝟎 … 𝟎 𝟎 𝟎 𝟏 ⋱ ⋮ ⋮ ⋮ ⋱ ⋱ 𝟎 𝟎 𝟎 … 𝟎 𝟏 𝟏 𝟎 … 𝟎 𝟎). \bf{A}=\left(\begin{array}[]{ccccc}1&1&0&\ldots&0\\ 0&0&1&\ddots&\vdots\\ \vdots&\vdots&\ddots&\ddots&0\\ 0&0&\ldots&0&1\\ 1&0&\ldots&0&0\end{array}\right). |  |

The characteristic polynomial of this matrix is

 | p k ​ ( λ):= det ( λ ​ 𝐈 − 𝐀) = det ( λ − 𝟏 − 𝟏 𝟎 … 𝟎 𝟎 λ − 𝟏 ⋱ ⋮ ⋮ ⋮ ⋱ ⋱ 𝟎 𝟎 𝟎 … λ − 𝟏 − 𝟏 𝟎 … 𝟎 λ). p_{k}(\lambda):=\det(\lambda\bf{I}-\bf{A})=\det\left(\begin{array}[]{ccccc}\lambda-1&-1&0&\ldots&0\\ 0&\lambda&-1&\ddots&\vdots\\ \vdots&\vdots&\ddots&\ddots&0\\ 0&0&\ldots&\lambda&-1\\ -1&0&\ldots&0&\lambda\end{array}\right). |  |

Expansion of this determinant by minors on the first column yields

 | p k ​ ( λ) = ( λ − 1) ​ λ k − 1 + ( − 1) k − 1 ​ ( − 1) ​ ( − 1) k − 1 = λ k − λ k − 1 − 1. \displaystyle p_{k}(\lambda)=(\lambda-1)\lambda^{k-1}+(-1)^{k-1}(-1)(-1)^{k-1}=\lambda^{k}-\lambda^{k-1}-1. |  | (4.7) |

The Perron eigenvalue of the nonnegative matrix 𝐀 \bf{A} will be a positive real root α k ≥ 1 \alpha_{k}\geq 1 of p ⁡ ( λ) p(\lambda). By ( 2.1) the topological entropy of the path set X ⁡ ( 1, L k) X(1,L_{k}) associated to C ⁡ ( 1, L k) C(1,L_{k}) is log ⁡ β k \log\beta_{k}, while by Proposition 2.2 the Hausdorff dimension of the 3 3 -adic path set fractal C ⁡ ( 1, L k) C(1,L_{k}) itself is log 3 ⁡ β k \log_{3}\beta_{k}

(2) We estimate the size of β k \beta_{k}. There is at most one real root β k ≥ 1 \beta_{k}\geq 1 since for λ > 1 − 1 / k \lambda>1-1/k one has

 | p k ′ ( λ) \displaystyle p_{k}^{{}^{\prime}}(\lambda) | = \displaystyle= | k ​ λ k − 1 − ( k − 1) ​ λ k − 2 = λ k − 2 ​ ( k ​ λ − ( k − 1)) > 0. \displaystyle k\lambda^{k-1}-(k-1)\lambda^{k-2}=\lambda^{k-2}(k\lambda-(k-1))>0. |  |

For the lower bound, we consider p k ​ ( λ) p_{k}(\lambda) for λ > 1 \lambda>1 and define variables y > 0 y>0 by λ = 1 + y k \lambda=1+\frac{y}{k} with y > 0 y>0, and x:= λ k > 1 x:=\lambda^{k}>1, noting that w = λ k = ( 1 + y k) k < e y w=\lambda^{k}=(1+\frac{y}{k})^{k}<e^{y} Now

 | λ k − 1 + 1 = x 1 + y k + 1 ≥ x ⁡ ( 1 − y k) + 1 ≥ x + ( 1 − x ​ y k), \lambda^{k-1}+1=\frac{x}{1+\frac{y}{k}}+1\geq x\left(1-\frac{y}{k}\right)+1\geq x+\left(1-\frac{xy}{k}\right), |  |

which exceeds x x whenever x ​ y ≤ k xy\leq k. Thus we have p k ​ ( 1 + y k) < 0 p_{k}(1+\frac{y}{k})<0 whenever x ​ y < y ​ e y ≤ k xy<ye^{y}\leq k. The choice y = log ⁡ k − 2 ​ log ⁡ log ​ k y=\log k-2\log\log k gives, for k ≥ 3 k\geq 3,

 | y ​ e y ≤ log ⁡ k ⁡ ( e log ⁡ k − 2 ​ log ⁡ log ​ k) ≤ k log ⁡ k ≤ k. ye^{y}\leq\log k(e^{\log k-2\log\log k})\leq\frac{k}{\log k}\leq k. |  |

Thus we have, for k ≥ 3 k\geq 3, p k ​ ( 1 + log ⁡ k k − 2 ​ log ⁡ log ⁡ k k) < 0 p_{k}(1+\frac{\log k}{k}-2\frac{\log\log k}{k})<0, so

 | β k ≥ 1 + log ⁡ ( k) k − 2 ​ log ⁡ log ⁡ k k, \beta_{k}\geq 1+\frac{\log(k)}{k}-2\frac{\log\log k}{k}, |  |

which is the lower bound in ( 4.5). For the upper bound, it suffices to show p k ​ ( 1 + log ⁡ k k) > 0 p_{k}(1+\frac{\log k}{k})>0 for k ≥ 6 k\geq 6. We wish to show ( 1 + log ⁡ k k) k − 1 ​ ( log ⁡ k k) > 1 (1+\frac{\log k}{k})^{k-1}(\frac{\log k}{k})>1 for k ≥ 6 k\geq 6. This becomes ( 1 + log ⁡ k k) k − 1 > k log ⁡ k (1+\frac{\log k}{k})^{k-1}>\frac{k}{\log k}, and on taking logarithms requires

 | ( log ⁡ k − 1) ​ log ⁡ ( 1 + log ⁡ k k) > log ⁡ k − log ⁡ log ⁡ k. (\log k-1)\log(1+\frac{\log k}{k})>\log k-\log\log k. |  |

Using the approximation log ⁡ ( 1 + x) ≥ x − 1 2 ​ x 2 \log(1+x)\geq x-\frac{1}{2}x^{2} valid for 0 < x < 1, 0<x<1, we verify this inequality holds for k ≥ 6 k\geq 6, and the upper bound in ( 4.5) follows. The asymptotic estimate ( 4.6) for the Hausdorff dimension of 𝒞 ⁡ ( 1, L k) \mathcal{C}(1,L_{k}) immediately follows by taking logarithms to base 3 3 of the estimates above.

∎

The results above imply Theorem 1.7 in the introduction.

###### Proof of Theorem 1.7.

Assertion (1) follows from Proposition 4.3. Assertions (2) and (3) follow from Theorem 4.2. ∎

### 4.3. The family N k = ( 10 k − 1 ​ 1) 3 = 3 k + 1 N_{k}=(10^{k-1}1)_{3}=3^{k}+1.

We prove the following result.

###### Theorem 4.4.

For every integer k ≥ 0 k\geq 0, and N k = 3 k + 1 = ( 10 k − 1 ​ 1) 3 N_{k}=3^{k}+1=(10^{k-1}1)_{3},

 | dim H ( 𝒞 ⁡ ( 1, N k)) = dim H 𝒞 ⁡ ( 1, ( 10 k − 1 ​ 1) 3) = log 3 ⁡ ( 1 + 5 2) ≈ 0.438018. \dim_{H}(\mathcal{C}(1,N_{k}))=\dim_{H}\mathcal{C}(1,(10^{k-1}1)_{3})=\log_{3}\bigg(\frac{1+\sqrt{5}}{2}\bigg)\approx 0.438018. |  | (4.8) |

To prove this result we first characterize the presentation 𝒢 = ( G, v 0) \mathcal{G}=(G,v_{0}) associated to N k N_{k} by the construction of Theorem 3.1.

###### Proposition 4.5.

For N k = 3 k + 1 N_{k}=3^{k}+1 the path set 𝒞 ⁡ ( 1, N k) \mathcal{C}(1,N_{k}) has a presentation 𝒢 = ( G, v 0) {\mathcal{G}}=(G,v_{0}) given by Algorithm A with the following properties.

(1) The vertices v m v_{m} have labels m m that comprise those integers 0 ≤ m ≤ 1 2 ​ ( 3 k − 1) 0\leq m\leq\frac{1}{2}(3^{k}-1) whose 3 3 -adic expansion ( m) 3 (m)_{3} omits the digit 2 2.

(2) The directed graph G G has exactly 2 k 2^{k} vertices.

(3) The directed graph G G is strongly connected and primitive.

###### Proof.

(1) Any vertex v m v_{m} reachable from v 0 v_{0} has a 3 3 -adic expansion (equivalently ternary expansion) ( m) 3 (m)_{3} that omits the digit 2 2, and has at most k k 3 3 -adic digits. This is proved by induction on the number of steps n n taken. The base case has the node ( 0) 3 (0)_{3}. For the induction step, every vertex in the graph has an exit edge labeled 0 0, and vertices with labels m ≡ 0 ( mod 3) m\equiv 0~(\bmod\,3) also have an exit edge labeled 1 1. The exit edges labeled 0 0 map m = ( b k − 1 b k − 2 ⋯ b 1 b 0) 3 m=(b_{k-1}b_{k-2}\cdots b_{1}b_{0})_{3} to m ′ = ( 0 b k − 1 b k − 2 ⋯ b 2 b 1) 3 m^{\prime}=(0b_{k-1}b_{k-2}\cdots b_{2}{b_{1}})_{3}. The exit edges labeled 1 1 map m m to m ′ = ( 1 b k − 1 b k − 2 ⋯ b 2 b 1) 3 m^{\prime}=(1b_{k-1}b_{k-2}\cdots b_{2}b_{1})_{3}. For both types of exit edges the new vertex reached at the next step omits the digit 2 2 from its 3 3 -adic expansion, completing the induction step.

(2) There are exactly 2 k 2^{k} possible such vertex labels m m in which ( m) 3 (m)_{3} omits the digit 2 2. Call such vertex labels admissible. The largest such m = 1 2 ​ ( 3 k − 1). m=\frac{1}{2}(3^{k}-1).

(3) To show the graph G k G_{k} is strongly connected it suffices to establish that:

1. (R1)

Every possible such vertex l v m v_{m} with admissible label m m is reachable by a directed path in G G from the initial vertex 0 = ( 00 ⋯ 0) 3 0=(00\cdots 0)_{3}.

2. (R2)

All admissible vertices v m v_{m} have a directed path in G G from v m v_{m} to v 0 v_{0}.

Note that (R1), (R2) together imply that G G is strongly connected. To show (R1), write m = ( b k − 1 ⋯ b 0) 3 m=(b_{k-1}\cdots b_{0})_{3}, with all b j = 0 b_{j}=0 or 1 1, and let i i be the smallest index with b i = 1 b_{i}=1. Starting from v 0 v_{0}, we may add a directed series of exit edges labeled in order b i, b i + 1, b i + 2, ⋯, b k − 1 b_{i},b_{i+1},b_{i+2},\cdots,b_{k-1} to arrive at v m v_{m}. Such edges exist in G G, because all intermediate vertices v m ′ v_{m^{\prime}} reached along this path have m ′ ≡ 0 ( mod 3) m^{\prime}\equiv 0~(\bmod 3) so that an exit edges labeled both 0 0 and 1 1 are available at that step. Indeed, the j j -th step in the path has ( m j) 3 (m_{j})_{3} having k − j k-j initial 3 3 -adic digits of 0 0, and k − 1 − i ≤ k − 1 k-1-i\leq k-1.

To show (R2) we observe that for any vertex v m v_{m} following a path of exit edges all labeled 0 0 will eventually arrive at the vertex v 0 v_{0}. This is permissible since ( m) 3 (m)_{3} has all digits 0 0 or 1 1.

Now G k G_{k} is strongly connected, and it is primitive since it has a loop at vertex 0 0. This completes the proof. ∎

To obtain an adjacency matrix for this graph, we must choose a suitable ordering of the vertex labels. Order the vertices of 𝒢 \mathcal{G} recursively as follows: the ( 0 k − 1) 3 (0^{k-1})_{3} -vertex is first I 1 I_{1}, and the ( 10 k − 1) 3 (10^{k-1})_{3} -vertex is second I 2 I_{2}. Now, suppose that at step j j we have ordered the vertices I 1, …, I m I_{1},\ldots,I_{m}, in that order, with m = 2 j m=2^{j}. Then for 1 ≤ j < k 1\leq j<k, we assert that there will be precisely 2 ​ m 2m vertices, all distinct from I 1, …, I m I_{1},\ldots,I_{m}, to which some I i I_{i} has an out edge. We can label these J 11, J 12, …, J m ​ 1, J m ​ 2 J_{11},J_{12},\ldots,J_{m1},J_{m2} so that J i ​ 1 J_{i1} has an in-edge labeled 0 from I i I_{i}, and J i ​ 2 J_{i2} has an in-edge labeled 1 from I i I_{i}. Assuming this assertion, at the j j -th step we expand our ordering to I 1 ​ …, I m, J 11, J 12, …, J m ​ 1, J m ​ 2 I_{1}\ldots,I_{m},J_{11},J_{12},\ldots,J_{m1},J_{m2}.

###### Proposition 4.6.

The ordering of the vertices above is valid, and the adjacency matrix 𝐀 \bf{A} of the underlying graph G G of 𝒢 \mathcal{G} is the following 2 k × 2 k 2^{k}\times 2^{k} matrix 𝐀 = ( a i ​ j) \mathbf{A}=(a_{ij}):

 | a i ​ j = { 1 if ​ 1 ≤ i ≤ 2 k − 1 ​ and ​ j ∈ { 2 ​ i − 1, 2 ​ i }; 1 if ​ 2 k − 1 < 1 ​ and ​ j = 2 ​ ( i − 2 k − 1) − 1; 0 otherwise. a_{ij}=\left\{\begin{array}[]{rl}1&\text{if }1\leq i\leq 2^{k-1}\text{ and }j\in\{2i-1,2i\};\\ 1&\text{if }2^{k-1}<1\text{ and }j=2(i-2^{k-1})-1;\\ 0&\text{otherwise}.\end{array}\right. |  |

This description is consistent and exhaustive, characterizing 𝐀 \mathbf{A}.

To illustrate this, we have for k = 2 k=2

 | 𝐀 = ( 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟏 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎), \bf{A}=\left(\begin{array}[]{cccc}1&1&0&0\\ 0&0&1&1\\ 1&0&0&0\\ 0&0&1&0\\ \end{array}\right), |  |

while for k = 3 k=3 we have

 | 𝐀 = ( 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟏 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟎 𝟏 𝟎). \bf{A}=\left(\begin{array}[]{cccccccc}1&1&0&0&0&0&0&0\\ 0&0&1&1&0&0&0&0\\ 0&0&0&0&1&1&0&0\\ 0&0&0&0&0&0&1&1\\ 1&0&0&0&0&0&0&0\\ 0&0&1&0&0&0&0&0\\ 0&0&0&0&1&0&0&0\\ 0&0&0&0&0&0&1&0\\ \end{array}\right). |  |

###### Proof.

First, we address the ordering of the vertices of 𝒢 \mathcal{G}. According to the prescription of the proposition, I 1 = ( 0) 3 I_{1}=(0)_{3}, I 2 = ( 10 k − 1) 3 I_{2}=(10^{k-1})_{3}. In the next step, there is an out-edge labeled 1 1 from vertex ( 10 k − 1) 3 (10^{k-1})_{3} to ( 110 k − 2) 3 (110^{k-2})_{3}, and an out-edge labeled 0 0 from vertex ( 10 k − 1) 3 (10^{k-1})_{3} to vertex ( 10 k − 2) 3 (10^{k-2})_{3}. This gives I 3 = ( 110 k − 2) 3 I_{3}=(110^{k-2})_{3}, I 4 = ( 10 k − 2) 3 I_{4}=(10^{k-2})_{3}. In general, for k 1 + ⋯ + k r < k k_{1}+\cdots+k_{r}<k all nonnegative, if we have a vertex ( 1 k 1 0 k 2 1 k 3 ⋯ 1 k r 0 k − Σ ​ k i) 3 (1^{k_{1}}0^{k_{2}}1^{k_{3}}\cdots 1^{k_{r}}0^{k-\Sigma k_{i}})_{3}, it has an out-edge labeled 1 1 to a vertex ( 1 k 1 + 1 0 k 2 1 k 3 ⋯ 1 k r 0 k − 1 − Σ ​ k i) 3 (1^{k_{1}+1}0^{k_{2}}1^{k_{3}}\cdots 1^{k_{r}}0^{k-1-\Sigma k_{i}})_{3} and an out-edged labeled 0 0 to a vertex ( 1 k 1 0 k 2 1 k 3 ⋯ 1 k r 0 k − 1 − Σ ​ k i) 3 (1^{k_{1}}0^{k_{2}}1^{k_{3}}\cdots 1^{k_{r}}0^{k-1-\Sigma k_{i}})_{3}. On the other hand, a vertex labeled ( 1 k 1 0 k 2 1 k 3 ⋯ 1 k r) 3 (1^{k_{1}}0^{k_{2}}1^{k_{3}}\cdots 1^{k_{r}})_{3} ending in 1 1 has a single out-edge labeled 0 0 to the vertex ( 1 k 1 0 k 2 1 k 3 ⋯ 1 k r − 1) 3 (1^{k_{1}}0^{k_{2}}1^{k_{3}}\cdots 1^{k_{r}-1})_{3}.

Thus, if an edge-walk originating at the 0 0 -vertex has label ( e r e r − 1 ⋯ e 1) 3 (e_{r}e_{r-1}\cdots e_{1})_{3}, the terminal vertex of this edge walk is the vertex ( e r e r − 1 ⋯ e 1 0 k − r) 3 (e_{r}e_{r-1}\cdots e_{1}0^{k-r})_{3}. Now, for any vertex ending in 0 0, edges labeled 0 0 and 1 1 are both admissible, which means that an edge walk labeled e 1 e 2 ⋯ e k e_{1}e_{2}\cdots e_{k} is admissible for all values e j = 0 e_{j}=0 or e j = 1 e_{j}=1 for all 1 ≤ j ≤ k 1\leq j\leq k. But this, then, says that all possible vertex labels from { 0, 1 } k \{0,1\}^{k} are achieved. Moreover, we showed above that a vertex with label from { 0, 1 } k \{0,1\}^{k} has out-edges only to other vertices labeled from { 0, 1 } k \{0,1\}^{k}, so this is precisely the set of vertices of 𝒢 \mathcal{G}. The r t ​ h r^{th} step of the vertex ordering procedure adds precisely those vertices which end in 0 k − r 0^{k-r}, of which there are 2 r − 1 = 2 ⋅ 2 r − 2 2^{r-1}=2\cdot 2^{r-2}. The procedure ends at the k k th step with those vertices which end in 1 1. In all, there are 2 k 2^{k} vertices, one for each label from { 0, 1 } k \{0,1\}^{k}.

Now we can understand the definition of the coefficients a i ​ j a_{ij} of the adjacency matrix 𝐀 \mathbf{A} of the underlying graph G G of 𝒢 \mathcal{G}. Vertex ( 0) 3 (0)_{3} maps into itself and vertex ( 10 k) 3 (10^{k})_{3}, which are ordered first and second with respect to the ordering. Thus a 11 = a 12 = 1 a_{11}=a_{12}=1, a 1 ​ j = 0 a_{1j}=0 for j > 2 j>2. Now suppose a vertex is ordered i t ​ h i^{t}h ( I i I_{i}) at the r t ​ h r^{th} stage, and r ≤ k − 1 r\leq k-1, so that not all vertices have yet been ordered. There are 2 r 2^{r} vertices ordered so far (so 1 ≤ i ≤ 2 r 1\leq i\leq 2^{r}), and the ( r + 1) s ​ t (r+1)^{st} stage of the construction orders the next 2 r 2^{r} vertices precisely so that the out-edges from vertex I i I_{i} go to vertices I 2 ​ i − 1 I_{2i-1} and I 2 ​ i I_{2i}. This gives the prescription for a i ​ j a_{ij} for 1 ≤ i ≤ 2 k − 1 1\leq i\leq 2^{k-1}.

Observe that the vertices I 2 k − 1 + 1, I 2 k − 1 + 2, …, I 2 k I_{2^{k-1}+1},I_{2^{k-1}+2},\ldots,I_{2^{k}} have labels ending in 1 1. Hence, such a vertex labeled m m has a single out-edge to the vertex labeled ( m − 1) / 3 (m-1)/3. But if m m is the label of I 2 k − 1 + r I_{2^{k-1}+r}, then ( m − 1) / 3 (m-1)/3 is the label of I 2 ​ r − 1 I_{2r-1}. But ( 2 k − 1 + r, 2 ​ r − 1) (2^{k-1}+r,2r-1) can be rewritten ( i, 2 ​ ( i − 2 k − 1) − 1) (i,2(i-2^{k-1})-1). This gives the result. ∎

We are now ready to prove Theorem 4.4.

###### Proof of Theorem 4.4.

Let 𝐀 k \mathbf{A}_{k} be the adjacency matrix of the presentation of 𝒞 ⁡ ( 1, N k) \mathcal{C}(1,N_{k}) constructed via our algorithm. We directly find a strictly positive eigenvector 𝐯 k {\bf v}_{k} of 𝐀 k \mathbf{A}_{k} having 𝐀 k ​ 𝐯 k T \mathbf{A}_{k}{\bf v}_{k}^{T} = ( 1 + 5 2) ​ 𝐯 k T (\frac{1+\sqrt{5}}{2}){\bf v}_{k}^{T}. Here 𝐯 k {\bf v}_{k} is a 2 k × 1 2^{k}\times 1 row vector, with v K T v_{K}^{T} its transpose, and let 𝐯 k ( j) {\bf v}_{k}^{(j)} denote its j j -th entry. The Perron-Frobenius Theorem [13, Theorem 4.2.3] then implies that α = 1 + 5 2 \alpha=\frac{1+\sqrt{5}}{2} is the Perron eigenvalue of 𝐀 k \mathbf{A}_{k}. Theorem 1.6 will then give us that

 | dim H ( 𝒞 ⁡ ( 1, N k)) = log 3 ⁡ ( 1 + 5 2). \dim_{H}(\mathcal{C}(1,N_{k}))=\log_{3}\bigg(\frac{1+\sqrt{5}}{2}\bigg). |  |

Let ϕ = 1 + 5 2 \phi=\frac{1+\sqrt{5}}{2} be the golden ratio. We define the vector 𝐯 k {\bf v}_{k} recursively as follows:

1. (1)

𝐯 1 = ( ϕ, 1) = ( ϕ 1, ϕ 0) {\bf v}_{1}=(\phi,1)=(\phi^{1},\phi^{0});

2. (2)

If 𝐯 j − 1 = ( ϕ k 1, ϕ k 2, …, ϕ k 2 j − 1) {\bf v}_{j-1}=(\phi^{k_{1}},\phi^{k_{2}},\ldots,\phi^{k_{2^{j-1}}}), then

 | 𝐯 j = ( ϕ k 1 + 1, ϕ k 2 + 1, …, ϕ k 2 j − 1 + 1, ϕ k 1, ϕ k 2, …, ϕ k 2 j − 1). {\bf v}_{j}=(\phi^{k_{1}+1},\phi^{k_{2}+1},\ldots,\phi^{k_{2^{j-1}}+1},\phi^{k_{1}},\phi^{k_{2}},\ldots,\phi^{k_{2^{j-1}}}). |  |

Note that 𝐯 j {\bf v}_{j} is obtained from 𝐯 j − 1 {\bf v}_{j-1} by adjoining ϕ ​ 𝐯 j − 1 \phi{\bf v}_{j-1} to the front of 𝐯 j {\bf v}_{j}.

We need now to check that 𝐀𝐯 k T = ϕ ​ 𝐯 k T \mathbf{A}{\bf v}_{k}^{T}=\phi{\bf v}_{k}^{T}. We will argue by induction on k k. The base case is easy. Now observe that if we write

 | 𝐀 𝐤 = ( 𝐓 𝐤 𝐁 𝐤) \bf{A}_{k}=\left(\begin{array}[]{c}T_{k}\\ B_{k}\\ \end{array}\right) |  |

for T k T_{k} and B k B_{k} each 2 k − 1 × 2 k 2^{k-1}\times 2^{k} blocks, then we have

 | B k + 1 = ( B k 0 0 B k) B_{k+1}=\left(\begin{array}[]{cc}B_{k}&0\\ 0&B_{k}\\ \end{array}\right) |  |

and

 | T k + 1 = ( T k 0 0 T k). T_{k+1}=\left(\begin{array}[]{cc}T_{k}&0\\ 0&T_{k}\\ \end{array}\right). |  |

It follows easily from this and the definition of the vectors 𝐯 k {\bf v}_{k} that if 𝐀 k ​ 𝐯 k T = ϕ ​ 𝐯 k T \mathbf{A}_{k}{\bf v}_{k}^{T}=\phi{\bf v}_{k}^{T}, then 𝐀 k + 1 ​ 𝐯 k + 1 T = ϕ ​ 𝐯 k + 1 T \mathbf{A}_{k+1}{\bf v}_{k+1}^{T}=\phi{\bf v}_{k+1}^{T}. This proves the theorem.

∎

###### Proof of Theorem 1.8.

Here (1) follows from Proposition 4.5, and (2) follows from Theorem 4.4. ∎

### 4.4. Hausdorff dimension bounds for 𝒞 ⁡ ( 1, M 1, …, M n) \mathcal{C}(1,M_{1},...,M_{n}) with M i M_{i} in families

The path set structures of each of the three infinite families are compatible with each other, as a function of k k, so that the associated 𝒞 ⁡ ( 1, M 1, …, M n) \mathcal{C}(1,M_{1},...,M_{n}) all have positive Hausdorff dimension. We treat them separately.

###### Theorem 4.7.

For the family L k = 1 2 ​ ( 3 k − 1) = ( 1 k) 3 L_{k}=\frac{1}{2}(3^{k}-1)=(1^{k})_{3}, for 1 ≤ k 1 < … < k n 1\leq k_{1}<\ldots<k_{n}, the pointed graph 𝒢 ⁡ ( 0, …, 0) \mathcal{G}(0,\ldots,0) of the path set X ( 1, L k 1, ⋯ L k m) X(1,L_{k_{1}},\cdots L_{k_{m}}) associated to 𝒞 ⁡ ( 1, L k 1, …, L k n) \mathcal{C}(1,L_{k_{1}},\ldots,L_{k_{n}}) is isomorphic to the pointed graph ( 𝒢 k n, 0) (\mathcal{G}_{k_{n}},0) presenting 𝒞 ⁡ ( 1, L k n) \mathcal{C}(1,L_{k_{n}}). In particular

 | dim H ( 𝒞 ⁡ ( 1, L k 1, …, L k n)) = dim H ( 𝒞 ⁡ ( 1, L k n)). \dim_{H}(\mathcal{C}(1,L_{k_{1}},\ldots,L_{k_{n}}))=\dim_{H}(\mathcal{C}(1,L_{k_{n}})). |  | (4.9) |

###### Proof.

The presentation ( 𝒢 k, 0) (\mathcal{G}_{k},0) of 𝒞 ⁡ ( 1, L k) \mathcal{C}(1,L_{k}) constructed with Algorithm A consists of a self-loop at the 0 0 -vertex and a cycle of length k k at the 0 0 -state. Taking in Algorithm B the label product 𝒢 k 1 ⋆ ⋯ ⋆ 𝒢 k n \mathcal{G}_{k_{1}}\star\cdots\star\mathcal{G}_{k_{n}} gives a graph 𝒢 \mathcal{G} with a self-loop at the ( 0, …, 0) (0,\ldots,0) -vertex and a cycle

 | ( 0, …, 0) \textstyle{(0,\ldots,0)\ignorespaces\ignorespaces\ignorespaces\ignorespaces} 1 \scriptstyle{1} ( 1 k 1 − 1, …, 1 k n − 1) \textstyle{(1^{k_{1}-1},\ldots,1^{k_{n}-1})\ignorespaces\ignorespaces\ignorespaces\ignorespaces} 0 \scriptstyle{0} ( 1 k 1 − 2, …, 1 k n − 2) \textstyle{(1^{k_{1}-2},\ldots,1^{k_{n}-2})\ignorespaces\ignorespaces\ignorespaces\ignorespaces} 0 \scriptstyle{0} ⋯ \textstyle{\cdots} ⋯ \textstyle{\quad\cdots\ignorespaces\ignorespaces\ignorespaces\ignorespaces} 0 \scriptstyle{0} ( 0, …, 0, 1) \textstyle{(0,\ldots,0,1)\ignorespaces\ignorespaces\ignorespaces\ignorespaces} 0 \scriptstyle{0} ( 0, …, 0). \textstyle{(0,\ldots,0).} |  |

This cycle has length k n k_{n}. We can then see that the graph 𝒢 \mathcal{G} is isomorphic to 𝒢 k n \mathcal{G}_{k_{n}} by an isomorphism sending ( 0, …, 0) (0,\ldots,0) to 0 0. ∎

We next treat multiple intersections drawn from the second family N k N_{k}.

###### Theorem 4.8.

For the family N k = 3 k + 1 = ( 10 k − 1 ​ 1) 3 N_{k}=3^{k}+1=(10^{k-1}1)_{3} the following hold.

(1) For 1 ≤ k 1 < k 2 < ⋯ < k n 1\leq k_{1}<k_{2}<\cdots<k_{n}, one has

 | dim H ( 𝒞 ⁡ ( 1, N k 1, N k 2, …, N k n)) ≥ d ​ i ​ m H ​ ( 𝒞 ⁡ ( 1, L k n + 1)) \dim_{H}(\mathcal{C}(1,N_{k_{1}},N_{k_{2}},\ldots,N_{k_{n}}))\geq dim_{H}(\mathcal{C}(1,L_{k_{n}+1})) |  | (4.10) |

Equality holds when k j = j k_{j}=j for 1 ≤ j ≤ n 1\leq j\leq n.

(2) For fixed n ≥ 1 n\geq 1, there holds

 | lim inf k → ∞ dim H ( 𝒞 ⁡ ( 1, N k, …, N k + n − 1)) ≥ 1 2 ​ ( log 3 ⁡ 2) ≈ 0.315464. \liminf_{k\rightarrow\infty}\dim_{H}(\mathcal{C}(1,N_{k},\ldots,N_{k+n-1}))\geq\frac{1}{2}(\log_{3}2)\approx 0.315464. |  | (4.11) |

In particular, Γ ⋆ ≥ 1 2 ​ ( log 3 ⁡ 2). \Gamma_{\star}\geq\frac{1}{2}(\log_{3}2).

###### Proof.

(1) It is easy to see that the set 𝒞 ⁡ ( 1, N k 1, N k 2, …, N k n) \mathcal{C}(1,N_{k_{1}},N_{k_{2}},\ldots,N_{k_{n}}) contains the set

 | Y k n:= { λ = ∑ j = 1 ∞ 3 ℓ 1 + ⋯ + ℓ j ∈ ℤ 3, 2 ¯: all ​ ℓ j ≥ k n + 1 }, Y_{k_{n}}:=\{\lambda=\sum_{j=1}^{\infty}3^{\ell_{1}+\cdots+\ell_{j}}\in{\mathbb{Z}}_{3,\bar{2}}:\,\mbox{all}~~\ell_{j}\geq k_{n}+1\}, |  |

(Here we allow finite sums, corresponding to some ℓ j = + ∞ \ell_{j}=+\infty). This fact holds by observing that if λ ∈ Y k, n \lambda\in Y_{k,n} then N k j ​ λ ∈ Σ 3, 2 ¯ N_{k_{j}}\lambda\in\Sigma_{3,\bar{2}} for 1 ≤ j ≤ n 1\leq j\leq n, because

 | N k j ​ λ = ( ∑ j = 1 ∞ 3 ℓ 1 + ⋯ + ℓ j) + ( ∑ j = 1 ∞ 3 ℓ 1 + ⋯ + ℓ j + k j) N_{k_{j}}\lambda=(\sum_{j=1}^{\infty}3^{\ell_{1}+\cdots+\ell_{j}})+(\sum_{j=1}^{\infty}3^{\ell_{1}+\cdots+\ell_{j}+k_{j}}) |  |

and the 3 3 -adic addition has no carry operations since all exponents are distinct. The set Y k n Y_{k_{n}} is a 3 3 -adic path set fractal and it is easily checked to be identical with 𝒞 ⁡ ( 1, L n k + 1) \mathcal{C}(1,L_{n_{k}+1}), using the structure of its associated graph. This proves ( 4.10). To show equality holds, one must show that allowable sequences for each of N 1, N 2, …, N n N_{1},N_{2},...,N_{n} require gaps of size at least n + 1 n+1 between each successive nonzero 3 3 -adic digit in an element of 𝒞 ⁡ ( 1, N 1, N 2, …, N n). \mathcal{C}(1,N_{1},N_{2},...,N_{n}). This can be done by induction on the current non-zero 3 3 -adic digit; we omit details.

(2) We study the symbolic dynamics of the elements of the underlying path sets in 𝒞 ⁡ ( 1, N k + j − 1) \mathcal{C}(1,N_{k+j-1}), for 1 ≤ j ≤ n 1\leq j\leq n, given in Theorem 4.4, and use this to lower bound the Hausdorff dimension.

Claim. The 3 3 -adic path set underlying 𝒞 ⁡ ( 1, N k, …, N k + n) \mathcal{C}(1,N_{k},\ldots,N_{k+n}) contains all symbol sequences which, when subdivided into successive blocks of length 2 ​ k + n 2k+n, have every such block of the form

 | ( 00 ⋯ 00 a k a k − 1 ⋯ a 3 a 2 1) 3 with each a i ∈ { 0, 1 }. (00\cdots 00a_{k}a_{k-1}\cdots a_{3}a_{2}1)_{3}\,\,\mbox{with each}\,\,a_{i}\in\{0,1\}. |  |

###### Proof of claim.

It suffices to show that all sequences split into blocks of length 2 ​ k + n 2k+n of the form ( 00 ⋯ 00 a k a k − 1 ⋯ a 3 a 2 1) 3 (00\cdots 00a_{k}a_{k-1}\cdots a_{3}a_{2}1)_{3} occur in 𝒞 ⁡ ( 1, N j) \mathcal{C}(1,N_{j}) for each k ≤ j ≤ k + n k\leq j\leq k+n, since this will imply the statement for the label product. Consider the presentation 𝒢 j \mathcal{G}_{j} of 𝒞 ⁡ ( 1, N j) \mathcal{C}(1,N_{j}) given by our algorithm. Beginning at the 0 0 -vertex, an edge labeled 1 1 takes us to the state ( 10 j − 1) 3 (10^{j-1})_{3}. From a vertex whose label ends in 0 0, one may traverse an edge with label 1 1 or 0 0. But if we are at a vertex whose labeled a ​ 0 a0, an edge labeled 0 0 takes us to a vertex labeled a a, and an edge labeled 1 1 takes us to a vertex labeled 1 ​ a 1a (this is specific to the case of N j N_{j}). In other words, we apply the truncated shift map to our vertex label and either concatenate with 1 1 on the left or not. It follows that from the vertex ( 10 j − 1) 3 (10^{j-1})_{3} the next ( j − 1) (j-1) edges traversed may be labeled either 0 0 or 1 1.

At this point the initial 1 1 from ( 10 j − 1) 3 (10^{j-1})_{3} has moved to the far right of our vertex label. Therefore, our choice is restricted: we must traverse an edge labeled 0 0. Since our vertex label, whatever it is, consists of only 0 0 ’s and 1 1 ’s, we can in any case traverse j j or more consecutive edges labeled 0 0 to get back to the 0 0 -vertex. Thus, first traversing an edge labeled 1 1, then traversing edges labeled 0 0 or 1 1 freely for the next ( k − 1) (k-1) -steps, then traversing k + n k+n edges labeled 0 0 and returning to the 0 0 -vertex, is possible in the graph 𝒢 j \mathcal{G}_{j} for each k ≤ j ≤ k + n k\leq j\leq k+n. It follows that all sequences of the desired form are in each 𝒞 ⁡ ( 1, N j) \mathcal{C}(1,N_{j}), and hence in 𝒞 ⁡ ( 1, N k ​ …, N k + n) \mathcal{C}(1,N_{k}\ldots,N_{k+n}), proving the claim. ∎

With this claim in hand, we see that each block of size ( 2 ​ k + n CLOSE (2k+n contains at least 2 k − 2 2^{k-2} admissible ( 2 ​ k + n) (2k+n) -blocks in 𝒞 ⁡ ( 1, N k, …, N k + n) \mathcal{C}(1,N_{k},\ldots,N_{k+n}). We conclude that the maximum eigenvalue β n, k \beta_{n,k} of the adjacency matrix of the graph 𝒢 n, k \mathcal{G}_{n,k} of 𝒞 ⁡ ( 1, N k, N k + 1, ⋯, N k + n − 1) \mathcal{C}(1,N_{k},N_{k+1},\cdots,N_{k+n-1}) must satisfy ( β n, k) 2 ​ n + k ≥ 2 k − 2. (\beta_{n,k})^{2n+k}\geq 2^{k-2}. This yields

 | β n, k ≥ 2 k − 2 k + 2 ​ n. \beta_{n,k}\geq 2^{\frac{k-2}{k+2n}}. |  |

and hence lim inf k → ∞ β n, k ≥ 2 \liminf_{k\to\infty}\beta_{n,k}\geq\sqrt{2}. The Hausdorff dimension formula in Proposition 2.2 then yields

 | lim sup k → ∞ dim H ( 𝒞 ⁡ ( 1, N k, …, N k + n)) ≥ lim sup k → ∞ log 3 ⁡ β n, k ≥ 1 2 ​ log 3 ​ 2. \limsup_{k\rightarrow\infty}\dim_{H}\big(\mathcal{C}(1,N_{k},\ldots,N_{k+n})\big)\geq\limsup_{k\rightarrow\infty}\log_{3}\beta_{n,k}\geq\frac{1}{2}\log_{3}2. |  | (4.12) |

as asserted.

The lower bound Γ ⋆ ≥ 1 2 ​ log 3 ​ 2 \Gamma_{\star}\geq\frac{1}{2}\log_{3}2 follows immediately from this bound, see ( 1.15). ∎

## 5. Applications

We give several applications to improving bounds for the Hausdorff dimension of various sets.

### 5.1. Hausdorff dimension of the generalized exceptional set ℰ ⋆ ​ ( ℤ 3) \mathcal{E}_{\star}(\mathbb{Z}_{3})

Theorem 4.8 (2) shows that there are arbitrarily large families 𝒞 ⁡ ( 1, N k 1, …, N k n) \mathcal{C}(1,N_{k_{1}},...,N_{k_{n}}) having Hausdorff dimension uniformly bounded below. If one properly restricts the choice of the N k j N_{k_{j}} then one can obtain an infinite set in this way, as was pointed out to us by Artem Bolshakov. It yields a nontrivial lower bound on the Hausdorff dimension of the generalized exceptional set.

###### Theorem 5.1.

(Lower Bound for Generalized Exceptional Set)

(1) The subset Y Y of the 3 3 -adic Cantor set Σ 3, 2 ¯ \Sigma_{3,\bar{2}} given by

 | Y:= { λ:= ∑ j = 0 ∞ a j 3 j: all a 2 ​ k ∈ { 0, 1 }, all a 2 ​ k + 1 = 0 } ⊂ ℤ 3. Y:=\{\lambda:=\sum_{j=0}^{\infty}a_{j}3^{j}:\mbox{all}~~a_{2k}\in\{0,1\},\,\,\mbox{all}\,\,a_{2k+1}=0\}\subset\mathbb{Z}_{3}. |  |

is a 3 3 -adic path set fractal having dim H ( Y) = 1 2 ​ log 3 ​ 2 ≈ 0.315464 \dim_{H}(Y)=\frac{1}{2}\log_{3}2\approx 0.315464. This set satisfies

 | Y ⊂ 𝒞 ⁡ ( 1, N 2 ​ k + 1), for all ​ k ≥ 0, Y\subset\mathcal{C}(1,N_{2k+1}),\,\,\mbox{ for all}\,\,k\geq 0, |  |

where N k = 3 k + 1 N_{k}=3^{k}+1, and in consequence

 | Y ⊆ ⋂ k = 1 ∞ 𝒞 ⁡ ( 1, N 2 ​ k + 1). Y\subseteq\bigcap_{k=1}^{\infty}\mathcal{C}(1,N_{2k+1}). |  |

(2) One has

 | dim H ( { λ ∈ Σ 3, 2 ¯: N 2 ​ k + 1 ​ λ ∈ Σ 3, 2 ¯ ​ for all ​ k ≥ 0 }) ≥ dim H ( Y) = 1 2 ​ log 3 ​ 2. \dim_{H}\Big(\{\lambda\in\Sigma_{3,\bar{2}}:\,\,N_{2k+1}\lambda\in\Sigma_{3,\bar{2}}\,\,\mbox{for all}\,k\geq 0\}\Big)\geq\dim_{H}(Y)=\frac{1}{2}\log_{3}2. |  | (5.1) |

Therefore

 | dim H ( ℰ ∗) ≥ 1 2 ​ log 3 ​ 2 = 0.315464. \dim_{H}(\mathcal{E}_{\ast})\geq\frac{1}{2}\log_{3}2=0.315464. |  | (5.2) |

###### Proof.

(1) The 3 3 -adic path set fractal property of Y ⊂ Σ 3, 2 ¯ Y\subset\Sigma_{3,\bar{2}} is easily established, since the underlying graph of its symbolic dynamics is pictured in Figure 5.1. The Perron eigenvalue of its adjacency matrix is 2 \sqrt{2}, and its Hausdorff dimension is 1 2 ​ log 3 ​ 2 \frac{1}{2}\log_{3}2 by Proposition 2.2.

-125,-20)(125,30) q11 q10q00
FIGURE 5.1. Presentation of Y Y.

The elements of Y Y can be rewritten in the form λ = ∑ j = 0 ∞ b 2 ​ j ​ 3 2 ​ j, \lambda=\sum_{j=0}^{\infty}b_{2j}3^{2j}, with all b 2 ​ j ∈ { 0, 1 } b_{2j}\in\{0,1\}. We then have

 | N 2 ​ k + 1 ​ λ = ∑ j = 0 ∞ b 2 ​ j ​ 3 2 ​ j + ∑ j = 0 ∞ b 2 ​ j ​ 3 2 ​ j + 2 ​ k + 1 ∈ Σ 3, 2 ¯, N_{2k+1}\lambda=\sum_{j=0}^{\infty}b_{2j}3^{2j}+\sum_{j=0}^{\infty}b_{2j}3^{2j+2k+1}\in\Sigma_{3,\bar{2}}, |  |

and the inclusion in the Cantor set Σ 3, 2 ¯ \Sigma_{3,\bar{2}} follows because the sets of 3 3 -adic exponents in the two sums on the right side are disjoint, so there are no carry operations in combining them under 3 3 -adic addition. This establishes that Y ⊂ 𝒞 ⁡ ( 1, N 2 ​ k + 1) Y\subset\mathcal{C}(1,N_{2k+1}).

(2) All elements λ ∈ Y \lambda\in Y have N 2 ​ k + 1 ​ λ ∈ Σ 3, 2 ¯ N_{2k+1}\lambda\in\Sigma_{3,\bar{2}} for all k ≥ 1 k\geq 1. Thus

 | Y ⊂ { λ ∈ Σ 3, 2 ¯: N 2 ​ k + 1 ​ λ ∈ Σ 3, 2 ¯ ​ for all ​ k ≥ 1 }. Y\subset\{\lambda\in\Sigma_{3,\bar{2}}:\,\,N_{2k+1}\lambda\in\Sigma_{3,\bar{2}}\,\,\mbox{for all}\,k\geq 1\}. |  |

The result ( 5.1) follows, from which ( 5.2) is immediate. ∎

Theorem 1.9 is included as part (2) of this result.

### 5.2. Bounds for approximations to the exceptional set ℰ ⁡ ( ℤ 3) \mathcal{E}(\mathbb{Z}_{3})

We conclude with numerical results concerning Hausdorff dimensions of the upper approximation sets ℰ ( k) ​ ( ℤ 3) \mathcal{E}^{(k)}(\mathbb{Z}_{3}) to the exceptional set ℰ ⁡ ( ℤ 3) \mathcal{E}(\mathbb{Z}_{3}). Recall that the only powers of 2 2 that are known to have ternary expansions that omit the digit 2 2 are 2 0 = 1 = ( 1) 3, 2 2 = 4 = ( 11) 3 2^{0}=1=(1)_{3},2^{2}=4=(11)_{3}, and 2 8 = 256 = ( 10111) 3 2^{8}=256=(10111)_{3}. In contrast 2 4 = 16 = ( 121) 3 2^{4}=16=(121)_{3} and 2 6 = 64 = ( 2101) 3 2^{6}=64=(2101)_{3}.

We begin with empirical results about the sets 𝒞 ⁡ ( 1, 2 m 1, …, 2 m n) \mathcal{C}(1,2^{m_{1}},\ldots,2^{m_{n}}) obtained via Algorithm A. Here we note the necessary condition 2 2 ​ n ≡ 1 ( mod 3) 2^{2n}\equiv 1~(\bmod\,3) for positive Hausdorff dimension.

Set | Hausdorff dimension |

𝒞 ⁡ ( 1, 2 2) \mathcal{C}(1,2^{2}) | 0. | 438018 |

𝒞 ⁡ ( 1, 2 4) \mathcal{C}(1,2^{4}) | 0. | 255960 |

𝒞 ⁡ ( 1, 2 6) \mathcal{C}(1,2^{6}) | 0. | 278002 |

𝒞 ⁡ ( 1, 2 8) \mathcal{C}(1,2^{8}) | 0. | 287416 |

𝒞 ⁡ ( 1, 2 10) \mathcal{C}(1,2^{10}) | 0. | 215201 |

𝒞 ⁡ ( 1, 2 12) \mathcal{C}(1,2^{12}) | 0. | 244002 |

𝒞 ⁡ ( 1, 2 14) \mathcal{C}(1,2^{14}) | 0. | 267112 |

𝒞 ⁡ ( 1, 2 2, 2 4) \mathcal{C}(1,2^{2},2^{4}) | 0. |  |

𝒞 ⁡ ( 1, 2 2, 2 6) \mathcal{C}(1,2^{2},2^{6}) | 0. |  |

𝒞 ⁡ ( 1, 2 2, 2 8) \mathcal{C}(1,2^{2},2^{8}) | 0. | 228392 |

𝒞 ⁡ ( 1, 2 2, 2 10) \mathcal{C}(1,2^{2},2^{10}) | 0. |  |

𝒞 ⁡ ( 1, 2 4, 2 6) \mathcal{C}(1,2^{4},2^{6}) | 0. |  |

𝒞 ⁡ ( 1, 2 4, 2 8) \mathcal{C}(1,2^{4},2^{8}) | 0. |  |

𝒞 ⁡ ( 1, 2 4, 2 10) \mathcal{C}(1,2^{4},2^{10}) | 0. |  |

𝒞 ⁡ ( 1, 2 6, 2 8) \mathcal{C}(1,2^{6},2^{8}) | 0. |  |

𝒞 ⁡ ( 1, 2 6, 2 10) \mathcal{C}(1,2^{6},2^{10}) | 0. |  |

𝒞 ⁡ ( 1, 2 8, 2 10) \mathcal{C}(1,2^{8},2^{10}) | 0. |  |

𝒞 ⁡ ( 1, 2 2, 2 8, 2 12) \mathcal{C}(1,2^{2},2^{8},2^{12}) | 0. |  |

𝒞 ⁡ ( 1, 2 2, 2 8, 2 14) \mathcal{C}(1,2^{2},2^{8},2^{14}) | 0. |  |

𝒞 ⁡ ( 1, 2 2, 2 8, 2 16) \mathcal{C}(1,2^{2},2^{8},2^{16}) | 0. |  |

TABLE 5.2. Hausdorff dimension of 𝒞 ⁡ ( 1, 2 m 1, …, 2 m k) \mathcal{C}(1,2^{m_{1}},\ldots,2^{m_{k}}) (to six decimal places)

###### Theorem 5.2.

The following bounds hold for sets ℰ ( k) ​ ( ℤ 3) \mathcal{E}^{(k)}(\mathbb{Z}_{3}).

 | dim H ( ℰ ( 2) ​ ( ℤ 3)) \displaystyle\dim_{H}(\mathcal{E}^{(2)}(\mathbb{Z}_{3})) | ≥ \displaystyle\geq | log 3 ⁡ ( 1 + 5 2) ≈ 0.438018, \displaystyle\log_{3}\bigg(\frac{1+\sqrt{5}}{2}\bigg)\approx 0.438018, |  |

 | dim H ( ℰ ( 3) ​ ( ℤ 3)) \displaystyle\dim_{H}(\mathcal{E}^{(3)}(\mathbb{Z}_{3})) | ≥ \displaystyle\geq | log 3 ⁡ β 1 ≈ 0.228392, \displaystyle\log_{3}\beta_{1}\approx 0.228392, |  |

where β 1 ≈ 1.28520 \beta_{1}\approx 1.28520 is a root of λ 6 − λ 5 − 1 = 0 \lambda^{6}-\lambda^{5}-1=0.

###### Proof.

We have

 | dim H ( ℰ ( 2) ​ ( ℤ 3)) \displaystyle\dim_{H}(\mathcal{E}^{(2)}(\mathbb{Z}_{3})) | = \displaystyle= | sup 0 ≤ m 1 < m 2 dim H ( 𝒞 ⁡ ( 2 m 1, 2 m 2)) \displaystyle\sup_{0\leq m_{1}<m_{2}}\dim_{H}(\mathcal{C}(2^{m_{1}},2^{m_{2}})) |  |

 |  | ≥ \displaystyle\geq | dim H ( 𝒞 ⁡ ( 2 0, 2 2)) = log 3 ⁡ ( 1 + 5 2). \displaystyle\dim_{H}(\mathcal{C}(2^{0},2^{2}))=\log_{3}\left(\frac{1+\sqrt{5}}{2}\right). |  |

The bound for N 1 = 2 2 = ( 11) 3 N_{1}=2^{2}=(11)_{3} follows from Theorem 1.8, taking k = 1 k=1.

We also have

 | dim H ( ℰ ( 3) ​ ( ℤ 3)) \displaystyle\dim_{H}(\mathcal{E}^{(3)}(\mathbb{Z}_{3})) | = \displaystyle= | sup 0 ≤ m 1 < m 2 < m 3 dim H ( 𝒞 ⁡ ( 2 m 1, 2 m 2, 2 m 3)) \displaystyle\sup_{0\leq m_{1}<m_{2}<m_{3}}\dim_{H}(\mathcal{C}(2^{m_{1}},2^{m_{2}},2^{m_{3}})) |  |

 |  | ≥ \displaystyle\geq | dim H ( 𝒞 ⁡ ( 2 0, 2 2, 2 8)) = log 3 ⁡ β 1 ≈ 0.228392 \displaystyle\dim_{H}(\mathcal{C}(2^{0},2^{2},2^{8}))=\log_{3}\beta_{1}\approx 0.228392 |  |

where β 1 ≈ 1.28520 ​ … \beta_{1}\approx 1.28520... is a root of λ 6 − λ 5 − 1 = 0. \lambda^{6}-\lambda^{5}-1=0. ∎

It is unclear whether dim H ( ℰ ( k) ​ ( ℤ 3)) \dim_{H}(\mathcal{E}^{(k)}(\mathbb{Z}_{3})) is positive for any k ≥ 4 k\geq 4. Currently 𝒞 ⁡ ( 1, 2 2, 2 8) \mathcal{C}(1,2^{2},2^{8}) is the only component of ℰ ( 3) ​ ( ℤ 3) \mathcal{E}^{(3)}(\mathbb{Z}_{3}) known to have positive Hausdorff dimension. At present we do not know of any set 𝒞 ⁡ ( 1, 2 m 1, 2 m 2, 2 m 3) \mathcal{C}(1,2^{m_{1}},2^{m_{2}},2^{m_{3}}) that has positive Hausdorff dimension.

### Acknowledgments

The authors thank Artem Bolshakov for making the key observation that Theorem 5.1 should hold. W. Abram acknowledges the support of an NSF Graduate Research Fellowship and of the University of Michigan, where this work was carried out.

## References

- [1] W. Abram and J. C. Lagarias, *Path sets and their symbolic dynamics,*eprint arXiv:1207:5004
- [2] W. Abram and J. C. Lagarias, *p p -Adic path set fractals and arithmetic,*eprint arXiv:1210:2478
- [3] W. Abram, A. Bolshakov and J. C. Lagarias, *Intersections of multiplicative translates of 3 3 -adic Cantor sets, Part II*, in preparation.
- [4] R.L. Adler and B. Marcus, Topological entropy and equivalence of dynamical systems, Memoirs of the American Mathematical Society, Volume 20, No. 219, AMS: Providence, RI 1979.
- [5] J.P. Alloche and J. O. Shallit, Automatic Sequences: Theory, Applications, Generalizations, Cambridge University Press: Cambridge 2003.
- [6] M. Boyle and D. Handelman, *The spectrum of nonnegative matrices via symbolic dynamics*, Ann. Math. 133 (1991), no. 2, 249–316.
- [7] G. Edgar, *Measure, topology and fractal geometry, Second Edition*Springer-Verlag: New York 2008.
- [8] P. Erdős, *Some unconventional problems in number theory*, Math. Mag. 52 (1979), 67-70.
- [9] E. de Faria and C. Tresser, *On Sloane’s persistence problem,*arXiv:1307.1188, July 2013.
- [10] A. Katok and B. Hasselblatt, Introduction to the Modern Theory of Dynamical Systems (Cambridge University Press, New York, 1995).
- [11] J.C. Lagarias, *Ternary expansions of powers of 2*, J. London Math. Soc.(2) 79 (2009), 562-588.
- [12] D. Lind, *The entropies of topological Markov shifts and a related class of algebraic integers*, Ergod. Th. Dyn. Sys. 4 (1984), no. 2, 283–300.
- [13] D. Lind and B. Marcus, An Introduction to Symbolic Dynamics and Coding, (Cambridge University Press, New York, 1995).
- [14] K. Mahler, Lectures on diophantine approximations, Part I. g g -adic numbers and Roth’s theorem, Prepared from notes of R. P. Bambah, University of Notre Dame Press, Notre Dame IN 1961.
- [15] R. D. Mauldin and M. Urbański, *Graph directed Markov systems. Geometry and dynamics of limit sets,*Cambridge Tracts in Mathematics No. 148, Cambridge Univ. Press: Cambridge 2003.
- [16] R. D. Mauldin and S. C. Williams, *On the Hausdorff dimension of some graphs,*Trans. Amer. Math. Soc. 298 (1986), no. 2, 793–803.
- [17] R.D. Mauldin and S.C. Williams, *Hausdorff Dimension of Graph Directed Constructions*, Transactions of the American Mathematical Society, 309, No. 2 (1988) , 811-829.
- [18] H. G. Senge and E. Straus, *P.V. numbers and sets of multiplicity,*Periodica Math. Hung. 3 (1973), 93–100.
- [19] J.G. Simonsen, *On the Computabillity of the Topological Entropy of Subshifts*, Discrete Mathematics and Theoretical Computer Science, 8 (2006), 83-96.
- [20] C. L. Stewart, *On the Representation of an Integer in two Different Bases,*J. Reine Angew. Math., 319 (1980), 63–72.
- [21] B. Weiss, *Subshifts of finite type and sofic systems,*Monatshefte für Math. 77 (1973), 462–474.
- [22] S. Williams, *A sofic system which is not spectrally of finite type,*Ergod. Th. Dyn. Sys. 8 (1988), 483–490.

[◄][3][image: ar5iv homepage] [4]
[Feeling lucky?][5] [6]
[Conversion report][7]
[Report an issue][8]
[View original on arXiv][9] [►][10]


## Links

[1]: mailto:wabram@hillsdale.edu
[2]: mailto:lagarias@umich.edu
[3]: /html/1308.3132
[4]: /
[5]: /feeling_lucky
[6]: /land_of_honey_and_milk
[7]: /log/1308.3133
[8]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1308.3133
[9]: https://arxiv.org/abs/1308.3133
[10]: /html/1308.3134
