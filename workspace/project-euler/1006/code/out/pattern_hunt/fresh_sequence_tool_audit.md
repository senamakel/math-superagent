# Fresh exact sequence-tool audit (2026-08-18)

Method: read current artifact files, retain exact integer terms, fit homogeneous rational recurrences (orders 1--12), and run Berlekamp--Massey modulo prime 100000007. These are finite diagnostics, not proofs.
## c1
- terms used: n=400, first 12=[1, 1, 2, 2, 2, 3, 3, 4, 4, 4, 5, 5]
- exact recurrence orders 1..12: []
- BM complexity mod 100000007: 232
- law c1(k)=1+floor(k*(3-sqrt(5))/2): first falsifier=None
## Lmin
- terms used: n=400, first 12=[2, 4, 7, 8, 12, 13, 14, 20, 21, 22, 23, 24]
- exact recurrence orders 1..12: []
- BM complexity mod 100000007: 200
- law Lmin(k)=k+NextFib(k)-1: first falsifier=None
## toeplitz defect
- terms used: n=400, first 12=[0, 0, 2, 0, 2, 8, 0, 18, 10, 16, 32, 0]
- exact recurrence orders 1..12: []
- BM complexity mod 100000007: 200
- zero indices (all supplied): [1, 2, 4, 7, 12, 20, 33, 54, 88, 143, 232, 376]
- all-zero conjecture first falsifier=(3, 2)
## Psi residues
- terms used: n=400, first 12=[1, 101, 20302, 2042402, 2250400, 44353102, 14581260, 65706380, 21161323, 10699667, 77738268, 50567341]
- exact recurrence orders 1..12: []
- BM complexity mod 100000007: 200
- Psi mod 100 == c1 first falsifier=(5, 2250400)
- Psi mod 1000 == c1 first falsifier=(2, 101)
## run gaps
- terms used: n=153, first 12=[1, 3, 2, 3, 3, 2, 3, 2, 3, 3, 2, 3]
- exact recurrence orders 1..12: []
- BM complexity mod 100000007: 88
- distinct gaps (after boundary marker)=[2, 3]; first non-{2,3}=None
## run starts
- terms used: n=154, first 12=[0, 10, 10010, 1010010, 1001010010, 1001001010010, 101001001010010, 100101001001010010, 10100101001001010010, 10010100101001001010010, 10010010100101001001010010, 1010010010100101001001010010]
- exact recurrence orders 1..12: []
- BM complexity mod 100000007: 89

## Conclusion
The exact audit finds no new surviving scalar constant-coefficient recurrence. The strongest surviving finite laws are c1 floor law, Lmin strict-next-Fibonacci law, run gaps in {2,3}, and Psi ≡ c1 (mod 100); Toeplitz defects are not identically zero and Psi mod 1000 is falsified early.
