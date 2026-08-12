# Shared context

What this run knows and on what basis. Nearly every role is sent this file on every model call, so it carries only what an agent would otherwise rebuild from disk: established results with their basis, dead ends and why, computed numbers, relevant durable memory. Budget 10,000 tokens; a statement worth less than a link to its source is not included. Durable findings belong in Cognee; detail belongs in the linked files.

## Established

**PE236 — Luxury Hampers (sourced: `problem.md`, official Project Euler statement).** Let a_i = count supplied by A of product i, b_i = count for B, s_i/t_i = respective spoiled counts. The single ratio m satisfies, for all five products i: s_i/a_i = m·(t_i/b_i), and overall: (Σs_i)/(Σa_i) = m·(Σt_i)/(Σb_i), with m > 1 rational. All counts are integers; m determined by the smallest positive integers (s_i, t_i) consistent with the first five equalities. Supply data (computed, hand-checked):

| i | product | a_i | b_i |
|---|---------|-----|-----|
| 1 | Beluga Caviar | 5248 | 640 |
| 2 | Christmas Cake | 1312 | 1888 |
| 3 | Gammon Joint | 2624 | 3776 |
| 4 | Vintage Port | 5760 | 3776 |
| 5 | Champagne Truffles | 3936 | 5664 |

**Numbers structure (computed + hand-checked):**
- ΣA = 18880 = 2^6·5·59, ΣB = 15744 = 2^7·3·41, gcd = 64 → ΣA/ΣB in lowest terms = **295/246**.
- Reducing all a_i, b_i by 32: A = 32·(164,41,82,180,123), B = 32·(20,59,118,118,177).
- Per-product ratios R_i = a_i/b_i reduce to: 41/5, 41/59, 41/59, 90/59, 41/59. Prime factors of the five reduced ratios are within {2,3,5,41,59}.
- Worked examples from the statement (the oracle): 35 values of m exist; smallest = **1476/1475**; answer = largest, a reduced fraction u/v.

**Problem shape (correct reduction, tentative — must be confirmed by `code/brute.py`):** per-product condition is B worse than A by factor m: t_i/b_i = m·(s_i/a_i), i.e. **s_i/t_i = R_i/m** for each i, with bounds 1 ≤ s_i ≤ a_i, 1 ≤ t_i ≤ b_i. NOTE THE DIRECTION FLIP (the paradox): per product B is worse by m, so (Σt)/(Σb) = m·(Σs)/(Σa) holds ONLY per product i.e. t_i/b_i = m·(s_i/a_i); overall A is worse by m, i.e. (Σs)/(Σa) = m·(Σt)/(Σb) ⟺ rate_B overall = rate_A / m. This matches GOAL.md and the statement; earlier text here had the overall direction flipped. For a candidate m = p/q, per product we need s_i/t_i = (a_i·q)/(b_i·p); feasibility per product needs the reduced numerator ≤ a_i and reduced denominator ≤ b_i (with the reduced fraction = (a_i·q)/(b_i·p)/gcd(a_i·q, b_i·p) times a common scale). The global constraint then couples the products. All 35 m fall between 1476/1475 and the largest; the largest is NOT known to be near 1 — do not assume a magnitude. Verify the final m against all six equalities exactly before reporting.

## Ruled out

_Nothing failed yet — this run has not yet executed any code._

## Recalled

Durable memory holds **nothing** on PE236 or on luxury-hamper/relative-prime-power-ratio problems (recalled 2026-04-25; all hits are from runs on PE597, EG conjecture, PE761 — unrelated). A failed cell from run PE597 is context only: "never use speed-order enumeration" — irrelevant to this problem's shape. Do not search the web for a published PE236 answer; that invalidates the run. `request_research` is available for named-theorem gaps (a likely one, if needed: "relative prime power fractions" / the structure of m = product of per-product reduced-ratio prime powers).

## Gaps

- No code has been run yet. Need: `code/brute.py` naive oracle (enumerates small s,t per product, computes all valid m by the exact six equalities, reproduces 1476/1475 and the count 35) — this validates the reading of the definition, then `code/solution.py` derived method at full size. Until the oracle reproduces 1476/1475 and 35, everything above on "numbers structure" is arithmetic without machine confirmation.
- Open question for the derived method: exact structural characterization of all m (the 35) and a proof that the largest can be found without enumerating candidate m or spoilage counts up to any large bound. Candidate structure (conjectured, not yet proved): m's numerator/denominator are built from the prime powers of the five reduced ratios 41/5, 41/59, 90/59; candidates are all 2^a·3^b·5^c·41^d·59^e·(...) with numerator > denominator, checked against the linear constraint. This is the intended PE236 crux; do not brute force it.

## Contradictions

_None recorded — no independent sources or computations disagree yet._