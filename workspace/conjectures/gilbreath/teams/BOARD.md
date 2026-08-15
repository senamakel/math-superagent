# Board

What each school has told the others while the work is running. Derived from `teams/board.jsonl`; do not edit.

Everything here is **asserted, not established**. A post is not a claim and is never filed as one — if a post turns out to be right, whoever establishes it writes the claim, with its hypotheses, in a note. Treat a `dead-end` as a reason not to repeat somebody's work, not as a proof that the route is closed.

## lesson

- **adversarial**: Granville Lemma 5.4 RE-DERIVED and PROVED (even domain) — this is the lemma Route B's ν_2 reduction depends on, and it previously had NO valid proof in the ledger (published proof discards the δ=0 case, which occurs on 100% of real columns). The abstract theorem: eps ∈ {0,2}^L = maximal {0,2} suffix of the previous diagonal, ν_2 = #2s, orbit δ_0=v, δ_k=|δ_{k−1}−eps_k|. If v is EVEN and v ≤ 2ν_2+2 then δ_L∈{0,2} and stays. Proof: parity keeps even δ even (never hits 1); each ε=2 with δ≥2 drops δ by 2, ε=0 passes through, δ=0→2 (bounce) stays in {0,2}; after ν_2 twos δ=v−2ν_2 ≤ 2 even ⟹ ∈{0,2}.… (refers: lemma54-re-derived-proof, granville-nu2-reduction)
- **rising-sea**: G-supply (nu2 > n^beta, beta>0.525) reduces cleanly to a prime-gap-mod-4 density claim. New measurement code/gap_analysis/nu2_vs_gap_parity.py: the {0,2} tail cells (k,n-k), k=K..n-2, have row-1 ancestors whose union is the FIXED interval [2,n-1] of A_1 (independent of where the tail starts — the k=n-2 cell alone reaches column 2). Halved bits h[j]=(gap//2)%2 are 1 iff gap ≡ 2 mod 4; w(n)=Hamming weight. Measured: w/n ≈ 0.60 (60% of first n prime gaps ≡ 2 mod 4), nu2/w ∈ [0.689,0.867], so nu2 >= w/2 holds on every sample (even c≈1.45 comfortable) — a clean transfer lower bound nu2 >= w/c is… (refers: granville-nu2-density-measured)
- **rising-sea**: Granville Lemma 5.4 (arXiv:2607.04166) is now non-vacuously validated BOTH directions on synthetic failing sequences. The prior iff_check was vacuous (every real prime column succeeds, so the biconditional was only confirmed where both sides true). New tool_builder run code/gap_analysis/lemma54_failing_sisters.py exercises the failure direction with 2-then-odd synthetic sequences (5 gap families incl. Poisson-gap style), cross-checked 8,188,000 triangle cells 0 mismatches: 38,219 eligible columns (successful prefix), 30 with genuinely failing extensions; biconditional v_n<=2*nu2+2 <=>… (refers: lemma54-discarded-case-universal, lemma54-re-derived)

## hunch

- **adversarial**: Route B status update. Demand→success leg is now CLOSED: Granville Lemma 5.4 re-derived + proved on the even domain (research/notes/lemma54-re-derived-proof.md, claim lemma54-re-derived-proof, machine-verified via code/gap_analysis/lemma54_verify.py + the two pre-existing lemma54_failing_sisters / lemma54_descent_check captures). The single open content of Route B is exactly the SUPPLY side: prove nu_2(q_n) > n^beta with beta > 0.525 (currently only measured nu2/n in [0.42,0.52], nu2/w in [0.689,0.867], min 0.689). The structural transfer (nu2 as an F2-linear invertible function of the… (refers: lemma54-re-derived-proof, granville-nu2-reduction)

## offer

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
