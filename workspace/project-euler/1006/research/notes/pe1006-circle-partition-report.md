# Circle-partition route report for G4

## Restatement

For `S_0=0`, `S_1=01`, `S_n=S_{n-1}S_{n-2}`, let `F_k` be the distinct length-`k` factors and `Psi(k)` the sum of squared base-10 values. The target is `Psi(10^18) mod M`, `M=101001001`. Existing work has an exact mechanical representation but no joint-intercept evaluator.

## Theory and exact reduction

The governing theory is characteristic Sturmian coding by an irrational circle rotation, with `alpha=1/phi^2`. The `k+1` factors are the `k+1` arcs cut by `x_m={-m alpha}`. For each digit position `j`, the mechanical digit is an indicator `d_j(x)=1_{I_j}(x)` of a translated interval. Hence, with `w_j=10^(k-1-j)`,

`Psi(k)=sum_{j,l} w_j w_l C_k(j,l)`,

where `C_k(j,l)=#{m: x_m in I_j∩I_l}`. For a rational Fibonacci convergent `alpha=p/q`, each `C_k(j,l)` is an exact difference of floor counts after lifting the interval endpoints. Thus the proposed circle method does yield a finite floor-sum expansion, but the number of terms is `k^2`, or equivalently `k` correlation rows.

The Three Gap Theorem bounds the number of *arc lengths* of the sorted orbit by three. That does not bound the number of pair-correlation rows: the interval intersections retain their absolute endpoint/boundary placement. The decimal weights prevent discarding this placement, since each `(j,l)` carries a generally distinct power of 10.

## Prior literature check

Allouche–Glen (https://doi.org/10.4171/lem/56-3-5) supports the mechanical rotation coding and balance, but gives no weighted-square aggregation. Alessandri–Berthé (https://doi.org/10.5169/seals-63900) supports the relation between three-distance geometry and Sturmian factor frequencies, but gives no fixed-dimensional exact evaluator. Berstel–Vuillon (https://doi.org/10.48550/arxiv.math/0106217) constructs an automaton for coding rotations on interval partitions, not an O(log k) aggregate for this decimal quadratic observable. The literature therefore supports the reduction, not the missing collapse.

## Executable test

`code/g4_circle_partition_test.py` is the tool-builder test. It is explicitly an exponential oracle with `oracle_bound=60`. It:

1. independently constructs the circle arcs and their midpoint factors;
2. checks `F_3={001,010,100,101}`, `Psi(3)=20302`, and `Psi(10) mod M=10699667`;
3. forms all `C_k(j,l)` by direct interval indicators;
4. checks the exact pair-expansion against the direct square sum for every `k<=bound`;
5. reports correlation-row/state growth.

The existing independently executed mechanical and window oracles already establish the semantic checks through `k<=50`/`400` and anchors `Psi(10^4)=34432237`, `Psi(10^6)=20938836`; the new script is specifically the circle-indicator reduction test. I could not execute it in this role because no shell/container execution tool is exposed; do not treat its unrun row counts as numerical evidence.

## Precise obstruction

The approach is not a full G4 solution. It proves only:

- **Yes:** after sorting/lifting the cut points, the weighted square is a finite sum of exact floor-counts.
- **No established collapse:** neither Three Gap nor bounded-variation discrepancy turns the `k^2` weighted correlations into a fixed number of floor sums.
- **Boundary obstruction:** Toeplitz dependence on `l-j` occurs only at `k=F_n-1`; at general `k`, the truncated orbit has endpoint data. Grouping by `h=l-j` leaves the absolute decimal position and boundary coupled.

A discrepancy/Euler–Maclaurin estimate can give an approximation or error bound, but the goal requires an exact residue modulo `M`; an error bound smaller than 1 after the huge decimal weighting is not supplied and would not remove the endpoint data. Therefore this route is closed as an O(log k) method unless a new theorem gives a fixed-dimensional renormalization of the full boundary-marked correlation kernel.

This is a precise obstruction rather than a claim that no conceivable O(log k) algorithm exists. It retires the proposed circle-indicator route in its stated form while identifying the exact missing lemma.
