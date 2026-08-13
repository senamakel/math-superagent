<!-- source: https://www.ics.uci.edu/~eppstein/numth/egypt/intro.html | converted from HTML -->

Algorithms for Egyptian Fractions

## Introduction

When we use fractional numbers today, there are two ways we usually represent them: as fractions (ratios of integers) such as 5/6, and as decimal numbers such as 0.8333. Computers typically use binary versions of either of these two representations. But these are not the only possibilities. The ancient Egyptians used a third method: instead of writing down a single fraction, they would write a sum of several distinct *unit fractions, *each having numerator one. For instance the Egyptians would have written 5/6 as 1/2 + 1/3 (of course, they would have used hieroglyphics instead of Arabic numerals). Today such sums are known as *Egyptian fractions. *(We will see another important modern representation, *continued fractions, *later.)

Any number has infinitely many Egyptian fraction representations, although there are only finitely many having a given number of terms [[Ste92]][1] It is not known how the Egyptians found their representations, but today many algorithms are known for this problem, each behaving differently in terms of the number of unit fractions produced, the size of the denominators of the fractions, and the time taken to find the representations. For a good but brief introduction to Egyptian fraction algorithms and their implementation in *Mathematica*, see Wagon's book [[Wag91]][2]. Here we examine a number of algorithms in more detail, implement them, and analyze their performance. We also include some investigations into how many unit fractions are needed to represent rational numbers having small numerators.

We will represent Egyptian fractions as lists of unit fractions. The original rational number represented by such a list can be recovered by Plus@@%. Throughout we use q to denote the rational number we are trying to represent, or x/y when we want to talk about its numerator and denominator separately.

An earlier version of this notebook was published as "Ten Algorithms for Egyptian Fractions" in *Mathematica in Education and Research.*I have since improved the [binary remainder method][3], and added the [reverse greedy][4], [.generalized remainder, and small multiple][5] methods.

[Methods Based on Approximation][6] [Conflict Resolution Methods][7] [Methods Based on the Binary Number System][8] [Continued Fraction Methods][9] [Reverse Greedy Methods][4] [Brute Force Methods][5] [Small Numerators][10] [References][11]


## Links

[1]: refs.html#Ste92
[2]: refs.html#Wag91
[3]: binary.html#binrem
[4]: greed.html
[5]: force.html
[6]: approx.html
[7]: conflict.html
[8]: binary.html
[9]: cfrac.html
[10]: smallnum.html
[11]: refs.html
