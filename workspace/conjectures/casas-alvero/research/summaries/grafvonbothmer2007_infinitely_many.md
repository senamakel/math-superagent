# Graf von Bothmer, Labs, Schicho, van de Woestijne, *The CA conjecture for infinitely many degrees* (J. Algebra 316 (2007) 224–230)

Full text: [[grafvonbothmer2007_infinitely_many.full]]

The foundational breakthrough: proves CA for degrees `p^k` and `2p^k` (char 0), and exhibits the char-p counterexamples that are the negative control for every argument in this run. (NOTE: the held `.full.md` is only the arXiv landing page with the abstract; the paper body is not physically held. The statements below are from the abstract and from what the other held sources — Castryck §1, Draisma–de Jong §7, Schaub–Spivakovsky — quote and re-derive from it.)

## The lift theorem and its consequences

```claim
id: gvb-lift
statement: (as quoted and reformulated by Castryck et al, Theorem 3) Let d>0 and p prime.
  If no CA-polynomials of degree d exist over F_p-bar, then CA holds in degree d p^k for
  all integers k≥0 (over F_p-bar and over char-0). Since no CA-polynomials exist in
  degree 1 or 2 in any characteristic, CA holds in degrees p^k and 2p^k (char 0).
hypotheses: char-p absence of degree-d CA-polynomials for the ground prime
holds-here: yes
status: asserted-by-source (the made proof is [7]'s; re-stated and used in the held sources)
bearing: This is the engine of every settled family. It also frames the run's method:
  to settle char-0 CA in degree dp^k it suffices to find one prime p with no char-p
  degree-d counterexamples, then verify d's bad primes.
anchor: research/sources/castryck2012_degree12_html.full.md (Thm 3; citing [7])
falsifies: a degree dp^k counterexample in char 0 for a good prime p.
```

## The char-p counterexample family (the run's negative control)

```claim
id: charp-witness-xpp1-xp
statement: In characteristic p, f(x) = x^{p+1} − x^p (and relatives) is a CA-polynomial
  (shares a non-trivial factor with every derivative) that is NOT a pure power. f(X^p)
  without constant term also works since all derivatives vanish. Hence CA is false in
  positive characteristic, and any char-0 proof must have a step with no char-p analogue.
hypotheses: char K = p > 0
holds-here: true — this is the hard constraint of the whole problem
status: asserted-by-source (abstract of [7]; also Wikipedia, Schaub–Spivakovsky)
bearing: The oracle in code/lib must report x^{p+1}−x^p as satisfying the hypothesis and
  NOT a pure power. Every candidate argument must be run against it and the failing
  step named.
anchor: research/sources/grafvonbothmer2007_infinitely_many.full.md (abstract),
  research/sources/wikipedia_casas_alvero.full.md
falsifies: a run of the oracle showing x^{p+1}−x^p does NOT pass, or IS a pure power.
```

## What it does not settle
Only p^k and 2p^k. Degrees like 3p^k, 4p^k, 5p^k need the p-adic/bad-primes refinements; degrees not of the form dp^k (12, 20, 24, 28, 30, 36, 40…) are out of reach of the plain lift — this is why d=20 is open.
