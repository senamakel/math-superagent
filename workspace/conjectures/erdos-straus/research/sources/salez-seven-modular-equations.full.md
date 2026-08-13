<!-- source: https://arxiv.org/html/1406.6307v1 | converted from HTML -->

The Erdős-Straus conjectureNew modular equations and checking up to = N 10 17

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1406.6307v1 [math.NT] 24 Jun 2014

# The Erdős-Straus conjecture
New modular equations
and checking up to N = 10 17 N=10^{17}

Serge E. Salez

###### Abstract

In 1999 Allan Swett [5] checked (in 150 hours) the Erdős-Straus conjecture up to N = 10 14 N=10^{14} with a sieve based on a single modular equation. After having proved the existence of a "complete" set of seven modular equations (including three new ones), this paper offers an optimized sieve based on these equations. A program written in C++ (and given elsewhere) allows then to make a checking whose running time, on a typical computer 1 1 1 AMD TurionII Dual-Core Mobile M250 ( 64 64 bits, 16 100 16\,100 MIPS)., range from few minutes for N = 10 14 N=10^{14} to about 16 hours for N = 10 17 N=10^{17}.

## 1 Basic formulas

A fraction is said to be k k -Egyptian if it is the sum of at most k k positive unit fractions (i.e with numerator equal to 1). The Erdős-Straus conjecture claims that 4 / n 4/n is a 3-Egyptian fraction for any n > 1 n>1.

### 1.1 Reduction

Through the identities

 | 1 t = 1 t + 1 + 1 t ⁡ ( t + 1) \frac{1}{t}=\frac{1}{t+1}+\frac{1}{t(t+1)} |  |

 | 2 2 ​ t − 1 = 1 t + 1 t ⁡ ( 2 ​ t − 1) \frac{2}{2t-1}=\frac{1}{t}+\frac{1}{t(2t-1)} |  |

it is equivalent (for n > 2 n>2) to require having exactly 3 different unit fractions, what we shall do thereafter.

On the other hand, the identities

 | 4 3 ​ t − 1 = 1 t + 1 3 ​ t − 1 + 1 t ⁡ ( 3 ​ t − 1) \frac{4}{3t-1}=\frac{1}{t}+\frac{1}{3t-1}+\frac{1}{t(3t-1)} |  |

 | 4 4 ​ t − 1 = 1 t + 1 t ⁡ ( 4 ​ t − 1) \frac{4}{4t-1}=\frac{1}{t}+\frac{1}{t(4t-1)} |  |

 | 4 8 ​ t − 3 = 1 2 ​ t + 1 t ⁡ ( 8 ​ t − 3) + 1 2 ​ t ​ ( 8 ​ t − 3) \frac{4}{8t-3}=\frac{1}{2t}+\frac{1}{t(8t-3)}+\frac{1}{2t(8t-3)} |  |

show that the conjecture is verified if n = − 1 mod 3 n=-1\mod 3 or n = − 1 mod 4 n=-1\mod 4 or n = − 3 mod 8 n=-3\mod 8. Moreover, if 4 / n 4/n is 3-Egyptian then 4 / k ​ n 4/kn is too.

To conclude, it is then sufficient to prove that 4 / p 4/p is 3-Egyptian, for any prime integer p p such that p = 1 mod 24 p=1\mod 24.

### 1.2 Rosati’s formulas

The following proposition is due (according to Mordell 2 2 2 So, unlike most paper, we don’t attribute to Mordell what Mordell himself attribute to others mathematicians. In his book [2], often quoted, the four pages given to this conjecture doesn’t introduce a personal work but report briefly some papers whose sources are scrupulously pointed out : hence, it is absolutely incorrect to speak of ”Mordell’s theorem” or of ”Mordell’s formulas”. On a different scale, it should be better not to remake what was done with Pell’s equation.) to Rosati [3]. The proof needs only simple calculations and has been given many a time. This one is nevertheless original and standardize the notations.

We set 𝒜 = ℤ \mathcal{A}=\mathbb{Z}. Let 𝒜 + \mathcal{A}_{+} be the set of strictly positive elements of ℤ \mathbb{Z}. In this context, we call prime element an odd prime integer.

###### Proposition 1

Let p p a prime element. The fraction 4 / p 4/p is 3-Egyptian if and only if there exists four elements of 𝒜 + \mathcal{A}_{+} denoted by A A, B B, C C, D D such that

 | 4 ​ A ​ B ​ C ​ D = A + B + p ​ C and ( A ​ B ​ D, p) = 1 4ABCD=A+B+pC\mathrm{\quad and\quad}(ABD,p)=1 |  | (1) |

or

 | 4 ​ A ​ B ​ C ​ D = p ⁡ ( A + B) + C and ( A ​ B ​ C ​ D, p) = 1 4ABCD=p(A+B)+C\mathrm{\quad and\quad}(ABCD,p)=1 |  | (2) |

Proof If we assume that 4 / p 4/p is 3-Egyptian, then there exists 3 elements of 𝒜 + \mathcal{A}_{+} denoted by X 1, X 2, X 3 X_{1},X_{2},X_{3} such that

 | 4 p = 1 X 1 + 1 X 2 + 1 X 3 \dfrac{4}{p}=\dfrac{1}{X_{1}}+\dfrac{1}{X_{2}}+\dfrac{1}{X_{3}} |  | (3) |

The X i X_{i} are not all divisible by p p for otherwise we would have

 | 4 = 1 X 1 / p + 1 X 2 / p + 1 X 3 / p ⩽ 3 4=\dfrac{1}{X_{1}/p}+\dfrac{1}{X_{2}/p}+\dfrac{1}{X_{3}/p}\leqslant 3 |  |

In view of ( 3) it follows that

 | 4 ​ X 1 ​ X 2 ​ X 3 = p ⁡ ( X 2 ​ X 3 + X 3 ​ X 1 + X 1 ​ X 2) 4X_{1}X_{2}X_{3}=p(X_{2}X_{3}+X_{3}X_{1}+X_{1}X_{2}) |  |

which shows that p p divides at least one of the X i X_{i}. Hence we may set x i = X i / p i x_{i}=X_{i}/p_{i} where

 | p 1 = p 2 = 1, p 3 = p and ( x 1 x 2, p) = 1 p_{1}=p_{2}=1,\quad p_{3}=p\mathrm{\quad and\quad}(x_{1}x_{2},p)=1 |  |

or

 | p 1 = p 2 = p, p 3 = 1 and ( x 3, p) = 1 p_{1}=p_{2}=p,\quad p_{3}=1\mathrm{\quad and\quad}(x_{3},p)=1 |  |

depending on p p divides exactly one or two X i X_{i}.

Therefore, since p 2 ​ p 3 = p p_{2}p_{3}=p

 | 4 ​ p 1 ​ p ​ x 1 ​ x 2 ​ x 3 = p ⁡ ( p 2 ​ p 3 ​ x 2 ​ x 3 + p 3 ​ p 1 ​ x 3 ​ x 1 + p 1 ​ p 2 ​ x 1 ​ x 2) 4p_{1}p\;x_{1}x_{2}x_{3}=p(p_{2}p_{3}x_{2}x_{3}+p_{3}p_{1}x_{3}x_{1}+p_{1}p_{2}x_{1}x_{2}) |  |

and hence

 | 4 ​ x 1 ​ x 2 ​ x 3 = p 3 ​ x 2 ​ x 3 + p 3 ​ x 3 ​ x 1 + p 2 ​ x 1 ​ x 2 4x_{1}x_{2}x_{3}=p_{3}x_{2}x_{3}+p_{3}x_{3}x_{1}+p_{2}x_{1}x_{2} |  |

We set D = ( x 1, x 2, x 3) D=(x_{1},x_{2},x_{3}) and x i ′ = x i / D x^{\prime}_{i}=x_{i}/D. Then

 | 4 ​ D ​ x 1 ′ ​ x 2 ′ ​ x 3 ′ = p 3 ​ x 2 ′ ​ x 3 ′ + p 3 ​ x 3 ′ ​ x 1 ′ + p 2 ​ x 1 ′ ​ x 2 ′ 4Dx^{\prime}_{1}x^{\prime}_{2}x^{\prime}_{3}=p_{3}x^{\prime}_{2}x^{\prime}_{3}+p_{3}x^{\prime}_{3}x^{\prime}_{1}+p_{2}x^{\prime}_{1}x^{\prime}_{2} |  |

At last we set

 | A = ( x 2 ′, x 3 ′), B = ( x 3 ′, x 1 ′), C = ( x 1 ′, x 2 ′) A=(x^{\prime}_{2},x^{\prime}_{3}),\quad B=(x^{\prime}_{3},x^{\prime}_{1}),\quad C=(x^{\prime}_{1},x^{\prime}_{2}) |  |

Since ( x 1 ′, x 2 ′, x 3 ′) = 1 (x^{\prime}_{1},x^{\prime}_{2},x^{\prime}_{3})=1 it follows that A, B, C A,B,C are pairwise relatively prime. So, we may write

 | x 1 ′ = B ​ C ​ t 1, x 2 ′ = C ​ A ​ t 2, x 3 ′ = A ​ B ​ t 3 x^{\prime}_{1}=BCt_{1},\quad x^{\prime}_{2}=CAt_{2},\quad x^{\prime}_{3}=ABt_{3} |  |

where t i ∈ 𝒜 + t_{i}\in\mathcal{A}_{+} are pairwise relatively prime. We note that

 | ( t 1, A) = ( t 2, B) = ( t 3, C) = 1 (t_{1},A)=(t_{2},B)=(t_{3},C)=1 |  |

With these notations, we have

 | 4 ​ D ​ B ​ C ​ C ​ A ​ A ​ B ​ t 1 ​ t 2 ​ t 3 = p 3 ​ C ​ A ​ A ​ B ​ t 2 ​ t 3 + p 3 ​ A ​ B ​ B ​ C ​ t 3 ​ t 1 + p 2 ​ B ​ C ​ C ​ A ​ t 1 ​ t 2 4D\,BC\,CA\,AB\,t_{1}t_{2}t_{3}=p_{3}CA\,AB\,t_{2}t_{3}+p_{3}AB\,BC\,t_{3}t_{1}+p_{2}BC\,CA\,t_{1}t_{2} |  |

and hence

 | 4 ​ A ​ B ​ C ​ D ​ t 1 ​ t 2 ​ t 3 = p 3 ​ A ​ t 2 ​ t 3 + p 3 ​ B ​ t 3 ​ t 1 + p 2 ​ C ​ t 1 ​ t 2 4ABCDt_{1}t_{2}t_{3}=p_{3}At_{2}t_{3}+p_{3}Bt_{3}t_{1}+p_{2}Ct_{1}t_{2} |  |

It follows that t 1 | p 3 ​ A ​ t 2 ​ t 3 t_{1}\mid p_{3}At_{2}t_{3} which reduce to t 1 | p 3 t_{1}\mid p_{3} and hence t 1 = 1 t_{1}=1 for ( x 1, p 3) = 1 (x_{1},p_{3})=1. Similar arguments lead to t 2 = 1 t_{2}=1 and t 3 = 1 t_{3}=1. Finally

 | 4 ​ A ​ B ​ C ​ D = p 3 ​ A + p 3 ​ B + p 2 ​ C 4ABCD=p_{3}A+p_{3}B+p_{2}C |  | (4) |

Conversely, if we assume that A, B, C, D A,B,C,D verify ( 4), we divide by p ​ A ​ B ​ C ​ D pABCD and then

 | 4 p = 1 p 1 ​ B ​ C ​ D + 1 p 2 ​ A ​ C ​ D + 1 p 3 ​ A ​ B ​ D \frac{4}{p}=\frac{1}{p_{1}BCD}+\frac{1}{p_{2}ACD}+\frac{1}{p_{3}ABD} |  |

which shows that 4 / p 4/p is 3-Egyptian 3 3 3 For all purpose, we may write x = T / A x=T/A, y = T / B y=T/B, z = T / C z=T/C where T = A ​ B ​ C ​ D T=ABCD.. ■ \blacksquare

We observe that if p p is not prime, ( 4) is still sufficient but no more necessary.

### 1.3 Notations

Henceforth, we systematically make use of the notations of Proposition 1. We add also E ∈ 𝒜 + E\in\mathcal{A}_{+} and F ∈ 𝒜 + F\in\mathcal{A}_{+} as follow.

By ( 4) and since ( C, p 3) = 1 (C,p_{3})=1, we have C | A + B C\mid A+B. If we write E = ( A + B) / C E=(A+B)/C then E ∈ 𝒜 + E\in\mathcal{A}_{+} and ( 4) is equivalent to

 | { 4 ​ A ​ B ​ D = p 3 ​ E + p 2 A + B = C ​ E \begin{cases}4ABD=p_{3}E+p_{2}\\ A+B=CE\end{cases} |  | (5) |

The relation ( 4) may be rewritten ( 4 ​ B ​ C ​ D − p 3) ​ A = p 3 ​ B + p 2 ​ C (4BCD-p_{3})A=p_{3}B+p_{2}C. We set F = 4 ​ B ​ C ​ D − p 3 F=4BCD-p_{3} and then ( 4) is equivalent to

 | { F ​ A = p 3 ​ B + p 2 ​ C ​ 2 F + p 3 = 4 ​ B ​ C ​ D \begin{cases}FA=p_{3}B+p_{2}C2\\ F+p_{3}=4BCD\end{cases} |  | (6) |

The second equation of ( 6) shows that F ∈ 𝒜 F\in\mathcal{A}, the first one that F ∈ 𝒜 + F\in\mathcal{A}_{+}.

Moreover, by ( 5) we have 4 ​ ( C ​ E − B) ​ B ​ D = p 3 ​ E + p 2 4(CE-B)BD=p_{3}E+p_{2} and then ( 4 ​ B ​ C ​ D − p 3) ​ E = 4 ​ B 2 ​ D + p 2 (4BCD-p_{3})E=4B^{2}D+p_{2}. Whence

 | F ​ E = 4 ​ B 2 ​ D + p 2 FE=4B^{2}D+p_{2} |  | (7) |

## 2 Generalization

### 2.1 Definitions

Like for the integers, we say that a rational fraction is k k -Egyptian if it is the sum of at most k k inverses of polynomials of ℤ ⁡ [X] \mathbb{Z}[X].

We set 𝒜 = ℤ ⁡ [X] \mathcal{A}=\mathbb{Z}[X]. Let 𝒜 + \mathcal{A}_{+} be the set of polynomials of ℤ ⁡ [X] \mathbb{Z}[X] whose leading coefficient is strictly positive. In this context, we call prime element an irreducible polynomial of 𝒜 + \mathcal{A}_{+}.

In the ring 𝒜 \mathcal{A}, the fundamental theorem of arithmetic is true and the GCD is unique if we request it has to be in 𝒜 + \mathcal{A}_{+}. Hence, the Proposition 1 holds also in this new context, without any change neither in the text nor in the proof. It is the same for E E and F F as well as the related equations.

### 2.2 First application

###### Proposition 2

(Schinzel’s Theorem )
Let a > 0 a>0 and b b such as ( a, b) = 1 (a,b)=1. If 4 / ( a ​ t + b) 4/(at+b) is 3-Egyptian 4 4 4 a ​ t + b at+b is supposed to be a polynomial (abuse of notation). then b b is a quadratic non residue modulo a a.

Proof We write p ⁡ ( t) = a ​ t + b p(t)=at+b. There exists τ \tau such as the polynomials p, A, B, C, D, E p,A,B,C,D,E take strictly positive values for t > τ t>\tau.

Depending on the case, the equation 4 ​ ( B − C ​ E) ​ B ​ D = p 3 ​ E + p 2 4(B-CE)BD=p_{3}E+p_{2} may be written

 | 4 ​ ( C ​ E − B) ​ B ​ D = E + p or 4 ​ ( C ​ E − B) ​ B ​ D = p ​ E + 1 4(CE-B)BD=E+p\mathrm{\quad or\quad}4(CE-B)BD=pE+1 |  |

So we have

 | p = ( 4 ​ B ​ C ​ D − 1) ​ E − 4 ​ B 2 ​ D or p ​ E 2 = ( 4 ​ B ​ C ​ D ​ E − 1) ​ E − 4 ​ B 2 ​ D ​ E p=(4BCD-1)E-4B^{2}D\mathrm{\quad or\quad}pE^{2}=(4BCDE-1)E-4B^{2}DE |  |

and then, if we write D ′ = D ​ E D^{\prime}=DE

 | p = − 4 ​ B 2 ​ D mod 4 ​ B ​ C ​ D − 1 or p ​ E 2 = − 4 ​ B 2 ​ D ′ mod 4 ​ B ​ C ​ D ′ − 1 p=-4B^{2}D\mod 4BCD-1\mathrm{\quad or\quad}pE^{2}=-4B^{2}D^{\prime}\mod 4BCD^{\prime}-1 |  |

If b b is a quadratic residue modulo a a, there exists an integer k > τ k>\tau such that a ​ k + b ak+b is a square. If t = k t=k, it follows from propriety of the Jacobi symbol 5 5 5 The same notations p, A, B, C, D, E p,A,B,C,D,E are still used for the values at t = k t=k of these polynomials. By the way, a similar calculation using the Kronecker symbol is made in the paper of Yamamoto [6].

 | ( p 4 ​ B ​ C ​ D − 1) = ( − 4 ​ B 2 ​ D 4 ​ B ​ C ​ D − 1) = − 1 \left(\dfrac{p}{4BCD-1}\right)=\left(\dfrac{-4B^{2}D}{4BCD-1}\right)=-1 |  |

which contradicts the fact that p p is a square. Idem with p ​ E 2 pE^{2}.

More precisely, if we write D = 2 α ​ m D=2^{\alpha}m where m m is odd, we obtain

 | ( − 4 ​ B 2 ​ D 4 ​ B ​ C ​ D − 1) = − ( D 4 ​ B ​ C ​ D − 1) = − ( 2 4 ​ B ​ C ​ D − 1) α ​ ( m 4 ​ B ​ C ​ D − 1) \left(\dfrac{-4B^{2}D}{4BCD-1}\right)=-\left(\dfrac{D}{4BCD-1}\right)=-\left(\dfrac{2}{4BCD-1}\right)^{\alpha}\left(\dfrac{m}{4BCD-1}\right) |  |

If α > 0 \alpha>0 then 4 ​ A ​ B ​ C ​ D − 1 = 7 mod 8 4ABCD-1=7\mod 8 and this implies

 | ( 2 4 ​ B ​ C ​ D − 1) = 1 \left(\dfrac{2}{4BCD-1}\right)=1 |  |

For the second factor, using the law of quadratic reciprocity, we have

 | ( m 4 ​ B ​ C ​ D − 1) = ( − 1) ( m − 1) / 2 ​ ( 4 ​ B ​ C ​ D − 1 m) = ( − 1) ( m − 1) / 2 ​ ( − 1 m) \left(\dfrac{m}{4BCD-1}\right)=(-1)^{(m-1)/2}\left(\dfrac{4BCD-1}{m}\right)=(-1)^{(m-1)/2}\left(\dfrac{-1}{m}\right) |  |

and then

 | ( m 4 ​ B ​ C ​ D − 1) = ( − 1) ( m − 1) / 2 ​ ( − 1) ( m − 1) / 2 = 1 \left(\dfrac{m}{4BCD-1}\right)=(-1)^{(m-1)/2}(-1)^{(m-1)/2}=1 |  |

■ \blacksquare

### 2.3 Modular equations

For greater convenience, we call modular equation a modular equation (or a system of modular equations) *with constant coefficients*.

Since A A and B B play symmetrical roles, we may suppose 6 6 6 The arbitrary definition of F F ( A A is factored out rather than B B) was made in anticipation of this relation. Otherwise we could not have d ∘ ​ F = 0 d^{\,\circ}F=0. that d ∘ ​ B ⩽ d ∘ ​ A d^{\,\circ}B\leqslant d^{\,\circ}A, where d ∘ d^{\,\circ} is the degree of a polynomial.

###### Lemma 1

Let p p be a prime polynomial of degree 1.

1. i)

If the relation ( 1) 4 ​ A ​ B ​ C ​ D = A + B + p ​ C 4ABCD=A+B+pC holds, then

 |

 | d ∘ ​ A = 1 d ∘ ​ B = 0 d ∘ ​ C = 0 d ∘ ​ D = 0 \displaystyle d^{\,\circ}A=1\qquad d^{\,\circ}B=0\qquad d^{\,\circ}C=0\qquad d^{\,\circ}D=0\qquad |  | (8a) |

 | d ∘ ​ A = 0 d ∘ ​ B = 0 d ∘ ​ C = 0 d ∘ ​ D = 1 \displaystyle d^{\,\circ}A=0\qquad d^{\,\circ}B=0\qquad d^{\,\circ}C=0\qquad d^{\,\circ}D=1\qquad |  | (8b) |

 | d ∘ ​ A = 1 d ∘ ​ B = 0 d ∘ ​ C = 1 d ∘ ​ D = 0 \displaystyle d^{\,\circ}A=1\qquad d^{\,\circ}B=0\qquad d^{\,\circ}C=1\qquad d^{\,\circ}D=0\qquad |  | (8c) |

2. ii)

If the relation ( 2) 4 ​ A ​ B ​ C ​ D = p ⁡ ( A + B) + C 4ABCD=p(A+B)+C holds, then

 |

 | d ∘ ​ A = 0 d ∘ ​ B = 0 d ∘ ​ C = 0 d ∘ ​ D = 1 \displaystyle d^{\,\circ}A=0\qquad d^{\,\circ}B=0\qquad d^{\,\circ}C=0\qquad d^{\,\circ}D=1\qquad |  | (9a) |

 | d ∘ ​ A = 1 d ∘ ​ B = 0 d ∘ ​ C = 0 d ∘ ​ D = 1 \displaystyle d^{\,\circ}A=1\qquad d^{\,\circ}B=0\qquad d^{\,\circ}C=0\qquad d^{\,\circ}D=1\qquad |  | (9b) |

 | d ∘ ​ A = 1 d ∘ ​ B = 0 d ∘ ​ C = 1 d ∘ ​ D = 0 \displaystyle d^{\,\circ}A=1\qquad d^{\,\circ}B=0\qquad d^{\,\circ}C=1\qquad d^{\,\circ}D=0\qquad |  | (9c) |

 | d ∘ ​ A = 2 d ∘ ​ B = 1 d ∘ ​ C = 0 d ∘ ​ D = 0 \displaystyle d^{\,\circ}A=2\qquad d^{\,\circ}B=1\qquad d^{\,\circ}C=0\qquad d^{\,\circ}D=0\qquad |  | (9d) |

Proof Since d ∘ ​ B ⩽ d ∘ ​ A d^{\,\circ}B\leqslant d^{\,\circ}A then d ∘ ​ ( A + B) = d ∘ ​ A d^{\,\circ}(A+B)=d^{\,\circ}A. Hence, by C ​ E = A + B C\,E=A+B, we have d ∘ ​ C ⩽ d ∘ ​ A d^{\,\circ}C\leqslant d^{\,\circ}A

i) By ( 1) it follows

 | ( 4 ​ A ​ B ​ D − p) ​ C = A + B (4ABD-p)C=A+B |  | (10) |

and

 | ( 4 ​ B ​ C ​ D − 1) ​ A = B + C ​ p (4BCD-1)A=B+Cp |  | (11) |

By ( 10) we have d ∘ ​ ( 4 ​ A ​ B ​ D − p) ⩽ d ∘ ​ A d^{\,\circ}(4ABD-p)\leqslant d^{\,\circ}A and hence d ∘ ​ ( 4 ​ A ​ B ​ D − p) ⩽ d ∘ ​ A ​ B ​ D d^{\,\circ}(4ABD-p)\leqslant d^{\,\circ}ABD.

* Case d ∘ ​ ( 4 ​ A ​ B ​ D − p) = d ∘ ​ A ​ B ​ D d^{\,\circ}(4ABD-p)=d^{\,\circ}ABD
By ( 10) we have

 | d ∘ ​ A ​ B ​ D + d ∘ ​ C = d ∘ ​ A d^{\,\circ}ABD+d^{\,\circ}C=d^{\,\circ}A |  |

and then

 | d ∘ ​ B + d ∘ ​ C + d ∘ ​ D = 0 d^{\,\circ}B+d^{\,\circ}C+d^{\,\circ}D=0 |  |

This result implies, in view of ( 11), that

 | d ∘ ​ A = d ∘ ​ p = 1 d^{\,\circ}A=d^{\,\circ}p=1 |  |

* Case d ∘ ​ ( 4 ​ A ​ B ​ D − p) < d ∘ ​ A ​ B ​ D d^{\,\circ}(4ABD-p)<d^{\,\circ}ABD. In this case

 | d ∘ ​ A ​ B ​ D = d ∘ ​ p = 1 and d ∘ ​ ( 4 ​ A ​ B ​ D − p) = 0 d^{\,\circ}ABD=d^{\,\circ}p=1\mathrm{\quad and\quad}d^{\,\circ}(4ABD-p)=0 |  |

We have, by the first equation

 | d ∘ ​ B = 0 and d ∘ ​ A + d ∘ ​ D = 1 d^{\,\circ}B=0\mathrm{\quad and\quad}d^{\,\circ}A+d^{\,\circ}D=1 |  |

and by the second together with ( 10)

 | d ∘ ​ C = d ∘ ​ A d^{\,\circ}C=d^{\,\circ}A |  |

ii) By ( 2) it follows

 | ( 4 ​ A ​ B ​ D − 1) ​ C = p ⁡ ( A + B) (4ABD-1)C=p(A+B) |  | (12) |

and

 | ( 4 ​ B ​ C ​ D − p) ​ A = p ​ B + C (4BCD-p)A=pB+C |  | (13) |

By ( 12) we have

 | d ∘ ​ A ​ B ​ D + d ∘ ​ C = d ∘ ​ A + d ∘ ​ p d^{\,\circ}ABD+d^{\,\circ}C=d^{\,\circ}A+d^{\,\circ}p |  |

and then

 | d ∘ ​ B + d ∘ ​ C + d ∘ ​ D = 1 d^{\,\circ}B+d^{\,\circ}C+d^{\,\circ}D=1 |  |

Here F = 4 ​ B ​ C ​ D − p F=4BCD-p. Then

 | d ∘ ​ F ⩽ 1 and d ∘ ​ ( p ​ B + C) = d ∘ ​ p ​ B d^{\,\circ}F\leqslant 1\mathrm{\quad and\quad}d^{\,\circ}(pB+C)=d^{\,\circ}pB |  |

and together with ( 13)

 | d ∘ ​ F + d ∘ ​ A = d ∘ ​ B + 1 d^{\,\circ}F+d^{\,\circ}A=d^{\,\circ}B+1 |  |

* Case d ∘ ​ F = 1 d^{\,\circ}F=1. In this case d ∘ ​ A = d ∘ ​ B d^{\,\circ}A=d^{\,\circ}B. On the other hand, as d ∘ ​ F = 1 d^{\,\circ}F=1, there exists t 0 ∈ ℝ t_{0}\in\mathbb{R} such that F ⁡ ( t 0) = 0 F(t_{0})=0. From F ​ E = 4 ​ B 2 ​ D + 1 FE=4B^{2}D+1, it follows 4 ​ B 2 ​ ( t 0) ​ D ​ ( t 0) + 1 = 0 4B^{2}(t_{0})D(t_{0})+1=0 and then D ⁡ ( t 0) < 0 D(t_{0})<0. Therefore d ∘ ​ D = 1 d^{\,\circ}D=1 and d ∘ ​ B = d ∘ ​ C = 0 d^{\,\circ}B=d^{\,\circ}C=0.

* Case d ∘ ​ F = 0 d^{\,\circ}F=0. In this case d ∘ ​ A = d ∘ ​ B + 1 d^{\,\circ}A=d^{\,\circ}B+1. ■ \blacksquare

###### Proposition 3

Let p p be a prime polynomial of degree 1. The fraction 4 / p 4/p is 3-Egyptian if and only if one of the next 7 modular equations holds.

 |

 |  | B + p ​ C = 0 mod 4 ​ B ​ C ​ D − 1 \displaystyle B+pC=0\mod 4BCD-1 |  | (14a) |

 |  | p + E = 0 mod 4 ​ A ​ B and A + B = 0 mod E \displaystyle p+E=0\mod 4AB\mathrm{\quad and\quad}A+B=0\mod E\qquad |  | (14b) |

 |  | p + E + 4 ​ B 2 ​ D = 0 mod 4 ​ B ​ D ​ E \displaystyle p+E+4B^{2}D=0\mod 4BDE |  | (14c) |

 |

 |  | p ​ E + 1 = 0 mod 4 ​ A ​ B and A + B = 0 mod E \displaystyle pE+1=0\mod 4AB\mathrm{\quad and\quad}A+B=0\mod E |  | (15a) |

 |  | p + F = 0 mod 4 ​ B ​ C and p ​ B + C = 0 mod F \displaystyle p+F=0\mod 4BC\mathrm{\quad and\quad}pB+C=0\mod F |  | (15b) |

 |  | p + F = 0 mod 4 ​ B ​ D and 4 ​ B 2 ​ D + 1 = 0 mod F \displaystyle p+F=0\mod 4BD\mathrm{\quad and\quad}4B^{2}D+1=0\mod F |  | (15c) |

 |  | p + F = 0 mod 4 ​ C ​ D and p 2 + 4 ​ C 2 ​ D = 0 mod F \displaystyle p+F=0\mod 4CD\mathrm{\quad and\quad}p^{2}+4C^{2}D=0\mod F |  | (15d) |

where ( A, B) = ( B, C) = ( C, D) = ( 4 ​ A ​ B ​ D, E) = ( 4 ​ B ​ C ​ D, F) = 1 (A,B)=(B,C)=(C,D)=(4ABD,E)=(4BCD,F)=1.

Proof The [] [\>] refer to the equations of the Lemma.

- ( 14)

Here "( 4) is equivalent to ( 5)" is written

 | 4 A B C D = A + B + p C ⟺ ( p + E = 4 A B D and A + B = C E) 4ABCD=A+B+pC\Longleftrightarrow(p+E=4ABD\mathrm{\quad and\quad}A+B=CE) |  |

  - ( 14a)

Case [8a] : B, C, D B,C,D are constants. If we suppose that ( 4) holds, then

 | B + p ​ C = ( 4 ​ B ​ C ​ D − 1) ​ A = 0 mod ( 4 ​ B ​ C ​ D − 1) B+pC=(4BCD-1)A=0\mod(4BCD-1) |  |

Conversely, we set

 | A = B + p ​ C 4 ​ B ​ C ​ D − 1 A=\dfrac{B+pC}{4BCD-1} |  |

  - ( 14b)

Case [8b] : A, B, E A,B,E are constants. If we suppose that ( 4) holds, then

 | p + E = 4 ​ A ​ B ​ D = 0 mod 4 ​ A ​ B and A + B = C ​ E = 0 mod E p+E=4ABD=0\mod 4AB\mathrm{\quad and\quad}A+B=CE=0\mod E |  |

Conversely, we set

 | D = p + E 4 ​ A ​ B and C = A + B E D=\dfrac{p+E}{4AB}\mathrm{\quad and\quad}C=\dfrac{A+B}{E} |  |

  - ( 14c)

Case [8c] : B, D, E B,D,E are constants. If we suppose that ( 4) holds, then

 | p + E = 4 ​ ( C ​ E − B) ​ B ​ D p+E=4(CE-B)BD |  |

Hence

 | p + E + 4 ​ B 2 ​ D = 4 ​ B ​ D ​ E ​ C = 0 mod 4 ​ B ​ D ​ E p+E+4B^{2}D=4BDEC=0\mod 4BDE |  |

Conversely, we set

 | A = p + E 4 ​ B ​ D and C = p + E + 4 ​ B 2 ​ D 4 ​ B ​ D ​ E ( C ​ E = A + B) A=\dfrac{p+E}{4BD}\mathrm{\quad and\quad}C=\dfrac{p+E+4B^{2}D}{4BDE}\quad\left(CE=A+B\right) |  |

- ( 15)

Here "( 4) is equivalent to ( 5)" is written

 | 4 A B C D = p ( A + B) + C ⟺ ( 4 A B D = p E + 1 and A + B = C E) 4ABCD=p(A+B)+C\Longleftrightarrow(4ABD=pE+1\mathrm{\quad and\quad}A+B=CE) |  |

and "( 4) is equivalent to ( 6)" is written

 | 4 A B C D = p ( A + B) + C ⟺ ( p + F = 4 B C D and p B + C = F A) 4ABCD=p(A+B)+C\Longleftrightarrow(p+F=4BCD\mathrm{\quad and\quad}pB+C=FA) |  |

where F = 4 ​ B ​ C ​ D − p and F ​ E = 4 ​ B 2 ​ D + 1 F=4BCD-p\mathrm{\quad and\quad}FE=4B^{2}D+1

  - ( 15a)

Case [9a] : A, B, E A,B,E are constants. If we suppose that ( 4) holds, then

 | p ​ E + 1 = 4 ​ A ​ B ​ D = 0 mod 4 ​ A ​ B and A + B = C ​ E = 0 mod E pE+1=4ABD=0\mod 4AB\mathrm{\quad and\quad}A+B=CE=0\mod E |  |

Conversely, we set

 | D = p ​ E + 1 4 ​ A ​ B and C = A + B E D=\dfrac{pE+1}{4AB}\mathrm{\quad and\quad}C=\dfrac{A+B}{E} |  |

  - In

the next cases d ∘ ​ A = d ∘ ​ B + 1 d^{\,\circ}A=d^{\,\circ}B+1 and then d ∘ ​ F = 0 d^{\,\circ}F=0.

  - ( 15b)

Case [9b] : B, C, F B,C,F are constants. If we suppose that ( 4) holds, then

 | p + F = 4 ​ B ​ C ​ D = 0 mod 4 ​ B ​ C and p ​ B + C = F ​ A = 0 mod F p+F=4BCD=0\mod 4BC\mathrm{\quad and\quad}pB+C=FA=0\mod F |  |

Conversely, we set

 | D = p + F 4 ​ B ​ C and A = p ​ B + C F D=\dfrac{p+F}{4BC}\mathrm{\quad and\quad}A=\dfrac{pB+C}{F} |  |

  - ( 15c)

Case [9c] : B, D, F B,D,F are constants. If we suppose that ( 4) holds, then

 | p + F = 4 ​ B ​ C ​ D = 0 mod 4 ​ B ​ D and 4 ​ B 2 ​ D + 1 = E ​ F = 0 mod F p+F=4BCD=0\mod 4BD\mathrm{\quad and\quad}4B^{2}D+1=EF=0\mod F |  |

Conversely, we set

 | C = p + F 4 ​ B ​ D E = 4 ​ B 2 ​ D + 1 F and A = C ​ E − B C=\dfrac{p+F}{4BD}\quad E=\dfrac{4B^{2}D+1}{F}\mathrm{\quad and\quad}A=CE-B |  |

We observe that F ​ A = p ​ B + C FA=pB+C.

  - ( 15d)

Case [9d] : C, D, F C,D,F are constants. If we suppose that ( 4) holds, then

 | p + F = 4 ​ B ​ C ​ D = 0 mod 4 ​ C ​ D and p ​ B + C = F ​ A = 0 mod F p+F=4BCD=0\mod 4CD\mathrm{\quad and\quad}pB+C=FA=0\mod F |  |

As

 | p ​ B + C = p ​ p + F 4 ​ C ​ D + C = p 2 + p ​ F + 4 ​ C 2 ​ D 4 ​ C ​ D pB+C=p\dfrac{p+F}{4CD}+C=\dfrac{p^{2}+pF+4C^{2}D}{4CD} |  |

it follows, since ( 4 ​ C ​ D, F) = 1 (4CD,F)=1,

 | p 2 + 4 ​ C 2 ​ D = 0 mod F p^{2}+4C^{2}D=0\mod F |  |

Conversely, we set

 | B = p + F 4 ​ C ​ D and A = p ​ B + C F B=\dfrac{p+F}{4CD}\mathrm{\quad and\quad}A=\dfrac{pB+C}{F} |  |

■ \blacksquare

We observe that, if p p is a prime polynomial of degree 1, the Lemme 1 shows that there are only 7 distinct cases, according to the degree of A A, B B, C C, D D ( d ∘ ​ B ⩽ d ∘ ​ A d^{\,\circ}B\leqslant d^{\,\circ}A). By the Proposition 3, each case is connected to a modular equation. Hence, there exist only 7 distinct modular equations with constant coefficients. So, we can build an algorithm giving the set (maybe empty) of all the way to write 4 / p 4/p.

### 2.4 Application to the integers

The proof of the Proposition 3 gives us formulas for A, B, C, D A,B,C,D. These variables take strictly positive values when the given data are strictly positive and one of the equation ( 1) or ( 2) holds. Hence we have the following corollary.

###### Corollary 1

Let p p be an odd prime integer. The fraction 4 / p 4/p is 3-Egyptian if and only if one of the 7 modular equations of the Proposition 3 holds.

Thereafter, we call these equations reference equations not only for the polynomials but for the integers too.

#### Comparison with previous results

Four of these equations have been well known for a long time, but the others are new.

1. ∙ \bullet

Rosati [3] (1954) gives only one condition for ( 1) and one for ( 2). Although they are not written in a modular form, his equations (3) and (6) are equivalent to ( 14a) and ( 15a).

2. ∙ \bullet

Yamamoto [6] (1965) gives two conditions for ( 1) and two for ( 2). Written in a modular form, his equations (3) to (6) are equivalent (not in the same order) to ( 14a), ( 14b), ( 15a), ( 15b).

Polynomials explain why the Yamamoto equivalent equations give distinct results. Even better, they give us three new equations.

#### "Complete" set of modular equations

Regarding prime polynomials of degree 1, the 7 reference equations form a complete set 7 7 7 Moreover, example 2 below shows that these equations are independent., that is, if a modular equation n = b mod a n=b\mod a (where ( a, b) = 1 (a,b)=1) is not equivalent to one of the reference equations then 4 / ( a ​ t + b) 4/(at+b) cannot be an 3-Egyptian fraction. This feature does not hold for integers : it may exist a process using such an equation and leading to the conclusion that 4 / n 4/n is a 3-Egyptian fraction. But, in this case, this process has to be of a still unknown new type.

### 2.5 Examples

Example 0. Of course, we may find the identities of paragraph 1.1. Here, we don’t look after *all*the way to write 4 / p 4/p, just those given in the paragraph.

- •

p = 3 ​ t − 1 p=3t-1 verifies ( 14a) : p + 1 = 0 mod 3 p+1=0\mod 3
where B = C = D = 1 B=C=D=1, and hence A = ( p + 1) / 3 = t A=(p+1)/3=t.

- •

p = 4 ​ t − 1 p=4t-1 verifies ( 14b) : p + 1 = 0 mod 4 p+1=0\mod 4
where A = B = E = 1 A=B=E=1 and hence C = 2 C=2 et D = ( p + 1) / 4 = t D=(p+1)/4=t.

- •

p = 8 ​ t − 3 p=8t-3 verifies ( 14b) : p + 3 = 0 mod 8 p+3=0\mod 8
where A = 1 A=1, B = 2 B=2, E = 3 E=3 and hence C = 1 C=1, D = ( p + 3) / 8 = t D=(p+3)/8=t.

Example 1. p = 24 ⋅ 5 ​ t − 23 ( p = 1 mod 24, and, p = 2 mod 5) \quad p=24\cdot 5t-23\qquad(p=1\mod 24\mathrm{\quad and\quad}p=2\mod 5)
We give all the way to write 4 / p 4/p\, and the distinctive feature is that the 7 reference equations (shown in [] [\;]) are present. We don’t know another analogous example where p = 1 mod 24 p=1\mod 24.

1. [14a]

4 p = 1 p ​ ( 1 4 + 1 4 ​ ( 16 ​ t − 3)) + 1 2 ​ ( 16 ​ t − 3) \quad\dfrac{4}{p}=\dfrac{1}{p}\left(\dfrac{1}{4}+\dfrac{1}{4(16t-3)}\right)+\dfrac{1}{2(16t-3)}

2. [14b]

4 p = 1 p ​ ( 1 10 ​ ( 6 ​ t − 1) + 1 2 ​ ( 6 ​ t − 1)) + 1 5 ​ ( 6 ​ t − 1) \quad\dfrac{4}{p}=\dfrac{1}{p}\left(\dfrac{1}{10(6t-1)}+\dfrac{1}{2(6t-1)}\right)+\dfrac{1}{5(6t-1)}

3. [14c]

4 p = 1 p ​ ( 1 10 ​ t + 1 10 ​ t ​ ( 6 ​ t − 1)) + 1 5 ​ ( 6 ​ t − 1) \quad\dfrac{4}{p}=\dfrac{1}{p}\left(\dfrac{1}{10t}+\dfrac{1}{10t(6t-1)}\right)+\dfrac{1}{5(6t-1)}

4 p = 1 p ​ ( 1 2 ​ t + 1 2 ​ t ​ ( 15 ​ t − 1)) + 1 2 ​ ( 15 ​ t − 1) \quad\dfrac{4}{p}=\dfrac{1}{p}\left(\dfrac{1}{2t}+\dfrac{1}{2t(15t-1)}\right)+\dfrac{1}{2(15t-1)}

4. [15a]

4 p = 1 5 ​ ( 21 ​ t − 4) + 1 2 ​ ( 21 ​ t − 4) + 1 10 ​ ( 21 ​ t − 4) ​ p \quad\dfrac{4}{p}=\dfrac{1}{5(21t-4)}+\dfrac{1}{2(21t-4)}+\dfrac{1}{10(21t-4)\,p}

5. [15b]

4 p = 1 5 ​ ( 6 ​ t − 1) + 1 2 ​ ( 6 ​ t − 1) ​ ( 100 ​ t − 19) + 1 10 ​ ( 6 ​ t − 1) ​ ( 100 ​ t − 19) ​ p \quad\dfrac{4}{p}=\dfrac{1}{5(6t-1)}+\dfrac{1}{2(6t-1)(100t-19)}+\dfrac{1}{10(6t-1)(100t-19)\,p}

4 p = 1 5 ​ ( 6 ​ t − 1) + 1 10 ​ ( 6 ​ t − 1) ​ ( 20 ​ t − 3) + 1 2 ​ ( 6 ​ t − 1) ​ ( 20 ​ t − 3) ​ p \quad\dfrac{4}{p}=\dfrac{1}{5(6t-1)}+\dfrac{1}{10(6t-1)(20t-3)}+\dfrac{1}{2(6t-1)(20t-3)\,p}

4 p = 1 OPEN 2 ​ ( 15 ​ t − 1)) + 1 ( 15 ​ t − 1) ​ ( 16 ​ t − 3) + 1 2 ​ ( 15 ​ t − 1) ​ ( 16 ​ t − 3) ​ p \quad\dfrac{4}{p}=\dfrac{1}{2(15t-1))}+\dfrac{1}{(15t-1)(16t-3)}+\dfrac{1}{2(15t-1)(16t-3)\,p}

6. [15c]

4 p = 1 5 ​ ( 6 ​ t − 1) + 1 10 ​ ( 6 ​ t − 1) ​ ( 21 ​ t − 4) + 1 10 ​ ( 21 ​ t − 4) ​ p \quad\dfrac{4}{p}=\dfrac{1}{5(6t-1)}+\dfrac{1}{10(6t-1)(21t-4)}+\dfrac{1}{10(21t-4)\,p}

7. [15d]

4 p = 1 5 ​ ( 6 ​ t − 1) + 1 10 ​ ( 120 ​ t 2 − 43 ​ t + 4) + 1 10 ​ ( 6 ​ t − 1) ​ ( 120 ​ t 2 − 43 ​ t + 4) ​ p \quad\dfrac{4}{p}=\dfrac{1}{5(6t-1)}+\dfrac{1}{10(120t^{2}-43t+4)}+\dfrac{1}{10(6t-1)(120t^{2}-43t+4)\,p}

Example 2. In this example, each p p\, is of the form p = 24 ⋅ 583 ​ t + b p=24\cdot 583t+b. At the opposite of the example 1, the distinctive feature is that, for some b b, there is only one way to write 4 / p 4/p. A value of b b is given for each reference equation.

1. [14a]

p = 24 ⋅ 583 ​ t − 911 ( p = 1 mod 24, and, p = 255 mod 583) \quad p=24\cdot 583t-911\quad(p=1\mod 24\mathrm{\quad and\quad}p=255\mod 583)

4 p = 1 p ​ ( 1 2 ⋅ 73 + 1 6 ​ ( 16 ​ t − 1)) + 1 3 ⋅ 73 ​ ( 16 ​ t − 1) \quad\dfrac{4}{p}=\dfrac{1}{p}\left(\dfrac{1}{2\cdot 73}+\dfrac{1}{6(16t-1)}\right)+\dfrac{1}{3\cdot 73(16t-1)}

2. [14b]

p = 24 ⋅ 583 ​ t − 119 ( p = 1 mod 24, and, p = 464 mod 583) \quad p=24\cdot 583t-119\quad(p=1\mod 24\mathrm{\quad and\quad}p=464\mod 583)

4 p = 1 p ​ ( 1 66 ​ t + 1 53 ​ t) + 1 66 ⋅ 53 ​ t \quad\dfrac{4}{p}=\dfrac{1}{p}\left(\dfrac{1}{66t}+\dfrac{1}{53t}\right)+\dfrac{1}{66\cdot 53t}

3. [14c]

p = 24 ⋅ 583 ​ t − 1127 ( p = 1 mod 24, and, p = 39 mod 583) \quad p=24\cdot 583t-1127\quad(p=1\mod 24\mathrm{\quad and\quad}p=39\mod 583)

4 p = 1 p ​ ( 1 22 ​ t + 1 2 ​ t ​ ( 159 ​ t − 11)) + 1 22 ​ ( 159 ​ t − 11) \quad\dfrac{4}{p}=\dfrac{1}{p}\left(\dfrac{1}{22t}+\dfrac{1}{2t(159t-11)}\right)+\dfrac{1}{22(159t-11)}

4. [15a]

p = 24 ⋅ 583 ​ t − 1799 ( p = 1 mod 24, and, p = 533 mod 583) \quad p=24\cdot 583t-1799\quad(p=1\mod 24\mathrm{\quad and\quad}p=533\mod 583)

4 p = 1 50 ⋅ 1749 ​ ( 70 ​ t − 9) + 1 50 ​ ( 70 ​ t − 9) + 1 1749 ​ ( 70 ​ t − 9) ​ p \quad\dfrac{4}{p}=\dfrac{1}{50\cdot 1749(70t-9)}+\dfrac{1}{50(70t-9)}+\dfrac{1}{1749(70t-9)\,p}

5. [15b]

p = 24 ⋅ 583 ​ t − 11159 ( p = 1 mod 24, and, p = 501 mod 583) \quad p=24\cdot 583t-11159\quad(p=1\mod 24\mathrm{\quad and\quad}p=501\mod 583)

 | 4 p = 1 22 ​ ( 159 ​ t − 125) + 1 8 ​ ( 242 ​ t − 193) ​ ( 159 ​ t − 125) + 1 88 ​ ( 242 ​ t − 193) ​ ( 159 ​ t − 125) ​ p \dfrac{4}{p}=\dfrac{1}{22(159t-125)}+\dfrac{1}{8(242t-193)(159t-125)}\\ +\dfrac{1}{88(242t-193)(159t-125)\,p} |  |

6. [15c]

p = 24 ⋅ 583 ​ t − 503 ( p = 1 mod 24, and, p = 80 mod 583) \quad p=24\cdot 583t-503\quad(p=1\mod 24\mathrm{\quad and\quad}p=80\mod 583)

4 p = 1 6 ⋅ 583 ​ t + 1 6 ⋅ 53 ​ t ​ ( 306 ​ t − 11) + 1 583 ​ ( 306 ​ t − 11) ​ p \quad\dfrac{4}{p}=\dfrac{1}{6\cdot 583t}+\dfrac{1}{6\cdot 53t(306t-11)}+\dfrac{1}{583(306t-11)\,p}

7. [15d]

p = 24 ⋅ 583 ​ t − 6407 ( p = 1 mod 24, and, p = 6 mod 583) \quad p=24\cdot 583t-6407\quad(p=1\mod 24\mathrm{\quad and\quad}p=6\mod 583)

 | 4 p = 1 22 ​ ( 159 ​ t − 71) + 1 22 ​ ( 13992 ​ t 2 − 12655 ​ t + 2861) + 1 11 ​ ( 159 ​ t − 71) ​ ( 13992 ​ t 2 − 12655 ​ t + 2861) ​ p \dfrac{4}{p}=\dfrac{1}{22(159t-71)}+\dfrac{1}{22(13992t^{2}-12655t+2861)}\\ +\dfrac{1}{11(159t-71)(13992t^{2}-12655t+2861)\,p} |  |

## 3 Modular sieve

The algorithms setting, for a given integer n > 2 n>2, at least one way (and even more) to write 4 / n 4/n are interesting. However, regarding the checking of the conjecture, an efficient algorithm needs an another point of view 8 8 8 This point of view has been used since Rosati’s paper (or maybe before)..

We denote by ℕ 0 \mathbb{N}_{0} the set of the integers n ∈ ℕ n\in\mathbb{N} verifying the condition n = 1 mod 24 n=1\mod 24. The process described below takes account specifically of the fact that the checked integers are in ℕ 0 \mathbb{N}_{0}. On the other hand, we let down the condition that n n is prime, which needs too much running time. Regarding the polynomial a ​ t + b at+b, the correlated conditions are a ​ t + b = 1 mod 24 at+b=1\mod 24 (which is equivalent to a = 0 mod 24 a=0\mod 24 and b = 1 mod 24 b=1\mod 24) and the cancellation of the condition ( a, b) = 1 (a,b)=1.

### 3.1 Modular filters

Definition : A sieve is a sorted set of filters.

Definition : A filter 9 9 9 We use the terminology given by Swett. If an integer n ∈ ℕ 0 n\in\mathbb{N}_{0} is such that n % ​ m ∈ F n\%m\in F then n n verifies the conjecture and n n is ”trapped” by the filter. Otherwise n n ”pass through”. modulo m m is a set F F such that for any n ∈ ℕ 0 n\in\mathbb{N}_{0}

 | n % ​ m ∈ F ⇒ 4 / n ​ is 3-Egyptian n\%m\in F\Rightarrow 4/n\;\textnormal{is 3-Egyptian} |  |

where n % ​ m n\%m is the residue of n n modulo m m (notation borrowed from C language).

For a > 0 a>0, we denote by Ω a \Omega_{a} the set of b ∈ ℤ b\in\mathbb{Z} such that 4 / ( a ​ t + b) 4/(at+b) is a 3-Egyptian fraction. If m m is odd, we set S m = ( Ω [m, 24] ∩ ℕ 0) % ​ m S_{m}=\left(\Omega_{[m,24]}\cap\mathbb{N}_{0}\right)\%m where [u, v] = LCM ( u, v) [u,v]=\mathop{\rm LCM}(u,v). It follows some obvious proprieties.

1. i)

if q | a q\mid a then Ω q ⊂ Ω a \Omega_{q}\subset\Omega_{a}.

2. ii)

if b 1 = b 2 mod a b_{1}=b_{2}\mod a then b 1 ∈ Ω a ⇒ b 2 ∈ Ω a b_{1}\in\Omega_{a}\Rightarrow b_{2}\in\Omega_{a}.

3. iii)

if n ∈ Ω a n\in\Omega_{a} ( n > 0 n>0) then 4 / n 4/n is a 3-Egyptian fraction.

4. iv)

if n ∈ ℕ 0 n\in\mathbb{N}_{0} then ( n ∈ Ω [m, 24] ⟺ n % m ∈ S m) \left(n\in\Omega_{[m,24]}\Longleftrightarrow n\%m\in S_{m}\right), which shows that S m S_{m} is a filter modulo m m.

5. v)

if n ∈ ℕ 0 n\in\mathbb{N}_{0} and if q | m q\mid m then n % ​ q ∈ S q ⇒ n % ​ m ∈ S m n\%q\in S_{q}\Rightarrow n\%m\in S_{m}.

Définition : We say that n ∈ ℕ 0 n\in\mathbb{N}_{0} is *certified*if there exists m m such that n % ​ m ∈ S m n\%m\in S_{m}. We also say that n n is certified by m m or that m m is a *modular certificate*of n n (vocabulary borrowed from the complexity theory).

The first results with prime integers:

1.

S 5 = { 0, 2, 3 } S_{5}=\{0,2,3\}

2.

S 7 = { 0, 3, 5, 6 } S_{7}=\{0,3,5,6\}

3.

S 11 = { 0, 7, 8, 10 } S_{11}=\{0,7,8,10\}

4.

S 13 = { 0, 5, 6, 8, 11 } S_{13}=\{0,5,6,8,11\}

5.

S 17 = { 0, 10, 11, 12, 14 } S_{17}=\{0,10,11,12,14\}

6.

S 19 = { 0, 8, 12, 14, 15, 18 } S_{19}=\{0,8,12,14,15,18\}

7.

S 23 = { 0, 7, 10, 11, 15, 17, 19, 20, 21, 22 } S_{23}=\{0,7,10,11,15,17,19,20,21,22\}

8.

S 29 = { 0, 14, 18, 19, 21, 26, 27 } S_{29}=\{0,14,18,19,21,26,27\}

9.

S 31 = { 0, 15, 22, 23, 24, 27, 29, 30 } S_{31}=\{0,15,22,23,24,27,29,30\}

10.

S 37 = { 0, 5, 15, 18, 22, 23, 29, 32, 35 } S_{37}=\{0,5,15,18,22,23,29,32,35\}

Some results with odd composite integers:

1.

S 15 = { 7, 10, 13 } S_{15}=\{7,10,13\}

2.

S 35 = { 0, 2, 3, 5, 6, 7, 8, 10, 12, 13, 14, 15, 17, 18, 19, 20, 21, 22, 23, 24 S_{35}=\{0,2,3,5,6,7,8,10,12,13,14,15,17,18,19,20,21,22,23,24
m, 25, 26, 27, 28, 30, 31, 32, 33, 34 },25,26,27,28,30,31,32,33,34\}

3.

S 55 = { 0, 2, 3, 5, 7, 8, 10, 11, 12, 13, 15, 17, 18, 19, 20, 21, 22, 23 S_{55}=\{0,2,3,5,7,8,10,11,12,13,15,17,18,19,20,21,22,23
m, 24, 25, 27, 28, 29, 30, 32, 33, 35, 37, 38, 39, 40, 41, 42, 43,24,25,27,28,29,30,32,33,35,37,38,39,40,41,42,43
m, 44, 45, 47, 48, 50, 51, 52, 53, 54 },44,45,47,48,50,51,52,53,54\}

### 3.2 Shortened filters

If m m is composite, some integers n ∈ ℕ 0 n\in\mathbb{N}_{0} are certified both par m m and by one of its divisors (cf. the propriety v) above). The next definition allows us to point out what is particular to m m.

Definition: The shortened filter S m ∗ S^{*}_{m} is the set of all x ∈ S m x\in S_{m} such that

x % ​ q ∉ S q x\%q\notin S_{q} for any q | m q\mid m, q ≠ m q\neq m

We observe that if m m is prime then S m ∗ = S m S^{*}_{m}=S_{m}.

The first (no empty) results

1.

S 55 ∗ = { 24, 39 } S^{*}_{55}=\{24,39\}

2.

S 65 ∗ = { 54, 59 } S^{*}_{65}=\{54,59\}

3.

S 77 ∗ = { 46, 72 } S^{*}_{77}=\{46,72\}

4.

S 85 ∗ = { 54, 74 } S^{*}_{85}=\{54,74\}

5.

S 95 ∗ = { 29, 59, 79, 89 } S^{*}_{95}=\{29,59,79,89\}

6.

S 99 ∗ = { 61, 79, 94 } S^{*}_{99}=\{61,79,94\}

7.

S 117 ∗ = { 85,106 } S^{*}_{117}=\{85,106\}

8.

S 119 ∗ = { 23, 39, 57, 58, 71, 88, 107, 109 } S^{*}_{119}=\{23,39,57,58,71,88,107,109\}

## 4 Checking of the conjecture

### 4.1 Choice of the progressions

The checked integers n n are in an arithmetic progression, namely they are of the form n = 24 ​ k + 1 n=24k+1. We call gap of the progression the difference between two consecutive terms. Here the gap is G 0 = 24 G_{0}=24 but if we use some filters S m S_{m} we may obtain other progressions whose gap is bigger.

With S 5 = { 0, 2, 3 } S_{5}=\{0,2,3\} we check only n n such that

 | n % ​ 24 = 1 and n % ​ 5 ∈ { 1, 4 } n\%24=1\mathrm{\quad and\quad}n\%5\in\{1,4\} |  |

and hence, by the Chinese remainder theorem

 | n % ​ 120 ∈ { 1, 49 } n\%120\in\{1,49\} |  |

The new gap is G 1 = 120 G_{1}=120, and there are 2 residues : then the mean gap is g 1 = 60 g_{1}=60. In comparison to 24, we check 2.5 2.5 times fewer integers ( 60 / 24 = 2.5 60/24=2.5).

Next, with S 7 = { 0, 3, 5, 6 } S_{7}=\{0,3,5,6\} we check only n n such that

 | n % ​ 120 ∈ { 1, 49 } and n % ​ 7 ∈ { 1, 2, 4 } n\%120\in\{1,49\}\mathrm{\quad and\quad}n\%7\in\{1,2,4\} |  |

and hence

 | n % ​ 840 ∈ R 2 n\%840\in R_{2} |  |

where R 2 = { 1,121,169,289,361, 529 } R_{2}=\{1,121,169,289,361,529\} is the set of the residues 10 10 10 It was the choice made by Swett.. The new gap is G 2 = 840 G_{2}=840 and the mean gap is g 2 = 140 g_{2}=140. In comparison to 24, we check nearly 6 times fewer integers ( 140 / 24 = 35 / 6 140/24=35/6).

We may keep on and use others S m S_{m}. The checked integers are then of the form

 | n % ​ G i ∈ R i n\%G_{i}\in R_{i} |  |

where the first values of G i = G i − 1 ​ m i G_{i}=G_{i-1}m_{i} and #​ R i \#R_{i} (the number of elements of R i R_{i}) are set out in the following table.

 | i m i G i #​ R i g i 1 5 120 2 60 2 7 840 6 140 3 11 9 240 34 272 4 13 120 120 192 626 5 17 2 042 040 1 507 1 355 6 19 38 798 760 13 380 2 900 7 23 892 371 480 147 348 6 056 \begin{array}[]{|c|c|c|c|c|}\hline\cr\vphantom{\Big(}i&m_{i}&G_{i}&\#R_{i}&g_{i}\\ \hline\cr\vphantom{\Big(}1&5&120&2&60\\ \hline\cr\vphantom{\Big(}2&7&840&6&140\\ \hline\cr\vphantom{\Big(}3&11&9\,240&34&272\\ \hline\cr\vphantom{\Big(}4&13&120\,120&192&626\\ \hline\cr\vphantom{\Big(}5&17&2\,042\,040&1\,507&1\,355\\ \hline\cr\vphantom{\Big(}6&19&38\,798\,760&13\,380&2\,900\\ \hline\cr\vphantom{\Big(}7&23&892\,371\,480&147\,348&6\,056\\ \hline\cr\end{array} |  |

Three comments about this table.

- •

The first concerns the reduction of R i R_{i} (done in the table). If n = r mod G i n=r\mod G_{i} then for any q q divisor of G i G_{i} we have n % ​ q = r % ​ q n\%q=r\%q. Hence, we may remove the residues r ∈ R i r\in R_{i} verifying r % ​ q ∈ S q r\%q\in S_{q}. This reduction is essential, otherwise it’s just a useless complicated process.

- •

The second concerns the last column : the mean gap g i = G i / #​ R i g_{i}=G_{i}/\#R_{i} is a good speed indicator. By example, as 6 056 / 140 ≈ 43 6\,056/140\approx 43, then using G 7 G_{7} rather than G 2 G_{2} leads to check about 43 43 times fewer integers and the running time is shortened accordingly.

- •

The last concerns the choice of the m i m_{i}. The usual order is misleading : each other set of seven integers seems to give a worse g 7 g_{7}. Next, with height integers we expect to add 31 31 (rather than 29 29). However, these two propositions have to be confirmed.

### 4.2 Optimized sieve

We denote by ℕ i \mathbb{N}_{i} the set of all the integers n ∈ ℕ n\in\mathbb{N} verifying n % ​ G i ∈ R i n\%G_{i}\in R_{i}. As the conjecture is verified for any integer n ∉ N i n\notin N_{i}, we have just to check the prime integers of N i N_{i}.

Let N = 10 17 N=10^{17} and M M the set of all the odd integers m < 5 000 m<5\,000. We claim that each n ∈ ℕ 7 n\in\mathbb{N}_{7} has a modular certificate in M M if n < N n<N and if n n is not a square. It is equivalent to say that ℕ 7 ∖ ⋃ m ∈ M Ω [m, 24] \mathbb{N}_{7}\setminus\bigcup_{m\in M}\Omega_{[m,24]} has not any element n < N n<N, except squares.

We could use this M M to prove that the conjecture is verified up to N N. However, if we want a running time as fewer as possible, we have to optimize the sieve. For this purpose, we remove the useless elements and sort M M in order to have at first the most efficient filters 11 11 11 The approach mostly hinge on experiments and make use of the shortened filters.. By example for N = 10 17 N=10^{17}, we give below the set M = M ​ O ​ D M=MOD which is used in our C++ program.

M O D = { MOD=\{ 3, 5, 7, 11, 13, 17, 19, 23, 4495, 2491, 2627, 4661, 4223, 1505, 4355, 3355, 4509, 4775, 2629, 4565, 4599, 4585, 3955, 3535, 3857, 3115, 3419, 3949, 3395, 3353, 1391, 1199, 3775, 4325, 4031, 2799, 1639, 4475, 2159, 4795, 2961, 1727, 4075, 1791, 4743, 2849, 3595, 1115, 3445, 3263, 2155, 2065, 2515, 2681, 4195, 3223, 2519, 4103, 3731, 4345, 3743, 2439, 1055, 2951, 1799, 4193, 1991, 3047, 2933, 3951, 4147, 1631, 2219, 4615, 3913, 3679, 1535, 2959, 1655, 4123, 1439, 3839, 1319, 3695, 4255, 3895, 1351, 2495, 1835, 2855, 2335, 4529, 1917, 1079, 1559, 1735, 1679, 2165, 4367, 4555, 2359, 2723, 3065, 3899, 3295, 3035, 4927, 3359, 4437, 3635, 4315, 2735, 3241, 4319, 4105, 4069, 1039, 4059, 1247, 3095, 4571, 3665, 1007, 1583, 4895, 1847, 2435, 1765, 2807, 3647, 1343, 2651, 3965, 1511, 2655, 4403, 1151, 887, 2935, 3545, 2879, 1967, 2815, 2399, 4419, 1159, 4487, 3119, 1223, 2039, 4745, 2305, 1103, 4077, 3215, 3715, 2279, 4915, 4873, 1031, 1475, 3865, 2483, 1399, 1823, 3173, 3305, 2241, 3985, 3563, 1349, 1259, 3959, 4415, 3455, 2615, 1487, 3599, 3935, 1759, 3505, 1871, 4879, 4535, 3199, 2045, 1367, 1493, 1919, 3787, 2111, 1975, 2053, 4739, 1231, 4151, 1837, 1213, 3655, 2183, 4135, 4939, 1019, 3023, 3995, 1855, 4265, 4079, 3983, 2575, 1063, 2351, 4985, 2687, 3167, 2447, 2725, 4631, 4595, 4115, 4175, 4055, 4679, 1013, 2239, 4385, 1091, 3429, 1909, 1719, 2365, 3415, 3079, 4955, 1147, 1133, 3191, 3475, 2759, 4405, 2207, 4765, 3431, 1139, 4471, 2727, 4145, 3247, 1279, 1751, 3755, 1087, 4835, 1733, 4645, 1979, 4711, 1177, 1073, 3055, 3239, 2999, 2087, 4855, 4039, 1703, 3527, 4295, 4799, 4207, 4505, 1187, 1109, 1567, 1379, 2119, 2911, 2591, 2015, 3785, 1651, 3155, 1819, 4751, 3719, 4735, 2345, 2831, 2099, 4995, 1427, 2059, 1333, 1069, 1663, 2719, 2063, 4285, 2231, 1093, 1607, 1423, 1411, 1027, 3805, 1769, 1121, 1903, 4063, 4759, 1363, 1973, 4715, 2663, 3863, 1433, 2479, 4703, 3299, 1451, 2339, 1613, 1471, 1619, 3671, 2287, 2367, 3845, 3537, 1591, 3733, 4463, 1271, 1931, 4619, 2903, 2135, 4921, 4685, 4705, 1003, 1429, 1193, 4067, 3275, 4311, 1327, 3015, 1499, 2413, 1237, 1181, 4045, 4081, 3605, 3779, 3103, 2837, 1579, 3439, 1033, 3799, 2333, 1829, 1241, 4393, 2357, 4159, 2699, 3791, 2453, 3625, 2579, 4945, 4127, 1649, 4741, 4871, 1667, 2177, 3835, 1043, 3407, 4919, 4885, 2267, 2693, 2507, 4967, 2327, 4639, 1691, 1549, 2583, 1123, 1717, 1999, 1807, 1933, 4553, 1049, 3479, 1553, 1853, 2543, 4343, 1501, 2743, 3699, 1787, 3989, 1129, 1525, 4445, 1675, 1993, 1301, 2273, 1217, 1843, 4003, 2411, 3245, 3401, 1117, 1789, 3379, 3901, 1831, 1957, 4085, 1507, 1987, 3373, 3893, 1621, 1943, 3937, 1291, 1543, 1571, 2143, 2533, 2767, 3253, 4883, 2551, 2833, 1229, 1877, 1949, 2009, 4391, 1643, 2251, 2729, 3915, 1907, 2243, 2603, 2669, 2897, 3043, 3313, 3739, 1171, 1361, 1817, 1879, 2659, 3623, 4283, 4859, 1537, 2003, 2161, 2389, 2869, 4439, 1099, 1415, 2269, 2293, 2943, 3233, 3967, 4181, 4261, 4559, 4699, 1447, 1895, 1921, 2195, 2939, 3293, 3565, 3607, 3749, 4247, 4591, 4829, 1157, 1417, 1951, 1997, 2179, 2225, 2619, 2785, 3041, 3717, 4583, 4783, 4887, 1283, 1517, 1721, 1747, 1961, 2033, 2117, 2129, 2741, 2803, 2893, 3161, 3589, 3613, 1211, 1273, 1459, 1483, 1811, 1867, 1889, 1971, 2043, 2069, 2149, 2213, 2423, 2709, 2779, 3013, 3149, 3551, 4013, 4097, 4363, 4399, 4589, 4681, 1021, 1097, 1145, 1197, 1297, 1373, 1397, 1555, 1609, 1723, 1773, 1777, 1783, 1801, 2123, 2191, 2259, 2291, 2371, 2407, 2443, 2671, 2845, 3389, 3493, 3725, 4021, 4171, 4351, 4999 } \}

### 4.3 Results

The checked integers are of the form n = r + k × G 7 n=r+k\times G_{7} where r ∈ R 7 r\in R_{7} and 0 ⩽ k < K 0\leqslant k<K. With N = 10 17 N=10^{17}, we take K = 112 066 560 K=112\,066\,560. Therefore we check 16 512 783 482 880 16\,512\,783\,482\,880 integers including 51 732 427 51\,732\,427 squares.

For each m ∈ M ​ O ​ D m\in MOD, the number of integers certified by m m is given at the same rank in the table below. We may observe that the sum of these numbers added with the number of squares is equal to the number of checked integers.

{ \{ 0, 0, 0, 0, 0, 0, 0, 9223757362766, 3739609092281, 1565954748220, 739166512371, 397180210351, 249398230928, 169050837573, 104088377604, 69101085771, 54368854713, 42523071218, 33206924179, 23406992663, 18890746142, 15211918708, 11968966501, 9473482721, 7560449664, 6273004978, 5196086887, 4344239727, 3485872879, 2944121141, 2498890993, 2067185415, 1765012627, 1499112458, 1259328652, 1044404123, 874512654, 723079141, 617340453, 515245196, 452563855, 390773540, 343076561, 300065591, 260653549, 229207022, 198772233, 174906642, 153551008, 135203129, 118673167, 99017032, 88208940, 78571579, 69928806, 62430095, 55603526, 48999877, 42755472, 38618483, 34775913, 31335757, 27560576, 24702471, 22410294, 19685100, 17852098, 16081935, 14466854, 13141729, 11726132, 10640116, 9491430, 8477371, 7732328, 6982821, 6272905, 5702788, 5268793, 4722801, 4390120, 4019516, 3650026, 3398755, 3140726, 2945648, 2736821, 2552135, 2394011, 2241501, 2100950, 1967613, 1834764, 1721795, 1606462, 1497392, 1396075, 1313066, 1211933, 1135277, 1058550, 992002, 932632, 867721, 807226, 759519, 707804, 665956, 625412, 586324, 552400, 520156, 484882, 459951, 434799, 408981, 385709, 365271, 343865, 322175, 305617, 290089, 275265, 260444, 247858, 235278, 223480, 212702, 201616, 190609, 179783, 171406, 163172, 153416, 146567, 138229, 131604, 125502, 118787, 113170, 106706, 101331, 96415, 91243, 87184, 83366, 79429, 75744, 72027, 68424, 65511, 62568, 59796, 57362, 54579, 52058, 49809, 47397, 45319, 43371, 41545, 39868, 38029, 36324, 34724, 33179, 31866, 30561, 29163, 27958, 26789, 25721, 24727, 23684, 22631, 21616, 20727, 19908, 19064, 18235, 17562, 16604, 15933, 15087, 14379, 13832, 13303, 12763, 12305, 11871, 11311, 10807, 10411, 9972, 9650, 9215, 8834, 8518, 8200, 7898, 7612, 7318, 7021, 6760, 6493, 6232, 5968, 5727, 5528, 5308, 5119, 4884, 4693, 4538, 4369, 4224, 4063, 3940, 3786, 3653, 3530, 3414, 3246, 3117, 3013, 2912, 2787, 2685, 2559, 2455, 2384, 2269, 2185, 2103, 2048, 1985, 1908, 1831, 1777, 1725, 1671, 1621, 1563, 1517, 1465, 1423, 1375, 1335, 1285, 1245, 1196, 1156, 1122, 1076, 1048, 1012, 977, 943, 920, 892, 860, 834, 803, 783, 761, 743, 718, 701, 679, 654, 637, 602, 586, 571, 559, 539, 521, 510, 488, 473, 461, 445, 435, 426, 414, 402, 383, 374, 362, 352, 346, 335, 324, 317, 313, 303, 295, 284, 277, 270, 261, 252, 245, 242, 232, 226, 223, 217, 213, 205, 200, 197, 191, 187, 180, 177, 174, 169, 166, 162, 157, 153, 151, 147, 142, 138, 135, 133, 131, 129, 127, 124, 119, 115, 114, 111, 110, 105, 102, 100, 98, 95, 94, 92, 90, 86, 85, 83, 82, 79, 78, 78, 76, 75, 72, 70, 69, 67, 65, 64, 61, 60, 58, 57, 57, 55, 55, 54, 52, 51, 49, 48, 47, 46, 44, 44, 43, 42, 42, 41, 40, 39, 39, 38, 37, 37, 35, 35, 34, 34, 33, 32, 32, 30, 30, 30, 29, 29, 29, 27, 27, 26, 25, 25, 25, 24, 24, 24, 23, 23, 22, 22, 22, 21, 21, 20, 20, 19, 19, 19, 18, 18, 18, 17, 17, 17, 17, 16, 16, 16, 15, 15, 15, 15, 14, 14, 14, 13, 13, 13, 13, 13, 13, 13, 13, 12, 12, 11, 11, 11, 11, 11, 10, 10, 10, 10, 9, 9, 9, 9, 9, 9, 9, 9, 8, 8, 8, 8, 8, 8, 8, 8, 7, 7, 7, 7, 7, 7, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 } \}

## References

- [1] Bernstein Von Leon (1962), Zur Lösung der diophantischen Gleichung m / n = 1 / x + 1 / y + 1 / z m/n=1/x+1/y+1/z, insbesondere im Fall m = 4 m=4, Journal für die reine und angewandte Mathematik, volume 211, p. 1-10. `http://gdz.sub.uni-goettingen.de/dms/load/img/?PPN=GDZPPN002179792`
- [2] Mordell Louis Joel(1967), Diophantine Equations, Academic Press, p. 287-290.
- [3] Rosati Luigi Antonio (1954), Sull’equazione diofantea 4 / n = 1 / x 1 + 1 / x 2 + 1 / x 3 4/n=1/x_{1}+1/x_{2}+1/x_{3}, Bollettino dell’Unone Matematica Italiana, serie 3, volume 9 n.1 p. 59-63. `http://www.bdim.eu/item?fmt=pdf&id=BUMI_1954_3_9_1_59_0`
- [4] Schinzel Andrzej (2000), On sums of three unit fractions with polynomial denominators, Functiones et Approximatio Commentarii Mathematici vol.XXVIII p.187-194. `http://www.staff.amu.edu.pl/˜fa/XXVIII/fa-28-1-187.pdf`
- [5] Swett Allan (1999), The Erdős-Straus conjecture, Current Research on ESC, rev.10/28/99. `http://math.uindy.edu/swett/esc.htm`
- [6] Yamamoto Koichi (1965), On the diophantine equation 4 / n = 1 / x + 1 / y + 1 / z 4/n=1/x+1/y+1/z, Memoirs of the Faculty of Science, Kyushu University, Series A, Mathematics, Vol. 19, p. 37-47. `https://www.jstage.jst.go.jp/article/kyushumfs/19/1/19_1_37/_pdf`


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
