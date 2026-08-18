<!-- source: https://mathworld.wolfram.com/RabbitSequence.html | captured via read_sources, 2026 -->

# Rabbit Sequence -- from Wolfram MathWorld

A sequence which arises in the hypothetical reproduction of a population of
rabbits. Let the substitution system map correspond to young rabbits growing
old, and correspond to old rabbits producing young rabbits. Starting with 0 and
iterating using string rewriting gives the terms 1, 10, 101, 10110, 10110101,
1011010110110, .... A recurrence plot of the limiting value of this sequence is
illustrated above.

Converted to decimal, this sequence gives 1, 2, 5, 22, 181, ... (OEIS A005203),
with the n-th term given by the recurrence relation a(n) = a(n-1)*2^F(n-1) +
a(n-2), with a(0)=1, a(1)=2, and F(n) the n-th Fibonacci number.

The limiting sequence written as a binary fraction (OEIS A005614), where
0.1011010110110...2 denotes a binary number (i.e., a number written in base 2,
so 0 or 1), is called the rabbit constant.

## See also

Fibonacci Number, Rabbit Constant, Thue-Morse Sequence

## References

Davison, J. L. "A Series and Its Associated Continued Fraction." Proc. Amer.
Math. Soc. 63, 29-32, 1977. Gould, H. W.; Kim, J. B.; and Hoggatt, V. E. Jr.
"Sequences Associated with t-ary Coding of Fibonacci's Rabbits." Fib. Quart.
15, 311-318, 1977. Schroeder, M. Fractals, Chaos, Power Laws: Minutes from an
Infinite Paradise. New York: W. H. Freeman, p. 55, 1991. Sloane, N. J. A.
Sequences A005203/M1539 and A005614 in "The On-Line Encyclopedia of Integer
Sequences."

## Cite this as:

Weisstein, Eric W. "Rabbit Sequence." From MathWorld--A Wolfram Web Resource.
https://mathworld.wolfram.com/RabbitSequence.html
