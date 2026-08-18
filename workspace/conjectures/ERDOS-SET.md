# The Erdős set: ten problems chosen for this harness

Selected 2026-08-18 from the 604 problems still marked open in the community
database behind erdosproblems.com (`teorth/erdosproblems`, `data/problems.yaml`,
cross-read against each problem's page).

**Selection criteria, in the order they were applied.**

1. **No prime-number problems.** Every problem tagged `primes`, and every
   problem whose difficulty is really a prime-distribution difficulty, was
   dropped.
2. **Polynomials preferred.** Four of the ten are about polynomials directly.
3. **Agent-friendly**, which here means three concrete things: the problem has
   an *exact* oracle a program can implement (exact rational or integer
   arithmetic, or a SAT/ILP decision procedure); it has **known small values**
   the oracle can be calibrated against, so a false claim dies to a finite
   computation; and its open content is stated as a bound or a construction
   rather than as a structure theory.
4. **Not already in this workspace.** Collatz (#1135), Erdős–Gyárfás,
   union-closed sets, the unit-distance chromatic number and the hypercube
   induced-degree problem are each already a workspace here.

| slug | # | subject | ground truth the oracle is calibrated on |
|---|---|---|---|
| `flat-littlewood-polynomials` | 1150 | is every `±1` polynomial's sup norm `> (1+c)√n`? | Parseval floor `√(n+1)`; Rudin–Shapiro; exact `m(n)` by exhaustion |
| `polynomial-sublevel-measure` | 1038 | `inf`/`sup` of `\|{\|f\|<1}\|`, `f` monic real-rooted in `[-1,1]` | `μ(x)=2`; `(x+1)(x-1)^m`; bracket `1.519 ≤ inf ≤ 1.835` |
| `lebesgue-l2-interpolation` | 1131 | `min ∫ Σ\|l_k\|²` — is it `2-(1+o(1))/n`? | `n=2`, nodes `{-1,1}`, `I=4/3`; Szabados kills the Legendre guess at `n=4` |
| `sidon-polynomial` | 324 | is some `f ∈ Z[x]` a Sidon set? | degrees 1,2,3 impossible; `x^4` collides; `x^5` collision-free |
| `property-b-hypergraph` | 901 | `m(n)`, fewest edges in a non-2-colourable `n`-uniform hypergraph | `m(2)=3`, `m(3)=7`, `m(4)=23` |
| `schutte-tournament` | 902 | `f(n)`, smallest tournament where every `n`-set is dominated | `f(1)=3`, `f(2)=7`, `f(3)=19` |
| `induced-regular-subgraph` | 82 | is `F(n)/log n → ∞`? | `F(5)=3`, `F(7)=4`, `G(3)=5`, `G(4)=7`, `G(5)=17` |
| `triangle-free-chromatic` | 1013 | `h_3(k)`, smallest triangle-free `k`-chromatic graph | `h_3(3)=5`, `h_3(4)=11` (Grötzsch), `h_3(5)=21` |
| `pancyclic-edge-surplus` | 1016 | `h(n)`, edge surplus of the sparsest pancyclic graph | `K_4` pancyclic, `C_n` not; exact `h(n)` for small `n` |
| `c4-min-degree-monotone` | 85 | is `f(n+1) ≥ f(n)` for the min degree forcing a `C_4`? | `f(4)=2`; Erdős–Rényi polarity graphs at `n=q²+q+1` |

Four of the ten (#901, #902, #82, #1016) share a shape worth noticing across
runs: a probabilistic upper bound and a counting lower bound, a factor-`n` or
factor-`log` gap between them, and no movement in sixty years. If more than one
runs at a time, the shared obstruction is itself worth a board post.

**Launch** — one container and one Cognee per problem:

```sh
./conjecture flat-littlewood-polynomials
./euler-tui --workspace conjectures/flat-littlewood-polynomials
```

Detached, so it outlives the terminal:

```sh
nohup ./conjecture <slug> > workspace/conjectures/<slug>/config/start.log 2>&1 &
```
