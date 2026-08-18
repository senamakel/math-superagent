<!-- source: https://ar5iv.labs.arxiv.org/html/1105.5810 | converted from HTML -->

[1105.5810] Substitutions and 1 2 -Discrepancy of { + ⁢ n θ x }

# Substitutions and 1 2 \frac{1}{2} -Discrepancy of { n ​ θ + x } \{n\theta+x\}

David Ralston Email address: [ralston.david.s@gmail.com][1] Address: Ben Gurion University, Department of Mathematics
POB 653
Beer Sheva 84105
ISRAEL

Date: August 8, 2026

###### Abstract.

The sequence of 1 / 2 1/2 -discrepancy sums of { x + i ​ θ mod 1 } \{x+i\theta\bmod 1\} is realized through a sequence of substitutions on an alphabet of three symbols; particular attention is paid to x = 0 x=0. The first application is to show that any asymptotic growth rate of the discrepancy sums not trivially forbidden may be achieved. A second application is to show that for badly approximable θ \theta and any x x the range of values taken over i = 0, 1, … ​ n − 1 i=0,1,\ldots n-1 is asymptotically similar to log ⁡ ( n) \log(n), a stronger conclusion than given by the Denjoy-Koksma inequality.

###### Key words and phrases:

discrepancy, irrational rotation, renormalization, substitution

###### 2010 Mathematics Subject Classification

Primary: 11K38, Secondary: 37E20, 37B10

## 1. Introduction

Given an irrational θ \theta and some x ∈ [0, 1) = S 1 x\in[0,1)=S^{1} (all addition in S 1 S^{1} is taken modulo one), let

(1) |  | f ⁡ ( x) = χ [0, 1 / 2) ​ ( x) − χ [1 / 2, 1) ​ ( x). f(x)=\chi_{[0,1/2)}(x)-\chi_{[1/2,1)}(x). |  |

With θ \theta fixed, the 1 / 2 1/2 -discrepancy sums of the sequence { x + i ​ θ } \{x+i\theta\} are given by

 | S n ​ ( x) = ∑ i = 0 n − 1 f ⁡ ( x + i ​ θ). S_{n}(x)=\sum_{i=0}^{n-1}f(x+i\theta). |  |

Two results are classical in this setting, for any irrational θ \theta and for all x x:

(2) |  | S n ​ ( x) ∈ o ⁡ ( n), S n ​ ( x) ∉ O ⁡ ( 1). S_{n}(x)\in o(n),\quad S_{n}(x)\notin O(1). |  |

The first restriction is due to unique ergodicity of the underlying rotation, and the second is a theorem of Kesten [5].

We will use standard continued fraction notation; partial quotients are denoted a i ​ ( θ) a_{i}(\theta), and convergents are denoted p i ​ ( θ) / q i ​ ( θ) p_{i}(\theta)/q_{i}(\theta). When θ \theta is clear from context we will simply write a i a_{i}, p i p_{i} and q i q_{i}. The distance from x x to the nearest integer is denoted ‖ x ‖ \|x\|. As θ ∈ ( 0, 1) \theta\in(0,1) without loss of generality, we will assume that a 0 ​ ( θ) = 0 a_{0}(\theta)=0 and omit this term, writing simply

 | θ = [a 1, a 2, a 3, …] = 1 a 1 + 1 a 2 + 1 a 3 + ⋱. \theta=[a_{1},a_{2},a_{3},\ldots]=\cfrac{1}{a_{1}+\cfrac{1}{a_{2}+\cfrac{1}{a_{3}+\ddots}}}. |  |

All necessary background in continued fractions may be found in [6]. The Gauss map will be denoted by γ \gamma, and acts as the non-invertible shift on the sequence of partial quotients:

(3) |  | γ ⁡ ( θ) = 1 θ mod 1, γ ⁡ ( [a 1, a 2, …]) = [a 2, a 3, …]. \gamma(\theta)=\frac{1}{\theta}\bmod 1,\quad\gamma([a_{1},a_{2},\ldots])=[a_{2},a_{3},\ldots]. |  |

Our goal is to investigate what behavior is possible for the sequence S n ​ ( x) S_{n}(x) within the constraints of ( 2). Because the sequence S n S_{n} is not monotone, however, it will be more convenient to consider the following sequences, which track the maximal and minimal discrepancies, as well as the range of values taken:

(4) |  | M n ( x) = max { S i ( x): i = 1, …, n − 1 }, \displaystyle M_{n}(x)=\max\{S_{i}(x):i=1,\ldots,n-1\}, |  |

(5) |  | m n ( x) = min { S i ( x): i = 1, …, n − 1 }, \displaystyle m_{n}(x)=\min\{S_{i}(x):i=1,\ldots,n-1\}, |  |

(6) |  | ρ n ​ ( x) = M n ​ ( x) − m n ​ ( x) + 1. \displaystyle\rho_{n}(x)=M_{n}(x)-m_{n}(x)+1. |  |

It is worth clarifying that m n m_{n} is taken as a minimum over integers, and as such can generally be expected to be negative. It is a matter of later convenience that i = 0 i=0 is not considered: for example, M 1 ​ ( 0) = m 1 ​ ( 0) = S 1 ​ ( 0) = 1 M_{1}(0)=m_{1}(0)=S_{1}(0)=1.

We will develop a renormalization procedure through which the sequence of values f ⁡ ( x + i ​ θ) f(x+i\theta) can be determined from a sequence of substitutions. Let θ < 1 / 2 \theta<1/2 and A = [0, 1 / 2) A=[0,1/2), B = [1 / 2, 1 − θ) B=[1/2,1-\theta), C = [1 − θ, 1) C=[1-\theta,1). If we wish to change which interval certain endpoints belong to (for example, if we wish for A A to be closed and B B to be open), we will say that we make a change of endpoints of the intervals A A, B B, and C C. Our central result is the following:

###### Theorem 1.1.

Given any irrational θ \theta and any x ∈ [0, 1) x\in[0,1), there is a sequence of words ω i \omega_{i} (some of which may be empty) and substitutions σ i \sigma_{i} (infinitely many are not identity) both defined on the alphabet { A, B, C } \{A,B,C\}, given by a dynamic process depending on x x and θ \theta, such that the infinite word given by

(7) |  | ω 0 ​ σ 0 ​ ( ω 1 ​ σ 1 ​ ( ω 2 ​ σ 2 ​ ( …))) \omega_{0}\sigma_{0}\left(\omega_{1}\sigma_{1}\left(\omega_{2}\sigma_{2}(\ldots)\right)\right) |  |

encodes the orbit of x x up to at most two errors. Alternately, the coding is exact up to a change of endpoints of the intervals A A, B B and C C. The dependence of σ i \sigma_{i} on θ \theta and ω i \omega_{i} on ( x, θ) (x,\theta) is explicit.

There is one special point x ⁡ ( θ) x(\theta) for which all ω i \omega_{i} may be taken to be the empty word, in which case the infinite word

(8) |  | lim n → ∞ ( σ 0 ∘ σ 1 ∘ ⋯ ∘ σ n − 1) ( ω) \lim_{n\rightarrow\infty}\left(\sigma_{0}\circ\sigma_{1}\circ\cdots\circ\sigma_{n-1}\right)(\omega) |  |

will encode the orbit of x ⁡ ( θ) x(\theta) regardless of the choice of nonempty word ω \omega. The orbit of zero can alternately be determined by

(9) |  | lim n → ∞ ( σ 0 ′ ∘ σ 1 ′ ∘ ⋯ ∘ σ n − 1 ′) ( ω n − 1 ′), \lim_{n\rightarrow\infty}\left(\sigma^{\prime}_{0}\circ\sigma^{\prime}_{1}\circ\cdots\circ\sigma^{\prime}_{n-1}\right)(\omega^{\prime}_{n-1}), |  |

where σ n ′ \sigma^{\prime}_{n} are either substitutions or a different map. This distinction and the word ω n ′ \omega^{\prime}_{n} are explicitly presented.

We will include some remarks regarding the point x ⁡ ( θ) x(\theta) (including a complete characterization of those θ \theta for which x ⁡ ( θ) = 0 x(\theta)=0 in Proposition 4.3), as well as proving that the sequence of substitutions σ i \sigma_{i} is eventually periodic if and only if θ \theta is a quadratic surd (Proposition 4.4).

As ( 0, 1 / 2) ⊂ A (0,1/2)\subset A and ( 1 / 2, 1) ⊂ ( B ∪ C) (1/2,1)\subset(B\cup C), any change of endpoints is completely irrelevant to the asymptotic growth rates of M n ​ ( x) M_{n}(x), m n ​ ( x) m_{n}(x), and ρ n ​ ( x) \rho_{n}(x). While Theorem 1.1 provides a way to produce the orbit of an arbitrary point, computation of the words ω i \omega_{i} is a nontrivial task. However, for the special point x ⁡ ( θ) x(\theta) and for 0 0, the process is much simpler. We will show that given any growth condition that does not violate ( 2), such behavior is seen to be possible:

###### Theorem 1.2.

Suppose that { c n } \{c_{n}\} and { d n } \{d_{n}\} are two increasing sequences of positive real numbers, both in o ⁡ ( n) o(n), the differences

 | Δ ​ c n = c n + 1 − c n \Delta c_{n}=c_{n+1}-c_{n} |  |

are in O ⁡ ( 1) O(1) (similarly for { Δ ​ d n } \{\Delta d_{n}\}), and at least one of { c n } \{c_{n}\}, { d n } \{d_{n}\} is divergent. Then there is a dense set of θ \theta such that if { c n } \{c_{n}\} is divergent, then

 | lim sup n → ∞ M n ​ ( 0) c n = 1, \limsup_{n\rightarrow\infty}\frac{M_{n}(0)}{c_{n}}=1, |  |

while if { c n } \{c_{n}\} is bounded then so is M n ​ ( 0) M_{n}(0). Similarly, if { d n } \{d_{n}\} is divergent, then

 | lim sup n → ∞ | m n ​ ( 0) | d n = 1, \limsup_{n\rightarrow\infty}\frac{|m_{n}(0)|}{d_{n}}=1, |  |

while if { d n } \{d_{n}\} is bounded then so is m n ​ ( 0) m_{n}(0).

A closely related result concerns the sequence of values M n ​ ( x) / | m n ​ ( x) | M_{n}(x)/|m_{n}(x)|:

###### Theorem 1.3.

Let 0 ≤ r 1 ≤ r 2 ≤ ∞ 0\leq r_{1}\leq r_{2}\leq\infty. Then there is a dense set of θ \theta such that the set of accumulation points of the sequence

 | { M n ​ ( 0) | m n ​ ( 0) |: n = 0, 1, 2, … } \left\{\frac{M_{n}(0)}{|m_{n}(0)|}:n=0,1,2,\ldots\right\} |  |

is the interval [r 1, r 2] [r_{1},r_{2}].

We will also include a partial rederivation of [2, Theorem 1] in Corollary 5.3: a characterization of those θ \theta for which S n ​ ( θ) ≥ 0 S_{n}(\theta)\geq 0 for all n ≥ 0 n\geq 0.

A classical application of the Denjoy-Koksma inequality is that if the a i ​ ( θ) a_{i}(\theta) are drawn from a finite set (such θ \theta are said to be badly approximable or of finite type), then S n ​ ( x) ∈ O ⁡ ( log ⁡ n) S_{n}(x)\in O(\log n).

###### Theorem 1.4.

If θ \theta is of finite type, then for all x x we have ρ n ​ ( x) ∼ log ⁡ n \rho_{n}(x)\sim\log n, meaning that the ratio is bounded away from both zero and infinity.

###### Corollary 1.5.

If θ \theta is of finite type, then | S n ​ ( x) | ∉ o ⁡ ( log ⁡ n) |S_{n}(x)|\notin o(\log n) for every x x, and

 | m n ​ ( x) ∈ o ⁡ ( log ⁡ n) ⟹ M n ​ ( x) ∼ log ⁡ n, m_{n}(x)\in o(\log n)\quad\Longrightarrow\quad M_{n}(x)\sim\log n, |  |

and vice-versa.

If A ∪ B A\cup B represents a single interval, then as S 1 S^{1} has been partitioned into two intervals of length θ \theta and 1 − θ 1-\theta, the analogous problem would be to encode the Sturmian sequences, and generating Sturmian sequences using a sequence of substitutions is intimately related to continued fraction expansions for numbers: see for example [3, Chapter 6]. The study of substitutions as they relate to discrepancy sequences of different intervals has been initiated before [1], in this paper our approach is different:

- •

the interval [0, 1 / 2] [0,1/2] is not dynamically defined, i.e. not dependent on θ \theta (although it is fixed),

- •

we develop an approach for all θ \theta (not just quadratic surds, though the process is nicest in this setting),

- •

we generate the orbit of any starting point x x (though x = 0 x=0 is one particularly nice case that we investigate).

## 2. Symbol Spaces, Encodings, and Substitutions

All background material pertaining to common definitions in symbolic dynamics and substitution systems may be found in [3, Chapter 1]; we present here only a short summary of specific notation used herein. Let 𝒜 = { A, B, C } \mathcal{A}=\{A,B,C\}, and denote by 𝒜 ∗ \mathcal{A}^{*} the free monoid on 𝒜 \mathcal{A}. Given ω ∈ 𝒜 ∗ \omega\in\mathcal{A}^{*}, we denote

 | ω = ( ω) 0 ​ ( ω) 1 ​ … ​ ( ω) n − 1, \omega=(\omega)_{0}(\omega)_{1}\ldots(\omega)_{n-1}, |  |

and say that ω \omega is a word of length n n with letters ( ω) i (\omega)_{i} drawn from the alphabet 𝒜 \mathcal{A}. Note that ω i \omega_{i} will refer to a sequence of words indexed by i i, while ( ω) i (\omega)_{i} will denote the individual letters of a fixed word ω \omega. This similarity is a potential source of confusion, but the latter notation is much more common in this work: we will rarely refer to specific letters in a given word.

Denote by | ω | |\omega| the length of ω \omega. Elements in 𝒜 ∗ \mathcal{A}^{*} multiply by concatenation, and we adopt power notation for this operation: ( A ​ B) 3 = A ​ B ​ A ​ B ​ A ​ B (AB)^{3}=ABABAB, for example. The empty word (the identity under concatenation) we denote ∅ \emptyset. A factor of ω \omega (of finite or infinite length) is some finite word ψ \psi of length n n such that there is some i i for which

 | ( ψ) j = ( ω) i + j, j = 0, 1, …, n − 1. (\psi)_{j}=(\omega)_{i+j},\quad j=0,1,\ldots,n-1. |  |

If i = 0 i=0 then we say ψ \psi is an left factor of ω \omega, and we say ψ \psi is a right factor of ω \omega if ( ψ) n − 1 = ( ω) | ω | − 1 (\psi)_{n-1}=(\omega)_{|\omega|-1}. The factor ψ \psi will be called proper if ψ ∉ { ω, ∅ } \psi\notin\{\omega,\emptyset\}.

Any map σ: 𝒜 → 𝒜 ∗ \sigma:\mathcal{A}\rightarrow\mathcal{A}^{*} may be extended to a map on 𝒜 ∗ \mathcal{A}^{*} be requiring it to be a homomorphism. The following is nonstandard but natural. Endow 𝒜 ℕ \mathcal{A}^{\mathbb{N}} with the cylinder topology, and let a finite word ω ∈ 𝒜 ∗ \omega\in\mathcal{A}^{*} represent a clopen set: the set of all elements of 𝒜 ℕ \mathcal{A}^{\mathbb{N}} with left factor ω \omega. We may then further extended σ \sigma to a map on 𝒜 ℕ \mathcal{A}^{\mathbb{N}} by defining

 | σ ⁡ ( ω) = ⋂ i = 0 ∞ σ ⁡ ( ( ω) 0 ​ ( ω) 1 ​ … ​ ( ω) i − 1). \sigma(\omega)=\bigcap_{i=0}^{\infty}\sigma((\omega)_{0}(\omega)_{1}\ldots(\omega)_{i-1}). |  |

In all of these situations we refer to σ \sigma as a substitution.

Given a sequence of words ω 0, ω 1, … \omega_{0},\omega_{1},\ldots such that ω i \omega_{i} is a left factor of ω i + 1 \omega_{i+1}, if

 | ⋂ i = 0 ∞ ω i = { x }, \bigcap_{i=0}^{\infty}\omega_{i}=\{x\}, |  |

then we say that x ∈ 𝒜 ℕ x\in\mathcal{A}^{\mathbb{N}} is the limit of the words ω i \omega_{i}.

Now consider the space S 1 = [0, 1) S^{1}=[0,1) with the map R θ ​ ( x) = x + θ mod 1 R_{\theta}(x)=x+\theta\mod 1 for some irrational θ \theta. Suppose that X X is partitioned into three intervals A A, B B, and C C. Then given a word ω \omega, we say that ω \omega encodes the orbit of x x if for all i ≤ | ω | − 1 i\leq|\omega|-1 we have

 | ( ω) i = A ⟺ x + i θ ∈ A, (\omega)_{i}=A\quad\Longleftrightarrow\quad x+i\theta\in A, |  |

and similarly for B B and C C. Given a partition, then, to each x ∈ S 1 x\in S^{1} we may identify an infinite word ω ∈ Ω \omega\in\Omega: the infinite word which encodes the (forward) orbit of x x.

Let 𝒟 \mathcal{D} be the discontinuities of ( f ∘ R θ i) ​ ( x) (f\circ R_{\theta}^{i})(x) for i = 0, 1, 2, … i=0,1,2,\ldots:

 | 𝒟 = { − i θ, − i θ + 1 / 2 }, i = 0, 1, 2, …. \mathcal{D}=\{-i\theta,-i\theta+1/2\},\quad i=0,1,2,\ldots. |  |

For each x ∈ 𝒟 x\in\mathcal{D}, then, we replace x ∈ S 1 x\in S^{1} with two points, a right and left limit, denoted x + x^{+} and x − x^{-}. We set

 | R θ ​ ( 0 +) = R θ ​ ( 1 −) = θ, R_{\theta}(0^{+})=R_{\theta}(1^{-})=\theta, |  |

and similarly for ( 1 / 2) ± (1/2)^{\pm}; while this makes the rotation two-to-one at these points, note that with respect to the alphabet 𝒜 \mathcal{A}, the symbolic coding for the forward orbit of θ + \theta^{+} and θ − \theta^{-} are identical, so we do not distinguish them. We still denote our space by S 1 S^{1}. We may now make each of A A, B B and C C closed, although we have made S 1 S^{1} totally disconnected.

Given an irrational θ \theta, partition S 1 = [0 +, 1 −] S^{1}=[0^{+},1^{-}] according to Table 1 and in a slight abuse of notation let S 1 S^{1} be the set of all words which encode orbits with respect to these conventions.

θ < 1 / 2 \theta<1/2 | θ > 1 / 2 \theta>1/2 |

A = [0 +, 1 2 −] A=\left[0^{+},\frac{1}{2}^{-}\right] | C = [0 +, ( 1 − θ) −] C=\left[0^{+},(1-\theta)^{-}\right] |

B = [1 2 +, ( 1 − θ) −] B=\left[\frac{1}{2}^{+},(1-\theta)^{-}\right] | B = [( 1 − θ) +, 1 2 −] B=\left[(1-\theta)^{+},\frac{1}{2}^{-}\right] |

C = [( 1 − θ) +, 1] C=\left[(1-\theta)^{+},1\right] | A = [1 2 +, 1 −] A=\left[\frac{1}{2}^{+},1^{-}\right] |

Table 1. The partition S 1 = A ∪ B ∪ C S^{1}=A\cup B\cup C depending on θ \theta.

The following lemma is immediate, and immediately explains the apparent ambiguity in the statement of Theorem 1.1:

###### Lemma 2.1.

If ω \omega is an infinite word encoding the orbit of a point x ∈ S 1 x\in S^{1} under rotation by θ \theta, then ω \omega encodes the orbit of some x ∈ S 1 x\in S^{1} without the introduction of 𝒟 \mathcal{D} with at most two errors. Alternately the coding is exact up a change of endpoints of the intervals A A, B B and C C.

###### Proof.

The orbit of any point can hit the endpoints of A A, B B and C C at most twice. ∎

## 3. The Renormalization Procedure

Recall γ \gamma, the Gauss map ( 3); we define a similar map.

(10) |  | g ⁡ ( [a 1, a 2, a 3, …]) = { [a 3, a 4, …] = γ 2 ​ ( θ) ( a 1 = 0 mod 2) [1, a 2, a 3, …] = 1 1 + γ ⁡ ( θ) ( a 1 = 1 mod 2, a 1 ≠ 1) [a 2 + 1, a 3, …] = 1 − θ ( a 1 = 1). g([a_{1},a_{2},a_{3},\ldots])=\begin{cases}[a_{3},a_{4},\ldots]=\gamma^{2}(\theta)&(a_{1}=0\bmod 2)\\ [1,a_{2},a_{3},\ldots]=\frac{1}{1+\gamma(\theta)}&(a_{1}=1\bmod 2,\,a_{1}\neq 1)\\ [a_{2}+1,a_{3},\ldots]=1-\theta&(a_{1}=1).\end{cases} |  |

Note that if θ > 1 / 2 \theta>1/2, then necessarily g ⁡ ( θ) < 1 / 2 g(\theta)<1/2. It will be convenient to define

(11) |  | E ( x) = max { n ≤ x: n ∈ ℤ, n = 0 mod 2 }. E(x)=\max\{n\leq x:n\in\mathbb{Z},\,n=0\bmod 2\}. |  |

The triplet { X, μ, T } \{X,\mu,T\} refers to a compact probability space { X, μ } \{X,\mu\} and a continuous transformation T T on X X which preserves μ \mu. Given irrational θ \theta, we denote

(12) |  | θ n = g n ​ ( θ), δ n = 1 − E ⁡ ( a 1 ​ ( θ n)) ​ θ n, I n = { S 1, μ, R θ n }. \theta_{n}=g^{n}(\theta),\quad\delta_{n}=1-E(a_{1}(\theta_{n}))\theta_{n},\quad I_{n}=\{S^{1},\mu,R_{\theta_{n}}\}. |  |

Note that δ n = 1 \delta_{n}=1 if and only if θ > 1 / 2 \theta>1/2; otherwise δ n < 1 / 2 \delta_{n}<1/2.

Partition each I n I_{n} into intervals A A, B B and C C according to Table 1, and recall that by convention we have disconnected each I n I_{n} such that all iterates of the characteristic functions of A A, B B and C C under R θ n i R^{i}_{\theta_{n}} are continuous. Given { X, μ, T } \{X,\mu,T\} and a set S ⊂ X S\subset X, the return time to S S is given by

 | n ⁡ ( x) = min ⁡ { n > 0: T n ​ ( x) ∈ S }. n(x)=\min\{n>0:T^{n}(x)\in S\}. |  |

As irrational rotations are minimal, n ⁡ ( x) n(x) will be defined for all x ∈ S 1 x\in S^{1} if S S is an interval of positive length. The induced system on S S is defined by

 | { S, μ | S, T | s }, \{S,\mu|_{S},T|_{s}\}, |  |

where T | S ​ ( x) = T n ⁡ ( x) ​ ( x) T|_{S}(x)=T^{n(x)}(x) for all x ∈ S x\in S. Define I n + 1 ′ ⊂ I n I_{n+1}^{\prime}\subset I_{n} by

 | I n + 1 ′ = [0 +, δ n −]. I^{\prime}_{n+1}=[0^{+},\delta_{n}^{-}]. |  |

Finally, define the substitutions σ n = σ ⁡ ( θ n) \sigma_{n}=\sigma(\theta_{n}) according to Table 2, and define the functions φ n = φ ⁡ ( θ n) \varphi_{n}=\varphi(\theta_{n}) according to:

(13) |  | φ ⁡ ( x) = { 1 − x ( a 1 ​ ( θ) = 1) δ n − 1 ​ x ( a 1 ​ ( θ) ≠ 1) \varphi(x)=\begin{cases}1-x&(a_{1}(\theta)=1)\\ \delta_{n}^{-1}x&(a_{1}(\theta)\neq 1)\end{cases} |  |

Case | Substitution |

a 1 = 2 ​ k, a 3 ≠ 1 a_{1}=2k,\,a_{3}\neq 1 | A → ( A k + 1 ​ B k − 1 ​ C) ​ ( A k ​ B k − 1 ​ C) a 2 − 1 A\rightarrow(A^{k+1}B^{k-1}C)(A^{k}B^{k-1}C)^{a_{2}-1} |

B → ( A k ​ B k ​ C) ​ ( A k ​ B k − 1 ​ C) a 2 − 1 B\rightarrow(A^{k}B^{k}C)(A^{k}B^{k-1}C)^{a_{2}-1} |

C → ( A k ​ B k ​ C) ​ ( A k ​ B k − 1 ​ C) a 2 C\rightarrow(A^{k}B^{k}C)(A^{k}B^{k-1}C)^{a_{2}} |

a 1 = 2 ​ k, a 3 = 1 a_{1}=2k,\,a_{3}=1 | A → ( A k ​ B k ​ C) ​ ( A k ​ B k − 1 ​ C) a 2 A\rightarrow(A^{k}B^{k}C)(A^{k}B^{k-1}C)^{a_{2}} |

B → ( A k + 1 ​ B k − 1 ​ C) ​ ( A k ​ B k − 1 ​ C) a 2 B\rightarrow(A^{k+1}B^{k-1}C)(A^{k}B^{k-1}C)^{a_{2}} |

C → ( A k + 1 ​ B k − 1 ​ C) ​ ( A k ​ B k − 1 ​ C) a 2 − 1 C\rightarrow(A^{k+1}B^{k-1}C)(A^{k}B^{k-1}C)^{a_{2}-1} |

a 1 = 2 ​ k + 1 a_{1}=2k+1 | A → A k ​ B k ​ C A\rightarrow A^{k}B^{k}C |

B → A k + 1 ​ B k − 1 ​ C B\rightarrow A^{k+1}B^{k-1}C |

C → A C\rightarrow A |

a 1 = 1 a_{1}=1 | A → A A\rightarrow A |

B → B B\rightarrow B |

C → C C\rightarrow C |

Table 2. The substitution σ \sigma as a function of θ \theta.

###### Lemma 3.1.

Suppose that θ < 1 / 2 \theta<1/2, E ​ ( a 1 ​ ( θ)) = 2 ​ k E(a_{1}(\theta))=2k, and

 | ( 1 − 2 ​ k ​ θ) + ≤ x ≤ ( 1 2 − ( k − 1) ​ θ) −. (1-2k\theta)^{+}\leq x\leq\left(\frac{1}{2}-(k-1)\theta\right)^{-}. |  |

Then the orbit of x x begins A k ​ B k − 1 ​ C A^{k}B^{k-1}C.

###### Proof.

The assumption θ < 1 / 2 \theta<1/2 tells us how to partition S 1 S^{1} according to Table 1 as well as guaranteeing that k ≥ 1 k\geq 1. Note that the lower inequality certainly guarantees that

 | 1 2 − k ​ θ < x ≤ ( 1 2 − ( k − 1) ​ θ) −, \frac{1}{2}-k\theta<x\leq\left(\frac{1}{2}-(k-1)\theta\right)^{-}, |  |

which tells us that x + i ​ θ ≤ ( 1 / 2) − x+i\theta\leq(1/2)^{-} for i = 0, 1, … ​ ( k − 1) i=0,1,\ldots(k-1), while x + k ​ θ > 1 / 2 x+k\theta>1/2. So the coding of the orbit of x x begins with exactly A k A^{k} before seeing either B B or C C. As we know

 | ( 1 − 2 ​ k ​ θ) + ≤ x < 1 − ( 2 ​ k − 1) ​ θ, \left(1-2k\theta\right)^{+}\leq x<1-(2k-1)\theta, |  |

we know that we have x + ( 2 ​ k − 1) ​ θ < 1 x+(2k-1)\theta<1, while x + 2 ​ k ​ θ ≥ 1 + x+2k\theta\geq 1^{+}. Therefore, once we have accounted for the points x + i ​ θ x+i\theta for i = 0, 1, …, k − 1 i=0,1,\ldots,k-1, the terms i = k, k + 1, …, ( 2 ​ k − 1) i=k,k+1,\ldots,(2k-1) must all belong to either B B or C C. That C C is an interval of length exactly θ \theta guarantees that exactly the final term is C C. The rest of the terms (if there are any) are therefore B B. ∎

###### Proposition 3.2.

We have the measurable and continuous isomorphism

 | { I n + 1 ′, μ | I n + 1 ′, ( R θ n) | I n + 1 } → φ n { I n + 1, μ, R θ n + 1 }. \left\{I^{\prime}_{n+1},\mu|_{I^{\prime}_{n+1}},\left(R_{\theta_{n}}\right)|_{I_{n+1}}\right\}\xrightarrow{\varphi_{n}}\left\{I_{n+1},\mu,R_{\theta_{n+1}}\right\}. |  |

Furthermore, for all x ∈ A ⊂ I n + 1 x\in A\subset I_{n+1}, the word σ n ​ ( A) \sigma_{n}(A) encodes the orbit of φ − 1 ​ ( x) \varphi^{-1}(x) through its return to I n + 1 ′ I_{n+1}^{\prime} (the encoding is with respect to the partition A A, B B, C C in I n I_{n}), and similarly for B B and C C.

###### Proof.

In the case that θ n > 1 / 2 \theta_{n}>1/2, then θ n + 1 = 1 − θ n \theta_{n+1}=1-\theta_{n} and I n + 1 ′ = [0 +, 1 −] I_{n+1}^{\prime}=[0^{+},1^{-}]. However, by referring to Table 1, we see that the intervals A A, B B and C C exactly reflect the reversal of orientation given by φ n ​ ( x) = 1 − x \varphi_{n}(x)=1-x, and the substitution σ n \sigma_{n} is identity. So we proceed on the assumption that θ n < 1 / 2 \theta_{n}<1/2: in I n I_{n} we have

 | A = [0 +, 1 / 2 −], B = [1 / 2 +, ( 1 − θ) −], C = [( 1 − θ) +, 1 −]. A=[0^{+},1/2^{-}],\quad B=[1/2^{+},(1-\theta)^{-}],\quad C=[(1-\theta)^{+},1^{-}]. |  |

Then φ n \varphi_{n} is scalar multiplication by δ n − 1 \delta_{n}^{-1}, so there are only two things to show:

- •

The first-return map ( R θ n) | I n + 1 ′ (R_{\theta_{n}})|_{I^{\prime}_{n+1}} is rotation by θ n + 1 \theta_{n+1}, after rescaling by φ n \varphi_{n}, and

- •

the substitution σ n \sigma_{n} encodes the correct information.

There are three cases to consider: a 1 ​ ( θ n) = 1 mod 2 a_{1}(\theta_{n})=1\bmod 2, or a 1 ​ ( θ n) = 0 mod 2 a_{1}(\theta_{n})=0\bmod 2 with the sub-cases a 3 ​ ( θ n) = 1 a_{3}(\theta_{n})=1 or ≠ 1 \neq 1. Assume for now that a 1 ​ ( θ n) = 0 mod 2 a_{1}(\theta_{n})=0\bmod 2 and a 3 ​ ( θ n) = 1 a_{3}(\theta_{n})=1.

As a 1 ​ ( θ n) = 0 mod 2 a_{1}(\theta_{n})=0\bmod 2 and a 3 ​ ( θ n) = 1 a_{3}(\theta_{n})=1, we have g ⁡ ( θ n) = γ 2 ​ ( θ n) > 1 / 2 g(\theta_{n})=\gamma^{2}(\theta_{n})>1/2, so in I n + 1 I_{n+1} we have

 | C = [0 +, ( 1 − θ n + 1) −], B = [( 1 − θ n + 1) +, 1 / 2 −], A = [1 / 2 +, 1 −], C=[0^{+},(1-\theta_{n+1})^{-}],\quad B=[(1-\theta_{n+1})^{+},1/2^{-}],\quad A=[1/2^{+},1^{-}], |  |

with corresponding preimages in I n + 1 ′ I^{\prime}_{n+1} scaled by δ n \delta_{n}. We will first verify that the intervals have the desired return times (which may be read from the length of the words σ n ​ ( A) \sigma_{n}(A), σ n ​ ( B) \sigma_{n}(B) and σ n ​ ( C) \sigma_{n}(C)) and that the induced map is indeed rotation by θ n + 1 \theta_{n+1} (up to scale δ n \delta_{n}). As E ⁡ ( a 1 ​ ( θ n)) = a 1 ​ ( θ n) E(a_{1}(\theta_{n}))=a_{1}(\theta_{n}) we have

 | δ n = ‖ q 1 ​ ( θ n) ⋅ θ n ‖, \delta_{n}=\|q_{1}(\theta_{n})\cdot\theta_{n}\|, |  |

from which it follows that the return time of 0 0 is

 | n ⁡ ( 0) = q 2 = a 1 ​ a 2 + 1, n(0)=q_{2}=a_{1}a_{2}+1, |  |

and one may now verify that the entire interval φ n − 1 ​ ( C) \varphi_{n}^{-1}(C) has this return time; the preimage of the right endpoint of C C under φ n \varphi_{n} is exactly 1 − ( q 1 + q 2) ​ θ n 1-(q_{1}+q_{2})\theta_{n}. The remaining points in I n + 1 ′ I^{\prime}_{n+1} have return time q 2 + q 1 q_{2}+q_{1} and the induced map is a rotation by q 2 ​ θ n q_{2}\theta_{n} on [0 +, δ n −] [0^{+},\delta_{n}^{-}]; see Figure 1.

∙ 0 \textstyle{\bullet_{0}\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces} q 2 \scriptstyle{\,q_{2}\,} φ n − 1 ​ ( C) \scriptstyle{\,\varphi_{n}^{-1}(C)\,} ∙ − ( q 1 + q 2) ​ θ n \textstyle{\bullet_{-(q_{1}+q_{2})\theta_{n}}\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces} φ n − 1 ​ ( A ∪ B) \scriptstyle{\,\varphi_{n}^{-1}(A\cup B)\,} q 1 + q 2 \scriptstyle{\,q_{1}+q_{2}\,} q 2 \scriptstyle{\,q_{2}\,} ∙ ‖ q 1 ​ ( θ n) ⋅ θ n ‖ \textstyle{\bullet_{\|q_{1}(\theta_{n})\cdot\theta_{n}\|}\ignorespaces\ignorespaces\ignorespaces\ignorespaces\ignorespaces} q 1 + q 2 \scriptstyle{\,q_{1}+q_{2}\,} ∙ 0 \textstyle{\bullet_{0}\ignorespaces\ignorespaces\ignorespaces\ignorespaces} ∙ ‖ q 2 ​ ( θ n) ​ θ n ‖ \textstyle{\bullet_{\|q_{2}(\theta_{n})\theta_{n}\|}\ignorespaces\ignorespaces\ignorespaces\ignorespaces} ∙ ‖ q 1 ​ ( θ n) ⋅ θ n ‖ \textstyle{\bullet_{\|q_{1}(\theta_{n})\cdot\theta_{n}\|}}

Figure 1. Return times for the case a 1 ​ ( θ n) = 0 mod 2 a_{1}(\theta_{n})=0\bmod 2, a 3 ​ ( θ n) = 1 a_{3}(\theta_{n})=1.

At this point we may verify that the rotation is by g ⁡ ( θ n) g(\theta_{n}), up to scale:

 | ‖ q 2 ​ ( θ n) ⋅ θ n ‖ δ n \displaystyle\frac{\|q_{2}(\theta_{n})\cdot\theta_{n}\|}{\delta_{n}} | = q 2 ​ ( θ n) ⋅ θ n − p 2 ​ ( θ n) 1 − q 1 ​ ( θ n) ⋅ θ n \displaystyle=\frac{q_{2}(\theta_{n})\cdot\theta_{n}-p_{2}(\theta_{n})}{1-q_{1}(\theta_{n})\cdot\theta_{n}} |  |

 |  | = ( a 1 ​ a 2 + 1) ​ θ n − a 2 1 − a 1 ​ θ n \displaystyle=\frac{(a_{1}a_{2}+1)\theta_{n}-a_{2}}{1-a_{1}\theta_{n}} |  |

 |  | = a 2 ​ ( a 1 − 1 θ n) + 1 1 θ n − a 1 \displaystyle=\frac{a_{2}\left(a_{1}-\frac{1}{\theta_{n}}\right)+1}{\frac{1}{\theta_{n}}-a_{1}} |  |

 |  | = 1 − a 2 ​ γ ​ ( θ n) γ ⁡ ( θ n) \displaystyle=\frac{1-a_{2}\gamma(\theta_{n})}{\gamma(\theta_{n})} |  |

 |  | = γ 2 ​ ( θ n). \displaystyle=\gamma^{2}(\theta_{n}). |  |

Now suppose that x ∈ φ − 1 ​ ( B) x\in\varphi^{-1}(B), and for convenience denote E ⁡ ( a 1) = a 1 = 2 ​ k E(a_{1})=a_{1}=2k. Clearly, the orbit of x x begins with a point in A A (in I n I_{n}, as A = [0 +, 1 / 2 −] A=[0^{+},1/2^{-}] contains [0 +, δ n −] [0^{+},\delta_{n}^{-}]). As x < 1 / 2 − k ​ θ n x<1/2-k\theta_{n}, however, we have

 | ( 1 − 2 ​ k ​ θ n) + ≤ x + θ n ≤ ( ( 1 / 2) − ( k − 1) ​ θ n) −, (1-2k\theta_{n})^{+}\leq x+\theta_{n}\leq\left((1/2)-(k-1)\theta_{n}\right)^{-}, |  |

so by Lemma 3.1, we may concatenate the word A k ​ B k − 1 ​ C A^{k}B^{k-1}C to this initial A A. Since 2 ​ k = a 1 2k=a_{1}, we now have

 | x + θ n + ( 2 ​ k ​ θ n) < x + θ n ≤ ( ( 1 / 2) − ( k − 1) ​ θ n) −. x+\theta_{n}+(2k\theta_{n})<x+\theta_{n}\leq\left((1/2)-(k-1)\theta_{n}\right)^{-}. |  |

Either we have returned to I n + 1 ′ I^{\prime}_{n+1}, in which case we are done, or we have not, in which case we apply Lemma 3.1 again, repeating until we return to I n + 1 ′ I^{\prime}_{n+1}, which must take a total of q 2 + q 1 = a 1 ​ ( a 2 + 1) + 1 q_{2}+q_{1}=a_{1}(a_{2}+1)+1 steps.

For those points in the interval φ n − 1 ​ ( a) \varphi_{n}^{-1}(a), note that the only discontinuity of R θ n i R_{\theta_{n}}^{i} for i = 0, 1, …, q 2 i=0,1,\ldots,q_{2} to distinguish the orbits compared to points in φ n − 1 ​ ( A) \varphi_{n}^{-1}(A) is the point 1 / 2 − k ​ θ 1/2-k\theta, which will change the single term x + k ​ θ x+k\theta from an ‘ A A ’ to a ‘ B B ’. Points in φ n − 1 ​ ( C) \varphi_{n}^{-1}(C) are considered identically to those in φ n − 1 ​ ( B) \varphi_{n}^{-1}(B), noting that the shorter return time requires one fewer concatenation of A a 1 ​ B a 1 − 1 ​ C A^{a_{1}}B^{a_{1}-1}C.

The other cases are similarly considered; the case a 1 ​ ( θ n) = 0 mod 2 a_{1}(\theta_{n})=0\bmod 2, a 3 ​ ( θ n) ≠ 1 a_{3}(\theta_{n})\neq 1 is nearly identical, while for the case a 1 ​ ( θ n) = 1 mod 1, ≠ 1 a_{1}(\theta_{n})=1\bmod 1,\,\neq 1 we have δ n > θ n \delta_{n}>\theta_{n}, so the return time of 0 + 0^{+} is one, explaining the much shorter substitution σ n ​ ( C) = A \sigma_{n}(C)=A in this case. ∎

Denote the iterated pull-back of I n I_{n} into I 0 I_{0} by

(14) |  | I ~ n = ( φ 0 − 1 ∘ ⋯ ∘ φ n − 1 − 1) ( I n). \tilde{I}_{n}=\left(\varphi_{0}^{-1}\circ\cdots\circ\varphi_{n-1}^{-1}\right)(I_{n}). |  |

###### Corollary 3.3.

We have the measurable and continuous isomorphism

 | { I ~ n, μ | I ~ n, ( R θ) | I ~ n } → ( φ n − 1 ∘ ⋯ ∘ φ 0) { I n, μ, R θ n }. \left\{\tilde{I}_{n},\mu|_{\tilde{I}_{n}},\left(R_{\theta}\right)|_{\tilde{I}_{n}}\right\}\xrightarrow{(\varphi_{n-1}\circ\cdots\circ\varphi_{0})}\left\{I_{n},\mu,R_{\theta_{n}}\right\}. |  |

Furthermore, for any x ∈ A ⊂ I n x\in A\subset I_{n}, the word ( σ 0 ∘ ⋯ ∘ σ n − 1) ( A) \left(\sigma_{0}\circ\cdots\circ\sigma_{n-1}\right)(A) encodes the orbit of ( φ 0 − 1 ∘ ⋯ ∘ φ n − 1 − 1) ( x) \left(\varphi_{0}^{-1}\circ\cdots\circ\varphi_{n-1}^{-1}\right)(x) in I 0 I_{0} through its return to I ~ n \tilde{I}_{n}, and similarly for B B, C C.

## 4. Proof of Theorem 1.1

The proof of ( 8) is immediate in light of Corollary 3.3; the point x ⁡ ( θ) x(\theta) is given by

 | x ⁡ ( θ) = ⋂ i = 0 ∞ I ~ i, x(\theta)=\bigcap_{i=0}^{\infty}\tilde{I}_{i}, |  |

where the I ~ i \tilde{I}_{i} were defined in ( 14). This intersection is nonempty as the sets are nested closed intervals in the compact space S 1 S^{1}. The length of I ~ n \tilde{I}_{n} is given by

 | δ 0 ⋅ δ 1 ⋯ δ n − 1, \delta_{0}\cdot\delta_{1}\cdots\delta_{n-1}, |  |

and we have already remarked that for θ n < 1 / 2 \theta_{n}<1/2, we have δ n < 1 / 2 \delta_{n}<1/2. As no two successive terms in the sequence θ 0, θ 1, … \theta_{0},\theta_{1},\ldots may be larger than one half, the length tends to zero, and the intersection is either a singleton or a pair { x −, x + } \{x^{-},x^{+}\}. In the latter scenario, however, both x − x^{-} and x + x^{+} would have identical coding of their forward orbits. As we did not ‘split’ the points i ​ θ i\theta or i ​ θ + 1 / 2 i\theta+1/2 for i > 0 i>0 when disconnecting S 1 S^{1}, this is not possible.

As all non-identity substitutions map each letter to a word beginning in A A, and all non-identity substitutions map A A to a word of length at least three, and no two consecutive substitutions may be identity, it follows that the sequence of words

 | ( σ 0 ∘ σ 1 ∘ ⋯ ∘ σ n − 1) ( ω) \left(\sigma_{0}\circ\sigma_{1}\circ\cdots\circ\sigma_{n-1}\right)(\omega) |  |

has a limit regardless of the choice of nonempty ω \omega, and Corollary 3.3 shows that this word must encode the orbit of x ⁡ ( θ) x(\theta) in the disconnected version of S 1 S^{1}. Lemma 2.1 finishes the proof of this portion of Theorem 1.1.

Let us now turn our attention to constructing the orbit of an arbitrary x 0 ∈ S 1 x_{0}\in S^{1}. Define

 | x 1 = x 0 + i ​ θ, i ∈ { j ≥ 0: x + j ​ θ ∈ I 1 ′ }, x_{1}=x_{0}+i\theta,\quad i\in\{j\geq 0:x+j\theta\in I^{\prime}_{1}\}, |  |

and let ω 0 \omega_{0} be the word which encodes the orbit of x 0 x_{0} through its arrival to x 1 x_{1}; if x 0 ∈ I 1 ′ x_{0}\in I^{\prime}_{1}, we may set ω 0 \omega_{0} to be the empty word (though we are not required to do so). We now pass to the system I 1 I_{1}, letting ( x 1 ∈ I 1) = φ 0 ​ ( x 1 ∈ I 1 ′) (x_{1}\in I_{1})=\varphi_{0}(x_{1}\in I^{\prime}_{1}). We set x 2 x_{2} to be a point in I 2 ′ I^{\prime}_{2} which is in the orbit of x 1 x_{1}, and let ω 1 \omega_{1} be the word encoding this finite portion of the orbit, then pass to I 2 I_{2}, etc. Equation ( 7) now follows from Proposition 3.2 so long as infinitely many ω n ≠ ∅ \omega_{n}\neq\emptyset. We only have the option of letting all but finitely many ω n \omega_{n} be empty if x x is a preimage of x ⁡ ( θ) x(\theta); we have already remarked in this case that the limiting word may be found handily.

A potential source of confusion at this point is the desire to claim that x ⁡ ( θ) = 0 x(\theta)=0, as we always construct I n + 1 ′ = [0 +, δ n −] I^{\prime}_{n+1}=[0^{+},\delta_{n}^{-}]. However, φ n ​ ( x) = 1 − x \varphi_{n}(x)=1-x for those n n such that θ n > 1 / 2 \theta_{n}>1/2. So φ n − 1 ∘ φ n + 1 − 1 \varphi_{n}^{-1}\circ\varphi_{n+1}^{-1} pulls back I n + 2 I_{n+2} to the interval [( 1 − δ n + 1) +, 1 −] ⊂ I n [(1-\delta_{n+1})^{+},1^{-}]\subset I_{n}. Those θ \theta for which x ⁡ ( θ) = 0 x(\theta)=0 will be addressed in Proposition 4.3.

###### Proposition 4.1.

Without loss of generality, ω n \omega_{n} may be required to either be empty, or a proper right factor of either σ n ​ ( A) \sigma_{n}(A), σ n ​ ( B) \sigma_{n}(B), or σ n ​ ( C) \sigma_{n}(C).

###### Proof.

The images of R θ n i ​ ( I n + 1 ′) R_{\theta_{n}}^{i}\left(I^{\prime}_{n+1}\right) cover all of I n I_{n} through the return times, so any x x may be viewed as returning to I n + 1 ′ I^{\prime}_{n+1} via a right factor of one of these words. If the return is through the entire word σ n ​ ( A) \sigma_{n}(A), we would have begun with x n ∈ I n + 1 ′ x_{n}\in I^{\prime}_{n+1} and could have set ω n = ∅ \omega_{n}=\emptyset. ∎

###### Remark.

One could alternately require that ω n \omega_{n} be nonempty by allowing all nonempty right factors of σ n ​ ( A) \sigma_{n}(A), σ n ​ ( B) \sigma_{n}(B), and σ n ​ ( C) \sigma_{n}(C); instead of ω n = ∅ \omega_{n}=\emptyset for x ∈ I n + 1 ′ x\in I^{\prime}_{n+1}, let ω n \omega_{n} be σ \sigma applied to the letter encoding whichever interval in I n + 1 I_{n+1} contains φ n ​ ( x) \varphi_{n}(x).

In order to construct the orbit of zero we will side-step this computation altogether:

###### Lemma 4.2.

Suppose that θ n > 1 / 2 \theta_{n}>1/2. Let Ω \Omega encode the orbit of 0 + 0^{+} in the system I n I_{n}, and Υ \Upsilon encode the orbit of 0 + 0^{+} in the system I n + 1 I_{n+1}. Then for all i ≥ 1 i\geq 1, ( Ω) i = ( Υ) i (\Omega)_{i}=(\Upsilon)_{i}. For i = 0 i=0, ( Ω) 0 = C (\Omega)_{0}=C while ( Υ) 0 = A (\Upsilon)_{0}=A.

###### Proof.

The isomorphism φ n ​ ( x) = 1 − x \varphi_{n}(x)=1-x and the identity substitution σ n \sigma_{n} ensures that Ω \Omega is identical to the coding of the orbit of 1 − 1^{-} in I n + 1 I_{n+1}. As the forward orbit of 0 0 under rotation by the irrational θ n \theta_{n} does not hit any other endpoints of the intervals A A, B B, and C C, we have that the orbit of 1 − 1^{-} and 0 + 0^{+} in the system I n + 1 I_{n+1} are identical after this initial term. ∎

With this lemma in mind, then, define the map Ψ ⁡ ( ω) \Psi(\omega) on both 𝒜 ∗ \mathcal{A}^{*} and 𝒜 ℕ \mathcal{A}^{\mathbb{N}}:

(15) |  | ( Ψ ​ ω) i = { C ( i = 0) ω i ( i ≠ 0). \left(\Psi\omega\right)_{i}=\begin{cases}C&(i=0)\\ \omega_{i}&(i\neq 0).\end{cases} |  |

Define the maps σ n ′ = σ ′ ​ ( θ n) \sigma^{\prime}_{n}=\sigma^{\prime}(\theta_{n}):

(16) |  | σ ′ ​ ( θ) = { σ ⁡ ( θ) ( θ < 1 / 2) Ψ ( θ > 1 / 2). \sigma^{\prime}(\theta)=\begin{cases}\sigma(\theta)&(\theta<1/2)\\ \Psi&(\theta>1/2).\end{cases} |  |

Then ( 9) follows if we appropriately choose the words ω n ′ \omega^{\prime}_{n} to accurately encode some string of the initial orbit of 0 + 0^{+} in I n I_{n}. Then the resulting word

 | ( σ 0 ′ ∘ σ 1 ′ ∘ ⋯ ∘ σ n − 1 ′) ( ω n ′) \left(\sigma_{0}^{\prime}\circ\sigma_{1}^{\prime}\circ\cdots\circ\sigma_{n-1}^{\prime}\right)(\omega^{\prime}_{n}) |  |

will accurately represent the initial orbit of 0 + 0^{+}, but it is no longer guaranteed that the length of this word increases! For example, if θ = [3, 2, 2, 2, 2, …] \theta=[3,2,2,2,2,\ldots], then we will alternate between σ n ′ \sigma_{n}^{\prime} being Ψ \Psi and a substitution which maps C → A C\rightarrow A. Setting ω n ′ = A \omega^{\prime}_{n}=A for all those n n for which θ n < 1 / 2 \theta_{n}<1/2 would therefore always map via this long string of compositions to

 | A → Ψ C → 𝜎 A → Ψ C → 𝜎 ⋯ A\xrightarrow{\Psi}C\xrightarrow{\sigma}A\xrightarrow{\Psi}C\xrightarrow{\sigma}\cdots |  |

Define

(17) |  | ω n ′ = { A k + 1 ​ B k − 1 ​ C ( a 1 ​ ( θ n) = 2 ​ k) A k + 1 ​ B k ( a 1 ​ ( θ) = 2 ​ k + 1) Ψ ⁡ ( ω n + 1 ′) ( a 1 ​ ( θ) = 1). \omega^{\prime}_{n}=\begin{cases}A^{k+1}B^{k-1}C&(a_{1}(\theta_{n})=2k)\\ A^{k+1}B^{k}&(a_{1}(\theta)=2k+1)\\ \Psi(\omega^{\prime}_{n+1})&(a_{1}(\theta)=1).\end{cases} |  |

The reader may verify that the word ω n ′ \omega^{\prime}_{n} does accurately encode some initial portion of the orbit of 0 + 0^{+} depending on the parity of a 1 ​ ( θ n) a_{1}(\theta_{n}). Note that whenever Ψ \Psi is applied, it affects only the first letter of its input. From this it follows that if ω = ( ω) 0 ​ ν \omega=(\omega)_{0}\nu, then

(18) |  | ( σ 0 ′ ∘ ⋯ ∘ σ n − 1 ′) ( ω) = ( σ 0 ′ ∘ ⋯ ∘ σ n − 1 ′) ( ( ω) 0) ( σ 0 ∘ ⋯ ∘ σ n − 1) ( ν). \left(\sigma^{\prime}_{0}\circ\cdots\circ\sigma^{\prime}_{n-1}\right)(\omega)=\left(\sigma^{\prime}_{0}\circ\cdots\circ\sigma^{\prime}_{n-1}\right)((\omega)_{0})\left(\sigma_{0}\circ\cdots\circ\sigma_{n-1}\right)(\nu). |  |

As ω n ′ \omega^{\prime}_{n} always has length larger than one, our previous reasoning now guarantees that the length of Ω n ′ \Omega^{\prime}_{n} diverges, establishing ( 9) and completing the proof.

Before moving on to the study of the growth rates of discrepancy sums, we present a few observations about this process.

###### Proposition 4.3.

Those θ \theta for which x ⁡ ( θ) = 0 ( = 0 +) x(\theta)=0(=0^{+}) are exactly the set

(19) |  | H = { θ: a 2 ​ i − 1 ( θ) = 0 mod 2, i = 1, 2, … }. H=\left\{\theta:a_{2i-1}(\theta)=0\bmod 2,\,i=1,2,\ldots\right\}. |  |

###### Proof.

We leave the reader to verify that H H is exactly the set of θ \theta for which g n ​ ( θ) < 1 / 2 g^{n}(\theta)<1/2 for every n n. For those θ ∈ H \theta\in H, then, we always have I n + 1 ′ = [0 +, δ n −] I^{\prime}_{n+1}=[0^{+},\delta_{n}^{-}], where δ n < 1 \delta_{n}<1, and we never need apply the isomorphism φ n ​ ( x) = 1 − x \varphi_{n}(x)=1-x. That is,

 | 0 ∈ ( φ 0 − 1 ∘ ⋯ ∘ φ n − 1 − 1) ( I n) 0\in\left(\varphi_{0}^{-1}\circ\cdots\circ\varphi_{n-1}^{-1}\right)(I_{n}) |  |

for all n n: 0 = x ⁡ ( θ) 0=x(\theta).

On the other hand, if n n is the first index such that θ n > 1 / 2 \theta_{n}>1/2, we must have φ n ​ ( x) = 1 − x \varphi_{n}(x)=1-x. As θ n + 1 < 1 / 2 \theta_{n+1}<1/2, however, it follows that within I n I_{n}, we have

 | φ n − 1 ∘ φ n + 1 − 1 ​ ( I n + 2) = [( 1 − δ n + 1) +, 1 −], \varphi_{n}^{-1}\circ\varphi_{n+1}^{-1}(I_{n+2})=[(1-\delta_{n+1})^{+},1^{-}], |  |

from which it follows that

 | 0 ∉ ( φ 0 − 1 ∘ ⋯ ∘ φ n + 1 − 1) ( I n + 2). ∎ 0\notin\left(\varphi_{0}^{-1}\circ\cdots\circ\varphi_{n+1}^{-1}\right)(I_{n+2}).\qed |  |

###### Proposition 4.4.

The sequence of substitutions σ n \sigma_{n} is eventually periodic if and only if θ \theta is a quadratic surd.

###### Proof.

Clearly the sequence σ n \sigma_{n} is eventually periodic if and only if the orbit of θ \theta under g g is eventually periodic. From the definition ( 10) of g g we have for all i ≥ 2 i\geq 2

(20) |  | a i ​ ( θ n + 1) = a i + k ​ ( θ n): k = { 0 ( a 1 ( θ n) = 1 mod 2, ≠ 1) 1 ( a 1 ​ ( θ n) = 1) 2 ( a 1 ​ ( θ n) = 0 mod 2) a_{i}(\theta_{n+1})=a_{i+k}(\theta_{n}):\quad k=\begin{cases}0&(a_{1}(\theta_{n})=1\bmod 2,\,\neq 1)\\ 1&(a_{1}(\theta_{n})=1)\\ 2&\left(a_{1}(\theta_{n})=0\bmod 2\right)\end{cases} |  |

So, if a i ​ ( θ) a_{i}(\theta) are eventually periodic (Gauss’ criteria for quadratic surds), we must have infinitely many n n such that for all i ≥ 2 i\geq 2 we have for any j, k j,k

 | a i ​ ( θ n k) = a i ​ ( θ n j). a_{i}(\theta_{n_{k}})=a_{i}(\theta_{n_{j}}). |  |

Suppose that a period of a i ​ ( θ) a_{i}(\theta) is given by the terms α 1, …, α N \alpha_{1},\ldots,\alpha_{N}, and assume without loss of generality that for i ≥ 2 i\geq 2

 | a i ​ ( θ n k) = α i mod N. a_{i}(\theta_{n_{k}})=\alpha_{i\bmod N}. |  |

Then a 1 ​ ( θ n k) a_{1}(\theta_{n_{k}}) is either 1 1, α 1 \alpha_{1}, or α 1 + 1 \alpha_{1}+1. Since the collection n k n_{k} was infinite, one value must be taken twice, giving a period in the orbit g ⁡ ( θ) g(\theta).

On the other hand, assume that θ j = θ j + n ​ k \theta_{j}=\theta_{j+nk} for n = 0, 1, … n=0,1,\ldots and k ≠ 0 k\neq 0. From ( 20) it follows that a i ​ ( θ) a_{i}(\theta) is eventually periodic. ∎

###### Remark.

The periods under g g and γ \gamma need not be the same, nor is one necessarily longer than the other. For example, the golden mean has period one under γ \gamma but period two under g g, while θ = [2, 1, 2, 1, …] \theta=[2,1,2,1,\ldots] has period two under γ \gamma and period one under g g. Furthermore, the sequence σ n \sigma_{n} is purely periodic if and only if θ n = θ 0 \theta_{n}=\theta_{0} for some n ≠ 0 n\neq 0, which is not the same as the partial quotients of θ \theta being purely periodic. Consider for example θ = [3, 2, 2, 2, …] \theta=[3,2,2,2,\ldots], whose partial quotients are clearly not purely periodic, but satisfies θ 2 = θ 0 \theta_{2}=\theta_{0}.

## 5. The Arithmetic of Our Substitutions

Let θ 0 < 1 / 2 \theta_{0}<1/2, so that

 | f ⁡ ( x) = { + 1 ( x ∈ A) − 1 ( x ∈ B ∪ C). f(x)=\begin{cases}+1&(x\in A)\\ -1&(x\in B\cup C).\end{cases} |  |

For θ 0 > 1 / 2 \theta_{0}>1/2 we could repeat all future arguments with a sign change. Given ω ∈ 𝒜 n \omega\in\mathcal{A}^{n}, define (consistent with existing notation)

 | S ⁡ ( ω) \displaystyle S(\omega) | = ∑ i = 0 n − 1 ( χ A − χ B ∪ C) ​ ω i, \displaystyle=\sum_{i=0}^{n-1}\left(\chi_{A}-\chi_{B\cup C}\right)\omega_{i}, |  |

 | M ⁡ ( ω) \displaystyle M(\omega) | = max { S ( ω 0 … ω j − 1): j = 1, 2, …, n }, \displaystyle=\max\left\{S(\omega_{0}\ldots\omega_{j-1}):j=1,2,\ldots,n\right\}, |  |

 | m ⁡ ( ω) \displaystyle m(\omega) | = min { S ( ω 0 … ω j − 1): j = 1, 2, …, n }. \displaystyle=\min\left\{S(\omega_{0}\ldots\omega_{j-1}):j=1,2,\ldots,n\right\}. |  |

Note that we do not include the empty word in determining M ⁡ ( ω) M(\omega), m ⁡ ( ω) m(\omega).

###### Proposition 5.1.

Suppose | ω | = n ≠ 0 |\omega|=n\neq 0, ω ≠ C \omega\neq C, M ⁡ ( ω) ≥ 0 M(\omega)\geq 0, ω \omega does not have C ​ C CC, C ​ B CB or B ​ A BA as factors, and σ \sigma is a substitution given by Table 2, depending on θ \theta. If a 1 ​ ( θ) = 0 mod 2 a_{1}(\theta)=0\bmod 2 and a 3 ​ ( θ) ≠ 1 a_{3}(\theta)\neq 1, or if a 1 ​ ( θ) = 1 a_{1}(\theta)=1, then:

 | S ⁡ ( σ ⁡ ( ω)) = S ⁡ ( ω), M ⁡ ( σ ⁡ ( ω)) = M ⁡ ( ω) + E ⁡ ( a 1), m ⁡ ( σ ⁡ ( ω)) = m ⁡ ( ω). S(\sigma(\omega))=S(\omega),\quad M(\sigma(\omega))=M(\omega)+E(a_{1}),\quad m(\sigma(\omega))=m(\omega). |  |

On the other hand, if a 1 ​ ( θ) = 0 mod 2 a_{1}(\theta)=0\bmod 2 and a 3 ​ ( θ) = 1 a_{3}(\theta)=1, then

 | S ⁡ ( σ ⁡ ( ω)) = − S ⁡ ( ω), M ⁡ ( σ ⁡ ( ω)) = − m ⁡ ( ω) + E ⁡ ( a 1), m ⁡ ( σ ⁡ ( ω)) = − M ⁡ ( ω). S(\sigma(\omega))=-S(\omega),\quad M(\sigma(\omega))=-m(\omega)+E(a_{1}),\quad m(\sigma(\omega))=-M(\omega). |  |

Finally, if a 1 ​ ( θ) = 1 mod 2 a_{1}(\theta)=1\bmod 2, ≠ 1 \neq 1, and either

- •

( ω) n − 1 ≠ C (\omega)_{n-1}\neq C, or

- •

( ω) n − 1 = C (\omega)_{n-1}=C, but there is some j ≠ n j\neq n such that S ⁡ ( ( ω) 0 ​ ( ω) 1 ​ … ​ ( ω) j − 1) = m ⁡ ( ω) S((\omega)_{0}(\omega)_{1}\ldots(\omega)_{j-1})=m(\omega),

then also

 | S ⁡ ( σ ⁡ ( ω)) = − S ⁡ ( ω), M ⁡ ( σ ⁡ ( ω)) = − m ⁡ ( ω) + E ⁡ ( a 1), m ⁡ ( σ ⁡ ( ω)) = − M ⁡ ( ω). S(\sigma(\omega))=-S(\omega),\quad M(\sigma(\omega))=-m(\omega)+E(a_{1}),\quad m(\sigma(\omega))=-M(\omega). |  |

If a 1 ​ ( θ) = 1 mod 2 a_{1}(\theta)=1\bmod 2, ( ω) n − 1 = C (\omega)_{n-1}=C and S ⁡ ( ( ω) 0 ​ … ​ ( ω) j − 1) > m ⁡ ( ω) S((\omega)_{0}\ldots(\omega)_{j-1})>m(\omega) for all j ≠ n j\neq n, then

 | S ⁡ ( σ ⁡ ( ω)) = − S ⁡ ( ω), M ⁡ ( σ ⁡ ( ω)) = − m ⁡ ( ω) − 1 + E ⁡ ( a 1), m ⁡ ( σ ⁡ ( ω)) = − M ⁡ ( ω). S(\sigma(\omega))=-S(\omega),\quad M(\sigma(\omega))=-m(\omega)-1+E(a_{1}),\quad m(\sigma(\omega))=-M(\omega). |  |

###### Proof.

The prohibition on C ​ B CB, C ​ C CC and B ​ A BA being factors of ω \omega are necessary for ω \omega to encode the orbit of any point under rotation by any θ \theta, so this condition is not prohibitive in our setting.

In all cases, the statements regarding the value S ⁡ ( σ ⁡ ( ω)) S(\sigma(\omega)) follow from examining S ⁡ ( σ ⁡ ( x)) S(\sigma(x)) for each x ∈ 𝒜 x\in\mathcal{A}; the reader may consult Table 2 to verify that S ⁡ ( σ ⁡ ( x)) = ± S ⁡ ( x) S(\sigma(x))=\pm S(x) as described, and the statement then follows from the fact that σ \sigma is a homomorphism. We will turn our attention, then, to the statements regarding m ⁡ ( σ ⁡ ( ω)) m(\sigma(\omega)) and M ⁡ ( σ ⁡ ( ω)) M(\sigma(\omega)). All cases but the last are considered similarly with the possible sign-change outlined above in mind.

For example, suppose that a 1 = 0 mod 2 a_{1}=0\bmod 2 and a 3 ≠ 1 a_{3}\neq 1. Let ω = υ ​ ψ \omega=\upsilon\psi, where υ \upsilon is the largest left factor of ω \omega such that S ⁡ ( υ) = M ⁡ ( ω) − 1 S(\upsilon)=M(\omega)-1: note that as M ⁡ ( ω) ≥ 0 M(\omega)\geq 0 and the empty word was not considered in computation of M ⁡ ( ω) M(\omega), we have ( ψ) 0 = A (\psi)_{0}=A. As S ⁡ ( σ ⁡ ( υ)) = S ⁡ ( υ) = M ⁡ ( ω) − 1 S(\sigma(\upsilon))=S(\upsilon)=M(\omega)-1 and M ⁡ ( σ ⁡ ( A)) = E ⁡ ( a 1) + 1 M(\sigma(A))=E(a_{1})+1, we know that

 | M ⁡ ( σ ⁡ ( ω)) ≥ M ⁡ ( σ ⁡ ( υ) ​ ψ) = M ⁡ ( ω) + E ⁡ ( a 1). M(\sigma(\omega))\geq M(\sigma(\upsilon)\psi)=M(\omega)+E(a_{1}). |  |

Assume on the other hand that

 | σ ⁡ ( ω) = σ ⁡ ( υ) ​ ν ​ ψ, S ⁡ ( σ ⁡ ( υ) ​ ν) > M ⁡ ( ω) + E ⁡ ( a 1), \sigma(\omega)=\sigma(\upsilon)\nu\psi,\quad S(\sigma(\upsilon)\nu)>M(\omega)+E(a_{1}), |  |

and υ \upsilon is of maximal length to allow such a decomposition. Note that ν ≠ ∅ \nu\neq\emptyset as S ⁡ ( σ ⁡ ( υ)) = S ⁡ ( υ) ≤ M ⁡ ( ω) S(\sigma(\upsilon))=S(\upsilon)\leq M(\omega). As υ \upsilon is a proper factor, it is followed by a letter, and by maximality on the length of υ \upsilon, ν \nu is a proper left factor of either σ ⁡ ( A) \sigma(A), σ ⁡ ( B) \sigma(B), or σ ⁡ ( C) \sigma(C), and E ⁡ ( a 1) ≠ 0 E(a_{1})\neq 0. If υ \upsilon is followed by A A in ω \omega,

 | S ⁡ ( σ ⁡ ( υ)) = S ⁡ ( υ) ≤ M − 1. S(\sigma(\upsilon))=S(\upsilon)\leq M-1. |  |

On the other hand, S ⁡ ( ν) ≤ E ⁡ ( a 1) + 1 = M ⁡ ( σ ⁡ ( A)) S(\nu)\leq E(a_{1})+1=M(\sigma(A)), contradicting the value S ⁡ ( σ ⁡ ( υ) ​ ν) S(\sigma(\upsilon)\nu). The possibility of υ \upsilon followed by B B or C C are similarly considered; the larger possible S ⁡ ( σ ⁡ ( υ)) = M ⁡ ( ω) S(\sigma(\upsilon))=M(\omega) is countered by S ⁡ ( ν) ≤ E ⁡ ( a 1) S(\nu)\leq E(a_{1}) in these cases.

The ambiguity in the situation when a 1 ​ ( θ) = 1 mod 2 a_{1}(\theta)=1\bmod 2, ≠ 1 \neq 1 is due to the substitution σ ⁡ ( A) = C \sigma(A)=C, which does not achieve an intermediate sum of E ⁡ ( a 1) E(a_{1}) (as does σ ⁡ ( B) \sigma(B)). On the assumption that there is some proper left factor ψ \psi of ω \omega such that S ⁡ ( ψ) = m ⁡ ( ω) S(\psi)=m(\omega), however, we know that the letter which follows ψ \psi must be A A; similar computations to the above then apply. If the only left factor of ω \omega which achieves a sum of m ⁡ ( ω) m(\omega) is in fact ω \omega itself, then if the final letter of ω \omega is B B we again have no problem.

Assume, then, that S ⁡ ( ω) = m ⁡ ( ω) S(\omega)=m(\omega), there is no proper left factor with this sum, and ω \omega ends with the letter C C. As M ⁡ ( ω) ≥ 0 M(\omega)\geq 0 by assumption, there is a letter preceding this terminal C C (that is, ω ≠ C \omega\neq C). If this letter is A A, then the left factor ψ \psi such that ω = ψ ​ A ​ C \omega=\psi AC has the minimal sum as its sum (even if it is empty), and the preceding reasoning applies. Therefore ω \omega must be of the form ψ ​ B ​ C \psi BC (recall that C ​ C CC is not a factor): considering σ ⁡ ( B) \sigma(B) following S ⁡ ( σ ⁡ ( ψ)) = − m ⁡ ( ω) − 2 S(\sigma(\psi))=-m(\omega)-2 completes the proposition. ∎

For convenience, denote

(21) |  | σ ( n) \displaystyle\sigma^{(n)} | = σ 0 ∘ σ 1 ∘ ⋯ ∘ σ n − 1, \displaystyle=\sigma_{0}\circ\sigma_{1}\circ\cdots\circ\sigma_{n-1}, |  |  |

(22) |  | σ ′ ( n) \displaystyle\sigma^{\prime(n)} | = σ ′ 0 ∘ σ ′ 1 ∘ ⋯ ∘ σ ′ n − 1. \displaystyle=\sigma^{\prime}_{0}\circ\sigma^{\prime}_{1}\circ\cdots\circ\sigma^{\prime}_{n-1}. |  |  |

Recall ( 17) and define for n ≥ 1 n\geq 1

(23) |  | Ω n = σ ( n) ​ ( A), Ω n ′ = σ ′ ( n) ​ ( ω ′ ​ ( n)). \Omega_{n}=\sigma^{(n)}(A),\quad\Omega^{\prime}_{n}=\sigma^{\prime(n)}(\omega^{\prime}(n)). |  |

Define p n p_{n} to track the parity of how many θ i > 1 / 2 \theta_{i}>1/2:

(24) |  | p n = ( ∑ i = 1 n − 1 χ ( 1 / 2, 1) ​ ( θ i)) mod 2. p_{n}=\left(\sum_{i=1}^{n-1}\chi_{(1/2,1)}(\theta_{i})\right)\bmod 2. |  |

We now have all the tools necessary to precisely study the sequences M n ​ ( y) M_{n}(y) and m n ​ ( y) m_{n}(y) for y ∈ { x ⁡ ( θ), 0 } y\in\{x(\theta),0\}:

###### Proposition 5.2.

Assume that θ 0 < 1 / 2 \theta_{0}<1/2. Then

 | S ⁡ ( Ω n) = ( − 1) p n, S ⁡ ( Ω n ′) = 1 S(\Omega_{n})=(-1)^{p_{n}},\quad S(\Omega^{\prime}_{n})=1 |  |

 | | M ⁡ ( Ω n) − ( 1 + ∑ i ≤ n − 1 p i = 0 E ⁡ ( a 1 ​ ( θ i))) | ≤ 1, M ⁡ ( Ω n ′) = 1 + ∑ i ≤ n p i = 0 E ⁡ ( a 1 ​ ( θ i)), \displaystyle\left|M(\Omega_{n})-\left(1+\sum_{\begin{subarray}{c}i\leq n-1\\ p_{i}=0\end{subarray}}E(a_{1}(\theta_{i}))\right)\right|\leq 1,\quad M(\Omega^{\prime}_{n})=1+\sum_{\begin{subarray}{c}i\leq n\\ p_{i}=0\end{subarray}}E(a_{1}(\theta_{i})), |  |

 | | m ⁡ ( Ω n) − ( 1 − ∑ i ≤ n − 1 p i = 1 E ⁡ ( a 1 ​ ( θ i))) | ≤ 1, m ⁡ ( Ω n ′) = 1 − ∑ i ≤ n p i = 1 E ⁡ ( a 1 ​ ( θ i)). \displaystyle\left|m(\Omega_{n})-\left(1-\sum_{\begin{subarray}{c}i\leq n-1\\ p_{i}=1\end{subarray}}E(a_{1}(\theta_{i}))\right)\right|\leq 1,\quad m(\Omega^{\prime}_{n})=1-\sum_{\begin{subarray}{c}i\leq n\\ p_{i}=1\end{subarray}}E(a_{1}(\theta_{i})). |  |

###### Proof.

The word Ω n \Omega_{n} in ( 23) is formed by successive substitutions acting on the word A A; as such, it will always begin with A A, so M ⁡ ( Ω n) ≥ 1 M(\Omega_{n})\geq 1. We immediately see that all S ⁡ ( Ω n) = ± 1 S(\Omega_{n})=\pm 1 according to the parity of p n p_{n} by applying Proposition 5.1 in succession. The ambiguous case in Proposition 5.1 arose when ω \omega was a word which had a nonnegative maximal sum (as do all Ω n \Omega_{n}) and whose minimum sum is only achieved as its total sum, with C C as a terminal factor. Furthermore, we would need θ n \theta_{n} to have first partial quotient odd and larger than one. For this to happen with the restriction that all S ⁡ ( Ω n) = ± 1 S(\Omega_{n})=\pm 1 requires that S ⁡ ( Ω n) = − 1 S(\Omega_{n})=-1 (otherwise the minimal sum is achieved by the proper left factor A A), and therefore S ⁡ ( Ω n − 1) = 1 S(\Omega_{n-1})=1. This scenario also require that M ⁡ ( Ω n − 1) = 1 M(\Omega_{n-1})=1 (otherwise m ⁡ ( Ω n) < − 1 ≤ S ⁡ ( Ω n) m(\Omega_{n})<-1\leq S(\Omega_{n})); so this situation can only occur in our scenario when Ω n − 1 = A \Omega_{n-1}=A: this possible error of one may only appear once in the sequence of arithmetic computations from repeated application of Proposition 5.1.

We leave to the reader the verification that the parity of p n p_{n} exactly dictates whether substitutions will add to the maximal values or subtract from the minimal values; refer to Proposition 5.1 again.

Let us now consider Ω n ′ \Omega^{\prime}_{n}. Note that σ j ′ = Ψ \sigma_{j}^{\prime}=\Psi exactly when θ j > 1 / 2 \theta_{j}>1/2, exactly when σ j − 1 \sigma_{j-1} has the property that S ⁡ ( σ j − 1 ​ ( ω)) = − S ⁡ ( ω) S(\sigma_{j-1}(\omega))=-S(\omega). Clearly we have S ⁡ ( Ψ ⁡ ( ω)) = S ⁡ ( ω) − 2 S(\Psi(\omega))=S(\omega)-2 provided ω \omega begins with A A. Also note that if S ⁡ ( ω) = 1 S(\omega)=1, then if m ⁡ ( ω) = 1 m(\omega)=1 we must have ω 0 = A \omega_{0}=A: it is never possible in our construction for ω \omega to terminate with C C, S ⁡ ( ω) = 1 S(\omega)=1, and m ⁡ ( Ψ ⁡ ( ω)) = S ⁡ ( Ψ ⁡ ( ω)) m(\Psi(\omega))=S(\Psi(\omega)) is the only time this value is reached.

Our choice of ω ′ ​ ( n) \omega^{\prime}(n) always begins with A A and has S ​ ( ω ′ ​ ( n)) = 1 S(\omega^{\prime}(n))=1, and for those σ n \sigma_{n} such that S ​ ( σ n ​ ( A)) = − 1 S(\sigma_{n}(A))=-1, the reader may verify that

 | S ⁡ ( σ n ​ ( Ψ ⁡ ( ω))) = 2 − S ⁡ ( ω) S\left(\sigma_{n}(\Psi(\omega))\right)=2-S(\omega) |  |

by applying Proposition 5.1. While this change will change the sum of + 1 +1 to − 1 -1, it is immediately followed by a substitution which reverses the sign of the sum: we maintain

 | S ⁡ ( Ω n ′) = 1. S(\Omega^{\prime}_{n})=1. |  |

Furthermore, as m ⁡ ( ω n ′) = 1 m(\omega^{\prime}_{n})=1 for all ω n ′ \omega^{\prime}_{n}, if we do apply Ψ \Psi (so m ⁡ ( Ψ ​ ω) = − 1 m(\Psi\omega)=-1) followed by one of these sign-reversing substitutions σ \sigma, we see

 | M ⁡ ( σ ⁡ ( Ψ ​ ω)) ≥ − m ⁡ ( Ψ ​ ω) + E ⁡ ( a 1) − 1 ≥ 1 + E ⁡ ( a 1) − 1 ≥ 0, M(\sigma(\Psi\omega))\geq-m(\Psi\omega)+E(a_{1})-1\geq 1+E(a_{1})-1\geq 0, |  |

so we may always apply Proposition 5.1 without worrying about the possible error of one. ∎

###### Corollary 5.3 ( [2], Theorem 1, case k = 2 k=2).

We have S n ​ ( θ) ≥ 0 S_{n}(\theta)\geq 0 for all n ≥ 0 n\geq 0 if and only if x ⁡ ( θ) = 0 x(\theta)=0.

###### Proof.

By viewing the ergodic sums as an additive cocycle, for all n > 0 n>0 we have S n ​ ( θ) = S n + 1 ​ ( 0) − 1 S_{n}(\theta)=S_{n+1}(0)-1, so we have by Proposition 5.2:

 | S | Ω n ′ | − 1 ( θ) = 0, M | Ω n ′ | − 1 ( θ) = ∑ i ≤ n p i = 0 E ( a 1 ( θ i)), m | Ω n ′ | − 1 ( θ) = − ∑ i ≤ n p i = 1 E ( a 1 ( θ i)). S_{|\Omega^{\prime}_{n}|-1}(\theta)=0,\quad M_{|\Omega^{\prime}_{n}|-1}(\theta)=\sum_{\begin{subarray}{c}i\leq n\\ p_{i}=0\end{subarray}}E(a_{1}(\theta_{i})),\quad m_{|\Omega^{\prime}_{n}|-1}(\theta)=-\sum_{\begin{subarray}{c}i\leq n\\ p_{i}=1\end{subarray}}E(a_{1}(\theta_{i})). |  |

So S n ​ ( θ) ≥ 0 S_{n}(\theta)\geq 0 for all n n if and only if p i = 0 mod 2 p_{i}=0\bmod 2 for all i i such that θ i < 1 / 2 \theta_{i}<1/2, which is equivalent to p i = 0 mod 2 p_{i}=0\bmod 2 for all i i. A direct inductive argument shows that p i = 0 p_{i}=0 for all i i if and only if a 2 ​ i − 1 ​ ( θ) = 0 mod 2 a_{2i-1}(\theta)=0\bmod 2 by considering the action of g g ( 10), which corresponds by Proposition 4.3 to x ⁡ ( θ) = 0 x(\theta)=0. ∎

###### Remark.

Using that σ \sigma are all homomorphisms, a more constructive version of ( 7) is

 | ω 0 σ ( 1) ( ω 1) σ ( 2) ( ω 2) ⋯ σ ( n) ( ω n) ⋯, \omega_{0}\sigma^{(1)}(\omega_{1})\sigma^{(2)}(\omega_{2})\cdots\sigma^{(n)}(\omega_{n})\cdots, |  |

which allows a more direct way of computing the word through successive computation of the words ω n \omega_{n} (given the starting point x x).

###### Lemma 5.4.

We always have

 | | σ ( n) ​ ( A) | = | σ ( n) ​ ( B) |, \left|\sigma^{(n)}(A)\right|=\left|\sigma^{(n)}(B)\right|, |  |

and if we define the matrices M i = M ⁡ ( θ i) M_{i}=M(\theta_{i}) according to Table 3, then

 | M n − 1 M n − 2 ⋯ M 1 M 0 [1 1] = [| σ ( n) ​ ( A) | | σ ( n) ​ ( C) |]. M_{n-1}M_{n-2}\cdots M_{1}M_{0}\left[\begin{array}[]{c}1\\ 1\end{array}\right]=\left[\begin{array}[]{c}|\sigma^{(n)}(A)|\\ |\sigma^{(n)}(C)|\end{array}\right]. |  |

###### Proof.

The first claim follows directly from the following observation: for all substitutions σ \sigma, the words σ ⁡ ( A) \sigma(A) and σ ⁡ ( B) \sigma(B) are always of the same length and always contain the same number of letters drawn from { A, B } \{A,B\}. That is, within

 | ( φ n − 1 − 1 ∘ ⋯ ∘ φ 0 − 1) ( A ∪ B) ⊂ I ~ n \left(\varphi_{n-1}^{-1}\circ\cdots\circ\varphi_{0}^{-1}\right)(A\cup B)\subset\tilde{I}_{n} |  |

the return time under R θ 0 R_{\theta_{0}} to I ~ n \tilde{I}_{n} is constant, and similarly on the pullback of C C. One need only count the number of C C and { A, B } \{A,B\} within σ n ​ ( C) \sigma_{n}(C) and σ n ​ ( { A, B }) \sigma_{n}(\{A,B\}) to construct the relevant matrices. ∎

Case | M ⁡ ( θ) M(\theta) |

a 1 ​ ( θ) = 0 mod 2 a_{1}(\theta)=0\bmod 2, a 3 ​ ( θ) ≠ 1 a_{3}(\theta)\neq 1 | [( a 1 − 1) ​ a 2 + 1 a 2 ( a 1 − 1) ​ a 2 + a 1 a 2 + 1] \left[\begin{array}[]{c c}(a_{1}-1)a_{2}+1&a_{2}\\ (a_{1}-1)a_{2}+a_{1}&a_{2}+1\end{array}\right] |

a 1 ​ ( θ) = 0 mod 2 a_{1}(\theta)=0\bmod 2, a 3 ​ ( θ) = 1 a_{3}(\theta)=1 | [( a 1 − 1) ​ a 2 + a 1 a 2 + 1 ( a 1 − 1) ​ a 2 + 1 a 2] \left[\begin{array}[]{c c}(a_{1}-1)a_{2}+a_{1}&a_{2}+1\\ (a_{1}-1)a_{2}+1&a_{2}\end{array}\right] |

a 1 ​ ( θ) = 1 mod 2 a_{1}(\theta)=1\bmod 2, ≠ 1 \neq 1 | [a 1 − 1 1 1 0] \left[\begin{array}[]{c c}a_{1}-1&1\\ 1&0\end{array}\right] |

a 1 ​ ( θ) = 1 a_{1}(\theta)=1 | [1 0 0 1] \left[\begin{array}[]{c c}1&0\\ 0&1\end{array}\right] |

Table 3. The matrices M ⁡ ( θ) M(\theta) used to determine return times in the induced systems.

###### Lemma 5.5.

 | | Ω n | ≤ | Ω n ′ | ≤ | Ω n + 1 |. |\Omega_{n}|\leq|\Omega^{\prime}_{n}|\leq|\Omega_{n+1}|. |  |

###### Proof.

The lower inequality is direct in light of ( 18), recalling that ( ω n ′) 1 = A (\omega^{\prime}_{n})_{1}=A. The upper bound follows from Lemma 5.4, noting that while ω n ′ \omega^{\prime}_{n} may or may not be a left factor of σ n ​ ( A) \sigma_{n}(A), it does contain the same number of { A, B } \{A,B\} versus C C as a proper left factor of σ n ​ ( A) \sigma_{n}(A). Furthermore, the only substitutions for which | σ ⁡ ( C) | > | σ ⁡ ( A) | |\sigma(C)|>|\sigma(A)| are those corresponding to a 1 = 0 mod 2 a_{1}=0\bmod 2, a 3 ≠ 0 a_{3}\neq 0; such substitutions are not followed by Ψ \Psi. That is,

 | | σ ′ ( n) ​ ( A) | ≤ | Ω n |, \left|\sigma^{\prime(n)}(A)\right|\leq|\Omega_{n}|, |  |

completing the proof of the upper bound. ∎

###### Example 5.6.

Let θ = 2 mod 1 = [2, 2, 2, …] \theta=\sqrt{2}\mod 1=[2,2,2,\ldots]. Then as θ \theta is a quadratic irrational, the sequence of substitutions σ i \sigma_{i} is eventually periodic by Proposition 4.4. As g ⁡ ( θ) = θ g(\theta)=\theta, the sequence of substitutions is periodic with period one, given by

 | σ: { A → A ​ A ​ C ​ A ​ C B → A ​ B ​ C ​ A ​ C C → A ​ B ​ C ​ A ​ C ​ A ​ C \sigma:\left\{\begin{array}[]{l}A\rightarrow AACAC\\ B\rightarrow ABCAC\\ C\rightarrow ABCACAC\end{array}\right. |  |

The point x ⁡ ( θ) = 0 x(\theta)=0 by Proposition 4.3, so applying Theorem 1.1, the orbit of zero is given by the sequence

 | lim n → ∞ σ n ​ ( A) = A ​ A ​ C ​ A ​ C ​ A ​ A ​ C ​ A ​ C ​ A ​ B ​ C ​ A ​ C ​ A ​ C ​ A ​ A ​ C ​ A ​ C ​ A ​ B ​ C ​ A ​ C ​ A ​ C ​ … \lim_{n\rightarrow\infty}\sigma^{n}(A)=AACACAACACABCACACAACACABCACAC\ldots |  |

The self-similar structure of the sequence of ergodic sums S n ​ ( 0) S_{n}(0) is not exact (as σ ⁡ ( B) ≠ σ ⁡ ( C) \sigma(B)\neq\sigma(C)), but nonetheless highly regular. This regularity was noticed by D. Hensley in [4, Figure 3.4]. We give several plots of S n ​ ( 0) S_{n}(0) for different values of n n in Figure 2. This same self-similarity for developing the orbit of x ⁡ ( θ) x(\theta) will be seen for any quadratic irrational θ \theta in light of Proposition 4.4.

[image: Refer to caption] (a) N = 5 N=5, σ ⁡ ( A) = A ​ A ​ C ​ A ​ C \sigma(A)=AACAC

[image: Refer to caption] (b) N = 29 N=29, σ 2 ​ ( A) \sigma^{2}(A)

[image: Refer to caption] (c) N = 169 N=169, σ 3 ​ ( A) \sigma^{3}(A)

[image: Refer to caption] (d) N = 33461 N=33461, σ 6 ​ ( A) \sigma^{6}(A)

Figure 2. Plots of S i ​ ( 0) S_{i}(0) for different ranges of 0 ≤ i ≤ N 0\leq i\leq N, where θ = 2 − 1 \theta=\sqrt{2}-1.

For quadratic irrational θ ∉ H \theta\notin H, computation of the point x ⁡ ( θ) x(\theta) is not too difficult:

###### Example 5.7.

Let θ = [1, 1, …] \theta=[1,1,\ldots] be the golden mean. Recall that S 1 S^{1} will be partitioned such that A = [( 1 / 2) +, 1 −] A=[(1/2)^{+},1^{-}] as θ > 1 / 2 \theta>1/2. As g 2 ​ ( θ) = θ g^{2}(\theta)=\theta, and a 1 = 1 a_{1}=1 corresponds to the identity substitution, the only non-identity substitution generated is

 | σ: { A → A ​ B ​ C ​ A ​ C B → A ​ A ​ C ​ A ​ C C → A ​ A ​ C \sigma:\left\{\begin{array}[]{l}A\rightarrow ABCAC\\ B\rightarrow AACAC\\ C\rightarrow AAC\end{array}\right. |  |

So, the orbit of x ⁡ ( θ) x(\theta) is given by

 | lim n → ∞ σ n ​ ( A) = A ​ B ​ C ​ A ​ C ​ A ​ A ​ C ​ A ​ C ​ A ​ A ​ C ​ A ​ B ​ C ​ A ​ C ​ A ​ A ​ C ​ …, \lim_{n\rightarrow\infty}\sigma^{n}(A)=ABCACAACACAACABCACAAC\ldots, |  |

while the orbit of 0 0 is given by

 | Ψ ⁡ ( σ ⁡ ( … ​ Ψ ​ ( A ​ A ​ C))) = C ​ A ​ C ​ A ​ B ​ C ​ A ​ C ​ A ​ A ​ C ​ A ​ B ​ C ​ A ​ C ​ A ​ A ​ C ​ A ​ C ​ …. \Psi(\sigma(\ldots\Psi(AAC)))=CACABCACAACABCACAACAC\ldots. |  |

To compute the point x ⁡ ( θ) x(\theta), we need to determine the intervals I n ~ \tilde{I_{n}}. For those θ n = [2, 1, 1, …] \theta_{n}=[2,1,1,\ldots] we have

 | δ n = 1 − 2 ​ θ n = 1 − 2 ​ ( 1 − θ) = 2 ​ θ − 1. \delta_{n}=1-2\theta_{n}=1-2(1-\theta)=2\theta-1. |  |

Denote this quantity by δ \delta for convenience. For this particular θ \theta we do not ever have two consecutive θ n < 1 / 2 \theta_{n}<1/2, so the intervals I n + 1 ′ ⊂ I n I^{\prime}_{n+1}\subset I_{n} strictly alternate between [0 +, δ −] [0^{+},\delta^{-}] and [( 1 − δ) +, 1 −] [(1-\delta)^{+},1^{-}] (for those n = 0 mod 2 n=0\bmod 2; for odd n n we have θ n > 1 / 2 \theta_{n}>1/2 and I n + 1 ′ = I n I^{\prime}_{n+1}=I_{n}). So the sequence of preimages I ~ n \tilde{I}_{n} (recall again ( 14)) is given by

 | [0 +, 1 −], [( 1 − δ) +, 1 −], [( 1 − δ) +, ( 1 − δ + δ 2) −], … \left[0^{+},1^{-}\right],\quad\left[(1-\delta)^{+},1^{-}\right],\quad\left[(1-\delta)^{+},(1-\delta+\delta^{2})^{-}\right],\ldots |  |

whose intersection is given by the geometric series

 | x ⁡ ( θ) = ∑ i = 0 ∞ ( − 1) i ​ δ i = 1 1 + ( 2 ​ θ − 1) = 1 2 ​ θ. x(\theta)=\sum_{i=0}^{\infty}(-1)^{i}\delta^{i}=\frac{1}{1+(2\theta-1)}=\frac{1}{2\theta}. |  |

See Figure 3 for both of these orbits.

[image: Refer to caption] (a) x = 0 x=0, with orbit C ​ A ​ C ​ A ​ B ​ C ​ A ​ C ​ A ​ A ​ C ​ … CACABCACAAC\ldots

[image: Refer to caption] (b) x = x ⁡ ( θ) = 1 / ( 2 ​ θ) x=x(\theta)=1/(2\theta), with orbit A ​ B ​ C ​ A ​ C ​ A ​ A ​ C ​ A ​ C ​ … ABCACAACAC\ldots

Figure 3. Plots of S i ​ ( x) S_{i}(x) for 0 ≤ i ≤ 100 0\leq i\leq 100, where θ \theta is the golden mean for the two given values of x x. Note that as θ > 1 / 2 \theta>1/2, we have A → − 1 A\rightarrow-1, B, C → + 1 B,C\rightarrow+1.

One particularly striking corollary of Proposition 5.2 is the following, which does not seem to be apparent from any other technique:

###### Corollary 5.8.

If θ \theta is a quadratic irrational, then

 | lim n → ∞ M n ​ ( 0) | m n ​ ( 0) | ∈ ℚ ∗, \lim_{n\rightarrow\infty}\frac{M_{n}(0)}{|m_{n}(0)|}\in\mathbb{Q}^{*}, |  |

where ℚ ∗ = ℚ ∪ { ∞ } \mathbb{Q}^{*}=\mathbb{Q}\cup\{\infty\}, and p / 0 = ∞ p/0=\infty for any positive integer p p. If θ n = θ n + k \theta_{n}=\theta_{n+k} is a minimal period under the orbit of g g and p n + k = p n + 1 p_{n+k}=p_{n}+1, then the ratio tends to one. Furthermore, for any nonnegative p / q ∈ ℚ ∗ p/q\in\mathbb{Q}^{*}, there is a quadratic irrational θ \theta such that the above ratio has limit p / q p/q.

###### Proof.

We have already shown that g n ​ ( θ) g^{n}(\theta) is eventually periodic for such θ \theta in Proposition 4.4. It follows from Proposition 5.2 that M n ​ ( 0) M_{n}(0) and m n ​ ( 0) m_{n}(0) see a periodic sequence of adjustments by bounded integer amounts, which must therefore have rational limit. If one period reflects a change in the parity of p p, it will always be followed by the mirrored changes in M n M_{n}, m n m_{n}, producing a limit of one.

To produce quadratic irrationals with the desired limit, if q = 0 q=0 then θ ∈ H \theta\in H will suffice ( m n ​ ( 0) ≡ 1 m_{n}(0)\equiv 1, and M n ​ ( 0) M_{n}(0) must therefore diverge), and for p = 0 p=0 any θ \theta such that a 1 ​ ( θ) = 1 a_{1}(\theta)=1 and g ⁡ ( θ) ∈ H g(\theta)\in H will suffice (here M n ​ ( 0) ≡ 1 M_{n}(0)\equiv 1). For p / q p/q with neither zero, just set

 | θ = [2 ​ p, 1, 1, 2 ​ q − 1, 1, 1, 2 ​ p − 1, 1, 1, 2 ​ q − 1, 1, 1, …], \theta=[2p,1,1,2q-1,1,1,2p-1,1,1,2q-1,1,1,\ldots], |  |

and verify that we will first add p p to M n ​ ( 0) M_{n}(0), then subtract q q from m n ​ ( 0) m_{n}(0), etc. ∎

## 6. Proof of Theorem 1.2

Let c n c_{n} and d n d_{n} be divergent monotone sequences in o ⁡ ( n) o(n) with bounded differences Δ ​ c n \Delta c_{n}, Δ ​ d n \Delta d_{n}; we will construct a dense set of θ \theta such that

 | lim sup n → ∞ M n ​ ( 0) c n = lim sup n → ∞ | m n ​ ( 0) | d n = 1. \limsup_{n\rightarrow\infty}\frac{M_{n}(0)}{c_{n}}=\limsup_{n\rightarrow\infty}\frac{|m_{n}(0)|}{d_{n}}=1. |  |

Any irrational θ \theta is completely determined by its sequence of partial quotients, which is equivalent to its orbit under g g, and its orbit under g g is completely determined by the sequence of values

 | a 1 ​ ( θ i) ( a 1 = 1 mod 2), a 1 ​ ( θ i), a 2 ​ ( θ i) ( a 1 = 0 mod 2). a_{1}(\theta_{i})\quad(a_{1}=1\bmod 2),\qquad a_{1}(\theta_{i}),\,a_{2}(\theta_{i})\quad(a_{1}=0\bmod 2). |  |

Suppose, then, that the first finitely many partial quotients of θ \theta are prescribed, such that the first n n values of θ i \theta_{i} are fixed. Without loss of generality, insert an additional single term if necessary so that p n = 0 p_{n}=0 (recall ( 24)). We are now completely free to choose k k to construct ω n ′ \omega^{\prime}_{n} (refer to ( 17)). If we denote

 | M ⁡ ( Ω n ′) = M, m ⁡ ( Ω n ′) = m, | Ω n ′ | = L n, M(\Omega^{\prime}_{n})=M,\quad m(\Omega^{\prime}_{n})=m,\quad|\Omega^{\prime}_{n}|=L_{n}, |  |

it follows from Proposition 5.2 that once we choose k k, we will have

 | M ⁡ ( Ω n + 1 ′) = M + k, m ⁡ ( Ω n + 1 ′) = m. M(\Omega^{\prime}_{n+1})=M+k,\quad m(\Omega^{\prime}_{n+1})=m. |  |

Denote by L n + 1 ​ ( k) = | Ω n + 1 ′ | L_{n+1}(k)=|\Omega^{\prime}_{n+1}| as a function of k k.

Assume first that M < c L n M<c_{L_{n}}, so we wish to increase the maximal sum compared to the sequence c n c_{n}. Then let a 1 ​ ( θ n) a_{1}(\theta_{n}) be odd, so

 | ω ′ ​ ( n + 1) = A k + 1 ​ B k. \omega^{\prime}(n+1)=A^{k+1}B^{k}. |  |

From ( 18) and the previous observation that | σ ( n) ​ ( A) | = | σ ( n) ​ ( B) | |\sigma^{(n)}(A)|=|\sigma^{(n)}(B)|, it follows that

 | L n + 1 ​ ( k) = | ω ~ | + 2 ​ k ​ | σ ( n + 1) ​ ( A) |, L_{n+1}(k)=|\tilde{\omega}|+2k|\sigma^{(n+1)}(A)|, |  |

where

 | ω ~ = σ ′ ( n + 1) ​ ( A). \tilde{\omega}=\sigma^{\prime(n+1)}(A). |  |

Consider, then, the proper left factors A i A^{i} of ω ′ ​ ( n + 1) \omega^{\prime}(n+1) for i = 1, 2, …, k + 1 i=1,2,\ldots,k+1. Applying Proposition 5.1, the new maximal sum M + k M+k is achieved at a time N N, where

 | | ω ~ ​ | + ( k − 1) | ​ σ ( n) ​ ( A) | ≤ N ≤ | ω ~ ​ | + k | ​ σ ( n) ​ ( A) |. |\tilde{\omega}|+(k-1)|\sigma^{(n)}(A)|\leq N\leq|\tilde{\omega}|+k|\sigma^{(n)}(A)|. |  |

As c n ∈ o ⁡ ( n) c_{n}\in o(n), we may choose k ≥ 1 k\geq 1 to be minimal such that

 | M + k c ⁡ ( | ω ~ ​ | + k | ​ σ ( n) ​ ( A) |) ≥ 1. \frac{M+k}{c(|\tilde{\omega}|+k|\sigma^{(n)}(A)|)}\geq 1. |  |

If, however, we had M ≥ c L n M\geq c_{L_{n}}, then we would wish to not greatly increase M M compared to c n c_{n}. In this case, let θ n = [2, k, 1, …] \theta_{n}=[2,k,1,\ldots], and pass directly to considering the word

 | σ ′ ( n + 1) ​ ( C) = σ ′ ( n) ​ ( A k + 1 ​ B k − 1 ​ C), \sigma^{\prime(n+1)}(C)=\sigma^{\prime(n)}(A^{k+1}B^{k-1}C), |  |

as C C is always a left factor of ω n + 1 ′ = Ψ ⁡ ( ω n + 2 ′) \omega^{\prime}_{n+1}=\Psi(\omega^{\prime}_{n+2}) in this case. Then the maximal sum reached for this word is M + 1 M+1, but its length is (similarly to before)

 | L n + 1 ​ ( k) = | ω ~ | + 2 ​ k ​ | σ ( n) ​ ( A) |. L_{n+1}(k)=|\tilde{\omega}|+2k|\sigma^{(n)}(A)|. |  |

We are now in the position of being able to increase the length of the word without increasing the maximal sum of M + 1 M+1, so as c n c_{n} is divergent, choose k ≥ 1 k\geq 1 minimal such that

 | M + 1 c ⁡ ( | ω ~ ​ | + k | ​ σ ( n) ​ ( A) |) ≤ 1. \frac{M+1}{c(|\tilde{\omega}|+k|\sigma^{(n)}(A)|)}\leq 1. |  |

After applying g g twice (to skip past the next θ k > 1 / 2 \theta_{k}>1/2), then, we find ourselves able to manipulate the growth of the minimal sums m ⁡ ( n) m(n). Continuing in this fashion, then, we construct a dense set of θ \theta (as the initial string of partial quotients was arbitrary). That the lim sup \limsup s are actually one follows from the minimal choice of k k and that Δ ​ c n \Delta c_{n}, Δ ​ d n \Delta d_{n} are bounded.

To prove the analogous statements where one of M n M_{n}, m n m_{n} is desired to remain bounded, one need only repeat the same arguments using θ n ∈ H \theta_{n}\in H (recall ( 19)) so that the value p n p_{n} is eventually constant.

The statement of Theorem 1.2 applies as well to M n ​ ( x ​ ( θ)) M_{n}(x(\theta)) and m n ​ ( x ​ ( θ)) m_{n}(x(\theta)); the proof is simpler, in fact, as the map Ψ \Psi is not a concern, and the possible error of one from Proposition 5.2 is not an asymptotic concern. This process is highly amenable to diagonalization techniques. For example:

###### Corollary 6.1.

Given a countable collection of sequences c n ( i) c^{(i)}_{n} and d n ( i) d^{(i)}_{n}, all of which are divergent and in o ⁡ ( n) o(n), such that

 | c n ( 1) ≤ c n ( 2) ≤ …, d n ( 1) ≥ d n ( 2) ≥ …, c^{(1)}_{n}\leq c^{(2)}_{n}\leq\ldots,\quad d^{(1)}_{n}\geq d^{(2)}_{n}\geq\ldots, |  |

there is a dense set of θ \theta for which

 | c n ( i) ∈ o ⁡ ( M n ​ ( 0)), | m n ​ ( 0) | ∈ o ⁡ ( d n ( i)) c^{(i)}_{n}\in o(M_{n}(0)),\quad|m_{n}(0)|\in o(d^{(i)}_{n}) |  |

for all i i.

###### Proof.

Apply Theorem 1.2 after using a diagonalization process to construct c n c_{n}, d n d_{n}, both monotone, divergent, and in o ⁡ ( n) o(n) such

 | c n ( i) ∈ o ⁡ ( c n), d n ∈ o ⁡ ( d n ( i)). ∎ c^{(i)}_{n}\in o(c_{n}),\quad d_{n}\in o(d^{(i)}_{n}).\qed |  |

Many permutations of the above corollary are possible. For example, we may construct a dense set of θ \theta such that the discrepancy sums grow in both directions faster than any n 1 − ϵ n^{1-\epsilon} (but necessarily in o ⁡ ( n) o(n), of course!), or such that the discrepancy sums are bounded below, but M n ​ ( 0) M_{n}(0) grows slower than all iterated logarithms (but necessarily divergent, of course!), etc. See Figure 4 for an example where for both θ \theta and γ ⁡ ( θ) \gamma(\theta) we have m n ≥ 1 m_{n}\geq 1, but M n ​ ( θ) ∉ o ⁡ ( n 1 − ϵ) M_{n}(\theta)\notin o(n^{1-\epsilon}) for any ϵ > 0 \epsilon>0 while M n ​ ( γ ⁡ ( θ)) ∈ o ⁡ ( log ( i) ⁡ n) M_{n}(\gamma(\theta))\in o(\log^{(i)}n) for all i i. In Figure 4 we set

 | θ = [2, 2 2, 2, 2 2 2, 2, 2 2 2 2, 2, …]. \theta=[2,2^{2},2,2^{2^{2}},2,2^{2^{2^{2}}},2,\ldots]. |  |

[image: Refer to caption] (a) θ \theta exhibiting very slow growth of M n ​ ( 0) M_{n}(0); this portion of the graph will repeat 2 16 2^{16} times with no additional growth.

[image: Refer to caption] (b) γ ⁡ ( θ) \gamma(\theta) exhibiting very fast growth of M n ​ ( 0) M_{n}(0); this sawtooth pattern will continue to climb by repeating itself E ⁡ ( 2 16) / 2 E(2^{16})/2 times.

Figure 4. Two different extreme growth rates for θ \theta and γ ⁡ ( θ) \gamma(\theta).

Using diagonalization techniques one may similarly find a dense set of θ \theta such that

 | lim sup i → ∞ M n i ​ ( j) ​ ( 0) c n i ​ ( j) ( j) = 1 \limsup_{i\rightarrow\infty}\frac{M_{n_{i}(j)}(0)}{c^{(j)}_{n_{i}(j)}}=1 |  |

for an arbitrary collection of divergent sequences c n ( j) c^{(j)}_{n} in o ⁡ ( n) o(n) for different subsequences n i ​ ( j) → ∞ n_{i}(j)\rightarrow\infty depending on j j, and similarly for the | m n ​ ( 0) | |m_{n}(0)| and a collection of sequences d n ( j) d^{(j)}_{n}.

Truly, beyond the constraints of ( 2), any asymptotic behavior desired is possible.

## 7. Proof of Theorem 1.3

Suppose that

(25) |  | lim inf n → ∞ M n ​ ( 0) | m n ​ 0 | = r 1, lim sup n → ∞ M n ​ ( 0) | m n ​ ( 0) | = r 2. \liminf_{n\rightarrow\infty}\frac{M_{n}(0)}{|m_{n}{0}|}=r_{1},\quad\limsup_{n\rightarrow\infty}\frac{M_{n}(0)}{|m_{n}(0)|}=r_{2}. |  |

That the set of accumulation points of the sequence is the entire closed interval [r 1, r 2] [r_{1},r_{2}] is direct and is left to the reader. Let an arbitrary finite string of partial quotients a 1, …, a N a_{1},\ldots,a_{N} be given which determine θ i \theta_{i} for i = 0, 1, …, n − 1 i=0,1,\ldots,n-1, and for convenience again assume without loss of generality that p n = 0 p_{n}=0.

Now let c n c_{n} and d n d_{n} be arbitrary integer-valued strictly increasing sequences such that Δ ​ c n \Delta c_{n} and Δ ​ d n \Delta d_{n} are in O ⁡ ( 1) O(1) and

 | lim inf n → ∞ c n d n = ρ 1, lim sup n → ∞ c n d n = ρ 2. \liminf_{n\rightarrow\infty}\frac{c_{n}}{d_{n}}=\rho_{1},\quad\limsup_{n\rightarrow\infty}\frac{c_{n}}{d_{n}}=\rho_{2}. |  |

Furthermore, assume that c 1 > M ⁡ ( Ω n ′) = M c_{1}>M(\Omega^{\prime}_{n})=M and d 1 > | m ⁡ ( Ω n ′) | = m d_{1}>|m(\Omega^{\prime}_{n})|=m.

Continue the continued fraction expansion of θ \theta in the following way:

 | θ n = [2 ​ ( c 1 − M) + 1, 2 ​ ( d 1 − m), 2 ​ ( c 2 − c 1), 2 ​ ( d 2 − d 1), …]. \theta_{n}=[2(c_{1}-M)+1,2(d_{1}-m),2(c_{2}-c_{1}),2(d_{2}-d_{1}),\ldots]. |  |

Then Ω n ′ \Omega^{\prime}_{n} will see the sequence of M ⁡ ( Ω n + 2 ​ k ′) = c k M(\Omega^{\prime}_{n+2k})=c_{k} and m ⁡ ( Ω n + 2 ​ k ′) = − d k m(\Omega^{\prime}_{n+2k})=-d_{k}; the bounded differences Δ ​ c n \Delta c_{n} and Δ ​ d n \Delta d_{n} ensure that the limiting behavior is the same as the limiting behavior along the subsequence of times | Ω n ′ | |\Omega^{\prime}_{n}|.

###### Example 7.1.

Suppose that θ = [1, 2, 3, 4, …] \theta=[1,2,3,4,\ldots]. Then we begin computing the sequence of values M n ​ ( 0) M_{n}(0) and | m n ​ ( 0) | |m_{n}(0)| according to Proposition 5.2:

(26) |  | θ 0 = [1, 2, 3, 4, …] p = 0 E ⁡ ( a 1) = 0 ( M, | m |) = ( 1, 1) θ 1 = [3, 3, 4, 5, …] p = 1 E ⁡ ( a 1) = 1 ( M, | m |) = ( 1, 0) θ 2 = [1, 3, 4, 5, …] p = 1 E ⁡ ( a 1) = 0 ( M, | m |) = ( 1, 0) θ 3 = [4, 4, 5, 6, …] p = 0 E ⁡ ( a 1) = 2 ( M, | m |) = ( 3, 0) θ 4 = [5, 6, 7, 8, …] p = 0 E ⁡ ( a 1) = 2 ( M, | m |) = ( 5, 0) θ 5 = [1, 6, 7, 8 ​ …] p = 0 E ⁡ ( a 1) = 0 ( M, | m |) = ( 5, 0) θ 6 = [7, 7, 8, 9, …] p = 1 E ⁡ ( a 1) = 3 ( M, | m |) = ( 5, 3) ⋮ ⋮ ⋮ ⋮ \begin{array}[]{|c |c |c |c|}\hline\cr\theta_{0}=[1,2,3,4,\ldots]&p=0&E(a_{1})=0&(M,|m|)=(1,1)\\ \theta_{1}=[3,3,4,5,\ldots]&p=1&E(a_{1})=1&(M,|m|)=(1,0)\\ \theta_{2}=[1,3,4,5,\ldots]&p=1&E(a_{1})=0&(M,|m|)=(1,0)\\ \theta_{3}=[4,4,5,6,\ldots]&p=0&E(a_{1})=2&(M,|m|)=(3,0)\\ \theta_{4}=[5,6,7,8,\ldots]&p=0&E(a_{1})=2&(M,|m|)=(5,0)\\ \hline\cr\theta_{5}=[1,6,7,8\ldots]&p=0&E(a_{1})=0&(M,|m|)=(5,0)\\ \theta_{6}=[7,7,8,9,\ldots]&p=1&E(a_{1})=3&(M,|m|)=(5,3)\\ \vdots&\vdots&\vdots&\vdots\\ \hline\cr\end{array} |  |

The pattern is seen to continue in groups of five terms. Over the terms θ 5 ​ k \theta_{5k} through θ 5 ​ k + 4 \theta_{5k+4}, we will subtract 2 ​ k + 1 2k+1 from m m while adding 2 ​ ( 2 ​ k + 2) 2(2k+2) to M M. We therefore have ρ 1 = ρ 2 = 2 \rho_{1}=\rho_{2}=2, or

 | lim n → ∞ M n ​ ( 0) | m n ​ ( 0) | = 2. \lim_{n\rightarrow\infty}\frac{M_{n}(0)}{|m_{n}(0)|}=2. |  |

See Figure 5 for this θ \theta.

[image: Refer to caption] Figure 5. A specific θ \theta for which M n ​ ( 0) / | m n ​ ( 0) | M_{n}(0)/|m_{n}(0)| has limit two; refer to ( 26) and note the changes to M M, m m.

## 8. Proof of Theorem 1.4

###### Lemma 8.1.

Suppose that f ⁡ ( x) f(x) is a step function on S 1 S^{1} with k < ∞ k<\infty discontinuities, and denote V ⁡ ( f) V(f) the variation of f f. Define S n ​ ( x) S_{n}(x), M n ​ ( x) M_{n}(x) and m n ​ ( x) m_{n}(x) as before. As we have not restricted f f to be integer-valued, define

 | ρ N ​ ( x) = ( M N − m N) ​ ( x). \rho_{N}(x)=\left(M_{N}-m_{N}\right)(x). |  |

Let n n be such that q n ≤ N < q n + 1 q_{n}\leq N<q_{n+1}. Then for any x, y ∈ S 1 x,y\in S^{1}:

 | ρ N ​ ( y) ≤ ρ q n + 2 ​ ( x) + a n + 1 ​ V ​ ( f). \rho_{N}(y)\leq\rho_{q_{n+2}}(x)+a_{n+1}V(f). |  |

###### Proof.

Consider the set { x + i ​ θ } \{x+i\theta\} for i = 0, 1, …, q n − 1 i=0,1,\ldots,q_{n}-1. Choose 0 ≤ j < q n 0\leq j<q_{n} such that x + j ​ θ x+j\theta is closest to y y. Then the distance between x + j ​ θ x+j\theta and y y is no larger than q n − 1 q_{n}^{-1}. For each discontinuity d i d_{i} there are therefore at most a n + 1 a_{n+1} preimages of d i d_{i} within this interval for time L = 0, 1, …, q n + 1 − 1 L=0,1,\ldots,q_{n+1}-1. It follows that f ⁡ ( x + ( j + i) ​ θ) = f ⁡ ( y + i ​ θ) f(x+(j+i)\theta)=f(y+i\theta) for all but at most k ⋅ a n + 1 k\cdot a_{n+1} of i = 0, 1, …, N < q n + 1 i=0,1,\ldots,N<q_{n+1}. As j + i j+i is less than q n + q n + 1 ≤ q n + 2 q_{n}+q_{n+1}\leq q_{n+2}, the lemma follows. ∎

Assume that a i ​ ( θ) ≤ M a_{i}(\theta)\leq M for all i i. Then (continuing with existing notation) we see that for some C > 1 C>1 independent of θ \theta

(27) |  | C n − 1 2 ≤ | Ω n ′ | ≤ ( M + 1) 2 ​ n + 2. C^{\frac{n-1}{2}}\leq|\Omega^{\prime}_{n}|\leq(M+1)^{2n+2}. |  |

The lower bound is due to the exponential decay in the length of the interval I ~ n \tilde{I}_{n} (any C < 2 C<2 eventually suffices, as I ~ n + 1 \tilde{I}_{n+1} is less than half as large as I ~ n \tilde{I}_{n} at least half the time, with the n − 1 n-1 accounting for the possibility that I 1 ′ = I 0 I^{\prime}_{1}=I_{0}, or θ 0 > 1 / 2 \theta_{0}>1/2). The upper bound follows from Lemma 5.4, Lemma 5.5, and the bound a i ​ ( θ) ≤ M a_{i}(\theta)\leq M. while at the same time,

(28) |  | n − 1 2 ≤ ρ | Ω n ′ | ​ ( 0) ≤ n ​ M 2; \frac{n-1}{2}\leq\rho_{|\Omega^{\prime}_{n}|}(0)\leq\frac{nM}{2}; |  |

the lower inequality is due to the fact that at most half of the words Ω n ′ = Ω n + 1 ′ \Omega^{\prime}_{n}=\Omega^{\prime}_{n+1} (corresponding to those θ n > 1 / 2 \theta_{n}>1/2) and for the rest, ρ ⁡ ( Ω n + 1) ≥ ρ ⁡ ( Ω n) + 1 \rho(\Omega_{n+1})\geq\rho(\Omega_{n})+1, as E ⁡ ( a 1) ≥ 1 E(a_{1})\geq 1 for these θ n < 1 / 2 \theta_{n}<1/2. The upper bound follows as E ⁡ ( a i ​ ( θ)) ≤ M / 2 E(a_{i}(\theta))\leq M/2 for all i i.

Now, for any N N let k k be chosen such that

 | | Ω k | ≤ N ≤ | Ω k + 1 |. |\Omega_{k}|\leq N\leq|\Omega_{k+1}|. |  |

From ( 27):

 | k ​ C 1 ≤ log ⁡ | Ω k ′ | ≤ log ⁡ ( N) ≤ log ⁡ | Ω k + 1 ′ | ≤ k ​ C 2, kC_{1}\leq\log|\Omega^{\prime}_{k}|\leq\log(N)\leq\log|\Omega^{\prime}_{k+1}|\leq kC_{2}, |  |

for two constants C 1 C_{1} and C 2 C_{2} which do not depend on k k. From ( 28):

 | ( k + 1) ​ M 2 ≥ ρ | Ω k + 1 ′ | ​ ( 0) ≥ ρ N ​ ( 0) ≥ ρ | Ω k ′ | ​ ( 0) ≥ k − 1 2, \frac{(k+1)M}{2}\geq\rho_{|\Omega^{\prime}_{k+1}|}(0)\geq\rho_{N}(0)\geq\rho_{|\Omega^{\prime}_{k}|}(0)\geq\frac{k-1}{2}, |  |

so ρ n ​ ( 0) ∼ log ⁡ ( n) \rho_{n}(0)\sim\log(n). The full theorem now follows from Lemma 8.1.

## Acknowledgements

The author is greatly indebted to many people for support and helpful conversations over the development of this paper. The original impetus for studying this problem came from a problem posed by M. Boshernitzan while the author was a Ph.D. student at Rice University, while a rudimentary form of Theorem 1.2 arose from discussions at PRIMA 2008 during a visit supported by the University of New South Wales. The author is currently supported by the Center for Advanced Studies at Ben Gurion University of the Negev, where Barak Weiss has provided invaluable suggestions on improving the clarity of an early draft. Of course, any mistakes or unclear passages in the current form are entirely the author’s responsibility.

## References

- [1] Boris Adamczewski. Répartition des suites ( n ​ α) n ∈ ℕ (n\alpha)_{n\in\mathbb{N}} et substitutions. Acta Arith., 112(1):1–22, 2004.
- [2] Michael Boshernitzan and David Ralston. Continued fractions and heavy sequences. Proc. Amer. Math. Soc., 137(10):3177–3185, 2009.
- [3] N. Pytheas Fogg. Substitutions in dynamics, arithmetics and combinatorics, volume 1794 of Lecture Notes in Mathematics. Springer-Verlag, Berlin, 2002. Edited by V. Berthé, S. Ferenczi, C. Mauduit and A. Siegel.
- [4] Doug Hensley. Continued Fractions. World Scientific Publishing Co. Pte. Ltd., Hackensack, NJ, 2006.
- [5] Harry Kesten. On a conjecture of Erdős and Szüsz related to uniform distribution mod ​ 1 {\rm mod}\ 1. Acta Arith., 12:193–212, 1966/1967.
- [6] A. Ya. Khinchin. Continued fractions. Dover Publications Inc., Mineola, NY, russian edition, 1997. With a preface by B. V. Gnedenko, Reprint of the 1964 translation.

[◄][2][image: ar5iv homepage] [3]
[Feeling lucky?][4] [5]
[Conversion report][6]
[Report an issue][7]
[View original on arXiv][8] [►][9]


## Links

[1]: mailto:ralston.david.s@gmail.com
[2]: /html/1105.5809
[3]: /
[4]: /feeling_lucky
[5]: /land_of_honey_and_milk
[6]: /log/1105.5810
[7]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1105.5810
[8]: https://arxiv.org/pdf/1105.5810
[9]: /html/1105.5811
