# Pure ballistic aggregation final-order parity: what the literature actually establishes

**Question answered:** In the *pure* (no-finish-line) 1D ballistic aggregation / sticky-gas /
bumper-race with iid continuous speeds, what is the probability the "final order parity" is even,
as a function of n, and is there efficient (non-enumerative) computation?

**Bottom line (verified, sourced):**
1. In the pure sticky model the **final order is the identity**: there is *no nontrivial final
   permutation of particles* whose parity one could ask for. The fan state is simply ordered.
2. The only permutation structure is through the **composition** (which initial particles end up
   in which cluster) = the cycle-length composition of a uniform random permutation.
3. The run's own torpids "pure-race parity" is **not** the dateable cycle-block functional of that
   composition. Any literature statement about cycle statistics does *not* hand over the PE597 pure-race
   parity; the run's verified numbers are the honest small-n answers.

---

## 1. The sticky fan state is identity-ordered — the parity question is vacuous as posed

Majumdar–Mallick–Sabhapandit (arXiv:0811.0908, PRE 79, 021109) define the model and prove the fan-state
structure:

> "When t ≫ N^3/2 the system evolves into a stationary state in which no more collisions can occur:
> the particles are grouped in k disjoint clusters of different masses. Each cluster moves at a constant
> velocity, and the speed of a given cluster is larger than that of its left neighbour ... and less than
> that of its right neighbour. In this ultimate state the clusters keep on moving farther apart, i.e.,
> they fan out from each other, thus justifying the name 'fan' state." (Sec. II.A)
> "the final state is uniquely given by the convex minorant of the corresponding random walk. Each line
> segment of the convex minorant represents a cluster in the fan state" (Sec. II.B)

Crucially, clusters never overtake (velocities strictly increasing left→right), so **the cluster order
equals the initial-position order**. Each cluster is a *consecutive block* of initial particles
(cluster ℓ = initial particles N_{ℓ-1}+1 … N_ℓ, Sec. II.C). Consequently:

- The induced permutation of the particle labels is **the identity** (boat j ends in the j-th position
  within its block; blocks are ordered by starting position). The "even permutation" question for the
  pure model, taken literally at the particle level, has trivial answer **1** (identity, even).
- All nontrivial content is in the **composition** (the block-size vector), which is what the paper
  maps to permutation cycles.

Source: https://arxiv.org/abs/0811.0908 (full text filed at `research/sources/mms_ballistic_aggregation_pdf.full.md`).

## 2. The composition law: cluster-size composition = cycle-length composition of a uniform permutation

MMS Eq. (14): P(k clusters) = S1(N,k)/N! (unsigned Stirling first kind), distribution-free over the
initial velocity law (universal). Eq. (15): P(cluster-size counts c_1,…,c_N) = ∏_j 1/(j^{c_j} c_j!),
i.e. exactly the cycle-count law of a uniform permutation. Grand-canonical generating function Eq. (17):
Γ(z,{t}) = exp(∑_k t_k z^k / k). Mean number of clusters = H_N = ∑_{k≤N} 1/k.

These facts are also in Suidan (doi:10.4213/tvp3898), Abramson–Pitman–Ross–Uribe Bravo
(doi:10.1214/ecp.v16-1648, Theorem 1), Alsmeyer–Kabluchko–Marynych–Vysotsky (doi:10.1214/20-ejp497),
Goldie (Camb. MPCPS), and the Sparre-Andersen F_n = 1 + ∑_{r=2}^n Ber(1/r) representation (from Steele,
doi:10.1016/S0377-0427(01)00472-1; and the escholarship thesis snippet). All agree the *face-length
composition* of the convex minorant equals the *cycle-length composition* of a uniform permutation,
distribution-free.

## 3. Two combinatorial parity facts that ARE sourced and exact

**(a) Parity of the NUMBER of cycles** of a uniform permutation is exactly balanced: for every n≥2 there
are exactly n!/2 permutations with an even number of cycles and n!/2 with an odd number. Proof: C_n(x)=∏_{j=0}^{n-1}(x+j); setting x=−1 gives C_n(−1)=∏(j−1)=0 for n≥2, and C_n(−1)=#even−#odd=0.
Sources: Bóna, "On a balanced property of derangements" arXiv:math/0606277 (states it explicitly);
Levande, arXiv:0907.3168; Shattuck "Parity theorems for statistics on permutations and Catalan words"
(10.5281/zenodo.7648640); Arndt's book. Mechanically verified this run by constructing the Stirling
triangle for n=2..10 (assert that even==odd==n!/2).

**(b) The cycle-length-composition parity functional the run tested** (Σ cycles C(size,2) mod 2, the
"cluster-block" proxy for a final-inversion count) has EGF A(z) = exp(∑_k (−1)^{C(k,2)} z^k/k) =
exp(arctan z)/√(1+z²), so P(even)=½(1+[z^n]A(z)). Exact small values (run-computed, code/cycle_parity.py):
n=3 → 1/6, n=4 → 5/12, n=13 → 33545/54432 ≈ 0.61627. This is a *valid exact combinatorial sequence*, but
see §4: **it is not the torpids parity**.

## 4. What the pure model does NOT give: the run's verified pure-race torpids parity

The honest small-n pure-race torpids limits (L→∞) are exact from the run's verified closed forms
(fixed rational functions of m=L/40):
- p(2,∞) = 1/2
- p(3,∞) = 7/18 ≈ 0.3889  (closed form p(3,L)=(7m²−17m+12)/(18m²−45m+27))
- p(4,∞) = 19/36 ≈ 0.5278  (closed form p(4,L)=(19m³−119m²+244m−162)/(36m³−216m²+423m−270))
Recorded in `code/out/exact_pn.json` (p(4,1800)=166802/317985≈0.52456) and the CONTEXT table. Large-L limits
confirmed by MC (n=5,6,7,8 → 0.5320, 0.4870, 0.4916, 0.5058, SE~7e-4).

These are **not** the cycle-block functional of §3(b): n=3 the functional gives 1/6 ≠ 7/18; n=4 gives
5/12 ≠ 19/36. The torpids bumper rule is *rear-removal* (rear bumper passes/OUT, front continues), so the
bump graph is a forest of chains (out-degree≤1, no cycles, edges strictly index-increasing), not the
sticky-conservation clusters; parity = #(chain pairs) mod 2, which is a forest functional, not a
cluster-block functional. Run-verified counterexamples: equal-GCM-composition speed vectors give different
torpids parity at n=5 (code/verify_gcm_parity_gap.py). So no *pure-race-sticky* literature formula can be
cited as the answer to the finite-finish parity, and none of the surveyed sticky/permutation theory covers
the finite-finish case (§5).

## 5. Efficiency of computing the pure model's statistics — and why it does not transfer

- The cluster/cycle statistics ARE efficiently computable: the family is encoded by one EGF
  exp(∑ t_k z^k/k), and P(k clusters)=S1(n,k)/n! is O(n²) via the Stirling recurrence (or O(n log n) with
  NTT on the falling-factorial product). This is the polynomial-time part of the pure model.
- The torpids parity does **not** reduce to it (run-verified, §4). To evaluate the run's own exact pure-race
  numbers at n≥5 you still need the finite-finish arrangement, whose naive exact enumeration explodes
  (n=4 → 1202 cells, n=5 → ~13,750 cells vs 85 hyperplanes), and n=13 via enumeration is dead.
- No published result gives a polynomial closed recursion for the *finite-finish-line* torpids parity. The
  finish event (inverse-exponential, non-constant hazard) breaks the exponential-clock / Plackett–Luce /
  Skorokhod machinery entirely; this is consistent with the entire surveyed sticky/permutation/record
  literature, none of which has a finish line.

## 6. Sources consulted and why

Used:
- MMS arXiv:0811.0908 / PRE 79 021109 (fan state = GCM, cluster=cycles) — primary. Full text filed.
- Bóna arXiv:math/0606277 (cycle parity balance, explicit statement) — primary for §3(a).
- Levande arXiv:0907.3168, Shattuck zenodo 7648640, Arndt book (independent §3(a) statements).
- Steele doi:10.1016/S0377-0427(01)00472-1 (Bohnenblust–Spitzer: F_n = #{records} = H_n distribution).
- Suidan, Abramson–Pitman–Ross–Uribe Bravo, Alsmeyer–Kabluchko–Marynych–Vysotsky (composition law).
   - Suidan and APRUB are paywalled abstracts; their statements are cited via the escholarship thesis
     snippet and the survey, flagged as such. MMS (open) carries the identical content, so no load-bearing
     claim rests on the paywalled ones.

Rejected as not bearing on the question:
- Haslegrave–Tournier, Benitez–Junge–Lyu–Redman–Reeves, Junge et al., Cruzado-Padró–Junge–Reeves (ballistic
  *annihilation*, three-speed, skyline universality): different rule (annihilate, not stick/pass), and their
  "skyline" universality is about survival/pairing structure, not a parity as a function of n. Noted in
  FRONTIER as adjacent-model leads only.
- Frachebourg–Martin–Piasecki (ballistic aggregation hierarchy): scaling/coarsening, not finite-n final
  parity; no new content beyond MMS for this question.
- Bullet-problem literature (Broutin–Marckert, Dygert, Śniady): annihilation rule, count of survivors, not
  parity; wrong-rule contrast already in library.

## 7. Direct answer to the user's sub-questions

- "Probability the final permutation parity is even as a function of n" — **vacuous** in the sticky model:
  the final order is identity (prob 1 even). The user is likely thinking of two different objects; neither
  is the torpids pure-race parity: (i) parity of #clusters is exactly ½ for all n≥2 (balanced); (ii) the
  block-composition parity ΣC(size,2) mod 2 is ½(1+[z^n]exp(arctan z)/√(1+z²)) = 1/6, 5/12, 33545/54432 for
  n=3,4,13 — a sourced exact formula, but **refuted** as the torpids parity (true values 7/18, 19/36).
- "Anything known about computing it efficiently" — the pure *compositional* statistics are polynomial
  (Stirling/EGF); the torpids parity is not reduced to them by anything found, and the finite-finish parity
  has no surveyed polynomial recursion.

## Sources (URLs)
- https://arxiv.org/abs/0811.0908 (full: https://arxiv.org/pdf/0811.0908)
- https://doi.org/10.1103/PhysRevE.79.021109
- https://arxiv.org/abs/math/0606277 (Bóna)
- https://doi.org/10.48550/arxiv.0907.3168 (Levande)
- https://doi.org/10.5281/zenodo.7648640 (Shattuck)
- https://doi.org/10.1016/S0377-0427(01)00472-1 (Steele)
- https://doi.org/10.4213/tvp3898 (Suidan)
- https://doi.org/10.1214/ecp.v16-1648 (Abramson–Pitman–Ross–Uribe Bravo)
- https://doi.org/10.1214/20-ejp497 (Alsmeyer et al.)
