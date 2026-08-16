```thread
question: Where does direct Gröbner/resultant/SNF verification of CA stop being feasible, and what boundary can the run honestly report?
status: open
rests-on: bad-prime-minors-criterion, 5p-bad-primes-chellali
next: rank over F_p for n=5 — test the named degree-5 bad primes {2,3,7,11,131,193,599,3541,8009}, report which drop rank below 120, and compare to Castryck Thm 4 / Chellali-Salinier (task badprimes-n5-rank-mod-p)
```

# Thread: the computational boundary and the bad-primes program

## Question
Where does direct Gröbner/resultant verification of CA stop being feasible, and
what is the boundary the run can honestly report?

## What the held sources establish
- Degree ≤7 verified by Diaz-Toca & Gonzalez-Vega (2006) by Gröbner over ℚ;
  degree 8 by the same authors.
- Degree 12 settled by Castryck-Laterveer-Ounaïes (2012) by combining
  theoretical constraints (scenarios/types) + reduction-mod-p + Gröbner in
  characteristic p. Cost: ~3 weeks of computation and ~90 GB RAM per scenario,
  5 scenarios total. The paper explicitly says pushing to d=20 "the next open
  case" is "utopic" with their method. This is a *reported* boundary.
- The characteristic to work in matters: a Gröbner basis over ℚ and over 𝔽_p
  answer different questions. The reduction-mod-p approach reduces a char-0
  degree-d check to checking absence of CA-polynomials over 𝔽_p for good
  primes (Graf-von-Bothmer Theorem): "If no CA-polynomials of degree d exist
  over 𝔽_p, then CA holds in degree d" (mod good-prime hypotheses).

## The boundary this run can extend
The GOAL asks the oracle to reproduce, by elimination/Gröbner over ℚ, CA for
the smallest degrees and record where computation stops being feasible and why.
Held sources give: ≤8 direct over ℚ; 12 via smart reduction-mod-p. Recomputing
4,5,6,8,9 (and the char-p witnesses) over ℚ should be feasible in sympy; the
boundary (likely 9 or 10 before blow-up, well below 12's heroic 90 GB) is the
honest reportable result.

## Bad-primes program (Schaub-Spivakovsky)
A prime p is *bad* for degree n iff CA fails in char p. Strategy: verify small
d, classify bad primes, lift CA to degrees dp^ℓ via good primes
(CA_{n,p} ⇒ CA_{np^ℓ,p} and CA_{np^ℓ,0}). Schaub-Spivakovsky give a criterion:
p bad iff p | J_T for some T, where J_T are gcds of minors of explicit
matrices; if CA_{n,0} holds, bad primes are bounded above by an explicit
combinatorial expression. These give computable filters.

## Status
The run's exact-oracle reproduction of the small-degree boundary over ℚ, the
char-p witness checks, and an attempted Gröbner push toward the reported
boundary is the deliverable from this thread. Feasibility boundary over ℚ is
expected well below 12.

## Measured boundary (n=5 SNF route)

**RESULT (measured, not asserted):** the Smith-normal-form minors route is
feasible at n=4 and infeasible at n=5, the two smallest degrees where it is
load-bearing.

- n=4: M_T is 19×15; all 4^3=64 tuples finish in milliseconds; lcm J_T =
  1575 = 3²·5²·7 → bad primes {3,5,7} (`code/out/badprimes_n4.captured.txt`).
- n=5: M_T is 195×120 (C=120 columns, D=195 rows); 5^4=625 tuples; a single
  SNF on one 195×120 matrix **did not finish within a 90 s cap**
  (`code/out/commands.log`, final command: "SNF exceeded 90s cap on one
  195x120 matrix"). Projected lower bound 625 × 90 s ≈ 15.6 h, and SNF cost is
  super-polynomial, so the full route is out of budget by orders of magnitude.
  Re-running with a longer alarm only confirms this more expensively.

Decision: **switch to rank over F_p**. Deciding whether a *named* prime p is
bad never needs J_T itself — only whether rank_{F_p}(M_T) < 120 for some tuple
T. `lib.badprimes.rank_mod_p` is modular Gaussian elimination, O(D·C²) per
tuple, vastly cheaper than SNF over ℤ. Task `badprimes-n5-rank-mod-p` carries
the work.

## References
- research/sources/castryck2012_degree12_html.full.md
- research/sources/schaub_spivakovsky_bad-primes_2024.full.md
- research/sources/schaub_spivakovsky_upper-bound-bad-primes_2024.full.md
- research/sources/grafvonbothmer2007_infinitely_many.full.md
