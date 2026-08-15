<!-- source: https://arxiv.org/html/2503.04182v1 | converted from HTML -->

Ducci Matrices in p -adic Context

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2503.04182v1 [math.NT] 06 Mar 2025

# Ducci Matrices in p p -adic Context

Piero Giacomelli Email: [pgiacome@gmail.com][3]

###### Abstract

In this paper, we mutuate the concept of Ducci matrices to the p p -adic setting, generalizing the classical Ducci sequences to the framework of p p -adic numbers. The classical Ducci operator, which iteratively computes the absolute differences of neighboring elements in a sequence or matrix, is redefined using the p p -adic absolute value | ⋅ | p |\cdot|_{p}. We investigate the dynamics of p p -adic Ducci sequences for matrices over ℚ p \mathbb{Q}_{p}, focusing on their convergence and periodicity properties.

Enrico Ducci an italian mathematician in 1930 [1] observed a singular property of the following map

 | δ: \displaystyle\delta: | ℕ ⟶ ℕ \displaystyle\mathbb{N}\longrightarrow\mathbb{N} |  |

 | ( x 1, x 2, x 3, x 4) \displaystyle(x_{1},x_{2},x_{3},x_{4}) | ↦ ( | x 1 − x 2 |, | x 2 − x 3 |, | x 3 − x 4 |, | x 4 − x 1 |) \displaystyle\mapsto(|x_{1}-x_{2}|,|x_{2}-x_{3}|,|x_{3}-x_{4}|,|x_{4}-x_{1}|) |  |

iterated with itself always lead to the null t-uple (0,0,0,0). The sequence:

 | x, δ ⁡ ( x), δ 2 ​ ( x) = δ ⁡ ( δ ⁡ ( x)), δ 3 ​ ( x) = δ ⁡ ( δ ⁡ ( δ ⁡ ( x))) x,\delta(x),\delta^{2}(x)=\delta(\delta(x)),\delta^{3}(x)=\delta(\delta(\delta(x))) |  |

was defined as the Ducci sequence of x = ( x 1, x 2, x 3, x 4) x=(x_{1},x_{2},x_{3},_{x}4). Eighty papers after in 2020 Clausing [2] defined a wider class of maps of with the Ducci sequence is only a particular case. Meanwhile, in a short note Giacomelli introduced the p p -adic Ducci operator D p D_{p} equivalent of the Ducci operator D D, but with the valuation norm | | ˙ p |\dot{|}_{p}. In this paper we extend the Ducci matrices in the non-archimedian field ℚ p \mathbb{Q}_{p} where p p is a prime number. We will start investigating the p p -adic Ducci matrices to understand the convergence of the starting sequences. We will start by reviewing some basic definition of the Ducci matrices by recalling the definition.

###### Definition 0.1.

Let A ∈ 𝕄 n × n ​ ( ℝ) A\in\mathbb{M}_{n\times n}(\mathbb{R}) a not all zeros squared matrix with real values. We define the Ducci operator the following map

 | δ ⁡ ( x): \displaystyle\delta(x): | ℝ n ⟶ ℝ n \displaystyle\mathbb{R}^{n}\longrightarrow\mathbb{R}^{n} |  |

 |  | x ⟼ | A ​ x | \displaystyle x\longmapsto|Ax| |  |

when the absolute value is taken componentwise | x | = ( | x 1 |, | x 2 |, …, | x n |) ⊤ |x|=(|x_{1}|,|x_{2}|,\dots,|x_{n}|)^{\top}.

It we take A A as follows

 | A = ( 1 − 1 0 0 0 1 − 1 0 0 0 1 − 1 − 1 0 0 1) \displaystyle A=\begin{pmatrix}1&-1&0&0\\ 0&1&-1&0\\ 0&0&1&-1\\ -1&0&0&1\end{pmatrix} |  |

We get the original Ducci map. Starting from a sequence x ∈ ℝ n x\in\mathbb{R}^{n} the sequence is arranged as

 | x, δ ⁡ ( x), δ 2 = δ ⁡ ( δ ⁡ ( x)) = δ ∘ δ, …, δ n ​ ( x), … \displaystyle x,\delta(x),\delta^{2}=\delta(\delta(x))=\delta\circ\delta,\dots,\delta^{n}(x),\dots |  |

will be called the Ducci sequence of x x respect to A A. It x x is a zero vector (i.e all the entries are zeros), we say that the Ducci sequence terminates. Moreover:

###### Definition 0.2.

We say that the Ducci map is cyclic if there exist and index n n a k ∈ ℕ + k\in\mathbb{N}^{+} and a not null vector x x such that

 | δ n ​ ( x) = δ n + k ​ ( x). \delta^{n}(x)=\delta^{n+k}(x). |  |

k k is called the length of the cycle.

And in a natural way the matrix A ∈ 𝕄 n × n ​ ( ℝ) A\in\mathbb{M}_{n\times n}(\mathbb{R}) is called the Ducci matrix associated to the Ducci map.

Some questions arise from the previous definition:

- •

Considering a Ducci matrix A A and non zero starting sequence x ∈ ℝ x\in\mathbb{R} does the Ducci sequence associated terminate?

- •

Considering a Ducci matrix A A what are the sequences that enter a cycle and in case what are the cycle of minumum lenght?

- •

Considering a Ducci matrix A A and the set of all starting sequences that terminates are the fastest (ie become null in the minimum number of iteration)?

In this paper we are interested to extend the previous definition in the using the p p -adic valuation instead of the standard absolute value norm and we will try to answer some of the previous questions in the p p -adic field ℚ p \mathbb{Q}_{p}. Using the previous notation we can move with the following

###### Definition 0.3.

Let p p be a prime and let x x be an n-tuple with entries in ℚ p \mathbb{Q}_{p} so that x ∈ ℚ p n x\in\mathbb{Q}_{p}^{n} and D p ∈ 𝕄 n × n ​ ( ℚ p) D_{p}\in\mathbb{M}_{n\times n}(\mathbb{Q}_{p}) a matrix whose entries are in the field ℚ p \mathbb{Q}_{p} we define the p p -adic Ducci operator δ p ​ ( x) \delta_{p}(x) as follows

 | δ p ​ ( x): \displaystyle\delta_{p}(x): | ℚ p n ⟶ ℚ p n \displaystyle\mathbb{Q}_{p}^{n}\longrightarrow\mathbb{Q}_{p}^{n} |  |

 |  | x ⟼ δ p ​ ( x) = | D p ​ x | p \displaystyle x\longmapsto\delta_{p}(x)=|D_{p}x|_{p} |  |

where if x ∈ ℚ p n x\in\mathbb{Q}^{n}_{p} then | x | p = ( | x 1 | p, | x 2 | p, …, | x n | p) |x|_{p}=(|x_{1}|_{p},|x_{2}|_{p},\dots,|x_{n}|_{p}) and for every i i we have that | x i | p = 1 p o ​ r ​ d p ​ ( x i) |x_{i}|_{p}=\frac{1}{p^{ord_{p}(x_{i})}} being o r d p ( x i) = m a x { m: p m | x i } ord_{p}(x_{i})=max\{m:p^{m}|x_{i}\} (i.e. o ​ r ​ d p ​ ( x) ord_{p}(x) is the maximum power of p p that divide x i x_{i}).

Prior to proceed let us consider the the product D p ​ x D_{p}x. Since D p D_{p} is an n × n n\times n matrix with entries in ℚ p \mathbb{Q}_{p} and x x is an n n -tuple with entries in ℚ p \mathbb{Q}_{p}, the result D p ​ x D_{p}x is an n n -tuple with entries in ℚ p \mathbb{Q}_{p}. Formally, if D p = ( d i ​ j) D_{p}=(d_{ij}) and x = ( x 1, x 2, …, x n) x=(x_{1},x_{2},\ldots,x_{n}), then the i i -th component of D p ​ x D_{p}x is given by:

 | ( D p ​ x) i = ∑ j = 1 n d i ​ j ​ x j ∈ ℚ p (D_{p}x)_{i}=\sum_{j=1}^{n}d_{ij}x_{j}\in\mathbb{Q}_{p} |  |

The p-adic norm | ⋅ | p |\cdot|_{p} is applied component-wise to the resulting n n -tuple D p ​ x D_{p}x. For each component ( D p ​ x) i (D_{p}x)_{i} of D p ​ x D_{p}x, we have:

 | | ( D p ​ x) i | p = 1 p ord p ​ ( ( D p ​ x) i) |(D_{p}x)_{i}|_{p}=\frac{1}{p^{\text{ord}_{p}((D_{p}x)_{i})}} |  |

where ord p ​ ( ( D p ​ x) i) \text{ord}_{p}((D_{p}x)_{i}) is the highest power of p p dividing ( D p ​ x) i (D_{p}x)_{i}.

Since the p-adic norm | ⋅ | p |\cdot|_{p} maps elements of ℚ p \mathbb{Q}_{p} to ℚ p \mathbb{Q}_{p}, applying it component-wise to an n n -tuple will result in another n n -tuple with entries in ℚ p \mathbb{Q}_{p}. Therefore, | D p ​ x | p |D_{p}x|_{p} is an n n -tuple with entries in ℚ p \mathbb{Q}_{p}.

Thus, δ p ​ ( x) = | D p ​ x | p ∈ ℚ p n \delta_{p}(x)=|D_{p}x|_{p}\in\mathbb{Q}_{p}^{n}, hence, the map δ p \delta_{p} is well-defined.

As we have seens previous we can define the p p -adic Ducci sequence the sequence

###### Definition 0.4 ( p p -adic Ducci sequence).

 | x, δ p ​ ( x), δ p 2 = δ p ​ ( δ p ​ ( x)) = δ p ∘ δ p, …, δ p n ​ ( x), … \displaystyle x,\delta_{p}(x),\delta_{p}^{2}=\delta_{p}(\delta_{p}(x))=\delta_{p}\circ\delta_{p},\dots,\delta_{p}^{n}(x),\dots |  |

with initial seed x ∈ ℚ p n x\in\mathbb{Q}_{p}^{n} respect to D p ∈ 𝕄 n × n ​ ( ℚ p) D_{p}\in\mathbb{M}_{n\times n}(\mathbb{Q}_{p}). In this p-adic context, we define a p-adic Ducci map associated with a p p -adic matrix D p D_{p} as a function that maps a p-adic vector x x to | D p ​ x | p |D_{p}x|_{p}, where | ⋅ | p |\cdot|_{p} is applied elementwise.

Without loss of generality we can define the following For convergence to zero, we analyze when x k → 0 x_{k}\to 0 as k → ∞ k\to\infty.

Prior to move forward we recall the following

###### Remark 1.

In the field of p p -adic numbers ℚ p \mathbb{Q}_{p}, the p p -adic absolute value | x | p |x|_{p} of a nonzero element x x is defined as:

 | | x | p = p − v p ​ ( x), |x|_{p}=p^{-v_{p}(x)}, |  |

where v p ​ ( x) v_{p}(x) is the p p -adic valuation of x x. The valuation v p ​ ( x) v_{p}(x) is the highest power of p p that divides x x in ℚ p \mathbb{Q}_{p}.

If | x | p < 1 |x|_{p}<1 and x ≠ 0 x\neq 0, this means that v p ​ ( x) > 0 v_{p}(x)>0, so x x is divisible by p p. The possible values of | x | p |x|_{p} in this case are:

 | | x | p = p − k, where ​ k ∈ ℕ ​ and ​ k ≥ 1. |x|_{p}=p^{-k},\quad\text{where }k\in\mathbb{N}\text{ and }k\geq 1. |  |

Thus, the possible values of | x | p |x|_{p} when | x | p < 1 |x|_{p}<1 are:

 | { p − 1, p − 2, p − 3, … }. \left\{p^{-1},p^{-2},p^{-3},\dots\right\}. |  |

So in | x | p < 1 ⇔ x ∈ 0 ∪ { p − 1, p − 2, … ​ p k, … } |x|_{p}<1\iff x\in{0}\cup\{p^{-1},p^{-2},\dots p^{k},\dots\}. The condition | x | p = 1 |x|_{p}=1 implies:

 | p − v p ​ ( x) = 1. p^{-v_{p}(x)}=1. |  |

Since p − v p ​ ( x) = 1 p^{-v_{p}(x)}=1 if and only if v p ​ ( x) = 0 v_{p}(x)=0, the condition | x | p = 1 |x|_{p}=1 is equivalent to v p ​ ( x) = 0 v_{p}(x)=0. So , if v p ​ ( x) = 0 v_{p}(x)=0, then x x is a p p -adic integer (i.e., x ∈ ℤ p x\in\mathbb{Z}_{p}) and x x is not divisible by p p.

We are now ready to answer some questions about the p p -adic Ducci sequence. The first one is find a necessary condition such that given any initial not null sequence x x, eventually the p p -adic Ducci sequence terminates.

Let us consider the first simpler case in the following

###### Proposition 2.

If all eigenvalues of D p ∈ 𝕄 n × n ​ ( ℚ p) D_{p}\in\mathbb{M}_{n\times n}(\mathbb{Q}_{p}) have p p -adic norm less that 1 1 then the p p -adic Ducci sequence terminates.

###### Proof.

Let D p D_{p} be a p p -adic diagonal matrix:

 | A = diag ​ ( λ 1, λ 2, …, λ n), A=\text{diag}(\lambda_{1},\lambda_{2},\dots,\lambda_{n}), |  |

where each λ i \lambda_{i} satisfies | λ i | p < 1 |\lambda_{i}|_{p}<1. Given an initial vector x 0 = ( x 1, x 2, …, x n) ⊤ ∈ ℚ p n x_{0}=(x_{1},x_{2},\dots,x_{n})^{\top}\in\mathbb{Q}_{p}^{n}, the iterates satisfy:

 | x k + 1 = D p k ​ x k. x_{k+1}=D_{p}^{k}x_{k}. |  |

Since D p D_{p} is diagonal, each component x i x_{i} of the n n -tuple x x follows:

 | x i k + 1 = λ i k ​ x i k, x_{i}^{k+1}=\lambda_{i}^{k}x_{i}^{k}, |  |

with 0 ≤ i ≤ n 0\leq i\leq n and k ∈ ℕ k\in\mathbb{N} Applying the p p -adic absolute value:

 | | x k ( i) | p = | λ i k ​ x 0 ( i) | p = | λ i | p k ⋅ | x 0 ( i) | p. |x_{k}^{(i)}|_{p}=|\lambda_{i}^{k}x_{0}^{(i)}|_{p}=|\lambda_{i}|_{p}^{k}\cdot|x_{0}^{(i)}|_{p}. |  |

Since | λ i | p < 1 |\lambda_{i}|_{p}<1, we have:

 | lim k → ∞ | λ i | p k = 0. \lim_{k\to\infty}|\lambda_{i}|_{p}^{k}=0. |  |

Thus,

 | lim k → ∞ | x k ( i) | p = 0. \lim_{k\to\infty}|x_{k}^{(i)}|_{p}=0. |  |

Since this holds for each coordinate i i, it follows that:

 | lim k → ∞ | ( D p) k ​ x 0 | p = 0. \lim_{k\to\infty}|(D_{p})^{k}x_{0}|_{p}=0. |  |

This proves that the sequence eventually terminates becoming the zero vector in ℚ p n \mathbb{Q}_{p}^{n}. ∎

We can also have the following corollary

###### Corollary 3.

Let D p D_{p} a p p -adic Ducci matrix if all eigenvalues are in the set { p − 1, …, p − n, … } \{p^{-1},\dots,p^{-n},\dots\} then the p p -adic Ducci sequence terminates.

A more interesting case of study for the p p -adic Ducci matrix is the following one

###### Theorem 4.

Let D p ∈ 𝕄 n × n ​ ( ℚ p) D_{p}\in\mathbb{M}_{n\times n}(\mathbb{Q}_{p}) be a p p -adic Ducci matrix, and let x 0 ∈ ℚ p n x_{0}\in\mathbb{Q}_{p}^{n} be an initial vector. If all eigenvalues λ i \lambda_{i} of D p D_{p} satisfy | λ i | p = 1 |\lambda_{i}|_{p}=1, then:

1. 1.

The p p -adic Ducci sequence { x k } \{x_{k}\} defined by x k + 1 = | D p ​ x k | p x_{k+1}=|D_{p}x_{k}|_{p} does not converge to zero.

2. 2.

If the eigenvalues are roots of unity in ℚ p \mathbb{Q}_{p}, the sequence { x k } \{x_{k}\} is eventually periodic.

###### Proof.

Let us start with the first part about the non-convergence to zero.
Let λ 1, λ 2, …, λ n \lambda_{1},\lambda_{2},\dots,\lambda_{n} be the eigenvalues of D p D_{p}, and assume | λ i | p = 1 |\lambda_{i}|_{p}=1 for all i i. By the Jordan canonical form, D p D_{p} can be decomposed as:

 | D p = P ​ J ​ P − 1, D_{p}=PJP^{-1}, |  |

where P P is an invertible matrix and J J is the Jordan canonical form of D p D_{p}. The Jordan blocks of J J correspond to the eigenvalues λ i \lambda_{i}.

For each eigenvalue λ i \lambda_{i}, the p p -adic norm satisfies | λ i | p = 1 |\lambda_{i}|_{p}=1. Consider the iterates of the sequence:

 | x k + 1 = | D p ​ x k | p. x_{k+1}=|D_{p}x_{k}|_{p}. |  |

In the Jordan basis, the iterates can be expressed as:

 | y k + 1 = | J ​ y k | p, y_{k+1}=|Jy_{k}|_{p}, |  |

where y k = P − 1 ​ x k y_{k}=P^{-1}x_{k}. Since J J is block-diagonal, the behavior of y k y_{k} is determined by the Jordan blocks of J J.

For each Jordan block corresponding to λ i \lambda_{i}, the iterates satisfy:

 | y k ( i) = λ i k ​ y 0 ( i) + (lower-order terms), y_{k}^{(i)}=\lambda_{i}^{k}y_{0}^{(i)}+\text{(lower-order terms)}, |  |

where the lower-order terms arise from the structure of the Jordan block. Applying the p p -adic norm:

 | | y k ( i) | p = | λ i k ​ y 0 ( i) + (lower-order terms) | p. |y_{k}^{(i)}|_{p}=|\lambda_{i}^{k}y_{0}^{(i)}+\text{(lower-order terms)}|_{p}. |  |

Since | λ i | p = 1 |\lambda_{i}|_{p}=1, we have:

 | | λ i k ​ y 0 ( i) | p = | λ i | p k ⋅ | y 0 ( i) | p = | y 0 ( i) | p. |\lambda_{i}^{k}y_{0}^{(i)}|_{p}=|\lambda_{i}|_{p}^{k}\cdot|y_{0}^{(i)}|_{p}=|y_{0}^{(i)}|_{p}. |  |

The lower-order terms do not affect the p p -adic norm because | λ i | p = 1 |\lambda_{i}|_{p}=1 ensures that the dominant term is λ i k ​ y 0 ( i) \lambda_{i}^{k}y_{0}^{(i)}. Thus:

 | | y k ( i) | p = | y 0 ( i) | p. |y_{k}^{(i)}|_{p}=|y_{0}^{(i)}|_{p}. |  |

This shows that the p p -adic norm of each component of y k y_{k} remains constant. Consequently, the sequence { x k } \{x_{k}\} does not converge to zero.
We would like to move on by examinating the periodicity of the roots of unity so to determinate the periodicity in this case. Assume that the eigenvalues λ i \lambda_{i} are roots of unity in ℚ p \mathbb{Q}_{p}. That is, for each λ i \lambda_{i}, there exists an integer m i ≥ 1 m_{i}\geq 1 such that:

 | λ i m i = 1. \lambda_{i}^{m_{i}}=1. |  |

Let m m be the least common multiple of the m i m_{i}. Then, for each λ i \lambda_{i}, we have:

 | λ i m = 1. \lambda_{i}^{m}=1. |  |

In the Jordan basis, the iterates satisfy:

 | y k + m ( i) = λ i k + m ​ y 0 ( i) + (lower-order terms) = λ i k ​ y 0 ( i) + (lower-order terms) = y k ( i). y_{k+m}^{(i)}=\lambda_{i}^{k+m}y_{0}^{(i)}+\text{(lower-order terms)}=\lambda_{i}^{k}y_{0}^{(i)}+\text{(lower-order terms)}=y_{k}^{(i)}. |  |

Thus, the sequence { y k } \{y_{k}\} is periodic with period m m. Transforming back to the original basis, the sequence { x k } \{x_{k}\} is also periodic with period m m.

∎

###### Theorem 5.

Let D p ∈ 𝕄 n × n ​ ( ℚ p) D_{p}\in\mathbb{M}_{n\times n}(\mathbb{Q}_{p}) be a p p -adic Ducci matrix, and let x 0 ∈ ℤ p n x_{0}\in\mathbb{Z}_{p}^{n} be an initial vector. If all eigenvalues λ i \lambda_{i} of D p D_{p} satisfy | λ i | p = 1 |\lambda_{i}|_{p}=1, then:

1. 1.

The p p -adic Ducci sequence { x k } \{x_{k}\} defined by x k + 1 = | D p ​ x k | p x_{k+1}=|D_{p}x_{k}|_{p} does not converge to zero.

2. 2.

If the eigenvalues are roots of unity in ℚ p \mathbb{Q}_{p}, the sequence { x k } \{x_{k}\} is eventually periodic.

###### Proof.

Part 1: Non-convergence to zero

Let λ 1, λ 2, …, λ n \lambda_{1},\lambda_{2},\dots,\lambda_{n} be the eigenvalues of D p D_{p}, and assume | λ i | p = 1 |\lambda_{i}|_{p}=1 for all i i. By the Jordan canonical form, D p D_{p} can be decomposed as:

 | D p = P ​ J ​ P − 1, D_{p}=PJP^{-1}, |  |

where P P is an invertible matrix and J J is the Jordan canonical form of D p D_{p}. The Jordan blocks of J J correspond to the eigenvalues λ i \lambda_{i}.

For each eigenvalue λ i \lambda_{i}, the p p -adic norm satisfies | λ i | p = 1 |\lambda_{i}|_{p}=1. Consider the iterates of the sequence:

 | x k + 1 = | D p ​ x k | p. x_{k+1}=|D_{p}x_{k}|_{p}. |  |

In the Jordan basis, the iterates can be expressed as:

 | y k + 1 = | J ​ y k | p, y_{k+1}=|Jy_{k}|_{p}, |  |

where y k = P − 1 ​ x k y_{k}=P^{-1}x_{k}. Since J J is block-diagonal, the behavior of y k y_{k} is determined by the Jordan blocks of J J.

For each Jordan block corresponding to λ i \lambda_{i}, the iterates satisfy:

 | y k ( i) = λ i k ​ y 0 ( i) + (lower-order terms), y_{k}^{(i)}=\lambda_{i}^{k}y_{0}^{(i)}+\text{(lower-order terms)}, |  |

where the lower-order terms arise from the structure of the Jordan block. Applying the p p -adic norm:

 | | y k ( i) | p = | λ i k ​ y 0 ( i) + (lower-order terms) | p. |y_{k}^{(i)}|_{p}=|\lambda_{i}^{k}y_{0}^{(i)}+\text{(lower-order terms)}|_{p}. |  |

Since | λ i | p = 1 |\lambda_{i}|_{p}=1, we have:

 | | λ i k ​ y 0 ( i) | p = | λ i | p k ⋅ | y 0 ( i) | p = | y 0 ( i) | p. |\lambda_{i}^{k}y_{0}^{(i)}|_{p}=|\lambda_{i}|_{p}^{k}\cdot|y_{0}^{(i)}|_{p}=|y_{0}^{(i)}|_{p}. |  |

The lower-order terms do not affect the p p -adic norm because | λ i | p = 1 |\lambda_{i}|_{p}=1 ensures that the dominant term is λ i k ​ y 0 ( i) \lambda_{i}^{k}y_{0}^{(i)}. Thus:

 | | y k ( i) | p = | y 0 ( i) | p. |y_{k}^{(i)}|_{p}=|y_{0}^{(i)}|_{p}. |  |

This shows that the p p -adic norm of each component of y k y_{k} remains constant. Consequently, the sequence { x k } \{x_{k}\} does not converge to zero.

Moving with the second part of the theorem we now assume that the eigenvalues λ i \lambda_{i} are roots of unity in ℚ p \mathbb{Q}_{p}. That is, for each λ i \lambda_{i}, there exists an integer m i ≥ 1 m_{i}\geq 1 such that:

 | λ i m i = 1. \lambda_{i}^{m_{i}}=1. |  |

Let m m be the least common multiple of the m i m_{i}. Then, for each λ i \lambda_{i}, we have:

 | λ i m = 1. \lambda_{i}^{m}=1. |  |

In the Jordan basis, the iterates satisfy:

 | y k + m ( i) = λ i k + m ​ y 0 ( i) + (lower-order terms) = λ i k ​ y 0 ( i) + (lower-order terms) = y k ( i). y_{k+m}^{(i)}=\lambda_{i}^{k+m}y_{0}^{(i)}+\text{(lower-order terms)}=\lambda_{i}^{k}y_{0}^{(i)}+\text{(lower-order terms)}=y_{k}^{(i)}. |  |

Thus, the sequence { y k } \{y_{k}\} is periodic with period m m. Transforming back to the original basis, the sequence { x k } \{x_{k}\} is also periodic with period m m.

∎

When the eigenvalues of the p p -adic Ducci matrix D p D_{p} are not bounded is it possible to find a sequence that does not terminates and does not enter a cycle.

###### Example 1.

Let p = 2 p=2 (for simplicity), and consider the following 2 × 2 2\times 2 matrix over ℚ 2 \mathbb{Q}_{2}:

 | D 2 = ( 1 2 0 0 1 2). D_{2}=\begin{pmatrix}\frac{1}{2}&0\\ 0&\frac{1}{2}\end{pmatrix}. |  |

The eigenvalues of D 2 D_{2} are λ 1 = 1 2 \lambda_{1}=\frac{1}{2} and λ 2 = 1 2 \lambda_{2}=\frac{1}{2}. The 2 2 -adic norm of these eigenvalues is:

 | | λ 1 | 2 = | λ 2 | 2 = | 1 2 | 2 = 2 > 1. |\lambda_{1}|_{2}=|\lambda_{2}|_{2}=\left|\frac{1}{2}\right|_{2}=2>1. |  |

For the matrix D 2 D_{2}, the iterates are:

 | x k + 1 = | ( 1 2 0 0 1 2) ​ x k | 2 = ( | 1 2 ​ x 1 ( k) | 2, | 1 2 ​ x 2 ( k) | 2) ⊤. x_{k+1}=\left|\begin{pmatrix}\frac{1}{2}&0\\ 0&\frac{1}{2}\end{pmatrix}x_{k}\right|_{2}=\left(\left|\frac{1}{2}x_{1}^{(k)}\right|_{2},\left|\frac{1}{2}x_{2}^{(k)}\right|_{2}\right)^{\top}. |  |

Using the properties of the p p -adic norm:

 | | 1 2 ​ x i ( k) | 2 = | 1 2 | 2 ⋅ | x i ( k) | 2 = 2 ⋅ | x i ( k) | 2. \left|\frac{1}{2}x_{i}^{(k)}\right|_{2}=\left|\frac{1}{2}\right|_{2}\cdot\left|x_{i}^{(k)}\right|_{2}=2\cdot\left|x_{i}^{(k)}\right|_{2}. |  |

Thus, the iteration becomes:

 | x k + 1 = 2 ⋅ x k. x_{k+1}=2\cdot x_{k}. |  |

Starting from x 0 = ( x 1, x 2) ⊤ x_{0}=(x_{1},x_{2})^{\top}, the sequence grows exponentially:

 | x 1 = 2 x 0, x 2 = 2 x 1 = 2 2 x 0, x 3 = 2 x 2 = 2 3 x 0, …, x k = 2 k x 0. x_{1}=2x_{0},\quad x_{2}=2x_{1}=2^{2}x_{0},\quad x_{3}=2x_{2}=2^{3}x_{0},\quad\dots,\quad x_{k}=2^{k}x_{0}. |  |

The p p -adic norm of x k x_{k} is:

 | | x k | 2 = | 2 k ​ x 0 | 2 = | 2 k | 2 ⋅ | x 0 | 2 = 2 − k ⋅ | x 0 | 2. |x_{k}|_{2}=|2^{k}x_{0}|_{2}=|2^{k}|_{2}\cdot|x_{0}|_{2}=2^{-k}\cdot|x_{0}|_{2}. |  |

Since | x 0 | 2 |x_{0}|_{2} is fixed and 2 − k 2^{-k} grows without bound as k → ∞ k\to\infty, the sequence { x k } \{x_{k}\} grows indefinitely in the p p -adic norm.

The matrix D 2 = ( 1 2 0 0 1 2) D_{2}=\begin{pmatrix}\frac{1}{2}&0\\ 0&\frac{1}{2}\end{pmatrix} has eigenvalues λ 1 = λ 2 = 1 2 \lambda_{1}=\lambda_{2}=\frac{1}{2}, which satisfy | λ i | 2 = 2 > 1 |\lambda_{i}|_{2}=2>1. The associated p p -adic Ducci sequence grows exponentially and diverges in the p p -adic norm. This provides an explicit example of a p p -adic Ducci matrix with eigenvalues greater than 1 in p p -adic valuation that leads to indefinite growth.

The fact that the Ducci matrix has values in 𝕄 n × n ​ ( ℚ p) \mathbb{M}_{n\times n}(\mathbb{Q}_{p}) and the initial sequence x x has values in ℚ p n \mathbb{Q}_{p}^{n} is essential for the previous behavior, a simple change in this assumption can lead to a different result as stated by the following:

###### Theorem 6.

Let D p ∈ 𝕄 n × n ​ ( ℤ p) D_{p}\in\mathbb{M}_{n\times n}(\mathbb{Z}_{p}) be a p p -adic Ducci matrix, and let x 0 ∈ ℤ p n x_{0}\in\mathbb{Z}_{p}^{n} be an initial vector. If all eigenvalues λ i \lambda_{i} of D p D_{p} satisfy | λ i | p = 1 |\lambda_{i}|_{p}=1, then:

1. 1.

The p p -adic Ducci sequence does not terminate.

2. 2.

If the eigenvalues are roots of unity in ℚ p \mathbb{Q}_{p}, the sequence { x k } \{x_{k}\} is eventually periodic.

###### Proof.

Let λ 1, λ 2, …, λ n \lambda_{1},\lambda_{2},\dots,\lambda_{n} be the eigenvalues of D p D_{p}, and assume | λ i | p = 1 |\lambda_{i}|_{p}=1 for all i i. By the Jordan canonical form, D p D_{p} can be decomposed as:

 | D p = P ​ J ​ P − 1, D_{p}=PJP^{-1}, |  |

where P P is an invertible matrix and J J is the Jordan canonical form of D p D_{p}. The Jordan blocks of J J correspond to the eigenvalues λ i \lambda_{i}.

For each eigenvalue λ i \lambda_{i}, the p p -adic norm satisfies | λ i | p = 1 |\lambda_{i}|_{p}=1. Consider the iterates of the sequence:

 | x k + 1 = | D p ​ x k | p. x_{k+1}=|D_{p}x_{k}|_{p}. |  |

In the Jordan basis, the iterates can be expressed as:

 | y k + 1 = | J ​ y k | p, y_{k+1}=|Jy_{k}|_{p}, |  |

where y k = P − 1 ​ x k y_{k}=P^{-1}x_{k}. Since J J is block-diagonal, the behavior of y k y_{k} is determined by the Jordan blocks of J J.

For each Jordan block corresponding to λ i \lambda_{i}, the iterates satisfy:

 | y k ( i) = λ i k ​ y 0 ( i) + (lower-order terms), y_{k}^{(i)}=\lambda_{i}^{k}y_{0}^{(i)}+\text{(lower-order terms)}, |  |

where the lower-order terms arise from the structure of the Jordan block. Applying the p p -adic norm:

 | | y k ( i) | p = | λ i k ​ y 0 ( i) + (lower-order terms) | p. |y_{k}^{(i)}|_{p}=|\lambda_{i}^{k}y_{0}^{(i)}+\text{(lower-order terms)}|_{p}. |  |

Since | λ i | p = 1 |\lambda_{i}|_{p}=1, we have:

 | | λ i k ​ y 0 ( i) | p = | λ i | p k ⋅ | y 0 ( i) | p = | y 0 ( i) | p. |\lambda_{i}^{k}y_{0}^{(i)}|_{p}=|\lambda_{i}|_{p}^{k}\cdot|y_{0}^{(i)}|_{p}=|y_{0}^{(i)}|_{p}. |  |

The lower-order terms do not affect the p p -adic norm because | λ i | p = 1 |\lambda_{i}|_{p}=1 ensures that the dominant term is λ i k ​ y 0 ( i) \lambda_{i}^{k}y_{0}^{(i)}. Thus:

 | | y k ( i) | p = | y 0 ( i) | p. |y_{k}^{(i)}|_{p}=|y_{0}^{(i)}|_{p}. |  |

This shows that the p p -adic norm of each component of y k y_{k} remains constant. Consequently, the sequence { x k } \{x_{k}\} does not converge to zero.

For the second part we can reuse the previous results. Assume that the eigenvalues λ i \lambda_{i} are roots of unity in ℚ p \mathbb{Q}_{p}. That is, for each λ i \lambda_{i}, there exists an integer m i ≥ 1 m_{i}\geq 1 such that:

 | λ i m i = 1. \lambda_{i}^{m_{i}}=1. |  |

Let m m be the least common multiple of the m i m_{i}. Then, for each λ i \lambda_{i}, we have:

 | λ i m = 1. \lambda_{i}^{m}=1. |  |

In the Jordan basis, the iterates satisfy:

 | y k + m ( i) = λ i k + m ​ y 0 ( i) + (lower-order terms) = λ i k ​ y 0 ( i) + (lower-order terms) = y k ( i). y_{k+m}^{(i)}=\lambda_{i}^{k+m}y_{0}^{(i)}+\text{(lower-order terms)}=\lambda_{i}^{k}y_{0}^{(i)}+\text{(lower-order terms)}=y_{k}^{(i)}. |  |

Thus, the sequence { y k } \{y_{k}\} is periodic with period m m. Transforming back to the original basis, the sequence { x k } \{x_{k}\} is also periodic with period m m.

∎

In this paper we present the ”dopplerganger” of the Ducci matrices and the Ducci operatorin the context of the p p -adic field ℚ p \mathbb{Q}_{p} and ℤ p \mathbb{Z}_{p} both as matrices as well as starting sequences. We studied different cases and we enlight some convergence criteria such that the original sequence terminates. We did not examine the velocity (ie. the mininum not null sequence that terminates in the fastest way. This will be object of further research.

## References

- [1] C. Ciamberlini and A. Marengoni, “Su una interessante curiosita numerica,” Periodico di Mathematiche, vol. 17, no. IV, pp. 25–30, 1937.
- [2] A. Clausing, “Ducci matrices,” The American Mathematical Monthly, vol. 125, no. 10, pp. 901–921, 2018.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:pgiacome@gmail.com
