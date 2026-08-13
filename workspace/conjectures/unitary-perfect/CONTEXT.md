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

- **(computed/checked) Witness set = the five known numbers**, verified by the
  exact-integer oracle `σ*(n) == 2n` with negative controls (12, 28 false):
  `6, 60, 90, 87360, 146361946186458562560000` (last = `2^18·3·5^4·7·11·13·19·37·79·109·157·313`).
  `code/out/known_five_verified.captured.txt`. All five divisible by 3;
  whether a sixth must be is open. **Sharpest edge of the witness set:** the
  two non-squarefree odd kernels are `3^2` (in 90) and `5^4` (fifth). Any
  lemma killing all repeated odd prime powers is **false** — run every
  candidate lemma against all five before recording it as anything but
  `asserted`.
- **(proved) No odd unitary perfect number.** Every UPN `n = 2^a·m`, `a ≥ 1`.
  `research/notes/parity-and-2-adic-budget.md` (Subbarao–Warren 1966).
- **(proved, checked against all five) 2-adic budget identity**:
  `Σ_i v2(p_i^{e_i}+1) = a + 1`, exactly; corollary `ω(odd part) ≤ a + 1`,
  equality iff every odd component `≡ 1 (mod 4)`. Bounds `ω` *above*; the
  open useful direction is a **lower** bound on `a`. Same note. **Provenance
  (scholar-pass 2026-08):** the identity is SW 1966 Lemma 1 remark (3.6) and
  Wall 1975 p.116; this run's derivation is an independent complete proof, not
  a new result.
- **(computed / checked, this run) Equality-case bound: `ω(odd) = a+1` is
  impossible for `2 ≤ a ≤ 28`.** Verified from captured output
  `code/out/equality_case_elimination.captured.txt`: (1) a=1 max product = 4/3
  exactly, {5,9} is the odd part of 90; (2) 2^8+1=257 is prime, forced when
  a=8; (3) 9=3^2 and 49=7^2 are admissible, 3 and 7 are not; (4) exclusion
  runs 2 ≤ a ≤ 28, stops at 29. Claim `budget-equality-case-impossible` is
  `checked`. Thread `a-ge-8-bound` is closed. a=1 is realised by n=90.
  `research/notes/equality-case-eliminated.md`.
- **(sourced) Graham 1989:** UPNs with squarefree odd part are exactly
  `6, 60, 87360` — so any sixth example has a **repeated odd prime power**.
  The summary is corrected (scholar-pass): previous "Digest only" banner was a
  template bug; file now carries the theorem and method (Mersenne-prime
  chains, `p_{i+1} ≥ 2p_i − 1` geometric growth).
- **(sourced) Subbarao–Warren 1966:** for each fixed `ω`, at most finitely
  many UPNs (Theorem 4); `m = 8,9,10` are **not** excluded in 1966 (that is
  Subbarao 1970).
- **(sourced, full text held) Maciejewski arXiv:2605.20475** (May 2026; 3-Higgs
  definition confirmed §1.1; OEIS A057447). Cardinal facts — anchor
  `research/notes/paper-extraction.md` (verified verbatim, scholar-pass 2026-08):
  - Every prime divisor of a UPN is **3-Higgs**: `p−1 | (product of smaller
    3-Higgs primes)^3`, exponent cap 3 (17 first non-Higgs, `v2(16)=4`).
  - Odd dependency graph, edges `p → r` when `r | p^e + 1`; inside the bounded
    box `B = {p ≤ 2000, e ≤ 6, p^e ≤ 10^9, |SCC| ≤ 6, cycle ≤ 6}` the only
    admissible source kernels are `3^2`, `5^4` and five impostor kernels,
    eliminated for `1 ≤ a ≤ 10000` (Thm 2; three filters: Zsigmondy/Higgs-
    exponent, seed-divisor non-3-Higgs witness, 2-adic-budget overshoot).
  - Prop 5: `H_even ⊆ {m ≡ 2 (mod 4)}`. Prop 4(3): for `m = 2k ∈ H_even`,
    k odd, every `q | k` is 3-Higgs with `v_q(k) ≤ 3` (k Higgs-cubefree, 246
    such k ≤ 600) and `2d ∈ H_even` for every odd `d | k`; composite members
    exist (m = 18 = 2·9, m = 30 = 2·15, confirmed by this run).
  - Thm 7 (prime-case reduction): `|H_even| < ∞` iff
    `{2p : p odd prime, 2p ∈ H_even}` is finite; `|H_even| ≤ 4^{|prime branch|}`.
  - Thm 8: `H_even ∩ [2,1200] = {2,6,10,18,26,30,46,62,82,122}`.
  - Thm 21: `#{m ≤ X : m ∈ H} ≪ X^{1−η}`, `Σ_{m∈H} 1/m < ∞` — **thinness,
    NOT finiteness**; on the prime branch the gap is exponential at the
    primitive-divisor height (Hong–Stewart lower bound).
  - Frontier (counting bounds): `|H_even ∩ [2,40000]| ≤ 201`,
    `|H_even ∩ [2,50000]| ≤ 272`; 262 undecided candidates, all `m = 2p` with
    p an odd Higgs prime, blocked by **unfactored 355–6000 digit cofactors** of
    `2^{2p}+1`.
  - Closures: `hb-no-v2ge4-witness-1e11` (catalogued, paper's computation):
    no prime `r ≡ 1 (mod 16p)`, `r ≤ 10^11`, divides `L_p` or `M_p` for the
    162 open candidates (m = 2426 extended to 6×10^11). `hb-lemma20-closures`
    (asserted): candidates 2446, 10294, 10958, 17398, 19066, 20282 closed by
    APR-CL-verified large prime divisors with non-3-Higgs Pratt witnesses;
    30882 via a further route. `research/notes/paper-extraction.md`.
  - Analytic target (live thread `research/threads/divisor-level-phi4p.md`):
    divisor-level problem for `Φ_{4p}(2)`; Aurifeuillean split
    `2^{2p}+1 = L_p·M_p`, `L_p = 2^p − 2^((p+1)/2) + 1`,
    `M_p = 2^p + 2^((p+1)/2) + 1`. §5.3: the missing theorem is
    divisor-transference / equidistribution of prime divisors of `Φ_{4p}(2)`
    (the paper states no such theorem exists); GRH and Artin/Hooley density
    are explicitly the wrong target.
- **(computed) The ten `H_even` members are independently confirmed IN** by
  **complete factorisation** of `2^m + 1` with every prime 3-Higgs —
  `code/out/heven_complete_verify.captured.txt` (e.g. `2^122+1 =
  5·733·1709·3456749·368140581013·667055378149`, all Higgs). Independent of
  the paper; **but it only proves membership of the ten, not emptiness of
  (122, 1200]** — that still rests on the paper (see Gaps).
- **(computed) 257 = 2^8+1 is non-3-Higgs** (`v2(256)=8 > 3`) in
  `code/out/heven_patterns.captured.txt`; the pattern script's hard-coded
  "want" table row `257:True` is a script bug, the computed False is correct.
- **(sourced, unverified) Frei 1978 via OEIS A002827 comment only:** a UPN not
  divisible by 3 has `2^m | n` with `m ≥ 144`, ≥ 144 odd components,
  `n > 10^440`. Primary text not in the library. Load-bearing for the
  "is 3 | n forced?" question.
- **(directive-8) Literature fetching is suspended for this cycle.** Downloads
  went 62 → 67 (Guy §B3, Handbook of Number Theory perfect-numbers chapter,
  Goto 2007) — all catalogue entries about a problem already stated correctly
  in `problem.md`. The library phase is closed; any new source fetch must be
  justified against a stated gap that actually blocks a computation, not a
  survey interest.
- **(sourced, unverified) Lean formalisation reference:**
  `google-deepmind/formal-conjectures ErdosProblems/1052.lean` defines
  `IsUnitaryPerfect`, asserts all five known are UPN, and marks "all UPNs are
  even" formally proved by AlphaProof per a linked fork — the fetched copy
  carries `sorry` bodies. Pointer for any lean_prover work; build nothing on
  it unverified.
  `research/summaries/erdos-1052-formal-lean-statement.md`
- **(scholar-pass 2026-08) Maciejewski full text verified verbatim.** Read the
  complete arXiv:2605.20475 paper; the `paper-extraction.md` digest is
  accurate. Additional pinned details: the 279→272 arithmetic is *inside* the
  paper (Theorem 19 factor-cache alone gives ≤ 279; Lemma 20's seven closures
  give 272); Lemma 20's exact table (m → p* digits → witness q) is
  2446→368→4513, 10294→1549→2657, 10958→1649→593, 17398→2612→139313,
  19066→2870→343081, 20282→3053 (v2(p*−1)=5071), plus 30882 = 6·5147 via
  Prop 4(3); the five composite-k inherited candidates are m ∈ {27978, 30354,
  31538, 41898, 46630}; Prop 5's proof uses the Fermat-number obstruction
  (`ord_q(2) = 2^(j+1)`, Lucas `q ≡ 1 (mod 2^(j+2))`, `v2(q−1) ≥ 4 > 3`).
  Claims `heven-verified-members`, `heven-frontier-50000`, `heven-two-mod-four`,
  `hb-*` all confirmed against the document.
- **(scholar-pass 2026-08) Wall 1975 read cover-to-cover.** The fifth UPN's
  exact factorization `2^18·3·5^4·…` is confirmed (OCR renders exponents as
  `2^183·5^47`; context + OEIS confirm 18 and 4). The paper's introduction
  *states the 2-adic budget identity*: for `N = 2^A k` UPN, k odd, the number
  of distinct prime divisors of k is at most A+1 — so the budget identity has
  1975 provenance too (and 1966 via SW Lemma 1 (3.6), recorded in the
  subbarao-warren summary). "10^102" does **not** occur in Wall 1975; the
  actual bound is `N < W ≈ 1.46e23`, seed cap `a < 38`.

## Ruled out

- **The structural backtracking search is CLOSED — with the correct Wall-1975
  statement.** Wall 1975 proves the fifth UPN `W ≈ 1.46e23` is next after
  87360 by eliminating all `N < W` (seed cap `a < 38`). **The figure "10^102"
  is unattested in any held source** (verified absence; the Wall–Hagis 1972
  letter and Guy §B3 are the likely carriers, both inaccessible so far —
  REQUESTS.md row open). State `10^23`, not `10^102`, when citing Wall.
  Compute-policy consequence unchanged: `10^23` alone is beyond any reachable
  region. Do not rerun the product-form search; keep only the denominator rule
  as a **forwards** divisibility constraint.
  `research/notes/wall-1975-bounds-and-102-claim.md`, `code/structural_search_CLOSED.py`.
- **Rarity is not finiteness.** Density-zero / `o(x)` / `O(x^ε)` statements
  about UPNs are almost certainly known and do not touch the question. Say
  which one you have.
- **The `a ≥ 8` line is closed as superseded** — Subbarao 1970 already establishes `a ≥ 11`. The equality-case thread `a-ge-8-bound` is closed: the bound `ω(odd)=a+1` is impossible for `2 ≤ a ≤ 28` (this run, checked). See Established.
- **The old sieve `pow(2,2400,r)==1` prefilter is FIXED; do not reintroduce
  it.** It dropped valid witnesses with `ord ∤ 2400` (e.g. `29 | 2^14+1`,
  ord 28). Current `code/heven_sieve.py` adds a complement sweep over orders
  `d ≤ 2400, v2(d) ≥ 2, d ∤ 2400`; the (29,14) class is recovered (m=14 in
  the 10^4 killed list).

## Numbers

- Oracle: `σ*(n) = Π_{p^a||n}(p^a+1)`, exact integers; `n` UP iff `σ*(n) == 2n`.
  Verified by hand on 6 and on non-UP controls.
- Budget table `(a, ω(odd), Σv2, a+1)`: 6→(1,1,2,2); 60→(2,2,3,3); 90→(1,2,2,2,
  equality); 87360→(6,4,7,7); fifth→(18,11,19,19). Identity exact in all five;
  equality in `ω ≤ a+1` holds only for 90.
- **Verify harness `code/heven_classify.py` Phase A is RED — current code
  fails its own self-tests** (`code/out/classify_test_10000.captured.txt`):
  (a) A2 prints "definitional mismatch" at every prime ≥ 3: `lib/higgs.py`
  `_higgs_status_bulk` has the literal-OEIS check backwards — it tests
  `product-of-q^{3e} | (p−1)` instead of `(p−1) | product-of-q^{3e}`; the
  classify-side literal loop is trivially identical to the working form so it
  cannot detect anything. The predicate itself is fine (17 non-Higgs, 31
  Higgs printed correctly). (b) A3 crashes at line ~113:
  `sympy.cyclotomic_poly(4*p).eval(2)` — the function returns an Expr with no
  `.eval`; use `.subs(x, 2)` or the Möbius product formula
  `Φ_n(2) = Π_{d|n}(2^d−1)^{μ(n/d)}`. Nothing built on classify's Phase A/B
  output is certified until these are fixed; the ten-member verification above
  does not depend on classify.
- **Sieve**: `sieve_test_1000` (old filter) and `sieve_test_10000` (complement
  sweep: 1859 witness pairs, 401 killed, incl. m=14) are small-range tests
  only. **No completed full pass to 10^8 / 10^9** — `sieve_pass_1e8` and
  `sieve_timing_1e6` carry "not run: superseded by the --lo/--hi interface"
  notes, not zero-byte files. `witnesses_1200.tsv` / `ord_sieve_table.tsv` on
  disk came from an uncertified partial sweep (largest witness prime 858001,
  e.g. `858001 | 2^104+1`, ord 104); re-run the sieve with --lo/--hi to a
  stated bound before trusting any B classification. The 1346-direct-pairs
  oracle equality quoted earlier was against the old buggy sieve — stale;
  re-run against the fixed sieve.
- **Claim ledger warning:** the Contradictions table of `research/CLAIMS.md`
  is corrupted (word-token garbage rows, from the derive script misreading the
  free-text `contradicts:` fields in the wall-1975 and subbarao-1970 notes).
  Read the notes themselves, not that table, until the parser is fixed.

## Recalled

Durable Cognee memory from earlier runs; consistent with Established here
(hypotheses checked against this problem).

- ROOT: any sixth UPN is even, has non-squarefree odd part (Graham), ≥ 9 odd
  components (Wall 1988), every prime divisor 3-Higgs, seed branch controlled
  by H_even; verification `|H_even ∩ [2,50000]| ≤ 272` with ~262 undecided
  candidates, blocked by unfactored cofactor digits.
- Settled restricted classes: no odd UPN (Subbarao–Warren), squarefree odd
  part exactly {6,60,87360} (Graham), impostor kernels eliminated for
  `1 ≤ a ≤ 10000` in the bounded box (Thm 2, three-filter certificate).
- 3-divisibility / Lemma 2 of Subbarao–Warren: first-γ / 3-divisibility
  structure underlies the seed description.
- Library inventory: 16 full texts held, library phase closed. Wall 1975
  *is* held (fifth-UPN paper); what is missing is the 10^102 anchor, Frei
  1978 primary, Goto 2007 primary.

## Contradictions

- **Encyclopedia of Mathematics "Unitary divisor"** writes `90 = 2·3^3·5`;
  correct is `2·3^2·5` (Subbarao–Warren, OEIS A002827, Wikipedia, workspace
  oracle). EoM typo; do not cite EoM for the factorization of 90.
- **"10^102 search bound": GOAL.md and ROOT.md state it as literature fact;
  the held Wall 1975 primary text contains no such figure** — its bound is
  `N < W ≈ 1.46e23`. Orphan claim (note `wall-1975-bounds-and-102-claim.md`);
  compute policy unaffected.
- **Verify harness vs expectation:** current `heven_classify` Phase A fails
  its self-tests while earlier CONTEXT described the pipeline as passing;
  nothing built on classify's Phase A/B output is certified until green.
- **Counting bounds: 279 vs 272 — RESOLVED (scholar-pass 2026-08).** The
  arithmetic is *inside* Maciejewski's paper: Theorem 19's factor-cache
  verification alone yields `|H_even∩[2,50000]| ≤ 279` (198 undecided in
  (1200,40000], 33 in (40000,45000], 38 in (45000,50000]); Lemma 20's seven
  closures (2446, 10294, 10958, 17398, 19066, 20282 via APR-CL-verified
  witness primes, plus 30882 = 6·5147 via Prop 4(3) from 10294) lower it to
  272. Same pipeline, two stages, resolved in the document. The 820 / 782 / 38
  figures (Theorem 19: 820 Higgs-cubefree candidates in (45000,50000], 782
  killed by verified non-3-Higgs witness, 38 partial-cofactor unknowns) are
  the coarser per-interval enumeration level, consistent with the 10 verified
  + 262 undecided split.
- **CLAIMS.md Contradictions table is corrupted** — the derive script
  misreads free-text `contradicts:` fields and emits word-token garbage rows
  (`contradicts (none)`, `contradicts research/notes/lower-bound-on-a.md only
  in that`, `contradicts GOAL.md, ROOT.md, CONTEXT.md to the extent…`). The
  real contradictions the notes assert are: (1) `subbarao1970-a-ge-11`
  supersedes the run's `a ≥ 8` — a strength ordering, not a disagreement; (2)
  `wall1975-bound-is-1e23-not-1e102` contradicts GOAL/ROOT/CONTEXT only in the
  unattested "10^102" figure. Read the notes, not the ledger table, until the
  parser is fixed.

## Gaps

1. **Verify harness Phase A is RED** — exact bugs in Numbers; fix (A2 literal
   direction, A3 exact cyclotomic value) and rerun
   `timeout 540 … | tee` before any Phase A/B claim from `heven_classify.py`
   is trusted. Immediate blocker for the independent `H_even ∩ [2,1200]`
   classification (TASKS.md item 2, spec `code/H_EVEN_VERIFY_SPEC.md`).
2. **Full sieve passes to 10^8 / 10^9 are not captured** — only small-range
   tests; run, capture with `timeout 540`, and restate the 1346-pairs oracle
   equality against the fixed sieve.
3. **`H_even ∩ (122,1200] = ∅` rests on the paper alone** until the B2 witness
   sieve + B3 complete-factor classification are green with certified
   witnesses.
4. Open structural directions, any result: (a) divisor-level problem for
   `Φ_{4p}(2)` — the paper's named analytic target (thread
   `divisor-level-phi4p`); (b) lower bound on `a` beyond 11, or impossibility
   of a residue class of `a`; (c) is `3 | n` forced for a sixth? (all five
   have it; open in both directions).
5. Sources not in library: Frei 1978 (e-periodica Heft 4 URL known), Goto
   2007 (paywalled), the 10^102 anchor (Wall–Hagis 1972 letter scanned with
   no OCR; Guy UPNT §B3 paywalled).
6. **`code/higgs/check_a057447.py` is execution-ready and has never been
   run** — no capture exists, and the script's own docstring says so. It is
   the true literal-definition check A2 was meant to be: generate 3-Higgs
   primes exactly per the OEIS A057447 name line, compare all 58 DATA terms,
   re-verify the five witnesses and the fifth term's EXAMPLE factorization,
   and test "every prime divisor of a UPN is 3-Higgs". Run
   `timeout 540 python3 code/higgs/check_a057447.py 2>&1 | tee
   code/out/higgs_a057447.captured.txt; echo EXIT_CODE=$?` — it closes the
   definitional-equivalence hole independently of the broken A2 self-test.