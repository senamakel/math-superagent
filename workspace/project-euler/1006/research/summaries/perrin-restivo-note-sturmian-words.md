# Perrin & Restivo — *A note on Sturmian words* (TCS 2012)

Source: https://hal.science/hal-00828351/file/noteSturmianWords.pdf
Full text: [[perrin-restivo-note-sturmian-words.full]]

## What this source establishes

**Definitions it fixes.**
- An infinite word over a binary alphabet is **Sturmian** iff it has exactly
  n+1 factors of length n for every n ≥ 1. (Section 2; this is the classical,
  complexity-based definition.)
- A finite word is Sturmian iff it is a factor of an infinite Sturmian word.
- A factor u of s is **right special** if u·0 and u·1 are both factors; every
  Sturmian word has exactly one right-special factor of each length.
- A set of words is **balanced** if any two words of equal length have counts
  of the letter b differing by at most 1; the length-n factors of a Sturmian
  word form a balanced set.
- **Mechanical word:** for 0 ≤ α ≤ 1 and intercept ρ, the *lower mechanical
  word* is s_{α,ρ}(n) = ⌊(n+1)α+ρ⌋ − ⌊nα+ρ⌋; the upper is the same with ⌈·⌉.
  α is the slope. Note the digit is a **height difference over one step**, which
  is how a mechanical word encodes a rotation (Perrin Lecture 2: s_{α,ρ}(n) = 0
  iff {nα+ρ} ∈ [0,1−α)).

**Theorem 1 (Sturmian ⟺ mechanical of irrational slope).** An infinite word s
is Sturmian iff it is a mechanical word of irrational slope. The slope α is
unique. (Lothaire ACW Thm 2.1.13, cited [8].)

**Characteristic word.** c_α := (s_{α,0} with the first letter, which is 0,
deleted) = s_{α,1−α}. The Fibonacci word *is* a characteristic word:

> Example 2: "The Fibonacci word is the characteristic word of slope α = 2/(3+√5)."

with the a/b alphabet relabelled (a↔0, b↔1). 2/(3+√5) = (3−√5)/2 = 1/φ² ≈
0.38197. The problem's word S (digits 0/1) is exactly this characteristic word
c_α = 010010100… (verified: the problem's S_4 = 01001010 is the length-8
prefix of c_α).

**Balance criterion (Prop 1).** w ∈ F(s) iff every factor u of w satisfies
|u|_b − 1 < α|u| < |u|_b + 1 — the digitised-line height bound.

**Standard words & the convergents (Ex. 4, 5, eq. (4)).** For slope α with
continued fraction [0;1+d₁,d₂,…], the standard sequence s_{−1}=b, s_0=a,
s_n = s_{n−1}^{d_n} s_{n−2} has |s_n|_b = p_n, |s_n| = q_n (convergents). The
directive sequence (1,1,1,…) gives the Fibonacci words, whose slopes are the
convergents of α. These are the mechanical-word rational approximants the
solver needs (F(n-2)/F(n) → 1/φ²).

**Consecutive factors (Theorem 2).** Two equal-length factors u < v of a
Sturmian set are lexicographically consecutive iff u = r·a·b·s, v = r·b·a·s
(or u = ra, v = rb). Purely a structure statement; not needed for the floor-sum
computation but confirms the factor set has the standard "one letter differs"
lattice structure.

## What it implies for PE1006

1. The problem's "only k+1 Fibonacci subwords of length k" is the factor-
   complexity definition of Sturmian, so the count is guaranteed — no
   enumeration needed (this already matches the brute oracle at k=1..20).
2. **Slope correction (contradicts directive 2's literal wording):** the
   Fibonacci word is characteristic of α = 2/(3+√5) = 1/φ², NOT of 1/φ ≈ 0.618.
   The factor set of S is the factor set of c_α with the mechanical digit rule
   at slope 1/φ²; a mechanical word of slope 1/φ (consecutive-Fibonacci ratio)
   is the *complement word* with 0↔1 swapped, which has a different factor set
   (exact-arithmetic check at k=3: 34/89 gives {001,010,100,101} = the problem's
   oracle; 55/89 gives {010,011,101,110} ≠ oracle). The run must use slope
   F(n-2)/F(n) → 1/φ².
3. The mechanical digit formula s_{α,ρ}(n) = ⌊(n+1)α+ρ⌋ − ⌊nα+ρ⌋ is the exact
   digit rule directive 2 needs, with intercept ρ the arc midpoint; all
   arithmetic is exact once α is the rational F(n-2)/F(n).

## Claims anchored here

`governing-sturmian`, `governing-factor-complexity`, `mechanical-word-digit-rule`
(in `research/notes/sourced-claims-governing-theory.md`).

## What it does NOT establish

- No statement about sums of squares of the factors interpreted as decimals —
  Ψ(k) is entirely this run's computation.
- No statement about computing Ψ via floor sums in O(log); that is the
  universal-Euclidean claim, anchored elsewhere.