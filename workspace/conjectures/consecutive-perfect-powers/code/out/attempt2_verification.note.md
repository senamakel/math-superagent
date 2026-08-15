# attempt2_verification.note.md — Tasks A and B of this attempt

Both tasks are bounded exact verifications.  Everything below was produced by
programs run in this attempt; captured outputs:

- `code/out/oracle_1e10.captured.txt` (Task A, EXIT_CODE=0)
- `code/out/dw_pairs_1e4.captured.txt` (Task B, EXIT_CODE=0)

## Task A — oracle extension to N = 10^9 and N = 10^10

Method: reuse `lib/valuation.perfect_powers_upto` / `lib/valuation.solutions`
(the exact-integer perfect-power oracle already verified through 10^8).  All
powers are built by repeated exact integer multiplication; comparisons are
exact integer equalities; no floats, no logarithms, no `math.pow` anywhere.

The oracle enumerates every perfect-power value `u = x^p <= N` (x >= 2,
p >= 2), keeps `u - 1` if it is also a perfect power `v = y^q`, and verifies
`x**p - y**q == 1` directly in integers.  Complexity: O(sqrt(N) log N) exact
big-int multiplications with ~10^5 perfect-power values at N = 10^10.

Results (from `oracle_1e10.captured.txt`):

```
N=1000000000   result=[(3, 2, 2, 3)]  OK  0.014s
N=10000000000  result=[(3, 2, 2, 3)]  OK  0.044s
independent count: perfect-power values <= 10^10 = 102230 (0.036s)
ORACLE: exactly {(3,2,2,3)} at N=10^9 and N=10^10. PASS
```

The N reached is 10^10, wall runtime 0.044 s for the oracle at that bound
(0.014 s at 10^9).  The oracle returns exactly `{(3,2,2,3)}` at both bounds.

Known-solution placement: the oracle's output set *is* the known solution,
so no lemma here eliminates it; this is a search result, not a proof for all
N (the effective bound needed for a full proof is astronomically larger).

## Task B — double-Wieferich pairs among odd primes p < q < 10000

Method: sieve the odd primes below 10^4 (1228 of them), then for each ordered
pair p < q evaluate both congruences by `pow(a, b, m)` — exact modular
exponentiation, no floats:

    q^(p-1) == 1 (mod p^2)   AND   p^(q-1) == 1 (mod q^2)

Complexity: O(pi(10^4)^2) ~ 7.5e5 modular exponentiations, 0.235 s wall.

Results (from `dw_pairs_1e4.captured.txt`):

```
odd primes < 10000: 1228
double-Wieferich pairs (both congruences) with p<q<10000:
  count = 1
  (83, 4871)
task-stated expected pairs (full, for the record):
  (83, 4871): q < 10000 -> True; in-box hit -> True
  (2903, 18787): q < 10000 -> False; in-box hit -> False
congruence check of both expected pairs (any q, exact pow):
  (83, 4871): ... BOTH -> True
  (2903, 18787): ... BOTH -> True
RESULT: in-box pairs == {(83, 4871)}
```

Placement of the expected pairs: at bound p < q < 10^4 the box contains only
(83, 4871).  The second stated pair (2903, 18787) has q = 18787 > 10^4 and is
therefore outside the box by construction; both of its congruences are
nevertheless verified True directly (independent of any bound), confirming
that the checker's definition matches the task's expectation and that the
absent hit is purely a bound artefact.  The in-box result is exactly the
single pair (83, 4871).

```claim
id: attempt2-oracle-1e10
statement: >
  The exact-integer oracle solutions(N) — enumerate all perfect-power values
  u = x^p <= N (x >= 2, p >= 2) by exact repeated multiplication, keep those
  with u - 1 also a perfect power, verify x**p - y**q == 1 in integers —
  returns exactly {(3, 2, 2, 3)} for N = 10^9 and for N = 10^10.  Wall
  runtimes 0.014 s (10^9) and 0.044 s (10^10); the independent count of
  perfect-power values <= 10^10 is 102230.  No floats anywhere.
hypotheses: >
  Bounds N = 10^9 and N = 10^10 only.  This is a computational search
  result, not a proof for all N; the bound needed for a full proof is far
  beyond any reachable search.
holds-here: yes
status: checked
bearing: >
  Extends the verified oracle range from 10^8 to 10^10; the known solution
  (3,2,2,3) is the only consecutive-perfect-power pair in this range, and
  the oracle itself returns it, so no over-elimination is possible here.
anchor: code/out/oracle_1e10.captured.txt
```

```claim
id: attempt2-dw-pairs-1e4
statement: >
  Among ordered pairs (p, q) of odd primes with p < q < 10^4, the two
  congruences q^(p-1) == 1 (mod p^2) and p^(q-1) == 1 (mod q^2) — evaluated
  by exact pow(a,b,m) — hold simultaneously for exactly one pair:
  (p, q) = (83, 4871).  The second task-stated pair (2903, 18787) lies
  outside the box (q = 18787 > 10^4) and is therefore not found at this
  bound; its two congruences are verified True directly, confirming the
  checker's definition matches the stated expectation.  Runtime 0.235 s.
hypotheses: >
  p, q odd primes, p < q < 10000.  Exact integer modular exponentiation
  only.  The statement is about this finite box, not about all primes.
holds-here: yes
status: checked
bearing: >
  The double-Wieferich condition is restrictive but not vacuous: exactly one
  ordered pair inside the box satisfies both congruences, matching the known
  minimal pair (83, 4871); the known solution (3,2,2,3) has p = 2 (even), so
  the odd-prime hypothesis excludes it rather than the congruences.
anchor: code/out/dw_pairs_1e4.captured.txt
```
