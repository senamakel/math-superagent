# Verification of Mignosi 1991 totient formula claim (hand-checked, exact)

Claim `mignosi-1991-sturmian-language-count` (note:
`research/summaries/mignosi-number-factors-sturmian-1991.md`): for m≥1,
card(A_m) = 1 + Σ_{i=1}^{m} (m−i+1) φ(i), where A_m is the set of length-m
factors occurring in *any* Sturmian word (the finite Sturmian language) and
φ is Euler's totient.

## Hand-check for m = 1..4 (exact)

Euler's totient: φ(1)=1, φ(2)=1, φ(3)=2, φ(4)=2.

m=1: 1 + (1−1+1)φ(1) = 1 + 1·1 = **2**.
  Length-1 balanced binary words: {a, b}. Count 2 ✓.
m=2: 1 + 2φ(1) + 1φ(2) = 1 + 2 + 1 = **4**.
  All four length-2 binary words (00,01,10,11) are balanced: their only
  length-2 factor is the word itself and the length-1 factors are the letters
  {0,1} with counts 0,1 (diff 1). Count 4 ✓.
m=3: 1 + 3φ(1) + 2φ(2) + 1φ(3) = 1 + 3 + 2 + 2 = **8**.
  Every length-3 binary word is balanced: length-2 factor ones-counts are
  consecutive-pair sums which differ by at most 1 in any binary word of
  length 3 (pair sums of 0/1 triple: 0,0,1,1,2 — any two adjacent-position
  pairs differ by ≤1; length-1 counts 0 vs 1). Count 8 ✓.
m=4: 1 + 4φ(1) + 3φ(2) + 2φ(3) + 1φ(4) = 1 + 4 + 3 + 4 + 2 = **14**.
  Of the 16 length-4 binary words, exactly 0011 and 1100 are unbalanced
  (their length-2 factor ones-counts are 0,1,2 — diff 2). All others are
  balanced, e.g. 0101 (pairs 1,1,1), 0110 (1,2,1), 1001 (1,0,1). Count
  16 − 2 = 14 ✓.

## Verdict

The totient formula is CONFIRMED for m = 1..4 by direct balanced-word
counting. (Balanced binary words = factors of Sturmian words is a standard
equivalence — Glen–Justin survey §7, Lothaire C2, all held.)

## Holds-here: no — confirmed correct classification

PE1006's F_k is the factor set of the *single* Fibonacci word, which has
exactly k+1 elements (verified by brute oracle: counts.txt k=1..20,
`code/out/brute_oracle_results.md`). A_m is the union over *all* Sturmian
words and is a strictly larger object (2, 4, 8, 14 vs 2, 3, 4, 5 for the
single word). The claim's `holds-here: no` is the right verdict: this
formula is the canonical enumeration of the finite Sturmian language, not
of PE1006's factor set.

Recorded 2026-08-20 by scholar digest cycle (memory server down).
