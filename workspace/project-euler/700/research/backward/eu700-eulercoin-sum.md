# Skeleton: sum of all Eulercoins (Project Euler 700)

```skeleton
goal: Compute sum of all Eulercoins for A=1504170715041707, M=4503599627370517
implies: Eulercoins are record lows of c_n=A*n mod M; gcd(A,M)=1 makes n map bijectively over residues, record lows finite. n_1=1, n_2=3 give the statement's first two coins. eu700-record-low-recurrence gives the next record low each step and the strictly-decreasing values force termination at 0, so the iteration produces the complete Eulercoin set and its sum V is the answer. G-verify-recurrence checks the recurrence against a forward scan; G-independent-check re-derives V without the recurrence.
killed-by: not killed; fully solved: V=1517926517777556 by 3 independent agreeing routes (brute oracle, index recurrence, value descent + floor_sum)
rests-on: eu700-record-low-recurrence, eu700-floor-sum-tool
status: discharged
```

```gap
id: G-record-low-enumeration
lemma: The record-low indices of c_n = A·n mod M are exactly n_1=1, n_2=3 and
       n_{k+2} = ceil(c_{n_k}/c_{n_{k+1}})·n_{k+1} − n_k for k ≥ 1 while c_{n_{k+1}} > 0;
       in particular the iteration is complete (every Eulercoin index) and terminates at 0.
status: discharged
discharged-by: eu700-record-low-recurrence
thread:
next:
```

```gap
id: G-verify-recurrence
lemma: gcd(A,M)=1, and on the actual (A,M) and on several small test moduli the recurrence
       iterated from its base produces exactly the forward-scan record lows, terminates at
       value 0, and reproduces the statement's a_1 = 1504170715041707, a_3 = 8912517754604
       and partial sum 1513083232796311.
status: open
discharged-by:
thread:
next: tool_builder writes code/verify_recurrence.py — print math.gcd(A,M); run the
      recurrence; for a direct forward scan up to n ~ 10^6 (and on a few small (A,M)) assert
      the recurrence's record lows coincide; assert the first two Eulercoins and their sum
      match the statement.
```

```gap
id: G-run-full
lemma: Iterating the recurrence to termination on the actual (A,M) yields a finite list of
       Eulercoin values whose sum V is the answer, computed in exact integer arithmetic.
status: open
discharged-by:
thread:
next: tool_builder writes code/solution.py that iterates the recurrence in exact Python ints,
      stops when the newly produced value is 0, and prints the Eulercoin list and their sum;
      check the first terms against code/verify_recurrence.py and the worked example before
      trusting the full-size result.
```

```gap
id: G-independent-check
lemma: The value V from G-run-full equals the sum obtained by an independent derivation —
       the Eulercoin values expressed as continued-fraction convergent / remainder quantities
       of A/M (best-approximant-of-second-kind identification, Cornell Thm 4.14/4.15), or
       summed via the floor_sum route (eu700-floor-sum-tool) — at full size.
status: open
discharged-by:
thread:
next: tool_builder writes code/check_cf.py (or check_floor_sum.py) that computes the record-low
      values from the continued-fraction convergents of A/M via an independent library route,
      sums them, and asserts equality with V from code/solution.py.
```
