# Oracle runs: naive exact Goldbach checker on the worked examples

Statement the runs bear on: every even n > 2 is a sum of two primes
(binary Goldbach, problem.md), formalised in code/lean/Lib/Statement.lean
and witnessed for n ≤ 50 in code/lean/Lib/GoldbachOracle.lean.

## `code/brute.py` (the oracle demonstration) — command and output

Command: `timeout 60 python code/brute.py` — exit 0.

The oracle functions themselves live in `code/lib/goldbach.py` (one source
of truth: `is_prime`, `goldbach_partitions`, `satisfies_goldbach`,
`verify_partitions`, `HAND_COUNTS_4_50`); `brute.py` is the demonstration
script that runs them against the problem's worked examples.

Output, verbatim:

```
=== Worked examples from problem.md ===
example 1: '4 = 2 + 2 is a valid representation'
  partitions(4) = [(2, 2)]
  satisfies_goldbach(4) = True
  agree? True
example 2: 'n = 2 has no representation (1 is not prime)'
  partitions(2) = []
  satisfies_goldbach(2) = False (excluded by n > 2, not a counterexample)
  agree? True
example 3: '1 is not prime'
  is_prime(1) = False
  agree? True

=== Hand-checked sanity sweep (same scale as the examples) ===
  every even n in [4, 50] satisfies Goldbach? True
  hand-counted partition numbers 4..50 all reproduced? True

ALL WORKED EXAMPLES MATCHED: True
```

## The three worked examples of problem.md, identified

1. "4 = 2 + 2 is a valid representation" — p, q need not be distinct.
2. "n = 2 has no representation (1 is not prime) and is excluded by
   hypothesis, not a counterexample" — the `n > 2` hypothesis.
3. "1 is not prime" — the reason 2 = 1 + 1 fails.

## Independent cross-route (sympy)

Command: sympy.isprime enumeration compared against `goldbach_partitions`
for every even n in [4, 198] — `oracle == sympy-enumeration for every even
n in [4, 198]: True` (exit 0). Second check: sympy independently
reproduces the whole `HAND_COUNTS_4_50` table — `True` (exit 0).

## Kernel-checked counterpart (Lean)

`code/lean/Lib/GoldbachOracle.lean` pins one witness pair per even n in
[4, 50] and proves, kernel-checked, that each is a genuine prime-sum pair
and that every even n in [4, 50] is a sum of two primes:

```
$ lean-verdict /workspace code/lean/Lib/GoldbachOracle.lean   # exit 0
outcome: verified
'Goldbach.witness_works' depends on axioms: [propext, Classical.choice, Quot.sound]
'Goldbach.all_even_4_to_50_goldbach' depends on axioms: [propext, Classical.choice, Quot.sound]
```

(verdict record also at code/out/lean/, with the sanity file
`GoldbachSanity.lean` likewise `verified`; the conjecture statement file
`Statement.lean` is `failed` by design — its single `sorry` is the open
conjecture itself.)

## What was NOT done

No full-size brute force: the literature's verification frontier is
~4·10^18 and this naive method is O(n·√n) per n — pointed at that bound it
is defeated by design. The oracle stays at the worked-example scale
(n ≤ 200) where it is the reference the real method is checked against.

```claim
id: oracle-brute-reproduces-worked-examples
statement: code/lib/goldbach.py's is_prime / goldbach_partitions /
  satisfies_goldbach reproduce all three worked examples in problem.md
  (4 = 2 + 2 valid; n = 2 has no representation and is excluded by
  hypothesis, not a counterexample; 1 is not prime), and reproduce the
  hand-counted partition-number table HAND_COUNTS_4_50 for even n in
  [4, 50].  The same witness pairs are kernel-checked in
  code/lean/Lib/GoldbachOracle.lean (lean-verdict: verified).
hypotheses: trial-division primality, exhaustive p in [2, n//2] search.
holds-here: yes, at the worked-example scale only.
evidence: brute.py output above (exit 0); independent sympy.isprime
  enumeration agreeing for every even n <= 198; lean-verdict exit 0 on
  GoldbachOracle.lean and GoldbachSanity.lean.
search-frame: swept every even n in [4, 50] by the naive oracle (24 cases,
  all satisfy Goldbach, counts = hand table); every even n in [4, 198] by
  the sympy cross-route, and the witness pairs for [4, 50] by the Lean
  kernel.  This lies far inside the published exhaustive regime
  (Oliveira e Silva–Herzog–Pardi ~4e18, per problem.md's recalled record);
  nothing here extends the verified frontier.
status: checked
falsified-by: any even n <= 50 whose partition count differs from the hand
  table, any disagreeing sympy route result, or a failed Lean kernel check
  of the witness theorems.
```
