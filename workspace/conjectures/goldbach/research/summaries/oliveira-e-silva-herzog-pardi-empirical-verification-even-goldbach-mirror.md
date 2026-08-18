> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/oliveira-e-silva-herzog-pardi-empirical-verification-even-goldbach-mirror.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://denisevellachemla.eu/empirical-verification-of-the-even-CG.pdf | converted from PDF -->

## What it claims

Abstract. This paper describes how the even Goldbach conjecture was con-
ﬁrmed to be true for all even numbers not larger than 4 · 1018. Usingaresult
of Ramar´e and Saouter, it follows that the odd Goldbach conjecture is true
up to 8.37 · 1026. The empirical data collected during this extensive veriﬁca-
tion eﬀort, namely, counts and ﬁrst occurrences of so-called minimal Goldbach
partitions with a given smallest prime and of gaps between consecutive primes
with a given even gap, are used to test several conjectured formulas related
to prime numbers. In particular, the counts of minimal Goldbach partitions
and of prime gaps are in excellent accord with the predictions made using the
prime k-tuple conjecture of Hardy and Littlewood (with an error that appears
to be O(√t log log t), where t is the true value of the quantity being estimated).
Prime gap moments also show excellent agreement with a generalization of a
conjecture made in 1982 by Heath-Brown.

The Goldbach conjecture [13] is a famous mathematical problem whose proof, or
disproof, has so far resisted the passage of time [20,…

## Statements it makes

Algorithm 1.1 (Segmented Eratosthenes sieve [3]). To generate all odd primes in
the interval (A, B),with B> A > 0,with A even, with K and Δ integers, and with
B = A +2KΔ, do:
1. [Initialize.] Set a to A and b to A +2Δ.Set j to 2.
2. [New interval.] Set m0,m1,... ,m∆−1 to 1.Set i to 2.
3. [New primes.] If p2 ≥ b then advance to step 5.
4. If p2 <a then set oj to (
2pj − 1 − (a + pj)mod (2pj))
/2; otherwise set oj
to (p2 − a − 1)/2.Add 1 to j and go back to step 3.
Comment: a +2oj +1 is the smallest odd multiple of pj larger than a that
needs to be considered.
5. [Mark composites.] If i ≥ j then advance to step 8.
6. If oi ≥ Δ then subtract Δ to oi, add 1 to i, and go back to step 5.
7. Set…

Algorithm 1.2 (Cache-eﬃcient segmented Eratosthenes sieve). To generate all
odd primes in the interval (A, B),with B> A > 0,with A even, with K and Δ
integers, and with B = A +2KΔ, do:

Algorithm 1.3 (Computation of the minimal Goldbach partition of n). To com-
pute the minimal Goldbach partition n = p(n)+ q(n), do:
1. [Initialize.] Set i to 2.
2. [Test.] If 2pi >n then terminate, stating that there is no Goldbach partition
of n.
3. If n − pi is prime, then set p(n) to pi and q(n) to n − pi,and terminate.
4. [Try next prime.] Increase i andgoback tostep2.

Algorithm 1.4 (Computation of the minimal Goldbach partition of all even num-
bers belonging to an interval). To compute the minimal Goldbach partition for all
even numbers belonging to the interval (C, D),with C and D odd, do:
1. [Initialize.] Set I to a value that depends on D and on the processor model
(see below). Set J to (pI +1)/2.Set L to (D − C)/2.Set u0, u1, ...,
uL+J−1 to zero.
Comment: ui will contain information about the smallest prime in the min-
imal Goldbach partition of C +1+2i.
2. [Mark.] For each prime q belonging to the interval (C − 3,D − 3),ordered
in increasing order, do step 3 (a subroutine) with j set to (q − C)/2.After
all primes q have been dealt with, go to step…

Theorem 2.1. Each odd number larger than 5 and smaller than

*[digest of a 118650 character source; every section, statement, and proof in full at `research/sources/oliveira-e-silva-herzog-pardi-empirical-verification-even-goldbach-mirror.full.md`]*
