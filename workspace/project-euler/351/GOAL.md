# Goal

Project Euler 351 (hexagonal orchard), solved directly without consulting any
published answer.

Completion criteria (all met):
- [x] `code/brute.py`: naive enumeration oracle, prints H(5)=30, H(10)=138,
      H(1000)=1177848 — all match the given values.
- [x] `code/solution.py`: exact H(n) = 3n^2 + 3n - 6*Phi(n) via an Euler
      totient sieve; parity table for n=5,10,1000 matches brute force; then
      computes Phi(10^8) and H(10^8) exactly with a memory-efficient int32
      sieve.
- [x] Phi(10^8) verified by a second, independent route (Möbius inversion).
- [x] Exact integers recorded in code/out/pe351_values.md.

Final values: Phi(10^8) = 3039635516365908,
H(10^8) = 11762187201804552.
