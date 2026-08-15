# Depth-survival ladder

The goal stated as an exact classification of the gap word. Every row of the
prime triangle reduces (parity, `gilbreath-reduces-to-second-in-02`) to the
single value `A_k(1)`, and for a 2-then-odds input that value is a **nested
absolute value of the even gaps**:

```
A_1 = (1, g_1, g_2, g_3, ...),   g_1 = 2, all g_i even positive
A_2(1) = |g_1 - g_2|
A_3(1) = ||g_1 - g_2| - |g_2 - g_3||
A_4(1) = |||g_1 - g_2| - |g_2 - g_3|| - ||g_2 - g_3| - |g_3 - g_4|||
```

so the conjecture is the statement that **for every k, the prime gap word
`(2, g_2, g_3, ...)` lies in the depth-k survival set**

```
S_k = { gap words of length k : A_k(1) ∈ {0,2} }.
```

The existing ladders attack `S_∞` through the block/recharge machinery; this
one attacks it **through the finite sets `S_2, S_3, S_4, ...` themselves**,
which is a strictly different object. The climb is: classify `S_k` for fixed
small k (finite, settleable today), observe that each `S_k` is finite even
over unbounded gaps, and then meet the one difficulty that makes the union
over k open.

```ladder
goal: For A_0 = (2,3,5,7,11,13,...) the primes in order and A_{k+1}(i) = |A_k(i) − A_k(i+1)|, prove A_k(0) = 1 for every k ≥ 1 (Gilbreath's conjecture, Proth 1878 / Gilbreath 1958); equivalently, for the prime gap word g_1 = 2, g_i = p_{i+2} − p_{i+1}, prove (2, g_2, g_3, ...) ∈ S_k for every k, where S_k = {gap words of length k : A_k(1) ∈ {0,2}}.
difficulties: infinite-horizon, leftward-drift, unbounded-gap-alphabet, deterministic-arrangement
status: open
```

The four difficulties, named as specific obstructions:

- `infinite-horizon` — the quantifier `∀ k ≥ 1` over the infinite triangle; a
  classification of `S_k` for every fixed k does not by itself give the `∀k`
  statement, because the family `{S_k}` has no inductive/telescoping structure.
- `leftward-drift` — the specific obstruction that `A_k(1)` is **not** a
  bounded-window function of the gap word: a large gap far to the right can
  propagate one column left per row and reach column 1 after enough descents.
  This is why `S_k` genuinely grows in complexity with k and why knowing
  `A_k(1) ∈ {0,2}` says nothing about `A_{k+1}(1)` without tracking the whole
  row. It is the "uncontrolled far entries" difficulty of the regeneration
  ladder, restated as non-locality of the nested absolute value.
- `unbounded-gap-alphabet` — prime gaps take arbitrarily large values, so the
  prime gap word is not contained in any fixed finite alphabet `{2,4,...,2m}`.
- `deterministic-arrangement` — the prime gap word is one fixed deterministic
  sequence with no independence/renewal law, so no probabilistic argument
  lower-bounds how often it lands in `S_k`.

```rung
id: R-depth2-survival-exact
statement: For A_1 = (1, g_1, g_2, ...) with g_1 = 2 and g_2 any even positive integer, A_2(1) = |2 − g_2|, hence A_2(1) ∈ {0,2} ⟺ g_2 ∈ {2,4}. So S_2 = {(2, g_2) : g_2 ∈ {2,4}} exactly: depth-2 survival is the single condition g_2 ∈ {2,4}. (Established by the one-line arithmetic |2−g_2| ∈ {0,2} ⟺ g_2 ∈ {0,2,4} ∩ even ⟹ g_2 ∈ {2,4}, which is the depth-2 instance of the proved reduction `gilbreath-reduces-to-second-in-02`; strictly weaker than the settled R-lipschitz-corner, which additionally needs |g_i − g_{i+1}| ≤ 2 for all i to make the whole row 2 the corner.)
off: infinite-horizon, leftward-drift, deterministic-arrangement
stance: settled
merge: Turn leftward-drift back on. At depth 2 only one gap matters; at depth 3 the value A_3(1) = ||2 − g_2| − |g_2 − g_3|| depends on two gaps, the first sign of non-locality. First move: enumerate S_3(m) over a finite alphabet {2,4,...,2m} and read off the arithmetic structure — this is the next rung and it is settleable today.
```

```rung
id: R-depth3-survival-exact
statement: For A_1 = (1, 2, g_2, g_3, ...) with g_2, g_3 even positive, A_3(1) = ||2 − g_2| − |g_2 − g_3||, so A_3(1) ∈ {0,2} ⟺ that quantity is 0 or 2. Over the finite alphabet {2,4,...,2m} the depth-3 survival set S_3(m) = {(g_2,g_3) ∈ {2,4,...,2m}² : ||2−g_2| − |g_2−g_3|| ∈ {0,2}} is exactly enumerable; the rung is to enumerate it and give a closed-form description (it is a finite union of linear families, since the condition is a disjunction of the four equations |2−g_2| − |g_2−g_3| ∈ {0,2} with sign choices).
off: infinite-horizon, leftward-drift, unbounded-gap-alphabet, deterministic-arrangement
stance: open
merge: This is the rung to attack next. It is a finite case analysis over two even integers (SAT/CP-SAT or a direct loop over m ≤ ~10⁴), and the deliverable is the exact set S_3(m) plus its density |S_3(m)|/m². Turning leftward-drift back on means depth 4, where A_4(1) depends on three gaps and the first genuine three-way interaction appears — that is R-depth4-survival-exact.
```

```rung
id: R-depth4-survival-exact
statement: For A_1 = (1, 2, g_2, g_3, g_4, ...) with g_2, g_3, g_4 even positive, give the exact depth-4 survival set S_4(m) = {(g_2,g_3,g_4) ∈ {2,4,...,2m}³ : A_4(1) ∈ {0,2}}, where A_4(1) = |||2−g_2| − |g_2−g_3|| − ||g_2−g_3| − |g_3−g_4|||.
off: infinite-horizon, leftward-drift, unbounded-gap-alphabet, deterministic-arrangement
stance: open
merge: Turn unbounded-gap-alphabet back on. The key bridge is that for ANY fixed depth k the survival set is finite even over unbounded gaps — settle that first (R-depth-k-finite) — then climb. For depth 4 the search is a cube over the alphabet, still small at m ≤ 10³, and the structure of S_4(m) is the first place where the non-telescoping of the family {S_k} becomes visible.
```

```rung
id: R-depth-k-finite
statement: For every fixed k ≥ 1, the set S_k of gap words (2, g_2, ..., g_k) with all g_i even positive satisfying A_k(1) ∈ {0,2} is FINITE: each gap is bounded by an explicit function of the others and k (a nested absolute value is bounded above by the maximum gap, and the condition A_k(1) ≤ 2 forces each gap below a computable bound). So the depth-k survival problem is a finite (though doubly-exponential in k) search even without a bounded alphabet.
off: infinite-horizon, leftward-drift, deterministic-arrangement
stance: failed
killed-by: (claim depth-k-finite-refuted) — S_3 is infinite. For fixed k=3, g_1=2, g_3=2, every even g_2=2M satisfies A_3(1) = ||2−2M| − |2M−2|| = |X−X| = 0 ∈ {0,2} by |a−b|=|b−a|, so (2,2M,2) ∈ S_3 for all M: g_2 is unbounded while g_1, g_3, k are all fixed. The claim "each gap bounded by a function of the others and k" fails; the rung's stated route (finite search over S_k) is defeated as written. Full detail: research/weakened/depth-k-finite-refuted.md.
merge: The depth-k survival sets are NOT all finite even over unbounded even gaps; the ladder's invariant "S_k is a finite set for each fixed k" is wrong. The real climb (infinite-horizon via leftward-drift) is untouched, but finiteness of S_k cannot be used as a route. Note S_k is finite when the gaps are confined to a bounded alphabet (e.g. {2,4,...,2m}) for fixed k — but that is a different claim from unbounded-gap finiteness and does not survive turning unbounded-gap-alphabet back on.
```

```rung
id: R-carved-gap24-infinite
statement: For A_0 = (2,3,x_1,x_2,...) with every x_i odd, x_1 − 3 = 2, and x_{i+1} − x_i ∈ {2,4} for all i (gaps after the first all equal 2 or 4), prove A_k(1) ∈ {0,2} for all k ≥ 1. This is the goal with the unbounded, irregularly arranged gap word switched off, and it is the first infinite-horizon rung this ladder reaches. It strictly generalises the proved consecutive-odds case and is NOT killed by Eppstein's construction or Colonna's deletion counterexamples (those need a ≥6 gap).
off: unbounded-gap-alphabet, deterministic-arrangement
stance: open
merge: Turn deterministic-arrangement back on. This rung is tracked on the recharge-ladder as R-carved-gap24 and the spike-propagation-ladder as R-gaps-24; empirical support is 0 deaths among 48 measured {2,4} sequences to depth 4000, not a proof. The single step from here to the primes is restoring the real (unbounded, deterministic) gap word and asking whether it stays in S_k for all k — the goal.
```

```rung
id: R-goal
statement: For the prime gap word g_1 = 2, g_i = p_{i+2} − p_{i+1}, prove (2, g_2, g_3, ...) ∈ S_k for every k ≥ 1, i.e. A_k(1) ∈ {0,2} for all k — Gilbreath's conjecture.
off:
stance: open
merge: none — top of ladder.
```
