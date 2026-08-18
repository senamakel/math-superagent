<!-- source: https://ar5iv.labs.arxiv.org/html/0902.0632 | converted from HTML -->

[0902.0632] A Note on Symmetries in the Rauzy graph and Factor Frequencies

# A Note on Symmetries in the Rauzy graph and Factor Frequencies

L​’ubomíra Balková and Edita Pelantová Address: Doppler Institute for Mathematical Physics and Applied Mathematics, and Department of Mathematics, FNSPE, Czech Technical University, Trojanova 13, 120 00 Praha 2, Czech Republic Email address: [l.balkova@centrum.cz, Edita.Pelantova@fjfi.cvut.cz][1]

###### Abstract.

We focus on infinite words with languages closed under reversal. If frequencies of all factors are well defined, we show that the number of different frequencies of factors of length n + 1 n+1 does not exceed 2 ​ Δ ​ C ​ ( n) + 1 2\Delta C(n)+1, where Δ ​ C ​ ( n) \Delta C(n) is the first difference of factor complexity C ⁡ ( n) C(n) of the infinite word.

## 1. Introduction

It is well-known that the Rauzy graph, despite of its simplicity, has turned out to be a powerful tool in the study of various combinatorial properties of words. The first one to use the idea to label edges of the Rauzy graph with frequencies was Dekking [8] in order to show that for every length, there exists at most three different factor frequencies in the Fibonacci sequence. Moreover, he described for every length n n, the set of frequencies of factors of length n n and the number of factors of length n n having the same frequency. Berthé in [3], observing also the evolution of Rauzy graphs for growing factor lengths, generalized Dekking’s result for all Sturmian words. 1 1 1 Note that this result follows also from the 3 3 gap theorem, see [12].

With help of the Rauzy graph, Boshernitzan [5] deduced an upper bound on the number of different frequencies in a general recurrent infinite word. He showed that the number of frequencies of factors of length n + 1 n+1 does not exceed 3 ​ Δ ​ C ​ ( n) 3\Delta C(n), where Δ ​ C ​ ( n) \Delta C(n) is the first difference of factor complexity of the infinite word.

Since Δ ​ C ​ ( n) \Delta C(n) is known to be bounded for infinite words with sublinear complexity (see [6]), it implies for fixed points of primitive substitutions and for fixed points of uniform substitutions (all images of letters have the same length) that the number of different frequencies of factors of the same length is bounded.

Boshernitzan’s upper bound 3 ​ Δ ​ C ​ ( n) 3\Delta C(n) can be further diminished, if the labeled Rauzy graphs corresponding to an infinite word have a nontrivial group of automorphisms. This property of the Rauzy graphs is guaranteed for example if the language of an infinite word is closed under reversal or closed under permutation of letters. The main aim of this paper is to prove the following theorem:

###### Theorem 1.1.

Let u u be an infinite word whose language is closed under reversal and such that the frequency ρ ⁡ ( w) \rho(w) exists for every factor w w of the word u u. Then for every n ∈ ℕ n\in\mathbb{N}, we have

(1) |  | #⁡ { ρ ⁡ ( w) | w ∈ ℒ n + 1 } ≤ 2 ​ Δ ​ C ​ ( n) + 1, \#\{\rho(w)|w\in{\mathcal{L}}_{n+1}\}\quad\leq\quad 2\Delta C(n)+1, |  |

where ℒ n + 1 {\mathcal{L}}_{n+1} denotes the set of factors of u u of length n + 1 n+1.

We also deduce that the equality holds for all sufficiently large n n if and only if u u is periodic. Nevertheless, a recent result of Ferenczi and Zamboni shows that this bound cannot be improved, keeping its general validity, even for aperiodic words whose languages are closed under reversal. In [10], they study the infinite words coding k k -interval exchange transformation with the symmetric permutation. The authors show among others that for such infinite words, the equality in Theorem 1.1 is reached infinitely many times. (In fact, they proved a stronger statement: the set of indices n n for which the equality ( 1) holds has density one.)

Finally, let us mention that the idea to exploit a symmetry of the Rauzy graph was already used in [2] in order to estimate the number of palindromes of a given length. Our article is intended as a further example why it is useful to study symmetries in Rauzy graphs.

## 2. Preliminaries

An alphabet 𝒜 \mathcal{A} is a finite set of symbols, called letters. A concatenation of letters is a word. Length of a word w w is the number of letters contained in w w and is denoted | w | |w|. The set 𝒜 ∗ \mathcal{A}^{*} of all finite words (including the empty word ε \varepsilon) provided with the operation of concatenation is a free monoid. We will also deal with right-sided infinite words u = u 0 ​ u 1 ​ u 2 ​ … u=u_{0}u_{1}u_{2}.... A finite word w w is called a factor of the word u u (finite or infinite) if there exist a finite word w ( 1) w^{(1)} and a word w ( 2) w^{(2)} (finite or infinite) such that u = w ( 1) ​ w ​ w ( 2) u=w^{(1)}ww^{(2)}. The factor w ( 1) w^{(1)} is a prefix of u u and w ( 2) w^{(2)} is a suffix of u u. An infinite word u u is said to be recurrent if each of its factors occur infinitely many times in u u.

Language ℒ {\mathcal{L}} of an infinite word u u is the set of all factors of u u. We denote by ℒ n {\mathcal{L}}_{n} the set of factors of length n n of the infinite word u u. Then, we can define complexity function (or complexity) C: ℕ → ℕ C:\mathbb{N}\rightarrow\mathbb{N} which associates to every n n the number of different factors of length n n of the infinite word u u, i.e. C ⁡ ( n) = #​ ℒ n. C(n)=\#{\mathcal{L}}_{n}.

An important role for determining the factor complexity is played by special factors. We say that a letter a a is right extension of a factor w ∈ ℒ w\in{\mathcal{L}} if w ​ a wa is also a factor of u u. We denote by R ​ e ​ x ​ t ​ ( w) Rext(w) the set of all right extensions of w w in u u, i.e. R ​ e ​ x ​ t ​ ( w) = { a ∈ 𝒜 | w ​ a ∈ ℒ } Rext(w)=\{a\in{\mathcal{A}}\bigm|wa\in{\mathcal{L}}\}. If #​ R ​ e ​ x ​ t ​ ( w) ≥ 2 \#Rext(w)\geq 2, then the factor w w is called right special (RS for short). Analogously, we define left extensions, L ​ e ​ x ​ t ​ ( w) Lext(w), left special factor (LS for short). Moreover, we say that a factor w w is bispecial (BS for short) if w w is LS and RS.

With this in hand, we can introduce a formula for the first difference of complexity Δ ​ C ​ ( n) = C ⁡ ( n + 1) − C ⁡ ( n) \Delta C(n)=C(n+1)-C(n) (taken from [7]).

(2) |  | Δ ​ C ​ ( n) = ∑ w ∈ ℒ n ( #​ R ​ e ​ x ​ t ​ ( w) − 1) = ∑ w ∈ ℒ n ( #​ L ​ e ​ x ​ t ​ ( w) − 1), n ∈ ℕ. \Delta C(n)=\sum_{w\in{\mathcal{L}}_{n}}\bigl(\#Rext(w)-1\bigr)=\sum_{w\in{\mathcal{L}}_{n}}\bigl(\#Lext(w)-1\bigr),\quad n\in\mathbb{N}. |  |

A language ℒ {\mathcal{L}} is closed under reversal, if for every factor w = w 1 ​ … ​ w n ∈ 𝒜 ∗ w=w_{1}\dots w_{n}\in\mathcal{A}^{*} also its mirror image w ¯ = w n ​ … ​ w 1 \overline{w}=w_{n}\dots w_{1} belongs to ℒ {\mathcal{L}}. A factor w w which coincides with its mirror image w ¯ \overline{w} is called palindrome.

If we denote by 𝒫 ​ a ​ l n {\mathcal{P}al}_{n} the set of palindromes of length n n contained in u u, then we can define palindromic complexity P: ℕ → ℕ P:\mathbb{N}\rightarrow\mathbb{N} of the infinite word u u by the prescription P ⁡ ( n) = #​ 𝒫 ​ a ​ l n P(n)=\#{\mathcal{P}al}_{n}. Clearly, P ⁡ ( n) ≤ C ⁡ ( n) P(n)\leq C(n) for any positive integer n n. A non-trivial inequality between P ⁡ ( n) P(n) and C ⁡ ( n) C(n) can be found in [1]. Here we shall use the result from [2]: if the language of an infinite recurrent word is closed under reversal, then

(3) |  | P ⁡ ( n) + P ⁡ ( n + 1) ≤ Δ ​ C ​ ( n) + 2. P(n)+P(n+1)\ \leq\ \Delta C(n)+2. |  |

In this paper, we focus on infinite words with well defined factor frequencies. More precisely, we will assume that for any factor w w of an infinite word u u, the following limit exists

 | lim | v | → ∞, v ∈ ℒ #​ { occurrences of w in v } | v |. \lim_{|v|\to\infty,v\in{\mathcal{L}}}\frac{\#\{\mbox{occurrences of $w$ in $v$}\}}{|v|}. |  |

This limit will be denoted by ρ ⁡ ( w) \rho(w) and called frequency of the factor w w. Let us add that an occurrence of w w in v = v 1 ​ v 2 ​ … ​ v m v=v_{1}v_{2}\ldots v_{m} is an index i ≤ m i\leq m such that w w is a prefix of the word v i ​ v i + 1 ​ … ​ v m v_{i}v_{i+1}\ldots v_{m}.

To dispose of all definitions needed for the deduction of an improved upper bound on the number of different frequencies, it remains to define the labeled Rauzy graph.

Labeled Rauzy graph of order n n of an infinite word u u is a directed graph Γ n \Gamma_{n} whose set of vertices is ℒ n {\mathcal{L}}_{n} and set of edges is ℒ n + 1 {\mathcal{L}}_{n+1}. Any edge e = w 0 ​ w 1 ​ … ​ w n e=w_{0}w_{1}\dots w_{n} starts in the vertex w = w 0 ​ w 1 ​ … ​ w n − 1 w=w_{0}w_{1}\dots w_{n-1}, ends in the vertex v = w 1 ​ … ​ w n − 1 ​ w n v=w_{1}\dots w_{n-1}w_{n}, and is labeled by its factor frequency ρ ⁡ ( e) \rho(e).

## 3. Reduced Rauzy graphs

Edge frequencies in a Rauzy graph Γ n \Gamma_{n} behave similarly as current in a circuit.We may formulate an analogy of Kirchhoff’s law: the sum of frequencies of edges ending in a vertex equals the sum of frequencies of edges starting in this vertex. As a direct consequence, if a Rauzy graph contains a vertex with only one incoming and one outgoing edge, then the frequency of these edges is the same, say ρ \rho. Therefore, we can replace this triple (edge-vertex-edge) with only one edge keeping the frequency ρ \rho. If we reduce the Rauzy graph step by step applying the above described procedure, we obtain the so-called reduced Rauzy graph Γ ~ n \tilde{\Gamma}_{n}, which simplifies the investigation of edge frequencies. In order to precise this consideration, we introduce the following notion.

###### Definition 3.1.

Let Γ n \Gamma_{n} be the labeled Rauzy graph of order n n of an infinite word u u. A directed path w ( 0) ​ w ( 1) ​ … ​ w ( m) w^{(0)}w^{(1)}\dots w^{(m)} of non-zero length in Γ n \Gamma_{n} such that its initial vertex w ( 0) w^{(0)} and its final vertex w ( m) w^{(m)} are LS or RS, and the other vertices are neither LS nor RS factors is called simple. We define label of the simple path as the label of any edge of this path.

###### Definition 3.2.

Reduced Rauzy graph Γ ~ n \tilde{\Gamma}_{n} of u u (of order n n) is a directed graph whose set of vertices is formed by LS and RS factors of ℒ n {\mathcal{L}}_{n} and whose set of edges is given in the following way. Vertices w w and v v are connected with an edge e e if there exists in Γ n \Gamma_{n} a simple path starting in w w and ending in v v. We assign to such an edge e e the label of the corresponding simple path.

For a recurrent word u u, at least one edge starts and at least one edge ends in every vertex of Γ n \Gamma_{n}. Therefore, no edge label is lost by the reduction of Γ n \Gamma_{n}. The number of different edge labels in the reduced Rauzy graph Γ ~ n \tilde{\Gamma}_{n} is clearly less or equal to the number of edges in Γ ~ n \tilde{\Gamma}_{n}. Let us thus calculate the number of edges in Γ ~ n \tilde{\Gamma}_{n} in order to get an upper bound on the number of frequencies of factors in ℒ n + 1 {\mathcal{L}}_{n+1}.

For every RS factor w ∈ ℒ n w\in{\mathcal{L}}_{n}, it holds that #​ R ​ e ​ x ​ t ​ ( w) \#Rext(w) edges begin in w w, and for every LS factor v ∈ ℒ n v\in{\mathcal{L}}_{n} which is not RS, only one edge begins in v v, thus we get the following relation

(4) |  | #⁡ { e | e ​ edge in ​ Γ ~ n } = ∑ w ​ RS in ℒ n #​ R ​ e ​ x ​ t ​ ( w) + ∑ v ​ LS ​ not RS in ℒ n 1. \#\{e|\ e\ \mbox{edge in}\ \tilde{\Gamma}_{n}\}=\sum_{w\ \text{RS in ${\mathcal{L}}_{n}$}}\#Rext(w)+\sum_{v\ \text{LS}\ \text{not RS in ${\mathcal{L}}_{n}$}}1. |  |

Using Equation ( 2), we deduce that

(5) |  | #⁡ { e | e ​ edge in ​ Γ ~ n } = Δ ​ C ​ ( n) + ∑ v ​ RS in ℒ n 1 + ∑ v ​ LS ​ not RS in ℒ n 1. \#\{e|\ e\ \mbox{edge in}\ \tilde{\Gamma}_{n}\}=\Delta C(n)+\sum_{v\ \text{RS in ${\mathcal{L}}_{n}$}}1+\sum_{v\ \text{LS}\ \text{not RS in ${\mathcal{L}}_{n}$}}1. |  |

Since #​ R ​ e ​ x ​ t ​ ( w) − 1 ≥ 1 \#Rext(w)-1\geq 1 for any RS factor w w and, similarly, for LS factors, we have

(6) |  | #{ w ∈ ℒ n | w R S } ≤ Δ C ( n) and #{ w ∈ ℒ n | w L S } ≤ Δ C ( n) \#\{w\in{\mathcal{L}}_{n}|\ w\ RS\}\ \leq\ \ \Delta C(n)\quad{\rm and}\quad\#\{w\in{\mathcal{L}}_{n}|\ w\ LS\}\ \leq\ \ \Delta C(n) |  |

The following result initially proved by Boshernitzan in [5] follows immediately by combining ( 5) and ( 6).

###### Theorem 3.3.

Let u u be an infinite recurrent word such that for every factor w ∈ ℒ w\in{\mathcal{L}}, the frequency ρ ⁡ ( w) \rho(w) exists. Then for every n ∈ ℕ n\in\mathbb{N}, it holds

 | #⁡ { ρ ⁡ ( e) | e ∈ ℒ n + 1 } ≤ 3 ​ Δ ​ C ​ ( n). \#\{\rho(e)\bigm|e\in{\mathcal{L}}_{n+1}\}\quad\leq\quad 3\Delta C(n). |  |

## 4. Proof of the Theorem 1.1

Let us focus in the sequel on infinite words u u whose languages are closed under reversal and such that the frequency of every factor exists.

1. (1)

Such words are necessarily recurrent.

2. (2)

For any pair of factors w, v ∈ ℒ w,v\in{\mathcal{L}}, it holds

 | #​ { occurrences of w in v } | v | = #​ { occurrences of w ¯ in v ¯ } | v ¯ |. \frac{\#\{\mbox{occurrences of $w$ in $v$}\}}{|v|}=\frac{\#\{\mbox{occurrences of $\overline{w}$ in $\overline{v}$}\}}{|\overline{v}|}. |  |

Consequently, ρ ⁡ ( w) = ρ ⁡ ( w ¯) \rho(w)=\rho(\overline{w}) for all factors w w of u u.

With the above two ingredients in hand, we will be able to prove an essential lemma. Proof of Theorem 1.1 will be then a direct consequence of this lemma.

###### Lemma 4.1.

Let u u be an infinite word whose language ℒ {\mathcal{L}} is closed under reversal and such that for each factor w ∈ ℒ w\in{\mathcal{L}}, the frequency ρ ⁡ ( w) \rho(w) exists. Then for every n ∈ ℕ n\in\mathbb{N}, we have

 | #⁡ { ρ ⁡ ( e) | e ∈ ℒ n + 1 } ≤ 1 2 ​ ( P ⁡ ( n) + P ⁡ ( n + 1) + Δ ​ C ​ ( n) − X − Y) + Z, \#\{\rho(e)|e\in{\mathcal{L}}_{n+1}\}\quad\leq\quad\frac{1}{2}\ \Bigl(P(n)+P(n+1)+\Delta C(n)-X-Y\Bigr)+Z, |  |

where | X X is the number of BS factors of length n n, |

 | Y Y is the number of BS palindromic factors of length n n, |

 | Z Z is the number of RS factors of length n n. |

###### Proof.

Let Γ n \Gamma_{n} be the labeled Rauzy graph of u u of order n n. Let us define a mapping μ \mu which to every vertex w ∈ ℒ n w\in{\mathcal{L}}_{n} associates the vertex w ¯ \overline{w}, to every edge e ∈ ℒ n + 1 e\in{\mathcal{L}}_{n+1} associates the edge e ¯ \overline{e}. Then, μ 2 = I ​ d {\mu}^{2}=Id, and, thanks to the closeness of ℒ {\mathcal{L}} under reversal, μ \mu maps Γ n \Gamma_{n} onto itself, in fact, μ \mu is an automorphism of Γ n \Gamma_{n}. Clearly, every simple path w ( 0) ​ w ( 1) ​ … ​ w ( m) w^{(0)}w^{(1)}\dots w^{(m)} in Γ n \Gamma_{n} is mapped by μ \mu to the simple path w ( m) ¯ ​ … ​ w ( 1) ¯ ​ w ( 0) ¯ \overline{w^{(m)}}\dots\overline{w^{(1)}}\ \overline{w^{(0)}}. This implies that μ \mu induces an automorphism on the reduced Rauzy graph Γ ~ n \tilde{\Gamma}_{n}, too.

We know already that the set of edge labels of Γ ~ n \tilde{\Gamma}_{n} is equal to the set of edge labels of Γ n \Gamma_{n}. Let us denote by A A the number of edges e e in Γ ~ n \tilde{\Gamma}_{n} (the number of simple paths in Γ n \Gamma_{n}) such that e e is mapped by μ \mu onto itself and by B B the number of edges e e in Γ ~ n \tilde{\Gamma}_{n} such that e e is not mapped by μ \mu onto itself, then clearly,

 | #⁡ { e | e ​ edge in ​ Γ ~ n } = A + B. \#\{e|\ e\ \mbox{edge in}\ \tilde{\Gamma}_{n}\}=A+B. |  |

If e e is mapped by μ \mu onto itself, then the corresponding simple path satisfies

 | w ( 0) ​ w ( 1) ​ … ​ w ( m) = w ( m) ¯ ​ … ​ w ( 1) ¯ ​ w ( 0) ¯, w^{(0)}w^{(1)}\dots w^{(m)}=\overline{w^{(m)}}\dots\overline{w^{(1)}}\ \overline{w^{(0)}}, |  |

hence, for m m even, its central vertex w ( m 2) w^{(\frac{m}{2})} is a palindrome, and for m m odd, its central edge going from w ( m − 1 2) w^{(\frac{m-1}{2})} to w ( m + 1 2) w^{(\frac{m+1}{2})} is a palindrome. On the other hand, every palindrome of length n + 1 n+1 is the central factor of a simple path mapped by μ \mu onto itself and every palindrome of length n n is either the central vertex of a simple path mapped by μ \mu onto itself or is BS. Therefore,

(7) |  | A = P ⁡ ( n) + P ⁡ ( n + 1) − #⁡ { w ∈ ℒ n | w ​ BS in 𝒫 ​ a ​ l n }. A=P(n)+P(n+1)-\#\{w\in{\mathcal{L}}_{n}|w\ \mbox{BS in ${\mathcal{P}al}_{n}$}\}. |  |

We subtract the number of palindromic BS factors of ℒ n {\mathcal{L}}_{n}, in the statement denoted by Y Y, since they are not inner vertices of any simple path.

Now, let us turn our attention to edges of Γ ~ n \tilde{\Gamma}_{n} which are not mapped by μ \mu onto themselves. For every such edge e e, at least one another edge, namely μ ⁡ ( e) \mu(e), has the same label ρ ⁡ ( e) \rho(e). These considerations lead to the following estimate

(8) |  | #⁡ { ρ ⁡ ( e) | e ∈ ℒ n + 1 } ≤ A + 1 2 ​ B = 1 2 ​ A + 1 2 ​ ( A + B). \#\{\rho(e)|\ e\in{\mathcal{L}}_{n+1}\}\leq A+\tfrac{1}{2}B=\tfrac{1}{2}A+\tfrac{1}{2}(A+B). |  |

Rewriting Equation ( 5), we obtain

 | A + B = Δ ​ C ​ ( n) + 2 ​ Z − X. A+B=\Delta C(n)+2Z-X. |  |

This fact together with ( 7) and ( 8) proves the statement. ∎

If we apply on P ⁡ ( n) + P ⁡ ( n + 1) P(n)+P(n+1) and Z Z from Lemma 4.1 the estimates ( 3) and ( 6), respectively, we obtain immediately Proof of Theorem 1.1. In fact, we get even a finer upper bound

(9) |  | #⁡ { ρ ⁡ ( e) | e ∈ ℒ n + 1 } ≤ 2 ​ Δ ​ C ​ ( n) + 1 − 1 2 ​ X − 1 2 ​ Y, \#\{\rho(e)|e\in{\mathcal{L}}_{n+1}\}\quad\leq\quad 2\Delta C(n)+1-\tfrac{1}{2}X-\tfrac{1}{2}Y, |  |

where X X is the number of BS factors of length n n and Y Y is the number of BS palindromic factors of length n n.

Let us study for which infinite words, the equality in Theorem 1.1 is attained. Infinite words whose languages are closed under reversal are either purely periodic or aperiodic.

- •

In case of purely periodic words, for sufficiently large n n, the first difference of complexity Δ ​ C ​ ( n) = 0 \Delta C(n)=0 and all factors of length n n have the same frequency.

- •

On the other hand, aperiodic words contain infinitely many BS factors. Hence, according to ( 9), the inequality in Theorem 1.1 is strict for infinitely many n n.

This reasoning leads to the following corollary.

###### Corollary 4.2.

Let u u be an infinite word whose language ℒ {\mathcal{L}} is closed under reversal and such that for each factor w ∈ ℒ w\in{\mathcal{L}}, the frequency ρ ⁡ ( w) \rho(w) exists. Then, the equality

 | #⁡ { ρ ⁡ ( e) | e ∈ ℒ n + 1 } = 2 ​ Δ ​ C ​ ( n) + 1 \#\{\rho(e)|e\in{\mathcal{L}}_{n+1}\}\quad=\quad 2\Delta C(n)+1 |  |

holds for all sufficiently large n n if and only if u u is periodic.

## 5. Comments

1. (1)

Berthé in [3] has shown that for every Sturmian word, the number of frequencies of factors of length n n equals 2 if ℒ n {\mathcal{L}}_{n} contains a BS factor, and is equal to 3 otherwise. Since any BS factor of a Sturmian word is a palindrome, the finer upper bound in ( 9) is reached for all n ∈ ℕ n\in\mathbb{N}.

2. (2)

Ferenczi and Zamboni [10] have proved that infinite words coding k k -interval exchange transformation whose language is closed under reversal attain the upper bound in ( 9) for all n ∈ ℕ n\in\mathbb{N}. As Sturmian words are infinite words coding 2-interval exchange transformation, Item (1) is a particular case of their result.

3. (3)

Another example of infinite words for which the upper bound in Theorem 1.1 is reached infinitely many times are fixed points of the following substitution φ \varphi on { 0, 1 } \{0,1\}:

 | φ ⁡ ( 0) = 0 a ​ 1, φ ⁡ ( 1) = 0 b ​ 1, a > b ≥ 1. \varphi(0)=0^{a}1,\quad\varphi(1)=0^{b}1,\quad a>b\geq 1. |  |

The substitution φ \varphi is a canonical substitution associated with quadratic non-simple Parry numbers (for the precise definition see [9]).

4. (4)

There exist infinite words having languages closed under reversal, however, containing only a finite number of palindromes. For an example see [4]. For such words, Lemma 4.1 provides even a better estimate

 | #⁡ { ρ ⁡ ( e) | e ∈ ℒ n + 1 } ≤ 3 2 ​ Δ ​ C ​ ( n). \#\{\rho(e)|e\in{\mathcal{L}}_{n+1}\}\quad\leq\quad\tfrac{3}{2}\Delta C(n). |  |

5. (5)

The essential idea of our approach relies in the fact that the closeness of the language under reversal implies existence of a non-triavial automorphism of the labeled Rauzy graph. More generally, our method can be applied on any infinite word whose language ℒ \mathcal{L} possesses a symmetry T: ℒ → ℒ T:{\mathcal{L}}\rightarrow{\mathcal{L}} with the following properties:

  1. (a)

T T is a bijective map,

  2. (b)

for every w, v ∈ ℒ w,v\in{\mathcal{L}},

 | #​ { occurrences of w in v } = #​ { occurrences of T ⁡ ( w) in T ⁡ ( v) }. \#\{\text{occurrences of $w$ in $v$}\}=\#\{\text{occurrences of $T(w)$ in $T(v)$}\}. |  |

Clearly, the mirror image map w → w ¯ w\to\overline{w} satisfies both assumptions. A further example can be obtained if we choose a permutation π \pi of letters and define T π ​ ( w 1 ​ w 2 ​ … ​ w n) = π ⁡ ( w 1) ​ π ​ ( w 2) ​ … ​ π ​ ( w n) T_{\pi}(w_{1}w_{2}\dots w_{n})=\pi(w_{1})\pi(w_{2})\dots\pi(w_{n}) for each factor w 1 ​ w 2 ​ … ​ w n w_{1}w_{2}\dots w_{n}. It may be shown that the group of all such symmetries T T is generated by the mirror image map and the mappings T π T_{\pi}.

6. (6)

If the language of a binary word is closed under exchange π \pi of letters (such words are called complementation-symmetric), no simple path is mapped by π \pi on itself and, thus, each frequency is assigned to at least two edges in a reduced Rauzy graph Γ ~ n \tilde{\Gamma}_{n}. As the number of edges is at most 3 ​ Δ ​ C ​ ( n) 3\Delta C(n), we obtain for frequencies the same upper bound as in Item ( 4).

7. (7)

The Thue-Morse sequence has in the sense of Item ( 5) the most symmetrical language among binary words. It explains why the upper bound from Theorem 1.1 overestimates the actual number of factor frequencies. For concrete values of factor frequencies consult Frid [11].

## 6. Acknowledgment

The authors acknowledge the financial support of Czech Science Foundation GAČR 201/05/0169 and the Ministry of Education of the Czech Republic LC06002.

## References

- [1] J.-P. Allouche, M. Baake, J. Cassaigne, D. Damanik, *Palindrome complexity*, Theoret. Comput. Sci. 292 (2003), 9–31
- [2] P. Baláži, Z. Masáková, E. Pelantová, Factor versus palindromic complexity of uniformly recurrent infinite words, Theoret. Comput. Sci. 3 80 (2007), 266–275
- [3] V. Berthé, Fréquences des facteurs des suites sturmiennes, Theor. comput. sci. 1 65 (1996), 295–309
- [4] J. Berstel, L. Boasson, O. Carton, I. Fagnot, Infinite words without palindromes, preprint (2006)
- [5] M. Boshernitzan, *A condition for unique ergodicity of minimal symbolic flows*, Ergodic Theory Dynam. Systems 12 (1992), 425–428
- [6] J. Cassaigne, Special factors of sequences with linear subword complexity, Developments in language theory, II (Magdeburg, 1995), World Sci. Publishing, Singapore (1996), 25–34
- [7] J. Cassaigne, Complexité et facteurs spéciaux [Complexity and special factors], Journées Montoises (Mons, 1994), Bull. Belg. Math. Soc. Simon Stevin 4 (1997), 67–88
- [8] M. Dekking, On the Thue-Morse measure, Acta Univ. Carolin. Math. Phys. 33 (1992), 35–40
- [9] S. Fabre, Substitutions et β \beta -systèmes de numération, Theoret. Comput. Sci. 137 (1995), 219–236
- [10] S. Ferenczi, L. Zamboni, Combinatorial structure of symmetric k k -interval exchange transformation, http://iml.univ-mrs.fr/ ferenczi/fz1.pdf
- [11] A. Frid, On the frequency of factors in a D0L word, Journal of Automata, Languages and Combinatorics 3 (1998), 29–41
- [12] V. Sós, On the distribution mod 1 of the sequence n ​ α n\alpha, Ann. Univ. Sci. Budapest, Eötvös Sect. Math. 1 (1958), 127–134

[◄][2][image: ar5iv homepage] [3]
[Feeling lucky?][4] [5]
[Conversion report][6]
[Report an issue][7]
[View original on arXiv][8] [►][9]


## Links

[1]: mailto:l.balkova@centrum.cz,%20Edita.Pelantova@fjfi.cvut.cz
[2]: /html/0902.0631
[3]: /
[4]: /feeling_lucky
[5]: /land_of_honey_and_milk
[6]: /log/0902.0632
[7]: https://github.com/dginev/ar5iv/issues/new?template=improve-article--arxiv-id-.md&title=Improve+article+0902.0632
[8]: https://arxiv.org/pdf/0902.0632
[9]: /html/0902.0633
