<!-- source: https://arxiv.org/html/2602.20036v1 | converted from HTML -->

Properties of the Function ⁢ F x , t ( k ) ( n ) with Applications to the Erdős–Straus, Sierpiński Conjectures and Their Generalizations

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2602.20036v1 [math.NT] 23 Feb 2026

# Properties of the Function F x, t ( k) ​ ( n) F_{x,t}^{(k)}(n) with Applications to the Erdős–Straus, Sierpiński Conjectures and Their Generalizations

Philemon Urbain Mballa Affiliation: [2ex] [philemon-urbain.mballa@etu.u-paris.fr][3] Email: [philemonmballa@gmail.com][4]

August 11, 2026

###### Abstract

This article develops a parametric approach to study the Diophantine equation k n = 1 x + 1 y + 1 z \frac{k}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}, underlying the Erdős–Straus ( k = 4 k=4), Sierpiński ( k = 5 k=5), and their generalizations. We introduce and analyze the fundamental function F x, t ( k) ​ ( n) = t 2 ​ ( k ​ x − n) 2 − 2 ​ n ​ x ​ t F_{x,t}^{(k)}(n)=t^{2}(kx-n)^{2}-2nxt, whose perfect square values are equivalent to solutions of the conjectures.

For any fixed pair ( x, t) (x,t), we define its admissible domain 𝒟 x, t ( k) \mathcal{D}_{x,t}^{(k)} and prove that on this domain, F F is strictly decreasing, non-negative, and converges to its minimum. A key result is the Zero Lemma: if F ⁡ ( n 0) = 0 F(n_{0})=0 for some n 0 n_{0} in the domain, then n 0 n_{0} is necessarily the upper bound of 𝒟 x, t ( k) \mathcal{D}_{x,t}^{(k)}, and such zeros of F F yield explicit symmetric solutions with y = z y=z.

As an illustration, in the classical Erdős–Straus case ( k = 4 k=4), we explicitly construct symmetric solutions y = z y=z for all integers n ≡ 0, 2, 3 ( mod 4) n\equiv 0,2,3\pmod{4}, covering already 75 % 75\% of all integers. For the remaining class n ≡ 1 ( mod 4) n\equiv 1\pmod{4}, which is traditionally more challenging, we construct explicit symmetric solutions based on the existence of a divisor b ≡ 3 ( mod 4) b\equiv 3\pmod{4}, and we show that this condition is satisfied for almost all such integers: the set of exceptions has natural density zero.

Consequently, the Erdős–Straus conjecture is verified for a proportion of integers tending to 1 1 in this class. In particular, we obtain infinitely many new explicit families of symmetric solutions for numbers not covered by Mordell’s theorem. These results elucidate the structural behavior of F F and provide a unified framework for generating large families of solutions.

## 1 Introduction

The Erdős–Straus conjecture, formulated in 1948 by Paul Erdős and Ernst G. Strauss, states that for every integer n ≥ 2 n\geq 2, there exist positive integers x, y, z x,y,z such that

 | 4 n = 1 x + 1 y + 1 z. \frac{4}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}. |  |

Despite numerous works, this conjecture remains open to this day. Table 1, adapted from Tao’s article [2], traces the history of numerical verifications that have progressively pushed forward the bound up to which the conjecture is validated.

Bound | Year | Author(s) |

5000 5000 | ⩽ 1950 \leqslant 1950 | Straus, see [3] |

8000 8000 | 1962 | Bernstein [4] |

20000 20000 | ⩽ 1969 \leqslant 1969 | Shapiro, see [5] |

106128 106128 | 1948/9 | Oblath [6] |

141648 141648 | 1954 | Rosati [7] |

10 7 10^{7} | 1964 | Yamomoto [8] |

1.1 × 10 7 1.1\times 10^{7} | 1976 | Jollensten [9] |

10 8 10^{8} | 1971 | Terzi [10] |

10 9 10^{9} | 1994 | Elsholtz & Roth (unpublished) |

10 10 10^{10} | 1995 | Elsholtz & Roth (unpublished) |

1.6 × 10 11 1.6\times 10^{11} | 1996 | Elsholtz & Roth (unpublished) |

10 10 10^{10} | 1999 | Kotsireas [11] |

10 14 10^{14} | 1999 | Swett [12] |

2 × 10 14 2\times 10^{14} | 2012 | Bello-Hernández, Benito, Fernández [13] |

10 17 10^{17} | 2014 | Salez [14] |

Table 1: Numerical verifications of the Erdős–Straus conjecture.

The Polish mathematician Wacław Sierpiński generalized this question by replacing the numerator 4 4 with 5 5:

 | 5 n = 1 x + 1 y + 1 z. \frac{5}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}. |  |

This conjecture, known as the Sierpiński conjecture, has also been the subject of numerous investigations. Article [15] presents a detailed history of numerical verifications for k = 5 k=5.

A natural generalization, often attributed to Andrzej Schinzel (a student of Sierpiński), consists in considering for any fixed integer k ≥ 4 k\geq 4 the equation

 | k n = 1 x + 1 y + 1 z. \frac{k}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}. |  |

for all natural numbers n n, except for finitely many n n. In the literature, almost all works focus on the cases k = 4 k=4 and k = 5 k=5, which is naturally explained by the increasing complexity of the problem as k k grows.

In our previous article [1], we proposed a unified approach to all these conjectures. For any fixed integer k ≥ 4 k\geq 4, we introduced the function

 | F x, t ( k) ​ ( n) = t 2 ​ ( k ​ x − n) 2 − 2 ​ n ​ x ​ t F_{x,t}^{(k)}(n)=t^{2}(kx-n)^{2}-2nxt |  |

and established the following fundamental equivalence:

 | k n = 1 x + 1 y + 1 z ⟺ ∃ x, t ∈ ℕ ∗, F x, t ( k) ( n) is a perfect square m 2, m ∈ ℕ, \frac{k}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}\;\Longleftrightarrow\;\exists x,t\in\mathbb{N}^{*},\;F_{x,t}^{(k)}(n)\text{ is a perfect square }m^{2},m\in\mathbb{N}, |  |

for every integer n ≥ N 1 n\geq N_{1} where N 1 N_{1} is an integer greater than or equal to 2 2, with then y = t ⁡ ( k ​ x − n) + m y=t(kx-n)+m and z = t ⁡ ( k ​ x − n) − m z=t(kx-n)-m. This equivalence reduces the search for solutions to the condition that F x, t ( k) ​ ( n) F_{x,t}^{(k)}(n) is a perfect square.

The present article deepens this approach by studying the fundamental properties of the function F F. For each fixed pair ( x, t) (x,t), we define its admissible domain 𝒟 x, t ( k) \mathcal{D}_{x,t}^{(k)} and prove that on this domain, F F is strictly decreasing, nonnegative, and converges to its minimum. A key result, the **Zero Lemma**, establishes that if F ⁡ ( n 0) = 0 F(n_{0})=0 for some n 0 n_{0} in the domain, then n 0 n_{0} is necessarily the upper bound of 𝒟 x, t ( k) \mathcal{D}_{x,t}^{(k)}.

These properties, although local (specific to each pair), are essential for understanding the behavior of F F and constitute a fundamental step toward characterizing the pairs ( x, t) (x,t) for which F F is a perfect square.

## Decrease, boundedness and convergence on the admissible domain

### Admissible domain of a pair

Let k ≥ 4 k\geq 4 be a fixed integer and for a given pair ( x, t) ∈ ℕ ∗ 2 (x,t)\in\mathbb{N}^{*2}, we define its admissible domain:

 | 𝒟 x, t ( k) = { n ∈ ℕ, n ≥ N 1 ≥ 2 | n < k x and t ≥ 2 ​ n ​ x ( k ​ x − n) 2 }. \mathcal{D}_{x,t}^{(k)}=\left\{n\in\mathbb{N},\ n\geq N_{1}\geq 2\ \middle|\ n<kx\ \text{and}\ t\geq\frac{2nx}{(kx-n)^{2}}\right\}. |  |

The condition n < k ​ x n<kx ensures that x > n / k x>n/k (necessary condition in the quadratic equivalence). The second condition guarantees the positivity of F F.

###### Proposition 1 (Decrease and positivity on the domain).

Let k ≥ 4 k\geq 4 and ( x, t) ∈ ℕ ∗ 2 (x,t)\in\mathbb{N}^{*2} be fixed. For every n ∈ 𝒟 x, t ( k) n\in\mathcal{D}_{x,t}^{(k)}, we have:

 | F x, t ( k) ​ ( n) = t 2 ​ ( k ​ x − n) 2 − 2 ​ n ​ x ​ t ≥ 0. F_{x,t}^{(k)}(n)=t^{2}(kx-n)^{2}-2nxt\geq 0. |  |

Moreover, for all n 1, n 2 ∈ 𝒟 x, t ( k) n_{1},n_{2}\in\mathcal{D}_{x,t}^{(k)} with n 1 > n 2 n_{1}>n_{2}, we have:

 | F x, t ( k) ​ ( n 1) < F x, t ( k) ​ ( n 2). F_{x,t}^{(k)}(n_{1})<F_{x,t}^{(k)}(n_{2}). |  |

Thus, n ↦ F x, t ( k) ​ ( n) n\mapsto F_{x,t}^{(k)}(n) is strictly decreasing on 𝒟 x, t ( k) \mathcal{D}_{x,t}^{(k)}.

###### Proof.

Let n 1, n 2 ∈ 𝒟 x, t ( k) n_{1},n_{2}\in\mathcal{D}_{x,t}^{(k)} with n 1 > n 2 n_{1}>n_{2}.

Since n 2 < k ​ x n_{2}<kx (because n 2 ∈ 𝒟 x, t ( k) n_{2}\in\mathcal{D}_{x,t}^{(k)}), we have k ​ x − n 2 > 0 kx-n_{2}>0. Similarly, k ​ x − n 1 > 0 kx-n_{1}>0 and k ​ x − n 1 < k ​ x − n 2 kx-n_{1}<kx-n_{2}.

The function y ↦ y 2 y\mapsto y^{2} being strictly increasing on ℝ + \mathbb{R}_{+}, we obtain:

 | ( k ​ x − n 1) 2 < ( k ​ x − n 2) 2. (kx-n_{1})^{2}<(kx-n_{2})^{2}. |  |

Multiplying by t 2 > 0 t^{2}>0:

 | t 2 ​ ( k ​ x − n 1) 2 < t 2 ​ ( k ​ x − n 2) 2. t^{2}(kx-n_{1})^{2}<t^{2}(kx-n_{2})^{2}. |  |

Furthermore, n 1 > n 2 n_{1}>n_{2} and x, t > 0 x,t>0 give:

 | − 2 ​ n 1 ​ x ​ t < − 2 ​ n 2 ​ x ​ t. -2n_{1}xt<-2n_{2}xt. |  |

Adding these two inequalities, we obtain F ⁡ ( n 1) < F ⁡ ( n 2) F(n_{1})<F(n_{2}), which establishes the strict decrease .

Positivity follows directly from the condition t ≥ 2 ​ n ​ x ( k ​ x − n) 2 t\geq\frac{2nx}{(kx-n)^{2}}, which is equivalent to :

 | t 2 ​ ( k ​ x − n) 2 ≥ 2 ​ n ​ x ​ t. t^{2}(kx-n)^{2}\geq 2nxt. |  |

since t > 0 t>0, which subsequently gives F ≥ 0 F\geq 0. ∎

###### Proposition 2 (Convergence and boundedness on the domain).

Let k ≥ 4 k\geq 4 be a fixed integer and let ( x, t) ∈ ℕ ∗ 2 (x,t)\in\mathbb{N}^{*2} be a given pair. The sequence n ↦ F x, t ( k) ​ ( n) n\mapsto F_{x,t}^{(k)}(n), defined for n ∈ 𝒟 x, t ( k) n\in\mathcal{D}_{x,t}^{(k)}, satisfies:

1. 1.

It is strictly decreasing.

2. 2.

It is bounded below by 0 0.

3. 3.

By the monotone convergence theorem applied to the finite sequence ( F ⁡ ( n)) n ∈ 𝒟 x, t ( k) (F(n))_{n\in\mathcal{D}_{x,t}^{(k)}}, it attains its infimum at the last element of the domain. Let us denote

 | L x, t = min n ∈ 𝒟 x, t ( k) ⁡ F x, t ( k) ​ ( n) ≥ 0. L_{x,t}=\min_{n\in\mathcal{D}_{x,t}^{(k)}}F_{x,t}^{(k)}(n)\geq 0. |  |

In particular, L x, t = F x, t ( k) ​ ( N x, t) L_{x,t}=F_{x,t}^{(k)}(N_{x,t}) where N x, t = max ⁡ 𝒟 x, t ( k) N_{x,t}=\max\mathcal{D}_{x,t}^{(k)}.

4. 4.

For every n ∈ 𝒟 x, t ( k) n\in\mathcal{D}_{x,t}^{(k)}, we have the inequality:

 | 0 ≤ L x, t ≤ F x, t ( k) ​ ( n) ≤ F x, t ( k) ​ ( m x, t), 0\leq L_{x,t}\leq F_{x,t}^{(k)}(n)\leq F_{x,t}^{(k)}(m_{x,t}), |  |

where m x, t = min ⁡ 𝒟 x, t ( k) m_{x,t}=\min\mathcal{D}_{x,t}^{(k)} (the smallest admissible value).

5. 5.

In particular, F x, t ( k) F_{x,t}^{(k)} is bounded on 𝒟 x, t ( k) \mathcal{D}_{x,t}^{(k)} and we may take

 | C ⁡ ( x, t) = F x, t ( k) ​ ( m x, t) C(x,t)=F_{x,t}^{(k)}(m_{x,t}) |  |

as an explicit upper bound (independent of n n within this domain).

###### Proof.

Points 1 and 2 follow from the previous proposition. Point 3 is a direct application of the monotone convergence theorem. Point 4 uses the decreasing property: for all n ≥ m x, t n\geq m_{x,t} in the domain, F ⁡ ( n) ≤ F ⁡ ( m x, t) F(n)\leq F(m_{x,t}). Moreover, since L x, t L_{x,t} is the limit, we have L x, t ≤ F ⁡ ( n) L_{x,t}\leq F(n) for all n n (as the sequence decreases to its limit). Point 5 is an immediate consequence of point 4. ∎

## Quadratic equivalence theorem

Let k ≥ 4 k\geq 4 be a fixed integer, and let n ≥ N 1 ≥ 2 n\geq N_{1}\geq 2 be a given integer. Let x ∈ ℕ ∗ x\in\mathbb{N}^{*} be such that

 | x ≥ ⌊ n k ⌋ + 1 ( which ensures ​ k ​ x > n). x\geq\left\lfloor\frac{n}{k}\right\rfloor+1\quad(\text{which ensures }kx>n). |  |

Then the following two statements are equivalent:

1. 1.

There exist y, z ∈ ℕ ∗ y,z\in\mathbb{N}^{*} such that

 | k n = 1 x + 1 y + 1 z. \frac{k}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}. |  |

2. 2.

There exists t ∈ ℕ ∗ t\in\mathbb{N}^{*} such that

 | F x, t ( k) ​ ( n) = t 2 ​ ( k ​ x − n) 2 − 2 ​ n ​ x ​ t F_{x,t}^{(k)}(n)=t^{2}(kx-n)^{2}-2nxt |  |

is a perfect square.

Moreover, when (2) holds and we set m = F x, t ( k) ​ ( n) ∈ ℕ m=\sqrt{F_{x,t}^{(k)}(n)}\in\mathbb{N}, an explicit solution of (1) is given by

 | y = t ⁡ ( k ​ x − n) + m, z = t ⁡ ( k ​ x − n) − m, y=t(kx-n)+m,\qquad z=t(kx-n)-m, |  |

(or the reverse order).

###### Proof.

(1) ⇒ \Rightarrow (2). Suppose there exist y, z ∈ ℕ ∗ y,z\in\mathbb{N}^{*} satisfying (1). Then

 | 1 y + 1 z = k n − 1 x = k ​ x − n n ​ x. \frac{1}{y}+\frac{1}{z}=\frac{k}{n}-\frac{1}{x}=\frac{kx-n}{nx}. |  |

Reducing to a common denominator yields

 | y + z y ​ z = k ​ x − n n ​ x, \frac{y+z}{yz}=\frac{kx-n}{nx}, |  |

that is,

 | n ​ x ​ ( y + z) = y ​ z ​ ( k ​ x − n). nx(y+z)=yz(kx-n). |  | (*) |

Set

 | S = y + z and P = y ​ z. S=y+z\quad\text{and}\quad P=yz. |  |

Equation (*) becomes n ​ x ​ S = P ⁡ ( k ​ x − n) nxS=P(kx-n). Since S S and P P are integers, we may write S = 2 ​ t ​ ( k ​ x − n) S=2t(kx-n) for some t ∈ ℕ ∗ t\in\mathbb{N}^{*} (the factor 2 2 is introduced to simplify the discriminant computation). Substituting into (*), we obtain

 | n ​ x ⋅ 2 ​ t ​ ( k ​ x − n) = P ⁡ ( k ​ x − n), nx\cdot 2t(kx-n)=P(kx-n), |  |

hence P = 2 ​ n ​ x ​ t P=2nxt. Thus,

 | y + z = 2 ​ t ​ ( k ​ x − n), y ​ z = 2 ​ n ​ x ​ t. y+z=2t(kx-n),\qquad yz=2nxt. |  |

Consequently, y y and z z are the roots of the quadratic equation

 | V 2 − 2 ​ t ​ ( k ​ x − n) ​ V + 2 ​ n ​ x ​ t = 0. V^{2}-2t(kx-n)V+2nxt=0. |  |

Its discriminant is

 | Δ = [2 ​ t ​ ( k ​ x − n)] 2 − 4 ⋅ 2 ​ n ​ x ​ t = 4 ​ [t 2 ​ ( k ​ x − n) 2 − 2 ​ n ​ x ​ t] = 4 ​ F x, t ( k) ​ ( n). \Delta=\bigl[2t(kx-n)\bigr]^{2}-4\cdot 2nxt=4\bigl[t^{2}(kx-n)^{2}-2nxt\bigr]=4\,F_{x,t}^{(k)}(n). |  |

For y y and z z to be integers, Δ \Delta must be a perfect square, which is equivalent to F x, t ( k) ​ ( n) F_{x,t}^{(k)}(n) being a perfect square.

(2) ⇒ \Rightarrow (1). Suppose there exists x, t ∈ ℕ ∗ x,t\in\mathbb{N}^{*} such that F x, t ( k) ​ ( n) = m 2 F_{x,t}^{(k)}(n)=m^{2} with m ∈ ℕ m\in\mathbb{N}. Then the equation

 | V 2 − 2 ​ t ​ ( k ​ x − n) ​ V + 2 ​ n ​ x ​ t = 0 V^{2}-2t(kx-n)V+2nxt=0 |  |

has discriminant Δ = 4 ​ m 2 \Delta=4m^{2}, so its roots are

 | V = 2 ​ t ​ ( k ​ x − n) ± 2 ​ m 2 = t ⁡ ( k ​ x − n) ± m. V=\frac{2t(kx-n)\pm 2m}{2}=t(kx-n)\pm m. |  |

Set

 | y = t ⁡ ( k ​ x − n) + m, z = t ⁡ ( k ​ x − n) − m. y=t(kx-n)+m,\qquad z=t(kx-n)-m. |  |

A direct computation gives

 | y + z = 2 ​ t ​ ( k ​ x − n), y ​ z = ( t ⁡ ( k ​ x − n) + m) ​ ( t ⁡ ( k ​ x − n) − m) = t 2 ​ ( k ​ x − n) 2 − m 2. y+z=2t(kx-n),\qquad yz=\bigl(t(kx-n)+m\bigr)\bigl(t(kx-n)-m\bigr)=t^{2}(kx-n)^{2}-m^{2}. |  |

Since m 2 = t 2 ​ ( k ​ x − n) 2 − 2 ​ n ​ x ​ t m^{2}=t^{2}(kx-n)^{2}-2nxt, we obtain y ​ z = 2 ​ n ​ x ​ t yz=2nxt. We then verify

 | y + z y ​ z = 2 ​ t ​ ( k ​ x − n) 2 ​ n ​ x ​ t = k ​ x − n n ​ x, \frac{y+z}{yz}=\frac{2t(kx-n)}{2nxt}=\frac{kx-n}{nx}, |  |

which implies

 | 1 y + 1 z = k n − 1 x, \frac{1}{y}+\frac{1}{z}=\frac{k}{n}-\frac{1}{x}, |  |

and finally k n = 1 x + 1 y + 1 z \displaystyle\frac{k}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}.

The numbers y y and z z are indeed positive integers. It is immediate that y ∈ ℕ ∗ y\in\mathbb{N}^{*}, since k ​ x − n > 0 kx-n>0 because

 | x ≥ ⌊ n k ⌋ + 1 > n k, x\geq\left\lfloor\frac{n}{k}\right\rfloor+1>\frac{n}{k}, |  |

and with t ∈ ℕ ∗ t\in\mathbb{N}^{*}, x ∈ ℕ ∗ x\in\mathbb{N}^{*}, n ∈ ℕ ∗ n\in\mathbb{N}^{*} and m ∈ ℕ m\in\mathbb{N}, we have y ∈ ℕ ∗ y\in\mathbb{N}^{*}.

Let us now show that z ∈ ℕ ∗ z\in\mathbb{N}^{*}. From

 | m 2 = t 2 ​ ( k ​ x − n) 2 − 2 ​ n ​ x ​ t < t 2 ​ ( k ​ x − n) 2, m^{2}=t^{2}(kx-n)^{2}-2nxt<t^{2}(kx-n)^{2}, |  |

since − 2 ​ n ​ x ​ t < 0 -2nxt<0 for n, x, t > 0 n,x,t>0, and since the square root function is increasing on ℝ + \mathbb{R}_{+}, we obtain

 | m < t ⁡ ( k ​ x − n). m<t(kx-n). |  |

Hence t ⁡ ( k ​ x − n) − m > 0 t(kx-n)-m>0, and since t, x, n, m t,x,n,m are integers, it follows that

 | z = t ⁡ ( k ​ x − n) − m ∈ ℕ ∗. z=t(kx-n)-m\in\mathbb{N}^{*}. |  |

∎

remark. This equivalence holds for all n ≥ N 1 n\geq N_{1}, where N 1 N_{1} is a threshold depending on k k. The integer N 1 N_{1} is chosen such that for every n ≥ N 1 n\geq N_{1}, any solution ( x, y, z) (x,y,z) of k n = 1 x + 1 y + 1 z \frac{k}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z} yields an integer

 | t = y + z 2 ​ ( k ​ x − n) = y ​ z 2 ​ n ​ x ∈ ℕ ∗, t=\frac{y+z}{2(kx-n)}=\frac{yz}{2nx}\in\mathbb{N}^{*}, |  |

so that we may write y = t ⁡ ( k ​ x − n) + m y=t(kx-n)+m and z = t ⁡ ( k ​ x − n) − m z=t(kx-n)-m with m = F x, t ( k) ​ ( n) ∈ ℕ m=\sqrt{F_{x,t}^{(k)}(n)}\in\mathbb{N}.

For k = 4 k=4 (Erdős–Straus), one has N 1 = 2 N_{1}=2. For k ≥ 5 k\geq 5, numerical experiments show the existence of a threshold N 0 < N 1 N_{0}<N_{1} below which solutions exist but do not yield an integer t t; instead they give a rational t t that still satisfies the parametrization. This phenomenon is due to the scarcity of Egyptian fraction decompositions for small n n in these cases. In such situations, F F becomes a rational perfect square, yet still produces integer solutions y, z y,z satisfying the conjecture.

In this work, we impose the condition t ∈ ℕ ∗ t\in\mathbb{N}^{*} to ensure that F F is an integer, which facilitates its study. The determination of an explicit value for N 1 N_{1} in terms of k k remains an open problem, related to the complexity of the generalized Erdős–Straus and Sierpiński conjectures. Even in the current literature, the exact value of N 0 N_{0} (the smallest integer from which the decomposition exists) is not known as a function of k k; the generalized conjecture merely states that the decomposition exists for all but finitely many n n. Consequently, expressing N 1 ≥ N 0 N_{1}\geq N_{0} explicitly is even more challenging.

Numerical simulations indicate that the gap between N 0 N_{0} and N 1 N_{1} grows slowly with k k. For k = 4 k=4, we have N 0 = N 1 = 2 N_{0}=N_{1}=2. For k = 5 k=5 (Sierpiński’s conjecture), N 0 = 2 N_{0}=2 and N 1 = 11 N_{1}=11. This does not pose a problem for our approach: if we can show that F F always yields an integer perfect square for all n ≥ N 1 n\geq N_{1}, the remaining range N 0 ≤ n < N 1 N_{0}\leq n<N_{1} can be handled numerically using the same function F F with rational values of t t. In [1], we proved the elementary fact that N 0 N_{0} cannot be strictly less than k / 3 k/3

This last theorem reduces the search for solutions of the Erdős–Straus conjecture ( k = 4 k=4), the Sierpiński conjecture ( k = 5 k=5), or their generalizations ( k ≥ 6 k\geq 6), to the problem of finding parameters x, t x,t for which F x, t ( k) ​ ( n) F_{x,t}^{(k)}(n) is a perfect square. The study of the boundedness, decrease, and other properties of F F thus becomes central.

lemma (Zero Lemma) Let k ≥ 4 k\geq 4 be an integer, and let x, t ∈ ℕ ∗ x,t\in\mathbb{N}^{*} be fixed. Consider n ↦ F x, t ( k) ​ ( n) n\mapsto F_{x,t}^{(k)}(n) defined on its admissible domain 𝒟 x, t = { n ≥ N 1 ≥ 2 ∣ n < k ​ x ​ and ​ t ≥ 2 ​ n ​ x ( k ​ x − n) 2 } \mathcal{D}_{x,t}=\{n\geq N_{1}\geq 2\mid n<kx\text{ and }t\geq\dfrac{2nx}{(kx-n)^{2}}\}.

If F x, t ( k) ​ ( n 0) = 0 F_{x,t}^{(k)}(n_{0})=0 for some n 0 ∈ 𝒟 x, t n_{0}\in\mathcal{D}_{x,t}, then n 0 n_{0} is necessarily the upper bound of 𝒟 x, t \mathcal{D}_{x,t}.

###### Proof.

By Proposition 1, the sequence n ↦ F x, t ( k) ​ ( n) n\mapsto F_{x,t}^{(k)}(n) is strictly decreasing on 𝒟 x, t \mathcal{D}_{x,t}.

Suppose there exists n 0 ∈ 𝒟 x, t n_{0}\in\mathcal{D}_{x,t} with F ⁡ ( n 0) = 0 F(n_{0})=0, and that n 0 n_{0} is not the upper bound of 𝒟 x, t \mathcal{D}_{x,t}. Then there would exist n 1 > n 0 n_{1}>n_{0} with n 1 ∈ 𝒟 x, t n_{1}\in\mathcal{D}_{x,t}.

By strict decrease, we would have F ⁡ ( n 1) < F ⁡ ( n 0) = 0 F(n_{1})<F(n_{0})=0. But since n 1 ∈ 𝒟 x, t n_{1}\in\mathcal{D}_{x,t}, the positivity condition (Proposition 1) implies F ⁡ ( n 1) ≥ 0 F(n_{1})\geq 0. Hence we obtain 0 ≤ F ⁡ ( n 1) < 0 0\leq F(n_{1})<0, a contradiction.

Therefore, such an n 1 n_{1} cannot exist, and n 0 n_{0} is indeed the greatest element of 𝒟 x, t \mathcal{D}_{x,t}. ∎

###### Proposition 3 (Explicit symmetric solutions for three residue classes).

For the classical Erdős–Straus conjecture ( k = 4 k=4), all integers n ≥ 2 n\geq 2 belonging to the residue classes

 | n ≡ 0, 2, 3 ( mod 4) n\equiv 0,\ 2,\ 3\pmod{4} |  |

admit symmetric solutions y = z y=z. More precisely, for each such n n, there exists an explicit pair ( x, t) ∈ ℕ ∗ 2 (x,t)\in\mathbb{N}^{*2} such that F x, t ( 4) ​ ( n) = 0 F_{x,t}^{(4)}(n)=0, yielding

 | y = z = t ⁡ ( 4 ​ x − n) and 4 n = 1 x + 1 y + 1 z. y=z=t(4x-n)\quad\text{and}\quad\frac{4}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}. |  |

###### Proof.

For each residue class modulo 4 4 (except n ≡ 1 ( mod 4) n\equiv 1\pmod{4}), we construct explicit pairs ( x, t) (x,t) with F x, t ( 4) ​ ( n) = 0 F_{x,t}^{(4)}(n)=0:

- •

If n = 4 ​ r n=4r with r ∈ ℕ ∗ r\in\mathbb{N}^{*}, take x = r + 1 x=r+1 and t = r ⁡ ( r + 1) 2 t=\dfrac{r(r+1)}{2}. Then 4 ​ x − n = 4 4x-n=4 and a direct computation shows F x, t ( 4) ​ ( n) = 0 F_{x,t}^{(4)}(n)=0.

- •

If n = 4 ​ r + 2 n=4r+2 with r ∈ ℕ r\in\mathbb{N}, take x = r + 1 x=r+1 and t = ( 2 ​ r + 1) ​ ( r + 1) t=(2r+1)(r+1). Then 4 ​ x − n = 2 4x-n=2 and F x, t ( 4) ​ ( n) = 0 F_{x,t}^{(4)}(n)=0.

- •

If n = 4 ​ r + 3 n=4r+3 with r ∈ ℕ r\in\mathbb{N}, take x = r + 1 x=r+1 and t = 2 ​ ( 4 ​ r + 3) ​ ( r + 1) t=2(4r+3)(r+1). Then 4 ​ x − n = 1 4x-n=1 and F x, t ( 4) ​ ( n) = 0 F_{x,t}^{(4)}(n)=0.

These three classes cover all integers except those congruent to 1 1 modulo 4 4, which represent asymptotically 25 % 25\% of all integers. Hence at least 75 % 75\% of integers are zeros of F F. For each such n n, the corresponding formulas yield symmetric solutions y = z = t ⁡ ( 4 ​ x − n) y=z=t(4x-n) that satisfy the conjecture. ∎

###### Proposition 4 (Explicit symmetric solutions for a subfamily of n ≡ 1 ( mod 4) n\equiv 1\pmod{4}).

Let n ≡ 1 ( mod 4) n\equiv 1\pmod{4}, written as n = 4 ​ r + 1 n=4r+1 with r ∈ ℕ ∗ r\in\mathbb{N}^{*}. Let b b be an odd integer such that b ≡ 3 ( mod 4) b\equiv 3\pmod{4}, and define

 | x = n + b 4. x=\frac{n+b}{4}. |  |

If b | n b\mid n (equivalently b | ( 4 ​ r + 1) b\mid(4r+1)), then there exists an integer t ∈ ℕ ∗ t\in\mathbb{N}^{*} such that F x, t ( 4) ​ ( n) = 0 F_{x,t}^{(4)}(n)=0. This yields the symmetric solution

 | y = z = t ⁡ ( 4 ​ x − n) = t ​ b, y=z=t(4x-n)=tb, |  |

satisfying

 | 4 n = 1 x + 1 y + 1 z. \frac{4}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}. |  |

###### Proof.

Since n = 4 ​ r + 1 n=4r+1 and b ≡ 3 ( mod 4) b\equiv 3\pmod{4}, we have

 | n + b ≡ 1 + 3 ≡ 0 ( mod 4), n+b\equiv 1+3\equiv 0\pmod{4}, |  |

hence

 | x = n + b 4 ∈ ℕ ∗. x=\frac{n+b}{4}\in\mathbb{N}^{*}. |  |

We compute

 | 4 ​ x − n = 4 ​ ( n + b) 4 − n = n + b − n = b. 4x-n=4\frac{(n+b)}{4}-n=n+b-n=b. |  |

From the definition

F x, t ( 4) ​ ( n) = t 2 ​ ( 4 ​ x − n) 2 − 2 ​ n ​ x ​ t F_{x,t}^{(4)}(n)=t^{2}(4x-n)^{2}-2nxt

the condition F x, t ( 4) ​ ( n) = 0 F_{x,t}^{(4)}(n)=0 gives

 | t = 2 ​ n ​ x ( 4 ​ x − n) 2, t=\frac{2nx}{(4x-n)^{2}}, |  |

Since 4 ​ x − n = b 4x-n=b, this becomes

 | t = 2 ​ n ​ x b 2. t=\frac{2nx}{b^{2}}. |  |

Substituting n = 4 ​ r + 1 n=4r+1 and x = ( 4 ​ r + 1 + b) 4 x=\frac{(4r+1+b)}{4} yields

 | t = 2 ​ ( 4 ​ r + 1) ​ 4 ​ r + 1 + b 4 b 2 = ( 4 ​ r + 1) ​ ( 4 ​ r + 1 + b) 2 ​ b 2. t=\frac{2(4r+1)\frac{4r+1+b}{4}}{b^{2}}=\frac{(4r+1)(4r+1+b)}{2b^{2}}. |  |

Assume now that b | ( 4 ​ r + 1) b\mid(4r+1). Then there exists an integer w ≥ 1 w\geq 1 such that

 | 4 ​ r + 1 = b ​ w. 4r+1=bw. |  |

Hence

 | 4 ​ r + 1 + b = b ​ w + b = b ⁡ ( w + 1), 4r+1+b=bw+b=b(w+1), |  |

and therefore

 | ( 4 ​ r + 1) ​ ( 4 ​ r + 1 + b) = b 2 ​ w ​ ( w + 1). (4r+1)(4r+1+b)=b^{2}w(w+1). |  |

Substituting into the expression of t t, we obtain

 | t = b 2 ​ w ​ ( w + 1) 2 ​ b 2 = w ⁡ ( w + 1) 2. t=\frac{b^{2}w(w+1)}{2b^{2}}=\frac{w(w+1)}{2}. |  |

Since w w and w + 1 w+1 are consecutive integers, one of them is even. Thus w ⁡ ( w + 1) w(w+1) is divisible by 2 2, and consequently

 | t ∈ ℕ ∗. t\in\mathbb{N}^{*}. |  |

Therefore, for every b ≡ 3 ( mod 4) b\equiv 3\pmod{4}, the condition

 | b | ( 4 ​ r + 1) b\mid(4r+1) |  |

defines an infinite arithmetic progression in r r, and hence in n n. This provides infinitely many explicit subfamilies in the class n ≡ 1 ( mod 4) n\equiv 1\pmod{4} yielding solutions

 | y = z = t ⁡ ( 4 ​ x − n) = t ​ b y=z=t(4x-n)=tb |  |

that satisfy the Erdős–Straus equation. ∎

Example Let b = 3 b=3, which satisfies 3 ≡ 3 ( mod 4) 3\equiv 3\pmod{4}.

The condition 3 | ( 4 ​ r + 1) 3\mid(4r+1) is equivalent to

 | 4 ​ r + 1 ≡ 0 ( mod 3). 4r+1\equiv 0\pmod{3}. |  |

Since 4 ≡ 1 ( mod 3) 4\equiv 1\pmod{3}, this becomes

 | r + 1 ≡ 0 ( mod 3), r+1\equiv 0\pmod{3}, |  |

hence

 | r ≡ 2 ( mod 3). r\equiv 2\pmod{3}. |  |

We may write r = 3 ​ a + 2 r=3a+2. Then

 | n = 4 ​ r + 1 = 4 ​ ( 3 ​ a + 2) + 1 = 12 ​ a + 9. n=4r+1=4(3a+2)+1=12a+9. |  |

Thus all integers of the form

 | n = 12 ​ a + 9 n=12a+9 |  |

form an infinite subfamily of integers congruent to 1 ( mod 4) 1\pmod{4} for which the above construction produces an integer t t and hence a solution arising from F = 0 F=0.

### An example of application to a residue class modulo 840

Mordell proved that for every integer n n not congruent to 1, 11 2, 13 2, 17 2, 19 2, 23 2 1,11^{2},13^{2},17^{2},19^{2},23^{2} modulo 840 840, the equation

 | 4 n = 1 x + 1 y + 1 z \frac{4}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z} |  |

admits a solution. Thus, numbers n ≡ 1 ( mod 840) n\equiv 1\pmod{840} belong to the cases not covered by Mordell’s result.

In this section, we show that our construction, based on the existence of a divisor b ≡ 3 ( mod 4) b\equiv 3\pmod{4} of n n, provides infinitely many symmetric solutions for some of these numbers, namely those of the form n = 840 ​ k + 1 n=840k+1.

Consider for instance b = 11 b=11, which satisfies 11 ≡ 3 ( mod 4) 11\equiv 3\pmod{4}. We look for integers k k such that 11 11 divides n = 840 ​ k + 1 n=840k+1.

The condition 11 | ( 840 ​ k + 1) 11\mid(840k+1) is equivalent to

 | 840 k + 1 ≡ 0 ( mod 11) ⟺ 840 k ≡ − 1 ≡ 10 ( mod 11). 840k+1\equiv 0\pmod{11}\quad\Longleftrightarrow\quad 840k\equiv-1\equiv 10\pmod{11}. |  |

Since 840 ≡ 4 ( mod 11) 840\equiv 4\pmod{11}, this becomes

 | 4 ​ k ≡ 10 ( mod 11). 4k\equiv 10\pmod{11}. |  |

We look for a multiple of 4 4 that is congruent to 10 10 modulo 11 11. One finds that 4 × 8 = 32 ≡ 10 ( mod 11) 4\times 8=32\equiv 10\pmod{11}. Hence

 | 4 ​ k ≡ 4 × 8 ( mod 11). 4k\equiv 4\times 8\pmod{11}. |  |

Since gcd ⁡ ( 4, 11) = 1 \gcd(4,11)=1, Gauss’s lemma implies that

 | k ≡ 8 ( mod 11). k\equiv 8\pmod{11}. |  |

Thus, all integers k k of the form k = 8 + 11 ​ m k=8+11m (with m ∈ ℕ m\in\mathbb{N}) satisfy the condition. This yields infinitely many values of k k.

Example : For m = 0 m=0, we have k = 8 k=8 and n = 840 × 8 + 1 = 6721 n=840\times 8+1=6721. One checks that 6721 = 11 × 611 6721=11\times 611. Since n n is divisible by b = 11 b=11 and 11 ≡ 3 ( mod 4) 11\equiv 3\pmod{4}, our construction applies. We obtain

 | x = n + b 4 = 6721 + 11 4 = 1683, x=\frac{n+b}{4}=\frac{6721+11}{4}=1683, |  |

 | t = n ⁡ ( n + b) 2 ​ b 2 = 6721 × 6732 2 × 121 = 186 966, t=\frac{n(n+b)}{2b^{2}}=\frac{6721\times 6732}{2\times 121}=186\,966, |  |

and therefore

 | y = z = t × b = 186 966 × 11 = 2 056 626. y=z=t\times b=186\,966\times 11=2\,056\,626. |  |

A direct verification shows that these values satisfy

 | 4 6721 = 1 1683 + 1 2 056 626 + 1 2 056 626. \frac{4}{6721}=\frac{1}{1683}+\frac{1}{2\,056\,626}+\frac{1}{2\,056\,626}. |  |

.

The same approach can be applied to the five other residue classes in Mordell’s theorem — namely, the integers n ≡ 1,121,169,289,361, 529 ( mod 840) n\equiv 1,121,169,289,361,529\pmod{840} not covered by his result — by explicitly choosing an integer b ≡ 3 ( mod 4) b\equiv 3\pmod{4} dividing n n. In what follows, we prove a stronger result: we show that the natural density of integers n ≡ 1 ( mod 4) n\equiv 1\pmod{4} admitting a divisor b ≡ 3 ( mod 4) b\equiv 3\pmod{4} is equal to 1 1.

## Natural density of integers n ≡ 1 ( mod 4) n\equiv 1\pmod{4} admitting a prime divisor ≡ 3 ( mod 4) \equiv 3\pmod{4}

### 1. Definition of the sets

Let ℙ \mathbb{P} denote the set of prime numbers. We define

 | 𝒜 = { n ≥ 1: n ≡ 1 ( mod 4), ∃ p ∈ ℙ, p ≡ 3 ( mod 4), p ∣ n }, \mathcal{A}=\{n\geq 1:n\equiv 1\pmod{4},\ \exists p\in\mathbb{P},\ p\equiv 3\pmod{4},\ p\mid n\}, |  |

and

 | ℬ = { n ≥ 1: n ≡ 1 ( mod 4), ∀ p ∈ ℙ, ( p ∣ n ⇒ p ≡ 1 ( mod 4)) }. \mathcal{B}=\{n\geq 1:n\equiv 1\pmod{4},\ \forall p\in\mathbb{P},\ (p\mid n\Rightarrow p\equiv 1\pmod{4})\}. |  |

The elements of ℬ \mathcal{B} are exactly the integers not captured by our construction.

We aim to show:

 | | ℬ ∩ [1, x] | x ⟶ 0 as ​ x → + ∞. \frac{|\mathcal{B}\cap[1,x]|}{x}\longrightarrow 0\quad\text{as }x\to+\infty. |  |

### 2. Multiplicative structure

An integer belongs to ℬ \mathcal{B} if and only if

 | n = ∏ p ≡ 1 ( mod 4) p α p, n=\prod_{p\equiv 1\pmod{4}}p^{\alpha_{p}}, |  |

where α p ≥ 0 \alpha_{p}\geq 0 and almost all α p \alpha_{p} are zero.

Thus ℬ \mathcal{B} is a multiplicative set.

We introduce its Dirichlet series, denoted by D ⁡ ( s) D(s):

 | D ⁡ ( s) = ∑ n ∈ ℬ 1 n s. D(s)=\sum_{n\in\mathcal{B}}\frac{1}{n^{s}}. |  |

For real s > 1 s>1, the series converges absolutely. By multiplicativity, we obtain the Euler product:

 | D ⁡ ( s) = ∏ p ≡ 1 ( mod 4) ( 1 − 1 p s) − 1. D(s)=\prod_{p\equiv 1\pmod{4}}\left(1-\frac{1}{p^{s}}\right)^{-1}. |  |

We now compare with the Riemann zeta function:

 | ζ ⁡ ( s) = ∏ p ( 1 − 1 p s) − 1. \zeta(s)=\prod_{p}\left(1-\frac{1}{p^{s}}\right)^{-1}. |  |

To relate D ⁡ ( s) D(s) to ζ ⁡ ( s) \zeta(s), we separate the prime p = 2 p=2 (which does not appear in ℬ \mathcal{B}) and the primes congruent to 3 3 modulo 4 4:

 | ζ ⁡ ( s) = ( 1 − 1 2 s) − 1 ​ ∏ p ≡ 1 ( mod 4) ( 1 − 1 p s) − 1 ​ ∏ p ≡ 3 ( mod 4) ( 1 − 1 p s) − 1. \zeta(s)=\left(1-\frac{1}{2^{s}}\right)^{-1}\prod_{p\equiv 1\pmod{4}}\left(1-\frac{1}{p^{s}}\right)^{-1}\prod_{p\equiv 3\pmod{4}}\left(1-\frac{1}{p^{s}}\right)^{-1}. |  |

It follows that

 | ∏ p ≡ 1 ( mod 4) ( 1 − 1 p s) − 1 = ζ ⁡ ( s) ​ ( 1 − 1 2 s) ​ ∏ p ≡ 3 ( mod 4) ( 1 − 1 p s). \prod_{p\equiv 1\pmod{4}}\left(1-\frac{1}{p^{s}}\right)^{-1}=\zeta(s)\left(1-\frac{1}{2^{s}}\right)\prod_{p\equiv 3\pmod{4}}\left(1-\frac{1}{p^{s}}\right). |  |

Therefore,

 | D ⁡ ( s) = ζ ⁡ ( s) ​ ( 1 − 1 2 s) ​ ∏ p ≡ 3 ( mod 4) ( 1 − 1 p s). D(s)=\zeta(s)\left(1-\frac{1}{2^{s}}\right)\prod_{p\equiv 3\pmod{4}}\left(1-\frac{1}{p^{s}}\right). |  |

### 3. Behavior near s = 1 s=1

It is well known that, as s → 1 + s\to 1^{+} (real),

 | ζ ⁡ ( s) ∼ 1 s − 1. \zeta(s)\sim\frac{1}{s-1}. |  |

Consider the product:

 | P ⁡ ( s) = ∏ p ≡ 3 ( mod 4) ( 1 − 1 p s). P(s)=\prod_{p\equiv 3\pmod{4}}\left(1-\frac{1}{p^{s}}\right). |  |

Using the logarithmic approximation:

 | log P ( s) = ∑ p ≡ 3 ( mod 4) log ( 1 − 1 p s) ∼ − ∑ p ≡ 3 ( mod 4) 1 p s. \log P(s)=\sum_{p\equiv 3\pmod{4}}\log\left(1-\frac{1}{p^{s}}\right)\sim-\sum_{p\equiv 3\pmod{4}}\frac{1}{p^{s}}. |  |

By Dirichlet’s theorem on arithmetic progressions,

 | ∑ p ≡ 3 ( mod 4) 1 p = + ∞. \sum_{p\equiv 3\pmod{4}}\frac{1}{p}=+\infty. |  |

Therefore, as s → 1 + s\to 1^{+},

 | ∑ p ≡ 3 ( mod 4) 1 p s ⟶ + ∞, \sum_{p\equiv 3\pmod{4}}\frac{1}{p^{s}}\longrightarrow+\infty, |  |

and consequently

 | P ⁡ ( s) ⟶ 0. P(s)\longrightarrow 0. |  |

Moreover, the factor ( 1 − 1 2 s) \left(1-\frac{1}{2^{s}}\right) tends to the nonzero constant 1 − 1 2 = 1 2 1-\frac{1}{2}=\frac{1}{2} as s → 1 + s\to 1^{+}. Hence it does not affect the vanishing behavior of D ⁡ ( s) D(s) relative to ζ ⁡ ( s) \zeta(s).

It follows that

 | D ⁡ ( s) = o ⁡ ( 1 s − 1). D(s)=o\!\left(\frac{1}{s-1}\right). |  |

### 4. Tauberian consequence

The series D ⁡ ( s) D(s) converges absolutely for ℜ ⁡ ( s) > 1 \Re(s)>1 and extends analytically to a meromorphic function on ℜ ⁡ ( s) > 0 \Re(s)>0, with a singularity at s = 1 s=1 weaker than a simple pole. A standard Tauberian theorem (of Ikehara–Wiener type) implies that if a Dirichlet series with nonnegative coefficients has a singularity at s = 1 s=1 which is o ⁡ ( 1 / ( s − 1)) o(1/(s-1)), then the corresponding set has natural density zero.

Thus,

 | | ℬ ∩ [1, x] | = o ⁡ ( x). |\mathcal{B}\cap[1,x]|=o(x). |  |

Hence

 | dens ⁡ ( ℬ) = 0. \boxed{\operatorname{dens}(\mathcal{B})=0.} |  |

### 5. Conclusion

Consequently,

 | | 𝒜 ∩ [1, x] | x = 1 − o ⁡ ( 1). \frac{|\mathcal{A}\cap[1,x]|}{x}=1-o(1). |  |

In other words, the proportion of integers n ≡ 1 ( mod 4) n\equiv 1\pmod{4} possessing at least one prime divisor p ≡ 3 ( mod 4) p\equiv 3\pmod{4} tends to 1 1 as x → + ∞ x\to+\infty.

We have exhibited explicit solutions for all integers n ≢ 1 ( mod 4) n\not\equiv 1\pmod{4}, and for the class n ≡ 1 ( mod 4) n\equiv 1\pmod{4}, we have proved that our construction applies to almost all such integers, the exceptions having natural density zero. In particular, this provides infinitely many new explicit families of symmetric solutions for numbers not covered by Mordell’s theorem, and establishes that the Erdős–Straus conjecture holds for a proportion of integers tending to 1 1.

## References

- [1] P. U. Mballa, Partial Resolution of the Erdos-Straus, Sierpinski, and Generalized Erdos-Straus Conjectures Using New Analytical Formulas, preprint, [arXiv:2502.20935 [math.NT]][5], 2026.
- [2] T. Tao, The number of solutions to 4 n = 1 x + 1 y + 1 z \frac{4}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}, preprint, [arXiv:1107.1010 [math.NT]][6], 2011
- [3] P. Erdős, Az 1/x 1 + 1/x 2 + . . . + 1/x n = a/b egyenlet egész számú megoldásairól, Mat. Lapok 1 (1950), 192–210.
- [4] L. Bernstein, Zur Lösung der diophantischen Gleichung m/n = 1/x + 1/y + 1/z, insbesondere im Fall m = 4, J. Reine Angew. Math. 211 (1962), 1–10.
- [5] L. J. Mordell, Diophantine Equations, Pure and Applied Mathematics 30, Academic Press, 1969.
- [6] M. R. Obláth, Sur l’équation diophantienne 4/n = 1/x 1 + 1/x 2 + 1/x 3, Mathesis 59 (1950), 308–316.
- [7] L. Rosati, Sull’equazione diofantea 4/n = 1/x 1 + 1/x 2 + 1/x 3, Boll. Un. Mat. Ital. (3) 9 (1954), 59–63.
- [8] K. Yamamoto, On the Diophantine Equation 4/n = 1/x + 1/y + 1/z, Mem. Fac. Sci. Kyushu Univ. Ser. A 19 (1965), 37–47.
- [9] R. W. Jollenstein, A note on the Egyptian problem, Congressus Numerantium 17, Utilitas Math., Winnipeg, Man. In Proceedings of the Seventh Southeastern Conference on Combinatorics, Graph Theory, and Computing, 351–364, Louisiana State Univ., Baton Rouge, La., 1976.
- [10] D. G. Terzi, On a conjecture by Erdős-Straus, Nordisk Tidskr. Informations-Behandling (BIT) 11 (1971), 212–216.
- [11] I. Kotsireas, The Erdős-Straus conjecture on Egyptian fractions, Paul Erdős and his mathematics (Budapest, 1999), 140–144, János Bolyai Math. Soc., Budapest, 1999.
- [12] A. Swett, The Erdős-Straus Conjecture, page web, [http://math.uindy.edu/swett/esc.htm][7], accessed on 27 July 2011.
- [13] M. Bello-Hernández, M. Benito, E. Fernández, On egyptian fractions, preprint, arXiv:1010.2035, version 2, 30 April 2012.
- [14] S. Salez, The Erdős-Straus conjecture: New modular equations and checking up to N = 10 17, preprint, arXiv:1406.6307, 2014.
- [15] [Reference to the article on the history of Sierpiński], [arXiv:2508.07367][8]


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:philemon-urbain.mballa@etu.u-paris.fr
[4]: mailto:philemonmballa@gmail.com
[5]: https://arxiv.org/abs/2502.20935
[6]: https://arxiv.org/abs/1107.1010
[7]: http://math.uindy.edu/swett/esc.htm
[8]: https://arxiv.org/html/2508.07367v1
