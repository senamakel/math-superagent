# Index — code/pattern

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `columns.py` | Verifies the column conjectures for the N(N,M) table (configs by max level M): tests whether N(N,M) = Q_k(N)*3^(2M-N-1) with Q_k a polynomial of degree k=N-M, computing v*3^(N-2M+1) as exact rationals and checking its finite differences. Extends the diagonal/sub-diagonal/offset study of diagonal.py and offsets.py. |
| `d2_oeis.py` | Verifies the run's 2D amoeba sequence D2(N) (N=0..21) against the published OEIS A007902 pebbling-configurations terms, confirming D2(N)=A007902(N+1) on every term and printing the last few growth ratios against Knessl's asymptotic d=2.3216. The program backing the d2d-equals-a007902 identification claim. |
| `diagonal.py` | Checks the M=N diagonal conjecture for PE763's structural parameter M (max level): tabulates count of configs with max level M=N against 3^(N-1), plus the near-diagonal M=N-1 column, reading the /workspace/data/level_N.txt feature dumps. |
| `holonomic_fit.py` | _(undescribed)_ |
| `mdist.py` | Counts reachable configs at each N by max level M from the /workspace/data/level_N.txt feature dumps, where M is read as the second field of each line, printing the M-distribution per N. Used to study how the structural parameter M grows with N. |
| `offsets.py` | Extracts the N(N,M) table (configs by max level M) from data/level_N.txt and examines fixed-offset diagonals M-N=k: prints v(N,N+k)/3^(N-1) for each N to look for a pattern N(N,N+k)=poly(N)*3^(N-1). Structural probe extending the diagonal study of diagonal.py. |
| `poly_test.py` | Tests whether D(N) = 3^(N-1)*P(N) for a polynomial P of fixed degree: computes R(N)=D(N)/3^(N-1) as exact rationals and checks whether its finite differences vanish (constant) at some order. Decisive structural test: if R(N) is a polynomial, D(N) has all characteristic roots equal to 3. |
| `q_array.py` | Extracts the full triangular array Q_k(N) = N(N,N-k)/3^(N-2k-1) from the data/level_N.txt feature dumps and prints each offset column k as a sequence of exact rationals, for OEIS-style closed-form hunting on the N(N,M) table. |
| `q_fresh_test.py` | _(undescribed)_ |
| `q_verify.py` | Verifies exact closed forms for the offset columns of the N(N,M) table: Q_0=1, Q_1=n-3, Q_2=(n-5)(n+2)/2, Q_3=(n^3-73n+168)/6 against N(N,N-k)=Q_k(N)*3^(N-2k-1) over the computed range N=2..12, then reconstructs D(N) as the sum of the modeled columns to confirm the submodel matches the true D(N). |
| `recur_deadend.py` | Characterizes the order-7 constant-coefficient recurrence (3D[n]=9D[n-1]+12D[n-2]-17D[n-3]-30D[n-4]-31D[n-5]+63D[n-6]) fitted over D(0..14): shows its first extrapolated term is non-integer (fails at n=18), so the recurrence can never reproduce D(20)/D(100). Records this as a dead end. |
| `recur_integral.py` | Second check of the same order-7 recurrence: extrapolates from the fitted 15 terms through n=200 and confirms it fails integrality at the first extrapolated term (n=15), so no integer linear recurrence of this order extends the sequence. Independent route to the dead-end conclusion in recur_deadend.py. |
| `recur_test.py` | Tests the conjectured order-7 linear recurrence against the held-out statement values D(20)=9204559704 and D(100) mod 10^9=780166455, and prints predicted D(15..30) and D(10000). Establishes the recurrence does NOT match the statement (the fitted recurrence is not the answer). |
