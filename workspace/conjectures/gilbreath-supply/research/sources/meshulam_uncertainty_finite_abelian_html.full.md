<!-- source: https://arxiv.org/html/math/0312407 | converted from HTML -->

An Uncertainty Inequality for Finite Abelian Groups

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: Assumed arXiv.org perpetual non-exclusive license][2]

arXiv:math/0312407v1 [math.CO] 22 Dec 2003

# An Uncertainty Inequality for
Finite Abelian Groups

Roy Meshulam Thanks: Department of Mathematics, Technion, Haifa 32000, Israel. e-mail: meshulam@math.technion.ac.il

###### Abstract

Let G G be a finite abelian group of order n n. For a complex valued function f f on G G let f ^ {\widehat{f}} denote the Fourier transform of f f. The classical uncertainty inequality asserts that if f ≠ 0 f\neq 0 then

 | | supp ⁡ ( f) | ⋅ | supp ⁡ ( f ^) | ≥ | G |. |{\rm supp}(f)|\cdot|{\rm supp}({\widehat{f}})|\geq|G|~~. |  | (1) |

Answering a question of Terence Tao, the following improvement of ( 1) is shown:

Theorem: Let d 1 < d 2 d_{1}<d_{2} be two consecutive divisors of n n. If d 1 ≤ k = | supp ⁡ ( f) | ≤ d 2 d_{1}\leq k=|{\rm supp}(f)|\leq d_{2} then

 | | supp ⁡ ( f ^) | ≥ n d 1 ​ d 2 ​ ( d 1 + d 2 − k). \displaystyle|{\rm supp}({\widehat{f}})|\geq\frac{n}{d_{1}d_{2}}(d_{1}+d_{2}-k)~~. |  |

## 1 Introduction

Let G G be a finite abelian group of order n n and let G ^ \widehat{G} be its character group. Let L ⁡ ( G) L(G) denote the space of complex valued functions on G G. For f ∈ L ⁡ ( G) f\in L(G) let f ^ ∈ L ⁡ ( G ^) {\widehat{f}}\in L(\widehat{G}) denote its Fourier transform:

 | f ^ ​ ( χ) = ∑ x ∈ G f ⁡ ( x) ​ χ ​ ( − x). \displaystyle{\widehat{f}}(\chi)=\sum_{x\in G}f(x)\chi(-x)~. |  |

Let supp ⁡ ( f) = { x ∈ G: f ⁡ ( x) ≠ 0 } {\rm supp}(f)=\{x\in G:f(x)\neq 0\} denote the support of f f. The classical uncertainty inequality (see e.g. [1, 3, 2, 5]) asserts that if 0 ≠ f ∈ L ⁡ ( G) 0\neq f\in L(G) then

 | | supp ⁡ ( f) | ⋅ | supp ⁡ ( f ^) | ≥ n. |{\rm supp}(f)|\cdot|{\rm supp}({\widehat{f}})|\geq n~~. |  | (2) |

For a subgroup H < G H<G let H ⟂ = { λ ∈ G ^: ker ⁡ λ ⊃ H } H^{\perp}=\{\lambda\in\widehat{G}~:~\ker\lambda\supset H\}. If f = 1 H f=1_{H} is the indicator function of H H, then f ^ = | H | ⋅ 1 H ⟂ {\widehat{f}}=|H|\cdot 1_{H^{\perp}} and ( 2) is satisfied with equality. Conversely, it can be shown (see [2]) that if f ∈ L ⁡ ( G) f\in L(G) satisfies ( 2) with equality and f ⁡ ( 0) = 1 f(0)=1 then f ⁡ ( x) = 1 H ​ ( x) ​ χ ​ ( x) f(x)=1_{H}(x)\chi(x) for some H < G H<G and χ ∈ H ^ \chi\in\widehat{H}.
Recently Tao [4] showed that ( 2) can be substantially improved when G = ℤ p G={\twelvebb Z}_{p} is the cyclic group of prime order p p.

###### Theorem 1.1

[4] If 0 ≠ f ∈ L ⁡ ( ℤ p) 0\neq f\in L({\twelvebb Z}_{p}) then

 | | supp ⁡ ( f) | + | supp ⁡ ( f ^) | ≥ p + 1. \displaystyle|{\rm supp}(f)|+|{\rm supp}({\widehat{f}})|\geq p+1~~. |  |

Tao further conjectured that one could similarly improve ( 2) for all finite abelian groups provided that | supp ⁡ ( f) | |{\rm supp}(f)| stays away from any divisor of | G | |G|.
In this note we extend Theorem 1.1 to general finite abelian groups. For an integer n n and a real number 1 ≤ k ≤ n 1\leq k\leq n let d 1 ​ ( n, k) d_{1}(n,k) denote the largest divisor d 1 d_{1} of n n such that d 1 ≤ k d_{1}\leq k, and let d 2 ​ ( n, k) d_{2}(n,k) denote the smallest divisor d 2 d_{2} of n n such that d 2 ≥ k d_{2}\geq k.

###### Theorem 1.2

Let f ∈ L ⁡ ( G) f\in L(G) such that 0 ≠ | supp ⁡ ( f) | = k 0\neq|{\rm supp}(f)|=k and let d i = d i ​ ( n, k) d_{i}=d_{i}(n,k). Then

 | | supp ⁡ ( f ^) | ≥ n d 1 ​ d 2 ​ ( d 1 + d 2 − k). |{\rm supp}({\widehat{f}})|\geq\frac{n}{d_{1}d_{2}}(d_{1}+d_{2}-k)~~. |  | (3) |

Remark: Tao noted that Theorem 1.2 can also be formulated as follows: If f f is a non-zero function on G G, then the lattice point ( | s ​ u ​ p ​ p ​ ( f) |, | s ​ u ​ p ​ p ​ ( f ^) |) (|supp(f)|,|supp({\widehat{f}})|) lies on or above the convex hull of the points ( | H |, | G / H |) (|H|,|G/H|), where H H ranges over all subgroups of G G. The classical uncertainty inequality, meanwhile, merely states that this lattice point lies above the hyperbola connecting those points.

The proof of Theorem 1.2 depends on Theorem 1.1 and on the following two simple observations. For 1 ≤ k ≤ n = | G | ~1\leq k\leq n=|G|~ let

 | θ ( G, k) = min { | supp ( f ^) |: 0 ≠ f ∈ L ( G), | supp ( f) | ≤ k }. \displaystyle\theta(G,k)=\min~\{~|{\rm supp}({\widehat{f}})|~:~0\neq f\in L(G)~,~|{\rm supp}(f)|\leq k~\}~~. |  |

###### Proposition 1.3

Let H H be a subgroup of G G and let 1 ≤ k ≤ n 1\leq k\leq n. Then there exist 1 ≤ s ≤ | H | 1\leq s\leq|H|~ and 1 ≤ t ≤ | G / H | ~1\leq t\leq|G/H|~ such that s ​ t ≤ k st\leq k and

 | θ ⁡ ( G, k) ≥ θ ⁡ ( H, s) ⋅ θ ⁡ ( G / H, t). \theta(G,k)\geq\theta(H,s)\cdot\theta(G/H,t)~~. |  | (4) |

For 1 ≤ k ≤ n 1\leq k\leq n let d i = d i ​ ( n, k) d_{i}=d_{i}(n,k) and let u ⁡ ( n, k) = n d 1 ​ d 2 ​ ( d 1 + d 2 − k). u(n,k)=\frac{n}{d_{1}d_{2}}(d_{1}+d_{2}-k)~~.

###### Proposition 1.4

For any divisor d d of n n and for any 1 ≤ s ≤ d, 1 ≤ t ≤ n d 1\leq s\leq d~,~1\leq t\leq\frac{n}{d}

 | u ⁡ ( d, s) ⋅ u ⁡ ( n d, t) ≥ u ⁡ ( n, s ​ t). u(d,s)\cdot u(\frac{n}{d},t)\geq u(n,st)~~. |  | (5) |

Proof of Theorem 1.2: We show by induction on | G | = n |G|=n that θ ⁡ ( G, k) ≥ u ⁡ ( n, k) \theta(G,k)\geq u(n,k) for all 1 ≤ k ≤ n 1\leq k\leq n. For prime n n, this reduces to Tao’s result. Otherwise let d d be a non-trivial divisor of n n and let H H be a subgroup of G G of order d d. By Proposition 1.3 there exist 1 ≤ s ≤ d 1\leq s\leq d and 1 ≤ t ≤ min ⁡ { k s, n d } 1\leq t\leq\min\{\frac{k}{s},\frac{n}{d}\} such that ( 4) holds. Combining the induction hypothesis with ( 5) and the monotonicity of u u, we obtain

 | θ ⁡ ( G, k) ≥ θ ⁡ ( H, s) ⋅ θ ⁡ ( G / H, t) ≥ u ⁡ ( d, s) ⋅ u ⁡ ( n d, t) ≥ u ⁡ ( n, s ​ t) ≥ u ⁡ ( n, k). \displaystyle\theta(G,k)\geq\theta(H,s)\cdot\theta(G/H,t)\geq u(d,s)\cdot u(\frac{n}{d},t)\geq u(n,st)\geq u(n,k)~~. |  |

□ \Box

The proofs of Propositions 1.3 and 1.4 are given in Sections 2 and 3. In Section 4 we remark on a possible extension to non-abelian groups.

## 2 Subgroups and Factor Groups

For a subgroup H < G H<G let q: G ^ → H ^ q:\widehat{G}\rightarrow\widehat{H} denote the restriction homomorphism. For each η ∈ H ^ \eta\in\widehat{H} choose an arbitrary but fixed η ~ ∈ G ^ \tilde{\eta}\in\widehat{G} such that q ⁡ ( η ~) = η q(\tilde{\eta})=\eta. Clearly q − 1 ​ ( η) = { η ~ ⋅ λ: λ ∈ H ⟂ } q^{-1}(\eta)=\{\tilde{\eta}\cdot\lambda~:~\lambda\in H^{\perp}\} and G ^ = { η ~ ⋅ λ: η ∈ H ^, λ ∈ H ⟂ } \widehat{G}=\{\tilde{\eta}\cdot\lambda~:~\eta\in\widehat{H}~,~\lambda\in H^{\perp}\}. For f ∈ L ⁡ ( G) f\in L(G) and y ∈ G y\in G let f y ∈ L ⁡ ( H) f_{y}\in L(H) be given by f y ​ ( z) = f ⁡ ( z + y) f_{y}(z)=f(z+y) for all z ∈ H z\in H. Let y ¯ = y + H \overline{y}=y+H denote the image of y ∈ G y\in G in G / H G/H. For η ∈ H ^ \eta\in\widehat{H} let F η ∈ L ⁡ ( G / H) F_{\eta}\in L(G/H) be defined by F η ​ ( y ¯) = f y ^ ​ ( η) ​ η ~ ​ ( − y). F_{\eta}(\overline{y})=\widehat{f_{y}}(\eta)\tilde{\eta}(-y)~~. It can be checked that the right-hand side indeed depends only on y ¯ \overline{y}. A character λ ∈ H ⟂ \lambda\in H^{\perp} gives rise to a character λ ′ ∈ G / H ^ \lambda^{\prime}\in\widehat{G/H} given by λ ′ ​ ( y ¯) = λ ​ ( y) \lambda^{\prime}(\overline{y})=\lambda(y). The map λ → λ ′ \lambda\rightarrow\lambda^{\prime} is an isomorphism between H ⟂ H^{\perp} and G / H ^ \widehat{G/H}.

###### Claim 2.1

For η ∈ H ^ \eta\in\widehat{H} and λ ∈ H ⟂ \lambda\in H^{\perp}

 | f ^ ​ ( η ~ ⋅ λ) = F η ^ ​ ( λ ′). \displaystyle{\widehat{f}}(\tilde{\eta}\cdot\lambda)=\widehat{F_{\eta}}(\lambda^{\prime})~~. |  |

Proof: Let ( G: H) = m (G:H)=m and let G = ⋃ i = 1 m ( y i + H) G=\bigcup_{i=1}^{m}(y_{i}+H) be the coset decomposition of G G. Then

 | f ^ ​ ( η ~ ⋅ λ) = ∑ x ∈ G f ⁡ ( x) ​ η ~ ​ ( − x) ​ λ ​ ( − x) = ∑ i = 1 m ∑ z ∈ H f ⁡ ( z + y i) ​ η ~ ​ ( − z − y i) ​ λ ​ ( − z − y i) = \displaystyle{\widehat{f}}(\tilde{\eta}\cdot\lambda)=\sum_{x\in G}f(x)\tilde{\eta}(-x)\lambda(-x)=\sum_{i=1}^{m}\sum_{z\in H}f(z+y_{i})\tilde{\eta}(-z-y_{i})\lambda(-z-y_{i})= |  |

 | ∑ i = 1 m ( ∑ z ∈ H f y i ​ ( z) ​ η ​ ( − z)) ​ η ~ ​ ( − y i) ​ λ ​ ( − y i) = ∑ i = 1 m f y i ^ ​ ( η) ​ η ~ ​ ( − y i) ​ λ ​ ( − y i) = \displaystyle\sum_{i=1}^{m}(~\sum_{z\in H}f_{y_{i}}(z)\eta(-z)~)\tilde{\eta}(-y_{i})\lambda(-y_{i})=\sum_{i=1}^{m}\widehat{f_{y_{i}}}(\eta)\tilde{\eta}(-y_{i})\lambda(-y_{i})= |  |

 | ∑ i = 1 m F η ​ ( y i ¯) ​ λ ′ ​ ( − y i ¯) = F η ^ ​ ( λ ′). \displaystyle\sum_{i=1}^{m}F_{\eta}(\overline{y_{i}})\lambda^{\prime}(-\overline{y_{i}})=\widehat{F_{\eta}}(\lambda^{\prime})~~. |  |

□ \Box

Proof of Proposition 1.3: Let f ∈ L ⁡ ( G) f\in L(G) with | supp ⁡ ( f) | = k > 0 |{\rm supp}(f)|=k>0. Keeping the notation of Claim 2.1 let

 | I = { 1 ≤ i ≤ m: supp ⁡ ( f) ​ ⋂ ( y i + H) ≠ ∅ } \displaystyle I=\{1\leq i\leq m~:~{\rm supp}(f)\bigcap(y_{i}+H)\neq\emptyset~\}~ |  |

and denote | I | = t |I|=t. Let η \eta be any element of H ^ \widehat{H}. If j ∉ I j\not\in I then f y j = 0 f_{y_{j}}=0 and therefore F η ​ ( y j ¯) = 0 F_{\eta}(\overline{y_{j}})=0. It follows that if F η ≠ 0 F_{\eta}\neq 0 then

 | | supp ⁡ ( F η ^) | ≥ θ ⁡ ( G / H, t). |{\rm supp}(\widehat{F_{\eta}})|\geq\theta(G/H,t)~~. |  | (6) |

By averaging there exists an i ∈ I i\in I such that 0 < | supp ⁡ ( f y i) | ≤ k t = s 0<|{\rm supp}(f_{y_{i}})|\leq\frac{k}{t}=s~. Let A = supp ⁡ ( f y i ^) ⊂ H ^ A={\rm supp}(\widehat{f_{y_{i}}})\subset\widehat{H} then

 | | A | ≥ θ ⁡ ( H, s). |A|\geq\theta(H,s)~. |  | (7) |

Furthermore F η ​ ( y i ¯) = f y i ^ ​ ( η) ⋅ η ~ ​ ( y i) ≠ 0 F_{\eta}(\overline{y_{i}})=\widehat{f_{y_{i}}}(\eta)\cdot\tilde{\eta}(y_{i})\neq 0 for all η ∈ A \eta\in A. Combining Claim 2.1 with ( 6) and ( 7) it follows that

 | | supp ⁡ ( f ^) | = ∑ η ∈ H ^ | supp ⁡ ( F η ^) | ≥ ∑ η ∈ A | supp ⁡ ( F η ^) | ≥ θ ⁡ ( H, s) ⋅ θ ⁡ ( G / H, t). \displaystyle|{\rm supp}({\widehat{f}})|=\sum_{\eta\in\widehat{H}}|{\rm supp}(\widehat{F_{\eta}})|\geq\sum_{\eta\in A}|{\rm supp}(\widehat{F_{\eta}})|\geq\theta(H,s)\cdot\theta(G/H,t)~. |  |

□ \Box

## 3 A Submultiplicativity Property of u ⁡ ( n, k) u(n,k)

Let k = s ​ t k=st. For i = 1, 2 i=1,2 let d i ​ ( d, s) = a i, d i ​ ( n d, t) = b i d_{i}(d,s)=a_{i}~,~d_{i}(\frac{n}{d},t)=b_{i}~ and d i ​ ( n, k) = c i ~d_{i}(n,k)=c_{i}~. Then

 | m 1 = max ⁡ { a 1, k b 2 } ≤ s ≤ min ⁡ { a 2, k b 1 } = m 2. m_{1}=\max\{a_{1},\frac{k}{b_{2}}\}\leq s\leq\min\{a_{2},\frac{k}{b_{1}}\}=m_{2}~~. |  | (8) |

We have to show that

 | ( a 1 + a 2 − s) ​ ( b 1 + b 2 − k s) a 1 ​ a 2 ​ b 1 ​ b 2 ≥ c 1 + c 2 − k c 1 ​ c 2. \frac{(a_{1}+a_{2}-s)(b_{1}+b_{2}-\frac{k}{s})}{a_{1}a_{2}b_{1}b_{2}}\geq\frac{c_{1}+c_{2}-k}{c_{1}c_{2}}~~. |  | (9) |

Without loss of generality we may assume a 1 ​ b 1 ≤ a 1 ​ b 2 ≤ a 2 ​ b 1 ≤ a 2 ​ b 2. a_{1}b_{1}\leq a_{1}b_{2}\leq a_{2}b_{1}\leq a_{2}b_{2}~. Consider three cases:

(1) a 1 ​ b 1 ≤ k ≤ a 1 ​ b 2. ~~a_{1}b_{1}\leq k\leq a_{1}b_{2}~~. Since both a 1 ​ b 1 a_{1}b_{1} and a 1 ​ b 2 a_{1}b_{2} are divisors of n n it follows that a 1 ​ b 1 ≤ c 1 ≤ k ≤ c 2 ≤ a 1 ​ b 2 a_{1}b_{1}\leq c_{1}\leq k\leq c_{2}\leq a_{1}b_{2}~. By convexity it therefore suffices to show

 | ( a 1 + a 2 − s) ​ ( b 1 + b 2 − k s) a 1 ​ a 2 ​ b 1 ​ b 2 ≥ a 1 ​ b 1 + a 1 ​ b 2 − k ( a 1 ​ b 1) ​ ( a 1 ​ b 2) \displaystyle\frac{(a_{1}+a_{2}-s)(b_{1}+b_{2}-\frac{k}{s})}{a_{1}a_{2}b_{1}b_{2}}\geq\frac{a_{1}b_{1}+a_{1}b_{2}-k}{(a_{1}b_{1})(a_{1}b_{2})}~~ |  |

or equivalently

 | a 1 ​ ( a 1 + a 2 − s) ​ ( b 1 + b 2 − k s) ≥ a 1 ​ a 2 ​ b 1 + a 1 ​ a 2 ​ b 2 − a 2 ​ k. a_{1}(a_{1}+a_{2}-s)(b_{1}+b_{2}-\frac{k}{s})\geq a_{1}a_{2}b_{1}+a_{1}a_{2}b_{2}-a_{2}k~~. |  | (10) |

By ( 8), a 1 = m 1 ≤ s ≤ m 2 = k b 1. a_{1}=m_{1}\leq s\leq m_{2}=\frac{k}{b_{1}}~. By convexity we just have to check ( 10) for the two extreme values of s s:
(i) s = a 1 s=a_{1}. Then ( 10) holds with equality.
(ii) s = k b 1 s=\frac{k}{b_{1}}. Then ( 10) is equivalent to ( k − a 1 ​ b 1) ​ ( a 2 ​ b 1 − a 1 ​ b 2) ≥ 0 (k-a_{1}b_{1})(a_{2}b_{1}-a_{1}b_{2})\geq 0 which clearly holds.

(2) a 1 ​ b 2 ≤ k ≤ a 2 ​ b 1. ~~a_{1}b_{2}\leq k\leq a_{2}b_{1}~~. Arguing as in case (1) it suffices to show

 | ( a 1 + a 2 − s) ​ ( b 1 + b 2 − k s) a 1 ​ a 2 ​ b 1 ​ b 2 ≥ a 1 ​ b 2 + a 2 ​ b 1 − k ( a 1 ​ b 2) ​ ( a 2 ​ b 1) \displaystyle\frac{(a_{1}+a_{2}-s)(b_{1}+b_{2}-\frac{k}{s})}{a_{1}a_{2}b_{1}b_{2}}\geq\frac{a_{1}b_{2}+a_{2}b_{1}-k}{(a_{1}b_{2})(a_{2}b_{1})} |  |

or equivalently

 | ( a 1 + a 2 − s) ​ ( b 1 + b 2 − k s) ≥ a 1 ​ b 2 + a 2 ​ b 1 − k. (a_{1}+a_{2}-s)(b_{1}+b_{2}-\frac{k}{s})\geq a_{1}b_{2}+a_{2}b_{1}-k~~. |  | (11) |

We check ( 11) for
(i) s = m 1 = k b 2 s=m_{1}=\frac{k}{b_{2}}. Then ( 11) is equivalent to ( b 2 − b 1) ​ ( k − a 1 ​ b 2) ≥ 0 (b_{2}-b_{1})(k-a_{1}b_{2})\geq 0~.
(ii) s = m 2 = k b 1 s=m_{2}=\frac{k}{b_{1}}. Then ( 11) is equivalent to ( b 2 − b 1) ​ ( a 2 ​ b 1 − k) ≥ 0 (b_{2}-b_{1})(a_{2}b_{1}-k)\geq 0~.

(3) a 2 ​ b 1 ≤ k ≤ a 2 ​ b 2. ~~a_{2}b_{1}\leq k\leq a_{2}b_{2}~~. It suffices to show

 | ( a 1 + a 2 − s) ​ ( b 1 + b 2 − k s) a 1 ​ a 2 ​ b 1 ​ b 2 ≥ a 2 ​ b 1 + a 2 ​ b 2 − k ( a 2 ​ b 1) ​ ( a 2 ​ b 2) \displaystyle\frac{(a_{1}+a_{2}-s)(b_{1}+b_{2}-\frac{k}{s})}{a_{1}a_{2}b_{1}b_{2}}\geq\frac{a_{2}b_{1}+a_{2}b_{2}-k}{(a_{2}b_{1})(a_{2}b_{2})} |  |

or equivalently

 | a 2 ​ ( a 1 + a 2 − s) ​ ( b 1 + b 2 − k s) ≥ a 1 ​ a 2 ​ b 1 + a 1 ​ a 2 ​ b 2 − a 1 ​ k. a_{2}(a_{1}+a_{2}-s)(b_{1}+b_{2}-\frac{k}{s})\geq a_{1}a_{2}b_{1}+a_{1}a_{2}b_{2}-a_{1}k~~. |  | (12) |

We check ( 12) for
(i) s = m 1 = k b 2 s=m_{1}=\frac{k}{b_{2}}. Then ( 12) is equivalent to ( a 2 ​ b 1 − a 1 ​ b 2) ​ ( a 2 ​ b 2 − k) ≥ 0 (a_{2}b_{1}-a_{1}b_{2})(a_{2}b_{2}-k)\geq 0~.
(ii) s = m 2 = a 2 s=m_{2}=a_{2}. Then ( 12) is in fact an equality.

□ \Box

## 4 Concluding Remarks

We have shown that if 0 < | supp ⁡ ( f) | = k 0<|{\rm supp}(f)|=k lies between two consecutive divisors d 1 < d 2 d_{1}<d_{2} of | G | = n |G|=n then | supp ⁡ ( f ^) | |{\rm supp}({\widehat{f}})| is at least the weighted average n d 1 ​ d 2 ​ ( d 1 + d 2 − k) \frac{n}{d_{1}d_{2}}(d_{1}+d_{2}-k) of n d 1 \frac{n}{d_{1}} and n d 2 \frac{n}{d_{2}}. It would be interesting to obtain a similar result in the following non-abelian setting: Let G G be any finite group and let ρ 1, …, ρ t \rho_{1},\ldots,\rho_{t} be the complex irreducible representations of G G, where ρ i: G → GL ⁡ ( V i) \rho_{i}:G\rightarrow{\rm GL}(V_{i}) and V i V_{i} is a complex vector space of dimension d i d_{i}. The Fourier Transform f ^ ​ ( ρ) {\widehat{f}}(\rho) of a function f ∈ L ⁡ ( G) f\in L(G) at a representation ρ: G → GL ⁡ ( V) \rho:G\rightarrow{\rm GL}(V) is given by

 | f ^ ​ ( ρ) = ∑ x ∈ G f ⁡ ( x) ​ ρ ​ ( x − 1) ∈ End ⁡ ( V). \displaystyle{\widehat{f}}(\rho)=\sum_{x\in G}f(x)\rho(x^{-1})\in{\rm End}(V)~~. |  |

Let μ ⁡ ( f) = ∑ i = 1 t d i ⋅ rank ​ f ^ ​ ( ρ i) \mu(f)=\sum_{i=1}^{t}d_{i}\cdot{\rm rank}~{\widehat{f}}(\rho_{i})~. The following non-abelian extension of ( 2) was noted in [2].

###### Theorem 4.1

[2] For any 0 ≠ f ∈ L ⁡ ( G) 0\neq f\in L(G)

 | | supp ⁡ ( f) | ⋅ μ ⁡ ( f) ≥ | G |. |{\rm supp}(f)|\cdot\mu(f)\geq|G|~. |  | (13) |

It seems likely that as in the abelian case, ( 13) could be improved when | supp ⁡ ( f) | |{\rm supp}(f)| is far from an order of any subgroup of G G.

Acknowledgement: I would like to thank Terry Tao for helpful comments.

## References

- [1] D.L. Donoho and P.B. Stark, Uncertainty principles and signal recovery, SIAM J. Applied Math. 49 (1989) 906-931.
- [2] R. Meshulam, An uncertainty inequality for groups of order p ​ q pq, European Journal of Combinatorics 13 (1992) 401-407.
- [3] K.T. Smith, The uncertainty principle on groups, SIAM J. Applied Math. 50 (1989) 876-882.
- [4] T. Tao, An uncertainty principle for cyclic groups of prime order, arXiv:math.CA/0308286 .
- [5] A. Terras, Fourier Analysis on Finite Groups and Applications, Cambridge University Press, Cambridge 1999.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
