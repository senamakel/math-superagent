# Scratchpad

## Phase 1 — small cases verified by hand (oracle)

f(0)=1, f(1)=1, f(2)=2 (2 = 2 = 1+1), f(3)=1 (3 = 2+1), f(4)=3 (4, 2+2, 2+1+1),
f(5)=2 (4+1, 2+2+1), f(6)=3 (4+2, 4+1+1, 2+2+1+1), f(7)=1 (4+2+1), f(8)=4
(8, 4+4, 4+2+2, 4+2+1+1), f(9)=3, f(10)=5 (matches the statement's five ways).

Ratio table f(n)/f(n-1), n=1..10: 1/1, 2/1, 1/2, 3/1, 2/3, 3/2, 1/3, 4/1, 3/5, 5/3.

## Phase 3 — structural insight (derivation sketch, to be promoted after research confirms)

Hypothesis: f(n) = s(n+1), s = Stern's diatomic sequence, s(0)=0, s(1)=1,
s(2n)=s(n), s(2n+1)=s(n)+s(n+1). Then f(n)/f(n-1) = s(n+1)/s(n) =: r(n).

Hand-checked: s(n+1) for n=0..10 = 1,1,2,1,3,2,3,1,4,3,5 = f(0..10). ✔

Recurrences for r(n) = s(n+1)/s(n):
- r(2m) = s(2m+1)/s(2m) = (s(m)+s(m+1))/s(m) = r(m)+1   (right child, index ends in bit 0)
- r(2m+1) = s(2m+2)/s(2m+1) = s(m+1)/(s(m)+s(m+1)) = r(m)/(r(m)+1)   (left child, bit 1)

So appending bit 0 to the binary index = "r := r+1" (right child of the Calkin–Wilf tree
with left child p/(p+q), right child (p+q)/q); appending bit 1 = "r := r/(r+1)" (left child).

Consequently r(n) is found at index n whose binary expansion is 1 followed by the path
bits (0 = right, 1 = left) — VERIFIED against known values: 1/1@1, 2/1@2, 1/2@3, 3/1@4,
2/3@5, 3/2@6, 1/3@7, 4/1@8, 3/5@13, 5/3@10. ✔ (hand-checked via Stern table)

Inverse walk (target → root), the Euclidean algorithm with digit emission:
- current r = a/b, gcd(a,b)=1.
- if a > b: parent is (a-b)/b; going down used bit 0.  (r = parent + 1)
- if a < b: parent is a/(b-a); going down used bit 1.  (r = parent/(parent+1))
- stop at (1,1) = root.
bits emitted upward; n's binary = '1' + reverse(bits).

Oracle check: 13/17 → steps: (13,17)→'1'(1/4 family ...). Bits up: 1,0,0,0,1,1,1 →
binary 11110001 = 241. SBE of 11110001 = 4,3,1. ✔ (matches statement exactly)

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
- Double check run-length merging: leading '1' merges with a following 1-run only.