# Tasks

- [x] Write brute.py: bounded-multiplicity coin DP computing f(n).
- [x] Verify f(10)=5, n=241 ratio 13/17, first-n scan = 241, SBE=4,3,1.
- [x] Empirically derive recurrences f(2n)=f(n)+f(n-1), f(2n+1)=f(n),
      f(2n-1)=f(n-1) and record them.
- [x] Identify/confirm governing theory (Calkin-Wilf / Stern diatomic A002487) with cited sources.
- [x] Write solution.py for ratio 123456789/987654321 (poly in log bound).
- [x] Verify final SBE by a second independent route. (verify_matrix.py's matrix/run model; answer SBE [1,13717420,8], ratio 123456789/987654321)
- [x] Write solution.md derivation artifact.
- [x] Both routes agree: answer SBE = [1,13717420,8]; reconstructed n = 2^13717428 + 255, bit length 13717429.
