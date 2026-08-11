# Working memory

## Problem

Project Euler 175-style task: f(n) = number of ways to write n as a sum of powers of 2, each
power used at most twice (f(0)=1); find the "Shortened Binary Expansion" of the smallest n
with f(n)/f(n−1) = 123456789/987654321. Output: comma-separated run-lengths of bin(n), MSB→LSB,
no whitespace. Oracle: f(10)=5; smallest n for 13/17 is 241, bin(241)=11110001, SBE=4,3,1.

## Established results (source-backed; see research_report.md for quotes & URLs)

1. **Hyperbinary count = Stern sequence.** A002487 comment (verbatim): "a(n+1) is the number
   of ways of writing n as a sum of powers of 2, each power being used at most twice (the
   number of hyperbinary representations of n) [Carlitz; Lind]." Wikipedia's Calkin–Wilf
   article proves fusc(n+1) counts these via the fusc recurrence. So f(n) = s(n+1), s(0)=0,
   s(1)=1, s(2m)=s(m), s(2m+1)=s(m)+s(m+1).
   Sources: https://oeis.org/A002487 ; https://en.wikipedia.org/wiki/Calkin%E2%80%93Wilf_tree ;
   http://www.math.upenn.edu/~wilf/website/recounting.pdf

2. **Calkin–Wilf enumeration.** C&W Theorem 1 (2000): the n-th rational in reduced form is
   b(n)/b(n+1) with b = hyperbinary count; consecutive values coprime; each positive reduced
   rational exactly once. OEIS comment: "a(n)/a(n+1) runs through all the reduced nonnegative
   rationals exactly once [Stern; Calkin and Wilf]." Stern (1858) proved coprime consecutive
   terms and unique representation of any coprime pair (per Steuding–Hofmann–Schuster 2008).
   Sources: https://oeis.org/A002487 ;
   https://ems.press/content/serial-article-files/45350

3. **Tree rules.** Root 1/1; left child a/(a+b) (<1), right child (a+b)/b (>1); parent of
   a/b<1 is a/(b−a), parent of a/b>1 is (a−b)/b; parent-sum strictly decreases, so iterating
   reaches 1. Sources: https://en.wikipedia.org/wiki/Calkin%E2%80%93Wilf_tree ; C&W paper.

4. **Ratio recurrences (derived, verified on oracle values).** r(n) = f(n)/f(n−1).
   r(2m) = (f(m)+f(m−1))/f(m−1) = r(m)+1; r(2m+1) = f(m)/(f(m−1)+f(m)) = r(m)/(r(m)+1)
   (using f(2m+1)=f(m), f(2m+2)=f(m)+f(m+1)). Checked against stated values:
   r(2)=2/1, r(3)=1/2, r(4)=3/1, r(5)=2/3, r(6)=3/2, r(7)=1/3, r(8)=4/1, r(10)=5/3 ✓.
   NOTE (scratchpad fix): f(9)/f(8) = 3/4 = r(9), and f(10)/f(9)=5/3 = r(10); the old
   scratchpad note "r(9)=3/5" was a typo.

5. **Path/binary correspondence.** With breadth-first indexing (left child of k is 2k, right
   child 2k+1), the binary expansion of a node's index is a leading 1 followed by its
   root-to-node path bits, 0 = left edge, 1 = right edge (Yorgey/MLT blog; note arXiv:1411.1747
   uses the opposite assignment). Euclidean inverse: (a,b) with a<b emits 0 → (a, b−a); a>b
   emits 1 → (a−b, b); to (1,1); prepend 1 to reversed bits.
   Source: https://mathlesstraveled.wordpress.com/2009/10/18/the-hyperbinary-sequence-and-the-calkin-wilf-tree/

## Failed / not-yet-resolved approaches

- Naive hand-derivation of 13/17 → 241 with "node index = n+1, bits = bin(n+1) MSB→LSB" did
  NOT reproduce the oracle; the exact index alignment (n vs n+1) and the MSB→LSB read of the
  bits must be pinned down and machine-verified against 13/17 → 241 = 11110001 (SBE 4,3,1)
  before any full-size run. This is Phase-4 implementation work, not a claim.

## Open questions

- Exact bit-to-child convention + index alignment (to be settled empirically against the
  oracle in code; the underlying facts are all sourced).
- Exact bibliographic citation for "Lind" in A002487's "[Carlitz; Lind]" (not needed for the
  solution; the identity is proven in C&W 2000 and Wikipedia).

## Files

- research_report.md in /workspace: full sourced report with verbatim quotes and URLs.
- /workspace/sources/: saved copies of all cited pages (Wikipedia, OEIS A002487 + internal,
  A018819, MathWorld, C&W PDF text via two mirrors, Yorgey blog, Northshield abstract,
  Dilcher–Ericksen abstract, OEIS Stern–Brocot page).