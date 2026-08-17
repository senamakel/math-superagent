<!-- source: https://mathworld.wolfram.com/RabbitSequence.html | converted from HTML -->

Rabbit Sequence -- from Wolfram MathWorld

# Rabbit Sequence

---

[image: DOWNLOAD Mathematica Notebook] [Download Wolfram Notebook][1]

[image: Rabbit sequence recurrence plot]

A [sequence][2] which arises in the hypothetical reproduction of a population of rabbits. Let the [substitution system][3] map [image: 0->1] correspond to young rabbits growing old, and [image: 1->10] correspond to old rabbits producing young rabbits. Starting with 0 and iterating using [string rewriting][4] gives the terms 1, 10, 101, 10110, 10110101, 1011010110110, .... A [recurrence plot][5] of the limiting value of this sequence is illustrated above.

Converted to [decimal][6], this sequence gives 1, 2, 5, 22, 181, ... (OEIS [A005203][7]), with the [image: n] th term given by the [recurrence relation][8]

[image:  a(n)=a(n-1)2^(F_(n-1))+a(n-2), ] |

with [image: a(0)=0], [image: a(1)=1], and [image: F_n] the [image: n] th [Fibonacci number][9].

The limiting sequence written as a [binary][10] [fraction][11][image: 0.1011010110110..._2] (OEIS [A005614][12]), where [image: (a_n...a_1a_0)_2] denotes a [binary number][10] (i.e., a number written in base 2, so [image: a_i=0] or 1), is called the [rabbit constant][13].

---

## See also

[Fibonacci Number][9], [Rabbit Constant][13], [Thue-Morse Sequence][14]

## Explore with Wolfram|Alpha

[image: WolframAlpha]

More things to try:

- [Fibonacci numbers][15]
- [beta distribution][16]
- [exponential fit 0.783,0.552,0.383,0.245,0.165,0.097][17]

## References

Davison, J. L. "A Series and Its Associated Continued Fraction." *Proc. Amer. Math. Soc.***63**, 29-32, 1977. Gould, H. W.; Kim, J. B.; and Hoggatt, V. E. Jr. "Sequences Associated with *t*-ary Coding of Fibonacci's Rabbits." *Fib. Quart.***15**, 311-318, 1977. Schroeder, M. *[Fractals, Chaos, Power Laws: Minutes from an Infinite Paradise.][18]*New York: W. H. Freeman, p. 55, 1991. Sloane, N. J. A. Sequences [A005203][7] /M1539 and [A005614][12] in "The On-Line Encyclopedia of Integer Sequences."

## Referenced on Wolfram|Alpha

[Rabbit Sequence][19]

## Cite this as:

[Weisstein, Eric W.][20] "Rabbit Sequence." From **[MathWorld][21] --A Wolfram Resource. [https://mathworld.wolfram.com/RabbitSequence.html][22]

## Subject classifications


## Links

[1]: /notebooks/IntegerSequences/RabbitSequence.nb
[2]: /Sequence.html
[3]: /SubstitutionSystem.html
[4]: /StringRewritingSystem.html
[5]: /RecurrencePlot.html
[6]: /Decimal.html
[7]: http://oeis.org/A005203
[8]: /RecurrenceRelation.html
[9]: /FibonacciNumber.html
[10]: /Binary.html
[11]: /Fraction.html
[12]: http://oeis.org/A005614
[13]: /RabbitConstant.html
[14]: /Thue-MorseSequence.html
[15]: https://www.wolframalpha.com/input/?i=Fibonacci+numbers
[16]: https://www.wolframalpha.com/input/?i=beta+distribution
[17]: https://www.wolframalpha.com/input/?i=exponential+fit+0.783%2C0.552%2C0.383%2C0.245%2C0.165%2C0.097
[18]: http://www.amazon.com/exec/obidos/ASIN/0716723573/ref=nosim/ericstreasuretro
[19]: https://www.wolframalpha.com/input/?i=rabbit+sequence
[20]: /about/author.html
[21]: /
[22]: https://mathworld.wolfram.com/RabbitSequence.html
