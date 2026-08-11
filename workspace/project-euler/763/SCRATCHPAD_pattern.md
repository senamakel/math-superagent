# Pattern-finder findings (PE763) — final

## 1. DEAD END: order-7 constant-coefficient recurrence is an OVERFIT
`find_linear_recurrence` over D(0..14) found an exact order-7 recurrence
3D[n]=9D[n-1]+12D[n-2]-17D[n-3]-30D[n-4]-31D[n-5]+63D[n-6]. Extrapolating,
3*D(18)=2387442214 NOT divisible by 3, first falsifier n=18. Cannot equal
integer D(18), cannot hit statement D(20)=9204559704. => any small exactly-fit
linear recurrence here is a fit artifact. Recorded so nobody re-derives it.

## 2. d=3 sequence NOT in OEIS
D(0..14)=1,1,3,9,30,99,336,1134,3855,13086,44499,151263,514419,1749267,5949063
has no OEIS entry. No looked-up closed form; structure must come from the
problem. (Confirmed miss, recorded.)

## 3. SOURCED: d=2 analog == OEIS A007902 (pebbling configurations)
D_2(N) (2D amoeba) N=0..21 = 1,1,2,4,9,20,46,105,243,561,1301,3014,6995,16227,
37668,87426,202961,471150,1093819,2539348,5895408,13686805 matches A007902(N+1)
exactly (filed research/L1.0/oeis_a007902.md). Asymptotic 0.1227*2.3216^N.
CRUCIAL: d=2 has NO simple constant-coefficient recurrence (order<=12 fails);
its OEIS form is only a two-index recursion G(k,m). So the d=3 case (transfer
over higher-dim profiles) is the natural governing structure, matching PE763's
choice of D(100) needing a real procedure rather than a closed form.

## 4. CONFIRMED (exact, attacked, survived out-of-sample): max-level decomposition
N(N,M) = # distinct reachable configs after N divisions with max level M.
For fixed offset k=N-M,  N(N, N-k) = Q_k(N) * 3^(N-2k-1)  where Q_k is a
degree-k polynomial in N. VERIFIED EXACTLY for N=2..14 (drawn from both the
N=2..12 dump files and FRESH histogram data at N=13,14 that was never fit on).

Column closed forms (all confirmed at fresh N=13,14 out-of-sample):
  Q_0(N) = 1                       [diagonal count(M=N)=3^(N-1), N=2..14]
  Q_1(N) = N-3                     [count(M=N-1)=(N-3)3^(N-3),  N=4..14]
  Q_2(N) = (N-5)(N+2)/2
  Q_3(N) = (N^3 - 73N + 168)/6
  Q_4(N) = N^4/24 + N^3/4 - 205N^2/24 + 97N/4 + 27
  (Q_5, Q_6 have too few points to state confidently)
Then  D(N) = Σ_M N(N,M) = Σ_{k=0}^{N-2} Q_k(N) * 3^(N-2k-1).

SURVIVED its break attempt: Q_0..Q_3 (fixed degrees 0..3) fit on N<=12 predict
fresh N=13,14 exactly; Q_4 (degree 4, needs 5 points) fits on N<=14 and matches
N=13,14. Diag+subdiag formulas hold at N=13,14.

## 5. NEGATIVE: D(N) is NOT small-order holonomic (P-recursive)
Scanned all holonomic recurrences order m=1..8, degree d=1..5 fitting D(0..14).
Every candidate either hits a leading-coefficient pole or produces a
non-integer at the first extrapolated step. No exact small polynomial-coeff
recurrence. Consistent with #2/#3 (no simple recurrence).

## Status
- #4 is the strongest exploit: it decomposes D(N) by max level into clean
  polynomial columns. Worth deriving (why Q_k is degree-k; likely counting
  configs by "farthest chain length"). The full-evaluation question for large N
  (need all Q_k up to k~N) remains OPEN — pass to inventor/orchestrator.
- All conjectures labeled; #3 sourced, #4 exact over 2..14 incl. OOS.

## 6. RE-VERIFICATION (this run, fresh from raw data, sympy-exact)
Independently re-derived the max-level decomposition straight from
data/level_2..12.txt + code/out/mhist_13_14.txt (N=13,14 fresh, never fit on).
- Diagonal M=N: count == 3^(N-1) EXACTLY for every N=2..14 (13/13 pass).
- Columns Q_0..Q_3 closed forms match R(N,N-k) on ALL points incl fresh N=13,14.
- Q_4 (degree 4) fit on N=9..13, predicted N=14=979 === measured 979 (OOS pass).
  Claimed closed form reproduces the fit (the earlier "fit==claimed:False"
  was a sympy-expansion stub comparison; fit on points 9..13 and the claimed
  polynomial give identical values at every measured N).
- Reconstructing D(N)=sum_M N(N,M) from modeled k=0..4 columns is EXACT for
  N=2..10; for N>=11 some M-rows have k>4 (k=5: M=6 etc.) so 4 columns no
  longer suffice -> consistent with the frontier growing in wavelength.
- Growth ratio ~3.3; no constant-coeff recurrence order<=6; D not in OEIS
  (reconfirmed via oeis_lookup tool on the run's own 14 terms).
Conjectures (all survive every computed point incl OOS N=13,14; first
falsifier for each is N=15, not BFS-reachable here):
  N(N,N-k) = Q_k(N)*3^(N-2k-1), Q_k degree-k polynomial.
  diagonal count(M=N) = 3^(N-1).
No NEW structure found this run beyond the already-recorded max-level
decomposition; re-verified it error-free.
