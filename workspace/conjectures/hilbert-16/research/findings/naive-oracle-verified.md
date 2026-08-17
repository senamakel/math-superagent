# Durable finding — naive oracle verified (2025)

Store into Cognee once the memory server recovers; this disk copy is the
source of truth meanwhile.

**What was built and verified (code/brute.py):**

For a radially symmetric polynomial planar field

    x' = A(r²)x − B(r²)y ,   y' = B(r²)x + A(r²)y ,   A,B ∈ Q[u], u = r²,

polar coordinates give `dr/dt = r·A(u)` and `dθ/dt = B(u)`, so the
displacement function `D(r) = (return map − id)(r)` has the SAME SIGN as
`A(u)` wherever `B ≠ 0`. Hence isolated periodic orbits = positive roots of
`A` with `B(u0) ≠ 0`; `A(u0)=B(u0)=0` is a ring of equilibria (excluded via
gcd). A root of odd multiplicity is a hyperbolic limit cycle.

Exact method: polynomial division to extract A,B, square-free factorization +
Sturm count for sign-changing roots. No floats, no integration, no sampling.

**All worked examples reproduced (7 cases, all PASS):**

| case | result |
| --- | --- |
| cubic normal form `1−u`, B=1 | count 1 at r=1 (root 1.0) |
| linear centre (−y,x) | A=0 → 0 cycles |
| linear expanding focus (x−2y, 2x+y) | A=1 → 0 cycles |
| van der Pol-like (non-radial) | refused, not miscounted |
| linear saddle (x,−y) (non-radial) | refused, not miscounted |
| A=(1−u)(2−u), B=1 | 2 cycles at u=1,2 |
| A=(1−u)²(2−u), B=1 | certified 1 (u=1 double root excluded) |

Second-route numeric check (scipy solve_ivp): cubic cycles from r0=0.5 and
r0=2.0 both converge to r=1 — stable hyperbolic cycle, consistent with exact
count 1.

**Honest boundary:** the oracle certifies only the radially symmetric class.
A general polynomial field has a displacement function this naive method
cannot compute exactly; the oracle refuses such fields rather than guess.
This pins down the exact statement for the tractable normal-form class and
leaves the general case (the actual H16.2 object) to the library/Lean side.