<!-- source: https://arxiv.org/html/2104.06491v2 | converted from HTML -->

p -adic Ducci Sequences: a short note

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2104.06491v2 [math.NT] 20 Dec 2021

# p p -adic Ducci Sequences: a short note

Piero Giacomelli Email: [pgiacomelli@fidiapharma.it][3] Affiliation: Fidia Farmaceutici S.p.A.

August 11, 2026

###### Abstract

In this short note we formalized the definition for the Ducci operator D D in the context of the p p -adic field ℚ p \mathbb{Q}_{p} as a natural extension of the classical one. Moreover we will describe the behavior of the operator and will provide some simple results as a counterpart to the classical one.

###### pacs

03.67.Pp, 03.67.Lx

## I Introduction

Ducci sequences were first introduced in 1937 Ciamberlini and Marengoni 1937. Their attractiveness is due to the easy definition and to the interesting properties. In the last years they regain attention and different questions regarding this sequences and the behaviour of the Ducci operator associate with them rise attentions. From the basic definitions some research have been done on finding some extension on general abelian groups , on reals and on cyclotomic fields Breuer 2010. Some study tried to extend the definition to an higher dimension case Breuer 2010. Some interesting connection between Ducci sequence and cellular automata Mendivil and Patterson 2012. Surprisingly, being that the Ducci operator that define the Ducci sequence is based on absolute value norm, there have been no study at all on the Ducci sequences defined by the Ducci operator using the p p -adic norm. In these paper we introduced the p p -adic Ducci operator and we define the p p -adic Ducci sequences on non-Archimedean valued field ℚ p \mathbb{Q}_{p}. Moreover we will describe the behavior of the p p -adic Ducci operator like in the case of the classical Ducci sequences.

## II Previous results

Let n ∈ ℕ n\in\mathbb{N}, we define the Ducci operator D D as the operator that maps ℤ N \mathbb{Z}^{N} into itself as follows:

 | D: ℤ n \displaystyle D:\mathbb{Z}^{n} | → ℤ n \displaystyle\rightarrow\mathbb{Z}^{n} |  |

 | ( a 1, a 2, …, a n) \displaystyle(a_{1},a_{2},\dots,a_{n}) | ↦ D ⁡ ( a 1, a 2, …, a n) = \displaystyle\mapsto D(a_{1},a_{2},\dots,a_{n})= |  |

 |  | ( | a 1 − a 2 |, | a 2 − a 3 |, …, | a n − a 1 |) \displaystyle(|a_{1}-a_{2}|,|a_{2}-a_{3}|,\dots,|a_{n}-a_{1}|) |  |

Let k ∈ ℕ k\in\mathbb{N}, we also define that D k D^{k} is the Ducci operator applied k k times. This brings to the following definition for the interation of the Ducci operator The Ducci sequences are defined as the recurrent sequences with seed α = ( a 1, a 2, …, a n) \alpha=(a_{1},a_{2},\dots,a_{n}) and the following terms calculated by applying the Ducci operator k k times.

 | α ( k) = { α ( 0) = α if ​ k = 0 α ( k) = D k ​ ( α) if ​ k > 0 \alpha_{(k)}=\left\{\begin{array}[]{ll}\alpha_{(0)}=\alpha&\mbox{if }k=0\\ \alpha_{(k)}=D^{k}(\alpha)&\mbox{if }k>0\end{array}\right. |  |

The previous literature focused on describing the behaviour of the Ducci sequences as k ↦ ∞ k\mapsto\infty. It has been proved that the Ducci sequences are ultimely periodic, so that there exists a number m ∈ ℕ m\in\mathbb{N} such that D k ​ ( α) = D k + m ​ ( α) D^{k}(\alpha)=D^{k+m}(\alpha). The number m m is called the lenght of the cycle.

Moreover it has been proved that if n n is a power of 2 2 then there exists a value K K such that D k ​ ( α) = 0 D^{k}(\alpha)=0 for every k ≥ K k\geq K

In these note we are interested on find if the same results holds one we redefine the Ducci operator in the context of the non-archimedian setting using the p p -adic valuation in the definition of the Ducci operator.

## III p p -adic Ducci operator and sequences

Let p p be a prime we are now ready to first define the p p -adic Ducci operator. The definition of the p p -adic ducci Operator slitlghy differ from the absolute value because the result of the p p -adic evaluation are always a integer power of p p. Let us starting by defining the p p -adic Ducci operator D p D_{p}.

###### Definition III.1.

Let P = { 0 } ∪ { p i: i ∈ ℤ } P=\{0\}\cup\{p^{i}:i\in\mathbb{Z}\}. We can define the p p -adic Ducci operator the following map.

 | D p: ℚ 𝕡 n \displaystyle D_{p}:\mathbb{Q_{p}}^{n} | → P n ⊆ ℚ 𝕡 n \displaystyle\rightarrow P^{n}\subseteq\mathbb{Q_{p}}^{n} |  |

 | ( a 1, a 2, …, a n) \displaystyle(a_{1},a_{2},\dots,a_{n}) | ↦ D p ​ ( a 1, a 2, …, a n) = \displaystyle\mapsto D_{p}(a_{1},a_{2},\dots,a_{n})= |  |

 |  | ( | a 1 − a 2 | p, | a 2 − a 3 | p, …, | a n − a 1 | p). \displaystyle(|a_{1}-a_{2}|_{p},|a_{2}-a_{3}|_{p},\dots,|a_{n}-a_{1}|_{p}). |  |

Where if x ∈ ℚ p x\in\mathbb{Q}_{p} then | x | p = 1 p o ​ r ​ d p ​ ( x) |x|_{p}=\frac{1}{p^{ord_{p}(x)}} being o r d p ( x) = m a x { m: p m | x } ord_{p}(x)=max\{m:p^{m}|x\} (i.e. o ​ r ​ d p ​ ( x) ord_{p}(x) is the maximum power of p p that divide x x).

From this definition if follows naturally the following one:

###### Definition III.2.

The p p -adic Ducci sequences are the ones generated by α \alpha and applying the p p -adic Ducci operator k k -times with k ∈ ℕ k\in\mathbb{N}, using the previous formalism if α = \alpha=

 | α p ( k) = { α p ( 0) = α p if ​ k = 0 α p ( k) = D p k ​ ( α) if ​ k > 0 \alpha^{(k)}_{p}=\left\{\begin{array}[]{ll}\alpha^{(0)}_{p}=\alpha_{p}&\mbox{if }k=0\\ \alpha^{(k)}_{p}=D_{p}^{k}(\alpha)&\mbox{if }k>0\end{array}\right. |  |

We are interested in showing wich results holds in the context of the ultrametric inequality respect the context of the absolute value. In the classical settings the following simple hold.

- •

D p ​ ( 0) = 0 D_{p}(0)=0, where 0 = { 0, 0, …, 0 } 0=\{0,0,\dots,0\}

- •

∀ a ∈ ℚ p \forall a\in\mathbb{Q}_{p}, D p ​ ( a ​ α) = a ​ D p ​ ( α) D_{p}(a\alpha)=aD_{p}(\alpha)

the followings are true for the p p -adic Ducci operator D p D_{p} as well as for the Ducci operator D D:

- •

D p ​ ( 0) = 0 D_{p}(0)=0, where 0 = { 0, 0, …, 0 } 0=\{0,0,\dots,0\}

- •

∀ a ∈ ℚ 𝕡 \forall a\in\mathbb{Q_{p}}, D p ​ ( a ​ α) = a ​ D p ​ ( α) D_{p}(a\alpha)=aD_{p}(\alpha)

The Ducci sequences are periodic being that for every sequence α ( k) = D k ( α) \alpha^{(}k)=D^{k}(\alpha) there exists two natural indexes r, s r,s such that α ( r) = α ( r + s) \alpha^{(r)}=\alpha^{(r+s)}. The number r − s = c r-s=c is called the lenght of the cycle. It is easy to see that in the classical context every constant sequence converge to the zeros sequence with cycle of lenght c = 1 c=1. One difference respect to the classical setting is that if the starting seed of the p p -adic Ducci sequence α ( 0) \alpha^{(0)} is in the p p -adic integer ring ℤ p \mathbb{Z}_{p} then being that α ( k) ∈ { 0, 1 } n, k > 1 \alpha^{(k)}\in\{0,1\}^{n},k>1 and that | a i − a i + 1 | p = m ​ a ​ x ​ ( | 0 | p, | ± 1 | p) = m ​ a ​ x ​ ( | 0 | p, | 0 | p) = 0 |a_{i}-a_{i+1}|_{p}=max(|0|_{p},|\pm{1}|_{p})=max(|0|_{p},|0|_{p})=0 we have

 | lim k → + ∞ D p ( k) = 0 \lim_{k\rightarrow+\infty}D_{p}^{(k)}=0 |  |

so an easy lemma is the following one

###### Lemma 1.

If α p ( 0) ∈ ℤ p \alpha_{p}^{(0)}\in\mathbb{Z}_{p} the ducci sequences generated by this seed is the null sequence with period 1 1.

###### Lemma 2.

Let

 | { α p ( k) } 0 ∞ \displaystyle\{\alpha^{(k)}_{p}\}_{0}^{\infty} | = \displaystyle= |  |

 |  | = { α p ( 0), α p ( 1), …, α p ( k), … } \displaystyle=\{\alpha^{(0)}_{p},\alpha^{(1)}_{p},\dots,\alpha^{(k)}_{p},\dots\} |  |

 |  | = { α, D p ( α), \displaystyle=\{\alpha,D_{p}(\alpha), |  |

 | D p 2 ​ ( α) \displaystyle D^{2}_{p}(\alpha) | = D p ​ ( D p ​ ( α), … CLOSE, \displaystyle=D_{p}(D_{p}(\alpha),\dots, |  |

 |  | D p k ( α), … } \displaystyle D_{p}^{k}(\alpha),\dots\} |  |

a p p -adic Ducci sequence. The sequence is ultimely periodic.

###### Proof.

We first notice that apart from the first term α ( 0) \alpha^{(0)} every term of the whole sequence { α ( k) } 0 ∞ \{\alpha^{(k)}\}_{0}^{\infty} is in P n P^{n}. So let us consider a generic term a i ( k) a_{i}^{(}k) of the p p -adic ducci sequence, we can notice that by the ultrametric inequality in x, y ∈ P x,y\in P then

 | | x − y | p = { m ​ a ​ x ​ ( | x | p, | y | p) if ​ x ≠ y 0 if ​ x = y |x-y|_{p}=\left\{\begin{array}[]{ll}max(|x|_{p},|y|_{p})&\mbox{if }x\neq y\\ 0&\mbox{if }x=y\end{array}\right. |  |

so very term a i ( k) a_{i}^{(k)} of the n-uple α ( k) \alpha^{(k)} is bounded between p − ν ≤ a i ( k) ≤ p ν p^{-\nu}\leq a_{i}^{(k)}\leq p^{\nu} where ν = m ​ a ​ x ​ ( | a i ( 0) | p) \nu=max(|a_{i}^{(0)}|_{p}). This means that there are only a finite number of possible values for α ( k) \alpha^{(k)} from k > 0 k>0 in P n P^{n}. Then by the Pigeonhole principle Ajtai 1994 there must be some r, s ∈ ℕ, r, s > 0 r,s\in\mathbb{N},r,s>0 so that α ( r) = α ( r + s) \alpha^{(r)}=\alpha^{(r+s)}. But then

 | α ( r + s + i ​ h) = α ( r + i) \alpha^{(r+s+ih)}=\alpha^{(r+i)} |  |

for every 0 ≤ i < s 0\leq i<s and h ∈ ℕ, h > 0 h\in\mathbb{N},h>0.

∎

The first interesting result with the classical Ducci operator is the fact that if α = α ⁡ ( 0) = { a 1, a 2, …, a n } \alpha=\alpha(0)=\{a_{1},a_{2},\dots,a_{n}\} contains a number of terms that is a power of 2 2 then there exists a index K ∈ ℕ K\in\mathbb{N} such that α ( k) = 0 \alpha^{(k)}=0.

This follow from the observation that for every term a ( k) a^{(k)} then | a i − a i + 1 | p ≡ a i + a i + 1 mod 2 |a_{i}-a_{i+1}|_{p}\equiv a_{i}+a_{i+1}\mod 2.

If a i ∈ P n a_{i}\in P^{n} then up to rearrange the indexes

 | | a i − a i + 1 | p \displaystyle|a_{i}-a_{i+1}|_{p} | = | p α − p β | p \displaystyle=|p^{\alpha}-p^{\beta}|_{p} |  |

 |  | ≤ m ​ a ​ x ​ ( | p α | p, | p β | p) \displaystyle\leq max(|p^{\alpha}|_{p},|p^{\beta}|_{p}) |  |

 |  | = m ​ i ​ n ​ ( α, β) \displaystyle=min(\alpha,\beta) |  |

this means that in general | a i − a i + 1 | ≡ ​ | a i + a i + 1 | mod 2 |a_{i}-a_{i+1}|_{\equiv}|a_{i}+a_{i+1}|\mod{2} and so the study of the p-adic Ducci sequences reduce to the study of the period in 𝔽 2 n \mathbb{F}^{n}_{2}. In particular the proof of section 3 in Ehrlich 1990 works without modification. So for example this means that in n n is a power of 2 2 then for every p-adic Ducci sequence { α p ( k) } \{\alpha^{(k)}_{p}\} there exist a K ≥ 0 K\geq 0 such that { α p ( k) } = 0 \{\alpha^{(k)}_{p}\}=0 for every k > K k>K.

## References

- Ciamberlini and Marengoni (1937) C. Ciamberlini and A. Marengoni, Periodico di Mathematiche 17, 25 (1937).
- Breuer (2010) F. Breuer, Journal of Difference Equations and Applications 16, 847 (2010).
- Mendivil and Patterson (2012) F. Mendivil and D. Patterson, The Rocky Mountain Journal of Mathematics , 695 (2012).
- Ajtai (1994) M. Ajtai, Combinatorica 14, 417 (1994).
- Ehrlich (1990) A. Ehrlich, Fibonacci Quart 28, 302 (1990).


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:pgiacomelli@fidiapharma.it
