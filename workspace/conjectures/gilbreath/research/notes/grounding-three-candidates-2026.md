# Grounding three candidate approaches (2026): coarea, affine-Weyl/crystal, ReLU synthesis

For the inventor's three proposed approaches. Each assessed: what the reformulation
is actually called, the precise statement of any theorem it relies on and whether
its hypotheses hold here, whether anyone has applied it to this problem, and what
it would buy.

---

## 1. coarea-layer-cake-level-decomposition

**What it is called.** The identity is the discrete form of the **layer-cake
(Cavalieri) representation** / the **coarea formula's one-dimensional level-set
version**: for nonnegative integers a,b,

    |a − b| = Σ_{t≥1} ( [a≥t] XOR [b≥t] ).

This is exactly the layer-cake identity ∫ f = ∫ μ({f>t}) dt written for the
function |a−b| over a counting measure; it recovers a,b's magnitude as the count
of levels where the two threshold indicators differ. The analysis literature
establishes it fully (e.g. Tzanavaris, "An Elementary Proof of the Layer Cake
Representation Theorem", Amer. Math. Monthly, 2025, doi:10.1080/00029890.2025.2583888;
Federer's coarea formula, Malý–Swanson–Ziemer, Trans. AMS 2002).

**The theorem's hypotheses and whether they hold here.** The layer-cake identity
itself is an identity — it holds for every integer row, no hypothesis needed. It
is exact, not an approximation. So the *identity* is grounded.

**What it would buy — the decisive point.** Nothing new, and the approach's own
proposed target is the already-refuted potential class. Three linked facts:

1. The natural aggregate of the transform is exactly the refuted quantity.
   Σ_t #{i : B^t_k(i) ≠ B^t_k(i+1)} (the per-level boundary count, summed over
   levels) = Σ_i |A_k(i) − A_k(i+1)| = TV(row k) = the sum of the entries of
   row k+1. The coarea decomposition's total "level-boundary mass" collapses to
   the total variation of the parent row. And the run has **machine-refuted**
   the total-variation/run-count potential class: `r(T(x)) ≤ r(x)` fails
   everywhere, including inside on the {0,2} regime at the halved string
   (0,0,1,1) → (0,1,0) (2 runs → 3), the minimal counterexample over all
   6,725,600 strings of length ≤ 8 (approach `total-variation-oscillation-potential`,
   refuted; claim refutation in `code/out/check_runcount_lemma.captured.txt`).

2. Per-level monotonicity fails for the same reason it failed for TV. Inside the
   {0,2} block the per-level bits evolve by XOR / Rule 90 (proved,
   `rule90-interior-xor`), whose bit-level run count *grows* (Sierpinski) — so a
   per-layer boundary-count invariant does not exist inside the very regime the
   conjecture targets. This is the identical obstruction that killed
   `level-set-percolation` (one threshold, needs monotone predicate — fails) and
   `persistent-homology` (superlevel death values — fails on saddle bookkeeping).

3. The statement "A_k(1) ∈ {0,2} ⟺ the two parent entries agree at all but at
   most two levels" is a **faithful restatement of the definition** A_k(1) =
   |A_k−1(1) − A_k−1(2)|, not a reduction. Two entries differ by ≤ 2 is exactly
   what the conjecture asserts; the coarea coordinates do not make the membership
   question easier.

The transform is exact and is bookkeeping. No source applies the layer-cake /
coarea decomposition to the iterated absolute-difference / Ducci / Gilbreath
problem (searched); the layer-cake literature is about integrals and measure, and
yields no discrete invariant of this operator.

**Verdict.** Refuted. The identity is grounded (layer-cake theorem) but the
proposed program — a per-layer monotone invariant — is the same class as the
machine-refuted total-variation/run-count potential, and the transform's aggregate
collapses exactly onto that refuted quantity, while per-level structure is
Rule-90-governed (run-count grows). The conjecture's second-entry claim is
faithfully but unhelpfully restated. `killed-by`: `total-variation-oscillation-potential`
(machine-refuted), `rule90-interior-xor` (per-level runs grow), the TV-equals-
level-boundary-mass identity.

---

## 2. affine-weyl-alcove-walk-crystal

**What it is called.** W̃(A₁) is the affine Weyl group of type A₁, the infinite
dihedral group ⟨s_0, s_1⟩ with s_0: x→−x and s_1: x→2−x (affine reflection about
1). The map x ↦ |x−2| is s_1 on [0,2] and a translation by −2 for x ≥ 2 — exactly
an affine extension of the simple reflections. **Alcove walks, Hecke algebras,
spherical functions and crystals** are the named framework (Ram, Pure Appl. Math.
Q. 2(4):963–1013 (2006); Parkinson–Ram, J. Comb. Theory 2008; and the J-folded
alcove walk / MV-intersection literature). The block interior evidencing Pascal
mod 2 = **Lucas theorem = sl₂ branching coefficients** is also real.

**The theorem and its hypotheses here.** The descent lemma x_s = |x_{s−1} − c_s|,
c_s ∈ {0,2}, is genuinely an alcove walk in W̃(A₁): the fold against 2 is the
affine reflection s_1, and c_s = 0 is a no-op. The run has **already proved the
exact endpoint statement** — `lemma54-descent-lean-formalised` (kernel-checked in
Lean, zero sorryAx): into the fundamental alcove {0,2} iff v ≤ 2ν₂+2, where ν₂ =
#{c_s = 2} is the number of 2-steps = number of wall-hits.

**What it would buy — the decisive point.** The candidate sets its own falsifier:
"Step (b)'s statistic match is the decisive probe; if ν₂ has no named
alcove-walk/crystal counterpart, the bijection is bookkeeping." That probe fires
decisively:

- In **rank 1**, the alcove-walk algebra collapses: the only substatistics an alcove
  walk carries are the weights of the chambers visited and the number of wall hits
  per reflection type. There is one reflection type that matters here (s_1, the
  fold against 2, applied ν₂ times), so the walk's only nontrivial statistic is
  ν₂ itself combined with the starting value v — literally the already-proved
  biconditional. Ram's alcove-walk statistics that carry real content (Hall-
  Littlewood/weight-space data, spherical function support) are higher-rank / higher-
  weight objects; A₁ has a single simple root and none of that structure. There is
  no rank-1 alcove-walk theorem that bounds the *rate* at which 2-steps arrive.
- The *rate at which c_s = 2 steps arrive* (when a regeneration's edge pattern drives
  the intruder down) is precisely the open regeneration / G-supply question — the
  same content that refuted `vectorial-subtractive-euclidean` (return-rate question
  = open regeneration rate in new variables). Alcove-walk and crystal theory
  contribute no handle on it.
- The crystal half (block interior = Pascal mod 2 = sl₂ branching) describes the
  static Sierpinski interior; it does not couple to the *drain* of the intruder in
  any source. No paper applies alcove walks, affine crystals, or Hecke combinatorics
  to the iterated absolute-difference / Ducci / Gilbreath problem (searched several
  angles; the Ducci literature is periodicity/cyclotomic — e.g. Breuer 2010,
  Lewis–Tefft 2024 — and never representation-theoretic).

So the dictionary (steps a–b of the proposal) is exactly true — a 1-D affine
reflection — and reproduces a *proved* lemma in representation-theoretic costume;
the open direction is untouched, and by the candidate's own criterion the successful
dictionary is bookkeeping. This is the same re-description pattern as
`vectorial-subtractive-euclidean` (refuted): exact dictionary, no new bound, open
rate restated.

**Verdict.** Refuted — by the candidate's own falsifier. The affine-Weyl reading of
the descent lemma is exact (and consistent with the proved `lemma54-descent-lean-formalised`),
but in rank 1 the alcove-walk statistics reduce to ν₂ and v, no named alcove-walk /
crystal statistic bounds the drain or regeneration rate, and no source applies the
framework to this problem. `killed-by`: rank-1 collapse of alcove-walk statistics to
ν₂ = wall-hits (no new content beyond the proved biconditional `lemma54-descent-lean-formalised`);
the rate side is the open G-supply/regeneration question in new variables
(`vectorial-subtractive-euclidean`).

---

## 3. relu-network-inductive-invariant-synthesis

**What it is called.** The one-step halved map H(h)_i = |h_i − h_{i+1}| =
(h_i−h_{i+1})₊ + (h_{i+1}−h_i)₊ is a fixed **piecewise-affine (PWA) / ReLU** map;
depth-k entries are a fixed ReLU circuit on the initial halved gaps. The proposed
move — search for a **forward-invariant (inductive) set** by template synthesis, or
certify safety by **complete ReLU/PWA reachability** — is a real, mature, named
program:

- **Inductive invariant synthesis / barrier functions for PWA and ReLU systems**:
  Samanipour–Poonawala, "Invariant Set Estimation for Piecewise Affine Dynamical
  Systems Using Piecewise Affine Barrier Function" (arXiv:2402.04243) and "Replacing
  K-infinity … Leaky ReLU … Union of Invariant Sets" (arXiv:2502.03765); Dai–Landry–
  Pavone–Tedrake (CDC 2020), "Counter-example guided synthesis of neural network
  Lyapunov functions for piecewise linear systems"; Teichrib–Darup (arXiv:2411.03834),
  polyhedral positively-invariant sets for PWA with NN controllers.
- **Complete ReLU reachability / verification**: Reluplex lineage, Marabou, star-set /
  abstract-interpretation domains (Bak–Tran–Hobbs–Johnson 2020 = arXiv:2001.07103;
  Yang–Johnson–Tran et al. 2021, facet-vertex incidence; Isac–Zohar–Barrett–Katz,
  CONCUR 2023 — verifiability of ReLU reachability is NP-complete and the reachability
  of a ReLU net with QF-LIA spec reduces to a reachability instance).

**The theorem and its hypotheses here.** The encoding is exact (|u−v| = (u−v)₊ +
(v−u)₊ is an identity), so the one-step map is precisely a ReLU layer and depth fits
this machinery with no hypothesis violated. The forward-invariant-set search and the
bounded complete reachability check are both legitimate on this object. Two honest
caveats the machinery itself imposes, neither fatal:

1. **Bounded-set caution.** The reachable set contains unbounded tail gaps, so any
   true invariant set must be unbounded in the tail directions (only the h_1 ≤ 1
   direction is bounded by safety). The linear-template S = {h : Σ c_i h_i ≤ d,
   h_i ≥ 0} can still be unbounded (zero or negative c on tail indices) and exclude
   h_1 ≥ 2 — the synthesis search must allow that, not assume a bounded set.
2. **Exact reachability is NP-complete** (Isac et al. 2023). For a bounded-depth
   complete check that means the solver's reachable depth K will be modest — a
   recorded bound, not a proof. That is fine and honest; the deliverable is the
   template-invariant SAT/UNSAT verdict or the bounded K with verdict.

**Has anyone applied it to this problem?** No — the ReLU-verification literature
targets ACAS Xu / control / perception benchmarks, never the Ducci/Gilbreath
difference operator (searched). This is unresolved-point a method-transfer. That is
acceptable for a grounded method: unlike coarea and affine-Weyl, this is not a
re-description — it genuinely converts "hand-hunt a scalar potential (all died on
XOR non-monotonicity)" into "let a solver search a template family and record a
warranted SAT/UNSAT verdict." Both outcomes are deliverables in the run's own terms:
a template invariant forcing A_k(1) ∈ {0,2} would be a GOAL.md invariant; UNSAT over
a stated template family would be a recorded negative bound on the whole polyhedral
invariant class (itself a result — it says no single linear/polyhedral template can
prove the conjecture).

**Verdict.** Grounded (as a method-transfer). The named machinery is real, mature,
and exactly fits the piecewise-linear shape of the operator; the encoding is exact
with no hypothesis violated. No one has applied it to this problem, so it carries
no precedent on the conjecture itself — but it is not a re-description and its
scoped verdict is a genuine deliverable. `precedent`: the PWA/ReLU invariant-synthesis
and complete-reachability papers above; run claims `gilbreath-reduces-to-second-in-02`
(the exact target the invariant must force), `fwd-diff-identity-refuted` (a reminder
that the linear part alone cannot certify the value). First step (encoder + oracle
check, then linear-template synthesis with SMT) remains for the tool_builder; the
bounded-set caveat above must be built into the template.

---

## Bottom line

- **coarea-layer-cake** — refuted: faithful restatement; aggregate = refuted TV; no
  per-layer invariant exists (Rule-90 run growth). Dead end.
- **affine-weyl-alcove-walk-crystal** — refuted by its own falsifier: rank-1 alcove
  statistics collapse to the already-proved ν₂; no application exists; open rate
  restated. Dead end / bookkeeping.
- **relu-network-inductive-invariant-synthesis** — grounded as a method. Real PWA/ReLU
  invariant-synthesis and complete-reachability machinery fits the operator exactly.
  Deliverable: a warranted template SAT/UNSAT verdict or a bounded-depth K with outcome.
  This is the one of the three worth an execution budget.
