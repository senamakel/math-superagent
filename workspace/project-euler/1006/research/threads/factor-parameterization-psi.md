# Thread: factor parameterization and the Psi(k) recurrence (PE1006)

```thread
question: Give an explicit, indexable description j -> w_j of the k+1 length-k factors of the
  Fibonacci word (Sturmian, slope 1/phi^2), with each factor's number of 1s, and turn it into
  an O(log k) (recurrence/matrix-power) evaluation of Psi(k) = sum of (decimal value)^2.
status: open
rests-on: MH-kplus1-factors, PR-consecutive-factors-lex, PE1006-factors-one-count-necessary,
  christoffel-conjugate-and-forest, PE1006-factors-dependent-slop-only
blocked-by: no closed form / low-order recurrence for Psi(k) yet identified; the Perrin–Restivo
  Next() enumeration is O(k^2) in length, infeasible at k=10^18.
next: use the lex-order consecutive-factor rule to write Psi(k) as a sum over r·ab·s / r·ba·s
  successors; reduce sum-of-squares to pairwise position-correlation counts N(j,l;k), which are
  organised by k's Fibonacci/Zeckendorf representation; find the minimal-order recurrence in k
  and validate against brute force for k<=40 (oracle), then against O(k) iteration to k~10^6.
```

## What the library already gives

- **Necessary condition only:** every length-k factor of the Fibonacci word has floor(k·α)
  or ceil(k·α) ones, α = 1/φ² (`PE1006-factors-one-count-necessary`). This is NOT a
  bijection — the earlier claim `PE1006-balanced-factors-floornalpha` ("the factors are
  exactly the balanced words with floor/ceil(kα) ones, and there are exactly k+1 of them")
  was **retracted as false** (`PE1006-balanced-bijection-refuted-checked`): at k=4 there are
  10 balanced words of the right count but only 5 factors. Do not build on it.
- The factors ordered lexicographically follow the rule: consecutive pairs are r·ab·s / r·ba·s
  (or r·a / r·b); Next(u) = rbas / rb from the longest right-special prefix r
  (`PR-consecutive-factors-lex`, proved). This is an explicit indexable j -> w_j enumeration:
  w_j = Next^j(lex-min), O(k) per factor, O(k²) total.
- The factor set depends only on slope 1/φ² (`PE1006-factors-dependent-slop-only`), so no
  finite-S_n ambiguity.
- Christoffel conjugate-class + singular-factor structure (`christoffel-conjugate-and-forest`,
  Perrin–Restivo Prop 3 / Example 10) is the natural frame for the fib-index dependence.
  At k = F_n the k+1 factors are exactly the n rotations of one Christoffel word plus one
  singular factor (`PE1006-conjugate-singular-iff-fibonacci`, checked to k=60), and Chuan's
  Thm 11/Cor 12 gives the 1-letter positions inside each rotation as arithmetic progressions
  mod F_n (`chuan-cyclic-shift-index`) — the positional structure the rotation-sum Psi(F_n)
  collapses by.

## Gap

The remaining work is purely the sum-of-squares: Psi(k) = sum_j (value(w_j))², and the
2-point statistics N(j,l;k) = #{factors with a 1 in positions j and l}. The library holds the
factor-set structure but no closed form or low-order recurrence for Psi(k). That is the run's
open computation (R3–R5 of the weakened ladder).
