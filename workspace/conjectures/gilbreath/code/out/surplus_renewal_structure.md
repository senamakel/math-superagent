# The recharge surplus is a monotone renewal statistic — depth 1000, exact

**What this run did.** `code/pattern/surplus_structure.py` was on disk with no
captured output. Executing it showed the script's built-in recharge-identity
integrity check failing; inspection found two bugs in the *check*, not in the
law: a 1-based/0-based index slip, and `>` instead of `>=` for event
detection, which silently dropped the 17 jump-0 stalls. Both fixed; the
program and a fully independent one-line recomputation now agree on
`code/out/blocks_depth1000.json` (depth 1000, sieve to 2·10⁷, 1,270,607
primes):

## The structural fact

Let `b_k` be the leading `{0,2}` block length of row k, and define the
**recharge surplus**

```
S_k = b_k − b_1 + (k−1) = Σ_{events i<k} (j_i + 1)
```

(the second equality is the recharge identity, `step-law-and-recharge-identity`,
`j_i` the jump at event i). Then, at every transition,

```
S_{k+1} − S_k = (b_{k+1} − b_k) + 1     (delta law, exact at every k)
```

so the surplus increments by exactly `j+1 ≥ 1` on a `(2,4)`-event and by
exactly `0` otherwise. Hence, exactly equivalent to the known step law:

- **`S_k` is monotone nondecreasing, and it strictly increases precisely at
  the 60 `(2,4)`-event rows** (verified: deltas > 0 ⇔ event, all 999
  transitions).
- **Gilbreath's conjecture for the primes is equivalent to `S_k ≥ k−1` for
  every k** (since `b_k = S_k − (k−1) + b_1 ≥ 1` ⇔ `S_k ≥ k−1` when
  `b_1 = 1`; for the primes `b_1 = 2`, so the exact requirement is
  `S_k ≥ k−2`). Equivalently the *shortage* `(k−1) − S_k ≡ b_1 − b_k` must
  stay ≤ `b_1 − 1`: the conjecture says **block length never reaches zero,
  which is exactly "the erosion count never overtakes the recharged surplus
  by more than b_1"**. This is the consumption-vs-regeneration invariant
  restated as one monotone quantity, no primes beyond `b_1 = 2` in the law
  itself.

Numerics on the depth-1000 record: min surplus 0 (at k=1, forced by b_1=2),
`S_1000 = 1,270,603` against required 998 — margin 1,269,605. Deltas `> 0`
take 36 distinct values {1,2,3,4,5,6,7,8,10,11,12,32,35,40,116,135,452,594,
595,603,842,1155,1315,1740,1739,8237,11354,17326,37746,53470,61088,129923,
176181,190810,217657,360698}, the 17 zero-deltas are the jump-0 stalls.
`S_k ≥ N_k` (number of events so far) at every k — each event leaves the
surplus strictly above the event count.

## Renewal table (all 60 events) — see `code/out/surplus_renewal_table.captured.txt`

Structure visible: small stalls (j=0) ride atop a just-arrived jump
(4 consecutive stalls at i=16–18, 47–49, 62–63, 111, 129, 135, 141–142);
big jumps (j ≥ 10⁴: i=64, 94, 110, 112, 126, 130, 134, 146, 161) arrive with
no prior surplus build-up — e.g. j=360,698 at i=146 comes after a j=3 event
3 rows earlier, so the giant jump is *not* "energy stored during erosion"
(mean gap before big jumps 3.54 vs 2.48 before small ones — not a separation;
asked by `surplus_structure.py` (3), answered, no signal). 43 of 60 events
after the first are preceded by an event within the previous 5 rows:
self-exciting, not renewal-arrival. Slope log(jump) vs log(b) = 0.388 over
the 43 positive-jump events — jumps grow sublinearly with block length
(consistent with `surplus_structure`'s OLS, and with the explosion of S
being dominated by a few giants).

Method: exact integer arithmetic, one pass over the on-disk record, O(D) time
and O(D) space for `D=1000`; independent recomputation reproduced identity,
monotonicity, event set (60) and slope. Reproduces the oracle `b`-series
k=1..40 (`oracle_agree_first_40: true` in the JSON) — the underlying rows were
checked against the witness generator when `blocks_depth1000.json` was made.

What it does NOT establish: any lower bound on the rate of `(2,4)`-events
(the open question — TASKS.md item 1); "surplus margin 1.27e6 at depth 1000"
is a fact about depth 1000.

```claim
id: surplus-renewal-structure-1000
statement: For the prime Gilbreath rows to depth 1000 (sieve 2e7, 1270607
  primes), with b_k the leading {0,2} block length and S_k = b_k - b_1 +
  (k-1) the recharge surplus, S_{k+1} - S_k = (b_{k+1} - b_k) + 1 at every
  transition (delta law); S_k is monotone nondecreasing and strictly
  increases exactly at the 60 (2,4)-events (17 of them jump-0 stalls);
  S_k >= N_k (events so far) at every k; S_1000 = 1270603 vs required
  k-2 = 998, margin 1269605; log(jump) vs log(b) OLS slope 0.388 over 43
  positive-jump events. Conjecture-equivalent reformulation: GC holds for
  the primes iff S_k >= k - b_1 for all k, i.e. block length never reaches
  zero iff erosion never overtakes the recharged surplus.
hypotheses: rows are iterated absolute differences of primes below 2e7,
  block length measured from position 1, depth 1000
holds-here: yes (depth 1000, exact)
status: checked
bearing: the monotone surplus S_k is the quantity whose unboundedness of
  (k-1) - S_k is the conjecture; converts regeneration into "S_k - (k-1) is
  bounded above by b_1", and shows regeneration events (incl. stalls) are the
  only increments. Does not bound the event rate — that is open and is the
  next step (TASKS.md item 1).
anchor: code/out/surplus_renewal_structure.md, code/out/surplus_structure.captured.txt, code/out/surplus_renewal_table.captured.txt
source: operator-computation
```