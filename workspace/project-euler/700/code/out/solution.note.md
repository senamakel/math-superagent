# Project Euler 700 final answer — computed and cross-verified

`code/solution.py` runs the verified record-low recurrence `eu700-record-low-recurrence`
to termination (until the residue hits 0 at n = M). Output in `code/out/solution.txt`.

## Result (computed, exact integer arithmetic)

- Number of Eulercoins: **102**
- **Sum of all Eulercoins: `1517926517777556`**
- Last coin: index n = M = 4503599627370517, value 0 (the final Eulercoin).
- First coins reproduced: (1, 1504170715041707), (3, 8912517754604), (506, 2044785486369),
  (2527, 1311409677241), (4548, 578033868113), … — the first two sum to
  1513083232796311 (the statement's worked example).

## Independent verification already on file

- `code/out/verify_recurrence.txt`: recurrence == brute-force full scan on small moduli
  (A=7/M=17, A=3/M=23, A=5/M=13) and on the real pair through n = 10^6; gcd(A,M)=1;
  reproduces worked example exactly. ALL CHECKS: PASS.
- `code/out/verify_scan.py` (ran): forward prefix-min scan to n = 7,000,000 — covers the
  first 13 recurrence coins (largest index 6755007); forward scan MATCHES recurrence.

Second independent route (per method rule 5): the forward scan and the small-modulus
brute forces are different derivations than the recurrence and agree with it at every
index/value/coin-count they can reach. Full-size agreement at n ~ 4.5e15 is not brute-force
reachable (scanning to M would be the prohibited "cost grows with the bound" method), so
full-size verification rests on (a) recurrence vs. brute agreement on all reachable cases,
and (b) the small-modulus plus 13-coin real-pair agreement.

```claim
id: eu700-final-answer
statement: The sum of all Eulercoins of the sequence a_n = A·n mod M, A = 1504170715041707, M = 4503599627370517, is 1517926517777556, comprising 102 Eulercoins.
hypotheses: gcd(A,M)=1, 0 < A < M (holds: gcd=1).
holds-here: yes
status: checked — computed by code/solution.py (exact integers) using the recurrence eu700-record-low-recurrence, which is itself verified against brute force on small moduli and through n=10^6 on the real pair; worked example (first-two sum 1513083232796311) reproduced.
bearing: the final answer to Project Euler 700.
follows-from: eu700-record-low-recurrence
answers: compute-sum-all-eulercoins
anchor: code/out/solution.txt
```
