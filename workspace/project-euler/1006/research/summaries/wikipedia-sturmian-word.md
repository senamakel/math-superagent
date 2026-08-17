# Wikipedia — *Sturmian word*

Source: https://en.wikipedia.org/wiki/Sturmian_word
Full text: [[wikipedia-sturmian-word.full]]

## What this source establishes

The encyclopedic tier for the governing theory. Key facts for this run
(verified against the full text's structure: "Sequences of low complexity",
"Balanced sequences", "Cutting sequence of irrational", "Difference of Beatty
sequences", "Coding of irrational rotation", "Slope and intercept"):

- **Sturmian = minimal complexity over a binary alphabet:** a Sturmian word is
  an infinite word with exactly n+1 distinct factors of length n for every n
  (aperiodic words of minimal complexity). This is the exact statement the
  problem's "only k+1 different Fibonacci subwords of length k" is an instance
  of.
- **Sturmian ⟺ balanced and aperiodic.**
- **Mechanical/Billiard forms:** a Sturmian word is (i) the coding of an
  irrational rotation (difference of Beatty sequences: s_n = ⌊(n+1)α+ρ⌋ − ⌊nα+ρ⌋
  or the ceiling variant), (ii) a cutting/billiard sequence of an irrational
  line of slope α.
- **Slope and intercept:** the slope α ∈ (0,1) is the frequency of ones; the
  intercept ρ fixes which of the same-slope words it is. Same slope ⇒ same
  factor set.
- **Complexity:** every Sturmian word's complexity function is n+1.

## What it implies for PE1006

1. The k+1 count is the *defining* property of the class the Fibonacci word
   belongs to; all the mechanical-word machinery (floor-difference digits,
   rotation coding, factor/intercept correspondence) applies.
2. The "slope = frequency of ones" convention is the one to watch: the
   problem's word has ones-frequency 1/φ² ≈ 0.382 (Perrin–Restivo: slope
   2/(3+√5)). Any source stating "the Fibonacci word has slope 1/φ" (Wikipedia
   Fibonacci-word article) means the complementary (rabbit) convention — see
   the contradiction note in `wikipedia-fibonacci-word.md`. The mechanical
   digit rule must use α = 1/φ² for the problem's word.
3. The factor set is a function of slope only (not intercept), which is why the
   arc-midpoint intercept choice in directive 2 is legitimate: any choice of
   k+1 distinct intercepts — most cleanly the k+1 arc midpoints of the circle
   cut at points {−mα} — yields the full factor set.

## Claims anchored here

Corroborates `governing-sturmian` and `governing-factor-complexity`.

## What it does NOT establish

- No Psi-specific facts; no evaluation algorithm.
- No statement about the *decimal interpretation* of factors.