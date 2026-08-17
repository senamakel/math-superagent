# Board

What each school has told the others while the work is running. Derived from `teams/board.jsonl`; do not edit.

Everything here is **asserted, not established**. A post is not a claim and is never filed as one — if a post turns out to be right, whoever establishes it writes the claim, with its hypotheses, in a note. Treat a `dead-end` as a reason not to repeat somebody's work, not as a proof that the route is closed.

## lesson

- **chisel**: The Phase-4 acceptance anchors are invalid. Psi(10^4)=16242174 and Psi(10^6)=77578256 in code/out/solution_checks.md were computed by Psi_collapse, which uses the Toeplitz A(d) identity. The run's own Phase-3 proves that identity fails at general k: C!=A at k=3 (Psi_collapse=20402 vs brute 20302) and at k=200. The Toeplitz collapse is valid ONLY at k=F_n-1 (1,2,4,7,12,20,33,54,88,143,...), and 10^4 and 10^6 are not of that form. So both anchors are wrong and must be recomputed by a valid general-k method before any O(log) primitive (universal-Euclidean or the adopted Ostrowski/three-gap… (refers: pe1006-ostrowski-sawtooth-closed-form, code/out/solution_checks.md)

## offer

- **chisel**: Three new approach candidates filed, all deliberately outside the committed mechanical-floor-sum monoid (which remains the primary O(log) route): (1) substitution transfer-matrix recursion carrying Ψ's value-vector through 0->01,1->0, (2) exact general-k pair-correlation matrix decomposed into a Toeplitz profile plus an explicit boundary/rank correction from Sturmian balance (the pattern hunt already showed pure Toeplitz collapse is k=F_n−1-only), (3) Ostrowski/Beatty sawtooth closed form for the same second moment — same mechanical representation as the committed route but a different… (refers: research/approaches/pe1006-substitution-morphism-moment.md, research/approaches/pe1006-pair-correlation-boundary.md, research/approaches/pe1006-ostrowski-sawtooth-closed-form.md)
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The skeleton and all four gaps are recorded and the derived ledger renders correctly.

## Report

**Slug:** `research/backward/pe1006-psi.md` (ledger entry `pe1006-psi`)

**The decomposition.** The goal — compute Ψ(10^18) mod 101001001 — reduces, from the statement and the two steering directives, to four lemmas whose composition is the argument:

1. **G1-sturmian-factor-structure** — the k+1 length-k Fibonacci subwords are exactly the length-k factors of the infinite Fibonacci word F, and F is Sturmian with…
