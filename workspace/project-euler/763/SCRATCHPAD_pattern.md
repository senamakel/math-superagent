# Pattern-finder scratchpad

## Dead end: order-7 constant-coefficient linear recurrence is an OVERFIT

`find_linear_recurrence` over D(0..14) found an exact order-7 constant-coeff
recurrence:
  3 D[n] = 9 D[n-1] + 12 D[n-2] - 17 D[n-3] - 30 D[n-4] - 31 D[n-5] + 63 D[n-6]
verified over all 15 supplied terms. BUT tested against held-out statement
values it is definitively dead:
  - extrapolating, 3*D(n) numerator is not divisible by 3 starting at n=18
    (3*D(18) = 2387442214, rem 1), so it cannot equal an integer D(18).
  - therefore it can never reproduce D(20)=9204559704 or D(100) last digits.
Conclusion: any 15-term exactly-fitted linear recurrence is uninformative here;
the recurrence is a fit artifact, not a structural fact. Recorded as a known
dead end so nobody re-derives it.

## OEIS

D(0..14)=1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063
has NO OEIS entry. Not catalogued -> no looked-up closed form; structure must
come from the problem. (Recorded.)

## Exact structural facts from per-config feature dumps (data/level_N.txt)

N(N,M) = #distinct reachable configs after N divisions with max level = M.

Diagonal M=N:  N(N,N) = 3^(N-1), exact for N=2..12.
  3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147.

Sub-diagonal M=N-1:  N(N,N-1) = (N-3)*3^(N-3), exact for N=4..12.
  3, 18, 81, 324, 1215, 4374, 15309, 52488, 177147.
  (ratio to diagonal = (N-3)/3: 1/9,2/9,...,9/9.)

Both are CONJECTURES beyond the computed range (structural: configs that reach
the top level; candidate derivation via monotone/straight-line chains).

Full (N,M) table observed (row N, entries M:N(N,M)):
N=2: 2:3
N=3: 3:9
N=4: 3:3, 4:27
N=5: 4:18, 5:81
N=6: 4:12, 5:81, 6:243
N=7: 5:81, 6:324, 7:729
N=8: 5:48, 6:405, 7:1215, 8:2187
N=9: 5:9, 6:360, 7:1782, 8:4374, 9:6561
N=10: 6:246, 7:1971, 8:7290, 9:15309, 10:19683
N=11: 6:72, 7:1827, 8:9396, 9:28431, 10:52488, 11:59049
N=12: 6:30, 7:1254, 8:10368, 9:41310, 10:107163, 11:177147, 12:177147

Sum of each row = D(N) (check: N=12 sum = 514419 ✓).

## Pending
- d=2 BFS (agent-run-10) for D_2(N) to high N: will give a much longer clean
  sequence; test if IT has a linear recurrence / OEIS match.
