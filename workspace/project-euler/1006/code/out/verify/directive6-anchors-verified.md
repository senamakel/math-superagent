# PE1006: directive-6 anchors verified in-container (checked)

The directive-6 acceptance anchors, previously asserted from outside the
container and listed as an open gap in CONTEXT.md (task `directive-6-anchors`,
blocked) and `research/backward/g4-universal-euclidean-floor-sum.md`, are now
**verified in-container** by the independent window/residue route.

## The verified numbers (exact, mod M = 101001001)

Program: `code/out/verify/window_residue_route.py`, run in-container, captured
to `code/out/verify/window_residue_route.captured.txt`:

- Psi(3) = 20302 (count 4) — matches the problem's oracle
- Psi(10) mod M = 10699667 (count 11) — matches the problem's oracle
- **Psi(10^4) mod M = 34432237 (distinct count 10001)** — the directive-6 anchor
- **Psi(10^6) mod M = 20938836 (distinct count 1000001)** — the directive-6 anchor
- k = 1..60 cross-checked against `code/brute.py` psi_of: **no mismatches** on
  value and count.

Method: builds the prefix of length L = k + NextFib(k) - 1 + k (NextFib the
least Fibonacci STRICTLY greater than k, via bisect_right), keeps each
distinct length-k window's value as two independent sliding residues mod M and
mod M2 = 1000000007 via w_{r+1} = (10·w_r − y_r·10^k + y_{r+k}) mod m, dedups by
the residue pair, and asserts the distinct count equals k+1. k=10^6 runs in
1.2 s wall. The captured file's banner: "ALL CHECKS PASS = True".

## Why this matters

This satisfies the **directive-10 hard gate** for the Lean arm: "no
lean_scribe/lean_prover run may be spawned until code/out holds a captured file
showing Psi(10^4)=34432237 and Psi(10^6)=20938836 recomputed inside the
container." `window_residue_route.captured.txt` is exactly such a file.

Caveat: this is verification of the *acceptance anchors* by the independent
sliding-window route. It is NOT yet the universal-Euclidean monoid output for
those k (task `implement-solution`, acceptance steps 4–5), which remains the
open item before the k=10^18 run.

```claim
id: directive6-anchors-verified-incontainer
statement: Psi(10^4) mod 101001001 = 34432237 with exactly 10001 distinct
length-10^4 factors, and Psi(10^6) mod 101001001 = 20938836 with exactly 1000001
distinct factors, computed in-container by the independent window/residue route
(prefix length k+NextFib(k)-1+k, NextFib strictly greater than k, dedup by two
moduli), agreeing on k=3,10 with the problem's oracle and on k=1..60 with the
brute oracle.
hypotheses: Fibonacci word; NextFib = least Fibonacci strictly greater than k;
windows read as decimals mod M and mod 1000000007, deduped by residue pair,
distinct count asserted equal to k+1.
holds-here: yes
status: checked (captured run, exact integers)
bearing: releases the directive-10 hard gate on the Lean arm; confirms the
acceptance anchors the universal-Euclidean evaluator must reproduce (acceptance
steps 4-5) before k=10^18. Not yet the monoid's own output for those k.
anchor: code/out/verify/window_residue_route.captured.txt
answers: (the old directive-6-anchors verification gap — the asserted anchors
are now reproduced in-container)
search-frame: window/residue route swept k=3, 10, 10^4, 10^6 over the prefix
of length k+NextFib(k)-1+k (NextFib strictly greater than k), every window
held as two sliding residues mod 101001001 and mod 1000000007 (w_{r+1} =
10·w_r − y_r·10^k + y_{r+k}), dedup by residue pair, distinct count asserted
equal to k+1; k=1..60 cross-checked against code/brute.py value and count.
```
