<!-- source: https://arxiv.org/html/1405.5607v1 | converted from HTML -->

Representations of Circular Words

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:1405.5607v1 [cs.FL] 22 May 2014

# Representations of Circular Words

László Hegedüs 1 1 footnotemark: 1 Benedek Nagy 1 1 footnotemark: 1 2 2 footnotemark: 2 Email: [{hegedus.laszlo,˜nbenedek}@inf.unideb.hu][3] Affiliation: 1 1 footnotemark: 1 Department of Computer Science,
Faculty of Informatics, University of Debrecen

###### Abstract

In this article we give two different ways of representations of circular words. Representations with tuples are intended as a compact notation, while representations with trees give a way to easily process all conjugates of a word. The latter form can also be used as a graphical representation of periodic properties of finite (in some cases, infinite) words. We also define iterative representations which can be seen as an encoding utilizing the flexible properties of circular words. Every word over the two letter alphabet can be constructed starting from a ​ b ab by applying the fractional power and the cyclic shift operators one after the other, iteratively.

## 1 Introduction

One of the most popular areas of research in theoretical computer science is combinatorics on words. This field deals with various properties of finite and infinite sequences or words. Being closely related to mathematics, it has connections to algebra, number theory, game theory and several others. Although it was written decades ago, the books of M. Lothaire are good reads and are recommended for researchers who want to get a deep overview of the subject [9, 10, 11]. Axel Thue contributed the first results to the field [20, 21]. Since then many applications in computer science have been discovered (e.g., in string matching, data compression, bioinformatics, etc.).

We deal with circular words (sometimes called necklaces [19] or cyclic words) that are different from linear ones and lead to some interesting new viewpoints. Similar sequences can appear in nature, for example, the DNA sequences of some bacteria has a similar form to a necklace. In the simplest sense, circular words are strongly periodic discrete functions.

Circular words are not as widely investigated as linear words. We hope that our approach and results may show that interesting facts can be obtained by analyzing these sequences. Dirk Nowotka wrote about unbordered conjugates of words in Chapter 4 of his dissertation [14]. Complementing this, we deal with bordered conjugates that have periods smaller than the length of the word. Another related article is [5], where permutations and cyclic permutations of primitive and non-primitive words were investigated. For an overview of current research about circular words, the reader can consult the following articles. Relations to Weinbaum factorizations are investigated in [4]. Several articles were written about pattern avoidance of circular words, for example, [3, 7, 18] to name a few. Other applications in mathematics, namely integer sequences [15, 16] were also considered.

The notion of weak and strong periods was introduced in [8]. One result about periodic functions is often cited in combinatorics on words, since it is clearly about periodic infinite words too. This result belongs to Fine and Wilf [6]. It can be shown by example that this statement is not true for weak periods of circular words [8]. In this paper, we investigate two kinds of representations of circular words continuing the research line of the paper [8] presented at the WORDS 2013 conference in Turku. The first one is connected to the property that every linear word has a shortest root, while the other one is related to tries (see e.g., [19]).

The structure of the paper is as follows. Section 2 defines the notation and notions used in the rest of the article. After this, in Section 3 we discuss ways of representing circular words with tuples and an algorithm to construct one of these representations. Section 4 is about representing circular words with trees (or tries) and we present some results related to Fibonacci words. At the end in Section 5 some possible directions of future research is discussed.

## 2 Preliminaries

The following notions and notation are used in the rest of the article. We will call a non-empty set of symbols an alphabet and denote it by Σ \Sigma. Words (or linear words) over Σ \Sigma are finite sequences of symbols of Σ \Sigma. The operation of concatenation is defined by writing two words after each-other. The empty word, i.e., the empty sequence is denoted by ε \varepsilon and it is the unit element of the monoid Σ ∗ \Sigma^{*}. We also define Σ + = Σ ∗ ∖ { ε } \Sigma^{+}=\Sigma^{*}\setminus\{\varepsilon\}. The length of the word w ∈ Σ ∗ w\in\Sigma^{*} (denoted by | w | |w|) is the length of w w as a sequence, that is, the number of all the symbols in w w. We will use ℕ \mathbb{N} to denote the set of non-negative integers.

We say, that v ∈ Σ ∗ v\in\Sigma^{*} is a factor of w ∈ Σ ∗ w\in\Sigma^{*} if there exist words x, y ∈ Σ ∗ x,y\in\Sigma^{*} such that w = x ​ v ​ y w=xvy. Furthermore, if x = ε x=\varepsilon (resp. y = ε y=\varepsilon), then v v is a prefix (resp. suffix) of w w. For any word w w and integer 0 ≤ k ≤ | w | 0\leq k\leq|w|, we denote the length k k factors of w w by ℱ k ​ ( w) \mathcal{F}_{k}(w). For arbitrary positive integers p p and q q, we use ( p ​ mod ​ q) (p~\mathrm{mod}~q) to denote the remainder of p q \frac{p}{q}. Let w ∈ Σ ∗ w\in\Sigma^{*} be a word of length n n, that is, w = w 1 ​ … ​ w n w=w_{1}\ldots w_{n}, where w 1, …, w n ∈ Σ w_{1},\ldots,w_{n}\in\Sigma. Then for any p ∈ ℕ p\in\mathbb{N}, we have w p n = w ⌊ p n ⌋ ​ w ′ w^{\frac{p}{n}}=w^{\lfloor\frac{p}{n}\rfloor}w^{\prime}, where w ′ = w 1 ​ … ​ w ( p ​ mod ​ n) w^{\prime}=w_{1}\ldots w_{(p~\mathrm{mod}~n)}. We call w p n w^{\frac{p}{n}} the fractional power of w w. From now on we will always refer to the i i th position of a word w ∈ Σ ∗ w\in\Sigma^{*} as w i w_{i}. A word w ∈ Σ + w\in\Sigma^{+} is primitive if there is no word v ∈ Σ ∗ v\in\Sigma^{*} such that w = v p w=v^{p} where p ∈ ℕ p\in\mathbb{N}, p > 1 p>1.

A positive integer p p is a period of w = w 1 ​ … ​ w n w=w_{1}\ldots w_{n} if w i = w i + p w_{i}=w_{i+p} for all i = 1, …, n − p i=1,\ldots,n-p. As a complementary notion, word v ∈ Σ ∗ v\in\Sigma^{*} is a border of w ∈ Σ ∗ w\in\Sigma^{*} if v v is a prefix and also a suffix of w w. Each word w ∈ Σ ∗ w\in\Sigma^{*} has trivial borders ε \varepsilon and w w. It is clear, that word w w has a border b b if and only if w w has period | w | − | b | |w|-|b|.

Words x x and y y are conjugates if there exist words u, v ∈ Σ ∗ u,v\in\Sigma^{*} such that x = u ​ v x=uv and y = v ​ u y=vu. Related to this notion, we define the shift operation σ ​ ( w) \sigma^{\,}(w) for all w ∈ Σ ∗ w\in\Sigma^{*} as follows:

 | σ ​ ( w) = w 2 ​ … ​ w n ​ w 1. \sigma^{\,}(w)=w_{2}\ldots w_{n}w_{1}. |  |

Moreover, σ ℓ ​ ( w) = σ ℓ − 1 ​ ( σ ​ ( w)) = w 1 + ℓ ​ … ​ w n ​ w 1 ​ … ​ w ℓ \sigma^{\,\ell}(w)=\sigma^{\,\ell-1}(\sigma^{\,}(w))=w_{1+\ell}\ldots w_{n}w_{1}\ldots w_{\ell}. Also, we will use σ − ℓ ​ ( w) \sigma^{\,-\ell}(w) that can also be written as σ | w | − ℓ ​ ( w) \sigma^{\,|w|-\ell}(w).

Lyndon and Schützenberger stated the following, which characterizes the relation between a word and its non-trivial borders [13].

###### Lemma 1 (Lyndon and Schützenberger).

Let x ∈ Σ + x\in\Sigma^{+}, y y, b ∈ Σ ∗ b\in\Sigma^{*} be arbitrary words. Then x ​ b = b ​ y xb=by if and only if there exist u ∈ Σ + u\in\Sigma^{+}, v ∈ Σ ∗ v\in\Sigma^{*} and k ∈ ℕ k\in\mathbb{N} such that x = u ​ v x=uv, y = v ​ u y=vu and b = ( u ​ v) k ​ u = u ​ ( v ​ u) k b=(uv)^{k}u=u(vu)^{k}.

A circular word is obtained from a linear word w ∈ Σ ∗ w\in\Sigma^{*} if we link its first symbol after the last one, as seen on Figure 1.

[image: Refer to caption] Figure 1: Creating the circular word w ∘ w_{\circ} from the linear word w w.

One can see from the figure that circular words do not have a beginning nor an end. Nor do the notions of suffix and prefix make sense. A circular word w ∘ w_{\circ} can be seen as the set of all conjugates of w w, or all cyclic shifts of w w, that is, the set

 | w ∘ = { v | v is a conjugate of w } = { σ ℓ ( w) | ℓ = 0, …, | w | − 1 }. w_{\circ}=\{v~|~v~\mbox{ is a conjugate of }~w\}=\{\sigma^{\,\ell}(w)~|~\ell=0,\ldots,|w|-1\}. |  |

Note, that w ∘ w_{\circ} consists exactly of the length | w | |w| factors of w ​ w ww. That is, w ∘ = ℱ | w | ​ ( w ​ w) w_{\circ}=\mathcal{F}_{|w|}(ww). The notions of weak- and strong periods were given in [8]. We will only refer to weak periods in this paper and define them as follows.

###### Definition 1.

The positive integer p p is a weak ( strong) period of a circular word w ∘ w_{\circ} if p p is a period of at least one (all) of the conjugates v ∈ w ∘ v\in w_{\circ}.

## 3 Representations with tuples

If not stated otherwise, we assume that alphabet Σ \Sigma can be arbitrary. Every word w ∈ Σ ∗ w\in\Sigma^{*} can be represented by a power of a (possibly shorter) word u ∈ Σ ∗ u\in\Sigma^{*} and a positive integer that is the length of w w. In other words, for all w ∈ Σ ∗ w\in\Sigma^{*}, there exists a word u ∈ Σ ∗ u\in\Sigma^{*} such that u | w | | u | = w u^{\frac{|w|}{|u|}}=w. We will call such a u u a root of w w, while the shortest root is called the primitive root of w w (see e.g., pages 10–11 of [19]). In this section we discuss analogous representations of circular words that take advantage of their lack of strictly specified endpoints.

###### Definition 2.

A pair ( u, n) ∈ Σ ∗ × ℕ (u,n)\in\Sigma^{*}\times\mathbb{N} is a representation of the circular word w ∘ w_{\circ} over Σ \Sigma if | u | ≤ n |u|\leq n, n = | w ∘ | n=|w_{\circ}| and u n | u | ∈ w ∘ u^{\frac{n}{|u|}}\in w_{\circ}.

###### Definition 3.

A minimal representation of a circular word w ∘ w_{\circ} over Σ \Sigma is a representation ( u, n) (u,n) of w ∘ w_{\circ}, such that | u | ≤ | u ′ | |u|\leq|u^{\prime}| for any other representation ( u ′, n) (u^{\prime},n) of w ∘ w_{\circ}.

It is clear, that every circular word has a minimal representation, since all of them have a smallest weak period. Trivially, that not all pairs ( u, n) (u,n) are minimal representations of some circular word. For example, consider the representation ( b ​ a ​ a, 5) (baa,5) of the circular word ( b ​ a ​ a ​ b ​ a) ∘ (baaba)_{\circ}. This circular word also has a representation ( a ​ b, 5) (ab,5) which is in fact a minimal representation.

It is also true, that a circular word can have more than one minimal representations. For example, ( a ​ b ​ a ​ b ​ a, 12) (ababa,12), ( b ​ a ​ b ​ a ​ a, 12) (babaa,12), ( a ​ b ​ a ​ a ​ b, 12) (abaab,12) and ( b ​ a ​ a ​ b ​ a, 12) (baaba,12) are all minimal representations of the circular word ( a ​ b ​ a ​ b ​ a ​ a ​ b ​ a ​ b ​ a ​ a ​ b) ∘ (ababaababaab)_{\circ}. Note, that ( a ​ a ​ b ​ a ​ b, 12) (aabab,12) is not a minimal representation of this circular word, since it represents ( a ​ a ​ b ​ a ​ b ​ a ​ a ​ b ​ a ​ b ​ a ​ a) ∘ (aababaababaa)_{\circ}.

Clearly, if n = k ⋅ | u | n=k\cdot|u| for some k ∈ ℕ k\in\mathbb{N} in a minimal representation ( u, n) (u,n), then ( σ ℓ ​ ( u), n) (\sigma^{\,\ell}(u),n) is also a minimal representation of the same circular word for all ℓ = 0, …, | u | − 1 \ell=0,\ldots,|u|-1.

Suppose, that w = u m ​ u ′ w=u^{m}u^{\prime} for some u ∈ Σ ∗ u\in\Sigma^{*} where u ′ u^{\prime} is a non empty prefix of u u and m ∈ ℕ ∖ { 0 } m\in\mathbb{N}\setminus\{0\}. Then for every k ∈ ℕ k\in\mathbb{N}, the word w ′ = w ​ u k w^{\prime}=wu^{k} has a cyclic shift σ | w | ​ ( w ′) = u k + m ​ u ′ \sigma^{\,|w|}(w^{\prime})=u^{k+m}u^{\prime}. Thus the circular word w ∘ ′ w^{\prime}_{\circ} has a representation ( u, | w | + k ⋅ | u |) (u,|w|+k\cdot|u|).

###### Theorem 1.

Let ( u, n) (u,n) be a representation of w ∘ w_{\circ}. Suppose, that u u has border s s, that is, u = s ​ x = y ​ s u=sx=ys, and n = 2 ⋅ | u | − | s | n=2\cdot|u|-|s|. Then ( y, n) (y,n) is also a representation of w ∘ w_{\circ}. Moreover, if s s is the longest non-trivial border of u u, then ( y, n) (y,n) is a minimal representation of w ∘ w_{\circ}.

###### Proof.

Let us have a representation ( u, n) (u,n) of w ∘ w_{\circ} that satisfies the assumption, that is, u u has border s s and n = 2 ⋅ | u | − | s | n=2\cdot|u|-|s|. Then u u is in the form u = s ​ x = y ​ s u=sx=ys for some x, y ∈ Σ ∗ x,y\in\Sigma^{*} and w ∘ = ( u ​ y) ∘ = ( y ​ s ​ y) ∘ w_{\circ}=(uy)_{\circ}=(ysy)_{\circ}. By Lemma 1, y ​ y ​ s yys has period | y | |y|, thus w ∘ w_{\circ} has weak period | y | |y| and a representation ( y, n) (y,n).

If s s is the longest non-trivial border of u u, then y y is the primitive root of u u, thus ( y, n) (y,n) is a minimal representation of w ∘ w_{\circ}. ∎

Suppose that we have a representation w ∘ = ( u, n) w_{\circ}=(u,n), where u ∈ Σ ∗ u\in\Sigma^{*} and n ∈ ℕ n\in\mathbb{N}. If | u | ≥ 2 |u|\geq 2, then u u may be compressed further. In other words, we can take a minimal representation ( u ′, | u |) (u^{\prime},|u|) with an additional parameter k ∈ ℕ k\in\mathbb{N}, such that σ k ​ ( u) \sigma^{\,k}(u) has primitive root u ′ u^{\prime}. This method of compression can be done finitely many times, until reaching a word u 0 u_{0} which we will refer to as a minimal root of w ∘ w_{\circ}. We will call these representations iterative representations, defined formally in Definition 4. Of course, if a minimal root of a word w ∘ w_{\circ} has only one letter, then it is in the form ( a | w |) ∘ (a^{|w|})_{\circ} for some a ∈ Σ a\in\Sigma. In this case, this letter is unique and we can refer to it as the minimal root of w ∘ w_{\circ}. Thus words in these forms have trivial representations and we will no longer deal with them.

###### Definition 4.

Let u ∈ Σ ∗ u\in\Sigma^{*}, m ∈ ℕ ∖ { 0 } m\in\mathbb{N}\setminus\{0\} and ℓ 1, ℓ 2, …, ℓ m − 1, ℓ m, k 1, k 2, …, k m − 1 ∈ ℕ \ell_{1},\ell_{2},\ldots,\ell_{m-1},\ell_{m},k_{1},k_{2},\ldots,k_{m-1}\in\mathbb{N}. The 2 ​ m 2m -tuple

 | ( u, ℓ 1, k 1, ℓ 2, k 2, …, ℓ m − 1, k m − 1, ℓ m) (u,\ell_{1},k_{1},\ell_{2},k_{2},\ldots,\ell_{m-1},k_{m-1},\ell_{m}) |  |

is an iterative representation of the circular word w ∘ = ( u m − 1 ℓ m ℓ m − 1) ∘ w_{\circ}=(u_{m-1}^{\frac{\ell_{m}}{\ell_{m-1}}})_{\circ} over the two letter alphabet { a, b } \{a,b\}, where u 0 = u u_{0}=u, u 1 = σ k 1 ​ ( u 0 ℓ 1 | u 0 |) u_{1}=\sigma^{\,k_{1}}(u_{0}^{\frac{\ell_{1}}{|u_{0}|}}) and u i = σ k i ​ ( u i − 1 ℓ i ℓ i − 1) u_{i}=\sigma^{\,k_{i}}(u_{i-1}^{\frac{\ell_{i}}{\ell_{i-1}}}) for all i = 2, …, m − 1 i=2,\ldots,m-1.

###### Example 1.

Consider the circular word w ∘ = ( b ​ a ​ b ​ a ​ b ​ a ​ a ​ b ​ b ​ a ​ b ​ a ​ a ​ b) ∘ w_{\circ}=(bababaabbabaab)_{\circ}. One of its iterative representations is

 | ( b ​ a ​ a, 4, 0, 6, 4, 14). (baa,4,0,6,4,14).\vskip-3.99994pt |  |

By using the previous definition of the words u i u_{i}, the following words are obtained during the reconstruction of the circular word: u 0 = b ​ a ​ a u_{0}=baa, u 1 = b ​ a ​ a ​ b u_{1}=baab, u 2 = b ​ a ​ b ​ a ​ a ​ b u_{2}=babaab and finally, w ∘ = ( b ​ a ​ b ​ a ​ a ​ b ​ b ​ a ​ b ​ a ​ a ​ b ​ b ​ a) ∘ w_{\circ}=(babaabbabaabba)_{\circ}. Note, that no shifting is required in the last step, because w ∘ = v ∘ w_{\circ}=v_{\circ} for all v ∈ w ∘ v\in w_{\circ}.

Of course, every circular word has an iterative representation of the form above that can be constructed with the greedy algorithm in Figure 2. Moreover, the algorithm halts if only if it has found a minimal root.

c onstruct_iterative_representation( w ∘ w_{\circ})

1. 1.

u ← w u\leftarrow w

2. 2.

v ← v\leftarrow find v v such that ( v, | w |) (v,|w|) is a minimal representation of w ∘ w_{\circ}

3. 3.

r ​ e ​ p ← [| w |] rep\leftarrow[|w|] # rep is a vector of integers

4. 4.

while true do

5. 5.

u ← v u\leftarrow v

6. 6.

v ← v\leftarrow find v v such that ( v, | u |) (v,|u|) is a minimal representation of u ∘ u_{\circ}

7. 7.

if | u | = | v | |u|=|v| then # if we have found a minimal root,

8. 8.

break # then the algorithm breaks the loop

9. 9.

endif

10. 10.

k ← k\leftarrow find k k such that σ − k ​ ( u) \sigma^{\,-k}(u) has root v v

11. 11.

r ​ e ​ p ← | u |: k: r ​ e ​ p rep\leftarrow|u|:k:rep # append | u | |u| and k k to r ​ e ​ p rep from the left

12. 12.

endwhile

13. 13.

return v: r ​ e ​ p v:rep

Figure 2: Algorithm for constructing the iterative representation of w ∘ w_{\circ}.

Note, that by using this algorithm, we can process the iterative representation in Example 1 further to obtain ( a ​ b, 3, 1, 4, 0, 6, 4, 14) (ab,3,1,4,0,6,4,14). In fact, the following can be stated about the iterative representations of circular words over the two letter alphabet { a, b } \{a,b\}.

###### Theorem 2.

Let w ∈ { a, b } ∗ w\in\{a,b\}^{*}. If ( u, ℓ 1, k 1, …, ℓ m − 1, k m − 1, | w |) (u,\ell_{1},k_{1},\ldots,\ell_{m-1},k_{m-1},|w|) is a minimal iterative representation of w ∘ w_{\circ}, then | u | ≤ 2 |u|\leq 2.

###### Proof.

It follows from the fact that every word u ∈ { a, b } u\in\{a,b\}, | u | ≥ 3 |u|\geq 3 has a conjugate that has a border of length at least one, thus in this case u ∘ u_{\circ} has a representation ( v, | u |) (v,|u|) such that | v | < | u | |v|<|u|. ∎

Let ( u, ℓ 1, k 1, …, ℓ m − 1, k m − 1, | w |) (u,\ell_{1},k_{1},\ldots,\ell_{m-1},k_{m-1},|w|) be an iterative representation of w ∘ w_{\circ}. It is optimal if for all iterative representations ( u ′, ℓ 1 ′, k 1 ′, …, ℓ m ′ − 1 ′, k m ′ − 1 ′, | w |) (u^{\prime},\ell^{\prime}_{1},k^{\prime}_{1},\ldots,\ell^{\prime}_{m^{\prime}-1},k^{\prime}_{m^{\prime}-1},|w|) of w ∘ w_{\circ}, | u | ≤ | u ′ | |u|\leq|u^{\prime}| and if | u | = | u ′ | |u|=|u^{\prime}|, then m ≤ m ′ m\leq m^{\prime}. In other words an optimal iterative representation of w ∘ w_{\circ} is one with the shortest possible minimal root, such that w ∘ w_{\circ} can be reconstructed from it with the least amount of fractional power operations (regardless of the amount of shift operations required).

The algorithm may not provide an optimal solution for all inputs w ∘ w_{\circ}. For example, consider the circular word ( a ​ b ​ a ​ b ​ a ​ a) ∘ (ababaa)_{\circ}. The algorithm would construct the iterative representation ( a ​ b, 3, 0, 4, 0, 6) (ab,3,0,4,0,6), while an optimal solution would be ( a ​ b, 5, 0, 6) (ab,5,0,6). One of the directions of future research is to look for an efficient algorithm that always finds an optimal iterative representation of any circular word w ∘ w_{\circ} (see Section 5).

Note, that we do not have to restrict ourselves to representations of circular words. If we are looking for a linear word, another shift operation has to be applied at the end of the reconstruction.

Let us now turn to another method of representation, which is not intended as an encoding, nor as a compression, but a way of representing the structure of different conjugates of a word and their relation to each-other (e.g., common prefixes).

## 4 Representations with trees

The tree τ \tau is the tree of the circular word w ∘ w_{\circ} if and only if for any word v = v 1 ​ … ​ v n v=v_{1}\ldots v_{n} in w ∘ w_{\circ}, there exists a path in τ \tau between the root and a leaf node with a series of edges labeled v 1, …, v n v_{1},\ldots,v_{n}.

This approach is related to tries that are data structures representing associative structures. They are often used to search for suffixes or other factors of words. Quite similarly, our trees represent a set of words that are conjugates of each-other. For more information on the use of tries consult [2].

We remark, that in our figures the letters appear as nodes, but they are to be considered as labels of edges between two (unnamed) nodes. This way, the represented words can be seen more clearly. First, consider the circular word

 | ( a ​ b ​ a ​ a ​ b) ∘ = { a ​ b ​ a ​ a ​ b, b ​ a ​ a ​ b ​ a, a ​ a ​ b ​ a ​ b, a ​ b ​ a ​ b ​ a, b ​ a ​ b ​ a ​ a }. (abaab)_{\circ}=\{abaab,baaba,aabab,ababa,babaa\}. |  |

Its tree representation is shown in Figure 4.

[image: Refer to caption] Figure 3: Tree representation of ( a ​ b ​ a ​ a ​ b) ∘ (abaab)_{\circ}.

[image: Refer to caption] Figure 4: Tree representation of ( a ​ a ​ b ​ b ​ c ​ a ​ c) ∘ (aabbcac)_{\circ}.

Now, see Figure 4 for the tree of the circular word ( a ​ a ​ b ​ b ​ c ​ a ​ c) ∘ (aabbcac)_{\circ} (over the three letter alphabet { a, b, c } \{a,b,c\}) which is the set

 | ( a ​ a ​ b ​ b ​ c ​ a ​ c) ∘ = { a ​ a ​ b ​ b ​ c ​ a ​ c, a ​ b ​ b ​ c ​ a ​ c ​ a, b ​ b ​ c ​ a ​ c ​ a ​ a, b ​ c ​ a ​ c ​ a ​ a ​ b, c ​ a ​ c ​ a ​ a ​ b ​ b, a ​ c ​ a ​ a ​ b ​ b ​ c, c ​ a ​ a ​ b ​ b ​ c ​ a }. (aabbcac)_{\circ}=\{aabbcac,abbcaca,bbcacaa,bcacaab,cacaabb,acaabbc,caabbca\}. |  |

Clearly, both trees represent finite-state automata with partially defined, deterministic transition functions. We can distinguish different levels of a tree. Vertex ∘ \circ is on level zero ( ℓ ⁡ ( ∘) = 0 \ell(\circ)=0) and if there is an edge u → v u\to v, then ℓ ⁡ ( v) = ℓ ⁡ ( u) + 1 \ell(v)=\ell(u)+1.

We can see some branching nodes in both trees. The tree in Figure 4 has two branching nodes on level one while no two branching nodes of the tree in Figure 4 are on the same level.

Examining branching nodes is useful for analyzing trees of circular words and the words themselves. Suppose that tree τ \tau has u 1, …, u k u_{1},\ldots,u_{k} branching nodes such that ∘ → a u 1 \circ\to^{a}u_{1} and u i → a u i + 1 u_{i}\to^{a}u_{i+1} for all i = 1, …, k − 1 i=1,\ldots,k-1. Then there is a letter b b such that a k a^{k}, a k − 1 ​ b a^{k-1}b, and thus a k − 2 ​ b, …, a ​ b a^{k-2}b,\ldots,ab, b b are all factors of w ∘ w_{\circ}. If the level of the leaf nodes is k + 1 k+1, then the represented circular word must be ( a k ​ b) ∘ (a^{k}b)_{\circ}. Similarly, if there are branching nodes u 1, …, u m u_{1},\ldots,u_{m} and v 1, …, v k v_{1},\ldots,v_{k} such that ∘ → a u 1 → a … → a u m \circ\to^{a}u_{1}\to^{a}\ldots\to^{a}u_{m} and ∘ → b v 1 → b … → b v k \circ\to^{b}v_{1}\to^{b}\ldots\to^{b}v_{k}, and the level of the leaf nodes is m + k m+k, then the tree can only represent the circular word ( a m ​ b k) ∘ (a^{m}b^{k})_{\circ}. Apart from these simple cases, we can state the following about the relation of circular words and branching nodes in their trees: Let w ∘ w_{\circ} be a circular word with tree τ \tau. There is a branching node in τ \tau on level ℓ \ell if and only if there are two distinct words w ′, w ′′ ∈ w ∘ w^{\prime},w^{\prime\prime}\in w_{\circ}, such that the longest common prefix of w ′ w^{\prime} and w ′′ w^{\prime\prime} is a word of length ℓ \ell. Moreover, if there is a branching node in the tree on level n > 0 n>0, then there is a branching node on level n − 1 n-1. These nodes do not necessarily lie on the same path. To verify this, assume that tree τ \tau contains the edges u → a v u\to^{a}v and u → b s u\to^{b}s, where u ≠ ∘ u\neq\circ. Then there are words x ​ a ​ y, x ​ b ​ z ∈ w ∘ xay,xbz\in w_{\circ} such that x, y, z ∈ Σ ∗ x,y,z\in\Sigma^{*} with | x | > 0 |x|>0, and a, b ∈ Σ a,b\in\Sigma, where Σ \Sigma is an alphabet of at least two letters. Write x = x 1, …, x m x=x_{1},\ldots,x_{m}. Clearly, both x 2 ​ … ​ x m ​ a ​ y ​ x 1 x_{2}\ldots x_{m}ayx_{1} and x 2 ​ … ​ x m ​ b ​ z ​ x 1 x_{2}\ldots x_{m}bzx_{1} are in w ∘ w_{\circ}, having a common prefix of length | x | − 1 |x|-1. Thus there must be a node u ′ u^{\prime} such that the path from ∘ \circ to u ′ u^{\prime} reads x 2 ​ … ​ x m x_{2}\ldots x_{m} and two nodes v ′ v^{\prime} and s ′ s^{\prime}, such that u ′ → a v ′ u^{\prime}\to^{a}v^{\prime} and u ′ → b s ′ u^{\prime}\to^{b}s^{\prime}.

###### Proposition 1.

Consider a circular word w ∘ ∈ { a, b } w_{\circ}\in\{a,b\} with tree τ \tau. If τ \tau has a branching node on level | w | − 2 |w|-2, then there is exactly one branching node on all levels m = 0, …, | w | − 2 m=0,\ldots,|w|-2 of τ \tau.

###### Proof.

From the previous argument, it follows that all levels k < | w | − 2 k<|w|-2 of the tree has at least one branching node. Clearly, the depth of the tree is | w | |w|. Since the root node is branching, the number of possible paths (words) up to level one is two. Moreover, if level k > 0 k>0 has m k ∈ ℕ m_{k}\in\mathbb{N} branching nodes, then the number of all possible paths up to level k + 1 k+1 is equal to the number of all possible paths up to level k k, plus m k m_{k}. Then we get that the number of possible paths on the level of the leaf nodes is 2 + m 1 + … + m | w | − 1 + m | w | = | w | 2+m_{1}+\ldots+m_{|w|-1}+m_{|w|}=|w|. We have stated, m i > 0 m_{i}>0 for all i = 1, …, | w | − 2 i=1,\ldots,|w|-2, thus m | w | − 1 = m | w | = 0 m_{|w|-1}=m_{|w|}=0 and 2 + m 1 + … + m | w | − 2 = | w | 2+m_{1}+\ldots+m_{|w|-2}=|w|. If m i > 1 m_{i}>1 for any i ≥ 1 i\geq 1, then m j = 0 m_{j}=0 for some j ≠ i j\neq i. This is impossible, since all levels under | w | − 2 |w|-2 have at least one branching node, thus m i = 1 m_{i}=1 for all i = 1, …, | w | − 2 i=1,\ldots,|w|-2. ∎

Now, let us analyze an interesting class of words. Let f 1 = b f_{1}=b, f 2 = a f_{2}=a and define f n = f n − 1 ​ f n − 2 f_{n}=f_{n-1}f_{n-2} for all n ≥ 3 n\geq 3. We call f n f_{n} (where n ≥ 1 n\geq 1) the n n th finite Fibonacci word. The infinite Fibonacci word is the limit of the sequence f 1, f 2, … f_{1},f_{2},\ldots

The following lemma describes a well known property of the infinite Fibonacci words.

###### Lemma 2 (see Séébold [17]).

If a word u 2 u^{2} is a factor of the infinite Fibonacci word, then u is a conjugate of some finite Fibonacci word. ∎

Note that the tree in Figure 4 represents the circular word obtained from f 5 f_{5} which is the fifth Fibonacci word. See the trees of ( f 6) ∘ (f_{6})_{\circ} and ( f 7) ∘ (f_{7})_{\circ} in Figure 5. One can observe that the structure of these trees are very similar. This is strongly related to the definition of Fibonacci words.

[image: Refer to caption]

[image: Refer to caption]

Figure 5: Trees of ( f 6) o (f_{6})_{o} and ( f 7) o (f_{7})_{o}.

###### Theorem 3.

Let us denote the tree of the finite Fibonacci word f i f_{i} by φ i \varphi_{i} for all i ∈ ℕ i\in\mathbb{N}. Then for all i ∈ ℕ i\in\mathbb{N}, the tree φ i \varphi_{i} has exactly one branching node on all of its levels, except for the last two.

###### Proof.

Consider the tree φ i \varphi_{i} of the circular Fibonacci word ( f i) ∘ (f_{i})_{\circ} and let ℓ ∈ { 0, …, | f i | } \ell\in\{0,\ldots,|f_{i}|\}. The paths from ∘ \circ to nodes on level k k represent the length k k factors of ( f i) ∘ (f_{i})_{\circ}. By the properties of Fibonacci words (or Sturmian words), we know that the number of distinct factors of length k k in the infinite Fibonacci word is k + 1 k+1. Since all of the length k k words of the tree appear in the infinite Fibonacci word (because it has factor f i 2 f_{i}^{2}), their number must not be more than k + 1 k+1. On the other hand, each tree of a primitive word of length n n must contain n n branching nodes. Thus in φ i \varphi_{i} all branching nodes must be on different levels. ∎

Based on the proof, we can state the following about the trees of circular Fibonacci words.

###### Corollary 1.

For all i, j ∈ ℕ ∖ { 0 } i,j\in\mathbb{N}\setminus\{0\}, if j > i j>i, then φ i \varphi_{i} is a subtree of φ j \varphi_{j}.

Thus the trees of Fibonacci words are not only very similar, but they contain recurring subtrees. Notice in Figure 5, that the tree of ( f 5) ∘ (f_{5})_{\circ} appears in the tree of ( f 6) ∘ (f_{6})_{\circ} which also appears in the tree of ( f 7) ∘ (f_{7})_{\circ}, marked by the dashed lines. Thus we can define the tree φ \varphi which belongs to the limit of the sequence of Fibonacci words, that is, the infinite Fibonacci word. Each path in the tree φ \varphi defines an infinite suffix of the infinite Fibonacci word. This is a consequence of the structure of the trees φ i \varphi_{i} ( i = 1, 2, … i=1,2,\ldots), since all of their words are factors of the infinite Fibonacci word and an infinite factor must be a suffix.

Let us state another interesting fact about branching nodes of trees of circular Fibonacci words.

###### Theorem 4.

Consider the tree φ i \varphi_{i} for any i ∈ ℕ i\in\mathbb{N}. Let u u and u ′ u^{\prime} be branching nodes of φ i \varphi_{i} such that they lie on the same path and there are no other branching nodes between them. Then | ℓ ⁡ ( u) − ℓ ⁡ ( u ′) | |\ell(u)-\ell(u^{\prime})| is a Fibonacci number.

###### Proof.

Assume the contrary, that is, there is a Fibonacci word f i f_{i} such that there are two branching nodes u u, u ′ u^{\prime} in tree φ i \varphi_{i} that lie on the same path and do not have any other branching nodes between them, but | ℓ ⁡ ( u) − ℓ ⁡ ( u ′) | |\ell(u)-\ell(u^{\prime})| is not a Fibonacci number. Then, there exists a Fibonacci word f j f_{j} with j ≥ i j\geq i such that ( f j) ∘ (f_{j})_{\circ} has square factor v ​ v vv where v v is the word constructed from the labels on the path between u u and u ′ u^{\prime}. Moreover, this will be true for all Fibonacci words f j ′ f_{j^{\prime}} where j ′ ≥ j j^{\prime}\geq j. Thus the infinite Fibonacci word must contain the square factor v ​ v vv. This contradicts Lemma 2, since v v cannot be a conjugate of any Fibonacci word because its length is not a Fibonacci number. Thus our indirect assumption is false. ∎

## 5 Conclusion and future directions

Combinatorics on circular words is a field that still has countless open problems and many possible research directions. We have shown some non-traditional methods of considering (representing) circular words. The following questions are still open and may lead to a better characterization of these sequences.

1. 1.

The algorithm presented in Section 3 does not always provide optimal solutions. Is there a way of deciding how to choose the best sequence of roots in the algorithm?

2. 2.

Theorem 2 is about the minimal roots of words over the two letter alphabet. What can we say about words over alphabets of more than two letters?

3. 3.

One could use the tree φ \varphi to deduce some properties of the infinite Fibonacci word.

4. 4.

Or the tree representations can be utilized to prove results about the structure of other (possibly infinite) words.

5. 5.

We believe, that Theorem 3 is true for all standard sturmian words (see e.g., [12] for their definition).

## Acknowledgements

The authors would like to thank the reviewers for their valuable and useful comments. The work is supported by the TÁMOP 4.2.2/C-11/1/KONV-2012-0001 and 4.2.2/B-10/1-2010-0024 projects. The projects are implemented through the New Hungary Development Plan, co-financed by the European Social Fund and the European Regional Development Fund.

## References

- [1]
- [2] Maxime Crochemore & Wojciech Rytter (2002): Jewels of Stringology. World Scientific Publishing Company, Incorporated, [10.1142/4838][4].
- [3] James D. Currie & D. Sean Fitzpatrick (2002): Circular words avoiding patterns. Proceedings of the 6th International Conference on Developments in Language Theory. LNCS 2450., pp. 319–325, [10.1007/3-540-45005-X_28][5].
- [4] Volker Diekert, Tero Harju & Dirk Nowotka (2006): Factorizations of cyclic words. Workshop on Words and Automata at CSR 7.
- [5] Szilárd Zsolt Fazekas & Benedek Nagy (2008): Scattered Subword Complexity of Non-primitive Words. J. Autom. Lang. Comb. 13(3), pp. 233–247.
- [6] Nathan J. Fine & Herbert S. Wilf (1965): Uniqueness theorems for periodic functions. Proceedings of the American Mathematical Society 16, pp. 109–114, [10.1090/S0002-9939-1965-0174934-9][6].
- [7] D. Sean Fitzpatrick (2005): There are binary cube-free circular words of length n n contained within the Thue-Morse word for all positive integers n n. Ars Combinatorica 74.
- [8] László Hegedüs & Benedek Nagy (2013): Periodicity of circular words. Local Proceedings of WORDS 2013, TUCS Lecture Notes 20, pp. 45–56.
- [9] M. Lothaire (1983): Combinatorics on words. Addison-Wesley.
- [10] M. Lothaire (2002): Algebraic Combinatorics on Words. Encyclopedia of Mathematics and its Applications 90, Cambridge University Press, [10.1017/CBO9781107326019][7].
- [11] M. Lothaire (2005): Applied Combinatorics on Words. Encyclopedia of Mathematics and its Applications 105, Cambridge University Press, [10.1017/CBO9781107341005][8].
- [12] Aldo de Luca & Filippo Mignosi (1994): Some combinatorial properties of Sturmian words. Theoretical Computer Science 136(2), pp. 361–385, [10.1016/0304-3975(94)00035-H][9].
- [13] Roger C. Lyndon & Marcel-Paul Schützenberger (1962): The equation a M = b N ​ c P a^{M}=b^{N}c^{P} in a free group. Michigan Math. J. 9(4), pp. 289–298, [10.1307/mmj/1028998766][10].
- [14] Dirk Nowotka (2004): Periodicity and unbordered factors of words. TUCS Dissertations No. 50.
- [15] Benoît Rittaud & Laurent Vivier (2011): Circular words and applications. Proceedings of Words 2011, Electronic Proceedings in Theoretical Computer Science 63, pp. 31–36, [10.4204/EPTCS.63.6][11].
- [16] Benoît Rittaud & Laurent Vivier (2012): Circular words and three applications: factors of the Fibonacci word, ℱ \mathcal{F} -adic numbers, and the sequence 1, 5, 16, 45, 121, 320,…. Funct. Approx. Comment. Math. 47(2), pp. 207–231, [10.7169/facm/2012.47.2.6][12].
- [17] Patrice Séébold (1985): Propriétés combinatoires des mots infinis engendrés par certains morphismes. Thèse de doctorat, Université P. et M. Curie, Institut de Programmation.
- [18] Arseny M. Shur (2010): On ternary square-free circular words. The Electronic Journal of Combinatorics 17.
- [19] William Smyth (2003): Computing patterns in strings. Addison-Wesley.
- [20] Axel Thue (1906): Über unendliche Zeichenreihen. Kra. Vidensk. Selsk. Skrifter, I. Mat. Nat. Kl. 7, pp. 1–22.
- [21] Axel Thue (1912): Über die gegenseitige Lage gleicher Teile gewisser Zeichenreihen. Kra. Vidensk. Selsk. Skrifter, I. Mat. Nat. Kl. 46, pp. 1–67.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:%7Bhegedus.laszlo,%CB%9Cnbenedek%7D@inf.unideb.hu
[4]: https://doi.org/10.1142/4838
[5]: https://doi.org/10.1007/3-540-45005-X_28
[6]: https://doi.org/10.1090/S0002-9939-1965-0174934-9
[7]: https://doi.org/10.1017/CBO9781107326019
[8]: https://doi.org/10.1017/CBO9781107341005
[9]: https://doi.org/10.1016/0304-3975(94)00035-H
[10]: https://doi.org/10.1307/mmj/1028998766
[11]: https://doi.org/10.4204/EPTCS.63.6
[12]: https://doi.org/10.7169/facm/2012.47.2.6
