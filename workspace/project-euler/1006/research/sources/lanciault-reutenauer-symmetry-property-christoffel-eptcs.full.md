<!-- source: https://arxiv.org/html/2406.16408 | converted from HTML -->

A Symmetry Property of Christoffel Words

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2406.16408v1 [math.CO] 24 Jun 2024

# A Symmetry Property of Christoffel Words

Yan Lanciault Email: [lanciault.yan@courrier.uqam.ca][3] Affiliation: LACIM, Université du Québec à Montréal,
Montréal, Québec Christophe Reutenauer Thanks: Christophe Reutenauer was partially supported by NSERC Email: [reutenauer.christophe@uqam.ca][4] Affiliation: LACIM, Université du Québec à Montréal,
Montréal, Québec

###### Abstract

Motivated by the theory of trapezoidal words, whose sequences of cardinality of factors by length are symmetric, we introduce a bivariate variant of this symmetry. We show that this symmetry characterizes Christoffel words, and prove other related results.

## 1 Introduction

Trapezoidal words were considered by Aldo de Luca in [11]; for such a word, w w say, of length n n, the graph of the discrete function { 0, 1, …, n } → ℕ \{0,1,\ldots,n\}\to\mathbb{N}, giving the number of factors of length k k of w w is an isosceles trapezoid, with successive values 1, 2, …, J, J + 1, …, J + 1, J, …, 2, 1 1,2,\ldots,J,J+1,\ldots,J+1,J,\ldots,2,1. He showed that Sturmians words are trapezoidal, but the converse does not necessarily hold. The terminology “trapezoidal” was introduced by Flavio d’Alessandro in [8], who studied these words, giving in particular a condition for which a trapezoidal word is Sturmian. In [5], Michelangelo Bucci, Alessandro De Luca and Gabriele Fici gave many equivalent conditions for a word to be trapezoidal; one of them is that the number of factors of length k k is at most k + 1 k+1 (also see the work of Florence Levé and Patrice Séébold [10], and that of Mira-Cristiana Anisiu and Julien Cassaigne [2]). Remind that a factor of a word is a contiguous subword.

A remarkable property of trapezoidal words is, as mentioned above, that the sequence of the lengths of the factors of these words, from length 0 to length n n, is symmetric. We may call such a word factor-symmetric.

In the present work, we present a generalization of this symmetry property. Let w w be a word over the alphabet { a, b } \{a,b\}, with p p occurrences of the letter a a and q q occurrences of the letter b b; in other words, the Parikh image of w w is ( p, q) (p,q). We say that w w is strongly factor-symmetric if for any i, j i,j, w w has as many distinct factors with Parikh image ( i, j) (i,j) as distinct factors of Parikh image ( p − i, q − j) (p-i,q-j). Note that in that case, the notion of symmetry does not necessarily mean invariant under reversal.

We show that each Christoffel word is strongly factor-symmetric (Theorem 3.1). Conversely, each finite primitive Sturmian word which is strongly factor-symmetric is a Christoffel word (Theorem 3.2). Note that a ​ a ​ b ​ b aabb is strongly factor-symmetric, so that the hypothesis “Sturmian” is not superfluous.

These results are interesting, in part because one obtain a characterization of Christoffel words among all Sturmian words. Indeed, in the literature there exist many characterizations of conjugate of Christoffel words ( [7, 12, 4, 14, 13, 15]), which do not distinguish between Christoffel words and their conjugates. However, another notable charaterization of Christoffel words is that a Sturmian word is a Christoffel word if and only if it is a Lyndon word [3], if and only if it is unbordered [6] (see also [9]).

Concerning nonprimitive words, we show that if w w is a nontrivial power of a primitive word u u, then w w is strongly factor-symmetric if and only if u u is a Christoffel word (Theorem 3.3). The hypothesis “Sturmian” is not necessary here. In particular, ( a ​ a ​ b ​ b) 2 (aabb)^{2} is not strongly factor-symmetric.

As a byproduct, we obtain that, with the notation of the previous paragraph, that w w is factor-symmetric if and only if u u is the conjugate of some Christoffel word (Theorem 4.3).

Concerning the strong factor symmetry of a Christoffel word w w, we give an explicit bijection between the factors of w w of Parikh image ( i, j) (i,j) and those of Parikh image ( p − i, q − j) (p-i,q-j) (Theorem 4.1); it relies on the notion of attractor and circular attractor [13]. Moreover, the support of the function of pairs of integers that counts the numbers of factors of w w for each Parikh image, which is a subset of the discrete plane, is the set of integer points on the two paths defined by w w and its reversal w ~ \tilde{w}, and between them (Theorem 4.2): see, for example ( 1) and Figure 1.

This work was partially supported by NSERC, Canada.

## 2 Christoffel words and Sturmian words

Among several equivalent definitions of Christoffel words, we choose the following: a Christoffel word on the alphabet { a, b } \{a,b\} is either a a or b b, or a word of the form a ​ m ​ b amb or b ​ m ​ a bma, such that m m is a palindrome, and w w is a product of two palindromes. For other characterizations, see for example the book of the second author [14]. Christoffel words are primitive, that is, are not equal to a nontrivial power of another word.

It is known that the factorization into two palindromes is unique, and it is called the palindromic factorization.

Given a word w w, we define the function δ w: ℕ 2 → ℕ \delta_{w}:\mathbb{N}^{2}\to\mathbb{N} by δ w ​ ( i, j) = \delta_{w}(i,j)= the number of factors of w w whose Parikh image is ( i, j) (i,j). We say that a word w w of Parikh image ( p, q) (p,q) is strongly factor-symmetric if for any i, j i,j, δ w ​ ( i, j) = δ w ​ ( p − i, q − j) \delta_{w}(i,j)=\delta_{w}(p-i,q-j). For example, the distinct factors of the Christoffel word a ​ a ​ b ​ a ​ b aabab are 1, a, b, a ​ a, a ​ b, b ​ a, a ​ a ​ b, a ​ b ​ a, b ​ a ​ b, a ​ a ​ b ​ a, a ​ b ​ a ​ b, a ​ a ​ b ​ a ​ b 1,a,b,aa,ab,ba,aab,aba,bab,aaba,abab,aabab so that δ w \delta_{w} is represented by the array whose i, j i,j -coordinate is δ w ​ ( i, j) \delta_{w}(i,j) (coordinates are as in the Cartesian plane, and this array is embedded in the plane):

 | 0 1 1 1 1 2 2 1 1 1 1 0 \begin{array}[]{cccccc}0&1&1&1\\ 1&2&2&1\\ 1&1&1&0\end{array} |  | (1) |

This array has a central symmetry, which means that w w is strongly factor-symmetric. We call this array the factor array of w w.

A word w w is called factor-symmetric if the sequence of length of factors, which turns out to be ∑ i + j = k δ w ​ ( i, j) \sum_{i+j=k}\delta_{w}(i,j), k = 0, …, | w | k=0,\ldots,|w| is symmetric; in other words, w w has as many factors of length i i as factors of length n − i n-i, for all i i, with n = | w | n=|w|. Clearly, a strongly factor-symmetric word is factor-symmetric.

Trapezoidal words are factor-symmetric words ( [11] Proposition 4.7, [5] Definition 2.5); and conversely, each factor-symmetric word w w is trapezoidal: indeed, if | w | = n |w|=n, then w w has n − i + 1 n-i+1 occurrences of factors of length i i, so that it has at most n − i + 1 n-i+1 such factors; but the factor symmetry implies that it has at most n − i + 1 n-i+1 factors of length n − i n-i, and hence it is trapezoidal by the cited proposition.

## 3 Main results

###### Theorem 3.1.

Each Christoffel word is strongly factor-symmetric.

We have a converse. Note that a Sturmian word is a factor of a Christoffel word.

###### Theorem 3.2.

If the support of δ w \delta_{w} is symmetric (and in particular, if w w is strongly factor-symmetric) and if w w is primitive and Sturmian, then w w is a Christoffel word.

Note that the factor array of the word a ​ a ​ b ​ b aabb is

 | 1 1 1 1 1 1 1 1 1 \begin{array}[]{cccccc}1&1&1\\ 1&1&1\\ 1&1&1\end{array} |  |

which has a central symmetry, so that a ​ a ​ b ​ b aabb is strongly factor-symmetric; this word is not a Christoffel word, but is not Sturmian either, since a ​ a aa and b ​ b bb cannot be both factors of a Sturmian word.

###### Theorem 3.3.

Let w = u k w=u^{k}, u u primitive, k ≥ 2 k\geq 2. Then w w is strongly factor-symmetric if and only if u u is a Christoffel word.

Here, the hypothesis “factor-symmetric” suffices for the “only if” part. And the hypothesis “Sturmian” is no more necessary.

## 4 Byproducts

An attractor of a word w = w 1 ⋯ w n w=w_{1}\cdots w_{n}, with w i w_{i} letters of the alphabet, is a subset K K of { 1, ⋯, n } \{1,\cdots,n\} such that every factors of w w has an occurrence that meets one of the letters indexed by one of the numbers in K K. A circular attractor is defined similarly, but with the notion of circular factors, that is factors of a conjugate of w w. Using theses concepts, we have a bijection that explains Theorem 3.1.

###### Theorem 4.1.

Let w = u ​ v w=uv be a Christoffel word of length n n with its palindromic factorization. Suppose k, 0 ≤ k ≤ n k,0\leq k\leq n. Consider all factors of length k k of w w that intersect the cut of the factorization, and order them from left to right: f 1, f 2, …, f r f_{1},f_{2},\ldots,f_{r}. Consider all factors of length n − k n-k of w w that intersect this cut, and order them from right to left: g 1, g 2, …, g s g_{1},g_{2},\ldots,g_{s}. Then r = s r=s, the words f i f_{i} are distinct, the words g i g_{i} are distinct, and the mapping f i ↦ g i f_{i}\mapsto g_{i} is a bijection from the set of factors of length k k of w w to the set of factors of length n − k n-k of w w, which complements the Parikh image γ ⁡ ( w) \gamma(w) of w w; that is: γ ⁡ ( f i) + γ ⁡ ( g i) = γ ⁡ ( w) \gamma(f_{i})+\gamma(g_{i})=\gamma(w).

An example: let w = a ​ a ​ b ​ a ​ b ​ a ​ b w=aababab, u ⋅ v = a ​ a ⋅ b ​ a ​ b ​ a ​ b u\cdot v=aa\cdot babab, k = 4 k=4, f 1 = a ​ a ​ b ​ a, f 2 = a ​ b ​ a ​ b, f 3 = b ​ a ​ b ​ a f_{1}=aaba,f_{2}=abab,f_{3}=baba, g 1 = b ​ a ​ b, g 2 = a ​ b ​ a, g 3 = a ​ a ​ b g_{1}=bab,g_{2}=aba,g_{3}=aab.

In the following, with each word on the alphabet { a, b } \{a,b\}, we associate the path in the discrete plane starting from the origin, where a a represents an horizontal step towards East, and b b a vertical step towards North.

###### Theorem 4.2.

Let w w be a lower Christoffel word, w ~ \tilde{w} the corresponding upper Christoffel word, and S w S_{w} the set of integer points on the paths corresponding to w w and w ~ \tilde{w}. Then S w S_{w} is the support of the function δ w \delta_{w}.

See for example Figure 1.

1 1 1 1 1 1 1 1 2 2 1 1 3 3 2 2 2 2 1 1 3 3 3 3 1 1 2 2 2 2 1 1 3 3 2 2 2 2 1 1 1 1 1 1 1 1 Figure 1: Paths of lower and upper Christoffel words w = a ​ a ​ b ​ a ​ a ​ b ​ a ​ a ​ b ​ a ​ b w=aabaabaabab and w ~ \tilde{w} and the function δ w \delta_{w}

###### Theorem 4.3.

Let w = u k w=u^{k}, u u primitive, k ≥ 2 k\geq 2. Then w w is factor-symmetric if and only if u u is the conjugate of some Christoffel word.

Open question: which primitive trapezoidal words are strongly factor-symmetric? We know that if a word is primitive, Sturmian, and strongly factor-symmetric, it must be a Christoffel word. Hence the question is really: which primitive trapezoidal words, that are not Sturmian, are strongly factor-symmetric? An example is the word a ​ a ​ b ​ b aabb. The work of [8] might help.

## 5 Sketch of proofs

Proving Theorem 3.1 amounts to proving that the bivariate (commutative) polynomial ∑ i, j δ w ​ ( i, j) ​ a i ​ b j ∈ ℕ ⁡ [a, b] \sum_{i,j}\delta_{w}(i,j)a^{i}b^{j}\in\mathbb{N}[a,b] is reciprocal, with an appropriate (but evident) definition of “reciprocal”. One shows that this property is preserved by product. Then one shows, using the notion of attractor and circular attractor [13] that the factors of w w, which intersect the cut in the palindromic factorization u ​ v uv of w w, are all the factors of w w; moreover they are distinct [4]. Hence the set of factors is the unambiguous product of the set of suffixes of u u by the set of prefixes of v v. Making the letters commute, the previous polynomial is the product of two polynomials; these are reciprocal, by palindromicity of u u and v v.

To prove Theorem 3.2, it is enough to prove that w w is unbordered. One show that w w has a nontrivial period p p if and only if the intersection of the support of δ w \delta_{w} and of the line of equation x + y = p x+y=p is a singleton. Hence, by symmetry of the support, if w w has this period, w w also has the period n − p n-p, hence is not primitive, by a Fine-Wilf lemma.

Let us sketch the proof of Theorem 3.3. Suppose that u u is a Christoffel word. Clearly, all circular factors of u u are factors of w w. An ad hoc construction then allows one to enumerate all factors of w w, relating them to the circular factors of u u, and implying that δ w \delta_{w} has the required symmetry.

Conversely, one shows that the hypothesis implies that u u has at most k + 1 k+1 circular factors of length k k, for k = 0, 1, …, | u | − 1 k=0,1,\ldots,|u|-1; being primitive, it must have exactly k + 1 k+1 factors. Hence u u is the conjugate of a Christoffel word. We conclude the result using periodicity as above.

For Theorem 4.1, a closer look at the combinatorics behind the algebraic proof using polynomials gives the bijection.

For Theorem 4.2, one notes that since w w is balanced, there at most two points in the intersection of the support of δ w \delta_{w} and the line of equation x + y = p x+y=p. One of them is given by the intersection of the lower path and the line, and corresponds to the prefix of length p p of w w. The other to the suffix of length p p of w w, since w = a ​ m ​ b w=amb, m m palindrome.

Finally, if w = u k w=u^{k} is factor symmetric, then one shows as above that u u is the conjugate of a Christoffel word. Conversely, each power of a conjugate of a Christoffel word is Sturmian, hence trapezoidal, hence factor-symmetric. This proves Theorem 4.3.

## References

- [1]
- [2] Mira-Cristiana Anisiu & Julien Cassaigne (2004): *Properties of the complexity function for finite words*. Rev. Anal. Numér. Théor. Approx. 33(2), pp. 123–139, [10.33993/jnaat332-767][5].
- [3] Jean Berstel & Aldo de Luca (1997): *Sturmian words, Lyndon words and trees*. Theoret. Comput. Sci. 178(1-2), pp. 171–203, [10.1016/S0304-3975(96)00101-6][6].
- [4] Jean-Pierre Borel & Christophe Reutenauer (2006): *On Christoffel classes*. Theor. Inform. Appl. 40(1), pp. 15–27, [10.1051/ita:2005038][7].
- [5] Michelangelo Bucci, Alessandro De Luca & Gabriele Fici (2013): *Enumeration and structure of trapezoidal words*. Theoret. Comput. Sci. 468, pp. 12–22, [10.1016/j.tcs.2012.11.007][8].
- [6] Wai-fong Chuan (1998): *Unbordered factors of the characteristic sequences of irrational numbers*. Theoret. Comput. Sci. 205(1-2), pp. 337–344, [10.1016/S0304-3975(98)00104-2][9].
- [7] Wai-Fong Chuan (1999): *Sturmian morphisms and α \alpha -words*. Theoret. Comput. Sci. 225(1-2), pp. 129–148, [10.1016/S0304-3975(97)00239-9][10].
- [8] Flavio D’Alessandro (2002): *A combinatorial problem on trapezoidal words*. Theoret. Comput. Sci. 273(1-2), pp. 11–33, [10.1016/S0304-3975(00)00431-X][11]. WORDS (Rouen, 1999).
- [9] Tero Harju & Dirk Nowotka (2004): *Minimal Duval extensions*. Internat. J. Found. Comput. Sci. 15(2), pp. 349–354, [10.1142/S0129054104002467][12].
- [10] Florence Levé & Patrice Séébold (2001): *Proof of a conjecture on word complexity*. Bull. Belg. Math. Soc. Simon Stevin 8(2), pp. 277–291, [10.36045/bbms/1102714173][13]. Available at [http://projecteuclid.org/euclid.bbms/1102714173][14]. Journées Montoises d’Informatique Théorique (Marne-la-Vallée, 2000).
- [11] Aldo de Luca (1999): *On the combinatorics of finite words*. Theoret. Comput. Sci. 218(1), pp. 13–39, [10.1016/S0304-3975(98)00248-5][15]. WORDS (Rouen, 1997).
- [12] S. Mantaci, A. Restivo & M. Sciortino (2003): *Burrows-Wheeler transform and Sturmian words*. Inform. Process. Lett. 86(5), pp. 241–246, [10.1016/S0020-0190(02)00512-4][16].
- [13] Sabrina Mantaci, Antonio Restivo, Giuseppe Romana, Giovanna Rosone & Marinella Sciortino (2021): *A combinatorial view on string attractors*. Theoret. Comput. Sci. 850, pp. 236–248, [10.1016/j.tcs.2020.11.006][17].
- [14] Christophe Reutenauer (2019): *From Christoffel words to Markoff numbers*. Oxford University Press, Oxford.
- [15] Christophe Reutenauer (2021): *Christoffel words and weak Markoff theory*. Adv. in Appl. Math. 127, pp. Paper No. 102179, 15, [10.1016/j.aam.2021.102179][18].


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:lanciault.yan@courrier.uqam.ca
[4]: mailto:reutenauer.christophe@uqam.ca
[5]: https://doi.org/10.33993/jnaat332-767
[6]: https://doi.org/10.1016/S0304-3975(96)00101-6
[7]: https://doi.org/10.1051/ita:2005038
[8]: https://doi.org/10.1016/j.tcs.2012.11.007
[9]: https://doi.org/10.1016/S0304-3975(98)00104-2
[10]: https://doi.org/10.1016/S0304-3975(97)00239-9
[11]: https://doi.org/10.1016/S0304-3975(00)00431-X
[12]: https://doi.org/10.1142/S0129054104002467
[13]: https://doi.org/10.36045/bbms/1102714173
[14]: http://projecteuclid.org/euclid.bbms/1102714173
[15]: https://doi.org/10.1016/S0304-3975(98)00248-5
[16]: https://doi.org/10.1016/S0020-0190(02)00512-4
[17]: https://doi.org/10.1016/j.tcs.2020.11.006
[18]: https://doi.org/10.1016/j.aam.2021.102179
