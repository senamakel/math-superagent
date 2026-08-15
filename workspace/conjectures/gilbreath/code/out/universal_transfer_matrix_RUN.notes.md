# universal_transfer_matrix_RUN — results and independent cross-check

Capture: `code/out/universal_transfer_matrix_RUN.captured.txt`, EXIT_CODE=0.

## (A) Universal claim `wt(Phi_n h) >= wt(h)/2` for all h in {0,1}^{n-2}

**REFUTED**, over n=4..20 with 19,947 violating h total. The smallest
counterexample is n=4, h=[1,1] (all-ones): `nu2 = wt(Phi_4 h) = 0`, `w = 2`,
so `0 < 1 = w/2`. Violations are not isolated — they appear in every n from 4
onward (1,1,2,5,9,19,26,...,9021).

## (B) Worst-case ratio `min_{h!=0} wt(Phi_n h)/wt(h)` per n

For **every** n in 4..20 the minimum ratio is **0**, achieved by (among
others) the all-ones h = 11...1 with `nu2 = 0`. So the exact worst-case ratio
is 0 for all n = 4..20, uniformly.

## (C) Consecutive-odds q=(2,3,5,7,9,11,...): all gaps ≡ 2 (mod 4)

Bottom entry of the difference triangle is 1 (SUCCESS) at every n = 1..18
(n=0 is the trivial single-entry triangle whose terminal is the entry 2
itself), while `nu2 = 0` (run's tail convention) and `w = n-2` grows linearly.
Right diagonal at each n is `(2n+1, 2, 0, 0, ..., 0, 1)`, so the maximal
{0,2} suffix before the terminal is all zeros → nu2 = 0.

## Verification: g-supply-transfer-refuted confirmed

`nu2 = 0` while `(2/3)w = (2/3)(n-2)` grows linearly: **nu2 >= (2/3)w is
false for every n >= 4**, in the claim's own domain (a successful 2-then-odds
prefix). This confirms the recorded claim `g-supply-transfer-refuted` and
decides the S1 fork to the prime-specific case (b): the nu2 >= c·w transfer is
NOT a universal combinatorial reduction.

## Independent cross-check (second route)

`lib.gilbreath.rows_generator` on q=(2,3,...,21) gives A_10(0)=1; and
`lib.rightdiag.incremental_diagonals` reproduces exactly the right diagonals
from (C): `[3,1],[5,2,1],[7,2,0,1],[9,2,0,0,1],[11,2,0,0,0,1]`. Both
independent code paths agree with the new script's hand-rolled builder, so the
consecutive-odds success and nu2=0 values are verified by a second route.
