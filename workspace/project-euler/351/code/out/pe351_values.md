# Exact values (Project Euler 351)

All values computed directly in this run; no published answer was consulted.

- Phi(5)     = 10
- Phi(10)    = 32
- Phi(1000)  = 304192
- Phi(10^8)  = 3039635516365908
- H(5)       = 30        (brute force; matches given oracle)
- H(10)      = 138       (brute force; matches given oracle)
- H(1000)    = 1177848   (brute force; matches given oracle)
- H(10^8)    = 11762187201804552   (3*N^2 + 3*N - 6*Phi(N))

## Verification

- brute.py enumerates all 3n^2+3n+1 points of the hexagon (axial coords,
  |a|,|b|,|a+b| <= n) and counts hidden as gcd(a,b) > 1, origin excluded:
  matches the given oracles at n = 5, 10, 1000.  (The origin is not counted
  as hidden; that is what makes the identity H = 3n^2+3n-6*Phi(n) hold.)
- solution.py's identity matches the brute-force oracle at n = 5, 10, 1000.
- Phi(10^8) computed two independent ways, agreeing exactly:
  1. incremental totient sieve (code/lib/totient.py sum_phi, int32 table),
  2. Mobius inversion Phi(N) = sum mu(k)*T(floor(N/k)) (verify_mobius.py,
     separate int8 mu sieve; shares only the prime list).
- Sanity: Phi(N)/N^2 = 0.30396355... vs 3/pi^2 = 0.30396355...

Producer programs: code/solution.py (H(10^8), parity table),
code/verify_mobius.py (independent Phi), code/brute.py (oracle).
