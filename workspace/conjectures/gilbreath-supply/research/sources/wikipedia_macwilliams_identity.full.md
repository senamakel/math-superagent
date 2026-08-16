<!-- source: https://en.wikipedia.org/wiki/MacWilliams_identity | converted from HTML -->

Enumerator polynomial - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

(Redirected from [MacWilliams identity][1])

Specifies the number of words of a binary linear code of each possible Hamming weight

In [coding theory][2], the **weight enumerator polynomial**of a binary [linear code][3] specifies the number of words of each possible [Hamming weight][4].

Let C ⊂ F 2 n {\displaystyle C\subset \mathbb {F} _{2}^{n}}[image: {\displaystyle C\subset \mathbb {F} _{2}^{n}}] be a binary linear code of length n {\displaystyle n}[image: {\displaystyle n}]. The **weight distribution**is the sequence of numbers

A t = #{ c ∈ C ∣ w ( c) = t } {\displaystyle A_{t}=\#\{c\in C\mid w(c)=t\}}[image: {\displaystyle A_{t}=\#\{c\in C\mid w(c)=t\}}]

giving the number of codewords *c*in *C*having weight *t*as *t*ranges from 0 to *n*. The **weight enumerator**is the bivariate [polynomial][5]

W ( C; x, y) = ∑ w = 0 n A w x w y n − w. {\displaystyle W(C;x,y)=\sum _{w=0}^{n}A_{w}x^{w}y^{n-w}.}[image: {\displaystyle W(C;x,y)=\sum _{w=0}^{n}A_{w}x^{w}y^{n-w}.}]

## Basic properties

[[edit][6]]

1. W ( C; 0, 1) = A 0 = 1 {\displaystyle W(C;0,1)=A_{0}=1}[image: {\displaystyle W(C;0,1)=A_{0}=1}]
2. W ( C; 1, 1) = ∑ w = 0 n A w = | C | {\displaystyle W(C;1,1)=\sum _{w=0}^{n}A_{w}=|C|}[image: {\displaystyle W(C;1,1)=\sum _{w=0}^{n}A_{w}=|C|}]
3. W ( C; 1, 0) = A n = 1 if ( 1, …, 1) ∈ C and 0 otherwise {\displaystyle W(C;1,0)=A_{n}=1{\mbox{ if }}(1,\ldots ,1)\in C\ {\mbox{ and }}0{\mbox{ otherwise}}}[image: {\displaystyle W(C;1,0)=A_{n}=1{\mbox{ if }}(1,\ldots ,1)\in C\ {\mbox{ and }}0{\mbox{ otherwise}}}]
4. W ( C; 1, − 1) = ∑ w = 0 n A w ( − 1) n − w = A n + ( − 1) 1 A n − 1 + … + ( − 1) n − 1 A 1 + ( − 1) n A 0 {\displaystyle W(C;1,-1)=\sum _{w=0}^{n}A_{w}(-1)^{n-w}=A_{n}+(-1)^{1}A_{n-1}+\ldots +(-1)^{n-1}A_{1}+(-1)^{n}A_{0}}[image: {\displaystyle W(C;1,-1)=\sum _{w=0}^{n}A_{w}(-1)^{n-w}=A_{n}+(-1)^{1}A_{n-1}+\ldots +(-1)^{n-1}A_{1}+(-1)^{n}A_{0}}]

## MacWilliams identity

[[edit][7]]

Denote the [dual code][8] of C ⊂ F 2 n {\displaystyle C\subset \mathbb {F} _{2}^{n}}[image: {\displaystyle C\subset \mathbb {F} _{2}^{n}}] by

C ⊥ = { x ∈ F 2 n ∣ ⟨ x, c ⟩ = 0 ∀ c ∈ C } {\displaystyle C^{\perp }=\{x\in \mathbb {F} _{2}^{n}\,\mid \,\langle x,c\rangle =0{\mbox{ }}\forall c\in C\}}[image: {\displaystyle C^{\perp }=\{x\in \mathbb {F} _{2}^{n}\,\mid \,\langle x,c\rangle =0{\mbox{  }}\forall c\in C\}}]

(where ⟨, ⟩ {\displaystyle \langle \ ,\ \rangle }[image: {\displaystyle \langle \ ,\ \rangle }] denotes the vector [dot product][9] and which is taken over F 2 {\displaystyle \mathbb {F} _{2}}[image: {\displaystyle \mathbb {F} _{2}}]).

The **MacWilliams identity**states that

W ( C ⊥; x, y) = 1 ∣ C ∣ W ( C; y − x, y + x). {\displaystyle W(C^{\perp };x,y)={\frac {1}{\mid C\mid }}W(C;y-x,y+x).}[image: {\displaystyle W(C^{\perp };x,y)={\frac {1}{\mid C\mid }}W(C;y-x,y+x).}]

The identity is named after [Jessie MacWilliams][10].

## Distance enumerator

[[edit][11]]

The **distance distribution**or **inner distribution**of a code *C*of size *M*and length *n*is the sequence of numbers

A i = 1 M #{ ( c 1, c 2) ∈ C × C ∣ d ( c 1, c 2) = i } {\displaystyle A_{i}={\frac {1}{M}}\#\left\lbrace (c_{1},c_{2})\in C\times C\mid d(c_{1},c_{2})=i\right\rbrace }[image: {\displaystyle A_{i}={\frac {1}{M}}\#\left\lbrace (c_{1},c_{2})\in C\times C\mid d(c_{1},c_{2})=i\right\rbrace }]

where *i*ranges from 0 to *n*. The **distance enumerator polynomial**is

A ( C; x, y) = ∑ i = 0 n A i x i y n − i {\displaystyle A(C;x,y)=\sum _{i=0}^{n}A_{i}x^{i}y^{n-i}}[image: {\displaystyle A(C;x,y)=\sum _{i=0}^{n}A_{i}x^{i}y^{n-i}}]

and when *C*is linear this is equal to the weight enumerator.

The **outer distribution**of *C*is the 2*n*-by-*n*+1 matrix *B*with rows indexed by elements of GF(2)*n*and columns indexed by integers 0...*n*, and entries

B x, i = #{ c ∈ C ∣ d ( c, x) = i }. {\displaystyle B_{x,i}=\#\left\lbrace c\in C\mid d(c,x)=i\right\rbrace .}[image: {\displaystyle B_{x,i}=\#\left\lbrace c\in C\mid d(c,x)=i\right\rbrace .}]

The sum of the rows of *B*is *M*times the inner distribution vector (*A*0,...,*A**n*).

A code *C*is **regular**if the rows of *B*corresponding to the codewords of *C*are all equal.

## References

[[edit][12]]

- Hill, Raymond (1986). **[A first course in coding theory][13]. Oxford Applied Mathematics and Computing Science Series. [Oxford University Press][14]. pp. [165–173][15]. [ISBN][16] [0-19-853803-0][17].
- [Pless, Vera][18] (1982). **[Introduction to the theory of error-correcting codes][19]. Wiley-Interscience Series in Discrete Mathematics. [John Wiley & Sons][20]. pp. 103– 119. [ISBN][16] [0-471-08684-3][21].
- J.H. van Lint (1992). **[Introduction to Coding Theory][22]. [GTM][23]. Vol. 86 (2nd ed.). [Springer-Verlag][24]. [ISBN][16] [3-540-54894-7][25]. Chapters 3.5 and 4.3.

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Enumerator_polynomial&oldid=1362628453#MacWilliams_identity][26] "

[Categories][27]:

- [Coding theory][28]
- [Error detection and correction][29]
- [Mathematical identities][30]
- [Polynomials][31]

Hidden categories:

- [Articles with short description][32]
- [Short description matches Wikidata][33]

Search

Enumerator polynomial

1 language Add topic


## Links

[1]: /w/index.php?title=MacWilliams_identity&amp;redirect=no
[2]: https://en.wikipedia.org/wiki/Coding_theory
[3]: https://en.wikipedia.org/wiki/Linear_code
[4]: https://en.wikipedia.org/wiki/Hamming_weight
[5]: https://en.wikipedia.org/wiki/Polynomial
[6]: /w/index.php?title=Enumerator_polynomial&amp;action=edit&amp;section=1
[7]: /w/index.php?title=Enumerator_polynomial&amp;action=edit&amp;section=2
[8]: https://en.wikipedia.org/wiki/Dual_code
[9]: https://en.wikipedia.org/wiki/Dot_product
[10]: https://en.wikipedia.org/wiki/Jessie_MacWilliams
[11]: /w/index.php?title=Enumerator_polynomial&amp;action=edit&amp;section=3
[12]: /w/index.php?title=Enumerator_polynomial&amp;action=edit&amp;section=4
[13]: https://archive.org/details/firstcourseincod0000hill
[14]: https://en.wikipedia.org/wiki/Oxford_University_Press
[15]: https://archive.org/details/firstcourseincod0000hill/page/165
[16]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[17]: https://en.wikipedia.org/wiki/Special:BookSources/0-19-853803-0
[18]: https://en.wikipedia.org/wiki/Vera_Pless
[19]: https://en.wikipedia.org/wiki/Introduction_to_the_Theory_of_Error-Correcting_Codes
[20]: https://en.wikipedia.org/wiki/John_Wiley_&amp;_Sons
[21]: https://en.wikipedia.org/wiki/Special:BookSources/0-471-08684-3
[22]: https://archive.org/details/introductiontoco0000lint
[23]: https://en.wikipedia.org/wiki/Graduate_Texts_in_Mathematics
[24]: https://en.wikipedia.org/wiki/Springer-Verlag
[25]: https://en.wikipedia.org/wiki/Special:BookSources/3-540-54894-7
[26]: https://en.wikipedia.org/w/index.php?title=Enumerator_polynomial&amp;oldid=1362628453#MacWilliams_identity
[27]: /wiki/Help:Category
[28]: /wiki/Category:Coding_theory
[29]: /wiki/Category:Error_detection_and_correction
[30]: /wiki/Category:Mathematical_identities
[31]: /wiki/Category:Polynomials
[32]: /wiki/Category:Articles_with_short_description
[33]: /wiki/Category:Short_description_matches_Wikidata
