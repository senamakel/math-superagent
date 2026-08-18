<!-- source: https://ar5iv.labs.arxiv.org/html/0903.5056 | converted from HTML -->

[0903.5056] Linear estimate for the number of zeros of Abelian integrals

# Linear estimate for the number of zeros of Abelian integrals

Sergey Malev Address: Faculty of Mathematics and Computer Science, The Weizmann Institute of Science POB 26, Rehovot 76100, ISRAEL Email address: [sergey.malev@weizmann.ac.il][1] and Dmitry Novikov Address: Faculty of Mathematics and Computer Science, The Weizmann Institute of Science POB 26, Rehovot 76100, ISRAEL Email address: [dmitry.novikov@weizmann.ac.il][2]

###### Abstract.

We prove a linear in deg ⁡ ω \deg\omega upper bound on the number of real zeros of the Abelian integral I ⁡ ( t) = ∫ δ ⁡ ( t) ω I(t)=\int_{\delta(t)}\omega, where δ ⁡ ( t) ⊂ ℝ 2 \delta(t)\subset{\mathbb{R}}^{2} is the real oval x 2 ​ y ​ ( 1 − x − y) = t x^{2}y(1-x-y)=t and ω \omega is a one-form with polynomial coefficients.

## 1. Introduction

For the polynomial H ⁡ ( x, y) = x 2 ​ y ​ ( 1 − x − y) H(x,y)=x^{2}y(1-x-y) consider the continuous family { δ ⁡ ( t), t ∈ ( 0, 1 64) } \{\delta(t),t\in\left(0,\frac{1}{64}\right)\} of compact connected components of the level curves { H = t } ⊂ ℝ 2 \{H=t\}\subset{\mathbb{R}}^{2}. Let ω = p ⁡ ( x, y) ​ d ​ x + q ⁡ ( x, y) ​ d ​ y ∈ Λ 1 ​ ( ℝ 2) \omega=p(x,y)dx+q(x,y)dy\in\Lambda^{1}({\mathbb{R}}^{2}) be a differential one-form with polynomial coefficients of degree n n. Define the complete Abelian integral:

(1) |  | I ⁡ ( t) = ∮ δ ⁡ ( t) ω, t ∈ ( 0, 1 64). I(t)=\oint_{\delta(t)}\omega,\ \ \ t\in\left(0,\frac{1}{64}\right). |  |

We provide an explicit answer to the Infinitesimal Hilbert 16th problem for this particular Abelian integral.

###### Theorem 1.1.

The number of isolated zeros of I ⁡ ( t) I(t) on ( 0, 1 64) (0,\frac{1}{64}) does not exceed 7 4 ​ n + 9 \frac{7}{4}n+9, where n = deg ⁡ ω n=\deg\omega.

It is well known that zeros of Abelian integrals correspond to limit cycles appearing in non-conservative perturbations of Hamiltonian, or, more general, integrable systems. Abelian integral ( 1) is related to perturbations of the integrable quadratic vector field which can be written in the Pfaffian form as follows:

(2) |  | 1 x ​ d ​ H − ε ​ ω = 0, H ⁡ ( x, y) = x 2 ​ y ​ ( 1 − x − y). \frac{1}{x}dH-{\varepsilon}\omega=0,\qquad H(x,y)=x^{2}y(1-x-y). |  |

Therefore Theorem 1.1 implies in a standard way the following claim:

###### Theorem 1.2.

The number of limit cycles appearing in non-conservative perturbation ( 2) and converging, as ϵ → 0 \epsilon\to 0, to a smooth cycle δ ⁡ ( t) \delta(t), does not exceed 1 4 ​ ( 7 ​ n + 43) \frac{1}{4}(7n+43).

Indeed, these limit cycles correspond to the isolated zeros of ∫ δ ⁡ ( t) x ​ ω \int_{\delta(t)}x\omega, so this upper bound follows from Theorem 1.1 by replacing n n by n + 1 n+1.

Our result should be considered in the general context of the Infinitesimal Hilbert 16th problem. So far, the only known general explicit result about the number of zeros of Abelian integrals is the recent result [1] providing double-exponential in max ⁡ ( deg ⁡ H, deg ⁡ ω) \max(\deg H,\deg\omega) upper bound for the number of zeros of Abelian integral. The result of Petrov-Khovanskii, see [10] for an exposition of the result, provides an upper bound which is a linear function of n = deg ⁡ ω n=\deg\omega, but provides no information about the coefficients of this function. It seems reasonable to expect that these two results can be combined together to provide an upper bound which would be linear in n n and double-exponential in deg ⁡ H \deg H. However, even this upper bound will by far exceed any known examples.

From the other side, for the cases of polynomials H H of low degree the situation seems to be better understood. More exact, for a generic polynomial H H of third degree Horozov and Iliev [6] were able to provide an explicit upper bound linear in n n which seems to be close to the best possible one. The key point was the ellipticity of the level curves of H H. This fact allowed to reduce the initial question to the question about number of zeros of polynomial combinations of solutions of some Riccati equation. This last question can be easily dealt with by essentially fewnomials technique (i.e. Rolle lemma). Later, the same approach was applied to the case of elliptic polynomial of fourth degree, see [5].

This result motivated consideration of integrable quadratic vector fields with center whose trajectories are elliptic curves. Gautier in [2] lists all these fields. Based on this list and results of [7], Gautier, Gavrilov and Iliev in [3] proposed a program of studying cyclicity of open nests of cycles defined by such foliations, and, in particular, conjectured that one can provide an effective upper bound for the number of zeros of corresponding Abelian integrals, similar to [6]. Our case is the case (rlv3) in notations of [3].

## 2. Decomposition in Petrov modules

Define the basic Abelian integrals as

(3) |  | I i, j ​ ( t) = 1 i + 1 ​ ∫ δ ⁡ ( t) x i + 1 ​ y j ​ 𝑑 y = ∬ Δ ⁡ ( t) x i ​ y j ​ 𝑑 x ∧ 𝑑 y, I_{i,j}(t)=\frac{1}{i+1}\int_{\delta(t)}x^{i+1}y^{j}dy=\iint_{\Delta(t)}x^{i}y^{j}dx\wedge dy, |  |

where Δ ⁡ ( t) \Delta(t) is the area bounded by the cycle δ ⁡ ( t) \delta(t). The integrals are well-defined for all (i.e. not only positive) i, j ∈ ℤ i,j\in{\mathbb{Z}} due to the following fact:

###### Remark 2.1.

The curve δ ⁡ ( t) \delta(t) lies in { x, y > 0 } \{x,y>0\}.

Our immediate goal is to construct explicit representation of the Abelian integrals defined in ( 1) as combinations with polynomial in t t coefficients of just three Abelain integrals J 1 ​ ( t) = I 0, 0 ​ ( t) J_{1}(t)=I_{0,0}(t), J 2 ​ ( t) = I 2, 0 ​ ( t) J_{2}(t)=I_{2,0}(t) and J 3 ​ ( t) = I 3, 0 ​ ( t) J_{3}(t)=I_{3,0}(t). In other words, we want to prove that Abelian integrals can be generated, as a ℂ ⁡ [t] {\mathbb{C}}[t] -module, by these 3 basic Abelian integrals.

Let H ⁡ ( x, y) = ∑ i, j ∈ ℤ 2 h i ​ j ​ x i ​ y j ∈ ℝ ⁡ [x, y] H(x,y)=\sum_{i,j\in{\mathbb{Z}}^{2}}h_{ij}x^{i}y^{j}\in{\mathbb{R}}[x,y] be a general Laurent polynomial in two variables and assume that the family δ ( t) ⊂ { H = t } \delta(t)\subset\{H=t\} of cycles lies in { x, y > 0 } \{x,y>0\}.

###### Lemma 2.2.

Abelian integrals I k, l ​ ( t) I_{k,l}(t) defined by ( 3) satisfy the following relations:

 | t ⁡ ( k + 1) ⋅ I k, l ​ ( t) \displaystyle t(k+1)\cdot I_{k,l}(t) | = ∑ i, j h i, j ​ ( k + i + 1) ⋅ I k + i, l + j ​ ( t), \displaystyle=\sum\limits_{i,j}h_{i,j}(k+i+1)\cdot I_{k+i,l+j}(t), |  |

(4) |  | t ⁡ ( l + 1) ⋅ I k, l ​ ( t) \displaystyle t(l+1)\cdot I_{k,l}(t) | = ∑ i, j h i, j ​ ( l + j + 1) ⋅ I k + i, l + j ​ ( t), \displaystyle=\sum\limits_{i,j}h_{i,j}(l+j+1)\cdot I_{k+i,l+j}(t), |  |

 | ( k + 1) ⋅ I k, l ​ ( t) \displaystyle(k+1)\cdot I_{k,l}(t) | = ∑ i, j i ​ h i, j ⋅ d d ​ t ​ I k + i, l + j ​ ( t), \displaystyle=\sum\limits_{i,j}ih_{i,j}\cdot\frac{d}{dt}I_{k+i,l+j}(t), |  |

 | ( l + 1) ⋅ I k, l ​ ( t) \displaystyle(l+1)\cdot I_{k,l}(t) | = ∑ i, j j ​ h i, j ⋅ d d ​ t ​ I k + i, l + j ​ ( t), \displaystyle=\sum\limits_{i,j}jh_{i,j}\cdot\frac{d}{dt}I_{k+i,l+j}(t), |  |

where i, j ∈ ℤ i,j\in{\mathbb{Z}}.

###### Proof.

Since H ⁡ ( x, y) = t H(x,y)=t on the cycle δ ⁡ ( t) ⊂ ℝ 2 \delta(t)\subset{\mathbb{R}}^{2} we have

 | t ⁡ ( k + 1) ⋅ I k, l ​ ( t) = ∫ δ ⁡ ( t) H ⁡ ( x, y) ​ x k + 1 ​ y l ​ 𝑑 y = ∑ i, j h i, j ​ ( k + i + 1) ​ I k + i, l + j ​ ( t), t(k+1)\cdot I_{k,l}(t)=\int\limits_{\delta(t)}H(x,y)x^{k+1}y^{l}dy=\sum_{i,j}h_{i,j}(k+i+1)I_{k+i,l+j}(t), |  |

which is the first equality of ( 4). The second identity is proved similarly.

By Gelfand-Leray formula we have

(5) |  | d d ​ t ​ ( ∬ γ ⁡ ( t) 𝑑 H ∧ x k + 1 ​ y l ​ 𝑑 y) = ∮ δ ⁡ ( t) x k + 1 ​ y l ​ 𝑑 y = ( k + 1) ​ I k, l ​ ( t). \frac{d}{dt}(\iint\limits_{\gamma(t)}dH\wedge x^{k+1}y^{l}dy)=\oint\limits_{\delta(t)}x^{k+1}y^{l}dy=(k+1)I_{k,l}(t). |  |

Replacing H H by ∑ ( i, j) ∈ ℤ 2 h i ​ j ​ x i ​ y j \sum\limits_{(i,j)\in{\mathbb{Z}}^{2}}h_{ij}x^{i}y^{j} we get the third identity. The fourth equality is proved similarly. ∎

For our particular choice H ⁡ ( x, y) = x 2 ​ y ​ ( 1 − x − y) H(x,y)=x^{2}y(1-x-y) we can rewrite the relations of Lemma 2.2 in more convenient form. We have

(6) |  | ( t ⁡ ( k + 1) − k − 3 k + 4 k + 3 t ⁡ ( l + 1) − l − 2 l + 2 l + 3) ⋅ ( I k, l I k + 2, l + 1 I k + 3, l + 1 I k + 2, l + 2) = ( 0 0). \left(\begin{array}[]{cccc}t(k+1)&-k-3&k+4&k+3\\ t(l+1)&-l-2&l+2&l+3\end{array}\right)\cdot\left(\begin{array}[]{c}I_{k,l}\\ I_{k+2,l+1}\\ I_{k+3,l+1}\\ I_{k+2,l+2}\end{array}\right)=\begin{pmatrix}0\\ 0\end{pmatrix}. |  |

Multiplying by ( l + 3 − k − 3 − l − 2 k + 4) \begin{pmatrix}l+3&-k-3\\ -l-2&k+4\end{pmatrix} from the left we get an equivalent for k + l ≠ − 6 k+l\neq-6 system of equations:

(7) |  | ( − 2 ​ t ​ ( l − k) − k − 3 k + l + 6 0 t ⁡ ( 3 ​ l − k + 2) − l − 2 0 k + l + 6) ⋅ ( I k, l I k + 2, l + 1 I k + 3, l + 1 I k + 2, l + 2) = ( 0 0). \left(\begin{array}[]{cccc}-2t(l-k)&-k-3&k+l+6&0\\ t(3l-k+2)&-l-2&0&k+l+6\end{array}\right)\cdot\left(\begin{array}[]{c}I_{k,l}\\ I_{k+2,l+1}\\ I_{k+3,l+1}\\ I_{k+2,l+2}\end{array}\right)=\begin{pmatrix}0\\ 0\end{pmatrix}. |  |

In other words, I k + 3, l + 1 ​ ( t) I_{k+3,l+1}(t) and I k + 2, l + 2 ​ ( t) I_{k+2,l+2}(t) can be represented as μ 1 k, l ​ ( t) ​ I k, l ​ ( t) + μ 2 k, l ​ ( t) ​ I k + 2, l + 1 ​ ( t) \mu^{k,l}_{1}(t)I_{k,l}(t)+\mu^{k,l}_{2}(t)I_{k+2,l+1}(t), where μ 1 k, l \mu^{k,l}_{1} is a polynomial of degree at most 1 1 and μ 2 k, l \mu^{k,l}_{2} is a constant. We have such representation for any pair ( k, l) (k,l) such that k + l ≠ − 6. k+l\neq-6.

Another corollary of ( 6):

(8) |  | ( − 2 ​ l + k − 1 3 ​ l − k + 2 2 ​ l − 2 ​ k) ⋅ ( I k + 2, l + 1 I k + 3, l + 1 I k + 2, l + 2) = 0. \left(\begin{array}[]{cccc}-2l+k-1&3l-k+2&2l-2k\end{array}\right)\cdot\left(\begin{array}[]{c}I_{k+2,l+1}\\ I_{k+3,l+1}\\ I_{k+2,l+2}\end{array}\right)=0. |  |

The equation ( 8) gives us linear dependence between I k + 2, l + 1, I k + 3, l + 1 I_{k+2,l+1},I_{k+3,l+1} and I k + 2, l + 2 I_{k+2,l+2} in all cases except k = l = − 1 k=l=-1. But in this case the equation ( 7) becomes:

(9) |  | ( 0 − 2 4 0 0 − 1 0 4) ⋅ ( I − 1, − 1 I 1, 0 I 2, 0 I 1, 1) = ( 0 0). \left(\begin{array}[]{cccc}0&-2&4&0\\ 0&-1&0&4\end{array}\right)\cdot\left(\begin{array}[]{c}I_{-1,-1}\\ I_{1,0}\\ I_{2,0}\\ I_{1,1}\end{array}\right)=\begin{pmatrix}0\\ 0\end{pmatrix}. |  |

Recall that J 1 ​ ( t) = I 0, 0 ​ ( t) J_{1}(t)=I_{0,0}(t), J 2 ​ ( t) = I 2, 0 ​ ( t) J_{2}(t)=I_{2,0}(t) and J 3 ​ ( t) = I 3, 0 ​ ( t) J_{3}(t)=I_{3,0}(t).

###### Lemma 2.3.

For any polynomial 1 1 -differential form ω \omega the Abelian integral I ⁡ ( t) = ∫ δ ⁡ ( t) ω I(t)=\int_{\delta(t)}\omega can be represented as p 1 ​ ( t) ​ J 1 ​ ( t) + p 2 ​ ( t) ​ J 2 ​ ( t) + p 3 ​ ( t) ​ J 3 ​ ( t) p_{1}(t)J_{1}(t)+p_{2}(t)J_{2}(t)+p_{3}(t)J_{3}(t) for some polynomials p i ​ ( t) p_{i}(t) of degree less than or equal to n 4 \frac{n}{4}, where n = deg ⁡ ω n=\deg\omega.

###### Remark 2.4.

The proof of this result below essentially provides the coefficients p i ​ ( t) p_{i}(t), i.e. provides an effective decomposition in the Petrov module corresponding to H H. This result does not formally follow from the result of Gavrilov [4] since x 2 ​ y ​ ( 1 − x − y) x^{2}y(1-x-y) is not a semi-weighted homogeneous polynomial. However, in this simple situation it can be obtained by a straightforward computation.

###### Proof.

First of all we will give such a representation for all I k, l ​ ( t) I_{k,l}(t) if k + l ≤ 3 k+l\leq 3, k, l ≥ 0 k,l\geq 0. By ( 9) we have I 1, 0 = 2 ​ J 2 I_{1,0}=2J_{2} and I 1, 1 = 1 2 ​ J 2 I_{1,1}=\frac{1}{2}J_{2}. Using ( 8) one can calculate the required representation for I 0, 1 I_{0,1} and I 2, 1 I_{2,1}. This implies similar representation for I 0, 2 I_{0,2} and I 1, 2 I_{1,2} and then for I 0, 3 I_{0,3}. Note that for these integrals the coefficients p i p_{i} are polynomials of degree 0 0, i.e. scalar.

For n = i + j ≥ 4 n=i+j\geq 4 the proof goes by induction on n n. Using ( 7), we see that the required representation of I k, n − k I_{k,n-k} for 2 ≤ k ≤ n − 1 2\leq k\leq n-1, together with bounds on the degrees of p i p_{i}, follows from the same for I k, l I_{k,l} with smaller k + l k+l. Using ( 8) one can obtain that I 1, n − 1 I_{1,n-1} is a linear combination of I 1, n − 2 I_{1,n-2} and I 2, n − 2 I_{2,n-2} (for k = − 1 k=-1 and l = n − 3 l=n-3) because 2 ​ l − 2 ​ k = 2 ​ n − 4 > 0 2l-2k=2n-4>0. Thus we obtain a required representation for I 1, n − 1 I_{1,n-1} and similarly for I 0, n I_{0,n}. Now we use ( 8) for k = n − 3 k=n-3 and l = − 1 l=-1 to obtain representation of I n, 0 I_{n,0} as a linear combination of I n − 1, 0 I_{n-1,0} and I n − 1, 1 I_{n-1,1}. One can easily check that the degrees of p i p_{i} are bounded by n / 4 n/4 in all these cases. ∎

## 3. Construction of the Picard-Fuchs system.

It is well known that the effective decomposition in Petrov modules allows to explicitly construct the Picard-Fuchs system for the generators of the Petrov module, see e.g. [9]. Here we follow this classical path.

###### Lemma 3.1.

The column J = ( J 1 ​ ( t) J 2 ​ ( t) J 3 ​ ( t)) J=\begin{pmatrix}J_{1}(t)\\ J_{2}(t)\\ J_{3}(t)\end{pmatrix} satisfies the system

(10) |  | J = d d ​ t ​ ( ( A + t ​ B) ​ J), J=\frac{d}{dt}((A+tB)J), |  |

where A = ( 0 − 1 12 1 12 0 − 1 56 1 56 0 − 5 504 5 504) A=\begin{pmatrix}0&-\frac{1}{12}&\frac{1}{12}\\ 0&-\frac{1}{56}&\frac{1}{56}\\ 0&-\frac{5}{504}&\frac{5}{504}\end{pmatrix} and B = ( 2 3 0 0 0 4 7 0 0 2 21 4 9). B=\begin{pmatrix}\frac{2}{3}&0&0\\ 0&\frac{4}{7}&0\\ 0&\frac{2}{21}&\frac{4}{9}\end{pmatrix}.

###### Proof.

of the lemma 3.1:

By Lemma 2.2 for any k k and l l (and in particular for l = 0 l=0 and k = 0, 1, 3 k=0,1,3) we have ( l + 1) ⋅ I k, l ​ ( t) = ∑ i, j j ​ h i, j ⋅ d d ​ t ​ I k + i, l + j ​ ( t). (l+1)\cdot I_{k,l}(t)=\sum_{i,j}jh_{i,j}\cdot\frac{d}{dt}I_{k+i,l+j}(t).

It implies

(11) |  | I k, 0 = d d ​ t ​ ( I k + 2, 1 − I k + 3, 1 − 2 ​ I k + 2, 2). I_{k,0}=\frac{d}{dt}(I_{k+2,1}-I_{k+3,1}-2I_{k+2,2}). |  |

Using Lemma 2.3 we represent I k, 1 I_{k,1} for 2 ≤ k ≤ 6 2\leq k\leq 6 and I k, 2 I_{k,2} for k = 2, 4 k=2,4 and 5 5 in terms of J i J_{i}. After calculation we obtain the result:

 | I 2, 1 \displaystyle I_{2,1} | = 1 2 ​ J 2 − 1 2 ​ J 3, \displaystyle=\frac{1}{2}J_{2}-\frac{1}{2}J_{3}, |  |

 | I 3, 1 \displaystyle I_{3,1} | = 1 4 ​ J 2 − 1 4 ​ J 3, \displaystyle=\frac{1}{4}J_{2}-\frac{1}{4}J_{3}, |  |

 | I 4, 1 \displaystyle I_{4,1} | = 1 7 ​ J 2 − 1 7 ​ J 3 − 4 7 ​ t ​ J 2, \displaystyle=\frac{1}{7}J_{2}-\frac{1}{7}J_{3}-\frac{4}{7}tJ_{2}, |  |

(12) |  | I 5, 1 \displaystyle I_{5,1} | = 5 56 ​ J 2 − 5 56 ​ J 3 − 6 7 ​ t ​ J 2, \displaystyle=\frac{5}{56}J_{2}-\frac{5}{56}J_{3}-\frac{6}{7}tJ_{2}, |  |

 | I 6, 1 \displaystyle I_{6,1} | = 5 84 ​ J 2 − 5 84 ​ J 3 − 4 7 ​ t ​ J 2 − 2 3 ​ t ​ J 3, \displaystyle=\frac{5}{84}J_{2}-\frac{5}{84}J_{3}-\frac{4}{7}tJ_{2}-\frac{2}{3}tJ_{3}, |  |

 | I 2, 2 \displaystyle I_{2,2} | = 1 6 ​ J 2 − 1 6 ​ J 3 − 1 3 ​ t ​ J 1, \displaystyle=\frac{1}{6}J_{2}-\frac{1}{6}J_{3}-\frac{1}{3}tJ_{1}, |  |

 | I 4, 2 \displaystyle I_{4,2} | = 1 28 ​ J 2 − 1 28 ​ J 3 − 1 7 ​ t ​ J 2, \displaystyle=\frac{1}{28}J_{2}-\frac{1}{28}J_{3}-\frac{1}{7}tJ_{2}, |  |

 | I 5, 2 \displaystyle I_{5,2} | = 5 252 ​ J 2 − 5 252 ​ J 3 − 4 21 ​ t ​ J 2 + 1 9 ​ t ​ J 3, \displaystyle=\frac{5}{252}J_{2}-\frac{5}{252}J_{3}-\frac{4}{21}tJ_{2}+\frac{1}{9}tJ_{3}, |  |

The formulas ( 11) and system ( 12) together immediately imply the system ( 10). ∎

The system ( 10) can be rewritten as

(13) |  | ( A + t ​ B) ⋅ J ′ = ( I 3 × 3 − B) ⋅ J, (A+tB)\cdot J^{\prime}=(I_{3\times 3}-B)\cdot J, |  |

where I 3 × 3 I_{3\times 3} is the 3 3 -dimensional identity operator.

This equation can be rewritten as

(14) |  | D ⁡ ( t) ⋅ J ′ ​ ( t) = Q ⁡ ( t) ⋅ J ⁡ ( t), D(t)\cdot J^{\prime}(t)=Q(t)\cdot J(t), |  |

where

 | Q ⁡ ( t) = ( − 1 2 + 32 ​ t 9 − 10 0 3 2 + 48 ​ t − 5 2 0 3 2 − 24 ​ t − 5 2 + 80 ​ t) ​ and ​ D ​ ( t) = 64 ​ t 2 − t. Q(t)=\begin{pmatrix}-\frac{1}{2}+32t&9&-10\\ 0&\frac{3}{2}+48t&-\frac{5}{2}\\ 0&\frac{3}{2}-24t&-\frac{5}{2}+80t\end{pmatrix}\ \text{and}\ D(t)=64t^{2}-t. |  |

Introducing new variables X = t − 1 2 ​ J 1, Y = J 2, Z = J 3 X=t^{-\frac{1}{2}}J_{1},\ Y=J_{2},\ Z=J_{3} we have

(15) |  | { D ⁡ ( t) ​ t ​ X ′ = 9 ​ Y − 10 ​ Z D ⁡ ( t) ​ Y ′ = ( 3 2 + 48 ​ t) ​ Y − 5 2 ​ Z D ⁡ ( t) ​ Z ′ = ( 3 2 − 24 ​ t) ​ Y + ( − 5 2 + 80 ​ t) ​ Z \begin{cases}D(t)\sqrt{t}X^{\prime}&=9Y-10Z\\ D(t)Y^{\prime}&=(\frac{3}{2}+48t)Y-\frac{5}{2}Z\\ D(t)Z^{\prime}&=(\frac{3}{2}-24t)Y+(-\frac{5}{2}+80t)Z\end{cases} |  |

## 4. Proof of Theorem 1.1

Take any Abelian integral I ⁡ ( t) I(t). By Lemma 2.3 I ⁡ ( t) = p 1 ​ ( t) ​ J 1 ​ ( t) + p 2 ​ ( t) ​ J 2 ​ ( t) + p 3 ​ ( t) ​ J 3 ​ ( t) I(t)=p_{1}(t)J_{1}(t)+p_{2}(t)J_{2}(t)+p_{3}(t)J_{3}(t) where deg ⁡ p i ≤ n 4 \deg p_{i}\leq\frac{n}{4}. Thus I ⁡ ( t) = t ​ p 1 ​ X + p 2 ​ Y + p 3 ​ Z. I(t)=\sqrt{t}p_{1}X+p_{2}Y+p_{3}Z.

Using ( 15), we obtain

(16) |  | ( I p 1 ​ t) ′ = 1 D ​ p 1 2 ​ t ​ t ⋅ ( p ~ 1 ​ Y + p ~ 2 ​ Z), \left(\frac{I}{p_{1}\sqrt{t}}\right)^{\prime}=\frac{1}{Dp_{1}^{2}t\sqrt{t}}\cdot(\tilde{p}_{1}Y+\tilde{p}_{2}Z), |  |

where p ~ i \tilde{p}_{i} are some polynomials of degree less than or equal to n 2 + 2 \frac{n}{2}+2.

Recall that Z = J 3 = I 0, 3 ​ ( t) = ∬ γ ⁡ ( t) y 3 ​ 𝑑 x ∧ 𝑑 y Z=J_{3}=I_{0,3}(t)=\iint\limits_{\gamma(t)}y^{3}dx\wedge dy, so Z Z is positive for t ∈ ( 0, 1 64) t\in(0,\frac{1}{64}) by Remark 2.1. Hence the function w = Y Z w=\frac{Y}{Z} is well-defined and by ( 15) satisfies the Riccati equation

(17) |  | D ​ w ′ = ( − 3 2 + 24 ​ t) ​ w 2 + ( 4 − 32 ​ t) ​ w − 5 2. Dw^{\prime}=\left(-\frac{3}{2}+24t\right)w^{2}+\left(4-32t\right)w-\frac{5}{2}. |  |

So for the function S ⁡ ( t) = p ~ 1 ​ w + p ~ 2 S(t)=\tilde{p}_{1}w+\tilde{p}_{2} we have

 | D ​ S ′ = ( − 3 2 + 24 ​ t) ​ p ~ 1 ​ w 2 + ( D ​ p ~ 1 ′ + ( 4 − 32 ​ t) ​ p ~ 1) ​ w + D ​ p ~ 2 ′ − 5 2 ​ p ~ 1. DS^{\prime}=\left(-\frac{3}{2}+24t\right)\tilde{p}_{1}w^{2}+(D\tilde{p}_{1}^{\prime}+(4-32t)\tilde{p}_{1})w+D\tilde{p}_{2}^{\prime}-\frac{5}{2}\tilde{p}_{1}. |  |

One can obtain

 | D ​ p ~ 1 ​ S ′ = ( − 3 2 + 24 ​ t) ​ ( S − p ~ 2) 2 + ( D ​ p ~ 1 ′ + ( 4 − 32 ​ t) ​ p ~ 1) ​ ( S − p ~ 2) + ( D ​ p ~ 2 ′ − 5 2 ​ p ~ 1) ​ p ~ 1. D\tilde{p}_{1}S^{\prime}=\left(-\frac{3}{2}+24t\right)(S-\tilde{p}_{2})^{2}+(D\tilde{p}_{1}^{\prime}+(4-32t)\tilde{p}_{1})(S-\tilde{p}_{2})+\left(D\tilde{p}_{2}^{\prime}-\frac{5}{2}\tilde{p}_{1}\right)\tilde{p}_{1}. |  |

Thus the Riccati equation for the function S ⁡ ( t) S(t) reads as

(18) |  | D ​ p ~ 1 ​ S ′ = A ​ S 2 + B ​ S + C, D\tilde{p}_{1}S^{\prime}=AS^{2}+BS+C, |  |

where A, B A,B and C C are polynomials and deg ⁡ C ≤ n + 5. \deg C\leq n+5. Now one can introduce new time τ \tau and rewrite ( 18) as a system

(19) |  | { t ˙ = D ​ p ~ 1 S ˙ = A ​ S 2 + B ​ S + C, \begin{cases}\dot{t}&=D\tilde{p}_{1}\\ \dot{S}&=AS^{2}+BS+C,\end{cases} |  |

where φ ˙ \dot{\varphi} denotes d ​ φ d ​ τ. \frac{d\varphi}{d\tau}. Denote by Δ j, \Delta_{j}, j = 1, …, k ⁡ ( k ≤ deg ⁡ p ~ 1 + 1) j=1,\dots,k\ (k\leq\deg\tilde{p}_{1}+1) the open intervals into which ( 0, 1 64) (0,\frac{1}{64}) is split by the zeros of p ~ 1 \tilde{p}_{1}. It is clear that in Δ j \Delta_{j} between any two zeros of S S there is a zero of C C. Let λ j \lambda_{j} be the number of zeros of C C on Δ j \Delta_{j}. Thus the number of zeros of S S in Δ j \Delta_{j} is less than or equal to λ j + 1 \lambda_{j}+1. So the number of zeros of S S in ( 0, 1 64) (0,\frac{1}{64}) is less than or equal to ∑ j = 1 k ( λ j + 1) ≤ deg ⁡ C + deg ⁡ p ~ 1 + 1. \sum\limits_{j=1}^{k}(\lambda_{j}+1)\leq\deg C+\deg\tilde{p}_{1}+1. Thus it does not exceed n + 5 + n 2 + 2 + 1 = 3 2 ​ n + 8. n+5+\frac{n}{2}+2+1=\frac{3}{2}n+8. By ( 16) we obtain that on ( 0, 1 64) (0,\frac{1}{64}) the number of zeros of ( I p 1 ​ t) ′ \left(\frac{I}{p_{1}\sqrt{t}}\right)^{\prime} does not exceed 3 2 ​ n + 8. \frac{3}{2}n+8.

Denote by Ξ j, \Xi_{j}, j = 1, …, l ⁡ ( l ≤ deg ⁡ p 1 + 1) j=1,\dots,l\ (l\leq\deg p_{1}+1) the open intervals into which ( 0, 1 64) (0,\frac{1}{64}) is split by the zeros of p 1 p_{1}. It is clear that in Ξ j \Xi_{j} between any two zeros of I I (i.e. zeros of I p 1 ​ t \frac{I}{p_{1}\sqrt{t}}) there is a zero of ( I p 1 ​ t) ′ \left(\frac{I}{p_{1}\sqrt{t}}\right)^{\prime}. Let l j l_{j} be the number of zeros of ( I p 1 ​ t) ′ \left(\frac{I}{p_{1}\sqrt{t}}\right)^{\prime} on Ξ j \Xi_{j}. Thus the number of zeros of I I in Ξ j \Xi_{j} is less than or equal to l j + 1 l_{j}+1. So the number of zeros of I I in ( 0, 1 64) (0,\frac{1}{64}) is less than or equal to ∑ j = 1 l ( l j + 1) \sum\limits_{j=1}^{l}(l_{j}+1) and ∑ j = 1 l l j ≤ 3 2 ​ n + 8. \sum\limits_{j=1}^{l}l_{j}\leq\frac{3}{2}n+8. Thus the number of zeros of I I in ( 0, 1 64) (0,\frac{1}{64}) is less than or equal to 3 2 ​ n + 8 + l ≤ 3 2 ​ n + 8 + n 4 + 1 = 7 4 ​ n + 9. \frac{3}{2}n+8+l\leq\frac{3}{2}n+8+\frac{n}{4}+1=\frac{7}{4}n+9. This proves Theorem 1.1.

## References

- [1] G. Binyamini, D. Novikov, S. Yakovenko, On the number of zeros of Abelian integrals (2008).
- [2] S. Gautier, *Quadratic centers defining elliptic surfaces*, J. of Diff. Eq., 245 (2008), no 12, p. 3545-3569.
- [3] S. Gautier, L. Gavrilov, ID. Iliev, Perturbations of quadratic centers of genus one (2007).
- [4] L. Gavrilov, Petrov modules and zeros of Abelian integrals, Bull. Sci. Math. 122 (1998), no. 8, 571–584.
- [5] F. Girard, M.-A. Jebrane, Majorations affines du nombre de zeros d’integrales abeliennes pour les hamiltoniens quartiques elliptiques, Annales de la faculte des sciences de Toulouse, Ser. 6, 7 no. 4 (1998), p. 671-685.
- [6] E. Horozov, I. D. Iliev, Linear estimate for the numbers of zeros of Abelian integrals with cubic Hamiltonians (1998).
- [7] I. D. Iliev, *Perturbations of quadratic centers,*Bull. Sci. Math. 122 (1998), no. 2, 107161.
- [8] Yu. Ilyashenko, Centenial History of Hilbert’s 16th problem Bull. Amer. Math. Soc. (N.S.) 39 (2002), no. 3, 301–354 (electronic).
- [9] S. Yakovenko Bounded decomposition in the Brieskorn lattice and Pfaffian Picard–Fuchs systems for Abelian integrals, Bull. Sci. Math 126 (2002), no. 7, 535–554.
- [10] H. Żola̧dek, The monodromy group, Instytut Matematyczny Polskiej Akademii Nauk. Monografie Matematyczne (New Series) [Mathematics Institute of the Polish Academy of Sciences. Mathematical Monographs (New Series)], vol. 67, Birkhäuser Verlag, Basel, 2006.

[◄][3][image: ar5iv homepage] [4]
[Feeling lucky?][5] [6]
[Conversion report][7]
[Report an issue][8]
[View original on arXiv][9] [►][10]


## Links

[1]: mailto:sergey.malev@weizmann.ac.il
[2]: mailto:dmitry.novikov@weizmann.ac.il
[3]: /html/0903.5055
[4]: /
[5]: /feeling_lucky
[6]: /land_of_honey_and_milk
[7]: /log/0903.5056
[8]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+0903.5056
[9]: https://arxiv.org/pdf/0903.5056
[10]: /html/0903.5057
