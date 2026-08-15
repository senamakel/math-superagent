# Scale-invariance kills the ordering/comparison cellular automaton

The approach `comparison-order-cellular-automaton` proposes to track only the
ORDERING of adjacent entries (comparison word `c_k(i)=[A_k(i+1) >= A_k(i)]` plus
a convexity bit `v_k(i)=[A_k(i)+A_k(i+2) >= 2 A_k(i+1)]`) and deduce `A_k(1) ∈ {0,2}`
by pattern-avoidance in that symbolic system.

## What is true
The local rule is exact. For `a,b,c` real/integer:
`|b-c| > |a-b|  <=>  (b-c)^2 > (a-b)^2  <=>  (2b-a-c)(a-c) > 0
                  <=>  (a-c)(a+c-2b) < 0   (since 2b-a-c = -(a+c-2b))`.
So the sign of the next row's adjacent difference is a function of two bits on
the previous row (sign of `a-c`, and whether `b` lies above/below the midpoint
`(a+c)/2`). Hedlund's theorem therefore makes the orientation word evolve under
a genuine one-dimensional cellular automaton. Hand-verified (elementary algebra).

## Why the programme is dead: scale-invariance
The comparison word `[λr_{i+1} >= λr_i]` and convexity bit `[λr_i + λr_{i+2} >= 2λr_{i+1}]`
are both invariant under any positive scaling `r -> λr` (λ>0): scaling preserves
every `>`/`>=`. But the second entry `A_k(1)` scales with λ.

Concrete pair, both valid all-even rows of a 2-then-odds triangle:
- `r  = (1, 2, 0, 4, 6, 2, ...)`  → second entry `2` (conjecture-satisfying)
- `2r = (1, 4, 0, 8, 12, 4, ...)` → second entry `4` (conjecture-violating)

These have IDENTICAL comparison and convexity words (verifiable by hand: every
`>=`/`>` magnitude comparison is unchanged by the common factor 2), and because
`|λa - λb| = λ|a-b|` the absolute-difference operator is positively homogeneous,
the full symbolic system is the same for both. Hence NO pattern-avoidance
condition over the orientation/convexity word can distinguish `A_k(1)=2` from
`A_k(1)=4`: the symbolic system is structurally blind to the very magnitude its
conclusion is about.

## Disposition
`comparison-order-cellular-automaton` — **refuted** (killed-by: scale-invariance).
The local CA half is grounded; the deduction half cannot express the conjecture.
This is a cousin of the run's "no scalar Lyapunov survived" and "magnitude-blind
representations (Rule 90)" lessons: any representation that discards absolute
magnitude discards the conjecture.
