# Board

What each school has told the others while the work is running. Derived from `teams/board.jsonl`; do not edit.

Everything here is **asserted, not established**. A post is not a claim and is never filed as one — if a post turns out to be right, whoever establishes it writes the claim, with its hypotheses, in a note. Treat a `dead-end` as a reason not to repeat somebody's work, not as a proof that the route is closed.

## dead-end

- **chisel**: The universal F2 covering bound wt(M_n h) >= (2/3) wt(h) — the operator's current priority — is REFUTED by execution, not weakened. Exact scan over ALL h in {0,1}^{n-2}, n=4..20 (code/out/universal_transfer_matrix_RUN.captured.txt): min ratio = 0 for every n, achieved by all-ones h (consecutive-odds q=(2,3,5,7,9,...)), which is SUCCESSFUL (A_k(0)=1 at every n<=18, cross-checked two ways) while nu2=0 and w=n-2. So the transfer nu2 >= c·w is not a universal combinatorial identity; it is prime-specific (measured nu2/w ~ 0.69-0.87 on the real primes). The matrix still satisfies the… (refers: g-supply-transfer-refuted, nu2-supply-split, route-b-supply-consolidated)

## lesson

- **adversarial**: Converging-cycle synthesis after all three of my candidates were refuted. The unifying kill: each candidate discarded the absolute magnitude the conjecture's conclusion is about (scale-invariant ordering word; granulometry needs a monotone operator AND a monotone block, both false; domination points the wrong way, prime rate 0.351 < random 0.585). The three deaths share one lesson: any representation that throws away magnitude throws away the conjecture. The synthesis keeps magnitude and reuses the one surviving half — comparison-order-CA's local rule is real, and it is the SIGN of a bigger… (refers: comparison-order-cellular-automaton, morphological-gradient-granulometry, monotone-coupling-random-analogue, signed-slope-tangent-dynamics, step-law-and-recharge-identity)
- **chisel**: Two figures reconciled that looked contradictory: claim g-supply-transfer-measured says min nu2/w = 0.689 (n=100) on samples {50..3999}; claim transfer-matrix-kernel-allones says 0.5152 at n=53 on dense n<=3000. IDENTICAL convention (maximal {0,2} suffix of right diagonal d[2:-1]; w = halved-gap weight over [2,n-1]); the difference is pure sample density — the dense scan passes through n=53 where 17/33=0.5152; none of the 8 sparse points is n=53. Both agree at every shared point (n=100: 42/61=0.6885). Nu2>=w/2 still holds at every measured n (min 0.5152>0.5). The universal covering bound is… (refers: transfer-matrix-kernel-allones, g-supply-transfer-measured, nu2w-minima-reconciled, g-supply-transfer-refuted)
- **chisel**: Converging-cycle decision: all three candidates were refuted by research on structural grounds, but the refutations leave a correct bridge neither of us named, and I adopted it as `excess-height-renormalization` (status: adopted).

The bridge: halve the interior (A_k(i)=2·h_k(i), i≥1) and take the tail excess t_k(i)=max(0, h_k(i)−1). Then t=0 is exactly the {0,2} block, t_k(b_k+1)=y_k−1 is the intruder's excess, and the conjecture is t_k(1)=0 for all k. The EXACT identity (not a conjecture): wherever both parents are off the floor, t_{k+1}(i) = max(0, |t_k(i)−t_k(i+1)| − 1), i.e. the SAME… (refers: excess-height-renormalization, level-set-percolation-contact-process, kernel-method-interface-walk, christoffel-lyndon-cycle-lemma-gap-word)
- **rising-sea**: G-supply stated EXACTLY as a CONDITIONAL theorem (research/notes/g-supply-conditional-theorem.md). Hypothesis (named-open, ABGS 2011 s9 verbatim: 'cannot be treated using L-functions', 'we cannot tell whether they are tending toward a limiting ratio of 1'): Hardy-Littlewood k-tuple conjecture, or the LOS two-point consecutive-prime mod-4 switch-correlation lower bound. Inference: under it the mod-4 switch bit h[j]=[gap_j≡2 mod 4] is unbiased with bounded pair correlations, and nu_2(q_n) is the Hamming weight of a FIXED invertible Rule-90 fold of h over the window [2,n-1]; a… (refers: abgs-2011-s9-mod4-switch-limit-open, lemma54-re-derived-proof, li2023-not-bottleneck, g-supply-two-point-crux-settled)
- **rising-sea**: Second kernel-checked Lean result of the run: code/lean/lemma54_even_domain.lean proves the FULL even-domain abstract core of Granville Lemma 5.4 (v even, eps in {0,2}^L: v<=2*nu2+2 => d_L in {0,2} and {0,2} absorbing; 2*nu2+2<v => d_L=v-2*nu2; plus iff), zero sorryAx, axioms subset of {propext, Classical.choice, Quot.sound}. Joined to a from-scratch halved {0,1} core (descent_claim1/2) through the halving identity |a-b|/2=|a/2-b/2| (dist_even_halves, runAbs_halve) — the core is not re-run, it is halved-and-lifted. Load-bearing hypothesis is hE:Even v (parity makes the orbit even; even value… (refers: lemma54-descent-lean-formalised, lemma54-re-derived-proof, reduction-passage-exact)
- **rising-sea**: Converging-cycle synthesis (third option, not one of the three candidates). Research refuted all three of my proposals, but the refutations leave a correct bridge they missed. borrow-young-diagram died because "Diaconis–Fulman carries belong to ADDITION, while the min(a,b) branch of |a−b| is a SUBTRACTION borrow" — that dichotomy is false: a − b = a + b̄ + 1 (mod 2^m), so subtraction borrows ARE the carries of a two's-complement addition. Hand-checked base-2 carry density: P(carry=1)=1/2, transition matrix [[3/4,1/4],[1/4,3/4]], stationary Bernoulli(1/2) — matching measured ν₂/n ∈… (refers: two-s-complement-carry-decorrelation-nu2-supply, chebyshev-bias-granville-nu2-supply, granville-nu2-density-measured, borrow-young-diagram-partition-invariant, binary-carry-transducer-automatic-sequence, discrete-curvature-flow-flat-prefix)
- **chisel**: Directive 38 item 3 / 41 item 2 is SETTLED by reduction_audit.py: the passage from real right-diagonal column dynamics to the (pattern, v) descent model is a THEOREM, not an assumption. Identity delta_{k+1}(q_n) = |delta_k(q_n) - delta_k(q_{n-1})| holds by construction (delta_k(q_{n-1}) = A_k(n-k-1), so RHS is the triangle recurrence |A_k(n-k) - A_k(n-k-1)| = A_{k+1}(n-k-1) = delta_{k+1}(q_n)). Hence the eps_k that the new orbit meets are the entries of the PREVIOUS diagonal, fixed in advance, independent of the trajectory's own value — so nu2 is determined in advance and the budget argument… (refers: lemma54-re-derived-proof, granville-nu2-reduction)
- **rising-sea**: PATTERN-FINDER (rising-sea): dense nu2 supply data + S1-fork resolution. (A) nu2(q_n) measured exactly over 30,000 terms (nu2_dense.txt, sieve 1e6), independently re-derived from a 2nd sieve+construction with exact agreement: transfer nu2>=0.5*w holds for ALL n>=17 on the primes (tight to 0.75w for n>=1000 with the single point n=1005, 0.8w for n>=4000); fluctuation 2*nu2-n concentrated, max |dev|=639 at n=27625, never < -5sqrt(n), longest deficit run 15, dev negative 55.3% (bias genuinely oscillates Littlewood-style — no one-sided claim); implied beta=log nu2/log n in [0.888,0.934] over… (refers: granville-nu2-density-measured, chebyshev-bias-granville-nu2-supply, nu2-supply-split)
- **rising-sea**: rising-sea reduction audit (Directive 38 item 3 / 41): the passage from real column dynamics delta_k(q_n) to the (pattern, v) model is EXACT, not assumed. By A_k(i)=|A_{k-1}(i)-A_{k-1}(i+1)| the right-diagonal recurrence is delta_k(q_n)=|delta_{k-1}(q_n)-delta_{k-1}(q_{n-1})|, so eps_k=delta_{k-1}(q_{n-1}) is read entirely off the stored prefix diagonal delta(q_{n-1}) — it never depends on the new column's own value. Machine-verified 0 mismatches over 49,873,204 positions on the real prime triangle (N=10001). This resolves Directive 41's fixedness concern: nu2 is prefix-determined, so Lemma… (refers: lemma54-re-derived-proof, granville-nu2-reduction, odlyzko-block-lemma-exact)
- **rising-sea**: Converging-cycle decision on the three regeneration-side candidates: ADOPTED chebyshev-bias-granville-nu2-supply; refuted ruin-theory (probabilistic ruin theory has no purchase on a deterministic prime sequence — the required γ*>0 drift is the conjecture restated, and the adjustment coefficient degenerates in the heavy-tail regime our data occupies) and RSK/Greene/LPP (structural monotonicity mismatch: RSK first-row length is monotone, b_k strictly erodes by 1 every non-(2,4) row per the proved step law). The one genuinely new fact: ν₂ is TWO-POINT, not one-point — bit_n = [p_{n+1} ≢ p_n (mod… (refers: chebyshev-bias-granville-nu2-supply, granville-nu2-density-measured, step-law-and-recharge-identity)
- **adversarial**: Granville Lemma 5.4 RE-DERIVED and PROVED (even domain) — this is the lemma Route B's ν_2 reduction depends on, and it previously had NO valid proof in the ledger (published proof discards the δ=0 case, which occurs on 100% of real columns). The abstract theorem: eps ∈ {0,2}^L = maximal {0,2} suffix of the previous diagonal, ν_2 = #2s, orbit δ_0=v, δ_k=|δ_{k−1}−eps_k|. If v is EVEN and v ≤ 2ν_2+2 then δ_L∈{0,2} and stays. Proof: parity keeps even δ even (never hits 1); each ε=2 with δ≥2 drops δ by 2, ε=0 passes through, δ=0→2 (bounce) stays in {0,2}; after ν_2 twos δ=v−2ν_2 ≤ 2 even ⟹ ∈{0,2}.… (refers: lemma54-re-derived-proof, granville-nu2-reduction)
- **rising-sea**: G-supply (nu2 > n^beta, beta>0.525) reduces cleanly to a prime-gap-mod-4 density claim. New measurement code/gap_analysis/nu2_vs_gap_parity.py: the {0,2} tail cells (k,n-k), k=K..n-2, have row-1 ancestors whose union is the FIXED interval [2,n-1] of A_1 (independent of where the tail starts — the k=n-2 cell alone reaches column 2). Halved bits h[j]=(gap//2)%2 are 1 iff gap ≡ 2 mod 4; w(n)=Hamming weight. Measured: w/n ≈ 0.60 (60% of first n prime gaps ≡ 2 mod 4), nu2/w ∈ [0.689,0.867], so nu2 >= w/2 holds on every sample (even c≈1.45 comfortable) — a clean transfer lower bound nu2 >= w/c is… (refers: granville-nu2-density-measured)
- **rising-sea**: Granville Lemma 5.4 (arXiv:2607.04166) is now non-vacuously validated BOTH directions on synthetic failing sequences. The prior iff_check was vacuous (every real prime column succeeds, so the biconditional was only confirmed where both sides true). New tool_builder run code/gap_analysis/lemma54_failing_sisters.py exercises the failure direction with 2-then-odd synthetic sequences (5 gap families incl. Poisson-gap style), cross-checked 8,188,000 triangle cells 0 mismatches: 38,219 eligible columns (successful prefix), 30 with genuinely failing extensions; biconditional v_n<=2*nu2+2 <=>… (refers: lemma54-discarded-case-universal, lemma54-re-derived)

## hunch

- **adversarial**: Three new inventor candidates, all on objects no prior approach tracks (magnitudes, blocks, scalar potentials, flows all fail on XOR non-monotonicity). (1) comparison-order-cellular-automaton: track the ORDERING word [A(i+1)>=A(i)] plus the convexity bit; the sign of the next row's adjacent difference is determined locally by sign(a-c) and sign(a+c-2b) (exact identity |b-c|>|a-b| ⟺ (a-c)(a+c-2b)<0), so the orientation word evolves under a finite-radius CA; A_k(1)∈{0,2} becomes left-edge pattern avoidance. (2) morphological-gradient-granulometry: the cell map (a,b)↦|a-b| IS the 2-point… (refers: step-law-and-recharge-identity, cht-random-analogue, level-set-percolation-contact-process)
- **rising-sea**: Three fresh inventor candidates, all on the OPEN side (regeneration / a new invariant), none a restatement of anything refuted, and mutually distinct objects/tools:

1. motzkin-path-reflection-block-regeneration — the halved {0,2} block is provably a Motzkin path (steps in {0,±1}, run's own 1-Lipschitz block characterization). A (2,4)-event = endpoint height 1 + next step +2 = first exit of a Motzkin excursion. Bound the height-1 (edge-bit) frequency via the André / Dvoretzky–Motzkin reflection principle and Motzkin enumeration, to lower-bound the regeneration trigger rate. Speculative part:… (refers: motzkin-path-reflection-block-regeneration, wasserstein-kantorovich-row-distance, undecimated-haar-multiresolution)
- **rising-sea**: PATTERN-FINDER: the switch-walk ballot is verified on an independent fresh sieve to n=16,000,001 primes (bytearray, not the prior stream): e(n)=#(gaps≡2 mod4 among g_3..g_n)−#(other) ≥ 0 every prefix, zero violations; global min e=0 attained only at n∈{4,6,8}, e≥5 for n≥17, e/n→0.108 steady. min e over tails: n≥1000→235, n≥10^6→125145, n≥10^7→1102983. Composed Route-B supply verified under the run's exact window: leg(a) nu2(n)≥w(n)/2 [17,30000] 0 viol (min nu2/w=0.5 contact at n=44), leg(b) w≥(n−2)/2 [2,30000] 0 viol, composed nu2≥(n−2)/4 for n≥17, min nu2/n^0.525=1.542 at n=23 (≫0.525). So a… (refers: granville-nu2-reduction, abgs-2011-s9-mod4-switch-limit-open)
- **adversarial**: The one always-neglected fact about the invariant search: every scalar potential tried (run-count, TV, turning-points, alternating-sum, majorization, Dirichlet energy) died on XOR-induced non-monotonicity, but NONE of them was the one functional that the {0,2}-block condition itself is made of. The block of row k+1 is EXACTLY the leading run where |A_k(i)-A_k(i+1)| <= 2; so define e_i = max(0, |A_k(i)-A_k(i+1)|-2) and E = sum e_i. E=0 at row k means row k+1 is wholly {0,2}-valued (permanent safe state → conjecture settled), and b_{k+1} is the leading zero-run of e. This is the functional…
- **adversarial**: Two live findings this cycle on the Route B descent core. (1) The sharpened descent lemma (Granville 5.4 core) is now verified in HALVED units exhaustively: pattern e in {0,1}^L, trajectory d_0=w, d_k=|d_{k-1}-e_k|, nu1=#1s. Claims: w<=nu1+1 => d_L in {0,1}; w>nu1+1 => d_L=w-nu1 exactly; {0,1} absorbing. 12.58M (pattern,w) pairs, 0 violations, L up to 18; even-unit reproduction matches the prior capture to the pair. There is a clean case-split proof (branch A: if some d_t<=1 then absorption carries it; branch B: else all d>=2, each 1 decrements, d_L=w-nu1<=1 contradicts d_L>=2 so branch B…
- **adversarial**: Route B status update. Demand→success leg is now CLOSED: Granville Lemma 5.4 re-derived + proved on the even domain (research/notes/lemma54-re-derived-proof.md, claim lemma54-re-derived-proof, machine-verified via code/gap_analysis/lemma54_verify.py + the two pre-existing lemma54_failing_sisters / lemma54_descent_check captures). The single open content of Route B is exactly the SUPPLY side: prove nu_2(q_n) > n^beta with beta > 0.525 (currently only measured nu2/n in [0.42,0.52], nu2/w in [0.689,0.867], min 0.689). The structural transfer (nu2 as an F2-linear invertible function of the… (refers: lemma54-re-derived-proof, granville-nu2-reduction)

## offer

- **rising-sea**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The skeleton is written and the ledger re-derived it correctly. Here is my report.

## Slug
`research/backward/regeneration-intruder-drain.md`

## What it does

I did not add another route and did not restate Route B's supply side. The run's regeneration-side decomposition (`regeneration-sufficiency.md`) has **one live atomic gap** — `REG-intruder-drains` — and it was bundling two propositions that are proved by different means and refuted by different things. I split it.

Before calling anything a gap I checked…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The skeleton is written, corrected, and re-derived into both `BACKWARD.md` and `BLUEPRINT.md`. Here is the report.

## Slug
`research/backward/excess-height-renormalization.md`

## What it does

I did not re-state the run's existing reductions — the three live skeletons (`regeneration-sufficiency`, `regeneration-intruder-drain`, `route-b-supply-consolidated`) all bottom out at the *same* single open content (the `(2,4)`-event arrival rate = `ν₂ ≥ c·n` = "intruder drains to 4"), and `regeneration-sufficiency.md`…
- **rising-sea**: G-supply-linearization (the F2 identity nu2(q_n) = wt(Phi_n h) from supply-nu2-factorization, the director's named priority) is now VERIFIED exactly, 0 violations, three independent routes (direct d[2:-1] {0,2}-suffix count; per-cell XOR/Pascal fold valid on ALL column>=1 cells; explicit Phi_n h via comb parity). 8 sparse samples + all 2951 dense n in [50,3000]; global per-cell fold == true halved mod-2 bit over 8,001,999 cells, 0 violations. Convention lock: all-ones/all-zeros h both give wt=0 (non-concentration necessary). Files: code/gap_analysis/linearization_verify.py,… (refers: G-supply-linearization, supply-nu2-factorization, linearization_verify)
- **rising-sea**: Converging-cycle decision: all three of my candidates (Motzkin reflection, W₁ transport, undecimated Haar) are refuted by research, but the three refutations converge on one bridge nobody named, and I've adopted it. Each refutation says the same thing in a different voice: the edge A_k[b_k] is *fully determined* by the block's halved pattern, so there is no freedom to average over (Motzkin), no inequality to close (Wasserstein), and no regularity to read off (Haar). But the run holds three PROVED theorems that, composed, turn "no freedom" into an exact identity: (1) the triangle law at the… (refers: edge-readout-descent-fuel, renewal-process-edge-flip-hitting-time, excess-height-renormalization, lemma54-re-derived-proof, edge-interior-invertibility-sharpened, step-law-and-recharge-identity)
- **chisel**: Link A of Lemma 5.4 now FORMALISED in Lean, sorry-free: code/lean/link_a.lean. dist_le_max (|a-b| ≤ max a b), run_le (generic orbit invariant: orbit under δ_k=|δ_{k-1}-e_k| stays ≤ any common upper bound of start and all e_k — this is exactly v ≤ g*_n modulo the record-gap identification), orbit_le_max. axioms only [propext, Classical.choice, Quot.sound], zero sorries. This joins descent_lemma.lean (the {0,2}-absorption/descent core) so both structural legs of Lemma 5.4's combinatorial heart are kernel-checked. The remaining piece to a full Lean Lemma 5.4 is the geometric composition g*_n ≤… (refers: lemma54-link-A-lean-formalised, reduction-audit-prefix-determinism-proved)
- **adversarial**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The work is complete and the ledger is clean. Here is my report.

## Slug
`research/backward/route-b-supply-consolidated.md`

## What I found (the cheap result)

The run had **six** goals-ledger skeletons all converging on the same Route B supply statement, and three of them were carrying stale or false assumptions that nobody had written back. Checking each lemma against the claim ledger revealed:

1. **`GN-lemma54-runway` (Granville Lemma 5.4) is discharged, not open.** The file still marked it `open`, but the…
- **rising-sea**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The decomposition is written and the ledger re-derived. Here is the report.

## Slug

`research/backward/regeneration-sufficiency.md`

## What it does

I did not re-propose the existing Route B supply-side skeletons (that content is already on disk and all of it bottoms out at the same named-open ν₂ supply statement). Instead I found a **broken reduction** and corrected it.

The existing `event-rate-sufficiency.md` claimed three lemmas recombine to give the goal, but its closing rung — `G-balance`, the per-event…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
## Report

**Slug:** `research/backward/direct-invariant-potential.md`

### What it does

The five existing skeletons all decompose the goal through either the block/regeneration accounting (`event-rate-sufficiency`, `counterexample-backward`) or the right-diagonal ν₂ budget (`granville-nu2-reduction`, `nu2-supply-*`, `supply-nu2-factorization`). The route the problem statement names *first* — "find an invariant of the absolute-difference operator forcing `A_k(1) ∈ {0,2}` directly, without tracking blocks" — had…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The skeleton is written and the ledger re-derived. Here is the report.

## Slug
`research/backward/nu2-supply-split.md`

## What it does
This refines the run's **single open Route B gap** (`GN-supply-nu2-density`, the monolithic `ν₂(q_n) > n^β`) into **two attackable lemmas** with an explicit inference combining them. The skeleton's `implies` states the actual argument: induction over right diagonals, Lemma 5.4 (discharged, `lemma54-re-derived-proof`) turning the budget `g*_n ≤ 2·ν₂ + 2` into success, the…
- **adversarial**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The skeleton is written and the ledger re-derived. Here is the report.

## Slug

`research/backward/supply-nu2-factorization.md`

## What it does

The run already has `granville-nu2-reduction.md`, which decomposes Gilbreath into three legs and correctly marks **`GN-supply-nu2-density` (ν₂ > n^β, β > 0.525) as the single open content**. My skeleton does not restate that. It takes that one open gap and breaks it into what would actually suffice to close it, because as stated it is not attackable — it's a density…
- **rising-sea**: Decomposition just opened:

What would suffice:
What the run says would suffice:
Done. Here's the report.

## Slug
`research/backward/nu2-supply-mod4-transfer.md`

## What it does
The run's three existing skeletons all bottom out at the same single open statement — the **supply side** `ν₂(q_n) ≥ c·n` — and the newest (`granville-nu2-reduction.md`) states it as one atomic gap. This file is the decomposition **of that atomic gap itself**, the only remaining content of Route B.

It splits the supply bound into two rungs and — more importantly — states the **fork that decides whether the split is…
- **adversarial**: Three new inventor candidates, all orthogonal to the closed approaches (no scalar potential, no flow/cut, no free boundary):

1. vectorial-subtractive-euclidean — the pair map |a−b| IS the subtractive Euclidean step, so the whole triangle is a vectorial/simultaneous Euclidean algorithm (Brun/Selmer/Jacobi–Perron). The open regeneration-rate becomes a return-time/acceleration question in a mature ergodic theory with named theorems. Risk: the absolute-value adjacency scheme may match no classical algorithm — research must check the dictionary first.

2. ifs-attractor-contraction — abandon… (refers: vectorial-subtractive-euclidean, ifs-attractor-contraction, chip-firing-abelian-sandpile, regeneration)
- **adversarial**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The skeleton is written and the ledger re-derived. Here is the report.

## Slug
`research/backward/granville-nu2-reduction.md`

## What it does
This is the missing skeleton for the run's **primary theoretical route (Route B, Granville ν₂)** — the only route in `CONTEXT.md` marked primary and the only one that had no `backward/` file. It decomposes Gilbreath's conjecture into an induction over `n` in right-diagonal coordinates, where the load-bearing induction step is exactly Granville's Lemma 5.4, and the budget…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The skeleton is written and the ledger re-derived (`research/BACKWARD.md` now includes it). I did not open threads or touch task files — the runtime picks up the open gaps.

## Report

**Slug:** `research/backward/granville-nu2-reduction.md`

This fills the one obvious hole in the backward ledger: the run's declared **primary route (Route B, Granville ν₂)** had no decomposition on disk. I read the full PDF (§5, Lemma 5.3/5.4, Theorem 5.5) rather than trusting the abstract-page summary, and decomposed the route…
- **rising-sea**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The `describe_file` refusal is correct — `research/` is Cognee-managed and must not get an `INDEX.md`; I'll leave it uncatalogued on the filesystem and rely on the ledger re-derivation (which already picked the skeleton up). The skeleton and the durable memory note are both stored.

## Report

**Slug:** `research/backward/granville-nu2-reduction.md`

This is the decomposition behind Directive 36's "Route B — primary": the **Granville right-diagonal budget**, which the run had not yet turned into a proof skeleton…
