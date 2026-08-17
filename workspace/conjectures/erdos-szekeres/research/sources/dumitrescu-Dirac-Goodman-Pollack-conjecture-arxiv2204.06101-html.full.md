<!-- source: https://arxiv.org/html/2204.06101v3 | converted from HTML -->

The Dirac–Goodman–Pollack Conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2204.06101v3 [math.CO] 28 Aug 2022

# The Dirac–Goodman–Pollack Conjecture

Adrian Dumitrescu Thanks: Algoresearch L.L.C., Milwaukee, WI, USA. Email˜ ad.dumitrescu@gmail.com

###### Abstract

In one of their seminal articles on allowable sequences, Goodman and Pollack gave combinatorial generalizations for three problems in discrete geometry, one of which being the Dirac conjecture. According to this conjecture, any set of n n noncollinear points in the plane has a point incident to at least c ​ n cn connecting lines determined by the set. The notion of allowable sequences of permutations provides a natural combinatorial setting for analyzing these problems. Within this formalism, the conjectured generalization reads as follows: *Any nontrivial allowable n n -sequence Σ \Sigma has a local sequence Λ i \Lambda_{i} whose half-period is at least c ​ n cn.*The conjecture is confirmed here with a concrete bound c = 1 / 845 c=1/845. Several related problems are discussed.

Keywords: allowable sequence, Dirac’s conjecture, Sylvester’s problem, the crossing lemma, the Szemerédi–Trotter theorem, Székely’s method.

## 1 Introduction

In one of their seminal articles on allowable sequences [27] Goodman and Pollack gave combinatorial generalizations (left as conjectures) for the following three problems in discrete geometry:

1. A \mathrm{A}

the Erdős–Szekeres conjecture that any 2 n − 2 + 1 2^{n-2}+1 points in general position in the plane contains n n points in convex position,

2. B \mathrm{B}

the Dirac conjecture that any set of n n noncollinear points in the plane contains a point incident to at least c ​ n cn connecting lines determined by the set, for some constant c > 0 c>0,

3. C \mathrm{C}

the problem of finding the minimum number of directions determined by n n noncollinear points in the plane.

The notion of allowable sequences of permutations provides a natural combinatorial setting independent from geometry for analyzing these problems and making them more transparent. Within this formalism, the conjectured generalizations for the three statements above read as follows:

1. A ′ \mathrm{A^{\prime}}

[27] Let Σ \Sigma be an allowable 2 n − 2 + 1 2^{n-2}+1 -sequence in which only strings of length two are reversed. Then there are n n indices such that each occurs before or after the others in some term of Σ \Sigma.

2. B ′ \mathrm{B^{\prime}}

[27] Any nontrivial allowable n n -sequence Σ \Sigma has a local sequence Λ i \Lambda_{i} whose half-period is at least c ​ n cn, for some constant c > 0 c>0.

3. C ′ \mathrm{C^{\prime}}

[27] If Σ \Sigma is a nontrivial allowable n n -sequence, the half-period of Σ \Sigma is at least 2 ​ ⌊ n / 2 ⌋ 2\lfloor n/2\rfloor.

The formalism as well as our results will be made precise in Section 2, at the end of which we state our results and review the status of the three problems and their generalizations. It will be evident at that point that A ′ ⟹ A \mathrm{A^{\prime}}\implies\mathrm{A}, B ′ ⟹ B \mathrm{B^{\prime}}\implies\mathrm{B}, and C ′ ⟹ C \mathrm{C^{\prime}}\implies\mathrm{C}, though not conversely. Our goal in this paper is the proof of Statement B ′ \mathrm{B^{\prime}}.

### Connecting lines and a theorem of de Bruijn and Erdős.

Before discussing Dirac’s conjecture, it is natural to mention how this question appeared in the broader context of estimating the total number of connecting lines determined by a noncollinear point set (clearly the answer is 1 1 for collinear sets). Theorem 2 below provides the answer.

Historically, the study of point sets and their connecting lines draws from a question asked by Sylvester [52] about 50 50 years earlier: *For a finite set of points, not all on a line, does there always exist a line that contains exactly two of the points?*If the answer is positive, the corresponding equivalent statement would read: if for every pair of points in the set, the line determined by these points contains a third one, then all the points are collinear. Given a point set S S, a connecting line (i.e., a line determined by the set) is called *ordinary*if it contains precisely two points of S S; see also [7]. Sylvester problem got forgotten over time but was rediscovered by Erdős [16] in 1943 1943.

The first proof of existence of an ordinary line dates back to those times and it is now commonly referred to as the *Sylvester–Gallai Theorem*(solutions were found by several researchers). Its colorful history is recounted by Chvátal in his recent monograph [10]. Earlier accounts on its development can be found in [8, 11, 19, 34, 46].

###### Theorem 1.

(Sylvester–Gallai). Every set of n n noncollinear points in the plane admits an ordinary line.

Motzkin [40] was the first to show that the number of ordinary lines tends to infinity with n n. Further, Kelly and Moser [33] proved that there are at least 3 ​ n / 7 3n/7 ordinary lines, and Csima and Sawyer [11] raised this bound to 6 ​ n / 13 6n/13 for n ≥ 8 n\geq 8. Finally, Green and Tao [29] proved that if n n is sufficiently large then there are at least n / 2 n/2 ordinary lines, thereby settling the so called strong Dirac–Motzkin conjecture for large n n (even though neither of the authors seem to have conjectured this in print, see [29]). On the other hand, there are arbitrarily large points sets with no more than n / 2 n/2 ordinary lines: for even n n, take a regular n / 2 n/2 -gon, which determines n / 2 n/2 directions, and the n / 2 n/2 projective points corresponding to these directions; see [8, Ch. 7.2].

Erdős [16] deduced the following interesting corollary of Theorem 1. Here the term *near-pencil*describes a point set that is almost collinear, in the sense that all but of one the points are collinear.

###### Theorem 2.

(Erdős [16]). For a set of n n noncollinear points in the plane, the number of connecting lines is always at least n n; and it is equal to n n if and only if the points form a near-pencil.

In fact every other configuration determines more lines as quantified in the following result of Kelly and Moser [33].

###### Theorem 3.

(Kelly and Moser [33]). Let S S be a set of n n points and let λ = λ ⁡ ( S) \lambda=\lambda(S) denote the number of connecting lines. If at most n − k n-k points of S S are collinear and n > 1 2 ​ { 3 ​ ( 3 ​ k − 2) 2 + 3 ​ k − 1 } n>\frac{1}{2}\{3(3k-2)^{2}+3k-1\} then λ ≥ k ​ n − 1 2 ​ ( 3 ​ k + 2) ​ ( k − 1) \lambda\geq kn-\frac{1}{2}(3k+2)(k-1).

In particular ( k = 2 k=2), if at most n − 2 n-2 points are collinear and n ≥ 27 n\geq 27, the number of connecting lines is always at least 2 ​ n − 4 2n-4; the lower bound actually holds for n ≥ 10 n\geq 10, see [34, Ch. 6].

Perhaps even more interesting than Theorem 2 is the following result of de Bruijn and Erdős [18] from about the same time—which provides the same answer under more general circumstances that distill the essential features present in the theorem. See also [37, Ch. 19], [44].

###### Theorem 4.

(de Bruijn and Erdős [18]). Let ( V, E) (V,E), | V | = n |V|=n, | E | = m |E|=m, be a hypergraph, where every pair of elements in V V is contained in precisely one edge in E E. Then m ≥ n m\geq n, with equality if and only if (i) one of the sets contains all but one elements of V V and the others are two-element sets containing the remaining element; or (ii) E E is the system of lines of a finite projective plane defined on V V.

A result of Motzkin [41], Rabin, and Chakerian [9] states that any set of n n two-colored (say, by red or blue) noncollinear points in the plane determines a monochromatic line; see also [2, Ch. 13].

### Dirac’s conjecture.

For a noncollinear set S S of n n points in the plane, let t ⁡ ( S) t(S) be the minimum number of lines spanned be S S that are incident to a point in S S; let t ⁡ ( n) t(n) be the minimum of t ⁡ ( S) t(S) over all point sets of size n n. In a dual setting, for a set ℒ \mathcal{L} of n n lines in the plane, no two of which are parallel, let r ⁡ ( ℒ) r(\mathcal{L}) be the maximum number of crossing points (vertices of the line arrangement) on a line in ℒ \mathcal{L}.

G. A. Dirac [12] and T. S. Motzkin [40], independently of each other and at the same time proposed the following problem: Does every noncollinear set of points contain some point that is incident to at least n / 2 n/2 lines determined by the set? Initially Dirac proved that there are at least n + 1 \sqrt{n+1} lines incident to one of the points and conjectured the existence of a point incident to at least ⌊ n / 2 ⌋ \lfloor n/2\rfloor connecting lines. Several counterexamples were found by Grünbaum (for n = 9, 15, 19, 25, 31 n=9,15,19,25,31, and 37 37), see [30] and [11, F12], and so the conjecture has been modified [17] to read as follows:

###### Conjecture 1.

(Dirac). Given a set S S of n n noncolllinear points in the plane, there exists a point in S S incident to c ​ n cn lines determined by S S, for some constant c > 0 c>0.

From the other direction, Akiyama et al. [4] considered the problem of finding noncollinear point sets S S with t ⁡ ( S) ≤ ⌊ n / 2 ⌋ t(S)\leq\lfloor n/2\rfloor. They showed that for every n ≥ 8 n\geq 8 of the form n = 12 ​ k + r n=12k+r, r ≠ 11 r\neq 11, there exists a set S S of n n noncollinear points satisfying t ⁡ ( S) ≤ ⌊ n / 2 ⌋ t(S)\leq\lfloor n/2\rfloor. An infinite family of counterexamples to the strong Dirac conjecture was found by Felsner [8, p. 313]. In the dual setting it consists of 6 ​ k + 7 6k+7 lines in the real projective plane (r.p.p.) where no line is incident to more than 3 ​ k + 2 3k+2 points of intersection. In a stronger form—the so called *strong Dirac conjecture*—the bound is replaced by n / 2 − c n/2-c, where c > 0 c>0 is a constant [42]; see also [8, Ch. 7.3].

In 1983 1983 Beck [5] proved the following result and further observed that Conjecture 1 immediately follows from it.

###### Theorem 5.

(Beck [5]). Let S S be a set of n n points in the plane. If at most ℓ \ell points of S S are collinear, then S S determines at least Ω ⁡ ( n ⁡ ( n − ℓ)) \Omega(n(n-\ell)) distinct lines.

At about the same time Szemerédi and Trotter [54] obtained their classic result on the number of point-lines incidences in the plane: Theorem 6 or 7 below. Their result also implies Conjecture 1. Interestingly enough, as remarked by Székely [53], Beck obtained his result on connecting lines from a result weaker than the Szemerédi–Trotter theorem.

Here we give two equivalent formulations of the Szemerédi and Trotter result. Given a point set S S in ℝ 2 \mathbb{R}^{2}, for any integer k ≥ 2 k\geq 2, a line is called *k k -rich*if it is incident to at least k k points of S S.

###### Theorem 6.

(Szemerédi–Trotter [54]). The number of point-line incidences among n n points and ℓ \ell lines in ℝ 2 \mathbb{R}^{2} is

 | I ⁡ ( n, ℓ) = 𝒪 ⁡ ( n 2 / 3 ​ ℓ 2 / 3 + n + ℓ). I(n,\ell)=\mathcal{O}(n^{2/3}\ell^{2/3}+n+\ell). |  |

###### Theorem 7.

(Szemerédi–Trotter [54]). Given n n points in ℝ 2 \mathbb{R}^{2}, the number of k k -rich lines, k ≥ 2 k\geq 2, is

 | 𝒪 ⁡ ( n 2 / k 3 + n / k). \mathcal{O}\left(n^{2}/k^{3}+n/k\right). |  |

The resulting constants, however, in the above proofs for Conjecture 1 are quite small; for instance, the constant obtained in [54] is 10 − 1087 10^{-1087}; see also [34, Ch. 6]. New developments in the theory of geometric graphs have lead over time to better constants in Dirac’s conjecture. One such tool is the classic crossing lemma proved in the early 1980s by Ajtai, Chvátal, Newborn, and Szemerédi [3] and Leighton [36]. The sharper constant appearing at the end of the lemma was established recently by Ackerman [1] who improved an earlier bound by Pach, Radoičić, Tardos, and Tóth [45]; see also [46, Ch. 4].

###### Lemma 1.

(Ajtai, Chvátal, Newborn, and Szemerédi [3] Leighton [36], Ackerman [1]). Let G = ( V, E) G=(V,E), where | V | = n |V|=n, | E | = e |E|=e, be a simple graph with with n n vertices and e ≥ 4 ​ n e\geq 4n edges. Then cr ⁡ ( G) ≥ c ⋅ e 3 / n 2 {\rm cr}(G)\geq c\cdot e^{3}/n^{2}, for a suitable constant c > 0 c>0. In particular, one may take c = 1 / 64 c=1/64; and if e ≥ 6.95 ​ n e\geq 6.95n, then one may take c = 1 / 29 c=1/29.

Another key development is due to Székely [53], whose groundbreaking approach of constructing suitable graphs and running the crossing lemma machinery led to new bounds and improved constants in relation to Dirac’s conjecture, but in many other problems as well. For instance, using this approach, Payne [47] showed in his thesis that Conjecture 1 holds with c = 2 − 15 c=2^{-15}; see also [48]. Further, Payne and Wood [48] raised the bound to c = 1 / 37 c=1/37; notably, Hirzebruch’s inequality is used in their proof; see also [8, Ch. 7]. Pham and Phi refined the argument of Payne and Wood and improved the bound to c = 1 / 26 c=1/26 [49]. Recently, Han [31] established the current best result in Dirac’s conjecture, showing that there is a point incident to ⌈ n / 3 ⌉ + 1 \left\lceil n/3\right\rceil+1 connecting lines; notably, the Bojanowski–Pokora inequality is used in their proof. His result answers a question of Klee and Wagon [34, Ch. 6]; the same question was reposed 20 20 years later by Akiyama et al. [4].

In regard to the proof techniques, it is worth mentioning that neither the Hirzebruch’s inequality nor the Bojanowski–Pokora inequality are known to hold in a pseudoline setting (discussed in Section 2).

### Outline of the paper.

Section 2 gives an overview of pseudoline arrangements and allowable sequences and lists our results. The main results are the lower bounds in Theorems 8 and 9 in relation to Conjecture 2 in Section 2 (i.e., Statement B ′ \mathrm{B^{\prime}} at the beginning of Section 1). The upper bound in Theorem 10 gives a partial answer to a question of Lund, Purdy and Smith [39]. Section 3 contains the proofs of Theorems 8 and 9. Section 4 contains the proof of Theorem 10.

## 2 Pseudolines, allowable sequences, and wiring diagrams

### Pseudoline arrangements.

A family (collection) of two-way infinite x x -monotone curves in the plane is called an *(Euclidean) arrangement of pseudolines*if any two curves have precisely one point in common, at which they properly cross [22, Ch. 6]. An arrangement is *simple*if no three pseudolines have a common point of intersection, see Fig. 1 (left). An arrangement is *nontrivial*if not all pseudolines cross at a single point.

Figure 1: Left: A simple arrangement 𝒜 \mathcal{A}. Center: Wiring diagram of 𝒜 \mathcal{A}. Right: An arrangement 𝒜 ′ \mathcal{A}^{\prime} that is not isomorphic to the arrangement 𝒜 \mathcal{A} on the left.

A family 𝒫 \mathcal{P} of pseudolines is *stretchable*if there exists a family of lines ℒ \mathcal{L} such that the cell decompositions induced by 𝒫 \mathcal{P} and ℒ \mathcal{L} are topologically isomorphic. Two arrangements are *isomorphic*, i.e., considered the same, if they can be mapped onto each other by a homeomorphism of the plane [24]; see Fig. 1 (right). Equivalently, two arrangements are isomorphic if there is an isomorphism between the induced cell decompositions [22, Ch. 6]. Two classic representations of pseudoline arrangements are *allowable sequences*[26, 28] and *wiring diagrams*[23].

### Allowable sequences.

Let P P be a set of n n points in the plane and assume that no two points have the same x x -coordinate. Label the points of P P by 1, 2, …, n 1,2,\ldots,n in increasing order of their x x -coordinate. Take a horizontal line ℓ \ell and start rotating it counterclockwise about a fixed point; In each position, the order of the orthogonal projections of the elements of P P onto ℓ \ell makes a permutation of 1, 2, …, n 1,2,\ldots,n. As the line ℓ \ell rotates counterclockwise about a fixed point, we obtain a periodic sequence of permutations which is called the *circular sequence*of the configuration [27]; see also [14, Ch. 2], [22, Ch. 6], [23], [46, Ch. 1]. The first half-period of this sequence starts with the identity permutation 1, 2, …, n 1,2,\ldots,n and ends with its reversal, n, n − 1, …, 1 n,n-1,\ldots,1; this corresponds to a rotation of ℓ \ell by 180 ∘ 180^{\circ}. During this half-period the following rule is in effect:

1. 1.

Every permutation is obtained from the previous one by reversing one or more nonoverlapping increasing subsequences of adjacent elements.

If the rotation of ℓ \ell continues, we obtain the same sequence of permutations as before, except that now each of them is reversed. After a complete rotation of 360 ∘ 360^{\circ}, we get back 1, 2, …, n 1,2,\ldots,n, the permutation we started with. And so one is usually interested only in the sequence for the first half-period.

Goodman and Pollack [27] generalized this process associated with a point set to an abstract setting. Any sequence of permutations that starts with 1, 2, …, n 1,2,\ldots,n, ends in n, n − 1, …, 1 n,n-1,\ldots,1, and satisfies the above rule is called an *allowable sequence*(or *n n -sequence*). The *half-period*of this sequence is one less than the number of permutations in the sequence i.e., the number of *steps*(or *moves*) in the process 1 1 1 If convenient, the process can be extended beyond the term n, n − 1, …, 1 n,n-1,\ldots,1, so that a periodic sequence of permutations results that cycles back to 1, 2, …, n 1,2,\ldots,n. Terms a half-period apart are the reverses of each other. However, this extension won’t be needed here.. An allowable sequence Σ \Sigma is *simple*if any two consecutive permutations in Σ \Sigma differ by the reversal of an adjacent pair i ​ j ij, where i < j i<j. An allowable sequence is *nontrivial*if it has more than two permutations; equivalently 1, 2, …, n 1,2,\ldots,n is not reversed in one step. Throughout this paper, we only consider nontrivial sequences.

One can extract an allowable sequence of permutations from any given arrangement of pseudolines by sweeping a vertical line from left to right and recording the switches that occur in that order. Even though not every allowable sequence is geometrically realizable as the circular sequence generated by a set of points (or lines), it is however true that every allowable sequence is realizable as the n n -sequence generated by an arrangement of pseudolines [28]. Write each permutation in the sequence as a vertical column of n n numbers and put the columns one after the other. The i i th pseudoline is the piecewise linear x x -monotone curve obtained by connecting all occurrences of number i i, for i = 1, 2, …, n i=1,2,\ldots,n and extended both ways to infinity. By construction, this family of curves is a pseudoline arrangement whose sweep-sequence is the given allowable sequence. By this equivalence, in our arguments we may use language that applies to one setting (allowable sequences) or the other one (pseudolines) as convenient.

Let Σ \Sigma be an allowable n n -sequence. For each i ∈ [n] i\in[n], its *local sequence*Λ i ​ ( Σ) \Lambda_{i}(\Sigma) is the sequence of reversals involving the index i i. Obviously such reversals appear in succession, i.e., no two are simultaneous. The *half-period*(or *length*) of a local sequence is the number of reversals in the sequence.

Figure 2: Wiring diagrams of a simple arrangement (left) and a non-simple one (right).

### Wiring diagrams.

A *wiring diagram*is an Euclidean arrangement of pseudolines consisting of piece-wise linear ‘wires’, each horizontal except for shorter slanted segments where it crosses other wires. Each pair of wires cross exactly once; see Fig. 1 (center). Wiring diagrams are also known as *reflection networks*, i.e., networks that bring n n wires labeled from 1 1 to n n into their reflection by means of performing switches of (two or more) adjacent wires [35, p. 35]. For example, the 5 5 -sequence for the wiring diagram in Fig. 2 (right) is

 | 12345 → 12, 45 21354 → 135 25314 → 25, 14 52341 → 34 52431 → 24 54231 → 23 54321. 12345\xrightarrow{12,45}21354\xrightarrow{135}25314\xrightarrow{25,14}52341\xrightarrow{34}52431\xrightarrow{24}54231\xrightarrow{23}54321. |  |

Its half-period is 6 6. Its five local sequences are the following. Λ 1 = 12,135, 14 \Lambda_{1}=12,135,14; Λ 2 = 12, 25, 24, 23 \Lambda_{2}=12,25,24,23; Λ 3 = 135, 34, 23 \Lambda_{3}=135,34,23; Λ 4 = 45, 14, 34, 24 \Lambda_{4}=45,14,34,24; and Λ 5 = 45,135, 25 \Lambda_{5}=45,135,25. The half-period of Λ 5 \Lambda_{5} is 3 3.

### Applications of allowable sequences.

A classic example is the result of Ungar mentioned in the introduction on the minimum number of directions determined by n n noncollinear points in the plane. If D ⁡ ( n) D(n) denotes this number, Ungar [55] showed that D ⁡ ( n) = 2 ​ ⌊ n / 2 ⌋ D(n)=2\lfloor n/2\rfloor, which is tight for the near-pencil configuration. His proof via allowable sequences concentrates on the subsequence of switches crossing the midline that separates the first n / 2 n/2 elements from the last n / 2 n/2 elements (assuming that n n is even). Another key result is one obtained by Edelsbrunner and Welzl [15] in the study of k k -sets; they showed that the number of k k -sets in a set of n n points is 𝒪 ⁡ ( n ​ k 1 / 2) \mathcal{O}(nk^{1/2}); see also [14, Ch. 2]. More recent applications can be found in [13] and [43]. In the latter article, Nilakantan obtained an alternative proof of Theorem 1 via allowable sequences by arguing the existence of a *simple switch*, namely one that involves only two elements.

### Dirac–Goodman–Pollack conjecture for pseudolines.

For an arrangement ℒ \mathcal{L} of pseudolines let r ⁡ ( ℒ) r(\mathcal{L}) be the maximum number of crossing points (vertices of the line arrangement) on a pseudoline in ℒ \mathcal{L}. The conjecture can be formulated in terms of allowable sequences (as mentioned in Section 1) or in terms of systems of pseudolines. The latter formulation is as follows.

###### Conjecture 2.

[12, 27] Let ℒ \mathcal{L} be a nontrivial arrangement of n n pseudolines. Then r ⁡ ( ℒ) ≥ c ​ n r(\mathcal{L})\geq cn, for some constant c > 0 c>0.

Lund, Purdy and Smith [39] claimed that such a bound holds, but did not provide any proof. From the other direction, they constructed arrangements with r ⁡ ( ℒ) ≤ 4 9 ​ n r(\mathcal{L})\leq\frac{4}{9}n. Regardless, here we obtain the first concrete lower bound (Theorem 8) and an extension for many pseudolines (Theorem 9).

###### Theorem 8.

Let ℒ \mathcal{L} be a nontrivial arrangement of n n pseudolines. Then there is a pseudoline in ℒ \mathcal{L} that is incident to at least c ​ n cn crossing points. In particular, one may take c = 1 / 845 c=1/845 for large n n.

###### Theorem 9.

Let 0 < δ < 1 0<\delta<1 be any constant. Consider an arrangement of pseudolines in which every crossing involves at most δ ​ n \delta n elements. Then there exist Ω ⁡ ( n) \Omega(n) pseudolines whose local sequences have length (i.e., half-period) Ω ⁡ ( n) \Omega(n).

From the other direction, an old construction studied by Rigby [50] shows the following.

###### Theorem 10.

There is an infinite family of arrangements of n n lines (as a system of pseudolines), such that

- •

each vertex is incident to at most 3 3 lines, and

- •

no line is incident to more than 1 2 ​ n + 𝒪 ⁡ ( 1) \frac{1}{2}\,n+\mathcal{O}(1) vertices.

We end this section with a brief review of the status of the three problems and their generalizations (from Section 1). Statement C ′ \mathrm{C^{\prime}} has been settled by Ungar in 1982 [55]. Statement B ′ \mathrm{B^{\prime}} is proved in Theorem 8 with a bound of n / 845 n/845 (for n n sufficiently large). Statement A ′ \mathrm{A^{\prime}} remains open, however, recent results are closing in on this problem. Let f ⁡ ( n) f(n) denote the minimum number of points in general position that determine a convex n n -gon. For the geometric variant A \mathrm{A}, Erdős and Szekeres [20, 21] proved many years ago that 2 n − 2 + 1 ≤ f ⁡ ( n) ≤ 4 n ⁡ ( 1 − o ⁡ ( 1)) 2^{n-2}+1\leq f(n)\leq 4^{n(1-o(1))}; after several constant-factor improvements by other researchers that we skip here, Suk [51] managed to bring the upper bound to same base as the lower bound, i.e., f ⁡ ( n) ≤ 2 n + 𝒪 ⁡ ( n 2 / 3 ​ log ⁡ n) f(n)\leq 2^{n+\mathcal{O}(n^{2/3}\log{n})}. Holmsen, Mojarrad, Pach, and Tardos [32] generalized Suk’s result to pseudoline arrangements and improved the error term. The improvement carries over to the geometric variant and implies f ⁡ ( n) ≤ 2 n + 𝒪 ⁡ ( n ​ log ⁡ n) f(n)\leq 2^{n+\mathcal{O}(\sqrt{n\log{n}})}.

## 3 Proofs of the main results

In this section we prove Theorems 8 and 9. The key component in the proof is a dual extension of the Szemerédi–Trotter theorem for point-line incidences to arrangements of x x -monotone pseudolines. We employ Székely’s method [53]. Let 2 ≤ k ≤ n 2\leq k\leq n. A crossing point is k k -*rich*if it is incident to at least k k pseudolines.

###### Lemma 2.

Let 5 ≤ k ≤ n − 1 5\leq k\leq n-1. For an arrangement of n n pseudolines, the number of k k -rich crossing points is at most

 | c 1 ​ n k + c 2 ​ n 2 k 3, c_{1}\frac{n}{k}+c_{2}\frac{n^{2}}{k^{3}}, |  | (1) |

for a suitable constants c 1, c 2 > 0 c_{1},c_{2}>0. In particular, one may take c 1 = 5 c_{1}=5 and c 2 = 125 / 2 c_{2}=125/2; and if k ≥ 8 k\geq 8 one may take c 1 = 14 c_{1}=14 and c 2 = 18.12 c_{2}=18.12.

###### Proof.

Construct a graph G = ( V, E) G=(V,E) drawn in the plane, where V V is the set of k k -rich crossing points in 𝒜 \mathcal{A} and edges connect vertices along the pseudolines in 𝒜 \mathcal{A}. Let | V | = m |V|=m. Refer to Fig. 3 for an example.

Figure 3: The graph G G; here n = 9 n=9, k = 3 k=3, m = 9 m=9, and | E | = 19 |E|=19.

The graph G G is simple since every pair of pseudolines cross exactly once. Since 𝒜 \mathcal{A} is an arrangement of n n pseudolines, cr ⁡ ( G) ≤ ( n 2) {\rm cr}(G)\leq{n\choose 2}. We have | V | = m |V|=m and | E | ≥ k ​ m − n |E|\geq km-n by easy counting. We distinguish two cases.

*Case 1.*k ​ m ≤ 5 ​ n km\leq 5n. Then m ≤ 5 ​ n / k m\leq 5n/k, as required.

*Case 2.*k ​ m ≥ 5 ​ n km\geq 5n. Then | E | ≥ k ​ m − k ​ m / 5 = 4 ​ k ​ m / 5 ≥ 4 ​ m |E|\geq km-km/5=4km/5\geq 4m by the assumption k ≥ 5 k\geq 5. The former setting of the crossing lemma (Lemma 1) can be applied and it gives

 | ( n 2) ≥ cr ⁡ ( G) ≥ | E | 3 64 ​ | V | 2, or ​ n 2 ≥ 2 64 ⋅ 4 3 5 3 ⋅ k 3 ​ m 3 m 2. {n\choose 2}\geq{\rm cr}(G)\geq\frac{|E|^{3}}{64|V|^{2}},\text{ or }n^{2}\geq\frac{2}{64}\cdot\frac{4^{3}}{5^{3}}\cdot\frac{k^{3}m^{3}}{m^{2}}. |  |

It follows that m ≤ 125 2 ​ n 2 k 3 m\leq\frac{125}{2}\,\frac{n^{2}}{k^{3}}, as required.

Assume now that k ≥ 8 k\geq 8. We distinguish two cases.

*Case 1.*k ​ m ≤ 14 ​ n km\leq 14n. Then m ≤ 14 ​ n / k m\leq 14n/k, as required.

*Case 2.*k ​ m ≥ 14 ​ n km\geq 14n. Then | E | ≥ k ​ m − k ​ m / 14 = 13 ​ k ​ m / 14 ≥ 7 ​ m |E|\geq km-km/14=13km/14\geq 7m by the assumption k ≥ 8 k\geq 8. The latter setting of the crossing lemma can be applied and it gives

 | ( n 2) ≥ cr ⁡ ( G) ≥ 1 29 ​ | E | 3 V | 2, or ​ n 2 ≥ 2 29 ⋅ 13 3 14 3 ⋅ k 3 ​ m 3 m 2. {n\choose 2}\geq{\rm cr}(G)\geq\frac{1}{29}\frac{|E|^{3}}{V|^{2}},\text{ or }n^{2}\geq\frac{2}{29}\cdot\frac{13^{3}}{14^{3}}\cdot\frac{k^{3}m^{3}}{m^{2}}. |  |

It follows that m ≤ 18.12 ​ n 2 k 3 m\leq 18.12\,\frac{n^{2}}{k^{3}}, as required. ∎

Showing that Σ \Sigma has a local sequence Λ i \Lambda_{i} whose half-period is Ω ⁡ ( n) \Omega(n) is equivalent to showing that at least one pseudoline is incident to Ω ⁡ ( n) \Omega(n) crossing points (these may be vertices of G G or edge crossings with the respective pseudoline).

###### Observation 1.

Let ℒ ′ ⊂ ℒ \mathcal{L}^{\prime}\subset\mathcal{L} be the subset of pseudolines participating in a crossing ξ \xi and ℓ ∈ ℒ ∖ ℒ ′ \ell\in\mathcal{L}\setminus\mathcal{L}^{\prime} be any other pseudoline. Then ℓ \ell must cross every pseudoline in ℒ ′ \mathcal{L}^{\prime} at a different crossing point.

###### Proof.

Let ℒ ′′ ⊂ ℒ \mathcal{L}^{\prime\prime}\subset\mathcal{L} be the subset of pseudolines participating in a fixed crossing other than ξ \xi. Then | ℒ ′ ​ ⋂ ℒ ′′ | ≤ 1 |\mathcal{L}^{\prime}\bigcap\mathcal{L}^{\prime\prime}|\leq 1, since every pair of pseudolines cross exactly once. Since ℓ \ell must cross every other pseudoline, in particular, every pseudoline in ℒ ′ \mathcal{L}^{\prime}, ℓ \ell must have at least | ℒ ′ | |\mathcal{L}^{\prime}| different crossing points. ∎

Note that the condition on the uniqueness of any pairwise intersection (as above) is essentially the same as that appearing in Theorem 4; see also [37, Ch. 19].

### Proof of Theorem 8.

First assume that there exists a k k -rich crossing point ξ \xi for k = n / 845 k=n/845. Consider the subset of pseudolines ℒ ′ ⊂ ℒ \mathcal{L}^{\prime}\subset\mathcal{L} involved in this crossing. We have | ℒ ′ | ≥ n / 845 |\mathcal{L}^{\prime}|\geq n/845; recall that | ℒ ′ | ≤ n − 1 |\mathcal{L}^{\prime}|\leq n-1. Pick any pseudoline ℓ ∈ ℒ ∖ ℒ ′ \ell\in\mathcal{L}\setminus\mathcal{L}^{\prime}. By Observation 1, ℓ \ell must intersect every element in ℒ ′ \mathcal{L}^{\prime} at a different crossing point. In other words, the length of ℓ \ell ’s local sequence is at least | ℒ ′ | ≥ n / 845 |\mathcal{L}^{\prime}|\geq n/845, as required.

We may now assume for the remainder of the proof that there are no k k -rich crossing points for k = n / 845 k=n/845. Since every pair of pseudolines intersect exactly once, the total number of pair switches is ( n 2) {n\choose 2}. We next compute an upper bound on the number of pair switches at the k k -rich crossing points for 256 ≤ k < n / 845 256\leq k<n/845. Since k ≥ 8 k\geq 8, we can use the latter setting of Lemma 2, with c 1 = 14 c_{1}=14 and c 2 = 18.12 c_{2}=18.12. Once this bound is obtained, we deduce from it (and the total count) a lower bound on the total number of switches at k k -rich crossing points for 2 ≤ k ≤ 255 2\leq k\leq 255. Finally we obtain a lower bound on the maximum number of crossings on some pseudoline in ℒ \mathcal{L}.

For i ≥ 1 i\geq 1, let V i ⊂ V V_{i}\subset V denote the subset of vertices incident to at least 2 i 2^{i} and at most 2 i + 1 − 1 2^{i+1}-1 pseudolines. Observe that a vertex in V i V_{i} contributes fewer than ( 2 i + 1 2) ≤ 2 ⋅ 4 i {2^{i+1}\choose 2}\leq 2\cdot 4^{i} switches (out of ( n 2) {n\choose 2}).

Let N 1 N_{1} denote the number of switches at k k -rich vertices for 256 ≤ k < n / 845 256\leq k<n/845 contributed by the first term (linear in n n) in Equation ( 1). Let x x be the minimum integer such that 2 x + 1 ≥ n / 845 2^{x+1}\geq n/845. Then 2 x < n / 845 2^{x}<n/845, whence we have

 | N 1 \displaystyle N_{1} | ≤ c 1 ​ n ​ ∑ i = 8 x 1 2 i ​ ( 2 i + 1 2) ≤ 2 ​ c 1 ​ n ​ ∑ i = 8 x 2 i ≤ 4 ​ c 1 ​ n ​ 2 x ≤ 4 ​ c 1 ​ n ​ ( n 845) ≤ 4.242 64 ​ n 2. \displaystyle\leq c_{1}n\sum_{i=8}^{x}\frac{1}{2^{i}}{2^{i+1}\choose 2}\leq 2c_{1}n\sum_{i=8}^{x}2^{i}\leq 4c_{1}n\,2^{x}\leq 4c_{1}n\left(\frac{n}{845}\right)\leq\frac{4.242}{64}n^{2}. |  |

Let N 2 N_{2} denote the number of switches at k k -rich vertices for 256 ≤ k < n / 845 256\leq k<n/845 contributed by the second term (quadratic in n n) in Equation ( 1). We have

 | N 2 ≤ ∑ i = 8 ∞ c 2 ​ n 2 2 3 ​ i ​ ( 2 i + 1 2) ≤ 2 ​ c 2 ​ n 2 ​ ( ∑ i = 8 ∞ 1 2 i) = 2 ​ c 2 ​ 1 128 ​ n 2 = 18.12 64 ​ n 2. \displaystyle N_{2}\leq\sum_{i=8}^{\infty}c_{2}\frac{n^{2}}{2^{3i}}{2^{i+1}\choose 2}\leq 2c_{2}n^{2}\left(\sum_{i=8}^{\infty}\frac{1}{2^{i}}\right)=2c_{2}\frac{1}{128}n^{2}=\frac{18.12}{64}n^{2}. |  |

Adding up the two contributions yields

 | N 1 + N 2 ≤ 22.362 64 ​ n 2. N_{1}+N_{2}\leq\frac{22.362}{64}n^{2}. |  |

Hence at least

 | ( n 2) − 22.362 64 ​ n 2 ≥ 9.637 64 ​ n 2 {n\choose 2}-\frac{22.362}{64}n^{2}\geq\frac{9.637}{64}n^{2} |  | (2) |

switches occur at crossing points that involve at most 255 255 pseudolines. In the last inequality we used the fact that n n is large enough. A crossing of j j pseudolines, where 2 ≤ j ≤ 255 2\leq j\leq 255, distributes j j credits to the respective lines and uses ( j 2) {j\choose 2} switches from the pool in ( 2). One credit received by a pseudoline counts for one crossing point on the respective pseudoline. The ratio of credits to switches in such a crossing,

 | j ( j 2) = 2 j − 1, \frac{j}{{j\choose 2}}=\frac{2}{j-1}, |  |

is minimized at j = 255 j=255, when the ratio is 1 / 127 1/127. Consequently, by the pigeonhole principle, there is a pseudoline that receives at least

 | 9.637 64 ​ n 2 ⋅ 1 127 ⋅ 1 n ≥ n 845 \frac{9.637}{64}n^{2}\cdot\frac{1}{127}\cdot\frac{1}{n}\geq\frac{n}{845} |  |

credits, i.e., has at least this number of crossing points, as required. ∎

The resemblance of the argument in the proof of Theorem 8 with the following result of Beck [5] is worth noting.

###### Theorem 11.

(Beck [5]). There is constant c > 0 c>0 such that for any set S S of n n points in the plane, either

1. ( α \alpha)

some line contains at least c ​ n cn points of S S, or

2. ( β \beta)

the number of distinct lines determined by S S is at least c ​ n 2 cn^{2}.

In general one cannot guarantee the existence of more pseudolines with the property in Theorem 8. Indeed, consider the n n -sequence of permutations:

 | 1, 2, …, n − 1, n → 1, 2, …, n − 1 n − 1, n − 2, …, 2, 1, n → 1, n n − 1, n − 2, …, 2, n, 1 → ⋯ → n, n − 1, …, 2, 1. 1,2,\ldots,n-1,n\xrightarrow{1,2,\ldots,n-1}n-1,n-2,\ldots,2,1,n\xrightarrow{1,n}n-1,n-2,\ldots,2,n,1\xrightarrow{}\cdots\xrightarrow{}n,n-1,\ldots,2,1. |  |

The only pseudoline whose local sequence is of length Ω ⁡ ( n) \Omega(n) is the n n th one. However, under very mild conditions, the stronger statement in Theorem 9 is in effect. Its proof is analogous to that of Theorem 8.

### Proof of Theorem 9 (sketch).

Assume first that there exists a k k -rich crossing point ξ \xi for k = c ​ n k=cn, for some positive constant c ≤ δ c\leq\delta. Consider the subset of pseudolines ℒ ′ ⊂ ℒ \mathcal{L}^{\prime}\subset\mathcal{L} involved in this crossing. We have c ​ n ≤ | ℒ ′ | ≤ δ ​ n cn\leq|\mathcal{L}^{\prime}|\leq\delta n. By Observation 1, for every pseudoline ℓ ∈ ℒ ∖ ℒ ′ \ell\in\mathcal{L}\setminus\mathcal{L}^{\prime}, the length of ℓ \ell ’s local sequence is at least c ​ n cn. Moreover, | ℒ ∖ ℒ ′ | ≥ ( 1 − δ) ​ n |\mathcal{L}\setminus\mathcal{L}^{\prime}|\geq(1-\delta)n, as required.

If there is no k k -rich crossing point for k = c ​ n k=cn, for a sufficiently small c > 0 c>0, the proof is finished as before, by obtaining an Ω ⁡ ( n 2) \Omega(n^{2}) lower bound analogous to ( 2). We omit the details. ∎

It should be noted that Theorem 9 is a dual extension of Beck’s result mentioned above.

## 4 Upper bound questions and concluding remarks

In this section we prove Theorem 10. In 2014 2014, Lund, Purdy, and Smith [39] demonstrated an infinite family of (nontrivial) pseudoline arrangements, in which an arrangement of n n pseudolines has no member incident to more than 4 ​ n / 9 4n/9 points of intersection (i.e., vertices of the arrangement), and thereby showed that the strong Dirac conjecture does not hold for pseudolines. One feature of the respective family of arrangements is that they contain vertices with high incidence, in particular, about n / 3 n/3 pseudolines are incident to a single vertex. The authors asked the following.

###### Question 1.

(Lund, Purdy, and Smith [39]) Is there an infinite family of arrangements of n n pseudolines, such that

- •

no vertex is incident to Ω ⁡ ( n) \Omega(n) pseudolines, and

- •

no pseudoline is incident to more than ( 1 − ε) ​ n 2 (1-\varepsilon)\,\frac{n}{2} vertices, for some constant ε > 0 \varepsilon>0?

The authors further relaxed the second requirement by replacing ( 1 − ε) ​ n 2 (1-\varepsilon)\,\frac{n}{2} with c ​ n cn, where c < 1 c<1 is a constant, and asked for such an arrangement. Here we give a positive answer to the latter question, while we show that the first requirement can be substantially strengthened in that case. Interestingly enough, the best construction we found uses straight lines as we were not able to exploit the power of curved pseudolines. The features of the construction are described in Theorem 10. It is worth noting, however, that this construction falls short of answering Question 1.

### The deltoid construction.

The construction can be traced back to Rigby [50] who provided an analysis, and even further back; for instance, an illustration can be found in [38, Ch. 8]. This line arrangement has been also used in [6, 25], where descriptions and useful properties can be found. Let ℓ ⁡ ( θ) \ell(\theta) denote the line connecting e i ​ θ e^{i\theta} and e i ⁡ ( π − 2 ​ θ) e^{i(\pi-2\theta)} on the unit circle, with the understanding that ℓ ⁡ ( θ) \ell(\theta) is the tangent line when the two points coincide. We take the freedom to denote the construction in this way based on the fact that ℓ ⁡ ( θ) \ell(\theta) envelops a *deltoid*as θ \theta varies. Its key property stems from the following.

###### Lemma 3.

(Rigby [50], Füredi and Palásti [25]). The lines ℓ ⁡ ( α) \ell(\alpha), ℓ ⁡ ( β) \ell(\beta), and ℓ ⁡ ( γ) \ell(\gamma) are concurrent if and only if α + β + γ ≡ 0 ( mod 2 ​ π) \alpha+\beta+\gamma\equiv 0\pmod{2\pi}.

Figure 4: The deltoid construction for n = 18 n=18 lines.

Consider a regular n n -gon inscribed in the unit circle centered at the origin, where n n is even, and refer to Fig. 4. Let p 0, p 1, …, p n − 1 p_{0},p_{1},\ldots,p_{n-1} denote its vertices labeled counterclockwise starting from p 0 = ( 1, 0) p_{0}=(1,0). For i = 0, 1, …, n − 1 i=0,1,\ldots,n-1, draw the lines connecting p i p_{i} with p n / 2 − 2 ​ i p_{n/2-2i}, where indices are considered modulo n n. If the points p i p_{i} and p n / 2 − 2 ​ i p_{n/2-2i} coincide, draw the tangent line to the circle at p i p_{i}. The resulting arrangement has n n lines, 1 + ⌈ n ⁡ ( n − 3) 6 ⌉ 1+\left\lceil\frac{n(n-3)}{6}\right\rceil triple points (i.e., vertices incident to 3 3 lines), and n − 3 + δ ⁡ ( n) n-3+\delta(n) double points (i.e., ordinary vertices), where δ ⁡ ( n) = 0 \delta(n)=0 if n ≡ 0 ( mod 3) n\equiv 0\pmod{3} and δ ⁡ ( n) = 2 \delta(n)=2 otherwise; see, e.g., [6]. Moreover, double points may only appear on the outer envelope, whence each line is incident to at most 3 3 double points, and Theorem 10 follows. Obviously, the constant 1 / 2 1/2 in the theorem is the best possible (for lines or pseudolines) under the first constraint.

Determining the right constant in Conjecture 2 remains an interesting open problem. It is easy to obtain small improvements in the lower bound by slightly adjusting the parameters in the proof of Theorem 8. Since we suspect that the answer is much closer to the best known upper bound of Lund, Purdy and Smith, we did not insist in that direction.

## References

- [1] Eyal Ackerman, On topological graphs with at most four crossings per edge, *Computational Geometry: Theory and Applications*85 (2019), article 101574.
- [2] Martin Aigner and Günter M. Ziegler, *Proofs from the Book*, 6th edition, Springer, Berlin, 2018.
- [3] Miklós Ajtai, Vašek Chvátal, Monroe M. Newborn, and Endre Szemerédi, Crossing-free subgraphs, *Annals of Discrete Mathematics*12 (1982), 9–12.
- [4] Jin Akiyama, Hiro Ito, Midori Kobayashi, and Gisaku Nakamura, Arrangements of n n points whose incident-line-numbers are at most n / 2 n/2, *Graphs and Combinatorics*27(3) (2011), 321–326.
- [5] József Beck, On the lattice property of the plane and some problems of Dirac, Motzkin and Erdős in combinatorial geometry, *Combinatorica*3 (1983), 281–297.
- [6] Jürgen Bokowski and Piotr Pokora, On the Sylvester–Gallai and the orchard problem for pseudoline arrangements, *Periodica Mathematica Hungarica*77(2) (2018), 164–174.
- [7] Peter Borwein and William O. J. Moser, A survey of Sylvester’s problem and its generalizations, *Aequationes Mathematicae*40(1) (1990), 111–135.
- [8] Peter Braß, William Moser, and János Pach, *Research Problems in Discrete Geometry*, Springer, New York, 2005.
- [9] Don Chakerian, Sylvester’s problem on collinear points and a relative, *The American Mathematical Monthly*77(2) (1970), 164–167.
- [10] Vašek Chvátal, *The Discrete Mathematical Charms of Paul Erdős*, Cambridge University Press, New York, 2021.
- [11] Hallard T. Croft, Kenneth J. Falconer, and Richard K. Guy, *Unsolved Problems in Geometry*, Springer, New York, 1991.
- [12] Gabriel A. Dirac, Collinearity properties of sets of points, *The Quarterly Journal of Mathematics*2(1) (1951), 221–227.
- [13] Adrian Dumitrescu and Csaba D. Tóth, Distinct triangle areas in a planar point set, *Proc. 12th Conference on Integer Programming and Combinatorial Optimization*(IPCO 2007), vol. 4513 of LNCS, Springer, pp. 119–129.
- [14] Herbert Edelsbrunner, *Algorithms in Combinatorial Geometry*, Springer, Berlin, 1987.
- [15] Herbert Edelsbrunner and Emo Welzl, On the number of line separations of a finite set in the plane, *Journal of Combinatorial Theory, Series A*38(1) (1985), 15–29.
- [16] Paul Erdős, Three point collinearity, *American Mathematical Monthly*50 (1943), 65.
- [17] Paul Erdős, Some unsolved problems, *Publ. Math. Inst. Hungar. Acad. Sci.*6 (1961), 221–254.
- [18] Nicolaas G. de Bruijn and Paul Erdős, On a combinatorial problem, *Proc. Kon. Ned. Akad. v. Wetensch.*51 (1948), 1277–1279.
- [19] Paul Erdős and George Purdy, Extremal problems in combinatorial geometry, in *Handbook of Combinatorics*(vol. 1), (Ronald Graham, László Lovász, and Martin Grötschel, editors), Elsevier, 1995, pp. 809–874.
- [20] Paul Erdős and György Szekeres, A combinatorial problem in geometry, *Compositio Mathematica*2 (1935), 463–470.
- [21] Paul Erdős and György Szekeres, On some extremum problems in elementary geometry, *Annales Universitatis Scientiarium Budapestinensis de Rolando Eötvös Nominatae Sectio Mathematica*3-4 (1960), 53–62.
- [22] Stefan Felsner, *Geometric Graphs and Arrangements*, Advanced Lectures in Mathematics, Vieweg Verlag, 2004.
- [23] Stefan Felsner and Jacob E. Goodman, Pseudoline arrangements, in *Handbook of Discrete and Computational Geometry*(3rd edition), (J. E. Goodman, J. O’Rourke, C. D. Tóth, editors), CRC Press, Boca Raton, 2017, pp. 125–157.
- [24] Stefan Felsner and Pavel Valtr, Coding and counting arrangements of pseudolines, *Discrete & Computational Geometry*46(4) (2011), 405–416.
- [25] Zoltán Füredi and Ilona Palásti, Arrangements of lines with a large number of triangles, *Proceedings of the American Mathematical Society*92(4) (1984), 561–566.
- [26] Jacob E. Goodman and Richard Pollack, On the combinatorial classification of nondegenerate configurations in the plane, *Journal of Combinatorial Theory Ser. A*29 (1980), 220–235.
- [27] Jacob E. Goodman and Richard Pollack, A combinatorial perspective on some problems in geometry, *Congressus Numerantium*32 (1981), 383–394.
- [28] Jacob E. Goodman and Richard Pollack, Allowable sequences and order types in discrete and computational geometry. in *New Trends in Discrete and Computational Geometry*(János Pach, editor), Algorithms and Combinatorics, Volume 10, Springer, New York, 1993, pp. 103–134.
- [29] Ben Green and Terence Tao, On sets defining few ordinary lines, *Discrete & Computational Geometry*50(2) (2013), 409–468.
- [30] Branko Grünbaum, *Arrangements and Spreads*, Amer. Math. Soc., Providence, 1972.
- [31] Zeye Han, A Note on the weak Dirac conjecture, *Electron. J. Comb.*24(1) (2017), #P1.63.
- [32] Andreas Holmsen, Hossein N. Mojarrad, János Pach, and Gábor Tardos, Two extensions of the Erdős–Szekeres problem, *Journal of the European Mathematical Society*22(12) (2020), 3981–3995.
- [33] Leroy M. Kelly and William O. J. Moser, On the number of ordinary lines determined by n n points, *Canadian Journal of Mathematics*10 (1958), 210–219.
- [34] Victor Klee and Stan Wagon, *Old and New Unsolved Problems in Plane Geometry and Number Theory*, Mathematical Association of America, Washington, DC, 1991.
- [35] Donald E. Knuth, *Axioms and Hulls*, Lecture Notes in Computer Science, Vol. 606, Springer, Berlin, 1992.
- [36] Thomas Leighton, New lower bound techniques for VLSI, *Math. Systems Theory*17 (1984), 47–70.
- [37] Jacobus H. van Lint and Richard M. Wilson, *A Course in Combinatorics*, Cambridge University Press, 2nd edition, New York, 2001.
- [38] Edward H. Lockwood, *A Book of Curves*, Cambridge University Press, 1961.
- [39] Ben Lund, George B. Purdy, and Justin W. Smith, A Pseudoline counterexample to the strong Dirac conjecture, *Electron. J. Comb.*21(2) (2014), #P2.31.
- [40] Theodore S. Motzkin, The lines and planes connecting the points of a finite set, *Transactions of the American Mathematical Society*70(3) (1951), 451–464.
- [41] Theodore S. Motzkin, Nonmixed connecting lines. Abstract 67T 605, *Notices Amer. Math. Soc*14 (1967), 837.
- [42] Theodore S. Motzkin, Sets for which no point lies on many connecting lines, *Journal of Combinatorial Theory, Series A*18(3) (1975), 345–348.
- [43] Niranjan Nilakantan, Extremal problems related to the Sylvester–Gallai theorem, in *Combinatorial and Computational Geometry*(Jacob E. Goodman, János Pach, Emo Welzl, editors), MSRI Publications, Volume 52, 2005, pp. 479–494.
- [44] János Pach, Directions in combinatorial geometry, *Jahresbericht der Deutschen Mathematiker-Vereinigung*107 (2005), 215–225.
- [45] János Pach, Radoš Radoičić, Gábor Tardos, and Géza Tóth, Improving the crossing lemma by finding more crossings in sparse graphs, *Discrete & Computational Geometry*36(4) (2006), 527–552.
- [46] János Pach and Micha Sharir, *Combinatorial Geometry and Its Algorithmic Applications—The Alcalá Lectures*, Mathematical Surveys and Monographs, Vol. 152, American Mathematical Society, Providence, RI, 2009.
- [47] Michael S. Payne, *Combinatorial Geometry of Point Sets with Collinearities*, PhD thesis, The University of Melbourne, Dept. of Mathematics and Statistics, 2014.
- [48] Michael S. Payne and David R. Wood, Progress on Dirac’s conjecture, *Electron. J. Comb.*21(2) (2014), #P2.12.
- [49] Hoang Ha Pham and Tien Cuong Phi, A new progress on weak Dirac conjecture, preprint, 2016, [arXiv:1607.08398][3].
- [50] John F. Rigby, Multiple intersections of diagonals of regular polygons, and related topics, *Geometriae Dedicata*9(2) (1980), 207–238.
- [51] Andrew Suk, On the Erdős–Szekeres convex polygon problem, *Journal of the American Mathematical Society*30 (2017), 1047–1053.
- [52] James Joseph Sylvester, Mathematical question 11851, *Educational Times*46 (1893), 156.
- [53] László Székely, Crossing numbers and hard Erdős problems in discrete geometry, *Combinatorics, Probability and Computing*6 (1997), 353–358.
- [54] Endre Szemerédi and William T. Trotter, Extremal problems in discrete geometry, *Combinatorica*3 (1983), 381–392.
- [55] Peter Ungar, 2 ​ N 2N noncollinear points determine at least 2 ​ N 2N directions, *Journal of Combinatorial Theory Ser. A*33 (1982), 343–347.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: arXiv:1607.08398
