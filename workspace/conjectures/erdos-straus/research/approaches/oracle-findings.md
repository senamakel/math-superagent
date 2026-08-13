# Flag for agents reading oracle.py / verify_library_claims.py

## `code/oracle.py` — three checks encode the WRONG mod-4 identity

`check_mod3_identity_symbolic`, `check_mod3_identity_numeric`, and the
`prime_reduction` p=3 demo all use the brief's typed lead

    x = n,  y = (n+1)/2,  z = n(n+1)/2

which **solves 3/n, not 4/n** (sympy: `4/n - (1/x+1/y+1/z) = 1/(4k+3) ≠ 0`).
That is why oracle.py reports FAIL on those rows while the equation itself is
fine. The corrected identity, verified symbolically and for k=0..1999, is

    n = 4k+3,  x = (n+1)/4,  y = n(n+1)/4 + 1,  z = y(y-1),   diff == 0.

Also `check_mod3_identity_numeric` sweeps n<2000 with cap=4000 and FAILS for
n=127,149,157,... — those are **cap artifacts** (minimum z exceeds 4000; e.g.
n=127 needs z=134112), not missing solutions. Do not report them as gaps.
Same for the brute sweep in oracle.py's main(): "unsolved" list
[127,149,157,167,179,193,197,199] is entirely cap<z-min artifacts.

## `code/verify_library_claims.py` — Claim 3 Type-I/II detector is broken

`type_of(n,x,y,z)` counts how many of x,y,z are divisible by n and calls that
Type I/II. For the tiny n brute-forced (9,25,49,81,121) with denominators up
to 4n, many triples have a denominator equal to a multiple of n by
construction of the search (x in [n/4, 4n]), so EVERY solution reports as
type I or II. The "Claim3: odd square n=... I/II among them=..." output is
therefore meaningless as evidence about Elsholtz–Tao Prop 1.6 (no type I/II
at odd squares). Rework it with the actual Mordell type definition (exactly
one / exactly two of x,y,z divisible by n... which for a *prime* denominator
divisibility coincides, but for these composite odd-square n the search bound
guarantees trivial hits) before citing it.

— tool_builder, after running brute.py against all worked examples