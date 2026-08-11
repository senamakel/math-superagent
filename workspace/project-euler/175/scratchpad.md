# Scratchpad

## Phase 1 — small cases verified by hand (oracle)

f(0)=1, f(1)=1, f(2)=2 (2 = 2 = 1+1), f(3)=1 (3 = 2+1), f(4)=3 (4, 2+2, 2+1+1),
f(5)=2 (4+1, 2+2+1), f(6)=3 (4+2, 4+1+1, 2+2+1+1), f(7)=1 (4+2+1), f(8)=4
(8, 4+4, 4+2+2, 4+2+1+1), f(9)=3, f(10)=5 (matches the statement's five ways).

Ratio table f(n)/f(n-1), n=1..10: 1/1, 2/1, 1/2, 3/1, 2/3, 3/2, 1/3, 4/1, 3/5, 5/3.

## Phase 3 — structural insight (Phase 2 research complete: see research_report.md and memory.md)

Sourced facts (URLs in memory.md):
- f(n) = s(n+1), s = Stern's diatomic sequence (OEIS A002487; Wikipedia; Calkin–Wilf 2000).
- C&W tree: root 1/1; left child a/(a+b), right child (a+b)/b; n-th rational = s(n)/s(n+1),
  all reduced, each positive reduced rational exactly once; consecutive terms coprime.
- Ratio recurrences (derived from sourced pairwise recurrences):
  r(2m) = r(m)+1, r(2m+1) = r(m)/(r(m)+1), r(1)=1/1.
- Path/binary: index = leading 1 + path bits (0=left,1=right); Euclidean inverse emits bits
  LSB-first, reverse then prepend 1.
- OPEN: exact n-vs-(n+1) index alignment and MSB→LSB read; must be machine-verified against
  oracle 13/17 → 241 = 11110001 (SBE 4,3,1) before full-size work.

## Phase 4 (next) — implementation checklist

1. Write f(n) via Stern/fusc (O(log n)) and verify f(10)=5.
2. Implement ratio-walk (EuEuclidean): (a,b)→(a,b−a) bit 0 / (a−b,b) bit 1 to (1,1);
   bits reversed, prepend 1; then adjust index alignment so 13/17 → 241 (bin 11110001, SBE
   4,3,1). Try both "node index = P" and "n = P−1" variants and pick the one matching 241.
3. Reduce 123456789/987654321 by gcd (9): 13717421/109739369; walk; SBE; independent
   verification route (e.g., forward recomputation of f(241+1) ratio check, or a second
   implementation by a different recurrence).
4. Keep total complexity O(log(a+b)) (compressed subtract-quotient runs).

## Reduced form of the target

p = 123456789, q = 987654321. gcd = 9: p/q = 9·13717421 / (9·109739369).
gcd(13717421, 109739369): 109739369 = 8·13717421 + 1 → gcd = 1. Reduced: 13717421/109739369.

## Preliminary hand-computation of the walk (to be re-derived in code)

(13717421, 109739369): since 8·13717421 = 109739368 < 109739369, emit '1' × 8 →
(13717421, 1). Then emit '0' × 13717420 → (1,1).
Bits up: 11111111 000...0 (13717420 zeros). Reversed: 000...0 11111111.
n binary = 1 000...0 (13717420 zeros) 11111111 → SBE = 1,13717420,8.
(To be confirmed by code: this '1,13717420,8' is a strong candidate but is NOT the answer
until the whole chain—reduced fraction, digit convention, run merging—is machine-verified
and independently confirmed.)

## Open questions before finalizing

- Research agent: cite confirmed theorem f(n) = s(n+1) (hyperbinary ↔ Stern) and the
  Calkin–Wilf bijection + digit-to-move correspondence + coprimality of consecutive Stern terms.
  **DONE in Phase 2** — see research_report.md, memory.md (sources: OEIS A002487, Wikipedia
  Calkin–Wilf, C&W 2000 PDF, Steuding et al. 2008, MathWorld, Yorgey blog).
- Double check run-length merging: leading '1' merges with a following 1-run only. (Still to
  confirm in code: exact bit alignment for the oracle 13/17 → 241.)