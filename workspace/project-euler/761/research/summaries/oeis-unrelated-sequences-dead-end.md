# OEIS A092982, A308358, A121828, A195072 — unrelated sequences from K(n) coincidence hunting

Sources: https://oeis.org/A092982, https://oeis.org/A308358, https://oeis.org/A121828, https://oeis.org/A195072.
No `.full` files held (OEIS text pages).

## What these records establish

Four unrelated OEIS integer sequences that entered this run only as cross-references
during the `K(n) = floor(3n/7)`-coincidence investigation:

- **A092982** — number of prime divisors of the squarefree number A092981(n): an increasing arithmetic-ish sequence, nothing to do with pursuit.
- **A308358** — Beatty sequence for √3/4: `a(n)=floor(n·A120011)` with A120011=√3/4≈0.4330; differs from A057357 first at n=37. (A120011 itself is the equilateral-triangle area, mislabelled "critical speed" in an earlier frontier pass — corrected in `oeis-a120011-critical-speed-constant.md`.)
- **A121828** — `ceiling((π−e)n)`.
- **A195072** — `n − floor(n/√3)`.

None is `K(n)` as n→∞: the true asymptotic slope of K(n) is
`c = 0.430296653…` (root of tan(cπ)=π(c+1) = B_circle/π), which is not 3/7
(0.42857), not √3/4 (0.43301), not (π−e) (0.4233), not (1−1/√3) (0.4226).
**All four are irrelevant to the hexagon answer.**

## Why they are kept

Closes the K(n) OEIS-coincidence hunt as a dead end (already recorded in
CONTEXT.md: "OEIS small-term matches (A057357) are coincidences"). Any later
run seeing these files knows not to re-fetch or re-derive a connection.

```claim
id: oeis-unrelated-sequences-dead-end
statement: OEIS A092982 (prime-divisor count), A308358 (Beatty sqrt(3)/4), A121828 (ceiling((pi-e)n)), and A195072 (n-floor(n/sqrt(3))) are unrelated integer sequences; none equals the stewbasic K(n) index: K(n) has asymptotic slope c=0.430296653 (root tan(c*pi)=pi(c+1)), not 3/7, sqrt(3)/4, pi-e, or 1-1/sqrt(3). The small-n coincidence with floor(3n/7) (A057357, n<=85) is not a theorem.
hypotheses: stewbasic general-n formula's K index; OEIS cross-reference lookups during pattern hunting.
holds-here: yes — documents a closed dead end; no relation to V_hexagon.
status: derived (run's verification code + OEIS records).
bearing: closes the OEIS-coincidence thread; K is auxiliary and irrelevant to the answer.
anchor: research/sources/oeis_a092982.md
```