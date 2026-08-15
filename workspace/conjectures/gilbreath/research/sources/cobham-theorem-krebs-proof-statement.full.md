<!-- source: https://arxiv.org/html/1801.06704v1 | converted from HTML -->

A more reasonable proof of Cobham’s theorem

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1801.06704v1 [cs.FL] 20 Jan 2018

# A more reasonable proof of Cobham’s theorem

Thijmen J. P. Krebs Address: Delft Institute of Applied Mathematics
Delft University of Technology
PO Box 5031
2600 GA Delft
Netherlands Email address: [t.j.p.krebs@protonmail.com][3]

###### Abstract.

We present a short new proof of Cobham’s theorem without using Kronecker’s approximation theorem, making it suitable for generalization beyond automatic sequences.

###### Key words and phrases:

Cobham’s theorem, automatic sequences

###### 2010 Mathematics Subject Classification

11B85 (Primary), 68Q45 (Secondary)

## 1. Introduction

In this note we give a short proof of the following celebrated theorem on automatic sequences.

###### Theorem 1 (Cobham).

Let a, b ∈ ℕ ≥ 2 a,b\in\mathbb{N}_{\geq 2} be multiplicatively independent (i.e. a m ≠ b n a^{m}\neq b^{n} for all m, n ∈ ℕ > 0 m,n\in\mathbb{N}_{>0}). A sequence ( f x) x ∈ ℕ (f_{x})_{x\in\mathbb{N}} is a a - and b b -automatic if and only if it is ultimately periodic.

The theorem is originally proven in [2]. To quote [4, p. 118]: “The proof is correct, long and hard. It is a challenge to find a more reasonable proof of this fine theorem.”. In response, [5] suggested an easier approach that starts by showing the sequence is syndetic (i.e. the gap between any successive occurrences of any value is bounded) before proving it is ultimately periodic with a combinatorial argument. See for instance the proof in [1] (together with [8]).

Syndeticity is typically established using Kronecker’s approximation theorem (see [3]), but that proved to be problematic for automatic functions on the Gaussian integers as shown in [6]. Our proof differs entirely from the classical approach and only needs a consequence of the much weaker approximation theorem of Dirichlet.

## 2. Preliminaries

We assume basic familiarity with formal language terminology, and briefly recall a few standard notions from automatic sequence theory. We refer to [1] for a comprehensive treatment.

###### Definition 2.

A *deterministic finite automaton with output*(*DFAO*) is a tuple ( S, D, δ, s 0, F) (S,D,\delta,s_{0},F), where S S is a finite set of *states*, D D a finite *input alphabet*, δ: S × D → S \delta\colon S\times D\to S a *transition function*, s 0 ∈ S s_{0}\in S an *initial state*, and F F an *output function*on S S. On input w ∈ D ∗ w\in D^{*} it outputs F ⁡ ( δ ⁡ ( s 0, w)) F(\delta(s_{0},w)), where we extend δ ⁡ ( s 0, w) = δ ⁡ ( δ ⁡ ( s 0, u), v) \delta(s_{0},w)=\delta(\delta(s_{0},u),v) for any u, v ∈ D ∗ u,v\in D^{*} with w = u ​ v w=uv as usual.

###### Definition 3.

In base b ∈ ℕ ≥ 2 b\in\mathbb{N}_{\geq 2}, a word w ∈ ℕ ∗ w\in\mathbb{N}^{*} of length n n represents the natural number [w] b = w 0 ​ b n − 1 + … + w n − 2 ​ b + w n − 1 [w]_{b}=w_{0}b^{n-1}+\ldots+w_{n-2}b+w_{n-1}, and a language L ⊆ ℕ ∗ L\subseteq\mathbb{N}^{*} represents [L] b = { [w] b ∣ w ∈ L } [L]_{b}=\{[w]_{b}\mid w\in L\}.

###### Definition 4.

Let b ∈ ℕ ≥ 2 b\in\mathbb{N}_{\geq 2} and { 0, 1, …, b − 1 } ⊆ D ⊆ ℕ \{0,1,\ldots,b-1\}\subseteq D\subseteq\mathbb{N} be finite. A sequence ( f x) x ∈ ℕ (f_{x})_{x\in\mathbb{N}} is ( b, D) (b,D) -*automatic*if there is a DFAO ( S, D, δ, s 0, F) (S,D,\delta,s_{0},F) such that f [w] b = F ⁡ ( δ ⁡ ( s 0, w)) f_{[w]_{b}}=F(\delta(s_{0},w)) for all w ∈ D ∗ w\in D^{*}. A sequence ( f x) x ∈ ℕ (f_{x})_{x\in\mathbb{N}} is b b -*automatic*if it is ( b, { 0, 1, …, b − 1 }) (b,\{0,1,\ldots,b-1\}) -automatic.

###### Lemma 5.

Let b ∈ ℕ ≥ 2 b\in\mathbb{N}_{\geq 2} and { 0, 1, …, b − 1 } ⊆ D ⊆ ℕ \{0,1,\ldots,b-1\}\subseteq D\subseteq\mathbb{N} be finite. A sequence ( f x) x ∈ ℕ (f_{x})_{x\in\mathbb{N}} is b b -automatic if and only if it is ( b, D) (b,D) -automatic.

###### Proof.

Adapt [1, Thm. 6.8.6] to use the transducer of [7, Prop. 7.1.4] for normalization on D ∗ D^{*}. ∎

Any two bases have relatively close powers, which follows easily from Dirichlet’s approximation theorem or by mimicking its proof to avoid logarithms as follows.

###### Lemma 6.

Let a, b ∈ ℕ ≥ 2 a,b\in\mathbb{N}_{\geq 2} and ϵ ∈ ℝ > 0 \epsilon\in\mathbb{R}_{>0}. Then there are m, n ∈ ℕ > 0 m,n\in\mathbb{N}_{>0} such that | a m − b n | ≤ ϵ ​ b n \lvert a^{m}-b^{n}\rvert\leq\epsilon b^{n}.

###### Proof.

We may assume that a ≥ b a\geq b by taking a suitable power of a a, so the sequence ( f x) x ∈ ℕ (f_{x})_{x\in\mathbb{N}} given by a x ​ b − f x ∈ [1, b) a^{x}b^{-f_{x}}\in[1,b) for all x ∈ ℕ x\in\mathbb{N} is strictly increasing. By the pigeonhole principle there are natural numbers x < y x<y such that | a y ​ b − f y − a x ​ b − f x | ≤ ϵ \lvert a^{y}b^{-f_{y}}-a^{x}b^{-f_{x}}\rvert\leq\epsilon, that is, | a y − x − b f y − f x | ≤ ϵ ​ b f y ​ a − x ≤ ϵ ​ b f y − f x \lvert a^{y-x}-b^{f_{y}-f_{x}}\rvert\leq\epsilon b^{f_{y}}a^{-x}\leq\epsilon b^{f_{y}-f_{x}}. ∎

A sequence ( f x) x ∈ ℕ (f_{x})_{x\in\mathbb{N}} has *local period*p ∈ ℕ > 0 p\in\mathbb{N}_{>0} on an interval I ⊆ ℕ I\subseteq\mathbb{N} if f x = f x + p f_{x}=f_{x+p} for all x, x + p ∈ I x,x+p\in I. Local periodicity on sufficiently overlapping intervals extends to their union.

###### Lemma 7.

Let ( f x) x ∈ ℕ (f_{x})_{x\in\mathbb{N}} have local period p p on an interval I I and local period q q on an interval J J. If | I ∩ J | ≥ p + q \lvert I\cap J\rvert\geq p+q, then f f has local period p p on the interval I ∪ J I\cup J.

###### Proof.

Pick any x, x + p ∈ I ∪ J x,x+p\in I\cup J. If x, x + p ∈ I x,x+p\in I, we have f x = f x + p f_{x}=f_{x+p} by assumption. Otherwise, since the interval I ∩ J I\cap J has cardinality at least p + q p+q, we have x, x + p ∈ J x,x+p\in J and we can pick y, y + p ∈ I ∩ J y,y+p\in I\cap J such that y ≡ x ( mod q) y\equiv x\pmod{q}. Then f x = f y = f y + p = f x + p f_{x}=f_{y}=f_{y+p}=f_{x+p} by local periodicity on J J, I I and J J respectively. ∎

## 3. Proof

Let B ⁡ [x; r] = { y ∈ ℕ ∣ | y − x | ≤ r } B[x;r]=\{y\in\mathbb{N}\mid\lvert y-x\rvert\leq r\} be the interval centered on x ∈ ℝ ≥ 0 x\in\mathbb{R}_{\geq 0} with radius r ∈ [0, x] r\in[0,x].

###### Proof of theorem 1.

As usual, we only prove the forward direction.

For each c ∈ { a, b } c\in\{a,b\}, f f is computed by a DFAO ( S c, D c, δ c, s 0, c, F c) (S_{c},D_{c},\delta_{c},s_{0,c},F_{c}) in base c c with digits D c = B ⁡ [c; c] D_{c}=B[c;c] by lemma 5. It is easy to check that B ⁡ [c n; c n] ⊆ [D c n] c B[c^{n};c^{n}]\subseteq[D_{c}^{n}]_{c} for all n ∈ ℕ > 0 n\in\mathbb{N}_{>0}. Define L c ​ s = { w ∈ D c ∗ ∣ δ c ​ ( s 0, c, w) = s } L_{cs}=\{w\in D_{c}^{*}\mid\delta_{c}(s_{0,c},w)=s\} for s ∈ S c s\in S_{c}. Then for all w ∈ L c ​ s w\in L_{cs} and v ∈ D c ∗ v\in D_{c}^{*} we have f [w ​ v] c = F c ​ ( δ c ​ ( s 0, c, w ​ v)) = F c ​ ( δ c ​ ( s, v)) f_{[wv]_{c}}=F_{c}(\delta_{c}(s_{0,c},wv))=F_{c}(\delta_{c}(s,v)), so for all x, y ∈ [L c ​ s] c x,y\in[L_{cs}]_{c}, n ∈ ℕ n\in\mathbb{N} and z ∈ [D c n] c z\in[D_{c}^{n}]_{c}

(1) |  | f x ​ c n + z = f y ​ c n + z. f_{xc^{n}+z}=f_{yc^{n}+z}. |  |

We create local periods of f f as follows. Let S ∞ S_{\infty} be the set of s ∈ S b s\in S_{b} for which [L b ​ s] b [L_{bs}]_{b} is infinite. Since { [L a ​ t] a ∣ t ∈ S a } \{[L_{at}]_{a}\mid t\in S_{a}\} is a finite cover of ℕ \mathbb{N}, we can fix for each s ∈ S ∞ s\in S_{\infty} some t ∈ S a t\in S_{a} and distinct x s ​ t, y s ​ t ∈ [L b ​ s] b ∩ [L a ​ t] a x_{st},y_{st}\in[L_{bs}]_{b}\cap[L_{at}]_{a}. Letting ξ = max { x s ​ t, y s ​ t ∣ s ∈ S ∞ } + 1 \xi=\max\{x_{st},y_{st}\mid s\in S_{\infty}\}+1, we can find m, n ∈ ℕ > 0 m,n\in\mathbb{N}_{>0} such that ξ ​ | a m − b n | ≤ 1 6 ​ b n \xi\lvert a^{m}-b^{n}\rvert\leq\frac{1}{6}b^{n} by lemma 6. In particular, we get 5 6 ​ b n ≤ a m \frac{5}{6}b^{n}\leq a^{m}. Since a m ≠ b n a^{m}\neq b^{n} we can take p s ​ t = ( x s ​ t − y s ​ t) ​ ( a m − b n) ∈ ( 0, 1 6 ​ b n] p_{st}=(x_{st}-y_{st})(a^{m}-b^{n})\in(0,\frac{1}{6}b^{n}] for all s ∈ S ∞ s\in S_{\infty} by swapping x s ​ t x_{st} and y s ​ t y_{st} if necessary.

We show for each s ∈ S ∞ s\in S_{\infty} and x ∈ [L b ​ s] b x\in[L_{bs}]_{b} that f f has local period p s ​ t p_{st} on the interval I x = B ⁡ [x ​ b n + b n; 2 3 ​ b n] I_{x}=B[xb^{n}+b^{n};\frac{2}{3}b^{n}]. Pick any z, z + p s ​ t ∈ B ⁡ [b n; 2 3 ​ b n] ⊆ [D b n] b z,z+p_{st}\in B[b^{n};\frac{2}{3}b^{n}]\subseteq[D_{b}^{n}]_{b}. Since

 | | z − y s ​ t ​ ( a m − b n) − a m | ≤ | z − b n | + ( y s ​ t + 1) ​ | a m − b n | ≤ 5 6 ​ b n ≤ a m, \lvert z-y_{st}(a^{m}-b^{n})-a^{m}\rvert\leq\lvert z-b^{n}\rvert+(y_{st}+1)\lvert a^{m}-b^{n}\rvert\leq\tfrac{5}{6}b^{n}\leq a^{m}, |  |

we have z − y s ​ t ​ ( a m − b n) ∈ B ⁡ [a m; a m] ⊆ [D a m] a z-y_{st}(a^{m}-b^{n})\in B[a^{m};a^{m}]\subseteq[D_{a}^{m}]_{a}. Hence, using ( 1) thrice we see as desired

 | f x ​ b n + z \displaystyle f_{xb^{n}+z} | = f y s ​ t ​ b n + z \displaystyle=f_{y_{st}b^{n}+z} |  |

 |  | = f y s ​ t ​ a m + z − y s ​ t ​ ( a m − b n) \displaystyle=f_{y_{st}a^{m}+z-y_{st}(a^{m}-b^{n})} |  |

 |  | = f x s ​ t ​ a m + z − y s ​ t ​ ( a m − b n) \displaystyle=f_{x_{st}a^{m}+z-y_{st}(a^{m}-b^{n})} |  |

 |  | = f x s ​ t ​ b n + z + p s ​ t \displaystyle=f_{x_{st}b^{n}+z+p_{st}} |  |

 |  | = f x ​ b n + z + p s ​ t. \displaystyle=f_{xb^{n}+z+p_{st}}. |  |

Let x ∈ ℕ x\in\mathbb{N} be such that { [L b ​ s] b ∣ s ∈ S ∞ } \{[L_{bs}]_{b}\mid s\in S_{\infty}\} covers x + ℕ x+\mathbb{N}, and fix for f f a local period p y ≤ 1 6 ​ b n p_{y}\leq\frac{1}{6}b^{n} on I y I_{y} for all y ≥ x y\geq x. We show that f f has local period p x p_{x} on ⋃ x ≤ y ≤ z I y \bigcup_{x\leq y\leq z}I_{y} for all z ≥ x z\geq x by induction. It surely holds if z = x z=x. Otherwise, f f has local period p x p_{x} on ⋃ x ≤ y < z I y \bigcup_{x\leq y<z}I_{y} by induction and local period p z p_{z} on I z I_{z}, so lemma 7 proves our induction hypothesis as ( ⋃ x ≤ y < z I y) ∩ I z = B ⁡ [( z + 1 2) ​ b n; 1 6 ​ b n] \big(\bigcup_{x\leq y<z}I_{y}\big)\cap I_{z}=B[(z+\frac{1}{2})b^{n};\frac{1}{6}b^{n}] has cardinality at least ⌊ 1 3 ​ b n ⌋ ≥ 2 ​ ⌊ 1 6 ​ b n ⌋ ≥ p x + p z \lfloor\frac{1}{3}b^{n}\rfloor\geq 2\lfloor\frac{1}{6}b^{n}\rfloor\geq p_{x}+p_{z}.

We conclude that f f has local period p x p_{x} on ⋃ x ≤ y I y \bigcup_{x\leq y}I_{y}, that is, f f is ultimately periodic. ∎

## 4. Future work

We will show that our approach extends well to prove the Cobham-Semenov theorem from [9], and to prove the Cobham-type theorem for automatic functions on vectors of imaginary quadratic integers. In particular, we will establish the conjecture for the Gaussian integers from [6].

## References

- [1] J. P. Allouche and J. O. Shallit. Automatic sequences: theory, applications, generalizations. Cambridge University Press, 2003.
- [2] A. Cobham. On the base-dependence of sets of numbers recognizable by finite automata. Math. Systems Theory, 3:186–192, 1969.
- [3] F. Durand and M. Rigo. On Cobham’s theorem. In Automata: from Mathematics to Applications. European Mathematical Society, to appear.
- [4] S. Eilenberg. Automata, Languages, and Machines, volume A. Academic Press, 1974.
- [5] G. Hansel. A propos d’un théorème de Cobham. In D. Perrin, editor, Actes de la Fête des Mots, pages 55–59, Greco de Programmation, CNRS, Rouen, 1982.
- [6] G. Hansel and T. Safer. Vers un théorème de Cobham pour les entiers de Gauss. Bull. Belg. Math. Soc. Simon Stevin, 10(5):723–735, 2003.
- [7] M. Lothaire. Algebraic Combinatorics on Words. Cambridge University Press, 2002.
- [8] M. Rigo and L. Waxweiler. A note on syndeticity, recognizable sets and Cobham’s theorem. 88:169–173, February 2006.
- [9] A. L. Semenov. Presburgerness of predicates regular in two number systems. Siberian J. Math., 18:289–300, 1977.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:t.j.p.krebs@protonmail.com
