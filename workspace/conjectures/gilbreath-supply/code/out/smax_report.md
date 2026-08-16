# max|S(n)|/n trajectory for the prime fold — exact computation to N=40000

Streaming script: `code/nu2_extended/track_smax.py`
```
python code/nu2_extended/track_smax.py 40000
```
(Run also to 30000; output files `code/out/smax_trajectory_N40000_W2000.txt` and
`_N30000_W2000.txt`.)

## Definitions (exact)
- h = prime gap-parity string, h[j] = [q_{j+1} ≠ q_j mod 4]
- T(n,d) = XOR over bitwise submasks o of d of h[n-1-d+o]
- nu2(n) = #{ d in [2,n-1] : T(n,d)=1 }  (fold weight, d in [2,n-1])
- S(n) = Σ_{d=2}^{n-1} (-1)^{T(n,d)} = n - 2 - 2·nu2(n)

All arithmetic exact (Python ints). Per-n computed by the O(n log n)
submask-product SOS (`s_sos`), streamed one n at a time — no O(n²) triangle
materialised. `s_sos` is cross-checked against the direct brute submask-XOR
oracle (`s_direct`) on n=4..200 at every run (all agree) and against the
independent character-sum run form (`s_char_runs`) at spot n.

## Checkpoint numbers (max |S|/n over m∈[50,n], cumulative, MONOTONE)
| n     | pointwise \|S(n)\|/n | cum-max\|S\|/n | cum-max\|S\| | nu2 | S |
|-------|------------------|-------------|------------|-----|----|
| 1000  | 0.002000         | 0.283019    | 104        | 500 | -2 |
| 5000  | 0.020400         | 0.283019    | 225        | 2448| 102 |
| 10000 | 0.015600         | 0.283019    | 326        | 5077| -156|
| 20000 | 0.000900         | 0.283019    | 478        | 9990| 18 |
| 30000 | 0.005400         | 0.283019    | 634        | 15080| -162|
| 40000 | 0.004100         | 0.283019    | 712        | 20081| -164|

## The key structural fact — why the cumulative running max is the wrong object
The cumulative running max of |S|/n over [50,n] is **monotone non-decreasing
by construction**. It is pinned at the small-n spike n=53 (|S(53)|/53 =
15/53 = 0.283019) and can only rise thereafter; it can never "decay toward 0".
Somewhere between n=2000 and n=4000 the window of fixed width 2000 eventually
slides past the spike, which is why the trailing-window max decays while the
cumulative one does not. Reporting the literal cumulative running max would
therefore read as a permanent 0.283 plateau even though large-n excursions
shrink — a monotone object cannot show decay.

To answer the actual question (does large-n |S(n)|/n keep decaying toward 0?),
the right diagnostics are (a) pointwise |S(n)|/n, and (b) the trailing-window
max.

## Pointwise max |S(n)|/n over the tail n ≥ X (the decay diagnostic)
| X      | argmax n | pointwise max over n≥X |≈|
|--------|----------|------------------------|---|
| 50     | 53       | 0.283019               | small-n spike |
| 1000   | 1403     | 0.084818               | |
| 2000   | 2534     | 0.070245               | |
| 4000   | 5754     | 0.046924               | |
| 8000   | 8147     | 0.038174               | |
| 10000  | 12322    | 0.034248               | |
| 15000  | 15334    | 0.026086               | |
| 20000  | 20845    | 0.024322               | |
| 25000  | 27624    | 0.022951               | |
| 30000  | 30463    | 0.020057               | |
| 35000  | 36972    | 0.019258               | |
| 40000  | 40000    | 0.004100               | |

This is a clean, continued **monotone decay** of the pointwise maximum toward
0 across every tail threshold from n=1000 to n=40000. No plateau: the largest
known |S(n)|/n among all large n keeps shrinking as the floor is raised.

## What this establishes
- The literal cumulative running max of |S(n)|/n does **not** decay — it is
  pinned at 0.283019 (n=53 spike) for all n≤40000. This is a monotone-by-
  construction artifact, not evidence of a real plateau.
- The physically meaningful pointwise max of |S(n)|/n (and the roughly
  −1/2-power trailing-window max) **does keep decaying** through n=40000,
  consistent with nu2(n)/n → 1/2 pointwise (S(n)/n → 0). This is numerical
  evidence, not a proof.
- max|S(n)| itself grows slowly (104→712 from n=1000 to 40000), slower than
  n, consistent with |S|/n→0.

## Verification / negative controls
- `s_sos == s_direct == s_char_runs` at n=53,54,64,100 (all three exact routes
  agree: nu2(53)=18, S(53)=15). Independent second route used.
- The monotone-deque windowed max matches a naive O(W) scan on every point for
  N=800 (all 751 points identical).
- Cross-check vs direct oracle on n=4..200 at every run.

## Known discrepancy vs older file
`code/out/nu2_terms.txt` lists nu2(53)=19, nu2(64)=28, whereas three
independent exact routes here give nu2(53)=18, nu2(64)=27. The older file uses
a different or inconsistent convention (its nu2(64)=28 ≠ 27). This run's values
are the cross-checked ones.

## Ceiling reached
N = 40000 (streamed in ~460s; run to 30000 in ~260s). Prior run ceiling was
20000; this pushes to 2× and confirms the decay continues past it.

## Claims (directive 8)

```claim
id: smax-decay-through-40000
statement: The pointwise max of |S(n)|/n and its trailing-window max keep decaying through n=40000, consistent with ν₂(n)/n → 1/2, while max|S(n)| grows 104 → 712 from n=1000 to 40000, i.e. slower than n.
hypotheses: ceiling N = 40000; trailing window W = 2000; exact integer arithmetic; convention d ∈ [2,n−1] with S(n) = Σ_{d=2}^{n−1} (−1)^{T(n,d)} = n−2−2·ν₂(n); s_sos == s_direct == s_char_runs cross-checked.
holds-here: yes, within N ≤ 40000 and W = 2000 only — measured evidence, not a theorem.
status: measured-not-proved
bearing: Evidence for c = 1/2 in SUPPLY (ν₂(n)/n → 1/2, equivalently S(n)/n → 0), and not an argument for it.
anchor: code/out/smax_report.md (tables); code/out/smax_trajectory_N40000_W2000.txt; script code/nu2_extended/track_smax.py.
```

```claim
id: nu2-terms-superseded
statement: code/out/nu2_terms.txt is superseded: it lists ν₂(53)=19 and ν₂(64)=28, contradicting three independent exact routes here that give ν₂(53)=18 and ν₂(64)=27. Do not re-import ν₂(53)=19 or ν₂(64)=28.
hypotheses: convention d ∈ [2,n−1]; s_sos == s_direct == s_char_runs agree at n=53,54,64,100.
holds-here: yes — the three routes are this run's own exact computation.
status: checked
bearing: Prevents re-importing the superseded values; the cross-checked values (ν₂(53)=18, ν₂(64)=27) are operative.
anchor: code/out/smax_report.md "Known discrepancy vs older file"; code/out/nu2_terms.txt (superseded).
```
