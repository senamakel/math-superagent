# Independent final verification route

The mechanical-word/floor-sum evaluator represents each factor by a mechanical
intercept and uses weighted floor moments. An independent exact formulation is
available before the missing asymptotic evaluator: choose the least Fibonacci
number N strictly larger than k and let q be the length-N Fibonacci word. The
position theorem says the distinct factors are the terminal windows of qq at
positions r=N-k-1,...,N-1. Thus, with V_r the decimal value of qq[r:r+k],

    Psi(k) = sum_{distinct terminal windows} V_r^2.

Values can be generated exactly by
V_{r+1}=10 V_r-q_r 10^k+q_{r+k}.

`code/mech/independent_second_route.py` implements this route and deduplicates
terminal strings (important at tiny N), then compares with `mech_psi` for every
k=1..150. The run passed, including Psi(3)=20302 and Psi(10)=10699667.

This is an independent check of the factor-position identity and decimal
indexing, but it is still O(k) (and the integers have k digits), so it cannot
produce Psi(10^18). The precise identity needed for a full independent final
check is a fixed-dimensional Fibonacci-block summary for the recurrence above:
for every Fibonacci block B, one must compose summaries of `(V, sum V,
sum V^2)` while simultaneously supplying the paired boundary digits
`(q_r,q_{r+k})`; the summary must be closed under Fibonacci concatenation and
support extraction of the prefix of length N-k-1. Agreement with the mechanical
route at k<=150 and with both anchors would then certify the final residue.
No such closed summary has been established here, so no target answer is
claimed.
