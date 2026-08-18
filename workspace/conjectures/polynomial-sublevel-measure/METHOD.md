Solve by real and potential-theoretic analysis of polynomials, with an
exact-arithmetic oracle underneath every decimal. The quantity is a Lebesgue
measure of a semialgebraic set, so for any fixed root vector it is an exact
algebraic number: compute it by isolating the real roots of `f - 1` and `f + 1`
in exact or certified interval arithmetic, never by sampling.

The oracle for this problem is that certified `mu(f)` evaluator together with a
global optimiser over root vectors in `[-1,1]^n` for each degree `n`, reporting
the extremal configurations themselves — their shape (clustered, endpoint,
repeated roots) is the mathematical content, not the number alone.

Use symbolic_math (sympy, PARI, Singular) for exact root isolation and for the
critical-point equations of the per-degree extremal problem; the optimum is
characterised by a Lagrange condition on the root vector, and deriving it
symbolically is more valuable than any amount of numerical search. Use coder for
the global search, and pattern_finder on the sequence of per-degree optima.

The classical frame is Chebyshev polynomials, logarithmic capacity and Cartan's
lemma: `cap([-1,1]) = 1/2` while `cap([-2,2]) = 1`, and the infimum drops to
zero exactly at the second. Any approach with no potential-theoretic reading
should say why it expects to see the mechanism without it.
