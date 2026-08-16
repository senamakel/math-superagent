# Satisfier / multiplier data (fresh, computed this session)

Exact Hasse-CA satisfier counts over GF(p), enumerated over all p^n monic
degree-n polys (bound p^n <= 80000). sat = number satisfying the Hasse-CA
hypothesis; ce = counterexamples (satisfy, not pure power); m = sat/p.

Constant identities (all verified over the range):
  (T) ce = sat - p   [the p pure powers (x-a)^n always satisfy]
  (C) sat % p == 0   [m = sat/p is an integer]

multiplier m = sat/p at fixed p, as a function of n:
  p=2, n=3..16:   2, 1, 2, 2, 8, 1, 2, 2, 8, 2, 8, 8, 457, 1
  p=3, n=3..9:    1, 3, 5, 1, 5, 39, 1
  (m=1 means the prime is GOOD for that degree: only pure powers satisfy)

sat at fixed p as a function of n:
  p=2, n=3..16:   4, 2, 4, 4, 16, 2, 4, 4, 16, 4, 16, 16, 914, 2
  p=3, n=3..9:    3, 9, 15, 3, 15, 117, 3

multiplier at bad primes (raw sat/ce from satisfier_table):
  n=3: bad={2} -> p=2: sat=4,ce=2 (m=2=p)  ; good p=3,5,7,11: sat=p m=1
  n=4: bad={3,5,7} -> p=3,5,7: sat=p^2, m=p  ; good p=2,11: m=1
  n=5: bad={2,3,7,..} -> p=2: m=2=p ✓ ; p=3: sat=15, m=5 (BREAKS m=p) ;
       p=7: sat=49 m=7=p ✓ ; good p=5: m=1
  n=6: bad={2,5,..} -> p=2 m=2=p ✓ ; p=5 m=5=p ✓ ; good p=3 m=1
  n=7: p=2: sat=16 m=8 (BREAKS) ; p=3: sat=15 m=5 (BREAKS)
  n=8: p=2: m=1 (2 good for 8=2^3) ; p=3: sat=117 m=39 (BREAKS)
  n=9: p=2: m=2 ; p=3 (good, 9=3^2): m=1
  n=15: p=2: sat=914 m=457 (large break)

The "m=p at bad primes" law holds at n=3,4,6 (all bad primes tested) and at
n=5,p=2; n=5,p=7. It BREAKS at (5,3),(7,2),(7,3),(8,3),(15,2). At those,
m takes values 5, 8, 5, 39, 457.
