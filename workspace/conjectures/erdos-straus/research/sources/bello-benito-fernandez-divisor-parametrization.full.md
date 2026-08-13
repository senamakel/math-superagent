<!-- source: https://arxiv.org/html/2606.10922v1 | converted from HTML -->

A Divisor Parametrization for the Erdős–Straus Conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2606.10922v1 [math.NT] 09 Jun 2026

# A Divisor Parametrization for the Erdős–Straus Conjecture

M. Bello-Hernández M. Benito E. Fernández

August 11, 2026

Abstract

We study representations of 1 / n 1/n as a sum of three unit fractions whose denominators are all divisible by a prescribed integer m m. After scaling, this is equivalent to representing m / n m/n as a sum of three unit fractions. Our main focus is the Erdős–Straus case m = 4 m=4. We introduce a divisor-based function fab ⁡ ( n, a, b) \mathrm{fab}(n,a,b), prove that its admissible parameters recover exactly the decompositions of 1 / n 1/n with all three denominators divisible by 4 4, and compare this parametrization with well-known Type I/II descriptions.

We also relate the construction to a shifted cubic equation and to the surface

 | P ⁡ ( u, v, w) = u ​ v ​ w − u − v, P(u,v,w)=uvw-u-v, |  |

whose subfamily P ⁡ ( α + 1, 4 ​ β + 3, 4 ​ γ + 3) P(\alpha+1,4\beta+3,4\gamma+3) gives a natural source of examples but contains no perfect squares. Finally, we prove a translation invariance property of fab \fabop, derive a modular sieve, and report computational evidence: all primes p ≡ 1 ( mod 4) p\equiv 1\pmod{4} with p < 10 14 p<10^{14} are detected by fab ⁡ ( p, a, b) \fabop(p,a,b) with 1 ≤ a, b ≤ 11 1\leq a,b\leq 11, although some composite values require larger parameters. We conclude with comparisons to Bradford’s two-variable reduction and Ventas’ FCT sources for the 5 / n 5/n setting.

## 1 Introduction

The Erdős–Straus conjecture asserts that, for every integer n ≥ 2 n\geq 2, there exist positive integers x, y, z x,y,z such that

 | 4 n = 1 x + 1 y + 1 z. \frac{4}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}. |  | (1) |

If the conjecture is known for a divisor p p of n n, then a decomposition for 4 / p 4/p can be scaled to one for 4 / n 4/n. Thus, as usual, it is enough to consider prime values of n n. We refer to Mordell [8], Yamamoto [12], Vaughan [10], Schinzel [9], Elsholtz–Tao [4], Bradford [2], and our manuscript [1] and the references therein for background on the conjecture and on other parametrizations of its solutions.

We present several complementary ways to generate and understand Erdős–Straus decompositions: (i) a general divisor-based procedure encoded by fab \fabop, (ii) the well-known Type I/II parametrizations and a basic rigidity obstruction for finite congruence covers, (iii) an algebraic-geometric model via the shifted cubic equation and the surface u ​ v ​ w − u − v = n uvw-u-v=n, and (iv) computational consequences, in particular a translation-invariant modular sieve.

We compare this divisor search with the well-known Type I and Type II forms. It is easy to see that fixing three of the four parameters to lie in a finite set yields only finitely many congruence classes, which cannot cover all primes p ≡ 1 ( mod 4) p\equiv 1\pmod{4}. This contrasts with the empirical effectiveness observed in the small search window of 1 ≤ a, b ≤ 11 1\leq a,b\leq 11 for the primes tested in our computations.

A second theme is the connection with the shifted equation

 | 1 n = 1 n + a + 1 n + b + 1 n + c \frac{1}{n}=\frac{1}{n+a}+\frac{1}{n+b}+\frac{1}{n+c} |  |

and with the polynomial surface

 | P ⁡ ( u, v, w) = u ​ v ​ w − u − v. P(u,v,w)=uvw-u-v. |  |

The decompositions produced by fab \fabop give rational points on this surface. The integral subfamily P ⁡ ( a + 1, 4 ​ b + 3, 4 ​ c + 3) P(a+1,4b+3,4c+3) provides a simple source of examples, but it also has a structural limitation: it contains no perfect squares. This is useful to keep in mind when comparing the polynomial parametrization with the more flexible divisor search.

In addition, we show that the ideas developed here can be adapted to obtain decompositions of fractions of the form 5 / n 5/n, suggesting that the method is not restricted to the classical case 4 / n 4/n. We obtain the Bradford’s two-variable reduction in 5 / n 5/n setting.

In the computational section we write down a modular lifting principle for bounded searches and explain how the residue-class sieve is used in the computations. It also clarifies why the bound 1 ≤ a, b ≤ 11 1\leq a,b\leq 11 should be interpreted cautiously: although it appears very effective for the tested primes, there are composite values not detected in that window but detected as soon as one allows a a or b b to be slightly larger.

## 2 A Divisor Identity and the Function fab ⁡ ( n, a, b) \fabop(n,a,b)

Let n, k ∈ ℕ n,k\in\mathbb{N} and put A = n ⁡ ( n + k) A=n(n+k). Then

 | 1 n = 1 n + k + k A + d + k A + d 1 \frac{1}{n}=\frac{1}{n+k}+\frac{k}{A+d}+\frac{k}{A+d_{1}} |  | (2) |

is equivalent to d ​ d 1 = A 2 = n 2 ​ ( n + k) 2. dd_{1}=A^{2}=n^{2}(n+k)^{2}. See [7].

###### Definition 1.

Let n, a, b ∈ ℕ n,a,b\in\mathbb{N}. Define the function fab ⁡ ( n, a, b) \fabop(n,a,b) to be the least positive divisor k k of a + b ​ n a+bn such that

 | k ≡ 3 ( mod 4), 4 b ∣ a + b ​ n k ( n + k), 4 a ∣ n a + b ​ n k ( n + k), k\equiv 3\pmod{4},\qquad 4b\mid\frac{a+bn}{k}(n+k),\qquad 4a\mid n\frac{a+bn}{k}(n+k), |  | (3) |

if such a divisor exists; otherwise set fab ⁡ ( n, a, b) = 0 \fabop(n,a,b)=0. We refer to k, a, b k,a,b satisfying ( 3) as admissible values for n n.

###### Proposition 2.

If fab ⁡ ( n, a, b) = k > 0 \fabop(n,a,b)=k>0, then

 | 1 n = 1 n + k + 1 ( a + b ​ n) ​ ( n + k) b ​ k + 1 ( a + b ​ n) ​ ( n + k) ​ n a ​ k. \frac{1}{n}=\frac{1}{n+k}+\frac{1}{\dfrac{(a+bn)(n+k)}{bk}}+\frac{1}{\dfrac{(a+bn)(n+k)n}{ak}}. |  | (4) |

If moreover n ≡ 1 ( mod 4) n\equiv 1\pmod{4}, then ( 4) gives a solution of ( 1).

###### Proof.

If fab ⁡ ( n, a, b) = k > 0 \fabop(n,a,b)=k>0, then d = a b ​ ( n + k) d=\frac{a}{b}(n+k) and d 1 = ( b / a) ​ n 2 ​ ( n + k) d_{1}=(b/a)n^{2}(n+k) are divisors of A 2 A^{2}. Then ( 2) becomes

 | 1 n = 1 n + k + k ​ b ( n + k) ​ ( a + b ​ n) + k ​ a n ​ ( n + k) ​ ( a + b ​ n). \frac{1}{n}=\frac{1}{n+k}+\frac{kb}{(n+k)(a+bn)}+\frac{ka}{n(n+k)(a+bn)}. |  | (5) |

By ( 3), the three denominators in ( 4) are divisible by 4 4. ∎

###### Example 3.

For n = 5 n=5, fab ⁡ ( 5, 1, 1) = 3 \fabop(5,1,1)=3, and

 | 4 5 = 1 2 + 1 4 + 1 20. \frac{4}{5}=\frac{1}{2}+\frac{1}{4}+\frac{1}{20}. |  |

###### Remark 4 (Prime squares).

The function fab \fabop also gives a very simple decomposition for the squares of primes p ≡ 3 ( mod 4) p\equiv 3\pmod{4}. Indeed, let n = p 2, a = k = p, b = 1. n=p^{2},\,a=k=p,\,b=1. Then a + b ​ n k = p + 1, \frac{a+bn}{k}=p+1, n + k = p 2 + p = p ⁡ ( p + 1) n+k=p^{2}+p=p(p+1), and ( 3) holds. Hence fab ⁡ ( p 2, p, 1) > 0. \fabop(p^{2},p,1)>0.

For primes p ≡ 1 ( mod 4) p\equiv 1\pmod{4}, computations suggest that one can often find a positive integer b b such that fab ⁡ ( p 2, p, b) > 0 \fabop(p^{2},p,b)>0. This case appears to be subtler: with n = p 2 n=p^{2}, a = p a=p, one has

 | a + b ​ n = p ⁡ ( b ​ p + 1), a+bn=p(bp+1), |  |

and one has to find a divisor k ≡ 3 ( mod 4) k\equiv 3\pmod{4} of b ​ p + 1 bp+1 satisfying the remaining divisibility condition. We do not pursue this question here.

###### Theorem 5 (Completeness of the divisor identity).

Let n ≡ 1 ( mod 4) n\equiv 1\pmod{4}. Suppose that

 | 1 n = 1 x + 1 y + 1 z \frac{1}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z} |  | (6) |

with 4 | x 4\mid x, 4 | y 4\mid y, 4 | z 4\mid z. Then there exist a, b ∈ ℕ a,b\in\mathbb{N} and an admissible divisor k ≡ 3 ( mod 4) k\equiv 3\pmod{4} such that the divisor identity ( 4) associated with f ​ a ​ b ​ ( n, a, b) fab(n,a,b) reproduces exactly the given decomposition.

###### Proof.

Since all summands in ( 6) are positive, each denominator is larger than n n. In particular, x > n x>n. Define

 | k = x − n. k=x-n. |  | (7) |

Since 4 | x 4\mid x and n ≡ 1 ( mod 4) n\equiv 1\pmod{4}, we have k = x − n ≡ 0 − 1 ≡ 3 ( mod 4). k=x-n\equiv 0-1\equiv 3\pmod{4}. Moreover, x = n + k x=n+k.

From ( 6), we obtain

 | z ⁡ ( k ​ y − n ​ x) = n ​ x ​ y. z(ky-nx)=nxy. |  | (8) |

Let

 | g = gcd ⁡ ( x, y), b = x g, a = k ​ y − n ​ x g. g=\gcdop(x,y),\qquad b=\frac{x}{g},\qquad a=\frac{ky-nx}{g}. |  | (9) |

The positivity of a a follows from ( 8). Therefore a, b ∈ ℕ a,b\in\mathbb{N}.

We now compute a + b ​ n = k ​ y / g. a+bn=ky/{g}. Since g | y g\mid y, it follows that

 | k | a + b ​ n. k\mid a+bn. |  | (10) |

Write q = ( a + b ​ n) / k. q={(a+bn)}/{k}. Then q = y / g. q={y}/{g}. Consequently, q ⁡ ( n + k) = y g ​ x = x g ​ y = b ​ y. q(n+k)=\frac{y}{g}x=\frac{x}{g}y=by. Since 4 | y 4\mid y, we get

 | 4 ​ b | q ⁡ ( n + k). 4b\mid q(n+k). |  | (11) |

On the other hand, dividing by g g in ( 8) and using the definition of a a, we obtain

 | a ​ z = n ​ x ​ y g. az=\frac{nxy}{g}. |  |

Also n ​ x ​ y / g = n ​ q ​ ( n + k). {nxy}/{g}=nq(n+k). Thus n ​ q ​ ( n + k) = a ​ z. nq(n+k)=az. Since 4 | z 4\mid z, it follows that

 | 4 ​ a | n ​ q ​ ( n + k). 4a\mid nq(n+k). |  | (12) |

Therefore, ( 10), ( 11), and ( 12) say that k k satisfies the admissibility conditions for the pair ( a, b) (a,b).

It remains to check that the associated identity recovers the original triple ( x, y, z) (x,y,z). According to ( 4), the first denominator is n + k = x. n+k=x. The second denominator is

 | ( a + b ​ n) ​ ( n + k) b ​ k = ( k ​ y / g) ​ x ( x / g) ​ k = y. \frac{(a+bn)(n+k)}{bk}=\frac{(ky/g)x}{(x/g)k}=y. |  |

The third denominator is

 | ( a + b ​ n) ​ ( n + k) ​ n a ​ k = ( k ​ y / g) ​ x ​ n a ​ k = n ​ x ​ y a ​ g. \frac{(a+bn)(n+k)n}{ak}=\frac{(ky/g)xn}{ak}=\frac{nxy}{ag}. |  |

By ( 8) and a = ( k ​ y − n ​ x) / g a=(ky-nx)/g, we have a ​ z ​ g = n ​ x ​ y azg=nxy, and hence

 | n ​ x ​ y a ​ g = z. \frac{nxy}{ag}=z. |  |

Thus the identity ( 4) associated with fab \fabop is exactly ( 6). ∎

###### Remark 6.

In the theorem above, we do not assert that fab ⁡ ( n, a, b) \fabop(n,a,b) coincides with the value of k k given by ( 7), with a, b a,b as in ( 9). We only establish that k ≥ fab ⁡ ( n, a, b) > 0 k\geq\fabop(n,a,b)>0 for those values of a, b a,b.

## 3 Well-known Type I/II Forms and the Cubic Equation

We shall only use the following standard parametrization as background; see Mordell [8, p. 287] or Yamamoto [12]. In order to avoid a conflict with the parameters of the function fab \fabop, we denote the parameters by capital letters A, B, C, D A,B,C,D. Thus, for prime n n, a solution of ( 1) (1) exists if and only if one can find positive integers A, B, C, D A,B,C,D such that either

 | ( 4 ​ A ​ B ​ C − 1) ​ D = ( A + B) ​ n, (4ABC-1)D=(A+B)n, |  | (13) |

or

 | ( 4 ​ A ​ B ​ C − 1) ​ D = A ​ n + B. (4ABC-1)D=An+B. |  | (14) |

Dividing by A ​ B ​ C ​ D ​ n ABCDn gives, respectively,

 | 4 n = 1 A ​ B ​ C ​ n + 1 B ​ C ​ D + 1 A ​ C ​ D, \frac{4}{n}=\frac{1}{ABCn}+\frac{1}{BCD}+\frac{1}{ACD}, |  | (15) |

or

 | 4 n = 1 A ​ B ​ C ​ n + 1 B ​ C ​ D + 1 A ​ C ​ D ​ n. \frac{4}{n}=\frac{1}{ABCn}+\frac{1}{BCD}+\frac{1}{ACDn}. |  | (16) |

Thus ( 15) has exactly one denominator divisible by n n, whereas ( 16) has two.

###### Remark 7.

To compare these formulae with the divisor identity associated with fab \fabop in Proposition 2, one has to pass from decompositions of 4 / n 4/n to decompositions of 1 / n 1/n. Let a f a_{\mathrm{f}} and b f b_{\mathrm{f}} denote the two parameters of the choice function fab ⁡ ( n, a f, b f) \fabop(n,a_{\mathrm{f}},b_{\mathrm{f}}), in order to distinguish them from the parameters A, B, C, D A,B,C,D. The completeness construction of Theorem 5 makes the comparison explicit. For instance, put G = gcd ⁡ ( A ​ n, D). G=\gcd(An,D). If in either type we choose n + k = 4 ​ A ​ B ​ C ​ n, n+k=4ABCn, then k = n ⁡ ( 4 ​ A ​ B ​ C − 1), b f = A ​ n G. k=n(4ABC-1),\,b_{\mathrm{f}}=\frac{An}{G}. Moreover, in type I decomposition a f = B ​ n 2 / G a_{\mathrm{f}}={Bn^{2}}/{G}, while in type II decomposition a f = B ​ n / G a_{\mathrm{f}}={Bn}/{G}.

Likewise, by interchanging the order of the summands in the decompositions displayed in ( 15) and ( 16), one obtains values of k k, a f a_{\mathrm{f}}, and b f b_{\mathrm{f}} for which the decompositions associated with these parameters, as prescribed by Proposition 2, agree with the decompositions given there.

As noted above, these decompositions do not imply that fab ⁡ ( n, a f, b f) = k \fabop(n,a_{\mathrm{f}},b_{\mathrm{f}})=k; they only show that

 | 0 < fab ⁡ ( n, a f, b f) ≤ k. 0<\fabop(n,a_{\mathrm{f}},b_{\mathrm{f}})\leq k. |  |

The following elementary observation explains why fixing most of the parameters in ( 13) or ( 14) cannot by itself lead to a finite congruence cover for all primes p ≡ 1 ( mod 4) p\equiv 1\pmod{4}. For a proof of this result, we refer the reader to [1].

###### Theorem 8.

Fix finite sets of triples of positive integers for the four possible choices of three fixed parameters. Then the corresponding finite-parameter subfamilies of either ( 13) or ( 14) cannot cover all primes p ≡ 1 ( mod 4) p\equiv 1\pmod{4}.

###### Remark 9.

This obstruction contrasts with the computational behaviour of fab \fabop: the authors have verified that, for every tested prime

 | 5 ≤ p ≡ 1 ( mod 4), p < 10 14, 5\leq p\equiv 1\pmod{4},\qquad p<10^{14}, |  |

there exist 1 ≤ a, b ≤ 11 1\leq a,b\leq 11 such that fab ⁡ ( p, a, b) > 0 \fabop(p,a,b)>0.

The shifted decomposition

 | 1 n = 1 n + a + 1 n + b + 1 n + c \frac{1}{n}=\frac{1}{n+a}+\frac{1}{n+b}+\frac{1}{n+c} |  | (17) |

is equivalent, after clearing denominators, to

 | a ​ b ​ c = n 2 ​ ( 2 ​ n + a + b + c), abc=n^{2}(2n+a+b+c), |  |

or

 | 2 ​ n 3 + ( a + b + c) ​ n 2 − a ​ b ​ c = 0. 2n^{3}+(a+b+c)n^{2}-abc=0. |  |

###### Remark 10.

The change of variables induced by the divisor identity in Proposition 2 separates the geometric and arithmetic parts of the construction. Indeed, let A, B, k, q ∈ ℕ A,B,k,q\in\mathbb{N}, and put

 | α = k, β = A + n ​ q B, γ = n 2 ​ ( B + q) A. \alpha=k,\qquad\beta=\frac{A+nq}{B},\qquad\gamma=\frac{n^{2}(B+q)}{A}. |  |

Then a direct computation gives

 | α ​ β ​ γ − n 2 ​ ( 2 ​ n + α + β + γ) = n 2 A ​ B ​ ( k ​ q − A − B ​ n) ​ ( A + B ​ n + n ​ q). \alpha\beta\gamma-n^{2}(2n+\alpha+\beta+\gamma)=\frac{n^{2}}{AB}(kq-A-Bn)(A+Bn+nq). |  |

Thus, in the positive range, the shifted cubic equation

 | α ​ β ​ γ = n 2 ​ ( 2 ​ n + α + β + γ) \alpha\beta\gamma=n^{2}(2n+\alpha+\beta+\gamma) |  |

is equivalent, under this change of variables, to the linear relation

 | k ​ q = A + B ​ n. kq=A+Bn. |  |

This relation should not be confused with the admissibility conditions in the definition of fab \fabop. It only ensures that the corresponding shifted parameters lie on the cubic, possibly as rational points. To obtain an integral decomposition one must also impose

 | 4 B ∣ q ( n + k), 4 A ∣ n q ( n + k). 4B\mid q(n+k),\qquad 4A\mid nq(n+k). |  |

Thus the divisor relation cuts out the cubic, whereas the remaining admissibility conditions select the integral congruence-compatible points produced by fab \fabop.

A simple subfamily comes from

 | P ⁡ ( u, v, w) = u ​ v ​ w − u − v. P(u,v,w)=uvw-u-v. |  | (18) |

If P = P ⁡ ( u, v, w) > 0 P=P(u,v,w)>0, then

 | 1 P = 1 P + v + 1 u ⁡ ( w ​ P + 1) + 1 P ⁡ ( w ​ P + 1), \frac{1}{P}=\frac{1}{P+v}+\frac{1}{u(wP+1)}+\frac{1}{P(wP+1)}, |  | (19) |

and

 | w ​ P + 1 = ( u ​ w − 1) ​ ( v ​ w − 1). wP+1=(uw-1)(vw-1). |  |

In the shifted notation,

 | n = P, a = v, b = ( u ​ w − 1) ​ P + u, c = P 2 ​ w. n=P,\qquad a=v,\qquad b=(uw-1)P+u,\qquad c=P^{2}w. |  |

For the congruence class relevant to ( 1), define

 | p ⁡ ( α, β, γ) = P ⁡ ( α + 1, 4 ​ β + 3, 4 ​ γ + 3) p(\alpha,\beta,\gamma)=P(\alpha+1,4\beta+3,4\gamma+3) |  | (20) |

that is,

 | p ⁡ ( α, β, γ) = ( α + 1) ​ ( 4 ​ β + 3) ​ ( 4 ​ γ + 3) − ( α + 1) − ( 4 ​ β + 3). p(\alpha,\beta,\gamma)=(\alpha+1)(4\beta+3)(4\gamma+3)-(\alpha+1)-(4\beta+3). |  |

###### Remark 11.

In [1] we show that the integral polynomial subfamily ( 20) can never account for square values of n n. This should be compared with the choice function fab \fabop: as observed above, fab \fabop gives immediate decompositions for n = p 2 n=p^{2} when p ≡ 3 ( mod 4) p\equiv 3\pmod{4}, by taking a = p a=p, b = 1 b=1, and k = p k=p. Thus the polynomial parametrization and the divisor search overlap, but neither one should be viewed as a literal substitute for the other. Obviously, k = 4 ​ γ + 3 k=4\gamma+3, a = α + 1 a=\alpha+1, and b = 1 b=1 are admissible parameters for n = p ⁡ ( α, β, γ) n=p(\alpha,\beta,\gamma).

## 4 A fab \fabop -Type Framework for the Sierpiński–Schinzel Case

The fab \fabop construction for the Erdős–Straus equation is naturally formulated in terms of decompositions of 1 / n 1/n whose denominators are all divisible by 4 4. From this point of view, the appropriate analogue for the numerator 5 5 problem is obtained by considering decompositions

 | 1 n = 1 X + 1 Y + 1 Z, 5 ∣ X, 5 ∣ Y, 5 ∣ Z, \frac{1}{n}=\frac{1}{X}+\frac{1}{Y}+\frac{1}{Z},\qquad 5\mid X,\quad 5\mid Y,\quad 5\mid Z, |  |

since, after writing

 | X = 5 ​ x, Y = 5 ​ y, Z = 5 ​ z, X=5x,\qquad Y=5y,\qquad Z=5z, |  |

one immediately recovers an Egyptian decomposition of

 | 5 n = 1 x + 1 y + 1 z. \frac{5}{n}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}. |  |

Thus, the numerator 5 5 case can be studied through a parametrization of those decompositions of 1 / n 1/n in which the three denominators are multiples of 5 5.

As in the Erdős–Straus situation, the residue class that deserves special attention is the one for which no uniform elementary decomposition is available. In the present setting, the cases n ≡ 0, 2, 3, 4 ( mod 5) n\equiv 0,2,3,4\pmod{5} admit straightforward decompositions into three unit fractions, whereas the genuinely difficult class is

 | n ≡ 1 ( mod 5). n\equiv 1\pmod{5}. |  |

This is the exact analogue of the residue class n ≡ 1 ( mod 4) n\equiv 1\pmod{4} in the Erdős–Straus conjecture, and it is therefore the natural setting in which to introduce a fab \mathrm{fab} -type device.

For n ≡ 1 ( mod 5) n\equiv 1\pmod{5}, the first denominator in the relevant identity will be of the form n + k n+k. In order to force this denominator to be divisible by 5 5, one must impose

 | k ≡ 4 ( mod 5). k\equiv 4\pmod{5}. |  |

This leads to the following definition.

###### Definition 12.

Let n ≡ 1 ( mod 5) n\equiv 1\pmod{5}, and let a, b ∈ ℕ a,b\in\mathbb{N}. We define fabfive ⁡ ( n, a, b) \fabfiveop(n,a,b) to be the small divisor k k of a + b ​ n a+bn such that

 | k ≡ 4 ( mod 5), 5 b ∣ a + b ​ n k ( n + k), 5 a ∣ n a + b ​ n k ( n + k), k\equiv 4\pmod{5},\qquad 5b\mid\frac{a+bn}{k}(n+k),\qquad 5a\mid n\,\frac{a+bn}{k}(n+k), |  |

provided such a divisor exists. If no such divisor exists, we set

 | fabfive ⁡ ( n, a, b) = 0. \fabfiveop(n,a,b)=0. |  |

Viewing the problem as one of representing the fraction as a sum of three unit fractions shows that many of the results established for decompositions with denominators divisible by 4 4 can be extended without difficulty to denominators divisible by other values. In particular, in the case of denominators divisible by 5 5, the analogues of Proposition 2 and Theorem 5 are the following results which can be proved identically to the corresponding results.

###### Proposition 13.

Assume that n ≡ 1 ( mod 5) n\equiv 1\pmod{5} and that fabfive ⁡ ( n, a, b) = k > 0 \fabfiveop(n,a,b)=k>0. If

 | q = a + b ​ n k, q=\frac{a+bn}{k}, |  |

then

 | 1 n = 1 n + k + 1 q ⁡ ( n + k) / b + 1 n ​ q ​ ( n + k) / a. \frac{1}{n}=\frac{1}{n+k}+\frac{1}{\,q(n+k)/b\,}+\frac{1}{\,nq(n+k)/a\,}. |  | (21) |

Moreover, each of the three denominators

 | n + k, q ⁡ ( n + k) b, n ​ q ​ ( n + k) a n+k,\qquad\frac{q(n+k)}{b},\qquad\frac{nq(n+k)}{a} |  |

is divisible by 5 5. Consequently, one obtains a decomposition of 5 n \frac{5}{n} into three unit fractions.

###### Theorem 14 (Completeness of fabfive \fabfiveop).

Let n ≡ 1 ( mod 5) n\equiv 1\pmod{5}, and suppose that

 | 1 n = 1 X + 1 Y + 1 Z, 5 ∣ X, 5 ∣ Y, 5 ∣ Z. \frac{1}{n}=\frac{1}{X}+\frac{1}{Y}+\frac{1}{Z},\qquad 5\mid X,\quad 5\mid Y,\quad 5\mid Z. |  |

Then there exist a, b ∈ ℕ a,b\in\mathbb{N} and an admissible divisor k ≡ 4 ( mod 5) k\equiv 4\pmod{5} such that the divisor identity ( 21) associated with fabfive ⁡ ( n, a, b) \fabfiveop(n,a,b) reproduces exactly the given decomposition.

###### Remark 15 (The numerator 5 polynomial family).

It may be useful to record that the polynomial surface ( 18) behaves differently in the numerator 5 setting from the corresponding numerator 4 subfamily. The analogue leads instead to the congruence condition

 | v ≡ w ≡ 4 ( mod 5). v\equiv w\equiv 4\pmod{5}. |  |

This family has no analogous square obstruction. For instance,

 | P ⁡ ( 3, 14, 9) = 3 ⋅ 14 ⋅ 9 − 3 − 14 = 361 = 19 2. P(3,14,9)=3\cdot 14\cdot 9-3-14=361=19^{2}. |  |

Thus the polynomial family with v and w congruent to 4 modulo 5 already contains prime-square values.

Computationally, this family also appears to be very effective for primes in the difficult numerator 5 residue class. A finite sieve based on the identity

 | n + v = u ⁡ ( v ​ w − 1) n+v=u(vw-1) |  |

shows that, up to the tested bound, the primes congruent to 1 modulo 5 are almost always represented by

 | n = P ⁡ ( u, v, w), v ≡ w ≡ 4 ( mod 5). n=P(u,v,w),\qquad v\equiv w\equiv 4\pmod{5}. |  |

In the range tested up to 10 6, 10^{6}, the only missing primes are 541, 1381. 541,\,1381. This should be contrasted with the numerator 4 polynomial subfamily, where square values are excluded for structural reasons. The numerator 5 polynomial family therefore seems worth mentioning, not as a replacement for the fabfive ⁡ ( CLOSE \fabfiveop() framework, but as an additional comparison showing that the behaviour of P ⁡ ( u, v, w) P(u,v,w) depends strongly on the chosen congruence class. Observe that fabfive ⁡ ( 541, 1, 2) = 19 \fabfiveop(541,1,2)=19 and fabfive ⁡ ( 1381, 1, 2) = 9 \fabfiveop(1381,1,2)=9, which yields

 | 5 541 = 1 3453744 + 1 3192 + 1 112, \frac{5}{541}=\frac{1}{3453744}+\frac{1}{3192}+\frac{1}{112}, |  |

and

 | 5 1381 = 1 117862826 + 1 42673 + 1 278. \frac{5}{1381}=\frac{1}{117862826}+\frac{1}{42673}+\frac{1}{278}. |  |

Of course, k = 5 ​ γ + 4 k=5\gamma+4, a = α + 1 a=\alpha+1, and b = 1 b=1 are admissible parameters for n = P ⁡ ( α + 1, 5 ​ β + 4, 5 ​ γ + 4) n=P(\alpha+1,5\beta+4,5\gamma+4) according to the function fabfive ⁡ ( n, a, b) \fabfiveop(n,a,b).

Finally, the same parametrizing argument extends without essential change to a general numerator m ≥ 2 m\geq 2, provided one interprets the problem in terms of decompositions of 1 / n 1/n whose three denominators are all divisible by m m. In this setting, the congruence condition becomes

 | k ≡ − n ( mod m), k\equiv-n\pmod{m}, |  |

and the divisibility conditions are replaced by

 | m b ∣ a + b ​ n k ( n + k), m a ∣ n a + b ​ n k ( n + k). mb\mid\frac{a+bn}{k}(n+k),\qquad ma\mid n\,\frac{a+bn}{k}(n+k). |  |

Whenever such an admissible divisor k k exists, the associated identity produces a decomposition of 1 / n 1/n with all three denominators divisible by m m, and hence, after scaling, a decomposition of m / n m/n into three unit fractions.

Thus the cases m = 4, 5 m=4,5 are particular instances of a more general fab m \mathrm{fab}_{m} parametrization. However, the assertion that the only residue class requiring special attention is n ≡ 1 ( mod m) n\equiv 1\pmod{m} should not be made for arbitrary m m. For m = 4 m=4 and m = 5 m=5 the complementary residue classes are covered by elementary identities, and the same phenomenon also occurs for m = 6 m=6. For larger numerators, however, the elementary treatment of the complementary classes is no longer automatic: after subtracting the natural first unit fraction one is led to a two-term Egyptian decomposition of r / N r/N, with r r possibly larger than 4 4, and this imposes additional arithmetic conditions.

## 5 Further Comparisons

We finish by recording two links between the divisor identity used in this paper and related approaches to the Erdős–Straus conjecture. The purpose of this section is not to give a survey, but rather to clarify how our parametrization interacts with Bradford’s two-variable reduction and with Ventas’ source-based FCT construction.

### Bradford’s Reduction

Bradford ( [2] and [3]) observed that, once a solution is given, the third denominator is forced by the first two through a gcd identity: if p ≡ 1 p\equiv 1 (mod 4) is a prime,

 | 4 p = 1 x + 1 y + 1 z, x ≤ y ≤ z, \frac{4}{p}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z},\qquad x\leq y\leq z, |  |

then

 | z = x ​ y ​ p gcd ⁡ ( y, p) ​ gcd ⁡ ( x ​ y, x + y). z=\frac{xyp}{\gcd(y,p)\gcd(xy,x+y)}. |  | (22) |

By Theorem 5, we have

 | z = p ​ x ​ y a ​ g, a = k ​ y − p ​ x g, z=\frac{pxy}{ag},\quad a=\frac{ky-px}{g}, |  |

where g = gcd ⁡ ( x, y) g=\gcd(x,y). Then from Bradford’s identity ( 22) we obtain

 | a = gcd ⁡ ( y, p) ​ gcd ⁡ ( x ​ y, x + y) gcd ⁡ ( x, y) a=\frac{\gcd(y,p)\gcd(xy,x+y)}{\gcd(x,y)} |  | (23) |

and

 | D = gcd ⁡ ( y, p) ​ gcd ⁡ ( x ​ y, x + y), D=\gcd(y,p)\gcd(xy,x+y), |  | (24) |

In view of the symmetry between the formulations for 4 / n 4/n and 5 / n 5/n (see Proposition 13 and Theorem 14), it is natural to expect the following analogue.

###### Theorem 16 (Bradford’s defect and the canonical fabfive \fabfiveop parameters).

Let p ≡ 1 ( mod 5) p\equiv 1\pmod{5} be prime, and let

 | 5 p = 1 x + 1 y + 1 z, x ≤ y ≤ z, \frac{5}{p}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z},\qquad x\leq y\leq z, |  | (25) |

be a solution. Put D 5 = 5 ​ x ​ y − p ⁡ ( x + y). D_{5}=5xy-p(x+y). Then

 | z = x ​ y ​ p gcd ⁡ ( y, p) ​ gcd ⁡ ( x ​ y, x + y). z=\frac{xyp}{\gcd(y,p)\gcd(xy,x+y)}. |  | (26) |

Therefore

 | D 5 = gcd ⁡ ( y, p) ​ gcd ⁡ ( x ​ y, x + y), D_{5}=\gcd(y,p)\gcd(xy,x+y), |  | (27) |

and the parameter a a in the fabfive \fabfiveop function is given by

 | a = gcd ⁡ ( y, p) ​ gcd ⁡ ( x ​ y, x + y) gcd ⁡ ( x, y). a=\frac{\gcd(y,p)\gcd(xy,x+y)}{\gcd(x,y)}. |  | (28) |

###### Proof.

By ( 25) we have

 | D 5 ​ z = p ​ x ​ y. D_{5}z=pxy. |  | (29) |

In particular, D 5 | p ​ x ​ y D_{5}\mid pxy. Set α = gcd ⁡ ( D 5, p) \alpha=\gcd(D_{5},p). As p p is a prime, α = 1 \alpha=1 or p p. If p | D 5 p\mid D_{5}, as p > 5 p>5, we have p | x p\mid x or p | y p\mid y. Since x ≤ y ≤ z x\leq y\leq z, the former condition and ( 25) yield a contradiction. Thus, if p | D 5 p\mid D_{5}, p ∤ x p\nmid x and p | y p\mid y. Therefore,

 | α = gcd ⁡ ( D 5, p) = gcd ⁡ ( y, p). \alpha=\gcd(D_{5},p)=\gcd(y,p). |  |

As D 5 | p ​ x ​ y D_{5}\mid pxy, we get

 | D 5 α | gcd ⁡ ( x ​ y, x + y). \frac{D_{5}}{\alpha}\mid\gcd(xy,x+y). |  | (30) |

Let us prove the reverse divisibility. Obviously,

 | gcd ⁡ ( x ​ y, x + y) | D 5. \gcd(xy,x+y)\mid D_{5}. |  |

We have proved that if α = p \alpha=p, then p ∤ x p\nmid x and p | y p\mid y. So p ∤ x + y p\nmid x+y and p ∤ gcd ⁡ ( x ​ y, x + y) p\nmid\gcd(xy,x+y). Thus,

 | α | D 5 \alpha\mid D_{5} |  |

Hence, we obtain

 | α ​ gcd ⁡ ( x ​ y, x + y) | D 5. \alpha\gcd(xy,x+y)\mid D_{5}. |  | (31) |

Therefore, combining ( 30) and ( 31) we get ( 27)

 | D 5 = α ​ gcd ⁡ ( x ​ y, x + y) = gcd ⁡ ( y, p) ​ gcd ⁡ ( x ​ y, x + y). D_{5}=\alpha\gcd(xy,x+y)=\gcd(y,p)\gcd(xy,x+y). |  |

This equation, together ( 29) shows ( 26).

The same argument as in the proof of Theorem 5, applied to the fabfive \fabfiveop parametrization, gives

 | z = p ​ x ​ y a ​ g, z=\frac{pxy}{ag}, |  |

and ( 28) follows. ∎

### Ventas’ FCT Sources

Ventas’ ceiling continued fraction construction (FCT, see [11]) can also be interpreted inside the same divisor framework. His source theorem assumes a divisor d ≡ 3 ( mod 4) d\equiv 3\pmod{4} of an external source p + i p+i, together with the divisibility condition 4 ​ i | p + d 4i\mid p+d. This is exactly a sufficient condition for a certificate in the layer b = 1 b=1 of our construction.

###### Proposition 17 (FCT sources as fab \fabop certificates).

Let p ≡ 1 ( mod 4) p\equiv 1\pmod{4} be prime. Suppose that there exist i, d ∈ ℕ i,d\in\mathbb{N} such that

 | d ∣ p + i, d ≡ 3 ( mod 4), 4 i ∣ p + d. d\mid p+i,\qquad d\equiv 3\pmod{4},\qquad 4i\mid p+d. |  |

Then d d is an admissible divisor for fab ⁡ ( p, i, 1) \fabop(p,i,1). If q = ( p + i) / d q=(p+i)/d, the corresponding identity is

 | 1 p = 1 p + d + 1 q ⁡ ( p + d) + 1 p ​ q ​ ( p + d) / i, \frac{1}{p}=\frac{1}{p+d}+\frac{1}{q(p+d)}+\frac{1}{pq(p+d)/i}, |  |

and, after division of the three denominators by 4 4, it gives

 | 4 p = 1 x + 1 y + 1 z, \frac{4}{p}=\frac{1}{x}+\frac{1}{y}+\frac{1}{z}, |  |

where

 | x = p + d 4, y = ( p + d) ​ ( p + i) 4 ​ d, z = p ​ ( p + d) ​ ( p + i) 4 ​ i ​ d. x=\frac{p+d}{4},\qquad y=\frac{(p+d)(p+i)}{4d},\qquad z=\frac{p(p+d)(p+i)}{4id}. |  |

###### Proof.

The conditions d | p + i d\mid p+i and d ≡ 3 ( mod 4) d\equiv 3\pmod{4} give the divisor and congruence requirements. With q = ( p + i) / d q=(p+i)/d, the hypothesis 4 ​ i | p + d 4i\mid p+d implies

 | 4 ∣ q ( p + d), 4 i ∣ p q ( p + d). 4\mid q(p+d),\qquad 4i\mid pq(p+d). |  |

These are precisely the remaining admissibility conditions for fab ⁡ ( p, i, 1) > 0 \fabop(p,i,1)>0. The displayed identity is the divisor identity for a = i a=i, b = 1 b=1, and k = d k=d. ∎

###### Remark 18.

Thus Ventas’ condition is naturally contained in the b = 1 b=1 layer of fab \fabop. Conversely, fab ⁡ ( p, i, 1) \fabop(p,i,1) is slightly more flexible: it only requires

 | 4 ∣ q ( p + k), 4 i ∣ p q ( p + k), q = p + i k, 4\mid q(p+k),\qquad 4i\mid pq(p+k),\qquad q=\frac{p+i}{k}, |  |

so the factor q q may also contribute to the required divisibility.

There is also a geometric overlap. If an FCT solution has coefficients ⌈ c 0, c 1, c 2 ⌉ \lceil c_{0},c_{1},c_{2}\rceil and final numerator p p, the negative recurrence gives

 | p = ( c 1 ​ c 2 − 1) ​ c 0 − c 2 = c 0 ​ c 1 ​ c 2 − c 0 − c 2. p=(c_{1}c_{2}-1)c_{0}-c_{2}=c_{0}c_{1}c_{2}-c_{0}-c_{2}. |  |

Hence, for P ⁡ ( u, v, w) = u ​ v ​ w − u − v P(u,v,w)=uvw-u-v,

 | p = P ⁡ ( c 2, c 0, c 1), p=P(c_{2},c_{0},c_{1}), |  |

so the FCT grid lies on the same cubic surface, up to a permutation of variables.

These two comparisons indicate that the divisor identity is not merely another parametrization, but a convenient common language in which several apparently different constructions can be expressed.

###### Remark 19.

We observe that the preceding result carries over without difficulty to the setting of Sierpiński’s conjecture. Indeed, for those values n ≡ 1 ( mod 5) n\equiv 1\pmod{5} arising from the polynomial surface

 | P ⁡ ( u, v, w) = u ​ v ​ w − u − v, P(u,v,w)=uvw-u-v, |  |

with v, w ≡ 4 ( mod 5) v,w\equiv 4\pmod{5}, the fractions 5 / n 5/n also admit representations as sums of three unit fractions.

## 6 Translation Invariance, Modular Sieving, and Computation

The choice function fab \fabop has a simple translation invariance that is useful in modular sieving.

###### Proposition 20 (Translation invariance).

Suppose fab ⁡ ( n, a, b) = k > 0 \fabop(n,a,b)=k>0 and put

 | n 1 = n + 4 ​ a ​ b ​ k. n_{1}=n+4abk. |  |

Then the same k k remains an admissible divisor for the congruence and divisibility tests defining fab ⁡ ( n 1, a, b) \fabop(n_{1},a,b).

###### Proof.

Since k | a + b ​ n k\mid a+bn, one has

 | a + b ​ n 1 = a + b ​ n + 4 ​ a ​ b 2 ​ k, a+bn_{1}=a+bn+4ab^{2}k, |  |

so k | a + b ​ n 1 k\mid a+bn_{1}. Moreover

 | a + b ​ n 1 k = a + b ​ n k + 4 ​ a ​ b 2, n 1 + k = n + k + 4 ​ a ​ b ​ k. \frac{a+bn_{1}}{k}=\frac{a+bn}{k}+4ab^{2},\qquad n_{1}+k=n+k+4abk. |  |

Thus the defining congruence tests are preserved. ∎

As an immediate consequence of the translation invariance, one obtains the following modular sieving algorithm, which is useful for bounded modular sieving.

###### Remark 21 (Modular sieving).

Proposition 20 gives a practical way to organize the bounded search. For a fixed bound C C, one may work modulo a convenient modulus m m and remove a residue class r ( mod m) r\pmod{m} as soon as a certificate

 | fab ( r, a, b) = k > 0, 1 ≤ a, b ≤ C, 4 a b k ∣ m \fabop(r,a,b)=k>0,\qquad 1\leq a,b\leq C,\qquad 4abk\mid m |  |

is found. The remaining residue classes are the only classes that still need to be explored when looking for values not detected by the bounded window 1 ≤ a, b ≤ C 1\leq a,b\leq C. If m 0 | m m_{0}\mid m, survivor classes modulo m 0 m_{0} can be lifted to classes modulo m m by testing the finitely many residues

 | r + ℓ ​ m 0 ( mod m), 0 ≤ ℓ < m / m 0. r+\ell m_{0}\pmod{m},\qquad 0\leq\ell<m/m_{0}. |  |

This is the modular principle behind the computational sieve used below.

###### Remark 22 (Modular inverse role).

Suppose that a a and b b are coprime to k ≡ 3 ( mod 4) k\equiv 3\pmod{4}. Let a ¯ \overline{a} and b ¯ \overline{b} be such that a ​ a ¯ ≡ 1 a\overline{a}\equiv 1 and b ​ b ¯ ≡ 1 b\overline{b}\equiv 1 (mod k k). The condition k | a + b ​ n k\mid a+bn is equivalent to

 | n ≡ − a ​ b ¯ ( mod k), n\equiv-a\overline{b}\pmod{k}, |  |

that is, k | b ¯ + a ¯ ​ n k\mid\overline{b}+\overline{a}n. Thus, when considering the divisors k ≡ 3 ( mod 4) k\equiv 3\pmod{4} of a + b ​ n a+bn, it is not only natural to ask whether ( 3) holds for such a k k, but also whether

 | 4 a ¯ ∣ b ¯ + a ¯ ​ n k ( n + k), 4 b ¯ ∣ n b ¯ + a ¯ ​ n k ( n + k). 4\overline{a}\mid\frac{\overline{b}+\overline{a}n}{k}(n+k),\qquad 4\overline{b}\mid n\frac{\overline{b}+\overline{a}n}{k}(n+k). |  |

If k | a + b ​ n k\mid a+bn, but either

 | 4 ​ a ∤ a + b ​ n k ​ ( n + k) or 4 ​ b ∤ a + b ​ n k ​ ( n + k) ​ n, 4a\nmid\frac{a+bn}{k}(n+k)\qquad\text{or}\qquad 4b\nmid\frac{a+bn}{k}(n+k)n, |  |

then one may try to shift the values of a a and b b by suitable multiples of k k, while preserving the congruence k | a + b ​ n k\mid a+bn, in order to make both divisibility conditions hold. For large n n, this approach appears to provide a promising strategy for finding admissible triples ( a, b, k) (a,b,k) associated with a given value of n n.

###### Remark 23 (Composite exceptional values for the bounded search).

The bounded search for composite n ≡ 1 ( mod 4) n\equiv 1\pmod{4} analogous to Remark 9 behaves differently. If one restricts Definition 1 to the window 1 ≤ a, b ≤ 11 1\leq a,b\leq 11, then some composite values are not detected in that window, although they are detected as soon as one allows one of the parameters to be slightly larger. The only numbers, which are not square, that require a a or b b greater than 11 up to 10 14 10^{14} appear in Table 1. Here comab ⁡ ( n) = ( a, b, k) \operatorname{comab}(n)=(a,b,k) means that k, a, b k,a,b are admissible values for n n.

n n | small factor of n n | comab ⁡ ( n) \operatorname{comab}(n) |

68889266161 68889266161 | 43969 43969 | ( 12, 1, 2639) (12,1,2639) |

198670395169 198670395169 | 38791 38791 | ( 1, 13, 1171) (1,13,1171) |

2081413401769 2081413401769 | 13 13 | ( 5, 12, 189415991) (5,12,189415991) |

32140320080401 32140320080401 | 13 13 | ( 13, 1, 7) (13,1,7) |

42042659579881 42042659579881 | 1699 1699 | ( 7, 15, 770953415279) (7,15,770953415279) |

58797131752129 58797131752129 | 19 19 | ( 7, 12, 25015620671) (7,12,25015620671) |

87574118340241 87574118340241 | 13 13 | ( 13, 1, 7) (13,1,7) |

Table 1: This table lists the only nonsquare integers n ≤ 10 14 n\leq 10^{14} for which fab ⁡ ( n, a, b) \fabop(n,a,b) requires parameters a, b a,b outside the window max ⁡ { a, b } ≤ 11 \max\{a,b\}\leq 11.

These examples do not contradict the prime computation, since they are composite rather than prime. They suggest, however, that the small window 1 ≤ a, b ≤ 11 1\leq a,b\leq 11 should be regarded as a phenomenon of the prime search, not as a uniform bound for all composite integers.

###### Remark 24 (Greedy survivor sequences).

The translation-invariant sieve gives rise to natural greedy survivor sequences. Starting from the single sieve value k = 3 k=3, one repeatedly takes the least prime, or composite, not detected by the current finite sieve and then adjoins the least new admissible k ≡ 3 ( mod 4) k\equiv 3\pmod{4} which detects it. The first prime survivors are

 | 73, 1129, 1201, 3361, 5569, 9241, 14401, …, 73,1129,1201,3361,5569,9241,14401,\ldots, |  |

whereas the first composite survivors, with the prime-square rule a = p a=p for n = p 2 n=p^{2}, are

 | 49, 1369, 1849, 2641, 5161, 6241, 11089, …. 49,1369,1849,2641,5161,6241,11089,\ldots. |  |

The largest prime survivor below 10 7 10^{7} found in our computations is 8803369 8803369, which requires k = 107 k=107. These sequences seem to encode the early growth of the modular sieve associated with fab \fabop.

###### Remark 25.

Using the choice function fabfive ⁡ ( n, a, b) \fabfiveop(n,a,b) to decompose 5 n \frac{5}{n}, we work within the window max ⁡ { a, b } ≤ 9 \max\{a,b\}\leq 9. The only integers up to 10 14 10^{14} that require values outside this window are in Table 2.

n n | smallest factor of n n | ( a, b) (a,b) |

305945641 305945641 | n n ( prime) | ( 10, 1) (10,1) |

2965123604521 2965123604521 | 13 13 | ( 2, 11) (2,11) |

7171425327781 7171425327781 | 11 11 | ( 11, 1) (11,1) |

2095120616401 2095120616401 | 739 739 | ( 10, 3) (10,3) |

4269339137701 4269339137701 | 11 11 | ( 11, 1) (11,1) |

11471606546401 11471606546401 | 37 37 | ( 10, 1) (10,1) |

45931894495201 45931894495201 | 11 11 | ( 1, 10) (1,10) |

63712786956841 63712786956841 | 11 11 | ( 1, 10) (1,10) |

80611085041201 80611085041201 | 11 11 | ( 10, 3) (10,3) |

Table 2: This table lists the only integers n ≤ 10 14 n\leq 10^{14} for which fabfive ⁡ ( n, a, b) \fabfiveop(n,a,b) requires a choice of parameters a, b a,b outside the window max ⁡ { a, b } ≤ 9 \max\{a,b\}\leq 9.

All computations reported in Remarks 9, 23, 24, and 25 were performed by an independent implementation of the admissibility conditions in Definition 1; the code is available from the authors upon request.

## Acknowledgments and AI Tool Disclosure.

Research of M. B-H. is supported in part by the grant PID2022–138342NB–I00 AEI, from Spanish Government.

ChatGPT 5.5 was used for proofreading. Outside of this AI tool use, the mathematics and the text of this paper were both human-generated.

## References

- [1] M. Bello-Hernández, M. Benito and E. Fernández, On Egyptian fractions, arXiv:1010.2035v2, (2012).
- [2] K. Bradford, A Note on the Erdős–Straus Conjecture, Integers 21 (2021), #A24, 10 pp.
- [3] K. Bradford, Elementary patterns from the Erdős–Straus conjecture, Integers 25 (2025), #A54 10 pp.
- [4] C. Elsholtz and T. Tao, Counting the number of solutions to the Erdős–Straus equation on unit fractions, J. Aust. Math. Soc. 94 (2013), 50–105.
- [5] P. Erdős, Az 1 x 1 + 1 x 2 + … + 1 x n = a b \frac{1}{x_{1}}+\frac{1}{x_{2}}+\ldots+\frac{1}{x_{n}}=\frac{a}{b} egyenlet egész számú megoldásairol. Mat. Lapok 1 (1950), 192–210.
- [6] L. K. Hua, *Introduction to Number Theory*, Springer, 1982.
- [7] J. Huang and R. C. Vaughan, Mean value theorems for binary Egyptian fractions. J. Number Theory 131 (2011), 1641–1656.
- [8] L. J. Mordell, *Diophantine Equations*, Academic Press, 1969.
- [9] A. Schinzel, On sums of three unit fractions with polynomial denominators, Funct. Approx. Comment. Math. 28 (2000), 187–194.
- [10] R. C. Vaughan, On a problem of Erdős, Straus, and Schinzel, Mathematika 17 (1970), 193–198.
- [11] A. Ventas, A ceiling continued fraction approach to the Erdős–Straus conjecture: Heuristic finiteness of counterexamples, arXiv:2605.04551v1, (2026).
- [12] K. Yamamoto, On the Diophantine equation 4 / n = 1 / x + 1 / y + 1 / z 4/n=1/x+1/y+1/z, Mem. Fac. Sci. Kyushu Univ. Ser. A 19 (1965), 37–47.

M. Bello-Hernández, corresponding author. Departamento de Matemáticas y Computación, Universidad de La Rioja. c/ Madre de Dios, 53, 26006 Logroño, La Rioja, Spain. Research supported in part by the grant PID2022–138342NB–I00 AEI, from Spanish Government.
mbello@unirioja.es

M. Benito, retired Professor. Instituto P. M. Sagasta, Logroño and Departamento de Matemáticas y Computación, Universidad de La Rioja. c/ Madre de Dios, 53, 26006 Logroño, La Rioja, Spain.
mbenitomunnoz@gmail.com

E. Fernández, retired Professor. Instituto P. M. Sagasta, Logroño and Departamento de Matemáticas y Computación, Universidad de La Rioja. c/ Madre de Dios, 53, 26006 Logroño, La Rioja, Spain.
emilio.fernandez@unirioja.es


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
