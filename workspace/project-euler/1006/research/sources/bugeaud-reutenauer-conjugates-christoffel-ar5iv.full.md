<!-- source: https://arxiv.org/html/2202.05486v5 | converted from HTML -->

On the conjugates of Christoffel words

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2202.05486v5 [math.CO] 04 Nov 2025

# On the conjugates of Christoffel words

Yann Bugeaud Christophe Reutenauer Université de Strasbourg et CNRS, Strasbourg, France
Institut universitaire de France
Université du Québec à Montréal, Montréal, Canada

###### Abstract

We introduce a parametrization of the conjugates of Christoffel words based on the integer Ostrowski numeration system. We use it to give a precise description of the borders (prefixes which are also suffixes) of the conjugates of Christoffel words and to revisit the notion of Sturmian graph introduced by Epifanio et al.

###### Keywords:

Combinatorics on words, Christoffel word, Ostrowski numeration

† † dmtcs-publicationdata: Volume vol. 27:3 (2025), #20, doi:10.46298/dmtcs.15140

## 1 Introduction

In an article published in 1875 Christoffel 1875, Christoffel introduced a class of words on a binary alphabet, which now bear his name (following Berstel Berstel 1990); they were shortly after rediscovered by Smith Smith 1876. Independently, in his 1880 work on minima of quadratic functions Markoff 1879; Markoff 1880, Markoff used these words to construct certain quadratic forms, which satisfy sharp inequalities relating their minima and their discriminant. Markoff was certainly unaware of the work of Christoffel. The relation between the work of Markoff and the Christoffel words was explicitly known to Frobenius Frobenius 1913, who also formulated the famous conjecture on the Markoff numbers (see Aigner 2013). The theory of these words may be found in several books: Fogg 2002; Lothaire 2002; Berstel et al. 2009; Aigner 2013; Reutenauer 2019.

The conjugates of Christoffel words (obtained by cyclically permuting these words) also have some importance, since they appear in different areas:

1. They coincide with the elements of the free group with two generators subject to the following conditions: they are positive (that is, with no inverted letter), they are cyclically reduced, and they are part of a basis of this free group; see Osborne and Zieschang 1981; Kassel and Reutenauer 2007.

2. They are the ‘‘perfectly clustering words” on a two-letter alphabet; this means that the last column of the Burrows-Wheeler tableau of such a word 1 1 1 This tableau was defined by Burrows and Wheeler in the theory of data compression, see Restivo and Rosone 2011 Section 4., whose rows are the lexicographically sorted conjugates, is decreasing; see Mantaci et al. 2003; Ferenczi and Zamboni 2013.

3. They constitute the finitary version of the Sturmian (infinite) words, which are obtained by discretizing straight lines in the plane, and which are characterized by the property that for each n n, they have exactly n + 1 n+1 factors of length n n. For example, a word is a conjugate of a Christoffel word if and only if all its conjugates are factors of a Sturmian word; equivalently, this word (of length n n say) is primitive and has exactly n − 1 n-1 circular factors of length n − 2 n-2; see Lothaire 2002, ( Reutenauer 2019, Theorem 15.3.1).

4. Besides the Christoffel words, which encode the Markoff forms and their minima, their conjugates correspond to the “small values” of these quadratic forms; see Reutenauer 2021.

It is well known that Christoffel words are parametrized by nonnegative rational numbers. In the present article we first introduce a parametrization of the conjugates of Christoffel words, which is a finitary version of Bugeaud and Laurent 2023. This parametrization is based on the integer Ostrowski numeration system. It generalizes a construction which is widely used in the theory of Sturmian words, following Rauzy Rauzy 1985 (the “Rauzy rules”), and de Luca and Mignosi de Luca 1997 (the “standard words”). The construction is given in ( 11). Theorem 7.3 states that the whole conjugation class is constructed, and that it is independent of the chosen Ostrowski representation. As a corollary we obtain a result of Frid Frid 2018, which states (in some equivalent formulation) that the prefixes of a standard word are parametrized by legal Ostrowski representations; see Corollary 7.6, which appears as a noncommutative lifting of the Ostrowski numeration system.

In Section 8, we study the borders (a prefix which is also a suffix) of conjugates of Christoffel words. It is well known that the length of the longest border of a word and its smallest period are simply related: their sum is the length of the word. The study of periods in words is an important matter in combinatorics on words, in particular in the theory of Sturmian words: it is known that each finite Sturmian word has a nontrivial proper period, except precisely the Christoffel words. We thus focus on conjugates of Christoffel words, and determine their longest borders. Our parametrization of the conjugates allows us to give precise statements on the form of these borders. In particular, they are themselves conjugates, or a power of them (Theorem 8.1, Corollaries 8.2 and 8.3). Note that smallest periods of conjugates of Christoffel words have been previously computed by Lapointe Lapointe 2017, and applied by her to the determination of normal forms, thereby allowing her to characterize conjugates within the class of Sturmian words. The set of smallest periods is also studied in Hegedüs and Nagy 2016 and Currie and Saari 2009.

In Section 9, we give an application of our methods to notions and results due to Epifanio, Frougny, Gabriele, Mignosi and Shallit Epifanio et al. 2007; Epifanio et al. 2012. The result of Frid, once formulated for the so-called “lazy” Ostrowski representation (a notion introduced by these authors), may be translated into a result on the paths of a certain graph, called the “compact graph”; it states that each suffix of the central word corresponding to a Christoffel word is the label of a unique path, starting from the origin, in this graph. By specializing to lengths, one obtains the “Sturmian graph”: this graph has the property that each integer from 0 to the length of the central word is the label of a unique path; see Corollaries 9.2 and 9.3, due to Epifanio et al. 2007; Epifanio et al. 2012. As a consequence, we obtain the new result that these two graphs are naturally embedded in the tree of central words and in the Stern-Brocot tree; see Corollary 9.5, for the proof of which we use the “iterated palindromisation” of Aldo de Luca.

Note that a link between lazy representations and periods of words was already established by Gabric, Rampersad and Shallit Gabric et al. 2021: they determine the set of periods of each prefix of length n n of a characteristic Sturmian (infinite) word and they show that the cardinality of this set is equal to the sum of the digits in the lazy representation of n n.

In the next five (short) sections, we recall classical results on continuant polynomials, Ostrowski numeration, conjugation, and Christoffel words. Our new results are stated and proved in Sections 7 to 9.

## 2 Continuant polynomials

Continuant polynomials are defined for any k ≥ 0 k\geq 0 and any integers n 1, …, n k n_{1},\ldots,n_{k} as follows: K − 1 = 0, K 0 = 1 K_{-1}=0,K_{0}=1 and

 | K k ​ ( n 1, …, n k) = K k − 1 ​ ( n 1, …, n k − 1) ​ n k + K k − 2 ​ ( n 1, …, n k − 2) K_{k}(n_{1},\ldots,n_{k})=K_{k-1}(n_{1},\ldots,n_{k-1})n_{k}+K_{k-2}(n_{1},\ldots,n_{k-2}) |  |

for any k ≥ 1 k\geq 1 ( right recursion formula). It is customary to drop the index k k and to write K ⁡ ( n 1, …, n k) K(n_{1},\ldots,n_{k}) for K k ​ ( n 1, …, n k) K_{k}(n_{1},\ldots,n_{k}), and in particular K ⁡ () = 1 K()=1. One has (for example Cohn 1985 p. 116)

 | P ( n 1) ⋯ P ( n k) = ( K ⁡ ( n 1, …, n k) K ⁡ ( n 1, …, n k − 1) K ⁡ ( n 2, …, n k) K ⁡ ( n 2, …, n k − 1)), P(n_{1})\cdots P(n_{k})=\left(\begin{array}[]{cc}K(n_{1},\ldots,n_{k})&K(n_{1},\ldots,n_{k-1})\\ K(n_{2},\ldots,n_{k})&K(n_{2},\ldots,n_{k-1})\end{array}\right), |  | (1) |

where P ⁡ ( n) = ( n 1 1 0) P(n)=\left(\begin{array}[]{cc}n&1\\ 1&0\end{array}\right). By associativity of the matrix product, one obtains the left recursion formula:

 | K ⁡ ( n 1, …, n k) = n 1 ​ K ​ ( n 2, …, n k) + K ⁡ ( n 3, …, n k). K(n_{1},\ldots,n_{k})=n_{1}K(n_{2},\ldots,n_{k})+K(n_{3},\ldots,n_{k}). |  |

It follows also, by transposing the product, and using the symmetry of the matrices P ⁡ ( n) P(n), that we have K ⁡ ( n 1, …, n k) = K ⁡ ( n k, …, n 1) K(n_{1},\ldots,n_{k})=K(n_{k},\ldots,n_{1}).

For later use, we mention the identity, for k ≥ 1 k\geq 1,

 | K ⁡ ( n 1, …, n k) = K ⁡ ( n 1 − 1, n 2, …, n k) + K ⁡ ( n 2, …, n k), K(n_{1},\ldots,n_{k})=K(n_{1}-1,n_{2},\ldots,n_{k})+K(n_{2},\ldots,n_{k}), |  | (2) |

which follows easily from the left recursion formula. The link with continued fractions is that each finite continued fraction

 | [n 1, …, n k] = n 1 + 1 n 2 + 1 n 3 + ⋯ + 1 n k [n_{1},\ldots,n_{k}]=n_{1}+\frac{1}{n_{2}+\frac{1}{n_{3}+\cdots+\frac{1}{n_{k}}}} |  |

is equal to the reduced fraction K ⁡ ( n 1, …, n k) / K ⁡ ( n 2, …, n k) K(n_{1},\ldots,n_{k})/K(n_{2},\ldots,n_{k}). Equivalently, the continued fraction [0, n 1, …, n k] [0,n_{1},\ldots,n_{k}] is equal to K ⁡ ( n 2, …, n k) / K ⁡ ( n 1, …, n k) K(n_{2},\ldots,n_{k})/K(n_{1},\ldots,n_{k}).

## 3 Ostrowski numeration

Let a 1, a 2, …, a m a_{1},a_{2},\ldots,a_{m} be a finite sequence of positive natural numbers. Define the positive integers q 0, q 1, …, q_{0},q_{1},\ldots, q m q_{m} by q i = K ⁡ ( a 1, …, a i) q_{i}=K(a_{1},\ldots,a_{i}), for i = 0, …, m i=0,\ldots,m. Note that q 0 = 1 q_{0}=1, q 1 = a 1 q_{1}=a_{1}, q 2 = a 1 ​ a 2 + 1 q_{2}=a_{1}a_{2}+1, and we let q − 1 = 0 q_{-1}=0, in accordance with the conventions for continuant polynomials. Note that the right recursion for continuant polynomials gives q i = q i − 1 ​ a i + q i − 2 q_{i}=q_{i-1}a_{i}+q_{i-2} for any i = 1, …, m i=1,\ldots,m. Note that the sequence of q i q_{i}, i ≥ − 1 i\geq-1, is strictly increasing, except for the following case: a 1 = 1 a_{1}=1, q 0 = q 1 q_{0}=q_{1}.

It is useful to define

 | b 1 = a 1 − 1, b i = a i ​ if ​ i ≥ 2. b_{1}=a_{1}-1,b_{i}=a_{i}\,\,\mbox{if}\,\,i\geq 2. |  | (3) |

Any expression

 | N = d 1 ​ q 0 + d 2 ​ q 1 + ⋯ + d m ​ q m − 1, N=d_{1}q_{0}+d_{2}q_{1}+\cdots+d_{m}q_{m-1}, |  | (4) |

where the digits d i d_{i} ’s are in ℤ \mathbb{Z}, is called (unrestricted) Ostrowski representation of the integer N N. We stress that, unlike in previous works, we allow the digits to be negative.

The representation ( 4) is called legal if one has the inequalities

 | ∀ i ≥ 1, 0 ≤ d i ≤ b i. \forall i\geq 1,0\leq d_{i}\leq b_{i}. |  | (5) |

Among the legal representations, we distinguish two of them. We say that the representation ( 4) is greedy if it is legal and if the following condition is satisfied

 | ∀ i ≥ 2, d i = b i ⇒ d i − 1 = 0. \forall i\geq 2,d_{i}=b_{i}\Rightarrow d_{i-1}=0. |  | (6) |

We say that the representation ( 4) is lazy if it is legal and if, with k = max ⁡ { i ∣ d i ≠ 0 } k=\max\{i\mid d_{i}\neq 0\},

 | ∀ i, 2 ≤ i ≤ k, d i = 0 ⇒ d i − 1 = b i − 1. \forall i,2\leq i\leq k,d_{i}=0\Rightarrow d_{i-1}=b_{i-1}. |  | (7) |

###### Proposition 3.1.

(i) Each integer N = 0, …, q m − 1 N=0,\ldots,q_{m}-1 has a unique greedy representation.

(ii) Each N = 0, …, q m + q m − 1 − 2 N=0,\ldots,q_{m}+q_{m-1}-2 has a unique lazy representation.

The existence of a representation ( 4) is implicit in Ostrowski’s article ( Ostrowski 1922, p.178); (i) is stated in Dupain 1979 p.83, and proved by Fraenkel, ( Fraenkel 1985, Theorem 3) (see also ( Allouche and Shallit 2003, Theorem 3.9.1) for a proof). Lazy Ostrowski representations were introduced by Epifanio, Frougny, Gabriele, Mignosi and Shallit in Epifanio et al. 2012; (ii) follows from their work.

For the sake of completeness, we give a proof of Proposition 3.1 in the Appendix (Section 10).

For later use, we state the following result. We say that a sequence d 1, …, d k d_{1},\ldots,d_{k} is alternating if its values are alternatively 0 0 and b i b_{i}; there are therefore two alternating sequences of length k k.

###### Lemma 3.2.

Let ∑ j = 1 m d j ​ q j − 1 \sum_{j=1}^{m}d_{j}q_{j-1} be a greedy Ostrowski representation. Then, the inequality

 | ∑ j = 1 m ( b j − d j) ​ q j − 1 ≤ q m − 1 − 1 \sum_{j=1}^{m}(b_{j}-d_{j})q_{j-1}\leq q_{m-1}-1 |  |

holds if and only if d m = b m d_{m}=b_{m} and the sequence d i, i = 1, …, m d_{i},i=1,\ldots,m, is alternating.

###### Proof.

By Proposition 3.1 (ii), ∑ j = 1 m b j ​ q j − 1 = q m + q m − 1 − 2 \sum_{j=1}^{m}b_{j}q_{j-1}=q_{m}+q_{m-1}-2 since the left-hand side is a lazy representation, and is necessarily the largest one. Thus the inequality of the lemma is equivalent to ∑ j = 1 m d j ​ q j − 1 ≥ q m − 1 \sum_{j=1}^{m}d_{j}q_{j-1}\geq q_{m}-1. By the proposition again, part (i) this time, this inequality is equivalent to the fact that the left-hand side is the unique greedy representation of q m − 1 q_{m}-1. But by Lemma 10.1 (i), this unique representation is the alternating one, with d m = b m d_{m}=b_{m}. ∎

## 4 Conjugation

We consider an alphabet A A, the free monoid A ∗ A^{*} generated by A A and the free group F ⁡ ( A) F(A) generated by A A. Let 1 1 denote the identity element of A ∗ A^{*}. If g g is in F ⁡ ( A) F(A) and x x in A A, we denote by | g | x |g|_{x} the number of occurrences of x x in g g, where one counts with -1 the occurrences of x − 1 x^{-1}; this is well defined and does not depend on the expression for g g. Moreover, define | g | = ∑ x ∈ A | g | x |g|=\sum_{x\in A}|g|_{x}, the algebraic length of g g. In particular, if g ∈ A ∗ g\in A^{*}, then | g | |g| is the length of g g.

Two words u, v u,v in A ∗ A^{*} are called conjugate if for some words x, y ∈ A ∗ x,y\in A^{*}, one has u = x ​ y, v = y ​ x u=xy,v=yx. The conjugator is the mapping of A ∗ A^{*} into itself that maps each word w = a ​ u w=au, a ∈ A, u ∈ A ∗ a\in A,u\in A^{*}, onto u ​ a ua (with C ⁡ ( 1) = 1 C(1)=1). Hence two words in A ∗ A^{*} are conjugate if and only one is the image of the other under some power of the conjugator: v = C | x | ​ ( u) v=C^{|x|}(u), with the previous notations.

Since y ​ x = x − 1 ​ ( x ​ y) ​ x yx=x^{-1}(xy)x, two words u, v u,v conjugate in A ∗ A^{*} are conjugate in F ⁡ ( A) F(A), too. The converse is also true, as is well known, and one may be more precise.

###### Lemma 4.1.

Let u, v ∈ A ∗ u,v\in A^{*}, g ∈ F ⁡ ( A) g\in F(A) be such that v = g − 1 ​ u ​ g v=g^{-1}ug. Then u, v u,v have the same length n n and v = C | g | ​ ( u) v=C^{|g|}(u). Let r r be the remainder of the Euclidean division of | g | |g| by n n. Then u = x ​ y, v = y ​ x u=xy,v=yx, u, v ∈ A ∗ u,v\in A^{*}, with x x of length r r.

###### Proof.

The first assertion is clear, by definition of the algebraic length.

We may assume that g g is reduced, that is, that g g is written as a product of elements of A A and their inverses, in such a way that no factor a ​ a − 1 aa^{-1} nor a − 1 ​ a a^{-1}a occurs in this product (one obtains a reduced expression of an element g g by removing these factors; it is well known that this algorithm does not change the algebraic length | g | |g|).

We show that v = C | g | ​ ( u) v=C^{|g|}(u), by induction on the length of the reduced expression of g g. If this length is 0, then g = 1 g=1 and the result is evident. Suppose that the length of g g is ≥ 1 \geq 1. We have v = g − 1 ​ u ​ g v=g^{-1}ug and v v is reduced, being in A ∗ A^{*}. Hence the first letter a a of u u is equal to the inverse of the last letter of g − 1 g^{-1}, that is, equal to the first letter of g g. Thus u = a ​ u 1, g = a ​ g 1 u=au_{1},g=ag_{1}, u 1 ∈ A ∗ u_{1}\in A^{*}, g 1 ∈ F ⁡ ( A) g_{1}\in F(A), and g 1 g_{1} is reduced and its length is one less than that of g g. Then v = ( a ​ g 1) − 1 ​ a ​ u 1 ​ a ​ g 1 = g 1 − 1 ​ u 1 ​ a ​ g 1 v=(ag_{1})^{-1}au_{1}ag_{1}=g_{1}^{-1}u_{1}ag_{1}. By induction, v = C | g 1 | ​ ( u 1 ​ a) v=C^{|g_{1}|}(u_{1}a). Hence g = C | g 1 | ∘ C ⁡ ( u) = C | g 1 | + 1 ​ ( u) g=C^{|g_{1}|}\circ C(u)=C^{|g_{1}|+1}(u), which implies the result.

Since C n C^{n} is the identity on the words of length n n, we have C | g | ​ ( u) = C r ​ ( u) C^{|g|}(u)=C^{r}(u), and this implies the last assertion. ∎

## 5 Morphisms

We consider now the alphabet A = { a, b } A=\{a,b\} ordered by a < b a<b.

The endomorphism of A ∗ A^{*} (resp. F ⁡ ( A) F(A)), sending a a onto u u and b b onto v v, is denoted by ( u, v) (u,v). Each endomorphism of A ∗ A^{*} extends uniquely to an endomorphism of F ⁡ ( A) F(A).

We define certain endomorphisms of A ∗ A^{*} and F ⁡ ( A) F(A):

 | E = ( b, a), G = ( a, a ​ b), G ~ = ( a, b ​ a), D = ( b ​ a, b), D ~ = ( a ​ b, b), E=(b,a),G=(a,ab),\widetilde{G}=(a,ba),D=(ba,b),\widetilde{D}=(ab,b), |  |

and

 | π ⁡ ( i, j) = ( a i ​ b ​ a j, a), \pi(i,j)=(a^{i}ba^{j},a), |  |

for all nonnegative integers i, j i,j. Note that all these endomorphisms, when viewed on F ⁡ ( A) F(A), are automorphisms of F ⁡ ( A) F(A).

One has G i = ( a, a i ​ b), D i = ( b i ​ a, b) G^{i}=(a,a^{i}b),D^{i}=(b^{i}a,b), and G ~ j = ( a, b ​ a j), D ~ j = ( a ​ b j, b) \widetilde{G}^{j}=(a,ba^{j}),\widetilde{D}^{j}=(ab^{j},b) for all nonnegative integers i, j i,j. It follows that

 | π ⁡ ( i, 0) = G i ​ E = E ​ D i, π ⁡ ( 0, j) = E ​ D ~ j = G ~ j ​ E. \pi(i,0)=G^{i}E=ED^{i},\pi(0,j)=E\widetilde{D}^{j}=\widetilde{G}^{j}E. |  | (8) |

In particular, the involution E E conjugates G, D G,D, and G ~, D ~ \widetilde{G},\widetilde{D}.

Given an endomorphism f f of F ⁡ ( A) F(A), its abelianization is the matrix

 | M ⁡ ( f) = ( | f ⁡ ( a) | a | f ⁡ ( b) | a | f ⁡ ( a) | b | f ⁡ ( b) | b). M(f)=\left(\begin{array}[]{cc}|f(a)|_{a}&|f(b)|_{a}\\ |f(a)|_{b}&|f(b)|_{b}\end{array}\right). |  |

This function is multiplicative: M ⁡ ( f ′ ∘ f) = M ⁡ ( f ′) ​ M ​ ( f) M(f^{\prime}\circ f)=M(f^{\prime})M(f), for any other endomorphism f ′ f^{\prime}. One has for any element g ∈ F ⁡ ( A) g\in F(A),

 | ( | f ⁡ ( g) | a | f ⁡ ( g) | b) = M ⁡ ( f) ​ ( | g | a | g | b). \left(\begin{array}[]{cc}|f(g)|_{a}\\ |f(g)|_{b}\end{array}\right)=M(f)\left(\begin{array}[]{cc}|g|_{a}\\ |g|_{b}\end{array}\right). |  | (9) |

Observe that the abelianization of the endomorphism ( a i ​ b ​ a j, a) (a^{i}ba^{j},a) is given by

 | M ⁡ ( ( a i ​ b ​ a j, a)) = P ⁡ ( i + j), M((a^{i}ba^{j},a))=P(i+j), |  | (10) |

where P P is defined in Section 2.

For g ∈ G g\in G ( G G is here a group), we denote by γ ⁡ ( g) \gamma(g) the conjugation by g g:

 | γ ⁡ ( g) ​ ( x) = g ​ x ​ g − 1. \gamma(g)(x)=gxg^{-1}. |  |

One has γ ⁡ ( g ​ h) = γ ⁡ ( g) ∘ γ ⁡ ( h) \gamma(gh)=\gamma(g)\circ\gamma(h). For later use, we state the following lemma (which is related to the well-known result that the subgroup of inner automorphisms of G G is a normal subgroup of the group of all automorphisms of G G).

###### Lemma 5.1.

Let φ i, ψ i \varphi_{i},\psi_{i}, i = 1, …, m i=1,\ldots,m, be automorphisms of a group G G and g 1, …, g m ∈ G g_{1},\ldots,g_{m}\in G be such that φ i = γ ⁡ ( g i) ​ ψ i \varphi_{i}=\gamma(g_{i})\psi_{i}. Then

 | φ 1 ⋯ φ m = γ ( g) ψ 1 ⋯ ψ m, \varphi_{1}\cdots\varphi_{m}=\gamma(g)\psi_{1}\cdots\psi_{m}, |  |

where

 | g = g 1 ψ 1 ( g 2) ⋯ ( ψ 1 ⋯ ψ m − 1) ( g m). g=g_{1}\psi_{1}(g_{2})\cdots(\psi_{1}\cdots\psi_{m-1})(g_{m}). |  |

The proof, by induction on m m, is left to the reader.

## 6 Christoffel words

Among many equivalent definitions of Christoffel words, we choose one that is useful for our purpose. A lower (resp. upper) Christoffel word is the image of a a or b b under an endomorphism of A ∗ A^{*} belonging to the monoid of endomorphisms generated by G G and D ~ \widetilde{D} (resp. G ~ \widetilde{G} and D D). A Christoffel word is a lower or an upper Christoffel word. It follows from these definitions that the endomorphisms G, D ~ G,\tilde{D} (resp. G ~, D \tilde{G},D) preserve lower (resp. upper) Christoffel words.

The conjugation class of some Christoffel word is called a Christoffel class. It is known that in each Christoffel class, there is exactly one lower, and one upper, Christoffel word. See Lothaire 2002; Rauzy 1985 for this and other properties of these words.

Since the involution E E exchanges a a and b b, and conjugates G G and D D (resp. G ~ \widetilde{G} and D ~ \widetilde{D}), it exchanges lower and upper Christoffel words.

We define two rational numbers associated to a word w w. We call Slope of w w the ratio | w | b / | w | |w|_{b}/|w|, and slope of w w the ratio | w | b / | w | a |w|_{b}/|w|_{a} (it is infinite if w = b w=b). It follows from the general theory of Christoffel words that for each s s in ℚ + ∪ ∞ \mathbb{Q}_{+}\cup\infty (resp. each S S in [0, 1] [0,1]), there exists a unique lower (resp. upper) Christoffel word of slope s s (resp. of Slope S S); for s ≠ 0, ∞ s\neq 0,\infty (resp. S ≠ 0, 1 S\neq 0,1), these two Christoffel words are distinct and conjugate.

Denoting by S S and s s the Slope and the slope respectively, one has

 | S = s 1 + s, s = S 1 − S. S=\frac{s}{1+s},\,\,s=\frac{S}{1-S}. |  |

Equivalently, S − 1 = 1 + s − 1 S^{-1}=1+s^{-1}. We have S = 0 S=0 if and only if s = 0 s=0, and S = 1 S=1 if and only if s = ∞ s=\infty. Otherwise, 0 < S < 1 0<S<1, and the continued fraction of S S is of the form [0, a 1, …, a m] [0,a_{1},\ldots,a_{m}], where the a i a_{i} are positive integers. Then s − 1 = S − 1 − 1 = [a 1, …, a m] − 1 = [a 1 − 1, a 2, …, a m] s^{-1}=S^{-1}-1=[a_{1},\ldots,a_{m}]-1=[a_{1}-1,a_{2},\ldots,a_{m}] if a 1 ≥ 2 a_{1}\geq 2, and therefore s = [0, a 1 − 1, a 2, …, a m] s=[0,a_{1}-1,a_{2},\ldots,a_{m}]; and if a 1 = 1 a_{1}=1, we have s − 1 = [0, a 2, …, a m] s^{-1}=[0,a_{2},\ldots,a_{m}] hence s = [a 2, …, a m] s=[a_{2},\ldots,a_{m}].

## 7 Construction of the conjugates of a Christoffel word

We fix a sequence a 1, …, a m a_{1},\ldots,a_{m} of positive integers and define b i, q i b_{i},q_{i} as in Section 3.

Following Bugeaud and Laurent 2023, given a sequence of integers d 1, …, d m d_{1},\ldots,d_{m} in ℤ {\mathbb{Z}}, we define the following sequence V i = V i ​ ( d 1, …, d m) V_{i}=V_{i}(d_{1},\ldots,d_{m}), of elements of F ⁡ ( A) F(A), by

 | V − 1 = b, V 0 = a, V_{-1}=b,V_{0}=a, |  |

and, for i = 1, …, m i=1,\ldots,m,

 | V i = V i − 1 b i − d i ​ V i − 2 ​ V i − 1 d i. V_{i}=V_{i-1}^{b_{i}-d_{i}}V_{i-2}V_{i-1}^{d_{i}}. |  | (11) |

Note that we do not ask for the moment that the d i d_{i} be nonnegative. This implies that the exponents in the previous equations may be negative, and the V i V_{i} may be in F ⁡ ( A) ∖ A ∗ F(A)\setminus A^{*}.

It is useful to note that one has the following stability property: V i ​ ( d 1, …, d m) V_{i}(d_{1},\ldots,d_{m}) depends only on a 1, …, a i a_{1},\ldots,a_{i} and on d 1, …, d i d_{1},\ldots,d_{i}. Note that the lengths of the words V i V_{i}, i ≥ 1 i\geq 1, are strictly increasing; the lengths of V − 1 = b V_{-1}=b and V 0 = a V_{0}=a are 1, and the length of V 1 V_{1} is 1 exactly when a 1 = 1 a_{1}=1, in which case V 1 = b V_{1}=b; if a 1 > 1 a_{1}>1, then | V 0 | = 1 < | V 1 | |V_{0}|=1<|V_{1}|.

###### Lemma 7.1.

With the previous definition, for any i = 0, …, m i=0,\ldots,m, the endomorphism ( V i, V i − 1) (V_{i},V_{i-1}) is equal to

 | π ( b 1 − d 1, d 1) ∘ ⋯ ∘ π ( b i − d i, d i). \pi(b_{1}-d_{1},d_{1})\circ\cdots\circ\pi(b_{i}-d_{i},d_{i}). |  |

In particular, the words V i − 1 V_{i-1} and V i V_{i} form the basis of a free submonoid of { a, b } ∗ \{a,b\}^{*}.

###### Proof.

The morphism ( V 0, V − 1) = ( a, b) (V_{0},V_{-1})=(a,b) is the identity morphism, so that the formula is true for i = 0 i=0. Let i ≥ 1 i\geq 1; then

 | ( V i, V i − 1) = ( V i − 1 b i − d i ​ V i − 2 ​ V i − 1 d i, V i − 1) = ( V i − 1, V i − 2) ∘ ( a b i − d i ​ b ​ a d i, a) (V_{i},V_{i-1})=(V_{i-1}^{b_{i}-d_{i}}V_{i-2}V_{i-1}^{d_{i}},V_{i-1})=(V_{i-1},V_{i-2})\circ(a^{b_{i}-d_{i}}ba^{d_{i}},a) |  |

 | = ( V i − 1, V i − 2) ∘ π ⁡ ( b i − d i, d i). =(V_{i-1},V_{i-2})\circ\pi(b_{i}-d_{i},d_{i}). |  |

By induction on i i, we have

 | ( V i − 1, V i − 2) = π ( b 1 − d 1, d 1) ∘ ⋯ ∘ π ( b i − 1 − d i − 1, d i − 1). (V_{i-1},V_{i-2})=\pi(b_{1}-d_{1},d_{1})\circ\cdots\circ\pi(b_{i-1}-d_{i-1},d_{i-1}). |  |

Thus the first assertion of the lemma follows.

The last one follows from the injectivity of the morphisms π ⁡ ( i, j) \pi(i,j) (because they extend to automorphisms of the free group), hence of their product. ∎

###### Lemma 7.2.

Let V m = V m ​ ( d 1, …, d m) V_{m}=V_{m}(d_{1},\ldots,d_{m}).

(i) | V m | a = K ⁡ ( a 1 − 1, a 2, …, a m) |V_{m}|_{a}=K(a_{1}-1,a_{2},\ldots,a_{m}), | V m | b = K ⁡ ( a 2, …, a m) |V_{m}|_{b}=K(a_{2},\ldots,a_{m}), | V m | = K ⁡ ( a 1, …, a m) |V_{m}|=K(a_{1},\ldots,a_{m}).

(ii) The Slope of V m V_{m} is [0, a 1, …, a m] [0,a_{1},\ldots,a_{m}].

###### Proof.

We have, by Lemma 7.1,

 | V m = ( V m, V m − 1) ( a) = π ( b 1 − d 1, d 1) ∘ ⋯ ∘ π ( b m − d m, d m) ( a). V_{m}=(V_{m},V_{m-1})(a)=\pi(b_{1}-d_{1},d_{1})\circ\cdots\circ\pi(b_{m}-d_{m},d_{m})(a). |  |

It follows from Section 5 that

 | ( | V m | a | V m | b) = P ( b 1) ⋯ P ( b m) ( 1 0). \left(\begin{array}[]{cc}|V_{m}|_{a}\\ |V_{m}|_{b}\end{array}\right)=P(b_{1})\cdots P(b_{m})\left(\begin{array}[]{cc}1\\ 0\end{array}\right). |  |

Thus by ( 1) | V m | a = K ⁡ ( b 1, …, b m) |V_{m}|_{a}=K(b_{1},\ldots,b_{m}) and | V m | b = K ⁡ ( b 2, …, b m) |V_{m}|_{b}=K(b_{2},\ldots,b_{m}). We have b i = a i b_{i}=a_{i}, except for i = 1 i=1, where b 1 = a 1 − 1 b_{1}=a_{1}-1. Thus (i) follows, using ( 2) for the third formula, and (ii) follows at once. ∎

If the sequence d 1, …, d m d_{1},\ldots,d_{m} satisfies the inequalities ( 5), then the exponents in ( 11) are all nonnegative, therefore V i ​ ( d 1, …, d m) ∈ A ∗ V_{i}(d_{1},\ldots,d_{m})\in A^{*}. Define

 | M m = V m ( 0, …, 0) = π ( b 1, 0) ∘ ⋯ ∘ π ( b m, 0) ( a), M_{m}=V_{m}(0,\ldots,0)=\pi(b_{1},0)\circ\cdots\circ\pi(b_{m},0)(a), |  | (12) |

the second equality holding by Lemma 7.1. Then M m ∈ A ∗ M_{m}\in A^{*}, and M m M_{m} is of length q m = K ⁡ ( a 1, …, a m) q_{m}=K(a_{1},\ldots,a_{m}), by Lemma 7.2.

###### Theorem 7.3.

The element V m = V m ​ ( d 1, …, d m) V_{m}=V_{m}(d_{1},...,d_{m}) is conjugate within F ⁡ ( A) F(A) to M m M_{m}. Precisely, V m = h − 1 ​ M m ​ h V_{m}=h^{-1}M_{m}h for some h ∈ F ⁡ ( A) h\in F(A) of algebraic length N = d 1 ​ q 0 + ⋯ + d m ​ q m − 1 N=d_{1}q_{0}+\cdots+d_{m}q_{m-1}.

The A ∗ A^{*} -conjugation class of M m M_{m} is equal to the set of all V m ​ ( d 1, …, d m) V_{m}(d_{1},\ldots,d_{m}), for all sequences d 1, …, d m d_{1},\ldots,d_{m} satisfying ( 5) and precisely V m = C N ​ ( M m) V_{m}=C^{N}(M_{m}), with N N as above. This class contains the two Christoffel words of Slope S = [0, a 1, …, a m] S=[0,a_{1},\ldots,a_{m}].

It follows from this theorem that to each sequence a 1, …, a m a_{1},\ldots,a_{m} of positive integers, we associate a Christoffel class.

###### Proof.

By Lemma 7.1,

 | V m = ( V m, V m − 1) ( a) = π ( b 1 − d 1, d 1) ∘ ⋯ ∘ π ( b m − d m, d m) ( a). V_{m}=(V_{m},V_{m-1})(a)=\pi(b_{1}-d_{1},d_{1})\circ\cdots\circ\pi(b_{m}-d_{m},d_{m})(a). |  |

We have

 | π ⁡ ( i, j) = ( a i ​ b ​ a j, a) = γ ⁡ ( a − j) ∘ ( a i + j ​ b, a) = γ ⁡ ( a − j) ∘ π ⁡ ( i + j, 0). \pi(i,j)=(a^{i}ba^{j},a)=\gamma(a^{-j})\circ(a^{i+j}b,a)=\gamma(a^{-j})\circ\pi(i+j,0). |  |

We apply Lemma 5.1 with φ i = π ⁡ ( b i − d i, d i), ψ i = π ⁡ ( b i, 0), g i = a − d i \varphi_{i}=\pi(b_{i}-d_{i},d_{i}),\psi_{i}=\pi(b_{i},0),g_{i}=a^{-d_{i}}. We obtain that

 | V m = γ ( g) ∘ π ( b 1, 0) ∘ ⋯ ∘ π ( b m, 0) ( a) = γ ( g) ( M m), V_{m}=\gamma(g)\circ\pi(b_{1},0)\circ\cdots\circ\pi(b_{m},0)(a)=\gamma(g)(M_{m}), |  |

where g g is equal to

 | a − d 1 ( π ( b 1, 0) ( a − d 2)) ⋯ ( π ( b 1, 0) ∘ ⋯ ∘ π ( b m − 1, 0) ( a − d m)). a^{-d_{1}}(\pi(b_{1},0)(a^{-d_{2}}))\cdots(\pi(b_{1},0)\circ\cdots\circ\pi(b_{m-1},0)(a^{-d_{m}})). |  | (13) |

This implies that V m V_{m} is conjugate within F ⁡ ( A) F(A) to M m M_{m}.

Let h h be the inverse of g g. Then

 | V m = h − 1 ​ M m ​ h V_{m}=h^{-1}M_{m}h |  | (14) |

and, by ( 10) and ( 9), the algebraic length of h h is equal to

 | d 1 + ( 1, 1) P ( b 1) ( d 2, 0) t + ⋯ + ( 1, 1) P ( b 1) ⋯ P ( b m − 1) ( d m, 0) t. d_{1}+(1,1)P(b_{1})\,{}^{t}\!(d_{2},0)+\cdots+(1,1)P(b_{1})\cdots P(b_{m-1})\,{}^{t}\!(d_{m},0). |  |

By ( 1), this is

 | d 1 + ( K ⁡ ( b 1) + K ⁡ ()) ​ d 2 + ⋯ + ( K ⁡ ( b 1, …, b m − 1) + K ⁡ ( b 2, …, b m − 1)) ​ d m d_{1}+(K(b_{1})+K())d_{2}+\cdots+(K(b_{1},\ldots,b_{m-1})+K(b_{2},\ldots,b_{m-1}))d_{m} |  |

 | = d 1 ​ q 0 + d 2 ​ q 1 + ⋯ + d m ​ q m − 1 = N, =d_{1}q_{0}+d_{2}q_{1}+\cdots+d_{m}q_{m-1}=N, |  |

by ( 2), since b i = a i b_{i}=a_{i} if i ≥ 2 i\geq 2, and b 1 = a 1 − 1 b_{1}=a_{1}-1.

If the sequence d 1, …, d m d_{1},\ldots,d_{m} satisfies ( 5), then V m V_{m} is in A ∗ A^{*}, and by Lemma 4.1, V m = C N ​ ( M m) V_{m}=C^{N}(M_{m}), thus V m V_{m} is in the conjugation class of M m M_{m}. Conversely, each element of this class appears, since M m M_{m} is of length K ⁡ ( a 1, …, a m) K(a_{1},\ldots,a_{m}) (Lemma 7.2), and since, by Proposition 3.1, each N = 0, …, K ⁡ ( a 1, …, a m) − 1 N=0,\ldots,K(a_{1},\ldots,a_{m})-1 has an Ostrowski representation satisfying ( 5).

We show now that the class contains a Christoffel word. Consider the sequence d 1, …, d m d_{1},\ldots,d_{m} defined by d m = b m, d m − 1 = 0, d m − 2 = b m − 2 d_{m}=b_{m},d_{m-1}=0,d_{m-2}=b_{m-2}, and so on, depending on the parity of m m. The corresponding element V m V_{m} is in A ∗ A^{*}, and is equal to ⋯ π ( 0, b m − 2) ∘ π ( b m − 1, 0) ∘ π ( 0, b m) ( a) \cdots\pi(0,b_{m-2})\circ\pi(b_{m-1},0)\circ\pi(0,b_{m})(a). If m m is even, then, by ( 8), we have

 | V m = G b 1 E E D ~ b 2 ⋯ G b m − 1 E E D ~ b m ( a); V_{m}=G^{b_{1}}EE\widetilde{D}^{b_{2}}\cdots G^{b_{m-1}}EE\widetilde{D}^{b_{m}}(a); |  |

since E E is an involution, since a a is a lower Christoffel word, and since D ~, G \widetilde{D},G preserve lower Christoffel words, we obtain that V m V_{m} is a lower Christoffel word. If m m is odd, then similarly

 | V m = G ~ b 1 E E D b 2 ⋯ G ~ b m E ( a); V_{m}=\widetilde{G}^{b_{1}}EED^{b_{2}}\cdots\widetilde{G}^{b_{m}}E(a); |  |

since E ⁡ ( a) = b E(a)=b is an upper Christoffel word, and since D, G ~ D,\widetilde{G} preserve upper Christoffel words, we obtain that V m V_{m} is an upper Christoffel word. ∎

###### Corollary 7.4.

Let N = ∑ 1 ≤ i ≤ m d i ​ q i − 1 N=\sum_{1\leq i\leq m}d_{i}q_{i-1} be a greedy representation. Then V m ​ ( d 1, …, d m) V_{m}(d_{1},\ldots,d_{m}) is a Christoffel word if and only if the sequence d 1, …, d m d_{1},\ldots,d_{m} is alternating. Said more precisely, for m ≥ 1 m\geq 1, the word V m ​ ( b 1, 0, b 3, 0, …) V_{m}(b_{1},0,b_{3},0,\ldots) is an upper Christoffel word, and the word V m ​ ( 0, b 2, 0, b 4, …) V_{m}(0,b_{2},0,b_{4},\ldots) is a lower Christoffel word.

###### Proof.

We know that each conjugation class of Christoffel word contains exactly one lower, and one upper, Christoffel word. By Theorem 7.3 and Proposition 3.1 (i), the mapping N ↦ V m ​ ( d 1, …, d m) N\mapsto V_{m}(d_{1},\ldots,d_{m}), where N = ∑ 1 ≤ i ≤ m d i ​ q i − 1 N=\sum_{1\leq i\leq m}d_{i}q_{i-1} is the greedy representation of N N, is a bijection from { 0, 1, …, q m − 1 } \{0,1,\ldots,q_{m}-1\} onto the conjugation class of M m M_{m}. Thus, it is enough to show the last assertion. By the end of the proof of Theorem 7.3, the two indicated words are Christoffel words. Note that a Christoffel word, distinct from a, b a,b (which are both lower and upper), is a lower one if and only if it begins by a a. We observe that if V i V_{i} and V i + 1 V_{i+1} begin by some letter x x, then so do all the words V j V_{j} for j ≥ i j\geq i.

Consider the alternating sequence beginning by 0 0, namely: d 1 = 0, d 2 = b 2, … d_{1}=0,d_{2}=b_{2},\ldots. Then V 1 = a b 1 ​ b V_{1}=a^{b_{1}}b begins by a a if a 1 ≥ 2 a_{1}\geq 2, and is equal to b b if a 1 = 1 a_{1}=1. Thus, if a 1 ≥ 2 a_{1}\geq 2, then V 0, V 1 V_{0},V_{1} begin by a a, hence also do all V i V_{i}, i ≥ 0 i\geq 0. If a 1 = 1 a_{1}=1, then V 2 = V 0 ​ V 1 b 2 = a ​ b b 2 V_{2}=V_{0}V_{1}^{b_{2}}=ab^{b_{2}}, and V 3 = V 2 b 3 ​ V 1 V_{3}=V_{2}^{b_{3}}V_{1} both begin by a a; hence V i V_{i} begins by a a for i ≥ 2 i\geq 2.

Consider now the alternating sequence beginning by b 1 b_{1}, namely: d 1 = b 1, d 2 = 0, … d_{1}=b_{1},d_{2}=0,\ldots. Then V 1 = b ​ a b 1, V 2 = V 1 b 2 ​ a V_{1}=ba^{b_{1}},V_{2}=V_{1}^{b_{2}}a both begin by b b, and therefore all V i V_{i}, i ≥ 1 i\geq 1, begin by b b. ∎

Throughout the paper x ~ {\widetilde{x}} denotes the reversal (mirror image) of the word x x. A palindrome is a word equal to its reversal. The empty word is a palindrome. Recall that each proper lower Christoffel word w w has the factorization w = a ​ p ​ b w=apb, where p p is a palindrome (called a central word), and that then the corresponding upper Christoffel word is w ~ = b ​ p ​ a \widetilde{w}=bpa, which is a conjugate of w w. A standard word is a a or b b, or a word of the from p ​ a ​ b pab or p ​ b ​ a pba for some central word p p; it is known that standard words are obtained from a, b a,b by applying the endomorphisms in the submonoid generated by G G and D D; moreover, each Christoffel class contains exactly two standard words p ​ a ​ b pab and p ​ b ​ a pba, where p p is the corresponding central palindrome. See ( Lothaire 2002, Subsection 2.2.1), Reutenauer 2019.

###### Corollary 7.5.

For m ≥ 1 m\geq 1, the word M m M_{m} is a standard word, equal to p ​ a ​ b pab if m m is odd and to p ​ b ​ a pba if m m is even.

###### Proof.

An easy induction shows that

 | M m = π ( b 1, 0) ∘ ⋯ ∘ π ( b m, 0) ( a) M_{m}=\pi(b_{1},0)\circ\cdots\circ\pi(b_{m},0)(a) |  |

ends by b b if m m is odd, and by a a if m m is even.

Suppose that m m is even. Then by ( 8),

 | M m = π ( b 1, 0) ∘ ⋯ ∘ π ( b m, 0) ( a) = G b 1 E E D b 2 ⋯ E D b m ( a). M_{m}=\pi(b_{1},0)\circ\cdots\circ\pi(b_{m},0)(a)=G^{b_{1}}EED^{b_{2}}\cdots ED^{b_{m}}(a). |  |

Hence M m M_{m} is a standard word. Since it ends by a a, we have M m = p ​ b ​ a M_{m}=pba.

Suppose that m m is odd. Then

 | M m = π ( b 1, 0) ∘ ⋯ ∘ π ( b m, 0) ( a) = G b 1 E E D b 2 ⋯ E D b m − 1 G b m E ( a). M_{m}=\pi(b_{1},0)\circ\cdots\circ\pi(b_{m},0)(a)=G^{b_{1}}EED^{b_{2}}\cdots ED^{b_{m-1}}G^{b_{m}}E(a). |  |

Hence M m M_{m} is a standard word. Since it ends by b b, we have M m = p ​ a ​ b M_{m}=pab. ∎

We may derive a result, which is equivalent to a result previously obtained by Frid, Frid 2018 Corollary 1, and which is a noncommutative version of the Ostrowski representation.

We consider below the Christoffel class associated to the sequence a 1, …, a m a_{1},\ldots,a_{m}.

###### Corollary 7.6.

Let N = 0, …, q m − 2 N=0,\ldots,q_{m}-2 be an integer whose legal Ostrowski representation is given by N = ∑ 1 ≤ i ≤ m d i ​ q i − 1 N=\sum_{1\leq i\leq m}d_{i}q_{i-1}. Then the prefix of length N N of the central palindrome p p is

 | M m − 1 d m ⋯ M 0 d 1. M_{m-1}^{d_{m}}\cdots M_{0}^{d_{1}}. |  |

In particular this product depends only on N N and not on the chosen legal Ostrowski representation of N N.

###### Proof.

The element h = g − 1 h=g^{-1}, appearing in the proof of Theorem 7.3, is by ( 13) and ( 12) equal to

 | h = ( π ( b 1, 0) ∘ ⋯ ∘ π ( b m − 1, 0) ( a d m)) ⋯ ( π ( b 1, 0) ( a d 2)) a d 1 h=(\pi(b_{1},0)\circ\cdots\circ\pi(b_{m-1},0)(a^{d_{m}}))\cdots(\pi(b_{1},0)(a^{d_{2}}))a^{d_{1}} |  |

 | = M m − 1 d m ⋯ M 1 d 2 M 0 d 0. =M_{m-1}^{d_{m}}\cdots M_{1}^{d_{2}}M_{0}^{d_{0}}. |  |

In particular, h h is in A ∗ A^{*}. Because of the inequalities ( 5), the word V m V_{m} is in A ∗ A^{*}, and M m M_{m} is in A ∗ A^{*} too. Moreover, h h is of length N N, by a calculation in the proof of Theorem 7.3; hence | h | < q m = | M m | |h|<q_{m}=|M_{m}|. Thus, by ( 14) and by Lemma 4.1, h h is a prefix of M m M_{m}. Since M m = p ​ a ​ b M_{m}=pab or M m = p ​ b ​ a M_{m}=pba is of length q m q_{m}, we get that h h is a prefix of p p. ∎

Define the sequence c i, i = 1, …, m c_{i},i=1,\ldots,m, by c i = a i c_{i}=a_{i} for i = 2, …, m − 1 i=2,\ldots,m-1 and c i = a i − 1 c_{i}=a_{i}-1 for i = 1, m i=1,m; in other words, the c i c_{i} coincide with the a i a_{i}, except the two extremes c 1, c m c_{1},c_{m}, which are one less; note that c i = b i c_{i}=b_{i}, except that c m = b m − 1 c_{m}=b_{m}-1, if m ≥ 2 m\geq 2. For later use, we prove

###### Lemma 7.7.

Let 1 ≤ i ≤ m 1\leq i\leq m and let 0 ≤ c ≤ c i 0\leq c\leq c_{i}. The word

 | M i − 1 c M i − 2 c i − 1 ⋯ M 1 c 2 M 0 c 1 M_{i-1}^{c}M_{i-2}^{c_{i-1}}\cdots M_{1}^{c_{2}}M_{0}^{c_{1}} |  |

is a palindrome.

This lemma could be deduced from a result of de Luca and Mignosi ( de Luca and Mignosi 1994, Prop. 7). We give an independent proof. See also Lemma 8.7 below.

###### Proof.

By stability, it is enough to prove this result for i = m i=m. Suppose first that b 1 = c 1 ≥ 1 b_{1}=c_{1}\geq 1. We have by Lemma 7.1 and ( 8),

 | M m − 1 c M m − 2 c m − 1 ⋯ M 1 c 2 M 0 c 1 M_{m-1}^{c}M_{m-2}^{c_{m-1}}\cdots M_{1}^{c_{2}}M_{0}^{c_{1}} |  |

 | = [π ( b 1, 0) ⋯ π ( b m − 1, 0) ( a c)] [π ( b 1, 0) ⋯ π ( b m − 2, 0) ( a c m − 1)] =[\pi(b_{1},0)\cdots\pi(b_{m-1},0)(a^{c})][\pi(b_{1},0)\cdots\pi(b_{m-2},0)(a^{c_{m-1}})] |  |

 | ⋯ [π ( b 1, 0) ( a c 2)] [a c 1] \cdots[\pi(b_{1},0)(a^{c_{2}})][a^{c_{1}}] |  |

 | = [G π ( b 1 − 1, 0) ⋯ π ( b m − 1, 0) ( a c)] [G π ( b 1 − 1, 0) ⋯ π ( b m − 2, 0) ( a c m − 1)] =[G\pi(b_{1}-1,0)\cdots\pi(b_{m-1},0)(a^{c})][G\pi(b_{1}-1,0)\cdots\pi(b_{m-2},0)(a^{c_{m-1}})] |  |

 | ⋯ [G π ( b 1 − 1, 0) ( a c 2)] [G ( a c 1 − 1)] a = G ( u) a \cdots[G\pi(b_{1}-1,0)(a^{c_{2}})][G(a^{c_{1}-1})]a=G(u)a |  |

where

 | u = [π ( b 1 − 1, 0) ⋯ π ( b m − 1, 0) ( a c)] [π ( b 1 − 1, 0) ⋯ π ( b m − 2, 0) ( a c m − 1)] u=[\pi(b_{1}-1,0)\cdots\pi(b_{m-1},0)(a^{c})][\pi(b_{1}-1,0)\cdots\pi(b_{m-2},0)(a^{c_{m-1}})] |  |

 | ⋯ [π ( b 1 − 1, 0) ( a c 2)] [a b 1 − 1]. \cdots[\pi(b_{1}-1,0)(a^{c_{2}})][a^{b_{1}-1}]. |  |

By induction on the sum of the a i a_{i}, u u is a palindrome. Hence G ⁡ ( u) ​ a G(u)a is a palindrome ( Reutenauer 2019, Lemma 4.1.4).

Suppose now that b 1 = 0 b_{1}=0, that is a 1 = 1 a_{1}=1. Then, since V 0 = a, V 1 = b V_{0}=a,V_{1}=b, the sequence of words V i, i = 1, …, m, V_{i},i=1,\ldots,m, is obtained from a shorter sequence, to which one applies E E. We may therefore conclude by induction on m m. ∎

The next result is of independent interest. Before stating it, we point out that if d 1, …, d m d_{1},\ldots,d_{m} is a greedy representation, then b 1 − d 1, …, b m − d m b_{1}-d_{1},\ldots,b_{m}-d_{m} is a lazy representation.

###### Proposition 7.8.

For any d 1, …, d m d_{1},\ldots,d_{m}, with 0 ≤ d k ≤ b k 0\leq d_{k}\leq b_{k} for k = 1, …, m k=1,\ldots,m, the word V m ​ ( d 1, …, d m) V_{m}(d_{1},\ldots,d_{m}) is the mirror image of the word V m ​ ( b 1 − d 1, …, b m − d m) V_{m}(b_{1}-d_{1},\ldots,b_{m}-d_{m}).

###### Proof.

This is proved by induction. Write

 | V m = V m − 1 b m − d m ​ V m − 2 ​ V m − 1 d m. V_{m}=V_{m-1}^{b_{m}-d_{m}}V_{m-2}V_{m-1}^{d_{m}}. |  |

Then, we have

 | V ~ m = V ~ m − 1 d m ​ V ~ m − 2 ​ V ~ m − 1 b m − d m = V m ​ ( b 1 − d 1, …, b m − d m), \widetilde{V}_{m}=\widetilde{V}_{m-1}^{d_{m}}{\widetilde{V}}_{m-2}{\widetilde{V}}_{m-1}^{b_{m}-d_{m}}=V_{m}(b_{1}-d_{1},\ldots,b_{m}-d_{m}), |  |

since, by the induction hypothesis, we have

 | V ~ m − 2 = V m − 2 ​ ( b 1 − d 1, …, b m − 2 − d m − 2), {\widetilde{V}}_{m-2}=V_{m-2}(b_{1}-d_{1},\ldots,b_{m-2}-d_{m-2}), |  |

and

 | V ~ m − 1 = V m − 1 ​ ( b 1 − d 1, …, b m − 1 − d m − 1). {\widetilde{V}}_{m-1}=V_{m-1}(b_{1}-d_{1},\ldots,b_{m-1}-d_{m-1}). |  |

The proof is complete. ∎

As a consequence of Proposition 7.8, we find the following well-known result.

###### Corollary 7.9.

Each Christoffel class comprises at most one palindrome and it comprises one palindrome precisely when b 1, …, b m b_{1},\ldots,b_{m} are all even, that is precisely when the words in the class have odd length.

This result is not new: it is a consequence for example of the fact that the Burrows-Wheeler tableau of a Christoffel word (and even each perfectly clustering word) has a central symmetry (Theorem 4.3 of Simpson and Puglisi Simpson and Puglisi 2008).

## 8 Borders of conjugates of Christoffel words

We keep the notation of Section 3. Recall that a border of a word is a nontrivial proper prefix which is also a suffix of this word.

### 8.1 Borders

In this subsection, we determine the longest border of every conjugate of a Christoffel word, thereby reproving a result of Lapointe Lapointe 2017 (but with a totally different method). Indeed, the length of the longest border and the smallest nontrivial period of a word are related: their sum is the length of the word.

Before stating the main result of this section, recall that Corollary 7.4 characterizes the cases where V m V_{m} is a Christoffel word: informally speaking, the digits d i d_{i} of the greedy representation must alternate between b i b_{i} and 0. This extends by stability to each word V i V_{i}, i < m i<m. It is well known that a Christoffel word has no border, which explains the hypothesis in the next result.

Moreover, in this result, we give the longest border of V m V_{m}. The other borders are all determined using Lemma 8.12.

###### Theorem 8.1.

Suppose that m ≥ 3 m\geq 3 or m = 2 m=2 and b 1 ≥ 1 b_{1}\geq 1. Let N N be an integer with 0 ≤ N ≤ q m − 1 0\leq N\leq q_{m}-1 and N = ∑ 1 ≤ i ≤ m d i ​ q i − 1 N=\sum_{1\leq i\leq m}d_{i}q_{i-1} be its greedy representation. Put V m = V m ​ ( d 1, …, d m) V_{m}=V_{m}(d_{1},\ldots,d_{m}), V m − 1 = V m − 1 ​ ( d 1, …, d m − 1) V_{m-1}=V_{m-1}(d_{1},\ldots,d_{m-1}), and V m − 2 = V m − 2 ​ ( d 1, …, d m − 2) V_{m-2}=V_{m-2}(d_{1},\ldots,d_{m-2}). Assume that V m V_{m} is not a Christoffel word. Let

 | ℓ = min ⁡ { b m − d m, d m } and h = min ⁡ { b m − 1 − d m − 1, d m − 1 + 1 }. \ell=\min\{b_{m}-d_{m},d_{m}\}\quad\hbox{and}\quad h=\min\{b_{m-1}-d_{m-1},d_{m-1}+1\}. |  |

Let B B be the longest border of V m V_{m}.

1.

[(i)]

2. 1.

If d m = b m d_{m}=b_{m}, then B = V m − 1 B=V_{m-1}.

3. 2.

If 1 ≤ d m ≤ b m − 1 1\leq d_{m}\leq b_{m}-1 and 1 ≤ d m − 1 ≤ b m − 1 − 1 1\leq d_{m-1}\leq b_{m-1}-1, then B = V m − 1 ℓ B=V_{m-1}^{\ell}.

4. 3.

If 1 ≤ d m ≤ b m − 1 1\leq d_{m}\leq b_{m}-1 and d m − 1 = 0 d_{m-1}=0, then B = V m − 1 ℓ B=V_{m-1}^{\ell}, except if b m − d m < d m b_{m}-d_{m}<d_{m} and the sequence d 1, …, d m − 1 d_{1},\ldots,d_{m-1} is not alternating, in which case B = V m − 1 ℓ + 1 B=V_{m-1}^{\ell+1}.

5. 4.

If 1 ≤ d m ≤ b m − 1 1\leq d_{m}\leq b_{m}-1 and d m − 1 = b m − 1 d_{m-1}=b_{m-1}, then B = V m − 1 ℓ B=V_{m-1}^{\ell}.

6. 5.

If d m = 0 d_{m}=0 and b m ≥ 2 b_{m}\geq 2, then B = V m − 1 b m − 1 ​ V m − 2 B=V_{m-1}^{b_{m}-1}V_{m-2}.

7. 6.

If d m = 0 d_{m}=0, b m = 1 b_{m}=1, and b m − 1 − d m − 1 ≥ 1 b_{m-1}-d_{m-1}\geq 1, B = V m − 2 h B=V_{m-2}^{h}, except if m ≥ 3 m\geq 3, d m − 2 = 0 d_{m-2}=0, b m − 1 − d m − 1 < d m − 1 + 1 b_{m-1}-d_{m-1}<d_{m-1}+1 and the sequence d 1, …, d m − 2 d_{1},\ldots,d_{m-2} is not alternating, in which case B = V m − 2 h + 1 B=V_{m-2}^{h+1}.

8. 7.

If d m = 0 d_{m}=0, b m = 1 b_{m}=1, and d m − 1 = b m − 1 d_{m-1}=b_{m-1}, then B = V m − 2 B=V_{m-2}.

Let us comment briefly the theorem. Since V m = V m − 1 b m − d m ​ V m − 2 ​ V m − 1 d m V_{m}=V_{m-1}^{b_{m}-d_{m}}V_{m-2}V_{m-1}^{d_{m}}, we see that V m − 1 min ⁡ { b m − d m, d m } V_{m-1}^{\min\{b_{m}-d_{m},d_{m}\}} is an obvious border of V m V_{m}. The point is that it may happen that it is not the longest. Indeed, if the last three digits in the greedy representation of N N are d m − 2, 0, d m d_{m-2},0,d_{m}, with d m ≥ 1 d_{m}\geq 1 and d m − 2 ≤ b m − 2 − 1 d_{m-2}\leq b_{m-2}-1, then

 | ( ∑ 1 ≤ i ≤ m − 3 d i ​ q i − 1) + ( d m − 2 + 1) ​ q m − 3 + b m − 1 ​ q m − 2 + ( d m − 1) ​ q m − 1 \Bigl(\,\sum_{1\leq i\leq m-3}d_{i}q_{i-1}\Bigr)+(d_{m-2}+1)q_{m-3}+b_{m-1}q_{m-2}+(d_{m}-1)q_{m-1} |  |

is a legal representation of N N. These representations induce, respectively, the factorizations

 | V m = V m − 1 b m − d m ​ V m − 2 ​ V m − 1 d m V_{m}=V_{m-1}^{b_{m}-d_{m}}V_{m-2}V_{m-1}^{d_{m}} |  | (15) |

and

 | V m = V m − 1 b m − d m + 1 ​ V m − 2 ′ ​ V m − 1 d m − 1, V_{m}=V_{m-1}^{b_{m}-d_{m}+1}V^{\prime}_{m-2}V_{m-1}^{d_{m}-1}, |  |

where we have V m − 1 ​ V m − 2 ′ = V m − 2 ​ V m − 1 V_{m-1}V^{\prime}_{m-2}=V_{m-2}V_{m-1} and V m − 1 = V m − 2 b m − 1 ​ V m − 3 = V m − 3 ​ ( V m − 2 ′) b m − 1 V_{m-1}=V_{m-2}^{b_{m-1}}V_{m-3}=V_{m-3}(V^{\prime}_{m-2})^{b_{m-1}}. In this case, V m − 1 min ⁡ { b m − d m + 1, d m } V_{m-1}^{\min\{b_{m}-d_{m}+1,d_{m}\}} is the longest border of V m V_{m}.

The key point for the proof of Theorem 8.1 is the determination of all the occurrences of V m − 1 V_{m-1} in V m V_{m}. Exactly b m b_{m} of them can be read on the factorization ( 15), but there may be additional ones. By primitivity of V m − 1 V_{m-1}, the word V m − 1 ​ V m − 1 V_{m-1}V_{m-1} contains exactly two occurrences of V m − 1 V_{m-1}. Consequently, if an additional occurrence of V m − 1 V_{m-1} appears, then it must be a factor of V m − 1 ​ V m − 2 ​ V m − 1 V_{m-1}V_{m-2}V_{m-1}. A more precise statement is given in Lemma 8.14.

Theorem 8.1 will be proved in Section 8.3.

### 8.2 Consequences

We display a direct consequence of Theorem 8.1.

###### Corollary 8.2.

Any border of a conjugate of a Christoffel word is a power of a conjugate of a Christoffel word.

As noted by one of the referees, this result may also be obtained as follows: if u u is a border of the Christoffel word w w, then u ​ u uu is a factor of w ​ w ww; since w ​ w ww is a Sturmian word, it is Sturmian, and thus u ​ u uu too. Hence all conjugates of u u are Sturmian. Among them is the power ℓ k \ell^{k} of some Lyndon word ℓ \ell, which is therefore Sturmian; hence ℓ \ell is a Christoffel word by a theorem of Berstel and de Luca (see Reutenauer 2019 Corollary 13.4.3).

One may be more precise. For this we need a notation, since we deal with different sequences a 1, …, a m a_{1},\ldots,a_{m}. We write

 | H N ​ ( a 1, …, a m) = C N ​ ( M m), H_{N}(a_{1},\ldots,a_{m})=C^{N}(M_{m}), |  |

where M m = V m ​ ( 0, …, 0) M_{m}=V_{m}(0,\ldots,0) is as before the word corresponding to the sequence a 1, …, a m a_{1},\ldots,a_{m} and to the Ostrowski representation of 0. Note that here N N may be in ℤ \mathbb{Z}; but the word H N ​ ( a 1, …, a m) H_{N}(a_{1},\ldots,a_{m}) depends only on N N modulo q m q_{m}, where q m q_{m} is the length of this word (recall that q j = K j ​ ( a 1, …, a j) q_{j}=K_{j}(a_{1},\ldots,a_{j})).

###### Corollary 8.3.

Let a 1 ​ …, a m a_{1}\ldots,a_{m} be a sequence of positive integers. If N = q m − 1 − 1 N=q_{m-1}-1 or N = q m − 1 N=q_{m}-1, then H N ​ ( a 1, …, a m) H_{N}(a_{1},\ldots,a_{m}) is a Christoffel word and has no border.

Now, let 0 ≤ N ≤ q m − 1 0\leq N\leq q_{m}{-1}, N ≠ q m − 1 − 1, q m − 1 N\neq q_{m-1}-1,q_{m}-1, and denote by B N B_{N} the longest border of H N ​ ( a 1, …, a m) H_{N}(a_{1},\ldots,a_{m}).

(a) Suppose that a m ≥ 2 a_{m}\geq 2.

If 0 ≤ N < q m − 1 − 1 0\leq N<q_{m-1}-1, then B N = H N ​ ( a 1, …, a m − 1, a m − 1) B_{N}=H_{N}(a_{1},\ldots,a_{m-1},a_{m}-1).

If q m − 1 ≤ N < q m − 1 q_{m-1}\leq N<q_{m}{-1}, then B N = H N ​ ( a 1, …, a m − 1) t B_{N}=H_{N}(a_{1},\ldots,a_{m-1})^{t}, where t = min ⁡ { ⌊ N q m − 1 ⌋, 1 + ⌊ q m − 2 − N q m − 1 ⌋ } t=\min\{\lfloor\frac{N}{q_{m-1}}\rfloor,1+\lfloor\frac{q_{m}-2-N}{q_{m-1}}\rfloor\}.

(b) Suppose that a m = 1 a_{m}=1.

If 0 ≤ N < q m − 1 − 1 0\leq N<q_{m-1}-1, then B N = H N ​ ( a 1, …, a m − 2) t B_{N}=H_{N}(a_{1},\ldots,a_{m-2})^{t}, where t = 1 + min ⁡ { ⌊ N q m − 2 ⌋, ⌊ q m − 1 − 2 − N q m − 2 ⌋ } t=1+\min\{\lfloor\frac{N}{q_{m-2}}\rfloor,\lfloor\frac{q_{m-1}-2-N}{q_{m-2}}\rfloor\}.

If q m − 1 ≤ N < q m − 1 q_{m-1}\leq N<q_{m}{-1}, then B N = H N ​ ( a 1, …, a m − 1) B_{N}=H_{N}(a_{1},\ldots,a_{m-1}).

Note that we recover a step function (the number t t in the statement) as it appears in Lapointe’s article, see for example ( Lapointe 2017, Figure 3).

Recall that E E denotes the involution which permutes a a and b b.

###### Lemma 8.4.

Suppose that a 1 = 1 a_{1}=1. Let V i V_{i}, i = 0, …, m i=0,\ldots,m, be as usual and V i ′ V^{\prime}_{i}, i = 0, …, m − 1 i=0,\ldots,m-1, the sequence of words associated with the sequence of positive numbers a 2 + 1, a 3, …, a m a_{2}+1,a_{3},\ldots,a_{m}. Then for any legal Ostrowski representation N = ∑ 1 ≤ i ≤ m d i ​ q i − 1 N=\sum_{1\leq i\leq m}d_{i}q_{i-1} (so that d 1 = 0 d_{1}=0), one has

 | V m ​ ( d 1, d 2, …, d m) = E ⁡ ( V m − 1 ′ ​ ( d 2, …, d m)). V_{m}(d_{1},d_{2},\ldots,d_{m})=E\bigl(V^{\prime}_{m-1}(d_{2},\ldots,d_{m})\bigr). |  |

###### Proof.

Denote the new sequence by a ′ 1 = a 2 + 1, a ′ 2 = a 3, …, a ′ m − 1 = a m a^{\prime}_{1}=a_{2}+1,a^{\prime}_{2}=a_{3},\ldots,a^{\prime}_{m-1}=a_{m}; then the associated sequence of b i b_{i} ’s is b ′ 1 = a ′ 1 − 1 = a 2, b ′ 2 = a ′ 2, …, b ′ m − 1 = a ′ m − 1 b^{\prime}_{1}=a^{\prime}_{1}-1=a_{2},b^{\prime}_{2}=a^{\prime}_{2},\ldots,b^{\prime}_{m-1}=a^{\prime}_{m-1}. Recall that V − 1 = V − 1 ′ = b, V 0 = V 0 ′ = a V_{-1}=V^{\prime}_{-1}=b,V_{0}=V^{\prime}_{0}=a. Observe that V 1 = b V_{1}=b, V 2 = b a 2 − d 2 ​ a ​ b d 2 V_{2}=b^{a_{2}-d_{2}}ab^{d_{2}}, while V 1 ′ = a a 2 − d 2 ​ b ​ a d 2 V^{\prime}_{1}=a^{a_{2}-d_{2}}ba^{d_{2}}. Thus, V 1 = E ⁡ ( V 0 ′) V_{1}=E(V^{\prime}_{0}) and V 2 = E ⁡ ( V 1 ′) V_{2}=E(V^{\prime}_{1}). An immediate induction based on ( 11) proves the lemma. ∎

###### Lemma 8.5.

Suppose that a m = 1 a_{m}=1. Let V i V_{i}, i = 1, …, m i=1,\ldots,m, be as usual and V i ′ V^{\prime}_{i}, i = 1, …, m − 1 i=1,\ldots,m-1, the sequence of words associated with the sequence of positive numbers a 1, …, a m − 2, a m − 1 + 1 a_{1},\ldots,a_{m-2},a_{m-1}+1. Then for any legal Ostrowski representation N = ∑ 1 ≤ i ≤ m d i ​ q i − 1 N=\sum_{1\leq i\leq m}d_{i}q_{i-1} (so that d m = 0 d_{m}=0 or 1 1), one has

 | V m ​ ( d 1, …, d m − 1, 0) = V m − 1 ′ ​ ( d 1, …, d m − 2, d m − 1 + 1), V_{m}(d_{1},\ldots,d_{m-1},0)=V^{\prime}_{m-1}(d_{1},\ldots,d_{m-2},d_{m-1}+1), |  |

 | V m ​ ( d 1, …, d m − 1, 1) = V m − 1 ′ ​ ( d 1, …, d m − 2, d m − 1). V_{m}(d_{1},\ldots,d_{m-1},1)=V^{\prime}_{m-1}(d_{1},\ldots,d_{m-2},d_{m-1}). |  |

###### Proof.

Let q i q_{i} be as usual and write q i ′ q^{\prime}_{i} for the corresponding numbers with respect to the sequence a 1, …, a m − 2, a m − 1 + 1 a_{1},\ldots,a_{m-2},a_{m-1}+1. By stability, we have V i = V i ′ V_{i}=V^{\prime}_{i} for i = 1, …, m − 2 i=1,\ldots,m-2. Next, we see that V m − 1 = V m − 2 b m − 1 − d m − 1 ​ V m − 3 ​ V m − 2 d m − 1 V_{m-1}=V_{m-2}^{b_{m-1}-d_{m-1}}V_{m-3}V_{m-2}^{d_{m-1}}. Thus,

 | V m ​ ( d 1, …, d m − 1, 0) = V m − 1 ​ V m − 2 = V m − 2 b m − 1 − d m − 1 ​ V m − 3 ​ V m − 2 d m − 1 + 1 = V ′ m − 2 b m − 1 − d m − 1 ​ V m − 3 ′ ​ V ′ m − 2 d m − 1 + 1 V_{m}(d_{1},\ldots,d_{m-1},0)=V_{m-1}V_{m-2}=V_{m-2}^{b_{m-1}-d_{m-1}}V_{m-3}V_{m-2}^{d_{m-1}+1}\\ ={V^{\prime}}_{m-2}^{b_{m-1}-d_{m-1}}V^{\prime}_{m-3}{V^{\prime}}_{m-2}^{d_{m-1}+1} |  |

 | = V m − 1 ′ ​ ( d 1, …, d m − 2, d m − 1 + 1). =V^{\prime}_{m-1}(d_{1},\ldots,d_{m-2},d_{m-1}+1). |  |

Moreover,

 | V m ​ ( d 1, …, d m − 1, 1) = V m − 2 ​ V m − 1 = V m − 2 b m − 1 − d m − 1 + 1 ​ V m − 3 ​ V m − 2 d m − 1 V_{m}(d_{1},\ldots,d_{m-1},1)=V_{m-2}V_{m-1}=V_{m-2}^{b_{m-1}-d_{m-1}+1}V_{m-3}V_{m-2}^{d_{m-1}} |  |

 | = V ′ m − 2 b m − 1 − d m − 1 + 1 ​ V m − 3 ′ ​ V ′ m − 2 d m − 1 ={V^{\prime}}_{m-2}^{b_{m-1}-d_{m-1}+1}V^{\prime}_{m-3}{V^{\prime}}_{m-2}^{d_{m-1}} |  |

 | = V m − 1 ′ ​ ( d 1, …, d m − 2, d m − 1), =V^{\prime}_{m-1}(d_{1},\ldots,d_{m-2},d_{m-1}), |  |

and the proof is complete. ∎

###### of Corollary 8.3.

We assume that m ≥ 2 m\geq 2, since the case m = 1 m=1 is easy to handle directly. We exclude the case m = 2, b 1 = 0 m=2,b_{1}=0, which, by Lemma 8.4, reduces to the case m = 1 m=1.

1. By Theorem 7.3, H N ​ ( a 1, …, a m) H_{N}(a_{1},\ldots,a_{m}) is equal to the word V m ​ ( d 1, …, d m) V_{m}(d_{1},\ldots,d_{m}), where N N has the greedy representation N = ∑ 1 ≤ i ≤ m d i ​ q i − 1 N=\sum_{1\leq i\leq m}d_{i}q_{i-1}. By Corollary 7.4 and Lemma 10.1 (i), the word H i ​ ( a 1, …, a m) H_{i}(a_{1},\ldots,a_{m}) is a Christoffel word if and only if N N is equal to q m − 1 − 1 q_{m-1}-1 or to q m − 1 q_{m}-1.

2. We study now the number t t in Part (a) of the statement. Since N = d m ​ q m − 1 + ∑ 1 ≤ i ≤ m − 1 d i ​ q i − 1 N=d_{m}q_{m-1}+\sum_{1\leq i\leq m-1}d_{i}q_{i-1}, we get ⌊ N q m − 1 ⌋ = d m \lfloor\frac{N}{q_{m-1}}\rfloor=d_{m} by Lemma 10.2 (i).

Next, let j = ∑ 1 ≤ i ≤ m − 1 d i ​ q i − 1 j=\sum_{1\leq i\leq m-1}d_{i}q_{i-1}. Then q m − 2 − N = b m ​ q m − 1 + q m − 2 − 2 − d m ​ q m − 1 − j = ( b m − d m) ​ q m − 1 + q m − 2 − 2 − j q_{m}-2-N=b_{m}q_{m-1}+q_{m-2}-2-d_{m}q_{m-1}-j=(b_{m}-d_{m})q_{m-1}+q_{m-2}-2-j. We have therefore p:= 1 + ⌊ q m − 2 − N q m − 1 ⌋ = 1 + b m − d m + ⌊ q m − 2 − 2 − j q m − 1 ⌋ p:=1+\lfloor\frac{q_{m}-2-N}{q_{m-1}}\rfloor=1+b_{m}-d_{m}+\lfloor\frac{q_{m-2}-2-j}{q_{m-1}}\rfloor.

We show that the numerator in the latter fraction is always in the interval [− q m − 1, q m − 1) [-q_{m-1},q_{m-1}), so that the integer part of this fraction is either − - 1 or 0, and we give the condition when it is 0 0. We have indeed − q m − 1 ≤ q m − 2 − 2 − j -q_{m-1}\leq q_{m-2}-2-j, since j ≤ q m − 1 − 1 j\leq q_{m-1}-1 by Lemma 10.2 (i), so that j + 2 ≤ q m − 1 + 1 ≤ q m − 1 + q m − 2 j+2\leq q_{m-1}+1\leq q_{m-1}+q_{m-2}. Moreover, q m − 2 − 2 − j < q m − 1 q_{m-2}-2-j<q_{m-1}, since the sequence q i q_{i} is increasing. Also, if d m − 1 > 0 d_{m-1}>0, then j ≥ q m − 2 j\geq q_{m-2}, hence q m − 2 − 2 − j < 0 q_{m-2}-2-j<0; and if d m − 1 = 0 d_{m-1}=0, then j = ∑ 1 ≤ i ≤ m − 2 d i ​ q i − 1 j=\sum_{1\leq i\leq m-2}d_{i}q_{i-1}, and q m − 2 − 2 − j < 0 q_{m-2}-2-j<0 if and only if j ≥ q m − 2 − 1 j\geq q_{m-2}-1, which, by Lemmas 10.1 (i) and 10.2 (i), is equivalent to the fact that the sequence d 1, …, d m − 2, 0 d_{1},\ldots,d_{m-2},0 is alternating.

It follows that p = b m − d m p=b_{m}-d_{m}, except if d m − 1 = 0 d_{m-1}=0 and if the sequence d 1, …, d m − 2, 0 d_{1},\ldots,d_{m-2},0 is not alternating, in which case p = b m − d m + 1 p=b_{m}-d_{m}+1. Note that in all cases, p = b m − d m p=b_{m}-d_{m} or p = b m − d m + 1 p=b_{m}-d_{m}+1.

3. We deduce from the previous part of the proof that t = min ⁡ { d m, b m − d m } = ℓ t=\min\{d_{m},b_{m}-d_{m}\}=\ell (defined in Theorem 8.1), except if d m − 1 = 0 d_{m-1}=0, if b m − d m < d m b_{m}-d_{m}<d_{m}, and if the sequence d 1, …, d m − 2, 0 d_{1},\ldots,d_{m-2},0 is not alternating, in which case t = ℓ + 1 t=\ell+1. This follows since if b m − d m ≥ d m b_{m}-d_{m}\geq d_{m}, then t = min ⁡ { d m, p } = d m = min ⁡ { d m, b m − d m } = ℓ t=\min\{d_{m},p\}=d_{m}=\min\{d_{m},b_{m}-d_{m}\}=\ell, because p = b m − d m p=b_{m}-d_{m} or p = b m − d m + 1 p=b_{m}-d_{m}+1.

4. We assume that a m ≥ 2 a_{m}\geq 2. Suppose that 0 ≤ N < q m − 1 − 1 0\leq N<q_{m-1}-1. Then d m = 0 d_{m}=0 by Lemma 10.2 (i). By Theorem 8.1 (v), we have B N = V m − 1 b m − 1 ​ V m − 2 = H N ​ ( a 1, …, a m − 1, a m − 1) B_{N}=V_{m-1}^{b_{m}-1}V_{m-2}=H_{N}(a_{1},\ldots,a_{m-1},a_{m}-1).

Suppose now that q m − 1 ≤ N < q m q_{m-1}\leq N<q_{m}. Then d m > 0 d_{m}>0 by Lemma 10.2 (i). We are therefore in case (i), (ii), (iii) or (iv) of Theorem 8.1. Note that V m − 1 = H J ​ ( a 1, …, a m − 1) V_{m-1}=H_{J}(a_{1},\ldots,a_{m-1}), where J = ∑ 1 ≤ i ≤ m − 1 d i ​ q i − 1 J=\sum_{1\leq i\leq m-1}d_{i}q_{i-1}, so that V m − 1 = H N ​ ( a 1, …, a m − 1) V_{m-1}=H_{N}(a_{1},\ldots,a_{m-1}), because N N is congruent to J J modulo q m − 1 q_{m-1}, the length of V m − 1 V_{m-1}. Thus we have to show that B N = V m − 1 t B_{N}=V_{m-1}^{t}.

In case (i), B N = V m − 1 t B_{N}=V_{m-1}^{t}; indeed, d m = b m d_{m}=b_{m} implies d m − 1 = 0 d_{m-1}=0 by greedyness, and since the sequence d 1, …, d m d_{1},\ldots,d_{m} is not alternating, t = 1 t=1 by Part 3.

In case (ii), B N = V m − 1 ℓ B_{N}=V_{m-1}^{\ell}, and ℓ = t \ell=t by Part 3.

In case (iii), we have d m − 1 = 0 d_{m-1}=0 and B N = V m − 1 ℓ B_{N}=V_{m-1}^{\ell}, except in the following case: b m − d m < d m b_{m}-d_{m}<d_{m}, the sequence d 1, …, d m − 1 d_{1},\ldots,d_{m-1} is not alternating, and then B N = V m − 1 ℓ + 1 B_{N}=V_{m-1}^{\ell+1}. Thus B N = V n − 1 t B_{N}=V_{n-1}^{t} by Part 3.

In case (iv), we have B N = V m − 1 ℓ B_{N}=V_{m-1}^{\ell} and ℓ = t \ell=t by Part 3 since d m − 1 ≠ 0 d_{m-1}\neq 0.

5. We assume that a m = 1 a_{m}=1. Define a i ′ = a i a^{\prime}_{i}=a_{i} if i = 1, …, m − 2 i=1,\ldots,m-2 and a m − 1 ′ = a m − 1 + 1 a^{\prime}_{m-1}=a_{m-1}+1. We denote by q i ′ q^{\prime}_{i} and M i ′ M^{\prime}_{i} the corresponding words and numbers. We have q i ′ = q i q^{\prime}_{i}=q_{i} for i = 1, …, m − 2 i=1,\ldots,m-2 and by ( 2), q m − 1 ′ = q m − 1 + q m − 2 = q m q^{\prime}_{m-1}=q_{m-1}+q_{m-2}=q_{m}.

We have H N ​ ( a 1, …, a m) = C N ​ ( M m) = C N ​ ( V m ​ ( 0, …, 0)) = C N ​ ( V m − 1 ′ ​ ( 0, …, 0, 1)) H_{N}(a_{1},\ldots,a_{m})=C^{N}(M_{m})=C^{N}(V_{m}(0,\ldots,0))=C^{N}(V^{\prime}_{m-1}(0,\ldots,0,1)) (by Lemma 8.5) = C N ​ ( C q m − 2 ​ ( M m − 1 ′)) =C^{N}(C^{q_{m-2}}(M^{\prime}_{m-1})) (by Theorem 7.3 and because q m − 2 ′ = q m − 2 q^{\prime}_{m-2}=q_{m-2}) = C N + q m − 2 ​ ( M m − 1 ′) = H N + q m − 2 ​ ( a 1 ′, …, a m − 1 ′) =C^{N+q_{m-2}}(M^{\prime}_{m-1})=H_{N+q_{m-2}}(a^{\prime}_{1},\ldots,a^{\prime}_{m-1}). Thus H N ​ ( a 1, …, a m) = H N ′ ​ ( a 1 ′, …, a m − 1 ′) H_{N}(a_{1},\ldots,a_{m})=H_{N^{\prime}}(a^{\prime}_{1},\ldots,a^{\prime}_{m-1}) where N ′ = N + q m − 2 N^{\prime}=N+q_{m-2}.

Suppose that 0 ≤ N < q m − 1 − 1 0\leq N<q_{m-1}-1. Then q m − 2 ′ = q m − 2 ≤ N ′ < q m − 1 + q m − 2 − 1 = q m − 1 = q m − 1 ′ − 1 q^{\prime}_{m-2}=q_{m-2}\leq N^{\prime}<q_{m-1}+q_{m-2}-1=q_{m}-1=q^{\prime}_{m-1}-1. It follows from Case (a) that B N = H N ′ ​ ( a 1 ′, …, a m − 2 ′) t B_{N}=H_{N^{\prime}}(a^{\prime}_{1},\ldots,a^{\prime}_{m-2})^{t}, with t = min ⁡ { ⌊ N ′ q m − 2 ′ ⌋, 1 + ⌊ q m − 1 ′ − 2 − N ′ q m − 2 ′ ⌋ } t=\min\{\lfloor\frac{N^{\prime}}{q^{\prime}_{m-2}}\rfloor,1+\lfloor\frac{q^{\prime}_{m-1}-2-N^{\prime}}{q^{\prime}_{m-2}}\rfloor\}. Note that we have H N ′ ​ ( a 1 ′, …, a m − 2 ′) = C N ′ ​ ( H 0 ​ ( a 1 ′, …, a m − 2 ′)) = C N + q m − 2 ​ ( H 0 ​ ( a 1, …, a m − 2)) H_{N^{\prime}}(a^{\prime}_{1},\ldots,a^{\prime}_{m-2})=C^{N^{\prime}}(H_{0}(a^{\prime}_{1},\ldots,a^{\prime}_{m-2}))=C^{N+q_{m-2}}(H_{0}(a_{1},\ldots,a_{m-2})) = C N ​ ( H 0 ​ ( a 1, …, a m − 2)) =C^{N}(H_{0}(a_{1},\ldots,a_{m-2})) (since the word is of length q m − 2 q_{m-2}) = H N ​ ( a 1, …, a m − 2) =H_{N}(a_{1},\ldots,a_{m-2}); moreover, t = min ⁡ { ⌊ N + q m − 2 q m − 2 ⌋, 1 + ⌊ q m − 1 + q m − 2 − 2 − N − q m − 2 q m − 2 ⌋ } t=\min\{\lfloor\frac{N+q_{m-2}}{q_{m-2}}\rfloor,1+\lfloor\frac{q_{m-1}+q_{m-2}-2-N-q_{m-2}}{q_{m-2}}\rfloor\}, which settles this case.

Suppose now that q m − 1 ≤ N < q m − 1 q_{m-1}\leq N<q_{m}-1. Then we have H N ​ ( a 1, …, a m) = H N ′ ​ ( a 1 ′, …, a m − 1 ′) H_{N}(a_{1},\ldots,a_{m})=H_{N^{\prime}}(a^{\prime}_{1},\ldots,a^{\prime}_{m-1}) = H N ′′ ​ ( a 1 ′, …, a m − 1 ′) =H_{N^{\prime\prime}}(a^{\prime}_{1},\ldots,a^{\prime}_{m-1}), where N ′′ = N ′ − q m = N + q m − 2 − q m = N − q m − 1 N^{\prime\prime}=N^{\prime}-q_{m}=N+q_{m-2}-q_{m}=N-q_{m-1}, since the words have length q m q_{m}. Now 0 ≤ N ′′ < q m − 2 − 1 0\leq N^{\prime\prime}<q_{m-2}-1. Hence by the first part, B N = H N ′′ ​ ( a 1 ′, …, a m − 1 ′ − 1) = C N ′′ ​ ( H 0 ​ ( a 1, …, a m − 1)) = C N ​ ( H 0 ​ ( a 1, …, a m − 1)) = H N ​ ( a 0, …, a m − 1) B_{N}=H_{N^{\prime\prime}}(a^{\prime}_{1},\ldots,a^{\prime}_{m-1}-1)=C^{N^{\prime\prime}}(H_{0}(a_{1},\ldots,a_{m-1}))=C^{N}(H_{0}(a_{1},\ldots,a_{m-1}))=H_{N}(a_{0},\ldots,a_{m-1}), since the word has length q m − 1 q_{m-1}. ∎

### 8.3 Proof of Theorem 8.1

We keep our notation and consider the word

 | V m = V m ​ ( d 1, …, d m), V_{m}=V_{m}(d_{1},\ldots,d_{m}), |  |

where

 | N = d 1 ​ q 0 + … + d m ​ q m − 1 N=d_{1}q_{0}+\ldots+d_{m}q_{m-1} |  | (16) |

is a legal representation. We keep in mind several facts:

( i) (i) If the words X, Y X,Y satisfy X ​ Y = Y ​ X XY=YX, then X X and Y Y are both integral powers of a same word.

( i ​ i) (ii) We know that V m V_{m} is a primitive word, that is, there do not exist a word Z Z and an integer ℓ ≥ 2 \ell\geq 2 such that V m = Z ℓ V_{m}=Z^{\ell}; indeed, by Lemma 7.1, this word is part of a basis of the free group, so cannot be a nontrivial power. Moreover, if there are words X, Y X,Y such that X ​ V m ​ Y = V m ​ V m XV_{m}Y=V_{m}V_{m}, then X X or Y Y is empty.

( i ​ i ​ i) (iii) Any word of the form V m u ​ V m − 1 ​ V m v V_{m}^{u}V_{m-1}V_{m}^{v} with u, v u,v nonnegative integers, is primitive. This follows for the same reason as in (ii).

( i ​ v) (iv) If the length of W W satisfies 1 ≤ | W | < | V m | 1\leq|W|<|V_{m}|, then W ​ V m WV_{m} is not a prefix of V m ​ V m V_{m}V_{m}, nor is V m ​ W V_{m}W a suffix of V m ​ V m V_{m}V_{m}.

( v) (v) The words V m ​ V m − 1 V_{m}V_{m-1} and V m − 1 ​ V m V_{m-1}V_{m} are different.

For k = 0, …, m − 1 k=0,\ldots,m-1, we let W k W_{k} (resp., X k X_{k}) denote the longest common prefix (resp., suffix) of V k + 1 ​ V k V_{k+1}V_{k} and V k ​ V k + 1 V_{k}V_{k+1}.

###### Lemma 8.6.

Put Z 1 = a ​ b Z_{1}=ab and Z − 1 = b ​ a Z_{-1}=ba. Let k = 0, …, m − 1 k=0,\ldots,m-1 be an integer. Then,

 | V k + 1 ​ V k = W k ​ Z ( − 1) k + 1 ​ X k, V k ​ V k + 1 = W k ​ Z ( − 1) k ​ X k. V_{k+1}V_{k}=W_{k}Z_{(-1)^{k+1}}X_{k},\quad V_{k}V_{k+1}=W_{k}Z_{(-1)^{k}}X_{k}. |  |

The word W k W_{k} factors as

 | W k = V k b k + 1 − d k + 1 V k − 1 b k − d k ⋯ V 0 b 1 − d 1 W_{k}=V_{k}^{b_{k+1}-d_{k+1}}V_{k-1}^{b_{k}-d_{k}}\cdots V_{0}^{b_{1}-d_{1}} |  |

and its length w k w_{k} is given by

 | w k = ∑ j = 1 k + 1 ( b j − d j) ​ q j − 1. w_{k}=\sum_{j=1}^{k+1}(b_{j}-d_{j})q_{j-1}. |  |

The word X k X_{k} factors as

 | X k = V 0 d 1 ⋯ V k − 1 d k V k d k + 1 X_{k}=V_{0}^{d_{1}}\cdots V_{k-1}^{d_{k}}V_{k}^{d_{k+1}} |  |

and its length x k x_{k} is given by

 | x k = ∑ j = 1 k + 1 d j ​ q j − 1. x_{k}=\sum_{j=1}^{k+1}d_{j}q_{j-1}. |  |

Observe that w k + x k = ∑ j = 1 k + 1 b j ​ q j − 1 = q k + 1 + q k − 2 w_{k}+x_{k}=\sum_{j=1}^{k+1}b_{j}q_{j-1}=q_{k+1}+q_{k}-2 (Lemma 10.2 (iii)).

###### Proof.

We prove the lemma by induction on k k. Recall that V − 1 = b V_{-1}=b, V 0 = a V_{0}=a, and V 1 = V 0 b 1 − d 1 ​ V − 1 ​ V 0 d 1 = a b 1 − d 1 ​ b ​ a d 1 V_{1}=V_{0}^{b_{1}-d_{1}}V_{-1}V_{0}^{d_{1}}=a^{b_{1}-d_{1}}ba^{d_{1}}. This implies that V 0 ​ V 1 = a b 1 − d 1 + 1 ​ b ​ a d 1 V_{0}V_{1}=a^{b_{1}-d_{1}+1}ba^{d_{1}} and V 1 ​ V 0 = a b 1 − d 1 ​ b ​ a d 1 + 1 V_{1}V_{0}=a^{b_{1}-d_{1}}ba^{d_{1}+1}. Thus

 | W 0 = a b 1 − d 1 = V 0 b 1 − d 1, w 0 = b 1 − d 1, X 0 = a d 1 = V 0 d 1, x 0 = d 1, W_{0}=a^{b_{1}-d_{1}}=V_{0}^{b_{1}-d_{1}},\quad w_{0}=b_{1}-d_{1},\quad X_{0}=a^{d_{1}}=V_{0}^{d_{1}},\quad x_{0}=d_{1}, |  |

and

 | V 1 ​ V 0 = W 0 ​ b ​ a ​ X 0 = W 0 ​ Z − 1 ​ X 0, V 0 ​ V 1 = W 0 ​ a ​ b ​ X 0 = W 0 ​ Z 1 ​ X 0. V_{1}V_{0}=W_{0}baX_{0}=W_{0}Z_{-1}X_{0},\quad V_{0}V_{1}=W_{0}abX_{0}=W_{0}Z_{1}X_{0}. |  |

This shows that the lemma holds for k = 0 k=0. Now let k ≥ 0 k\geq 0 be an integer with k < m − 1 k<m-1. Assume that V k + 1 ​ V k = W k ​ Z ( − 1) k + 1 ​ X k V_{k+1}V_{k}=W_{k}Z_{(-1)^{k+1}}X_{k} and V k ​ V k + 1 = W k ​ Z ( − 1) k ​ X k V_{k}V_{k+1}=W_{k}Z_{(-1)^{k}}X_{k}.

Since V k + 2 = V k + 1 b k + 2 − d k + 2 ​ V k ​ V k + 1 d k + 2 V_{k+2}=V_{k+1}^{b_{k+2}-d_{k+2}}V_{k}V_{k+1}^{d_{k+2}}, we get from our inductive assumption that

 | V k + 2 ​ V k + 1 = V k + 1 b k + 2 − d k + 2 ​ V k ​ V k + 1 ​ V k + 1 d k + 2 = V k + 1 b k + 2 − d k + 2 ​ W k ​ Z ( − 1) k ​ X k ​ V k + 1 d k + 2 V_{k+2}V_{k+1}=V_{k+1}^{b_{k+2}-d_{k+2}}V_{k}V_{k+1}V_{k+1}^{d_{k+2}}=V_{k+1}^{b_{k+2}-d_{k+2}}W_{k}Z_{(-1)^{k}}X_{k}V_{k+1}^{d_{k+2}} |  |

and

 | V k + 1 ​ V k + 2 = V k + 1 b k + 2 − d k + 2 ​ V k + 1 ​ V k ​ V k + 1 d k + 2 = V k + 1 b k + 2 − d k + 2 ​ W k ​ Z ( − 1) k + 1 ​ X k ​ V k + 1 d k + 2. V_{k+1}V_{k+2}=V_{k+1}^{b_{k+2}-d_{k+2}}V_{k+1}V_{k}V_{k+1}^{d_{k+2}}=V_{k+1}^{b_{k+2}-d_{k+2}}W_{k}Z_{(-1)^{k+1}}X_{k}V_{k+1}^{d_{k+2}}. |  |

This shows that

 | W k + 1 = V k + 1 b k + 2 − d k + 2 ​ W k, X k + 1 = X k ​ V k + 1 d k + 2. W_{k+1}=V_{k+1}^{b_{k+2}-d_{k+2}}W_{k},\quad X_{k+1}=X_{k}V_{k+1}^{d_{k+2}}. |  |

Furthermore,

 | V k + 2 ​ V k + 1 = W k + 1 ​ Z ( − 1) k ​ X k + 1 = W k + 1 ​ Z ( − 1) k + 2 ​ X k + 1 V_{k+2}V_{k+1}=W_{k+1}Z_{(-1)^{k}}X_{k+1}=W_{k+1}Z_{(-1)^{k+2}}X_{k+1} |  |

and

 | V k + 1 ​ V k + 2 = W k + 1 ​ Z ( − 1) k + 1 ​ X k + 1. V_{k+1}V_{k+2}=W_{k+1}Z_{(-1)^{k+1}}X_{k+1}. |  |

Since q j q_{j} is the length of V j V_{j}, this proves the lemma. ∎

###### Lemma 8.7.

Let k = 0, …, m − 1 k=0,\ldots,m-1 be an integer. With the above notation, the word X k ​ W k X_{k}W_{k} can be expressed as

 | X k W k = V 0 d 1 ⋯ V k − 1 d k V k b k + 1 V k − 1 b k − d k ⋯ V 0 b 1 − d 1 X_{k}W_{k}=V_{0}^{d_{1}}\cdots V_{k-1}^{d_{k}}V_{k}^{b_{k+1}}V_{k-1}^{b_{k}-d_{k}}\cdots V_{0}^{b_{1}-d_{1}} |  |

and is a palindrome. More precisely, it is the central word of the conjugation class of V k ​ V k + 1 V_{k}V_{k+1}.

###### Proof.

The expression of X k ​ W k X_{k}W_{k} is an immediate consequence of Lemma 8.6. Recall Pirillo’s theorem: if the words a ​ u ​ b, b ​ u ​ a aub,bua are conjugate, then u u is a central word ( Pirillo 1999, ( Reutenauer 2019, Theorem 15.2.5)). By Lemma 8.6, the words a ​ X k ​ W k ​ b aX_{k}W_{k}b and b ​ X k ​ W k ​ a bX_{k}W_{k}a are conjugate. This proves the lemma. ∎

Lemma 8.7 extends Lemma 7.7, which corresponds to the case d 1 = … = d k = 0 d_{1}=\ldots=d_{k}=0.

We display a consequence of Lemma 8.6.

###### Corollary 8.8.

If V k + 1 V_{k+1} is a prefix of V k ​ V k + 1 V_{k}V_{k+1}, then d k + 1 = 0 d_{k+1}=0. If V k + 1 V_{k+1} is a suffix of V k + 1 ​ V k V_{k+1}V_{k}, then d k + 1 = b k + 1 d_{k+1}=b_{k+1}.

###### Proof.

If V k + 1 V_{k+1} is a prefix of V k ​ V k + 1 V_{k}V_{k+1}, then the common prefix W k W_{k} of V k ​ V k + 1 V_{k}V_{k+1} and V k + 1 ​ V k V_{k+1}V_{k} is of length w k ≥ q k + 1 w_{k}\geq q_{k+1}; since w k + x k = q k + 1 + q k − 2 w_{k}+x_{k}=q_{k+1}+q_{k}-2, we obtain x k ≤ q k − 2 x_{k}\leq q_{k}-2. By Lemma 8.6 this implies that d k + 1 = 0 d_{k+1}=0. Similarly, if V k + 1 V_{k+1} is a suffix of V k + 1 ​ V k V_{k+1}V_{k}, then w k ≤ q k − 2 w_{k}\leq q_{k}-2 and b k + 1 − d k + 1 = 0 b_{k+1}-d_{k+1}=0. ∎

Recall that alternating sequences have been defined in Section 3.

###### Corollary 8.9.

Suppose that the representation ( 16) is greedy. The word V m − 1 ​ ( d 1, …, d m − 1) V_{m-1}(d_{1},\ldots,d_{m-1}) is a prefix of V m ​ ( d 1, …, d m) V_{m}(d_{1},\ldots,d_{m}) if and only if V m ​ ( d 1, …, d m) V_{m}(d_{1},\ldots,d_{m}) is not the Christoffel word V m ​ ( …, 0, b m − 2, 0, b m) V_{m}(\ldots,0,b_{m-2},0,b_{m}).

###### Proof.

Observe that V m − 1 V_{m-1} is a prefix of V m V_{m} if and only if the common prefix W m − 1 W_{m-1} of V m ​ V m − 1 V_{m}V_{m-1} and V m − 1 ​ V m V_{m-1}V_{m} has length at least q m − 1 q_{m-1}. In view of Lemma 8.6, this common prefix has length

 | w m − 1 = ∑ j = 1 m ( b j − d j) ​ q j − 1. w_{m-1}=\sum_{j=1}^{m}(b_{j}-d_{j})q_{j-1}. |  |

The lemma then follows from Lemma 3.2 and Corollary 7.4. ∎

###### Corollary 8.10.

Suppose that the representation ( 16) is greedy. The word V m − 1 V_{m-1} is not a prefix of the word V m − 2 ​ V m − 1 V_{m-2}V_{m-1} if and only if d m − 1 = 0 d_{m-1}=0 and the sequence d 1, …, d m − 1 d_{1},\ldots,d_{m-1} is alternating.

###### Proof.

We apply Corollary 8.9 to the sequence a 1, …, a m − 1, 1 a_{1},\ldots,a_{m-1},1 and the words V m − 1 ​ ( d 1, …, d m − 1) V_{m-1}(d_{1},\ldots,d_{m-1}) and V m ′ = V m ​ ( d 1, …, d m − 1, 1) V^{\prime}_{m}=V_{m}(d_{1},\ldots,d_{m-1},1), so that V m ′ = V m − 2 ​ V m − 1 V^{\prime}_{m}=V_{m-2}V_{m-1}: thus the word V m − 1 V_{m-1} is a prefix of V m − 2 ​ V m − 1 V_{m-2}V_{m-1} if and only if V m ′ V^{\prime}_{m} is not a Christoffel word; but, by Corollary 7.4, V m ′ V^{\prime}_{m} is a Christoffel word if and only if the sequence d 1, …, d m − 1, 1 d_{1},\ldots,d_{m-1},1 is alternating; this means that d m − 1 = 0 d_{m-1}=0 and the sequence d 1, …, d m − 1 d_{1},\ldots,d_{m-1} is alternating. ∎

Let us state several result on borders.

###### Lemma 8.11.

Let i ≥ 2 i\geq 2, Y Y be a primitive word and X X a prefix of Y Y. Then the longest border B B of Y i ​ X Y^{i}X is Y i − 1 ​ X Y^{i-1}X.

Recall that an internal factor of a word means a factor that is not a prefix nor a suffix.

###### Proof.

The word Y i − 1 ​ X Y^{i-1}X is a border of Y i ​ X Y^{i}X. Suppose that B B is longer. It begins by Y i − 1 ​ X Y^{i-1}X, hence by Y Y since i ≥ 2 i\geq 2: B = Y ​ B ′ B=YB^{\prime}. Moreover, Y i ​ X = U ​ B Y^{i}X=UB, where the length of U U satisfies 0 < | U | < | Y | 0<|U|<|Y|. Thus Y i ​ X = U ​ Y ​ B ′ Y^{i}X=UYB^{\prime} and we see that Y Y is an internal factor of Y ​ Y YY, a contradiction. ∎

Observe that a border of a border of a word W W is a border of W W: the borders of W W are totally ordered by the relation “being a border”.

###### Lemma 8.12.

Let W W be a finite word and V V be its longest border.

(i) The borders of W W are precisely V V and its borders.

(ii) If V = U ℓ ​ Z V=U^{\ell}Z with U U primitive, ℓ ≥ 1 \ell\geq 1, and Z Z a proper, possibly empty, prefix of U U, then the borders of W W are V = U ℓ ​ Z, U ℓ − 1 ​ Z, …, U ​ Z V=U^{\ell}Z,U^{\ell-1}Z,\ldots,UZ and the borders of U ​ Z UZ.

###### Proof.

(i) Let X X be a border of W W with X ≠ V X\not=V. Then X X is a prefix and a suffix of W W, hence, being shorter than V V, also a prefix and a suffix of V V. Consequently, X X is a border of V V. The converse follows from the observation before the lemma.

(ii) Follows from (i) and Lemma 8.11. ∎

Remark. Observe that if U ​ U UU is a border of W W and V V a border of U U, then U ​ V UV is not necessarily a border of W W. A counterexample is given by a ​ b ​ a ​ a ​ b ​ a ​ b ​ b ​ a ​ b ​ a ​ a ​ b ​ a abaababbabaaba, with U = a ​ b ​ a U=aba and V = a V=a.

In the following lemmas, we consider the legal representation ( 16) and put V m = V m ​ ( d 1, …, d m) V_{m}=V_{m}(d_{1},\ldots,d_{m}), V m − 1 = V m − 1 ​ ( d 1, …, d m − 1) V_{m-1}=V_{m-1}(d_{1},\ldots,d_{m-1}), and V m − 2 = V m − 2 ​ ( d 1, …, d m − 2) V_{m-2}=V_{m-2}(d_{1},\ldots,d_{m-2}).

###### Lemma 8.13.

The word V m V_{m} is neither an internal factor of V m ​ V m − 1 V_{m}V_{m-1}, nor of V m − 1 ​ V m V_{m-1}V_{m}.

###### Proof.

We may assume that m ≥ 2 m\geq 2. Suppose that V m V_{m} is an internal factor of V m ​ V m − 1 V_{m}V_{m-1}. Then V m ​ V m − 1 = X ​ V m ​ Y V_{m}V_{m-1}=XV_{m}Y, with X X and Y Y nonempty. Since V m − 1 V_{m-1} is shorter than V m V_{m}, there exist a suffix W W of V m V_{m} and a prefix Z Z of V m − 1 V_{m-1} such that V m = X ​ W = W ​ Z V_{m}=XW=WZ. Note that | X | = | Z | |X|=|Z|. Since V m V_{m} is primitive, it is not equal to one of its conjugates, thus the words X X and Z Z are different; moreover, X X is a prefix of V m V_{m} and Z Z is a prefix of V m − 1 V_{m-1}; since they have the same positive length and are different, V m − 1 V_{m-1} is not a prefix of V m V_{m}. Consequently, we have V m = V m − 2 ​ V m − 1 b m V_{m}=V_{m-2}V_{m-1}^{b_{m}}, V m − 2 ​ V m − 1 b m + 1 = V m ​ V m − 1 = X ​ V m ​ Y = X ​ V m − 2 ​ V m − 1 b m ​ Y V_{m-2}V_{m-1}^{b_{m}+1}=V_{m}V_{m-1}=XV_{m}Y=XV_{m-2}V_{m-1}^{b_{m}}Y. Since b m ≥ 1 b_{m}\geq 1 and Y Y is shorter than V m − 1 V_{m-1} (because V m ​ V m − 1 = X ​ V m ​ Y V_{m}V_{m-1}=XV_{m}Y, hence | X | + | Y | = | V m − 1 | |X|+|Y|=|V_{m-1}| and X X nonempty), V m − 1 ​ Y V_{m-1}Y is a suffix of V m − 1 ​ V m − 1 V_{m-1}V_{m-1}. Since Y Y is nonempty, V m − 1 V_{m-1} is an internal factor of V m − 1 ​ V m − 1 V_{m-1}V_{m-1}. This contradicts the primitivity of V m − 1 V_{m-1}.

The proof for V m − 1 ​ V m V_{m-1}V_{m} is similar and we omit it. ∎

###### Lemma 8.14.

Assume that m ≥ 1 m\geq 1. Let u, v u,v be positive integers and set V = V m u ​ V m − 1 ​ V m v V=V_{m}^{u}V_{m-1}V_{m}^{v}. There is no other occurrence of V m V_{m} in V V, except possibly, one starting by V m − 1 V_{m-1} (case L) and one ending by V m − 1 V_{m-1} (case R). Case L occurs if and only V m V_{m} is a prefix of V m − 1 ​ V m V_{m-1}V_{m}, and then d m = 0 d_{m}=0. Case R occurs if and only if V m V_{m} is a suffix of V m ​ V m − 1 V_{m}V_{m-1}, and then d m = b m d_{m}=b_{m}.

###### Proof.

A) Consider an occurrence of V m V_{m} in V V. By the primitivity of V m V_{m} and Lemma 8.13, suppose by contradiction that there exist nonempty words X, Y X,Y such that V m = X ​ V m − 1 ​ Y V_{m}=XV_{m-1}Y, where V m − 1 V_{m-1} is the factor appearing in the indicated factorization of V V, X X is a suffix of V m V_{m} and Y Y a prefix of V m V_{m}.

1. Assume first that 1 ≤ d m ≤ b m − 1 1\leq d_{m}\leq b_{m}-1. Thus by ( 15), the word V m − 1 V_{m-1} is a prefix and a suffix of V m V_{m}. We show that either X X is an integer power of V m − 1 V_{m-1}, or Y Y is an integer power of V m − 1 V_{m-1}. Indeed, if | X | < | V m − 1 | |X|<|V_{m-1}|, then X X is a nontrivial proper suffix of V m − 1 V_{m-1}, V m − 1 = U ​ X V_{m-1}=UX, where U U is nonempty, and V m V_{m} begins with X ​ V m − 1 XV_{m-1}; but V m V_{m} also begins with V m − 1 V_{m-1}, V m = V m − 1 ​ W V_{m}=V_{m-1}W, hence U ​ V m − 1 ​ W = U ​ V m = U ​ X ​ V m − 1 ​ Y = V m − 1 ​ V m − 1 ​ Y UV_{m-1}W=UV_{m}=UXV_{m-1}Y=V_{m-1}V_{m-1}Y; since U U is nonempty and shorter than V m − 1 V_{m-1}, we see that V m − 1 V_{m-1} is a proper factor of V m − 1 2 V_{m-1}^{2}, and we have a contradiction with the primitivity of V m − 1 V_{m-1}.

Consequently, | X | ≥ V m − 1 |X|\geq V_{m-1}, and therefore X = X ′ ​ V m − 1 X=X^{\prime}V_{m-1} (since X X and V m − 1 V_{m-1} are both suffixes of V m V_{m}). A symmetric argument shows that Y = V m − 1 ​ Y ′ Y=V_{m-1}Y^{\prime}. Thus, V m = X ′ ​ V m − 1 3 ​ Y ′ V_{m}=X^{\prime}V_{m-1}^{3}Y^{\prime}. Since V m = V m − 1 b m − d m ​ V m − 2 ​ V m − 1 d m V_{m}=V_{m-1}^{b_{m}-d_{m}}V_{m-2}V_{m-1}^{d_{m}}, | V m − 2 | ≤ | V m − 1 | |V_{m-2}|\leq|V_{m-1}|, and V m − 2 ≠ V m − 1 V_{m-2}\neq V_{m-1}, we see that V m − 1 V_{m-1} is an internal factor of V m − 1 2 V_{m-1}^{2}, a contradiction with the primitivity of V m − 1 V_{m-1}. Hence, X ′ X^{\prime} or Y ′ Y^{\prime} is an integer power of V m − 1 V_{m-1}.

Assume that X = V m − 1 z X=V_{m-1}^{z}, for some positive integer z z, the other case being similar. We have two cases, depending on the relative values of z z and b m − d m b_{m}-d_{m}. In both cases, we claim that V m − 2 ​ V m − 1 V_{m-2}V_{m-1} is a prefix of V m − 1 2 V_{m-1}^{2}, a contradiction with the primitivity of V m − 1 V_{m-1}, since V m − 2 V_{m-2} is not longer than V m − 1 V_{m-1} and V m − 1 ≠ V m − 2 V_{m-1}\neq V_{m-2}. For the claim, we have indeed V m = X ​ V m − 1 ​ Y = V m − 1 z + 2 ​ Y ′ V_{m}=XV_{m-1}Y=V_{m-1}^{z+2}Y^{\prime} and V m = V m − 1 b m − d m ​ V m − 2 ​ V m − 1 d m V_{m}=V_{m-1}^{b_{m}-d_{m}}V_{m-2}V_{m-1}^{d_{m}}. If b m − d m ≤ z b_{m}-d_{m}\leq z, then z = b m − d m + h z=b_{m}-d_{m}+h, h ≥ 0 h\geq 0, thus V m − 1 h + 2 ​ Y ′ = V m − 2 ​ V m − 1 d m V_{m-1}^{h+2}Y^{\prime}=V_{m-2}V_{m-1}^{d_{m}}, which proves the claim in this case, since d m ≥ 1 d_{m}\geq 1. If b m − d m > z b_{m}-d_{m}>z, then b m − d m = z + h + 1 b_{m}-d_{m}=z+h+1, h ≥ 0 h\geq 0, and V m − 1 2 ​ Y ′ = V m − 1 h + 1 ​ V m − 2 ​ V m − 1 d m V_{m-1}^{2}Y^{\prime}=V_{m-1}^{h+1}V_{m-2}V_{m-1}^{d_{m}}, thus Y = V m − 1 ​ Y ′ = V m − 1 h ​ V m − 2 ​ V m − 1 d m Y=V_{m-1}Y^{\prime}=V_{m-1}^{h}V_{m-2}V_{m-1}^{d_{m}}; now Y Y is a prefix of V m V_{m}, V m = Y ​ W V_{m}=YW, hence V m − 1 h ​ V m − 2 ​ V m − 1 d m ​ W = V m = V m − 1 z + h + 1 ​ V m − 2 ​ V m − 1 d m V_{m-1}^{h}V_{m-2}V_{m-1}^{d_{m}}W=V_{m}=V_{m-1}^{z+h+1}V_{m-2}V_{m-1}^{d_{m}}, thus V m − 2 ​ V m − 1 d m ​ W = V m − 1 z + 1 ​ V m − 2 ​ V m − 1 d m V_{m-2}V_{m-1}^{d_{m}}W=V_{m-1}^{z+1}V_{m-2}V_{m-1}^{d_{m}}, which proves the claim, since z, d m ≥ 1 z,d_{m}\geq 1.

2. Assume now that d m = 0 d_{m}=0, hence V m = V m − 1 b m ​ V m − 2 V_{m}=V_{m-1}^{b_{m}}V_{m-2}. Since V m = X ​ V m − 1 ​ Y V_{m}=XV_{m-1}Y, we see that: either Y Y is shorter than V m − 2 V_{m-2} and then V m − 1 V_{m-1} is an internal factor of V m − 1 ​ V m − 2 V_{m-1}V_{m-2}, contradicting Lemma 8.13; or the length of Y Y is larger than that of V m − 2 V_{m-2}, and noncongruent to it modulo | V m − 1 | |V_{m-1}|, and then V m − 1 V_{m-1} is an internal factor of V m − 1 2 V_{m-1}^{2}, contradicting the primitivity of V m − 1 V_{m-1}; or the length of Y Y is congruent to | V m − 2 | |V_{m-2}| modulo | V m − 1 | |V_{m-1}|, and then X X is an integral power of V m − 1 V_{m-1}.

Precisely, there are integers r, s r,s such that r + s + 1 = b m r+s+1=b_{m}, X = V m − 1 r X=V_{m-1}^{r} and Y = V m − 1 s ​ V m − 2 Y=V_{m-1}^{s}V_{m-2}. If r ≥ 2 r\geq 2, then V m − 1 ​ V m − 1 V_{m-1}V_{m-1} and V m − 1 ​ V m − 2 V_{m-1}V_{m-2} are suffixes of V m V_{m}, a contradiction with the primitivity of V m − 1 V_{m-1}. Thus, we have r = 1 r=1 and V m − 2 V_{m-2} is a prefix of V m − 1 V_{m-1} (since Y Y, of length at most equal to ( s + 1) ​ | V m − 1 | (s+1)|V_{m-1}|, is a prefix of V m = V m − 1 r + s + 1 ​ V m − 2 V_{m}=V_{m-1}^{r+s+1}V_{m-2}, hence of V m − 1 r + 1 + s V_{m-1}^{r+1+s}). Observe that X = V m − 1 X=V_{m-1} and V m − 1 ​ V m − 2 V_{m-1}V_{m-2} are suffixes of V m V_{m}. Since V m − 2 V_{m-2} is a prefix of V m − 1 V_{m-1}, we get V m − 1 ​ V m − 2 = V m − 2 ​ V m − 1 V_{m-1}V_{m-2}=V_{m-2}V_{m-1}, a contradiction.

3. The case d m = b m d_{m}=b_{m} is similar to the case d m = 0 d_{m}=0 and we omit it.

B) Suppose now that there is an occurrence of V m V_{m} starting at V m − 1 V_{m-1}. This means that V m V_{m} is a prefix of V m − 1 ​ V m V_{m-1}V_{m}. Then d m = 0 d_{m}=0 by Corollary 8.8.

Suppose now that there is an occurrence of V m V_{m} ending at V m − 1 V_{m-1}; this is equivalent to the fact that V m V_{m} is a suffix of V m ​ V m − 1 V_{m}V_{m-1}. Then, similarly, we must have d m = b m d_{m}=b_{m}. ∎

###### Lemma 8.15.

Let i, j i,j be positive integers, and X, Y X,Y be nonempty words such that X X is shorter than Y Y, Y Y is primitive, and X ​ Y ≠ Y ​ X XY\neq YX. Suppose further that in the word W = Y i ​ X ​ Y j W=Y^{i}XY^{j} there are at most i + j + 2 i+j+2 occurrences of the factor Y Y, namely the i + j i+j ones coming from the indicated factorization of W W, and at most two others, beginning or ending by the X X indicated in the factorization (we denote these two cases respectively by L and R). Let ℓ = min ⁡ { i, j } \ell=\min\{i,j\}. Then the longest border B B of W W is Y ℓ + 1 Y^{\ell+1} if either i < j i<j and case L occurs, or i > j i>j and case R occurs. In all other cases, B = Y ℓ B=Y^{\ell}.

Note that the cases L and R match with those of Lemma 8.14.

###### Proof.

1. Suppose by contradiction that B = Y i ​ X ​ Y r B=Y^{i}XY^{r}, with 0 ≤ r ≤ j 0\leq r\leq j. Then r < j r<j since B ≠ W B\neq W. Moreover Y i ​ X ​ Y j − r ​ Y r = W = U ​ B = U ​ Y i − 1 ​ Y ​ X ​ Y r Y^{i}XY^{j-r}Y^{r}=W=UB=UY^{i-1}YXY^{r}, hence Y i ​ X ​ Y j − r = U ​ Y i − 1 ​ Y ​ X Y^{i}XY^{j-r}=UY^{i-1}YX; if j − r = 1 j-r=1, then X ​ Y = Y ​ X XY=YX, a contradiction; thus j − r ≥ 2 j-r\geq 2 and, since X X is shorter than Y Y, we see that Y Y is an internal factor of Y ​ Y YY, which contradicts the primitivity of Y Y.

We deduce that B ≠ Y i ​ X ​ Y r B\neq Y^{i}XY^{r}, when 0 ≤ r ≤ j 0\leq r\leq j, and by symmetry, B ≠ Y r ​ X ​ Y j B\neq Y^{r}XY^{j}, when 0 ≤ r ≤ i 0\leq r\leq i.

2. We show that cases L and R cannot occur simultaneously. Indeed, if they occur together then, since X X is nonempty and shorter than Y Y, the factor Y Y beginning at X X is an internal factor of Y ​ Y YY, product of the factor Y Y ending at X X and of the first factor Y Y of Y j Y^{j}; this contradicts the primitivity of Y Y.

3. By symmetry, we may assume that i ≤ j i\leq j. Then ℓ = i \ell=i. Clearly, Y i Y^{i} is a border.

Suppose that B B is longer; then B B extends Y i Y^{i} to the left, hence B B ends by Y Y, since i ≥ 1 i\geq 1; moreover, we may extend the prefix Y i Y^{i} of W W to the longer prefix B B, and since B B ends by Y Y, by 1. this Y Y is the factor Y Y of W W starting at X X, and we are in case L; thus, since B B ends by Y Y, by 1. and by the hypothesis on the locations of the factors Y Y in W W, B = Y i + 1 B=Y^{i+1}. But B B is also a right factor of W W, hence we must have j > i j>i, otherwise there is a factor Y Y ending at X X, which is excluded by 2. ∎

###### Lemma 8.16.

Let j ≥ 1 j\geq 1, Y Y be a primitive word, and X X a nonempty word, shorter that Y Y, such that Y Y is a prefix of X ​ Y j XY^{j}, and that Y Y is not an internal factor of X ​ Y XY. Then the longest border B B of X ​ Y j XY^{j} is Y Y.

###### Proof.

We may write B = Y ​ U ​ Z B=YUZ, where the length of U U is a multiple of that of Y Y, and | Z | < | Y | |Z|<|Y|; assume by contradiction that Z Z is nonempty.

Then, since B B is a suffix of X ​ Y j XY^{j}, we have X ​ Y j = W ​ Y ~ ​ U ​ Z XY^{j}=W{\widetilde{Y}}UZ; then we see that that either Y ~ \widetilde{Y} is an internal factor of X ​ Y XY (a contradiction with the hypothesis), or Y ~ \widetilde{Y} is an internal factor of Y ​ Y YY (which contradicts the fact that Y Y is primitive). Thus Z Z must be empty.

It follows that B = Y ​ U B=YU, hence B = Y h B=Y^{h}, since B B is a suffix of X ​ Y j XY^{j}. If we have h ≥ 2 h\geq 2, then j ≥ 2 j\geq 2, and since B B is a prefix of X ​ Y j XY^{j}, and X X is nonempty and shorter that Y Y, we see that Y Y is an internal factor of Y ​ Y YY, a contradiction again. Thus h = 1 h=1. ∎

###### Lemma 8.17.

If m ≥ 2 m\geq 2, d m = 0 d_{m}=0 and V m − 1 V_{m-1} is a suffix of V m V_{m}, then d m − 1 = b m − 1 d_{m-1}=b_{m-1}.

###### Proof.

We have by ( 11)

 | V m = V m − 1 b m ​ V m − 2. V_{m}=V_{m-1}^{b_{m}}V_{m-2}. |  |

Suppose that m = 2 m=2. Then V − 1 = b, V 0 = a, V 1 = a b 1 − d 1 ​ b ​ a d 1 V_{-1}=b,V_{0}=a,V_{1}=a^{b_{1}-d_{1}}ba^{d_{1}}, V 2 = V 1 b 2 ​ a V_{2}=V_{1}^{b_{2}}a, so that V 2 V_{2} ends with a b 1 − d 1 ​ b ​ a d 1 ​ a a^{b_{1}-d_{1}}ba^{d_{1}}a; thus V 1 V_{1} is not suffix of V 2 V_{2}.

Therefore m ≥ 3 m\geq 3. Note that, since V m − 1 V_{m-1} and V m − 2 V_{m-2} are both suffixes of the same word V m V_{m}, the word V m − 2 V_{m-2} is a suffix of V m − 1 V_{m-1}. Let V m − 2 h V_{m-2}^{h} be suffix of V m − 1 V_{m-1}, with h h maximal; then h ≥ 1 h\geq 1 and V m − 2 h + 1 V_{m-2}^{h+1} is a suffix of V m V_{m}, since b m ≥ 1 b_{m}\geq 1 because m ≥ 2 m\geq 2. We show that | V m − 2 h + 1 | > | V m − 1 | |V_{m-2}^{h+1}|>|V_{m-1}|. Indeed, otherwise V m − 2 h + 1 V_{m-2}^{h+1} is not longer than V m − 1 V_{m-1}, and since both V m − 2 h + 1 V_{m-2}^{h+1} and V m − 1 V_{m-1} are suffixes of the same word V m V_{m}, the word V m − 2 h + 1 V_{m-2}^{h+1} is a suffix of V m − 1 V_{m-1}, contradicting the maximality of h h. We thus deduce that V m − 1 = U ​ V m − 2 h V_{m-1}=UV_{m-2}^{h}, where U U is shorter than V m − 2 V_{m-2}.

Recall that V m − 1 = V m − 2 b m − 1 − d m − 1 ​ V m − 3 ​ V m − 2 d m − 1 V_{m-1}=V_{m-2}^{b_{m-1}-d_{m-1}}V_{m-3}V_{m-2}^{d_{m-1}}. If b m − 1 − d m − 1 ≥ 2 b_{m-1}-d_{m-1}\geq 2 then, since U ​ V m − 2 UV_{m-2} is a prefix of V m − 1 V_{m-1}, it is a prefix of V m − 2 ​ V m − 2 V_{m-2}V_{m-2}, a contradiction with the primitivity of V m − 2 V_{m-2} ( U U is nonempty, otherwise either V m − 1 V_{m-1} is not primitive, or V m − 1 = V m − 2 V_{m-1}=V_{m-2}, a contradiction in both cases). Therefore we have b m − 1 − d m − 1 = 1 b_{m-1}-d_{m-1}=1, hence V m − 1 = V m − 2 ​ V m − 3 ​ V m − 2 b m − 1 − 1 V_{m-1}=V_{m-2}V_{m-3}V_{m-2}^{b_{m-1}-1}. Then,

 | V m = V m − 1 b m ​ V m − 2 = ( V m − 2 ​ V m − 3 ​ V m − 2 b m − 1 − 1) b m ​ V m − 2 = V m − 2 ​ ( V m − 3 ​ V m − 2 b m − 1) b m, V_{m}=V_{m-1}^{b_{m}}V_{m-2}=(V_{m-2}V_{m-3}V_{m-2}^{b_{m-1}-1})^{b_{m}}V_{m-2}=V_{m-2}(V_{m-3}V_{m-2}^{b_{m-1}})^{b_{m}}, |  |

and, as V m − 1 V_{m-1} is a suffix of V m V_{m}, we get, by comparing suffixes of the same length, the equality V m − 1 = V m − 3 ​ V m − 2 b m − 1 V_{m-1}=V_{m-3}V_{m-2}^{b_{m-1}}. Since also V m − 1 = V m − 2 ​ V m − 3 ​ V m − 2 b m − 1 − 1 V_{m-1}=V_{m-2}V_{m-3}V_{m-2}^{b_{m-1}-1}, we deduce that V m − 3 ​ V m − 2 = V m − 2 ​ V m − 3 V_{m-3}V_{m-2}=V_{m-2}V_{m-3}, a contradiction. Thus b m − 1 − d m − 1 = 0 b_{m-1}-d_{m-1}=0.

∎

###### Lemma 8.18.

Suppose that the representation ( 16) is greedy. If d m = b m d_{m}=b_{m}, then V m V_{m} is not a suffix of V m ​ V m − 1 V_{m}V_{m-1}.

###### Proof.

We have d m − 1 = 0 d_{m-1}=0. Suppose that the lemma is false. We show first that V m V_{m} is a Christoffel word. It is enough to prove that the d i d_{i} are alternatively b i b_{i} and 0 (Corollary 7.4). Since V m = V m − 2 ​ V m − 1 b m V_{m}=V_{m-2}V_{m-1}^{b_{m}} is a suffix of V m ​ V m − 1 = V m − 2 ​ V m − 1 b m + 1 V_{m}V_{m-1}=V_{m-2}V_{m-1}^{b_{m}+1}, the word V m − 2 V_{m-2} is a suffix of V m − 1 V_{m-1}. Note that for m = 1 m=1, this cannot be true, and neither for m = 2 m=2, since V 1 = a b 1 ​ b V_{1}=a^{b_{1}}b, V 0 = a V_{0}=a; hence we must have m ≥ 3 m\geq 3. Since d m − 1 = 0 d_{m-1}=0, we deduce from Lemma 8.17, applied to m − 1 m-1, that d m − 2 = b m − 2 d_{m-2}=b_{m-2}.

Moreover, since V m − 1 = V m − 2 b m − 1 ​ V m − 3 V_{m-1}=V_{m-2}^{b_{m-1}}V_{m-3} and V m − 2 V_{m-2} is a suffix of V m − 1 V_{m-1}, V m − 2 V_{m-2} is a suffix of V m − 2 ​ V m − 3 V_{m-2}V_{m-3}.

We thus obtain that V m − 2 V_{m-2} is a suffix of V m − 2 ​ V m − 3 V_{m-2}V_{m-3} and that d m − 2 = b m − 2 d_{m-2}=b_{m-2}. Continuing like this, we infer that V m V_{m} is the Christoffel word V m ​ ( …, 0, b m) V_{m}(\ldots,0,b_{m}).

To conclude, note that V m − 2 V_{m-2} is a prefix and a suffix of V m V_{m}, contradicting the fact that a Christoffel word has no border. ∎

Now we are armed to prove Theorem 8.1.

###### of Theorem 8.1.

( i) (i) If d m = b m d_{m}=b_{m}, then d m − 1 = 0 d_{m-1}=0 and we have

 | V m = V m − 2 ​ V m − 1 b m, V m − 1 = V m − 2 b m − 1 ​ V m − 3. V_{m}=V_{m-2}V_{m-1}^{b_{m}},\quad V_{m-1}=V_{m-2}^{b_{m-1}}V_{m-3}. |  |

Observe that V m − 1 = V m − 2 b m − 1 ​ V m − 3 V_{m-1}=V_{m-2}^{b_{m-1}}V_{m-3} is a prefix of V m = V m − 2 V m − 2 b m − 1 V m − 3 ⋯ V_{m}=V_{m-2}V_{m-2}^{b_{m-1}}V_{m-3}\cdots if and only if V m − 3 V_{m-3} is a prefix of V m − 2 V_{m-2}, thus, by Corollary 8.9, if and only if V m − 2 V_{m-2} is not the Christoffel word V m − 2 ​ ( …, 0, b m − 2) V_{m-2}(\ldots,0,b_{m-2}). But V m − 2 V_{m-2} cannot be equal to the latter word, since V m V_{m} is by assumption not a Christoffel word, and d m = b m, d m − 1 = 0 d_{m}=b_{m},d_{m-1}=0. Thus V m − 1 V_{m-1} is a prefix of V m V_{m}, and B = V m − 1 B=V_{m-1} by Lemmas 8.13 (applied to m − 1 m-1) and 8.16.

( i ​ i) (ii) Suppose that 1 ≤ d m ≤ b m − 1 1\leq d_{m}\leq b_{m}-1 and 1 ≤ d m − 1 ≤ b m − 1 − 1 1\leq d_{m-1}\leq b_{m-1}-1. There are no other occurrences of V m − 1 V_{m-1} in V m V_{m} than those seen in the factorization V m = V m − 1 b m − d m ​ V m − 2 ​ V m − 1 d m V_{m}=V_{m-1}^{b_{m}-d_{m}}V_{m-2}V_{m-1}^{d_{m}}; indeed, this follows from Lemma 8.14 (applied to m − 1 m-1), and our assumption on d m − 1 d_{m-1}. Consequently, by Lemma 8.15, B = V m − 1 ℓ B=V_{m-1}^{\ell}.

( i ​ i ​ i) (iii) If 1 ≤ d m ≤ b m − 1 1\leq d_{m}\leq b_{m}-1 and d m − 1 = 0 d_{m-1}=0, then V m − 1 = V m − 2 b m − 1 ​ V m − 3 V_{m-1}=V_{m-2}^{b_{m-1}}V_{m-3}. By Lemma 8.14 (applied to m − 1 m-1), and the hypothesis d m − 1 = 0 d_{m-1}=0, any occurrence of V m − 1 V_{m-1} in V m V_{m} can be read on the factorisation V m = V m − 1 b m − d m ​ V m − 2 ​ V m − 1 d m V_{m}=V_{m-1}^{b_{m}-d_{m}}V_{m-2}V_{m-1}^{d_{m}}, or it begins by V m − 2 V_{m-2}. It follows from Lemma 8.15 that B = V m − 1 ℓ + 1 B=V_{m-1}^{\ell+1} if V m − 1 V_{m-1} is a prefix of V m − 2 ​ V m − 1 V_{m-2}V_{m-1} and b m − d m < d m b_{m}-d_{m}<d_{m}, and otherwise B = V m − 1 ℓ B=V_{m-1}^{\ell}.

By Corollary 8.10, since d m − 1 = 0 d_{m-1}=0, V m − 1 V_{m-1} is a prefix of V m − 2 ​ V m − 1 V_{m-2}V_{m-1} if and only if the sequence d 1, …, d m − 1 d_{1},\ldots,d_{m-1} is not alternating.

( i ​ v) (iv) Suppose that 1 ≤ d m ≤ b m − 1 1\leq d_{m}\leq b_{m}-1 and d m − 1 = b m − 1 d_{m-1}=b_{m-1}. Then V m − 1 = V m − 3 ​ V m − 2 b m − 1 V_{m-1}=V_{m-3}V_{m-2}^{b_{m-1}}.

We claim that there are no other occurrences of V m − 1 V_{m-1} in V m V_{m} than those given by the factorization V m = V m − 1 b m − d m ​ V m − 2 ​ V m − 1 d m V_{m}=V_{m-1}^{b_{m}-d_{m}}V_{m-2}V_{m-1}^{d_{m}}. The claim is proved below. It follows from the claim and from Lemma 8.15 that B = V m − 1 ℓ B=V_{m-1}^{\ell}.

By Lemma 8.14, to prove the claim, it is enough to show that V m − 1 V_{m-1} is not a prefix of V m − 2 ​ V m − 1 V_{m-2}V_{m-1}, nor a suffix of V m − 1 ​ V m − 2 V_{m-1}V_{m-2}.

This is immediate if m = 2 m=2 and b 1 ≥ 1 b_{1}\geq 1, since we then get V 0 = a V_{0}=a and V 1 = b ​ a b 1 V_{1}=ba^{b_{1}}. Thus, we assume m ≥ 3 m\geq 3.

By contradiction, suppose first that V m − 1 V_{m-1} is a prefix of V m − 2 ​ V m − 1 V_{m-2}V_{m-1}. Since V m − 2 V_{m-2} is a suffix of V m − 1 V_{m-1}, V m − 1 ​ V m − 2 V_{m-1}V_{m-2} is equal to V m − 2 ​ V m − 1 V_{m-2}V_{m-1}, a contradiction.

Supppose now that V m − 1 V_{m-1} is a suffix of V m − 1 ​ V m − 2 V_{m-1}V_{m-2}. This contradicts Lemma 8.18, applied to m − 1 m-1, since d m − 2 = 0 d_{m-2}=0 by greedyness.

( v) (v) If d m = 0 d_{m}=0, then we have

 | V m = V m − 1 b m ​ V m − 2, V_{m}=V_{m-1}^{b_{m}}V_{m-2}, |  |

and, by Corollary 8.9, either V m − 1 V_{m-1} is the Christoffel word V m − 1 ​ ( …, b m − 3, 0, b m − 1) V_{m-1}(\ldots,b_{m-3},0,b_{m-1}), or V m − 2 V_{m-2} is a prefix of V m − 1 V_{m-1}. The former case is excluded, since V m V_{m} would be a Christoffel word. In the latter case, V m − 1 b m − 1 ​ V m − 2 V_{m-1}^{b_{m}-1}V_{m-2} is a border of V m V_{m}, and since b m ≥ 2 b_{m}\geq 2, by Lemma 8.11, B = V m − 1 b m − 1 ​ V m − 2 B=V_{m-1}^{b_{m}-1}V_{m-2}.

( v ​ i) (vi) We suppose from now on that d m = 0 d_{m}=0 and b m = 1 b_{m}=1. Then

 | V m = V m − 1 ​ V m − 2 = V m − 2 b m − 1 − d m − 1 ​ V m − 3 ​ V m − 2 d m − 1 + 1 V_{m}=V_{m-1}V_{m-2}=V_{m-2}^{b_{m-1}-d_{m-1}}V_{m-3}V_{m-2}^{d_{m-1}+1} |  |

and there are several cases to distinguish.

If m = 2 m=2 and b 1 ≥ 1 b_{1}\geq 1, then V 2 = a b 1 − d 1 ​ b ​ a b 1 + 1 V_{2}=a^{b_{1}-d_{1}}ba^{b_{1}+1} and B = a h = V m − 2 h B=a^{h}=V_{m-2}^{h}. Assume that m ≥ 3 m\geq 3.

If b m − 1 − d m − 1 ≥ 1 b_{m-1}-d_{m-1}\geq 1 and 1 ≤ d m − 2 ≤ b m − 2 − 1 1\leq d_{m-2}\leq b_{m-2}-1, then it follows from Lemma 8.14 (applied to m − 2 m-2) and the hypothesis on d m − 2 d_{m-2}, that there are no further occurrences of V m − 2 V_{m-2} in V m V_{m}. Thus B = V m − 2 h B=V_{m-2}^{h} by Lemma 8.15.

If b m − 1 − d m − 1 ≥ 1 b_{m-1}-d_{m-1}\geq 1 and d m − 2 = 0 d_{m-2}=0, then by Lemmas 8.14 and 8.15, B = V m − 2 h + 1 B=V_{m-2}^{h+1} if b m − 1 − d m − 1 < d m − 1 + 1 b_{m-1}-d_{m-1}<d_{m-1}+1 and V m − 2 V_{m-2} is a prefix of V m − 3 ​ V m − 2 V_{m-3}V_{m-2}, and B = V m − 2 h B=V_{m-2}^{h} otherwise. But, by Corollary 8.10 with m m replaced by m − 1 m-1, V m − 2 V_{m-2} is a prefix of V m − 3 ​ V m − 2 V_{m-3}V_{m-2} if and only if the sequence d 1, …, d m − 2 d_{1},\ldots,d_{m-2} is not alternating.

If b m − 1 − d m − 1 ≥ 1 b_{m-1}-d_{m-1}\geq 1 and d m − 2 = b m − 2 d_{m-2}=b_{m-2}, then by Lemma 8.18 with m m replaced by m − 2 m-2, V m − 2 V_{m-2} is not a suffix of V m − 2 ​ V m − 3 V_{m-2}V_{m-3}. Thus by Lemmas 8.14 and 8.15, B = V m − 2 h B=V_{m-2}^{h}.

( v ​ i ​ i) (vii) We have m ≥ 3 m\geq 3: indeed, for m = 2 m=2, V 2 = b ​ a b 1 + 1 V_{2}=ba^{b_{1}+1} is a Christoffel word, which was excluded. Since d m − 1 = b m − 1 d_{m-1}=b_{m-1}, then d m − 2 = 0 d_{m-2}=0 by the greedy condition, and V m = V m − 3 ​ V m − 2 b m − 1 + 1 V_{m}=V_{m-3}V_{m-2}^{b_{m-1}+1}. If V m − 2 V_{m-2} is not a prefix of V m − 3 ​ V m − 2 V_{m-3}V_{m-2}, then by Corollary 8.10, the sequence d 1, …, d m − 2 d_{1},\ldots,d_{m-2} is alternating; then, since d m − 2 = 0, d m − 1 = b m − 1, d m = 0 d_{m-2}=0,d_{m-1}=b_{m-1},d_{m}=0, the sequence d 1, …, d m d_{1},\ldots,d_{m} is alternating too, and V m V_{m} is a Christoffel word, a contradiction. Thus V m − 2 V_{m-2} is a prefix of V m − 3 ​ V m − 2 V_{m-3}V_{m-2}, and by Lemmas 8.13 and 8.16, we get that B = V m − 2 B=V_{m-2}. ∎

## 9 The Sturmian graph revisited

We turn now to the suffixes of the central palindrome p p corresponding to a given Christoffel class. For this, we define L m = M ~ m L_{m}=\widetilde{M}_{m}, the reversal of the word M m M_{m}, with the previous notations.

###### Corollary 9.1.

Each suffix of p p has a unique factorization

 | L 0 d 1 L 1 d 2 ⋯ L m − 1 d m L_{0}^{d_{1}}L_{1}^{d_{2}}\cdots L_{m-1}^{d_{m}} |  |

where ∑ 1 ≤ i ≤ m d i ​ q i − 1 \sum_{1\leq i\leq m}d_{i}q_{i-1} is the lazy Ostrowski representation of its length. In particular

 | p = L 0 c 1 L 1 c 2 ⋯ L m − 1 c m, p=L_{0}^{c_{1}}L_{1}^{c_{2}}\cdots L_{m-1}^{c_{m}}, |  | (17) |

where the c i c_{i} are defined at the end of Section 7.

###### Proof.

Let s s be a suffix of p p, of length N = ∑ 1 ≤ i ≤ m d i ​ q i − 1 N=\sum_{1\leq i\leq m}d_{i}q_{i-1}, its lazy Ostrowski representation. Then s ~ \widetilde{s} is a prefix of p p. By Frid’s result (Corollary 7.6), we have s ~ = M m − 1 d m ⋯ M 0 d 1 \widetilde{s}=M_{m-1}^{d_{m}}\cdots M_{0}^{d_{1}}. Applying the reversal mapping, which is an anti-automorphism, we obtain s = L 0 d 1 L 1 d 2 ⋯ L m − 1 d m s=L_{0}^{d_{1}}L_{1}^{d_{2}}\cdots L_{m-1}^{d_{m}}. Uniqueness follows from the uniqueness of the lazy representation.

The last assertion follows from the equality q m − 2 = ∑ 1 ≤ i ≤ m c i ​ q i − 1 q_{m}-2=\sum_{1\leq i\leq m}c_{i}q_{i-1}, see Lemma 10.2 (iii). ∎

The previous corollary has a graph-theoretic interpretation. We construct an edge-labelled directed graph ( V, E) (V,E), that we shall call compact graph for short. It will turn out to be a graph introduced in Epifanio et al. 2007, where it is called the compact directed acyclic word graph of p p.

For the construction of this graph, it is convenient to view ( 17) as a word over the letters L 0, …, L m − 1 L_{0},\ldots,L_{m-1}; in particular we consider prefixes of this word, which are the elements of V V; the latter set has therefore c 1 + ⋯ + c m + 1 c_{1}+\cdots+c_{m}+1 elements. We denote by 1 1 the vertex corresponding to the empty word. For each vertex U ​ L i, 0 ≤ i ≤ m − 1 UL_{i},0\leq i\leq m-1, there is an edge labelled L i L_{i} from U U to U ​ L i UL_{i}:

 | U → L i U ​ L i. U\xrightarrow{L_{i}}UL_{i}. |  |

Moreover, if i < m − 1 i<m-1 and k ≥ 1 k\geq 1, then for each vertex of the form U ​ L i k ​ L i + 1, k ≥ 1 UL_{i}^{k}L_{i+1},k\geq 1, there is an edge labelled L i + 1 L_{i+1} from U U to U ​ L i k ​ L i + 1 UL_{i}^{k}L_{i+1}:

 | U → L i + 1 U ​ L i k ​ L i + 1. U\xrightarrow{L_{i+1}}UL_{i}^{k}L_{i+1}. |  |

The construction is illustrated in Figure 1.

We call the vertex 1 1 the origin. The label of a path in this graph is as usual the product of the labels of the edges of this path.

⋯ \cdots ⋯ \cdots ⋯ \cdots ⋯ \cdots L i − 1 L_{i-1} L i L_{i} L i L_{i} L i L_{i} L i L_{i} L i + 1 L_{i+1} L i + 1 L_{i+1} L i + 1 L_{i+1} L i + 1 L_{i+1} L i + 2 L_{i+2} L i + 1 L_{i+1} L i + 2 L_{i+2} blue arrows are all labelled L i + 1 L_{i+1} green arrows are all labelled L i + 2 L_{i+2} a pink node separates L j − 1 L_{j-1} -arrows from L j L_{j} -arrows for any j = 1, … ​ m j=1,\ldots m, there are c j + 1 c_{j+1} horizontal arrows labelled L j L_{j} Figure 1: The compact graph ( V, E) (V,E)

###### Corollary 9.2.

For each suffix s s of p p, there is a unique path in the compact graph, starting from the origin, and with label s s.

###### Proof.

We know that, for i = 0, …, m − 1 i=0,\ldots,m-1, the last letter of the word M i M_{i} is alternatively a a and b b (Corollary 7.5). Hence the first letter of L i L_{i} is alternatively a a and b b. By construction, each vertex has at most two outgoing edges, and then they are labelled L i L_{i} and L i + 1 L_{i+1}. Thus the graph has the following deterministic property: for each vertex, and for any two edges starting from it, the labels of these edges begin by distinct letters. This property ensures that for each word, there is at most one path starting from the origin and having this word as label. This proves uniqueness in the statement.

Consider some path from the origin in the graph. By inspection of the graph in Figure 1, its label s s is a product L 0 d 1 ⋯ L i + 1 d i + 2 ⋯ L m − 1 d m L_{0}^{d_{1}}\cdots L_{i+1}^{d_{i+2}}\cdots L_{m-1}^{d_{m}}, where for any j = 0, …, m − 1 j=0,\ldots,m-1, d j + 1 d_{j+1} is the number of edges labelled L j L_{j} in the path; hence 0 ≤ d j + 1 ≤ c j + 1 ≤ b j + 1 0\leq d_{j+1}\leq c_{j+1}\leq b_{j+1}. Thus N = ∑ 1 ≤ i ≤ m d i ​ q i − 1 N=\sum_{1\leq i\leq m}d_{i}q_{i-1} is a legal Ostrowski representation of the length N N of s s. This representation is lazy: indeed, suppose that for some i ≥ 0 i\geq 0, d i + 2 = 0 d_{i+2}=0 (with i + 2 ≤ m i+2\leq m); this means that the path has no edge labelled L i + 1 L_{i+1}; looking at the figure (where these edges are blue), we see that either the path has no vertex at the right of the central pink vertex (and then for all j ≥ i + 2 j\geq i+2, d j = 0 d_{j}=0), or the path must pass through this vertex, which implies that the path passes through all L i L_{i} -edges (red in the figure), and therefore d i + 1 = c i + 1 = b i + 1 d_{i+1}=c_{i+1}=b_{i+1} (the last equality holds since i + 1 < m i+1<m). Hence the representation is lazy, and by Corollary 9.1, s s is a suffix of p p.

Let now s s be any suffix of p p. Then by Corollary 9.1, s s is equal to L 0 d 1 L 1 d 2 ⋯ L m − 1 d m L_{0}^{d_{1}}L_{1}^{d_{2}}\cdots L_{m-1}^{d_{m}}, where ∑ i = 1 m d i ​ q i − 1 \sum_{i=1}^{m}d_{i}q_{i-1} is the lazy Ostrowski representation of the length of s s. Let k k be maximal such that d k ≠ 0 d_{k}\neq 0. Then s = L 0 d 1 L 1 d 2 ⋯ L k − 1 d k s=L_{0}^{d_{1}}L_{1}^{d_{2}}\cdots L_{k-1}^{d_{k}}. We claim that for each j = 1, …, k j=1,\ldots,k, there is a path labelled L 0 d 1 ⋯ L j − 1 d j L_{0}^{d_{1}}\cdots L_{j-1}^{d_{j}} from the origin until the vertex L 0 c 1 ⋯ L j − 2 c j − 1 L j − 1 d j L_{0}^{c_{1}}\cdots L_{j-2}^{c_{j-1}}L_{j-1}^{d_{j}}. The claim is clear for j = 1 j=1, since one has the edges 1 → L 0 → L 0 2 → ⋯ → L 0 c 1 1\to L_{0}\to L_{0}^{2}\to\cdots\to L_{0}^{c_{1}}, all labelled L 0 L_{0} and since d 1 ≤ b 1 = c 1 d_{1}\leq b_{1}=c_{1}. Admitting the claim for j ≤ k − 1 j\leq k-1, we prove it for j + 1 ≤ k j+1\leq k. If d j + 1 = 0 d_{j+1}=0, then j + 1 < k j+1<k and by laziness, d j = b j = c j d_{j}=b_{j}=c_{j} (the last equality holds since j < m j<m); then the path for j + 1 j+1 is the same as that for j j: there is a path labelled L 0 d 1 ⋯ L j − 1 d j = L 0 d 1 ⋯ L j − 1 d j L j d j + 1 L_{0}^{d_{1}}\cdots L_{j-1}^{d_{j}}=L_{0}^{d_{1}}\cdots L_{j-1}^{d_{j}}L_{j}^{d_{j+1}} from the origin until the vertex L 0 c 1 ⋯ L j − 2 c j − 1 L j − 1 d j = L 0 c 1 ⋯ L j − 2 c j − 1 L j − 1 c j L j d j + 1 L_{0}^{c_{1}}\cdots L_{j-2}^{c_{j-1}}L_{j-1}^{d_{j}}=L_{0}^{c_{1}}\cdots L_{j-2}^{c_{j-1}}L_{j-1}^{c_{j}}L_{j}^{d_{j+1}}. Suppose now that d j + 1 ≠ 0 d_{j+1}\neq 0; in the graph we have the c j + 1 c_{j+1} consecutive edges L 0 c 1 ⋯ L j − 2 c j − 1 L j − 1 d j → L 0 c 1 ⋯ L j − 2 c j − 1 L j − 1 c j L j → L 0 c 1 ⋯ L j − 2 c j − 1 L j − 1 c j L j 2 → ⋯ → L 0 c 1 ⋯ L j − 2 c j − 1 L j − 1 c j L j c j + 1 L_{0}^{c_{1}}\cdots L_{j-2}^{c_{j-1}}L_{j-1}^{d_{j}}\to L_{0}^{c_{1}}\cdots L_{j-2}^{c_{j-1}}L_{j-1}^{c_{j}}L_{j}\to L_{0}^{c_{1}}\cdots L_{j-2}^{c_{j-1}}L_{j-1}^{c_{j}}L_{j}^{2}\to\cdots\to L_{0}^{c_{1}}\cdots L_{j-2}^{c_{j-1}}L_{j-1}^{c_{j}}L_{j}^{c_{j+1}}, all labelled L j L_{j}; note that d j + 1 ≤ c j + 1 d_{j+1}\leq c_{j+1}: indeed, the representation is legal, hence d j + 1 ≤ b j + 1 d_{j+1}\leq b_{j+1} and b j + 1 = c j + 1 b_{j+1}=c_{j+1}, except if j + 1 = m j+1=m; but in this case, since s s is of length at most q m − 2 q_{m}-2, we have d m ≤ b m − 1 = c m d_{m}\leq b_{m}-1=c_{m} by Corollary 10.3; thus the claim follows for j + 1 j+1 too.

Thus, for j = k j=k, we obtain that there is a path starting from the origin and labelled s s, in the graph. ∎

In the compact graph ( V, E) (V,E), replace each label of an edge by its length. We obtain a graph whose edges are labelled by positive natural numbers. This time, the sum of the labels of the edges of a path is called the label of this path. Since the suffixes of p p have all distinct lengths, we obtain

###### Corollary 9.3.

For each natural number N = 0, 1, …, q m − 2 N=0,1,\ldots,q_{m}-2 there is a unique path in this graph, starting from the origin, with label N N.

The compact graph is the Sturmian graph of Epifanio et al. 2007; Epifanio et al. 2012. This will be verified now.

We define the notion of generalized automaton: it is a directed graph, whose vertices are called states, whose edges are called transitions and are labelled by nonempty words, with a distinguished vertex called the initial state, and a distinguished subset of the vertices, called the set of final states; the automaton is called deterministic if for any two edges outgoing from a vertex, their labels have distinct first letters; the generalized automaton is called homogeneous if for each vertex, the incoming edges all have the same label. The language recognized by a generalized automaton is the set of words which are labels of some path from the initial state to some final state.

The compact graph is a deterministic homogeneous generalized automaton. Its initial state is the empty word, and each state is final; it recognizes the set of suffixes of p p, by Corollary 9.2.

We may turn this generalized automaton into an automaton 𝒜 \mathcal{A} (that is, where all the labels of the edges are letters), as follows: using Figure 1, note that there is a maximal horizontal path labelled L i + 1 L_{i+1}:

 | q 0 → L i + 1 q 1 → L i + 1 ⋯ → L i + 1 q c, q_{0}\overset{L_{i+1}}{\to}q_{1}\overset{L_{i+1}}{\to}\cdots\overset{L_{i+1}}{\to}q_{c}, |  |

where c = c i + 2 c=c_{i+2} is the number of horizontal edges labelled L i + 1 L_{i+1} (the blue edges) in the compact graph. Replace this path by an horizontal path whose edges are labelled by the letters of L i + 1 c L_{i+1}^{c}, adding enough new vertices and new edges:

 | q 0 → 𝑥 q ′ ⋯ → 𝑦 q c, q_{0}\overset{x}{\to}q^{\prime}\cdots\overset{y}{\to}q_{c}, |  |

where x x is the first letter of L i + 1 L_{i+1}, and y y its last. Now, let each curved blue edge in the figure point onto the vertex q ′ q^{\prime}, and have new label x x. The initial state of 𝒜 \mathcal{A} is unchanged, and similarly for the final states.

A moment’s thought shows that this new automaton 𝒜 \mathcal{A} is deterministic, homogeneous, and recognizes the same language as the compact graph, that is, the set of suffixes of p p. This automaton has | p | + 1 |p|+1 vertices (because there is in 𝒜 \mathcal{A} a path labelled p p containing all vertices); hence it is minimal, in the sense that it has the smallest number of vertices among all automata recognizing this language: indeed, such an automaton must have at least | p | + 1 |p|+1 vertices.

There is a simple algorithm to recover the compact graph from the minimal automaton 𝒜 \mathcal{A} of the set of suffixes of p p: one chooses some vertex v v which is not final, which has only one outgoing edge v ​ → 𝑡 ​ v ′ v\overset{t}{\to}v^{\prime}; one considers all incoming edges, all labelled by the same letter z z (since the automaton is homogeneous); then one suppresses the vertex v v and one lets the incoming edges point towards v ′ v^{\prime}, adding t t at the end of their label. Iterating this procedure, called compaction, one recovers ( V, E) (V,E).

In the light of Epifanio et al. 2007 (Theorem 19, and beginning of Section 19, where compaction is described 2 2 2 The notion of compaction of an automaton appears in Blumer et al. 1987.), this proves that the graph of Corollary 9.3 is the Sturmian graph. It implies also Theorem 47 of Epifanio et al. 2012: each path in the Sturmian graph, with label N N, corresponds to the lazy Ostrowski representation of N N.

We indicate now how to construct the compact graph using the iterated palindromization of Aldo de Luca de Luca 1997 (see also ( Reutenauer 2019, Section 12.1)). Recall the definition of this operator, denoted P ​ a ​ l Pal. One defines first the right palindromic closure of a word w w, denoted w ( +) w^{(+)}: it is the shortest palindrome having w w as prefix. Then the mapping P ​ a ​ l Pal from a free monoid into itself is defined recursively by P ​ a ​ l ​ ( 1) = 1 Pal(1)=1 and P ​ a ​ l ​ ( w ​ x) = ( P ​ a ​ l ​ ( w) ​ x) ( +) Pal(wx)=(Pal(w)x)^{(+)} for any word w w and any letter x x. The theorem of de Luca is that P ​ a ​ l Pal is a bijection from { a, b } ∗ \{a,b\}^{*} onto the set of central words.

If p = P ​ a ​ l ​ ( v) p=Pal(v), v v is called the directive word of the central word p p. It follows from the definition of P ​ a ​ l Pal that the palindromic prefixes of P ​ a ​ l ​ ( v) Pal(v) are the words P ​ a ​ l ​ ( u) Pal(u), where u u runs through the prefixes of v v.

###### Proposition 9.4.

The central word p p has the directive word v = a c 1 b c 2 a c 3 ⋯ ( a or b) c m v=a^{c_{1}}b^{c_{2}}a^{c_{3}}\cdots(a\,\mbox{or}\,\,b)^{c_{m}}. The word p = P ​ a ​ l ​ ( v) p=Pal(v) has 1 + c 1 + ⋯ + c m 1+c_{1}+\cdots+c_{m} palindromic prefixes, which are the formal prefixes of ( 17). In particular, L i = P a l ( a c 1 ⋯ ( a or b) c i) − 1 P a l ( a c 1 ⋯ ( a or b) c i ( b or a)) L_{i}=Pal(a^{c_{1}}\cdots(a\,\mbox{or}\,\,b)^{c_{i}})^{-1}Pal(a^{c_{1}}\cdots(a\,\mbox{or}\,\,b)^{c_{i}}(b\,\mbox{or}\,\,a)).

###### Proof.

We know that the Slope of M m M_{m}, and in particular of the lower Christoffel word in the conjugation class of M m M_{m}, is S = [0, a 1, …, a n] S=[0,a_{1},\ldots,a_{n}] (Theorem 7.3). It follows from the analysis at the end of Section 6 that s = [0, b 1, …, b m] s=[0,b_{1},\ldots,b_{m}] if b 1 ≥ 1 b_{1}\geq 1, and s = [b 2, …, b m] s=[b_{2},\ldots,b_{m}] if b 1 = 0 b_{1}=0. It follows from Theorem 14.2.3 in Reutenauer 2019 (the result is from ( Graham et al. 1989, Section 14.2.3)) that the path leading from the root to the node s s in the Stern-Brocot tree is coded by the word v = a c 1 b c 2 ⋯ ( a or b) c m v=a^{c_{1}}b^{c_{2}}\cdots(a\,\mbox{or}\,\,b)^{c_{m}} ( a a means left, and b b means right). It follows then from the correspondence between the Stern-Brocot tree, the tree of Christoffel words, and the tree of central words (see Sections 12.1, 14.1 and 14.2 in Reutenauer 2019) that the path from the root to p p in the latter tree is coded by v v, proving the first assertion.

The word p = P ​ a ​ l ​ ( v) p=Pal(v) has | v | + 1 |v|+1 palindromic prefixes. It follows from Lemma 7.7 that all the words M i − 1 c M i − 2 c i − 1 ⋯ M 1 c 2 M 0 c 1 M_{i-1}^{c}M_{i-2}^{c_{i-1}}\cdots M_{1}^{c_{2}}M_{0}^{c_{1}}, where i = 1, …, m i=1,\ldots,m, 0 ≤ c ≤ c i 0\leq c\leq c_{i}, are palindromes. Hence their reversals L 0 c 1 ​ L 1 c 2 ​ … ​ L i − 2 c i − 1 ​ L i − 1 c L_{0}^{c_{1}}L_{1}^{c_{2}}\ldots L_{i-2}^{c_{i-1}}L_{i-1}^{c} are palindromes too, and are suffixes of p p by Corollary 9.1, proving the second assertion.

The last assertion then follows. ∎

The proposition implies that the compact graph, and the Sturmian graph, are embedded in the tree of central words, and in the Stern-Brocot tree.

###### Corollary 9.5.

Consider in the tree of central words (resp. the Stern-Brocot tree) the path form the root to p p (resp. to the slope s s of M m M_{m}). Direct the edges downwards and label each edge u → v u\to v (resp. p / q → p ′ / q ′ p/q\to p^{\prime}/q^{\prime}) by u − 1 ​ v u^{-1}v (resp. by p ′ + q ′ − p − q p^{\prime}+q^{\prime}-p-q). Add an edge from each vertex to the first vertex after the first turn below on the path; the label of a new edge depends only on its final vertex. This graph is the compact graph (resp. the Sturmian graph).

###### Proof.

Consider some node on the tree of central words; as in the proof above, we associate with it the word v ∈ { a, b } ∗ v\in\{a,b\}^{*}, which encodes the path from the root to this vertex; then this vertex is P ​ a ​ l ​ ( v) Pal(v) (see ( Reutenauer 2019, Section 12.1)). The construction of the compact graph then follows from the proposition. And from this the construction of the Sturmian graph also follows. ∎

An example may be useful. Let m = 3, a 1 = 2, a 2 = 1, a 3 = 3 m=3,a_{1}=2,a_{2}=1,a_{3}=3. Then M − 1 = b, M 0 = a, M 1 = M 0 a 1 − 1 ​ M − 1 = a ​ b M_{-1}=b,M_{0}=a,M_{1}=M_{0}^{a_{1}-1}M_{-1}=ab, M 2 = M 1 a 2 ​ M 0 = a ​ b ​ a M_{2}=M_{1}^{a_{2}}M_{0}=aba, M 3 = M 2 a 3 ​ M 1 = a ​ b ​ a ​ a ​ b ​ a ​ a ​ b ​ a ​ a ​ b M_{3}=M_{2}^{a_{3}}M_{1}=abaabaabaab. Since M 3 = p ​ a ​ b M_{3}=pab, we have p = a ​ b ​ a 2 ​ b ​ a 2 ​ b ​ a p=aba^{2}ba^{2}ba. The palindromic prefixes of p p are 1 1, a a, a ​ b ​ a aba, a ​ b ​ a ​ a ​ b ​ a abaaba, p p; the letter following each palindromic prefix is underlined: p = a ¯ ​ b ¯ ​ a ​ a ¯ ​ b ​ a ​ a ¯ ​ b ​ a p=\underline{a}\,\underline{b}a\underline{a}ba\underline{a}ba, and therefore p = P ​ a ​ l ​ ( a ​ b ​ a ​ a) p=Pal(abaa). One has P ​ a ​ l ​ ( 1) = 1, P ​ a ​ l ​ ( a) = a, P ​ a ​ l ​ ( a ​ b) = a ​ b ​ a, P ​ a ​ l ​ ( a ​ b ​ a) = a ​ b ​ a ​ a ​ b ​ a Pal(1)=1,Pal(a)=a,Pal(ab)=aba,Pal(aba)=abaaba. The tree interpretation is shown in Figure 2: the words 1, a, a ​ b ​ a, a ​ b ​ a ​ a ​ b ​ a, p 1,a,aba,abaaba,p are the nodes on the path from the root to p p in the tree of central words. One recovers in two ways that L 0 = a, L 1 = b ​ a, L 2 = a ​ b ​ a L_{0}=a,L_{1}=ba,L_{2}=aba: using L i = M ~ i L_{i}=\widetilde{M}_{i}, or using the last assertion of Proposition 9.4.

a ​ b ​ a ​ a ​ b ​ a ​ a ​ b ​ a abaabaaba a ​ b ​ a ​ a ​ b ​ a abaaba a ​ b ​ a aba a a ϵ \epsilon a ​ b ​ a ​ a ​ b ​ a ​ a ​ b ​ a abaabaaba a ​ b ​ a ​ a ​ b ​ a abaaba a ​ b ​ a aba a a ϵ \epsilon a a b ​ a ba b ​ a ba a ​ b ​ a aba a ​ b ​ a aba a ​ b ​ a aba 4 7 \frac{4}{7} 3 5 \frac{3}{5} 2 3 \frac{2}{3} 1 2 \frac{1}{2} 1 1 \frac{1}{1} 1 1 2 2 2 2 3 3 3 3 3 3 Figure 2: A path in the tree of central words, a compact graph and a Sturmian graph

## 10 Appendix: a proof of existence and uniqueness of the greedy and lazy representations

We want to prove Proposition 3.1. We begin by two lemmas.

###### Lemma 10.1.

Let k = 0, …, m k=0,\ldots,m and a legal Ostrowski representation

 | N = d 1 ​ q 0 + d 2 ​ q 1 + ⋯ + d k ​ q k − 1. N=d_{1}q_{0}+d_{2}q_{1}+\cdots+d_{k}q_{k-1}. |  | (18) |

(i) If in ( 18) the sequence d i d_{i} is alternating, with k = 0 k=0 or d k ≠ 0 d_{k}\neq 0, then N = q k − 1 N=q_{k}-1.

(ii) If in ( 18) one assumes that the representation is lazy and that k = 0 k=0 or d k = b k d_{k}=b_{k}, then N ≥ q k − 1 N\geq q_{k}-1.

Note that we say that the representation ( 18) is legal (resp. greedy, resp. lazy) if the representation ( 4) of N N obtained by letting d i = 0 d_{i}=0 for i = k + 1, …, m i=k+1,\ldots,m has this property.

###### Proof.

(i) The hypothesis implies d k = b k d_{k}=b_{k}. For k = 0 k=0 and k = 1 k=1, the equality follows from q 0 = 1 q_{0}=1 and b 1 = a 1 − 1 = q 1 − 1 b_{1}=a_{1}-1=q_{1}-1. Suppose that k ≥ 1 k\geq 1, and that the equality is true for k − 1 k-1 and k k. Consider an alternating sequence d 1, …, d k + 1 d_{1},\ldots,d_{k+1} with d k + 1 ≠ 0 d_{k+1}\neq 0; then d k + 1 = b k + 1 d_{k+1}=b_{k+1}. We have ∑ i = 1 k + 1 d i ​ q i − 1 = b k + 1 ​ q k + ∑ i = 1 k − 1 d i ​ q i − 1 \sum_{i=1}^{k+1}d_{i}q_{i-1}=b_{k+1}q_{k}+\sum_{i=1}^{k-1}d_{i}q_{i-1} (since d k = 0 d_{k}=0, because the sequence is alternating) = a k + 1 ​ q k + q k − 1 − 1 =a_{k+1}q_{k}+q_{k-1}-1 (by induction, since d k − 1 = b k − 1 ≠ 0 d_{k-1}=b_{k-1}\neq 0) = q k + 1 − 1 =q_{k+1}-1.

(ii) This is clearly true for k = 0 k=0 and k = 1 k=1, since q 0 = 1 q_{0}=1 and b 1 = a 1 − 1 = q 1 − 1 b_{1}=a_{1}-1=q_{1}-1. Assume that k ≥ 1 k\geq 1 and that it is true for k − 1 k-1 and k k, and we prove it for k + 1 k+1; thus we consider a sequence d 1, …, d k + 1 d_{1},\ldots,d_{k+1} with d k + 1 = b k + 1 d_{k+1}=b_{k+1}. If d k ≠ 0 d_{k}\neq 0, then N = ∑ i = 1 k + 1 d i ​ q i − 1 ≥ b k + 1 ​ q k + q k − 1 = a k + 1 ​ q k + q k − 1 = q k + 1 ≥ q k + 1 − 1 N=\sum_{i=1}^{k+1}d_{i}q_{i-1}\geq b_{k+1}q_{k}+q_{k-1}=a_{k+1}q_{k}+q_{k-1}=q_{k+1}\geq q_{k+1}-1. If d k = 0 d_{k}=0 then, assuming that k ≥ 2 k\geq 2, we have d k − 1 = b k − 1 d_{k-1}=b_{k-1} since the representation is lazy ; thus by induction, N ≥ b k + 1 ​ q k + q k − 1 − 1 = a k + 1 ​ q k + q k − 1 − 1 = q k + 1 − 1 N\geq b_{k+1}q_{k}+q_{k-1}-1=a_{k+1}q_{k}+q_{k-1}-1=q_{k+1}-1. The remaining case is k = 1, d 2 = b 2 = a 2, d 1 = 0 k=1,d_{2}=b_{2}=a_{2},d_{1}=0 and N = d 2 ​ q 1 = a 2 ​ a 1 = q 2 − 1 N=d_{2}q_{1}=a_{2}a_{1}=q_{2}-1. ∎

###### Lemma 10.2.

Let 0 ≤ k ≤ m 0\leq k\leq m, N ∈ ℕ N\in\mathbb{N}, and N = ∑ i = 1 k d i ​ q i − 1 N=\sum_{i=1}^{k}d_{i}q_{i-1} be a legal Ostrowski representation.

(i) If the representation is greedy, then

 | N ≤ q k − 1; N\leq q_{k}-1; |  |

if moreover k = 0 k=0 or d k ≠ 0 d_{k}\neq 0, then

 | q k − 1 − 1 < N. q_{k-1}-1<N. |  |

(ii) If k ≥ 1 k\geq 1 and the representation is lazy, then

 | N ≤ q k + q k − 1 − 2; N\leq q_{k}+q_{k-1}-2; |  |

if moreover, d k ≠ 0 d_{k}\neq 0, then

 | q k − 1 + q k − 2 − 2 < N. q_{k-1}+q_{k-2}-2<N. |  |

(iii) One has

 | ∑ i = 1 k b i ​ q i − 1 = q k + q k − 1 − 2. \sum_{i=1}^{k}b_{i}q_{i-1}=q_{k}+q_{k-1}-2. |  |

###### Proof.

(i) We prove the first inequality by induction on k k. For k = 0 k=0, N = 0 N=0 and it holds since q 0 = 1 q_{0}=1. For k = 1 k=1, it holds since d 1 ≤ a 1 − 1 d_{1}\leq a_{1}-1. Assume that k ≥ 1 k\geq 1, and that it is true for 1, …, k 1,\ldots,k, and we prove it for k + 1 k+1. If d k + 1 = a k + 1 = b k + 1 d_{k+1}=a_{k+1}=b_{k+1} (since k + 1 ≥ 2 k+1\geq 2), then d k = 0 d_{k}=0 by ( 6); then d 1 ​ q 0 + d 2 ​ q 1 + ⋯ + d k + 1 ​ q k = d 1 ​ q 0 + d 2 ​ q 1 + … + d k − 1 ​ q k − 2 + a k + 1 ​ q k ≤ d_{1}q_{0}+d_{2}q_{1}+\cdots+d_{k+1}q_{k}=d_{1}q_{0}+d_{2}q_{1}+\ldots+d_{k-1}q_{k-2}+a_{k+1}q_{k}\leq (by induction) q k − 1 − 1 + a k + 1 ​ q k = q k + 1 − 1 q_{k-1}-1+a_{k+1}q_{k}=q_{k+1}-1; if on the other hand, d k + 1 ≤ a k + 1 − 1 d_{k+1}\leq a_{k+1}-1, then d 1 ​ q 0 + d 2 ​ q 1 + ⋯ + d k + 1 ​ q k = d 1 ​ q 0 + d 2 ​ q 1 + ⋯ + d k ​ q k − 1 + d k + 1 ​ q k ≤ d_{1}q_{0}+d_{2}q_{1}+\cdots+d_{k+1}q_{k}=d_{1}q_{0}+d_{2}q_{1}+\cdots+d_{k}q_{k-1}+d_{k+1}q_{k}\leq (by induction) q k − 1 + a k + 1 ​ q k − q k < − 1 + q k − 1 + a k + 1 ​ q k = q k + 1 − 1 q_{k}-1+a_{k+1}q_{k}-q_{k}<-1+q_{k-1}+a_{k+1}q_{k}=q_{k+1}-1.

The second inequality follows from q − 1 = 0 q_{-1}=0, and from d k > 0 d_{k}>0 if k ≥ 1 k\geq 1.

(ii) If k = 1 k=1, both inequalities are easy to verify. Suppose that they hold for k ≥ 1 k\geq 1, and consider the case k + 1 k+1, N = ∑ i = 1 k + 1 d i ​ q i − 1 N=\sum_{i=1}^{k+1}d_{i}q_{i-1}. By induction, ∑ i = 1 k d i ​ q i − 1 ≤ q k + q k − 1 − 2 \sum_{i=1}^{k}d_{i}q_{i-1}\leq q_{k}+q_{k-1}-2, hence, since d k + 1 ≤ a k + 1 d_{k+1}\leq a_{k+1}, N ≤ q k + q k − 1 − 2 + a k + 1 ​ q k = q k + 1 + q k − 2 N\leq q_{k}+q_{k-1}-2+a_{k+1}q_{k}=q_{k+1}+q_{k}-2.

Suppose now that d k + 1 ≠ 0 d_{k+1}\neq 0. Then, if d k ≥ 1 d_{k}\geq 1, then N = d k + 1 ​ q k + d k ​ q k − 1 + ⋯ ≥ q k + q k − 1 > q k + q k − 1 − 2 N=d_{k+1}q_{k}+d_{k}q_{k-1}+\cdots\geq q_{k}+q_{k-1}>q_{k}+q_{k-1}-2. Suppose now that d k = 0 d_{k}=0; if k ≥ 2 k\geq 2, we have d k − 1 = b k − 1 d_{k-1}=b_{k-1} by lazyness, hence by Lemma 10.1 (ii) ∑ i = 1 k − 1 d i ​ q i − 1 ≥ q k − 1 − 1 \sum_{i=1}^{k-1}d_{i}q_{i-1}\geq q_{k-1}-1; thus N = d k + 1 ​ q k + ∑ i = 1 k − 1 d i ​ q i − 1 ≥ q k + q k − 1 − 1 > q k + q k − 1 − 2 N=d_{k+1}q_{k}+\sum_{i=1}^{k-1}d_{i}q_{i-1}\geq q_{k}+q_{k-1}-1>q_{k}+q_{k-1}-2. The remaining case is k = 1 k=1, d 2 ≥ 1 d_{2}\geq 1, d 1 = 0 d_{1}=0; then N = d 2 ​ q 1 = d 2 ​ a 1 ≥ a 1 > a 1 − 1 = q 1 + q 0 − 2 N=d_{2}q_{1}=d_{2}a_{1}\geq a_{1}>a_{1}-1=q_{1}+q_{0}-2.

(iii) is proved similarly by induction. ∎

###### Corollary 10.3.

Let k ≥ 1 k\geq 1. For a lazy representation N = ∑ i = 1 k d i ​ q i − 1 N=\sum_{i=1}^{k}d_{i}q_{i-1}, one has d k = b k d_{k}=b_{k} if and only if N ≥ q k − 1 N\geq q_{k}-1.

###### Proof.

Suppose that d k = b k d_{k}=b_{k}; then N ≥ q k − 1 N\geq q_{k}-1 by Lemma 10.1 (ii).

Suppose now that d k ≠ b k d_{k}\neq b_{k}; then d k ≤ b k − 1 d_{k}\leq b_{k}-1. Then N + q k − 1 N+q_{k-1} has the lazy representation ( d k + 1) ​ q k − 1 + ∑ i = 1 k − 1 d i ​ q i − 1 (d_{k}+1)q_{k-1}+\sum_{i=1}^{k-1}d_{i}q_{i-1}. Thus by Lemma 10.2 (ii), N + q k − 1 ≤ q k + q k − 1 − 2 N+q_{k-1}\leq q_{k}+q_{k-1}-2, hence N ≤ q k − 2 N\leq q_{k}-2. ∎

###### of Proposition 3.1.

We observe that the sequence q k q_{k}, k = − 1, 0, 1, 2, …, m, k=-1,0,1,2,\ldots,m, is strictly increasing, except that one can have q 0 = q 1 = 1 q_{0}=q_{1}=1, and this happens if and only if a 1 = 1 a_{1}=1.

(i) Let 0 ≤ k ≤ m 0\leq k\leq m. We prove the existence of a greedy representation N = ∑ i = 1 k d i ​ q i − 1 N=\sum_{i=1}^{k}d_{i}q_{i-1} for each N N satisfying N ≤ q k − 1 N\leq q_{k}-1; by the previous observation, this will prove the existence of a greedy representation for each N N with 0 ≤ N ≤ q m − 1 0\leq N\leq q_{m}-1. For k = 0 k=0, we have N = 0 N=0 and existence is clear. For k = 1 k=1, N ≤ q 1 − 1 N\leq q_{1}-1; then N ≤ a 1 − 1 N\leq a_{1}-1 and we have N = d 1 ​ q 0 N=d_{1}q_{0}, d 1 = N ≤ a 1 − 1 d_{1}=N\leq a_{1}-1 and existence follows.

Suppose now that k ≥ 1 k\geq 1, and let N N satisfy N ≤ q k + 1 − 1 N\leq q_{k+1}-1. Then N ≤ a k + 1 ​ q k + q k − 1 − 1 N\leq a_{k+1}q_{k}+q_{k-1}-1. Since q k − 1 − 1 < q k q_{k-1}-1<q_{k}, we have N < ( a k + 1 + 1) ​ q k N<(a_{k+1}+1)q_{k}; thus, performing the Euclidean division of N N by q k q_{k}, there are uniquely determined r, t r,t with N = t ​ q k + r N=tq_{k}+r, 0 ≤ r ≤ q k − 1 0\leq r\leq q_{k}-1 and t ≤ a k + 1 t\leq a_{k+1}.

By induction on k k, r r has a greedy representation r = ∑ i = 1 k d i ​ q i − 1 r=\sum_{i=1}^{k}d_{i}q_{i-1}, and then N N has the representation obtained by adding that of r r and t ​ q k tq_{k}. If t < a k + 1 t<a_{k+1}, it is a greedy representation. If t = a k + 1 t=a_{k+1}, then we have a k + 1 ​ q k + r = N ≤ q k + 1 − 1 = a k + 1 ​ q k + q k − 1 − 1 a_{k+1}q_{k}+r=N\leq q_{k+1}-1=a_{k+1}q_{k}+q_{k-1}-1, thus r ≤ q k − 1 − 1 r\leq q_{k-1}-1, and N = r + 0 ⋅ q k − 1 + a k + 1 ​ q k N=r+0\cdot q_{k-1}+a_{k+1}q_{k}, and we conclude by induction on k k that r r has a greedy representation, hence N N too.

We prove now the uniqueness of the greedy representation. We may assume that N ≠ 0 N\neq 0. Assume that we have two greedy representations for N N, N = ∑ i = 1 k d i ​ q i − 1 N=\sum_{i=1}^{k}d_{i}q_{i-1}, N = ∑ i = 1 h e i ​ q i − 1 N=\sum_{i=1}^{h}e_{i}q_{i-1}, written in such a way that d k ≠ 0 ≠ e h d_{k}\neq 0\neq e_{h}. We have by Lemma 10.2 (i): N < q k N<q_{k}, N < q h N<q_{h}, N ≥ q k − 1 N\geq q_{k-1}, and N ≥ q h − 1 N\geq q_{h-1}. This forces k = h k=h, since the sequence ( q i) (q_{i}) is increasing. By Lemma 10.2 (i), we have r = ∑ i = 1 k − 1 d i ​ q i − 1 < q k − 1 r=\sum_{i=1}^{k-1}d_{i}q_{i-1}<q_{k-1}; since N = d k ​ q k − 1 + r N=d_{k}q_{k-1}+r, d k d_{k} is the quotient of the Euclidean division of N N by q k − 1 q_{k-1}; similarly for e k e_{k}, so that d k = e k d_{k}=e_{k}, and the representations coincide by induction on k k, since the greedy condition remains if one replaces the highest nonzero digit by 0.

(ii) We prove now the existence of the lazy representation. We observe that ( ∗) (*) the sequence q k + q k − 1 − 2 q_{k}+q_{k-1}-2 is strictly increasing for k = 0, …, m k=0,\ldots,m, with first value − 1 -1. We prove by induction on k = 1, …, m k=1,\ldots,m that if N ≤ q k + q k − 1 − 2 N\leq q_{k}+q_{k-1}-2, then N N has a lazy representation of the form N = ∑ i = 1 k d i ​ q i − 1 N=\sum_{i=1}^{k}d_{i}q_{i-1}. For k = 1 k=1, the inequality is N ≤ a 1 − 1 N\leq a_{1}-1, and we have indeed N = d 1 ​ q 0 N=d_{1}q_{0}, with d 1 = N d_{1}=N, 0 ≤ d 1 ≤ a 1 − 1 0\leq d_{1}\leq a_{1}-1. Assume now that k ≥ 1 k\geq 1, and that the property holds for k k, and we prove it when N N satisfies N ≤ q k + 1 + q k − 2 N\leq q_{k+1}+q_{k}-2. By induction, we may assume that q k + q k − 1 − 2 < N q_{k}+q_{k-1}-2<N. We have q k + q k − 1 − 1 ≤ N q_{k}+q_{k-1}-1\leq N and since q k − 1 − 1 ≥ 0 q_{k-1}-1\geq 0 (because k ≥ 1 k\geq 1), there exists j j, 1 ≤ j ≤ a k + 1 1\leq j\leq a_{k+1} such that j ​ q k ≤ N jq_{k}\leq N and we take j j maximal. Then either j = a k + 1 j=a_{k+1} and N ≤ q k + q k + 1 − 2 = ( j + 1) ​ q k + q k − 1 − 2 N\leq q_{k}+q_{k+1}-2=(j+1)q_{k}+q_{k-1}-2; or j < a k + 1 j<a_{k+1} and then j + 1 ≤ a k + 1 j+1\leq a_{k+1} and by maximality, N < ( j + 1) ​ q k ≤ ( j + 1) ​ q k + q k − 1 − 1 N<(j+1)q_{k}\leq(j+1)q_{k}+q_{k-1}-1 and we have N ≤ ( j + 1) ​ q k + q k − 1 − 2 N\leq(j+1)q_{k}+q_{k-1}-2, too.

Write N = j ​ q k + N ′ N=jq_{k}+N^{\prime}; then 0 ≤ N ′ ≤ q k + q k − 1 − 2 0\leq N^{\prime}\leq q_{k}+q_{k-1}-2. By induction, N ′ N^{\prime} has a lazy representation N ′ = d 1 ​ q 0 + ⋯ + d k ​ q k − 1. N^{\prime}=d_{1}q_{0}+\cdots+d_{k}q_{k-1}. Then, d 1 ​ q 0 + ⋯ + d k ​ q k − 1 + j ​ q k d_{1}q_{0}+\cdots+d_{k}q_{k-1}+jq_{k} is a lazy representation of N N, except when d k = 0 d_{k}=0 and d k − 1 ≠ b k − 1 d_{k-1}\not=b_{k-1} (so that k ≥ 2 k\geq 2); since a k = b k a_{k}=b_{k}, d 1 ​ q 0 + ⋯ + ( d k − 1 + 1) ​ q k − 2 + b k ​ q k − 1 + ( j − 1) ​ q k d_{1}q_{0}+\cdots+(d_{k-1}+1)q_{k-2}+b_{k}q_{k-1}+(j-1)q_{k} is then a lazy representation of N N.

We prove now uniqueness of the lazy representation. We may assume that N ≠ 0 N\neq 0. Suppose that N N has two lazy representations N = ∑ i = 1 k d i ​ q i − 1 N=\sum_{i=1}^{k}d_{i}q_{i-1}, N = ∑ i = 1 h e i ​ q i − 1 N=\sum_{i=1}^{h}e_{i}q_{i-1}, written in such a way that d k ≠ 0 ≠ e h d_{k}\neq 0\neq e_{h}. We have by Lemma 10.2 (ii): q k − 1 + q k − 2 − 2 < N ≤ q k + q k − 1 − 2 q_{k-1}+q_{k-2}-2<N\leq q_{k}+q_{k-1}-2 and q h − 1 + q h − 2 − 2 < N ≤ q h + q h − 1 − 2 q_{h-1}+q_{h-2}-2<N\leq q_{h}+q_{h-1}-2. This implies that k = h k=h, by observation ( ∗) (*).

We claim that b k − d k b_{k}-d_{k} is the quotient of the Euclidean division of N ′ = q k + q k − 1 − 2 − N N^{\prime}=q_{k}+q_{k-1}-2-N by q k − 1 q_{k-1}. The same being true for b k − e k b_{k}-e_{k}, we have d k = e k d_{k}=e_{k} and we conclude by induction that the representations coincide.

For the claim, we may assume that k ≥ 2 k\geq 2; we have N ′ = ∑ i = 1 k ( b i − d i) ​ q i − 1 N^{\prime}=\sum_{i=1}^{k}(b_{i}-d_{i})q_{i-1} by Lemma 10.2 (iii). We have N ′ = ( b k − d k) ​ q k − 1 + r N^{\prime}=(b_{k}-d_{k})q_{k-1}+r, where r = ∑ i = 1 k − 1 ( b i − d i) ​ q i − 1 r=\sum_{i=1}^{k-1}(b_{i}-d_{i})q_{i-1}. By lazyness, this is a greedy representation of r r. Hence r ≤ q k − 1 − 1 r\leq q_{k-1}-1 by Lemma 10.2 (i); since r ≥ 0 r\geq 0, the claim follows. ∎

###### Acknowledgements.

We thank the two anonymous referees for their comments. This work was partially supported by NSERC, Canada.

## References

- Aigner (2013) M. Aigner. *Markov’s theorem and 100 years of the uniqueness conjecture*. Springer, Cham, 2013. ISBN 978-3-319-00887-5; 978-3-319-00888-2. URL [https://doi.org/10.1007/978-3-319-00888-2][3]. A mathematical journey from irrational numbers to perfect matchings.
- Allouche and Shallit (2003) J.-P. Allouche and J. Shallit. *Automatic sequences*. Cambridge University Press, Cambridge, 2003. ISBN 0-521-82332-3. URL [https://doi.org/10.1017/CBO9780511546563][4]. Theory, applications, generalizations.
- Berstel (1990) J. Berstel. Tracé de droites, fractions continues et morphismes itérés. In *Mots*, Lang. Raison. Calc., pages 298–309. Hermès, Paris, 1990.
- Berstel et al. (2009) J. Berstel, A. Lauve, C. Reutenauer, and F. V. Saliola. *Combinatorics on words*, volume 27 of *CRM Monograph Series*. American Mathematical Society, Providence, RI, 2009. ISBN 978-0-8218-4480-9. URL [https://doi.org/10.1090/crmm/027][5]. Christoffel words and repetitions in words.
- Blumer et al. (1987) A. Blumer, J. Blumer, D. Haussler, R. McConnell, and A. Ehrenfeucht. Complete inverted files for efficient text retrieval and analysis. *J. Assoc. Comput. Mach.*, 34(3):578–595, 1987. ISSN 0004-5411. URL [https://doi.org/10.1145/28869.28873][6].
- Bugeaud and Laurent (2023) Y. Bugeaud and M. Laurent. Combinatorial structure of Sturmian words and continued fraction expansion of Sturmian numbers. *Ann. Inst. Fourier (Grenoble)*, 73(5):2029–2078, 2023. ISSN 0373-0956. URL [https://doi.org/10.5802/aif.3561][7].
- Christoffel (1875) E. B. Christoffel. Observatio arithmetica. *Annali di Matematica Pura ed Applicata*, 6:145–152, 1875.
- Cohn (1985) P. M. Cohn. *Free rings and their relations*, volume 19 of *London Mathematical Society Monographs*. Academic Press, Inc. [Harcourt Brace Jovanovich, Publishers], London, second edition, 1985. ISBN 0-12-179152-1.
- Currie and Saari (2009) J. D. Currie and K. Saari. Least periods of factors of infinite words. *Theor. Inform. Appl.*, 43(1):165–178, 2009. ISSN 0988-3754. URL [https://doi.org/10.1051/ita:2008006][8].
- de Luca (1997) A. de Luca. Sturmian words: structure, combinatorics, and their arithmetics. *Theoret. Comput. Sci.*, 183(1):45–82, 1997. ISSN 0304-3975. URL [https://doi.org/10.1016/S0304-3975(96)00310-6][9].
- de Luca and Mignosi (1994) A. de Luca and F. Mignosi. Some combinatorial properties of Sturmian words. *Theoret. Comput. Sci.*, 136(2):361–385, 1994. ISSN 0304-3975. URL [https://doi.org/10.1016/0304-3975(94)00035-H][10].
- Dupain (1979) Y. Dupain. Discrépance de la suite ( { n ​ α }) (\{n\alpha\}), α = ( 1 + 5) / 2 \alpha=(1+\surd 5)/2. *Ann. Inst. Fourier (Grenoble)*, 29(1):xiv, 81–106, 1979. ISSN 0373-0956. URL [https://doi.org/10.5802/aif.728][11].
- Epifanio et al. (2007) C. Epifanio, F. Mignosi, J. Shallit, and I. Venturini. On Sturmian graphs. *Discrete Appl. Math.*, 155(8):1014–1030, 2007. ISSN 0166-218X. URL [https://doi.org/10.1016/j.dam.2006.11.003][12].
- Epifanio et al. (2012) C. Epifanio, C. Frougny, A. Gabriele, F. Mignosi, and J. Shallit. Sturmian graphs and integer representations over numeration systems. *Discrete Appl. Math.*, 160(4-5):536–547, 2012. ISSN 0166-218X. URL [https://doi.org/10.1016/j.dam.2011.10.029][13].
- Ferenczi and Zamboni (2013) S. Ferenczi and L. Q. Zamboni. Clustering words and interval exchanges. *J. Integer Seq.*, 16(2):Article 13.2.1, 9, 2013.
- Fogg (2002) N. P. Fogg. *Substitutions in dynamics, arithmetics and combinatorics*, volume 1794 of *Lecture Notes in Mathematics*. Springer-Verlag, Berlin, 2002. ISBN 3-540-44141-7. URL [https://doi.org/10.1007/b13861][14]. Edited by V. Berthé, S. Ferenczi, C. Mauduit and A. Siegel.
- Fraenkel (1985) A. S. Fraenkel. Systems of numeration. *Amer. Math. Monthly*, 92(2):105–114, 1985. ISSN 0002-9890. URL [https://doi.org/10.2307/2322638][15].
- Frid (2018) A. E. Frid. Sturmian numeration systems and decompositions to palindromes. *European J. Combin.*, 71:202–212, 2018. ISSN 0195-6698. URL [https://doi.org/10.1016/j.ejc.2018.04.003][16].
- Frobenius (1913) G. F. Frobenius. über die markoffschen zahlen. *Sitzungsberichte der Königlich Preussischen Akademie der Wissenschaften zu Berlin*, 26:458–487, 1913.
- Gabric et al. (2021) D. Gabric, N. Rampersad, and J. Shallit. An inequality for the number of periods in a word. *Internat. J. Found. Comput. Sci.*, 32(5):597–614, 2021. ISSN 0129-0541. URL [https://doi.org/10.1142/S0129054121410094][17].
- Graham et al. (1989) R. L. Graham, D. E. Knuth, and O. Patashnik. *Concrete mathematics*. Addison-Wesley Publishing Company, Advanced Book Program, Reading, MA, 1989. ISBN 0-201-14236-8. A foundation for computer science.
- Hegedüs and Nagy (2016) L. Hegedüs and B. Nagy. On periodic properties of circular words. *Discrete Math.*, 339(3):1189–1197, 2016. ISSN 0012-365X. URL [https://doi.org/10.1016/j.disc.2015.10.043][18].
- Kassel and Reutenauer (2007) C. Kassel and C. Reutenauer. Sturmian morphisms, the braid group B 4 B_{4}, Christoffel words and bases of F 2 F_{2}. *Ann. Mat. Pura Appl. (4)*, 186(2):317–339, 2007. ISSN 0373-3114. URL [https://doi.org/10.1007/s10231-006-0008-z][19].
- Lapointe (2017) M. Lapointe. Study of Christoffel classes: normal form and periodicity. In *Combinatorics on words*, volume 10432 of *Lecture Notes in Comput. Sci.*, pages 109–120. Springer, Cham, 2017. URL [https://doi.org/10.1007/978-3-319-66396-8_11][20].
- Lothaire (2002) M. Lothaire. *Algebraic combinatorics on words*, volume 90 of *Encyclopedia of Mathematics and its Applications*. Cambridge University Press, Cambridge, 2002. ISBN 0-521-81220-8. URL [https://doi.org/10.1017/CBO9781107326019][21]. A collective work by Jean Berstel, Dominique Perrin, Patrice Seebold, Julien Cassaigne, Aldo De Luca, Steffano Varricchio, Alain Lascoux, Bernard Leclerc, Jean-Yves Thibon, Veronique Bruyere, Christiane Frougny, Filippo Mignosi, Antonio Restivo, Christophe Reutenauer, Dominique Foata, Guo-Niu Han, Jacques Desarmenien, Volker Diekert, Tero Harju, Juhani Karhumaki and Wojciech Plandowski, With a preface by Berstel and Perrin.
- Mantaci et al. (2003) S. Mantaci, A. Restivo, and M. Sciortino. Burrows-Wheeler transform and Sturmian words. *Inform. Process. Lett.*, 86(5):241–246, 2003. ISSN 0020-0190. URL [https://doi.org/10.1016/S0020-0190(02)00512-4][22].
- Markoff (1879) A. Markoff. Sur les formes quadratiques binaires indéfinies. *Mathematische Annalen*, 15:381–496, 1879.
- Markoff (1880) A. Markoff. Sur les formes quadratiques binaires indéfinies (second mémoire). *Mathematische Annalen*, 17:379–399, 1880.
- Osborne and Zieschang (1981) R. P. Osborne and H. Zieschang. Primitives in the free group on two generators. *Invent. Math.*, 63(1):17–24, 1981. ISSN 0020-9910. URL [https://doi.org/10.1007/BF01389191][23].
- Ostrowski (1922) A. Ostrowski. Bemerkungen zur Theorie der Diophantischen Approximationen. *Abh. Math. Sem. Univ. Hamburg*, 1(1):77–98, 1922. ISSN 0025-5858. URL [https://doi.org/10.1007/BF02940581][24].
- Pirillo (1999) G. Pirillo. A new characteristic property of the palindrome prefixes of a standard Sturmian word. *Sém. Lothar. Combin.*, 43:Art. B43f, 3, 1999.
- Rauzy (1985) G. Rauzy. Mots infinis en arithmétique. In *Automata on infinite words (Le Mont-Dore, 1984)*, volume 192 of *Lecture Notes in Comput. Sci.*, pages 165–171. Springer, Berlin, 1985.
- Restivo and Rosone (2011) A. Restivo and G. Rosone. Balancing and clustering of words in the Burrows-Wheeler transform. *Theoret. Comput. Sci.*, 412(27):3019–3032, 2011. ISSN 0304-3975. URL [https://doi.org/10.1016/j.tcs.2010.11.040][25].
- Reutenauer (2019) C. Reutenauer. *From Christoffel words to Markoff numbers*. Oxford University Press, Oxford, 2019. ISBN 978-0-19-882754-2.
- Reutenauer (2021) C. Reutenauer. On quadratic numbers and forms, and Markoff theory. *J. Number Theory*, 227:265–305, 2021. ISSN 0022-314X. URL [https://doi.org/10.1016/j.jnt.2021.03.005][26].
- Simpson and Puglisi (2008) J. Simpson and S. J. Puglisi. Words with simple Burrows-Wheeler transforms. *Electron. J. Combin.*, 15(1):Research Paper 83, 17, 2008. URL [https://doi.org/10.37236/807][27].
- Smith (1876) H. Smith. Note on continued fractions. *Messenger of Mathematics*, 6:1–14, 1876.

*


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: https://doi.org/10.1007/978-3-319-00888-2
[4]: https://doi.org/10.1017/CBO9780511546563
[5]: https://doi.org/10.1090/crmm/027
[6]: https://doi.org/10.1145/28869.28873
[7]: https://doi.org/10.5802/aif.3561
[8]: https://doi.org/10.1051/ita:2008006
[9]: https://doi.org/10.1016/S0304-3975(96)00310-6
[10]: https://doi.org/10.1016/0304-3975(94)00035-H
[11]: https://doi.org/10.5802/aif.728
[12]: https://doi.org/10.1016/j.dam.2006.11.003
[13]: https://doi.org/10.1016/j.dam.2011.10.029
[14]: https://doi.org/10.1007/b13861
[15]: https://doi.org/10.2307/2322638
[16]: https://doi.org/10.1016/j.ejc.2018.04.003
[17]: https://doi.org/10.1142/S0129054121410094
[18]: https://doi.org/10.1016/j.disc.2015.10.043
[19]: https://doi.org/10.1007/s10231-006-0008-z
[20]: https://doi.org/10.1007/978-3-319-66396-8_11
[21]: https://doi.org/10.1017/CBO9781107326019
[22]: https://doi.org/10.1016/S0020-0190(02)00512-4
[23]: https://doi.org/10.1007/BF01389191
[24]: https://doi.org/10.1007/BF02940581
[25]: https://doi.org/10.1016/j.tcs.2010.11.040
[26]: https://doi.org/10.1016/j.jnt.2021.03.005
[27]: https://doi.org/10.37236/807
