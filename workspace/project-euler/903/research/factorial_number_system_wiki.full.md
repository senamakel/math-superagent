<!-- source: https://en.wikipedia.org/wiki/Factorial_number_system | converted from HTML -->

Factorial number system - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Numeral system in combinatorics

Part of [a series][1] on |

[Numeral systems][2] |

[Place-value notation][3]

[Hindu–Arabic numerals][4]

- [Western Arabic][5]
- [Eastern Arabic][6]

---

- [Bengali][7]
- [Devanagari][8]
- [Gujarati][9]
- [Gurmukhi][10]
- [Odia][11]
- [Sinhala][12]
- [Tamil][13]
- [Malayalam][14]
- [Telugu][15]
- [Kannada][16]
- [Dzongkha][17]

---

- [Tibetan][18]
- [Balinese][19]
- [Burmese][20]
- [Javanese][21]
- [Khmer][22]
- [Lao][23]
- [Mongolian][24]
- [Sundanese][25]
- [Thai][26]

 |

Other systems

- [History][27]

---

[Ancient][28]

- [Babylonian][29]

---

[Post-classical][30]

- [Cistercian][31]
- [Mayan][32]
- [Muisca][33]
- [Pentadic][34]
- [Quipu][35]
- [Rumi][36]

---

Contemporary

- [Cherokee][37]
- [Kaktovik][38] (Iñupiaq)

 |

By [radix/base][39]

Common radices/bases

- [2][40]
- [3][41]
- [4][42]
- [5][43]
- [6][44]
- [8][45]
- [10][46]
- [11][47]
- [12][48]
- [16][49]
- [20][50]
- [60][51]

---

[Non-standard radices/bases][52]

- [Bijective][53] ( [1][54])
- [Signed-digit][55] ( [balanced ternary][56])
- [Mixed][57] ( [factorial][58])
- [Negative][59]
- [Complex][60] (**[2 i][61])
- [Non-integer][62] ( [φ][63])
- [Asymmetric][64]

 |

 |

[Sign-value notation][65]

Non-alphabetic

Contemporary East Asian

- [Chinese][66]

  - [Hokkien][67]
  - [Suzhou][68]

- [Japanese][69]
- [Korean][70]
- [Vietnamese][71]

Historic East Asian

- [Counting rods][72]
- [Tangut][73]

---

Other non-alphabetic

- [Aegean][74]
- [Attic][75]
- [Aztec][76]
- [Brahmi][77]
- [Chuvash][78]
- [Egyptian][79]
- [Etruscan][80]
- [Kharosthi][81]
- [Prehistoric counting][82]
- [Proto-cuneiform][83]
- [Roman][84]
- [Tally marks][85]

 |

[Alphabetic][86]

- [Abjad][87]
- [Armenian][88]
- [Alphasyllabic][89]

  - [Akṣarapallī][90]
  - [Āryabhaṭa][91]
  - [Kaṭapayādi][92]

- [Coptic][93]
- [Cyrillic][94]
- [Geʽez][95]
- [Georgian][96]
- [Glagolitic][97]
- [Greek][98]
- [Hebrew][99]

 |

 |

[List of numeral systems][100] |

- [v][101]
- [t][102]
- [e][103]

 |

[image: icon] [104]

 |

This article **needs [more citations][105]**. Please help [improve this article][106] by [adding citations to reliable sources][107]. Unsourced material may be challenged and [removed][108].
*Find sources:*["Factorial number system"][109] – [news][110]**·**[newspapers][111]**·**[books][112]**·**[scholar][113]**·**[JSTOR][114]*( March 2021)**( [Learn how and when to remove this message][115])*

 |

In [combinatorics][116], the **factorial number system**(also known as **factoradic**), is a [mixed radix][57] [numeral system][2] adapted to numbering [permutations][117]. It is also called **factorial base**, although [factorials][118] do not function as [base][39], but as [place value][119] of digits. By converting a number less than *n*! to factorial representation, one obtains a [sequence][120] of *n*digits that can be converted to a permutation of *n*elements in a straightforward way, either using them as [Lehmer code][121] or as [inversion][122] table [1] representation; in the former case the resulting map from [integers][123] to permutations of *n*elements lists them in [lexicographical order][124]. General mixed radix systems were studied by [Georg Cantor][125]. [2]

The term "factorial number system" is used by [Knuth][126], [3] while the French equivalent "numération factorielle" was first used in 1888. [4] The term "factoradic", which is a [portmanteau][127] of factorial and mixed radix, appears to be of more recent date. [5]

## Definition

[[edit][128]]

The factorial number system is a [mixed radix][57] [numeral system][2]: the *i*-th digit from the right has base*i*, which means that the digit must be strictly less than *i*, and that (taking into account the bases of the less significant digits) its value is to be multiplied by (*i*− 1)! (its place value).

style=\"background-color: var(--background-color-neutral,#eaecf0);color: var(--color-base,#202122);font-weight: bold; vertical-align: middle; text-align: left; \" class=\"table-rh\"</span>"},{"html":""}]]}'>Radix/Base | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |

style=\"background-color: var(--background-color-neutral,#eaecf0);color: var(--color-base,#202122);font-weight: bold; vertical-align: middle; text-align: left; \" class=\"table-rh\"</span>"},{"html":""}]]}'>Place value | 7! | 6! | 5! | 4! | 3! | 2! | 1! | 0! |

style=\"background-color: var(--background-color-neutral,#eaecf0);color: var(--color-base,#202122);font-weight: bold; vertical-align: middle; text-align: left; \" class=\"table-rh\"</span>"},{"html":""}]]}'>Place value in decimal | 5040 | 720 | 120 | 24 | 6 | 2 | 1 | 1 |

style=\"background-color: var(--background-color-neutral,#eaecf0);color: var(--color-base,#202122);font-weight: bold; vertical-align: middle; text-align: left; \" class=\"table-rh\"</span>"},{"html":""}]]}'>Highest digit allowed | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |

From this it follows that the rightmost digit is always 0, the second can be 0 or 1, the third 0, 1 or 2, and so on (sequence [A124252][129] in the [OEIS][130]). The factorial number system is sometimes defined with the 0! place omitted because it is always zero (sequence [A007623][131] in the [OEIS][130]).

In this article, a factorial number representation will be flagged by a subscript "!". In addition, some examples will have digits delimited by a colon. For example, 3:4:1:0:1:0! stands for

= 3×5! + 4×4! + 1×3! + 0×2! + 1×1! + 0×0! = ((((3×5 + 4)×4 + 1)×3 + 0)×2 + 1)×1 + 0 = 463 10.

(The place value is the factorial of one less than the radix position, which is why the equation begins with 5! for a 6-digit factoradic number.)

General properties of mixed radix number systems also apply to the factorial number system. For instance, one can convert a number into factorial representation producing digits from right to left, by repeatedly dividing the number by the radix (1, 2, 3, ...), taking the remainder as digits, and continuing with the integer [quotient][132], until this quotient becomes 0.

For example, 463 10 can be transformed into a factorial representation by these successive divisions:

463 ÷ 1 = 463, remainder 0 463 ÷ 2 = 231, remainder 1 231 ÷ 3 = 77, remainder 0 77 ÷ 4 = 19, remainder 1 19 ÷ 5 = 3, remainder 4 3 ÷ 6 = 0, remainder 3 |

The process terminates when the quotient reaches zero. Reading the remainders backward gives 3:4:1:0:1:0!.

In principle, this system may be extended to represent [rational numbers][133], though rather than the natural extension of place values (−1)!, (−2)!, etc., which are undefined, the symmetric choice of radix values *n*= 0, 1, 2, 3, 4, etc. after the point may be used instead. Again, the 0 and 1 places may be omitted as these are always zero. The corresponding place values are therefore 1/1, 1/1, 1/2, 1/6, 1/24, ..., 1/*n*!, etc.

## Examples

[[edit][134]]

The following sortable table shows the 24 permutations of four elements with different [inversion][122] related vectors. The left and right inversion counts l {\displaystyle l}[image: {\displaystyle l}] and r {\displaystyle r}[image: {\displaystyle r}] (the latter often called [Lehmer code][121]) are particularly eligible to be interpreted as factorial numbers. l {\displaystyle l}[image: {\displaystyle l}] gives the permutation's position in reverse [colexicographic][135] order (the default order of this table), and the latter the position in [lexicographic][124] order (both counted from 0).

Sorting by a column that has the omissible 0 on the right makes the factorial numbers in that column correspond to the index numbers in the immovable column on the left. The small columns are reflections of the columns next to them, and can be used to bring those in colexicographic order. The rightmost column shows the digit sums of the factorial numbers ( [OEIS][130]: [A034968][136] in the tables default order).

[137] The factorial numbers of a given length form a [permutohedron][138] when ordered by the bitwise ≤ {\displaystyle \leq }[image: {\displaystyle \leq }] relation

These are the right inversion counts (aka Lehmer codes) of the permutations of four elements.

 |

0 |

1 |

2 |

3 |

4 |

5 |

6 |

7 |

8 |

9 |

10 |

11 |

12 |

13 |

14 |

15 |

16 |

17 |

18 |

19 |

20 |

21 |

22 |

23 |

 |

 | π {\displaystyle \pi }[image: {\displaystyle \pi }] |  | v {\displaystyle v}[image: {\displaystyle v}] |  |  | l {\displaystyle l}[image: {\displaystyle l}] | p-b | r {\displaystyle r}[image: {\displaystyle r}] |  | # |

0 | [139] | 1234 | 4321 | 000 0 | 0 000 | 000 0 | 0 000 | [140] | 000 0 | 0 000 | 0 |

1 | [141] | 2134 | 4312 | 100 0 | 0 001 | 001 0 | 0 100 | [142] | 100 0 | 0 001 | 1 |

2 | [143] | 1324 | 4231 | 010 0 | 0 010 | 010 0 | 0 010 | [144] | 010 0 | 0 010 | 1 |

3 | [145] | 3124 | 4213 | 110 0 | 0 011 | 011 0 | 0 110 | [146] | 200 0 | 0 002 | 2 |

4 | [147] | 2314 | 4132 | 200 0 | 0 002 | 020 0 | 0 020 | [148] | 110 0 | 0 011 | 2 |

5 | [149] | 3214 | 4123 | 210 0 | 0 012 | 021 0 | 0 120 | [150] | 210 0 | 0 012 | 3 |

6 | [151] | 1243 | 3421 | 001 0 | 0 100 | 100 0 | 0 001 | [152] | 001 0 | 0 100 | 1 |

7 | [153] | 2143 | 3412 | 101 0 | 0 101 | 101 0 | 0 101 | [154] | 101 0 | 0 101 | 2 |

8 | [155] | 1423 | 3241 | 011 0 | 0 110 | 110 0 | 0 011 | [156] | 020 0 | 0 020 | 2 |

9 | [157] | 4123 | 3214 | 111 0 | 0 111 | 111 0 | 0 111 | [158] | 300 0 | 0 003 | 3 |

10 | [159] | 2413 | 3142 | 201 0 | 0 102 | 120 0 | 0 021 | [160] | 120 0 | 0 021 | 3 |

11 | [161] | 4213 | 3124 | 211 0 | 0 112 | 121 0 | 0 121 | [162] | 310 0 | 0 013 | 4 |

12 | [163] | 1342 | 2431 | 020 0 | 0 020 | 200 0 | 0 002 | [164] | 011 0 | 0 110 | 2 |

13 | [165] | 3142 | 2413 | 120 0 | 0 021 | 201 0 | 0 102 | [166] | 201 0 | 0 102 | 3 |

14 | [167] | 1432 | 2341 | 021 0 | 0 120 | 210 0 | 0 012 | [168] | 021 0 | 0 120 | 3 |

15 | [169] | 4132 | 2314 | 121 0 | 0 121 | 211 0 | 0 112 | [170] | 301 0 | 0 103 | 4 |

16 | [171] | 3412 | 2143 | 220 0 | 0 022 | 220 0 | 0 022 | [172] | 220 0 | 0 022 | 4 |

17 | [173] | 4312 | 2134 | 221 0 | 0 122 | 221 0 | 0 122 | [174] | 320 0 | 0 023 | 5 |

18 | [175] | 2341 | 1432 | 300 0 | 0 003 | 300 0 | 0 003 | [176] | 111 0 | 0 111 | 3 |

19 | [177] | 3241 | 1423 | 310 0 | 0 013 | 301 0 | 0 103 | [178] | 211 0 | 0 112 | 4 |

20 | [179] | 2431 | 1342 | 301 0 | 0 103 | 310 0 | 0 013 | [180] | 121 0 | 0 121 | 4 |

21 | [181] | 4231 | 1324 | 311 0 | 0 113 | 311 0 | 0 113 | [182] | 311 0 | 0 113 | 5 |

22 | [183] | 3421 | 1243 | 320 0 | 0 023 | 320 0 | 0 023 | [184] | 221 0 | 0 122 | 5 |

23 | [185] | 4321 | 1234 | 321 0 | 0 123 | 321 0 | 0 123 | [186] | 321 0 | 0 123 | 6 |

 |

For another example, the greatest number that could be represented with six digits would be 543210! which equals 719 in [decimal][46]:

5×5! + 4×4! + 3x3! + 2×2! + 1×1! + 0×0!.

Clearly the next factorial number representation after 5:4:3:2:1:0! is 1:0:0:0:0:0:0! which designates 6! = 720 10, the place value for the radix-7 digit. So the former number, and its summed out expression above, is equal to:

6! − 1.

The factorial number system provides a unique representation for each natural number, with the given restriction on the "digits" used. No number can be represented in more than one way because the sum of consecutive factorials multiplied by their index is always the next factorial minus one:

∑ i = 0 n i ⋅ i! = ( n + 1)! − 1. {\displaystyle \sum _{i=0}^{n}{i\cdot i!}={(n+1)!}-1.}[image: {\displaystyle \sum _{i=0}^{n}{i\cdot i!}={(n+1)!}-1.}]

This can be easily [proved][187] with [mathematical induction][188], or simply by noticing that ∀ i, i ⋅ i! = ( i + 1 − 1) ⋅ i! = ( i + 1)! − i! {\displaystyle \forall i,i\cdot i!=(i+1-1)\cdot i!=(i+1)!-i!}[image: {\displaystyle \forall i,i\cdot i!=(i+1-1)\cdot i!=(i+1)!-i!}]: subsequent terms cancel each other, leaving the first and last term (see [Telescoping series][189]).

However, when using [Arabic numerals][5] to write the digits (and not including the subscripts as in the above examples), their simple concatenation becomes ambiguous for numbers having a "digit" greater than 9. The smallest such example is the number 10 × 10! = 36,288,000 10, which may be written A0000000000! =10:0:0:0:0:0:0:0:0:0:0!, but not 100000000000! = 1:0:0:0:0:0:0:0:0:0:0:0! which denotes 11! = 39,916,800 10. Thus using letters A–Z to denote digits 10, 11, 12, ..., 35 as in other base-*N*make the largest representable number 36 × 36! − 1. For arbitrarily greater numbers one has to choose a base for representing individual digits, say decimal, and provide a separating mark between them (for instance by subscripting each digit by its base, also given in decimal, like 2 4 0 3 1 2 0 1, this number also can be written as 2:0:1:0!). In fact the factorial number system itself is not truly a [numeral system][2] in the sense of providing a representation for all natural numbers using only a finite alphabet of symbols.

## Permutations

[[edit][190]]

There is a natural [mapping][191] between the integers 0, 1,...,*n*! − 1 (or equivalently the numbers with *n*digits in factorial representation) and [permutations][117] of *n*elements in [lexicographical][192] order, when the integers are expressed in factoradic form. This mapping has been termed the [Lehmer code][121] (or inversion table). For example, with *n*= 3, such a mapping is

decimal | factoradic | permutation |

0 10 | 0:0:0! | (0,1,2) |

1 10 | 0:1:0! | (0,2,1) |

2 10 | 1:0:0! | (1,0,2) |

3 10 | 1:1:0! | (1,2,0) |

4 10 | 2:0:0! | (2,0,1) |

5 10 | 2:1:0! | (2,1,0) |

In each case, calculating the permutation proceeds by using the leftmost factoradic digit (here, 0, 1, or 2) as the first permutation digit, then removing it from the list of choices (0, 1, and 2). Think of this new list of choices as zero indexed, and use each successive factoradic digit to choose from its remaining elements. If the second factoradic digit is "0" then the first element of the list is selected for the second permutation digit and is then removed from the list. Similarly, if the second factoradic digit is "1", the second is selected and then removed. The final factoradic digit is always "0", and since the list now contains only one element, it is selected as the last permutation digit.

The process may become clearer with a longer example. Let's say we want the 2982nd permutation of the numbers 0 through 6. The number 2982 is 4:0:4:1:0:0:0! in factoradic, and that number picks out digits (4,0,6,2,1,3,5) in turn, via indexing a dwindling ordered set of digits and picking out each digit from the set at each turn:

```
                            4:0:4:1:0:0:0!  ─►  (4,0,6,2,1,3,5)
factoradic: 4              :   0            :   4          :   1        :   0      :   0    :   0!
            ├─┬─┬─┬─┐          │                ├─┬─┬─┬─┐      ├─┐          │          │        │
sets:      (0,1,2,3,4,5,6) ─► (0,1,2,3,5,6) ─► (1,2,3,5,6) ─► (1,2,3,5) ─► (1,3,5) ─► (3,5) ─► (5)
                    │          │                        │        │          │          │        │
permutation:       (4,         0,                       6,       2,         1,         3,       5)
```

A natural index for the [direct product][193] of two [permutation groups][194] is the [concatenation][195] of two factoradic numbers, with two subscript "!"s.

```
           concatenated
 decimal   factoradics        permutation pair
    010     0:0:0!0:0:0!           ((0,1,2),(0,1,2))
    110     0:0:0!0:1:0!           ((0,1,2),(0,2,1))
               ...
    510     0:0:0!2:1:0!           ((0,1,2),(2,1,0))
    610     0:1:0!0:0:0!           ((0,2,1),(0,1,2))
    710     0:1:0!0:1:0!           ((0,2,1),(0,2,1))
               ...
   2210     1:1:0!2:0:0!           ((1,2,0),(2,0,1))
               ...
   3410     2:1:0!2:0:0!           ((2,1,0),(2,0,1))
   3510     2:1:0!2:1:0!           ((2,1,0),(2,1,0))
```

## Fractional values

[[edit][196]]

Unlike single radix systems whose place values are *base**n*for both positive and negative integral *n*, the factorial number base cannot be extended to negative place values as these would be (−1)!, (−2)! and so on, and these values are undefined (see [factorial][118]).

One possible extension is therefore to use 1/0!, 1/1!, 1/2!, 1/3!, ..., 1/*n*! etc. instead, possibly omitting the 1/0! and 1/1! places which are always zero.

With this method, all rational numbers have a terminating expansion, whose length in 'digits' is less than or equal to the denominator of the rational number represented. This may be proven by considering that there exists a factorial for any integer and therefore the denominator divides into its own factorial even if it does not divide into any smaller factorial.

By necessity, therefore, the factoradic expansion of the reciprocal of a [prime][197] has a length of exactly that prime (less one if the 1/1! place is omitted). Other terms are given as the sequence [A046021][198] on the OEIS. It can also be proven that the last 'digit' or term of the representation of a rational with prime denominator is equal to the difference between the numerator and the prime denominator.

Similar to how checking the divisibility of 4 in base 10 requires looking at only the last two digits, checking the divisibility of any number in factorial number system requires looking at only a finite number of digits. That is, it has a [divisibility rule][199] for each number.

There is also a non-terminating equivalent for every rational number akin to the fact that in decimal 0.24999... = 0.25 = 1/4 and [0.999... = 1][200], etc., which can be created by reducing the final term by 1 and then filling in the remaining infinite number of terms with the highest value possible for the radix of that position.

In the following selection of examples, spaces are used to separate the place values, otherwise represented in decimal. The rational numbers on the left are also in decimal:

- 1 / 2 = 0.0 1! {\displaystyle 1/2=0.0\ 1_{!}}[image: {\displaystyle 1/2=0.0\ 1_{!}}]
- 1 / 3 = 0.0 0 2! {\displaystyle 1/3=0.0\ 0\ 2_{!}}[image: {\displaystyle 1/3=0.0\ 0\ 2_{!}}]
- 2 / 3 = 0.0 1 1! {\displaystyle 2/3=0.0\ 1\ 1_{!}}[image: {\displaystyle 2/3=0.0\ 1\ 1_{!}}]
- 1 / 4 = 0.0 0 1 2! {\displaystyle 1/4=0.0\ 0\ 1\ 2_{!}}[image: {\displaystyle 1/4=0.0\ 0\ 1\ 2_{!}}]
- 3 / 4 = 0.0 1 1 2! {\displaystyle 3/4=0.0\ 1\ 1\ 2_{!}}[image: {\displaystyle 3/4=0.0\ 1\ 1\ 2_{!}}]
- 1 / 5 = 0.0 0 1 0 4! {\displaystyle 1/5=0.0\ 0\ 1\ 0\ 4_{!}}[image: {\displaystyle 1/5=0.0\ 0\ 1\ 0\ 4_{!}}]
- 1 / 6 = 0.0 0 1! {\displaystyle 1/6=0.0\ 0\ 1_{!}}[image: {\displaystyle 1/6=0.0\ 0\ 1_{!}}]
- 5 / 6 = 0.0 1 2! {\displaystyle 5/6=0.0\ 1\ 2_{!}}[image: {\displaystyle 5/6=0.0\ 1\ 2_{!}}]
- 1 / 7 = 0.0 0 0 3 2 0 6! {\displaystyle 1/7=0.0\ 0\ 0\ 3\ 2\ 0\ 6_{!}}[image: {\displaystyle 1/7=0.0\ 0\ 0\ 3\ 2\ 0\ 6_{!}}]
- 1 / 8 = 0.0 0 0 3! {\displaystyle 1/8=0.0\ 0\ 0\ 3_{!}}[image: {\displaystyle 1/8=0.0\ 0\ 0\ 3_{!}}]
- 1 / 9 = 0.0 0 0 2 3 2! {\displaystyle 1/9=0.0\ 0\ 0\ 2\ 3\ 2_{!}}[image: {\displaystyle 1/9=0.0\ 0\ 0\ 2\ 3\ 2_{!}}]
- 1 / 10 = 0.0 0 0 2 2! {\displaystyle 1/10=0.0\ 0\ 0\ 2\ 2_{!}}[image: {\displaystyle 1/10=0.0\ 0\ 0\ 2\ 2_{!}}]
- 1 / 11 = 0.0 0 0 2 0 5 3 1 4 0 A! {\displaystyle 1/11\ \ =0.0\ 0\ 0\ 2\ 0\ 5\ 3\ 1\ 4\ 0\ A_{!}}[image: {\displaystyle 1/11\ \ =0.0\ 0\ 0\ 2\ 0\ 5\ 3\ 1\ 4\ 0\ A_{!}}]
- 2 / 11 = 0.0 0 1 0 1 4 6 2 8 1 9! {\displaystyle 2/11\ \ =0.0\ 0\ 1\ 0\ 1\ 4\ 6\ 2\ 8\ 1\ 9_{!}}[image: {\displaystyle 2/11\ \ =0.0\ 0\ 1\ 0\ 1\ 4\ 6\ 2\ 8\ 1\ 9_{!}}]
- 9 / 11 = 0.0 1 1 3 3 1 0 5 0 8 2! {\displaystyle 9/11\ \ =0.0\ 1\ 1\ 3\ 3\ 1\ 0\ 5\ 0\ 8\ 2_{!}}[image: {\displaystyle 9/11\ \ =0.0\ 1\ 1\ 3\ 3\ 1\ 0\ 5\ 0\ 8\ 2_{!}}]
- 10 / 11 = 0.0 1 2 1 4 0 3 6 4 9 1! {\displaystyle 10/11=0.0\ 1\ 2\ 1\ 4\ 0\ 3\ 6\ 4\ 9\ 1_{!}}[image: {\displaystyle 10/11=0.0\ 1\ 2\ 1\ 4\ 0\ 3\ 6\ 4\ 9\ 1_{!}}]
- 1 / 12 = 0.0 0 0 2! {\displaystyle 1/12\ \ =0.0\ 0\ 0\ 2_{!}}[image: {\displaystyle 1/12\ \ =0.0\ 0\ 0\ 2_{!}}]
- 5 / 12 = 0.0 0 2 2! {\displaystyle 5/12\ \ =0.0\ 0\ 2\ 2_{!}}[image: {\displaystyle 5/12\ \ =0.0\ 0\ 2\ 2_{!}}]
- 7 / 12 = 0.0 1 0 2! {\displaystyle 7/12\ \ =0.0\ 1\ 0\ 2_{!}}[image: {\displaystyle 7/12\ \ =0.0\ 1\ 0\ 2_{!}}]
- 11 / 12 = 0.0 1 2 2! {\displaystyle 11/12=0.0\ 1\ 2\ 2_{!}}[image: {\displaystyle 11/12=0.0\ 1\ 2\ 2_{!}}]
- 1 / 15 = 0.0 0 0 1 3! {\displaystyle 1/15=0.0\ 0\ 0\ 1\ 3_{!}}[image: {\displaystyle 1/15=0.0\ 0\ 0\ 1\ 3_{!}}]
- 1 / 16 = 0.0 0 0 1 2 3! {\displaystyle 1/16=0.0\ 0\ 0\ 1\ 2\ 3_{!}}[image: {\displaystyle 1/16=0.0\ 0\ 0\ 1\ 2\ 3_{!}}]
- 1 / 18 = 0.0 0 0 1 1 4! {\displaystyle 1/18=0.0\ 0\ 0\ 1\ 1\ 4_{!}}[image: {\displaystyle 1/18=0.0\ 0\ 0\ 1\ 1\ 4_{!}}]
- 1 / 20 = 0.0 0 0 1 1! {\displaystyle 1/20=0.0\ 0\ 0\ 1\ 1_{!}}[image: {\displaystyle 1/20=0.0\ 0\ 0\ 1\ 1_{!}}]
- 1 / 24 = 0.0 0 0 1! {\displaystyle 1/24=0.0\ 0\ 0\ 1_{!}}[image: {\displaystyle 1/24=0.0\ 0\ 0\ 1_{!}}]
- 1 / 30 = 0.0 0 0 0 4! {\displaystyle 1/30=0.0\ 0\ 0\ 0\ 4_{!}}[image: {\displaystyle 1/30=0.0\ 0\ 0\ 0\ 4_{!}}]
- 1 / 36 = 0.0 0 0 0 3 2! {\displaystyle 1/36=0.0\ 0\ 0\ 0\ 3\ 2_{!}}[image: {\displaystyle 1/36=0.0\ 0\ 0\ 0\ 3\ 2_{!}}]
- 1 / 60 = 0.0 0 0 0 2! {\displaystyle 1/60=0.0\ 0\ 0\ 0\ 2_{!}}[image: {\displaystyle 1/60=0.0\ 0\ 0\ 0\ 2_{!}}]
- 1 / 72 = 0.0 0 0 0 1 4! {\displaystyle 1/72=0.0\ 0\ 0\ 0\ 1\ 4_{!}}[image: {\displaystyle 1/72=0.0\ 0\ 0\ 0\ 1\ 4_{!}}]
- 1 / 120 = 0.0 0 0 0 1! {\displaystyle 1/120=0.0\ 0\ 0\ 0\ 1_{!}}[image: {\displaystyle 1/120=0.0\ 0\ 0\ 0\ 1_{!}}]
- 1 / 144 = 0.0 0 0 0 0 5! {\displaystyle 1/144=0.0\ 0\ 0\ 0\ 0\ 5_{!}}[image: {\displaystyle 1/144=0.0\ 0\ 0\ 0\ 0\ 5_{!}}]
- 1 / 240 = 0.0 0 0 0 0 3! {\displaystyle 1/240=0.0\ 0\ 0\ 0\ 0\ 3_{!}}[image: {\displaystyle 1/240=0.0\ 0\ 0\ 0\ 0\ 3_{!}}]
- 1 / 360 = 0.0 0 0 0 0 2! {\displaystyle 1/360=0.0\ 0\ 0\ 0\ 0\ 2_{!}}[image: {\displaystyle 1/360=0.0\ 0\ 0\ 0\ 0\ 2_{!}}]
- 1 / 720 = 0.0 0 0 0 0 1! {\displaystyle 1/720=0.0\ 0\ 0\ 0\ 0\ 1_{!}}[image: {\displaystyle 1/720=0.0\ 0\ 0\ 0\ 0\ 1_{!}}]

There are also a small number of constants that have patterned representations with this method:

- e = 1 0.0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1...! {\displaystyle e=1\ 0.0\ 1\ 1\ 1\ 1\ 1\ 1\ 1\ 1\ 1\ 1\ 1\ 1\ 1\ 1\ 1..._{!}}[image: {\displaystyle e=1\ 0.0\ 1\ 1\ 1\ 1\ 1\ 1\ 1\ 1\ 1\ 1\ 1\ 1\ 1\ 1\ 1..._{!}}]
- e − 1 = 0.0 0 2 0 4 0 6 0 8 0 A 0 C 0 E...! {\displaystyle e^{-1}=0.0\ 0\ 2\ 0\ 4\ 0\ 6\ 0\ 8\ 0\ A\ 0\ C\ 0\ E..._{!}}[image: {\displaystyle e^{-1}=0.0\ 0\ 2\ 0\ 4\ 0\ 6\ 0\ 8\ 0\ A\ 0\ C\ 0\ E..._{!}}]
- sin ⁡ ( 1) = 0.0 1 2 0 0 5 6 0 0 9 A 0 0 D E...! {\displaystyle \sin(1)=0.0\ 1\ 2\ 0\ 0\ 5\ 6\ 0\ 0\ 9\ A\ 0\ 0\ D\ E..._{!}}[image: {\displaystyle \sin(1)=0.0\ 1\ 2\ 0\ 0\ 5\ 6\ 0\ 0\ 9\ A\ 0\ 0\ D\ E..._{!}}]
- cos ⁡ ( 1) = 0.0 1 0 0 4 5 0 0 8 9 0 0 C D 0...! {\displaystyle \cos(1)=0.0\ 1\ 0\ 0\ 4\ 5\ 0\ 0\ 8\ 9\ 0\ 0\ C\ D\ 0..._{!}}[image: {\displaystyle \cos(1)=0.0\ 1\ 0\ 0\ 4\ 5\ 0\ 0\ 8\ 9\ 0\ 0\ C\ D\ 0..._{!}}]
- sinh ⁡ ( 1) = 1.0 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0...! {\displaystyle \sinh(1)=1.0\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0..._{!}}[image: {\displaystyle \sinh(1)=1.0\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0..._{!}}]
- cosh ⁡ ( 1) = 1.0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1...! {\displaystyle \cosh(1)=1.0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1..._{!}}[image: {\displaystyle \cosh(1)=1.0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1\ 0\ 1..._{!}}]

## See also

[[edit][201]]

- [Combinatorial number system][202] (also called combinadics)
- [Profinite integers][203], which can be represented as infinite digit sequences in the factorial number system
- [Steinhaus–Johnson–Trotter algorithm][204], an algorithm that generates [Gray codes][205] for the factorial number system

## References

[[edit][206]]

1. ↑ [Knuth, D. E.][207] (1973), "Volume 3: Sorting and Searching", *[The Art of Computer Programming][208]*, Addison-Wesley, p. 12, [ISBN][209] [0-201-89685-0][210]
2. ↑ [Cantor, G.][125] (1869), *Zeitschrift für Mathematik und Physik*, vol. 14.
3. ↑ [Knuth, D. E.][207] (1997), "Volume 2: Seminumerical Algorithms", *The Art of Computer Programming*(3rd ed.), Addison-Wesley, p. 192, [ISBN][209] [0-201-89684-2][211].
4. ↑ [Laisant, Charles-Ange][212] (1888), ["Sur la numération factorielle, application aux permutations"][213], *Bulletin de la Société Mathématique de France*(in French), **16**: 176– 183.
5. ↑ The term "factoradic" is apparently introduced in [McCaffrey, James][214] (2003), **[Using Permutations in .NET for Improved Systems Security][215], Microsoft Developer Network.

- Mantaci, Roberto; Rakotondrajao, Fanja (2001), ["A permutation representation that knows what "Eulerian" means"][216] (PDF), *Discrete Mathematics and Theoretical Computer Science*, **4**: 101– 108, archived from [the original][217] (PDF) on 2011-05-24, retrieved 2005-03-27.
- Arndt, Jörg (2010). **[Matters Computational: Ideas, Algorithms, Source Code][218]. pp. 232– 238.

## External links

[[edit][219]]

- [A Lehmer code calculator][220] Note that their permutation digits start from 1, so mentally reduces all permutation digits by one to get results equivalent to those on this page.
- [Factorial number system][221]

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Factorial_number_system&oldid=1309641022][222] "

[Categories][223]:

- [Combinatorics][224]
- [Factorial and binomial topics][225]
- [Non-standard positional numeral systems][226]

Hidden categories:

- [Articles with short description][227]
- [Short description is different from Wikidata][228]
- [Pages using sidebar with the child parameter][229]
- [Articles needing additional references from March 2021][230]
- [All articles needing additional references][231]
- [CS1 French-language sources (fr)][232]

Search

Factorial number system

9 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/Category:Numeral_systems
[2]: https://en.wikipedia.org/wiki/Numeral_system
[3]: https://en.wikipedia.org/wiki/Positional_notation
[4]: https://en.wikipedia.org/wiki/Hindu–Arabic_numeral_system
[5]: https://en.wikipedia.org/wiki/Arabic_numerals
[6]: https://en.wikipedia.org/wiki/Eastern_Arabic_numerals
[7]: https://en.wikipedia.org/wiki/Bengali_numerals
[8]: https://en.wikipedia.org/wiki/Devanagari_numerals
[9]: https://en.wikipedia.org/wiki/Gujarati_numerals
[10]: https://en.wikipedia.org/wiki/Gurmukhi_numerals
[11]: https://en.wikipedia.org/wiki/Odia_numerals
[12]: https://en.wikipedia.org/wiki/Sinhala_numerals
[13]: https://en.wikipedia.org/wiki/Tamil_numerals
[14]: https://en.wikipedia.org/wiki/Malayalam_numerals
[15]: https://en.wikipedia.org/wiki/Telugu_script#Numerals
[16]: https://en.wikipedia.org/wiki/Kannada_script#Numerals
[17]: https://en.wikipedia.org/wiki/Dzongkha_numerals
[18]: https://en.wikipedia.org/wiki/Tibetan_numerals
[19]: https://en.wikipedia.org/wiki/Balinese_numerals
[20]: https://en.wikipedia.org/wiki/Burmese_numerals
[21]: https://en.wikipedia.org/wiki/Javanese_numerals
[22]: https://en.wikipedia.org/wiki/Khmer_numerals
[23]: https://en.wikipedia.org/wiki/Lao_script#Numerals
[24]: https://en.wikipedia.org/wiki/Mongolian_numerals
[25]: https://en.wikipedia.org/wiki/Sundanese_numerals
[26]: https://en.wikipedia.org/wiki/Thai_numerals
[27]: https://en.wikipedia.org/wiki/History_of_ancient_numeral_systems
[28]: https://en.wikipedia.org/wiki/Ancient_history
[29]: https://en.wikipedia.org/wiki/Babylonian_cuneiform_numerals
[30]: https://en.wikipedia.org/wiki/Post-classical_history
[31]: https://en.wikipedia.org/wiki/Cistercian_numerals
[32]: https://en.wikipedia.org/wiki/Maya_numerals
[33]: https://en.wikipedia.org/wiki/Muisca_numerals
[34]: https://en.wikipedia.org/wiki/Pentadic_numerals
[35]: https://en.wikipedia.org/wiki/Quipu
[36]: https://en.wikipedia.org/wiki/Rumi_Numeral_Symbols
[37]: https://en.wikipedia.org/wiki/Cherokee_syllabary#Numerals
[38]: https://en.wikipedia.org/wiki/Kaktovik_numerals
[39]: https://en.wikipedia.org/wiki/Radix
[40]: https://en.wikipedia.org/wiki/Binary_number
[41]: https://en.wikipedia.org/wiki/Ternary_numeral_system
[42]: https://en.wikipedia.org/wiki/Quaternary_numeral_system
[43]: https://en.wikipedia.org/wiki/Quinary
[44]: https://en.wikipedia.org/wiki/Senary
[45]: https://en.wikipedia.org/wiki/Octal
[46]: https://en.wikipedia.org/wiki/Decimal
[47]: https://en.wikipedia.org/wiki/Undecimal
[48]: https://en.wikipedia.org/wiki/Duodecimal
[49]: https://en.wikipedia.org/wiki/Hexadecimal
[50]: https://en.wikipedia.org/wiki/Vigesimal
[51]: https://en.wikipedia.org/wiki/Sexagesimal
[52]: https://en.wikipedia.org/wiki/Non-standard_positional_numeral_systems
[53]: https://en.wikipedia.org/wiki/Bijective_numeration
[54]: https://en.wikipedia.org/wiki/Unary_numeral_system
[55]: https://en.wikipedia.org/wiki/Signed-digit_representation
[56]: https://en.wikipedia.org/wiki/Balanced_ternary
[57]: https://en.wikipedia.org/wiki/Mixed_radix
[58]: https://en.wikipedia.org/wiki/Factorial_number_system
[59]: https://en.wikipedia.org/wiki/Negative_base
[60]: https://en.wikipedia.org/wiki/Complex-base_system
[61]: https://en.wikipedia.org/wiki/Quater-imaginary_base
[62]: https://en.wikipedia.org/wiki/Non-integer_base_of_numeration
[63]: https://en.wikipedia.org/wiki/Golden_ratio_base
[64]: https://en.wikipedia.org/wiki/Asymmetric_numeral_systems
[65]: https://en.wikipedia.org/wiki/Sign-value_notation
[66]: https://en.wikipedia.org/wiki/Chinese_numerals
[67]: https://en.wikipedia.org/wiki/Hokkien_numerals
[68]: https://en.wikipedia.org/wiki/Suzhou_numerals
[69]: https://en.wikipedia.org/wiki/Japanese_numerals
[70]: https://en.wikipedia.org/wiki/Korean_numerals
[71]: https://en.wikipedia.org/wiki/Vietnamese_numerals
[72]: https://en.wikipedia.org/wiki/Counting_rods
[73]: https://en.wikipedia.org/wiki/Tangut_numerals
[74]: https://en.wikipedia.org/wiki/Aegean_numerals
[75]: https://en.wikipedia.org/wiki/Attic_numerals
[76]: https://en.wikipedia.org/wiki/Aztec_script#Numerals
[77]: https://en.wikipedia.org/wiki/Brahmi_numerals
[78]: https://en.wikipedia.org/wiki/Chuvash_numerals
[79]: https://en.wikipedia.org/wiki/Egyptian_numerals
[80]: https://en.wikipedia.org/wiki/Etruscan_numerals
[81]: https://en.wikipedia.org/wiki/Kharosthi_numerals
[82]: https://en.wikipedia.org/wiki/Prehistoric_counting
[83]: https://en.wikipedia.org/wiki/Proto-cuneiform
[84]: https://en.wikipedia.org/wiki/Roman_numerals
[85]: https://en.wikipedia.org/wiki/Tally_marks
[86]: https://en.wikipedia.org/wiki/Alphabetic_numeral_system
[87]: https://en.wikipedia.org/wiki/Abjad_numerals
[88]: https://en.wikipedia.org/wiki/Armenian_numerals
[89]: https://en.wikipedia.org/wiki/Alphasyllabic_numeral_system
[90]: https://en.wikipedia.org/wiki/Aksharapalli
[91]: https://en.wikipedia.org/wiki/Āryabhaṭa_numeration
[92]: https://en.wikipedia.org/wiki/Katapayadi_system
[93]: https://en.wikipedia.org/wiki/Coptic_numerals
[94]: https://en.wikipedia.org/wiki/Cyrillic_numerals
[95]: https://en.wikipedia.org/wiki/Geʽez_script#Numerals
[96]: https://en.wikipedia.org/wiki/Georgian_numerals
[97]: https://en.wikipedia.org/wiki/Glagolitic_numerals
[98]: https://en.wikipedia.org/wiki/Greek_numerals
[99]: https://en.wikipedia.org/wiki/Hebrew_numerals
[100]: https://en.wikipedia.org/wiki/List_of_numeral_systems
[101]: https://en.wikipedia.org/wiki/Template:Numeral_systems
[102]: https://en.wikipedia.org/wiki/Template_talk:Numeral_systems
[103]: https://en.wikipedia.org/wiki/Special:EditPage/Template:Numeral_systems
[104]: https://en.wikipedia.org/wiki/File:Question_book-new.svg
[105]: https://en.wikipedia.org/wiki/Wikipedia:Verifiability
[106]: https://en.wikipedia.org/wiki/Special:EditPage/Factorial_number_system
[107]: https://en.wikipedia.org/wiki/Help:Referencing_for_beginners
[108]: https://en.wikipedia.org/wiki/Wikipedia:Verifiability#Burden_of_evidence
[109]: https://www.google.com/search?as_eq=wikipedia&amp;q=%22Factorial+number+system%22
[110]: https://www.google.com/search?tbm=nws&amp;q=%22Factorial+number+system%22+-wikipedia&amp;tbs=ar:1
[111]: https://www.google.com/search?amp;q=%22Factorial+number+system%22&amp;tbs=bkt:s&amp;tbm=bks
[112]: https://www.google.com/search?tbs=bks:1&amp;q=%22Factorial+number+system%22+-wikipedia
[113]: https://scholar.google.com/scholar?q=%22Factorial+number+system%22
[114]: https://www.jstor.org/action/doBasicSearch?Query=%22Factorial+number+system%22&amp;acc=on&amp;wc=on
[115]: https://en.wikipedia.org/wiki/Help:Maintenance_template_removal
[116]: https://en.wikipedia.org/wiki/Combinatorics
[117]: https://en.wikipedia.org/wiki/Permutation
[118]: https://en.wikipedia.org/wiki/Factorial
[119]: https://en.wikipedia.org/wiki/Place_value
[120]: https://en.wikipedia.org/wiki/Sequence
[121]: https://en.wikipedia.org/wiki/Lehmer_code
[122]: https://en.wikipedia.org/wiki/Inversion_(discrete_mathematics)
[123]: https://en.wikipedia.org/wiki/Integer
[124]: https://en.wikipedia.org/wiki/Lexicographical_order
[125]: https://en.wikipedia.org/wiki/Georg_Cantor
[126]: https://en.wikipedia.org/wiki/Donald_Knuth
[127]: https://en.wikipedia.org/wiki/Portmanteau
[128]: /w/index.php?title=Factorial_number_system&amp;action=edit&amp;section=1
[129]: //oeis.org/A124252
[130]: https://en.wikipedia.org/wiki/On-Line_Encyclopedia_of_Integer_Sequences
[131]: //oeis.org/A007623
[132]: https://en.wikipedia.org/wiki/Quotient
[133]: https://en.wikipedia.org/wiki/Rational_number
[134]: /w/index.php?title=Factorial_number_system&amp;action=edit&amp;section=2
[135]: https://en.wikipedia.org/wiki/Colexicographical_order
[136]: //oeis.org/A034968
[137]: https://en.wikipedia.org/wiki/File:Symmetric_group_4;_permutohedron_3D;_Lehmer_codes.svg
[138]: https://en.wikipedia.org/wiki/Permutohedron
[139]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_00.svg
[140]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_00.svg
[141]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_01.svg
[142]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_01.svg
[143]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_02.svg
[144]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_02.svg
[145]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_03.svg
[146]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_03.svg
[147]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_04.svg
[148]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_04.svg
[149]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_05.svg
[150]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_05.svg
[151]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_06.svg
[152]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_06.svg
[153]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_07.svg
[154]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_07.svg
[155]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_08.svg
[156]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_08.svg
[157]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_09.svg
[158]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_09.svg
[159]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_10.svg
[160]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_10.svg
[161]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_11.svg
[162]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_11.svg
[163]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_12.svg
[164]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_12.svg
[165]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_13.svg
[166]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_13.svg
[167]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_14.svg
[168]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_14.svg
[169]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_15.svg
[170]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_15.svg
[171]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_16.svg
[172]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_16.svg
[173]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_17.svg
[174]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_17.svg
[175]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_18.svg
[176]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_18.svg
[177]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_19.svg
[178]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_19.svg
[179]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_20.svg
[180]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_20.svg
[181]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_21.svg
[182]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_21.svg
[183]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_22.svg
[184]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_22.svg
[185]: https://en.wikipedia.org/wiki/File:4-el_perm_matrix_23.svg
[186]: https://en.wikipedia.org/wiki/File:4-el_perm_invset_23.svg
[187]: https://en.wikipedia.org/wiki/Mathematical_proof
[188]: https://en.wikipedia.org/wiki/Mathematical_induction
[189]: https://en.wikipedia.org/wiki/Telescoping_series
[190]: /w/index.php?title=Factorial_number_system&amp;action=edit&amp;section=3
[191]: https://en.wikipedia.org/wiki/Function_(mathematics)
[192]: https://en.wikipedia.org/wiki/Lexicographical
[193]: https://en.wikipedia.org/wiki/Direct_product_of_groups
[194]: https://en.wikipedia.org/wiki/Permutation_group
[195]: https://en.wikipedia.org/wiki/Concatenation
[196]: /w/index.php?title=Factorial_number_system&amp;action=edit&amp;section=4
[197]: https://en.wikipedia.org/wiki/Prime_number
[198]: https://oeis.org/A046021
[199]: https://en.wikipedia.org/wiki/Divisibility_rule
[200]: https://en.wikipedia.org/wiki/0.999...
[201]: /w/index.php?title=Factorial_number_system&amp;action=edit&amp;section=5
[202]: https://en.wikipedia.org/wiki/Combinatorial_number_system
[203]: https://en.wikipedia.org/wiki/Profinite_integer
[204]: https://en.wikipedia.org/wiki/Steinhaus–Johnson–Trotter_algorithm
[205]: https://en.wikipedia.org/wiki/Gray_code
[206]: /w/index.php?title=Factorial_number_system&amp;action=edit&amp;section=6
[207]: https://en.wikipedia.org/wiki/Donald_Ervin_Knuth
[208]: https://en.wikipedia.org/wiki/The_Art_of_Computer_Programming
[209]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[210]: https://en.wikipedia.org/wiki/Special:BookSources/0-201-89685-0
[211]: https://en.wikipedia.org/wiki/Special:BookSources/0-201-89684-2
[212]: https://en.wikipedia.org/wiki/Charles-Ange_Laisant
[213]: http://www.numdam.org/item?id=BSMF_1888__16__176_0
[214]: https://en.wikipedia.org/wiki/James_D._McCaffrey
[215]: http://msdn2.microsoft.com/en-us/library/aa302371.aspx
[216]: https://web.archive.org/web/20110524210428/http://www.dmtcs.org/volumes/abstracts/pdfpapers/dm040203.pdf
[217]: http://www.dmtcs.org/volumes/abstracts/pdfpapers/dm040203.pdf
[218]: http://www.jjj.de/fxt/#fxtbook
[219]: /w/index.php?title=Factorial_number_system&amp;action=edit&amp;section=7
[220]: https://web.archive.org/web/20050115122923/http://www-ang.kfunigraz.ac.at/~fripert/fga/k1lehm.html
[221]: http://archive.numdam.org/ARCHIVE/BSMF/BSMF_1888__16_/BSMF_1888__16__176_0/BSMF_1888__16__176_0.pdf
[222]: https://en.wikipedia.org/w/index.php?title=Factorial_number_system&amp;oldid=1309641022
[223]: /wiki/Help:Category
[224]: /wiki/Category:Combinatorics
[225]: /wiki/Category:Factorial_and_binomial_topics
[226]: /wiki/Category:Non-standard_positional_numeral_systems
[227]: /wiki/Category:Articles_with_short_description
[228]: /wiki/Category:Short_description_is_different_from_Wikidata
[229]: /wiki/Category:Pages_using_sidebar_with_the_child_parameter
[230]: /wiki/Category:Articles_needing_additional_references_from_March_2021
[231]: /wiki/Category:All_articles_needing_additional_references
[232]: /wiki/Category:CS1_French-language_sources_(fr)
