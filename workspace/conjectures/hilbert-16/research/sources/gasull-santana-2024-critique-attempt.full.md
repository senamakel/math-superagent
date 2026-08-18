<!-- source: https://arxiv.org/html/2411.09594v1 | converted from HTML -->

A note on a recent attempt to solvethe second part of Hilbert’s 16th Problem

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2411.09594v1 [math.DS] 14 Nov 2024

# A note on a recent attempt to solve
the second part of Hilbert’s 16th Problem

Claudio A. Buzzi 1 and Douglas D. Novaes 2 Address: 1 Universidade Estadual Paulista, IBILCE-UNESP - Av. Cristovão Colombo, 2265, 15.054-000, S. J. Rio Preto, SP, Brasil Email address: [claudio.buzzi@unesp.br][3] Address: 2 Universidade Estadual de Campinas (UNICAMP), Departamento de Matemática, Instituto de Matemática, Estatística e Computação Científica (IMECC) - Rua Sérgio Buarque de Holanda, 651, Cidade Universitária Zeferino Vaz, 13083–859, Campinas, SP, Brasil Email address: [ddnovaes@unicamp.br][4]

###### Abstract.

For a given natural number n n, the second part of Hilbert’s 16th Problem asks whether there exists a finite upper bound for the maximum number of limit cycles that planar polynomial vector fields of degree n n can have. This maximum number of limit cycle, denoted by H ⁡ ( n) H(n), is called the n n th Hilbert number. It is well-established that H ⁡ ( n) H(n) grows asymptotically as fast as n 2 ​ log ⁡ n n^{2}\log n. A direct consequence of this growth estimation is that H ⁡ ( n) H(n) cannot be bounded from above by any quadratic polynomial function of n n. Recently, the authors of the paper [Exploring limit cycles of differential equations through information geometry unveils the solution to Hilbert’s 16th problem. Entropy, 26(9), 2024] affirmed to have solved the second part of Hilbert’s 16th Problem by claiming that H ⁡ ( n) = 2 ​ ( n − 1) ​ ( 4 ​ ( n − 1) − 2) H(n)=2(n-1)(4(n-1)-2). Since this expression is quadratic in n n, it contradicts the established asymptotic behavior and, therefore, cannot hold. In this note, we further explore this issue by discussing some counterexamples.

###### Key words and phrases:

limit cycles, Hilbert’s 16th Problem, Hilbert number, asymptotic growth estimation

###### 2010 Mathematics Subject Classification

34C07, 34C23, 37G15

## 1. Introduction

For a given natural number n n, the second part of Hilbert’s 16th Problem asks whether there is a finite upper bound for the number of limit cycles that planar polynomial vector fields of degree n n can possess. More precisely, let

 | H ( n):= sup { π ( P, Q): deg ( P), deg ( Q) ≤ n }, H(n):=\sup\{\pi(P,Q):\deg(P),\deg(Q)\leq n\}, |  |

where π ⁡ ( P, Q) \pi(P,Q) denotes the number of limit cycles of the polynomial differential system

(1) |  | { x ˙ = P ⁡ ( x, y), y ˙ = Q ⁡ ( x, y). \begin{cases}\dot{x}=P(x,y),\\ \dot{y}=Q(x,y).\end{cases} |  |

Recall that a limit cycle of ( 1) is a (non-stationary) periodic orbit that is isolated from other periodic orbits (see [8, Definition 9]). Thus, the second part of Hilbert’s 16th Problem consists of proving that H ⁡ ( n) < ∞ H(n)<\infty for all n ∈ ℕ n\in\mathbb{N} (see [8, Chapter 2]). The value H ⁡ ( n) H(n) is called the n n th Hilbert number.

The most significant advancement in understanding the asymptotic behavior of the function H ⁡ ( n) H(n) was made by Christopher and Lloyd in [2], who introduced a method showing that H ⁡ ( n) H(n) grows as fast as n 2 ​ log ⁡ n n^{2}\log n. This classical result has been revisited and improved by several works, including [1, 4, 5]. In particular, Han and Li in [4] refined Christopher and Lloyd’s result, demonstrating that H ⁡ ( n) H(n) grows at least as fast as ( n + 2) 2 ​ log ⁡ ( n + 2) / ( 2 ​ log ⁡ 2) (n+2)^{2}\log(n+2)/(2\log 2) by establishing that

 | lim n → ∞ inf H ⁡ ( n) ( n + 2) 2 ​ log ⁡ ( n + 2) ≥ 1 2 ​ log ⁡ 2. \lim_{n\to\infty}\inf\dfrac{H(n)}{(n+2)^{2}\log(n+2)}\geq\dfrac{1}{2\log 2}. |  |

This remains the best-known lower estimation for the asymptotic growth of H ⁡ ( n) H(n).

A direct conclusion from this asymptotic growth estimation is that H ⁡ ( n) H(n) cannot be bounded from above by any quadratic polynomial function in n n, as the expression ( n + 2) 2 ​ log ⁡ ( n + 2) / ( 2 ​ log ⁡ 2) (n+2)^{2}\log(n+2)/(2\log 2) surpasses any degree two polynomial in n n for sufficiently large values of n n.

Recently, the authors of the paper [3] affirmed to have solved the second part of Hilbert’s 16th Problem by claiming that

(2) |  | H ⁡ ( n) = 2 ​ ( n − 1) ​ ( 4 ​ ( n − 1) − 2), H(n)=2(n-1)(4(n-1)-2), |  |

for n ≥ 2 n\geq 2 (see [3, Theorem 4]). They make use of the following scalar curvature associated to a Fisher information metric:

(3) |  | R = 1 G ​ [∂ ∂ x ​ ( 1 G ​ ∂ G 22 ∂ x) + ∂ ∂ y ​ ( 1 G ​ ∂ G 11 ∂ y)], R=\dfrac{1}{\sqrt{G}}\left[\dfrac{\partial}{\partial x}\left(\dfrac{1}{\sqrt{G}}\dfrac{\partial G_{22}}{\partial x}\right)+\dfrac{\partial}{\partial y}\left(\dfrac{1}{\sqrt{G}}\dfrac{\partial G_{11}}{\partial y}\right)\right], |  |

where

 | G 11 = 2 ​ [( ∂ P ∂ x) 2 + ( ∂ Q ∂ x) 2], G 22 = 2 ​ [( ∂ P ∂ y) 2 + ( ∂ Q ∂ y) 2], and ​ G = G 11 ​ G 22. G_{11}=2\left[\left(\dfrac{\partial P}{\partial x}\right)^{2}+\left(\dfrac{\partial Q}{\partial x}\right)^{2}\right],\,\,G_{22}=2\left[\left(\dfrac{\partial P}{\partial y}\right)^{2}+\left(\dfrac{\partial Q}{\partial y}\right)^{2}\right],\,\,\text{and}\,\,G=G_{11}G_{22}. |  |

Their approach relies on [3, Definition 1], which aims to provide an alternative definition for limit cycles, referred to as being “in the framework of GBT”. It begins by establishing that

1. ( A) (A)

a limit cycle is the periodic state of ( 1) in which R R is positive in the neighborhood of the equilibrium points of ( 1) and | R | |R| is singular.

By | R | |R| singular, they mean the existence of zeros of the denominator of | R | |R| that makes | R | |R| to diverge to infinity. Thus, it is also asserted that

1. ( B) (B)

if R R is positive in the neighborhood of the equilibrium points of ( 1) and the magnitude of R R diverges to infinity at symmetrical singularities with respect to the origin, then ( 1) possesses only one limit cycle. Nonetheless, if R R is positive in the neighborhood of the equilibrium points of ( 1) and the magnitude of R R diverges to infinity at different singularities, then ( 1) has more than one limit cycle such that the total number of distinctive divergences of | R | |R| to infinity provides the maximum number of limit cycles of ( 1).

Subsequent to Definition 1, it is stated that such a definition “agrees with the definition of limit cycles in the framework of classical bifurcation theory”, that is (non-stationary) periodic orbits isolated from other periodic orbits. In this way, the approach employed in [3] to obtain ( 2) consisted in counting the number of divergences of | R | |R| to infinity, as highlighted in the proof of [3, Theorem 4].

As previously mentioned, the function H ⁡ ( n) H(n) cannot be bounded from above by any quadratic polynomial in n n. Therefore, the relationship ( 2), which is quadratic in n n, cannot hold. To explore this issue further, we present counterexamples in the following sections. Section 2 discusses a well-known example from the literature that contradicts ( 2), along with references to other known examples that serves as counterexamples to ( 2). In Section 3, we provide examples of polynomial systems that exhibit limit cycles but do not satisfy ( A ) , and vice versa. This demonstrates that ( A ) is neither necessary nor sufficient for the existence of limit cycles of ( 1) and, therefore, is not equivalent to the standard definition of limit cycles. As a result, the definition of limit cycles proposed in [3] is not applicable to the study of the second part of Hilbert’s 16th problem, meaning that the number of singularities of | R | |R| does not determine the maximum number of limit cycles in ( 1), as suggested by assertion ( B ) .

## 2. Known counterexamples in the literature

The objective of this section is not to construct new counterexamples to the main conclusion ( 2) of [3], but rather to highlight known examples from the literature that serve as counterexamples for it.

In [5, Section 3], Li et al. revisited the class of polynomial differential systems originally studied by Christopher and Lloyd [2], addressing a minor issue in the original analysis. This correction did not affect the leading term n 2 ​ log ⁡ n n^{2}\log n of the lower estimation for the asymptotic growth of H ⁡ ( n) H(n). Their approach, as well as Christopher and Lloyd’s approach, consists of constructing a sequence of recursively defined polynomial differential systems ( P ​ H k) (PH_{k}) of degree 2 k − 1 2^{k}-1, each possessing at least S k S_{k} limit cycles, where

 | S k = 4 k − 1 ​ ( k − 13 6) + 2 k − 1 3. S_{k}=4^{k-1}\left(k-\dfrac{13}{6}\right)+2^{k}-\dfrac{1}{3}. |  |

This sequence implies that

(4) |  | H ⁡ ( 2 k − 1) ≥ S k = 4 k − 1 ​ ( k − 13 6) + 2 k − 1 3. H(2^{k}-1)\geq S_{k}=4^{k-1}\left(k-\dfrac{13}{6}\right)+2^{k}-\dfrac{1}{3}. |  |

However, the conclusion ( 2) from [3] provides that

 | H ⁡ ( 2 k − 1) = 4 ​ ( 2 k − 2) ​ ( 2 k + 1 − 5), H(2^{k}-1)=4(2^{k}-2)(2^{k+1}-5), |  |

which contradicts ( 4) for k ≥ 35 k\geq 35. This means that system P ​ H k PH_{k}, for k ≥ 35 k\geq 35, has more limit cycles than predicted by the main result of [3]. The other sequences of polynomial systems discussed in [5, Sections 4 and 5] also provide counterexamples to ( 2).

The works [4] and, more recently, [1] also provide similar lower estimations for the asymptotic growth of H ⁡ ( n) H(n). Both works present sequences of polynomial differential systems with specified degrees and numbers of limit cycles, differing in the mechanisms used to generate these limit cycles. Counterexamples to ( 2) can be derived from these sequences in a way analogous to the approach outlined above.

## 3. Possible issue for the proposed method

We begin by presenting three examples of polynomial differential systems where the existence of limit cycles is guaranteed, but assertion ( A ) does not hold. Specifically, in these examples, either R R is negative in a neighborhood of the unique equilibrium point, or R R is positive in a neighborhood of the unique equilibrium point, but | R | |R| is not singular. These examples demonstrate that limit cycles satisfying ( A ) do not encompass all possible limit cycles in polynomial systems. As a result, the maximum number of limit cycles satisfying ( A ) for a polynomial system of degree n n does not provide an upper bound for H ⁡ ( n) H(n). This likely explains why the main result ( 2) of [3] does not agree with the established lower estimations for the asymptotic growth of H ⁡ ( n) H(n), as discussed in the previous section.

###### Example 1.

We start by considering the following cubic vector field

(5) |  | { x ˙ = − y + x ⁡ ( x 2 + y 2 − 1), y ˙ = x + y ⁡ ( x 2 + y 2 − 1), \begin{cases}\displaystyle\dot{x}=-y+x(x^{2}+y^{2}-1),\\ \displaystyle\dot{y}=x+y(x^{2}+y^{2}-1),\end{cases} |  |

which has a single equilibrium point, located at the origin ( 0, 0) (0,0). This vector field also has a unique limit cycle surrounding the origin. To see that, it is enough to write system ( 5) in polar coordinates ( x, y) = ( r ​ cos ⁡ ( θ), r ​ sin ⁡ ( θ)) (x,y)=(r\cos(\theta),r\sin(\theta)) as follows:

 | { r ˙ = r ⁡ ( r 2 − 1), θ ˙ = 1. \begin{cases}\displaystyle\dot{r}=r(r^{2}-1),\\ \displaystyle\dot{\theta}=1.\end{cases} |  |

This implies that system ( 5) has a unique limit cycle which is unstable and whose orbit corresponds to the unit circle with center at the origin. Now, computing the function R R we get

 | R ⁡ ( x, y) = R 1 ​ ( x, y) R 2 ​ ( x, y), R(x,y)=\dfrac{R_{1}(x,y)}{R_{2}(x,y)}, |  |

where

 | R 1 ​ ( x, y) = \displaystyle R_{1}(x,y)= | 72 ​ x 10 − 216 ​ x 8 ​ y 2 − 204 ​ x 8 − 320 ​ x 7 ​ y − 3056 ​ x 6 ​ y 4 + 464 ​ x 6 ​ y 2 + 368 ​ x 6 + 192 ​ x 5 ​ y 3 + 192 ​ x 5 ​ y \displaystyle 72x^{10}-216x^{8}y^{2}-204x^{8}-320x^{7}y-3056x^{6}y^{4}+464x^{6}y^{2}+368x^{6}+192x^{5}y^{3}+192x^{5}y |  |

 |  | − 3056 ​ x 4 ​ y 6 + 2360 ​ x 4 ​ y 4 − 304 ​ x 4 ​ y 2 − 240 ​ x 4 − 192 ​ x 3 ​ y 5 − 216 ​ x 2 ​ y 8 + 464 ​ x 2 ​ y 6 − 304 ​ x 2 ​ y 4 − 96 ​ x 2 ​ y 2 \displaystyle-3056x^{4}y^{6}+2360x^{4}y^{4}-304x^{4}y^{2}-240x^{4}-192x^{3}y^{5}-216x^{2}y^{8}+464x^{2}y^{6}-304x^{2}y^{4}-96x^{2}y^{2} |  |

 |  | + 96 ​ x 2 + 320 ​ x ​ y 7 − 192 ​ x ​ y 5 + 72 ​ y 10 − 204 ​ y 8 + 368 ​ y 6 − 240 ​ y 4 + 96 ​ y 2 − 16 and \displaystyle+96x^{2}+320xy^{7}-192xy^{5}+72y^{10}-204y^{8}+368y^{6}-240y^{4}+96y^{2}-16\quad\text{and}\quad |  |

 | R 2 ​ ( x, y) = \displaystyle R_{2}(x,y)= | ( ( 3 ​ x 2 + y 2 − 1) 2 + ( 2 ​ x ​ y + 1) 2) 2 ​ ( ( x 2 + 3 ​ y 2 − 1) 2 + ( 2 ​ x ​ y − 1) 2) 2. \displaystyle\Big((3x^{2}+y^{2}-1)^{2}+(2xy+1)^{2}\Big)^{2}\Big((x^{2}+3y^{2}-1)^{2}+(2xy-1)^{2}\Big)^{2}. |  |

Observe that R 2 R_{2} does not vanish at the origin, implying that R R is continuous in its neighborhood. Additionally, since R ⁡ ( 0, 0) = − 1 < 0 R(0,0)=-1<0, continuity ensures that R ⁡ ( x, y) R(x,y) remains negative in a neighborhood of the origin, which corresponds to the unique equilibrium point of ( 5). Therefore, system ( 5) provides an example of a limit cycle that does not satisfy assertion ( A ) .

###### Example 2.

Using the approach from Example 1, we can easily construct polynomial systems with any number of limit cycles and a unique equilibrium point, where R R is negative in its neighborhood. For instance, the following polynomial system has a single equilibrium point at the origin and two nested limit cycles surrounding it:

(6) |  | { x ˙ = − y + x ⁡ ( x 2 + y 2 − 1) ​ ( x 2 + y 2 − 4), y ˙ = x + y ⁡ ( x 2 + y 2 − 1) ​ ( x 2 + y 2 − 4). \begin{cases}\displaystyle\dot{x}=-y+x(x^{2}+y^{2}-1)(x^{2}+y^{2}-4),\\ \displaystyle\dot{y}=x+y(x^{2}+y^{2}-1)(x^{2}+y^{2}-4).\end{cases} |  |

Indeed, by applying a polar change of variables, one can deduce that ( 6) has exactly two limit cycles: an asymptotically stable one, whose orbit corresponds to the unit circle centered at the origin; and an unstable one whose orbit corresponds to a circle of radius two, also centered at the origin. The expression for R R is cumbersome and thus omitted here, but following the same reasoning of Example 1, we conclude that R R is continuous in a neighborhood of the origin, with R ( 0, 0) = − 80 / 289 < 0 R(0,0)=-80/289<0, implying that R R remains negative near the origin. Therefore, system ( 6) provides examples of limit cycles that do not satisfy assertion ( A ) .

###### Example 3.

Now, consider the system ( 5) under the following linear change of variables: ( x, y) = ( u, u + v / 2) (x,y)=(u,u+v/2). This yields the transformed system:

(7) |  | { u ˙ = − 2 ​ u − v 2 + 2 ​ u 3 + u 2 ​ v + u ​ v 2 4, v ˙ = 4 ​ u + 2 ​ u 2 ​ v + u ​ v 2 + v 3 4. \begin{cases}\displaystyle\dot{u}=-2u-\frac{v}{2}+2u^{3}+u^{2}v+\frac{uv^{2}}{4},\\ \displaystyle\dot{v}=4u+2u^{2}v+uv^{2}+\frac{v^{3}}{4}.\end{cases} |  |

Of course, system ( 7) has a unique equilibrium point at the origin ( 0, 0) (0,0) and a unique limit cycle surrounding it. Computing the function R R for system ( 7), we obtain

 | R ⁡ ( u, v) = R 1 ​ ( u, v) R 2 ​ ( u, v), R(u,v)=\dfrac{R_{1}(u,v)}{R_{2}(u,v)}, |  |

where

 | R 1 ​ ( u, v) = \displaystyle R_{1}(u,v)= | 32 ​ ( − 663552 ​ u 10 − 8638464 ​ u 9 ​ v − 25353216 ​ u 8 ​ v 2 − 7421952 ​ u 8 − 37943808 ​ u 7 ​ v 3 − 18733056 ​ u 7 ​ v CLOSE \displaystyle 32\Big(-663552u^{10}-8638464u^{9}v-25353216u^{8}v^{2}-7421952u^{8}-37943808u^{7}v^{3}-18733056u^{7}v |  |

 |  | − 36060032 ​ u 6 ​ v 4 − 22151168 ​ u 6 ​ v 2 + 5670912 ​ u 6 − 23658048 ​ u 5 ​ v 5 − 18140416 ​ u 5 ​ v 3 + 10874880 ​ u 5 ​ v \displaystyle-36060032u^{6}v^{4}-22151168u^{6}v^{2}+5670912u^{6}-23658048u^{5}v^{5}-18140416u^{5}v^{3}+10874880u^{5}v |  |

 |  | − 10971920 ​ u 4 ​ v 6 − 11152128 ​ u 4 ​ v 4 + 7196416 ​ u 4 ​ v 2 − 2199552 ​ u 4 − 3555048 ​ u 3 ​ v 7 − 4852576 ​ u 3 ​ v 5 \displaystyle-10971920u^{4}v^{6}-11152128u^{4}v^{4}+7196416u^{4}v^{2}-2199552u^{4}-3555048u^{3}v^{7}-4852576u^{3}v^{5} |  |

 |  | + 2186496 ​ u 3 ​ v 3 − 4174848 ​ u 3 ​ v − 772632 ​ u 2 ​ v 8 − 1359232 ​ u 2 ​ v 6 + 296160 ​ u 2 ​ v 4 − 2595840 ​ u 2 ​ v 2 \displaystyle+2186496u^{3}v^{3}-4174848u^{3}v-772632u^{2}v^{8}-1359232u^{2}v^{6}+296160u^{2}v^{4}-2595840u^{2}v^{2} |  |

 |  | + 219136 ​ u 2 − 103056 ​ u ​ v 9 − 222052 ​ u ​ v 7 + 49248 ​ u ​ v 5 − 828032 ​ u ​ v 3 + 472064 ​ u ​ v − 6399 ​ v 10 − 18528 ​ v 8 \displaystyle+219136u^{2}-103056uv^{9}-222052uv^{7}+49248uv^{5}-828032uv^{3}+472064uv-6399v^{10}-18528v^{8} |  |

 |  | OPEN + 18596 ​ v 6 − 126272 ​ v 4 + 134912 ​ v 2 + 61440) and \displaystyle+18596v^{6}-126272v^{4}+134912v^{2}+61440\Big)\quad\text{and}\quad |  |

 | R 2 ​ ( u, v) = \displaystyle R_{2}(u,v)= | ( ( 24 ​ u 2 + 8 ​ u ​ v + v 2 − 8) 2 + 16 ​ ( 4 ​ u ​ v + v 2 + 4) 2) 2 ​ ( ( 8 ​ u 2 + 8 ​ u ​ v + 3 ​ v 2) 2 + 4 ​ ( 2 ​ u 2 + u ​ v − 1) 2) 2. \displaystyle\Big((24u^{2}+8uv+v^{2}-8)^{2}+16(4uv+v^{2}+4)^{2}\Big)^{2}\Big((8u^{2}+8uv+3v^{2})^{2}+4(2u^{2}+uv-1)^{2}\Big)^{2}. |  |

Again, R 2 R_{2} does not vanish at the origin, so R R is continuous in its neighborhood. Moreover, since R ⁡ ( 0, 0) = 6 / 5 > 0 R(0,0)=6/5>0, continuity ensures that R ⁡ ( u, v) R(u,v) is positive in a neighborhood of the origin, corresponding to the unique equilibrium point of ( 7). Additionally, since R 2 R_{2} is a product of sums of squares, it follows that R 2 ​ ( u, v) = 0 R_{2}(u,v)=0 if and only if ( u, v) (u,v) satisfies one of the following systems of algebraic equations:

 | S 1: { 24 ​ u 2 + 8 ​ u ​ v + v 2 − 8 = 0 4 ​ u ​ v + v 2 + 4 = 0 or S 2: { 8 ​ u 2 + 8 ​ u ​ v + 3 ​ v 2 = 0 2 ​ u 2 + u ​ v − 1 = 0. S_{1}:\begin{cases}24u^{2}+8uv+v^{2}-8=0\\ 4uv+v^{2}+4=0\end{cases}\quad\text{or}\quad S_{2}:\begin{cases}8u^{2}+8uv+3v^{2}=0\\ 2u^{2}+uv-1=0.\end{cases} |  |

We begin by analyzing S 1 S_{1}. First, note that if ( u, v) (u,v) is a solution of S 1 S_{1}, then v ≠ 0 v\neq 0. Solving the second equation of S 1 S_{1} for u u and substituting into the first equation yields the algebraic equation 17 ​ v 4 + 152 ​ v 2 + 384 = 0 17v^{4}+152v^{2}+384=0, which has no real solutions. Next, for system S 2 S_{2}, if ( u, v) (u,v) is a solution, then u ≠ 0 u\neq 0. Solving the second equation of S 2 S_{2} for v v and substituting into the first equation leads to the algebraic equation 3 − 4 ​ u 2 + 4 ​ u 4 = 0 3-4u^{2}+4u^{4}=0, which also has no real solutions. This shows that the denominator R 2 R_{2} of R R does not vanish, and hence | R | |R| has no singularities. Therefore, system ( 7) provides another example of a limit cycle that does not satisfy assertion ( A ) .

From the above examples, we observed that assertion ( A ) is not necessary for the existence of limit cycles, as there are polynomial systems with limit cycles where ( A ) does not hold. Nevertheless, we can still ask whether ( A ) is a sufficient condition for the existence of limit cycles. The following example provides a negative answer to this question.

###### Example 4.

Consider the following quadratic polynomial system:

(8) |  | { x ˙ = − y + x 2, y ˙ = x + x ​ y. \begin{cases}\displaystyle\dot{x}=-y+x^{2},\\ \displaystyle\dot{y}=x+xy.\end{cases} |  |

This system and its properties have been extensively studied in the literature, as it appears as a normal form for a class of isochronous quadratic systems, commonly referred to as S 2 S_{2} (see [6, 7]). This system has a unique equilibrium point at the origin, which is a center, meaning that there exists a neighborhood U U around the origin where all orbits in U ∖ { ( 0, 0) } U\setminus\{(0,0)\} are periodic. Clearly, no periodic orbit in U U is a limit cycle, as none are isolated from other periodic orbits. In fact, this system does not have any limit cycles. By computing the function R R for system ( 8), we obtain

 | R ⁡ ( x, y) = 1 ( x 2 + 1) 2 ​ ( 4 ​ x 2 + ( y + 1) 2). R(x,y)=\frac{1}{\left(x^{2}+1\right)^{2}\left(4x^{2}+(y+1)^{2}\right)}. |  |

Observe that R R is continuous in a neighborhood of the origin, as its denominator does not vanish at ( 0, 0) (0,0). Since R ⁡ ( 0, 0) = 1 R(0,0)=1, continuity ensures that R R remains positive in a neighborhood around the origin, which is the unique equilibrium point of ( 8). Furthermore, | R | |R| is singular at ( x, y) = ( 0, − 1) (x,y)=(0,-1). Thus, system ( 8) provides an example where assertion ( A ) holds for every periodic orbit within U U, despite the absence of limit cycles.

## 4. Conclusion

In this note, we have demonstrated that the recent attempt to solve the second part of Hilbert’s 16th problem, as presented in [3], contains significant issues. We began by exploring counterexamples which demonstrate that the quadratic expression proposed for H ⁡ ( n) H(n) contradicts the well-established asymptotic behavior of this function, which states that H ⁡ ( n) H(n) grows as fast as ( n + 2) 2 ​ log ⁡ ( n + 2) / ( 2 ​ log ⁡ 2) (n+2)^{2}\log(n+2)/(2\log 2). Moreover, we discussed how the alternative definition of limit cycles ( A ) , used in [3], is not applicable to the study of the second part of Hilbert’s 16th problem, as it is neither necessary nor sufficient for the existence of limit cycles in ( 1), according to the standard definition, which refers to (non-stationary) periodic orbits isolated from other periodic orbits.

## References

- [1] M. Álvarez, B. Coll, P. D. Maesschalck, and R. Prohens. Asymptotic lower bounds on Hilbert numbers using canard cycles. Journal of Differential Equations, 268(7):3370–3391, Mar. 2020.
- [2] C. J. Christopher and N. G. Lloyd. Polynomial systems: a lower bound for the Hilbert numbers. Proc. Roy. Soc. London Ser. A, 450(1938):219–224, 1995.
- [3] V. B. da Silva, J. P. Vieira, and E. D. Leonel. Exploring limit cycles of differential equations through information geometry unveils the solution to Hilbert’s 16th problem. Entropy, 26(9), 2024.
- [4] M. Han and J. Li. Lower bounds for the Hilbert number of polynomial systems. J. Differential Equations, 252(4):3278–3304, 2012.
- [5] J. Li, H. S. Y. Chan, and K. W. Chung. Some lower bounds for H ⁡ ( n) H(n) in Hilbert’s 16th problem. Qual. Theory Dyn. Syst., 3(2):345–360, 2002.
- [6] W. S. Loud. Behavior of the period of solutions of certain plane autonomous systems near centers. Contributions to Differential Equations, 3:21–36, 1964.
- [7] P. Mardešić, C. Rousseau, and B. Toni. Linearization of isochronous centers. J. Differential Equations, 121(1):67–108, 1995.
- [8] R. Roussarie. Bifurcation of planar vector fields and Hilbert’s sixteenth problem, volume 164 of Progress in Mathematics. Birkhäuser Verlag, Basel, 1998.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:claudio.buzzi@unesp.br
[4]: mailto:ddnovaes@unicamp.br
