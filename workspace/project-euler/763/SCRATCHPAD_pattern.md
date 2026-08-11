# Pattern-finder findings (PE763)

## 1. DEAD END: order-7 constant-coefficient recurrence is an OVERFIT

`find_linear_recurrence` over D(0..14) found an exact order-7 recurrence
3D[n]=9D[n-1]+12D[n-2]-17D[n-3]-30D[n-4]-31D[n-5]+63D[n-6], verified on all 15
terms. But extrapolating, 3*D(18)=2387442214 is NOT divisible by 3, so it
cannot equal integer D(18). First falsifier n=18. It can never reproduce the
statement's D(20)=9204559704 or D(100) last digits. => any 15-term exactly
fitted linear recurrence here is a fit artifact. Do not re-derive.

## 2. OEIS misses for the d=3 sequence

D(0..14)=1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063
is NOT in OEIS. No looked-up closed form; structure must come from the problem.
(Recorded already.)

## 3. SOURCED: d=2 sequence == OEIS A007902 (pebbling configurations)

D_2(N) (2D amoeba, count distinct configs after N divisions) for N=0..21:
1,1,2,4,9,20,46,105,243,561,1301,3014,6995,16227,37668,87426,202961,471150,
1093819,2539348,5895408,13686805
matches OEIS A007902(N+1) exactly (filed research/L1.0/oeis_a007902.md).
Sourced; asymptotic D_2(N)~0.1227*2.3216^N (Knessl 2006). d=2 has NO simple
constant-coefficient recurrence either (order<=12 fails) — its OEIS form is a
two-index G(k,m) recursion. First falsifier (untested): D2(22) vs A007902(23)=
31775756 (d=2 BFS OOM'd at 22 in this container).

## 4. Structural: configs decompose by max level M

N(N,M) = # distinct reachable configs after N divisions with max level M
(=x+y+z) satisfies EXACTLY (N=2..12):
   N(N, N-k) = Q_k(N) · 3^(N-2k-1)   where Q_k is a polynomial in N, degree k.
   Q_0 = 1
   Q_1 = N-3
   Q_2 = (N-5)(N+2)/2
   Q_3 = (N^3 - 73N + 168)/6
   Q_4, Q_5: 4,9,82,203,384,... ; 72,418 (too few points to pin down yet)
D(N) = sum_M N(N,M). This decomposition reproduces D(2..8) totally; for
N>=9, D = (k<=K model sum) + (deeper offsets), matching exactly only when all
offsets included.

Q-array (row N, col k=N-M):
N=2: 1
N=3: 1
N=4: 1 1
N=5: 1 2
N=6: 1 3 4
N=7: 1 4 9
N=8: 1 5 15 16
N=9: 1 6 22 40 9
N=10: 1 7 30 73 82
N=11: 1 8 39 116 203 72
N=12: 1 9 49 170 384 418

Other exact column forms seen: count(M=N)=3^(N-1); count(M=N-1)=(N-3)3^(N-3).

## Status of conjectures
- All are CONJECTURES beyond computed range; none promoted to MEMORY yet.
- (N,M) decomposition + Q_0..Q_3 verified EXACTLY over every computed point
  (attacked; consistent). Survived its break attempt for the points available.
- Q_4, Q_5 have too few points (only ~3-4 rows) to confirm closed forms.
- First falsifier for diagonal 3^(N-1): N=13 (needs M=13, not BFS-computed).
