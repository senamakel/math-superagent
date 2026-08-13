# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. It carries what an agent would otherwise rebuild from disk.

It has a token budget (`MATH_AGENT_CONTEXT_TOKENS`, 10,000). Link the file that
still holds detail compressed away. The problem, its objective and the
criterion that ends the run are in `GOAL.md`; `research/ROOT.md` states the
structure of the object, the naive-count obstruction, and what the sources
establish.

## Established

**The modular sieve is exactly `|A_k| = 2^(k-1)` and therefore can never close.**
*(proved unconditionally — three-lemma argument, claim `ternary-lifting-theorem`;
numerically checked k = 1..26 — this is the run's main negative result and one of
the stated deliverable options.)*
- The three-lemma proof is in `code/out/lifting_theorem.md`: (1)
  `2^(2·3^(k-2))` has order 3 mod 3^k, so equals `1 + c·3^(k-1)` with `3 ∤ c`
  (c=1 checked k=2..15); (2) the three lifts `r + j·2·3^(k-2)` agree mod
  3^(k-1) so share their low k−1 digits; (3) the k-th digit is
  `d + v·j·c mod 3`, an affine bijection of Z/3 since 3 divides neither v
  (a power of 2) nor c — so the three top digits are 0,1,2 and exactly one
  lift dies, two survive. Hence `|A_k| = 2|A_{k-1}|`, `|A_1| = 1`,
  `|A_k| = 2^(k-1)` for **all** k. Supersedes `ternary-sieve-count-doubles`
  (which asserted it only to k=22).
- **Stop sieving**: `sieve_structure.py` enumerating `A_k` explicitly is data
  no longer needed; the count is a theorem, not a table.
- So density `|A_k|/(2·3^(k-1)) = (1/2)(2/3)^(k-1) → 0` while **the count
  doubles each level**. Narkiewicz's `O(x^{log_3 2})` bound matches this up to
  constant and gives no path information. **Conclusion: no obstruction modulo
  any power of 3 can prove the Erdős conjecture at any finite 3-adic
  precision.**
- The three witnesses `n = 0, 2, 8` survive in `A_k` at every level checked; the
  negation of "the sieve closes" is not a forbidden-witness overreach.

**Reformulation (proved-here, `research/threads/sieve-dynamics.md`):** the
closure of `{2^n : n ∈ Z}` in `Z_3^×` is all of `Z_3^×` (4 topologically
generates `1+3Z_3`, LTE `ord(4 mod 3^k) = 3^(k-1)`; 2 ≡ −1 mod 3). The conjecture
is exactly: **the dense orbit `{2^n}` meets the 3-adic Cantor set `Σ_{0,1}`
(digits all in {0,1}) in exactly {1, 4, 256}.** Dimension arguments on the
closure cannot decide this; only the arithmetic of `n ↦ 2^n`. This is why every
existing method stalls.

**What the sources settle** (each with basis in `research/CLAIMS.md`):
- **Saye verification bound** (asserted-by-source, arXiv:2202.13256): no new
  solution for `n ≤ 2·3^45 ≈ 5.9×10^21`, covering both the digit-2 (Erdős) and
  digit-0 (Sloane) conjectures. History: Gupta 1978 `n < 4374`, Vardi `≤ 2·3^20`.
- **Dimitrov–Howe** (proved): any counterexample beyond {0,2,8} has **≥ 26 ones**
  in its ternary expansion; sparse case fully settled.
- **Narkiewicz / Lagarias** (LAG-2 proved, LAG-1 asserted): for every nonzero
  λ ∈ Z_3, `#{n ≤ X : (λ2^n)_3 omits digit 2} ≤ 2 X^{log_3 2}`. Count bound only,
  no existence content.

## Ruled out

- **The modular / 3-adic sieve cannot close.** `|A_k| = 2^(k-1)` proves it:
  the count grows forever, so "the sieve empties at finite k" is false by
  bijection. This is the p-adic dead end for this problem, closed for good. Any
  new approach must attack **which paths survive to infinity**, never the count.
- **Density and digit-independence heuristics** are true and irrelevant: they
  concern all integers avoiding digit 2 (density → 0) or give `(2/3)^k`, and
  never reach the thin orbit `2^n`. Never cite as proof. (In `GOAL.md` as the
  trap; recorded as heuristic only.)
- *Operational note for later cycles:* the first phase-4 "solve" attempt
  (launched the `goals` agent) died at spawn with an empty API response — an
  infrastructure failure, not a mathematical one. Nothing mathematical followed
  from it. `research/approaches/` holds closed directions if any agent opens one.

## Numbers

- `|A_k| = 2^(k-1)` **exactly** for `k = 1..26` (lifting, checked against full
  sieve for k ≤ 8; `code/out/sieve_lift.captured.txt`, `sieve_structure`). The
  count is a theorem, not a trend.
- Surviving classes at k=8 (and full lists k=1..8) in `code/out/sieve_structure.captured.txt`; the witnesses 0,2,8 stay in `A_k` at every level.
- Verification bound `n ≤ 2·3^45 ≈ 5.9×10^21` (Saye, asserted).
- **Compute cost fact:** sieving by materialising `A_k` as a set cost `k=26` → 333s and 2.1 GiB. **Do not re-sieve that way** — use the 2-to-1 lifting (or Saye's Θ(2^K) recursion) instead; the lifting/machine check up to k=26 is already done. (`research/threads/lifting-proof.md`)

## Recalled (durable memory from earlier runs — corroborates, not this run's own)

- Order of 2 mod 3^k is `2·3^(k-1)` = `φ(3^k)`; the digit rule
  `d_{k+1}(2^(i·u_k+j)) ≡ d_{k+1}(2^j) + i·d_1(2^j) (mod 3)` gives the recursive
  sieve in Θ(2^K) not Θ(3^K) (Saye). (`recall_memory`)
- Conjecture graph nodes: Erdős ternary-2n (open), Sloane ternary-0, the
  interchangeable "dense-orbit vs Cantor set" framing threads through
  Lagarias et al. (`relate_memory`)

## Contradictions

- None active. Narkiewicz's `1.62 X^{log_3 2}` (EP-406, asserted) vs LAG-2's
  `2 X^{log_3 2}` (proved) differ in constant; both have exponent `log_3 2 < 1`
  and neither contradicts the exact `2^(k-1)` sieve count. The primary Narkiewicz
  source (constant/method) is still missing from the library.

## Gaps

- **The real open question:** which of the `2^(k-1)` infinite survival paths
  are actually realised as `2^n` for an integer n? The constructor
  (order/digit-splitting) proves every path exists at every finite level
  (mod 3^k); the missing piece is the **middle/high-digit coupling** that makes
  only {0,2,8} extend to a genuine integer exponent. A transfer operator or
  recursion on *paths*, not counts, is the suggested next line.
- Narkiewicz (1980) primary source not in library (constant and original method
  unverified). Dupuy–Weirich, Gupta 1978, Abram–Lagarias also absent. See
  `research/REQUESTS.md`.
- The LTE lifting proof of the 2-to-1 map has a carry step not automatic; the
  bijection proof supersedes it, so the LTE route is kept only as a check.
