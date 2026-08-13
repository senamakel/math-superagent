# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. So what is here is what the run knows without going to look, and
what is missing is what each agent rediscovers separately.

It has a token budget (`MATH_AGENT_CONTEXT_TOKENS`, 10,000 default). The file is
re-sent on every model call in every role that reads it, so length here is a
bill the whole run pays many times over. Link the file that still holds any
detail compressed away. Durable findings belong in Cognee. A statement nobody
can trace to a source is worth less than no statement.

## Established

Every claim marked with its evidence class; all anchors are in this workspace.

- **(proved) No odd unitary perfect number.** Every UP `n = 2^a·m`, `a ≥ 1`.
  Proof is three lines (v2 argument) in `research/notes/parity-and-2-adic-budget.md`.
  Subbarao–Warren 1966.
- **(proved, checked against all five) 2-adic budget identity**:
  `Σ_i v2(p_i^{e_i}+1) = a + 1`, exactly, for `n = 2^a Π p_i^{e_i}` UP with `p_i`
  odd distinct. Corollary `ω(odd part) ≤ a + 1`, with equality iff every odd
  component `≡ 1 (mod 4)`. This is the elementary form of the paper's
  "2-adic budget overshoot" filter. It bounds `ω` *above*; the open useful
  direction is a **lower** bound on `a` in terms of `ω`, or impossibility of a
  residue class of `a`. `research/notes/parity-and-2-adic-budget.md`.
- **(computed/checked) Witness set = the five known numbers**, verified by the
  exact-integer oracle `σ*(n) == 2n` with negative controls (12, 28 false):
  `6, 60, 90, 87360, 146361946186458562560000` (last = `2^18·3·5^4·7·11·13·19·37·79·109·157·313`).
  `code/out/known_five_verified.captured.txt`.
- **(computed) All five are divisible by 3.** Whether a sixth must be is open.
  **Sharpest edge of the witness set:** the two non-squarefree kernels are
  `3^2` (in 90) and `5^4` (in the fifth). Any lemma killing repeated odd prime
  powers kills two of the five and is **false** — run every candidate lemma
  against all five before recording it as anything but `asserted`.
- **(sourced) Graham 1989:** unitary perfect numbers with squarefree odd part
  are exactly `6, 60, 87360`. So any sixth example has a **repeated odd prime
  power**.
- **(sourced, full text held)** Maciejewski arXiv:2605.20475 (May 2026):
  `research/sources/maciejewski-bounded-box-subbarao-warren.full.md` (93 KB,
  the definition of 3-Higgs confirmed at §1.1). Key proven statements, all
  with this paper as anchor: (1) Every prime divisor of a UPN is **3-Higgs**:
  `p-1` divides the cube of the product of smaller 3-Higgs primes, exponent
  cap 3 (OEIS A057447). (2) The odd dependency graph: edges `p → r` when
  `r | p^e + 1` for admissible e; source SCCs; within the box
  `B = {p ≤ 2000, e ≤ 6, p^e ≤ 10^9, |SCC| ≤ 6, cycle ≤ 6}` the only admissible
  source kernels are `3^2`, `5^4` and five impostors. (3) Proposition 5:
  `H_even ⊆ {m ≡ 2 (mod 4)}`. Finiteness *reduces* to the prime case
  `m = 2p` (Theorem 7); composite members exist (k=9, k=15 are verified
  members of H_even per `heven_complete_verify`) and are inherited from
  unresolved prime divisors via Proposition 4(3).
  `m = 2k ∈ H_even`, `k` odd, every prime factor of `k` is 3-Higgs with
  `v_q(k) ≤ 3`, and `2d ∈ H_even` for every odd `d | k`. (5) Theorem 7
  (prime-case reduction): `|H_even| < ∞` iff `|{m = 2p : p odd prime,
  2p ∈ H_even}| < ∞`, with `|H_even| ≤ 4^|H_even^prime|`. (6) Theorem 8:
  `H_even ∩ [2,1200] = {2,6,10,18,26,30,46,62,82,122}`. (7) Theorem 21:
  `#{m ≤ X : m ∈ H} << X^(1-η)` and `Σ 1/m < ∞` — **thinness, not
  finiteness**; the gap is exponential at the primitive-divisor height.
  (8) Frontier: `|H_even ∩ [2,40000]| ≤ 201`, `|H_even ∩ [2,50000]| ≤ 272`,
  rigorous, with explicit candidate lists (Theorems 9–19 + Lemma 20 APR-CL
  closures). Analytic target: divisor-level problem for `Φ_{4p}(2)`, the
  Aurifeuillean split `2^(2p)+1 = L_p·M_p` with `L_p = 2^p − 2^((p+1)/2) + 1`,
  `M_p = 2^p + 2^((p+1)/2) + 1`. All details in
  `research/notes/heven-and-3-higgs-structure.md`.
- **(sourced, unverified) Frei 1978 (via OEIS A002827 comment only):** a UPN not
  divisible by 3 has `2^m | n` with `m ≥ 144`, ≥ 144 distinct odd prime
  factors, and `n > 10^440`. The two bogus TOC-page files previously filed
  under Frei's name were deleted per directive (tombstones at
  `research/sources/frei-1978-unitar-perfekte-zahlen*.full.md`). Primary
  text not yet in the library; the OEIS-sourced theorem is unverified.
- **(computed/checked) Lower bound on `a`:** any sixth UPN has
  `a ≥ ω(odd) − 1 ≥ 8`, so `2^8 | n`. Wall (1988) (≥ 9 odd components for a
  new example) + budget corollary. Equality `a = 8` forces 9 odd components,
  all `≡ 1 (mod 4)` — a rigid candidate class.
  `research/notes/lower-bound-on-a.md`, `code/out/wall1988_budget_lower_bound.captured.txt`.
- **Equality case `a = 8` was eliminated** (`research/notes/equality-case-eliminated.md`,
  `code/out/equality_case_elimination.captured.txt`). The equality case
  `ω(odd) = a + 1` requires `Π(1+1/q_i) = 2^{a+1}/(2^a+1)`, maximised over
  smallest admissible sizes. For `2 ≤ a ≤ 28` the maximum falls short; `a = 8`
  is dead (257 prime forces 257 as component, deficit 0.297). The bound is
  attained with equality at `a = 1` (n = 90). Undecided beyond `a = 28`. So any
  sixth example in the equality case has `a ≥ 29`. **Over-read correctly:** this
  does NOT give any sixth with exactly 9 odd components `a ≥ 29` — with `ω(odd)
  = 9` and `a ≥ 9` the example is not in the equality case (needs `a+1 = ω`),
  so only `a = 8` is excluded there; correct bound for `ω = 9` is `a ≥ 9`. The
  fifth example shows `ω < a+1` is normal (ω=11, a+1=19); the lemma bites only
  at the exact extremum. Thread `a-ge-8-bound` superseded by this result.
- **(OEIS finding)** The verified H_even members `2,6,10,18,26,30,46,62,82,122`
  match **no** OEIS sequence — no catalogued closed form; structure comes from
  the problem.
- **(computed/checked, independent reproduction)** The ten members of
  `H_even ∩ [2,1200]` are each verified IN by **complete factorisation** of
  `2^m+1` with every prime 3-Higgs:
  `code/out/heven_complete_verify.captured.txt` — 2^122+1 factored completely into
  `5·733·1709·3456749·368140581013·667055378149`, all 3-Higgs. So the ten
  members are independently confirmed (not merely taken from the paper).
- **(computed) 257 = 2^8+1 is non-3-Higgs** (`v2(256)=8 > 3`), confirmed by the
  witness check in `code/out/heven_patterns.captured.txt`. This underpins
  Route B to kill the `a=8` equality case in the thread. NB the pattern script's
  hard-coded "want" table had `257:True`; the computed (correct) value is False —
  that table row is a script bug, and the genuine value is non-Higgs.

## Ruled out

- **The structural backtracking search is CLOSED.** The product form
  `Π (q_i+1)/q_i = 2` with the denominator rule forcing the next prime whenever
  the remaining target is not an integer recovers exactly the five known numbers
  within any bound this container reaches and produces no information at any
  such bound — Wall (1975) cleared past `10^102`. Do not rerun it. The one thing
  worth keeping is the denominator rule as a **divisibility constraint** (if the
  remaining target is `A/B`, every prime dividing `B` divides `n`) — the
  structural content the odd dependency graph is built from; use it forwards, do
  not execute it. `research/notes/why-the-search-is-closed.md`,
  `code/structural_search_CLOSED.py`.
- **Rarity is not finiteness.** A density-zero / `o(x)` / `O(x^ε)` statement
  about UP numbers is almost certainly already known and does not touch the
  question. Say which one you have.
- **The B2 witness sieve's `pow(2,2400,r)==1` prefilter is buggy** — it must not
  be trusted for the H_even verification. A prime `r | 2^m+1` (m even ≤1200,
  m=2k) only needs `ord_r(2) = 2d` with `d | k` (i.e. `ord = 4d` with `d|k`),
  NOT `ord | 2400`. The oracle cross-check is decisive: direct witness pairs
  `(r≤1000, m even≤1200)` with `r|2^m+1` = **1346**, but the sieve's table
  (after the fix attempt) holds only 836, missing the `(29,14),(29,42),…` class:
  `ord_29(2)=28∤2400` yet `29 | 2^14+1`. So the filter wrongly discards valid
  witnesses and **under-kills** (it can only err toward claiming an m is IN when
  it is not — the dangerous direction). A corrected sieve must iterate odd
  divisors `d | m` / `d | 600` and test `pow(2, m, r)` directly for `r ≡ 1
  mod 2d`, not filter on `ord | 2400`. NOT CERTIFIED. See the D_COMP (576 odd-norm
  divisors) analysis in the commands log.

## Numbers

- Oracle: `σ*(n) = Π_{p^a||n}(p^a+1)`, exact integers; `n` UP iff `σ*(n) == 2n`.
  Verified by hand on 6 and on non-UP controls.
- Witness table (a, ω(odd), Σv2, a+1): 6→(1,1,2,2); 60→(2,2,3,3); 90→(1,2,2,2,
  equality); 87360→(6,4,7,7); fifth→(18,11,19,19). Identity exact in all five;
  equality in `ω ≤ a+1` holds only for 90.
- Paper's open branch (abstract): `|H_even ∩ [2,40000]| ≤ 201`,
  `|H_even ∩ [2,50000]| ≤ 272`, where `H_even = { even m : every prime divisor
  of 2^m+1 is 3-Higgs }`. Analytic target named in the paper: a divisor-level
  problem for the cyclotomic values `Φ_{4p}(2)`.

## Recalled

Durable Cognee memory now holds this problem's own accumulated findings, marked
as recalled rather than as fresh results; verify their hypotheses against this
problem before building on them (all checked here and consistent with the
Established section above).

- **ROOT construction** (recalled): any sixth UPN `n = 2^a·m` is even, has
  non-squarefree odd part (Graham), ≥9 odd components (Wall 1988), every prime
  divisor of the seed factor `2^a+1` is 3-Higgs, and its seed branch is
  controlled by `H_even`. Verification bound `|H_even ∩ [2,50000]| ≤ 272`
  rigorous with ~262 undecided candidates, all `m = 2p` with `p` odd Higgs,
  blocked by unfactored 355–6000 digit cofactors.
- **Settled restricted classes, with hypotheses** (recalled): no odd UPN
  (Subbarao–Warren), squarefree odd part `{6,60,87360}` (Graham), five impostor
  kernels eliminated for `1 ≤ a ≤ 10000` within the bounded box (Maciejewski
  Thm 2, three-filter certificate: Zsigmondy/Higgs-exponent, seed-divisor
  non-3-Higgs witness, 2-adic budget overshoot).
- **3-divisibility, Lemma 2** (recalled, from Subbarao–Warren): the structure
  of first-γ/3-divisibility underlies the seed description.
- **Library inventory** (recalled): 16 full texts held; the library is
  complete (phase-1 exit satisfied). Open gaps recorded in memory: Frei 1978
  primary, Wall 1975 primary, Goto 2007 primary, Wall's 10^102 search bound
  statement (also listed in Gaps below).

## Contradictions

- **Encyclopedia of Mathematics "Unitary divisor"** (fetched
  `research/sources/encyclopedia-of-math-unitary-divisor.full.md`) writes
  `90 = 2·3^3·5`. That is wrong: `90 = 2·3^2·5`, as in Subbarao–Warren 1966,
  OEIS A002827, Wikipedia, and the workspace oracle. The EoM entry has a
  typo in the exponent of 3. Do not cite EoM for the factorization of 90.

## Gaps

- **The full H_even ∩ [2,1200] exact classification (`code/H_EVEN_VERIFY_SPEC.md`,
  Phase B) is NOT complete.** The ten IN-members are independently confirmed by
  complete factorisation (`heven_complete_verify.captured.txt`), and the
  survivor/undecided split (how many even m ≤1200 are killed vs undecided) needs
  the **B2 witness sieve**, which is currently **buggy and not certified** (see
  Ruled out: the `ord | 2400` prefilter drops valid witnesses like 29|2^14+1).
  Until a corrected sieve passes the 1346-direct-pairs oracle equality and is
  wrapped in `timeout 540 … | tee`, the classification is not verified and the
  `H_even ∩ (122,1200] = ∅` claim rests on the paper alone, not on this run.
  The spec is the yardstick; Phase A (A1 sigma+budget, A2 Higgs primes, A3
  cyclotomic/Aurifeuillean/m=2426/Filter-N) must pass before Phase B, and only
  the ten IN-members have been reproduced so far.
- **Frei 1978 full text** (Über unitar perfekte Zahlen, Elem. Math. 33 (1978)
  95–96). The previous file at `research/sources/frei-1978-unitar-perfekte-zahlen.full.md`
  was a table-of-contents page (8 KB, "Über die Flächeninhalte ebener Schnitte
  konvexer Körper") — deleted and replaced with a tombstone. Correct e-periodica
  URL for Heft 4: `https://www.e-periodica.ch/digbib/view?pid=edm-001:1978:33#105`.
  The OEIS-recorded theorem (UPN not divisible by 3 has m ≥ 144, ω ≥ 144,
  n > 10^440) is load-bearing for the "is 3 | n forced?" question and is
  unverified against the primary text. Either refetch from the correct URL or
  find an alternate source.
- **Wall 1975 full text** (The fifth unitary perfect number, CMB 18 (1975)
  115–122) is paywalled at Cambridge. The fifth UPN's construction is carried
  by OEIS/Wikipedia/Wall 1987/1988/Maciejewski, but the primary proof of
  "W is the next after 87360" is not in the library.
- **Goto 2007** (Upper Bounds for UPNs, RMJM 37 (2007) 1557–1576) is
  paywalled at Project Euclid; the OEIS-recorded bound `m < 2^(2^k)` for
  `ω(m) = k` is carried but not verified against the primary text.
- Open structural question: is `3 | n` forced for a sixth example? (all five
  have it; open.) Both directions are a result.
