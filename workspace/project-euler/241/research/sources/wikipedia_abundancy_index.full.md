<!-- source: https://en.wikipedia.org/wiki/Abundancy_index | converted from HTML -->

Abundant number - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

(Redirected from [Abundancy index][1])

Number that is less than the sum of its proper divisors

[2] Demonstration, with [Cuisenaire rods][3], of the abundance of the number 12

In [number theory][4], an **abundant number**or **excessive number**is a [positive integer][5] for which the sum of its [proper divisors][6] is greater than the number. The integer 12 is the first abundant number: its proper divisors are 1, 2, 3, 4 and 6, and their sum 16 is larger than 12. The amount by which the sum exceeds the number is the **abundance**. The number 12 has an abundance of 4, for example.

## Definition and examples

[[edit][7]]

An *abundant number*is a [natural number][8]*n*for which the [sum of divisors][9]*σ*(*n*) satisfies 2''n''"}},"i":0}}]}'>*σ*(*n*) > 2*n*, or, equivalently, the sum of proper divisors (or [aliquot sum][10]) *s*(*n*) satisfies ''n''"}},"i":0}}]}'>*s*(*n*) > *n*. [1]: 84 [2]: 693 [3]: 273 [4]: 185 The *abundance*of a natural number is the [integer][11]*σ*(*n*) − *2n*(equivalently, *s*(*n*) − *n*). [5]

The abundant numbers smaller than 100 are

12, 18, 20, 24, 30, 36, 40, 42, 48, 54, 56, 60, 66, 70, 72, 78, 80, 84, 88, 90, and 96 (sequence [A005101][12] in the [OEIS][13]).

For example, the proper divisors of 24 are 1, 2, 3, 4, 6, 8, and 12, whose sum is 36. Because 36 is greater than 24, the number 24 is abundant, and its abundance is 36 − 24 = 12.

Numbers that are not abundant are either [perfect][14] (if *σ*(*n*) = 2*n*) or [deficient][15] (if *σ*(*n*) < 2*n*).

## Properties

[[edit][16]]

[17] Let a ( n) {\displaystyle a(n)}[image: {\displaystyle a(n)}] be the number of abundant numbers not exceeding n {\displaystyle n}[image: {\displaystyle n}]. Plot of a ( n) / n {\displaystyle a(n)/n}[image: {\displaystyle a(n)/n}] for n < 10 6 {\displaystyle n<10^{6}}[image: {\displaystyle n<10^{6}}] (with n {\displaystyle n}[image: {\displaystyle n}] log-scaled)

Every multiple of an abundant number is abundant. [2]: 695 [5] For example, every multiple of 20 (including 20 itself) is abundant because if n is a multiple of 20 then σ ( n) ≥ n 2 + n 4 + n 5 + n 10 + n 20 = n + n 10. {\displaystyle \sigma (n)\geq {\tfrac {n}{2}}+{\tfrac {n}{4}}+{\tfrac {n}{5}}+{\tfrac {n}{10}}+{\tfrac {n}{20}}=n+{\tfrac {n}{10}}.}[image: {\displaystyle \sigma (n)\geq {\tfrac {n}{2}}+{\tfrac {n}{4}}+{\tfrac {n}{5}}+{\tfrac {n}{10}}+{\tfrac {n}{20}}=n+{\tfrac {n}{10}}.}] Similarly, every multiple of a [perfect number][14] (except the perfect number itself) is abundant. [6]: 134 For example, every multiple n of 6 greater than 6 is abundant because σ ( n) ≥ 1 + n 2 + n 3 + n 6 = n + 1. {\displaystyle \sigma (n)\geq 1+{\tfrac {n}{2}}+{\tfrac {n}{3}}+{\tfrac {n}{6}}=n+1.}[image: {\displaystyle \sigma (n)\geq 1+{\tfrac {n}{2}}+{\tfrac {n}{3}}+{\tfrac {n}{6}}=n+1.}] An abundant number that is not the multiple of an abundant number or perfect number (i.e., whose proper divisors are all deficient) is called a [primitive abundant number][18].

Unlike for perfect numbers, [even and odd][19] abundant numbers are known to exist. The smallest odd abundant number is 945. [7] [3]: 199 Consequently, infinitely many abundant numbers exist with each [parity][20]. The smallest abundant number that is not divisible by 2 or by 3 is 5391411025; its distinct [prime factors][21] are 5, 7, 11, 13, 17, 19, 23, and 29. An algorithm given by Iannucci in 2005 shows how to find the smallest abundant number not divisible by the first *k*[primes][22] (sequence [A047802][23] in the [OEIS][13]). [8] If A ( k) {\displaystyle A(k)}[image: {\displaystyle A(k)}] represents the smallest abundant number not divisible by the first *k*primes then for all 0"}}'> 0}"> ϵ > 0 {\displaystyle \epsilon >0} 0}"/> we have ( 1 − ϵ) ( k ln ⁡ k) 2 − ϵ < ln ⁡ A ( k) < ( 1 + ϵ) ( k ln ⁡ k) 2 + ϵ {\displaystyle (1-\epsilon )(k\ln k)^{2-\epsilon }<\ln A(k)<(1+\epsilon )(k\ln k)^{2+\epsilon }}[image: {\displaystyle (1-\epsilon )(k\ln k)^{2-\epsilon }<\ln A(k)<(1+\epsilon )(k\ln k)^{2+\epsilon }}] for sufficiently large *k*.

The set of abundant numbers has a non-zero [natural density][24]: that is, as N grows large, the fraction of the natural numbers less than N that are abundant approaches a constant. This limiting fraction lies between 0.2476171 and 0.2476475. [9] [10] [11]

The first pair of consecutive abundant numbers is (5775, 5776), and the first consecutive triple is (171078830, 171078831, 171078832). [12] Let E ( n) {\displaystyle E(n)}[image: {\displaystyle E(n)}] be the length of the longest run of consecutive abundant numbers not exceeding n {\displaystyle n}[image: {\displaystyle n}]. [Paul Erdős][25] (1935) showed that there exists two constants c 1, c 2 {\displaystyle c_{1},c_{2}}[image: {\displaystyle c_{1},c_{2}}] such that c 1 log ⁡ log ⁡ log ⁡ n ≤ E ( n) ≤ c 2 log ⁡ log ⁡ log ⁡ n {\displaystyle c_{1}\log \log \log n\leq E(n)\leq c_{2}\log \log \log n}[image: {\displaystyle c_{1}\log \log \log n\leq E(n)\leq c_{2}\log \log \log n}] for all sufficiently large n {\displaystyle n}[image: {\displaystyle n}]. [13] As a matter of fact, the limit lim n → ∞ E ( n) log ⁡ log ⁡ log ⁡ n {\displaystyle \lim _{n\to \infty }{\dfrac {E(n)}{\log \log \log n}}}[image: {\displaystyle \lim _{n\to \infty }{\dfrac {E(n)}{\log \log \log n}}}] exists, with value lying between 3.24 and 3.54. [14]

Every [integer][11] greater than 20161 can be written as the sum of two abundant numbers. [3]: 273 The largest even number that is not the sum of two abundant numbers is 46. [15]

## Related concepts

[[edit][26]]

[27] [Euler diagram][28] of numbers under 100:

**Abundant**

[Primitive abundant][18]

[Highly abundant][29]

[Superabundant][30] and [highly composite][31]

[Colossally abundant][32] and [superior highly composite][33]

[Weird][34]

[Perfect][14]

[Composite][35]

[Deficient][15]

Numbers whose sum of proper factors equals the number itself (such as 6 and 28) are called [perfect numbers][14], [4]: 11 [1]: 84 while numbers whose sum of proper factors is less than the number itself are called [deficient numbers][15]. [4]: 185 [1]: 84 The first known classification of numbers as deficient, perfect or abundant was by [Nicomachus][36] in his *[Introductio Arithmetica][37]*(ca. 100 CE) and by [Theon of Smyrna][38] in his *On Mathematics Useful for the Understanding of Plato*(ca. 100 CE). [16]: 74 [6]: 128

The **abundancy index**of n is the ratio *σ*(*n*)/*n*. [1]: 84 A number whose abundancy index is greater than any lower number is called a [superabundant number][30] (sequence [A004394][39] in the [OEIS][13]). [1]: 88 Distinct numbers *n*1, *n*2, ... (whether abundant or not) with the same abundancy index are called [friendly numbers][40].

The sequence (*a**k*) of least numbers *n*such that *σ*(*n*) > *kn*, in which *a*2 = 12 corresponds to the first abundant number, grows very quickly (sequence [A134716][41] in the [OEIS][13]). The smallest odd integer with abundancy index exceeding 3 is 1018976683725 = 3 3 × 5 2 × 7 2 × 11 × 13 × 17 × 19 × 23 × 29. [17]

If **p**= (*p*1, ..., *p n*) is a list of primes, then **p**is termed *abundant*if some integer composed only of primes in **p**is abundant. A necessary and sufficient condition for this is that the product of the numbers p k p k − 1 {\displaystyle {\frac {p_{k}}{p_{k}-1}}}[image: {\displaystyle {\frac {p_{k}}{p_{k}-1}}}] be larger than 2. [18]

A number n for which the sum of its divisors (including itself) is greater than the sum of the divisors of any smaller natural number is called a [highly abundant number][29].

An abundant number which is not a [semiperfect number][42] is called a [weird number][34]. [6]: 144 An abundant number with abundance 1 is called a [quasiperfect number][43]; it is not known whether any quasiperfect numbers exist.

## References

[[edit][44]]

\n {{cite book\n | author = Shyam Sunder Gupta\n | doi = 10.1007/978-981-97-2465-9\n | isbn = 978-981-97-2465-9\n | publisher = Springer Nature Singapore Pte Ltd.\n | title = Exploring the Beauty of Fascinating Numbers\n | year = 2025\n }}\n </ref>\n <ref name=\"heath1921\">\n {{cite book\n | author = Heath, Thomas\n | publisher = Oxford University Press\n | title = A History of Greek Mathematics\n | volume = 1\n | url = https://archive.org/details/historyofgreekm01heat\n | year = 1921\n }}\n </ref>\n <ref name=\"laatsch1986\">\n {{cite journal\n | doi=10.2307/2690424\n | first=Richard\n | issn=0025-570X\n | journal=[[Mathematics Magazine]]\n | jstor=2690424\n | last=Laatsch\n | mr=0835144\n | number=2\n | pages=84–92\n | title=Measuring the abundancy of integers\n | volume=59\n | year=1986\n | zbl=0601.10003\n }}\n </ref>\n <ref name=\"prielipp1970\">\n {{cite journal\n | author = Prielipp, Robert W.\n | issue = 8\n | journal = The Mathematics Teacher\n | title = Perfect Numbers, Abundant Numbers, and Deficient Numbers\n | url = https://www.jstor.org/stable/27958492\n | volume = 63\n | year = 1970\n }}\n </ref>\n <ref name=\"roberts1992\">\n {{cite book\n | author = Roberts, Joe\n | isbn = 0-88385-502-X\n | publisher = The Mathematical Association of America (Incorporated)\n | title = Lure of Integers\n | year = 1992\n }}\n </ref>\n <ref name=\"tattersall2005\">\n {{cite book\n | edition = 2nd\n | first = James J.\n | isbn = 978-0-511-06583-5\n | last = Tattersall\n | publisher = [[Cambridge University Press]]\n | title = Elementary Number Theory in Nine Chapters\n | url = https://www.cambridge.org/9780521585033\n | year = 2005\n | zbl = 1071.11002\n }}\n </ref>\n <ref name=\"wolfram\">\n {{cite web\n | access-date = 21 May 2026\n | title = Abundant Number\n | url = https://mathworld.wolfram.com/AbundantNumber.html\n }}\n </ref>"}},"i":0}}]}'>

1. 1 2 3 4 5 Laatsch, Richard (1986). "Measuring the abundancy of integers". *[Mathematics Magazine][45]*. **59**(2): 84– 92. [doi][46]: [10.2307/2690424][47]. [ISSN][48] [0025-570X][49]. [JSTOR][50] [2690424][51]. [MR][52] [0835144][53]. [Zbl][54] [0601.10003][55].
2. 1 2 Prielipp, Robert W. (1970). ["Perfect Numbers, Abundant Numbers, and Deficient Numbers"][56]. *The Mathematics Teacher*. **63**(8).
3. 1 2 3 Roberts, Joe (1992). *Lure of Integers*. The Mathematical Association of America (Incorporated). [ISBN][57] [0-88385-502-X][58].
4. 1 2 3 Shyam Sunder Gupta (2025). *Exploring the Beauty of Fascinating Numbers*. Springer Nature Singapore Pte Ltd. [doi][46]: [10.1007/978-981-97-2465-9][59]. [ISBN][57] [978-981-97-2465-9][60].
5. 1 2 ["Abundant Number"][61]. Retrieved 21 May 2026.
6. 1 2 3 Tattersall, James J. (2005). **[Elementary Number Theory in Nine Chapters][62] (2nd ed.). [Cambridge University Press][63]. [ISBN][57] [978-0-511-06583-5][64]. [Zbl][54] [1071.11002][65].
7. ↑ [Sloane, N. J. A.][66] (ed.). ["Sequence A005231 (Odd abundant numbers (odd numbers m whose sum of divisors exceeds 2m).)"][67]. *The [On-Line Encyclopedia of Integer Sequences][13]*. OEIS Foundation.
8. ↑ D. Iannucci (2005), **["On the smallest abundant number not divisible by the first k primes"][68], *[Bulletin of the Belgian Mathematical Society][69]*, **12**(1): 39– 44, [doi][46]: [10.36045/bbms/1113318127][70]
9. ↑ Hall, Richard R.; [Tenenbaum, Gérald][71] (1988). *Divisors*. Cambridge Tracts in Mathematics. Vol. 90. Cambridge: [Cambridge University Press][63]. p. 95. [ISBN][57] [978-0-521-34056-4][72]. [Zbl][54] [0653.10001][73].
10. ↑ Deléglise, Marc (1998). ["Bounds for the density of abundant integers"][74]. *Experimental Mathematics*. **7**(2): 137– 143. [CiteSeerX][75] [10.1.1.36.8272][76]. [doi][46]: [10.1080/10586458.1998.10504363][77]. [ISSN][48] [1058-6458][78]. [MR][52] [1677091][79]. [Zbl][54] [0923.11127][80].`{{ [cite journal][81] }}`: Cite uses deprecated parameter `| citeseerx=`( [help][82])
11. ↑ Kobayashi, Mitsuo (2010), ["On the density of abundant numbers"][83], *Dartmouth Dissertations*: 1– 239, [doi][46]: [10.1349/ddlp.1662][84]
12. ↑ [Sloane, N. J. A.][66] (ed.). ["Sequence A094268"][85]. *The [On-Line Encyclopedia of Integer Sequences][13]*. OEIS Foundation.
13. ↑ Erdős, Paul (1935), ["Note on consecutive abundant numbers"][86] (PDF), *Journal of the London Mathematical Society*, **10**: 128– 131
14. ↑ Chen, Yong-Gao; Lv, Hui (2016), **[On consecutive abundant numbers][87]
15. ↑ [Sloane, N. J. A.][66] (ed.). ["Sequence A048242 (Numbers that are not the sum of two abundant numbers)"][88]. *The [On-Line Encyclopedia of Integer Sequences][13]*. OEIS Foundation.
16. ↑ Heath, Thomas (1921). **[A History of Greek Mathematics][89]. Vol. 1. Oxford University Press.
17. ↑ For smallest odd integer *k*with abundancy index exceeding *n*, see = n."}},"i":0}}]}'/> [Sloane, N. J. A.][66] (ed.). **["Sequence A119240 (Least odd number k such that sigma(k)/k >= n.)"][90]. *The [On-Line Encyclopedia of Integer Sequences][13]*. OEIS Foundation.
18. ↑ Friedman, Charles N. (1993). ["Sums of divisors and Egyptian fractions"][91]. *[Journal of Number Theory][92]*. **44**(3): 328– 339. [doi][46]: [10.1006/jnth.1993.1057][91]. [MR][52] [1233293][93]. [Zbl][54] [0781.11015][94].

## External links

[[edit][95]]

- [The Prime Glossary: Abundant number][96]
- [Abundant number][97] at [PlanetMath][98].

- [v][99]
- [t][100]
- [e][101]

Divisibility-based sets of integers

 |

Overview |

- [Integer factorization][102]
- [Divisor][103]
- [Unitary divisor][104]
- [Divisor function][9]
- [Prime factor][21]
- [Fundamental theorem of arithmetic][105]

 |

[image: Divisibility of 60] [106]

 |

Factorization forms |

- [Prime][22]
- [Composite][35]
- [Semiprime][107]
- [Pronic][108]
- [Sphenic][109]
- [Square-free][110]
- [Powerful][111]
- [Perfect power][112]
- [Achilles][113]
- [Smooth][114]
- [Regular][115]
- [Rough][116]
- [Unusual][117]

 |

Constrained divisor sums |

- [Perfect][14]
- [Almost perfect][118]
- [Quasiperfect][43]
- [Multiply perfect][119]
- [Hemiperfect][120]
- [Hyperperfect][121]
- [Superperfect][122]
- [Unitary perfect][123]
- [Semiperfect][42]
- [Practical][124]
- [Descartes][125]
- [Erdős–Nicolas][126]

 |

With many divisors |

- [Abundant][127]
- [Primitive abundant][18]
- [Highly abundant][29]
- [Superabundant][30]
- [Colossally abundant][32]
- [Highly composite][31]
- [Superior highly composite][33]
- [Weird][34]

 |

[Aliquot sequence][128] -related |

- [Untouchable][129]
- [Amicable][130] ( [Triple][131])
- [Sociable][132]
- [Betrothed][133]

 |

[Base][134] -dependent |

- [Equidigital][135]
- [Extravagant][136]
- [Frugal][137]
- [Harshad][138]
- [Polydivisible][139]
- [Smith][140]

 |

Other sets |

- [Arithmetic][141]
- [Deficient][15]
- [Friendly][40]
- [Solitary][142]
- [Sublime][143]
- [Harmonic divisor][144]
- [Refactorable][145]
- [Superperfect][122]

 |

- [v][146]
- [t][147]
- [e][148]

Classes of [natural numbers][8]

 |

[Powers][149] and related numbers

 |

- [Achilles][113]
- [Power of 2][150]
- [Power of 3][151]
- [Power of 10][152]
- [Square][153]
- [Cube][154]
- [Fourth power][155]
- [Fifth power][156]
- [Sixth power][157]
- [Seventh power][158]
- [Eighth power][159]
- [Perfect power][112]
- [Powerful][111]
- [Prime power][160]

 |

 |

Of the form *a*× 2*b*± 1

 |

- [Cullen][161]
- [Double Mersenne][162]
- [Fermat][163]
- [Mersenne][164]
- [Proth][165]
- [Thabit][166]
- [Woodall][167]

 |

 |

Other polynomial numbers

 |

- [Hilbert][168]
- [Idoneal][169]
- [Leyland][170]
- [Loeschian][171]
- [Lucky numbers of Euler][172]

 |

 |

[Recursively][173] defined numbers

 |

- [Fibonacci][174]
- [Jacobsthal][175]
- [Leonardo][176]
- [Lucas][177]
- [Narayana][178]
- [Padovan][179]
- [Pell][180]
- [Perrin][181]
- [Graham][182]

 |

 |

Possessing a specific set of other numbers

 |

- [Amenable][183]
- [Congruent][184]
- [Knödel][185]
- [Riesel][186]
- [Sierpiński][187]

 |

 |

Expressible via specific sums

 |

- [Nonhypotenuse][188]
- [Polite][189]
- [Practical][124]
- [Primary pseudoperfect][190]
- [Ulam][191]
- [Wolstenholme][192]

 |

 |

[Figurate numbers][193]

 |

[2-dimensional][194] |

[centered][195] |

- [Centered triangular][196]
- [Centered square][197]
- [Centered pentagonal][198]
- [Centered hexagonal][199]
- [Centered heptagonal][200]
- [Centered octagonal][201]
- [Centered nonagonal][202]
- [Centered decagonal][203]
- [Star][204]

 |

[non-centered][205] |

- [Triangular][206]
- [Square][153]
- [Square triangular][207]
- [Pentagonal][208]
- [Hexagonal][209]
- [Heptagonal][210]
- [Octagonal][211]
- [Nonagonal][212]
- [Decagonal][213]
- [Dodecagonal][214]

 |

 |

[3-dimensional][215] |

[centered][216] |

- [Centered tetrahedral][217]
- [Centered cube][218]
- [Centered octahedral][219]
- [Centered dodecahedral][220]
- [Centered icosahedral][221]

 |

[non-centered][222] |

- [Tetrahedral][223]
- [Cubic][154]
- [Octahedral][224]
- [Dodecahedral][225]
- [Icosahedral][226]
- [Stella octangula][227]

 |

[pyramidal][228] |

- [Square pyramidal][229]

 |

 |

[4-dimensional][230] |

non-centered |

- [Pentatope][231]
- [Squared triangular][232]
- [Tesseractic][155]

 |

 |

 |

 |

Combinatorial numbers

 |

- [Bell][233]
- [Cake][234]
- [Catalan][235]
- [Dedekind][236]
- [Delannoy][237]
- [Euler][238]
- [Eulerian][239]
- [Fuss–Catalan][240]
- [Lah][241]
- [Lazy caterer's sequence][242]
- [Lobb][243]
- [Motzkin][244]
- [Narayana][245]
- [Ordered Bell][246]
- [Schröder][247]
- [Schröder–Hipparchus][248]
- [Stirling first][249]
- [Stirling second][250]
- [Telephone number][251]
- [Wedderburn–Etherington][252]

 |

 |

[Primes][22]

 |

- [Wieferich][253]
- [Wall–Sun–Sun][254]
- [Wolstenholme prime][255]
- [Wilson][256]

 |

 |

[Pseudoprimes][257]

 |

- [Carmichael number][258]
- [Catalan pseudoprime][259]
- [Elliptic pseudoprime][260]
- [Euler pseudoprime][261]
- [Euler–Jacobi pseudoprime][262]
- [Fermat pseudoprime][263]
- [Frobenius pseudoprime][264]
- [Lucas pseudoprime][265]
- [Lucas–Carmichael number][266]
- [Perrin pseudoprime][267]
- [Somer–Lucas pseudoprime][268]
- [Strong pseudoprime][269]

 |

 |

[Arithmetic functions][270] and [dynamics][271]

 |

[Divisor functions][9] |

- [Abundant][127]
- [Almost perfect][118]
- [Arithmetic][141]
- [Betrothed][133]
- [Colossally abundant][32]
- [Deficient][15]
- [Descartes][125]
- [Hemiperfect][120]
- [Highly abundant][29]
- [Highly composite][31]
- [Hyperperfect][121]
- [Multiply perfect][119]
- [Perfect][14]
- [Practical][124]
- [Primitive abundant][18]
- [Quasiperfect][43]
- [Refactorable][145]
- [Semiperfect][42]
- [Sublime][143]
- [Superabundant][30]
- [Superior highly composite][33]
- [Superperfect][122]

 |

[Prime omega functions][272] |

- [Almost prime][273]
- [Semiprime][107]

 |

[Euler's totient function][274] |

- [Highly cototient][275]
- [Highly totient][276]
- [Noncototient][277]
- [Nontotient][278]
- [Perfect totient][279]
- [Sparsely totient][280]

 |

[Aliquot sequences][128] |

- [Amicable][130]
- [Perfect][14]
- [Sociable][281]
- [Untouchable][129]

 |

[Primorial][282] |

- [Euclid][283]
- [Fortunate][284]

 |

 |

 |

Other [prime factor][21] or [divisor][103] related numbers

 |

- [Blum][285]
- [Cyclic][286]
- [Erdős–Nicolas][126]
- [Erdős–Woods][287]
- [Friendly][40]
- [Giuga][288]
- [Harmonic divisor][144]
- [Jordan–Pólya][289]
- [Lucas–Carmichael][266]
- [Pronic][108]
- [Regular][115]
- [Rough][116]
- [Smooth][114]
- [Sphenic][109]
- [Størmer][290]
- [Super-Poulet][291]

 |

 |

[Numeral system][292] -dependent numbers

 |

[Arithmetic functions][270]
and [dynamics][271] |

- [Persistence][293]

  - [Additive][294]
  - [Multiplicative][295]

[Digit sum][296] |

- [Digit sum][296]
- [Digital root][297]
- [Self][298]
- [Sum-product][299]

 |

Digit product |

- [Multiplicative digital root][300]
- [Sum-product][299]

 |

Coding-related |

- [Meertens][301]

 |

Other |

- [Dudeney][302]
- [Factorion][303]
- [Kaprekar][304]
- [Kaprekar's constant][305]
- [Keith][306]
- [Lychrel][307]
- [Narcissistic][308]
- [Perfect digit-to-digit invariant][309]
- [Perfect digital invariant][310]

  - [Happy][311]

 |

 |

[P-adic numbers][312] -related |

- [Automorphic][313]

  - [Trimorphic][314]

 |

[Digit][315] -composition related |

- [Palindromic][316]
- [Pandigital][317]
- [Repdigit][318]
- [Repunit][319]
- [Self-descriptive][320]
- [Smarandache–Wellin][321]
- [Undulating][322]

 |

Digit- [permutation][323] related |

- [Cyclic][324]
- [Digit-reassembly][325]
- [Parasitic][326]
- [Primeval][327]
- [Transposable][328]

 |

Divisor-related |

- [Equidigital][135]
- [Extravagant][136]
- [Frugal][137]
- [Harshad][138]
- [Polydivisible][139]
- [Smith][140]
- [Vampire][329]

 |

Other |

- [Friedman][330]

 |

 |

 |

[Binary numbers][331]

 |

- [Evil][332]
- [Odious][333]
- [Pernicious][334]

 |

 |

Generated via a [sieve][335]

 |

- [Lucky][336]
- [Prime][337]

 |

 |

[Sorting][338] related

 |

- [Pancake number][339]
- [Sorting number][340]

 |

 |

[Natural language][341] related

 |

- [Aronson's sequence][342]
- [Ban][343]

 |

 |

[Graphemics][344] related

 |

- [Strobogrammatic][345]

 |

 |

- [346] [Mathematics portal][347]

 |

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Abundant_number&oldid=1363371058#Related_concepts][348] "

[Categories][349]:

- [Arithmetic dynamics][350]
- [Divisor function][351]
- [Integer sequences][352]

Hidden categories:

- [Articles with short description][353]
- [Short description is different from Wikidata][354]
- [CS1 errors: deprecated parameters][355]

Search

Abundant number

45 languages Add topic


## Links

[1]: /w/index.php?title=Abundancy_index&amp;redirect=no
[2]: https://en.wikipedia.org/wiki/File:Abundant_number_Cuisenaire_rods_12.png
[3]: https://en.wikipedia.org/wiki/Cuisenaire_rods
[4]: https://en.wikipedia.org/wiki/Number_theory
[5]: https://en.wikipedia.org/wiki/Positive_integer
[6]: https://en.wikipedia.org/wiki/Proper_divisor
[7]: /w/index.php?title=Abundant_number&amp;action=edit&amp;section=1
[8]: https://en.wikipedia.org/wiki/Natural_number
[9]: https://en.wikipedia.org/wiki/Divisor_function
[10]: https://en.wikipedia.org/wiki/Aliquot_sum
[11]: https://en.wikipedia.org/wiki/Integer
[12]: //oeis.org/A005101
[13]: https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences
[14]: https://en.wikipedia.org/wiki/Perfect_number
[15]: https://en.wikipedia.org/wiki/Deficient_number
[16]: /w/index.php?title=Abundant_number&amp;action=edit&amp;section=2
[17]: https://en.wikipedia.org/wiki/File:Proportion_of_abundant_numbers.svg
[18]: https://en.wikipedia.org/wiki/Primitive_abundant_number
[19]: https://en.wikipedia.org/wiki/Even_and_odd_numbers
[20]: https://en.wikipedia.org/wiki/Parity_(mathematics)
[21]: https://en.wikipedia.org/wiki/Prime_factor
[22]: https://en.wikipedia.org/wiki/Prime_number
[23]: //oeis.org/A047802
[24]: https://en.wikipedia.org/wiki/Natural_density
[25]: https://en.wikipedia.org/wiki/Paul_Erdős
[26]: /w/index.php?title=Abundant_number&amp;action=edit&amp;section=3
[27]: https://en.wikipedia.org/wiki/File:Euler_diagram_numbers_with_many_divisors.svg
[28]: https://en.wikipedia.org/wiki/Euler_diagram
[29]: https://en.wikipedia.org/wiki/Highly_abundant_number
[30]: https://en.wikipedia.org/wiki/Superabundant_number
[31]: https://en.wikipedia.org/wiki/Highly_composite_number
[32]: https://en.wikipedia.org/wiki/Colossally_abundant_number
[33]: https://en.wikipedia.org/wiki/Superior_highly_composite_number
[34]: https://en.wikipedia.org/wiki/Weird_number
[35]: https://en.wikipedia.org/wiki/Composite_number
[36]: https://en.wikipedia.org/wiki/Nicomachus
[37]: https://en.wikipedia.org/wiki/Introduction_to_Arithmetic
[38]: https://en.wikipedia.org/wiki/Theon_of_Smyrna
[39]: //oeis.org/A004394
[40]: https://en.wikipedia.org/wiki/Friendly_number
[41]: //oeis.org/A134716
[42]: https://en.wikipedia.org/wiki/Semiperfect_number
[43]: https://en.wikipedia.org/wiki/Quasiperfect_number
[44]: /w/index.php?title=Abundant_number&amp;action=edit&amp;section=4
[45]: https://en.wikipedia.org/wiki/Mathematics_Magazine
[46]: https://en.wikipedia.org/wiki/Doi_(identifier)
[47]: https://doi.org/10.2307%2F2690424
[48]: https://en.wikipedia.org/wiki/ISSN_(identifier)
[49]: https://search.worldcat.org/issn/0025-570X
[50]: https://en.wikipedia.org/wiki/JSTOR_(identifier)
[51]: https://www.jstor.org/stable/2690424
[52]: https://en.wikipedia.org/wiki/MR_(identifier)
[53]: https://mathscinet.ams.org/mathscinet-getitem?mr=0835144
[54]: https://en.wikipedia.org/wiki/Zbl_(identifier)
[55]: https://zbmath.org/?format=complete&amp;q=an:0601.10003
[56]: https://www.jstor.org/stable/27958492
[57]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[58]: https://en.wikipedia.org/wiki/Special:BookSources/0-88385-502-X
[59]: https://doi.org/10.1007%2F978-981-97-2465-9
[60]: https://en.wikipedia.org/wiki/Special:BookSources/978-981-97-2465-9
[61]: https://mathworld.wolfram.com/AbundantNumber.html
[62]: https://www.cambridge.org/9780521585033
[63]: https://en.wikipedia.org/wiki/Cambridge_University_Press
[64]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-511-06583-5
[65]: https://zbmath.org/?format=complete&amp;q=an:1071.11002
[66]: https://en.wikipedia.org/wiki/Neil_Sloane
[67]: https://oeis.org/A005231
[68]: https://projecteuclid.org/journals/bulletin-of-the-belgian-mathematical-society-simon-stevin/volume-12/issue-1/On-the-smallest-abundant-number-not-divisible-by-the-first/10.36045/bbms/1113318127.full
[69]: https://en.wikipedia.org/wiki/Bulletin_of_the_Belgian_Mathematical_Society
[70]: https://doi.org/10.36045%2Fbbms%2F1113318127
[71]: https://en.wikipedia.org/wiki/Gérald_Tenenbaum
[72]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-521-34056-4
[73]: https://zbmath.org/?format=complete&amp;q=an:0653.10001
[74]: http://projecteuclid.org/euclid.em/1048515661
[75]: https://en.wikipedia.org/wiki/CiteSeerX_(identifier)
[76]: https://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.36.8272
[77]: https://doi.org/10.1080%2F10586458.1998.10504363
[78]: https://search.worldcat.org/issn/1058-6458
[79]: https://mathscinet.ams.org/mathscinet-getitem?mr=1677091
[80]: https://zbmath.org/?format=complete&amp;q=an:0923.11127
[81]: https://en.wikipedia.org/wiki/Template:Cite_journal
[82]: https://en.wikipedia.org/wiki/Help:CS1_errors#deprecated_params
[83]: http://collections.dartmouth.edu/archive/object/dcdis/dcdis-kobayashim2010
[84]: https://doi.org/10.1349%2Fddlp.1662
[85]: https://oeis.org/A094268
[86]: https://www.renyi.hu/~p_erdos/1935-03.pdf
[87]: https://arxiv.org/abs/1603.06176
[88]: https://oeis.org/A048242
[89]: https://archive.org/details/historyofgreekm01heat
[90]: https://oeis.org/A119240
[91]: https://doi.org/10.1006%2Fjnth.1993.1057
[92]: https://en.wikipedia.org/wiki/Journal_of_Number_Theory
[93]: https://mathscinet.ams.org/mathscinet-getitem?mr=1233293
[94]: https://zbmath.org/?format=complete&amp;q=an:0781.11015
[95]: /w/index.php?title=Abundant_number&amp;action=edit&amp;section=5
[96]: http://primes.utm.edu/glossary/page.php?sort=AbundantNumber
[97]: https://planetmath.org/AbundantNumber
[98]: https://en.wikipedia.org/wiki/PlanetMath
[99]: https://en.wikipedia.org/wiki/Template:Divisor_classes
[100]: https://en.wikipedia.org/wiki/Template_talk:Divisor_classes
[101]: https://en.wikipedia.org/wiki/Special:EditPage/Template:Divisor_classes
[102]: https://en.wikipedia.org/wiki/Integer_factorization
[103]: https://en.wikipedia.org/wiki/Divisor
[104]: https://en.wikipedia.org/wiki/Unitary_divisor
[105]: https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic
[106]: https://en.wikipedia.org/wiki/File:Lattice_of_the_divisibility_of_60.svg
[107]: https://en.wikipedia.org/wiki/Semiprime
[108]: https://en.wikipedia.org/wiki/Pronic_number
[109]: https://en.wikipedia.org/wiki/Sphenic_number
[110]: https://en.wikipedia.org/wiki/Square-free_integer
[111]: https://en.wikipedia.org/wiki/Powerful_number
[112]: https://en.wikipedia.org/wiki/Perfect_power
[113]: https://en.wikipedia.org/wiki/Achilles_number
[114]: https://en.wikipedia.org/wiki/Smooth_number
[115]: https://en.wikipedia.org/wiki/Regular_number
[116]: https://en.wikipedia.org/wiki/Rough_number
[117]: https://en.wikipedia.org/wiki/Unusual_number
[118]: https://en.wikipedia.org/wiki/Almost_perfect_number
[119]: https://en.wikipedia.org/wiki/Multiply_perfect_number
[120]: https://en.wikipedia.org/wiki/Hemiperfect_number
[121]: https://en.wikipedia.org/wiki/Hyperperfect_number
[122]: https://en.wikipedia.org/wiki/Superperfect_number
[123]: https://en.wikipedia.org/wiki/Unitary_perfect_number
[124]: https://en.wikipedia.org/wiki/Practical_number
[125]: https://en.wikipedia.org/wiki/Descartes_number
[126]: https://en.wikipedia.org/wiki/Erdős–Nicolas_number
[127]: https://en.wikipedia.org/wiki/Abundant_number
[128]: https://en.wikipedia.org/wiki/Aliquot_sequence
[129]: https://en.wikipedia.org/wiki/Untouchable_number
[130]: https://en.wikipedia.org/wiki/Amicable_numbers
[131]: https://en.wikipedia.org/wiki/Amicable_triple
[132]: https://en.wikipedia.org/wiki/Sociable_number
[133]: https://en.wikipedia.org/wiki/Betrothed_numbers
[134]: https://en.wikipedia.org/wiki/Radix
[135]: https://en.wikipedia.org/wiki/Equidigital_number
[136]: https://en.wikipedia.org/wiki/Extravagant_number
[137]: https://en.wikipedia.org/wiki/Frugal_number
[138]: https://en.wikipedia.org/wiki/Harshad_number
[139]: https://en.wikipedia.org/wiki/Polydivisible_number
[140]: https://en.wikipedia.org/wiki/Smith_number
[141]: https://en.wikipedia.org/wiki/Arithmetic_number
[142]: https://en.wikipedia.org/wiki/Friendly_number#Solitary_numbers
[143]: https://en.wikipedia.org/wiki/Sublime_number
[144]: https://en.wikipedia.org/wiki/Harmonic_divisor_number
[145]: https://en.wikipedia.org/wiki/Refactorable_number
[146]: https://en.wikipedia.org/wiki/Template:Classes_of_natural_numbers
[147]: https://en.wikipedia.org/wiki/Template_talk:Classes_of_natural_numbers
[148]: https://en.wikipedia.org/wiki/Special:EditPage/Template:Classes_of_natural_numbers
[149]: https://en.wikipedia.org/wiki/Exponentiation
[150]: https://en.wikipedia.org/wiki/Power_of_two
[151]: https://en.wikipedia.org/wiki/Power_of_three
[152]: https://en.wikipedia.org/wiki/Power_of_10
[153]: https://en.wikipedia.org/wiki/Square_number
[154]: https://en.wikipedia.org/wiki/Cube_(algebra)
[155]: https://en.wikipedia.org/wiki/Fourth_power
[156]: https://en.wikipedia.org/wiki/Fifth_power_(algebra)
[157]: https://en.wikipedia.org/wiki/Sixth_power
[158]: https://en.wikipedia.org/wiki/Seventh_power
[159]: https://en.wikipedia.org/wiki/Eighth_power
[160]: https://en.wikipedia.org/wiki/Prime_power
[161]: https://en.wikipedia.org/wiki/Cullen_number
[162]: https://en.wikipedia.org/wiki/Double_Mersenne_number
[163]: https://en.wikipedia.org/wiki/Fermat_number
[164]: https://en.wikipedia.org/wiki/Mersenne_prime
[165]: https://en.wikipedia.org/wiki/Proth_number
[166]: https://en.wikipedia.org/wiki/Thabit_number
[167]: https://en.wikipedia.org/wiki/Woodall_number
[168]: https://en.wikipedia.org/wiki/Hilbert_number
[169]: https://en.wikipedia.org/wiki/Idoneal_number
[170]: https://en.wikipedia.org/wiki/Leyland_number
[171]: https://en.wikipedia.org/wiki/Loeschian_number
[172]: https://en.wikipedia.org/wiki/Lucky_numbers_of_Euler
[173]: https://en.wikipedia.org/wiki/Recursion
[174]: https://en.wikipedia.org/wiki/Fibonacci_sequence
[175]: https://en.wikipedia.org/wiki/Jacobsthal_number
[176]: https://en.wikipedia.org/wiki/Leonardo_number
[177]: https://en.wikipedia.org/wiki/Lucas_number
[178]: https://en.wikipedia.org/wiki/Supergolden_ratio#Narayana_sequence
[179]: https://en.wikipedia.org/wiki/Padovan_sequence
[180]: https://en.wikipedia.org/wiki/Pell_number
[181]: https://en.wikipedia.org/wiki/Perrin_number
[182]: https://en.wikipedia.org/wiki/Graham's_number
[183]: https://en.wikipedia.org/wiki/Amenable_number
[184]: https://en.wikipedia.org/wiki/Congruent_number
[185]: https://en.wikipedia.org/wiki/Knödel_number
[186]: https://en.wikipedia.org/wiki/Riesel_number
[187]: https://en.wikipedia.org/wiki/Sierpiński_number
[188]: https://en.wikipedia.org/wiki/Nonhypotenuse_number
[189]: https://en.wikipedia.org/wiki/Polite_number
[190]: https://en.wikipedia.org/wiki/Primary_pseudoperfect_number
[191]: https://en.wikipedia.org/wiki/Ulam_number
[192]: https://en.wikipedia.org/wiki/Wolstenholme_number
[193]: https://en.wikipedia.org/wiki/Figurate_number
[194]: https://en.wikipedia.org/wiki/Plane_(mathematics)
[195]: https://en.wikipedia.org/wiki/Centered_polygonal_number
[196]: https://en.wikipedia.org/wiki/Centered_triangular_number
[197]: https://en.wikipedia.org/wiki/Centered_square_number
[198]: https://en.wikipedia.org/wiki/Centered_pentagonal_number
[199]: https://en.wikipedia.org/wiki/Centered_hexagonal_number
[200]: https://en.wikipedia.org/wiki/Centered_heptagonal_number
[201]: https://en.wikipedia.org/wiki/Centered_octagonal_number
[202]: https://en.wikipedia.org/wiki/Centered_nonagonal_number
[203]: https://en.wikipedia.org/wiki/Centered_decagonal_number
[204]: https://en.wikipedia.org/wiki/Star_number
[205]: https://en.wikipedia.org/wiki/Polygonal_number
[206]: https://en.wikipedia.org/wiki/Triangular_number
[207]: https://en.wikipedia.org/wiki/Square_triangular_number
[208]: https://en.wikipedia.org/wiki/Pentagonal_number
[209]: https://en.wikipedia.org/wiki/Hexagonal_number
[210]: https://en.wikipedia.org/wiki/Heptagonal_number
[211]: https://en.wikipedia.org/wiki/Octagonal_number
[212]: https://en.wikipedia.org/wiki/Nonagonal_number
[213]: https://en.wikipedia.org/wiki/Decagonal_number
[214]: https://en.wikipedia.org/wiki/Dodecagonal_number
[215]: https://en.wikipedia.org/wiki/Three-dimensional_space
[216]: https://en.wikipedia.org/wiki/Centered_polyhedral_number
[217]: https://en.wikipedia.org/wiki/Centered_tetrahedral_number
[218]: https://en.wikipedia.org/wiki/Centered_cube_number
[219]: https://en.wikipedia.org/wiki/Centered_octahedral_number
[220]: https://en.wikipedia.org/wiki/Centered_dodecahedral_number
[221]: https://en.wikipedia.org/wiki/Centered_icosahedral_number
[222]: https://en.wikipedia.org/wiki/Polyhedral_number
[223]: https://en.wikipedia.org/wiki/Tetrahedral_number
[224]: https://en.wikipedia.org/wiki/Octahedral_number
[225]: https://en.wikipedia.org/wiki/Dodecahedral_number
[226]: https://en.wikipedia.org/wiki/Icosahedral_number
[227]: https://en.wikipedia.org/wiki/Stella_octangula_number
[228]: https://en.wikipedia.org/wiki/Pyramidal_number
[229]: https://en.wikipedia.org/wiki/Square_pyramidal_number
[230]: https://en.wikipedia.org/wiki/Four-dimensional_space
[231]: https://en.wikipedia.org/wiki/Pentatope_number
[232]: https://en.wikipedia.org/wiki/Squared_triangular_number
[233]: https://en.wikipedia.org/wiki/Bell_number
[234]: https://en.wikipedia.org/wiki/Cake_number
[235]: https://en.wikipedia.org/wiki/Catalan_number
[236]: https://en.wikipedia.org/wiki/Dedekind_number
[237]: https://en.wikipedia.org/wiki/Delannoy_number
[238]: https://en.wikipedia.org/wiki/Euler_number
[239]: https://en.wikipedia.org/wiki/Eulerian_number
[240]: https://en.wikipedia.org/wiki/Fuss–Catalan_number
[241]: https://en.wikipedia.org/wiki/Lah_number
[242]: https://en.wikipedia.org/wiki/Lazy_caterer's_sequence
[243]: https://en.wikipedia.org/wiki/Lobb_number
[244]: https://en.wikipedia.org/wiki/Motzkin_number
[245]: https://en.wikipedia.org/wiki/Narayana_number
[246]: https://en.wikipedia.org/wiki/Ordered_Bell_number
[247]: https://en.wikipedia.org/wiki/Schröder_number
[248]: https://en.wikipedia.org/wiki/Schröder–Hipparchus_number
[249]: https://en.wikipedia.org/wiki/Stirling_numbers_of_the_first_kind
[250]: https://en.wikipedia.org/wiki/Stirling_numbers_of_the_second_kind
[251]: https://en.wikipedia.org/wiki/Telephone_number_(mathematics)
[252]: https://en.wikipedia.org/wiki/Wedderburn–Etherington_number
[253]: https://en.wikipedia.org/wiki/Wieferich_prime#Wieferich_numbers
[254]: https://en.wikipedia.org/wiki/Wall–Sun–Sun_prime
[255]: https://en.wikipedia.org/wiki/Wolstenholme_prime
[256]: https://en.wikipedia.org/wiki/Wilson_prime#Wilson_numbers
[257]: https://en.wikipedia.org/wiki/Pseudoprime
[258]: https://en.wikipedia.org/wiki/Carmichael_number
[259]: https://en.wikipedia.org/wiki/Catalan_pseudoprime
[260]: https://en.wikipedia.org/wiki/Elliptic_pseudoprime
[261]: https://en.wikipedia.org/wiki/Euler_pseudoprime
[262]: https://en.wikipedia.org/wiki/Euler–Jacobi_pseudoprime
[263]: https://en.wikipedia.org/wiki/Fermat_pseudoprime
[264]: https://en.wikipedia.org/wiki/Frobenius_pseudoprime
[265]: https://en.wikipedia.org/wiki/Lucas_pseudoprime
[266]: https://en.wikipedia.org/wiki/Lucas–Carmichael_number
[267]: https://en.wikipedia.org/wiki/Perrin_number#Perrin_primality_test
[268]: https://en.wikipedia.org/wiki/Somer–Lucas_pseudoprime
[269]: https://en.wikipedia.org/wiki/Strong_pseudoprime
[270]: https://en.wikipedia.org/wiki/Arithmetic_function
[271]: https://en.wikipedia.org/wiki/Arithmetic_dynamics
[272]: https://en.wikipedia.org/wiki/Prime_omega_function
[273]: https://en.wikipedia.org/wiki/Almost_prime
[274]: https://en.wikipedia.org/wiki/Euler's_totient_function
[275]: https://en.wikipedia.org/wiki/Highly_cototient_number
[276]: https://en.wikipedia.org/wiki/Highly_totient_number
[277]: https://en.wikipedia.org/wiki/Noncototient
[278]: https://en.wikipedia.org/wiki/Nontotient
[279]: https://en.wikipedia.org/wiki/Perfect_totient_number
[280]: https://en.wikipedia.org/wiki/Sparsely_totient_number
[281]: https://en.wikipedia.org/wiki/Sociable_numbers
[282]: https://en.wikipedia.org/wiki/Primorial
[283]: https://en.wikipedia.org/wiki/Euclid_number
[284]: https://en.wikipedia.org/wiki/Fortunate_number
[285]: https://en.wikipedia.org/wiki/Blum_integer
[286]: https://en.wikipedia.org/wiki/Cyclic_number_(group_theory)
[287]: https://en.wikipedia.org/wiki/Erdős–Woods_number
[288]: https://en.wikipedia.org/wiki/Giuga_number
[289]: https://en.wikipedia.org/wiki/Jordan–Pólya_number
[290]: https://en.wikipedia.org/wiki/Størmer_number
[291]: https://en.wikipedia.org/wiki/Super-Poulet_number
[292]: https://en.wikipedia.org/wiki/Numeral_system
[293]: https://en.wikipedia.org/wiki/Persistence_of_a_number
[294]: https://en.wikipedia.org/wiki/Additive_persistence
[295]: https://en.wikipedia.org/wiki/Multiplicative_persistence
[296]: https://en.wikipedia.org/wiki/Digit_sum
[297]: https://en.wikipedia.org/wiki/Digital_root
[298]: https://en.wikipedia.org/wiki/Self_number
[299]: https://en.wikipedia.org/wiki/Sum-product_number
[300]: https://en.wikipedia.org/wiki/Multiplicative_digital_root
[301]: https://en.wikipedia.org/wiki/Meertens_number
[302]: https://en.wikipedia.org/wiki/Dudeney_number
[303]: https://en.wikipedia.org/wiki/Factorion
[304]: https://en.wikipedia.org/wiki/Kaprekar_number
[305]: https://en.wikipedia.org/wiki/Kaprekar's_routine
[306]: https://en.wikipedia.org/wiki/Keith_number
[307]: https://en.wikipedia.org/wiki/Lychrel_number
[308]: https://en.wikipedia.org/wiki/Narcissistic_number
[309]: https://en.wikipedia.org/wiki/Perfect_digit-to-digit_invariant
[310]: https://en.wikipedia.org/wiki/Perfect_digital_invariant
[311]: https://en.wikipedia.org/wiki/Happy_number
[312]: https://en.wikipedia.org/wiki/P-adic_numbers
[313]: https://en.wikipedia.org/wiki/Automorphic_number
[314]: https://en.wikipedia.org/wiki/Trimorphic_number
[315]: https://en.wikipedia.org/wiki/Numerical_digit
[316]: https://en.wikipedia.org/wiki/Palindromic_number
[317]: https://en.wikipedia.org/wiki/Pandigital_number
[318]: https://en.wikipedia.org/wiki/Repdigit
[319]: https://en.wikipedia.org/wiki/Repunit
[320]: https://en.wikipedia.org/wiki/Self-descriptive_number
[321]: https://en.wikipedia.org/wiki/Smarandache–Wellin_number
[322]: https://en.wikipedia.org/wiki/Undulating_number
[323]: https://en.wikipedia.org/wiki/Permutation
[324]: https://en.wikipedia.org/wiki/Cyclic_number
[325]: https://en.wikipedia.org/wiki/Digit-reassembly_number
[326]: https://en.wikipedia.org/wiki/Parasitic_number
[327]: https://en.wikipedia.org/wiki/Primeval_number
[328]: https://en.wikipedia.org/wiki/Transposable_integer
[329]: https://en.wikipedia.org/wiki/Vampire_number
[330]: https://en.wikipedia.org/wiki/Friedman_number
[331]: https://en.wikipedia.org/wiki/Binary_number
[332]: https://en.wikipedia.org/wiki/Evil_number
[333]: https://en.wikipedia.org/wiki/Odious_number
[334]: https://en.wikipedia.org/wiki/Pernicious_number
[335]: https://en.wikipedia.org/wiki/Sieve_theory
[336]: https://en.wikipedia.org/wiki/Lucky_number
[337]: https://en.wikipedia.org/wiki/Generation_of_primes
[338]: https://en.wikipedia.org/wiki/Sorting_algorithm
[339]: https://en.wikipedia.org/wiki/Pancake_sorting
[340]: https://en.wikipedia.org/wiki/Sorting_number
[341]: https://en.wikipedia.org/wiki/Natural_language
[342]: https://en.wikipedia.org/wiki/Aronson's_sequence
[343]: https://en.wikipedia.org/wiki/Ban_number
[344]: https://en.wikipedia.org/wiki/Graphemics
[345]: https://en.wikipedia.org/wiki/Strobogrammatic_number
[346]: https://en.wikipedia.org/wiki/File:Symbol_portal_class.svg
[347]: https://en.wikipedia.org/wiki/Portal:Mathematics
[348]: https://en.wikipedia.org/w/index.php?title=Abundant_number&amp;oldid=1363371058#Related_concepts
[349]: /wiki/Help:Category
[350]: /wiki/Category:Arithmetic_dynamics
[351]: /wiki/Category:Divisor_function
[352]: /wiki/Category:Integer_sequences
[353]: /wiki/Category:Articles_with_short_description
[354]: /wiki/Category:Short_description_is_different_from_Wikidata
[355]: /wiki/Category:CS1_errors:_deprecated_parameters
