# Precedent report — the three reformulations (research agent)

Scope: take each of the inventor's three candidate reformulations to the
literature, report what each is called, the precise theorem it relies on and
whether its hypotheses hold here, whether anyone has applied it to SUPPLY, and
what it buys. Verdicts are recorded inside each `research/approaches/*.md`
file; this is the consolidated account.

## 1. `anf-mobius-reed-muller` — Reed–Muller / Möbius inversion

**Status: grounded (identity) / payoff ungrounded.**

What it is called: the **F₂ Möbius / Zhegalkin transform** computing the
**algebraic normal form (ANF)** of a Boolean function. Confirmed by the
cryptanalysis/coding literature: the coefficient of the monomial with support
`{i1..ik}` is `⊕_{x_i ≤ a_i} f(x)` — exactly `a_d = ⊕_{x⊆d} g(x)` here
(Springer algebraic-degree paper; Barbier–Cheballah–Le Bars arXiv:2004.11146).

Theorem it relies on and whether it holds here: the ANF-coefficient (Möbius)
formula `b_(a1..an) = ⊕_{x≤a} f(x)`, which is a bijection (self-inverse
transform). It **holds here** — the identity reduces to one substitution,
`x = d−o` bijective on submasks of `d`, giving `T(n,d) = a_d`. This reproduces
claim `supply-fold-submask-zeta-involution` in coding-theoretic language: the
Scholze gate passes.

Anyone applied it to SUPPLY? **No.** No source applies Reed–Muller weight
enumeration or the MacWilliams identity to a sliding-window ANF-support lower
bound — and the RM weight-spectrum problem is itself open (Carlet 2023, 2024),
so this hands the problem to a category that is not easier. The RM machinery
bounds Hamming weight of *low-degree* codewords; our windows are arbitrary and
our quantity is ANF-support size, not function weight. The uncertainty bounds
already on disk (Donoho–Stark, Meshulam, Tao) point the same direction — their
extremals are exactly the closed-door low-weight inputs — so no input-free lower
bound is available. **Change of language, not yet change of ground.**

## 2. `hypergraph-cut-cheeger` — hypergraph cut / isoperimetry

**Status: refuted** (false kernel premise + degenerate Cheeger machinery).

The refutation was already recorded on the kernel side (d=0 singleton edge on
[d∈0,n−1]; on the operative [2,n−1] range the kernel is span(even-alt, odd-alt),
nullity 2 — `fold-rank-is-n-2-nullity-2-alternating`, not span(all-ones)). The
literature side independently kills the Cheeger hope: all hypergraph Cheeger
inequalities are **k-uniform** (Mulas 10.1007/s00373-021-02348-z; Banerjee;
Xu–Zhou), and the fold's hypergraph has edge sizes 1..n — wildly non-uniform.
The strongest non-uniform results (Lau–Tung–Wang arXiv:2211.09776) pay a factor
`log r` in the maximum hyperedge size `r ≈ n`, which swallows the linear
target. The fold is also an **F₂ parity coboundary**, not a real symmetric
Laplacian, so the spectral-cut transfer is not in the literature. And even had
the kernel premise held, the hypergraph is violently volume-imbalanced (vertices
near the centre on Θ(n) edges, ends on O(log n)), whose Cheeger constant is
~1/n — no bound of the needed shape can fire. Refutation stands on two
independent grounds.

## 3. `pascal-cascade-block-recursion` — dyadic cascade on ν₂(n)

**Status: grounded (block structure of the matrix) / recursion-on-weight
ungrounded.**

The crux — "Φ_n is an anti-diagonal slice, so it inherits a 2×2 block recursion
in n" — is exactly wrong, and the literature says so. The Sierpinski
self-similarity (Kronecker power `[[1,1],[1,0]]`; Fine's `a₂(n)=2^popcount(n)`;
Rowland arXiv:1001.1783 for prime powers; Kubelka; Barbé; Gamelin–Mnatsakanian)
lives on **rows/blocks/triangular regions**, not on the anti-diagonal slice.
The diagonal sequences are the **binomial sequences** of Cardell–Fúster-Sabater
(10.1155/2019/2108014): they are 2-regular *generators* of period-2^m sequences
(period-2^m binary strings are XORs of binomial sequences) — precisely the
`diagonal-2regular-automaton` route this candidate claims to be distinct from.
Northshield's (1,1)-diagonal sum gives the same functional-equation/2-regular
home. So block recursion is grounded for the full Pascal matrix rows
(reproducing `hofer-mod2-pascal-thue-morse-structure`), ungrounded for the
anti-diagonal slice that SUPPLY uses; the recursion on the *weight* would have
to be derived from scratch, and the literature gives no reason to expect a
small cross term. **The dyadic hope is better housed in the already-on-disk
2-regular/binomial-sequence reformulation than as a new weight-block recursion.**

## Negative results worth carrying forward

- **ν₂(n) is not in the OEIS** (20-term prefix, n=3..22, no entry): `oeis-nu2-not-catalogued` —
  no catalogued closed form to look up; structure must come from the problem.
- No source found applies **Reed–Muller / MacWilliams** to sliding-window
  ANF-support bounds; no source found applies **hypergraph Cheeger** to an
  F₂-parity coboundary with n-sized edges; no source found derives a
  **weight-block recursion** for an anti-diagonal Pascal-mod-2 slice. These are
  facts about absence of precedent, stated as such.

## Sources (exact URLs / DOIs)

- ANF/Möbius: Springer 10.1007/s12095-023-00660-4; arXiv:2004.11146.
- Reed–Muller weights: 10.3934/math.2024518; 10.1016/j.disc.2023.113568;
  techrxiv.23662062.
- Hypergraph Cheeger: 10.1007/s00373-021-02348-z; S0166218X25004329;
  arXiv:2211.09776; arXiv:1809.04396.
- Pascal self-similarity / row weights: arXiv:1001.1783 (Rowland);
  10.1155/2019/2108014 (Cardell–Fúster-Sabater); hdl.handle.net/1951/69939
  (Northshield); 10.1080/00150517.2004.12428445 (Kubelka).
- On-disk claims reproduced: `supply-fold-submask-zeta-involution`,
  `fold-rank-is-n-2-nullity-2-alternating`, `hofer-mod2-pascal-thue-morse-structure`.

Deliverable for this pass: three approach files updated with
`status`/`precedent`/verdict and a `killed-by` for the refuted one. The pass
did not execute code (no runner in this role); the invented checker
`code/out/anf_dictionary_check.py` remains unrun — flagged in the file.
