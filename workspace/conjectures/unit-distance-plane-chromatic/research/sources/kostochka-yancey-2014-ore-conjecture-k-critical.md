# Kostochka–Yancey: Ore's conjecture on color-critical graphs is almost true

**Subject:** The sharp lower bound on the number of edges in a k-critical
graph — the analytical spine of the discharging approach to the size-bound
rung (a 5-critical unit-distance graph cannot be too small, because its edge
count must exceed the unit-distance density ceiling). General graph theory,
non-planar, does not rely on the four-colour theorem.

## Source
- A. Kostochka, M. Yancey, *Ore's conjecture on color-critical graphs is
  almost true*, Electron. J. Combin. 21(1) (2014) #P1.7; arXiv:1209.1050
  (2012 preprint). Retrieved via server-side retrieval (`read_sources`); the
  arXiv/publisher full text is blocked at this run's network boundary.
- Source URL: https://arxiv.org/abs/1209.1050

## Exact statement

**Definition.** `G` is **k-critical** if `chi(G) = k` but every proper
subgraph has `chi < k`. Let `f_k(n)` be the minimum number of edges in an
n-vertex k-critical graph.

**Theorem (Kostochka–Yancey).** If `k >= 4` and `G` is k-critical, then

    |E(G)| >= ceil( ((k+1)(k-2) n - k(k-3)) / (2(k-1)) )

i.e. for `n >= k`, `n != k+1`:

    f_k(n) >= F(k,n) := ( (k+1)(k-2)n - k(k-3) ) / (2(k-1)).

This bound is **exact**:
- for `k = 4` and **every** `n >= 6`;
- for `k >= 5`, when `n ≡ 1 (mod k-1)`, `n != 1`.

**Specialised values.**
- `k = 5`: `f_5(n) >= F(5,n) = ((6)(3)n - 5(2))/8 = (18n - 10)/8 = (9n - 5)/4
  ≈ 2.25 n`. An average degree just above 4.25, sharp when `n ≡ 1 (mod 4)`.
- `f_k(2k) = k^2 - 3`; `f_k(3k-2) = 3k(k-1)/2 - 2`.

**Corollary refuting the discharge-meets-ceiling route (run's own hand check,
recorded in `research/approaches/discharging-minimal-counterexample.md`).** A
5-critical unit-distance graph must have `>= (9n-5)/4` edges by this bound,
but any n plane points have `<= C n^{4/3}` unit distances (SST). Setting
`(9n-5)/4 <= C n^{4/3}` first stops forcing a contradiction between n=9 and
n=10 even at the impossible constant C=1 — so the provable N from this clash
is `<= 9`, below the nauty census's n=11. A sharper unit-distance-specific
density/angle bound is needed to extend; that is the open problem itself.

## Method
Constructive potential-based argument: the paper defines k-potentials `rho_k(R)`
and uses induced-subgraph structure, improving the classical bounds of Gallai
and Dirac and the subsequent ones of Krivelevich and Kostochka–Stiebitz. It
yields a polynomial-time algorithm to (k-1)-colour any graph satisfying the
local density condition `|E(G[W])| < F_k(|W|)` for all `W` with `|W| >= k`.
Also gives a short proof of Grötzsch's theorem (triangle-free planar graphs are
3-colourable) as an application.

## Why it matters here
The size-bound rung ("prove every unit-distance graph on at most N vertices is
4-colourable for the largest N provable") needs the edge-count lower bound on
a hypothetical minimal 5-chromatic (5-critical) unit-distance graph. The
Kostochka–Yancey bound is the sharpest such bound. The run's own computation
(discharging approach, `status: refuted`) showed this exact bound cannot alone
force a contradiction past n=9, but the theorem is the correct sharp reference
for the attempt and the reason that route stalls is recorded, not silent.

## Basis and status
- Statements retrieved verbatim from the abstract/intro via server-side
  retrieval.
- Not machine-re-derived here (general graph theory); the run's own exact
  oracle is the unit-distance side. The n=9..10 clash is the run's hand check
  recorded in the refuted discharging approach, an arithmetic computation
  (programmatically checkable).

## Claim block
```claim
id: kostochka-yancey-2014-critical-edge-bound
statement: For k >= 4 and an n-vertex k-critical graph G with n >= k, n != k+1,
  |E(G)| >= F(k,n) = ((k+1)(k-2)n - k(k-3))/(2(k-1)); exact for k=4 all n >= 6
  and for k >= 5 with n ≡ 1 (mod k-1). In particular f_5(n) >= (9n-5)/4.
hypotheses: G finite simple k-critical graph, k >= 4, n >= k, n != k+1.
holds-here: YES — a minimal 5-chromatic unit-distance graph would be 5-critical,
  so its edge count satisfies the bound verbatim; the size-bound rung's edge-
  lower-bound ingredient.
status: asserted-by-source (Kostochka–Yancey 2014, arXiv:1209.1050, EJC, peer-
  reviewed; not re-derived here).
bearing: the sharpest edge-count lower bound for the size-bound rung; combined
  with the unit-distance ceiling u_2(n)=O(n^{4/3}) it bounds how small a
  5-chromatic UDG can be (fails to force a contradiction past n=9, per the
  run's own computation in the refuted discharging approach).
anchor: research/sources/kostochka-yancey-2014-ore-conjecture-k-critical.md
falsifies: a 5-critical unit-distance graph on n vertices with fewer than
  (9n-5)/4 edges — impossible by the theorem, which classifies the min-edge
  problem for general (non-planar) graphs.
```
