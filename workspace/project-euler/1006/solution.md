# Solution derivation

## Theory
Use Sturmian factor complexity and mechanical-word rotation coding. The Fibonacci limit is the characteristic mechanical word of irrational slope `alpha=1/phi^2`. For a fixed length `k`, the k+1 factor changes occur only when the intercept crosses one of the k+1 rotated partition boundaries. Pick one representative in each interval.

For representative `x`, define
`d_j(x)=floor(x+(j+1)alpha)-floor(x+j alpha)` and
`v(x)=sum_{j=0}^{k-1} d_j(x) 10^(k-1-j)`.
Then the required quantity is `sum_x v(x)^2` over the k+1 interval representatives. Telescoping and collecting adjacent floor terms expresses `v` as an affine linear combination of `floor(x+j alpha)` with geometric coefficients. Therefore `v^2` is a quadratic polynomial in floor values, and only weighted sums of `1`, `floor`, and `floor^2` are needed.

## Euclidean reduction
Approximate the irrational slope by a Fibonacci convergent `p/q` with q>k. The interval endpoints become rational rotations and the representatives can be ordered as a Euclidean lattice path. Each path segment has a constant-size state
`(dR,dU,w,S0,S1,S2)`, where `w=z^dR`, `S0=sum z^i`, `S1=sum z^i h_i`, and `S2=sum z^i h_i^2`; `h_i=floor((p i+b)/q)` under the chosen 1-index convention and `z=10^{-1} mod M`. Concatenation of left and right segments is
`dR=L.dR+R.dR`, `dU=L.dU+R.dU`, `w=L.w R.w`,
`S0=L.S0+L.w R.S0`,
`S1=L.S1+L.w(R.S1+L.dU R.S0)`,
`S2=L.S2+L.w(R.S2+2 L.dU R.S1+L.dU^2 R.S0)` modulo M.

The standard Euclidean floor-sum recursion constructs this monoid product using quotient/remainder swaps. Each reciprocal step reduces the denominator/range, hence there are O(log q) steps. The final affine combination gives Psi(k) modulo M. For k=10^18, choose q from two successive Fibonacci convergents exceeding k; factor sets stabilize because both approximants encode the same length-k factors.

## Boundary and verification
The mechanical representation, slope convention, indexing, and monoid shifts must first be checked against the naive factor oracle at every small k reachable. A wrong slope (1/phi rather than 1/phi^2), an endpoint representative, or a z power offset can pass generic monoid tests but fail Psi(3) or Psi(10). Full-size verification should use a separate contiguous-window/Fibonacci-prefix implementation, not the same floor-sum code.