<!-- source: https://arxiv.org/html/2107.08308v1 | converted from HTML -->

Reciprocity Relations for Summations of Squares of Floor Functions and Fractional Parts of Fractions

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2107.08308v1 [math.NT] 17 Jul 2021

# Reciprocity Relations for Summations of Squares of Floor Functions and Fractional Parts of Fractions

Damanvir Singh Binner
Department of Mathematics
Simon Fraser University
Burnaby, BC V5A 1S6
Canada
dbinner@sfu.ca

###### Abstract

Given positive coprime integers a a and b b and a natural number h h, we obtain reciprocity relations which can be used to quickly evaluate summations like ∑ i = 1 h { i ​ b a } 2 \sum_{i=1}^{h}\{\frac{ib}{a}\}^{2} and ∑ i = 1 h ⌊ i ​ b a ⌋ 2 \sum_{i=1}^{h}\lfloor\frac{ib}{a}\rfloor^{2}, where ⌊ x ⌋ \lfloor x\rfloor and { x } \{x\} denote the floor function and the fractional part of x x, respectively.

## 1 Introduction

We introduce the following notation.

- •

T 1 ​ ( a, b, h):= ∑ i = 1 h { i ​ b a } 2 T_{1}(a,b;h):=\sum_{i=1}^{h}\{\frac{ib}{a}\}^{2}.

- •

T 2 ​ ( a, b, h):= ∑ i = 1 h i ⁡ ⌊ i ​ b a ⌋ T_{2}(a,b;h):=\sum_{i=1}^{h}i\lfloor\frac{ib}{a}\rfloor.

- •

T 3 ​ ( a, b, h):= ∑ i = 1 h ⌊ i ​ b a ⌋ 2 T_{3}(a,b;h):=\sum_{i=1}^{h}\lfloor\frac{ib}{a}\rfloor^{2}.

We can reformulate these sums as follows. Let q i q_{i} and r i r_{i} denote the quotient and remainder when i ​ b ib is divided by a a. Then

 | T 1 ​ ( a, b, h) \displaystyle T_{1}(a,b;h) | = 1 a 2 ​ ∑ i = 1 h r i 2, \displaystyle=\frac{1}{a^{2}}\sum_{i=1}^{h}r_{i}^{2}, |  |

 | T 2 ​ ( a, b, h) \displaystyle T_{2}(a,b;h) | = ∑ i = 1 h i ​ q i, \displaystyle=\sum_{i=1}^{h}iq_{i}, |  |

 | T 3 ​ ( a, b, h) \displaystyle T_{3}(a,b;h) | = ∑ i = 1 h q i 2. \displaystyle=\sum_{i=1}^{h}q_{i}^{2}. |  |

Note that summations like ∑ i = 1 h i ​ r i \sum_{i=1}^{h}ir_{i} and ∑ i = 1 h q i ​ r i \sum_{i=1}^{h}q_{i}r_{i} can be easily expressed in terms of these sums using the division algorithm. We remark in passing that in 2020 2020, the present author described a reciprocity relation which can be used to quickly calculate ∑ i = 1 h q i \sum_{i=1}^{h}q_{i} and ∑ i = 1 h r i \sum_{i=1}^{h}r_{i} (see [1, Lemma 7]). This reciprocity relationship is also described in Theorem 3 below.

In Section 2, we derive reciprocity relations for T 1 ​ ( a, b, h) T_{1}(a,b;h). Using these, we then obtain a reciprocity relation for T 2 ​ ( a, b, h) T_{2}(a,b;h) in Section 3. These reciprocity relations help us to easily calculate T 1 ​ ( a, b, h) T_{1}(a,b;h) and T 2 ​ ( a, b, h) T_{2}(a,b;h). In Section 4, we show that T 1 ​ ( a, b, h) T_{1}(a,b;h) and T 2 ​ ( a, b, h) T_{2}(a,b;h) can be calculated in O ⁡ ( log ⁡ t) O(\log t) and O ⁡ ( ( log ⁡ t) 2) O((\log t)^{2}) steps, where t = max ⁡ ( a, b) t=\max(a,b) and by a step, we mean a basic arithmetic operation on the bits of a a and b b. Further we show that T 3 ​ ( a, b, h) T_{3}(a,b;h) can be easily calculated using the values of T 1 ​ ( a, b, h) T_{1}(a,b;h) and T 2 ​ ( a, b, h) T_{2}(a,b;h). In Sections 2.2 and 3.2, we demonstrate our formulas for an example. Let q i q_{i} and r i r_{i} denote the quotients and remainders when 2732 ​ i 2732\hskip 1.42271pti is divided by 8411 8411. By performing only a few steps, we show that

 | ∑ i = 1 1221 r i 2 \displaystyle\sum_{i=1}^{1221}r_{i}^{2} | = 28850219593, \displaystyle=28850219593, |  |

 | ∑ i = 1 1221 i ​ q i \displaystyle\sum_{i=1}^{1221}iq_{i} | = 196956430, \displaystyle=196956430, |  |

 | ∑ i = 1 1221 q i 2 \displaystyle\sum_{i=1}^{1221}q_{i}^{2} | = 63853169. \displaystyle=63853169. |  |

We require three main results. The first one is the following well-known result of Sylvester.

###### Theorem 1 (Sylvester (1882)).

If a a and b b are positive coprime numbers, the number of natural numbers that cannot be expressed in the form a ​ x + b ​ y ax+by for nonnegative integers x x and y y is equal to ( a − 1) ​ ( b − 1) 2 \frac{(a-1)(b-1)}{2}.

This result can be found in [3]. Moreover, Sylvester posed this as a recreational problem, and Curran [4] published a short proof based on generating functions.

Let N ​ R ​ ( a, b) NR(a,b) denotes the set of nonnegative integers nonrepresentable in terms of a a and b b. That is, N ​ R ​ ( a, b) NR(a,b) is the set of nonnegative integers n n that cannot be expressed in the form a ​ x + b ​ y ax+by. Then, by Theorem 1, | N ​ R ​ ( a, b) | = ( a − 1) ​ ( b − 1) 2 |NR(a,b)|=\frac{(a-1)(b-1)}{2}. In 1993 1993, Brown and Shiue [2] discovered the sum S ⁡ ( a, b) S(a,b) of natural numbers that cannot be expressed in the form a ​ x + b ​ y ax+by.

###### Theorem 2 (Brown and Shiue (1993)).

For positive coprime numbers a a and b b,

 | S ⁡ ( a, b):= ∑ n ∈ N ​ R ​ ( a, b) n = 1 12 ​ ( a − 1) ​ ( b − 1) ​ ( 2 ​ a ​ b − a − b − 1). S(a,b):=\sum_{n\in NR(a,b)}n=\frac{1}{12}(a-1)(b-1)(2ab-a-b-1). |  |

For various calculations involved in our examples, we need the following reciprocity relationship proved by the present author in 2020 2020.

###### Theorem 3 (Binner(2020)).

Let a a, b b, d d, and K K be positive integers such that b < a b<a, d < a d<a, gcd ⁡ ( a, b) = 1 \gcd(a,b)=1, and K = ⌊ b ​ d a ⌋ K=\left\lfloor\frac{bd}{a}\right\rfloor. Then

 | ∑ i = 1 d ⌊ i ​ b a ⌋ + ∑ i = 1 K ⌊ i ​ a b ⌋ = d ​ K. \sum_{i=1}^{d}\left\lfloor\frac{ib}{a}\right\rfloor+\sum_{i=1}^{K}\left\lfloor\frac{ia}{b}\right\rfloor=dK. |  |

## 2 An algorithm for T 1 ​ ( a, b, h) T_{1}(a,b;h)

In this section, we derive reciprocity relations which can be used to calculate T 1 ​ ( a, b, h) T_{1}(a,b;h).

### 2.1 Reciprocity relation

Define

 | S ⁡ ( a, b, h):= ( a 2) ​ T 1 ​ ( a, b, h) + ( a 2 + 1) ​ ∑ i = 1 h ⌊ i ​ b a ⌋. S(a,b;h):=\left(\frac{a}{2}\right)T_{1}(a,b;h)+\left(\frac{a}{2}+1\right)\sum_{i=1}^{h}\left\lfloor\frac{ib}{a}\right\rfloor. |  |

We describe reciprocity relations for S ⁡ ( a, b, h) S(a,b;h). This leads to a method to quickly calculate T 1 ​ ( a, b, h) T_{1}(a,b;h) because ∑ i = 1 h ⌊ i ​ b a ⌋ \sum_{i=1}^{h}\left\lfloor\frac{ib}{a}\right\rfloor can be easily calculated using the algorithm described in [1, Section 2.3]. We need some more notation.

- •

n 0 n_{0} is the remainder obtained upon dividing − b ⁡ ( h + 1) -b(h+1) by a a.

- •

n:= a ​ b − a + n 0 n:=ab-a+n_{0}. Note that a ​ b − a ≤ n < a ​ b ab-a\leq n<ab.

- •

H:= n 1 − 1 H:=n_{1}-1, where n 1 n_{1} is the remainder when − n ​ a − 1 -na^{-1} is divided by b b.

Our approach is to calculate the number of nonnegative integer solutions ( x, y, z, u) (x,y,z,u) of the equation a ​ x + b ​ y + z + u = n ax+by+z+u=n in two different ways. First, we use Theorems 1 and 2 to find the number of solutions of this equation.

###### Lemma 4.

The number of nonnegative integer solutions of the equation a ​ x + b ​ y + z + u = n ax+by+z+u=n is given by

 | ( n + 1) ​ ( n + 2) 2 + ( a − 1) ​ ( b − 1) 12 ​ ( 2 ​ a ​ b − a − b − 6 ​ n − 7). \frac{(n+1)(n+2)}{2}+\frac{(a-1)(b-1)}{12}(2ab-a-b-6n-7). |  |

###### Proof.

It is well-known that the equation a ​ x + b ​ y = n ax+by=n has either 0 0 or 1 1 solutions if n < a ​ b n<ab (see [5, Lemma 2 and Lemma 4]). We view the equation a ​ x + b ​ y + z + u = n ax+by+z+u=n as the pair of equations a ​ x + b ​ y = i ax+by=i and z + u = n − i z+u=n-i, as i i varies from 0 0 to n n. Note that the former equation has a solution only if i ∉ N ​ R ​ ( a, b) i\not\in NR(a,b). Then the required number of solutions of the equation a ​ x + b ​ y + z + u = n ax+by+z+u=n is given by

 | ∑ i = 0, i ∉ N ​ R ​ ( a, b) n ( n + 1 − i). \sum_{\begin{subarray}{c}i=0,\\ i\not\in NR(a,b)\end{subarray}}^{n}(n+1-i). |  |

Using Theorems 1 and 2 and simplifying, we get that

 |  | ∑ i = 0, i ∉ N ​ R ​ ( a, b) n ( n + 1 − i) \displaystyle\sum_{\begin{subarray}{c}i=0,\\ i\not\in NR(a,b)\end{subarray}}^{n}(n+1-i) |  |

 |  | = ∑ i = 0 n ( n + 1 − i) − ∑ i ∈ N ​ R ​ ( a, b) ( n + 1 − i) \displaystyle=\sum_{i=0}^{n}(n+1-i)-\sum_{i\in NR(a,b)}(n+1-i) |  |

 |  | = ( n + 1) ​ ( n + 2) 2 − ( n + 1) ​ | N ​ R ​ ( a, b) | + ∑ i ∈ N ​ R ​ ( a, b) i \displaystyle=\frac{(n+1)(n+2)}{2}-(n+1)|NR(a,b)|+\sum_{i\in NR(a,b)}i |  |

 |  | = ( n + 1) ​ ( n + 2) 2 − ( n + 1) ​ ( a − 1) ​ ( b − 1) 2 + 1 12 ​ ( a − 1) ​ ( b − 1) ​ ( 2 ​ a ​ b − a − b − 1) \displaystyle=\frac{(n+1)(n+2)}{2}-(n+1)\frac{(a-1)(b-1)}{2}+\frac{1}{12}(a-1)(b-1)(2ab-a-b-1) |  |

 |  | = ( n + 1) ​ ( n + 2) 2 + ( a − 1) ​ ( b − 1) 12 ​ ( 2 ​ a ​ b − a − b − 6 ​ n − 7). \displaystyle=\frac{(n+1)(n+2)}{2}+\frac{(a-1)(b-1)}{12}(2ab-a-b-6n-7). |  |

∎

Next, we find the number of solutions of this equation using the method of generating functions. Though our method is similar in spirit to the proof of [1, Theorem 5], there are several key differences and we provide all the details here for the sake of completeness. We require some more notation.

 |  | α ⁡ ( a, b):= a ​ b ​ ( a + b − 2) 2, \displaystyle\alpha(a,b):=\frac{ab(a+b-2)}{2}, |  |

 |  | β ⁡ ( a, b):= a ​ b ​ ( a − 1) ​ ( b − 1) 2 + a ​ b ​ ( ( a − 1) ​ ( a − 2) + ( b − 1) ​ ( b − 2)) 3, \displaystyle\beta(a,b):=\frac{ab(a-1)(b-1)}{2}+\frac{ab\left((a-1)(a-2)+(b-1)(b-2)\right)}{3}, |  |

 |  | γ ⁡ ( a, b):= 2 ​ α 2 ​ ( a, b) − a ​ b ​ β ​ ( a, b) 2 ​ ( a ​ b) 3, \displaystyle\gamma(a,b):=\frac{2\alpha^{2}(a,b)-ab\beta(a,b)}{2(ab)^{3}}, |  |

 |  | η 1 ​ ( a, b, h):= ( h + H + 1) + n ​ γ ​ ( a, b) + n ⁡ ( n + 3) 2 ​ ( a + b − 2 2 ​ a ​ b) + n 3 + 6 ​ n 2 + 11 ​ n 6 ​ a ​ b \displaystyle\eta_{1}(a,b,h):=(h+H+1)+n\gamma(a,b)+\frac{n(n+3)}{2}\left(\frac{a+b-2}{2ab}\right)+\frac{n^{3}+6n^{2}+11n}{6ab} |  |

 |  | + ( h + 1) ​ ( a − 1) ​ ( a − 5) 12 ​ a + ( H + 1) ​ ( b − 1) ​ ( b − 5) 12 ​ b − b ​ h ​ ( h + 1) ​ ( a + 2) 4 ​ a − a ​ H ​ ( H + 1) ​ ( b + 2) 4 ​ b. \displaystyle+\frac{(h+1)(a-1)(a-5)}{12a}+\frac{(H+1)(b-1)(b-5)}{12b}-\frac{bh(h+1)(a+2)}{4a}-\frac{aH(H+1)(b+2)}{4b}. |  |

###### Lemma 5.

Let N N denote the number of nonnegative integer solutions of the equation a ​ x + b ​ y + z + u = n ax+by+z+u=n. Then

 | N = S ⁡ ( a, b, h) + S ⁡ ( b, a, H) + η 1 ​ ( a, b, h). N=S(a,b;h)+S(b,a;H)+\eta_{1}(a,b,h). |  |

###### Proof.

By elementary theory of generating functions, we know that N N is equal to the coefficient of x n x^{n} in

 | 1 ( 1 − x a) ​ ( 1 − x b) ​ ( 1 − x) 2. \frac{1}{(1-x^{a})(1-x^{b})(1-x)^{2}}. |  |

Let ζ m \zeta_{m} denote e 2 ​ π ​ i m e^{{\frac{2\pi i}{m}}}. We know that

 | ( 1 − x a) ​ ( 1 − x b) ​ ( 1 − x) 2 = ( 1 − x) 4 ​ ∏ k = 1 a − 1 ( 1 − ζ a − k ​ x) ​ ∏ k = 1 b − 1 ( 1 − ζ b − k ​ x). (1-x^{a})(1-x^{b})(1-x)^{2}=(1-x)^{4}\prod_{k=1}^{a-1}(1-\zeta_{a}^{-k}x)\prod_{k=1}^{b-1}(1-\zeta_{b}^{-k}x). |  |

Since a a and b b are coprime, 1 − ζ a − k ​ x 1-\zeta_{a}^{-k}x and 1 − ζ b − k ​ x 1-\zeta_{b}^{-k}x are distinct for all values of k k. Thus, we obtain the partial fraction decomposition

 | 1 ( 1 − x a) ​ ( 1 − x b) ​ ( 1 − x) 2 \displaystyle\frac{1}{(1-x^{a})(1-x^{b})(1-x)^{2}} | = d 1 1 − x + d 2 ( 1 − x) 2 + d 3 ( 1 − x) 3 + d 4 ( 1 − x) 4 \displaystyle=\frac{d_{1}}{1-x}+\frac{d_{2}}{(1-x)^{2}}+\frac{d_{3}}{(1-x)^{3}}+\frac{d_{4}}{(1-x)^{4}} |  | (1) |

 |  | + ∑ k = 1 a − 1 A k 1 − ζ a − k ​ x + ∑ k = 1 b − 1 B k 1 − ζ b − k ​ x. \displaystyle+\sum_{k=1}^{a-1}\frac{A_{k}}{1-\zeta_{a}^{-k}x}+\sum_{k=1}^{b-1}\frac{B_{k}}{1-\zeta_{b}^{-k}x}. |  |

On comparing the coefficients of x n x^{n} on both sides of ( 1), we find

 | N = d 1 + ( n + 1) ​ d 2 + ( n + 2) ​ ( n + 1) 2 ​ d 3 + ( n + 3) ​ ( n + 2) ​ ( n + 1) 6 ​ d 4 + ∑ k = 1 a − 1 A k ​ ζ a − n ​ k + ∑ k = 1 b − 1 B k ​ ζ b − n ​ k. N=d_{1}+(n+1)d_{2}+\frac{(n+2)(n+1)}{2}d_{3}+\frac{(n+3)(n+2)(n+1)}{6}d_{4}+\sum_{k=1}^{a-1}A_{k}\zeta_{a}^{-nk}+\sum_{k=1}^{b-1}B_{k}\zeta_{b}^{-nk}. |  | (2) |

If we substitute x = 0 x=0 in ( 1), we get

 | 1 = d 1 + d 2 + d 3 + d 4 + ∑ k = 1 a − 1 A k + ∑ k = 1 b − 1 B k. 1=d_{1}+d_{2}+d_{3}+d_{4}+\sum_{k=1}^{a-1}A_{k}+\sum_{k=1}^{b-1}B_{k}. |  | (3) |

Upon subtracting ( 3) from ( 2), we get

 | N − 1 \displaystyle N-1 | = n ​ d 2 + n ⁡ ( n + 3) 2 ​ d 3 + n 3 + 6 ​ n 2 + 11 ​ n 6 ​ d 4 \displaystyle=nd_{2}+\frac{n(n+3)}{2}d_{3}+\frac{n^{3}+6n^{2}+11n}{6}d_{4} |  | (4) |

 |  | − ∑ k = 1 a − 1 A k ( 1 − ζ a − n ​ k) − ∑ k = 1 b − 1 B k ( 1 − ζ b − n ​ k). \displaystyle-\sum_{k=1}^{a-1}A_{k}(1-\zeta_{a}^{-nk})-\sum_{k=1}^{b-1}B_{k}(1-\zeta_{b}^{-nk}). |  |

The usual procedure for finding coefficients of a partial fraction expansion gives the following equations.

 | d 4 \displaystyle d_{4} | = 1 a ​ b, \displaystyle=\frac{1}{ab}, |  |

 | d 3 \displaystyle d_{3} | = a + b − 2 2 ​ a ​ b, \displaystyle=\frac{a+b-2}{2ab}, |  |

 | d 2 \displaystyle d_{2} | = γ ⁡ ( a, b), \displaystyle=\gamma(a,b), |  |

 | A k \displaystyle A_{k} | = 1 a ⁡ ( 1 − ζ a b ​ k) ​ ( 1 − ζ a k) 2, \displaystyle=\frac{1}{a(1-\zeta_{a}^{bk})(1-\zeta_{a}^{k})^{2}}, |  |

 | B k \displaystyle B_{k} | = 1 b ⁡ ( 1 − ζ b c ​ k) ​ ( 1 − ζ b k) 2. \displaystyle=\frac{1}{b(1-\zeta_{b}^{ck})(1-\zeta_{b}^{k})^{2}}. |  |

Substituting these back into ( 4), we have

 | N = 1 + n ​ γ ​ ( a, b) + n ⁡ ( n + 3) 2 ​ ( a + b − 2 2 ​ a ​ b) + n 3 + 6 ​ n 2 + 11 ​ n 6 ​ a ​ b − ( S 1 a + S 2 b), N=1+n\gamma(a,b)+\frac{n(n+3)}{2}\left(\frac{a+b-2}{2ab}\right)+\frac{n^{3}+6n^{2}+11n}{6ab}-\left(\frac{S_{1}}{a}+\frac{S_{2}}{b}\right), |  | (5) |

where

 | S 1 = ∑ k = 1 a − 1 1 − ζ a − n ​ k ( 1 − ζ a b ​ k) ​ ( 1 − ζ a k) 2 S_{1}=\sum_{k=1}^{a-1}\frac{1-\zeta_{a}^{-nk}}{(1-\zeta_{a}^{bk})(1-\zeta_{a}^{k})^{2}} |  |

and

 | S 2 = ∑ k = 1 b − 1 1 − ζ b − n ​ k ( 1 − ζ b a ​ k) ​ ( 1 − ζ b k) 2. S_{2}=\sum_{k=1}^{b-1}\frac{1-\zeta_{b}^{-nk}}{(1-\zeta_{b}^{ak})(1-\zeta_{b}^{k})^{2}}. |  |

Next, we find S 1 S_{1} and S 2 S_{2}. By definition of n n, we have n ≡ − b ⁡ ( h + 1) n\equiv-b(h+1) (mod a a), so ζ a − n ​ k = ζ a b ⁡ ( h + 1) ​ k \zeta_{a}^{-nk}=\zeta_{a}^{b(h+1)k}, and thus,

 | S 1 \displaystyle S_{1} | = ∑ k = 1 a − 1 1 − ζ a b ⁡ ( h + 1) ​ k ( 1 − ζ a b ​ k) ​ ( 1 − ζ a k) 2 \displaystyle=\sum_{k=1}^{a-1}\frac{1-\zeta_{a}^{b(h+1)k}}{(1-\zeta_{a}^{bk})(1-\zeta_{a}^{k})^{2}} |  | (6) |

 |  | = ∑ k = 1 a − 1 ∑ j = 0 h ζ a j ​ b ​ k ( 1 − ζ a k) 2 \displaystyle=\sum_{k=1}^{a-1}\sum_{j=0}^{h}\frac{\zeta_{a}^{jbk}}{(1-\zeta_{a}^{k})^{2}} |  |

 |  | = ∑ k = 1 a − 1 ∑ j = 0 h 1 ( 1 − ζ a k) 2 − ∑ k = 1 a − 1 ∑ j = 0 h 1 − ζ a j ​ b ​ k ( 1 − ζ a k) 2. \displaystyle=\sum_{k=1}^{a-1}\sum_{j=0}^{h}\frac{1}{(1-\zeta_{a}^{k})^{2}}-\sum_{k=1}^{a-1}\sum_{j=0}^{h}\frac{1-\zeta_{a}^{jbk}}{(1-\zeta_{a}^{k})^{2}}. |  |

Note that for each 1 ≤ k ≤ ( a − 1) 1\leq k\leq(a-1), 1 1 − ζ a k \frac{1}{1-\zeta_{a}^{k}} satisfies ( 1 − 1 x) a = 1 \left(1-\frac{1}{x}\right)^{a}=1. That is, for each 1 ≤ k ≤ ( a − 1) 1\leq k\leq(a-1), 1 1 − ζ a k \frac{1}{1-\zeta_{a}^{k}} is a root of the equation

 | a ​ x a − 1 − ( a 2) ​ x a − 2 + ( a 3) ​ x a − 3 − ⋯ = 0. ax^{a-1}-{a\choose 2}x^{a-2}+{a\choose 3}x^{a-3}-\cdots=0. |  |

From there, it is easy to see that

 | ∑ k = 1 a − 1 1 ( 1 − ζ a k) 2 = − ( a − 1) ​ ( a − 5) 12, \sum_{k=1}^{a-1}\frac{1}{(1-\zeta_{a}^{k})^{2}}=-\frac{(a-1)(a-5)}{12}, |  |

and thus, changing the order of summations yields

 | ∑ k = 1 a − 1 ∑ j = 0 h 1 ( 1 − ζ a k) 2 = − ( h + 1) ​ ( a − 1) ​ ( a − 5) 12. \sum_{k=1}^{a-1}\sum_{j=0}^{h}\frac{1}{(1-\zeta_{a}^{k})^{2}}=-\frac{(h+1)(a-1)(a-5)}{12}. |  | (7) |

Moreover,

 | ∑ k = 1 a − 1 ∑ j = 0 h 1 − ζ a j ​ b ​ k ( 1 − ζ a k) 2 \displaystyle\sum_{k=1}^{a-1}\sum_{j=0}^{h}\frac{1-\zeta_{a}^{jbk}}{(1-\zeta_{a}^{k})^{2}} | = ∑ k = 1 a − 1 ∑ j = 1 h 1 − ζ a j ​ b ​ k ( 1 − ζ a k) 2 \displaystyle=\sum_{k=1}^{a-1}\sum_{j=1}^{h}\frac{1-\zeta_{a}^{jbk}}{(1-\zeta_{a}^{k})^{2}} |  | (8) |

 |  | = ∑ k = 1 a − 1 ∑ j = 1 h ∑ l = 0 b ​ j − 1 ζ a k ​ l 1 − ζ a k \displaystyle=\sum_{k=1}^{a-1}\sum_{j=1}^{h}\sum_{l=0}^{bj-1}\frac{\zeta_{a}^{kl}}{1-\zeta_{a}^{k}} |  |

 |  | = ∑ k = 1 a − 1 ∑ j = 1 h ∑ l = 0 b ​ j − 1 1 1 − ζ a k − ∑ k = 1 a − 1 ∑ j = 1 h ∑ l = 1 b ​ j − 1 1 − ζ a k ​ l 1 − ζ a k \displaystyle=\sum_{k=1}^{a-1}\sum_{j=1}^{h}\sum_{l=0}^{bj-1}\frac{1}{1-\zeta_{a}^{k}}-\sum_{k=1}^{a-1}\sum_{j=1}^{h}\sum_{l=1}^{bj-1}\frac{1-\zeta_{a}^{kl}}{1-\zeta_{a}^{k}} |  |

 |  | = ∑ j = 1 h ∑ l = 0 b ​ j − 1 ∑ k = 1 a − 1 1 1 − ζ a k − ∑ k = 1 a − 1 ∑ j = 1 h ∑ l = 1 b ​ j − 1 ∑ m = 0 l − 1 ζ a m ​ k \displaystyle=\sum_{j=1}^{h}\sum_{l=0}^{bj-1}\sum_{k=1}^{a-1}\frac{1}{1-\zeta_{a}^{k}}-\sum_{k=1}^{a-1}\sum_{j=1}^{h}\sum_{l=1}^{bj-1}\sum_{m=0}^{l-1}\zeta_{a}^{mk} |  |

 |  | = ( a − 1) ​ b ​ h ​ ( h + 1) 4 − ∑ k = 0 a − 1 ∑ j = 1 h ∑ l = 1 b ​ j − 1 ∑ m = 0 l − 1 ζ a m ​ k + b 2 ​ h ​ ( h + 1) ​ ( 2 ​ h + 1) 12 − b ​ h ​ ( h + 1) 4 \displaystyle=\frac{(a-1)bh(h+1)}{4}-\sum_{k=0}^{a-1}\sum_{j=1}^{h}\sum_{l=1}^{bj-1}\sum_{m=0}^{l-1}\zeta_{a}^{mk}+\frac{b^{2}h(h+1)(2h+1)}{12}-\frac{bh(h+1)}{4} |  |

 |  | = ( a − 2) ​ b ​ h ​ ( h + 1) 4 − ∑ k = 0 a − 1 ∑ j = 1 h ∑ l = 1 b ​ j − 1 ∑ m = 0 l − 1 ζ a m ​ k + b 2 ​ h ​ ( h + 1) ​ ( 2 ​ h + 1) 12. \displaystyle=\frac{(a-2)bh(h+1)}{4}-\sum_{k=0}^{a-1}\sum_{j=1}^{h}\sum_{l=1}^{bj-1}\sum_{m=0}^{l-1}\zeta_{a}^{mk}+\frac{b^{2}h(h+1)(2h+1)}{12}. |  |

We know that ∑ k = 0 a − 1 ζ a m ​ k ≠ 0 \sum_{k=0}^{a-1}\zeta_{a}^{mk}\neq 0 only if a a divides m m, and in that case, the sum is a a. Therefore,

 | ∑ k = 0 a − 1 ∑ j = 1 h ∑ l = 1 b ​ j − 1 ∑ m = 0 l − 1 ζ a m ​ k \displaystyle\sum_{k=0}^{a-1}\sum_{j=1}^{h}\sum_{l=1}^{bj-1}\sum_{m=0}^{l-1}\zeta_{a}^{mk} | = ∑ j = 1 h ∑ l = 1 b ​ j − 1 ∑ m = 0 l − 1 ∑ k = 0 a − 1 ζ a m ​ k \displaystyle=\sum_{j=1}^{h}\sum_{l=1}^{bj-1}\sum_{m=0}^{l-1}\sum_{k=0}^{a-1}\zeta_{a}^{mk} |  | (9) |

 |  | = a ​ ∑ j = 1 h ∑ l = 1 b ​ j − 1 ( ⌊ l − 1 a ⌋ + 1) \displaystyle=a\sum_{j=1}^{h}\sum_{l=1}^{bj-1}\left(\left\lfloor\frac{l-1}{a}\right\rfloor+1\right) |  |

 |  | = a ​ ∑ j = 1 h ∑ l = 1 b ​ j − 1 ⌊ l − 1 a ⌋ + a ​ b ​ h ​ ( h + 1) 2 − a ​ h. \displaystyle=a\sum_{j=1}^{h}\sum_{l=1}^{bj-1}\left\lfloor\frac{l-1}{a}\right\rfloor+\frac{abh(h+1)}{2}-ah. |  |

Next, note that ⌊ l − 1 a ⌋ = ⌊ l a ⌋ \left\lfloor\frac{l-1}{a}\right\rfloor=\left\lfloor\frac{l}{a}\right\rfloor unless a a divides l l. Therefore,

 | ∑ j = 1 h ∑ l = 1 b ​ j − 1 ⌊ l − 1 a ⌋ \displaystyle\sum_{j=1}^{h}\sum_{l=1}^{bj-1}\left\lfloor\frac{l-1}{a}\right\rfloor | = ∑ j = 1 h ∑ l = 1 b ​ j − 1 ⌊ l a ⌋ − ∑ j = 1 h ⌊ b ​ j − 1 a ⌋ \displaystyle=\sum_{j=1}^{h}\sum_{l=1}^{bj-1}\left\lfloor\frac{l}{a}\right\rfloor-\sum_{j=1}^{h}\left\lfloor\frac{bj-1}{a}\right\rfloor |  | (10) |

 |  | = ∑ j = 1 h ∑ l = 1 b ​ j − 1 ⌊ l a ⌋ − ∑ j = 1 h ⌊ b ​ j a ⌋ \displaystyle=\sum_{j=1}^{h}\sum_{l=1}^{bj-1}\left\lfloor\frac{l}{a}\right\rfloor-\sum_{j=1}^{h}\left\lfloor\frac{bj}{a}\right\rfloor |  |

 |  | = ∑ j = 1 h ∑ l = 1 b ​ j ⌊ l a ⌋ − 2 ​ ∑ j = 1 h ⌊ b ​ j a ⌋. \displaystyle=\sum_{j=1}^{h}\sum_{l=1}^{bj}\left\lfloor\frac{l}{a}\right\rfloor-2\sum_{j=1}^{h}\left\lfloor\frac{bj}{a}\right\rfloor. |  |

Finally, note that for any 1 ≤ j ≤ h 1\leq j\leq h,

 | ∑ l = 1 b ​ j ⌊ l a ⌋ \displaystyle\sum_{l=1}^{bj}\left\lfloor\frac{l}{a}\right\rfloor | = a ⁡ ( 1 + 2 + ⋯ + ( ⌊ b ​ j a ⌋ − 1)) + ⌊ b ​ j a ⌋ ​ ( b ​ j − a ⁡ ⌊ b ​ j a ⌋ + 1) \displaystyle=a\left(1+2+\cdots+\left(\left\lfloor\frac{bj}{a}\right\rfloor-1\right)\right)+\left\lfloor\frac{bj}{a}\right\rfloor\left(bj-a\left\lfloor\frac{bj}{a}\right\rfloor+1\right) |  | (11) |

 |  | = ( b ​ j ​ ⌊ b ​ j a ⌋ − a 2 ​ ⌊ b ​ j a ⌋ 2) − ( a 2 − 1) ​ ⌊ b ​ j a ⌋ \displaystyle=\left(bj\left\lfloor\frac{bj}{a}\right\rfloor-\frac{a}{2}\left\lfloor\frac{bj}{a}\right\rfloor^{2}\right)-\left(\frac{a}{2}-1\right)\left\lfloor\frac{bj}{a}\right\rfloor |  |

 |  | = a 2 ​ ⌊ b ​ j a ⌋ ​ ( 2 ​ b ​ j a − ⌊ b ​ j a ⌋) − ( a 2 − 1) ​ ⌊ b ​ j a ⌋ \displaystyle=\frac{a}{2}\left\lfloor\frac{bj}{a}\right\rfloor\left(\frac{2bj}{a}-\left\lfloor\frac{bj}{a}\right\rfloor\right)-\left(\frac{a}{2}-1\right)\left\lfloor\frac{bj}{a}\right\rfloor |  |

 |  | = a 2 ​ ( b ​ j a − { b ​ j a }) ​ ( b ​ j a + { b ​ j a }) − ( a 2 − 1) ​ ⌊ b ​ j a ⌋ \displaystyle=\frac{a}{2}\left(\frac{bj}{a}-\left\{\frac{bj}{a}\right\}\right)\left(\frac{bj}{a}+\left\{\frac{bj}{a}\right\}\right)-\left(\frac{a}{2}-1\right)\left\lfloor\frac{bj}{a}\right\rfloor |  |

 |  | = a 2 ​ ( ( b ​ j a) 2 − { b ​ j a } 2) − ( a 2 − 1) ​ ⌊ b ​ j a ⌋. \displaystyle=\frac{a}{2}\left(\left(\frac{bj}{a}\right)^{2}-\left\{\frac{bj}{a}\right\}^{2}\right)-\left(\frac{a}{2}-1\right)\left\lfloor\frac{bj}{a}\right\rfloor. |  |

Therefore, by ( 10) and ( 11),

 | ∑ j = 1 h ∑ l = 1 b ​ j − 1 ⌊ l − 1 a ⌋ \displaystyle\sum_{j=1}^{h}\sum_{l=1}^{bj-1}\left\lfloor\frac{l-1}{a}\right\rfloor | = b 2 ​ h ​ ( h + 1) ​ ( 2 ​ h + 1) 12 ​ a − a 2 ​ ( ∑ j = 1 h { b ​ j a } 2) − ( a 2 + 1) ​ ∑ j = 1 h ⌊ b ​ j a ⌋ \displaystyle=\frac{b^{2}h(h+1)(2h+1)}{12a}-\frac{a}{2}\left(\sum_{j=1}^{h}\left\{\frac{bj}{a}\right\}^{2}\right)-\left(\frac{a}{2}+1\right)\sum_{j=1}^{h}\left\lfloor\frac{bj}{a}\right\rfloor |  | (12) |

 |  | = b 2 ​ h ​ ( h + 1) ​ ( 2 ​ h + 1) 12 ​ a − S ⁡ ( a, b, h). \displaystyle=\frac{b^{2}h(h+1)(2h+1)}{12a}-S(a,b;h). |  |

From ( 6), ( 7), ( 8), ( 9) and ( 12), we get that

 | S 1 = − ( h + 1) ​ ( a − 1) ​ ( a − 5) 12 + b ​ h ​ ( h + 1) ​ ( a + 2) 4 − a ​ ∑ j = 1 h ⌊ b ​ j a ⌋ − a ​ h − a ​ S ​ ( a, b, h). S_{1}=-\frac{(h+1)(a-1)(a-5)}{12}+\frac{bh(h+1)(a+2)}{4}-a\sum_{j=1}^{h}\left\lfloor\frac{bj}{a}\right\rfloor-ah-aS(a,b;h). |  | (13) |

Symmetrically, we get

 | S 2 = − ( H + 1) ​ ( b − 1) ​ ( b − 5) 12 + a ​ H ​ ( H + 1) ​ ( b + 2) 4 − b ​ ∑ j = 1 H ⌊ a ​ j b ⌋ − b ​ H − b ​ S ​ ( b, a, H). S_{2}=-\frac{(H+1)(b-1)(b-5)}{12}+\frac{aH(H+1)(b+2)}{4}-b\sum_{j=1}^{H}\left\lfloor\frac{aj}{b}\right\rfloor-bH-bS(b,a;H). |  | (14) |

The result now follows from ( 5), ( 13) and ( 14). ∎

Using Lemma 4 and Lemma 5, we get the following reciprocity relation for S ⁡ ( a, b, h) S(a,b;h). For brevity of notation, define

 | η 2 ​ ( a, b, h):= ( n + 1) ​ ( n + 2) 2 + ( a − 1) ​ ( b − 1) ​ ( 2 ​ a ​ b − a − b − 6 ​ n − 7) 12 − η 1 ​ ( a, b, h). \eta_{2}(a,b,h):=\frac{(n+1)(n+2)}{2}+\frac{(a-1)(b-1)(2ab-a-b-6n-7)}{12}-\eta_{1}(a,b,h). |  |

###### Theorem 6.

For given positive coprime integers a a and b b, and a given natural number h h, S ⁡ ( a, b, h) S(a,b;h) satisfies the following reciprocity relationship:

 | S ⁡ ( a, b, h) + S ⁡ ( b, a, H) = η 2 ​ ( a, b, h). S(a,b;h)+S(b,a;H)=\eta_{2}(a,b,h). |  |

Next, we describe our algorithm for calculating S ⁡ ( a, b, h) S(a,b;h).

1. 1.

Suppose a > b a>b. We express S ⁡ ( a, b, h) S(a,b;h) in terms of S ⁡ ( b, a, H) S(b,a;H) using Theorem 6.

2. 2.

Suppose b ≥ a b\geq a. Then, b = a ​ q + r b=aq+r for some q ≥ 1 q\geq 1 and r < a r<a. Then, it is easy to observe that

 | S ⁡ ( a, b, h) = S ⁡ ( a, r, h) + q ​ h ​ ( h + 1) ​ ( a + 2) 4. S(a,b;h)=S(a,r;h)+\frac{qh(h+1)(a+2)}{4}. |  | (15) |

3. 3.

We keep repeating Steps 1 1 and 2 2 until we are done.

### 2.2 An example

Suppose we want to calculate the value of T 1 ​ ( 8411, 2732, 1221) T_{1}(8411,2732;1221), that is

 | ∑ i = 1 1221 { 2732 ​ i 8411 } 2. \sum_{i=1}^{1221}\left\{\frac{2732\hskip 1.42271pti}{8411}\right\}^{2}. |  |

First, we evaluate S ⁡ ( 8411, 2732, 1221) S(8411,2732;1221) using the above algorithm. Set a = 8411 a=8411, b = 2732 b=2732 and h = 1221 h=1221 in Theorem 6 to get

 | S ⁡ ( 8411, 2732, 1221) + S ⁡ ( 2732, 8411, 2335) = 5521952154451967 441901. S(8411,2732;1221)+S(2732,8411;2335)=\frac{5521952154451967}{441901}. |  | (16) |

Using ( 15), we get

 | S ⁡ ( 2732, 8411, 2335) = S ⁡ ( 2732,215, 2335) + 11184575280. S(2732,8411;2335)=S(2732,215;2335)+11184575280. |  | (17) |

Using Theorem 6, we get

 | S ⁡ ( 2732,215, 2335) + S ⁡ ( 215, 2732, 31) = 43105956866071 146845. S(2732,215;2335)+S(215,2732;31)=\frac{43105956866071}{146845}. |  | (18) |

Using ( 15), we get

 | S ⁡ ( 215, 2732, 31) = S ⁡ ( 215,152, 31) + 645792. S(215,2732;31)=S(215,152;31)+645792. |  | (19) |

Using Theorem 6, we get

 | S ⁡ ( 215,152, 31) + S ⁡ ( 152,215, 129) = 62027530983 65360. S(215,152;31)+S(152,215;129)=\frac{62027530983}{65360}. |  | (20) |

Using ( 15), we get

 | S ⁡ ( 152,215, 129) = S ⁡ ( 152, 63, 129) + 645645. S(152,215;129)=S(152,63;129)+645645. |  | (21) |

Using Theorem 6, we get

 | S ⁡ ( 152, 63, 129) + S ⁡ ( 63,152, 9) = 1719655381 6384. S(152,63;129)+S(63,152;9)=\frac{1719655381}{6384}. |  | (22) |

Using ( 15), we get

 | S ⁡ ( 63,152, 9) = S ⁡ ( 63, 26, 9) + 2925. S(63,152;9)=S(63,26;9)+2925. |  | (23) |

Using Theorem 6, we get

 | S ⁡ ( 63, 26, 9) + S ⁡ ( 26, 63, 21) = 9093619 1092. S(63,26;9)+S(26,63;21)=\frac{9093619}{1092}. |  | (24) |

Using ( 15), we get

 | S ⁡ ( 26, 63, 21) = S ⁡ ( 26, 11, 21) + 6468. S(26,63;21)=S(26,11;21)+6468. |  | (25) |

Using Theorem 6, we get

 | S ⁡ ( 26, 11, 21) + S ⁡ ( 11, 26, 1) = 757997 572. S(26,11;21)+S(11,26;1)=\frac{757997}{572}. |  | (26) |

Finally, it is easy to see that

 | S ⁡ ( 11, 26, 1) = 151 11. S(11,26;1)=\frac{151}{11}. |  | (27) |

From ( 16) to ( 27), we get that

 | S ⁡ ( 8411, 2732, 1221) = 658946167630 647. S(8411,2732;1221)=\frac{658946167630}{647}. |  |

That is,

 | ( 8411 2) ​ ∑ i = 1 1221 { 2732 ​ i 8411 } 2 + ( 8413 2) ​ ∑ i = 1 1221 ⌊ 2732 ​ i 8411 ⌋ = 658946167630 647. \left(\frac{8411}{2}\right)\sum_{i=1}^{1221}\left\{\frac{2732\hskip 1.42271pti}{8411}\right\}^{2}+\left(\frac{8413}{2}\right)\sum_{i=1}^{1221}\left\lfloor\frac{2732\hskip 1.42271pti}{8411}\right\rfloor=\frac{658946167630}{647}. |  | (28) |

The summation ∑ i = 1 1221 ⌊ 2732 ​ i 8411 ⌋ \sum_{i=1}^{1221}\left\lfloor\frac{2732\hskip 1.42271pti}{8411}\right\rfloor can be easily calculated using the algorithm described in [1, Section 2.3]. However, we provide all the details here for the sake of completeness.

In order to solve the first sum, we apply Theorem 3 to get

 | ∑ i = 1 1221 ⌊ 2732 ​ i 8411 ⌋ = 483516 − ∑ i = 1 396 ⌊ 8411 ​ i 2732 ⌋. \sum_{i=1}^{1221}\left\lfloor\frac{2732\hskip 1.42271pti}{8411}\right\rfloor=483516-\sum_{i=1}^{396}\left\lfloor\frac{8411\hskip 1.42271pti}{2732}\right\rfloor. |  | (29) |

Then, by the division algorithm,

 | ∑ i = 1 396 ⌊ 8411 ​ i 2732 ⌋ \displaystyle\sum_{i=1}^{396}\left\lfloor\frac{8411\hskip 1.42271pti}{2732}\right\rfloor | = ∑ i = 1 396 ( 3 ​ i + ⌊ 215 ​ i 2732 ⌋) \displaystyle=\sum_{i=1}^{396}\left(3i+\left\lfloor\frac{215i}{2732}\right\rfloor\right) |  | (30) |

 |  | = 235818 + ∑ i = 1 396 ⌊ 215 ​ i 2732 ⌋. \displaystyle=235818+\sum_{i=1}^{396}\left\lfloor\frac{215i}{2732}\right\rfloor. |  |

Repeated applications of Theorem 3, followed by the division algorithm, give the following equations.

 | ∑ i = 1 396 ⌊ 215 ​ i 2732 ⌋ \displaystyle\sum_{i=1}^{396}\left\lfloor\frac{215i}{2732}\right\rfloor | = 12276 − ∑ i = 1 31 ⌊ 2732 ​ i 215 ⌋ \displaystyle=12276-\sum_{i=1}^{31}\left\lfloor\frac{2732\hskip 1.42271pti}{215}\right\rfloor |  | (31) |

 |  | = 6324 − ∑ i = 1 31 ⌊ 152 ​ i 215 ⌋, \displaystyle=6324-\sum_{i=1}^{31}\left\lfloor\frac{152i}{215}\right\rfloor, |  |

 | ∑ i = 1 31 ⌊ 152 ​ i 215 ⌋, \displaystyle\sum_{i=1}^{31}\left\lfloor\frac{152i}{215}\right\rfloor, | = 651 − ∑ i = 1 21 ⌊ 215 ​ i 152 ⌋ \displaystyle=651-\sum_{i=1}^{21}\left\lfloor\frac{215i}{152}\right\rfloor |  | (32) |

 |  | = 420 − ∑ i = 1 21 ⌊ 63 ​ i 152 ⌋, \displaystyle=420-\sum_{i=1}^{21}\left\lfloor\frac{63i}{152}\right\rfloor, |  |

 | ∑ i = 1 21 ⌊ 63 ​ i 152 ⌋ \displaystyle\sum_{i=1}^{21}\left\lfloor\frac{63i}{152}\right\rfloor | = 168 − ∑ i = 1 8 ⌊ 152 ​ i 63 ⌋ \displaystyle=168-\sum_{i=1}^{8}\left\lfloor\frac{152i}{63}\right\rfloor |  | (33) |

 |  | = 96 − ∑ i = 1 8 ⌊ 26 ​ i 63 ⌋, \displaystyle=96-\sum_{i=1}^{8}\left\lfloor\frac{26i}{63}\right\rfloor, |  |

 | ∑ i = 1 8 ⌊ 26 ​ i 63 ⌋ \displaystyle\sum_{i=1}^{8}\left\lfloor\frac{26i}{63}\right\rfloor | = 24 − ∑ i = 1 3 ⌊ 63 ​ i 26 ⌋ \displaystyle=24-\sum_{i=1}^{3}\left\lfloor\frac{63i}{26}\right\rfloor |  | (34) |

 |  | = 12 − ∑ i = 1 3 ⌊ 11 ​ i 26 ⌋, \displaystyle=12-\sum_{i=1}^{3}\left\lfloor\frac{11i}{26}\right\rfloor, |  |

and

 | ∑ i = 1 3 ⌊ 11 ​ i 26 ⌋ \displaystyle\sum_{i=1}^{3}\left\lfloor\frac{11i}{26}\right\rfloor | = 3 − ∑ i = 1 1 ⌊ 26 ​ i 11 ⌋ \displaystyle=3-\sum_{i=1}^{1}\left\lfloor\frac{26i}{11}\right\rfloor |  | (35) |

 |  | = 1. \displaystyle=1. |  |

From ( 29) to ( 35), we get

 | ∑ i = 1 1221 ⌊ 2732 ​ i 8411 ⌋ = 241709. \sum_{i=1}^{1221}\left\lfloor\frac{2732\hskip 1.42271pti}{8411}\right\rfloor=241709. |  | (36) |

From ( 28) and ( 36), we get that

 | T 1 ​ ( 8411, 2732, 1221) = ∑ i = 1 1221 { 2732 ​ i 8411 } 2 = 2219247661 5441917. T_{1}(8411,2732;1221)=\sum_{i=1}^{1221}\left\{\frac{2732\hskip 1.42271pti}{8411}\right\}^{2}=\frac{2219247661}{5441917}. |  | (37) |

Multiplying both sides of this equation by 8411 2 8411^{2}, the above statement is equivalent to

 | ∑ i = 1 1221 r i 2 = 28850219593, \sum_{i=1}^{1221}r_{i}^{2}=28850219593, |  |

where r i r_{i} is the remainder when 2732 ​ i 2732\hskip 1.42271pti is divided by 8411 8411.

## 3 An algorithm for T 2 ​ ( a, b, h) T_{2}(a,b;h) and T 3 ​ ( a, b, h) T_{3}(a,b;h)

Recall our notation from Section 1.

- •

T 1 ​ ( a, b, h) = ∑ i = 1 h { i ​ b a } 2 T_{1}(a,b;h)=\sum_{i=1}^{h}\{\frac{ib}{a}\}^{2}.

- •

T 2 ​ ( a, b, h) = ∑ i = 1 h i ⁡ ⌊ i ​ b a ⌋ T_{2}(a,b;h)=\sum_{i=1}^{h}i\lfloor\frac{ib}{a}\rfloor.

- •

T 3 ​ ( a, b, h) = ∑ i = 1 h ⌊ i ​ b a ⌋ 2 T_{3}(a,b;h)=\sum_{i=1}^{h}\lfloor\frac{ib}{a}\rfloor^{2}.

Note that

 | T 3 ​ ( a, b, h) − T 1 ​ ( a, b, h) \displaystyle T_{3}(a,b;h)-T_{1}(a,b;h) | = ∑ i = 1 h i ​ b a ​ ( ⌊ i ​ b a ⌋ − { i ​ b a }) \displaystyle=\sum_{i=1}^{h}\frac{ib}{a}\left(\left\lfloor\frac{ib}{a}\right\rfloor-\left\{\frac{ib}{a}\right\}\right) |  |

 |  | = ∑ i = 1 h i ​ b a ​ ( 2 ​ ⌊ i ​ b a ⌋ − i ​ b a) \displaystyle=\sum_{i=1}^{h}\frac{ib}{a}\left(2\left\lfloor\frac{ib}{a}\right\rfloor-\frac{ib}{a}\right) |  |

 |  | = 2 ​ b a ​ T 2 ​ ( a, b, h) − b 2 ​ h ​ ( h + 1) ​ ( 2 ​ h + 1) 6 ​ a 2. \displaystyle=\frac{2b}{a}T_{2}(a,b;h)-\frac{b^{2}h(h+1)(2h+1)}{6a^{2}}. |  |

Thus, we get the following relationship between T 1 ​ ( a, b, h) T_{1}(a,b;h), T 2 ​ ( a, b, h) T_{2}(a,b;h) and T 3 ​ ( a, b, h) T_{3}(a,b;h).

 | T 3 ​ ( a, b, h) = T 1 ​ ( a, b, h) + 2 ​ b a ​ T 2 ​ ( a, b, h) − b 2 ​ h ​ ( h + 1) ​ ( 2 ​ h + 1) 6 ​ a 2. T_{3}(a,b;h)=T_{1}(a,b;h)+\frac{2b}{a}T_{2}(a,b;h)-\frac{b^{2}h(h+1)(2h+1)}{6a^{2}}. |  | (38) |

### 3.1 Reciprocity relation for T 2 ​ ( a, b, h) T_{2}(a,b;h)

Next, we use another method to calculate T 3 ​ ( a, b, h) T_{3}(a,b;h). We generalize the ideas in the proof of Theorem 3 described in [1]. For the sake of completeness, we provide all the details here. Let h ′ h^{\prime} denote the quantity ⌊ b ​ h a ⌋ \left\lfloor\frac{bh}{a}\right\rfloor. Then,

 | T 3 ​ ( a, b, h) = ∑ t = 1 h ′ t 2 ​ n t, T_{3}(a,b;h)=\sum_{t=1}^{h^{\prime}}t^{2}n_{t}, |  |

where n t n_{t} is the number of i i such that 1 ≤ i ≤ h 1\leq i\leq h and ⌊ i ​ b a ⌋ = t \left\lfloor\frac{ib}{a}\right\rfloor=t. Clearly, if t < h ′ t<h^{\prime}, then

 | n t = ⌊ ( t + 1) ​ a b ⌋ − ⌊ t ​ a b ⌋; n_{t}=\left\lfloor\frac{(t+1)a}{b}\right\rfloor-\left\lfloor\frac{ta}{b}\right\rfloor; |  |

if t = h ′ t=h^{\prime}, then

 | n t = h − ⌊ h ′ ​ a b ⌋. n_{t}=h-\left\lfloor\frac{h^{\prime}a}{b}\right\rfloor. |  |

Therefore,

 | ∑ i = 1 h ⌊ i ​ b a ⌋ 2 \displaystyle\sum_{i=1}^{h}\left\lfloor\frac{ib}{a}\right\rfloor^{2} | = ∑ t = 1 h ′ − 1 ( ⌊ ( t + 1) ​ a b ⌋ − ⌊ t ​ a b ⌋) ​ t 2 + ( h − ⌊ h ′ ​ a b ⌋) ​ h ′ 2 \displaystyle=\sum_{t=1}^{h^{\prime}-1}\left(\left\lfloor\frac{(t+1)a}{b}\right\rfloor-\left\lfloor\frac{ta}{b}\right\rfloor\right)t^{2}+\left(h-\left\lfloor\frac{h^{\prime}a}{b}\right\rfloor\right)h^{\prime 2} |  |

 |  | = ∑ t = 1 h ′ − 1 ( t 2 ​ ⌊ ( t + 1) ​ a b ⌋ − ( t − 1) 2 ​ ⌊ t ​ a b ⌋) − ∑ t = 1 h ′ − 1 ( 2 ​ t − 1) ​ ⌊ t ​ a b ⌋ + ( h − ⌊ h ′ ​ a b ⌋) ​ h ′ 2 \displaystyle=\sum_{t=1}^{h^{\prime}-1}\left(t^{2}\left\lfloor\frac{(t+1)a}{b}\right\rfloor-(t-1)^{2}\left\lfloor\frac{ta}{b}\right\rfloor\right)-\sum_{t=1}^{h^{\prime}-1}(2t-1)\left\lfloor\frac{ta}{b}\right\rfloor+\left(h-\left\lfloor\frac{h^{\prime}a}{b}\right\rfloor\right)h^{\prime 2} |  |

 |  | = ( h ′ − 1) 2 ​ ⌊ h ′ ​ a b ⌋ − ∑ t = 1 h ′ − 1 ( 2 ​ t − 1) ​ ⌊ t ​ a b ⌋ + h ​ h ′ 2 − h ′ 2 ​ ⌊ h ′ ​ a b ⌋ \displaystyle=(h^{\prime}-1)^{2}\left\lfloor\frac{h^{\prime}a}{b}\right\rfloor-\sum_{t=1}^{h^{\prime}-1}(2t-1)\left\lfloor\frac{ta}{b}\right\rfloor+hh^{\prime 2}-h^{\prime 2}\left\lfloor\frac{h^{\prime}a}{b}\right\rfloor |  |

 |  | = h ​ h ′ 2 − ∑ t = 1 h ′ ( 2 ​ t − 1) ​ ⌊ t ​ a b ⌋ \displaystyle=hh^{\prime 2}-\sum_{t=1}^{h^{\prime}}(2t-1)\left\lfloor\frac{ta}{b}\right\rfloor |  |

 |  | = h ​ h ′ 2 − 2 ​ T 2 ​ ( b, a, h ′) + ∑ t = 1 h ′ ⌊ t ​ a b ⌋. \displaystyle=hh^{\prime 2}-2T_{2}(b,a;h^{\prime})+\sum_{t=1}^{h^{\prime}}\left\lfloor\frac{ta}{b}\right\rfloor. |  |

Thus, we obtain the following relation:

 | T 3 ​ ( a, b, h) = h ​ h ′ 2 − 2 ​ T 2 ​ ( b, a, h ′) + ∑ t = 1 h ′ ⌊ t ​ a b ⌋. T_{3}(a,b;h)=hh^{\prime 2}-2T_{2}(b,a;h^{\prime})+\sum_{t=1}^{h^{\prime}}\left\lfloor\frac{ta}{b}\right\rfloor. |  | (39) |

Using ( 38) and ( 39), we get the following reciprocity relation for T 2 ​ ( a, b, h) T_{2}(a,b;h):

 | T 2 ​ ( a, b, h) + a b ​ T 2 ​ ( b, a, h ′) = a ​ h ​ h ′ 2 2 ​ b + a 2 ​ b ​ ( ∑ t = 1 h ′ ⌊ t ​ a b ⌋) − a 2 ​ b ​ T 1 ​ ( a, b, h) + b ​ h ​ ( h + 1) ​ ( 2 ​ h + 1) 12 ​ a. T_{2}(a,b;h)+\frac{a}{b}T_{2}(b,a;h^{\prime})=\frac{ahh^{\prime 2}}{2b}+\frac{a}{2b}\left(\sum_{t=1}^{h^{\prime}}\left\lfloor\frac{ta}{b}\right\rfloor\right)-\frac{a}{2b}T_{1}(a,b;h)+\frac{bh(h+1)(2h+1)}{12a}. |  | (40) |

We describe our algorithm for calculating T 2 ​ ( a, b, h) T_{2}(a,b;h). The quantity T 3 ​ ( a, b, h) T_{3}(a,b;h) can then be easily obtained from T 1 ​ ( a, b, h) T_{1}(a,b;h) and T 2 ​ ( a, b, h) T_{2}(a,b;h) using ( 38). Our algorithm for T 2 ​ ( a, b, h) T_{2}(a,b;h) is as follows:

1. 1.

Suppose a > b a>b. We express T 2 ​ ( a, b, h) T_{2}(a,b;h) in terms of T 2 ​ ( b, a, h ′) T_{2}(b,a;h^{\prime}) using ( 40). Note that the expression involves the terms T 1 ​ ( a, b, h) T_{1}(a,b;h) and ∑ t = 1 h ′ ⌊ t ​ a b ⌋ \sum_{t=1}^{h^{\prime}}\left\lfloor\frac{ta}{b}\right\rfloor. The former can be calculated using the algorithm in Section 2 and the latter can be calculated using Theorem 3, as described in the algorithm in [1, Section 2.3].

2. 2.

Suppose b ≥ a b\geq a. Then, b = a ​ q + r b=aq+r for some q ≥ 1 q\geq 1 and r < a r<a. Then, it is easy to observe that

 | T 2 ​ ( a, b, h) = T 2 ​ ( a, r, h) + q ​ h ​ ( h + 1) ​ ( 2 ​ h + 1) 6. T_{2}(a,b;h)=T_{2}(a,r;h)+\frac{qh(h+1)(2h+1)}{6}. |  | (41) |

3. 3.

We keep repeating Steps 1 1 and 2 2 until we are done.

### 3.2 An example

We return to our example a = 8411 a=8411, b = 2732 b=2732 and h = 1221 h=1221. Using our algorithm for T 1 ​ ( a, b, h) T_{1}(a,b;h) in Section 2 and the algorithm for ∑ i = 1 h ′ ⌊ i ​ a b ⌋ \sum_{i=1}^{h^{\prime}}\left\lfloor\frac{ia}{b}\right\rfloor in [1, Section 2.3], we easily obtain

 | T 1 ​ ( 8411, 2732, 1221) \displaystyle T_{1}(8411,2732;1221) | = 2219247661 5441917, \displaystyle=\frac{2219247661}{5441917}, |  |

 | ∑ i = 1 396 ⌊ 8411 ​ i 2732 ⌋ \displaystyle\sum_{i=1}^{396}\left\lfloor\frac{8411\hskip 1.42271pti}{2732}\right\rfloor | = 241807. \displaystyle=241807. |  |

Then using ( 40),

 | T 2 ​ ( 8411, 2732, 1221) + 8411 2732 ​ T 2 ​ ( 2732, 8411, 396) = 1075804292917 2732. T_{2}(8411,2732;1221)+\frac{8411}{2732}T_{2}(2732,8411;396)=\frac{1075804292917}{2732}. |  | (42) |

From ( 41), we get

 | T 2 ​ ( 2732, 8411, 396) = T 2 ​ ( 2732,215, 396) + 62334558. T_{2}(2732,8411;396)=T_{2}(2732,215;396)+62334558. |  | (43) |

Using our algorithm for T 1 ​ ( a, b, h) T_{1}(a,b;h) in Section 2 and the algorithm for ∑ i = 1 h ′ ⌊ i ​ a b ⌋ \sum_{i=1}^{h^{\prime}}\left\lfloor\frac{ia}{b}\right\rfloor in [1, Section 2.3], we easily obtain

 | T 1 ​ ( 2732,215, 396) \displaystyle T_{1}(2732,215;396) | = 489539849 3731912, \displaystyle=\frac{489539849}{3731912}, |  |

 | ∑ i = 1 31 ⌊ 2732 ​ i 215 ⌋ \displaystyle\sum_{i=1}^{31}\left\lfloor\frac{2732\hskip 1.42271pti}{215}\right\rfloor | = 6287. \displaystyle=6287. |  |

Then using ( 40),

 | T 2 ​ ( 2732,215, 396) + 2732 215 ​ T 2 ​ ( 215, 2732, 31) = 704030131 215. T_{2}(2732,215;396)+\frac{2732}{215}T_{2}(215,2732;31)=\frac{704030131}{215}. |  | (44) |

From ( 41), we get

 | T 2 ​ ( 215, 2732, 31) = T 2 ​ ( 215,152, 31) + 124992. T_{2}(215,2732;31)=T_{2}(215,152;31)+124992. |  | (45) |

Using our algorithm for T 1 ​ ( a, b, h) T_{1}(a,b;h) in Section 2 and the algorithm for ∑ i = 1 h ′ ⌊ i ​ a b ⌋ \sum_{i=1}^{h^{\prime}}\left\lfloor\frac{ia}{b}\right\rfloor in [1, Section 2.3], we easily obtain

 | T 1 ​ ( 215,152, 31) \displaystyle T_{1}(215,152;31) | = 483579 46225, \displaystyle=\frac{483579}{46225}, |  |

 | ∑ i = 1 21 ⌊ 215 ​ i 152 ⌋ \displaystyle\sum_{i=1}^{21}\left\lfloor\frac{215\hskip 1.42271pti}{152}\right\rfloor | = 316. \displaystyle=316. |  |

Then using ( 40),

 | T 2 ​ ( 215,152, 31) + 215 152 ​ T 2 ​ ( 152,215, 21) = 515533 38. T_{2}(215,152;31)+\frac{215}{152}T_{2}(152,215;21)=\frac{515533}{38}. |  | (46) |

From ( 41), we get

 | T 2 ​ ( 152,215, 21) = T 2 ​ ( 152, 63, 21) + 3311. T_{2}(152,215;21)=T_{2}(152,63;21)+3311. |  | (47) |

Using our algorithm for T 1 ​ ( a, b, h) T_{1}(a,b;h) in Section 2 and the algorithm for ∑ i = 1 h ′ ⌊ i ​ a b ⌋ \sum_{i=1}^{h^{\prime}}\left\lfloor\frac{ia}{b}\right\rfloor in [1, Section 2.3], we easily obtain

 | T 1 ​ ( 152, 63, 21) \displaystyle T_{1}(152,63;21) | = 164511 23104, \displaystyle=\frac{164511}{23104}, |  |

 | ∑ i = 1 8 ⌊ 152 ​ i 63 ⌋ \displaystyle\sum_{i=1}^{8}\left\lfloor\frac{152\hskip 1.42271pti}{63}\right\rfloor | = 83. \displaystyle=83. |  |

Then using ( 40),

 | T 2 ​ ( 152, 63, 21) + 152 63 ​ T 2 ​ ( 63,152, 8) = 151139 63. T_{2}(152,63;21)+\frac{152}{63}T_{2}(63,152;8)=\frac{151139}{63}. |  | (48) |

From ( 41), we get

 | T 2 ​ ( 63,152, 8) = T 2 ​ ( 63, 26, 8) + 408. T_{2}(63,152;8)=T_{2}(63,26;8)+408. |  | (49) |

Using our algorithm for T 1 ​ ( a, b, h) T_{1}(a,b;h) in Section 2 and the algorithm for ∑ i = 1 h ′ ⌊ i ​ a b ⌋ \sum_{i=1}^{h^{\prime}}\left\lfloor\frac{ia}{b}\right\rfloor in [1, Section 2.3], we easily obtain

 | T 1 ​ ( 63, 26, 8) \displaystyle T_{1}(63,26;8) | = 3233 1323, \displaystyle=\frac{3233}{1323}, |  |

 | ∑ i = 1 3 ⌊ 63 ​ i 26 ⌋ \displaystyle\sum_{i=1}^{3}\left\lfloor\frac{63\hskip 1.42271pti}{26}\right\rfloor | = 13. \displaystyle=13. |  |

Then using ( 40),

 | T 2 ​ ( 63, 26, 8) + 63 26 ​ T 2 ​ ( 26, 63, 3) = 3695 26. T_{2}(63,26;8)+\frac{63}{26}T_{2}(26,63;3)=\frac{3695}{26}. |  | (50) |

From ( 41), we get

 | T 2 ​ ( 26, 63, 3) = T 2 ​ ( 26, 11, 3) + 28. T_{2}(26,63;3)=T_{2}(26,11;3)+28. |  | (51) |

Using our algorithm for T 1 ​ ( a, b, h) T_{1}(a,b;h) in Section 2 and the algorithm for ∑ i = 1 h ′ ⌊ i ​ a b ⌋ \sum_{i=1}^{h^{\prime}}\left\lfloor\frac{ia}{b}\right\rfloor in [1, Section 2.3], we easily obtain

 | T 1 ​ ( 26, 11, 3) \displaystyle T_{1}(26,11;3) | = 327 338, \displaystyle=\frac{327}{338}, |  |

 | ∑ i = 1 1 ⌊ 26 ​ i 11 ⌋ \displaystyle\sum_{i=1}^{1}\left\lfloor\frac{26\hskip 1.42271pti}{11}\right\rfloor | = 2. \displaystyle=2. |  |

Then using ( 40),

 | T 2 ​ ( 26, 11, 3) + 26 11 ​ T 2 ​ ( 11, 26, 1) = 85 11. T_{2}(26,11;3)+\frac{26}{11}T_{2}(11,26;1)=\frac{85}{11}. |  | (52) |

From ( 41), we get

 | T 2 ​ ( 11, 26, 1) = T 2 ​ ( 11, 4, 1) + 2. T_{2}(11,26;1)=T_{2}(11,4;1)+2. |  | (53) |

It is easy to see that

 | T 2 ​ ( 11, 4, 1) = 0. T_{2}(11,4;1)=0. |  | (54) |

From ( 42) to ( 54), it follows that

 | T 2 ​ ( 8411, 2732, 1221) = ∑ i = 1 1221 i ⁡ ⌊ 2732 ​ i 8411 ⌋ = 196956430. T_{2}(8411,2732;1221)=\sum_{i=1}^{1221}i\left\lfloor\frac{2732\hskip 1.42271pti}{8411}\right\rfloor=196956430. |  | (55) |

Finally, we use ( 38) to calculate T 3 ​ ( 8411, 2732, 1211) T_{3}(8411,2732;1211) from the values of T 1 ​ ( 8411, 2732, 1211) T_{1}(8411,2732;1211) and T 1 ​ ( 8411, 2732, 1211) T_{1}(8411,2732;1211) obtained in ( 37) and ( 55), respectively.

 | T 3 ​ ( 8411, 2732, 1221) \displaystyle T_{3}(8411,2732;1221) | = T 1 ​ ( 8411, 2732, 1221) + 5464 8411 ​ T 2 ​ ( 8411, 2732, 1221) − 348800520350128 5441917 \displaystyle=T_{1}(8411,2732;1221)+\frac{5464}{8411}T_{2}(8411,2732;1221)-\frac{348800520350128}{5441917} |  |

 |  | = 2219247661 5441917 + 5464 8411 × 196956430 − 348800520350128 5441917 \displaystyle=\frac{2219247661}{5441917}+\frac{5464}{8411}\times 196956430-\frac{348800520350128}{5441917} |  |

 |  | = 63853169. \displaystyle=63853169. |  |

That is,

 | T 3 ​ ( 8411, 2732, 1221) = ∑ i = 1 1221 ⌊ 2732 ​ i 8411 ⌋ 2 = 63853169. T_{3}(8411,2732;1221)=\sum_{i=1}^{1221}\left\lfloor\frac{2732\hskip 1.42271pti}{8411}\right\rfloor^{2}=63853169. |  |

## 4 Efficiency of the algorithms

We compare the reciprocity relation in Theorem 6 with that in Theorem 3. The analysis in [1, Section 2.5] shows that S ⁡ ( a, b, h) S(a,b;h) can be calculated in O ⁡ ( log ⁡ t) O(\log t) steps where t = max ⁡ ( a, b) t=\max(a,b). The quantity ∑ i = 1 h ⌊ i ​ b a ⌋ \sum_{i=1}^{h}\left\lfloor\frac{ib}{a}\right\rfloor can also be calculated in O ⁡ ( log ⁡ t) O(\log t) steps, as described in [1, Section 2.5]. Therefore, T 1 ​ ( a, b, h) = ∑ i = 1 h { i ​ b a } 2 T_{1}(a,b;h)=\sum_{i=1}^{h}\{\frac{ib}{a}\}^{2} can be calculated in O ⁡ ( log ⁡ t) O(\log t) steps.

Consider the reciprocity relation for T 2 ​ ( a, b, h) T_{2}(a,b;h) in ( 40). Note that this is similar to the ones above except that in each step, we need to calculate T 1 ​ ( a, b, h) T_{1}(a,b;h) and ∑ i = 1 h ′ ⌊ i ​ a b ⌋ \sum_{i=1}^{h^{\prime}}\left\lfloor\frac{ia}{b}\right\rfloor, both of which require O ⁡ ( log ⁡ t) O(\log t) steps. Thus, in order to calculate T 2 ​ ( a, b, h) T_{2}(a,b;h), we need to apply the reciprocity relation O ⁡ ( log ⁡ t) O(\log t) times and each time, we need to perform O ⁡ ( log ⁡ t) O(\log t) steps. Hence, the number of steps required for calculating T 2 ​ ( a, b, h) = ∑ i = 1 h i ⁡ ⌊ i ​ b a ⌋ T_{2}(a,b;h)=\sum_{i=1}^{h}i\lfloor\frac{ib}{a}\rfloor is O ⁡ ( ( log ⁡ t) 2) O((\log t)^{2}).

The quantity T 3 ​ ( a, b, h) T_{3}(a,b;h) can be obtained from T 1 ​ ( a, b, h) T_{1}(a,b;h) and T 2 ​ ( a, b, h) T_{2}(a,b;h) using ( 38). Therefore, the number of steps required for calculating T 3 ​ ( a, b, h) = ∑ i = 1 h ⌊ i ​ b a ⌋ 2 T_{3}(a,b;h)=\sum_{i=1}^{h}\lfloor\frac{ib}{a}\rfloor^{2} is also O ⁡ ( ( log ⁡ t) 2) O((\log t)^{2}).

## 5 Acknowledgements

I want to thank the Maths Department at SFU for providing me various awards and fellowships which help me conduct my research.

## References

- [1] D. S. Binner, The number of solutions to a ​ x + b ​ y + c ​ z = n ax+by+cz=n and its relation to quadratic residues. Journal of Integer Sequences, 23 (20.6.5), 2020.
- [2] T. C. Brown and P. J. Shiue, A remark related to the Frobenius problem, Fibonacci Quart., 31, 32–36, 1993.
- [3] J. J. Sylvester, On subinvariants, i.e. semi-invariants to binary quantics of an unlimited order, Amer. J. Math. 5, 79–136, 1882.
- [4] J. J. Sylvester, Problem 7382 7382, *Mathematical Questions, with their Solutions, from the Educational Times*41, 21, 1884.
- [5] A. Tripathi, The number of solutions to a ​ x + b ​ y = n ax+by=n, Fibonacci Quart. 38, 290–293, 2000.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
