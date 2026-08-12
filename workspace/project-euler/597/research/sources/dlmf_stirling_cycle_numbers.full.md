<!-- source: https://dlmf.nist.gov/26.13 | converted from HTML -->

DLMF: §26.13 Permutations: Cycle Notation ‣ Properties ‣ Chapter 26 Combinatorial Analysis

[DLMF][1]

[About the Project][2]

[26 Combinatorial Analysis][3] [Properties][4] [26.12 Plane Partitions][5] [26.14 Permutations: Order Notation][6]

# §26.13 Permutations: Cycle Notation

ⓘ

Defines: 𝔖 n: set of permutations of { 1, 2, …, n } Keywords: [Stirling cycle numbers][7], [adjacent transposition][8], [cycle notation][9], [derangement][10], [derangement number][11], [even or odd][12], [fixed points][13], [inversion numbers][14], [permutations][15], [sign][16], [transpositions][17] Notes: See Cameron ( [1994][18], pp. 77, 80–84) and Stanley ( [1997][19], pp. 20–21, 67). Referenced by: [§1.2(vi)][20], [§26.14(i)][21], [§26.15][22] Permalink: [http://dlmf.nist.gov/26.13][23] See also: Annotations for [Ch.26][24]

𝔖 n denotes the set of permutations of { 1, 2, …, n }. σ ∈ 𝔖 n is a one-to-one and onto mapping from { 1, 2, …, n } to itself. An explicit representation of σ can be given by the 2 × n matrix:

26.13.1 |  | [1 2 3 ⋯ n σ ⁡ ( 1) σ ⁡ ( 2) σ ⁡ ( 3) ⋯ σ ⁡ ( n)]. |  |

ⓘ

Symbols: [n: nonnegative integer][25] and [σ: permutation][26] Permalink: [http://dlmf.nist.gov/26.13.E1][27] Encodings: [TeX][28], [pMML][29], [png][30] See also: Annotations for [§26.13][31] and [Ch.26][24]

 |

In cycle notation, the elements in each cycle are put inside parentheses, ordered so that σ ⁡ ( j) immediately follows j or, if j is the last listed element of the cycle, then σ ⁡ ( j) is the first element of the cycle. The permutation

26.13.2 |  | [1 2 3 4 5 6 7 8 3 5 2 4 7 8 1 6] |  |

ⓘ

Referenced by: [§26.13][32], [§26.13][33], [§26.13][34] Permalink: [http://dlmf.nist.gov/26.13.E2][35] Encodings: [TeX][36], [pMML][37], [png][38] See also: Annotations for [§26.13][31] and [Ch.26][24]

 |

is ( 1, 3, 2, 5, 7) ⁢ ( 4) ⁢ ( 6, 8) in cycle notation. Cycles of length one are *fixed points*. They are often dropped from the cycle notation. In consequence, ( [26.13.2][39]) can also be written as ( 1, 3, 2, 5, 7) ⁢ ( 6, 8).

An element of 𝔖 n with a 1 fixed points, a 2 cycles of length 2, …, a n cycles of length n, where n = a 1 + 2 ⁢ a 2 + ⋯ + n ⁢ a n, is said to have *cycle type*( a 1, a 2, …, a n). The number of elements of 𝔖 n with cycle type ( a 1, a 2, …, a n) is given by ( [26.4.7][40]).

The *Stirling cycle numbers*of the first kind, denoted by [n k], count the number of permutations of { 1, 2, …, n } with exactly k cycles. They are related to Stirling numbers of the first kind by

26.13.3 |  | [n k] = | s ⁡ ( n, k) |. |  |

ⓘ

Defines: [n k]: Stirling cycle number of the first kind Symbols: [s ⁡ ( n, k): Stirling number of the first kind][41], [k: nonnegative integer][25] and [n: nonnegative integer][25] Referenced by: [§4.13][42] Permalink: [http://dlmf.nist.gov/26.13.E3][43] Encodings: [TeX][44], [pMML][45], [png][46] See also: Annotations for [§26.13][31] and [Ch.26][24]

 |

See § [26.8][47] for generating functions, recurrence relations, identities, and asymptotic approximations.

A *derangement*is a permutation with no fixed points. The *derangement number*, d ⁡ ( n), is the number of elements of 𝔖 n with no fixed points:

26.13.4 |  | d ⁡ ( n) = n! ⁢ ∑ j = 0 n ( − 1) j ⁢ 1 j! = ⌊ n! + e − 2 e ⌋. |  |

ⓘ

Symbols: [e: base of natural logarithm][48], [!: factorial (as in n!)][49], [⌊ x ⌋: floor of x][50], [j: nonnegative integer][25], [n: nonnegative integer][25] and [d ⁡ ( n): derangement number][51] Permalink: [http://dlmf.nist.gov/26.13.E4][52] Encodings: [TeX][53], [pMML][54], [png][55] See also: Annotations for [§26.13][31] and [Ch.26][24]

 |

A *transposition*is a permutation that consists of a single cycle of length two. An *adjacent transposition*is a transposition of two consecutive integers. A permutation that consists of a single cycle of length k can be written as the composition of k − 1 two-cycles (read from right to left):

26.13.5 |  | ( j 1, j 2, …, j k) = ( j 1, j 2) ⁢ ( j 2, j 3) ⁢ ⋯ ⁢ ( j k − 2, j k − 1) ⁢ ( j k − 1, j k). |  |

ⓘ

Symbols: [( S): cycle][56], [j: nonnegative integer][25] and [k: nonnegative integer][25] Permalink: [http://dlmf.nist.gov/26.13.E5][57] Encodings: [TeX][58], [pMML][59], [png][60] See also: Annotations for [§26.13][31] and [Ch.26][24]

 |

Every permutation is a product of transpositions. A permutation with cycle type ( a 1, a 2, …, a n) can be written as a product of a 2 + 2 ⁢ a 3 + ⋯ + ( n − 1) ⁢ a n = n − ( a 1 + a 2 + ⋯ + a n) transpositions, and no fewer. For the example ( [26.13.2][39]), this decomposition is given by ( 1, 3, 2, 5, 7) ⁢ ( 6, 8) = ( 1, 3) ⁢ ( 2, 3) ⁢ ( 2, 5) ⁢ ( 5, 7) ⁢ ( 6, 8).

A permutation is *even*or *odd*according to the parity of the number of transpositions. The *sign of a permutation*is + if the permutation is even, − if it is odd.

Every transposition is the product of adjacent transpositions. If j < k, then ( j, k) is a product of 2 ⁢ k − 2 ⁢ j − 1 adjacent transpositions:

26.13.6 |  | ( j, k) = ( k − 1, k) ⁢ ( k − 2, k − 1) ⁢ ⋯ ⁢ ( j + 1, j + 2) ⁢ ( j, j + 1) ⁢ ( j + 1, j + 2) ⁢ ⋯ ⁢ ( k − 1, k). |  |

ⓘ

Symbols: [( S): cycle][56], [j: nonnegative integer][25] and [k: nonnegative integer][25] Permalink: [http://dlmf.nist.gov/26.13.E6][61] Encodings: [TeX][62], [pMML][63], [png][64] See also: Annotations for [§26.13][31] and [Ch.26][24]

 |

Every permutation is a product of adjacent transpositions. Given a permutation σ ∈ 𝔖 n, the *inversion number*of σ, denoted inv ( σ), is the least number of adjacent transpositions required to represent σ. Again, for the example ( [26.13.2][39]) a minimal decomposition into adjacent transpositions is given by ( 1, 3, 2, 5, 7) ⁢ ( 6, 8) = ( 2, 3) ⁢ ( 1, 2) ⁢ ( 4, 5) ⁢ ( 3, 4) ⁢ ( 2, 3) ⁢ ( 3, 4) ⁢ ( 4, 5) ⁢ ( 6, 7) ⁢ ( 5, 6) ⁢ ( 7, 8) ⁢ ( 6, 7): inv ( ( 1, 3, 2, 5, 7) ⁢ ( 6, 8)) = 11.

[26.12 Plane Partitions][5] [26.14 Permutations: Order Notation][6]

[© 2010–2026 NIST][65] / [Disclaimer][66] / [Feedback][67]; Version 1.2.7; Release date 2026-06-15.

[image: NIST] [68]

[Site Privacy][69] [Accessibility][70] [Privacy Program][71] [Copyrights][72] [Vulnerability Disclosure][73] [No Fear Act Policy][74] [FOIA][75] [Environmental Policy][76] [Scientific Integrity][77] [Information Quality Standards][78] [Commerce.gov][79] [Science.gov][80] [USA.gov][81]


## Links

[1]: ./
[2]: ./about/
[3]: ./26
[4]: ./26#PT2
[5]: ./26.12
[6]: ./26.14
[7]: ./search/search?q=Stirling%20cycle%20numbers
[8]: ./search/search?q=adjacent%20transposition
[9]: ./search/search?q=cycle%20notation
[10]: ./search/search?q=derangement
[11]: ./search/search?q=derangement%20number
[12]: ./search/search?q=even%20or%20odd
[13]: ./search/search?q=fixed%20points
[14]: ./search/search?q=inversion%20numbers
[15]: ./search/search?q=permutations
[16]: ./search/search?q=sign
[17]: ./search/search?q=transpositions
[18]: ./bib/C#bib405
[19]: ./bib/S#bib2157
[20]: ./1.2#Px11.p1
[21]: ./26.14#i.p1
[22]: ./26.15#p1
[23]: ./26.13
[24]: ./26#info
[25]: ./26.1#t1.r2
[26]: ./26.13#p1
[27]: ./26.13.E1
[28]: ./26.13.E1.tex
[29]: ./26.13.E1.pmml
[30]: ./26.13.E1.png
[31]: ./26.13#info
[32]: ./26.13#p10
[33]: ./26.13#p4
[34]: ./26.13#p8
[35]: ./26.13.E2
[36]: ./26.13.E2.tex
[37]: ./26.13.E2.pmml
[38]: ./26.13.E2.png
[39]: ./26.13#E2
[40]: ./26.4#E7
[41]: ./26.8#i.p1
[42]: ./4.13#p6
[43]: ./26.13.E3
[44]: ./26.13.E3.tex
[45]: ./26.13.E3.pmml
[46]: ./26.13.E3.png
[47]: ./26.8
[48]: ./4.2#E11
[49]: ./front/introduction#common.t1.r15
[50]: ./front/introduction#common.t1.r17
[51]: ./26.13#p7
[52]: ./26.13.E4
[53]: ./26.13.E4.tex
[54]: ./26.13.E4.pmml
[55]: ./26.13.E4.png
[56]: ./26.2#Px2
[57]: ./26.13.E5
[58]: ./26.13.E5.tex
[59]: ./26.13.E5.pmml
[60]: ./26.13.E5.png
[61]: ./26.13.E6
[62]: ./26.13.E6.tex
[63]: ./26.13.E6.pmml
[64]: ./26.13.E6.png
[65]: ./about/notices
[66]: ./about/notices#S2
[67]: /cdn-cgi/l/email-protection#e1a5adaca7cc878484858380828aa18f889295cf868e97
[68]: http://www.nist.gov/
[69]: https://www.nist.gov/privacy-policy
[70]: https://www.nist.gov/oism/accessibility
[71]: https://www.nist.gov/privacy
[72]: https://www.nist.gov/oism/copyrights
[73]: https://www.commerce.gov/vulnerability-disclosure-policy
[74]: https://www.nist.gov/no-fear-act-policy
[75]: https://www.nist.gov/foia
[76]: https://www.nist.gov/environmental-policy-statement
[77]: https://www.nist.gov/summary-report-scientific-integrity
[78]: https://www.nist.gov/nist-information-quality-standards
[79]: https://www.commerce.gov/
[80]: http://www.science.gov/
[81]: http://www.usa.gov/
