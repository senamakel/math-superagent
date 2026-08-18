<!-- source: https://ar5iv.labs.arxiv.org/html/1603.04211 | converted from HTML -->

[1603.04211] 1Introduction

\CJKindent

The number of distinct and repeated squares

and cubes in the Fibonacci sequence

Huang Yuke 1 1 1 School of Mathematics and Systems Science, Beihang University (BUAA), Beijing, 100191, P. R. China. E-mail address: huangyuke07@tsinghua.org.cn, hyg03ster@163.com. Wen Zhiying 2 2 2 Department of Mathematical Sciences, Tsinghua University, Beijing, 100084, P. R. China. E-mail address: wenzy@tsinghua.edu.cn(Corresponding author).

ABSTRACT

The Fibonacci sequence 𝔽 \mathbb{F} is the fixed point beginning with a a of morphism σ ⁡ ( a, b) = ( a ​ b, a) \sigma(a,b)=(ab,a). In this paper, we get the explicit expressions of all squares and cubes, then we determine the number of distinct squares and cubes in 𝔽 ⁡ [1, n] \mathbb{F}[1,n] for all n n, where 𝔽 ⁡ [1, n] \mathbb{F}[1,n] is the prefix of 𝔽 \mathbb{F} of length n n. By establishing and discussing the recursive structure of squares and cubes, we give algorithms for counting the number of repeated squares and cubes in 𝔽 ⁡ [1, n] \mathbb{F}[1,n] for all n n, and get explicit expressions for some special n n such as n = f m n=f_{m} (the Fibonacci number) etc., which including some known results such as in A.S.Fraenkel and J.Simpson [8, 9], J.Shallit et al [7].

Key words: the Fibonacci sequence; square; cube; algorithm; the sequence of return words.

## 1 Introduction

Let 𝒜 = { a, b } \mathcal{A}=\{a,b\} be a binary alphabet. The concatenation of factors ν \nu and ω \omega denoted by ν ​ ω \nu\omega. The Fibonacci sequence 𝔽 \mathbb{F} is the fixed point beginning with a a of the Fibonacci morphism σ \sigma defined by σ ⁡ ( a) = a ​ b \sigma(a)=ab and σ ⁡ ( b) = a \sigma(b)=a. As a classical example over a binary alphabet, 𝔽 \mathbb{F} having many remarkable properties, we refer to M.Lothaire [14, 15], J.M.Allouche and J.Shallit [1], Berstel [2, 3].

Let ω \omega be a factor of 𝔽 \mathbb{F}, denoted by ω ≺ 𝔽 \omega\prec\mathbb{F}. Since 𝔽 \mathbb{F} is uniformly recurrent, ω \omega occurs infinitely many times. Let ω p \omega_{p} be the p p -th occurrence of ω \omega. If the factor ω \omega and integer p p such that ω p ​ ω p + 1 \omega_{p}\omega_{p+1} (resp. ω p ​ ω p + 1 ​ ω p + 2 \omega_{p}\omega_{p+1}\omega_{p+2}) is the factor of 𝔽 \mathbb{F}, we call it a square (resp. cube) of 𝔽 \mathbb{F}. As we know, 𝔽 \mathbb{F} contains no fourth powers. The properties of squares and cubes are objects of a great interest in many aspects of mathematics and computer science etc.

We denote F m = σ m ​ ( a) F_{m}=\sigma^{m}(a) for m ≥ 0 m\geq 0 and define F − 1 = b F_{-1}=b, F − 2 = ε F_{-2}=\varepsilon (empty word). Define f m = | F m | f_{m}=|F_{m}| the m m -th Fibonacci number, f − 2 = 0 f_{-2}=0, f − 1 = 1 f_{-1}=1, f m + 1 = f m + f m − 1 f_{m+1}=f_{m}+f_{m-1} for m ≥ − 1 m\geq-1. Let 𝔽 ⁡ [1, n] \mathbb{F}[1,n] be the prefix of 𝔽 \mathbb{F} of length n n. In this paper, we consider the four functions below:

A ⁡ ( n):= ♯ ⁡ { ω: ω ​ ω ≺ 𝔽 ⁡ [1, n] } A(n):=\sharp\{\omega:\omega\omega\prec\mathbb{F}[1,n]\}, the number of distinct squares in 𝔽 ⁡ [1, n] \mathbb{F}[1,n];

B ⁡ ( n):= ♯ ⁡ { ( ω, p): ω p ​ ω p + 1 ≺ 𝔽 ⁡ [1, n] } B(n):=\sharp\{(\omega,p):\omega_{p}\omega_{p+1}\prec\mathbb{F}[1,n]\}, the number of repeated squares in 𝔽 ⁡ [1, n] \mathbb{F}[1,n];

C ⁡ ( n):= ♯ ⁡ { ω: ω ​ ω ​ ω ≺ 𝔽 ⁡ [1, n] } C(n):=\sharp\{\omega:\omega\omega\omega\prec\mathbb{F}[1,n]\}, the number of distinct cubes in 𝔽 ⁡ [1, n] \mathbb{F}[1,n];

D ⁡ ( n):= ♯ ⁡ { ( ω, p): ω p ​ ω p + 1 ​ ω p + 2 ≺ 𝔽 ⁡ [1, n] } D(n):=\sharp\{(\omega,p):\omega_{p}\omega_{p+1}\omega_{p+2}\prec\mathbb{F}[1,n]\}, the number of repeated cubes in 𝔽 ⁡ [1, n] \mathbb{F}[1,n].

The methods for counting the four functions have attracted some many authors, but known results are not rich. A.S.Fraenkel and J.Simpson gave the expression of A ⁡ ( f m) A(f_{m}) and B ⁡ ( f m) B(f_{m}) in 1999 [8] and 2014 [9]. In 2014, C.F.Du, H.Mousavi, L.Schaeffer and J.Shallit gave the expression of B ⁡ ( f m) B(f_{m}) and D ⁡ ( f m) D(f_{m}) by mechanical methods, see Theorem 58 and Theorem 59 in [7]. In this paper, we give the explicit expressions of A ⁡ ( n) A(n), B ⁡ ( f m) B(f_{m}), C ⁡ ( n) C(n) and D ⁡ ( f m) D(f_{m}). Although we haven’t get the explicit expressions of B ⁡ ( n) B(n) and D ⁡ ( n) D(n), we give fast algorithms for counting B ⁡ ( n) B(n) and D ⁡ ( n) D(n) for all n n.

The main tool of this paper is the “structure properties” of the sequence of return words in the Fibonacci sequence, which introduced and studied in [11], also see Property 2.2. The definition of return words is from F.Durand [6]. Let ω \omega be a factor of 𝔽 \mathbb{F}. For p ≥ 1 p\geq 1, let ω p = x i + 1 ⋯ x i + n \omega_{p}=x_{i+1}\cdots x_{i+n} and ω p + 1 = x j + 1 ⋯ x j + n \omega_{p+1}=x_{j+1}\cdots x_{j+n}. The factor x i + 1 ⋯ x j x_{i+1}\cdots x_{j} is called the p p -th return word of ω \omega and denoted by r p ​ ( ω) r_{p}(\omega). The sequence { r p ​ ( ω) } p ≥ 1 \{r_{p}(\omega)\}_{p\geq 1} is called the sequences of the return words of factor ω \omega.

By the “structure properties” (Property 2.2), we can determine the positions of all ω p \omega_{p}. By the definition of square (resp. cube) and return word, we have

 | ω p ​ ω p + 1 ≺ 𝔽 ⇔ r p ​ ( ω) = ω, ω p ​ ω p + 1 ​ ω p + 2 ≺ 𝔽 ⇔ r p ​ ( ω) = r p + 1 ​ ( ω) = ω, \omega_{p}\omega_{p+1}\prec\mathbb{F}\Leftrightarrow r_{p}(\omega)=\omega,~~\omega_{p}\omega_{p+1}\omega_{p+2}\prec\mathbb{F}\Leftrightarrow r_{p}(\omega)=r_{p+1}(\omega)=\omega, |  |

where the “=” means “have the same expressions”. By these relations, we can determine the positions of all squares and cubes, and then get A ⁡ ( n) A(n), B ⁡ ( n) B(n), C ⁡ ( n) C(n) and D ⁡ ( n) D(n). But this method is complicated, another improved and fast method is used in this paper.

This paper is organized as follows. Section 2 present some basic notations and known results. Section 3 prove some basic properties of squares. We determine A ⁡ ( n) A(n) (distinct squares) in Section 4. Section 5 is devoted to establish the recursive structure of squares, then we determine B ⁡ ( n) B(n) (repeated squares) in Section 6. Similarly, we establish the recursive structure of cubes, then determine C ⁡ ( n) C(n) (distinct cubes) and D ⁡ ( n) D(n) (repeated cubes) in Section 7 to 10.

## 2 Preliminaries

Let τ = x 1 ⋯ x n \tau=x_{1}\cdots x_{n} be a finite word (or τ = x 1 x 2 ⋯ \tau=x_{1}x_{2}\cdots be a sequence). For any i ≤ j ≤ n i\leq j\leq n, define τ [i, j]:= x i x i + 1 ⋯ x j − 1 x j \tau[i,j]:=x_{i}x_{i+1}\cdots x_{j-1}x_{j}. By convention, we denote τ ⁡ [i]:= τ ⁡ [i, i] = x i \tau[i]:=\tau[i,i]=x_{i} and τ ⁡ [i, i − 1] = ε \tau[i,i-1]=\varepsilon. Notation ν ⊳ ω \nu\triangleright\omega means word ν \nu is a suffix of word ω \omega.

For m ≥ − 1 m\geq-1, let δ m ∈ { a, b } \delta_{m}\in\{a,b\} be the last letter of F m F_{m}, then δ m = a \delta_{m}=a iff m m is even. The m m -th singular word is defined as K m = δ m + 1 ​ F m ​ δ m − 1 = δ m + 1 ​ F m ​ [1, f m − 1] K_{m}=\delta_{m+1}F_{m}\delta_{m}^{-1}=\delta_{m+1}F_{m}[1,f_{m}-1] for m ≥ − 1 m\geq-1. By Property 2(9) in [18], all singular words are palindromes. Let K ​ e ​ r ​ ( ω) Ker(\omega) be the maximal singular word occurring in factor ω \omega, called the kernel of ω \omega. Then by Theorem 1.9 in [11], K ​ e ​ r ​ ( ω) Ker(\omega) occurs in ω \omega only once. Moreover

###### Property 2.1 (Theorem 2.8 in [11]).

K ​ e ​ r ​ ( ω p) = K ​ e ​ r ​ ( ω) p Ker(\omega_{p})=Ker(\omega)_{p} for all ω ∈ 𝔽 \omega\in\mathbb{F} and p ≥ 1. p\geq 1.

This means, let K ​ e ​ r ​ ( ω) = K m Ker(\omega)=K_{m}, then the maximal singular word occurring in ω p \omega_{p} is just K m, p K_{m,p}. For instance, K ​ e ​ r ​ ( a ​ b ​ a) = b Ker(aba)=b, ( a ​ b ​ a) 3 = 𝔽 ⁡ [6, 8] (aba)_{3}=\mathbb{F}[6,8], ( b) 3 = 𝔽 ⁡ [7] (b)_{3}=\mathbb{F}[7], so K ​ e ​ r ​ ( ( a ​ b ​ a) 3) = ( b) 3 Ker((aba)_{3})=(b)_{3}, ( a ​ b ​ a) 3 = a ​ ( b) 3 ​ a (aba)_{3}=a(b)_{3}a.

###### Property 2.2 (Theorem 2.11 in [11]).

For any factor ω \omega, the sequence of return words { r p ​ ( ω) } p ≥ 1 \{r_{p}(\omega)\}_{p\geq 1} is the Fibonacci sequence over the alphabet { r 1 ​ ( ω), r 2 ​ ( ω) } \{r_{1}(\omega),r_{2}(\omega)\}.

Property 2.3 and 2.4 are useful in our proofs. Property 2.3 can be proved by induction. Since all singular words are palindromes, Property 2.4 holds by the cylinder structure of palindromes in [13].

###### Property 2.3 (Lemma 2.2 in [11]).

For m ≥ − 1 m\geq-1, (1) K m + 3 = K m + 1 ​ K m ​ K m + 1 K_{m+3}=K_{m+1}K_{m}K_{m+1}.

(2) K m + 2 = K m ​ K m + 1 ​ δ m − 1 ​ δ m + 1 = δ m − 1 ​ δ m + 1 ​ K m + 1 ​ K m K_{m+2}=K_{m}K_{m+1}\delta_{m}^{-1}\delta_{m+1}=\delta_{m}^{-1}\delta_{m+1}K_{m+1}K_{m}.

###### Property 2.4.

K m ≺ K m + 3 ​ [2, f m + 3 − 1] K_{m}\prec K_{m+3}[2,f_{m+3}-1], K m + 1 ​ ≺ K m + 3 ​ [2, f m + 3 − 1] K_{m+1}\not\!\prec K_{m+3}[2,f_{m+3}-1], K m + 2 ​ ≺ K m + 3 ​ [2, f m + 3 − 1] K_{m+2}\not\!\prec K_{m+3}[2,f_{m+3}-1].

## 3 Basic properties of squares

By Definition 2.9 and Corollary 2.10 in [11], any factor ω \omega with kernel K m K_{m} can be expressed uniquely as ω = K m + 1 ​ [i, f m + 1] ​ K m ​ K m + 1 ​ [1, j] = K m + 3 ​ [i, f m + 2 + j], \omega=K_{m+1}[i,f_{m+1}]K_{m}K_{m+1}[1,j]=K_{m+3}[i,f_{m+2}+j], where 2 ≤ i ≤ f m + 1 + 1 2\leq i\leq f_{m+1}+1 and 0 ≤ j ≤ f m + 1 − 1 0\leq j\leq f_{m+1}-1. By Property 2.1, ω p ​ ω p + 1 ≺ 𝔽 \omega_{p}\omega_{p+1}\prec\mathbb{F} means

 | ω p ​ ω p + 1 = K m + 1 ​ [i, f m + 1] ​ K m, p ​ K m + 1 ​ [1, j] ​ K m + 1 ​ [i, f m + 1] ⏟ r p ​ ( K m) ​ K m, p + 1 ​ K m + 1 ​ [1, j] ≺ 𝔽. \omega_{p}\omega_{p+1}=K_{m+1}[i,f_{m+1}]\underbrace{K_{m,p}K_{m+1}[1,j]K_{m+1}[i,f_{m+1}]}_{r_{p}(K_{m})}K_{m,p+1}K_{m+1}[1,j]\prec\mathbb{F}. |  |

By Property 2.2, K m K_{m} has only two distinct return words r 1 ​ ( K m) = K m ​ K m + 1 r_{1}(K_{m})=K_{m}K_{m+1} and r 2 ​ ( K m) = K m ​ K m − 1 r_{2}(K_{m})=K_{m}K_{m-1}, so ω p ​ ω p + 1 ≺ 𝔽 \omega_{p}\omega_{p+1}\prec\mathbb{F} has two cases as below, and in each case, | ω | = | r p ​ ( K m) | |\omega|=|r_{p}(K_{m})|.

Case 1. r p ​ ( K m) = r 1 ​ ( K m) = K m ​ K m + 1 r_{p}(K_{m})=r_{1}(K_{m})=K_{m}K_{m+1}. Comparing the two expressions of r p ​ ( K m) r_{p}(K_{m}), we have

 | K m ​ K m + 1 ​ [1, j] ​ K m + 1 ​ [i, f m + 1] = K m ​ K m + 1 ⇒ j = i − 1. K_{m}K_{m+1}[1,j]K_{m+1}[i,f_{m+1}]=K_{m}K_{m+1}\Rightarrow j=i-1. |  |

Comparing the two ranges of i i that 2 ≤ i ≤ f m + 1 + 1 2\leq i\leq f_{m+1}+1 and 0 ≤ j = i − 1 ≤ f m + 1 − 1 0\leq j=i-1\leq f_{m+1}-1, we have 2 ≤ i ≤ f m + 1 2\leq i\leq f_{m+1} and m ≥ 0 m\geq 0. Moreover | ω | = | r 1 ​ ( K m) | = f m + 2 |\omega|=|r_{1}(K_{m})|=f_{m+2} and

 | ω ​ ω = K m + 1 ​ [i, f m + 1] ​ K m ​ K m + 1 ​ K m ​ K m + 1 ​ [1, i − 1] = K m + 2 ​ [i, f m + 2] ​ K m + 1 ¯ ​ K m + 2 ​ [1, f m + i − 1] = K m + 4 ​ [i, 2 ​ f m + 2 + i − 1]. \begin{split}\omega\omega=&K_{m+1}[i,f_{m+1}]K_{m}K_{m+1}K_{m}K_{m+1}[1,i-1]\\ =&K_{m+2}[i,f_{m+2}]\underline{K_{m+1}}K_{m+2}[1,f_{m}+i-1]=K_{m+4}[i,2f_{m+2}+i-1].\end{split} |  |

The second and third equalities hold by Property 2.3.

Since K m + 1 ≺ ω ​ ω ≺ K m + 4 ​ [2, f m + 4 − 1] K_{m+1}\prec\omega\omega\prec K_{m+4}[2,f_{m+4}-1], by Property 2.4, K ​ e ​ r ​ ( ω ​ ω) = K m + 1 Ker(\omega\omega)=K_{m+1}.

Case 2. r p ​ ( K m) = r 2 ​ ( K m) = K m ​ K m − 1 r_{p}(K_{m})=r_{2}(K_{m})=K_{m}K_{m-1}. Comparing the two expressions, we have

 | K m ​ K m + 1 ​ [1, j] ​ K m + 1 ​ [i, f m + 1] = K m ​ K m − 1 ⇒ j = i − f m − 1. K_{m}K_{m+1}[1,j]K_{m+1}[i,f_{m+1}]=K_{m}K_{m-1}\Rightarrow j=i-f_{m}-1. |  |

So f m + 1 ≤ i ≤ f m + 1 + 1 f_{m}+1\leq i\leq f_{m+1}+1 and m ≥ − 1 m\geq-1. Moreover | ω | = | r 2 ​ ( K m) | = f m + 1 |\omega|=|r_{2}(K_{m})|=f_{m+1} and

 | ω ​ ω = K m + 1 ​ [i, f m + 1] ​ K m ​ K m − 1 ​ K m ​ K m + 1 ​ [1, i − f m − 1] = K m + 1 ​ [i, f m + 1] ​ K m + 2 ¯ ​ K m + 1 ​ [1, i − f m − 1] = K m + 5 ​ [f m + 2 + i, f m + 3 + f m + 1 + i − 1]. \begin{split}\omega\omega=&K_{m+1}[i,f_{m+1}]K_{m}K_{m-1}K_{m}K_{m+1}[1,i-f_{m}-1]\\ =&K_{m+1}[i,f_{m+1}]\underline{K_{m+2}}K_{m+1}[1,i-f_{m}-1]=K_{m+5}[f_{m+2}+i,f_{m+3}+f_{m+1}+i-1].\end{split} |  |

Since K m + 2 ≺ ω ​ ω ≺ K m + 5 ​ [2, f m + 4 − 1] K_{m+2}\prec\omega\omega\prec K_{m+5}[2,f_{m+4}-1], by Property 2.4, K ​ e ​ r ​ ( ω ​ ω) = K m + 2 Ker(\omega\omega)=K_{m+2}.

###### Remark 3.1.

By the discussion above, we have: all squares in 𝔽 \mathbb{F} are of length 2 ​ f m 2f_{m} for some m ≥ 0 m\geq 0; for all m ≥ 0 m\geq 0, there exists a square of length 2 ​ f m 2f_{m} in 𝔽 \mathbb{F}. This is a known result of P.S e ´ ​ e ´ \acute{e}\acute{e} bold [16].

###### Property 3.2 (Property 4.1 in [13]).

P ⁡ ( K m, p) = p ​ f m + 1 + ( ⌊ ϕ ​ p ⌋ + 1) ​ f m − 1 P(K_{m},p)=pf_{m+1}+(\lfloor\phi p\rfloor+1)f_{m}-1 for m ≥ − 1 m\geq-1, p ≥ 1 p\geq 1.

###### Corollary 3.3 (Corollary 4.2 in [13]).

P ⁡ ( a, p) = p + ⌊ ϕ ​ p ⌋ P(a,p)=p+\lfloor\phi p\rfloor, P ⁡ ( b, p) = 2 ​ p + ⌊ ϕ ​ p ⌋ P(b,p)=2p+\lfloor\phi p\rfloor for p ≥ 1 p\geq 1.

For m, p ≥ 1 m,p\geq 1, we define two sets below

 | { ⟨ 1, K m, p ⟩:= { P ( ω ω, p): K e r ( ω ω) = K m, | ω | = f m + 1, ω ω ≺ 𝔽 } ⟨ 2, K m, p ⟩:= { P ( ω ω, p): K e r ( ω ω) = K m, | ω | = f m − 1, ω ω ≺ 𝔽 } \begin{cases}\langle 1,K_{m},p\rangle:=\{P(\omega\omega,p):Ker(\omega\omega)=K_{m},|\omega|=f_{m+1},\omega\omega\prec\mathbb{F}\}\\ \langle 2,K_{m},p\rangle:=\{P(\omega\omega,p):Ker(\omega\omega)=K_{m},|\omega|=f_{m-1},\omega\omega\prec\mathbb{F}\}\end{cases} |  |

Obviously they correspond the two cases of squares respectively. By Property 3.2 we have

 | ⟨ 1, K m, p ⟩ = { P ( ω, p): ω = K m + 1 [i, f m + 1] K m K m + 1 [1, f m − 1 + i − 1], 2 ≤ i ≤ f m } = { P ( K m, p) + f m − 1 + i − 1, 2 ≤ i ≤ f m } = { p ​ f m + 1 + ⌊ ϕ ​ p ⌋ ​ f m + f m + 1, ⋯, p ​ f m + 1 + ⌊ ϕ ​ p ⌋ ​ f m + f m + 2 − 2 }, ⟨ 2, K m, p ⟩ = { P ( ω, p): ω = K m − 1 [i, f m − 1] K m K m − 1 [1, i − f m − 2 − 1], f m − 2 + 1 ≤ i ≤ f m − 1 + 1 } = { P ( K m, p) + i − f m − 2 − 1, f m − 2 + 1 ≤ i ≤ f m − 1 + 1 } = { p ​ f m + 1 + ⌊ ϕ ​ p ⌋ ​ f m + f m − 1, ⋯, p ​ f m + 1 + ⌊ ϕ ​ p ⌋ ​ f m + 2 ​ f m − 1 − 1 }. \begin{split}\langle 1,K_{m},p\rangle=&\{P(\omega,p):\omega=K_{m+1}[i,f_{m+1}]K_{m}K_{m+1}[1,f_{m-1}+i-1],2\leq i\leq f_{m}\}\\ =&\{P(K_{m},p)+f_{m-1}+i-1,2\leq i\leq f_{m}\}\\ =&\{pf_{m+1}+\lfloor\phi p\rfloor f_{m}+f_{m+1},\cdots,pf_{m+1}+\lfloor\phi p\rfloor f_{m}+f_{m+2}-2\},\\ \langle 2,K_{m},p\rangle=&\{P(\omega,p):\omega=K_{m-1}[i,f_{m-1}]K_{m}K_{m-1}[1,i-f_{m-2}-1],f_{m-2}+1\leq i\leq f_{m-1}+1\}\\ =&\{P(K_{m},p)+i-f_{m-2}-1,f_{m-2}+1\leq i\leq f_{m-1}+1\}\\ =&\{pf_{m+1}+\lfloor\phi p\rfloor f_{m}+f_{m}-1,\cdots,pf_{m+1}+\lfloor\phi p\rfloor f_{m}+2f_{m-1}-1\}.\end{split} |  |

###### Corollary 3.4.

♯ ⁡ ⟨ 1, K m, p ⟩ = f m − 1 \sharp\langle 1,K_{m},p\rangle=f_{m}-1 and ♯ ⁡ ⟨ 2, K m, p ⟩ = f m − 3 + 1 \sharp\langle 2,K_{m},p\rangle=f_{m-3}+1 for m, p ≥ 1 m,p\geq 1.

## 4 The number of distinct squares in 𝔽 ⁡ [1, n] \mathbb{F}[1,n]

Denote a ( n):= ♯ { ω: ω ω ⊳ 𝔽 [1, n], ω ω ≺ 𝔽 [1, n − 1] } a(n):=\sharp\{\omega:\omega\omega\triangleright\mathbb{F}[1,n],\omega\omega\not\!\prec\mathbb{F}[1,n-1]\}, obversely, A ⁡ ( n) = ∑ i = 1 n a ⁡ ( i) A(n)=\sum_{i=1}^{n}a(i). In order to count a ⁡ ( n) a(n), we only need to consider ⟨ i, K m, 1 ⟩ \langle i,K_{m},1\rangle where i = 1, 2 i=1,2.

###### Property 4.1.

⟨ 1, K m, 1 ⟩ = { 2 ​ f m + 1, ⋯, f m + 3 − 2 } \langle 1,K_{m},1\rangle=\{2f_{m+1},\cdots,f_{m+3}-2\}, ⟨ 2, K m, 1 ⟩ = { f m + 2 − 1, ⋯, f m + 1 + 2 ​ f m − 1 − 1 } \langle 2,K_{m},1\rangle=\{f_{m+2}-1,\cdots,f_{m+1}+2f_{m-1}-1\}.

It is easy to see that sets ⟨ i, K m, 1 ⟩ \langle i,K_{m},1\rangle are pairwise disjoint, and each set contains some consecutive integers. Therefore we get a chain

 | ⟨ 2, K 1, 1 ⟩, ⟨ 1, K 1, 1 ⟩, ⋯, ⟨ 1, K m − 1, 1 ⟩, ⟨ 2, K m, 1 ⟩, ⟨ 1, K m, 1 ⟩, ⟨ 2, K m + 1, 1 ⟩, ⋯ \langle 2,K_{1},1\rangle,\langle 1,K_{1},1\rangle,\cdots,\langle 1,K_{m-1},1\rangle,\langle 2,K_{m},1\rangle,\langle 1,K_{m},1\rangle,\langle 2,K_{m+1},1\rangle,\cdots |  |

By this chain, a ⁡ ( n) = 1 a(n)=1 iff n ∈ ∪ m ≥ 1 ( ⟨ 2, K m, 1 ⟩ ∪ ⟨ 1, K m, 1 ⟩) n\in\cup_{m\geq 1}(\langle 2,K_{m},1\rangle\cup\langle 1,K_{m},1\rangle). The “ ∪ \cup ” means pairwise disjoint union in this paper. Moreover, we have ⟨ 1, K m, 1 ⟩ ∪ ⟨ 2, K m + 1, 1 ⟩ = { 2 ​ f m + 1, ⋯, f m + 2 + 2 ​ f m − 1 } \langle 1,K_{m},1\rangle\cup\langle 2,K_{m+1},1\rangle=\{2f_{m+1},\cdots,f_{m+2}+2f_{m}-1\}.

###### Property 4.2.

a ⁡ ( 1) = a ⁡ ( 2) = a ⁡ ( 3) = 0 a(1)=a(2)=a(3)=0, a ⁡ ( 4) = 1 a(4)=1 and for n ≥ 5 n\geq 5

 | a ( n) = 1 iff n ∈ ∪ m ≥ 1 { 2 f m + 1, ⋯, f m + 2 + 2 f m − 1 }. a(n)=1\text{ iff }n\in\cup_{m\geq 1}\{2f_{m+1},\cdots,f_{m+2}+2f_{m}-1\}. |  |

One method for counting A ⁡ ( n) A(n) is by A ⁡ ( n) = ∑ i = 1 n a ⁡ ( i) A(n)=\sum_{i=1}^{n}a(i). By consider A ⁡ ( f m + 2 + 2 ​ f m − 1) A(f_{m+2}+2f_{m}-1) for m ≥ 1 m\geq 1, we can give a fast algorithm of A ⁡ ( n) A(n) for all n ≥ 1 n\geq 1. Since ∑ i = − 1 m f i = f m + 2 − 1 \sum_{i=-1}^{m}f_{i}=f_{m+2}-1,

 | A ⁡ ( f m + 2 + 2 ​ f m − 1) = a ⁡ ( 4) + ∑ i = 1 m ♯ ⁡ { 2 ​ f i + 1, ⋯, f i + 2 + 2 ​ f i − 1 } = 1 + ∑ i = 1 m ( f i + f i − 2) = 1 + ∑ i = − 1 m f i − f 0 − f − 1 + ∑ i = − 1 m − 2 f i = f m + 2 + f m − 3. \begin{array}[]{rl}&A(f_{m+2}+2f_{m}-1)=a(4)+\sum\limits_{i=1}^{m}\sharp\{2f_{i+1},\cdots,f_{i+2}+2f_{i}-1\}\\ =&1+\sum\limits_{i=1}^{m}(f_{i}+f_{i-2})=1+\sum\limits_{i=-1}^{m}f_{i}-f_{0}-f_{-1}+\sum\limits_{i=-1}^{m-2}f_{i}=f_{m+2}+f_{m}-3.\end{array} |  |

###### Theorem 4.3.

For all n ≥ 1 n\geq 1, let m m satisfies 2 ​ f m ≤ n < 2 ​ f m + 1 2f_{m}\leq n<2f_{m+1},

 | A ⁡ ( n) = { n − f m − 1 − 2, n ≤ f m + 1 + 2 ​ f m − 1 − 1; f m + 1 + f m − 1 − 3, o ​ t ​ h ​ e ​ r ​ w ​ i ​ s ​ e. A(n)=\begin{cases}n-f_{m-1}-2,&n\leq f_{m+1}+2f_{m-1}-1;\\ f_{m+1}+f_{m-1}-3,&otherwise.\end{cases} |  |

###### Proof.

When f m + 1 + 2 ​ f m − 1 ≤ n ≤ 2 ​ f m + 1 − 1 f_{m+1}+2f_{m-1}\leq n\leq 2f_{m+1}-1, a ⁡ ( n) = 0 a(n)=0, A ⁡ ( n) = A ⁡ ( f m + 1 + 2 ​ f m − 1 − 1) = f m + 1 + f m − 1 − 3 A(n)=A(f_{m+1}+2f_{m-1}-1)=f_{m+1}+f_{m-1}-3.

When 2 ​ f m ≤ n ≤ f m + 1 + 2 ​ f m − 1 − 1 2f_{m}\leq n\leq f_{m+1}+2f_{m-1}-1, a ⁡ ( n) = 1 a(n)=1, A ⁡ ( n) = A ⁡ ( 2 ​ f m − 1) + n − 2 ​ f m + 1 A(n)=A(2f_{m}-1)+n-2f_{m}+1. Since A ⁡ ( 2 ​ f m − 1) = A ⁡ ( f m + 2 ​ f m − 2 − 1) A(2f_{m}-1)=A(f_{m}+2f_{m-2}-1), we have A ⁡ ( n) = n − f m − 1 − 2 A(n)=n-f_{m-1}-2. Thus the conclusion holds. ∎

###### Remark 4.4.

Since 2 ​ f m − 2 ≤ f m ≤ f m − 1 + 2 ​ f m − 3 − 1 2f_{m-2}\leq f_{m}\leq f_{m-1}+2f_{m-3}-1 for m ≥ 2 m\geq 2, as a spacial case of Theorem 4.3,

 | A ⁡ ( f m) = f m − f m − 3 − 2 = 2 ​ f m − 2 − 2. A(f_{m})=f_{m}-f_{m-3}-2=2f_{m-2}-2. |  |

This is a known result of A.S.Fraenkel and J.Simpson, see Theorem 1 in [8].

## 5 The recursive structure of squares

In this section, we establish a recursive structure of squares. Using it, we will count the number of repeated squares in 𝔽 ⁡ [1, n] \mathbb{F}[1,n] (i.e. B ⁡ ( n) B(n)) in Section 6. For m, p ≥ 1 m,p\geq 1, consider the vectors

 | Γ 1, m, p: = [p ​ f m + 1 + ⌊ ϕ ​ p ⌋ ​ f m + f m + 1 − 1, ⟨ 1, K m, p ⟩] = [p ​ f m + 1 + ⌊ ϕ ​ p ⌋ ​ f m + f m + 1 − 1, ⋯, p ​ f m + 1 + ⌊ ϕ ​ p ⌋ ​ f m + f m + 2 − 2]; Γ 2, m, p: = [⟨ 2, K m, p ⟩, p ​ f m + 1 + ⌊ ϕ ​ p ⌋ ​ f m + 2 ​ f m − 1, ⋯, p ​ f m + 1 + ⌊ ϕ ​ p ⌋ ​ f m + f m + 1 − 2] = [p ​ f m + 1 + ⌊ ϕ ​ p ⌋ ​ f m + f m − 1, ⋯, p ​ f m + 1 + ⌊ ϕ ​ p ⌋ ​ f m + f m + 1 − 2]. \begin{split}\Gamma_{1,m,p}:&=[pf_{m+1}+\lfloor\phi p\rfloor f_{m}+f_{m+1}-1,\langle 1,K_{m},p\rangle]\\ &=[pf_{m+1}+\lfloor\phi p\rfloor f_{m}+f_{m+1}-1,\cdots,pf_{m+1}+\lfloor\phi p\rfloor f_{m}+f_{m+2}-2];\\ \Gamma_{2,m,p}:&=[\langle 2,K_{m},p\rangle,pf_{m+1}+\lfloor\phi p\rfloor f_{m}+2f_{m-1},\cdots,pf_{m+1}+\lfloor\phi p\rfloor f_{m}+f_{m+1}-2]\\ &=[pf_{m+1}+\lfloor\phi p\rfloor f_{m}+f_{m}-1,\cdots,pf_{m+1}+\lfloor\phi p\rfloor f_{m}+f_{m+1}-2].\end{split} |  |

Here vector [⟨ i, K m, p ⟩] [\langle i,K_{m},p\rangle] means arrange all elements in set ⟨ i, K m, p ⟩ \langle i,K_{m},p\rangle, i = 1, 2 i=1,2.

Obversely, each Γ i, m, p \Gamma_{i,m,p} contains consecutive integers. The numbers of components in vectors Γ 1, m, p \Gamma_{1,m,p} and Γ 2, m, p \Gamma_{2,m,p} are f m f_{m} and f m − 1 f_{m-1} respectively. Moreover max ⁡ Γ 2, m, p + 1 = min ⁡ Γ 1, m, p \max\Gamma_{2,m,p}+1=\min\Gamma_{1,m,p} for m, p ≥ 1 m,p\geq 1.

###### Lemma 5.1 (Lemma 5.3 and 5.4 in [13]).

⌊ ϕ ⁡ ( p + ⌊ ϕ ​ p ⌋ + 1) ⌋ = p \lfloor\phi(p+\lfloor\phi p\rfloor+1)\rfloor=p, ⌊ ϕ ⁡ ( 2 ​ p + ⌊ ϕ ​ p ⌋ + 1) ⌋ = p + ⌊ ϕ ​ p ⌋ \lfloor\phi(2p+\lfloor\phi p\rfloor+1)\rfloor=p+\lfloor\phi p\rfloor.

###### Property 5.2.

Γ 1, m, p = [Γ 2, m − 1, P ⁡ ( a, p) + 1, Γ 1, m − 1, P ⁡ ( a, p) + 1] \Gamma_{1,m,p}=[\Gamma_{2,m-1,P(a,p)+1},\Gamma_{1,m-1,P(a,p)+1}] for m ≥ 2 m\geq 2, p ≥ 1 p\geq 1.

###### Proof.

By Corollary 3.3, P ⁡ ( a, p) + 1 = p + ⌊ ϕ ​ p ⌋ + 1 P(a,p)+1=p+\lfloor\phi p\rfloor+1. By Lemma 5.1, ⌊ ϕ ⁡ ( p + ⌊ ϕ ​ p ⌋ + 1) ⌋ = p \lfloor\phi(p+\lfloor\phi p\rfloor+1)\rfloor=p.

 | min ⁡ Γ 2, m − 1, P ⁡ ( a, p) + 1 = ( p + ⌊ ϕ ​ p ⌋ + 1) ​ f m + ⌊ ϕ ⁡ ( p + ⌊ ϕ ​ p ⌋ + 1) ⌋ ​ f m − 1 + f m − 1 − 1 = ( p + ⌊ ϕ ​ p ⌋ + 1) ​ f m + p ​ f m − 1 + f m − 1 − 1 = p ​ f m + 1 + ⌊ ϕ ​ p ⌋ ​ f m + f m + 1 − 1 = min ⁡ Γ 1, m, p; max ⁡ Γ 1, m − 1, P ⁡ ( a, p) + 1 = ( p + ⌊ ϕ ​ p ⌋ + 1) ​ f m + ⌊ ϕ ⁡ ( p + ⌊ ϕ ​ p ⌋ + 1) ⌋ ​ f m − 1 + f m + 1 − 2 = ( p + ⌊ ϕ ​ p ⌋ + 1) ​ f m + p ​ f m − 1 + f m + 1 − 2 = p ​ f m + 1 + ⌊ ϕ ​ p ⌋ ​ f m + f m + 2 − 2 = max ⁡ Γ 1, m, p. \begin{split}&\min\Gamma_{2,m-1,P(a,p)+1}=(p+\lfloor\phi p\rfloor+1)f_{m}+\lfloor\phi(p+\lfloor\phi p\rfloor+1)\rfloor f_{m-1}+f_{m-1}-1\\ =&(p+\lfloor\phi p\rfloor+1)f_{m}+pf_{m-1}+f_{m-1}-1=pf_{m+1}+\lfloor\phi p\rfloor f_{m}+f_{m+1}-1=\min\Gamma_{1,m,p};\\ &\max\Gamma_{1,m-1,P(a,p)+1}=(p+\lfloor\phi p\rfloor+1)f_{m}+\lfloor\phi(p+\lfloor\phi p\rfloor+1)\rfloor f_{m-1}+f_{m+1}-2\\ =&(p+\lfloor\phi p\rfloor+1)f_{m}+pf_{m-1}+f_{m+1}-2=pf_{m+1}+\lfloor\phi p\rfloor f_{m}+f_{m+2}-2=\max\Gamma_{1,m,p}.\end{split} |  |

Since max ⁡ Γ 2, m, p + 1 = min ⁡ Γ 1, m, p \max\Gamma_{2,m,p}+1=\min\Gamma_{1,m,p} for m, p ≥ 1 m,p\geq 1, max ⁡ Γ 2, m − 1, P ⁡ ( a, p) + 1 + 1 = min ⁡ Γ 1, m − 1, P ⁡ ( a, p) + 1 \max\Gamma_{2,m-1,P(a,p)+1}+1=\min\Gamma_{1,m-1,P(a,p)+1}. Thus the conclusion holds. ∎

By an analogous argument, we have

###### Property 5.3.

Γ 2, m, p = [Γ 2, m − 2, P ⁡ ( b, p) + 1, Γ 1, m − 2, P ⁡ ( b, p) + 1] \Gamma_{2,m,p}=[\Gamma_{2,m-2,P(b,p)+1},\Gamma_{1,m-2,P(b,p)+1}] for m ≥ 3 m\geq 3, p ≥ 1 p\geq 1.

In Property 5.2 and 5.3, we establish the recursive relations for any Γ 1, m, p \Gamma_{1,m,p} ( m ≥ 2 m\geq 2) and Γ 2, m, p \Gamma_{2,m,p} ( m ≥ 3 m\geq 3). By the one-to-one correspondence between Γ i, m, p \Gamma_{i,m,p} and ⟨ i, K m, p ⟩ \langle i,K_{m},p\rangle, we can define the recursive structure over { ⟨ i, K m, p ⟩ | i = 1, 2; m, p ≥ 1 } \{\langle i,K_{m},p\rangle|~i=1,2;~m,p\geq 1\} denoted by 𝒮 \mathcal{S}. Each ⟨ i, K m, p ⟩ \langle i,K_{m},p\rangle is an element in 𝒮 \mathcal{S}. The recursive structure 𝒮 \mathcal{S} is a family of finite trees with root ⟨ i, K m, 1 ⟩ \langle i,K_{m},1\rangle for all i = 1, 2 i=1,2, m ≥ 1 m\geq 1; and with recursive relations:

 | { τ 1 ​ ⟨ 1, K m, p ⟩ = ⟨ 2, K m − 1, P ⁡ ( a, p) + 1 ⟩ ∪ ⟨ 1, K m − 1, P ⁡ ( a, p) + 1 ⟩ for ​ m ≥ 2; τ 2 ​ ⟨ 2, K m, p ⟩ = ⟨ 2, K m − 2, P ⁡ ( b, p) + 1 ⟩ ∪ ⟨ 1, K m − 2, P ⁡ ( b, p) + 1 ⟩ for ​ m ≥ 3. \begin{cases}\tau_{1}\langle 1,K_{m},p\rangle=\langle 2,K_{m-1},P(a,p)+1\rangle\cup\langle 1,K_{m-1},P(a,p)+1\rangle&\text{for }m\geq 2;\\ \tau_{2}\langle 2,K_{m},p\rangle=\langle 2,K_{m-2},P(b,p)+1\rangle\cup\langle 1,K_{m-2},P(b,p)+1\rangle&\text{for }m\geq 3.\end{cases} |  |

###### Property 5.4.

Each ⟨ i, K m, p ⟩ \langle i,K_{m},p\rangle belongs to the recursive structure 𝒮 \mathcal{S}, i = 1, 2 i=1,2, m, p ≥ 1 m,p\geq 1.

###### Proof.

Each element ⟨ i, K m, 1 ⟩ \langle i,K_{m},1\rangle is root of a finite tree in 𝒮 \mathcal{S}. For m, p ≥ 1 m,p\geq 1,

 | { ⟨ 1, K m, P ⁡ ( a, p) + 1 ⟩ ∈ τ 1 ​ ⟨ 1, K m + 1, p ⟩ ⟨ 1, K m, P ⁡ ( b, p) + 1 ⟩ ∈ τ 2 ​ ⟨ 2, K m + 2, p ⟩ ​ and ​ { ⟨ 2, K m, P ⁡ ( a, p) + 1 ⟩ ∈ τ 1 ​ ⟨ 1, K m + 1, p ⟩ ⟨ 2, K m, P ⁡ ( b, p) + 1 ⟩ ∈ τ 2 ​ ⟨ 2, K m + 2, p ⟩ \begin{cases}\langle 1,K_{m},P(a,p)+1\rangle\in\tau_{1}\langle 1,K_{m+1},p\rangle\\ \langle 1,K_{m},P(b,p)+1\rangle\in\tau_{2}\langle 2,K_{m+2},p\rangle\end{cases}\text{and }\begin{cases}\langle 2,K_{m},P(a,p)+1\rangle\in\tau_{1}\langle 1,K_{m+1},p\rangle\\ \langle 2,K_{m},P(b,p)+1\rangle\in\tau_{2}\langle 2,K_{m+2},p\rangle\end{cases} |  |

Since ℕ = { 1 } ∪ { P ⁡ ( a, p) + 1 } ∪ { P ⁡ ( b, p) + 1 } \mathbb{N}=\{1\}\cup\{P(a,p)+1\}\cup\{P(b,p)+1\}, the recursive structure 𝒮 \mathcal{S} contains all ⟨ i, K m, p ⟩ \langle i,K_{m},p\rangle. ∎

On the other hand, by the recursive relations τ 1 \tau_{1} and τ 2 \tau_{2}, each element ⟨ i, K m, p ⟩ \langle i,K_{m},p\rangle has a unique position in 𝒮 \mathcal{S}. By Property 5.2 and 5.3, the trees in 𝒮 \mathcal{S} are pairwise disjoint. Fig.1 and Fig.2 show the two finite trees in the recursive structure 𝒮 \mathcal{S} with roots ⟨ 1, K 5, 1 ⟩ \langle 1,K_{5},1\rangle and ⟨ 2, K 5, 1 ⟩ \langle 2,K_{5},1\rangle respectively.

Fig.1: The finite tree in the recursive structure 𝒮 \mathcal{S} with root ⟨ 1, K 5, 1 ⟩ \langle 1,K_{5},1\rangle.

Fig.2: The finite tree in the recursive structure 𝒮 \mathcal{S} with root ⟨ 2, K 5, 1 ⟩ \langle 2,K_{5},1\rangle.

By the recursive structure 𝒮 \mathcal{S}, we have the relation between the number of squares ending at position Γ 1, m, p ​ [i] = p ​ f m + 1 + ⌊ ϕ ​ p ⌋ ​ f m + f m + 1 + i − 1 \Gamma_{1,m,p}[i]=pf_{m+1}+\lfloor\phi p\rfloor f_{m}+f_{m+1}+i-1 and Γ 1, m, 1 ​ [i] = 2 ​ f m + 1 + i − 1 \Gamma_{1,m,1}[i]=2f_{m+1}+i-1, see Property 5.5. Similarly, we have the relation between the number of squares ending at position Γ 2, m, p ​ [i] = p ​ f m + 1 + ⌊ ϕ ​ p ⌋ ​ f m + f m + i − 2 \Gamma_{2,m,p}[i]=pf_{m+1}+\lfloor\phi p\rfloor f_{m}+f_{m}+i-2 and Γ 2, m, 1 ​ [i] = f m + 2 + i − 2 \Gamma_{2,m,1}[i]=f_{m+2}+i-2, see Property 5.6.

###### Property 5.5.

For 1 ≤ i ≤ f m − 1 1\leq i\leq f_{m}-1,

 | { ω: ω ​ ω ⊳ 𝔽 ⁡ [1, 2 ​ f m + 1 + i − 1] } = { ω: ω ω ⊳ 𝔽 [1, p f m + 1 + ⌊ ϕ p ⌋ f m + f m + 1 + i − 1], K e r ( ω) = K j, 1 ≤ j ≤ m }. \begin{split}&\{\omega:\omega\omega\triangleright\mathbb{F}[1,2f_{m+1}+i-1]\}\\ =&\{\omega:\omega\omega\triangleright\mathbb{F}[1,pf_{m+1}+\lfloor\phi p\rfloor f_{m}+f_{m+1}+i-1],Ker(\omega)=K_{j},1\leq j\leq m\}.\end{split} |  |

###### Property 5.6.

For 1 ≤ i ≤ f m − 3 + 1 1\leq i\leq f_{m-3}+1,

 | { ω: ω ​ ω ⊳ 𝔽 ⁡ [1, f m + 2 + i − 2] } = { ω: ω ω ⊳ 𝔽 [1, p f m + 1 + ⌊ ϕ p ⌋ f m + f m + i − 2], K e r ( ω) = K j, 1 ≤ j ≤ m }. \begin{split}&\{\omega:\omega\omega\triangleright\mathbb{F}[1,f_{m+2}+i-2]\}\\ =&\{\omega:\omega\omega\triangleright\mathbb{F}[1,pf_{m+1}+\lfloor\phi p\rfloor f_{m}+f_{m}+i-2],Ker(\omega)=K_{j},1\leq j\leq m\}.\end{split} |  |

For instance, taking m = 3 m=3, p = 3 p=3 and i = 2 i=2 in the property above. All squares ending at position 13 are { a ​ a ​ b ​ a ​ a ​ b } \{aabaab\}. All squares ending at position 34 are { a ​ a ​ b ​ a ​ a ​ b, a ​ b ​ a ​ a ​ b ​ a ​ a ​ b ​ a ​ b ​ a ​ a ​ b ​ a ​ a ​ b } \{aabaab,abaabaababaabaab\}. Since K ​ e ​ r ​ ( a ​ a ​ b ​ a ​ a ​ b) = a ​ a ​ b ​ a ​ a = K 3 Ker(aabaab)=aabaa=K_{3} and K ​ e ​ r ​ ( a ​ b ​ a ​ a ​ b ​ a ​ a ​ b ​ a ​ b ​ a ​ a ​ b ​ a ​ a ​ b) = a ​ a ​ b ​ a ​ a ​ b ​ a ​ b ​ a ​ a ​ b ​ a ​ a = K 5 Ker(abaabaababaabaab)=aabaababaabaa=K_{5}, only { a ​ a ​ b ​ a ​ a ​ b } \{aabaab\} is square with kernel K j K_{j}, 1 ≤ j ≤ 3 1\leq j\leq 3. Fig.3 shows the relation:

Fig.3: An example of the graph embedding in the recursive structure 𝒮 \mathcal{S}.

From Fig.3 we can see that: in the tree with root ⟨ 2, K 5, 1 ⟩ \langle 2,K_{5},1\rangle, the branch from node ⟨ 2, K 3, 3 ⟩ \langle 2,K_{3},3\rangle is the graph embedding of the tree with root ⟨ 2, K 3, 1 ⟩ \langle 2,K_{3},1\rangle.

## 6 The number of repeated squares in 𝔽 ⁡ [1, n] \mathbb{F}[1,n]

Denote b ⁡ ( n):= ♯ ⁡ { ( ω, p): ω p ​ ω p + 1 ⊳ 𝔽 ⁡ [1, n] } b(n):=\sharp\{(\omega,p):\omega_{p}\omega_{p+1}\triangleright\mathbb{F}[1,n]\} the number of squares ending at position n n. By the definition of ⟨ i, K m, p ⟩ \langle i,K_{m},p\rangle, b ⁡ ( n) b(n) is equal to the number of integer n n occurs in the recursive structure 𝒮 \mathcal{S}. Thus we can calculate b ⁡ ( n) b(n) by the property below.

###### Property 6.1.

b ⁡ ( [1, 2, 3]) = [0, 0, 0] b([1,2,3])=[0,0,0], b ⁡ ( Γ 2, 1, 1) = b ⁡ ( [4]) = [1] b(\Gamma_{2,1,1})=b([4])=[1], b ⁡ ( Γ 1, 1, 1) = b ⁡ ( [5, 6]) = [0, 1] b(\Gamma_{1,1,1})=b([5,6])=[0,1], b ⁡ ( Γ 2, 2, 1) = b ⁡ ( [7, 8]) = [1, 1] b(\Gamma_{2,2,1})=b([7,8])=[1,1], b ⁡ ( Γ 1, 2, 1) = b ⁡ ( [9, 10, 11]) = [1, 1, 2] b(\Gamma_{1,2,1})=b([9,10,11])=[1,1,2], for m ≥ 3 m\geq 3,

 | { b ⁡ ( Γ 1, m, 1) = [b ⁡ ( Γ 2, m − 1, 1), b ⁡ ( Γ 1, m − 1, 1)] + [0, 1, ⋯, 1 ⏟ f m − 1]; b ⁡ ( Γ 2, m, 1) = [b ⁡ ( Γ 2, m − 2, 1), b ⁡ ( Γ 1, m − 2, 1)] + [1, ⋯, 1 ⏟ f m − 3 + 1, 0, ⋯, 0 ⏟ f m − 2 − 1]. \begin{cases}~b(\Gamma_{1,m,1})=[b(\Gamma_{2,m-1,1}),b(\Gamma_{1,m-1,1})]+[0,\underbrace{1,\cdots,1}_{f_{m}-1}];\\ ~b(\Gamma_{2,m,1})=[b(\Gamma_{2,m-2,1}),b(\Gamma_{1,m-2,1})]+[\underbrace{1,\cdots,1}_{f_{m-3}+1},\underbrace{0,\cdots,0}_{f_{m-2}-1}].\end{cases} |  |

The first few values of b ⁡ ( n) b(n) are b ⁡ ( [1, 2, 3]) = [0, 0, 0] b([1,2,3])=[0,0,0], b ⁡ ( [4]) = [1] b([4])=[1], b ⁡ ( [5, 6]) = [0, 1] b([5,6])=[0,1],

b ⁡ ( [7, 8]) = [1, 1] b([7,8])=[1,1], b ⁡ ( [9, 10, 11]) = [1, 1, 2] b([9,10,11])=[1,1,2], b ⁡ ( [12, 13, 14]) = [2, 1, 1] b([12,13,14])=[2,1,1], b ⁡ ( [15, ⋯, 19]) = [1, 2, 2, 2, 3] b([15,\cdots,19])=[1,2,2,2,3],

b ⁡ ( [20, ⋯, 24]) = [2, 2, 2, 1, 2] b([20,\cdots,24])=[2,2,2,1,2], b ⁡ ( [25, ⋯, 32]) = [2, 2, 2, 2, 3, 3, 3, 4] b([25,\cdots,32])=[2,2,2,2,3,3,3,4].

For m ≥ 3 m\geq 3, the immediately corollaries are

 | { ∑ b ⁡ ( Γ 1, m, 1) = ∑ b ⁡ ( Γ 2, m − 1, 1) + ∑ b ⁡ ( Γ 1, m − 1, 1) + f m − 1; ∑ b ⁡ ( Γ 2, m, 1) = ∑ b ⁡ ( Γ 2, m − 2, 1) + ∑ b ⁡ ( Γ 1, m − 2, 1) + f m − 3 + 1. \begin{cases}\sum b(\Gamma_{1,m,1})=\sum b(\Gamma_{2,m-1,1})+\sum b(\Gamma_{1,m-1,1})+f_{m}-1;\\ \sum b(\Gamma_{2,m,1})=\sum b(\Gamma_{2,m-2,1})+\sum b(\Gamma_{1,m-2,1})+f_{m-3}+1.\end{cases} |  |

###### Property 6.2.

For m ≥ 1 m\geq 1, (1) ∑ b ⁡ ( Γ 1, m, 1) = 2 ​ m + 5 5 ​ f m + 2 ​ m − 6 5 ​ f m − 2 − 1 \sum b(\Gamma_{1,m,1})=\frac{2m+5}{5}f_{m}+\frac{2m-6}{5}f_{m-2}-1,

(2) ∑ b ⁡ ( Γ 2, m, 1) = 2 ​ m − 2 5 ​ f m − 1 + 2 ​ m − 3 5 ​ f m − 3 + 1 \sum b(\Gamma_{2,m,1})=\frac{2m-2}{5}f_{m-1}+\frac{2m-3}{5}f_{m-3}+1.

Since Γ 1, m, 1 = [2 ​ f m + 1 − 1, ⋯, f m + 3 − 2] \Gamma_{1,m,1}=[2f_{m+1}-1,\cdots,f_{m+3}-2] and Γ 2, m, 1 = [f m + 2 − 1, ⋯, 2 ​ f m + 1 − 2] \Gamma_{2,m,1}=[f_{m+2}-1,\cdots,2f_{m+1}-2], we have B ⁡ ( f m + 3 − 2) = B ⁡ ( f m + 2 − 2) + ∑ b ⁡ ( Γ 2, m, 1) + ∑ b ⁡ ( Γ 1, m, 1) B(f_{m+3}-2)=B(f_{m+2}-2)+\sum b(\Gamma_{2,m,1})+\sum b(\Gamma_{1,m,1}) and B ⁡ ( 2 ​ f m + 1 − 2) = B ⁡ ( f m + 2 − 2) + ∑ b ⁡ ( Γ 2, m, 1) B(2f_{m+1}-2)=B(f_{m+2}-2)+\sum b(\Gamma_{2,m,1}). Thus by induction and Property 6.2,

###### Property 6.3.

(1) B ⁡ ( f m + 3 − 2) = 2 ​ m − 4 5 ​ f m + 3 + 2 ​ m 5 ​ f m + 1 + 4 B(f_{m+3}-2)=\frac{2m-4}{5}f_{m+3}+\frac{2m}{5}f_{m+1}+4 for m ≥ − 1 m\geq-1.

(2) B ⁡ ( 2 ​ f m + 1 − 2) = 4 ​ m − 11 5 ​ f m + 1 + 4 ​ m − 3 5 ​ f m − 1 + 5 B(2f_{m+1}-2)=\frac{4m-11}{5}f_{m+1}+\frac{4m-3}{5}f_{m-1}+5 for m ≥ 0 m\geq 0.

Property 6.4 can be proved by induction and Property 6.1.

###### Property 6.4.

b ⁡ ( f m − 1) = ⌊ m − 1 2 ⌋ b(f_{m}-1)=\lfloor\frac{m-1}{2}\rfloor, b ⁡ ( f m) = ⌊ m 2 − 1 ⌋ b(f_{m})=\lfloor\frac{m}{2}-1\rfloor, b ⁡ ( f m − 1) + b ⁡ ( f m) = m − 2 b(f_{m}-1)+b(f_{m})=m-2 for m ≥ 2 m\geq 2.

###### Remark 6.5.

Since B ⁡ ( f m) = B ⁡ ( f m − 2) + b ⁡ ( f m − 1) + b ⁡ ( f m) B(f_{m})=B(f_{m}-2)+b(f_{m}-1)+b(f_{m}), m ≥ 2 m\geq 2. By Property 6.3 and 6.4,

 | B ⁡ ( f m) = 4 5 ​ ( m + 1) ​ f m − 2 5 ​ ( m + 7) ​ f m − 1 − 4 ​ f m − 2 + m + 2 = 4 ​ m − 16 5 ​ f m − 2 ​ m − 6 5 ​ f m − 1 + m + 2. B(f_{m})=\tfrac{4}{5}(m+1)f_{m}-\tfrac{2}{5}(m+7)f_{m-1}-4f_{m-2}+m+2=\tfrac{4m-16}{5}f_{m}-\tfrac{2m-6}{5}f_{m-1}+m+2. |  |

This is a known result of A.S.Fraenkel and J.Simpson [9].

Obversely we can calculate B ⁡ ( n) B(n) by B ⁡ ( n) = ∑ i = 4 n b ⁡ ( i) B(n)=\sum_{i=4}^{n}b(i). But when n n is large, this method is complicated. Now we turn to give a fast algorithm. For any n ≥ 4 n\geq 4, let m m such that f m ≤ n + 1 < f m + 1 f_{m}\leq n+1<f_{m+1}. Since we already determine the expression of B ⁡ ( f m − 2) B(f_{m}-2) and B ⁡ ( 2 ​ f m − 1 − 2) B(2f_{m-1}-2) for m ≥ 2 m\geq 2, in order to give a fast algorithm of B ⁡ ( n) B(n), we only need to calculate ∑ i = f m − 1 n b ⁡ ( i) \sum_{i=f_{m}-1}^{n}b(i) or ∑ i = 2 ​ f m − 1 − 1 n b ⁡ ( i) \sum_{i=2f_{m-1}-1}^{n}b(i). One method is calculating b ⁡ ( n) b(n) by Property 6.1, the other method is using the corollaries as below.

###### Corollary 6.6.

For n ≥ 4 n\geq 4, let m m such that f m ≤ n + 1 ≤ 2 ​ f m − 1 − 1 f_{m}\leq n+1\leq 2f_{m-1}-1, then m ≥ 3 m\geq 3 and

 | ∑ i = f m − 1 n b ⁡ ( i) = { ∑ i = f m − 2 − 1 n − f m − 1 b ⁡ ( i) + n − f m + 2, n + 1 ≤ f m + f m − 5 − 1; ∑ i = f m − 2 + f m − 5 − 1 n − f m − 1 b ⁡ ( i) + 2 ​ m − 5 5 ​ f m − 5 + 2 ​ m − 11 5 ​ f m − 7 + 2, o ​ t ​ h ​ e ​ r ​ w ​ i ​ s ​ e. \sum_{i=f_{m}-1}^{n}b(i)=\begin{cases}\sum\limits_{i=f_{m-2}-1}^{n-f_{m-1}}b(i)+n-f_{m}+2,&n+1\leq f_{m}+f_{m-5}-1;\\ \sum\limits_{i=f_{m-2}+f_{m-5}-1}^{n-f_{m-1}}b(i)+\frac{2m-5}{5}f_{m-5}+\frac{2m-11}{5}f_{m-7}+2,&otherwise.\end{cases} |  |

###### Proof.

By Property 6.1, when f m ≤ n + 1 ≤ f m + f m − 5 − 1 f_{m}\leq n+1\leq f_{m}+f_{m-5}-1,

 | ∑ i = f m − 1 n b ⁡ ( i) = ∑ i = f m − 2 − 1 n − f m − 1 [b ⁡ ( i) + 1] = ∑ i = f m − 2 − 1 n − f m − 1 b ⁡ ( i) + n − f m + 2. \begin{array}[]{rl}\sum\limits_{i=f_{m}-1}^{n}b(i)=\sum\limits_{i=f_{m-2}-1}^{n-f_{m-1}}[b(i)+1]=\sum\limits_{i=f_{m-2}-1}^{n-f_{m-1}}b(i)+n-f_{m}+2.\end{array} |  |

When f m + f m − 5 ≤ n + 1 ≤ 2 ​ f m − 1 − 1 f_{m}+f_{m-5}\leq n+1\leq 2f_{m-1}-1, ∑ i = f m − 1 n b ⁡ ( i) = ∑ i = f m − 1 f m + f m − 5 − 2 b ⁡ ( i) + ∑ i = f m + f m − 5 − 1 n b ⁡ ( i) \sum\limits_{i=f_{m}-1}^{n}b(i)=\sum\limits_{i=f_{m}-1}^{f_{m}+f_{m-5}-2}b(i)+\sum\limits_{i=f_{m}+f_{m-5}-1}^{n}b(i), where

 | { ∑ i = f m − 1 f m + f m − 5 − 2 b ⁡ ( i) = ∑ i = f m − 2 − 1 f m − 2 + f m − 5 − 2 [b ⁡ ( i) + 1] = ∑ b ⁡ ( Γ 2, m − 4, 1) + f m − 5 = 2 ​ m − 5 5 ​ f m − 5 + 2 ​ m − 11 5 ​ f m − 7 + 1; ∑ i = f m + f m − 5 − 1 n b ⁡ ( i) = ∑ i = f m − 2 + f m − 5 − 1 n − f m − 1 b ⁡ ( i) + 1. \left\{\begin{array}[]{rl}\sum\limits_{i=f_{m}-1}^{f_{m}+f_{m-5}-2}b(i)=&\sum\limits_{i=f_{m-2}-1}^{f_{m-2}+f_{m-5}-2}[b(i)+1]=\sum b(\Gamma_{2,m-4,1})+f_{m-5}\\ =&\frac{2m-5}{5}f_{m-5}+\frac{2m-11}{5}f_{m-7}+1;\\ \sum\limits_{i=f_{m}+f_{m-5}-1}^{n}b(i)=&\sum\limits_{i=f_{m-2}+f_{m-5}-1}^{n-f_{m-1}}b(i)+1.\end{array}\right. |  |

Thus ∑ i = f m − 1 n b ⁡ ( i) = ∑ i = f m − 2 + f m − 5 − 1 n − f m − 1 b ⁡ ( i) + 2 ​ m − 5 5 ​ f m − 5 + 2 ​ m − 11 5 ​ f m − 7 + 2 \sum\limits_{i=f_{m}-1}^{n}b(i)=\sum\limits_{i=f_{m-2}+f_{m-5}-1}^{n-f_{m-1}}b(i)+\frac{2m-5}{5}f_{m-5}+\frac{2m-11}{5}f_{m-7}+2. The conclusion holds. ∎

###### Corollary 6.7.

For n ≥ 9 n\geq 9, let m m such that 2 ​ f m − 1 ≤ n + 1 ≤ f m + 1 − 1 2f_{m-1}\leq n+1\leq f_{m+1}-1, then m ≥ 4 m\geq 4 and

 | ∑ i = 2 ​ f m − 1 − 1 n b ⁡ ( i) = { ∑ i = f m − 1 − 1 n − f m − 1 b ⁡ ( i) + n − 2 ​ f m − 1 + 1, n + 1 ≤ f m + f m − 2 − 1; ∑ i = 2 ​ f m − 2 − 1 n − f m − 1 b ⁡ ( i) + n − 2 ​ f m − 1 + 2 ​ m − 8 5 ​ f m − 4 + 2 ​ m − 9 5 ​ f m − 6 + 2, o ​ t ​ h ​ e ​ r ​ w ​ i ​ s ​ e. \sum_{i=2f_{m-1}-1}^{n}b(i)=\begin{cases}\sum\limits_{i=f_{m-1}-1}^{n-f_{m-1}}b(i)+n-2f_{m-1}+1,~~~~~~~~~~~~~~~~~~n+1\leq f_{m}+f_{m-2}-1;\\ \sum\limits_{i=2f_{m-2}-1}^{n-f_{m-1}}b(i)+n-2f_{m-1}+\frac{2m-8}{5}f_{m-4}+\frac{2m-9}{5}f_{m-6}+2,~otherwise.\end{cases} |  |

###### Proof.

By Property 6.1, when 2 ​ f m − 1 ≤ n + 1 ≤ 2 ​ f m − 1 + f m − 4 − 1 = f m + f m − 2 − 1 2f_{m-1}\leq n+1\leq 2f_{m-1}+f_{m-4}-1=f_{m}+f_{m-2}-1,

 | ∑ i = 2 ​ f m − 1 − 1 n b ⁡ ( i) = ∑ i = f m − 1 − 1 n − f m − 1 b ⁡ ( i) + ∑ i = f m − 1 n − f m − 1 1 = ∑ i = f m − 1 − 1 n − f m − 1 b ⁡ ( i) + n − 2 ​ f m − 1 + 1. \begin{array}[]{c}\sum\limits_{i=2f_{m-1}-1}^{n}b(i)=\sum\limits_{i=f_{m-1}-1}^{n-f_{m-1}}b(i)+\sum\limits_{i=f_{m-1}}^{n-f_{m-1}}1=\sum\limits_{i=f_{m-1}-1}^{n-f_{m-1}}b(i)+n-2f_{m-1}+1.\end{array} |  |

When f m + f m − 2 ≤ n + 1 ≤ f m + 1 − 1 f_{m}+f_{m-2}\leq n+1\leq f_{m+1}-1, ∑ i = 2 ​ f m − 1 − 1 n b ⁡ ( i) = ∑ i = 2 ​ f m − 1 − 1 f m + f m − 2 − 2 b ⁡ ( i) + ∑ i = f m + f m − 2 − 1 n b ⁡ ( i) \sum\limits_{i=2f_{m-1}-1}^{n}b(i)=\sum\limits_{i=2f_{m-1}-1}^{f_{m}+f_{m-2}-2}b(i)+\sum\limits_{i=f_{m}+f_{m-2}-1}^{n}b(i), where

 | { ∑ i = 2 ​ f m − 1 − 1 f m + f m − 2 − 2 b ⁡ ( i) = ∑ i = f m − 1 − 1 2 ​ f m − 2 − 2 b ⁡ ( i) + ∑ i = f m − 1 2 ​ f m − 2 − 2 1 = ∑ i = f m − 1 − 1 2 ​ f m − 2 − 2 b ⁡ ( i) + f m − 4 − 1 = ∑ b ⁡ ( Γ 2, m − 3, 1) + f m − 4 − 1 = 2 ​ m − 3 5 ​ f m − 4 + 2 ​ m − 9 5 ​ f m − 6; ∑ i = f m + f m − 2 − 1 n b ⁡ ( i) = ∑ i = 2 ​ f m − 2 − 1 n − f m − 1 [b ⁡ ( i) + 1] = ∑ i = 2 ​ f m − 2 − 1 n − f m − 1 b ⁡ ( i) + n − 2 ​ f m − 1 − f m − 4 + 2. \left\{\begin{array}[]{rl}\sum\limits_{i=2f_{m-1}-1}^{f_{m}+f_{m-2}-2}b(i)=&\sum\limits_{i=f_{m-1}-1}^{2f_{m-2}-2}b(i)+\sum\limits_{i=f_{m-1}}^{2f_{m-2}-2}1=\sum\limits_{i=f_{m-1}-1}^{2f_{m-2}-2}b(i)+f_{m-4}-1\\ =&\sum b(\Gamma_{2,m-3,1})+f_{m-4}-1=\frac{2m-3}{5}f_{m-4}+\frac{2m-9}{5}f_{m-6};\\ \sum\limits_{i=f_{m}+f_{m-2}-1}^{n}b(i)=&\sum\limits_{i=2f_{m-2}-1}^{n-f_{m-1}}[b(i)+1]=\sum\limits_{i=2f_{m-2}-1}^{n-f_{m-1}}b(i)+n-2f_{m-1}-f_{m-4}+2.\end{array}\right. |  |

Thus ∑ i = 2 ​ f m − 1 − 1 n b ⁡ ( i) = ∑ i = 2 ​ f m − 2 − 1 n − f m − 1 b ⁡ ( i) + n − 2 ​ f m − 1 + 2 ​ m − 8 5 ​ f m − 4 + 2 ​ m − 9 5 ​ f m − 6 + 2 \sum\limits_{i=2f_{m-1}-1}^{n}b(i)=\sum\limits_{i=2f_{m-2}-1}^{n-f_{m-1}}b(i)+n-2f_{m-1}+\frac{2m-8}{5}f_{m-4}+\frac{2m-9}{5}f_{m-6}+2. The conclusion holds. ∎

Example. One method to calculate ∑ i = 20 23 b ⁡ ( i) \sum_{i=20}^{23}b(i) is by Property 6.1. Since b ⁡ ( Γ 2, 4, 1) = b ⁡ ( [20, ⋯, 24]) = [2, 2, 2, 1, 2] b(\Gamma_{2,4,1})=b([20,\cdots,24])=[2,2,2,1,2], ∑ i = 20 23 b ⁡ ( i) = 7 \sum_{i=20}^{23}b(i)=7. The other method is using Corollary 6.6 and 6.7:

 | ∑ i = 20 23 b ⁡ ( i) = ∑ i = f 4 + f 1 − 1 23 − f 5 b ⁡ ( i) + 7 5 ​ f 1 + 1 5 ​ f − 1 + 2 = ∑ i = 9 10 b ⁡ ( i) + 5 = 7. \begin{array}[]{c}\sum\limits_{i=20}^{23}b(i)=\sum\limits_{i=f_{4}+f_{1}-1}^{23-f_{5}}b(i)+\frac{7}{5}f_{1}+\frac{1}{5}f_{-1}+2=\sum\limits_{i=9}^{10}b(i)+5=7.\end{array} |  |

###### Algorithm 6.8 (The number of repeated squares, B ⁡ ( n) B(n)).

Step 1. For n ≤ 3 n\leq 3, B ⁡ ( n) = 0 B(n)=0; for n ≤ 4 n\leq 4, find the m m such that f m ≤ n + 1 < f m + 1 f_{m}\leq n+1<f_{m+1}.

Step 2. Compare n n with 2 ​ f m − 1 − 1 2f_{m-1}-1.

(1) If n < 2 ​ f m − 1 − 1 n<2f_{m-1}-1, calculate B ⁡ ( f m − 2) B(f_{m}-2) by Property 6.3; calculate ∑ i = f m − 1 n b ⁡ ( i) \sum_{i=f_{m}-1}^{n}b(i) by Property 6.1 or by Corollary 6.6 and 6.7. Then B ⁡ ( n) = B ⁡ ( f m − 2) + ∑ i = f m − 1 n b ⁡ ( i) B(n)=B(f_{m}-2)+\sum_{i=f_{m}-1}^{n}b(i).

(2) If n ≥ 2 ​ f m − 1 − 1 n\geq 2f_{m-1}-1, calculate B ⁡ ( 2 ​ f m − 1 − 2) B(2f_{m-1}-2) by Property 6.3; calculate ∑ i = 2 ​ f m − 1 − 1 n b ⁡ ( i) \sum_{i=2f_{m-1}-1}^{n}b(i) by Property 6.1 or by Corollary 6.6 and 6.7. Then B ⁡ ( n) = B ⁡ ( 2 ​ f m − 1 − 2) + ∑ i = 2 ​ f m − 1 − 1 n b ⁡ ( i) B(n)=B(2f_{m-1}-2)+\sum_{i=2f_{m-1}-1}^{n}b(i).

###### Remark 6.9.

When m m is large (resp. small), Corollary 6.6 and 6.7 (resp. Property 6.1) is faster.

Example. We calculate B ⁡ ( 23) B(23). Since f 6 = 21 ≤ 23 + 1 < f 7 = 34 f_{6}=21\leq 23+1<f_{7}=34, m = 6 m=6. Moreover 23 < 2 ​ f 5 − 1 23<2f_{5}-1.

By Property 6.3, B ⁡ ( f 6 − 2) = B ⁡ ( 19) = 2 5 ​ f 6 + 6 5 ​ f 4 + 4 = 22 B(f_{6}-2)=B(19)=\frac{2}{5}f_{6}+\frac{6}{5}f_{4}+4=22. By Property 6.1 or by Corollary 6.6 and 6.7, ∑ i = 20 23 b ⁡ ( i) = 7 \sum_{i=20}^{23}b(i)=7. Thus B ⁡ ( 23) = B ⁡ ( 19) + ∑ i = 20 23 b ⁡ ( i) = 22 + 7 = 29 B(23)=B(19)+\sum_{i=20}^{23}b(i)=22+7=29.

## 7 Basic properties of cubes

Let ω \omega be a factor with kernel K m K_{m}, by an analogous argument as Section 3 and by Proposition 4.8 in [11], ω p ​ ω p + 1 ​ ω p + 2 ≺ 𝔽 \omega_{p}\omega_{p+1}\omega_{p+2}\prec\mathbb{F} has only one case: r p ​ ( K m) = r p + 1 ​ ( K m) = r 1 ​ ( K m) = K m ​ K m + 1 r_{p}(K_{m})=r_{p+1}(K_{m})=r_{1}(K_{m})=K_{m}K_{m+1}. In this case, | ω | = f m + 2 |\omega|=f_{m+2}. Moreover 2 ≤ i ≤ f m + 1 2\leq i\leq f_{m+1} and m ≥ 0 m\geq 0,

 | ω ​ ω ​ ω = K m + 1 ​ [i, f m + 1] ​ K m ​ K m + 1 ​ K m ​ K m + 1 ​ K m ​ K m + 1 ​ [1, i − 1] = K m + 2 ​ [i, f m + 2] ​ K m + 3 ¯ ​ K m + 2 ​ [1, i + f m − 1] = K m + 6 ​ [i + f m + 3, i + f m + 5 + f m − 1]. \begin{split}\omega\omega\omega=&K_{m+1}[i,f_{m+1}]K_{m}K_{m+1}K_{m}K_{m+1}K_{m}K_{m+1}[1,i-1]\\ =&K_{m+2}[i,f_{m+2}]\underline{K_{m+3}}K_{m+2}[1,i+f_{m}-1]=K_{m+6}[i+f_{m+3},i+f_{m+5}+f_{m}-1].\end{split} |  |

Since K m + 3 ≺ ω ​ ω ​ ω ≺ K m + 6 ​ [2, f m + 6 − 1] K_{m+3}\prec\omega\omega\omega\prec K_{m+6}[2,f_{m+6}-1], by Property 2.4, K ​ e ​ r ​ ( ω ​ ω ​ ω) = K m + 3 Ker(\omega\omega\omega)=K_{m+3}.

###### Remark 7.1.

By the discussion above, we have: all cubes in 𝔽 \mathbb{F} are of length 3 ​ f m 3f_{m} for some m ≥ 2 m\geq 2, and a cube of each such length occurs. This is Theorem 8 in J.Shallit et al [7].

For m ≥ 3 m\geq 3 and p ≥ 1 p\geq 1, we define a set below:

 | ⟨ K m, p ⟩:= { P ( ω ω ω, p): K e r ( ω ω ω) = K m, | ω | = f m − 1, ω ω ω ≺ 𝔽 }. \langle K_{m},p\rangle:=\{P(\omega\omega\omega,p):Ker(\omega\omega\omega)=K_{m},|\omega|=f_{m-1},\omega\omega\omega\prec\mathbb{F}\}. |  |

Obviously it contains all cubes. By Property 3.2 we have

 | ⟨ K m, p ⟩ = { P ( ω, p): ω = K m − 1 [i, f m − 1] K m K m − 1 [1, i + f m − 3 − 1], 2 ≤ i ≤ f m − 2 } = { P ( K m, p) + f m − 3 + i − 1, 2 ≤ i ≤ f m − 2 } = { p ​ f m + 1 + ⌊ ϕ ​ p ⌋ ​ f m + 2 ​ f m − 1, ⋯, p ​ f m + 1 + ⌊ ϕ ​ p ⌋ ​ f m + f m + 1 − 2 }. \begin{split}\langle K_{m},p\rangle=&\{P(\omega,p):\omega=K_{m-1}[i,f_{m-1}]K_{m}K_{m-1}[1,i+f_{m-3}-1],2\leq i\leq f_{m-2}\}\\ =&\{P(K_{m},p)+f_{m-3}+i-1,2\leq i\leq f_{m-2}\}\\ =&\{pf_{m+1}+\lfloor\phi p\rfloor f_{m}+2f_{m-1},\cdots,pf_{m+1}+\lfloor\phi p\rfloor f_{m}+f_{m+1}-2\}.\end{split} |  |

###### Corollary 7.2.

♯ ⁡ ⟨ K m, p ⟩ = f m − 2 − 1 \sharp\langle K_{m},p\rangle=f_{m-2}-1 for m ≥ 3 m\geq 3, p ≥ 1 p\geq 1.

## 8 The number of distinct cubes in 𝔽 ⁡ [1, n] \mathbb{F}[1,n]

Denote c ( n):= ♯ { ω: ω ω ω ⊳ 𝔽 [1, n], ω ω ω ≺ 𝔽 [1, n − 1] } c(n):=\sharp\{\omega:\omega\omega\omega\triangleright\mathbb{F}[1,n],\omega\omega\omega\not\!\prec\mathbb{F}[1,n-1]\}. Obversely, C ⁡ ( n) = ∑ i = 1 n c ⁡ ( i) C(n)=\sum_{i=1}^{n}c(i).

###### Property 8.1.

⟨ K m, 1 ⟩ = { f m + 1 + 2 ​ f m − 1, ⋯, 2 ​ f m + 1 − 2 } \langle K_{m},1\rangle=\{f_{m+1}+2f_{m-1},\cdots,2f_{m+1}-2\} for m ≥ 3 m\geq 3.

Sets ⟨ K m, 1 ⟩ \langle K_{m},1\rangle are pairwise disjoint, and each set contains some consecutive integers. We get a chain ⟨ K 3, 1 ⟩ = { 14 }, ⟨ K 4, 1 ⟩ = { 23, 24 }, ⋯, ⟨ K m, 1 ⟩, ⋯ \langle K_{3},1\rangle=\{14\},\langle K_{4},1\rangle=\{23,24\},\cdots,\langle K_{m},1\rangle,\cdots. So c ⁡ ( n) = 1 c(n)=1 iff n ∈ ∪ m ≥ 3 ⟨ K m, 1 ⟩ n\in\cup_{m\geq 3}\langle K_{m},1\rangle. Thus

###### Property 8.2.

c ⁡ ( n) = 1 c(n)=1 iff n ∈ ∪ m ≥ 3 { f m + 1 + 2 f m − 1, ⋯, 2 f m + 1 − 2 } n\in\cup_{m\geq 3}\{f_{m+1}+2f_{m-1},\cdots,2f_{m+1}-2\}.

By consider C ⁡ ( 2 ​ f m + 1 − 2) C(2f_{m+1}-2) for m ≥ 3 m\geq 3, we can give a fast algorithm of C ⁡ ( n) C(n) for all n ≥ 1 n\geq 1. Since ∑ i = − 1 m f i = f m + 2 − 1 \sum_{i=-1}^{m}f_{i}=f_{m+2}-1, C ⁡ ( 2 ​ f m + 1 − 2) = ∑ i = 3 m ♯ ⁡ ⟨ K i, 1 ⟩ = ∑ i = 3 m ( f i − 2 − 1) = f m − m − 1 C(2f_{m+1}-2)=\sum_{i=3}^{m}\sharp\langle K_{i},1\rangle=\sum_{i=3}^{m}(f_{i-2}-1)=f_{m}-m-1.

###### Theorem 8.3.

For n < 14 n<14, C ⁡ ( n) = 0 C(n)=0; for n ≥ 14 n\geq 14, let m m s.t. f m + 1 + 2 ​ f m − 1 ≤ n < f m + 2 + 2 ​ f m − 1 f_{m+1}+2f_{m-1}\leq n<f_{m+2}+2f_{m}-1, then m ≥ 3 m\geq 3 and

 | C ⁡ ( n) = { n − f m + 1 − f m − 1 − m + 1, n ≤ 2 ​ f m + 1 − 2; f m − m − 1, o ​ t ​ h ​ e ​ r ​ w ​ i ​ s ​ e. C(n)=\begin{cases}n-f_{m+1}-f_{m-1}-m+1,&n\leq 2f_{m+1}-2;\\ f_{m}-m-1,&otherwise.\end{cases} |  |

###### Proof.

When 2 ​ f m + 1 − 1 ≤ n ≤ f m + 2 + 2 ​ f m − 1 2f_{m+1}-1\leq n\leq f_{m+2}+2f_{m}-1, c ⁡ ( n) = 0 c(n)=0, C ⁡ ( n) = C ⁡ ( 2 ​ f m + 1 − 2) = f m − m − 1 C(n)=C(2f_{m+1}-2)=f_{m}-m-1.

When f m + 1 + 2 ​ f m − 1 ≤ n ≤ 2 ​ f m + 1 − 2 f_{m+1}+2f_{m-1}\leq n\leq 2f_{m+1}-2, c ⁡ ( n) = 1 c(n)=1,

 | C ⁡ ( n) = C ⁡ ( f m + 1 + 2 ​ f m − 1 − 1) + n − f m + 1 − 2 ​ f m − 1 + 1. C(n)=C(f_{m+1}+2f_{m-1}-1)+n-f_{m+1}-2f_{m-1}+1. |  |

Since C ⁡ ( f m + 1 + 2 ​ f m − 1 − 1) = C ⁡ ( 2 ​ f m − 2) = f m − 1 − m C(f_{m+1}+2f_{m-1}-1)=C(2f_{m}-2)=f_{m-1}-m, C ⁡ ( n) = n − f m + 1 − f m − 1 − m + 1. C(n)=n-f_{m+1}-f_{m-1}-m+1. Thus the conclusion holds. ∎

Since 2 ​ f m − 2 − 1 ≤ f m ≤ f m − 1 + 2 ​ f m − 3 − 1 2f_{m-2}-1\leq f_{m}\leq f_{m-1}+2f_{m-3}-1 for m ≥ 6 m\geq 6, we have

###### Theorem 8.4.

C ⁡ ( f m) = 0 C(f_{m})=0 for m ≤ 5 m\leq 5, C ⁡ ( f m) = f m − 3 − m + 2 C(f_{m})=f_{m-3}-m+2 for m ≥ 6 m\geq 6.

## 9 The recursive structure of cubes

In this section, we establish a recursive structure of cubes. Using it, we will count the number of repeated cubes in 𝔽 ⁡ [1, n] \mathbb{F}[1,n] (i.e. D ⁡ ( n) D(n)) in Section 10.

###### Property 9.1.

For m ≥ 5 m\geq 5, min ⁡ ⟨ K m, p ⟩ − 2 = max ⁡ ⟨ K m − 2, P ⁡ ( b, p) + 1 ⟩ \min\langle K_{m},p\rangle-2=\max\langle K_{m-2},P(b,p)+1\rangle.

###### Proof.

Since P ⁡ ( b, p) = 2 ​ p + ⌊ ϕ ​ p ⌋ P(b,p)=2p+\lfloor\phi p\rfloor, ⌊ ϕ ⁡ ( 2 ​ p + ⌊ ϕ ​ p ⌋ + 1) ⌋ = p + ⌊ ϕ ​ p ⌋ \lfloor\phi(2p+\lfloor\phi p\rfloor+1)\rfloor=p+\lfloor\phi p\rfloor, for m ≥ 3 m\geq 3, f m − 1 + f m − 4 = 2 ​ f m − 2 f_{m-1}+f_{m-4}=2f_{m-2},

 | max ⁡ ⟨ K m − 2, P ⁡ ( b, p) + 1 ⟩ + 2 = ( 2 ​ p + ⌊ ϕ ​ p ⌋ + 1) ​ f m − 1 + ⌊ ϕ ⁡ ( 2 ​ p + ⌊ ϕ ​ p ⌋ + 1) ⌋ ​ f m − 2 + f m − 1 = ( 2 ​ p + ⌊ ϕ ​ p ⌋ + 1) ​ f m − 1 + ( p + ⌊ ϕ ​ p ⌋) ​ f m − 2 + f m − 1 = p ​ f m + 1 + ⌊ ϕ ​ p ⌋ ​ f m + 2 ​ f m − 1 = min ⁡ ⟨ K m, p ⟩. \begin{split}&\max\langle K_{m-2},P(b,p)+1\rangle+2=(2p+\lfloor\phi p\rfloor+1)f_{m-1}+\lfloor\phi(2p+\lfloor\phi p\rfloor+1)\rfloor f_{m-2}+f_{m-1}\\ =&(2p+\lfloor\phi p\rfloor+1)f_{m-1}+(p+\lfloor\phi p\rfloor)f_{m-2}+f_{m-1}=pf_{m+1}+\lfloor\phi p\rfloor f_{m}+2f_{m-1}=\min\langle K_{m},p\rangle.\end{split} |  |

This means max ⁡ ⟨ K m − 2, P ⁡ ( b, p) + 1 ⟩ + 2 = min ⁡ ⟨ K m, p ⟩ \max\langle K_{m-2},P(b,p)+1\rangle+2=\min\langle K_{m},p\rangle, so the conclusion holds. ∎

By an analogous argument, we have

###### Property 9.2.

For m ≥ 4 m\geq 4, max ⁡ ⟨ K m, p ⟩ + f m − 4 + 2 = min ⁡ ⟨ K m − 1, P ⁡ ( a, p) + 1 ⟩ \max\langle K_{m},p\rangle+f_{m-4}+2=\min\langle K_{m-1},P(a,p)+1\rangle.

In Property 9.1 and 9.2, we establish the recursive relations for any ⟨ K m, p ⟩ \langle K_{m},p\rangle, m ≥ 3 m\geq 3. Thus we can define the recursive structure over { ⟨ K m, p ⟩ | m ≥ 3, p ≥ 1 } \{\langle K_{m},p\rangle|~m\geq 3,p\geq 1\} denoted by 𝒞 \mathcal{C}. Each ⟨ K m, p ⟩ \langle K_{m},p\rangle is an element in 𝒞 \mathcal{C}. The recursive structure 𝒞 \mathcal{C} is a family of finite trees with roots ⟨ K m, 1 ⟩ \langle K_{m},1\rangle for all m ≥ 3 m\geq 3; and with recursive relations:

 | { τ 3 ​ ⟨ K m, p ⟩ = ⟨ K m − 2, P ⁡ ( b, p) + 1 ⟩ ∪ ⟨ K m − 1, P ⁡ ( a, p) + 1 ⟩ ​ for ​ m ≥ 5; τ 4 ​ ⟨ K 4, p ⟩ = ⟨ K m − 1, P ⁡ ( a, p) + 1 ⟩. \begin{cases}\tau_{3}\langle K_{m},p\rangle=\langle K_{m-2},P(b,p)+1\rangle\cup\langle K_{m-1},P(a,p)+1\rangle\text{ for }m\geq 5;\\ \tau_{4}\langle K_{4},p\rangle=\langle K_{m-1},P(a,p)+1\rangle.\end{cases} |  |

Since max ⁡ ⟨ K m − 2, P ⁡ ( b, p) + 1 ⟩ < min ⁡ ⟨ K m − 1, P ⁡ ( a, p) + 1 ⟩ \max\langle K_{m-2},P(b,p)+1\rangle<\min\langle K_{m-1},P(a,p)+1\rangle, the “ ∪ \cup ” is a disjoint union.

###### Property 9.3.

Each ⟨ K m, p ⟩ \langle K_{m},p\rangle belongs to the recursive structure 𝒞 \mathcal{C}, for m ≥ 3 m\geq 3 and p ≥ 1 p\geq 1.

###### Proof.

Each element ⟨ K m, 1 ⟩ \langle K_{m},1\rangle is root of a finite tree in 𝒞 \mathcal{C}. For p ≥ 1 p\geq 1,

 | { ⟨ K m, P ⁡ ( a, p) + 1 ⟩ ∈ τ 3 ​ ⟨ K m + 1, p ⟩ ​ ( m ≥ 4) ​ and ​ ⟨ K 3, P ⁡ ( a, p) + 1 ⟩ ∈ τ 4 ​ ⟨ K 4, p ⟩; ⟨ K m, P ⁡ ( b, p) + 1 ⟩ ∈ τ 3 ​ ⟨ K m + 2, p ⟩ ​ ( m ≥ 3). \begin{cases}\langle K_{m},P(a,p)+1\rangle\in\tau_{3}\langle K_{m+1},p\rangle~(m\geq 4)\text{ and }\langle K_{3},P(a,p)+1\rangle\in\tau_{4}\langle K_{4},p\rangle;\\ \langle K_{m},P(b,p)+1\rangle\in\tau_{3}\langle K_{m+2},p\rangle~(m\geq 3).\end{cases} |  |

Since ℕ = { 1 } ∪ { P ⁡ ( a, p) + 1 } ∪ { P ⁡ ( b, p) + 1 } \mathbb{N}=\{1\}\cup\{P(a,p)+1\}\cup\{P(b,p)+1\}, the recursive structure 𝒞 \mathcal{C} contains all ⟨ K m, p ⟩ \langle K_{m},p\rangle. ∎

On the other hand, by the recursive relations τ 3 \tau_{3} and τ 4 \tau_{4}, each element ⟨ K m, p ⟩ \langle K_{m},p\rangle has a unique position in 𝒞 \mathcal{C}. Fig.4 show the finite tree in the recursive structure 𝒞 \mathcal{C} with root ⟨ K 6, 1 ⟩ \langle K_{6},1\rangle.

Fig.4: The finite tree in the recursive structure 𝒞 \mathcal{C} with root ⟨ K 6, 1 ⟩ \langle K_{6},1\rangle.

###### Lemma 9.4.

For m ≥ 1 m\geq 1, (1) P ⁡ ( a, f m − 1) = f m + 1 − 2 P(a,f_{m}-1)=f_{m+1}-2, ⌊ ϕ ⁡ ( f m − 1) ⌋ = f m − 1 − 1 \lfloor\phi(f_{m}-1)\rfloor=f_{m-1}-1.

(2) ⌊ ϕ ​ f m ⌋ = f m − 1 \lfloor\phi f_{m}\rfloor=f_{m-1} if m m is odd; ⌊ ϕ ​ f m ⌋ = f m − 1 − 1 \lfloor\phi f_{m}\rfloor=f_{m-1}-1 if m m is even. (3) P ⁡ ( b, f 2 ​ m) = f 2 ​ m + 2 − 1 P(b,f_{2m})=f_{2m+2}-1.

###### Proof.

Denote by | ω | a |\omega|_{a} (resp. | ω | b |\omega|_{b}) the number of letter a a (resp. b b) occurring in ω \omega.

(1) Since | F m + 1 | a = f m |F_{m+1}|_{a}=f_{m}, a ​ b ​ a ⊳ F 2 ​ m aba\triangleright F_{2m} and a ​ a ​ b ⊳ F 2 ​ m + 1 aab\triangleright F_{2m+1}, we have P ⁡ ( a, f m − 1) = f m + 1 − 2 P(a,f_{m}-1)=f_{m+1}-2. On the other hand, by Corollary 3.3, P ⁡ ( a, f m − 1) = f m − 1 + ⌊ ϕ ⁡ ( f m − 1) ⌋ P(a,f_{m}-1)=f_{m}-1+\lfloor\phi(f_{m}-1)\rfloor. Comparing the two expressions of P ⁡ ( a, f m − 1) P(a,f_{m}-1), we have ⌊ ϕ ⁡ ( f m − 1) ⌋ = f m − 1 − 1 \lfloor\phi(f_{m}-1)\rfloor=f_{m-1}-1 for m ≥ 1 m\geq 1.

(2) By Corollary 3.3, P ⁡ ( a, f m) = f m + ⌊ ϕ ​ f m ⌋ P(a,f_{m})=f_{m}+\lfloor\phi f_{m}\rfloor. By the analogous argument in (1), we have: when m m is odd, P ⁡ ( a, f m) = f m + 1 P(a,f_{m})=f_{m+1}, then P ⁡ ( a, f m) = f m + 1 = f m + ⌊ ϕ ​ f m ⌋ ⇒ ⌊ ϕ ​ f m ⌋ = f m − 1 P(a,f_{m})=f_{m+1}=f_{m}+\lfloor\phi f_{m}\rfloor\Rightarrow\lfloor\phi f_{m}\rfloor=f_{m-1}; when m m is even, P ⁡ ( a, f m) = f m + 1 − 1 P(a,f_{m})=f_{m+1}-1, then P ⁡ ( a, f m) = f m + 1 − 1 = f m + ⌊ ϕ ​ f m ⌋ ⇒ ⌊ ϕ ​ f m ⌋ = f m − 1 − 1 P(a,f_{m})=f_{m+1}-1=f_{m}+\lfloor\phi f_{m}\rfloor\Rightarrow\lfloor\phi f_{m}\rfloor=f_{m-1}-1.

(3) Since | F m | b = f m − 2 |F_{m}|_{b}=f_{m-2}, a ​ b ​ a ⊳ F 2 ​ m aba\triangleright F_{2m}, we have P ⁡ ( b, f 2 ​ m) = f 2 ​ m + 2 − 1 P(b,f_{2m})=f_{2m+2}-1 for m ≥ 1 m\geq 1. ∎

###### Lemma 9.5.

f m ​ f k + f m − 1 ​ f k − 1 = f m + k + 1 f_{m}f_{k}+f_{m-1}f_{k-1}=f_{m+k+1} for m, k ≥ − 1 m,k\geq-1.

###### Proof.

Since f m ​ f k + f m − 1 ​ f k − 1 = f m ​ ( f k − 1 + f k − 2) + f m − 1 ​ f k − 1 = f m ​ f k − 2 + ( f m + f m − 1) ​ f k − 1 f_{m}f_{k}+f_{m-1}f_{k-1}=f_{m}(f_{k-1}+f_{k-2})+f_{m-1}f_{k-1}=f_{m}f_{k-2}+(f_{m}+f_{m-1})f_{k-1}, using it repeatedly, f m ​ f k + f m − 1 ​ f k − 1 = f m ​ f k − 2 + f m + 1 ​ f k − 1 = ⋯ = f m + k − 1 ​ f − 1 + f m + k ​ f 0 = f m + k + 1 f_{m}f_{k}+f_{m-1}f_{k-1}=f_{m}f_{k-2}+f_{m+1}f_{k-1}=\cdots=f_{m+k-1}f_{-1}+f_{m+k}f_{0}=f_{m+k+1}. ∎

For m ≥ 3 m\geq 3, we define the vectors Γ m:= [f m + 2 − 1, ⋯, f m + 3 − 2] \Gamma_{m}:=[f_{m+2}-1,\cdots,f_{m+3}-2], then

###### Property 9.6.

The finite tree with root ⟨ K m, 1 ⟩ \langle K_{m},1\rangle belongs to Γ m \Gamma_{m} for m ≥ 3 m\geq 3.

###### Proof.

(1) Since P ⁡ ( a, f m − 1) = f m + 1 − 2 P(a,f_{m}-1)=f_{m+1}-2, the maximal of the recursive structure from ⟨ K m, 1 ⟩ \langle K_{m},1\rangle is

 | max ⁡ { max ⁡ ⟨ K m, 1 ⟩, max ⁡ ⟨ K m − 1, f 2 − 1 ⟩, max ⁡ ⟨ K m − 2, f 3 − 1 ⟩, ⋯, max ⁡ ⟨ K 3, f m − 2 − 1 ⟩ } \max\{\max\langle K_{m},1\rangle,\max\langle K_{m-1},f_{2}-1\rangle,\max\langle K_{m-2},f_{3}-1\rangle,\cdots,\max\langle K_{3},f_{m-2}-1\rangle\} |  |

By Property 9.2, max ⁡ ⟨ K m, p ⟩ < min ⁡ ⟨ K m − 1, P ⁡ ( a, p) + 1 ⟩ \max\langle K_{m},p\rangle<\min\langle K_{m-1},P(a,p)+1\rangle, so max ⁡ ⟨ K m − i, f i + 1 − 1 ⟩ \max\langle K_{m-i},f_{i+1}-1\rangle is strictly increasing for 0 ≤ i ≤ m − 3 0\leq i\leq m-3. Thus the maximal integer in the tree is max ⁡ ⟨ K 3, f m − 2 − 1 ⟩ \max\langle K_{3},f_{m-2}-1\rangle.

 | max ⁡ ⟨ K 3, f m − 2 − 1 ⟩ = ( f m − 2 − 1) ​ f 4 + ⌊ ϕ ⁡ ( f m − 2 − 1) ⌋ ​ f 3 + f 4 − 2 = ( f m − 2 − 1) ​ f 4 + ( f m − 3 − 1) ​ f 3 + 6 = f m − 2 ​ f 4 + f m − 3 ​ f 3 − 7 = f m + 3 − 7 < max ⁡ Γ m. \begin{split}&\max\langle K_{3},f_{m-2}-1\rangle=(f_{m-2}-1)f_{4}+\lfloor\phi(f_{m-2}-1)\rfloor f_{3}+f_{4}-2\\ =&(f_{m-2}-1)f_{4}+(f_{m-3}-1)f_{3}+6=f_{m-2}f_{4}+f_{m-3}f_{3}-7=f_{m+3}-7<\max\Gamma_{m}.\end{split} |  |

(2) Similarly, since P ⁡ ( b, f 2 ​ m) = f 2 ​ m + 2 − 1 P(b,f_{2m})=f_{2m+2}-1, min ⁡ ⟨ K m − 2 ​ i, f 2 ​ i ⟩ \min\langle K_{m-2i},f_{2i}\rangle is strictly decreasing for 0 ≤ i ≤ [m − 4 2] 0\leq i\leq[\frac{m-4}{2}]. So the minimal integer in the tree is

 | min ⁡ { min ⁡ ⟨ K m, 1 ⟩, min ⁡ ⟨ K m − 2, f 2 ⟩, min ⁡ ⟨ K m − 4, f 4 ⟩, ⋯ } = { min ⁡ ⟨ K 4, f m − 4 ⟩ if m is even; min ⁡ ⟨ K 3, f m − 3 ⟩ if m is odd. \min\{\min\langle K_{m},1\rangle,\min\langle K_{m-2},f_{2}\rangle,\min\langle K_{m-4},f_{4}\rangle,\cdots\}=\begin{cases}\min\langle K_{4},f_{m-4}\rangle&\text{if $m$ is even;}\\ \min\langle K_{3},f_{m-3}\rangle&\text{if $m$ is odd.}\end{cases} |  |

When m m is even, min ⁡ ⟨ K 4, f m − 4 ⟩ = f m − 4 ​ f 5 + ⌊ ϕ ​ f m − 4 ⌋ ​ f 4 + 2 ​ f 3 \min\langle K_{4},f_{m-4}\rangle=f_{m-4}f_{5}+\lfloor\phi f_{m-4}\rfloor f_{4}+2f_{3}, ⌊ ϕ ​ f m − 4 ⌋ = f m − 5 − 1 \lfloor\phi f_{m-4}\rfloor=f_{m-5}-1, so

 | min ⁡ ⟨ K 4, f m − 4 ⟩ = f m − 4 ​ f 5 + ( f m − 5 − 1) ​ f 4 + 2 ​ f 3 = f m + 2 + 2 > min ⁡ Γ m. \min\langle K_{4},f_{m-4}\rangle=f_{m-4}f_{5}+(f_{m-5}-1)f_{4}+2f_{3}=f_{m+2}+2>\min\Gamma_{m}. |  |

When m m is odd, min ⁡ ⟨ K 3, f m − 3 ⟩ = f m − 3 ​ f 4 + ⌊ ϕ ​ f m − 3 ⌋ ​ f 3 + 2 ​ f 2 \min\langle K_{3},f_{m-3}\rangle=f_{m-3}f_{4}+\lfloor\phi f_{m-3}\rfloor f_{3}+2f_{2}, ⌊ ϕ ​ f m − 3 ⌋ = f m − 4 − 1 \lfloor\phi f_{m-3}\rfloor=f_{m-4}-1, so

 | min ⁡ ⟨ K 3, f m − 3 ⟩ = f m − 3 ​ f 4 + ( f m − 4 − 1) ​ f 3 + 2 ​ f 2 = f m + 2 + 1 > min ⁡ Γ m. \min\langle K_{3},f_{m-3}\rangle=f_{m-3}f_{4}+(f_{m-4}-1)f_{3}+2f_{2}=f_{m+2}+1>\min\Gamma_{m}. |  |

In each case, the minimal integer in the tree is larger than min ⁡ Γ m \min\Gamma_{m}, so the conclusion holds. ∎

By Property 9.6 and the definition of Γ m \Gamma_{m}, the finite trees in recursive structure 𝒞 \mathcal{C} with different roots ⟨ K m, 1 ⟩ \langle K_{m},1\rangle are disjoint.

## 10 The number of repeated cubes in 𝔽 ⁡ [1, n] \mathbb{F}[1,n]

Denote d ⁡ ( n):= ♯ ⁡ { ( ω, p): ω p ​ ω p + 1 ​ ω p + 2 ⊳ 𝔽 ⁡ [1, n] } d(n):=\sharp\{(\omega,p):\omega_{p}\omega_{p+1}\omega_{p+2}\triangleright\mathbb{F}[1,n]\}, the number of cubes ending at position n n. Obversely, D ⁡ ( n) = ∑ i = 1 n d ⁡ ( i) D(n)=\sum_{i=1}^{n}d(i). By the definition of ⟨ K m, p ⟩ \langle K_{m},p\rangle, d ⁡ ( n) d(n) is equal to the number of integer n n occurs in the recursive structure 𝒞 \mathcal{C}. Thus we can calculate d ⁡ ( n) d(n) by the property below.

###### Property 10.1.

For m ≥ 3 m\geq 3,

 | d ⁡ ( [f m + 4 − 1, ⋯, f m + 5 − 2]) = d ⁡ ( [f m + 2 − 1, ⋯, f m + 3 − 2, f m + 3 − 1, ⋯, f m + 4 − 2]) + [0, ⋯, 0 ⏟ f m − 1 + 1, 1, ⋯, 1 ⏟ f m − 1, 0, ⋯, 0 ⏟ f m + 2]. \begin{split}&d([f_{m+4}-1,\cdots,f_{m+5}-2])\\ =&d([f_{m+2}-1,\cdots,f_{m+3}-2,f_{m+3}-1,\cdots,f_{m+4}-2])+[\underbrace{0,\cdots,0}_{f_{m-1}+1},\underbrace{1,\cdots,1}_{f_{m}-1},\underbrace{0,\cdots,0}_{f_{m+2}}].\end{split} |  |

The first few values of d ⁡ ( n) d(n) are d ⁡ ( [f 5 − 1, ⋯, f 6 − 2]) = [d ⁡ ( 12), ⋯, d ⁡ ( 19)] = [0, 0, 1, 0, 0, 0, 0, 0] d([f_{5}-1,\cdots,f_{6}-2])=[d(12),\cdots,d(19)]=[0,0,1,0,0,0,0,0],

d ⁡ ( [f 6 − 1, ⋯, f 7 − 2]) = [d ⁡ ( 20), ⋯, d ⁡ ( 32)] = [0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0] d([f_{6}-1,\cdots,f_{7}-2])=[d(20),\cdots,d(32)]=[0,0,0,1,1,0,0,1,0,0,0,0,0],

d ⁡ ( [f 7 − 1, ⋯, f 8 − 2]) = [d ⁡ ( 33), ⋯, d ⁡ ( 53)] = [0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0] d([f_{7}-1,\cdots,f_{8}-2])=[d(33),\cdots,d(53)]=[0,0,1,0,1,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,0].

By Property 10.1, ∑ d ⁡ ( Γ m + 2) = ∑ d ⁡ ( Γ m) + ∑ d ⁡ ( Γ m + 1) + f m − 2 − 1 \sum d(\Gamma_{m+2})=\sum d(\Gamma_{m})+\sum d(\Gamma_{m+1})+f_{m-2}-1. By induction, we have

###### Lemma 10.2.

∑ f m + 2 − 1 f m + 3 − 2 d ⁡ ( n) = m − 5 5 ​ f m + m + 2 5 ​ f m − 2 + 1 \sum\limits_{f_{m+2}-1}^{f_{m+3}-2}d(n)=\frac{m-5}{5}f_{m}+\frac{m+2}{5}f_{m-2}+1 for m ≥ 3 m\geq 3.

By the definition of D ⁡ ( n) D(n), D ⁡ ( f m + 1 − 2) = D ⁡ ( f m − 2) + ∑ f m − 1 f m + 1 − 2 d ⁡ ( n) D(f_{m+1}-2)=D(f_{m}-2)+\sum_{f_{m}-1}^{f_{m+1}-2}d(n). By induction, we have

###### Property 10.3.

D ⁡ ( f m − 2) = m − 11 5 ​ f m − 1 + m + 1 5 ​ f m − 3 + m + 1 D(f_{m}-2)=\frac{m-11}{5}f_{m-1}+\frac{m+1}{5}f_{m-3}+m+1 for m ≥ 6 m\geq 6.

By Property 10.1, we get d ⁡ ( f m − 1) = d ⁡ ( f m) = 0 d(f_{m}-1)=d(f_{m})=0 easily by induction, thus D ⁡ ( f m) = D ⁡ ( f m − 2) D(f_{m})=D(f_{m}-2).

###### Theorem 10.4.

D ⁡ ( f m) = m − 11 5 ​ f m − 1 + m + 1 5 ​ f m − 3 + m + 1 D(f_{m})=\frac{m-11}{5}f_{m-1}+\frac{m+1}{5}f_{m-3}+m+1 for m ≥ 6 m\geq 6.

###### Remark 10.5.

Theorem 59 in [7] shows the number of cube occurrences in F m F_{m} as

 | D ⁡ ( f m) = [d 1 ​ ( m + 2) + d 2] ​ α m + 2 + [d 3 ​ ( m + 2) + d 4] ​ β m + 2 + m + 1. D(f_{m})=[d_{1}(m+2)+d_{2}]\alpha^{m+2}+[d_{3}(m+2)+d_{4}]\beta^{m+2}+m+1. |  |

where α = 1 + 5 2 \alpha=\frac{1+\sqrt{5}}{2}, β = 1 − 5 2 \beta=\frac{1-\sqrt{5}}{2}, d 1 = 3 − 5 10 d_{1}=\frac{3-\sqrt{5}}{10}, d 2 = 17 50 ​ 5 − 3 2 d_{2}=\frac{17}{50}\sqrt{5}-\frac{3}{2}, d 3 = 3 + 5 10 d_{3}=\frac{3+\sqrt{5}}{10}, d 4 = − 17 50 ​ 5 − 3 2 d_{4}=-\frac{17}{50}\sqrt{5}-\frac{3}{2}. Since

 | f m = α m + 2 − β m + 2 α − β, α β = − 1, 1 α = 5 − 1 2, 1 β = − 1 − 5 2, ( 1 α) 3 = 5 − 2, ( 1 β) 3 = − 5 − 2, \begin{array}[]{c}f_{m}=\frac{\alpha^{m+2}-\beta^{m+2}}{\alpha-\beta},~\alpha\beta=-1,~\frac{1}{\alpha}=\frac{\sqrt{5}-1}{2},~\frac{1}{\beta}=\frac{-1-\sqrt{5}}{2},~(\frac{1}{\alpha})^{3}=\sqrt{5}-2,~(\frac{1}{\beta})^{3}=-\sqrt{5}-2,\end{array} |  |

we can prove the two expressions are same. By our expression in Theorem 10.4,

 | D ⁡ ( f m) − m − 1 = m − 11 5 × α m + 1 − β m + 1 α − β + m + 1 5 × α m − 1 − β m − 1 α − β = m − 11 5 ​ 5 × ( 5 − 1 2 ​ α m + 2 + 1 + 5 2 ​ β m + 2) + m + 1 5 ​ 5 × ( ( 5 − 2) ​ α m + 2 + ( 5 + 2) ​ β m + 2) = [m − 11 5 ​ 5 × 5 − 1 2 + m + 1 5 ​ 5 ​ ( 5 − 2)] ​ α m + 2 + [m − 11 5 ​ 5 × 1 + 5 2 + m + 1 5 ​ 5 ​ ( 5 + 2)] ​ β m + 2 = [3 − 5 10 ​ m + 7 ​ 5 − 45 50] ​ α m + 2 + [3 + 5 10 ​ m + − 7 ​ 5 − 45 50] ​ β m + 2. \begin{array}[]{rl}&D(f_{m})-m-1=\frac{m-11}{5}\times\frac{\alpha^{m+1}-\beta^{m+1}}{\alpha-\beta}+\frac{m+1}{5}\times\frac{\alpha^{m-1}-\beta^{m-1}}{\alpha-\beta}\\ =&\frac{m-11}{5\sqrt{5}}\times\left(\frac{\sqrt{5}-1}{2}\alpha^{m+2}+\frac{1+\sqrt{5}}{2}\beta^{m+2}\right)+\frac{m+1}{5\sqrt{5}}\times\left((\sqrt{5}-2)\alpha^{m+2}+(\sqrt{5}+2)\beta^{m+2}\right)\\ =&[\frac{m-11}{5\sqrt{5}}\times\frac{\sqrt{5}-1}{2}+\frac{m+1}{5\sqrt{5}}(\sqrt{5}-2)]\alpha^{m+2}+[\frac{m-11}{5\sqrt{5}}\times\frac{1+\sqrt{5}}{2}+\frac{m+1}{5\sqrt{5}}(\sqrt{5}+2)]\beta^{m+2}\\ =&[\frac{3-\sqrt{5}}{10}m+\frac{7\sqrt{5}-45}{50}]\alpha^{m+2}+[\frac{3+\sqrt{5}}{10}m+\frac{-7\sqrt{5}-45}{50}]\beta^{m+2}.\end{array} |  |

By J.shallit’s expression in [7],

 | D ⁡ ( f m) − m − 1 = [3 − 5 10 ​ m + 3 − 5 5 + 17 50 ​ 5 − 3 2] ​ α m + 2 + [3 + 5 10 ​ m + 3 + 5 5 − 17 50 ​ 5 − 3 2] ​ β m + 2. \begin{array}[]{c}D(f_{m})-m-1=[\frac{3-\sqrt{5}}{10}m+\frac{3-\sqrt{5}}{5}+\frac{17}{50}\sqrt{5}-\frac{3}{2}]\alpha^{m+2}+[\frac{3+\sqrt{5}}{10}m+\frac{3+\sqrt{5}}{5}-\frac{17}{50}\sqrt{5}-\frac{3}{2}]\beta^{m+2}.\end{array} |  |

Comparing the coefficients of m ​ α m + 2 m\alpha^{m+2}, α m + 2 \alpha^{m+2}, m ​ β m + 2 m\beta^{m+2} and β m + 2 \beta^{m+2}, we have the two expressions are same.

For any n ≥ 12 n\geq 12, let m m such that f m ≤ n + 1 < f m + 1 f_{m}\leq n+1<f_{m+1}. Since we already determine the expression of D ⁡ ( f m − 2) D(f_{m}-2), in order to give a fast algorithm of D ⁡ ( n) D(n), we only need to calculate ∑ i = f m − 1 n d ⁡ ( i) \sum_{i=f_{m}-1}^{n}d(i). One method is calculating d ⁡ ( n) d(n) by Property 10.1, the other method is using the corollaries as below.

###### Corollary 10.6.

For n ≥ 12 n\geq 12, let m m such that f m ≤ n + 1 < f m + 1 f_{m}\leq n+1<f_{m+1}, then m ≥ 5 m\geq 5 and

 | ∑ i = f m − 1 n d ⁡ ( i) = { ∑ i = f m − 2 − 1 n − f m − 1 d ⁡ ( i), f m ≤ n + 1 ≤ f m + f m − 5; ∑ i = f m − 2 + 1 n − f m − 1 d ⁡ ( i) + n − f m − f m − 5 + 1, f m + f m − 5 + 1 ≤ n + 1 ≤ f m + f m − 3 − 1; ∑ i = f m − 1 − 1 n − f m − 1 d ⁡ ( i) + m − 4 5 ​ f m − 4 + m − 2 5 ​ f m − 6, f m + f m − 3 ≤ n + 1 < f m + 1. \sum_{i=f_{m}-1}^{n}d(i)=\begin{cases}\sum\limits_{i=f_{m-2}-1}^{n-f_{m-1}}d(i),&f_{m}\leq n+1\leq f_{m}+f_{m-5};\\ \sum\limits_{i=f_{m-2}+1}^{n-f_{m-1}}d(i)+n-f_{m}-f_{m-5}+1,&f_{m}+f_{m-5}+1\leq n+1\leq f_{m}+f_{m-3}-1;\\ \sum\limits_{i=f_{m-1}-1}^{n-f_{m-1}}d(i)+\frac{m-4}{5}f_{m-4}+\frac{m-2}{5}f_{m-6},&f_{m}+f_{m-3}\leq n+1<f_{m+1}.\end{cases} |  |

###### Proof.

By Property 10.1, when f m ≤ n + 1 ≤ f m + f m − 5 f_{m}\leq n+1\leq f_{m}+f_{m-5}, ∑ i = f m − 1 n d ⁡ ( i) = ∑ i = f m − 2 − 1 n − f m − 1 d ⁡ ( i) \sum\limits_{i=f_{m}-1}^{n}d(i)=\sum\limits_{i=f_{m-2}-1}^{n-f_{m-1}}d(i).

When f m + f m − 5 + 1 ≤ n + 1 ≤ f m + f m − 3 − 1 f_{m}+f_{m-5}+1\leq n+1\leq f_{m}+f_{m-3}-1,

 | ∑ i = f m − 1 n d ⁡ ( i) = ∑ i = f m − 1 f m + f m − 5 − 1 d ⁡ ( i) + ∑ i = f m + f m − 5 n d ⁡ ( i) = ∑ i = f m − 2 + 1 n − f m − 1 d ⁡ ( i) + ∑ i = f m − 2 + f m − 5 n − f m − 1 1 = ∑ i = f m − 2 + 1 n − f m − 1 d ⁡ ( i) + n − f m − f m − 5 + 1. \begin{array}[]{rl}&\sum\limits_{i=f_{m}-1}^{n}d(i)=\sum\limits_{i=f_{m}-1}^{f_{m}+f_{m-5}-1}d(i)+\sum\limits_{i=f_{m}+f_{m-5}}^{n}d(i)=\sum\limits_{i=f_{m-2}+1}^{n-f_{m-1}}d(i)+\sum\limits_{i=f_{m-2}+f_{m-5}}^{n-f_{m-1}}1\\ =&\sum\limits_{i=f_{m-2}+1}^{n-f_{m-1}}d(i)+n-f_{m}-f_{m-5}+1.\end{array} |  |

When f m + f m − 3 ≤ n + 1 < f m + 1 f_{m}+f_{m-3}\leq n+1<f_{m+1},

 | ∑ i = f m − 1 n d ⁡ ( i) = ∑ i = f m − 1 f m + f m − 5 − 1 d ⁡ ( i) + ∑ i = f m + f m − 5 f m + f m − 3 − 2 d ⁡ ( i) + ∑ i = f m + f m − 3 − 1 n d ⁡ ( i) = ∑ i = f m − 2 − 1 f m − 1 − 2 d ⁡ ( i) + f m − 4 − 1 + ∑ i = f m − 1 − 1 n − f m − 1 d ⁡ ( i) = ∑ i = f m − 1 − 1 n − f m − 1 d ⁡ ( i) + m − 4 5 ​ f m − 4 + m − 2 5 ​ f m − 6. \begin{array}[]{rl}&\sum\limits_{i=f_{m}-1}^{n}d(i)=\sum\limits_{i=f_{m}-1}^{f_{m}+f_{m-5}-1}d(i)+\sum\limits_{i=f_{m}+f_{m-5}}^{f_{m}+f_{m-3}-2}d(i)+\sum\limits_{i=f_{m}+f_{m-3}-1}^{n}d(i)\\ =&\sum\limits_{i=f_{m-2}-1}^{f_{m-1}-2}d(i)+f_{m-4}-1+\sum\limits_{i=f_{m-1}-1}^{n-f_{m-1}}d(i)=\sum\limits_{i=f_{m-1}-1}^{n-f_{m-1}}d(i)+\frac{m-4}{5}f_{m-4}+\frac{m-2}{5}f_{m-6}.\end{array} |  |

So the conclusion holds. ∎

Example. Since [d ⁡ ( 33), ⋯, d ⁡ ( 53)] = [0, 0, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0] [d(33),\cdots,d(53)]=[0,0,1,0,1,1,1,1,0,0,0,1,1,0,0,1,0,0,0,0,0], using Property 10.1, we have ∑ i = 33 48 d ⁡ ( i) = 8 \sum_{i=33}^{48}d(i)=8. The other method is using Corollary 10.6. Since f 7 + f 4 = 42 ≤ n + 1 = 49 < f 8 = 55 f_{7}+f_{4}=42\leq n+1=49<f_{8}=55, ∑ i = 33 48 d ⁡ ( i) = ∑ i = f 6 − 1 48 − f 6 d ⁡ ( i) + 3 5 ​ f 3 + 5 5 ​ f 1 = ∑ i = 20 27 d ⁡ ( i) + 5 = ∑ i = 12 14 d ⁡ ( i) + 7 = 8. \sum_{i=33}^{48}d(i)=\sum_{i=f_{6}-1}^{48-f_{6}}d(i)+\frac{3}{5}f_{3}+\frac{5}{5}f_{1}=\sum_{i=20}^{27}d(i)+5=\sum_{i=12}^{14}d(i)+7=8.

###### Algorithm 10.7 (The number of repeated cubes occurrences, D ⁡ ( n) D(n)).

Step 1. For n ≤ 11 n\leq 11, D ⁡ ( n) = 0 D(n)=0; for n ≤ 12 n\leq 12, find the m m such that f m ≤ n + 1 < f m + 1 f_{m}\leq n+1<f_{m+1}.

Step 2. Calculate D ⁡ ( f m − 2) D(f_{m}-2) by Property 10.3.

Step 3. Calculate ∑ i = f m − 1 n d ⁡ ( i) \sum_{i=f_{m}-1}^{n}d(i) by Property 10.1 or by Corollary 10.6.

Step 4. D ⁡ ( n) = D ⁡ ( f m − 2) + ∑ i = f m − 1 n d ⁡ ( i) D(n)=D(f_{m}-2)+\sum_{i=f_{m}-1}^{n}d(i).

Example. We calculate D ⁡ ( 48) D(48). Since f 7 = 34 ≤ 48 + 1 < f 8 = 55 f_{7}=34\leq 48+1<f_{8}=55, m = 7 m=7.

By Property 10.3, D ⁡ ( 32) = D ⁡ ( f 7 − 2) = − 4 5 ​ f 6 + 8 5 ​ f 4 + 7 + 1 = 4 D(32)=D(f_{7}-2)=\frac{-4}{5}f_{6}+\frac{8}{5}f_{4}+7+1=4.

By Property 10.1 or by Corollary 10.6, ∑ i = 33 48 d ⁡ ( i) = 8 \sum_{i=33}^{48}d(i)=8. Thus D ⁡ ( 48) = D ⁡ ( 32) + ∑ i = 33 48 d ⁡ ( i) = 12 D(48)=D(32)+\sum_{i=33}^{48}d(i)=12.

Acknowledgments

The research is supported by the Grant NSF No.11431007, No.11271223 and No.11371210.

## References

- [1] J.M.Allouche, J.Shallit. Automatic sequences: Theory, applications, generalizations. Cambridge University Press, Cambridge, 2003.
- [2] J.Berstel. Recent results in Sturmian words, in J.Dassow, A.Salomaa (Eds.), Developments in Language Theory, World Scientific, Singapore. (1966) 13-24.
- [3] J.Berstel. Mot de Fibonacci, S e ´ \acute{e} minaire d’informatique th e ´ \acute{e} rique, L.I.T.P., Paris, 1980/1981, 57-78.
- [4] W.-F.Chuan, H.-L.Ho. Locating factors of the infinite Fibonacci word, Theoretical Computer Science. 349 (2005) 429-442.
- [5] W.-T.Cao, Z.-Y.Wen. Some properties of the factors of Sturmian sequences, Theoretical Computer Science. 304 (2003) 365-385.
- [6] F.Durand. A characterization of substitutive sequences using return words, Discrete Math. 179 (1998) 89-101.
- [7] C.-F.Du, H.Mousavi, L.Schaeffer, J.Shallit. Decision Algorithms for Fibonacci-Automatic Words, with Applications to Pattern Avoidance. Eprint Arxiv, 2014.
- [8] A.S.Fraenkel, J.Simpson. The exact number of squares in Fibonacci words, Theoretical Computer Science. 218 (1999) 95-106.
- [9] A.S.Fraenkel, J.Simpson. Corrigendum to “The exact number of squares in Fibonacci words”, Theoretical Computer Science. 547 (2014) 122.
- [10] A.Glen. On Sturmian and Episturmian Words, and Related Topics, PhD thesis, The University of Adelaide, Australia. 2006.
- [11] Y.-K.Huang, Z.-Y.Wen. The sequence of return words of the Fibonacci sequence, Theoretical Computer Science. 593 (2015) 106-116.
- [12] Y.-K.Huang, Z.-Y.Wen. Kernel words and gap sequence of the Tribonacci sequence, Acta Mathematica Scientia (Series B). 36.1 (2016) 173-194.
- [13] Y.-K.Huang, Z.-Y.Wen. The structure of palindromes in the Fibonacci sequence. arXiv: 1601.04391.
- [14] M.Lothaire. Combinatorics on words, in: Encyclopedia of Mathematics and its applications, Vol.17, Addison-Wesley, Reading, MA, 1983.
- [15] M.Lothaire. Algebraic combinatorics on words, Cambridge Univ. Press, Cambridge, 2002.
- [16] P.S e ´ ​ e ´ \acute{e}\acute{e} bold. Propri e ´ \acute{e} t e ´ \acute{e} s combinatoires des mots infinis engendr e ´ \acute{e} s par certains morphismes (Th e `\grave{e} se de 3 e 3^{e} cycle). PhD thesis, Universit e ´ \acute{e} P. et M. Curie, Institut de Programmation, Paris, 1985.
- [17] B.Tan, Z.-X.Wen. Invertible substitutions and Sturmian sequences. European Journal of Combinatorics, 24.8 (2003) 983-1002.
- [18] Z.-X.Wen, Z.-Y.Wen. Some properties of the singular words of the Fibonacci word, European J. Combin. 15 (1994) 587-598.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/1603.04210
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/1603.04211
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1603.04211
[7]: https://arxiv.org/pdf/1603.04211
[8]: /html/1603.04212
