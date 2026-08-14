# Oracle calibration — run brute.py and capture it

```thread
question: Is code/brute.py a trusted oracle for this problem, i.e. does a captured run reproduce the GOAL.md calibration on the 7-vertex graph (11 exact unit edges, 4-colourable SAT witness, 3-colourable UNSAT) in exact arithmetic?
status: checked
rests-on: code/brute.py (exact Q(sqrt3,sqrt11) edge certifier + complete symmetry-broken k-colouring test); problem.md's 7-vertex worked example; code/out/brute.captured.txt (sha256 f73f3724bc0e7855c574daae588cddbce71f5feaa7edbbd6febbea93bcc574dc) with 11 exact edges, witness, not-3, CALIBRATION PASSED, EXIT_CODE=0
blocked-by: nothing
next: the oracle is trusted; it has since been exercised at increasing size by the Minkowski-power census (A^k, k=2..5, up to 301 vertices / 1375 edges, two independent edge certifications and two agreeing complete colouring tests) and by the lattice-patch census (up to 2601 vertices). New measurements may proceed against claims G-five-chromatic-graph / G-exhaust with the calibration standing.
```

## Why this thread exists

Directive 2: code/brute.py has never been run with captured output anywhere in
`code/out/`. `code/out/commands.log` shows only a `timeout 120` run, and
`code/out/oracle_calibration.md`'s "verbatim" edge list (e.g. `edge 0-1  edge
0-2 ...`) does not match `brute.py`'s actual print format (`edge 0-1: |p0 - p1|^2
== 1  exactly`). The existing `G-oracle-calibrated` claim in `research/CLAIMS.md`
is therefore not accepted as calibration.

## Acceptance condition

`code/out/brute.captured.txt` exists, contains 11 exactly-certified unit edges,
`4-colourable? True` with a witness, `3-colourable? False`,
`CALIBRATION PASSED`, and `EXIT_CODE=0`. Nothing new is measured until this
holds.
