# Index — code/pattern

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `mdist.py` | Counts reachable configs at each N by max level M from the /workspace/data/level_N.txt feature dumps, where M is read as the second field of each line, printing the M-distribution per N. Used to study how the structural parameter M grows with N. |
| `recur_deadend.py` | Characterizes the order-7 constant-coefficient recurrence (3D[n]=9D[n-1]+12D[n-2]-17D[n-3]-30D[n-4]-31D[n-5]+63D[n-6]) fitted over D(0..14): shows its first extrapolated term is non-integer (fails at n=18), so the recurrence can never reproduce D(20)/D(100). Records this as a dead end. |
| `recur_integral.py` | Second check of the same order-7 recurrence: extrapolates from the fitted 15 terms through n=200 and confirms it fails integrality at the first extrapolated term (n=15), so no integer linear recurrence of this order extends the sequence. Independent route to the dead-end conclusion in recur_deadend.py. |
| `recur_test.py` | Tests the conjectured order-7 linear recurrence against the held-out statement values D(20)=9204559704 and D(100) mod 10^9=780166455, and prints predicted D(15..30) and D(10000). Establishes the recurrence does NOT match the statement (the fitted recurrence is not the answer). |
