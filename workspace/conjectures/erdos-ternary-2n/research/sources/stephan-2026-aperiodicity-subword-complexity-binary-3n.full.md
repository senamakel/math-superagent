<!-- source: https://arxiv.org/html/2607.14774 | converted from HTML -->

Aperiodicity and subword complexityin the binary expansion of powers of three

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC Zero][2]

arXiv:2607.14774v2 [math.CO] 03 Aug 2026

# Aperiodicity and subword complexity
in the binary expansion of powers of three Thanks: Institute for Globally Distributed Open Research and Education (IGDORE)

Ralf Stephan

Date: August 11, 2026

###### Abstract.

We prove two results on the fine structure of the binary digits of 3 m 3^{m}. First, for every fixed period p p, the number of positions at which the binary expansion of 3 m 3^{m} breaks p p -periodicity grows in order like log ⁡ m / log ⁡ log ​ m \log m/\log\log m; equivalently, no window of the expansion deeper than a fixed power of log ⁡ m \log m is p p -periodic. Second, the finite binary word formed by the low-order digits of 3 m 3^{m} meets the Morse–Hedlund floor: its complexity function satisfies p 3 m ​ ( n) ≥ n + 1 p_{3^{m}}(n)\geq n+1 for every length n n, once m m is large enough.

## 1. Introduction

Write a positive integer N N in binary, N = ∑ i ≥ 0 bit i ​ ( N) ​ 2 i N=\sum_{i\geq 0}\mathrm{bit}_{i}(N)\,2^{i} with bit i ​ ( N) ∈ { 0, 1 } \mathrm{bit}_{i}(N)\in\{0,1\}, and let

 | M ⁡ ( N):= ⌊ log 2 ⁡ N ⌋, s 2 ​ ( N):= ∑ i ≥ 0 bit i ​ ( N), M(N):=\lfloor\log_{2}N\rfloor,\qquad s_{2}(N):=\sum_{i\geq 0}\mathrm{bit}_{i}(N), |  |

so that N N has M ⁡ ( N) + 1 M(N)+1 binary digits and s 2 ​ ( N) s_{2}(N) is its number of 1 1 -bits. This note concerns the arrangement of the binary digits of N = 3 m N=3^{m}. Throughout, “ log \log ” is the natural logarithm.

We use two further statistics of the digit string. A *digit change*of N N is an index i < M ⁡ ( N) i<M(N) with bit i ​ ( N) ≠ bit i + 1 ​ ( N) \mathrm{bit}_{i}(N)\neq\mathrm{bit}_{i+1}(N); writing N N as a concatenation of maximal runs of equal digits (its *blocks*), the number of digit changes is one less than the number of blocks. For a fixed period p ≥ 1 p\geq 1, a *period- p p break*of N N is an index i < M ⁡ ( N) i<M(N) with bit i ​ ( N) ≠ bit i + p ​ ( N) \mathrm{bit}_{i}(N)\neq\mathrm{bit}_{i+p}(N).

###### Definition 1.1.

For N ≥ 1 N\geq 1, let

 | T ⁡ ( N):= #⁡ { i < M ⁡ ( N): bit i ​ ( N) ≠ bit i + 1 ​ ( N) }, \displaystyle T(N):=\#\{\,i<M(N):\mathrm{bit}_{i}(N)\neq\mathrm{bit}_{i+1}(N)\,\}, |  |

 | B p ​ ( N):= #⁡ { i < M ⁡ ( N): bit i ​ ( N) ≠ bit i + p ​ ( N) }. \displaystyle B_{p}(N):=\#\{\,i<M(N):\mathrm{bit}_{i}(N)\neq\mathrm{bit}_{i+p}(N)\,\}. |  |

Thus T ⁡ ( N) T(N) is the number of digit changes of N N (its number of blocks is T ⁡ ( N) + 1 T(N)+1), and B p ​ ( N) B_{p}(N) is its number of period- p p breaks; note B 1 = T B_{1}=T.

Finally, for a word w = ( w 0, w 1, …) w=(w_{0},w_{1},\dots) over a finite alphabet, the *subword complexity*(or *factor complexity*) p w ​ ( n) p_{w}(n) is the number of distinct factors of length n n occurring in w w. We read the low bits of 3 m 3^{m} as the finite word w = ( bit 0 ​ ( 3 m), …, bit M − 1 ​ ( 3 m)) w=(\mathrm{bit}_{0}(3^{m}),\dots,\mathrm{bit}_{M-1}(3^{m})), M = M ⁡ ( 3 m) M=M(3^{m}), and write p 3 m ​ ( n) p_{3^{m}}(n) for its complexity: the number of distinct length- n n factors at the positions 0, 1, …, M − n 0,1,\dots,M-n.

### 1.1. Known results

The starting point is a theorem of Stewart on integers with few digits in two bases. In the notation of [Ste80], s 2 ​ ( N) s_{2}(N) is the number of nonzero binary digits, and Stewart’s Theorem 2, applied to the recurrence u n = 3 n u_{n}=3^{n} with base 2 2, gives the following.

###### Theorem 1.2 (Stewart [Ste80]).

There is a constant C > 0 C>0 such that

 | s 2 ​ ( 3 m) ≥ log ⁡ m log ⁡ log ⁡ m + C − 1 for every ​ m ≥ 2. s_{2}(3^{m})\ \geq\ \frac{\log m}{\log\log m+C}-1\qquad\text{for every }m\geq 2. |  |

In particular s 2 ​ ( 3 m) → ∞ s_{2}(3^{m})\to\infty: no power of three eventually has sparse binary digits.

Stewart’s proof rests on Baker’s theory of linear forms in logarithms; in the present work the corresponding input is the following effective theorem of Baker and Wüstholz [BW93], stated in Section 2. For an embedding φ: K → ℂ \varphi\colon K\to\mathbb{C} of a number field K K of degree d d, write h ′ ​ ( α) h^{\prime}(\alpha) for the modified height of α ∈ K \alpha\in K and C ⁡ ( n, d) C(n,d) for the Baker–Wüstholz constant; the theorem asserts that a nonzero linear form Λ = ∑ i b i ​ log ⁡ φ ⁡ ( α i) \Lambda=\sum_{i}b_{i}\log\varphi(\alpha_{i}) with integer coefficients bounded by B ≥ 2 B\geq 2 obeys log | Λ | ≥ − C ( n, d) max ( log B, 1 d) ∏ i h ′ ( α i) \log|\Lambda|\geq-C(n,d)\max(\log B,\tfrac{1}{d})\prod_{i}h^{\prime}(\alpha_{i}) (Theorem 2.1).

Counting the 1 1 -bits says nothing about their placement, and it is natural to count instead the blocks of 3 m 3^{m}. That the number of blocks tends to infinity is a theorem of Blecksmith, Filaseta and Nicol [BFN93], who introduced this quantity; an effective, and faster, lower bound follows from work of Bugeaud and Kaneko. Since 3 m 3^{m} is an integral S S -unit with S = { 3 } S=\{3\}, their Corollary 1.5 and the block variant recorded in their Remark 4.4 apply.

###### Theorem 1.3 (Blecksmith–Filaseta–Nicol; Bugeaud–Kaneko).

The number of binary blocks of 3 m 3^{m} tends to infinity, and grows in order at least like log ⁡ m / log ⁡ log ​ m \log m/\log\log m; equivalently

 | T ⁡ ( 3 m) ≥ log ⁡ m log ⁡ log ⁡ m + C − 1 T(3^{m})\ \geq\ \frac{\log m}{\log\log m+C}-1 |  |

for a constant C > 0 C>0 and all m ≥ 2 m\geq 2.

Here the order log ⁡ m / log ⁡ log ​ m \log m/\log\log m comes from log ⁡ log ⁡ ( 3 m) = log ⁡ m + O ⁡ ( 1) \log\log(3^{m})=\log m+O(1) in [BK17, Cor. 1.5, Rem. 4.4]. On the opposite, sparse side, the powers of three with few nonzero bits are known exactly in the relevant range. The case s 2 ≤ 2 s_{2}\leq 2 is elementary; the case s 2 = 3 s_{2}=3 is a theorem of Dimitrov and Howe.

###### Theorem 1.4 (Dimitrov–Howe [DH23]).

The equation 3 m = 2 a + 2 b + 1 3^{m}=2^{a}+2^{b}+1 with 1 ≤ b < a 1\leq b<a has the unique solution ( m, b, a) = ( 4, 4, 6) (m,b,a)=(4,4,6). More generally [DH23, Thm. 1.1], the powers of three with at most 22 22 nonzero binary digits are exactly 3 0, …, 3 25 3^{0},\dots,3^{25}.

###### Theorem 1.5 (sparse powers of three).

s 2 ​ ( 3 m) ≤ 2 s_{2}(3^{m})\leq 2 if and only if m ≤ 2 m\leq 2, and s 2 ​ ( 3 m) = 3 s_{2}(3^{m})=3 if and only if m = 4 m=4. Explicitly 3 0 = 1 2 3^{0}=1_{2}, 3 1 = 11 2 3^{1}=11_{2}, 3 2 = 1001 2 3^{2}=1001_{2} have s 2 ≤ 2 s_{2}\leq 2, and 3 4 = 1010001 2 3^{4}=1010001_{2} is the unique power of three with s 2 = 3 s_{2}=3.

The first assertion of Theorem 1.5 is elementary (peeling the least significant bit reduces it to ruling out 3 m = 2 a + 1 3^{m}=2^{a}+1 for m ≥ 3 m\geq 3); the second is the s 2 = 3 s_{2}=3 reading of Theorem 1.4. The smallest powers of three breaking the sparse bound are 3 3 = 11011 2 3^{3}=11011_{2} ( s 2 = 4 s_{2}=4) and 3 4 = 1010001 2 3^{4}=1010001_{2} ( s 2 = 3 s_{2}=3).

The combinatorial input to our second result is a finite form of the Morse–Hedlund theorem [MH38]: an infinite word of subword complexity p w ​ ( n) ≤ n p_{w}(n)\leq n for some n n is eventually periodic. We use a quantitative finite version, stated and proved in Section 4 (Lemma 4.1), in the spirit of the special-factor analysis of Carpi and de Luca [CdL00].

### 1.2. Results of this paper

Theorems 1.2 and 1.3 forbid long constant runs. We strengthen this in two directions, neither of which, to our knowledge, has been treated for the integer 3 m 3^{m}; the existing quantitative results on digit changes and on subword complexity in this circle concern algebraic irrationals, whose expansions are infinite, rather than the finite word of a single power.

Our first result forbids long *periodic*runs, of any fixed period. It is proved in Section 3.

###### Theorem A.

For every fixed period p ≥ 1 p\geq 1 there is a constant C p > 0 C_{p}>0 such that

 | B p ​ ( 3 m) ≥ log ⁡ m log ⁡ log ⁡ m + C p − 2 for every ​ m ≥ 2; B_{p}(3^{m})\ \geq\ \frac{\log m}{\log\log m+C_{p}}-2\qquad\text{for every }m\geq 2; |  |

in particular B p ​ ( 3 m) → ∞ B_{p}(3^{m})\to\infty. Equivalently, no window of the binary expansion of 3 m 3^{m} deeper than a fixed power of log ⁡ m \log m can be p p -periodic.

The case p = 1 p=1 recovers Theorem 1.3. The engine is a new estimate for periodic windows (Lemma 2.7), a four-logarithm companion of the run estimates behind the classical bounds. The constant is explicit: one may take C 1 < 39.31 C_{1}<39.31, and C p < 40 + 3 ​ log ⁡ ( p + 1) C_{p}<40+3\log(p+1) for every p ≥ 1 p\geq 1 (Remark 3.3).

Our second result is a Morse–Hedlund floor for the finite binary word of a single 3 m 3^{m}. It is proved in Section 4.

###### Theorem B.

For every length n ≥ 1 n\geq 1, the low-order binary word of 3 m 3^{m} meets the Morse–Hedlund floor,

 | p 3 m ​ ( n) ≥ n + 1, p_{3^{m}}(n)\ \geq\ n+1, |  |

for all sufficiently large m m.

The value n + 1 n+1 is the aperiodicity threshold, not the maximum available to a binary word; Remark 4.3 states precisely what the theorem does and does not assert.

The threshold in m m is effective: p 3 m ​ ( n) ≥ n + 1 p_{3^{m}}(n)\geq n+1 once m m exceeds the point where the linear growth of M ⁡ ( 3 m) ≥ m M(3^{m})\geq m overtakes a bound of order n 2 ​ log ⁡ m n^{2}\log m coming from Theorem A ’s engine. Numerically it suffices to take m ≥ 2 × 10 18 ​ n 2 ​ ( 1 + log ⁡ n) m\geq 2\times 10^{18}n^{2}(1+\log n), and m ≥ 1.33 × 10 18 m\geq 1.33\times 10^{18} when n = 1 n=1 (Remark 4.4).

Neither theorem hides an ineffective constant. The single quantitative input is the Baker–Wüstholz constant C ⁡ ( 4, 1) C(4,1), which [BW93] specifies by a closed formula; Remark 2.2 evaluates it and traces it through to the constants above. We do not claim these numbers are of the right order of magnitude—they are not—only that the results are effective rather than qualitative.

Both theorems have been formally verified in the Lean 4 proof assistant; Appendix A records the Lean name and status of every statement appearing in this paper.

## 2. Linear forms in logarithms and the periodic-run estimate

The engine common to the classical bounds and to Theorems A and B is Stewart’s: a long run, or more generally a long periodic stretch, in the binary expansion of 3 m 3^{m} produces a small nonzero linear form in the logarithms of 2 2, 3 3 and an auxiliary integer, which the Baker–Wüstholz theorem forbids from being too small.

###### Theorem 2.1 (Baker–Wüstholz [BW93]).

Let α 1, …, α n \alpha_{1},\dots,\alpha_{n} be nonzero elements of a number field K K of degree d d, and let b 1, …, b n ∈ ℤ b_{1},\dots,b_{n}\in\mathbb{Z} satisfy | b i | ≤ B |b_{i}|\leq B with B ≥ 2 B\geq 2. If Λ:= ∑ i b i ​ log ⁡ φ ⁡ ( α i) ≠ 0 \Lambda:=\sum_{i}b_{i}\log\varphi(\alpha_{i})\neq 0 ( ( principal branch)), then

 | log | Λ | ≥ − C ( n, d) ⋅ max ( log B, 1 d) ⋅ ∏ i h ′ ( α i). \log|\Lambda|\ \geq\ -\,C(n,d)\cdot\max\!\Bigl(\log B,\tfrac{1}{d}\Bigr)\cdot\prod_{i}h^{\prime}(\alpha_{i}). |  |

We use Theorem 2.1 only over K = ℚ K=\mathbb{Q} ( d = 1 d=1), where each α i \alpha_{i} is a positive rational and the modified height of a positive integer a a is h ′ ​ ( a) = max ⁡ ( log ⁡ a, 1) h^{\prime}(a)=\max(\log a,1); thus h ′ ​ ( 3) = log ⁡ 3 h^{\prime}(3)=\log 3, while h ′ ​ ( 2) = 1 h^{\prime}(2)=1 because the floor 1 / d = 1 1/d=1 is active for a = 2 a=2 (note log ⁡ 2 < 1 \log 2<1). Set M:= M ⁡ ( 3 m) = ⌊ log 2 ⁡ 3 m ⌋ M:=M(3^{m})=\lfloor\log_{2}3^{m}\rfloor.

###### Remark 2.2 (All constants are explicit).

Theorem 2.1 is effective, and the constant C ⁡ ( n, d) C(n,d) occurring in it is not an unspecified quantity: [BW93] gives

 | C ⁡ ( n, d) = 18 ​ ( n + 1)! ​ n n + 1 ​ ( 32 ​ d) n + 2 ​ log ⁡ ( 2 ​ n ​ d). C(n,d)\ =\ 18\,(n+1)!\;n^{\,n+1}\,(32d)^{\,n+2}\,\log(2nd). |  |

Every application in this paper is at ( n, d) = ( 4, 1) (n,d)=(4,1), so the only constant entering the argument is the single number

 | C ⁡ ( 4, 1) = 18 ⋅ 5! ⋅ 4 5 ⋅ 32 6 ⋅ log ⁡ 8 = 6480 ⋅ 2 40 ​ log ⁡ 2 < 4.94 × 10 15. C(4,1)\ =\ 18\cdot 5!\cdot 4^{5}\cdot 32^{6}\cdot\log 8\ =\ 6480\cdot 2^{40}\log 2\ <\ 4.94\times 10^{15}. |  |

Everything downstream is an elementary expression in this number: the coefficient κ p \kappa_{p} and the constant C p C_{p} of Theorem A (Remark 3.3) and the threshold m 0 ​ ( n) m_{0}(n) of Theorem B (Remark 4.4). We record the resulting numerical values as they arise; no estimate below is merely qualitative, and no step of either proof appeals to a compactness, limit or contradiction argument that would destroy effectivity. The formalization uses the same definition: BakerWustholz.C n d is the displayed formula, and the Lean proofs of both theorems instantiate it at ( 4, 1) (4,1).

The constants are, of course, far from optimal: C ⁡ ( 4, 1) C(4,1) is a general-purpose transcendence constant, and no attempt is made here to sharpen it. What matters for the statements is that they are computable, so that the qualifiers “for a constant C p C_{p} ” and “for all sufficiently large m m ” can be replaced by numbers.

The estimates behind Theorems 1.2 and 1.3 bound how far below the top of the expansion a run of *constant*bits can begin: a run of zeros (resp. ones) in positions [x, y) [x,y) forces ( M − x) ​ log ​ 2 ≤ C ⁡ ( 3, 1) ​ log ​ 3 ​ ( M + 1 − y) ​ max ⁡ ( log ⁡ 2 ​ m, 1) (M-x)\log 2\leq C(3,1)\log 3\,(M+1-y)\max(\log 2m,1), via a three-term linear form. 1 1 1 We use the descriptive names *run estimate*for these lemmas and *period- p p run estimate*for Lemma 2.7; the formalization calls them “gap principles”. Each is an instance of Theorem 2.1. The result of this paper needs the analogous estimate for *periodic*runs, which is new and uses a four-term form.

The combinatorial half of that estimate is the following remainder identity, which converts a periodic window into an exact equation between integers. It is where the auxiliary integer 2 p − 1 2^{p}-1 —the fourth logarithm—originates.

###### Lemma 2.3 (Periodic remainder identity).

Let N, x, y, p ∈ ℕ N,x,y,p\in\mathbb{N} with p ≥ 1 p\geq 1, and suppose bit i ​ ( N) = bit i + p ​ ( N) \mathrm{bit}_{i}(N)=\mathrm{bit}_{i+p}(N) for all i i with x ≤ i x\leq i and i + p < y i+p<y. Put c:= ⌊ N / 2 x ⌋ mod 2 p c:=\lfloor N/2^{x}\rfloor\bmod 2^{p}. Then for every t ≥ 0 t\geq 0 with x + t ​ p ≤ y x+tp\leq y,

 | ( 2 p − 1) ​ ( N mod 2 x + t ​ p) = ( 2 p − 1) ​ ( N mod 2 x) + c ⁡ ( 2 x + t ​ p − 2 x). (2^{p}-1)\bigl(N\bmod 2^{x+tp}\bigr)\ =\ (2^{p}-1)\bigl(N\bmod 2^{x}\bigr)+c\,\bigl(2^{x+tp}-2^{x}\bigr). |  |

###### Proof.

We first record that the p p -bit block read off at each level of the window is the same, namely c c: for every j j with x + j ​ p + p ≤ y x+jp+p\leq y,

(2.1) |  | ⌊ N / 2 x + j ​ p ⌋ mod 2 p = c. \lfloor N/2^{x+jp}\rfloor\bmod 2^{p}\ =\ c. |  |

Indeed, the block at level x + j ​ p x+jp consists of the bits

 | bit x + j ​ p ​ ( N), …, bit x + j ​ p + p − 1 ​ ( N), \mathrm{bit}_{x+jp}(N),\dots,\mathrm{bit}_{x+jp+p-1}(N), |  |

and each of these equals its counterpart p p places higher—all the indices involved satisfy the hypothesis, because x + j ​ p + p ≤ y x+jp+p\leq y. So the block at level x + j ​ p x+jp equals the block at level x + j ​ p + p x+jp+p, and induction on j j from the base case j = 0 j=0, where the block is c c by definition, gives ( 2.1).

Next, peeling one p p -bit block off a remainder is the identity

 | N mod 2 a + p = ( N mod 2 a) + ( ⌊ N / 2 a ⌋ mod 2 p) ​ 2 a, N\bmod 2^{a+p}=\bigl(N\bmod 2^{a}\bigr)+\bigl(\lfloor N/2^{a}\rfloor\bmod 2^{p}\bigr)2^{a}, |  |

valid for every a a. Taking a = x + t ​ p a=x+tp and inserting ( 2.1),

(2.2) |  | N mod 2 x + ( t + 1) ​ p = ( N mod 2 x + t ​ p) + c ​ 2 x + t ​ p. N\bmod 2^{x+(t+1)p}\ =\ \bigl(N\bmod 2^{x+tp}\bigr)+c\,2^{x+tp}. |  |

Now induct on t t. For t = 0 t=0 both sides of the assertion equal ( 2 p − 1) ​ ( N mod 2 x) (2^{p}-1)(N\bmod 2^{x}). Assuming it for t t, multiply ( 2.2) by 2 p − 1 2^{p}-1; the new term is

 | ( 2 p − 1) ​ c ​ 2 x + t ​ p = c ⁡ ( 2 x + ( t + 1) ​ p − 2 x + t ​ p), (2^{p}-1)c\,2^{x+tp}=c\bigl(2^{x+(t+1)p}-2^{x+tp}\bigr), |  |

and it combines with the inductive hypothesis by the telescoping

 | ( 2 x + t ​ p − 2 x) + ( 2 x + ( t + 1) ​ p − 2 x + t ​ p) = 2 x + ( t + 1) ​ p − 2 x. \bigl(2^{x+tp}-2^{x}\bigr)+\bigl(2^{x+(t+1)p}-2^{x+tp}\bigr)=2^{x+(t+1)p}-2^{x}. |  |

∎

###### Remark 2.4.

Unrolled, Lemma 2.3 says

 | N mod 2 x + t ​ p = ( N mod 2 x) + c ​ 2 x ​ ( 2 t ​ p − 1) / ( 2 p − 1): N\bmod 2^{x+tp}=\bigl(N\bmod 2^{x}\bigr)+c\,2^{x}\,(2^{tp}-1)/(2^{p}-1): |  |

the window contributes t t copies of the pattern c c, a geometric series. The point of stating it in the cleared form is that multiplying by 2 p − 1 2^{p}-1 removes the denominator, so every quantity in sight stays a rational integer; the price is the extra factor 2 p − 1 2^{p}-1, which is exactly the fourth logarithm in Lemma 2.7 below and the source of its C ⁡ ( 4, 1) C(4,1).

The arithmetic half is the following nondegeneracy statement, which is what keeps the linear form of Lemma 2.7 away from zero. We state it in base b b, both because nothing is gained by specializing and because the general form is what Section 5 needs.

###### Lemma 2.5 (Nondegeneracy of the remainder).

Let b ≥ 2 b\geq 2, p ≥ 1 p\geq 1 and x ≥ 0 x\geq 0 be integers, let N ≥ 1 N\geq 1, and put

 | G:= b p − 1, A 2:= N mod b x, c:= ⌊ N / b x ⌋ mod b p, E:= G ​ A 2 − c ​ b x. \begin{gathered}G:=b^{p}-1,\qquad A_{2}:=N\bmod b^{x},\qquad c:=\lfloor N/b^{x}\rfloor\bmod b^{p},\\[2.0pt] E:=G\,A_{2}-c\,b^{x}.\end{gathered} |  |

If ℓ \ell is a prime with ℓ | b \ell\mid b and ℓ ∤ N \ell\nmid N, then

 | E ≡ − N ( mod ℓ); E\ \equiv\ -N\ \pmod{\ell}; |  |

in particular E ≠ 0 E\neq 0.

###### Proof.

The two cases give the same congruence. If x ≥ 1 x\geq 1 then ℓ | b x \ell\mid b^{x}, so c ​ b x ≡ 0 c\,b^{x}\equiv 0 and A 2 = N mod b x ≡ N A_{2}=N\bmod b^{x}\equiv N, while G = b p − 1 ≡ − 1 G=b^{p}-1\equiv-1; hence E ≡ − N E\equiv-N. If x = 0 x=0 then A 2 = N mod 1 = 0 A_{2}=N\bmod 1=0 and b x = 1 b^{x}=1, so E = − c = − ( N mod b p) E=-c=-(N\bmod b^{p}), and ℓ | b p \ell\mid b^{p} gives N mod b p ≡ N N\bmod b^{p}\equiv N; hence again E ≡ − N E\equiv-N. As ℓ ∤ N \ell\nmid N, we get E ≢ 0 ( mod ℓ) E\not\equiv 0\pmod{\ell}, so E ≠ 0 E\neq 0. ∎

###### Remark 2.6 (Degeneracy, and the role of x ≥ 1 x\geq 1).

Two comments on the hypotheses, the second of which we have not pursued.

*(i) What the hypothesis excludes is the trailing-digit degeneracy.*If every prime of b b divides N N, then E E genuinely can vanish. For b = 2 b=2 and N = 6 m = 2 m ​ 3 m N=6^{m}=2^{m}3^{m}, any x x and p p with x + p ≤ m x+p\leq m give A 2 = 0 A_{2}=0 and c = 0 c=0, hence E = 0 E=0: at m = 10 m=10, x = 3 x=3, p = 4 p=4 one has E = 0 E=0 on the nose, and the identity ( 2.5) below degenerates to 0 = 0 0=0. Nothing is lost, because the deep windows of such an N N really are periodic—they are constant—and no linear form could say otherwise. This is the mechanism behind the ( a, b) = ( 6, 2) (a,b)=(6,2) discussion of Section 5.

*(ii) The condition x ≥ 1 x\geq 1 of Lemma 2.7 is not needed for nondegeneracy.*Lemma 2.5 covers x = 0 x=0, where the two contributions to E E simply exchange roles: A 2 A_{2} vanishes and all of E E is carried by − c = − ( N mod b p) -c=-(N\bmod b^{p}). Since x ≥ 1 x\geq 1 enters the proof of Lemma 2.7 nowhere else—see Remark 2.8 —the lemma should hold with 1 ≤ x 1\leq x weakened to 0 ≤ x 0\leq x, and Theorem A would then carry the offset − 1 -1 in place of − 2 -2, no window being sacrificed, matching Theorems 1.2 and 1.3 exactly. We have not made that change. The formalized gap_principle retains the hypothesis 1 ≤ x 1\leq x —it is used there at exactly two points, both inside the parity computation—and the verified form of Theorem A is the one stated above, with − 2 -2. The improvement is recorded here as an observation, not claimed as a theorem of this paper.

###### Lemma 2.7 (Period- p p run estimate).

Let m ≥ 1 m\geq 1, p ≥ 1 p\geq 1, 1 ≤ x < y ≤ M 1\leq x<y\leq M with 2 ​ p ≤ y − x 2p\leq y-x, and suppose bit i ​ ( 3 m) = bit i + p ​ ( 3 m) \mathrm{bit}_{i}(3^{m})=\mathrm{bit}_{i+p}(3^{m}) for all i i with x ≤ i x\leq i and i + p < y i+p<y. Then

 | ( M − x) ​ log ​ 2 ≤ C ⁡ ( 4, 1) ​ p ​ log ​ 3 ​ ( M + 2 ​ p − y) ​ max ⁡ ( log ⁡ ( 2 ​ m + p), 1) + ( p + 1) ​ log ​ 2. (M-x)\log 2\ \leq\ C(4,1)\,p\,\log 3\,(M+2p-y)\,\max\bigl(\log(2m+p),1\bigr)+(p+1)\log 2. |  |

###### Proof.

Write N:= 3 m N:=3^{m}, so that 2 M ≤ N < 2 M + 1 2^{M}\leq N<2^{M+1}, and put G:= 2 p − 1 G:=2^{p}-1.

*Step 1: trimming the window to whole periods.*Let t:= ⌊ ( y − x) / p ⌋ t:=\lfloor(y-x)/p\rfloor and y ′:= x + t ​ p y^{\prime}:=x+tp. Then y ′ ≤ y y^{\prime}\leq y and

(2.3) |  | y − y ′ = ( y − x) mod p ≤ p − 1. y-y^{\prime}\ =\ (y-x)\bmod p\ \leq\ p-1. |  |

The hypothesis 2 ​ p ≤ y − x 2p\leq y-x gives t ≥ 2 t\geq 2, whence x < x + 2 ​ p ≤ y ′ ≤ y ≤ M x<x+2p\leq y^{\prime}\leq y\leq M; in particular

(2.4) |  | x + 2 ≤ x + 2 ​ p ≤ M. x+2\ \leq\ x+2p\ \leq\ M. |  |

The trimmed window [x, y ′) [x,y^{\prime}) is still p p -periodic and now consists of exactly t ≥ 2 t\geq 2 full periods.

*Step 2: the repeated pattern.*Put A 2:= N mod 2 x A_{2}:=N\bmod 2^{x}, the digits strictly below the window, and c:= ⌊ N / 2 x ⌋ mod 2 p c:=\lfloor N/2^{x}\rfloor\bmod 2^{p}, the pattern that repeats. Lemma 2.3, applied with this t t, gives

 | G ⁡ ( N mod 2 y ′) = G ​ A 2 + c ⁡ ( 2 y ′ − 2 x). G\,\bigl(N\bmod 2^{y^{\prime}}\bigr)\ =\ G\,A_{2}+c\,\bigl(2^{y^{\prime}}-2^{x}\bigr). |  |

*Step 3: an exact integer identity.*Put A 1 ′′:= ⌊ N / 2 y ′ ⌋ A_{1}^{\prime\prime}:=\lfloor N/2^{y^{\prime}}\rfloor, the digits at or above y ′ y^{\prime}, and A 1 ′:= G ​ A 1 ′′ + c A_{1}^{\prime}:=G\,A_{1}^{\prime\prime}+c. Division with remainder, N = A 1 ′′ ​ 2 y ′ + ( N mod 2 y ′) N=A_{1}^{\prime\prime}2^{y^{\prime}}+\bigl(N\bmod 2^{y^{\prime}}\bigr), combined with Step 2, gives G ​ N = G ​ A 1 ′′ ​ 2 y ′ + G ​ A 2 + c ​ 2 y ′ − c ​ 2 x GN=GA_{1}^{\prime\prime}2^{y^{\prime}}+GA_{2}+c\,2^{y^{\prime}}-c\,2^{x}, that is,

(2.5) |  | ( 2 p − 1) ​ 3 m = A 1 ′ ​ 2 y ′ + E, E:= G ​ A 2 − c ​ 2 x. (2^{p}-1)\,3^{m}\ =\ A_{1}^{\prime}\,2^{y^{\prime}}+E,\qquad E:=G\,A_{2}-c\,2^{x}. |  |

*Step 4: parity nondegeneracy, E ≠ 0 E\neq 0.*This is Lemma 2.5 with b = 2 b=2 and ℓ = 2 \ell=2, legitimate because 3 m 3^{m} is odd: it gives E ≡ − 3 m ≡ 1 ( mod 2) E\equiv-3^{m}\equiv 1\pmod{2}, so E E is odd and in particular nonzero. Concretely, G = 2 p − 1 G=2^{p}-1 is odd and A 2 = 3 m mod 2 x A_{2}=3^{m}\bmod 2^{x} is odd because x ≥ 1 x\geq 1, so G ​ A 2 GA_{2} is odd, while c ​ 2 x c\,2^{x} is even for the same reason. It is this parity that replaces, in the periodic setting, the appeal to the irrationality of log ⁡ 2 / log ⁡ 3 \log 2/\log 3 making the corresponding form nonzero for constant runs. The hypothesis x ≥ 1 x\geq 1 is used nowhere else in this proof, and Lemma 2.5 does not require it; see Remark 2.6 (ii).

*Step 5: the size of A 1 ′ A_{1}^{\prime}.*From 2 M ≤ N 2^{M}\leq N we get A 1 ′′ ≥ 2 M − y ′ A_{1}^{\prime\prime}\geq 2^{M-y^{\prime}}, hence A 1 ′ ≥ G ​ 2 M − y ′ ≥ 1 A_{1}^{\prime}\geq G\,2^{M-y^{\prime}}\geq 1. From N < 2 M + 1 N<2^{M+1} we get A 1 ′′ < 2 M + 1 − y ′ A_{1}^{\prime\prime}<2^{M+1-y^{\prime}}, so, using G < 2 p G<2^{p} and c < 2 p c<2^{p},

(2.6) |  | A 1 ′ < 2 p ​ A 1 ′′ + 2 p = 2 p ​ ( A 1 ′′ + 1) ≤ 2 M + 1 + p − y ′. A_{1}^{\prime}\ <\ 2^{p}A_{1}^{\prime\prime}+2^{p}\ =\ 2^{p}\bigl(A_{1}^{\prime\prime}+1\bigr)\ \leq\ 2^{\,M+1+p-y^{\prime}}. |  |

*Step 6: the ratio lies within 1 2 \tfrac{1}{2} of 1 1.*Set R:= G ​ 3 m / ( A 1 ′ ​ 2 y ′) > 0 R:=G\,3^{m}/\bigl(A_{1}^{\prime}2^{y^{\prime}}\bigr)>0, so that R − 1 = E / ( A 1 ′ ​ 2 y ′) R-1=E/\bigl(A_{1}^{\prime}2^{y^{\prime}}\bigr) by ( 2.5). For the numerator, 0 ≤ G ​ A 2 < 2 p ​ 2 x 0\leq GA_{2}<2^{p}2^{x} and 0 ≤ c ​ 2 x < 2 p ​ 2 x 0\leq c\,2^{x}<2^{p}2^{x}, so | E | ≤ 2 x + p |E|\leq 2^{x+p}. For the denominator, Step 5 gives A 1 ′ ​ 2 y ′ ≥ G ​ 2 M − y ′ ​ 2 y ′ = G ​ 2 M ≥ 2 p − 1 ​ 2 M A_{1}^{\prime}2^{y^{\prime}}\geq G\,2^{M-y^{\prime}}2^{y^{\prime}}=G\,2^{M}\geq 2^{p-1}2^{M}. Hence

(2.7) |  | | R − 1 | ≤ 2 x + p 2 p − 1 ​ 2 M = 2 x + 1 − M ≤ 1 2, |R-1|\ \leq\ \frac{2^{x+p}}{2^{p-1}\,2^{M}}\ =\ 2^{\,x+1-M}\ \leq\ \tfrac{1}{2}, |  |

the last inequality by ( 2.4).

*Step 7: the four-term form and its upper bound.*By Step 4 we have E ≠ 0 E\neq 0, so R ≠ 1 R\neq 1, and therefore

 | Λ:= log ⁡ ( 2 p − 1) + m ​ log ⁡ 3 − y ′ ​ log ⁡ 2 − log ⁡ A 1 ′ = log ⁡ R \Lambda\ :=\ \log(2^{p}-1)+m\log 3-y^{\prime}\log 2-\log A_{1}^{\prime}\ =\ \log R |  |

is nonzero. Since R ≥ 1 2 R\geq\tfrac{1}{2} by ( 2.7), the two-sided estimate | log ⁡ R | ≤ 2 ​ | R − 1 | |\log R|\leq 2|R-1| applies: for R ≥ 1 R\geq 1 it is log ⁡ R ≤ R − 1 \log R\leq R-1, and for R < 1 R<1 it follows from − log ⁡ R = log ⁡ ( 1 / R) ≤ 1 / R − 1 = ( 1 − R) / R ≤ 2 ​ ( 1 − R) -\log R=\log(1/R)\leq 1/R-1=(1-R)/R\leq 2(1-R). Combining with ( 2.7),

(2.8) |  | 0 < | Λ | ≤ 2 x + 2 − M, hence log | Λ | ≤ ( x + 2 − M) ​ log ⁡ 2. 0<|\Lambda|\leq 2^{\,x+2-M},\qquad\text{hence}\qquad\log|\Lambda|\ \leq\ (x+2-M)\log 2. |  |

*Step 8: the lower bound from Theorem 2.1.*Apply Theorem 2.1 over K = ℚ K=\mathbb{Q}, d = 1 d=1, with n = 4 n=4 and

 | ( α 1, …, α 4) = ( 2 p − 1, 3, 2, A 1 ′), ( b 1, …, b 4) = ( 1, m, − y ′, − 1), (\alpha_{1},\dots,\alpha_{4})=\bigl(2^{p}-1,\,3,\,2,\,A_{1}^{\prime}\bigr),\qquad(b_{1},\dots,b_{4})=\bigl(1,\,m,\,-y^{\prime},\,-1\bigr), |  |

 | B:= 2 ​ m + p ≥ 2. B:=2m+p\ \geq\ 2. |  |

All four α i \alpha_{i} are nonzero positive rationals by Step 5, and the coefficients are admissible: the only one needing comment is | b 3 | = y ′ ≤ M ≤ 2 ​ m |b_{3}|=y^{\prime}\leq M\leq 2m, where M ≤ 2 ​ m M\leq 2m because 3 m ≤ 4 m = 2 2 ​ m 3^{m}\leq 4^{m}=2^{2m}. For the heights, recall h ′ ​ ( a) = max ⁡ ( log ⁡ a, 1) h^{\prime}(a)=\max(\log a,1) for a positive integer a a, and log ⁡ 2 ≤ 1 \log 2\leq 1:

 | h ′ ​ ( 2 p − 1) ≤ max ⁡ ( p ​ log ⁡ 2, 1) ≤ p, h ′ ​ ( 3) = log ⁡ 3, h ′ ​ ( 2) = 1, h^{\prime}(2^{p}-1)\leq\max(p\log 2,1)\leq p,\qquad h^{\prime}(3)=\log 3,\qquad h^{\prime}(2)=1, |  |

the first using p ≥ 1 p\geq 1; and by ( 2.6),

 | h ′ ​ ( A 1 ′) ≤ max ⁡ ( log ⁡ A 1 ′, 1) ≤ M + 1 + p − y ′, h^{\prime}(A_{1}^{\prime})\ \leq\ \max\bigl(\log A_{1}^{\prime},1\bigr)\ \leq\ M+1+p-y^{\prime}, |  |

where the floor 1 1 is harmless because y ′ ≤ M y^{\prime}\leq M and p ≥ 1 p\geq 1 force M + 1 + p − y ′ ≥ 1 M+1+p-y^{\prime}\geq 1. Hence ∏ i h ′ ​ ( α i) ≤ p ​ log ⁡ 3 ​ ( M + 1 + p − y ′) \prod_{i}h^{\prime}(\alpha_{i})\leq p\log 3\,(M+1+p-y^{\prime}), and since Λ ≠ 0 \Lambda\neq 0,

(2.9) |  | log | Λ | ≥ − C ⁡ ( 4, 1) ​ p ​ log ⁡ 3 ​ ( M + 1 + p − y ′) ​ max ⁡ ( log ⁡ ( 2 ​ m + p), 1). \log|\Lambda|\ \geq\ -C(4,1)\,p\,\log 3\,(M+1+p-y^{\prime})\,\max\bigl(\log(2m+p),1\bigr). |  |

*Step 9: conclusion.*Chaining ( 2.8) and ( 2.9) and using the identity ( M − x) ​ log ⁡ 2 = 2 ​ log ⁡ 2 − ( x + 2 − M) ​ log ⁡ 2 (M-x)\log 2=2\log 2-(x+2-M)\log 2,

 | ( M − x) ​ log ​ 2 ≤ C ⁡ ( 4, 1) ​ p ​ log ​ 3 ​ ( M + 1 + p − y ′) ​ max ⁡ ( log ⁡ ( 2 ​ m + p), 1) + 2 ​ log ​ 2. (M-x)\log 2\ \leq\ C(4,1)\,p\,\log 3\,(M+1+p-y^{\prime})\,\max\bigl(\log(2m+p),1\bigr)+2\log 2. |  |

Finally ( 2.3) gives M + 1 + p − y ′ ≤ M + 2 ​ p − y M+1+p-y^{\prime}\leq M+2p-y, and 2 ​ log ⁡ 2 ≤ ( p + 1) ​ log ⁡ 2 2\log 2\leq(p+1)\log 2 because p ≥ 1 p\geq 1. This is the asserted inequality. ∎

###### Remark 2.8 (Where the hypotheses are used).

Each hypothesis of Lemma 2.7 enters at exactly one place, and it is worth isolating them.

- •

x ≥ 1 x\geq 1 is used only in Step 4, and only to keep the parity computation in the form given there; Lemma 2.5 delivers E ≠ 0 E\neq 0 without it. As stated, this single requirement is what forces the sacrifice of one depth window in the proof of Theorem A, hence the offset − 2 -2 there in place of − 1 -1 —a loss that Remark 2.6 (ii) argues is avoidable.

- •

2 ​ p ≤ y − x 2p\leq y-x is used twice, both in Step 1: to obtain t ≥ 2 t\geq 2, so that the trimmed window is nonempty, and to obtain ( 2.4), which is precisely what places R R within 1 2 \tfrac{1}{2} of 1 1 in ( 2.7) and so licenses the two-sided logarithm estimate of Step 7. A window shorter than two periods carries no information here.

- •

y ≤ M y\leq M is used in Step 5, both for the lower bound A 1 ′′ ≥ 2 M − y ′ A_{1}^{\prime\prime}\geq 2^{M-y^{\prime}} and for M + 1 + p − y ′ ≥ 1 M+1+p-y^{\prime}\geq 1 in Step 8.

- •

The trimming of Step 1 costs at most an additive p − 1 p-1 in the depth factor; this is absorbed in Step 9 by replacing M + 1 + p − y ′ M+1+p-y^{\prime} with the larger M + 2 ​ p − y M+2p-y, which is the only reason the stated bound carries 2 ​ p 2p rather than p p.

At p = 1 p=1 we have G = 1 G=1, so the leading term log ⁡ ( 2 p − 1) \log(2^{p}-1) vanishes and Λ \Lambda degenerates to the three-term form behind Theorems 1.2 and 1.3. The lemma nonetheless invokes Theorem 2.1 with n = 4 n=4, so it does not recover the classical constant C ⁡ ( 3, 1) C(3,1) at p = 1 p=1; this is the one respect in which Theorem A is weaker, at p = 1 p=1, than the Theorem 1.3 it formally contains.

Stewart’s counting device turns such estimates into an effective lower bound. Fix θ ≥ 2 \theta\geq 2 and consider, for j = 0, 1, 2, … j=0,1,2,\dots, the depth windows of bit positions

 | [M − θ j + 1, M − θ j); \bigl[\,M-\theta^{\,j+1},\ M-\theta^{\,j}\,\bigr); |  |

there are ⌊ log θ ⁡ M ⌋ \lfloor\log_{\theta}M\rfloor disjoint such windows below the top bit. If a counting function is bounded below by the number of windows carrying a witness, an effective lower bound follows with a single constant.

###### Proposition 2.9.

Let κ > 0 \kappa>0 and Q: ℕ → ℕ Q\colon\mathbb{N}\to\mathbb{N}. Suppose that for all m ≥ 2 m\geq 2 and all θ ≥ 2 \theta\geq 2 with κ ​ log ⁡ m < θ ​ log ⁡ 2 \kappa\log m<\theta\log 2 one has ⌊ log θ ⁡ ⌊ log 2 ⁡ 3 m ⌋ ⌋ ≤ Q ⁡ ( m) \lfloor\log_{\theta}\lfloor\log_{2}3^{m}\rfloor\rfloor\leq Q(m). Then there is a constant C > 0 C>0, which one may take to be max ⁡ ( log ⁡ κ + 2 log ⁡ 2, 1) \max\bigl(\log\frac{\kappa+2}{\log 2},1\bigr), such that

 | Q ⁡ ( m) ≥ log ⁡ m log ⁡ log ⁡ m + C − 1 for every ​ m ≥ 2. Q(m)\ \geq\ \frac{\log m}{\log\log m+C}-1\qquad\text{for every }m\geq 2. |  |

###### Proof sketch.

Choose θ ≈ C ′ ​ log ⁡ m \theta\approx C^{\prime}\log m just above the threshold, so θ ≤ C ′ ​ log ⁡ m \theta\leq C^{\prime}\log m for a constant C ′ C^{\prime}; then k:= ⌊ log θ ⁡ M ⌋ ≤ Q ⁡ ( m) k:=\lfloor\log_{\theta}M\rfloor\leq Q(m) by hypothesis. Since 3 m ≥ 2 m 3^{m}\geq 2^{m} gives M ≥ m M\geq m, one has log ⁡ m ≤ ( k + 1) ​ log ⁡ θ \log m\leq(k+1)\log\theta and log ⁡ θ ≤ log ⁡ log ⁡ m + C \log\theta\leq\log\log m+C; dividing yields the bound. Positivity of the denominator uses log ⁡ log ⁡ 2 > − 1 \log\log 2>-1. ∎

###### Lemma 2.10.

If Q: ℕ → ℕ Q\colon\mathbb{N}\to\mathbb{N} satisfies Q ⁡ ( m) ≥ log ⁡ m / ( log ⁡ log ⁡ m + C) − 1 Q(m)\geq\log m/(\log\log m+C)-1 for all m ≥ 2 m\geq 2 and some C > 0 C>0, then Q ⁡ ( m) → ∞ Q(m)\to\infty.

###### Proof sketch.

The right-hand side tends to infinity, since log ⁡ m \log m dominates log ⁡ log ⁡ m \log\log m; the quantitative threshold uses log ⁡ log ⁡ m ≤ 2 ​ log ⁡ m \log\log m\leq 2\sqrt{\log m}. ∎

## 3. Aperiodicity: period- p p breaks

We prove Theorem A: for each fixed period p p, the number of places where the binary expansion of 3 m 3^{m} fails period p p grows at the Stewart rate.

The proof is a fixed procedure with two interchangeable parts: the estimate (Lemma 2.7), which certifies that one prescribed window carries a break, and the counting scheme (Proposition 2.9), which converts “one break per window” into a growth rate. It is worth setting the procedure out in full, since the passage from windows to breaks is where the two meet.

The scheme. Fix p ≥ 1 p\geq 1 and m ≥ 2 m\geq 2. Write M = M ⁡ ( 3 m) M=M(3^{m}), and let θ ≥ 2 \theta\geq 2 be any window size satisfying the *admissibility condition*

(3.1) |  | κ p ​ log ⁡ m < θ ​ log ⁡ 2, where κ p:= C ⁡ ( 4, 1) ​ log ⁡ 3 ⋅ p ⁡ ( 1 + 2 ​ p) ​ β p + ( p + 1) ⏟ needed in (W3) + 2 ​ p ⏟ needed in (W2), \begin{gathered}\kappa_{p}\,\log m\ <\ \theta\,\log 2,\qquad\text{where}\\[4.0pt] \kappa_{p}\ :=\ \underbrace{C(4,1)\log 3\cdot p(1+2p)\,\beta_{p}+(p+1)}_{\text{needed in (W3)}}\ +\ \underbrace{2p}_{\text{needed in (W2)}},\end{gathered} |  |

where β p = 2 + ( log ⁡ ( 2 + p) + 1) / log ⁡ 2 \beta_{p}=2+(\log(2+p)+1)/\log 2; note κ p ≍ p 2 ​ log ⁡ p \kappa_{p}\asymp p^{2}\log p. Put k:= ⌊ log θ ⁡ M ⌋ k:=\lfloor\log_{\theta}M\rfloor and, for 0 ≤ j < k − 1 0\leq j<k-1,

 | W j:= [M − θ j + 1, M − θ j), W_{j}\ :=\ \bigl[\,M-\theta^{\,j+1},\ M-\theta^{\,j}\,\bigr), |  |

so that the W j W_{j} tile the expansion from the top downwards in geometrically growing steps:

 | [0, M − θ k − 1) ⏟ unused ⋯ [M − θ 2, M − θ) ⏟ W 1 [M − θ, M) ⏟ W 0. \underbrace{\bigl[\,0,\ M-\theta^{\,k-1}\bigr)}_{\text{unused}}\ \ \cdots\ \ \underbrace{\bigl[\,M-\theta^{2},\,M-\theta\bigr)}_{W_{1}}\ \ \underbrace{\bigl[\,M-\theta,\,M\bigr)}_{W_{0}}. |  |

- (W1)

*Geometry.*The W j W_{j} are pairwise disjoint subintervals of [0, M) [0,M); W j W_{j} has width θ j + 1 − θ j = θ j ​ ( θ − 1) \theta^{j+1}-\theta^{j}=\theta^{j}(\theta-1) and begins at depth θ j + 1 \theta^{j+1} below the top bit. There are k − 1 k-1 of them, not k k: the index j = k − 1 j=k-1 is discarded because Lemma 2.7 requires base position ≥ 1 \geq 1, i.e. θ j + 1 < M \theta^{j+1}<M strictly. This is the sacrificed window, and the whole source of the offset − 2 -2 (see Remark 2.6 (ii)).

- (W2)

*Admissibility gives width.*Since κ p ≥ 2 ​ p \kappa_{p}\geq 2p and log ⁡ m ≥ log ⁡ 2 \log m\geq\log 2, condition ( 3.1) forces θ > 2 ​ p \theta>2p. Hence every W j W_{j} has width θ j ​ ( θ − 1) ≥ θ − 1 ≥ 2 ​ p \theta^{j}(\theta-1)\geq\theta-1\geq 2p, which is exactly the hypothesis 2 ​ p ≤ y − x 2p\leq y-x of Lemma 2.7. This is what the summand 2 ​ p 2p in κ p \kappa_{p} is for.

- (W3)

*Each window carries a break.*Suppose some W j W_{j} were p p -periodic. Apply Lemma 2.7 with x = M − θ j + 1 x=M-\theta^{j+1} and y = M − θ j y=M-\theta^{j}, so that M − x = θ j + 1 M-x=\theta^{j+1} and M + 2 ​ p − y = θ j + 2 ​ p ≤ ( 1 + 2 ​ p) ​ θ j M+2p-y=\theta^{j}+2p\leq(1+2p)\theta^{j}:

 | θ j + 1 ​ log ​ 2 ≤ C ⁡ ( 4, 1) ​ p ​ log ​ 3 ​ ( 1 + 2 ​ p) ​ θ j ​ max ⁡ ( log ⁡ ( 2 ​ m + p), 1) + ( p + 1) ​ log ​ 2. \theta^{j+1}\log 2\ \leq\ C(4,1)\,p\log 3\,(1+2p)\,\theta^{j}\,\max\bigl(\log(2m+p),1\bigr)+(p+1)\log 2. |  |

Divide by θ j ≥ 1 \theta^{j}\geq 1 and use max ⁡ ( log ⁡ ( 2 ​ m + p), 1) ≤ β p ​ log ​ m \max(\log(2m+p),1)\leq\beta_{p}\log m together with log ⁡ 2 ≤ log ⁡ m \log 2\leq\log m:

 | θ ​ log ⁡ 2 ≤ [C ⁡ ( 4, 1) ​ log ​ 3 ⋅ p ⁡ ( 1 + 2 ​ p) ​ β p + ( p + 1)] ​ log ​ m ≤ κ p ​ log ​ m, \theta\log 2\ \leq\ \bigl[C(4,1)\log 3\cdot p(1+2p)\beta_{p}+(p+1)\bigr]\log m\ \leq\ \kappa_{p}\log m, |  |

contradicting ( 3.1). So W j W_{j} is not p p -periodic: there is an index i j i_{j} with M − θ j + 1 ≤ i j M-\theta^{j+1}\leq i_{j}, i j + p < M − θ j i_{j}+p<M-\theta^{j} and bit i j ​ ( 3 m) ≠ bit i j + p ​ ( 3 m) \mathrm{bit}_{i_{j}}(3^{m})\neq\mathrm{bit}_{i_{j}+p}(3^{m}). This is the one step that consumes arithmetic; everything else is bookkeeping.

- (W4)

*The injection.*The assignment j ↦ i j j\mapsto i_{j} is strictly decreasing, hence injective: if a < b a<b then

 | i b < i b + p < M − θ b ≤ M − θ a + 1 ≤ i a. i_{b}\ <\ i_{b}+p\ <\ M-\theta^{\,b}\ \leq\ M-\theta^{\,a+1}\ \leq\ i_{a}. |  |

Each i j i_{j} lies in [0, M) [0,M) and is by construction a period- p p break, so j ↦ i j j\mapsto i_{j} injects { 0, …, k − 2 } \{0,\dots,k-2\} into the set counted by B p ​ ( 3 m) B_{p}(3^{m}). Comparing cardinalities,

(3.2) |  | ⌊ log θ ⁡ M ⌋ − 1 = k − 1 ≤ B p ​ ( 3 m), i.e. ⌊ log θ ⁡ M ⌋ ≤ B p ​ ( 3 m) + 1. \Bigl\lfloor\log_{\theta}M\Bigr\rfloor-1\ =\ k-1\ \leq\ B_{p}(3^{m}),\qquad\text{i.e.}\qquad\Bigl\lfloor\log_{\theta}M\Bigr\rfloor\ \leq\ B_{p}(3^{m})+1. |  |

- (W5)

*The endgame.*Steps (W1)–(W4) were carried out for an arbitrary θ \theta satisfying ( 3.1), so ( 3.2) holds for *every*admissible θ \theta. That is precisely the hypothesis of Proposition 2.9, applied to Q ⁡ ( m) = B p ​ ( 3 m) + 1 Q(m)=B_{p}(3^{m})+1 with coefficient κ p \kappa_{p}.

###### Proof of Theorem A.

Run the scheme. By (W5) and Proposition 2.9,

 | B p ​ ( 3 m) + 1 ≥ log ⁡ m log ⁡ log ⁡ m + C p − 1 for all ​ m ≥ 2, B_{p}(3^{m})+1\ \geq\ \frac{\log m}{\log\log m+C_{p}}-1\qquad\text{for all }m\geq 2, |  |

with C p = max ⁡ ( log ⁡ ( ( κ p + 2) / log ⁡ 2), 1) > 0 C_{p}=\max\bigl(\log((\kappa_{p}+2)/\log 2),1\bigr)>0; subtracting 1 1 gives the stated inequality. The divergence B p ​ ( 3 m) → ∞ B_{p}(3^{m})\to\infty is Lemma 2.10. ∎

###### Remark 3.1 (The division of labour).

The scheme isolates the two inputs cleanly. Lemma 2.7 is used exactly once, in (W3), and only through the single implication “a window at depth θ j + 1 \theta^{j+1} and of width ≥ 2 ​ p \geq 2p cannot be p p -periodic”; it never sees the counting. Proposition 2.9 is used exactly once, in (W5), and only through ( 3.2); it never sees the digits—in the formalization all Baker content is quarantined in its hypothesis, which is why windowCount_lower_bound_gen carries the footprint std3 while gap_principle carries std3 + [BW93]. The coefficient κ p \kappa_{p} is the only channel between them, and ( 3.1) displays it doing its two jobs: the bracket is what (W3) must beat, the summand 2 ​ p 2p is what (W2) needs. Replacing Lemma 2.7 by a sharper estimate would change only κ p \kappa_{p}, leaving (W1), (W2), (W4) and (W5) untouched—which is the sense in which Remark 4.5 ’s discussion of better transcendence input is a statement about κ p \kappa_{p} alone.

###### Remark 3.2.

The offset is − 2 -2, rather than the − 1 -1 of Theorems 1.2 and 1.3, because one window is sacrificed: Lemma 2.7 requires the base position of the periodic stretch to be at least 1 1. The bound is uniform in m m for each fixed p p; the growth C p ≍ log ⁡ p C_{p}\asymp\log p of the constant is carried by the coefficient κ p ≍ p 2 ​ log ⁡ p \kappa_{p}\asymp p^{2}\log p.

###### Remark 3.3 (The constant C p C_{p}, numerically).

The proof exhibits C p C_{p}, via Proposition 2.9, as

 | C p = max ⁡ ( log ⁡ κ p + 2 log ⁡ 2, 1), κ p = C ⁡ ( 4, 1) ​ log ⁡ 3 ⋅ p ⁡ ( 1 + 2 ​ p) ​ β p + 3 ​ p + 1, C_{p}=\max\Bigl(\log\frac{\kappa_{p}+2}{\log 2},\,1\Bigr),\qquad\kappa_{p}=C(4,1)\log 3\cdot p(1+2p)\,\beta_{p}+3p+1, |  |

 | β p = 2 + log ⁡ ( 2 + p) + 1 log ⁡ 2, \beta_{p}=2+\frac{\log(2+p)+1}{\log 2}, |  |

so Remark 2.2 turns it into a number. For p = 1 p=1, β 1 < 5.028 \beta_{1}<5.028, κ 1 < 8.19 × 10 16 \kappa_{1}<8.19\times 10^{16} and

 | C 1 < 39.31, C_{1}<39.31, |  |

i.e. B 1 ​ ( 3 m) = T ⁡ ( 3 m) ≥ log ⁡ m / ( log ⁡ log ⁡ m + 39.31) − 2 B_{1}(3^{m})=T(3^{m})\geq\log m/(\log\log m+39.31)-2 for all m ≥ 2 m\geq 2. In general κ p < 5.43 × 10 15 ​ p ​ ( 2 ​ p + 1) ​ β p \kappa_{p}<5.43\times 10^{15}\,p(2p+1)\beta_{p} and

 | C p < 40 + 3 ​ log ⁡ ( p + 1) for every ​ p ≥ 1. C_{p}\ <\ 40+3\log(p+1)\qquad\text{for every }p\geq 1. |  |

The size of these constants is dominated entirely by C ⁡ ( 4, 1) C(4,1); the combinatorial part of the argument contributes the factor p ⁡ ( 2 ​ p + 1) ​ β p p(2p+1)\beta_{p}, of order p 2 ​ log ⁡ p p^{2}\log p.

The first ten periods, evaluated from ( 3.1) and Proposition 2.9:

p p | β p \beta_{p} | κ p \kappa_{p} | C p C_{p} | least m m with B p ​ ( 3 m) ≥ 1 B_{p}(3^{m})\geq 1 |

1 1 | 5.028 5.028 | 8.18 × 10 16 8.18\times 10^{16} | 39.31 39.31 | 1.1 × 10 38 1.1\times 10^{38} |

2 2 | 5.443 5.443 | 2.95 × 10 17 2.95\times 10^{17} | 40.59 40.59 | 1.5 × 10 39 1.5\times 10^{39} |

3 3 | 5.765 5.765 | 6.57 × 10 17 6.57\times 10^{17} | 41.39 41.39 | 7.6 × 10 39 7.6\times 10^{39} |

4 4 | 6.028 6.028 | 1.18 × 10 18 1.18\times 10^{18} | 41.98 41.98 | 2.5 × 10 40 2.5\times 10^{40} |

5 5 | 6.250 6.250 | 1.87 × 10 18 1.87\times 10^{18} | 42.44 42.44 | 6.4 × 10 40 6.4\times 10^{40} |

6 6 | 6.443 6.443 | 2.73 × 10 18 2.73\times 10^{18} | 42.82 42.82 | 1.4 × 10 41 1.4\times 10^{41} |

7 7 | 6.613 6.613 | 3.77 × 10 18 3.77\times 10^{18} | 43.14 43.14 | 2.7 × 10 41 2.7\times 10^{41} |

8 8 | 6.765 6.765 | 4.99 × 10 18 4.99\times 10^{18} | 43.42 43.42 | 4.8 × 10 41 4.8\times 10^{41} |

9 9 | 6.902 6.902 | 6.40 × 10 18 6.40\times 10^{18} | 43.67 43.67 | 7.9 × 10 41 7.9\times 10^{41} |

10 10 | 7.028 7.028 | 8.01 × 10 18 8.01\times 10^{18} | 43.89 43.89 | 1.3 × 10 42 1.3\times 10^{42} |

The last column is the least m m at which log ⁡ m / ( log ⁡ log ⁡ m + C p) − 2 \log m/(\log\log m+C_{p})-2 becomes positive, i.e. the point from which Theorem A asserts anything at all. Two features are worth noting. First, C p C_{p} barely moves: it is a logarithm of κ p \kappa_{p}, so the factor p 2 ​ log ⁡ p p^{2}\log p by which κ p \kappa_{p} grows across the table costs C p C_{p} less than five units. Second, that slow growth is nevertheless amplified on exponentiation, and the last column climbs some four orders of magnitude over p ≤ 10 p\leq 10. Both columns are ordinary evaluations of the displayed formulas; Remark 4.5 discusses what such magnitudes mean.

## 4. Subword complexity

We now prove Theorem B. The combinatorial input is the following finite form of the Morse–Hedlund theorem, in which we make no appeal to Fine–Wilf; it is proved by a self-contained determinism-propagation argument.

###### Lemma 4.1 (Finite Morse–Hedlund floor).

Let u = ( u 0, u 1, …) u=(u_{0},u_{1},\dots) be a word over an alphabet with decidable equality, and let n ≥ 1 n\geq 1 and L ≥ 3 ​ n L\geq 3n. If u u has at most n n distinct factors of length n n among the positions 0, …, L − n 0,\dots,L-n, then there exist a a and 1 ≤ p ≤ n 1\leq p\leq n such that u u has period p p on the factor [a, a + ( L − 2 n)) [a,\,a+(L-2n)); that is, u t = u t + p u_{t}=u_{t+p} for all a ≤ t a\leq t with t + p < a + ( L − 2 ​ n) t+p<a+(L-2n).

###### Proof sketch.

On the fixed position set [0, L − n] [0,L-n] the number c ⁡ ( k) c(k) of distinct length- k k factors is non-decreasing in k k: dropping the last letter of a length- ( k + 1) (k+1) factor surjects onto the length- k k factors. Since c ⁡ ( 0) = 1 c(0)=1 and c ⁡ ( n) ≤ n c(n)\leq n, the count cannot strictly increase n n times, so there is a plateau c ⁡ ( k) = c ⁡ ( k + 1) c(k)=c(k+1) with k < n k<n. A plateau forces right-determinism—two positions carrying the same length- k k factor carry the same next letter. Pigeonhole over the first c ⁡ ( k) + 1 c(k)+1 positions produces two equal length- k k factors at an offset p ≤ n p\leq n, and determinism propagates the period- p p relation across the window. ∎

Feeding such a periodic factor to the period- p p run estimate caps its depth, in the following effective form.

###### Lemma 4.2.

Let n ≥ 1 n\geq 1 and M = ⌊ log 2 ⁡ 3 m ⌋ ≥ 4 ​ n + 1 M=\lfloor\log_{2}3^{m}\rfloor\geq 4n+1. If p 3 m ​ ( n) ≤ n p_{3^{m}}(n)\leq n, then

 | ( M − ( 3 ​ n + 2)) ​ log ⁡ 2 ≤ 4 ​ C ​ ( 4, 1) ​ n 2 ​ log ⁡ 3 ​ max ⁡ ( log ⁡ ( 2 ​ m + n), 1). \bigl(M-(3n+2)\bigr)\log 2\ \leq\ 4\,C(4,1)\,n^{2}\,\log 3\,\max\bigl(\log(2m+n),1\bigr). |  |

###### Proof sketch.

By Lemma 4.1 with L = M L=M, a factor complexity ≤ n \leq n yields a period- p p factor with 1 ≤ p ≤ n 1\leq p\leq n of length M − 2 ​ n M-2n, starting at some a ≤ 2 ​ n a\leq 2n. Apply the period- p p run estimate (Lemma 2.7) with base x = a + 1 ≥ 1 x=a+1\geq 1 and y = a + ( M − 2 ​ n) y=a+(M-2n): the depth factor is M + 2 ​ p − y = 2 ​ p + 2 ​ n − a ≤ 4 ​ n M+2p-y=2p+2n-a\leq 4n, and p ⁡ ( 2 ​ p + 2 ​ n − a) ≤ 4 ​ n 2 p(2p+2n-a)\leq 4n^{2} collapses the right-hand side to the stated form. ∎

###### Proof of Theorem B.

Fix n ≥ 1 n\geq 1 and suppose, for contradiction, that p 3 m ​ ( n) ≤ n p_{3^{m}}(n)\leq n for arbitrarily large m m. Since M = ⌊ log 2 ⁡ 3 m ⌋ ≥ m M=\lfloor\log_{2}3^{m}\rfloor\geq m, Lemma 4.2 would give

 | ( m − ( 3 ​ n + 2)) ​ log ⁡ 2 ≤ 4 ​ C ​ ( 4, 1) ​ n 2 ​ log ⁡ 3 ​ max ⁡ ( log ⁡ ( 2 ​ m + n), 1); (m-(3n+2))\log 2\ \leq\ 4\,C(4,1)\,n^{2}\log 3\,\max(\log(2m+n),1); |  |

but the left-hand side grows linearly in m m while the right-hand side grows like log ⁡ m \log m, a contradiction for large m m. Hence p 3 m ​ ( n) ≥ n + 1 p_{3^{m}}(n)\geq n+1 eventually. The effective threshold m 0 ​ ( n) m_{0}(n) is where m m overtakes

 | 4 ​ C ​ ( 4, 1) ​ n 2 ​ log ⁡ 3 log ⁡ 2 ​ log ⁡ ( 2 ​ m + n) + ( 3 ​ n + 2). ∎ 4\,C(4,1)\,n^{2}\,\frac{\log 3}{\log 2}\,\log(2m+n)+(3n+2).\qed |  |

###### Remark 4.3 (What Theorem B does and does not say).

The word in question has length M = M ⁡ ( 3 m) M=M(3^{m}), so its complexity function is confined to

 | 1 ≤ p 3 m ​ ( n) ≤ min ⁡ ( 2 n, M − n + 1), 1\ \leq\ p_{3^{m}}(n)\ \leq\ \min\bigl(2^{n},\,M-n+1\bigr), |  |

the upper bound being trivial: there are only 2 n 2^{n} binary words of length n n, and only M − n + 1 M-n+1 positions at which to read one. Within that range the value n + 1 n+1 sits at the very bottom of the aperiodic regime, not near the top.

- •

By Morse–Hedlund [MH38] —in the finite form of Lemma 4.1 —the inequality p w ​ ( n) ≤ n p_{w}(n)\leq n for a *single*n n already forces periodicity. So “ p ⁡ ( n) ≥ n + 1 p(n)\geq n+1 for every n n ” is exactly the negation of periodicity, and asserts nothing beyond it.

- •

The bound is attained identically: Sturmian words satisfy p w ​ ( n) = n + 1 p_{w}(n)=n+1 for all n n, and they are precisely the aperiodic words of *minimal*complexity. A word meeting our bound with equality is thus as far from maximal complexity as an aperiodic word can be.

- •

Maximal complexity, p ⁡ ( n) = min ⁡ ( 2 n, M − n + 1) p(n)=\min(2^{n},M-n+1), is a de Bruijn-type property; a normal or random word has p ⁡ ( n) = 2 n p(n)=2^{n} throughout the range 2 n ≲ M 2^{n}\lesssim M. We prove nothing of the sort, and nothing intermediate either.

Theorem B should therefore be read as the quantitative, n n -uniform statement that *the low-order digit word of 3 m 3^{m} is not periodic*, valid for all m m beyond an explicit threshold. Whether p 3 m ​ ( n) / n → ∞ p_{3^{m}}(n)/n\to\infty —let alone p 3 m ​ ( n) = 2 n p_{3^{m}}(n)=2^{n} in the admissible range—is open.

To be clear, the combiatorial half of the argument imposes this ceiling: Lemma 4.1 converts the hypothesis p ⁡ ( n) ≤ n p(n)\leq n into a long periodic factor, whereas a hypothesis of the shape p ⁡ ( n) ≤ C ​ n p(n)\leq Cn with C > 1 C>1 yields no periodic factor at all, and so gives Lemma 2.7 nothing to act on. Sharpening the linear-forms input would not move the bound past n + 1 n+1.

###### Remark 4.4 (The threshold m 0 ​ ( n) m_{0}(n), numerically).

By Remark 2.2 the coefficient 4 ​ C ​ ( 4, 1) ​ n 2 ​ log ⁡ 3 / log ⁡ 2 4C(4,1)n^{2}\log 3/\log 2 is at most 3.14 × 10 16 ​ n 2 3.14\times 10^{16}\,n^{2}, so m 0 ​ ( n) m_{0}(n) is the least m m with m ≥ 3.14 × 10 16 ​ n 2 ​ log ⁡ ( 2 ​ m + n) + 3 ​ n + 2 m\geq 3.14\times 10^{16}\,n^{2}\log(2m+n)+3n+2; the left side then stays ahead for all larger m m, since 3.14 × 10 16 ​ n 2 / m < 1 2 3.14\times 10^{16}n^{2}/m<\tfrac{1}{2} there. Solving,

 | m 0 ( 1) < 1.33 × 10 18, m 0 ( n) < 2 × 10 18 n 2 ( 1 + log n) ( n ≥ 1). m_{0}(1)<1.33\times 10^{18},\qquad m_{0}(n)<2\times 10^{18}\,n^{2}\,(1+\log n)\quad(n\geq 1). |  |

Thus p 3 m ​ ( n) ≥ n + 1 p_{3^{m}}(n)\geq n+1 holds for every m ≥ m 0 ​ ( n) m\geq m_{0}(n) with m 0 m_{0} as above. As in Remark 3.3 the magnitude is inherited from C ⁡ ( 4, 1) C(4,1), and the thresholds are far beyond direct computation; the n 2 ​ log n^{2}\log shape, not the numerical value, is what the linear-forms input dictates.

Thresholds across a range of factor lengths:

n n | m 0 ​ ( n) m_{0}(n) | m 0 ​ ( n) / n 2 m_{0}(n)/n^{2} | binary digits of 3 m 0 ​ ( n) 3^{m_{0}(n)} |

1 1 | 1.33 × 10 18 1.33\times 10^{18} | 1.33 × 10 18 1.33\times 10^{18} | 2.1 × 10 18 2.1\times 10^{18} |

2 2 | 5.49 × 10 18 5.49\times 10^{18} | 1.37 × 10 18 1.37\times 10^{18} | 8.7 × 10 18 8.7\times 10^{18} |

3 3 | 1.26 × 10 19 1.26\times 10^{19} | 1.40 × 10 18 1.40\times 10^{18} | 2.0 × 10 19 2.0\times 10^{19} |

5 5 | 3.58 × 10 19 3.58\times 10^{19} | 1.43 × 10 18 1.43\times 10^{18} | 5.7 × 10 19 5.7\times 10^{19} |

10 10 | 1.48 × 10 20 1.48\times 10^{20} | 1.48 × 10 18 1.48\times 10^{18} | 2.3 × 10 20 2.3\times 10^{20} |

20 20 | 6.08 × 10 20 6.08\times 10^{20} | 1.52 × 10 18 1.52\times 10^{18} | 9.6 × 10 20 9.6\times 10^{20} |

50 50 | 3.95 × 10 21 3.95\times 10^{21} | 1.58 × 10 18 1.58\times 10^{18} | 6.3 × 10 21 6.3\times 10^{21} |

100 100 | 1.62 × 10 22 1.62\times 10^{22} | 1.62 × 10 18 1.62\times 10^{18} | 2.6 × 10 22 2.6\times 10^{22} |

The third column exhibits the shape: m 0 ​ ( n) m_{0}(n) is very nearly 1.4 × 10 18 ​ n 2 1.4\times 10^{18}\,n^{2} across the whole range, the slow drift—about 22 % 22\% from n = 1 n=1 to n = 100 n=100 —being the residual log \log factor of Lemma 4.2. The last column records how long the digit string of 3 m 3^{m} must be before the theorem applies, which is the figure Remark 4.5 takes up for n = 10 n=10.

###### Remark 4.5 (A ballpark at n = 10 n=10, and how the gap divides).

It is worth seeing what such a threshold means concretely. Take n = 10 n=10. Solving the inequality of Remark 4.4 gives

 | m 0 ​ ( 10) < 1.48 × 10 20, m_{0}(10)\ <\ 1.48\times 10^{20}, |  |

at which point 3 m 3^{m} has some 2.3 × 10 20 2.3\times 10^{20} binary digits—about 7.0 × 10 19 7.0\times 10^{19} decimal digits, or 29 29 exabytes merely to write down. Counting from 1 1 to m 0 ​ ( 10) m_{0}(10) at one step per nanosecond would take some 4700 4700 years. The threshold is thus entirely out of computational reach and will remain so.

The truth is some nineteen orders of magnitude smaller. Direct computation gives p 3 m ​ ( 10) ≥ 11 p_{3^{m}}(10)\geq 11 already at m = 13 m=13, and at every m m from 13 13 to 899 899, as far as we have checked. Indeed m = 13 m=13 is the earliest value at which the inequality is so much as satisfiable: M ⁡ ( 3 13) = 20 M(3^{13})=20 leaves exactly the eleven positions 0, …, 10 0,\dots,10 at which to read a factor of length 10 10, and the eleven factors read there are distinct. For n = 10 n=10, then, the conclusion holds from the first moment it is not vacuous.

The gap divides unevenly between the two inputs. About sixteen and a half orders of magnitude are charged to C ⁡ ( 4, 1) C(4,1) alone: replacing it by the absurd value 1 1 in Lemma 4.2 would already bring m 0 ​ ( 10) m_{0}(10) down to roughly 6.0 × 10 3 6.0\times 10^{3}. The remaining two and a half orders are charged to the method, which is lossy even with a perfect transcendence constant—the periodic windows that Lemma 2.7 fails to exclude are far longer than any the digits of 3 m 3^{m} appear to contain. Sharpening the linear-forms input would therefore improve the threshold almost proportionally, but nothing short of a different mechanism brings it near 13 13.

It is natural to ask whether a sharper transcendence input would help, and by how much. The literature offers a definite ladder. Matveev’s theorem [Mat00] replaces the n 2 ​ n n^{2n} -type factor of [BW93] by a pure exponential 30 n + 3 30^{n+3}, worth roughly a factor 325 325 at n = 4 n=4, d = 1 d=1; that alone would bring m 0 ​ ( 10) m_{0}(10) down to about 4 × 10 17 4\times 10^{17}. Sharper still are the few-logarithm specialists: Laurent’s two-logarithm bound [Lau08], Rhin’s Padé bound for the specific pair ( 2, 3) (2,3) [Rhi87], and the three-logarithm kit of Mignotte and Voutier [MV24], which runs some 10 3 10^{3} – 10 4 10^{4} below the closed-form n = 3 n=3 engines.

The difficulty is that the sharpest of these are unavailable to us for a structural, not a practical, reason. The form Λ \Lambda of Step 7 has four logarithms and cannot be shortened. Two of them are the fixed log ⁡ 2 \log 2 and log ⁡ 3 \log 3; the other two are not optional. The term log ⁡ A 1 ′ \log A_{1}^{\prime} carries the digit structure— A 1 ′ A_{1}^{\prime} is the very quantity whose size the argument bounds, and its height grows like M M —while log ⁡ ( 2 p − 1) \log(2^{p}-1) is the geometric-series denominator that Lemma 2.3 forces. So n ≥ 3 n\geq 3 always, and n = 4 n=4 as soon as p ≥ 2 p\geq 2: the two-logarithm engines, Rhin’s included, are out of reach however much effort is spent on them. The one exception is instructive. At p = 1 p=1 we have 2 p − 1 = 1 2^{p}-1=1, the leading term vanishes, and the run estimate behind Theorems 1.2 and 1.3 is genuinely a three-logarithm form, to which [MV24] applies in principle. Theorem A for p ≥ 2 p\geq 2, and Theorem B, which needs every p ≤ n p\leq n, gain nothing from it.

A second obstacle attaches to the instance-tuned kits specifically. [MV24] does not supply a closed-form constant: for a given coefficient vector one runs a parameter search, and the theorem returns a per-instance trichotomy. Our vector ( 1, m, − y ′, − 1) (1,m,-y^{\prime},-1) varies with m m, and the conclusion is asymptotic in m m, so no single certified instance suffices; one would have to stratify m m into ranges and certify each, obtaining a threshold with range-dependent constants, or else find a uniform version. Compounding this, one of our α i \alpha_{i} —again A 1 ′ A_{1}^{\prime} —has height growing with m m, whereas such kits are calibrated for fixed α i \alpha_{i} and growing coefficients.

Finally, the arithmetic input is not the whole gap. Bringing m 0 ​ ( 10) m_{0}(10) down to 10 9 10^{9}, where a computation might conceivably reach it, would need C ⁡ ( 4, 1) C(4,1) replaced by about 7 × 10 4 7\times 10^{4} —a reduction by a factor 7 × 10 10 7\times 10^{10} —and 10 6 10^{6} would require going below 110 110; nothing in the present literature is within many orders of magnitude of either, and the residual factor of some 460 460 identified above would survive a perfect constant anyway. The realistic assessment is that a sharper engine would move these thresholds by a few orders of magnitude without bringing them into computational range. Matveev is the immediately available one, and substituting it is a bounded piece of work, since it differs from [BW93] chiefly in its height normalization rather than in its shape; we have not carried it out here.

The numerical values in this remark are ordinary computations, reported to calibrate expectations; they are not part of the formalization.

Theorem B is the analogue, for the finite digit word of a single integer 3 m 3^{m}, of the Morse–Hedlund rung for the infinite steering word of ( 3 / 2) n (3/2)^{n}. For that word a superlinear bound is available [RS26]; no such strengthening is claimed here, and Remark 4.3 explains why the present method cannot reach one. Superlinear complexity for the digits of 3 m 3^{m} remains a separate and harder question.

## 5. Scope: other bases and other sequences

The number 3 3 plays almost no role in the proofs of Theorems A and B, and the base 2 2 enters through exactly one arithmetic fact. This section records what the argument consumes, the generality it yields, and where it stops. Nothing here is claimed as a theorem of this paper: unlike every statement of Sections 1 – 4, the assertions below are *not*formalized, and we have not written out the proofs they would need.

### 5.1. What the proof uses about the pair ( 3, 2) (3,2)

Fix integers a, b ≥ 2 a,b\geq 2 and consider the base- b b digits of a m a^{m}; this paper is the case ( a, b) = ( 3, 2) (a,b)=(3,2). Walk through the proof of Lemma 2.7.

Steps 1, 2, 3, 5, 6 and 7 use nothing about a a and b b beyond b ≥ 2 b\geq 2. In particular Lemma 2.3 holds verbatim with 2 2 replaced by b b: the repeated block is c = ⌊ N / b x ⌋ mod b p c=\lfloor N/b^{x}\rfloor\bmod b^{p}, the cleared identity is

 | ( b p − 1) ​ ( N mod b x + t ​ p) = ( b p − 1) ​ ( N mod b x) + c ⁡ ( b x + t ​ p − b x), (b^{p}-1)\bigl(N\bmod b^{x+tp}\bigr)=(b^{p}-1)\bigl(N\bmod b^{x}\bigr)+c\,\bigl(b^{x+tp}-b^{x}\bigr), |  |

and the proof is the same two inductions. (The Lean version is written for b = 2 b=2, but uses nothing about 2 2.) Step 3 becomes ( b p − 1) ​ a m = A 1 ′ ​ b y ′ + E (b^{p}-1)a^{m}=A_{1}^{\prime}b^{y^{\prime}}+E with E = ( b p − 1) ​ A 2 − c ​ b x E=(b^{p}-1)A_{2}-c\,b^{x}, and Step 6 gives | R − 1 | ≤ b x + 1 − M ≤ b − 1 ≤ 1 2 |R-1|\leq b^{\,x+1-M}\leq b^{-1}\leq\tfrac{1}{2}, using b p − 1 ≥ b p − 1 b^{p}-1\geq b^{p-1}.

Step 8 uses only that log ⁡ a m = m ​ log ⁡ a \log a^{m}=m\log a is an integer multiple of one fixed logarithm. The four logarithms are those of b p − 1 b^{p}-1, a a, b b and A 1 ′ A_{1}^{\prime}, so the constant is still C ⁡ ( 4, 1) C(4,1): neither n = 4 n=4 nor d = 1 d=1 moves. Only the height product changes, from p ​ log ⁡ 3 ⋅ 1 ⋅ ( M + 1 + p − y ′) p\log 3\cdot 1\cdot(M+1+p-y^{\prime}) to a quantity of size ≍ p ​ log ⁡ a ​ ( log ⁡ b) 3 ​ ( M + 1 + p − y ′) \asymp p\,\log a\,(\log b)^{3}\,(M+1+p-y^{\prime}) when b ≥ 3 b\geq 3; at b = 2 b=2 the floors h ′ ​ ( ⋅) ≥ 1 h^{\prime}(\cdot)\geq 1 are active instead, as in Step 8. The effect is on κ p \kappa_{p} and hence on C p C_{p}, never on the shape log ⁡ m / log ⁡ log ​ m \log m/\log\log m.

Step 4 is the only step with arithmetic content, and the only one where a a and b b must be related at all. What it needs is

(5.1) |  | there is a prime ​ ℓ | b ​ with ​ ℓ ∤ a. \text{there is a prime }\ell\mid b\text{ with }\ell\nmid a. |  |

This is exactly the hypothesis of Lemma 2.5, which was stated in base b b for this reason: it gives E ≡ − a m ≢ 0 ( mod ℓ) E\equiv-a^{m}\not\equiv 0\pmod{\ell}, hence E ≠ 0 E\neq 0, for every x ≥ 0 x\geq 0. For ( a, b) = ( 3, 2) (a,b)=(3,2) the prime is ℓ = 2 \ell=2 and the congruence is the parity computation of Step 4.

### 5.2. The resulting generality

Under ( 5.1) the argument goes through unchanged and yields, for every fixed p ≥ 1 p\geq 1,

 | B p ( b) ​ ( a m) ≥ log ⁡ m log ⁡ log ⁡ m + C p ​ ( a, b) − 2, p a m ( b) ​ ( n) ≥ n + 1 ( m ≥ m 0 ​ ( n, a, b)), \begin{gathered}B_{p}^{(b)}(a^{m})\ \geq\ \frac{\log m}{\log\log m+C_{p}(a,b)}-2,\\[4.0pt] p^{(b)}_{a^{m}}(n)\ \geq\ n+1\quad\bigl(m\geq m_{0}(n,a,b)\bigr),\end{gathered} |  |

where B p ( b) B^{(b)}_{p} and p ( b) p^{(b)} are the base- b b analogues and the constants are explicit exactly as in Remarks 3.3 and 4.4. The combinatorial half of Theorem B needs no change whatever: Lemma 4.1 is stated and proved over an arbitrary alphabet with decidable equality—as is its Lean form—so it applies to base- b b digits as it stands.

Hypothesis ( 5.1) is not an artifact of the write-up. It implies that a a and b b are multiplicatively independent, since a = g i a=g^{i} and b = g j b=g^{j} would give a a and b b the same prime divisors; and some such hypothesis is necessary, because for a = b k a=b^{k} the integer a m = b k ​ m a^{m}=b^{km} has a single nonzero base- b b digit, so B p ( b) ​ ( a m) = 1 B_{p}^{(b)}(a^{m})=1 for every m m and Theorem A is simply false. In the intermediate case where a a and b b are multiplicatively independent but every prime of b b divides a a —say ( a, b) = ( 6, 2) (a,b)=(6,2), the degeneracy exhibited in Remark 2.6 (i)—it is the proof that fails, not the conclusion: 6 m = 2 m ​ 3 m 6^{m}=2^{m}3^{m} ends in m m binary zeros, so the deep windows on which Step 4 operates carry no information, whereas the conclusion survives by the shift, the digits above position m m being those of 3 m 3^{m}. A statement adapted to that case should concern the digits above the trailing zeros, and our windowing, which reaches down to x ≥ 1 x\geq 1, is not adapted to it.

### 5.3. How far the sequence can be moved

Nothing in Steps 1–7 uses that the integer being expanded is a power. The constraint sits in Step 8, and it is sharp: the linear form needs log ⁡ u \log u to be a ℤ \mathbb{Z} -combination, with coefficients of size O ⁡ ( log ⁡ u) O(\log u), of the logarithms of a *fixed finite*set of algebraic numbers.

*S S -units.*Let S S be a fixed finite set of primes and let u u range over the positive integers with all prime factors in S S. Writing u = ∏ q ∈ S q e q u=\prod_{q\in S}q^{e_{q}}, with e q ≤ log ⁡ u / log ⁡ 2 e_{q}\leq\log u/\log 2, the form becomes

 | Λ = log ⁡ ( b p − 1) + ∑ q ∈ S e q ​ log ⁡ q − y ′ ​ log ⁡ b − log ⁡ A 1 ′, \Lambda=\log(b^{p}-1)+\sum_{q\in S}e_{q}\log q-y^{\prime}\log b-\log A_{1}^{\prime}, |  |

of | S | + 3 |S|+3 terms; ( 5.1) becomes the requirement that some prime of b b lie outside S S. Everything else is unchanged, and the conclusion takes the form B p ( b) ​ ( u) ≫ log ⁡ log ⁡ u / ( log ⁡ log ⁡ log ⁡ u + C) B_{p}^{(b)}(u)\gg\log\log u/(\log\log\log u+C), with C ⁡ ( | S | + 3, 1) C(|S|+3,1) in place of C ⁡ ( 4, 1) C(4,1). This is the natural home of the argument. It is also the setting of Bugeaud–Kaneko [BK17], whose Corollary 1.5 is quoted in Theorem 1.3 for exactly this reason; the increment over S S -units would be the periodic refinement, B p B_{p} in place of T T.

*Everything else.*If u u is not an S S -unit then log ⁡ u \log u is not a short combination of fixed logarithms, and u u must itself enter the form as one of the α i \alpha_{i}. Its modified height is then ≍ log ⁡ u \asymp\log u, the right-hand side of ( 2.9) degrades from O ⁡ ( log ⁡ m) O(\log m) to O ⁡ ( m ​ log ⁡ m) O(m\log m), and the contradiction of Step 9—which pits it against the linear growth of M ≍ m M\asymp m —evaporates. This is the real boundary of the method, and it is a height obstruction rather than a defect of the exposition.

Linear recurrence sequences sit instructively in between. For a non-degenerate binary recurrence with dominant root α \alpha one has u m = c ​ α m + O ⁡ ( | β | m) u_{m}=c\,\alpha^{m}+O(|\beta|^{m}) with | β | < | α | |\beta|<|\alpha|, so log ⁡ u m \log u_{m} is a combination of the fixed logarithms log ⁡ c \log c and log ⁡ α \log\alpha up to an exponentially small error, at the cost of working in ℚ ⁡ ( α, β) \mathbb{Q}(\alpha,\beta) and hence with C ⁡ ( n, d) C(n,d) for d > 1 d>1. That is the setting of Stewart’s Theorem 2 in [Ste80], which is stated for recurrence sequences and specialized to u n = 3 n u_{n}=3^{n} in Theorem 1.2; so the classical rungs, Theorems 1.2 and 1.3, are available there. What is *not*immediate is Lemma 2.7. Its Step 3 is an exact identity between integers, and for a recurrence that is not an S S -unit it would have to be replaced by an approximate one, with the subdominant-root error carried through Steps 6–9; and the parity argument of Step 4 would need a substitute, since E E would no longer be a single congruence away from zero. We see no obstruction in principle, but we have not carried it out. Sequences such as ⌊ ( 3 / 2) m ⌋ \lfloor(3/2)^{m}\rfloor, whose logarithms are not linear forms at all, lie outside the method entirely.

### 5.4. What is genuinely specific to 3 3

Only the sparse side. Theorem 1.4 —the powers of three with at most 22 22 nonzero binary digits—is a statement about the pair ( 3, 2) (3,2) and an instance of a conjecture of Erdős; it is not the specialization of anything general, and Theorem 1.5 inherits that. By contrast Theorems A and B, and the run estimates driving them, see the number 3 3 only through the quantity log ⁡ 3 \log 3 in their constants.

## 6. Acknowledgements

The author utilized Claude Code as an AI coding assistant to aid in the Lean 4 formalization of the proofs presented in this paper. The author directed and reviewed all generated code and takes full responsibility for the mathematical integrity and final content of the work.

## Appendix A Formalization

Every statement in Sections 1 – 4 —the classical bounds reviewed in Section 1.1 as well as the new Theorems A and B —was verified in Lean 4. There are two exceptions, both flagged where they occur. Section 5 is discussion: none of the generalizations sketched there has been formalized or written out in full. And Remark 2.6 (ii)—that the hypothesis x ≥ 1 x\geq 1 may be dropped, so that Theorem A would carry the offset − 1 -1 —is an observation only: the Lean gap_principle retains 1 ≤ x 1\leq x, and the verified form of Theorem A is the one stated in this paper. Lemma 2.5 itself appears in Lean only inline, as the step hEr_ne of gap_principle, in the base- 2 2, x ≥ 1 x\geq 1 case. The files live under TH/DigitBlocks/, with TH/StewartDigits.lean, TH/BakerInterface.lean (the modified height over ℚ \mathbb{Q}), ForMathlib/Data/Nat/BinaryDigits.lean (the bit-manipulation lemmas of Lemma 2.3), ForMathlib/Combinatorics/SubwordComplexity.lean, CITED/BakerWustholz.lean and CITED/DimitrovHowe.lean supplying inputs. “std3” abbreviates the ambient axioms of classical Lean (propositional extensionality, choice, quotient soundness); “[BW93]” marks additional reliance on the cited Baker–Wüstholz axiom BakerWustholz.linearForms_logs, and “[DH23]” on the cited Dimitrov–Howe axiom DH.three_pow_three_binary_digits. Every entry is fully proved in Lean except the two marked *cited axiom*.

A word on the constants of Remarks 2.2 – 4.4 and their formal counterparts. BakerWustholz.C n d is *defined*by the closed formula of Remark 2.2, so the cited axiom linearForms_logs is recorded in its explicit form and every Lean statement downstream carries that value. Theorem A ( breakCount_three_pow_lower) and Proposition 2.9 ( windowCount_lower_bound_gen) are nevertheless *stated*with an existentially quantified constant, ∃ C > 0 \exists\,C>0; the witness their proofs supply is exactly max ⁡ ( log ⁡ κ + 2 log ⁡ 2, 1) \max\bigl(\log\frac{\kappa+2}{\log 2},1\bigr) with κ = κ p \kappa=\kappa_{p}, which is what Remark 3.3 evaluates. Similarly Theorem B ( three_pow_complexity_ge) is stated with Mathlib’s eventually-filter ∀ f \forall^{f} m in atTop, the threshold being the one computed in Remark 4.4. The numerical values quoted in this paper are therefore the ones the formal proofs produce, but they are read off from the proof terms rather than appearing in the Lean statements.

All Lean-4 files are available from the repository https://github.com/rwst/Aperiodicity-and-Subword-Complexity

### A.1. Formalizing the classical bounds

The classical statements reviewed in Section 1.1 account for the larger part of the development: roughly 1 300 1\,300 lines of Lean in StewartDigits, Transitions, SparseSide and Defs, against some 800 800 for the new Theorems A and B ( Aperiodicity, Complexity, SubwordComplexity) and a further 1 400 1\,400 of shared infrastructure ( GapPrinciples, BinaryDigits, BakerInterface). Three aspects of that effort seem worth recording.

*(a) The digit dictionary.*Mathlib provides both Nat.digits (the digit list) and Nat.testBit (bit access), but no bridge between them—and the two are needed at opposite ends of the argument. Runs, blocks and periodic windows are naturally statements about testBit, whereas s 2 s_{2} is naturally a sum over Nat.digits 2. ForMathlib/Data/Nat/BinaryDigits.lean supplies the missing dictionary: peeling a single bit or a whole p p -block off a remainder ( mod_two_pow_succ, mod_two_pow_add), collapsing a constant run ( mod_two_pow_eq_of_testBit_eq_false and its all-ones companion), and sum_digits_two_eq_sum_testBit, which identifies the digit-list sum with ∑ i < k bit i ​ ( n) \sum_{i<k}\mathrm{bit}_{i}(n) whenever n < 2 k n<2^{k}. A second dictionary, TH/BakerInterface.lean, computes the Baker–Wüstholz modified height over ℚ \mathbb{Q}; the identity h ′ ​ ( 2) = 1 h^{\prime}(2)=1 recorded in Section 2 is mh_two there.

*(b) Stewart’s counting is a lemma, not a pattern.*The pigeonhole endgame is stated once and instantiated three times. windowCount_lower_bound takes the counting function Q: ℕ → ℕ Q\colon\mathbb{N}\to\mathbb{N} as a parameter and the gap principle as a *hypothesis*—the implication “ θ \theta clears the threshold ⇒ ⌊ log θ ⁡ M ⌋ ≤ Q ⁡ ( m) \Rightarrow\lfloor\log_{\theta}M\rfloor\leq Q(m) ”—and returns Q ⁡ ( m) ≥ log ⁡ m / ( log ⁡ log ⁡ m + C) − 1 Q(m)\geq\log m/(\log\log m+C)-1. Because the transcendence input sits entirely inside that hypothesis, the lemma’s own axiom footprint is std3: no Baker content at all. Theorem 1.2 is its instantiation at Q ⁡ ( m) = s 2 ​ ( 3 m) Q(m)=s_{2}(3^{m}), Theorem 1.3 at Q ⁡ ( m) = T ⁡ ( 3 m) Q(m)=T(3^{m}), and Theorem A at Q ⁡ ( m) = B p ​ ( 3 m) + 1 Q(m)=B_{p}(3^{m})+1 through the variant windowCount_lower_bound_gen, which abstracts the coefficient κ \kappa as well. This is the formal counterpart of Remark 3.1: one counting argument, three consumers, and the [BW93] dependency entering at exactly one point in each.

The step that informal exposition compresses into “the windows inject into the break set” is the most laborious part of the whole file. In Lean it is a family of existentials, one per window, discharged by choose into a function j ↦ i j j\mapsto i_{j}; a strict antitonicity lemma, a < b ⇒ i b < i a a<b\Rightarrow i_{b}<i_{a}, read off the window geometry by omega; injectivity by trichotomy; and finally Finset.card_le_card_of_injOn against the filtered Finset.range M M that *defines*the counter. Steps (W1)–(W4) of Section 3 are a transcription of that block. Theorem 1.3 needs one further discrete step, exists_transition: a window holding both a set and a clear bit holds two adjacent unequal bits.

*(c) The rational instance simplifies the classical proofs.*Two steps of [Ste80] turn out to be unnecessary once the recurrence is u n = 3 n u_{n}=3^{n} and the base is 2 2. Stewart’s degenerate case Λ = 0 \Lambda=0 is excluded by parity—the low part A 2 A_{2} of 3 m 3^{m} is odd, hence nonzero, so 3 m > A 1 ​ 2 y 3^{m}>A_{1}2^{y} strictly—which removes the appeal to his Lemma 2 (Loxton–van der Poorten) and to the irrationality of log ⁡ 2 / log ⁡ 3 \log 2/\log 3; and the one-sided estimate log ⁡ ( 1 + u) ≤ u \log(1+u)\leq u replaces his inequality (10), removing both of his “sufficiently large” conditions, so the formalized bound holds for every m ≥ 2 m\geq 2 rather than eventually. That parity observation, transplanted from constant runs to periodic ones, is precisely Lemma 2.5 of this paper. In the same spirit Lemma 4.1 is proved by determinism propagation rather than through Fine–Wilf, which the classical route uses: this keeps it self-contained and, as Section 5 notes, alphabet-general.

### A.2. Statement index

*Reviewed results and cited inputs ( § ​ 1.1, § ​ 2) (\lx@sectionsign\ref{sub:known},\lx@sectionsign\ref{sec:tools}).*

Statement | Lean identifier | File | Status |

Def. 1.1 | transitionCount | Defs | def |

Thm. 1.2 | stewart_digitSum_three_pow | StewartDigits | std3 + [BW93] |

Thm. 1.3 | transitionCount_three_pow_lower | Transitions | std3 + [BW93] |

— | transitionCount_three_pow_tendsto_atTop | Transitions | std3 + [BW93] |

Thm. 1.4 | DH.three_pow_three_binary_digits | DimitrovHowe | cited axiom [DH23] |

Thm. 1.5 | digitSum_three_pow_le_two | SparseSide | std3 |

— | digitSum_three_pow_eq_one/_two | SparseSide | std3 |

— | digitSum_three_pow_eq_three | SparseSide | std3 + [DH23] |

Thm. 2.1 | BakerWustholz.linearForms_logs | BakerWustholz | cited axiom [BW93] |

— | gap_bound_ones | GapPrinciples | std3 + [BW93] |

— | windowCount_lower_bound | GapPrinciples | std3 |

*New results and their tools ( § ​ 2 𝐶𝐿𝑂𝑆𝐸 (\lx@sectionsign\ref{sec:tools} – 𝑂𝑃𝐸𝑁 § ​ 4) \lx@sectionsign\ref{sec:complexity}).*

Statement | Lean identifier | File | Status |

Def. 1.1 | breakCount | Aperiodicity | def |

Lem. 2.3 | Nat.periodic_mod_identity | BinaryDigits | std3 |

— | Nat.periodic_chunk_eq ( 2.1) | BinaryDigits | std3 |

— | Nat.mod_two_pow_add ( 2.2) | BinaryDigits | std3 |

Lem. 2.5 | gap_principle ( hEr_ne) | GapPrinciples | std3, inline |

Lem. 2.7 | gap_principle | GapPrinciples | std3 + [BW93] |

Prop. 2.9 | windowCount_lower_bound_gen | GapPrinciples | std3 |

Lem. 2.10 | tendsto_atTop_of_lower_bound | GapPrinciples | std3 |

Thm. A | breakCount_three_pow_lower | Aperiodicity | std3 + [BW93] |

— | breakCount_three_pow_tendsto_atTop | Aperiodicity | std3 + [BW93] |

— | subwordComplexity | SubwordComplexity | def |

Lem. 4.1 | finite_morse_hedlund | SubwordComplexity | std3 |

Lem. 4.2 | log_le_of_lowComplexity | Complexity | std3 + [BW93] |

Thm. B | three_pow_complexity_ge | Complexity | std3 + [BW93] |

The sanity witnesses T ⁡ ( 243) = 2 T(243)=2 (three blocks), s 2 ​ ( 243) = 6 s_{2}(243)=6, s 2 ​ ( 27) = 4 s_{2}(27)=4 and s 2 ​ ( 81) = 3 s_{2}(81)=3 are verified by decision procedures ( transitionCount_three_pow_five, digitSum_three_pow_five, digitSum_three_pow_three, digitSum_three_pow_four).

## References

- [BW93] A. Baker, G. Wüstholz, *Logarithmic forms and group varieties*, J. reine angew. Math. 442 (1993), 19–62.
- [BFN93] R. Blecksmith, M. Filaseta, C. Nicol, *A result on the digits of a n a^{n}*, Acta Arith. 64 (1993), 331–339.
- [BK17] Y. Bugeaud, H. Kaneko, *On the digital representation of smooth numbers*, arXiv:1704.00432 (2017).
- [CdL00] A. Carpi, A. de Luca, *Special factors, periodicity, and an application to Sturmian words*, Acta Inform. 36 (2000), 983–1006.
- [DH23] V. S. Dimitrov, E. W. Howe, *Powers of 3 with few nonzero bits and a conjecture of Erdős*, arXiv:2105.06440v4 (2023).
- [Lau08] M. Laurent, *Linear forms in two logarithms and interpolation determinants II*, Acta Arith. 133 (2008), 325–348.
- [Mat00] E. M. Matveev, *An explicit lower bound for a homogeneous rational linear form in the logarithms of algebraic numbers. II*, Izv. Math. 64 (2000), 1217–1269.
- [MH38] M. Morse, G. A. Hedlund, *Symbolic dynamics*, Amer. J. Math. 60 (1938), 815–866.
- [MV24] M. Mignotte, P. Voutier, *A kit for linear forms in three logarithms*, with an appendix by M. Laurent, Math. Comp. (2024); arXiv:2205.08899.
- [Rhi87] G. Rhin, *Approximants de Padé et mesures effectives d’irrationalité*, Séminaire de Théorie des Nombres, Paris 1985–86, Progr. Math. 71, Birkhäuser, Boston, 1987, 155–164.
- [RS26] R. Stephan, *Superlinear complexity of the ( 3 / 2) n (3/2)^{n} steering word*, arXiv:2607.11648v2 (2026).
- [Ste80] C. L. Stewart, *On the representation of an integer in two different bases*, J. reine angew. Math. 319 (1980), 63–72.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
