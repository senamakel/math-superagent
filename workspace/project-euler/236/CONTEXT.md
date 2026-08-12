# Shared context

What this run knows and on what basis. Nearly every role is sent this file on every model call, so it carries only what an agent would otherwise rebuild from disk: established results with their basis, dead ends and why, computed numbers, relevant durable memory. Budget 10,000 tokens; a statement worth less than a link to its source is not included. Durable findings belong in Cognee; detail belongs in the linked files.

## Established

**PE236 — Luxury Hampers (sourced: `problem.md`, official statement at https://projecteuler.net/minimal=236).** a_i = count supplied by A of product i, b_i = count for B, s_i/t_i = respective spoiled counts; all integers with 1 ≤ s_i ≤ a_i, 1 ≤ t_i ≤ b_i. The single rational m > 1 satisfies, for all five products i: t_i/b_i = m·(s_i/a_i) (B's per-product rate worse by m), and overall: (Σs)/(ΣA) = m·(Σt)/(ΣB) (A's overall rate worse by the same m). Statement's worked oracle: 35 values of m exist; smallest = **1476/1475**; answer = the largest, reduced u/v.

**Definition reading CONFIRMED (basis: `code/brute.py` run + `code/verify_oracle.py`; see code/INDEX.md).** The six equalities above with s_i/t_i = (a_i/b_i)/m per product reproduce count 35 and smallest 1476/1475, so the earlier "direction flip" uncertainty in this file is resolved. Supply data (gcds hand-verified):

| i | product | a_i | b_i |
|---|---------|-----|-----|
| 1 | Beluga Caviar | 5248 | 640 |
| 2 | Christmas Cake | 1312 | 1888 |
| 3 | Gammon Joint | 2624 | 3776 |
| 4 | Vintage Port | 5760 | 3776 |
| 5 | Champagne Truffles | 3936 | 5664 |

**Numbers structure (arithmetic hand-verified):** ΣA = 18880 = 2^6·5·59, ΣB = 15744 = 2^7·3·41, gcd 64 → ΣA/ΣB = **295/246**. Scaling by 32: A = 32·(164,41,82,180,123), B = 32·(20,59,118,118,177). Reduced per-product ratios R_i = a_i/b_i: **41/5, 41/59, 41/59, 90/59, 41/59** — primes {2,3,5,41,59} suffice for the ratios.

**ORACLE COMPUTED — exactly 35 valid m; SMALLEST = 1476/1475 ≈ 1.0007; LARGEST = 123/59 ≈ 2.0847.** The full sorted 35-value list is embedded (identical, curator re-counted 35) in `code/verify_oracle.py`, `code/theory_check.py`, `code/factor_analysis.py`. Agreement by independent routes: `brute.py` (base product = Christmas Cake, fewest (s,t) pairs) and `verify_oracle.py` check B (base product = Beluga Caviar) return the same set; check A builds explicit spoilage witnesses (s_i,t_i) for all 35 and verifies all six equalities literally with Fraction arithmetic; check C re-confirms smallest/largest. Reference factorizations (hand-checked): 1476 = 2²·3²·41, 1475 = 5²·59, 123 = 3·41, 1003 = 17·59, 885 = 3·5·59, 1711 = 29·59.

**Structural theorem — verified by `code/theory_check.py`, 0 mismatches vs direct enumeration on all 35 m (basis: code file, its own docstring).** For reduced m = p/q, per-product condition forces s_i/t_i = A_i·q/(B_i·p), so (s_i,t_i) = k_i·(c_i,d_i) with c_i = A_i·q/g_i, d_i = B_i·p/g_i, g_i = gcd(A_i·q, B_i·p). An integer solution exists **iff g_i ≥ max(p,q)**, and then 1 ≤ k_i ≤ K_i = g_i // max(p,q). The overall equality becomes the exact bounded 5-term condition Σ k_i·w_i = 0, w_i = q·ΣB·c_i − p·ΣA·d_i (subset-sum over each k_i ∈ [1,K_i]). This reduction is the engine of brute.py, theory_check.py, verify_oracle.py.

## Ruled out

- **"All m are built only from prime powers of the reduced-ratio primes {2,3,5,41,59}" — FALSIFIED** by the computed list (`code/factor_analysis.py` over all 35 values). Counter-examples in the list: 902/885 = 2·11·41/(3·5·59), 1230/1003 = 2·3·5·41/(17·59), 3321/3245 = 3⁴·41/(5·11·59), 2460/1711 = 2²·3·5·41/(29·59) — primes 11, 17, 29 appear. Any derived method must not assume prime support confined to {2,3,5,41,59}.
- Nothing else has failed. Earlier draft claims here ("no code run yet", "largest not near 1 — do not assume") are superseded by the computed oracle above, not merely supplemented.

## Recalled

- Pre-run durable memory (recalled 2026-04-25): nothing on PE236 or relative-ratio problems; all hits were PE597/EG/NO4 and unrelated. A PE597 failed cell ("never use speed-order enumeration") does not bear on this problem's shape.
- This run has stored three durable memories in Cognee (source: the code files, this cycle): the oracle result (35 values, 1476/1475 smallest, 123/59 largest), the gcd-threshold structural theorem, and the falsified prime-support conjecture. Scratch holds only the earlier hand-gcd ratio analysis (session s18cb19a9a83edc64-1) — consistent with, and superseded by, the verified computation.
- Do not search for a published PE236 answer; that invalidates the run.

## Gaps

- **`code/solution.py` (derived, exact, full-size method) does not exist yet; TASKS.md is still a stub.** The oracle routes enumerate all (s,t) pairs of one base product (Christmas Cake: 2,477,056 pairs) — correct as oracle, wrong at scale per method policy. A method whose cost grows with a_i·b_i is prohibited; the intended crux is a structural characterization of the valid m using the gcd-threshold form g_i ≥ max(p,q) (a divisibility filter on candidates), not pair enumeration.
- Completion criteria unmet only at the last step: brute.py reproduces the oracle; solution.py must agree with it and produce the largest at full size. **Largest = 123/59 so far rests on the two oracle routes only** (brute.py; verify_oracle.py checks A–C); solution.py agreement is the required third route before reporting.
- `research/CLAIMS.md` is empty: the structural theorem is a verified result but no claim block has been written into a research note yet.

## Contradictions

- None recorded: brute.py (both base products), theory_check.py, verify_oracle.py checks A–C, and the statement's own two examples all agree.