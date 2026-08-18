<!-- source: https://arxiv.org/html/2512.19046v1 | converted from HTML -->

The cyclicity of period annulus of cubic isochronous Hamiltonian systems

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2512.19046v1 [math.DS] 22 Dec 2025

# The cyclicity of period annulus of cubic isochronous Hamiltonian systems

Jihua Yang Thanks: E-mail addresses: jihua1113@163.com, yangjh@mail.bnu.edu.cn. Affiliation: School of Mathematical Sciences, Tianjin Normal University, Tianjin 300387, P. R. China

Abstract Cima, Mañosas and Villadelprat (J. Differ. Equations, 157, 373–413, 1999) proved that a cubic Hamiltonian system possesses an isochronous center at the origin if and only if its Hamiltonian function can be expressed as

 | H 1 ​ ( x, y) = k 1 2 ​ x 2 + ( k 2 ​ y + k 3 ​ x + k 4 ​ x 2) 2, \displaystyle H_{1}(x,y)=k_{1}^{2}x^{2}+(k_{2}y+k_{3}x+k_{4}x^{2})^{2}, |  |

where k 1, k 2, k 3, k 4 ∈ ℝ k_{1},k_{2},k_{3},k_{4}\in\mathbb{R}, k 1 ​ k 2 ≠ 0 k_{1}k_{2}\neq 0. This paper is devoted to investigating the weak Hilbert’s 16th problem for the dynamical system associated with the above Hamiltonian function. We show that the maximum number of limit cycles is n − 1 n-1. Furthermore, this number is reached. That is, we solve the weak Hilbert’s 16th problem restricted to cubic Hamiltonian systems with an isochronous center at the origin.

Keywords weak Hilbert’s 16th problem; isochronous Hamiltonian system; recurrence formula; limit cycle; Abelian integral

2020 Mathematics Subject Classification 34C07; 34C05

## 1 Introduction and main result

For a planar autonomous differential system

 | d ​ x d ​ t = F n ​ ( x, y), d ​ y d ​ t = G n ​ ( x, y), \displaystyle\frac{dx}{dt}=F_{n}(x,y),\ \frac{dy}{dt}=G_{n}(x,y), |  | (1.1) |

where F n ​ ( x, y) F_{n}(x,y) and G n ​ ( x, y) G_{n}(x,y) are real polynomials of degree n n. Let Γ \Gamma be a closed orbit of system (1.1). If there exists a neighborhood of Γ \Gamma containing no other closed orbits of (1.1), then Γ \Gamma is called a limit cycle of (1.1). Geometrically, such a limit cycle is an isolated closed orbit with the distinctive property that all neighboring trajectories asymptotically approach it (either as t → + ∞ t\rightarrow+\infty or t → − ∞ t\rightarrow-\infty) in a spiraling manner, hence the terminology “limit cycle”. The bifurcation theory of limit cycles in differential systems not only arises naturally in mathematical modeling of biological systems [29, 40, 8], physics [6, 17], economics [37], mechanics [5], astronomy [11], electronics [2], but is also fundamentally connected to Hilbert’s 16th problem and its weak version [1, 20].

At the Second International Congress of Mathematicians held in Paris in 1900, the renowned mathematician D. Hilbert, with his vast knowledge and profound vision, proposed 23 mathematical problems (published in 1902 [20]), among which the second part of the 16th problem asks: what is the least upper bound on the number of limit cycles in system (1.1), and what are their possible relative configurations? In recent decades, mathematicians have conducted extensive research on this problem, yet substantial progress remains limited [25, 31, 18, 33, 19]. In 1977, Arnold [1] first proposed the weak Hilbert’s 16th problem concerning the near-Hamiltonian system:

 | { d ​ x d ​ t = ∂ H ⁡ ( x, y) ∂ y + ε ​ f ​ ( x, y), d ​ y d ​ t = − ∂ H ⁡ ( x, y) ∂ x + ε ​ g ​ ( x, y), \begin{cases}\dfrac{dx}{dt}=\dfrac{\partial H(x,y)}{\partial y}+\varepsilon f(x,y),\\[10.0pt] \dfrac{dy}{dt}=-\dfrac{\partial H(x,y)}{\partial x}+\varepsilon g(x,y),\end{cases} |  | (1.2) |

where 0 < | ε | ≪ 1 0<|\varepsilon|\ll 1, H ⁡ ( x, y) H(x,y) is a polynomial of degree m + 1 m+1, and f ⁡ ( x, y) f(x,y) and g ⁡ ( x, y) g(x,y) are polynomials of degree n n. Assume the unperturbed system ( 1.2) ε = 0 (1.2)_{\varepsilon=0} possesses a family of closed orbits { Γ h } \{\Gamma_{h}\}, and let Σ \Sigma denote the maximal open interval of h h where they exist, i.e.,

 | Γ h = { ( x, y) ∣ H ( x, y) = h, h ∈ Σ }. \Gamma_{h}=\{(x,y)\mid H(x,y)=h,h\in\Sigma\}. |  |

Given that Γ h \Gamma_{h} varies monotonically with h h, we consider the Abelian integral:

 | I ⁡ ( h) = ∮ Γ h g ⁡ ( x, y) ​ 𝑑 x − f ⁡ ( x, y) ​ 𝑑 y. I(h)=\oint_{\Gamma_{h}}g(x,y)dx-f(x,y)dy. |  | (1.3) |

The fundamental question is: what is the maximum number of isolated zeros (counting multiplicities) of the Abelian integral I ⁡ ( h) I(h)? Numerous excellent works have addressed the weak Hilbert’s 16th problem; see, for example, [3, 16, 23, 30, 26, 24, 27, 39] and the references therein.

It is well known that the number of limit cycles for a perturbation of a Hamiltonian system is closely related to the number of isolated zeros of the corresponding Abelian integral [16, 26, 36]. More specifically, the total number of zeros of the Abelian integral I ⁡ ( h) I(h), counted with multiplicities, provides an upper bound for the number of limit cycles of system (1.2) bifurcating from the corresponding open period annulus ⋃ h ∈ Σ Γ h \bigcup\limits_{h\in\Sigma}\Gamma_{h} [16]. The same is true for the closed period annulus, provided that it is bounded by a homoclinic loop as proved by Roussarie [38]. Moreover, a lower bound for the number of limit cycles is given by the number of multiple simple zeros of I ⁡ ( h) I(h).

When m = n = 2 m=n=2, the weak Hilbert’s 16th problem has been completely resolved. This outcome constitutes one of the exceedingly few complete solutions in this research domain, accomplished through more than a decade of sustained scholarly efforts, see [16, 22, 30, 35, 45]. However, for the case m = n = 3 m=n=3, only partial results have been obtained so far. Li, Liu and Yang [28] proved that there exist polynomials f ⁡ ( x, y) f(x,y) and g ⁡ ( x, y) g(x,y) of degree 3 such that system (1.2) has 13 limit cycles. Liu and Li [32], as well as Yang, Han, Li and Yu [44], have also established examples demonstrating the existence of 13 limit cycles in cubic differential systems. For the elliptic Hamiltonian of degree 4 as follows:

 | H ⁡ ( x, y) = 1 2 ​ y 2 + a 4 ​ x 4 + b 3 ​ x 3 + c 2 ​ x 2, a, b, c ∈ ℝ, a ≠ 0, \displaystyle H(x,y)=\frac{1}{2}y^{2}+\frac{a}{4}x^{4}+\frac{b}{3}x^{3}+\frac{c}{2}x^{2},\ a,b,c\in\mathbb{R},a\neq 0, |  |

there are five types of continuous families of ovals on the level curves of H ⁡ ( x, y) H(x,y), depending on the values of the parameters ( a, b, c) (a,b,c), called the truncated pendulum, the saddle loop, the global center, the cuspidal loop and the figure-eight loop, respectively. When the perturbation is Liénard type: ( α + β ​ x + γ ​ x 2) ​ y ​ d ​ x (\alpha+\beta x+\gamma x^{2})ydx, there is a series of papers dealing with the exact number of zeros of the Abelian integrals over five types of ovals. Horozov [21] considered the truncated pendulum, while the seminal work of Dumortier and Li [12, 13, 14, 15] addressed fundamental scenarios such as the saddle loop, global center, cuspidal loop, and figure-eight loop, which represent classical results in this domain. Regarding perturbations with n n -th degree polynomials, Zhao and Zhang [46] proved that the upper bound is 7 ​ n + 5 7n+5. Liu [34] studied the total number of zeros for the ovals in the two annuli surrounded by the figure-eight loop, and improves the upper bound given in [46]. When the Hamiltonian function H ⁡ ( x, y) H(x,y) contains x i ​ y j x^{i}y^{j}, where i i and j j are positive integers, Zhou and Li [47] obtained the algebraic structure of the Abelian integral for the Hamiltonian

 | H ⁡ ( x, y) = x 2 + y 2 + a ​ x 4 + b ​ x 2 ​ y 2 + c ​ y 4, a, b, c ∈ ℝ, H(x,y)=x^{2}+y^{2}+ax^{4}+bx^{2}y^{2}+cy^{4},\ a,b,c\in\mathbb{R}, |  |

and an upper bound of the number of zeros of Abelian integral I ⁡ ( h) I(h) was given for a special case a > 0, b = 0 a>0,b=0 and c = 1 c=1. Later, Chen and Yu [7] obtained an upper bound for a, b, c ∈ ℝ a,b,c\in\mathbb{R}. Wu, Zhang and Li [41] obtained an upper bound for the case

 | H ⁡ ( x, y) = x 2 + y 2 + c ​ x 2 ​ y 2 − x 4 + y 4, c > − 2. H(x,y)=x^{2}+y^{2}+cx^{2}y^{2}-x^{4}+y^{4},\ c>-2. |  |

Yang and Zhao [43] gave an upper bound (except the butterfly phase portrait) for the case

 | H ⁡ ( x, y) = − x 2 + a ​ x 4 + b ​ x 2 ​ y 2 + c ​ y 4, a, b, c ∈ ℝ, c ≠ 0. H(x,y)=-x^{2}+ax^{4}+bx^{2}y^{2}+cy^{4},\ a,b,c\in\mathbb{R},c\neq 0. |  |

Later, Yang, Sui and Zhao [42] got an upper bound of the above system with the butterfly phase portrait. Chang, Zhao and Wang [4] derived an upper bound for the case

 | H ⁡ ( x, y) = α ​ x 2 + β ​ y 2 + a ​ x 4 + b ​ x 2 ​ y 2 + c ​ y 4, α, β, a, b, c ∈ ℝ, α ​ β < 0. H(x,y)=\alpha x^{2}+\beta y^{2}+ax^{4}+bx^{2}y^{2}+cy^{4},\ \alpha,\beta,a,b,c\in\mathbb{R},\alpha\beta<0. |  |

It is worth noting that the systems studied in the aforementioned literature are all symmetric with respect to the x x -axis or y y -axis, which reduces the number of generators for the Abelian integrals. Inspired by these works, this paper focuses on the limit cycle bifurcations in a class of cubic Hamiltonian systems that lack symmetry about the coordinate axes. In 1999, Cima, Mañosas and Villadelprat [9] determined all the cubic Hamiltonian systems that have an isochronus center at the origin. They proved the following conclusion:

Theorem 1.1 [9] A cubic Hamiltonian system has an isochronous center at the origin if and only if after a linear change of coordinates its Hamiltonian function can be written as

 | H 1 ​ ( x, y) = k 1 2 ​ x 2 + ( k 2 ​ y + k 3 ​ x + k 4 ​ x 2) 2, \displaystyle H_{1}(x,y)=k_{1}^{2}x^{2}+(k_{2}y+k_{3}x+k_{4}x^{2})^{2}, |  | (1.4) |

where k i ∈ ℝ k_{i}\in\mathds{R} for i = 1, 2, 3, 4 i=1,2,3,4 and k 1 k_{1} and k 2 k_{2} are different from zero.

In the present paper, we study the weak Hilbert’s 16th problem for the dynamical system associated with Hamiltonian function (1.4). The Hamiltonian system corresponding to (1.4) is

 | { d ​ x d ​ t = − 2 ​ k 2 ​ ( k 2 ​ y + k 3 ​ x + k 4 ​ x 2), d ​ y d ​ t = 2 ​ k 1 2 ​ x + 2 ​ ( k 3 + 2 ​ k 4 ​ x) ​ ( k 2 ​ y + k 3 ​ x + k 4 ​ x 2), \displaystyle\begin{cases}\frac{dx}{dt}=-2k_{2}(k_{2}y+k_{3}x+k_{4}x^{2}),\\ \frac{dy}{dt}=2k_{1}^{2}x+2(k_{3}+2k_{4}x)(k_{2}y+k_{3}x+k_{4}x^{2}),\end{cases} |  | (1.5) |

Letting t 1 = 2 ​ k 2 ​ k 3 ​ t t_{1}=2k_{2}k_{3}t, x 1 = k 4 k 3 ​ x x_{1}=\frac{k_{4}}{k_{3}}x and y 1 = k 2 ​ k 4 k 1 2 + k 3 2 ​ y y_{1}=\frac{k_{2}k_{4}}{k_{1}^{2}+k_{3}^{2}}y ( k i ≠ 0, i = 1, 2, 3, 4) (k_{i}\neq 0,i=1,2,3,4), one can change system (1.5) into

 | { d ​ x d ​ t = − λ − 1 ​ y − x − x 2, d ​ y d ​ t = x + y + 2 ​ x ​ y + 3 ​ λ ​ x 2 + 2 ​ λ ​ x 3, \displaystyle\begin{cases}\frac{dx}{dt}=-\lambda^{-1}y-x-x^{2},\\ \frac{dy}{dt}=x+y+2xy+3\lambda x^{2}+2\lambda x^{3},\end{cases} |  | (1.6) |

with the Hamiltonian function

 | H ⁡ ( x, y) = 1 2 ​ x 2 + λ ​ x 3 + 1 2 ​ λ ​ x 4 + 1 2 ​ λ − 1 ​ y 2 + x ​ y + x 2 ​ y, \displaystyle H(x,y)=\frac{1}{2}x^{2}+\lambda x^{3}+\frac{1}{2}\lambda x^{4}+\frac{1}{2}\lambda^{-1}y^{2}+xy+x^{2}y, |  | (1.7) |

where λ = k 3 2 k 1 2 + k 3 2 \lambda=\frac{k_{3}^{2}}{k_{1}^{2}+k_{3}^{2}}. Clearly, 0 < λ < 1 0<\lambda<1. Here and below, we shall omit the subscript 1. System (1.6) has an isochronous center at the origin and a family of periodic orbits, denoted by

 | Γ h = { ( x, y): H ( x, y) = h, h ∈ ( 0, + ∞) }. \Gamma_{h}=\{(x,y):H(x,y)=h,h\in(0,+\infty)\}. |  |

The parabola y = − λ ​ x 2 − λ ​ x y=-\lambda x^{2}-\lambda x divides Γ h \Gamma_{h} into an upper arc and a lower arc, with their respective function expressions given by

 | y = − λ ​ x 2 − λ ​ x + ( λ 2 − λ) ​ x 2 + 2 ​ λ ​ h y=-\lambda x^{2}-\lambda x+\sqrt{(\lambda^{2}-\lambda)x^{2}+2\lambda h} |  |

and

 | y = − λ ​ x 2 − λ ​ x − ( λ 2 − λ) ​ x 2 + 2 ​ λ ​ h. y=-\lambda x^{2}-\lambda x-\sqrt{(\lambda^{2}-\lambda)x^{2}+2\lambda h}. |  |

The coordinates of the two intersection points between the parabola (the red curve in Fig. 1) and Γ h \Gamma_{h} (the blue closed curves in Fig. 1) are as follows:

 | ( 2 ​ h 1 − λ, − λ ​ 2 ​ h 1 − λ − 2 ​ λ ​ h 1 − λ), ( − 2 ​ h 1 − λ, λ ​ 2 ​ h 1 − λ − 2 ​ λ ​ h 1 − λ). \Big(\sqrt{\frac{2h}{1-\lambda}},-\lambda\sqrt{\frac{2h}{1-\lambda}}-\frac{2\lambda h}{1-\lambda}\Big),\ \Big(-\sqrt{\frac{2h}{1-\lambda}},\lambda\sqrt{\frac{2h}{1-\lambda}}-\frac{2\lambda h}{1-\lambda}\Big). |  |

Our main result is the following theorem.

Theorem 1.2 Consider the following perturbation of system (1.6):

 | { d ​ x d ​ t = − λ − 1 ​ y − x − x 2 + ε ​ ∑ i + j = 0 n a i, j ​ x i ​ y j, d ​ y d ​ t = x + y + 2 ​ x ​ y + 3 ​ λ ​ x 2 + 2 ​ λ ​ x 3 + ε ​ ∑ i + j = 0 n b i, j ​ x i ​ y j, \displaystyle\begin{cases}\frac{dx}{dt}=-\lambda^{-1}y-x-x^{2}+\varepsilon\sum\limits_{i+j=0}^{n}a_{i,j}x^{i}y^{j},\\ \frac{dy}{dt}=x+y+2xy+3\lambda x^{2}+2\lambda x^{3}+\varepsilon\sum\limits_{i+j=0}^{n}b_{i,j}x^{i}y^{j},\\ \end{cases} |  | (1.8) |

where 0 < | ε | ≪ 1. 0<|\varepsilon|\ll 1. Then, by using the Abelian integral, the upper bound for the number of limit cycles of system (1.8) bifurcating from the period annulus is n − 1 n-1 for n ≥ 2 n\geq 2, counted with multiplicities. Moreover, this bound is sharp.

Remark 1.1 (i) One major challenge in this paper lies in analyzing the algebraic structure of the Abelian integral I ⁡ ( h) I(h). As demonstrated, the number of generators of I ⁡ ( h) I(h) depends on the degree n n of the perturbation polynomials, which constitutes the key distinction from existing literature. To address this difficulty, we classify the terms I i, j ​ ( h) I_{i,j}(h) appearing in I ⁡ ( h) I(h) into two categories:

(a) formula-iterable terms admitting recursive computation: I i, j ​ ( h), i ≥ 2, j ≥ 1 I_{i,j}(h),i\geq 2,j\geq 1;

(b) non-iterable terms requiring alternative treatment: I i, j ​ ( h), i = 0, 1, j ≥ 1 I_{i,j}(h),i=0,1,j\geq 1.

For the non-iterable terms I i, j ​ ( h) I_{i,j}(h), we first derive the differential equations they satisfy and then obtain their explicit expressions by solving these differential equations.

(ii) After obtaining the explicit expression of I ⁡ ( h) I(h), verifying the linear independence of its coefficients becomes essential for determining the lower bound of the number of limit cycles. This constitutes another fundamental challenge in our work, which we successfully overcome through an innovative application of mathematical induction.

(iii) As shown in Fig. 1, the phase portrait of system (1.6) exhibits no symmetry whatsoever–neither about the coordinate axes nor about the origin. This inherent asymmetry inevitably leads to a larger number of generators for the corresponding Abelian integral I ⁡ ( h) I(h) than classical methodologies can accommodate, rather than a restriction to a small finite set (e.g., two or three generators).

The paper is organized as follows. The detailed expression of the Abelian integral I ⁡ ( h) I(h) is obtained in Section 2. The proof of the Theorem 1.1 and some numerical simulations are presented in Section 3. The discussion is then presented in the final section.

## 2 The algebraic structure of Abelian integral

For abbreviation we denote

 | I i, j ( h) = ∮ Γ h x i y j d x, h ∈ ( 0, + ∞), i, j ∈ ℕ. I_{i,j}(h)=\oint_{\Gamma_{h}}x^{i}y^{j}dx,\ h\in(0,+\infty),\ i,j\in\mathds{N}. |  |

It is straightforward to check that I n, 0 ​ ( h) = 0 I_{n,0}(h)=0. Direct computation by applying Green’s formula yields

 | I ⁡ ( h) = ∑ i + j = 0 n b i, j ​ ∮ Γ h x i ​ y j ​ 𝑑 x − ∑ i + j = 0 n a i, j ​ ∮ Γ h x i ​ y j ​ 𝑑 y = ∑ i + j = 1, j ≥ 1 n ξ i, j ​ I i, j ​ ( h), \displaystyle\begin{aligned} I(h)=&\sum\limits_{i+j=0}^{n}b_{i,j}\oint_{\Gamma_{h}}x^{i}y^{j}dx-\sum\limits_{i+j=0}^{n}a_{i,j}\oint_{\Gamma_{h}}x^{i}y^{j}dy\\ =&\sum\limits_{i+j=1,j\geq 1}^{n}\xi_{i,j}I_{i,j}(h),\end{aligned} |  | (2.1) |

in view of

 | ∮ Γ h x i ​ y j ​ d y = − i j + 1 ​ I i − 1, j + 1 ​ ( h), \displaystyle\begin{aligned} \oint_{\Gamma_{h}}x^{i}y^{j}dy=-\frac{i}{j+1}I_{i-1,j+1}(h),\end{aligned} |  | (2.2) |

where ξ i, j = b i, j + i + j j ​ a i + 1, j − 1 \xi_{i,j}=b_{i,j}+\frac{i+j}{j}a_{i+1,j-1} and can be chosen as free parameters.

Lemma 2.1 The following relationship holds

 | I n, 1 ​ ( h) = { 0, n ​ o ​ d ​ d, − 4 ∫ 0 2 ​ h 1 − λ x n ( λ 2 − λ) ​ x 2 + 2 ​ λ ​ h d x, n e v e n. \displaystyle I_{n,1}(h)=\begin{cases}0,\qquad\qquad\qquad\qquad\qquad\quad\quad\qquad\ \ n\ odd,\\ -4\int_{0}^{\sqrt{\frac{2h}{1-\lambda}}}x^{n}\sqrt{(\lambda^{2}-\lambda)x^{2}+2\lambda h}dx,\ n\ even.\end{cases} |  | (2.3) |

Proof Some direct computation yields

 | I n, 1 ​ ( h) = \displaystyle I_{n,1}(h)= | ∮ Γ h x n ​ y ​ 𝑑 x = ∫ 2 ​ h 1 − λ − 2 ​ h 1 − λ x n ​ [− λ ​ x 2 − λ ​ x + ( λ 2 − λ) ​ x 2 + 2 ​ λ ​ h] ​ 𝑑 x \displaystyle\oint_{\Gamma_{h}}x^{n}ydx=\int_{\sqrt{\frac{2h}{1-\lambda}}}^{-\sqrt{\frac{2h}{1-\lambda}}}x^{n}\big[-\lambda x^{2}-\lambda x+\sqrt{(\lambda^{2}-\lambda)x^{2}+2\lambda h}\big]dx |  |

 |  | + ∫ − 2 ​ h 1 − λ 2 ​ h 1 − λ x n [− λ x 2 − λ x − ( λ 2 − λ) ​ x 2 + 2 ​ λ ​ h] d x \displaystyle+\int_{-\sqrt{\frac{2h}{1-\lambda}}}^{\sqrt{\frac{2h}{1-\lambda}}}x^{n}\big[-\lambda x^{2}-\lambda x-\sqrt{(\lambda^{2}-\lambda)x^{2}+2\lambda h}\big]dx |  |

 | = \displaystyle= | − 2 ∫ − 2 ​ h 1 − λ 2 ​ h 1 − λ x n ( λ 2 − λ) ​ x 2 + 2 ​ λ ​ h d x. \displaystyle-2\int_{-\sqrt{\frac{2h}{1-\lambda}}}^{\sqrt{\frac{2h}{1-\lambda}}}x^{n}\sqrt{(\lambda^{2}-\lambda)x^{2}+2\lambda h}dx. |  |

Note that when n n is odd, the integrand of the above integral is an odd function, and when n n is even, the integrand is an even function. Then (2.3) follows immediately by symmetry. This completes the proof. ◊ \lozenge

The following lemma plays a crucial role in determining the algebraic structure of the Abelian integral I ⁡ ( h) I(h).

Lemma 2.2 For n ≥ 5 n\geq 5, the Abelian integral I ⁡ ( h) I(h) can be expressed as

 | I ⁡ ( h) = ∑ i = 1 n − 2 P ¯ [n + 1 − i 4] ​ ( h) ​ I 0, i ​ ( h) + α 1 ​ I 0, n − 1 ​ ( h) + α 2 ​ I 0, n ​ ( h) + ∑ i = 2 n − 3 Q ¯ [n + 1 − i 4] ( h) I 1, i ( h) + β 1 I 1, n − 2 ( h) + β 2 I 1, n − 1 ( h), \displaystyle\begin{aligned} I(h)=&\sum\limits_{i=1}^{n-2}\bar{P}_{[\frac{n+1-i}{4}]}(h)I_{0,i}(h)+\alpha_{1}I_{0,n-1}(h)+\alpha_{2}I_{0,n}(h)\\ &+\sum\limits_{i=2}^{n-3}\bar{Q}_{[\frac{n+1-i}{4}]}(h)I_{1,i}(h)+\beta_{1}I_{1,n-2}(h)+\beta_{2}I_{1,n-1}(h),\end{aligned} |  | (2.4) |

where P ¯ l ​ ( h) \bar{P}_{l}(h) and Q ¯ l ​ ( h) \bar{Q}_{l}(h) are polynomials of degree l l.

Proof Differentiating both sides of H ⁡ ( x, y) = h H(x,y)=h in (1.7) with respect to x x gives

 | x + y + 2 ​ x ​ y + 3 ​ λ ​ x 2 + 2 ​ λ ​ x 3 + λ − 1 ​ y ​ ∂ y ∂ x + x ​ ∂ y ∂ x + x 2 ​ ∂ y ∂ x = 0. \displaystyle\begin{aligned} x+y+2xy+3\lambda x^{2}+2\lambda x^{3}+\lambda^{-1}y\frac{\partial y}{\partial x}+x\frac{\partial y}{\partial x}+x^{2}\frac{\partial y}{\partial x}=0.\end{aligned} |  | (2.5) |

Multiplying both sides of (2.5) by x i − 3 ​ y j ​ d ​ x x^{i-3}y^{j}dx and integrating along Γ h \Gamma_{h}, one gets

 | I i, j ​ ( h) = 1 2 ​ λ [i − 3 λ ⁡ ( j + 2) I i − 4, j + 2 ( h) − I i − 2, j ( h) + i − 2 ​ j − 3 j + 1 I i − 2, j + 1 ( h) − 3 λ I i − 1, j ( h) + i − j − 3 j + 1 I i − 3, j + 1 ( h)]. \displaystyle\begin{aligned} I_{i,j}(h)=&\frac{1}{2\lambda}\Big[\frac{i-3}{\lambda(j+2)}I_{i-4,j+2}(h)-I_{i-2,j}(h)+\frac{i-2j-3}{j+1}I_{i-2,j+1}(h)\\ &-3\lambda I_{i-1,j}(h)+\frac{i-j-3}{j+1}I_{i-3,j+1}(h)\Big].\end{aligned} |  | (2.6) |

At the same time, multiplying both sides of H ⁡ ( x, y) = h H(x,y)=h by x i ​ y j − 2 ​ d ​ x x^{i}y^{j-2}dx and integrating along Γ h \Gamma_{h} imply

 | I i, j ​ ( h) = 2 ​ λ ​ h ​ I i, j − 2 ​ ( h) − λ ​ I i + 2, j − 2 ​ ( h) − 2 ​ λ ​ I i + 2, j − 1 ​ ( h) − λ 2 ​ I i + 4, j − 2 ​ ( h) − 2 ​ λ ​ I i + 1, j − 1 ​ ( h) − 2 ​ λ 2 ​ I i + 3, j − 2 ​ ( h). \displaystyle\begin{aligned} I_{i,j}(h)=&2\lambda hI_{i,j-2}(h)-\lambda I_{i+2,j-2}(h)-2\lambda I_{i+2,j-1}(h)\\ &-\lambda^{2}I_{i+4,j-2}(h)-2\lambda I_{i+1,j-1}(h)-2\lambda^{2}I_{i+3,j-2}(h).\end{aligned} |  | (2.7) |

On account of (2.6) and (2.7), one can derive two recurrence formulas

 | I i, j ​ ( h) = 1 λ ⁡ ( i + 2 ​ j + 1) [2 ( i − 3) h I i − 4, j ( h) − ( i + j − 1) I i − 2, j ( h) − λ ⁡ ( 2 ​ i + 3 ​ j) ​ I i − 1, j ​ ( h) − j ⁡ ( i + 2 ​ j + 1) j + 1 ​ I i − 2, j + 1 ​ ( h) − j ⁡ ( i + j − 1) j + 1 I i − 3, j + 1 ( h)], \displaystyle\begin{aligned} I_{i,j}(h)=&\frac{1}{\lambda(i+2j+1)}\Big[2(i-3)hI_{i-4,j}(h)-(i+j-1)I_{i-2,j}(h)\\ &-\lambda(2i+3j)I_{i-1,j}(h)-\frac{j(i+2j+1)}{j+1}I_{i-2,j+1}(h)\\ &-\frac{j(i+j-1)}{j+1}I_{i-3,j+1}(h)\Big],\end{aligned} |  | (2.8) |

and

 | I i, j ​ ( h) = λ ​ j i + 2 ​ j + 1 [4 h I i, j − 2 ( h) − I i + 2, j − 2 ( h) − λ I i + 3, j − 2 ( h) − i + 2 ​ j + 1 j − 1 I i + 2, j − 1 ( h) − i + 3 ​ j − 1 j − 1 I i + 1, j − 1 ( h)]. \displaystyle\begin{aligned} I_{i,j}(h)=&\frac{\lambda j}{i+2j+1}\Big[4hI_{i,j-2}(h)-I_{i+2,j-2}(h)-\lambda I_{i+3,j-2}(h)\\ &-\frac{i+2j+1}{j-1}I_{i+2,j-1}(h)-\frac{i+3j-1}{j-1}I_{i+1,j-1}(h)\Big].\end{aligned} |  | (2.9) |

Eliminating I i + 2, j − 1 ​ ( h) I_{i+2,j-1}(h) and I i + 3, j − 2 ​ ( h) I_{i+3,j-2}(h) in (2.9) using (2.8) leads to

 | 4 ​ λ ​ j ​ ( j − 1) ​ ( i + 2 ​ j) ​ h ​ I i, j − 2 ​ ( h) + j ⁡ ( i + j) ​ ( i + 2 ​ j + λ ​ j − 2 ​ λ) ​ I i, j − 1 ​ ( h) − 2 ​ j ​ ( i − 1) ​ ( i + 2 ​ j) ​ h ​ I i − 2, j − 1 ​ ( h) + ( i + j) ​ ( j − 1) ​ ( i + 2 ​ j) ​ I i − 1, j ​ ( h) + λ ​ j ​ ( i + j) ​ ( i + 2 ​ j) ​ I i + 1, j − 1 ​ ( h) − λ ​ j ​ ( j − 1) ​ ( i + 2 ​ j − 2 ​ λ ​ i − 3 ​ λ ​ j) ​ I i + 2, j − 2 ​ ( h) − 2 ​ λ ​ i ​ j ​ ( j − 1) ​ h ​ I i − 1, j − 2 ​ ( h) + λ ​ j ​ ( j − 1) ​ ( i + j) ​ I i + 1, j − 2 ​ ( h) = 0. \displaystyle\begin{aligned} &4\lambda j(j-1)(i+2j)hI_{i,j-2}(h)+j(i+j)(i+2j+\lambda j-2\lambda)I_{i,j-1}(h)\\ &-2j(i-1)(i+2j)hI_{i-2,j-1}(h)+(i+j)(j-1)(i+2j)I_{i-1,j}(h)\\ &+\lambda j(i+j)(i+2j)I_{i+1,j-1}(h)-\lambda j(j-1)(i+2j-2\lambda i-3\lambda j)I_{i+2,j-2}(h)\\ &-2\lambda ij(j-1)hI_{i-1,j-2}(h)+\lambda j(j-1)(i+j)I_{i+1,j-2}(h)=0.\end{aligned} |  | (2.10) |

Taking i → i − 1, j → j + 1 i\rightarrow i-1,j\rightarrow j+1 in (2.10) yields another required recurrence formula

 | I i, j ​ ( h) = − 1 λ ⁡ ( j + 1) ​ ( i + j) ​ ( i + 2 ​ j + 1) [4 λ j ( j + 1) ( i + 2 j + 1) h I i − 1, j − 1 ( h) − 2 ​ ( i − 2) ​ ( j + 1) ​ ( i + 2 ​ j + 1) ​ h ​ I i − 3, j ​ ( h) + j ⁡ ( i + j) ​ ( i + 2 ​ j + 1) ​ I i − 2, j + 1 ​ ( h) + ( j + 1) ​ ( i + j) ​ ( i + 2 ​ j + 1 + λ ​ j − λ) ​ I i − 1, j ​ ( h) − λ ​ j ​ ( j + 1) ​ ( i + 2 ​ j + 1 − 2 ​ λ ​ i − 3 ​ λ ​ j − λ) ​ I i + 1, j − 1 ​ ( h) − 2 λ j ( i − 1) ( j + 1) h I i − 2, j − 1 ( h) + λ j ( j + 1) ( i + j) I i, j − 1 ( h)]. \displaystyle\begin{aligned} I_{i,j}(h)=&-\frac{1}{\lambda(j+1)(i+j)(i+2j+1)}\big[4\lambda j(j+1)(i+2j+1)hI_{i-1,j-1}(h)\\ &-2(i-2)(j+1)(i+2j+1)hI_{i-3,j}(h)+j(i+j)(i+2j+1)I_{i-2,j+1}(h)\\ &+(j+1)(i+j)\big(i+2j+1+\lambda j-\lambda\big)I_{i-1,j}(h)\\ &-\lambda j(j+1)\big(i+2j+1-2\lambda i-3\lambda j-\lambda\big)I_{i+1,j-1}(h)\\ &-2\lambda j(i-1)(j+1)hI_{i-2,j-1}(h)+\lambda j(j+1)(i+j)I_{i,j-1}(h)\big].\end{aligned} |  | (2.11) |

We are now in a position to prove (2.4) by induction on n n using the recurrence formulas (2.8) and (2.11). It follows from (2.8), (2.11) and Lemma 2.1 that

 | I 2, 1 ​ ( h) = − 1 2 ​ λ ​ I 0, 2 ​ ( h), I 2, 2 ​ ( h) = 1 7 ​ h ​ I 0, 1 ​ ( h) − λ + 6 7 ​ λ ​ I 0, 2 ​ ( h) − 2 3 ​ λ ​ I 0, 3 ​ ( h), I 3, 2 ​ ( h) = − 3 14 ​ h ​ I 0, 1 ​ ( h) − 3 14 ​ λ ​ I 0, 2 ​ ( h) + 2 3 ​ λ ​ I 0, 3 ​ ( h) + 3 ​ λ + 14 14 ​ λ ​ I 1, 2 ​ ( h) − 2 3 ​ λ ​ I 1, 3 ​ ( h), I 4, 1 ​ ( h) = − 1 28 ​ λ ​ h ​ I 0, 1 ​ ( h) + 3 14 ​ λ 2 ​ I 0, 2 ​ ( h) + 1 3 ​ λ 2 ​ I 0, 3 ​ ( h) + λ + 7 28 ​ λ 2 ​ I 1, 2 ​ ( h), I 2, 3 ​ ( h) = 42 ​ λ − 37 210 ​ h ​ I 0, 1 ​ ( h) + 1 210 ​ λ ​ ( 28 ​ λ ​ h + 42 ​ λ − 37) ​ I 0, 2 ​ ( h) − 28 45 ​ λ ​ ( λ − 1) ​ I 0, 3 ​ ( h) − 3 4 ​ λ ​ I 0, 4 ​ ( h) + 1 5 ​ λ ​ ( 2 ​ λ − 7) ​ I 1, 3 ​ ( h) − 1 210 ​ λ ​ ( 504 ​ λ ​ h + 42 ​ λ 2 + 159 ​ λ − 196) ​ I 1, 2 ​ ( h), \displaystyle\begin{aligned} I_{2,1}(h)=&-\frac{1}{2\lambda}I_{0,2}(h),\\ I_{2,2}(h)=&\frac{1}{7}hI_{0,1}(h)-\frac{\lambda+6}{7\lambda}I_{0,2}(h)-\frac{2}{3\lambda}I_{0,3}(h),\\ I_{3,2}(h)=&-\frac{3}{14}hI_{0,1}(h)-\frac{3}{14\lambda}I_{0,2}(h)+\frac{2}{3\lambda}I_{0,3}(h)+\frac{3\lambda+14}{14\lambda}I_{1,2}(h)-\frac{2}{3\lambda}I_{1,3}(h),\\ I_{4,1}(h)=&-\frac{1}{28\lambda}hI_{0,1}(h)+\frac{3}{14\lambda^{2}}I_{0,2}(h)+\frac{1}{3\lambda^{2}}I_{0,3}(h)+\frac{\lambda+7}{28\lambda^{2}}I_{1,2}(h),\\ I_{2,3}(h)=&\frac{42\lambda-37}{210}hI_{0,1}(h)+\frac{1}{210\lambda}(28\lambda h+42\lambda-37)I_{0,2}(h)\\ &-\frac{28}{45\lambda}(\lambda-1)I_{0,3}(h)-\frac{3}{4\lambda}I_{0,4}(h)+\frac{1}{5\lambda}(2\lambda-7)I_{1,3}(h)\\ &-\frac{1}{210\lambda}(504\lambda h+42\lambda^{2}+159\lambda-196)I_{1,2}(h),\end{aligned} |  | (2.12) |

which yields that (2.4) is valid for n = 5 n=5. Some tedious manipulation using (2.8) and (2.11) gives rise to

 | 𝚽 ⁡ ( I 2, n − 2 ​ ( h) I 3, n − 3 ​ ( h) I 4, n − 4 ​ ( h) I n − 2, 2 ​ ( h) I n − 1, 1 ​ ( h)) = ( v 1 ​ ( h) v 2 ​ ( h) v 3 ​ ( h) v n − 3 ​ ( h) v n − 2 ​ ( h)), \displaystyle\mathbf{\Phi}\left(\begin{matrix}I_{2,n-2}(h)\\ I_{3,n-3}(h)\\ I_{4,n-4}(h)\\ \vdots\\ I_{n-2,2}(h)\\ I_{n-1,1}(h)\end{matrix}\right)=\left(\begin{matrix}v_{1}(h)\\ v_{2}(h)\\ v_{3}(h)\\ \vdots\\ v_{n-3}(h)\\ v_{n-2}(h)\end{matrix}\right), |  | (2.13) |

where

 | v 1 ​ ( h) = − 1 λ ​ n ​ ( n − 1) ​ ( 2 ​ n − 1) [4 λ ( n − 1) ( n − 2) ( 2 n − 1) h I 1, n − 3 ( h) + n ⁡ ( n − 2) ​ ( 2 ​ n − 1) ​ I 0, n − 1 ​ ( h) + n ⁡ ( n − 1) ​ ( ( n − 3) ​ λ − 1 + 2 ​ n) ​ I 1, n − 2 ​ ( h) − 2 λ ( n − 1) ( n − 2) h I 0, n − 3 ( h) + λ n ( n − 1) ( n − 2) I 2, n − 3 ( h)], v 2 ​ ( h) = − 1 2 ​ λ ​ ( n − 2) [( n − 2) I 1, n − 3 ( h) + 2 ( n − 3) I 1, n − 2 ( h) + 3 λ ( n − 2) I 2, n − 3 ( h) + ( n − 3) I 0, n − 2 ( h)], v 3 ​ ( h) = − 1 λ ​ ( n − 3) ​ ( 2 ​ n − 3) [( n 2 − 5 n + 4) I 1, n − 3 ( h) + ( n 2 − 4 n + 3) I 2, n − 4 ( h) + ( 2 ​ n 2 − 11 ​ n + 12) ​ I 2, n − 3 ​ ( h) − 2 ​ ( n − 3) ​ h ​ I 0, n − 4 ​ ( h) + λ ( n − 3) ( 3 n − 4) I 3, n − 4 ( h)], ⋮ v n − 3 ​ ( h) = 1 3 ​ λ ​ ( n + 3) [6 ( n − 5) h I n − 6, 2 ( h) − 2 ( n − 1) I n − 5, 3 ( h) − 3 ( n − 1) I n − 4, 2 ( h) − 2 ( n + 3) I n − 4, 3 ( h) − 6 λ ( n + 1) I n − 3, 2 ( h)], v n − 2 ​ ( h) = 1 2 ​ λ ​ ( n + 2) [4 ( n − 4) h I n − 5, 1 ( h) − ( n − 1) I n − 4, 2 ( h) − 2 ( n − 1) I n − 3, 1 ( h) − ( n + 2) I n − 3, 2 ( h) − 2 λ ( 2 n + 1) I n − 2, 1 ( h)], \displaystyle\begin{aligned} v_{1}(h)=&-\frac{1}{\lambda n(n-1)(2n-1)}\big[4\lambda(n-1)(n-2)(2n-1)hI_{1,n-3}(h)\\ &+n(n-2)(2n-1)I_{0,n-1}(h)+n(n-1)((n-3)\lambda-1+2n)I_{1,n-2}(h)\\ &-2\lambda(n-1)(n-2)hI_{0,n-3}(h)+\lambda n(n-1)(n-2)I_{2,n-3}(h)\big],\\ v_{2}(h)=&-\frac{1}{2\lambda(n-2)}\big[(n-2)I_{1,n-3}(h)+2(n-3)I_{1,n-2}(h)\\ &+3\lambda(n-2)I_{2,n-3}(h)+(n-3)I_{0,n-2}(h)\big],\\ v_{3}(h)=&-\frac{1}{\lambda(n-3)(2n-3)}\big[(n^{2}-5n+4)I_{1,n-3}(h)+(n^{2}-4n+3)I_{2,n-4}(h)\\ &+(2n^{2}-11n+12)I_{2,n-3}(h)-2(n-3)hI_{0,n-4}(h)\\ &+\lambda(n-3)(3n-4)I_{3,n-4}(h)\big],\\ &\qquad\qquad\qquad\qquad\qquad\qquad\vdots\\ v_{n-3}(h)=&\frac{1}{3\lambda(n+3)}\big[6(n-5)hI_{n-6,2}(h)-2(n-1)I_{n-5,3}(h)-3(n-1)I_{n-4,2}(h)\\ &-2(n+3)I_{n-4,3}(h)-6\lambda(n+1)I_{n-3,2}(h)\big],\\ v_{n-2}(h)=&\frac{1}{2\lambda(n+2)}\big[4(n-4)hI_{n-5,1}(h)-(n-1)I_{n-4,2}(h)-2(n-1)I_{n-3,1}(h)\\ &-(n+2)I_{n-3,2}(h)-2\lambda(2n+1)I_{n-2,1}(h)\big],\end{aligned} |  |

 | 𝚽 = ( 1 ( n − 2) ​ ( ( 3 ​ n − 1) ​ λ + 1 − 2 ​ n) n ⁡ ( 2 ​ n − 1) 0 ⋯ 0 0 0 1 0 ⋯ 0 0 0 0 1 ⋯ 0 0 ⋱ 0 0 0 ⋯ 1 0 0 0 0 ⋯ 0 1). \mathbf{\Phi}=\left(\begin{matrix}1&\frac{(n-2)((3n-1)\lambda+1-2n)}{n(2n-1)}&0&\cdots&0&0\\ 0&1&0&\cdots&0&0\\ 0&0&1&\cdots&0&0\\ \vdots&\vdots&\vdots&\ddots&\vdots&\vdots\\ 0&0&0&\cdots&1&0\\ 0&0&0&\cdots&0&1\\ \end{matrix}\right). |  |

In order to invoke the induction hypothesis, we rewrite I ⁡ ( h) I(h) in the following form:

 | I ⁡ ( h) = ∑ i + j = 0 n ξ i, j ​ I i, j ​ ( h) = ∑ i + j = 0 n − 1 ξ i, j ​ I i, j ​ ( h) + ξ 0, n ​ I 0, n ​ ( h) + ξ 1, n − 1 ​ I 1, n − 1 ​ ( h) + ξ 2, n − 2 ​ I 2, n − 2 ​ ( h) + ⋯ + ξ n − 1, 1 ​ I n − 1, 1 ​ ( h). \displaystyle\begin{aligned} I(h)=\sum\limits_{i+j=0}^{n}\xi_{i,j}I_{i,j}(h)=&\sum\limits_{i+j=0}^{n-1}\xi_{i,j}I_{i,j}(h)+\xi_{0,n}I_{0,n}(h)+\xi_{1,n-1}I_{1,n-1}(h)\\ &+\xi_{2,n-2}I_{2,n-2}(h)+\cdots+\xi_{n-1,1}I_{n-1,1}(h).\end{aligned} |  |

Substituting (2.13) into the above equation and applying the induction hypothesis immediately yields (2.4). This completes the proof. ◊ \lozenge

Remark 2.1 (i) Although the recurrence formulas (2.8) and (2.11) play a crucial role in studying the algebraic structure of the Abelian integral I ⁡ ( h) I(h), I 0, n ​ ( h) I_{0,n}(h) and I 1, n − 1 ​ ( h) I_{1,n-1}(h) cannot be iterated using these two formulas. This implies that I ⁡ ( h) I(h) cannot be represented by a finite set of generators, which constitutes the most significant distinction from previous literature.

(ii) As evident from the proof of Lemma 2.2, both the iterative formula (2.11) itself and its derivation process are remarkably complex, owing to the intricate nature of the first integral of system (1.6).

In the lemma below, we present the exact expressions of I ⁡ ( h) I(h) corresponding to n = 1, 2, 3, 4, n=1,2,3,4, which are derived by direct computation using Lemma 2.1.

Lemma 2.3 The Abelian integral I ⁡ ( h) I(h) can be written as

 | I ⁡ ( h) = { ξ 0, 1 ​ I 0, 1 ​ ( h), n = 1, ξ 0, 1 ​ I 0, 1 ​ ( h) + ξ 0, 2 ​ I 0, 2 ​ ( h), n = 2, ξ 0, 1 ​ I 0, 1 ​ ( h) + ( ξ 0, 2 − 1 2 ​ λ ​ ξ 2, 1) ​ I 0, 2 ​ ( h) + ξ 0, 3 ​ I 0, 3 ​ ( h) + ξ 1, 2 ​ I 1, 2 ​ ( h), n = 3, ξ 0, 1 ​ I 0, 1 ​ ( h) + ( ξ 0, 2 − 1 2 ​ λ ​ ξ 2, 1 − 1 2 ​ λ ​ ξ 2, 2) ​ I 0, 2 ​ ( h) + ξ 0, 3 ​ I 0, 3 ​ ( h) + ξ 1, 2 ​ I 1, 2 ​ ( h) + ξ 0, 4 ​ I 0, 4 ​ ( h) + ξ 1, 3 ​ I 1, 3 ​ ( h), n = 4. \displaystyle I(h)=\begin{cases}\xi_{0,1}I_{0,1}(h),\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\qquad\ n=1,\\ \xi_{0,1}I_{0,1}(h)+\xi_{0,2}I_{0,2}(h),\qquad\qquad\qquad\qquad\qquad\qquad\qquad\ \ \ n=2,\\ \xi_{0,1}I_{0,1}(h)+(\xi_{0,2}-\frac{1}{2\lambda}\xi_{2,1})I_{0,2}(h)+\xi_{0,3}I_{0,3}(h)+\xi_{1,2}I_{1,2}(h),\ n=3,\\ \xi_{0,1}I_{0,1}(h)+(\xi_{0,2}-\frac{1}{2\lambda}\xi_{2,1}-\frac{1}{2\lambda}\xi_{2,2})I_{0,2}(h)+\xi_{0,3}I_{0,3}(h)\\ \quad\qquad\quad\ +\xi_{1,2}I_{1,2}(h)+\xi_{0,4}I_{0,4}(h)+\xi_{1,3}I_{1,3}(h),\qquad\qquad\ \,\,n=4.\end{cases} |  |

Our current objective is to compute the integrals I 0, i ​ ( h) I_{0,i}(h) for i = 1, 2, ⋯, n i=1,2,\cdots,n, along with I 1, j ​ ( h) I_{1,j}(h) for j = 2, 3, ⋯, n − 1 j=2,3,\cdots,n-1 in Lemmas 2.2 and 2.3. This will enable us to derive a more detailed expression for the Abelian integral I ⁡ ( h) I(h). The following lemma plays a crucial role in the computation of I 0, i ​ ( h) I_{0,i}(h) and I 1, j ​ ( h) I_{1,j}(h).

Lemma 2.4 For n ≥ 3 n\geq 3, the following equalities hold:

 | I 2, n ​ ( h) = ∑ i = 1 n − 1 P ¯ 1 i ​ ( h) ​ I 0, i ​ ( h) + α ¯ 1 ​ I 0, n ​ ( h) + α ¯ 2 ​ I 0, n + 1 ​ ( h) + ∑ i = 2 n − 1 Q ¯ i 1 ( h) I 1, i ( h) + β ¯ 1 I 1, n ( h), I 3, n ​ ( h) = ∑ i = 1 n − 1 P ~ 1 i ​ ( h) ​ I 0, i ​ ( h) + α ~ 1 ​ I 0, n ​ ( h) + α ~ 2 ​ I 0, n + 1 ​ ( h) + ∑ i = 2 n − 1 Q ~ i 1 ( h) I 1, i ( h) + β ~ 1 I 1, n ( h) + β ~ 2 I 1, n + 1 ( h), I 4, n ​ ( h) = ∑ i = 1 n P ^ 1 i ​ ( h) ​ I 0, i ​ ( h) + α ^ 1 ​ I 0, n + 1 ​ ( h) + α ^ 2 ​ I 0, n + 2 ​ ( h) + ∑ i = 2 n Q ^ i 1 ( h) I 1, i ( h) + β ^ 1 I 1, n + 1 ( h), \displaystyle\begin{aligned} I_{2,n}(h)=&\sum\limits_{i=1}^{n-1}\bar{P}^{i}_{1}(h)I_{0,i}(h)+\bar{\alpha}_{1}I_{0,n}(h)+\bar{\alpha}_{2}I_{0,n+1}(h)\\ &+\sum\limits_{i=2}^{n-1}\bar{Q}^{i}_{1}(h)I_{1,i}(h)+\bar{\beta}_{1}I_{1,n}(h),\\ I_{3,n}(h)=&\sum\limits_{i=1}^{n-1}\tilde{P}^{i}_{1}(h)I_{0,i}(h)+\tilde{\alpha}_{1}I_{0,n}(h)+\tilde{\alpha}_{2}I_{0,n+1}(h)\\ &+\sum\limits_{i=2}^{n-1}\tilde{Q}^{i}_{1}(h)I_{1,i}(h)+\tilde{\beta}_{1}I_{1,n}(h)+\tilde{\beta}_{2}I_{1,n+1}(h),\\ I_{4,n}(h)=&\sum\limits_{i=1}^{n}\hat{P}^{i}_{1}(h)I_{0,i}(h)+\hat{\alpha}_{1}I_{0,n+1}(h)+\hat{\alpha}_{2}I_{0,n+2}(h)\\ &+\sum\limits_{i=2}^{n}\hat{Q}^{i}_{1}(h)I_{1,i}(h)+\hat{\beta}_{1}I_{1,n+1}(h),\\ \end{aligned} |  | (2.14) |

where P ¯ 1 i ​ ( h) \bar{P}_{1}^{i}(h), Q ¯ 1 i ​ ( h) \bar{Q}_{1}^{i}(h), P ~ 1 i ​ ( h) \tilde{P}_{1}^{i}(h), Q ~ 1 i ​ ( h) \tilde{Q}_{1}^{i}(h), P ^ 1 i ​ ( h) \hat{P}_{1}^{i}(h) and Q ^ 1 i ​ ( h) \hat{Q}_{1}^{i}(h) are linear polynomials of h h and α ¯ i, β ¯ i, α ~ i, β ~ i, α ^ i, β ^ i ∈ ℝ \bar{\alpha}_{i},\bar{\beta}_{i},\tilde{\alpha}_{i},\tilde{\beta}_{i},\hat{\alpha}_{i},\hat{\beta}_{i}\in\mathbb{R}.

Proof We only prove the first relation in (2.14) by mathematical induction, using (2.8) and (2.11). The proofs of the other two relations proceed in a similar fashion. The fifth relation in (2.12) implies that the conclusion holds when n = 3 n=3. Taking ( i, j) = ( 2, n + 1) (i,j)=(2,n+1) in (2.11) and ( i, j) = ( 3, n) (i,j)=(3,n) in (2.8) give rise to

 | I 2, n + 1 ​ ( h) = 2 ​ ( n + 1) ( n + 3) ​ ( 2 ​ n + 5) ​ h ​ I 0, n ​ ( h) − 4 ​ ( n + 1) n + 3 ​ h ​ I 1, n ​ ( h) − n + 1 2 ​ n + 5 ​ h ​ I 2, n ​ ( h) − n + 1 λ ⁡ ( n + 2) ​ I 0, n + 2 ​ ( h) − 2 ​ n + λ ​ n + 5 λ ⁡ ( 2 ​ n + 5) ​ I 1, n + 1 ​ ( h) + ( n + 1) ​ ( 2 ​ n − 3 ​ λ ​ n − 8 ​ λ + 5) 2 ​ n 2 + 11 ​ n + 15 ​ I 3, n ​ ( h), \displaystyle\begin{aligned} I_{2,n+1}(h)=&\frac{2(n+1)}{(n+3)(2n+5)}hI_{0,n}(h)-\frac{4(n+1)}{n+3}hI_{1,n}(h)-\frac{n+1}{2n+5}hI_{2,n}(h)\\ &-\frac{n+1}{\lambda(n+2)}I_{0,n+2}(h)-\frac{2n+\lambda n+5}{\lambda(2n+5)}I_{1,n+1}(h)\\ &+\frac{(n+1)(2n-3\lambda n-8\lambda+5)}{2n^{2}+11n+15}I_{3,n}(h),\end{aligned} |  | (2.15) |

and

 | I 3, n ​ ( h) = − 1 2 ​ λ ​ I 1, n ​ ( h) − 3 2 ​ I 2, n ​ ( h) − n λ ⁡ ( n + 1) ​ I 1, n + 1 ​ ( h) − n 2 ​ λ ​ ( n + 1) ​ I 0, n + 1 ​ ( h). \displaystyle\begin{aligned} I_{3,n}(h)=&-\frac{1}{2\lambda}I_{1,n}(h)-\frac{3}{2}I_{2,n}(h)-\frac{n}{\lambda(n+1)}I_{1,n+1}(h)-\frac{n}{2\lambda(n+1)}I_{0,n+1}(h).\end{aligned} |  | (2.16) |

By substituting (2.16) into (2.15), one obtains

 | I 2, n + 1 ​ ( h) = ( n + 1) ​ ( 9 ​ λ ​ n − 8 ​ n + 24 ​ λ − 21) 4 ​ n 2 + 22 ​ n + 30 ​ I 2, n ​ ( h) + 2 ​ ( n + 1) ( n + 3) ​ ( 2 ​ n + 5) ​ h ​ I 0, n ​ ( h) + n ⁡ ( 3 ​ λ ​ n − 2 ​ n + 8 ​ λ − 5) 2 ​ λ ​ ( n + 3) ​ ( 2 ​ n + 5) ​ I 0, n + 1 ​ ( h) − n + 1 λ ⁡ ( n + 2) ​ I 0, n + 2 ​ ( h) − ( n + 1) ​ ( ( 16 ​ λ ​ n + 40 ​ λ) ​ h − 3 ​ λ ​ n + 2 ​ n − 8 ​ λ + 5) 2 ​ λ ​ ( n + 3) ​ ( 2 ​ n + 5) ​ I 1, n ​ ( h) + λ ​ n − 2 ​ n − 3 λ ⁡ ( n + 3) ​ I 1, n + 1 ​ ( h). \displaystyle\begin{aligned} I_{2,n+1}(h)=&\frac{(n+1)(9\lambda n-8n+24\lambda-21)}{4n^{2}+22n+30}I_{2,n}(h)+\frac{2(n+1)}{(n+3)(2n+5)}hI_{0,n}(h)\\ &+\frac{n(3\lambda n-2n+8\lambda-5)}{2\lambda(n+3)(2n+5)}I_{0,n+1}(h)-\frac{n+1}{\lambda(n+2)}I_{0,n+2}(h)\\ &-\frac{(n+1)\big((16\lambda n+40\lambda)h-3\lambda n+2n-8\lambda+5\big)}{2\lambda(n+3)(2n+5)}I_{1,n}(h)\\ &+\frac{\lambda n-2n-3}{\lambda(n+3)}I_{1,n+1}(h).\end{aligned} |  | (2.17) |

The conclusion is immediately established by (2.17) together with the induction hypothesis. This completes the proof. ◊ \lozenge

In order to determine I 0, i ​ ( h) I_{0,i}(h) and I 1, j ​ ( h) I_{1,j}(h), in addition to Lemma 2.4, we also need to find the differential equations they satisfy, as provided by the following lemma.

Lemma 2.5 For n ≥ 2 n\geq 2, the following differential equations hold:

 | I 0, n ​ ( h) = 4 ​ h ​ I 0, n ′ ​ ( h) − n n + 1 ​ I 1, n + 1 ′ ​ ( h) − I 2, n ′ ​ ( h) − λ ​ I 3, n ′ ​ ( h), \displaystyle\begin{aligned} &I_{0,n}(h)=4hI^{\prime}_{0,n}(h)-\frac{n}{n+1}I^{\prime}_{1,n+1}(h)-I^{\prime}_{2,n}(h)-\lambda I^{\prime}_{3,n}(h),\\ \end{aligned} |  | (2.18) |

 | I 1, n ​ ( h) = 2 ​ ( n + 3) 3 ​ h ​ I 1, n ′ ​ ( h) − n + 3 6 ​ I 3, n ′ ​ ( h) − λ ⁡ ( n + 3) 6 ​ I 4, n ′ ​ ( h) − n ⁡ ( n + 3) 6 ​ n + 6 ​ I 2, n + 1 ′ ​ ( h), \displaystyle\begin{aligned} I_{1,n}(h)=&\frac{2(n+3)}{3}hI^{\prime}_{1,n}(h)-\frac{n+3}{6}I^{\prime}_{3,n}(h)\\ &-\frac{\lambda(n+3)}{6}I^{\prime}_{4,n}(h)-\frac{n(n+3)}{6n+6}I^{\prime}_{2,n+1}(h),\end{aligned} |  | (2.19) |

where ′ means a differentiation with respect to h h.

Proof In the equation H ⁡ ( x, y) = h H(x,y)=h, we regard y y as a bivariate function of x x and h h. Differentiating both sides of H ⁡ ( x, y) = h H(x,y)=h with respect to h h gives

 | ∂ y ∂ h = 1 x + x 2 + λ − 1 ​ y, \frac{\partial y}{\partial h}=\frac{1}{x+x^{2}+\lambda^{-1}y}, |  |

which yields that

 | I i, j ′ ​ ( h) = j ​ ∮ Γ h x i ​ y j − 1 x + x 2 + λ − 1 ​ y ​ 𝑑 x. \displaystyle I^{\prime}_{i,j}(h)=j\oint_{\Gamma_{h}}\frac{x^{i}y^{j-1}}{x+x^{2}+\lambda^{-1}y}dx. |  | (2.20) |

A straightforward computation using (2.20), one has

 | I i, j ​ ( h) = 1 λ ⁡ ( j + 2) ​ I i, j + 2 ′ ​ ( h) + 1 j + 1 ​ I i + 1, j + 1 ′ ​ ( h) + 1 j + 1 ​ I i + 2, j + 1 ′ ​ ( h). \displaystyle I_{i,j}(h)=\frac{1}{\lambda(j+2)}I^{\prime}_{i,j+2}(h)+\frac{1}{j+1}I^{\prime}_{i+1,j+1}(h)+\frac{1}{j+1}I^{\prime}_{i+2,j+1}(h). |  | (2.21) |

Multiplying both sides of (2.20) by h h, one obtains

 | h ​ I i, j ′ ​ ( h) = 1 2 ​ I i + 2, j ′ ​ ( h) + λ ​ I i + 3, j ′ ​ ( h) + λ 2 ​ I i + 4, j ′ ​ ( h) + j 2 ​ λ ​ ( j + 2) ​ I i, j + 2 ′ ​ ( h) + j j + 1 ​ I i + 1, j + 1 ′ ​ ( h) + j j + 1 ​ I i + 2, j + 1 ′ ​ ( h). \displaystyle\begin{aligned} hI^{\prime}_{i,j}(h)=&\frac{1}{2}I^{\prime}_{i+2,j}(h)+\lambda I^{\prime}_{i+3,j}(h)+\frac{\lambda}{2}I^{\prime}_{i+4,j}(h)+\frac{j}{2\lambda(j+2)}I^{\prime}_{i,j+2}(h)\\ &+\frac{j}{j+1}I^{\prime}_{i+1,j+1}(h)+\frac{j}{j+1}I^{\prime}_{i+2,j+1}(h).\end{aligned} |  | (2.22) |

From another perspective, some routine calculations using (2.2) show

 | I i, j ​ ( h) = − j i + 1 ∮ Γ h x i + 1 y j − 1 d y = 1 i + 1 ​ I i + 2, j ′ ​ ( h) + j ( i + 1) ​ ( j + 1) ​ I i + 1, j + 1 ′ ​ ( h) + 3 ​ λ i + 1 ​ I i + 3, j ′ ​ ( h) + 2 ​ j ( i + 1) ​ ( j + 1) ​ I i + 2, j + 1 ′ ​ ( h) + 2 ​ λ i + 1 ​ I i + 4, j ′ ​ ( h). \displaystyle\begin{aligned} I_{i,j}(h)=&-\frac{j}{i+1}\oint_{\Gamma_{h}}x^{i+1}y^{j-1}dy\\ =&\frac{1}{i+1}I^{\prime}_{i+2,j}(h)+\frac{j}{(i+1)(j+1)}I^{\prime}_{i+1,j+1}(h)+\frac{3\lambda}{i+1}I^{\prime}_{i+3,j}(h)\\ &+\frac{2j}{(i+1)(j+1)}I^{\prime}_{i+2,j+1}(h)+\frac{2\lambda}{i+1}I^{\prime}_{i+4,j}(h).\end{aligned} |  | (2.23) |

It follows from (2.21), (2.22) and (2.23) that

 | I i, j ​ ( h) = i 2 + 3 ​ i + 2 ​ i ​ j + 2 ( i + 1) 2 ​ ( i + 2) ​ ( 4 ​ h ​ I i, j ′ ​ ( h) − I i + 2, j ′ ​ ( h) − λ ​ I i + 3, j ′ ​ ( h) − j j + 1 ​ I i + 1, j + 1 ′ ​ ( h)). \displaystyle I_{i,j}(h)=\frac{i^{2}+3i+2ij+2}{(i+1)^{2}(i+2)}\Big(4hI^{\prime}_{i,j}(h)-I^{\prime}_{i+2,j}(h)-\lambda I^{\prime}_{i+3,j}(h)-\frac{j}{j+1}I^{\prime}_{i+1,j+1}(h)\Big). |  | (2.24) |

Taking ( i, j) = ( 0, n), ( 1, n) (i,j)=(0,n),(1,n) in (2.24) gives (2.18) and (2.19). This completes the proof. ◊ \lozenge

Lemma 2.6 Let n n be a positive integer with n ≥ 2 n\geq 2. Then we have

 | I 0, n ​ ( h) = h ​ P n − 1 ​ ( h), I 1, n ​ ( h) = h ​ Q n − 1 ​ ( h), \displaystyle I_{0,n}(h)=hP_{n-1}(h),\ \ I_{1,n}(h)=hQ_{n-1}(h), |  | (2.25) |

where P n − 1 ​ ( h) P_{n-1}(h) and Q n − 1 ​ ( h) Q_{n-1}(h) are polynomials of degree n − 1 n-1.

Proof A direct calculation gives rise to

 | I 0, 2 ​ ( h) = I 1, 2 ​ ( h) = 8 ​ λ ​ ∫ 0 2 ​ h 1 − λ x 2 ​ 2 ​ λ ​ h + ( λ 2 − λ) ​ x 2 ​ d x = 2 ​ π ​ λ 3 2 ( 1 − λ) 3 2 ​ h 2, I 0, 3 ( h) = − 4 λ ∫ 0 2 ​ h 1 − λ ( 3 λ x 4 + 4 λ x 2 − x 2 + 2 h) 2 ​ λ ​ h + ( λ 2 − λ) ​ x 2 d x = − 3 ​ π ​ λ 3 2 ( 1 − λ) 5 2 ​ h ​ ( λ ​ h 2 − λ ​ h + h), I 1, 3 ( h) = − 24 λ 2 λ ∫ 0 2 ​ h 1 − λ x 4 2 ​ λ ​ h + ( λ 2 − λ) ​ x 2 d x = − 6 ​ π ​ λ 5 2 ( 1 − λ) 5 2 h 3, \displaystyle\begin{aligned} &I_{0,2}(h)=I_{1,2}(h)=8\lambda\int_{0}^{\sqrt{\frac{2h}{1-\lambda}}}x^{2}\sqrt{2\lambda h+(\lambda^{2}-\lambda)x^{2}}dx=\frac{2\pi\lambda^{\frac{3}{2}}}{(1-\lambda)^{\frac{3}{2}}}h^{2},\\ &I_{0,3}(h)=-4\lambda\int_{0}^{\sqrt{\frac{2h}{1-\lambda}}}(3\lambda x^{4}+4\lambda x^{2}-x^{2}+2h)\sqrt{2\lambda h+(\lambda^{2}-\lambda)x^{2}}dx\\ &\qquad\ \ =-\frac{3\pi\lambda^{\frac{3}{2}}}{(1-\lambda)^{\frac{5}{2}}}h(\lambda h^{2}-\lambda h+h),\\ &I_{1,3}(h)=-24\lambda^{2}\lambda\int_{0}^{\sqrt{\frac{2h}{1-\lambda}}}x^{4}\sqrt{2\lambda h+(\lambda^{2}-\lambda)x^{2}}dx=-\frac{6\pi\lambda^{\frac{5}{2}}}{(1-\lambda)^{\frac{5}{2}}}h^{3},\ \end{aligned} |  | (2.26) |

which imply that (2.25) is valid for n = 2, 3 n=2,3. Assume that (2.25) holds for all m ≤ n m\leq n. In order to find I 0, n + 1 ​ ( h) I_{0,n+1}(h) and I 1, n + 1 ​ ( h) I_{1,n+1}(h), we proceed to establish the differential equations they satisfy. In fact, replacing n n by n − 1 n-1 in (2.19), one has

 | I 1, n − 1 ​ ( h) = 2 ​ ( n + 2) 3 ​ h ​ I 1, n − 1 ′ ​ ( h) − n + 2 6 ​ I 3, n − 1 ′ ​ ( h) − λ ⁡ ( n + 2) 6 ​ I 4, n − 1 ′ ​ ( h) − ( n − 1) ​ ( n + 2) 6 ​ n ​ I 2, n ′ ​ ( h). \displaystyle\begin{aligned} I_{1,n-1}(h)=&\frac{2(n+2)}{3}hI^{\prime}_{1,n-1}(h)-\frac{n+2}{6}I^{\prime}_{3,n-1}(h)\\ &-\frac{\lambda(n+2)}{6}I^{\prime}_{4,n-1}(h)-\frac{(n-1)(n+2)}{6n}I^{\prime}_{2,n}(h).\end{aligned} |  | (2.27) |

Plugging (2.14) into ( 2.27) (2.27) and applying the induction hypothesis implies a simple differential equation satisfied by I 0, n + 1 ′ ​ ( h) I^{\prime}_{0,n+1}(h)

 | I 0, n + 1 ′ ​ ( h) = P ˇ n ​ ( h), \displaystyle I^{\prime}_{0,n+1}(h)=\check{P}_{n}(h), |  | (2.28) |

where P ˇ n ​ ( h) \check{P}_{n}(h) is a polynomial of degree n n. Solving differential equation (2.28) yields the first equality in (2.25). Substituting (2.14) into (2.18) and applying the induction hypothesis together with (2.28), one can obtain the differential equation satisfied by I 1, n + 1 ′ ​ ( h) I^{\prime}_{1,n+1}(h) as follows

 | I 1, n + 1 ′ ​ ( h) = Q ˇ n ​ ( h), \displaystyle I^{\prime}_{1,n+1}(h)=\check{Q}_{n}(h), |  | (2.29) |

where Q ˇ n ​ ( h) \check{Q}_{n}(h) is a polynomial of degree n n. Solving the above differential equation gives the second equality in (2.25). This completes the proof. ◊ \lozenge

With the preceding preparations in place, we can now derive a more complete expression for the Abelian integral I ⁡ ( h) I(h), which in fact takes polynomial form.

Proposition 2.1 The Abelian integral I ⁡ ( h) I(h) can be expressed as

 | I ⁡ ( h) = ∑ i = 1 n α i ​ h i, \displaystyle I(h)=\sum\limits_{i=1}^{n}\alpha_{i}h^{i}, |  | (2.30) |

where α i, i = 1, 2, ⋯, n \alpha_{i},i=1,2,\cdots,n are arbitrary constants that can be expressed in terms of ξ i, j \xi_{i,j}.

Proof We prove the proposition by induction on n n. When n = 2 n=2, after a direct computation, one has

 | I ⁡ ( h) = ξ 0, 1 ​ I 0, 1 ​ ( h) + ξ 0, 2 ​ I 0, 2 ​ ( h) = α 1 ​ h + α 2 ​ h 2, \displaystyle I(h)=\xi_{0,1}I_{0,1}(h)+\xi_{0,2}I_{0,2}(h)=\alpha_{1}h+\alpha_{2}h^{2}, |  | (2.31) |

where

 | α 1 = − 2 ​ π ​ λ 1 − λ ​ ξ 0, 1, α 2 = 2 ​ π ​ λ 3 2 ( 1 − λ) 3 2 ​ ξ 0, 2. \alpha_{1}=-\frac{2\pi\sqrt{\lambda}}{\sqrt{1-\lambda}}\xi_{0,1},\ \alpha_{2}=\frac{2\pi\lambda^{\frac{3}{2}}}{(1-\lambda)^{\frac{3}{2}}}\xi_{0,2}. |  |

By taking advantage of the above two equalities, one gets that the determinant of the following matrix

 | ∂ ( α 1, α 2) ∂ ( ξ 0, 1, ξ 0, 2) = ( − 2 ​ π ​ λ 1 − λ 0 0 2 ​ π ​ λ 3 2 ( 1 − λ) 3 2) \frac{\partial(\alpha_{1},\alpha_{2})}{\partial(\xi_{0,1},\xi_{0,2})}=\begin{pmatrix}-\frac{2\pi\sqrt{\lambda}}{\sqrt{1-\lambda}}&0\\ 0&\frac{2\pi\lambda^{\frac{3}{2}}}{(1-\lambda)^{\frac{3}{2}}}\\ \end{pmatrix} |  |

is different from 0 0. This implies that α 1 \alpha_{1} and α 2 \alpha_{2} can be taken as free parameters. Similar to the arguments in the case for n = 2 n=2, when n = 3 n=3, the Abelian integral I ⁡ ( h) I(h) can be written as

 | I ⁡ ( h) = ξ 0, 1 ​ I 0, 1 ​ ( h) + ξ 0, 2 ​ I 0, 2 ​ ( h) + ξ 0, 3 ​ I 0, 3 ​ ( h) + ξ 1, 2 ​ I 1, 2 ​ ( h) + ξ 2, 1 ​ I 2, 1 ​ ( h) = α 1 ​ h + α 2 ​ h 2 + α 3 ​ h 3, \displaystyle\begin{aligned} I(h)&=\xi_{0,1}I_{0,1}(h)+\xi_{0,2}I_{0,2}(h)+\xi_{0,3}I_{0,3}(h)+\xi_{1,2}I_{1,2}(h)+\xi_{2,1}I_{2,1}(h)\\ &=\alpha_{1}h+\alpha_{2}h^{2}+\alpha_{3}h^{3},\end{aligned} |  | (2.32) |

where

 |  | α 1 = − 2 ​ π ​ λ 1 − λ ξ 0, 1, α 3 = − 3 ​ π ​ λ 5 2 ( 1 − λ) 5 2 ξ 0, 3, \displaystyle\alpha_{1}=-\frac{2\pi\sqrt{\lambda}}{\sqrt{1-\lambda}}\xi_{0,1},\ \alpha_{3}=-\frac{3\pi\lambda^{\frac{5}{2}}}{(1-\lambda)^{\frac{5}{2}}}\xi_{0,3}, |  |

 |  | α 2 = 2 ​ π ​ λ 3 2 ( 1 − λ) 3 2 ​ ξ 0, 2 − 3 ​ π ​ λ 3 2 ( 1 − λ) 3 2 ​ ξ 0, 3 + 2 ​ π ​ λ 3 2 ( 1 − λ) 3 2 ​ ξ 1, 2 − π ​ λ ( 1 − λ) 3 2 ​ ξ 2, 1. \displaystyle\alpha_{2}=\frac{2\pi\lambda^{\frac{3}{2}}}{(1-\lambda)^{\frac{3}{2}}}\xi_{0,2}-\frac{3\pi\lambda^{\frac{3}{2}}}{(1-\lambda)^{\frac{3}{2}}}\xi_{0,3}+\frac{2\pi\lambda^{\frac{3}{2}}}{(1-\lambda)^{\frac{3}{2}}}\xi_{1,2}-\frac{\pi\sqrt{\lambda}}{(1-\lambda)^{\frac{3}{2}}}\xi_{2,1}. |  |

Note that ξ 0, 1 \xi_{0,1} does not appear in α 2 \alpha_{2}, ξ 0, 1 \xi_{0,1} and ξ 0, 2 \xi_{0,2} do not appear in α 3 \alpha_{3} and ξ 0, 3 \xi_{0,3} must appear in α 3 \alpha_{3}. Hence, one gets

 | det [∂ ( α 1, α 2, α 3) ∂ ( ξ 0, 1, ξ 0, 2, ξ 0, 3)] = det [( − 2 ​ π ​ λ 1 − λ 0 0 0 2 ​ π ​ λ 3 2 ( 1 − λ) 3 2 − 3 ​ π ​ λ 3 2 ( 1 − λ) 3 2 0 0 − 3 ​ π ​ λ 5 2 ( 1 − λ) 5 2)] = 12 ​ π 3 ​ λ 9 2 ( 1 − λ) 9 2 ≠ 0, \det\Big[\frac{\partial(\alpha_{1},\alpha_{2},\alpha_{3})}{\partial(\xi_{0,1},\xi_{0,2},\xi_{0,3})}\Big]=\det\Big[\begin{pmatrix}-\frac{2\pi\sqrt{\lambda}}{\sqrt{1-\lambda}}&0&0\\ 0&\frac{2\pi\lambda^{\frac{3}{2}}}{(1-\lambda)^{\frac{3}{2}}}&-\frac{3\pi\lambda^{\frac{3}{2}}}{(1-\lambda)^{\frac{3}{2}}}\\ 0&0&-\frac{3\pi\lambda^{\frac{5}{2}}}{(1-\lambda)^{\frac{5}{2}}}\end{pmatrix}\Big]=\frac{12\pi^{3}\lambda^{\frac{9}{2}}}{(1-\lambda)^{\frac{9}{2}}}\neq 0, |  |

which yields that α 1 \alpha_{1}, α 2 \alpha_{2}, and α 3 \alpha_{3} can be chosen arbitrarily. In view of Lemma 2.6 and (2.13), one has

 | I ⁡ ( h) = \displaystyle I(h)= | ∑ i + j = 0 n ξ i, j ​ I i, j ​ ( h) \displaystyle\sum\limits_{i+j=0}^{n}\xi_{i,j}I_{i,j}(h) |  |

 | = \displaystyle= | ∑ i + j = 0 n − 1 ξ i, j ​ I i, j ​ ( h) + ξ 0, n ​ I 0, n ​ ( h) + ξ 1, n − 1 ​ I 1, n − 1 ​ ( h) + ⋯ + ξ n − 1, 1 ​ I n − 1, 1 ​ ( h) \displaystyle\sum\limits_{i+j=0}^{n-1}\xi_{i,j}I_{i,j}(h)+\xi_{0,n}I_{0,n}(h)+\xi_{1,n-1}I_{1,n-1}(h)+\cdots+\xi_{n-1,1}I_{n-1,1}(h) |  |

 | = \displaystyle= | α ~ 1 ​ h + α ~ 2 ​ h 2 + ⋯ + α ~ n − 1 ​ h n − 1 \displaystyle\tilde{\alpha}_{1}h+\tilde{\alpha}_{2}h^{2}+\cdots+\tilde{\alpha}_{n-1}h^{n-1} |  |

 |  | + ξ 0, n ​ I 0, n ​ ( h) + ξ 1, n − 1 ​ I 1, n − 1 ​ ( h) + ⋯ + ξ n − 1, 1 ​ I n − 1, 1 ​ ( h) \displaystyle+\xi_{0,n}I_{0,n}(h)+\xi_{1,n-1}I_{1,n-1}(h)+\cdots+\xi_{n-1,1}I_{n-1,1}(h) |  |

 | ≜ \displaystyle\triangleq | ∑ i = 1 n α i ​ h i, \displaystyle\sum\limits_{i=1}^{n}\alpha_{i}h^{i}, |  |

where the second and third equalities employ the induction hypothesis. Again, thanks to the induction hypothesis, one has α ~ 1 \tilde{\alpha}_{1}, α ~ 2 \tilde{\alpha}_{2}, ⋯ \cdots, α ~ n − 1 \tilde{\alpha}_{n-1} are mutually independent, which implies that the determinant of the Jacobian matrix

 | 𝐀 = ∂ ( α 1, α 2, ⋯, α n − 1) ∂ ( ξ i 1, j 1, ξ i 2, j 2, ⋯, ξ i n − 1, j n − 1) \mathbf{A}=\frac{\partial(\alpha_{1},\alpha_{2},\cdots,\alpha_{n-1})}{\partial(\xi_{i_{1},j_{1}},\xi_{i_{2},j_{2}},\cdots,\xi_{i_{n-1},j_{n-1}})} |  |

is non-vanishing, where the sum of the two subscripts of ξ \xi in the above matrix 𝐀 \mathbf{A} is less than n n. Observe that α n \alpha_{n} is the coefficient of h n h^{n}, hence ξ i 1, j 1, ξ i 2, j 2, ⋯, ξ i n − 1, j n − 1 \xi_{i_{1},j_{1}},\xi_{i_{2},j_{2}},\cdots,\xi_{i_{n-1},j_{n-1}} do not appear in α n \alpha_{n}. It follows that the partial derivatives of α n \alpha_{n} with respect to them all vanish. According to Lemma 2.6, ξ 0, n \xi_{0,n} must appear in α n \alpha_{n}. Based on the previous arguments, it follows that

 | 𝐁 = ∂ ( α 1, α 2, ⋯, α n − 1, α n) ∂ ( ξ i 1, j 1, ξ i 1, j 1, ⋯, ξ i n − 1, j n − 1, ξ 0, n) = ( 𝐀 𝐂 𝟎 δ), \mathbf{B}=\frac{\partial(\alpha_{1},\alpha_{2},\cdots,\alpha_{n-1},\alpha_{n})}{\partial(\xi_{i_{1},j_{1}},\xi_{i_{1},j_{1}},\cdots,\xi_{i_{n-1},j_{n-1}},\xi_{0,n})}=\left(\begin{array}[]{ccc}\mathbf{A}&\mathbf{C}\\ \mathbf{0}&\delta\\ \end{array}\right), |  |

where 𝐂 \mathbf{C} is an ( n − 1) (n-1) -dimensional column vector, 𝟎 \mathbf{0} is an ( n − 1) (n-1) -dimensional zero row vector, and δ \delta is a nonzero constant. Therefore, one gets

 | det ( 𝐁) = δ ​ det ( 𝐀) ≠ 0, \det(\mathbf{B})=\delta\det(\mathbf{A})\neq 0, |  |

which implies that α 1 \alpha_{1}, α 2 \alpha_{2}, ⋯ \cdots, α n − 1, α n \alpha_{n-1},\alpha_{n} are mutually independent. This completes the proof. ◊ \lozenge

Remark 2.2 When determining the lower bound of the number of limit cycles, it is essential to verify the independence of the coefficients of I ⁡ ( h) I(h) in (2.30). According to conventional methods used in existing literature, this requires obtaining an explicit expression of α i \alpha_{i}, i = 1, 2, ⋯, n i=1,2,\cdots,n in terms of ξ i, j \xi_{i,j}, i = 0, 1, 2, ⋯, n; j = 0, 1, 2, ⋯, n i=0,1,2,\cdots,n;j=0,1,2,\cdots,n. This is a task that is extremely difficult or even impossible to accomplish. During the proof of Proposition 2.1, by skillfully applying mathematical induction, we successfully circumvent this difficulty by focusing exclusively on the coefficient α n \alpha_{n} of h n h^{n}. This approach not only dramatically reduced computational effort but also achieved what was previously deemed impossible.

## 3 Proof of the main result and numerical simulation

In order to obtain the lower bound of the number of zeros of I ⁡ ( h) I(h), we resort to a result of Coll, Gasull and Prohens published in [10]. We review this result here for the convenience of the reader.

Lemma 3.1 Consider p + 1 p+1 linearly independent analytical functions f i: U → ℝ, i = 0, 1, 2, ⋯, p f_{i}:U\rightarrow\mathbb{R},\ i=0,1,2,\cdots,p, where U ⊂ ℝ U\subset\mathbb{R} is an interval. Suppose that there exists j ∈ { 0, 1, ⋯, p } j\in\{0,1,\cdots,p\} such that f j f_{j} has constant sign. Then there exists p + 1 p+1 constants δ i, i = 0, 1, ⋯, p \delta_{i},\ i=0,1,\cdots,p, such that f ⁡ ( x) = ∑ i = 0 p δ i ​ f i ​ ( x) f(x)=\sum\limits_{i=0}^{p}\delta_{i}f_{i}(x) has at least p p simple zeros in U U.

Proof of Theorem 1.1 When n = 1 n=1, a direct computation gives

 | I ⁡ ( h) = ξ 0, 1 ​ I 0, 1 ​ ( h) = − 2 ​ π ​ λ 1 − λ ​ h, I(h)=\xi_{0,1}I_{0,1}(h)=-\frac{2\pi\sqrt{\lambda}}{\sqrt{1-\lambda}}h, |  |

which yields that system (1.8) has no limit cycle. When n ≥ 2 n\geq 2, it follows from Proposition 2.1 that I ⁡ ( h) I(h) has at most n − 1 n-1 simple zeros. It is apparent that h, h 2, ⋯, h n h,h^{2},\cdots,h^{n} are linearly independent analytical functions and h h has constant sign in ( 0, + ∞) (0,+\infty). The existence of n − 1 n-1 simple zeros on ( 0, + ∞) (0,+\infty) for I ⁡ ( h) I(h) can be guaranteed by an appropriate choice of the parameters α 1 \alpha_{1}, α 2 \alpha_{2}, ⋯ \cdots, α n − 1, α n \alpha_{n-1},\alpha_{n}, as indicated by Lemma 3.1. This completes the proof of Theorem 1.1. ◊ \lozenge

Next, we will provide corresponding numerical simulations for concrete values of n n and λ \lambda to verify the theoretical result. When n = 2 n=2, it follows from Proposition 2.1 and (2.31) that I ⁡ ( h) I(h) possesses a simple zero ( 1 − λ) ​ ξ 0, 1 λ ​ ξ 0, 2 \frac{(1-\lambda)\xi_{0,1}}{\lambda\xi_{0,2}} in ( 0, 1) (0,1). Taking ξ 0, 1 = 1, ξ 0, 2 = 3 \xi_{0,1}=1,\xi_{0,2}=3 and λ = 1 2 \lambda=\frac{1}{2} yields that I ⁡ ( h) I(h) has a zero 1 3 \frac{1}{3}. That is, we can find a differential system

When n = 3 n=3, according to (2.32), we take α 1 = π, α 2 = − 5 ​ π, α 3 = 6 ​ π \alpha_{1}=\pi,\alpha_{2}=-5\pi,\alpha_{3}=6\pi and λ = 1 2 \lambda=\frac{1}{2}, then I ⁡ ( h) I(h) has two positive zeros 1 2 \frac{1}{2} and 1 3 \frac{1}{3}. Based on the previous analysis, one can find a system

When n = 4 n=4, following an analogous approach to the preceding analysis, one has

 | I ⁡ ( h) = α 1 ​ h + α 2 ​ h 2 + α 3 ​ h 3 + α 4 ​ h 4, \displaystyle I(h)=\alpha_{1}h+\alpha_{2}h^{2}+\alpha_{3}h^{3}+\alpha_{4}h^{4}, |  |

where

 |  | α 1 = − 2 ​ π ​ λ 1 − λ ξ 0, 1, α 4 = 5 ​ π ​ λ 7 2 ( 1 − λ) 7 2 ξ 0, 4, \displaystyle\alpha_{1}=-\frac{2\pi\sqrt{\lambda}}{\sqrt{1-\lambda}}\xi_{0,1},\ \alpha_{4}=\frac{5\pi\lambda^{\frac{7}{2}}}{(1-\lambda)^{\frac{7}{2}}}\xi_{0,4}, |  |

 |  | α 2 = 2 ​ π ​ λ 3 2 ( 1 − λ) 3 2 ​ ξ 0, 2 − 3 ​ π ​ λ 3 2 ​ ( λ − 1) ( 1 − λ) 5 2 ​ ξ 0, 3 + 2 ​ π ​ λ 3 2 ( 1 − λ) 3 2 ​ ξ 1, 2 − π ​ λ ( 1 − λ) 3 2 ​ ξ 2, 1 \displaystyle\alpha_{2}=\frac{2\pi\lambda^{\frac{3}{2}}}{(1-\lambda)^{\frac{3}{2}}}\xi_{0,2}-\frac{3\pi\lambda^{\frac{3}{2}}(\lambda-1)}{(1-\lambda)^{\frac{5}{2}}}\xi_{0,3}+\frac{2\pi\lambda^{\frac{3}{2}}}{(1-\lambda)^{\frac{3}{2}}}\xi_{1,2}-\frac{\pi\sqrt{\lambda}}{(1-\lambda)^{\frac{3}{2}}}\xi_{2,1} |  |

 |  | α 3 = − 3 ​ π ​ λ 5 2 ( 1 − λ) 5 2 ​ ξ 0, 3 − 4 ​ π ​ λ 5 2 ​ ( 2 ​ λ 2 − λ − 1) ( 1 − λ) 7 2 ​ ξ 0, 4 − 6 ​ π ​ λ 5 2 ( 1 − λ) 5 2 ​ ξ 1, 3 + 2 ​ π ​ λ 3 2 ( 1 − λ) 5 2 ​ ξ 2, 2. \displaystyle\alpha_{3}=-\frac{3\pi\lambda^{\frac{5}{2}}}{(1-\lambda)^{\frac{5}{2}}}\xi_{0,3}-\frac{4\pi\lambda^{\frac{5}{2}}(2\lambda^{2}-\lambda-1)}{(1-\lambda)^{\frac{7}{2}}}\xi_{0,4}-\frac{6\pi\lambda^{\frac{5}{2}}}{(1-\lambda)^{\frac{5}{2}}}\xi_{1,3}+\frac{2\pi\lambda^{\frac{3}{2}}}{(1-\lambda)^{\frac{5}{2}}}\xi_{2,2}. |  |

Taking α 1 = − 4 ​ π, α 2 = 55 ​ π, α 3 = − 325 2 ​ π, α 4 = 125 ​ π \alpha_{1}=-4\pi,\alpha_{2}=55\pi,\alpha_{3}=-\frac{325}{2}\pi,\alpha_{4}=125\pi and λ = 1 2 \lambda=\frac{1}{2}, then I ⁡ ( h) I(h) has three positive zeros 1 10, 2 5 \frac{1}{10},\frac{2}{5} and 4 5 \frac{4}{5}. Depending on the values of α i ​ ( i = 1, 2, 3, 4) \alpha_{i}(i=1,2,3,4), we can identify a system

 | { d ​ x d ​ t = − 2 ​ y − x − x 2, d ​ y d ​ t = x + y + 2 ​ x ​ y + 3 2 ​ x 2 + x 3 + ε ⁡ ( 2 ​ y + 15 2 ​ x ​ y 2 − 20 ​ x 2 ​ y − 245 8 ​ x 2 ​ y 2 + 40 ​ x ​ y 3 + 25 ​ y 4) \displaystyle\begin{cases}\frac{dx}{dt}=-2y-x-x^{2},\\ \frac{dy}{dt}=x+y+2xy+\frac{3}{2}x^{2}+x^{3}+\varepsilon(2y+\frac{15}{2}xy^{2}-20x^{2}y-\frac{245}{8}x^{2}y^{2}+40xy^{3}+25y^{4})\end{cases} |  | (3.1) |

with three limit cycles, as illustrated in Fig. 4. with ε = 10 − 4 \varepsilon=10^{-4}.

## 4 Discussion

After more than a decade of relentless efforts by numerous scholars, the weak Hilbert’s 16th problem has been completely resolved for the case where the Hamiltonian function H ⁡ ( x, y) H(x,y) has degree deg ⁡ H ⁡ ( x, y) = 3 \deg H(x,y)=3 and the perturbation polynomials satisfy deg ⁡ f ⁡ ( x, y) = deg ⁡ g ⁡ ( x, y) = 2 \deg f(x,y)=\deg g(x,y)=2. This stands as one of the few comprehensive results achieved in this field of research. Bearing this in mind, this paper focuses on the weak Hilbert’s 16th problem for a class of cubic isochronous Hamiltonian systems, where the Hamiltonian function is

 | H ⁡ ( x, y) = 1 2 ​ x 2 + λ ​ x 3 + 1 2 ​ λ ​ x 4 + 1 2 ​ λ − 1 ​ y 2 + x ​ y + x 2 ​ y. \displaystyle H(x,y)=\frac{1}{2}x^{2}+\lambda x^{3}+\frac{1}{2}\lambda x^{4}+\frac{1}{2}\lambda^{-1}y^{2}+xy+x^{2}y. |  |

Under n n -th degree polynomial perturbations, the exact number of limit cycles is derived.

Unlike previous studies, some terms I i, j ​ ( h) I_{i,j}(h) appearing in the Abelian integral I ⁡ ( h) I(h) of this system cannot be iterated using the derived recurrence formulas. As a result, the number of generators of I ⁡ ( h) I(h) depends on the degree n n of the perturbation terms. To overcome this difficulty, we identify the differential equations satisfied by these non-iterable terms and obtain their explicit expressions by solving these differential equations. Another key difficulty lies in verifying the linear independence of coefficients in the expression of I ⁡ ( h) I(h) when investigating the lower bound for the number of limit cycles. This obstacle was resolved through mathematical induction. The results presented in this work constitute a meaningful advancement in addressing the weak Hilbert’s 16th problem on cubic isochronous Hamiltonian systems. Investigating the weak Hilbert’s 16th problem for other types of cubic systems will be an important focus of our future research.

Acknowledgment

This work was supported by the National Natural Science Foundation of China (12161069).

Author Contributions

Jihua Yang: Conceptualization, Funding acquisition, Investigation, Methodology, Project administration, Resources, Supervision, Writing-original draft, Writing-review & \& editing.

Conflict of interest

The authors declare that they have no known competing financial interests or personal relationships that could have appeared to influence the work reported in this paper.

Data availability statement

No data was used for the research in this article. It is pure mathematics.

## References

- [1] V. I. Arnold, Ten problems in theory of singularities and its applications, Adv. Soviet Math. 1 (1990) 1–8.
- [2] S. Banerjee, G. Verghese, Nonlinear Phenomena in Power Electronics: Attractors, Bifurcations, Chaos, and Nonlinear Control, Wiley-IEEE Press, New York, 2001.
- [3] G. Binyamini, D. Novikov, S. Yakovenko, On the number of zeros of Abelian integrals: A constructive solution of the infinitesimal Hilbert 16th problem, Invent. Math. 181 (2010) 227–289.
- [4] Y. Chang, L. Zhao, Q. Wang, The Poincaré bifurcation by perturbing a class of cubic Hamiltonian systems, Nonlinear Anal. RWA 82 (2025) 104246.
- [5] H. Chen, S. Duan, Y. Tang, J. Xie, Global dynamics of a mechanical system with dry friction, J. Differ. Equations 265 (2018) 5490–5519.
- [6] H. Chen, L. Zou, Global study of Rayleigh-Duffing oscillators, J. Phys. A 49 (2016) 165202.
- [7] Y. Chen, J. Yu, The study on cyclicity of a class of cubic systems, Discrete Contin. Dyn. Syst. Ser. B, 27(11) (2022) 6233–6256.
- [8] Y. Chen, J. Yu, C. Sun, Stability and Hopf bifurcation analysis in a three-level food chain system with delay, Chaos Solitons Fractals 31 (2007) 683–694.
- [9] A. Cima, F. Mañosas, J. Villadelprat, Isochronicity for several classes of Hamiltonian systems, J. Differ. Equations 157 (1999) 373–413.
- [10] B. Coll, A. Gasull, R. Prohens, Bifurcation of limit cycles from two families of ceters, Dyn. Contin. Discrete Implus, Syst. Ser. A 12 (2005) 275–287.
- [11] C. B. Collins, Static stars: Some mathematical curiosities, J. Math. Phys. 18 (1977) 1374–1377.
- [12] F. Dumortier, C. Li, Perturbations from an elliptic Hamiltonian of degree four: (I) saddle loop and two saddle cycle, J. Diff. Equations 176 (2001) 114–157.
- [13] F. Dumortier, C. Li, Perturbations from an elliptic Hamiltonian of degree four: (II) cuspidal loop, J. Diff. Equations 175 (2001) 209–243.
- [14] F. Dumortier, C. Li, Perturbations from an elliptic Hamiltonian of degree four: (III) global cernter, J. Diff. Equations 188 (2003) 473–511.
- [15] F. Dumortier, C. Li, Perturbations from an elliptic Hamiltonian of degree four: (IV) figure-eight loop, J. Diff. Equations 188 (2001) 512–554.
- [16] L. Gavrilov, The infinitesimal 16th Hilbert problem in the quadratic case, Invent. Math. 143 (2001) 449–497.
- [17] J. Guckenheimer, P. Holmes, Nonlinear Oscillations, Dynamical Systems, and Bifurcations of Vector Fields, Applied Mathematical Sciences, 42. Springer-Verlag, New York, 1983.
- [18] M. Han, Bifurcation Theory of Limit Cycles, Science Press, Beijing, 2013.
- [19] M. Han, J. Li, Lower bounds for the Hilbert number of polynomial systems, J. Differ. Equations, 252 (2012) 3278–3304.
- [20] D. Hilbert, Mathematical problems, Bull. Amer. Math. Soc. 8 (1902) 437–479; Reprinted in: Bull. Amer. Math. Soc. (N.S.) 37 (2000) 407–436.
- [21] E. Horozov, Versal deformations of equivalent vector fields in the case of symmetry of order 2 and 3, Trudy Sem. 5 (1979) 163–192.
- [22] E. Horozov, I. Iliev, On the number of limit cycles in perturbations of quadratic Hamiltonian systems, Proc. Lond. Math. Soc. 69 (1994) 198–224
- [23] E. Horozov, I. Iliev, Linear estimate for the number of zeros of Abelian integrals with cubic Hamiltonians, Nonlinearity 11 (1998) 1521–1537.
- [24] I. Iliev, Perturbations of quadratic centers, Bull. Sci. math. 22 (1998) 107–161.
- [25] Yu. Ilyashenko, Centennial history of Hilbert’s 16th problem, Bull. Amer. Math. Soc. (N.S.) 39 (2002) 301–354.
- [26] Yu. Ilyashenko, S. Yakovenko, Double exponential estimate for the number of zeros of complete Abelian integrals, Invent. Math. 121 (1995) 613–650.
- [27] A. Khovanskii, Real analytic manifolds with the property of finiteness, and complex Abelian integrals, Functional Anal. Appl. 18(2) (1984) 40–50.
- [28] C. Li, C. Liu, J. Yang, A cubic system with thirteen limit cycles, J. Differ. Equations 246 (2009) 3609–3619.
- [29] C. Li, Z. Ma, Y. Zhou, Periodic orbits in 3-dimensional systems and application to a perturbed Volterra system, J. Differ. Equations 260 (2016) 2750–2762.
- [30] C. Li, Z. Zhang, Remarks on 16th weak Hilbert problem for n = 2 n=2, Nonlinearity 15 (2002) 1975–1992.
- [31] J. Li, Hilbert’s 16th problem and bifurcations of planar vector fields, Internat. J. Bifur. Chaos, 13 (2003) 47–106.
- [32] Y. Liu, J. Li, Z 2 Z_{2} -equivariant cubic system which yields 13 limit cycles, Acta Mathematicae Applicatae Sinica, English Series 30(3) (2014) 781–800.
- [33] C. Li, On Hilbet’s 16th Problem, Math. Theory Appl., 45(2) (2025) 1–21. (In Chinese)
- [34] C. Liu, Estimate of the number of zeros of Abelian integrals for an elliptic Hamiltonian with figure-of-eight loop, Nonlinearity 16 (2003) 1151–1163.
- [35] Y. Markov, Limit cycles of perturbations of a class of quadratic Hamiltonian vector fields, Serdica Math. J. 22(2) (1996) 91–108.
- [36] L. Pontryagin, On dynamic systems close to Hamiltonian systems, Zh. Eksp. Teor. Fiz. 4 (1934) 234–238.
- [37] T. Puu, Attractors, Bifurcations and Chaos Nonlinear Phenomena in Economics, Springer-Verlag, Berlin, 2000.
- [38] R. Roussarie, On the number of limit cycles which appear by perturbation of separatrix loop of planar vector fields, Bol. Soc. Bras. Math. 17(2) (1986) 67–101.
- [39] A. Varchenko, Estimation of the number of zeros of an Abelian integral depending on a parameter, and limit cycles, Functional Anal. Appl. 18(2) (1984) 14–25.
- [40] S. Wang, X. Wang, X. Wu, Bifurcation analysis for a food chain model with nonmonotonic nutrition conversion rate of predator to top predator, Internat. J. Bifur. Chaos 30 (2020) 2050113.
- [41] J. Wu, Y. Zhang, C. Li, On the number of zeros of Abelian integrals for a kind of quartic hamiltonians, Appl. Math. Comput. 228 (2014) 329–335.
- [42] J. Yang, S. Sui, L. Zhao, On the number of zeros of Abelian integral for a class of cubic Hamilton systems with the phase portrait butterfly, Qual. Theory Dyn. Syst. 18 (2019) 947–967.
- [43] J. Yang, L. Zhao, The cyclicity of period annuli for a class of cubic Hamiltonian systems with nilpotent singular points, J. Differ. Equations 263 (2017) 5554–5581.
- [44] J. Yang, M. Han, J. Li and P. Yu, Existence conditions of thirteen limit cycles in a cubic system, Internat. J. Bifur. Chaos 20 (2010) 2569–2577.
- [45] Z. Zhang, C. Li, On the number of limit cycles of a class of quadratic Hamiltonian systems under quadratic perturbations, Adv. Math. 26 (1997) 445–460.
- [46] Y. Zhao, Z. Zhang, Linear estimate of the number of zeros of Abelian integrals for a kind of quartic Hamiltonians, J. Differ. Equations 155 (1999) 73–88.
- [47] X. Zhou, C. Li, Estimate of the number of zeros of Abelian integrals for a kind of quartic Hamiltonians with two centers, Appl. Math. Comput. 204 (2008) 202–209.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
