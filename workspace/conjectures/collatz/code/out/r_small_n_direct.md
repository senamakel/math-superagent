# Verified: every 1 <= n <= 2^20 reaches 1 under the Collatz map

Program: `code/r-small-n-direct/verify_small.py`, run
`python3 code/r-small-n-direct/verify_small.py > code/out/r_small_n_direct.txt`
at workspace root. Raw output: `code/out/r_small_n_direct.txt`.

Bears on: `code/lean/Lib/collatz_conjecture.lean`,
`Cited.collatz_conjecture` — `∀ n > 0, ∃ k, C^k(n) = 1` with
`C(n) = n/2` even, `3n+1` odd. This run is finite, exact evidence for the
instances `n <= 2^20` of that statement, not a proof for all `n`.

Method: naive direct simulation one step at a time (visited set, step cap
10^6 — the same semantics as the oracle `code/brute.py`) plus a dict
memoising the verdict for every decided value, so no orbit is ever walked
twice. The single source for the map C and for the naive oracle is
`code/brute.py`, imported as `brute`, so the two methods share one
definition of a step. Exact integer arithmetic throughout; the verdicts
True / False / None mean reached 1 / non-trivial cycle (a counterexample) /
cap exhausted (unknown).

Results, as printed:

```
worked example (code/brute.py): orbit of 1 (4 terms) = [1, 4, 2, 1], matched: True
  tiny orbits n = 1..10, 27: reaches 1 = True for all 11
cross-check vs code/brute.py orbit_reaches_one on n=1..1000: AGREE
count of n checked: 1048576
sweep wall time: 1.327 s
VERDICT: ALL n <= 2^20 REACH 1
```

What each number establishes:

- The worked example `1 -> 4 -> 2 -> 1` reproduced, and the 11 tiny orbits
  (n = 1..10, 27) all reach 1 — the oracle's own check that it implements
  the statement as `problem.md` states it.
- The cross-check on n = 1..1000 (0 mismatches) compares the memoized
  method against the independent naive oracle `orbit_reaches_one` on the
  same n: it is what makes the memoisation trusted, not the naive walk.
- The sweep checked all 1 048 576 values `1 <= n <= 2^20`; every verdict
  was True; none returned False (no non-trivial cycle below 2^20) and none
  returned None (no divergence observed). Wall time 1.327 s is a property
  of this container, not of the statement.
- A non-trivial cycle would print `FAIL: n=... verdict=False` — none did.
  `False` would have been a genuine counterexample to the conjecture, not
  a numeric artefact.

What a larger bound would settle, before trying one: raising the bound from
2^20 would only extend the same finite verification to larger n — it cannot
touch the conjecture, whose obstruction is the unbounded case (divergence or
a cycle with arbitrarily large elements), so this run stops at 2^20 as
instructed. The published computational frontier (all n up to ~2^68 or
further, via accelerated maps) is far beyond anything direct simulation of
`C` could reach, so a bigger direct sweep adds evidence, not a proof.

```claim
id: r-small-n-direct-2^20
status: checked
statement: every integer n with 1 <= n <= 2^20 reaches 1 under C(n) = n/2
  if n even, 3n+1 if n odd; equivalently the finite instances n <= 2^20 of
  Cited.collatz_conjecture hold, with no non-trivial cycle and no observed
  divergence among them.
evidence: code/out/r_small_n_direct.txt (exit 0; cross-check on n=1..1000
  AGREE against the naive oracle code/brute.py; count checked 1048576;
  verdict ALL n <= 2^20 REACH 1). Oracle semantics reproduced the worked
  example 1 -> 4 -> 2 -> 1 and n = 1..10, 27 in
  code/out/brute_worked_examples.txt.
status-note: verified computation, finite range only; proves nothing about
  n > 2^20 and nothing about the conjecture in general.
```
