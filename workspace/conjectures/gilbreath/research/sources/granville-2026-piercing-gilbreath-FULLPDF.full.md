<!-- source: https://arxiv.org/pdf/2607.04166 (v3, cs.CR, 14 Jul 2026) | pdftotext -layout of the FULL PDF, not the abstract page -->

                                              Piercing Gilbreath’s Conjecture: From Deep Number Theory
                                                          Insights to Fintech and Cybersecurity

                                                                      Vincent Granville, Ph.D. | CAIO | vincent@BondingAI.io
                                                                               BondingAI.io, version 1.0, July 2026


                                                                                                   Abstract
                                                   I propose a new methodology to attack the fascinating Gilbreath’s conjecture about prime numbers, first
                                               posted in 1878 and unsolved to this day. The problem statement is rudimentary: kids can understand it.
                                               However, despite decades of research, almost no progress has been made. This paper changes the game by
                                               presenting a new approach based on sieving, a number of new results with proof, a precise path to the solu-
                                               tion, and solid references. It also introduces the concept of reverse sieving, along with applications to testing
                                               randomness, pattern and fraud detection, cybersecurity, synthetic data, sequence categorization and nor-
                                               malization, or to detect and quantify a new type of chaos in time series including Brownian motions. Magic
                                               primes, forbidden prime number constellations, cellular automata, and reduction via classes of equivalent
                                               sequences, are some of the innovative and promising topics discussed in the paper.


                                         Contents
                                         1 Introduction                                                                                                            1




arXiv:2607.04166v3 [cs.CR] 14 Jul 2026
                                         2 Proof for sifted sequences: standard and reverse sieving                                                                2

                                         3 Full list of short sequences and sequence categorization                                                                5
                                           3.1 Testing an exhaustive infinite list of admissible short sequences . . . . . . . . . . . . . . . . . . .             5
                                           3.2 Efficient sequence corridors . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .          6
                                           3.3 Hidden patterns causing failures . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .            8

                                         4 Synthetic sequences with Poisson gaps to mimic prime numbers                                               9
                                           4.1 High performance computing to discover rare failure patterns . . . . . . . . . . . . . . . . . . . . 10
                                           4.2 Prime gaps and forbidden prime constellations . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

                                         5 A deeper version of Gilbreath’s conjecture with partial proof                                                           12
                                           5.1 Distance between a successful sequence and its closest failing sister . . . . . . . . . . . . . . . . .             12
                                           5.2 General framework, proof for magic primes and other cases . . . . . . . . . . . . . . . . . . . . .                 14
                                           5.3 Canonical form reduction and equivalence classes for sequences . . . . . . . . . . . . . . . . . . .                19

                                         6 Applications: cybersecurity, fraud detection and Fintech                                                                21
                                           6.1 Hidden patterns, error detection, checksum, and data quality audit . . . . . . . . . . . . . . . . .                21
                                           6.2 Fraud detection and transaction score synthesis . . . . . . . . . . . . . . . . . . . . . . . . . . . .             22
                                           6.3 Cellular automata random generator and new tests of randomness . . . . . . . . . . . . . . . . .                    22
                                           6.4 Unusual patterns in time series: modeling, detection and synthesis . . . . . . . . . . . . . . . . .                24
                                           6.5 Security issues in ciphers relying on prime numbers . . . . . . . . . . . . . . . . . . . . . . . . . .             25

                                         7 Conclusions                                                                                                             25

                                         References                                                                                                                25

                                         A Appendix: Python code                                                                                           27
                                           A.1 Main program . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
                                           A.2 Gilbreath library . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33


                                         1    Introduction
                                         The Gilbreath conjecture is a celebrated mathematical problem tied to prime numbers, first raised by François
                                         Proth in 1878 and unsolved to this day, despite numerous attempts and computational verification up to primes
                                         larger than 1014 in 2025 [26]. In 2023, Zachary Chase proved an analog for random integers with very small
                                         growth (much smaller than prime numbers), see [6]. But the problem for the prime numbers sequence remains
                                         fully open. However, Chase’s proof generated renewed interest and fruitful discussions, notably by well-known
                                         mathematician Juan Arias de Reyna, see here. In an earlier blog posted here in 2011, computer scientist David


                                                                                                      1
Eppstein shares a different version of the conjecture, applicable to practical numbers, a type of integers derived
from Egyptian fractions with a distribution similar to that of primes. See also recent paper by Leila Muney [24].



          2       3       5       7       11 13 17 19 23 29 31                                     2       3       5       7       11 13 17 23 31 41 43
      6       1       2       2       4       2       4       2       4       6       2       10       1       2       2       4       2       4       6       8       10       2
      4           1       0       2       2       2       2       2       2       4           8            1       0       2       2       2       2       2       2        8
      2               1       2       0       0       0       0       0       2               6                1       2       0       0       0       0       0       6
      2                   1       2       0       0       0       0       2                   6                    1       2       0       0       0       0       6
      2                       1       2       0       0       0       2                       6                        1       2       0       0       0       6
      2                           1       2       0       0       2                           6                            1       2       0       0       6
      2                               1       2       0       2                               6                                1       2       0       6
      2                                   1       2       2                                   6                                    1       2       6
      1                                       1       0                                       4                                        1       4
      1                                           1                                           3                                            3

              Table 1: Prime numbers, one of many                                                      Table 2: Removing a few primes from
               sequences verifying the conjecture                                                       the sequence invalidates the result


Gilbreath’s conjecture is illustrated in table 1: the successive differences of adjacent numbers, in absolute value,
all start with 1 when the original sequence at the top consists of the prime numbers. Whether you look at the
first 20 primes, the first 1014 , or all of them. Remove a few primes in the list, and you get the counter-example
featured in table 2. The leftmost column (left to the triangle) represents the maximum value at each level. It
contains all the critical information towards understanding the mechanics behind the scene.
     Surprisingly, the conjecture has nothing to do with prime numbers nor even their distribution. It works
for plenty of sequences, some growing much faster, some much slower than primes, and even with oscillations
or full chaos (Brownian motions, see figure 8), even with negative numbers. Yet, the proof sketch outlined in
this article heavily relies on properties of prime numbers. It is as if the prime numbers are the ideal candidate,
leading to simplifications not attainable with arbitrary numbers that also satisfy the conjecture. In the end,
the core result is that in order to verify the conjecture, the sequence can be chaotic in certain specific ways
(I called it constrained chaos), or smooth but again with specific constraints. The prime numbers happen to
meet those constraints. Other curious sequences are listed in OEIS entry A358691, here, including Fibonacci
numbers leading to periodicity in the left diagonal of the triangle instead of 1’s.
     Understanding what is going on in tables 1 and 2, and what broke the nice pattern in the latter, is critical
to build a proof of the conjecture. In short, in the bottom table, we skipped the primes 19, 29, and 37. This
accelerated the growth and introduced higher values in the first differences, including a 10. But that alone did
not kill the pattern. What killed it is the prime 43, not because it was too large compared to 41 (the classic way
to crash), but because it was too small. This resulted in a very high value in the second differences, given its
short length: the number 8 circled in yellow. If you replace 43 by 45, it will work.
     In layman’s term, you can visualize the problem as follows. You are a pilot about to take off. The runway
in front of you is the triangle. It ends in the bottom row: your either fly if the bottom number is 1, otherwise
you crash. The yellow light flashing on your dashboard tells you something is not right. The column left to the
triangle tells your speed: the higher the value, the lower the speed. Your dashboard tells you that you are not
accelerating fast enough. And at that low acceleration rate, you don’t have enough runway to take off.


2     Proof for sifted sequences: standard and reverse sieving
If the original sequence (the row above the triangle) has n elements, then the corresponding triangle has n − 1
rows called levels, labeled from 1 at the top to n − 1 at the bottom. The maximum value at level k is denoted
as γ(k) and called the depth at level k, with 1 ≤ k ≤ n − 1. In my implementation, by design I stop growing
the sequence (adding new elements to the right), and thus the size of the triangle, when one of the following
two conditions is met:
    • We arrived at the bottom row: either with a 1 (called success), or with a number > 1 (called failure).
    • At any level, the leftmost element is not 1 (called failure). In short, we stop at the first level where this
      problem occurs, if it ever does.
As a result, my triangles always have a 1 on the left at each level except possibly for the last level consisting
of one element. For infinite sequences, I look at all finite subsequences of increasing length. To be marked as
success, all finite subsequences must be marked as success. I now state a few fundamental yet trivial results.


                                                                                          2
Theorem 2.1 All integers in the triangle are even, except the first one on the left at each level, which is odd.
Also, the depth function γ(k) is a non-increasing function. Finally, if we reach γ(k0 ) = 2 at some level k0 , we
can stop: we know for certain that the end result will be a success.
Proof: For two positive integers x, y we always have |x − y| ≤ min(x, y). Thus from one level to the next, the
values can not increase, insuring that the maximum value γ(k + 1) at level k + 1 cannot be larger than γ(k).
Now, if γ(k0 ) = 2 at some level k0 , then γ(k) ≤ 2 for all k > k0 . Since the length of each row in the triangle
decreases by 1 each time we increase k, we eventually reach a level with 2 elements: the one on the left equal
to 1, and the one the right equal to 0 or 2. The next level is the final one, and consists of one element equal to
either |0 − 1| or |2 − 1|. Either way, it is equal to 1, that is, success. □

The minimum k0 satisfying γ(k0 ) = 2, if it exists, is called the regularity coefficient of the sequence. If there
is no such k0 , the sequence is said to be irregular. In case of success, typically (but not always), γ(k) decays
exponentially fast, but it can stay at γ(k) = 2 for a large number of k before ending on 1. Thus, stopping the
computations as soon as we find k0 with γ(k0 ) = 2 can save much time for very large sequences, or when testing
a large number of small sequences.
Theorem 2.2 Modifying, removing, or adding new elements to a sequence does not modify the sub-triangle on
the left, attached to the unchanged terms on the left to where the changes start occurring.
Proof: Compare tables 1 and 2. The first seven elements 2, 3, 5, 7, 11, 13, 17 are common to both sequences. The
corresponding sub-triangles are identical. Generalization is straightforward. This is true whether the numbers
are prime or not, and whether the sequence is finite or infinite. □

Theorem 2.2 is useful in the following context. Let’s pn be the last element in a finite sequence of length n
that is marked as successful. You want to add one element pn+1 . What are the possible values for pn+1 so that
the augmented sequence is also successful? In many cases, any odd pn+1 in [ pn , 2pn ] will work. In even more
cases, any odd pn+1 in [ pn , 1.2 pn ] works. This is interesting, since Nagura’s theorem, published in 1952, states
that there is always a prime number in the interval [ pn , 1.2 pn ] if pn ≥ 25. One would think that this proves
Gilbreath’s conjecture, as it guarantees that you can always find the next prime within the prescribed range to
grow the sequence indefinitely, eventually covering all primes, while preserving success at all times. However,
the counter-example in table 2 is a huge blow to this strategy.
    Examples like table 2 are exotic and rare. Whether there are finitely or infinitely many of them is unknown.
And while you would expect such exceptions to occur only in short sequences that are otherwise well behaved,
no one knows if it could also happen in sequences of arbitrary length. The idea might be worth pursing, but it
does not appear as an easy path to prove the conjecture. Before stating the next theorem, let’s call an infinite
sequence ∆-periodic if its first-order differences eventually become periodic.
Theorem 2.3 If the sequence is ∆-periodic, looking at the numbers up to the first full period cycle, is enough to
decide about its success: it turns an infinite problem into a finite one. In particular, starting with the sequence
of all integers > 1, then removing even numbers except p1 = 2, then removing multiples of 3 except p2 = 3, then
removing multiples of 5 except p3 = 5, yields a successful ∆-periodic sequence denoted as S3 . This remains true
if we continue the iterations with p4 , p5 and so on up to p8 = 19, leading to successful S8 .
Proof: All the differences (first, second order and so on) must have the same period. Thus all values within each
level will keep repeating themselves with the same period. You only need to look at the first cycle and pre-period
values. This proves the first part of the theorem. Now solving the second part.
   • Removing all even numbers and adding back 2 yields γ(1) = 2. So, we are done at the first level thanks
     to theorem 2.1. The period has length 1 and starts at position 2 in the first order differences.
   • Removing all multiples of 3 and adding back 3, after the previous step, yields γ(1) = 4 and γ(2) = 2. So,
     we are done at the second level. Now, the period has length 2 and starts at position 3 in the first order
     differences.
   • Removing all multiples of 5 and adding back 5, after the two previous steps, yields γ(1) = 6, γ(2) = 4 and
     γ(3) = 2. So, we are done at the third level. This time the period is [4, 2, 4, 2, 4, 6, 2, 6], has length 8 and
     starts at position 4 in the first order differences.
   • Beyond p3 = 5, I verified the result on a computer up to p8 = 19. A finite number of steps is required for
     each pi , see the Python code in section A.
This concludes the proof. Thanks to theorem 2.2, keeping 2, 3 and 5 before the period kicks in does not change
the success status. Note how fast the depth function decays. □

Gilbreath’s conjecture states that theorem 2.3 is true no matter how long we go with prime sieving. By contrast



                                                         3
to Plouffe who shows success for the finite sequence consisting of the first 1014 primes [26], we proved success for
infinite sequences containing all primes but blended with a proportion ρk of all compound integers, where
                                                     κ 
                                                     Y           1    e−γ
                                              ρκ =         1−       ∼                                                (1)
                                                     i=1
                                                                 pi   log κ

according to Meterns’ third theorem. So far, theorem 2.3 is proved for κ ≤ 8, and ρ8 ≈ 17%. The next the-
orem, while stating nothing new, starts our descent into deep number theory. The short proof is worth reading.

Theorem 2.4 Starting with all integers > 1, let Sκ be the sequence obtained by iteratively removing all multiples
of pi except pi , for i = 1, . . . κ, where p1 , p2 and so on are the prime numbers starting with p1 = 2. Then Sκ is
∆-periodic with period length
                                                                            κ
                                                                            Y
                                  L(Sκ ) = ϕ p#
                                                
                                              κ   = ϕ(p1 · p 2 · · · pκ ) =   (pi − 1).                              (2)
                                                                                i=1

The period kicks in in the first order differences after the first κ elements. Furthermore, in the periodic cycle, the
depth at level 1 (maximum gap between successive values in Sκ ) satisfies

                                                γκ (1) = O κ2 log2 κ .
                                                                       
                                                                                                                   (3)

Here γκ (·) denotes the depth function attached to the sequence Sκ and γκ (1) stands for the first level.
Proof: This is an application of the sieve of Eratosthenes. The period length is known: ϕ(·) is the Eulter totient
function. The asymptotic result (3) is a consequence of Iwaniec’s bound established in 1978, and γk (1) is the
primorial Jacobsthal function with argument κ. The notation p#   κ represents primorial numbers. □

The sequence Sκ consists of the integers coprime to the primorial p# κ = p1 · · · pκ . This is a topic of active research
in Sieve theory, including about its first and second order differences, whose absolute values match the entries in
our triangle. Theorem 2.4 gives us the exact, finite number of terms we need to look at in Sk and its differences
of any order in absolute value, allowing us to ignore all the other terms. The period length L(Sκ ), as a function
of κ, is listed on OEIS as sequence A005867, see here. The primorial Jacobsthal function (largest gap in Sκ ) is
listed as sequence A048670, see here. Its first few values are
       2, 4, 6, 10, 14, 22, 26, 34, 40, 46, 58, 66, 74, 90, 100, 106, 118, 132, 152, 174, 190, 200, 216, 234,
       258, 264, 282, 300, 312, 330, 354, 378, 388, 414, 432, 450, 476, 492, 510, 538, 550, 574, 600, 616,
       642, 660, 686, 718, 742, 762, 798, 810, 834, 858, 876, 908, 926, 954
The sieve in theorem 2.4 can be performed in random order: the primes can be rearranged in any order, as long
as you cover all of them in the long run. I call it random prime sieving, and I use the notation S2′ , S3′ and so on
for the generated sequences produced this way. For instance, If p1 = 11, p2 = 47 and p3 = 3, then S3′ is based
on these three primes. Sieving the primes in random order should not be confused with sieving random integers
sequentially [9]. There is no research papers about the former; the latter has applications in cryptography. For
more about the patterns linked to sieving, see [18]. First order differences are discussed in [11], focusing on
large gaps between consecutive primes, and in [29] focusing on consecutive numbers coprime to primorials (our
main topic). The Cramér-Shanks conjecture [14] also quantifies how fast these gaps may grow. See also [27].
Finally, theorem 2.4 can be generalized to random prime sieving, as follows.

Theorem 2.5 Random prime sieving using any combination of κ distinct primes p1 , . . . , pk in any order, leads
to increasingly thinner successful ∆-periodic sequences S1′ , . . . , Sκ′ encompassing all primes, for any κ ≤ κ0 .
Here κ0 is a constant yet to be determined. The period length is
                                                                          κ
                                                                          Y
                                       L(Sκ′ ) = ϕ(p1 · p2 · · · pκ ) =       (pi − 1).                              (4)
                                                                          i=1

Again, ϕ(·) is the Euler totient function. The period applies to Sκ′ differences of any order, in absolute value.
Proof: Take κ0 = 0 and the theorem is proved! For κ0 = 1, the proof should be quite easy: the difficult step is
to prove that the sequence succeeds regardless of p1 (the first prime being sieved out).
Periodicity and length of the period is well known for all κ. Note that formulas (2) and (4) are identical except
that now, the product p1 · · · pκ is not a primorial in general. Proving success for all κ ≤ κ0 might not be easy
for larger values of κ0 . I conjecture success for any κ0 including κ0 = ∞. □

My conjecture stated in the proof of theorem 2.5 is stronger than Gilbreath. You don’t need success for all Sκ′


                                                             4
but only for at least one infinite subsequence and for at least one permutation of all primes (out of the infinitely
many possibilities) when applying the random prime sieve.

        p 3    5    7    11    13      17       19                p 19     17   13     11     7       5       3
        λ   2 3 15 16     22    37      41                        λ    1    17  21   34   31    31     41
        γ   4 6 10 14     22    26      34                        γ    2     6   8   10   12    18     34
        τ   4 9 50 30 1818 39,205 10,283                          τ    2   282 543 964 828 17,248 10,283
        ν   7 23 199 113 9439 217,127 60,043                      ν    3   625 1307 2559 2559 67,191 60,043

        Table 3: Stats for standard sieve (κ = 8)                     Table 4: Stats for reverse sieve (κ = 8)


Tables 3 and 4 illustrate respectively theorem 2.4 and 2.5. For the latter, I sieved in reverse order (called reverse
prime sieving), starting from the largest prime under consideration, p8 = 19, down to the smallest one p1 = 2.
All the generated sequences succeed. As you move from left to right in either table, each sequence (summarized
in the corresponding column) is a subsequence of the previous one. The rows are as follows:
    • λ is the smallest index k for which γ(k) = 2.
    • γ is a shortcut for γ(1), the maximum value in the first order differences.
    • τ is the index in the first order differences, for the first occurrence of the record γ(1). In short, this is the
      index of the first value in the sequence followed by a the maximum gap.
    • ν is the left value in the sequence, leading to the first occurrence of maximum gap γ(1) in the first order
      differences. Not to be confused with OEIS A002386.
Row γ in table 3 corresponds to entry A048670 in the OEIS encyclopedia (Jacobsthal function), when extended
to all primes. The other rows do not have an entry in OEIS. And row τ may not be a good candidate because
it depends on how you compute it. In my case, after sieving all multiples of a prime p, I add p back into the
sequence, creating an offset for τ , that increases with the number of sieved primes, as you move to the right in
table 3. Entries in table 4 are not good OEIS candidates, as they depend on which prime you start the reverse
sieving.


3     Full list of short sequences and sequence categorization
I now shift perspective, working with the sequence of primes and other sequences with similar patterns. In the
end, what could validate Gilbreath’s conjecture is not the random character of primes, but the opposite: the lack
of randomness on some key metrics. More specifically, the unusual rarity of long runs in first order differences.
Likewise, what would make an arbitrary sequence not to succeed despite meeting most requirements, is caused
by specific non-random patterns that are incompatible with the non-random patterns found in primes, such as
very long runs early on in first order differences followed by a steep cliff. This is the exact opposite of prime
number behavior. It makes primes unlikely to fail Gilthreat’s conjecture, or in case of failure, failure points are
incredibly rare and the first one must occur very late in the sequence, well beyond the first 1014 primes.

3.1    Testing an exhaustive infinite list of admissible short sequences
A sequence Sn = (q1 , . . . , qn ) of positive integers is admissible if q1 = 2, q2 = 3, all subsequent elements are odd,
and all differences in absolute value start with 1, except possibly the last one (the bottom of the triangle). The
seed σ is the second element in the row just above the bottom value. Obviously, a sequence succeeds if and only
if σ ∈ {0, 2}. Otherwise, σ is an even number > 2 and the sequence fails, unable to reach 1 at the bottom. Let
N (σ, n) be the number of admissible sequences Sn with seed σ. Finally, by definition, a valid sequence is one
that is admissible but also satisfies qk < qk+1 for all k. For finite sequences of any length n, we have:
Theorem 3.1 For any fixed n > 2, the number N (σ, n) of admissible sequences Sn with n elements and seed σ,
is high when σ = 0, highest when σ = 2, then sharply decreases as σ increases. The decrease is rather fast at
first, then loses momentum and eventually stops. That is, for each n, there is a value σ0 (n), such that N (σ, n) is
constant (not depending on n) if σ ≥ σ0 (n). In addition, for any fixed n,
 (1) The number N + (n) of successful admissible sequences Sn grows faster than n! by orders of magnitude,
     while the number N − (n) of failed ones is infinite.
 (2) The last element qn of any admissible sequence Sn , successful or not, satisfies σ +3 ≤ qn ≤ σ +2n −1. Both
     the lower and upper bounds are attained for all n, σ, and cannot be sharpened.



                                                           5
 (3) By construction, admissible sequences satisfy qk+1 ≥ qk while valid ones satisfy qk+1 ≥ qk + 2. For any n
     and σ, there are of course more admissible sequences than valid ones. The ratio ρ(σ, n) between these two
     numbers oscillates around 0.30 for small values of n.
Proof: For any fixed σ, the first order differences of any admissible sequence Sn stays within these two extremes
instances: (1, 0, 0, 0, . . . , 0, 0, σ) and (1, 2, 4, 8, . . . , 2n−2 , σ ′ ), where σ ′ = 2n−1 + σ − 2. Thus qn ≥ σ + 3 and the
bound cannot be increased. Similarly, the upper bound for qn is
                                                    n−2
                                                             !
                                                    X
                                       qn ≤ 2 +          2k + (2n−1 + σ − 2) = σ + 2n − 1.
                                                k=0

This upper bound is also always attained and cannot be lowered. Thus: σ + 3 ≤ qn ≤ σ + 2n − 1. Since q1 = 2,
q2 = 3 and q3 ≤ q4 ≤ · · · ≤ qn , the number N (σ, n) is always finite.
For a fixed n, at equilibrium, when N (σ, n) is constant regardless of σ > σ0 (n), the following happens. If you
remove the last (rightmost) element in each sequence in two different sets corresponding to two distinct σ, σ ′ >
σ0 (n), the resulting two sets of truncated sequences are perfectly identical in all respects. In short, the sequence
generator is stuck: it has no more leeway to create new sequences, other than changing the last element qn in
each, as a function of the seed. At that point, qn largely dominates q1 , q2 and so on. It means that the number
of sequences is now the same for each new σ > σ0 (n). Therefore, the number of failed sequences at any given
n, computed as the aggregate over σ = 4, 6, 8 and so on, is infinite. The number of successful ones, aggregated
over σ = 0, 2, is finite.
I now work on the remaining points in the theorem.
    • The fact that N (0, n) < N (1, n) is because σ = 1 has more leeway than σ = 0 to move up from the very
      bottom of the triangle. This early advantage back-propagates from bottom to top at each level n in the
      triangle.
                                                                                                            2
    • For a fixed σ, as n increases, the growth for N (σ, n) appears to be of the order An B n , where A, B are
      two constants barely depending on σ (if at all), with B ≈ 1.45. See table 5 with explanations.
    • For ρ(σ, n) values, see table 6 with explanations. It is not clear if this ratio stays around 0.30 as n gets
      larger, or if it decreases, possibly converging to 0 while being about the same across all σ, at each level n.
Of particular interest are the values σ0 (n). They tell you at what σ the equilibrium is reached, given n. I haven’t
had time to look at this yet. □

Table 5 shows the ratios N (σ, n)/N (σ, n − 1). The ratio of successive ratios (the multiplicative equivalent of first
order differences), within each column, is about 1.45 and shows little variations. This is where the number 1.45
comes from in the proof of theorem 3.1. Table 6 shows the proportion of valid sequences among admissible ones,
for various σ and n. That proportion seems to not depend on σ, and possibly not even on n.

               n   σ=0 σ=1 σ=2 σ=3 σ=4                                 n   σ=0 σ=1 σ=2 σ=3 σ=4
               5    3.50     3.33    2.50    2.50      2.50            5   0.428    0.300   0.400   0.400   0.400
               6    5.14     4.60    3.60    3.40      3.40            6   0.333    0.326   0.333   0.352   0.352
               7    7.06     6.93    5.33    5.06      4.82            7   0.342    0.291   0.343   0.314   0.329
               8   10.57     9.89    8.39    7.64      7.35            8   0.308    0.303   0.303   0.313   0.313
               9   15.06    14.74   12.60   11.94     11.33            9   0.301    0.298   0.299   0.298   0.303
              10   21.96    21.57   19.11   18.16     17.56           10   0.296    0.295   0.293   0.296   0.296
              11   31.81    31.70   28.29   27.72     26.80           11   0.296    0.288   0.294   0.285   0.296

           Table 5: Growth ratios N (σ, n)/N (σ, n − 1)             Table 6: Prop. ρ(σ, n) of valid sequences


3.2     Efficient sequence corridors
I now introduce the concept of sequence corridor. An efficient sequence corridor is a narrow, bounded set of
admissible sequences containing the one of particular interest, and where the density of failing sequences if low.
The corridor is said to be optimum if it contains no failing sequences. In our case, optimum means that for each
triangle in the corridor, all the rows start with 1, including the bottom one. Failure, for a specific sequence or
triangle, is when the value in the bottom row is an odd integer > 1. In our setting, all rows start with 1 except
possibly the bottom one, regardless of success status.
     I now build an optimum corridor that contains the sequence consisting of the first n primes and no other
integers, for n = 11. Because n if finite, this corridor contains only a finite number of sequences. It can easily be



                                                               6
extended to n = ∞. Proving optimality at n = ∞ would imply that Gilbreath’s conjecture is true. Sequences
in the corridor are called corridor sequences, and built as follows:
   • A corridor sequence Sn = (q1 , . . . , qn ) starts with q1 = 2 and q2 = 3. Then, followed by strictly increasing
     odd numbers. The rows in the corresponding triangle, except possibly the bottom one, must start with
     1. That way, the sequence is both admissible and valid.
   • The first m terms q1 , . . . , qm with m < n constitute the warm-up period. No extra conditions are imposed
     upon them. The parameter m is called the offset. The corridor is governed by a smooth function f called
     the corridor function, indicating the general trend of the sequence. Here, f (x) = x log x.
   • For all k > m, the values must satisfy

                                   α1 f (k) ≤ qk ≤ α2 f (k),     β1 qk−1 ≤ qk ≤ β2 qk−1                                (5)

     The positive coefficients α1 , α2 , β1 , β2 along with m are called the corridor parameters. Also, in our case,
     α1 = β1 = 1, so I focus on α2 and β2 only.
The parameters must be chosen so that most sequences in the corridor succeed, and that the target sequence
of particular interest (here, the prime number sequence) is also in the corridor. By contrast, table 8 features a
sequence outside the corridor for multiple reasons: not a valid one because not strictly increasing, also growing
too fast, and finally the success at the bottom of the triangle is preceded by 3 failures. Now I can state have the
following result.
Theorem 3.2 The corridor with offset m = 5, parameters α1 = 1.0, α2 = 1.3, β1 = 1.0, β2 = 1.5, and governed
by the function f (x) = x log(x), contains the prime number sequence. Also, for all sequences of length n = 11 in
the corridor, only one is failing; it is featured in table 7.
Proof: To show that the prime number sequence is in the corridor, replace qk , qk−1 by the successive primes
pk , pk−1 in (5) and check that the formula holds when k > m with the prescribed set of parameters. The right-
most inequality in (5) holds thanks to Nagura’s theorem (year 1952), that guarantees the existence of a prime
between p and 1.2 p for any prime p > 23. Sharper bounds have been found more recently, including Schoenfeld
(1976), Dusart [10] and Axler [2]. I also checked that the prime sequence satisfies the corridor requirements for
the first 105 primes. See the function test primes in the Python code.
To prove that the sequence in table 7 is the only exception with n = 11 in the efficient corridor, I generated
all admissible sequences of length n, with σ ∈ {4, 6, 8, 10}. There are about 107 of them. Besides the example
in table 7 which has σ = 4, I found no other exceptions in the corridor. Then, by digging into the proof of
theorem 3.1, I concluded that exceptions are not possible if σ > 10 (assuming n = 11), under the corridor
requirements.
Note that success corresponds to σ ∈ {0, 2}. By skipping these two values in my test as I was looking for failures
only, and stopping at σ = 10, it reduced compute time by a factor at least 10. □

Clearly, the main cause of failure is unexpected spikes in the sequence, especially early on. Long sub-sequences
with identical values is another major cause of failure, but they are ruled out as non valid. Large spikes are
eliminated thanks to the corridor requirements. For the prime numbers, spikes are called prime gaps and are
benign compared to other sequences in the corridor. The first occurrence of successive prime gap records are
listed in OEIS A002386. The primes concerned are shown in the first list below.
   2, 3, 7, 23, 89, 113, 523, 887, 1129, 1327, 9551, 15683, 19609, 31397, 155921, 360653, 370261, 492113,
   1349533, 1357201, 2010733, 4652353, 17051707, 20831323, 47326693, 122164747, 189695659, 191912783,
   387096133, 436273009, 1294268491, . . .
   1, 2, 4, 6, 8, 14, 18, 20, 22, 34, 36, 44, 52, 72, 86, 96, 112, 114, 118, 132, 148, 154, 180, 210, 220, 222, 234,
   248, 250, 282, 288, 292, 320, 336, 354, 382, 384, 394, 456, 464, 468, 474, 486, 490, 500, 514, 516, 532, 534,
   540, 582, 588, 602, 652,. . .
They are well spaced out, and the record values increase slowly, see OEIS A005250 with extract just above.
These two facts combined make the gaps too weak to cause anything but local disturbances quickly absorbed
in the triangle, in a reasonable number of levels well before we reach the bottom. Of cause, large gaps followed
by tiny prime differences (such as twin primes) take more time to dissipate, and are worth investigating. For
instance, between 20,831,323 and 20,831,533, there is a massive gap of 210 composite numbers. Yet, directly
following 20,831,533, the next prime is 20,831,537, creating an incredibly small gap of just 4. More on this topic
on the Prime Gap Project website, here. The Polymath Project proved that there are infinitely many prime gaps
smaller than 246.



                                                          7
     However, a real concern is the presence of very long runs (called plateaus) in the first order differences (the
prime gaps), followed by a steep cliff (a spike), followed by more plateaus and cliffs with the worst possible
distribution of elevations. Especially when happening early on. The only failing sequence with n = 11 in the
corridor (table 7) exhibits such a pattern. Yet, prime numbers are notorious for lacking such patterns due to
congruential demands. For instance, there is only one run of the form p, p + 2, p + 4 where all three numbers are
prime, because one of them must be a multiple of 3. The only possibility is 3, 5, 7 because 3 is the only prime
divisible by 3. The topic is related to primes in arithmetic progressions and discussed in [22, 25]. Prime runs
are listed in OEIS A067090. I summarize all these observations in the next statement.
Statement 3.1 If the prime number sequence fails (that is, if Gilbreath’s conjecture is not true), it would not
be caused by unusually large gaps in prime numbers, nor by the asymptotic distribution of primes, nor by the
extreme rarity of long runs in prime gaps (the maximum length of arithmetic progressions consisting of primes
only), nor by how early such runs occur.

3.3    Hidden patterns causing failures
I now discuss a very unusual sequence in the corridor: the only one that fails when n = 11. I haven’t tested
larger values of n due to computational complexity. Despite reassurances provided by statement 3.1, there is a
possibility that some unknown insanely rare pattern could manifest after a colossal number of terms in the
prime number sequence.
     The unfortunate, exotic, and extremely rare sequence in table 7 is of critical importance. It is the only
valid one of length n = 11 out of infinitely many, that fails while meeting the requirements to be in the efficient
corridor. One may argue that the first differences have a long run incompatible with primes, and a gap larger
than any in the first 11 primes. However the failure point happens at 29, not early on. Replacing 29 by either
27 or 31 leads to success, despite the long run and large gap still there. So, something else is causing the failure.
But what? Think about it before reading on.
     In his paper on Gilbreath’s conjecture [6], Chase uses a narrow corridor with slow growth. The growth—too
slow to encompass the prime number sequence—guarantees that large spikes take a very long time to show up,
increasing the proportion of succeeding sequences in his corridor. He then proves that his set of failing sequences
has zero density in his corridor. By contrast, my corridor grows at the speed of primes. Yet, large gaps are not
the issue. After all, the valid sequence 2, 3, 5, 9, 17, . . . with qk+1 = 2qk − 1 succeeds, but is not in my corridor.
As a side note, this example is the most extreme of all valid successful sequences, in terms of growth.
     To dig further into the problem, look at table 7. What creates the failure is not just the number 29, even
though prior to reaching it, the sequence was successful despite a major issue. The large gap of 8 between 17
and 25, combined with a run of identical tiny gaps right after, is an issue. You can fix it by replacing 29 either
with 27 or 31. But there is more to it. What compounds the problem is the segment 11, 13, 15, 17, resulting
in a long run of 2 (smallest possible gap) followed by the large gap of 8. The first issue causes 6 (a high value
this early) to trickle down a few levels, more than expected. The second issue allows 6 to propagate down much
further, not leaving enough levels to fully recover from it, thus crashing at the bottom.
     Actually, even the segment 3, 5 contributes to the demise, introducing a 0 near the bottom and next to 1.
This, combined with a 4 next to it, itself arising from the above issues, kills the deal. It is not possible to change
3, 5 to get rid of that problem, without introducing a new fatal issue, unless you also change some other values.
In the end, not only large values in the triangle are a liability, but also the 0’s. Especially when they pop up too
close to the left at a level too close to the bottom, with many consecutive 0’s followed by a large value, followed
by more 0’s, followed by another large but different value in-between 0 and the previous high, and so on.


          2       3       5       9       11 13 15 17 25 27 29                                     2       3       5       7       9       15 41 43 47 43 27
      8       1       2       4       2       2       2       2       8       2       2       26       1       2       2   26 2 4 4 16
                                                                                                                               2       6
      6           1       2       2       0       0       0       6       6       0           24           1       0       0       4
                                                                                                                        20 24 2 0 12
      6               1       0       2       0       0       6       0       6               22               1 0 4 16 4 22 2 12
      6                   1       2       2       0       6       6       6                   20                1 4 12 12 18 20 10
      6                       1       0       2       6       0       0                       10                  3 8 0 6 2 10
      6                           1       2       4       6       0                           8                    5 8 6 4 8
      6                               1       2       2       6                               4                      3 2 2 4
      4                                   1       0       4                                   2                       1 0 2
      4                                       1       4                                       2                        1 2
      3                                           3                                           1                          1

              Table 7: Unusually rare instance of                                             Table 8: 4 successes, then 3 failures then 3
              failure within the efficient corridor                                            successes (sequence outside the corridor)


                                                                                          8
     large integer. Each digit is the equivalent of a row in the triangle. Usually, the impact is local. But in rare
instances, it propagates back to the first digit, changing its value. In the same way that adding 29 to the right
to the sequence 2, 3, 5, 9, 11, 13, 15, 17, 25, 27 changes the bottom value in the triangle from 1 to 3, while
adding 27 or 31 preserves the 1. I conclude with the following statement.
Statement 3.2 Removing from the corridor all the sequences with the type of plateau and cliff combinations just
described, would reduce the already low density of failing sequences by an additional order of magnitude. If these
A good analogy is when adding a small integer to a large number. The carryover operations modify the digits
in the combinations are the only non-trivial issue, then all sequences in the upgraded corridor would succeed,
including the prime numbers which would still meet the additional requirement to stay in the new corridor.

                                   Successful Sequences              Failed Sequences
                         n   Admissible     Valid    Corridor Admissible Valid Corridor
                         6       82         27              4       ∞         ∞         0
                         7      573        180              7       ∞         ∞         0
                         8     5,839      1,786            18       ∞         ∞         0
                         9    86,921     26,094            46       ∞         ∞         1
                         10 1,890,317   559,127           121       ∞         ∞         0
                         11 60,013,894 17,535,396         345       ∞         ∞         1

                             Table 9: Sequence count depending on type and length n

Table 9 shows how rare failing sequences are in the corridor, at least up to length n = 11. Empirical evidence
suggests that failure rate decreases when n increases, as the failure point usually occurs early in failing sequences
in the corridor. In short, while the number of failing sequences may increase with n, even exponentially fast, the
number of successful ones increases at a much faster pace, by orders of magnitude. I summarize this intuition
in the following conjecture.
Conjecture 3.1 Let g(n) and h(n) be the number of sequences of length n respectively succeeding and failing in
our corridor. Then both g(n) and h(n) grow indefinitely, with h(n)/g(n) → 0.
The above claim depends heavily on the corridor and its threshold parameters. A different corridor configuration
or parameter set may lead to very different conclusions. In some cases, h(n) and even g(n) may stay finite at
all times. I found a similar behavior in a different corridor with growth n3/2 instead of n log n, but again the
choice of corridor parameters had a big impact. Of course, the lower the proportion of failures, the better. With
one caveat: if failures are extremely rare, it may be difficult to figure out what could cause them, besides trivial
patterns.


4     Synthetic sequences with Poisson gaps to mimic prime numbers
I discuss the most interesting insights first, before detailing my expanded search for failures and the implications
for the prime number sequence. From the mathematician’s vantage point, it looks like a war is taking place in
the corridor, with prime numbers using every possible trick to win it. Not with deep theoretical machinery, but
rather, simple, deterministic patterns that make the primes eminently non random. In particular:
    • Besides the obvious, the feature most likely to kill a sequence is the pattern 2 4 2 4 2 4 and so on, preceded
      or followed by a moderately large value, in the first order differences. Or buried deeper in lower levels in
      the triangle. It is almost a requirement.
    • In prime numbers, the first order differences are known as prime gaps, controlled by congruential rules.
      Infinitely many patterns are banned or can happen only once at the very beginning. The best example is
      arguably 2 4 2 4 2 4 and so on. So the prime number sequence will never face the issue just described.
    • If the pattern 2 4 2 4 2 and so on appears at a lower level in the triangle, surrounded by a big enough
      number on either side to guarantee failure at the bottom level, the end result upstream (at the sequence
      level) is a much bigger number or too fast of a growth that kicks the sequence outside the corridor. Thus,
      it cannot be found either at lower levels in prime numbers, whose sequence is inside the corridor.
What determines failure or not is the length of the pattern in question, how close to the left it starts, at which
level, and how big the two surrounding numbers are (left and right). Of course, the sequence may still succeed
if the values to the left are such that they can dilute the generated impulse fast enough before it propagates to
the bottom. A good example is the sequence consisting of the primes 2, 3, . . . , 47 followed by 49, 53, 55, 65. It


                                                           9
fails not because the gap between 55 and 65 is too large. Replace (55, 65) by (53, 67) and it succeeds despite
increasing that gap and creating a duplicate of 53. Yet the gap 55–65, while modest, is large enough that when
combined with the preceding numbers in the original sequence, it leads to failure. The suggested replacement
breaks a combination of bad cycles. Barely, but just enough to move from failure to success. The good looking
sequence fails, its ugly sister succeeds. See table 10.

             2       3       5       7       11       13       17       19       23       29       31       37       41       43       47       49       53       55        65
        10       1       2       2       4        2        4        2        4        6        2        6        4        2        4        2        4        2        10
        8            1       0       2       2        2        2        2        2        4        4        2        2        2        2        2        2        8
        6                1       2       0        0        0        0        0        2        0        2        0        0        0        0        0        6
        6                    1       2       0        0        0        0        2        2        2        2        0        0        0        0        6
        6                        1       2        0        0        0        2        0        0        0        2        0        0        0        6
        6                            1       2        0        0        2        2        0        0        2        2        0        0        6
        6                                1        2        0        2        0        2        0        2        0        2        0        6
        6                                    1        2        2        2        2        2        2        2        2        2        4
        4                                         1        0        0        0        0        0        0        0        0        4
        4                                             1        0        0        0        0        0        0        0        4
        4                                                  1        0        0        0        0        0        0        4
        4                                                      1        0        0        0        0        0        4
        4                                                           1        0        0        0        0        4
        4                                                               1        0        0        0        4
        4                                                                    1        0        0        4
        4                                                                        1        0        4
        4                                                                             1        4
        3                                                                                  3

                 Table 10: Rare failing sequence; replace 53, 55, 65 by 53, 53, 67 to make it succeed!


To summarize, the new failure causes discovered are: (1) the flip side of a basin with one-time spike at the border,
that is, a high elevation plateau surrounded by a one-time abyss on either side, (2) the pattern 2 4 2 4 2 4 with
a rather large value on either end, and variants not found in prime gaps, and (3) the same at a lower level. The
last case results in larger values at the top level, kicking the sequence out of the corridor. If this can be precisely
quantified and proved, it would solve Gilbreath’s conjecture. The work needed does not seem insurmountable.
Prime numbers are actually a very good candidate for success due to congruential constraints on prime gaps,
unlike more random sequences. But the first step is to check whether or not I covered all failure types.
     The concepts of cliff, plateau and abyss also apply to sequences growing faster than the primes, with similar
conclusions. For instance, the sequence 2, 3, 5, 9, 15, 23, 33, 45, . . . with q1 = 2 and qn = n2 − 3n + 5 for n > 1
obviously succeeds no matter how long it is. After q8 = 45, one expect q9 = 59. Without even computing the
triangle, you can tell that adding q9 ∈ {59, 61} succeeds while q9 ≥ 63 fails. It gives you the minimum height
for the killing cliff. With little efforts, you find that adding q9 ∈ {57, 55, 53} succeeds while adding q9 ≤ 51 fails.
And this determines the minimum depth of the deadly abyss. In this sequence, the values between q2 = 3 and
q8 = 45 play the role of the plateau, by constituting a very smooth albeit fast growing segment, with 2nd order
differences all zero as the degree of the polynomial is 2. Again, we are talking about a very narrow cliff of abyss,
just one outlier value. Otherwise, future values at the sequence level could restore success, as explained earlier.

4.1    High performance computing to discover rare failure patterns
So far, researchers focused on large prime gaps as the main danger, using the best bounds available to shrink the
corridor by imposing conditions stricter than (5). This is the wrong approach: the non trivial causes for failures
are different, not visible to the naked eye, and hard to find in simulations within a narrow corridor. Actually,
more chaotic sequences with bigger gaps have a high success rate, see figure 8 also based on Poisson increments.
     My first attempt to build long sequences to discover new patterns of failure in the corridor, produced mixed
results. The first failure always happened very early on in the simulations, and always due to a moderately
large gap preceded by a small one – which also happens in succeeding sequences including the primes. I did not
discover other patterns because I run too few simulations: I generated 106 random sequences in the corridor.
Other patterns exist, see section 5.1. You might need more than 1050 simulations to find one, or use a different
approach. The following simulation problem is a good analogy: you generate bit streams of length n. Success
is defined as a stream with above 10% of ‘1’. Failures are easy to find for small n, but with n = 100, the chance
of failure for a random bit stream is 1.107 × 10−17 . For n = 1000, it goes down to 7.428 × 10−163 . Yet, the
number of failures over all bit streams increases with n and becomes infinite, while the proportion of failing
streams tends to zero very fast.


                                                                                      10
     In my 106 sequences, each with 1000 terms, 2883 failed. The sequences were all distinct, but there is little
leeway for the first 20 terms or so, especially since all sequences start with 2, 3, 5, 7, 11, . . . , 31, 37, 41, 43. As
a result, I found many duplicates among the short paths that lead to first failure. After duplicates removal, the
number 2883 is reduced down to 81 distinct failure cases. They are listed in table 11 where the columns are as
follows:
   • n is the index of the term where first failure occurs. Since the first 14 term are the same in each sequence,
     for instance n = 17 means that failure occurred just after adding 3 new terms.
   • σ has the same meaning as earlier; σ − 1 is the value at the bottom of the triangle. It is the first one ̸= 1
     in the left diagonal. In case of success, σ ∈ {0, 2}. Otherwise σ is an even integer ≥ 4.
   • γ is the maximum value in the first order differences when stopping at the first failure point.
   • δn = qn − qn−1 where qn is the value at first failure point in the sequence. With few exceptions, the large
     |δn − δn−1 | is causing the failure. Usually, the maximum γ occurs at the right end, that is, γ = δn .
   • The “forbidden” column is the most striking feature, see section 4.2. Note the entry 2, 4, 2, 4, 2 mentioned
     previously and linked to potential early failure.
Statement 4.1 The vast majority of failing corridor sequences contain a forbidden prime constellation pattern
early on. Primes do not have such patterns. It also explains why the prime number sequence does not fail early
on, where the chance of failure is highest.
Statement 4.1 is based on table 11. I now describe my simulations. All the failures occurring late in a sequence
were preceded by a failure early on within the same sequence, thus defeating the purpose. But they did reveal
many banned patterns in the first order differences: the forbidden constellations. The algorithm starts with the
sequence consisting of the first 14 primes. At iteration n, the new added term is qn+1 = qn + 2 + 2un+1 , where
the un are i.i.d deviates from a Poisson(λ) distribution. If the augmented sequence with qn+1 is no longer in
the corridor, I repeat this step until I find a new un+1 candidate that keeps us in the corridor.
     Thus, I use rejection sampling to mimic the gaps qn+1 − qn . For a better fit, use the prime gap empirical
distribution, a generalized Poisson [8], or an adjusted Poisson that depends on n, with the Hardy-Littlewood
k-tuples correction. Tao and others [7] use a geometric distribution. More on this topic in [4, 20, 21]. These
models assume independence between successive gaps. This assumption is wrong due to the forbidden patterns.
The small λ = 2.5 produces few rejections in rejection sampling (speeding up the algorithm) and generates the
largest number of distinct sequence failures, yet < 0.01% out of 106 generated sequences with n = 1000 terms.
Almost all failures were caused by a too large gap early on, after the first 14 terms.
    As of today, the best asymptotic bound for the maximum gap between two primes, proved unconditionally
(without assuming that the Riemann Hypothesis is true), is

                                           pn+1 − pn ≲ O p525
                                                              
                                                           n    ,                                     (6)

established in 2001 by Baker [3], see also [1]. In our context, a weaker bound suffices. According to conjecture 5.1,
we only need pn+1 − pn ≲ n. Not meeting this bound would guarantee failure of the prime number sequence.         Of
course, the sharper bound you use, the easier to prove Gilbreath’s conjecture. Assuming RH, O p0.525    n     can be
               √
reduced to O pn log pn , a small improvement. Cramér conjectured in 1936 that it can be lowered to O(log2 pn )
                         

but his heuristic has been questioned. In 2025, Wang [28] claimed to have proved Cramér’s conjecture. As you
may know, pn ∼ n log n, thus the average prime gap is asymptotically log n.

4.2    Prime gaps and forbidden prime constellations
The “forbidden” column in table 11 lists the first instance of a forbidden prime constellation found beyond the
first 14 elements in all but one of the 81 failed sequences from the previous experiment (see section 4.1). But
what is exactly?
     Take the quintuplet 2, 4, 2, 4, 2 in the first order differences. If present in the primes, it means that there
is at least one prime p for which p, p + 2, p + 6, p + 8, p + 12, p + 14 are all primes. But no matter p, at least one
of these 6 numbers is always a multiple of 5. So this quintuplet can not be found in prime gaps, except possibly
just once, at the beginning. Actually 5, 7, 11, 13, 17, 19 works, but this is the only exception. Thus, it is called a
forbidden pattern. This quintuplet is found in failed sequences, but not in successful ones, in my small sample.
     Likewise, the forbidden patterns 4, 4 and 8, 8 happens frequently in successful sequences, but not in the
failed ones (again, small sample that only indicates a probability of occurrence). Of course all banned patterns
occur in successful sequences, but their distribution is much different from that in failed ones, especially for
longer patterns. To find them in a given sequence, I looked at successive pairs in the first order differences after
the first 14 terms and tested each pair for admissibility in primes (that is, satisfying or not the congruential


                                                           11
constraints). I then did the same with triplets, quadruplets, and so on. If a pair is banned, all triplets containing
it are also banned. In particular the most fundamental pair 2, 2 is banned. Thus, so is 4, 2, 2 or 4, 2, 2, 6, 2
and so on. Same with triplets, quadruplets and all tuples. It makes the prime numbers anything but random.
At the same time, it gives them some protection against failure: a long chain of 2 is dangerous if followed or
worse, preceded by a spike. Primes are protected against that and other dangerous patterns such as 2, 4, 2, 4,
2 (all banned).
     I did not find any reference about forbidden patterns, but there is a lot of ongoing research about admissible
ones, sometimes called permissible prime constellations. It started with the prime k-tuple conjecture and the
Hardy–Littlewood asymptotic constants. See the Wolfram entry on the topic, here, and Richard Mathar’s table
of prime gap constellations, here. For more more recent references on the topic, see [13, 23].


    n   σ   γ   δn−1 δn     Forbidden       n    σ   γ    δn−1 δn Forbidden      n    σ   γ    δn−1 δn   Forbidden
    16 4 12      2    12        –           18   4   14    2    14     2, 2      22   4   12    2   12    2, 6, 2
    18 4 10      2    10     4, 6, 4        20   6   14    2    14     2, 8      22   4   12    2   12      2, 2
    16 4 14      2    14       2, 2         22   6   14    2    14     2, 8      22   4   12    2   12     4, 10
    22 4 12      2    12       2, 8         20   4   12    2    12     2, 8      22   4   12    2   12   4, 6, 10
    18 6 12      2    12     4, 6, 4        22   4   12    2    12   8, 6, 2     18   6   16    2   16      2, 2
    17 4 14      4    14 6, 4, 2, 4, 2, 4   22   4   12    2    12    4, 10      22   6   14    2   14      2, 8
    18 4 10      2    10 2, 4, 2, 4, 2      22   4   12    2    12     2, 8      22   4   12    2   12    4, 6, 4
    18 6 12      2    12 2, 4, 2, 4, 2      22   4   12    2    12    4, 10      32   4   12    2   12     10, 4
    20 4 12      6     4       2, 2         20   8   16    2    16     2, 8      22   6   14    2   14 2, 4, 6, 6, 6
    18 4 14      2    14       2, 2         26   4   10    2    10     2, 8      24   4   12    6    8      2, 8
    18 8 14      2    14 2, 4, 2, 4, 2      22   6   16    2    16     2, 2      20   4   12    2   12      2, 2
    26 6 12      2    12       2, 8         22   4   12    2    12 4, 2, 6, 6    22   4   12    2   12     4, 10
    18 4 14      2    14     2, 6, 2        22   6   14    2    14     2, 8      20   4    8    2    8      2, 8
    22 6 14      2    14       2, 2         22   4   12    6     4    4, 10      22   4   16    2   16      2, 2
    18 10 16     2    16 2, 4, 2, 4, 2      22   4   12    2    12     2, 8      22   4   12    2   12      2, 2
    25 4 14      4    14       2, 8         22   4   12    2    12     2, 8      24   4   12    2   12      2, 8
    22 6 14      2    14       2, 8         22   4   12    2    12 4, 2, 6, 6    24   4   12    6    4      2, 8
    20 4 16      2    16       2, 2         22   4   12    2    12     2, 8      22   4   18    2   18      2, 2
    20 4 12      2    12       2, 8         22   4   12    2    12     2, 8      24   4   12    6    4     4, 10
    26 6 14      2    14       2, 2         22   6   14    2    14 4, 2, 6, 6    24   4   12    6    4      2, 2
    22 4 12      2    12       2, 8         24   4   12    2    12     2, 8      20   4   20    2   20      4, 4
    22 4 12      2    12      4, 10         22   4   12    2    12     2, 2      22   6   14    2   14 4, 2, 6, 6
    25 4 14      4     6       2, 8         25   4   14    4     6   8, 6, 2     22   4   12    2   12      8, 2
    20 4 12      2    12       2, 2         28   4   16    6     4 16, 2, 4, 2   20   4   16    2   16      2, 8
    20 4 12      2    12      4, 10         24   4   12    6     8   4, 6, 4     24   4   12    6    8     4, 10
    22 4 14      2     8       2, 8         21   4   16    4     6     2, 2      22   6   16    2    2      2, 8
    20 4 16      2    16       2, 8         24   4   12    2    12   4, 6, 4     21   4   18    4   18      2, 8

 Table 11: List of failing corridor sequences, out of 106 sampled ones; all but one contain a forbidden pattern


5       A deeper version of Gilbreath’s conjecture with partial proof
In this section, I iteratively compute the bottom element in the triangle attached to a sequence q1 , . . . , qn by
working on the right diagonal only, updating it incrementally as n increases. The sequence succeeds if and only
if the last element in the diagonal is equal to 1. I also compute the maximum interval In = [qn− , qn+ ] such that
the augmented sequence q1 , . . . , qn , qn+1 continues to succeed if and only if qn+1 ∈ In . Along the way, I build
a theoretical framework to solve the conjecture, leading to a partial proof and deeper claims. The approach is
innovative. For instance, in section 5.3, I reduce valid sequences to a canonical form: starting at some level in
the triangle and going downwards, the original and reduced sequences have the exact same rows. They differ
only in the upper levels. It allows you to focus on a simpler, equivalent sequence, to check success status.

5.1     Distance between a successful sequence and its closest failing sister
The simulations in section 4.1 did not produce sequences that fail for the first time only after a large number of
terms. This was my intended purpose. Despite generating 106 sequences, only 81 failed, and all failed early on.
While it started an interesting discussion about banned prime gap constellations in section 4.2 with more on
this topic here, I have yet to find first failure points occurring much later in a corridor sequence. In this section,


                                                           12
this goal is I achieved, while setting the foundations with detailed steps, some completed, to prove Gilbreath’s
conjecture for the prime number sequence in particular. I chose the primes not because the original conjecture
focuses on them only, but because they are an ideal candidate, and in some ways easier to handle compared to
other types of chaotic sequences.




     Figure 1: Prime sequence: qn+ , qn , qn− resp. in orange, white, green (left). Ratio (center) and delta (right).




    Figure 2: Random sequence: qn+ , qn , qn− resp. in orange, white, green (left). Ratio (center) and delta (right).




      Figure 3: Log sequence: qn+ , qn , qn− resp. in orange, white, green (left). Ratios (center) and deltas (right).

The left plot in figures 1–2 shows the increasing width of the success interval In = [qn− , qn+ ] as n increases,
with n on the X-axis. The sequence q1 , q2 and so on, colored in white, has qn ∈ In−1 . The orange and green
curves are (resp.) the admissible lower and upper bounds for qn . The meaning is as follows: if the sequence
is successful up to qn , then it will be successful at qn+1 if and only if qn+1 ∈ In . The middle plot shows the
        +                         −                                                       +
ratios qn−1 /qn in orange, and qn−1   /qn in green; the right plot shows the differences qn−1 − qn in orange, and
  −
qn−1 − qn in green. Here, negative gaps are allowed. I tested 4 sequences:
   • Figure 1: The prime number sequence.
   • Figure 2: Random sequence with Poisson increments of mean λ = 2.5 (multiplied by 2 to make them even
     like prime gaps) and rejection sampling to stay in the logarithmic corridor. See section 4.


                                                            13
   • Figure 3: Log model. Here qn = ⌊log qn−1+
                                               ⌋ rounded to the smallest odd integer > qn−1 . The brackets ⌊·⌋
     stand for the integer (floor) function.
   • Figure 4: Power model. Here qn = ⌊(qn−1
                                         +
                                             )0.35 ⌋ rounded to the smallest odd integer > qn−1 .
The first two (prime numbers and the random sequence with similar growth) have the largest delta between the
lower and upper bounds. It means that at any given qn , there is a lot of leeway to choose the next qn+1 so
that the augmented sequence continue to succeed iteratively, and thus indefinitely. Also, qn stays in the middle
between the two bounds, never getting close to either one. It is impossible that these sequences could ever fail,
if this behavior persists indefinitely. By contrast, the last two ones (the log and power sequences) progress in
a narrow band, getting close to failing at regular intervals. Unless proved otherwise, success for all qn is not
guaranteed. Some sequences could hit a wall with no possible escape from failure. Or for the prime number
sequence, for some unknown insanely large n, qn could jump above the upper bound, maybe even just one single
time in its entire history, returning within the band at n + 1 and staying in it thereafter, forever.




      Figure 4: Power sequence: qn+ , qn , qn− resp. in orange, white, green (left). Ratio (center) and delta (right).


By design, the random and the prime number sequences share a lot in common. However, there are major
differences. The primes exhibit regular spikes in the upper and lower bounds. Also, for the primes, on occasions,
the right diagonal consists only of 0 and 2, besides the first and last elements. These primes, always the largest
in a pair of twin primes, are called magic primes: see theorem 5.1. In the random sequence, this happens much
less frequently regardless of λ, and the pattern seems to stop at some point. One may argue that my simulations
do not mimic the primes very well. The reality is the opposite: the primes lack randomness. It shows on multiple
occasions including here, making them more risky than most people think in cryptographic applications.

5.2    General framework, proof for magic primes and other cases
So far, I discussed several situations that could lead to failure. For the prime numbers, the record gaps are not
the main issue; they are not large enough to be a concern. A combination of a moderately large gap surrounded
by several tiny ones and/or some halfway between, especially if this pattern repeats itself in close succession,
creating plateaus, basins, dips and spikes in the first or higher order differences, causes problems not immediately
but later on in the right diagonal. I know formalize these findings, leading to theorem 5.5 and conjecture 5.1.

                             n      qn    1    2    3    4    5    6   7   8   9   10 11 12
                            205    1277   18   8    6    2    0    0   2   0   2    0    0   2
                            206    1279   2    16   8    2    0    0   0   2   2    0    0   0
                            207    1283   4    2    14   6    4    4   4   4   2    0    0   0
                            208    1289   6    2    0    14   8    4   0   4   0    2    2   2
                            209    1291   2    4    2    2    12 4     0   0   4    4    2   0
                            210    1297   6    4    0    2    0    12 8    8   8    4    0   2
                            211    1301   4    2    2    2    0    0   12 4    4    4    0   0
                            212    1303   2    2    0    2    0    0   0   12 8     4    0   0
                            213    1309   6    4    2    2    0    0   0   0   12 4      0   0
                            214    1319   10   4    0    2    0    0   0   0   0    12 8     8
                            215    1327   8    2    2    2    0    0   0   0   0    0   12 4

                                 Table 12: δk (qn ), with 1 ≤ k ≤ 12 and 205 ≤ n ≤ 215


                                                              14
Theorem 5.1 In the prime number sequence, there are twin primes (p − 2, p) called magic twins, presumably
infinitely many of them, for which the right diagonal δ(p) consists only of 0 and 2 except for the first and last
elements. If the sequence succeeds up to p − 2, adding p guarantees success at p.
Proof: The fact that the sequence succeeds at p if it succeeds at p − 2 is trivial. Let δ−1 (p), δ−2 (p) denote the
last 2 elements in the right diagonal δ(p). Success means δ−1 (p) = 1. However if we succeed at p − 2, we must
have δ−1 (p − 2) = 1. Since δ−2 (p) ∈ {0, 2} and δ−1 (p) = |δ−2 (p) − δ−1 (p − 2)|, we must have δ−1 (p) = 1. □

Theorem 5.1 features the easiest case where adding the next prime guarantees success in the augmented sequence
if it was successful up to the previous one. And the regular resets to a right diagonal consisting only of 0 and 2
contributes to making the full, infinite prime sequence successful. The list of magic twin pairs (p − 2, p) is not
in the OEIS encyclopedia. Below are the first few p, that I also call magic primes:
      13, 19, 43, 73, 103, 109, 283, 463, 619, 2689, 2713, 2803, 3469, 5659, 13693, 14563, 24109, 28663,
      36013, 36793, 42409, 42703, 56533, 65719, 74203, 80683, 92383, 97003
Theorem 5.1 leads to a generalization. First, let me define the 0-2 cycle in a right diagonal in any valid, finite
sequence. It is the longest section at the bottom, on the right in the corresponding triangle, just above the last
element (itself necessarily an odd integer), and consisting of 0 or 2 only. It may or may not exist. The length
of the 0-2 cycle and when it starts are what matter the most; it ranges from 1 element (a single 0 or 2) to the
whole diagonal as in theorem 5.1. If and only if not present, the sequence fails. The 0-2 cycle may contain only
0, only 2, or any combination of both.

Theorem 5.2 For a finite valid sequence to continue to succeed after adding a term q, the right diagonal δ(q) in
the triangle attached to the augmented sequence, must have a 0-2 cycle. You use this fact to recursively augment a
sequence ad infinitum while keeping success at all times.
Proof: It uses the same argument as in the proof of theorem 5.1. □

I now discuss related concepts. In any sequence q1 , . . . qn , the right diagonal δ(qn ) has n elements by construction.
Let ρn (k) be the proportion of k, for k = 0, 2, 4 and so on. The sequence is said to have a balanced right diagonal
if the following is satisfied:
                                                                           p
                                                 1               1         2n log log n
                                  max ρn (0) − , ρn (2) −               ≤                 .                           (7)
                                                  2               2              n
                                                                            √
If n > 928, the diagonal δ(qn ) is conjectured to contain fewer than n log n elements greater than 2. Thus, as
n increases, ρn (k) tends to 21 if k ∈ {0, 2}, and to 0 otherwise. Formula (7) is a direct application of the law of
the iterated logarithm. The bound in (7) is the strongest possible asymptotically under perfect randomness. At
a magic prime where 0 and 2 alternate (thus non random), 2n log log n can be lowered by orders of magnitude.
In my conjecture 5.1, part 4 claims that (7) is always satisfied for the prime number sequence if n > 770. But
a weak version, say with 2n log log n replaced by n3/2 , is enough for our needs. When only the weak version is
satisfied, the right diagonal is said to be weakly balanced. If δ(qn ) is balanced, you need additional conditions on
δ(qn ) to guarantee that it remains true for δ(qn+1 ). These conditions are distinct from randomness; they pertain
to the lengths of the successive runs of 0 and 2 in the 0-2 cycle of the right diagonal δ(qn ).
Now I can state and prove the main theorem 5.5, starting with lemmas 5.3 and 5.4.

Lemma 5.3 Let q1 , . . . , qn be a valid sequence (qk ≥ qk−1 +2) with right diagonal δ(qn ) = [ δ0 (qn ), . . . , δn−1 (qn ) ].
Thus, δk (qn ) = |δk−1 (qn ) − δk−1 (qn−1 )| with δ0 (qn ) = qn . Let gk = qk − qk−1 be the first order differences. Then
for k ≥ 2, we have:
                                         δk (qn ) ≤ sup (gn−j+1 − 2),                                                      (8)
                                                    1≤j≤k
                                                       h                        i
                                         δk (qn ) ≤ max δ1 (qn ), sup δj (qn−1 ) .                                         (9)
                                                                   1≤j<k

The maximum in (8) cannot be lowered without restrictions on the sequence. Thus, δ(qn ) may have reversals; its
second largest value after qn = δ0 (qn ) is not always gn = δ1 (qn ). However all values besides qn are bounded by
the maximum gap in g2 , . . . , gn . For prime numbers (qn = pn ), the max gap in question is < p0.525
                                                                                                   n   .
Proof: By recursion. For instance, δ3 (qn ) = |δ2 (qn ) − δ2 (qn−1 )|. Assuming δ2 (qn ) ∈ [0, max(gn , gn−1 ) − 2] and
δ2 (qn−1 ) ∈ [0, max(gn−1 , gn−2 ) − 2], we have
                                             h                                          i
                              δ3 (qn ) ≤ max max(gn , gn−1 ) − 2, max(gn−1 , gn−2 ) − 2
                                                             
                                       = max gn , gn−1 , gn−2 − 2.


                                                              15
Thus the result is also true for δ3 (qn ). The inequality comes from this: if x ∈ [a, b], y ∈ [c, d] and z = |x − y|,
then z ≤ max(|c − b|, |d − a|). Also, δ1 (qn ) = gn ∈ [2, gn ]. That’s where the 2 comes from. This proves (8).
The proof for (9) is based on a simple generalization of the following argument: Using twice the recursive formula
that defines δk (n), we have δk (n) = |||δk−3 (qn ) − δk−3 (qn−1 )| − δk−2 (qn−1 )| − δk−1 (qn−1 )|. Since for any a, b, c, d,
                                                                                                                            
|||a − b| − c| − d| ≤ max(a, b, c, d), we conclude that δk (n) ≤ max δk−3 (qn ); δk−3 (qn−1 ), δk−2 (qn−1 ), δk−1 (qn−1 ) .
Iteratively apply the same recursion to the leftmost argument in the maximum to complete the proof.
The last part, stating that δk (qn ) < p0.525
                                        n     for the prime number sequence, comes from a famous theorem proved
in 2001 by Baker [3]. □
In practice, for any fixed
                         √ n, the values δk (qn ) decay very fast as k increases, with ups and downs, and enter the
0-2 cycle in fewer than n log n steps. Proving this is the main challenge. According to (9), they can potentially
bounce back several times and stay elevated for very long. Table 12 shows how this could happen. Each row
features a right diagonal δn (qn ) in the prime number sequence. The third column represents the prime gap
gn = δ1 (qn ). Rows with n ≤ 212 list the real gaps. Beyond n = 212, I replaced prime gaps by other values (in
yellow) chosen to keep pushing the large rectangled elements to the right, towards the end of δ(qn ). The main
findings are as follows:
   • There is a large gap at n = 205. Not a problem, δ(q205 ) looks good. It is followed by a tiny gap at n = 206.
     Again not a problem yet. Between n = 205 and n = 209, the bold values 18, 16, 14, 14, 12 keep decreasing
     on average. So far, so good.
   • Between n = 210 and n = 215, there is no decrease. The impact of the large gap followed by a small one
     at n = 205, 206 (resp.) is now fully felt. The length of the long tail of δ(qn ), starting after the bold value,
     still remains the same as n increases. But now that tail always starts with the large value 12, increasing
     the risk that at some future n, the sequence could fail if the streak continues.
   • In reality, at n = 213, the true value of δ1 (qn ) is 4, not 6, breaking the streak. I changed it to 6 to check
     how long the bad streak could last in a random sequence. Instead of 6, I could have picked up 2 with same
     result. But it would have created 4, 2, 2 in successive gaps, which is a forbidden prime gap constellation,
     see section 4.2. Following 6, I had four options for δ1 (q214 ): 2, 6, 10, 14. Only 10 was not forbidden, so I
     chose 10. I had more acceptable options for δ1 (q215 ). Forbidden patterns severely limit the progression of
     a streak, but not completely. What will kill the streak is that soon enough, your only options for the next
     prime will be composite numbers due to the rarity of primes. For instance, in the table, q213 = 1309 is not
     a prime.
   • The scenario described here may be more complex and involve multiple parallel streaks in table 12, each
     caused upstream by a large gap followed by a small one. Also, the 12 could move to the right at a faster
     pace, and even increase, further reducing the chance of success. Changing δ1 (q213 ) from 6 to 38 does both.
     But it kills the 12 streak, starting a new one with even larger values, concerning because δ1 (q212 ) = 2 is a
     tiny gap. Incidentally, the real gap at n = 217 is δ1 (q217 ) = 34, a record. And all the fear just described is
     vastly exaggerated. But for a formal proof, no scenario can be a priori ruled out, even if insanely unlikely.

Lemma 5.4 Let q1 , . . . , qn−1 be a valid, successful sequence and ν2 (qn−1 ) be the number of elements equal to 2 in
the 0-2 cycle of its right diagonal δ(qn−1 ). Then q1 , . . . , qn also succeeds if gn∗ ≤ 2ν2 (qn−1 ) + 2, where

                                              gn∗ = max g2 , g3 , . . . , gn .
                                                                            
                                                                                                                  (10)

As usual, gk = δ1 (qk ) = qk − qk−1 is the gap between qk and qk−1 . This lemma is not specific to prime numbers.
Proof: I pictured the two right diagonal δ(qn−1 ) and δ(qn ) in table 13. Blocks of the same color have the same
number of elements. The gray block in the top row is δ(qn−1 )’s 0-2 cycle. It starts at index k = τn and it is
followed by a single value in green, always an odd integer but in this case equal to 1 because I assumed that
δ(qn−1 ) is successful. This 0-2 cycle must exist to guarantee success: see theorem 5.2.

      0       1         ···           τn                               ···                                  n−2     n−1
                          ∗
    qn−1    gn−1       < gn−1                          0-2 cycle (long tail, 0 and 2)                         1
     qn      gn         < gn∗         vn              decreasing values ≤ vn + 2 (also, vn < gn∗ )                    ?

       Table 13: δ(qn−1 ) (top) and δ(qn ) (bottom): joint block structure. Labels represent the index k.


Now let’s focus on the bottom row, δ(qn ). By construction, the gray block has the same number of elements
as the 0-2 cycle in δ(qn−1 ). We don’t know what’s in it. By construction, it is followed by the last element in
green, and preceded by the yellow element whose unknown value is denoted as vn . In general the gray block in


                                                             16
δ(qn ) is not the 0-2 cycle. The 0-2 cycle may or may not exist. What we know is that except for δ0 (qn ) = qn
and δ1 (qn ) = gn , we have δk (qn ) < gn∗ , by virtue of (8) in lemma 5.3. In particular, this applies to vn . Also, all
values are even integers, and the total length of δ(qn ) is n, starting at index k = 0 and ending at k = n − 1.

If vn = 0, success is trivial. So, let’s assume that vn ≥ 2. By definition, δk (qn ) = |δk−1 (qn ) − δk−1 (qn−1 )|. Also,
at k = τn , δk (qn ) = vn . If k > τn , we are in the gray block in the bottom row, and the corresponding value
δk−1 (qn−1 ) in the top row is ≤ 2. Thus, δk (qn ) ∈ {δk−1 (qn ) − 2, δk−1 (qn )} unless δk−1 (qn ) = 0. We can ignore
that exception: when it happens, success is guaranteed. The challenge is when vn is large: do we have enough
runway, that is, is the the gray block long enough, to end up with δn−1 (qn ) = 1 in the rightmost cell?

To answer that question, let’s look at an example. Say vn = 14 at index k = 5, with the 0-2 cycle in δ(qn−1 ) as
featured in the top row in table 14. Then the sequence in the middle row succeeds: it ends with 1 in the green
cell.

        0    1         ···          5                                  ···                              17    18
                         ∗
      qn−1 gn−1       < gn−1        0     2       2     0     2   0     2    0    0     0    2     2    1
        qn   gn        < gn∗        14   14      12    10    10   8    8     6    6     6    6     4     2     1
        qn   gn        < gn∗        16   16      14    12    12   10   10    8    8     8    8     6     4     3

          Table 14: Sample δ(qn−1 ) (top) and δ(qn ) (two bottom rows). Labels represent the index k.

Now increase vn to 16, as shown in the bottom row. Then the sequence fails, as it ends with 3. Clearly, success
at qn depends on how many 2 you have in the 0-2 cycle of δ(qn−1 ), and how large vn is. More specifically, the
sequence succeeds if and only if vn ≤ 2ν2 (qn−1 ) + 2. In my example, ν2 (qn−1 ) = 6 and n = 19. We have success
if vn ≤ 14 = 2 × 6 + 2 and failure if vn > 14
Since vn < gn∗ , success is guaranteed if gn∗ ≤ 2ν2 (qn−1 ) + 2. □

Theorem 5.5 Let q1 , . . . , qn−1 be a valid, successful sequence and ν2 (qn−1 ) be the number of elements equal to
2 in the 0-2 cycle of its right diagonal δ(qn−1 ). Assume that gn∗ < nα where gn∗ is the record gap at qn , that is,
the largest gap ever encountered so far. If there is a constant β such that
                                              ν2 (qn−1 ) > nβ ,   with β > α,                                       (11)
then for n large enough, the sequence also succeeds at qn if it succeeds at qn−1 .
Proof: It is a corollary of lemma 5.4. For the prime number sequence, α = 0.525 works as proved by Baker in
2001, see [3]. Independently and unrelated to primes, β = 0.99 works, see part 4 in conjecture 5.1. Heuristics
suggest that ν2 (qn−1 ) ∼ n/2, an even stronger claim tied to (7) about balanced right diagonals. □

Essentially, my strongest claim is that the 0 and 2 in the 0-2 cycle of δ(qn−1 ) behave like the binary digits 0 and
1 in a normal number. Yet no one knows for a number like π if the proportion of 0 and 1 actually exists. But
I proved in [16] that for most numbers x included x = π, √  infinitely many times, the proportion of 1 is between
25% and 75% either for x, x + 31 , or both. Likewise, for 2, it was proved that the number of 1 in the first n
digits must be above 1.41nβ with β = 0.5. Given the analogy between normal numbers in base 2 and balanced
diagonals, this is encouraging in terms of the extra work needed to prove Gilbreath’s conjecture from where I
stand now.
     It is easy to prove that if δ(qn ) is strictly decreasing and gn∗ < n, then the sequence succeeds at qn as
it has enough runway to reach 1 at the end. Also, if qn is a magic prime, the sequence succeeds both at qn
by virtue of theorem 5.1, but also at qn+1 . This also applies to sequences other than prime numbers, where
“magic prime” is replaced by qn − qn−1 = 2 along with δ(qn ) consisting of 0 and 2 only (besides the first and
last elements). It also requires the condition gn∗ < nβ . I now summarize the unproved insights discovered so far
in the next conjecture 5.1.

Conjecture 5.1 The following was prepared for the prime number sequence. Some items in the list below may
apply to other valid sequences even outside the corridor (with much faster growth), under specific conditions.
 (1) If the sequence q1 , . . . , qn succeeds, adding qn+1 = qn preserves success. If it fails and adding qn+1 fails,
     then replacing qn+1 by any larger integer, will also fail. Thus there is a maximum qn+ ≥ qn such that for any
     q ∈ {qn , . . . , qn+ }, the augmented sequence with qn+1 = q, succeeds, but fails if you choose qn+1 > qn+ .
 (2) Thanks to this, you can run a binary search to efficiently find qn+ , using the bisection method with qn and
     2qn as the lower and upper bounds (resp.) for the initial search interval. Ignore the triangle, just work on
     the right diagonal: update it incrementally as needed. It ends with 1 if and only if the sequence succeeds.


                                                             17
 (3) The rightmost picture in figure 1 strongly suggests that for primes (qn = pn ), we have qn+ = qn + n + o(n).
     Also qn− = qn − n + o(n) if you allow for negative gaps. With success in all cases when qn− ≤ qn+1 ≤ qn+ .
     If true, it trivially proves the Gilbreath conjecture as there is always a prime between pn and pn + n, if
     pn ≥ 11. But it needs some care: o(n) could be as low as − log n or −n/ log n.
                                                                                     √
 (4) In the right diagonal δ(qn ), the section before the 0-2 cycle has fewer than n log n elements if n > 928.
     This is more than what we need to prove Gilbreath’s conjecture. Finally, for the prime number sequence,
     δ(qn ) is balanced for all n > 770. Also, (11) is satisfied if β = 0.99 and n > 2535, or β = 0.55 and n > 16.
     To prove Gilbreath, β > 0.525 is enough as it is tied to the best proven bound on prime gaps.

I tested the conjecture on the prime numbers and a few other sequences, with success up to the last value that I
tried (n = 104 ). But there are short artificial sequences where (1) is not satisfied, see tables 15 and 16. These
cases do not jeopardize my conclusions; chance of failure is always much higher at the beginning, and you can
replace the requirement qn+ ≥ qn by qn+ ≥ qn + 2 to drastically reduce the risk, ruling out non-valid sequences
as they are more prone to failures.
     The sequences covered in the conjecture not only have a 0-2 cycle at all qn (guaranteeing success by virtue
of theorem 5.2), but that cycle occupies almost the entire space in the right
                                                                         √ diagonal. Let ωn denote the length
of the section before the 0-2 cycle. For n large enough, we have ωn < n log n while the diagonal δ(qn ) has n
elements. None of this is proved yet despite massive empirical evidence. For n ≤ 2 × 104 , we have the following
statistics:
   • Magic primes (ωn = 0) represent 0.17% of the qn ’s. With guaranteed success. Since we also have success
     at the successor of a magic prime, we have “proven success” for 0.34%” of the qn ’s.
   • When the right diagonal is strictly decreasing, success is also proved: there is enough runway to reach 1
     at the end. This covers an additional 4.90% of the qn ’s, with provable success.
   • When ωn ≤ 10 at qn , we obviously have a 0-2 cycle if n ≥ 12, and thus success at qn , and also success at
     qn+1 based on theory. This covers 52.05% of the qn ’s.
   • When ωn ≤ 32 at qn , we obviously have a 0-2 cycle if n ≥ 34, and thus success at qn , and also success at
     qn+1 based on theory. This covers 96.29% of the qn ’s.
    • There is a little bias: ωn is less likely to be odd than even.
                                                                   √
In short, wn is overwhelmingly very small, much smaller than n log n for almost all qn . The high proportions
just cited are of course lower if you look at a bigger window, say n ≤ 105 , but they decrease very slowly with n.
Also, if you replace qn+1 by much larger qn+ , you still succeed (for primes, qn+ ≲ qn + n while qn+1 ≲ qn + n0.55
due to bounds on record prime gaps). Yet, replacing qn+1 by qn+ + 2 leads to failure. Understanding what makes
the former succeed and the later fail, may bring valuable insights. Another worthwhile investigation consists in
analyzing the spikes in figure 1. They are uncorrelated to magic primes locations, and absent in random primes
in figure 2. Finally, I developed a lighter version of Gilbreath’s problem, where the recursion to compute δ(qn ),
namely δk (qn ) = |δk−1 (qn ) − δk−1 (qn−1 )|, is replaced by
                                                                                 
                                     δk (qn ) = max |δk−1 (qn ) − δk−1 (qn−1 )|, 1 .                          (12)

It does not allow for 0 in the triangle (the minimum value is now 1), thus eliminating some complexity. In many
cases, failure in the standard problem also implies failure in this lighter version, but not always. The sequence
in table 2 is an exception. The prime number sequence still succeeds. I encourage the reader to play with this
easier version, establish the equivalent of conjecture 5.1 (let’s call it the baby conjecture), and try to prove it,
before attacking the standard version. In the python code, to use the light version, add delta=’light’ in
the arguments when calling the the check function from the gilbreath lib library.

                                   n≤5            n = 6 and q6 ≤ q5+ = 25           n = 6 and q6 > q5+ = 25
                  n        1   2    3    4    5   6 6 6 6 6                6   6 6 6 6 6 6 6
                  qn       2   3    5    9   15   15 17 19 21 23           25 27 29 31 33 35 37 39
                δ1 (qn )       1    2    4   6    0   2   4        6   8   10   12 14 16 18 20        22      24
                δ2 (qn )            1    2   2    6   4   2        0   2    4    6 8 10 12 14         16      18
                δ3 (qn )                 1   0    4   2   0        2   0    2    4 6 8 10 12          14      16
                δ4 (qn )                     1    4   2   0        2   0    2    4 6 8 10 12          14      16
                δ5 (qn )                          3   1   1        1   1   1    3     5   7   9   11 13 15

                       Table 15: Example with failure at qn+1 = qn , even though qn succeeds



                                                              18
                                                       n≤5                                 n = 6 and q6 ≤ q5+ = 17                       n = 6 and q6 > q5+ = 17
                              n            1       2           3   4           5       6        6   6     6 6 6                  6   6 6 6 6 6 6
                              qn           2       3           5   11          5       5        7   9    11 13 15                17 19 21 23 25 27 29
                          δ1 (qn )                 1           2       6       6       0     2      4        6   8       10 12           14 16 18 20 22                          24
                          δ2 (qn )                             1       4       0       6     4      2        0   2        4 6             8 10 12 14 16                          18
                          δ3 (qn )                                     3       4       6     4      2        0   2        4 6             8 10 12 14 16                          18
                          δ4 (qn )                                             1       2     0      2        4   2        0 2             4 6 8 10 12                            14
                          δ5 (qn )                                                     1        1   1        3   1       1       1       3       5       7       11 13 15

                              Table 16: Example with failure at qn+1 < qn+ , despite success at qn+1 = qn


I conclude this section with computational complexity. To check if a sequence with n elements succeeds, using
the full table is O(n2 ). If you stop at the first row with 0 and 2 only, it is O(n log n). If you rely solely on the
right diagonal, it is O(n). Likewise, searching for qn+ takes O(n) with brute force, and O(log n) with a binary
search assuming part (2) in conjecture 5.1 is true. Thus, the total number of operations to compute qn+ for all
k ≤ n ranges from O(n4 ) with the least efficient implementation, down to O(n2 log n) with the best one. As a
side note, integer polynomial sequences of degree d takes only d + 1 levels in the triangle to end up in a row
consisting of 0 only except for the first element.

5.3       Canonical form reduction and equivalence classes for sequences
If two sequences S1 , S2 have the same k-th order differences for some k > 0 (the k-th row in the triangle beneath
the sequence itself), that remains true for any k ′ > k. Thus, S1 succeeds if and only if S2 succeeds, if you ignore
the first k terms in both sequences for which success needs to be checked separately. The sequences S1 , S2 are
said to be equivalent at level k. If S1 has large gaps and S2 does not, it makes sense to work with S2 . Actually,
you can even work with any sequence S2′ built backwards one level above k. And neither S2 nor S2′ need to be
valid: in short, they do not need to be strictly increasing; they can be oscillating with tiny gaps up and down.
     Tables 17 and 18 illustrate the concept. Why work with the prime number sequence S1 if you can work with
its equivalent at level 3, the sequence S2 ? The triangles are the same, except for the first two rows at the top.
With S2 , success is already guaranteed at level 1, as the first row contains only 0 and 2. The numbers highlighted
in yellow, on the left, represent the maximum value in the corresponding row. The next question is how to build
levels backwards, going up starting from below, rather than the other way around. However, we have a problem:
the recursion δk (qn ) = |δk (qn−1 )−δk−1 (qn−1 )| is not invertible. In fact, there is a very large number of “inverses”.
They are all built with the following multivalued formula, with both options in (14) equally acceptable:

                                                                           (
                                                                               δk (qn ) + δk (qn−1 )                 if δk (qn ) < δk (qn−1 )                                                             (13)
                                               δk−1 (qn ) =
                                                                               δk (qn ) ± δk (qn−1 )                 otherwise                                                                            (14)

That’s how I built S2 . It is easy to check that the two tables satisfy both the inverse and standard recursions.
The row at level k is denoted as δk , with k = 0 for the sequence itself. The leftmost element at level k is denoted
as δk (q1 ), and equal to 1 if k > 0 except in case of failure. When building S2 , first its level 2 based on level 3 in
table 17, then its level 1 recursively, then S2 on top of level 1, I chose the minus sign in (14) whenever possible.
This construction leads to the level 3 canonical form of S1 , in this case S2 based on level 3 at S1 .

          2       3       5        7       11 13 17 19 23 29 31                                                      2       1       1       1       3       3       1       1        3       3       3
      6       1       2       2        4       2           4       2       4       6        2                    2       1       0       0       2       0       2       0       2        0       0
      4           1       0        2       2       2           2       2       2       4                         2           1       0       2       2       2       2       2        2       0
      2               1       2        0       0           0       0       0       2                             2               1       2       0       0       0       0       0        2
      2                   1        2       0       0           0       0       2                                 2                   1       2       0       0       0       0        2
      2                       1        2       0           0       0       2                                     2                       1       2       0       0       0       2
      2                            1       2       0           0       2                                         2                           1       2       0       0       2
      2                                1       2           0       2                                             2                               1       2       0       2
      2                                    1       2           2                                                 2                                   1       2       2
      1                                        1           0                                                     1                                       1       0
      1                                                1                                                         1                                           1

       Table 17: The prime numbers sequence S1                                                                   Table 18: Seq. S2 equivalent to S1 at level 3



                                                                                                        19
Let λ be the chosen number of levels, for instance, λ = 3 in table 18. You would think that always choosing the
minus sign in (14) leads to a sequence S2 with minimum growth as shown in table 18. In general, this is not the
case when n or λ is large: S2 grows much faster than S1 as the technique is a variant of the greedy algorithm.
Of course, selecting the plus sign would result in even much faster growth. The slowest growth is achieved with
a combination of pluses and minuses.
     The benefit of the canonical form is that the largest gap in S2 remains small if λ is not too small compared
to n. We want λ = λn large enough, yet with λn = o(n). Then we can increase both λn and n iteratively,
with n growing much faster than λn , without ever facing a gap larger than 2 except in case of failure. See
table 19 for illustration: for maximum efficiency, λn grows at a rate similar to that of the n-th record gap gn∗ in
prime numbers (OEIS sequence A005250), while n follows the growth rate of the index of the record in question
(OEIS sequence A005669). Under these conditions, the maximum gap in the first n terms of S2 is conjectured
to always be 2. To avoid confusions, S2 is denoted as S2 (λn ) to indicate that it is the canonical form of S1 at
level λn .

                                        n   50 200 1000 8000 20000 40000
                                       λn 10     20    36        66   66    96
                                       gn∗ 14    22    34        72   86   112

                                      Table 19: Level λn guarantees max gap
                                        ≤ 2 in the first n terms of S2 (λn )


     When building S2 (λn ), you iteratively create news rows in the triangle on top of each other, above level
λn . In each of these rows, the first value must be initiated. I set the first value to 1 to keep success at all levels,
assuming this was the case for the parent sequence S1 . But what would happen if you set one or two of these
initial values to 3, 5, or any larger odd integer, thus causing failure in S2 (λn )? In other words, getting some
rows in the new triangle to start with a value > 1. You can do it in the program by specifying a non-empty list
of failing levels (above λn ), via the optional argument fail level in the canonical function located in the
Gilbreath lib library. In my example, I use the prime number sequence with n = 1000 for S1 and λn = 400
for S2 , choosing 2 levels λ1 <λ2 <λn starting with 3 rather than 1, with λ1 = 120. The results are as follows:
   • Because λn is much larger than needed given n, the successful sequence S2 (λn ) (when no failures are
     added) consists only of 2 at the beginning, followed by either 1’s or 3’s as in table 18. Actually, the first
     λn values, besides the 2 at the start, are all 1. You can see it in figures 5 and 6, where the green “curve”
     represents the successful sequence on a log scale, taking on two distinct values only: 1 and 3, that is, 0
     and log 3 on a log scale. With the first 400 flat before oscillating randomly between the two.
   • The red curve represents S2 (λn ) when adding failure at λ1 = 120, λ2 = 143 (figure 5) or λ1 = 120, λ2 = 144
     (figure 6). Failures are magnified in S2 (λn ). When λ2 = 143, the magnification is massive with values > e40
     in the first 400 terms.
   • In conclusion, adding two failures generates one of the following: (1) little blips detectable in the first 400
     terms, (2) a strong explosion highly visible as in figure 6, or (3) a titanic blast that dwarfs everything else
     and can go on well beyond the first 400 terms as in figure 5, possibly forever. Failures at levels such as
     case (3) can not exist in practice; it does not happen in natural sequences, even faulty ones. Yet it is one
     of the most common when reverse building a sequence by adding failures at random levels. In short, the
     failure levels can not be random. These insights are summarized in statement 5.1.
   • What will cause a little blip, a strong explosion, or a titanic blast is impossible to predict. Failure levels
     well spaced out produce little blips. Other than that, the proximity between failing levels, how close to
     the top level the failures are located, the parity of λ1 and λ2 , and the left value on a failing row (with >3
     worse than 3) are the top factors influencing the outcome. Here I assume that λn is large enough so that
     there are only 0 and 2 at level λn , besides the leftmost value.

Statement 5.1 For a slow growth sequence such as the prime numbers or synthetic primes, if it has more than
one failing point, there are strong constraints on the distance between these failing points, and the parity of
their indexes. Failures cannot happen at random locations, regardless of the gap sizes. Otherwise, the canonical
sequence may explode in a way that is incompatible with acceptable bounds.

I conclude this section with a probabilistic argument. I am interested in a probability central to the triangle:
the one that dictates how frequently the plus and minus signs occur in (14). More specifically, let
                                                                     
                                          πk = P δk (qn ) < δk (qn−1 ) .                                    (15)



                                                            20
The canonical function in the code returns these probabilities as the output vector s1 proba, estimated on
S1 . For each k, it is computed by averaging on n = 1, 2 and so on. As usual, k specifies the level, with k = 1 for
the first order differences. Instead of always choosing the minus sign in (14) to produce S2 , one may choose to
randomly alternate +/- at each level k (1 ≤ k < λn ) to slow the growth. And decide how frequently to accept
the minus sign depending on πk . My first attempt at that was inconclusive, but it revealed interesting facts:
    • Of course π1 = 1 since the sequence S1 is strictly increasing. Based on n = 20, 000, the next values for the
      prime number sequence are π2 = 0.69, π3 = 0.65, π4 = 0.49. But for my synthetic primes, these values are
      π2 = 0.91, π3 = 0.51, π4 = 0.40. The large differences confirm that the prime numbers do not abide well
      with the laws of randomness.
    • Eventually, both for real and synthetic primes, πk decays to about 0.25 as k increases. This may sound like
      a mystery, but it has a simple explanation: when k is large and the rows contain just 0’s and 2’s, there are
      4 possible combinations for δk (qn ), δk (qn−1 ) , each equally likely: (0, 0), (0, 2), (2, 0), and (2, 2). Only
      (2, 0) satisfies (14). This leads to my next and last conjecture.

Conjecture 5.2 For many sequences with no failing points including prime numbers and synthetic primes, as
k increases, the k-th row in the triangle consists almost exclusively of 0 and 2 in equal proportions. Also, rows
k and k + 1 are uncorrelated. Of course, this is not true for integer polynomial sequences ending with 0 only,
or the geometric progression 1, 2, 4, 8, 16 and so on, staying the same for all rows.


6      Applications: cybersecurity, fraud detection and Fintech
I now discuss applications. In particular, I extend the concept of successful sequence to continuous time series
such as Brownian motions, and how success or failure translates into real-world data, and how to interpret it.
I focus on modeling, data synthesis, random number generation and testing, liabilities in cryptography heavily
relying on prime numbers, as well as error and pattern detection—especially hidden or hard to detect patterns.

6.1     Hidden patterns, error detection, checksum, and data quality audit
Adding failure points at different levels when building the triangle backwards (from a lower level to the top)
creates irregularities in the reconstructed sequence. There is another way to look at it, with practical applications
to detect errors in real-life data: compute the differences in absolute value (first, second and higher orders). If
some rows in the triangle start with a value other than 1, it is an indicator of potential error or data quality
issue. Especially if it impacts multiple rows and the starting value is higher than 3.




    Figure 5: Data issue detected via the canonical form:        Figure 6: Same as figure 5 but with less severe problem.
    green signal when no problem is found, red otherwise.        The green signal takes on 2 values only, and starts flat.


Reconstructing the sequence backwards to find its canonical form, magnifies the errors as seen in figures 5 and 6.
It offers another way to reveal hidden patterns, errors and other types of issues in your dataset. In the figures
in question, the curves represent the reconstructed sequence in its canonical form, denoted as S2 in section 5.3.
The red curves correspond to corrupted data, that is, a row in the triangle not starting with 1. The left element
in each row plays the role of a checksum or error flag. When there is no issue (all rows start with 1), you get the
green signal instead. This method can be combined with the standard technique for error detection, explained
in [19].


                                                            21
6.2    Fraud detection and transaction score synthesis
There are many similarities between the admissible, valid sequences in this article, and credit card history and
transaction scoring, if you replace failure/success by fraud/no fraud or accepted/declined. The sequence corridor
in section 3.2 is the equivalent of the credit card limit over time based on customer history, slowly increasing,
or much faster or even decreasing or blocked based on circumstances, while qn plays the role of the transaction
amount. Each sequence represents a customer.
     The proportion of failures is low, comparable to that of fraudulent transactions. Like credit card issuers, I
had to generate synthetic data to understand the various mechanisms that cause them. Analogy to rule-based
systems is provided by the forbidden prime constellations. And finally, qn+ in section 5.1 is the critical threshold
(based on the whole history) that tells you if the new value qn+1 (the new credit card transaction) is flagged as
fraudulent or not, or in my case, as success or failure. A too high value is a typical cause of failure (or declined
transaction), but it depends on history with some sequences (credit card users) allowed much larger values. The
subtle cause of failure in non-trivial cases, is due to complex patterns not involving large values.
     To conclude, the large sequence dataset gil output.txt and its many features, available upon request,
is a great sandbox to test fraud detection and transaction scoring algorithms. Perhaps the next step, both in
the credit card industry and in my sequence system, is to generate all the possible patterns (trillions of them),
then cluster and categorize them to finally attach a label to each of them: fraud or no fraud. This would lead
to more efficient detection, especially in real time. I started to gather all the possible patterns in my system,
see section 3, but I have yet to cluster them. Labeling as success/failure is trivial in my case, as that flag is in
the dataset by construction and readily available for any future “transaction”. This last part is what makes my
data particularly attractive in the context of testing fraud detection systems.

6.3    Cellular automata random generator and new tests of randomness
As noted in the last paragraphs in section 5.3, when you start with a large sequence and build the triangle from
top to bottom, after a number of levels, you end up with uncorrelated rows consisting of 0 and 2 only in about
the same proportions. This is the case when you start with the prime number sequence or synthetic primes, and
indeed with most non-failing sequences. The mechanism behind the scenes is well understood: each element in
the triangle is the difference in absolute value of the two elements above it. This operation is responsible for the
scrambling. Also, it prevents you from retrieving the elements in a row if you only know the elements one level
below or further down. Exceptions include biased sequences such as prime numbers where reverse engineering
is somewhat less difficult due to forbidden patterns.
     Thus, you can use the bottom rows of a triangle as a random number generator (PRNG). The code below
does that efficiently, starting with a sequence consisting of n bits, and then computing the successive differences
in absolute value. To keep the same number of terms in each row, I add one bit to the right at each level. The
bit in question comes from a precomputed bitstream, here the array last bit.
      import numpy as np
      from PIL import Image

      np.random.seed(40)
      n = 1000
      n_levels = 1000
      sequence = np.random.binomial(n=1, p=0.5, size=n)
      last_bit = np.random.binomial(n=1, p=0.5, size=n_levels)

      bitmap = []

      for k in range(n_levels):
         new_sequence = np.abs(sequence[:n-1] - sequence[-(n-1):])
         new_sequence = np.append(new_sequence, last_bit[k]) ##
         covar = np.corrcoef(sequence[:n-1], new_sequence[:n-1])
         count_0 = np.count_nonzero(sequence == 0)
         count_1 = np.count_nonzero(sequence == 1)
         print(k, sequence[:20], count_0, count_1, covar[0, 1])
         sequence = new_sequence
         bitmap.append(sequence)

      scaled_array = np.array(bitmap, dtype=np.uint8) * 255
      img = Image.fromarray(scaled_array, mode=’L’).convert(’1’)
      img.save(’bitmap_output.png’)

In chapter 8 in my new book [16], I discuss NPG, one of my cryptographically secure PRNGs, faster, and more
random than the most recent additions to the Numpy library: PCG64 and PCG64DXSM. See my article on
the topic, here, where I also introduce a new test of randomness: predicting the next bits using large language


                                                        22
models, similar to predicting the next tokens, and based on a deep neural network (DNN). Bitstreams for which
the correct prediction rate is > 52% or < 48% are flagged as unsecure. For a fast alternative to DNNs, where
the global optimum of the loss function is obtained in one shot with a simple closed-form formula, thus without
training, see my blog post here, and my article on the topic [17].




    Figure 7: Random numbers generated with the code in section 6.3; each line is a level (n = 1000, 1000 levels)


With binary numbers as in the above code, |a−b| = XOR(a, b). The resulting triangle is identical to the output of
the rule 90 cellular automaton [Wiki], extensively studied [12] with numerous applications. Also, the associated
random number generator is fast, see xoroshiro [5]. By contrast to xoroshiro, my system leads to a non-periodic
PRNG thanks to the addition of the rightmost bit at each level. However, the raw version lacks some randomness
as seen in figure 7: the patterns are similar to the Sierpiński triangle and identical to those in the Thomas matrix
introduced by James Thomas in 2004, see here. Zoom in on the picture to see more granular details. For other
chaotic behavior linked to iterated differences in absolute value, see section 7.2.2 in [16].
     Finally, the material in this article led to yet another test, not found in most standard libraries: checking
the indexes of the successive records in run lengths. Having more than log2 n consecutive 0 in the first n bits
at any level in the triangle, violates the laws of randomness and increases the risk of sequence failure. When
running the above code snippet, the initial sequence fails the record run test. The Mersenne Twister in the
Numpy random module causes the issue: there is a run of 8 ones in the first 14 bits; the maximum allowed
this early is 4. In practice, the initial sequence is the seed of my new PRNG. A good choice is a combination
of interlaced binary digits coming from the square roots of various integers; the same applies to last bit.


                                                         23
6.4    Unusual patterns in time series: modeling, detection and synthesis
Gilbreath’s conjecture and its traditional generalizations [6] apply to discrete integer sequences with small growth,
strictly increasing and random in some ways. Here I show how it also works for discrete or time-continuous time
series, smooth (no randomness) or highly chaotic, with massive or no growth, or even decreasing or oscillating.
I also discuss industrial applications, for instance in financial time series modeling. Case studies are featured in
figures 8 and 9, where the red and green curves illustrate (resp.) sequence failure and success. In particular, fig-
ure 8 shows time-continuous Brownian motions generated via a discrete random walk (the underlying sequence)
with jumps up and down following a Poisson distribution of parameter λ. Success or failure is dictated by the
value of λ, with higher λ more prone to failures.




Figure 8: Brownian motions moving in the same direction          Figure 9: Two smooth curves with nearly identical
at each step; red fails the test, but the green one passes it     parameters; red fails the test, green one passes it


At a macro level, what makes the green and red curve different, resulting in a different success status, is visible to
the naked eye: it is the amount of volatility. But in many cases, the chaos is well hidden and not visible. A good
example is the sequence in table 10. Also, the two examples in figures 8 and 9 are borderline: green is close to
failure and red close to success. What if we could have a metric that automatically quantify chaos and categorize
time series at any given time based on invisible yet disruptive patterns, to make appropriate decisions such as
buying or selling assets? The Lyapunov exponent is one of several metrics but it does not reveal hidden patterns.
More are discussed in my book on chaotic dynamical systems [15]. A metric that takes into account more subtle
patterns would be useful. And the material in this paper offers several alternatives for quantized data:
   • How many levels it takes in the triangle to reach the first row consisting only of 0 and 2 (besides the odd
     value at the start of each row)? The fewer you need, the less chaotic the sequence. Here chaos is defined
     not in a classical sense, but in connection to the triangle behavior.
   • The number of failure points: how many times a row in the triangle starts with 3 instead of 1? Or worse,
     with 5 or above? How spaced out are these failure points? It quantifies the level of chaos and the intensity
     of each failure point.
   • In case of success, how close are we to a failure at any given time? This is linked to the distances |qn+1 −qn+ |
     and |qn+1 − qn− |, and shown in figures 1–4. In case of failure, how close are we to success?
   • Is the canonical form of the sequence error-free, that is, do you get the green signal in figure 6, or the
     red one? And in case of errors, do we observe little blips, or a big explosion as in figure 6? The case in
     figure 5 (titanic, long lasting or permanent blast) cannot happen in real-life data.
   • For the prime number sequence and synthetic primes (both well behaved) at some point in the triangle,
     we end up with 0 and 2 only, evenly and uniformly distributed within each row. In addition, rows at this
     stage are independent from each other (uncorrelated). Is this the case for your data? Even though real
     and fake primes are well behaved, the real ones exhibit little spikes in figure 1; fake ones in figure 2 don’t.
     Those little spikes, if found in your data in a well behaved sequence, indicate some small irregularities and
     pinpoint their locations. The spikes point outward, which is good. If they were pointing inward, it would
     increase the risk of failure.
   • Are there missing patterns in your sequence, in the first order differences? That is, expected patterns that
     are absent, such as the forbidden constellations in the prime number sequence. Missing patterns in the
     second or higher order differences is an indicator of a bigger problem.



                                                            24
Finally, a time series can change from chaotic to smooth, or from fast to slow growth or even oscillating, even
multiples times each with a different duration, yet succeed. Another series, apparently better behaved when
seen with the naked eye, may fail. Eventually, what my system flags as failure or success in a time series with
structural changes is not how volatile it suddenly becomes, but whether the transition between the different
phases is well controlled or not. My set of metrics should be tested and fine-tuned on real data to see if it can
catch a shift before other indicators notice it when it is too late for actions. Be it financial or Earthquake data.

6.5    Security issues in ciphers relying on prime numbers
Prime numbers have patterns that significantly increase their odds to satisfy Gilbreath’s conjecture, compared
to other sequences with similar growth, but more random. For instance, you cannot find 2, 2, let alone 2, 2, 2, 2,
in successive prime gaps except at the very beginning. Yet 2, 2 is the most basic pair, one of the most frequent
in random sequences, but it is banned in prime numbers, and referred to a forbidden prime constellation. At
the same time, 2, 2, 2, 2 followed or preceded by a large gap, and then by another (say) 2, 2, 2 is among the
most dangerous configurations: it can kill success if happening too soon in the first order differences. Another
forbidden prime gap pattern is 2, 4, 2, 4, 2, and again, linked to higher failure risk. There are many others, all
with small numbers (thus abundant in other sequences but absent in primes), giving prime numbers some extra
immunity against failure.
     But what makes prime numbers strong in Gilbreath’s context is exactly what makes them weak in cyber-
surity. The prime gaps are anything but random. And while there might be no forbidden patterns in higher
order differences (the rows below prime gaps in the triangle), the pattern distribution remains biased down-
wards, with probabilities attached to patterns not matching those found in random data or synthetic primes.
Put it differently, given any row in the triangle, it is possible to tell whether or not it comes from prime numbers
by looking at the probabilistic structure attached to the row in question. In short, reverse engineering is feasible
if the original sequence consists of prime numbers, despite the obfuscation created by successive differentiating
in absolute values. Ciphers or crypto-secure random numbers derived mostly from prime numbers but lacking
strong obfuscation—and there are still many around—are subject to the same problem caused by congruential
constraints.


7     Conclusions
Gilbreath’s conjecture, first stated by François Proth in 1878 and unproved to this day, features a very simple
pattern among prime numbers. It is well-known in mathematical circles as a very challenging unsolved mystery.
In this paper, I discuss a path towards a resolution, as well as applications pertaining to Fintech, chaotic systems,
cybersecurity, high performance computing, data synthesis, random number generation, fraud detection and
more, well beyond the original scope.
     From a research perspective, Gilbreath’s conjecture has little to do with prime numbers: a large class of
sequences, including many with either slow or fast growth, with either chaotic or smooth behavior, satisfy it.
Yet the prime number sequence has something unique that makes it the ideal candidate. It’s not its random
character: deterministic patterns such as forbidden prime number constellations, actually contribute to its
success while the lack of randomness is a cybersecurity liability. Also, I proved that the Sieve of Eratosthenes
leads to sequences that satisfy the conjecture. It also works if you sieve in any order. Sieving in reverse order
allows you to assess the long-range impact of small primes. This technique may be used to discover new results,
perhaps about twin primes. For instance, the sum of the inverse of twin primes converges; the proof is based
on standard sieving.
      This paper turns what was initially recreational math into mainstream computer science, dynamical sys-
tems, and number theory, with significant research and application potential across multiple disciplines, and
many new opportunities yet to be explored. Along the way, it leads to interesting integer sequences , some listed
in the OEIS encyclopedia, and some waiting to be added such as magic primes where success is always guaran-
teed. Finally, it features high performance computing at its best, with intense simulations to help progress and
in some instances, even to prove statements. Equivalent sequences and sequence reduction eliminate large gaps,
facilitate theoretical research, and leads to applications such as hidden patterns discovery, error detection, and
data quality audit. The connection to cellular automata leads to a very efficient random generator.


References
 [1] Ryan Alweiss and Sammy Luo. Bounded gaps between primes in short intervals. Preprint, pages 1–29,
     2017. arXiv:1707.05437 [Link]. 11



                                                         25
 [2] Christian Axler. Effective estimates for some functions defined over primes. Integers, 24:227–251, 2024.
     [Link]. 7
 [3] R. C. Baker, G. Harman, and J. Pintz. Bounded gaps between primes in short intervals. Proceedings of
     the London Mathematical Society, 83:532–562, 2001. 11, 16, 17
 [4] William Banks, Kevin Ford, and Terence Tao. Large prime gaps and probabilistic models. Inventiones
     mathematicae, 233:1471–1518, 2023. arXiv:2605.23014 [Link]. 11
 [5] David Blackman and Sebastiano Vigna. Scrambled linear pseudorandom number generators. ACM Trans-
     actions on Mathematical Software, 47:1–32, 2021. arXiv:1805.01407 [Link]. 23
 [6] Zachary Chase. A random analogue of Gilbreath’s conjecture. Mathematische Annalen, 388:2611—-2625,
     2023. [Link]. 1, 8, 24
 [7] Zachary Chase, Zach Hunter, and Terence Tao. Gilbreath’s conjecture: a Cramér random model and a
     deterministic analysis. Preprint, pages 1–28, 2026. arXiv:2607.08712 [Link]. 11
 [8] Chak Kwong Cheng and Hakan Demirtas. Generation of multivariate discrete data with generalized Poisson,
     negative binomial and binomial marginal distributions. Preprint, pages 1–19, 2026. arXiv:2602.07707 [Link].
     11
 [9] Congzao Dong, Alexander Marynych, and Viacheslav Melnykov. Random sieves and generalized leader-
     election. Austrian Journal of Statistics, 52:13–25, 2023. 4
[10] Pierre Dusart. Explicit estimates of some functions over primes. The Ramanujan Journal, 45:227–251,
     2018. [Link]. 7
[11] Kevin Ford et al. Large gaps between consecutive prime numbers. Annals of Mathematics, 183:935–974,
     2016. [Link]. 4
[12] Henryk Fukś. Solvable Cellular Automata, Methods and Applications. Springer, 2023. [Link]. 23
[13] Daniel A. Goldston, János Pintz, and Cem Y. Yı́ldı́rı́m. Primes in tuples I. Annals of Mathematics,
     170:819–862, 2009. [Link]. 12
[14] Andrew Granville. Harald Cramér and the distribution of prime numbers. Scandinavian Actuarial Journal,
     1:12–28, 1995. [Link]. 4
[15] Vincent Granville. Gentle Introduction To Chaotic Dynamical Systems. MLT, 2023. [Link]. 24
[16] Vincent Granville. Breakthroughs on the Digit Distribution of Classic Constants. MLT, 2026. [Link]. 17,
     22, 23
[17] Vincent Granville. LLMs without deep neural networks: New architecture, benefits and case study.
     Preprint, pages 1–9, 2026. arXiv:2605.30385 [Link]. 23
[18] George Grob and Matthias Schmitt. Cycles and patterns in the sieve of Eratosthenes. Preprint, pages
     1–18, 2019. arXiv:1905:03117 [Link]. 4
[19] P.G. Guest. The estimation of standard error from successive finite differences. Journal of the Royal
     Statistical Society: Series B, 3:233–237, 1951. [Link]. 21
[20] Abhishek Jha. The Poisson tail conjecture for primes in short intervals. Preprint, pages 1–30, 2026.
     arXiv:2605.23014 [Link]. 11
[21] Daniele Lattanzi. Statistical distributions of prime number gaps. Journal of Advances in Mathematics and
     Computer Science, 39:36–61, 2024. [Link]. 11
[22] Helmut Maier. Chains of large gaps between consecutive primes. Advances in Mathematics, 39:257–269,
     1981. [Link]. 8
[23] James Maynard. Small gaps between primes. Annals of Mathematics, 181:383–413, 2015. [Link]. 12
[24] Leila Muney. Holes in valid-extension sets of finite gilbreath sequences. Preprint, pages 1–36, 2026.
     arXiv:2606.23721 [Link]. 2
[25] Janos Pintz. On the distribution of gaps between consecutive primes. The Ramanujan Journal, 45:1–22,
     2014. [Link]. 8
[26] Simon Plouffe. Preprint, Verification of Gilbreath’s conjecture up to 1014 :1–7, 2025. arXiv:2510:06688
     [Link]. 1, 4
[27] Terence Tao. Large gaps between consecutive prime numbers. Terence Tao’s Blog, 2014. [Link]. 4
[28] Wang and Cheng-Ting. On the maximal gap between primes. Preprint, pages 1–8, 2025. arXiv:2510.17065v1
     [Link]. 11
[29] Mario Ziller. On differences between consecutive numbers coprime to primorials. Preprint, pages 1–14,
     2020. arXiv:2007:01808 [Link]. 4



                                                      26
     A     Appendix: Python code
     The main program gilbreath3.py is listed in section A.1. It imports gilbreath lib.py, a home-made,
     internal library. The latter is listed in section A.2. Also, in section A.1, I included a summary, linking the
     various parts and functions in the Python code, to the sections and figures in this article.

     A.1     Main program
     The code is also on GitHub, here. Below is a summary linking the different parts to the material in this article;
     gil stands for the gilbreath lib.py library.
         • Data synthesis (synthetic primes): Function: gil.generate random sequence. Lines 36–104 in the
           code. Section 4.1 in the paper.
         • Forbidden prime constellations: Function: gil.banned found in seq. Lines 98 in the code. Sec-
           tion 4.2 in the paper.
         • Sequence reduction (canonical): Functions: gil.canonical, gil.generate random sequence.
           Lines 105–141 in the code. Sections 5.3 and 6.1 in the paper.
         • Sequence augmentation (qn+ , qn− ): Functions: gil.collect statistics, gil.max gap allowed,
           gil.augment, gil.generate random sequence, gil.test conjecture, gil.arr plot. Lines
           142–255 in the code. Section 5.1 in the paper.
         • Sieving and reverse sieving: Lines 256–322 in the code. Section 2 in the paper.
         • Continuous time series: Lines 338–408 in the code. Section 6.4 in the paper.
         • Full list of short sequences: Functions: gil.admissibility, gil.get all sequences. Lines
           409–457 in the code. Section 3 in the paper.
     The code is based on Python 3.13.3. Besides my library gilbreath lib.py listed in section A.2, it requires
     Numpy 2.2.5, Matplotlib 3.10.1, PrimePy, and Time. It also produces the output file gil output.txt, which
     is not discussed in the article but linked to the computation of qn+ . Throughout the code, the main sequence is
     denoted as arr a, its last element qn as the variable a, and the first order differences as first diff.

1    import importlib
2    import gilbreath_lib as gil
3    importlib.reload(gil)
4
5    import time
6    import numpy as np
7    import matplotlib.pyplot as plt
8    import matplotlib as mpl
9
10   mpl.rcParams[’axes.linewidth’] = 0.5
11   plt.rcParams[’xtick.labelsize’] = 8
12   plt.rcParams[’ytick.labelsize’] = 8
13   plt.rcParams[’legend.fontsize’] = ’x-small’
14
15
16   #--- 1. Showing how central function gil.check works
17
18   nprimes = 30
19   from primePy import primes
20   prime_list = primes.first(nprimes)
21   arr_a = prime_list[0:nprimes]
22   # arr_a = [2, 3, 5, 11, 13, 15, 31, 33, 35, 39, 51 ]
23   print("--- Part 1: gil.check\n")
24
25   flag, first_amax_idx, hash_stats = gil.check(arr_a, show_triangle = ’Full’, mode = ’Full’, delta =
         ’standard’)
26
27   right_diagonal = hash_stats[’right_diagonal’]
28   left_diagonal = hash_stats[’left_diagonal’]
29   failing_level = hash_stats[’failing_level’]
30   print("Right diagonal:", right_diagonal)
31   print("Left diagonal:", left_diagonal)
32   print("Failing_level:", failing_level)
33   print()
34
35
36   #--- 2. Detect failed sequences by simulation [Poisson increments]
37




                                                            27
38    parameters = {
39                ’prime’: [1.0, 1.3, 1.50, 5],
40                ’power’: [0.9, 1.1, 1.25, 5, 1.50],
41              }
42
43    model = ’prime’
44
45    n = 60 # number of values to add after arr_init
46    nsamples = 400
47    llambda = 1.5
48    rejection_sampling = True # set to True to guarantee sequences are in the corridor
49    arr_init = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
50    rng = np.random.default_rng(seed=42)
51
52    offset = len(arr_init)
53
54    from primePy import primes
55    prime_list = primes.first(n + offset)
56    p_n = prime_list[-1]
57    success = 0
58    in_corridor = 0
59    sum = 0
60    hash_fail = {}
61    print("--- Part 2: Simulations\n")
62
63    for sample in range(nsamples):
64
65       arr_a = gil.generate_random_sequence(n, arr_init, llambda, parameters, model, rng)
66       sum += arr_a[-1]
67       flag, first_amax_idx, hash_stats = gil.check(arr_a, show_triangle = ’None’)
68       failing_level = hash_stats[’failing_level’]
69       first_diff = hash_stats[’first_diff’]
70       left_diaginal = hash_stats[’left_diagonal’]
71       valid, bounded, smooth, fvals, sequence = gil.admissibility(first_diff, parameters, model) #
             fvals empty if in corridor
72
73       if flag == ’Fail’ and (bounded or smooth):
74
75          snapshot = arr_a[offset-1 : failing_level]
76          left_diagonal = hash_stats[’left_diagonal’]
77          sigma = 1 + left_diagonal[-1]
78          failing_diff = tuple(first_diff[0:failing_level])
79          gamma = np.max(failing_diff)
80          hash_fail[failing_diff] = (failing_level, sigma, gamma, failing_diff[-2], failing_diff[-1])
81          print("Failed:", sample, failing_level, sigma, bounded, smooth, arr_a[-1],
82                       p_n, failing_level, first_diff[0:failing_level])
83
84       if bounded and smooth:
85          in_corridor += 1
86       if flag == ’Success’:
87          success += 1
88       if sample % 500 == 0:
89          print("Sample", sample, success-1)
90
91    avg_last_value = sum/nsamples
92
93    for first_diff in hash_fail:
94
95       value = gil.make_readable(hash_fail[first_diff])
96       first_diff = gil.make_readable(first_diff)
97       first_diff_seq = first_diff[offset-6:len(first_diff)]
98       banned_found, banned_pattern = gil.banned_found_in_seq(first_diff_seq)
99       banned_pattern = gil.make_readable(banned_pattern)
100
101   failed_deduped = len(hash_fail)
102   print("Simulations:", success, "/", nsamples, avg_last_value, p_n, in_corridor, failed_deduped)
103   print()
104
105   #--- 3. Canonical form of sequence
106
107   n_levels = 400
108   fail_levels = { 120:3, 281:3 } # err1.png
109   fail_levels = { 120:3, 143:3 } # err2.png
110   fail_levels = { 120:3, 144:3 } # err3.png
111
112   N = 1000



                                                        28
113   primes_ = ’real’ # options: ’real’ or ’fake’
114
115   if primes_ == ’real’:
116      prime_list = primes.first(N)
117   else:
118      arr_init = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
119      llambda = 2.5
120      prime_list = gil.generate_random_sequence(N, arr_init, llambda, parameters, model, rng)
121
122   s1 = np.copy(prime_list)
123   valid = False
124   print("--- Part 3: Canonical form\n")
125
126   s2_failed, s2_failed_gaps, s1_bottom, s1_max_gap, s1_proba = gil.canonical(s1, n_levels, fail_level
          = fail_levels, valid = valid)
127   s2_succes, s2_succes_gaps, s1_bottom, s1_max_gap, s1_proba = gil.canonical(s1, n_levels, valid =
          valid)
128
129   plt.gca().set_facecolor(’black’)
130   arr_k = np.arange(2, len(s1))
131   plt.plot(arr_k, np.log(s2_failed[2:]), c=’red’, lw=0.9)
132   plt.plot(arr_k, np.log(s2_succes[2:]), c=’green’, lw=0.6)
133   for k in fail_levels:
134      plt.axvline(x=k, color=’gray’, linestyle=’--’, linewidth=0.4)
135   plt.axvline(x=n_levels, color=’gray’, linestyle=’--’, linewidth=0.4)
136   plt.show()
137
138   print("Summary:", N, n_levels, np.max(s2_succes_gaps), np.max(s1_bottom), np.max(s2_succes),
          np.max(s1), s1_max_gap)
139   print("Probas:", s1_proba[0:5])
140
141
142   #--- 4. Find bounds for next prime, to keep the sequence successful moving forward
143
144   sequence_type = ’prime_gaps’ # options: ’primes’, ’log_gaps’, ’power_gaps’
145   prime_type = ’real’ # ’real’, ’simulated’
146   nprimes = 5000
147   start = 2 # must be 2 or higher
148
149   test_mode = False # very slow if True, will test conjecture
150   if test_mode:
151      conjecture = ’satisfied’ # satisfied until proven wrong
152   else:
153      conjecture = ’untested’
154
155   if prime_type == ’real’:
156      from primePy import primes
157      prime_list = primes.first(nprimes)
158   else:
159      arr_init = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
160      llambda = 2.5 # 5
161      prime_list = gil.generate_random_sequence(nprimes, arr_init, llambda, parameters, model, rng)
162      flag, acheck, hash_stats = gil.check(prime_list, show_triangle = ’None’, mode = ’Fast’)
163      print("check status of generated sequence:", flag)
164
165   arr_k = []
166   arr_min = []
167   arr_max = []
168   arr_a = []
169   arr_old_a = []
170   resets_list = ()
171   a = prime_list[start-1]
172   print("\n--- Part 4: find q_plus, q_minus\n")
173
174   OUT = open("gil_output.txt", "wt")
175   print("idx", "reset", "rvbool", "k", "a", "a-old_a", "max_a-a-k", "end", "counts",
176        "dmax", "dmax2", "dmax2_idx", "extract", file = OUT, sep="\t")
177
178   # mode = ’Full’ to not stop as soon as success is detected and get full diagonal
179   flag, acheck, hash_stats = gil.check(prime_list[0:start], mode = ’Full’)
180   right_diagonal = hash_stats[’right_diagonal’]
181   right_diagonal = gil.make_readable(right_diagonal)
182   hash_output = gil.collect_statistics(right_diagonal)
183
184   start_time = time.perf_counter()
185




                                                       29
186   for k in range(start, nprimes):
187
188      # given previous primes, find possible range for next one to guarantee success
189      # augmenting sequence with previous prime as starting point, seems to always succeeds
190
191      old_a = a
192      old_hash_output = hash_output
193
194      max_a, trials1 = gil.max_gap_allowed(right_diagonal, old_a)
195      min_a, trials2 = gil.min_gap_allowed(right_diagonal, old_a)
196
197      if sequence_type == ’prime_gaps’:
198            a = prime_list[k]
199      else:
200         if sequence_type == ’log_gaps’:
201            # mimic prime growth
202            gap = int(np.log(max_a)) # max_a can be as large as 2a
203         elif sequence_type == ’power_gaps’:
204            gap = int(max_a**0.35) # exponent must be < 1
205         gap = 2 + (gap - gap % 2)
206         a += gap
207
208      arr_k.append(k)
209      arr_min.append(min_a)
210      arr_max.append(max_a)
211      arr_a.append(a)
212      arr_old_a.append(old_a)
213
214      if test_mode:
215         # check if all ’a’ are in [old_a, max_a] succeed, and max_a + 2 fails
216         satisfied, flag = gil.test_conjecture(old_a, max_a, right_diagonal)
217         if not satisfied:
218            conjecture = ’not satisfied’
219
220      old_idx = old_hash_output[’before_02_index’]
221      old_nu_2 = old_hash_output[’nu_2’]
222      success, right_diagonal = gil.augment(right_diagonal, a)
223      right_diagonal = gil.make_readable(right_diagonal)
224      hash_output = gil.collect_statistics(right_diagonal)
225
226      reset   = hash_output[’reset’]
227      counts = hash_output[’counts’]
228      dmax2   = hash_output[’max_value’]
229      dmax2_idx = hash_output[’max_index’]
230      end     = hash_output[’before_02_value’]
231      idx     = hash_output[’before_02_index’]
232      dmax    = hash_output[’max_tail_value’]
233      # ri      = hash_output[’reversal_idx’]
234      # rval    = hash_output[’reversal_value’]
235      rvbool = hash_output[’reversal’]
236
237      if reset:
238         resets_list = (*resets_list, k)
239      if k % 1000 == 0:
240         print("progress:", k, "/", nprimes)
241
242      extract = right_diagonal[1:20]
243      print(old_idx, idx, old_nu_2, reset, rvbool, k, a, a-old_a, max_a-a-k, end, counts,
244           dmax, dmax2, dmax2_idx, extract, file = OUT, sep="\t")
245
246   end_time = time.perf_counter()
247   elapsed_ms = end_time - start_time
248   print(f"Elapsed time: {elapsed_ms:.2f} ms")
249   OUT.close()
250
251   gil.arr_plots(arr_k, arr_min, arr_max, arr_a) # , resets_list)
252
253   # future project: analyse p_n - 2 p_{n-1} + p_{n-2}
254
255
256   #--- 5. Produce trimmed sequences with Sieve of Eratosthenes
257
258   all_primes = False
259   max_period = 20000
260   if all_primes:
261      from primePy import primes



                                                       30
262      # use the first 100k primes
263      moduli = primes.first(100000)
264   else:
265      moduli = (2, 3, 5, 7, 11, 13, 17, 19)
266
267   period = 1
268   for p in moduli:
269      period *= p - 1
270   print("period = ", period)
271   arr_a = [2, 3]
272   start = 4
273   end = min(period + len(moduli), max_period)
274
275   count = 0
276   k = start
277
278   while count < min(end, max_period):
279     keep = True
280     index = 0
281     while keep and index < len(moduli):
282        mod = moduli[index]
283        if k % mod == 0:
284            keep = False
285        index += 1
286     if keep or k in moduli:
287        arr_a.append(k)
288        count += 1
289     k += 1
290     if k % 1000000 == 0:
291        print("/...", k, count)
292
293   print("\n--- Part 5: Sieve of Eratosthenes\n")
294   show_triangle = ’Compact’
295   arr_a_truncated = arr_a[0:max_period]
296   flag, acheck, hash_stats = gil.check(arr_a_truncated, show_triangle)
297
298   # gap combos
299
300   print()
301   hash_gaps = {}
302   nobs = len(arr_a)
303   for k in range(1,nobs):
304      gap = arr_a[k] - arr_a[k-1]
305      block = int(4*k/nobs)
306      if (gap, block) in hash_gaps:
307         hash_gaps[(gap, block)] += 1
308      else:
309         hash_gaps[(gap, block)] = 1
310
311   for gap in range(2, 16, 2):
312      for block in range(4):
313         key = (gap, block)
314         if key in hash_gaps:
315            count = hash_gaps[key]
316         else:
317            count = 0
318         print("Gap combos:", key, count)
319   print("len arr_a", len(arr_a))
320
321
322   #--- 6. Impact of removing/adding one number
323
324   arr_list = [[2, 3, 5, 7, 11, 13],
325            [2, 3, 5, 7, 13],
326            [2, 3, 5, 7, 11, 13, 19],
327            [2, 3, 5, 9, 13, 17, 25, 49, 81, 121, 169, 225, 313],
328            [2, 3, 5, 9, 13, 17, 25, 49, 81, 121, 169, 225, 301, 455, 753, 1347, 2549, 2567, 2999,
                   3439],
329            [2, 3, 5, 9, 13, 11, 15, 9, 7, 11, 21, 25, 27, 21, 13, 17]]
330
331   print("\n--- Part 6: Removing/adding one term\n")
332
333   for arr_a in arr_list:
334      flag, acheck, hash_stats = gil.check(arr_a, show_triangle)
335      print("\n")
336




                                                          31
337
338   #--- 7. Continuous time series: Brownian motion
339
340   rng = np.random.default_rng(45)
341   np.random.seed(45)
342
343   # Generate a single Poisson random variable with lambda (lam) = 4
344   single_val = rng.poisson(lam=4)
345   arr_a = [2, 3]
346   arr_b = [2, 3]
347   a = arr_a[-1]
348   b = arr_a[-1]
349
350   for k in range(2000):
351     sign = np.random.uniform(0, 1)
352     if sign < 0.5:
353        sign = -1
354     else:
355        sign = 1
356        llambda_a = 0.8*np.log(1+k)
357        llambda_b = 0.5*np.log(1+k)
358
359     a = a + 2 * sign * rng.poisson(lam=llambda_a)
360     b = b + 2 * sign * rng.poisson(lam=llambda_b)
361     arr_a.append(a)
362     arr_b.append(b)
363
364   print("\n--- Part 7: Brownian motion\n")
365   show_triangle = ’Compact’
366   flag_a, acheck_a, hash_stats_a = gil.check(arr_a, show_triangle)
367   arr_stats_a = hash_stats_a[’arr_amax’]
368   flag_b, acheck_b, hash_stats_b = gil.check(arr_b, show_triangle)
369   arr_stats_b = hash_stats_b[’arr_amax’]
370
371   arr_k = np.arange(0, len(arr_a), 1)
372   plt.scatter(arr_k, arr_a, linewidth = 0.0, s = 1.6, c= ’red’)
373   plt.scatter(arr_k, arr_b, linewidth = 0.0, s = 1.6, c= ’green’)
374
375   plt.gca().set_facecolor(’black’)
376   plt.show()
377   print(flag_a, len(arr_stats_a), flag_b, len(arr_stats_b))
378
379
380   #--- 8. Continuous time series: Smooth curve
381
382   arr_a = [2, 3, 5, 9, 13, 17]
383   arr_b = [2, 3, 5, 9, 13, 17]
384   a0 = arr_a[-1]
385   b0 = arr_a[-1]
386
387   for k in range(1000):
388      a = a0 + 2*int(38*np.sin(k/21) + 23*np.sin(k/17))
389      b = b0 + 2*int(28*np.sin(k/21) + 23*np.sin(k/17))
390      arr_a.append(a)
391      arr_b.append(b)
392
393   print("\n--- Part 8: Smooth curve\n")
394   show_triangle = ’Compact’
395   flag_a, acheck_a, hash_stats_a = gil.check(arr_a)
396   arr_stats_a = hash_stats_a[’arr_amax’]
397   flag_b, acheck_b, hash_stats_b = gil.check(arr_b)
398   arr_stats_b = hash_stats_b[’arr_amax’]
399
400
401   arr_k = np.arange(0, len(arr_a), 1)
402   plt.scatter(arr_k, arr_a, linewidth = 0.0, s = 3.0, c= ’red’)
403   plt.scatter(arr_k, arr_b, linewidth = 0.0, s = 3.0, c= ’green’)
404   plt.gca().set_facecolor(’black’)
405   plt.show()
406   print(flag_a, len(arr_stats_a), flag_b, len(arr_stats_b))
407
408
409   #--- 9. Build all short sequences with n <= nlevels, sigma in (0, 6, 2)
410
411   left_start = 1
412   nlevels = 5



                                                          32
413
414   parameters = {
415               ’prime’: [1.0, 1.3, 1.50, 5],
416               ’power’: [0.9, 1.1, 1.25, 5, 1.50],
417             }
418
419   model = ’prime’
420
421   hash_count = {}
422   hash_count_valid = {}
423   hash_count_bounded = {}
424   hash_count_smooth = {}
425
426
427   print("\n--- Part 9: Build all short sequences starting from bottom\n")
428   gil.test_primes(parameters)
429   print()
430
431   for seed in range(0, 6, 2):
432      # seed is denored as sigma in the paper
433
434      full_hash = gil.get_all_sequences(seed, nlevels, left_start)
435
436      for first_differences in full_hash:
437
438         level = full_hash[first_differences]
439         key = (seed, level)
440         gil.update_hash(hash_count, key, 1)
441         valid, bounded, smooth, fvals, sequence = gil.admissibility(first_differences, parameters,
                model)
442         if valid:
443             gil.update_hash(hash_count_valid, key, 1)
444
445         if valid and bounded:
446            gil.update_hash(hash_count_bounded, key, 1)
447            if smooth:
448               gil.update_hash(hash_count_smooth, key, 1)
449               if level >= 2:
450                  print("output part 9A", seed, level, sequence)
451
452   for key in hash_count:
453      all = gil.get_hash(hash_count, key)
454      valid = gil.get_hash(hash_count_valid, key)
455      bounded = gil.get_hash(hash_count_bounded, key)
456      smooth = gil.get_hash(hash_count_smooth, key)
457      print("output part 9B:", key, all, valid, bounded, smooth)



      A.2    Gilbreath library
      The code below features the gilbreath lib.lib library, used extensively in the main program in section A.1.
      It is also on GitHub, here.

 1    import numpy as np
 2    import copy
 3
 4    #--- Utils
 5
 6    def make_readable(data, type = "int"):
 7
 8       readable_data = []
 9       for elt in data:
10          if type == "int":
11             readable_data.append(int(elt))
12          elif type == "float":
13             readable_data.append(float(elt))
14       return(readable_data)
15
16
17    def update_hash(hash, key, count):
18       if key in hash:
19          hash[key] += count
20       else:
21          hash[key] = count
22       return(hash)


                                                          33
23
24
25   def get_hash(hash, key):
26      if key in hash:
27         count = hash[key]
28      else:
29         count = 0
30      return(count)
31
32
33   def arr_plots(arr_k, arr_min, arr_max, arr_a, resets_list = ()):
34
35      import matplotlib.pyplot as plt
36      import matplotlib as mpl
37
38      mpl.rcParams[’axes.linewidth’] = 0.5
39      plt.rcParams[’xtick.labelsize’] = 8
40      plt.rcParams[’ytick.labelsize’] = 8
41      plt.rcParams[’legend.fontsize’] = ’x-small’
42
43      arr_k = np.array(arr_k)
44      arr_min = np.array(arr_min)
45      arr_max = np.array(arr_max)
46      arr_a = np.array(arr_a)
47
48      from matplotlib.ticker import FormatStrFormatter
49      from matplotlib.ticker import MaxNLocator
50
51      fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(0.8*9, 0.8*3))
52
53      ax1.yaxis.get_offset_text().set_fontsize(6)
54      ax1.plot(arr_k, arr_min, lw=0.4, color=’lightgreen’)
55      ax1.plot(arr_k, arr_max, lw=0.4, color=’orange’)
56      ax1.plot(arr_k, arr_a, color=’white’, lw = 0.4)
57      for k in resets_list:
58         ax1.axvline(x=k, color=’red’, lw=0.4)
59      ax1.ticklabel_format(style=’sci’, scilimits=(0, 0), axis=’y’, useMathText=True)
60      ax1.yaxis.set_major_locator(MaxNLocator(nbins=5, prune=’lower’))
61      ax1.set_facecolor(’black’)
62      ax1.tick_params(labelsize=6, pad=2, length=2)
63
64      ax2.plot(arr_k, arr_min/arr_a, lw=0.4, color=’lightgreen’)
65      ax2.plot(arr_k, arr_max/arr_a, lw=0.4, color=’orange’)
66      ax2.axhline(y=1.0, color=’white’, lw=0.4)
67      ax2.ticklabel_format(style=’sci’, scilimits=(0, 0), axis=’y’, useMathText=True)
68      ax2.yaxis.set_major_formatter(FormatStrFormatter(’%.1f’))
69      ax2.yaxis.set_major_locator(MaxNLocator(nbins=5, prune=’lower’))
70      ax2.set_facecolor(’black’)
71      ax2.tick_params(labelsize=6, pad=2, length=2)
72      ax2.set_ylim(0.2, 1.8)
73
74      ax3.yaxis.get_offset_text().set_fontsize(6)
75      ax3.plot(arr_k, arr_min-arr_a, lw=0.4, color=’lightgreen’)
76      ax3.plot(arr_k, arr_max-arr_a, lw=0.4, color=’orange’)
77      ax3.axhline(y=0.0, color=’white’, lw=0.4)
78      ax3.ticklabel_format(style=’sci’, scilimits=(0, 0), axis=’y’, useMathText=True)
79      ax3.yaxis.set_major_locator(MaxNLocator(nbins=6, prune=’lower’))
80      ax3.set_facecolor(’black’)
81      ax3.tick_params(labelsize=6, pad=2, length=2)
82
83      plt.tight_layout()
84      plt.subplots_adjust(wspace=0.15)
85      plt.show()
86      return()
87
88
89   #--- banned prime gaps series and simulation
90
91   def banned_gaps_loop(gaps, start):
92
93      val = start
94      seq = (val,)
95      for k in range(0, len(gaps)):
96         val += gaps[k]
97         seq = (*seq, val)
98




                                                      34
99      banned = False
100
101     for modulo in (3, 5, 7, 11, 13):
102        hash_residues = {}
103        for val in seq:
104           residue = val % modulo
105           update_hash(hash_residues, residue, 1)
106
107         if len(hash_residues) == modulo:
108            banned = True
109            break
110
111     return(banned)
112
113
114   def banned_gaps(gaps):
115
116     banned = True
117     for start in (2, 4, 6, 8, 10, 12):
118        banned_start = banned_gaps_loop(gaps, start)
119        if not banned_start:
120           banned = False
121           break
122     return(banned)
123
124
125   def banned_found_in_seq(first_diff_seq):
126
127     banned_found = False
128     banned_pattern = ()
129
130     for size in (2, 3, 4, 5, 6, 7):
131        for k in range(len(first_diff_seq)-size):
132           gaps = ()
133           for j in range(size):
134              gaps = (*gaps, first_diff_seq[k+j])
135           banned = banned_gaps(gaps)
136           if banned:
137              banned_found = True
138              banned_pattern = gaps
139              break
140        if banned_found:
141           break
142     return(banned_found, banned_pattern)
143
144
145   def generate_random_sequence(n, arr_init, llambda, parameters, model, rng, rejection_sampling =
          True):
146
147      # the generated sequence is guaranteed to be valid (no duplicates)
148
149      q = arr_init[-1]
150      arr_a = np.copy(arr_init)
151      sum = np.sum(arr_a)
152      offset = len(arr_init)
153
154      for k in range(n):
155
156         ccontinue = True
157
158         while ccontinue:
159            # until in corridor
160
161            u = 2 + 2*rng.poisson(lam=llambda) # try increasing llambda
162            new_q = q + u
163            current_n = offset + k + 1
164
165            admissible = admissibility_local(q, new_q, sum, current_n, parameters, model)
166            if admissible or not rejection_sampling:
167               ccontinue = False
168
169         q += u
170         arr_a = np.append(arr_a, q)
171
172      return(arr_a)
173




                                                       35
174
175   #--- get canonical form of sequence arr_a
176
177   def canonical(s1, n_levels, fail_level = {}, valid = False, threshold = 1.0):
178
179      # s1 is in the input sequence
180      # s2 is the canonical form of s1 if nor failures added during construction
181      # fail_level = {} for no failure
182      # fail_level = {23:3, 41:5} to build fails at level 23, 41 resp. with 3, 5 instead of 1 (1 = no
             fail)
183
184      arr_a = np.copy(s1)
185      np.random.seed(66)
186      n = len(arr_a)
187      arr_p =[-1]
188
189      for level in range(1, n_levels+1, 1):
190
191         arr1 = np.copy(arr_a)
192         arr_a = []
193         cnt = 0
194         for k in range(len(arr1) - 1):
195            a = abs(arr1[k+1] - arr1[k])
196            arr_a.append(a)
197            if arr_a[k] < arr1[k]:
198               cnt += 1
199         arr_a = make_readable(arr_a)
200         p = cnt / len(arr_a)
201         arr_p.append(p)
202         if level == 1:
203            s1_max_gap = np.max(arr_a)
204
205      s1_bottom = np.copy(arr_a)
206
207      for level in range(n_levels-1, -1, -1):
208
209         # "reduced" primes is last arr_a produced (after adding 1)
210
211         arr1 = np.copy(arr_a)
212         if level in fail_level:
213            fail_value = fail_level[level]
214            arr_a = [fail_value]
215         else:
216            arr_a = [1]
217
218         for k in range(1, len(arr1)+1):
219
220            a1 = arr_a[k-1] + arr1[k-1]
221            a2 = arr_a[k-1] - arr1[k-1]
222            if a2 < 0:
223               a = a1
224            else:
225               u = np.random.uniform(0,1)
226               # random choice
227               if u < threshold: # try u < arr_p[level]
228                  a = a2
229               else:
230                  a = a1
231            if valid:
232               if level == 0:
233                  # make sure next prime is not less than previous prime
234                  a = a1
235               elif level == 1:
236                  # make sure next prime is bigger than previous one
237                  if a2 == 0:
238                      a = a1
239            arr_a.append(a)
240
241         arr_a = make_readable(arr_a)
242         if level == 1:
243            s2_gaps = np.copy(arr_a)
244
245      for k in range(len(arr_a)):
246         arr_a[k] += 1
247      s2 = np.copy(arr_a)
248      s1_proba = make_readable(arr_p, type = "float")



                                                       36
249
250      return(s2, s2_gaps, s1_bottom, s1_max_gap, s1_proba)
251
252
253   #--- find bounds for next prime
254
255   def augment(right_diagonal, a):
256
257      new_diagonal = [a,]
258      val = a
259      success = False
260      for j in range(len(right_diagonal)):
261         next = abs(val - right_diagonal[j])
262         new_diagonal.append(next)
263         val = next
264      if val == 1:
265         success = True
266      return(success, new_diagonal)
267
268
269   def max_gap_allowed(right_diagonal, a):
270
271      lower = a
272      upper = 2*a + 1
273      found = False
274      trials = 0
275
276      while not found:
277         trials += 1
278         b = (upper + lower) // 2
279         if b % 2 == 0:
280            b += 1
281         success, new_diagonal = augment(right_diagonal, b)
282         if success:
283            lower = b
284         else:
285            upper = b
286         if upper - lower == 2 or trials > 28:
287            found = True
288
289      return(b, trials)
290
291
292   def min_gap_allowed(right_diagonal, a):
293
294      lower = 1
295      upper = a
296      found = False
297      trials = 0
298
299      while not found:
300         trials += 1
301         b = (upper + lower) // 2
302         if b % 2 == 0:
303            b += 1
304         success, new_diagonal = augment(right_diagonal, b)
305         if success:
306            upper = b
307         else:
308            lower = b
309         if upper - lower == 2 or trials > 280:
310            found = True
311
312      return(b, trials)
313
314
315   def test_conjecture(old_a, max_a, right_diagonal):
316
317      satisfied = True
318      flag = ’no issue’
319
320      # at ’a = max + 2’, we must fail, it’s above the max limit
321      success1, test_diagonal = augment(right_diagonal, max_a + 2)
322      success1 = bool(not success1)
323
324      if success1:



                                                       37
325         # check values below max_a; they must all succeed
326         for a in range(old_a, max_a, 2):
327            success2, test_diagonal = augment(right_diagonal, a)
328            if not success2:
329               flag = (old_a, a, max_a)
330               satisfied = False
331               break
332      else:
333         flag = ’a_max + 2 succeeds, not supposed to’
334         satisfied = False
335      return(satisfied, flag)
336
337
338   def collect_statistics(right_diagonal):
339
340      length = len(right_diagonal)
341      idx = -1
342      idx2 = -1
343      end = -1
344      reversal_idx = - 1
345      reversal_value = -1
346      reversal = False
347      reset = False
348      hash_output = {}
349
350      for kx in range(length-1, 0, -1):
351         if right_diagonal[kx] > 2:
352            idx = kx
353            end = right_diagonal[kx]
354            break
355      if idx == -1:
356         reset = True
357
358      dmax2 = np.max(right_diagonal[1:])
359      for kx in range(length-1, 0, -1):
360         if right_diagonal[kx] == dmax2:
361            dmax2_idx = kx
362            break
363
364      for kx in range(len(right_diagonal[1:])):
365         d1 = right_diagonal[kx]
366         d2 = right_diagonal[kx+1]
367         if d2 >= d1 and d2 > 2:
368            reversal_idx = kx + 1
369            reversal_value = d2
370            reversal = True
371            break
372
373      # dmax is maximum value after the first log(length)
374      start = int(np.log(length))
375      dmax = np.max(right_diagonal[start:])
376
377      counts = ()
378      for kx in (0, 2):
379         counts = (*counts, right_diagonal.count(kx))
380
381      arr_cycle02 =right_diagonal[idx+1:-2]
382      nu_2 = arr_cycle02.count(2)
383
384      hash_output[’reset’] = reset
385      hash_output[’counts’] = counts
386      hash_output[’max_value’] = dmax2
387      hash_output[’max_index’] = dmax2_idx
388      hash_output[’before_02_value’] = end
389      hash_output[’before_02_index’] = idx
390      hash_output[’max_tail_value’] = dmax
391      hash_output[’reversal_idx’] = reversal_idx
392      hash_output[’reversal_value’] = reversal_value
393      hash_output[’reversal’] = reversal
394      hash_output[’nu_2’] = nu_2
395
396      return(hash_output)
397
398
399   #--- Main function
400




                                                          38
401   def check(arr_a, show_triangle = ’None’, mode = ’Fast’, delta = ’standard’):
402
403      hash_stats = {}
404      right_diagonal = []
405      left_diagonal = []
406      arr_amax = []
407      right_diagonal.append(arr_a[-1])
408      arr1 = np.copy(arr_a)
409      arr1 = np.array(arr1).astype(int)
410      if show_triangle in (’Full’,):
411         print("Sequence:", arr_a)
412      imax = len(arr_a) - 1
413      flag = ’Success’
414      level = 0
415      failing_level = -1
416
417      for k in range(imax, 0, -1):
418
419         level += 1
420         arr2 = np.zeros(k)
421         for j in range(k):
422            if delta == ’standard’:
423               arr2[j] = abs(arr1[j+1] - arr1[j])
424            elif delta == ’light’:
425               arr2[j] = max(abs(arr1[j+1] - arr1[j]), 1)
426         if k == imax:
427            first_diff = np.copy(arr2)
428         right_diagonal.append(arr2[-1])
429         left_diagonal.append(arr2[0])
430
431         amax = np.max(arr2)
432         first_amax_idx = 1 + np.argmax(arr2 == amax)
433         first_amax_val = int(arr1[first_amax_idx - 1])
434         amax = int(amax)
435         arr1 = np.copy(arr2)
436         arr1 = np.array(arr1).astype(int)
437
438         count = np.count_nonzero(arr1 == amax)
439         arr_amax.append([level, amax, count])
440         if arr1[0] != 1:
441            flag = ’Fail’
442            failing_level = level
443            if not mode == ’Full’:
444               break
445         if show_triangle == ’Compact’:
446            print("Level",level,"|amax=",amax,"|idx=",first_amax_idx,"|val=",first_amax_val,"|count=",count)
447         elif show_triangle == ’Full’:
448            print("Level",level,"|amax=",amax,"|idx=",first_amax_idx,"|val=",first_amax_val,arr1)
449         if amax == 2:
450            flag = ’Success’
451            if mode == ’Fast’:
452               break
453
454      right_diagonal = np.array(right_diagonal).astype(int)
455      left_diagonal = np.array(left_diagonal).astype(int)
456      first_diff = np.array(first_diff).astype(int)
457
458      hash_stats[’arr_amax’] = arr_amax
459      hash_stats[’first_diff’] = first_diff
460      hash_stats[’right_diagonal’] = right_diagonal
461      hash_stats[’left_diagonal’] = left_diagonal
462      hash_stats[’failing_level’] = failing_level
463
464      return(flag, first_amax_idx, hash_stats)
465
466
467   def admissibility_local(q, proposed_next_q, sum, n, parameters, model):
468
469      # testing a new value; assumes it is admissible prior to that
470
471      constants = parameters[model]
472      lower_constant = constants[0]
473      upper_constant = constants[1]
474      smooth_constant = constants[2]
475
476      old_sum = sum



                                                         39
477     sum += proposed_next_q
478
479     if model == ’power’:
480        exponent = constants[4]
481        growth = n**exponent
482     elif model == ’prime’:
483        growth = n*np.log(n)
484     lower = lower_constant * growth
485     upper = upper_constant * growth
486
487     pass_test1 = bool(lower < proposed_next_q < upper)
488     pass_test2 = bool(proposed_next_q < smooth_constant * q)
489
490      if pass_test1 and pass_test2:
491         admissible = True
492      else:
493         admissible = False
494      return(admissible)
495
496
497   def admissibility(first_differences, parameters, model):
498
499      # check if sequence is in corridor; test the whole sequence
500      # n = index of first failure
501      # fvals = (n lower bound, observed value, upper bound) if failing bound test
502      # fvals = (n, observed value, max allowed given past value) if failing smooth test
503
504      valid = True
505      bounded = True
506      smooth = True
507      fvals = ()
508
509      if 0 in first_differences:
510
511         valid = False
512         sequence = ()
513
514      else:
515
516         constants = parameters[model]
517         lower_constant = constants[0]
518         upper_constant = constants[1]
519         smooth_constant = constants[2]
520         offset = constants[3]
521
522         sum = 2
523         sequence = (sum,)
524         n = 1
525
526         for value in first_differences:
527
528              n += 1
529              old_sum = sum
530              sum += value
531              if model == ’power’:
532                 exponent = constants[4]
533                 growth = n**exponent
534              elif model == ’prime’:
535                 growth = n*np.log(n)
536              lower = lower_constant * growth
537              upper = upper_constant * growth
538
539              pass_test1 = bool(lower < sum < upper)
540              if not pass_test1 and n > offset:
541                 bounded = False
542                 if len(fvals) == 0:
543                    fvals = (n, lower, sum, upper)
544              pass_test2 = bool(sum < smooth_constant * old_sum)
545              if not pass_test2 and n > offset:
546                 smooth = False
547                 if len(fvals) == 0:
548                    fvals = (n, lower, smooth_constant * old_sum)
549              sequence = (*sequence, sum)
550
551     return(valid, bounded, smooth, fvals, sequence)
552




                                                         40
553
554   def test_primes(parameters):
555
556      # check if prime number sequence (first 1000 primes) is in corridor
557      from primePy import primes
558      prime_list = primes.first(1000)
559      # prime_list = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)
560
561      model = ’prime’
562      first_differences = ()
563      for k in range(len(prime_list) - 1):
564         delta = prime_list[k+1] - prime_list[k]
565         first_differences = (*first_differences, delta)
566      valid, bounded, smooth, fvals, sequence = admissibility(first_differences, parameters, model)
567      print("Testing prime sequence: bounded = %s | smooth = %s " %(bounded, smooth))
568      return()
569
570
571   def integrate(x, left_start = 1):
572
573      # find all sequences y one level above x such that diff(y) = x
574
575      y = (left_start,)
576      list2 = (y,)
577
578      for k in range(1, 1+len(x)):
579
580         list3 = () # used to be {}
581
582         for y in list2:
583
584            # we must have if len(y) == k:
585
586            y_k_plus = y[k-1] + x[k-1]
587            new_y_plus = (*y, y_k_plus)
588            list3 = (*list3, new_y_plus)
589
590            if x[k-1] !=0:
591               y_k_minus = y[k-1] - x[k-1]
592               if y_k_minus >= 0:
593                  new_y_minus = (*y, y_k_minus)
594                  list3 = (*list3, new_y_minus)
595
596         list2 = copy.deepcopy(list3)
597
598      return(list2)
599
600
601   def get_all_sequences(seed, nlevels, left_start = 1):
602
603      hash_arr = { (left_start, seed):1 }
604      full_hash = {}
605
606      for level in range(nlevels):
607
608         hash3 = {}
609         count = len(hash_arr)
610         sub_count = 0
611
612         for arr1 in hash_arr:
613
614            if sub_count % 100 == 0 and sub_count > 0:
615               print("GBL Progress",seed, level, sub_count,"/", count)
616            sub_count += 1
617            local_list = integrate(arr1, left_start)
618
619            # Add the collected local_lists to list2
620            for arr2 in local_list:
621               hash3[arr2] = level + 1
622
623         hash_arr = hash3.copy()
624         full_hash.update(hash_arr)
625
626      return(full_hash)




                                                          41
