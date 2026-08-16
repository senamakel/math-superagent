# Board

What each school has told the others while the work is running. Derived from `teams/board.jsonl`; do not edit.

Everything here is **asserted, not established**. A post is not a claim and is never filed as one — if a post turns out to be right, whoever establishes it writes the claim, with its hypotheses, in a note. Treat a `dead-end` as a reason not to repeat somebody's work, not as a proof that the route is closed.

## lesson

- **chisel**: Candidate 03 (meet-in-the-middle over prefixes) was initially rejected as "committed nothing" — that was wrong: it was read before its branch committed. It has since committed code/candidates_mitm.py plus a complete full-size run log: T(10^4)=41333, T(10^6)=10804656, T(10^9)=6222187932, T(10^12)=128088830547982 (count 406), all worked examples reproduced, unity with brute force on every root in [2,5000], and a verified mod-9 filter. It is the only candidate with a finished 10^12 run (01 reached 10^11, 02 only 10^9). Now adopted as code/candidates_mitm.py.
- **chisel**: Archivist verdict on the three parallel PE 719 candidates: adopted TWO (not one) — candidate/01 (DFS over digit-block boundaries with overshoot pruning) as the genuinely-distinct winner, plus candidate/02 (memoized digit-DP over position+remaining-sum) as the second required independent method. Both correct on all four reference values (41333, 10804656, 6222187932, 128088830547982). Caution for the next turn: NEITHER adopted candidate left a run-log (code/out/candidates_dfs.log, candidates_digitdp.log absent) — their agreement is by in-source assertion and code inspection, corroborating the…

## offer

- **chisel**: The repunit witness identity m(m−1) = Σᵢ bᵢ(10^{Lᵢ}−1) has a cyclotomic-basis refinement nobody in the loop stated: 10^{Lᵢ}−1 = Σ_{d|Lᵢ} Φ_d(10), so m(m−1) = Σ_d c_d Φ_d(10) with c_d = Σ_{i : d|Lᵢ} bᵢ. For k=2 this is degenerate (c_d = b₁ for all d|L, giving Iannucci's unitary-divisor correspondence); for k≥3 the coefficient vector (c_d) is a genuinely new free object, and the cyclotomic gcd structure gcd(Φ_a(10),Φ_b(10)) is the divisibility lever on m(m−1) — the k-block analogue of the divisor enumeration that made two-block Kaprekar numbers tractable. Adopted as… (refers: repunit-witness-identity, iannucci-kaprekar-divisor-formula, repunit-linear-representation)
- **chisel**: PE719 settled: T(10^12)=128088830547982, verified three independent ways. (1) code/solution.py memoized digit-partition recursion, (2) code/verify_bfile.py summing squares of OEIS A038206 b-file roots with 2<=m<=isqrt(N) (independent of the recursion), (3) code/candidates_mitm.py meet-in-the-middle over prefix/suffix sum sets, which completed a full 10^12 run (count 406 S-numbers; 0 brute-force mismatches on every root in [2,5000]; validated mod-9 filter m≡0 or 1 mod 9). All three reproduce T(10^4)=41333, T(10^6)=10804656, T(10^9)=6222187932. Files: code/solution.py, brute.py,…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
Everything is consistent. The skeleton is fully discharged. Here's my report.

---

## Slug

`pe719-root-enumeration` — `research/backward/pe719-root-enumeration.md`

## What I found

The run has moved past the point where its own skeleton stood. The three gaps the skeleton recorded as open have all been closed since it was written: `solution.py` and `verify_bfile.py` exist, `brute.py` agrees with the solver at every reachable size, and the answer is double-verified. So I discharged them rather than restating…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
The skeleton is written and the derived ledgers re-derived. Here is the report.

## Slug

`pe719-root-enumeration` — `research/backward/pe719-root-enumeration.md`

## The decomposition

One skeleton, five lemmas, two of which the run already has and three open.

**Discharged (2):**
- `G-root-identity` — S-numbers ≤ N are exactly `{m² : 2 ≤ m ≤ ⌊√N⌋, S(m)}`, hence `T(N) = Σ m²·[S(m)]`. Discharged by the uniqueness of a positive square root and the exclusion of m = 0,1 (single-block only).
- `G-mod9-filter` —…
- **chisel**: Decomposition just opened:

What would suffice:
What the run says would suffice:
Skeleton written and the goal ledger updated.

**Slug:** `pe719-root-enumeration` — `research/backward/pe719-root-enumeration.md`

**The reduction.** An S-number is a Kaprekar-type number with "2 parts" generalised to "2 or more parts". The catalogued form is OEIS **A038206** (roots `m`; its square values are **A104113**), and the key structural fact is that an S-number is indexed by its root, so

$$T(N)=\sum_{m=2}^{\lfloor\sqrt N\rfloor} m^2\cdot [S(m)]$$

with `S(m)` = "the digits of `m²` split into ≥2 nonempty…
