<!-- source: https://arxiv.org/html/1806.09561v6 | converted from HTML -->

The Casas-Alvero conjecture for three recycled roots in degree 20

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1806.09561v6 [math.AG] 25 Aug 2023

# The Casas-Alvero conjecture for three recycled roots in degree 20 Journal: arXiv

César Massri Email: [cmassri@caece.edu.ar][3] Address: Department of Mathematics, CAECE, Buenos Aires, Argentina Corresponding author: Address for correspondence: Department of Mathematics, CAECE, Buenos Aires, Argentina. Postal address: Av. de Mayo 866. Phone number: 54-11-5217-7878. Note: The author was fully supported by CONICET, IMAS, Buenos Aires, Argentina

###### Abstract

The Casas-Alvero conjecture says that a degree n n complex univariate polynomial sharing a root with each of its derivative must have only one root. In this article we give three results. The first one, is that the number of possible counterexamples in normal form of degree p r + p s p^{r}+p^{s} or p r + 2 ​ p s p^{r}+2p^{s} is finite ( p p prime, r, s r,s positive integers). The second result is that a possible counterexample in normal form of degree p r + 1 p^{r}+1 has algebraic coefficients and the final result is that in degree 20 20 there are no counterexamples with three recycled roots.

###### Keywords:

Casas-Alvero problem, Abel-Gontcharoff polynomial, complex automorphisms , recycled roots

###### 2010 MSC

14N05, 14R20, 14L30, 12D10

## Introduction

E. Casas-Alvero conjectured in relation to his work on plane curves [3, 2], that a degree n n polynomial f f sharing a root with each of its derivative must have only one root. Specifically, let f ∈ ℂ ⁡ [x] f\in\mathbb{C}[x] be a univariate polynomial such that

 | res ⁡ ( f, f i) = 0, 1 ≤ i ≤ n − 1, \res(f,f^{i})=0,\quad 1\leq i\leq n-1, |  |

where res ⁡ ( −, −) \res(-,-) is the resultant. The Casas-Alvero conjecture says that f f has a multiplicity n n root. This conjecture was checked with a computer in low degrees [6] and proved, by using techniques from number theory for degrees p e, 2 ​ p e, 3 ​ p e, 4 ​ p e, 5 ​ p e p^{e},2p^{e},3p^{e},4p^{e},5p^{e}, where e e is a natural number and p p runs through a list of infinitely many prime numbers, see [15, 5, 7, 9] for a precise statement. Also, in [17, 16, 4] several constrains on a possible counterexample are given. The conjecture is known to be false in positive characteristic and the first open case is n = 20 n=20.

In this article, we present new results regarding the Casas-Alvero conjecture. We based our analysis in standard arguments appearing in the literature and on the properties of Abel-Gontcharoff polynomials. Specifically, we applied arguments on positive characteristics and brute-force computations to deduce our first two results. Our third result were deduced from properties of Abel-Gontcharoff polynomials where we proved that there are no counterexamples in degree 20 with three recycled roots.

In the first four sections we collect some results from the available bibliography (published or not) and give some remarks. We do not take credit on these results except maybe on Proposition 3.5 that we do not found it in the literature on interpolation theory. In section 5 we prove that there are a finite number of possible counterexamples (written in normal form) of degrees p s ​ ( p r + 1) p^{s}(p^{r}+1) or p s ​ ( p r + 2) p^{s}(p^{r}+2), where p p is a prime and r, s r,s non-negative integers. In section 6 we prove that the possible counterexamples in degree p r + 1 p^{r}+1 are in ℚ ¯ ​ [x] \overline{\mathbb{Q}}[x] and finally, in section 7 we prove that there are no counterexamples with three recycled roots in degree 20 20.

## 1 Polynomials with one root

###### Definition 1.1.

Let f f be a degree n n complex polynomial and let h h be some complex number. We denote f h f^{h} to the polynomial given by

 | f h ​ ( x):= f ⁡ ( x + h), x ∈ ℂ. f^{h}(x):=f(x+h),\quad x\in\mathbb{C}. |  |

Notice that if a a is a root of f f, then a − h a-h is a root of f h f^{h}.

###### Lemma 1.2.

Let f f be a degree n n complex monic polynomial and let F F be its companion matrix. Then, the following are equivalent

1. 1.

f f is equal to b ​ ( x − a) n b(x-a)^{n} for some complex numbers a, b a,b, b ≠ 0 b\neq 0.

2. 2.

f f has exactly 1 1 root.

3. 3.

res ⁡ ( f, f h) ≠ 0 \res(f,f^{h})\neq 0 for all non-zero complex number h h.

4. 4.

det ( f h ​ ( F)) ≠ 0 \det(f^{h}(F))\neq 0 for all non-zero complex number h h.

5. 5.

det ( f h ​ ( F)) \det(f^{h}(F)) as a polynomial in h h has exactly 1 1 root.

6. 6.

det ( f h ​ ( F)) \det(f^{h}(F)) as a polynomial in h h is equal to h m h^{m} for some m > 0 m>0.

7. 7.

det ( f h ​ ( F)) \det(f^{h}(F)) as a polynomial in h h is equal to h n 2 h^{n^{2}}.

8. 8.

res ⁡ ( f, f h) = h n 2 \res(f,f^{h})=h^{n^{2}}.

###### Proof.

Let us prove 2 2 implies 3 3. If f f has exactly one root a a, then f h f^{h} also has exactly one root equal to a − h a-h. Then, res ⁡ ( f, f h) \res(f,f^{h}) is zero if and only if h = 0 h=0. Now let us prove 8 8 implies 1 1. From 8 8 we deduce that res ⁡ ( f, f h) \res(f,f^{h}) is zero if and only if h = 0 h=0 and this implies 1 1. ∎

###### Lemma 1.3.

Let f f be a degree n n complex polynomial with roots { λ 1, …, λ n } \{\lambda_{1},\ldots,\lambda_{n}\} and let F F be its companion matrix. Then, det ( f h ​ ( F)) \det(f^{h}(F)) as a polynomial in h h is equal to either of the following expressions

 | ∑ k = 0 n 2 ( ∑ k 1 + ⋯ + k n = k f ( k 1) ​ ( λ 1) k 1! ​ … ​ f ( k n) ​ ( λ n) k n!) ​ h k = h n ​ ∏ i < j ( h 2 − ( λ i − λ j) 2). \sum_{k=0}^{n^{2}}\left(\sum_{k_{1}+\dots+k_{n}=k}\frac{f^{(k_{1})}(\lambda_{1})}{k_{1}!}\dots\frac{f^{(k_{n})}(\lambda_{n})}{k_{n}!}\right)h^{k}=h^{n}\prod_{i<j}\left(h^{2}-(\lambda_{i}-\lambda_{j})^{2}\right). |  |

Both expressions are symmetric polynomials in { λ 1, …, λ n } \{\lambda_{1},\ldots,\lambda_{n}\}.

###### Proof.

Given that f h f^{h} is a polynomial and that F F is similar to a lower triangular matrix, we can compute the expression det ( f h ​ ( F)) \det(f^{h}(F)) from the eigenvalues of F F which are the roots of f f. Then,

 | det ( f h ​ ( F)) = f h ​ ( λ 1) ​ … ​ f h ​ ( λ n) = f ⁡ ( λ 1 + h) ​ … ​ f ​ ( λ n + h). \det(f^{h}(F))=f^{h}(\lambda_{1})\dots f^{h}(\lambda_{n})=f(\lambda_{1}+h)\dots f(\lambda_{n}+h). |  |

Recall that if λ 1, …, λ n \lambda_{1},\dots,\lambda_{n} are the roots of f f, then the roots of f ⁡ ( λ k + h) f(\lambda_{k}+h) are λ 1 − λ k, …, λ n − λ k \lambda_{1}-\lambda_{k},\dots,\lambda_{n}-\lambda_{k}. Hence, we can factorize the right hand side of the previous equation as

 | f ⁡ ( λ 1 + h) ​ … ​ f ​ ( λ n + h) \displaystyle f(\lambda_{1}+h)\dots f(\lambda_{n}+h) | = ( ( h − λ 1 + λ 1) ​ … ​ ( h − λ 1 + λ n)) ​ … ​ ( ( h − λ n + λ 1) ​ … ​ ( h − λ n + λ n)) \displaystyle=\left((h-\lambda_{1}+\lambda_{1})\dots(h-\lambda_{1}+\lambda_{n})\right)\dots\left((h-\lambda_{n}+\lambda_{1})\dots(h-\lambda_{n}+\lambda_{n})\right) |  |

 |  | = h n ​ ∏ i < j ( h 2 − ( λ i − λ j) 2) \displaystyle=h^{n}\prod_{i<j}\left(h^{2}-(\lambda_{i}-\lambda_{j})^{2}\right) |  |

where, in the last equality, we simplified h − λ k + λ k h-\lambda_{k}+\lambda_{k} and collected the terms ( h − λ i + λ j) ​ ( h − λ j + λ i) (h-\lambda_{i}+\lambda_{j})(h-\lambda_{j}+\lambda_{i}). Now, expanding in h h the left hand side of the previous equation, we get

 | f ⁡ ( λ 1 + h) ​ … ​ f ​ ( λ n + h) = ∏ i = 1 n ( ∑ k i = 0 n f ( k i) ​ ( λ i) k i! ​ h k i) = ∑ k = 0 n 2 ( ∑ k 1 + ⋯ + k n = k f ( k 1) ​ ( λ 1) k 1! ​ … ​ f ( k n) ​ ( λ n) k n!) ​ h k. f(\lambda_{1}+h)\dots f(\lambda_{n}+h)=\prod_{i=1}^{n}\left(\sum_{k_{i}=0}^{n}\frac{f^{(k_{i})}(\lambda_{i})}{k_{i}!}h^{k_{i}}\right)=\sum_{k=0}^{n^{2}}\left(\sum_{k_{1}+\dots+k_{n}=k}\frac{f^{(k_{1})}(\lambda_{1})}{k_{1}!}\dots\frac{f^{(k_{n})}(\lambda_{n})}{k_{n}!}\right)h^{k}. |  |

∎

###### Remark 1.4.

Let e k e_{k} be the k k -th elementary symmetric polynomial in n ⁡ ( n − 1) / 2 n(n-1)/2 variables and degree k k evaluated at { ( λ i − λ j) 2 } i < j \{(\lambda_{i}-\lambda_{j})^{2}\}_{i<j}. Then,

 | h n ​ ∏ i < j ( h 2 − ( λ i − λ j) 2) = h n 2 + e 1 ​ h n 2 − 2 + e 2 ​ h n 2 − 4 + ⋯ + e k ​ h n 2 − 2 ​ k + ⋯ + e n ⁡ ( n − 1) 2 ​ h n. h^{n}\prod_{i<j}\left(h^{2}-(\lambda_{i}-\lambda_{j})^{2}\right)=h^{n^{2}}+e_{1}h^{n^{2}-2}+e_{2}h^{n^{2}-4}+\dots+e_{k}h^{n^{2}-2k}+\dots+e_{\frac{n(n-1)}{2}}h^{n}. |  |

In particular, if r r is such that n 2 − r n^{2}-r is odd,

 | ∑ k 1 + ⋯ + k n = r f ( k 1) ​ ( λ 1) k 1! ​ … ​ f ( k n) ​ ( λ n) k n! = 0. \sum_{k_{1}+\dots+k_{n}=r}\frac{f^{(k_{1})}(\lambda_{1})}{k_{1}!}\dots\frac{f^{(k_{n})}(\lambda_{n})}{k_{n}!}=0. |  |

Clearly, if some k i = 0 k_{i}=0, then f ( k i) ​ ( λ i) = f ⁡ ( λ i) = 0 f^{(k_{i})}(\lambda_{i})=f(\lambda_{i})=0. Hence, the first non-trivial term is f ′ ​ ( λ 1) ​ … ​ f ′ ​ ( λ n) f^{\prime}(\lambda_{1})\dots f^{\prime}(\lambda_{n}), the coefficient of h n h^{n}.

## 2 CA-polynomials

###### Definition 2.1.

A degree n n complex univariate polynomial f f is called a *CA-polynomial*if the resultant between f f and its i i -th derivative vanishes,

 | res ⁡ ( f, f ( i)) = 0, 1 ≤ i ≤ n − 1. \res(f,f^{(i)})=0,\quad 1\leq i\leq n-1. |  |

###### Notation 2.2.

Let ϵ i \epsilon_{i} be the i i -th elementary symmetric polynomial in n n variables and degree i i. The following notation will be used throughout the article. Let us denote ϵ i k \epsilon_{i}^{k} to the polynomial ϵ i ​ ( λ 1 − λ k, …, λ n − λ k) \epsilon_{i}(\lambda_{1}-\lambda_{k},\dots,\lambda_{n}-\lambda_{k}) in ℤ ⁡ [λ 1, …, λ n] \mathbb{Z}[\lambda_{1},\dots,\lambda_{n}],

 | ϵ i k:= ϵ i ​ ( λ 1 − λ k, …, λ n − λ k). \epsilon_{i}^{k}:=\epsilon_{i}(\lambda_{1}-\lambda_{k},\dots,\lambda_{n}-\lambda_{k}). |  |

###### Proposition 2.3.

Let f f be a CA-polynomial with roots λ 1, …, λ n \lambda_{1},\dots,\lambda_{n}. The following are equivalent

1. 1.

f f is a CA-polynomial.

2. 2.

The roots of f f satisfies the polynomial equations,

 | f ( i) ( x 1) … f ( i) ( x n) = 0, i = 1, …, n − 1. f^{(i)}(x_{1})\dots f^{(i)}(x_{n})=0,\quad i=1,\dots,n-1. |  |

3. 3.

For all i = 1, …, n − 1 i=1,\dots,n-1,

 | ϵ n − i 1 ​ … ​ ϵ n − i n = 0. \epsilon_{n-i}^{1}\dots\epsilon_{n-i}^{n}=0. |  |

4. 4.

There exists a function φ: { 1, …, n − 1 } → { 1, …, n } \varphi:\{1,\dots,n-1\}\to\{1,\dots,n\} such that

 | ϵ 1 φ ⁡ ( 1) = ⋯ = ϵ n − 1 φ ⁡ ( n − 1) = 0. \epsilon_{1}^{\varphi(1)}=\dots=\epsilon_{n-1}^{\varphi(n-1)}=0. |  |

###### Proof.

Let us prove the equivalence between 1 1 and 4 4. Let f f be a CA-polynomial. Given that res ⁡ ( f, f ( i)) = 0 \res(f,f^{(i)})=0, there exists some root λ k \lambda_{k} such that f ( i) ​ ( λ k) = 0 f^{(i)}(\lambda_{k})=0. Hence, writing

 | f ⁡ ( λ k + h) = f ⁡ ( λ k) + h ​ f ( 1) ​ ( λ k) + h 2 2! ​ f ( 2) ​ ( λ k) + ⋯ + h n n! ​ f ( n) ​ ( λ k), f(\lambda_{k}+h)=f(\lambda_{k})+hf^{(1)}(\lambda_{k})+\frac{h^{2}}{2!}f^{(2)}(\lambda_{k})+\dots+\frac{h^{n}}{n!}f^{(n)}(\lambda_{k}), |  |

we get that the coefficient of the monomial h i h^{i} is zero. But, given that the roots of f ⁡ ( h + λ k) f(h+\lambda_{k}) are { λ 1 − λ k, …, λ n − λ k } \{\lambda_{1}-\lambda_{k},\dots,\lambda_{n}-\lambda_{k}\}, it follows that the coefficient of h i h^{i} is equal to ϵ n − i k \epsilon_{n-i}^{k}. Hence,

 | ϵ n − i ​ ( λ 1 − λ k, …, λ n − λ k) = 0. \epsilon_{n-i}(\lambda_{1}-\lambda_{k},\dots,\lambda_{n}-\lambda_{k})=0. |  |

Now, let f f be a degree n n complex polynomial and assume that there exists a function φ: { 1, …, n − 1 } → { 1, …, n } \varphi:\{1,\dots,n-1\}\to\{1,\dots,n\} such that ϵ i ​ ( λ 1 − λ φ ⁡ ( i), …, λ n − λ φ ⁡ ( i)) = 0 \epsilon_{i}(\lambda_{1}-\lambda_{\varphi(i)},\dots,\lambda_{n}-\lambda_{\varphi(i)})=0 for 1 ≤ i ≤ n − 1 1\leq i\leq n-1. Then, the polynomial f ⁡ ( λ φ ⁡ ( i) + h) f(\lambda_{\varphi(i)}+h) do not have the monomial h n − i h^{n-i}. Hence, taking derivatives n − i n-i times and evaluating at h = 0 h=0, we get f ( n − i) ​ ( λ φ ⁡ ( i)) = 0 f^{(n-i)}(\lambda_{\varphi(i)})=0. In other words, res ⁡ ( f, f ( n − i)) = 0 \res(f,f^{(n-i)})=0. ∎

###### Remark 2.4.

Another way to express ϵ n − i ​ ( λ 1 − λ k, …, λ n − λ k) \epsilon_{n-i}(\lambda_{1}-\lambda_{k},\dots,\lambda_{n}-\lambda_{k}) is by using the fact that it is equal to f ( i) ​ ( λ k) / i! f^{(i)}(\lambda_{k})/i!,

 | f ⁡ ( x) = ∑ j ≥ 0 n ( − 1) n − j ​ ϵ n − j ​ ( λ 1, …, λ n) ​ x j ⟹ f ( i) ​ ( λ k) i! = ∑ j ≥ i n ( j i) ​ ( − 1) n − j ​ ϵ n − j ​ ( λ 1, …, λ n) ​ λ k j − i. f(x)=\sum_{j\geq 0}^{n}(-1)^{n-j}\epsilon_{n-j}(\lambda_{1},\dots,\lambda_{n})x^{j}\Longrightarrow\frac{f^{(i)}(\lambda_{k})}{i!}=\sum_{j\geq i}^{n}\binom{j}{i}(-1)^{n-j}\epsilon_{n-j}(\lambda_{1},\dots,\lambda_{n})\lambda_{k}^{j-i}. |  |

Then, for 1 ≤ i ≤ n − 1 1\leq i\leq n-1 and 1 ≤ k ≤ n 1\leq k\leq n,

 | ϵ n − i ​ ( λ 1 − λ k, …, λ n − λ k) = ∑ j ≥ i n ( j i) ​ ( − 1) n − j ​ ϵ n − j ​ ( λ 1, …, λ n) ​ λ k j − i. \epsilon_{n-i}(\lambda_{1}-\lambda_{k},\dots,\lambda_{n}-\lambda_{k})=\sum_{j\geq i}^{n}\binom{j}{i}(-1)^{n-j}\epsilon_{n-j}(\lambda_{1},\dots,\lambda_{n})\lambda_{k}^{j-i}. |  |

###### Remark 2.5.

Given that the polynomials

 | ϵ 1 1 ​ … ​ ϵ 1 n, …, ϵ n − 1 1 ​ … ​ ϵ n − 1 n \epsilon_{1}^{1}\dots\epsilon_{1}^{n},\quad\dots,\quad\epsilon_{n-1}^{1}\dots\epsilon_{n-1}^{n} |  |

are symmetric in { λ 1, …, λ n } \{\lambda_{1},\dots,\lambda_{n}\} we can rewrite them as polynomials in the elementary symmetric polynomials { ϵ 0, …, ϵ n − 1 } \{\epsilon_{0},\dots,\epsilon_{n-1}\}, or equivalently, in the coefficients of f = x n + a n − 1 ​ x n − 1 + ⋯ + a 0 f=x^{n}+a_{n-1}x^{n-1}+\dots+a_{0}. The resulting polynomials are precisely the resultants,

 | res ⁡ ( f, f ( i) / i!), 1 ≤ i ≤ n − 1. \res(f,f^{(i)}/i!),\quad 1\leq i\leq n-1. |  |

Indeed, the determinant of f ( i) ​ ( F) / i! f^{(i)}(F)/i!, where F F is the companion matrix of f f, is equal to res ⁡ ( f, f ( i) / i!) \res(f,f^{(i)}/i!), but also, is equal to f ( i) ​ ( λ 1) / i! ​ … ​ f ( i) ​ ( λ n) / i! f^{(i)}(\lambda_{1})/i!\dots f^{(i)}(\lambda_{n})/i!.

## 3 Abel-Gontcharoff polynomials

In this section we review some known results about Abel-Gontcharoff polynomials that can be found in [13].

###### Definition 3.1.

The Abel-Gontcharoff polynomial of degree 0 0 is G ⁡ ( x) = 1 G(x)=1 and the Abel-Gontcharoff polynomial of degree n ≥ 1 n\geq 1 is defined as

 | G ⁡ ( x, y 0, …, y n − 1) = ( − 1) n ​ n! ​ ∫ y 0 x d ​ t 1 ​ ∫ y 1 t 1 d ​ t 2 ​ … ​ ∫ y n − 1 t n − 1 d ​ t n, n ≥ 1. G(x;y_{0},\dots,y_{n-1})=(-1)^{n}n!\int_{y_{0}}^{x}dt_{1}\int_{y_{1}}^{t_{1}}dt_{2}\dots\int_{y_{n-1}}^{t_{n-1}}dt_{n},\quad n\geq 1. |  |

The normalizing factor of ( − 1) n ​ n! (-1)^{n}n! is not present in [13].

###### Lemma 3.2.

. Let G ⁡ ( x, y 0, …, y n − 1) ∈ ℤ ⁡ [x, y 0, …, y n − 1, c] G(x;y_{0},\dots,y_{n-1})\in\mathbb{Z}[x,y_{0},\dots,y_{n-1},c] be the degree n ≥ 1 n\geq 1 Abel-Gontcharoff polynomial and c c a new variable. Then,

- 1.

G ⁡ ( y 0, y 0, …, y n − 1) = 0 G(y_{0};y_{0},\dots,y_{n-1})=0.

- 2.

G ⁡ ( x, y 0, …, y n − 1) G(x;y_{0},\dots,y_{n-1}) is homogeneous of degree n n and

 | G ⁡ ( x + c, y 0 + c, …, y n − 1 + c) = G ⁡ ( x, y 0, …, y n − 1). G(x+c;y_{0}+c,\dots,y_{n-1}+c)=G(x;y_{0},\dots,y_{n-1}). |  |

- 3.

 | 1 k! ​ ∂ k G ⁡ ( x, y 0, …, y n − 1) ∂ x k = ( n k) ​ G ​ ( x, y k, …, y n − 1) \frac{1}{k!}\frac{\partial^{k}G(x;y_{0},\dots,y_{n-1})}{\partial x^{k}}=\binom{n}{k}G(x;y_{k},\dots,y_{n-1}) |  |

In particular, if f ⁡ ( x) = G ⁡ ( x, y 0, …, y n − 1) f(x)=G(x;y_{0},\dots,y_{n-1}), then f ( k) ​ ( y k) = 0 f^{(k)}(y_{k})=0.

- 4.

G ⁡ ( x, y 0, …, y n − 1) G(x;y_{0},\dots,y_{n-1}) is a monic polynomial in x x,

- 5.

 | ∂ G ⁡ ( x, y 0, …, y n − 1) ∂ y k = − n ​ ( n − 1 k) ​ G ​ ( x, y 0, …, y k − 1) ​ G ​ ( y k, y k + 1, …, y n − 1) \frac{\partial G(x;y_{0},\dots,y_{n-1})}{\partial y_{k}}=-n\binom{n-1}{k}G(x;y_{0},\dots,y_{k-1})G(y_{k};y_{k+1},\dots,y_{n-1}) |  |

###### Proof.

The first assertion follows from the definition. The second, third and fifth assertion are proven in [13, §2,§3]. The fourth assertion follows by computing ∂ n G / ∂ x n \partial^{n}G/\partial x^{n} and dividing by n! n!. ∎

###### Corollary 3.3.

Let G ⁡ ( x, y 0, …, y n − 1) ∈ ℤ ⁡ [x, y 0, …, y n − 1, c] G(x;y_{0},\dots,y_{n-1})\in\mathbb{Z}[x,y_{0},\dots,y_{n-1},c] be the degree n ≥ 1 n\geq 1 Abel-Gontcharoff polynomial, c c a new variable and let 0 ≤ k < n 0\leq k<n. Then,

 | G ⁡ ( x, y 0, …, y n − 1) − G ⁡ ( x, y 0, …, y k − 1, c, y k + 1, …, y n − 1) = ( n k) ​ G ​ ( x, y 0, …, y k − 1) ​ G ​ ( c, y k, …, y n − 1). G(x;y_{0},\dots,y_{n-1})-G(x;y_{0},\dots,y_{k-1},c,y_{k+1},\dots,y_{n-1})=\binom{n}{k}G(x;y_{0},\dots,y_{k-1})G(c;y_{k},\dots,y_{n-1}). |  |

###### Proof.

The result follows by integrating an identity from Lemma 3.2,

 | G ⁡ ( x, y 0, …, y n − 1) \displaystyle G(x;y_{0},\dots,y_{n-1}) | − G ⁡ ( x, y 0, …, y k − 1, c, y k + 1, …, y n − 1) \displaystyle-G(x;y_{0},\dots,y_{k-1},c,y_{k+1},\dots,y_{n-1}) |  |

 |  | = ∫ c y k ∂ G ⁡ ( x, y 0, …, y n − 1) ∂ y k ​ d ​ y k \displaystyle=\int_{c}^{y_{k}}\frac{\partial G(x;y_{0},\dots,y_{n-1})}{\partial y_{k}}dy_{k} |  |

 |  | = − ∫ c y k n ( n − 1 k) G ( x; y 0, …, y k − 1) G ( y k; y k + 1, …, y n − 1) d y k \displaystyle=-\int_{c}^{y_{k}}n\binom{n-1}{k}G(x;y_{0},\dots,y_{k-1})G(y_{k};y_{k+1},\dots,y_{n-1})dy_{k} |  |

 |  | = − n ( n − 1 k) G ( x; y 0, …, y k − 1) ∫ c y k G ( y k; y k + 1, …, y n − 1) d y k \displaystyle=-n\binom{n-1}{k}G(x;y_{0},\dots,y_{k-1})\int_{c}^{y_{k}}G(y_{k};y_{k+1},\dots,y_{n-1})dy_{k} |  |

 |  | = − n n − k ​ ( n − 1 k) ​ G ​ ( x, y 0, …, y k − 1) ​ ( G ⁡ ( y k, y k, y k + 1, …, y n − 1) − G ⁡ ( c, y k, y k + 1, …, y n − 1)) \displaystyle=-\frac{n}{n-k}\binom{n-1}{k}G(x;y_{0},\dots,y_{k-1})\left(G(y_{k};y_{k},y_{k+1},\dots,y_{n-1})-G(c;y_{k},y_{k+1},\dots,y_{n-1})\right) |  |

 |  | = ( n k) ​ G ​ ( x, y 0, …, y k − 1) ​ G ​ ( c, y k, y k + 1, …, y n − 1). \displaystyle=\binom{n}{k}G(x;y_{0},\dots,y_{k-1})G(c;y_{k},y_{k+1},\dots,y_{n-1}). |  |

∎

###### Remark 3.4.

From Corollary 3.3 it follows that if λ \lambda is a root of f = G ⁡ ( x, y 0, …, y n − 1) f=G(x;y_{0},\dots,y_{n-1}), then we have the divisibility

 | f ( k) ​ ( c) | G ⁡ ( λ, y 0, …, y k − 1, c, y k + 1, …, y n − 1) f^{(k)}(c)\,\big|\,G(\lambda;y_{0},\dots,y_{k-1},c,y_{k+1},\dots,y_{n-1}) |  |

as polynomials in c c.

###### Proposition 3.5.

Let G ⁡ ( x, y 0, …, y n − 1) ∈ ℤ ⁡ [x, y 0, …, y n − 1, c 0, …, c n − 1] G(x;y_{0},\dots,y_{n-1})\in\mathbb{Z}[x,y_{0},\dots,y_{n-1},c_{0},\dots,c_{n-1}] be the degree n ≥ 1 n\geq 1 Abel-Gontcharoff polynomial. Then,

 | G ⁡ ( x, y 0, …, y n − 1) = G ⁡ ( x, c 0, …, c n − 1) + ∑ i = 0 n − 1 ( n i) ​ G ​ ( x, c 0, …, c i − 1) ​ G ​ ( c i, y i, …, y n − 1). G(x;y_{0},\dots,y_{n-1})=G(x;c_{0},\dots,c_{n-1})+\sum_{i=0}^{n-1}\binom{n}{i}G(x;c_{0},\dots,c_{i-1})G(c_{i};y_{i},\dots,y_{n-1}). |  |

Furthermore,

 | ( n − k)! n! ​ ∂ k G ⁡ ( x, y 0, …, y n − 1) ∂ x k = G ⁡ ( x, c k, …, c n − 1) + ∑ i = k n − 1 ( n − k i − k) ​ G ​ ( x, c k, …, c i − 1) ​ G ​ ( c i, y i, …, y n − 1). \frac{(n-k)!}{n!}\frac{\partial^{k}G(x;y_{0},\dots,y_{n-1})}{\partial x^{k}}=G(x;c_{k},\dots,c_{n-1})+\sum_{i=k}^{n-1}\binom{n-k}{i-k}G(x;c_{k},\dots,c_{i-1})G(c_{i};y_{i},\dots,y_{n-1}). |  |

###### Proof.

Applying Corollary 3.3 for 0 ≤ i < n 0\leq i<n we get,

 | G ⁡ ( x, c 0, …, c i − 1, y i, …, y n − 1) \displaystyle G(x;c_{0},\dots,c_{i-1},y_{i},\dots,y_{n-1}) | − G ⁡ ( x, c 0, …, c i − 1, c i, y i + 1 ​ …, y n − 1) \displaystyle-G(x;c_{0},\dots,c_{i-1},c_{i},y_{i+1}\dots,y_{n-1}) |  |

 |  | = ( n i) ​ G ​ ( x, c 0, …, c i − 1) ​ G ​ ( c i, y i, …, y n − 1). \displaystyle=\binom{n}{i}G(x;c_{0},\dots,c_{i-1})G(c_{i},y_{i},\dots,y_{n-1}). |  |

The first formula follows by taking an alternated sum. The formula for the derivative is obtained by using the identities from Lemma 3.2 and the identity

 | ( n k) ​ ( n − k i − k) = ( i k) ​ ( n i). \binom{n}{k}\binom{n-k}{i-k}=\binom{i}{k}\binom{n}{i}. |  |

∎

###### Remark 3.6.

Taking c 0 = ⋯ = c n − 1 = 0 c_{0}=\dots=c_{n-1}=0 in the previous Proposition, we recover the standard writing,

 | G ⁡ ( x, y 0, …, y n − 1) = x n + ∑ i = 0 n − 1 ( n i) ​ x i ​ b i, b i = G ⁡ ( 0, y i, …, y n − 1). G(x;y_{0},\dots,y_{n-1})=x^{n}+\sum_{i=0}^{n-1}\binom{n}{i}x^{i}b_{i},\quad b_{i}=G(0;y_{i},\dots,y_{n-1}). |  |

## 4 The conjecture

###### Definition 4.1.

Let us define three different schemes over ℤ \mathbb{Z}. The root schemes ( [8, §5.1]), the coefficients scheme ( [9, §2]) and the Abel-Gontcharoff scheme. The *root scheme*ℛ ⊆ ℙ n − 1 \mathcal{R}\subseteq\mathbb{P}^{n-1} is defined by the ideal

 | ⟨ ϵ n − i 1 ( λ 1, …, λ n) … ϵ n − i n ( λ 1, …, λ n), i = 1, …, n − 1 ⟩ ⊆ ℤ [λ 1, …, λ n], \langle\epsilon_{n-i}^{1}(\lambda_{1},\dots,\lambda_{n})\dots\epsilon_{n-i}^{n}(\lambda_{1},\dots,\lambda_{n}),\quad i=1,\dots,n-1\rangle\subseteq\mathbb{Z}[\lambda_{1},\dots,\lambda_{n}], |  |

the *Abel-Gontcharoff scheme*𝒢 ⊆ ℙ n − 1 \mathcal{G}\subseteq\mathbb{P}^{n-1} is defined by the ideal

 | ⟨ G ( y k; y 0, …, y n − 1), k = 1, …, n − 1 ⟩ ⊆ ℤ [y 0, …, y n − 1] \langle G(y_{k};y_{0},\dots,y_{n-1}),\quad k=1,\dots,n-1\rangle\subseteq\mathbb{Z}[y_{0},\dots,y_{n-1}] |  |

and the *coefficients scheme*𝒳 ⊆ ℙ ⁡ ( n, n − 1, …, 1) \mathcal{X}\subseteq\mathbb{P}(n,n-1,\dots,1) is a weighted projective scheme defined by the ideal

 | ⟨ res ( P, H k ( P)), k = 1, …, n − 1 ⟩ ⊆ ℤ [a 0, …, a n − 1] \langle\res(P,H_{k}(P)),\quad k=1,\dots,n-1\rangle\subseteq\mathbb{Z}[a_{0},\dots,a_{n-1}] |  |

where P = x n + a n − 1 ​ x n − 1 + ⋯ + a 1 ​ x + a 0 ∈ ℤ ⁡ [a 0, …, a n − 1] ​ [x] P=x^{n}+a_{n-1}x^{n-1}+\dots+a_{1}x+a_{0}\in\mathbb{Z}[a_{0},\dots,a_{n-1}][x].

Notice that any point in ℛ ⁡ ( ℂ) \mathcal{R}(\mathbb{C}) or in 𝒢 ⁡ ( ℂ) \mathcal{G}(\mathbb{C}) or in 𝒳 ⁡ ( ℂ) \mathcal{X}(\mathbb{C}) defines a polynomial f f such that f ( k) ​ ( y k) = f ⁡ ( y k) = 0 f^{(k)}(y_{k})=f(y_{k})=0 for all k = 0, …, n − 1 k=0,\dots,n-1, that is, a CA-polynomial.

###### Proposition 4.2.

The dimensions of ℛ \mathcal{R}, 𝒢 \mathcal{G} and 𝒳 \mathcal{X} coincide.

###### Proof.

Let us define two maps ϕ 1: ℛ → 𝒳 \phi_{1}:\mathcal{R}\to\mathcal{X} and ϕ 2: 𝒢 → 𝒳 \phi_{2}:\mathcal{G}\to\mathcal{X},

 | ϕ 1 ( λ 1: …: λ n):= \displaystyle\phi_{1}(\lambda_{1}:\dots:\lambda_{n}):= | ( ϵ n ( λ 1, …, λ n): …: ϵ 1 ( λ 1, …, λ n)), \displaystyle\left(\epsilon_{n}(\lambda_{1},\dots,\lambda_{n}):\dots:\epsilon_{1}(\lambda_{1},\dots,\lambda_{n})\right), |  |

 | ϕ 2 ( y 0: …: y n − 1):= \displaystyle\phi_{2}(y_{0}:\dots:y_{n-1}):= | ( ( n 0) G ( 0; y 0, …, y n − 1): …: ( n n − 2) G ( 0; y n − 2, y n − 1): ( n n − 1) G ( 0; y n − 1)). \displaystyle\left(\binom{n}{0}G(0;y_{0},\dots,y_{n-1}):\dots:\binom{n}{n-2}G(0;y_{n-2},y_{n-1}):\binom{n}{n-1}G(0;y_{n-1})\right). |  |

The result follows by noting that these two maps are finite and surjective. ∎

###### Proposition 4.3.

The following are equivalent

1. 1.

The Casas-Alvero conjecture is true.

2. 2.

The cardinal of ℛ ⁡ ( ℂ) \mathcal{R}(\mathbb{C}) is 1 1.

3. 3.

The dimension of ℛ ⁡ ( ℂ) \mathcal{R}(\mathbb{C}) is zero.

4. 4.

{ ϵ i 1 ​ … ​ ϵ i n: 1 ≤ i ≤ n − 1 } \{\epsilon_{i}^{1}\dots\epsilon_{i}^{n}\colon 1\leq i\leq n-1\} is a regular sequence over ℂ ⁡ [λ 1, …, λ n] \mathbb{C}[\lambda_{1},\dots,\lambda_{n}].

5. 5.

ℛ ⁡ ( ℂ) \mathcal{R}(\mathbb{C}) is finite.

###### Proof.

Let us prove 1 1 implies 2 2 and 5 5 implies 1 1. The other implications i i implies i + 1 i+1 are clear, 2 ≤ i ≤ 4 2\leq i\leq 4. Assume the Casas-Alvero conjecture is true and let ( λ 1: …: λ n) ∈ ℛ ( ℂ) (\lambda_{1}:\dots:\lambda_{n})\in\mathcal{R}(\mathbb{C}). Then, from Proposition 2.3, the polynomial ( x − λ 1) ​ … ​ ( x − λ n) (x-\lambda_{1})\dots(x-\lambda_{n}) is a CA-polynomial and from the hypothesis, ( λ 1: …: λ n) = ( 1: …: 1) (\lambda_{1}:\dots:\lambda_{n})=(1:\dots:1).

Assume now that ℛ ⁡ ( ℂ) \mathcal{R}(\mathbb{C}) is finite and let f f be a CA-polynomial of degree n n. Then, from Proposition 2.3 the roots of f f determine a point ( λ 1: …: λ n) ∈ ℛ ( ℂ) (\lambda_{1}:\dots:\lambda_{n})\in\mathcal{R}(\mathbb{C}). But f ⁡ ( x + b) f(x+b) is also a CA-polynomial for all b ∈ ℂ b\in\mathbb{C}. Then,

 | ( λ 1 − b: …: λ n − b) ∈ ℛ ( ℂ), ∀ b ∈ ℂ. (\lambda_{1}-b:\dots:\lambda_{n}-b)\in\mathcal{R}(\mathbb{C}),\quad\forall b\in\mathbb{C}. |  |

From the finiteness of ℛ ⁡ ( ℂ) \mathcal{R}(\mathbb{C}), it follows necessarily λ 1 = ⋯ = λ n \lambda_{1}=\dots=\lambda_{n}. ∎

###### Remark 4.4.

From the previous proof we deduce that ℛ ⁡ ( ℂ) \mathcal{R}(\mathbb{C}) is a cone with vertex ( 1: …: 1) (1:\dots:1). In other words, if p ∈ ℛ ⁡ ( ℂ) p\in\mathcal{R}(\mathbb{C}), then the line joining p p and ( 1: …: 1) (1:\dots:1) is contained in ℛ ⁡ ( ℂ) \mathcal{R}(\mathbb{C}). Indeed, if ( s: t) ∈ ℙ 1 ​ ( ℂ) (s:t)\in\mathbb{P}^{1}(\mathbb{C}) and t ≠ 0 t\neq 0,

 | ( s + t p 0: …: s + t p n) = ( s / t + p 0: …: s / t + p n) ∈ ℛ ( ℂ). (s+tp_{0}:\dots:s+tp_{n})=(s/t+p_{0}:\dots:s/t+p_{n})\in\mathcal{R}(\mathbb{C}). |  |

The last containment follows from the fact that if f = ( x − p 0) ​ … ​ ( x − p n) f=(x-p_{0})\dots(x-p_{n}) is a CA-polynomial, then f ⁡ ( x − s / t) f(x-s/t) is also a CA-polynomial. The same argument implies that 𝒢 ⁡ ( ℂ) \mathcal{G}(\mathbb{C}), 𝒢 ⁡ ( K) \mathcal{G}(K) and ℛ ⁡ ( K) \mathcal{R}(K) are also cones for any field K K.

## 5 First result

In this section we prove that if n = p s + r + p s n=p^{s+r}+p^{s} or n = p s + r + 2 ​ p s n=p^{s+r}+2p^{s} then dim ℛ ⁡ ( ℂ) ≤ 1 \dim\mathcal{R}(\mathbb{C})\leq 1.

###### Lemma 5.1.

Let K K be a field of characteristic p p and let n = p r + 1 n=p^{r}+1. Then,

 | ( n k) = 0, 2 ≤ k ≤ n − 2. \binom{n}{k}=0,\quad 2\leq k\leq n-2. |  |

###### Proof.

Notice that n n in base p p is equal to n = 1 + 0 ​ p + ⋯ + 0 ​ p r − 1 + 1 ​ p r n=1+0p+\dots+0p^{r-1}+1p^{r}. Then,

 | ( n k) = ( n 0 k 0) ​ ( n 1 k 1) ​ … ​ ( n r k r) = ( 1 k 0) ​ ( 0 k 1) ​ … ​ ( 0 k r − 1) ​ ( 1 k r). \binom{n}{k}=\binom{n_{0}}{k_{0}}\binom{n_{1}}{k_{1}}\dots\binom{n_{r}}{k_{r}}=\binom{1}{k_{0}}\binom{0}{k_{1}}\dots\binom{0}{k_{r-1}}\binom{1}{k_{r}}. |  |

Given that 2 ≤ k ≤ n − 2 2\leq k\leq n-2, it follows that k r = 0 k_{r}=0 and also that k 0 > 1 k_{0}>1 or some k 1, …, k r − 1 > 0 k_{1},\dots,k_{r-1}>0. In either case, the result follows. ∎

###### Definition 5.2.

Following [8], let us define the k k -th *net derivative*of f f as N k ​ ( f):= H k ​ ( f) / C ⁡ ( n, k) N_{k}(f):=H_{k}(f)/C(n,k), where C ⁡ ( n, k) C(n,k) is the binomial coefficient

 | C ⁡ ( n, k):= ( n k). C(n,k):=\binom{n}{k}. |  |

From the equality C ⁡ ( j, k) ​ C ​ ( n, j) = C ⁡ ( n, k) ​ C ​ ( n − k, j − k) C(j,k)C(n,j)=C(n,k)C(n-k,j-k) and the relations a i = C ⁡ ( n, i) ​ b i a_{i}=C(n,i)b_{i}, i = 1, …, n − 1 i=1,\dots,n-1, it follows N k ​ ( f) ∈ ℤ ⁡ [b k, …, b n − 1] N_{k}(f)\in\mathbb{Z}[b_{k},\dots,b_{n-1}],

 | H k ​ ( f) = \displaystyle H_{k}(f)= | ( n k) ​ x n − k + ( n − 1 k) ​ a n − 1 ​ x n − 1 − k + ⋯ + ( k + 1 k) ​ a k + 1 ​ x + a k \displaystyle\binom{n}{k}x^{n-k}+\binom{n-1}{k}a_{n-1}x^{n-1-k}+\dots+\binom{k+1}{k}a_{k+1}x+a_{k} |  |

 | = \displaystyle= | ( n k) ​ x n − k + ( n − 1 k) ​ ( n n − 1) ​ b n − 1 ​ x n − 1 − k + ⋯ + ( k + 1 k) ​ ( n k + 1) ​ b k + 1 ​ x + ( n k) ​ b k \displaystyle\binom{n}{k}x^{n-k}+\binom{n-1}{k}\binom{n}{n-1}b_{n-1}x^{n-1-k}+\dots+\binom{k+1}{k}\binom{n}{k+1}b_{k+1}x+\binom{n}{k}b_{k} |  |

 | = \displaystyle= | ( n k) ⁡ ( x n − k + ( n − k n − k − 1) ​ b n − 1 ​ x n − 1 − k + ⋯ + ( n − k k + 1 − k) ​ b k + 1 ​ x + b k) \displaystyle\binom{n}{k}\left(x^{n-k}+\binom{n-k}{n-k-1}b_{n-1}x^{n-1-k}+\dots+\binom{n-k}{k+1-k}b_{k+1}x+b_{k}\right) |  |

 | = \displaystyle= | ( n k) ​ N k ​ ( f). \displaystyle\binom{n}{k}N_{k}(f). |  |

###### Definition 5.3.

Consider the field extension ℚ ⊆ ℂ \mathbb{Q}\subseteq\mathbb{C} and let us choose an absolute value | ⋅ | |\cdot| on ℂ \mathbb{C} compatible with the p p -adic absolute value in ℚ \mathbb{Q}. Recall that the closed ball R = { x ∈ ℂ: | x | ≤ 1 } R=\{x\in\mathbb{C}\,\colon\,|x|\leq 1\} is a ring with maximal ideal the open ball 𝔪 = { x ∈ ℂ: | x | < 1 } \mathfrak{m}=\{x\in\mathbb{C}\,\colon\,|x|<1\}. The field K = R / 𝔪 K=R/\mathfrak{m} is of characteristic p p and K = K ¯ K=\overline{K}, [12, XII]. We say that a monic CA-polynomial f f of degree n n is written in *normal form*if all its roots are in R R and if it is written as

 | f = x n − n ​ x n − 1 + ( n n − 2) ​ b n − 2 ​ x n − 2 + ⋯ + ( n 2) ​ b 2 ​ x 2, f=x^{n}-nx^{n-1}+\binom{n}{n-2}b_{n-2}x^{n-2}+\dots+\binom{n}{2}b_{2}x^{2}, |  |

where | b k | ≤ 1 |b_{k}|\leq 1 for k = 2, …, n − 2 k=2,\dots,n-2. According to [4, (3.4)], by applying the transformations f ⁡ ( x − a) f(x-a) and f ⁡ ( b ​ x) / b n f(bx)/b^{n}, we can convert any monic CA-polynomial to a polynomial in normal form.

###### Proposition 5.4.

If dim ℛ ⁡ ( K) = d \dim\mathcal{R}(K)=d, then dim ℛ ⁡ ( ℂ) ≤ d \dim\mathcal{R}(\mathbb{C})\leq d.

###### Proof.

By hypothesis, the fiber of ℛ \mathcal{R} at p p has dimension d d. Given that Spec ⁡ ( ℤ) \spec(\mathbb{Z}) has dimension 1 1, it follows from [14, §4.3.1, Th.3.12] that dim ℛ ≤ d + 1 \dim\mathcal{R}\leq d+1. Hence, by generic flatness [10, Th.6.9.1], the dimension of the generic fiber is less than or equal to d d, dim ℛ ⁡ ( ℚ ¯) ≤ d \dim\mathcal{R}(\overline{\mathbb{Q}})\leq d. Finally, let us prove dim ℛ ⁡ ( ℚ ¯) = dim ℛ ⁡ ( ℂ) \dim\mathcal{R}(\overline{\mathbb{Q}})=\dim\mathcal{R}(\mathbb{C}) by using Noether normalization lemma [1, §5 Ex.16] and the fact that ℂ \mathbb{C} is flat over ℚ ¯ \overline{\mathbb{Q}}. If A A is a finitely generated ℚ ¯ \overline{\mathbb{Q}} -algebra, then there exists a polynomial ring P P such that P ⊆ A P\subseteq A and A A is a finitely generated P P -module. Tensoring by ℂ \mathbb{C}, it follows that P ℂ ⊆ A ℂ P_{\mathbb{C}}\subseteq A_{\mathbb{C}} and A ℂ A_{\mathbb{C}} is a finitely generated P ℂ P_{\mathbb{C}} -module. Hence,

 | dim ( A) = dim ( P) = dim ( P ℂ) = dim ( A ℂ). \dim(A)=\dim(P)=\dim(P_{\mathbb{C}})=\dim(A_{\mathbb{C}}). |  |

∎

###### Lemma 5.5.

Any CA-polynomials of degree n = p r + 1 n=p^{r}+1 in normal form has one simple root equal to 1 1 and the other roots in 𝔪 \mathfrak{m}.

###### Proof.

The class of f = x n − n ​ x n − 1 + C ⁡ ( n, n − 2) ​ b n − 2 ​ x n − 2 + ⋯ + C ⁡ ( n, 2) ​ b 2 ​ x 2 f=x^{n}-nx^{n-1}+C(n,n-2)b_{n-2}x^{n-2}+\dots+C(n,2)b_{2}x^{2} in K K is equal to ( x − 1) ​ x n − 1 (x-1)x^{n-1}. ∎

###### Lemma 5.6.

Assume p > 2 p>2. The only CA-polynomial in normal form of degree n = p r + 2 n=p^{r}+2 in K ⁡ [x] K[x] is

 | x n − 2 ​ ( x − 1) 2. x^{n-2}(x-1)^{2}. |  |

###### Proof.

As in Lemma 5.1, C ⁡ ( n, k) = 0 C(n,k)=0 for 3 ≤ k ≤ n − 3 3\leq k\leq n-3, C ⁡ ( n, 2) = C ⁡ ( n, n − 2) = 1 C(n,2)=C(n,n-2)=1 and C ⁡ ( n, n − 1) = 2 C(n,n-1)=2. Then, any CA-polynomial in normal form over K ⁡ [x] K[x] can be written as

 | f = x n − 2 ​ x n − 1 + b n − 2 ​ x n − 2 + b 2 ​ x 2. f=x^{n}-2x^{n-1}+b_{n-2}x^{n-2}+b_{2}x^{2}. |  |

Two of its net derivatives are N 2 ​ ( f) = x n − 2 + b 2 N_{2}(f)=x^{n-2}+b_{2} and N n − 2 ​ ( f) = x 2 − 2 ​ x + b n − 2 N_{n-2}(f)=x^{2}-2x+b_{n-2}. In order to compute the resultants, let us factorize the derivatives. If α n − 2 = b 2 \alpha^{n-2}=b_{2}, then N 2 ​ ( f) = ( x + α) n − 2 N_{2}(f)=(x+\alpha)^{n-2} and it follows res ⁡ ( f, N 2 ​ ( f)) = f ​ ( − α) n − 2 \res(f,N_{2}(f))=f(-\alpha)^{n-2}. Given that N n − 1 ​ ( f) = x − 1 N_{n-1}(f)=x-1, we have res ⁡ ( f, N n − 1 ​ ( f)) = f ⁡ ( 1) \res(f,N_{n-1}(f))=f(1). Finally, if N n − 2 ​ ( f) = ( x − 1 − β) ​ ( x − 1 + β) N_{n-2}(f)=(x-1-\beta)(x-1+\beta), then res ⁡ ( f, N n − 2 ​ ( f)) = f ⁡ ( 1 + β) ​ f ​ ( 1 − β) \res(f,N_{n-2}(f))=f(1+\beta)f(1-\beta). Summing up,

 | res ⁡ ( f, N 2 ​ ( f)) = b 2 n − 2 ​ b n − 2 n − 2 + 2 ​ b 2 n − 1, res ⁡ ( f, N n − 2 ​ ( f)) = b 2 2 ​ b n − 2 2, res ⁡ ( f, N n − 1 ​ ( f)) = − 1 + b n − 2 + b 2. \res(f,N_{2}(f))=b_{2}^{n-2}b_{n-2}^{n-2}+2b_{2}^{n-1},\quad\res(f,N_{n-2}(f))=b_{2}^{2}b_{n-2}^{2},\quad\res(f,N_{n-1}(f))=-1+b_{n-2}+b_{2}. |  |

Then, the only possibility is f = x n − 2 ​ x n − 1 + x n − 2 f=x^{n}-2x^{n-1}+x^{n-2}. ∎

###### Theorem 5.7.

The following statements are true

1. 1.

If there exists a finite number of CA-polynomials in normal form of degree n n in K ⁡ [x] K[x], then dim ℛ ⁡ ( ℂ) ≤ 1 \dim\mathcal{R}(\mathbb{C})\leq 1.

2. 2.

Let r r be a positive integer. If n = p r + 1 n=p^{r}+1, then dim ℛ ⁡ ( ℂ) ≤ 1 \dim\mathcal{R}(\mathbb{C})\leq 1.

3. 3.

Let r, s r,s be a positive integers. If n = p s + r + p s n=p^{s+r}+p^{s}, then dim ℛ ⁡ ( ℂ) ≤ 1 \dim\mathcal{R}(\mathbb{C})\leq 1.

4. 4.

Let r r be a positive integer. If n = p r + 2 n=p^{r}+2, then dim ℛ ⁡ ( ℂ) ≤ 1 \dim\mathcal{R}(\mathbb{C})\leq 1.

5. 5.

Let r, s r,s be a positive integers. If n = p s + r + 2 ​ p s n=p^{s+r}+2p^{s}, then dim ℛ ⁡ ( ℂ) ≤ 1 \dim\mathcal{R}(\mathbb{C})\leq 1.

###### Proof.

The hypothesis of the first statement implies dim ℛ ⁡ ( K) = 1 \dim\mathcal{R}(K)=1. The second statement follows from Lemma 5.5 which implies that there is only one CA-polynomial in K ⁡ [x] K[x]. For the third statement we deduce from [9, Prop.26] (or [7, Prop.9]), that there is also one CA-polynomial in K K equal to ( ( x − 1) ​ x p r) p s ((x-1)x^{p^{r}})^{p^{s}}. The last two statements follow from Lemma 5.6. ∎

###### Remark 5.8.

For n = p s + r + p s n=p^{s+r}+p^{s} or n = p s + r + 2 ​ p s n=p^{s+r}+2p^{s}, we deduce from Theorem 5.7 that if ℛ ⁡ ( ℂ) \mathcal{R}(\mathbb{C}) is not a point, then it is a finite union of lines joined at ( 1: …: 1) (1:\dots:1). Hence, we can apply this result to several of the cases listed in [4, 6.5],

 | 20, 24, 28, 30, 35, 36, 40, 42, 45, 48, 55, 56, 60, 63, 66, 70, 72, 77, 78, 80, 84, 88, 90, 91, 98, 99, 100. \begin{matrix}20,24,28,30,35,36,40,42,45,48,55,56,60,\\ 63,66,70,72,77,78,80,84,88,90,91,98,99,100.\end{matrix} |  |

For example, if n ∈ { 20, 24, 28, 30, 40, 56, 66, 35, 45, 99 } n\in\{20,24,28,30,40,56,66,35,45,99\}, then dim ℛ ⁡ ( ℂ) ≤ 1 \dim\mathcal{R}(\mathbb{C})\leq 1. Indeed,

 | 20 = 2 2 + 2 4 = 1 + 19, 24 = 1 + 23 = 2 3 + 2 4, 28 = 1 + 3 3, 30 = 3 + 3 3 = 5 + 5 2 = 1 + 29, 40 = 2 3 + 2 5, 56 = 7 + 7 2, 66 = 2 + 2 6, 35 = 2.5 + 5 2, 45 = 2.3 2 + 3 3 = 2 + 43, 99 = 2 + 97 = 2.3 2 + 3 4. \begin{matrix}20=2^{2}+2^{4}=1+19,&24=1+23=2^{3}+2^{4},&28=1+3^{3},\\ 30=3+3^{3}=5+5^{2}=1+29,&40=2^{3}+2^{5},&56=7+7^{2},\\ 66=2+2^{6},&35=2.5+5^{2},&45=2.3^{2}+3^{3}=2+43,\\ 99=2+97=2.3^{2}+3^{4}.\end{matrix} |  |

This result bounds the dimension of all the cases listed except for n ∈ { 70, 77, 78, 88, 100 } n\in\{70,77,78,88,100\}.

## 6 Second result

In this section we prove that the coefficients of a CA-polynomial of degree n = p r + 1 n=p^{r}+1 in normal form are in ℚ ¯ \overline{\mathbb{Q}}.

###### Lemma 6.1.

Let f ∈ ℂ ⁡ [x] f\in\mathbb{C}[x] be a monic CA-polynomial of degree n n with roots λ 1, …, λ n \lambda_{1},\dots,\lambda_{n} and let σ \sigma be a complex automorphism over ℚ \mathbb{Q}, [11]. Then, f σ f^{\sigma} is another monic CA-polynomial of the same degree with roots σ ⁡ ( λ 1), …, σ ⁡ ( λ n) \sigma(\lambda_{1}),\dots,\sigma(\lambda_{n}). Clearly, if λ ∈ ℚ \lambda\in\mathbb{Q}, then σ ⁡ ( λ) = λ \sigma(\lambda)=\lambda.

###### Proof.

If f = x n + a n − 1 ​ x n − 1 + ⋯ + a 1 ​ x + a 0 f=x^{n}+a_{n-1}x^{n-1}+\dots+a_{1}x+a_{0}, then f σ = x n + σ ⁡ ( a n − 1) ​ x n − 1 + ⋯ + σ ⁡ ( a 1) ​ x + σ ⁡ ( a 0) f^{\sigma}=x^{n}+\sigma(a_{n-1})x^{n-1}+\dots+\sigma(a_{1})x+\sigma(a_{0}). Then,

 | H k ​ ( f σ) = H k ​ ( f) σ = ( n k) ​ x n − k + ( n − 1 k) ​ σ ​ ( a n − 1) ​ x n − 1 − k + ⋯ + ( k + 1 k) ​ σ ​ ( a k + 1) ​ x + σ ⁡ ( a k). H_{k}(f^{\sigma})=H_{k}(f)^{\sigma}=\binom{n}{k}x^{n-k}+\binom{n-1}{k}\sigma(a_{n-1})x^{n-1-k}+\dots+\binom{k+1}{k}\sigma(a_{k+1})x+\sigma(a_{k}). |  |

Now, if λ \lambda is a root of f f, it is easy to check that σ ⁡ ( λ) \sigma(\lambda) is a root of f σ f^{\sigma},

 | f σ ​ ( σ ⁡ ( λ)) = ∑ i = 0 n σ ⁡ ( a i) ​ σ ​ ( λ) i = σ ⁡ ( ∑ i = 0 n a i ​ λ i) = σ ⁡ ( f ⁡ ( λ)) = 0. f^{\sigma}(\sigma(\lambda))=\sum_{i=0}^{n}\sigma(a_{i})\sigma(\lambda)^{i}=\sigma\left(\sum_{i=0}^{n}a_{i}\lambda^{i}\right)=\sigma(f(\lambda))=0. |  |

Finally, if f f is a CA-polynomial in normal form, it follows from above that f σ f^{\sigma} is also a CA-polynomial in normal form. ∎

###### Theorem 6.2.

Let f ∈ ℂ ⁡ [x] f\in\mathbb{C}[x] be a CA-polynomial of degree n = p r + 1 n=p^{r}+1 in normal form. Then, f ∈ ℚ ¯ ​ [x] f\in\overline{\mathbb{Q}}[x].

###### Proof.

Let { λ 1, …, λ n } \{\lambda_{1},\dots,\lambda_{n}\} be the roots of f f, where λ 1 = 1 \lambda_{1}=1 and λ 2, …, λ n ∈ 𝔪 \lambda_{2},\dots,\lambda_{n}\in\mathfrak{m}. Let σ \sigma be a complex automorphism and let λ ∈ 𝔪 \lambda\in\mathfrak{m} be a root such that | σ ⁡ ( λ) | = 1 |\sigma(\lambda)|=1. Then f σ f^{\sigma} is another CA-polynomial in normal form without linear term and with two roots of absolute value 1 1. This contradicts Lemma 5.5. Then, if some root of f f is transcendental, then there exists a complex automorphism sending it to a transcendental of absolute value 1 1 which is not possible. ∎

## 7 Third result

In this final section, we prove that there are no CA-polynomial of degree 20 20 with three recycled roots.

###### Lemma 7.1.

If y 0, …, y k − 1 ∈ R y_{0},\dots,y_{k-1}\in R, then G ⁡ ( x, y 0, …, y k − 1) ∈ R ⁡ [x] G(x;y_{0},\dots,y_{k-1})\in R[x] and its roots are in R R.

###### Proof.

Given that the coefficients of g = G ⁡ ( x, y 0, …, y k − 1) g=G(x;y_{0},\dots,y_{k-1}) are polynomials in y 0, …, y k − 1 y_{0},\dots,y_{k-1}, it follows that g ∈ R ⁡ [x] g\in R[x]. Then, from the Newton polygon of g g, it follows that all of its roots are also in R R. ∎

###### Lemma 7.2.

Let y 0, …, y k − 1, c 0, …, c k − 1 ∈ R y_{0},\dots,y_{k-1},c_{0},\dots,c_{k-1}\in R be such that y i − c i ∈ 𝔪 y_{i}-c_{i}\in\mathfrak{m} for all i = 0, …, k − 1 i=0,\dots,k-1. Consider the set of indices S = { i: c i ≠ y i } ⊆ { 0, …, k − 1 } S=\{i\,\colon\,c_{i}\neq y_{i}\}\subseteq\{0,\dots,k-1\}, the value M = max ⁡ { | C ⁡ ( k, i) |: i ∈ S } M=\max\{|C(k,i)|\,\colon\,i\in S\} and an element λ ∈ R \lambda\in R. Then,

 | | G ⁡ ( λ, y 0, …, y k − 1) | = M ⇔ | G ⁡ ( λ, c 0, …, c k − 1) | = M. |G(\lambda;y_{0},\dots,y_{k-1})|=M\iff|G(\lambda;c_{0},\dots,c_{k-1})|=M. |  |

###### Proof.

From Corollary 3.5 we have

 | G ⁡ ( x, y 0, …, y k − 1) = G ⁡ ( x, c 0, …, c k − 1) + ∑ i = 0 k − 1 ( k i) ​ G ​ ( x, c 0, …, c i − 1) ​ G ​ ( c i, y i, …, y k − 1), G(x;y_{0},\dots,y_{k-1})=G(x;c_{0},\dots,c_{k-1})+\sum_{i=0}^{k-1}\binom{k}{i}G(x;c_{0},\dots,c_{i-1})G(c_{i};y_{i},\dots,y_{k-1}), |  |

For any i ∈ { 0, …, k − 1 } i\in\{0,\dots,k-1\}, G ⁡ ( c i, y i, …, y k − 1) G(c_{i};y_{i},\dots,y_{k-1}) is congruent to G ⁡ ( y i, y i, …, y k − 1) G(y_{i};y_{i},\dots,y_{k-1}) modulo 𝔪 \mathfrak{m}, but given that G ⁡ ( y i, y i, …, y k − 1) = 0 G(y_{i};y_{i},\dots,y_{k-1})=0, it follows | G ⁡ ( c i, y i, …, y k − 1) | < 1 |G(c_{i};y_{i},\dots,y_{k-1})|<1. Furthermore, if i ∉ S i\not\in S, we have c i = y i c_{i}=y_{i} and then G ⁡ ( c i, y i, …, y k − 1) = 0 G(c_{i};y_{i},\dots,y_{k-1})=0. Hence,

 | G ⁡ ( x, y 0, …, y k − 1) = G ⁡ ( x, c 0, …, c k − 1) + ∑ i ∈ S ( k i) ​ G ​ ( x, c 0, …, c i − 1) ​ G ​ ( 0, y i, …, y k − 1). G(x;y_{0},\dots,y_{k-1})=G(x;c_{0},\dots,c_{k-1})+\sum_{i\in S}\binom{k}{i}G(x;c_{0},\dots,c_{i-1})G(0;y_{i},\dots,y_{k-1}). |  |

For i ∈ S i\in S, since G ⁡ ( x, c 0, …, c i − 1) ∈ R ⁡ [x] G(x,c_{0},\dots,c_{i-1})\in R[x] and λ ∈ R \lambda\in R, it follows | G ⁡ ( λ, c 0, …, c i − 1) | ≤ 1 |G(\lambda,c_{0},\dots,c_{i-1})|\leq 1. Finally, the absolute value of the sum at x = λ x=\lambda is less than M M. ∎

The next Corollary gives a similar result as in [4, Th.2].

###### Corollary 7.3.

Let n = p r + 1 n=p^{r}+1, let y 2, …. y n − 2 ∈ 𝔪 ∪ { 1 } y_{2},\dots.y_{n-2}\in\mathfrak{m}\cup\{1\} and let f ⁡ ( x) = G ⁡ ( x, 0, 0, y 2, …, y n − 2, 1) f(x)=G(x;0,0,y_{2},\dots,y_{n-2},1). Let c i = 0 c_{i}=0 if | y i | < 1 |y_{i}|<1 and c i = 1 c_{i}=1 if y i = 1 y_{i}=1. If | G ⁡ ( 1, c 0, …, c n − 1) | = 1 / p |G(1;c_{0},\dots,c_{n-1})|=1/p, then f f is not a CA-polynomial.

###### Proof.

Lemma 7.2 implies | f ⁡ ( 1) | = 1 / p |f(1)|=1/p, but if f f is a CA-polynomial, then f ⁡ ( 1) = 0 f(1)=0, a contradiction. ∎

###### Remark 7.4.

For the case n = 20 n=20 and p = 19 p=19, we checked all the 2 17 2^{17} cases for

 | | G ⁡ ( 1, 0, 0, c 2, …, c n − 2, 1) | = 1 p. |G(1;0,0,c_{2},\dots,c_{n-2},1)|=\frac{1}{p}. |  |

We obtained that there are 6680 6680 possible CA-polynomials with two or more different roots. Avoiding the cases y 4 = y 16 = 1 y_{4}=y_{16}=1, y 5 = y 10 = 1 y_{5}=y_{10}=1 and y 10 = y 15 = 1 y_{10}=y_{15}=1 we reduced the list to 3125 3125 cases of possible CA-polynomials of degree 20 20. For each case, the conditions of being a CA-polynomial produce a system with one more equation than variables. For example, the most computationally intensive cases, have 16 16 equations with 15 15 variables. These 4 possible CA-polynomials are

 | G ⁡ ( x CLOSE \displaystyle G(x | ; 0, 0, y 2, y 3, y 4, y 5, y 6, y 7, y 8, y 9, 1, y 11, 1, y 13, y 14, y 15, y 16, y 17, y 18, 1), \displaystyle;0,0,y_{2},y_{3},y_{4},y_{5},y_{6},y_{7},y_{8},y_{9},1,y_{11},1,y_{13},y_{14},y_{15},y_{16},y_{17},y_{18},1), |  |

 | G ⁡ ( x CLOSE \displaystyle G(x | ; 0, 0, y 2, y 3, y 4, y 5, y 6, y 7, y 8, y 9, 1, 1, y 12, y 13, y 14, y 15, y 16, y 17, y 18, 1), \displaystyle;0,0,y_{2},y_{3},y_{4},y_{5},y_{6},y_{7},y_{8},y_{9},1,1,y_{12},y_{13},y_{14},y_{15},y_{16},y_{17},y_{18},1), |  |

 | G ⁡ ( x CLOSE \displaystyle G(x | ; 0, 0, y 2, y 3, y 4, 1, y 6, y 7, y 8, y 9, y 10, y 11, y 12, y 13, y 14, y 15, 1, y 17, y 18, 1), \displaystyle;0,0,y_{2},y_{3},y_{4},1,y_{6},y_{7},y_{8},y_{9},y_{10},y_{11},y_{12},y_{13},y_{14},y_{15},1,y_{17},y_{18},1), |  |

 | G ⁡ ( x CLOSE \displaystyle G(x | ; 0, 0, y 2, y 3, 1, y 5, y 6, y 7, y 8, y 9, y 10, y 11, y 12, y 13, y 14, y 15, y 16, 1, y 18, 1). \displaystyle;0,0,y_{2},y_{3},1,y_{5},y_{6},y_{7},y_{8},y_{9},y_{10},y_{11},y_{12},y_{13},y_{14},y_{15},y_{16},1,y_{18},1). |  |

The next Proposition gives a similar result as in [4, Prop.20].

###### Proposition 7.5.

Let n = p r + 1 n=p^{r}+1 and let m m be the minimum of | G ⁡ ( 1, 0, 0, c 2, …, c n − 2, 1) | |G(1;0,0,c_{2},\dots,c_{n-2},1)| for all c 2, …, c n − 2 ∈ { 0, 1 } c_{2},\dots,c_{n-2}\in\{0,1\},

 | m = min { | G ( 1; 0, 0, c 2, …, c n − 2, 1) |: c 2, …, c n − 2 ∈ { 0, 1 } }. m=\min\left\{|G(1;0,0,c_{2},\dots,c_{n-2},1)|\,\colon\,c_{2},\dots,c_{n-2}\in\{0,1\}\right\}. |  |

Let f = G ⁡ ( x, 0, 0, y 2, …, y n − 2, 1) f=G(x;0,0,y_{2},\dots,y_{n-2},1) be a polynomial with | y i | ≤ m |y_{i}|\leq m or y i = 1 y_{i}=1 for 2 ≤ i ≤ n − 2 2\leq i\leq n-2. Then f f is not a CA-polynomial

###### Proof.

First recall from [7, Prop.6] that m > 0 m>0. Let c i = 0 c_{i}=0 if | y i | < 1 |y_{i}|<1 and c i = 1 c_{i}=1 if y i = 1 y_{i}=1. Notice that G ⁡ ( x, y i, …, y n − 2, 1) G(x;y_{i},\dots,y_{n-2},1) is a polynomial in R ⁡ [x] R[x] with roots in R R and y i y_{i} one of its roots. Hence, its constant term b i:= G ⁡ ( 0, y i, …, y n − 2, 1) b_{i}:=G(0;y_{i},\dots,y_{n-2},1) satisfy | b i | ≤ | y i | |b_{i}|\leq|y_{i}|. Let us write f f as

 | f ⁡ ( x) = G ⁡ ( x, c 0, …, c n − 1) + ∑ i ∈ S ( n i) ​ G ​ ( x, c 0, …, c i − 1) ​ b i, f(x)=G(x;c_{0},\dots,c_{n-1})+\sum_{i\in S}\binom{n}{i}G(x;c_{0},\dots,c_{i-1})b_{i}, |  |

where S = { i: c i = 0 } S=\{i\,\colon\,c_{i}=0\}, | b i | ≤ | y i | ≤ m |b_{i}|\leq|y_{i}|\leq m and | C ⁡ ( n, i) | < 1 |C(n,i)|<1 for all i ∈ S i\in S. Then, the absolute value of the sum is less than m m which implies | f ⁡ ( 1) | = | G ⁡ ( 1, c 0, …, c n − 1) | ≥ m |f(1)|=|G(1;c_{0},\dots,c_{n-1})|\geq m. ∎

###### Remark 7.6.

For the case n = 20 n=20 and p = 19 p=19, the number m m from the previous Proposition can be computed relatively easy and it is equal to 5 5. Hence, in any CA-polynomial of degree 20 20 there exists a common root of absolute value greater than ( 1 / p) 5 (1/p)^{5}. The same result holds for n = 24 n=24 and p = 23 p=23.

The next Propositions generalizes [4, Prop.16]

###### Proposition 7.7.

Let f f be a degree n n complex polynomial having two or more different roots. Assume there exist a prime q q, a set S S and a root λ \lambda such that | C ⁡ ( n, i) | q < 1 |C(n,i)|_{q}<1 for all i ∈ S i\in S and f ( i) ​ ( λ) = 0 f^{(i)}(\lambda)=0 for all i ∉ S i\not\in S. Then, f f is not a CA-polynomial.

###### Proof.

By changing x x by x − λ x-\lambda in f f and scaling it by the root of maximum absolute value (with respect to q q) we can write f f as

 | f = x n + ( n n − 1) ​ b n − 1 ​ x n − 1 + ⋯ + ( n 1) ​ b 1 ​ x, f=x^{n}+\binom{n}{n-1}b_{n-1}x^{n-1}+\dots+\binom{n}{1}b_{1}x, |  |

where | b i | q ≤ 1 |b_{i}|_{q}\leq 1 for all i i and by hypothesis b i = 0 b_{i}=0 for all i ∉ S i\not\in S. Then, evaluating at the root 1 1, we get

 | − 1 = ∑ i ∈ S ( n i) ​ b i. -1=\sum_{i\in S}\binom{n}{i}b_{i}. |  |

By taking the absolute value on both sides of the equality, we arrive at a contradiction. ∎

###### Remark 7.8.

For the case n = 20 n=20, we can apply the previous Proposition to deduce that there is no CA-polynomial G ⁡ ( x, y 0, …, y 19) G(x;y_{0},\dots,y_{19}) such that y 1 = y 19 y_{1}=y_{19} or y 4 = y 16 y_{4}=y_{16} or y 5 = y 10 = y 15 y_{5}=y_{10}=y_{15}.

###### Theorem 7.9.

There is no CA-polynomial of degree 20 20 with a root of multiplicity 11 11 or more and there is no CA-polynomial of degree 24 24 with a root of multiplicity 15 15 or more.

###### Proof.

Let f f be a CA-polynomial of degree 20 20 with a root of multiplicity 11 11 or more. Then, f = G ⁡ ( x, y 0, …, y 19) f=G(x;y_{0},\dots,y_{19}) where we can assume y 0 = ⋯ = y 10 = 0 y_{0}=\dots=y_{10}=0. Hence, y 5 = y 10 = 0 y_{5}=y_{10}=0. Analogously, if f f is a CA-polynomial of degree 24 24 with a root of multiplicity 15 15 or more, then y 7 = y 14 = 0 y_{7}=y_{14}=0. Let us prove that these two cases are not possible. First case n = 20 n=20 over 𝔽 5 \mathbb{F}_{5}. The radical of the ideal

 | ⟨ f ⁡ ( 1), res ⁡ ( f, N 5 ​ ( f)), res ⁡ ( f, N 10 ​ ( f)), res ⁡ ( f, N 15 ​ ( f)) ⟩ \langle f(1),\res(f,N_{5}(f)),\res(f,N_{10}(f)),\res(f,N_{15}(f))\rangle |  |

gives three solutions,

 | ( b 5, b 10, b 15) ∈ { ( 0, − 1, 0), ( 1, 0, − 2), ( − 2, 0, 1) }. (b_{5},b_{10},b_{15})\in\left\{(0,-1,0),(1,0,-2),(-2,0,1)\right\}. |  |

If y 5 = y 10 = 0 y_{5}=y_{10}=0, then b 5 = b 10 = 0 b_{5}=b_{10}=0 which is not possible. Second case n = 24 n=24 over 𝔽 7 \mathbb{F}_{7}. The radical of the ideal

 | ⟨ f ⁡ ( 1), res ⁡ ( f, N 7 ​ ( f)), res ⁡ ( f, N 14 ​ ( f)), res ⁡ ( f, N 21 ​ ( f)) ⟩ \langle f(1),\res(f,N_{7}(f)),\res(f,N_{14}(f)),\res(f,N_{21}(f))\rangle |  |

gives the solutions

 | ( b 7, b 14, b 21) ∈ { ( 3, 3, 0), ( − 3, − 1, 0), ( 1, 0, 1), ( 0, − 3, 1), ( − 1, 0, 3), ( 0, 2, − 2) }. (b_{7},b_{14},b_{21})\in\left\{(3,3,0),(-3,-1,0),(1,0,1),(0,-3,1),(-1,0,3),(0,2,-2)\right\}. |  |

If y 7 = y 14 = 0 y_{7}=y_{14}=0, then b 7 = b 14 = 0 b_{7}=b_{14}=0 which is not possible. ∎

###### Theorem 7.10.

There are no CA-polynomial of degree 20 20 with three recycled roots. That is, if f = G ⁡ ( x, 0, 0, y 2, …, y n − 2, 1) f=G(x;0,0,y_{2},\dots,y_{n-2},1) and y i ∈ { 0, 1, y } y_{i}\in\{0,1,y\} for all i i, then f f is not a CA-polynomial.

###### Proof.

Let i i be a positive integer less than 3 17 3^{17} written in base 3 3, i = d 2 + d 3 ​ 3 + d 2 ​ 3 2 + ⋯ + d 18 ​ 3 17 i=d_{2}+d_{3}3+d_{2}3^{2}+\dots+d_{18}3^{17} where d 2, …, d 18 ∈ { 0, 1, 2 } d_{2},\dots,d_{18}\in\{0,1,2\}. Let f i f_{i} be the polynomial defined as f i = G ⁡ ( x, 0, 0, y 2, …, y 18, 1) f_{i}=G(x;0,0,y_{2},\dots,y_{18},1) where

 | y k = { 1 if ​ d k = 1 0 if ​ d k = 0 y if ​ d k = 2, k = 2, …, 18. y_{k}=\begin{cases}1&\text{ if }d_{k}=1\\ 0&\text{ if }d_{k}=0\\ y&\text{ if }d_{k}=2\end{cases},\quad k=2,\dots,18. |  |

Then, f i f_{i} is a CA-polynomial if and only if f i ​ ( 1) = f i ​ ( y) = 0 f_{i}(1)=f_{i}(y)=0. In other words, if res ⁡ ( f i ​ ( 1), f i ​ ( y)) = 0 \res(f_{i}(1),f_{i}(y))=0 as a polynomial in y y. We checked each of the 3 17 3^{17} possible cases in less than 48 hours in a personal computer (4GHz of CPU and 4GB of memory).

In order to avoid the computation of the resultant, we analyzed the slopes of the Newton polygons of f ⁡ ( 1) f(1) and f ⁡ ( y) f(y) (for several primes), but we concluded that the computation of the resultant is faster. ∎

## References

- [1] M. F. Atiyah and I. G. Macdonald. Introduction to commutative algebra. Addison-Wesley Publishing Co., Reading, Mass.-London-Don Mills, Ont., 1969.
- [2] Eduardo Casas-Alvero. Singularities of plane curves, volume 276 of London Mathematical Society Lecture Note Series. Cambridge University Press, Cambridge, 2000.
- [3] Eduardo Casas-Alvero. Higher order polar germs. J. Algebra, 240(1):326–337, 2001.
- [4] Wouter Castryck, Robert Laterveer, and Myriam Ounaïes. Constraints on counterexamples to the casas-alvero conjecture and a verification in degree 12. Mathematics of Computation, 83(290):3017–3037, 2014.
- [5] Mustapha Chellali and Alain Salinier. La conjecture de Casas Alvero pour les degrés 5 ​ p e 5p^{e}. An. Univ. Dunărea de Jos Galaţi Fasc. II Mat. Fiz. Mec. Teor., 4(35)(1-2):54–62, 2012.
- [6] Gema M Diaz-Toca and Laureano González-Vega. On a conjecture about univariate polynomials and their roots. In Algorithmic Algebra and Logic, pages 83–90, 2005.
- [7] Jan Draisma and Johan P. de Jong. On the Casas-Alvero conjecture. Eur. Math. Soc. Newsl., (80):29–33, 2011.
- [8] Rosa María de Frutos Marín. Perspectivas aritméticas para la conjetura de casas-alvero. Ph.D. thesis, 2013.
- [9] Hans-Christian Graf von Bothmer, Oliver Labs, Josef Schicho, and Christiaan van de Woestijne. The Casas-Alvero conjecture for infinitely many degrees. J. Algebra, 316(1):224–230, 2007.
- [10] A. Grothendieck. Éléments de géométrie algébrique. IV. Étude locale des schémas et des morphismes de schémas. II. Inst. Hautes Études Sci. Publ. Math., (24):231, 1965.
- [11] H. Kestelman. Automorphisms of the field of complex numbers. Proc. London Math. Soc. (2), 53:1–12, 1951.
- [12] Serge Lang. Algebra, volume 211 of Graduate Texts in Mathematics. Springer-Verlag, New York, third edition, 2002.
- [13] Norman Levinson. The Gontcharoff polynomials. Duke Math. J., 11:729–733, 1944.
- [14] Qing Liu. Algebraic geometry and arithmetic curves, volume 6 of Oxford Graduate Texts in Mathematics. Oxford University Press, Oxford, 2002. Translated from the French by Reinie Erné, Oxford Science Publications.
- [15] Hendrik Verhoek. Some remarks about a polynomial conjecture of casas-alvero. Séminaire Bourbakettes, Paris, 2009.
- [16] S. Yakubovich. Polynomial problems of the Casas-Alvero type. J. Class. Anal., 4(2):97–120, 2014.
- [17] S. Yakubovich. On some properties of the Abel-Goncharov polynomials and the Casas-Alvero problem. Integral Transforms Spec. Funct., 27(8):599–610, 2016.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:cmassri@caece.edu.ar
