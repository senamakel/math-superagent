<!-- source: https://arxiv.org/html/1011.6083v4 | converted from HTML -->

On Stephan’s conjectures concerning Pascal triangle modulo 2 and their polynomial generalization

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1011.6083v4 [math.NT] 01 Apr 2012

# On Stephan’s conjectures concerning Pascal triangle modulo 2 and their polynomial generalization

Vladimir Shevelev Address: Department of Mathematics
Ben-Gurion University of the Negev
Beer-Sheva 84105, Israel. e-mail:shevelev@bgu.ac.il

###### Abstract.

We prove a series of Stephan’s conjectures concerning Pascal triangle modulo 2 and give a polynomial generalization.

###### 1991 Mathematics Subject Classification

11B65

## 1. Introduction

Consider Pascal triangle for binomial coefficient modulo 2. If to read every row of this triangle as a binary number, then we obtain the following sequence { c ⁡ ( n) } n ≥ 0 \{c(n)\}_{n\geq 0} (cf. A001317 in [11]):

(1.1) |  | 1, 3, 5, 15, 17, 51, 85, 255, 257, 771, 1285, 3855, 4369, 13107, 21845, … 1,3,5,15,17,51,85,255,257,771,1285,3855,4369,13107,21845,... |  |

It is easy to see that

(1.2) |  | c ( 2 n) ≡ 1 ( mod 4), n = 0, 1, … c(2n)\equiv 1\pmod{4},\enskip n=0,1,... |  |

Denote

(1.3) |  | l ⁡ ( n) = c ⁡ ( 2 ​ n) − 1 4. l(n)=\frac{c(2n)-1}{4}. |  |

In 2004, for sequence { l ⁡ ( n) } n ≥ 0, \{l(n)\}_{n\geq 0}, R. Stephan formulated a series of the following conjectures (cf. his comments to A089893 in [11]):

###### Conjecture 1.

(1.4) |  | l ⁡ ( 2 k) = 2 2 k + 1 − 2. l(2^{k})=2^{2^{k+1}-2}. |  |

###### Conjecture 2.

(1.5) |  | OPEN lim n → ∞ l ⁡ ( 2 ​ n + 1) / l ⁡ ( 2 ​ n)) = 5. \lim_{n\rightarrow\infty}l(2n+1)/l(2n))=5. |  |

###### Conjecture 3.

(1.6) |  | OPEN lim n → ∞ l ⁡ ( 4 ​ n + 2) / l ⁡ ( 4 ​ n + 1)) = 17 / 5. \lim_{n\rightarrow\infty}l(4n+2)/l(4n+1))=17/5. |  |

###### Conjecture 4.

(1.7) |  | OPEN lim n → ∞ l ⁡ ( 8 ​ n + 4) / l ⁡ ( 8 ​ n + 3)) = 257 / 85. \lim_{n\rightarrow\infty}l(8n+4)/l(8n+3))=257/85. |  |

etc.
We add that Moscow PhD student S. Shakirov conjectured (private communication) that a generating function for sequence { c ⁡ ( n) } \{c(n)\} is

(1.8) |  | ∏ k = 0 ∞ ( 1 + x 2 k + ( 2 ​ x) 2 k) = ∑ n = 0 ∞ c ⁡ ( n) ​ x n. \prod_{k=0}^{\infty}(1+x^{2^{k}}+(2x)^{2^{k}})=\sum_{n=0}^{\infty}c(n)x^{n}. |  |

In this paper we prove these conjectures and give a polynomial generalizations.

## 2. On sequence A001317

Consider an infinite in both sides ( 0, 1) (0,1) -sequence with a finite set of 1’s which we call C C -sequence. Removing in it all 0’s before the first 1 and after the last 1, we obtain some odd number which we call the kernel of C C -sequence. Every C C -sequence generates a new C C -sequence, if to write sums of every pair of its adjacent terms modulo 2. If to consider infinite iterations of such process beginning with C C -sequence with kern 1, then we obtain C C -sequences, the kernels { c ⁡ ( i) } i ≥ 0 \{c(i)\}_{i\geq 0} of which form Pascal’s triangle for binomial coefficients modulo 2. Note that, c ⁡ ( 0) = 1 c(0)=1 and c ⁡ ( i) c(i) contains i + 1 i+1 binary digits.
Consider now sequence { d ⁡ ( n) } \{d(n)\} defined by the formula d ⁡ ( 0) = 1; d(0)=1; for n ≥ 1, n\geq 1, if binary expansion of n n is

(2.1) |  | n = ∑ i = 1 m 2 k i, n=\sum_{i=1}^{m}2^{k_{i}}, |  |

then

(2.2) |  | d ⁡ ( n) = ∏ i = 1 m F ⁡ ( k i), d(n)=\prod_{i=1}^{m}F(k_{i}), |  |

where

(2.3) |  | F ⁡ ( n) = 2 2 n + 1, n ≥ 0, F(n)=2^{2^{n}}+1,\enskip n\geq 0, |  |

is Fermat number. Such decomposition of d ⁡ ( n) d(n) we call its Fermat factorization.
From ( 2.1)-( 2.2) immediately follows a generating function for { d ⁡ ( i) }: \{d(i)\}:

(2.4) |  | ∏ k = 0 ∞ ( 1 + F ⁡ ( k) ​ x 2 k) = ∑ n = 0 ∞ d ⁡ ( n) ​ x n, 0 < x < 1 2. \prod_{k=0}^{\infty}(1+F(k)x^{2^{k}})=\sum_{n=0}^{\infty}d(n)x^{n},\enskip 0<x<\frac{1}{2}. |  |

Note that sequence { d ⁡ ( i) } \{d(i)\} possesses the following properties:
1) d ⁡ ( n) d(n) is a binary number with n + 1 ​ ( 0, 1) n+1\enskip(0,1) -digits;
2) numbers { d ⁡ ( i) } \{d(i)\} are 1 and all Fermat numbers or products of distinct Fermat numbers;

3) number of Fermat factors in the product equals to d ⁡ ( n) d(n) is the number of 1’s in the binary expansion of n. n.
4) F ⁡ ( i) F(i) divides d ⁡ ( n), n > 1, d(n),\enskip n>1, if and only if it is a factor in product ( 2.2).
Proofs of these properties is very easy: 1) follows from a simple induction; 2) and 3) follow from the definition; 4) follows from the well known fact (cf., e.g., [12]) that every two Fermat numbers are relatively prime, in view of recursion

(2.5) |  | F ⁡ ( n) = 2 + ∏ i = 0 n − 1 F ⁡ ( i). F(n)=2+\prod_{i=0}^{n-1}F(i). |  |

###### Theorem 1.

For n = 0, 1, …, n=0,1,..., we have

(2.6) |  | c ⁡ ( n) = d ⁡ ( n). c(n)=d(n). |  |

Proof. We use induction, the base of which is c ⁡ ( 0) = d ⁡ ( 0) = 1, c ⁡ ( 1) = d ⁡ ( 1) = 3, c ⁡ ( 2) = d 2 = 5. c(0)=d(0)=1,\enskip c(1)=d(1)=3,\enskip c(2)=d_{2}=5. Suppose that c ⁡ ( i) = d ⁡ ( i), c(i)=d(i), for i ≤ k. i\leq k. Let m m be the most number for which F ⁡ ( m) F(m) divides c ⁡ ( k) = d ⁡ ( k). c(k)=d(k). In non-trivial case, when c ⁡ ( k) ≠ F ⁡ ( m), c(k)\neq F(m), using property 4), for some r < k, r<k, we have c ⁡ ( k) = d ⁡ ( r) ​ F ​ ( m) = c ⁡ ( r) ​ F ​ ( m). c(k)=d(r)F(m)=c(r)F(m). Furthermore, since, by the condition, F ⁡ ( m) F(m) is the most Fermat divisor of c ⁡ ( k) c(k) and, in view of ( 2.5), we have

(2.7) |  | c ⁡ ( r) = c ⁡ ( k) F ⁡ ( m) ≤ ∏ i = 0 m − 1 F ⁡ ( i) = F ⁡ ( m) − 2. c(r)=\frac{c(k)}{F(m)}\leq\prod_{i=0}^{m-1}F(i)=F(m)-2. |  |

Besides, since c ⁡ ( r) < c ⁡ ( k), c(r)<c(k), then, by the inductive supposition,

 | c ⁡ ( r + 1) = d ⁡ ( r + 1). c(r+1)=d(r+1). |  |

Adding the case when c ⁡ ( k) = F ⁡ ( m), c(k)=F(m), let us prove a recursion: c ⁡ ( 0) = 1, c ⁡ ( 1) = 3, c ⁡ ( 2) = 5; c(0)=1,c(1)=3,c(2)=5; for k ≥ 2, k\geq 2,

(2.8) |  | c ⁡ ( k + 1) = { 3 ​ F ​ ( m), i ​ f ​ c ​ ( k) = F ⁡ ( m), F ⁡ ( m + 1), i ​ f ​ 1 < c ⁡ ( r) = F ⁡ ( m) − 2, F ⁡ ( m) ​ c ​ ( r + 1), i ​ f ​ 1 < c ⁡ ( r) < F ⁡ ( m) − 2. c(k+1)=\begin{cases}3F(m),\enskip if\enskip c(k)=F(m),\\ F(m+1),\enskip if\enskip 1<c(r)=F(m)-2,\\ F(m)c(r+1),\enskip if\enskip 1<c(r)<F(m)-2.\end{cases} |  |

Let c ⁡ ( k) = F ⁡ ( m), m ≥ 1. C c(k)=F(m),\enskip m\geq 1.\enskip C -sequence with kernel c ⁡ ( k) c(k) is

 | ...01 ​ 0 ​ … ​ 0 ⏟ 2 m − 1 ​ 10 ​ …...01\underbrace{0...0}_{2^{m}-1}10... |  |

Thus the following C C -sequence with kernel c ⁡ ( k + 1) c(k+1) is

 | ...011 ​ 0 ​ … ​ 0 ⏟ 2 m − 2 ​ 110 ​ …...011\underbrace{0...0}_{2^{m}-2}110... |  |

Comparing kernels c ⁡ ( k) c(k) and c ⁡ ( k + 1), c(k+1), we conclude that c ⁡ ( k + 1) = 3 ​ c ​ ( k) = 3 ​ F ​ ( m). c(k+1)=3c(k)=3F(m).

Furthermore, if c ⁡ ( r) = F ⁡ ( m) − 2, c(r)=F(m)-2, then, by ( 2.7), we have

 | c ⁡ ( k) = F ⁡ ( m) ​ c ​ ( r) = F ⁡ ( m) ​ ( F ⁡ ( m) − 2) = F ⁡ ( m + 1) − 2 = 11 ​ … ​ 1 ⏟ 2 m + 1. c(k)=F(m)c(r)=F(m)(F(m)-2)=F(m+1)-2=\underbrace{11...1}_{2^{m+1}}. |  |

Thus the C C -sequence with kernel c ⁡ ( k) c(k) is

 | ...0 ​ 11 ​ … ​ 1 ⏟ 2 m + 1 ​ 0 ​ …...0\underbrace{11...1}_{2^{m+1}}0... |  |

Therefore, by the definition, the C C -sequence with kernel c ⁡ ( k + 1) c(k+1) is

 | ...01 ​ 0 ​ … ​ 0 ⏟ 2 m + 1 − 1 ​ 10 ​ …...01\underbrace{0...0}_{2^{m+1}-1}10... |  |

and we see that c ⁡ ( k + 1) = F ⁡ ( m + 1). c(k+1)=F(m+1).
Let now c ⁡ ( r) < F ⁡ ( m) − 2. c(r)<F(m)-2. Since, by the supposition of induction, c ⁡ ( r) = d ⁡ ( r). c(r)=d(r). Therefore, c ⁡ ( r) c(r) is a product of Fermat numbers and

 | c ⁡ ( r) ≤ ∏ i = 0 m − 1 F ⁡ ( i) F ⁡ ( 0) = F ⁡ ( m) − 2 F ⁡ ( 0). c(r)\leq\frac{\prod_{i=0}^{m-1}F(i)}{F(0)}=\frac{F(m)-2}{F(0)}. |  |

Hence, c ⁡ ( r) c(r) is not more than ( 2 m − 1) (2^{m}-1) -digits odd binary number. Since

 | c ⁡ ( k) = F ⁡ ( m) ​ c ​ ( r) = 2 2 m ​ c ​ ( r) + c ⁡ ( r), c(k)=F(m)c(r)=2^{2^{m}}c(r)+c(r), |  |

then c ⁡ ( k) c(k) has the binary expansion of the form

(2.9) |  | c ⁡ ( k) = c ⁡ ( r) ​ 0 ​ … ​ 0 ⏟ l ​ c ​ ( r) ¯, c(k)=\overline{c(r)\underbrace{0...0}_{l}c(r)}, |  |

where l ≥ 1. l\geq 1.
Passing on to the following kernel, we have:

 | c ⁡ ( k + 1) = c ⁡ ( r + 1) ​ 0 ​ … ​ 0 ⏟ l − 1 ​ c ​ ( r + 1) ¯, c(k+1)=\overline{c(r+1)\underbrace{0...0}_{l-1}c(r+1)}, |  |

where l − 1 ≥ 0. l-1\geq 0. Thus

 | c ⁡ ( k + 1) = c ⁡ ( r + 1) ​ 2 2 m + c ⁡ ( r + 1) = c ⁡ ( r + 1) ​ F ​ ( m). c(k+1)=c(r+1)2^{2^{m}}+c(r+1)=c(r+1)F(m). |  |

This completes formula ( 2.8). From this formula we conclude that c ⁡ ( k + 1) c(k+1) is a term of sequence { d ⁡ ( i) }. \{d(i)\}. Moreover, since c ⁡ ( k + 1) c(k+1) contains k + 2 k+2 binary digits, then, in view of property 1) of numbers { d ⁡ ( i) }, \{d(i)\}, both of c ⁡ ( k + 1) c(k+1) and d ⁡ ( k + 1) d(k+1) contain ( k + 2) (k+2) binary digits. Therefore, c ⁡ ( k + 1) = d ⁡ ( k + 1). ■ c(k+1)=d(k+1).\blacksquare

###### Remark 1.

In proof of Theorem 1 we essentially followed to our arguments from preprint [9], 1991. 1991.

###### Remark 2.

Hewgill [4], for the first time, found a relationship between Pascal’s triangle modulo 2 2 and Fermat numbers. In fact, using a simple induction, he proved the following explicit formula for the binary representation of c n c_{n}:

 | c n = ( ∏ i = 0 ⌊ log 2 ⁡ n ⌋ F i ( ⌊ n 2 i ⌋ ( mod 2))) 2. c_{n}=(\prod_{i=0}^{\lfloor\log_{2}n\rfloor}F_{i}^{(\lfloor\frac{n}{2^{i}}\rfloor\pmod{2})})_{2}. |  |

###### Remark 3.

Karttunen [6] gave a representation of c n c_{n} in the Fibonacci number system.

###### Corollary 1.

Conjectural generating formula ( 1.8) (\ref{1.8}) is true.

Proof. According to ( 2.4) and Theorem 1, we have

(2.10) |  | ∏ k = 0 ∞ ( 1 + F ⁡ ( k) ​ x 2 k) = ∑ n = 0 ∞ c ⁡ ( n) ​ x n, 0 < x < 1 2. \prod_{k=0}^{\infty}(1+F(k)x^{2^{k}})=\sum_{n=0}^{\infty}c(n)x^{n},\enskip 0<x<\frac{1}{2}. |  |

It is left to note that

 | 1 + F ⁡ ( k) ​ x 2 k = 1 + x 2 k + ( 2 ​ x) 2 k. ■ 1+F(k)x^{2^{k}}=1+x^{2^{k}}+(2x)^{2^{k}}.\blacksquare |  |

Denote s ⁡ ( n) s(n) the number of 1’s in the binary expansion of n. n.

###### Corollary 2.

OPEN a) a) Number of factors in Fermat factorization of c ⁡ ( n) c(n) is s ⁡ ( n). s(n).
𝑂𝑃𝐸𝑁 b) b) Moreover, the following formula holds

(2.11) |  | s ⁡ ( c ⁡ ( n)) = 2 s ⁡ ( n). s(c(n))=2^{s(n)}. |  |

Proof. a) follows from Theorem 1 and property 3) of numbers { d ⁡ ( n) }. \{d(n)\}.
b) Let, firstly, c ⁡ ( k) c(k) be not a Fermat number and, as in proof of Theorem 1, m m be the most number for which F ⁡ ( m) F(m) divides c ⁡ ( k), c(k), such that c ⁡ ( k) = F ⁡ ( m) ​ c ​ ( r). c(k)=F(m)c(r). Since the difference between numbers of factors in Fermat factorization of c ⁡ ( k) c(k) and c ⁡ ( r) c(r) is 1, then, according to a), we have

 | s ⁡ ( k) = s ⁡ ( r) + 1. s(k)=s(r)+1. |  |

Now we use induction. If the statement is true for i ≤ k − 1, i\leq k-1, then, in particular, s ⁡ ( c ⁡ ( r)) = 2 s ⁡ ( r). s(c(r))=2^{s(r)}. Therefore, by ( 2.9), we have

 | s ⁡ ( c ⁡ ( k)) = 2 ​ s ​ ( c ⁡ ( r)) = 2 ⋅ 2 s ⁡ ( r) = 2 s ⁡ ( r) + 1 = 2 s ⁡ ( k). s(c(k))=2s(c(r))=2\cdot 2^{s(r)}=2^{s(r)+1}=2^{s(k)}. |  |

It is left to consider case c ⁡ ( k) = F ⁡ ( l). c(k)=F(l). Here, by a), s ⁡ ( k) = 1 s(k)=1 and ( 2.9) satisfies trivially. ■ \blacksquare
Note that point b) of Corollary 2 means that the number of odd binomial coefficient in n n -th row of Pascal triangle is 2 s ⁡ ( n). 2^{s(n)}. It is known result of J.Glaisher [2]. His proof was based on well known Lucas (1878) comparison modulo 2: if the binary representations of numbers m ≥ t m\geq t are m = m 1 ​ … ​ m k ¯, t = t 1 ​ … ​ t k ¯ m=\overline{m_{1}...m_{k}},\enskip t=\overline{t_{1}...t_{k}} (with, probably, some first t i = 0 t_{i}=0), then

 | ( n t) ≡ ∏ i = 0 m ( n i t i) ( mod 2). \binom{n}{t}\equiv\prod_{i=0}^{m}\binom{n_{i}}{t_{i}}\pmod{2}. |  |

In [3] A.Granville gives a new interesting proof of Glaisher’s result. Our proof is the third one. Generalizations in other directs see in [1], [3], [5], [8], [10].

###### Corollary 3.

If F ⁡ ( m) F(m) is the most Fermat divisor of numbers c ⁡ ( k − 1) c(k-1) and c ⁡ ( l − 1) c(l-1) from interval ( 1, F ⁡ ( m) − 2), (1,\enskip F(m)-2), then

(2.12) |  | c ⁡ ( k − 1) ​ c ​ ( l) = c ⁡ ( l − 1) ​ c ​ ( k). c(k-1)c(l)=c(l-1)c(k). |  |

Proof. Using ( 2.8), we have

 | c ⁡ ( k) = c ⁡ ( k − 1) ​ F ​ ( m), c ⁡ ( l) = c ⁡ ( l − 1) ​ F ​ ( m) c(k)=c(k-1)F(m),\enskip c(l)=c(l-1)F(m) |  |

and ( 2.12) follows. ■ \blacksquare

###### Corollary 4.

If k = 2 m ​ l + 2 m − 1, m ≥ 1, k=2^{m}l+2^{m-1},\enskip m\geq 1, then

(2.13) |  | c ⁡ ( k) = c ⁡ ( 2 m ​ l) ​ F ​ ( m − 1). c(k)=c(2^{m}l)F(m-1). |  |

Proof. From ( 2.1)-( 2.2), we immediately have d ⁡ ( k) = d ⁡ ( 2 m ​ l) ​ F ​ ( m − 1), d(k)=d(2^{m}l)F(m-1), and ( 2.13) follows from Theorem 1. ■ \blacksquare

## 3. Proof of Conjecture 1

Now proof of Conjecture 1 is especially simple. Indeed, in view of ( 1.3) and ( 2.3), formula ( 1.4) of Conjecture 1 can be rewritten as

(3.1) |  | c ⁡ ( 2 n) = F ⁡ ( n), c(2^{n})=F(n), |  |

where n = k + 1 ≥ 1. n=k+1\geq 1.
According to Corollary 1 OPEN a), a), number c ⁡ ( 2 n) c(2^{n}) has only one Fermat factor, i.e., for some t, t, we have c ⁡ ( 2 n) = F t. c(2^{n})=F_{t}. Besides, by the definition, c ⁡ ( 2 n) c(2^{n}) has 2 n + 1 2^{n}+1 binary digits. It is left to notice that, the unique Fermat number having 2 n + 1 2^{n}+1 binary digits is F ⁡ ( n), F(n), i.e., t = n t=n and c ⁡ ( 2 n) = F ⁡ ( n). ■ c(2^{n})=F(n).\blacksquare
In addition, prove that

(3.2) |  | c ⁡ ( 2 n − 1) = F ⁡ ( n) − 2. c(2^{n}-1)=F(n)-2. |  |

Indeed, by the definition of sequence { d ⁡ ( n) } \{d(n)\} and ( 2.3), we conclude that F ⁡ ( n) − 2, F(n)-2, as a product of distinct Fermat numbers, is a term of sequence { d ⁡ ( i) } \{d(i)\} and thus, by Theorem 1, is a term of sequence { c ⁡ ( i) }. \{c(i)\}. Now it is left to notice that numbers c ⁡ ( 2 n − 1) c(2^{n}-1) and F ⁡ ( n) − 2 F(n)-2 have the same number ( 2 n) (2^{n}) of binary digits. ■ \blacksquare

## 4. Proof of Conjectures 2, 3, 4, e ​ t ​ c. etc.

###### Lemma 1.

For every n ≥ 0, t ≥ 1 n\geq 0,\enskip t\geq 1 we have identity

(4.1) |  | ( F ⁡ ( t − 1) − 2) ​ c ​ ( 2 t ​ n) = c ⁡ ( 2 t ​ n + 2 t − 1 − 1). (F(t-1)-2)c(2^{t}n)=c(2^{t}n+2^{t-1}-1). |  |

Proof. As in proof of ( 3.2), we conclude that ( F ⁡ ( t − 1) − 2) ​ c ​ ( 2 t ​ n) (F(t-1)-2)c(2^{t}n) is a term of sequence { c ⁡ ( i) }. \{c(i)\}. Note that number c ⁡ ( 2 t ​ n + 2 t − 1 − 1) c(2^{t}n+2^{t-1}-1) has 2 t ​ n + 2 t − 1 2^{t}n+2^{t-1} binary digits. Besides, number F ⁡ ( t − 1) − 2 = 1 ​ … ​ 1 ⏟ 2 t − 1 F(t-1)-2=\underbrace{1...1}_{2^{t-1}} and c ⁡ ( 2 t ​ n) c(2^{t}n) has 2 t ​ n + 1 2^{t}n+1 binary digits. Therefore, number ( F ⁡ ( t − 1) − 2) ​ c ​ ( 2 t ​ n) (F(t-1)-2)c(2^{t}n) contains not less binary digits than number 1 ​ … ​ 1 ⏟ 2 t − 1 ​ 0 ​ … ​ 0 ⏟ 2 t ​ n, \underbrace{1...1}_{2^{t-1}}\underbrace{0...0}_{2^{t}n}, i.e. ( F ⁡ ( t − 1) − 2) ​ c ​ ( 2 t ​ n) (F(t-1)-2)c(2^{t}n) has not less than 2 t − 1 + 2 t ​ n 2^{t-1}+2^{t}n binary digits. On the other hand, ( F ⁡ ( t − 1) − 2) ​ c ​ ( 2 t ​ n) (F(t-1)-2)c(2^{t}n) contains not more binary digits than number

 | 1 ​ … ​ 1 ⏟ 2 t − 1 ​ 1 ​ … ​ 1 ⏟ 2 t ​ n = ( 2 2 t − 1 − 1) ​ ( 2 2 t ​ n − 1) ≤ 2 2 t − 1 + 2 t ​ n − 1, \underbrace{1...1}_{2^{t-1}}\underbrace{1...1}_{2^{t}n}=(2^{2^{t-1}}-1)(2^{2^{t}n}-1)\leq 2^{2^{t-1}+2^{t}n}-1, |  |

i.e., ( F ⁡ ( t − 1) − 2) ​ c ​ ( 2 t ​ n) (F(t-1)-2)c(2^{t}n) has not more than 2 t − 1 + 2 t ​ n 2^{t-1}+2^{t}n binary digits. Thus number ( F ⁡ ( t − 1) − 2) ​ c ​ ( 2 t ​ n) (F(t-1)-2)c(2^{t}n) has exactly 2 t − 1 + 2 t ​ n 2^{t-1}+2^{t}n binary digits. Consequently, two terms ( F ⁡ ( t − 1) − 2) ​ c ​ ( 2 t ​ n) (F(t-1)-2)c(2^{t}n) and c ⁡ ( 2 t ​ n + 2 t − 1 − 1) c(2^{t}n+2^{t-1}-1) of sequence { c ⁡ ( i) } \{c(i)\} has the same number of digits. Therefore, equality ( 4.1) holds. ■ \blacksquare

###### Lemma 2.

For every n ≥ 0, t ≥ 1, n\geq 0,\enskip t\geq 1, we have identities

(4.2) |  | ( F ⁡ ( t − 1) − 2) ​ c ​ ( 2 t ​ n + 2 t − 1) = F ⁡ ( t − 1) ​ c ​ ( 2 t ​ n + 2 t − 1 − 1), (F(t-1)-2)c(2^{t}n+2^{t-1})=F(t-1)c(2^{t}n+2^{t-1}-1), |  |

(4.3) |  | ( F ⁡ ( t − 1) − 2) ​ c ​ ( 2 t ​ n + 2 t − 1) = 3 ​ F ​ ( t − 1) ​ c ​ ( 2 t ​ n + 2 t − 1 − 2). (F(t-1)-2)c(2^{t}n+2^{t-1})=3F(t-1)c(2^{t}n+2^{t-1}-2). |  |

Proof. Multiplying ( 4.1) by F ⁡ ( t − 1) F(t-1) and using formula ( 2.13) of Corollary 4 (for l = n l=n and m = t m=t), we obtain ( 4.2). Furthermore, if to take in Corollary 4 m = 1, l = 2 t − 1 ​ n + 2 t − 2 − 1, m=1,\enskip l=2^{t-1}n+2^{t-2}-1, then, in view of F ⁡ ( 0) = 3, F(0)=3, we have c ⁡ ( 2 t ​ n + 2 t − 1 − 1) = 3 ​ c ​ ( 2 t ​ n + 2 t − 1 − 2), c(2^{t}n+2^{t-1}-1)=3c(2^{t}n+2^{t-1}-2), and ( 4.3) follows. ■ \blacksquare

Now we are able to get a proof of Conjectures 2, 3, 4, e ​ t ​ c. etc. According to ( 1.3), we have

(4.4) |  | c ⁡ ( 2 ​ n) = 4 ​ l ​ ( n) + 1. c(2n)=4l(n)+1. |  |

Let in ( 4.3) t ≥ 2. t\geq 2. Then, by ( 4.4), we have

 | ( F ⁡ ( t − 1) − 2) ​ ( 4 ​ l ​ ( 2 t − 1 ​ n + 2 t − 2) + 1) = 3 ​ F ​ ( t − 1) ​ ( 4 ​ l ​ ( 2 t − 1 ​ n + 2 t − 2 − 1) + 1), (F(t-1)-2)(4l(2^{t-1}n+2^{t-2})+1)=3F(t-1)(4l(2^{t-1}n+2^{t-2}-1)+1), |  |

or

 | 4 ​ l ​ ( 2 t − 1 ​ n + 2 t − 2) + 1 4 ​ l ​ ( 2 t − 1 ​ n + 2 t − 2 − 1) + 1 = 3 ​ F ​ ( t − 1) F ⁡ ( t − 1) − 2. \frac{4l(2^{t-1}n+2^{t-2})+1}{4l(2^{t-1}n+2^{t-2}-1)+1}=\frac{3F(t-1)}{F(t-1)-2}. |  |

Hence, we finally find

(4.5) |  | lim n → ∞ l ⁡ ( 2 t − 1 ​ n + 2 t − 2) l ⁡ ( 2 t − 1 ​ n + 2 t − 2 − 1) = 3 ​ F ​ ( t − 1) F ⁡ ( t − 1) − 2. \lim_{n\rightarrow\infty}\frac{l(2^{t-1}n+2^{t-2})}{l(2^{t-1}n+2^{t-2}-1)}=\frac{3F(t-1)}{F(t-1)-2}. |  |

■ \blacksquare

So, if t = 2, 3, 4, 5, …, t=2,3,4,5,..., then the right hand side is

 | 3 ⋅ 5 5 − 2 = 5, 3 ⋅ 17 17 − 2 = 17 5, 3 ⋅ 257 257 − 2 = 257 85, 3 ⋅ 65537 65537 − 2 = 65537 21845, … \frac{3\cdot 5}{5-2}=5,\enskip\frac{3\cdot{17}}{17-2}=\frac{17}{5},\enskip\frac{3\cdot{257}}{257-2}=\frac{257}{85},\enskip\frac{3\cdot{65537}}{65537-2}=\frac{65537}{21845},... |  |

respectively.

## 5. Second proof of key identity ( 4.3) based on notion of orthogonality of nonnegative integers

We can essentially simplify our proof of Stephan’s conjectures by a simplification of key identity ( 4.3). Put to every nonnegative integer n n to one-to-one correspondence ( 0, 1) (0,1) -vector n ¯ \overline{n} by the rule: if the binary expansion of n n is n = n 1 ​ … ​ n m ¯, n=\overline{n_{1}...n_{m}}, then

(5.1) |  | n ¯ =...0 ​ … ​ 0 ​ n 1 ​ … ​ n m ¯ \overline{n}=\overline{...0...0n_{1}...n_{m}} |  |

with infinitive 0’s before n 1. n_{1}. For two integers u ≤ v u\leq v with vectors u ¯ =...0 ​ … ​ 0 ​ u 1 ​ … ​ u l ¯ \overline{u}=\overline{...0...0u_{1}...u_{l}} and v ¯ =...0 ​ … ​ 0 ​ v 1 ​ … ​ v m ¯, l ≤ m \overline{v}=\overline{...0...0v_{1}...v_{m}},\enskip l\leq m introduce ”circ-product” by formula ( which is, for the corresponding vectors, similar to dot-product)

(5.2) |  | u ∘ v = u ¯ ​ v ¯ = u l ​ v m + u l − 1 ​ v m − 1 + … + u 1 ​ v m − l + 1. u\circ v=\overline{u}\overline{v}=u_{l}v_{m}+u_{l-1}v_{m-1}+...+u_{1}v_{m-l+1}. |  |

###### Definition 1.

We call two non-negative integers u, v u,\enskip v mutually orthogonal ( u ⊥ v), (u\bot v), if u ∘ v = 0. u\circ v=0.

Note that if ( u ⊥ v), (u\bot v), then the sets of positions of 1’s in their binary representations do not intersect.

An important source for obtaining various identities for numbers { c ⁡ ( n) } \{c(n)\} is the following exponential-like ”addition theorem”.

###### Lemma 3.

If n 1 ⊥ n 2, n_{1}\bot n_{2}, then

(5.3) |  | c ⁡ ( n 1 + n 2) = c ⁡ ( n 1) ​ c ​ ( n 2). c(n_{1}+n_{2})=c(n_{1})c(n_{2}). |  |

Proof. Let n 1 ≥ n 2 n_{1}\geq n_{2} and the binary expansions of n 1 n_{1} and n 2 n_{2} be n 1 = ∑ i = 1 m 2 k i n_{1}=\sum_{i=1}^{m}2^{k_{i}} and n 2 = ∑ j = 1 m 2 l j n_{2}=\sum_{j=1}^{m}2^{l_{j}} (with, probably, some first l i = 0 l_{i}=0). Since n 1 ⊥ n 2, n_{1}\bot n_{2}, then k i ≠ l j, i, j = 1, …, m. k_{i}\neq l_{j},\enskip i,j=1,...,m. Thus the binary expansion of n 1 + n 2 n_{1}+n_{2} is ∑ i = 1 m 2 k i + ∑ j = 1 m 2 l j. \sum_{i=1}^{m}2^{k_{i}}+\sum_{j=1}^{m}2^{l_{j}}. Therefore, according to ( 2.1)-( 2.2), we have

 | c ⁡ ( n 1 + n 2) = ( ∏ i = 1 m F ⁡ ( k i)) ​ ( ∏ j = 1 m F ⁡ ( l j)) = c ⁡ ( n 1) ​ c ​ ( n 2). ■ c(n_{1}+n_{2})=(\prod_{i=1}^{m}F(k_{i}))(\prod_{j=1}^{m}F(l_{j}))=c(n_{1})c(n_{2}).\blacksquare |  |

Second proof of ( 4.3).
a)Using the notion of numbers orthogonality, we immediately obtain formula ( 4.2) by the following way.
By ( 3.2), we have

(5.4) |  | F ⁡ ( t − 1) − 2 = c ⁡ ( 2 t − 1 − 1). F(t-1)-2=c(2^{t-1}-1). |  |

Since, evidently, ( 2 t − 1 − 1) ⊥ ( 2 t ​ n + 2 t − 1), (2^{t-1}-1)\bot(2^{t}n+2^{t-1}), then, using (5.3)-(5.4), we find

 | ( F ⁡ ( t − 1) − 2) ​ c ​ ( 2 t ​ n + 2 t − 1) = c ⁡ ( 2 t ​ n + 2 t − 1 + 2 t − 1 − 1) = c ⁡ ( 2 t ​ n + 2 t − 1). (F(t-1)-2)c(2^{t}n+2^{t-1})=c(2^{t}n+2^{t-1}+2^{t-1}-1)=c(2^{t}n+2^{t}-1). |  |

On the other hand, since 2 t − 1 ⊥ ( 2 t ​ n + 2 t − 1 − 1), 2^{t-1}\bot(2^{t}n+2^{t-1}-1), then

 | F ⁡ ( t − 1) ​ c ​ ( 2 t ​ n + 2 t − 1 − 1) = c ⁡ ( 2 t − 1) ​ c ​ ( 2 t ​ n + 2 t − 1 − 1) = c ⁡ ( 2 t ​ n + 2 t − 1). F(t-1)c(2^{t}n+2^{t-1}-1)=c(2^{t-1})c(2^{t}n+2^{t-1}-1)=c(2^{t}n+2^{t}-1). |  |

Thus we conclude that ( 4.2) holds.
b) Note now that, 1 ⊥ 2 t ​ n + 2 t − 2. 1\bot 2^{t}n+2^{t}-2. Thus 3 ​ c ​ ( 2 t ​ n + 2 t − 1 − 2) = c ⁡ ( 2 t ​ n + 2 t − 1 − 1) 3c(2^{t}n+2^{t-1}-2)=c(2^{t}n+2^{t-1}-1) and ( 4.3) follows as well. ■ \blacksquare
Further we consider a polynomial generalization.

## 6. Polynomials p n ​ ( z), q n ​ ( z) p_{n}(z),\enskip q_{n}(z) and their properties

Consider sequence of polynomials (cf. [3])

(6.1) |  | p n ( z) = 1 2 ∑ i = 0 n ( 1 − ( − 1) ( n i)) z i, n = 0, 1, …, z ∈ ℂ, p_{n}(z)=\frac{1}{2}\sum_{i=0}^{n}(1-(-1)^{\binom{n}{i}})z^{i},\enskip n=0,1,...,\enskip z\in\mathbb{C}, |  |

such that

(6.2) |  | p n ​ ( 0) = 1, p n ​ ( 1) = 2 s ⁡ ( n), p n ​ ( 2) = c ⁡ ( n). p_{n}(0)=1,\enskip p_{n}(1)=2^{s(n)},\enskip p_{n}(2)=c(n). |  |

The second equality we have in view of ( 2.9).
By the same way, one can prove a generalization of Theorem 1.

###### Theorem 2.

For n ≥ 1, n\geq 1, we have the following decomposition of p n ​ ( z): p_{n}(z):

(6.3) |  | p n ​ ( z) = ∏ i = 0 m ( z 2 k i + 1), p_{n}(z)=\prod_{i=0}^{m}(z^{2^{k_{i}}}+1), |  |

if the binary expansion of n n is

(6.4) |  | n = ∑ i = 0 m 2 k i. n=\sum_{i=0}^{m}2^{k_{i}}. |  |

Thus a generating function for polynomials { p n ​ ( z) } \{p_{n}(z)\} is

(6.5) |  | ∏ k = 0 ∞ ( 1 + ( z 2 k + 1) ​ x 2 k) = ∑ n = 0 ∞ p n ​ ( z) ​ x n, 0 < x < 1 | z |. \prod_{k=0}^{\infty}(1+(z^{2^{k}}+1)x^{2^{k}})=\sum_{n=0}^{\infty}p_{n}(z)x^{n},\enskip 0<x<\frac{1}{|z|}. |  |

In particular, we have

(6.6) |  | p 2 n ​ ( z) = z 2 n + 1. p_{2^{n}}(z)=z^{2^{n}}+1. |  |

Note that, if n n has binary expansion ( 6.4), then 2 ​ n = ∑ i = 0 m 2 k i + 1. 2n=\sum_{i=0}^{m}2^{k_{i}+1}. Since z 2 k i + 1 = ( z 2) 2 k i, z^{2^{k_{i}+1}}=(z^{2})^{2^{k_{i}}}, then we have

(6.7) |  | p 2 ​ n ​ ( z) = ∏ i = 0 m ( ( z 2) 2 k i + 1) = p n ​ ( z 2). p_{2n}(z)=\prod_{i=0}^{m}((z^{2})^{2^{k_{i}}}+1)=p_{n}(z^{2}). |  |

Analogously, since 2 ​ n + 1 = 1 + ∑ i = 0 m 2 k i + 1, 2n+1=1+\sum_{i=0}^{m}2^{k_{i}+1}, then

(6.8) |  | p 2 ​ n + 1 ​ ( z) = ( z + 1) ​ ∏ i = 0 m ( ( z 2) 2 k i + 1) = ( z + 1) ​ p n ​ ( z 2). p_{2n+1}(z)=(z+1)\prod_{i=0}^{m}((z^{2})^{2^{k_{i}}}+1)=(z+1)p_{n}(z^{2}). |  |

Formulas ( 6.7)-( 6.8) give a simple recursion for polynomials { p n ​ ( z) }, \{p_{n}(z)\}, which recently were obtained by S. Northshield (cf. [7], Lemma 3.1) in a quite another way.
Note that every two different polynomials in sequence { p 2 i ( z) = z 2 i + 1 } i ≥ 0 \{p_{2^{i}}(z)=z^{2^{i}}+1\}_{i\geq 0} are respectively prime. It follows from the identity

(6.9) |  | p 2 n ​ ( z) = 2 + ( z − 1) ​ ∏ i = 0 n − 1 p 2 i ​ ( z). p_{2^{n}}(z)=2+(z-1)\prod_{i=0}^{n-1}p_{2^{i}}(z). |  |

Put

(6.10) |  | F n ​ ( z) = p 2 n ​ ( z) = z 2 n + 1. F_{n}(z)=p_{2^{n}}(z)=z^{2^{n}}+1. |  |

The following identity holds (cf. [9])

(6.11) |  | ∑ n = 0 ∞ 1 p n ​ ( z) s = ∏ k = 0 ∞ ( 1 + F k ​ ( z) − s), | z | > 1, ℜ ⁡ s > 0. \sum_{n=0}^{\infty}\frac{1}{p_{n}(z)^{s}}=\prod_{k=0}^{\infty}(1+F_{k}(z)^{-s}),\enskip|z|>1,\enskip\Re{s}>0. |  |

In particular, for z = 2, s = 1, z=2,\enskip s=1, we have

(6.12) |  | ∑ n = 0 ∞ 1 c ⁡ ( n) = ∏ k = 0 ∞ ( 1 + F k − 1) = 1.700735495 ​ …. \sum_{n=0}^{\infty}\frac{1}{c(n)}=\prod_{k=0}^{\infty}(1+F_{k}^{-1})=1.700735495...\enskip. |  |

According to Theorem 2 and in view that s ⁡ ( n) ≡ m n ( mod 2), s(n)\equiv m_{n}\pmod{2}, where m n = 0, 1, 1, 0, 1, 0, 0, 1, 1 ​ … {m_{n}}={0,1,1,0,1,0,0,1,1...} is Thou-Morse sequence, together with ( 6.11), we have also

(6.13) |  | ∑ n = 0 ∞ ( − 1) m n p n ​ ( z) s = ∏ k = 0 ∞ ( 1 − F k ​ ( z) − s), | z | > 1, ℜ ⁡ s > 0. \sum_{n=0}^{\infty}\frac{(-1)^{m_{n}}}{p_{n}(z)^{s}}=\prod_{k=0}^{\infty}(1-F_{k}(z)^{-s}),\enskip|z|>1,\enskip\Re{s}>0. |  |

Let us show that, in particular, for s = 1, s=1, we have

(6.14) |  | ∑ n = 0 ∞ ( − 1) m n p n ​ ( z) = 1 − 1 z, | z | > 1. \sum_{n=0}^{\infty}\frac{(-1)^{m_{n}}}{p_{n}(z)}=1-\frac{1}{z},\enskip|z|>1. |  |

Indeed, since

 | 1 − 1 F n ​ ( z) = ( 1 + 1 z 2 n) − 1, 1-\frac{1}{F_{n}(z)}=(1+\frac{1}{z^{2^{n}}})^{-1}, |  |

then

 | ∏ k = 0 ∞ ( 1 − F k ​ ( z) − 1) = ∏ k = 0 ∞ ( 1 + 1 z 2 n) − 1 \prod_{k=0}^{\infty}(1-F_{k}(z)^{-1})=\prod_{k=0}^{\infty}(1+\frac{1}{z^{2^{n}}})^{-1} |  |

and it is left to note that

(6.15) |  | ∏ n = 0 ∞ ( 1 + 1 z 2 n) = 1 − 1 z. \prod_{n=0}^{\infty}(1+\frac{1}{z^{2^{n}}})=1-\frac{1}{z}. |  |

In particular, together with ( 6.12), for z = 2, z=2, we find

(6.16) |  | ∑ n = 0 ∞ ( − 1) m n c ⁡ ( n) = 1 2. \sum_{n=0}^{\infty}\frac{(-1)^{m_{n}}}{c(n)}=\frac{1}{2}. |  |

In addition, note that, if to consider all different finite products of not necessarily distinct polynomials from sequence { p n ​ ( z) }, \{p_{n}(z)\}, then we obtain a sequence of polynomials q n ​ ( z): q_{n}(z):

 | q 0 ​ ( z) = 1, q 1 ​ ( z) = z + 1, q 2 ​ ( z) = z 2 + 1, q 3 ​ ( z) = ( z + 1) 2, q_{0}(z)=1,\enskip q_{1}(z)=z+1,\enskip q_{2}(z)=z^{2}+1,\enskip q_{3}(z)=(z+1)^{2}, |  |

(6.17) |  | q 4 ​ ( z) = ( z + 1) ​ ( z 2 + 1), q 5 ​ ( z) = z 4 + 1, q 6 ​ ( z) = ( z 2 + 1) 2. q_{4}(z)=(z+1)(z^{2}+1),\enskip q_{5}(z)=z^{4}+1,\enskip q_{6}(z)=(z^{2}+1)^{2}. |  |

For these polynomials, together with ( 6.11), we have the following analog of Euler identity for primes:

(6.18) |  | ∏ F ∈ F ⁡ ( z) ( 1 − F − s) − 1 = ∑ n = 0 ∞ 1 OPEN q n ​ ( z)) s, | z | > 1, ℜ ⁡ s > 0, \prod_{F\in F(z)}(1-F^{-s})^{-1}=\sum_{n=0}^{\infty}\frac{1}{q_{n}(z))^{s}},\enskip|z|>1,\enskip\Re{s}>0, |  |

where

 | F ⁡ ( z) = { F n ​ ( z) } n ≥ 0. F(z)=\{F_{n}(z)\}_{n\geq 0}. |  |

In particular, for s = 1, s=1, using ( 6.15), we have

 | ∑ n = 0 ∞ 1 q n ​ ( z) = ∏ F ∈ F ⁡ ( z) ( 1 − F − 1) − 1 = \sum_{n=0}^{\infty}\frac{1}{q_{n}(z)}=\prod_{F\in F(z)}(1-F^{-1})^{-1}= |  |

(6.19) |  | ∏ n = 0 ∞ ( 1 + 1 z 2 n) − 1 = z z − 1, | z | > 1. \prod_{n=0}^{\infty}(1+\frac{1}{z^{2^{n}}})^{-1}=\frac{z}{z-1},\enskip|z|>1. |  |

Furthermore, introducing an analog of Möbius function

(6.20) |  | ν ⁡ ( n) = { ( − 1) m n, i ​ f ​ n ​ i ​ s ​ s ​ q ​ u ​ a ​ r ​ e ​ f ​ r ​ e ​ e, 0, o ​ t ​ h ​ e ​ r ​ w ​ i ​ s ​ e, \nu(n)=\begin{cases}(-1)^{m_{n}},\;\;if\;\;n\enskip is\enskip squarefree,\\ 0,\;\;otherwise,\end{cases} |  |

we get

(6.21) |  | ∑ n = 0 ∞ ν ⁡ ( n) q n ​ ( z) s = ∏ F ∈ F ⁡ ( z) ( 1 − F − s), | z | > 1, ℜ ⁡ s > 0. \sum_{n=0}^{\infty}\frac{\nu(n)}{q_{n}(z)^{s}}=\prod_{F\in F(z)}(1-F^{-s}),\enskip|z|>1,\enskip\Re{s}>0. |  |

In particular, for s = 1, s=1, we have

(6.22) |  | ∑ n = 0 ∞ ν ⁡ ( n) q n ​ ( z) = 1 − 1 z, | z | > 1. \sum_{n=0}^{\infty}\frac{\nu(n)}{q_{n}(z)}=1-\frac{1}{z},\enskip|z|>1. |  |

## 7. Polynomial generalization of Stephan’s relations

Now we consider a polynomial generalization of formulas of the previous sections which leads us to the corresponding generalization of Stephan’s relations. Since proof of the generalized formulas is quite analogous, then we restrict ourself only by writing of the chain of them. For | z | > 1, |z|>1, we have

(7.1) |  | p 2 n − 1 = F n ​ ( z) − 2 z − 1. p_{2^{n}-1}=\frac{F_{n}(z)-2}{z-1}. |  |

This formula generalizes ( 3.2). Furthermore, the following generalization of ( 2.13) holds:

(7.2) |  | p 2 m ​ l + 2 m − 1 ​ ( z) = p 2 m ​ l ​ ( z) ​ F m − 1 ​ ( z). p_{2^{m}l+2^{m-1}}(z)=p_{2^{m}l}(z)F_{m-1}(z). |  |

In particular, taking in ( 7.2) m = 1, l = 2 t − 1 ​ n + 2 t − 2 − 1, m=1,\enskip l=2^{t-1}n+2^{t-2}-1, in view of F 0 ​ ( z) = z + 1, F_{0}(z)=z+1, we find

(7.3) |  | p 2 t ​ n + 2 t − 1 − 1 ​ ( z) = ( z + 1) ​ p 2 t ​ n + 2 t − 1 − 2 ​ ( z). p_{2^{t}n+2^{t-1}-1}(z)=(z+1)p_{2^{t}n+2^{t-1}-2}(z). |  |

After that the corresponding generalization of formulas ( 4.1)-( 4.3) is obtained. We have

(7.4) |  | ( F t − 1 ​ ( z) − 2) ​ p 2 t ​ n ​ ( z) = p 2 t ​ n + 2 t − 1 − 1 ​ ( z), (F_{t-1}(z)-2)p_{2^{t}n}(z)=p_{2^{t}n+2^{t-1}-1}(z), |  |

(7.5) |  | ( F t − 1 ​ ( z) − 2) ​ p 2 t ​ n + 2 t − 1 ​ ( z) = ( z − 1) ​ F t − 1 ​ ( z) ​ p 2 t ​ n + 2 t − 1 − 1 ​ ( z), (F_{t-1}(z)-2)p_{2^{t}n+2^{t-1}}(z)=(z-1)F_{t-1}(z)p_{2^{t}n+2^{t-1}-1}(z), |  |

(7.6) |  | ( F t − 1 ​ ( z) − 2) ​ p 2 t ​ n + 2 t − 1 ​ ( z) = ( z 2 − 1) ​ F t − 1 ​ ( z) ​ p 2 t ​ n + 2 t − 1 − 2 ​ ( z). (F_{t-1}(z)-2)p_{2^{t}n+2^{t-1}}(z)=(z^{2}-1)F_{t-1}(z)p_{2^{t}n+2^{t-1}-2}(z). |  |

Note that

(7.7) |  | p 2 ​ n ​ ( z) ≡ 1 ( mod z 2). p_{2n}(z)\equiv 1\pmod{z^{2}}. |  |

Put

(7.8) |  | l n ​ ( z) = p 2 ​ n ​ ( z) − 1 z 2. l_{n}(z)=\frac{p_{2n}(z)-1}{z^{2}}. |  |

Let in ( 7.6) t ≥ 2. t\geq 2. Then we have

(7.9) |  | ( F t − 1 ​ ( z) − 2) ​ ( z 2 ​ l 2 t − 1 ​ n + 2 t − 2 ​ ( z) + 1) = ( z 2 − 1) ​ F t − 1 ​ ( z) ​ ( z 2 ​ l 2 t − 1 ​ n + 2 t − 2 − 1 ​ ( z) + 1), (F_{t-1}(z)-2)(z^{2}l_{2^{t-1}n+2^{t-2}}(z)+1)=(z^{2}-1)F_{t-1}(z)(z^{2}l_{2^{t-1}n+2^{t-2}-1}(z)+1), |  |

or

(7.10) |  | z 2 ​ l 2 t − 1 ​ n + 2 t − 2 ​ ( z) + 1 z 2 ​ l 2 t − 1 ​ n + 2 t − 2 − 1 ​ ( z) + 1 = ( z 2 − 1) ​ F t − 1 ​ ( z) F t − 1 ​ ( z) − 2 \frac{z^{2}l_{2^{t-1}n+2^{t-2}}(z)+1}{z^{2}l_{2^{t-1}n+2^{t-2}-1}(z)+1}=\frac{(z^{2}-1)F_{t-1}(z)}{F_{t-1}(z)-2} |  |

and, consequently,

(7.11) |  | lim n → ∞ l 2 t − 1 ​ n + 2 t − 2 ​ ( z) l 2 t − 1 ​ n + 2 t − 2 − 1 ​ ( z) = ( z 2 − 1) ​ F t − 1 ​ ( z) F t − 1 ​ ( z) − 2. \lim_{n\rightarrow\infty}\frac{l_{2^{t-1}n+2^{t-2}}(z)}{l_{2^{t-1}n+2^{t-2}-1}(z)}=\frac{(z^{2}-1)F_{t-1}(z)}{F_{t-1}(z)-2}. |  |

In particular, for t = 2, t=2,

 | lim n → ∞ l 2 ​ n + 1 ​ ( z) l 2 ​ n ​ ( z) = z 2 + 1; \lim_{n\rightarrow\infty}\frac{l_{2n+1}(z)}{l_{2n}(z)}=z^{2}+1; |  |

for t = 3, t=3,

 | lim n → ∞ l 4 ​ n + 2 ​ ( z) l 4 ​ n + 1 ​ ( z) = z 4 + 1 z 2 + 1; \lim_{n\rightarrow\infty}\frac{l_{4n+2}(z)}{l_{4n+1}(z)}=\frac{z^{4}+1}{z^{2}+1}; |  |

for t = 4, t=4,

 | lim n → ∞ l 8 ​ n + 4 ​ ( z) l 8 ​ n + 3 ​ ( z) = z 8 + 1 ( z 4 + 1) ​ ( z 2 + 1), e ​ t ​ c. \lim_{n\rightarrow\infty}\frac{l_{8n+4}(z)}{l_{8n+3}(z)}=\frac{z^{8}+1}{(z^{4}+1)(z^{2}+1)},\enskip etc. |  |

In case of z = 2, z=2, we again obtain formulas ( 1.5)-( 1.7).

## References

- [1] W. B. Everett, Number of binomial coefficients divisible by a fixed power of a prime, INTEGERS, 8 (2008), #​ A ​ 11. \#A11.
- [2] J. Glaisher, On the residue of a binomial-theorem coefficient with respect to a prime modulus, Quart. J. of Pure and Applied Math., 30 (1899), 150-156.
- [3] A. Granville, Zaphod Beeblebrox’s brain and the fifty-ninth row of Pascal’s triangle, Amer. Math. Monthly, 99 , no. 4 (1992), 318-331; 104 , no. 9 (1997), 848-851.
- [4] D. Hewgill, A relationship between Pascal’s triangle and Fermat numbers, Fib. Quart., 15 (1977), 183-184.
- [5] J. G. Huard, B. K. Spearman, K. S. Williams , Pascal’s triangle ( mod 8) \pmod{8}, Europ. J. Combin., 19 , no.1 (1998), 45-62.
- [6] A. Karttunen, On Pascal’s triangle modulo 2 in Fibonacci representation, Fib. Quart., 42, no.1 (2004), 38-46.
- [7] S. Northshield, Sums across Pascal’s triangle modulo 2, Congressus Numerantium, 200 (2010), 35-52.
- [8] E. S. Rowland, The number of nonzero binomial coefficients modulo p α, p^{\alpha}, arXiv: 1001.1783v2 (2010).
- [9] V. S. Shevelev, On a combinatorial-analytical identity and some analogs of Euler formula for zeta-function, Deposed in VINITI, no. 3481-B91 (1991), 1-6 (in Russian).
- [10] V. Shevelev, Binomial coefficient predictors, arXiv: 0907.3302v4 (2009); J. Integer Seq., 14 (2011), Article 11.2.8.
- [11] N. J. A. Sloane, The On-Line Encyclopedia of Integer Sequences (http://oeis.org.)
- [12] E. Trost, Primzahlen Birkhäuser-Verlag, 1953.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
