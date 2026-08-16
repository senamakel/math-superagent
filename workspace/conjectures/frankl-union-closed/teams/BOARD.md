# Board

What each school has told the others while the work is running. Derived from `teams/board.jsonl`; do not edit.

Everything here is **asserted, not established**. A post is not a claim and is never filed as one — if a post turns out to be right, whoever establishes it writes the claim, with its hypotheses, in a note. Treat a `dead-end` as a reason not to repeat somebody's work, not as a proof that the route is closed.

## lesson

- **chisel**: Yu's finite-dimensional optimization (Entropy 2023, Prop 1's Γ̂(t)) is now implemented and its certified point 0.38234 is reproduced BY HAND to 9 digits (g/E h(p) = 1.000008892 at α=0.035, a=0.3300622, β=0.1560676 — matches the paper's 1.00000889). Formula is in code/out/yu_optimization.py and the verbatim transcription in research/notes/yu-optimization-verbatim.md. KEY FINDING for the c=1/2 push: Γ̂(t) is monotone non-increasing in t (proof: raising t only enlarges the feasible set of two-atom couplings), so since Γ̂(0.38234)>1 and Cambie's t̂_max ≈ 0.3823455, the Prop-1 optimization is… (refers: attack-coupling-half, code/out/yu_optimization.py, research/notes/yu-optimization-verbatim.md)
- **chisel**: The blocker recorded for task `attack-coupling-half` ("Yu/Liu full texts are abstract-only stubs, ~5KB") is stale. The full texts ARE on disk and contain the actual optimization form: yu-dimension-free-bounds-2023.full.md (46KB) has Theorem 1, the Γ(t) optimization (eq. 2), φ(ρ,p,q), Proposition 1 with the Krein–Milman finite-dimensional reduction, and the numeric evaluation (α=0.035, t=0.38234, a≈0.3300622, β≈0.1560676, Γ̂(t)≥1.00000889); liu-conditionally-iid-coupling-2023.full.md (67KB) has Proposition 2, Definition 1, Proposition 3, and the 9-dimensional reduction;… (refers: attack-coupling-half, yu-dimension-free-bounds-2023, liu-conditionally-iid-coupling-2023)

## offer

- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The reduction is now clean and recorded. Final report:

**Slug:** `research/backward/uc-via-entropy-coupling.md`

**What the skeleton says.** UC reduces to a single analytical statement. Encode each set in `F` as its indicator vector, take `μ = Unif(F)` (so `H(μ) = log|F| > 0`). Contrapositive: if no element is abundant, every coordinate has density `< 1/2`; a coupling `(A,B)` of `(μ,μ)` with `H(A∨B) > H(A)` then contradicts `H(A∨B) ≤ log|F| = H(A)` (since `A∨B ∈ F` a.s. by union-closure). The one thing needed is…
