<!-- source: https://ar5iv.labs.arxiv.org/html/1804.09084 | converted from HTML -->

[1804.09084] A new explicit formula in the additive theory of primes with applications II. The exceptional set in Goldbach’s problem

# A new explicit formula in the additive theory of primes with applications II. The exceptional set in Goldbach’s problem Thanks: Supported by ERC-AdG. 321104 and National Research Development and Innovation Office, NKFIH, K 119528.

by Affiliation: János Pintz

Dedicated to the 60 th birthday of Sz. Gy. Révész

## 1 Introduction

The first non-trivial, although conditional, estimate for the exceptional set ( 𝒫 CLOSE (\mathcal{P} denotes the set of primes)

(1.1) |  | ℰ = { 2 ∣ n; n ≠ p + p ′, p, p ′ ∈ 𝒫 } \mathcal{E}=\{2\mid n;\ n\neq p+p^{\prime},\ p,p^{\prime}\in\mathcal{P}\} |  |

in Goldbach’s problem was achieved by Hardy and Littlewood [8] in 1924. They showed under the Generalized Riemann Hypothesis (GRH) the estimate

(1.2) |  | E ( X) = { n ≤ X; n ∈ ℰ } ≪ ε X 1 / 2 + ε E(X)=\{n\leq X;\ n\in\mathcal{E}\}\ll_{\varepsilon}X^{1/2+\varepsilon} |  |

for any ε > 0 \varepsilon>0. This result is apart from the substitution of X ε X^{\varepsilon} by log c ⁡ X \log^{c}X by Goldston [6] even today the best conditional result on GRH.

The basic result that almost all even integers are Goldbach numbers, that is, can be represented as the sum of two primes, was proved by the aid of Vinogradov’s method [21] in 1937/38 simultaneously and independently by Van der Corput [19], Čudakov [3] and Estermann [5]. They showed

(1.3) |  | E ( X) ≪ A X ( log ⁡ X) A for any A > 0. E(X)\ll_{A}\frac{X}{(\log X)^{A}}\quad\text{ for any }\ A>0. |  |

It is easy to see that ( 1.3), even any estimate of type

(1.4) |  | E ⁡ ( 2 ​ N) < π ⁡ ( 2 ​ N) − 1 for ​ N > N E(2N)<\pi(2N)-1\quad\text{ for }\ N>N |  |

implies Vinogradov’s three primes theorem [21] that every sufficiently large odd integer can be written as the sum of three primes.

The result ( 1.3) held the record for 35 years, when Vaughan [20] improved it in 1972 to

(1.5) |  | E ⁡ ( X) ≪ X ​ exp ⁡ ( − c ​ log ⁡ X). E(X)\ll X\exp\bigl(-c\sqrt{\log X}\bigr). |  |

The breakthrough came just 3 years later when Montgomery and Vaughan [16] showed that the estimate

(1.6) |  | E ( X) ≪ δ X 1 − δ E(X)\ll_{\delta}X^{1-\delta} |  |

holds with an unspecified but explicitly calculable value δ > 0 \delta>0.

The problem, to show ( 1.6) with a not too small explicit value of δ \delta turned out to be very difficult. It was shown in 1989 by J. R. Chen and M. Liu [1] that ( 1.6) holds with δ = 0.05 \delta=0.05, ten years later by H. Z. Li [12] that also δ = 0.079 \delta=0.079 is admissible. This was improved by him [13] to

(1.7) |  | E ⁡ ( X) < X 0.914 E(X)<X^{0.914} |  |

for any X > X 0 X>X_{0}, ineffective constant. Finally in 2010 Lu [14] succeeded to show

(1.8) |  | E ⁡ ( X) < X 0.879 E(X)<X^{0{.}879} |  |

for X > X 2 X>X_{2} ineffective constant.

The present work will be devoted to the proof of the following result.

###### Theorem 1.

There is an ineffective constant X 2 X_{2} such that for X > X 2 X>X_{2}

(1.9) |  | E ⁡ ( X) < X 0.72. E(X)<X^{0.72}. |  |

The seemingly moderate size of the present work is still misleading concerning the difficulties of the proof of Theorem 1. Namely, a crucial role will be played in the proof by the results of part I of this series ( [18]) which is again heavily based on the results of another preparatory work ( [17]). Finally we mention that apart from the relatively short final Section 9 all results of the present work (in many cases in a refined form) will be used in later parts of this series to achieve further improvements over ( 1.9).

## 2 Notation. The role of the explicit formula

The explicit formula proved in part I ( [18]) will play a central role in the proof of Theorem 1; in fact, it serves as the basis for any further examination. In order to formulate the explicit formula we first need to introduce the notation.

Let ε \varepsilon and ε 0 \varepsilon_{0} be small positive numbers, X X be a number large enough ( X > X 0 ​ ( ε, ε 0)) (X>X_{0}(\varepsilon,\varepsilon_{0})), and let us define

(2.1) |  | X 1:= X 1 − ε 0, e ⁡ ( u):= e 2 ​ π ​ i ​ u, S ⁡ ( α):= ∑ X 1 < p ≤ X log ⁡ p ​ e ​ ( p ​ α), X_{1}:=X^{1-\varepsilon_{0}},\quad e(u):=e^{2\pi iu},\quad S(\alpha):=\sum_{X_{1}<p\leq X}\log pe(p\alpha), |  |

where p p, p ′ p^{\prime}, p i p_{i} will always denote primes. | ℳ | |\mathcal{M}| will denote the cardinality of the finite set ℳ \mathcal{M}. We will define the major ( 𝔐 \mathfrak{M}) and minor ( 𝔪 \mathfrak{m}) arcs through the parameters P P and Q Q satisfying

(2.2) |  | ( log ⁡ X) C ≤ P ≤ X 4 / 9 − ε, Q = X P, (\log X)^{C}\leq P\leq X^{4/9-\varepsilon},\quad Q=\frac{X}{P}, |  |

(2.3) |  | 𝔐 = ⋃ q ≤ P ⋃ a ( a, q) = 1 [a q − 1 q ​ Q, a q + 1 q ​ Q], 𝔪 = [1 Q, 1 + 1 Q] ∖ 𝔐. \mathfrak{M}=\bigcup_{q\leq P}\bigcup_{\begin{subarray}{c}a\\ (a,q)=1\end{subarray}}\left[\frac{a}{q}-\frac{1}{qQ},\frac{a}{q}+\frac{1}{qQ}\right],\quad\mathfrak{m}=\left[\frac{1}{Q},1+\frac{1}{Q}\right]\setminus\mathfrak{M}. |  |

We will examine the number of Goldbach decompositions of even numbers m ∈ [X / 2, X] m\in[X/2,X] in the form

(2.4) |  | R ⁡ ( m) = ∑ p + p ′ = m p, p ′ ≥ X 1 log ⁡ p ⋅ log ⁡ p ′ = R 1 ​ ( m) + R 2 ​ ( m), R(m)=\sum_{\begin{subarray}{c}p+p^{\prime}=m\\ p,p^{\prime}\geq X_{1}\end{subarray}}\log p\cdot\log p^{\prime}=R_{1}(m)+R_{2}(m), |  |

where

(2.5) |  | R 1 ​ ( m) = ∫ 𝔐 S 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α, R 2 ​ ( m) = ∫ 𝔪 S 2 ​ ( α) ​ e ​ ( − m ​ α) ​ 𝑑 α. R_{1}(m)=\int\limits_{\mathfrak{M}}S^{2}(\alpha)e(-m\alpha)d\alpha,\qquad R_{2}(m)=\int\limits_{\mathfrak{m}}S^{2}(\alpha)e(-m\alpha)d\alpha. |  |

The now standard treatment of the minor arcs (Parseval’s theorem and the estimate of Vinogradov, reproved in a simpler way by Vaughan) gives

(2.6) |  | | R 2 ​ ( m) | ≤ X log ⁡ X for ​ P ≤ X 2 / 5 |R_{2}(m)|\leq\frac{X}{\sqrt{\log X}}\quad\text{ for }\ P\leq X^{2/5} |  |

apart from at most C ​ X P ​ log 10 ⁡ X C\frac{X}{P}\log^{10}X exceptional values m m (see Section 5 of [18], for example).

In order to formulate the explicit formula for the major arcs in Goldbach’s problem we will define the set ℰ = ℰ ⁡ ( H, P, T, X) \mathcal{E}=\mathcal{E}(H,P,T,X) of generalized exceptional singularities of the functions L ′ / L L^{\prime}/L for all primitive L L -functions mod ​ r \,\text{\rm mod}\;r, r ≤ P r\leq P, as follows ( χ 0 = χ 0 ​ ( mod ​ 1) \chi_{0}=\chi_{0}(\,\text{\rm mod}\;1) is considered as a primitive character mod ​ 1 \,\text{\rm mod}\;1)

(2.7) |  | ( ϱ 0, χ 0) \displaystyle(\varrho_{0},\chi_{0}) | ∈ ℰ if ​ ϱ 0 = 1, \displaystyle\in\mathcal{E}\quad\text{ if }\ \varrho_{0}=1, |  |

 | ( ϱ i, χ i) \displaystyle(\varrho_{i},\chi_{i}) | ∈ ℰ if ∃ χ i, cond χ i = r i ≤ P, L ( ϱ i, χ i) = 0, \displaystyle\in\mathcal{E}\quad\text{ if }\ \exists\chi_{i},\ \mathrm{cond}\,\chi_{i}=r_{i}\leq P,\ L(\varrho_{i},\chi_{i})=0, |  |

 | β i \displaystyle\beta_{i} | ≥ 1 − H log ⁡ X, | γ i | ≤ T, \displaystyle\geq 1-\frac{H}{\log X},\quad|\gamma_{i}|\leq T, |  |

where zeros of L L -functions are denoted by ϱ = β + i ​ γ = 1 − δ + i ​ γ \varrho=\beta+i\gamma=1-\delta+i\gamma and cond ​ χ \text{\rm cond}\,\chi denotes the conductor of χ \chi. Let further

(2.8) |  | A ⁡ ( ϱ) \displaystyle A(\varrho) | = 1 if ​ ϱ = 1, \displaystyle=1\phantom{-}\quad\text{ if }\ \varrho=1, |  |

 | A ⁡ ( ϱ) \displaystyle A(\varrho) | = − 1 if ​ ϱ ≠ 1. \displaystyle=-1\quad\text{ if }\ \varrho\neq 1. |  |

The expected main term of R 1 ​ ( m) R_{1}(m) is the well-known singular series of Hardy and Littlewood, arising from the effect of the pole of ζ ⁡ ( s) \zeta(s) at s = 1 s=1:

(2.9) |  | 𝔖 ⁡ ( m):= 𝔖 ⁡ ( χ 0, χ 0, m):= ∏ p | m ( 1 + 1 p − 1) ​ ∏ p ∤ m ( 1 − 1 ( p − 1) 2). {\mathfrak{S}}(m):={\mathfrak{S}}(\chi_{0},\chi_{0},m):=\prod_{p\mid m}\left(1+\frac{1}{p-1}\right)\prod_{p\nmid m}\left(1-\frac{1}{(p-1)^{2}}\right). |  |

However, if we have zeros near to s = 1 s=1 then we necessarily have a number of secondary terms with coefficients 𝔖 ⁡ ( χ i, χ j, m) {\mathfrak{S}}(\chi_{i},\chi_{j},m) corresponding to the primitive characters belonging to generalized exceptional zeros. We will call these characters generalized exceptional characters, the corresponding singular series 𝔖 ⁡ ( χ i, χ j, m) {\mathfrak{S}}(\chi_{i},\chi_{j},m) generalized exceptional singular series. They can be expressed in a very complicated explicit form, proven in the Main Lemma of part I ( [18]). However, the important properties of it can be incorporated into the following theorem, where we use the notation and conditions of the present section.

Theorem A (Explicit formula). Let 0 < ε < ε 0 0<\varepsilon<\varepsilon_{0}, ε < ϑ < 4 9 − ε \varepsilon<\vartheta<\frac{4}{9}-\varepsilon be any numbers, 2 | m ∈ [X 2, X] 2\mid m\in\left[\frac{X}{2},X\right]. Then there exists P ∈ ( X ϑ − ε, X ϑ) P\in(X^{\vartheta-\varepsilon},X^{\vartheta}) such that for X > X 0 ​ ( ε) X>X_{0}(\varepsilon)

(2.10) |  | R 1 ​ ( m) \displaystyle R_{1}(m) | = ∑ ϱ i ∈ ℰ ∑ ϱ j ∈ ℰ A ⁡ ( ϱ i) ​ A ​ ( ϱ j) ​ 𝔖 ​ ( χ i, χ j, m) ​ Γ ⁡ ( ϱ i) ​ Γ ​ ( ϱ j) Γ ⁡ ( ϱ i + ϱ j) ​ m ϱ i + ϱ j − 1 \displaystyle=\sum_{\varrho_{i}\in\mathcal{E}}\sum_{\varrho_{j}\in\mathcal{E}}A(\varrho_{i})A(\varrho_{j}){\mathfrak{S}}(\chi_{i},\chi_{j},m)\frac{\Gamma(\varrho_{i})\Gamma(\varrho_{j})}{\Gamma(\varrho_{i}+\varrho_{j})}m^{\varrho_{i}+\varrho_{j}-1} |  |

 |  | + O ⁡ ( X ​ e − c ​ H + X T + X 1 − ε), \displaystyle\quad+O\left(Xe^{-cH}+\frac{X}{\sqrt{T}}+X^{1-\varepsilon}\right), |  |

where the generalized singular series satisfy

(2.11) |  | | 𝔖 ⁡ ( χ i, χ j, m) | ≤ 𝔖 ⁡ ( χ 0, χ 0, m) = 𝔖 ⁡ ( m); |{\mathfrak{S}}(\chi_{i},\chi_{j},m)|\leq{\mathfrak{S}}(\chi_{0},\chi_{0},m)={\mathfrak{S}}(m); |  |

further for any η \eta small enough

(2.12) |  | | 𝔖 ⁡ ( χ i, χ j, m) | ≤ η, |{\mathfrak{S}}(\chi_{i},\chi_{j},m)|\leq\eta, |  |

unless the following three conditions all hold,

(2.13) |  | r i | C ⁡ ( η) ​ m, r j | C ⁡ ( η) ​ m, cond ​ χ i ​ χ j < η − 3 r_{i}|C(\eta)m,\ r_{j}|C(\eta)m,\ \ \text{\rm cond}\,\chi_{i}\chi_{j}<\eta^{-3} |  |

where C ⁡ ( η) C(\eta) is a suitable constant depending only on η \eta.

Its proof follows from Theorem 1 and Main Lemma 1 in part I [18].

Remark. A very important feature of the explicit formula is that the number K K of generalized exceptional zeros appearing in ( 2.10) is by log-free zero density theorems (cf. Jutila [10]) bounded from above by

(2.14) |  | K ≤ C ​ e 2 ​ H, K\leq Ce^{2H}, |  |

so it is bounded by an absolute constant (depending on ε \varepsilon), if we choose H H as a sufficiently large absolute constant depending on ε \varepsilon, which we suppose later on in the proof of Theorem 1. Similarly, we will choose T T as a sufficiently large constant depending on ε \varepsilon.

Although the quoted explicit formula is in general a good starting point for the proof of

(2.15) |  | R 1 ​ ( m) > ε ​ 𝔖 ​ ( m) ​ m R_{1}(m)>\varepsilon{\mathfrak{S}}(m)m |  |

if ϑ \vartheta is small enough, the argument breaks down in case of the existence of a Siegel-zero, 1 − δ 1-\delta corresponding to L ⁡ ( s, χ 1) L(s,\chi_{1}), in which case we might have 𝔖 ⁡ ( χ 1, χ 1, m) = − 𝔖 ⁡ ( m) {\mathfrak{S}}(\chi_{1},\chi_{1},m)=-{\mathfrak{S}}(m) and we cannot show the crucial relation ( 2.15) if δ \delta is small enough. In this case the Deuring–Heilbronn phenomenon can help. This case was worked out as Theorem 2 in part I [18] which we quote now as

Theorem B. Let ε ′ > 0 \varepsilon^{\prime}>0 be arbitrary. If X > X ⁡ ( ε ′) X>X(\varepsilon^{\prime}), ineffective constant and there exists a Siegel zero β 1 \beta_{1} of L ⁡ ( s, χ 1) L(s,\chi_{1}) with

(2.16) |  | β 1 > 1 − h / log ⁡ X, cond ​ χ 1 ≤ X 4 9 − ε ′, \beta_{1}>1-h/\log X,\ \ \text{\rm cond}\,\chi_{1}\leq X^{\frac{4}{9}-\varepsilon^{\prime}}, |  |

where h h is a sufficiently small constant depending on ε ′ \varepsilon^{\prime}, then

(2.17) |  | E ⁡ ( X) < X 3 5 + ε ′. E(X)<X^{\frac{3}{5}+\varepsilon^{\prime}}. |  |

Remark. We will choose ε ′ = 10 − 3 \varepsilon^{\prime}=10^{-3} here. Then in the proof of Theorem 1 we are entitled to suppose that all L ⁡ ( s, χ) L(s,\chi) functions mod ​ r ≤ P \,\text{\rm mod}\;r\leq P satisfy

(2.18) |  | L ⁡ ( s, χ) ≠ 0 for ​ s ∈ [1 − c 0 / log ⁡ X, 1] L(s,\chi)\neq 0\quad\text{ for }\ s\in[1-c_{0}/\log X,\ 1] |  |

if we choose ϑ ≤ 0.44 \vartheta\leq 0.44. In other words, we do not need to worry about exceptional zeros 1 − δ 1-\delta satisfying δ < c 0 / log ⁡ X \delta<c_{0}/\log X with a small but fixed c 0 > 0 c_{0}>0.

The well-known relation (cf. [11], p. 46) ( Re ​ w, Re ​ z > 0) (\mathrm{Re}\,w,\mathrm{Re}\,z>0)

(2.19) |  | Γ ⁡ ( w) ​ Γ ​ ( z) Γ ⁡ ( w + z) = B ⁡ ( w, z) = ∫ 0 1 x w − 1 ​ ( 1 − x) z − 1 ​ 𝑑 x \frac{\Gamma(w)\Gamma(z)}{\Gamma(w+z)}=B(w,z)=\int\limits^{1}_{0}x^{w-1}(1-x)^{z-1}dx |  |

tells us that

(2.20) |  | | B ⁡ ( ϱ i, ϱ j) | ≤ | B ⁡ ( Re ​ ϱ i, Re ​ ϱ j) | = B ⁡ ( 1, 1) + O ⁡ ( 1 / log ⁡ X) = 1 + O ⁡ ( 1 / log ⁡ X). |B(\varrho_{i},\varrho_{j})|\leq|B(\mathrm{Re}\,\varrho_{i},\mathrm{Re}\,\varrho_{j})|=B(1,1)+O(1/\log X)=1+O(1/\log X). |  |

Hence, taking into account the relations ( 2.11)–( 2.13) we see that the estimation ( 2.15) will follow, if we can show

(2.21) |  | ∑ ∗ ϱ i, ϱ j ∈ ℰ ( ϱ i, ϱ j) ≠ ( 1, 1) ​ X − δ i − δ j < 1 − 2 ​ ε, \underset{\begin{subarray}{c}\varrho_{i},\varrho_{j}\in\mathcal{E}\\ (\varrho_{i},\varrho_{j})\neq(1,1)\end{subarray}}{\sum\nolimits^{*}}X^{-\delta_{i}-\delta_{j}}<1-2\varepsilon, |  |

where the ∗ *means that the additional condition ( 2.13) is satisfied for the pairs ( ϱ i, ϱ j) (\varrho_{i},\varrho_{j}) of zeros in the summation.

The expression ( 2.21) can be estimated directly by density theorems and the Deuring–Heilbronn phenomenon, as done in the earlier estimates of Chen-Liu [1] and Hongze Li [12], [13], and Lu [14]. It also resembles the well-studied problem of the Linnik-constant, with the seemingly major disadvantage that

 | the zeros do not belong to a fixed modulus ​ q ≤ P \text{the zeros do not belong to a fixed modulus }q\leq P |  |

but to a set of different moduli r i ≤ P r_{i}\leq P.

In what follows below, we will show that this disadvantage can be overwhelmed thanks to the information ( 2.13) supplied by the explicit formula.

We will choose P 0 = X ϑ + 2 ​ ε P_{0}=X^{\vartheta+2\varepsilon}, so our P P will satisfy

(2.22) |  | P ∈ [X ϑ + ε, X ϑ + 2 ​ ε]. P\in\Bigl[X^{\vartheta+\varepsilon},X^{\vartheta+2\varepsilon}\Bigr]. |  |

Thus the exceptional set arising from the minor arcs ( 2.6) will be o ⁡ ( X 1 − ϑ) o(X^{1-\vartheta}). Then we consider the set ℛ {\mathcal{R}} of the K K generalized exceptional zeros appearing in ( 2.10) whose number K K is bounded by an absolute constant depending on ε \varepsilon,

(2.23) |  | 0 ≤ K ≤ K ⁡ ( ε) − 1 0\leq K\leq K(\varepsilon)-1 |  |

according to ( 2.14) since we will choose H H as a big constant depending on ε \varepsilon. (If K = 0 K=0 we are ready.)

Let us choose now

(2.24) |  | η = ε K 2 ​ ( ε), \eta=\frac{\varepsilon}{K^{2}(\varepsilon)}, |  |

and write

(2.25) |  | C ​ ( η) = C 1 ​ ( ε). C(\eta)=C_{1}(\varepsilon). |  |

In this case the total contribution of terms not satisfying ( 2.13) will be really less than ε ​ X \varepsilon X in ( 2.10), so ( 2.21) will really imply ( 2.15). Let us divide now the even numbers m m in [X / 2, X] [X/2,X] into at most 2 | ℛ | 2^{|{\mathcal{R}}|} different classes ℳ ⁡ ( ℛ ′) \mathcal{M}({\mathcal{R}}^{\prime}) according to the subset ℛ ′ ⊂ ℛ {\mathcal{R}}^{\prime}\subset{\mathcal{R}} of zeros which belong to primitive characters with moduli dividing C 1 ​ ( ε) ​ m C_{1}(\varepsilon)m

(2.26) |  | ℳ ( ℛ ′) = { m ∈ [X / 2, X], 2 ∣ m, r i ∣ C 1 ( ε) m ⇔ r i ∈ ℛ ′ }. \mathcal{M}({\mathcal{R}}^{\prime})=\bigl\{m\in[X/2,X],\ 2\mid m,\ r_{i}\mid C_{1}(\varepsilon)m\Leftrightarrow r_{i}\in{\mathcal{R}}^{\prime}\bigr\}. |  |

(The subset might be empty for some ℛ ′ ⊂ ℛ {\mathcal{R}}^{\prime}\subset{\mathcal{R}}; for example, if ϱ i ∈ ℛ ′ \varrho_{i}\in{\mathcal{R}}^{\prime}, ϱ j ∉ ℛ ′ \varrho_{j}\notin{\mathcal{R}}^{\prime}, r i = r j r_{i}=r_{j}, or if l. c. m. r i ∈ ℛ ′ ​ [r i] > X ​ C 1 ​ ( ε) \underset{r_{i}\in{\mathcal{R}}^{\prime}}{\mathrm{l.c.m.}}[r_{i}]>XC_{1}(\varepsilon).)

Let us denote

(2.27) |  | q ⁡ ( ℛ ′):= l. c. m. [r i; r i ∈ ℛ ′]. q({\mathcal{R}}^{\prime}):=\mathrm{l.c.m.}[r_{i};\ r_{i}\in{\mathcal{R}}^{\prime}]. |  |

Now we can delete all classes ℳ ⁡ ( ℛ ′) \mathcal{M}({\mathcal{R}}^{\prime}) with

(2.28) |  | q ⁡ ( ℛ ′) > X ϑ, q({\mathcal{R}}^{\prime})>X^{\vartheta}, |  |

since in this case clearly

(2.29) |  | | ℳ ⁡ ( ℛ ′) | ≤ C 1 ​ ( ε) ​ X 1 − ϑ, |\mathcal{M}({\mathcal{R}}^{\prime})|\leq C_{1}(\varepsilon)X^{1-\vartheta}, |  |

and the number of all classes is

(2.30) |  | 2 | ℛ | ≤ 2 K ⁡ ( ε) = C 2 ​ ( ε). 2^{|{\mathcal{R}}|}\leq 2^{K(\varepsilon)}=C_{2}(\varepsilon). |  |

Let us fix now any concrete class ℛ ′ {\mathcal{R}}^{\prime} with

(2.31) |  | q:= q ⁡ ( ℛ ′) ≤ X ϑ. q:=q({\mathcal{R}}^{\prime})\leq X^{\vartheta}. |  |

Due to ( 2.30) it is sufficient to restrict our attention now for values m m with

(2.32) |  | m ∈ ℳ ⁡ ( ℛ ′). m\in\mathcal{M}({\mathcal{R}}^{\prime}). |  |

Hence, by ( 2.21) it is sufficient to show for any q ≤ X ϑ q\leq X^{\vartheta}

(2.33) |  | S 0 = ∑ ∗ ⁣ ∗ ϱ i, ϱ j ∈ ℰ ( ϱ i, ϱ j) ≠ ( 0, 0) ​ q − A ⁡ ( δ i + δ j) < 1 − 2 ​ ε S_{0}=\underset{\begin{subarray}{c}\varrho_{i},\varrho_{j}\in\mathcal{E}\\ (\varrho_{i},\varrho_{j})\neq(0,0)\end{subarray}}{\sum\nolimits^{**}}q^{-A(\delta_{i}+\delta_{j})}<1-2\varepsilon |  |

where A = 1 / ϑ A=1/\vartheta and the notation ∗ ⁣ ∗ **abbreviates now the condition

(2.34) |  | r i | q, r j | q, cond ​ ( χ i ​ χ j) < C 0 ​ ( ε) ( = ε 3 K 6 ​ ( ε)). r_{i}\mid q,\ r_{j}\mid q,\ \ \text{\rm cond}\,(\chi_{i}\chi_{j})<C_{0}(\varepsilon)\ \left(=\frac{\varepsilon^{3}}{K^{6}(\varepsilon)}\right). |  |

Thus we managed to get rid of the condition ( †) (\dagger), and it is sufficient to consider characters modulo the same q ≤ X ϑ q\leq X^{\vartheta}. Further advantages compared to the earlier treatments ( [1], [12], [13], [14]) are that

(i) both zeros ϱ i \varrho_{i} and ϱ j \varrho_{j} run only through zeros with a bounded height | γ | ≤ T ⁡ ( ε) |\gamma|\leq T(\varepsilon) and

(ii) the second zero ϱ j \varrho_{j} runs for every fixed ϱ i \varrho_{i} only through zeros belonging to characters χ j \chi_{j} with

(2.35) |  | cond ​ ( χ i ​ χ j) < C 0 ​ ( ε). \text{\rm cond}\,(\chi_{i}\chi_{j})<C_{0}(\varepsilon). |  |

Since zeros of L ⁡ ( s, χ) L(s,\chi) and L ⁡ ( s, χ ¯) L(s,\overline{\chi}) are conjugate it will be simpler for us to change the condition ( 2.35) to consider further on the inequality

(2.36) |  | S 0 = ∑ ′ q − A ⁡ ( δ i + δ j) < 1 − 2 ​ ε S_{0}=\sum\nolimits^{\prime}q^{-A(\delta_{i}+\delta_{j})}<1-2\varepsilon |  |

where the condition ∑ ′ \sum^{\prime} will mean later on

(2.37) |  | ( 1, 1) ≠ ( ϱ i, ϱ j) ∈ ℰ, r i ∣ q, r j ∣ q, cond ( χ i χ ¯ j) < C 0 ( ε). (1,1)\neq(\varrho_{i},\varrho_{j})\in\mathcal{E},\quad r_{i}\mid q,\ r_{j}\mid q,\ \ \text{\rm cond}\,(\chi_{i}\overline{\chi}_{j})<C_{0}(\varepsilon). |  |

This form makes the quasi-diagonal form of S 0 S_{0} clear: only those pairs of zeros count where the relevant primitive characters are the same up to a character with a bounded conductor.

Let us use further on the notation (this will change the values of H H and T T by a factor A A)

(2.38) |  | log ⁡ q = ℒ, λ i = δ i ​ ℒ ≤ H, | μ i | = | γ i ​ ℒ | ≤ T. \log q=\mathcal{L},\quad\lambda_{i}=\delta_{i}\mathcal{L}\leq H,\quad|\mu_{i}|=|\gamma_{i}\mathcal{L}|\leq T. |  |

Then we can rewrite S 0 S_{0} as

(2.39) |  | S 0 = ∑ ′ e − A ⁡ ( λ i + λ j). S_{0}=\sum\nolimits^{\prime}e^{-A(\lambda_{i}+\lambda_{j})}. |  |

According to ( 2.37) we will say that two generalized exceptional characters χ \chi and χ ′ \chi^{\prime} are equivalent, in notation χ ∼ χ ′ \chi\sim\chi^{\prime} if there is a chain of generalized exceptional characters χ ν \chi_{\nu} ( ν = 1, 2, …, n) (\nu=1,2,\dots,n) such that χ 1 = χ \chi_{1}=\chi, χ n = χ ′ \chi_{n}=\chi^{\prime}

(2.40) |  | cond ​ ( χ ν ​ χ ν + 1 ¯) < C 0 ​ ( ε) for ​ ν = 1, …, n − 1. \text{\rm cond}\,(\chi_{\nu}\overline{\chi_{\nu+1}})<C_{0}(\varepsilon)\quad\text{ for }\ \nu=1,\dots,n-1. |  |

Such a chain has at most K ≤ K ⁡ ( ε) K\leq K(\varepsilon) characters in it; hence if χ \chi and χ ′ \chi^{\prime} are equivalent, then

(2.41) |  | cond ​ ( χ, χ ¯ ′) < C 3 ​ ( ε) = C 0 ​ ( ε) K ⁡ ( ε) − 1. \text{\rm cond}\,(\chi,\overline{\chi}^{\prime})<C_{3}(\varepsilon)=C_{0}(\varepsilon)^{K(\varepsilon)-1}. |  |

We remark here that since by Davenport [4], Ch. 14

(2.42) |  | δ ≫ 1 q ​ log 2 ​ q, \delta\gg\frac{1}{\sqrt{q}\log^{2}q}, |  |

there is no generalized exceptional character χ ∼ χ 0 ​ ( mod ​ 1) \chi\sim\chi_{0}(\,\text{\rm mod}\;1), so the sum S 0 S_{0} in ( 2.39) in fact does not contain any pair of singularities ( 1, ϱ) (1,\varrho), just pairs of zeros. In such a way we can distribute the generalized exceptional zeros into M M ( ≤ K) (\leq K) classes according to the equivalence classes ℋ ν \mathcal{H}_{\nu} ( ν = 1, 2, … ​ M) (\nu=1,2,\dots M) of the generalized exceptional characters. Thus we obtain

(2.43) |  | S 0 ≤ S:= ∑ ν = 1 M S ν 2, S_{0}\leq S:=\sum^{M}_{\nu=1}S^{2}_{\nu}, |  |

where S ν S_{\nu} denotes the quantity

(2.44) |  | S ν:= ∑ ϱ ν, j ∈ ℰ, χ ν, j ∈ ℋ ν e − A ​ λ ν, j. S_{\nu}:=\sum_{\varrho_{\nu,j}\in\mathcal{E},\ \chi_{\nu,j}\in\mathcal{H}_{\nu}}e^{-A\lambda_{\nu,j}}. |  |

According to this it will be important to introduce (and later estimate) the quantities

(2.45) |  | N ⁡ ( Λ) = ∑ ϱ i ∈ ℰ, λ ≤ Λ 1 N(\Lambda)=\sum_{\varrho_{i}\in\mathcal{E},\ \lambda\leq\Lambda}1 |  |

and

(2.46) |  | N ν ​ ( Λ) = ∑ χ ∈ ℋ ν, λ = λ χ ≤ Λ 1, N ~ ​ ( Λ) = max ν ⁡ N ν ​ ( Λ). N_{\nu}(\Lambda)=\sum_{\chi\in{\mathcal{H}}_{\nu},\ \lambda=\lambda_{\chi}\leq\Lambda}1,\ \ \ \ \widetilde{N}(\Lambda)=\max_{\nu}N_{\nu}(\Lambda). |  |

## 3 Methods

The reduction to zeros corresponding to characters modulo a fixed q ≤ P q\leq P, the fact that it is sufficient to consider zeros with bounded height and the quasi-diagonal form ( 2.37) of the critical sum ( 2.33) are all new features compared with the earlier methods applied to the exceptional set in the previous works (cf. [1], [12], [13], [14]). A further advantage is that ( 2.33) shows now strong similarities to the case of the estimation of Linnik’s constant; in fact, it looks like a “two-dimensional” variant of Linnik’s problem. This gives hope to apply the very powerful methods and/or results of Heath-Brown [9] used by him to achieve the huge improvement L ≤ 5.5 L\leq 5.5 in the estimation of Linnik’s constant compared to the earlier result L = 13.5 L=13.5 of Chen and Liu [2].

The estimation of ( 2.33) will be based on the following three principles, mentioned and used by Heath-Brown [9].

Principle 1. Zero-free region for ∏ χ ⁡ ( mod ​ q) L ⁡ ( s, χ) \prod\limits_{\chi(\,\text{\rm mod}\;q)}L(s,\chi).

Principle 2. Deuring–Heilbronn phenomenon.

Principle 3. ‘Log-free’ zero density estimates.

For the proof of the result E ⁡ ( X) < X 1 − ϑ E(X)<X^{1-\vartheta} it will suffice to take over from Heath-Brown’s work [9] a small part of his results concerning Principles 1 and 2 (see Theorems E, F, G in our next section) partially in the form improved by Xylouris [22]. In the forthcoming papers, when proving sharper inequalities for E ⁡ ( X) E(X) we will need much more results of this type and in many cases in somewhat stronger form.

On the other hand, the zero density estimates of [9], as well as some similar ones of others, used in earlier examination of Linnik’s problem do not suite for our purposes.

Heath-Brown starts, namely, with a weighted average over primes, which does not seem to work in Goldbach’s problem. Since in this way in Linnik’s problem zeros of the same L L -function can be treated together, it is sufficient to estimate the number of L L -functions mod ​ q \,\text{\rm mod}\;q, having at least one zero in a given range, instead of the total number of zeros in the relevant range as in case of usual density theorems. The corresponding density theorems of Chen–Liu [1] and H. Z. Li [12], [13] and Lu [14] are far too weak as to yield Theorem 1. Therefore we will show a new log-free density theorem (Theorem C) which counts all zeros and is still just slightly weaker than the corresponding result of Heath-Brown [9], Lemma 11.1 which counts only the number of ℒ \mathcal{L} -functions belonging to these zeros.

Another invention of Heath-Brown [9] is the proof of a ‘new density theorem’, his Lemma 12.1, which works only for zeros very near to the line σ = 1 \sigma=1 (approximately in the region σ > 1 − 5 / ( 4 ​ log ⁡ q) \sigma>1-5/(4\log q)). This result can also be extended for the number of L L -functions having at least one zero in the relevant range. The method of proof of this result is nearer to the proof of the Deuring–Heilbronn phenomenon than to that of the density theorems. Concerning this result we succeeded in modifying the proof in such a way as to yield the same estimate without any loss for the total number of zeros (cf. Theorems H and I). In another version of this method we can directly prove a weighted density theorem, essentially for the weights appearing in ( 2.33) which is even more useful than unweighted density theorems (cf. Theorem J).

A new feature of our case is (which does not appear in Linnik’s problem) that we need density theorems for zeros of a restricted class of L L -functions belonging to equivalent characters (cf. ( 2.40), ( 2.41) and ( 2.46)). The usual proofs for density theorems naturally work for these cases as well, and they usually yield somewhat stronger results in this case, like a comparison of Corollaries 1 and 2 show in the next section. However, an improvement of the technique applied by Heath-Brown in the proof of his new density theorem allows us to reach drastic improvements for the number of zeros in one equivalence class ( N ν ​ ( Λ)) (N_{\nu}(\Lambda)) compared with the case of all L L -functions ( N ⁡ ( Λ)) (N(\Lambda)). In the range σ > 1 − 5 / ( 4 ​ log ⁡ q) \sigma>1-5/(4\log q) ( ⇔ λ < 5 / 4) (\Leftrightarrow\lambda<5/4), for example, we obtain at most 7 7 zeros for one class, instead of the bound more than a hundred, supplied by the old or new density theorems of Heath-Brown (cf. [9], Tables 12 and 13) for the number of all L L -function having at least one zero in the same range. A further advantage of this method is that the bounds obtained in this way for N ν ​ ( Λ) N_{\nu}(\Lambda) remain valid in the much wider range σ > 1 − 6 / log ⁡ q \sigma>1-6/\log q. After this, the contribution of zeros with λ > 6 \lambda>6 can be estimated already very efficiently by Corollary 2.

## 4 Auxiliary results

In the present section we will list the needed auxiliary theorems for the estimation of the crucial quantity for S 0 S_{0} in ( 2.33). These auxiliary theorems give important information about the distribution of zeros of L L -functions near to s = 1 s=1.

The first one is a weighted density theorem which is the generalization of Heath-Brown’s Lemma 11.1 [9] for the case when we estimate the total number of zeros instead of the number of L L -functions having at least one zero in the given region. The result will have two different versions according to which we consider all L L -functions or just a class of similar L L -functions in the sense of Theorem D.

Theorem C. Let C ′, ε, c 1, c 2, Λ > 0 C^{\prime},\varepsilon,c_{1},c_{2},\Lambda>0 be given, q ≥ q ⁡ ( ε, c 1, c 2, C ′, κ) q\geq q(\varepsilon,c_{1},c_{2},C^{\prime},\kappa),

(4.1) |  | Λ ∞ = 1 3 ​ log ⁡ log ⁡ ℒ, φ ≥ max χ ⁡ ( mod ​ q) ⁡ φ ⁡ ( χ), r = φ + c 1 + c 2 3, x 0 = 2 ​ φ + 3 ​ c 1 + c 2, \Lambda_{\infty}=\frac{1}{3}\log\log\mathcal{L},\ \ \varphi\geq\max_{\chi(\,\text{\rm mod}\;q)}\varphi(\chi),\ \ r=\frac{\varphi+c_{1}+c_{2}}{3},\ \ x_{0}=2\varphi+3c_{1}+c_{2}, |  |

(4.2) |  | w ⁡ ( ϱ) = w ⁡ ( 1 − ℒ ⁡ ( λ + i ​ μ)) = e − 2 ​ ( x 0 + κ) ​ λ − r + κ 2 ​ d, d = max ⁡ ( 0, Λ − λ). w(\varrho)=w\bigl(1-\mathcal{L}(\lambda+i\mu)\bigr)=e^{-2(x_{0}+\kappa)\lambda-\frac{r+\kappa}{2}d},\quad d=\max(0,\Lambda-\lambda). |  |

Then we have with an absolute constant C C depending on C ′ C^{\prime}

(4.3) |  | ∑ ϱ = ϱ χ, χ ⁡ ( mod ​ q) λ ≤ Λ ∞ | μ | ≤ C ′ w ⁡ ( ϱ) ≤ ( 1 + C ​ ε) ​ C 1 ​ B φ, κ ​ ( Λ) ​ B φ, r ​ ( Λ) / κ = C 2 ​ ( φ, κ, Λ) ​ ( 1 + C ​ ε), \sum_{\begin{subarray}{c}\varrho=\varrho_{\chi},\ \chi(\,\text{\rm mod}\;q)\\ \lambda\leq\Lambda_{\infty}\\ |\mu|\leq C^{\prime}\end{subarray}}w(\varrho)\leq(1+C\varepsilon)C_{1}\sqrt{B_{\varphi,\kappa}(\Lambda)B_{\varphi,r}(\Lambda)}/\kappa=C_{2}(\varphi,\kappa,\Lambda)(1+C\varepsilon), |  |

where

(4.4) |  | C 1 = 2 ​ φ + 2 ​ c 1 + c 2 2 ​ c 1 ​ c 2, C_{1}=\frac{2\varphi+2c_{1}+c_{2}}{2c_{1}c_{2}}, |  |

(4.5) |  | B φ, ω ​ ( y) = φ 2 ​ ( 1 − e − 2 ​ ω ​ y y) + ( 1 − e − ω ​ y y) 2. B_{\varphi,\omega}(y)=\frac{\varphi}{2}\left(\frac{1-e^{-2\omega y}}{y}\right)+\left(\frac{1-e^{-\omega y}}{y}\right)^{2}. |  |

Theorem D. Suppose that 𝒦 \mathcal{K} is a set of characters χ i ​ mod ​ q \chi_{i}\,\text{\rm mod}\;q with the condition that for all pairs χ i, χ j ∈ 𝒦 \chi_{i},\chi_{j}\in\mathcal{K}

(4.6) |  | cond ​ ( χ i ​ χ ¯ j) ≤ q ε. \text{\rm cond}\,(\chi_{i}\overline{\chi}_{j})\leq q^{\varepsilon}. |  |

Further let us suppose the conditions of Theorem C with

(4.7) |  | x 0 = φ + 3 ​ c 1 + c 2, φ ≥ max χ ∈ 𝒦 ⁡ φ ⁡ ( χ). x_{0}=\varphi+3c_{1}+c_{2},\quad\varphi\geq\max_{\chi\in\mathcal{K}}\varphi(\chi). |  |

Then ( 4.3) holds if the sum is restricted for zeros of L ⁡ ( s, χ) L(s,\chi), χ ∈ 𝒦 \chi\in\mathcal{K}.

Remark 1. Although the estimate on the right-hand side of ( 4.3) remained unchanged, the new estimate is stronger, since the new weights will be larger, due to the smaller choice of x 0 x_{0} in ( 4.7).

Choosing c 1 = 1 / 12 c_{1}=1/12, c 2 = 1 / 4 c_{2}=1/4, φ = 1 / 3 \varphi=1/3, κ = 1 / 6 \kappa=1/6, ( C 1 = 26 C_{1}=26) we are led to the following results (to be used in Section 9).

###### Corollary 1.

Let Λ 0 = 1.311 \Lambda_{0}=1.311, Λ 1 = 2.421 \Lambda_{1}=2.421, Λ 2 = 3.96 \Lambda_{2}=3.96, Λ 3 = 5.8 \Lambda_{3}=5.8, E 0 = 22.281 E_{0}=22.281, E 1 = 15.6 E_{1}=15.6, E 2 = 10.4 E_{2}=10.4, E 3 = 7.01 E_{3}=7.01. Then we have for i = 0, 1, 2 i=0,1,2:

(4.8) |  | ∑ λ ≤ Λ ∞ e − 8 3 ​ λ − 5 12 ​ max ⁡ ( 0, Λ − λ) < E i for ​ Λ ≥ Λ i, \sum_{\lambda\leq\Lambda_{\infty}}e^{-\frac{8}{3}\lambda-\frac{5}{12}\max(0,\Lambda-\lambda)}<E_{i}\quad\text{ for }\ \Lambda\geq\Lambda_{i}, |  |

(4.9) |  | ∑ χ ∈ 𝒦 λ ≤ Λ ∞ e − 2 ​ λ − 5 12 ​ max ⁡ ( 0, Λ − λ) < E i for ​ Λ ≥ Λ i. \sum_{\begin{subarray}{c}\chi\in\mathcal{K}\\ \lambda\leq\Lambda_{\infty}\end{subarray}}e^{-2\lambda-\frac{5}{12}\max(0,\Lambda-\lambda)}<E_{i}\quad\text{ for }\ \Lambda\geq\Lambda_{i}. |  |

###### Corollary 2.

With the notation of ( 2.45)–( 2.46) and Corollary 1 we have

(4.10) |  | N ⁡ ( Λ) < E i ​ e 8 ​ Λ / 3 for ​ Λ ≥ Λ i, N(\Lambda)<E_{i}e^{8\Lambda/3}\quad\text{ for }\ \Lambda\geq\Lambda_{i}, |  |

(4.11) |  | N ν ​ ( Λ) < E i ​ e 2 ​ Λ for ​ Λ ≥ Λ i. N_{\nu}(\Lambda)<E_{i}e^{2\Lambda}\quad\text{ for }\ \Lambda\geq\Lambda_{i}. |  |

Remark. Since the functions B φ, ω ​ ( y) B_{\varphi,\omega}(y) are monotonically decreasing in y y for all non-negative values of the parameters φ \varphi and a a, the estimates E i E_{i} arising from Λ i \Lambda_{i} are valid for all Λ ≥ Λ i \Lambda\geq\Lambda_{i}.

The results listed as Theorems E, F, G below are Theorem 1 of Xylorius and Theorems 2 and 4 (more precisely Lemma 8.8) of Heath-Brown [9] with the only change that the condition | γ | ≤ 1 |\gamma|\leq 1 for the zeros can be substituted without any essential change in the proof for | γ | ≤ T |\gamma|\leq T if q > q 0 ​ ( T) q>q_{0}(T). ( T T is in our case a large constant depending on ε \varepsilon.) Thus in the following theorems let ε, T \varepsilon,T be positive constants,

(4.12) |  | M ⁡ ( s) = ∏ χ ⁡ ( mod ​ q) L ⁡ ( s, χ), M(s)=\prod_{\chi(\,\text{\rm mod}\;q)}L(s,\chi), |  |

(4.13) |  | R ⁡ ( α, T) = { s; σ ≥ 1 − α log ⁡ q, | t | ≤ T } R(\alpha,T)=\left\{s;\ \sigma\geq 1-\frac{\alpha}{\log q},\ |t|\leq T\right\} |  |

and let us suppose that q > q 0 ​ ( T, ε) q>q_{0}(T,\varepsilon).

Theorem E. M ⁡ ( s) M(s) has at most one zero in R ⁡ ( 0.44, T) R(0.44,T). Such a zero, if it exists, is real and simple and corresponds to a non-principal character.

Theorem F. M ⁡ ( s) M(s) has at most two zeros, counted according to multiplicity, in R ⁡ ( 0.702, T) R(0.702,T).

Remark. Heath-Brown [9] proved this with 0.696 0.696 in place of 0.702 0.702. The small improvement is due to Xylouris [22, Tabellen 2, 3 and 7].

Theorem G. Suppose that χ \chi is a real non-principal character mod ​ q \,\text{\rm mod}\;q with

(4.14) |  | L ⁡ ( 1 − λ log ⁡ q, χ) = 0, 0 < λ ≤ 0.44. L\left(1-\frac{\lambda}{\log q},\chi\right)=0,\quad 0<\lambda\leq 0.44. |  |

Then M ⁡ ( s) M(s) has only the zero 1 − λ / log ⁡ q 1-\lambda/\log q in the region R ⁡ ( Λ ⁡ ( λ), T) ∪ R ⁡ ( 1.18, T) R(\Lambda(\lambda),T)\cup R(1.18,T)

(4.15) |  | Λ ⁡ ( λ) = min ⁡ { ( 12 11 − ε) ​ log ⁡ 1 λ, 1 3 ​ log ⁡ log ​ log ⁡ q }. \Lambda(\lambda)=\min\left\{\left(\frac{12}{11}-\varepsilon\right)\log\frac{1}{\lambda},\frac{1}{3}\log\log\log q\right\}. |  |

The fact that M ⁡ ( s) M(s) has no other zeros in R ⁡ ( Λ ⁡ ( λ), T) R(\Lambda(\lambda),T) is exactly Lemma 8.8 of Heath-Brown [9]. The absence of other zeros in R ⁡ ( 1.18, T) R(1.18,T) follows from Tables 4 and 7 of Heath-Brown [9] (pp. 298, 301), which follow from his Lemmas 8.3 and 8.7, respectively.

In the following we will formulate the new density theorems which are improved forms of Lemma 12.1 of Heath-Brown [9]. Although in the application we will work (unlike Heath-Brown) with a concrete function we will formulate the result more generally, similarly to [9]. (The following condition is the same as Conditions 1 and 2 of [9] together.)

Condition 1. Let f f be a non-negative continuous function from [0, ∞) [0,\infty) to ℝ \mathbb{R}, supported in [0, t 0) [0,t_{0}), twice differentiable on ( 0, t 0) (0,t_{0}) with f ′′ f^{\prime\prime} continuous and bounded. Suppose that its Laplace transform

(4.16) |  | F ⁡ ( z) = ∫ 0 t 0 e − z ​ t ​ f ​ ( t) ​ 𝑑 t F(z)=\int\limits^{t_{0}}_{0}e^{-zt}f(t)dt |  |

satisfies

(4.17) |  | Re ​ F ​ ( z) ≥ 0 for ​ Re ​ z ≥ 0. \mathrm{Re}\,F(z)\geq 0\quad\text{ for }\ \text{\rm Re}\,z\geq 0. |  |

We will work with the following pair of functions, satisfying Condition 1 (which appears in Lemma 7.2 of [9])

(4.18) |  | g ⁡ ( u) = 1 30 ​ ( 2 − u) 3 ​ ( 4 + 6 ​ u + u 2) with ​ u ∈ [0, 2] g(u)=\frac{1}{30}(2-u)^{3}(4+6u+u^{2})\quad\text{ with }\ u\in[0,2] |  |

(4.19) |  | G ⁡ ( z) \displaystyle G(z) | = ∫ 0 2 e − z ​ u ​ g ​ ( u) ​ 𝑑 u \displaystyle=\int\limits^{2}_{0}e^{-zu}g(u)du |  |

 |  | = 16 15 ​ z − 8 3 ​ z 3 + 4 z 4 − 4 z 6 + 4 ​ e − 2 ​ z z 4 ​ ( z + 1 z) 2. \displaystyle=\frac{16}{15z}-\frac{8}{3z^{3}}+\frac{4}{z^{4}}-\frac{4}{z^{6}}+\frac{4e^{-2z}}{z^{4}}\left(\frac{z+1}{z}\right)^{2}. |  |

The explicit form of G ⁡ ( z) G(z) follows simply by computation. Further (cf. [9], Lemma 7.2)

(4.20) |  | g = h ∗ h, where ​ h ​ ( t) = 1 − t 2, − 1 ≤ t ≤ 1. g=h*h,\quad\text{ where }\ h(t)=1-t^{2},\ \ -1\leq t\leq 1. |  |

Therefore we have

(4.21) |  | Re ⁡ ( G ⁡ ( i ​ y)) = ∫ 0 2 g ⁡ ( u) ​ cos ⁡ ( u ​ y) ​ 𝑑 u = 2 ​ ( ∫ 0 1 h ⁡ ( t) ​ cos ⁡ t ​ y ​ 𝑑 t) 2 ≥ 0. \mathrm{Re}(G(iy))=\int\limits^{2}_{0}g(u)\cos(uy)du=2\biggl(\int\limits^{1}_{0}h(t)\cos ty\,dt\biggr)^{2}\geq 0. |  |

Finally, from Lemma 4.1 of [9] (see also p. 279 of [9]) we have by ( 4.21)

(4.22) |  | Re ​ G ​ ( z) ≥ 0 for ​ Re ​ z ≥ 0. \mathrm{Re}\,G(z)\geq 0\quad\text{ for }\ \mathrm{Re}\,z\geq 0. |  |

Instead of the concrete functions g ⁡ ( u) g(u) and G ⁡ ( z) G(z) above we will use a one-parameter family of functions:

(4.23) |  | f = f x ​ ( u) = x ​ g ​ ( u ​ x), u ​ x ∈ [0, 2] ⇔ u ∈ [0, 2 x] f=f_{x}(u)=xg(ux),\qquad ux\in[0,2]\Leftrightarrow u\in\left[0,\frac{2}{x}\right] |  |

(4.24) |  | F = F x ​ ( z) \displaystyle F=F_{x}(z) | = ∫ 0 2 / x e − z ​ u ​ f x ​ ( u) ​ 𝑑 u = ∫ 0 2 / x e − z x ​ u ​ x ​ g ​ ( u ​ x) ​ x ​ 𝑑 u \displaystyle=\int\limits^{2/x}_{0}e^{-zu}f_{x}(u)du=\int\limits^{2/x}_{0}e^{-\frac{z}{x}ux}g(ux)xdu |  |

 |  | = ∫ 0 2 e − z x ​ v ​ g ​ ( v) ​ 𝑑 v = G ⁡ ( z x). \displaystyle=\int\limits^{2}_{0}e^{-\frac{z}{x}v}g(v)dv=G\Bigl(\frac{z}{x}\Bigr). |  |

An easy calculation shows (cf. Lemma 7.2 of [9])

(4.25) |  | f ⁡ ( 0) = 16 ​ x 15, F ⁡ ( 0) = G ⁡ ( 0) = 8 9, F ⁡ ( − x) = G ⁡ ( − 1) = 8 5. f(0)=\frac{16x}{15},\quad F(0)=G(0)=\frac{8}{9},\quad F(-x)=G(-1)=\frac{8}{5}. |  |

In the applications (Theorems I, H, J) the following additional property of the functions F F will have importance, which is satisfied for G ⁡ ( z) G(z) for A 0 = 13 A_{0}=13, B 0 = 1.25 B_{0}=1.25, for example.

Condition 2. There are non-negative constants A 0 A_{0} and B 0 B_{0} such that for any t ∈ ℝ t\in\mathbb{R}

(4.26) |  | Re ​ G ⁡ ( a + i ​ t) G ⁡ ( a) ≥ Re ​ G ⁡ ( − b + i ​ t) G ⁡ ( − b) \mathrm{Re}\,\frac{G(a+it)}{G(a)}\geq\mathrm{Re}\,\frac{G(-b+it)}{G(-b)} |  |

if

(4.27) |  | 0 ≤ a ≤ A 0, 0 ≤ b ≤ B 0. 0\leq a\leq A_{0},\quad 0\leq b\leq B_{0}. |  |

Remark. Let us take A 0 A_{0}, B 0 B_{0} arbitrary, non-negative constants, η > 0 \eta>0 fix. Then for η ≤ a ≤ A 0 \eta\leq a\leq A_{0}, 0 ≤ b ≤ B 0 0\leq b\leq B_{0}, | t | > t 0 ​ ( η, A 0, B 0) |t|>t_{0}(\eta,A_{0},B_{0}) we have from ( 4.19)

(4.28) |  | Re ​ G ⁡ ( a + i ​ t) G ⁡ ( a) > c ⁡ ( A 0, η) t 2 > − c ′ ​ ( B 0) t 2 > Re ​ G ⁡ ( − b + i ​ t) G ⁡ ( − b) \mathrm{Re}\,\frac{G(a+it)}{G(a)}>\frac{c(A_{0},\eta)}{t^{2}}>-\frac{c^{\prime}(B_{0})}{t^{2}}>\mathrm{Re}\,\frac{G(-b+it)}{G(-b)} |  |

with positive constants c ⁡ ( A 0, η) c(A_{0},\eta), c ′ ​ ( B 0) c^{\prime}(B_{0}).

This shows already that Condition 2 can be verified for the G G function in ( 4.19) by the aid of computers for concrete values of A 0 A_{0} and B 0 B_{0} (consequently for the F F -functions in ( 4.24) if x x, A 0 A_{0} and B 0 B_{0} are given).

This preparation makes possible to formulate the remaining 3 density theorems. In these theorems we will use the notation ( 2.45)–( 2.46), where in ( 2.46) we can ease the condition of equivalent characters without any loss for the final estimate. Let T > 0 T>0, ε > 0 \varepsilon>0 be constants, q > q ⁡ ( T, ε) q>q(T,\varepsilon), ℒ = log ⁡ q \mathcal{L}=\log q; zeros of L L -functions belonging to characters χ \chi mod ​ q \,\text{\rm mod}\;q with φ ≥ max ⁡ φ ⁡ ( q) \varphi\geq\max\varphi(q) will be denoted (cf. ( 2.38)) as

(4.29) |  | ϱ:= ϱ χ:= 1 − δ + i ​ γ, λ:= δ ​ ℒ, μ:= γ ​ ℒ. \varrho:=\varrho_{\chi}:=1-\delta+i\gamma,\quad\lambda:=\delta\mathcal{L},\ \ \mu:=\gamma\mathcal{L}. |  |

Suppose that with a λ 0 ≥ 0 \lambda_{0}\geq 0 we have for all zeros of all L ⁡ ( s, χ) L(s,\chi), χ ​ mod ​ q \chi\,\,\text{\rm mod}\;q

(4.30) |  | λ ≥ λ 0. \lambda\geq\lambda_{0}. |  |

We will use the following notation with λ = λ j ≤ Λ \lambda=\lambda_{j}\leq\Lambda:

(4.31) |  | F ⁡ ( λ j − λ 0) F ⁡ ( − λ 0) = ψ j, F ⁡ ( Λ − λ 0) F ⁡ ( − λ 0) = ψ, f ⁡ ( 0) ​ φ 2 ​ F ​ ( − λ 0) = ξ, Δ = ψ − ξ > 0. \frac{F(\lambda_{j}-\lambda_{0})}{F(-\lambda_{0})}=\psi_{j},\quad\frac{F(\Lambda-\lambda_{0})}{F(-\lambda_{0})}=\psi,\quad\frac{f(0)\varphi}{2F(-\lambda_{0})}=\xi,\quad\Delta=\psi-\xi>0. |  |

Theorem H. Suppose that f f and F F satisfy Conditions 1 and 2. Let 0 ≤ λ 0 ≤ B 0 ​ ( F) 0\leq\lambda_{0}\leq B_{0}(F), 0 ≤ Λ − λ 0 ≤ A 0 ​ ( F) 0\leq\Lambda-\lambda_{0}\leq A_{0}(F), Δ 2 > ξ + ε \Delta^{2}>\xi+\varepsilon. Then

(4.32) |  | N ⁡ ( Λ):= N T ​ ( Λ) = ∑ | γ | ≤ T, λ ≤ Λ 1 ≤ 1 − ξ Δ 2 − ξ − ε. N(\Lambda):=N_{T}(\Lambda)=\sum_{|\gamma|\leq T,\ \lambda\leq\Lambda}1\leq\frac{1-\xi}{\Delta^{2}-\xi-\varepsilon}. |  |

Theorem I. Suppose that ℋ \mathcal{H} is a set of characters χ ​ mod ​ q \chi\,\,\text{\rm mod}\;q with the property

(4.33) |  | cond ​ ( χ ​ χ ¯ ′) ≤ q ε for ​ χ, χ ′ ∈ ℋ. \text{\rm cond}\,(\chi\overline{\chi}^{\prime})\leq q^{\varepsilon}\quad\text{ for }\ \chi,\chi^{\prime}\in\mathcal{H}. |  |

Then with the conditions of Theorem H we have

(4.34) |  | N ~ ​ ( Λ) = N T, ℋ ​ ( Λ) = ∑ χ ∈ ℋ | γ χ | ≤ T, λ χ ≤ Λ 1 ≤ 1 + ε Δ 2. \widetilde{N}(\Lambda)=N_{T,\mathcal{H}}(\Lambda)=\sum_{\begin{subarray}{c}\chi\in\mathcal{H}\\ |\gamma_{\chi}|\leq T,\ \lambda_{\chi}\leq\Lambda\end{subarray}}1\leq\frac{1+\varepsilon}{\Delta^{2}}. |  |

The following Theorem J will enable us to estimate directly weighted sums over zeros, which arise in our problem. This method partly reduces drastically the needed amount of calculations and also yields better estimates for the weighted sums than the usual treatment via partial summation (which cannot be performed easily in these cases due to the complicated forms of the upper bounds). Further on we will suppose the Conditions of Theorem H and additionally the existence of two constants B B and C C with

(4.35) |  | B > max ⁡ ( C, t 0 ​ ( f)) ≥ 0 B>\max\bigl(C,t_{0}(f)\bigr)\geq 0 |  |

where t 0 = t 0 ​ ( f) t_{0}=t_{0}(f) is defined in Condition A by f ⁡ ( t) = 0 f(t)=0 for t ≥ t 0 t\geq t_{0}.

First we state

Theorem J. Under the conditions of Theorem H we have

(4.36) |  | D ⁡ ( Λ):= ∑ | γ j | ≤ T, λ j ≤ Λ ( ψ j − ψ) ≤ 1 − ξ + O ⁡ ( ε) 2 ​ Δ. D(\Lambda):=\sum_{|\gamma_{j}|\leq T,\ \lambda_{j}\leq\Lambda}(\psi_{j}-\psi)\leq\frac{1-\xi+O(\varepsilon)}{2\Delta}. |  |

Suppose that F F satisfies Condition A, d 0 d_{0} and C ′ C^{\prime} are given and with the J J unknown variables d 0 ≥ d 1 ≥ ⋯ ≥ d J ≥ 0 d_{0}\geq d_{1}\geq\dots\geq d_{J}\geq 0 ( d j = Λ − λ j CLOSE (d_{j}=\Lambda-\lambda_{j}, OPEN j = 0, …, J) j=0,\dots,J) we know the upper bound

(4.37) |  | D ∗ ​ ( d 0) = ∑ j ≤ J ( F ⁡ ( d 0 − d j) − F ⁡ ( d 0)) ≤ C ′. D^{*}(d_{0})=\sum_{j\leq J}\bigl(F(d_{0}-d_{j})-F(d_{0})\bigr)\leq C^{\prime}. |  |

We are interested in the maximal value of the quantity

(4.38) |  | S ∗ = ∑ j ≤ J ( e B ​ d j − e C ​ d j), B > C ≥ 0, S^{*}=\sum_{j\leq J}\bigl(e^{Bd_{j}}-e^{Cd_{j}}\bigr),\qquad B>C\geq 0, |  |

under the additional constraint with given { e j } 1 J \{e_{j}\}^{J}_{1}

(4.39) |  | d j ≤ e j, e 1 ≥ e 2 ≥ ⋯ ≥ e J. d_{j}\leq e_{j},\quad e_{1}\geq e_{2}\geq\dots\geq e_{J}. |  |

In this case we can find the maximum of S ∗ S^{*} with a type of greedy algorithm as follows. Suppose that 1 ≤ r ≤ J 1\leq r\leq J is defined as

(4.40) |  | ∑ j = 1 r − 1 ( F ⁡ ( d 0 − e j) − F ⁡ ( d 0)) ≤ C ′ < ∑ j = 1 r ( F ⁡ ( d 0 − e j) − F ⁡ ( d 0)). \sum^{r-1}_{j=1}\bigl(F(d_{0}-e_{j})-F(d_{0})\bigr)\leq C^{\prime}<\sum^{r}_{j=1}\bigl(F(d_{0}-e_{j})-F(d_{0})\bigr). |  |

Theorem K. Under the above conditions the optimal choice is ( r = 1 r=1 is possible too, when ( 4.41) is void) to choose

(4.41) |  | d j = e j ​ for ​ j = 1, 2, …, r − 1 d_{j}=e_{j}\ \text{ for }\ j=1,2,\dots,r-1 |  |

and d r d_{r} as the unique value with

(4.42) |  | F ⁡ ( d 0 − d r) = F ⁡ ( d 0) + C ′ − ∑ j = 1 r − 1 ( F ⁡ ( d 0 − e j) − F ⁡ ( d 0)). F(d_{0}-d_{r})=F(d_{0})+C^{\prime}-\sum_{j=1}^{r-1}\bigl(F(d_{0}-e_{j})-F(d_{0})\bigr). |  |

Further, we choose d ν = 0 d_{\nu}=0 for r < ν ≤ J r<\nu\leq J.

Remark 1. If there is no r ∈ ( 1, J) r\in(1,J) with ( 4.40), that is

(4.43) |  | ∑ j = 1 J ( F ⁡ ( d 0 − e j) − F ⁡ ( d 0)) ≤ C ′, \sum^{J}_{j=1}\bigl(F(d_{0}-e_{j})-F(d_{0})\bigr)\leq C^{\prime}, |  |

then the maximum of S ∗ S^{*} is clearly given by the choice e j = d j e_{j}=d_{j} for 1 ≤ j ≤ J 1\leq j\leq J.

Remark 2. By the fact that F F is strictly monotonically decreasing if f ⁡ ( t) f(t) is not identically 0 0, we obtain from ( 4.42) that d r d_{r} is completely determined and 0 ≤ d r ≤ e r 0\leq d_{r}\leq e_{r} due to F ⁡ ( d 0 − e r) ≥ F ⁡ ( d 0 − d r) ≥ F ⁡ ( d 0) F(d_{0}-e_{r})\geq F(d_{0}-d_{r})\geq F(d_{0}).

Remark 3. Theorem K itself refers to arbitrary numbers but in the applications we will use it with

(4.44) |  | d j = Λ − λ j, d 0 = Λ − λ 0, C ′ = F ⁡ ( − λ 0) ​ 1 − ξ + C ​ ε 2 ​ Δ d_{j}=\Lambda-\lambda_{j},\ \ d_{0}=\Lambda-\lambda_{0},\ \ C^{\prime}=F(-\lambda_{0})\frac{1-\xi+C\varepsilon}{2\Delta} |  |

in conjunction with estimate ( 4.36) of Theorem J. Although Theorem K itself does need only Condition 1 for F F, Theorem J needs both Conditions 1 and 2.

Remark 4. The conditions d i ≤ e i d_{i}\leq e_{i}, i = 1, … ​ J i=1,\dots J imply J J inequalities of the type ( m = 1, 2, …, J) (m=1,2,\dots,J)

(4.45) |  | D ∗ ​ ( d 0, m) = ∑ j ≤ m ( F ⁡ ( d 0 − d j) − F ⁡ ( d 0)) ≤ C 0 ′ ​ ( m) D^{*}(d_{0},m)=\sum_{j\leq m}\bigl(F(d_{0}-d_{j})-F(d_{0})\bigr)\leq C^{\prime}_{0}(m) |  |

with

(4.46) |  | C 0 ′ ​ ( m):= C 0 ′ ​ ( m, { e j }) = ∑ j ≤ m ( F ⁡ ( d 0 − e j) − F ⁡ ( d 0)). C^{\prime}_{0}(m):=C^{\prime}_{0}(m;\{e_{j}\})=\sum_{j\leq m}\bigl(F(d_{0}-e_{j})-F(d_{0})\bigr). |  |

Although it is not necessary for application in the present work (just in later parts of this series) we will examine the more general case when in place of the conditions d i ≤ e i d_{i}\leq e_{i} we will have more generally a finite sequence of M M inequalities ( d 1 ≥ ⋯ ≥ d M ≥ 0) (d_{1}\geq\dots\geq d_{M}\geq 0)

(4.47) |  | D ~ ​ ( d 0, m) = ∑ j ≤ m F ⁡ ( d 0 − d j) ≤ c ′ ​ ( m) = c ⁡ ( m) + m ​ F ​ ( d 0) \widetilde{D}(d_{0},m)=\sum_{j\leq m}F(d_{0}-d_{j})\leq c^{\prime}(m)=c(m)+mF(d_{0}) |  |

where c ⁡ ( m) ≥ c ⁡ ( m − 1) c(m)\geq c(m-1) is an increasing sequence of real numbers satisfying for m = 2, … ​ M − 1 m=2,\dots M-1

(4.48) |  | c ⁡ ( m + 1) − c ⁡ ( m) ≤ c ⁡ ( m) − c ⁡ ( m − 1). c(m+1)-c(m)\leq c(m)-c(m-1). |  |

(If there exists an m 0 = min ⁡ { ν; c ⁡ ( ν) < 0 } m_{0}=\min\{\nu;\ c(\nu)<0\}, then the system consists of at most m 0 − 1 m_{0}-1 elements. In this case we cancel the inequalities with index ≥ m 0 \geq m_{0}, which is equivalent to the condition M = m 0 − 1 M=m_{0}-1, c ⁡ ( j) ≥ 0 c(j)\geq 0 for j = 1, …, M j=1,\dots,M.)

Theorem L. Under the above conditions the maximum of S ∗ S^{*} in ( 4.38) (with M = J M=J) is achieved for the uniquely determined sequence { d m } m = 1 M \{d_{m}\}^{M}_{m=1} for which equality holds in ( 4.47) for all m = 1, …, M m=1,\dots,M.

Remark 5. If we add at the end some terms d m = 0 d_{m}=0 with m > M m>M this does not change the value of S ∗ S^{*}, so allowing some extra conditions with M < m ≤ R M<m\leq R ( R R a fixed large constant) c ⁡ ( m) = c ⁡ ( M) c(m)=c(M), will definitely not decrease the maximum. In this way we can work in the applications with an a priori determined (large but bounded) number M M of variables (since we know that in our application the number of zeros with λ j ≤ λ \lambda_{j}\leq\lambda satisfies a bound depending on λ \lambda – see e.g. Corollary 2) and the obtained upper bound for the new (extended) sum S ∗ S^{*} will constitute an upper bound for the original S ∗ S^{*}.

Remark 6. As we substituted the conditions d i ≤ e i d_{i}\leq e_{i} by its consequence ( 4.45)–( 4.46) this may theoretically increase the maximum value S ∗ S^{*}. However, Theorem L tells us that this is not the case since for the maximum configuration { d i } \{d_{i}\} we will in fact have d i = e i d_{i}=e_{i} for i ≤ J i\leq J, since all the inequalities ( 4.45) are sharp.

## 5 Proof of Theorems C and D

In this section we will prove Theorems C and D. The first part of the proof will be very similar to the proof presented in Section 3 of [17] which follows the works of Heath-Brown [9] and Graham [7]. The second part of the proof will use also ideas of Heath-Brown [9], however not from the proof of the corresponding density theorem, but from Section 13 of [9].

Following more closely [9] and slightly different from (3.14) of [17] we will use the notation

(5.1) |  | U = q u, U 0 = q u 0, V = q v, W = q w, X 1 = q x 1, X = q x, X 0 = q x 0, U ¯ = U ​ ℒ 2, U\!=\!q^{u},\ U_{0}\!=\!q^{u_{0}},\ V\!=\!q^{v},\ W=q^{w},\ X_{1}=q^{x_{1}},\ X=q^{x},\ X_{0}=q^{x_{0}},\ \overline{U}=U\mathcal{L}^{2}, |  |

(5.2) |  | ε 1 = ε 2 / 100, w = c 1 − ε, v = u + c 2, x 0 = u 0 + r, x 1 = x 0 + κ, u = u 0 + η, x = x 0 + η, 0 ≤ η ≤ κ. \begin{gathered}\varepsilon_{1}=\varepsilon^{2}/100,\ \ w=c_{1}-\varepsilon,\ \ v=u+c_{2},\ \ x_{0}=u_{0}+r,\\ x_{1}=x_{0}+\kappa,\ \ u=u_{0}+\eta,\ \ x=x_{0}+\eta,\ \ 0\leq\eta\leq\kappa.\end{gathered} |  |

Further, in case of Theorem C, we will choose

(5.3) |  | u 0 = φ + 2 ​ c 1, x 0 = 2 ​ φ + 3 ​ c 1 + c 2, r = φ + c 1 + c 2, u_{0}=\varphi+2c_{1},\quad x_{0}=2\varphi+3c_{1}+c_{2},\quad r=\varphi+c_{1}+c_{2}, |  |

whereas in case of Theorem D we set

(5.4) |  | u 0 = 2 ​ c 1, x 0 = φ + 3 ​ c 1 + c 2, r = φ + c 1 + c 2. u_{0}=2c_{1},\quad x_{0}=\varphi+3c_{1}+c_{2},\quad r=\varphi+c_{1}+c_{2}. |  |

Similarly to [17] and [9] we will use Graham’s weights

(5.5) |  | ψ d \displaystyle\psi_{d} | = { μ ⁡ ( d) for ​ 1 ≤ d ≤ U ¯ μ ⁡ ( d) ​ log ⁡ ( V / d) log ⁡ ( V / U ¯) for ​ U ¯ ≤ d ≤ V 0 for ​ d ≥ V, \displaystyle=\begin{cases}\mu(d)&\text{ for }\ 1\leq d\leq\overline{U}\\ \mu(d)\frac{\log(V/d)}{\log(V/\overline{U})}&\text{ for }\ \overline{U}\leq d\leq V\\ 0&\text{ for }\ d\geq V\end{cases}, |  |

(5.6) |  | θ d \displaystyle\theta_{d} | = { μ ⁡ ( d) ​ log ⁡ W / d log ⁡ W for ​ 1 ≤ d ≤ W 0 for ​ d ≥ W, \displaystyle=\begin{cases}\mu(d)\frac{\log W/d}{\log W}&\ \,\text{ for }\ 1\leq d\leq W\\ 0&\ \,\text{ for }\ d\geq W\end{cases}, |  |

(5.7) |  | Ψ ⁡ ( n) = ∑ d | n ψ d, ϑ ⁡ ( n) = ∑ d | n θ d, \Psi(n)=\sum_{d\mid n}\psi_{d},\qquad\vartheta(n)=\sum_{d\mid n}\theta_{d}, |  |

further, the functions

(5.8) |  | F ⁡ ( s) \displaystyle F(s) | = ∑ i ≤ V, j ≤ W ψ i ​ θ j ​ χ ​ ( ( [i, j])) ​ [i, j] − s, G q ​ ( s) = ∑ i ≤ W, j ≤ W θ i ​ θ j ​ [i, j] − s, \displaystyle=\sum_{i\leq V,\ j\leq W}\psi_{i}\theta_{j}\chi\bigl(([i,j])\bigr)[i,j]^{-s},\ \ G_{q}(s)=\sum_{i\leq W,\ j\leq W}\theta_{i}\theta_{j}[i,j]^{-s}, |  |

(5.9) |  | S ⁡ ( Y) \displaystyle S(Y) | = ∑ n = 1 ∞ Ψ ( n) ϑ ( n) χ ( n) n − ϱ e − n / Y = 1 2 ​ π ​ i ∫ ( 1) L ( s + ϱ, χ) F ( s + ϱ) Γ ( s) Y s d s, \displaystyle=\sum^{\infty}_{n=1}\Psi(n)\vartheta(n)\chi(n)n^{-\varrho}e^{-n/Y}=\frac{1}{2\pi i}\int\limits_{(1)}L(s+\varrho,\chi)F(s+\varrho)\Gamma(s)Y^{s}ds, |  |

where [i, j] [i,j] denotes the least common multiple of i i and j j ( Re ​ ϱ = β \mathrm{Re}\,\varrho=\beta). We move the line of integration in ( 5.9) to Re ​ s = 1 − β − 1 / k \mathrm{Re}\,s=1-\beta-1/k with k = ⌈ 4 ​ ε − 1 ⌉ k=\lceil 4\varepsilon^{-1}\rceil, and obtain analogously to p. 318 of [9] the estimate

(5.10) |  | S ⁡ ( X) ≪ ( q φ ​ V ​ W ​ X − 1) 1 / k ​ q 1 / k 2 ​ ℒ 3 ​ X 1 − β ≪ ( q φ ​ V ​ W ​ X − 1) 1 / k ​ q 2 k 2 − ε 1 ≪ q − ε 1 S(X)\ll(q^{\varphi}VWX^{-1})^{1/k}q^{1/k^{2}}\mathcal{L}^{3}X^{1-\beta}\ll(q^{\varphi}VWX^{-1})^{1/k}q^{\frac{2}{k^{2}}-\varepsilon_{1}}\ll q^{-\varepsilon_{1}} |  |

in view of 1 − β ≤ ε 1 / x 1-\beta\leq\varepsilon_{1}/x, F ⁡ ( s + ϱ) ≪ ∑ n ≤ V ​ W d 2 ​ ( n) ​ n − 1 + 1 / k ≪ ( V ​ W) 1 / k ​ ℒ 3 F(s+\varrho)\ll\sum\limits_{n\leq VW}d^{2}(n)n^{-1+1/k}\ll(VW)^{1/k}\mathcal{L}^{3} and

(5.11) |  | x − v − w − φ = x 0 − u 0 − c 2 − w − φ = ε > 2 / k, x-v-w-\varphi=x_{0}-u_{0}-c_{2}-w-\varphi=\varepsilon>2/k, |  |

analogously to (11.8)–(11.10) of [9], and (3.24)–(3.27) of [17].

The relation Ψ ⁡ ( n) = 0 \Psi(n)=0 for 2 ≤ n ≤ U ​ ℒ 2 = U ¯ 2\leq n\leq U\mathcal{L}^{2}=\overline{U} implies

(5.12) |  | S ( U) = e − 1 / U + O ( ∑ n > ℒ 2 ​ U d 2 ( n) e − n / U) = 1 + O ( 1 U). S(U)=e^{-1/U}+O\biggl(\sum_{n>\mathcal{L}^{2}U}d^{2}(n)e^{-n/U}\biggr)=1+O\left(\frac{1}{U}\right). |  |

This and ( 5.10) yield

(5.13) |  | ∑ n = 1 ∞ Ψ ( n) ϑ ( n) ( e − n / X − e − n / U) χ ( n) n − ϱ = − 1 + O ( q − ε 1). \sum^{\infty}_{n=1}\Psi(n)\vartheta(n)\bigl(e^{-n/X}-e^{-n/U}\bigr)\chi(n)n^{-\varrho}=-1+O(q^{-\varepsilon_{1}}). |  |

We will use now Halász’ inequality in the simple form given by Lemma 1.7 of [15], with

(5.14) |  | a n \displaystyle a_{n} | = Ψ ⁡ ( n) ​ ϑ ​ ( n) ​ n − 1 2 ​ ( e − n X − e − n U) \displaystyle=\Psi(n)\vartheta(n)n^{-\frac{1}{2}}\bigl(e^{-\frac{n}{X}}-e^{-\frac{n}{U}}\bigr) |  |

 | b n \displaystyle b_{n} | = ϑ 2 ​ ( n) ​ ( e − n X − e − n U), s j = ϱ j − 1 2. \displaystyle=\vartheta^{2}(n)\bigl(e^{-\frac{n}{X}}-e^{-\frac{n}{U}}\bigr),\quad s_{j}=\varrho_{j}-\frac{1}{2}. |  |

 | ξ = ( Ψ ⁡ ( n) ​ n − 1 2 ​ e − n / X − e − n / U) n = 1 ∞, φ j = ( b n ​ χ j ​ ( n) ​ n − s j) n = 1 ∞ \xi=\Bigl(\Psi(n)n^{-\frac{1}{2}}\sqrt{e^{-n/X}-e^{-n/U}}\Bigr)^{\infty}_{n=1},\quad\varphi_{j}=\Bigl(\sqrt{b_{n}}\chi_{j}(n)n^{-s_{j}}\Bigr)^{\infty}_{n=1} |  |

 | ( φ j, ξ) = f ⁡ ( s j, χ j) = ∑ n = 1 ∞ a n ​ χ j ​ ( n) ​ n − s j (\varphi_{j},\xi)=f(s_{j},\chi_{j})=\sum^{\infty}_{n=1}a_{n}\chi_{j}(n)n^{-s_{j}} |  |

 | ( φ i, φ j) = B ⁡ ( s i + s ¯ j, χ i ​ χ ¯ j), B ⁡ ( s, χ) = ∑ n = 1 ∞ b n ​ χ ​ ( n) ​ n − s. (\varphi_{i},\varphi_{j})=B\bigl(s_{i}+\overline{s}_{j},\chi_{i}\overline{\chi}_{j}\bigr),\quad B(s,\chi)=\sum^{\infty}_{n=1}b_{n}\chi(n)n^{-s}. |  |

Here we have analogously to [9], (11.14) and [17], (3.32)

(5.15) |  | ‖ ξ ‖ 2 = ∑ n = 1 ∞ | a n | 2 b n \displaystyle\|\xi\|^{2}=\sum^{\infty}_{n=1}\frac{|a_{n}|^{2}}{b_{n}} | = ( 1 + O ⁡ ( 1 / ℒ)) ​ 2 ​ x − u − v 2 ​ ( v − u) = ( 1 + O ⁡ ( 1 ℒ)) ​ 𝒞 0, \displaystyle=\bigl(1+O(1/\mathcal{L})\bigr)\frac{2x-u-v}{2(v-u)}=\left(1+O\left(\frac{1}{\mathcal{L}}\right)\right)\mathcal{C}_{0}, |  |

 | 𝒞 0 \displaystyle\mathcal{C}_{0} | = 2 ​ φ + 2 ​ c 1 + c 2 2 ​ c 2. \displaystyle=\frac{2\varphi+2c_{1}+c_{2}}{2c_{2}}. |  |

Any term with χ i ​ χ ¯ j ≠ χ 0 \chi_{i}\overline{\chi}_{j}\neq\chi_{0} ( χ 0 \chi_{0} is the principal character mod ​ q \mathrm{mod}\,q) will be, similarly to ( 5.10), in case of Theorem C

(5.16) |  | B ⁡ ( s i + s ¯ j, χ i ​ χ ¯ j) \displaystyle B(s_{i}+\overline{s}_{j},\chi_{i}\overline{\chi}_{j}) | = ∑ n = 1 ∞ ϑ 2 ​ ( n) ​ χ i ​ χ ¯ j ​ ( n) ​ ( e − n X − e − n U) ​ n − ( ϱ i + ϱ ¯ j − 1) \displaystyle=\sum^{\infty}_{n=1}\vartheta^{2}(n)\chi_{i}\overline{\chi}_{j}(n)\bigl(e^{-\frac{n}{X}}-e^{-\frac{n}{U}}\bigr)n^{-(\varrho_{i}+\overline{\varrho}_{j}-1)} |  |

 |  | ≪ ( q φ ​ W 2 ​ U − 1) 1 k ​ q 2 k 2 ≪ q − ε 1 \displaystyle\ll(q^{\varphi}W^{2}U^{-1})^{\frac{1}{k}}q^{\frac{2}{k^{2}}}\ll q^{-\varepsilon_{1}} |  |

whereas in case of Theorem D:

(5.17) |  | B ⁡ ( s i + s ¯ j, χ i ​ χ ¯ j) ≪ ( W 2 ​ U − 1) 1 k ​ q 2 k 3 ≪ q − ε 1. B(s_{i}+\overline{s}_{j},\chi_{i}\overline{\chi}_{j})\ll(W^{2}U^{-1})^{\frac{1}{k}}q^{\frac{2}{k^{3}}}\ll q^{-\varepsilon_{1}}. |  |

If χ i ​ χ ¯ j = χ 0 \chi_{i}\overline{\chi}_{j}=\chi_{0}, that is, χ i = χ j \chi_{i}=\chi_{j}, then, similarly to (3.35)–(3.38) of [17], we have

(5.18) |  | B ⁡ ( s i + s ¯ j, χ 0) = φ ⁡ ( q) q ​ G q ​ ( 1) ​ Γ ​ ( 2 − ϱ i − ϱ ¯ j) ​ ( X 2 − ϱ i − ϱ ¯ j − U 2 − ϱ i − ϱ ¯ j) + O ⁡ ( q − ε 1) B(s_{i}+\overline{s}_{j},\chi_{0})=\frac{\varphi(q)}{q}G_{q}(1)\Gamma(2-\varrho_{i}-\overline{\varrho}_{j})\bigl(X^{2-\varrho_{i}-\overline{\varrho}_{j}}-U^{2-\varrho_{i}-\overline{\varrho}_{j}}\bigr)+O(q^{-\varepsilon_{1}}) |  |

where the real quantity G q ​ ( 1) G_{q}(1) satisfies

(5.19) |  | | φ ⁡ ( q) q ​ G q ​ ( 1) | ≤ 1 + O ⁡ ( 1 / ℒ) w ​ ℒ, \left|\frac{\varphi(q)}{q}G_{q}(1)\right|\leq\frac{1+O(1/\mathcal{L})}{w\mathcal{L}}, |  |

by the Proposition after (3.36) in [17].

Until now we followed quite closely [9], Section 11 and [17]. The above considerations were valid for all values ε, c 1, c 2, κ, x 0, η \varepsilon,c_{1},c_{2},\kappa,x_{0},\eta, which determine the values of the remaining parameters u 0 u_{0}, x 0 x_{0}, v v, w w, u u and x x. Now we will take an average over η \eta with 0 ≤ η ≤ κ 0\leq\eta\leq\kappa.

Using Halász’s inequality (Lemma 1.7 of [15]) with the notation

(5.20) |  | w j = w ⁡ ( ϱ j) = e − 2 ​ x 1 ​ λ j − κ + r 2 ​ d j z i, j = ℒ ⁡ ( 2 − ϱ i − ϱ ¯ j) = ℒ ⁡ ( δ i + δ j + i ⁡ ( γ j − γ i)) = λ i + λ j + i ⁡ ( μ j − μ i) \begin{gathered}w_{j}=w(\varrho_{j})=e^{-2x_{1}\lambda_{j}-\frac{\kappa+r}{2}d_{j}}\\ z_{i,j}=\mathcal{L}(2-\varrho_{i}-\overline{\varrho}_{j})=\mathcal{L}(\delta_{i}+\delta_{j}+i(\gamma_{j}-\gamma_{i}))=\lambda_{i}+\lambda_{j}+i(\mu_{j}-\mu_{i})\end{gathered} |  |

we obtain from the relations ( 5.1)–( 5.4), ( 5.13)–( 5.19) with C 1 = C 0 / c 1 C_{1}=C_{0}/c_{1}, after taking average in η ∈ [0, κ] \eta\in[0,\kappa] which affects x, u, X, U x,u,X,U.

(5.21) |  | ( 1 + O ⁡ ( ε)) ​ ( ∑ j = 1 J w j) 2 = 1 + O ⁡ ( ε) κ ​ ∫ 0 κ ( ∑ j = 1 J w j) 2 ​ 𝑑 η ≤ C 1 ​ ∑ j = 1 J w j ​ ∑ i ∼ j w i ​ | ℋ ⁡ ( z j, i) | (1+O(\varepsilon))\biggl(\sum^{J}_{j=1}w_{j}\biggr)^{2}=\frac{1+O(\varepsilon)}{\kappa}\int\limits_{0}^{\kappa}\biggl(\sum_{j=1}^{J}w_{j}\biggr)^{2}d\eta\leq C_{1}\sum^{J}_{j=1}w_{j}\sum_{i\sim j}w_{i}|\mathcal{H}(z_{j,i})| |  |

where we write i ∼ j i\sim j if ϱ i \varrho_{i} and ϱ j \varrho_{j} are zeros of the same L ⁡ ( s, χ) L(s,\chi) and

(5.22) |  | | ℋ ⁡ ( z) |: \displaystyle|\mathcal{H}(z)|: | = | Γ ⁡ ( z / ℒ) | ℒ ⋅ 1 κ ​ | ( e x 0 ​ z − e u 0 ​ z) ​ e κ ​ z − 1 z | \displaystyle=\frac{|\Gamma(z/\mathcal{L})|}{\mathcal{L}}\cdot\frac{1}{\kappa}\left|\bigl(e^{x_{0}z}-e^{u_{0}z}\bigr)\frac{e^{\kappa z}-1}{z}\right| |  |

 |  | = 1 + O ⁡ ( ε) κ ​ | e ( x 0 + κ) ​ z ​ ( 1 − e − r ​ z) ​ ( 1 − e − κ ​ z) z 2 | \displaystyle=\frac{1+O(\varepsilon)}{\kappa}\left|e^{(x_{0}+\kappa)z}\frac{(1-e^{-rz})(1-e^{-\kappa z})}{z^{2}}\right| |  |

 |  | ≤ 1 + O ⁡ ( ε) κ ​ e x 1 ​ a ​ | 1 − e − r ​ z z | ​ | 1 − e − κ ​ z z | =: 1 + O ⁡ ( ε) κ ​ ℋ 1 ​ ( z) \displaystyle\leq\frac{1+O(\varepsilon)}{\kappa}e^{x_{1}a}\left|\frac{1-e^{-rz}}{z}\right|\,\left|\frac{1-e^{-\kappa z}}{z}\right|=:\frac{1+O(\varepsilon)}{\kappa}\mathcal{H}_{1}(z) |  |

if Re ​ z = a \mathrm{Re}\,z=a.

We call the attention of the reader to the fact that while the value of the LHS of ( 5.21) is independent of η \eta (up to O ⁡ ( ε) O(\varepsilon)) the RHS would actually depend on η \eta. This dependence disappears only after taking the integral over η \eta and this phase is represented already in the form given on the RHS of ( 5.21).

In order to estimate for a given fixed zero ϱ j \varrho_{j} belonging to a given χ ≠ χ 0 \chi\neq\chi_{0}, say, the sum over all terms ℋ 1 ​ ( z j, i) \mathcal{H}_{1}(z_{j,i}) ( ϱ i = ϱ χ) (\varrho_{i}=\varrho_{\chi}) we introduce the notation (cf. [9], p. 325) (with new parameters ω \omega and λ \lambda, ω = κ \omega=\kappa or r r)

 | f 1 ​ ( t) = { sinh ⁡ ( ( ω − t) ​ λ) for ​ 0 ≤ t ≤ ω 0 for ​ t ≥ ω, f_{1}(t)=\begin{cases}\sinh((\omega-t)\lambda)&\text{for }0\leq t\leq\omega\\ 0&\text{for }t\geq\omega\end{cases}, |  |

(5.23) |  | F 1, ω ​ ( z) = F 1 ​ ( z) \displaystyle F_{1,\omega}(z)=F_{1}(z) | = ∫ 0 ∞ e − z ​ t ​ f 1 ​ ( t) ​ 𝑑 t = 1 2 ​ { e ω ​ λ λ + z + e − ω ​ λ λ − z − 2 ​ λ ​ e − ω ​ z λ 2 − z 2 } \displaystyle=\int\limits^{\infty}_{0}e^{-zt}f_{1}(t)dt=\frac{1}{2}\left\{\frac{e^{\omega\lambda}}{\lambda+z}+\frac{e^{-\omega\lambda}}{\lambda-z}-\frac{2\lambda e^{-\omega z}}{\lambda^{2}-z^{2}}\right\} |  |

 | F 2, ω ​ ( z) = F 2 ​ ( z) \displaystyle F_{2,\omega}(z)=F_{2}(z) | = ( 1 − e − ω ​ z z) 2. \displaystyle=\left(\frac{1-e^{-\omega z}}{z}\right)^{2}. |  |

As in (13.2) of [9] we see that

(5.24) |  | Re ​ F 1 ​ ( z) ≥ λ ​ e ω ​ λ 2 ​ | F 2 ​ ( λ + z) | for ​ Re ​ z ≥ 0, \mathrm{Re}\,F_{1}(z)\geq\frac{\lambda e^{\omega\lambda}}{2}|F_{2}(\lambda+z)|\ \ \text{ for }\ \mathrm{Re}\,z\geq 0, |  |

because the relation ( 5.24) holds with equality for Re ​ z = 0 \mathrm{Re}\,z=0 and therefore, by Lemma 4.1 of [9], ( 5.24) holds for the whole halfplane Re ​ z ≥ 0 \mathrm{Re}\,z\geq 0.

Choosing the parameter λ \lambda in ( 5.23) as

(5.25) |  | λ = λ j, \lambda=\lambda_{j}, |  |

we obtain for a fixed j j by ( 5.24) (the summation runs over zeros of L ⁡ ( s, χ) L(s,\chi))

(5.26) |  |  | ∑ i; i ∼ j | γ i − γ j | < ℒ − 1 / 2 | F 2 ( λ j + λ i + i ( μ j − μ i) | \displaystyle\sum_{\begin{subarray}{c}i;i\sim j\\ |\gamma_{i}-\gamma_{j}|<\mathcal{L}^{-1/2}\end{subarray}}\bigl|F_{2}(\lambda_{j}+\lambda_{i}+i(\mu_{j}-\mu_{i})\bigr| |  |

 |  | ≤ 2 λ j ​ e − ω ​ λ j ​ ∑ i; i ∼ j | γ i − γ j | < ℒ − 1 / 2 Re ​ F 1 ​ ( ( s j − ϱ i) ​ ℒ) \displaystyle\leq\frac{2}{\lambda_{j}}e^{-\omega\lambda_{j}}\sum_{\begin{subarray}{c}i;i\sim j\\ |\gamma_{i}-\gamma_{j}|<\mathcal{L}^{-1/2}\end{subarray}}\mathrm{Re}\,F_{1}\bigl((s_{j}-\varrho_{i})\mathcal{L}\bigr) |  |

where s j = 1 + i ​ γ j s_{j}=1+i\gamma_{j}.

The contribution of all terms with | γ i − γ ℓ | > ℒ − 1 / 2 |\gamma_{i}-\gamma_{\ell}|>\mathcal{L}^{-1/2} (consequently | μ i − μ j | > ℒ 1 / 2 |\mu_{i}-\mu_{j}|>\mathcal{L}^{1/2}) for any ℓ \ell is clearly by well known log-free density theorems

(5.27) |  | ≪ ( ∑ w j) 2 ​ e ( x 0 + κ) ​ e 3 ​ Λ ∞ ℒ < ε ​ ( ∑ w i) 2. \ll\Bigl(\sum w_{j}\Bigr)^{2}e^{(x_{0}+\kappa)}\frac{e^{3\Lambda_{\infty}}}{\mathcal{L}}<\varepsilon\Bigl(\sum w_{i}\Bigr)^{2}. |  |

Applying the last displayed formula of the proof of Lemma 13.2 of [9]:

(5.28) |  |  | ∑ i; i ∼ j | γ i − γ j | < ℒ − 1 / 2 Re ​ F 1 ​ ( ( s j − ϱ i) ​ ℒ) \displaystyle\sum_{\begin{subarray}{c}i;i\sim j\\ |\gamma_{i}-\gamma_{j}|<\mathcal{L}^{-1/2}\end{subarray}}\mathrm{Re}\,F_{1}\bigl((s_{j}-\varrho_{i})\mathcal{L}\bigr) |  |

 |  | ≤ f 1 ​ ( 0) ​ ( φ 2 + ε) − ℒ − 1 ​ ∑ n = 1 ∞ Λ ⁡ ( n) ​ Re ​ ( χ ⁡ ( n) n s j) ​ f 1 ​ ( log ⁡ n ℒ) \displaystyle\leq f_{1}(0)\left(\frac{\varphi}{2}+\varepsilon\right)-\mathcal{L}^{-1}\sum^{\infty}_{n=1}\Lambda(n)\mathrm{Re}\,\left(\frac{\chi(n)}{n^{s_{j}}}\right)f_{1}\left(\frac{\log n}{\mathcal{L}}\right) |  |

 |  | ≤ f 1 ​ ( 0) ​ ( φ 2 + ε) + ℒ − 1 ​ ∑ n = 1 ∞ Λ ⁡ ( n) ​ χ 0 ​ ( n) n ​ f 1 ​ ( log ⁡ n ℒ) \displaystyle\leq f_{1}(0)\left(\frac{\varphi}{2}+\varepsilon\right)+\mathcal{L}^{-1}\sum^{\infty}_{n=1}\Lambda(n)\frac{\chi_{0}(n)}{n}f_{1}\left(\frac{\log n}{\mathcal{L}}\right) |  |

 |  | ≤ f 1 ​ ( 0) ​ ( φ 2 + ε) + F 1 ​ ( 0) + ε. \displaystyle\leq f_{1}(0)\left(\frac{\varphi}{2}+\varepsilon\right)+F_{1}(0)+\varepsilon. |  |

So, we obtain finally from ( 5.26)–( 5.28) for any fixed j j

(5.29) |  | ∑ i; i ∼ j | γ i − γ j | < ℒ − 1 / 2 | F 2 ​ ( z i, j) | \displaystyle\sum_{\begin{subarray}{c}i;i\sim j\\ |\gamma_{i}-\gamma_{j}|<\mathcal{L}^{-1/2}\end{subarray}}|F_{2}(z_{i,j})| | ≤ φ 2 ​ ( 1 − e − 2 ​ ω ​ λ j λ j) + ( 1 − e − ω ​ λ j λ j) 2 + ε \displaystyle\leq\frac{\varphi}{2}\left(\frac{1-e^{-2\omega\lambda_{j}}}{\lambda_{j}}\right)+\left(\frac{1-e^{-\omega\lambda_{j}}}{\lambda_{j}}\right)^{2}+\varepsilon |  |

 |  | =: B φ, ω ​ ( λ j) + ε. \displaystyle=:B_{\varphi,\omega}(\lambda_{j})+\varepsilon. |  |

This, together with ( 5.21), ( 5.22), ( 5.23) and ( 5.27) yields

(5.30) |  |  | ( 1 + O ⁡ ( ε)) ​ ( ∑ j w j) 2 \displaystyle(1+O(\varepsilon))\biggl(\sum_{j}w_{j}\biggr)^{2} |  |

 |  | = ( 1 + O ⁡ ( ε)) ​ ( ∑ j e − 2 ​ x 1 ​ λ j − r + κ 2 ​ d j) 2 \displaystyle=(1+O(\varepsilon))\biggl(\sum_{j}e^{-2x_{1}\lambda_{j}-\frac{r+\kappa}{2}d_{j}}\biggr)^{2} |  |

 |  | ≤ C 1 ​ κ − 1 ​ ∑ j ∑ i ∼ j | γ i − γ j | < ℒ − 1 / 2 e − 2 ​ x 1 ​ ( λ i + λ j) − r + κ 2 ​ ( d i + d j) ​ e x 1 ​ ( λ i + λ j) ​ | F 2, κ ​ ( z i, j) ​ F 2, r ​ ( z i, j) | \displaystyle\leq C_{1}\kappa^{-1}\sum_{j}\!\!\sum_{\begin{subarray}{c}i\sim j\\ |\gamma_{i}-\gamma_{j}|<\mathcal{L}^{-1/2}\end{subarray}}\!\!e^{-2x_{1}(\lambda_{i}+\lambda_{j})-\frac{r+\kappa}{2}(d_{i}+d_{j})}e^{x_{1}(\lambda_{i}\!+\!\lambda_{j})}\sqrt{|F_{2,\kappa}(z_{i,j})F_{2,r}(z_{i,j})|} |  |

 |  | = C 1 ​ κ − 1 ​ ∑ j ∑ i ∼ j | γ i − γ j | < ℒ − 1 / 2 e − x 1 ​ ( λ i + λ j) − r + κ 2 ​ ( d i + d j) ​ | F 2, κ ​ ( z i, j) ​ F 2, r ​ ( z i, j) |. \displaystyle=C_{1}\kappa^{-1}\sum_{j}\sum_{\begin{subarray}{c}i\sim j\\ |\gamma_{i}-\gamma_{j}|<\mathcal{L}^{-1/2}\end{subarray}}e^{-x_{1}(\lambda_{i}+\lambda_{j})-\frac{r+\kappa}{2}(d_{i}+d_{j})}\sqrt{|F_{2,\kappa}(z_{i,j})F_{2,r}(z_{i,j})|}. |  |

Taking into account that

(5.31) |  | 1 − e − x x \frac{1-e^{-x}}{x} |  |

is monotonically decreasing for x ≥ 0 x\geq 0, we obtain that

(5.32) |  | e − ω ​ d j ​ B φ, ω ​ ( λ j) = B φ, ω ​ ( λ j) ≤ B φ, ω ​ ( Λ) for ​ λ j ≥ Λ. e^{-\omega d_{j}}B_{\varphi,\omega}(\lambda_{j})=B_{\varphi,\omega}(\lambda_{j})\leq B_{\varphi,\omega}(\Lambda)\quad\text{ for }\ \lambda_{j}\geq\Lambda. |  |

Further, as

(5.33) |  | e x − e − x x \frac{e^{x}-e^{-x}}{x} |  |

is monotonically increasing for x ≥ 0 x\geq 0, so is e ω ​ λ ​ B φ, ω ​ ( λ) e^{\omega\lambda}B_{\varphi,\omega}(\lambda). Hence we obtain for λ j ≤ Λ \lambda_{j}\leq\Lambda

(5.34) |  | e − ω ​ d j ​ B φ, ω ​ ( λ j) = e − ω ​ Λ ​ e ω ​ λ j ​ B φ, ω ​ ( λ j) ≤ B φ, ω ​ ( Λ). e^{-\omega d_{j}}B_{\varphi,\omega}(\lambda_{j})=e^{-\omega\Lambda}e^{\omega\lambda_{j}}B_{\varphi,\omega}(\lambda_{j})\leq B_{\varphi,\omega}(\Lambda). |  |

Now using the trivial relation | F 2 ​ ( z i, j) | = | F 2 ​ ( z j, i) | |F_{2}(z_{i,j})|=|F_{2}(z_{j,i})|, by 2 ​ a ​ b ≤ a 2 + b 2 2ab\leq a^{2}+b^{2} we obtain from ( 5.31)–( 5.34), ( 5.29) and the Cauchy inequality

(5.35) |  |  | ∑ j ∑ i ∼ j | γ i − γ j | < ℒ − 1 / 2 e − x 1 ​ ( λ i + λ j) − r + κ 2 ​ ( d i + d j) ​ | F 2, κ ​ ( z i, j) | ​ | F 2, r ​ ( z i, j) | \displaystyle\sum_{j}\sum_{\begin{subarray}{c}i\sim j\\ |\gamma_{i}-\gamma_{j}|<\mathcal{L}^{-1/2}\end{subarray}}e^{-x_{1}(\lambda_{i}+\lambda_{j})-\frac{r+\kappa}{2}(d_{i}+d_{j})}\sqrt{|F_{2,\kappa}(z_{i,j})|\,|F_{2,r}(z_{i,j})|} |  |

 |  | ≤ ∑ j e − 2 ​ x 1 ​ λ j − r + κ 2 ​ d j ​ ( ∑ i; i ∼ j | γ i − γ j | < ℒ − 1 / 2 e − κ ​ d j ​ | F 2, κ ​ ( z i, j) |) 1 2 ​ ( ∑ i; i ∼ j | γ i − γ j | < ℒ − 1 / 2 e − r ​ d j ​ F 2, r ​ ( z i, j)) 1 2 \displaystyle\leq\!\sum_{j}e^{-2x_{1}\lambda_{j}-\frac{r+\kappa}{2}d_{j}}\biggl(\!\sum_{\begin{subarray}{c}i;i\sim j\\ |\gamma_{i}-\gamma_{j}|<\mathcal{L}^{-1/2}\end{subarray}}\!\!\!\!e^{-\kappa d_{j}}|F_{2,\kappa}(z_{i,j})|\!\biggr)^{\!\!\frac{1}{2}}\!\biggl(\!\sum_{\begin{subarray}{c}i;i\sim j\\ |\gamma_{i}-\gamma_{j}|<\mathcal{L}^{-1/2}\end{subarray}}\!\!\!\!e^{-rd_{j}}F_{2,r}(z_{i,j})\!\!\biggr)^{\!\!\frac{1}{2}} |  |

 |  | ≤ ( ∑ j w j) ​ ( B φ, κ ​ ( Λ) ​ B φ, r ​ ( Λ) + ε). \displaystyle\leq\biggl(\sum_{j}w_{j}\biggr)\Bigl(\sqrt{B_{\varphi,\kappa}(\Lambda)B_{\varphi,r}(\Lambda)}+\varepsilon\Bigr). |  |

Consequently, from ( 5.30) and ( 5.35) we have

(5.36) |  | ∑ j w j ≤ ( 1 + O ⁡ ( ε)) ​ C 1 ​ B φ, κ ​ ( Λ) ​ B φ, r ​ ( Λ) / κ = ( 1 + O ⁡ ( ε)) ​ C 2 ​ ( φ, κ, Λ), \sum_{j}w_{j}\leq(1+O(\varepsilon))C_{1}\sqrt{B_{\varphi,\kappa}(\Lambda)B_{\varphi,r}(\Lambda)}/\kappa=(1+O(\varepsilon))C_{2}(\varphi,\kappa,\Lambda), |  |

which proves Theorems C and D.

## 6 Properties of the G G -function

The following two lemmas show that the problem of showing Condition 2 for the G G -function defined in ( 4.19) can be reduced to its validity in a bounded region. In the first 3 lemmas we will use explicit forms of G ⁡ ( z) G(z) and G ′ ​ ( z) G^{\prime}(z) as follows:

(6.1) |  | G ⁡ ( z) \displaystyle G(z) | = 16 15 ​ z − 8 3 ​ z 3 + 4 z 4 − 4 z 6 + 4 ​ e − 2 ​ z z 4 ​ ( z + 1 z) 2, \displaystyle=\frac{16}{15z}-\frac{8}{3z^{3}}+\frac{4}{z^{4}}-\frac{4}{z^{6}}+\frac{4e^{-2z}}{z^{4}}\left(\frac{z+1}{z}\right)^{2}, |  |

(6.2) |  | G ′ ​ ( z) \displaystyle G^{\prime}(z) | = − 16 15 ​ z 2 + 8 z 4 − 16 z 5 + 24 z 7 − 8 ​ e − 2 ​ z z 4 ​ ( 1 + 4 z + 6 z 2 + 3 z 3). \displaystyle=-\frac{16}{15z^{2}}+\frac{8}{z^{4}}-\frac{16}{z^{5}}+\frac{24}{z^{7}}-\frac{8e^{-2z}}{z^{4}}\left(1+\frac{4}{z}+\frac{6}{z^{2}}+\frac{3}{z^{3}}\right). |  |

The integral form of G ⁡ ( z) G(z) in ( 4.19) and g ⁡ ( u) ≥ 0 g(u)\geq 0 trivially implies that for real x ∈ R x\in R

(6.3) |  | G ( x) > 0, G ′ ( x) < 0, G ′′ ( x) > 0, …. G(x)>0,\quad G^{\prime}(x)<0,\quad G^{\prime\prime}(x)>0,\dots\ . |  |

Let z = a + i ​ t z=a+it and let us examine for fixed t t the behaviour of the functions

(6.4) |  | Ψ t ​ ( a) \displaystyle\Psi_{t}(a) | = Re ​ G ​ ( a + i ​ t) G ⁡ ( a) \displaystyle=\frac{\mathrm{Re}\,G(a+it)}{G(a)} |  |

(6.5) |  | Φ t ​ ( a) \displaystyle\Phi_{t}(a) | = Re ​ G ′ ​ ( z) ⋅ G ⁡ ( a) − Re ​ G ​ ( z) ⋅ G ′ ​ ( a) = G 2 ​ ( a) ​ d ​ Ψ t ​ ( a) d ​ a. \displaystyle=\mathrm{Re}\,G^{\prime}(z)\cdot G(a)-\mathrm{Re}\,G(z)\cdot G^{\prime}(a)=G^{2}(a)\frac{d\Psi_{t}(a)}{da}. |  |

###### Lemma 1.

For 0 ≤ a ≤ 13 0\leq a\leq 13, | t | ≥ 14 |t|\geq 14 we have

(6.6) |  | Φ t ​ ( a) > 9 ​ G ​ ( a) | z | 4 > 0. \Phi_{t}(a)>\frac{9G(a)}{|z|^{4}}>0. |  |

Proof. Since for Re ​ z ≥ 0 \mathrm{Re}\,z\geq 0, we have Re ​ G ​ ( z) ≥ 0 \mathrm{Re}\,G(z)\geq 0 (cf. ( 4.22)) and 0 < G ⁡ ( a) < 1 0<G(a)<1 it is sufficient to prove

(6.7) |  | Re ​ G ′ ​ ( z) > 9 | z | 4. \mathrm{Re}\,G^{\prime}(z)>\frac{9}{|z|^{4}}. |  |

From ( 6.2) and ( 4.25) we obtain by | e − 2 ​ z | ≤ 1 |e^{-2z}|\leq 1, G ⁡ ( a) ≤ G ⁡ ( 0) = 8 / 9 G(a)\leq G(0)=8/9 as claimed above. Further,

(6.8) |  | Re ​ G ′ ​ ( z) \displaystyle\mathrm{Re}\,G^{\prime}(z) | ≥ 16 | z | 4 ​ ( 1 15 ​ ( t 2 − a 2) − 1 − 3 | z | − 3 | z | 2 − 3 | z | 3) \displaystyle\geq\frac{16}{|z|^{4}}\left(\frac{1}{15}(t^{2}-a^{2})-1-\frac{3}{|z|}-\frac{3}{|z|^{2}}-\frac{3}{|z|^{3}}\right) |  |

 |  | ≥ 16 | z | 4 ​ ( 27 15 − 1 − 3 14 − 3 14 2 − 3 14 3) > 9 | z | 4 \displaystyle\geq\frac{16}{|z|^{4}}\left(\frac{27}{15}-1-\frac{3}{14}-\frac{3}{14^{2}}-\frac{3}{14^{3}}\right)>\frac{9}{|z|^{4}} |  |

###### Lemma 2.

For a = − b ∈ [− 1.25, 0] a=-b\in[-1.25,\,0], | t | ≥ 50 |t|\geq 50 we have

(6.9) |  | Φ t ​ ( a) > G ⁡ ( − b) 25 ​ | z | 2. \Phi_{t}(a)>\frac{G(-b)}{25|z|^{2}}. |  |

Proof. We will use the notation h ⁡ ( b) = 8 9 ​ G ​ ( − b) + b ​ G ′ ​ ( − b) h(b)=\frac{8}{9}G(-b)+bG^{\prime}(-b). Then

(6.10) |  | h ′ ​ ( b) = G ′ ​ ( − b) 9 − b ​ G ′′ ​ ( − b) < 0, h^{\prime}(b)=\frac{G^{\prime}(-b)}{9}-bG^{\prime\prime}(-b)<0, |  |

and hence

(6.11) |  | h ⁡ ( b) ≥ h ⁡ ( 1.25) > 1 / 90 ​ for ​ b ∈ [0, 1.25]. h(b)\geq h(1.25)>1/90\ \text{ for }\ b\in[0,\,1.25]. |  |

Further, by simple computation

(6.12) |  | G ⁡ ( − b) ≥ G ⁡ ( 0) = 8 9, | G ′ ​ ( − b) | ≤ | G ′ ​ ( − 1.25) | < 1.36. G(-b)\geq G(0)=\frac{8}{9},\ |G^{\prime}(-b)|\leq|G^{\prime}(-1.25)|<1.36. |  |

Now, from ( 6.1), ( 6.2), ( 6.5), and ( 6.10)–( 6.12)

(6.13) |  | G ⁡ ( − b) ≥ max ⁡ ( 9 8 ​ b ​ | G ′ ​ ( − b) |, 0.65 ​ | G ′ ​ ( − b) |) G(-b)\geq\max\left(\frac{9}{8}b|G^{\prime}(-b)|,\,0.65|G^{\prime}(-b)|\right) |  |

we obtain

(6.14) |  |  | Φ t ​ ( − b) \displaystyle\Phi_{t}(-b) |  |

 |  | ≥ 16 ​ G ​ ( − b) 15 ​ | z | 2 ​ ( − ( b / t) 2 + ( b / t) 2 − 7.5 | z | 2 ​ ( 1 + 2 | z | + 3 | z | 3 + e 2.5 ​ ( + 4 | z | + 6 | z | 2 + 3 | z | 3))) \displaystyle\geq\frac{16G(-b)}{15|z|^{2}}\left(\frac{1\!-\!(b/t)^{2}}{1\!+\!(b/t)^{2}}-\frac{7.5}{|z|^{2}}\left(\!1+\frac{2}{|z|}+\frac{3}{|z|^{3}}\!+\!e^{2.5}\!\left(\!1\!+\frac{4}{|z|}+\frac{6}{|z|^{2}}+\frac{3}{|z|^{3}}\!\right)\!\right)\!\right) |  |

 |  | − 16 ​ | G ′ ​ ( − b) | 15 ​ | z | 2 ​ ( b + 3.75 | z | 2 ​ ( 1 + 2 | z | 2 + 2 ​ b 3 ​ | z | 2 + e 2.5 ​ t 2 + 1 t 2)) \displaystyle\quad-\frac{16|G^{\prime}(-b)|}{15|z|^{2}}\left(b+\frac{3.75}{|z|^{2}}\left(1+\frac{2}{|z|^{2}}+\frac{2b}{3|z|^{2}}+e^{2.5}\frac{t^{2}+1}{t^{2}}\right)\right) |  |

 |  | ≥ 16 ​ G ​ ( − b) 15 ​ | z | 2 ​ ( 0.957 − 8 9 − 1.55 ⋅ 0.015) > G ⁡ ( − b) 25 ​ | z | 2. \displaystyle\geq\frac{16G(-b)}{15|z|^{2}}\left(0.957-\frac{8}{9}-1.55\cdot 0.015\right)>\frac{G(-b)}{25|z|^{2}}. |  |

The following lemma reduces the range for numerical check

###### Lemma 3.

If | t | ≥ 8 |t|\geq 8, Re ​ z = − b ∈ [− 1.25, − 0.14] \text{\rm Re }z=-b\in[-1.25,-0.14], then

(6.15) |  | Re ​ G ​ ( z) < − 1 140 ​ | z | 2. \mathrm{Re}\,G(z)<-\frac{1}{140|z|^{2}}. |  |

Proof. Since | z + 1 z | 2 = ( 1 − b) 2 + t 2 6 2 + t 2 ≤ 1 + 1 | z | 2 ≤ 65 64 \left|\frac{z+1}{z}\right|^{2}=\frac{(1-b)^{2}+t^{2}}{6^{2}+t^{2}}\leq 1+\frac{1}{|z|^{2}}\leq\frac{65}{64} and Re ​ z − 3 = | z | − 6 ​ b ​ ( 3 ​ t 2 − b 2) > 0 \mathrm{Re}\,z^{-3}=|z|^{-6}b(3t^{2}-b^{2})>0 we obtain

(6.16) |  | Re ​ G ​ ( z) \displaystyle\mathrm{Re}\,G(z) | ≤ 1 | z | 2 ​ ( − 16 15 ​ b + 4 | z | 2 ​ ( 1 + 1 | z | 2 + e 2 ​ b ​ | z + 1 z | 2)) \displaystyle\leq\frac{1}{|z|^{2}}\left(-\frac{16}{15}b+\frac{4}{|z|^{2}}\left(1+\frac{1}{|z|^{2}}+e^{2b}\left|\frac{z+1}{z}\right|^{2}\right)\right) |  |

 |  | ≤ − 1 15 ​ | z | 2 ​ ( 16 ​ b − 60 64 ⋅ 65 64 ​ ( e 2 ​ b + 1)). \displaystyle\leq\frac{-1}{15|z|^{2}}\left(16b-\frac{60}{64}\cdot\frac{65}{64}(e^{2b}+1)\right). |  |

The function

(6.17) |  | h ⁡ ( b) = 16 ​ b − 975 1024 ​ ( e 2 ​ b + 1) h(b)=16b-\frac{975}{1024}(e^{2b}+1) |  |

is increasing for b < b 0 = 1 2 ​ ln ⁡ 8192 975 b<b_{0}=\frac{1}{2}\ln\frac{8192}{975} and decreasing for b > b 0 b>b_{0}, so its minimum in [0.14, 1.25] [0.14,1.25] is

(6.18) |  | min ⁡ ( h ⁡ ( 0.14), h ⁡ ( 1.25)) = 0.028 ​ ⋯ > 0. \min\bigl(h(0.14),h(1.25)\bigr)=0.028\dots>0. |  |

Q.E.D.

Now we will prove a lemma, which proves Condition 2 for the restricted range | t | ≤ π / 2 |t|\leq\pi/2 for A 0, B 0 = ∞ A_{0},B_{0}=\infty and for an arbitrary function F ⁡ ( z) F(z) satisfying

(6.19) |  | F ⁡ ( z) = ∫ 0 2 e − z ​ v ​ f ​ ( v) ​ 𝑑 v with ​ f ​ ( v) ≥ 0. F(z)=\int\limits^{2}_{0}e^{-zv}f(v)dv\quad\text{ with }\ f(v)\geq 0. |  |

###### Lemma 4.

Φ t ​ ( x) = Re ​ F ​ ( x + i ​ t) / F ⁡ ( x) \Phi_{t}(x)=\mathrm{Re}\,F(x+it)/F(x) is monotonically increasing in x x for all x ∈ ℝ x\in\mathbb{R}, if | t | ≤ π / 2 |t|\leq\pi/2 and F F satisfies ( 6.19).

Proof. Let

(6.20) |  | k ⁡ ( v) = f ⁡ ( v) ​ e − x ​ v, h ⁡ ( u, x) = ∫ 0 u k ⁡ ( v) ​ 𝑑 v, q u ​ ( x) = h ⁡ ( u, x) F ⁡ ( x). k(v)=f(v)e^{-xv},\quad h(u,x)=\int\limits^{u}_{0}k(v)dv,\quad q_{u}(x)=\frac{h(u,x)}{F(x)}. |  |

From ( 6.19) we obtain by partial integration

(6.21) |  | Re ​ F ​ ( x + i ​ t) \displaystyle\mathrm{Re}\,F(x+it) | = [h ⁡ ( u, x) ​ cos ⁡ ( u ​ t)] 0 2 − ∫ 0 2 h ⁡ ( u, x) ​ ( − t ​ sin ⁡ ( u ​ t)) ​ 𝑑 u \displaystyle=\bigl[h(u,x)\cos(ut)\bigr]^{2}_{0}-\int\limits^{2}_{0}h(u,x)(-t\sin(ut))du |  |

 |  | = F ⁡ ( x) ​ cos ⁡ 2 ​ t + ∫ 0 2 h ⁡ ( u, x) ​ t ​ sin ⁡ ( u ​ t) ​ 𝑑 u, \displaystyle=F(x)\cos 2t+\int\limits^{2}_{0}h(u,x)t\sin(ut)du, |  |

(6.22) |  | Φ t ​ ( x) = cos ⁡ 2 ​ t + ∫ 0 2 q u ​ ( x) ​ ( t ​ sin ⁡ ( u ​ t)) ​ 𝑑 u. \Phi_{t}(x)=\cos 2t+\int\limits^{2}_{0}q_{u}(x)(t\sin(ut))du. |  |

Since for | t | ≤ π / 2 |t|\leq\pi/2, u ∈ [0, 2] u\in[0,2] we have t ​ sin ⁡ ( u ​ t) ≥ 0 t\sin(ut)\geq 0. Hence, in order to show the lemma, it is sufficient to prove

(6.23) |  | d d ​ x ​ q u ​ ( x) ≥ 0 for ​ u ∈ [0, 2]. \frac{d}{dx}q_{u}(x)\geq 0\quad\text{for }\ u\in[0,2]. |  |

The property f ⁡ ( v) ≥ 0 f(v)\geq 0 implies

(6.24) |  | F 2 ​ ( x) ​ d d ​ x ​ q u ​ ( x) \displaystyle F^{2}(x)\frac{d}{dx}q_{u}(x) | = − ∫ 0 u k ( v) v d v ∫ 0 2 k ( y) d y + ∫ 0 u k ( y) d y ∫ 0 2 k ( v) v d v \displaystyle=-\int\limits^{u}_{0}k(v)vdv\int\limits^{2}_{0}k(y)dy+\int\limits^{u}_{0}k(y)dy\int\limits^{2}_{0}k(v)vdv |  |

 |  | = ∫ u 2 k ⁡ ( v) ​ v ​ 𝑑 v ​ ∫ 0 u k ⁡ ( y) ​ 𝑑 y − ∫ u 2 k ⁡ ( y) ​ 𝑑 y ​ ∫ 0 u k ⁡ ( v) ​ v ​ 𝑑 v \displaystyle=\int\limits^{2}_{u}k(v)vdv\int\limits^{u}_{0}k(y)dy-\int\limits^{2}_{u}k(y)dy\int\limits^{u}_{0}k(v)vdv |  |

 |  | ≥ u ⁡ ( ∫ u 2 k ⁡ ( v) ​ 𝑑 v ​ ∫ 0 u k ⁡ ( y) ​ 𝑑 y − ∫ u 2 k ⁡ ( y) ​ 𝑑 y ​ ∫ 0 u k ⁡ ( v) ​ 𝑑 v) = 0. \displaystyle\geq u\biggl(\int\limits^{2}_{u}k(v)dv\int\limits^{u}_{0}k(y)dy-\int\limits^{2}_{u}k(y)dy\int\limits^{u}_{0}k(v)dv\!\biggr)\!=0. |  |

Q.E.D.

Finally, we can check the remaining range by computer and verify Condition 2 for the G G -function with A 0 = 13 A_{0}=13, B 0 = 1.25 B_{0}=1.25.

###### Lemma 5.

The function G ⁡ ( z) G(z) in ( 4.19) satisfies

(6.25) |  | Re ​ G ​ ( a + i ​ t) G ⁡ ( a) ≥ Re ​ G ​ ( − b + i ​ t) G ⁡ ( − b) \frac{\mathrm{Re}\,G(a+it)}{G(a)}\geq\frac{\mathrm{Re}\,G(-b+it)}{G(-b)} |  |

for any t ∈ R t\in R if 0 ≤ a ≤ 13 0\leq a\leq 13, 0 ≤ b ≤ 1.25 0\leq b\leq 1.25.

The proof follows from Lemmas 1 – 4 and from a computer check of ( 6.25) (using Maple) for

(6.26) |  | a \displaystyle a | = 0, \displaystyle=0,\ \  |  | 0 ≤ b ≤ 0.14 \displaystyle 0\leq b\leq 0.14\ \  |  | for ​ 14 ≤ | t | < 50, \displaystyle\text{ for }\ \,14\leq|t|<50, |  |

(6.27) |  | 0 \displaystyle 0 | ≤ a ≤ 13, \displaystyle\leq a\leq 13,\ \  |  | 0 ≤ b ≤ 0.14 \displaystyle 0\leq b\leq 0.14\ \  |  | for 8 ≤ | t | < 14, \displaystyle\text{ for }\,\phantom{88}8\leq|t|<14, |  |

(6.28) |  | 0 \displaystyle 0 | ≤ a ≤ 13, \displaystyle\leq a\leq 13, |  | 0 ≤ b ≤ 1.25 \displaystyle 0\leq b\leq 1.25 |  | for ​ π / 2 < | t | < 8. \displaystyle\text{ for }\pi/2<|t|<8. |  |

## 7 Proof of Theorems H and I

Let

(7.1) |  | ϱ j = β j + i γ j = 1 − δ j + i γ j = 1 + ℒ − 1 ( − λ j + i μ j), j = 1, 2, …, N = N ( λ) \varrho_{j}=\beta_{j}+i\gamma_{j}=1-\delta_{j}+i\gamma_{j}=1+\mathcal{L}^{-1}(-\lambda_{j}+i\mu_{j}),\quad j=1,2,\dots,N=N(\lambda) |  |

be the zeros of the L ⁡ ( s, χ j) L(s,\chi_{j}) functions mod ​ q \mathrm{mod}\,q (counted with multiplicity if L ⁡ ( ϱ, χ) = L ⁡ ( ϱ, χ ′) L(\varrho,\chi)=L(\varrho,\chi^{\prime}) or ϱ \varrho is a multiple zero of some L ⁡ ( s, χ) L(s,\chi))

(7.2) |  | λ 0 ≤ λ j ≤ Λ, | γ j | ≤ L ⇔ | μ j | ≤ ℒ ​ L, L ≤ ℒ. \lambda_{0}\leq\lambda_{j}\leq\Lambda,\quad|\gamma_{j}|\leq L\Leftrightarrow|\mu_{j}|\leq\mathcal{L}L,\quad L\leq\mathcal{L}. |  |

Since ζ ⁡ ( s) \zeta(s) has no zero in the region above we can assume χ ≠ χ 0 \chi\neq\chi_{0}. The notation k ∼ j k\sim j will denote that ϱ k \varrho_{k} and ϱ j \varrho_{j} are zeros of the same L ⁡ ( s, χ) L(s,\chi). Further, suppose that the L L -functions belonging to the distinct characters χ ( ν) \chi^{(\nu)} ( 1 ≤ ν ≤ m) (1\leq\nu\leq m) have exactly N ν N_{\nu} zeros in the above region (counted with multiplicity). Then clearly N = N 1 + N 2 + ⋯ + N m N=N_{1}+N_{2}+\dots+N_{m}. Let us denote the set of zeros of L ⁡ ( s, χ) L(s,\chi) in ( 7.2) by Z ⁡ ( χ) Z(\chi). Further, let for any j ∈ [1, N] j\in[1,N] and with a function F = F x = G ⁡ ( z / x) F=F_{x}=G(z/x) (cf. ( 4.16)–( 4.17) and ( 4.26)–( 4.27))

(7.3) |  | a k, j = Re ​ F ​ ( λ k − λ 0 + i ⁡ ( μ j − μ k)) F ⁡ ( λ k − λ 0), b k, j = Re ​ F ​ ( − λ 0 + i ⁡ ( μ j − μ k)) F ⁡ ( − λ 0) a_{k,j}=\frac{\mathrm{Re}\,F(\lambda_{k}-\lambda_{0}+i(\mu_{j}-\mu_{k}))}{F(\lambda_{k}-\lambda_{0})},\quad b_{k,j}=\frac{\mathrm{Re}\,F(-\lambda_{0}+i(\mu_{j}-\mu_{k}))}{F(-\lambda_{0})} |  |

(7.4) |  | A k = ∑ ′ j j ∼ k ​ a k, j, B k = ∑ ′ j j ∼ k ​ b k, j, ψ k = F ⁡ ( λ k − λ 0) F ⁡ ( − λ 0), A_{k}=\underset{\begin{subarray}{c}j\\ j\sim k\end{subarray}}{\sum\nolimits^{\prime}}a_{k,j},\qquad B_{k}=\underset{\begin{subarray}{c}j\\ j\sim k\end{subarray}}{\sum\nolimits^{\prime}}b_{k,j},\qquad\psi_{k}=\frac{F(\lambda_{k}-\lambda_{0})}{F(-\lambda_{0})}, |  |

(7.5) |  | N ′ ℓ = ∑ ϱ k ∈ Z ⁡ ( χ ℓ) A k, N ′ = ∑ m ℓ = 1 N ′ ℓ = ∑ N j = 1 A j, ψ = F ⁡ ( λ − λ 0) F ⁡ ( − λ 0), ξ = f ⁡ ( 0) ​ φ 2 ​ F ​ ( − λ 0), Δ = ψ − ξ, \begin{gathered}N^{\prime}_{\ell}=\sum_{\varrho_{k}\in Z(\chi_{\ell})}A_{k},\quad N^{\prime}=\sum^{m}_{\ell=1}N^{\prime}_{\ell}=\sum^{N}_{j=1}A_{j},\\ \psi=\frac{F(\lambda-\lambda_{0})}{F(-\lambda_{0})},\quad\xi=\frac{f(0)\varphi}{2F(-\lambda_{0})},\ \ \Delta=\psi-\xi,\end{gathered} |  |

where the ∑ ′ \sum^{\prime} sign means in ( 7.4) the extra condition | λ j + i ⁡ ( μ j − μ k) | < ℒ ​ δ |\lambda_{j}+i(\mu_{j}-\mu_{k})|<\mathcal{L}\delta where δ = δ ⁡ ( ε) \delta=\delta(\varepsilon) is a sufficiently small constant.

Conditions 1, 2 (see ( 4.16)–( 4.17) and ( 4.26)–( 4.27)) and the definitions show that

(7.6) |  | a k, j ≥ b k, j, a k, j ≥ 0, a k, k = 1, a_{k,j}\geq b_{k,j},\quad a_{k,j}\geq 0,\quad a_{k,k}=1, |  |

consequently for every k = 1, 2, …, N k=1,2,\dots,N

(7.7) |  | A k ≥ B k, A k ≥ 1, N ℓ ′ ≥ N ℓ, N ′ ≥ N. A_{k}\geq B_{k},\quad A_{k}\geq 1,\quad N^{\prime}_{\ell}\geq N_{\ell},\quad N^{\prime}\geq N. |  |

Let K ⁡ ( s, χ) K(s,\chi) be defined as in [9] (p. 285, after (6.2))

(7.8) |  | K ⁡ ( s, χ) = ∑ r = 1 ∞ Λ ⁡ ( n) ​ Re ​ ( χ ⁡ ( n) n s) ​ f ​ ( log ⁡ n ℒ) K(s,\chi)=\sum_{r=1}^{\infty}\Lambda(n)\text{\rm Re }\left(\frac{\chi(n)}{n^{s}}\right)f\left(\frac{\log n}{\mathcal{L}}\right) |  |

with a function f ⁡ ( u) = f x ​ ( u) = x ​ g ​ ( u ​ x) f(u)=f_{x}(u)=xg(ux) as in ( 4.18) and ( 4.23) connected to F ⁡ ( z) F(z) by ( 4.24). (We will omit the lower index x x to f f, F F and K K which might change often depending on the particular problem.)

Following [9], Section 12 we will apply Lemma 5.2 of [9] with the above function K K. So we obtain for any ϱ j \varrho_{j} in ( 7.1) with β 0 = 1 − ℒ − 1 ​ λ 0 \beta_{0}=1-\mathcal{L}^{-1}\lambda_{0} by λ j ≥ λ 0 \lambda_{j}\geq\lambda_{0}

(7.9) |  | K ( β 0 + i γ j, χ j) ≤ − ℒ ∑ k k ∼ j | λ k + i ⁡ ( μ j − μ k) | < ℒ ​ δ Re F ( λ k − λ 0 + i ( μ j − μ k)) + f ( 0) ( φ 2 + ε 2) ℒ. K(\beta_{0}+i\gamma_{j},\chi_{j})\leq-\mathcal{L}\!\!\!\!\sum_{\begin{subarray}{c}k\\ k\sim j\\ |\lambda_{k}+i(\mu_{j}-\mu_{k})|<\mathcal{L}\delta\end{subarray}}\!\!\!\!\!\mathrm{Re}\,F\bigl(\lambda_{k}-\lambda_{0}+i(\mu_{j}-\mu_{k})\bigr)+f(0)\left(\frac{\varphi}{2}+\frac{\varepsilon}{2}\right)\mathcal{L}. |  |

Extending the summation for all zeros in ( 7.2) with | λ k + i ⁡ ( μ j − μ k) | ≥ ℒ ​ δ |\lambda_{k}+i(\mu_{j}-\mu_{k})|\geq\mathcal{L}\delta and using the relations 0 ≤ λ k − λ 0 ≤ 13 ​ x 0\leq\lambda_{k}-\lambda_{0}\leq 13x we have in these cases by ( 6.1)

(7.10) |  | F ⁡ ( λ k − λ 0 + i ⁡ ( μ j − μ k)) ≪ 1 | μ j − μ k | ≪ 1 ℒ ​ δ. F\bigl(\lambda_{k}-\lambda_{0}+i(\mu_{j}-\mu_{k})\bigr)\ll\frac{1}{|\mu_{j}-\mu_{k}|}\ll\frac{1}{\mathcal{L}\delta}. |  |

Since the number of terms being uniformly bounded by Jutila’s density theorem

(7.11) |  | N ( 1 − Λ / ℒ, ℒ, q) ≪ ε ( q ℒ) ( 2 + ε) ​ Λ / ℒ ≪ e 3 ​ Λ ≪ 1, N(1-\Lambda/\mathcal{L},\mathcal{L},q)\ll_{\varepsilon}(q\mathcal{L})^{(2+\varepsilon)\Lambda/\mathcal{L}}\ll e^{3\Lambda}\ll 1, |  |

including the other zeros in the summation on the right-hand side of ( 7.9) leads to an additional error of size O ⁡ ( δ − 1) = o ⁡ ( ℒ) O(\delta^{-1})=o(\mathcal{L}). Thus we obtain from this modified form of ( 7.9), after summation for all j ∈ ( 1, N) j\in(1,N)

(7.12) |  |  | ℒ ⁡ { ∑ j ≤ N ( ( ∑ k k ∼ j a k, j ​ ψ k) ​ F ​ ( − λ 0) − f ⁡ ( 0) ​ φ 2 − ε) } \displaystyle\mathcal{L}\Biggl\{\sum_{j\leq N}\Biggl(\biggl(\sum_{\begin{subarray}{c}k\\ k\sim j\end{subarray}}a_{k,j}\psi_{k}\biggr)F(-\lambda_{0})-\frac{f(0)\varphi}{2}-\varepsilon\Biggr)\Biggr\} |  |

 |  | ≤ − ∑ j ≤ N K ( β 0 + i γ j, χ j) \displaystyle\leq-\sum_{j\leq N}K(\beta_{0}+i\gamma_{j},\chi_{j}) |  |

 |  | = − ∑ n = 1 ∞ Λ ( n) χ 0 ( n) n − β 0 f ( ℒ − 1 log n) Re { ∑ j ≤ N χ j ( n) n − i ​ γ j } \displaystyle=-\sum^{\infty}_{n=1}\Lambda(n)\chi_{0}(n)n^{-\beta_{0}}f(\mathcal{L}^{-1}\log n)\mathrm{Re}\biggl\{\sum_{j\leq N}\chi_{j}(n)n^{-i\gamma_{j}}\biggr\} |  |

 |  | ≤ ∑ n = 1 ∞ Λ ⁡ ( n) ​ χ 0 ​ ( n) ​ n − β 0 ​ f ​ ( ℒ − 1 ​ log ⁡ n) ​ | ∑ j ≤ N χ j ​ ( n) ​ n − i ​ γ j |. \displaystyle\leq\sum^{\infty}_{n=1}\Lambda(n)\chi_{0}(n)n^{-\beta_{0}}f(\mathcal{L}^{-1}\log n)\biggl|\sum_{j\leq N}\chi_{j}(n)n^{-i\gamma_{j}}\biggr|. |  |

Using ( 4.31) we obtain

(7.13) |  | F ⁡ ( − λ 0) ≥ F ⁡ ( Λ − λ 0) ≥ f ⁡ ( 0) ​ ( φ / 2 + ε). F(-\lambda_{0})\geq F(\Lambda-\lambda_{0})\geq f(0)(\varphi/2+\varepsilon). |  |

Interchanging the order of summation on the left-hand side of ( 7.12), we obtain from ( 7.12), by A k ≥ 1 A_{k}\geq 1

(7.14) |  | ℒ 2 { ∑ k ≤ N ( ψ k ( ∑ j j ∼ k a k, j) F ( − λ 0) − f ( 0) φ / 2 − ε) } 2 ≤ ∑ 1 ∑ 2, \mathcal{L}^{2}\Biggl\{\sum_{k\leq N}\biggl(\psi_{k}\biggl(\sum_{\begin{subarray}{c}j\\ j\sim k\end{subarray}}a_{k,j}\biggr)F(-\lambda_{0})-f(0)\varphi/2-\varepsilon\biggr)\Biggr\}^{2}\leq\sum\nolimits_{1}\sum\nolimits_{2}, |  |

where, using Lemma 5.3 of [9]

(7.15) |  | ∑ 1 = ∑ n = 1 ∞ Λ ( n) χ 0 ( n) n − β 0 f ( ℒ − 1 log n) = K ( β 0, χ 0) = ℒ ( F ( − λ 0) + o ( 1)) \sum\nolimits_{1}=\sum^{\infty}_{n=1}\Lambda(n)\chi_{0}(n)n^{-\beta_{0}}f(\mathcal{L}^{-1}\log n)=K(\beta_{0},\chi_{0})=\mathcal{L}\bigl(F(-\lambda_{0})+o(1)\bigr) |  |

and

(7.16) |  | ∑ 2 \displaystyle\sum\nolimits_{2} | = ∑ n = 1 ∞ Λ ⁡ ( n) ​ χ 0 ​ ( n) ​ n − β 0 ​ f ​ ( ℒ − 1 ​ log ⁡ n) ​ | ∑ j ≤ N χ j ​ ( n) ​ n − i ​ γ j | 2 \displaystyle=\sum^{\infty}_{n=1}\Lambda(n)\chi_{0}(n)n^{-\beta_{0}}f(\mathcal{L}^{-1}\log n)\biggl|\sum_{j\leq N}\chi_{j}(n)n^{-i\gamma_{j}}\biggr|^{2} |  |

 |  | = ∑ j, k ≤ N K ⁡ ( β 0 + i ⁡ ( γ j − γ k), χ j ​ χ ¯ k) \displaystyle=\sum_{j,k\leq N}K\bigl(\beta_{0}+i(\gamma_{j}-\gamma_{k}),\chi_{j}\overline{\chi}_{k}\bigr) |  |

since the above value is real. By Lemma 5.3 of [9] we have by ( 7.3)–( 7.7) for any fixed k k for the terms with j ∼ k j\sim k a sum

(7.17) |  | ∑ j j ∼ k K ⁡ ( β 0 + i ⁡ ( γ j − γ k), χ 0) \displaystyle\sum_{\begin{subarray}{c}j\\ j\sim k\end{subarray}}K\bigl(\beta_{0}+i(\gamma_{j}\!-\!\gamma_{k}),\chi_{0}\bigr) | = ∑ j j ∼ k ℒ ⁡ { Re ​ F ​ ( − λ 0 + i ⁡ ( μ j − μ k)) + o ⁡ ( 1) } \displaystyle=\sum_{\begin{subarray}{c}j\\ j\sim k\end{subarray}}\mathcal{L}\bigl\{\mathrm{Re}\,F(-\lambda_{0}+i(\mu_{j}-\mu_{k}))+o(1)\bigr\} |  |

 |  | = ℒ ⁡ { B k ​ F ​ ( − λ 0) + o ⁡ ( 1) } ≤ ℒ ⁡ { A k ​ F ​ ( − λ 0) + o ⁡ ( 1) }. \displaystyle=\mathcal{L}\bigl\{B_{k}F(-\lambda_{0})+o(1)\bigr\}\leq\mathcal{L}\bigl\{A_{k}F(-\lambda_{0})+o(1)\bigr\}. |  |

Again, by Lemma 5.2 of [9], we obtain in case of Theorem H for the total contribution of all other terms the estimate

(7.18) |  | ∑ j, k ≤ N k ≁ j K ⁡ ( β 0 + i ⁡ ( γ j − γ k), χ j ​ χ ¯ k) ≤ ℒ ⁡ ( f ⁡ ( 0) ​ φ 2 + ε) ​ ∑ κ, ν ≤ m κ ≠ ν N ν ​ N κ, \sum_{\begin{subarray}{c}j,k\leq N\\ k\not\sim j\end{subarray}}K\bigl(\beta_{0}+i(\gamma_{j}-\gamma_{k}),\chi_{j}\overline{\chi}_{k}\bigr)\leq\mathcal{L}\left(\frac{f(0)\varphi}{2}+\varepsilon\right)\sum_{\begin{subarray}{c}\kappa,\nu\leq m\\ \kappa\neq\nu\end{subarray}}N_{\nu}N_{\kappa}, |  |

while in case of Theorem I we obtain

(7.19) |  | ∑ j, k ≤ N k ≁ j K ⁡ ( β 0 + i ⁡ ( γ j − γ k), χ j ​ χ ¯ k) ≤ ε ​ ℒ ​ ∑ κ, ν ≤ m κ ≠ ν N ν ​ N κ. \sum_{\begin{subarray}{c}j,k\leq N\\ k\not\sim j\end{subarray}}K\bigl(\beta_{0}+i(\gamma_{j}-\gamma_{k}),\chi_{j}\overline{\chi}_{k}\bigr)\leq\varepsilon\mathcal{L}\sum_{\begin{subarray}{c}\kappa,\nu\leq m\\ \kappa\neq\nu\end{subarray}}N_{\nu}N_{\kappa}. |  |

Dividing ( 7.14) by ( ℒ ​ F ​ ( − λ 0)) 2 (\mathcal{L}F(-\lambda_{0}))^{2} we obtain from ( 7.15)–( 7.18) with the choice of a new ε 1 \varepsilon_{1},

(7.20) |  | ( ∑ k ≤ N ( A k ​ ψ k − ξ)) 2 ≤ ∑ k ≤ N A k + ξ ​ ∑ κ, ν ≤ m k ≠ ν N ν ​ N κ + ε 1 ​ ( N ′) 2. \biggl(\sum_{k\leq N}(A_{k}\psi_{k}-\xi)\biggr)^{2}\leq\sum_{k\leq N}A_{k}+\xi\sum_{\begin{subarray}{c}\kappa,\nu\leq m\\ k\neq\nu\end{subarray}}N_{\nu}N_{\kappa}+\varepsilon_{1}(N^{\prime})^{2}. |  |

Consequently, by A k ≥ 1 A_{k}\geq 1, ψ k ≥ ψ \psi_{k}\geq\psi, N ≤ N ′ N\leq N^{\prime} and ( 7.5), ( 7.7), ( 7.13) we have

(7.21) |  | ( N ′ ​ Δ) 2 ≤ N ′ + ξ ⁡ ( N ′ 2 − N ′) + ε 1 ​ ( N ′) 2, (N^{\prime}\Delta)^{2}\leq N^{\prime}+\xi({N^{\prime}}^{2}-N^{\prime})+\varepsilon_{1}(N^{\prime})^{2}, |  |

(7.22) |  | N ≤ N ′ ≤ 1 − ξ Δ 2 − ξ − ε 1 N\leq N^{\prime}\leq\frac{1-\xi}{\Delta^{2}-\xi-\varepsilon_{1}} |  |

in case of Theorem H. Similarly, in case of Theorem I we have

(7.23) |  | ( N ′ ​ Δ) 2 ≤ N ′ + ε 1 ​ ( N ′) 2, (N^{\prime}\Delta)^{2}\leq N^{\prime}+\varepsilon_{1}(N^{\prime})^{2}, |  |

(7.24) |  | N ≤ N ′ ≤ 1 Δ 2 − ε 1. N\leq N^{\prime}\leq\frac{1}{\Delta^{2}-\varepsilon_{1}}. |  |

Q.E.D.

## 8 Proof of Theorems J, K and L

In order to show our weighted density theorem (Theorem K) we will use the notation of Section 7 with the additional quantity

(8.1) |  | D ′ = def ∑ j ≤ N ( A j ​ ( ψ j − ψ)) ≥ D = def ∑ j ≤ N ( ψ j − ψ) ≥ 0. D^{\prime}\stackrel{{\scriptstyle{\rm def}}}{{=}}\sum_{j\leq N}\bigl(A_{j}(\psi_{j}-\psi)\bigr)\geq D\stackrel{{\scriptstyle{\rm def}}}{{=}}\sum_{j\leq N}(\psi_{j}-\psi)\geq 0. |  |

This quantity, completely neglected in the proofs of Theorems H and I, will be our crucial one in the following. We will start from ( 7.20) to obtain, instead of ( 7.21)–( 7.22):

(8.2) |  | ( N ′ ​ Δ + D ′) 2 ≤ N ′ + ξ ⁡ ( N ′ 2 − N ′) + ε 1 ​ ( N ′) 2 (N^{\prime}\Delta+D^{\prime})^{2}\leq N^{\prime}+\xi({N^{\prime}}^{2}-N^{\prime})+\varepsilon_{1}(N^{\prime})^{2} |  |

(8.3) |  | ( N ′) 2 ​ ( Δ 2 − ξ − ε 1) + N ′ ​ ( 2 ​ Δ ​ D ′) ≤ N ′ ​ ( 1 − ξ) (N^{\prime})^{2}(\Delta^{2}-\xi-\varepsilon_{1})+N^{\prime}(2\Delta D^{\prime})\leq N^{\prime}(1-\xi) |  |

from which, by ξ < Δ 2 \xi<\Delta^{2}, we obtain

(8.4) |  | D ≤ D ′ ≤ 1 − ξ 2 ​ Δ − ε 1. D\leq D^{\prime}\leq\frac{1-\xi}{2\Delta-\varepsilon_{1}}. |  |

Suppose now that λ 0 \lambda_{0} is given, the λ j \lambda_{j} ’s ( 1 ≤ j ≤ N) (1\leq j\leq N) and their number N N are unknown quantities with

(8.5) |  | d j = def Λ − λ j ≥ 0, d 1 ≥ d 2 ≥ ⋯ ≥ d N, d_{j}\stackrel{{\scriptstyle{\rm def}}}{{=}}\Lambda-\lambda_{j}\geq 0,\quad d_{1}\geq d_{2}\geq\dots\geq d_{N}, |  |

with prescribed conditions

(8.6) |  | 0 ≤ d j ≤ e j e 1 ≥ e 2 ≥ ⋯ ≥ e N. 0\leq d_{j}\leq e_{j}\qquad e_{1}\geq e_{2}\geq\dots\geq e_{N}. |  |

We will suppose that f f and F F are the functions of Section 4 with the parameter x x satisfying

(8.7) |  | 2 / x ≤ B ⇔ x ≥ 2 / B. 2/x\leq B\Leftrightarrow x\geq 2/B. |  |

Since by Corollary 2 or by Jutila’s density theorem [10] we know that the unknown number N N is bounded by some absolute constant R ∈ ℤ R\in\mathbb{Z}, we can suppose that in our extremal problem N = R N=R by the introduction of additional trivial terms with e j = 0 e_{j}=0 (consequently d j = 0 d_{j}=0) for N < j ≤ R N<j\leq R. These new trivial terms do not change the values of D D and those of S S and D ∗ D^{*}, defined below

(8.8) |  | D ∗ = D ⋅ F ⁡ ( − λ 0) \displaystyle D^{*}=D\cdot F(-\lambda_{0}) | = ∑ j = 1 N ( F ⁡ ( λ j − λ 0) − F ⁡ ( Λ − λ 0)) \displaystyle=\sum^{N}_{j=1}\bigl(F(\lambda_{j}-\lambda_{0})-F(\Lambda-\lambda_{0})\bigr) |  |

 |  | = ∑ j = 1 R ( F ⁡ ( d 0 − d j) − F ⁡ ( d 0)). \displaystyle=\sum^{R}_{j=1}\bigl(F(d_{0}-d_{j})-F(d_{0})\bigr). |  |

Then, under the constraint D ≤ C ~ ′ D\leq\widetilde{C}^{\prime} we are looking for an upper bound for the quantity

(8.9) |  | S = ∑ j = 1 R ( e B ​ d j − e C ​ d j) = ∑ j = 1 N ( e B ​ d j − e C ​ d j), S=\sum^{R}_{j=1}(e^{Bd_{j}}-e^{Cd_{j}})=\sum^{N}_{j=1}(e^{Bd_{j}}-e^{Cd_{j}}), |  |

with the side constraints ( 8.5)–( 8.6) and B > C ≥ 0 B>C\geq 0, where R R is now a fixed, large constant. The upper bound will naturally depend on B B, C C and C ′ C^{\prime} but not on R R.

Let

(8.10) |  | T = t 0 ( f), b = B T ≥ 1, 0 ≤ c = C T < b, Y j = e e j ​ T ≥ y j = e d j ​ T ≥ 1, h 1 ( y) = y v, h 2 ( y) = y b − y c. \begin{gathered}T=t_{0}(f),\ \ b=\frac{B}{T}\geq 1,\ \ 0\leq c=\frac{C}{T}<b,\\ Y_{j}=e^{e_{j}T}\geq y_{j}=e^{d_{j}T}\geq 1,\ \ h_{1}(y)=y^{v},\ \ h_{2}(y)=y^{b}-y^{c}.\end{gathered} |  |

Then we have with the above notation

(8.11) |  | D 1 ∗ ​ ( y):= ∑ j = 1 R F ⁡ ( d 0 − d j) = T ​ ∫ 0 1 f ⁡ ( v ​ T) ​ e − d 0 ​ v ​ T ​ ∑ j = 1 R y j v ​ 𝑑 v. D^{*}_{1}(y):=\sum^{R}_{j=1}F(d_{0}-d_{j})=T\int\limits^{1}_{0}f(vT)e^{-d_{0}vT}\sum^{R}_{j=1}y^{v}_{j}\,dv. |  |

The following observation is sufficient to show Theorem K.

Proposition. If y ≥ z > 1 y\geq z>1, η > 0 \eta>0, 0 < v < 1 0<v<1, b ≥ 1 b\geq 1, 0 ≤ c < b 0\leq c<b, then

(8.12) |  | H i ​ ( y, z, η) = h i ​ ( y + η) + h i ​ ( z − η) − ( h i ​ ( y) + h i ​ ( z)) ​ < > ​ 0 ​ for ​ i = 1, i = 2. H_{i}(y,z,\eta)=h_{i}(y+\eta)+h_{i}(z-\eta)-\bigl(h_{i}(y)+h_{i}(z)\bigr)\begin{aligned} &<\\ &>\end{aligned}\ 0\text{ for }\begin{aligned} &i=1,\\ &i=2.\end{aligned} |  |

Proof. h 1 ′ ​ ( y) h^{\prime}_{1}(y) is decreasing, h 2 ′ ​ ( y) h^{\prime}_{2}(y) is increasing for y ≥ 1 y\geq 1 due to

(8.13) |  | h 1 ′′ ​ ( y) = v ⁡ ( v − 1) ​ y v − 2 < 0, h 2 ′′ ​ ( y) = b ⁡ ( b − 1) ​ y b − 2 − c ⁡ ( c − 1) ​ y c − 2 > 0. h^{\prime\prime}_{1}(y)=v(v-1)y^{v-2}<0,\quad h^{\prime\prime}_{2}(y)=b(b-1)y^{b-2}-c(c-1)y^{c-2}>0. |  |

Consequently,

(8.14) |  | H i ​ ( y, z, η) = ∫ 0 η ( h i ′ ​ ( y + t) − h i ′ ​ ( z − η + t)) ​ 𝑑 t ​ < > ​ 0 ​ for ​ i = 1, i = 2. H_{i}(y,z,\eta)=\int\limits^{\eta}_{0}\bigl(h^{\prime}_{i}(y+t)-h^{\prime}_{i}(z-\eta+t)\bigr)dt\begin{aligned} &<\\ &>\end{aligned}\ 0\text{ for }\begin{aligned} &i=1,\\ &i=2.\end{aligned} |  |

The proposition means that if we have a given configuration of the variables { y j } j = 1 R \{y_{j}\}^{R}_{j=1} with y i ≥ y i + 1 y_{i}\geq y_{i+1}, Y i ≥ Y i + 1 Y_{i}\geq Y_{i+1}, Y i ≥ y i ≥ 1 Y_{i}\geq y_{i}\geq 1, then this configuration cannot yield a maximum for the h 2 ∗ ​ ( y ¯) = ∑ j = 1 R h 2 ​ ( y j) h^{*}_{2}(\underline{y})=\sum\limits^{R}_{j=1}h_{2}(y_{j}) if there is a possibility to increase the distance between two variables among y 1, …, y R y_{1},\dots,y_{R}. According to this, let r r be the largest index with y r > 1 y_{r}>1 in the maximal system { y i } i = 1 R \{y_{i}\}^{R}_{i=1}. Then necessarily

(8.15) |  | y i = Y i ⇔ d i = e i for ​ i = 1, …, r − 1. y_{i}=Y_{i}\Leftrightarrow d_{i}=e_{i}\quad\text{ for }\ i=1,\dots,r-1. |  |

Namely, otherwise we could change with a small η > 0 \eta>0 y k \,y_{k} to y k + η y_{k}+\eta, y r y_{r} to y r − η y_{r}-\eta and obtain a larger value for h 2 ∗ ​ ( y ¯) h^{*}_{2}(\underline{y}) if k k is defined by

(8.16) |  | k = min ⁡ { ν; y ν < Y ν }, k=\min\{\nu;\ y_{\nu}<Y_{\nu}\}, |  |

while the corresponding function h 1 ∗ ​ ( y ¯) = ∑ j = 1 R y j v h^{*}_{1}(\underline{y})=\sum\limits^{R}_{j=1}y^{v}_{j}, and consequently D 1 ∗ ​ ( y ¯) D^{*}_{1}(\underline{y}) would decrease and thus D ∗ ≤ D ~ D^{*}\leq\widetilde{D} would still hold for the new system y ¯ \underline{y}. This proves Theorem K.

In order to show Theorem L, taking into account Remark 5, suppose that the first index, for which in the maximum case we do not have equality in ( 4.47) is k ∈ [1, M] k\in[1,M]. The case k = M k=M is clearly impossible since then we could increase y k y_{k} in view of d k < d k − 1 d_{k}<d_{k-1} which follows by ( 4.48) from

(8.17) |  | F ⁡ ( d 0 − d k) − F ⁡ ( d 0) < c ⁡ ( k) − c ⁡ ( k − 1) ≤ c ⁡ ( k − 1) − c ⁡ ( k − 2) = F ⁡ ( d 0 − d k − 1) − F ⁡ ( d 0). F(d_{0}-d_{k})-F(d_{0})<c(k)-c(k-1)\leq c(k-1)-c(k-2)=F(d_{0}-d_{k-1})-F(d_{0}). |  |

If we increase y k y_{k} that would lead to an increase of h 2 ​ ( y) = y k b − y k c h_{2}(y)=y_{k}^{b}-y_{k}^{c} and thereby to an increase of S ∗ S^{*}.

If k < M k<M we also must have d k < d k − 1 d_{k}<d_{k-1} by ( 8.17). Suppose that we have exactly ℓ ≥ 1 \ell\geq 1 equal variables after k k, that is we have

(8.18) |  | d k ≥ d = d k + 1 = ⋯ = d k + ℓ > d k + ℓ + 1 ≥ 0 d_{k}\geq d=d_{k+1}=\dots=d_{k+\ell}>d_{k+\ell+1}\geq 0 |  |

and d k + ℓ d_{k+\ell} is not the last term. We clearly have d = d k + ℓ > 0 d=d_{k+\ell}>0 if it is the last term, otherwise we could simply slightly increase d k d_{k}, that is, increase y k y_{k} slightly which would yield a larger value for S ∗ S^{*}. If ℓ = 1 \ell=1 we can substitute y k + 1 y_{k+1} by y k + 1 − η y_{k+1}-\eta, y k y_{k} by y k + η y_{k}+\eta with a sufficiently small η \eta and we obtain a contradiction. If ℓ ≥ 2 \ell\geq 2 then we cannot have equality in any of the ℓ − 1 \ell-1 relations of type ( 4.47) for m = k + i m=k+i, 1 ≤ i ≤ ℓ − 1 1\leq i\leq\ell-1, since if the first one for which ( 4.47) is sharp has index m m, then

(8.19) |  | c ⁡ ( m) − c ⁡ ( m − 1) < F ⁡ ( d 0 − d m) − F ⁡ ( d 0) = F ⁡ ( d 0 − d m + 1) − F ⁡ ( d 0) ≤ c ⁡ ( m + 1) − c ⁡ ( m). c(m)-c(m-1)<F(d_{0}-d_{m})-F(d_{0})=F(d_{0}-d_{m+1})-F(d_{0})\leq c(m+1)-c(m). |  |

which contradicts ( 4.48). But then we can substitute similarly to the case ℓ = 1 \ell=1 y k \,y_{k} by y k + η y_{k}+\eta, y k + ℓ y_{k+\ell} by y k + ℓ − η y_{k+\ell}-\eta with a sufficiently small η \eta and we again arrive at a contradiction. This proves Theorem L.

## 9 Proof of Theorem 1

According to ( 2.36)–( 2.46) our task will be to show with some small but fixed constant c 0 > 0 c_{0}>0

(9.1) |  | S 0 = ∑ i = 1 M S i 2 ≤ 1 − c 0. S_{0}=\sum^{M}_{i=1}S^{2}_{i}\leq 1-c_{0}. |  |

Let us dissect the sums S i S_{i} as

(9.2) |  | S i = 25 7 ∫ 0 H N i ( λ) e − 25 7 ​ λ d λ = 25 7 ∫ 0 Λ 0 + 25 7 ∫ Λ 0 H = a i + b i, S_{i}=\frac{25}{7}\int\limits^{H}_{0}N_{i}(\lambda)e^{-\frac{25}{7}\lambda}d_{\lambda}=\frac{25}{7}\int\limits^{\Lambda_{0}}_{0}+\frac{25}{7}\int\limits^{H}_{\Lambda_{0}}=a_{i}+b_{i}, |  |

where Λ 0 = 1.311 \Lambda_{0}=1.311,

(9.3) |  | N i ​ ( λ) = ∑ ϱ j ∈ R, λ j ≤ λ χ j ∼ χ i 1. N_{i}(\lambda)=\sum_{\begin{subarray}{c}\varrho_{j}\in R,\ \lambda_{j}\leq\lambda\\ \chi_{j}\sim\chi_{i}\end{subarray}}1. |  |

Our basic inequality will be a small refinement of

(9.4) |  | S ≤ ∑ i ≤ M a i 2 + max i ≤ M ⁡ b i ​ ( 2 ​ ∑ i ≤ M a i + ∑ i ≤ M b i), S\leq\sum_{i\leq M}a^{2}_{i}+\max_{i\leq M}b_{i}\biggl(2\sum_{i\leq M}a_{i}+\sum_{i\leq M}b_{i}\biggr), |  |

where we will treat two classes (and eventually its conjugate classes) containing the zeros with the greatest real part separately. According to ( 9.4) we will estimate ∑ a i \sum a_{i}, ∑ b i \sum b_{i}, max ⁡ b i \max b_{i}, using Principles 1–3 in form of Theorems C–K and a few other results of [9] and [22].

As mentioned already in the introduction, we will try to give a relatively simple proof leaving many possibilities for improvement for future parts of this series.

Throughout we will use the notation that the classes will be ordered according to decreasing value of the greatest real part of the zeros belonging to the relevant class, so according to increasing value of λ i = λ i ​ 1 \lambda_{i}=\lambda_{i1} where the other zeros of the same class will be ordered as λ i ​ 1 ≤ λ i ​ 2 ≤ … \lambda_{i1}\leq\lambda_{i2}\leq\dots. Zeros will be ordered and counted always by multiplicity. In contrast to [9] and [22] we will include also conjugate classes and conjugate zeros in the calculation. We will distinguish first

Case I. λ 1 > 0.44 \lambda_{1}>0.44

Case II/A. 0.35 < λ 1 ≤ 0.44 0.35<\lambda_{1}\leq 0.44

Case II/B. λ 1 ≤ 0.35 \lambda_{1}\leq 0.35

According to Theorem E of [22] we have in Case II at most the real zero ϱ 1 = 1 − δ = 1 − λ 1 ​ ℒ \varrho_{1}=1-\delta=1-\lambda_{1}\mathcal{L} of the real non-principal χ 1 \chi_{1} with the property λ i ​ j ≤ 0.44 \lambda_{ij}\leq 0.44. The reason to distinguish between Cases II/A and II/B is that in Case II/B we have no other zeros with λ ≤ Λ 0 \lambda\leq\Lambda_{0} (in fact with λ ≤ 1.42 \lambda\leq 1.42) while in Case II/A we might have zeros with λ > 1.18 \lambda>1.18 (see Table 7 on p. 301 of [9]).

We will begin the estimation of max ⁡ b i \max b_{i}: Important role will be played by Lemma 10.3 of [9], p. 316, according to which apart from at most two characters and its conjugates we will have λ i ≥ 6 7 − ε \lambda_{i}\geq\frac{6}{7}-\varepsilon for q > q 0 ​ ( ε) q>q_{0}(\varepsilon) for each character. Since we have by Theorem F apart from at most two zeros λ i ≥ 0.702 \lambda_{i}\geq 0.702, we will distinguish the following cases for the estimation of max ⁡ b i \max b_{i}

Case 1 λ i ≥ 6 / 7 − ε \lambda_{i}\geq 6/7-\varepsilon (surely valid for i > 4 i>4)
Case 2 λ i ≥ 0.702 \lambda_{i}\geq 0.702 (surely valid for i > 2 i>2)
Case 3 0.35 < λ i < 0.702 0.35<\lambda_{i}<0.702

In this case i = 1 i=1 or 2 2 and χ i = χ 1 \chi_{i}=\chi_{1} or χ ¯ 1 \overline{\chi}_{1}.
Case 4 λ i ≤ 0.35 \lambda_{i}\leq 0.35

In this case χ 1 \chi_{1} and ϱ 1 \varrho_{1} are real and λ > 1.42 > Λ 0 \lambda>1.42>\Lambda_{0} for all other zeros [9, Tables 3 and 7].

In order to calculate an upper estimate for b i b_{i} we will apply for Cases 1–4 Theorem I with λ 0 = 6 7 − 10 − 8 \lambda_{0}=\frac{6}{7}-10^{-8}, 0.702 0.702, 0.35 0.35 and 0 0, resp. and in the last case we will take into account λ > 1.42 \lambda>1.42 for all other zeros. Using Theorem I we can give a lower estimate for the first few zeros with λ i ​ j ≤ 3 \lambda_{ij}\leq 3 (their number is in Cases 1–4 at most 45 45, 38 38, 34 34 and 31 31, resp.) and then apply an upper estimate for the zeros below 3 + k / 10 3+k/10 ( k = 0, 1, 2, …) (k=0,1,2,\dots) until about 6 6 which is approximately the limit for Theorem I. We will actually use Theorem I until Λ 2, 1 = 6.6 \Lambda_{2,1}=6.6, Λ 2.2 = 6.4 \Lambda_{2.2}=6.4, Λ 2, 3 = 6 \Lambda_{2,3}=6 and Λ 3, 4 = 5.8 \Lambda_{3,4}=5.8 in Cases 1–4, resp. Further we will use in Cases 1–4 the values λ 0 = 6 / 7 − 10 − 8 \lambda_{0}=6/7-10^{-8}, λ 0 = 0.702 \lambda_{0}=0.702, λ 0 = 0.35 \lambda_{0}=0.35, λ 0 = 0 \lambda_{0}=0, resp. (The limit of Theorem I will be larger if λ 0 \lambda_{0} is larger.) On the other hand the value x x for F x ​ ( z) = G ​ ( z x) F_{x}(z)=G\left(\frac{z}{x}\right) (see ( 4.24)) is chosen experimentally to obtain the approximately optimal estimate for the N th N^{\text{\rm th}} zero of the same class or to bound N i ​ ( 3 + k / 10) N_{i}(3+k/10) for 3 ≤ 3 + k / 10 ≤ Λ 2 ​ ν 3\leq 3+k/10\leq\Lambda_{2\nu} ( 1 ≤ ν ≤ 4) (1\leq\nu\leq 4). The condition B = 25 / 7 > t 0 ​ ( f) = 2 / x B=25/7>t_{0}(f)=2/x will be always satisfied as well as λ 0 / x ≤ 5 / 4 \lambda_{0}/x\leq 5/4 which assures Condition 2 (see ( 4.26)) for F x ​ ( z) = G ⁡ ( z / x) F_{x}(z)=G(z/x). For all the other zeros of the same class, i.e. for Λ 2 ​ μ ≤ λ i ​ j ≤ Λ ∞ = log ⁡ log ⁡ log ⁡ q \Lambda_{2\mu}\leq\lambda_{ij}\leq\Lambda_{\infty}=\log\log\log q ( 1 ≤ μ ≤ 4) (1\leq\mu\leq 4) we can use our estimate ( 4.11) of Corollary 2 of Theorem D. For simplicity we can calculate in all Cases 1–4 with E 3 E_{3} arising from Λ 3 = 5.8 \Lambda_{3}=5.8 valid for all Λ ≥ 5.8 \Lambda\geq 5.8. We obtain

###### Lemma 6.

We have max ⁡ b i ≤ c j ∗ \max b_{i}\leq c_{j}^{*} in Case j, where

(9.5) |  | c 1 ∗ = 0.0722, c 2 ∗ = 0.0751, c 3 ∗ = 0.0826, c 4 ∗ = 0.715. c_{1}^{*}=0.0722,\ \ c_{2}^{*}=0.0751,\ \ c_{3}^{*}=0.0826,\ \ c_{4}^{*}=0.715. |  |

###### Proof.

We give just a brief account of the results of the calculation for the typical Case 1 (which applies apart from at most four classes for all others). We obtain at most 6 6 zeros below Λ 0 = 1.311 \Lambda_{0}=1.311 for which the corresponding value e − 25 / 7 max ( λ i ​ j, Λ 0) e^{-25/7\max(\lambda_{ij},\Lambda_{0})} is independently from the concrete value λ i ​ j ≤ Λ 0 \lambda_{ij}\leq\Lambda_{0} just e − ( 25 / 7) ​ Λ 0 e^{-(25/7)\Lambda_{0}}. For the other possible zeros below 3 3 we get the bounds (in brackets the value of the parameters x x used for the function F x ​ ( z) = G ⁡ ( z / x) F_{x}(z)=G(z/x)) λ i ​ 7 ≥ 1.47 \lambda_{i7}\geq 1.47 ( 1.58) (1.58), λ i ​ 8 ≥ 1.61 \lambda_{i8}\geq 1.61 ( 1.6) (1.6), λ i ​ 9 ≥ 1.73 \lambda_{i9}\geq 1.73 ( 1.62) (1.62), λ i ​ 10 ≥ 1.85 \lambda_{i10}\geq 1.85 ( 1.66) (1.66), λ i ​ 11 ≥ 1.94 \lambda_{i11}\geq 1.94 ( 1.66) (1.66), λ i ​ 12 ≥ 2.05 \lambda_{i12}\geq 2.05 ( 1.68) (1.68), λ i ​ 13 ≥ 2.12 \lambda_{i13}\geq 2.12 ( 1.68) (1.68), λ i ​ 14 ≥ 2.20 \lambda_{i14}\geq 2.20 ( 1.68) (1.68), λ i ​ 15 ≥ 2.27 \lambda_{i15}\geq 2.27 ( 1.68) (1.68), λ i ​ 16 ≥ 2.33 \lambda_{i16}\geq 2.33 ( 1.68) (1.68), λ i ​ 17 ≥ 2.4 \lambda_{i17}\geq 2.4, λ i ​ 18 ≥ 2.45 \lambda_{i18}\geq 2.45, λ i ​ 19 ≥ 2.51 \lambda_{i19}\geq 2.51, λ i ​ 20 ≥ 2.56 \lambda_{i20}\geq 2.56, λ i ​ 21 ≥ 2.61 \lambda_{i21}\geq 2.61, λ i ​ 22 ≥ 2.65 \lambda_{i22}\geq 2.65, λ i ​ 23 ≥ 2.7 \lambda_{i23}\geq 2.7, λ i ​ 24 ≥ 2.74 \lambda_{i24}\geq 2.74, λ i ​ 25 ≥ 2.78 \lambda_{i25}\geq 2.78, λ i ​ 26 ≥ 2.82 \lambda_{i26}\geq 2.82, λ i ​ 27 ≥ 2.85 \lambda_{i27}\geq 2.85, λ i ​ 28 ≥ 2.89 \lambda_{i28}\geq 2.89, λ i ​ 29 ≥ 2.92 \lambda_{i29}\geq 2.92, λ i ​ 30 ≥ 2.95 \lambda_{i30}\geq 2.95, λ i ​ 31 ≥ 2.99 \lambda_{i31}\geq 2.99 ( λ i ​ 32 ≥ 3) (\lambda_{i32}\geq 3) with the parameters x 17 = x 18 = ⋯ = x 31 = 1 x_{17}=x_{18}=\dots=x_{31}=1. Similarly we can calculate with experimentally optimally chosen parameters x = x k ′ ∈ [0.6, 1.7] x=x_{k}^{\prime}\in[0.6,1.7] an upper estimate for N i ​ ( 3 + k / 10) N_{i}(3+k/10) for 0 ≤ k ≤ 35 0\leq k\leq 35. ∎

The value ∑ b i \sum b_{i} can be easily estimated by Corollary 1 as

(9.6) |  | ∑ i ≤ I b i \displaystyle\sum_{i\leq I}b_{i} | = def 25 7 ​ ∫ Λ 0 H N ⁡ ( λ) ​ e − 25 7 ​ λ ​ 𝑑 λ ≤ ∑ λ j ≤ H e − 25 7 ​ max ⁡ ( λ j, Λ 0) \displaystyle\stackrel{{\scriptstyle{\rm def}}}{{=}}\frac{25}{7}\int\limits^{H}_{\Lambda_{0}}N(\lambda)e^{-\frac{25}{7}\lambda}d\lambda\leq\sum_{\lambda_{j}\leq H}e^{-\frac{25}{7}\max(\lambda_{j},\Lambda_{0})} |  |

 |  | ≤ e − 19 Λ 0 / 21 ∑ λ j ≤ H e − ( 8 / 3) ​ max ⁡ ( λ j, Λ 0) ≤ e − 19 Λ 0 / 21 ∑ λ j ≤ H e − 8 3 ​ λ j e − r + κ 2 ​ d j \displaystyle\leq e^{-19\Lambda_{0}/21}\sum_{\lambda_{j}\leq H}e^{-(8/3)\max(\lambda_{j},\Lambda_{0})}\leq e^{-19\Lambda_{0}/21}\sum_{\lambda_{j}\leq H}e^{-\frac{8}{3}\lambda_{j}}e^{-\frac{r+\kappa}{2}d_{j}} |  |

 |  | < 22.281 e − 19 Λ 0 / 21 < 6.805. \displaystyle<22.281e^{-19\Lambda_{0}/21}<6.805. |  |

In order to estimate ∑ a i \sum a_{i} we will distinguish 8 cases as follows ( h h is a small constant)

Case 1 λ 1 ≥ 0.68 \lambda_{1}\geq 0.68 | Case 5 0.35 ≤ λ 1 < 0.44 0.35\leq\lambda_{1}<0.44 |

Case 2 0.6 ≤ λ 1 < 0.68 0.6\leq\lambda_{1}<0.68 | Case 6 0.14 ≤ λ 1 < 0.35 0.14\leq\lambda_{1}<0.35 |

Case 3 0.5 ≤ λ 1 < 0.6 0.5\leq\lambda_{1}<0.6 | Case 7 0.04 ≤ λ 1 < 0.14 0.04\leq\lambda_{1}<0.14 |

Case 4 0.44 ≤ λ 1 < 0.5 0.44\leq\lambda_{1}<0.5 | Case 8 λ 1 < 0.06 \lambda_{1}<0.06 |

In the most sophisticated Cases 1–5 we will use Theorem K (for its proof see Section 8) with the parameters λ 0 = 0.44 \lambda_{0}=0.44, x = 0.68 x=0.68 for Cases 2–5 and x = 0.7 x=0.7 for Case 1, φ = 1 3 \varphi=\frac{1}{3}. We will choose Λ 0 \Lambda_{0} in such a way that it should be just slightly smaller than the value λ \lambda for which

(9.7) |  | ( G ⁡ ( λ − λ 0 x) − f ⁡ ( 0) ​ φ 2) 2 = f ⁡ ( 0) ​ φ 2 ​ G ​ ( − λ 0 x) ⇔ ψ = ξ + ξ \left(G\left(\frac{\lambda-\lambda_{0}}{x}\right)-\frac{f(0)\varphi}{2}\right)^{2}=\frac{f(0)\varphi}{2}G\left(-\frac{\lambda_{0}}{x}\right)\Leftrightarrow\psi=\xi+\sqrt{\xi} |  |

holds. Λ 0 = 1.311 \Lambda_{0}=1.311 will be such a choice.

In view of f ⁡ ( 0) = 16 ​ x / 15 f(0)=16x/15 we have then with the notation of ( 7.4)–( 7.5)

(9.8) |  | G ( − λ 0 x) = 1.56903 …, f ⁡ ( 0) ​ φ 2 = 8 45 ⋅ 0.7, λ = Λ 0 = 1.311, G ( Λ − λ 0 x) = 0.5882 … ψ = 0.37488 …, ξ = 0.07931 … Δ = 0.29557 … \begin{gathered}G\left(-\frac{\lambda_{0}}{x}\right)=1.56903\dots,\quad\frac{f(0)\varphi}{2}=\frac{8}{45}\cdot 0.7,\quad\lambda=\Lambda_{0}=1.311,\\ G\left(\frac{\Lambda-\lambda_{0}}{x}\right)=0.5882\dots{\\ }\psi=0.37488\dots,\quad\xi=0.07931\dots\quad\Delta=0.29557\dots{}\end{gathered} |  |

and consequently by ( 4.36)

(9.9) |  | D = ∑ ( ψ j − ψ) ≤ 1.5575, D 0 = ∑ ( G ⁡ ( λ j − λ 0 x) − G ⁡ ( λ − λ 0 x)) ≤ 2.4438. D=\sum(\psi_{j}-\psi)\leq 1.5575,\ D_{0}=\sum\left(\!G\!\left(\!\frac{\lambda_{j}\!-\!\lambda_{0}}{x}\!\right)\!-\!G\left(\!\frac{\lambda\!-\!\lambda_{0}}{x}\!\right)\!\right)\leq 2.4438. |  |

According to the theorem the sum

(9.10) |  | S ′ = ∑ λ j ≤ Λ 0 ( e − 25 7 ​ λ j − e − 25 7 ​ Λ 0) = e − 25 7 ​ Λ 0 ​ ∑ λ j ≤ Λ 0 ( e 25 7 ​ d j − 1) = e − 25 7 ​ Λ 0 ​ S S^{\prime}=\sum_{\lambda_{j}\leq\Lambda_{0}}\bigl(e^{-\frac{25}{7}\lambda_{j}}-e^{-\frac{25}{7}\Lambda_{0}}\bigr)=e^{-\frac{25}{7}\Lambda_{0}}\sum_{\lambda_{j}\leq\Lambda_{0}}(e^{\frac{25}{7}d_{j}}-1)=e^{-\frac{25}{7}\Lambda_{0}}S |  |

is, in view of Theorem K maximal, if, taking into account Theorems E, F, we choose

(9.11) |  | λ 1 = λ 2 = 0.68, λ 3 = ⋯ = λ k = 0.702 \lambda_{1}=\lambda_{2}=0.68,\quad\lambda_{3}=\dots=\lambda_{k}=0.702 |  |

and λ k + 1 ∈ [0.702, Λ 0] \lambda_{k+1}\in[0.702,\Lambda_{0}] in such a way that D 0 = 2.4438 D_{0}=2.4438 should hold. Since we have

(9.12) |  | G ⁡ ( λ 1 − λ 0 x) = 8 9, G ⁡ ( λ 3 − λ 0 x) = 0.8747 ​ …, G ⁡ ( Λ 0 − λ 0 x) = 0.5882 ​ … G\left(\frac{\lambda_{1}\!-\!\lambda_{0}}{x}\right)=\frac{8}{9},\ G\left(\frac{\lambda_{3}\!-\!\lambda_{0}}{x}\right)=0.8747\dots,\ G\left(\frac{\Lambda_{0}\!-\!\lambda_{0}}{x}\right)=0.5882\dots |  |

we obtain k = 6 k=6, G ⁡ ( λ 9 − λ 0 x) = 0.71336 ​ … G\left(\frac{\lambda_{9}-\lambda_{0}}{x}\right)=0.71336\dots, λ 9 = 0.99 ​ … \lambda_{9}=0.99\dots. Consequently,

(9.13) |  | S ′ ≤ 2 e − ( 25 / 7) ⋅ 0.68 + 6 e − ( 25 / 7) ⋅ 0.702 + e − ( 25 / 7) ⋅ 0.99 − 9 e − ( 25 / 7) ​ Λ 0 < 0.612 S^{\prime}\leq 2e^{-(25/7)\cdot 0.68}+6e^{-(25/7)\cdot 0.702}+e^{-(25/7)\cdot 0.99}-9e^{-(25/7)\Lambda_{0}}<0.612 |  |

which settles Case 1.

Similarly we obtain the result for Cases 1–5, that is,

###### Lemma 7.

We have

(9.14) |  | ∑ i ≤ I a i ≤ c ~ ν ​ for Case ​ ν ​ ( 1 ≤ ν ≤ 5) ​ above, where \sum_{i\leq I}a_{i}\leq\widetilde{c}_{\nu}\ \text{ for Case }\nu\ (1\leq\nu\leq 5)\ \text{ above, where } |  |

(9.15) |  | c ~ 1 = 0.612, c ~ 2 = 0.622, c ~ 3 = 0.564, c ~ 4 = 0.453, c ~ 5 = 0.483. \widetilde{c}_{1}=0.612,\ \widetilde{c}_{2}=0.622,\ \widetilde{c}_{3}=0.564,\ \widetilde{c}_{4}=0.453,\ \widetilde{c}_{5}=0.483. |  |

###### Proof.

The proof is completely analogous in Cases 2-3 where we use that apart from two zeros which might be as large as the lower bounds stipulated in Case ν \nu we have for all other zeros, i.e. for λ 3 \lambda_{3}, by Tabellen 2, 3, 7 of [22]

(9.16) |  | λ ≥ c ν ′, c 2 ′ = 0.74, c 3 ′ = 0.97. \lambda\geq c_{\nu}^{\prime},\ \ c_{2}^{\prime}=0.74,\ \ c_{3}^{\prime}=0.97. |  |

In Case 4, if χ 1 \chi_{1} or ϱ 1 \varrho_{1} is complex, then by Tabelle 7 of [22] we have at most two zeros, ϱ 1 \varrho_{1} and ϱ ¯ 1 \overline{\varrho}_{1} (of L ⁡ ( s, χ 1) L(s,\chi_{1}) or L ⁡ ( s, χ 1) L(s,\chi_{1}) and L ⁡ ( s, χ ¯ 1) L(s,\overline{\chi}_{1}), respectively) with λ ≤ Λ 0 \lambda\leq\Lambda_{0} (in fact if λ ≠ λ 1 \lambda\neq\lambda_{1} then λ ≥ 1.36 \lambda\geq 1.36)

(9.17) |  | ∑ i ≤ I a i ≤ 2 ( e − ( 25 / 7) ⋅ 0.44 − e − ( 25 / 7) ​ Λ 0) < 0.39698. \sum_{i\leq I}a_{i}\leq 2\bigl(e^{-(25/7)\cdot 0.44}-e^{-(25/7)\Lambda_{0}}\bigr)<0.39698. |  |

If Case 4 holds and χ 1 \chi_{1} and ϱ 1 \varrho_{1} are real, then by Tables 4 and 7 of [9] we have apart from this *single*zero λ ≥ 1.08 \lambda\geq 1.08 for all other zeros, so we can apply the same procedure as in Case 1 (cf. ( 9.7)–( 9.14)) and obtain ( 9.14) in this case with an upper bound. Comparison with ( 9.17) yields the estimate ( 9.15) for ν = 4 \nu=4. ∎

Case 5 is more simple in the sense that in this case χ 1 \chi_{1} and ϱ 1 \varrho_{1} must be real by Theorem E. Further we have by Tables 4 and 7 of [9] λ ≥ 1.18 \lambda\geq 1.18 apart from this single zero. Applying again the same procedure as before (cf. ( 9.7)–( 9.13)) we obtain ( 9.14)–( 9.15) for ν = 5 \nu=5.

Case 6 is even more simple since in this case we have just the single real ϱ 1 \varrho_{1} for real χ 1 \chi_{1} within R ⁡ ( Λ 0, T) R(\Lambda_{0},T). This means that in this case we have

(9.18) |  | ∑ i ≤ I a i = a 1 ≤ ( e − ( 25 / 7) ⋅ 0.14 − e − ( 25 / 7) ​ Λ 0) = 0.59727 …. \sum_{i\leq I}a_{i}=a_{1}\leq\bigl(e^{-(25/7)\cdot 0.14}-e^{-(25/7)\Lambda_{0}}\bigr)=0.59727\ldots. |  |

The same applies in Cases 7 and 8 when

(9.19) |  | ∑ i ≤ I a i = e − ( 25 / 7) ​ λ 1 − e − ( 25 / 7) ​ Λ 0. \sum_{i\leq I}a_{i}=e^{-(25/7)\lambda_{1}}-e^{-(25/7)\Lambda_{0}}. |  |

Summarizing we have

###### Corollary.

In Cases 7–8 we have ( 9.19) while in Cases 1–6

(9.20) |  | ∑ i a i ≤ 0.622. \sum_{i}a_{i}\leq 0.622. |  |

Cases 7–8 we will settle just using the results of [9] about further zeros by the aid of Theorems C and D. For Cases 1–6 we state

###### Corollary.

In Cases 1–6 we have for S S in ( 9.4) the estimate

(9.21) |  | S < 0.9903. S<0.9903. |  |

###### Proof.

Let us forget for a moment that the typical estimate c 1 ∗ = 0.0722 c_{1}^{*}=0.0722 holds up to at most four exceptional classes for max ⁡ b i \max b_{i}. If we had no exceptions then in Cases 1–6 we would have ( 9.20) and this would lead by ( 9.6) and ( 9.4) to

(9.22) |  | S − ≤ 0.622 2 + 0.0722 ​ ( 2 ⋅ 0.622 + 6.805) = 0.9680218. S^{-}\leq 0.622^{2}+0.0722(2\cdot 0.622+6.805)=0.9680218. |  |

However, two of the classes might have a surplus

(9.23) |  | c 3 ∗ − c 1 ∗ = 0.0826 − 0.0722 = 0.0104 c_{3}^{*}-c_{1}^{*}=0.0826-0.0722=0.0104 |  |

for max ⁡ b i \max b_{i} and this surplus obtains the factor at most 1.244 + 2 ⋅ 0.0826 = 1.4092 1.244+2\cdot 0.0826=1.4092 from 2 ​ ∑ a i 2\sum a_{i} and from b i 1 + b i 2 b_{i_{1}}+b_{i_{2}} (the corresponding two exceptional classes). This leads to the surplus

(9.24) |  | Δ 1 = 0.01465568. \Delta_{1}=0.01465568. |  |

Analogously we might have another smaller surplus

(9.25) |  | c 3 ∗ − c 1 ∗ = 0.0751 − 0.0722 = 0.0029 c_{3}^{*}-c_{1}^{*}=0.0751-0.0722=0.0029 |  |

for max ⁡ b i \max b_{i} with a factor 2 ⋅ 0.0751 = 0.1502 2\cdot 0.0751=0.1502 (since we calculated already the contribution of ∑ a i \sum a_{i} with the larger surplus for all classes). This yields another surplus of size

(9.26) |  | Δ 2 = 0.0029 ⋅ 0.1502 = 4.3558 ⋅ 10 − 4. \Delta_{2}=0.0029\cdot 0.1502=4.3558\cdot 10^{-4}. |  |

Adding Δ 1 + Δ 2 \Delta_{1}+\Delta_{2} to S − S^{-} in ( 9.22) we obtain S < 0.9832 S<0.9832, i.e. ( 9.21) holds for Cases 1–6. ∎

In Case 7 we have by Tables 4 and 5 of [9] apart from the single real zero ϱ 1 \varrho_{1} for all other zeros λ ≥ 2.421 = Λ 1 \lambda\geq 2.421=\Lambda_{1} and we define a i a_{i}, b i b_{i} by Λ 1 \Lambda_{1} instead of Λ 0 \Lambda_{0}.

Consequently we have by ( 9.4)–( 9.5), ( 9.19) and similary to ( 9.6) in this case

(9.27) |  | ∑ i b i ≤ 15.6 e − 19 Λ 1 / 21 < 1.74516, \sum_{i}b_{i}\leq 15.6e^{-19\Lambda_{1}/21}<1.74516, |  |

(9.28) |  | max ⁡ b i < c 4 ∗ = 0.0715, \max b_{i}<c_{4}^{*}=0.0715, |  |

(9.29) |  | ∑ a i < e − ( 25 / 7) ​ 0.04 − e − ( 25 / 7) ​ Λ 1 < 0.86671, \sum a_{i}<e^{-(25/7)0.04}-e^{-(25/7)\Lambda_{1}}<0.86671, |  |

(9.30) |  | S ≤ 0.86671 2 + 0.0715 ​ ( 2 ⋅ 0.86671 + 1.74516) < 0.99991. S\leq 0.86671^{2}+0.0715(2\cdot 0.86671+1.74516)<0.99991. |  |

We note that although the estimate ( 9.28) was shown for the value Λ 0 \Lambda_{0} instead of Λ 1 \Lambda_{1}, but the definition

 | b i = b i ​ ( Λ) = 25 7 ​ ∑ Λ H N i ​ ( λ) ​ e − ( 25 / 7) ​ λ ​ d ​ λ b_{i}=b_{i}(\Lambda)=\frac{25}{7}\sum\limits_{\Lambda}^{H}N_{i}(\lambda)e^{-(25/7)\lambda}d\lambda |  |

is clearly decreasing in Λ \Lambda so in fact we would get a much better estimate for c 4 ∗ c_{4}^{*} with Λ 1 \Lambda_{1} in place of Λ 0 \Lambda_{0}.

Finally, in Case 8 we have again a single real zero ϱ 1 \varrho_{1} with λ 1 ≤ 0.04 \lambda_{1}\leq 0.04, while for all other zeros we have by Theorem G and Table 5 of [9]

(9.31) |  | λ ≥ Λ ∗ = max ⁡ ( ( 12 11 − ε) ​ log ⁡ 1 λ 1, Λ 2) ​ with ​ Λ 2 = 3.96. \lambda\geq\Lambda^{*}=\max\left(\Bigl(\frac{12}{11}-\varepsilon\Bigr)\log\frac{1}{\lambda_{1}},\Lambda_{2}\right)\ \text{ with }\ \Lambda_{2}=3.96. |  |

Consequently, we have, by Corollary 1 for λ ≥ Λ ∗ \lambda\geq\Lambda^{*}

(9.32) |  | ∑ Λ ∗ ≤ λ j ≤ Λ ∞ e − ( 8 / 3) ​ λ j < 10.4, ∑ λ i ​ j ∈ κ Λ ∗ ≤ λ i ​ j ≤ Λ ∞ e − 2 ​ λ i ​ j < 10.4. \sum_{\Lambda^{*}\leq\lambda_{j}\leq\Lambda_{\infty}}e^{-(8/3)\lambda_{j}}<10.4,\ \ \ \sum_{\begin{subarray}{c}\lambda_{ij}\in\kappa\\ \Lambda^{*}\leq\lambda_{ij}\leq\Lambda_{\infty}\end{subarray}}e^{-2\lambda_{ij}}<10.4. |  |

This implies (defining b i b_{i} now with Λ ∗ = Λ ∗ ​ ( λ 1) \Lambda^{*}=\Lambda^{*}(\lambda_{1}))

(9.33) |  | ∑ Λ ∗ ≤ λ j ≤ Λ ∞ b i ≤ e − ( 25 7 − 8 3) ​ Λ ∗ ⋅ 10.4 ≤ 10.4 ​ λ 1 76 / 77 < 0.435, \sum_{\Lambda^{*}\leq\lambda_{j}\leq\Lambda_{\infty}}b_{i}\leq e^{-(\frac{25}{7}-\frac{8}{3})\Lambda^{*}}\cdot 10.4\leq 10.4\lambda_{1}^{76/77}<0.435, |  |

(9.34) |  | max ⁡ b i ≤ e − ( 25 7 − 2) ​ Λ ∗ ⋅ 10.4 ≤ 10.4 ​ λ 1 11 / 7 \max b_{i}\leq e^{-\left(\frac{25}{7}-2\right)\Lambda^{*}}\cdot 10.4\leq 10.4\lambda_{1}^{11/7} |  |

(9.35) |  | ∑ a i = a 1 = e − ( 25 / 7) ​ λ 1 − e − ( 25 / 7) ​ Λ ∗ < e − 25 7 ​ λ 1. \sum a_{i}=a_{1}=e^{-(25/7)\lambda_{1}}-e^{-(25/7)\Lambda^{*}}<e^{-\frac{25}{7}\lambda_{1}}. |  |

So we have by ( 9.4) and λ 1 ≤ 0.04 \lambda_{1}\leq 0.04

(9.36) |  | S ≤ e − 50 7 ​ λ 1 + 2.87 ⋅ 10.4 ​ λ 1 11 / 7 ≤ e − 7 ​ λ 1 + 5 ​ λ 1 < 1, S\leq e^{-\frac{50}{7}\lambda_{1}}+2.87\cdot 10.4\lambda_{1}^{11/7}\leq e^{-7\lambda_{1}}+5\lambda_{1}<1, |  |

since ( 1 − e − y) / y (1-e^{-y})/y is decreasing for y ≥ 0 y\geq 0 and so we have for λ 1 ≤ 0.04 \lambda_{1}\leq 0.04

(9.37) |  | 1 − e − 7 ​ λ 1 λ 1 ≥ 1 − e − 0.28 0.04 > 6.1 > 5. \frac{1-e^{-7\lambda_{1}}}{\lambda_{1}}\geq\frac{1-e^{-0.28}}{0.04}>6.1>5. |  |

Thereby ( 9.36) is really true which settles the remaining Case 8 and consequently the proof of Theorem 1 is complete.

Acknowledgement. The author would like to thank his colleague and friend, Sz. Gy. Révész, for supplying the proof of Lemma 4.

## References

- [1] Jing Run Chen, Jian Min Liu, The exceptional set of Goldbach numbers III, Chinese Quart. J. Math. 4 (1989), 1–15.
- [2] Jing Run Chen, Jian Min Liu, On the least prime in an arithmetical progression. III and IV, Sci. China Ser. A 32 (1989), no. 6, 654–673 and no. 7, 792–807.
- [3] N. G. Cudakov, On the density of the set of even numbers which are not representable as a sum of two primes, Izv. Akad. Nauk SSSR 2 (1938), 25–40.
- [4] H. Davenport, Multiplicative number theory, 2nd edition. Revised by Hugh L. Montgomery, Graduate Texts in Mathematics, 74, Springer-Verlag, New York–Berlin, 1980. xiii+177 pp.
- [5] T. Estermann, On Goldbach’s problem: Proof that almost all even positive integers are sums of two primes, Proc. London Math. Soc. (2) 44 (1938), 307–314.
- [6] D. A. Goldston, On Hardy and Littlewood’s contribution to the Goldbach conjecture, Proceedings of the Amalfi Conference on Analytic Number Theory (Maiori, 1989), 115–155, Univ. Salerno, Salerno, 1992.
- [7] Graham, S. W., Applications of sieve methods, Ph. D. Thesis, University of Michigan, 1977.
- [8] G. H. Hardy, J. E. Littlewood, Some problems of ‘Partitito Numerorum’, V: A further contribution to the study of Goldbach’s problem, Proc. London Math. Soc. (2) 22 (1924), 46–56.
- [9] D. R. Heath-Brown, Zero-free regions for Dirichlet L L -functions, and the least prime in an arithmetic progression, Proc. London Math. Soc. (3) 64 (1992), no. 2, 265–338.
- [10] M. Jutila, On Linnik’s constant, Math. Scand. 41 (1975), 45–62.
- [11] Anatolij A. Karatsuba, Basic analytic number theory. Translated from the second (1983) Russian edition and with a preface by Melvyn B. Nathanson, Springer-Verlag, Berlin, 1993. xiv+222 pp.
- [12] Hongze Li, The exceptional set of Goldbach numbers I, Quart J. Math. Oxford Ser. (2) 50 (2000), no. 200, 471–482.
- [13] Hongze Li, The exceptional set of Goldbach numbers II, Acta Arith. 92 (2000), no. 1, 71–88.
- [14] Wen Chao Lu, Exceptional set of Goldbach number, J. Number Theory 130 (2010), no. 10, 2359-–2392.
- [15] H. L. Montgomery, Topics in multiplicative number theory, Lecture Notes in Mathematics, Vol. 227. Springer-Verlag, Berlin–New York, 1971. ix+178 pp.
- [16] H. L. Montgomery, R. C. Vaughan, The exceptional set in Goldbach’s problem. Collection of articles in memory of Juriĭ Vladimirovič Linnik, Acta Arith. 27 (1975), 353-–370.
- [17] J. Pintz, Some new density theorems for Dirichlet L L -functions, arXiv: 1804.05552
- [18] J. Pintz, A new explicit formula in the additive theory of primes with applications I. The explicit formula for the Goldbach and Generalized Twin Prime Problems, arXiv: 1804.05561
- [19] J. G. van der Corput, Sur l’hypothése de Goldbach pour Presque tous les nombres pairs, Acta Arith. 2 (1937), 266–290.
- [20] R. C. Vaughan, On Goldbach’s problem, Acta Arith. 22 (1972), 21-–48.
- [21] I. M. Vinogradov, Representation of an odd number as a sum of three prime numbers, Doklady Akad. Nauk SSSR 15 (1937), 291–294 (Russian).
- [22] Xylouris, T., Über die Linniksche Konstante, Diplomarbeit, Universität Bonn, 2009, arXiv: 0906, 2749v1

János Pintz
Rényi Mathematical Institute
of the Hungarian Academy of Sciences
Budapest, Reáltanoda u. 13–15
H-1053 Hungary
e-mail: pintz.janos@renyi.mta.hu

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/1804.09083
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/1804.09084
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1804.09084
[7]: https://arxiv.org/pdf/1804.09084
[8]: /html/1804.09085
