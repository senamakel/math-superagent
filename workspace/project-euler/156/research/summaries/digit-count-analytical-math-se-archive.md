# math.SE 47477 — occurrences of digit 1 in 0..n (crasic's analytic form)

**Source:** https://math.stackexchange.com/questions/47477/number-of-occurrences-of-the-digit-1-in-the-numbers-from-0-to-n (crasic's accepted answer, Jun 2011; witnessed via Wayback: web.archive.org/web/2023/https://math.stackexchange.com/questions/47477). Full text: `research/sources/digit-count-analytical-math-se-archive.full.md`.

## What it establishes

- The thread IS Project Euler 156 material: the question asks for the next n with f(1,n)=n after n=1, and crasic's answer calls it "project euler problem #156".
- **Analytic closed form (crasic, independently derived).** With n = [r_k, r_{k-1}, ..., r_0] (list representation, n = Σ r_j 10^j), E(j) = j·10^(j-1), and n[j:] the number formed by the last j digits:
  f(d,n) = Σ_{j=0}^{k} ( Σ_{i=0}^{r_j} (10^j δ_{i-1,d}) + r_j·E(j) + δ_{r_j,d}(n[j:]+1) ).
  This counts occurrences of digit d in the numbers 0..n. It generalizes to any base B by replacing 10^k with B^k.
- Cross-checks: typing this into Mathematica gives the next solution 199981 for f(1,n)=n. The brute-force Mathematica scan in Listing's answer gives the full run 0,1,199981..199990,200000.
- S4M's answer: f(10^n−1) = n·10^(n−1) (André Nicolas's correction f(10^{n+1})=(n+1)10^n), and u_9 > v_9, u_10 < v_10 so any solution lies below 10^10−1 — an early, independent finiteness heuristic matching the d·10^10 bound idea (for d=1, solution bound 10^10; paper's tight bound is actually 1,111,111,110 < 10^10).

## Implications for PE156

- Confirms the closed form in `code/lib/digits.py::f_place_value` from an independent source (second route), and independently produces 199981, matching the statement's oracle.
- crasic's own note is exactly the caution the run heed: even the closed form "is too slow to solve the big problem" if you evaluate it per-n; the run must combine it with the bound (G2) and skip-search (G3), which the Khovanova–Marton paper supplies.

## Does not settle

- Does not prove the search bound, does not give the per-digit solution counts, does not give s(1).