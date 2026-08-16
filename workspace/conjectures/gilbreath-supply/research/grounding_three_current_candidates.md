# Grounding report: the three current SUPPLY candidates (read-cone, mixing, Maynard-pattern)

Date: this run. Author: research role (grounding pass).

Task: take each candidate to the literature and report per candidate: what the
reformulation is actually called, the precise statement of any theorem it relies
on and whether its hypotheses hold *here*, whether anyone has applied it to this
problem, and what it would buy — then set `grounded` or `refuted` (with
`killed-by`). Refute on evidence, not absence: say plainly when a search simply
found nothing.

(These are the three candidates in the current prompt — `read-cone-column-
equivalence`, `mixing-implies-linear-fold`, `maynard-pattern-densification` —
not the three in the older grounding reports, which covered hoffman/frankl-wilson,
hypergraph-containers, rubinstein-sarnak and then level-set/haar-chaos/cramer.)

## Verdicts

- `read-cone-column-equivalence` — **grounded**, with a named open crux. The
  machinery is real, named, and its first half (the column bound) is provable
  bookkeeping; the decisive dyadic claim is genuinely novel — no source found
  proves or refutes it, and a finite check can settle which way it goes.
- `mixing-implies-linear-fold` — **grounded**, with the hypothesis as the gate.
  The transfer machinery (ψ-mixing + the already-adopted Parseval identity) is
  real and satisfies the Scholze gate; the *input hypothesis* (the prime
  switch-string ε is ψ-mixing with summable coefficients) is unproved, and the
  inventor's own falsifier (c) — the LOS non-summable decay — is the live risk.
- `maynard-pattern-densification` — **refuted**. The arithmetic engines from
  which the non-constant input was to come either fail their hypotheses at the
  fold's modulus or supply the wrong (equal-residue) direction; the densification
  step has nothing to densify.

---

## 1. `read-cone-column-equivalence` — grounded

### What the reformulation is actually called

The route recasts `G-sup-implies-switch` (the open converse: zero switch density
forces `liminf ν₂(n)/n = 0`) as the claim that a **fixed sparse support** `S` can
only make `ν₂ ≳ n` through **dyadic-aligned** coordinates. The two named legs:

1. **The column/influence bound** — `ν₂(n) = wt(Φ_n h) ≤ Σ_j h[j]·|C_j(n)|`
   where `C_j(n)` is the **read-cone** of coordinate `j`: the set of depths `d`
   that read `j`, i.e. `{ d ∈ [2,n−1] : (d−(n−1−j)) ⊆ d }`. This is an instance
   of the standard *total-influence* inequality in Boolean-function analysis
   (`wt(f) ≤ Inf_total(f)`, here for `f` = indicator that column `n`'s fold is
   odd), and the cone is the **Sierpinski / Pascal-mod-2 read structure**.
2. **The dyadic crux** — for a fixed density-0 `S`,
   `W_S(n) = Σ_{j∈S, j≤n−1} 2^{−popcount(n−1−j)}`, and the theorem needed is
   `inf_n W_S(n) = 0` for every density-0 `S`.

### Theorems it relies on, and whether hypotheses hold here

- **Influence inequality** `wt(f) ≤ total influence(f)`: real, standard, holds
  trivially (an odd cell needs ≥ 1 incident `1`, so weight ≤ incidence count).
  This half is bookkeeping and is machine-checkable against the oracle
  (`code/research_grounding/read_cone_check.py`, step 1, handed to tool_builder).
- **Sierpinski read-cone geometry**: the Pascal-mod-2 structure of the fold is
  documented (Callan arXiv:math/0610932, Thm 1 & 2: the inverse of the Pascal
  mod-2 matrix is Thue–Morse-valued; digital down-set / binomial-index structure;
  see the on-disk `supply-fold-submask-zeta-involution` and
  `g-run-telescope-verified` claims). Holds here.
- **The crux** `inf_n W_S(n) = 0` for every density-0 `S`: **no theorem found in
  either direction.** This is a "popcount-weighted Furstenberg / normal-number"
  statement — the weight `2^{−popcount(n−1−j)}` is large only where
  `popcount(n−1−j)` is small, which happens along sparse subsequences of `n`.
  The search returned nothing directly on this weighted sum. It is a *genuinely
  novel* combinatorial question, not a named theorem one can cite. The finite
  check (SAT/ILP on `n ≤ 64`) can settle the pattern; the inventor's own sanity
  checks (powers-of-2: `W(2^m) = m·2^{−m+1} → 0`, `W(2^m+1) = Ω(1)`) already
  explain why those strings have liminf 0 and confirm the right quantifier is
  liminf, not density-1.

### Who has applied it to this problem

Nobody. The influence/Sierpinski vocabulary is standard, but the specific
recast of `G-sup-implies-switch` as a dyadic weighted-`popcount` liminf
statement appears nowhere in the searched literature. This is not a proof of
novelty — it is a report that the search found no precedent, which is exactly
the honest ground for calling the crux open rather than settled.

### What it would buy

If the finite check supports `inf W_S = 0` for sparse `S` (UNSAT across a sparsity
grid), it is the cleanest route to the equivalence theorem SUPPLY ⇔ switch
density (GOAL priority 3 / problem result 5): a genuine negative closure. If a
sparse `S` with `W_S ≥ c` for all large `n` is found, it is an explicit growing
witness that SUPPLY is strictly weaker than switch density — a new direction. The
column bound alone is a cheap, verifiable structural fact.

**Distinct from the closed doors.** The single-boundary family `e_{n−1}`
(claim `single-boundary-one-refutes-switch-equivalence-as-stated`) refutes the
*literal per-window* form of the converse, but that family uses a position that
moves with `n`; candidate 1 is about a *fixed* `S`, so it is not caught by that
refutation. It is also not the refuted `furstenberg-measure-rigidity` route
(which concerned the collapse of ×2-invariant inputs), and not
`anf-mobius-reed-muller` (which hit the open RM weight-spectrum — candidate 1
does not need the RM spectrum).

**Status: grounded** — the reformulation is real, named, its first half is
provable/verifiable, and its decisive claim is a genuinely open novelty with a
finite check available. Set `status: grounded`, `precedent`: influence + KKL
(Cambridge CPC / Kahn–Kalai–Linial), Callan Sierpinski/Thue–Morse
arXiv:math/0610932, and the in-workspace claims. The open crux itself is a
`request_research` candidate.

---

## 2. `mixing-implies-linear-fold` — grounded (hypothesis is the gate)

### What the reformulation is actually called

The route promotes the already-proved meet-join Parseval identity
(`E_{μ_p}[S(n)²] = F_n(1−2p) = O(n)`, adopt `fold-second-moment-krawtchouk` /
`meet-join-parseval-self-duality`) from **product measures** to **mixing
measures**, with the surviving open statement `E[S(n)²] = O(n)` read as a
**correlation-decay transfer theorem**: if the ±1 process `ε_j = (−1)^{h_j}` on
the prime switch string has sufficiently decaying correlations, then the fold's
second moment is `O(n)` and, by Chebyshev, `ν₂/n → 1/2` on a density-1 set.
This is GOAL priority 2 (weakest arithmetic input), priced as exactly as it can
be today.

### Theorems it relies on, and whether hypotheses hold here

- **Meet-join Parseval / distance enumerator** `E_{μ_p}[S(n)²] = F_n(1−2p) = O(n)`:
  already adopted and proved in-workspace (`downset-row-intersection-meet-formula`
  gives `|M_d △ M_{d'}| = 2^{pc(d)} + 2^{pc(d')} − 2^{pc(d∧d')+1}`; `F_n(z) = O(n)`
  for `|z|<1`). Holds here. **Scholze gate satisfied**: the mixing setting
  reproduces the product-measure case as the `z^{|M_d△M_{d'}|}` specialization.
- **ψ-mixing product-over-separated-blocks correlation decay**: the named theory
  is Bradley's *Basic Properties of Strong Mixing Conditions, a Survey*
  (DOI 10.1214/154957805100000104; also Bradley 1986), which fixes ψ, ψ′, ρ, φ, β
  coefficients and their interrelations. The needed estimate — that the
  correlation of a product over a set that is a union of `k` separated intervals
  factors up to a function of the gap lengths and the mixing coefficients — is
  standard in this theory (this is why the fold's structure, where `M_d △ M_{d'}`
  is a union of intervals governed by the run telescope, is the right home).
  Holds as the transfer engine.
- **The input hypothesis** — *the prime switch string `ε_j = χ₄(q_j)χ₄(q_{j+1})`
  is ψ-mixing with summable coefficients*: **NOT established.** The two-point
  correlation whose decay the hypothesis needs at dyadic lags includes the
  `g=0` adjacent term `Σ_j χ₄(q_j)χ₄(q_{j+1})`, which is the mod-4 switch-pair
  object — the named parity barrier (`abgs-p1-wide-open`,
  `lau-nonconstant-pattern-open`). No theorem bounds its decay. The inventor's
  falsifier (c) fires here as a live risk: the LOS bias (`los-scale-bias-slowdecay`
  — the pair-frequency bias decays at the `loglog/log` scale, which is **not**
  summable) is a first-order mean effect, but it warns that full ψ-mixing may be
  too strong an assumption.

### Who has applied it to this problem

The ψ-mixing machinery is standard and heavily used for correlation decay of
products over blocks (Bradley survey; copula-Markov ψ-mixing literature; the
interlaced-ρ equivalence of lower ψ-mixing / exponential decay). Nobody has
applied it to the fold's distance-enumerator second moment for a fixed prime
string; the encyclopedia of applications covers random processes, not the
fixed prime `ε` string. This is a report of no-found-precedent for *this fold*,
not a theorem of absence.

### What it would buy

A genuine transfer theorem: *correlation decay of `ε` ⇒ `E[S(n)²] = O(n)` ⇒
density-1 SUPPLY*, naming the weakest arithmetic input exactly. The measured
margin is large (`anticorrelation-margin-of-the-fold`: the primes' lag-1
autocorrelation ≈ −0.04 sits at `1−2a ≈ −0.08`, a ~9× margin before the fold's
balancing degrades), so a summable-ψ input would settle SUPPLY's density-1 form
with substantial slack — *if* such an input were proved for the primes, which
is the untouched gate.

**Distinct from adopted `lucas-mixing-finite-transfer`**: that route's engine is
Pivato–Yassawi Lucas mixing on the 2-adic odometer (measure-level ergodic
equivalence, `lucas-mixing-iff-fold-randomization`) with no finite transfer.
Candidate 2 is a *probabilistic* correlation-decay transfer through the distance
enumerator, orthogonal: it attacks the same surviving statement
(`E[S²]=O(n)`) from the mixing side rather than the LCA ergodic side.

**Status: grounded** on the transfer machinery, **hypothesis open**. Set
`status: grounded`, `precedent`: Bradley's survey (DOI 10.1214/154957805100000104),
the meet-join Parseval claims, the modulus-4 parity-barrier claims, LOS slow-decay.

---

## 3. `maynard-pattern-densification` — refuted

### What the reformulation is actually called

Read each fold cell as a fixed **multi-point residue pattern**: `T(n,2) =
h[n−3] ⊕ h[n−1]` is a 4-point pattern of the residue string
(`[r_{n−3}≠r_{n−2}] ⊕ [r_{n−1}≠r_n]`), etc. `ν₂(n)` counts odd cells, so
SUPPLY asks for a positive density of odd cells. The route wants the
unconditional **consecutive-prime residue-pattern** theorems — Maynard's
admissible-tuple machine, BFTB bounded-gap equal-residue strings, Lau's
"≫ m/(log m)^10 · φ(q)² m-tuples infinitely often" — to supply a *non-constant*
pattern input, then a **densification lemma** to convert infinitely-often (or
bounded-gap) occurrence into positive density of odd cells via window overlap.

### Theorems it relies on, and whether hypotheses hold here — **they fail at the fold's modulus**

- **Lau's count bound** (`lau-pattern-count-bound`, Lau arXiv:2409.12819,
  Thm 1.5 / Cor 1.6–1.8): *for `q` squarefree with `φ(q) ≫ (log m)^10`, at least
  `≫ m/(log m)^10 · φ(q)²` residue-class m-tuples occur infinitely often among
  consecutive primes.* **Hypotheses fail here.** The fold's input needs the
  modulus **`4 = 2²`, which is NOT squarefree**. Lau's theorem does not apply at
  `q=4, m=2`, so it cannot supply the non-constant mod-4 pair input.
- **Lau's own emphasis** (`lau-nonconstant-pattern-open`): *even a single
  non-constant pattern of length `m` — in particular the 2-term `(1,3)`/`(3,1)`
  mod 4 switch — is not known to occur infinitely often.* So even where Lau's
  count bound applies (squarefree q), it counts patterns that are not
  specifically the non-constant ones the fold needs; the non-constant side is,
  by the source's own statement, beyond current methods.
- **Maynard 3.3 / BFTB** (`maynard-positive-density-congruent-strings`,
  `bftb-bounded-gap-equal-residue-strings`): these are unconditional and hold
  at `q=4`, but they are the **equal-residue** direction (`p_n ≡ … ≡ p_{n+m}
  mod q`). In the gap-parity string `h`, a run of equal residues is a run of
  *constant* `h`, i.e. the *wrong parity direction* — it is the closed door
  #2/#3 machinery, not a source of switch/odd cells.

### Why it is refuted

The route's arithmetic input — *non-constant mod-4 residue patterns occur
infinitely often, or with positive density* — is exactly the parity barrier
(`abgs-p1-wide-open`; `lau-nonconstant-pattern-open`). The three named engines
cannot produce it: Lau fails at the non-squarefree modulus `q=4` (and even in
its valid regime finds no non-constant patterns), and Maynard/BFTB supply only
the equal-residue (wrong) direction. Therefore the **densification step has
nothing to densify**: there is no provably-infinitely-often supply of the
non-constant patterns the fold's odd cells need, so the window-overlap lemma is
never fed. The route collapses into the dead switch-density reduction at the
first step (its own falsifier (a)/(c)).

### Who has applied it to this problem

Nobody has applied these pattern theorems to `wt(Φ_n h)`; more importantly,
every settled instance of them (Shiu, BFTB, Maynard, Lau) is on the
equal-residue side, which SUPPLY does not need. The non-constant side the fold
requires is open and L-function-inaccessible. No source found.

### What it would buy

Nothing over the existing reduction — it re-proposes the switch-density
hypothesis in the vocabulary of multi-point patterns, but cannot reach even the
two-point non-constant pattern, which is the whole difficulty. The fold's
multi-point reading is real (`endpoint-sign-corrected-identity`), but the
arithmetic supply that would make it bite is unavailable.

**Status: refuted.** `killed-by`:
`lau-pattern-count-bound` hypotheses fail at `q=4` (modulus must be squarefree;
`4 = 2²` is not) + `lau-nonconstant-pattern-open` (even one non-constant mod-4
pattern is beyond reach) + `maynard-positive-density-congruent-strings` /
`bftb-bounded-gap-equal-residue-strings` give only the equal-residue (wrong)
direction. The densification step is never fed.

---

## Summary for the board

- **read-cone-column-equivalence**: the one candidate whose arithmetic claim is
  genuinely novel and checkable. Machinery grounded; crux (`inf_n W_S = 0` for
  density-0 `S`) open, finite-checkable, and the cleanest route to the
  equivalence theorem. **grounded.**
- **mixing-implies-linear-fold**: grounded transfer machinery; the input
  hypothesis (prime `ε` ψ-mixing, summable) is the untouched, possibly-too-strong
  gate (LOS non-summable decay). **grounded.**
- **maynard-pattern-densification**: refuted — the non-constant pattern input is
  the parity barrier, Lau's engine fails at `q=4`, Maynard/BFTB supply the wrong
  direction. **refuted.**

The recurring lesson stands: no named tool supplies the two-point non-constant
mod-4 input; the two grounded routes attack the *second moment* or the *column
geometry* to avoid needing pointwise switch density, which is the only family the
literature leaves open.
