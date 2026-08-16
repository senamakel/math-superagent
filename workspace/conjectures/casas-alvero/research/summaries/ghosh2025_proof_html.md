# Ghosh, *Proof of the Casas-Alvero conjecture* (arXiv:2501.09272, v1 Jan 2025, v2 Mar 2026 "major revisions")

Full text: [[ghosh2025_proof_html.full]]

The current strongest **claimed** complete proof of CA. **Unverified preprint** — not peer-reviewed, no independent validation, Wikipedia still lists "Unsolved" with d=20 smallest open. Per GOAL.md, the run treats CA as open until this stands; the single most valuable object here is the **char-0-only step**, which this summary isolates.

## What is claimed

```claim
id: ghosh-2025-claim
statement: Theorem A: Let f be monic of degree d≥3 over a char-0 field K. Then
  gcd(f,f_i) non-trivial for all i=1,…,d−1 iff f = (X−α)^d. I.e. CA holds in ALL
  degrees d≥3 over every char-0 field. Corollaries: for each d a finite set P(d) of
  primes such that CA holds in degree d unless char K ∈ P(d); and dim X_d = 0 for all d≥3.
hypotheses: characteristic 0; d≥3
holds-here: this is the claimed theorem — unverified
status: asserted-by-source (preprint, "major revisions" on v2)
bearing: If it stood, the run's target would change to stress-testing it. It does not
  stand; the working assumption remains CA open. The proof structure is anyway the
  thing to learn from: downward induction on degree + Koszul homology + a ℂ step.
anchor: research/sources/ghosh2025_proof_html.full.md (Theorem A, §4)
falsifies: peer-review rejection, a found gap, or an independent check failing.
```

## The char-0-only step (the load-bearing point for this run)

```claim
id: ghosh-char0-step
statement: The proof proceeds by downward induction on degree d (assume degree n+1,
  prove degree n). It has two ingredients: (1) an algebraic step showing local and
  global minimal numbers of generators of the relevant ideals coincide, reduced (local
  → global) using Abel–Gontcharoff polynomials and the topological Brouwer-degree
  theory, applied over ℂ; (2) a homological step via Koszul homology relating the
  truncated Koszul complexes in degrees n+1 and n through a filtration. The intro
  states explicitly: "this step works only over ℂ."
hypotheses: char 0 (specifically ℂ for the Brouwer-degree step)
holds-here: true — this is the named candidate for the step that must break in char p
status: asserted-by-source (intro §1.1.1, §4)
bearing: CA is false in char p, so some step must break there. The ℂ/Brouwer-degree
  ingredient has no char-p analogue and is the prime candidate. The Koszul/homological
  part alone, run in char p, must NOT collapse to the (false-in-char-p) conclusion —
  that is the test to run.
anchor: research/sources/ghosh2025_proof_html.full.md (intro §1.1.1, §4)
falsifies: showing the ℂ step is inessential (then the proof proves a false char-p statement).
```

## How it relates to the settled universe
- Uses, as the base of the downward induction, the finitely-many-settled-degrees results ([Graf-von-Bothmer] p^k, 2p^k + [Castryck] d=12 etc.): "we invoke the results of [16]/[11] which verify the conjecture in infinitely many degrees, and thereby along with our downward induction, prove CA in all degrees." So if any base degree's verification fails, the induction collapses — another attack surface.
- Restates the CA-as-regular-sequence reformulation (Prop D = [14, Prop 5.2]): CA(d) over alg-closed K iff for all index choices the sequence of homogeneous polynomials `Φ^#(H D)…` is regular in `K[x_1,…,x_{d−1}]`. This is the Schaub–Spivakovsky / Ghosh-2024 complete-intersection reformulation that the run's scheme argument targets.

## What it does not settle
No peer review, no independent verification. The "almost counterexamples over ℂ satisfying weaker hypotheses" (Brouwer-degree consequences) are asserted. The downward-induction base depends on the (also-unverified) Ghosh 2024. Nothing here changes the standing status: **CA open**.
