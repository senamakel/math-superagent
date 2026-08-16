# A342810 — traced and rejected as a lead (red herring)

Source traced: https://arxiv.org/abs/2106.05866 (Rüdiger Jehn, Kester Habermann,
"Properties of terms of OEIS A342810", 2021). Appeared in
`derived/FRONTIER.md` under a search for the multi-block split-and-sum problem.

**What A342810 actually is.** OEIS A342810 = numbers x that divide the smallest
positive integer whose *digit sum* equals x. E.g. 27 divides 999, the smallest
number with digit sum 27, so 27 is a term. The paper's structural results are
all about digit-sum divisibility and the multiplicative order of 10 modulo
prime factors of terms of the form 3^m·y.

**Why it is NOT relevant to PE 719.** The S-number rule is about *splitting the
digit string of a perfect square into contiguous blocks that sum to the root*
— a partition-of-the-decimal-string property. A342810 is about a number
dividing the smallest integer with a given *whole* digit sum. The two share
only the words "sum of digits" and do not interact: neither the terms nor the
structure carry over to split-and-sum S-numbers. The OEIS lookup for the
S-number terms 0,1,81,100,1296,2025,3025,6724,8281,9801,10000 matches only
A104113 (already in the library), confirming A342810 is not the S-number
sequence.

**Do not re-fetch.** A dead lead. The library holds everything relevant:
A104113/A038206 (the S-numbers and roots, arbitrary blocks), A102766/A006886
(the two-block subcase), Iannucci (two-block parametrisation), Dudeney/Javaheri
(torn numbers), ProofWiki (single-block digit-sum bound 0,1,81), and
Butler–Graham–Stong (partition-sum mod-(b−1) invariance, the structural root of
the mod-9 filter).
