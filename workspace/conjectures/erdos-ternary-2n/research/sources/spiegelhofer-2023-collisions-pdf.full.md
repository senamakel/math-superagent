<!-- source: https://arxiv.org/html/2105.11173v2 | converted from HTML -->

Collisions of digit sums in bases 2 and 3

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2105.11173v2 [math.NT] 20 Apr 2022

# Collisions of digit sums in bases 2 2 and 3 3

Lukas Spiegelhofer Note: Supported by the FWF-ANR project ArithRand (grant numbers I4945-N and ANR-20-CE91-0006). Affiliation: Montanuniversität Leoben, Austria

Dedicated to Jean-Marc Deshouillers on the occasion of his 75th birthday

###### Abstract

We prove a folklore conjecture concerning the sum-of-digits functions in bases two and three: there are infinitely many positive integers n n such that the sum of the binary digits of n n equals the sum of the ternary digits of n n.

† † footnotetext: *2020 Mathematics Subject Classification.*Primary: 11A63, 60F10; Secondary: 11B25, 11B50 † † footnotetext: *Key words and phrases.*sum-of-digits function, digital expansions in different bases

## 1 Introduction and main result

Representations of the same number x x in two or more multiplicatively independent integer bases apparently look very different. This topic is far from being understood, and the relation of the base- q 1 q_{1} and the base- q 2 q_{2} expansion to each other is a source of difficult problems.

The base- q q expansion is intimately connected to powers of q q. In order to understand the relation of different bases q 1 q_{1} and q 2 q_{2} to each other better we consider, as a start, the arrangement of powers of 2 2 and 3 3. Assume that the set containing all powers of two and three (with nonnegative exponents) is sorted in ascending order:

 | ( a n) n ≥ 0 = ( 1, 2, 3, 4, 8, 9, 16, 27, 32, 64, 81, 128, 243, 256, 512, 729, 1024, …) (a_{n})_{n\geq 0}=(1,2,3,4,8,9,16,27,32,64,81,128,243,256,512,729,1024,\ldots) |  |

(this is sequence A006899 in Sloane’s OEIS [54]). In what manner are the powers of two and three interleaved? Taking logarithms, we see that the answer to this question is encoded in the Sturmian word

 | w = ( ⌊ ( n + 1) ​ α ⌋ − ⌊ n ​ α ⌋) n ≥ 0, w=\bigl(\lfloor(n+1)\alpha\rfloor-\lfloor n\alpha\rfloor\bigr)_{n\geq 0}, |  |

where α = log ⁡ 3 / log ⁡ 2 = log 2 ⁡ ( 3) \alpha=\log 3/\log 2=\log_{2}(3), as follows: start with 3 0 = 1 3^{0}=1, append the first w 0 = 1 w_{0}=1 powers of two — that is, the integer 2 2 — append 3 1 3^{1}, then w 1 = 2 w_{1}=2 powers of two, followed by 3 2 3^{2} and w 2 = 1 w_{2}=1 powers of two, and so on. Our question is therefore equivalent to understanding the *continued fraction expansion*of α \alpha (consult, for example, Berthé [7] for an explanation of this connection). However, it is not even known whether the sequence of partial quotients of α \alpha is bounded, that is, whether α \alpha is *badly approximable*; any system in this sequence has yet to be found. The number α \alpha is transcendental by the Gelfond–Schneider theorem [23, 24]; by Baker’s theorem [4, 5, 6] we obtain

 | | log ⁡ 3 log ⁡ 2 − p q | ≥ c q ρ \left\lvert\frac{\log 3}{\log 2}-\frac{p}{q}\right\rvert\geq\frac{c}{q^{\rho}} |  |

for all integers q > 0 q>0 and p p and some effective positive constants c c and ρ \rho. More precisely, a bound for the *irrationality measure*μ ⁡ ( α) \mu(\alpha) of α \alpha, which is the infimum of ρ \rho for which there exists c c such that this estimate holds for all p, q p,q, was given by Rhin [48, Equation (8)]: we have μ ⁡ ( α) ≤ 8.616 \mu(\alpha)\leq 8.616. Also, Wu and Wang [60] obtained the bound μ ⁡ ( log ⁡ 3) ≤ 5.1163051 \mu(\log 3)\leq 5.1163051. Note that badly approximable numbers have irrationality measure 2 2. We would also like to mention the interesting blog entry by Tao 1 1 1 https://terrytao.wordpress.com/2011/08/21/hilberts-seventh-problem-and-powers-of-2-and-3/ on the topic.

In view of the above problem we have to expect major difficulties when we try to mix different bases. In this context, the following unsolved conjecture of Furstenberg [22] is of interest, concerning *multiplicatively independent*integer bases p, q ≥ 2 p,q\geq 2 (that is, such that p k ≠ q ℓ p^{k}\neq q^{\ell} for all k, ℓ ≥ 1 k,\ell\geq 1): define

 | O a ​ ( x) ≔ { a k ​ x mod 1: k ∈ ℕ } O_{a}(x)\coloneqq\bigl\{a^{k}x\bmod 1:k\in\mathbb{N}\bigr\} |  |

and let dim H ( A) \dim_{H}(A) be the Hausdorff dimension of a set A ⊆ [0, 1] A\subseteq[0,1]. Then

 | dim H ( O p ​ ( x) ¯) + dim H ( O q ​ ( x) ¯) ≥ 1 \dim_{H}\bigl(\overline{O_{p}(x)}\bigr)+\dim_{H}\bigl(\overline{O_{q}(x)}\bigr)\geq 1 |  | (1) |

for all irrational x ∈ [0, 1] x\in[0,1]. Furstenberg’s conjecture underlines the idea stated before: different bases should produce very different representations of the same number. We note the papers [53, 59] for recent progress on this conjecture, and the recent preprint [1] by Adamczewski and Faverjon, where related independence results can be found.

The related topic of studying the base- p p expansion of powers of q q is very difficult and has attracted the attention of many researchers; we note the recent preprint [27] by Kerr, Mérai, and Shparlinski and the references contained therein. Erdős [20] conjectured that the only powers of two having no digit 𝟸 \mathtt{2} in its ternary expansion are 1, 4 1,4, and 256 256 (see also Lagarias [29]). This conjecture is open, and Erdős wrote “[…] as far as I can see, there is no method at our disposal to attack this conjecture” [20]. Meanwhile, there is a close connection to to Erdős’ *squarefree conjecture*[21], stating that the central binomial coefficient ( 2 ​ n n) \binom{2n}{n} is never squarefree for n ≥ 5 n\geq 5. The latter conjecture was proved for all large n n by Sárközy [49], and solved completely by Granville and Ramaré [26]. The connection between these two conjectures can be understood by considering the identities

 | ν 2 ​ ( ( 2 ​ n n)) = s 2 ​ ( n) and ν 3 ​ ( ( 2 ​ n n)) = s 3 ​ ( n) − s 3 ​ ( 2 ​ n) 2, \nu_{2}\left(\binom{2n}{n}\right)=s_{2}(n)\quad\text{and}\quad\nu_{3}\left(\binom{2n}{n}\right)=s_{3}(n)-\frac{s_{3}(2n)}{2}, |  |

where s q s_{q} is the sum-of-digits function in base q q, and ν p \nu_{p} is the p p -adic valuation of an integer ≥ 1 \geq 1 (with p p prime). That is, ( 2 ​ n n) \binom{2n}{n} is divisible by the square 4 4 if n ≥ 1 n\geq 1 is not a power of two, and so a stronger form of the (already proved) squarefree conjecture would follow from a proof of the conjecture that

 | s 3 ​ ( 2 k) − s 3 ​ ( 2 k + 1) / 2 ≥ 2 for ​ k ≥ 9. s_{3}(2^{k})-s_{3}(2^{k+1})/2\geq 2\quad\text{for }k\geq 9. |  | (2) |

In fact, ( 2) implies 4 | ( 2 ​ n n) 4\mid\binom{2n}{n} or 9 | ( 2 ​ n n) 9\mid\binom{2n}{n} for each n ≥ 257 n\geq 257, while ( 512 256) \binom{512}{256} is divisible by neither 4 4 nor 3 3. Equation ( 2) in turn would follow if we could prove that the integer 2 k 2^{k} contains at least two digits equal to 𝟸 \mathtt{2} in ternary for k ≥ 9 k\geq 9: in this case at least two carries appear in the addition 2 k + 2 k 2^{k}+2^{k} in ternary. We also would like to note the recent preprint [13] by Dimitrov and Howe on this topic.

The main objects in this paper are the sum-of-digits functions s 2 s_{2} and s 3 s_{3}. For a nonnegative integer n n and a base q q, the integer s q ​ ( n) s_{q}(n) is in fact the minimal number of powers of q q needed to represent n n as their sum (which can be proved using that the q q -ary expansion is the lexicographically largest representation of n n as a sum of powers of q q).

Senge and Straus [52] proved the important theorem that for coprime integers p, q ≥ 2 p,q\geq 2 and arbitrary c > 0 c>0, there are only finitely many integers n ≥ 0 n\geq 0 such that

 | s p ​ ( n) ≤ c and s q ​ ( n) ≤ c. s_{p}(n)\leq c\quad\text{and}\quad s_{q}(n)\leq c. |  | (3) |

This statement is, at least heuristically, close to Furstenberg’s conjecture ( 1): digital expansions of a number in multiplicatively independent bases usually cannot be simple simultaneously. Extensions of ( 3) were proved by Stewart [58], Mignotte [42], Schlickewei [50, 51], Pethő–Tichy [47], and Ziegler [61]. See also [9, 10, 30] for related results.

Gelfond [25] proposed to prove that

 | #⁡ { n ≤ x: s q 1 ​ ( n) ≡ ℓ 1 mod m 1 ​ and ​ s q 2 ​ ( n) ≡ ℓ 2 mod m 2 } = x m 1 ​ m 2 + 𝒪 ⁡ ( x δ) \#\bigl\{n\leq x:s_{q_{1}}(n)\equiv\ell_{1}\bmod m_{1}\text{ and }s_{q_{2}}(n)\equiv\ell_{2}\bmod m_{2}\bigr\}=\frac{x}{m_{1}m_{2}}+\LandauO\bigl(x^{\delta}\bigr) |  | (4) |

for some δ < 1 \delta<1, where q 1, q 2 ≥ 2 q_{1},q_{2}\geq 2 are coprime bases, m 1, m 2 m_{1},m_{2} are integers satisfying gcd ⁡ ( m 1, q 1 − 1) = gcd ⁡ ( m 2, q 2 − 1) = 1 \gcd(m_{1},q_{1}-1)=\gcd(m_{2},q_{2}-1)=1, and ℓ 1, ℓ 2 ∈ ℤ \ell_{1},\ell_{2}\in\mathbb{Z}. A weak error term o ⁡ ( 1) o(1) for this problem was proved by Bésineau [8], while the full statement was obtained by D.-H. Kim [28].

Drmota [14, Theorem 4] proved (among other things) an asymptotic formula for the proportion

 | 1 x #{ n < x: s q 1 ( n) = k 1, s q 2 ( n) = k 2 }, \frac{1}{x}\#\bigl\{n<x:s_{q_{1}}(n)=k_{1},s_{q_{2}}(n)=k_{2}\bigr\}, |  | (5) |

where q 1, q 2 ≥ 2 q_{1},q_{2}\geq 2 are coprime bases, with an error term ( log ⁡ x) − 1 (\log x)^{-1}. This may be called a *local limit theorem*for the joint sum-of-digits function n ↦ ( s p ​ ( n), s q ​ ( n)) n\mapsto(s_{p}(n),s_{q}(n)). Note that Bésineau’s result follows as a special case, as the two sum-of-digits functions on [0, x) [0,x) are mostly found close to their expected values, compare ( 58) below.

We also wish to note the recent paper by Drmota, Mauduit, and Rivat [17], who proved a result on the sum of digits of prime numbers in two different bases.

The starting point for the present paper is the article [12] by Deshouillers, Habsieger, Landreau, and Laishram.

“[…] it seems to be unknown whether there are infinitely many integers n n for which s 2 ​ ( n) = s 3 ​ ( n) s_{2}(n)=s_{3}(n) or even for which | s 2 ​ ( n) − s 3 ​ ( n) | \lvert s_{2}(n)-s_{3}(n)\rvert is significantly small.” [12]

They prove the following result.

###### Theorem.

For sufficiently large N N, we have

 | #⁡ { n ≤ N: | s 3 ​ ( n) − s 2 ​ ( n) | ≤ 0.1457205 ​ log ⁡ n } > N 0.970359. \#\bigl\{n\leq N:\lvert s_{3}(n)-s_{2}(n)\rvert\leq 0.1457205\log n\bigr\}>N^{0.970359}. |  |

Note that the difference s 3 ​ ( n) − s 2 ​ ( n) s_{3}(n)-s_{2}(n) is expected to have a value around C ​ log ⁡ n C\log n, where

 | C = 1 log ⁡ 3 − 1 log ⁡ 4 = 0.18889 ​ …; C=\frac{1}{\log 3}-\frac{1}{\log 4}=0.18889\ldots; |  |

by the above theorem there exist indeed many integers n n such the difference | s 2 ​ ( n) − s 3 ​ ( n) | \lvert s_{2}(n)-s_{3}(n)\rvert is “significantly small”.

This result was extended by La Bretèche, Stoll, and Tenenbaum [11], who proved in particular that

 | { s p ​ ( n) / s q ​ ( n): n ≥ 1 } \bigl\{s_{p}(n)/s_{q}(n):n\geq 1\} |  | (6) |

is dense in ℝ + \mathbb{R}^{+} for all multiplicatively independent integer bases p p, q ≥ 2 q\geq 2.

We also wish to note the papers [40] by Mauduit and Sárközy, and by Mauduit, Pomerance, and Sárközy [35]. In these papers, integers with a fixed sum of digits and corresponding asymptotic formulas are studied, and possible extensions to several bases are addressed.

Let us call a natural number n n such that s 2 ​ ( n) = s 3 ​ ( n) s_{2}(n)=s_{3}(n) a *collision*(of s 2 s_{2} and s 3 s_{3}). The question on the infinitude of collisions, mentioned in [12], is not a new one. M. Drmota (private communication to the author) received a hand-written letter from A. Hildebrand more than twenty years ago, in which the very same problem was presented.

In the present paper, we give a definite answer to this question.

###### Theorem 1.1.

There exist infinitely many nonnegative integers n n such that

 | s 2 ​ ( n) = s 3 ​ ( n). s_{2}(n)=s_{3}(n). |  | (7) |

More precisely, for all δ > 0 \delta>0 we have

 | #⁡ { n < N: s 2 ​ ( n) = s 3 ​ ( n) } ≫ N log ⁡ 3 log ⁡ 4 − δ, \#\bigl\{n<N:s_{2}(n)=s_{3}(n)\bigr\}\gg N^{\frac{\log 3}{\log 4}-\delta}, |  | (8) |

where the implied constant may depend on δ \delta. Note that log ⁡ 3 / log ⁡ 4 = 0.792 ​ … \log 3/\log 4=0.792\ldots.

The difficulty in proving this theorem lies in the separation of the values of s 2 ​ ( n) s_{2}(n) and s 3 ​ ( n) s_{3}(n). The sum-of-digits functions can be thought of as a sum of independent, identically distributed random variables, and they concentrate (according to Hoeffding’s inequality, for example) around the values 1 2 ​ log 2 ​ N \frac{1}{2}\log_{2}N and log 3 ⁡ N \log_{3}N respectively, where 0 ≤ n < N 0\leq n<N. More precisely, the variances are of order log ⁡ N \log N, and the tails of these distributions decay as least as fast as exp ( − C ( x − μ) 2 / σ 2) \exp(-C(x-\mu)^{2}/\sigma^{2}), where μ \mu is the expected value, and σ 2 \sigma^{2} the variance. Since the gap ( 1 / log ⁡ 3 − 1 / log ⁡ 4) ​ log ⁡ N (1/\log 3-1/\log 4)\log N comprises ≍ ( log ⁡ N) 1 / 2 \asymp(\log N)^{1/2} standard deviations, we can only expect a number ≪ N δ \ll N^{\delta} of collisions, where δ < 1 \delta<1 is some constant. In the light of this argument, we see that our result cannot be too far from the true number of collisions.

The increasing sequence 𝔰 2, 3 \mathfrak{s}_{2,3} of nonnegative integers n n such that s 2 ​ ( n) = s 3 ​ ( n) s_{2}(n)=s_{3}(n) is listed as entry A037301 in the OEIS [54]. The question whether this sequence is infinite had to remain open there. The first few collisions are as follows:

 | n ​ in binary 0 1 110 111 1010 1011 1100 1101 10010 10011 10101 100100 n ​ in ternary 0 1 20 21 101 102 110 111 200 201 210 1100 n ​ in decimal 0 1 6 7 10 11 12 13 18 19 21 36. \begin{array}[]{rrrrrrrrrrrrrr@{\hskip 0.25mm}l}n\mbox{ in}&\mbox{binary}&0&1&110&111&1010&1011&1100&1101&10010&10011&10101&100100\hskip 0.7113pt\\ n\mbox{ in}&\mbox{ternary}&0&1&20&21&101&102&110&111&200&201&210&1100\hskip 0.7113pt\\ n\mbox{ in}&\mbox{decimal}&0&1&6&7&10&11&12&13&18&19&21&36\hskip 0.7113pt&.\end{array} |  |

###### Remarks.

Note the subsequence ( 10, 11, 12, 13) (10,11,12,13); contiguous subsequences of ℕ \mathbb{N} of length greater than four do not appear in 𝔰 2, 3 \mathfrak{s}_{2,3}, since s 3 s_{3} on such a subsequence contains two consecutive up-steps, while s 2 s_{2} decreases or stays constant after one up-step. We expect that it is possible to extend our proof to arbitrary *patterns*in 𝔰 2, 3 \mathfrak{s}_{2,3}: for example, we expect that there are infinitely many n n such that

 | s 2 ​ ( n + v) = s 3 ​ ( n + v) for v ∈ { 0, 1, 2, 3 }, s_{2}(n+v)=s_{3}(n+v)\quad\text{for}\quad v\in\{0,1,2,3\}, |  | (9) |

and infinitely many n n (the integer n = 13 n=13 is an example) such that

 | { v ∈ { 0, …, 23 }: s 2 ​ ( n + v) = s 3 ​ ( n + v) } = { 0, 5, 6, 8, 23 }. \bigl\{v\in\{0,\ldots,23\}:s_{2}(n+v)=s_{3}(n+v)\bigr\}=\{0,5,6,8,23\}. |  | (10) |

More generally, every pattern that appears at all should appear infinitely often in 𝔰 2, 3 \mathfrak{s}_{2,3}. To this end, we will have to study certain residue classes modulo 2 k ​ 3 ℓ 2^{k}3^{\ell} — note that for n ∈ ( 2 + 8 ​ ℤ) ∩ ( 1 + 9 ​ ℤ) n\in(2+8\mathbb{Z})\cap(1+9\mathbb{Z}), for example, we have s 2 ​ ( n + v) − s 3 ​ ( n + v) = c s_{2}(n+v)-s_{3}(n+v)=c for some c c and all v ∈ { 0, 1, 2, 3 } v\in\{0,1,2,3\}. The next step would be to scan these “candidate residue classes” for collisions, using our method. But residue classes of this form are used in our proof anyway, therefore we are optimistic that the main problems have already been overcome. (Note that also a suitable replacement for Proposition 2.1 below will have to be found. This proposition takes care of the parity restriction s 3 ​ ( n + t) − s 3 ​ ( n) ≡ s 3 ​ ( t) mod 2 s_{3}(n+t)-s_{3}(n)\equiv s_{3}(t)\bmod 2.)

We would like to note that our proof of Theorem 1.1 is not a constructive one. We do not give an algorithm that allows us to find integers n n such that s 2 ​ ( n) = s 3 ​ ( n) s_{2}(n)=s_{3}(n). We leave it as an open problem to find a construction method for such integers n n.

Also, it is a very interesting open problem to prove that s 2 ​ ( p) = s 3 ​ ( p) s_{2}(p)=s_{3}(p) for infinitely many prime numbers p p. We believe that this question is difficult. This guess is due to the analogy to *missing digit problems*, where sparse sets S ⊆ ℕ S\subseteq\mathbb{N} (that is, #⁡ ( S ∩ [1, N]) ≪ N δ \#(S\cap[1,N])\ll N^{\delta} for some δ < 1 \delta<1) of a similar kind are studied; Maynard [41], in an important and difficult paper, could prove that infinitely many primes excluding any given decimal digit exist. Our set S = { n: s 2 ​ ( n) = s 3 ​ ( n) } S=\{n:s_{2}(n)=s_{3}(n)\} is even less understood than the set of integers in Maynard’s result, hence our scepticism.

Plan of the paper.

The main body of the paper concerns the proof of the auxiliary statement, Proposition 2.1 below, which directly leads to the main theorem. This proof is organized into three main steps, represented by Propositions 2.2 – 2.4. After the statement of these results, in Section 2.1, we prove Proposition 2.1 and thus Theorem 1.1 from these three propositions. The three sections thereafter, Sections 2.2, 2.3, and 2.4, are dedicated to the proofs of the three main steps. At the end of the paper, we present (mostly difficult) research questions.

###### Notation.

The symbol log \log denotes the natural logarithm, and log a = 1 log ⁡ a ​ log \log_{a}=\frac{1}{\log a}\log is the logarithm in base a > 1 a>1. We use Landau notation, employing the symbols 𝒪 \LandauO, ≪ \ll, and o o. The symbol f ⁡ ( n) ≍ g ⁡ ( n) f(n)\asymp g(n) abbreviates the statement ( f ⁡ ( n) ≪ g ⁡ ( n) CLOSE \bigl(f(n)\ll g(n) and OPEN g ⁡ ( n) ≪ f ⁡ ( n)) g(n)\ll f(n)\bigr), while f ⁡ ( n) ∼ g ⁡ ( n) f(n)\sim g(n) means that f ⁡ ( n) / g ⁡ ( n) f(n)/g(n) converges to 1 1 as n → ∞ n\rightarrow\infty. We also use the exponential e ⁡ ( x) = exp ⁡ ( 2 ​ π ​ ix) \e(x)=\exp(2\pi ix). For M ≥ 0 M\geq 0, the statement “ a a is M M -close to b b ” means | a − b | ≤ M \lvert a-b\rvert\leq M.

## 2 Proofs

Our main theorem follows from the following proposition.

###### Proposition 2.1.

For all δ > 0 \delta>0 the number of n < N n<N such that

 | s 2 ​ ( n) − s 3 ​ ( n) ∈ { 0, 1 } s_{2}(n)-s_{3}(n)\in\{0,1\} |  | (11) |

is bounded below by C ​ N log ⁡ 3 log ⁡ 4 − δ CN^{\frac{\log 3}{\log 4}-\delta} (where the constant C C may depend on δ \delta).

We call an integer n n such that ( 11) is satisfied an *almost-collision*.

Let N ≥ 4 N\geq 4 be an integer. We are going to find many collisions in the interval [N, 2 ​ N) [N,2N) for all large enough N N, which will prove Theorem 1.1. Let ε > 0 \varepsilon>0 be arbitrary throughout this proof. This variable is used as exponent of log ⁡ log ⁡ N \log\log N, and its value, as long as it is strictly positive, is irrelevant for our proof. For given N N, we define λ \lambda, η \eta, f f, m m, and J J as follows. Set

 | λ 0 ≔ log ⁡ N, η 0 ≔ λ 0 3 / 4, f 0 ≔ ( log ⁡ λ 0) 1 / 2 + ε, m 0 ≔ λ 0 1 / 2 / f 0, J 0 ≔ f 0 2, λ ≔ ⌊ λ 0 ⌋, η ≔ 4 ​ ⌊ η 0 / 4 ⌋, f ≔ ⌊ f 0 ⌋, m ≔ ⌊ m 0 ⌋, J ≔ ⌊ J 0 ⌋. \begin{array}[]{r@{\hskip 1mm}lr@{\hskip 1mm}lr@{\hskip 1mm}lr@{\hskip 1mm}lr@{\hskip 1mm}l}\lambda_{0}\hskip 2.84526pt&\coloneqq\log N,&\eta_{0}\hskip 2.84526pt&\coloneqq\lambda_{0}^{3/4},&f_{0}\hskip 2.84526pt&\coloneqq(\log\lambda_{0})^{1/2+\varepsilon},&m_{0}\hskip 2.84526pt&\coloneqq\lambda_{0}^{1/2}/f_{0},&J_{0}\hskip 2.84526pt&\coloneqq f_{0}^{2},\\[2.84526pt] \lambda\hskip 2.84526pt&\coloneqq\lfloor\lambda_{0}\rfloor,&\eta\hskip 2.84526pt&\coloneqq 4\lfloor\eta_{0}/4\rfloor,&f\hskip 2.84526pt&\coloneqq\lfloor f_{0}\rfloor,&m\hskip 2.84526pt&\coloneqq\lfloor m_{0}\rfloor,&J\hskip 2.84526pt&\coloneqq\lfloor J_{0}\rfloor.\end{array} |  | (12) |

We wish to give a rough and very imprecise idea of the meaning of this choice of variables. The length of a binary or ternary expansion of n ∈ [N, 2 ​ N) n\in[N,2N) is of size ≍ λ \asymp\lambda, and the standard deviation of a (binary or ternary) sum-of-digits function on [N, 2 ​ N) [N,2N) is of order ≍ ( log ⁡ N) 1 / 2 \asymp(\log N)^{1/2}. The variable m m is smaller than the standard deviation by a factor f f (the *fineness*), and taking J J steps of length m m, we cover sufficiently many standard deviations. That is, the tail (comprising deviations larger than J ​ m Jm from the expected value) is bounded by λ − D \lambda^{-D} for all D > 0 D>0 due to the presence of ε > 0 \varepsilon>0. Finally, η \eta is the ternary length of certain integers 𝔞 \mathfrak{a} and 𝔟 \mathfrak{b} that we choose freely. It is large enough to allow for differences of ternary sum-of-digits functions larger than the standard deviation ≍ λ 1 / 2 \asymp\lambda^{1/2} by any logarithmic factor ( log ⁡ λ) ρ (\log\lambda)^{\rho} (compare to ( 42)), and small enough so that a concatenation of 2 ​ J + 1 2J+1 ternary expansions of length η \eta is still much shorter than λ \lambda.

After this very informal explanation of our choice of parameters, we give a brief description of the proof. The search for collisions will consist of three main steps.

1. 1.

“Preparation”: find a residue class A ′ A^{\prime} on which f ⁡ ( n + t) − f ⁡ ( n) f(n+t)-f(n) takes prescribed, constant differences, where f ⁡ ( n) = s 2 ​ ( n) − s 3 ​ ( n) f(n)=s_{2}(n)-s_{3}(n);

2. 2.

“Rarefaction”: concentrate the values of f ⁡ ( n) f(n) into the interval [− J ​ m, J ​ m] [-Jm,Jm] by finding a rarefied and truncated arithmetic progression A ′′ ⊂ A ′ A^{\prime\prime}\subset A^{\prime}, and considering only integers n ∈ A ′′ n\in A^{\prime\prime};

3. 3.

“Fair share”: select only those n ∈ A ′′ n\in A^{\prime\prime} such that f ⁡ ( n) ∈ m ​ ℤ f(n)\in m\mathbb{Z}.

Steps 2 and 3 are used to find many values of n n from a given given residue class such that f ⁡ ( n) ∈ Q ≔ { − J ​ m, ( − J + 1) ​ m, …, J ​ m } f(n)\in Q\coloneqq\{-Jm,(-J+1)m,\ldots,Jm\}. The purpose of Step 1 is to define *in advance*a larger residue class A ′ = L + 2 ν ​ 3 β ​ ℤ A^{\prime}=L+2^{\nu}3^{\beta}\mathbb{Z} and a set 𝐝 = { d − J, d − J + 1, …, d J } \mathbf{d}=\{d_{-J},d_{-J+1},\ldots,d_{J}\} of *shifts*such that f ⁡ ( n + d j) − f ⁡ ( n) = j ​ m + ξ j f(n+d_{j})-f(n)=jm+\xi_{j} for all n ∈ A ′ n\in A^{\prime}, all j ∈ { − J, …, J } j\in\{-J,\ldots,J\}, and some ξ j ∈ { 0, 1 } \xi_{j}\in\{0,1\}. This procedure yields many n n such that f ⁡ ( n) ∈ { 0, 1 } f(n)\in\{0,1\}, by choosing for each index n n such that f ⁡ ( n) ∈ Q f(n)\in Q the appropriate shift d ⁡ ( n) ∈ 𝐝 d(n)\in\mathbf{d}. A short argument involving differences s j ​ ( n + 1) − s j ​ ( n) s_{j}(n+1)-s_{j}(n) of sum-of-digits functions on residue classes (where j ∈ { 2, 3 } j\in\{2,3\}) allows us to get rid of the unpleasant correction term ξ j \xi_{j}.

We will prove the following three propositions, corresponding to our three steps.

###### Proposition 2.2.

Let β = ( 2 ​ J + 1) ​ η + 1 \beta=(2J+1)\eta+1 and choose the integer ν ≥ 1 \nu\geq 1 minimal such that 2 ν − 1 ≥ 3 β 2^{\nu-1}\geq 3^{\beta}. Set

 | d j ≔ ( 𝟷 ( j + 1 + J) ​ η ​ 𝟶) 3 = 3 ​ 3 ( j + 1 + J) ​ η − 1 2. d_{j}\coloneqq\bigl(\mathtt{1}^{(j+1+J)\eta}\mathtt{0}\bigr)_{3}=3\frac{3^{(j+1+J)\eta}-1}{2}. |  | (13) |

There exists L ∈ { 0, …, 2 ν ​ 3 β − 1 } L\in\{0,\ldots,2^{\nu}3^{\beta}-1\} such that L ≡ 9 mod 12 L\equiv 9\bmod 12, and ξ j ∈ { 0, 1 } \xi_{j}\in\{0,1\} for − J ≤ j ≤ J -J\leq j\leq J such that

 | f ⁡ ( n + d j) − f ⁡ ( n) = j ​ m + ξ j for all ​ j ∈ { − J, …, J } ​ and all ​ n ∈ A ′ ≔ L + 2 ν ​ 3 β ​ ℕ. f(n+d_{j})-f(n)=jm+\xi_{j}\quad\text{for all }j\in\{-J,\ldots,J\}\text{ and all }n\in A^{\prime}\coloneqq L+2^{\nu}3^{\beta}\mathbb{N}. |  | (14) |

###### Proposition 2.3.

For an integer ζ ≥ 0 \zeta\geq 0, define

 | A ′′ ≔ ( L + 2 ν ​ 3 β + ζ ​ ℕ) ∩ [N, 2 ​ N) A^{\prime\prime}\coloneqq\bigl(L+2^{\nu}3^{\beta+\zeta}\mathbb{N}\bigr)\cap[N,2N) |  | (15) |

and

 | I ≔ { k ∈ ℕ: N ≤ L + 2 ν ​ 3 β + ζ ​ k < 2 ​ N }. I\coloneqq\bigl\{k\in\mathbb{N}:N\leq L+2^{\nu}3^{\beta+\zeta}k<2N\bigr\}. |  | (16) |

Here ν \nu, β \beta, and L L are given by Proposition 2.2. For all D > 0 D>0 there exists a constant C = C ⁡ ( D) C=C(D) such that the following statement holds.

 | There exists a sequence ( ζ N) N ≥ 4 \bigl(\zeta_{N}\bigr)_{N\geq 4} of nonnegative integers such that ζ N ∼ log 3 ⁡ ( N) ​ ( 1 − log ⁡ 3 / log ⁡ 4) \zeta_{N}\sim\log_{3}(N)\bigl(1-\log 3/\log 4\bigr) as N → ∞ N\rightarrow\infty, and for all N N and all but at most C ​ | I | ​ λ − D C\lvert I\rvert\lambda^{-D} integers n ∈ A ′′ n\in A^{\prime\prime}, the quantity f ⁡ ( n) f(n) is J ​ m Jm -close to 0 0. |  | (17) |

Note that I I and A ′′ A^{\prime\prime} in this statement depend on ζ = ζ N \zeta=\zeta_{N}, which in turn depends on N N.

###### Proposition 2.4.

Using the set A ′′ A^{\prime\prime} from ( 15), we set

 | P ≔ #⁡ { n ∈ A ′′: f ⁡ ( n) ∈ m ​ ℤ }. P\coloneqq\#\bigl\{n\in A^{\prime\prime}:f(n)\in m\mathbb{Z}\bigr\}. |  | (18) |

As N → ∞ N\rightarrow\infty, we have

 | P = | I | m ​ ( 1 + o ​ ( 1)). P=\frac{\lvert I\rvert}{m}\bigl(1+o(1)\bigr). |  | (19) |

That is, the residue class m ​ ℤ m\mathbb{Z} receives the expected ratio λ − 1 / 2 ( log λ) 1 / 2 + ε \lambda^{-1/2}(\log\lambda)^{1/2+\varepsilon} of the values of f ⁡ ( n) = s 2 ​ ( n) − s 3 ​ ( n) f(n)=s_{2}(n)-s_{3}(n) along the finite arithmetic progression A ′′ A^{\prime\prime} defined in ( 15).

### 2.1 Deriving Theorem 1.1 from Propositions 2.2 – 2.4

The expected number P P of integers n ∈ A ′′ n\in A^{\prime\prime} such that f ⁡ ( n) ∈ m ​ ℤ f(n)\in m\mathbb{Z} is given by Proposition 2.4. At the same time, Proposition 2.3 states that for all D > 0 D>0, f ⁡ ( n) f(n) lies in the interval [− J ​ m, J ​ m] [-Jm,Jm] for | I | ​ ( 1 − 𝒪 ⁡ ( λ − D)) \lvert I\rvert(1-\LandauO(\lambda^{-D})) many integers n ∈ A ′′ n\in A^{\prime\prime} (where the implied constant depends on D D). Note that for D > 1 / 2 D>1/2 this error term is of smaller magnitude than P P. Consequently, any choice D > 1 / 2 D>1/2 will yield many integers n ∈ A ′′ n\in A^{\prime\prime} such that s 2 ​ ( n) − s 3 ​ ( n) = j ​ m s_{2}(n)-s_{3}(n)=jm for some j ∈ { − J, …, J } j\in\{-J,\ldots,J\}. By ( 14) the integer n ′ = n + d − j n^{\prime}=n+d_{-j} satisfies s 2 ​ ( n ′) − s 3 ​ ( n ′) ∈ { 0, 1 } s_{2}(n^{\prime})-s_{3}(n^{\prime})\in\{0,1\}. Noting that ζ ≍ log ⁡ N \zeta\asymp\log N and J ​ η ≪ ( log ⁡ N) 3 / 4 ​ ( log ⁡ log ⁡ N) 1 + 2 ​ ε J\eta\ll(\log N)^{3/4}(\log\log N)^{1+2\varepsilon}, we see that the shifts d j d_{j} are asymptotically smaller than the common difference 2 ν ​ 3 β + ζ 2^{\nu}3^{\beta+\zeta} of A ′′ A^{\prime\prime}. Varying N N, we get an almost-collision (as in Proposition 2.1) in each large enough interval [N, 2 ​ N) [N,2N) and thus the qualitative statement in Theorem 1.1.

Considering the asymptotic sizes of ν \nu, β \beta, and ζ \zeta, it is easy to see that the interval I I defined in ( 16) is in fact of size ≫ N log ⁡ 3 / log ⁡ 4 − δ \gg N^{\log 3/\log 4-\delta} for all δ > 0 \delta>0. Most k ∈ I k\in I yield a value f ~ ​ ( k) = f ⁡ ( L + 2 ν ​ 3 β + ζ ​ k) ∈ [− J ​ m, J ​ m] \tilde{f}(k)=f(L+2^{\nu}3^{\beta+\zeta}k)\in[-Jm,Jm] by ( 17), and the expected proportion ∼ m − 1 ≫ ( log N) − 1 / 2 \sim m^{-1}\gg(\log N)^{-1/2} of them satisfy f ~ ​ ( k) ∈ m ​ ℤ \tilde{f}(k)\in m\mathbb{Z}, see ( 19). These k k yield pairwise different values k + d j ⁡ ( k) k+d_{j(k)} as before. Here the integer j = j ⁡ ( k) j=j(k) is chosen suitably from { − J, …, J } \{-J,\ldots,J\} in order to force an almost-collision.

Let δ > 0 \delta>0 be given and set A = log ⁡ 3 / log ⁡ 4 − δ A=\log 3/\log 4-\delta. If the number of n < N n<N such that s 2 ​ ( n) − s 3 ​ ( n) = 0 s_{2}(n)-s_{3}(n)=0 and n ≡ 9 mod 12 n\equiv 9\bmod 12 is ≫ N A \gg N^{A}, there is nothing to be done. Otherwise, we note that n ≡ 9 mod 12 n\equiv 9\bmod 12 is equivalent to ( n ≡ 0 mod 3 CLOSE \bigl(n\equiv 0\bmod 3 and OPEN n ≡ 1 mod 4) n\equiv 1\bmod 4\bigr), therefore s 3 ​ ( n + 1) = s 3 ​ ( n) + 1 s_{3}(n+1)=s_{3}(n)+1 and s 2 ​ ( n + 1) = s 2 ​ ( n) s_{2}(n+1)=s_{2}(n). The existence of a number ≫ N A \gg N^{A} of solutions of s 2 ​ ( n) − s 3 ​ ( n) = 1 s_{2}(n)-s_{3}(n)=1 on ( 9 + 12 ​ ℤ) ∩ [N, 2 ​ N) (9+12\mathbb{Z})\cap[N,2N) therefore implies a number ≫ N A \gg N^{A} of collisions on ( 10 + 12 ​ ℤ) ∩ [N, 2 ​ N) (10+12\mathbb{Z})\cap[N,2N). This establishes ( 8) and completes the proof. ∎

###### Remark.

In the last step towards finding almost-collisions — namely, choosing j ∈ { − J, …, J } j\in\{-J,\ldots,J\} suitably — the “element of non-constructiveness” in our argument is clearly visible. Currently we do not have any control over the choice of j j.

In order to prove Theorem 1.1, it is sufficient to establish Propositions 2.2 – 2.4.

### 2.2 Constant differences of sum-of-digits functions — proof of Proposition 2.2

We will use *blocks*in ternary, whose lengths are given by the integer η \eta. Let us choose nonnegative integers d − J, d − J + 1, …, d J d_{-J},d_{-J+1},\ldots,d_{J} by concatenating such blocks of ternary digits. Set

 | 𝔟 ≔ ( 𝟷 η) 3 = 3 η − 1 2, \mathfrak{b}\coloneqq\bigl(\mathtt{1}^{\eta}\bigr)_{3}=\frac{3^{\eta}-1}{2}, |  |

where 𝟷 η \mathtt{1}^{\eta} denotes η \eta -fold repetition of the digit 𝟷 \mathtt{1}. Define d j d_{j}, for − J ≤ j ≤ J -J\leq j\leq J, by ( j + 1 + J) (j+1+J) -fold concatenation of 𝟷 η \mathtt{1}^{\eta}, with 𝟶 \mathtt{0} appended at the right, as in ( 13). The emphasis on “blocks of length η \eta ” will become clear in the construction of the integers k j k_{j} further down (see ( 46)). Since the ternary expansion of d j d_{j} consists of blocks 𝟷𝟷𝟷𝟷 \mathtt{1}\mathtt{1}\mathtt{1}\mathtt{1} and ends with 𝟶 \mathtt{0}, we have d j ≡ 0 mod 12 d_{j}\equiv 0\bmod 12 (note that 4 | ( 𝟷𝟷𝟷𝟷) 3 = 40 4\mid(\mathtt{1}\mathtt{1}\mathtt{1}\mathtt{1})_{3}=40). Choose the integer ν ≥ 1 \nu\geq 1 minimal so that

 | 2 ν − 1 ≥ 3 ( 2 ​ J + 1) ​ η + 1. 2^{\nu-1}\geq 3^{(2J+1)\eta+1}. |  | (20) |

In particular,

 | d j < 2 ν − 1. d_{j}<2^{\nu-1}. |  | (21) |

The next important step consists in choosing a certain integer a ∈ { 1, …, 2 ν − 1 − 1 } a\in\{1,\ldots,2^{\nu-1}-1\}; its meaning will become clear in a moment. The size restrictions imply d j + a < 2 ν d_{j}+a<2^{\nu} for all j ∈ { − J, …, J } j\in\{-J,\ldots,J\}. This means in particular that no carry from the ( ν − 1) (\nu-1) th to the ν \nu th digit occurs in the addition d j + a d_{j}+a, which implies the simple but important identity

 | s 2 ​ ( 2 ν ​ n + a + d j) − s 2 ​ ( 2 ν ​ n + a) \displaystyle s_{2}\bigl(2^{\nu}n+a+d_{j}\bigr)-s_{2}\bigl(2^{\nu}n+a\bigr) | = s 2 ( ν) ​ ( a + d j) − s 2 ( ν) ​ ( a) \displaystyle=s_{2}^{(\nu)}(a+d_{j})-s_{2}^{(\nu)}(a) |  | (22) |

for all n ≥ 0 n\geq 0. The function defined by s 2 ( ν) ​ ( n) = s 2 ​ ( n mod 2 ν) s_{2}^{(\nu)}(n)=s_{2}(n\bmod 2^{\nu}) is the *truncated binary sum-of-digits function*. Note that the right hand side of ( 22) is independent of n n; we want to use Chebychev’s inequality for choosing a value a a such that these values are small for all j ∈ { − J, …, J } j\in\{-J,\ldots,J\}. In order to obtain an estimate for the variance, needed for Chebychev’s inequality, we adapt parts from [56]. For integers t, L ≥ 0 t,L\geq 0 and j j, we define a probability mass function φ ⁡ ( ¯, t, L) \varphi(\hskip 0.5pt\underline{\hphantom{\hskip 6.00006pt}}\hskip 0.5pt,t,L) by

 | φ ⁡ ( j, t, L) ≔ 1 2 L ​ #​ { 0 ≤ n < 2 L: s 2 ( L) ​ ( n + t) − s 2 ( L) ​ ( n) = j }, \varphi(j,t,L)\coloneqq\frac{1}{2^{L}}\#\bigl\{0\leq n<2^{L}:s^{(L)}_{2}(n+t)-s^{(L)}_{2}(n)=j\bigr\}, |  | (23) |

and the characteristic function

 | ω t ​ ( ϑ, L) ≔ ∑ j ∈ ℤ φ ⁡ ( j, t, L) ​ e ⁡ ( j ​ ϑ) = 1 2 L ​ ∑ 0 ≤ n < 2 L e ⁡ ( ϑ ​ s 2 ( L) ​ ( n + t) − ϑ ​ s 2 ( L) ​ ( n)), \omega_{t}(\vartheta,L)\coloneqq\sum_{j\in\mathbb{Z}}\varphi(j,t,L)\e(j\vartheta)=\frac{1}{2^{L}}\sum_{0\leq n<2^{L}}\e\bigl(\vartheta s_{2}^{(L)}(n+t)-\vartheta s_{2}^{(L)}(n)\bigr), |  | (24) |

where e ⁡ ( x) = exp ⁡ ( 2 ​ π ​ ix) \e(x)=\exp(2\pi ix). Noting that

 | s 2 ( L + 1) ​ ( 2 ​ n) = s 2 ( L) ​ ( n) and s 2 ( L + 1) ​ ( 2 ​ n + 1) = s 2 ( L) ​ ( n) + 1, s_{2}^{(L+1)}(2n)=s_{2}^{(L)}(n)\quad\text{and}\quad s_{2}^{(L+1)}(2n+1)=s_{2}^{(L)}(n)+1, |  | (25) |

the proof of the following statement is not difficult and left to the reader.

###### Lemma 2.5.

For all t, L ≥ 0 t,L\geq 0 and j ∈ ℤ j\in\mathbb{Z} we have

 | φ ⁡ ( j, 1, L) \displaystyle\varphi(j,1,L) | = { 2 j − 2, − L + 2 ≤ j ≤ 1; 2 − L, j = − L; 0, otherwise, \displaystyle=\begin{cases}2^{j-2},&-L+2\leq j\leq 1;\\ 2^{-L},&j=-L;\\ 0,&\text{otherwise,}\end{cases} |  | (26) |

 | φ ⁡ ( j, 2 ​ t, L + 1) \displaystyle\varphi(j,2t,L+1) | = φ ⁡ ( j, t, L), \displaystyle=\varphi(j,t,L), |  |

 | φ ⁡ ( j, 2 ​ t + 1, L + 1) \displaystyle\varphi(j,2t+1,L+1) | = 1 2 ​ φ ​ ( j − 1, t, L) + 1 2 ​ φ ​ ( j + 1, t + 1, L). \displaystyle=\frac{1}{2}\varphi(j-1,t,L)+\frac{1}{2}\varphi(j+1,t+1,L). |  |

The characteristic function satisfies

 | | ω t ( ϑ, L) | \displaystyle\bigl\lvert\omega_{t}(\vartheta,L)\bigr\rvert | ≤ 1, \displaystyle\leq 1, |  | (27) |

 | ω 2 ​ t ​ ( ϑ, L + 1) \displaystyle\omega_{2t}(\vartheta,L+1) | = ω t ​ ( ϑ, L), \displaystyle=\omega_{t}(\vartheta,L), |  |

 | ω 2 ​ t + 1 ​ ( ϑ, L + 1) \displaystyle\omega_{2t+1}(\vartheta,L+1) | = e ⁡ ( ϑ) 2 ω t ( ϑ, L) + e ⁡ ( − ϑ) 2 ω t + 1 ( ϑ, L) for t ≥ 1. \displaystyle=\frac{\e(\vartheta)}{2}\omega_{t}(\vartheta,L)+\frac{\e(-\vartheta)}{2}\omega_{t+1}(\vartheta,L)\quad\text{for }t\geq 1. |  |

The recurrence ( 27) leads to a recurrence for the moments

 | m k ​ ( t, L) ≔ ∑ j ∈ ℤ φ ⁡ ( j, t, L) ​ j k m_{k}(t,L)\coloneqq\sum_{j\in\mathbb{Z}}\varphi(j,t,L)j^{k} |  | (28) |

of φ ⁡ ( ¯, t, L) \varphi(\hskip 0.5pt\underline{\hphantom{\hskip 6.00006pt}}\hskip 0.5pt,t,L). Using the identity

 | ω t ​ ( ϑ, L) = ∑ j ∈ ℤ δ ⁡ ( j, t) ​ e ⁡ ( jx) = ∑ k ≥ 0 m k ​ ( t, L) k! ​ ( 2 ​ π ​ i ​ ϑ) k \omega_{t}(\vartheta,L)=\sum_{j\in\mathbb{Z}}\delta(j,t)\e(jx)=\sum_{k\geq 0}\frac{m_{k}(t,L)}{k!}\bigl(2\pi i\vartheta\bigr)^{k} |  | (29) |

(all involved series are absolutely convergent), we obtain

 | m k ​ ( t, L) = k! ( 2 ​ π ​ i) k ​ [ϑ k] ​ ω t ​ ( ϑ, L), m_{k}(t,L)=\frac{k!}{(2\pi i)^{k}}\bigl[\vartheta^{k}\bigr]\omega_{t}(\vartheta,L), |  | (30) |

from which we can iteratively obtain recurrences for the moments m k ​ ( t, L) m_{k}(t,L).

From ( 26) we clearly see that m 0 ​ ( t, L) = ∑ j ∈ ℤ φ ⁡ ( j, t, L) = 1 m_{0}(t,L)=\sum_{j\in\mathbb{Z}}\varphi(j,t,L)=1, m 1 ​ ( t, L) = ∑ j ∈ ℤ j ​ φ ​ ( j, t, L) = 0 m_{1}(t,L)=\sum_{j\in\mathbb{Z}}j\varphi(j,t,L)=0, φ ⁡ ( j, 2 ​ t, L + 1) = φ ⁡ ( j, t, L) \varphi(j,2t,L+1)=\varphi(j,t,L), and m 2 ​ ( 1, L) = 2 − 2 − L + 1 m_{2}(1,L)=2-2^{-L+1}. Moreover, ( 27), ( 29), and ( 30) imply

 | m 2 ​ ( 2 ​ t + 1, L + 1) \displaystyle m_{2}(2t+1,L+1) | = − 1 4 ​ π 2 ​ [ϑ 2] ​ ( ( 1 + 2 ​ π ​ i ​ ϑ − 2 ​ π 2 ​ ϑ 2) ​ ( 1 − ( 2 ​ π 2) ​ m 2 ​ ( t, L)) CLOSE \displaystyle=-\frac{1}{4\pi^{2}}\bigl[\vartheta^{2}\bigr]\Bigl(\bigl(1+2\pi i\vartheta-2\pi^{2}\vartheta^{2}\bigr)\bigl(1-\bigl(2\pi^{2}\bigr)m_{2}(t,L)\bigr) |  |

 |  | OPEN + ( 1 − 2 ​ π ​ i ​ ϑ − 2 ​ π 2 ​ ϑ 2) ​ ( 1 − ( 2 ​ π 2) ​ m 2 ​ ( t + 1, L))) \displaystyle\hskip 50.00008pt+\bigl(1-2\pi i\vartheta-2\pi^{2}\vartheta^{2}\bigr)\bigl(1-\bigl(2\pi^{2}\bigr)m_{2}(t+1,L)\bigr)\Bigr) |  |

 |  | = m 2 ​ ( t, L) / 2 + m 2 ​ ( t + 1, L) / 2 + 1. \displaystyle=m_{2}(t,L)/2+m_{2}(t+1,L)/2+1. |  |

Summarizing, for all k ≥ 0 k\geq 0, t ≥ 1 t\geq 1, and L ≥ 0 L\geq 0, we have

 | m 0 ​ ( t, L) \displaystyle m_{0}(t,L) | = 1, \displaystyle=1, |  | (31) |

 | m 1 ​ ( t, L) \displaystyle m_{1}(t,L) | = 0, \displaystyle=0, |  |

 | m 2 ​ ( 1, L) \displaystyle m_{2}(1,L) | = 2 − 2 − L + 1, \displaystyle=2-2^{-L+1}, |  |

 | m k ​ ( 2 ​ t, L + 1) \displaystyle m_{k}(2t,L+1) | = m k ​ ( t, L), \displaystyle=m_{k}(t,L), |  |

 | m 2 ​ ( 2 ​ t + 1, L + 1) \displaystyle m_{2}(2t+1,L+1) | = m 2 ​ ( t, L) + m 2 ​ ( t + 1, L) 2 + 1. \displaystyle=\frac{m_{2}(t,L)+m_{2}(t+1,L)}{2}+1. |  |

From the recurrence ( 27) for the characteristic function we could easily obtain recurrences for the higher moments too (compare [56, (2 ⋅ \cdot 11)]), but here we only need the first and second moments. In analogy to Corollary 2.3 in [57] we obtain the following statement.

There exists a constant C C such that for all integers B, L ≥ 1 B,L\geq 1, and t ≥ 1 t\geq 1 having B B blocks of 𝟷 \mathtt{1} s,

 | m 2 ​ ( t, L) ≤ C ​ B. m_{2}(t,L)\leq CB. |  |

However, we only need the following version, which follows directly from ( 31): we have

 | m 2 ​ ( t, ν) ≤ 2 ​ ν for all ​ t, ν ≥ 1 ​ such that ​ t < 2 ν. m_{2}(t,\nu)\leq 2\nu\quad\text{for all }t,\nu\geq 1\text{ such that }t<2^{\nu}. |  | (32) |

In particular, this holds for t = d j t=d_{j} defined in ( 13), and for this estimate we do not need to know what d j d_{j} looks like in binary. We are interested in the differences on the right hand side of ( 22). By Chebychev’s inequality and ( 32), the number of integers a ∈ { 0, …, 2 ν − 1 } a\in\{0,\ldots,2^{\nu}-1\} such that

 | | s 2 ( ν) ( a + d j) − s 2 ( ν) ( a) | ≤ R 2 ( 2 ν) 1 / 2 \Bigl\lvert s_{2}^{(\nu)}(a+d_{j})-s_{2}^{(\nu)}(a)\Bigr\rvert\leq R_{2}(2\nu)^{1/2} |  | (33) |

is bounded below by

 | 2 ν ​ ( 1 − 1 / R 2 2). 2^{\nu}\bigl(1-1/R_{2}^{2}\bigr). |  |

Intersecting 2 ​ J + 1 2J+1 sets, we obtain the set of a < 2 ν a<2^{\nu} that satisfy ( 33) for all j ∈ { − J, …, J } j\in\{-J,\ldots,J\}, having cardinality ≥ 2 ν ​ ( 1 − ( 2 ​ J + 1) / R 2 2) \geq 2^{\nu}(1-(2J+1)/R_{2}^{2}). We choose R 2 = λ / ( 2 ​ ν) R_{2}=\lambda/(2\nu), which is ≍ λ 1 / 8 / ( log ⁡ λ) 1 / 2 + ε \asymp\lambda^{1/8}/(\log\lambda)^{1/2+\varepsilon} as N → ∞ N\rightarrow\infty. It follows that the set of a ∈ { 0, …, 2 ν − 1 } a\in\{0,\ldots,2^{\nu}-1\} satisfying

 | | s 2 ( ν) ( a + d j) − s 2 ( ν) ( a) | ≤ λ 1 / 2 for all j ∈ { − J, …, J } \Bigl\lvert s_{2}^{(\nu)}(a+d_{j})-s_{2}^{(\nu)}(a)\Bigr\rvert\leq\lambda^{1/2}\quad\text{for all }j\in\{-J,\ldots,J\} |  | (34) |

has at least

 | 2 ν ( 1 − 𝒪 ( ( log λ) 2 + 4 ​ ε λ − 1 / 4)) 2^{\nu}\bigl(1-\LandauO\bigl((\log\lambda)^{2+4\varepsilon}\lambda^{-1/4}\bigr)\bigr) |  |

elements, by the definitions ( 12). Since powers win against logarithms for large N N, we obtain some integer a a with the properties that

 | a ≡ 1 mod 4, 0 ≤ a < 2 ν − 1, and | δ j | ≤ λ 1 / 2 for all ​ j ∈ { − J, …, J }, \begin{array}[]{ll}a\equiv 1\bmod 4,\\[5.69054pt] 0\leq a<2^{\nu-1},&\text{and}\\[5.69054pt] \lvert\delta_{j}\rvert\leq\lambda^{1/2}&\text{for all }j\in\{-J,\ldots,J\},\end{array} |  | (35) |

where

 | δ j ≔ s 2 ( ν) ​ ( a + d j) − s 2 ( ν) ​ ( a). \delta_{j}\coloneqq s_{2}^{(\nu)}(a+d_{j})-s_{2}^{(\nu)}(a). |  | (36) |

Note that the first two restrictions in ( 35) will pose no problem since asymptotically almost all a < 2 ν a<2^{\nu} (as N → ∞ N\rightarrow\infty) satisfy the third.

By ( 22) we have therefore found an arithmetic progression

 | A = a + 2 ν ​ ℕ A=a+2^{\nu}\mathbb{N} |  | (37) |

such that each of the sequences

 | σ j = ( s 2 ​ ( m + d j) − s 2 ​ ( m)) m ∈ A, \sigma_{j}=\bigl(s_{2}(m+d_{j})-s_{2}(m)\bigr)_{m\in A}, |  |

for − J ≤ j ≤ J -J\leq j\leq J, is constant, and attains a value δ j \delta_{j} bounded by λ 1 / 2 \lambda^{1/2} in absolute value.

In the next step, the ternary sum of digits will come into play, and we rarefy the progression A A by a factor 3 β 3^{\beta}, where

 | β = ( 2 ​ J + 1) ​ η + 1. \beta=(2J+1)\eta+1. |  | (38) |

Note that η ≍ λ 3 / 4 \eta\asymp\lambda^{3/4} has been used in the definition ( 13) of the values d j d_{j} before. The selection of this subsequence has to be carried out with care, so that certain differences f ⁡ ( n + d j) − f ⁡ ( n) f(n+d_{j})-f(n), where

 | f ⁡ ( n) = s 2 ​ ( n) − s 3 ​ ( n), f(n)=s_{2}(n)-s_{3}(n), |  | (39) |

are attained on this rarefied progression for − J ≤ j ≤ J -J\leq j\leq J. Sure enough, in order to obtain these differences we will have to “repair” the deviation δ j \delta_{j} from 0 0 caused by the differences of binary sums of digits. We are going to select a residue class B = K + 3 β ​ ℕ B=K+3^{\beta}\mathbb{N}, where K < 3 β K<3^{\beta}, on which certain differences

 | s 3 ​ ( n + d j) − s 3 ​ ( n) s_{3}(n+d_{j})-s_{3}(n) |  | (40) |

occur for n ∈ B n\in B. This process will be executed step by step, thinning out the current residue class by a factor 3 η 3^{\eta} for each j ∈ { − J, …, J } j\in\{-J,\ldots,J\}. We have found a certain arithmetic progression A A in ( 37). A sub-progression A ′ A^{\prime} of A A having the desired difference properties in bases 2 2 and 3 3 — that is, s 2 ​ ( n + d j) − s 2 ​ ( n) = δ j s_{2}(n+d_{j})-s_{2}(n)=\delta_{j} and ( 49) below — will be obtained by the intersection

 | A ∩ B = ( a + 2 ν ​ ℕ) ∩ ( K + 3 β ​ ℕ) = L + 2 ν ​ 3 β ​ ℕ, A\cap B=\left(a+2^{\nu}\mathbb{N}\right)\cap\left(K+3^{\beta}\mathbb{N}\right)=L+2^{\nu}3^{\beta}\mathbb{N}, |  | (41) |

where 0 ≤ L < 2 ν ​ 3 β 0\leq L<2^{\nu}3^{\beta}. We need to find K K. This number will in fact be divisible by 3 3 (hence the definition of d j d_{j} as a multiple of three) — together with a ≡ 1 mod 4 a\equiv 1\bmod 4 this leads to L ≡ 9 mod 12 L\equiv 9\bmod 12. The construction is similar to the definition of d j d_{j}, where we concatenated ternary expansions of length η \eta, given by 𝔟 = ( 𝟷 η) 3 \mathfrak{b}=\bigl(\mathtt{1}^{\eta}\bigr)_{3}. We begin with the integer k − J k_{-J}. By our preparation, the quantity J ​ m + δ − J Jm+\delta_{-J} (of size λ 1 / 2 \lambda^{1/2} times a logarithmic factor) is considerably smaller than η \eta (of size λ 3 / 4 \lambda^{3/4}).

The large number of 𝟷 \mathtt{1} s in 𝔟 \mathfrak{b} can be used to find some 𝔞 ∈ { 0, …, 3 η − 1 − 1 } \mathfrak{a}\in\{0,\ldots,3^{\eta-1}-1\} and ξ ∈ { 0, 1 } \xi\in\{0,1\} such that

 | s 3 ​ ( 𝔞 + 𝔟) − s 3 ​ ( 𝔞) = J ​ m + δ − J − ξ. s_{3}\bigl(\mathfrak{a}+\mathfrak{b}\bigr)-s_{3}(\mathfrak{a})=Jm+\delta_{-J}-\xi. |  | (42) |

In fact, such an integer 𝔞 \mathfrak{a} is found by assembling blocks of length four of ternary digits, where no carry between these blocks occurs, using the following addition patterns in base 3 3:

 | 𝟶𝟷𝟷𝟸 + 𝟷𝟷𝟷𝟷 = 𝟸𝟶𝟶𝟶. 𝟶𝟸𝟶𝟸 + 𝟷𝟷𝟷𝟷 = 𝟸𝟶𝟸𝟶, 𝟶𝟸𝟶𝟶 + 𝟷𝟷𝟷𝟷 = 𝟸𝟶𝟷𝟷. \begin{array}[]{r@{\hskip 1mm}r@{\hskip 0em}l}\hskip 2.84526pt&\mathtt{0}\mathtt{1}\mathtt{1}\mathtt{2}\hskip 0.0pt\\ +\hskip 2.84526pt&\mathtt{1}\mathtt{1}\mathtt{1}\mathtt{1}\hskip 0.0pt\\ \hline\cr=\hskip 2.84526pt&\mathtt{2}\mathtt{0}\mathtt{0}\mathtt{0}\hskip 0.0pt&.\end{array}\quad\begin{array}[]{r@{\hskip 1mm}r@{\hskip 0em}l}\hskip 2.84526pt&\mathtt{0}\mathtt{2}\mathtt{0}\mathtt{2}\hskip 0.0pt\\ +\hskip 2.84526pt&\mathtt{1}\mathtt{1}\mathtt{1}\mathtt{1}\hskip 0.0pt\\ \hline\cr=\hskip 2.84526pt&\mathtt{2}\mathtt{0}\mathtt{2}\mathtt{0}\hskip 0.0pt&,\end{array}\quad\begin{array}[]{r@{\hskip 1mm}r@{\hskip 0em}l}\hskip 2.84526pt&\mathtt{0}\mathtt{2}\mathtt{0}\mathtt{0}\hskip 0.0pt\\ +\hskip 2.84526pt&\mathtt{1}\mathtt{1}\mathtt{1}\mathtt{1}\hskip 0.0pt\\ \hline\cr=\hskip 2.84526pt&\mathtt{2}\mathtt{0}\mathtt{1}\mathtt{1}\hskip 0.0pt&.\end{array} |  |

We see that each block of length four can be used to obtain a variation ∈ { − 2, 0, 2 } \in\{-2,0,2\} of the ternary sum of digits; there are η / 4 ≫ λ 3 / 4 \eta/4\gg\lambda^{3/4} such blocks, while the needed variation is ≍ λ 1 / 2 ​ ( log ⁡ λ) 1 / 2 + ε \asymp\lambda^{1/2}(\log\lambda)^{1/2+\varepsilon} and thus much smaller. Moreover, by construction ( 12), the integer η \eta is divisible by four, so there are no phenomena due to trailing digits. Using any ξ ∈ { 0, 1 } \xi\in\{0,1\} and 𝔞 < 3 η − 1 \mathfrak{a}<3^{\eta-1} satisfying ( 42), we set

 | k − J ≔ 3 ​ 𝔞 and ξ − J ≔ ξ. k_{-J}\coloneqq 3\mathfrak{a}\quad\text{and}\quad\xi_{-J}\coloneqq\xi. |  | (43) |

Trivially, we obtain

 | s 3 ​ ( k − J + d − J) − s 3 ​ ( k − J) = J ​ m + δ − J − ξ − J. s_{3}\bigl(k_{-J}+d_{-J}\bigr)-s_{3}\bigl(k_{-J}\bigr)=Jm+\delta_{-J}-\xi_{-J}. |  | (44) |

Since 𝔞 < 3 η − 1 \mathfrak{a}<3^{\eta-1}, there does not appear a carry to the η + 1 \eta+1 th ternary digit in the addition k − J + d − J k_{-J}+d_{-J}. Assume that k j − 1 k_{j-1} has already been defined, for some − J < j ≤ J -J<j\leq J. In analogy to the above, choose 𝔞 ∈ { 0, …, 3 η − 1 − 1 } \mathfrak{a}\in\{0,\ldots,3^{\eta-1}-1\} and ξ ∈ { 0, 1 } \xi\in\{0,1\} in such a way that

 | s 3 ​ ( 𝔞 + 𝔟) − s 3 ​ ( 𝔞) = − m − δ j − 1 + ξ j − 1 + δ j − ξ, s_{3}(\mathfrak{a}+\mathfrak{b})-s_{3}(\mathfrak{a})=-m-\delta_{j-1}+\xi_{j-1}+\delta_{j}-\xi, |  | (45) |

and set

 | k j = k j − 1 + 3 ( j + J) ​ η + 1 ​ 𝔞 and ξ j ≔ ξ. k_{j}=k_{j-1}+3^{(j+J)\eta+1}\mathfrak{a}\quad\text{and}\quad\xi_{j}\coloneqq\xi. |  | (46) |

Note that the target value satisfies − m − δ j − 1 + ξ j − 1 + δ j − ξ ≪ λ 1 / 2 -m-\delta_{j-1}+\xi_{j-1}+\delta_{j}-\xi\ll\lambda^{1/2}, which is again small compared to the number of 𝟷 \mathtt{1} s in 𝔟 \mathfrak{b}. Since carry propagation between blocks of length η \eta is not possible by construction (as in the case j = − J j=-J), we obtain by concatenating blocks of length η \eta and applying a telescoping sum,

 | s 3 ​ ( k j + d j) − s 3 ​ ( k j) = − j ​ m + δ j − ξ j for all ​ j ∈ { − J, …, J }. s_{3}\bigl(k_{j}+d_{j}\bigr)-s_{3}\bigl(k_{j}\bigr)=-jm+\delta_{j}-\xi_{j}\quad\text{for all }j\in\{-J,\ldots,J\}. |  | (47) |

Finally, set K = k J K=k_{J} and note that β = ( 2 ​ J + 1) ​ η + 1 \beta=(2J+1)\eta+1 according to ( 38), so that K < 3 β K<3^{\beta}. By construction (note that the ternary digits of d j d_{j} from ( j + 1 + J) ​ η + 1 (j+1+J)\eta+1 on are zero) we have

 | s 3 ​ ( K + d j) − s 3 ​ ( K) = − j ​ m + δ j − ξ j for all ​ j ∈ { − J, …, J }. s_{3}(K+d_{j})-s_{3}(K)=-jm+\delta_{j}-\xi_{j}\quad\text{for all }j\in\{-J,\ldots,J\}. |  | (48) |

Similar to ( 22), noting that there is no carry propagation in base three to the β \beta th digit in the addition K + d j K+d_{j}, we have in fact

 | s 3 ​ ( n + d j) − s 3 ​ ( n) = − j ​ m + δ j − ξ j s_{3}(n+d_{j})-s_{3}(n)=-jm+\delta_{j}-\xi_{j} |  | (49) |

for all n ∈ K + 3 β ​ ℕ n\in K+3^{\beta}\mathbb{N}. Define L L by ( 41). By construction, the residue class L + 2 ν ​ 3 β ​ ℤ L+2^{\nu}3^{\beta}\mathbb{Z} is a subset of both 3 ​ ℤ 3\mathbb{Z} and 1 + 4 ​ ℤ 1+4\mathbb{Z}, therefore L ≡ 9 mod 12 L\equiv 9\bmod 12, and we obtain the *difference property*( 14) and thus Proposition 2.2.∎

### 2.3 Small values of f ⁡ ( n) f(n) — proof of Proposition 2.3

By our difference property ( 14) it is sufficient to prove the existence of (many) elements n ∈ A ′ n\in A^{\prime} such that

 | f ⁡ ( n) ∈ Q, where Q = { j ​ m: − J ≤ j ≤ J }. f(n)\in Q,\quad\text{where}\quad Q=\{jm:-J\leq j\leq J\}. |  | (50) |

After all, for each n n satisfying ( 50) we can adjust the value of f f, up to a correction term ∈ { 0, 1 } \in\{0,1\}, by any amount c ∈ Q c\in Q using a suitably chosen shift d ⁡ ( n) ∈ { d − J, d − J + 1, …, d J } d(n)\in\{d_{-J},d_{-J+1},\ldots,d_{J}\}. Having done so, we arrive at the desired property f ⁡ ( n + d ⁡ ( n)) ∈ { 0, 1 } f(n+d(n))\in\{0,1\}. Since for each given N N the constructed quantities d j d_{j} are nonnegative and smaller than the common difference of A ′ A^{\prime} — by ( 13) we have d j < 2 ν ​ 3 β d_{j}<2^{\nu}3^{\beta} — this will show that there are infinitely many solutions to s 2 ​ ( n) − s 3 ​ ( n) ∈ { 0, 1 } s_{2}(n)-s_{3}(n)\in\{0,1\}, and in fact we will give a quantitative lower bound. Proving that ( 50) has many solutions in A ′ A^{\prime} will be the subject of this and the following section, constituting the second (“rarefaction”) and third (“fair share”) stages of our proof, respectively.

In the present section we are concerned with restricting our residue class A ′ A^{\prime} in order to obtain f ⁡ ( n) ∈ [− J ​ m, J ​ m] f(n)\in[-Jm,Jm] for many integers n n in the new set A ′′ A^{\prime\prime}. The third step will consist in the study of the property f ⁡ ( n) ∈ m ​ ℤ f(n)\in m\mathbb{Z}, which will be carried out in Section 2.4.

Note that for all M M, the value s 2 ​ ( a + n ​ M) s_{2}(a+nM) will be C ​ log ⁡ N C\sqrt{\log N} -close to log 4 ⁡ ( N) \log_{4}(N) for asymptotically almost all n < N n<N as N → ∞ N\rightarrow\infty, while s 3 ​ ( a + n ​ M) s_{3}(a+nM) will be C ​ log ⁡ N C\sqrt{\log N} -close to log 3 ⁡ ( N) \log_{3}(N) most of the time. Therefore a concentration property of f ⁡ ( n) f(n) can only be satisfied for a finite segment of any arithmetic progression. The fact that the values of f f can be concentrated around zero by selecting a finite arithmetic subsequence is an essential point. It is based on the consideration that 3 τ ​ n 3^{\tau}n has the same ternary sum of digits as n n for all integers τ ≥ 0 \tau\geq 0, while the binary sum of digits — usually — increases considerably under multiplication by 3 τ 3^{\tau}. This small remark is in fact the main idea that started the research on the present paper.

Recall the definition ( 15) of A ′′ A^{\prime\prime}, for a natural number ζ \zeta that will be chosen in due course. Suitable choice of ζ \zeta will cause most values of f f along A ′′ A^{\prime\prime} to lie in the interval [− J ​ m, J ​ m] [-Jm,Jm]. At this point we only note that 3 ζ 3^{\zeta} will be much larger than 2 ν 2^{\nu} and 3 β 3^{\beta}, in orders of magnitude, ν ≍ β ≍ λ 3 / 4 ​ ( log ⁡ λ) 1 + 2 ​ ε \nu\asymp\beta\asymp\lambda^{3/4}(\log\lambda)^{1+2\varepsilon}, while ζ ≍ λ \zeta\asymp\lambda. Trivially, ( 14) is satisfied on the subsequence A ′′ A^{\prime\prime} too. We are therefore interested in the expression

 | f ⁡ ( L + 2 ν ​ 3 β + ζ ​ k) = s 2 ​ ( L + 2 ν ​ 3 β + ζ ​ k) − s 3 ​ ( L + 2 ν ​ 3 β + ζ ​ k), f\bigl(L+2^{\nu}3^{\beta+\zeta}k\bigr)=s_{2}\bigl(L+2^{\nu}3^{\beta+\zeta}k\bigr)-s_{3}\bigl(L+2^{\nu}3^{\beta+\zeta}k\bigr), |  | (51) |

where k k varies in the interval I I defined in ( 16). We can decompose ( 51) in the form

 | f ⁡ ( L + 2 ν ​ 3 β + ζ ​ k) = s 2 ​ ( b 2 + 3 β + ζ ​ k) − s 3 ​ ( b 3 + 2 ν ​ k) + s 2 ​ ( r 2) − s 3 ​ ( r 3), f\bigl(L+2^{\nu}3^{\beta+\zeta}k\bigr)=s_{2}\bigl(b_{2}+3^{\beta+\zeta}k\bigr)-s_{3}\bigl(b_{3}+2^{\nu}k\bigr)+s_{2}(r_{2})-s_{3}(r_{3}), |  | (52) |

where

 | b 2 = ⌊ 2 − ν ​ L ⌋ and b 3 = ⌊ 3 − β − ζ ​ L ⌋, r 2 = L mod 2 ν and r 3 = L mod 3 β + ζ. \begin{array}[]{r@{\hskip 2mm}c@{\hskip 2mm}l@{\hskip 2em}l@{\hskip 2em}r@{\hskip 2mm}c@{\hskip 2mm}l}b_{2}\hskip 5.69054pt&=\hfil\hskip 5.69054pt&\bigl\lfloor 2^{-\nu}L\bigr\rfloor\hfil\qquad&\text{and}\hfil\qquad&b_{3}\hskip 5.69054pt&=\hfil\hskip 5.69054pt&\bigl\lfloor 3^{-\beta-\zeta}L\bigr\rfloor,\\[2.84526pt] r_{2}\hskip 5.69054pt&=\hfil\hskip 5.69054pt&L\bmod 2^{\nu}\hfil\qquad&\text{and}\hfil\qquad&r_{3}\hskip 5.69054pt&=\hfil\hskip 5.69054pt&L\bmod 3^{\beta+\zeta}.\end{array} |  |

Let us choose

 | ζ 0 ≔ log 3 ⁡ ( N) ​ ( 1 − log ⁡ 3 log ⁡ 4) + s 3 ​ ( L) − s 2 ​ ( r 2) + ν 2 − β, and ζ ≔ ⌊ ζ 0 ⌋. \zeta_{0}\coloneqq\log_{3}(N)\left(1-\frac{\log 3}{\log 4}\right)+s_{3}(L)-s_{2}(r_{2})+\frac{\nu}{2}-\beta,\quad\text{and}\quad\zeta\coloneqq\lfloor\zeta_{0}\rfloor. |  | (53) |

We have r 2 < 2 ν r_{2}<2^{\nu}, and L < 2 ν ​ 3 β L<2^{\nu}3^{\beta}; moreover, it follows from the definitions that ν = o ⁡ ( log ⁡ N) \nu=o(\log N) and β = o ⁡ ( log ⁡ N) \beta=o(\log N). Therefore ζ ∼ C ​ log 3 ​ N \zeta\sim C\log_{3}N, where the constant equals

 | C = 1 − log ⁡ 3 2 ​ log ⁡ 2 = 0.207 ​ …. C=1-\frac{\log 3}{2\log 2}=0.207\ldots. |  | (54) |

In particular, 3 ζ ≥ 2 ν 3^{\zeta}\geq 2^{\nu} for all large N N. Since L < 2 ν ​ 3 β L<2^{\nu}3^{\beta}, we have in fact

 | b 3 = 0 and r 3 = L. b_{3}=0\quad\mbox{and}\quad r_{3}=L. |  |

That is, r 2 r_{2} and r 3 r_{3} do not depend on the particular choice of ζ ≥ ν ​ log 3 ​ 2 \zeta\geq\nu\log_{3}2. In ( 53) this freedom is used in order to define the rarefaction parameter ζ \zeta suitably. This in turn determines the arithmetic progression A ′′ A^{\prime\prime} defined in ( 15). Note that we have already replaced r 3 r_{3} by L L in the definition of ζ 0 \zeta_{0} in order to avoid a circular definition. This procedure, as we will see, very accurately defines an interval around zero in which f ⁡ ( n) f(n), for n ∈ A ′′ n\in A^{\prime\prime}, can be found most of the time. That is, ( 51) is close to zero for most k ∈ I k\in I.

We study the values

 | f 2 ​ ( k) = s 2 ​ ( b 2 + 3 β + ζ ​ k) and f 3 ​ ( k) = s 3 ​ ( 2 ν ​ k) f_{2}(k)=s_{2}\bigl(b_{2}+3^{\beta+\zeta}k\bigr)\quad\text{and}\quad f_{3}(k)=s_{3}\bigl(2^{\nu}k\bigr) |  | (55) |

separately, as k k varies in I I.

Sure enough, the study of ( 55) will be infeasible in general using current techniques. This is the case because we encounter problems arising from powers of 2 2 and 3 3, as considered in the introduction. In our application however, the interval I I is of the form

 | I = [M, 2 ​ M + 𝒪 ⁡ ( 1)] I=[M,2M+\LandauO(1)] |  | (56) |

for some M M considerably larger than 2 ν 2^{\nu} and 3 β + ζ 3^{\beta+\zeta}, which enables us to prove a nontrivial statement on the distributions of f 2 ​ ( k) f_{2}(k) and f 3 ​ ( k) f_{3}(k).

In the following, we use the abbreviation α = β + ζ \alpha=\beta+\zeta. Let us partition the binary expansion of b 2 + 3 α ​ k b_{2}+3^{\alpha}k into two parts, using the integer κ 2 = min ⁡ { m: 2 m ≥ 3 α } \kappa_{2}=\min\{m:2^{m}\geq 3^{\alpha}\}. For all integers k ≥ 0 k\geq 0, we have

 | s 2 ​ ( b 2 + 3 α ​ k) = s 2 ​ ( ⌊ k ​ 3 α 2 κ 2 + σ ⌋) + s 2 ​ ( ( b 2 + 3 α ​ k) mod 2 κ 2), \displaystyle s_{2}\bigl(b_{2}+3^{\alpha}k\bigr)=s_{2}\left(\left\lfloor k\frac{3^{\alpha}}{2^{\kappa_{2}}}+\sigma\right\rfloor\right)+s_{2}\bigl(\bigl(b_{2}+3^{\alpha}k\bigr)\bmod 2^{\kappa_{2}}\bigr), |  | (57) |

where σ = b 2 ​ 2 − κ 2 < 1 \sigma=b_{2}2^{-\kappa_{2}}<1, which follows from b 2 ≤ L ​ 2 − ν < 3 β < 2 κ 2 b_{2}\leq L2^{-\nu}<3^{\beta}<2^{\kappa_{2}}.

The values of ⌊ k ​ 3 α / 2 κ 2 + σ ⌋ \lfloor k3^{\alpha}/2^{\kappa_{2}}+\sigma\rfloor start at M ~ + 𝒪 ⁡ ( 1) \tilde{M}+\LandauO(1), where M ~ = ρ ​ M \tilde{M}=\rho M and ρ = 3 α / 2 κ 2 ∈ ( 1 / 2, 1) \rho=3^{\alpha}/2^{\kappa_{2}}\in(1/2,1), increase step by step as k k runs through I I, and remain on the same integer for at most two consecutive values of k k. Consequently, the distribution of the first summand for k ∈ I k\in I originates from the distribution of s 2 ​ ( k ′) s_{2}(k^{\prime}) for k ′ ∈ I ′ k^{\prime}\in I^{\prime}, where

 | I ′ = [M ~ − 1, 2 ​ M ~ + 1], I^{\prime}=[\tilde{M}-1,2\tilde{M}+1], |  |

and each number of occurrences is multiplied by a value ∈ { 0, 1, 2 } \in\{0,1,2\}. Therefore, using the binomial distribution, the first summand in ( 57) can be found within a short interval containing 1 2 ​ log 2 ​ M \tfrac{1}{2}\log_{2}M most of the time. More precisely, we apply Hoeffding’s inequality. Construing the binary sum-of-digits function on [0, 2 K) [0,2^{K}) as a sum of independent random variables with mean 1 / 2 1/2, we obtain for all integers T ≥ 0 T\geq 0 and real t ≥ 0 t\geq 0

 | 1 2 T { 0 ≤ n < 2 T: | s 2 ( n) − T / 2 | ≥ t } ≤ 2 exp ( − 2 t 2 / T). \frac{1}{2^{T}}\bigl\{0\leq n<2^{T}:\bigl\lvert s_{2}(n)-T/2\bigl\rvert\geq t\bigr\}\leq 2\exp\left(-2t^{2}/T\right). |  | (58) |

We apply this for t = J ​ m / 5 t=Jm/5 and T T minimal such that 2 T ≥ 2 ​ M ~ + 1 2^{T}\geq 2\tilde{M}+1. Note that

 | T ∼ log 2 ⁡ ( N 2 ν ​ 3 β + ζ) ≍ λ. T\sim\log_{2}\left(\frac{N}{2^{\nu}3^{\beta+\zeta}}\right)\asymp\lambda. |  |

Note that we used the definition of ζ \zeta for the latter asymptotics. From ( 58) we obtain

 | { k ∈ I: | s 2 ( ⌊ k 3 α / 2 κ 2 + σ ⌋) − T / 2 | ≥ t } \displaystyle\left\{k\in I:\bigl\lvert s_{2}\left(\lfloor k3^{\alpha}/2^{\kappa_{2}}+\sigma\rfloor\right)-T/2\bigr\rvert\geq t\right\} | ≤ 2 { k ′ ∈ I ′: | s 2 ( k ′) − T / 2 | ≥ t } \displaystyle\leq 2\left\{k^{\prime}\in I^{\prime}:\bigl\lvert s_{2}(k^{\prime})-T/2\bigr\rvert\geq t\right\} |  | (59) |

 |  | ≤ 2 { 0 ≤ k ′ < 2 T: | s 2 ( k ′) − T / 2 | ≥ t } \displaystyle\leq 2\left\{0\leq k^{\prime}<2^{T}:\bigl\lvert s_{2}(k^{\prime})-T/2\bigr\rvert\geq t\right\} |  |

 |  | ≪ exp ( − 2 λ ( log λ) 1 + 2 ​ ε / ( 25 T)) \displaystyle\ll\exp\bigl(-2\lambda(\log\lambda)^{1+2\varepsilon}/(25T)\bigr) |  |

 |  | ≪ exp ⁡ ( − C ​ ( log ⁡ λ) 1 + 2 ​ ε) \displaystyle\ll\exp\bigl(-C(\log\lambda)^{1+2\varepsilon}\bigr) |  |

 |  | ≪ λ − D \displaystyle\ll\lambda^{-D} |  |

for all D > 0 D>0 and some C C, as N → ∞ N\rightarrow\infty. Meanwhile, the second summand in ( 57) also follows a binomial distribution, with mean κ 2 / 2 \kappa_{2}/2 and a corresponding concentration property. For this, it is important to note that the sum over k k is longer than 2 κ 2 2^{\kappa_{2}} (for large N N): this is due to the observation, given in ( 54), that C < 1 / 2 C<1/2. Therefore, multiples of the odd integer 3 α 3^{\alpha} traverse each residue class modulo 2 κ 2 2^{\kappa_{2}} in a uniform way. After forming an intersection, the value of f 2 ​ ( k) = s 2 ​ ( b 2 + 3 α ​ k) f_{2}(k)=s_{2}(b_{2}+3^{\alpha}k) is 2 ​ J ​ m / 5 2Jm/5 -close to the value

 | E 2 = 1 2 ​ log 2 ⁡ ( N 2 ν ​ 3 β + ζ) + 1 2 ​ log 2 ​ 3 β + ζ = 1 2 ​ log 2 ⁡ ( N) − ν 2, E_{2}=\frac{1}{2}\log_{2}\left(\frac{N}{2^{\nu}3^{\beta+\zeta}}\right)+\frac{1}{2}\log_{2}3^{\beta+\zeta}=\frac{1}{2}\log_{2}(N)-\frac{\nu}{2}, |  |

for all but 𝒪 ⁡ ( | I | ​ λ − D) \LandauO\bigl(\lvert I\rvert\lambda^{-D}\bigr) integers k ∈ I k\in I. The contribution of f 3 ​ ( k) = s 3 ​ ( 2 ν ​ k) f_{3}(k)=s_{3}(2^{\nu}k) can be handled in an analogous fashion. In this case, the expression f 3 ​ ( k) f_{3}(k) is 2 ​ J ​ m / 5 2Jm/5 -close to the value

 | E 3 = log 3 ⁡ ( N 2 ν ​ 3 β + ζ) + log 3 ⁡ ( 2 ν) = log 3 ⁡ ( N) − β − ζ E_{3}=\log_{3}\left(\frac{N}{2^{\nu}3^{\beta+\zeta}}\right)+\log_{3}(2^{\nu})=\log_{3}(N)-\beta-\zeta |  |

for all but 𝒪 ⁡ ( | I | ​ λ − D) \LandauO\bigl(\lvert I\rvert\lambda^{-D}\bigr) integers k ∈ I k\in I. Again, D > 0 D>0 is arbitrary. Including the term s 2 ​ ( r 2) − s 3 ​ ( r 3) s_{2}(r_{2})-s_{3}(r_{3}) from ( 52) leads to the definition of ζ \zeta in ( 53). Joining the preceding statements and ( 52), noting that the allowed deviation J ​ m Jm is not surpassed when adding two times the error 2 ​ J ​ m / 5 2Jm/5 and also considering the rounding error coming from the floor function ζ = ⌊ ζ 0 ⌋ \zeta=\lfloor\zeta_{0}\rfloor, we obtain Proposition 2.3.∎

### 2.4 The critical expression modulo m m — proof of Proposition 2.4

The final piece in the puzzle, which we consider before we proceed to the assembly of these pieces, is the study of the function f ⁡ ( n) mod m = ( s 2 ​ ( n) − s 3 ​ ( n)) mod m f(n)\bmod m=(s_{2}(n)-s_{3}(n))\bmod m along arithmetic progressions.

We are going to adapt the Mauduit–Rivat method for digital problems [15, 16, 17, 19, 31, 32, 33, 34, 36, 37, 38, 39], also applied in the papers [18, 43, 44, 45, 46, 55]. This will be used in order to obtain a statement concerning the number P P defined in ( 18),

 | P \displaystyle P | = #⁡ { n ∈ A ′′: f ⁡ ( n) ∈ m ​ ℤ } \displaystyle=\#\bigl\{n\in A^{\prime\prime}:f(n)\in m\mathbb{Z}\bigr\} |  |

 |  | = #⁡ { k ∈ I: s 2 ​ ( b 2 + 3 β + ζ ​ k) − s 3 ​ ( 2 ν ​ k) ≡ t mod m }, \displaystyle=\#\left\{k\in I:s_{2}\bigl(b_{2}+3^{\beta+\zeta}k\bigr)-s_{3}\bigl(2^{\nu}k\bigr)\equiv t\bmod m\right\}, |  |

where t = s 3 ​ ( r 3) − s 2 ​ ( r 2) t=s_{3}(r_{3})-s_{2}(r_{2}) (see ( 52)). In order to handle this quantity, it is sufficient to study

 | S 0 = S 0 ​ ( ϑ) = ∑ k ∈ I e ⁡ ( ϑ ​ s 2 ​ ( b 2 + 3 β + ζ ​ k) − ϑ ​ s 3 ​ ( 2 ν ​ k)), S_{0}=S_{0}(\vartheta)=\sum_{k\in I}\e\bigl(\vartheta s_{2}\bigl(b_{2}+3^{\beta+\zeta}k\bigr)-\vartheta s_{3}\bigl(2^{\nu}k\bigr)\bigr), |  | (60) |

with ϑ = ℓ / m \vartheta=\ell/m, where ℓ ∈ { 0, …, m − 1 } \ell\in\{0,\ldots,m-1\}. By orthogonality relations,

 | P = | I | m + 1 m ​ ∑ 1 ≤ b < m e ⁡ ( − bt m) ​ S 0 ​ ( b m), \displaystyle P=\frac{\lvert I\rvert}{m}+\frac{1}{m}\sum_{1\leq b<m}\e\left(-\frac{bt}{m}\right)S_{0}\left(\frac{b}{m}\right), |  | (61) |

and it is sufficient to find an upper bound for S 0 ​ ( ϑ) S_{0}(\vartheta). We apply van der Corput’s inequality (for example, [37, Lemme 4]), where R ≥ 1 R\geq 1 is chosen later:

 | | S 0 | 2 ≤ | I | + R − 1 R ​ ∑ − R < r < R ( 1 − | r | R) × ∑ k ∈ I k + r ∈ I e ⁡ ( ϑ ⁡ ( s 2 ​ ( b 2 + 3 β + ζ ​ ( k + r)) − s 2 ​ ( b 2 + 3 β + ζ ​ k)) − ϑ ⁡ ( s 3 ​ ( 2 ν ​ ( k + r)) − s 3 ​ ( 2 ν ​ k))). \lvert S_{0}\rvert^{2}\leq\frac{\lvert I\rvert+R-1}{R}\sum_{-R<r<R}\left(1-\frac{\lvert r\rvert}{R}\right)\\ \times\sum_{\begin{subarray}{c}k\in I\\ k+r\in I\end{subarray}}\e\Bigl(\vartheta\bigl(s_{2}\bigl(b_{2}+3^{\beta+\zeta}(k+r)\bigr)-s_{2}\bigl(b_{2}+3^{\beta+\zeta}k\bigr)\bigr)-\vartheta\bigl(s_{3}\bigl(2^{\nu}(k+r)\bigr)-s_{3}\bigl(2^{\nu}k\bigr)\bigr)\Bigr). |  |

Next, we apply a suitable *carry propagation lemma*in order to “cut off digits”, that is, to replace s 2 s_{2} and s 3 s_{3} by *truncated sum-of-digits functions*:

 | s 2 ( μ 2) ​ ( n) \displaystyle s_{2}^{(\mu_{2})}(n) | = s 2 ​ ( n mod 2 μ 2), \displaystyle=s_{2}\bigl(n\bmod 2^{\mu_{2}}\bigr), |  |

 | s 3 ( μ 3) ​ ( n) \displaystyle s_{3}^{(\mu_{3})}(n) | = s 3 ​ ( n mod 3 μ 3), \displaystyle=s_{3}\bigl(n\bmod 3^{\mu_{3}}\bigr), |  |

where μ 2, μ 3 ≥ 0 \mu_{2},\mu_{3}\geq 0 are chosen later. See [55, Lemma 4.5] for the base- 2 2 version used here; an analogous statement holds for all bases, and we also need the completely analogous base- 3 3 variant (the original statement was given in [37, Lemme 5], compare also [36, Lemme 16]). We discard the condition n + r ∈ I n+r\in I, and join the cases r r and − r -r, in order to obtain

 | | S 0 | 2 \displaystyle\lvert S_{0}\rvert^{2} | ≤ | I | 2 𝒪 ( R | I | + 3 β + ζ ​ R 2 μ 2 + 2 ν ​ R 3 μ 3) + 2 ​ | I | R ∑ 0 ≤ r < R | S 1 |, \displaystyle\leq\lvert I\rvert^{2}\mathcal{O}\left(\frac{R}{\lvert I\rvert}+\frac{3^{\beta+\zeta}R}{2^{\mu_{2}}}+\frac{2^{\nu}R}{3^{\mu_{3}}}\right)+\frac{2\,\lvert I\rvert}{R}\sum_{0\leq r<R}\bigl\lvert S_{1}\bigr\rvert, |  | (62) |

where

 |  | S 1 = ∑ k ∈ I e ⁡ ( ϑ ​ s 2 ( μ 2) ​ ( 3 β + ζ ​ k + b 2 + 3 β + ζ ​ r) − ϑ ​ s 2 ( μ 2) ​ ( 3 β + ζ ​ k + b 2) CLOSE \displaystyle S_{1}=\sum_{k\in I}\e\Bigl(\vartheta s_{2}^{(\mu_{2})}\bigl(3^{\beta+\zeta}k+b_{2}+3^{\beta+\zeta}r\bigr)-\vartheta s_{2}^{(\mu_{2})}\bigl(3^{\beta+\zeta}k+b_{2}\bigr) |  | (63) |

 |  | OPEN − ϑ ​ s 3 ( μ 3) ​ ( 2 ν ​ k + 2 ν ​ r) + ϑ ​ s 3 ( μ 3) ​ ( 2 ν ​ k)). \displaystyle-\vartheta s_{3}^{(\mu_{3})}\bigl(2^{\nu}k+2^{\nu}r\bigr)+\vartheta s_{3}^{(\mu_{3})}\bigl(2^{\nu}k\bigr)\Bigr). |  |

Note that the lowest μ 2 \mu_{2} binary digits of b 2 + 3 β + ζ ​ k b_{2}+3^{\beta+\zeta}k and the lowest μ 3 \mu_{3} ternary digits of 2 ν ​ k 2^{\nu}k are visited *uniformly and independently*— this is just the Chinese remainder theorem.

We obtain

 |  | S 1 = | I | 2 μ 2 ​ 3 μ 3 ​ ∑ 0 ≤ n 2 < 2 μ 2 e ⁡ ( ϑ ​ s 2 ( μ 2) ​ ( n 2 + 3 β + ζ ​ r) − ϑ ​ s 2 ( μ 2) ​ ( n 2)) \displaystyle S_{1}=\frac{\lvert I\rvert}{2^{\mu_{2}}3^{\mu_{3}}}\sum_{0\leq n_{2}<2^{\mu_{2}}}\e\bigl(\vartheta s_{2}^{(\mu_{2})}\bigl(n_{2}+3^{\beta+\zeta}r\bigr)-\vartheta s_{2}^{(\mu_{2})}(n_{2})\bigr) |  | (64) |

 |  | × ∑ 0 ≤ n 3 < 3 μ 3 e ⁡ ( ϑ ​ s 3 ( μ 3) ​ ( n 3 + 2 ν ​ r) − ϑ ​ s 3 ( μ 3) ​ ( n 3)) + 𝒪 ⁡ ( 2 μ 2 ​ 3 μ 3). \displaystyle\times\sum_{0\leq n_{3}<3^{\mu_{3}}}\e\bigl(\vartheta s_{3}^{(\mu_{3})}\bigl(n_{3}+2^{\nu}r\bigr)-\vartheta s_{3}^{(\mu_{3})}(n_{3})\bigr)+\mathcal{O}\bigl(2^{\mu_{2}}3^{\mu_{3}}\bigr). |  |

For this estimate to be relevant, it is important that the number C C defined in ( 54) is smaller than 1 / 2 1/2: the interval I I has length ≍ N / ( 2 ν ​ 3 β + ζ) \asymp N/(2^{\nu}3^{\beta+\zeta}), and we need to run through 2 ν ​ 3 β + ζ 2^{\nu}3^{\beta+\zeta} many integers n ∈ I n\in I in order to apply the Chinese remainder theorem. In contrast, comparing the bases 2 2 and 7 7, the corresponding constant

 | C 2, 7 ≔ 1 − ( 2 − 1) ​ log ⁡ 7 ( 7 − 1) ​ log ⁡ 2 = 0.532 ​ … C_{2,7}\coloneqq 1-\frac{(2-1)\log 7}{(7-1)\log 2}=0.532\ldots |  |

will already be greater than 1 / 2 1/2, so new ideas will be needed for bases of “very different size”. Meanwhile, adjacent bases b b and b + 1 b+1, for example, can certainly be handled by our method; the sequence of constants C b, b + 1 C_{b,b+1} decreases to zero as b → ∞ b\rightarrow\infty.

It is sufficient to find a nontrivial estimate for the first factor in ( 64), concerning the binary expansion. We are concerned with the correlation (a characteristic function) we had in ( 24):

 | ω t ​ ( ϑ, L) = 1 2 L ​ ∑ 0 ≤ n < 2 L e ⁡ ( ϑ ​ s 2 ( L) ​ ( n + t) − ϑ ​ s 2 ( L) ​ ( n)). \omega_{t}(\vartheta,L)=\frac{1}{2^{L}}\sum_{0\leq n<2^{L}}\e\bigl(\vartheta s_{2}^{(L)}(n+t)-\vartheta s_{2}^{(L)}(n)\bigr). |  |

Reusing the argument leading to [56, Lemma 2 ⋅ \cdot 7], and Lemma 2.5, we obtain the following result.

###### Lemma 2.6.

Assume that integers B ≥ 0 B\geq 0 and L, t ≥ 1 L,t\geq 1 are given such that t t contains at least 2 ​ B + 1 2B+1 blocks of 𝟷 \mathtt{1} s, and t < 2 L t<2^{L}. Then for all real ϑ \vartheta,

 | | ω t ( ϑ, L) | ≤ ( 1 − 1 2 ∥ ϑ ∥ 2) B. \bigl\lvert\omega_{t}(\vartheta,L)\bigr\rvert\leq\left(1-\frac{1}{2}\lVert\vartheta\rVert^{2}\right)^{B}. |  |

Our focus therefore lies on the number B B of blocks of 𝟷 \mathtt{1} s in the binary expansion of 3 β + ζ ​ r 3^{\beta+\zeta}r. The only thing we need to know about powers of three in this context is the fact that they are odd integers — we exploit in an essential way the summation over r r instead. The parameter R R will be a certain power of N N; in this way, the expected size of B B is ≫ λ \gg\lambda.

Note that counting the number of blocks of 𝟷 \mathtt{1} s in binary amounts to counting the number of occurrences of 𝟶𝟷 \mathtt{0}\mathtt{1} (where the 𝟶 \mathtt{0} corresponds to the more significant digit), up to an error 𝒪 ⁡ ( 1) \LandauO(1). For simplicity, we only count such occurrences where the digit 𝟷 \mathtt{1} in the block 𝟶𝟷 \mathtt{0}\mathtt{1} occurs at an even index. For example, in the binary expansion 𝟷𝟶𝟷𝟷𝟶𝟷𝟷𝟶 \mathtt{1}\mathtt{0}\mathtt{1}\mathtt{1}\mathtt{0}\mathtt{1}\mathtt{1}\mathtt{0} the corresponding number is 1 1, whereas there exist three blocks of 𝟷 \mathtt{1} s. This simplification will, on average, give 1 / 2 1/2 of the actual expected value, which is sufficient for our purposes. We are therefore concerned with the number #​ 𝟷 ​ ( n) \#\mathtt{1}(n) of 𝟷 \mathtt{1} s occurring in the base- 4 4 expansion of n n: the number of integers 0 ≤ n < 4 K 0\leq n<4^{K} such that #​ 𝟷 ​ ( n) = ℓ \#\mathtt{1}(n)=\ell is given by

 | 4 K ​ ( K ℓ) ​ ( 1 / 4) ℓ ​ ( 3 / 4) K − ℓ. 4^{K}\binom{K}{\ell}(1/4)^{\ell}(3/4)^{K-\ell}. |  |

Suppose that we have R = 4 K R=4^{K}. Note that

 | r ↦ r ​ 3 β + ζ mod 4 K r\mapsto r3^{\beta+\zeta}\bmod 4^{K} |  |

is a bijection of the set { 0, …, 4 K − 1 } \{0,\ldots,4^{K}-1\}. We abbreviate α = 1 − ∥ ϑ ∥ 2 / 2 \alpha=1-\lVert\vartheta\rVert^{2}/2, and obtain by Lemma 2.6

 | S 2 ≔ \displaystyle S_{2}\coloneqq | ∑ 0 ≤ r < R | 1 2 μ 2 ​ ∑ 0 ≤ n 2 < 2 μ 2 e ⁡ ( ϑ ​ s 2 ( μ 2) ​ ( n 2 + 3 β + ζ ​ r) − ϑ ​ s 2 ( μ 2) ​ ( n 2)) | \displaystyle\sum_{0\leq r<R}\left\lvert\frac{1}{2^{\mu_{2}}}\sum_{0\leq n_{2}<2^{\mu_{2}}}\e\bigl(\vartheta s_{2}^{(\mu_{2})}\bigl(n_{2}+3^{\beta+\zeta}r\bigr)-\vartheta s_{2}^{(\mu_{2})}(n_{2})\bigr)\right\rvert |  |

 |  | ≤ ∑ 0 ≤ ℓ ≤ K ∑ 0 ≤ r < 4 K #​ 𝟷 ​ ( r) = ℓ α ℓ − 2 2 \displaystyle\leq\sum_{0\leq\ell\leq K}\sum_{\begin{subarray}{c}0\leq r<4^{K}\\ \#\mathtt{1}(r)=\ell\end{subarray}}\alpha^{\frac{\ell-2}{2}} |  |

 |  | = 4 K ​ α − 1 ​ ∑ 0 ≤ ℓ ≤ K ( K ℓ) ​ ( 1 / 4) ℓ ​ ( 3 / 4) K − ℓ ​ α ℓ / 2 \displaystyle=4^{K}\alpha^{-1}\sum_{0\leq\ell\leq K}\binom{K}{\ell}(1/4)^{\ell}(3/4)^{K-\ell}\alpha^{\ell/2} |  |

 |  | = 4 K ​ α − 1 ​ ( α / 4 + 3 / 4) K. \displaystyle=4^{K}\alpha^{-1}\bigl(\sqrt{\alpha}/4+3/4\bigr)^{K}. |  |

Since 1 + x ≤ 1 + x / 2 \sqrt{1+x}\leq 1+x/2 for x ≥ − 1 x\geq-1, we have

 | α = ( 1 − ∥ ϑ ∥ 2 / 2) 1 / 2 ≤ 1 − 1 4 ​ ∥ ϑ ∥ 2, \sqrt{\alpha}=\bigl(1-\lVert\vartheta\rVert^{2}/2\bigr)^{1/2}\leq 1-\frac{1}{4}\lVert\vartheta\rVert^{2}, |  | (65) |

and the inequality ( 1 + x) K = exp ⁡ ( K ​ log ⁡ ( 1 + x)) ≤ exp ⁡ ( K ​ x) (1+x)^{K}=\exp\bigl(K\log(1+x)\bigr)\leq\exp(Kx) yields

 | S 2 ≪ 4 K ​ exp ⁡ ( − K 16 ​ ∥ ϑ ∥ 2). S_{2}\ll 4^{K}\exp\left(-\frac{K}{16}\lVert\vartheta\rVert^{2}\right). |  | (66) |

We translate this back to S 0 S_{0}, noting that ∥ ϑ ∥ ≥ 1 / m ∼ λ − 1 / 2 ( log λ) 1 / 2 + ε \lVert\vartheta\rVert\geq 1/m\sim\lambda^{-1/2}(\log\lambda)^{1/2+\varepsilon}: for some constant C > 0 C>0 (any value C ∈ ( 0, 1 / 16) C\in(0,1/16) is good enough) we obtain

 | | S 0 | 2 \displaystyle\lvert S_{0}\rvert^{2} | ≪ | I | 2 ​ ( R | I | + 3 β + ζ ​ R 2 μ 2 + 2 ν ​ R 3 μ 3 + exp ⁡ ( − C ​ K ​ λ − 1 ​ ( log ⁡ λ) 1 + 2 ​ ε)). \displaystyle\ll\lvert I\rvert^{2}\left(\frac{R}{\lvert I\rvert}+\frac{3^{\beta+\zeta}R}{2^{\mu_{2}}}+\frac{2^{\nu}R}{3^{\mu_{3}}}+\exp\bigl(-CK\lambda^{-1}(\log\lambda)^{1+2\varepsilon}\bigr)\right). |  | (67) |

We see that the last term yields a contribution to S 0 S_{0} that is is smaller than the fair share | I | m − 1 ∼ | I | λ − 1 / 2 ( log λ) 1 / 2 + ε \lvert I\rvert m^{-1}\sim\lvert I\rvert\lambda^{-1/2}(\log\lambda)^{1/2+\varepsilon} as soon as K ≍ λ K\asymp\lambda, due to the presence of the power ( log ⁡ λ) 1 + 2 ​ ε (\log\lambda)^{1+2\varepsilon} in the exponent. For this, we need to choose R = 4 K R=4^{K} as large as some positive (fixed) power of N N. At the same time we have to take care of the other error terms in ( 67). It is obvious that we can choose R ≍ N ι R\asymp N^{\iota}, where ι \iota is small, and 2 μ 2 2^{\mu_{2}} resp. 3 μ 3 3^{\mu_{3}} larger than R ​ 3 β + ζ R\,3^{\beta+\zeta} resp. R ​ 2 ν R\,2^{\nu} (by some small power of N N), in such a way that 2 μ 2 ​ 3 μ 3 2^{\mu_{2}}3^{\mu_{3}} is still smaller than | I | \lvert I\rvert (by another power of N N). Such a choice is possible by the fact that ζ < 1 / 2 \zeta<1/2, and we commented on this after ( 64). We therefore obtain ( 19) from ( 61) and ( 67), which completes the proof of Proposition 2.4 and thus the proof of Theorem 1.1.∎

## 3 Open problems

1. 1.

Find a construction method for collisions, and for patterns of collisions as in ( 9), ( 10).

2. 2.

Prove that there are infinitely many prime numbers p p such that

 | s 2 ​ ( p) = s 3 ​ ( p). s_{2}(p)=s_{3}(p). |  | (68) |

3. 3.

Prove or disprove the asymptotic formula

 | #⁡ { n < N: s 2 ​ ( n) = s 3 ​ ( n) } ∼ c ​ N η \#\bigl\{n<N:s_{2}(n)=s_{3}(n)\bigr\}\sim cN^{\eta} |  | (69) |

for some real constants c c and η \eta.

4. 4.

Prove an asymptotic formula (in k k) for the number of solutions of the equation

 | 2 μ 1 + ⋯ + 2 μ k = 3 ν 1 + ⋯ + 3 ν k, 2^{\mu_{1}}+\cdots+2^{\mu_{k}}=3^{\nu_{1}}+\cdots+3^{\nu_{k}}, |  | (70) |

and for the numbers

 | #⁡ { n ∈ ℕ: s 2 ​ ( n) = s 3 ​ ( n) = k } \#\bigl\{n\in\mathbb{N}:s_{2}(n)=s_{3}(n)=k\bigr\} |  |

(finiteness in the second case was proved by Senge and Straus [52]).

5. 5.

Generalize Theorem 1.1 and Problems 1 – 4 to any pair ( q 1, q 2) (q_{1},q_{2}) of multiplicatively independent bases, and to arbitrary families ( q 1, …, q K) (q_{1},\ldots,q_{K}) of pairwise coprime bases ≥ 2 \geq 2. It would also be interesting to prove the existence of infinitely many Catalan numbers *exactly divisible*by some power of a a, where a ≥ 2 a\geq 2 is an arbitrary integer. This property can be defined by

 | a k | n ⇔ ( a k ∣ n ​ and ​ gcd ⁡ ( n ​ a − k, a) = 1). a^{k}\|n\Leftrightarrow\left(a^{k}\mid n\hskip 5.69054pt\mbox{{and}}\hskip 2.84526pt\gcd(na^{-k},a)=1\right). |  | (71) |

6. 6.

Study collisions of integer-valued k k -*regular sequences*[2, 3] in coprime bases, generalizing the sum-of-digits case.

### Acknowledgements.

The author is grateful to Michael Drmota and Joël Rivat, who introduced him to digital expansions as a research topic, and to Thomas Stoll for proposing related research problems to him. Moreover, he thanks Jean-Marc Deshouillers for pointing out the article [12], which was the starting point for the work on the present paper.

## References

- [1] B. Adamczewski and C. Faverjon, Mahler’s method in several variables and finite automata, 2020.
- [2] J.-P. Allouche and J. Shallit, The ring of k k -regular sequences, Theoret. Comput. Sci., 98 (1992), pp. 163–197.
- [3], The ring of k k -regular sequences. II, Theoret. Comput. Sci., 307 (2003), pp. 3–29. Words.
- [4] A. Baker, Linear forms in the logarithms of algebraic numbers, Mathematika, 13 (1966), pp. 204–216.
- [5] A. Baker, Linear forms in the logarithms of algebraic numbers. II, Mathematika, 14 (1967), pp. 102–107.
- [6], Linear forms in the logarithms of algebraic numbers. III, Mathematika, 14 (1967), pp. 220–228.
- [7] V. Berthé, Autour du système de numération d’Ostrowski, Bull. Belg. Math. Soc. Simon Stevin, 8 (2001), pp. 209–239. Journées Montoises d’Informatique Théorique (Marne-la-Vallée, 2000).
- [8] J. Bésineau, Indépendance statistique d’ensembles liés à la fonction “somme des chiffres”, Acta Arith., 20 (1972), pp. 401–416.
- [9] J. J. Bravo and F. Luca, On the Diophantine equation F n + F m = 2 a F_{n}+F_{m}=2^{a}, Quaest. Math., 39 (2016), pp. 391–400.
- [10] Y. Bugeaud, M. Cipu, and M. Mignotte, On the representation of Fibonacci and Lucas numbers in an integer base, Ann. Math. Qué., 37 (2013), pp. 31–43.
- [11] R. de la Bretèche, T. Stoll, and G. Tenenbaum, Somme des chiffres et changement de base, Ann. Inst. Fourier, 69 (2019), pp. 2507–2518.
- [12] J.-M. Deshouillers, L. Habsieger, S. Laishram, and B. Landreau, Sums of the digits in bases 2 2 and 3 3, in Number theory — Diophantine problems, uniform distribution and applications, Springer, 2017, pp. 211–217.
- [13] V. S. Dimitrov and E. W. Howe, Powers of 3 3 with few nonzero bits and a conjecture of Erdős, 2021.
- [14] M. Drmota, The joint distribution of q q -additive functions, Acta Arith., 100 (2001), pp. 17–39.
- [15] M. Drmota, C. Mauduit, and J. Rivat, Primes with an average sum of digits, Compos. Math., 145 (2009), pp. 271–292.
- [16], Normality along squares, J. Eur. Math. Soc. (JEMS), 21 (2019), pp. 507–548.
- [17] M. Drmota, C. Mauduit, and J. Rivat, Prime numbers in two bases, Duke Math. J., 169 (2020), pp. 1809–1876.
- [18] M. Drmota and J. F. Morgenbesser, Generalized Thue-Morse sequences of squares, Isr. J. Math., 190 (2012), pp. 157–193.
- [19] M. Drmota, J. Rivat, and T. Stoll, The sum of digits of primes in ℤ ⁡ [i] \mathbb{Z}[i], Monatsh. Math., 155 (2008), pp. 317–347.
- [20] P. Erdős, Some unconventional problems in number theory, Math. Mag., 52 (1979), pp. 67–70.
- [21] P. Erdős and R. L. Graham, Old and new problems and results in combinatorial number theory, vol. 28, L’Enseignement Mathématique, Université de Genève, Genève, 1980.
- [22] H. Furstenberg, Intersections of Cantor sets and transversality of semi-groups. Probl. Analysis, Sympos. in Honor of Salomon Bochner, Princeton Univ. 1969, 41-59 (1970)., 1970.
- [23] A. Gelfond, Sur le septième problème de D. Hilbert, C. R. (Dokl.) Acad. Sci. URSS, n. Ser., 1934 (1934), pp. 1–6.
- [24], Sur le septième Problème de Hilbert, Bull. Acad. Sci. URSS, 1934 (1934), pp. 623–634.
- [25] A. O. Gel’fond, Sur les nombres qui ont des propriétés additives et multiplicatives données, Acta Arith., 13 (1967/68), pp. 259–265.
- [26] A. Granville and O. Ramaré, Explicit bounds on exponential sums and the scarcity of squarefree binomial coefficients, Mathematika, 43 (1996), pp. 73–107.
- [27] B. Kerr, L. Mérai, and I. E. Shparlinski, On digits of mersenne numbers, 2021.
- [28] D.-H. Kim, On the joint distribution of q q -additive functions in residue classes, J. Number Theory, 74 (1999), pp. 307–336.
- [29] J. C. Lagarias, Ternary expansions of powers of 2 2, J. Lond. Math. Soc., II. Ser., 79 (2009), pp. 562–588.
- [30] F. Luca, On the Diophantine equation p x 1 − p x 2 = q y 1 − q y 2 p^{x_{1}}-p^{x_{2}}=q^{y_{1}}-q^{y_{2}}, Indag. Math., New Ser., 14 (2003), pp. 207–222.
- [31] B. Martin, C. Mauduit, and J. Rivat, Théorème des nombres premiers pour les fonctions digitales, Acta Arith., 165 (2014), pp. 11–45.
- [32], Fonctions digitales le long des nombres premiers, Acta Arith., 170 (2015), pp. 175–197.
- [33], Nombres premiers avec contraintes digitales multiples, Bull. Soc. Math. Fr., 147 (2019), pp. 259–287.
- [34], Propriétés locales des chiffres des nombres premiers, J. Inst. Math. Jussieu, 18 (2019), pp. 189–224.
- [35] C. Mauduit, C. Pomerance, and A. Sárközy, On the distribution in residue classes of integers with a fixed sum of digits, Ramanujan J., 9 (2005), pp. 45–62.
- [36] C. Mauduit and J. Rivat, La somme des chiffres des carrés, Acta Math., 203 (2009), pp. 107–148.
- [37], Sur un problème de Gelfond: la somme des chiffres des nombres premiers, Ann. of Math. (2), 171 (2010), pp. 1591–1646.
- [38], Prime numbers along Rudin-Shapiro sequences, J. Eur. Math. Soc. (JEMS), 17 (2015), pp. 2595–2642.
- [39] C. Mauduit and J. Rivat, Rudin-Shapiro sequences along squares, Trans. Am. Math. Soc., 370 (2018), pp. 7899–7921.
- [40] C. Mauduit and A. Sárközy, On the arithmetic structure of the integers whose sum of digits is fixed, Acta Arith., 81 (1997), pp. 145–173.
- [41] J. Maynard, Primes with restricted digits, Invent. Math., 217 (2019), pp. 127–218.
- [42] M. Mignotte, Sur les entiers qui s’écrivent simplement en différentes bases. (On integers simply represented in different bases), Eur. J. Comb., 9 (1988), pp. 307–316.
- [43] J. F. Morgenbesser and T. Stoll, On a problem of Chen and Liu concerning the prime power factorization of n! n!, Proc. Am. Math. Soc., 141 (2013), pp. 2289–2297.
- [44] C. Müllner, Automatic sequences fulfill the Sarnak conjecture, Duke Math. J., 166 (2017), pp. 3219–3290.
- [45] C. Müllner, The Rudin-Shapiro sequence and similar sequences are normal along squares, Can. J. Math., 70 (2018), pp. 1096–1129.
- [46] N. Ouled Azaiez, M. Mkaouar, and J. M. Thuswaldner, Sur les chiffres des nombres premiers translatés, Funct. Approximatio, Comment. Math., 51 (2014), pp. 237–267.
- [47] A. Pethő and R. F. Tichy, S S -unit equations, linear recurrences and digit expansions, Publ. Math., 42 (1993), pp. 145–154.
- [48] G. Rhin, Approximants de Padé et mesures effectives d’irrationalité. Théorie des Nombres, Sémin. Paris 1985/86, Prog. Math. 71, 155-164 (1987)., 1987.
- [49] A. Sárközy, On divisors of binomial coefficients. I, J. Number Theory, 20 (1985), pp. 70–80.
- [50] H. P. Schlickewei, Linear equations in integers with bounded sum of digits, J. Number Theory, 35 (1990), pp. 335–344.
- [51], S-unit equations over number fields, Invent. Math., 102 (1990), pp. 95–107.
- [52] H. G. Senge and E. G. Straus, PV-numbers and sets of multiplicity, Period. Math. Hung., 3 (1973), pp. 93–100.
- [53] P. Shmerkin, On Furstenberg’s intersection conjecture, self-similar measures, and the L q L^{q} norms of convolutions, Ann. Math. (2), 189 (2019), pp. 319–391.
- [54] N. J. A. Sloane, The On-Line Encyclopedia of Integer Sequences, 2021. Published electronically at https://oeis.org.
- [55] L. Spiegelhofer, The level of distribution of the Thue–Morse sequence, Compos. Math., 156 (2020), pp. 2560–2587.
- [56], A lower bound for Cusick’s conjecture on the digits of n + t n+t, Math. Proc. Cambridge Philos. Soc., (2020). Published online by Cambridge University Press: 24 February 2021, pp. 1-23.
- [57] L. Spiegelhofer and M. Wallner, The binary digits of n + t n+t, 2021. Accepted for publication in Ann. Sc. norm. super. Pisa – Cl. sci. Preprint available on arXiv.
- [58] C. L. Stewart, On the representation of an integer in two different bases, J. Reine Angew. Math., 319 (1980), pp. 63–72.
- [59] M. Wu, A proof of Furstenberg’s conjecture on the intersections of × p \times p - and × q \times q -invariant sets, Ann. Math. (2), 189 (2019), pp. 707–751.
- [60] Q. Wu and L. Wang, On the irrationality measure of log ⁡ 3 \log 3, J. Number Theory, 142 (2014), pp. 264–273.
- [61] V. Ziegler, Effective results for linear equations in members of two recurrence sequences, Acta Arith., 190 (2019), pp. 139–169.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
