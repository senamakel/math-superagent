<!-- source: https://arxiv.org/html/math/0212144 | converted from HTML -->

Symmetric Pascal matrices modulo p

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: Assumed arXiv.org perpetual non-exclusive license][2]

arXiv:math/0212144v2 [math.NT] 31 Jan 2003

# Symmetric Pascal matrices modulo p

Roland Bacher Note: Support from the Swiss National Science Foundation is gratefully acknowledged. Robin Chapman

30 January 2003

## 1 Introduction

This paper presents results and conjectures concerning symmetric matrices associated to Pascal’s triangle. We first give a formula for the determinant over 𝐙 \mathbf{Z} of the reduction modulo 2 2 with values in { 0, 1 } \{0,1\} for such a matrix. We then study the reduction modulo a prime p p of the characteristic polynomials of these matrices. Our main results imply a formula for the prime p = 2 p=2 and a conjectural formula for p = 3 p=3.

Consider the symmetric matrix P ⁡ ( n) P(n) with coefficients

 | p i, j = ( i + j i), 0 ≤ i, j < n. p_{i,j}={i+j\choose i},\ 0\leq i,j<n\ . |  |

We call P ⁡ ( n) P(n) the *symmetric Pascal matrix*of order n n. The entries of P ⁡ ( n) P(n) satisfy the recurrence

 | p i, j = p i − 1, j + p i, j − 1. p_{i,j}=p_{i-1,j}+p_{i,j-1}. |  |

In [2] the first author studied the determinant of the general matrix with entries satisfying this recurrence.

An easy computation yields P ⁡ ( ∞) = T ​ T t P(\infty)=T\ T^{t} where T T is the infinite unipotent lower triangular matrix

 | T = ( 1 1 1 1 2 1 1 3 3 1 ⋮ ⋱) = exp ​ ( 0 1 0 0 2 0 0 3 0 ⋱) T=\left(\begin{array}[]{cccccccccc}1\cr 1&1\cr 1&2&1\cr 1&3&3&1\cr\vdots&&&&\ddots\end{array}\right)=\hbox{exp}\left(\begin{array}[]{cccccccccc}0\cr 1&0\cr 0&2&0\cr&0&3&0\cr&&&&\ddots\end{array}\right) |  |

with coefficients t i, j = ( i j) t_{i,j}={i\choose j}. This shows that det ( P ⁡ ( n)) = 1 \det(P(n))=1 and that P ⁡ ( n) P(n) is positive definite for all n ∈ 𝐍 n\in{\bf N}. Hence all zeroes of the characteristic polynomial χ n ​ ( t) = det ( t ​ I ​ ( n) − P ⁡ ( n)) \chi_{n}(t)=\det(tI(n)-P(n)) (where I ⁡ ( n) I(n) denotes the identity matrix of size n n) of P ⁡ ( n) P(n) are positive reals. The inverse P ​ ( n) − 1 P(n)^{-1} of P ⁡ ( n) P(n) is given by

 | P ​ ( n) − 1 = ( T ​ ( n) t) − 1 ​ T ​ ( n) − 1 P(n)^{-1}=\left(T(n)^{t}\right)^{-1}T(n)^{-1} |  |

and T ​ ( n) − 1 T(n)^{-1} has coefficients ( − 1) i + j ​ ( i j), 0 ≤ i, j < n (-1)^{i+j}{i\choose j},\ 0\leq i,j<n. Hence T ⁡ ( n) T(n) and T ​ ( n) − 1 T(n)^{-1} are conjugate, and thus also P ⁡ ( n) P(n) and P ​ ( n) − 1 P(n)^{-1} are conjugate. The characteristic polynomial χ n ​ ( t) \chi_{n}(t) therefore satisfies χ n ​ ( t) = ( − t) n ​ χ ​ ( 1 / t) \chi_{n}(t)=(-t)^{n}\chi(1/t) and 1 1 is always an eigenvalue of P ⁡ ( 2 ​ n + 1) P(2n+1), cf. [4]. The polynomials χ n ​ ( t) \chi_{n}(t), especially their behaviour modulo primes, will be our main object of study. For convenience, we write I I for I ⁡ ( n) I(n) whenever the size of the identity matrix is unambiguous.

Define P ¯ ​ ( n) 2 {\overline{P}}(n)_{2} as the reduction modulo 2 2 of P ⁡ ( n) P(n) with values in { 0, 1 } \{0,1\} by setting

 | p ¯ i, j = ( ( i + j i) ( mod 2)) ∈ { 0, 1 }. {\overline{p}}_{i,j}=\left({i+j\choose i}\pmod{2}\right)\in\{0,1\}\ . |  |

The Thue-Morse sequence s n = ∑ ν i ( mod 2) s_{n}=\sum\nu_{i}\pmod{2} counts the parity of all non-zero digits of a binary integer n = ∑ ν i ​ 2 i n=\sum\nu_{i}2^{i}. It can also be defined recursively by s 0 = 0 s_{0}=0, s 2 ​ k = s k s_{2k}=s_{k} and s 2 ​ k + 1 = 1 − s k s_{2k+1}=1-s_{k} (cf. for instance [1]).

###### Theorem 1.1

The determinant (over 𝐙 \bf Z) of P ¯ ​ ( n) 2 {\overline{P}}(n)_{2} is given by

 | det ( P ¯ ​ ( n) 2) = ∏ k = 0 n − 1 ( − 1) s k. \det({\overline{P}}(n)_{2})=\prod_{k=0}^{n-1}(-1)^{s_{k}}\ . |  |

A similar result holds for the reduction modulo 3 3 of P ⁡ ( n) P(n) with values in { − 1, 0, 1 } \{-1,0,1\}.

In the sequel, we will be interested in the characteristic polynomial det ( t ​ I − P ⁡ ( n)) ( mod p) \det(tI-P(n))\pmod{p} for p p a prime number. The next result yields a formula for n = p l n=p^{l} and is of crucial importance in the sequel.

###### Proposition 1.2

Given a power q = p l q=p^{l} of a prime p p, the matrix P ⁡ ( q) P(q) has order 3 3 over 𝐅 p \mathbf{F}_{p}. Its characteristic polynomial χ q ​ ( t) = det ( t ​ I ​ ( q) − P ⁡ ( q)) \chi_{q}(t)=\det(tI(q)-P(q)) satisfies

 | χ q ​ ( t) ≡ ( t 2 + t + 1) q − ϵ ⁡ ( q) 3 ​ ( t − 1) q + 2 ​ ϵ ​ ( q) 3 ( mod p) \chi_{q}(t)\equiv(t^{2}+t+1)^{\frac{q-\epsilon(q)}{3}}(t-1)^{\frac{q+2\epsilon(q)}{3}}\pmod{p} |  |

where ϵ ⁡ ( q) ∈ { − 1, 0, 1 } \epsilon(q)\in\{-1,0,1\} satisfies ϵ ⁡ ( q) ≡ q ( mod 3) \epsilon(q)\equiv q\pmod{3}.

In particular, P ⁡ ( q) P(q) can be diagonalized over 𝐅 p 2 \mathbf{F}_{p^{2}} except when p = 3 p=3. For instance, P ⁡ ( 3) P(3) has a unique Jordan block over 𝐅 3 \mathbf{F}_{3}.

This proposition (except for the diagonalization part) admits the following generalization:

###### Theorem 1.3

When q = p l q=p^{l} is a power of a prime p p and 0 ≤ k ≤ q / 2 0\leq k\leq q/2 then

 | χ q − k ​ ( t) ≡ ( t 2 + t + 1) ( q − ϵ ⁡ ( q)) / 3 − k ​ ( t − 1) ( q + 2 ​ ϵ ​ ( q)) / 3 − k ​ det ( t 2 ​ I + P ⁡ ( k)) ( mod p) \chi_{q-k}(t)\equiv(t^{2}+t+1)^{(q-\epsilon(q))/3-k}(t-1)^{(q+2\epsilon(q))/3-k}\det(t^{2}I+P(k))\pmod{p} |  |

where ϵ ⁡ ( q) ∈ { − 1, 0, 1 } \epsilon(q)\in\{-1,0,1\} satisfies ϵ ⁡ ( q) ≡ q ( mod 3) \epsilon(q)\equiv q\pmod{3}.

Theorem 1.3 completely determines the reduction modulo 2 2 of χ n ​ ( t) \chi_{n}(t) as follows: Define a sequence γ ⁡ ( 0) = 0, γ ⁡ ( 1), … \gamma(0)=0,\gamma(1),\dots recursively by

 | γ ⁡ ( 2 l − k) = 2 l + 2 ​ ( − 1) l 3 − k + 2 ​ γ ​ ( k), 0 ≤ k ≤ 2 l − 1. \gamma(2^{l}-k)=\frac{2^{l}+2(-1)^{l}}{3}-k+2\gamma(k),\ 0\leq k\leq 2^{l-1}\ . |  |

###### Theorem 1.4

For all n ∈ 𝐍 n\in\mathbf{N}

 | χ n ​ ( t) ≡ ( t + 1) γ ⁡ ( n) ​ ( t 2 + t + 1) γ 2 ​ ( n) ( mod 2) \chi_{n}(t)\equiv(t+1)^{\gamma(n)}(t^{2}+t+1)^{\gamma_{2}(n)}\pmod{2} |  |

where γ 2 ​ ( n) = 1 2 ​ ( n − γ ⁡ ( n)) \gamma_{2}(n)=\frac{1}{2}(n-\gamma(n)).

It follows immediately that the matrix I − P ​ ( n) 3 I-P(n)^{3} is nilpotent over 𝐅 2 \mathbf{F}_{2} for all n ∈ 𝐍 n\in{\bf N}.

The first terms γ ⁡ ( 1), …, γ ⁡ ( 32) \gamma(1),\dots,\gamma(32) and γ 2 ​ ( 1), …, γ 2 ​ ( 32) \gamma_{2}(1),\dots,\gamma_{2}(32) are given by

 | n 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 γ ⁡ ( n) 1 0 3 2 5 0 3 2 5 0 11 6 9 4 7 6 γ 2 ​ ( n) 0 1 0 1 0 3 2 3 2 5 0 3 2 5 4 5 n 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 γ ⁡ ( n) 9 4 15 10 21 0 11 6 9 4 15 10 13 8 11 10 γ 2 ​ ( n) 4 7 2 5 0 11 6 9 8 11 6 9 8 11 10 11 \begin{array}[]{| c | cccccccccccccccc |}\hline\cr n&1&2&3&4&5&6&7&8&9&10&11&12&13&14&15&16\cr\gamma(n)&1&0&3&2&5&0&3&2&5&0&11&6&9&4&7&6\cr\gamma_{2}(n)&0&1&0&1&0&3&2&3&2&5&0&3&2&5&4&5\cr\hline\cr n&17&18&19&20&21&22&23&24&25&26&27&28&29&30&31&32\cr\gamma(n)&9&4&15&10&21&0&11&6&9&4&15&10&13&8&11&10\cr\gamma_{2}(n)&4&7&2&5&0&11&6&9&8&11&6&9&8&11&10&11\cr\hline\cr\end{array} |  |

The sequence γ ⁡ ( 0), γ ⁡ ( 1), … \gamma(0),\gamma(1),\dots has many interesting arithmetic features. In order to describe them, let us introduce the number b ⁡ ( n) b(n) of “blocks” of adjacent ones in the binary representation of a positive integer n n. For instance 667 = ( 1010011011) 2 667=(1010011011)_{2} and so b ⁡ ( 667) = 4 b(667)=4. Notice that b ⁡ ( 2 ​ n) = b ⁡ ( n) b(2n)=b(n) and b ⁡ ( 2 ​ n + 1) = b ⁡ ( n) + 1 − ( n ( mod 2)) b(2n+1)=b(n)+1-\left(n\pmod{2}\right) (with n ( mod 2) ∈ { 0, 1 } n\pmod{2}\in\{0,1\}). This, together with b ⁡ ( 0) = 0 b(0)=0, defines the sequence b ⁡ ( n) b(n) recursively.

###### Theorem 1.5

(i) We have

 | γ ⁡ ( 2 l + k) = 2 l + 2 ​ ( − 1) l 3 − k + 4 ​ γ ​ ( k) \gamma(2^{l}+k)=\frac{2^{l}+2(-1)^{l}}{3}-k+4\gamma(k) |  |

for all 0 ≤ k ≤ 2 l − 1 0\leq k\leq 2^{l-1}.

(ii) We have for all n ∈ 𝐍 n\in\mathbf{N} and 2 l − 2 ≤ k ≤ 2 l − 1 2^{l-2}\leq k\leq 2^{l-1}

 | γ ⁡ ( 2 l − k) = γ ⁡ ( k) + 2 ​ γ ​ ( 2 l − 1 − k). \gamma(2^{l}-k)=\gamma(k)+2\gamma(2^{l-1}-k)\ . |  |

(iii) We have

 | γ ⁡ ( 2 l + k) = 1 + γ ⁡ ( 2 l + k − 1) + 2 ​ γ ​ ( 2 l − k) − 2 ​ γ ​ ( 2 l + 1 − k) \gamma(2^{l}+k)=1+\gamma(2^{l}+k-1)+2\gamma(2^{l}-k)-2\gamma(2^{l}+1-k) |  |

for 1 ≤ k ≤ 2 l 1\leq k\leq 2^{l}.

(iv) We have

 | γ ⁡ ( 2 ​ n) = n − γ ⁡ ( n), γ ⁡ ( 2 ​ n − 1) = γ ⁡ ( 2 ​ n) + ( 4 b ⁡ ( 2 ​ n − 1) − 1) / 3 = n − γ ⁡ ( n) + ( 4 b ⁡ ( 2 ​ n − 1) − 1) / 3, γ ⁡ ( 2 ​ n + 1) = γ ⁡ ( 2 ​ n) + ( 2 1 + 2 ​ b ​ ( n) + 1) / 3 = n − γ ⁡ ( n) + ( 2 1 + 2 ​ b ​ ( n) + 1) / 3. \begin{array}[]{lcl}\gamma(2n)&=&n-\gamma(n)\ ,\cr\gamma(2n-1)&=&\gamma(2n)+(4^{b(2n-1)}-1)/3=n-\gamma(n)+(4^{b(2n-1)}-1)/3\ ,\cr\gamma(2n+1)&=&\gamma(2n)+(2^{1+2b(n)}+1)/3=n-\gamma(n)+(2^{1+2b(n)}+1)/3\ .\end{array} |  |

Part (iv) of this Theorem gives an alternative recursive definition of the sequence ( γ ⁡ ( n)) (\gamma(n)).

Theorem 1.3 seems to have many generalizations. A first one is given by the following:

###### Conjecture 1.6

For each integer k ≥ 0 k\geq 0 there exists a monic polynomial c k ​ ( t) ∈ 𝐙 ​ [t] c_{k}(t)\in\mathbf{Z}[t] of degree 4 ​ k 4k such that c k ​ ( t) = t 4 ​ k ​ c k ​ ( t − 1) c_{k}(t)=t^{4k}c_{k}(t^{-1}) with the following property: if q q is a power of a prime p p, and 0 ≤ k ≤ q / 2 0\leq k\leq q/2 then

 | χ q + k ​ ( t) ≡ ( t 2 + t + 1) ( q − ϵ ⁡ ( q)) / 3 − k ​ ( t − 1) ( q + 2 ​ ϵ ​ ( q)) / 3 − k ​ c k ​ ( t) ( mod p) \chi_{q+k}(t)\equiv(t^{2}+t+1)^{(q-\epsilon(q))/3-k}(t-1)^{(q+2\epsilon(q))/3-k}c_{k}(t)\pmod{p} |  |

where ϵ ⁡ ( q) ∈ { − 1, 0, 1 } \epsilon(q)\in\{-1,0,1\} satisfies ϵ ⁡ ( q) ≡ q ( mod 3) \epsilon(q)\equiv q\pmod{3}.

The first few of these conjectural polynomials c k ​ ( t) c_{k}(t) are

 | c 0 ​ ( t) \displaystyle c_{0}(t) | = \displaystyle= | 1, \displaystyle 1, |  |

 | c 1 ​ ( t) \displaystyle c_{1}(t) | = \displaystyle= | t 4 − 2 ​ t 3 − 2 ​ t + 1, \displaystyle t^{4}-2t^{3}-2t+1, |  |

 | c 2 ​ ( t) \displaystyle c_{2}(t) | = \displaystyle= | t 8 − 6 ​ t 7 + 4 ​ t 6 − 4 ​ t 5 + 15 ​ t 4 − 4 ​ t 3 + 4 ​ t 2 − 6 ​ t + 1, \displaystyle t^{8}-6t^{7}+4t^{6}-4t^{5}+15t^{4}-4t^{3}+4t^{2}-6t+1, |  |

 | c 3 ​ ( t) \displaystyle c_{3}(t) | = \displaystyle= | ( t 4 − 2 ​ t 3 − 2 ​ t + 1) ​ ( t 8 − 16 ​ t 7 + 4 ​ t 6 − 4 ​ t 5 + 40 ​ t 4 − 4 ​ t 3 + 4 ​ t 2 − 16 ​ t + 1), \displaystyle(t^{4}-2t^{3}-2t+1)(t^{8}-16t^{7}+4t^{6}-4t^{5}+40t^{4}-4t^{3}+4t^{2}-16t+1), |  |

 | c 4 ​ ( t) \displaystyle c_{4}(t) | = \displaystyle= | t 16 − 58 ​ t 15 + 288 ​ t 14 − 240 ​ t 13 + 393 ​ t 12 − 1440 ​ t 11 + 836 ​ t 10 − 902 ​ t 9 \displaystyle t^{16}-58t^{15}+288t^{14}-240t^{13}+393t^{12}-1440t^{11}+836t^{10}-902t^{9} |  |

 |  |  | + 2376 ​ t 8 − 902 ​ t 7 + ⋯ − 58 ​ t + 1, \displaystyle{}+2376t^{8}-902t^{7}+\cdots-58t+1, |  |

 | c 5 ​ ( t) \displaystyle c_{5}(t) | = \displaystyle= | c 1 ​ ( t) ​ ( t 16 − 196 ​ t 15 + 2112 ​ t 14 − 792 ​ t 13 + 1290 ​ t 12 − 10560 ​ t 11 CLOSE \displaystyle c_{1}(t)(t^{16}-196t^{15}+2112t^{14}-792t^{13}+1290t^{12}-10560t^{11} |  |

 |  |  | OPEN + 2768 ​ t 10 − 2972 ​ t 9 + 17424 8 − 2972 ​ t 7 + ⋯ − 196 ​ t + 1). \displaystyle{}+2768t^{10}-2972t^{9}+17424^{8}-2972t^{7}+\cdots-196t+1). |  |

For p = 2 p=2, it follows from Theorem 1.4 and assertion (ii) in Theorem 1.5 that if c k ​ ( t) c_{k}(t) exists then

 | c k ​ ( t) ≡ ( det ( t ​ I + P ⁡ ( k))) 4 ( mod 2). c_{k}(t)\equiv\left(\det(tI+P(k))\right)^{4}\pmod{2}. |  |

Computations suggest:

###### Conjecture 1.7

We have

 | c k ​ ( t) ≡ ( t + 1) 3 ​ k ​ det ( t ​ I + P ⁡ ( k)) ( mod 3). c_{k}(t)\equiv(t+1)^{3k}\det(tI+P(k))\pmod{3}\ . |  |

This conjecture, together with Theorem 1.3 yields conjectural recursive formulas for p n ​ ( t) = det ( t ​ I ​ ( n) − P ⁡ ( n)) ( mod 3) p_{n}(t)=\det(tI(n)-P(n))\pmod{3} as follows: Set p 0 ​ ( t) = 1 ( mod 3), p 1 ​ ( t) = 1 − t ( mod 3) p_{0}(t)=1\pmod{3},\ p_{1}(t)=1-t\pmod{3}. For n = 3 l ± k > 1 n=3^{l}\pm k>1 with 0 ≤ k < 3 l 2 0\leq k<\frac{3^{l}}{2} the characteristic polynomial χ n ​ ( t) ( mod 3) \chi_{n}(t)\pmod{3} is then conjecturally given by

 | ( t − 1) 3 l − 3 ​ k ​ det ( t 2 ​ I + P ⁡ ( k)) if ​ n = 3 l − k, ( t − 1) 3 l − 3 ​ k ​ ( t + 1) 3 ​ k ​ det ( t ​ I + P ⁡ ( k)) if ​ n = 3 l + k. \begin{array}[]{ll}\displaystyle(t-1)^{3^{l}-3k}\ \det(t^{2}I+P(k))&\displaystyle\hbox{if }n=3^{l}-k\ ,\cr\displaystyle(t-1)^{3^{l}-3k}\ (t+1)^{3k}\ \det(tI+P(k))&\displaystyle\hbox{if }n=3^{l}+k\ .\end{array} |  |

In particular, all roots of χ n ​ ( t) \chi_{n}(t) modulo 3 3 should be of multiplicative order a power of 2 2 in the algebraic closure of 𝐅 3 \mathbf{F}_{3}.

We conclude finally by mentioning a last conjectural observation:

###### Conjecture 1.8

Given a prime-power q = p l ≡ 2 ( mod 3) q=p^{l}\equiv 2\pmod{3}, we have

 | χ ( q + 1) / 3 ​ ( t) ≡ ( t + 1) ( q + 1) / 3 ( mod p) \chi_{(q+1)/3}(t)\equiv(t+1)^{(q+1)/3}\pmod{p} |  |

and

 | χ ( 2 ​ q − 1) / 3 ​ ( t) ≡ ( t + 1) ( q + 1) / 3 ​ ( t − 1) ( q − 2) / 3 ( mod p). \chi_{(2q-1)/3}(t)\equiv(t+1)^{(q+1)/3}\ (t-1)^{(q-2)/3}\pmod{p}. |  |

###### Remark 1.9

(i) The matrix C = P ⁡ ( q + 1 3) + I ⁡ ( q + 1 3) C=P(\frac{q+1}{3})+I(\frac{q+1}{3}) for q = p l ≡ 2 ( mod 3) q=p^{l}\equiv 2\pmod{3} a prime-power, appears to have a unique Jordan block of maximal length over 𝐅 p \mathbf{F}_{p}. If so, the rows of C ( q + 1) / 6 C^{(q+1)/6} generate a self-dual code over 𝐅 p \mathbf{F}_{p}.

(ii) Given a prime power q = p l ≡ 2 ( mod 3) q=p^{l}\equiv 2\pmod{3} as above we set n = 2 ​ q + 2 3 n=\frac{2q+2}{3} and k = 2 ​ q − 1 3 k=\frac{2q-1}{3}. We conjecture that the characteristic polynomial of the matrix P ~ k ​ ( n) \tilde{P}_{k}(n) with coefficients

 | p ~ i, j = ( i + j + 2 ​ k i + k), 0 ≤ i, j < n \tilde{p}_{i,j}={i+j+2k\choose i+k},\ 0\leq i,j<n |  |

satisfies det ( t ​ I − P ~ k ​ ( n)) ≡ ( 1 + t) n ( mod p) \det(tI-\tilde{P}_{k}(n))\equiv(1+t)^{n}\pmod{p}.

###### Remark 1.10

In [3, Theorems 32 and 35] Krattenthaler gives evaluations of determinants related to ours, namely of det ( ω ​ I + Q ⁡ ( n)) \det(\omega I+Q(n)) where ω \omega is a sixth root of unity, and Q ⁡ ( n) Q(n) has entries ( 2 ​ μ + i + j j) {2\mu+i+j\choose j} ( 0 ≤ i, j < n) (0\leq i,j<n).

The sequel of this paper is organized as follows:

Section 2 is devoted to autosimilar matrices. Such matrices generalize the matrix P ¯ ​ ( ∞) 2 {\overline{P}}(\infty)_{2} and their properties imply easily Theorem 1.1.

Section 3 contains proofs of Proposition 1.2 and Theorem 1.3.

Section 4 contains proofs of Theorems 1.4 and 1.5.

## 2 Autosimilar matrices

Let b ≥ 1 b\geq 1 be a natural integer. An infinite matrix M M with coefficients m i, j m_{i,j} ( i, j ≥ 0 i,j\geq 0) is b b -autosimilar if m 0, 0 = 1 m_{0,0}=1 and if

 | m s, t = ∏ i m σ i, τ i m_{s,t}=\prod_{i}m_{\sigma_{i},\tau_{i}} |  |

where the indices s = ∑ σ i ​ b i, t = ∑ τ i ​ b i s=\sum\sigma_{i}b^{i},\ t=\sum\tau_{i}b^{i} are written in base b b, that is, σ i, τ i ∈ { 0, …, b − 1 } \sigma_{i},\tau_{i}\in\{0,\dots,b-1\} for all i = 0, 1, 2, … i=0,1,2,\dots.

We denote by M ⁡ ( n) M(n) the finite sub-matrix of M M with coefficients m i, j, 0 ≤ i, j < n m_{i,j},\ 0\leq i,j<n. A b b -autosimilar matrix M M is non-degenerate if the determinants

 | det ( M ⁡ ( n)) \det(M(n)) |  |

are invertible for n = 2, …, b n=2,\dots,b.

###### Theorem 2.1

Let b ≥ 2 b\geq 2 be an integer and let M M be a b b -autosimilar matrix which is non-degenerate. One has then a factorization

 | M = L ​ D ​ U M=LDU |  |

where L, D, U L,D,U are b b -autosimilar and where L L is unipotent lower-triangular, D D is diagonal and U U is unipotent upper-triangular.

###### Corollary 2.2

Given a non-degenerate b b -autosimilar matrix M M one has

 | det ( M ⁡ ( n)) = ∏ i = 0 n − 1 d ν i \det(M(n))=\prod_{i=0}^{n-1}d_{\nu_{i}} |  |

for all n = ∑ ν i ​ b i n=\sum\nu_{i}b^{i} with d 0 = 1 d_{0}=1 and

 | d k = det ( M ⁡ ( k + 1)) / det ( M ⁡ ( k)) d_{k}=\det(M(k+1))/\det(M(k)) |  |

for k = 1, …, b − 1 k=1,\dots,b-1.

###### Remark 2.3

In general, one can compute determinants of arbitrary b b -autosimilar matrices over a field K K by applying Corollary 2.2 to the b b -autosimilar matrix obtained from a generic perturbation of the form

 | M t ​ ( b) = ( 1 − t) ​ M ​ ( b) + t ​ P ​ ( b) M_{t}(b)=(1-t)M(b)+tP(b) |  |

(where P ⁡ ( b) P(b) is a suitable matrix) and working over the rational function field K ⁡ ( t) K(t).

Proof of Theorem 2.1. The genericity of M M implies that

 | M ⁡ ( b) = L ⁡ ( b) ​ D ​ ( b) ​ U ​ ( b) M(b)=L(b)D(b)U(b) |  |

where L ⁡ ( b) L(b) and U ⁡ ( b) U(b) are unipotent upper and lower triangular matrices and the diagonal matrix D ⁡ ( b) D(b) has entries d 0, 0 = 1 d_{0,0}=1 and d k, k = det ( M ⁡ ( k + 1)) / det ( M ⁡ ( k)) d_{k,k}=\det(M(k+1))/\det(M(k)) for k = 1, …, b − 1 k=1,\dots,b-1. Extending L ⁡ ( b) L(b), D ⁡ ( b) D(b) and U ⁡ ( b) U(b) in the unique possible way to infinite b b -autosimilar matrices L L, D D and U U we have

 | ( L ​ D ​ U) s, t = ∑ k L s, k ​ D k, k ​ U k, t = ∑ k = ∑ κ i ​ b i ∏ i L σ i, κ i ​ D κ i, κ i ​ U κ i, τ i = ∏ i ∑ κ i = 0 b − 1 L σ i, κ i ​ D κ i, κ i ​ U κ i, τ i = ∏ i M σ i, τ i = M s, t \begin{array}[]{ll}\displaystyle(LDU)_{s,t}&\displaystyle=\sum_{k}L_{s,k}D_{k,k}U_{k,t}\cr&\displaystyle=\sum_{k=\sum\kappa_{i}b^{i}}\prod_{i}L_{\sigma_{i},\kappa_{i}}D_{\kappa_{i},\kappa_{i}}U_{\kappa_{i},\tau_{i}}\cr&\displaystyle=\prod_{i}\sum_{\kappa_{i}=0}^{b-1}L_{\sigma_{i},\kappa_{i}}D_{\kappa_{i},\kappa_{i}}U_{\kappa_{i},\tau_{i}}\cr&\displaystyle=\prod_{i}M_{\sigma_{i},\tau_{i}}=M_{s,t}\end{array} |  |

for all s = ∑ σ i ​ b i, t = ∑ τ i ​ b i ∈ 𝐍 s=\sum\sigma_{i}b^{i},t=\sum\tau_{i}b^{i}\in{\bf N}. □ \Box

The identity

 | det ( M ⁡ ( n)) = det ( D ⁡ ( n)) \det(M(n))=\det(D(n)) |  |

implies immediately Corollary 2.2.

### 2.1 Binomial coefficients modulo a prime p p

Let p p be a prime number. We have then

 | ( 1 + x) n = ∏ ( 1 + x) ν i ​ p i ≡ ( 1 + x p i) ν i ( mod p) (1+x)^{n}=\prod(1+x)^{\nu_{i}p^{i}}\equiv(1+x^{p^{i}})^{\nu_{i}}\pmod{p} |  |

(using properties of the Frobenius automorphism in characteristic p p). This implies immediately the equality

 | ( n k) = ∏ i ( ν i κ i) {n\choose k}=\prod_{i}{\nu_{i}\choose\kappa_{i}} |  |

allowing (for small primes) an efficient computation of binomial coefficients ( mod p) \pmod{p}.

This equality shows that the reductions modulo 2 or 3 of the symmetric Pascal triangle P P with coefficients

 | p ¯ i, j = ( ( i + j i) ( mod 2)) ∈ { 0, 1 } {\overline{p}}_{i,j}=\left({i+j\choose i}\pmod{2}\right)\in\{0,1\} |  |

respectively

 | p ¯ i, j = ( ( i + j i) ( mod 3)) ∈ { − 1, 0, 1 } {\overline{p}}_{i,j}=\left({i+j\choose i}\pmod{3}\right)\in\{-1,0,1\} |  |

are 2 − 2- (respectively 3 − 3-) autosimilar matrices.

For p = 2 p=2 we have

 | ( 1 1 1 0) = ( 1 0 1 1) ​ ( 1 0 0 − 1) ​ ( 1 1 0 1) \left(\begin{array}[]{cc}1&1\cr 1&0\end{array}\right)=\left(\begin{array}[]{cc}1&0\cr 1&1\end{array}\right)\left(\begin{array}[]{rr}1&0\cr 0&-1\end{array}\right)\left(\begin{array}[]{rr}1&1\cr 0&1\end{array}\right) |  |

which yields d 0 = 1, d 1 = − 1 d_{0}=1,d_{1}=-1 and Corollary 2.2 implies now Theorem 1.1.

###### Remark 2.4

One can show that the inverse of the integral matrix P ¯ ​ ( n) 2 {\overline{P}}(n)_{2} considered in Theorem 1.1 has all its coefficients in { − 1, 0, 1 } \{-1,0,1\} for all n n.

For p = 3 p=3 we have

 | ( 1 1 1 1 − 1 0 1 0 0) = ( 1 0 0 1 1 0 1 1 2 1) ​ ( 1 0 0 0 − 2 0 0 0 − 1 2) ​ ( 1 1 1 0 1 1 2 0 0 1) \left(\begin{array}[]{rrr}1&1&1\cr 1&-1&0\cr 1&0&0\end{array}\right)=\left(\begin{array}[]{rrr}1&0&0\cr 1&1&0\cr 1&\frac{1}{2}&1\end{array}\right)\left(\begin{array}[]{rrr}1&0&0\cr 0&-2&0\cr 0&0&-\frac{1}{2}\end{array}\right)\left(\begin{array}[]{rrr}1&1&1\cr 0&1&\frac{1}{2}\cr 0&0&1\end{array}\right) |  |

This shows that det ( P ¯ ​ ( n) 3) \det(\overline{P}(n)_{3}) (over 𝐙 \bf Z) equals ( − 2) a − b (-2)^{a-b} where a a and b b are the number of digits 1 1 and 2 2 needed in order to write all natural integers < n <n in base 3 3.

## 3 Proofs of Proposition 1.2 and Theorem 1.3

Proof of Proposition 1.2 Let R R be a commutative ring, and let

 | A = ( a b c d) ∈ GL ( 2, R). A=\left(\begin{array}[]{cc}{a}&{b}\\ {c}&{d}\end{array}\right)\in\mathop{\mathrm{GL}}(2,R). |  |

Then A A determines a (graded R R -algebra) automorphism ϕ A \phi_{A} of R ⁡ [X, Y] R[X,Y] via ϕ A ​ ( X) = a ​ X + b ​ Y \phi_{A}(X)=aX+bY and ϕ A ​ ( Y) = c ​ X + d ​ Y \phi_{A}(Y)=cX+dY, or alternatively

 | ( ϕ A ​ ( X) ϕ A ​ ( Y)) = A ​ ( X Y). \left(\begin{array}[]{c}{\phi_{A}(X)}\\ {\phi_{A}(Y)}\end{array}\right)=A\left(\begin{array}[]{c}{X}\\ {Y}\end{array}\right). |  |

It is easy to see that ϕ A ∘ ϕ B = ϕ B ​ A \phi_{A}\circ\phi_{B}=\phi_{BA}. Each ϕ A \phi_{A} restricts to an R R -module automorphism of the homogeneous polynomials R ​ [X, Y] n − 1 R[X,Y]_{n-1} of degree n − 1 n-1. Let A ( n) A^{(n)} denote the matrix of this endomorphism with respect to the basis X n − 1 X^{n-1}, X n − 2 ​ Y X^{n-2}Y, X n − 3 ​ Y 2, …, Y n − 1 X^{n-3}Y^{2},\ldots,Y^{n-1}, that is

 | ( ϕ A ​ ( X n − 1) ϕ A ​ ( X n − 2 ​ Y) ϕ A ​ ( X n − 3 ​ Y 2) ⋮ ϕ A ​ ( Y n − 1)) = A ( n) ​ ( X n − 1 X n − 2 ​ Y X n − 3 ​ Y 2 ⋮ Y n − 1). \left(\begin{array}[]{c}{\phi_{A}(X^{n-1})}\\ {\phi_{A}(X^{n-2}Y)}\\ {\phi_{A}(X^{n-3}Y^{2})}\\ \vdots\\ {\phi_{A}(Y^{n-1})}\\ \end{array}\right)=A^{(n)}\left(\begin{array}[]{c}{X^{n-1}}\\ {X^{n-2}Y}\\ {X^{n-3}Y^{2}}\\ \vdots\\ {Y^{n-1}}\\ \end{array}\right). |  |

Then A ( n) ∈ GL ( n, R) A^{(n)}\in\mathop{\mathrm{GL}}(n,R) and ( A ​ B) ( n) = A ( n) ​ B ( n) (AB)^{(n)}=A^{(n)}B^{(n)}. (Another way of expressing this is to say that A ( n) A^{(n)} is the ( n − 1) (n-1) -th symmetric power of A A.)

Let us specialize to the case R = 𝐅 p = 𝐙 / p ​ 𝐙 R=\mathbf{F}_{p}=\mathbf{Z}/p\mathbf{Z} and n = p l n=p^{l}. In this case A ( n) = I A^{(n)}=I if and only if A A is a scalar matrix. The matrix

 | A = ( 1 − 1 1 0) A=\left(\begin{array}[]{cc}{1}&{-1}\\ {1}&{0}\end{array}\right) |  |

yields A ( n) ≡ P ⁡ ( p l) ( mod p) A^{(n)}\equiv P(p^{l})\pmod{p}. Since A 3 = − I A^{3}=-I, the matrix A ( n) A^{(n)} has order 3 3.

Let us now compute the multiplicities of the three eigenvalues of P = P ⁡ ( p) ( mod p) P=P(p)\pmod{p} over 𝐅 p \mathbf{F}_{p} (the formula for P ⁡ ( p l) P(p^{l}) is then a straightforward consequence of the fact the P ⁡ ( p l) P(p^{l}) is the l − l- fold Kronecker product of P ⁡ ( p) P(p) with itself).

The easy identity ( 2 ​ k k) = ( ( p − 1) / 2 k) ​ ( − 4) k ( mod p) {2k\choose k}={(p-1)/2\choose k}(-4)^{k}\pmod{p} for p p an odd prime and 0 ≤ k ≤ ( p − 1) / 2 0\leq k\leq(p-1)/2 shows

 | ∑ k = 0 ( p − 1) / 2 ( 2 ​ k k) ​ ( − x 4) k ≡ ( 1 + x) ( p − 1) / 2 ( mod p) \sum_{k=0}^{(p-1)/2}{2k\choose k}\left(\frac{-x}{4}\right)^{k}\equiv(1+x)^{(p-1)/2}\pmod{p} |  |

and yields tr ​ ( P) ≡ ( − 3) ( p − 1) / 2 ≡ ϵ ⁡ ( p) ( mod p) \hbox{tr}(P)\equiv(-3)^{(p-1)/2}\equiv\epsilon(p)\pmod{p} (where ϵ ⁡ ( p) ∈ { − 1, 0, 1 } \epsilon(p)\in\{-1,0,1\} satisfies ϵ ⁡ ( p) ≡ p ( mod 3) \epsilon(p)\equiv p\pmod{3}) by quadratic reciprocity.

Since the characteristic polynomial for P P has antisymmetric coefficients ( α k = − α p − k \alpha_{k}=-\alpha_{p-k}) the two eigenvalues ≠ 1 \not=1 of P P have equal multiplicity r r. Lifting into positive integers ≤ p − 1 2 \leq\frac{p-1}{2} the solution of the linear system − r + ( p − 2 ​ r) ≡ tr ​ ( P) ( mod p) -r+(p-2r)\equiv\hbox{tr}(P)\pmod{p} yields now the result.

The case p = 2 p=2 is easily solved by direct inspection. □ \Box

###### Remark 3.1

Recall that we have (with the notations of the above proof) P = P ⁡ ( n) = A ( n) ( mod p) P=P(n)=A^{(n)}\pmod{p} for n = p l n=p^{l} and introduce L = L ⁡ ( n) = B ( n) ( mod p) L=L(n)=B^{(n)}\pmod{p} and L ~ = L ~ ​ ( n) = C ( n) ( mod p) \tilde{L}=\tilde{L}(n)=C^{(n)}\pmod{p} where

 | A = ( 1 − 1 1 0), B = ( 1 0 − 1 − 1), C = ( 1 0 1 − 1). A=\left(\begin{array}[]{cc}{1}&{-1}\\ {1}&{0}\end{array}\right),B=\left(\begin{array}[]{cc}{1}&{0}\\ {-1}&{-1}\end{array}\right),C=\left(\begin{array}[]{cc}{1}&{0}\\ {1}&{-1}\end{array}\right). |  |

It is straightforward to check that L L and L ~ \tilde{L} have coefficients

 | l i, j = ( − 1) i ​ ( i j) ( mod p) and l ~ i, j = ( − 1) j ​ ( i j) ( mod p) l_{i,j}=(-1)^{i}{i\choose j}\pmod{p}\qquad\hbox{ and }\qquad\tilde{l}_{i,j}=(-1)^{j}{i\choose j}\pmod{p} |  |

for 0 ≤ i, j < n 0\leq i,j<n.

Then A 3 = − I A^{3}=-I, but ( − I) ( n) (-I)^{(n)} is the identity. Hence P 3 = I P^{3}=I. Also C 2 = I C^{2}=I and C ​ A ​ C = A − 1 CAC=A^{-1}. It follows that A A and C C generate a dihedral group of order 12, containing − I -I. Hence A ( n) = P A^{(n)}=P and C ( n) = L ~ C^{(n)}=\tilde{L} generate a dihedral group of order 6.

The group G p G_{p} generated by P P and L L depends on the prime p p (but not on the power l l of n = p l n=p^{l}). It is isomorphic to a subgroup of PGL 2 ​ ( 𝐅 p) \hbox{PGL}_{2}(\mathbf{F}_{p}). For all but finitely many primes p p, G p G_{p} is isomorphic to PSL 2 ​ ( 𝐅 p) \hbox{PSL}_{2}(\mathbf{F}_{p}) or PGL 2 ​ ( 𝐅 p) \hbox{PGL}_{2}(\mathbf{F}_{p}) according to whether − 1 -1 is or is not a square in 𝐅 p \mathbf{F}_{p}. The exceptional primes are 5 5, 7 7 and 29 29 where G p G_{p} has order 24 24, 42 42 and 120 120 respectively.

Proof of Theorem 1.3 Using Proposition 1.2, we can rewrite the equation to be proved as

 | ( t 3 − 1) k ​ det ( t ​ I − P ⁡ ( q − k)) ≡ det ( t ​ I − P ⁡ ( q)) ​ det ( t 2 ​ I + P ⁡ ( k)) ( mod p). (t^{3}-1)^{k}\det(tI-P(q-k))\equiv\det(tI-P(q))\det(t^{2}I+P(k))\pmod{p}. |  |

Here, and in the sequel, we write I I for I ⁡ ( n) I(n) whenever this notation is unambiguous; also we denote the zero matrix of any size by O O.

We now work over the field 𝐅 p \mathbf{F}_{p}. Unless otherwise stated vectors will be row vectors.

It is convenient to define a category ℰ = ℰ 𝐅 p \mathcal{E}=\mathcal{E}_{\mathbf{F}_{p}} as follows. Its objects will be pairs ( V, α) (V,\alpha) where V V is a finite-dimensional vector space over 𝐅 p \mathbf{F}_{p} and α \alpha is a vector space endomorphism of V V. A morphism ϕ: ( V, α) → ( W, β) \phi:(V,\alpha)\to(W,\beta) in ℰ \mathcal{E} will be a linear map ϕ: V → W \phi:V\to W with ϕ ∘ α = β ∘ ϕ \phi\circ\alpha=\beta\circ\phi. (In fact ℰ \mathcal{E} is equivalent to the category of finitely generated torsion modules over the polynomial ring 𝐅 p ​ [X] \mathbf{F}_{p}[X].) If ( V, α) (V,\alpha) is an object of ℰ \mathcal{E} we define χ ⁡ ( V, α, t) \chi(V,\alpha,t) as the characteristic polynomial of α \alpha acting on V V, that is, χ ⁡ ( V, α, t) = det ( t ​ I − A) \chi(V,\alpha,t)=\det(tI-A) where A A is a matrix representing α \alpha with respect to some basis of V V. An r r by r r matrix A A defines an object ( ( 𝐅 p) r, α) ((\mathbf{F}_{p})^{r},\alpha), denoted by ( ( 𝐅 p) r, A) ((\mathbf{F}_{p})^{r},A), where α \alpha is the endomorphism defined by A A.

It is easy to see that ℰ \mathcal{E} is an abelian category, and that if

 | 0 → ( V, α) → ( X, γ) → ( W, β) → 0 0\to(V,\alpha)\to(X,\gamma)\to(W,\beta)\to 0 |  |

is a short exact sequence, then χ ⁡ ( X, γ, t) = χ ⁡ ( V, α, t) ​ χ ​ ( W, β, t) \chi(X,\gamma,t)=\chi(V,\alpha,t)\chi(W,\beta,t). This is because there is a basis for X X with respect to which the matrix of γ \gamma (acting on row vectors from the the right) is

 | ( A O C B) \left(\begin{array}[]{cc}A&O\\ C&B\end{array}\right) |  |

where A A and B B are matrices representing α \alpha and β \beta respectively.

Set k ′ = q − k k^{\prime}=q-k. We can partition the Pascal matrices P ⁡ ( k ′) P(k^{\prime}) and P ⁡ ( q) P(q) as follows:

 | P ⁡ ( k ′) = ( A B B t C) and P ⁡ ( q) = ( A B D B t C O D t O O) P(k^{\prime})=\left(\begin{array}[]{cc}A&B\\ B^{t}&C\end{array}\right)\qquad\textrm{and}\qquad P(q)=\left(\begin{array}[]{ccc}A&B&D\\ B^{t}&C&O\\ D^{t}&O&O\end{array}\right) |  |

where A = P ⁡ ( k) A=P(k).

Let A ¯ \overline{A} denote the matrix obtained by rotating A A through 180 ∘ 180^{\circ}. Then P ​ ( q) 2 = P ⁡ ( q) ¯ P(q)^{2}=\overline{P(q)} and P ​ ( q) 3 = I P(q)^{3}=I. Hence

 | P ​ ( q) 2 = ( O O D t ¯ O C ¯ B t ¯ D ¯ B ¯ A ¯). P(q)^{2}=\left(\begin{array}[]{ccc}O&O&\overline{D^{t}}\\ O&\overline{C}&\overline{B^{t}}\\ \overline{D}&\overline{B}&\overline{A}\end{array}\right). |  |

Thus

 | A 2 + B ​ B t + D ​ D t = O A^{2}+BB^{t}+DD^{t}=O |  |

and so

 | P ​ ( k ′) 2 = ( − D ​ D t O O C ¯). P(k^{\prime})^{2}=\left(\begin{array}[]{cc}-DD^{t}&O\\ O&\overline{C}\end{array}\right). |  |

From P ​ ( q) 2 = P ⁡ ( q) ¯ P(q)^{2}=\overline{P(q)} it follows that A ​ D = D t ¯ AD=\overline{D^{t}} and from P ⁡ ( q) ¯ ​ P ​ ( q) = I \overline{P(q)}P(q)=I it follows that D t ¯ ​ D t = I \overline{D^{t}}D^{t}=I. Hence A ​ D ​ D t = I ADD^{t}=I and so

 | P ​ ( k ′) 2 = ( − A − 1 O O C ¯). P(k^{\prime})^{2}=\left(\begin{array}[]{cc}-A^{-1}&O\\ O&\overline{C}\end{array}\right). |  |

Let V = ( 𝐅 p) q V=(\mathbf{F}_{p})^{q} and X = ( 𝐅 p) 3 ​ k X=(\mathbf{F}_{p})^{3k}. Let

 | Q 1 = ( O I ⁡ ( k) O O O I ⁡ ( k) I ⁡ ( k) O O). Q_{1}=\left(\begin{array}[]{ccc}O&I(k)&O\\ O&O&I(k)\\ I(k)&O&O\end{array}\right). |  |

Let ϕ: X → V \phi:X\to V be the map defined by the matrix

 | ( I O O A B D O O D t ¯). \left(\begin{array}[]{ccc}I&O&O\\ A&B&D\\ O&O&\overline{D^{t}}\end{array}\right). |  |

Then

 | Q 1 ​ ( I O O A B D O O D t ¯) = ( A B D O O D t ¯ I O O) Q_{1}\left(\begin{array}[]{ccc}I&O&O\\ A&B&D\\ O&O&\overline{D^{t}}\end{array}\right)=\left(\begin{array}[]{ccc}A&B&D\\ O&O&\overline{D^{t}}\\ I&O&O\end{array}\right) |  |

and

 | ( I O O A B D O O D t ¯) ​ P ​ ( q) = ( I O O A B D O O D t ¯) ​ ( A B D B t C O D t O O) = ( A B D O O D t ¯ I O O) \left(\begin{array}[]{ccc}I&O&O\\ A&B&D\\ O&O&\overline{D^{t}}\end{array}\right)P(q)=\left(\begin{array}[]{ccc}I&O&O\\ A&B&D\\ O&O&\overline{D^{t}}\end{array}\right)\left(\begin{array}[]{ccc}A&B&D\\ B^{t}&C&O\\ D^{t}&O&O\end{array}\right)=\left(\begin{array}[]{ccc}A&B&D\\ O&O&\overline{D^{t}}\\ I&O&O\end{array}\right) |  |

where we have used the formulas P ​ ( q) 2 = P ⁡ ( q) ¯ P(q)^{2}=\overline{P(q)} and P ⁡ ( q) ¯ ​ P ​ ( q) = I \overline{P(q)}P(q)=I. Hence ϕ \phi is a morphism from ( ( 𝐅 p) 3 ​ k, Q 1) ((\mathbf{F}_{p})^{3k},Q_{1}) to ( ( 𝐅 p) q, P ⁡ ( q)) ((\mathbf{F}_{p})^{q},P(q)) in ℰ \mathcal{E}.

Let W = ( 𝐅 p) k ′ W=(\mathbf{F}_{p})^{k^{\prime}} and Y = ( 𝐅 p) 2 ​ k Y=(\mathbf{F}_{p})^{2k}. Let

 | Q 2 = ( O I ⁡ ( k) − A − 1 O). Q_{2}=\left(\begin{array}[]{cc}O&I(k)\\ -A^{-1}&O\\ \end{array}\right). |  |

Let ψ: Y → W \psi:Y\to W be the map defined by the matrix

 | ( I O A B). \left(\begin{array}[]{cc}I&O\\ A&B\end{array}\right). |  |

Then

 | Q 2 ​ ( I O A B) = ( A B − A − 1 O) Q_{2}\left(\begin{array}[]{cc}I&O\\ A&B\end{array}\right)=\left(\begin{array}[]{cc}A&B\\ -A^{-1}&O\end{array}\right) |  |

and

 | ( I O A B) ​ P ​ ( k ′) = ( I O A B) ​ ( A B B t C) = ( A B − A − 1 O) \left(\begin{array}[]{cc}I&O\\ A&B\end{array}\right)P(k^{\prime})=\left(\begin{array}[]{cc}I&O\\ A&B\end{array}\right)\left(\begin{array}[]{cc}A&B\\ B^{t}&C\end{array}\right)=\left(\begin{array}[]{cc}A&B\\ -A^{-1}&O\end{array}\right) |  |

where we have used the formula

 | P ​ ( k ′) 2 = ( − A − 1 O O C ¯). P(k^{\prime})^{2}=\left(\begin{array}[]{cc}-A^{-1}&O\\ O&\overline{C}\end{array}\right). |  |

Hence ψ \psi is a morphism from ( ( 𝐅 p) 2 ​ k, Q 2) ((\mathbf{F}_{p})^{2k},Q_{2}) to ( ( 𝐅 p) k ′, P ⁡ ( k ′)) ((\mathbf{F}_{p})^{k^{\prime}},P(k^{\prime})) in ℰ \mathcal{E}.

We need to divide into the cases k ≤ q / 3 k\leq q/3 and k ≥ q / 3 k\geq q/3. In the former cases ϕ \phi and ψ \psi are injective and in the latter case they are surjective. In the former case we consider their cokernels, in the latter case their kernels.

The matrix B B has size k k by q − 2 ​ k q-2k. If B B has rank k k (which is only possible if k ≤ q / 3 k\leq q/3) then ϕ \phi and ψ \psi are injective. If B B has rank q − 2 ​ k q-2k (which is only possible if k ≥ q / 3 k\geq q/3) then ϕ \phi and ψ \psi are surjective.

The matrix B B contains a submatrix

 | ( ( i + j + k i)) i, j = 0 r − 1 \left({i+j+k\choose i}\right)_{i,j=0}^{r-1} |  |

where r = min ⁡ ( k, q − 2 ​ k) r=\min(k,q-2k). This submatrix has determinant 1 1 (consider it as a matrix over 𝐙 \mathbf{Z} and reduce it to a Vandermonde matrix or see for instance [2]). Thus B B has rank r r and indeed ϕ \phi and ψ \psi are injective for k ≤ q / 3 k\leq q/3 and surjective for k ≥ q / 3 k\geq q/3.

Consider first the case where k ≤ q / 3 k\leq q/3. Let ( X 1, θ 1) (X_{1},\theta_{1}) and ( X 2, θ 2) (X_{2},\theta_{2}) denote the cokernels of ϕ: ( ( 𝐅 p) 3 ​ k, Q 1) → ( ( 𝐅 p) q, P ⁡ ( q)) \phi:((\mathbf{F}_{p})^{3k},Q_{1})\to((\mathbf{F}_{p})^{q},P(q)) and ψ: ( ( 𝐅 p) 2 ​ k, Q 2) → ( ( 𝐅 p) k ′, P ⁡ ( k ′)) \psi:((\mathbf{F}_{p})^{2k},Q_{2})\to((\mathbf{F}_{p})^{k^{\prime}},P(k^{\prime})) in ℰ \mathcal{E}. Then

 | χ ⁡ ( ( 𝐅 p) q, P ⁡ ( q), t) = χ ⁡ ( ( 𝐅 p) 3 ​ k, Q 1, t) ​ χ ​ ( X 1, θ 1, t) \chi((\mathbf{F}_{p})^{q},P(q),t)=\chi((\mathbf{F}_{p})^{3k},Q_{1},t)\chi(X_{1},\theta_{1},t) |  |

and

 | χ ⁡ ( ( 𝐅 p) k ′, P ⁡ ( k ′), t) = χ ⁡ ( ( 𝐅 p) 2 ​ k, Q 2, t) ​ χ ​ ( X 2, θ 2, t). \chi((\mathbf{F}_{p})^{k^{\prime}},P(k^{\prime}),t)=\chi((\mathbf{F}_{p})^{2k},Q_{2},t)\chi(X_{2},\theta_{2},t). |  |

It is apparent that

 | χ ⁡ ( ( 𝐅 p) 3 ​ k, Q 1, t) = ( t 3 − 1) k \chi((\mathbf{F}_{p})^{3k},Q_{1},t)=(t^{3}-1)^{k} |  |

and

 | χ ⁡ ( ( 𝐅 p) 2 ​ k, Q 2, t) = det ( t 2 ​ I + A − 1) = det ( t 2 ​ I + A) \chi((\mathbf{F}_{p})^{2k},Q_{2},t)=\det(t^{2}I+A^{-1})=\det(t^{2}I+A) |  |

as A A and A − 1 A^{-1} are similar. Hence

 | det ( t ​ I − P ⁡ ( q)) = ( t 3 − 1) k ​ χ ​ ( X 1, θ 1, t) \det(tI-P(q))=(t^{3}-1)^{k}\chi(X_{1},\theta_{1},t) |  |

and

 | det ( t ​ I − P ⁡ ( k ′)) = det ( t 2 ​ I + A) ​ χ ​ ( X 2, θ 2, t). \det(tI-P(k^{\prime}))=\det(t^{2}I+A)\chi(X_{2},\theta_{2},t). |  |

It suffices to prove that ( X 1, θ 1) (X_{1},\theta_{1}) and ( X 2, θ 2) (X_{2},\theta_{2}) are isomorphic in ℰ \mathcal{E}.

As D t ¯ \overline{D^{t}} is nonsingular, it is apparent that X 1 X_{1} is isomorphic to ( 𝐅 p) q − 2 ​ k / Y (\mathbf{F}_{p})^{q-2k}/Y where Y Y is the row space of B B and that the action of θ 1 \theta_{1} is induced by that of the matrix C C on ( 𝐅 p) q − 2 ​ k (\mathbf{F}_{p})^{q-2k}. It is even more apparent that X 2 X_{2} is isomorphic to ( 𝐅 p) q − 2 ​ k / Y (\mathbf{F}_{p})^{q-2k}/Y and that the action of θ 2 \theta_{2} is induced by C C. Hence ( X 1, θ 1) (X_{1},\theta_{1}) and ( X 2, θ 2) (X_{2},\theta_{2}) are isomorphic in ℰ \mathcal{E}. This completes the argument in the case k ≤ q / 3 k\leq q/3.

Now suppose that k ≥ q / 3 k\geq q/3. Let ( K 1, θ 1) (K_{1},\theta_{1}) and ( K 2, θ 2) (K_{2},\theta_{2}) denote the kernels of ϕ: ( ( 𝐅 p) 3 ​ k, Q 1) → ( ( 𝐅 p) q, P ⁡ ( q)) \phi:((\mathbf{F}_{p})^{3k},Q_{1})\to((\mathbf{F}_{p})^{q},P(q)) and ψ: ( ( 𝐅 p) 2 ​ k, Q 2) → ( ( 𝐅 p) k ′, P ⁡ ( k ′)) \psi:((\mathbf{F}_{p})^{2k},Q_{2})\to((\mathbf{F}_{p})^{k^{\prime}},P(k^{\prime})) in ℰ \mathcal{E}. Then

 | χ ⁡ ( ( 𝐅 p) q, P ⁡ ( q), t) ​ χ ​ ( K 1, θ 1, t) = χ ⁡ ( ( 𝐅 p) 3 ​ k, Q 1, t) \chi((\mathbf{F}_{p})^{q},P(q),t)\chi(K_{1},\theta_{1},t)=\chi((\mathbf{F}_{p})^{3k},Q_{1},t) |  |

and

 | χ ⁡ ( ( 𝐅 p) k ′, P ⁡ ( k ′), t) ​ χ ​ ( K 2, θ 2, t) = χ ⁡ ( ( 𝐅 p) 2 ​ k, Q 2, t). \chi((\mathbf{F}_{p})^{k^{\prime}},P(k^{\prime}),t)\chi(K_{2},\theta_{2},t)=\chi((\mathbf{F}_{p})^{2k},Q_{2},t). |  |

Hence

 | ( t 3 − 1) k det ( t ​ I − P ⁡ ( q)) = χ ⁡ ( K 1, θ 1, t) \frac{(t^{3}-1)^{k}}{\det(tI-P(q))}=\chi(K_{1},\theta_{1},t) |  |

and

 | det ( t 2 ​ I + A) det ( t ​ I − P ⁡ ( k ′)) = χ ⁡ ( K 2, θ 2, t). \frac{\det(t^{2}I+A)}{\det(tI-P(k^{\prime}))}=\chi(K_{2},\theta_{2},t). |  |

It suffices to prove that ( K 1, θ 1) (K_{1},\theta_{1}) and ( K 2, θ 2) (K_{2},\theta_{2}) are isomorphic in ℰ \mathcal{E}.

As D t ¯ \overline{D^{t}} is nonsingular and has inverse D t D^{t}, it is apparent that

 | K 1 = { ( − u A, u, − u D D t) = ( − u A, u, − u A − 1): u ∈ ( 𝐅 p) k, u B = 0 } K_{1}=\{(-uA,u,-uDD^{t})=(-uA,u,-uA^{-1}):u\in(\mathbf{F}_{p})^{k},uB=0\} |  |

and we have

 | ( − u ​ A, u, − u ​ A − 1) ​ Q 1 = ( − u ​ A − 1, − u ​ A, u). (-uA,u,-uA^{-1})Q_{1}=(-uA^{-1},-uA,u)\ . |  |

Also

 | K 2 = { ( − u A, u): u ∈ ( 𝐅 p) k, u B = 0 } K_{2}=\{(-uA,u):u\in(\mathbf{F}_{p})^{k},uB=0\} |  |

and

 | ( − u ​ A, u) ​ Q 2 = ( − u ​ A − 1, − u ​ A). (-uA,u)Q_{2}=(-uA^{-1},-uA)\ . |  |

Hence the linear map

 | ( − u ​ A, u, − u ​ A − 1) ⟼ ( − u ​ A, u) (-uA,u,-uA^{-1})\longmapsto(-uA,u) |  |

induces an isomorphism between ( K 1, θ 1) (K_{1},\theta_{1}) and ( K 2, θ 2) (K_{2},\theta_{2}). □ \Box

## 4 Proofs for the prime p = 2 p=2

Proof of Theorem 1.4. Set n = 2 l − k n=2^{l}-k and q = 2 l q=2^{l} where 1 ≤ k ≤ 2 l − 1 1\leq k\leq 2^{l-1}.

Theorem 1.3 yields then over 𝐅 2 \mathbf{F}_{2}

 | χ n ​ ( t) = χ q − k ​ ( t) = ( t 2 + t + 1) ( q − ϵ ⁡ ( q)) / 3 − k ​ ( t + 1) ( q + 2 ​ ϵ ​ ( q)) / 3 − k ​ det ( t ​ I + P ⁡ ( k)) 2 \chi_{n}(t)=\chi_{q-k}(t)=(t^{2}+t+1)^{(q-\epsilon(q))/3-k}(t+1)^{(q+2\epsilon(q))/3-k}\det(tI+P(k))^{2} |  |

since x ⟼ x 2 x\longmapsto x^{2} is an automorphism in characteristic 2 2.

By induction on l l, the only possible irreducible factors of det ( t ​ I ​ ( n) − P ⁡ ( n)) ( mod 2) \det(tI(n)-P(n))\pmod{2} are ( 1 + t) (1+t) and ( 1 + t + t 2) (1+t+t^{2}). The multiplicity μ ⁡ ( n) = μ ⁡ ( 2 l − k) \mu(n)=\mu(2^{l}-k) of the factor ( 1 + t) (1+t) in this polynomial is hence recursively defined by

 | μ ⁡ ( n) = 2 l + 2 ​ ( − 1) l 3 − k + 2 ​ μ ​ ( k) \mu(n)=\frac{2^{l}+2(-1)^{l}}{3}-k+2\mu(k) |  |

and coincides hence with the sequence γ \gamma of Theorem 1.4. The remaining factor of det ( t ​ I ​ ( n) − P ⁡ ( n)) ( mod 2) \det(tI(n)-P(n))\pmod{2} is hence given by ( 1 + t + t 2) γ 2 ​ ( n) (1+t+t^{2})^{\gamma_{2}(n)} where γ 2 ​ ( n) = 1 2 ​ ( n − γ ⁡ ( n)) \gamma_{2}(n)=\frac{1}{2}(n-\gamma(n)) and this proves the result. □ \Box

Proof of Theorem 1.5. We have for 0 ≤ k ≤ 2 l − 1 0\leq k\leq 2^{l-1}

 | γ ⁡ ( 2 l + k) \displaystyle\gamma(2^{l}+k) | = \displaystyle= | γ ⁡ ( 2 l + 1 − ( 2 l − k)) \displaystyle\gamma(2^{l+1}-(2^{l}-k)) |  |

 |  | = \displaystyle= | 2 l + 1 − 2 ​ ( − 1) l 3 − 2 l + k + 2 ​ γ ​ ( 2 l − k) \displaystyle\frac{2^{l+1}-2(-1)^{l}}{3}-2^{l}+k+2\gamma(2^{l}-k) |  |

 |  | = \displaystyle= | 2 l + 1 − 2 ​ ( − 1) l 3 − 2 l + k + 2 ​ 2 l + 2 ​ ( − 1) l 3 − 2 ​ k + 4 ​ γ ​ ( k) \displaystyle\frac{2^{l+1}-2(-1)^{l}}{3}-2^{l}+k+2\frac{2^{l}+2(-1)^{l}}{3}-2k+4\gamma(k) |  |

which is assertion (i).

We have for all 2 l − 2 ≤ k ≤ 2 l − 1 2^{l-2}\leq k\leq 2^{l-1}

 | γ ⁡ ( 2 l − k) \displaystyle\gamma(2^{l}-k) | = \displaystyle= | 2 l + 2 ​ ( − 1) l 3 − k + γ ⁡ ( k) + γ ⁡ ( 2 l − 1 − ( 2 l − 1 − k)) \displaystyle\frac{2^{l}+2(-1)^{l}}{3}-k+\gamma(k)+\gamma(2^{l-1}-(2^{l-1}-k)) |  |

 |  | = \displaystyle= | 2 l + 2 ​ ( − 1) l 3 − k + γ ⁡ ( k) + 2 l − 1 − 2 ​ ( − 1) l 3 − 2 l − 1 + k + 2 ​ γ ​ ( 2 l − 1 − k) \displaystyle\frac{2^{l}+2(-1)^{l}}{3}-k+\gamma(k)+\frac{2^{l-1}-2(-1)^{l}}{3}-2^{l-1}+k+2\gamma(2^{l-1}-k) |  |

 |  | = \displaystyle= | γ ⁡ ( k) + 2 ​ γ ​ ( 2 l − 1 − k) \displaystyle\gamma(k)+2\gamma(2^{l-1}-k) |  |

which proves assertion (ii).

Similarly, we have for 1 ≤ k ≤ 2 l 1\leq k\leq 2^{l}

 | γ ⁡ ( 2 l + k) − γ ⁡ ( 2 l + k − 1) \displaystyle\gamma(2^{l}+k)-\gamma(2^{l}+k-1) | = \displaystyle= | γ ⁡ ( 2 l + 1 − ( 2 l − k)) − γ ⁡ ( 2 l + 1 − ( 2 l − k + 1)) \displaystyle\gamma(2^{l+1}-(2^{l}-k))-\gamma(2^{l+1}-(2^{l}-k+1)) |  |

 |  | = \displaystyle= | 1 + 2 ​ γ ​ ( 2 l − k) − 2 ​ γ ​ ( 2 l − k + 1) \displaystyle 1+2\gamma(2^{l}-k)-2\gamma(2^{l}-k+1) |  |

which proves assertion (iii).

Writing 2 ​ n = 2 l − 2 ​ k 2n=2^{l}-2k with 1 ≤ k ≤ 2 l − 2 1\leq k\leq 2^{l-2} we have, using induction on n n,

 | γ ⁡ ( 2 l − 2 ​ k) \displaystyle\gamma(2^{l}-2k) | = \displaystyle= | 2 l − ( − 1) l 3 − 2 ​ k + 2 ​ γ ​ ( 2 ​ k) \displaystyle\frac{2^{l}-(-1)^{l}}{3}-2k+2\gamma(2k) |  |

 |  | = \displaystyle= | 2 l − ( − 1) l 3 − 2 ​ k + 2 ​ ( k − γ ⁡ ( k)) \displaystyle\frac{2^{l}-(-1)^{l}}{3}-2k+2\left(k-\gamma(k)\right) |  |

 |  | = \displaystyle= | ( 2 l − 1 − k) − ( 2 l − 1 − ( − 1) l − 1 3 − k + 2 ​ γ ​ ( k)) \displaystyle\left(2^{l-1}-k\right)-\left(\frac{2^{l-1}-(-1)^{l-1}}{3}-k+2\gamma(k)\right) |  |

 |  | = \displaystyle= | ( 2 l − 1 − k) − γ ⁡ ( 2 l − 1 − k) \displaystyle\left(2^{l-1}-k\right)-\gamma(2^{l-1}-k) |  |

which proves the first equality of assertion (iv) (this equality follows also from the fact that P ⁡ ( 2 ​ n) P(2n) is the Kronecker product of P ⁡ ( n) P(n) with P ⁡ ( 2) P(2) over 𝐅 2 \mathbf{F}_{2}).

The second identity of assertion (iv) amounts to the equality

 | γ ⁡ ( 2 ​ n − 1) − γ ⁡ ( 2 ​ n) = 4 b ⁡ ( 2 ​ n − 1) − 1 3. \gamma(2n-1)-\gamma(2n)=\frac{4^{b(2n-1)}-1}{3}\ . |  |

We prove first by induction on n n that this identity is equivalent to the last identity.

The last identity and induction yield

 | γ ⁡ ( 2 ​ n − 1) − γ ⁡ ( 2 ​ n) \displaystyle\gamma(2n-1)-\gamma(2n) | = \displaystyle= | γ ⁡ ( 2 ​ n − 1) − γ ⁡ ( 2 ​ n − 2) + γ ⁡ ( 2 ​ n − 2) − γ ⁡ ( 2 ​ n) \displaystyle\gamma(2n-1)-\gamma(2n-2)+\gamma(2n-2)-\gamma(2n) |  |

 |  | = \displaystyle= | 2 1 + 2 ​ b ​ ( n − 1) + 1 3 − 1 + γ ⁡ ( n) − γ ⁡ ( n − 1). \displaystyle\frac{2^{1+2b(n-1)}+1}{3}-1+\gamma(n)-\gamma(n-1). |  |

We now divide into cases according to the parity of n n.

Suppose first that n = 2 ​ m n=2m is even. Then inductively

 | γ ⁡ ( n) − γ ⁡ ( n − 1) = γ ⁡ ( 2 ​ m) − γ ⁡ ( 2 ​ m − 1) = − 4 b ⁡ ( 2 ​ m − 1) − 1 3 = − 4 b ⁡ ( n − 1) − 1 3 \gamma(n)-\gamma(n-1)=\gamma(2m)-\gamma(2m-1)=-\frac{4^{b(2m-1)-1}}{3}=-\frac{4^{b(n-1)-1}}{3} |  |

Hence

 | γ ⁡ ( 2 ​ n − 1) − γ ⁡ ( 2 ​ n) = − 1 + 2 1 + 2 ​ b ​ ( n − 1) + 1 3 − 2 2 ​ b ​ ( n − 1) − 1 3 = 2 2 ​ b ​ ( n − 1) − 1 3. \gamma(2n-1)-\gamma(2n)=-1+\frac{2^{1+2b(n-1)}+1}{3}-\frac{2^{2b(n-1)}-1}{3}=\frac{2^{2b(n-1)}-1}{3}. |  |

But

 | 2 2 ​ b ​ ( n − 1) = 4 b ⁡ ( n − 1) = 4 b ⁡ ( 2 ​ n − 1) 2^{2b(n-1)}=4^{b(n-1)}=4^{b(2n-1)} |  |

as the binary representation of n − 1 n-1 ends in 1 1 and that of 2 ​ n − 1 2n-1 is obtained by appending 1 1.

Now suppose that n = 2 ​ m + 1 n=2m+1 is odd. Then

 | γ ⁡ ( n) − γ ⁡ ( n − 1) = γ ⁡ ( 2 ​ m + 1) − γ ⁡ ( 2 ​ m) = 2 1 + 2 ​ b ​ ( m) + 1 3 = 2 1 + 2 ​ b ​ ( 2 ​ m) + 1 3. \gamma(n)-\gamma(n-1)=\gamma(2m+1)-\gamma(2m)=\frac{2^{1+2b(m)}+1}{3}=\frac{2^{1+2b(2m)}+1}{3}. |  |

Hence

 | γ ⁡ ( 2 ​ n − 1) − γ ⁡ ( 2 ​ n) = − 1 + 2 1 + 2 ​ b ​ ( n − 1) + 1 3 + 2 1 + 2 ​ b ​ ( n − 1) + 1 3 = 2 2 + 2 ​ b ​ ( n − 1) − 1 3. \gamma(2n-1)-\gamma(2n)=-1+\frac{2^{1+2b(n-1)}+1}{3}+\frac{2^{1+2b(n-1)}+1}{3}=\frac{2^{2+2b(n-1)}-1}{3}. |  |

But

 | 2 2 + 2 ​ b ​ ( n − 1) = 4 1 + b ⁡ ( n − 1) = 4 b ⁡ ( 2 ​ n − 1) 2^{2+2b(n-1)}=4^{1+b(n-1)}=4^{b(2n-1)} |  |

as the binary representation of n − 1 n-1 ends in 0 0 and that of 2 ​ n − 1 2n-1 is obtained by appending 1 1.

This completes the proof of equivalence of the two last identities in assertion (iv).

We prove now the last identity by induction on n n.

The last identity of assertion (iv) is equivalent to

 | γ ⁡ ( 2 ​ n + 1) − γ ⁡ ( 2 ​ n) = 2 1 + 2 ​ b ​ ( n) + 1 3. \gamma(2n+1)-\gamma(2n)=\frac{2^{1+2b(n)}+1}{3}\ . |  |

Writing 2 ​ n + 1 = 2 l + k 2n+1=2^{l}+k with 1 ≤ k < 2 l 1\leq k<2^{l} and applying assertion (iii) and the second identity of assertion (iv) (which holds by induction) we have

 | γ ⁡ ( 2 ​ n + 1) − γ ⁡ ( 2 ​ n) \displaystyle\gamma(2n+1)-\gamma(2n) | = \displaystyle= | 1 + 2 ​ γ ​ ( 2 l − k) − 2 ​ γ ​ ( 2 l + 1 − k) \displaystyle 1+2\gamma(2^{l}-k)-2\gamma(2^{l}+1-k) |  |

 |  | = \displaystyle= | 1 + 2 ​ 4 b ⁡ ( 2 l − k) − 1 3 \displaystyle 1+2\frac{4^{b(2^{l}-k)}-1}{3} |  |

 |  | = \displaystyle= | 2 1 + 2 ​ b ​ ( 2 l − k) + 1 3 \displaystyle\frac{2^{1+2b(2^{l}-k)}+1}{3} |  |

Since ( 2 l + k − 1) + ( 2 l − k) = 2 l + 1 − 1 (2^{l}+k-1)+(2^{l}-k)=2^{l+1}-1 and since 2 l + k − 1 2^{l}+k-1 is even and greater than 2 l − k 2^{l}-k, they have the same number of blocks 1 ​ … ​ 1 1\dots 1 in their binary expansion. This shows b ⁡ ( 2 l − k) = b ⁡ ( 2 ​ n) = b ⁡ ( n) b(2^{l}-k)=b(2n)=b(n) and establishes the last identity of assertion (iv). □ \Box

The first author wishes to thank J.-P. Allouche, F. Sigrist, U. Vishne and A. Wassermann for interesting comments and remarks.

## References

- [1] J.-P. Allouche, J. Shallit, The ubiquitous Prouhet-Thue-Morse sequence, Proceedings of SETA 98 (C. Ding, T. Helleseth, H. Niederreiter, editors), Springer (1999).
- [2] R. Bacher, Determinants of matrices related to the Pascal triangle, J. de Th. des Nombres de Bordeaux 14 (2002), 19–41.
- [3] C. Krattenthaler, *Advanced determinant calculus*, Sémin. Lothar. Comb. 42, B42q (1999), 67 pages.
- [4] W.F. Lunnon, *The Pascal matrix*, Fib. Quart. vol. 15 (1977), 201–204.

Roland Bacher, Institut Fourier, UMR 5582, Laboratoire de Mathématiques, BP 74, 38402 St. Martin d’Hères Cedex, France, Roland.Bacher@ujf-grenoble.fr

Robin Chapman, University of Exeter, School of Mathematical Sciences, North Park Road, EX4 4QE Exeter, UK, rjc@maths.ex.ac.uk


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
