# Grounding report: the three `proposed` SUPPLY candidates

Date: this run. Author: research role.

## What this report is

The caller asked me to take each proposed line of attack to the literature and
report per candidate: what the reformulation is actually called, the precise
statement of any theorem it relies on and whether its hypotheses hold here,
whether anyone has applied it to this problem, and what it would buy — then
either `grounded` it or `refuted` it with a `killed-by`.

I found the three candidates with `status: proposed` and `precedent` blank in
`research/APPROACHES.md`:

1. `hoffman-frankl-wilson-image-support`
2. `hypergraph-containers-sparse-image`
3. `rubinstein-sarnak-prime-race-ergodic`

The three candidates circulating before (furstenberg-measure-rigidity,
gowers-u2-nilsequence-uniformity, matomaki-radziwill-index-autocorrelation)
are already `refuted` with full killed-by reasons on disk, and I independently
re-confirmed those refutations from the primary literature (below, "Notes on
the three historical candidates"). They are not re-opened here.

## Verdicts

All three `proposed` candidates are **refuted** — each relies on real, correctly
stated machinery, but the specific application to the fold does not work, and
in two cases the machinery does not even reach the object.

---

## 1. `hoffman-frankl-wilson-image-support` — **refuted**

### What the reformulation is actually called

The route frames `S(n) = Σ_d (−1)^{a_d}` (the excess; `S(n) = (n−2) − 2·wt(Φ_n h)`,
by the checked claim `excess-is-negative-character-sum`) as a statement about
the *disjointness/orthogonality graph* of the fold's row supports `R_d =
{n−1−d+o : o ⊆ d}`, with edges where `d ∧ e = 0`. The two named engines are
**Hoffman's eigenvalue bound** for the independence number of a regular graph,
and the **Frankl–Wilson theorem** on families with restricted pairwise
intersections. Both are real, standard, exactly-statable results.

### Precise statements

**Hoffman bound** (for an n-vertex d-regular graph G with minimum adjacency
eigenvalue λmin):
`α(G) ≤ n·(−λmin)/(d − λmin)`.
(Confirmed: the hypercube/Boolean-lattice orthogonality graph is regular and
its spectrum is given by Krawtchouk polynomials, so the bound is computable in
principle.)

**Frankl–Wilson (1981)** (Ellis survey Theorem 2.7): let `p` be prime,
`k ≤ n`, and `λ_1,…,λ_s ∈ {0} ∪ {1,…,p−1}` with `λ_i ≡ k (mod p)` for all i.
If `F ⊆ [n]^(k)` and for any two distinct `S,T ∈ F` there is `i` with
`|S∩T| ≡ λ_i (mod p)`, then `|F| ≤ n^s`.

### Whether the hypotheses hold here

The stated hypothesis structure — the load-bearing Gram identity
`|R_d ∩ R_e| = 2^{popcount(d∧e)}`, which would make the fold Gram matrix exactly
the disjointness matrix `J[d,e] = [d∧e=0]` — is **unverified** (the proposal
itself flags it as "machine-checkable but not yet checked"). That is a real
open step, but it is not the decisive defect.

### Why it is refuted — the decisive defect

**The independence number of the disjointness graph is LARGE, so "a small image
support D contradicts the independence number" fires in the wrong direction.**
An independent set in the disjointness graph is a family of row indices `d`
with `d ∧ e ≠ 0` for all distinct pairs — a *pairwise intersecting* family of
subsets of the digit set. The maximum size of such a family is `2^{n−1}`
(whole-set families, e.g. all subsets containing a fixed element), which is
comparable to the total number of rows. So the upper bound on an independent
set is on the order of the whole vertex set, and a "small" image support `D`
(with `|D| = wt(Φ_n h)`, which SUPPLY wants to be `≥ c·n`, i.e. large) is in
no contradiction with the independence number — the bound says independent sets
can be as large as half the cube. Frankl–Wilson's `n^s` bound governs a
*different* regime (uniform `k`-subsets of an `n`-set with restricted
intersection *sizes*), and the rows here are not uniform-weight subsets; the
theorem's hypotheses (prime `k`, `λ_i ≡ k mod p`) do not transpose onto the
row-index disjointness graph in the way the mechanism needs.

Additionally, the falsifier already fired for the naive form: **Thue–Morse is
balanced on both parity classes** (kernel coordinates `≈ n/4` each) yet has
sublinear `ν₂`, so any mechanism using only the two kernel bits is dead. The
proposal's own "live only via the distribution of the image column" hedge is
exactly the step that the literature does not supply.

### Precedent found

- Ellis, *Intersection Problems in Extremal Combinatorics*, arXiv:2107.06371 —
  Frankl–Wilson Theorem 2.7 and the whole restricted-intersection theory.
- Frankl–Rödl, *Forbidden intersections*, Trans. AMS 1987, DOI
  10.1090/s0002-9947-1987-0871675-6.
- Albertson et al., *Distinguishing orthogonality graphs*, J. Graph Theory, DOI
  10.1002/jgt.22704 — orthogonality graph of the cube, spectrum by Krawtchouk.
- Jenssen–Malekshahian–Park, *On Dedekind's problem, a sparse version of
  Sperner's theorem, and antichains of a given size*, DOI 10.1112/jlms.70624 —
  independence/antichain structure of the Boolean lattice.
- In-workspace: `excess-is-negative-character-sum` (checked),
  `fold-rank-n-minus-2-binomial-proved` (proved), the Thue–Morse negative
  control measurements.

**Verdict: refuted.** The engines are real; the direction of application to the
disjointness graph is wrong (a large, not small, independent number), and the
Frankl–Wilson hypotheses do not transpose. Would buy nothing further.

---

## 2. `hypergraph-containers-sparse-image` — **refuted**

### What the reformulation is actually called

**The hypergraph container method** (Saxton–Thomason and Balogh–Morris–Samotij):
for an `s`-uniform hypergraph `H` whose edges are "evenly distributed"
(supersaturation / co-degree conditions), the family of independent sets of `H`
is covered by a small collection of "containers", each a structured superset
with few edges inside. The route wants to bound the "bad set"
`B(ε) = {h ∈ F₂^n : wt(Φ_n h) ≤ εn}` by containers, then show the prime string
avoids all containers by an arithmetic input.

### Precise statement

**Container theorem** (BMS 2015 / ST 2015; Balogh–Morris–Samotij survey, ICM
2018): for an `s`-uniform hypergraph `H` with average degree `d` and
co-degrees controlled, there is a family `C` of subsets of `V(H)` such that
(i) every independent set is contained in some `C ∈ C`; (ii) each `C` induces
few edges; (iii) `|C|` is exponentially small. The strength depends on
quantitative supersaturation and co-degree bounds.

### Whether the hypotheses hold here — **they fail at the most basic level**

**`B(ε)` is not a family of independent sets of any hypergraph on the cube,
so the container theorem does not apply.** The container method governs the
*independent sets* of a hypergraph (sets containing no edge). Here `B(ε)` is the
preimage of a *Hamming ball* under the surjective linear map `Φ_n` of rank
`n−2`: `|B(ε)| = 4·Σ_{k≤εn} C(n−2,k)`. The set of strings whose image has small
weight is not characterized as "containing no edge of a fixed hypergraph"; it
is a low-density-set condition, which is a different object. The route's own
proposed hypergraph (one edge per row `d` = the affine hyperplane `a_d = 1`) is
a family of *edges*; `B(ε)` is the set of vertices incident to few edges of one
sign — the *complement* of an independent-style condition, not the independent
sets.

### Why it is refuted — the container characterization is false

Even granting the container framing, the proposed container shape — "h is
ε-close to a dyadic-alternating (kernel-like) string" — is **false as a
description of `B(ε)`**. The negative control **Thue–Morse** has sublinear
`ν₂(n)`, so `h = Thue–Morse ∈ B(ε)` for small ε, yet Thue–Morse is *not close
to the kernel* (kernel is the two alternating strings; Thue–Morse differs from
both on half the coordinates). Therefore Thue–Morse must lie inside every
container family that covers `B(ε)`, and any container characterization that
excludes it is wrong. This is not a gap; it is a false structural claim about
the very set the container method was to cover. It also re-opens the closed
family: "the primes avoid being close to an alternating string" is a weak
non-complexity input that cannot separate primes from Thue–Morse (which is also
far from alternating yet collapses).

### Precedent found

- Balogh, Morris, Samotij, *Independent sets in hypergraphs*, J. Amer. Math.
  Soc. 28 (2015) 669–709, DOI 10.1090/S0894-0347-2014-00816-X.
- Saxton, Thomason, *Hypergraph containers*, Invent. Math. (2015),
  arXiv:1204.6506 (the general theorem).
- Balogh–Morris–Samotij, *The method of hypergraph containers*, ICM 2018
  survey / arXiv 2015.
- Mousset–Nenadov–Steger, *On the number of graphs without large cliques*,
  DOI 10.1137/130947878 — the standard container application template (K_ℓ-free
  graphs).
- Campos–Samotij, *Towards an optimal hypergraph container lemma*, Combinatorica
  2026, DOI 10.1007/s00493-026-00214-1 — recent strengthening.

**Verdict: refuted.** Real, powerful, correctly stated machinery; but it governs
independent sets of a hypergraph, and `B(ε)` is not such an object, and the
proposed container shape is falsified by Thue–Morse. Would buy nothing and
re-opens a closed door.

---

## 3. `rubinstein-sarnak-prime-race-ergodic` — **refuted**

### What the reformulation is actually called

**Chebyshev's bias / the prime number race**, in the Rubinstein–Sarnak framework:
the distribution, under logarithmic density, of the normalized bias
`δ(x) = (π(x;4,3) − π(x;4,1))/√x` (or the density `δ(q;a,b)` of
`x : π(x;q,a) > π(x;q,b)`). The route wants to make the fold statistic `S(n)/n`
a functional of this one-point race and transfer the limiting measure through
the fold.

### Precise statement (Rubinstein–Sarnak, Expt. Math. 1994; conditional)

**Under GRH and a linear-independence hypothesis (LI)** on the non-negative
imaginary parts of the nontrivial zeros of the Dirichlet L-functions, the
normalized error `E(x) = (π(x;4,3) − π(x;4,1))·φ(4)/√x` has a limiting
distribution as `x → ∞` under *logarithmic* density; for mod 4 the logarithmic
density of `{x : π(x;4,3) > π(x;4,1)}` is approximately **0.9959**. This is
strictly conditional on GRH and LI, and it is a **one-point** statement (a race
between two residue classes), established only under logarithmic density.

### Whether the hypotheses hold here — they fail

(1) **It is conditional.** The route would hand SUPPLY a proof resting on GRH +
LI, which are not available for this problem and which the problem explicitly
wants to avoid. Every settled statement about the mod-4 bias (Rubinstein–Sarnak,
Fiorilli–Martin refinements, Harper–Lamzouri for many contestants) assumes GRH
and LI.

(2) **The g=0 stratum of `S(n)` is the adjacent-pair product**
`χ(r_j)χ(r_{j+1})` (the mod-4 switch-pair), which is *pair* data. By the run
telescope (claim `g-run-telescope-verified`, checked), each row `d` reads the
residue string at index pairs `(a_R, b_R)` with `b_R − a_R = 2^{ν₂(d+1)}`; at
`g=0` the reads are at ADJACENT indices. A one-point race distribution
(π counts per residue class) does not determine the joint distribution of
adjacent residues — that is exactly the parity barrier the workspace has named
(ABGS §9, `abgs-p1-wide-open`: positive mod-4 switch density "cannot be
treated using L-functions"). A one-point input cannot force the g=0 term to
vanish; no source computes a *filtered/digital functional* of the race from the
one-point measure alone.

(3) **Lemke Oliver–Soundararajan's consecutive-prime (mod q) pattern
distribution is conjectural** (Hardy–Littlewood/k-tuple based; the asymptotics
for the pattern frequencies are conjectural, not unconditional). So even the
two-point side of the literature (which is exactly what the g=0 term needs) is
open and conditional; it is not a resource this route can invoke.

### Precedent found

- Rubinstein, Sarnak, *Chebyshev's bias*, Experiment. Math. 3 (1994) 173–197,
  DOI 10.1080/10586458.1994.10504289 — the definition and GRH+LI limiting
  distribution.
- Fiorilli, Martin, *Inequities in the Shanks–Rényi prime number race*,
  Crelle 2012, DOI 10.1515/crelle.2012.004 — asymptotic series for the
  logarithmic densities (still GRH+LI).
- Harper, Lamzouri, *Orderings of weakly correlated random variables, and prime
  number races with many contestants*, Probab. Theory Relat. Fields 2017,
  DOI 10.1007/s00440-017-0800-2 — races from one-point data under GRH+LI.
- Granville, Martin, *Prime number races*, Amer. Math. Monthly (2006), DOI
  10.1080/00029890.2006.11920275 — survey; states GRH+LI conditional.
- Lemke Oliver, Soundararajan, *Unexpected biases in the distribution of
  consecutive primes*, PNAS 2016, DOI 10.1073/pnas.1605366113 — consecutive-
  prime (mod q) patterns, conjectural.
- In-workspace: `g-run-telescope-verified` (checked),
  `abgs-p1-wide-open` / `lau-nonconstant-pattern-open` (the mod-4 pair barrier).

**Verdict: refuted.** Real, precisely-stated machinery; but it is conditional on
GRH+LI, one-point, and logarithmic-density, and the fold's g=0 term is an
unconditionally-open two-point object that no one-point race distribution
determines. This is the parity barrier again, not a way past it.

---

## Notes on the three historical candidates (already refuted; re-confirmed)

I independently re-verified from the primary literature that the refutations
already on disk are correct:

- **Furstenberg measure rigidity** (`furstenberg-measure-rigidity-disjointness`):
  the rigidity theorems (Rudolph, Johnson; Furstenberg's ×2×3 conjecture) all
  require **two multiplicatively independent maps** (×2 and ×3, log p/log q
  irrational). Confirmed by Rudolph DOI 10.1017/s0143385700005681, Lindenstrauss
  survey DOI 10.4171/009-1/16, and the arXiv:2110.05989 survey: *"For p,q > 1
  multiplicatively independent... any atomless invariant, ergodic measure must
  be Lebesgue."* A single ×2 map has no rigidity (Bernoulli structure). Also the
  proved `fair-model-exact-binomial` shows the ×2-invariant (Haar) measure is
  the paradigm NON-collapse input. Refutation stands.

- **Gowers U² / Green–Tao nilsequence** (`gowers-u2-nilsequence-uniformity`):
  Green–Tao (Ann. of Math. 175, 2012; arXiv:0807.1736) prove Möbius is strongly
  orthogonal to *nilsequences* evaluated in the Walsh/Fourier basis at INTEGER
  values n. The fold reads the F₂ Möbius/zeta (ANF) transform at PRIME INDEX j —
  a different basis (zeta vs Walsh) and a different index. The GTZ U^s+1 inverse
  theorem (Ann. of Math. 176, 2012) is a Walsh-basis statement. Basis mismatch
  confirmed. Refutation stands.

- **Matomäki–Radziwill** (`matomaki-radziwill-index-autocorrelation`): MRT
  (Ann. of Math. 183, 2016, DOI 10.4007/annals.2016.183.3.6) controls sums over
  short VALUE-intervals `[x,x+H]` of a multiplicative `f(n)`. The object here,
  `s_j = χ(q_j)`, is not multiplicative in the prime INDEX j, and the g=0
  stratum is the open mod-4 switch-pair correlation. Value-domain tool for an
  index-domain object. Confirmed. Refutation stands. (The log-averaged Chowla of
  Tao, arXiv:1508.00540, is a value-domain two-point statement that breaks the
  parity barrier only for the *value-shifted* λ(n)λ(n+h), not the index-shifted
  prime object here.)

## What a genuine route would look like

The consistently lethal obstruction across every candidate is the **g=0 (adjacent
index/adjacent residue) stratum** — the mod-4 switch-pair correlation, which is a
two-point object that no one-point or structural input forces and that ABGS §9 (and
the workspace's named claims) identify as the parity barrier. The adopted live
routes (`fold-second-moment-krawtchouk`, `lucas-mixing-finite-transfer`,
`downset-row-code-distance-closed-form`) work around this by bounding the
*second moment / row-code distance distribution without* pointwise pair control.
That is the family that actually survives the literature; the three candidates
here die on pair=g=0 or on a non-transposing hypothesis.
