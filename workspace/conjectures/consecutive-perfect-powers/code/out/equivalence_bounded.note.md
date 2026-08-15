# Note — exp2 descent <-> Lebesgue equivalence settled

Program: `code/exp2_descent/verify_equivalence_bounded.py`
Outputs: `code/out/equivalence_bounded.captured.txt`,
`code/out/verify_direction_split.captured.txt`,
`code/out/verify_subclaim_fresh.captured.txt`

## Why this run existed

`code/exp2_descent/verify_equivalence.py` had 0-byte captures
(`equivalence.captured.txt`, `equivalence_rerun.captured.txt`) — written but
never successfully executed. The reason was a genuine defect: it set
`Xb = 2 * S**q = 2 * 30**37` (astronomically large) and swept
`for x in range(3, Xb+1, 2)`, an **infinite loop**. This is a concrete, located
bug, now fixed.

## What was settled

**Claim (equivalence).** For q an odd prime, the descent sub-claim

    r^q - 2^{mq-2} s^q = +-1     (m>=1, r,s>=1, gcd(r,s)=1)

is bijective with the solutions of `x^2 - y^q = 1`, under the maps

    -1 branch:  x = 2r^q + 1,  y = 2^m r s
    +1 branch:  x = 2r^q - 1,  y = 2^m r s

(the `+1` branch needs `x = 2r^q - 1`, not the single map `x=2r^q+1` that the
original docstring used — that single map fails; `verify_direction_split.py`
shows `x^2 - y^q = 1 + 8 r^q` for it in the +1 case).

**Result (verified-numerically, exact integer arithmetic).** The round-trip
bijection holds on the common finite range `x <= 300000, m <= 8, r,s <= 300`
for **all odd primes q <= 37**. Calibration: `(x,y) = (3,2)` satisfies
`x^2 - y^3 = 1`, present in both directions.

`verify_direction_split.py` (EXIT 0) additionally shows:
- the **known solution is the −1 branch**: `(q,m,r,s) = (3,1,1,1)` gives
  `r^q - 2^{mq-2}s^q = 1-2^1 = -1` and maps to `(x,y) = (3,2)`;
- the **+1 branch never occurs** in any small range scanned: no `(q,m,r,s)`
  with `gcd=1` and `r^q - 2^{mq-2}s^q = +1` exists over q<=7, m<=8, r,s<=60.

`verify_subclaim.py` (fresh capture, `code/out/verify_subclaim_fresh.captured.txt`):
two independent routes agree the only descent solution over q<=37, m<=8,
r,s<=500 is `(3,1,1,1)`:
- route 1 (direct sweep): 0 counterexamples;
- route 2 (via Lebesgue `x^2-y^q=1`, x<=200000): only `(q,x,y) = (3,3,2)`;
- cross-check: restricted route-1 image == route-2 image == `{(3,3,2)}`.

The `"0 found / calibration []"` lines in the older `verify_subclaim.captured.txt`
are cosmetic, not a contradiction: `route1_direct` filters out `(3,1,1,1)`
before appending, so "0" means zero *counterexamples*, and the known solution
is confirmed by route 2 and the cross-check.

## Falsifier

The known solution `3^2 - 2^3 = 1` is **found**, not excluded: it maps to the
−1-branch descent solution `(3,1,1,1)`. The equivalence therefore does not
over-eliminate; it correctly places the known solution in the −1 branch.

## Status

Verified-numerically (exact integer arithmetic) over the stated ranges; the
algebra of the maps is exact. Not a proof for all q — the open gap is the
general proof that `r^q - 2^{mq-2}s^q = ±1` has only `(3,1,1,1)` (which the
sweeps strongly support) and the general Lebesgue theorem.

```claim
id: exp2-descent-lebesgue-equivalence-bounded
statement: >
  For odd prime q, the descent sub-claim r^q - 2^{mq-2}s^q = +-1
  (m>=1, r,s>=1, gcd(r,s)=1) is bijective with the solutions of x^2-y^q=1
  under the branch-corrected maps x=2r^q+1 ((-1) branch) and x=2r^q-1
  ((+1) branch), y=2^m r s. Verified: the round-trip bijection holds on
  x<=300000, m<=8, r,s<=300 for all odd primes q<=37; calibration
  (x,y)=(3,2) at q=3 present. Known solution is the -1 branch (3,1,1,1);
  the +1 branch never occurs in any small range scanned.
hypotheses: >
  q odd prime; exact integer arithmetic; the verification is over finite
  ranges (x<=3e5, m<=8, r,s<=300; q<=37), not all pairs.
holds-here: yes -- the known solution (3,2) is found (in the -1 branch),
  never excluded.
status: checked (verified-numerically over the stated finite ranges; exact;
  not a proof for all q)
bearing: >
  Establishes the descent<->Lebesgue equivalence on a bounded range with
  branch-corrected maps, closing a 0-byte-capture gap; supports the Case-A
  reduction x^2-y^q=1 -> descent equation. The general proof that the
  descent has only (3,1,1,1) remains the open step.
anchor: code/out/equivalence_bounded.captured.txt,
  code/out/verify_direction_split.captured.txt,
  code/out/verify_subclaim_fresh.captured.txt
```
