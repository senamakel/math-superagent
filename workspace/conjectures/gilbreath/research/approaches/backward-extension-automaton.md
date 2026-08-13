```approach
idea: Backward extension as a finite-state automaton — prove the conjecture by
      showing the local valid-extension set eventually equals {0,2} and traps
mechanism: >
  Muney 2026 studied the sets of integers that can be appended to a prefix of a
  Gilbreath triangle while preserving the "leading column = 1" property. The
  approach treats the Gilbreath triangle as a deterministic transducer from the
  initial row to the left column: if the set of valid next-values at position N
  depends only on a bounded window of recent row history, then the sequence of
  valid-extension sets forms a finite-state process. If the good component
  (where extensions are {0,2}-valued) is a trap state, the conjecture reduces
  to showing the primes stay in it.

  More precisely: define the "state" at position N as the last K rows truncated
  to a window of width W (the "backward light cone" of the left column). If the
  extension function e_N stabilizes and the state space is finite, then proving
  the conjecture reduces to (a) computing the state transition graph for small
  K,W, (b) showing the prime sequence stays in the "good" component, and (c)
  arguing the good component is a trap.

status: refuted
killed-by: >
  The literatures gives exact criteria for valid extensions, and they are GLOBAL,
  not bounded-window — so the finite-state Markov assumption does not hold.

  (1) Alkan et al. 2023 (Mathematics 11(18):4006, "Gilbreath Equation, Gilbreath
  Polynomials..."): S=(s_1..s_n) is Gilbreath iff s_1 has opposite parity to
  s_2..s_n and min K(s_1..s_m) <= s_{m+1} <= max K(s_1..s_m) for ALL m <= n, where
  max K_S = s_1·(n−1)! + s_2·(n−2)! + ... + s_n·0! + 1 and
  min K_S = 2·s_n − max K_S. The valid-extension condition at position N is
  therefore a factorial-weighted functional of the ENTIRE prefix — no bounded
  window of recent rows determines it (the weights reach all the way back to
  s_1). The state space cannot be finite in K,W.

  (2) Muney 2026 (arXiv:2606.23721, "Holes in Valid-Extension Sets of Finite
  Gilbreath Sequences"): the previously-proposed characterization that the
  valid-extension set fills a natural parity interval around the last term is
  FALSE — there are interior holes, smallest at length 5 for (2,3,5,9,15). The
  correct criterion is an order-sensitive analogue of the Brown completeness
  criterion for subset sums — again a global, order-dependent condition on the
  whole sequence, not a local window.

  (3) The "trap state" hope is exactly what Eppstein 2011 ("Anti-Gilbreath
  sequences") refutes for the general class: for any unbounded monotone f(n)>=2
  he builds a 2-then-odds sequence with gaps <= f(n) whose right edge switches
  between 1 and other values INFINITELY OFTEN (leaves and re-enters the "good"
  regime indefinitely). His construction extends the prefix "backwards from the
  right", and the escape condition is gap > row-sum of the ENTIRE previous row —
  a global quantity. So the good component is NOT a trap in general; proving the
  primes stay in it is equivalent to (not easier than) the conjecture itself.

  The one genuinely useful object this approach surfaces is Muney's valid-
  extension set, which is the backward-extension analogue of the run's leading
  {0,2}-block. But its exact membership criterion is global, so it does not give
  a finite-state induction; it re-describes the regeneration obstruction rather
  than resolving it.
precedent: >
  - https://doi.org/10.48550/arXiv.2606.23721 (Muney 2026, exact global criterion,
    holes, Brown-completeness analogue, enumeration through length 11)
  - https://www.mdpi.com/2227-7390/11/18/4006 (Alkan et al. 2023, Gilbreath
    polynomials, factorial-weighted min/max K criterion)
  - https://11011110.github.io/blog/2011/02/20/anti-gilbreath-sequences.html
    (Eppstein 2011, backward construction, infinite escape/re-entry)
holding-claims: larger
  anti-gilbreath-construction, gilbreath-polynomials-imply-gc
falsifies: >
  That there exists a finite (K,W) such that the valid-extension set depends only
  on the last K rows within a window of width W. Alkan's criterion has factorial
  weights reaching to s_1, and Muney's is order-sensitive over the whole prefix,
  so no fixed window suffices as N grows.
buy: >
  Restates regeneration as a global extension condition but offers no finite
  algorithm: the exact criteria in the literature are as hard to check as the
  conjecture and do not localize. Marked refuted.
first-step (retired): >
  Computing extension sets for N=1..100 and checking Markovianity could only
  confirm non-locality empirically; the exact global criteria (Alkan factorial
  bound, Muney order-sensitive completeness) already decide the question
  structurally. Not worth running as a route to a proof.
```

Fenced claim:

```claim
id: valid-extension-nonlocal
statement: The valid-extension set of a finite Gilbreath sequence is not determined by any bounded window of recent rows: Alkan et al. 2023 give the criterion min K(s_1..s_m) <= s_{m+1} <= max K(s_1..s_m) for all m, with max K_S = s_1·(n−1)! + ... + s_n·0! + 1 (factorial weights over the whole prefix); Muney 2026 give an order-sensitive analogue of Brown's subset-sum completeness criterion. Hence the finite-state Markov automaton of the backward-extension approach has no finite state space. The trap-state hope also fails in general: Eppstein 2011 builds 2-then-odds sequences with gaps <= f(n) whose right edge leaves and re-enters 1 infinitely often.
hypotheses: finite Gilbreath sequences; primes as special case.
holds-here: yes
status: sourced (exact criteria asserted by the papers; not independently reproduced here, consistent with each other and with Eppstein's construction)
bearing: refutes the finite-state local-decidability assumption; the valid-extension criterion is global in the sequence prefix, so backward-extension cannot be a finite induction independent of the primes' special structure.
anchor: research/approaches/backward-extension-automaton.md
```
