<!-- source: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Szekeres_theorem | converted from HTML -->

Erdős–Szekeres theorem - Wikipedia

Jump to content

From Wikipedia, the free encyclopedia

Sufficiently long sequences of numbers have long monotonic subsequences

[1] A path of four upward-sloping edges in a set of 17 points. By the Erdős–Szekeres theorem, every set of 17 points has a path of this length that slopes either upward or downward. The 16-point subset with the central point removed has no such path.

In [mathematics][2], the **Erdős–Szekeres theorem**asserts that, given r {\displaystyle r}[image: {\displaystyle r}] and s {\displaystyle s}[image: {\displaystyle s}], any sequence of distinct real numbers with length at least ( r − 1) ( s − 1) + 1 {\displaystyle (r-1)(s-1)+1}[image: {\displaystyle (r-1)(s-1)+1}] contains a monotonically increasing subsequence of length*r**or*a monotonically decreasing subsequence of length*s*. The proof appeared in the same 1935 paper that mentions the [Happy Ending problem][3]. [1]

It is a finitary result that makes precise one of the corollaries of [Ramsey's theorem][4]. While Ramsey's theorem makes it easy to prove that every infinite sequence of distinct real numbers contains a monotonically increasing infinite [subsequence][5]*or*a monotonically decreasing infinite subsequence, the result proved by [Paul Erdős][6] and [George Szekeres][7] goes further.

## Example

[[edit][8]]

For *r*= 3 and *s*= 2, the formula tells us that any permutation of three numbers has an increasing subsequence of length three or a decreasing subsequence of length two. Among the six permutations of the numbers 1,2,3:

- ⟨ 1, 2, 3 ⟩ {\displaystyle \langle 1,2,3\rangle }[image: {\displaystyle \langle 1,2,3\rangle }] has an increasing subsequence consisting of all three numbers.
- ⟨ 1, 3, 2 ⟩ {\displaystyle \langle 1,3,2\rangle }[image: {\displaystyle \langle 1,3,2\rangle }] has a decreasing subsequence ⟨ 3, 2 ⟩ {\displaystyle \langle 3,2\rangle }[image: {\displaystyle \langle 3,2\rangle }]
- ⟨ 2, 1, 3 ⟩ {\displaystyle \langle 2,1,3\rangle }[image: {\displaystyle \langle 2,1,3\rangle }] has a decreasing subsequence ⟨ 2, 1 ⟩ {\displaystyle \langle 2,1\rangle }[image: {\displaystyle \langle 2,1\rangle }]
- ⟨ 2, 3, 1 ⟩ {\displaystyle \langle 2,3,1\rangle }[image: {\displaystyle \langle 2,3,1\rangle }] has two decreasing subsequences, ⟨ 2, 1 ⟩ {\displaystyle \langle 2,1\rangle }[image: {\displaystyle \langle 2,1\rangle }] and ⟨ 3, 1 ⟩ {\displaystyle \langle 3,1\rangle }[image: {\displaystyle \langle 3,1\rangle }]
- ⟨ 3, 1, 2 ⟩ {\displaystyle \langle 3,1,2\rangle }[image: {\displaystyle \langle 3,1,2\rangle }] has two decreasing subsequences, ⟨ 3, 1 ⟩ {\displaystyle \langle 3,1\rangle }[image: {\displaystyle \langle 3,1\rangle }] and ⟨ 3, 2 ⟩ {\displaystyle \langle 3,2\rangle }[image: {\displaystyle \langle 3,2\rangle }]
- ⟨ 3, 2, 1 ⟩ {\displaystyle \langle 3,2,1\rangle }[image: {\displaystyle \langle 3,2,1\rangle }] has three decreasing length-2 subsequences, ⟨ 3, 2 ⟩ {\displaystyle \langle 3,2\rangle }[image: {\displaystyle \langle 3,2\rangle }], ⟨ 3, 1 ⟩ {\displaystyle \langle 3,1\rangle }[image: {\displaystyle \langle 3,1\rangle }] and ⟨ 2, 1 ⟩ {\displaystyle \langle 2,1\rangle }[image: {\displaystyle \langle 2,1\rangle }].

## Alternative interpretations

[[edit][9]]

### Geometric interpretation

[[edit][10]]

One can interpret the positions of the numbers in a sequence as *x*-coordinates of points in the [Euclidean plane][11], and the numbers themselves as *y*-coordinates; conversely, for any point set in the plane, the *y*-coordinates of the points, ordered by their *x*-coordinates, forms a sequence of numbers (unless two of the points have equal *x*-coordinates). With this translation between sequences and point sets, the Erdős–Szekeres theorem can be interpreted as stating that in any set of at least *rs*−*r*−*s*+ 2 points we can find a [polygonal path][12] of either *r*− 1 positive-slope edges or *s*− 1 negative-slope edges. In particular (taking *r*=*s*), in any set of at least *n*points we can find a polygonal path of at least ⌊ √*n*-1 ⌋ edges with same-sign slopes. For instance, taking *r*=*s*= 5, any set of at least 17 points has a four-edge path in which all slopes have the same sign.

An example of *rs*−*r*−*s*+ 1 points without such a path, showing that this bound is tight, can be formed by applying a small rotation to an (*r*− 1)-by-(*s*− 1) grid.

### Permutation pattern interpretation

[[edit][13]]

The Erdős–Szekeres theorem may also be interpreted in the language of [permutation patterns][14] as stating that every permutation of length at least (*r*− 1)(*s*− 1) + 1 must contain the pattern 12⋯*r*or the pattern *s*⋯21.

## Proofs

[[edit][15]]

The Erdős–Szekeres theorem can be proved in several different ways; Steele (1995) surveys six different proofs of the Erdős–Szekeres theorem, including the following two. [2] Other proofs surveyed by Steele include the original proof by Erdős and Szekeres as well as those of Blackwell (1971), [3] Hammersley (1972), [4] and Lovász (1979). [5]

### Pigeonhole principle

[[edit][16]]

Given a sequence of length (*r*− 1)(*s*− 1) + 1, label each number *n i*in the sequence with the pair (*a i*, *b i*), where *a i*is the length of the longest monotonically increasing subsequence ending with *n i*and *b i*is the length of the longest monotonically decreasing subsequence ending with *n i*. Each two numbers in the sequence are labeled with a different pair: if *i*< *j*and i</sub>'' < ''n<sub>j</sub>''"}},"i":0}}]}'>*n i*< *n j*then i</sub>'' < ''a<sub>j</sub>''"}},"i":0}}]}'>*a i*< *a j*, and on the other hand if i</sub>'' > ''n<sub>j</sub>''"}},"i":0}}]}'>*n i*> *n j*then i</sub>'' < ''b<sub>j</sub>''"}},"i":0}}]}'>*b i*< *b j*. But there are only (*r*− 1)(*s*− 1) possible labels if *a i*is at most *r*− 1 and *b i*is at most *s*− 1, so by the [pigeonhole principle][17] there must exist a value of *i*for which *a i*or *b i*is outside this range. If *a i*is out of range then *n i*is part of an increasing sequence of length at least *r*, and if *b i*is out of range then *n i*is part of a decreasing sequence of length at least *s*.

Steele (1995) credits this proof to the one-page paper of Seidenberg (1959) and calls it "the slickest and most systematic" of the proofs he surveys. [2] [6]

### Dilworth's theorem

[[edit][18]]

Another of the proofs uses [Dilworth's theorem][19] on chain decompositions in partial orders, or its simpler dual ( [Mirsky's theorem][20]).

To prove the theorem, define a partial ordering on the members of the sequence, in which *x*is less than or equal to *y*in the partial order if *x*≤*y*as numbers and *x*is not later than *y*in the sequence. A chain in this partial order is a monotonically increasing subsequence, and an [antichain][21] is a monotonically decreasing subsequence. By Mirsky's theorem, either there is a chain of length *r*, or the sequence can be partitioned into at most *r*− 1 antichains; but in that case the largest of the antichains must form a decreasing subsequence with length at least

⌈ r s − r − s + 2 r − 1 ⌉ = s. {\displaystyle \left\lceil {\frac {rs-r-s+2}{r-1}}\right\rceil =s.}[image: {\displaystyle \left\lceil {\frac {rs-r-s+2}{r-1}}\right\rceil =s.}]

Alternatively, by Dilworth's theorem itself, either there is an antichain of length *s*, or the sequence can be partitioned into at most *s*− 1 chains, the longest of which must have length at least*r*.

### Application of the Robinson–Schensted correspondence

[[edit][22]]

The result can also be obtained as a corollary of the [Robinson–Schensted correspondence][23].

Recall that the Robinson–Schensted correspondence associates to each sequence a [Young tableau][24]*P*whose entries are the values of the sequence. The tableau *P*has the following properties:

- The length of the longest increasing subsequence is equal to the length of the first row of *P*.
- The length of the longest decreasing subsequence is equal to the length of the first column of *P*.

Now, it is not possible to fit (*r*− 1)(*s*− 1) + 1 entries in a square box of size (*r*− 1)(*s*− 1), so that either the first row is of length at least *r*or the last row is of length at least *s*.

## See also

[[edit][25]]

- [Longest increasing subsequence problem][26]

## References

[[edit][27]]

1. ↑ [Erdős, Paul][6]; [Szekeres, George][7] (1935), ["A combinatorial problem in geometry"][28], *[Compositio Mathematica][29]*, **2**: 463– 470, [Zbl][30] [0012.27010][31]; reprinted in *Classic Papers in Combinatorics*(Springer, 2008), pp. 49–56, [doi][32]: [10.1007/978-0-8176-4842-8_3][33], [ISBN][34] [978-0-8176-4841-1][35]
2. 1 2 [Steele, J. Michael][36] (1995), "Variations on the monotone subsequence theme of Erdős and Szekeres", in [Aldous, David][37]; [Diaconis, Persi][38]; [Spencer, Joel][39]; [Steele, J. Michael][36] (eds.), **[Discrete Probability and Algorithms][40] (PDF), IMA Volumes in Mathematics and its Applications, vol. 72, Springer-Verlag, pp. 111– 131, [ISBN][34] [0-387-94532-6][41].
3. ↑ Blackwell, Paul (1971), "An alternative proof of a theorem of Erdős and Szekeres", *[American Mathematical Monthly][42]*, **78**(3): 273, [doi][32]: [10.2307/2317525][43], [JSTOR][44] [2317525][45].
4. ↑ [Hammersley, J. M.][46] (1972), "A few seedlings of research", *Proc. 6th Berkeley Symp. Math. Stat. Prob.*, University of California Press, pp. 345– 394. As cited by Steele (1995).
5. ↑ [Lovász, László][47] (1979), "Solution to Exercise 14.25", *Combinatorial Problems and Exercises*, North-Holland. As cited by Steele (1995).
6. ↑ [Seidenberg, A.][48] (1959), "A simple proof of a theorem of Erdős and Szekeres", *[Journal of the London Mathematical Society][49]*, **34**(3): 352, [doi][32]: [10.1112/jlms/s1-34.3.352][50]

## External links

[[edit][51]]

- [Weisstein, Eric W.][52], ["Erdős-Szekeres Theorem"][53], *[MathWorld][54]*

Retrieved from " [https://en.wikipedia.org/w/index.php?title=Erdős–Szekeres_theorem&oldid=1360671181][55] "

[Categories][56]:

- [Ramsey theory][57]
- [Permutation patterns][58]
- [Theorems in discrete geometry][59]
- [Paul Erdős][60]
- [Theorems in discrete mathematics][61]

Hidden categories:

- [Articles with short description][62]
- [Short description is different from Wikidata][63]
- [Articles containing proofs][64]

Search

Erdős–Szekeres theorem

11 languages Add topic


## Links

[1]: https://en.wikipedia.org/wiki/File:Monotone-subseq-17-5.svg
[2]: https://en.wikipedia.org/wiki/Mathematics
[3]: https://en.wikipedia.org/wiki/Happy_Ending_problem
[4]: https://en.wikipedia.org/wiki/Ramsey's_theorem
[5]: https://en.wikipedia.org/wiki/Subsequence
[6]: https://en.wikipedia.org/wiki/Paul_Erdős
[7]: https://en.wikipedia.org/wiki/George_Szekeres
[8]: /w/index.php?title=Erd%C5%91s%E2%80%93Szekeres_theorem&amp;action=edit&amp;section=1
[9]: /w/index.php?title=Erd%C5%91s%E2%80%93Szekeres_theorem&amp;action=edit&amp;section=2
[10]: /w/index.php?title=Erd%C5%91s%E2%80%93Szekeres_theorem&amp;action=edit&amp;section=3
[11]: https://en.wikipedia.org/wiki/Euclidean_plane
[12]: https://en.wikipedia.org/wiki/Polygonal_path
[13]: /w/index.php?title=Erd%C5%91s%E2%80%93Szekeres_theorem&amp;action=edit&amp;section=4
[14]: https://en.wikipedia.org/wiki/Permutation_pattern
[15]: /w/index.php?title=Erd%C5%91s%E2%80%93Szekeres_theorem&amp;action=edit&amp;section=5
[16]: /w/index.php?title=Erd%C5%91s%E2%80%93Szekeres_theorem&amp;action=edit&amp;section=6
[17]: https://en.wikipedia.org/wiki/Pigeonhole_principle
[18]: /w/index.php?title=Erd%C5%91s%E2%80%93Szekeres_theorem&amp;action=edit&amp;section=7
[19]: https://en.wikipedia.org/wiki/Dilworth's_theorem
[20]: https://en.wikipedia.org/wiki/Mirsky's_theorem
[21]: https://en.wikipedia.org/wiki/Antichain
[22]: /w/index.php?title=Erd%C5%91s%E2%80%93Szekeres_theorem&amp;action=edit&amp;section=8
[23]: https://en.wikipedia.org/wiki/Robinson–Schensted_correspondence
[24]: https://en.wikipedia.org/wiki/Young_tableau
[25]: /w/index.php?title=Erd%C5%91s%E2%80%93Szekeres_theorem&amp;action=edit&amp;section=9
[26]: https://en.wikipedia.org/wiki/Longest_increasing_subsequence_problem
[27]: /w/index.php?title=Erd%C5%91s%E2%80%93Szekeres_theorem&amp;action=edit&amp;section=10
[28]: http://www.numdam.org/item?id=CM_1935__2__463_0
[29]: https://en.wikipedia.org/wiki/Compositio_Mathematica
[30]: https://en.wikipedia.org/wiki/Zbl_(identifier)
[31]: https://zbmath.org/?format=complete&amp;q=an:0012.27010
[32]: https://en.wikipedia.org/wiki/Doi_(identifier)
[33]: https://doi.org/10.1007%2F978-0-8176-4842-8_3
[34]: https://en.wikipedia.org/wiki/ISBN_(identifier)
[35]: https://en.wikipedia.org/wiki/Special:BookSources/978-0-8176-4841-1
[36]: https://en.wikipedia.org/wiki/J._Michael_Steele
[37]: https://en.wikipedia.org/wiki/David_Aldous
[38]: https://en.wikipedia.org/wiki/Persi_Diaconis
[39]: https://en.wikipedia.org/wiki/Joel_Spencer
[40]: http://www-stat.wharton.upenn.edu/~steele/Publications/PDF/VOTMSTOEAS.pdf
[41]: https://en.wikipedia.org/wiki/Special:BookSources/0-387-94532-6
[42]: https://en.wikipedia.org/wiki/American_Mathematical_Monthly
[43]: https://doi.org/10.2307%2F2317525
[44]: https://en.wikipedia.org/wiki/JSTOR_(identifier)
[45]: https://www.jstor.org/stable/2317525
[46]: https://en.wikipedia.org/wiki/John_Hammersley
[47]: https://en.wikipedia.org/wiki/László_Lovász
[48]: https://en.wikipedia.org/wiki/Abraham_Seidenberg
[49]: https://en.wikipedia.org/wiki/Journal_of_the_London_Mathematical_Society
[50]: https://doi.org/10.1112%2Fjlms%2Fs1-34.3.352
[51]: /w/index.php?title=Erd%C5%91s%E2%80%93Szekeres_theorem&amp;action=edit&amp;section=11
[52]: https://en.wikipedia.org/wiki/Eric_W._Weisstein
[53]: https://mathworld.wolfram.com/Erdos-SzekeresTheorem.html
[54]: https://en.wikipedia.org/wiki/MathWorld
[55]: https://en.wikipedia.org/w/index.php?title=Erdős–Szekeres_theorem&amp;oldid=1360671181
[56]: /wiki/Help:Category
[57]: /wiki/Category:Ramsey_theory
[58]: /wiki/Category:Permutation_patterns
[59]: /wiki/Category:Theorems_in_discrete_geometry
[60]: /wiki/Category:Paul_Erd%C5%91s
[61]: /wiki/Category:Theorems_in_discrete_mathematics
[62]: /wiki/Category:Articles_with_short_description
[63]: /wiki/Category:Short_description_is_different_from_Wikidata
[64]: /wiki/Category:Articles_containing_proofs
