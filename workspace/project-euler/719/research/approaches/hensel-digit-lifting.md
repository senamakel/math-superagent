# Construct the root digit-by-digit via Hensel lifting instead of scanning

## The idea in one line

Turn the search inside out: build the root m from its least-significant decimal
digits upward, using the fact that each new digit of m determines 2j digits of
m², and prune whenever a block boundary of m² would force a block value that the
running sum to m can no longer absorb.

## Mathematics

The square map m ↦ m² is a 10-adic lifting: if m ≡ m_j (mod 10^j) is known, then
m² is determined modulo 10^{2j}, and extending m_j by one digit m_j + d·10^j
extends m² by the two new digits. This is **Hensel's lemma / Newton iteration**
for the polynomial x² in the 10-adic ring (10 = 2·5 is not prime, so it is a
CRT-composed lifting over ℤ₂ × ℤ₅ — Hensel applies componentwise). Reading the
S-witness from the least significant side, the low blocks of m² are fully
determined once enough low digits of m are fixed; the condition that those
blocks sum into m gives local constraints on each new digit before the high
digits are even known.

Concretely: suppose a block b ends at decimal position P of m². Then b is
determined by m² mod 10^P and m² mod 10^{P+len(b)}. Fixing m mod 10^j with
2j ≥ P determines that block exactly. So a "block lands and contributes value
v" is a congruence condition on m mod 10^j. The full witness is a
simultaneous system of such conditions, and the root scan is replaced by
extending partial roots whose currently-determined blocks already sum into
[0, m], pruning the moment the committed partial sum exceeds m or forces the
remaining high digits of m out of range.

## Why it is a different line of attack

The adopted method fixes m and searches over splits of m²'s digit string (the
digit-DP memoises (position, remaining-sum) over a *given* square). This
proposal fixes the *splitting constraint* and searches over the digits of m —
the independent variable is the root's digit string, constructed incrementally,
with m² read off by Hensel lifting rather than recomputed wholesale. It is the
standard "constraint propagation / backtracking over digits" pattern that
solves cryptarithmetic and digit-substitution problems, applied with the square
map's lifting structure doing the pruning. If the committed partial blocks prune
early enough, the number of partial roots explored is far below 10⁶; if the
pruning is weak, the approach collapses to the scan and closes with that reason.

## What is speculation vs established

- Established: Hensel lifting / Newton iteration for x²; CRT over ℤ₂×ℤ₅; the
  digit-by-digit square recurrence m²_{j+1} from m_{j} is exact integer
  arithmetic (the frontier already notes a paper on constructive digit-by-digit
  root extraction).
- Speculation: that the block-boundary constraints prune the lifting tree hard
  enough to beat the isqrt(N) scan. Untested by this run — the digit-DP prunes
  over *splits of a fixed square*, not over *digits of the root*.

## Cost

If pruning is strong, O(number of surviving partial roots × digits), potentially
≪ 10⁶. If weak, it is O(10⁶ · D) — no worse than the adopted scan — but then it
closes as a dead end with the measured branching factor recorded.

```approach
idea: Build each candidate root m from its least-significant digits upward with Hensel lifting of the square map, pruning the digit tree the moment a committed low block of m² would push the block-sum past m or out of range.
mechanism: Hensel's lemma / Newton iteration for x² over ℤ₂×ℤ₅ (CRT); a block of m² is fully determined once enough low digits of m are fixed, so the S-witness becomes local congruence constraints on each new digit — the cryptarithmetic constraint-propagation pattern, with the square's lifting structure doing the pruning.
status: refuted
## Research verdict (researcher, sourced)

**What the reformulation is actually called.** This is **digit-by-digit (or
digit-block) root extraction / Hensel (Newton) lifting of the square map**, in the
*constraint-propagation over decimal digits* paradigm used for cryptarithms and
digit-substitution problems. The square map m ↦ m² fixing j low digits of m
determines 2j low digits of m² is exactly the p-adic (Hensel) lifting of x², over
ℤ₂ × ℤ₅ via CRT, and the classical long-division/square-root algorithm is the
decimal special case of this. Cost estimate: worst case O(10^6 · D) digits of m —
no better than the scan; the only win would be early block-boundary pruning.

**Theorems it rests on, and whether they hold here.**
- *Hensel's lemma / Newton iteration for x² over a p-adic ring*: if m ≡ m_j
  (mod p^j), then m² is determined mod p^{2j}, and a root of x² − a mod p^j lifts
  to mod p^{2j} when the derivative condition holds. Here the ring is ℤ₁₀ ≅ ℤ₂×ℤ₅
  (10 = 2·5 is not prime, so one does a CRT-composed lifting on each factor).
  **Holds* here**: the digit-by-digit square recurrence m_{j+1} = 10·m_j + d with
  (10m+d)² = 100m²+20md+d² is exact integer arithmetic — this is standard and
  verified by the adopted digit-DP and by the run's brute force.
- The *cryptarithmetic constraint-propagation* idea: a low block of m² "lands"
  once enough low digits of m are fixed, giving a local congruence constraint on
  each new digit. This is a genuine, standard pattern, and the run already has the
  theory and code for the *exact* digit partition (split-and-sum recursion, mod-9
  filter) that this pruning would feed. But there is **no published source** that
  applies digit-by-digit square lifting to the S-number split-and-sum-to-root
  condition specifically; searches return (a) general digit-by-digit *root
  extraction* (long division, and modern exact e-th root algorithms such as
  arXiv:2601.02703, Zambaldi Garcia et al. 2026 DOI 10.5433/1679-0375.2026.v47.54706)
  and (b) p-adic square-root lifting in its own right (Zerzaihi–Kecies–Knapp 2010,
  Ignacio et al. 2013, relaxed Hensel lifting). None of these targets the
  split-and-sum predicate.

**What it would buy.** If block-boundary pruning kept the digit-lifting tree well
below 10^6 partial roots it would beat the isqrt(N) scan; if not it is O(10^6·D),
the same cost as the scan already recorded. Which it is is a *measurement*, not a
theorem — the candidate's own first-step says to measure and, if weak, close with
the measured branching factor. There is no literature claiming strong pruning for
this square-split predicate.

**Bottom line.** The mechanism (digit-by-digit square lifting / Hensel over ℤ₁₀,
constraint propagation over decimal digits) is **genuine and grounded** as a real
technique the literature confirms; its *application to the S-number predicate* is
novel with no precedent found. Whether it beats the already-settled O(sqrt N)
scan is empirically open, not a theorem. Also: unlike candidates 1 and 2 it
offers no N-independent asymptotic improvement — worst case it just re-enumerates
roots, so its only virtue is a possibly-constant-gain constant.

precedent: |
  - Digit-by-digit square root / long division: classical; modern exact treatment
    in arXiv:2601.02703 ("Exact Constructive Digit-by-Digit Algorithms for Integer
    e-th Root Extraction").
  - Digit-based square-root block algorithm: Zambaldi Garcia et al. 2026,
    DOI 10.5433/1679-0375.2026.v47.54706.
  - p-adic Hensel lifting of square roots: Zerzaihi–Kecies–Knapp 2010
    (DOI 10.2298/aadm1000009m); Secant/Halley p-adic root refinement
    (S0885064X09000818); relaxed Hensel lifting (ACM ISSAC, DOI 10.1145/2442829.2442842).
  - The exact split-and-sum recursion it feeds: claim `a038206-expr-recursion`,
    `partition-sum-invariant-mod9` (mod-9 carry/filter), source BGS arXiv:1501.04067.
  - No source found applying digit-by-digit lifting to the split-and-sum-to-root
    predicate. Application is novel (no precedent).
first-step: Implement the digit-by-digit square recurrence m²_{j+1} from m_j exactly, instrument the block-boundary conditions as they "land," and measure the branching factor of the lifting tree over roots ≤ 10⁴ against brute.py — if the tree size is far below the number of roots, scale to 10⁶; if not, record the measured branching factor and close.
killed-by: offers no asymptotic gain over the settled O(sqrt N) scan — worst case it re-enumerates all 10⁶ roots, so as a reformulation it collapses to the adopted method and its only possible win is a constant factor. Its genuine contribution, the local congruence structure of the square map, is folded into the adopted repunit approach's cyclotomic-basis first step.
```
