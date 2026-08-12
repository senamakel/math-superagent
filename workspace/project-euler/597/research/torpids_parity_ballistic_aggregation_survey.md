# Parity and sign structure of 1D ballistic aggregation and the
# bumping-race final-order permutation (literature survey + run verification)

**Question:** Is there a closed form / determinantal-combinatorial formula for
the probability that the final relative order in a 1D "bumping" race is an
even permutation, and does an absorbing finish boundary break the classical
convex-minorant result?

**Answer in one paragraph.** For the *pure* (no-finish) version, the final
bump partition IS the greatest convex minorant (GCM) of a random walk, whose
statistics are the cycle statistics of a uniform random permutation
(Sparre Andersen's 1950s representation; Majumdar–Mallick–Sabhapandit;
Abramson–Pitman–Ross–Uribe Bravo). But the *parity of the torpids new order is not a
function of that GCM partition*: the torpids rule is a *rear-removal* variant
(rear bumper is out/transparent; front continues), so the bump graph is a
**forest of chains**, not a set of cluster-blocks, and two speed vectors with
the *same* convex-minorant composition can have different torpids parity
(verified by the run's oracle, see code). Hence the classical result — which
is about *cluster sizes and velocities* — does not hand over the parity of the
torpids permutation even in the pure limit. The **absorbing finish line** adds
a second break: it removes boats *by time* (L−p_j)/v_j, an inverse-exponential
(non-constant-hazard) clock, and the bumped/OUT boats as transparent removes
the key "no-passing" assumption that drives the record-minima/platoon
equivalence. The literature contains **no closed-form or determinantal formula
for the even-parity probability** of the finite-finish torpids order; the run's
own exact small-n oracle (p(3,160)=56/135, p(4,400)=521/1020) matches the
given values, MC pins p(13,1800)≈0.5002±0.00007, and every recursive/treap
reduction proposed in the run was refuted.

---

## 1. Classical background: pure ballistic aggregation = convex minorant

**Model.** N unit-mass point particles on a line at positions p_i, velocities
v_i, merging perfectly inelastically (mass and momentum conserved). This is
the sticky gas / ballistic aggregation, exactly solvable in 1D
(Carnevale–Pomeau–Young 1990; Frachebourg 1999; Frachebourg–Martin–Piasecki
2000).

**Theorem (convex-minorant characterization).** For particles at the lattice
sites 0,1,…,n−1 with iid continuous speeds, the final (no-further-collision)
"fan" state is in bijection with the **greatest convex minorant** of the walk
S_j = Σ_{i≤j} v_i: each straight face/segment of the GCM is one final cluster,
with horizontal length = cluster mass and slope = cluster velocity; slopes
increasing left to right.
- **Majumdar–Mallick–Sabhapandit**, *Statistical properties of the final state
  in one-dimensional ballistic aggregation*, Phys. Rev. E 79, 021109 (2009),
  arXiv:0811.0908. https://arxiv.org/pdf/0811.0908
- **Abramson, Pitman, Ross, Uribe Bravo**, *Convex minorants of random walks
  and Lévy processes*, ECP 16 (2011), https://doi.org/10.1214/ecp.v16-1648
  (Theorem 1: face lengths of the GCM of a walk with exchangeable increments,
  no subset-average ties, have the joint distribution of the ranked cycle
  lengths of a uniform random permutation of n elements).
- **Goldie**, *Records, permutations and greatest convex minorants*, Math.
  Proc. Camb. Phil. Soc. (2022), 
  https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/records-permutations-and-greatest-convex-minorants/DEE42D1FC4782ACA192BD360A1B1EE36
  (translates permutation results to record times and GCM; identifies the
  Bernoulli variables in the standard representation of the number of GCM
  sides).

**Theorem (universality + permutation-cycle identity).** For iid continuous
increments (any law), the *number* of clusters F_n has the distribution of the
number of cycles K_n of a uniform random permutation:
- F_n =^d K_n,  and  P(F_n = k) = S1(n,k)/n!   (unsigned Stirling numbers of
  the first kind, U(n,k)/n!).
- Sparre Andersen representation: F_n = 1 + Σ_{r=2}^{n} Ber(1/r)
  (independent Bernoulli indicators I_r with P(I_r=1)=1/r) — this is exactly
  the classical representation of the cycle count of a uniform random
  permutation (the "Bernoulli variables" Goldie identifies).
- The induced composition of n by face lengths is distributed as the
  composition by cycle lengths of a uniform random permutation.
- Sources (all primary):
  - **Suidan**, *Convex minorants of random walks and Brownian motion*,
    Theory Probab. Appl. 46 (2001), https://doi.org/10.4213/tvp3898
    (bijection between cycle-type distributions and GCM segment-length
    compositions; uses Shepp–Lloyd, Vershik–Shmidt).
  - **Abramson, Pitman, Ross, Uribe Bravo** (ECP 2011), Thms 1–2.
  - **Alsmeyer, Kabluchko, Marynych, Vysotsky**, *How long is the convex
    minorant of a one-dimensional random walk?*, EJP 25 (2020),
    https://doi.org/10.1214/20-ejp497 (uses Sparre Andersen's original
    1950s representation; §2.1 states the permutation representation).
  - **Kabluchko, Vysotsky, Zaporozhets**, *Convex hulls of random walks:
    expected number of faces and face probabilities*, Adv. Math. (2018),
    arXiv:1612.00249, https://doi.org/10.48550/arxiv.1612.00249
    (Stirling-number formulas for expected face counts; distribution-free).
  - **Bóna**, *On a balanced property of derangements*, Electron. J. Combin.
    13 (2006), https://doi.org/10.37236/1128 (§1 states c(n,k) = signless
    Stirling first kind, C_n(x) = x(x+1)…(x+n−1), and the classical fact
    P(even #cycles)=P(odd #cycles)=1/2 for uniform random permutations via
    C_n(−1)=0).

**What this gives (and does not give) for parity.**
- The number-of-clusters distribution F_n = K_n is *closed form* (Stirling).
- The **composition** (which boats share a cluster) is *not* a deterministic
  function of anything simple; it is a random composition of n distributed as
  permutation cycle lengths (joint via the Bernoulli/cycle representation or
  via Ewens-type formulas).
- The parity of "the convex-minorant cluster permutation" — if one defines a
  permutation by listing clusters (as cycles) — is an *additional statistic*
  NOT supplied by the GCM/cycle-length literature. The parity of the number of
  cycles already balances (1/2), and the sign of a permutation is not a
  function of its cycle-length composition (any composition of n into k cycles
  supports both parities for k ≥ 2).

**Independent verification (run's own).** `code/verify_cm_face_dist.py`
simulates the GCM of a random walk with iid continuous increments and checks
- P(F_n = k) = S1(n,k)/n! (against the Bernoulli-sum representation)
- composition frequencies agree with the uniform random-permutation
  cycle-composition counts, independent of the increment law (normal vs
  exponential), confirming distribution-freeness of the COMPOSITION (not of
  parity).

---

## 2. What breaks for the torpids/bumping race

### 2.1 The bump rule is NOT the sticky-particle rule
The torpids rule: on a bump, the **rear** (bumping) boat is removed
(OUT/transparent), the **front** boat continues and may be re-bumped. This is
a *one-sided rear-removal* rule, not mass-conserving coalescence. In bump
sports (the actual Oxford/Cambridge "bumps" regattas), the rear boat stops
and the front continues — the *rear* is out. The convex-minorant/sticky-gas
rule instead merges mass and keeps the combined cluster moving at the mean
velocity; the front particle's identity is not preserved.

Consequences (established by the run, `code/structure_taxonomy.py` +
`structure_report.md`, over 360k trials n=3,4,5):
- The bump graph is ALWAYS a **directed forest** whose edges point to strictly
  higher indices: out-degree ≤ 1 (each boat bumps at most once), in-degree
  unbounded (a boat can be re-bumped many times), no cycles, boat n−1 never
  bumps, boat 0 never a target.
- Parity of the new order = **#(chain pairs i→…→j, i<j) mod 2**, i.e. the
  inversion count of the final permutation (verified match with
  `parity_of_new_order`).
- Because components are forests of chains, the number of chain-pairs in a
  component is NOT Σ C(size,2): within a cluster (connected component of the
  bump graph) not every pair is chain-linked. The run's
  `no_finish_structure.py` documents mismatches between the torpids
  components and the convex-minorant segments, between within-component
  chain-completeness and C(|C|,2), and between roots and right-to-left record
  minima of speeds — all in the pure (no finish) limit. So the naive
  "cluster parity = Σ C(size,2)" formula is refuted by the run's exact engine.

### 2.2 Parity is not a function of the convex-minorant composition
`code/verify_gcm_parity_gap.py`: sampling pairs of speed vectors with the SAME
GCM composition, the torpids parities differ (run again at n=5, 30k trials,
pairs with equal GCM composition; a nonzero fraction have different parity).
Therefore no "closed form" for the parity can be a function only of the GCM
composition — a negative result directly relevant to the requested
"is the parity of the convex-minorant cluster permutation computable in closed
form".

### 2.3 The absorbing finish line breaks the classical result (named mechanism)
The classical convex-minorant/record/platoon results assume **no boundary**.
The PE 597 model has a finish line at position L: boat j finishes (is removed
by crossing L) at time T_j = (L − p_j)/v_j. What exactly breaks:
1. **Finish times are inverse-exponential, not exponential clocks.** v_j~Exp(1)
   ⇒ 1/v_j has the inverse-exponential law with density (c/t²)e^{−c/t} and
   NON-constant hazard (Wikipedia "Inverse distribution"; run's library note
   `research/L1.0/inverse_exponential_finish_times_wikipedia.md`). The whole
   Plackett–Luce / competing-exponential-clock / order-statistic-spacings
   machinery (rate-ratio products, memoryless renewal) has HYPOTHESIS
   "arrival times are exponential", which fails.
2. **Relative speeds are Laplace, not exponential.** v_j − v_i for iid Exp(1)
   is standard Laplace (Siegrist LibreTexts 5.28, in library). Bump times
   (pos_k−pos_j)/(v_j−v_k) are ratio-type events, not exponential clocks.
3. **Record-minima/platoon equivalence fails.** In the pure race, the convoy
   leaders are the right-to-left record minima of speeds, each cluster a
   record run (Haghighi-Talab & Wright 1973, DOI 10.2307/3212776). With a
   finish line, a SLOW boat far from the line may finish before a fast boat
   behind it catches it — "unbumps" (a boat can exit by finishing) break the
   monotone record structure entirely.
4. **The OUT/transparent removal** changes the geometry: boats behind can pass
   through a stopped boat, so the "no-passing" lane assumption underlying
   platoon theory and the convex-minorant face structure is not satisfied in
   the finite model either.

**Named hypotheses of the classical theorems (why they fail here).**
- MMS 2009 / Abramson–Pitman–Ross–Uribe Bravo: N particles, no boundary,
  ballistic, mass-conserving sticky collisions. Fails: rear-removal +
  finish-line absorption.
- Sparre Andersen / Alsmeyer et al.: random-walk GCM on a fixed interval,
  exchangeable increments, no subset-average ties (continuous). Holds for the
  *pure* torpids composition (same GCM statistics), but the torpids PARITY is
  not a GCM-functional anyway (verified), and the finish line is outside this
  framework.
- Haghighi-Talab & Wright: single-lane no-passing records; fails with
  transparent OUT boats and with boats exiting by finish.

---

## 3. Literature search results: what exists and what does not

Searches run (exa_search, several angles):
- "convex minorant random permutation cycles parity sign ballistic aggregation"
- "greatest convex minorant number of faces distribution unsigned Stirling
  numbers"
- "sign of random permutation even odd probability Stirling number cycles"
- "sticky particles ballistic aggregation absorbing boundary escape exit"
- "ballistic aggregation sticky gas evaporation removal convex minorant"
- "rowing bump race ranking permutation probability even odd"
- "one-dimensional particles overtaking rear removed transparent obstacle"
- record/platoon, Ewens, inversion-parity, Coxeter-group inversion counts.

**Found (kept):**
- **GCM = random-permutation cycles** (composition distribution): the named
  theorems above (MMS, Suidan, APRU, Alsmeyer et al., Kabluchko et al.,
  Goldie, Bóna). These give the *cluster statistics* in closed form
  (Stirling / Bernoulli-representation), including the exact distribution of
  the number of clusters and the composition law.
- **Convex minorant of Brownian motion / meander / bridge** (Pitman et al.):
  continuous analogues, same cycle structure (references inside APRU).
- **Sign/parity of random permutations** (Baxter–Zeilberger;
  Bóna; Kahle–Stump): the parity of a uniform random permutation is balanced
  (1/2) for n≥2, and inversion count is asymptotically normal (Mahonian).
  These are *input statistics* for any "parity functional" of a
  permutation-valued final order, but do not supply the probability for THIS
  race model.

**Not found (the honest gap):**
- No paper computes the probability that the final-order permutation of a
  *rear-removal, absorbing-boundary* 1D bump race is even. Searches for
  "towards" variants (ballistic aggregation + evaporation, sticky gas +
  absorbing boundary, overtaking with rear removal, record theory with exit)
  turn up the *sticky/aggregation* literature (which is mass-conserving) or
  *diffusive* absorption (Brownian escape problems, Aldous's "up the river"
  problem, Tang–Tsai) — none with the torpids rule.
- The convex-minorant theorem itself has NO statement about the *sign* of a
  permutation; it gives cluster sizes/velocities. The run's verification
  shows the torpids parity is not even a functional of the composition.

**Rejected (why):**
- Coalescing random walks / Śniady-type coalescent determinantal formulas:
  for diffusive (random-walk) motion, not ballistic constant speeds; wrong
  process.
- Ballistic annihilation / three-velocity coalescing ballistic annihilation:
  different collision rule (annihilate or reassign speed), not rear-removal.
- Two-lane / moving-bottleneck traffic models, platoon engineering,
  TASEP with defects: macroscopic flow vs. exact final-order permutation
  parity; not the right object.
- Brownian escape / sticky-boundary papers (Bressloff; Scher–Reuveni–
  Grebenkov): absorption of *diffusive* particles via boundary local time,
  not a *deterministic* ballistic race with a fixed finish line.
- The one PE solution sketch surfaced (cirosantilli GitHub:
  `solvers/597.md`) — **not used** (explicitly out of scope: no Project Euler
  solutions/forums). Noted only to confirm we did not search for it.

---

## 4. What the run's own numbers establish (basis: run's verified engines)

| object | value / verdict | basis |
|---|---|---|
| p(3,160) | 56/135 = 0.4148148… (given example) | exact rational cell sum + MC + second engine |
| p(4,400) | 521/1020 = 0.5107843137… (given) | exact + MC + second engine |
| p(2,L) | L/(2L−40) closed form | analytic + cell + MC |
| p(3,L) | (7m²−17m+12)/(18m²−45m+27), m=L/40 | established, verified over 28 L |
| parity cells | n=3→32 (17 even), n=4→1202 (595 even), L-independent | exact enumeration |
| bump graph | always a directed forest, edges index-increasing, outdeg≤1 | proved consequences + 360k trials |
| parity identity | parity = #(chain pairs) mod 2 | verified every pattern |
| GCM vs torpids | components ≠ GCM segments; parity not a GCM functional | run verification |
| p(13,1800) | ≈0.5002 ± 0.00007 (10M–60M MC) — NOT a 10-dp answer | MC only (exact route open) |

All computational claims are from the run's own verified programs
(`code/brute.py`, `code/cell_exact.py`, `code/arrangement_pn.py`,
`code/structure_taxonomy.py`, plus the two new verification scripts in
`code/`), all cross-checked against the two given example values.

---

## 5. Precise answer to the two concrete questions

**Q1: Is the parity of the convex-minorant cluster permutation computable in
closed form?**
- The *composition* (which elements lie in which GCM clusters) has a closed
  form: it is the cycle-composition of a uniform random permutation
  (S1(n,k)/n!, Bernoulli-representation F_n = 1 + Σ Ber(1/r), Ewens-type
  joint laws). That is exact and polynomial-time computable.
- The *sign/parity of the final-order permutation* of the torpids race is NOT
  a function of that composition (run-verified: same composition, different
  torpids parity). No literature formula gives it. For the pure sticky-gas
  case, if one defines the permutation by the *clusters as blocks sorted by
  velocity*, the parity functional is a derived statistic not present in the
  GCM papers; the run's data shows the torpids parity is not even that
  cluster-block parity.
- The classical parity-balance result P(even) = P(odd) = 1/2 (uniform random
  permutation, n≥2) is a red herring for this model: the race order is not a
  uniform random permutation.

**Q2: What changes when a boat can exit by finishing (absorbing boundary)?**
- The pure result (GCM cluster partition = random-permutation cycles) is a
  *partition/order statistic* statement holding for a boundary-free sticky
  gas. With an absorbing finish line:
  - boats are removed by *time*, with inverse-exponential (non-constant
    hazard) clocks — the Plackett–Luce / exponential-spacing machinery breaks
    (hypothesis failure, named above);
  - the removal changes the bump graph (transparent boats allow passing), so
    even the *pure* no-finish torpids parity ≠ GCM-cluster parity;
  - the record-minima/platoon equivalence for convoys fails (a slow boat can
    finish before being caught).
- Bottom line: the convex-minorant result for the *cluster statistics* is NOT
  broken in the pure limit (verified: composition distribution matches), but
  (i) it never gave the parity, and (ii) with a finish line the whole
  chronology changes (finish events are not exponential clocks), which the
  run refuted for every recursive/treap/rank reduction tried.

---

## 6. Claims for the library ledger

```claim
id: cm-composition-distribution
statement: For a random walk S_j = sum_{i<=j} X_i with iid continuous increments, the greatest convex minorant on [0,n] has F_n faces with P(F_n = k) = S1(n,k)/n! (unsigned Stirling first kind), equivalently F_n = 1 + sum_{r=2}^n Ber(1/r) in distribution; the face-length composition of n equals in distribution the cycle-length composition of a uniform random permutation of [n], distribution-free over the increment law.
hypotheses: iid (or exchangeable) increments; no subset-average ties (continuous law); boundary-free walk on a fixed interval.
holds-here: Yes for the PURE (no-finish) torpids race composition; NOT handed over to the finite-finish model, and NOT to the torpids parity functional.
status: sourced (MMS 2009; Suidan 2001; Abramson–Pitman–Ross–Uribe Bravo 2011; Alsmeyer–Kabluchko–Marynych–Vysotsky 2020; Kabluchko–Vysotsky–Zaporozhets 2018; Goldie 2022) + run-verified by simulation (code/verify_cm_face_dist.py).
bearing: gives exact cluster-composition statistics for the pure model; the requested PARITY is a further statistic not supplied.
anchor: https://arxiv.org/pdf/0811.0908 ; https://doi.org/10.1214/ecp.v16-1648 ; https://doi.org/10.1214/20-ejp497
```

```claim
id: torpids-parity-not-gcm-functional
statement: The torpids final-order parity (parity = #(chain pairs) mod 2) is not a function of the convex-minorant composition of the speed vector: there exist speed vectors with equal GCM composition but different torpids parity (pure race), verified by the run's exact engine at n=5.
hypotheses: torpids rear-removal bump rule; iid continuous speeds.
holds-here: Yes (this is the run's own model; the claim says the naive 'cluster parity from GCM' is false).
status: run-verified (code/verify_gcm_parity_gap.py; structure_report.md). Not claimed in the literature (no source found), which is itself the gap finding.
bearing: kills the route 'parity = function of convex minorant / cluster composition' for the full problem.
anchor: workspace code/verify_gcm_parity_gap.py
```

```claim
id: finish-line-breaks-exponential-clock-machinery
statement: In the finite-finish torpids race, finish times (L-p_j)/v_j with v_j~Exp(1) are inverse-exponential with non-constant hazard; relative speeds v_j-v_i are Laplace. Hence the Plackett–Luce / competing-exponential / order-statistic-spacings machinery (which requires exponential arrivals) does not apply to the bump/finish chronology.
hypotheses: v_j iid Exp(1); finish at fixed position L.
holds-here: Yes.
status: sourced (Wikipedia Inverse distribution; Siegrist LibreTexts 5.28; UChicago STAT317 Lec 9; Nagaraja INID chapter) + run-refutation of all recursive/treap reductions (MEMORY.md).
bearing: explains why no exponential-clock recursion for the finite model exists in the surveyed literature.
anchor: https://en.wikipedia.org/wiki/Inverse_distribution ; research/L1.0/inverse_exponential_finish_times_wikipedia.md ; research/L1.0/laplace_difference_of_exponentials_libretexts.md
```

```claim
id: torpids-bump-graph-forest
statement: The torpids bump graph is always a directed forest with edges to strictly higher indices (out-degree ≤ 1, no cycles); parity of the new order equals the number of chain-pairs mod 2; within a connected component not every pair is chain-linked.
hypotheses: torpids rear-removal rule, any L including ∞; speeds continuous.
holds-here: Yes (this run's model).
status: verified over 360k trials + proved consequences (structure_report.md); second engine + MC agreement on all exact values.
bearing: structural reason single-root tree/treap models fail; parity is a forest functional, not a cluster-block functional.
anchor: workspace structure_report.md ; code/structure_taxonomy.py
```

---

## 7. Gaps (what a further search could still establish)

1. **Sign of a 'cluster permutation' defined by GCM blocks.** I found no paper
   computing the parity/sign distribution of the permutation obtained by
   ordering GCM clusters (by velocity or by position). This is a well-posed
   combinatorial object (random permutation conditioned on cycle-length
   composition, then a derived sign functional) — the parity is
   P = Σ_comp (composition prob)·(1±s(comp))/2 and is computable from the
   composition law, but I have not seen it in the literature and this run has
   not computed it.
2. **Any exact identity for the finite-finish torpids parity.** Still open;
   the run's MC (≈0.5002±0.00007 at n=13, L=1800) is consistent with a small
   bias or with exactly 1/2 — the 10-dp target needs the exact value, and the
   library's exact route (simplex-section volumes via Lasserre) is the only
   proven-last-step if a recursive reduction is found.
3. **"Ballistic aggregation with evaporation / absorbing boundary"** exists in
   the physics literature only for *diffusive* or *annihilating* variants, not
   for rear-removal bumps with a fixed finish line. A search for this exact
   combination ((sticky gas || ballistic aggregation) + (evaporation ||
   absorbing boundary || sink)) returned nothing matching; the field seems not
   to have studied the parity functional of the final-order permutation in
   this model.

*Write-up: research specialist of this run. Literature claims carry URLs;
computational claims are from the run's own verified engines. No Project Euler
solution or forum was used or searched for.*