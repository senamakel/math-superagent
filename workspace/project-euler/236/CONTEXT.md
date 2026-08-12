# Shared context

What this run knows and on what basis. Nearly every role is sent this file on every model call, so it carries only what an agent would otherwise rebuild from disk: established results with their basis, dead ends and why, computed numbers, relevant durable memory. Budget 10,000 tokens; a statement worth less than a link to its source is not included. Durable findings belong in Cognee; detail belongs in the linked files.

## Established

**PE236 — Luxury Hampers: ANSWER = 123/59.** The largest rational m > 1 satisfying all six spoilage equalities is **m = 123/59 ≈ 2.0847**, established by THREE independent routes that agree: `code/brute.py` (naive oracle), `code/verify_oracle.py` (independent recomputation from a different base product + literal witness for every m), and `code/solution.py` (derived exact solver, all asserts pass). Literal six-equality Fraction check on the largest passes with explicit witness s=[413,1,1,30,10], t=[105,3,3,41,30]. Sourced: official statement `problem.md` at https://projecteuler.net/minimal=236; full derivation in `solution.md`.

**Setup.** a_i/b_i = counts supplied by A/B of product i; s_i/t_i = spoiled (1 ≤ s_i ≤ a_i, 1 ≤ t_i ≤ b_i). Six equalities: per product t_i/b_i = m·(s_i/a_i), and overall (Σs)/(ΣA) = m·(Σt)/(ΣB). Data:

| i | product | a_i | b_i |
|---|---------|-----|-----|
| 1 | Beluga Caviar | 5248 | 640 |
| 2 | Christmas Cake | 1312 | 1888 |
| 3 | Gammon Joint | 2624 | 3776 |
| 4 | Vintage Port | 5760 | 3776 |
| 5 | Champagne Truffles | 3936 | 5664 |

ΣA = 18880, ΣB = 15744.

**Oracle.** Exactly 35 valid m; smallest = **1476/1475** (the statement's worked example, reproduced); largest = **123/59**. Full sorted 35-value list embedded in `code/verify_oracle.py`, `code/theory_check.py`, `code/factor_analysis.py`. Agreement across brute.py (both base products), theory_check.py, verify_oracle.py checks A–C, and solution.py.

**Structural theorem (the governing fact, verified 0 mismatches vs direct enumeration on all 35 m by `code/theory_check.py`).** For reduced m = p/q, per-product condition forces s_i/t_i = A_i·q/(B_i·p), so (s_i,t_i) = k_i·(c_i,d_i) with c_i = A_i·q/g_i, d_i = B_i·p/g_i, g_i = gcd(A_i·q, B_i·p). Integer solution exists **iff g_i ≥ max(p,q)**, then 1 ≤ k_i ≤ K_i = g_i//max(p,q). Overall equality becomes the exact bounded 5-term subset-sum Σ k_i·w_i = 0, w_i = q·ΣB·c_i − p·ΣA·d_i. Candidates come from product 1: m = a_1·t/(b_1·s), O(a_1·b_1) fixed-input gcds; nothing scales with the answer bound. Shared machinery in `code/lib/pe236.py`.

**What bounds the answer.** Pattern work (`code/bound_tightness.py`) shows per-product gcd thresholds alone permit 596 reduced m > 123/59, so the answer is set by the OVERALL subset-sum condition, not per-product boxes.

## Ruled out

- **"All m built only from primes {2,3,5,41,59}" — FALSIFIED** by `code/factor_analysis.py` over all 35 values: primes 11, 17, 29 appear (e.g. 902/885 = 2·11·41/(3·5·59), 1230/1003 = 2·3·5·41/(17·59)). Any characterization must allow primes outside the ratio support.
- Enumerating spoilage counts up to supply sizes (naive bound-24000) is exponential in the data — wrong method; replaced by the gcd-threshold + subset-sum reduction.
- Nothing else has failed. Earlier draft claims (no code run, largest not near 1) are superseded by the verified oracle.

## Recalled (durable memory, Cognee)

- This run stored three durable memories, all source-backed by run code: (1) the oracle result 35 values / 1476/1475 smallest / 123/59 largest; (2) the gcd-threshold structural theorem; (3) the falsified prime-support conjecture.
- Pre-run long-term memory has nothing on PE236 or relative spoilage-ratio problems (only unrelated PE597/EG/NO4 hits).

## Missing

- **Literature pass not done.** `research/threads/theory-pass.md` opened the question whether standard theory (Farey/Stern-Brocot mediant structure, Diophantine linear systems, bounded subset-sum) contributes beyond the self-derived reduction; open request `farey-sequences-stern-7a1f` in `research/REQUESTS.md`. `research/sources/` is empty. This bears on the method's framing, NOT on the correctness of 123/59 (already triple-verified). Compare any source's hypotheses against this problem before importing.
- **`research/CLAIMS.md` is empty**: the structural theorem is a verified result but no claim block has been written into a research note yet.

## Contradictions

- None. brute.py (both base products), theory_check.py, verify_oracle.py checks A–C, solution.py, and the statement's own oracle all agree on 35 / 1476/1475 / 123/59.

## Pointers

- Full derivation: `solution.md`. Shared solver machinery: `code/lib/pe236.py`. File purposes: `code/INDEX.md`. Task checklist: `TASKS.md` (all three complete).
