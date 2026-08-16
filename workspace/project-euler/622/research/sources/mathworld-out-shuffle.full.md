<!-- source: https://mathworld.wolfram.com/Out-Shuffle.html | converted from HTML -->

Out-Shuffle -- from Wolfram MathWorld

# Out-Shuffle

---

[image: DOWNLOAD Mathematica Notebook] [Download Wolfram Notebook][1]

An out-shuffle, also known as a perfect shuffle (Golomb 1961), is a [riffle shuffle][2] in which the top half of the deck is placed in the right hand, and cards are then alternatively interleaved from the right and left hands. In other words, an out-shuffle on a deck of [image: 2n] cards separates the bottom [image: n] cards from the top [image: n] cards and precisely interleaves them, with the bottom card remaining on the bottom (Golomb 1961).

Using an out-shuffle, a deck originally arranged as 1 2 3 4 5 6 7 8 would become 1 5 2 6 3 7 4 8. The ordering of a deck of 52 cards after an out-shuffle is given by 1, 27, 2, 28, 3, 29, ... (OEIS [A059953][3]).

Out-shuffling an even number [image: n] cards [image: n-2] times when [image: n-1] is prime results in the original order (Conway and Guy 1996).

The numbers of out-shuffles needed to return a deck of [image: n=2], 4, ... to its original order are 1, 2, 4, 3, 6, 10, 12, 4, 8, 18, 6, 11, ... (OEIS [A002326][4]), which is simply the [multiplicative order][5] of 2 (mod [image: n-1]). For example, a deck of 52 cards therefore is returned to its original state after eight out-shuffles, since [image: 2^8=1 (mod 51)] (Golomb 1961). The smallest numbers of cards [image: 2n] that require 1, 2, 3, ... out-shuffles to return to the deck's original state are 1, 2, 4, 3, 16, 5, 64, 9, 37, 6, ... (OEIS [A114894][6]).

An out-shuffle on an infinite deck was considered by Gale (1992). Take an infinite deck of cards labeled 1, 2, 3, 4, 5, 6, .... At step [image: n], pick up the top [image: n] cards and interlace them with the next [image: n] cards. This is called a perfect [image: n] -shuffle. For example, after step two, we have 3, 2, 4, 1, 5, 6, 7, .... For step three, pick up 3, 2, 4 and shuffle them in, giving 1, 3, 5, 2, 6, 4, 7, 8, 9, .... Iterate this process. It is conjectured that eventually every number appears on top of the deck.

The cards on top of deck at the [image: n] th step are 1, 2, 3, 1, 6, 5, 9, 1, 4, 2, 16, 10, 12, ... (OEIS [A035485][7]). The step at which card [image: n] first appears on top the deck is given by 0, 1, 2, 8, 5, 4, 78, 37, ... (OEIS [A035490][8]). The position of the first card after the [image: n] th shuffle is 1, 2, 4, 1, 2, 4, 8, 1, 2, 4, 8, 16, 7, 14, 28, ... (OEIS [A035492][9]). The order in which new cards appear on top for the first time is 1, 2, 3, 6, 5, 9, 4, 16, 10, ... (OEIS [A035493][10]). The order in which record new high cards appear on top for the first time is 1, 2, 3, 6, 9, 16, ... (OEIS [A035494][11]).

---

## See also

[In-Shuffle][12], [Kimberling Sequence][13], [Riffle Shuffle][2], [Shuffle][14]

## Explore with Wolfram|Alpha

[image: WolframAlpha]

More things to try:

- [bridge][15]
- [cards][16]
- [30-sided polyhedron][17]

## References

Conway, J. H. and Guy, R. K. "Fractions Cycle into Decimals." In *[The Book of Numbers.][18]*New York: Springer-Verlag, pp. 163-165, 1996. Gale, D. "Mathematical Entertainments: Careful Card-Shuffling and Cutting Can Create Chaos." *Math. Intell.***14**, 54-56, 1992. Gale, D. *[Tracking the Automatic Ant and Other Mathematical Explorations, A Collection of Mathematical Entertainments Columns from The Mathematical Intelligencer.][19]*New York: Springer-Verlag, 1998. Golomb, S. W. "Permutations by Cutting and Shuffling." *SIAM Rev.***3**, 293-297, 1961. Sloane, N. J. A. Sequences [A002326][4] /M0936, [A035485][7], [A035490][8], [A035492][9], [A035493][10], [A035494][11], [A059953][3], and [A114894][6] in "The On-Line Encyclopedia of Integer Sequences."

## Referenced on Wolfram|Alpha

[Out-Shuffle][20]

## Cite this as:

[Weisstein, Eric W.][21] "Out-Shuffle." From **[MathWorld][22] --A Wolfram Resource. [https://mathworld.wolfram.com/Out-Shuffle.html][23]

## Subject classifications


## Links

[1]: /notebooks/Games/Out-Shuffle.nb
[2]: /RiffleShuffle.html
[3]: http://oeis.org/A059953
[4]: http://oeis.org/A002326
[5]: /MultiplicativeOrder.html
[6]: http://oeis.org/A114894
[7]: http://oeis.org/A035485
[8]: http://oeis.org/A035490
[9]: http://oeis.org/A035492
[10]: http://oeis.org/A035493
[11]: http://oeis.org/A035494
[12]: /In-Shuffle.html
[13]: /KimberlingSequence.html
[14]: /Shuffle.html
[15]: https://www.wolframalpha.com/input/?i=bridge
[16]: https://www.wolframalpha.com/input/?i=cards
[17]: https://www.wolframalpha.com/input/?i=30-sided+polyhedron
[18]: http://www.amazon.com/exec/obidos/ASIN/038797993X/ref=nosim/ericstreasuretro
[19]: http://www.amazon.com/exec/obidos/ASIN/0387982728/ref=nosim/ericstreasuretro
[20]: https://www.wolframalpha.com/input/?i=out-shuffle
[21]: /about/author.html
[22]: /
[23]: https://mathworld.wolfram.com/Out-Shuffle.html
