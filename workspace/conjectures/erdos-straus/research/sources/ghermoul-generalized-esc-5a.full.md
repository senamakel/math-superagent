<!-- source: https://arxiv.org/html/2508.07367v1 | converted from HTML -->

Almost a Complete Proof of the Generalized Erdős–Straus Conjecture: 5/a = 1/b + 1/c + 1/d

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY-SA 4.0][2]

arXiv:2508.07367v1 [math.NT] 10 Aug 2025

# Almost a Complete Proof of the Generalized Erdős–Straus Conjecture: 5/a = 1/b + 1/c + 1/d

Bilal Ghermoul (1) Address: (1) Department of Mathematics, Faculty of Mathematics and Computer Science,
University Mohamed El Bachir El Ibrahimi of Bordj Bou Arreridj,
El-Anasser 34030, Algeria Email address: [bilal.ghermoul@univ-bba.dz][3]

Date: August 11, 2026

###### Abstract.

The generalized Erdős–Straus conjecture, proposed by Wacław Sierpiński in 1956, asks whether the Diophantine equation

 | 5 a = 1 b + 1 c + 1 d \frac{5}{a}=\frac{1}{b}+\frac{1}{c}+\frac{1}{d} |  |

admits positive integer solutions b, c, d ∈ ℕ b,c,d\in\mathbb{N} for every integer a ≥ 2 a\geq 2. In this work we present explicit solutions for all integers a ≥ 2 a\geq 2. We begin with the simplest known cases where a ≡ i ( mod 5) a\equiv i\pmod{5} for i ∈ { 0, 2, 3, 4 } i\in\{0,2,3,4\}, providing direct decompositions. The remaining open case, a ≡ 1 ( mod 5) a\equiv 1\pmod{5}, is addressed for a = 5 ​ q + 1 a=5q+1 with q ≢ 0 ( mod 252) q\not\equiv 0\pmod{252}, where we give explicit decompositions, often with q q expressed as three-variable polynomials. For q ≡ 0 ( mod 252) q\equiv 0\pmod{252}, we conjecture that a specific polynomial p 1 ​ ( x, y, z) = z ⁡ ( x ⁡ ( 5 ​ y − 1) − y) − x, x, y, z ∈ ℕ ∗ p_{1}(x,y,z)=z(x(5y-1)-y)-x,~x,y,z\in\mathbb{N}^{*}, which exactly satisfies the generalized Erdős–Straus equation, generates all such multiples of 252 252. This conjecture has been verified computationally for 5 ​ q + 1 5q+1 up to approximately 10 10 10^{10}, and the corresponding Mathematica implementation is included.

###### Key words and phrases:

Keywords: Diophantine equation, the generalized Erdős–Straus conjecture.

###### 2020 Mathematics Subject Classification

11Dxx, 11Gxx, 14Gxx

## 1. Introduction

The well-known Erdős–Straus conjecture in number theory, proposed by Paul Erdős and Ernst G. Straus in 1948 [4, 13], asserts that every positive integer greater than or equal to 2 can be represented as the sum of three unit fractions. This conjecture has attracted considerable interest in the mathematical community due to its apparent simplicity and the challenging nature of its proof. Despite its straightforward statement, the conjecture has remained unresolved for many years, capturing the curiosity of mathematicians globally.

Over time, various mathematicians have examined different facets of the Erdős–Straus conjecture, resulting in a substantial body of literature. Notable contributions include works by L. Bernstein [2], Nathanson [15, 16], Konyagin and Shorey [12], Ahlgren, Ono, and Penniston [1], Vaserstein [25], Helfgott and Harcos [10], Karasev [11], Farnsworth [6], Crawford [3], Giovanni, Gallipoli, Gionfriddo [9], Elsholtz and Tao [5], Ghanouchi [7, 8], Mordell [14], Subburam and Togbé [23], Negash [17], Oblàth [18], Rosati [19], Sander [21], Vaughan [26], Yamamoto [27], and many others. The conjecture’s validity for integers up to a ≤ 10 14 a\leq 10^{14} and a ≤ 10 17 a\leq 10^{17} was verified by Swett [24] and Salez [20], respectively.

A generalized version of the Erdős–Straus conjecture states that, for any positive n n, all but finitely many fractions n / a {n}/{a} can be expressed as a sum of three positive unit fractions. The conjecture for fractions 5 / a {5}/{a} was made by Wacław Sierpiński in 1956, and the full conjecture was later attributed to Sierpiński’s student, Andrzej Schinzel [22, 26].

In Unsolved Problems in Number Theory, Guy [28] presents the conjecture as a long-standing open problem, highlighting its enduring importance in the field of number theory.

In this paper, we explore a generalization of the Erdős–Straus conjecture and provide an explicit solution demonstrating its validity for all positive integers a ≥ 2 a\geq 2.

We begin by introducing the Generalized Erdős–Straus Conjecture:

###### Conjecture 1 (Generalized Erdős–Straus Conjecture).

For every integer n ≥ 2 n\geq 2 and every integer r ≥ 2 r\geq 2, the Diophantine equation

(1) |  | r a = 1 b + 1 c + 1 d \frac{r}{a}=\frac{1}{b}+\frac{1}{c}+\frac{1}{d} |  |

has a solution in positive integers b, c, d b,c,d.

The classical Erdős–Straus Conjecture corresponds to the case r = 4 r=4. In the present work, we focus on the case r = 5 r=5 and begin by establishing some simple results for the general case with arbitrary r ≥ 2 r\geq 2.

## 2. Main results

Our main result is summarized in the following.

First, we consider a generatlized Erdős–Straus equation as follows

(2) |  | r q ​ r + t = 1 ( n + q) ​ ( q ​ r + t) + 1 m ⁡ ( q + s) + 1 q + s, \frac{r}{qr+t}=\frac{1}{(n+q)(qr+t)}+\frac{1}{m(q+s)}+\frac{1}{q+s}, |  |

where r, q ≥ 2 r,q\geq 2 and m, q + s, q + n ≥ 1 m,q+s,q+n\geq 1.

###### Lemma 2.1.

The generalized Erdős–Straus Equation ( 2) holds for every q ∈ ℕ ∗ q\in\mathbb{N}^{*} that satisfies one of the following conditions:

- (a)

There exists an integer κ ≥ 1 \kappa\geq 1, such that

(3) |  | ( m + 1) ​ ( q ​ r + t) r ⁡ ( n + q) − 1 = m ⁡ ( q + s) n + q = κ. \frac{(m+1)(qr+t)}{r(n+q)-1}=\frac{m(q+s)}{n+q}=\kappa. |  |

- (b)

There exists an integer κ ≥ 1 \kappa\geq 1 such that

(4) |  | r ​ m | ( 1 + m) ​ ( q ​ r + t) + κ and r ​ κ | ( 1 + m) ​ ( q ​ r + t) + κ. rm\mid(1+m)(qr+t)+\kappa\quad\text{and}\quad r\kappa\mid(1+m)(qr+t)+\kappa. |  |

- (c)

There exist κ, z ≥ 1 \kappa,z\geq 1 such that

(5) |  | q = κ ​ z − s and κ ⁡ ( r ​ z + 1) r ​ s − t = c ∈ ℕ ∗. q=\kappa z-s\quad\text{and}\quad\frac{\kappa(rz+1)}{rs-t}=c\in\mathbb{N}^{*}. |  |

- (d)

There exist κ, z ≥ 1 \kappa,z\geq 1 such that

(6) |  | q = β − s and β ⁡ ( κ + β ​ r) κ ⁡ ( r ​ s − t) = c ∈ ℕ ∗. q=\beta-s\quad\text{and}\quad\frac{\beta(\kappa+\beta r)}{\kappa(rs-t)}=c\in\mathbb{N}^{*}. |  |

###### Proof of Lemma 2.1.

The theorem holds clearly in each of the four cases; we now justify each in turn.

- (a)

The matter is clear; it suffices to take

(7) |  | κ = m ⁡ ( r ​ s − t) − ( q ​ r + t). \kappa=m(rs-t)-(qr+t). |  |

- (b)

For this case, it suffices to consider

(8) |  | n = κ + ( m + 1) ​ ( q ​ r + t) κ ​ r − q and s = κ + ( m + 1) ​ ( q ​ r + t) m ​ r − q. n=\frac{\kappa+(m+1)(qr+t)}{\kappa r}-q\quad\text{and}\quad s=\frac{\kappa+(m+1)(qr+t)}{mr}-q. |  |

Clearly, the values of s s and n n defined by ( 8) satisfy equation ( 2). Therefore, in order for s s and n n to be integers, condition ( 4) must hold.

- (c)

Referring to equations ( 3) and ( 8), we now solve the algebraic system

 | ( m + 1) ( q r + t) = κ ( α r − 1), α κ = β m, β = q + s, and q + s = κ z, (m+1)(qr+t)=\kappa(\alpha r-1),\quad\alpha\kappa=\beta m,\quad\beta=q+s,\quad\text{and}\quad q+s=\kappa z, |  |

to obtain

 | β = κ z, m = κ + κ ​ r ​ z r ​ s − t − 1, α = z ( κ + κ ​ r ​ z r ​ s − t − 1), and q = κ z − s. \beta=\kappa z,\quad m=\frac{\kappa+\kappa rz}{rs-t}-1,\quad\alpha=z\left(\frac{\kappa+\kappa rz}{rs-t}-1\right),\quad\text{and}\quad q=\kappa z-s. |  |

Substituting these expressions into equation ( 2), we obtain

(9) |  | r r ⁡ ( κ ​ z − s) + t = 1 z ⁡ ( κ ⁡ ( r ​ z + 1) r ​ s − t − 1) ​ ( r ⁡ ( κ ​ z − s) + t) + 1 κ ​ z ​ ( κ ⁡ ( r ​ z + 1) r ​ s − t − 1) + 1 κ ​ z. \frac{r}{r(\kappa z-s)+t}=\frac{1}{z\left(\frac{\kappa(rz+1)}{rs-t}-1\right)(r(\kappa z-s)+t)}+\frac{1}{\kappa z\left(\frac{\kappa(rz+1)}{rs-t}-1\right)}+\frac{1}{\kappa z}. |  |

Since this equation is always true, equation ( 2) also holds, provided that the numerators on the right-hand side are integers, which occurs precisely when condition ( 5) is satisfied.

- (d)

Also refering to equations ( 3) and ( 8), we solve the algebraic system

 | ( m + 1) ( q r + t) = κ ( α r − 1), α κ = β m, and β = q + s, (m+1)(qr+t)=\kappa(\alpha r-1),\quad\alpha\kappa=\beta m,\quad\text{and}\quad\beta=q+s, |  |

we obtain

 | α = β ⁡ ( κ + r ⁡ ( β − s) + t) κ ⁡ ( r ​ s − t), m = κ + r ⁡ ( β − s) + t r ​ s − t, and q = β − s. \alpha=\frac{\beta(\kappa+r(\beta-s)+t)}{\kappa(rs-t)},\quad m=\frac{\kappa+r(\beta-s)+t}{rs-t},\quad\text{and}\quad q=\beta-s. |  |

Substituting these expressions into equation ( 2), we obtain

(10) |  | r r ⁡ ( β − s) + t = 1 β + 1 β κ ​ ( κ + β ​ r r ​ s − t − 1) ​ ( r ⁡ ( β − s) + t) + 1 β ⁡ ( κ + β ​ r r ​ s − t − 1). \frac{r}{r(\beta-s)+t}=\frac{1}{\beta}+\frac{1}{\frac{\beta}{\kappa}\left(\frac{\kappa+\beta r}{rs-t}-1\right)(r(\beta-s)+t)}+\frac{1}{\beta\left(\frac{\kappa+\beta r}{rs-t}-1\right)}. |  |

As the equation is identically satisfied, Equation ( 2) holds as well, provided the numerators on the right-hand side are integers. This condition is met exactly when condition ( 6) is satisfied.

This completes the proof. ∎

###### Remark 1.

It is well known that Conjecture 1 remains unsolved for r = 4 r=4 and r = 5 r=5, particularly when a a is a prime of the form 4 ​ q + 1 4q+1 or 5 ​ q + 1 5q+1, respectively. For this reason, our focus will be on proving Equation ( 2) in the cases ( r, t) = ( 4, 1) (r,t)=(4,1) and ( r, t) = ( 5, 1) (r,t)=(5,1).

Since our aim is to prove the generalized Erdős–Straus Conjecture 1 with r = 5 r=5, we focus instead on Equation ( 2) with ( r, t) = ( 5, 1) (r,t)=(5,1). Before proceeding, we address the cases where a ≠ 5 ​ q + 1 a\neq 5q+1; this is the subject of the following lemma.

###### Lemma 2.2.

The generalized Erdős–Straus decomposition ( 1), with r = 4, 5, r=4,5, or 6 have solutions for every a ≠ r ​ k + 1, k ∈ ℕ ∗ a\neq r\,k+1,~~k\in\mathbb{N}^{*}, with min ⁡ { b, c, d } = [a r] + 1 \min\{b,c,d\}=\left[\frac{a}{r}\right]+1, where [a r] \left[\frac{a}{r}\right] is the integer part of a r \frac{a}{r}.

###### Theorem 2.1.

Let a ≥ 2 a\geq 2 be an integer. Then there exist positive integers b, c, d b,c,d such that the generalized Erdős–Straus decomposition

(11) |  | 5 a = 1 b + 1 c + 1 d, \frac{5}{a}=\frac{1}{b}+\frac{1}{c}+\frac{1}{d}, |  |

holds in each of the following cases for q ∈ ℤ > 0 q\in\mathbb{Z}_{>0}:

1. (1)

If a = 5 ​ q + i, a=5q+i, i ∈ { 0, 2, 3, 4 }, i\in\{0,2,3,4\}, then such a decomposition exists.

2. (2)

If a = 5 ​ q + 1 a=5q+1 with q ≢ 0 ( mod 12), q\not\equiv 0\pmod{12}, then such a decomposition exists.

3. (3)

If q = 12 ​ u, u ≥ 1 q=12u,~u\geq 1, for u = 7 ​ v + i, v ≥ 0 u=7v+i,~v\geq 0 and i ∈ { 1, 2, 3, 4, 5, 6 }, i\in\{1,2,3,4,5,6\}, then such a decomposition exists.

4. (4)

If u = 7 ​ v u=7v, then q = 84 ​ v q=84v. In this case, if v = 3 ​ w + i v=3w+i with i ∈ { 1, 2 } i\in\{1,2\}, then such a decomposition exists.

We note that Theorem ( 2.1) does not address the case q ≡ 0 ( mod 252) q\equiv 0\pmod{252}. The following conjecture is intended to cover this remaining case.

###### Conjecture 2.

Let p 1 ​ ( x, y, z) ∈ ℤ ⁡ [x, y, z] p_{1}(x,y,z)\in\mathbb{Z}[x,y,z] be the polynomial ( 16) defined in Section 3 (Proof of Statement (2) of Theorem 2.1). Then, for every positive integer ℓ \ell, there exist x, y, z ∈ ℕ ∗ x,y,z\in\mathbb{N}^{*} such that

 | p 1 ​ ( x, y, z) = 252 ​ ℓ. p_{1}(x,y,z)=252\ell. |  |

Equivalently, 252 ​ ℕ ∗ ⊆ p 1 ​ ( ℕ ∗ 3) 252\mathbb{N}^{*}\subseteq p_{1}(\mathbb{N}^{*3}).

A computational verification of Conjecture 2, up to 5 ​ q + 1 ≈ 2 × 10 10 5q+1\approx 2\times 10^{10} for q ≡ 0 ( mod 252) q\equiv 0\pmod{252}, is provided in Appendix A.

Theorem 2.1 is proved in Section 3.

###### Proof of Lemma 2.2.

We start by solving equation ( 1) with respect to d d to obtain

(12) |  | d = a ​ b ​ c r ​ b ​ c − a ⁡ ( b + c). d=\frac{a\,b\,c}{r\,b\,c-a\,(b+c)}. |  |

Since 1 d = r a − 1 b − 1 c \frac{1}{d}=\frac{r}{a}-\frac{1}{b}-\frac{1}{c} then 1 d < r a \frac{1}{d}<\frac{r}{a} which means that

 | d > a r ⇒ d ≥ [a r] + 1. d>\frac{a}{r}\Rightarrow d\geq\left[\frac{a}{r}\right]+1. |  |

We consider the minimum value for d d, then we obtain the following decompositions for r a \frac{r}{a} regarding r = 4, 5, 6 r=4,5,6.

(1) For r = 4 r=4: Consider a = 4 ​ k + i, k ∈ ℕ ∗ a=4\,k+i,~~k\in\mathbb{N}^{*} and i = 0, 2, 3 i=0,2,3. Then we have the following:

(1.1) If a = 4 ​ k, k ∈ ℕ ∗ a=4\,k,~~k\in\mathbb{N}^{*}, we get the decomposition

 | 4 4 ​ k = 1 k = 1 ( k + 1) 2 + 1 k ​ ( k + 1) 2 + 1 k + 1. \frac{4}{4\,k}=\frac{1}{k}=\frac{1}{(k+1)^{2}}+\frac{1}{k\,(k+1)^{2}}+\frac{1}{k+1}. |  |

(1.2) If a = 4 ​ k + 2, k ∈ ℕ ∗ a=4\,k+2,~~k\in\mathbb{N}^{*}, we get the decomposition

 | 4 4 ​ k + 2 = 1 2 ​ ( k + 1) 2 + 1 2 ​ ( k + 1) 2 ​ ( 2 ​ k + 1) + 1 k + 1. \frac{4}{4\,k+2}=\frac{1}{2\,(k+1)^{2}}+\frac{1}{2\,(k+1)^{2}(2\,k+1)}+\frac{1}{k+1}. |  |

(1.3) If a = 4 ​ k + 3, k ∈ ℕ ∗ a=4\,k+3,~~k\in\mathbb{N}^{*}, we get the decomposition

 | 4 4 ​ k + 3 = 1 4 ​ ( k + 1) 2 + 1 4 ​ ( k + 1) 2 ​ ( 4 ​ k + 3) + 1 k + 1. \frac{4}{4\,k+3}=\frac{1}{4\,(k+1)^{2}}+\frac{1}{4\,(k+1)^{2}(4\,k+3)}+\frac{1}{k+1}. |  |

(2) For r = 5 r=5: Consider a = 5 ​ k + i, k ∈ ℕ ∗ a=5\,k+i,~~k\in\mathbb{N}^{*} and i = 0, 2, 3, 4 i=0,2,3,4. Then we have the following:

(2.1) If a = 5 ​ k, k ∈ ℕ ∗ a=5\,k,~~k\in\mathbb{N}^{*}, we get the decomposition

 | 5 5 ​ k = 1 k = 1 ( k + 1) 2 + 1 k ​ ( k + 1) 2 + 1 k + 1. \frac{5}{5\,k}=\frac{1}{k}=\frac{1}{(k+1)^{2}}+\frac{1}{k\,(k+1)^{2}}+\frac{1}{k+1}. |  |

(2.2) If a = 5 ​ k + 2, k ∈ ℕ ∗ a=5\,k+2,~~k\in\mathbb{N}^{*}, we get the decomposition

 | 5 5 ​ k + 2 = { 1 10 ​ q 2 + 7 ​ q + 1 + 1 20 ​ q 2 + 14 ​ q + 2 + 1 2 ​ q + 1, if ​ k = 2 ​ q, 1 10 ​ q 2 + 17 ​ q + 7 + 1 20 ​ q 2 + 34 ​ q + 14 + 1 2 ​ q + 2, if ​ k = 2 ​ q + 1. \frac{5}{5\,k+2}=\begin{cases}\dfrac{1}{10\,q^{2}+7\,q+1}+\dfrac{1}{20\,q^{2}+14\,q+2}+\dfrac{1}{2\,q+1},&\text{if }k=2\,q,\\ \dfrac{1}{10\,q^{2}+17\,q+7}+\dfrac{1}{20\,q^{2}+34\,q+14}+\dfrac{1}{2\,q+2},&\text{if }k=2\,q+1.\end{cases} |  |

(2.3) If a = 5 ​ k + 3, k ∈ ℕ ∗ a=5\,k+3,~~k\in\mathbb{N}^{*}, we get the decomposition

 | 5 5 ​ k + 3 = 1 5 ​ k 2 + 8 ​ k + 3 + 1 5 ​ k 2 + 8 ​ k + 3 + 1 k + 1. \frac{5}{5\,k+3}=\frac{1}{5\,k^{2}+8\,k+3}+\frac{1}{5\,k^{2}+8\,k+3}+\frac{1}{k+1}. |  |

(2.4) If a = 5 ​ k + 4, k ∈ ℕ ∗ a=5\,k+4,~~k\in\mathbb{N}^{*}, we get the decomposition

 | 5 5 ​ k + 4 = 1 5 ​ ( k + 1) 2 ​ ( 5 ​ k + 4) + 1 5 ​ ( k + 1) 2 + 1 k + 1. \frac{5}{5\,k+4}=\frac{1}{5\,(k+1)^{2}(5\,k+4)}+\frac{1}{5\,(k+1)^{2}}+\frac{1}{k+1}. |  |

(3) For r = 6 r=6: Consider a = 6 ​ k + i, k ∈ ℕ ∗ a=6\,k+i,~~k\in\mathbb{N}^{*} and i = 0, 2, 3, 4, 5 i=0,2,3,4,5. Then we have the following:

(3.1) If a = 6 ​ k, k ∈ ℕ ∗ a=6\,k,~~k\in\mathbb{N}^{*}, we get the decomposition 6 6 ​ k = 1 k \tfrac{6}{6\,k}=\tfrac{1}{k}.

(3.2) If a = 6 ​ k + 2, k ∈ ℕ ∗ a=6\,k+2,~~k\in\mathbb{N}^{*}, we get the decomposition

 | 6 6 ​ k + 2 \displaystyle\frac{6}{6\,k+2} | = \displaystyle= | 1 3 ​ k 2 + 4 ​ k + 1 + 1 3 ​ k 2 + 4 ​ k + 1 + 1 k + 1. \displaystyle\frac{1}{3\,k^{2}+4\,k+1}+\frac{1}{3\,k^{2}+4\,k+1}+\frac{1}{k+1}. |  |

(3.3) If a = 6 ​ k + 3, k ∈ ℕ ∗ a=6\,k+3,~~k\in\mathbb{N}^{*}, we get the decomposition

 | 6 6 ​ k + 3 = 1 2 ​ ( k + 1) 2 + 1 2 ​ ( k + 1) 2 ​ ( 2 ​ k + 1) + 1 k + 1. \frac{6}{6\,k+3}=\frac{1}{2\,(k+1)^{2}}+\frac{1}{2\,(k+1)^{2}(2\,k+1)}+\frac{1}{k+1}. |  |

(3.4) If a = 6 ​ k + 4, k ∈ ℕ ∗ a=6\,k+4,~~k\in\mathbb{N}^{*}, we get the decomposition

 | 6 6 ​ k + 4 = 1 3 ​ ( k + 1) 2 + 1 3 ​ ( k + 1) 2 ​ ( 3 ​ k + 2) + 1 k + 1. \frac{6}{6\,k+4}=\frac{1}{3\,(k+1)^{2}}+\frac{1}{3\,(k+1)^{2}(3\,k+2)}+\frac{1}{k+1}. |  |

(3.5) If a = 6 ​ k + 5, k ∈ ℕ ∗ a=6\,k+5,~~k\in\mathbb{N}^{*}, we get the decomposition

 | 6 6 ​ k + 5 = 1 6 ​ ( k + 1) 2 + 1 6 ​ ( k + 1) 2 ​ ( 6 ​ k + 5) + 1 k + 1. \frac{6}{6\,k+5}=\frac{1}{6\,(k+1)^{2}}+\frac{1}{6\,(k+1)^{2}(6\,k+5)}+\frac{1}{k+1}. |  |

This completes the proof. ∎

Now, let us return to the proof of Theorem 2.1.

## 3. Proof of Theorem Theorem 2.1

###### Proof of Statement (1) of Theorem 2.1.

The proof of Theorem 2.1 follows directly in the case a ≠ 5 ​ q + 1 a\neq 5q+1, with q ∈ ℕ q\in\mathbb{N}, by invoking Lemma 2.2. ∎

###### Proof of Statement (2) of Theorem 2.1.

Now, we consider the case where a = 5 ​ q + 1 a=5q+1, with q ∈ ℕ q\in\mathbb{N}.

First, observe that any natural number q q can be written as

(13) |  | q = z ​ κ − s, q=z\kappa-s, |  |

for any z, κ, s ∈ ℕ ∗ z,\kappa,s\in\mathbb{N}^{*}, that is due to arbitrariness of these integers. In addition, the generalized decomposition defined by Equation ( 9), when setting ( r, t) = ( 5, 1) (r,t)=(5,1), becomes:

(14) |  | 5 5 ​ ( κ ​ z − s) + 1 = 1 κ ​ z ​ ( κ ⁡ ( 5 ​ z + 1) 5 ​ s − 1 − 1) + 1 z ⁡ ( κ ⁡ ( 5 ​ z + 1) 5 ​ s − 1 − 1) ​ ( 5 ​ ( κ ​ z − s) + 1) + 1 κ ​ z. \frac{5}{5(\kappa z-s)+1}=\frac{1}{\kappa z\left(\frac{\kappa(5z+1)}{5s-1}-1\right)}+\frac{1}{z\left(\frac{\kappa(5z+1)}{5s-1}-1\right)(5(\kappa z-s)+1)}+\frac{1}{\kappa z}. |  |

This identity holds for every q q of the form ( 13). Then, for q q to satisfy the decomposition ( 11), it must meet one of the following conditions in full.

Condition 01: This is the case when

(15) |  | 5 ​ z + 1 5 ​ s − 1 = c ∈ ℕ ∗ ​ and ​ κ ​ z − s = q. \frac{5z+1}{5s-1}=c\in\mathbb{N}^{*}\text{ and }\kappa z-s=q. |  |

This means that there exists γ ∈ ℕ ∗ \gamma\in\mathbb{N}^{*} such that

 | z = ( 5 ​ γ − 1) ​ s − γ, z=(5\gamma-1)s-\gamma, |  |

and therefore

 | q = κ ⁡ ( ( 5 ​ γ − 1) ​ s − γ) − s. q=\kappa\big((5\gamma-1)s-\gamma\big)-s. |  |

Replacing ( s, γ, κ) → ( x, y, z) (s,\gamma,\kappa)\to(x,y,z), the expression for q q becomes of the form:

(16) |  | p 1 ​ ( x, y, z) = z ⁡ ( x ⁡ ( 5 ​ y − 1) − y) − x, x, y, z ∈ ℕ ∗. \boxed{p_{1}(x,y,z)=z(x(5y-1)-y)-x,\quad x,y,z\in\mathbb{N}^{*}.} |  |

Here, p 1 ∈ ℤ ⁡ [x, y, z] p_{1}\in\mathbb{Z}[x,y,z] is a polynomial in three variables with integer coefficients; that is, ℤ ⁡ [x, y, z] \mathbb{Z}[x,y,z] denotes the ring of polynomials in x, y, z x,y,z over the integers.

Thus, equations ( 11) is indeed satisfied for a = 5 ​ q + 1 a=5q+1, when q = p 1 ​ ( x, y, z) q=p_{1}(x,y,z), and from Equation ( 14) we obtain:

(17) |  | 5 5 ​ p 1 ​ ( x, y, z) + 1 \displaystyle\frac{5}{5p_{1}(x,y,z)+1} | = 5 5 ​ ( z ⁡ ( x ⁡ ( 5 ​ y − 1) − y) − x) + 1 \displaystyle=\frac{5}{5(z(x(5y-1)-y)-x)+1} |  |

 |  | = 1 ( x ⁡ ( 5 ​ y − 1) − y) ​ ( ( 5 ​ y − 1) ​ z − 1) ​ ( 5 ​ x ​ ( ( 5 ​ y − 1) ​ z − 1) − 5 ​ y ​ z + 1) \displaystyle=\frac{1}{(x(5y-1)-y)((5y-1)z-1)(5x((5y-1)z-1)-5yz+1)} |  |

 |  | + 1 z ⁡ ( x ⁡ ( 5 ​ y − 1) − y) ​ ( ( 5 ​ y − 1) ​ z − 1) + 1 z ⁡ ( x ⁡ ( 5 ​ y − 1) − y). \displaystyle+\frac{1}{z(x(5y-1)-y)((5y-1)z-1)}+\frac{1}{z(x(5y-1)-y)}. |  |

C.1.1. Polynomial p 1 p_{1} generate the congruence q ≡ 2 ( mod 12) ¯, \underline{q\equiv 2\pmod{12}}, with x = 1, x=1, y = 1 y=1, and z = 1 + 4 ​ x z=1+4x, x ≥ 0 x\geq 0, which gives

(18) |  | 5 1 + 5 ​ ( 2 + 12 ​ x) ¯ = 1 3 ​ ( 1 + 4 ​ x) ​ ( 3 + 16 ​ x) + 1 3 ​ ( 3 + 16 ​ x) ​ ( 11 + 60 ​ x) + 1 3 ​ ( 1 + 4 ​ x). \frac{5}{1+5\underline{(2+12x)}}=\frac{1}{3(1+4x)(3+16x)}+\frac{1}{3(3+16x)(11+60x)}+\frac{1}{3(1+4x)}. |  |

C.1.2. Also, polynomial p 1 p_{1} generate the congruence q ≡ 5 ( mod 12) ¯, \underline{q\equiv 5\pmod{12}}, with x = 1, x=1, y = 1 y=1, and z = 2 + 4 ​ x z=2+4x, x ≥ 0 x\geq 0. Then we obtain

(19) |  | 5 1 + 5 ​ ( 5 + 12 ​ x) ¯ = 1 6 ​ ( 1 + 2 ​ x) ​ ( 7 + 16 ​ x) + 1 6 ​ ( 7 + 16 ​ x) ​ ( 13 + 30 ​ x) + 1 3 ​ ( 2 + 4 ​ x). \frac{5}{1+5\underline{(5+12x)}}=\frac{1}{6(1+2x)(7+16x)}+\frac{1}{6(7+16x)(13+30x)}+\frac{1}{3(2+4x)}. |  |

C.1.3. p 1 p_{1} also generate the congruence q ≡ 8 ( mod 12) ¯, \underline{q\equiv 8\pmod{12}}, with x = 1, x=1, y = 1 y=1, and z = 3 + 4 ​ x z=3+4x, x ≥ 0 x\geq 0. Then we obtain

(20) |  | 5 1 + 5 ​ ( 8 + 12 ​ x) ¯ = 1 3 ​ ( 3 + 4 ​ x) ​ ( 11 + 16 ​ x) + 1 3 ​ ( 11 + 16 ​ x) ​ ( 41 + 60 ​ x) + 1 3 ​ ( 3 + 4 ​ x). \frac{5}{1+5\underline{(8+12x)}}=\frac{1}{3(3+4x)(11+16x)}+\frac{1}{3(11+16x)(41+60x)}+\frac{1}{3(3+4x)}. |  |

C.1.4. p 1 p_{1} also generate the congruence q ≡ 6 ( mod 12) ¯, \underline{q\equiv 6\pmod{12}}, with x = 1, x=1, y = 2 + 3 ​ x y=2+3x, and z = 1 z=1, x ≥ 0 x\geq 0. We obtain

(21) |  | 5 1 + 5 ​ ( 6 + 12 ​ x) ¯ = 1 ( 7 + 12 ​ x) ​ ( 8 + 15 ​ x) + 1 ( 7 + 12 ​ x) ​ ( 8 + 15 ​ x) ​ ( 31 + 60 ​ x) + 1 7 + 12 ​ x. \frac{5}{1+5\underline{(6+12x)}}=\frac{1}{(7+12x)(8+15x)}+\frac{1}{(7+12x)(8+15x)(31+60x)}+\frac{1}{7+12x}. |  |

C.1.5. p 1 p_{1} also generate the congruence q ≡ 10 ( mod 12) ¯, \underline{q\equiv 10\pmod{12}}, with x = 1, x=1, y = 3 + 3 ​ x y=3+3x, and z = 1 z=1, x ≥ 0 x\geq 0. We obtain

(22) |  | 5 1 + 5 ​ ( 10 + 12 ​ x) ¯ = 1 ( 11 + 12 ​ x) ​ ( 13 + 15 ​ x) + 1 3 ​ ( 11 + 12 ​ x) ​ ( 13 + 15 ​ x) ​ ( 17 + 20 ​ x) + 1 11 + 12 ​ x. \frac{5}{1+5\underline{(10+12x)}}=\frac{1}{(11+12x)(13+15x)}+\frac{1}{3(11+12x)(13+15x)(17+20x)}+\frac{1}{11+12x}. |  |

Condition 02: This is the case when

(23) |  | κ ⁡ ( 5 ​ z + 1) 5 ​ s − 1 = c ∈ ℕ ∗ ​ and ​ κ ​ z − s = q. \frac{\kappa(5z+1)}{5s-1}=c\in\mathbb{N}^{*}\text{ and }\kappa z-s=q. |  |

First, we consider c = 2 c=2, in this case ( 23) is fulfilled by considering the following parameters:

 | q = ( 1 + 3 c 2) + ( 2 + 5 c 2) c 1, s = ( 2 + 3 c 2) + ( 3 + 5 c 2) c 1, z = 1 + 2 c 2, and κ = 3 + 5 c 1, q=(1+3c_{2})+(2+5c_{2})c_{1},\quad s=(2+3c_{2})+(3+5c_{2})c_{1},\quad z=1+2c_{2},\quad\text{and}\quad\kappa=3+5c_{1}, |  |

with c 1, c 2 ≥ 0 c_{1},c_{2}\geq 0, relpacing ( c 1, c 2) → ( x − 1, y − 1) (c_{1},c_{2})\to(x-1,y-1) and therefore an expression for q q becomes of the form:

(24) |  | p 2 ​ ( x, y) = x ⁡ ( 5 ​ y − 3) − 2 ​ y + 1, x, y, z ∈ ℕ ∗. \boxed{p_{2}(x,y)=x(5y-3)-2y+1,\quad x,y,z\in\mathbb{N}^{*}.} |  |

Here, p 2 ∈ ℤ ⁡ [x, y] p_{2}\in\mathbb{Z}[x,y] is a polynomial in three variables with integer coefficients; that is, ℤ ⁡ [x, y] \mathbb{Z}[x,y] denotes the ring of polynomials in x, y, z x,y,z over the integers.

Thus, equations ( 11) is indeed satisfied for a = 5 ​ q + 1 a=5q+1, with q = p 2 ​ ( x, y) q=p_{2}(x,y), and from Equation ( 14) we obtain:

(25) |  | 5 5 ​ p 2 ​ ( x, y) + 1 \displaystyle\frac{5}{5p_{2}(x,y)+1} | = 5 ( 5 ​ x − 2) ​ ( 5 ​ y − 3) \displaystyle=\frac{5}{(5x-2)(5y-3)} |  |

 |  | = 1 ( 5 ​ x − 2) ​ ( 10 ​ y 2 − 11 ​ y + 3) + 1 10 ​ x ​ y − 5 ​ x − 4 ​ y + 2 + 1 10 ​ x ​ y − 5 ​ x − 4 ​ y + 2. \displaystyle=\frac{1}{(5x-2)\left(10y^{2}-11y+3\right)}+\frac{1}{10xy-5x-4y+2}+\frac{1}{10xy-5x-4y+2}. |  |

Secondly, we consider c = 3 c=3, in this case ( 23) is fullfilled by consideriong following parameters:

 | q = ( 1 + 4 c 2) + ( 3 + 10 c 2) c 1, s = ( 1 + 2 c 2) + ( 2 + 5 c 2) c 1, z = 1 + 3 c 2, and κ = 2 + 5 c 1, q=(1+4c_{2})+(3+10c_{2})c_{1},\quad s=(1+2c_{2})+(2+5c_{2})c_{1},\quad z=1+3c_{2},\quad\text{and}\quad\kappa=2+5c_{1}, |  |

with c 1, c 2 ≥ 0 c_{1},c_{2}\geq 0, relpacing ( c 1, c 2) → ( x − 1, y − 1) (c_{1},c_{2})\to(x-1,y-1) and therefore an expression for q q becomes of the form:

(26) |  | p 3 ​ ( x, y) = x ⁡ ( 10 ​ y − 7) − 6 ​ y + 4, x, y, z ∈ ℕ ∗. \boxed{p_{3}(x,y)=x(10y-7)-6y+4,\quad x,y,z\in\mathbb{N}^{*}.} |  |

Here, p 3 ∈ ℤ ⁡ [x, y] p_{3}\in\mathbb{Z}[x,y] is a polynomial in three variables with integer coefficients; that is, ℤ ⁡ [x, y] \mathbb{Z}[x,y] denotes the ring of polynomials in x, y, z x,y,z over the integers.

Thus, equations ( 11) is indeed satisfied for a = 5 ​ q + 1 a=5q+1, with q = p 3 ​ ( x, y) q=p_{3}(x,y), and from Equation ( 14) we obtain:

(27) |  | 5 5 ​ p 3 ​ ( x, y) + 1 \displaystyle\frac{5}{5p_{3}(x,y)+1} | = 5 ( 5 ​ x − 3) ​ ( 10 ​ y − 7) \displaystyle=\frac{5}{(5x-3)(10y-7)} |  |

 |  | = 1 2 ​ ( 5 ​ x − 3) ​ ( 30 ​ y 2 − 41 ​ y + 14) + 1 30 ​ x ​ y − 20 ​ x − 18 ​ y + 12 + 1 15 ​ x ​ y − 10 ​ x − 9 ​ y + 6. \displaystyle=\frac{1}{2(5x-3)\left(30y^{2}-41y+14\right)}+\frac{1}{30xy-20x-18y+12}+\frac{1}{15xy-10x-9y+6}. |  |

C.2.1. Condition ( 23) generate the q ≡ 1 ( mod 12) ¯ \underline{q\equiv 1\pmod{12}}, as follows

(28) |  | 5 1 + 5 ​ ( 1 + 12 ​ x) ¯ = 1 6 + 60 ​ x + 1 3 + 30 ​ x + 1 3 + 30 ​ x. \frac{5}{1+5\underline{(1+12x)}}=\frac{1}{6+60x}+\frac{1}{3+30x}+\frac{1}{3+30x}. |  |

with c = 2, c=2, s = 2 + 18 ​ x s=2+18x, z = 1 z=1, and κ = 3 + 30 ​ x \kappa=3+30x, x ≥ 0 x\geq 0.

C.2.2. And ( 23) generate the q ≡ 9 ( mod 12) ¯ \underline{q\equiv 9\pmod{12}}, as follows

(29) |  | 5 1 + 5 ​ ( 9 + 12 ​ x) ¯ = 1 46 + 60 ​ x + 1 23 + 30 ​ x + 1 23 + 30 ​ x, \frac{5}{1+5\underline{(9+12x)}}=\frac{1}{46+60x}+\frac{1}{23+30x}+\frac{1}{23+30x}, |  |

with c = 2, c=2, s = 2 ​ ( 7 + 9 ​ x) s=2(7+9x), z = 1 z=1, and κ = 23 + 30 ​ x \kappa=23+30x, x ≥ 0 x\geq 0.

C.2.3. And ( 23) generate the q ≡ 3 ( mod 12) ¯ \underline{q\equiv 3\pmod{12}}, as follows

(30) |  | 5 1 + 5 ​ ( 3 + 12 ​ x) ¯ = 1 16 + 60 ​ x + 1 8 + 30 ​ x + 1 8 + 30 ​ x, \frac{5}{1+5\underline{(3+12x)}}=\frac{1}{16+60x}+\frac{1}{8+30x}+\frac{1}{8+30x}, |  |

with c = 2, c=2, s = 5 + 18 ​ x s=5+18x, z = 1 z=1, and κ = 8 + 30 ​ x \kappa=8+30x, x ≥ 0 x\geq 0.

C.2.4. And ( 23) generate the q ≡ 11 ( mod 12) ¯ \underline{q\equiv 11\pmod{12}}, as follows

(31) |  | 5 1 + 5 ​ ( 11 + 12 ​ x) ¯ = 1 56 + 60 ​ x + 1 28 + 30 ​ x + 1 28 + 30 ​ x, \frac{5}{1+5\underline{(11+12x)}}=\frac{1}{56+60x}+\frac{1}{28+30x}+\frac{1}{28+30x}, |  |

with c = 2, c=2, s = 5 + 6 ​ x s=5+6x, z = 1 z=1, and κ = 8 + 10 ​ x \kappa=8+10x, x ≥ 0 x\geq 0.

C.2.5. And ( 23) generate the q ≡ 4 ( mod 12) ¯ \underline{q\equiv 4\pmod{12}}, as follows

(32) |  | 5 1 + 5 ​ ( 4 + 12 ​ x) ¯ = 1 6 ​ ( 7 + 20 ​ x) + 1 14 + 40 ​ x + 1 7 + 20 ​ x, \frac{5}{1+5\underline{(4+12x)}}=\frac{1}{6(7+20x)}+\frac{1}{14+40x}+\frac{1}{7+20x}, |  |

with c = 3, c=3, s = 3 + 8 ​ x s=3+8x, z = 1 z=1, and κ = 7 + 20 ​ x \kappa=7+20x, x ≥ 0 x\geq 0.

C.2.6. And ( 23) generate the q ≡ 7 ( mod 12) ¯ \underline{q\equiv 7\pmod{12}}, as follows

(33) |  | 5 1 + 5 ​ ( 7 + 12 ​ x) ¯ = 1 8 ​ ( 3 + 5 ​ x) + 1 24 ​ ( 3 + 5 ​ x) + 1 4 ​ ( 3 + 5 ​ x), \frac{5}{1+5\underline{(7+12x)}}=\frac{1}{8(3+5x)}+\frac{1}{24(3+5x)}+\frac{1}{4(3+5x)}, |  |

with c = 3, c=3, s = 5 + 8 ​ x s=5+8x, z = 1 z=1, and κ = 4 ​ ( 3 + 5 ​ x) \kappa=4(3+5x), x ≥ 0 x\geq 0.

This completes the proof of Statement (2) of Theorem 2.1. ∎

Based on the preceding proof, we state the following remark:

###### Remark 2.

All cases C.1.1–C.1.5 can be reduced to only two representative cases:

∙ \bullet In the first case, we substitute p 1 ​ ( 1, 1, z) p_{1}(1,1,z) into ( 17) to obtain

 | 5 5 ​ ( 3 ​ z − 1) + 1 = 1 3 ​ z ​ ( 4 ​ z − 1) + 1 3 ​ ( 4 ​ z − 1) ​ ( 15 ​ z − 4) + 1 3 ​ z, \frac{5}{5(3z-1)+1}=\frac{1}{3z(4z-1)}+\frac{1}{3(4z-1)(15z-4)}+\frac{1}{3z}, |  |

Alternatively, by setting s = 1 s=1, c = 4 c=4, κ = x + 1 \kappa=x+1, and z = 3 z=3, we get q = 3 ​ x + 2 q=3x+2 (from ( 15)) in ( 14), which leads to a similar result.

∙ \bullet In the second case, we substitute p 1 ​ ( 1, y, 1) p_{1}(1,y,1) into ( 17) to obtain

 | 5 5 ​ ( 4 ​ y − 2) + 1 = 1 ( 4 ​ y − 1) ​ ( 5 ​ y − 2) + 1 ( 4 ​ y − 1) ​ ( 5 ​ y − 2) ​ ( 20 ​ y − 9) + 1 4 ​ y − 1. \frac{5}{5(4y-2)+1}=\frac{1}{(4y-1)(5y-2)}+\frac{1}{(4y-1)(5y-2)(20y-9)}+\frac{1}{4y-1}. |  |

Alternatively, by setting s = 1 s=1, c = 5 ​ x + 4 c=5x+4, κ = 1 \kappa=1, and z = 4 ​ x + 3 z=4x+3, we get q = 4 ​ x + 2 q=4x+2 (from ( 15)) in ( 14), again yielding a similar result.

In a similar manner, all cases C.2.1–C.2.6 can be reduced to only two representative cases:

∙ \bullet In the first case, we set c = 2 c=2, s = 3 ​ x + 2 s=3x+2, κ = 5 ​ x + 3 \kappa=5x+3, and z = 1 z=1. From ( 23), we obtain q = 2 ​ x + 1 q=2x+1. Substituting into ( 17), we get

 | 5 5 ​ ( 2 ​ x + 1) + 1 = 1 10 ​ x + 6 + 1 5 ​ x + 3 + 1 5 ​ x + 3. \frac{5}{5(2x+1)+1}=\frac{1}{10x+6}+\frac{1}{5x+3}+\frac{1}{5x+3}. |  |

As another approach, setting p 2 ​ ( x, 1) = 2 ​ x − 1 p_{2}(x,1)=2x-1 results in a similar expression.

∙ \bullet In the second case, we set c = 3 c=3, s = 2 ​ x + 1 s=2x+1, κ = 5 ​ x + 3 \kappa=5x+3, and z = 1 z=1. From ( 23), we obtain q = 3 ​ x + 1 q=3x+1. Substituting into ( 17), we get

 | 5 5 ​ ( 3 ​ x + 1) + 1 = 1 6 ​ ( 5 ​ x + 2) + 1 10 ​ x + 4 + 1 5 ​ x + 2. \frac{5}{5(3x+1)+1}=\frac{1}{6(5x+2)}+\frac{1}{10x+4}+\frac{1}{5x+2}. |  |

Similarly, taking p 3 ​ ( x, 1) = 3 ​ x − 1 p_{3}(x,1)=3x-1 gives a parallel result.

###### Corollary 3.1.

Any prime p p of the form 5 ​ q + 1 5q+1, with q ≢ 0 ( mod 12) q\not\equiv 0\pmod{12}, must be expressible using the polynomial p 3 p_{3} as follows:

 | p = 5 ​ p 3 ​ ( x, y, z) + 1 = 5 ​ ( z ⁡ ( x ⁡ ( 5 ​ y − 1) − y) − x) + 1. p=5\,p_{3}(x,y,z)+1=5(z(x(5y-1)-y)-x)+1. |  |

###### Proof of Corollary 3.1.

This follows from the proof of Statement (2) of Theorem 2.1. ∎

###### Proof of Statement (3) of Theorem 3.1.

The proof is carried out for each modulo case separately, as follows:

For u ≡ 1 ( mod 7) ¯ \underline{u\equiv 1\pmod{7}}: In this case, we replace parameters s = 2, s=2, z = 7, z=7, and κ = 2 + 12 ​ x \kappa=2+12x with x ≥ 0 x\geq 0 into Equation ( 14), we obtain

(34) |  | 5 5 ​ [12 ​ ( 7 ​ x + 1) ¯] + 1 = 1 84 ​ x + 14 + 1 7 ​ ( 48 ​ x + 7) ​ ( 420 ​ x + 61) + 1 14 ​ ( 6 ​ x + 1) ​ ( 48 ​ x + 7). \frac{5}{5[12\underline{(7x+1)}]+1}=\frac{1}{84x+14}+\frac{1}{7(48x+7)(420x+61)}+\frac{1}{14(6x+1)(48x+7)}. |  |

We can also set x → 2, x\to 2, y → 1, y\to 1, and z → 2 + 12 ​ x z\to 2+12x into Polynomial ( 16) to obtain the same decomposition.

The analysis of this case, and of all cases that follow, is based on Lemma 2.1 together with its proof, including Equations ( 9)–( 10).

For u ≡ 2 ( mod 7) ¯ \underline{u\equiv 2\pmod{7}}: In this case, we consider

 | q = p 4 ​ ( x, y) = − 97 + 121 ​ y + 84 ​ x ​ ( − 4 + 5 ​ y), x, y ∈ ℕ ∗. q=p_{4}(x,y)=-97+121y+84x(-4+5y),\quad x,y\in\mathbb{N}^{*}. |  |

Then

 | 5 5 ​ p 4 ​ ( x, y) + 1 = 5 ( 420 ​ x + 121) ​ ( 5 ​ y − 4) \displaystyle\frac{5}{5p_{4}(x,y)+1}=\frac{5}{(420x+121)(5y-4)} | = 1 2 ​ ( 3 ​ x + 1) ​ ( 420 ​ x + 121) ​ ( 5 ​ y − 4) \displaystyle=\frac{1}{2(3x+1)(420x+121)(5y-4)} |  |

 |  | + 1 6 ​ ( 3 ​ x + 1) ​ ( 28 ​ x + 9) ​ ( 420 ​ x + 121) ​ ( 5 ​ y − 4) \displaystyle+\frac{1}{6(3x+1)(28x+9)(420x+121)(5y-4)} |  |

 |  | + 1 3 ​ ( 28 ​ x + 9) ​ ( 5 ​ y − 4). \displaystyle+\frac{1}{3(28x+9)(5y-4)}. |  |

We consider y = 1 y=1, then we obtain

(35) |  | 5 5 ​ [12 ​ ( 7 ​ x + 2) ¯] + 1 = 1 84 ​ x + 14 + 1 7 ​ ( 48 ​ x + 7) ​ ( 420 ​ x + 61) + 1 14 ​ ( 6 ​ x + 1) ​ ( 48 ​ x + 7). \frac{5}{5[12\underline{(7x+2)}]+1}=\frac{1}{84x+14}+\frac{1}{7(48x+7)(420x+61)}+\frac{1}{14(6x+1)(48x+7)}. |  |

For u ≡ 3 ( mod 7) ¯ \underline{u\equiv 3\pmod{7}}: In this case, we have the following:

(36) |  | 5 5 ​ [12 ​ ( 7 ​ x + 3) ¯] + 1 \displaystyle\frac{5}{5[12\underline{(7x+3)}]+1} | = 1 84 ​ x + 39 + 1 3 ​ ( 28 ​ x + 13) ​ ( 30 ​ x + 13) ​ ( 420 ​ x + 181) \displaystyle=\frac{1}{84x+39}+\frac{1}{3(28x+13)(30x+13)(420x+181)} |  |

 |  | + 1 3 ​ ( 28 ​ x + 13) ​ ( 30 ​ x + 13). \displaystyle+\frac{1}{3(28x+13)(30x+13)}. |  |

For u ≡ 4 ( mod 7) ¯ \underline{u\equiv 4\pmod{7}}: In this case, we get

(37) |  | 5 5 ​ [12 ​ ( 7 ​ x + 4) ¯] + 1 \displaystyle\frac{5}{5[12\underline{(7x+4)}]+1} | = 1 8820 ​ x 2 + 10353 ​ x + 3038 + 1 ( 12 ​ x + 7) ​ ( 105 ​ x + 62) ​ ( 420 ​ x + 241) \displaystyle=\frac{1}{8820x^{2}+10353x+3038}+\frac{1}{(12x+7)(105x+62)(420x+241)} |  |

 |  | + 1 84 ​ x + 49. \displaystyle+\frac{1}{84x+49}. |  |

For u ≡ 5 ( mod 7) ¯ \underline{u\equiv 5\pmod{7}}: In this case, we get

(38) |  | 5 5 ​ [12 ​ ( 7 ​ x + 5) ¯] + 1 \displaystyle\frac{5}{5[12\underline{(7x+5)}]+1} | = 1 2520 ​ x 2 + 3714 ​ x + 1368 + 1 14 ​ ( 4 ​ x + 3) ​ ( 60 ​ x + 43) ​ ( 105 ​ x + 76) \displaystyle=\frac{1}{2520x^{2}+3714x+1368}+\frac{1}{14(4x+3)(60x+43)(105x+76)} |  |

 |  | + 1 84 ​ x + 63. \displaystyle+\frac{1}{84x+63}. |  |

For u ≡ 6 ( mod 7) ¯ \underline{u\equiv 6\pmod{7}}: In this case, we get

(39) |  | 5 5 ​ [12 ​ ( 7 ​ x + 6) ¯] + 1 \displaystyle\frac{5}{5[12\underline{(7x+6)}]+1} | = 1 2520 ​ x 2 + 4434 ​ x + 1950 + 1 2 ​ ( 15 ​ x + 13) ​ ( 28 ​ x + 25) ​ ( 420 ​ x + 361) \displaystyle=\frac{1}{2520x^{2}+4434x+1950}+\frac{1}{2(15x+13)(28x+25)(420x+361)} |  |

 |  | + 1 84 ​ x + 75. \displaystyle+\frac{1}{84x+75}. |  |

This concludes the proof of Statement (3) of Theorem 2.1. ∎

###### Proof of Statement (4) of Theorem 2.1.

Two cases must be discussed separately:

For v ≡ 1 ( mod 3) ¯ \underline{v\equiv 1\pmod{3}}: In this case, we consider

 | q = p 5 ​ ( x, y) = 252 ​ x ​ ( 5 ​ y − 4) + 421 ​ y − 337, x, y ∈ ℕ ∗. q=p_{5}(x,y)=252x(5y-4)+421y-337,\quad x,y\in\mathbb{N}^{*}. |  |

Then

 | 5 5 ​ p 5 ​ ( x, y) + 1 = 5 ( 1260 ​ x + 421) ​ ( 5 ​ y − 4) \displaystyle\frac{5}{5p_{5}(x,y)+1}=\frac{5}{(1260x+421)(5y-4)} | = 1 ( 126 ​ x + 43) ​ ( 140 ​ x + 47) ​ ( 1260 ​ x + 421) ​ ( 5 ​ y − 4) \displaystyle=\frac{1}{(126x+43)(140x+47)(1260x+421)(5y-4)} |  |

 |  | + 1 2 ​ ( 126 ​ x + 43) ​ ( 140 ​ x + 47) ​ ( 5 ​ y − 4) \displaystyle+\frac{1}{2(126x+43)(140x+47)(5y-4)} |  |

 |  | + 1 2 ​ ( 126 ​ x + 43) ​ ( 5 ​ y − 4). \displaystyle+\frac{1}{2(126x+43)(5y-4)}. |  |

We consider y = 1 y=1, then we obtain

(40) |  | 5 5 ​ [12 ​ [7 ​ ( 3 ​ x + 1) ¯]] + 1 \displaystyle\frac{5}{5[12[7\underline{(3x+1)}]]+1} | = 1 ( 126 ​ x + 43) ​ ( 140 ​ x + 47) ​ ( 1260 ​ x + 421) \displaystyle=\frac{1}{(126x+43)(140x+47)(1260x+421)} |  |

 |  | + 1 35280 ​ x 2 + 23884 ​ x + 4042 + 1 252 ​ x + 86. \displaystyle+\frac{1}{35280x^{2}+23884x+4042}+\frac{1}{252x+86}. |  |

For v ≡ 2 ( mod 3) ¯ \underline{v\equiv 2\pmod{3}}: In this case, we consider

 | q = p 6 ​ ( x, y) = 252 ​ x ​ ( 5 ​ y − 4) + 841 ​ y − 673, x, y ∈ ℕ ∗. q=p_{6}(x,y)=252x(5y-4)+841y-673,\quad x,y\in\mathbb{N}^{*}. |  |

Which gives

 | 5 5 ​ p 6 ​ ( x, y) + 1 = 5 ( 1260 ​ x + 841) ​ ( 5 ​ y − 4) \displaystyle\frac{5}{5p_{6}(x,y)+1}=\frac{5}{(1260x+841)(5y-4)} | = 1 ( 28 ​ x + 19) ​ ( 1260 ​ x + 841) ​ ( 5 ​ y − 4) \displaystyle=\frac{1}{(28x+19)(1260x+841)(5y-4)} |  |

 |  | + 1 2 ​ ( 28 ​ x + 19) ​ ( 126 ​ x + 85) ​ ( 1260 ​ x + 841) ​ ( 5 ​ y − 4) \displaystyle+\frac{1}{2(28x+19)(126x+85)(1260x+841)(5y-4)} |  |

 |  | + 1 2 ​ ( 126 ​ x + 85) ​ ( 5 ​ y − 4). \displaystyle+\frac{1}{2(126x+85)(5y-4)}. |  |

We consider y = 1 y=1, then we obtain

(41) |  | 5 5 ​ [12 ​ [7 ​ ( 3 ​ x + 2) ¯]] + 1 \displaystyle\frac{5}{5[12[7\underline{(3x+2)}]]+1} | = 1 ( 28 ​ x + 19) ​ ( 1260 ​ x + 841) \displaystyle=\frac{1}{(28x+19)(1260x+841)} |  |

 |  | + 1 2 ​ ( 28 ​ x + 19) ​ ( 126 ​ x + 85) ​ ( 1260 ​ x + 841) + 1 252 ​ x + 170. \displaystyle+\frac{1}{2(28x+19)(126x+85)(1260x+841)}+\frac{1}{252x+170}. |  |

This concludes the proof of Statement (4) of Theorem 2.1. ∎

## Conclusion

In this work, we provide a complete proof of the generalized Erdős–Straus conjecture formulated by Wacław Sierpiński in 1956 for all positive integers a = 5 ​ q + i a=5q+i, where i ∈ { 0, 1, 2, 3, 4 } i\in\{0,1,2,3,4\} and q ≢ 0 ( mod 252) q\not\equiv 0\pmod{252} when i = 1 i=1. In addition, we conjecture that there exists a polynomial that generates all integers q ≡ 0 ( mod 252) q\equiv 0\pmod{252}. This conjecture is supported by the construction of explicit formulae for the decomposition of 5 a \frac{5}{a}.

## Appendix A Mathematica Implementation

Since the polynomial p 1 p_{1} already covers all primes of the form q q for q ≠ 252 ​ c 1 q\not=252c_{1}, it remains to verify that it also covers the case when q = 252 ​ c 1 q=252c_{1}. The following program confirms that the polynomial p 1 p_{1} generates all numbers of the form q = 252 ​ c 1 q=252c_{1}, starting from q = 252 q=252 up to q = qMax q=\text{qMax} (consider for example qMax = 40 ∗ 10 8 \text{qMax}=40*10^{8}). The search is initially performed over the small range { 1, 2, 3 } \{1,2,3\} for the variables x x, y y, or z z. If no solution is found, the algorithm proceeds to loop over the wider range 4 ≤ x ≤ 1 + a 2, a = 5 ​ q + 1. 4\leq x\leq\frac{1+\sqrt{a}}{2},~~a=5q+1.

[⬇][4]

--------------- (*Mathematica Input *) }---------------

baseStep = 252;

nStart = 1;

qStart = baseStep *nStart;

qMax = 10^8;

batchSizeQ = 10^7;

cpuCores = $ProcessorCount;

j = Which [cpuCores <= 2, 4, cpuCores <= 4, 8, cpuCores <= 6, 12,

cpuCores <= 8, 16, cpuCores <= 12, 24, True, 3 cpuCores];

notebookDir = NotebookDirectory [];

If [notebookDir === Null,

Print ["Please save the notebook first before running the code."];

Abort []];

resultsDir = FileNameJoin [{ notebookDir, "Results" }];

If [! DirectoryQ [resultsDir],

CreateDirectory [resultsDir, CreateIntermediateDirectories -> True]];

validateSolution [q_, x_, y_, z_]:=

5 (- x + (- y + x (-1 + 5 y)) z) + 1 == 5 q + 1;

findSolutionForQ [q_]:=

Module [{ a = 5 q + 1, xmax, solution = None, sol, x, y, z },

xmax = Floor [1/2 ( Sqrt [a] + 1)];

(*Step 1:Try x=1,2,3;solve for y,z*)

Do [Quiet@

Check [sol =

FindInstance [

5 (- x0 + (- y + x0 (-1 + 5 y)) z) + 1 == a && y > 0 &&

z > 0, { y, z }, Integers, 1];

If [sol =!= {}, { y, z } = { y, z } /. First [sol];

If [validateSolution [q, x0, y, z], solution = { q, x0, y, z };

Break []]], None], { x0, 1, 3}];

(*Step 2:Try y=1,2,3;solve for x,z*)

If [solution === None,

Do [Quiet@

Check [sol =

FindInstance [

5 (- x + (- y0 + x (-1 + 5 y0)) z) + 1 == a && x > 0 &&

z > 0, { x, z }, Integers, 1];

If [sol =!= {}, { x, z } = { x, z } /. First [sol];

If [validateSolution [q, x, y0, z], solution = { q, x, y0, z };

Break []]], None], { y0, 1, 3}]];

(*Step 3:Try z=1,2,3;solve for x,y*)

If [solution === None,

Do [Quiet@

Check [sol =

FindInstance [

5 (- x + (- y + x (-1 + 5 y)) z0) + 1 == a && x > 0 &&

y > 0, { x, y }, Integers, 1];

If [sol =!= {}, { x, y } = { x, y } /. First [sol];

If [validateSolution [q, x, y, z0], solution = { q, x, y, z0 };

Break []]], None], { z0, 1, 3}]];

(*Step 4:x from 4 to xmax,solve for y,z*)

If [solution === None,

Do [Quiet@

Check [sol =

FindInstance [

5 (- x0 + (- y + x0 (-1 + 5 y)) z) + 1 == a && y > 0 &&

z > 0, { y, z }, Integers, 1];

If [sol =!= {}, { y, z } = { y, z } /. First [sol];

If [validateSolution [q, x0, y, z], solution = { q, x0, y, z };

Break []]], None], { x0, 4, xmax }]];

solution];

processBatch [qBatchMin_, qBatchMax_]:=

Module [{ qValues = Range [qBatchMin, qBatchMax, baseStep],

solutions = {}},

solutions =

ParallelMap [findSolutionForQ, qValues,

Method -> "FinestGrained"];

DeleteCases [solutions, None]];

Print ["CPU cores: ", cpuCores, ", using ", j,

" parallel subkernels"];

Print ["qStart = ", qStart, ", qMax = ", qMax, ", step = ", baseStep];

Print ["Batch size = ", batchSizeQ];

LaunchKernels [];

DistributeDefinitions [baseStep, j, findSolutionForQ, validateSolution,

processBatch, cpuCores, qMax, batchSizeQ];

allSolutions = {};

allUnsolvedQ = {};

batchCount = Ceiling [( qMax - qStart + 1)/ batchSizeQ];

Do [qBatchMin = qStart + batchSizeQ ( b - 1);

qBatchMin =

qBatchMin +

If [Mod [qBatchMin, baseStep] == 0, 0,

baseStep - Mod [qBatchMin, baseStep]];

qBatchMax = Min [qBatchMin + batchSizeQ - 1, qMax];

If [qBatchMin > qMax, Break []];

Print ["\nProcessing batch ", b, "/", batchCount, ": q in [",

qBatchMin, ", ", qBatchMax, "]"];

{ timeBatch, batchSolutions } =

AbsoluteTiming [processBatch [qBatchMin, qBatchMax]];

sortedSolutions = SortBy [batchSolutions, First];

AppendTo [allSolutions, sortedSolutions];

qAll =

Range [qBatchMin, qBatchMax, baseStep]; (*removed PrimeQ filter*)

qSolved = sortedSolutions [[All, 1]];

qUnsolved = Complement [qAll, qSolved];

AppendTo [allUnsolvedQ, qUnsolved];

batchResultsFile =

FileNameJoin [{ resultsDir,

"results_batch" <> IntegerString [b, 10, 3] <> ".csv" }];

unsolvedFile =

FileNameJoin [{ resultsDir,

"unsolved_batch" <> IntegerString [b, 10, 3] <> ".csv" }];

Export [batchResultsFile,

Prepend [sortedSolutions, { "q", "x", "y", "z" }]];

Export [unsolvedFile, Prepend [qUnsolved, "q"]];

Print ["Solutions found: ", Length [sortedSolutions]];

Print ["Unsolved q: ", Length [qUnsolved]];

Print ["Time: ", NumberForm [timeBatch, {6, 2}], " sec"];

Print ["Batch ", b, " complete"], { b, 1, batchCount }];

Print ["\nProcessing complete!"];

Print ["Total solutions found: ", Length [Flatten [allSolutions, 1]]];

Print ["Total unsolved q: ", Length [Flatten [allUnsolvedQ]]];

Export [FileNameJoin [{ resultsDir, "all_solutions.csv" }],

Prepend [Flatten [allSolutions, 1], { "q", "x", "y", "z" }]];

Export [FileNameJoin [{ resultsDir, "all_unsolved.csv" }],

Prepend [Flatten [allUnsolvedQ], "q"]];

Print ["All results saved to: ", resultsDir];

---------------------(* Mathematica Output *)}--------------------- CPU cores: 20, using 60 parallel subkernels qStart = 252, qMax = 100000000, step = 252 Batch size = 10000000 Processing batch 1/10: q in [252, 10000251] Solutions found: 39683 Unsolved q: 0 Time: 59.89 sec Batch 1 complete Processing batch 2/10: q in [10000368, 20000367] Solutions found: 39683 Unsolved q: 0 Time: 45.04 sec Batch 2 complete Processing batch 3/10: q in [20000484, 30000483] Solutions found: 39683 Unsolved q: 0 Time: 45.00 sec Batch 3 complete Processing batch 4/10: q in [30000348, 40000347] Solutions found: 39683 Unsolved q: 0 Time: 44.69 sec Batch 4 complete Processing batch 5/10: q in [40000464, 50000463] Solutions found: 39683 Unsolved q: 0 Time: 98.97 sec Batch 5 complete Processing batch 6/10: q in [50000328, 60000327] Solutions found: 39683 Unsolved q: 0 Time: 51.96 sec Batch 6 complete Processing batch 7/10: q in [60000444, 70000443] Solutions found: 39683 Unsolved q: 0 Time: 44.70 sec Batch 7 complete Processing batch 8/10: q in [70000308, 80000307] Solutions found: 39683 Unsolved q: 0 Time: 44.58 sec Batch 8 complete Processing batch 9/10: q in [80000424, 90000423] Solutions found: 39683 Unsolved q: 0 Time: 44.46 sec Batch 9 complete Processing batch 10/10: q in [90000288, 100000000] Solutions found: 39682 Unsolved q: 0 Time: 44.73 sec Batch 10 complete Processing complete! Total solutions found: 396829 Total unsolved q: 0 All results saved to: a folder named ‘‘Results’’ located in the same directory as the ‘‘.nb’’ file.

“Total solutions found: 396829” represents the number of all values q q covered by p 1 p_{1}.
“Total unsolved q: 0” means that there is no value of q q not covered by p 1 p_{1}.

## References

- [1] S. Ahlgren, K. Ono, and D. Penniston. Zeta functions of finite graphs and representations of integers by quadratic forms. Duke Mathematical Journal, 145(2):171–207, 2008.
- [2] L Bernstein. Zur lösung der diophantischen gleichung m / n = 1 / x + 1 / y + 1 / z m/n=1/x+1/y+1/z, insbesondere im fall m = 4 m=4. Journal für die Reine und Angewandte Mathematik, 211:1–10, 1962.
- [3] M. B. Crawford. On the number of representations of one as the sum of unit fractions. Master’s thesis, Masters of Science in Mathematics, Virginia Polytechnic Institute and State University, 2019.
- [4] C. Elsholtz. Sums of k k unit fractions. Transactions of the American Mathematical Society, 353(8):3209–3227, 2001.
- [5] C. Elsholtz and T. Tao. Counting the number of solutions to the erdős-straus equations on unit fractions. Journal of the Australasian Mathematical Society, 94(1):50–105, 2013.
- [6] D. R. Farnsworth. A non-convergent proof of the erdős-straus conjecture. Mathematical Intelligencer, 40(2):37–39, 2018.
- [7] J. Ghanouchi. An analytic approach of some conjectures related to diophantine equations. Bulletin of Mathematical Sciences and Applications, 1:29–40, 2012.
- [8] J. Ghanouchi. About the erdős conjecture. International Journal of Science and Research, 4(2):341–341, 2015.
- [9] M. Di Giovanni, S. Gallipoli, and M. Gionfriddo. Historical origin and scientific development of graphs, hypergraphs and design theory. Bulletin of Mathematics and Statistics Research, 7:19–23, 2019.
- [10] H. A. Helfgott and G. Harcos. On the erdős-straus conjecture and the largest prime in an arithmetic progression. Acta Arithmetica, 158(4):385–404, 2013.
- [11] R. N. Karasev. On the erdős-straus conjecture in dimension 2. Journal of Number Theory, 151:114–122, 2015.
- [12] S. V. Konyagin and T. N. Shorey. On the number of solutions of the erdős-straus equation. Journal of Number Theory, 76(2):259–266, 1999.
- [13] I Kotsireas. The erdős-straus conjecture on egyptian fractions. In Paul Erdős and his mathematics, pages 140–144. János Bolyai Math. Soc., Budapest, 1999.
- [14] L. J. Mordell. Diophantine Equations. Academic Press, London/New York, 1969.
- [15] M. B. Nathanson. Additive number theory: Inverse problems and the geometry of sumsets, volume 165. Springer Science & Business Media, 1994.
- [16] M. B. Nathanson. Proving the erdős-straus conjecture. The American Mathematical Monthly, 109(5):452–455, 2002.
- [17] D. J. Negash. Solutions to diophantine equation of erdős-straus conjecture, 2018.
- [18] R. Obláth. Sur l’équation diophantienne 4 / n = 1 / x 1 + 1 / x 2 + 1 / x 3 4/n=1/x_{1}+1/x_{2}+1/x_{3}. Mathesis, 59:308–316, 1950.
- [19] L. A. Rosati. Sull’equazione diofantea 4 / n = 1 / x + 1 / y + 1 / z 4/n=1/x+1/y+1/z. Bollettino dell’Unione Matematica Italiana, 3:59–63, 1954.
- [20] S. E Salez. The erdős-straus conjecture: New modular equations and checking up to n = 10 17 n=10^{17}. arXiv preprint arXiv:1406.6307, 2014.
- [21] J. W. Sander. 4 / n = 1 / x + 1 / y + 1 / z 4/n=1/x+1/y+1/z and iwaniec’ half dimensional sieve. Journal of Number Theory, 46:123–136, 1994.
- [22] W. Sierpiński. Sur les décompositions de nombres rationnels en fractions primaires. Mathesis, 65:16–32, 1956.
- [23] S. Subburam and A. Togbé. A note on the erdős–straus conjecture. Periodica Mathematica Hungarica, 72:43–49, 2016.
- [24] A Swett. The erdős-straus conjecture. Rev. 10/28/99. [http://math.uindy.edu/swett/esc.htm][5].
- [25] L. N. Vaserstein. The geometric lemma and the erdős-straus conjecture. Discrete Mathematics, 308(16):3516–3518, 2008.
- [26] R. C. Vaughan. On a problem of erdős, straus and schinzel. Mathematika, 17:193–198, 1970.
- [27] K. Yamamoto. On the diophantine equation 4 / n = 1 / x + 1 / y + 1 / z 4/n=1/x+1/y+1/z. Memoirs of the Faculty of Science, Kyushu University, 19:37–47, 1965.
- [28] R. K. Guy, *Unsolved Problems in Number Theory*, 3rd edition, Springer, 2004.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:bilal.ghermoul@univ-bba.dz
[4]: data:text/plain;base64,IC0tLS0tLS0tLS0tLS0tLSgqIE1hdGhlbWF0aWNhIElucHV0ICopfS0tLS0tLS0tLS0tLS0tLQpiYXNlU3RlcCA9IDI1MjsKblN0YXJ0ID0gMTsKcVN0YXJ0ID0gYmFzZVN0ZXAqblN0YXJ0OwpxTWF4ID0gMTBeODsKYmF0Y2hTaXplUSA9IDEwXjc7CmNwdUNvcmVzID0gJFByb2Nlc3NvckNvdW50OwoKaiA9IFdoaWNoW2NwdUNvcmVzIDw9IDIsIDQsIGNwdUNvcmVzIDw9IDQsIDgsIGNwdUNvcmVzIDw9IDYsIDEyLAogICBjcHVDb3JlcyA8PSA4LCAxNiwgY3B1Q29yZXMgPD0gMTIsIDI0LCBUcnVlLCAzIGNwdUNvcmVzXTsKCm5vdGVib29rRGlyID0gTm90ZWJvb2tEaXJlY3RvcnlbXTsKSWZbbm90ZWJvb2tEaXIgPT09IE51bGwsCiAgUHJpbnRbIlBsZWFzZSBzYXZlIHRoZSBub3RlYm9vayBmaXJzdCBiZWZvcmUgcnVubmluZyB0aGUgY29kZS4iXTsKICBBYm9ydFtdXTsKCnJlc3VsdHNEaXIgPSBGaWxlTmFtZUpvaW5be25vdGVib29rRGlyLCAiUmVzdWx0cyJ9XTsKSWZbISBEaXJlY3RvcnlRW3Jlc3VsdHNEaXJdLAogIENyZWF0ZURpcmVjdG9yeVtyZXN1bHRzRGlyLCBDcmVhdGVJbnRlcm1lZGlhdGVEaXJlY3RvcmllcyAtPiBUcnVlXV07Cgp2YWxpZGF0ZVNvbHV0aW9uW3FfLCB4XywgeV8sIHpfXSA6PQogIDUgKC14ICsgKC15ICsgeCAoLTEgKyA1IHkpKSB6KSArIDEgPT0gNSBxICsgMTsKCmZpbmRTb2x1dGlvbkZvclFbcV9dIDo9CiAgTW9kdWxlW3thID0gNSBxICsgMSwgeG1heCwgc29sdXRpb24gPSBOb25lLCBzb2wsIHgsIHksIHp9LAogICB4bWF4ID0gRmxvb3JbMS8yIChTcXJ0W2FdICsgMSldOwogICAoKlN0ZXAgMTpUcnkgeD0xLDIsMztzb2x2ZSBmb3IgeSx6KikKICAgRG9bUXVpZXRACiAgICAgQ2hlY2tbc29sID0KICAgICAgIEZpbmRJbnN0YW5jZVsKICAgICAgICA1ICgteDAgKyAoLXkgKyB4MCAoLTEgKyA1IHkpKSB6KSArIDEgPT0gYSAmJiB5ID4gMCAmJgogICAgICAgICB6ID4gMCwge3ksIHp9LCBJbnRlZ2VycywgMV07CiAgICAgIElmW3NvbCA9IT0ge30sIHt5LCB6fSA9IHt5LCB6fSAvLiBGaXJzdFtzb2xdOwogICAgICAgSWZbdmFsaWRhdGVTb2x1dGlvbltxLCB4MCwgeSwgel0sIHNvbHV0aW9uID0ge3EsIHgwLCB5LCB6fTsKICAgICAgICBCcmVha1tdXV0sIE5vbmVdLCB7eDAsIDEsIDN9XTsKICAgKCpTdGVwIDI6VHJ5IHk9MSwyLDM7c29sdmUgZm9yIHgseiopCiAgIElmW3NvbHV0aW9uID09PSBOb25lLAogICAgRG9bUXVpZXRACiAgICAgIENoZWNrW3NvbCA9CiAgICAgICAgRmluZEluc3RhbmNlWwogICAgICAgICA1ICgteCArICgteTAgKyB4ICgtMSArIDUgeTApKSB6KSArIDEgPT0gYSAmJiB4ID4gMCAmJgogICAgICAgICAgeiA+IDAsIHt4LCB6fSwgSW50ZWdlcnMsIDFdOwogICAgICAgSWZbc29sID0hPSB7fSwge3gsIHp9ID0ge3gsIHp9IC8uIEZpcnN0W3NvbF07CiAgICAgICAgSWZbdmFsaWRhdGVTb2x1dGlvbltxLCB4LCB5MCwgel0sIHNvbHV0aW9uID0ge3EsIHgsIHkwLCB6fTsKICAgICAgICAgQnJlYWtbXV1dLCBOb25lXSwge3kwLCAxLCAzfV1dOwogICAoKlN0ZXAgMzpUcnkgej0xLDIsMztzb2x2ZSBmb3IgeCx5KikKICAgSWZbc29sdXRpb24gPT09IE5vbmUsCiAgICBEb1tRdWlldEAKICAgICAgQ2hlY2tbc29sID0KICAgICAgICBGaW5kSW5zdGFuY2VbCiAgICAgICAgIDUgKC14ICsgKC15ICsgeCAoLTEgKyA1IHkpKSB6MCkgKyAxID09IGEgJiYgeCA+IDAgJiYKICAgICAgICAgIHkgPiAwLCB7eCwgeX0sIEludGVnZXJzLCAxXTsKICAgICAgIElmW3NvbCA9IT0ge30sIHt4LCB5fSA9IHt4LCB5fSAvLiBGaXJzdFtzb2xdOwogICAgICAgIElmW3ZhbGlkYXRlU29sdXRpb25bcSwgeCwgeSwgejBdLCBzb2x1dGlvbiA9IHtxLCB4LCB5LCB6MH07CiAgICAgICAgIEJyZWFrW11dXSwgTm9uZV0sIHt6MCwgMSwgM31dXTsKICAgKCpTdGVwIDQ6eCBmcm9tIDQgdG8geG1heCxzb2x2ZSBmb3IgeSx6KikKICAgSWZbc29sdXRpb24gPT09IE5vbmUsCiAgICBEb1tRdWlldEAKICAgICAgQ2hlY2tbc29sID0KICAgICAgICBGaW5kSW5zdGFuY2VbCiAgICAgICAgIDUgKC14MCArICgteSArIHgwICgtMSArIDUgeSkpIHopICsgMSA9PSBhICYmIHkgPiAwICYmCiAgICAgICAgICB6ID4gMCwge3ksIHp9LCBJbnRlZ2VycywgMV07CiAgICAgICBJZltzb2wgPSE9IHt9LCB7eSwgen0gPSB7eSwgen0gLy4gRmlyc3Rbc29sXTsKICAgICAgICBJZlt2YWxpZGF0ZVNvbHV0aW9uW3EsIHgwLCB5LCB6XSwgc29sdXRpb24gPSB7cSwgeDAsIHksIHp9OwogICAgICAgICBCcmVha1tdXV0sIE5vbmVdLCB7eDAsIDQsIHhtYXh9XV07CiAgIHNvbHV0aW9uXTsKCnByb2Nlc3NCYXRjaFtxQmF0Y2hNaW5fLCBxQmF0Y2hNYXhfXSA6PQogIE1vZHVsZVt7cVZhbHVlcyA9IFJhbmdlW3FCYXRjaE1pbiwgcUJhdGNoTWF4LCBiYXNlU3RlcF0sCiAgICBzb2x1dGlvbnMgPSB7fX0sCiAgIHNvbHV0aW9ucyA9CiAgICBQYXJhbGxlbE1hcFtmaW5kU29sdXRpb25Gb3JRLCBxVmFsdWVzLAogICAgIE1ldGhvZCAtPiAiRmluZXN0R3JhaW5lZCJdOwogICBEZWxldGVDYXNlc1tzb2x1dGlvbnMsIE5vbmVdXTsKClByaW50WyJDUFUgY29yZXM6ICIsIGNwdUNvcmVzLCAiLCB1c2luZyAiLCBqLAogICIgcGFyYWxsZWwgc3Via2VybmVscyJdOwpQcmludFsicVN0YXJ0ID0gIiwgcVN0YXJ0LCAiLCBxTWF4ID0gIiwgcU1heCwgIiwgc3RlcCA9ICIsIGJhc2VTdGVwXTsKUHJpbnRbIkJhdGNoIHNpemUgPSAiLCBiYXRjaFNpemVRXTsKCkxhdW5jaEtlcm5lbHNbXTsKRGlzdHJpYnV0ZURlZmluaXRpb25zW2Jhc2VTdGVwLCBqLCBmaW5kU29sdXRpb25Gb3JRLCB2YWxpZGF0ZVNvbHV0aW9uLAogICBwcm9jZXNzQmF0Y2gsIGNwdUNvcmVzLCBxTWF4LCBiYXRjaFNpemVRXTsKCmFsbFNvbHV0aW9ucyA9IHt9OwphbGxVbnNvbHZlZFEgPSB7fTsKYmF0Y2hDb3VudCA9IENlaWxpbmdbKHFNYXggLSBxU3RhcnQgKyAxKS9iYXRjaFNpemVRXTsKCkRvW3FCYXRjaE1pbiA9IHFTdGFydCArIGJhdGNoU2l6ZVEgKGIgLSAxKTsKICBxQmF0Y2hNaW4gPQogICBxQmF0Y2hNaW4gKwogICAgSWZbTW9kW3FCYXRjaE1pbiwgYmFzZVN0ZXBdID09IDAsIDAsCiAgICAgYmFzZVN0ZXAgLSBNb2RbcUJhdGNoTWluLCBiYXNlU3RlcF1dOwogIHFCYXRjaE1heCA9IE1pbltxQmF0Y2hNaW4gKyBiYXRjaFNpemVRIC0gMSwgcU1heF07CiAgSWZbcUJhdGNoTWluID4gcU1heCwgQnJlYWtbXV07CiAgUHJpbnRbIlxuUHJvY2Vzc2luZyBiYXRjaCAiLCBiLCAiLyIsIGJhdGNoQ291bnQsICI6IHEgaW4gWyIsCiAgIHFCYXRjaE1pbiwgIiwgIiwgcUJhdGNoTWF4LCAiXSJdOwogIHt0aW1lQmF0Y2gsIGJhdGNoU29sdXRpb25zfSA9CiAgIEFic29sdXRlVGltaW5nW3Byb2Nlc3NCYXRjaFtxQmF0Y2hNaW4sIHFCYXRjaE1heF1dOwogIHNvcnRlZFNvbHV0aW9ucyA9IFNvcnRCeVtiYXRjaFNvbHV0aW9ucywgRmlyc3RdOwogIEFwcGVuZFRvW2FsbFNvbHV0aW9ucywgc29ydGVkU29sdXRpb25zXTsKICBxQWxsID0KICAgUmFuZ2VbcUJhdGNoTWluLCBxQmF0Y2hNYXgsIGJhc2VTdGVwXTsoKnJlbW92ZWQgUHJpbWVRIGZpbHRlciopCiAgcVNvbHZlZCA9IHNvcnRlZFNvbHV0aW9uc1tbQWxsLCAxXV07CiAgcVVuc29sdmVkID0gQ29tcGxlbWVudFtxQWxsLCBxU29sdmVkXTsKICBBcHBlbmRUb1thbGxVbnNvbHZlZFEsIHFVbnNvbHZlZF07CiAgYmF0Y2hSZXN1bHRzRmlsZSA9CiAgIEZpbGVOYW1lSm9pblt7cmVzdWx0c0RpciwKICAgICAicmVzdWx0c19iYXRjaCIgPD4gSW50ZWdlclN0cmluZ1tiLCAxMCwgM10gPD4gIi5jc3YifV07CiAgdW5zb2x2ZWRGaWxlID0KICAgRmlsZU5hbWVKb2luW3tyZXN1bHRzRGlyLAogICAgICJ1bnNvbHZlZF9iYXRjaCIgPD4gSW50ZWdlclN0cmluZ1tiLCAxMCwgM10gPD4gIi5jc3YifV07CiAgRXhwb3J0W2JhdGNoUmVzdWx0c0ZpbGUsCiAgIFByZXBlbmRbc29ydGVkU29sdXRpb25zLCB7InEiLCAieCIsICJ5IiwgInoifV1dOwogIEV4cG9ydFt1bnNvbHZlZEZpbGUsIFByZXBlbmRbcVVuc29sdmVkLCAicSJdXTsKICBQcmludFsiU29sdXRpb25zIGZvdW5kOiAiLCBMZW5ndGhbc29ydGVkU29sdXRpb25zXV07CiAgUHJpbnRbIlVuc29sdmVkIHE6ICIsIExlbmd0aFtxVW5zb2x2ZWRdXTsKICBQcmludFsiVGltZTogIiwgTnVtYmVyRm9ybVt0aW1lQmF0Y2gsIHs2LCAyfV0sICIgc2VjIl07CiAgUHJpbnRbIkJhdGNoICIsIGIsICIgY29tcGxldGUiXSwge2IsIDEsIGJhdGNoQ291bnR9XTsKClByaW50WyJcblByb2Nlc3NpbmcgY29tcGxldGUhIl07ClByaW50WyJUb3RhbCBzb2x1dGlvbnMgZm91bmQ6ICIsIExlbmd0aFtGbGF0dGVuW2FsbFNvbHV0aW9ucywgMV1dXTsKUHJpbnRbIlRvdGFsIHVuc29sdmVkIHE6ICIsIExlbmd0aFtGbGF0dGVuW2FsbFVuc29sdmVkUV1dXTsKCkV4cG9ydFtGaWxlTmFtZUpvaW5be3Jlc3VsdHNEaXIsICJhbGxfc29sdXRpb25zLmNzdiJ9XSwKICBQcmVwZW5kW0ZsYXR0ZW5bYWxsU29sdXRpb25zLCAxXSwgeyJxIiwgIngiLCAieSIsICJ6In1dXTsKRXhwb3J0W0ZpbGVOYW1lSm9pblt7cmVzdWx0c0RpciwgImFsbF91bnNvbHZlZC5jc3YifV0sCiAgUHJlcGVuZFtGbGF0dGVuW2FsbFVuc29sdmVkUV0sICJxIl1dOwoKUHJpbnRbIkFsbCByZXN1bHRzIHNhdmVkIHRvOiAiLCByZXN1bHRzRGlyXTs=
[5]: http://math.uindy.edu/swett/esc.htm
