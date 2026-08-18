# Refuted approach: naive Diophantine collision

The proposed route tried to combine Hercher's bridge inequality with Zudilin's effective irrationality measure and a reciprocal-sum estimate to prove a lower bound on a cycle minimum.

It fails in two independently checkable ways:

1. Hercher Corollary 24 Table 1 bounds `K`, the number of odd members, not `x_min`. The exact published rows are captured in `code/out/collision_table.txt`.
2. If `delta=(log 3)/(log 2)`, the bridge gives
   `(m+L)/m - delta < (3 log 2/m) S`.
   Zudilin gives `c0/m^mu < |delta-(m+L)/m|`; for a cycle the difference is positive, so
   `c0/m^mu < (3 log 2/m) S`.
   Thus `S > c0*m^(mu-1)/(3 log 2)`. With `S <= m/x_min`, this gives
   `x_min < (3 log 2/c0)m^(2-mu)`, the reverse of the desired lower bound.

The Lean file `code/lean/Lib/cycle_collision.lean` pins down the attempted hypotheses and retains the requested open theorem as a `sorry` blueprint, but the theorem must not be reported as established. A future attempt should rederive the cycle identity with carefully checked signs and distinguish K, m, L, local minima, and x_min before seeking a new reduction.