# Grounding three inventor approaches: literature + exact-value refutation

Question: for each of the three candidate lines in `research/approaches/`, what
is the reformulation called, what theorem does it rely on and do its hypotheses
hold here, has anyone applied it to this problem, what would it buy — and does
the literature support it?

Method: searched each technique's own primary sources (allowed) while the
evidence policy correctly withheld any source reporting this problem's answer.
Then the two candidates carrying CHECKABLE structural claims were settled
against the run's own verified exact values / matrices, which is stronger than
a citation.

---

## 1. Delsarte / Krawtchouk LP (`delsarte-krawtchouk-lp.md`) — REFUTED

**What it is.** Delsarte's linear programming bound in the binary Hamming
association scheme H(n,2): the Bowes–Mesner algebra spanned by distance
matrices, Krawtchouk (= MacWilliams) transform, inner distribution a_i of S.
Source of the technique: Delsarte (1973).

**Does the theorem's hypothesis hold?** The LP's only structural constraint is
the MacWilliams nonnegativity `K·a >= 0` (a >= 0 is the spectral/moment
constraint of the scheme, i.e. of the *distance-symmetric* adjacency). The
signed matrix A_n that actually carries the sqrt(n) eigenvalue — Huang's signing
— has entries whose sign depends on the differing coordinate and the prefix
parity, NOT on Hamming distance, so `A_n ∉ Span(D_0..D_n)`. **The sqrt(n)
eigenvalue is invisible to the Krawtchouk/MacWilliams constraint.** This is the
exact point where the covers-clause (Scholze's rule: must reproduce
`huang-f-n-sqrt-n` in the coding-theory frame) fails.

**Second, independent failure.** The surviving value `min a_1` is the *average*
internal degree (a_1 = 2e(S)/|S|). Averaging-type methods are stated in
problem.md (and confirmed by every average-type source in the library) to cap
at Theta(log n) for a max-internal-degree quantity. So even a tight dual at the
parity codes yields only a log bound.

**Applied to this problem?** No source applies the Delsarte LP to the
max-internal-degree quantity D(S)=f(n); the entire published literature bounds
codes/min-distance (A(n,d)) or independence number — both distance-average
quantities. The closest genuinely useful result: uniqueness of the Delsarte LP
optimum when d ≤ 2 (the parity regime here) — the parity codes ARE the
Delsarte-optimal objects at distance 2, confirming where the +1 excess sits but
not bounding D(S).

**What it would buy.** Only a machine-checked certificate of WHERE the
average-degree LP stops, which is a located-obstruction instrument, not a
lower-bound proof. Orthogonal to closing the gap.

**Verdict: refuted** (Scholze's rule fails — signed matrix not in the scheme;
and averaging obstruction). Sources:
- https://link.springer.com/article/10.1007/s10623-023-01191-y (Unique optima of Delsarte LP, 2023)
- https://dl.acm.org/doi/10.1109/TIT.2024.3476974 (New solutions to Delsarte's dual LPs)
- https://www.sciencedirect.com/science/article/pii/S0024379506004630 (Delsarte LP as ratio bound / Lovasz theta)

---

## 2. Entropy / hard-core with degree ceiling (`entropy-degree-constrained-hardcore.md`) — REFUTED as a route to sqrt(n); GROUNDED for the d=0 line only

**What it is.** Kahn's entropy method / Shearer's lemma for independent sets in
regular bipartite graphs, and Galvin's hard-core threshold on the cube.
Real, deep, well-attested technique.

**Theorem relied on.** Kahn (2001): for an n-regular bipartite graph on N
vertices, i(G) ≤ (2^n+1)^{N/(2n)} (entropy via Shearer). Hyp: n-regular
bipartite. The hypercube Q_n satisfies this (N=2^n). But this bounds the
NUMBER of independent sets, not the degree ceiling at |S|=2^{n-1}+1. The
independence number α=2^{n-1} is trivially attained by the parity classes and
does not need entropy.

**The genuinely new proposal** — a degree-ceiling large-deviation entropy bound
whose inversion at |S|=2^{n-1}+1 forces max degree sqrt(n) — has NO published
support, and is average-type: entropy bounds a total, so it faces the averaging
obstruction. Concrete red flag at n=5: the exact extremal set has a *flat*
profile (12/17 vertices at the max degree 3; average = 44/17 = 2.59). Any
average/entropy upper bound on |S| as a function of ceiling d is dominated by
this spread and caps at log growth — it cannot force the flat max to sqrt(n).

**Applied to this problem?** Entire hard-core-on-cube literature (Kahn, Galvin,
Jenssen–Perkins–Potukuchi, Sah et al.) bounds counts and typical/average
structure, never the max internal degree D(S).

**Verdict: refuted as a sqrt(n) route; grounded only as the d=0 /
independence-number line** (satisfies Scholze's rule for that sub-claim, which
the file already reproduces). Sources:
- Kahn 2001: https://doi.org/10.1090/s0002-9939-01-06058-0 and CPC 10:219-237
- Sah et al. 2019: https://www.sciencedirect.com/science/article/pii/S0095895619300085
- Galvin: https://doi.org/10.1017/s0963548310000155
- Jenssen–Perkins–Potukuchi: https://doi.org/10.1017/s0963548321000559
- https://www.mdpi.com/1099-4300/23/3/270

---

## 3. Clifford / Dirac / fermionic (`clifford-dirac-fermionic.md`) — reformulation GROUNDED and correct; overshoot conjecture REFUTED at n=4

**What it is.** Reading Huang's signed adjacency as the Dirac operator
A_n = Σ γ_i in the n-generator Clifford algebra (Majorana/Fock space). The
identification A_n = Σγ_i with γ_i²=I, γ_i γ_j = −γ_j γ_i is self-verified to
equal the Huang matrix (this run's own hand derivation; n=2 checked in the
file, and A_n²=nI is exactly the Clifford relation A²=Σγ_i² = nI). This is a
correct and native-algebra restatement of the spectral route: the sqrt(n)
norm is genuinely native to the Clifford/Dirac world (norm of the Dirac
operator). Scholze's rule holds here for reproducing `huang-signed-adjacency`
and `huang-interlacing-sqrt` (Courant–Fischer subsumes interlacing).

**But the overshoot — "extremal sets = parity class + one excitation, forcing
f(n)=ceil(sqrt(n))" — is REFUTED at n=4, settled against the exact values.**
In Q_4, a parity-plus-one set (8 even + 1 odd x) has x adjacent to all four of
its neighbours (flipping a bit flips parity), so the lone excitation has
internal degree **4**. Hence D(parity+one)=4 at n=4, while f(4)=2 (exhaustive),
attained by a 4-even/5-odd witness with D=2. The fermion-number classification
of the minimisers is therefore false — the minimisers are NOT parity-plus-one.
The value conjecture f(n)=ceil(sqrt(n)) itself survives (matches f(1..5)=
1,2,2,2,3) but the stated mechanism for it is killed at n=4.

**Applied to this problem?** No source applies the Clifford/Dirac reading to
this max-internal-degree problem; it is a repackaging of the closed spectral
route (same sqrt(n) proof, no new lower bound). Sources develop the technique:
- https://link.springer.com/article/10.1007/JHEP02(2022)104 (lattice fermions as spectral graphs)
- https://link.springer.com/article/10.1007/s00006-010-0206-z (Clifford algebra applied to Grover)
- https://doi.org/10.1007/JHEP11(2020)154 (Majorana fermions on the hypercube)

**Verdict: reformulation grounded and correct (no independent lower bound); the
only falsifiable new claim refuted at n=4.**

---

## Summary

| Candidate | Verdict | Reason |
|---|---|---|
| Delsarte/Krawtchouk LP | refuted | signed matrix not in Bose–Mesner algebra (Scholze rule fails); min a_1 is average-type |
| Entropy/hard-core degree ceiling | refuted (as sqrt(n) route); grounded (d=0 line) | entropy is average-type; flat n=5 profile |
| Clifford/Dirac/fermionic | reformulation grounded; overshoot refuted | identification correct, but minimisers not parity+one at n=4 |

All three were settled by the technique's own literature and, where possible,
against the run's verified exact values/matrices — no source reporting this
problem's answer was needed or used.
