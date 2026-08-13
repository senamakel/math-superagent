> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/eppstein-anti-gilbreath-sequences.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://11011110.github.io/blog/2011/02/20/anti-gilbreath-sequences.html | converted from HTML -->

Anti-Gilbreath sequences

[&laquo; Gilbreath made practical][1] [The sad case of Ike Antkare &raquo;][2]

Here's a followup to my post yesterday about [a practical variant][1] of [Gilbreath's conjecture][3]. Recall that the conjecture concerns a triangle of numbers in which the primes run down the left edge of the triangle and each other number is the difference of the two numbers to its left; Gilbreath conjectured that the numbers on the right edge are all 1. Many sources on this problem repeat a statement by Hallard Croft that the conjecture has nothing to do with prime numbers, and that every sequence that has similar general properties to the primes (all numbers but the first having different parity from the first number, slow growth rate, and small gaps) would have the same property.

But it isn't true.

Instead, for any unbounded monotonic function \( f(n) \ge 2 \), no matter how slowly growing, there is a sequence \( X \) whose \( n \)th gap is at most \( f(n) \) and whose triangle's right edge switches between \( 1 \) and other values infinitely often.

To see this, suppose that we have already settled on the first few values of some sequence \( X \), and have generated a triangle from that prefix. For instance, \( X \) might start off like the sequence of primes:

```
  2
  3 1
  5 2 1
  7 2 0 1
 11 4 2 2 1
 13 2 2 0 2 1
 17 4 2 0 0 2 1
 19 2 2 0 0 0 2 1
 23 4 2 0 0 0 0 2 1
 29 6 2 0 0 0 0 0 2 1
 31 2 4 2 2 2 2 2 2 0 1
```

Let \( g_i \) be the number in the second column of row \( i \) (the gap between two consecutive numbers in the defining sequence) and let \( s_i \) be the sum of all of the entries on row \( i − 1 \) other than the first and the last one. For instance, in the row beginning \( 29 \), this sum is \( 6+2+2=10 \), but in the row beginning \( 31 \) it is \( 2+4+2+2+2+2+2+2=18 \), much larger. The significance of this definition is that, if the gap is larger than the row sum, then the rightmost number in that row will be their difference (minus one). For instance, if we replaced \( 31 \) by \( 43 \) we would have a big gap, bigger than the previous row sum:

```
  2
  3  1
  5  2  1
  7  2  0  1
 11  4  2  2  1
 13  2  2  0  2  1
 17  4  2  0  0  2  1
 19  2  2  0  0  0  2  1
 23  4  2  0  0  0  0  2  1
 29  6  2  0  0  0  0  0  2  1
 43 14  8  6  6  6  6  6  6  4  3
```

In this example, the gap \( g_i \) is \( 14 \), while the previous row sum \( s_i \) is only \( 10 \), so the gap is big enough to survive differencing with all the entries in the row above it and escape to the right side of the triangle giving us a big value there.

But maybe \( 14 \) is too big a gap to be allowed at this point in the sequence? No problem! We just need to control the sequence in such a way that the row sums remain small while the gap limit grows, so that in some later row the gap limit will exceed the row sum.

To do so, extend the triangle a row at a time, working backwards from the right side of the row (rather than forwards from the left) to determine the values in each row. More specifically, starting from the triangle we have already computed, the positions under the final "1" in our partial triangle should form a column of 2s, and the positions to the right of them should all be zero. To the left of the column of 2s, each number is calculated as either the sum or the difference of the numbers above and to the right, choosing the difference when possible so that the numbers all stay small.

Starting again from our partial triangle of prime numbers, this gives us:

```
  2
  3 1
  5 2 1
  7 2 0 1
 11 4 2 2 1
 13 2 2 0 2 1
 17 4 2 0 0 2 1
 19 2 2 0 0 0 2 1
 23 4 2 0 0 0 0 2 1
 29 6 2 0 0 0 0 0 2 1
 31 2 4 2 2 2 2 2 2 0 1
 35 4 2 2 0 2 0 2 0 2 2 1
 39 4 0 2 0 0 2 2 0 0 2 0 1
 43 4 0 0 2 2 2 0 2 2 2 0 0 1
 47 4 0 0 0 2 0 2 2 0 2 0 0 0 1
 51 4 0 0 0 0 2 2 0 2 2 0 0 0 0 1

*[excerpt ends; 2672 characters not shown — see `research/sources/eppstein-anti-gilbreath-sequences.full.md`]*
