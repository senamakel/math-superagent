# Solution: Project Euler 175 — derivation

## Problem restated

f(0) = 1; for n ≥ 1, f(n) = #{ multisets of powers of 2 in which each power occurs at
most twice, whose elements sum to n }.  Such a multiset is called a *hyperbinary
representation* of n.

Claim (given): for every reduced-ish fraction p/q with p > 0, q > 0 there is some n ≥ 1
with f(n)/f(n-1) = p/q.  Task: for p/q = 123456789/987654321 find the *smallest* such n,
and output its Shortened Binary Expansion (SBE): the lengths of the maximal runs of equal
bits of bin(n), read MSB→LSB, comma-separated, no whitespace.

## Governing theory (see memory.md for statements + citations)

1. Stern's diatomic sequence s: s(0)=0, s(1)=1, s(2m)=s(m), s(2m+1)=s(m)+s(m+1).
2. Theorem (Stern / Carlitz / Lindström):  f(n) = s(n+1).  I.e., hyperbinary
   representations of n are counted by s(n+1).
3. Calkin–Wilf tree: root 1/1; left child of a/b is a/(a+b); right child is (a+b)/b.
   The node with index n is s(n)/s(n+1); every positive rational appears exactly once,
   in lowest terms.  The binary expansion of n (n ≥ 1) encodes the path from the root:
   the MSB '1' is the root itself, and each subsequent bit takes the left (1) or right (0)
   child.  (Worked out below; hence r(n) := s(n+1)/s(n) = f(n)/f(n-1) enumerates every
   positive reduced fraction exactly once as n runs over 1,2,3,….)

## Why it applies

- f(n)/f(n-1) = s(n+1)/s(n) =: r(n) is instantly a positive rational in lowest terms
  (consecutive Stern terms are coprime).
- The map n ↦ r(n) is a bijection 1,2,3,… → Q⁺ (in reduced form), because the Calkin–Wilf
  enumeration is a bijection and n ↦ r(n) is exactly the enumeration of the tree's
  *ratios*; equivalently r(n) sits at the position n of the Calkin–Wilf sequence ordered
  by level-order index.  Consequently "the smallest n with ratio p/q" is simply
  n = the index of p/q in this enumeration — no search is involved at all.

## Path → ratio recurrences (hand-checked, see below)

Write r(n) = s(n+1)/s(n), n ≥ 1.  From Stern's recurrences:

- r(2m) = s(2m+1)/s(2m) = (s(m)+s(m+1))/s(m) = r(m) + 1        (index bit 0 ⇒ ratio +1)
- r(2m+1) = s(2m+2)/s(2m+1) = s(m+1)/(s(m)+s(m+1)) = r(m)/(r(m)+1)  (index bit 1)

So the bits of n, read MSB→LSB after the leading '1', are the *steps* of a walk on the
Calkin–Wilf tree: bit 0 = "right child" (ratio : r ↦ r+1), bit 1 = "left child"
(ratio : r ↦ r/(r+1)).  Root = 1/1 = r(1).

Hand-check against the oracle table (r(1..10) = 1/1, 2/1, 1/2, 3/1, 2/3, 3/2, 1/3, 4/1,
3/5, 5/3, matching f(n)/f(n-1) in scratchpad for n=1..10):
- r(5): 5 = 101₂, path bits 0,1 after '1': root → right (2/1) → left (2/2+1=2/3) ✔
- r(10): 10 = 1010₂, path 0,1,0: 1/1 → 2/1 → 2/3 → 5/3 ✔

## Inverse: ratio → index (Euclidean walk)

Given reduced a/b with a/b = r(n):

- If a > b: parent of the node is (a-b)/b, and the downward step was bit 0 (right).
- If a < b: parent is a/(b-a), and the downward step was bit 1 (left).
- Stop when a = b = 1 (root, r(1)).

Repeatedly stepping up to the root yields the path bits in *reverse* order (last taken
first); the binary expansion of n is '1' followed by the path bits in forward order, i.e.
reversing the collected bits.  This is the Euclidean algorithm; the number of steps is
O(log p + log q), independent of n.  **No search of the answer space is involved** — the
cost grows with the size (bit length) of p and q, not with n.

## Oracle check of the inverse walk (must and does reproduce the statement)

Target 13/17 (r(n) = 13/17):
- (13,17), a<b: up → (13,4), bit 1
- (13,4), a>b: up → (9,4), bit 0
- (9,4), a>b: up → (5,4), bit 0
- (5,4), a>b: up → (1,4), bit 0
- (1,4), a<b: up → (1,3), bit 1
- (1,3), a<b: up → (1,2), bit 1
- (1,2), a<b: up → (1,1), bit 1
Bits upward: 1,0,0,0,1,1,1. Reverse: 1,1,1,0,0,0,1. Binary: 11110001 = 241. ✔
SBE(11110001) = runs (4 ones)(3 zeros)(1 one) = "4,3,1". ✔ matches the statement exactly.

## Full-size run

Target p/q = 123456789/987654321.

Step 1 — reduce: gcd(123456789, 987654321) = 9, so p/q = 13717421/109739369.
Check: 109739369 = 8·13717421 + 1, so gcd(13717421, 109739369) = 1 and the fraction is in
lowest terms.  (The *ratio* r(n) = f(n)/f(n-1) is always in lowest terms, so n comes from
the reduced fraction; the claim's p/q need not be reduced a priori, but reducing is
harmless and necessary for the Euclidean walk to stop at (1,1).)

Step 2 — Euclidean walk from (13717421, 109739369):
- 109739369 = 8·13717421 + 1: since a < b and ⌊b/a⌋ = 8 with remainder 1:
  eight consecutive "bit 1" up-steps: (13717421, 109739369) → … → (13717421, 1).
- Then a > b: 13717420 consecutive "bit 0" up-steps: (13717421, 1) → … → (1,1).
Bits upward: '1' × 8, then '0' × 13717420.  Reverse: '0' × 13717420, then '1' × 8.
Binary of n: '1' + (zeros × 13717420) + (ones × 8).

Step 3 — SBE: the leading '1' is the first bit of the binary expansion and is followed by
a run of zeros, so the first run has length 1; then a run of 13717420 zeros; then a run
of 8 ones.  Candidate SBE = 1,13717420,8.

## What remains (phases 4–5)

- solution.py must reproduce the oracle (f(10)=5 via direct enumeration; ratio walk →
  n=241, SBE "4,3,1") before the full-size run, then compute the full-size answer with
  exact integer arithmetic (a pure Euclidean loop, no floating point).
- Independent verification route: a second program that (i) mirrors the Calkin–Wilf
  enumeration with a *different* formulation (e.g. dense index-free recursion or the
  Stern-table construction s(n+1)/s(n) at the found index, or the "opposite" walk
  direction), plus brute-force confirmation of the oracle values and of as large a case
  as brute force can reach (exact integer numerator/denominator compare, no floats).
- The candidate "1,13717420,8" above is provisional until machine-verified.