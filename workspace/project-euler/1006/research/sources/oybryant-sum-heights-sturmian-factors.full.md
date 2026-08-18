<!-- source: https://arxiv.org/html/math/0611365 | converted from HTML -->

On the Sum of the Heights of Sturmian Factors

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: Assumed arXiv.org perpetual non-exclusive license][2]

arXiv:math/0611365v1 [math.CO] 13 Nov 2006

# On the Sum of the Heights of Sturmian Factors

Kevin O’Bryant

###### Abstract

A binary word is a map W: ℕ → { 0, 1 } W\colon{\mathbb{N}}\to\{0,1\}, and the set of factors of W W with length n n is F n ​ ( W):= { ( W ⁡ ( i), W ⁡ ( i + 1), …, W ⁡ ( i + n − 1)): i ≥ 0 } F_{n}(W):=\{\big(W(i),W(i+1),\dots,W(i+n-1)\big)\colon i\geq 0\}. A word is Sturmian if | F n ​ ( W) | = n + 1 |F_{n}(W)|=n+1 for every n ≥ 1 n\geq 1. We show that the sum of the heights (also known as hamming weights) of the n + 1 n+1 factors with length n n of a binary Sturmian word has the same parity as n n, independent of W W.

Many facts are known about the factors of length n n of a Sturmian word W W. Among the many noteworthy results are: that F n ​ ( W) F_{n}(W) is closed under reversals (the map that takes ( w 1, …, w n) (w_{1},\dots,w_{n}) to ( w n, …, w 1) (w_{n},\dots,w_{1})) [3] *Prop 2.1.19; that the volume of the convex hull of F n ​ ( W) F_{n}(W) is 1 / n! 1/n!, independent of W W [4] *Thm 1.1; and that as W W varies over all Sturmian words, F n ​ ( W) F_{n}(W) takes on ∑ i = 1 n ϕ ⁡ ( i) \sum_{i=1}^{n}\phi(i) values. We direct the reader to either [1] *Chap 9 or [3] *Chap 2 for an introduction to Sturmian words. To these we add

###### Theorem 1.

For every binary Sturmian word W W and every positive integer n n,

 | ∑ w → ∈ F n ​ ( W) h ⁡ ( w →) ≡ n ( mod 2), \sum_{\vec{w}\in F_{n}(W)}h(\vec{w})\equiv n\pmod{2}, |  |

where h ⁡ ( w →) h(\vec{w}) is the number of components of w → \vec{w} that are ‘1’.

A natural approach to proving this is to observe that since F n ​ ( W) F_{n}(W) is closed under reversal, we can pair off non-palindrome factors that have the same height h ⁡ ( w →) h(\vec{w}), and therefore it suffices to consider only the palindromes in F n ​ ( W) F_{n}(W). Moreover, if a palindrome has even length, then it must have even height, and so the ‘even- n n case’ of our theorem does follow easily from the ‘closure under reversal’ property. When n n is odd, the situation is more complicated as a palindrome may have even or odd weight, and there are always two [2]:

 | { ( 1, 0, 1, 0, 1, 0, 1), ( 1, 1, 0, 1, 0, 1, 1) } ⊆ F 7 ​ ( c 1 / 3), \big\{(1,0,1,0,1,0,1),(1,1,0,1,0,1,1)\big\}\subseteq F_{7}(c_{1/\sqrt{3}}), |  |

where c 1 / 3 c_{1/\sqrt{3}} is a particular Sturmian word defined below. Our proof does not follow this line, and does not make use of closure under reversal.

This result (and other computations) suggests that the eigenvalues of the Gram matrix G α ​ ( n):= ( w i ⋅ w j) 1 ≤ i, j ≤ n + 1 G_{\alpha}(n):=(w_{i}\cdot w_{j})_{1\leq i,j\leq n+1}, where F n ​ ( W) = { w 1, …, w n + 1 } F_{n}(W)=\{w_{1},\dots,w_{n+1}\}, may have structure. Note that the eigenvalues of a Gram matrix do not depend on the ordering of the vectors, and are necessarily nonnegative real numbers. A particularly striking phenomenon is the following. Set m ⁡ ( n) m(n) to be the multiplicity of 1 as an eigenvalue of G 2 / ( 5 − 1) ​ ( n) G_{2/(\sqrt{5}-1)}(n). For example m ⁡ ( 55) = 13 m(55)=13 and m ⁡ ( 65) = 0 m(65)=0. Figure 1 shows an impressive amount of structure, but this author has no explanation for why any structure would exist as n n changes. Similar pictures result from considering other irrationals.

Figure 1: The multiplicity of 1 as an eigenvalue of G 2 / ( 5 − 1) ​ ( n) G_{2/(\sqrt{5}-1)}(n)

## 1 The route of the proof

Let ⌊ x ⌋ \left\lfloor x\right\rfloor denote the floor of x x, and { x } \{x\} the fractional part of x x, i.e., x = ⌊ x ⌋ + { x } x=\left\lfloor x\right\rfloor+\{x\}. Define B α ( k):= #{ q: 1 ≤ q < k, { q α } < { k α } } B_{\alpha}(k):=\#\{q\colon 1\leq q<k,\,\{q\alpha\}<\{k\alpha\}\}, which counts the number of integers in [1, k) [1,k) that are ‘better’ denominators for approximating α \alpha from below.

Our proof proceeds by connecting the sum in Theorem 1 to B α ​ ( n) B_{\alpha}(n) (for some α \alpha), finding a recurrence satisfied by B α ​ ( n) B_{\alpha}(n), and then reducing that recurrence modulo 2.

The characteristic word with slope α \alpha is defined by

 | c α ​ ( n):= ⌊ ( n + 2) ​ α ⌋ − ⌊ ( n + 1) ​ α ⌋. c_{\alpha}(n):=\left\lfloor(n+2)\alpha\right\rfloor-\left\lfloor(n+1)\alpha\right\rfloor. |  |

If α \alpha is irrational, then c α c_{\alpha} is a Sturmian word [3] *Thm 2.1.13. It is known [3] *Thm 2.1.3, Prop 2.1.18 that for every binary Sturmian word W W and natural number n n, there is an α ∈ ( 0, 1) \alpha\in(0,1) with F n ​ ( W) = F n ​ ( c α) F_{n}(W)=F_{n}(c_{\alpha}), and so it suffices for our purposes to consider characteristic words, and to write F n ​ ( α):= F n ​ ( c α) F_{n}(\alpha):=F_{n}(c_{\alpha}).

###### Lemma 1.

∑ w → ∈ F n ​ ( α) h ⁡ ( w →) = B α ​ ( n) + ( n + 1) ​ ⌊ n ​ α ⌋ + 1. \displaystyle\sum_{\vec{w}\in F_{n}(\alpha)}h(\vec{w})=B_{\alpha}(n)+(n+1)\left\lfloor n\alpha\right\rfloor+1.

###### Lemma 2.

Let α ∈ ( 0, 1 / 2) \alpha\in(0,1/2) be irrational. Then B α ​ ( k) + B 1 − α ​ ( k) = k − 1 B_{\alpha}(k)+B_{1-\alpha}(k)=k-1. Moreover, B α ​ ( 1) = 0 B_{\alpha}(1)=0, B α ​ ( 2) = 1 B_{\alpha}(2)=1, and for k ≥ 3 k\geq 3

 | B α ​ ( k) − 2 ​ B α ​ ( k − 1) + B α ​ ( k − 2) = { 1 − k, { k ​ α } ∈ [0, α); k − 1, { k ​ α } ∈ [α, 2 ​ α); 0, { k ​ α } ∈ [2 ​ α, 1). B_{\alpha}(k)-2B_{\alpha}(k-1)+B_{\alpha}(k-2)=\begin{cases}1-k,&\{k\alpha\}\in[0,\alpha);\\ k-1,&\{k\alpha\}\in[\alpha,2\alpha);\\ 0,&\{k\alpha\}\in[2\alpha,1).\end{cases} |  |

###### Lemma 3.

Let α ∈ ( 0, 1) \alpha\in(0,1) be irrational, and k k any positive integer. If k k is odd, then B α ​ ( k) B_{\alpha}(k) is even. If k k is even, then B α ​ ( k) ≡ ⌊ k ​ α ⌋ + 1 ( mod 2) B_{\alpha}(k)\equiv\left\lfloor k\alpha\right\rfloor+1\pmod{2}.

## 2 Proofs

###### Proof of Lemma 1.

We begin by following [1] *Lem 10.5.1; define π i \pi_{i} by

 | { 0 = π 0 < π 1 < π 2 < ⋯ < π n } = { 0, { − α }, { − 2 α }, …, { − n α } }. \{0=\pi_{0}<\pi_{1}<\pi_{2}<\dots<\pi_{n}\}=\{0,\{-\alpha\},\{-2\alpha\},\dots,\{-n\alpha\}\}. |  |

Set v i ​ ( x):= ⌊ ( i + 1) ​ α + x ⌋ − ⌊ i ​ α + x ⌋ v_{i}(x):=\left\lfloor(i+1)\alpha+x\right\rfloor-\left\lfloor i\alpha+x\right\rfloor, and set

 | w i:= ( v 0 ​ ( π i), v 1 ​ ( π i), v 2 ​ ( π i), …, v n − 1 ​ ( π i)). w_{i}:=\big(v_{0}(\pi_{i}),v_{1}(\pi_{i}),v_{2}(\pi_{i}),\dots,v_{n-1}(\pi_{i})\big). |  |

Nontrivially (see [1]), F n ​ ( α) = { w i: 0 ≤ i ≤ n } F_{n}(\alpha)=\big\{w_{i}\colon 0\leq i\leq n\big\}, and w 0, w 1, …, w n w_{0},w_{1},\dots,w_{n} are ordered lexicographically. Elementary examination yields h ( w i) = | ℤ ∩ ( π i, n α + π i] | h(w_{i})=|{\mathbb{Z}}\cap(\pi_{i},n\alpha+\pi_{i}]|, and this last quantity is either ⌊ n ​ α ⌋ \left\lfloor n\alpha\right\rfloor or ⌊ n ​ α ⌋ + 1 \left\lfloor n\alpha\right\rfloor+1. We start with h ⁡ ( w 0) = ⌊ n ​ α ⌋ h(w_{0})=\left\lfloor n\alpha\right\rfloor, and the first i i for which h ⁡ ( w i) = ⌊ n ​ α ⌋ + 1 h(w_{i})=\left\lfloor n\alpha\right\rfloor+1 is the i i for which n ​ α + π i ∈ ℤ n\alpha+\pi_{i}\in{\mathbb{Z}}, that is, when { − n ​ α } = π i \{-n\alpha\}=\pi_{i}. In other words, the last B α ​ ( n) + 1 B_{\alpha}(n)+1 factors have weight ⌊ n ​ α ⌋ + 1 \left\lfloor n\alpha\right\rfloor+1 and the first n + 1 − ( B α ​ ( n) + 1) n+1-(B_{\alpha}(n)+1) factors have weight ⌊ n ​ α ⌋ \left\lfloor n\alpha\right\rfloor. This gives

 | ∑ w → ∈ F n ​ ( α) h ⁡ ( w →) = ( B α ​ ( n) + 1) ​ ( ⌊ n ​ α ⌋ + 1) + ( n + 1 − ( B α ​ ( n) + 1)) ​ ⌊ n ​ α ⌋ = 1 + B α ​ ( n) + ( n + 1) ​ ⌊ n ​ α ⌋. \sum_{\vec{w}\in F_{n}(\alpha)}h(\vec{w})=(B_{\alpha}(n)+1)(\left\lfloor n\alpha\right\rfloor+1)+(n+1-(B_{\alpha}(n)+1))\left\lfloor n\alpha\right\rfloor\\ =1+B_{\alpha}(n)+(n+1)\left\lfloor n\alpha\right\rfloor. |  |

∎

Our proof of Lemma 2 is similar in spirit to, and was directly inspired by, Sós’s proof of the Three-Gap Theorem [5].

###### Proof of Lemma 2.

Observe that 0 < { q ​ α } < { k ​ α } 0<\{q\alpha\}<\{k\alpha\} iff { k ⁡ ( 1 − α) } < { q ⁡ ( 1 − α) } < 1 \{k(1-\alpha)\}<\{q(1-\alpha)\}<1, so that q q with 1 ≤ q < k 1\leq q<k is in either the set { q: 1 ≤ q < k, { q α } < { k α } } \{q:1\leq q<k,\{q\alpha\}<\{k\alpha\}\} or in the set { q: 1 ≤ q < k, { q ( 1 − α) } < { k ( 1 − α) } } \{q:1\leq q<k,\{q(1-\alpha)\}<\{k(1-\alpha)\}\}, and is not in both (as α \alpha is irrational, { k ⁡ ( 1 − α) } ≠ { q ⁡ ( 1 − α) } \{k(1-\alpha)\}\not=\{q(1-\alpha)\}). Thus, B α ​ ( k) + B 1 − α ​ ( k) = k − 1 B_{\alpha}(k)+B_{1-\alpha}(k)=k-1.

We think of the k + 2 k+2 numbers 0, { α }, …, { k ​ α }, 1 0,\{\alpha\},\dots,\{k\alpha\},1 as lying on a unit circle, and labeled P 0, P 1, …, P k, P 0 P_{0},P_{1},\dots,P_{k},P_{0}, respectively, i.e., P j:= e 2 ​ π ​ j ​ α ​ − 1 = e 2 ​ π ​ { j ​ α } ​ − 1 P_{j}:=e^{2\pi j\alpha\sqrt{-1}}=e^{2\pi\{j\alpha\}\sqrt{-1}}. “The arc P i ​ P j ¯ \overline{P_{i}P_{j}} ” refers to the half-open counterclockwise arc from P i P_{i} to P j P_{j}, containing P i P_{i} but not P j P_{j}. We say that three distinct points A, B, C A,B,C are in order if B ∉ C ​ A ¯ B\not\in\overline{CA}. We say that A, B, C, D A,B,C,D are *in order*if both A, B, C A,B,C and C, D, A C,D,A are in order. Essentially, if when moving counter-clockwise around the circle starting from A A, we encounter first the point B B, then C C, then D D, and finally A A (again), then A, B, C, D A,B,C,D are in order.

By rotating the circle through an angle of 2 ​ π ​ α 2\pi\alpha, so that P i ↦ P i + 1 P_{i}\mapsto P_{i+1} ( 0 ≤ i ≤ k 0\leq i\leq k), we find that each P P on the arc P k − 2 ​ P k − 1 ¯ \overline{P_{k-2}P_{k-1}} is rotated onto a P P on the arc P k − 1 ​ P k ¯ \overline{P_{k-1}P_{k}}. Specifically, the number of P 0, P 1, …, P k − 2 P_{0},P_{1},\dots,P_{k-2} on P k − 2 ​ P k − 1 ¯ \overline{P_{k-2}P_{k-1}} is the same as the number of P 1, P 2, …, P k − 1 P_{1},P_{2},\dots,P_{k-1} on P k − 1 ​ P k ¯ \overline{P_{k-1}P_{k}}. Set

 | X:= { P 0, P 1, …, P k − 2 } and Y:= { P 1, P 2, …, P k − 1 }, X:=\{P_{0},P_{1},\dots,P_{k-2}\}\quad\text{and}\quad Y:=\{P_{1},P_{2},\dots,P_{k-1}\}, |  |

so that what we have observed is

 | | X ∩ P k − 2 ​ P k − 1 ¯ | = | Y ∩ P k − 1 ​ P k ¯ |. \left|X\cap\overline{P_{k-2}P_{k-1}}\right|=\left|Y\cap\overline{P_{k-1}P_{k}}\right|. |  | (1) |

Also, we will use the definition of B α B_{\alpha} in the forms B α ​ ( k) = | Y ∩ P 0 ​ P k ¯ | B_{\alpha}(k)=\left|Y\cap\overline{P_{0}P_{k}}\right| and B α ​ ( k − 1) = | X ∩ P 0 ​ P k − 1 ¯ | − 1 B_{\alpha}(k-1)=|X\cap\overline{P_{0}P_{k-1}}|-1, and with k k and k − 1 k-1 replaced by k − 1 k-1 and k − 2 k-2, when circumstances allow.

Now, first, suppose that { k ​ α } ∈ [0, α) \{k\alpha\}\in[0,\alpha), so that the points P 0, P k, P k − 2, P k − 1 P_{0},P_{k},P_{k-2},P_{k-1} are in order on the circle. We have

 | X ∩ P k − 2 ​ P k − 1 ¯ \displaystyle X\cap\overline{P_{k-2}P_{k-1}} | = X ∩ ( P 0 ​ P k − 1 ¯ ∖ P 0 ​ P k − 2 ¯) \displaystyle=X\cap\left(\overline{P_{0}P_{k-1}}\setminus\overline{P_{0}P_{k-2}}\right) |  |

 |  | = ( X ∩ P 0 ​ P k − 1 ¯) ∖ ( X ∩ P 0 ​ P k − 2 ¯) \displaystyle=\left(X\cap\overline{P_{0}P_{k-1}}\right)\setminus\left(X\cap\overline{P_{0}P_{k-2}}\right) |  |

 | | X ∩ P k − 2 ​ P k − 1 ¯ | \displaystyle\left|X\cap\overline{P_{k-2}P_{k-1}}\right| | = | ( X ∩ P 0 ​ P k − 1 ¯) | − | ( X ∩ P 0 ​ P k − 2 ¯) | \displaystyle=\left|\left(X\cap\overline{P_{0}P_{k-1}}\right)\right|\,-\,\left|\left(X\cap\overline{P_{0}P_{k-2}}\right)\right| |  |

 |  | = ( B α ​ ( k − 1) − 1) − ( B α ​ ( k − 2) − 1) \displaystyle=\left(B_{\alpha}(k-1)-1\right)-\left(B_{\alpha}(k-2)-1\right) |  |

 |  | = B α ​ ( k − 1) − B α ​ ( k − 2), \displaystyle=B_{\alpha}(k-1)-B_{\alpha}(k-2), |  |

and similarly

 | Y ∩ P k − 1 ​ P k ¯ \displaystyle Y\cap\overline{P_{k-1}P_{k}} | = ( Y ∩ P k − 1 ​ P 0 ¯) ∪ ( Y ∩ P 0 ​ P k ¯) \displaystyle=\left(Y\cap\overline{P_{k-1}P_{0}}\right)\cup\left(Y\cap\overline{P_{0}P_{k}}\right) |  |

 |  | = ( Y ∖ ( Y ∩ P 0 ​ P k − 1 ¯)) ∪ ( Y ∩ P 0 ​ P k ¯) \displaystyle=\left(Y\setminus\left(Y\cap\overline{P_{0}P_{k-1}}\right)\right)\cup\left(Y\cap\overline{P_{0}P_{k}}\right) |  |

 | | Y ∩ P k − 1 ​ P k ¯ | \displaystyle\left|Y\cap\overline{P_{k-1}P_{k}}\right| | = ( | Y | − | Y ∩ P 0 ​ P k − 1 ¯ |) + | Y ∩ P 0 ​ P k ¯ | \displaystyle=(|Y|-\left|Y\cap\overline{P_{0}P_{k-1}}\right|)\,+\,\left|Y\cap\overline{P_{0}P_{k}}\right| |  |

 |  | = ( k − 1 − B α ​ ( k − 1)) + B α ​ ( k) \displaystyle=(k-1-B_{\alpha}(k-1))+B_{\alpha}(k) |  |

so that Eq. ( 1) becomes B α ​ ( k − 1) − B α ​ ( k − 2) = B α ​ ( k) − B α ​ ( k − 1) + k − 1 B_{\alpha}(k-1)-B_{\alpha}(k-2)=B_{\alpha}(k)-B_{\alpha}(k-1)+k-1, as claimed in the statement of this lemma.

Now suppose that { k ​ α } ∈ [α, 2 ​ α) \{k\alpha\}\in[\alpha,2\alpha), so that the points P 0, P k − 1, P k, P k − 2 P_{0},P_{k-1},P_{k},P_{k-2} are in order. By arguing as in the above case, we find

 | X ∩ P k − 2 ​ P k − 1 ¯ = ( X ∖ ( X ∩ P 0 ​ P k − 2 ¯)) ∪ ( X ∩ P 0 ​ P k − 1 ¯), X\cap\overline{P_{k-2}P_{k-1}}=\left(X\setminus\left(X\cap\overline{P_{0}P_{k-2}}\right)\right)\cup\left(X\cap\overline{P_{0}P_{k-1}}\right), |  |

and so | X ∩ P k − 2 ​ P k − 1 ¯ | = k − 1 − ( B ⁡ ( k − 2) − 1) + ( B ⁡ ( k − 1) − 1) \left|X\cap\overline{P_{k-2}P_{k-1}}\right|=k-1-(B(k-2)-1)+(B(k-1)-1). Likewise,

 | Y ∩ P k − 1 ​ P k ¯ = ( Y ∩ P 0 ​ P k ¯) ∖ ( Y ∩ P 0 ​ P k − 1 ¯) Y\cap\overline{P_{k-1}P_{k}}=\left(Y\cap\overline{P_{0}P_{k}}\right)\setminus\left(Y\cap\overline{P_{0}P_{k-1}}\right) |  |

so that | Y ∩ P k − 1 ​ P k ¯ | = B α ​ ( k) − B α ​ ( k − 1) \left|Y\cap\overline{P_{k-1}P_{k}}\right|=B_{\alpha}(k)-B_{\alpha}(k-1). Thus, in this case Eq. ( 1) becomes B α ​ ( k − 1) − B α ​ ( k − 2) + k − 1 = B α ​ ( k) − B α ​ ( k − 1) B_{\alpha}(k-1)-B_{\alpha}(k-2)+k-1=B_{\alpha}(k)-B_{\alpha}(k-1), as claimed in the statement of the lemma.

Finally, suppose that { k ​ α } ∈ [2 ​ α, 1) \{k\alpha\}\in[2\alpha,1), so that the points P 0, P k − 2, P k − 1, P k P_{0},P_{k-2},P_{k-1},P_{k} are in order. We find

 | X ∩ P k − 2 ​ P k − 1 ¯ = ( X ∩ P 0 ​ P k − 1 ¯) ∖ ( X ∩ P 0 ​ P k − 2 ¯) X\cap\overline{P_{k-2}P_{k-1}}=\left(X\cap\overline{P_{0}P_{k-1}}\right)\setminus\left(X\cap\overline{P_{0}P_{k-2}}\right) |  |

and so | X ∩ P k − 2 ​ P k − 1 ¯ | = B ⁡ ( k − 1) − B ⁡ ( k − 2) \left|X\cap\overline{P_{k-2}P_{k-1}}\right|=B(k-1)-B(k-2). Also,

 | Y ∩ P k − 1 ​ P k ¯ = ( Y ∩ P 0 ​ P k ¯) ∖ ( Y ∩ P 0 ​ P k − 1 ¯) Y\cap\overline{P_{k-1}P_{k}}=\left(Y\cap\overline{P_{0}P_{k}}\right)\setminus\left(Y\cap\overline{P_{0}P_{k-1}}\right) |  |

and so | Y ∩ P k − 1 ​ P k ¯ | = B α ​ ( k) − B α ​ ( k − 1) \left|Y\cap\overline{P_{k-1}P_{k}}\right|=B_{\alpha}(k)-B_{\alpha}(k-1). As claimed, Eq. ( 1) becomes B α ​ ( k − 1) − B α ​ ( k − 2) = B α ​ ( k) − B α ​ ( k − 1) B_{\alpha}(k-1)-B_{\alpha}(k-2)=B_{\alpha}(k)-B_{\alpha}(k-1). ∎

For the remaining proofs, we write [[Q]]:= { 1, Q is true; 0, Q is false. \displaystyle[\![Q]\!]:=\left\{\begin{array}[]{ll}1,&\hbox{$Q$ is true;}\\ 0,&\hbox{$Q$ is false.}\end{array}\right.

###### Proof of Lemma 3.

Reducing Lemma 2 modulo 2, we find that if 0 < α < 1 / 2 0<\alpha<1/2, then

 | B α ( k) ≡ B α ( k − 2) + [[k even]] [[{ k α } < 2 α]]. B_{\alpha}(k)\equiv B_{\alpha}(k-2)+[\![k\text{ even}]\!]\,[\![\{k\alpha\}<2\alpha]\!]. |  |

and if 1 / 2 < α < 1 1/2<\alpha<1, then

 | B α ​ ( k) = − B 1 − α ​ ( k) + k − 1 ≡ B 1 − α ​ ( k) + [[k ​ even]] ( mod 2) B_{\alpha}(k)=-B_{1-\alpha}(k)+k-1\equiv B_{1-\alpha}(k)+[\![k\text{ even}]\!]\pmod{2} |  |

We work in four cases: k k may be odd or even, and α \alpha may be less than or greater than 1 / 2 1/2.

Assume first that k k is odd and 0 < α < 1 / 2 0<\alpha<1/2. As B α ​ ( 1) = 0 B_{\alpha}(1)=0 and B α ​ ( k) ≡ B α ​ ( k − 2) ( mod 2) B_{\alpha}(k)\equiv B_{\alpha}(k-2)\pmod{2}, we see by induction that B α ​ ( k) B_{\alpha}(k) is even.

Now assume that k k is odd and 1 / 2 < α < 1 1/2<\alpha<1. We have B α ​ ( k) ≡ B 1 − α ​ ( k) ( mod 2) B_{\alpha}(k)\equiv B_{1-\alpha}(k)\pmod{2}, and as 0 < 1 − α < 1 / 2 0<1-\alpha<1/2, the paragraph immediately above implies that B 1 − α ​ ( k) B_{1-\alpha}(k) is even.

Now assume that k k is even and 0 < α < 1 2 0<\alpha<\tfrac{1}{2}. Set β = 2 ​ α \beta=2\alpha, k = 2 ​ ℓ k=2\ell and B ′ ​ ( i) = B α ​ ( 2 ​ i) B^{\prime}(i)=B_{\alpha}(2i), so that B ′ ​ ( 1) = 1 B^{\prime}(1)=1 and B ′ ( i) ≡ B ′ ( i − 1) + [[{ i β } < β]] ( mod 2). B^{\prime}(i)\equiv B^{\prime}(i-1)+[\![\{i\beta\}<\beta]\!]\pmod{2}. We have

 | B α ​ ( k) = B α ​ ( 2 ​ ℓ) = B ′ ​ ( ℓ) \displaystyle B_{\alpha}(k)=B_{\alpha}(2\ell)=B^{\prime}(\ell) | ≡ B ′ ( ℓ − 1) + [[{ ℓ β } < β]] ( mod 2) \displaystyle\equiv B^{\prime}(\ell-1)+[\![\{\ell\beta\}<\beta]\!]\pmod{2} |  |

 |  | ≡ B ′ ( 1) + ∑ i = 2 ℓ [[{ i β } < β]] ( mod 2) \displaystyle\equiv B^{\prime}(1)+\sum_{i=2}^{\ell}[\![\{i\beta\}<\beta]\!]\pmod{2} |  |

 |  | = B ′ ​ ( 1) + ⌊ ℓ ​ β ⌋ = 1 + ⌊ ( k / 2) ​ ( 2 ​ α) ⌋ = 1 + ⌊ k ​ α ⌋, \displaystyle=B^{\prime}(1)+\left\lfloor\ell\beta\right\rfloor=1+\left\lfloor(k/2)(2\alpha)\right\rfloor=1+\left\lfloor k\alpha\right\rfloor, |  |

since ∑ i = 2 ℓ [[{ i β } < β]] \sum_{i=2}^{\ell}[\![\{i\beta\}<\beta]\!], with β ∈ ( 0, 1) \beta\in(0,1), counts the integers in the interval ( β, ℓ ​ β] (\beta,\ell\beta].

Finally, suppose that k k is even and 1 / 2 < α < 1 1/2<\alpha<1. By the paragraph immediately above, B 1 − α ​ ( k) ≡ 1 + ⌊ k ⁡ ( 1 − α) ⌋ ( mod 2) B_{1-\alpha}(k)\equiv 1+\left\lfloor k(1-\alpha)\right\rfloor\pmod{2}. We have

 | B α ​ ( k) \displaystyle B_{\alpha}(k) | ≡ 1 + B 1 − α ​ ( k) ( mod 2) \displaystyle\equiv 1+B_{1-\alpha}(k)\pmod{2} |  |

 |  | ≡ ⌊ k ⁡ ( 1 − α) ⌋ ( mod 2) \displaystyle\equiv\left\lfloor k(1-\alpha)\right\rfloor\pmod{2} |  |

 |  | ≡ ⌊ k ​ α ⌋ + 1 ( mod 2), \displaystyle\equiv\left\lfloor k\alpha\right\rfloor+1\pmod{2}, |  |

where we have again used the irrationality of α \alpha in the last line. ∎

###### Proof of Theorem 1.

Now, if n n is odd, then by Lemma 3, B α ​ ( n) ≡ 0 ( mod 2) B_{\alpha}(n)\equiv 0\pmod{2} and obviously n + 1 ≡ 0 ( mod 2) n+1\equiv 0\pmod{2}, whence 1 + B α ​ ( n) + ( n + 1) ​ ⌊ n ​ α ⌋ ≡ 1 ( mod 2) 1+B_{\alpha}(n)+(n+1)\left\lfloor n\alpha\right\rfloor\equiv 1\pmod{2}. If n n is even, then by Lemma 3, B α ​ ( n) ≡ ⌊ n ​ α ⌋ + 1 B_{\alpha}(n)\equiv\left\lfloor n\alpha\right\rfloor+1, whence 1 + B α ​ ( n) + ( n + 1) ​ ⌊ n ​ α ⌋ ≡ 0 ( mod 2) 1+B_{\alpha}(n)+(n+1)\left\lfloor n\alpha\right\rfloor\equiv 0\pmod{2}. ∎

## References

- [1] J. Allouche and J. Shallit (2003) Automatic sequences. Cambridge University Press. Note: Theory, applications, generalizations External Links: ISBN 0-521-82332-3, Review [MR 1997038][3] Cited by: §2, §2, On the Sum of the Heights of Sturmian Factors.
- [2] X. Droubay and G. Pirillo (1999) Palindromes and sturmian words. Theoret. Comput. Sci. 223 ( 1-2), pp. 73–85. External Links: ISSN 0304-3975, Review [MR 1704637][4] Cited by: On the Sum of the Heights of Sturmian Factors.
- [3] M. Lothaire (2002) Algebraic combinatorics on words. Encyclopedia of Mathematics and its Applications, Vol. 90, Cambridge University Press. Note: Chapter 2 written by Jean Berstel and Patrice Séébold External Links: ISBN 0-521-81220-8, Review [MR 1905123][5] Cited by: §1, On the Sum of the Heights of Sturmian Factors.
- [4] K. O’Bryant (2004) Sturmian words and the permutation that orders fractional parts. J. Algebraic Combin. 19 ( 1), pp. 91–115. External Links: ISSN 0925-9899, Review [MR 2056768][6] Cited by: On the Sum of the Heights of Sturmian Factors.
- [5] V. T. Sós (1957) On a geometrical theory of continued fractions. Mat. Lapok 8, pp. 248–263 ( Hungarian, with Russian and English summaries). External Links: ISSN 0025-519X, Review [MR 0102500][7] Cited by: §2.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: http://www.ams.org/mathscinet-getitem?mr=1997038
[4]: http://www.ams.org/mathscinet-getitem?mr=1704637
[5]: http://www.ams.org/mathscinet-getitem?mr=1905123
[6]: http://www.ams.org/mathscinet-getitem?mr=2056768
[7]: http://www.ams.org/mathscinet-getitem?mr=0102500
