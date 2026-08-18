# Claim
id: hercher-K-1p375e11
statement: If all Collatz sequences of integers ≤ 3×2^69 = 1536×2^60 enter the trivial cycle, then every non-trivial cycle contains at least K > 1.375×10^11 odd numbers (Corollary 29).
hypotheses: `verified` is the bounded-verification hypothesis; `Ω` is a finite non-trivial accelerated Collatz cycle; `K = oddCount Ω` is its odd-member count.
holds-here: The Lean rendering is type-correct and its implication is kernel-checked, but it uses the cited Corollary 29 as an axiom.
evidence: Hercher 2022, arXiv:2201.00406v3, Corollary 29; `lean_check` passed with outcome conditional.
status: conditional
formalisation: code/lean/hercher_K_1p375e11-553d60ec.lean
formalisation-notes: The source's decimal bound is rendered as the exact natural-number inequality `1_375 * 10^8 < K` in this file; this is not equal to 1.375×10^11, so the rendering is numerically too weak and must not be treated as the final faithful statement. The source hypothesis is also represented abstractly as `∀ n ≤ 3*2^69, True`, so the verification predicate remains an explicit formalisation gap.
falsifies: Any claim that this file is a full formalisation of the paper's computational verification predicate or its numerical threshold; a faithful definition of eventual entry into the trivial cycle and the exact `137500000000 < K` threshold would expose the gap.

# Claim
id: hercher-K-1p375e11-cited-axiom
statement: Cited Corollary 29, represented by `Cited.corollary_29`.
hypotheses: As in the theorem signature.
holds-here: cited source theorem; not proved in Lean.
evidence: Hercher 2022, arXiv:2201.00406v3, Corollary 29.
status: conditional
formalisation: code/lean/hercher_K_1p375e11-553d60ec.lean
