<!-- source: https://arxiv.org/html/1411.4111v1 | converted from HTML -->

Repeated binomial coefficients and high-degree curves

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1411.4111v1 [math.NT] 15 Nov 2014

# Repeated binomial coefficients and high-degree curves

Hugo Jenkins

###### Abstract.

We consider the problem of characterizing solutions in ( x, y) (x,y) to the equation ( x y) = ( x − a y + b) {x\choose y}={{x-a}\choose{y+b}} in terms of a a and b b. We obtain one simple result which allows the determination of a ratio in terms of a a and b b which the ratio x y \frac{x}{y} must approximate. We then add to the understanding of the infinite family of repeated coefficients discovered by D. Singmaster, by using fundamental results from Diophantine geometry to prove that in the case a ≠ b a\neq b, solutions to ( x y) = ( x − a y + b) {x\choose y}={{x-a}\choose{y+b}} are finite. Finally, we make some observations about the potential utility of equations of the form ( x y) = ( x − a y + b) {x\choose y}={{x-a}\choose{y+b}} in proving Singmaster’s conjecture, which is the main unsolved problem in the area of repeated binomial coefficient study. We remark that this approach to the conjecture is markedly different from previous approaches, which have only established logarithmic bounds on a function which counts the number of representations of t t as a binomial coefficient.

## 1. Introduction

The sequence of binomial coefficients is one of the most well-studied, frequently-used, and generally significant sequences in all of mathematics. It is interesting, therefore, that the analysis of repeated binomial coefficients (coefficients which occur more often than the trivial two times which every number occurs) has only received sustained attention in the past 50 years. Clearly, many numbers occur three and four times; these are what fill up the inside of Pascal’s triangle. However, the only other high multiplicities known to occur—6 and 8—are rare, and the patterns in which they appear are not well understood.

However, some scattered progress has been made. It has been shown by Abbott *et al.*[1] that the function N ⁡ ( t) N(t) which counts the number of ways of representing t t as a binomial coefficient has average order and normal order 2. All solutions to ( x 2) = ( y 3) {x\choose 2}={y\choose 3} were found by Avanesov [2, referenced in 10], and Kiss [10] established the more general result of finiteness of solutions to ( x 2) = ( y p) {x\choose 2}={y\choose p}, for p p a prime. ( x 2) = ( y 4) {x\choose 2}={y\choose 4} and ( x 3) = ( y 4) {x\choose 3}={y\choose 4} have also been completely solved by de Weger [17]. More recently, Bugeaud *et al.*[4] have found all solutions to ( x 2) = ( y 5) {x\choose 2}={y\choose 5} using an improvement of the Mordell-Weil sieve, which is applicable to finding integral points on all hyperelliptic curves.

Perhaps the most striking result was found by Lind [11], who showed that if n = F 2 ​ i + 2 ​ F 2 ​ i + 3 − 1 n=F_{2i+2}F_{2i+3}-1 and k = F 2 ​ i ​ F 2 ​ i + 3 − 1 k=F_{2i}F_{2i+3}-1 (where F i F_{i} is the i i -th Fibonacci number), then ( n + 1 k + 1) = ( n k + 2) {{n+1}\choose{k+1}}={n\choose{k+2}}. David Singmaster [16] also provided a proof of this, and noted that his result provides an infinite family of numbers with multiplicity at least 6. The first member of this family—3003—is also the only known number with multiplicity 8. Singmaster [15] also made the following dramatic conjecture, the study of which has been an important feature of subsequent work on repeated binomial coefficients: If N ⁡ ( t) N(t) denotes the number of times t t occurs in Pascal’s triangle, N ⁡ ( t) = O ⁡ ( 1) N(t)=O(1).

There has been no direct attempt at proving the existence of such a finite upper bound on the number of ways t t may be represented as a binomial coefficient. Bounds on N ⁡ ( t) N(t) in terms of t t were obtained first by Singmaster [15], then by Abbott *et al.*[1], and then by Kane [8]. Currently the best unconditional bound is N ⁡ ( t) = O ⁡ ( ( log ⁡ t) ​ ( log ⁡ log ⁡ log ⁡ t) ( log ⁡ log ⁡ t) 3) N(t)=O(\frac{(\log{t})(\log{\log{\log{t}}})}{(\log{\log{t}})^{3}}), obtained by Kane [9] via an argument relating integer solutions of ( x y) = m {x\choose y}=m to derivatives of a function implicitly defined in terms of the Γ \Gamma -function. Conditional on Cramér’s conjecture about small gaps between prime numbers, Abbott *et al.*[1] obtained N ⁡ ( t) = O ⁡ ( ( log ⁡ t) 2 3) N(t)=O((\log{t})^{\frac{2}{3}}).

The purpose here will be to provide information about generalizations of the equation solved by Lind [11] and Singmaster [16]: ( n + 1 k + 1) = ( n k + 2) {{n+1}\choose{k+1}}={n\choose{k+2}}. This is equivalent to ( n k) = ( n − 1 k + 1) {n\choose k}={{n-1}\choose{k+1}}. However, to our knowledge, no studies of equations of the general form ( n k) = ( n − a k + b) {n\choose k}={{n-a}\choose{k+b}} have been made. We will present two independent results about the solutions to such equations; one describes where solutions may occur, and the other asserts the finiteness of solutions (in most cases). We will also provide a rationale for why considering such equations may provide a powerful framework for proving the Singmaster conjecture itself.

## 2. Results

First, we make the following basic proposition about the location of repeats.

###### Proposition.

Let x x, y y, a a, and b b be natural numbers such that a < y a<y; let ζ \zeta be the positive number defined by ζ a + b − ( ζ + 1) a = 0 \zeta^{a+b}-(\zeta+1)^{a}=0. If ( x y) = ( x − a y + b) {x\choose y}={{x-a}\choose{y+b}}, we have x − a − y − b + 1 y + b < ζ < x − y y − a + 1 \frac{x-a-y-b+1}{y+b}<\zeta<\frac{x-y}{y-a+1}.

###### Proof.

First, note the elementary fact that any entry in Pascal’s triangle may be written as the sum of the two entries above it: ( n k) = ( n − 1 k) + ( n − 1 k − 1) {n\choose k}={{n-1}\choose k}+{{n-1}\choose{k-1}}. This process may be iterated to obtain a representation of ( n k) {n\choose k} as a sum of binomial coefficients of any row number less than n n. For example, with two and three iterations, we obtain, respectively,

 | ( n k) = ( n − 2 k − 2) + 2 ​ ( n − 2 k − 1) + ( n − 2 k), {n\choose k}={{n-2}\choose{k-2}}+2{{n-2}\choose{k-1}}+{{n-2}\choose k}, |  |

 | ( n k) = ( n − 3 k − 3) + 3 ​ ( n − 3 k − 2) + 3 ​ ( n − 3 k − 1) + ( n − 3 k). {n\choose k}={{n-3}\choose{k-3}}+3{{n-3}\choose{k-2}}+3{{n-3}\choose{k-1}}+{{n-3}\choose k}. |  |

That the coefficients appearing in the r r -th such iterate correspond to the binomial coefficients of row r r follows from the observation that when generating the coefficient for the next term with k − s k-s, one adds together the coefficients of the current terms with k − s k-s and k − s + 1 k-s+1. This is exactly the process which ordinarily generates the binomial coefficients in Pascal’s triangle.

We therefore may always write the equation ( x y) = ( x − a y + b) {x\choose y}={{x-a}\choose{y+b}} as

(1) |  | ( x − a y − a) + a ​ ( x − a y − a + 1) + ( a 2) ​ ( x − a y − a + 2) ​ ⋯ + ( x − a y) = ( x − a y + b) {{x-a}\choose{y-a}}+a{{x-a}\choose{y-a+1}}+{a\choose 2}{{x-a}\choose{y-a+2}}\dots+{{x-a}\choose{y}}={{x-a}\choose{y+b}} |  |

Next, we note that if k < n 2 k<\frac{n}{2} and n n and k k are large, the ratios of successive binomial coefficients ( n k + 1): ( n k) {n\choose{k+1}}:{n\choose k}, ( n k + 2): ( n k + 1) {n\choose{k+2}}:{n\choose{k+1}}, and so on, are strictly decreasing, and are close to being constant. Specifically, ( n k + 1) / ( n k) = n − k k + 1 {n\choose{k+1}}/{n\choose k}=\frac{n-k}{k+1}. Suppose we call the ratios ( x − a y − a + 1) / ( x − a y − a) {{x-a}\choose{y-a+1}}/{{x-a}\choose{y-a}}, ( x − a y − a + 2) / ( x − a y − a + 1) {{x-a}\choose{y-a+2}}/{{x-a}\choose{y-a+1}}, ( x − a y − a + 3) / ( x − a y − a + 2) {{x-a}\choose{y-a+3}}/{{x-a}\choose{y-a+2}} … r 1 r_{1}, r 2 r_{2}, r 3 r_{3} and so on. Then we may rewrite (1) as

(2) |  | 1 + a ​ r 1 + ( a 2) ​ r 1 ​ r 2 + ( a 3) ​ r 1 ​ r 2 ​ r 3 ​ ⋯ + r 1 ​ r 2 ​ r 3 ​ … ​ r a − 1 = r 1 ​ r 2 ​ r 3 ​ … ​ r a + b 1+ar_{1}+{a\choose 2}r_{1}r_{2}+{a\choose 3}r_{1}r_{2}r_{3}\dots+r_{1}r_{2}r_{3}\dots r_{a-1}=r_{1}r_{2}r_{3}\dots r_{a+b} |  |

When x x and y y are very large in comparison to a a and b b, all the r i r_{i} are approximately the same (because of the expression for the ratio of successive binomial coefficients), and hence by the binomial theorem are all approximately the (positive) solution of ( ζ + 1) a = ζ a + b (\zeta+1)^{a}=\zeta^{a+b}.

(2) would be true if ζ = r 1 = r 2 = r 3 ​ ⋯ = r a + b \zeta=r_{1}=r_{2}=r_{3}\dots=r_{a+b}. However, because of the strict decrease mentioned above, we have r 1 > r 2 > r 3 ​ ⋯ > r a + b r_{1}>r_{2}>r_{3}\dots>r_{a+b}. Suppose, then, that r 1 < ζ r_{1}<\zeta. Then all the r i r_{i} are, and the right side of (2) has experienced a proportional decrease from ζ a + b \zeta^{a+b} which is the product of all the proportional decreases in the individual r i r_{i}. However, the left side cannot have experienced so great a decrease from ( ζ + 1) a (\zeta+1)^{a}, since no term has decreased proportionally more than the right side, and there is one term (the constant, 1) which has not decreased at all. Thus the equation (2) can no longer be true. We apply the same argument to find that r a + b r_{a+b} cannot be greater than ζ \zeta.

Writing out r 1 = ( x − a y − a + 1) / ( x − a y − a) = x − y y − a + 1 r_{1}={{x-a}\choose{y-a+1}}/{{x-a}\choose{y-a}}=\frac{x-y}{y-a+1} and r a + b = ( x − a y + b) / ( x − a y + b − 1) = x − a − y − b + 1 y + b r_{a+b}={{x-a}\choose{y+b}}/{{x-a}\choose{y+b-1}}=\frac{x-a-y-b+1}{y+b} yields the inequality in the Proposition. We must impose the condition a < y a<y, because in reformulating equation (1) as equation (2), we have assumed that we may divide through by the leftmost term ( x − a y − a) {{x-a}\choose{y-a}}, which is nonzero iff a < y a<y. ∎

###### Theorem.

If b ≠ a b\neq a, the equation ( x y) = ( x − a y + b) {x\choose y}={{x-a}\choose{y+b}} has finitely many solutions in natural numbers x x, y y.

Any such equation can be written as the equation of an algebraic curve 𝒞 \mathcal{C}

(3) |  | ∏ r = 0 a + b − 1 ( x − y − r) − ∏ p = 0 a − 1 ( x − p) ​ ∏ q = 1 b ( y + q) = 0 \prod_{r=0}^{a+b-1}(x-y-r)-\prod_{p=0}^{a-1}(x-p)\prod_{q=1}^{b}(y+q)=0 |  |

in x x and y y. For example, the equation ( x y) = ( x − 1 y + 1) {x\choose y}={{x-1}\choose{y+1}}, which Singmaster [16] solved, corresponds to the curve ( x − y) ​ ( x − y − 1) − x ⁡ ( y + 1) = 0 (x-y)(x-y-1)-x(y+1)=0. This means that the proof of the theorem is reduced to the well-studied problem of determining whether an algebraic curve has an infinity of lattice points. For an individual curve, the standard approach to such a problem is to determine that the curve is irreducible and has genus greater than 0. If so, then by Siegel’s theorem [7, p. 353] the set of lattice points on the curve is finite. However, determining the genus alone requires an analysis of singularities [7, p. 72]. This, in turn, amounts to solving the system where the three partial derivatives of the homogeneous version of the curve are simultaneously equated to zero [5, p. 19]; a task which appears to be unattackable for general curves of this complexity.

We therefore will not attempt to prove that Siegel’s theorem is directly applicable to these curves, but instead will make use of the following criterion given by Nagell (originally due to Maillet) [12, p. 264].

A unicursal [genus 0] curve passes through an infinity of lattice points if and only if there exists a parametric representation of the form

 | x = f ⁡ ( t) ( h ⁡ ( t)) n, y = g ⁡ ( t) ( h ⁡ ( t)) n x=\frac{f(t)}{(h(t))^{n}},\hskip 48.36967pty=\frac{g(t)}{(h(t))^{n}} |  |

where n n is a natural number, and where f ⁡ ( t) f(t), g ⁡ ( t) g(t), and h ⁡ ( t) h(t) are integral polynomials in t t satisfying one of the following conditions:

1. Either h ⁡ ( t) = a ​ t + b h(t)=at+b with gcd ⁡ a, b = 1 \gcd{a,b}=1 or h ⁡ ( t) = 1 h(t)=1; f ⁡ ( t) f(t) and g ⁡ ( t) g(t) are both of degree n n;

2. h ⁡ ( t) = a ​ t 2 + b ​ t + c h(t)=at^{2}+bt+c is irreducible, and a > 0 a>0, b 2 − 4 ​ a ​ c > 0 b^{2}-4ac>0; f ⁡ ( t) f(t) and g ⁡ ( t) g(t) are both of degree 2 ​ n 2n; the form a ​ u 2 + b ​ u ​ v + c ​ v 2 au^{2}+buv+cv^{2} can represent for integral values of u u and v v a certain integer k ≠ 0 k\neq 0 such that k n k^{n} divides all the coefficients of both f ⁡ ( t) f(t) and g ⁡ ( t) g(t).

Nagell goes on to state that shortly after Maillet gave this criterion, Siegel proved that it applies to all curves (i.e. not just unicursal ones).

To apply this criterion to our curves, it will be necessary to consider the limiting behavior as y → ∞ y\rightarrow\infty. We may assume the curves have points of arbitrarily large y y; if they did not, they could not have arbitrarily large x x either (since clearly lim y → ∞ x y ≠ ∞ \lim_{y\to\infty}\frac{x}{y}\neq\infty) and so could only pass through finitely many points with natural x x, y y, which are the only points which matter for the theorem about binomial coefficients.

Qualitatively, it is clear that lim y → ∞ x y \lim_{y\to\infty}\frac{x}{y} must be such that the highest total degree terms in the equation of 𝒞 \mathcal{C} almost cancel each other out as y → ∞ y\rightarrow\infty. Formally if T n T_{n} is the n n -th term with total degree a + b a+b,

(4) |  | lim y → ∞ ∑ T n y a + b = 0, \lim_{y\to\infty}\frac{\sum T_{n}}{y^{a+b}}=0, |  |

because otherwise, for large y y, the value of ∑ T n \sum T_{n} would be the only O ⁡ ( y a + b) O(y^{a+b}) term in 𝒞 \mathcal{C}. There would be other terms O ⁡ ( y a + b − 1) O(y^{a+b-1}), O ⁡ ( y a + b − 2) O(y^{a+b-2}), and so on, but even a direct sum of these is not O ⁡ ( y a + b) O(y^{a+b}), and they clearly are not all summed together.

What is the sum of the highest total degree terms in (3)? The degree a + b a+b terms from the first product, ∏ r = 0 a + b − 1 ( x − y − r) \prod_{r=0}^{a+b-1}(x-y-r), are simply the terms of ( x − y) a + b (x-y)^{a+b}. There is only one degree a + b a+b term in the second product; it is x a ​ y b x^{a}y^{b}. Equation (4) then becomes

 | lim y → ∞ ( x − y) a + b − x a ​ y b y a + b = 0; \lim_{y\to\infty}\frac{(x-y)^{a+b}-x^{a}y^{b}}{y^{a+b}}=0; |  |

 | lim y → ∞ ( x a + b y a + b − ( a + b 1) ​ x a + b − 1 y a + b − 1 + ( a + b 2) ​ x a + b − 2 y a + b − 2 ​ ⋯ − x a y a) = 0. \lim_{y\to\infty}\left(\frac{x^{a+b}}{y^{a+b}}-{{a+b}\choose 1}\frac{x^{a+b-1}}{y^{a+b-1}}+{{a+b}\choose 2}\frac{x^{a+b-2}}{y^{a+b-2}}\dots-\frac{x^{a}}{y^{a}}\right)=0. |  |

Therefore, if we take c = lim y → ∞ x y c=\lim_{y\to\infty}\frac{x}{y}, we must have ( c − 1) a + b − c a = 0 (c-1)^{a+b}-c^{a}=0.

Now, consider the form of lim y → ∞ x y \lim_{y\to\infty}\frac{x}{y} if there exists a parametric representation as described in Nagell’s [12, p. 264] criterion. If h ⁡ ( t) = 1 h(t)=1, y = g ⁡ ( t) y=g(t), and y y goes to ∞ \infty as t t does. This means that lim y → ∞ x y = lim t → ∞ f ⁡ ( t) g ⁡ ( t) \lim_{y\to\infty}\frac{x}{y}=\lim_{t\to\infty}\frac{f(t)}{g(t)}, which has a constant, rational value, because f ⁡ ( x) f(x) and g ⁡ ( x) g(x) are integral polynomials of the same degree in t t. This cannot be the case, because a simple application of the rational root test shows that c c is irrational.

By Nagell’s criterion, it must then be that x x and y y are given by rational functions of t t with numerator and denominator polynomials of the same degree. Then y y can only approach infinity when t t approaches one of the roots of the denominator, h ⁡ ( t) h(t), i. e. when t t approaches either a rational or quadratic irrational number α \alpha. We thus have that c = lim y → ∞ x y = lim t → α f ⁡ ( t) g ⁡ ( t) c=\lim_{y\to\infty}\frac{x}{y}=\lim_{t\to\alpha}\frac{f(t)}{g(t)}. lim t → α f ⁡ ( t) g ⁡ ( t) \lim_{t\to\alpha}\frac{f(t)}{g(t)} is clearly the quotient of two quadratic irrationals; because f f and g g have the same input α \alpha, the number under the radical in both quadratic irrationals is the same. This means that the quotient is itself a quadratic irrational, by rationalization of denominators. We will now show that if a ≠ b a\neq b, c c cannot be a quadratic irrational, and hence no parametrization of the type described can exist. For convenience, we will work with the equation c a + b − ( c + 1) a = 0 c^{a+b}-(c+1)^{a}=0, instead of the original ( c − 1) a + b − c a = 0 (c-1)^{a+b}-c^{a}=0; the former is shifted 1 unit to the left, and obviously has quadratic zeros iff the original does.

###### Lemma.

If n n and r r are such that n > r n>r and n r ≠ 2 \frac{n}{r}\neq 2, the polynomial P ⁡ ( x) = x n − ( x + 1) r P(x)=x^{n}-(x+1)^{r} has no real roots of degree 2.

###### Proof.

We will attack this by showing that it is impossible for P P to have a quadratic factor with positive discriminant. We begin by noting that since P ⁡ ( x) P(x) is primitive, by Gauss’ lemma [13, p. 49], it suffices to consider quadratic factors with integral coefficients. Since the first and last terms of P ⁡ ( x) P(x) have magnitude 1, any such factor must be of the form ± x 2 + b ​ x ± 1 \pm x^{2}+bx\pm 1 or ± x 2 + b ​ x ∓ 1 \pm x^{2}+bx\mp 1, with b ∈ ℤ b\in\mathbb{Z}.

Also note that by Descartes’ sign test, P ⁡ ( x) P(x) has exactly 1 positive root. Make the substitution x ↦ x − 1 x\mapsto x-1, generating the new polynomial G ⁡ ( x) = ( x − 1) n − x r G(x)=(x-1)^{n}-x^{r}, which has been shifted 1 unit to the right. Substituting − x -x for x x in G G, we see that regardless of the parity of n n and r r, there are no sign changes. Thus, G G has no negative roots. We conclude that P ⁡ ( x) P(x) has no negative roots smaller than − 1 -1.

We have P ⁡ ( 0) = − 1 P(0)=-1, and P ⁡ ( − 1) = ± 1 P(-1)=\pm 1, depending on whether n n is even or odd. This means that any quadratic factor Q Q must take the values ± 1 \pm 1 at x = 0 x=0 and x = − 1 x=-1. If Q ⁡ ( − 1) = 1 Q(-1)=1, we have the following four cases:

 | Q ⁡ ( − 1) = 1 = ( − 1) 2 + b × ( − 1) + 1 Q(-1)=1=(-1)^{2}+b\times(-1)+1 |  |

 | Q ⁡ ( − 1) = 1 = − ( − 1) 2 + b × ( − 1) − 1 Q(-1)=1=-(-1)^{2}+b\times(-1)-1 |  |

 | Q ⁡ ( − 1) = 1 = ( − 1) 2 + b × ( − 1) − 1 Q(-1)=1=(-1)^{2}+b\times(-1)-1 |  |

 | Q ⁡ ( − 1) = 1 = − ( − 1) 2 + b × ( − 1) + 1 Q(-1)=1=-(-1)^{2}+b\times(-1)+1 |  |

which yield, respectively, b = 1 b=1, b = − 3 b=-3, b = − 1 b=-1, and b = − 1 b=-1. The values obtained by the same process for Q ⁡ ( − 1) = − 1 Q(-1)=-1 are, in order, b = 3 b=3, b = − 1 b=-1, b = 1 b=1, and b = 1 b=1. The four cases where the first and last terms of Q Q have the same sign generate only two polynomials with distinct roots, as do the cases where they have opposite signs. The complete list of quadratic factors of x n − ( x + 1) r x^{n}-(x+1)^{r} to be considered is thus

 | x 2 + x + 1 x 2 + 3 ​ x + 1 x 2 − x − 1 x 2 + x − 1 x^{2}+x+1\hskip 28.45274ptx^{2}+3x+1\hskip 28.45274ptx^{2}-x-1\hskip 28.45274ptx^{2}+x-1 |  |

The first has no real roots. The second has a root − 3 2 − 5 2 -\frac{3}{2}-\frac{\sqrt{5}}{2}, which is less than − 1 -1; therefore it cannot be a factor, by the sign test performed earlier. Neither can the last, because of the root − 1 2 − 5 2 -\frac{1}{2}-\frac{\sqrt{5}}{2}.

The only possible quadratic factor is thus x 2 − x − 1 x^{2}-x-1. We observe that if n r = 2 \frac{n}{r}=2, this *is*a factor, as can be seen from writing x 2 ​ r − ( x + 1) r = 0 x^{2r}-(x+1)^{r}=0, adding one term to the other side, and taking roots. It is then easily seen that no other polynomials x n − ( x + 1) r x^{n}-(x+1)^{r} can share this factor, for if they did, the difference x 2 ​ r − ( x + 1) r − ( x n − ( x + 1) r) = x 2 ​ r − x n x^{2r}-(x+1)^{r}-(x^{n}-(x+1)^{r})=x^{2r}-x^{n} must also share the factor, which it clearly does not. This proves the lemma, and by extension the theorem. ∎

## 3. Analysis of Methods and Intuitive Explanation

The results obtained here describe instances where the numbers in a particular “configuration” in the triangle are the same. The most basic instance of this, the “configuration”

[image: [Uncaptioned image]]

was shown by Singmaster [16] and Lind [11] to occur infinitely many times; in fact, precisely when n n and k k are certain expressions given by Fibonacci numbers. We have shown that configurations such as

[image: [Uncaptioned image]]

and [image: [Uncaptioned image]]

can occur only finitely many times, if at all. But we have *not*shown, for example, that

[image: [Uncaptioned image]]

and [image: [Uncaptioned image]]

occur finitely many times, because in those cases the difference in k k -values is equal to the difference in n n -values, and the associated polynomial x 2 ​ r − ( x + 1) r x^{2r}-(x+1)^{r} has the quadratic irrational roots φ \varphi and − 1 φ -\frac{1}{\varphi}. However, the assertion that solutions are finite is still nothing more than asserting that a certain subclass of the curves studied are irreducible and have fewer than the maximum allowable number of singularities ( ( d − 1) ​ ( d − 2) 2 \frac{(d-1)(d-2)}{2} [7, p. 72], barring the possibility of non-ordinary singularities), something which seems very likely.

We will now analyze one of the higher-degree analogues to the curve ( x − y) ​ ( x − y − 1) − x ⁡ ( y + 1) = 0 (x-y)(x-y-1)-x(y+1)=0 in order to illustrate the validity of this idea. As we will see, the reason this is difficult in general is because of the necessity of computing a Gröbner basis to determine that the polynomial and its two partial derivatives share no common zeros.

In the case of the next curve with possibly infinite lattice points (the curve with a = 2 a=2, b = 2 b=2; defined by F ⁡ ( x, y) = ( x − y) ​ ( x − y − 1) ​ ( x − y − 2) ​ ( x − y − 3) − x ⁡ ( x − 1) ​ ( y + 1) ​ ( y + 2) = 0 F(x,y)=(x-y)(x-y-1)(x-y-2)(x-y-3)-x(x-1)(y+1)(y+2)=0), we may mechanically compute the Gröbner basis [13, pp. 221, 237] for the system F = ∂ F ∂ x = ∂ F ∂ y = 0 F=\frac{\partial F}{\partial x}=\frac{\partial F}{\partial y}=0 [5, p. 19] to see that there are no affine singularities. If we then homogenize coordinates, and consider the system ∂ F ∂ x = ∂ F ∂ y = ∂ F ∂ z = 0 \frac{\partial F}{\partial x}=\frac{\partial F}{\partial y}=\frac{\partial F}{\partial z}=0 [5, p. 19] at z = 0 z=0, we see that the only solution must be [x: y: z] = [0: 0: 0] [x:y:z]=[0:0:0], which is not a valid point [7, p. 12]. This is because ∂ F ∂ x \frac{\partial F}{\partial x}, ∂ F ∂ y \frac{\partial F}{\partial y}, and ∂ F ∂ z \frac{\partial F}{\partial z} are all homogeneous polynomials in x x and y y when z = 0 z=0. By the same argument we have used to determine lim y → ∞ x y \lim_{y\to\infty}\frac{x}{y}, any homogeneous polynomial in two variables represents the union of some (possibly complex) lines through the origin. None of these lines are the same, and thus the only solution to this system is ( 0, 0) (0,0). We conclude that F F has no singularities.

We may therefore apply the genus-degree formula without subtraction of additional terms: g = ( d − 1) ​ ( d − 2) 2 = 3 × 2 2 = 3 g=\frac{(d-1)(d-2)}{2}=\frac{3\times 2}{2}=3 [7, p. 72]. That F F is irreducible follows immediately from its being nonsingular, for by Bézout’s theorem [7, p. 84], any hypothetical components of F F must intersect somewhere in the complex projective plane, and thus create a singularity in F F. By Siegel’s theorem [7, p. 353], therefore, the set of lattice points is finite.

In the Proposition, we have shown that if a certain configuration occurs entirely within the triangle, the smooth function giving the ratio of one binomial coefficient to the preceding one must take a value ζ \zeta (1 plus the root of the associated polynomial) between the “beginning” of the configuration and the “end”.

This is essentially a precise way of stating that all the occurrences of a particular configuration have approximately the same ratio n k \frac{n}{k}. The restriction y > a y>a, which was algebraically necessary to avoid dividing by zero, corresponds to requiring that the configuration is not “cut off” by the edge of the triangle. All currently known nontrivial repetitions (excluding Singmaster’s [16]) occur so close to the side of the triangle that the Proposition does not apply; however, it is still satisfied, because the ratios on the edge are very large and change very rapidly. It is easily seen that there cannot be more than a a of the “cutoff” cases, because for each y y, there is clearly at most one x x where ( x y) = ( x − a y + b) {x\choose y}={{x-a}\choose{y+b}}.

In the case of Singmaster’s infinite family, the ratio φ \varphi is always less than ( n − 1 k + 1) / ( n − 1 k) {{n-1}\choose{k+1}}/{{n-1}\choose k}, and greater than ( n − 1 k) / ( n − 1 k − 1) {{n-1}\choose k}/{{n-1}\choose{k-1}}. This can also be seen as a direct result of working out ratios of the given expressions involving Fibonacci numbers ( n = F 2 ​ i + 2 ​ F 2 ​ i + 3 − 1 n=F_{2i+2}F_{2i+3}-1 and k = F 2 ​ i ​ F 2 ​ i + 3 − 1 k=F_{2i}F_{2i+3}-1). It works out that the ratios ( n − 1 k + 1) / ( n − 1 k) {{n-1}\choose{k+1}}/{{n-1}\choose k} and ( n − 1 k) / ( n − 1 k − 1) {{n-1}\choose k}/{{n-1}\choose{k-1}} are ratios of successive pairs of Fibonacci numbers—successive continued fraction convergents to φ \varphi. In this sense, the coefficient repetition occurs at all the “best possible” approximations to φ \varphi. It is tempting to think that this is somehow necessary for repetitions to occur, and then to try and disprove the existence of *any*other repeats “deep” in the triangle by proving that convergents to the other, non-quadratic ratios cannot occur sequentially in this way. This seems plausible because, even without invoking the more rapid continued fraction convergence properties of higher degree algebraic numbers, we have that the maximum difference between consecutive continued fraction convergents with first denominator q q is less than 3 2 ​ q 2 \frac{3}{2q^{2}} [6, p. 152], which is very often less than the difference n + 1 ( k + 1) ​ ( k + 2) \frac{n+1}{(k+1)(k+2)} between consecutive coefficient ratios. However, there is no such obvious argument for the “necessity” of continued fraction convergence.

## 4. Possible Extensions

The most obvious extension of our work would be to show that the curve defined by ( x − y) ​ ( x − y − 1) − x ⁡ ( y + 1) = 0 (x-y)(x-y-1)-x(y+1)=0 is the only one of this family of curves which passes through infinitely many lattice points, i. e. to extend the Theorem to the case when a = b a=b and a ≠ 1 a\neq 1. To do that, an entirely different argument to the one used in this paper would be necessary, since we have relied on the fact that the limiting ratio of x x to y y in most cases is not quadratic. If a = b a=b, it is quadratic, and there is no apparent way to prove that Nagell’s [12, p. 264] criterion cannot be satisfied. It is possible that the symmetry of the polynomial defining the curve when a = b a=b allows a simple algebraic manipulation of the system where it and its two partial derivatives are set equal to 0, such that an inconsistency is derived. As we have seen from the previous consideration of ( x − y) ​ ( x − y − 1) ​ ( x − y − 2) ​ ( x − y − 3) − x ⁡ ( x − 1) ​ ( y + 1) ​ ( y + 2) = 0 (x-y)(x-y-1)(x-y-2)(x-y-3)-x(x-1)(y+1)(y+2)=0, we may work with this system, instead of ∂ F ∂ x = ∂ F ∂ y = ∂ F ∂ z = 0 \frac{\partial F}{\partial x}=\frac{\partial F}{\partial y}=\frac{\partial F}{\partial z}=0, because the absence of singular points at infinity follows easily for all these curves.

Another idea would be to try and use the fact that ( x − y) ​ ( x − y − 1) − x ⁡ ( y + 1) = 0 (x-y)(x-y-1)-x(y+1)=0 is nonsingular in order to establish the non-singularity of the higher-degree curves by induction. If we designate the first large product in the equation of one of our curves as G ⁡ ( x, y) G(x,y), and the second as R ⁡ ( x, y) R(x,y), we may write the curve as G ⁡ ( x, y) = R ⁡ ( x, y) G(x,y)=R(x,y). If G ⁡ ( x, y) = R ⁡ ( x, y) G(x,y)=R(x,y) is the equation of a curve with a = b = n a=b=n, then the equation of the curve with a = b = n + 1 a=b=n+1 is ( x − y − 2 ​ n) ​ ( x − y − 2 ​ n − 1) ​ G ​ ( x, y) = ( x − n) ​ ( y + n + 1) ​ R ​ ( x, y) (x-y-2n)(x-y-2n-1)G(x,y)=(x-n)(y+n+1)R(x,y); in other words, when n n increases by 1, the equation is “multiplied” by a shifted version of ( x − y) ​ ( x − y − 1) = x ⁡ ( y + 1) (x-y)(x-y-1)=x(y+1). If this kind of “multiplication” of two nonsingular curves could be shown to preserve non-singularity, we would have an induction argument to extend the Theorem.

* * *

The conclusions we have reached here are significant in their own right: they are, to our knowledge, the first fundamental results established concerning equations of the general form ( x y) = ( x − a y + b) {x\choose y}={{x-a}\choose{y+b}}, where x x and y y vary. This is fundamentally different than considering ( n k) = ( s r) {n\choose k}={s\choose r} and allowing, say, k k and r r to vary (an area in which some progress in bounding and tabulating solutions has already been made [2, referenced in 10] [10] [17] [4]).

However, it is hardly debatable that the most ambitious and important goal in the examination of repeated coefficients is the proof of Singmaster’s [15] conjecture. So far, the most pointed attacks on the conjecture have resulted only in an increasingly tight series of logarithmic bounds—an approach which *a priori*seems unlikely to yield the desired O ⁡ ( 1) O(1) result. Kane [8] has stated that his method—which initially yielded O ⁡ ( log ⁡ t ​ log ⁡ log ⁡ log ​ t ( log ⁡ log ⁡ t) 2) O(\frac{\log{t}\log{\log{\log{t}}}}{(\log{\log{t}})^{2}}), and then was improved by a factor of log ⁡ log ⁡ t \log{\log{t}} [9]—probably cannot be further extended. It may be more fruitful, therefore, to cease considering N ⁡ ( t) N(t) as a function to be bounded, and instead only to try analyze when particularly high multiplicities of t t occur. We have not done this; our concern has simply been with a certain type of nontrivial repetition. However, a large part of the value of our exploration lies in the fact that the algebraic curves we have used would seem to provide a good basis for pursuing this.

Notice, for instance, that a coefficient occurring six times simply corresponds to an integral intersection between two of our curves beyond a certain x x -value (the degree of the higher degree curve). A multiplicity of eight corresponds to three curves intersecting at the same point, and so on. Furthermore, any set of the curves has at least some easily calculable number of these common intersections, because of the trivial integral points near the origin which they all share. These correspond to repetitions in the negative triangle. Each large-multiplicity integral intersection between these curves also corresponds to a large integral point on a curve of much lower degree; specifically, if m m curves with highest degree n n intersect at ( a, b) (a,b), there is an integral point on a curve of degree at most m n \frac{m}{n} with greater x x and y y coordinates than ( a − n, b) (a-n,b).

The Singmaster [15] conjecture would be proved by bounding the number of these curves which can share a common intersection beyond a given x x -value (although this statement is stronger than is necessary; the conjecture only considers integral intersections).

The naïve way to do this would be to take a general set of some number of these curves, shift them left sufficiently far, and try to show via Nullstellensatz manipulations [13, p. 22] (generating other polynomials in the same ideal) that there could not be a common intersection in the first quadrant. The difficulty, of course, lies in working generally with curves of arbitrary complexity. It should be noted, however, that because of the fact that the Nullstellensatz deals with all intersections, not just integral ones, this strategy is not equivalent to simply manipulating general binomial coefficients themselves. Even if the task is still seemingly difficult, we are able to utilize a more powerful tool.

*Figs. 1-3. Several of the curves we have considered. The first nontrivial intersection occurs between a = 104 a=104, b = 1 b=1, and a = 110 a=110, b = 2 b=2. It corresponds to ( 120 1) = ( 16 2) = ( 10 3) {120\choose 1}={16\choose 2}={10\choose 3}.*

[image: [Uncaptioned image]]

*Fig. 1. Singmaster’s curve: a = 1 a=1, b = 1 b=1

*

[image: [Uncaptioned image]]

*Fig. 2. a = 1 a=1, b = 2 b=2*

[image: [Uncaptioned image]]

*Fig. 3. a = 5 a=5, b = 3 b=3*

Advanced tools of algebraic geometry are also possibly applicable to this reformulation of the conjecture, although a major strengthening of current knowledge would certainly be necessary first. If a general effective form of Siegel’s theorem [7, p. 353] were known, it would be possible to bound the “height” of integral points on these curves (their coordinate size, essentially). However, the currently known effective methods for genus 1 curves, such as Baker’s [3, p. 45] method, generate bounds too large (triple exponential) to be useful, even if they were generalized. More desirable (and more difficult) would be an effective Schmidt subspace theorem, as this would result in an effective form of a corollary [14, p. 5] on simultaneous approximation of algebraic numbers:

Let α 1 \alpha_{1}, … α n \alpha_{n} be algebraic numbers such that 1 1, α 1 \alpha_{1}, … α n \alpha_{n} are linearly independent over the rationals. Then for any ϵ > 0 \epsilon>0 there are only finitely many integers p 1 p_{1}, … p n p_{n}, q q with q > 0 q>0 such that

 | | α 1 − p 1 q | < q − 1 − 1 / n − ϵ, … ​ | α n − p n q | < q − 1 − 1 / n − ϵ. \lvert\alpha_{1}-\frac{p_{1}}{q}\rvert<q^{-1-1/n-\epsilon},\dots\lvert\alpha_{n}-\frac{p_{n}}{q}\rvert<q^{-1-1/n-\epsilon}. |  |

If we could find the ratios p i q \frac{p_{i}}{q} where the various algebraic numbers ζ \zeta associated with a set of our curves are simultaneously approximated, we could find the intersection point. Unfortunately, we have not yet provided a requirement that the approximations to ζ \zeta be as close as is dictated in the corollary.

The Singmaster conjecture remains as Paul Erdős once described it [cited in 15, p. 385]: a “very hard” problem. The intent here has been only to introduce a novel form for viewing repeated binomial coefficient problems to which the well-developed tools of 20th century mathematics are at least somewhat applicable. Whether this method can yield a truly new understanding of such an antique, basic, elementary part of mathematics, remains to be seen.

## References

[1] Abbott, H. L.; Erdős, P.; Hanson, D. *On the number of times an integer occurs as a binomial coefficient*. Amer. Math. Monthly 81 (1974): 256-261. MR0335283 (49 #65)

[2] Avanesov, È. T. *Solution of a problem on figurate numbers*. (Russian) Acta Arithm. 12 (1966/1967): 409-420. �MR0215784 (35 #6619)

[3] Baker, A. *Transcendental number theory*. Cambridge University Press, London-New York, 1975.� MR0422171 (54 #10163)

[4] Bugeaud, Y.; Mignotte, M.; Siksek, S.; Stoll, M.; Tengely, Sz. *Integral points on hyperelliptic curves*. Algebra & Number Theory 2 (2008), no. 8: 859-885.� arXiv:0801.4459

[5] Coolidge, J. L. *A treatise on algebraic plane curves*. Dover Publications, New York, 1959 [1931]. MR0120551 (22 #11302)

[6] Hardy, G. H.; Wright, E. M. *An introduction to the theory of numbers*. 3rd. edn., Oxford University Press, New York, 1954 [1938]. MR0067125

[7] Hindry, M.; Silverman, J. H. *Diophantine geometry: an introduction*. Graduate Texts in Mathematics, 201, Springer, New York, 2000.� MR1745599 (2001e:11058)

[8] Kane, D. M. *New bounds on the number of representations of t as a binomial coefficient*. Integers: Electronic J. of Combinatorial Number Theory 4 (2004), #A07: 1-10. �MR2056013

[9] Kane, D. M. *Improved bounds on the number of ways of expressing t as a binomial coefficient*. Integers: Electronic� J. of Combinatorial Number Theory 7 (2007), #A53: 1-7.� MR2373115 (2008m:05014)

[10] Kiss, P. *On the number of solutions of the Diophantine equation \ \backslash binom(x, p) = \ \backslash binom(y, 2)*. Fib. Quart. 26 (1988), no. 2: 127-129. �MR0938585 �(89f:11050)

[11] Lind, D. A. *The quadratic field Q( 5 \sqrt{5}) and a certain Diophantine equation*. Fib. Quart. 6 (1968), no. 3: 86-93.� MR0231784 �(38 #112)

[12] Nagell, T. *Introduction to number theory*. 2nd edn., Chelsea Publishing Company, New York, 1964 [1951].

[13] Prasolov, V. V. *Polynomials*, trans. D. Leites. Algorithms and Computation in Mathematics, 11, Springer, Berlin, 2004. �MR2082772 (2005f:12001)

[14] Schlickewei, H. P. *The mathematical work of Wolfgang Schmidt*. In Schlickewei, H. P.; Tichy, R. F.; Schmidt, K. D., eds. *Diophantine approximation: festschrift for Wolfgang Schmidt*. Springer, Vienna-New York, 2000: 1-14.

[15] Singmaster, D. *How often does an integer occur as a binomial coefficient?*Amer. Math. Monthly 78 (1971), no. 4: 385-386.� MR1536288

[16] Singmaster, D. *Repeated binomial coefficients and Fibonacci numbers*. Fib. Quart. 13 (1975), no. 4: 295-298. MR0412095 (54 #224)

[17] de Weger, B. M. M. *Equal binomial coefficients: some elementary considerations*. J. Number Theory 63 (1997), no. 2: 373-386.� MR1443768 (98b:11027)


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
