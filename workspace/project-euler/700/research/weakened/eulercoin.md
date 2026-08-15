```ladder
goal: Find the sum of all Eulercoins for the sequence a_n = 1504170715041707 * n mod 4503599627370517 (n = 1,2,3,...), where an Eulercoin is a term strictly smaller than every previously found Eulercoin. (Project Euler 700.)
difficulties: unbounded-n, large-coefficients, modular-wrap, index-bookkeeping, termination, no-oracle-at-size
status: open
```

The six declared difficulties, each a specific obstruction and not a topic:

- `unbounded-n` — the index n runs to ~M = 4.5e15. A forward scan computing every
  a_n is the forbidden method whose cost grows with the statement's bound.
- `large-coefficients` — A = 1504170715041707 and M = 4503599627370517. Products
  A·n (n up to M) are ~2e31, far beyond a signed 64-bit integer, so exact
  big-integer arithmetic is required and silent overflow corrupts the sum.
- `modular-wrap` — a_n = A·n mod M is not monotone in n; a new minimum arises
  only when A·n wraps past a multiple of M. The record lows therefore live in a
  quotient/remainder (Euclidean) structure, not in an ordered scan.
- `index-bookkeeping` — the sum needs only coin *values*, but finding the next
  coin needs the *index* at which the current one occurred. Each step advances n
  by a quotient, and recovering that index correctly is the off-by-one trap.
- `termination` — the coin run ends exactly at the value-0 coin (period M;
  gcd(A,M)=1 gives a_M = 0), and the sum must include every coin through 0
  without dropping or double-counting the last one.
- `no-oracle-at-size` — the full instance cannot be brute-forced, so the descent
  must be trusted on a theorem rather than checked; only the statement's first
  few coins are available as a partial oracle.

```rung
id: R-tiny-scan
statement: M = 17, A = 7 (gcd = 1). For n = 1..17 define a_n = 7n mod 17 (one full period; a_17 = 0). An Eulercoin is a term strictly smaller than every previous Eulercoin; a_1 = 7 is the first. Sum all Eulercoins over n = 1..17. Hand-anticipated coins 7@1, 4@3, 1@5, 0@17, sum 12 — code/brute.py is the oracle that confirms or corrects this.
off: unbounded-n, large-coefficients, index-bookkeeping, termination, no-oracle-at-size
stance: open
merge: Turn `index-bookkeeping` back on (to R-small-descent): replace the n=1..17 scan by the Euclidean descent and reproduce the same four coins with their indices. First move: state "next coin = current remainder mod current coin, next index = current index + quotient" and check it yields coin 4 at n=3 from coin 7 at n=1.
```

```rung
id: R-small-descent
statement: Same pair M = 17, A = 7, but produce the coin list (value with index) by the quotient/remainder descent instead of a scan: the coins are the successive remainders in the Euclidean algorithm on (M, A), each coin's index recovered from the quotients. Must reproduce the scan's coins 7@1, 4@3, 1@5, 0@17 and sum 12.
off: unbounded-n, large-coefficients, no-oracle-at-size
stance: open
merge: Turn `large-coefficients`, `unbounded-n`, and `no-oracle-at-size` back on together (to R-full-first-coins) — all three arrive with the single switch "use the real pair". First move: pin the descent as a theorem, "the Eulercoins are exactly the Euclidean remainders of (M, A)", and sanity-check it on one more tiny coprime pair such as (89, 55) so it is trusted without a full oracle.
```

```rung
id: R-full-first-coins
statement: The real pair A = 1504170715041707, M = 4503599627370517 (verify gcd = 1). Run the Euclidean descent and recover the first coins with indices; must reproduce the statement's a_1 = 1504170715041707 at n=1, the non-coin a_2 = 3008341430083414 at n=2, the second coin a_3 = 8912517754604 at n=3, and the first-two-coin sum 1513083232796311.
off: termination
stance: open
merge: Turn `termination` back on (to R-full): run the descent to the end (remainder 0) and sum every coin including the final 0 exactly once. First move: state the halting rule — the descent stops when the remainder is 0, that remainder IS the last coin (value 0 at n = M) — and count the coins so none are dropped or doubled.
```

```rung
id: R-full
statement: Project Euler 700 verbatim: A = 1504170715041707, M = 4503599627370517, a_n = A * n mod M for n = 1,2,3,...; an Eulercoin is a term strictly smaller than every previously found Eulercoin; find the sum of all Eulercoins (the run ends at the 0 coin at n = M, since gcd(A,M)=1).
off:
stance: open
merge: None — this is the goal. If it is settled the ladder is exhausted. The difficulty expected to actually bite is `index-bookkeeping` (recovering each coin's index from quotient steps); `no-oracle-at-size` is what lets a wrong index go undetected until the final sum.
```
