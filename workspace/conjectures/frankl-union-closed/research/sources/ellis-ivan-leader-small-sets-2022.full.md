<!-- source: https://arxiv.org/html/2201.11484 | converted from HTML -->

SMALL SETS IN UNION-CLOSED FAMILIES

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2201.11484v3 [math.CO] 23 Jan 2023

# SMALL SETS IN UNION-CLOSED FAMILIES

DAVID ELLIS MARIA-ROMINA IVAN AND IMRE LEADER

###### Abstract

Our aim in this note is to show that, for any ϵ > 0 \epsilon>0, there exists a union-closed family ℱ \mathcal{F} with (unique) smallest set S S such that no element of S S belongs to more than a fraction ϵ \epsilon of the sets in ℱ \mathcal{F}. More precisely, we give an example of a union-closed family with smallest set of size k k such that no element of this set belongs to more than a fraction ( 1 + o ⁡ ( 1)) ​ log 2 ⁡ k 2 ​ k (1+o(1))\frac{\log_{2}k}{2k} of the sets in ℱ \mathcal{F}.

We also give explicit examples of union-closed families containing ‘small’ sets for which we have been unable to verify the Union-Closed Conjecture.

## 1 Introduction

If X X is a set, a family ℱ \mathcal{F} of subsets of X X is said to be union-closed if the union of any two sets in ℱ \mathcal{F} is also in ℱ \mathcal{F}. The Union-Closed Conjecture (a conjecture of Frankl [5]) states that if X X is a finite set and ℱ \mathcal{F} is a union-closed family of subsets of X X (with ℱ ≠ { ∅ } \mathcal{F}\neq\{\emptyset\}), then there exists an element x ∈ X x\in X such that x x is contained in at least half of the sets in ℱ \mathcal{F}. Despite the efforts of many researchers over the last forty-five years, and a recent Polymath project [7] aimed at resolving it, this conjecture remains wide open. It has only been proved under very strong constraints on the ground-set X X or the family ℱ \mathcal{F}; for example, Balla, Bollobás and Eccles [3] proved it in the case where | ℱ | ≥ 2 3 ​ 2 | X | |\mathcal{F}|\geq\tfrac{2}{3}2^{|X|}; more recently, Karpas [6] proved it in the case where | ℱ | ≥ ( 1 2 − c) ​ 2 | X | |\mathcal{F}|\geq(\tfrac{1}{2}-c)2^{|X|} for a small absolute constant c > 0 c>0; and it is also known to hold whenever | X | ≤ 12 |X|\leq 12 or | ℱ | ≤ 50 |\mathcal{F}|\leq 50, from work of Vučković and Živković [11] and of Roberts and Simpson [9]. Note that the Union-Closed Conjecture is not even known to hold in the weaker form where we replace the fraction 1 / 2 1/2 by any other fixed ϵ > 0 \epsilon>0. 1 1 1 Note added in proof: shortly before the acceptance of this manuscript, Gilmer [arXiv:2211.09055] obtained a breakthrough on the Union-Closed Conjecture, showing that it holds in the weaker form with the fraction 1 / 2 1/2 replaced by 1 / 100 1/100. For general background and a wealth of further information on the Union-Closed Conjecture see the survey of Bruhn and Schaudt [4].

As usual, if X X is a set we write 𝒫 ⁡ ( X) \mathcal{P}(X) for its power-set. If X X is a finite set and ℱ ⊂ 𝒫 ⁡ ( X) \mathcal{F}\subset\mathcal{P}(X) with ℱ ≠ ∅ \mathcal{F}\neq\emptyset, we define the frequency of x x (with respect to ℱ \mathcal{F}) to be γ x = | { A ∈ ℱ: x ∈ A } | / | ℱ | \gamma_{x}=|\{A\in\mathcal{F}:\ x\in A\}|/|\mathcal{F}|, i.e., γ x \gamma_{x} is the proportion of members of X X that contain x x. If a union-closed family contains a ‘small’ set, what can we say about the frequencies in that set?

If a union-closed family ℱ \mathcal{F} contains a singleton, then that element clearly has frequency at least 1 / 2 1/2, while if it contains a set S S of size 2 then, as noted by Sarvate and Renaud [10], some element of S S has frequency at least 1 / 2 1/2. However, they also gave an example of a union-closed family ℱ \mathcal{F} whose smallest set S S has size 3 and yet where each element of S S has frequency below 1 / 2 1/2. Generalising a construction of Poonen [8], Bruhn and Schaudt [4] gave, for each k ≥ 3 k\geq 3, an example of a union-closed family with (unique) smallest set of size k k and with every element of that set having frequency below 1 / 2 1/2.

However, in these and all other known examples, there is always some element of a minimal-size set having frequency at least 1 / 3 1/3. So it is natural to ask if there is really a constant lower bound for these frequencies.

Our aim in this note is to show that this is not the case.

###### Theorem 1.

For any positive integer k k, there exists a union-closed family in which the (unique) smallest set has size k k, but where each element of this set has frequency

 | ( 1 + o ⁡ ( 1)) ​ log ⁡ k 2 ​ k. (1+o(1))\frac{\log k}{2k}. |  |

(All logarithms in this paper are to base 2. Also, as usual, the o ⁡ ( 1) o(1) denotes a function of k k that tends to zero as k k tends to infinity.) The proof of Theorem 1 is by an explicit construction.

Theorem 1 is asymptotically sharp, in view of results of Wójcik [12] and Balla [2]: Wójcik showed that if S S is a set of size k ≥ 1 k\geq 1 in a finite union-closed family, then the average frequency of the elements in S S is at least c k c_{k}, where k ⋅ c k k\cdot c_{k} is defined to be the minimum average set-size over all union-closed families on the ground-set [k] [k], and Balla showed that c k = ( 1 + o ⁡ ( 1)) ​ log ⁡ k 2 ​ k c_{k}=(1+o(1))\frac{\log k}{2k}, confirming a conjecture of Wójcik from [12].

Remarkably, there are union-closed families containing small sets, even sets of size 3, for which we have been unable to verify the Union-Closed Conjecture. We give some examples at the end of the paper.

## 2 Proof of main result

For our construction, we need the following ‘design-theoretic’ lemma.

###### Lemma 2.

For any positive integers k > t k>t there exist infinitely many positive integers d d such that t t divides d ​ k dk and the following holds. If X X is a set of size d ​ k / t dk/t, then there exists a family 𝒜 = { A 1, …, A k } \mathcal{A}=\{A_{1},\ldots,A_{k}\} of k k d d -element subsets of X X, such that each element of X X is contained in exactly t t sets in 𝒜 \mathcal{A}, and for 2 ≤ r ≤ t 2\leq r\leq t, any r r distinct sets in 𝒜 \mathcal{A} have intersection of size

 | d ​ ( t − 1) ​ ( t − 2) ​ … ​ ( t − r + 1) ( k − 1) ​ ( k − 2) ​ … ​ ( k − r + 1), d\dfrac{(t-1)(t-2)\ldots(t-r+1)}{(k-1)(k-2)\ldots(k-r+1)}, |  |

i.e.

 | | A i 1 ∩ A i 2 ∩ … ∩ A i r | = d ​ ( t − 1) ​ ( t − 2) ​ … ​ ( t − r + 1) ( k − 1) ​ ( k − 2) ​ … ​ ( k − r + 1) |A_{i_{1}}\cap A_{i_{2}}\cap\ldots\cap A_{i_{r}}|=d\dfrac{(t-1)(t-2)\ldots(t-r+1)}{(k-1)(k-2)\ldots(k-r+1)} |  |

for any 1 ≤ i 1 < i 2 < … < i r ≤ k 1\leq i_{1}<i_{2}<\ldots<i_{r}\leq k.

###### Proof.

Let q q be a positive integer, and set d = ( k − 1 t − 1) ​ q t d=\binom{k-1}{t-1}q^{t}; we will take | X | = ( k t) ​ q t |X|=\binom{k}{t}q^{t}. Partition [q ​ k] [qk] into k k sets, B 1, B 2, …, B k B_{1},B_{2},\ldots,B_{k} say, each of size q q; we call these sets ‘blocks’. We let X X be the set of all t t -element subsets of [q ​ k] [qk] that contain at most one element from each block. For each i ∈ [k] i\in[k] we let A i A_{i} be the family of all sets in X X that contain an element from the block B i B_{i}. Clearly, | A i | = ( k − 1 t − 1) ​ q t = d |A_{i}|=\binom{k-1}{t-1}q^{t}=d for each i ∈ [k] i\in[k], and each element of X X appears in exactly t t of the A i A_{i}. Also, for example A i ∩ A j A_{i}\cap A_{j} consists of all sets in X X that contain both an element from the block B i B_{i} and an element from the block B j B_{j}, so

 | | A i ∩ A j | = ( k − 2 t − 2) ​ q t = ( k − 1 t − 1) ​ q t ​ t − 1 k − 1 = d ​ t − 1 k − 1. |A_{i}\cap A_{j}|=\binom{k-2}{t-2}q^{t}=\binom{k-1}{t-1}q^{t}\dfrac{t-1}{k-1}=d\dfrac{t-1}{k-1}. |  |

It is easy to check that the other intersections also have the claimed sizes. ∎

We remark that, in what follows, it is vital that the integer d d in Lemma 2 can be taken to be arbitrarily large as a function of k k and t t.

###### Proof of Theorem 1.

We define n = d ​ k / t + k n=dk/t+k, we take d ∈ ℕ d\in\mathbb{N} as in the above lemma, and we let X = [d ​ k / t] X=[dk/t]; the claim yields a family 𝒜 = { A 1, …, A k } \mathcal{A}=\{A_{1},\ldots,A_{k}\} of k k d d -element subsets of X = [d ​ k / t] X=[dk/t] such that each element of [d ​ k / t] [dk/t] is contained in exactly t t of the sets in 𝒜 \mathcal{A}, and for any 2 ≤ r ≤ t 2\leq r\leq t, any r r distinct sets in 𝒜 \mathcal{A} have intersection of size

 | d ​ ( t − 1) ​ ( t − 2) ​ … ​ ( t − r + 1) ( k − 1) ​ ( k − 2) ​ … ​ ( k − r + 1). d\dfrac{(t-1)(t-2)\ldots(t-r+1)}{(k-1)(k-2)\ldots(k-r+1)}. |  |

Write m = d ​ k / t m=dk/t. We take ℱ ⊂ 𝒫 ⁡ ( [n]) \mathcal{F}\subset\mathcal{P}([n]) to be the smallest union-closed family containing the k k -element set { m + 1, …, m + k } \{m+1,\ldots,m+k\} and all sets of the form { m + i } ∪ ( X ∖ { x }) \{m+i\}\cup(X\setminus\{x\}) where i ∈ [k] i\in[k] and x ∈ A i x\in A_{i}.

For brevity, we write S 0 = { m + 1, m + 2, …, m + k } S_{0}=\{m+1,m+2,\ldots,m+k\}. We will show that each element of S 0 S_{0} has frequency

 | ( 1 + o ⁡ ( 1)) ​ log ⁡ k 2 ​ k, (1+o(1))\frac{\log k}{2k}, |  |

provided t t and d d are chosen to be appropriate functions of k k; moreover, with these choices, S 0 S_{0} will be the smallest set in ℱ \mathcal{F}.

Clearly, ℱ \mathcal{F} contains S 0 S_{0}, all sets of the form S 0 ∪ ( X ∖ { x }) S_{0}\cup(X\setminus\{x\}) for x ∈ X x\in X, all sets of the form R ∪ X R\cup X where R R is a nonempty subset of S 0 S_{0}, and finally all sets of the form R ∪ ( X ∖ { x }) R\cup(X\setminus\{x\}), where R = { m + i 1, …, m + i r } R=\{m+i_{1},\ldots,m+i_{r}\} is a nonempty r r -element subset of S 0 S_{0} and x ∈ A i 1 ∩ A i 2 ∩ … ∩ A i r x\in A_{i_{1}}\cap A_{i_{2}}\cap\ldots\cap A_{i_{r}}, for 1 ≤ r ≤ t 1\leq r\leq t. It is easy to see that the family ℱ \mathcal{F} contains no other sets.

It follows that

 | | ℱ | \displaystyle|\mathcal{F}| | = 1 + d ​ k / t + ( 2 k − 1) + ∑ r = 1 t ( k r) ​ d ​ ( t − 1) ​ ( t − 2) ​ … ​ ( t − r + 1) ( k − 1) ​ ( k − 2) ​ … ​ ( k − r + 1) \displaystyle=1+dk/t+(2^{k}-1)+\sum_{r=1}^{t}{k\choose r}d\dfrac{(t-1)(t-2)\ldots(t-r+1)}{(k-1)(k-2)\ldots(k-r+1)} |  |

 |  | = d ​ k / t + 2 k + d ​ k t ​ ∑ r = 1 t ( t r) \displaystyle=dk/t+2^{k}+\frac{dk}{t}\sum_{r=1}^{t}{t\choose r} |  |

 |  | = d ​ k / t + 2 k + d ​ k t ​ ( 2 t − 1) \displaystyle=dk/t+2^{k}+\frac{dk}{t}(2^{t}-1) |  |

 |  | = 2 k + d ​ k ​ 2 t t. \displaystyle=2^{k}+\frac{dk2^{t}}{t}. |  |

On the other hand, the number of sets in ℱ \mathcal{F} that contain the element m + 1 m+1 is equal to

 |  | 1 + d ​ k / t + 2 k − 1 + ∑ r = 1 t ( k − 1 r − 1) ​ d ​ ( t − 1) ​ ( t − 2) ​ … ​ ( t − r + 1) ( k − 1) ​ ( k − 2) ​ … ​ ( k − r + 1) \displaystyle 1+dk/t+2^{k-1}+\sum_{r=1}^{t}{k-1\choose r-1}d\dfrac{(t-1)(t-2)\ldots(t-r+1)}{(k-1)(k-2)\ldots(k-r+1)} |  |

 |  | = 1 + d ​ k / t + 2 k − 1 + d ​ ∑ r = 1 t ( t − 1 r − 1) \displaystyle=1+dk/t+2^{k-1}+d\sum_{r=1}^{t}{t-1\choose r-1} |  |

 |  | = 1 + d ​ k / t + 2 k − 1 + 2 t − 1 ​ d. \displaystyle=1+dk/t+2^{k-1}+2^{t-1}d. |  |

It follows that the frequency of m + 1 m+1 (or, by symmetry, of any other element of S 0 S_{0}) equals

 | 1 + k ​ d / t + 2 k − 1 + 2 t − 1 ​ d 2 k + d ​ k ​ 2 t / t = ( 1 + 2 k − 1) / d + k / t + 2 t − 1 2 k / d + k ​ 2 t / t. \frac{1+kd/t+2^{k-1}+2^{t-1}d}{2^{k}+dk2^{t}/t}=\frac{(1+2^{k-1})/d+k/t+2^{t-1}}{2^{k}/d+k2^{t}/t}. |  |

To (asymptotically) minimise this expression, we take t = ⌊ log ⁡ k ⌋ t=\lfloor\log k\rfloor and d → ∞ d\to\infty (for fixed k k); this yields a union-closed family in which the (unique) smallest set (namely S 0 S_{0}) has size k k, and every element of that set has frequency

 | ( 1 + o ⁡ ( 1)) ​ log ⁡ k 2 ​ k, (1+o(1))\frac{\log k}{2k}, |  |

proving the theorem. ∎

## 3 An open problem

We now turn to some explicit examples of union-closed families containing small sets for which we have been unable to establish the Union-Closed Conjecture. For simplicity, we concentrate on the most striking case, when the family contains a set of size 3, and indeed is generated by sets of size 3.

Our families live on ground-set ℤ n 2 \mathbb{Z}_{n}^{2}, the n × n n\times n torus.

###### Question 3.

Let n ∈ ℕ n\in\mathbb{N} and let R ⊂ ℤ n R\subset\mathbb{Z}_{n} with | R | = 3 |R|=3. Does the Union-Closed Conjecture hold for the union-closed family ℱ \mathcal{F} of subsets of ℤ n 2 \mathbb{Z}_{n}^{2} generated by all the translates of R × { 0 } R\times\{0\} and of { 0 } × R \{0\}\times R?

(Here, as usual, we say a union-closed family ℱ \mathcal{F} is generated by a family 𝒢 \mathcal{G} if it consists of all unions of sets in 𝒢 \mathcal{G}.)

Perhaps the most interesting case is when n n is prime. In that case we may assume that R = { 0, 1, r } R=\{0,1,r\} for some r r, and so one feels that the verification of the Union-Closed Conjecture should be a triviality, but it seems not to be. Note that all the families in Question 3 are transitive families, in the sense that all points ‘look the same’, so that the Union-Closed Conjecture is equivalent to the assertion that the average size of the sets in the family is at least n 2 / 2 n^{2}/2.

We mention that the corresponding result in ℤ n \mathbb{Z}_{n} (in other words, the union-closed family on ground-set ℤ n \mathbb{Z}_{n} generated by translates of R R) is known to hold: this is proved in [1].

We have verified the special case of Question 3 where R = { 0, 1, 2 } R=\{0,1,2\}. A sketch of the proof is as follows. Assume that n ≥ 6 n\geq 6, and let ℱ ⊂ 𝒫 ⁡ ( ℤ n 2) \mathcal{F}\subset\mathcal{P}(\mathbb{Z}_{n}^{2}) be the union-closed family generated by all translates of { 0, 1, 2 } × { 0 } \{0,1,2\}\times\{0\} and of { 0 } × { 0, 1, 2 } \{0\}\times\{0,1,2\} (we call these translates 3-tiles, for brevity). Let C = { 0, 1, 2, 3 } 2 C=\{0,1,2,3\}^{2}, a 4 × 4 4\times 4 square. Consider the bipartite graph H = ( 𝒳, 𝒴) H=(\mathcal{X},\mathcal{Y}) with vertex-classes 𝒳 \mathcal{X} and 𝒴 \mathcal{Y}, where 𝒳 \mathcal{X} consists of all subsets of C C with size less than 8 that are intersections with C C of sets in ℱ \mathcal{F}, 𝒴 \mathcal{Y} consists of all subsets of C C with size greater than 8 that are intersections with C C of sets in ℱ \mathcal{F}, and we join S ∈ 𝒳 S\in\mathcal{X} to S ′ ∈ 𝒴 S^{\prime}\in\mathcal{Y} if | S ′ | + | S | ≥ 16 |S^{\prime}|+|S|\geq 16 and S ′ = S ∪ U S^{\prime}=S\cup U for some union U U of 3-tiles that are contained within C C. It can be verified (by computer) that H H has a matching m: 𝒳 → 𝒴 m:\mathcal{X}\to\mathcal{Y} of size | 𝒳 | = 16520 |\mathcal{X}|=16520. Such a matching m m gives rise to an injection

 | f: { S ∈ ℱ: | S ∩ C | < | C | / 2 } → { S ∈ ℱ: | S ∩ C | > | C | / 2 } f:\{S\in\mathcal{F}:\ |S\cap C|<|C|/2\}\to\{S\in\mathcal{F}:\ |S\cap C|>|C|/2\} |  |

given by

 | f ⁡ ( S) = ( S ∖ C) ∪ m ⁡ ( S ∩ C) \quad f(S)=(S\setminus C)\cup m(S\cap C) |  |

with the property that | S ∩ C | + | f ⁡ ( S) ∩ C | ≥ | C | |S\cap C|+|f(S)\cap C|\geq|C| for all S ∈ ℱ S\in\mathcal{F} with | S ∩ C | < | C | / 2 |S\cap C|<|C|/2. It follows that a uniformly random subset of ℱ \mathcal{F} has intersection with | C | |C| of expected size at least | C | / 2 |C|/2, which in turn implies that there is an element of C C with frequency at least 1 / 2 1/2 (and in fact, since ℱ \mathcal{F} is transitive, every element has frequency at least 1/2).

We remark that this proof does not work if one tries to replace C = { 0, 1, 2, 3 } 2 C=\{0,1,2,3\}^{2} by { 0, 1, 2 } 2 \{0,1,2\}^{2}, as the resulting bipartite graph H ′ = ( 𝒳 ′, 𝒴 ′) H^{\prime}=(\mathcal{X}^{\prime},\mathcal{Y}^{\prime}) does not contain a matching of size | 𝒳 ′ | |\mathcal{X}^{\prime}|.

We remark also that it would be nice to find a non-computer proof of the above result.

Acknowledgement: We are very grateful to Igor Balla for bringing the papers [2] and [12] to our attention.

## References

- [1] J. Aaronson, D. Ellis and I. Leader, A note on transitive union-closed families. Electronic J. Combin. 28 (2021), P2.3.
- [2] I. Balla, Minimum density of union-closed families. Preprint. arXiv:1106.0369.
- [3] I. Balla, B. Bollobás and T. Eccles, Union-closed families of sets. J. Combin. Theory (Series A) 120 (2013), 531–544.
- [4] H. Bruhn and O. Schaudt, The journey of the union-closed sets conjecture. Graphs Combin. 31 (2015), 2043–2074.
- [5] D. Duffus, in: I. Rival (Ed.), Graphs and Order. Reidel, Dordrecht, Boston, 1985, p. 525.
- [6] I. Karpas, Two results on union-closed families. Preprint, August 2017. arXiv:1708.01434.
- [7] Polymath11: Frankl’s Union-Closed Conjecture.
https://gowers.wordpress.com/2016/01/29/func1-strengthenings-variants-potential-counterexamples/.
- [8] B. Poonen, Union-closed families. J. Combin. Theory (Series A) 59 (1992), 253–268.
- [9] I. Roberts and J. Simpson, A note on the union-closed sets conjecture. Australas. J. Combin. 47 (2010), 265–267.
- [10] D.G. Sarvate and J.-C. Renaud, Improved bounds for the union-closed sets conjecture. Ars Combin. 29 (1990), 181–185.
- [11] B. Vučković and M. Živković, The 12-element case of Frankl’s conjecture. IPSI Transactions on Advanced Research, January 2017, Paper 9.
- [12] P. Wójcik, Density of union-closed families. Discrete Math. 105 (1992), 259–267.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
