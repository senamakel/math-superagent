<!-- source: https://arxiv.org/html/2606.23721v2 | converted from HTML -->

Holes in Valid-Extension Sets of Finite Gilbreath Sequences

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2606.23721v2 [math.CO] 16 Jul 2026

# Holes in Valid-Extension Sets of Finite Gilbreath Sequences

Leila Muney

###### Abstract

Given a finite sequence of integers, form its difference triangle by repeatedly taking absolute differences of consecutive entries. We call the sequence *Gilbreath*if the leftmost entry of every row below the top is 1 1. The Gilbreath conjecture, which remains open, asserts that every initial segment of the primes is a Gilbreath sequence.

This paper studies the local extension problem: given a Gilbreath sequence, which integers can be appended to it while preserving the Gilbreath property? We call the set of such admissible values the *valid-extension set*of the sequence. A previously proposed characterization in the literature predicts that this set always fills a natural parity interval around the last term. We show that this fails in general: the valid-extension set can have interior holes, with the smallest failure occurring at length 5 5 for the sequence ( 2, 3, 5, 9, 15) (2,3,5,9,15).

The paper develops a corrected extension set theory. We give an exact criterion for membership in the valid-extension set, an algorithm that computes it, and a sharp condition determining exactly when the set fills the candidate interval. This last condition is an order-sensitive analogue of the classical Brown completeness criterion for subset sums. We also establish endpoint validity and reflection symmetry, determine the exact minimum size of the valid-extension set together with its unique minimizer, exhibit a family whose valid-extension set has exponentially many components, and provide enumeration data through length 11 11.

## 1 Introduction

Given a finite integer sequence S = ( s 1, …, s n) S=(s_{1},\ldots,s_{n}), its *difference triangle*is defined by s a 0:= s a s_{a}^{0}:=s_{a} and

 | s a b:= | s a + 1 b − 1 − s a b − 1 | for ​ b ≥ 1, 1 ≤ a ≤ n − b. s_{a}^{b}:=\left|s_{a+1}^{b-1}-s_{a}^{b-1}\right|\quad\text{for }b\geq 1,\ 1\leq a\leq n-b. |  |

The sequence is *Gilbreath*if s 1 b = 1 s_{1}^{b}=1 for every 1 ≤ b ≤ n − 1 1\leq b\leq n-1. Figure 1 depicts the construction of the triangle for n = 5 n=5.

 | s 1 s 2 s 3 s 4 s 5 s 1 1 s 2 1 s 3 1 s 4 1 s 1 2 s 2 2 s 3 2 s 1 3 s 2 3 s 1 4 \begin{array}[]{ccccc}s_{1}&s_{2}&s_{3}&s_{4}&s_{5}\\[6.00006pt] &s_{1}^{1}&s_{2}^{1}&s_{3}^{1}&s_{4}^{1}\\[6.00006pt] &&s_{1}^{2}&s_{2}^{2}&s_{3}^{2}\\[6.00006pt] &&&s_{1}^{3}&s_{2}^{3}\\[6.00006pt] &&&&s_{1}^{4}\end{array} |  |

Figure 1: Difference triangle of an arbitrary sequence of length n = 5 n=5. The sequence is Gilbreath if and only if s 1 1 = s 1 2 = s 1 3 = s 1 4 = 1 s_{1}^{1}=s_{1}^{2}=s_{1}^{3}=s_{1}^{4}=1.

The iterated absolute-difference triangle was first studied by Proth and rediscovered by Gilbreath in the context of the prime sequence. Computer experiments by Killgrove and Ralston [14] and most extensively by Odlyzko [16], the latter for primes up to 10 13 10^{13} (about 3.4 × 10 11 3.4\times 10^{11} primes), provide substantial numerical evidence that initial segments of the primes are Gilbreath. The assertion that this property holds for every initial segment of the primes is known as *Gilbreath’s conjecture*, and remains open. It is recorded as Problem A10 in Guy [13] and as Appendix Problem 68 in Montgomery [15].

The features of the prime sequence responsible for the Gilbreath property have been investigated through several lenses. Croft, reported by Gardner [10], observed that the property does not seem to depend on primality in any deep sense: he conjectured that any sequence beginning with 2 2, continuing with odd numbers, and having sufficiently small gaps should be Gilbreath. This small-gap heuristic was later formalized in probabilistic form by Chase [7], who proved that sequences beginning 2, 3 2,3 with random small gaps are almost surely Gilbreath.

Our finite family 𝒢 n \mathcal{G}_{n} (defined below) is naturally aligned with this small-gap perspective, but the results in this paper do not address the Gilbreath conjecture directly. Instead, we focus on a finite, local question: *given a Gilbreath sequence, which integers can be appended to it while preserving the Gilbreath property?*

For a Gilbreath sequence S S, the *valid extension set*is

 | K S:= { k ∈ ℤ: ( s 1, …, s n, k) ​ is Gilbreath }. K_{S}:=\{k\in\mathbb{Z}:(s_{1},\ldots,s_{n},k)\text{ is Gilbreath}\}. |  |

We call the cardinality | K S | |K_{S}| the *extension width*of S S. We work with the family

 | 𝒢 n:= { S = ( s 1, …, s n): S ​ is strictly increasing, Gilbreath, and ​ ( s 1, s 2) = ( 2, 3) }. \mathcal{G}_{n}:=\{S=(s_{1},\ldots,s_{n}):S\text{ is strictly increasing, Gilbreath, and }(s_{1},s_{2})=(2,3)\}. |  |

The choice ( s 1, s 2) = ( 2, 3) (s_{1},s_{2})=(2,3) is arbitrary: a shift argument (Section 7.1) shows that | K S | |K_{S}| and the structure of K S K_{S} depend only on the gap sequence, so all results extend to the shifted family with initial pair ( a, a + 1) (a,a+1) for any integer a a.

### 1.1 Note on a previously claimed interval characterization

Gatti [11] introduces a nested-absolute-value equation

 | | s 1 n − 1 − | s 2 n − 2 − | ⋯ − | s n − k | − ⋯ | | | = 1 \left|s_{1}^{n-1}-\left|s_{2}^{n-2}-\left|\cdots-|s_{n}-k|\cdots\right|\right|\right|=1 |  |

characterizing membership of k k in K S K_{S}, and proposes to unfold this into an independently signed sum

 | k = ± s 1 n − 1 ± s 2 n − 2 ± ⋯ ± s n − 1 1 + s n ± 1, k=\pm s_{1}^{n-1}\pm s_{2}^{n-2}\pm\cdots\pm s_{n-1}^{1}+s_{n}\pm 1, |  |

treating the n n signs as freely chosen in { + 1, − 1 } \{+1,-1\}. However, the signs in this unfolding are not independent in general; some independent sign choices produce values that do not return a Gilbreath sequence when appended to S S. Gatti [11] further claims that the set of all possible values attainable from this formula produces a parity interval that is equal to K S K_{S}. We show in Section 5 that this is not the case: the signed formula can both miss values in the candidate interval and include values that are not valid extensions.

The present paper develops a corrected extension-set theory. We give an exact algorithm for K S K_{S}, clarify the relationship between the signed-sum set of [11], the candidate interval C S C_{S}, and the true valid-extension set K S K_{S}, identify the surviving features (endpoint validity, parity, and reflection symmetry), characterize precisely when K S = C S K_{S}=C_{S}, and study the extremal and disconnectedness behavior of K S K_{S}.

### 1.2 Notation guide

For ease of reference, we collect the main notation used throughout the paper below.

𝒢 n \mathcal{G}_{n}

Strictly increasing Gilbreath sequences of length n n beginning with ( 2, 3) (2,3).

K S K_{S}

The valid-extension set: all k ∈ ℤ k\in\mathbb{Z} such that ( S, k) (S,k) is Gilbreath.

K S + K_{S}^{+}

The increasing valid extensions:

 | K S + = { k ∈ K S: k > s n }. K_{S}^{+}=\{k\in K_{S}:k>s_{n}\}. |  |

e i e_{i}

The right anti-diagonal entry

 | e i = s n − i i. e_{i}=s_{n-i}^{i}. |  |

A ⁡ ( S) A(S)

The anti-diagonal sum:

 | A ⁡ ( S) = ∑ i = 1 n − 1 e i. A(S)=\sum_{i=1}^{n-1}e_{i}. |  |

r i r_{i}

The new right-edge entries created after appending a proposed extension k k:

 | r 0 = | k − s n |, r i = | r i − 1 − e i |. r_{0}=|k-s_{n}|,\qquad r_{i}=|r_{i-1}-e_{i}|. |  |

F S F_{S}

The folding map determined by the right anti-diagonal:

 | F S ( d) = | ⋯ | | d − e 1 | − e 2 | ⋯ − e n − 1 |. F_{S}(d)=\left|\cdots\left||d-e_{1}|-e_{2}\right|\cdots-e_{n-1}\right|. |  |

Thus F S ​ ( | k − s n |) = r n − 1 F_{S}(|k-s_{n}|)=r_{n-1}.

C S C_{S}

The candidate set:

 | C S = { k ∈ ℤ: | k − s n | ≤ A ( S) + 1, k ≡ s n ( mod 2) }; C_{S}=\{k\in\mathbb{Z}:|k-s_{n}|\leq A(S)+1,\ k\equiv s_{n}\pmod{2}\}; |  |

the parity-compatible interval of radius A ⁡ ( S) + 1 A(S)+1 around s n s_{n}.

H S H_{S}

The hole set:

 | H S = C S ∖ K S. H_{S}=C_{S}\setminus K_{S}. |  |

h ⁡ ( S) h(S)

The defect:

 | h ⁡ ( S) = | H S | = | C S | − | K S |. h(S)=|H_{S}|=|C_{S}|-|K_{S}|. |  |

S ± S_{\pm}

The signed-sum set obtained by treating the signs in the unfolded absolute-value expression as independent.

W S W_{S}

The weight multiset W S = { e 1, …, e n − 1, 1 } W_{S}=\{e_{1},\ldots,e_{n-1},1\} associated to the signed-sum relaxation.

Σ ⁡ ( W) \Sigma(W)

The set of subset sums of a multiset W W.

D S D_{S}

The valid distance set:

 | D S = { | k − s n |: k ∈ K S }. D_{S}=\{|k-s_{n}|:k\in K_{S}\}. |  |

P e P_{e}

The reverse preimage step for x ↦ | x − e | x\mapsto|x-e|.

T i T_{i}

The unnormalized reverse-tree sets used to compute D S D_{S}.

Q a Q_{a}

The normalized preimage step after dividing by 2 2.

T ~ i, L i, a i \widetilde{T}_{i},L_{i},a_{i}

The normalized reverse-tree sets, interval lengths, and normalized anti-diagonal entries used in the interval-completeness criterion.

L n L_{n}

The minimal sequence

 | ( 2, 3, 5, 7, …, 2 ​ n − 1). (2,3,5,7,\ldots,2n-1). |  |

U n U_{n}

The doubling sequence

 | ( 2, 3, 5, 9, 17, …, 2 n − 1 + 1). (2,3,5,9,17,\ldots,2^{n-1}+1). |  |

V n V_{n}

The component-doubling family from Section 13.

M n M_{n}

The maximum extension width:

 | M n = max S ∈ 𝒢 n ⁡ | K S |. M_{n}=\max_{S\in\mathcal{G}_{n}}|K_{S}|. |  |

m n m_{n}

The minimum extension width:

 | m n = min S ∈ 𝒢 n ⁡ | K S |. m_{n}=\min_{S\in\mathcal{G}_{n}}|K_{S}|. |  |

N n N_{n}

The number of sequences in 𝒢 n \mathcal{G}_{n}:

 | N n = | 𝒢 n |. N_{n}=|\mathcal{G}_{n}|. |  |

### 1.3 Summary of main results

The paper has three main parts. We summarize them here and indicate where the main results are proved.

First, we give an exact criterion for valid extensions. The right anti-diagonal of the difference triangle determines an iterated absolute-value map F S F_{S}, and a proposed extension k k is valid exactly when

 | F S ​ ( | k − s n |) = 1 F_{S}(|k-s_{n}|)=1 |  |

(Proposition 2). This identifies the valid distance set as a fiber of a composition of folding maps and leads to the reverse-tree algorithm for computing K S K_{S} exactly (Proposition 18). The criterion immediately yields the candidate bound K S ⊆ C S K_{S}\subseteq C_{S} (Corollary 3), and a short parity argument gives endpoint validity and reflection symmetry of K S K_{S} (Theorems 15 and 16).

Second, we compare the true extension set with the signed-sum relaxation implicit in [11]. We show that the signed-sum set is an affine image of a subset-sum set associated to the right anti-diagonal (Theorem 12). Thus the question of when the signed sums fill the natural candidate interval C S C_{S} is governed by Brown’s classical criterion for when subset sums fill a full interval. The equality K S = C S K_{S}=C_{S} is more rigid: the signs must be compatible with the ordered nested absolute-value recurrence. Our main structural theorem gives the exact ordered analogue:

 | K S = C S ⟺ e i ≤ 1 + ∑ j > i e j ( 1 ≤ i ≤ n − 2). K_{S}=C_{S}\quad\Longleftrightarrow\quad e_{i}\leq 1+\sum_{j>i}e_{j}\quad(1\leq i\leq n-2). |  |

This is Theorem 20.

Third, we study the consequences of this criterion. We identify the first failure of interval-completeness: for n ≤ 4 n\leq 4 all sequences in 𝒢 n \mathcal{G}_{n} are interval-complete, while at n = 5 n=5 the unique counterexample is ( 2, 3, 5, 9, 15) (2,3,5,9,15), with a single hole at 15 15 (Theorem 24). We determine the minimum possible extension width, showing that it is 5 5 for every n ≥ 3 n\geq 3, uniquely achieved by L n = ( 2, 3, 5, 7, …, 2 ​ n − 1) L_{n}=(2,3,5,7,\ldots,2n-1) (Theorem 25). We also compute the extension width of the doubling sequence U n = ( 2, 3, 5, 9, 17, …, 2 n − 1 + 1) U_{n}=(2,3,5,9,17,\ldots,2^{n-1}+1), obtaining | K U n | = 2 n − 1 + 1 |K_{U_{n}}|=2^{n-1}+1 (Theorem 29); exhaustive computation through n ≤ 10 n\leq 10 shows this value is the maximum extension width in 𝒢 n \mathcal{G}_{n}, giving rise to Conjecture 30. We construct an explicit family V n ∈ 𝒢 n V_{n}\in\mathcal{G}_{n} whose valid-extension set has exactly 2 n − 4 2^{n-4} connected components in the parity lattice (Theorem 35), so the maximum component count over 𝒢 n \mathcal{G}_{n} grows exponentially in n n. Finally, we give enumeration data for N n = | 𝒢 n | N_{n}=|\mathcal{G}_{n}| through n ≤ 11 n\leq 11 and extremal data through n ≤ 10 n\leq 10 (Section 14).

### 1.4 Related work

Beyond the historical references in the introduction, the present paper relates to several active threads in additive number theory and combinatorial dynamics.

The signed-sum relaxation arising in this paper connects the extension problem to the classical theory of subset sums and complete sequences. Brown’s criterion gives a necessary and sufficient condition for the subset sums of a finite sequence of nonnegative integers to fill the entire interval from 0 0 to their total sum [4]. This is the finite completeness criterion used in Section 6 to characterize when S ± = C S S_{\pm}=C_{S}. Complete sequences and related subset-sum questions also appear in the Erdős line of additive number theory: Burr and Erdős studied Ramsey-type completeness properties [5], and Conlon, Fox, and Pham recently resolved several problems on subset sums, completeness, and colorings, including questions of Burr and Erdős [9]. In this terminology, the classical completeness criterion governs when the signed sums fill the candidate interval. Our main interval-completeness theorem identifies a strictly stronger order-sensitive condition governing when the true valid-extension set fills the interval. The gap between these two conditions captures the consistency required by the nested absolute-value structure.

Chase [7], mentioned in the introduction, formalizes Croft’s small-gap heuristic in probabilistic form. Like ours, Chase’s model fixes the starting point 2, 3 2,3 and treats subsequent entries as free, but the questions are different: Chase studies probabilistic eventual Gilbreath behavior, whereas we study the local finite extension problem of determining exactly which next values preserve the Gilbreath property. More recently, Chase, Hunter, and Tao [8] combine probabilistic and deterministic approaches to Gilbreath’s conjecture, proving a Cram’er random-model analogue and establishing a deterministic inverse theorem that identifies the principal obstructions to the Gilbreath property under suitable assumptions on prime gaps. Their work seeks to understand global mechanisms governing Gilbreath’s conjecture, whereas our focus is complementary: we develop an exact structural theory of the finite valid-extension set K S K_{S}, giving complete characterizations, algorithms, and extremal results for the local extension problem.

Granville [12] also studies Gilbreath’s conjecture from a global perspective, developing a framework based on sieving, reverse sieving, and equivalence classes of finite sequences to reduce the conjecture to a collection of representative cases. While his approach likewise aims to understand the conjecture itself, our work instead analyzes the finite extension problem for a fixed Gilbreath sequence, characterizing the exact set of admissible next values and the combinatorial structure of the resulting valid-extension set K S K_{S}.

Bhat, Cobeli, and Zaharescu [2] study the same Proth–Gilbreath triangle as a discrete dynamical system, introducing the operator Υ \Upsilon that sends the top row to the left edge and analyzing its six-fold “helicoidal” iteration, an associated 𝔽 2 ​ [[X]] \mathbb{F}_{2}[[X]] involution T ⁡ ( f) ​ ( X) = f ⁡ ( X / ( 1 + X)) ⋅ ( 1 + X) − 1 T(f)(X)=f\!\big(X/(1+X)\big)\cdot(1+X)^{-1}, and the statistical distribution of 0 0 ’s and nonzero entries along rays parallel to an edge. Their padding construction ( [2, Prop. 3.1]) builds a triangle backwards from a prescribed southern vertex by choosing eastern-edge values. This is reminiscent of our reverse-tree process (Section 8), but the inverse problem is different: their construction pads the *eastern*edge to realize a single target apex, whereas our reverse tree runs up the *right anti-diagonal*from the apex value 1 1 to enumerate the entire valid-extension set K S K_{S}. Equivalently, our valid distance set is the fiber over 1 1 of an ordered composition of folding maps x ↦ | x − e i | x\mapsto|x-e_{i}|, with the fold parameters supplied by the right anti-diagonal. Earlier work in this dynamical direction includes the Proth–Gilbreath analogue of Caragiu, Zaharescu, and Zaki [6] and the quasi-periodicity study of Bhat, Cobeli, and Zaharescu [3].

Agama [1] reformulates Gilbreath’s conjecture through a “gap sequence / path / circuit” framework. While both Agama’s paper and ours provide a finite structural reframing, our machinery and goals are different. Agama examines gap sequences through path combinatorics, while we examine the combinatorial and additive structure of the extension set of a fixed finite sequence.

It is important to note that the counts N n = | 𝒢 n | N_{n}=|\mathcal{G}_{n}| coincide (after an index shift) with OEIS sequence [20], where a comment of T. D. Noe already identifies that the slowest- and fastest-growing length- n n Gilbreath sequences are the minimal sequence L n = ( 2, 3, 5, 7, …, 2 ​ n − 1) L_{n}=(2,3,5,7,\ldots,2n-1) and the doubling sequence ( 2, 3, 5, 9, 17, …) (2,3,5,9,17,\ldots), respectively. Our minimum extension-width theorem (Theorem 25) and doubling-sequence extension-width formula (Theorem 29) show that these sequences are also extremal for extension width: the minimal sequence is the unique minimizer for all n ≥ 3 n\geq 3, and exhaustive computation shows that the doubling sequence is the maximizer for n ≤ 10 n\leq 10. We attribute the growth extremizer identification to [20] and claim novelty only for the cardinality formulas of the corresponding K S K_{S} and the general structural theory.

For clarity, we explicitly state what we do and do not claim as new. We do *not*claim novelty for the enumeration N n = | 𝒢 n | N_{n}=|\mathcal{G}_{n}|, which coincides with OEIS [20], nor for the identification of the minimal sequence and doubling sequence as the extremal-growth sequences, which is stated as a note there. We also do not claim novelty for the classical subset-sum completeness criterion used to analyze S ± S_{\pm}, which is due to Brown [4]. The contributions we believe to be new are the structural theory of the valid-extension set K S K_{S}: the exact membership criterion, the reverse-tree algorithm producing K S K_{S}, the interpretation of K S = C S K_{S}=C_{S} as an ordered folding analogue of classical subset-sum completeness, and the interval-completeness criterion (Theorem 20). We also identify the first hole, prove the exact minimum extension-width theorem with uniqueness (Theorem 25), and identify the structural properties of the exponentially disconnected family V n V_{n} (Theorem 35). The correction to the interval-filling claim of [11] is the conceptual starting point, but the paper develops a broader extension-set theory around it. We note that these originality claims are based on searches in the literature and databases, and we would welcome correction.

For more context on iterated-difference and difference-triangle sequences, see the OEIS discussion in Section 14.1.

## 2 The exact extension criterion

Throughout, for S ∈ 𝒢 n S\in\mathcal{G}_{n} we define the *right anti-diagonal*

 | e i:= s n − i i, 1 ≤ i ≤ n − 1. e_{i}:=s_{n-i}^{i},\qquad 1\leq i\leq n-1. |  |

Thus e 1 = s n − 1 1 = s n − s n − 1 e_{1}=s_{n-1}^{1}=s_{n}-s_{n-1} is the last gap, while e n − 1 = s 1 n − 1 = 1 e_{n-1}=s_{1}^{n-1}=1 is the bottom entry of the triangle. We also set

 | A ⁡ ( S):= ∑ i = 1 n − 1 e i. A(S):=\sum_{i=1}^{n-1}e_{i}. |  |

###### Example 1.

For S = ( 2, 3, 5, 9, 15) S=(2,3,5,9,15), the difference triangle is

 | 2 3 5 9 15 1 2 4 6 1 2 2 1 0 1 \begin{array}[]{rrrrr}2&3&5&9&15\\ &1&2&4&6\\ &&1&2&2\\ &&&1&0\\ &&&&1\end{array} |  |

The left diagonal below the top row is ( 1, 1, 1, 1) (1,1,1,1), so S S is Gilbreath. The right anti-diagonal is

 | ( e 1, e 2, e 3, e 4) = ( 6, 2, 0, 1), (e_{1},e_{2},e_{3},e_{4})=(6,2,0,1), |  |

and A ⁡ ( S) = 9 A(S)=9. Figure 2 highlights these two parts of the triangle.

2 2 3 3 5 5 9 9 15 15 1 1 2 2 4 4 6 6 1 1 2 2 2 2 1 1 0 0 1 1 left diagonal = 1 =1 (Gilbreath) right anti-diagonal both (apex) Figure 2: Anatomy of the difference triangle of S = ( 2, 3, 5, 9, 15) S=(2,3,5,9,15). The left diagonal (red) consists of 1 1 ’s, which is the defining Gilbreath condition. The right anti-diagonal (blue) is ( e 1, e 2, e 3, e 4) = ( 6, 2, 0, 1) (e_{1},e_{2},e_{3},e_{4})=(6,2,0,1). When a proposed extension k k is appended, the new right-edge entries are computed by comparing the previous new entry with these anti-diagonal entries. The bottom apex 1 1 belongs to both structures, since e n − 1 = s 1 n − 1 e_{n-1}=s_{1}^{n-1}.

The right anti-diagonal determines a composition of folding maps. Define

 | F S: ℤ ≥ 0 → ℤ ≥ 0, F S ( d):= | ⋯ | | d − e 1 | − e 2 | ⋯ − e n − 1 |. F_{S}:\mathbb{Z}_{\geq 0}\to\mathbb{Z}_{\geq 0},\qquad F_{S}(d):=\left|\cdots\left||d-e_{1}|-e_{2}\right|\cdots-e_{n-1}\right|. |  |

Here the entries e 1, e 2, …, e n − 1 e_{1},e_{2},\ldots,e_{n-1} are applied in their fixed anti-diagonal order. This order is part of the structure; unlike the signed-sum relaxation studied later, the fold parameters cannot be sorted or chosen independently.

Given a proposed extension k k, set

 | r 0:= | k − s n | r_{0}:=|k-s_{n}| |  |

and then recursively

 | r i:= | r i − 1 − e i |, 1 ≤ i ≤ n − 1. r_{i}:=|r_{i-1}-e_{i}|,\qquad 1\leq i\leq n-1. |  |

Thus r 0 r_{0} is the new entry created in row 1 1 after appending k k, r 1 r_{1} is the new entry created in row 2 2, and so on. Equivalently, if d = | k − s n | d=|k-s_{n}|, then

 | F S ​ ( d) = r n − 1. F_{S}(d)=r_{n-1}. |  |

In particular, F S ​ ( | k − s n |) F_{S}(|k-s_{n}|) is the new bottom entry of the extended triangle.

The following criterion is essentially bookkeeping: appending k k only creates one new right-edge entry in each row, and those entries are exactly the r i r_{i} ’s.

###### Proposition 2 (Iterated absolute-value criterion).

Let S ∈ 𝒢 n S\in\mathcal{G}_{n} and k ∈ ℤ k\in\mathbb{Z}. Then

 | k ∈ K S ⟺ F S ( | k − s n |) = 1. k\in K_{S}\quad\Longleftrightarrow\quad F_{S}(|k-s_{n}|)=1. |  |

Equivalently, with r 0, …, r n − 1 r_{0},\ldots,r_{n-1} defined as above,

 | k ∈ K S ⟺ r n − 1 = 1. k\in K_{S}\quad\Longleftrightarrow\quad r_{n-1}=1. |  |

###### Proof.

Appending k k to S S creates one new entry on the right side of each row of the difference triangle. The new entry in row 1 1 is

 | r 0 = | k − s n |. r_{0}=|k-s_{n}|. |  |

If the new entry in row i i is r i − 1 r_{i-1}, then the old rightmost entry in that row is e i e_{i}, so the new entry in the next row is

 | | r i − 1 − e i | = r i. |r_{i-1}-e_{i}|=r_{i}. |  |

Therefore r n − 1 = F S ​ ( | k − s n |) r_{n-1}=F_{S}(|k-s_{n}|) is exactly the new bottom entry of the extended triangle. Since all old entries are unchanged, the extended sequence is Gilbreath if and only if this new bottom entry is 1 1. ∎

It is useful to record the corresponding fiber interpretation. If

 | D S:= { | k − s n |: k ∈ K S } D_{S}:=\{|k-s_{n}|:k\in K_{S}\} |  |

is the valid distance set, then Proposition 2 gives

 | D S = { d ∈ ℤ ≥ 0: F S ​ ( d) = 1 }. D_{S}=\{d\in\mathbb{Z}_{\geq 0}:F_{S}(d)=1\}. |  |

Thus the extension problem is an inverse problem for a finite composition of folding maps x ↦ | x − e i | x\mapsto|x-e_{i}|. The reverse-tree algorithm in Section 8 computes this fiber exactly.

###### Corollary 3 (Candidate bound).

If k ∈ K S k\in K_{S}, then

 | | k − s n | ≤ A ⁡ ( S) + 1. |k-s_{n}|\leq A(S)+1. |  |

###### Proof.

Let

 | d:= | k − s n |. d:=|k-s_{n}|. |  |

Suppose

 | d > A ⁡ ( S) + 1 = e 1 + ⋯ + e n − 1 + 1. d>A(S)+1=e_{1}+\cdots+e_{n-1}+1. |  |

We show that no sign flip occurs while computing the r i r_{i} ’s. Since r 0 = d r_{0}=d, the claim is true at the beginning. If

 | r i − 1 = d − ( e 1 + ⋯ + e i − 1), r_{i-1}=d-(e_{1}+\cdots+e_{i-1}), |  |

then

 | r i − 1 > e i + e i + 1 + ⋯ + e n − 1 + 1 ≥ e i. r_{i-1}>e_{i}+e_{i+1}+\cdots+e_{n-1}+1\geq e_{i}. |  |

Hence

 | r i = | r i − 1 − e i | = r i − 1 − e i = d − ( e 1 + ⋯ + e i). r_{i}=|r_{i-1}-e_{i}|=r_{i-1}-e_{i}=d-(e_{1}+\cdots+e_{i}). |  |

By induction,

 | r n − 1 = d − ( e 1 + ⋯ + e n − 1) = d − A ⁡ ( S) > 1. r_{n-1}=d-(e_{1}+\cdots+e_{n-1})=d-A(S)>1. |  |

Thus F S ​ ( d) = r n − 1 ≠ 1 F_{S}(d)=r_{n-1}\neq 1, so k ∉ K S k\notin K_{S}. Taking the contrapositive gives the desired bound. ∎

## 3 Parity

The right-adjusted display of the difference triangle is most naturally read along diagonals rather than columns. For fixed a a, the entries

 | s a, s a 1, s a 2, …, s a n − a s_{a},\ s_{a}^{1},\ s_{a}^{2},\ \ldots,\ s_{a}^{n-a} |  |

form one diagonal of the triangle. The first diagonal is special: s 1 = 2 s_{1}=2 is even, while the Gilbreath condition says

 | s 1 1 = s 1 2 = ⋯ = s 1 n − 1 = 1. s_{1}^{1}=s_{1}^{2}=\cdots=s_{1}^{n-1}=1. |  |

Thus the first diagonal has parity pattern

 | even, odd, odd, …, odd. \text{even},\ \text{odd},\ \text{odd},\ \ldots,\ \text{odd}. |  |

###### Lemma 4.

For every S = ( s 1, …, s n) ∈ 𝒢 n S=(s_{1},\ldots,s_{n})\in\mathcal{G}_{n}, every term s a s_{a} with a ≥ 2 a\geq 2 is odd, and every positive-row entry s a b s_{a}^{b} with a ≥ 2 a\geq 2 and b ≥ 1 b\geq 1 is even. Equivalently, every diagonal after the first begins with an odd entry and then consists entirely of even entries. In particular,

 | e 1, e 2, …, e n − 2 e_{1},e_{2},\ldots,e_{n-2} |  |

are even, while

 | e n − 1 = 1. e_{n-1}=1. |  |

We note that this lemma is also stated in [11]. We include a proof for completeness.

###### Proof.

We work modulo 2 2. Since signs and absolute values do not matter modulo 2 2, the recurrence

 | s a b = | s a + 1 b − 1 − s a b − 1 | s_{a}^{b}=\left|s_{a+1}^{b-1}-s_{a}^{b-1}\right| |  |

becomes

 | s a b ≡ s a b − 1 + s a + 1 b − 1 ( mod 2). s_{a}^{b}\equiv s_{a}^{b-1}+s_{a+1}^{b-1}\pmod{2}. |  |

Equivalently,

 | s a + 1 b − 1 ≡ s a b + s a b − 1 ( mod 2). s_{a+1}^{b-1}\equiv s_{a}^{b}+s_{a}^{b-1}\pmod{2}. |  |

Thus, once one diagonal

 | s a, s a 1, s a 2, … s_{a},\ s_{a}^{1},\ s_{a}^{2},\ldots |  |

is known modulo 2 2, the next diagonal is obtained by adding adjacent entries on that diagonal.

The first diagonal is known: s 1 = 2 s_{1}=2 is even, and the Gilbreath condition gives

 | s 1 1 = s 1 2 = ⋯ = s 1 n − 1 = 1. s_{1}^{1}=s_{1}^{2}=\cdots=s_{1}^{n-1}=1. |  |

Thus the first diagonal has parity pattern

 | even, odd, odd, …, odd. \text{even},\ \text{odd},\ \text{odd},\ldots,\text{odd}. |  |

For a triangle of size 5 5, the resulting parity pattern is

 | E O O O O O E E E O E E O E O \begin{array}[]{ccccc}E&O&O&O&O\\ &O&E&E&E\\ &&O&E&E\\ &&&O&E\\ &&&&O\end{array} |  |

where E E denotes even and O O denotes odd.

The general case follows by the same propagation. First, the second diagonal has the desired pattern, since

 | s 2 ≡ s 1 + s 1 1 ≡ E + O ≡ O, s_{2}\equiv s_{1}+s_{1}^{1}\equiv E+O\equiv O, |  |

while for b ≥ 1 b\geq 1,

 | s 2 b ≡ s 1 b + 1 + s 1 b ≡ O + O ≡ E. s_{2}^{b}\equiv s_{1}^{b+1}+s_{1}^{b}\equiv O+O\equiv E. |  |

Now suppose some diagonal a ≥ 2 a\geq 2 begins with an odd entry and has only even entries below it:

 | s a ≡ 1 ( mod 2), s a b ≡ 0 ( mod 2) ( b ≥ 1). s_{a}\equiv 1\pmod{2},\qquad s_{a}^{b}\equiv 0\pmod{2}\quad(b\geq 1). |  |

Then the next diagonal satisfies

 | s a + 1 ≡ s a + s a 1 ≡ 1 + 0 ≡ 1 ( mod 2), s_{a+1}\equiv s_{a}+s_{a}^{1}\equiv 1+0\equiv 1\pmod{2}, |  |

so its top entry is odd. For every b ≥ 1 b\geq 1,

 | s a + 1 b ≡ s a b + 1 + s a b ≡ 0 + 0 ≡ 0 ( mod 2), s_{a+1}^{b}\equiv s_{a}^{b+1}+s_{a}^{b}\equiv 0+0\equiv 0\pmod{2}, |  |

so all lower entries are even. By induction, every diagonal after the first has this pattern.

Finally, e i = s n − i i e_{i}=s_{n-i}^{i}. For 1 ≤ i ≤ n − 2 1\leq i\leq n-2, the entry e i e_{i} lies below the top of one of the later diagonals, so it is even. The last anti-diagonal entry is

 | e n − 1 = s 1 n − 1 = 1 e_{n-1}=s_{1}^{n-1}=1 |  |

by the Gilbreath condition. ∎

###### Corollary 5.

For every S ∈ 𝒢 n S\in\mathcal{G}_{n}, every k ∈ K S k\in K_{S} satisfies

 | k ≡ s n ( mod 2). k\equiv s_{n}\pmod{2}. |  |

In the normalization s 1 = 2 s_{1}=2, every k ∈ K S k\in K_{S} is odd.

###### Proof.

Let k ∈ K S k\in K_{S}, and define r 0, …, r n − 1 r_{0},\ldots,r_{n-1} as in Section 2. By Proposition 2,

 | r n − 1 = 1, r_{n-1}=1, |  |

which is odd.

Since

 | r n − 1 = | r n − 2 − e n − 1 | r_{n-1}=|r_{n-2}-e_{n-1}| |  |

and e n − 1 = 1 e_{n-1}=1, the value r n − 2 r_{n-2} must be even. For all earlier steps, the entries

 | e 1, e 2, …, e n − 2 e_{1},e_{2},\ldots,e_{n-2} |  |

are even by Lemma 4. Subtracting an even number and taking an absolute value does not change parity. Therefore the parity of

 | r n − 2, r n − 3, …, r 0 r_{n-2},r_{n-3},\ldots,r_{0} |  |

is the same. In particular, r 0 r_{0} is even.

But

 | r 0 = | k − s n |. r_{0}=|k-s_{n}|. |  |

Thus k − s n k-s_{n} is even, so

 | k ≡ s n ( mod 2). k\equiv s_{n}\pmod{2}. |  |

Finally, s n s_{n} is odd by Lemma 4, so every k ∈ K S k\in K_{S} is odd. ∎

## 4 Candidate set, holes, and defect

###### Definition 6.

The *candidate set*of S ∈ 𝒢 n S\in\mathcal{G}_{n} is

 | C S:= { k ∈ ℤ: | k − s n | ≤ A ( S) + 1, k ≡ s n ( mod 2) }. C_{S}:=\{k\in\mathbb{Z}:|k-s_{n}|\leq A(S)+1,\ k\equiv s_{n}\pmod{2}\}. |  |

By Corollary 3 and Corollary 5, K S ⊆ C S K_{S}\subseteq C_{S} always.

###### Lemma 7.

| C S | = A ⁡ ( S) + 2 |C_{S}|=A(S)+2.

###### Proof.

By Lemma 4, e 1, …, e n − 2 e_{1},\ldots,e_{n-2} are even and e n − 1 = 1 e_{n-1}=1, so A ⁡ ( S) A(S) is odd and A ⁡ ( S) + 1 A(S)+1 is even. The interval | k − s n | ≤ A ⁡ ( S) + 1 |k-s_{n}|\leq A(S)+1 restricted to k ≡ s n ( mod 2) k\equiv s_{n}\pmod{2} contains A ⁡ ( S) + 2 A(S)+2 integers. ∎

###### Definition 8.

The *hole set*of S S is H S:= C S ∖ K S H_{S}:=C_{S}\setminus K_{S}, and the *defect*is h ⁡ ( S):= | H S | = A ⁡ ( S) + 2 − | K S | h(S):=|H_{S}|=A(S)+2-|K_{S}|. We say S S is *interval-complete*if h ⁡ ( S) = 0 h(S)=0 (equivalently, K S = C S K_{S}=C_{S}).

Thus the previously claimed interval characterization is equivalent to the assertion h ⁡ ( S) = 0 h(S)=0 for all S ∈ 𝒢 n S\in\mathcal{G}_{n}. The next sections identify exactly when this holds and the first case where it fails. But first, we examine the signed-sum set proposed by [11].

## 5 The signed-sum set

It is useful to separate two different enlargements of K S K_{S}. Let S ∈ 𝒢 n S\in\mathcal{G}_{n} have right anti-diagonal ( e 1, …, e n − 1) (e_{1},\ldots,e_{n-1}), and define the *signed-sum set*originally defined by [11] to be

 | S ±:= { s n + ϵ 1 e 1 + ⋯ + ϵ n − 1 e n − 1 + ϵ n: ϵ 1, …, ϵ n ∈ { ± 1 } }. S_{\pm}:=\left\{s_{n}+\epsilon_{1}e_{1}+\cdots+\epsilon_{n-1}e_{n-1}+\epsilon_{n}:\epsilon_{1},\ldots,\epsilon_{n}\in\{\pm 1\}\right\}. |  |

This is the set obtained by treating all signs in the unfolded expression as independent.

Every valid extension lies in this signed-sum set. Indeed, if k ∈ K S k\in K_{S}, then the chain

 | r 0 = | k − s n |, r i = | r i − 1 − e i | r_{0}=|k-s_{n}|,\qquad r_{i}=|r_{i-1}-e_{i}| |  |

ends at r n − 1 = 1 r_{n-1}=1. Unfolding the absolute values along this actual chain determines a consistent choice of signs, and hence expresses k k as an element of S ± S_{\pm}. Thus

 | K S ⊆ S ±. K_{S}\subseteq S_{\pm}. |  |

On the other hand, every element of S ± S_{\pm} has the correct parity and lies within distance A ⁡ ( S) + 1 A(S)+1 of s n s_{n}, so

 | S ± ⊆ C S. S_{\pm}\subseteq C_{S}. |  |

Therefore

 | K S ⊆ S ± ⊆ C S. K_{S}\subseteq S_{\pm}\subseteq C_{S}. |  |

Both containments can be strict, and they fail for different reasons. The containment S ± ⊆ C S S_{\pm}\subseteq C_{S} may be strict because signed sums need not realize every parity-compatible value in the interval. The containment K S ⊆ S ± K_{S}\subseteq S_{\pm} may be strict because an arbitrary independent choice of signs need not be consistent with the intermediate values in the nested absolute-value recurrence.

###### Example 9 (The signed sums need not fill the candidate interval).

Let

 | S = ( 2, 3, 5, 9, 15). S=(2,3,5,9,15). |  |

Then the right anti-diagonal is

 | ( e 1, e 2, e 3, e 4) = ( 6, 2, 0, 1), (e_{1},e_{2},e_{3},e_{4})=(6,2,0,1), |  |

so

 | A ⁡ ( S) = 9 A(S)=9 |  |

and

 | C S = { 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25 }. C_{S}=\{5,7,9,11,13,15,17,19,21,23,25\}. |  |

The signed-sum offsets from s n = 15 s_{n}=15 are

 | ± 6 ± 2 ± 0 ± 1 ± 1. \pm 6\pm 2\pm 0\pm 1\pm 1. |  |

These produce

 | { − 10, − 8, − 6, − 4, − 2, 2, 4, 6, 8, 10 }, \{-10,-8,-6,-4,-2,2,4,6,8,10\}, |  |

but not 0 0. Hence

 | S ± = { 5, 7, 9, 11, 13, 17, 19, 21, 23, 25 } = C S ∖ { 15 }. S_{\pm}=\{5,7,9,11,13,17,19,21,23,25\}=C_{S}\setminus\{15\}. |  |

In this example the signed-sum set coincides with the true valid-extension set:

 | S ± = K S, S_{\pm}=K_{S}, |  |

but it does not coincide with the full candidate interval C S C_{S}. Thus the interval-filling conclusion does not follow merely from the existence of a signed-sum expression.

###### Example 10 (The signed sums can contain invalid extensions).

Let

 | S = ( 2, 3, 5, 9, 17, 19). S=(2,3,5,9,17,19). |  |

The right anti-diagonal is

 | ( e 1, e 2, e 3, e 4, e 5) = ( 2, 6, 2, 0, 1), (e_{1},e_{2},e_{3},e_{4},e_{5})=(2,6,2,0,1), |  |

so A ⁡ ( S) = 11 A(S)=11, and the candidate set is

 | C S = { 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31 }. C_{S}=\{7,9,11,13,15,17,19,21,23,25,27,29,31\}. |  |

In this case the signed sums do fill the whole candidate interval:

 | S ± = C S. S_{\pm}=C_{S}. |  |

However, the true valid-extension set is smaller:

 | K S = { 7, 9, 11, 13, 15, 19, 23, 25, 27, 29, 31 }. K_{S}=\{7,9,11,13,15,19,23,25,27,29,31\}. |  |

Thus

 | S ± ∖ K S = { 17, 21 }. S_{\pm}\setminus K_{S}=\{17,21\}. |  |

The values 17 17 and 21 21 arise from some independent choices of signs, but those choices are not compatible with the nested absolute-value recurrence. Therefore the signed-sum set can contain false positives even when it fills the entire candidate interval.

These examples show that the signed-sum set and the candidate interval play different roles. The signed-sum set S ± S_{\pm} is an intermediate superset of the true valid-extension set K S K_{S}, while the candidate interval C S C_{S} is a still coarser parity-and-size bound. The reverse-tree algorithm in Section 8 computes K S K_{S} exactly by enforcing the missing consistency conditions.

## 6 Signed sums and subset-sum completeness

The signed-sum set S ± S_{\pm} has a useful reformulation in the language of subset sums. This reformulation explains exactly which part of the extension problem is classical and which part is new. The equality S ± = C S S_{\pm}=C_{S} is a standard complete-sequence question: do the subset sums of a certain multiset fill the entire interval from 0 0 to their total sum? The equality K S = C S K_{S}=C_{S}, by contrast, is more rigid: it asks for the same interval-filling phenomenon under the fixed order imposed by the nested absolute values.

For a finite multiset W = { w 1, …, w m } W=\{w_{1},\ldots,w_{m}\} of nonnegative integers, write

 | Σ ⁡ ( W):= { ∑ i ∈ I w i: I ⊆ { 1, …, m } } \Sigma(W):=\left\{\sum_{i\in I}w_{i}:I\subseteq\{1,\ldots,m\}\right\} |  |

for its set of subset sums, with multiplicities respected. We use the following classical criterion of Brown [4]. Zero weights do not affect Σ ⁡ ( W) \Sigma(W), so the usual positive-sequence form of Brown’s criterion applies after deleting zeros; we state the equivalent nonnegative multiset form. Related complete-sequence questions, including Ramsey-type versions originating with Burr and Erdős, remain active in additive and combinatorial number theory [5, 9].

###### Theorem 11 (Classical completeness criterion).

Let W = { w 1, …, w m } W=\{w_{1},\ldots,w_{m}\} be a finite multiset of nonnegative integers, listed in nondecreasing order

 | 0 ≤ w 1 ≤ w 2 ≤ ⋯ ≤ w m, 0\leq w_{1}\leq w_{2}\leq\cdots\leq w_{m}, |  |

and let T = w 1 + ⋯ + w m T=w_{1}+\cdots+w_{m}. Then

 | Σ ⁡ ( W) = { 0, 1, …, T } \Sigma(W)=\{0,1,\ldots,T\} |  |

if and only if

 | w j ≤ 1 + ∑ i < j w i for every ​ 1 ≤ j ≤ m. w_{j}\leq 1+\sum_{i<j}w_{i}\qquad\text{for every }1\leq j\leq m. |  |

A multiset satisfying this condition will be called *complete*.

###### Proof.

Suppose first that the displayed inequalities hold. We prove by induction on j j that the subset sums of { w 1, …, w j } \{w_{1},\ldots,w_{j}\} fill { 0, 1, …, w 1 + ⋯ + w j } \{0,1,\ldots,w_{1}+\cdots+w_{j}\}. The case j = 0 j=0 is trivial. If the claim holds through j − 1 j-1, set T j − 1 = w 1 + ⋯ + w j − 1 T_{j-1}=w_{1}+\cdots+w_{j-1}. After adding w j w_{j}, the subset sums are the union of

 | { 0, 1, …, T j − 1 } and { w j, w j + 1, …, w j + T j − 1 }. \{0,1,\ldots,T_{j-1}\}\quad\text{and}\quad\{w_{j},w_{j}+1,\ldots,w_{j}+T_{j-1}\}. |  |

The inequality w j ≤ T j − 1 + 1 w_{j}\leq T_{j-1}+1 says exactly that these two intervals overlap or touch, so their union is the full interval { 0, 1, …, T j − 1 + w j } \{0,1,\ldots,T_{j-1}+w_{j}\}.

Conversely, suppose Σ ⁡ ( W) = { 0, 1, …, T } \Sigma(W)=\{0,1,\ldots,T\}. If the inequality failed for some j j, then

 | w j > 1 + ∑ i < j w i. w_{j}>1+\sum_{i<j}w_{i}. |  |

The integer 1 + ∑ i < j w i 1+\sum_{i<j}w_{i} could not be represented as a subset sum: using only weights before w j w_{j} gives at most ∑ i < j w i \sum_{i<j}w_{i}, while using w j w_{j} or any later weight gives at least w j w_{j}. This contradicts completeness. Hence all the inequalities hold. ∎

Given S ∈ 𝒢 n S\in\mathcal{G}_{n} with right anti-diagonal ( e 1, …, e n − 1) (e_{1},\ldots,e_{n-1}), define the associated *weight multiset*

 | W S:= { e 1, e 2, …, e n − 1, 1 }. W_{S}:=\{e_{1},e_{2},\ldots,e_{n-1},1\}. |  |

Let B:= A ⁡ ( S) + 1 B:=A(S)+1. Since e n − 1 = 1 e_{n-1}=1, the value 1 1 appears in W S W_{S} at least twice, and

 | ∑ w ∈ W S w = B. \sum_{w\in W_{S}}w=B. |  |

###### Theorem 12 (Subset-sum reformulation).

Let S ∈ 𝒢 n S\in\mathcal{G}_{n}, and write B = A ⁡ ( S) + 1 B=A(S)+1. Then

 | S ± = { s n − B + 2 ​ t: t ∈ Σ ⁡ ( W S) }. S_{\pm}=\{s_{n}-B+2t:t\in\Sigma(W_{S})\}. |  |

Consequently,

 | S ± = C S ⟺ Σ ( W S) = { 0, 1, …, B }. S_{\pm}=C_{S}\quad\Longleftrightarrow\quad\Sigma(W_{S})=\{0,1,\ldots,B\}. |  |

###### Proof.

Write each ϵ i ∈ { − 1, + 1 } \epsilon_{i}\in\{-1,+1\} uniquely as ϵ i = 2 ​ δ i − 1 \epsilon_{i}=2\delta_{i}-1, with δ i ∈ { 0, 1 } \delta_{i}\in\{0,1\}. Substituting into the definition of S ± S_{\pm},

 | s n + ∑ i = 1 n − 1 ϵ i ​ e i + ϵ n \displaystyle s_{n}+\sum_{i=1}^{n-1}\epsilon_{i}e_{i}+\epsilon_{n} | = s n + ∑ i = 1 n − 1 ( 2 ​ δ i − 1) ​ e i + ( 2 ​ δ n − 1) \displaystyle=s_{n}+\sum_{i=1}^{n-1}(2\delta_{i}-1)e_{i}+(2\delta_{n}-1) |  |

 |  | = s n + 2 ​ ( ∑ i = 1 n − 1 δ i ​ e i + δ n) − ( ∑ i = 1 n − 1 e i + 1) \displaystyle=s_{n}+2\left(\sum_{i=1}^{n-1}\delta_{i}e_{i}+\delta_{n}\right)-\left(\sum_{i=1}^{n-1}e_{i}+1\right) |  |

 |  | = s n − B + 2 ​ t, \displaystyle=s_{n}-B+2t, |  |

where t = ∑ i = 1 n − 1 δ i ​ e i + δ n t=\sum_{i=1}^{n-1}\delta_{i}e_{i}+\delta_{n} is a subset sum of W S W_{S}. As the δ i \delta_{i} range independently over { 0, 1 } \{0,1\}, the value t t ranges over Σ ⁡ ( W S) \Sigma(W_{S}). This proves the first identity.

For the equivalence, note that

 | C S = { s n − B + 2 ​ u: u ∈ { 0, 1, …, B } }, C_{S}=\{s_{n}-B+2u:u\in\{0,1,\ldots,B\}\}, |  |

since C S C_{S} consists of all parity-compatible values in the interval [s n − B, s n + B] [s_{n}-B,s_{n}+B]. Both S ± S_{\pm} and C S C_{S} are images under the injective affine map x ↦ s n − B + 2 ​ x x\mapsto s_{n}-B+2x, so they coincide if and only if Σ ⁡ ( W S) = { 0, 1, …, B } \Sigma(W_{S})=\{0,1,\ldots,B\}. ∎

###### Corollary 13.

The equality S ± = C S S_{\pm}=C_{S} holds if and only if W S W_{S} is complete in the sense of Theorem 11.

Theorem 12 isolates the classical part of the problem. The signed-sum set forgets the order in which the absolute values are evaluated: it only remembers the multiset of fold sizes. By Brown’s criterion, the question S ± = C S S_{\pm}=C_{S} is answered by sorting the weights in W S W_{S} and checking whether each new sorted weight is at most one plus the sum of the preceding sorted weights.

The true valid-extension set is different. A signed expression represents a genuine element of K S K_{S} only if its signs arise from an actual chain

 | r i = | r i − 1 − e i |. r_{i}=|r_{i-1}-e_{i}|. |  |

This chain processes the anti-diagonal entries in their fixed geometric order. Thus the interval-completeness condition for K S K_{S} has the same “no gap” shape as Brown’s criterion, but the order is forced:

 | e i ≤ 1 + ∑ j > i e j. e_{i}\leq 1+\sum_{j>i}e_{j}. |  |

In short, Brown’s condition is a sorted subset-sum completeness criterion, while Theorem 20 below is an ordered folding completeness criterion.

###### Proposition 14 (Hierarchy of completeness conditions).

For every S ∈ 𝒢 n S\in\mathcal{G}_{n}, if K S = C S K_{S}=C_{S}, then W S W_{S} is complete (equivalently, S ± = C S S_{\pm}=C_{S}). The converse fails.

###### Proof.

If K S = C S K_{S}=C_{S}, then the inclusion chain K S ⊆ S ± ⊆ C S K_{S}\subseteq S_{\pm}\subseteq C_{S} forces S ± = C S S_{\pm}=C_{S}. By Corollary 13, this is equivalent to completeness of W S W_{S}.

For the converse, take

 | S = ( 2, 3, 5, 9, 17, 19), S=(2,3,5,9,17,19), |  |

as in Example 10. Its right anti-diagonal is

 | ( e 1, e 2, e 3, e 4, e 5) = ( 2, 6, 2, 0, 1), (e_{1},e_{2},e_{3},e_{4},e_{5})=(2,6,2,0,1), |  |

so

 | W S = { 2, 6, 2, 0, 1, 1 }. W_{S}=\{2,6,2,0,1,1\}. |  |

Sorted, this is ( 0, 1, 1, 2, 2, 6) (0,1,1,2,2,6). The cumulative sums are

 | 0, 1, 2, 4, 6, 12, 0,1,2,4,6,12, |  |

and each entry is at most one plus the sum of the preceding entries. Thus W S W_{S} is complete, so S ± = C S S_{\pm}=C_{S}. However, the ordered criterion of Theorem 20 fails at i = 2 i=2, since

 | e 2 = 6 > 1 + e 3 + e 4 + e 5 = 1 + 2 + 0 + 1 = 4. e_{2}=6>1+e_{3}+e_{4}+e_{5}=1+2+0+1=4. |  |

Therefore K S ≠ C S K_{S}\neq C_{S}. Indeed, Example 10 computes S ± = C S S_{\pm}=C_{S} but K S = C S ∖ { 17, 21 } K_{S}=C_{S}\setminus\{17,21\}. ∎

The classical completeness criterion governs when the signed sums fill the candidate interval. The ordered interval-completeness criterion governs when the true valid-extension set fills the interval. The gap between the two captures the consistency required by the nested absolute-value structure: elements of S ± ∖ K S S_{\pm}\setminus K_{S} are exactly values produced by independent sign choices that cannot occur along any actual folding chain.

## 7 Endpoint validity and symmetry

###### Theorem 15 (Endpoint validity).

For every S ∈ 𝒢 n S\in\mathcal{G}_{n},

 | s n − A ⁡ ( S) − 1 ∈ K S and s n + A ⁡ ( S) + 1 ∈ K S. s_{n}-A(S)-1\in K_{S}\quad\text{and}\quad s_{n}+A(S)+1\in K_{S}. |  |

###### Proof.

Take d = A ⁡ ( S) + 1 = e 1 + e 2 + ⋯ + e n − 1 + 1 d=A(S)+1=e_{1}+e_{2}+\cdots+e_{n-1}+1. We prove by induction on i i that

 | r i = e i + 1 + e i + 2 + ⋯ + e n − 1 + 1 ( 0 ≤ i ≤ n − 1), r_{i}=e_{i+1}+e_{i+2}+\cdots+e_{n-1}+1\qquad(0\leq i\leq n-1), |  |

where the empty sum (at i = n − 1 i=n-1) is 0 0. For i = 0 i=0 this is the definition of d d. Assuming the formula for r i − 1 r_{i-1}, we have

 | r i − 1 = e i + ( e i + 1 + ⋯ + e n − 1 + 1) > e i, r_{i-1}=e_{i}+\big(e_{i+1}+\cdots+e_{n-1}+1\big)>e_{i}, |  |

since the bracketed remainder is at least 1 1. Hence no sign flip occurs and

 | r i = | r i − 1 − e i | = r i − 1 − e i = e i + 1 + ⋯ + e n − 1 + 1. r_{i}=|r_{i-1}-e_{i}|=r_{i-1}-e_{i}=e_{i+1}+\cdots+e_{n-1}+1. |  |

At i = n − 1 i=n-1 this gives r n − 1 = 1 r_{n-1}=1, so both s n + ( A ⁡ ( S) + 1) s_{n}+(A(S)+1) and s n − ( A ⁡ ( S) + 1) s_{n}-(A(S)+1) lie in K S K_{S}. ∎

###### Theorem 16 (Reflection symmetry).

For every S ∈ 𝒢 n S\in\mathcal{G}_{n} and every k ∈ ℤ k\in\mathbb{Z}, k ∈ K S k\in K_{S} iff 2 ​ s n − k ∈ K S 2s_{n}-k\in K_{S}. Hence K S K_{S}, C S C_{S}, and H S H_{S} are symmetric about s n s_{n}.

###### Proof.

k ∈ K S k\in K_{S} depends on k k only through | k − s n | |k-s_{n}|, which is invariant under k ↦ 2 ​ s n − k k\mapsto 2s_{n}-k. ∎

### 7.1 Shift-invariance

For any integer c c, the map S ↦ S + c S\mapsto S+c preserves the entire difference triangle below row 0 0, hence the Gilbreath property and the anti-diagonal. The correspondence k ↔ k + c k\leftrightarrow k+c gives a bijection K S → K S + c K_{S}\to K_{S+c}. Consequently | K S | |K_{S}|, | C S | |C_{S}|, h ⁡ ( S) h(S), the component count, and other purely combinatorial invariants depend only on the gap sequence and are independent of s 1 s_{1}. All results extend verbatim to the shifted family with initial pair ( a, a + 1) (a,a+1) for any integer a a.

## 8 A reverse-tree algorithm

The iterated absolute-value criterion yields a backward algorithm for computing K S K_{S}. Instead of starting with a proposed extension k k and pushing the distance | k − s n | |k-s_{n}| downward through the absolute values, we start at the required final value 1 1 and compute all possible previous values.

In Section 2, we viewed the valid distance set as the fiber F S − 1 ​ ( { 1 }) F_{S}^{-1}(\{1\}). The reverse-tree algorithm computes this fiber by inverting the folds one at a time.

###### Definition 17.

For e ∈ ℤ ≥ 0 e\in\mathbb{Z}_{\geq 0} and T ⊆ ℤ ≥ 0 T\subseteq\mathbb{Z}_{\geq 0}, define the *preimage step*

 | P e ( T):= { e + t: t ∈ T } ∪ { e − t: t ∈ T, e ≥ t }. P_{e}(T):=\{e+t:t\in T\}\cup\{e-t:t\in T,\ e\geq t\}. |  |

This is exactly the set of nonnegative solutions x x to equations of the form | x − e | = t |x-e|=t with t ∈ T t\in T. The branch x = e + t x=e+t is always allowed, whereas the branch x = e − t x=e-t is allowed only when e ≥ t e\geq t. Thus the second branch is not | e − t | |e-t| in general.

###### Proposition 18 (Reverse-tree characterization).

Let T n − 1:= { 1 } T_{n-1}:=\{1\} and recursively T i − 1:= P e i ​ ( T i) T_{i-1}:=P_{e_{i}}(T_{i}) for i = n − 1, n − 2, …, 1 i=n-1,n-2,\ldots,1. Then

 | D S:= { | k − s n |: k ∈ K S } = T 0, D_{S}:=\{|k-s_{n}|:k\in K_{S}\}=T_{0}, |  |

and K S = { s n + d: d ∈ D S } ∪ { s n − d: d ∈ D S } K_{S}=\{s_{n}+d:d\in D_{S}\}\cup\{s_{n}-d:d\in D_{S}\}.

###### Proof.

The condition d = | k − s n | ∈ D S d=|k-s_{n}|\in D_{S} is equivalent to: there exists a nonnegative chain r 0 = d, r 1, …, r n − 1 r_{0}=d,r_{1},\ldots,r_{n-1} with r i = | r i − 1 − e i | r_{i}=|r_{i-1}-e_{i}| and r n − 1 = 1 r_{n-1}=1. Working backward, if r i = t r_{i}=t then the possible values of r i − 1 ≥ 0 r_{i-1}\geq 0 are e i + t e_{i}+t (always) and e i − t e_{i}-t (only when e i ≥ t e_{i}\geq t), so the possible values form exactly P e i ​ ( { t }) P_{e_{i}}(\{t\}). Iterating gives T 0 = D S T_{0}=D_{S}. ∎

###### Example 19 (Reverse tree for S = ( 2, 3, 5, 9, 15) S=(2,3,5,9,15)).

Let S = ( 2, 3, 5, 9, 15) S=(2,3,5,9,15). Its right anti-diagonal is ( e 1, e 2, e 3, e 4) = ( 6, 2, 0, 1) (e_{1},e_{2},e_{3},e_{4})=(6,2,0,1). We begin from the required final value T 4 = { 1 } T_{4}=\{1\} and move upward through the anti-diagonal:

 | T 3 = P 1 ​ ( { 1 }) = { 0, 2 }, T 2 = P 0 ​ ( { 0, 2 }) = { 0, 2 }, T_{3}=P_{1}(\{1\})=\{0,2\},\quad T_{2}=P_{0}(\{0,2\})=\{0,2\}, |  |

since the lower branch 0 − 2 0-2 is not allowed,

 | T 1 = P 2 ​ ( { 0, 2 }) = { 0, 2, 4 }, T 0 = P 6 ​ ( { 0, 2, 4 }) = { 2, 4, 6, 8, 10 }. T_{1}=P_{2}(\{0,2\})=\{0,2,4\},\quad T_{0}=P_{6}(\{0,2,4\})=\{2,4,6,8,10\}. |  |

Thus D S = T 0 = { 2, 4, 6, 8, 10 } D_{S}=T_{0}=\{2,4,6,8,10\}, and reflecting these distances around s n = 15 s_{n}=15 gives

 | K S = { 15 ± d: d ∈ D S } = { 5, 7, 9, 11, 13, 17, 19, 21, 23, 25 }. K_{S}=\{15\pm d:d\in D_{S}\}=\{5,7,9,11,13,17,19,21,23,25\}. |  |

This process is visualized in the figure below.

 | 2 3 5 9 15 { 5, 7, 9, 11, 13, 17, 19, 21, 23, 25 } 1 2 4 6 { 2, 4, 6, 8, 10 } 1 2 2 { 0, 2, 4 } 1 0 { 0, 2 } 1 { 0, 2 } 1 \begin{array}[]{ccccc@{\qquad}l}2&3&5&9&15&\{5,7,9,11,13,17,19,21,23,25\}\\[11.99998pt] &1&2&4&6&\{2,4,6,8,10\}\\[11.99998pt] &&1&2&2&\{0,2,4\}\\[11.99998pt] &&&1&0&\{0,2\}\\[11.99998pt] &&&&1&\{0,2\}\\[11.99998pt] &&&&&1\end{array} |  |

Figure 3: The reverse-tree process on the sequence ( 2, 3, 5, 9, 15) (2,3,5,9,15).

## 9 Interval-complete sequences

We now characterize exactly when K S K_{S} equals the full candidate interval C S C_{S}. By Corollary 13, the weaker equality S ± = C S S_{\pm}=C_{S} is controlled by the classical subset-sum completeness of the sorted multiset W S W_{S}. The equality K S = C S K_{S}=C_{S} is more rigid. It requires the independently signed expression to be compatible with the ordered folding recurrence r i = | r i − 1 − e i | r_{i}=|r_{i-1}-e_{i}|, or equivalently with the fiber condition F S ​ ( d) = 1 F_{S}(d)=1. The criterion below is therefore an ordered folding analogue of Brown’s completeness criterion. Figure 4 illustrates the local mechanism that underlies the criterion.

(a) a ≤ L a\leq L: Q a ​ ( T ~) = { 0, 1, …, a + L } Q_{a}(\widetilde{T})=\{0,1,\ldots,a+L\} is the full interval. 0 0 a a L L a + L a+L lower: a − T ~ = [0, a] a-\widetilde{T}=[0,a] upper: a + T ~ = [a, a + L] a+\widetilde{T}=[a,a+L] Q a ​ ( T ~) = { 0, …, a + L } Q_{a}(\widetilde{T})=\{0,\ldots,a+L\} (b) a > L a>L: lower branch starts at a − L > 0 a-L>0, leaving a gap. 0 0 a − L a-L a a a + L a+L lower: a − T ~ = [a − L, a] a-\widetilde{T}=[a-L,a] upper: a + T ~ = [a, a + L] a+\widetilde{T}=[a,a+L] missing: { 0, …, a − L − 1 } \{0,\ldots,a-L-1\} Figure 4: The mechanism behind the interval-completeness criterion (Theorem 20). With T ~ = { 0, 1, …, L } \widetilde{T}=\{0,1,\ldots,L\}, the preimage map Q a ​ ( T ~) Q_{a}(\widetilde{T}) consists of a lower branch a − T ~ a-\widetilde{T} and an upper branch a + T ~ a+\widetilde{T}. (a) When a ≤ L a\leq L, the two branches meet at a a and together cover the full integer interval { 0, 1, …, a + L } \{0,1,\ldots,a+L\}. (b) When a > L a>L, the lower branch starts at a − L > 0 a-L>0 and the values { 0, 1, …, a − L − 1 } \{0,1,\ldots,a-L-1\} are missing from Q a ​ ( T ~) Q_{a}(\widetilde{T}). The criterion e i ≤ 1 + ∑ j > i e j e_{i}\leq 1+\sum_{j>i}e_{j} ensures that case (a) occurs at every step of the reverse tree.

###### Theorem 20 (Interval-completeness criterion).

Let S ∈ 𝒢 n S\in\mathcal{G}_{n} with n ≥ 2 n\geq 2 and right anti-diagonal ( e 1, …, e n − 1) (e_{1},\ldots,e_{n-1}). Then K S = C S K_{S}=C_{S} if and only if

 | e i ≤ 1 + ∑ j = i + 1 n − 1 e j for every ​ 1 ≤ i ≤ n − 2. e_{i}\leq 1+\sum_{j=i+1}^{n-1}e_{j}\qquad\text{for every }1\leq i\leq n-2. |  |

###### Proof.

For n = 2 n=2 the index range 1 ≤ i ≤ n − 2 1\leq i\leq n-2 is empty, the condition holds vacuously, and indeed 𝒢 2 = { ( 2, 3) } \mathcal{G}_{2}=\{(2,3)\} has K S = C S = { 1, 3, 5 } K_{S}=C_{S}=\{1,3,5\}; we therefore assume n ≥ 3 n\geq 3.

We use the reverse-tree characterization of Proposition 18. Recall T n − 1 = { 1 } T_{n-1}=\{1\}, and T i − 1 = P e i ​ ( T i) T_{i-1}=P_{e_{i}}(T_{i}) for i = n − 1, …, 1 i=n-1,\ldots,1, with D S = T 0 D_{S}=T_{0}. By Lemma 4, e n − 1 = 1 e_{n-1}=1 and e 1, …, e n − 2 e_{1},\ldots,e_{n-2} are even. The first reverse step gives

 | T n − 2 = P 1 ​ ( { 1 }) = { 0, 2 }. T_{n-2}=P_{1}(\{1\})=\{0,2\}. |  |

From this stage onward, all elements of T i T_{i} are even, since they arise by adding or subtracting an even e j e_{j} from even values. We normalize by dividing by 2 2: write a i:= e i / 2 a_{i}:=e_{i}/2 for 1 ≤ i ≤ n − 2 1\leq i\leq n-2, and set

 | T ~ n − 2:= T n − 2 / 2 = { 0, 1 }, T ~ i − 1:= Q a i ​ ( T ~ i), \widetilde{T}_{n-2}:=T_{n-2}/2=\{0,1\},\qquad\widetilde{T}_{i-1}:=Q_{a_{i}}(\widetilde{T}_{i}), |  |

where Q a ( T ~):= { a + u: u ∈ T ~ } ∪ { a − u: u ∈ T ~, a ≥ u } Q_{a}(\widetilde{T}):=\{a+u:u\in\widetilde{T}\}\cup\{a-u:u\in\widetilde{T},\ a\geq u\} is the normalized preimage map. Then D S = 2 ​ T ~ 0 D_{S}=2\widetilde{T}_{0}.

For 0 ≤ i ≤ n − 2 0\leq i\leq n-2, define L i:= 1 + ∑ j = i + 1 n − 2 a j L_{i}:=1+\sum_{j=i+1}^{n-2}a_{j}, so L n − 2 = 1 L_{n-2}=1 and L i − 1 = a i + L i L_{i-1}=a_{i}+L_{i}. The full candidate distance set (after normalization) corresponds to { 0, 1, …, L 0 } \{0,1,\ldots,L_{0}\}: indeed, | C S | = A ⁡ ( S) + 2 |C_{S}|=A(S)+2 and the candidate distances are { 0, 2, 4, …, A ⁡ ( S) + 1 } \{0,2,4,\ldots,A(S)+1\}, normalizing to { 0, 1, …, ( A ⁡ ( S) + 1) / 2 } = { 0, 1, …, L 0 } \{0,1,\ldots,(A(S)+1)/2\}=\{0,1,\ldots,L_{0}\} since L 0 = 1 + ( a 1 + ⋯ + a n − 2) = 1 + ( A ⁡ ( S) − 1) / 2 = ( A ⁡ ( S) + 1) / 2 L_{0}=1+(a_{1}+\cdots+a_{n-2})=1+(A(S)-1)/2=(A(S)+1)/2.

Therefore K S = C S K_{S}=C_{S} is equivalent to T ~ 0 = { 0, 1, …, L 0 } \widetilde{T}_{0}=\{0,1,\ldots,L_{0}\}. The proof reduces to the following elementary claim, whose content is exactly Figure 4.

Claim. Let T ~ ⊆ { 0, 1, …, L } \widetilde{T}\subseteq\{0,1,\ldots,L\} and a ≥ 0 a\geq 0. Then Q a ​ ( T ~) = { 0, 1, …, a + L } Q_{a}(\widetilde{T})=\{0,1,\ldots,a+L\} if and only if T ~ = { 0, 1, …, L } \widetilde{T}=\{0,1,\ldots,L\} and a ≤ L a\leq L.

Proof of claim. ( ⇐) (\Leftarrow) Suppose T ~ = { 0, 1, …, L } \widetilde{T}=\{0,1,\ldots,L\} and a ≤ L a\leq L. Then { a + u: u ∈ T ~ } = { a, a + 1, …, a + L } \{a+u:u\in\widetilde{T}\}=\{a,a+1,\ldots,a+L\}, and since a ≤ L a\leq L, every u ∈ T ~ u\in\widetilde{T} with u ≤ a u\leq a is in T ~ \widetilde{T}, so { a − u: u ∈ T ~, a ≥ u } = { 0, 1, …, a } \{a-u:u\in\widetilde{T},a\geq u\}=\{0,1,\ldots,a\}. The union is { 0, 1, …, a + L } \{0,1,\ldots,a+L\}.

( ⇒) (\Rightarrow) Suppose Q a ​ ( T ~) = { 0, 1, …, a + L } Q_{a}(\widetilde{T})=\{0,1,\ldots,a+L\}. Any v > a v>a in Q a ​ ( T ~) Q_{a}(\widetilde{T}) can only arise as v = a + u v=a+u for some u ∈ T ~ u\in\widetilde{T} (since a − u ≤ a a-u\leq a). Hence for every 1 ≤ u ≤ L 1\leq u\leq L, the value a + u a+u being in Q a ​ ( T ~) Q_{a}(\widetilde{T}) forces u ∈ T ~ u\in\widetilde{T}. So { 1, …, L } ⊆ T ~ \{1,\ldots,L\}\subseteq\widetilde{T}. Also, a ∈ Q a ​ ( T ~) a\in Q_{a}(\widetilde{T}) requires 0 ∈ T ~ 0\in\widetilde{T} (via a + 0 a+0 or a − 0 a-0). Thus T ~ = { 0, 1, …, L } \widetilde{T}=\{0,1,\ldots,L\}.

It remains to show a ≤ L a\leq L. If a = 0 a=0, this is immediate. If a > 0 a>0, then the value 0 ∈ Q a ​ ( T ~) 0\in Q_{a}(\widetilde{T}) cannot arise from the upper branch a + u a+u, so it must arise from the lower branch a − u = 0 a-u=0 for some u ∈ T ~ u\in\widetilde{T}. Hence a = u ∈ T ~ a=u\in\widetilde{T}. Since T ~ ⊆ { 0, 1, …, L } \widetilde{T}\subseteq\{0,1,\ldots,L\}, this forces a ≤ L a\leq L. □ \square

*Boundedness.*Before applying the claim we record that T ~ i ⊆ { 0, 1, …, L i } \widetilde{T}_{i}\subseteq\{0,1,\ldots,L_{i}\} for every i i. This holds at i = n − 2 i=n-2 since T ~ n − 2 = { 0, 1 } \widetilde{T}_{n-2}=\{0,1\} and L n − 2 = 1 L_{n-2}=1; and if T ~ i ⊆ { 0, …, L i } \widetilde{T}_{i}\subseteq\{0,\ldots,L_{i}\}, then every element of Q a i ​ ( T ~ i) Q_{a_{i}}(\widetilde{T}_{i}) has the form a i + u a_{i}+u or a i − u a_{i}-u with 0 ≤ u ≤ L i 0\leq u\leq L_{i}, hence lies in [0, a i + L i] = [0, L i − 1] [0,\,a_{i}+L_{i}]=[0,\,L_{i-1}]. Thus T ~ i − 1 ⊆ { 0, …, L i − 1 } \widetilde{T}_{i-1}\subseteq\{0,\ldots,L_{i-1}\}, completing the induction.

*Sufficiency.*Suppose e i ≤ 1 + ∑ j > i e j e_{i}\leq 1+\sum_{j>i}e_{j} for every 1 ≤ i ≤ n − 2 1\leq i\leq n-2. Since e n − 1 = 1 e_{n-1}=1, this rearranges to e i ≤ 2 + ∑ j = i + 1 n − 2 e j e_{i}\leq 2+\sum_{j=i+1}^{n-2}e_{j}, and dividing by 2 2 gives a i ≤ 1 + ∑ j = i + 1 n − 2 a j = L i a_{i}\leq 1+\sum_{j=i+1}^{n-2}a_{j}=L_{i}. By the claim ( ⇐) (\Leftarrow) applied at each step i = n − 2, n − 3, …, 1 i=n-2,n-3,\ldots,1, the equality T ~ i − 1 = { 0, 1, …, L i − 1 } \widetilde{T}_{i-1}=\{0,1,\ldots,L_{i-1}\} propagates from T ~ n − 2 \widetilde{T}_{n-2} down to T ~ 0 = { 0, 1, …, L 0 } \widetilde{T}_{0}=\{0,1,\ldots,L_{0}\}. Hence D S = 2 ​ T ~ 0 D_{S}=2\widetilde{T}_{0} is the full parity-compatible interval, and K S = C S K_{S}=C_{S}.

*Necessity.*Conversely, suppose K S = C S K_{S}=C_{S}, equivalently T ~ 0 = { 0, 1, …, L 0 } \widetilde{T}_{0}=\{0,1,\ldots,L_{0}\}. Since T ~ 0 = Q a 1 ​ ( T ~ 1) \widetilde{T}_{0}=Q_{a_{1}}(\widetilde{T}_{1}) and, by the boundedness established above, T ~ 1 ⊆ { 0, 1, …, L 1 } \widetilde{T}_{1}\subseteq\{0,1,\ldots,L_{1}\}, the claim ( ⇒) (\Rightarrow) forces T ~ 1 = { 0, 1, …, L 1 } \widetilde{T}_{1}=\{0,1,\ldots,L_{1}\} and a 1 ≤ L 1 a_{1}\leq L_{1}. Iterating, T ~ i = { 0, 1, …, L i } \widetilde{T}_{i}=\{0,1,\ldots,L_{i}\} and a i ≤ L i a_{i}\leq L_{i} for every 1 ≤ i ≤ n − 2 1\leq i\leq n-2. In unnormalized form, e i ≤ 2 ​ L i = 2 + ∑ i < j ≤ n − 2 e j e_{i}\leq 2L_{i}=2+\sum_{i<j\leq n-2}e_{j}, equivalently e i ≤ 1 + ∑ j > i e j e_{i}\leq 1+\sum_{j>i}e_{j} (using e n − 1 = 1 e_{n-1}=1). ∎

###### Remark 21 (Generality of the criterion).

The proof of Theorem 20 uses the Gilbreath assumption only through Lemma 4 (which gives e n − 1 = 1 e_{n-1}=1 and e 1, …, e n − 2 e_{1},\ldots,e_{n-2} even). The criterion therefore applies to any ordered tuple of nonnegative integers ( e 1, …, e m − 1) (e_{1},\ldots,e_{m-1}) with e m − 1 = 1 e_{m-1}=1 and the remaining entries even, regardless of whether ( e i) (e_{i}) arises as the right anti-diagonal of a Gilbreath sequence. In this generality, with F ⁡ ( d) = ‖ ⋯ ‖ ​ d − e 1 | − e 2 ​ | ⋯ − e m − 1 | F(d)=||\cdots||d-e_{1}|-e_{2}|\cdots-e_{m-1}|, the fiber F − 1 ​ ( { 1 }) F^{-1}(\{1\}) coincides with the full parity-compatible interval { 0, 2, …, A + 1 } \{0,2,\ldots,A+1\}, A = ∑ i e i A=\sum_{i}e_{i}, if and only if e i ≤ 1 + ∑ j > i e j e_{i}\leq 1+\sum_{j>i}e_{j} for every 1 ≤ i ≤ m − 2 1\leq i\leq m-2.

###### Corollary 22.

The minimal sequence L n = ( 2, 3, 5, 7, …, 2 ​ n − 1) L_{n}=(2,3,5,7,\ldots,2n-1) is interval-complete.

###### Proof.

Its right anti-diagonal is ( 2, 0, 0, …, 0, 1) (2,0,0,\ldots,0,1). The only nontrivial criterion is at i = 1 i=1: e 1 = 2 ≤ 1 + 0 + ⋯ + 0 + 1 = 2 e_{1}=2\leq 1+0+\cdots+0+1=2. ∎

###### Corollary 23.

The doubling sequence U n = ( 2, 3, 5, 9, 17, …, 2 n − 1 + 1) U_{n}=(2,3,5,9,17,\ldots,2^{n-1}+1) is interval-complete, so | K U n | = A ⁡ ( U n) + 2 = 2 n − 1 + 1 |K_{U_{n}}|=A(U_{n})+2=2^{n-1}+1.

###### Proof.

For every positive row b ≥ 1 b\geq 1, the triangle of U n U_{n} has row b b equal to

 | ( 1, 2, 4, …, 2 n − b − 1). (1,2,4,\ldots,2^{n-b-1}). |  |

Thus the right anti-diagonal is

 | ( e 1, …, e n − 1) = ( 2 n − 2, 2 n − 3, …, 2, 1). (e_{1},\ldots,e_{n-1})=(2^{n-2},2^{n-3},\ldots,2,1). |  |

At each i i, we have e i = 2 n − i − 1 e_{i}=2^{n-i-1}, while

 | 1 + ∑ j > i e j = 1 + ( 2 n − i − 1 − 1) = 2 n − i − 1. 1+\sum_{j>i}e_{j}=1+(2^{n-i-1}-1)=2^{n-i-1}. |  |

Equality holds throughout the criterion, so U n U_{n} is interval-complete. Since

 | A ⁡ ( U n) = 2 n − 1 − 1, A(U_{n})=2^{n-1}-1, |  |

we get

 | | K U n | = A ⁡ ( U n) + 2 = 2 n − 1 + 1. |K_{U_{n}}|=A(U_{n})+2=2^{n-1}+1. |  |

∎

## 10 The first hole

5 5 7 7 9 9 11 11 13 13 15 15 17 17 19 19 21 21 23 23 25 25 hole at k = s n = 15 k=s_{n}=15 s n − A ⁡ ( S) − 1 s_{n}-A(S)-1 s n + A ⁡ ( S) + 1 s_{n}+A(S)+1 C S C_{S}: 11 odd integers from 5 5 to 25 25 Figure 5: The first hole. For S = ( 2, 3, 5, 9, 15) S=(2,3,5,9,15), the candidate set C S C_{S} consists of all odd integers in [s n − A ⁡ ( S) − 1, s n + A ⁡ ( S) + 1] = [5, 25] [s_{n}-A(S)-1,\,s_{n}+A(S)+1]=[5,25]. The valid-extension set K S K_{S} (blue dots) contains all of these except the center value k = 15 k=15 (marked × \times). Thus H S = { 15 } H_{S}=\{15\} and h ⁡ ( S) = 1 h(S)=1.

###### Theorem 24 (First hole).

For n ≤ 4 n\leq 4, every S ∈ 𝒢 n S\in\mathcal{G}_{n} has K S = C S K_{S}=C_{S}. The smallest n n for which some S ∈ 𝒢 n S\in\mathcal{G}_{n} has K S ≠ C S K_{S}\neq C_{S} is n = 5 n=5. At this length, the unique sequence S ∈ 𝒢 5 S\in\mathcal{G}_{5} with K S ≠ C S K_{S}\neq C_{S} is

 | S = ( 2, 3, 5, 9, 15). S=(2,3,5,9,15). |  |

Explicitly,

 | C S = { 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25 }, K S = { 5, 7, 9, 11, 13, 17, 19, 21, 23, 25 }, C_{S}=\{5,7,9,11,13,15,17,19,21,23,25\},\quad K_{S}=\{5,7,9,11,13,17,19,21,23,25\}, |  |

so H S = { 15 } H_{S}=\{15\} (Figure 5).

###### Proof.

*The case n ≤ 4 n\leq 4.*The families are

 | 𝒢 2 = { ( 2, 3) }, 𝒢 3 = { ( 2, 3, 5) }, 𝒢 4 = { ( 2, 3, 5, 7), ( 2, 3, 5, 9) }. \mathcal{G}_{2}=\{(2,3)\},\qquad\mathcal{G}_{3}=\{(2,3,5)\},\qquad\mathcal{G}_{4}=\{(2,3,5,7),(2,3,5,9)\}. |  |

Their right anti-diagonals are respectively

 | ( 1), ( 2, 1), ( 2, 0, 1), ( 4, 2, 1). (1),\qquad(2,1),\qquad(2,0,1),\qquad(4,2,1). |  |

Each satisfies the criterion of Theorem 20 (vacuously for n = 2 n=2, and directly for the others), so all four sequences are interval-complete.

*The case n = 5 n=5.*𝒢 5 \mathcal{G}_{5} has six sequences. These are obtained by extending the two elements of 𝒢 4 \mathcal{G}_{4}:

 | K ( 2, 3, 5, 7) + = { 9, 11 }, K ( 2, 3, 5, 9) + = { 11, 13, 15, 17 }. K_{(2,3,5,7)}^{+}=\{9,11\},\qquad K_{(2,3,5,9)}^{+}=\{11,13,15,17\}. |  |

Thus the displayed six sequences are all of 𝒢 5 \mathcal{G}_{5}. We list them with their right anti-diagonals:

 | S ( e 1, e 2, e 3, e 4) ( 2, 3, 5, 7, 9) ( 2, 0, 0, 1) ( 2, 3, 5, 7, 11) ( 4, 2, 2, 1) ( 2, 3, 5, 9, 11) ( 2, 2, 0, 1) ( 2, 3, 5, 9, 13) ( 4, 0, 2, 1) ( 2, 3, 5, 9, 15) ( 6, 2, 0, 1) ( 2, 3, 5, 9, 17) ( 8, 4, 2, 1) \begin{array}[]{l|l}S&(e_{1},e_{2},e_{3},e_{4})\\ \hline\cr(2,3,5,7,9)&(2,0,0,1)\\ (2,3,5,7,11)&(4,2,2,1)\\ (2,3,5,9,11)&(2,2,0,1)\\ (2,3,5,9,13)&(4,0,2,1)\\ (2,3,5,9,15)&(6,2,0,1)\\ (2,3,5,9,17)&(8,4,2,1)\end{array} |  |

For each of these we check the criterion e i ≤ 1 + ∑ j > i e j e_{i}\leq 1+\sum_{j>i}e_{j} at i = 1, 2, 3 i=1,2,3. All five sequences except ( 2, 3, 5, 9, 15) (2,3,5,9,15) satisfy the criterion at every i i and are therefore interval-complete by Theorem 20. For ( 2, 3, 5, 9, 15) (2,3,5,9,15), the criterion fails at i = 1 i=1: e 1 = 6 > 1 + 2 + 0 + 1 = 4 e_{1}=6>1+2+0+1=4. The corresponding extension sets are

 | S K S | K S | ( 2, 3, 5, 7, 9) { 5, 7, 9, 11, 13 } 5 ( 2, 3, 5, 7, 11) { 1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21 } 11 ( 2, 3, 5, 9, 11) { 5, 7, 9, 11, 13, 15, 17 } 7 ( 2, 3, 5, 9, 13) { 5, 7, 9, 11, 13, 15, 17, 19, 21 } 9 ( 2, 3, 5, 9, 15) { 5, 7, 9, 11, 13, 17, 19, 21, 23, 25 } 10 ( 2, 3, 5, 9, 17) { 1, 3, 5, …, 33 } 17 \begin{array}[]{l|l|c}S&K_{S}&|K_{S}|\\ \hline\cr(2,3,5,7,9)&\{5,7,9,11,13\}&5\\ (2,3,5,7,11)&\{1,3,5,7,9,11,13,15,17,19,21\}&11\\ (2,3,5,9,11)&\{5,7,9,11,13,15,17\}&7\\ (2,3,5,9,13)&\{5,7,9,11,13,15,17,19,21\}&9\\ (2,3,5,9,15)&\{5,7,9,11,13,17,19,21,23,25\}&10\\ (2,3,5,9,17)&\{1,3,5,\ldots,33\}&17\end{array} |  |

and only ( 2, 3, 5, 9, 15) (2,3,5,9,15) has | K S | ≠ A ⁡ ( S) + 2 |K_{S}|\neq A(S)+2.

*Identifying the hole.*The right anti-diagonal of S = ( 2, 3, 5, 9, 15) S=(2,3,5,9,15) is ( 6, 2, 0, 1) (6,2,0,1) (Example 1). Applying the reverse tree of Proposition 18:

 | T 4 = { 1 }, T 3 = P 1 ​ ( { 1 }) = { 0, 2 }, T 2 = P 0 ​ ( { 0, 2 }) = { 0, 2 }, T_{4}=\{1\},\ T_{3}=P_{1}(\{1\})=\{0,2\},\ T_{2}=P_{0}(\{0,2\})=\{0,2\}, |  |

 | T 1 = P 2 ​ ( { 0, 2 }) = { 0, 2, 4 }, T 0 = P 6 ​ ( { 0, 2, 4 }) = { 2, 4, 6, 8, 10 }. T_{1}=P_{2}(\{0,2\})=\{0,2,4\},\ T_{0}=P_{6}(\{0,2,4\})=\{2,4,6,8,10\}. |  |

The value 0 0 would be in T 0 T_{0} only via 6 − 6 6-6, but 6 ∉ T 1 6\notin T_{1}; hence 0 ∉ T 0 0\notin T_{0}. Therefore D S = { 2, 4, 6, 8, 10 } D_{S}=\{2,4,6,8,10\}, giving K S = { 15 ± d: d ∈ D S } = C S ∖ { 15 } K_{S}=\{15\pm d:d\in D_{S}\}=C_{S}\setminus\{15\}, so H S = { 15 } H_{S}=\{15\}. ∎

## 11 Minimum extension width

###### Theorem 25 (Minimum extension width).

For every n ≥ 3 n\geq 3,

 | min S ∈ 𝒢 n ⁡ | K S | = 5, \min_{S\in\mathcal{G}_{n}}|K_{S}|=5, |  |

and the minimum is uniquely achieved by the minimal sequence L n = ( 2, 3, 5, 7, …, 2 ​ n − 1) L_{n}=(2,3,5,7,\ldots,2n-1).

We separate the proof into three lemmas.

###### Lemma 26.

For every S ∈ 𝒢 n S\in\mathcal{G}_{n}, | D S | ≥ 3 |D_{S}|\geq 3.

###### Proof.

The reverse tree starts with T n − 1 = { 1 } T_{n-1}=\{1\}, and the first step gives T n − 2 = P 1 ​ ( { 1 }) = { 0, 2 } T_{n-2}=P_{1}(\{1\})=\{0,2\}. Each preimage step P e ​ ( T) P_{e}(T) contains the translated set { e + t: t ∈ T } \{e+t:t\in T\} with the same cardinality as T T, so the cardinality of T i T_{i} is non-decreasing as i i decreases.

By Lemma 4, e 1 = s n − s n − 1 e_{1}=s_{n}-s_{n-1} is a positive even integer, so e 1 ≥ 2 e_{1}\geq 2.

*Case 1.*If e 2 = ⋯ = e n − 2 = 0 e_{2}=\cdots=e_{n-2}=0, then each step P 0 ​ ( { 0, 2 }) = { 0, 2 } P_{0}(\{0,2\})=\{0,2\} leaves the set unchanged, so T 1 = { 0, 2 } T_{1}=\{0,2\}. The final step is P e 1 ​ ( { 0, 2 }) P_{e_{1}}(\{0,2\}). Since e 1 ≥ 2 e_{1}\geq 2, both e 1 − 0 = e 1 e_{1}-0=e_{1} and e 1 − 2 e_{1}-2 are nonnegative, giving T 0 = { e 1 − 2, e 1, e 1 + 2 } T_{0}=\{e_{1}-2,e_{1},e_{1}+2\}, three distinct values.

*Case 2.*If some e j e_{j} with 2 ≤ j ≤ n − 2 2\leq j\leq n-2 is positive, take the largest such j j. Then e j + 1 = ⋯ = e n − 2 = 0 e_{j+1}=\cdots=e_{n-2}=0, so T j = { 0, 2 } T_{j}=\{0,2\}. Since e j e_{j} is a positive even integer (Lemma 4), e j ≥ 2 e_{j}\geq 2, and T j − 1 = P e j ​ ( { 0, 2 }) = { e j − 2, e j, e j + 2 } T_{j-1}=P_{e_{j}}(\{0,2\})=\{e_{j}-2,e_{j},e_{j}+2\} has 3 3 distinct elements. By cardinality non-decrease, | T 0 | ≥ 3 |T_{0}|\geq 3.

In both cases | D S | = | T 0 | ≥ 3 |D_{S}|=|T_{0}|\geq 3. ∎

###### Lemma 27.

If | K S | = 5 |K_{S}|=5, then ( e 1, e 2, …, e n − 1) = ( 2, 0, 0, …, 0, 1) (e_{1},e_{2},\ldots,e_{n-1})=(2,0,0,\ldots,0,1).

###### Proof.

By Theorem 16, | K S | = 2 ​ | D S | |K_{S}|=2|D_{S}| if 0 ∉ D S 0\notin D_{S} and | K S | = 2 ​ | D S | − 1 |K_{S}|=2|D_{S}|-1 if 0 ∈ D S 0\in D_{S}. So | K S | = 5 |K_{S}|=5 requires | D S | = 3 |D_{S}|=3 and 0 ∈ D S 0\in D_{S}.

For 0 ∈ D S = P e 1 ​ ( T 1) 0\in D_{S}=P_{e_{1}}(T_{1}), we need e 1 − t = 0 e_{1}-t=0 for some t ∈ T 1 t\in T_{1}, i.e., e 1 ∈ T 1 e_{1}\in T_{1}. Since e 1 ≥ 2 e_{1}\geq 2, this means T 1 T_{1} contains an element ≥ 2 \geq 2.

If | T 1 | ≥ 3 |T_{1}|\geq 3, then P e 1 ​ ( T 1) P_{e_{1}}(T_{1}) contains the three distinct positive elements { e 1 + t: t ∈ T 1 } \{e_{1}+t:t\in T_{1}\}, plus the element 0 0 from the lower branch, giving | D S | ≥ 4 |D_{S}|\geq 4 and contradicting | D S | = 3 |D_{S}|=3. Hence | T 1 | = 2 |T_{1}|=2.

The sequence T n − 2 = { 0, 2 }, T n − 3, …, T 1 T_{n-2}=\{0,2\},T_{n-3},\ldots,T_{1} has non-decreasing cardinality, so all these sets have cardinality 2 2. Each middle e j e_{j} is even (Lemma 4), so either e j = 0 e_{j}=0, in which case P e j ​ ( { 0, 2 }) = { 0, 2 } P_{e_{j}}(\{0,2\})=\{0,2\}, or e j ≥ 2 e_{j}\geq 2, in which case P e j ​ ( { 0, 2 }) = { e j − 2, e j, e j + 2 } P_{e_{j}}(\{0,2\})=\{e_{j}-2,\,e_{j},\,e_{j}+2\} has three distinct elements. Preservation of cardinality 2 2 therefore forces e j = 0 e_{j}=0 for each 2 ≤ j ≤ n − 2 2\leq j\leq n-2, and T 1 = { 0, 2 } T_{1}=\{0,2\}.

Since e 1 ∈ T 1 = { 0, 2 } e_{1}\in T_{1}=\{0,2\} and e 1 ≥ 2 e_{1}\geq 2, e 1 = 2 e_{1}=2. Combined with e n − 1 = 1 e_{n-1}=1, we get ( e 1, …, e n − 1) = ( 2, 0, …, 0, 1) (e_{1},\ldots,e_{n-1})=(2,0,\ldots,0,1). ∎

###### Lemma 28.

If S ∈ 𝒢 n S\in\mathcal{G}_{n} has ( e 1, e 2, …, e n − 1) = ( 2, 0, 0, …, 0, 1) (e_{1},e_{2},\ldots,e_{n-1})=(2,0,0,\ldots,0,1), then S = L n S=L_{n}.

###### Proof.

Write g j:= s j + 1 − s j g_{j}:=s_{j+1}-s_{j} for the gaps of S S. Since ( s 1, s 2) = ( 2, 3) (s_{1},s_{2})=(2,3), we have g 1 = 1 g_{1}=1. Also g n − 1 = s n − s n − 1 = e 1 = 2 g_{n-1}=s_{n}-s_{n-1}=e_{1}=2.

We prove by descending induction that

 | g j = 2 ( 2 ≤ j ≤ n − 1). g_{j}=2\qquad(2\leq j\leq n-1). |  |

The base case j = n − 1 j=n-1 was just proved. Now suppose 2 ≤ j ≤ n − 2 2\leq j\leq n-2 and assume inductively that

 | g j + 1 = g j + 2 = ⋯ = g n − 1 = 2. g_{j+1}=g_{j+2}=\cdots=g_{n-1}=2. |  |

Then the row- 1 1 entries strictly to the right of position j j are all 2 2. Hence, by induction on the row index, every entry s a b s_{a}^{b} with a ≥ j + 1 a\geq j+1, b ≥ 2 b\geq 2, and a + b ≤ n a+b\leq n is zero: in row 2 2 these are absolute differences of equal row- 1 1 entries, and in higher rows they are absolute differences of zeros.

Now use the anti-diagonal hypothesis at index i = n − j i=n-j. Since e i = s n − i i e_{i}=s_{n-i}^{i}, we have

 | e n − j = s j n − j = 0. e_{n-j}=s_{j}^{n-j}=0. |  |

We propagate this zero upward to row 2 2. For each m = 2, 3, …, n − j − 1 m=2,3,\ldots,n-j-1, the entry s j + 1 m s_{j+1}^{m} is zero by the preceding paragraph, and the recurrence gives

 | s j m + 1 = | s j + 1 m − s j m | = | 0 − s j m | = s j m. s_{j}^{m+1}=|s_{j+1}^{m}-s_{j}^{m}|=|0-s_{j}^{m}|=s_{j}^{m}. |  |

If n − j = 2 n-j=2, this already says s j 2 = 0 s_{j}^{2}=0. Otherwise, applying the identity successively for

 | m = n − j − 1, n − j − 2, …, 2, m=n-j-1,\ n-j-2,\ \ldots,\ 2, |  |

gives

 | s j n − j = s j n − j − 1 = ⋯ = s j 2. s_{j}^{n-j}=s_{j}^{n-j-1}=\cdots=s_{j}^{2}. |  |

Since s j n − j = 0 s_{j}^{n-j}=0, it follows in all cases that s j 2 = 0 s_{j}^{2}=0. But

 | s j 2 = | s j + 1 1 − s j 1 | = | g j + 1 − g j | = | 2 − g j |. s_{j}^{2}=|s_{j+1}^{1}-s_{j}^{1}|=|g_{j+1}-g_{j}|=|2-g_{j}|. |  |

Therefore g j = 2 g_{j}=2, completing the descending induction.

Thus g 1 = 1 g_{1}=1 and g 2 = ⋯ = g n − 1 = 2 g_{2}=\cdots=g_{n-1}=2, so

 | S = ( 2, 3, 5, 7, …, 2 ​ n − 1) = L n. S=(2,3,5,7,\ldots,2n-1)=L_{n}. |  |

∎

###### Proof of Theorem 25.

By Lemma 26, | D S | ≥ 3 |D_{S}|\geq 3, so | K S | ≥ 2 ⋅ 3 − 1 = 5 |K_{S}|\geq 2\cdot 3-1=5. Equality requires 0 ∈ D S 0\in D_{S} and | D S | = 3 |D_{S}|=3, which by Lemma 27 forces the anti-diagonal ( 2, 0, …, 0, 1) (2,0,\ldots,0,1), which by Lemma 28 forces S = L n S=L_{n}. Conversely, L n L_{n} has this anti-diagonal, and the reverse tree gives D L n = { 0, 2, 4 } D_{L_{n}}=\{0,2,4\}, hence | K L n | = 5 |K_{L_{n}}|=5. ∎

## 12 The doubling sequence and the maximum-width conjecture

###### Theorem 29 (Extension width of the doubling sequence).

For every n ≥ 2 n\geq 2, | K U n | = 2 n − 1 + 1 |K_{U_{n}}|=2^{n-1}+1.

###### Proof.

By Corollary 23. ∎

###### Conjecture 30 (Maximum width).

For every n ≥ 2 n\geq 2, max S ∈ 𝒢 n ⁡ | K S | = 2 n − 1 + 1 \max_{S\in\mathcal{G}_{n}}|K_{S}|=2^{n-1}+1, uniquely achieved by U n U_{n}.

This conjecture is verified by exhaustive computation for n ≤ 10 n\leq 10; see Table 1. A proof would have to use the fact that the anti-diagonal arises from a Gilbreath sequence, not from arbitrary nonnegative integers, since the reverse-tree analysis alone permits anti-diagonals exceeding the doubling bound.

## 13 An exponentially disconnected family

For a finite set X ⊆ ℤ X\subseteq\mathbb{Z} all of one parity class, #​ comp ​ ( X) \#\textup{comp}(X) denotes the number of maximal runs of common difference 2 2.

###### Definition 31.

For n ≥ 5 n\geq 5, set V n:= ( v 1, …, v n) V_{n}:=(v_{1},\ldots,v_{n}) where v 1 = 2 v_{1}=2, v i = 2 i − 1 + 1 v_{i}=2^{i-1}+1 for 2 ≤ i ≤ n − 1 2\leq i\leq n-1, and v n = 2 n − 1 − 1 v_{n}=2^{n-1}-1.

So V n V_{n} follows the doubling through position n − 1 n-1 and then undershoots at the last position by 2 2: V 5 = ( 2, 3, 5, 9, 15) V_{5}=(2,3,5,9,15), V 6 = ( 2, 3, 5, 9, 17, 31) V_{6}=(2,3,5,9,17,31), V 7 = ( 2, 3, 5, 9, 17, 33, 63) V_{7}=(2,3,5,9,17,33,63).

###### Example 32.

For V 5 V_{5}, the reverse tree gives D 5 = { 2, 4, 6, 8, 10 } D_{5}=\{2,4,6,8,10\}, a single block of 5 5 consecutive even integers. For V 6 V_{6}, the right anti-diagonal is ( 14, 6, 2, 0, 1) (14,6,2,0,1); running the reverse tree, the preimage step P 14 P_{14} applied to D 5 D_{5} splits each element into two preimages 14 − d 14-d and 14 + d 14+d, giving D 6 = { 4, 6, 8, 10, 12 } ∪ { 16, 18, 20, 22, 24 } D_{6}=\{4,6,8,10,12\}\cup\{16,18,20,22,24\}, two 5 5 -element blocks separated by a gap. Figure 6 shows the first three stages.

0 0 10 10 20 20 30 30 40 40 50 50 60 60 D 5 D_{5} D 6 D_{6} D 7 D_{7} 1 component 2 components 4 components E 6 = 14 E_{6}=14 E 7 = 30 E_{7}=30 Figure 6: Component doubling in the family V n V_{n} (Theorem 35). Each horizontal block represents a maximal run of even integers spaced by 2 2. The recursion D n = P E n ​ ( D n − 1) D_{n}=P_{E_{n}}(D_{n-1}), with E n = 2 n − 2 − 2 E_{n}=2^{n-2}-2, sends D n − 1 D_{n-1} to two separated reflected copies E n − D n − 1 E_{n}-D_{n-1} and E n + D n − 1 E_{n}+D_{n-1}. Thus the number of components doubles at each step.

###### Lemma 33.

For n ≥ 5 n\geq 5, V n ∈ 𝒢 n V_{n}\in\mathcal{G}_{n} with right anti-diagonal e i = 2 n − i − 1 − 2 e_{i}=2^{n-i-1}-2 for 1 ≤ i ≤ n − 2 1\leq i\leq n-2 and e n − 1 = 1 e_{n-1}=1.

###### Proof.

The first n − 1 n-1 terms of V n V_{n} form the doubling sequence U n − 1 U_{n-1}, whose triangle is the powers-of-two array. The final gap is v n − v n − 1 = ( 2 n − 1 − 1) − ( 2 n − 2 + 1) = 2 n − 2 − 2 v_{n}-v_{n-1}=(2^{n-1}-1)-(2^{n-2}+1)=2^{n-2}-2, giving e 1 = 2 n − 2 − 2 e_{1}=2^{n-2}-2. The rightmost entry of U n − 1 U_{n-1} ’s row 1 1 is 2 n − 3 2^{n-3}, so e 2 = | 2 n − 2 − 2 − 2 n − 3 | = 2 n − 3 − 2 e_{2}=|2^{n-2}-2-2^{n-3}|=2^{n-3}-2. Iterating, e i = 2 n − i − 1 − 2 e_{i}=2^{n-i-1}-2 for 1 ≤ i ≤ n − 2 1\leq i\leq n-2; in particular e n − 2 = 0 e_{n-2}=0. Finally e n − 1 = | 1 − 0 | = 1 e_{n-1}=|1-0|=1. ∎

Throughout this section write D n:= D V n D_{n}:=D_{V_{n}} for the distance set of V n V_{n}, and recall the preimage map P e P_{e} of Section 8. By Lemma 33 the right anti-diagonal of V n V_{n} is ( e 1, …, e n − 1) = ( 2 n − 2 − 2, 2 n − 3 − 2, …, 2, 0, 1) (e_{1},\ldots,e_{n-1})=(2^{n-2}-2,\,2^{n-3}-2,\,\ldots,\,2,\,0,\,1), and the anti-diagonal of V n V_{n} is precisely that of V n − 1 V_{n-1} with one new leading entry E n:= 2 n − 2 − 2 E_{n}:=2^{n-2}-2 prepended. Consequently the reverse-tree process (Proposition 18) for V n V_{n} is the process for V n − 1 V_{n-1} followed by one additional preimage step:

 | D n = P E n ( D n − 1), E n = 2 n − 2 − 2 ( n ≥ 6). D_{n}=P_{E_{n}}(D_{n-1}),\qquad E_{n}=2^{n-2}-2\quad(n\geq 6). |  | (1) |

We first isolate the arithmetic of the extremes of D n D_{n}, since the component count and cardinality both depend on it.

###### Lemma 34 (Extremes and structure of D n D_{n}).

For every n ≥ 5 n\geq 5 the set D n D_{n} consists of positive even integers, and

 | min ⁡ D n = 2 ​ n − 8, max ⁡ D n = 2 n − 1 − 2 ​ n + 4. \min D_{n}=2n-8,\qquad\max D_{n}=2^{n-1}-2n+4. |  |

Moreover, for n ≥ 6 n\geq 6 the recursion ( 1) acts as two disjoint reflected copies:

 | D n = ( E n − D n − 1) ⊔ ( E n + D n − 1), D_{n}=(E_{n}-D_{n-1})\,\sqcup\,(E_{n}+D_{n-1}), |  | (2) |

where every element of E n − D n − 1 E_{n}-D_{n-1} is strictly smaller than every element of E n + D n − 1 E_{n}+D_{n-1}.

###### Proof.

We argue by induction on n n.

*Base case n = 5 n=5.*The reverse-tree computation in Example 32 gives D 5 = { 2, 4, 6, 8, 10 } D_{5}=\{2,4,6,8,10\}, all positive and even, with min ⁡ D 5 = 2 = 2 ​ ( 5) − 8 \min D_{5}=2=2(5)-8 and max ⁡ D 5 = 10 = 2 4 − 2 ​ ( 5) + 4 \max D_{5}=10=2^{4}-2(5)+4. This establishes the base case. (The split ( 2) is asserted only for n ≥ 6 n\geq 6.)

*Inductive step.*Fix n ≥ 6 n\geq 6 and assume the statement for n − 1 n-1; in particular D n − 1 D_{n-1} consists of positive even integers with

 | min ⁡ D n − 1 = 2 ​ n − 10, max ⁡ D n − 1 = 2 n − 2 − 2 ​ n + 6. \min D_{n-1}=2n-10,\qquad\max D_{n-1}=2^{n-2}-2n+6. |  | (3) |

Recall that

 | P E n ( D n − 1) = { E n + d: d ∈ D n − 1 } ∪ { E n − d: d ∈ D n − 1, E n ≥ d }. P_{E_{n}}(D_{n-1})=\{E_{n}+d:d\in D_{n-1}\}\;\cup\;\{E_{n}-d:d\in D_{n-1},\ E_{n}\geq d\}. |  |

We first show the second branch is unconditional, i.e. that E n ≥ d E_{n}\geq d for every d ∈ D n − 1 d\in D_{n-1}. It suffices to check E n ≥ max ⁡ D n − 1 E_{n}\geq\max D_{n-1}. Using ( 3),

 | E n − max ⁡ D n − 1 = ( 2 n − 2 − 2) − ( 2 n − 2 − 2 ​ n + 6) = 2 ​ n − 8 ≥ 4 > 0, E_{n}-\max D_{n-1}=(2^{n-2}-2)-(2^{n-2}-2n+6)=2n-8\;\geq\;4\;>\;0, |  | (4) |

since n ≥ 6 n\geq 6. Hence E n > max ⁡ D n − 1 ≥ d E_{n}>\max D_{n-1}\geq d for all d ∈ D n − 1 d\in D_{n-1}, so both branches are active and D n = ( E n − D n − 1) ∪ ( E n + D n − 1) D_{n}=(E_{n}-D_{n-1})\cup(E_{n}+D_{n-1}).

*Disjoint and ordered.*Every element of the lower branch satisfies E n − d < E n E_{n}-d<E_{n} (as d > 0 d>0), while every element of the upper branch satisfies E n + d > E n E_{n}+d>E_{n}. Hence each element of E n − D n − 1 E_{n}-D_{n-1} is strictly below E n E_{n} and each element of E n + D n − 1 E_{n}+D_{n-1} strictly above, giving ( 2) with the claimed ordering; in particular the union is disjoint.

*Parity and positivity.*Each d ∈ D n − 1 d\in D_{n-1} is even and E n = 2 n − 2 − 2 E_{n}=2^{n-2}-2 is even, so E n ± d E_{n}\pm d is even. The smallest element of D n D_{n} is E n − max ⁡ D n − 1 = 2 ​ n − 8 > 0 E_{n}-\max D_{n-1}=2n-8>0 by ( 4); hence all elements of D n D_{n} are positive.

*New extremes.*By the ordering in ( 2),

 | min ⁡ D n = E n − max ⁡ D n − 1 = 2 ​ n − 8, \min D_{n}=E_{n}-\max D_{n-1}=2n-8, |  |

 | max ⁡ D n = E n + max ⁡ D n − 1 = ( 2 n − 2 − 2) + ( 2 n − 2 − 2 ​ n + 6) = 2 n − 1 − 2 ​ n + 4. \max D_{n}=E_{n}+\max D_{n-1}=(2^{n-2}-2)+(2^{n-2}-2n+6)=2^{n-1}-2n+4. |  |

These are the claimed formulas at n n, completing the induction. ∎

With the structure of D n D_{n} in hand, the main theorem follows.

###### Theorem 35 (Exponentially many components).

For every n ≥ 5 n\geq 5,

 | | K V n | = 5 ⋅ 2 n − 4, #​ comp ​ ( K V n) = 2 n − 4, h ⁡ ( V n) = 3 ⋅ 2 n − 4 − 2 ​ n + 5. |K_{V_{n}}|=5\cdot 2^{n-4},\quad\#\textup{comp}(K_{V_{n}})=2^{n-4},\quad h(V_{n})=3\cdot 2^{n-4}-2n+5. |  |

###### Proof.

We first show, by induction on n ≥ 5 n\geq 5, that

 | | D n | = 5 ⋅ 2 n − 5 and #​ comp ​ ( D n) = 2 n − 5. |D_{n}|=5\cdot 2^{n-5}\qquad\text{and}\qquad\#\textup{comp}(D_{n})=2^{n-5}. |  | (5) |

For n = 5 n=5, D 5 = { 2, 4, 6, 8, 10 } D_{5}=\{2,4,6,8,10\} has | D 5 | = 5 = 5 ⋅ 2 0 |D_{5}|=5=5\cdot 2^{0} and is a single run, so #​ comp ​ ( D 5) = 1 = 2 0 \#\textup{comp}(D_{5})=1=2^{0}. For n ≥ 6 n\geq 6, Lemma 34 gives the disjoint union ( 2); since d ↦ E n + d d\mapsto E_{n}+d and d ↦ E n − d d\mapsto E_{n}-d are injective, each copy has | D n − 1 | |D_{n-1}| elements, so | D n | = 2 ​ | D n − 1 | = 5 ⋅ 2 n − 5 |D_{n}|=2|D_{n-1}|=5\cdot 2^{n-5}.

For the component count, the gap separating the two copies in ( 2) is

 | ( min ⁡ ( E n + D n − 1)) − ( max ⁡ ( E n − D n − 1)) = ( E n + min ⁡ D n − 1) − ( E n − min ⁡ D n − 1) = 2 ​ min ​ D n − 1 ≥ 4 \big(\min(E_{n}+D_{n-1})\big)-\big(\max(E_{n}-D_{n-1})\big)=(E_{n}+\min D_{n-1})-(E_{n}-\min D_{n-1})=2\min D_{n-1}\geq 4 |  |

by Lemma 34 ( min ⁡ D n − 1 = 2 ​ n − 10 ≥ 2 \min D_{n-1}=2n-10\geq 2 for n ≥ 6 n\geq 6). A gap of at least 4 4 between consecutive even integers breaks the run, so the two copies lie in distinct parity-lattice components, and within each copy the reflection d ↦ E n ± d d\mapsto E_{n}\pm d preserves adjacency of common difference 2 2. Hence #​ comp ​ ( D n) = 2 ​ #​ comp ​ ( D n − 1) = 2 n − 5 \#\textup{comp}(D_{n})=2\,\#\textup{comp}(D_{n-1})=2^{n-5}, proving ( 5).

By Lemma 34, min ⁡ D n = 2 ​ n − 8 > 0 \min D_{n}=2n-8>0, so 0 ∉ D n 0\notin D_{n} and the reflection of Theorem 16 produces two disjoint translated copies K V n = ( v n − D n) ⊔ ( v n + D n) K_{V_{n}}=(v_{n}-D_{n})\,\sqcup\,(v_{n}+D_{n}), separated by a gap of 2 ​ min ⁡ D n ≥ 4 2\min D_{n}\geq 4. Hence

 | | K V n | = 2 ​ | D n | = 5 ⋅ 2 n − 4, #​ comp ​ ( K V n) = 2 ​ #​ comp ​ ( D n) = 2 n − 4. |K_{V_{n}}|=2|D_{n}|=5\cdot 2^{n-4},\qquad\#\textup{comp}(K_{V_{n}})=2\,\#\textup{comp}(D_{n})=2^{n-4}. |  |

Finally, by Lemma 33,

 | A ⁡ ( V n) = ∑ i = 1 n − 2 ( 2 n − i − 1 − 2) + 1 = ( 2 n − 1 − 2) − 2 ​ ( n − 2) + 1 = 2 n − 1 − 2 ​ n + 3, A(V_{n})=\sum_{i=1}^{n-2}\!\big(2^{n-i-1}-2\big)+1=(2^{n-1}-2)-2(n-2)+1=2^{n-1}-2n+3, |  |

so by Lemma 7 the candidate set has size A ⁡ ( V n) + 2 = 2 n − 1 − 2 ​ n + 5 A(V_{n})+2=2^{n-1}-2n+5, and

 | h ⁡ ( V n) = | C V n | − | K V n | = ( 2 n − 1 − 2 ​ n + 5) − 5 ⋅ 2 n − 4 = 3 ⋅ 2 n − 4 − 2 ​ n + 5. ∎ h(V_{n})=|C_{V_{n}}|-|K_{V_{n}}|=(2^{n-1}-2n+5)-5\cdot 2^{n-4}=3\cdot 2^{n-4}-2n+5.\qed |  |

###### Corollary 36.

For every n ≥ 5 n\geq 5,

 | max S ∈ 𝒢 n ⁡ #​ comp ​ ( K S) ≥ 2 n − 4 and max S ∈ 𝒢 n ⁡ h ⁡ ( S) ≥ 3 ⋅ 2 n − 4 − 2 ​ n + 5. \max_{S\in\mathcal{G}_{n}}\#\textup{comp}(K_{S})\geq 2^{n-4}\quad\text{and}\quad\max_{S\in\mathcal{G}_{n}}h(S)\geq 3\cdot 2^{n-4}-2n+5. |  |

The first inequality is sharp for n ≤ 10 n\leq 10 (by exhaustive computation); the second is not, in general.

## 14 Computational data

Table 1 records enumeration data for 𝒢 n \mathcal{G}_{n} computed using the corrected extension test, as well as extremal-width data for 2 ≤ n ≤ 10 2\leq n\leq 10, with N 11 N_{11} included since it is computable from the 𝒢 10 \mathcal{G}_{10} frontier. The data was generated using the reverse-tree algorithm of Proposition 18; the code in Section 17 reproduces the full table.

n n | N n N_{n} | m n m_{n} | #min | M n M_{n} | #max | #i.c. | #defective | max def | max comp |

2 | 1 | 3 | 1 | 3 | 1 | 1 | 0 | 0 | 1 |

3 | 1 | 5 | 1 | 5 | 1 | 1 | 0 | 0 | 1 |

4 | 2 | 5 | 1 | 9 | 1 | 2 | 0 | 0 | 1 |

5 | 6 | 5 | 1 | 17 | 1 | 5 | 1 | 1 | 2 |

6 | 27 | 5 | 1 | 33 | 1 | 22 | 5 | 5 | 4 |

7 | 180 | 5 | 1 | 65 | 1 | 120 | 60 | 15 | 8 |

8 | 1,786 | 5 | 1 | 129 | 1 | 1,026 | 760 | 47 | 16 |

9 | 26,094 | 5 | 1 | 257 | 1 | 12,782 | 13,312 | 121 | 32 |

10 | 559,127 | 5 | 1 | 513 | 1 | 237,073 | 322,054 | 281 | 64 |

11 | 17,535,396 | – | – | – | – | – | – | – | – |

Table 1: Enumeration data for 𝒢 n \mathcal{G}_{n} computed using the corrected extension test, together with extremal extension-width data. Here “#i.c.” is the count of interval-complete sequences ( h ⁡ ( S) = 0 h(S)=0), “#defective” is the count with h ⁡ ( S) > 0 h(S)>0, and components are counted in the parity lattice. For n = 11 n=11 only N 11 N_{11} is recorded; per-sequence statistics for n = 11 n=11 were not enumerated.

For 2 ≤ n ≤ 10 2\leq n\leq 10 the unique maximizer of | K S | |K_{S}| is the doubling sequence U n U_{n}, and the unique minimizer is L n L_{n}. The fraction of defective sequences grows from 1 / 6 ≈ 17 % 1/6\approx 17\% at n = 5 n=5 to 322054 / 559127 ≈ 57.6 % 322054/559127\approx 57.6\% at n = 10 n=10.

### 14.1 OEIS connections

The enumeration N n = | 𝒢 n | N_{n}=|\mathcal{G}_{n}| coincides, after an index shift, with OEIS [20] (“number of positive increasing integer sequences of length n n with Gilbreath transform ( 1, 1, 1, …) (1,1,1,\ldots) ”), whose terms are 1, 1, 1, 2, 6, 27, 180, 1786, 26094, 559127, 17535396, … 1,1,1,2,6,27,180,1786,26094,559127,17535396,\ldots. This provides an independent confirmation of our corrected values N 2, …, N 11 = 1, 1, 2, 6, 27, 180, 1786, 26094, 559127, 17535396 N_{2},\ldots,N_{11}=1,1,2,6,27,180,1786,26094,559127,17535396, and we attribute the enumeration to that entry rather than claiming it as new. A comment of T. D. Noe on [20] further records that the extremal (slowest- and fastest-growing) length- n n sequences are the minimal sequence and the doubling sequence, consistent with our Theorems 25 and 29.

By contrast, we did not find OEIS entries matching the interval-complete counts

 | 1, 1, 2, 5, 22, 120, 1026, 12782, 237073, 1,1,2,5,22,120,1026,12782,237073, |  |

the maximum-defect sequence

 | 0, 0, 0, 1, 5, 15, 47, 121, 281, 0,0,0,1,5,15,47,121,281, |  |

or the V n V_{n} extension-set width 5 ⋅ 2 n − 4 5\cdot 2^{n-4}; to the best of our knowledge the structural theory of K S K_{S} developed here (interval-completeness criterion, holes, defect, and the V n V_{n} family) is new. For broader context on the iterated-difference and difference-triangle literature, related OEIS entries include A036262 [18] (the Gilbreath array of the primes), A036261 [17] (the corresponding iterated absolute differences), A054977 [19] (the conjectured leftmost column), A173816 [21] (row sums), and A347924–A347925 [22, 23] (Gatti polynomial coefficient numerators and denominators). None of these coincide with the interval-complete, defect, or component sequences above. As exhaustive sequence search is delicate, we would welcome verification of these originality claims.

## 15 Discussion

The framework of this paper has three complementary readings.

From the additive-combinatorics side, the signed-sum set associated to a finite Gilbreath sequence is a subset-sum set (Theorem 12), and the coincidence S ± = C S S_{\pm}=C_{S} is governed by the classical Brown completeness criterion applied to the weight multiset W S = { e 1, …, e n − 1, 1 } W_{S}=\{e_{1},\ldots,e_{n-1},1\}. The interval-completeness criterion of Theorem 20 is the ordered analogue of Brown’s criterion: the same “next weight is at most one plus the sum of previous weights” shape, but read in the fixed anti-diagonal order forced by the folding recurrence.

From the dynamical-systems side, the valid distance set is the fiber over the apex value 1 1 of an ordered composition of folding maps x ↦ | x − e i | x\mapsto|x-e_{i}|. The reverse-tree algorithm of Section 8 solves the corresponding inverse problem explicitly. This places the work alongside the Proth–Gilbreath operator analysis of Bhat, Cobeli, and Zaharescu [2], which studies the forward dynamics of the same triangle. Our results contribute the structural analysis of the inverse direction for finite prefixes.

From the probabilistic side, the conjectures recorded in Section 16 ask for the asymptotic distribution of the defect and component count over a uniformly random sequence S ∈ 𝒢 n S\in\mathcal{G}_{n}. These are the finite, deterministic counterparts of the small-gap probabilistic questions resolved by Chase [7], who studies whether infinite sequences with random small gaps are Gilbreath. The framework of this paper makes such finite-distribution questions concrete: each one is a statement about the distribution of F S − 1 ​ ( { 1 }) F_{S}^{-1}(\{1\}) as S S ranges over 𝒢 n \mathcal{G}_{n}.

In all three readings the central object is the same. The interval-completeness theorem is simultaneously a sharp completeness criterion for an ordered subset-sum problem, a structure theorem for finite fibers of folding-map compositions, and a deterministic companion to the random Gilbreath models studied recently.

## 16 Open questions

1. (1)

(Conjecture 30) Is M n = 2 n − 1 + 1 M_{n}=2^{n-1}+1 for all n n, uniquely achieved by U n U_{n}?

2. (2)

Asymptotics of p n:= #⁡ { S ∈ 𝒢 n: h ⁡ ( S) = 0 } / N n p_{n}:=\#\{S\in\mathcal{G}_{n}:h(S)=0\}/N_{n}. Data through n = 10 n=10 shows

 | p n = 1, 1, 1, 5 6, 22 27, 120 180, 1026 1786, 12782 26094, 237073 559127 ≈ 0.424. p_{n}=1,\,1,\,1,\,\tfrac{5}{6},\,\tfrac{22}{27},\,\tfrac{120}{180},\,\tfrac{1026}{1786},\,\tfrac{12782}{26094},\,\tfrac{237073}{559127}\;\approx\;0.424. |  |

Does p n p_{n} tend to a limit? More generally, what are the asymptotic distributions of h ⁡ ( S) h(S), | K S | |K_{S}|, and #​ comp ​ ( K S) \#\textup{comp}(K_{S}) under uniform sampling on 𝒢 n \mathcal{G}_{n}? These are finite, deterministic analogues of the probabilistic Gilbreath questions resolved by Chase [7].

3. (3)

Closed form for max S ∈ 𝒢 n ⁡ h ⁡ ( S) \max_{S\in\mathcal{G}_{n}}h(S). The lower bound 3 ⋅ 2 n − 4 − 2 ​ n + 5 3\cdot 2^{n-4}-2n+5 from Corollary 36 is not tight.

4. (4)

Is max S ∈ 𝒢 n ⁡ #​ comp ​ ( K S) = 2 n − 4 \max_{S\in\mathcal{G}_{n}}\#\textup{comp}(K_{S})=2^{n-4} for all n ≥ 5 n\geq 5? Verified for n ≤ 10 n\leq 10.

5. (5)

Stability classification near the minimum: characterize S ∈ 𝒢 n S\in\mathcal{G}_{n} with | K S | ≤ 9 |K_{S}|\leq 9.

## 17 Reproducible code

The following Python module computes the data in Table 1 using only the right anti-diagonal state rather than repeatedly storing and rebuilding full difference triangles. This makes the computation substantially faster than a direct triangle-based reference implementation. The program also verifies the first-hole example and computes N 11 N_{11} by summing the number of increasing valid extensions from the length- 10 10 frontier.

[⬇][3]

from functools import lru_cache

def preimage_step ( e, T):

"" "

Preimages of T under x -> |x-e|, with x >= 0.

For each t in T, the solutions are x=e+t and, if e>=t, x=e-t.

" ""

out = set ()

for t in T:

out. add ( e + t)

if e >= t:

out. add ( e - t)

return tuple ( sorted ( out))

@lru_cache ( maxsize = None)

def valid_distances_from_antidiagonal ( e_tuple):

"" "

Given the right anti-diagonal (e_1,...,e_{n-1}), return

D_S = {|k-s_n|: k in K_S}.

" ""

T = (1,)

for e in reversed ( e_tuple):

T = preimage_step ( e, T)

return T

def child_antidiagonal ( e_tuple, d):

"" "

If d=|k-s_n| is a valid positive distance and k=s_n+d, return the

right anti-diagonal after appending k.

Old anti-diagonal: (e_1,...,e_{n-1}).

New anti-diagonal: (d, |d-e_1|, ||d-e_1|-e_2|,..., 1).

" ""

r = d

new_e = [r]

for e in e_tuple:

r = abs ( r - e)

new_e. append ( r)

assert new_e [-1] == 1

return tuple ( new_e)

def width_from_distances ( D):

"" "

Full extension width |K_S| from the distance set D.

Distance 0 contributes one extension; each positive distance

contributes two symmetric extensions.

" ""

return 2 *len ( D) - (1 if 0 in D else 0)

def valid_extensions_from_state ( sn, e_tuple):

"" "

Full two-sided valid-extension set K_S.

" ""

D = valid_distances_from_antidiagonal ( e_tuple)

out = set ()

for d in D:

out. add ( sn + d)

out. add ( sn - d)

return tuple ( sorted ( out))

def candidate_set_from_state ( sn, e_tuple):

"" "

Candidate set C_S.

" ""

A = sum ( e_tuple)

return tuple ( k for k in range ( sn - A - 1, sn + A + 2)

if ( k - sn) % 2 == 0)

def is_interval_complete ( e_tuple):

"" "

Check the criterion e_i <= 1 + sum_{j>i} e_j for all i<=n-2.

Here e_tuple = (e_1,...,e_{n-1}).

" ""

tail_sum = e_tuple [-1] #e_{n-1}=1

for e in reversed ( e_tuple [:-1]):

if e > 1 + tail_sum:

return False

tail_sum += e

return True

def components_count ( vals, step =2):

"" "

Number of connected components in one parity lattice.

" ""

vals = sorted ( set ( vals))

if not vals:

return 0

count = 1

for a, b in zip ( vals, vals [1:]):

if b - a!= step:

count += 1

return count

def K_components_count ( sn, e_tuple):

"" "

Number of connected components of K_S in the parity lattice.

" ""

return components_count ( valid_extensions_from_state ( sn, e_tuple), step =2)

def generate_states ( max_n):

"" "

Generate states for G_n up to max_n.

A state is (s_n, e_tuple, seq), where:

s_n = last term,

e_tuple = right anti-diagonal,

seq = full sequence, kept only for reporting examples.

" ""

states = [(3, (1,), (2, 3))]

by_n = {2: states }

for n in range (3, max_n + 1):

next_states = []

for sn, e_tuple, seq in states:

D = valid_distances_from_antidiagonal ( e_tuple)

for d in D:

if d > 0: #increasing extension k=s_n+d

k = sn + d

new_e = child_antidiagonal ( e_tuple, d)

next_states. append (( k, new_e, seq + ( k,)))

states = next_states

by_n [n] = states

print ( f "generated G_{n}: {len(states)} sequences")

return by_n

def summarize_states ( states):

"" "

Compute one row of the numerical data table.

" ""

N = len ( states)

min_width = None

max_width = None

num_min = 0

num_max = 0

num_complete = 0

num_defective = 0

max_defect = 0

max_components = 0

min_seq = None

max_seq = None

max_defect_seq = None

max_components_seq = None

for sn, e_tuple, seq in states:

D = valid_distances_from_antidiagonal ( e_tuple)

width = width_from_distances ( D)

defect = sum ( e_tuple) + 2 - width

comp = K_components_count ( sn, e_tuple)

if min_width is None or width < min_width:

min_width = width

num_min = 1

min_seq = seq

elif width == min_width:

num_min += 1

if max_width is None or width > max_width:

max_width = width

num_max = 1

max_seq = seq

elif width == max_width:

num_max += 1

if is_interval_complete ( e_tuple):

num_complete += 1

else:

num_defective += 1

if defect > max_defect:

max_defect = defect

max_defect_seq = seq

if comp > max_components:

max_components = comp

max_components_seq = seq

return {

"N": N,

"min_width": min_width,

"num_min": num_min,

"min_seq": min_seq,

"max_width": max_width,

"num_max": num_max,

"max_seq": max_seq,

"num_complete": num_complete,

"num_defective": num_defective,

"max_defect": max_defect,

"max_defect_seq": max_defect_seq,

"max_components": max_components,

"max_components_seq": max_components_seq,

}

def print_table ( by_n):

"" "

Print the table data for n=2,...,10.

" ""

header = (

"n | N_n | m_n | #min | M_n | #max | "

"#ic | #def | max def | max comp | max seq"

)

print ( header)

print ( "-" *len ( header))

for n in range (2, 11):

stats = summarize_states ( by_n [n])

print (

n,

stats ["N"],

stats ["min_width"],

stats ["num_min"],

stats ["max_width"],

stats ["num_max"],

stats ["num_complete"],

stats ["num_defective"],

stats ["max_defect"],

stats ["max_components"],

stats ["max_seq"],

sep = " | "

)

def compute_N_next ( states):

"" "

Given states for G_n, compute N_{n+1} by summing the number of

positive valid distances.

" ""

total = 0

for sn, e_tuple, seq in states:

D = valid_distances_from_antidiagonal ( e_tuple)

total += sum (1 for d in D if d > 0)

return total

def verify_first_hole ():

"" "

Verify the first-hole example S=(2,3,5,9,15).

" ""

S = (2, 3, 5, 9, 15)

sn = 15

e_tuple = (6, 2, 0, 1)

C = candidate_set_from_state ( sn, e_tuple)

K = valid_extensions_from_state ( sn, e_tuple)

H = tuple ( sorted ( set ( C) - set ( K)))

print ( "\nFirst-hole verification")

print ( "S =", S)

print ( "right anti-diagonal =", e_tuple)

print ( "A(S) =", sum ( e_tuple))

print ( "C_S =", C)

print ( "K_S =", K)

print ( "H_S =", H)

def V_sequence ( n):

"" "

The component-doubling family V_n.

" ""

assert n >= 5

return (2,) + tuple (2**( i -1) + 1 for i in range (2, n)) + (2**( n -1) - 1,)

def V_antidiagonal ( n):

"" "

Right anti-diagonal of V_n:

e_i = 2^{n-i-1}-2 for 1<=i<=n-2, and e_{n-1}=1.

" ""

assert n >= 5

return tuple (2**( n - i -1) - 2 for i in range (1, n -1)) + (1,)

def verify_V_family ( up_to =10):

"" "

Verify the V_n formulas for n=5,...,up_to.

" ""

print ( "\nV_n family verification")

print ( "n | V_n | |K| | components | defect")

for n in range (5, up_to + 1):

S = V_sequence ( n)

sn = S [-1]

e_tuple = V_antidiagonal ( n)

D = valid_distances_from_antidiagonal ( e_tuple)

width = width_from_distances ( D)

comp = K_components_count ( sn, e_tuple)

defect = sum ( e_tuple) + 2 - width

print ( n, S, width, comp, defect, sep = " | ")

if __name__ == "__main__":

by_n = generate_states (10)

print ()

print_table ( by_n)

N11 = compute_N_next ( by_n [10])

print ( "\nN_11 =", N11)

verify_first_hole ()

verify_V_family (10)

On a standard laptop, this anti-diagonal-state implementation produces the table through n = 10 n=10 and computes N 11 N_{11} in well under a minute. Runtime will vary by machine.

## Acknowledgments

This project made use of AI tools during the exploratory stage, including computational experimentation, conjecture generation, and preliminary drafting. The computational claims were verified against an independent implementation; responsibility for the mathematical statements and proofs rests with the author, and the arguments are offered for expert review.

## References

- [1] T. Agama, *On the gap sequence and Gilbreath’s conjecture*, preprint, arXiv:2104.05258 (2021).
- [2] R. N. Bhat, C. Cobeli, and A. Zaharescu, *Filtered rays over iterated absolute differences on layers of integers*, Chaos, Solitons & Fractals 178 (2024), 114315.
- [3] R. N. Bhat, C. Cobeli, and A. Zaharescu, *On quasi-periodicity in Proth–Gilbreath triangles*, Bull. Math. Soc. Sci. Math. Roumanie 67(115) (2024), no. 1, 3–21.
- [4] J. L. Brown, Jr., *Note on complete sequences of integers*, American Mathematical Monthly 68 (1961), no. 6, 557–560.
- [5] S. A. Burr and P. Erdős, *A Ramsey-type property in additive number theory*, Glasgow Mathematical Journal 27 (1985), 5–10.
- [6] M. Caragiu, A. Zaharescu, and M. Zaki, *An analogue of the Proth–Gilbreath conjecture*, Far East Journal of Mathematical Sciences 81 (2013), no. 1, 1–12.
- [7] Z. Chase, *A random analogue of Gilbreath’s conjecture*, Mathematische Annalen 388 (2024), 2611–2625. doi:10.1007/s00208-023-02579-w.
- [8] D. Chase, J. Hunter, and T. Tao, *Gilbreath’s conjecture, a Cramér random model, and a deterministic analysis*, preprint, arXiv:2607.08712 (2026).
- [9] D. Conlon, J. Fox, and H. T. Pham, *Subset sums, completeness and colorings*, preprint, arXiv:2104.14766 (2021).
- [10] M. Gardner, *Mathematical games: patterns in primes are a clue to the strong law of small numbers*, Scientific American 243 (1980), no. 6, 18–28.
- [11] R. Gatti, *Gilbreath equation, Gilbreath polynomials, and upper and lower bounds for Gilbreath conjecture*, Mathematics 11 (2023), no. 18, 4006.
- [12] V. Granville, *Piercing Gilbreath’s Conjecture: From Deep Number Theory Insights to Fintech and Cybersecurity*, preprint, arXiv:2607.04166 (2026).
- [13] R. K. Guy, *Unsolved Problems in Number Theory*, 3rd ed., Springer-Verlag, New York, 2004.
- [14] R. B. Killgrove and K. E. Ralston, *On a conjecture concerning the primes*, Mathematical Tables and Other Aids to Computation 13 (1959), 121–122.
- [15] H. L. Montgomery, *Ten Lectures on the Interface Between Analytic Number Theory and Harmonic Analysis*, CBMS Regional Conference Series in Mathematics 84, American Mathematical Society, Providence, RI, 1994.
- [16] A. M. Odlyzko, *Iterated absolute values of differences of consecutive primes*, Mathematics of Computation 61 (1993), no. 203, 373–380.
- [17] N. J. A. Sloane et al., *Sequence A036261*, The On-Line Encyclopedia of Integer Sequences, [https://oeis.org/A036261][4].
- [18] N. J. A. Sloane et al., *Sequence A036262*, The On-Line Encyclopedia of Integer Sequences, [https://oeis.org/A036262][5].
- [19] N. J. A. Sloane et al., *Sequence A054977*, The On-Line Encyclopedia of Integer Sequences, [https://oeis.org/A054977][6].
- [20] N. J. A. Sloane et al., *Sequence A080839*, The On-Line Encyclopedia of Integer Sequences, [https://oeis.org/A080839][7].
- [21] N. J. A. Sloane et al., *Sequence A173816*, The On-Line Encyclopedia of Integer Sequences, [https://oeis.org/A173816][8].
- [22] N. J. A. Sloane et al., *Sequence A347924*, The On-Line Encyclopedia of Integer Sequences, [https://oeis.org/A347924][9].
- [23] N. J. A. Sloane et al., *Sequence A347925*, The On-Line Encyclopedia of Integer Sequences, [https://oeis.org/A347925][10].


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: data:text/plain;base64,ZnJvbSBmdW5jdG9vbHMgaW1wb3J0IGxydV9jYWNoZQoKZGVmIHByZWltYWdlX3N0ZXAoZSwgVCk6CiAgICAiIiIKICAgIFByZWltYWdlcyBvZiBUIHVuZGVyIHggLT4gfHgtZXwsIHdpdGggeCA+PSAwLgogICAgRm9yIGVhY2ggdCBpbiBULCB0aGUgc29sdXRpb25zIGFyZSB4PWUrdCBhbmQsIGlmIGU+PXQsIHg9ZS10LgogICAgIiIiCiAgICBvdXQgPSBzZXQoKQogICAgZm9yIHQgaW4gVDoKICAgICAgICBvdXQuYWRkKGUgKyB0KQogICAgICAgIGlmIGUgPj0gdDoKICAgICAgICAgICAgb3V0LmFkZChlIC0gdCkKICAgIHJldHVybiB0dXBsZShzb3J0ZWQob3V0KSkKCkBscnVfY2FjaGUobWF4c2l6ZT1Ob25lKQpkZWYgdmFsaWRfZGlzdGFuY2VzX2Zyb21fYW50aWRpYWdvbmFsKGVfdHVwbGUpOgogICAgIiIiCiAgICBHaXZlbiB0aGUgcmlnaHQgYW50aS1kaWFnb25hbCAoZV8xLC4uLixlX3tuLTF9KSwgcmV0dXJuCiAgICBEX1MgPSB7fGstc19ufCA6IGsgaW4gS19TfS4KICAgICIiIgogICAgVCA9ICgxLCkKICAgIGZvciBlIGluIHJldmVyc2VkKGVfdHVwbGUpOgogICAgICAgIFQgPSBwcmVpbWFnZV9zdGVwKGUsIFQpCiAgICByZXR1cm4gVAoKZGVmIGNoaWxkX2FudGlkaWFnb25hbChlX3R1cGxlLCBkKToKICAgICIiIgogICAgSWYgZD18ay1zX258IGlzIGEgdmFsaWQgcG9zaXRpdmUgZGlzdGFuY2UgYW5kIGs9c19uK2QsIHJldHVybiB0aGUKICAgIHJpZ2h0IGFudGktZGlhZ29uYWwgYWZ0ZXIgYXBwZW5kaW5nIGsuCgogICAgT2xkIGFudGktZGlhZ29uYWw6IChlXzEsLi4uLGVfe24tMX0pLgogICAgTmV3IGFudGktZGlhZ29uYWw6IChkLCB8ZC1lXzF8LCB8fGQtZV8xfC1lXzJ8LCAuLi4sIDEpLgogICAgIiIiCiAgICByID0gZAogICAgbmV3X2UgPSBbcl0KICAgIGZvciBlIGluIGVfdHVwbGU6CiAgICAgICAgciA9IGFicyhyIC0gZSkKICAgICAgICBuZXdfZS5hcHBlbmQocikKICAgIGFzc2VydCBuZXdfZVstMV0gPT0gMQogICAgcmV0dXJuIHR1cGxlKG5ld19lKQoKZGVmIHdpZHRoX2Zyb21fZGlzdGFuY2VzKEQpOgogICAgIiIiCiAgICBGdWxsIGV4dGVuc2lvbiB3aWR0aCB8S19TfCBmcm9tIHRoZSBkaXN0YW5jZSBzZXQgRC4KICAgIERpc3RhbmNlIDAgY29udHJpYnV0ZXMgb25lIGV4dGVuc2lvbjsgZWFjaCBwb3NpdGl2ZSBkaXN0YW5jZQogICAgY29udHJpYnV0ZXMgdHdvIHN5bW1ldHJpYyBleHRlbnNpb25zLgogICAgIiIiCiAgICByZXR1cm4gMiAqIGxlbihEKSAtICgxIGlmIDAgaW4gRCBlbHNlIDApCgpkZWYgdmFsaWRfZXh0ZW5zaW9uc19mcm9tX3N0YXRlKHNuLCBlX3R1cGxlKToKICAgICIiIgogICAgRnVsbCB0d28tc2lkZWQgdmFsaWQtZXh0ZW5zaW9uIHNldCBLX1MuCiAgICAiIiIKICAgIEQgPSB2YWxpZF9kaXN0YW5jZXNfZnJvbV9hbnRpZGlhZ29uYWwoZV90dXBsZSkKICAgIG91dCA9IHNldCgpCiAgICBmb3IgZCBpbiBEOgogICAgICAgIG91dC5hZGQoc24gKyBkKQogICAgICAgIG91dC5hZGQoc24gLSBkKQogICAgcmV0dXJuIHR1cGxlKHNvcnRlZChvdXQpKQoKZGVmIGNhbmRpZGF0ZV9zZXRfZnJvbV9zdGF0ZShzbiwgZV90dXBsZSk6CiAgICAiIiIKICAgIENhbmRpZGF0ZSBzZXQgQ19TLgogICAgIiIiCiAgICBBID0gc3VtKGVfdHVwbGUpCiAgICByZXR1cm4gdHVwbGUoayBmb3IgayBpbiByYW5nZShzbiAtIEEgLSAxLCBzbiArIEEgKyAyKQogICAgICAgICAgICAgICAgIGlmIChrIC0gc24pICUgMiA9PSAwKQoKZGVmIGlzX2ludGVydmFsX2NvbXBsZXRlKGVfdHVwbGUpOgogICAgIiIiCiAgICBDaGVjayB0aGUgY3JpdGVyaW9uIGVfaSA8PSAxICsgc3VtX3tqPml9IGVfaiBmb3IgYWxsIGk8PW4tMi4KICAgIEhlcmUgZV90dXBsZSA9IChlXzEsLi4uLGVfe24tMX0pLgogICAgIiIiCiAgICB0YWlsX3N1bSA9IGVfdHVwbGVbLTFdICAjIGVfe24tMX09MQogICAgZm9yIGUgaW4gcmV2ZXJzZWQoZV90dXBsZVs6LTFdKToKICAgICAgICBpZiBlID4gMSArIHRhaWxfc3VtOgogICAgICAgICAgICByZXR1cm4gRmFsc2UKICAgICAgICB0YWlsX3N1bSArPSBlCiAgICByZXR1cm4gVHJ1ZQoKZGVmIGNvbXBvbmVudHNfY291bnQodmFscywgc3RlcD0yKToKICAgICIiIgogICAgTnVtYmVyIG9mIGNvbm5lY3RlZCBjb21wb25lbnRzIGluIG9uZSBwYXJpdHkgbGF0dGljZS4KICAgICIiIgogICAgdmFscyA9IHNvcnRlZChzZXQodmFscykpCiAgICBpZiBub3QgdmFsczoKICAgICAgICByZXR1cm4gMAogICAgY291bnQgPSAxCiAgICBmb3IgYSwgYiBpbiB6aXAodmFscywgdmFsc1sxOl0pOgogICAgICAgIGlmIGIgLSBhICE9IHN0ZXA6CiAgICAgICAgICAgIGNvdW50ICs9IDEKICAgIHJldHVybiBjb3VudAoKZGVmIEtfY29tcG9uZW50c19jb3VudChzbiwgZV90dXBsZSk6CiAgICAiIiIKICAgIE51bWJlciBvZiBjb25uZWN0ZWQgY29tcG9uZW50cyBvZiBLX1MgaW4gdGhlIHBhcml0eSBsYXR0aWNlLgogICAgIiIiCiAgICByZXR1cm4gY29tcG9uZW50c19jb3VudCh2YWxpZF9leHRlbnNpb25zX2Zyb21fc3RhdGUoc24sIGVfdHVwbGUpLCBzdGVwPTIpCgpkZWYgZ2VuZXJhdGVfc3RhdGVzKG1heF9uKToKICAgICIiIgogICAgR2VuZXJhdGUgc3RhdGVzIGZvciBHX24gdXAgdG8gbWF4X24uCgogICAgQSBzdGF0ZSBpcyAoc19uLCBlX3R1cGxlLCBzZXEpLCB3aGVyZToKICAgICAgc19uICAgICA9IGxhc3QgdGVybSwKICAgICAgZV90dXBsZSA9IHJpZ2h0IGFudGktZGlhZ29uYWwsCiAgICAgIHNlcSAgICAgPSBmdWxsIHNlcXVlbmNlLCBrZXB0IG9ubHkgZm9yIHJlcG9ydGluZyBleGFtcGxlcy4KICAgICIiIgogICAgc3RhdGVzID0gWygzLCAoMSwpLCAoMiwgMykpXQogICAgYnlfbiA9IHsyOiBzdGF0ZXN9CgogICAgZm9yIG4gaW4gcmFuZ2UoMywgbWF4X24gKyAxKToKICAgICAgICBuZXh0X3N0YXRlcyA9IFtdCiAgICAgICAgZm9yIHNuLCBlX3R1cGxlLCBzZXEgaW4gc3RhdGVzOgogICAgICAgICAgICBEID0gdmFsaWRfZGlzdGFuY2VzX2Zyb21fYW50aWRpYWdvbmFsKGVfdHVwbGUpCiAgICAgICAgICAgIGZvciBkIGluIEQ6CiAgICAgICAgICAgICAgICBpZiBkID4gMDogICMgaW5jcmVhc2luZyBleHRlbnNpb24gaz1zX24rZAogICAgICAgICAgICAgICAgICAgIGsgPSBzbiArIGQKICAgICAgICAgICAgICAgICAgICBuZXdfZSA9IGNoaWxkX2FudGlkaWFnb25hbChlX3R1cGxlLCBkKQogICAgICAgICAgICAgICAgICAgIG5leHRfc3RhdGVzLmFwcGVuZCgoaywgbmV3X2UsIHNlcSArIChrLCkpKQogICAgICAgIHN0YXRlcyA9IG5leHRfc3RhdGVzCiAgICAgICAgYnlfbltuXSA9IHN0YXRlcwogICAgICAgIHByaW50KGYiZ2VuZXJhdGVkIEdfe259OiB7bGVuKHN0YXRlcyl9IHNlcXVlbmNlcyIpCgogICAgcmV0dXJuIGJ5X24KCmRlZiBzdW1tYXJpemVfc3RhdGVzKHN0YXRlcyk6CiAgICAiIiIKICAgIENvbXB1dGUgb25lIHJvdyBvZiB0aGUgbnVtZXJpY2FsIGRhdGEgdGFibGUuCiAgICAiIiIKICAgIE4gPSBsZW4oc3RhdGVzKQoKICAgIG1pbl93aWR0aCA9IE5vbmUKICAgIG1heF93aWR0aCA9IE5vbmUKICAgIG51bV9taW4gPSAwCiAgICBudW1fbWF4ID0gMAoKICAgIG51bV9jb21wbGV0ZSA9IDAKICAgIG51bV9kZWZlY3RpdmUgPSAwCiAgICBtYXhfZGVmZWN0ID0gMAogICAgbWF4X2NvbXBvbmVudHMgPSAwCgogICAgbWluX3NlcSA9IE5vbmUKICAgIG1heF9zZXEgPSBOb25lCiAgICBtYXhfZGVmZWN0X3NlcSA9IE5vbmUKICAgIG1heF9jb21wb25lbnRzX3NlcSA9IE5vbmUKCiAgICBmb3Igc24sIGVfdHVwbGUsIHNlcSBpbiBzdGF0ZXM6CiAgICAgICAgRCA9IHZhbGlkX2Rpc3RhbmNlc19mcm9tX2FudGlkaWFnb25hbChlX3R1cGxlKQogICAgICAgIHdpZHRoID0gd2lkdGhfZnJvbV9kaXN0YW5jZXMoRCkKICAgICAgICBkZWZlY3QgPSBzdW0oZV90dXBsZSkgKyAyIC0gd2lkdGgKICAgICAgICBjb21wID0gS19jb21wb25lbnRzX2NvdW50KHNuLCBlX3R1cGxlKQoKICAgICAgICBpZiBtaW5fd2lkdGggaXMgTm9uZSBvciB3aWR0aCA8IG1pbl93aWR0aDoKICAgICAgICAgICAgbWluX3dpZHRoID0gd2lkdGgKICAgICAgICAgICAgbnVtX21pbiA9IDEKICAgICAgICAgICAgbWluX3NlcSA9IHNlcQogICAgICAgIGVsaWYgd2lkdGggPT0gbWluX3dpZHRoOgogICAgICAgICAgICBudW1fbWluICs9IDEKCiAgICAgICAgaWYgbWF4X3dpZHRoIGlzIE5vbmUgb3Igd2lkdGggPiBtYXhfd2lkdGg6CiAgICAgICAgICAgIG1heF93aWR0aCA9IHdpZHRoCiAgICAgICAgICAgIG51bV9tYXggPSAxCiAgICAgICAgICAgIG1heF9zZXEgPSBzZXEKICAgICAgICBlbGlmIHdpZHRoID09IG1heF93aWR0aDoKICAgICAgICAgICAgbnVtX21heCArPSAxCgogICAgICAgIGlmIGlzX2ludGVydmFsX2NvbXBsZXRlKGVfdHVwbGUpOgogICAgICAgICAgICBudW1fY29tcGxldGUgKz0gMQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIG51bV9kZWZlY3RpdmUgKz0gMQoKICAgICAgICBpZiBkZWZlY3QgPiBtYXhfZGVmZWN0OgogICAgICAgICAgICBtYXhfZGVmZWN0ID0gZGVmZWN0CiAgICAgICAgICAgIG1heF9kZWZlY3Rfc2VxID0gc2VxCgogICAgICAgIGlmIGNvbXAgPiBtYXhfY29tcG9uZW50czoKICAgICAgICAgICAgbWF4X2NvbXBvbmVudHMgPSBjb21wCiAgICAgICAgICAgIG1heF9jb21wb25lbnRzX3NlcSA9IHNlcQoKICAgIHJldHVybiB7CiAgICAgICAgIk4iOiBOLAogICAgICAgICJtaW5fd2lkdGgiOiBtaW5fd2lkdGgsCiAgICAgICAgIm51bV9taW4iOiBudW1fbWluLAogICAgICAgICJtaW5fc2VxIjogbWluX3NlcSwKICAgICAgICAibWF4X3dpZHRoIjogbWF4X3dpZHRoLAogICAgICAgICJudW1fbWF4IjogbnVtX21heCwKICAgICAgICAibWF4X3NlcSI6IG1heF9zZXEsCiAgICAgICAgIm51bV9jb21wbGV0ZSI6IG51bV9jb21wbGV0ZSwKICAgICAgICAibnVtX2RlZmVjdGl2ZSI6IG51bV9kZWZlY3RpdmUsCiAgICAgICAgIm1heF9kZWZlY3QiOiBtYXhfZGVmZWN0LAogICAgICAgICJtYXhfZGVmZWN0X3NlcSI6IG1heF9kZWZlY3Rfc2VxLAogICAgICAgICJtYXhfY29tcG9uZW50cyI6IG1heF9jb21wb25lbnRzLAogICAgICAgICJtYXhfY29tcG9uZW50c19zZXEiOiBtYXhfY29tcG9uZW50c19zZXEsCiAgICB9CgpkZWYgcHJpbnRfdGFibGUoYnlfbik6CiAgICAiIiIKICAgIFByaW50IHRoZSB0YWJsZSBkYXRhIGZvciBuPTIsLi4uLDEwLgogICAgIiIiCiAgICBoZWFkZXIgPSAoCiAgICAgICAgIm4gfCBOX24gfCBtX24gfCAjbWluIHwgTV9uIHwgI21heCB8ICIKICAgICAgICAiI2ljIHwgI2RlZiB8IG1heCBkZWYgfCBtYXggY29tcCB8IG1heCBzZXEiCiAgICApCiAgICBwcmludChoZWFkZXIpCiAgICBwcmludCgiLSIgKiBsZW4oaGVhZGVyKSkKCiAgICBmb3IgbiBpbiByYW5nZSgyLCAxMSk6CiAgICAgICAgc3RhdHMgPSBzdW1tYXJpemVfc3RhdGVzKGJ5X25bbl0pCiAgICAgICAgcHJpbnQoCiAgICAgICAgICAgIG4sCiAgICAgICAgICAgIHN0YXRzWyJOIl0sCiAgICAgICAgICAgIHN0YXRzWyJtaW5fd2lkdGgiXSwKICAgICAgICAgICAgc3RhdHNbIm51bV9taW4iXSwKICAgICAgICAgICAgc3RhdHNbIm1heF93aWR0aCJdLAogICAgICAgICAgICBzdGF0c1sibnVtX21heCJdLAogICAgICAgICAgICBzdGF0c1sibnVtX2NvbXBsZXRlIl0sCiAgICAgICAgICAgIHN0YXRzWyJudW1fZGVmZWN0aXZlIl0sCiAgICAgICAgICAgIHN0YXRzWyJtYXhfZGVmZWN0Il0sCiAgICAgICAgICAgIHN0YXRzWyJtYXhfY29tcG9uZW50cyJdLAogICAgICAgICAgICBzdGF0c1sibWF4X3NlcSJdLAogICAgICAgICAgICBzZXA9IiB8ICIKICAgICAgICApCgpkZWYgY29tcHV0ZV9OX25leHQoc3RhdGVzKToKICAgICIiIgogICAgR2l2ZW4gc3RhdGVzIGZvciBHX24sIGNvbXB1dGUgTl97bisxfSBieSBzdW1taW5nIHRoZSBudW1iZXIgb2YKICAgIHBvc2l0aXZlIHZhbGlkIGRpc3RhbmNlcy4KICAgICIiIgogICAgdG90YWwgPSAwCiAgICBmb3Igc24sIGVfdHVwbGUsIHNlcSBpbiBzdGF0ZXM6CiAgICAgICAgRCA9IHZhbGlkX2Rpc3RhbmNlc19mcm9tX2FudGlkaWFnb25hbChlX3R1cGxlKQogICAgICAgIHRvdGFsICs9IHN1bSgxIGZvciBkIGluIEQgaWYgZCA+IDApCiAgICByZXR1cm4gdG90YWwKCmRlZiB2ZXJpZnlfZmlyc3RfaG9sZSgpOgogICAgIiIiCiAgICBWZXJpZnkgdGhlIGZpcnN0LWhvbGUgZXhhbXBsZSBTPSgyLDMsNSw5LDE1KS4KICAgICIiIgogICAgUyA9ICgyLCAzLCA1LCA5LCAxNSkKICAgIHNuID0gMTUKICAgIGVfdHVwbGUgPSAoNiwgMiwgMCwgMSkKCiAgICBDID0gY2FuZGlkYXRlX3NldF9mcm9tX3N0YXRlKHNuLCBlX3R1cGxlKQogICAgSyA9IHZhbGlkX2V4dGVuc2lvbnNfZnJvbV9zdGF0ZShzbiwgZV90dXBsZSkKICAgIEggPSB0dXBsZShzb3J0ZWQoc2V0KEMpIC0gc2V0KEspKSkKCiAgICBwcmludCgiXG5GaXJzdC1ob2xlIHZlcmlmaWNhdGlvbiIpCiAgICBwcmludCgiUyA9IiwgUykKICAgIHByaW50KCJyaWdodCBhbnRpLWRpYWdvbmFsID0iLCBlX3R1cGxlKQogICAgcHJpbnQoIkEoUykgPSIsIHN1bShlX3R1cGxlKSkKICAgIHByaW50KCJDX1MgPSIsIEMpCiAgICBwcmludCgiS19TID0iLCBLKQogICAgcHJpbnQoIkhfUyA9IiwgSCkKCmRlZiBWX3NlcXVlbmNlKG4pOgogICAgIiIiCiAgICBUaGUgY29tcG9uZW50LWRvdWJsaW5nIGZhbWlseSBWX24uCiAgICAiIiIKICAgIGFzc2VydCBuID49IDUKICAgIHJldHVybiAoMiwpICsgdHVwbGUoMioqKGktMSkgKyAxIGZvciBpIGluIHJhbmdlKDIsIG4pKSArICgyKioobi0xKSAtIDEsKQoKZGVmIFZfYW50aWRpYWdvbmFsKG4pOgogICAgIiIiCiAgICBSaWdodCBhbnRpLWRpYWdvbmFsIG9mIFZfbjoKICAgIGVfaSA9IDJee24taS0xfS0yIGZvciAxPD1pPD1uLTIsIGFuZCBlX3tuLTF9PTEuCiAgICAiIiIKICAgIGFzc2VydCBuID49IDUKICAgIHJldHVybiB0dXBsZSgyKioobi1pLTEpIC0gMiBmb3IgaSBpbiByYW5nZSgxLCBuLTEpKSArICgxLCkKCmRlZiB2ZXJpZnlfVl9mYW1pbHkodXBfdG89MTApOgogICAgIiIiCiAgICBWZXJpZnkgdGhlIFZfbiBmb3JtdWxhcyBmb3Igbj01LC4uLix1cF90by4KICAgICIiIgogICAgcHJpbnQoIlxuVl9uIGZhbWlseSB2ZXJpZmljYXRpb24iKQogICAgcHJpbnQoIm4gfCBWX24gfCB8S3wgfCBjb21wb25lbnRzIHwgZGVmZWN0IikKICAgIGZvciBuIGluIHJhbmdlKDUsIHVwX3RvICsgMSk6CiAgICAgICAgUyA9IFZfc2VxdWVuY2UobikKICAgICAgICBzbiA9IFNbLTFdCiAgICAgICAgZV90dXBsZSA9IFZfYW50aWRpYWdvbmFsKG4pCiAgICAgICAgRCA9IHZhbGlkX2Rpc3RhbmNlc19mcm9tX2FudGlkaWFnb25hbChlX3R1cGxlKQogICAgICAgIHdpZHRoID0gd2lkdGhfZnJvbV9kaXN0YW5jZXMoRCkKICAgICAgICBjb21wID0gS19jb21wb25lbnRzX2NvdW50KHNuLCBlX3R1cGxlKQogICAgICAgIGRlZmVjdCA9IHN1bShlX3R1cGxlKSArIDIgLSB3aWR0aAogICAgICAgIHByaW50KG4sIFMsIHdpZHRoLCBjb21wLCBkZWZlY3QsIHNlcD0iIHwgIikKCmlmIF9fbmFtZV9fID09ICJfX21haW5fXyI6CiAgICBieV9uID0gZ2VuZXJhdGVfc3RhdGVzKDEwKQogICAgcHJpbnQoKQogICAgcHJpbnRfdGFibGUoYnlfbikKCiAgICBOMTEgPSBjb21wdXRlX05fbmV4dChieV9uWzEwXSkKICAgIHByaW50KCJcbk5fMTEgPSIsIE4xMSkKCiAgICB2ZXJpZnlfZmlyc3RfaG9sZSgpCiAgICB2ZXJpZnlfVl9mYW1pbHkoMTAp
[4]: https://oeis.org/A036261
[5]: https://oeis.org/A036262
[6]: https://oeis.org/A054977
[7]: https://oeis.org/A080839
[8]: https://oeis.org/A173816
[9]: https://oeis.org/A347924
[10]: https://oeis.org/A347925
