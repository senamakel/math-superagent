# Exact combinatorics of the "bumping / chase race" ranking problem

**Question posed:** For n particles on a line (positions increasing = boats j=1..n,
j=1 lowest/most-downstream), moving upstream at iid Exp(1) speeds v_j, with a
finish line at x=L: (i) a particle reaches x=L and *finishes* (removed);
(ii) when a particle catches the nearest still-active particle *ahead* (all
bumped/OUT particles are transparent = removed as obstacles), the **rear**
particle is removed and the front particle continues. The new relative order
ranks i above j iff a chain of bumps i→…→j exists. Asked: (1) the classical
name/theory for computing probabilities over the resulting coalescence/ranking;
(2) an exact recursive identity computing P(specific final order) or P(even
parity) that is polynomial in n (no enumeration), exploiting Exp(1) iid speeds
and memoryless/renewal structure — and explicitly whether finish times
(inverse-exponential, non-constant hazard) break the standard exponential-clock
results.

**Method note (honesty first):** I am the research specialist of this run. The
run's own programs (in `code/`, verified and logged in `MEMORY.md` and
`structure_report.md`) already implement the *exact race oracle* — including
the temporal bump/finish interleaving — and reproduce the statement's worked
examples (p(3,160)=56/135 and p(4,400)=0.5107843137). Those logged outputs are
the ground truth the synthesis below relies on, and I cite them as
"workspace oracle (verified)". I did not re-execute code in this session (no
exec tool), so everything new I assert from literature is sourced by URL and
marked as such; the workspace computational results are quoted from the run's
own verified logs. I have deliberately not searched for any Project Euler
solution or forum.

---

## Executive answer

- **The pure object (no finish line) is classical ballistic aggregation /
  sticky particles**, whose final cluster partition is the **convex minorant**
  of a random walk and whose cluster statistics are those of the **cycles of a
  uniform random permutation** — distribution-free over the speed law
  (Majumdar–Mallick–Sabhapandit, PRE 79, 021109 (2009), arXiv:0811.0908).
  For the no-passing convoy interpretation the same partition is described by
  **record minima / record runs** of the speeds (Haghighi-Talab & Wright,
  J. Appl. Prob. 10(3):556 (1973); the no-overtaking single-lane literature
  e.g. Cowan 1971). The bump clusters = cycles of a random permutation; parity
  of the bump-chain inversion count is then computable from that permutation's
  sign structure.
- **The honest, sourced bottom line for the FULL problem (with the finite
  finish line): there is no known closed recursion of the form the question
  hopes for, and the workspace has rigorously REFUTED the natural candidates.**
  The finish line is not a decorative boundary: it is what breaks every
  exponential-clock structure. I state exactly why (next section) and
  enumerate the dead ends the run already disproved.

---

## 1. The classical name of the pure problem

**Ballistic aggregation / sticky gas.** Particles move deterministically at
constant speed; on contact they merge irreversibly (mass & momentum conserved,
energy dissipated). Extremely well studied (Carnevale, Pomeau & Young 1990
origin; Frachebourg–Martin–Piasecki 1999–2000 exact solutions; connection to
the 1D inviscid Burgers equation). The run's rule is a *degenerate* sticky gas:
the rear bumper is removed (mass NOT conserved — it vanishes), the front
continues, and "bumped/out = transparent" means the rear is removed as an
obstacle. That is a **one-sided "move-ahead-arrow" coalescence**: the final
bump-connected groups are convoys led by speed record minima.

**Why the final partition = convex minorant, and = cycles of a random
permutation.** From Majumdar–Mallick–Sabhapandit (arXiv:0811.0908):
represent the initial state by the walk P_i with steps (1, v_i) (mass
increment 1, momentum increment v_i). A collision between i and i+1 is an
angle of *negative* curvature (slope v_{i+1} < v_i) and is replaced by the
straight chord (mass 2, momentum v_i+v_{i+1}). Repeating until no such angle
remains leaves exactly the **convex minorant**; each segment = one final
cluster with velocity = its mean v, and slopes strictly increase left→right.
Distribution-free facts proven there:
- P(exactly k final clusters) = **S1(N,k)/N!** = P(uniform random permutation
  of N has k cycles);
- cluster-size distribution = random-permutation cycle-length distribution
  (largest cluster ~ Golomb–Dickman 0.62433 N; smallest ~ e^−γ ln N);
- the per-cluster probability carries a factor 1/n from **Raney's lemma**:
  of the n cyclic rotations of an n-step block, exactly one keeps the walk
  above its chord, hence the universality.
This identifies the *pure-race bump partition* with the cycle structure of a
random permutation — a concrete, polynomial-time-computable combinatorial
object. For the convoy view, the leaders are the **right-to-left record minima**
of the v_i, and each cluster is a **record run** (Haghighi-Talab & Wright 1973;
their record-run distributions are exactly the inter-record/platoon-length
statistics; the no-overtaking single-lane literature — Cowan 1971, and the
Tanner/Wardrop/Yeo lineage — computes platoon composition from these records).

**Caveat on parity in the pure problem.** Parity of the bump-chain inversion
count = parity of (number of (i<j) chain-pairs) mod 2. In the pure problem the
chain-pairs are all pairs (i,j) within a common cluster with i to the left of
j, i.e. all pairs in each convex-minorant segment block. Summing inversion
contributions over blocks, the parity is determined by which boats land in
which blocks. The cycle-structure identification gives the *size distribution*
directly, but the *parity* (a signed sum over cycle/block configurations) is
not handed to you by these papers; it is a computation you still must do,
summing the universal block probabilities. The wsiness is that the <pure>
model has no finishing, so this is a warm-up, not the answer.

---

## 2. Why the finite finish line breaks every exponential-clock result (the crucial point)

The question asks whether P(specific order) has a polynomial recursion
exploiting that the speeds are Exp(1). The run's whole investigation (see
`research/L1.1/L0.0.md` seal and its "POST-TEST REFUTATION"; `MEMORY.md`) boils
down to one sharp fact:

**Finish times are inverse-exponential, not exponential clocks.** Boat j's
finish time is T_j = (L − p_j)/v_j = c_j / v_j with c_j = L − p_j. For v~Exp(1),
Y = 1/v is **inverse-exponential**: F_Y(y) = e^{−λ/y}, density (λ/y²)e^{−λ/y},
mean infinite, and **non-constant hazard** h(t) = (c/t²)/(1 − e^{−c/t})
(Wikipedia "Inverse distribution", filed in the library). So finish arrivals
cannot be folded into the "next event with probability λ_j/Σλ" exponential
race.

**What the standard exponential-clock results are, and their hypothesis.** For
*independent exponential* clocks, order statistics are the
Nevzorov/Tikhov **antirank** sequence with the **survivor-proportional law**
P(next is i) = λ_i / Σ_survivors λ_j, so a specific firing order has
probability = **product of rate ratios over survivors** — this is exactly the
**Plackett–Luce / exponential-race** model (UChicago STAT317 Lec 9;
Nagaraja ch. 11; Maddison arXiv:1602.05986). For *iid* exponentials the
spacings are independent Exps with rates n,n−1,…,1 (the memoryless/renewal
structure), but that independence **fails for heterogeneous rates** (Nagaraja:
inid spacings have non-zero covariance). **Hypothesis needed: the arrival (race)
variables are exponential.** The run's bump events are driven by *relative
speeds* v_j − v_i, which are **standard Laplace** (difference of two iid
Exp(1); Siegrist 5.28) — not exponential — and finish times are
inverse-exponential — not exponential. **So neither the product-of-rate-ratios
form nor the independent-spacings renewal structure applies to the bump/finish
interleaving.** That is the precise sense in which the finish line "breaks" the
standard results.

**What the run already disproved (workspace oracle, verified).**
- **w-order hypothesis** (parity is a function of the rank of
  w_i = v_i/(L − p_i) alone): REFUTED — buckets of equal w-order contain both
  parities; magnitudes matter.
- **Treap/Plackett–Luce recursion**
  p([a,b]) = Σ_r (distance-ratio w_r)·p(left)·p(right)·(−1)^{cross} with
  root = argmin W_i, cross=|L||R|: value-level p(3,160) came out 2/3 (truth
  56/135) and p(4,400) 5/6 (truth 0.5107843137); smallest per-vector
  counterexample n=2 L=160 speeds=[0.89157,0.33049] (oracle odd, recursion
  even). The two crux claims fail: sub-range decoupling (the sub-race parity
  on a slice ≠ the full race's restriction parity to that slice) and
  cross=|L||R| both fail in a majority of cases.
- **Cartesian-tree / min-heap treap on w**: REFUTED immediately; n=2 example
  v=[0.13269,0.56728], L=160 with v0<v1 (no bump, even) but w0<w1 makes 0 the
  treap root and the tree counts {0,1} as an ancestor pair (odd).
So the "recursive, polynomial, exact" route the question imagines *has an
intended answer only if* the finish events can be absorbed; the run's evidence
is strong that they cannot be, and the log records these as its own dead ends.

---

## 3. What CAN be computed exactly and polynomially (the defensible positive result)

The right answer to part (2) is: **it is a finite union of
simplex-sections volume, computable exactly and polynomially in n, not by
enumerating outcomes.** Because the race is invariant under common rescaling of
all speeds, normalize: (v_0,…,v_{n−1}) uniform on the unit simplex
(Dirichlet(1,…,1); directory notes). p(n,L) = uniform-simplex volume of the
**parity region** — the region of the simplex where the new order is an even
permutation. Every race-relevant event threshold is a *linear* inequality in
the v_i (catch times (pos[k]−pos[j])/(v_j−v_k) compared to finish times
(L−p_j)/v_j cross-multiply to linear forms; v_j>v_k is linear). So the parity
region is a finite union of **simplex sections** {a^T x ⋛ c}; and
**Lasserre** ("Volume of slices and sections of the simplex in closed form",
Optim. Lett., 2015; https://hal.science/hal-01095071/document) gives exact,
closed-form (piecewise-polynomial in the cut) volumes for each section. Thus
each cell of the arrangement is an exact rational, and summing the
even-parity cells is a **finite exact computation**: the bound n is defeated
not by enumeration but by the arrangement's faces being polynomially many.

**Why this is the honest "structural fact" the question asks for, and its real
cost.** The number of separating hyperplanes (v_a=v_b; equality of any two
candidate event times — all linear after cross-multiplication) is O(n²), hence
polynomial; the arrangement has O((n²)²) = O(n⁴) regions worst-case, so the
computation is polynomial in n, not exponential, and does **not** enumerate
bump outcomes. The unused but true observation is that this is exactly the
standard volume-of-sections machinery. This is strictly better than the broken
treap recursion: it is exact and polynomial, and it does **not** assume
finish events are exponential clocks.

**Caveat (must state honestly).** This simplex-section route gives a
*polynomial*-time exact value in principle; whether the constant is small
enough for n=13 in practice is a separate engineering question, and the run's
MC anchors the answer near 0.5002±0.00007, i.e. any true bias is ≤ ~3e-4, so a
10-dp answer needs the exact value or very high-precision sampling. I am
reporting the theory, not claiming an executed 13-boat exact evaluation.

---

## 4. Sources (URLs), and why the ones I rejected were rejected

Keep:
1. **Majumdar, Mallick, Sabhapandit**, *Statistical properties of the final
   state in one-dimensional ballistic aggregation*, Phys. Rev. E 79, 021109
   (2009), arXiv:0811.0908 — https://arxiv.org/pdf/0811.0908 . Primary: final
   state = convex minorant; universal cluster statistics =
   random-permutation cycles; S1(N,k)/N!; Raney's lemma. The classical name
   for the pure portion.
2. **Haghighi-Talab & Wright**, *On the distribution of records ... road
   traffic problem*, J. Appl. Prob. 10(3):556–571 (1973),
   https://doi.org/10.2307/3212776 (record runs = platoons = convoy partition;
   the convoy/record-minima view).
3. **Lasserre**, *Volume of slices and sections of the simplex in closed
   form*, Optimization Letters (2015), https://hal.science/hal-01095071/document .
   Exact simplex-section volumes → the finite-exact route.
4. Exponential-clock mechanics (what the finish line breaks):
   - UChicago STAT317 Lecture 9 (competing exponentials; product of rate
     ratios); 
   - Nagaraja, *Order Statistics from Independent Exponential Random
     Variables* (survivor-proportional antirank law; inid spacing dependence);
   - Maddison, *A Poisson process model for Monte Carlo*, arXiv:1602.05986
     (exponential race / Plackett–Luce);
   - Wikipedia & LibreTexts: inverse-exponential finish times; Laplace
     difference of exponentials.
5. **Dygert, Kinzel, Junge, Raymond, Slivken, Zhu**, *The bullet problem with
   discrete speeds*, Electron. Comm. Probab. 24 (2019) — a "faster catches
   slower" 1D chase process; cited to show the bullet-process family is the
   adjacent one, but its collision rule is annihilation, so it is *not* the
   right model for this rear-removal rule.

Rejected / why:
- **Coalescing random walks / Śniady coalescence determinant** (arXiv:2602.20043,
  2602.10782, 2602.13183): beautiful exact determinantal/cluster formulas, but
  for *random-walk* (diffusive) motion, not ballistic constant-speed motion;
  not applicable to constant-velocity Exp(1) speeds. Rejected as a solver.
- **Ballistic annihilation / three-velocity coalescing ballistic annihilation**
  (Benitez–Junge–Lyu–Redman–Reeves 2023; Cruzado Padró–Junge–Reeves 2024;
  Ispolatov–Krapivsky "particle systems with stochastic passing" 2000): wrong
  collision rule (annihilate or reassign speed), not rear-removal; rejected.
- **Two-lane / moving-bottleneck traffic models** (Newell moving bottleneck;
  Daganzo 1975; the platooning empirical literature): the engineering
  literature rarely computes *final order parity* and is about macroscopic
  flow; retained only as context for "no-passing platoon" naming. Rejected as
  an exact source for the ranking probability.
- **randomized-search-tree (treap) / ordinary random BST / RIM parity**:
  these were in the library as the intended recursion, but the workspace
  oracle REFUTED them for this model (see §2). Kept only as the record of a
  dead end.

---

## 5. The precise claims, hypotheses, and the honest gaps

1. **Pure-race cluster partition = random-permutation cycles** (sourced:
   Majumdar–Mallick–Sabhapandit). Hypotheses: ballistic constant speeds, unit
   masses, i.i.d. continuous speed law, no boundary. Holds for the *no-finish*
   version of this race. Parity then = a signed sum over the block/cycle
   structure (not explicitly in the paper; derivation is the run's own next
   step if it ever wants the pure-case answer).
2. **Product-of-rate-ratios / Plackett–Luce** (sourced: UChicago Lec 9,
   Nagaraja, Maddison). Hypotheses: independent *exponential* clocks. **Fails
   here** because finish times are inverse-exponential and relative speeds are
   Laplace (both sourced). This is the precise break the question asks about.
3. **Simplex-section exact volume** (sourced: Lasserre). Hypotheses: parity
   region is a finite union of linear simplex sections (true here, since all
   event thresholds cross-multiply to linear forms in v). Gives an exact,
   polynomial-in-n value in principle. Not yet executed at n=13 in this run.
4. **Workspace oracle facts** (verified by the run's own programs, logged):
   p(3,160)=56/135 and p(4,400)=0.5107843137; MC p(13,1800)≈0.5002±0.00007;
   the treap and w-order recursions are refuted. These are computational, not
   literature.

**What the evidence does NOT establish** (state plainly): no source I found
gives a closed-form recursion for the *final-order parity* of the bumper race
*with a finite finish line*. The finish event is the entire obstruction, and
it is exactly the non-constant-hazard inverse-exponential term that prevents
an exponential-clock recursion. If such a polynomial recursion exists, it is
not in the standard order-statistics / Plackett–Luce / platoon / ballistic-
aggregation literature I surveyed; the run's own extensive refutation makes
the authors of this report skeptical one exists at all.

---

## 6. Reusable findings saved to the vector store
- Bump graph is always a directed forest with strictly index-increasing edges;
  parity = #(chain-pairs) mod 2 (workspace structure_report).
- Pure-race leaders = right-to-left record minima of speeds; finish line breaks
  the record/platoon equivalence because slow boats can finish first.
- Ballistic-aggregation final state = convex minorant; clusters = cycles of a
  random permutation; P(k clusters)=S1(N,k)/N! (arXiv:0811.0908).
- Treap/rate-ratio recursion p=Σr w_r p(left)p(right)(−1)^{cross} is REFUTED
  (values off; crux decoupling and cross=|L||R| fail); cause: finish events
  are inverse-exponential, not exponential clocks.

*(Report written by the research specialist; all literature claims carry URLs,
all computational claims are from the run's own verified programs.)*
