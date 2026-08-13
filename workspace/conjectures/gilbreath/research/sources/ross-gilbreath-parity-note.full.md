<!-- source: https://michaelmross.github.io/gilbreath-parity-note.html | converted from HTML -->

Is Gilbreath’s Conjecture Garden-Variety Numerology?

It is often observed that Gilbreath’s conjecture is “really” a fact about parity rather than about primes. If you start any suitable sequence with 2 and follow it with odd numbers, the difference pyramid seems to funnel down to 1. The observation is illuminating, and the question in the title deserves a precise answer. It turns out the answer is: half yes, half no — and locating the boundary between the two halves is where the interesting arithmetic lives.

## §1 The trivial half: the leading term is odd

Start with the number 2 followed by odd numbers, and take iterated absolute forward differences. The first difference row has the shape (odd, even, even, …): the single odd entry on the left is |3 − 2| = 1, and everything to its right is |odd − odd| = even. The induction is then airtight: if a row has the shape (odd, even, even, …), the next row’s leading entry is |even − odd| = odd and every other entry is |even − even| = even, so the shape persists.

Proposition (parity wave)

For any sequence beginning 2, odd, odd, odd, …, the leading term of every row of iterated absolute differences is odd.

That is a genuine theorem, it is elementary, and it has nothing to do with primes. Substituting a random ascending odd sequence for the primes demonstrates it directly — this is the sense in which the “numerology” observation is exactly right.

## §2 Odd is not 1

Notice, however, what the proposition proves: *odd*, not *1*. The content of Gilbreath’s conjecture is precisely the step from “odd” to “exactly 1,” and parity alone says nothing about that step. Two small examples make the distinction concrete. The sequence 2, 3, 13 gives rows (1, 10), then (9) — a leading term of 9: odd, but not 1. And a pyramid built on every sixth prime (2, 17, 41, 67, …, taken to 13 terms) has leading column 2, 15, 9, 7, 5, 3, 1, 1, 1, 1, 1, 7, 3 — parity intact throughout, while the collapse to 1 comes and goes. So the parity mechanism, by itself, guarantees only that such a pyramid funnels to *some odd number*; whether that number is 1 is a further question.

## §3 The second mechanism: the {0, 2} regime

What forces the odd number to be 1 is a separate, self-perpetuating structure. The set {0, 2} is closed under absolute differencing (|0 − 2| = 2, |2 − 2| = 0, |0 − 0| = 0), and a leading 1 against a 0 or a 2 stays 1 (|1 − 0| = |1 − 2| = 1). Once a row of the form (1, then a long run of 0s and 2s) appears, the 1 is locked in for as many rows as the run is long. Gilbreath’s conjecture is really the claim that the prime pyramid *reaches and indefinitely sustains*that regime. This is what Odlyzko verified computationally — for the first 3.4 × 10 11 rows [3] — and it is not a parity fact.

The same closure property, though, cuts both ways. {0, *d*} is closed under differencing for every *d*≥ 2, so the mechanism that pins the 1 in place when *d*= 2 is also the mechanism that could preserve a large disturbance when *d*is large. That double edge is the crux of §5.

## §4 A side-by-side comparison

Placing the prime pyramid next to a random-odd pyramid of comparable scale is instructive — and what the comparison reveals most clearly is how the two pyramids *differ*. Below, odd entries are set in red; entries in the pinned {0, 2} regime are set in green.

```
```

odd (the parity wave) 0 or 2 (pinned regime) other even

Fig. 1 — The first 20 primes. The second row is already (1, then small evens); by the third row nearly everything to the right of the wall is 0s and 2s. The 1 is pinned immediately and permanently.

```
```

Fig. 2 — The sequence 2 followed by 19 ascending odd numbers below 100, chosen to match the primes in range (99 vs. 71), mean gap (5.1 vs. 3.6), and maximum gap (8 vs. 6). Even so, the left edge wanders: 1, 7, 7, 3, 3 before reaching 1 in row 6. Parity guarantees it stays odd; nothing guaranteed it would reach 1 before the triangle ran out.

The leading columns tell the whole story at a glance:

first 20 primes

1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

random odd sequence

1 7 7 3 3 1 1 1 1 1 1 1 1 1 1 1 1 1 1

The comparison is deliberately scale-matched — the odd sequence stays below 100, with mean gap 5.1 against the primes’ 3.6 — so the contrast cannot be blamed on exaggerated gaps. Even so, the transient 7, 7, 3, 3 appears, and its origin is exact rather than statistical: the leading entry at row *r*depends only on the first *r*+ 1 terms, so the transient is the light-cone image of the two gaps of 8 sitting beside the wall (|8 − 1| = 7), and its decay is decided entirely within the first five columns. The primes never wander for the same local reason: their second gap is 2, so the wall reads |2 − 1| = 1 immediately, and every later step pits the 1 against a small even. The every-sixth-prime example shows the recovery can also fail within the available rows.

The bottom of the matched pyramid teaches a second lesson. Its quasi-arithmetic regularity — gap runs 4, 4 and 6, 6, 6 — synchronizes the interior into a perfectly alternating row 0, 2, 0, 2, … by row 12, which collapses to all 2s, then all 0s, frozen to the apex: a miniature of exactly the rigid two-valued blocks of §5. Here the block is harmless because its neighbor is the 1; beside any larger value, the same structure would preserve that value instead. The primes’ tail, by contrast, keeps an aperiodic 0/2 texture to the last row — irregular enough to avoid both the transient’s cause and the freeze. Gilbreath’s conjecture asserts that this holds for *every*row, forever.

## §5 Where the actual difficulty lives

It is tempting to say that the hard half reduces to a single arithmetic input — that a Cramér-type bound on prime gaps, *p**n*+1 − *p**n*≪ log²*n*, would settle the matter. It would not. Such a bound controls only the *size*of the entries in the top row; it says nothing about their *arrangement*, and arrangement is what governs whether the pyramid decays. Eppstein’s anti-Gilbreath sequences [4] make this concrete: one can have small, slowly growing gaps and still fail.

The obstruction is that certain patterns refuse to shrink. The set {0, *d*} is closed under absolute differencing for *every**d*≥ 2, not just *d*= 2 — so a long block taking only the values 0 and *d*propagates downward at undiminished amplitude, and a long block of pure zeroes likewise props up whatever sits beside it. Chase, Hunter and Tao [6] prove this intuition is essentially the whole story: assuming Cramér-type gap bounds, their deterministic inverse theorem shows that *the only*obstructions to the array collapsing are long zero blocks and long shallow {0, *d*}-valued blocks. Ruling those out for the primes appears difficult even under strong conjectures such as Hardy–Littlewood.

This also sharpens Croft’s observation (recorded by Guy [4]): the phenomenon was never about primality per se — but the correct hypothesis on a general sequence is not merely “gaps grow slowly.” It is that the gaps do not *concentrate in an arithmetically rigid set*. The precise notion is 2-separation: a set of integers containing no two consecutive values, such as the evens or the multiples of 3. If the gaps were trapped in such a set, the whole array would be trapped with them, and the collapse to 1 could genuinely fail.

## §6 The state of the art

The randomized versions of the conjecture are now theorems. Chase [7] proved it for uniformly distributed initial data of slowly growing range, and Chase–Hunter–Tao [6] proved it for the Cramér random model — where normalized prime gaps are replaced by independent geometric variables of logarithmic size — and, more generally, for any independent model whose entries neither grow linearly nor concentrate in a 2-separated set. So Gilbreath’s conjecture is exactly what one expects of a “random” sequence with prime-like gap statistics; what is missing is any handle on the primes’ actual arrangement.

Even the averaged decay rate remains stubborn. For exponential initial data, let *c i*be the expected value of an entry at depth *i*. One might guess exponential decay; in fact Chase–Hunter–Tao show Σ*i*≤*n**c i*≥ log(*n*+ *e*), so *c i*cannot decay faster than 1/*i*— and the sequence is not even monotone, its irregularity apparently tied to the count of odd entries in rows of Pascal’s triangle. They can prove neither that *c i*tends to zero nor even that it stays bounded. The rate at which a Gilbreath array grinds itself down is, remarkably, still an open question.

Answer

Half yes, half no. The *parity wave*— leading term stays odd, right side drains to evens — is garden-variety in the best sense: elementary, fully understood, and independent of primality. The *pinning to exactly 1*is a claim that the array never harbors a long zero block or a long shallow {0, *d*}-valued block, and it is open even granting strong conjectures on prime gaps. The two are easy to conflate because the pyramid displays them together, but “odd” and “1” are different statements — and the conjecture lives in the space between them.

## References

1. N. L. Gilbreath (1958); see M. Gardner, *Patterns in primes are a clue to the strong law of small numbers*, Sci. Amer. **243**(Dec. 1980), 18–28.
2. A. M. Odlyzko, *Iterated absolute values of differences of consecutive primes*, Math. Comp. **61**(1993), 373–380.
3. R. K. Guy, *Unsolved Problems in Number Theory*, 2nd ed., §A10, Springer, 1994.
4. D. Eppstein, *Anti-Gilbreath sequences*, [11011110.github.io/blog][1], 2011.
5. Z. Chase, Z. Hunter, T. Tao, *Gilbreath’s conjecture: a Cramér random model and a deterministic analysis*, [arXiv:2607.08712][2], July 2026.
6. Z. Chase, *A random analogue of Gilbreath’s conjecture*, Math. Ann. **388**(2024), 2611–2625.
7. M. M. Ross, *Empirical Structure of the Gilbreath Decay Constants*, [zenodo.21326025][3], July 2026.
8. T. Tao, *Gilbreath decay constants*, [Interactive web application][4], (accessed July 20, 2026).


## Links

[1]: https://11011110.github.io/blog/2011/02/20/anti-gilbreath-sequences.html
[2]: https://arxiv.org/abs/2607.08712
[3]: https://doi.org/10.5281/zenodo.21326025
[4]: https://teorth.github.io/tao-web/apps/gilbreath-cn.html
