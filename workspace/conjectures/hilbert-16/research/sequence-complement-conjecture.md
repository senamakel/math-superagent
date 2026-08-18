# Provisional sequence finding: quadratic-focus monomial counts

Exact executed data: d=4,6,8,10,12,14,16 gives monomial counts
`a=[4,30,97,236,485,890,1505]`. With h=d-2, the complementary counts in the full homogeneous degree-h space of five variables are
`c=[7,10,16,23,31,40,50]`.

Exact reruns found that for h=4,6,8,10,12,14,
`c=(h^2+14h+8)/8`, equivalently
`a=(binomial(h+4,4)-(h^2+14h+8)/8)/2`.
It fails at h=2: observed c=7, formula=5. Therefore this is only a conjecture for h>=4 (d>=6), not an established formula. The first uncomputed falsifier is h=16 (d=18), where it predicts a=2392.

`analyze_sequence` found no low-degree polynomial; `find_linear_recurrence` found no constant-coefficient recurrence of order <=6 over the seven a terms or seven c terms. OEIS lookup of the a sequence returned no match. The larger d=18 computation would settle the conjecture's first falsifier, but was not run because it is expensive and only tests this extrapolation.
