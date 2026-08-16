<!-- source: https://ar5iv.labs.arxiv.org/html/2211.13139 | converted from HTML -->

[2211.13139] Extension of a method of Gilmer

# Extension of a method of Gilmer

Luke Pebody

Wednesday 23, November

###### Abstract

It is a well-known conjecture, sometimes attributed to Frankl, that for any family of sets which is closed under the union operation, there is some element which is contained in at least half of the sets.

Gilmer [1] was the first to prove a constant bound, showing that there is some element contained in at least 1% of the sets. They state in their paper that the best possible bound achievable by the same method is 3 − 5 2 ≈ 38.1 % \frac{3-\sqrt{5}}{2}\approx 38.1\%.

This note achieves that bound by finding the optimum value, given a binary variable X X potentially depending on some other variable S S with a given expected value E ⁡ ( X) E(X) and conditional entropy H ⁡ ( X | S) H(X|S) of the conditional entropy of H ⁡ ( X 1 ∪ X 2 | S 1, S 2) H(X_{1}\cup X_{2}|S_{1},S_{2}) for independent readings X 1, S 1 X_{1},S_{1} and X 2, S 2 X_{2},S_{2}.

## 1 Introduction

In this note, we prove the following result (strengthening almost as much as possible the main result from [1]).

###### Theorem 1.

Let A A and B B denote independent samples from a distribution over subsets of [n] [n]. Assume that for all i ∈ [n] i\in[n], Pr [i ∈ A] ≤ α \Pr[i\in A]\leq\alpha for some value 0 < α ≤ 3 − 5 2 0<\alpha\leq\frac{3-\sqrt{5}}{2}. Then H ⁡ ( A ∪ B) ≥ H ⁡ ( α 2) H ⁡ ( α) ​ H ​ ( A). H(A\cup B)\geq\frac{H(\alpha^{2})}{H(\alpha)}H(A).

This will imply the following.

###### Theorem 2.

Let ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} be a union-closed family, ℱ ≠ ∅ \mathcal{F}\neq\emptyset. Then there exists i ∈ [n] i\in[n] that is contained in at least a 3 − 5 2 ≈ 38.1 % \frac{3-\sqrt{5}}{2}\approx 38.1\% fraction of the sets in ℱ \mathcal{F}.

###### Proof.

Suppose not. Let A A and B B be drawn independently and uniformly from ℱ \mathcal{F}. Then, since Pr [i ∈ A] \Pr[i\in A] is rational for each i i, there exists some α < 3 − 5 2 \alpha<\frac{3-\sqrt{5}}{2} for which Pr [i ∈ A] ≤ α \Pr[i\in A]\leq\alpha for all i ∈ [n] i\in[n]. Then from Theorem 1 it follows that H ⁡ ( A ∪ B) ≥ H ⁡ ( α 2) H ⁡ ( α) ​ H ​ ( A) > H ⁡ ( A) H(A\cup B)\geq\frac{H(\alpha^{2})}{H(\alpha)}H(A)>H(A). But this causes a contradiction, as A A is drawn from the uniform distribution on ℱ \mathcal{F} and A ∪ B A\cup B is drawn from some other distribution on ℱ \mathcal{F} and the uniform distribution has the maximum entropy. ∎

## 2 Main Lemma

###### Lemma 3.

For 1 ≤ i ≤ n 1\leq i\leq n, let p i, v i ∈ [0, 1] p_{i},v_{i}\in[0,1] be numbers such that ∑ i p i = 1 \sum_{i}p_{i}=1 and ∑ i p i ​ v i ≤ α \sum_{i}p_{i}v_{i}\leq\alpha for some 0 < α ≤ 3 − 5 2 0<\alpha\leq\frac{3-\sqrt{5}}{2}. Then

 | ∑ i, j p i ​ p j ​ H ​ ( v i + v j − v i ​ v j) ≥ H ⁡ ( 2 ​ α − α 2) H ⁡ ( α) ​ ∑ i p i ​ H ​ ( v i). \sum_{i,j}p_{i}p_{j}H(v_{i}+v_{j}-v_{i}v_{j})\geq\frac{H(2\alpha-\alpha^{2})}{H(\alpha)}\sum_{i}p_{i}H(v_{i}). |  |

###### Proof of Theorem 1 from Lemma 3.

The proof follows exactly as the Proof of Theorem 1 from Lemma 1 in [1]. ∎

For ease of writing in the remainder, we use the fact that H ⁡ ( 1 − x) = H ⁡ ( x) H(1-x)=H(x) to rewrite Lemma 3 in terms of w i = 1 − v i w_{i}=1-v_{i}.

###### Lemma 4 (Lemma 3 Rewritten).

For 1 ≤ i ≤ n 1\leq i\leq n, let p i, w i ∈ [0, 1] p_{i},w_{i}\in[0,1] be numbers such that ∑ i p i = 1 \sum_{i}p_{i}=1 and ∑ i p i ​ w i ≥ β \sum_{i}p_{i}w_{i}\geq\beta for some 1 > β ≥ 5 − 1 2 1>\beta\geq\frac{\sqrt{5}-1}{2}. Then

 | ∑ i, j p i ​ p j ​ H ​ ( w i ​ w j) ≥ H ⁡ ( β 2) H ⁡ ( β) ​ ∑ i p i ​ H ​ ( w i). \sum_{i,j}p_{i}p_{j}H(w_{i}w_{j})\geq\frac{H(\beta^{2})}{H(\beta)}\sum_{i}p_{i}H(w_{i}). |  |

## 3 Some monotonic functions

###### Lemma 5.

The function H ⁡ ( x 2) H ⁡ ( x) \frac{H(x^{2})}{H(x)} is increasing on the range [0, 1] [0,1].

###### Proof.

To be proven. ∎

###### Lemma 6.

The function H ⁡ ( x 2) x ​ H ​ ( x) \frac{H(x^{2})}{xH(x)} is increasing on the range [5 − 1 2, 1] [\frac{\sqrt{5}-1}{2},1].

###### Proof.

To be proven. ∎

## 4 Properties of H ⁡ ( x) / x H(x)/x

Our proof depends on various properties of H ⁡ ( x) x \frac{H(x)}{x} (and its inverse). For ease of notation, let us write f ⁡ ( x) = H ⁡ ( x) x f(x)=\frac{H(x)}{x}.

###### Lemma 7.

The function f f is continuous, onto and decreasing from ( 0, 1] (0,1] to ( 0, ∞) (0,\infty).

###### Proof.

The derivative of f f is f ′ ​ ( x) = log ⁡ ( 1 − x) x 2 f^{\prime}(x)=\frac{\log(1-x)}{x^{2}}, which is negative on the region. Clearly H ⁡ ( 1) 1 = 0 \frac{H(1)}{1}=0 and as x → 0 x\to 0, H ⁡ ( x) x > − log ⁡ x \frac{H(x)}{x}>-\log x tends to infinity. ∎

It follows that for all non-negative real y y, there is a unique value g ⁡ ( y) g(y) for which f ⁡ ( g ⁡ ( y)) = y f(g(y))=y. By standard properties of derivatives, if g ⁡ ( y) = x g(y)=x, g g is differentiable at y y, with derivative 1 / f ′ ​ ( x). 1/f^{\prime}(x).

###### Lemma 8.

For all 0 < α < 1 0<\alpha<1, the function f ⁡ ( α ​ g ​ ( x)) f(\alpha g(x)) is convex.

###### Proof.

The derivative of f ⁡ ( α ​ g ​ ( x)) f(\alpha g(x)) with respect to x x is

 | f ′ ​ ( α ​ g ​ ( x)) ​ α ​ g ′ ​ ( x) \displaystyle f^{\prime}(\alpha g(x))\alpha g^{\prime}(x) | = log ⁡ ( 1 − α ​ g ​ ( x)) α 2 ​ g ​ ( x) 2 ​ α f ′ ​ ( g ​ ( x)) \displaystyle=\frac{\log(1-\alpha g(x))}{\alpha^{2}g(x)^{2}}\frac{\alpha}{f^{\prime}(g(x))} |  |

 |  | = log ⁡ ( 1 − α ​ g ​ ( x)) α 2 ​ g ​ ( x) 2 ​ α ​ g ​ ( x) 2 log ⁡ ( 1 − g ⁡ ( x)) \displaystyle=\frac{\log(1-\alpha g(x))}{\alpha^{2}g(x)^{2}}\frac{\alpha g(x)^{2}}{\log(1-g(x))} |  |

 |  | = log ⁡ ( 1 − α ​ g ​ ( x)) α ​ log ⁡ ( 1 − g ⁡ ( x)). \displaystyle=\frac{\log(1-\alpha g(x))}{\alpha\log(1-g(x))}. |  |

We will show this is increasing in x x. Since g ⁡ ( x) g(x) is decreasing, this is the same as showing that log ⁡ ( 1 − α ​ y) α ​ log ⁡ ( 1 − y) \frac{\log(1-\alpha y)}{\alpha\log(1-y)} is decreasing on the range ( 0, 1] (0,1].

The derivative of this with respect to y y is

 | d d ​ y \displaystyle\frac{d}{dy} | = − α / ( 1 − α y) α log ( 1 − y) + α / ( 1 − y) log ( 1 − α y) α 2 ​ log ⁡ ( 1 − y) 2 \displaystyle=\frac{-\alpha/(1-\alpha y)\alpha\log(1-y)+\alpha/(1-y)\log(1-\alpha y)}{\alpha^{2}\log(1-y)^{2}} |  |

 |  | = − α ⁡ ( 1 − y) ​ log ⁡ ( 1 − y) + ( 1 − α ​ y) ​ log ⁡ ( 1 − α ​ y) α ​ log ⁡ ( 1 − y) 2 ​ ( 1 − y) ​ ( 1 − α ​ y) 2 \displaystyle=\frac{-\alpha(1-y)\log(1-y)+(1-\alpha y)\log(1-\alpha y)}{\alpha\log(1-y)^{2}(1-y)(1-\alpha y)^{2}} |  |

 |  | = − ( 1 − y) log ( 1 − y) / y + ( 1 − α y) log ( 1 − α y) / ( α y) log ⁡ ( 1 − y) 2 ​ ( 1 − y) ​ ( 1 − α ​ y) 2 / y. \displaystyle=\frac{-(1-y)\log(1-y)/y+(1-\alpha y)\log(1-\alpha y)/(\alpha y)}{\log(1-y)^{2}(1-y)(1-\alpha y)^{2}/y}. |  |

So showing that f ⁡ ( α ​ g ​ ( x)) f(\alpha g(x)) is convex for all 0 < α < 1 0<\alpha<1 is the same as showing that − ( 1 − α y) log ( 1 − α y) / ( α y) > − ( 1 − y) log ( 1 − y) / y -(1-\alpha y)\log(1-\alpha y)/(\alpha y)>-(1-y)\log(1-y)/y for all 0 < α < 1 0<\alpha<1, which is the same as showing that − ( 1 − z) log ( 1 − z) / z -(1-z)\log(1-z)/z is decreasing on [0, 1] [0,1].

An elementary property of the derivative of quotients is that if g ′ ​ ( x) > 0 g^{\prime}(x)>0 and g ⁡ ( x) > 0 g(x)>0, f ⁡ ( x) / g ⁡ ( x) f(x)/g(x) is decreasing whenever f ⁡ ( x) / g ⁡ ( x) ≥ f ′ ​ ( x) / g ′ ​ ( x) f(x)/g(x)\geq f^{\prime}(x)/g^{\prime}(x). Thus − ( 1 − z) log ( 1 − z) / z -(1-z)\log(1-z)/z is decreasing if − ( 1 − z) log ( 1 − z) / z ≥ 1 + log ( 1 − z) -(1-z)\log(1-z)/z\geq 1+\log(1-z), which can be rewritten as log ⁡ ( 1 − z) ≤ − z \log(1-z)\leq-z, or 1 − z ≤ exp ⁡ ( − z) 1-z\leq\exp(-z). Since this is true for all z z, we are done. ∎

## 5 Optimising Joint Entropy

In this section we will show that for any distribution p p on [0, 1] [0,1], there exists a distribution q q on [0, 1] [0,1] with at most one non-zero point in its support, for which 𝔼 q ​ ( X) = 𝔼 p ​ ( X) \mathbb{E}_{q}(X)=\mathbb{E}_{p}(X), 𝔼 q ​ ( H ⁡ ( X)) = 𝔼 p ​ ( H ⁡ ( X)) \mathbb{E}_{q}(H(X))=\mathbb{E}_{p}(H(X)) and 𝔼 q, q ​ ( H ⁡ ( X 1 ​ X 2)) ≤ 𝔼 p, p ​ ( H ⁡ ( X 1 ​ X 2) CLOSE \mathbb{E}_{q,q}(H(X_{1}X_{2}))\leq\mathbb{E}_{p,p}(H(X_{1}X_{2}).

We will do this by proving first for distributions with finite support, inductively by reducing the size of the non-zero support by one at a time.

This will be achieved by the following technical lemma.

###### Lemma 9.

Given numbers p 1, p 2, x 1, x 2 ∈ ( 0, 1] p_{1},p_{2},x_{1},x_{2}\in(0,1], there exists numbers q q and y y such that p 1 ​ x 1 + p 2 ​ x 2 = q ​ y p_{1}x_{1}+p_{2}x_{2}=qy and p 1 ​ H ​ ( x 1) + p 2 ​ H ​ ( x 2) = q ​ H ​ ( y) p_{1}H(x_{1})+p_{2}H(x_{2})=qH(y).

For such q q and y y, the following properties hold:

1. 1.

q ≤ p 1 + p 2 q\leq p_{1}+p_{2},

2. 2.

For all 0 ≤ z ≤ 1 0\leq z\leq 1, p 1 ​ H ​ ( z ​ x 1) + p 2 ​ H ​ ( z ​ x 2) ≥ q ​ H ​ ( z ​ y) p_{1}H(zx_{1})+p_{2}H(zx_{2})\geq qH(zy) and

3. 3.

p 1 2 ​ H ​ ( x 1 2) + 2 ​ p 1 ​ p 2 ​ H ​ ( x 1 ​ x 2) + p 2 2 ​ H ​ ( x 2 2) ≥ q 2 ​ H ​ ( y) 2 p_{1}^{2}H(x_{1}^{2})+2p_{1}p_{2}H(x_{1}x_{2})+p_{2}^{2}H(x_{2}^{2})\geq q^{2}H(y)^{2}.

###### Proof.

Since f: t → H ⁡ ( t) / t f:t\to H(t)/t is onto, there exists y y such that

 | H ⁡ ( y) y = f ⁡ ( y) \displaystyle\frac{H(y)}{y}=f(y) | = p 1 ​ x 1 p 1 ​ x 1 + p 2 ​ x 2 ​ f ​ ( x 1) + p 2 ​ x 2 p 1 ​ x 1 + p 2 ​ x 2 ​ f ​ ( x 2) \displaystyle=\frac{p_{1}x_{1}}{p_{1}x_{1}+p_{2}x_{2}}f(x_{1})+\frac{p_{2}x_{2}}{p_{1}x_{1}+p_{2}x_{2}}f(x_{2}) |  |

 |  | = p 1 ​ H ​ ( x 1) + p 2 ​ h ​ ( x 2) p 1 ​ x 1 + p 2 ​ x 2. \displaystyle=\frac{p_{1}H(x_{1})+p_{2}h(x_{2})}{p_{1}x_{1}+p_{2}x_{2}}. |  |

Thus if we set q = p 1 ​ x 1 + p 2 ​ x 2 y q=\frac{p_{1}x_{1}+p_{2}x_{2}}{y}, the required equalities clearly hold.

By construction, H ⁡ ( y) y \frac{H(y)}{y} is contained in the interval spanned by H ⁡ ( x 1) x 1 \frac{H(x_{1})}{x_{1}} and H ⁡ ( x 2) x 2 \frac{H(x_{2})}{x_{2}}. Since f f is monotonic, it follows that y y is contained in the interval spanned by x 1 x_{1} and x 2 x_{2}. Hence it follows that q ≤ p 1 + p 2 q\leq p_{1}+p_{2}.

Fix 0 ≤ z ≤ 1 0\leq z\leq 1. By Lemma 8, f ⁡ ( z ​ g ​ ( x)) f(zg(x)) is convex. If we write p = p 1 ​ x 1 p 1 ​ x 1 + p 2 ​ x 2 p=\frac{p_{1}x_{1}}{p_{1}x_{1}+p_{2}x_{2}} then since f ⁡ ( y) = p ​ f ​ ( x 1) + ( 1 − p) ​ f ​ ( x 2) f(y)=pf(x_{1})+(1-p)f(x_{2}), it follows that f ⁡ ( z ​ g ​ ( f ⁡ ( y))) ≤ p ​ f ​ ( z ​ g ​ ( f ⁡ ( x 1))) + ( 1 − p) ​ f ​ ( α ​ g ​ ( f ⁡ ( x 2))) f(zg(f(y)))\leq pf(zg(f(x_{1})))+(1-p)f(\alpha g(f(x_{2}))). Since g g and f f are inverse functions, this can be rewritten as f ⁡ ( z ​ y) ≤ p ​ f ​ ( z ​ x 1) + ( 1 − p) ​ f ​ ( z ​ x 2) f(zy)\leq pf(zx_{1})+(1-p)f(zx_{2}), which gives

 | H ⁡ ( z ​ y) y \displaystyle\frac{H(zy)}{y} | ≤ p 1 ​ x 1 p 1 ​ x 1 + p 2 ​ x 2 ​ H ⁡ ( z ​ x 1) x 1 + p 2 ​ x 2 p 1 ​ x 1 + p 2 ​ x 2 ​ H ⁡ ( z ​ x 2) x 2 \displaystyle\leq\frac{p_{1}x_{1}}{p_{1}x_{1}+p_{2}x_{2}}\frac{H(zx_{1})}{x_{1}}+\frac{p_{2}x_{2}}{p_{1}x_{1}+p_{2}x_{2}}\frac{H(zx_{2})}{x_{2}} |  |

 | H ⁡ ( z ​ y) \displaystyle H(zy) | ≤ p 1 ​ x 1 ​ H ⁡ ( z ​ x 1) x 1 + p 2 ​ x 2 ​ H ⁡ ( z ​ x 2) x 2 \displaystyle\leq p_{1}x_{1}\frac{H(zx_{1})}{x_{1}}+p_{2}x_{2}\frac{H(zx_{2})}{x_{2}} |  |

 |  | = p 1 ​ H ​ ( z ​ x 1) + p 2 ​ H ​ ( z ​ x 2). \displaystyle=p_{1}H(zx_{1})+p_{2}H(zx_{2}). |  |

Finally the last inequality comes from the second inequality applied at z = y, x 1 z=y,x_{1} and x 2 x_{2}:

 | q 2 ​ H ​ ( y 2) \displaystyle q^{2}H(y^{2}) | ≤ q ⁡ ( p 1 ​ H ​ ( y ​ x 1) + p 2 ​ H ​ ( y ​ x 2)) \displaystyle\leq q(p_{1}H(yx_{1})+p_{2}H(yx_{2})) |  |

 |  | = p 1 ​ ( q ​ H ​ ( y ​ x 1)) + p 2 ​ ( q ​ H ​ ( y ​ x 2)) \displaystyle=p_{1}(qH(yx_{1}))+p_{2}(qH(yx_{2})) |  |

 |  | ≤ p 1 ​ ( p 1 ​ H ​ ( x 1) 2 + p 2 ​ H ​ ( x 1 ​ x 2)) + p 2 ​ ( p 1 ​ H ​ ( x 1 ​ x 2) + p 2 ​ H ​ ( x 2) 2). \displaystyle\leq p_{1}(p_{1}H(x_{1})^{2}+p_{2}H(x_{1}x_{2}))+p_{2}(p_{1}H(x_{1}x_{2})+p_{2}H(x_{2})^{2}). |  |

∎

This solves the above optimisation problem.

###### Theorem 10.

For any distribution p p on [0, 1] [0,1], there exists a distribution q q on [0, 1] [0,1] with at most one non-zero point in its support, for which 𝔼 q ​ ( X) = 𝔼 p ​ ( X) \mathbb{E}_{q}(X)=\mathbb{E}_{p}(X), 𝔼 q ​ ( H ⁡ ( X)) = 𝔼 p ​ ( H ⁡ ( X)) \mathbb{E}_{q}(H(X))=\mathbb{E}_{p}(H(X)) and 𝔼 q, q ​ ( H ⁡ ( X 1 ​ X 2)) ≤ 𝔼 p, p ​ ( H ⁡ ( X 1 ​ X 2) 𝐶𝐿𝑂𝑆𝐸 \mathbb{E}_{q,q}(H(X_{1}X_{2}))\leq\mathbb{E}_{p,p}(H(X_{1}X_{2}).

###### Proof.

Suppose first that p p is of finite support, but has more than one non-zero point in its support. Let x 1, x 2 x_{1},x_{2} be distinct non-zero points in the support and let p 1 = Pr ⁡ ( X = x 1) p_{1}=\Pr(X=x_{1}) and p 2 = Pr ⁡ ( X = x 2) p_{2}=\Pr(X=x_{2}).

If we let q q and y y be the numbers described in Lemma 9, and make p ′ p^{\prime} be a distribution which is identical to p p but replaces hitting the elements x 1, x 2 x_{1},x_{2} with probability p 1, p 2 p_{1},p_{2} by hitting the elements y, 0 y,0 with probability q, p 1 + p 2 − q q,p_{1}+p_{2}-q, we still have a probability distribution (as 0 ≤ q ≤ p 1 + p 2 0\leq q\leq p_{1}+p_{2}), but with smaller support. Further, by the definition of q q and y y, 𝔼 p ​ ( X) = 𝔼 p ′ ​ ( X) \mathbb{E}_{p}(X)=\mathbb{E}_{p^{\prime}}(X) and 𝔼 p ​ ( H ⁡ ( X)) = 𝔼 p ′ ​ ( H ⁡ ( X)) \mathbb{E}_{p}(H(X))=\mathbb{E}_{p^{\prime}}(H(X)). Further, from the inequalities in Lemma 9, 𝔼 p ′, p ′ ​ ( H ⁡ ( X 1 ​ X 2)) ≤ 𝔼 p, p ​ ( H ⁡ ( X 1 ​ X 2) CLOSE \mathbb{E}_{p^{\prime},p^{\prime}}(H(X_{1}X_{2}))\leq\mathbb{E}_{p,p}(H(X_{1}X_{2}).

Inductively, for any distribution of finite support we can replace two non-zero elements with one repeatedly, maintaining 𝔼 p ​ ( X) \mathbb{E}_{p}(X) and 𝔼 p ​ ( H ​ ( X)) \mathbb{E}_{p}(H(X)) but never increasing 𝔼 p, p ​ ( H ⁡ ( X 1 ​ X 2)) \mathbb{E}_{p,p}(H(X_{1}X_{2})). Eventually we will reach such a distribution q q. This proves the Theorem for all distributions of finite support.

The distributions of finite support are dense in the set of all distributions and these expectations are continuous. As such, we can generalise to all distributions. ∎

We will rewrite this Theorem using the function g g which we defined as the inverse of f ⁡ ( x) = H ⁡ ( x) / x f(x)=H(x)/x.

###### Corollary 11.

For real numbers 0 < t, u < 1 0<t,u<1 with u ≤ H ⁡ ( t) u\leq H(t), the minimum possible value of 𝔼 p, p ​ ( H ⁡ ( X 1 ​ X 2)) \mathbb{E}_{p,p}(H(X_{1}X_{2})) with 𝔼 p ​ ( X) = t \mathbb{E}_{p}(X)=t and 𝔼 p ​ ( H ​ ( x)) = u \mathbb{E}_{p}(H(x))=u is t 2 ​ H ​ ( v 2) / v 2 t^{2}H(v^{2})/v^{2} where v = g ⁡ ( u / t) v=g(u/t).

###### Proof.

This is achievable by the distribution which takes v v with probability t v \frac{t}{v} and 0 with probability 1 − t v 1-\frac{t}{v}, note that f ⁡ ( v) = u / t ≤ H ⁡ ( t) / t = f ⁡ ( t) f(v)=u/t\leq H(t)/t=f(t), so t < v t<v and this is a proper distribution.

To show this is optimal, take any distribution p p. Then we know by Theorem 10 there is a distribution q q on [0, 1] [0,1] with at most one non-zero point in its support for which 𝔼 q ​ ( X) = t \mathbb{E}_{q}(X)=t, 𝔼 q ​ ( H ​ ( X)) = u \mathbb{E}_{q}(H(X))=u and OPEN 𝔼 q, q ​ ( H ⁡ ( X 1) ​ X 2)) ≤ 𝔼 p, p ​ ( H ⁡ ( X 1 ​ X 2)) \mathbb{E}_{q,q}(H(X_{1})X_{2}))\leq\mathbb{E}_{p,p}(H(X_{1}X_{2})).

Since the expectation of X X under q q is non-zero, there is a non-zero point in the support of q q. Let it be v ′ v^{\prime} and the probability be p p.

Then t = p ​ v ′ t=pv^{\prime} and u = p ​ H ​ ( v ′) u=pH(v^{\prime}), so f ⁡ ( v ′) = u / t = f ⁡ ( v) f(v^{\prime})=u/t=f(v) and hence v = v ′ v=v^{\prime} and p = t v p=\frac{t}{v}, so the distribution q q is in fact the construction from the first paragraph of this proof. ∎

###### Proof of Lemma 4.

Let us suppose as defined in the lemma, that for 1 ≤ i ≤ n 1\leq i\leq n, p i p_{i} and w i ∈ [0, 1] w_{i}\in[0,1] are numbers such that ∑ i p i = 1 \sum_{i}p_{i}=1 and ∑ i p i ​ w i ≥ β \sum_{i}p_{i}w_{i}\geq\beta where 1 > β ≥ 5 − 1 2 1>\beta\geq\frac{\sqrt{5}-1}{2}.

Set t = ∑ i p i ​ w i t=\sum_{i}p_{i}w_{i}. Since H H is concave, it follows that 0 ≤ ∑ i p i ​ H ​ ( w i) ≤ H ⁡ ( t) 0\leq\sum_{i}p_{i}H(w_{i})\leq H(t).

Set u = ∑ i p i ​ H ​ ( w i) u=\sum_{i}p_{i}H(w_{i}) and v = g ⁡ ( u / t) v=g(u/t). Then from Corollary 11 it follows that

 | ∑ i ∑ j p i ​ p j ​ H ​ ( w i ​ w j) ≥ t 2 ​ H ​ ( v 2) / v 2. \sum_{i}\sum_{j}p_{i}p_{j}H(w_{i}w_{j})\geq t^{2}H(v^{2})/v^{2}. |  |

Recall that f ⁡ ( v) = u / t ≤ H ⁡ ( t) / t = f ⁡ ( t) f(v)=u/t\leq H(t)/t=f(t) so t < v t<v. From Lemma 6, H ⁡ ( v 2) v ​ H ​ ( v) ≥ H ⁡ ( t 2) t ​ H ​ ( t) \frac{H(v^{2})}{vH(v)}\geq\frac{H(t^{2})}{tH(t)}. Note that this is the only place in the proof we use that β ≥ 5 − 1 2 \beta\geq\frac{\sqrt{5}-1}{2}.

It follows that

 | ∑ i ∑ j p i ​ H ​ ( w i ​ w j) \displaystyle\sum_{i}\sum_{j}p_{i}H(w_{i}w_{j}) | ≥ t 2 ​ H ​ ( v 2) / v 2 \displaystyle\geq t^{2}H(v^{2})/v^{2} |  |

 |  | = t ​ H ⁡ ( v 2) v ​ H ​ ( v) ​ t ​ H ​ ( v) v \displaystyle=t\frac{H(v^{2})}{vH(v)}\frac{tH(v)}{v} |  |

 |  | = t ​ u ​ H ⁡ ( v 2) v ​ H ​ ( v) \displaystyle=tu\frac{H(v^{2})}{vH(v)} |  |

 |  | ≥ t ​ u ​ H ⁡ ( t 2) t ​ H ​ ( t) \displaystyle\geq tu\frac{H(t^{2})}{tH(t)} |  |

 |  | = H ⁡ ( t 2) H ⁡ ( t) ​ ∑ i p i ​ h ​ ( W i) \displaystyle=\frac{H(t^{2})}{H(t)}\sum_{i}p_{i}h(W_{i}) |  |

 |  | ≥ H ⁡ ( β 2 CLOSE H ⁡ ( β) ​ ∑ i p i ​ H ​ ( w i), \displaystyle\geq\frac{H(\beta^{2}}{H(\beta)}\sum_{i}p_{i}H(w_{i}), |  |

the last inequality coming from Lemma 5 ∎

## References

- [1] J. Gilmer, “A constant lower bound for the union-closed sets conjecture,” 2022.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/2211.13138
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/2211.13139
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+2211.13139
[7]: https://arxiv.org/pdf/2211.13139
[8]: /html/2211.13140
