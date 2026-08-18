# Runtime note — memory store outage

`remember_memory` and `note_scratch` both failed on this run: the memory
server's health check did not answer within 8 s, and the tool reported the
document "would be accepted and dropped rather than stored."

Nothing of the run's findings was lost: the Chen-prime check result is
durably recorded in `code/out/chen_goldbach_1e8.md` (fenced `claim` block,
status: checked), in `code/chen_goldbach/INDEX.md`, and in `code/out/INDEX.md`.
When the memory server recovers, store:

- durable finding: every even n ≡ 4 (mod 6) with 4 ≤ n ≤ 10^8 is a sum of
  two Chen primes; no first failure at 10^6 / 10^7 / 10^8; witness at n=10^8
  is (29, 99999971); 63.12 s wall; exact bytearray sieve method, oracle
  cross-checked for p ≤ 200 and hand-checked for p=2,3,7, ordinary Goldbach
  reproduced for all even n in [4, 1000]. Evidence toward G-structural-closure
  candidate (d); not a proof (exceptional set could be nonempty above 10^8).
- durable finding (all-even extension, second outage): the all-even Chen-pair
  check (every even n in [4,B], n = p + q with p, q Chen primes) finds its
  FIRST FAILURE at n = 302 (≡ 2 mod 6), independent of bound; the 4-mod-6
  class stays clean through 10^9; all 27 failures ≤ 10^6 are ≡ 2 mod 6.
  Verified by two independent routes (sieve + sympy factorisation, identical
  27-failure list ≤ 10^5) and the trial-division oracle (first failure 302).
  Runs: 10^7 4.29 s, 10^8 63.98 s, 10^9 800.59 s. Claim
  chen-prime-goldbach-all-even-1e9 in code/out/chen_goldbach_all_1e9.md.
  The 4-mod-6 restriction in Grimmelt–Teräväinen is genuine, not an artifact.
  Not a proof: 2-mod-6 failures may exist above 10^6 and 4-mod-6 may fail
  above 10^9.
