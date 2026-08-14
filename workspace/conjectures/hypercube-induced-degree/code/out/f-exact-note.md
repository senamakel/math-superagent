# f(n) for n = 1..4, and the cross-check against the recalled Huang prediction

Backing program: `code/brute.py` (exhaustive oracle), output in
`code/out/brute.captured.txt`.

```claim
id: f-exact-1..4
statement: f(1)=1, f(2)=2, f(3)=2, f(4)=2, where f(n)=min D(S) over S⊆{0,1}^n, |S|=2^{n-1}+1.
hypotheses: exact exhaustive enumeration; S sizes 2,3,5,9.
holds-here: yes
status: checked
bearing: exact values. They equal ceil(sqrt(n)) for n=1..4 (1,2,2,2), which is
exactly what the recalled Huang lower bound (max internal degree >= sqrt(n) for
any >2^{n-1}-vertex induced subgraph) together with the sqrt(n) upper
construction would predict. This is a second, independent route (exact
computation) agreeing with the recalled theorem's prediction at small n, but it
does NOT prove the theorem — it is consistent with it.
falsifies: a computed f(n) < ceil(sqrt(n)) for any n would refute the recalled
Huang bound in that regime.
anchor: code/out/brute.captured.txt
```

## Degree profiles (from oracle)

- n=2, S=[0,1,2]: degrees {1:2, 2:1}
- n=3, S=[0,1,2,5,6]: {1:2, 2:3}
- n=4, S=[0,1,2,5,6,11,12,13,14]: {0:1, 2:8}

These show the extremal S spreads internal degree so that the max is small (2 at
n=3,4) while many vertices share it — a flat profile, not a Hamming-ball-like
one. This is the kind of structure an averaging argument would not predict,
consistent with problem.md's obstruction.

## Status note

`f(n) >= sqrt(n)` (equivalently Huang's theorem) is NOT established by this
computation: n=1..4 cannot distinguish sqrt(n) from log n, and the oracle only
says these exact small values are consistent with the recalled bound. The
run's decisive open question — is the gap already closed by the spectral
interlacing argument? — is recorded in
`research/threads/spectral-interlacing-sqrt-lower-bound.md` and the linear
algebra must be settled by coder/theorem_prover/lean_prover, not by the
librarian.
