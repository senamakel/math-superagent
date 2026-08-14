# Tasks

- [x] Verify coordinate model and identity: H(n) = 3n^2 + 3n - 6*Phi(n) with
      Phi(n) = sum phi(k); origin not counted as hidden (else +1 off).
- [x] Write brute force (code/brute.py); reproduce oracles 30, 138, 1177848.
- [x] Write exact solution (code/solution.py) with int32 totient sieve;
      parity table vs brute at n = 5, 10, 1000.
- [x] Compute Phi(10^8) = 3039635516365908 and H(10^8) = 11762187201804552.
- [x] Verify Phi(10^8) independently via Möbius inversion (verify_mobius.py).
- [x] Record exact values in code/out/pe351_values.md.
