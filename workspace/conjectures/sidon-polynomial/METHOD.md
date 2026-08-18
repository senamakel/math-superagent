Solve by Diophantine analysis of the equation `f(a)+f(b)=f(c)+f(d)` in `Z[x]`,
with an exact-integer collision oracle underneath every claim. Low degrees are
closed and must be re-proved here first — the quadratic obstruction and the
cubic obstruction of Dubickas–Novikas are the templates for what an obstruction
looks like, and degree 4 is the first place a new one could go.

The oracle for this problem is an exact-integer collision search: given `f` and
`N`, every `(a,b,c,d)` with `0 <= a < b <= N`, `0 <= c < d <= N` and
`f(a)+f(b)=f(c)+f(d)`, by hashing the `O(N^2)` sums. Never floating point: a
degree-5 value at `n ~ 10^6` overflows a double and a float comparison invents
collisions. Calibrate the oracle by making it rediscover the `x^4` collision and
a cubic collision on its own; an oracle that misses those makes every later
number worthless.

The two live routes are (a) making Ruzsa's `n^5 + floor(c n^4)` construction
effective and landing it in `Z[x]` — a concrete question about rational `c`,
directly searchable — and (b) ruling out degree 4 unconditionally, extending
Dubickas–Novikas. Proving `x^5` works is a case of Lander–Parkin–Selfridge and
is not a route; any argument that assumes it produces a conditional result and
must say so.

Use coder for the sweep and the collision search, symbolic_math for the
parametrised identities that kill low degrees, sat_solver or smt_solver for the
bounded-coefficient existence questions the sweep throws off, and pattern_finder
on the surviving polynomials.
