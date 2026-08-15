# Grounding the three new inventor approaches

Question for each candidate: what is the reformulation called, what theorem does
it rely on and do its hypotheses hold here, has anyone applied it to this
problem, and what would it buy. Two candidates carried falsifiable structural
claims; both are settled by pure reasoning (no computation needed), which is
stronger than a citation.

Status context: the run has already CLOSED the gap via the spectral route
(f(n) = Theta(sqrt n), Huang chain independently re-derived). So "grounding" of
these three is against the closed theorem, not against an open target: none can
be a NEW lower bound; the useful question is whether the machine is real and
whether it could independently re-prove sqrt n or locate a precise obstruction.

---

## 1. `kruskal-katona-degree-ceiling-shadow` — REFUTED

**What it is.** Inverting the problem: define g_d(n) = max{|S| : D(S) <= d}, then
f(n) > d <=> g_d(n) < 2^{n-1}+1, and attack g_d via the Kruskal-Katona shadow
theorem plus coordinate compression (shifting) on the cube. Makes the degree
ceiling a per-vertex face bound.

**Theorem relied on.** Kruskal-Katona: for a family U of m k-sets,
|lower shadow| >= C(a_k,k-1)+C(a_{k-1},k-2)+... from the k-binomial decomposition
of m; equality attained by initial segments / vertex-decomposable complexes.
This is real and is already in the library (`kruskal-katona-shadow-formula`,
`induced-subgraphs-hypercube-full-vertices-kk`), where it counts HIGH-degree
(full) vertices of Q_k[S].

**Do the hypotheses hold and does the mechanism work? No — two independent
failures.**

(1) The load-bearing compression move is false. The file asserts an extremal S
for g_d(n) can be taken down-closed in the product order (coordinate shifting
does not increase D(S)). But the d=0 extremal sets are the two parity classes
(verified in this run: max independent sets of Q_n are exactly the parity
classes). At n=2, g_0(2)=2, achieved by {00,11}; but no down-closed order ideal
of size 2 with D=0 exists — the only size-2 order ideals are {00,01} and
{00,10}, both with D(S)=1. So compressing to down-closed sets destroys the
degree ceiling on the very d=0 line the proposal claims to reproduce. The
compression invariance of D(S) is not a theorem.

(2) Even granting compression, the natural KK shadow output is the d-skeleton
volume sum_{i<=d} C(n,i), which reaches 2^{n-1} only when d ~ n/2 — i.e. it
bounds g_d on the WRONG scale (linear in n) and inverting it could never certify
f(n) >= sqrt n. The route caps far above the truth; not sharp.

**Applied to this problem?** The large-induced-bounded-degree-subgraph literature
(Alon-Krivelevich-Sudakov nearly-regular; D'Elia-Frati planar/outerplanar) bounds
guaranteed large bounded-degree induced subgraphs in OTHER graph classes, not Q_n
at |S|=2^{n-1}+1. None touches the max-internal-degree quantity g_d(n).

**What it would buy.** Only a wrong-order-of-magnitude upper bound on g_d, and an
instrument that locates where KK stops — which the exact oracle already
computes. Orthogonal to the closed sqrt bound.

**Verdict: refuted** — killed by the false down-closure claim and the wrong
(linear) scale of the KK volume bound.

---

## 2. `independence-complex-topology-kahn-saks-sturtevant` — REFUTED

**What it is.** Reading D(S) topologically: the link of v in the independence
complex I(Q_n[S]) is claimed to sit on deg_S(v) vertices, so D(S) is the
largest possible link size; bound it from below via Meshulam's domination
theorem and Kahn-Saks-Sturtevant Z_2-index / box-complex.

**Theorem relied on.** Meshulam (2003): domination numbers of a graph control
vanishing of reduced homology of its independence complex. Lovasz (1978) /
Babson-Kozlov (Annals 165) / Matousek-Ziegler: the Z_2-index of the box complex
lower-bounds the CHROMATIC number. Both are genuine and well-attested.

**Do the hypotheses hold and does the mechanism work? No — the load-bearing
incidence is FALSE and INVERTED.**

The link of v in I(Q_n[S]) sits on the NON-neighbors of v. A face containing v
is {v} ∪ sigma with sigma an independent set of the graph induced on
S \ (N(v) ∪ {v}); so the link's vertex set is the non-neighbors of v, of size
|S| − 1 − deg_S(v), NOT deg_S(v). Worked check, n=2, S={00,11} (parity, both
deg=0): link(00) sits on 1 vertex (= the non-neighbour 11 = |S|−1−0), while
deg_S(00)=0. So a LARGE internal degree corresponds to a SMALL link, exactly
inverting the proposed direction. The deg information is carried by the
COMPLEMENT of the link's vertex set, not by the link itself — so
Meshulam-connectivity of I(Q_n[S]) forces nothing about the large links.

Independent second failure: the named topological invariants bound the chromatic
number, and chi(Q_n[S]) = 2 for every S (the cube is bipartite), so the
KSS/box-complex bound is vacuous (2 >= 2). No force.

**Applied to this problem?** No published source applies independence-complex
homology to a max-internal-degree quantity. The topology regime (link incidence
through vertex DELETION / complement, not link size) points away from a sqrt
bound.

**What it would buy.** Nothing for the lower bound; at best a precisely-stated
"topology cannot see sqrt n" obstruction.

**Verdict: refuted** — killed by the inverted link incidence (the complement of
N(v)∪{v}, not N(v)) and the vacuousness of the chromatic/box-complex route on a
bipartite host.

---

## 3. `sos-lasserre-certificate-exact-value` — GROUNDED (as certificate /
instrument machinery)

**What it is.** Treat the decision "exists S, |S|=2^{n-1}+1, D(S) <= d" as a
binary quadratic feasibility problem and attack it with the sum-of-squares /
Lasserre hierarchy; block-diagonalise the SDP over the 2^n characters of Z_2^n
(Cayley structure of Q_n); the dual is a proof certificate for f(n) >= ceil(sqrt n).

**Theorem relied on.** SoS/Lasserre hierarchy with Putinar/Schmuegen
Positivstellensatze on the hypercube; symmetry reduction of SDPs. All standard.
In this context: the degree ceiling is genuinely a per-vertex max (not an
average) — so it does NOT hit the averaging obstruction that killed Delsarte and
entropy. The x_v^2 = x_v Boolean ideal and the character block-diagonalisation
are both real and directly applicable. Scholze's rule holds: the level-2
certificate is exactly Huang's spectral chain (quadratic form λ_max <= D(S) plus
interlacing λ_max >= sqrt n), so the route reproduces huang-f-n-sqrt-n as a
degree-2 SoS proof.

**What the literature adds.** (a) Symmetric-quadratic hypercube functions get
degree O(sqrt(n k) log n) certificates (Kurpisz-Potechin-Wirth, ICALP 2021) —
showing the character symmetry the proposal names is genuinely powerful;
(b) effective Positivstellensatz degree bounds on the cube are known (Schmuegen
O(1/sqrt(eta)): Optimization Letters 2022; Putinar O(fmax/fmin): Baldi-Slot) —
so low levels can be large and the "does not close" failure mode is a studied,
real phenomenon (Lauria-Nordstroem CCC 2015); (c) the framework is sound.

**Applied to this problem?** No published source applies the Lasserre hierarchy
to certify the exact max-internal-degree value f(n); the specific dual-at-fixed-
level-for-all-n certificate is the proposal's own target. So nothing in the
literature answers whether the hierarchy closes at fixed level — that is a
computation, not a citation.

**What it would buy.** If levels above 2 certify ceil(sqrt n) at low fixed level,
a machine-checkable certificate (dual polynomials, Lean-checkable) for the exact
value — a proof artifact, genuinely new content over the one-line spectral
bound. If it does not close, a precisely-located "hierarchy does not close before
level t" obstruction, which is also a genuine result. Either way it is the most
honest of the three candidates and the only one with real forward value.

**Verdict: grounded** as instrument/certificate machinery, not as a new lower
bound (the lower bound is already Huang's; the hierarchy would re-derive it at
level 2 and possibly certify the exact value above that). No hypothesis
violated; no falsifier found in the literature beyond the honest "may not close"
possibility.

---

## Summary

| Candidate | Verdict | Deadly flaw or grounding |
|---|---|---|
| kruskal-katona-degree-ceiling-shadow | refuted | down-closure of extremal S false (parity not order ideal, n=2 check); KK volume is O(C(n,d)), d~n/2, wrong scale, can't certify sqrt |
| independence-complex-topology-kss | refuted | link of v sits on NON-neighbors = |S|-1-deg_S(v), inverted; box-complex/Z2-index bounds chi, vacuous on bipartite cube |
| sos-lasserre-certificate-exact-value | grounded | framework real; level-2 = Huang's proof (Scholze holds); symmetry reduction powerful; new content is a certificate computation, not a citation |

Both refutations rest on structural facts verifiable by hand (parity-class
d=0 extremals from the library's own exhaustive f-exact values; the link
incidence at n=2), not on any computation this session needed to run. No source
reporting this problem's answer was used; the screens withheld them, and none was
needed.
