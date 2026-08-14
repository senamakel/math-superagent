# Bentley & Yao, "An Almost Optimal Algorithm for Unbounded Searching"

**Source:** Information Processing Letters 5(3) (1976) 82–87, DOI 10.1016/0020-0190(76)90071-5. Full text on disk: `research/sources/bentley-yao-unbounded-searching.full.md` (a PDF-to-text conversion; the OCR is noisy — read this summary for the clean statements, open the full text only to quote the paper itself).

## Problem it formalizes

Unbounded searching: F : N⁺ → {X, Y} with F(j) = X for j < n and F(j) = Y for j ≥ n, where n is a fixed but **unbounded** integer; cost = number of evaluations of F. Isomorphic to looking up a fixed z in an infinite ordered table S₁, S₂, … using only "is Sᵢ < z?" queries.

## Results (algorithms B₀, B₁, B₂, …, B_k, U and a lower bound)

- **B₀ (linear/unary search):** test F(1), F(2), … until F(n) = Y; cost n. This is the naive method the run must not use.
- **B₁ (doubling probe + bounded binary search):** stage 1 evaluates F(2^i − 1) for i = 1, 2, … until F(2^m − 1) = Y, where m = ⌊lg n⌋ + 1 (m evaluations); stage 2 runs ordinary binary search on the 2^m − 1 candidates (⌊lg n⌋ evaluations). Total **C_B₁(n) = 2⌊lg n⌋ + 1**.
- **B₂:** replace the unary stage of B₁ by B₁ itself (find m by binary search over the doubling probes); C_B₂(n) = ⌊lg n⌋ + 2⌊lg(⌊lg n⌋ + 1)⌋ + 1.
- **B_k (k-nested):** nest k times; C_Bk(n) = Σ_{1≤i<k} L^i(n) + L^k(n) + 1, where L¹(n) = ⌊lg n⌋ and L^{i+1}(n) = ⌊lg L^i(n)⌋ + 1.
- **U (ultimate algorithm):** pick k = L*(n) = the least j with g(j) ≥ n, where g(0) = 2 and g(j+1) = 2^{g(j)} + 1 (a tower-of-twos recursion); stage 1 finds k by probing F(g(0)), F(g(1)), …, stage 2 runs B_k. Cost C_U(n) = 4 + L*(n) + Σ_{1≤i<L*(n)−1} L^i(n) — within O(1) + lg* n of the information floor.
- **Lower bound (Theorem A):** every unbounded-search algorithm induces a prefix code of the integers, so Kraft's inequality applies; for infinitely many n any algorithm's cost exceeds lg n + lg⁽²⁾ n + ⋯ + lg^(K(n)) n − 2 lg* n. Hence no algorithm costs lg n + lg⁽²⁾ n + ⋯ for all n; B₁'s 2⌊lg n⌋ + 1 is not optimal, and U is very nearly optimal (F. Chung & R. L. Graham sharpened the bound, also reported in the paper).

## Why this run needs it

Khovanova & Marton's §7 search for the a≥(d) sequences uses "a variation of unbounded binary search [Bentley–Yao]" whose safeleft range doubles when the right end still satisfies f_d(x+p) < x and halves otherwise. Bentley–Yao is the classical citation justifying that such doubling/halving probe schedules are within a small constant of the optimal number of evaluations. In PE156 the search domain is bounded by d·10^10 (Prop 9.1), so the run's jump iterator (gap G3) never actually searches an unbounded domain — but it mirrors the same doubling/halving rationale, and in the full-size run it needed only 5,932–29,409 f-evaluations per digit (86,649 total across d = 1..9, `code/out/solution-run.log`) to find all 661 fixed points over [0, d·10^10]. This source is the efficiency justification, not a correctness input: completeness rests on the bound (G2) plus the skip rules (G3).

Claim ledger entry: `bentley-yao-unbounded-search` (see `research/notes/bentley-yao-unbounded-searching.md`).