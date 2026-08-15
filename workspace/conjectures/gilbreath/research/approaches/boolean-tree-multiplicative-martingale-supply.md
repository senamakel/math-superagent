```approach
idea: Represent ν₂/n as the fraction of nodes d of the binary submask tree where the product f(d) = Π_{j⊆d} u_j equals −1 (u_j = (−1)^{h(j)}, h the mod-4 switch bit). This turns the supply question into a non-degeneracy question for a tree-indexed multiplicative martingale, and the collapse class into the degenerate case where the tree product is eventually identically 0.

mechanism: Split d at its top bit: f(d) = u_d · f(d∖top) · f̃(d∖top), where f̃ is the product over the shifted subtree {j + top : j ⊆ d∖top} — a 2×2 branching of the product over the two halves of the Boolean lattice. If u has no tree-correlation, f is a genuine martingale indexed by the tree and by the martingale CLT / branching-product Lyapunov theory (Furstenberg–Kesten) the sign density → 1/2; if u is 2-adically structured (period 2^k), the two subtrees cancel identically for deep d and f degenerates, giving ζ(h) sparse (exactly `dyadic-collapse-proved`). The new invariant is the non-degeneracy of this tree product — its second-moment/Lyapunov growth rate along the tree — and the general-class theorem is "non-degenerate tree product ⟹ ν₂/n ≥ c". This is a probability-on-the-tree setting for the supply side, distinct from the refuted edge-martingale route (which claimed independence of a two-tap XOR where none exists): here the submask product introduces one genuinely fresh factor u_d per node, so the tree-martingale structure is exact, and the failure mode is degeneracy (subtree cancellation), not false independence.

status: refuted
killed-by: Same fatal identification as the Gowers candidate, plus the named
  martingale/Lyapunov theorems do not supply a non-degeneracy-to-density
  transfer on this object.
  (1) WRONG OBJECT. The proposal reads ν₂/n as "the fraction of nodes d of the
  Boolean submask tree where f(d) = Π_{j⊆d} u_j = −1", i.e.
  ν₂(q_n) = #{d : ζ(h)[d] = 1} with ζ(h)[d] = (1−f(d))/2 the F₂ subset-zeta
  fold. That is the identical fold-PARITY identification the run has already
  refuted (`boolean-influence-parity-subset-density`, `thue-morse-sublinear-supply-witness`):
  ζ(h)[d] is a mod-4 parity that fires on halved values odd (actual 2,6,10,…),
  NOT a {0,2}-membership count. Thue–Morse: TM ν₂(100)=27 vs fold count 7,
  first mismatch at n=1. So a branching-product statement about f(d) =
  (−1)^{ζ(h)[d]} certifies the sign density of a product that is NOT ν₂/n. The
  martingale is about the wrong observable from the first line.
  (2) THE NAMED THEOREMS apply to a different tree. The branching-product /
  multiplicative-cascade literature — Benjamini–Peres tree-indexed processes
  (1992 chapter, 1994), branching random walks and Martingale convergence
  (Biggins 1977 / JAP; Kesten–Stigum), nondegenerate limits of derivative
  martingales (Chen, Adv. Appl. Prob. 2016, Biggins–Kyprianou lineage) — is
  about martingales on trees with INDEPENDENT (or Markov) edge/population
  randomness whose non-degenerate limit is a fixed point of a Mandelbrot
  smoothing transform. Here the "tree" is the deterministic submask poset of a
  FIXED bit string; the factors u_j are NOT independent (they are the prime
  gaps mod 4, deterministically given), and the object whose second-moment
  growth the proposal wants to measure is a deterministic product over
  submasks, not a random martingale. No theorem in this body gives
  "non-degenerate tree product ⟹ sign-density ≥ c" for a fixed non-random
  submask product, and none is cited. The Furstenberg–Kesten / Kesten
  Lyapunov machinery governs PRODUCTS OF RANDOM MATRICES under i.i.d. or
  ergodic stationary randomness; the submask products across distinct d SHARE
  factors (the file's own speculation flag concedes this), so the clean CLT /
  Lyapunov statement for independent increments does not apply.
  (3) Where the branching-product structure is real, it is already the wrong
  shape for G-supply: `subset-zeta-preserves-automaticity-christol` shows the
  fold ζ(h) of a 2-automatic h (period-2^k, Thue–Morse) has rational limiting
  density, and Thue–Morse is the standing witness that NON-degenerate-looking
  (density-1/2, richly structured) switch bits still give SUBLINEAR true ν₂.
  So the collapse/non-collapse split the tree-product dictionary wants is not
  carried by the product's degeneracy even in principle.
  (4) Independently: no source applies tree-indexed multiplicative
  martingales / multi-type branching / Mandelbrot cascades to the Gilbreath or
  iterated-absolute-difference problem (none found). The linear supply bound
  for the primes stays on the named-open two-point mod-4 correlation
  (`abgs-2011-s9-mod4-switch-limit-open`), not on a tree-product
  non-degeneracy statement.
precedent: >
  Sourced: Benjamini–Peres, "A Correlation Inequality for Tree-Indexed Markov
  Chains" (1992, doi:10.1007/978-1-4612-0381-0_2) and "Tree-indexed random
  walks on groups and first passage percolation" (1994, doi:10.1007/bf01311350);
  Biggins "Martingale convergence in the branching random walk" (J. Appl. Prob.,
  Kesten–Stigum-lineage); Chen "A necessary and sufficient condition for the
  nontrivial limit of the derivative martingale" (Adv. Appl. Prob., 2016);
  Su, "Branching random walks and contact processes on Galton–Watson trees"
  (arXiv:1311.3616).
  Internal claims: thue-morse-sublinear-supply-witness,
  dyadic-separating-invariant-three-strings, dyadic-collapse-proved,
  subset-zeta-preserves-automaticity-christol,
  subset-zeta-rational-substitution-verified.
  Sibling refuted approach: boolean-influence-parity-subset-density.
  No source was found applying tree-indexed multiplicative martingales /
  branching products to the Gilbreath problem.
buy: The single durable fact is that multiplicative-cascade non-degeneracy is
  a real distinction in branching processes, but the submask products here are
  deterministic, non-independent, shared-factor objects to whose sign density
  no named martingale theorem transfers. Nil — the object is the wrong one and
  the named theorems cannot fire on it. Retire it; the supply-side separating
  invariant stays the measured 2-adic spectral mass
  (`dyadic-linear-complexity-supply`), not a tree martingale.
first-step: Compute the exact tree-product recursion on the four families (period 2^k, period 3, Thue–Morse, real prime switch bit to n ≤ 2·10^5) and measure the second-moment growth rate E_d f(d)² restricted to level sets of the tree (the branching-product "Lyapunov exponent") as a function of n; check that collapse words have decaying/degenerate growth and primes/odd-period have non-degenerate growth.
```

## Established vs speculation

- **Established:** the submask factorization `ζ(h)[d] = Σ_{j⊆d} h[j]` is the held `rule90-interior-xor` / Lucas identification; `dyadic-collapse-proved` gives period 2^k ⟹ ζ(h) sparse, which is precisely the degeneracy claim; Thue–Morse has sublinear ν₂ (`thue-morse-sublinear-supply-witness`).
- **Speculation:** the clean CLT/Lyapunov statement "non-degenerate increments ⟹ sign density → 1/2 with Gaussian fluctuations" is standard for independent increments but the submask products across distinct d share factors; whether a quantitative non-degeneracy condition (bounded second moment growth away from 0) suffices for a lower bound on the sign density is the load-bearing open step and must be checked against the branching-product literature (Furstenberg–Kesten, Benjamini–Peres, tree-indexed martingales).

## Scholze gate

The reformulation must reproduce `dyadic-collapse-proved` and `thue-morse-sublinear-supply-witness` as the degenerate/sublinear pole of one tree-process, and `dyadic-oddfactor-infimum-bounded` as the non-degenerate pole. If the tree-product growth rate does not cleanly split period-2^k from period-3, the representation is not yet worth having.

## Falsifier

Smallest input that breaks it: a word that is 2-adically structured (collapse) but whose tree product has non-degenerate second-moment growth, or a non-structured word with degenerate growth. The first such inversion refutes the dictionary; the computation in the first step is exactly this test.
