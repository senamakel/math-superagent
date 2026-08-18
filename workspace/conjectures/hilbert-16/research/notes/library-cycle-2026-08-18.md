# Library cycle 2026-08-18

## Search coverage
Searched current H16.2 status, DRR graphics, o-minimality/finite cyclicity, Abelian-integral bounds, and critiques of claimed solutions. Existing library prevented duplicate downloads for Gasull–Santana 2024, Speissegger 2018, Binyamini–Dor 2011, and Binyamini–Novikov–Yakovenko 2008; their local summaries/full sources were checked by the tool. A new full source is held at `research/sources/gasull-santana-2024-critique-attempt.full.md`, source URL in its header.

## Claim blocks

### Claim: H16.2 remains open
- **Statement:** For polynomial planar fields of degree at most n, uniform finiteness of H(n) remains open, including n=2.
- **Hypotheses:** Standard limit cycle = nonstationary periodic orbit isolated among periodic orbits; polynomial P,Q with degrees <= n.
- **Evidence class:** asserted-by-source, corroborated by Gasull–Santana 2024 and Buzzi–Novaes 2024.
- **Falsifier:** a refereed proof of a uniform degree-dependent bound.
- **Source:** https://arxiv.org/html/2407.13465; https://arxiv.org/html/2411.09594v1

### Claim: finite cyclicity is the uniform local target
- **Statement:** Roussarie's finite-cyclicity conjecture requires one N and neighborhoods U,V so every nearby parameter field has at most N cycles near the limit-periodic set; pointwise finiteness is insufficient.
- **Hypotheses:** finite-parameter family and limit-periodic set/graphic.
- **Evidence class:** asserted-by-source.
- **Falsifier:** a source proving pointwise finiteness alone implies the uniform statement.
- **Source:** https://ar5iv.labs.arxiv.org/html/1804.03585

### Claim: restricted Abelian-integral bounds
- **Statement:** BNY gives a uniform double-exponential bound for zeros of Abelian integrals for deg H <= n+1 and deg omega <= n; Binyamini–Dor gives an explicit bound linear in deg omega with dependence on deg H.
- **Hypotheses:** Hamiltonian polynomial, nonsingular ovals, first-order/nonconservative perturbation.
- **Evidence class:** asserted-by-source.
- **Falsifier:** a counterexample within the stated Hamiltonian/oval hypotheses.
- **Source:** https://ar5iv.labs.arxiv.org/html/0808.2952; https://arxiv.org/html/1108.1846

### Claim: claimed quadratic solution is refuted by lower growth
- **Statement:** The formula H(n)=2(n-1)(4(n-1)-2) cannot be a solution because known lower estimates grow at least on the order n^2 log n; the source gives an explicit recursive family contradiction for sufficiently large k and examples showing the proposed curvature criterion is not equivalent to standard limit cycles.
- **Evidence class:** asserted-by-source (the critique is held, not independently re-proved).
- **Falsifier:** invalidity of the cited lower-bound construction or correction of the recursive inequality.
- **Source:** https://arxiv.org/html/2411.09594v1

## Gaps
The exact complete graphic-by-graphic current ledger is still not established; 121 versus 125 conventions remain. No source downloaded this cycle resolves it. Existing `research/ROOT.md` already meets the initial library criterion (minimal obstruction, verification boundary, >=3 restricted classes).