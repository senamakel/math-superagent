<!-- source: https://mathworld.wolfram.com/GilbreathsConjecture.html | converted from HTML -->

Gilbreath's Conjecture -- from Wolfram MathWorld

# Gilbreath's Conjecture

---

[image: DOWNLOAD Mathematica Notebook] [Download Wolfram Notebook][1]

Let the [difference][2] of successive [primes][3] be defined by [image: d_n=p_(n+1)-p_n], and [image: d_n^k] by

[image:  d_n^k={d_n   for k=1; |d_(n+1)^(k-1)-d_n^(k-1)|   for k>1. ] |

(1)

 |

N. L. Gilbreath claimed that [image: d_1^k=1] for all [image: k] (Guy 1994). In 1959, the claim was verified for [image: k<63419]. In 1993, Odlyzko extended the claim to all [primes][3] up to [image: pi(10^(13))].

Gilbreath's conjecture is equivalent to the statement that, in the triangular array of the primes, iteratively taking the [absolute difference][4] of each pair of terms

[image:  2,3,5,7,11,13,17,19,23,29,...
1,2,2,4,2,4,2,4,6,...
1,0,2,2,2,2,2,2,...
1,2,0,0,0,0,0,...
1,2,0,0,0,0,...
1,2,0,0,0,...
1,2,0,0,...
1,2,0,...
1,2,...
1,...  ] |

(2)

 |

(OEIS [A036262][5]), always gives leading term 1 (after the first row).

The number of terms before reaching the first greater than two in the second, third, etc., rows are given by 3, 8, 14, 14, 25, 23, 22, 25, ... (OEIS [A000232][6]).

---

## See also

[Prime Difference Function][7]

## Explore with Wolfram|Alpha

[image: WolframAlpha]

More things to try:

- [abc conjecture][8]
- [Andrica's conjecture][9]
- [5 dice][10]

## References

Caldwell, C. K. "Gilbreath's Conjecture." [https://t5k.org/glossary/page.php?sort=GilbreathsConjecture][11]. Debono, A. N. "Numbers and Computers (11): More on Primes." [http://www.eng.um.edu.mt/~andebo/numbers/numcom11.htm][12]. Gardner, M. "Patterns in Primes Are a Clue to the Strong Law of Small Numbers." *Sci. Amer.***243**, 18-28, Dec. 1980. Guy, R. K. "Gilbreath's Conjecture." &sect;A10 in *[Unsolved Problems in Number Theory, 2nd ed.][13]*New York: Springer-Verlag, pp. 25-26, 1994. Kilgrove, R. B. and Ralston, K. E. "On a Conjecture concerning the Primes." *Math. Tables Aids Comput.***13**, 121-122, 1959. Odlyzko, A. M. "Iterated Absolute Values of Differences of Consecutive Primes." *Math. Comput.***61**, 373-380, 1993. Proth, F. "Sur la s&eacute;rie des nombres premiers." *Nouv. Corresp. Math***4**, 236-240, 1878. Sloane, N. J. A. Sequences [A000232][6] /M2718 and [A036262][5] in "The On-Line Encyclopedia of Integer Sequences."

## Referenced on Wolfram|Alpha

[Gilbreath's Conjecture][14]

## Cite this as:

[Weisstein, Eric W.][15] "Gilbreath's Conjecture." From **[MathWorld][16] --A Wolfram Resource. [https://mathworld.wolfram.com/GilbreathsConjecture.html][17]

## Subject classifications


## Links

[1]: /notebooks/PrimeNumbers/GilbreathsConjecture.nb
[2]: /Difference.html
[3]: /PrimeNumber.html
[4]: /AbsoluteDifference.html
[5]: http://oeis.org/A036262
[6]: http://oeis.org/A000232
[7]: /PrimeDifferenceFunction.html
[8]: https://www.wolframalpha.com/input/?i=abc+conjecture
[9]: https://www.wolframalpha.com/input/?i=Andrica%27s+conjecture
[10]: https://www.wolframalpha.com/input/?i=5+dice
[11]: https://t5k.org/glossary/page.php?sort=GilbreathsConjecture
[12]: http://www.eng.um.edu.mt/~andebo/numbers/numcom11.htm
[13]: http://www.amazon.com/exec/obidos/ASIN/0387208607/ref=nosim/ericstreasuretro
[14]: https://www.wolframalpha.com/input/?i=gilbreaths+conjecture
[15]: /about/author.html
[16]: /
[17]: https://mathworld.wolfram.com/GilbreathsConjecture.html
