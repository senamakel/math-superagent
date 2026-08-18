<!-- source: https://ar5iv.labs.arxiv.org/html/0809.0603 | converted from HTML -->

[0809.0603] Relation between powers of factors and recurrence function characterizing Sturmian words

# Relation between powers of factors and recurrence
function characterizing Sturmian words

Z. Masáková 1 1 1 corresponding author and E. Pelantová

Doppler Institute & Department of Mathematics

FNSPE, Czech Technical University

Trojanova 13, 120 00 Praha 2, Czech Republic

e-mails: zuzana.masakova@fjfi.cvut.cz, edita.pelantova@fjfi.cvut.cz

###### Abstract

In this paper we use the relation of the index of an infinite aperiodic word and its recurrence function to give another characterization of Sturmian words. As a byproduct, we give a new proof of theorem describing the index of a Sturmian word in terms of the continued fraction expansion of its slope. This theorem was independently proved in [7] and [9].

## 1 Introduction

Sturmian words constitute the most studied example of aperiodic infinite words. For the first time they appeared in the paper of Morse and Hedlund in 1938 [17]. But even after 70 years of extensive research, Sturmian words continue to attract attention of numerous mathematicians and newly also computer scientists. The appeal of Sturmian words stems in that they appear in various contexts. This is also why Sturmian words are often hidden under different titles: cutting sequences, Beatty sequences, mechanical words, etc. The beauty of Sturmian words consists in the abundance of equivalent definitions. Already Morse and Hedlund in [18] show that Sturmian words can be characterized by the so-called balance property. The reference [14] contains a nice exposition on diverse definitions of Sturmian words. The most recent ones, which [14] does not mention, are characterization of Sturmian words using return words given by Vuillon [21] (for less technical proof see [2]), characterization using the number of palindromes of given length given in [10] and yet another characterization by Richomme [19].

The aim of this paper is to give another equivalent definition of Sturmian words. Our characteristics puts into relation the recurrence function and the index of an infinite word u u. Flagrant similarity between formulas for recurrence quotient and index of a Sturmian word was noted already in [1, 5, 7].

The recurrence function R R associates to every n ∈ ℕ n\in\mathbb{N} the minimal length R ⁡ ( n) ∈ ℕ R(n)\in\mathbb{N} such that arbitrary segment of the infinite word u u of length R ⁡ ( n) R(n) contains all factors of u u of length n n. This function has been studied already by Hendlund and Morse, who gave an explicit formula for R ⁡ ( n) R(n) for an arbitrary Sturmian word u u and determined the so-called recurrence quotient, lim sup n → ∞ R ⁡ ( n) / n \limsup_{n\to\infty}{R(n)}/{n}. On the other hand, the index of an infinite word u u describes the maximal repetition of a factor of u u. The study of the index of infinite words is considerably younger, nevertheless, in the last decade very intense, especially due to applications in spectral theory for corresponding Schrödinger operators [8].

Repetitions in the most prominent Sturmian word, namely the Fibonacci word, were studied in [13]. More general results about index of Sturmian words can be found in [3, 5, 6, 12, 15, 16, 20]. The complete solution to the problem was given independently by Carpi and de Luca in [7] and by Damanik and Lenz in [9].

The paper is organized as follows. In Section 2 we introduce all necessary notions. Section 3 contains the proof of the main result of the paper, namely the following theorem.

###### Theorem 1.1.

A uniformly recurrent infinite word u u is Sturmian if and only if there exist infinitely many factors w w of u u such that

 | R ⁡ ( | w |) = | w | ​ ind ​ ( w) + 1. R(|w|)=|w|\,{\rm ind}(w)+1\,. |  |

Notation | w | |w| stands for the length of the factor w w, and ind ⁡ ( w) {\rm ind}(w) is the maximal rational exponent r r such that w r w^{r} is a factor of u u.

It was pointed to us that already from [7] one can extract that Sturmian words satisfy the above equality for infinitely many factors. Their proof uses the explicit formula for recurrence function from [18]. Our proof relies on Vuillon’s description of Sturmian words by return words and avoids manipulation with continued fraction of the slope of the Sturmian word. Our theorem moreover states that Sturmian words are the only having the above property.

With the help of Theorem 1.1, one can derive the upper bound on the index of u u (Section 4). In Section 5 we prove that the bound is in fact reached. For the construction of factors of u u with large repetition we use the knowledge of Sturmian morphisms, i.e. morphisms preserving the family of Sturmian words, as described in [4]. Sections 4 and 5 thus represent an alternative proof of the result of [7] and [9].

## 2 Preliminaries

An alphabet 𝒜 \mathcal{A} is a finite set of symbols, called A word w w of length | w | = n |w|=n is a concatenation of n n letters. The number of letters X X occurring in the word w w is denoted by | w | X |w|_{X}. 𝒜 ∗ {\mathcal{A}}^{*} is the set of all finite words over the alphabet 𝒜 {\mathcal{A}} including the empty word ϵ \epsilon. Equipped with the operation of concatenation, it is a monoid. We define also infinite words u = ( u n) n ∈ ℕ ∈ 𝒜 ℕ u=(u_{n})_{n\in\mathbb{N}}\in{\mathcal{A}}^{\mathbb{N}}.

A finite word v ∈ 𝒜 ∗ v\in{{\mathcal{A}}}^{*} is called a factor of a word w w (finite or infinite), if there exist words w ( 1), w ( 2) w^{(1)},w^{(2)} such that w = w ( 1) ​ v ​ w ( 2) w=w^{(1)}vw^{(2)}. If w ( 1) = ϵ w^{(1)}=\epsilon, then v v is said to be a prefix of w w, if w ( 2) = ϵ w^{(2)}=\epsilon, then v v is a suffix of w w. The set of all factors of length n n of an infinite word u u is denoted by Ł n ​ ( u) \L_{n}(u), the set of all factors of u u is called the language of u u and denoted by Ł ⁡ ( u) \L(u).

The mapping 𝒞: n ↦ #​ Ł n ​ ( u) {\mathcal{C}}:n\mapsto\#\L_{n}(u) is called the complexity of the infinite word u u. For determining the complexity of an infinite word one uses the so-called special factors. A factor w ∈ Ł ⁡ ( u) w\in\L(u) is called left special, if there exist letters A, B ∈ 𝒜 A,B\in{\mathcal{A}}, A ≠ B A\neq B, such that both A ​ w Aw and B ​ w Bw belong to Ł ⁡ ( u) \L(u). Similarly, one defines right special factors. A factor of u u is called bispecial, if it is in the same time right special and left special. Every eventually periodic word has bounded complexity. For aperiodic words, one has for all n ∈ ℕ n\in\mathbb{N} that 𝒞 ⁡ ( n) ≥ n + 1 {\mathcal{C}}(n)\geq n+1. Infinite words, for which equality holds for all n ∈ ℕ n\in\mathbb{N}, i.e. aperiodic words with minimal complexity, are called Sturmian words. Directly from the definition one can derive that in the language of a Sturmian word u u one has exactly one left special and exactly one right special factor of each length, and Sturmian words are characterized by this property.

Sturmian words are obviously defined over a binary alphabet, say { A, B } \{A,B\}. The densities of letters A A, B B in a Sturmian word u = ( u i) i ∈ ℕ u=(u_{i})_{i\in\mathbb{N}} are well defined,

 | ϱ ⁡ ( A) = lim n → ∞ | u 0 ⋯ u n − 1 | A n = α, ϱ ⁡ ( B) = lim n → ∞ | u 0 ⋯ u n − 1 | B n = 1 − α, \varrho(A)=\lim_{n\to\infty}\frac{|u_{0}\cdots u_{n-1}|_{A}}{n}=\alpha\,,\qquad\varrho(B)=\lim_{n\to\infty}\frac{|u_{0}\cdots u_{n-1}|_{B}}{n}=1-\alpha\,, |  |

for some α ∈ ( 0, 1) \alpha\in(0,1). In fact, the language of a Sturmian word u u depends only on the parameter α \alpha, which is also called the slope of u u. For a given α \alpha, one can construct all Sturmian words with the slope α \alpha for example as codings of different orbits under an exchange of two intervals. Let α ∈ ( 0, 1) \alpha\in(0,1) be an irrational number. Denote I = [0, 1) I=[0,1) (resp. I = ( 0, 1] I=(0,1]) and I A = [0, α) I_{A}=[0,\alpha), I B = [α, 1) I_{B}=[\alpha,1) (resp. I A = ( 0, α] I_{A}=(0,\alpha], I B = ( α, 1] I_{B}=(\alpha,1]). The mapping T: I ↦ I T:I\mapsto I given by the prescription

 | T ⁡ ( x) = { x + 1 − α for ​ x ∈ I A, x − α for ​ x ∈ I B, T(x)=\left\{\begin{array}[]{ll}x+1-\alpha&\hbox{ for }x\in I_{A}\,,\\ x-\alpha&\hbox{ for }x\in I_{B}\,,\end{array}\right. |  |

is called an exchange of two intervals with slope α \alpha. For an arbitrary x 0 ∈ I x_{0}\in I we define an infinite word ( u n) n ∈ ℕ (u_{n})_{n\in\mathbb{N}} by

 | u n = X ∈ { A, B } if T n ​ ( x 0) ∈ I X. u_{n}=X\in\{A,B\}\quad\hbox{if}\quad T^{n}(x_{0})\in I_{X}\,. |  | (1) |

It is known that the set of Sturmian words coincides with the set of infinite words given by the prescription ( 1). Since we assume that the slope is irrational, the language of a Sturmian word does not depend on the choice of the initial point x 0 x_{0}, but only on α \alpha. Due to the symmetry α ↔ 1 − α \alpha\leftrightarrow 1-\alpha, studying the language of a Sturmian word, one can consider without loss of generality only parameters α > 1 2 \alpha>\frac{1}{2}. From the exchange of intervals is not difficult to see that with such an assumption, ϱ ⁡ ( A) > ϱ ⁡ ( B) \varrho(A)>\varrho(B) and, in fact, the Sturmian word can be viewed as composed by blocks of the form A k A^{k}, A k + 1 A^{k+1}, with k = ⌊ α 1 − α ⌋ k=\lfloor\frac{\alpha}{1-\alpha}\rfloor, separated by single letters B B.

In this paper we study repetition of factors in Sturmian words. We say that a word v v is a power of a word w w, if | v | ≥ | w | |v|\geq|w| and v v is a prefix of the periodic word w w w ⋯ www\cdots. We write v = w r v=w^{r} where r = | v | / | w | r=|v|/|w|. The index of a word w w in an infinite word u u is defined by

 | ind ⁡ ( w) = sup { r ∈ ℚ ∣ w r ∈ Ł ⁡ ( u) }. {\rm ind}(w)=\sup\{r\in\mathbb{Q}\mid w^{r}\in\L(u)\}\,. |  | (2) |

A power v v of w w with maximal r r is called a maximal repetition of w w. We have thus v = w ind ⁡ ( w) v=w^{{\rm ind}(w)}. From what it was said above, it is clear that in a Sturmian word with slope α > 1 2 \alpha>\frac{1}{2}, one has

 | ind ⁡ ( B) = 1 and ind ⁡ ( A) = ⌊ α 1 − α ⌋ + 1. {\rm ind}(B)=1\qquad\hbox{ and }\qquad{\rm ind}(A)=\Bigl\lfloor\frac{\alpha}{1-\alpha}\Bigr\rfloor+1\,. |  | (3) |

Taking supremum of indices over all factors of an infinite word u u, one obtains an important characteristics of u u, the so-called index of u u. Formally,

 | ind ⁡ ( u) = sup { ind ⁡ ( w) ∣ w ∈ Ł ⁡ ( u) }. {\rm ind}(u)=\sup\{{\rm ind}(w)\mid w\in\L(u)\}\,. |  | (4) |

It turns out that for the study of index of Sturmian words, the notion of return words and recurrence function is important. A return word of a factor w w of an infinite word u u is a factor v ∈ Ł ⁡ ( u) v\in\L(u) such that v ​ w ∈ Ł ⁡ ( u) vw\in\L(u), w w is a prefix of v ​ w vw and the factor w w occurs in v ​ w vw exactly twice. The factor v ​ w vw is often called a complete return word of w w. The set of return words of a factor w w is denoted by Ret ⁡ ( w) {\rm Ret}(w). If the set Ret ⁡ ( w) {\rm Ret}(w) is finite for any factor w w of an infinite word u u, then u u is said to be uniformly recurrent. In fact, it means that distances between consecutive occurrences of a given factor are bounded. Let us mention that for a uniformly recurrent word u u the supremum in ( 2) is always reached, as will be explained later, and therefore the notion of index of u u in ( 4) has sense. For a uniformly recurrent infinite word u u we define a mapping R: ℕ ↦ ℕ R:\mathbb{N}\mapsto\mathbb{N} by the prescription

 | R ( n):= − 1 + max { | v w | | v ∈ Ret ( w), w ∈ Ł n ( u) }, R(n):=-1+\max\bigl\{|vw|\,\bigm|\,v\in{\rm Ret}(w),\,w\in\L_{n}(u)\bigr\}\,, |  | (5) |

i.e. R ⁡ ( n) + 1 R(n)+1 is equal to the maximum of lengths of a complete return word over all factors of length n n. It is not difficult to see that an arbitrary segment of the infinite word u u of length R ⁡ ( n) R(n) contains all factors of the word u u of length n n. Formally, we have

 | Ł n ( u) = { u i u i + 1 ⋯ u i + n − 1 ∣ k ≤ i ≤ k + R ( n) − n + 1 }, for all k ∈ ℕ. \L_{n}(u)=\{u_{i}u_{i+1}\cdots u_{i+n-1}\mid k\leq i\leq k+R(n)-n+1\}\,,\quad\hbox{for all }\ k\in\mathbb{N}\,. |  | (6) |

Moreover, the number R ⁡ ( n) R(n) is the smallest possible, so that ( 6) remains valid. The mapping R ⁡ ( n) R(n) is called the recurrence function of the infinite word u u.

## 3 Recurrence function and index

Our aim is to find relation between the recurrence function (well defined for uniformly recurrent words) and the index of aperiodic words. We first show that index of every factor in an aperiodic uniformly recurrent word is finite, and we then determine a lower bound on the recurrence function.

###### Proposition 3.1.

Let u u be an aperiodic uniformly recurrent word. Then for every factor w ∈ Ł ⁡ ( u) w\in\L(u) we have ind ⁡ ( w) < + ∞ \ {\rm ind}(w)<+\infty\ and

 | R ⁡ ( | w |) ≥ | w | ​ ind ​ ( w) + 𝒞 ⁡ ( | w |) − | w |. R(|w|)\ \geq\ |w|\,{\rm ind}(w)+{\mathcal{C}}(|w|)-|w|\,. |  | (7) |

###### Proof.

Let w = w 1 ⋯ w n w=w_{1}\cdots w_{n} be a factor of u u. We first show that ind ⁡ ( w) {\rm ind}(w) is finite. Without loss of generality, let ind ⁡ ( w) ≥ 2 {\rm ind}(w)\geq 2. Obviously, all factors of the form w i ⋯ w n w 1 ⋯ w i − 1 w_{i}\cdots w_{n}w_{1}\cdots w_{i-1} for any 1 ≤ i ≤ n 1\leq i\leq n belong to Ł ⁡ ( u) \L(u). (Such factors are called conjugates of w w.) Since 𝒞 ⁡ ( n) ≥ n + 1 {\mathcal{C}}(n)\geq n+1, there exists a factor w ′ w^{\prime} which is not conjugate of w w. If Ł ⁡ ( u) \L(u) contained factors w k w^{k} for all k ∈ ℕ k\in\mathbb{N}, then distances between consecutive occurrences of w ′ w^{\prime} would be unbounded, which would contradict uniform recurrence of u u. Therefore ind ⁡ ( w) < + ∞ {\rm ind}(w)<+\infty.

Let now v v be a maximal repetition of w w. We prolong v v to a factor v ​ v ′ ∈ Ł ⁡ ( u) vv^{\prime}\in\L(u) so that v ​ v ′ vv^{\prime} contains all 𝒞 ⁡ ( | w |) {\mathcal{C}}(|w|) factors of u u of length | w | |w|, but none of prefixes of v ​ v ′ vv^{\prime} satisfies it. Since v v has at most | w | |w| factors of length | w | |w|, (namely the conjugates of w w), we must have | v ′ | ≥ 𝒞 ⁡ ( | w |) − | w | |v^{\prime}|\geq{\mathcal{C}}(|w|)-|w|. From the definition of the recurrence function, we have

 | R ⁡ ( | w |) ≥ | v ​ v ′ | ≥ | v | + 𝒞 ⁡ ( | w |) − | w |. R(|w|)\geq|vv^{\prime}|\geq|v|+{\mathcal{C}}(|w|)-|w|\,. |  |

As v = | w | ​ ind ​ ( w) v=|w|\,{\rm ind}(w), the proof is complete. ∎

Note that in particular, for a Sturmian word u u one has R ⁡ ( | w |) ≥ | w | ​ ind ​ ( w) + 1 R(|w|)\ \geq\ |w|\,{\rm ind}(w)+1 for every factor w w of u u. The following proposition states, that if equality is reached for infinitely many factors w w of an aperiodic word u u, then u u is Sturmian.

###### Proposition 3.2.

Let u u be an aperiodic uniformly recurrent infinite word. If there exist infinitely many factors w ∈ Ł ⁡ ( u) w\in\L(u) such that R ⁡ ( | w |) = | w | ​ ind ​ ( w) + 1 R(|w|)\ =\ |w|\,{\rm ind}(w)+1, then u u is a Sturmian word.

###### Proof.

Using the assumption of the proposition and ( 7), there exist infinitely many factors w w of u u such that 𝒞 ⁡ ( | w |) ≤ | w | + 1 {\mathcal{C}}(|w|)\leq|w|+1, i.e. for infinitely many n ∈ ℕ n\in\mathbb{N} we have 𝒞 ⁡ ( n) ≤ n + 1 {\mathcal{C}}(n)\leq n+1. The complexity of an aperiodic word is a strictly increasing function and 𝒞 ⁡ ( 1) ≥ 2 {\mathcal{C}}(1)\geq 2. This implies that 𝒞 ⁡ ( n) = n + 1 {\mathcal{C}}(n)=n+1 for all n n and u u is therefore Sturmian. ∎

In order to show the opposite implication to that of Proposition 3.2, we need to cite a nice result of Vuillon [21] which characterizes Sturmian words using return words. He shows that a binary infinite word u u is Sturmian if and only if every factor of u u has exactly two return words. For every factor w w of a Sturmian word u u thus exist two finite words r 0 ​ ( w) r_{0}(w), r 1 ​ ( w) r_{1}(w) such that the suffix of u u starting with the first occurrence of w w can be written as an infinite concatenation of blocks r 0 ​ ( w) r_{0}(w) and r 1 ​ ( w) r_{1}(w), i.e.

 | u = p r i 0 ( w) r i 1 ( w) r i 2 ( w) r i 3 ( w) ⋯, u=p\,r_{i_{0}}(w)r_{i_{1}}(w)r_{i_{2}}(w)r_{i_{3}}(w)\cdots\,, |  |

where p p is a prefix of u u and i 0, i 1, i 2, i 3, ⋯ ∈ { 0, 1 } i_{0},i_{1},i_{2},i_{3},\cdots\in\{0,1\}. We can therefore define the so-called derivated word v = ( v n) n ∈ ℕ v=(v_{n})_{n\in\mathbb{N}} over the alphabet { 0, 1 } \{0,1\} by the prescription v n = i n v_{n}=i_{n}, coding the order of the blocks r 0 ​ ( w) r_{0}(w), r 1 ​ ( w) r_{1}(w) in the infinite concatenation. We could now study return words of factors of the newly defined infinite word v v. However, since return words of factors of the derivated word are in one-to-one correspondence with return words of factors in the original infinite word (see [11]), we deduce that every factor of v v has again exactly two return words, and thus is itself Sturmian.

It is obvious that for finding factors w w with the maximal index in the infinite word, we can limit our consideration to primitive factors w w, i.e. such that w ≠ z k w\neq z^{k} for any z ∈ Ł ⁡ ( u) z\in\L(u) and any k ∈ ℕ k\in\mathbb{N}, k ≥ 2 k\geq 2.

###### Proposition 3.3.

Let u u be a Sturmian word and let w ∈ Ł ⁡ ( u) w\in\L(u) be a primitive factor such that w ​ w ∈ Ł ⁡ ( u) ww\in\L(u), and, moreover, let it have the maximal index among all factors of u u of length n n with the above properties. Then

 | R ⁡ ( n) = n ​ ind ​ ( w) + 1. R(n)=n\,{\rm ind}(w)+1\,. |  |

###### Proof.

Let k = [ind ⁡ ( w)] k=[{\rm ind}(w)] and θ = { ind ⁡ ( w) } \theta=\{{\rm ind}(w)\}. Then w w can be written as w = w 1 ​ w 2 w=w_{1}w_{2} where | w 1 | = θ ​ n |w_{1}|=\theta n and the maximal repetition of w w is the word

 | ( w 1 w 2) ( w 1 w 2) ⋯ ( w 1 w 2) ⏟ k ​ times ​ w 1 ∈ Ł ⁡ ( u). \underbrace{(w_{1}w_{2})(w_{1}w_{2})\cdots(w_{1}w_{2})}_{k\ \hbox{\scriptsize times}}w_{1}\in\L(u)\,. |  |

Let us find X, Y ∈ { A, B } X,Y\in\{A,B\} such that

 | X w 1 w 2 ⋯ w 1 w 2 w 1 Y ∈ Ł ( u). Xw_{1}w_{2}\cdots w_{1}w_{2}w_{1}Y\in\L(u)\,. |  | (8) |

Since ind ⁡ ( w) = k + θ {\rm ind}(w)=k+\theta is the greatest power such that w k + θ ∈ Ł ⁡ ( u) w^{k+\theta}\in\L(u), the letter Y Y is not a prefix of w 2 w_{2}. Since w w is a primitive word with the greatest index in Ł n ​ ( u) \L_{n}(u), the letter X X is not a suffix of w 2 w_{2}. This, together with the fact that k ≥ 2 k\geq 2, means that w 1 ​ w 2 = w w_{1}w_{2}=w is a left special factor and w 2 ​ w 1 =: w ′ w_{2}w_{1}=:w^{\prime} is a right special factor. A Sturmian word has exactly one left special and one right special factor of each length.

Let us consider the Rauzy graph Γ n \Gamma_{n} of u u. The set of vertices of Γ n \Gamma_{n} is equal to Ł n ​ ( u) \L_{n}(u) and the set of its edges to Ł n + 1 ​ ( u) \L_{n+1}(u). The Rauzy graph Γ n \Gamma_{n} of a Sturmian word thus has n + 1 {n+1} vertices and n + 2 n+2 edges. An edge e ∈ Ł n + 1 ​ ( u) e\in\L_{n+1}(u) starts in a vertex v ∈ Ł n ​ ( u) v\in\L_{n}(u) and ends in v ′ ∈ Ł n ​ ( u) v^{\prime}\in\L_{n}(u) if v v is a prefix and v ′ v^{\prime} a suffix of e e. An arbitrary factor u u of length m ≥ n m\geq n in the language of the infinite word u u can be viewed as a path of length m − n m-n in the graph Γ n \Gamma_{n} starting in the vertex corresponding to the prefix and ending in the vertex corresponding to the suffix of u u of length n n.

Since w ∈ Ł n ​ ( u) w\in\L_{n}(u), w ​ w ∈ Ł ⁡ ( u) ww\in\L(u) and w w is primitive, there exists a cycle C C of length n n in the graph Γ n \Gamma_{n} containing the factor w w. Let us denote the vertices of the cycle C C by v ( 0) = w v^{(0)}=w, v ( 1) v^{(1)}, …, v ( n − 1) v^{(n-1)}. Since Γ n \Gamma_{n} has n + 1 n+1 vertices, only one of them is missing in C C. Let us denote it by v ( n) v^{(n)}. Recall that w w is the only left special factor in Ł n ​ ( u) \L_{n}(u), and thus the only vertex in Γ n \Gamma_{n} with indegree 2. Similarly, w ′ w^{\prime} is the only right special factor in Ł n ​ ( u) \L_{n}(u) and thus the only vertex in Γ n \Gamma_{n} with outdegree 2. Since Γ n \Gamma_{n} is a strongly connected graph, an edge must go from the vertex v ( n) v^{(n)} to the cycle C C and an edge from the cycle C C to the vertex v ( n) v^{(n)}. Thus w ′ = v ( s) w^{\prime}=v^{(s)} for some 0 ≤ s ≤ n − 1 0\leq s\leq n-1. Relation ( 8) implies that the edge from v ( s) v^{(s)} to v ( n) v^{(n)} is w 2 ​ w 1 ​ Y w_{2}w_{1}Y and the edge from v ( n) v^{(n)} to v ( 0) v^{(0)} is X ​ w 1 ​ w 2 Xw_{1}w_{2}. The Rauzy graph Γ n \Gamma_{n} is thus of the following form.

Let us consider the return words of w w. Since w ​ w ∈ Ł ⁡ ( u) ww\in\L(u), one of the return words of w w is r 0 ​ ( w) = w r_{0}(w)=w, the complete return word is w ​ w ww and the corresponding path in the Rauzy graph is the cycle C C. We denote the other return word of w w by r 1 ​ ( w) r_{1}(w). From the structure of the graph Γ n \Gamma_{n} it follows that the complete return word r 1 ​ ( w) ​ w r_{1}(w)w corresponds to the cycle C ′ C^{\prime} given by vertices v ( 0) v^{(0)}, v ( 1) v^{(1)}, …, v ( s) v^{(s)}, v ( n) v^{(n)}.

As we have already mentioned, the order of the blocks r 0 ​ ( w) r_{0}(w), r 1 ​ ( w) r_{1}(w) is given by the derivated word over the alphabet { 0, 1 } \{0,1\}, which is Sturmian. Since ( r 0 ​ ( w)) k = w k ∈ Ł ⁡ ( u) (r_{0}(w))^{k}=w^{k}\in\L(u), for k = ⌊ ind ⁡ ( w) ⌋ ≥ 2 k=\lfloor{\rm ind}(w)\rfloor\geq 2, the derivated word has blocks 0 k 0^{k}, 0 k − 1 0^{k-1} separated by single letters 1. As a consequence, among all factors of length n n, it is v ( n) v^{(n)} which has the longest complete return word, namely of the form

 | X ​ w w ⋯ w ⏟ k ​ times ​ w 1 ​ Y. X\underbrace{ww\cdots w}_{k\ \hbox{\scriptsize times}}w_{1}Y\,. |  |

From the definition ( 5) it follows that

 | R ⁡ ( n) = − 1 + | w k + θ | + 2 = 1 + ( k + θ) ​ n, R(n)=-1+|w^{k+\theta}|+2=1+(k+\theta)n\,, |  |

which completes the proof. ∎

###### Proof of Theorem 1.1.

In order to comlpete the proof of Theorem 1.1, we have to show that there exist infinitely many primitive factors w w with index at least 2. For the construction of such factors we make use of bispecial factors. Let b b be a bispecial factor in Ł ⁡ ( u) \L(u). Denote by n n its length, n:= | b | n:=|b| and by r 0 ​ ( b) r_{0}(b), r 1 ​ ( b) r_{1}(b) its return words. From the Rauzy graph Γ n \Gamma_{n} it follows that the two return words of b b are given by the two cycles in Γ n \Gamma_{n}, which have b b as the only common vertex. Therefore | r 0 ​ ( b) | + | r 1 ​ ( b) | = n + 2 |r_{0}(b)|+|r_{1}(b)|=n+2. Without loss of generality, let b b contain both letters. Then | r i ​ ( b) | ≥ 2 |r_{i}(b)|\geq 2. At least for one of the return words, say r 0 ​ ( b) r_{0}(b), it holds that n / 2 < | r 0 ​ ( b) | ≤ n n/2<|r_{0}(b)|\leq n, and therefore r 0 ​ ( b) r_{0}(b) is a prefix of b b. It follows that the complete return word r 0 ​ ( b) ​ b ∈ Ł ​ ( u) r_{0}(b)b\in\L(u) has as its prefix r 0 ​ ( b) ​ r 0 ​ ( b) r_{0}(b)r_{0}(b). Moreover, a return word of an arbitrary factor of any uniformly recurrent word is primitive. Thus we can take r 0 ​ ( b) r_{0}(b) for the desired factor w w. Since there are infinitely many bispecial factors b b, we can construct infinitely many primitive factors with index ≥ 2 \geq 2 and length ≥ | b | 2 \geq\frac{|b|}{2}. ∎

## 4 Upper bound on index of Sturmian words

In this section we mention the consequences of Proposition 3.3, which puts into relation the recurrence function and index of factors of a Sturmian word. In particular, we can very easily derive the upper bound on the index of a Sturmian word, which constitutes an alternative proof for the result of Damanik and Lenz [9]. The bound depends on the continued fraction expansion of the slope of the Sturmian word.

Recall the notion of continued fraction. To every irrational β ∈ ( 0, 1) \beta\in(0,1) one associates the continued fraction β = [0, b 1, b 2, …] \beta=[0,b_{1},b_{2},\dots], where b i ∈ ℤ b_{i}\in\mathbb{Z}, b i ≥ 1 b_{i}\geq 1. Obviously, if β > 1 2 \beta>\frac{1}{2}, then b 1 = 1 b_{1}=1. The convergents of β \beta form a sequence of fractions ( p n q n) (\frac{p_{n}}{q_{n}}),

 | p 1 q 1 = 1 b 1, p 2 q 2 = 1 b 1 + 1 b 2, p 3 q 3 = 1 b 1 + 1 b 2 + 1 b 3, … \frac{p_{1}}{q_{1}}=\frac{1}{b_{1}}\,,\qquad\frac{p_{2}}{q_{2}}=\cfrac{1}{b_{1}+\cfrac{1}{b_{2}}}\,,\qquad\frac{p_{3}}{q_{3}}=\cfrac{1}{b_{1}+\cfrac{1}{b_{2}+\cfrac{1}{b_{3}}}}\,,\qquad\dots |  |

We have p n p_{n} coprime to q n q_{n} and lim n → ∞ p n q n = β \lim_{n\to\infty}\frac{p_{n}}{q_{n}}=\beta.

It is known that the denominators q n q_{n} of convergents of β \beta satisfy the recurrence

 | q N = b N ​ q N − 1 + q N − 2 q_{N}=b_{N}q_{N-1}+q_{N-2} |  |

with initial values q − 1 = 0 q_{-1}=0, q 0 = 1 q_{0}=1. Denoting the matrix M c:= ( c 1 1 0) M_{c}:=\bigl(\begin{smallmatrix}c&1\\ 1&0\end{smallmatrix}\bigr), then the recurrence can be rewritten as

 | ( q N, q N − 1) = ( q N − 1, q N − 2) ​ M b N, (q_{N},q_{N-1})=(q_{N-1},q_{N-2})M_{b_{N}}\,, |  |

and by repetition, we obtain

 | ( q N, q N − 1) = ( 1, 0) M b 1 M b 2 ⋯ M b N (q_{N},q_{N-1})=(1,0)M_{b_{1}}M_{b_{2}}\cdots M_{b_{N}} |  |

In order to extract the component q N q_{N}, it suffices to multiply the latter from the right by the vector ( 1 0) \binom{1}{0}. We obtain

 | q N = ( 1, 0) M b 1 M b 2 ⋯ M b N ( 1 0) = ( 1, 0) M b N ⋯ M b 2 M b 1 ( 1 0), q_{N}=(1,0)M_{b_{1}}M_{b_{2}}\cdots M_{b_{N}}\textstyle{\binom{1}{0}}=(1,0)M_{b_{N}}\cdots M_{b_{2}}M_{b_{1}}\textstyle{\binom{1}{0}}\,, |  | (9) |

where we have used that equality must hold also for the transpose q N T = q N q_{N}^{T}=q_{N} and M c T = M c M_{c}^{T}=M_{c} for all c ∈ ℕ c\in\mathbb{N}.

For the derivation of the lower bound on the index of Sturmian words we use an old result on recurrence function of Sturmian words given in [18].

###### Theorem 4.1 ( [18]).

Let u u be a Sturmian word with slope α \alpha. Denote by q 0, q 1, q 2, … q_{0},q_{1},q_{2},\dots the denominators of the convergents of α \alpha. Then for every n ∈ ℕ n\in\mathbb{N},

 | R ⁡ ( n) = q N + 1 + q N + n − 1, where N is such that ​ q N ≤ n < q N + 1. R(n)=q_{N+1}+q_{N}+n-1\,,\qquad\hbox{where $N$ is such that }\ q_{N}\leq n<q_{N+1}\,. |  |

Substituting into Proposition 3.3, one obtains an easy proof of the following result. Similar derivation one can find in [7].

###### Corollary 4.2.

Index of every factor of a Sturmian word u u with the slope α = [0, 1, a 2, a 3, …] \alpha=[0,1,a_{2},a_{3},\dots] is bounded by

 | sup { 2 + a N + 1 + q N − 1 − 2 q N | N ≥ 1 }, \sup\Big\{\,2+a_{N+1}+\frac{q_{N-1}-2}{q_{N}}\;\Big|\;N\geq 1\,\Big\}\,, |  |

where q N q_{N} are the denominators of the convergents of α \alpha.

###### Proof.

Obviously, it suffices to consider only factors w w satisfying assumptions of Theorem 3.3. Let | w | = n |w|=n and let q N ≤ n < q N + 1 q_{N}\leq n<q_{N+1}. Using Proposition 3.3 and Theorem 4.1, we have

 | n ​ ind ​ ( w) + 1 = R ⁡ ( n) = q N + 1 + q N + n − 1. n\,{\rm ind}(w)+1\ =\ R(n)\ =\ q_{N+1}+q_{N}+n-1\,. |  |

Therefore

 | q N ​ ( ind ⁡ ( w) − 1) ≤ n ⁡ ( ind ⁡ ( w) − 1) = q N + 1 + q N − 2 = ( a N + 1 + 1) ​ q N + q N − 1 − 2, q_{N}\bigl({\rm ind}(w)-1\bigr)\ \leq\ n\bigl({\rm ind}(w)-1\bigr)\ =\ q_{N+1}+q_{N}-2\ =\ (a_{N+1}+1)q_{N}+q_{N-1}-2\,, |  |

and consequently

 | ind ⁡ ( w) ≤ 2 + a N + 1 + q N − 1 − 2 q N. {\rm ind}(w)\ \leq\ 2+a_{N+1}+\frac{q_{N-1}-2}{q_{N}}\,. |  |

∎

## 5 Sturmian morphisms and factors with maximal index

In this section we provide a lower bound on the index of a Sturmian word u u of slope α \alpha. Obviously, ind ⁡ ( u) ≥ a 2 + 1 {\rm ind}(u)\geq a_{2}+1, since ⌊ α 1 − α ⌋ \lfloor\frac{\alpha}{1-\alpha}\rfloor in the formula ( 3) for the index of the letter A A is equal to the coefficient a 2 a_{2} of the continued fraction of α \alpha. The idea for construction of factors with large index in a Sturmian word u u stems in application of specific Sturmian morphisms. Since application of a morphism preserves repetitions, it suffices to know how the chosen morphism changes the slope of the Sturmian word. Let us recall the necessary facts.

A morphism over the alphabet { A, B } \{A,B\} is a mapping φ: { A, B } ∗ ↦ { A, B } ∗ \varphi:\{A,B\}^{*}\mapsto\{A,B\}^{*} satisfying φ ⁡ ( w 1 ​ w 2) = φ ⁡ ( w 1) ​ φ ​ ( w 2) \varphi(w_{1}w_{2})=\varphi(w_{1})\varphi(w_{2}). Obviously, a morphism is uniquely determined by φ ⁡ ( A) \varphi(A), φ ⁡ ( B) \varphi(B). The incidence matrix of a morphism φ \varphi is given by

 | M φ = ( | φ ⁡ ( A) | A | φ ⁡ ( A) | B | φ ⁡ ( B) | A | φ ⁡ ( B) | B) M_{\varphi}=\Biggl(\!\begin{array}[]{cc}|\varphi(A)|_{A}&|\varphi(A)|_{B}\\ |\varphi(B)|_{A}&|\varphi(B)|_{B}\end{array}\!\Biggr) |  |

The action of a morphism can be naturally extended to infinite words by

 | φ ( u 0 u 1 u 2 ⋯) = φ ( u 0) φ ( u 1) φ ( u 2) ⋯ \varphi(u_{0}u_{1}u_{2}\cdots)=\varphi(u_{0})\varphi(u_{1})\varphi(u_{2})\cdots |  |

It is easy to show that for the number of letters in the image of a word w w, one has

 | ( | φ ⁡ ( w) | A, | φ ⁡ ( w) | B) = ( | w | A, | w | B) ​ M φ. \bigl(|\varphi(w)|_{A},|\varphi(w)|_{B}\bigr)=\bigl(|w|_{A},|w|_{B}\bigr)M_{\varphi}\,. |  | (10) |

From that, we can deduce the following fact for the densities of letters in an infinite word u u. If ϱ ⁡ ( A) \varrho(A), ϱ ⁡ ( B) \varrho(B) are the densities in u u, than the densities in the word u ′ = φ ⁡ ( u) u^{\prime}=\varphi(u) are ϱ ′ ​ ( A) \varrho^{\prime}(A), ϱ ′ ​ ( B) \varrho^{\prime}(B), where

 | ( ϱ ′ ​ ( A), ϱ ′ ​ ( B)) = 𝑐𝑜𝑛𝑠𝑡. ( ϱ ⁡ ( A), ϱ ⁡ ( B)) ​ M φ, \bigl(\varrho^{\prime}(A),\varrho^{\prime}(B)\bigr)={\it const.}\,\bigl(\varrho(A),\varrho(B)\bigr)M_{\varphi}\,, |  | (11) |

and 𝑐𝑜𝑛𝑠𝑡. {\it const.} is chosen so that ϱ ′ ​ ( A) + ϱ ′ ​ ( B) = 1 \varrho^{\prime}(A)+\varrho^{\prime}(B)=1.

A morphism φ \varphi is called Sturmian, if φ ⁡ ( u) \varphi(u) is a Sturmian word for every Sturmian word u u. Obviously, the set of Sturmian morphisms equipped with the operation of composition is a monoid, denoted by 𝑆𝑡 {\it St}. It is known [4] that the monoid 𝑆𝑡 {\it St} has three generators, namely

 | ψ 1: A ↦ A ​ B B ↦ B ψ 2: A ↦ B ​ A B ↦ B E: A ↦ B B ↦ A \psi_{1}:\begin{array}[]{rcl}A&\mapsto&AB\\ B&\mapsto&B\end{array}\qquad\psi_{2}:\begin{array}[]{rcl}A&\mapsto&BA\\ B&\mapsto&B\end{array}\qquad E:\begin{array}[]{rcl}A&\mapsto&B\\ B&\mapsto&A\end{array} |  | (12) |

Consider a Sturmian word with slope β ∈ ( 1 2, 1) \beta\in(\frac{1}{2},1) whose continued fraction is of the form β = [0, 1, b 2, b 3, …] \beta=[0,1,b_{2},b_{3},\dots]. For c ∈ ℕ c\in\mathbb{N}, we shall study the action of the morphism

 | φ: A ↦ A c ​ B B ↦ A \varphi:\begin{array}[]{rcl}A&\mapsto&A^{c}B\\ B&\mapsto&A\end{array} |  | (13) |

on the Sturmian word u u with slope β \beta. The morphism φ \varphi is a Sturmian morphism; it is a composition of the generators ( 12) of the Sturmian monoid, namely φ = E ​ ψ 2 c \varphi=E\psi_{2}^{c}. The corresponding incidence matrix is M φ = M c = ( c 1 1 0) M_{\varphi}=M_{c}=\bigl(\begin{smallmatrix}c&1\\ 1&0\end{smallmatrix}\bigr), as defined in the Preliminaries. Consequently, the infinite word φ ⁡ ( u) \varphi(u) is also Sturmian, i.e. there exists an irrational β ′ \beta^{\prime} such that u ′:= φ ⁡ ( u) u^{\prime}:=\varphi(u) is a Sturmian word with slope β ′ \beta^{\prime}. According to ( 11), the densities of letters a, b a,b in the word u ′ u^{\prime} satisfy

 | ( β ′, 1 − β ′) = 𝑐𝑜𝑛𝑠𝑡. ( β, 1 − β) ​ ( c 1 1 0). (\beta^{\prime},1-\beta^{\prime})\ =\ {\it const.}\ (\beta,1-\beta)\ \Bigl(\!\begin{array}[]{cc}c&1\\ 1&0\end{array}\!\Bigr)\,. |  |

Therefore β ′ = c ​ β + 1 − β c ​ β + 1 \beta^{\prime}=\frac{c\beta+1-\beta}{c\beta+1}. It is not difficult to show that the continued fraction of β ′ \beta^{\prime} is equal to

 | β ′ = [0, 1, c, b 2, b 3, …]. \beta^{\prime}=[0,1,c,b_{2},b_{3},\dots]\,. |  | (14) |

The following lemma is crucial for construction of factors of a Sturmian word with maximal index.

###### Lemma 5.1.

Let u u be a Sturmian word with slope β \beta having the continued fraction β = [0, 1, b 2, b 3, …] \beta=[0,1,b_{2},b_{3},\dots]. Let w ∈ Ł ⁡ ( u) w\in\L(u), and let r ∈ ℚ r\in\mathbb{Q}, r ≥ 2 r\geq 2 be such that v = w r ∈ Ł ⁡ ( u) v=w^{r}\in\L(u). Denote

 | w ′ = φ ⁡ ( w) and v ′ = φ ⁡ ( v) ​ A c, w^{\prime}=\varphi(w)\qquad\hbox{and}\qquad v^{\prime}=\varphi(v)A^{c}\,, |  |

where φ \varphi is the morphism given by ( 13). Then v ′ v^{\prime} is a rational power of w ′ w^{\prime} in a Sturmian word u ′ u^{\prime} with slope β ′ = [0, 1, c, b 2, b 3, …] \beta^{\prime}=[0,1,c,b_{2},b_{3},\dots].

###### Proof.

If | w | = 1 |w|=1, then necessarily w = A w=A, v = A r v=A^{r} for 2 < r ≤ b 2 + 1 2<r\leq b_{2}+1, φ ⁡ ( w) = A c ​ B \varphi(w)=A^{c}B, and φ ⁡ ( v) ​ A c = ( A c ​ B) r ​ A c \varphi(v)A^{c}=(A^{c}B)^{r}A^{c} is a factor of u ′ u^{\prime}, since a Sturmian word with slope β ′ = [0, 1, c, b 2, b 3, …] \beta^{\prime}=[0,1,c,b_{2},b_{3},\dots] has blocks A c A^{c}, A c + 1 A^{c+1} separated by single letters B B.

If | w | ≥ 2 |w|\geq 2, let us write w = w 1 ​ w 2 w=w_{1}w_{2} so that w 2 ≠ ϵ w_{2}\neq\epsilon and v = ( w 1 ​ w 2) ⌊ r ⌋ ​ w 1 v=(w_{1}w_{2})^{\lfloor r\rfloor}w_{1}. Then φ ⁡ ( v) ​ A c = φ ⁡ ( w ⌊ r ⌋) ​ φ ​ ( w 1) ​ A c \varphi(v)A^{c}=\varphi(w^{\lfloor r\rfloor})\varphi(w_{1})A^{c}. In order to show that φ ⁡ ( v) ​ A c \varphi(v)A^{c} is a power of φ ⁡ ( w) \varphi(w), it suffices to show that φ ⁡ ( w 1) ​ A c \varphi(w_{1})A^{c} is a prefix of φ ⁡ ( w) \varphi(w) or φ ⁡ ( w) ​ φ ​ ( w) \varphi(w)\varphi(w). If w 2 w_{2} starts with A A or B ​ A BA, then φ ⁡ ( w 2) \varphi(w_{2}) has prefix A c A^{c} and thus φ ⁡ ( w 1) ​ A c \varphi(w_{1})A^{c} is a prefix of φ ⁡ ( w) = φ ⁡ ( w 1) ​ φ ​ ( w 2) \varphi(w)=\varphi(w_{1})\varphi(w_{2}). Since B ​ B ∉ Ł ⁡ ( u) BB\notin\L(u), it remains to discuss the special case when w 2 = B w_{2}=B. As | w | ≥ 2 |w|\geq 2, we have w 1 ≠ ϵ w_{1}\neq\epsilon. Since w 2 ​ w 1 ∈ Ł ⁡ ( u) w_{2}w_{1}\in\L(u), the word w 1 w_{1} must start with the letter A A and therefore φ ⁡ ( w 1) ​ A c \varphi(w_{1})A^{c} is a prefix of φ ⁡ ( w 1 ​ B) ​ φ ​ ( w 1 ​ B) = ( φ ⁡ ( w)) 2 \varphi(w_{1}B)\varphi(w_{1}B)=\bigl(\varphi(w)\bigr)^{2}. ∎

###### Theorem 5.2.

Let u u be a Sturmian word with slope α = [0, 1, a 2, a 3, …] \alpha=[0,1,a_{2},a_{3},\dots]. Then for every N ∈ ℕ N\in\mathbb{N} there exists a factor w ∈ Ł ⁡ ( u) w\in\L(u) with index at least equal to 2 + a N + 1 + q N − 1 − 2 q N 2+a_{N+1}+\frac{q_{N-1}-2}{q_{N}}, where q N q_{N} is the denominator of the N N -th convergent of α \alpha.

###### Proof.

For N = 1 N=1 it follows from the continued fraction of α \alpha that q 1 = 1 q_{1}=1, q 0 = 1 q_{0}=1 and therefore we have to find a factor with index 2 + a 2 − 1 = a 2 + 1 2+a_{2}-1=a_{2}+1. It suffices to put w = A w=A. Therefore we consider N ≥ 2 N\geq 2. We shall construct the desired factor w w and its power v v by ( N − 1) (N-1) -fold application of Lemma 5.1. Consider the irrational number α 0 \alpha_{0} with the continued fraction α 0 = [0, 1, a N + 1, a N + 2, …] \alpha_{0}=[0,1,a_{N+1},a_{N+2,\dots}]. Take a Sturmian word u ( 0) u^{(0)} with slope α 0 {\alpha_{0}} and its factors w ( 0):= A w^{(0)}:=A, v ( 0):= A 1 + a N + 1 v^{(0)}:=A^{1+a_{N+1}} for initial values of the construction. For 1 ≤ i ≤ N − 1 1\leq i\leq N-1, define

 | w ( i):= φ i ( w ( i − 1)), v ( i):= φ i ( v ( i − 1)) A a N − i + 1, where φ i: A ↦ A a N − i + 1 ​ B B ↦ A. w^{(i)}:=\varphi_{i}(w^{(i-1)})\,,\qquad v^{(i)}:=\varphi_{i}(v^{(i-1)})A^{a_{N-i+1}}\,,\qquad\hbox{where}\quad\varphi_{i}:\begin{array}[]{rcl}A&\mapsto&A^{a_{N-i+1}}B\\ B&\mapsto&A\end{array}\,. |  |

By Lemma 5.1, the word w ( i) w^{(i)} is a factor of a Sturmian word u ( i) u^{(i)} with slope α i {\alpha_{i}}, where α i \alpha_{i} has the continued fraction α i = [0, 1, a N + 1 − i, a N + 2 − i, …] \alpha_{i}=[0,1,a_{N+1-i},a_{N+2-i},\dots] and v ( i) v^{(i)} is a power of w ( i) w^{(i)} in the word u ( i) u^{(i)}. In particular, w ( N − 1) w^{(N-1)} is a factor of a Sturmian word u u with slope α = [0, 1, a 2, a 3, …] \alpha=[0,1,a_{2},a_{3},\dots] and v ( N − 1) v^{(N-1)} is its power in u u.

It suffices now to show that the length of w ( N − 1) w^{(N-1)} is q N q_{N} and the length of v ( N − 1) v^{(N-1)} is ( 2 + a N + 1) ​ q N + q N − 1 − 2 (2+a_{N+1})q_{N}+q_{N-1}-2. For the recurrent expression of lengths of factors w ( i) w^{(i)}, v ( i) v^{(i)} we use formula ( 10). We have

 | ( | w ( i) | A, | w ( i) | B) = ( | w ( i − 1) | A, | w ( i − 1) | B) ​ M a N − i + 1, \bigl(|w^{(i)}|_{A},|w^{(i)}|_{B}\bigr)=\bigl(|w^{(i-1)}|_{A},|w^{(i-1)}|_{B}\bigr)M_{a_{N-i+1}}\,, |  |

for all i = 1, 2, …, N − 1 i=1,2,\dots,N-1, with ( | w ( 0) | A, | w ( 0) | B) = ( 1, 0) \bigl(|w^{(0)}|_{A},|w^{(0)}|_{B}\bigr)=(1,0). It can be easily seen that

 | ( | w ( N − 1) | A, | w ( N − 1) | B) = ( 1, 0) M a N M a N − 1 ⋯ M a 2. \bigl(|w^{(N-1)}|_{A},|w^{(N-1)}|_{B}\bigr)=(1,0)M_{a_{N}}M_{a_{N-1}}\cdots M_{a_{2}}\,. |  |

In order to obtain | w ( N − 1) | = | w ( N − 1) | A + | ​ w ( N − 1) | B |w^{(N-1)}|=|w^{(N-1)}|_{A}+|w^{(N-1)}|_{B}, we multiply the latter from the right by the vector ( 1 1) \binom{1}{1}, which can be also written as ( 1 1) = ( 1 1 1 0) ​ ( 1 0) \binom{1}{1}=\bigl(\begin{smallmatrix}1&1\\ 1&0\end{smallmatrix}\bigr)\binom{1}{0}. Since in the continued fraction of α \alpha we have a 1 = 1 a_{1}=1, we can use ( 9) to obtain

 | | w ( N − 1) | = ( 1, 0) M a N M a N − 1 ⋯ M a 2 M a 1 ( 1 0) = q N. |w^{(N-1)}|=(1,0)M_{a_{N}}M_{a_{N-1}}\cdots M_{a_{2}}M_{a_{1}}\textstyle{\binom{1}{0}}=q_{N}\,. |  |

From the definition of words v ( i) v^{(i)} we have for their lengths

 | ( | v ( i) | A, | v ( i) | B) = ( | v ( i − 1) | A, | v ( i − 1) | B) ​ M a N − i + 1 + ( a N − i + 1, 0), \bigl(|v^{(i)}|_{A},|v^{(i)}|_{B}\bigr)=\bigl(|v^{(i-1)}|_{A},|v^{(i-1)}|_{B}\bigr)M_{a_{N-i+1}}+(a_{N-i+1},0)\,, |  | (15) |

with ( | v ( 0) | A, | v ( 0) | B) = ( 1 + a N + 1, 0) \bigl(|v^{(0)}|_{A},|v^{(0)}|_{B}\bigr)=(1+a_{N+1},0). Let us compute the lengths for N = 1 N=1,

 | ( | v ( 1) | A, | v ( 1) | B) = ( 1 + a N + 1, 0) ​ ( a N 1 1 0) + ( a N, 0) = ( 2 + a N + 1) ​ ( 1, 0) ​ M a N + ( 1, 0) − ( 1, 1). \bigl(|v^{(1)}|_{A},|v^{(1)}|_{B}\bigr)=(1+a_{N+1},0)\bigl(\begin{smallmatrix}a_{N}&1\\ 1&0\end{smallmatrix}\bigr)+(a_{N},0)=(2+a_{N+1})(1,0)M_{a_{N}}+(1,0)-(1,1)\,. |  |

Since for every c c we have − ( 1, 1) ​ M c + ( c, 0) = − ( 1, 1) -(1,1)M_{c}+(c,0)=-(1,1), by repeated application of the recurrence ( 15) we obtain

 | ( | v ( N − 1) | A, | v ( N − 1) | B) = ( 2 + a N + 1) ( 1, 0) M a N M a N − 1 ⋯ M a 2 + ( 1, 0) M a N − 1 ⋯ M a 2 − ( 1, 1). \bigl(|v^{(N-1)}|_{A},|v^{(N-1)}|_{B}\bigr)=(2+a_{N+1})(1,0)M_{a_{N}}M_{a_{N-1}}\cdots M_{a_{2}}+(1,0)M_{a_{N-1}}\cdots M_{a_{2}}-(1,1)\,. |  |

Again, multiplying the latter from the right by the vector ( 1 1) = M a 1 ​ ( 1 0) \binom{1}{1}=M_{a_{1}}\binom{1}{0} and using ( 9), we obtain

 | | v ( N − 1) | = ( 2 + a N + 1) ​ q N + q N − 1 − 2. |v^{(N-1)}|=(2+a_{N+1})q_{N}+q_{N-1}-2\,. |  |

∎

## 6 Acknowledgements

We are grateful to J.-P. Allouche for pointing out the reference [7]. We also acknowledge financial support by the grants MSM6840770039 and LC06002 of the Ministry of Education, Youth, and Sports of the Czech Republic.

## References

- [1] B. Adamczewski and J.-P. Allouche, Reversals and palindromes in continued fractions, Theoret. Comput. Sci. 380 (2007), 220–237.
- [2] L. Balková, E. Pelantová, and W. Steiner, Sequences with constant number of return words, Monatsh. Math. (2008).
- [3] J. Berstel, On the index of Sturmian words, In ’ Jewels are forever ’, Springer (1999), 287–294.
- [4] J. Berstel and P. Séébold, Morphismes de Sturm, Bull. Belg. Math. Soc. Simon Stevin 1 (1994), 175–189.
- [5] V. Berthé, C. Holton, and L. Q. Zamboni, Initial powers of Sturmian sequences, Acta Arith. 122 (2006), 315–347.
- [6] W.-T. Cao and Z.-Y. Wen, Some properties of the factors of Sturmian sequences, Theoret. Comput. Sci. 304 (2003), 365–385.
- [7] A. Carpi and A. de Luca, Special factors, periodicity, and an application to Sturmian words, Acta Inform. 36 (2000), 983–1006.
- [8] D. Damanik, Singular continuous spectrum for a class of substitution Hamiltonians. II, Lett. Math. Phys. 54 (2000), 25–31.
- [9] D. Damanik and D. Lenz, The index of Sturmian sequences, European J. Combin. 23 (2002), 23–29.
- [10] X. Droubay and G. Pirillo, Palindromes and sturmian words, Theor. Comput. Sci. 223 (1999), 73–85.
- [11] F. Durand, A characterization of substitutive sequences using return words, Discrete Math. 179 (1998), 89–101.
- [12] J. Justin and G. Pirillo, Fractional powers in Sturmian words, Theoret. Comput. Sci. 255 (2001), 363–376.
- [13] J. Karhumäki, On cube-free ω \omega -words generated by binary morphisms, Discrete Appl. Math. 5 (1983), 279–297.
- [14] M. Lothaire, Algebraic combinatorics on words, volume 90 of Encyclopedia of Mathematics and its Applications, Cambridge University Press, Cambridge, (2002).
- [15] F. Mignosi and G. Pirillo, Repetitions in the Fibonacci infinite word, RAIRO Inform. Théor. Appl. 26 (1992), 199–204.
- [16] F. Mignosi, Infinite words with linear subword complexity, Theoret. Comput. Sci. 65 (1989), 221–242.
- [17] M. Morse and G. A. Hedlund, Symbolic Dynamics, Amer. J. Math. 60 (1938), 815–866.
- [18] M. Morse and G. A. Hedlund, Symbolic dynamics II. Sturmian trajectories, Amer. J. Math. 62 (1940), 1–42.
- [19] G. Richomme, Another characterization of Sturmian words (one more), Bull. Eur. Assoc. Theor. Comput. Sci. EATCS 67 (1999), 173–175.
- [20] D. Vandeth, Sturmian words and words with a critical exponent, Theoret. Comput. Sci. 242 (2000), 283–300.
- [21] L. Vuillon, A characterization of Sturmian words by return words, European J. Combin. 22 (2001), 263–275.

[◄][1][image: ar5iv homepage] [2]
[Feeling lucky?][3] [4]
[Conversion report][5]
[Report an issue][6]
[View original on arXiv][7] [►][8]


## Links

[1]: /html/0809.0602
[2]: /
[3]: /feeling_lucky
[4]: /land_of_honey_and_milk
[5]: /log/0809.0603
[6]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+0809.0603
[7]: https://arxiv.org/pdf/0809.0603
[8]: /html/0809.0604
