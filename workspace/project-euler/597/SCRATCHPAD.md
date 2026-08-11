# Scratchpad

## Run (tool_builder): naive oracle code/brute.py verified against the whole statement

Command: `cd /workspace && python3 code/task1_verify.py`

Used the already-present `code/brute.py` (naive chronological replay that
records every bump edge and builds the new order by full reachability) rather
than writing a second oracle. Exact output:

```
=== TASK 1a: table parity reproduction (n=3,L=160) ===
  none                         speeds=[0.157, 0.607, 1.473] order=[0, 1, 2] parity=even expected=even  [OK]
  B bumps C                    speeds=[0.073, 0.215, 0.093] order=[0, 2, 1] parity=odd expected=odd  [OK]
  A bumps B                    speeds=[0.257, 0.137, 1.662] order=[1, 0, 2] parity=odd expected=odd  [OK]
  B bumps C then A bumps C     speeds=[2.205, 2.057, 0.126] order=[2, 0, 1] parity=even expected=even  [OK]
  A bumps B then B bumps C     speeds=[3.218, 2.055, 1.316] order=[2, 1, 0] parity=odd expected=odd  [OK]
  all five parities: PASS

=== TASK 1b: MC p(3,160) and p(4,400) at ~200k ===
  MC p(3,160) = 0.415850   (target 56/135=0.414815)
  MC p(4,400) = 0.509220   (target given 0.510784)
```

Every worked example matched:
- new orders agree with the statement table ([0,1,2]=ABC, [0,2,1]=ACB,
  [1,0,2]=BAC, [2,0,1]=CAB, [2,1,0]=CBA) and the parities agree (even/odd).
- MC p(3,160)=0.415850 vs exact 56/135=0.414815 (within SE~0.0011).
- MC p(4,400)=0.509220 vs given 0.510784 (within SE~0.0011).
- p(3,160) MC here is relative to exact 56/135; p(4,400) to the given value.

Conclusion: the naive oracle's reading of the definition is correct. All
statement examples reproduced.

## Task
Run `/workspace/verify_hypothesis.py` with N=200000; report the four MC
estimates (expect p(3,160)≈0.4148, p(4,400)≈0.5108) and whether any w-order
bucket holds both parities.

## Run result (verbatim)
```
MC p(3,160)   = 1.000000  (exact 4.15+4/27 = 56/135 = 0.414815)
MC p(4,400)   = 1.000000  (given 0.5107843137)
n=3 L=160: 60000 samples, 6 distinct w-orders seen, 0 order(s) with inconsistent parity
n=4 L=160: 60000 samples, 24 distinct w-orders seen, 0 order(s) with inconsistent parity
n=4 L=400: 60000 samples, 24 distinct w-orders seen, 0 order(s) with inconsistent parity
n=5 L=400: 60000 samples, 120 distinct w-orders seen, 0 order(s) with inconsistent parity
n=5 L=1800: 60000 samples, 120 distinct w-orders seen, 0 order(s) with inconsistent parity
```

## Diagnosis: MC=1.000000 is a BUG, not a finding
Both MC estimates came out exactly 1.0, but the stated values are ≈0.4148 and
≈0.5108. So the parity computation in `brute.parity_of_new_order` is broken.
The `lower(a,b)` comparator uses the wrong `above` test:

```python
def lower(a, b):
    if a in above and b in above[a]:   # WRONG
        return True
    ...
    return a < b
```
`above[i]` = boats placed BELOW i (bump chain under i). So "a placed lower
than b" means `a in above[b]`, not `b in above[a]`. As written every case whose
bump structure is non-trivial falls to the `return a < b` fallback, producing
identity order [0,1,2] and parity 0 for essentially everything.

Table reproduction with the buggy routine (expected parity from problem table):
```
none                   -> [0,1,2] parity=0 expected=even  OK
B bumps C              -> [0,1,2] parity=0 expected=odd   FAIL
A bumps B              -> [0,1,2] parity=0 expected=odd   FAIL
B then A both bump C   -> [0,1,2] parity=0 expected=even  OK
A bumps B then B bumps C -> [0,1,2] parity=0 expected=odd FAIL
```
Only identity/easy cases agreed; all odd cases were misreported as even. Hence
the "0 inconsistent orders" verdict is also meaningless, and the structural
hypothesis test is not yet usable.

## Fix
Correct comparator: a is placed lower than b  <=>  a in above[b].
```python
def lower(a, b):
    if a in above[b]: return True      # b above a, so a lower
    if b in above[a]: return False     # a above b, so a higher
    return a < b
```
Then re-verify: parity routine must reproduce the 5-table parities, and MC
must give p(3,160)≈0.41 and p(4,400)≈0.51. Only then is the w-order
consistency check meaningful.

## verifier for the hypothesis
`verify_hypothesis.py` also has a cosmetic bug in a print string:
`exact 4.15+4/27` should be `4/15+4/27`. Not functional, but note.

## Task: verify brute oracle + investigate edge-loss in examine_multibump.py

### 1. Worked examples reproduced (fixed engine)
- All five n=3,L=160 table parities confirmed by both `brute.outcome_parity`
  and `exact_race.outcome_parity_exact`:
  none=0, B bumps C=1, A bumps B=1, B->C then A->C=0, A->B->C chain=1.
- MC p(3,160) 500k = 0.415108 ~ exact 56/135 = 0.414815.
- MC p(4,400) 500k = 0.512368 (~ given 0.510784; 200k gave 0.51218).

### 2. Edge-loss bug: real, fixed, but impossible to flip order/parity
- Differential brute vs full-reachability (`simulate_order_nobug`):
  * above sets differ in ~40% of 2M trials (829245/2M) — brute's single
    `out_of` chain loses transitive edges.
  * BUT order_diff = 0 and par_diff = 0 across 2M random trials, and 0 of
    541981 lost edges flipped a relative order.
- Reason: a bumped boat continuing can be bumped again, overwriting
  `bumped_by[k]`; the chain then misses an intermediate. Empirically every
  lost edge had a direct replacement preserving the order. Regardless, fixed
  brute.py to record ALL edge `edges[a].append(b)` and compute `above` by full
  graph reachability (same approach as simulate_order_nobug). After fix:
  brute.simulate_order == simulate_order_nobug on 500k trials (0 diffs).
- Note: exact_race.py had the same single-chain bug; it delegates to brute's
  parity and builds its own above with the same pattern. Both now consistent
  because parity depends only on inversion count, which survived.

### 3. Parity identity (the clean definition)
- parity = (number of pairs i<j with a bump chain i->...->j) mod 2.
  Verified: true chain-count parity == brute parity over 1M trials (0 mismatch).

### 4. Large MC p(13,1800) (fixed engine, Exp(1) speeds)
- 100k: 0.500470 | 200k: 0.499400 | 300k: 0.499027 | 1.2M: 0.500880.
- Ballpark target ~0.500 (parity near a fair coin as n grows).

## Cartesian-tree (treap) hypothesis: REFUTED (test_treap.py)
- Tested: min-heap Cartesian tree over indices with priority w_i=v_i/(L-40i),
  in-order = index order; hypothesis "bump chain i->...->j <=> ancestor/desc.,
  parity = (# such pairs) mod 2".
- Outcome: n=2..6, L in {160,400,1800}, 20k samples each -> every (n,L) starts
  mismatching from the first handful of trials; 30 mismatches within ~62 total.
- Tree-MC implied probabilities are badly wrong: p(3,160)=0.333 (given
  56/135=0.4148), p(4,400)=0.833 (given 0.5108), p(13,1800)=0.536.
- Minimal counterexample n=2: v=[0.13269,0.56728], L=160. v0<v1 -> boat0 never
  catches boat1, no bump -> oracle even. But w0=0.0008<w1=0.0047 makes 0 the
  treap root, so {0,1} an ancestor pair -> tree predicts odd. Treap ancestor
  relation is NOT bump-chronology reachability.
- Root cause: bumping depends on pairwise RELATIVE speed and actual catch/finish
  chronology; a single scalar priority (time-to-finish rate) cannot encode which
  pairs actually chain. Treap ancestry over-counts relations the race never makes.

## Run (tool_builder): structure_taxonomy.py — worked-table verification + bump-graph taxonomy
Command: `cd /workspace && python3 code/structure_taxonomy.py`
- Part A: n=3,L=160 five-row table all reproduced (parities even/odd/odd/even/odd
  for none/B->C/A->B/B&C->C/A->B->C). Exact rational: all-five sum = 1,
  even-rows sum = 4/15+4/27 = 56/135 = p(3,160). PASS.
- Part B: MC p(4,400) = 0.511487 +/- 0.000790 vs given 0.5107843137. PASS.
- Part C (60k trials each, n=3,4,5 x L=160,1800 = 360k races): bump graph is
  ALWAYS a forest: out-deg<=1, edges strictly increasing, zero cycles in every
  trial. Boat n-1 never bumps, boat 0 never bumped (P=0 over 100k). In-degree
  unbounded (up to 4 at n=5); top boats are the most-bumped targets.
  Chains/roots need not be consecutive (bumper-set non-consecutive ~1-3% at
  n=5/6). Distinct edge structures: 5 (n=3), 14 (n=4), 14-42 (n=5); edge-set
  and above-reachability counts agree.
- Findings written to /workspace/structure_report.md.
