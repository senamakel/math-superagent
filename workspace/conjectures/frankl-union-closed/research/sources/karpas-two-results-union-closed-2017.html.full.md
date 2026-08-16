<!-- source: https://ar5iv.labs.arxiv.org/html/1708.01434 | converted from HTML -->

[1708.01434] Two Results on Union-Closed Families

# Two Results on Union-Closed Families

Ilan Karpas Thanks: Department of Mathematics, Hebrew University of Jerusalem.
Email: ilan.karpas@mail.huji.ac.il

August 7, 2026

###### Abstract

We show that there is some absolute constant c > 0 c>0, such that for any union-closed family ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]}, if | ℱ | ≥ ( 1 2 − c) ​ 2 n |\mathcal{F}|\geq(\frac{1}{2}-c)2^{n}, then there is some element i ∈ [n] i\in[n] that appears in at least half of the sets of ℱ \mathcal{F}. We also show that for any union-closed family ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]}, the number of sets which are not in ℱ \mathcal{F} that cover a set in ℱ \mathcal{F} is at most 2 n − 1 2^{n-1}, and provide examples where the inequality is tight.

## 1 Introduction

The objects of study in this paper are union-closed families. A family
ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} is called union-closed, if for every two sets A, B ∈ ℱ A,B\in\mathcal{F}, A ∪ B ∈ ℱ A\cup B\in\mathcal{F}. There is a wide range of literature concerning various properties of union-closed families. For instance, Alekseev [1] approximated the number of union-closed families of subsets of [n] [n], Kleitman [12] gave an upper-bound for the number of basis sets for such families, and Reimer [22] found a tight lower-bound for the average size of a set inside a union-closed family containing m m sets.

However, if you stop a combinatorialist on the street, and ask him what is the best-known conjecture regarding union-closed sets, most probably he will respond ”Frankl’s conjecture”, or simply ”The union-closed set conjecture”. This conjecture was made by Peter Frankl in the late 1970 1970 ’s. The conjecture asserts that for every finite union-closed family which contains a non-empty set, there is some element that belongs to at least half of its members. Formally, for a family ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} and i ∈ [n] i\in[n], we write ℱ i:= { A ∈ ℱ | i ∈ A } \mathcal{F}_{i}:=\{A\in\mathcal{F}|i\in A\}. If | ℱ i | | ℱ | ≥ 1 2 \frac{|\mathcal{F}_{i}|}{|\mathcal{F}|}\geq\frac{1}{2} we say that i i is abundant in ℱ \mathcal{F}. If, on the otherhand, | ℱ i | | ℱ | ≤ 1 2 \frac{|\mathcal{F}_{i}|}{|\mathcal{F}|}\leq\frac{1}{2} we say that i i is rare in ℱ \mathcal{F}. Frankl’s conjecture can be stated as follows:

###### Conjecture 1.1.

Let ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} be a union-closed family, ℱ ≠ { ∅ } \mathcal{F}\neq\{\emptyset\}. Then there is some element i ∈ [n] i\in[n] that is abundant in ℱ \mathcal{F}.

There have been various partial results regarding the conjecture. Let us first recommend the survey paper of Bruhn and Schaudt [4] for details. Vučković and Živkoić [25] showed that the conjecture is shown to be true for any union-closed family ℱ \mathcal{F} with a universe of at most 12 12 elements, improving on results in [3, 17, 18, 9, 21]. Lo Faro [15], and later independently Roberts and Simpson [23], showed that if ℱ \mathcal{F} is a counterexample to the conjecture, and the universe of ℱ \mathcal{F} is of size q q, then | ℱ | ≥ 4 ​ q − 1 |\mathcal{F}|\geq 4q-1. Falgas-Ravry [7] showed that the conjecture holds for any separating union-closed family ℱ \mathcal{F} with a universe of n n elements with at most 2 ​ n 2n elements (separating here means that no two distinct elements i, j ∈ [n] i,j\in[n] appear in exactly the same sets in ℱ \mathcal{F}). This was slightly improved by Maßberg [16], from 2 ​ n 2n to 2 ​ ( n + n log 2 ⁡ n − log ⁡ log 2 ⁡ n) 2(n+\frac{n}{\log_{2}n-\log\log_{2}n}). Interestingly, Hu [10] proved that if this bound can be improved to ( 2 + c) ​ n (2+c)n for some constant c > 0 c>0, this already implies that any union-closed family ℱ \mathcal{F} has an element appearing in at least c − 2 2 ​ ( c − 1) ​ | ℱ | \frac{c-2}{2(c-1)}|\mathcal{F}| sets in ℱ \mathcal{F}. At the moment, all that is known is that each union-closed family ℱ \mathcal{F} has an element occuring in at least Ω ⁡ ( | ℱ | log 2 ⁡ | ℱ |) \Omega(\frac{|\mathcal{F}|}{\log_{2}|\mathcal{F}|}) sets in ℱ \mathcal{F} [13, 24]. A Polymath project was dedicated to try to prove the conjecture, but without success (so far) [20].

Of more relevance to this paper, are results proving that the conjecture holds for union-closed families ℱ \mathcal{F} with many sets, compared to the size of the universe. Czédli [5] proved that for any union-closed family ℱ ⊂ 2 [n] \mathcal{F}\subset 2^{[n]}, where | ℱ | ≥ 2 n − 2 n / 2 |\mathcal{F}|\geq 2^{n}-2^{n/2}, the conjecture holds. This was significantly improved by Balla, Bóllobas and Eccles [2] to all union-closed families of subsets of [n] [n] of size at least 2 3 ​ 2 n \frac{2}{3}2^{n}, and then further improved by Eccles [6] to ( 2 3 − 1 104) ​ 2 n (\frac{2}{3}-\frac{1}{104})2^{n}. Our first theorem, is that the bound can be improved to 1 2 ​ 2 n \frac{1}{2}2^{n}:

###### Theorem 1.2.

Let ℱ ⊂ 2 [n] \mathcal{F}\subset 2^{[n]} be a union-closed family, where | ℱ | ≥ 2 n − 1 |\mathcal{F}|\geq 2^{n-1}. Then there is some element i ∈ [n] i\in[n], so that | ℱ i | ≥ 1 2 ​ | ℱ | |\mathcal{F}_{i}|\geq\frac{1}{2}|\mathcal{F}|.

We use basic Boolean-Analysis techniques to prove this result. To the best of our knowledge, Boolean-Analysis has not been used before to tackle Frankl’s conjecture.

The second main theorem of this paper, regards the maximum number of sets in the upper-shadow of a union-closed family, which are not in the family itself.

For a subset A ⊆ [n] A\subseteq[n], The upper-shadow of A A with respect to n n, denoted as ∂ + A \partial^{+}A, is the following:

 | ∂ + A = { A ∪ { i } | i ∈ [n] ∖ A } \partial^{+}A=\{A\cup\{i\}|i\in[n]\setminus A\} |  |

.

For a family of sets ℱ ⊂ 2 [n] \mathcal{F}\subset 2^{[n]}, the upper-shadow of the family is just the union of the upper-shadow of all sets in ℱ \mathcal{F}:

 | ∂ + ℱ = ⋃ A ∈ ℱ ∂ + A \partial^{+}\mathcal{F}=\bigcup_{A\in\mathcal{F}}\partial^{+}A |  |

.

We show that the upper shadow of a union-closed family can not be too large:

###### Theorem 1.3.

Let ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} be a union-closed family. Then

 | | ∂ + ℱ ∖ ℱ | ≤ 2 n − 1. |\partial^{+}\mathcal{F}\setminus\mathcal{F}|\leq 2^{n-1}. |  |

Note that this is tight, for instance by considering the family ℱ = { A ⊆ [n] | 1 ∉ A } \mathcal{F}=\{A\subseteq[n]|1\notin A\}.

Lastly, we use Theorem 1.3, combined with more advanced Boolean-Analysis results, to improve slightly on Theorem 1.2. We show:

###### Theorem 1.4.

Let ℱ ⊂ 2 [n] \mathcal{F}\subset 2^{[n]} be a union-closed family, where | ℱ | ≥ ( 1 2 − c) ​ 2 n |\mathcal{F}|\geq(\frac{1}{2}-c)2^{n}. Then there is some element i ∈ [n] i\in[n], so that | ℱ i | ≥ 1 2 ​ | ℱ | |\mathcal{F}_{i}|\geq\frac{1}{2}|\mathcal{F}|.

Although Theorem 1.2 is, of course, an immediate consequence of Theorem 1.4, nevertheless we have decided to include the proof of the former, both because the proof is simpler and because its proof can be extended naturally to a more general setting than union-closed families (see section 3 3 for details).

The structure of the paper is as follows:

in section 2 2, we provide the necessary definitions and tools from Boolean-Analysis, and prove some basic properties of union-closed families. In section 3 3 we prove Theorem 1.2, and in section 4 4 we prove Theorem 1.3. In section 5 5 we prove Theorem 1.4, and finally, in section 6 6, we discuss some implications and open problems stemming from this paper’s results.

## 2 Preliminaries

### 2.1 Boolean Analysis

In most of this subsection we provide basic definitons and facts from Boolean-Analysis. Towards the end we cite two non-trivial theorems in Boolean-Analysis.

We identify subsets of [n] [n] with boolean strings of length n n, by associating with each S ⊆ [n] S\subseteq[n] the string x S = x 1 S ​ … ​ x n S ∈ { 0, 1 } n x^{S}=x^{S}_{1}\dots x^{S}_{n}\in\{0,1\}^{n}, where x i S = 1 x^{S}_{i}=1 iff i ∈ S i\in S.

We define an inner product on boolean vectors ⟨.,. ⟩: { 0, 1 } n × { 0, 1 } n → ℤ \langle.,.\rangle:\{0,1\}^{n}\times\{0,1\}^{n}\to\mathbb{Z}. For x = x 1 ​ … ​ x n x=x_{1}\dots x_{n}, y = y 1 ​ … ​ y n y=y_{1}\dots y_{n}, their inner product is

 | ⟨ x, y ⟩ = ∑ i = 1 n x i ​ y i. \langle x,y\rangle=\sum_{i=1}^{n}x_{i}y_{i}. |  |

The space of boolean functions itself also has an inner product. For functions f, g: { 0, 1 } n → { − 1, 1 } f,g:\{0,1\}^{n}\to\{-1,1\}, their inner product is taken to be:

 | ⟨ f, g ⟩ = 𝔼 x ∼ { 0, 1 } n ​ f ​ ( x) ​ g ​ ( x). \langle f,g\rangle=\mathbb{E}_{x\sim\{0,1\}^{n}}f(x)g(x). |  |

Notice that this number is always between − 1 -1 and 1 1. The distance between f f and g g is then defined as

 | d ​ i ​ s ​ t ​ ( f, g) = 1 2 ​ ( 1 − ⟨ f, g ⟩). dist(f,g)=\frac{1}{2}(1-\langle f,g\rangle). |  |

The distance between two classes of boolean functions on n n -coordinates 𝒜 \mathcal{A} and ℬ \mathcal{B} is the minimal distance between a function in 𝒜 \mathcal{A} and a function in ℬ \mathcal{B}.

A special role is played by the so called character functions. For every S ⊆ [n] S\subseteq[n] there exists a unique character function of S S, χ S: { 0, 1 } n → { − 1, 1 } \chi_{S}:\{0,1\}^{n}\to\{-1,1\}, which is defined thus:

 | χ S ​ ( x) = ( − 1) ⟨ x, x S ⟩. \chi_{S}(x)=(-1)^{\langle x,x_{S}\rangle}. |  |

In the special case that | S | = 1 |S|=1, the function χ S ​ ( x) \chi_{S}(x) is known as a dictator. Similarly, in this case, − χ S ​ ( x) -\chi_{S}(x) is called an anti-dictator. The set of all character functions is an orthonormal basis (with the inner product we have defined) for the space of boolean functions f: { 0, 1 } n → { − 1, 1 } f:\{0,1\}^{n}\to\{-1,1\}. For a boolean function f f, we define its fourier coefficient for S ⊆ [n] S\subseteq[n] to be

 | f ^ ​ ( S) = ⟨ f, χ s ⟩. \hat{f}(S)=\langle f,\chi_{s}\rangle. |  |

Notice that this is the coefficient of χ s \chi_{s} in the unique representation of f f as a linear combination of the characters. We call all fourier-coefficients of sets of size k k the level k k coefficients of f f. The sum of squares of all level k k coefficients of f f is called the level- k k weight of f f, and is denoted as

 | W k ​ ( f):= ∑ | S | = k f ^ ​ ( S) 2. W^{k}(f):=\sum_{|S|=k}\hat{f}(S)^{2}. |  |

At the heart of boolean analysis lays the following identity, known as Parseval’s identity:

###### Lemma 2.1.

For any f: { 0, 1 } n → { − 1, 1 } f:\{0,1\}^{n}\to\{-1,1\}

 | ∑ k = 0 n W k ​ ( f) = 1 \sum_{k=0}^{n}W^{k}(f)=1 |  | (1) |

For any coordinate i i, we define the i i th positive (negative) influence, I i + ​ ( f) I_{i}^{+}(f) thus:

 |  | I i + ​ ( f) = ℙ S ∼ [n] ∖ { i } ​ ( f ⁡ ( x S) = − 1 ∧ f ⁡ ( x S ∪ { i }) = 1) \displaystyle I_{i}^{+}(f)=\mathbb{P}_{S\sim[n]\setminus\{i\}}(f(x^{S})=-1\wedge f(x^{S\cup\{i\}})=1) |  |

 | ( \displaystyle( | OPEN I i − ​ ( f) = ℙ S ∼ [n] ∖ { i } ​ ( f ⁡ ( x S) = 1 ∧ f ⁡ ( x S ∪ { i }) = − 1)) \displaystyle I_{i}^{-}(f)=\mathbb{P}_{S\sim[n]\setminus\{i\}}(f(x^{S})=1\wedge f(x^{S\cup\{i\}})=-1)) |  |

In other words, if we partition { 0, 1 } n \{0,1\}^{n} to 2 n − 1 2^{n-1} pairs of the form ( x, x ⊕ e i) (x,x\oplus e_{i}) where x i = 0 x_{i}=0, then the i i th positive (negative) influence is the fraction of all such pairs for which f ⁡ ( x) = 1 f(x)=1 and f ⁡ ( x ⊕ e i) = − 1 f(x\oplus e_{i})=-1 ( f ⁡ ( x) = − 1 f(x)=-1 and f ⁡ ( x ⊕ e i) = 1 f(x\oplus e_{i})=1). We then define the i i th influence, I i ​ ( f) I_{i}(f), to be the sum of these two:

 | I i ​ ( f) = I i − ​ ( f) + I i − ​ ( f). I_{i}(f)=I_{i}^{-}(f)+I_{i}^{-}(f). |  |

The positive (negative) influence of f f is:

 | I + ​ ( f) = ∑ i = 1 n I i + ​ ( f) ( I − ​ ( f) = ∑ i = 1 n I i − ​ ( f)), I^{+}(f)=\sum_{i=1}^{n}I_{i}^{+}(f)\quad(I^{-}(f)=\sum_{i=1}^{n}I_{i}^{-}(f)), |  |

and the influence of f f is simply the sum of the positive and the negative influences:

 | I ⁡ ( f) = I + ​ ( f) + I − ​ ( f). I(f)=I^{+}(f)+I^{-}(f). |  |

The reader new to the subject might want to get some feel for the definitions, by proving to himself the following observation:

###### Observation 2.2.

Let f: { 0, 1 } n → { − 1, 1 } f:\{0,1\}^{n}\to\{-1,1\} be a boolean function. Then:

1. 1.

f ^ ​ ( ∅) = 1 − 2 1 − n ​ | f − 1 ​ ( − 1) | \hat{f}(\emptyset)=1-2^{1-n}|f^{-1}(-1)|.

2. 2.

For every i ∈ [n] i\in[n], f ^ ​ ( i) = I i + ​ ( f) − I i − ​ ( f) \hat{f}(i)=I_{i}^{+}(f)-I_{i}^{-}(f).

The influence of a function f f has a nice analytic expression, whose proof can be found in any standard introduction to the subject (see, e.g., [19]).

 | I ⁡ ( f) = ∑ i = 0 n W i. I(f)=\sum_{i=0}^{n}W^{i}. |  | (2) |

In this paper, what we shall actually use later on is an analytic expression that provides a lower bound for the influence:

###### Corollary 2.3.

For any f: { 0, 1 } n → { − 1, 1 } f:\{0,1\}^{n}\to\{-1,1\}, and any k ∈ [n] k\in[n]:

 | I ⁡ ( f) ≥ k − ∑ i = 0 k − 1 ( k − i) ​ W i ​ ( f) I(f)\geq k-\sum_{i=0}^{k-1}(k-i)W^{i}(f) |  |

.

###### Proof.

 | I ⁡ ( f) = \displaystyle I(f)={} | ∑ i = 0 n i ​ W i ​ ( f) ≥ ∑ i = 0 k − 1 W i ​ ( f) + ∑ i = k n k ​ W i ​ ( f) = \displaystyle\sum_{i=0}^{n}iW^{i}(f)\geq\sum_{i=0}^{k-1}W^{i}(f)+\sum_{i=k}^{n}kW^{i}(f)= |  | (3) |

 |  | = k ​ ∑ i = 0 n W i ​ ( f) − ∑ i = 0 k − 1 ( k − i) ​ W i ​ ( f) = k − ∑ i = 0 k − 1 ( k − i) ​ W i ​ ( f) \displaystyle=k\sum_{i=0}^{n}W^{i}(f)-\sum_{i=0}^{k-1}(k-i)W^{i}(f)=k-\sum_{i=0}^{k-1}(k-i)W^{i}(f) |  |

where the last equality uses Parseval’s identity. ∎

We end this subsection by stating two important theorems in this subject. The first one is a famous result by Freidgut, Kalai and Naor [8], known in the field as FKN theorem. The theorem states that if a boolean function has almost all of its weight on level- 1 1, then this function is close (distance here being as we have defined above) to some dictator or anti-dictator:

###### Theorem 2.4.

(FKN) [8] There is some absolute constant C 1 C_{1}, so that the following holds. For any boolean function f: { 0, 1 } n → { − 1, 1 } f:\{0,1\}^{n}\to\{-1,1\}, if W 1 ​ ( f) ≥ 1 − δ W^{1}(f)\geq 1-\delta, then there is some i ∈ [n] i\in[n], for which either d ​ i ​ s ​ t ​ ( f, χ i) < C 1 ​ δ dist(f,\chi_{i})<C_{1}\delta or d ​ i ​ s ​ t ​ ( f, − χ i) < C 1 ​ δ dist(f,-\chi_{i})<C_{1}\delta.

Several years after this theorem was discovered, Kindler and Safra [11] managed to show an analog for higher (constant) weights. Specifically of interest to us is the level- 2 2 concentration case.

###### Theorem 2.5.

There is some absolute constant C 2 > 0 C_{2}>0, so that the following holds. For any n ∈ ℕ n\in\mathbb{N}, denote by 𝒜 n \mathcal{A}_{n} the class of all functions either of the form ± χ i, j \pm\chi_{i,j} for some distinct i, j ∈ [n] i,j\in[n], or of the form ± 1 2 ​ ( χ i, j + χ j, k + χ k, l − χ i, l) \pm\frac{1}{2}(\chi_{i,j}+\chi_{j,k}+\chi_{k,l}-\chi_{i,l}), for some distinct i, j, k, l ∈ [n] i,j,k,l\in[n]. Let f: { 0, 1 } n → { − 1, 1 } f:\{0,1\}^{n}\to\{-1,1\} be a boolean function, so that W 2 ​ ( f) ≥ 1 − δ W^{2}(f)\geq 1-\delta. Then d ​ i ​ s ​ t ​ ( f, 𝒜 n) < C 2 ​ δ dist(f,\mathcal{A}_{n})<C_{2}\delta.

Notice that, in both theorems, all functions which are used to approximate f f are balanced function. That is, They have value − 1 -1 on exactly half of the points in { 0, 1 } n \{0,1\}^{n}, or equivalently, their zero-level fourier coefficient is 0 0.

### 2.2 Union-closed and Simply-rooted Families

###### Remark 2.6.

For a set A A and an element i ∈ A i\in A, we denote by [i, A] [i,A] the family of all sets containing element i i and contained in A A. We often, by abuse of notation, write i i when we in fact mean the singleton { i } \{i\}. The meaning should be clear from context.

Recall that a family 𝒢 ∈ 2 [n] \mathcal{G}\in 2^{[n]} is called union-closed, if for every two sets A, B ∈ 𝒢 A,B\in\mathcal{G} A ∪ B ∈ 𝒢 A\cup B\in\mathcal{G}. A family ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} is called simply-rooted, if for every A ∈ ℱ A\in\mathcal{F}, there is some i ∈ A i\in A, so that [i, A] ⊆ ℱ [i,A]\subseteq\mathcal{F}. We say in this case that A A is rooted in i i.

###### Lemma 2.7.

𝒢 \mathcal{G} is union-closed iff ℱ:= 2 [n] ∖ 𝒢 \mathcal{F}:=2^{[n]}\setminus\mathcal{G} is simply-rooted.

###### Proof.

Assume 𝒢 \mathcal{G} is union-closed, and assume by contradiction ℱ \mathcal{F} is not simply-rooted. That is, there exists some A ∈ ℱ A\in\mathcal{F} with the following property. For every i ∈ A i\in A there is some set A i ∈ 𝒢 A_{i}\in\mathcal{G}, where i ∈ A i ⊆ A i\in A_{i}\subseteq A. Notice that ⋃ i ∈ A A i = A \bigcup_{i\in A}A_{i}=A by definition, but since 𝒢 \mathcal{G} is union-closed, also ⋃ i ∈ A A i ∈ 𝒢 \bigcup_{i\in A}A_{i}\in\mathcal{G}. This means that A ∈ 𝒢 A\in\mathcal{G}, which is a contradiction.

For the other direction, assume that ℱ \mathcal{F} is simply-rooted, and assume by contradiction 𝒢 \mathcal{G} is not union-closed. So there are two sets A, B ∈ 𝒢 A,B\in\mathcal{G}, with A ∪ B ∈ ℱ A\cup B\in\mathcal{F}. This means that there is some i ∈ A ∪ B i\in A\cup B with [i, A ∪ B] ⊆ ℱ [i,A\cup B]\subseteq\mathcal{F}, so i i is in A A or in B B. Assume without loss of generality that i ∈ A i\in A. Then A ∈ [i, A ∪ B] ⊆ ℱ A\in[i,A\cup B]\subseteq\mathcal{F}. But this is a contradiction, since we took A ∈ 𝒢 A\in\mathcal{G}. ∎

We have defined in the introduction the upper shadow of a set. We define, in similar manner, the lower shadow. Let A ⊆ [n] A\subseteq[n]. Then the lower shadow of A, denoted by ∂ − A \partial^{-}A, is defined as follows:

 | ∂ − A = { A ∖ i | i ∈ A }. \partial^{-}A=\{A\setminus i|i\in A\}. |  |

For a family of sets ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]}, the lower shadow of ℱ \mathcal{F} is simply the union of the lower shadow of all sets inside ℱ \mathcal{F}:

 | ∂ − ℱ = ⋃ A ∈ ℱ ∂ − A. \partial^{-}\mathcal{F}=\bigcup_{A\in\mathcal{F}}\partial^{-}A. |  |

With this definition at hand, we prove:

###### Lemma 2.8.

Let ℱ \mathcal{F} be a simply-rooted family. Then for every A ∈ ℱ A\in\mathcal{F},

 | ∂ − A ∖ ℱ = { { A ∖ i }, if A is rooted in i and in no other element. ∅, otherwise. } \partial^{-}A\setminus\mathcal{F}=\left\{\begin{array}[]{lr}\{A\setminus{i}\},&\text{if $A$ is rooted in $i$ and in no other element.}\\ \emptyset,\text{otherwise.}\end{array}\right\} |  |

###### Proof.

Let A ∈ ℱ A\in\mathcal{F}, with A A rooted in element i i. Then [i, A] ⊆ ℱ [i,A]\subseteq\mathcal{F}, which means that for every j ∈ A j\in A with j ≠ i j\neq i, A ∖ j ∈ [i, A] A\setminus j\in[i,A], and thus A ∖ j ∈ ℱ A\setminus j\in\mathcal{F}. If A A is rooted in another element j j, then by the same token A ∖ i ∈ [j, A] ⊆ ℱ A\setminus i\in[j,A]\subseteq\mathcal{F}. So in this case ∂ − A ∖ ℱ = ∅ \partial^{-}A\setminus\mathcal{F}=\emptyset.

If, on the other hand, A A is rooted only in element i i, then for every element j ∈ A ∖ i j\in A\setminus i, there is some set A j ∈ 𝒢 A_{j}\in\mathcal{G}, satisfying j ∈ A j ⊆ A ∖ i j\in A_{j}\subseteq A\setminus i. Taking the union of them, and recalling that 𝒢 \mathcal{G} is union-closed, we obtain A ∖ i = ⋃ j ∈ A ∖ i A j ∈ 𝒢 A\setminus i=\bigcup_{j\in A\setminus i}A_{j}\in\mathcal{G}, proving the lemma. ∎

## 3 Frankl’s conjecture for large families

Due to Lemma 2.7, Theorem 1.2 can be stated in terms of simply-rooted families, rather than union-closed sets. The key observation here, is that every element i ∈ [n] i\in[n] appears in exactly half the sets in 2 [n] 2^{[n]}. Thus, an element i ∈ [n] i\in[n] is abundant in family ℱ \mathcal{F} iff it is rare in 2 [n] ∖ ℱ 2^{[n]}\setminus\mathcal{F}:

###### Theorem.

1.2 *Let ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} be simply-rooted, | ℱ | ≤ 2 n − 1 |\mathcal{F}|\leq 2^{n-1}. Then there is some element i ∈ [n] i\in[n] such that i i is rare in ℱ \mathcal{F}.

###### Proof.

Let ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} be a simply-rooted family of size | ℱ | = ( 1 2 − δ) ​ 2 n |\mathcal{F}|=(\frac{1}{2}-\delta)2^{n}, where δ ≥ 0 \delta\geq 0. Assume by contradiction that | ℱ i | > 1 2 ​ | ℱ | |\mathcal{F}_{i}|>\frac{1}{2}|\mathcal{F}| for every i ∈ [n] i\in[n]. Identify ℱ \mathcal{F} with a function f: { 0, 1 } n → { − 1, 1 } f:\{0,1\}^{n}\to\{-1,1\} as in section 2.1 2.1. Our goal is to find both a lower and an upper bound for the positive influence I + ​ ( f) I^{+}(f), and then show that the lower bound is in fact larger than the upper bound. This is of course impossible.

For the upper bound, observe that, by Lemma 2.8, for any x ∈ { 0, 1 } n x\in\{0,1\}^{n} such that f ⁡ ( x) = − 1 f(x)=-1, there is at most one i ∈ [n] i\in[n] for which x i = 1 x_{i}=1 and f ⁡ ( x ⊕ e i) = 1 f(x\oplus e_{i})=1. Thus, each such x x contributes at most 2 1 − n 2^{1-n} to the positive influence. Since | f − 1 ​ ( − 1) | = ( 1 2 − δ) ​ 2 n |f^{-1}(-1)|=(\frac{1}{2}-\delta)2^{n}, we deduce the upper bound:

 | I + ​ ( f) ≤ 1 − 2 ​ δ. I^{+}(f)\leq 1-2\delta. |  | (4) |

What about the lower bound?

By Lemma 2.2, we have:

 | f ^ ​ ( ∅) = 1 − 2 ​ ( 1 2 − δ) = 2 ​ δ. \hat{f}(\emptyset)=1-2(\frac{1}{2}-\delta)=2\delta. |  | (5) |

Furthermore, for any i ∈ [n] i\in[n]:

 | f ^ ​ ( i) = I i + ​ ( f) − I i − ​ ( f) > 0. \hat{f}(i)=I_{i}^{+}(f)-I_{i}^{-}(f)>0. |  | (6) |

Indeed, ( 6) is equivalent to our assumption that | ℱ i | > 1 2 ​ | ℱ | |\mathcal{F}_{i}|>\frac{1}{2}|\mathcal{F}| for every i ∈ [n] i\in[n].

Because all level 1 1 fourier coefficients are strictly between 0 0 and 1 1, then f ^ ​ ( i) > f ^ ​ ( i) 2 \hat{f}(i)>\hat{f}(i)^{2} for all i ∈ [n] i\in[n]. Summing over all i i ’s, we obtain:

 | I + ​ ( f) − I − ​ ( f) = ∑ i = 1 n f ^ ​ ( i) > ∑ i = 1 n f ^ ​ ( i) 2. I^{+}(f)-I^{-}(f)=\sum_{i=1}^{n}\hat{f}(i)>\sum_{i=1}^{n}\hat{f}(i)^{2}. |  |

Plugging the latter inequality to the one stated in Corollary 2.3, for k = 2 k=2, gives:

 | I + ​ ( f) + I − ​ ( f) ≥ 2 − ∑ i = 1 n f ^ ​ ( i) 2 − 2 ​ f ^ ​ ( ∅) 2 > 2 − ( I + ​ ( f) − I − ​ ( f)) − 8 ​ δ 2, I^{+}(f)+I^{-}(f)\geq 2-\sum_{i=1}^{n}\hat{f}(i)^{2}-2\hat{f}(\emptyset)^{2}>2-(I^{+}(f)-I^{-}(f))-8\delta^{2}, |  |

or

 | I + ​ ( f) > 1 − 4 ​ δ 2 I^{+}(f)>1-4\delta^{2} |  | (7) |

Finally, by combining ( 4) and ( 7), we see that

 | δ > 1 2, \delta>\frac{1}{2}, |  |

but this is absurd, since | ℱ | = ( 1 2 − δ) ​ 2 n |\mathcal{F}|=(\frac{1}{2}-\delta)2^{n} can not be a negative number, and the theorem is proved. ∎

###### Remark 3.1.

Notice that the above theorem also holds if instead of demanding that ℱ \mathcal{F} is simply-rooted, we make the weaker demand that every set in ℱ \mathcal{F} covers at most one set that is not in ℱ \mathcal{F}. Indeed, this is the only property of simply-rooted families used in the proof.

## 4 Upper Shadow of Union-closed families

Let 𝒢 ⊆ 2 [n] \mathcal{G}\subseteq 2^{[n]} be a union-closed family, and let ℱ:= 2 [n] ∖ 𝒢 \mathcal{F}:=2^{[n]}\setminus\mathcal{G}. By Lemma 2.7, ℱ \mathcal{F} is a simply-rooted family. By definiton of the upper-shadow, for any set A A, A ∈ ∂ + 𝒢 ∖ 𝒢 A\in\partial^{+}\mathcal{G}\setminus\mathcal{G} iff A ∈ ℱ A\in\mathcal{F}, and there exists some i ∈ A i\in A such that A ∖ i ∈ 𝒢 A\setminus i\in\mathcal{G}. However, from Lemma 2.8, this happens exactly when A ∈ ℱ A\in\mathcal{F} and is rooted in exactly one element. So Theorem 1.3 can be equivalently stated like so:

###### Theorem.

1.3 * Let ℱ \mathcal{F} be a simply-rooted family of subsets of [n] [n]. Then there are at most 2 n − 1 2^{n-1} sets in ℱ \mathcal{F} that are rooted in only one element.

###### Proof.

We identify 2 [n] 2^{[n]} with the set of vertices of the n n -dimensional Hamming cube, V ⁡ ( Q n) V(Q_{n}) in the obvious manner. We do this, since we shall use the following theorem of Kotlov from 2000 2000:

###### Theorem 4.1.

(Kotlov, 2000 2000) [14] Denote by Q n Q_{n} the n n -dimensional Hamming cube, and let V V be a subset of the vertices, so that | V | > 2 n − 1 |V|>2^{n-1}. Then in the induced subgraph Q n ​ [V] Q_{n}[V], there is a connected component G G containing edges in all n n directions.

Let, then, ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} be a simply-rooted family, and let ℱ ′ ⊆ ℱ \mathcal{F^{\prime}}\subseteq\mathcal{F} be the family of all sets in ℱ \mathcal{F} rooted in exactly one element. Partition ℱ ′ \mathcal{F}^{\prime} to families ℱ i ′:= { A ∈ ℱ ′ | A ​ is rooted in ​ i } \mathcal{F}^{\prime}_{i}:=\{A\in\mathcal{F^{\prime}}|A\text{ is rooted in }i\}, for 1 ≤ i ≤ n 1\leq i\leq n. We claim that for A ∈ ℱ i ′ A\in\mathcal{F}^{\prime}_{i}, B ∈ ℱ j ′ B\in\mathcal{F}^{\prime}_{j} with distinct i i and j j, there can not be an edge (in the hamming cube) between A A and B B. Indeed, assume there is such an edge. That is, B = A ∖ k B=A\setminus k for some k ∈ A k\in A. But notice that by our choice of A A and B B, A ∖ i, B ∖ j ∈ 𝒢 A\setminus i,B\setminus j\in\mathcal{G}. That is, B ∖ { i, k }, B ∖ j ∈ 𝒢 B\setminus\{i,k\},B\setminus j\in\mathcal{G}. Hence, B = ( B ∖ { i, k }) ∪ B ∖ j ∈ 𝒢 B=(B\setminus\{i,k\})\cup B\setminus j\in\mathcal{G}, a contradiction.

Consequentially, every connected component in Q n ​ [ℱ ′] Q_{n}[\mathcal{F}^{\prime}] lies entirely, for some i ∈ [n] i\in[n], in Q n ​ [ℱ i ′] Q_{n}[\mathcal{F}^{\prime}_{i}]. Finally, assume by contradiction that | ℱ ′ |\mathcal{F}^{\prime} | > 2 n − 1 |>2^{n-1}. By Theorem 4.1, this means that Q n ​ [ℱ ′] Q_{n}[\mathcal{F}^{\prime}] has a connected component with edges in all n n directions, and by the previous paragraph, this connected component lies entirely in Q n ​ [ℱ i ′] Q_{n}[\mathcal{F}^{\prime}_{i}] for some i ∈ [n] i\in[n]. But this is impossible, since Q n ​ [ℱ i ′] Q_{n}[\mathcal{F}^{\prime}_{i}] can not contain edges in the i i th-direction. Indeed, for every A ∈ ℱ i ′ A\in\mathcal{F}^{\prime}_{i}, i ∈ A i\in A. Thus, | ℱ ′ | ≤ 2 n − 1 |\mathcal{F}^{\prime}|\leq 2^{n-1}, proving the theorem. ∎

## 5 Frankl’s conjecture for large families - an improvement

In this section, we relax slightly the lower-bound on the size of ℱ \mathcal{F} in Theorem 1.2. We formulate the the problem in terms of simply-rooted families, as we have done in section 3 3. Formulated thus, Theorem 1.4 Says the following:

###### Theorem.

1.4 *There is some absolute constant c > 0 c>0, such that if ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} is simply-rooted, and | ℱ | ≤ ( 1 2 + c) ​ 2 n |\mathcal{F}|\leq(\frac{1}{2}+c)2^{n},then there is some element i ∈ [n] i\in[n] such that i i is rare in ℱ \mathcal{F}.

###### Proof.

Let ℱ ⊆ 2 [n] \mathcal{F}\subseteq 2^{[n]} be a family fulfilling the assumptions of the theorem. If | ℱ | ≥ 2 n − 1 |\mathcal{F}|\geq 2^{n-1}, then we are in the situation of Theorem 1.2 *, and we are done. So let us assume that | ℱ | = ( 1 2 + δ) ​ 2 n |\mathcal{F}|=(\frac{1}{2}+\delta)2^{n}, where 0 < δ < c 0<\delta<c, c c being some absolute constant to be determined later. Assume by contradiction that ℱ \mathcal{F} does not have an abundant element. Identify ℱ \mathcal{F} with a boolean function f: { 0, 1 } n → { − 1, 1 } f:\{0,1\}^{n}\to\{-1,1\} as in section 2.1 2.1. Observe that for this function f f:

 | f ^ ​ ( ∅) = − 2 ​ δ \hat{f}(\emptyset)=-2\delta |  | (8) |

 | f ^ ​ ( i) = I i + ​ ( f) − I i − ​ ( f) > 0, ∀ i ∈ [n] \hat{f}(i)=I_{i}^{+}(f)-I_{i}^{-}(f)>0,\forall i\in[n] |  | (9) |

In a similar fashion to the proof of Theorem 1.2, we try to bound the total influence of f f from below and from above. Let us start with the upper-bound.

Theorem 1.3 provides a bound on the positive influence of f f. Observe that this theorem implies I + ​ ( f) ≤ 1 I^{+}(f)\leq 1. Indeed, the positive influence of f f is exactly the number of simply-rooted elements in ℱ \mathcal{F}, divided by 2 n − 1 2^{n-1}. We can also lower-bound the difference between the positive and the negative influence of f f. Equation 9 asserts that all the level- 1 1 fourier coefficients are positive. Thus:

 | W 1 ​ ( f) = ∑ i = 1 n f ^ ​ ( i) 2 < ∑ i = 1 n f ^ ​ ( i) = I + ​ ( f) − I − ​ ( f) \sqrt{W^{1}(f)}=\sqrt{\sum_{i=1}^{n}\hat{f}(i)^{2}}<\sum_{i=1}^{n}\hat{f}(i)=I^{+}(f)-I^{-}(f) |  |

Combining the equation above with our bound on I + ​ ( f) I^{+}(f), we can upper bound the total influence:

 | I ⁡ ( f) = I + ​ ( f) + I − ​ ( f) < 2 − W 1 ​ ( f). I(f)=I^{+}(f)+I^{-}(f)<2-\sqrt{W^{1}(f)}. |  | (10) |

As for the lower-bound of the influence, we in fact provide two lower-bounds, both derived from Corollary 2.3 with different values of k k. For k = 2 k=2, using also equation 10, we have:

 | 2 − W 1 ​ ( f) > I + ​ ( f) + I − ​ ( f) ≥ 2 − W 1 ​ ( f) − 2 ​ f ^ ​ ( ∅) 2 = 2 − W 1 ​ ( f) − 8 ​ δ 2 2-\sqrt{W^{1}(f)}>I^{+}(f)+I^{-}(f)\geq 2-W^{1}(f)-2\hat{f}(\emptyset)^{2}=2-W^{1}(f)-8\delta^{2} |  |

After moving terms, this amounts to:

 | W 1 ​ ( f) ​ ( 1 − W 1 ​ ( f)) < 8 ​ δ 2. \sqrt{W^{1}(f)}(1-\sqrt{W^{1}(f)})<8\delta^{2}. |  | (11) |

Taking k = 3 k=3 in Corollary 2.3, and using equation 10 (here we use the weaker version I ⁡ ( f) ≤ 2 I(f)\leq 2) gives:

 | 2 ≥ I ⁡ ( f) > 3 − W 2 ​ ( f) − 2 ​ W 1 ​ ( f) − 12 ​ δ 2. 2\geq I(f)>3-W^{2}(f)-2W^{1}(f)-12\delta^{2}. |  |

Or:

 | W 2 ​ ( f) > 1 − 2 ​ W 1 ​ ( f) − 12 ​ δ 2. W^{2}(f)>1-2W^{1}(f)-12\delta^{2}. |  | (12) |

We shall presently see that it’s impossible for both equations 11 and 12 to hold, thus deriving a contradiction. Assume that equation 11 holds. For δ \delta, and thus c c, sufficiently small, this equation implies that either W 1 ​ ( f) < 9 ​ δ 2 \sqrt{W^{1}(f)}<9\delta^{2} or 1 − W 1 ​ ( f) < 9 ​ δ 2 1-\sqrt{W^{1}(f)}<9\delta^{2}.

Assume the latter. Then W 1 ​ ( f) > 1 − 9 ​ δ 2 \sqrt{W^{1}(f)}>1-9\delta^{2}, hence W 1 ​ ( f) > 1 − 18 ​ δ 2 W^{1}(f)>1-18\delta^{2}. By Theorem 2.4 (FKN), this means that f f is at most 18 ​ C 1 ​ δ 2 18C_{1}\delta^{2} -distant from some balanced function, g g. On the other hand, we know that f ^ ​ ( ∅) = − 2 ​ δ \hat{f}(\emptyset)=-2\delta, so f f is at least δ \delta -distant from any balanced function. But if c c, and thus δ \delta, is sufficiently small, then δ > 18 ​ C 1 ​ δ 2 \delta>18C_{1}\delta^{2}, and we arrive at a contradiction.

Assume, then, that W 1 ​ ( f) < 9 ​ δ 2 \sqrt{W^{1}(f)}<9\delta^{2}. For c c sufficiently small, this implies W 1 ​ ( f) < δ 2 W^{1}(f)<\delta^{2}. Plugging this inequality to equation 12, we learn that:

 | W 2 ​ ( f) > 1 − 14 ​ δ 2. W^{2}(f)>1-14\delta^{2}. |  |

Once again, we claim that this is impossible, provided that c c is sufficiently small. Indeed, on the one hand, from Theorem 2.5 (Kindler-Safra), f f is at most 14 ​ C 2 ​ δ 2 14C_{2}\delta^{2} -distant from some balanced function g g, and on the other hand f f is at least δ \delta -distant from any balanced function, and δ > 14 ​ C 2 ​ δ 2 \delta>14C_{2}\delta^{2} if c c is small enough.

In any case we arrive at a contradiction, thus proving the theorem. ∎

## 6 Conclusion

Theorem 1.3, in the language of boolean functions, says that for any simply-rooted function f: { 0, 1 } n → { − 1, 1 } f:\{0,1\}^{n}\to\{-1,1\}, I + ​ ( f) ≤ 1 I^{+}(f)\leq 1. As we have mentioned, this inequality is tight. Consider the following examples:

1. 1.

f 1 ​ ( x) = χ { 1 } ​ ( x) f_{1}(x)=\chi_{\{1\}}(x).

2. 2.

f 2 ​ ( x) = χ { 1, 2 } ​ ( x) f_{2}(x)=\chi_{\{1,2\}}(x).

3. 3.

f 3 ​ ( x) = − 1 2 + 1 2 ​ χ { 1 } ​ ( x) + 1 2 ​ χ { 2 } ​ ( x) + 1 2 ​ χ { 1, 2 } ​ ( x) f_{3}(x)=-\frac{1}{2}+\frac{1}{2}\chi_{\{1\}}(x)+\frac{1}{2}\chi_{\{2\}}(x)+\frac{1}{2}\chi_{\{1,2\}}(x).

The first two examples are balanced functions. That is, the level- 0 0 fourier coefficient is zero. In the last example, this coefficient is − 1 2 -\frac{1}{2}. It would be interesting to understand how big can I + ​ ( f) I^{+}(f) be, as f ^ ​ ( ∅) \hat{f}(\emptyset) grows smaller. We have managed to prove, although we do not include the proof here for the sake of brevity, that if f: { 0, 1 } n → { − 1, 1 } f:\{0,1\}^{n}\to\{-1,1\} is simply-rooted, and f ^ ​ ( ∅) < − 1 2 \hat{f}(\emptyset)<-\frac{1}{2}, then I + ​ ( f) < 1 I^{+}(f)<1. We make the following conjecture regarding the relation of these two qunatities:

###### Conjecture 6.1.

Let f: { 0, 1 } n → { − 1, 1 } f:\{0,1\}^{n}\to\{-1,1\} be a simply-rooted function, and let k ∈ [0, n − 1] k\in[0,n-1], so that f ^ ​ ( ∅) ≤ − ( 1 − 2 − k) \hat{f}(\emptyset)\leq-(1-2^{-k}). Then I + ​ ( f) ≤ ( k + 1) ​ 2 − k I^{+}(f)\leq(k+1)2^{-k}.

The above conjecture, if true, would be tight in the following sense. Let k ∈ [0, n − 1] k\in[0,n-1]. Then C k: { 0, 1 } n → { − 1, 1 } C_{k}:\{0,1\}^{n}\to\{-1,1\}, defined by C k − 1 ​ ( − 1) = { x ∈ { 0, 1 } n | x 1 = 1 ∨ ⋯ ∨ x k = 1 } C_{k}^{-1}(-1)=\{x\in\{0,1\}^{n}|x_{1}=1\vee\dots\vee x_{k}=1\}, is a simply-rooted function, C k ^ ​ ( ∅) = − ( 1 − 2 − k) \widehat{C_{k}}(\emptyset)=-(1-2^{-k}), and I + ​ ( C k) = I ⁡ ( C k) = ( k + 1) ​ 2 − k I^{+}(C_{k})=I(C_{k})=(k+1)2^{-k}. We do not make a conjecture as to the uniqueness of the function. In fact, notice that, in the examples above, both f 1 f_{1} (which is actually C 1 C_{1}) and f 2 f_{2} achieve this bound.

This conjecture should be compared with the well-known edge-isoperimetric inequality for the Hamming cube, which implies the following:

###### Theorem 6.2.

Let f: { 0, 1 } n → { − 1, 1 } f:\{0,1\}^{n}\to\{-1,1\} be a boolean function, and let k ∈ [0, n − 1] k\in[0,n-1], so that − ( 1 − 2 − k) ≤ f ^ ​ ( ∅) ≤ 0 -(1-2^{-k})\leq\hat{f}(\emptyset)\leq 0. Then I ⁡ ( f) ≥ ( k + 1) ​ 2 − k I(f)\geq(k+1)2^{-k}.

The very same function C k C_{k} shows that this is tight. In other words, we conjecture that, out of all simply-rooted functions f: { 0, 1 } n → { − 1, 1 } f:\{0,1\}^{n}\to\{-1,1\} with f ^ ​ ( ∅) = − ( 1 − 2 − k) \hat{f}(\emptyset)=-(1-2^{-k}), the same function, C k C_{k} has both the smallest possible influence and the largest possible positive influence.

## 7 Acknowledgemnts

I would like to thank Ohad Klein, Nathan Keller and my advisor, Gil Kalai, for many helpful suggestions.

## References

- [1] V.B. Alekseev. On the Number of Intersection Semilattices (in Russian). Diskretnaya Matematika, 1:129-136. 1989.
- [2] I. Balla, B. Bollobás, T. Eccles. Union-Closed Families of Sets. Journal of Combinatorial Theory, Series A, 120(3):531-544. 2013.
- [3] I. Bošnjak, P. Marković. The 11-element Case of Frankl’s Conjecture. Electronic Journal of Combinatorics, 15 . Research Paper 88. 2008,
- [4] H. Bruhn, O. Scahudt. The Journey of the Union-Closed Sets Conjecture. Graphs and Combinatorics,31(6):2043-2074. 2015.
- [5] G. Czédli. On Averaging Frankl’s Conjecture for Large Union-Closed Sets. Journal of Combinatorial Theorey, Series A, 116(3):724-729. 2009.
- [6] T. Eccles. A Stability Result for the Union-Closed Size Problem. Combinatorics, Probability and Computing, 25(3):399-418. 2016.
- [7] V. Falgas-Ravry. Minimal Weight in Union-Closed Families. Electronic Journal of Combinatorics, 19(P95):114. 2011.
- [8] E. Friedgut, G. Kalai, A. Naor. Boolean Functions Whose Fourier Transform is Concentrated on the First Two Levels. Advances in Applied Mathematics, 29(3):427-437. 2002.
- [9] W.D. Gao, H.Q. Yu. Note on the Union-Closed Sets Conjecture. Ars Combinatorica, 49:280-288. 1998.
- [10] Y. Hu. On the Union-Closed Sets Conjecture. [https://arxiv.org/abs/1706.06167][1], 2017.
- [11] G. Kindler, S. Safra. Noise-Resistant Boolean-Functions Are Juntas. [https://pdfs.semanticscholar.org/697b/7ec46680ac2be42e1a27c5a3966d949975f4.pdf][2], 2003.
- [12] D.J. Kleitman. Extremal Properties of Collections of Subsets Containing No Two Sets and Their Union. Journal of Combinatorial Theory (Series A), 20:390392. 1976.
- [13] E. Knill Graph Generated Union-Closed Families of Sets. [https://arxiv.org/abs/math/9409215][3]. 1994.
- [14] A. Kotlov. Bulky Subraphs of the Hypercube. European Journal of Combinatorics, 21(4):503-507. 2000.
- [15] G. Lo Faro. A Note on the Union-Closed Sets Conjecture. Journal of the Australian Mathematical Society Series A, 57:230-236. 1994.
- [16] J. Maßberg. The Union-Closed Sets Conjecture for Small Families. Graphs and Combinatorics, 32(5): 2047-2051. 2016.
- [17] P. Marković. An Attempt at Frankl’s Conjecture. Publication de l’institut Mathematique, 81(95):29-43. 2007.
- [18] R. Morris. FC-families and Improved Bounds for Frankl’s Conjecture. European Journal of Combinatorics, 27 : 269-282. 2006.
- [19] R. O’Donnell. Analysis of Boolean Functions. [http://www.contrib.andrew.cmu.edu/~ryanod/?cat=63][4].
- [20] Polymath 11 11. Gowers’s Blog. [https://gowers.wordpress.com/2016/01/21/frankls-union-closed-conjecture-a-possible-polymath-project/][5].
- [21] B. Poonen. Union-closed families. Jorunal of Combinatorial Theory Series A, 59:253-268. 1992.
- [22] D. Reimer. An Average Set Size Theorem. Combinatorics, Probability and Computing, 12(1):89-93. 2003.
- [23] I. Roberts, J. Simpson. A Note on the Union-Closed Sets Conjecture. Australasian Journal of Cominatorics, 47:265-267. 2010.
- [24] P. Wójcik. Union-Closed Families of Sets. Discrete Mathematics, 199:173-182. 1999.
- [25] B. Vučković, M. Živković. The 12 Element Case of Frankl’s Conjecture, preprint. 2012.

[◄][6][image: ar5iv homepage] [7]
[Feeling lucky?][8] [9]
[Conversion report][10]
[Report an issue][11]
[View original on arXiv][12] [►][13]


## Links

[1]: https://arxiv.org/pdf/1706.06167
[2]: https://pdfs.semanticscholar.org/697b/7ec46680ac2be42e1a27c5a3966d949975f4.pdf
[3]: https://arxiv.org/pdf/math/9409215
[4]: http://www.contrib.andrew.cmu.edu/~ryanod/?cat=63
[5]: https://gowers.wordpress.com/2016/01/21/frankls-union-closed-conjecture-a-possible-polymath-project/
[6]: /html/1708.01433
[7]: /
[8]: /feeling_lucky
[9]: /land_of_honey_and_milk
[10]: /log/1708.01434
[11]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+1708.01434
[12]: https://arxiv.org/pdf/1708.01434
[13]: /html/1708.01435
