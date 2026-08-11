# Working memory

## Problem

Project Euler 175: f(0)=1; for n≥1, f(n) = number of ways to write n as a sum of powers of 2 where
no power occurs more than twice ("hyperbinary representations"). For every p>0,q>0 there is an
n with f(n)/f(n-1)=p/q. Find the Shortened Binary Expansion (runs of bin(n), MSB→LSB,
comma-separated, no whitespace) of the SMALLEST n with f(n)/f(n-1)=123456789/987654321.
Oracle: f(10)=5 (five listed representations); 13/17 → n=241, bin 11110001, SBE "4,3,1".
Full statement in /workspace/goal.md.

## Established results (with sources; local copies under /workspace/sources/, full report /workspace/research_report.md)

1. **f(n) = s(n+1)**, s = Stern's diatomic sequence: s(0)=0, s(1)=1, s(2m)=s(m), s(2m+1)=s(m)+s(m+1)
   (OEIS A002487 "a(n+1) is the number of hyperbinary representations of n [Carlitz; Lind]" —
   https://oeis.org/A002487 ; proof via recurrences in https://en.wikipedia.org/wiki/Calkin%E2%80%93Wilf_tree ;
   primary source Calkin & Wilf, "Recounting the rationals", AMM 107 (2000) 360–363,
   https://www2.math.upenn.edu/~wilf/website/recounting.pdf , b(n) = hyperbinary count, proves
   b(2n+1)=b(n), b(2n+2)=b(n)+b(n+1), b(0)=1).
   CAREFUL: OEIS A018819 is the UNRESTRICTED binary partition function — different sequence, do not use.

2. **Calkin–Wilf tree**: root 1/1; children of a/b: left a/(a+b), right (a+b)/b; every positive
   rational occurs exactly once, in lowest terms; n-th rational (BFS) = s(n)/s(n+1);
   consecutive Stern terms are coprime (Wikipedia, C&W 2000 Theorem 1, OEIS A002487;
   Stern 1858 via https://ems.press/content/serial-article-files/45350 ).
   Parent rules: if a/b < 1 parent a/(b-a); if > 1 parent (a-b)/b (Wikipedia).

3. **Binary-index ↔ path** (Yorgey, https://mathlesstraveled.wordpress.com/2009/10/18/the-hyperbinary-sequence-and-the-calkin-wilf-tree/ ):
   label edges 0 (left) / 1 (right); path bits + leading 1 = binary index. NOTE: conventions of
   0/1 = left/right vary between sources; the working convention for THIS problem is fixed by the
   oracle (13/17 → 241): ratio r(n)=s(n+1)/s(n), r(1)=1/1, recurrences r(2m)=r(m)+1,
   r(2m+1)=r(m)/(r(m)+1), i.e. bit 0 = right (r ↦ r+1), bit 1 = left (r ↦ r/(r+1)), bits read
   MSB→LSB after the leading '1'. Hand-verified on oracle values r(1..10) and on 13/17 → 11110001.

4. **Inverse Euclidean walk** (ratio → index): from reduced (a,b): if a>b step up to (a-b,b)
   (downward step was bit 0); if a<b step up to (a,b-a) (downward step was bit 1); stop at (1,1).
   Bits collected rootward; n = '1' + reversed(bits). Compressed: a>b: j=(a-1)//b steps of '0',
   a-=j*b; a<b: j=(b-1)//a steps of '1', b-=j*a. O(log) steps. Source: Wikipedia parent rules +
   Yorgey's algorithm; whole argument = Euclidean algorithm.

5. Caveat from research: the exact MSB→LSB bit/ratio alignment is pinned by the oracle 13/17 → 241
   (implementations must reproduce it). (Resolved in Phase 3 by hand; solution.md derives it.)

## Failed approaches / corrections

- Scratchpad had "r(9)=3/5" typo: correctly f(9)/f(8) = 3/4 (f(8)=4, f(9)=3). All other hand values
  verified by the research agent against the recurrences.
- A018819 UI mistaken for the hyperbinary sequence → discarded (different sequence).
- "Lindström 1971" reference for the hyperbinary identity could not be bibliographically pinned down;
  the identity itself is fully sourced via C&W 2000 / OEIS / Wikipedia. Do not cite "Lindström 1971".

## Open questions

- None blocking. Pending: machine verification of the full-size SBE by an independent program
  (Phase 5), including forward verification s(n+1)/s(n) at the enormous found n via an independent
  implementation of Stern's recurrences, brute-force scan on reachable ratios, and hyperbinary-DP
  vs Stern-table agreement.

## Provisional candidate (NOT final until machine-verified)

Reduced target 13717421/109739369; walk gives bits up: '1'×8 then '0'×13717420 →
n = 1 followed by 13717420 zeros and 8 ones → SBE = 1,13717420,8 (to be confirmed in Phases 4–5).