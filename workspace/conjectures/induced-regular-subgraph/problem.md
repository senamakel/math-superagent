# Large induced regular subgraphs

*Erdős Problem #82 (erdosproblems.com/82), conjectured by Erdős, Fajtlowicz and
Staton; stated in [Er93, p.340], [Er95], [Er97d].*

## Statement

A graph is **regular** if all its vertices have the same degree (the empty graph
and the complete graph are both regular). Let

```
F(n) = max { k : every graph on n vertices has an induced regular subgraph on >= k vertices }.
```

> **Conjecture.** `F(n) / log n -> infinity`.

The dual formulation is the one the computation uses:

```
G(k) = min { m : every graph on m vertices has an induced regular subgraph on >= k vertices },
```

so `F(n) >= k` iff `n >= G(k)`. In this language the conjecture is exactly

> **`G(k) <= 2^{o(k)}`.**

## What the statement does and does not say

- **Induced**, not arbitrary. The subgraph on a vertex set `S` is the one `G`
  induces on `S`; you may not delete edges. This is what makes the problem hard —
  a *spanning* regular subgraph question is entirely different.
- **Regular includes empty and complete.** So a clique or an independent set
  counts, which is why Ramsey's theorem immediately gives `F(n) >> log n`. **The
  conjecture asks to beat Ramsey**, and that is its whole content: is there
  always something regular that is *not* just a trivial (empty or complete)
  subgraph?
- The related Erdős question, worth keeping in view: if `t(n)` is the largest
  guaranteed *trivial* subgraph (`t(n) >> log n` by Ramsey), is
  `F(n) - t(n) -> infinity`?
- Both `F(n)` and `G(k)` are **finite exactly computable numbers**, and the known
  exact values are small. This is an unusually well-grounded problem for a
  computational run.

## Where the literature is known to have got to — verify each

Nothing below may be cited without a primary source and a claim block.

- **Exact values.** `F(5) = 3`, `F(7) = 4`. In the dual formulation,
  Fajtlowicz, McColgan, Reid and Staton [FMRS95] showed
  ```
  G(1) = 1,  G(2) = 2,  G(3) = 5,  G(4) = 7,  G(5) >= 12,
  ```
  and **Boris Alexeev and Brendan McKay** computed `G(5) = 17`, `G(6) >= 21`,
  `G(7) >= 29`. **Dyson and McKay [DyMc26]** improved this to `G(7) >= 30` and
  proved `G(k) >> k^2` — specifically `G(k) >= (9/163) k^2` for large `k`.
  Verify every one of these numbers, and **reproduce `G(3) = 5` and `G(4) = 7`
  from scratch**: they are within exhaustive reach and they calibrate the
  oracle.
- **Lower bound on `F`.** Ramsey's theorem gives `F(n) >> log n`. That is the
  bound the conjecture asks to beat, and **it has not been beaten.**
- **Upper bounds on `F`.** Bollobás observed `F(n) << n^{1/2 + o(1)}`;
  Alon, Krivelevich and Sudakov [AKS07] improved this to `n^{1/2}(log n)^{O(1)}`;
  Dyson and McKay [DyMc26] to `F(n) << n^{1/2}`.

So the bracket is
```
log n   <<   F(n)   <<   n^{1/2},
```
a gap between a logarithm and a square root that has not been closed from below
at all. **Say this in `CONTEXT.md` on day one: nothing better than Ramsey is
known for the lower bound, and beating Ramsey by any amount — `F(n) >> (log n)^{1+c}`
— would be a genuine result.**

- See also Erdős Problem #1031 for a neighbouring question on induced regular
  subgraphs.

## The obstruction, stated honestly

1. **Ramsey is the only known lower bound, and it uses nothing about
   regularity.** It finds a clique or an independent set — the two *trivial*
   regular graphs. Every attempt to do better has to find a non-trivial regular
   induced subgraph, and there is no known method that produces one. **An
   approach that ends up producing a clique or an independent set has not
   improved anything, and the run must say, of every argument, which regular
   subgraph it produces.**

2. **The upper bound is at `n^{1/2}` and is believed close to the truth.**
   Constructions (random graphs, and structured examples with few regular
   induced subgraphs) sit around `n^{1/2}`, and `G(k) >> k^2` from below matches
   it. So the *truth is probably near `n^{1/2}`*, and the conjecture — merely
   beating `log n` — is a very weak statement that is nonetheless open. **That
   asymmetry is the reason to work on this problem: the target is far below what
   is believed true.**

3. **Small exact values are computable and the sequence is short.** `G(5) = 17`
   took serious computation, `G(6)` and `G(7)` are only bounded. **Improving a
   bound on `G(6)` or `G(7)` is a concrete, checkable, finite objective** —
   a lower bound needs one explicit graph, and an upper bound needs an
   exhaustive argument.

Stated as the thing to beat:

> **Every known lower bound produces a trivial (empty or complete) regular
> induced subgraph. A proof of the conjecture must produce a non-trivial one, or
> must exploit that avoiding non-trivial regular induced subgraphs forces the
> graph to be Ramsey-like in a way that can then be beaten.**

Say which of these the approach attempts.

## The oracle: exact `G(k)`, and a witness checker

1. **`maxRegularInduced(G)`** — the largest `k` such that `G` has an induced
   regular subgraph on `k` vertices. This is a search over vertex subsets and
   must **not** be done by enumerating all `2^n` of them past about `n = 25`.
   Encode as SAT/ILP: choose a subset `S` and a target degree `d`, and require
   every chosen vertex to have exactly `d` chosen neighbours — a cardinality
   constraint per vertex. Loop over `d`. Verify by hand on `C_5` (regular, so
   the whole graph, `k = 5`) and on the Petersen graph.

2. **`G(k)` exactly, as far as it goes.** A lower bound `G(k) > m` needs a single
   explicit graph on `m` vertices with no induced regular subgraph on `k`
   vertices — **cheap to verify, and the natural target.** An upper bound
   `G(k) <= m` needs every graph on `m` vertices checked, i.e. exhaustive
   generation up to isomorphism (nauty/geng-style) with early pruning. **Say
   which half of any claimed value was actually done.**

3. **Certificate discipline.** Every lower-bound graph is stored explicitly (in
   graph6 or an adjacency list) in `code/out/` and re-verified by an independent
   checker, not by the search that found it. A search and its own checker
   failing the same way is the standard failure here.

4. **The falsification oracle.** Any claimed bound is evaluated against
   `G(3)=5`, `G(4)=7`, `G(5)=17`, `G(6)>=21`, `G(7)>=30`, `F(5)=3`, `F(7)=4`.
   **A claimed lower bound on `F` exceeding `F(5)=3` or `F(7)=4` is false —
   refuted, not weakened.** Any claimed asymptotic must be evaluated at these
   points before it is believed.

Expect `k <= 7` to be unable to distinguish `log n` from `n^{1/2}`. Compute it
anyway; it is the only thing standing between the run and a plausible false
theorem.

## Leads — verify each before relying on it

- **Dyson–McKay [DyMc26]**: `F(n) << n^{1/2}`, `G(k) >> k^2`, `G(7) >= 30` — the
  current state of the art, and the source of the extremal constructions.
- **Alon–Krivelevich–Sudakov [AKS07]**: the `n^{1/2}(log n)^{O(1)}` upper bound
  and the random-graph analysis behind it.
- **[FMRS95]** and the Alexeev–McKay computation of `G(5) = 17`: the search
  method, the symmetry breaking, and the hardware. That is the template for any
  attempt on `G(6)`.
- **Ramsey lower bounds** and exactly how much slack there is between "clique or
  independent set" and "regular induced subgraph" in a random graph.
- **Erdős Problem #1031**, the neighbouring induced-regular question.
- **Degree sequences and near-regularity**: results guaranteeing induced
  subgraphs whose degrees vary by at most one, which are often much easier and
  may bound how far the exact-regularity requirement is really costing.
