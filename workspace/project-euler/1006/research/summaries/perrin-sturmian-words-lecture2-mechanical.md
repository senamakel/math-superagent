# Perrin — *Sturmian words, Lecture 2: mechanical words, rotations*

Source: http://www-igm.univ-mlv.fr/~perrin/Enseignement/Master2011/Slides/Lecture2/slides2.pdf
Full text: [[perrin-sturmian-words-lecture2-mechanical.full]]

## What this source establishes

**Mechanical-word definition (the digit rule).** For 0 ≤ α, ρ ≤ 1,
- lower mechanical word: s_{α,ρ}(n) = ⌊(n+1)α + ρ⌋ − ⌊nα + ρ⌋
- upper mechanical word: s′_{α,ρ}(n) = ⌈(n+1)α + ρ⌉ − ⌈nα + ρ⌉
Both are {0,1}-valued. The word s_{α,ρ} is the one directive 2 uses.

**Rotation coding.** With the rotation R(z) = {z + α} and the partition
I₀ = [0, 1−α), I₁ = [1−α, 1),
  s_{α,ρ}(n) = 0 iff Rⁿ(ρ) ∈ I₀, 1 iff Rⁿ(ρ) ∈ I₁.
So the word is the coding of the orbit {nα + ρ} mod 1.

**Factor/interval correspondence (the key structural fact).** A word
w = b₀…b_{m−1} occurs as a factor of s_{α,ρ} starting at position n iff
Rⁿ(ρ) ∈ I_w := I_{b₀} ∩ R^{−1}(I_{b₁}) ∩ … ∩ R^{−m+1}(I_{b_{m−1}}).
- The interval I_w is nonempty iff w is a factor.
- **This property is independent of ρ, so s_{α,ρ} and s_{α,ρ′} have the same
  factor set.** Hence the factor set of slope α is exhaustively described by any
  one intercept's orbit.

**Morse–Hedlund 1940 (Theorem).** For an infinite word s the following are
equivalent: (1) s is Sturmian; (2) s is balanced and aperiodic; (3) s is
irrational mechanical. This is the theorem that makes the Fibonacci word's
k+1 factor count a *defining* property rather than an accident.

**Consequences used by the solver.**
- (Height bound) For a factor u = s(n)…s(n+p−1), its height
  h(u) = ⌊α(n+p)+ρ⌋ − ⌊αn+ρ⌋ satisfies α|u|−1 < h(u) < α|u|+1, so
  ⌊α|u|⌋ ≤ h(u) ≤ 1+⌊α|u|⌋: the height of a length-k factor takes two
  consecutive values — balance. This is why the k+1 factors split into two
  height classes (k·α−1 < h ≤ k·α+1, and h = ⌊kα⌋ or ⌊kα⌋+1). This directly
  bounds the digit distributions in Ψ(k).
- (Characteristic word) For irrational α, s_{α,0} = 0·c_α and s′_{α,0} = 1·c_α,
  where c_α is the characteristic word of slope α: c_α(n) = ⌊(n+2)α⌋ − ⌊(n+1)α⌋.
  So the problem's word S = c_α with α = 1/φ², and S(0)=0, S(1)=1, S(2)=0, …
  — matching S₀=0, S₁=01.
- Same slope ⇒ same factor set; distinct slopes ⇒ finite intersection.
- Rational α = p/q: s_{p/q,0} is purely periodic with period t_{p,q}, the
  **Christoffel word** t_{p,q} = 0·z_{p,q}·1 (starts 0, ends 1).

## What it implies for PE1006

1. The mechanical-word digit formula is the correct, source-backed model for the
   problem's Fibonacci word factors (slope 1/φ², intercepts = arc midpoints).
2. The k+1 factors can be indexed by k+1 distinct intercepts (one per open arc
   of the circle cut at k+2 points), each giving a k-digit 0/1 string via the
   floor-difference rule; that is directive 2's construction, now anchored.
3. The height bound h(u) ∈ {⌊kα⌋, ⌊kα⌋+1} is a cheap independent check on any
   implementation: every generated length-k factor must have ones-count in that
   two-element set. (For k=10^18, k·α ≈ 3.82·10^17, so the two counts differ by
   one — a strong test of the generated representative strings.)

## Claims anchored here

`governing-sturmian`, `governing-factor-complexity` (Morse–Hedlund),
`mechanical-word-digit-rule` (interval correspondence + same-slope-same-factors)
in `research/notes/sourced-claims-governing-theory.md`.

## What it does NOT establish

- No formula for Ψ(k); the sum-of-squares computation is the run's own.
- No O(log) evaluation of the geometric floor sums; that is the
  universal-Euclidean claim (fhq / OI-wiki / LOJ138).