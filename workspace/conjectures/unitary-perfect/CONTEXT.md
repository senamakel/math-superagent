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
  impossible for `2 ≤ a ≤ 28`.** Primary anchor `code/out/equality_case_verify_FIXED.captured.txt`
  (directives 4–14, exact Fraction arithmetic, 4/4 points PASS): (1) a=1 max
  product = 4/3 exactly, {5,9} is the odd part of 90; (2) 2^8+1=257 is prime,
  forced when a=8; (3) 9=3^2 and 49=7^2 are admissible, 3 and 7 are not;
  (4) M(a) < T(a) exactly for all 2 ≤ a ≤ 28 with
  M(28)=1.997752859598546538 < T(28)=1.999999993, and
  M(29)=2.004964963784822807 > T(29) — **a=29 is NOT excluded, boundary is
  28**. Consequence (directive 14): a sixth UPN in the equality case needs
  `a ≥ 29`; with Wall 1988's ≥ 9 odd components, that is the sharpest form
  the workspace holds. Claim `budget-equality-case-impossible` is `checked`
  (first ledger conversion in twelve cycles). BUG-FIX (directive 11):
  `admissible_sizes()` had a slice-then-sort bug (missed 37,41,53; wrongly
  included 121,361,529); fixed to sort-then-slice over BOUND=800 + safety
  assertion. Thread `a-ge-8-bound` closed. a=1 is realised by n=90.
  `research/notes/equality-case-eliminated.md`.
- **(computed / checked, this run) Divisor-level Gaussian table for all odd
  primes p ≤ 61**: full factorization of `2^{2p}+1` (max 37 digits, nothing
  left unfactored), 71 primitive-divisor rows, all checks C1–C7 pass —
  `code/heven_gauss.py` → `code/out/heven_gauss_61.captured.txt`. Verifies
  **(F1)** every prime divisor `r | Φ_{4p}(2)` is primitive, `ord_r(2) = 4p`,
  `r ≡ 1 (mod 4p)`, with the single exception `r = 5 | Φ_20(2)` at p = 5
  (LTE: `v_5(2^{2p}+1) = 1 + v_5(p)`); **(F2)** the one-way generator
  equivalence `(2/r)_4 = +1 ⟺ r ≡ 1 (mod 16)`, i.e. `v2(r−1) ≥ 4 ⟹ r ∉ P_3`.
  **The converse is FALSE** (sourced, paper Lemma 20): 343081 has
  `v2(343080) = 3` yet is non-3-Higgs via Pratt chain
  `343081 ≻ 953 ≻ 17` — the mod-16 test is a one-way obstruction only.
  Exactly **12 heads** (`r ≡ 1 mod 16`): p=7:113; 11:2113; 19:525313;
  29:536903681; 37:593,231769777; 43:500177; 47:3761,140737471578113;
  53:15358129,586477649; 59:157649 — independently certified by
  `heven_heads_verify.py` (`ALL HEADS CERTIFIED 12/12`,
  `code/out/heven_heads_verify.captured.txt`). Empirical (exact, not a
  proof): for the 16 3-Higgs primes p ≤ 61, `2p ∈ H_even` (the seven Thm-8
  members) iff `Φ_{4p}(2)` has no divisor `≡ 1 mod 16` — all seven members
  have zero heads, all nine excluded p (7,11,19,29,37,43,47,53,59) carry a
  head. Character distribution by (p mod 8, Aurifeuillean half) is in the
  capture: **no residue class forces a head** (the per-class shortcut, M4,
  is refuted). **Extended to p ≤ 97** (`char_mod16_sums.captured.txt`,
  24 rows, 291 s): 7 further heads — p=73: 649301712182209,
  9444732965601851473921; p=79: 381364611866507317969,
  604462909806215075725313; p=83: 13063537; p=97: 4657, 17637260034881 —
  consistent at p=83,97 with `heven_extend_probe` full factorisations.
  p=67,71,89 are 3-Higgs with **zero heads yet excluded** by Thm 8, so a
  missing head is NOT a membership certificate: the p≤61 zero-head ⟺
  membership iff was range-limited. The extension run's self-check FAIL
  lines are pinned as script artefacts: Q1 Parseval divides by 8 instead
  of 4 (divisor 4 confirmed by `char_mod16_verify.captured.txt`), and
  Q2's "sum_e = 3 or 2" targets drop the non-primitive factor 5 and use a
  rational e-of-class — the honest full-Gaussian exponent is 0 mod 4 for
  all p (identical to the directive-14 closed form). The 7 new heads are
  NOT yet independently certified (`char_mod16_verify2.py` prepared;
  capture 0 bytes).
- **(computed/checked, this run) Directive-14 RESOLVED: closed-no-constraint.**
  `(2/(2^p+i))_4 = 1` identically for every odd prime p ≥ 3 —
  `code/out/directive14_quartic_closed_form.captured.txt` (EXIT_CODE=0), two
  independent exact routes agreeing on all 17 primes p ≤ 61: (A) direct
  product over the Gaussian factorization of 2^p+i; (B) Williams-1976
  supplement on the primary associate 1−2^p·i, exponent (2^p−2^{2p})/2
  ≡ 0 (mod 4) for all odd p, valid for all p ≥ 3 given the sourced law.
  Consequence: the quartic product pins divisor class-counts only mod 4 and
  never forces a head r ≡ 1 mod 16 — it adds nothing to the one-way
  per-divisor mod-16 test. `biquadratic-character-divisors` is definitively
  closed; the adopted `second-moment-character-mod16` approach is untouched
  (its bound is on the quadratic character sums, not the product).
- **(computed / checked) Definitional equivalence of 3-Higgs is closed
  independently of the classify harness.** `code/higgs/check_a057447.py`
  first-executed → `code/out/higgs_a057447.captured.txt`: literal A057447
  recursion (p 3-Higgs iff `p−1 | P³`, P = product of certified primes,
  base 2) reproduces all 58 OEIS DATA terms; all five witnesses pass
  `σ*(n) == 2n`; every witness prime divisor is 3-Higgs — ALL CHECKS
  PASSED. `code/out/verify_257_literal.captured.txt` adds: literal rule vs
  `lib.higgs.is_3_higgs` agree on all 168 primes ≤ 1000 (0 disagreements,
  127 literal-Higgs); 257 non-Higgs confirmed.
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
  - **Gap decomposition (live skeleton `research/backward/heven-finiteness-via-mod16.md`):**
    **CORRECTED per directive 16.** The four structural reductions
    (prime-case, m ≡ 2 mod 4, Higgs-cubefree, Thm-30 conditional) are
    **conditional-on-paper** — asserted/catalogued from Maciejewski, not
    independently proved or checked here. The skeleton now honestly shows
    **6 open gaps**: four conditional-on-paper structural lemmas plus the
    two genuinely open (H1) and (H2). The parallel C29 skeleton shows 4
    genuinely open gaps (no structural borrows masked as discharged). Both
    are conditional reductions, which is a real result. Exactly two lemmas
    remain to attack for the Thm-30 route: (H1) — every p with
    `ω(Φ_{4p}(2)) ≥ C·log p` has a divisor `r ≡ 1 mod 16` — and (H2) —
    `ω(Φ_{4p}(2)) ≥ C·log p` for p ≥ p0.
    Each of the paper's Conjectures 23 / 24 / 29 alone would close C6;
    Conjecture 29 (proportional `#{r ≡ 1 mod 16} ≥ c·ω`) is the adopted
    second-moment approach's target.
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
- **(sourced) Williams 1976 primary text held** (`research/summaries/williams-1976-supplement-biquadratic-reciprocity.md`,
  claim `williams1976-biquadratic-supplement-primary`): π = a+bi primary iff
  `a+b ≡ 1 mod 4`, `b ≡ 0 mod 2`; main law `(α/β)_4 = (−1)^{bd/4}(β/α)_4`;
  supplements `[1+i/π]_4 = i^{(a−b−1−b²)/4}`, `[i/π]_4 = i^{(a−1)/2}`,
  and the derived `[2/π]_4 = i^{−b/2}` — proves the 1+i row that
  `qr-supplementary-2` (Wikipedia) only asserted.
  **Numerically verified against the definitional quartic character**
  (computed/checked): `code/verify_biquadratic_supplement.py` →
  `code/out/q_supplement.captured.txt` (43 bytes, EXIT_CODE=0) — the closed
  forms for i, 1+i, −1, 2 agree with the definitional evaluation
  `α^((Nπ−1)/4) mod π` on **all 501 primary Gaussian primes** with 1 ≤ a < 400.
  This is a check of the start of the Williams source, not of the whole paper.
  Primary anchor for the first-moment evaluation in the adopted second-moment
  approach; terminal input for the directive-14 closure (that evaluation is a
  class function of r mod 16 with no odd-prime information).
- **(sourced, unverified) Frei 1978 via OEIS A002827 comment only:** a UPN not
  divisible by 3 has `2^m | n` with `m ≥ 144`, ≥ 144 odd components,
  `n > 10^440`. Primary text not in the library. Load-bearing for the
  "is 3 | n forced?" question.
- **(directive-8) Literature fetching is suspended for this cycle.** The
  library phase is closed; the last acquisitions (Guy 3rd-ed §B3, Handbook of
  Number Theory perfect-numbers chapter, Goto 2007, Hagis 1985, a second Frei
  volume-TOC scan) are all catalogue entries about a problem already stated
  correctly in `problem.md`, or adjacent problems with no bearing — none adds
  a theorem this run lacks. Any new source fetch must be justified against a
  stated gap that actually blocks a computation, not a survey interest.
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
- **Sequence-level structure hunting on H_even is exhausted (negative,
  `code/out/pattern_extract.captured.txt`).** `K_SEQ = m/2 =
  {1,3,5,9,13,15,23,31,41,61}` and `M_SEQ = {2,6,10,18,26,30,46,62,82,122}`
  match **no OEIS entry**; no constant-coefficient recurrence (the order-5 fit
  is a spurious artifact of 10 points), no low-degree polynomial, no stable
  differences, no closed-form structure. The 264 prime candidates
  `1213 ≤ p ≤ 24989` are residue-mixed mod 4 (117 of 264 ≡ 1). Membership and
  candidates are determined by the factorization of `2^{2p}+1`; do not re-run
  sequence mining on the 10 verified terms.
- **Approach ledger: `biquadratic-character-divisors` is REFUTED (absorbed);
  `second-moment-character-mod16` is ADOPTED.** (Why: the
  biquadratic route's deliverable — existence of one head, the (H1) form of
  Thm 30 — is strictly weaker than Conjecture 29's proportional bound, and
  its product identity determines a character sum only mod 4; orthogonality
  needs the sum. What survives inside the adopted approach: the verified
  one-way equivalence `(2/r)_4 = 1 ⟺ r ≡ 1 mod 16` as the first-moment
  evaluation. The adopted approach targets `#{r ≡ 1 mod 16} ≥ c·ω` via
  Dirichlet orthogonality on (Z/16Z)* + a second-moment bound; its falsifier
  is systematic bias into `r ≡ 9 mod 16`.) **TASKS.md
  "Active approaches" is STALE** — it still calls biquadratic-character-divisors adopted; the
  approach file and APPROACHES.md both say refuted. **DIRECTIVE 14 is CLOSED
  at the argument level (unconditional):** heads are exactly the
  character-+1 class (`(2/r)_4 = +1 ⟺ r ≡ 1 mod 16`, F2), so every product
  identity over these characters is invariant under adding/removing heads —
  the head count never occurs in any product identity, hence no product
  identity can force a head for any residue class of p (deliverable (a) is
  impossible by argument, not merely unproved). The product identity's
  entire content is the congruence `C5−C13+2·C9 ≡ 0 (mod 4)` among the
  NON-head classes {5,9,13}, all with v2(r−1) ≤ 3 whose 3-Higgs status is
  decided by odd primes of r−1 — invisible to quartic characters of 2; the
  composite evaluation candidate is verified identically +1 (computed/checked,
  `code/out/directive14_quartic_closed_form.captured.txt`, all 17 odd primes
  p ≤ 61, 71 Gaussian divisor rows): `(2/(2^p+i))_4` evaluated two independent
  ways — direct product of `(2/π)_4^e` over the Gaussian factorization, and
  the supplementary-law closed form `[2/α]_4 = i^{(2a−b−2−b²)/2}` on the
  primary associate α = −i(2^p+i) = 1 − 2^p i (hand derivation of the
  exponent `2^{p−1}(1−2^p) ≡ 0 (mod 4)`) — every row +1, all matches OK.
  Verdict: **no residue class of p forces a head `r ≡ 1 mod 16`, and the
  global quartic character carries no information about which r | Φ_{4p}(2)
  can be 3-Higgs beyond the one-way per-divisor mod-16 test. Directive 14 is
  CLOSED with a computed capture — the biquadratic line is dead twice over:
  product ≠ sum (a product determines the character sum only mod 4, and
  orthogonality needs the sum), and the product is ≡ +1 identically, so it
  cannot even pin the count mod 4.** The adopted second-moment approach is
  untouched: its first moment S_χ is a SUM with weight +1 on heads; only the
  product is head-blind.
  `research/approaches/biquadratic-character-divisors.md`,
  `research/approaches/second-moment-character-mod16.md`.

## Numbers

- Oracle: `σ*(n) = Π_{p^a||n}(p^a+1)`, exact integers; `n` UP iff `σ*(n) == 2n`.
  Verified by hand on 6 and on non-UP controls.
- Budget table `(a, ω(odd), Σv2, a+1)`: 6→(1,1,2,2); 60→(2,2,3,3); 90→(1,2,2,2,
  equality); 87360→(6,4,7,7); fifth→(18,11,19,19). Identity exact in all five;
  equality in `ω ≤ a+1` holds only for 90.
- Gaussian/character tables: 17 primes p ≤ 61, 71 divisor rows, 12 certified
  heads (`heven_gauss_61.captured.txt`); extended to 24 primes p ≤ 97
  (`char_mod16_sums.captured.txt`, 19 heads total of which 12 certified, 7
  awaiting certification); full per-p table at `heven_gauss_61.captured.txt`.
- Factorisation frontier (Aurifeuillean halves, `heven_extend_probe.captured.txt`):
  L_p·M_p fully factors through p = 307 (12 primes 61..307; worst singles
  p=251 M 381 s, p=151 M 77 s); probes p=331/401/521 hit the 540 s cap
  (rc=124). Beyond ~307 only partial factorisation — and a head needs just one
  found divisor.
- **Verify harness `heven_classify.py`: the two Phase-A bugs are FIXED ON DISK
  but the full rerun is UNCERTIFIED.** Code now has the literal rule
  `(P**3) % (p−1) == 0` (correct direction) in both `lib/higgs.py::
  _higgs_status_bulk` and `phase_a2`, and `phase_a3` computes `Φ_{4p}(2)` via
  `cyclotomic_poly(4*p, x).subs(x, 2)` (the `.eval` crash is gone). The
  standalone equivalents PASS (`verify_257_literal.captured.txt`,
  `higgs_a057447.captured.txt` — see Established). But
  `classify_test_10000_FIXED.captured.txt` is **0 bytes**: the full
  `heven_classify.py` run has no PASS capture on disk, so nothing built on
  classify's Phase A/B output is certified until it is rerun with
  `timeout 540 … | tee`. B3/B4 additionally needs certified sieve tables
  (Gap 2 below).
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
- **Verify harness vs expectation:** the `heven_classify` Phase-A bugs are
  fixed on disk and the standalone equivalents PASS, but the full harness has
  no PASS capture (`classify_test_10000_FIXED.captured.txt` is 0 bytes) —
  nothing built on classify's Phase A/B output is certified until a nonzero
  green capture exists. Earlier CONTEXT described the pipeline as RED on a
  stale capture; the code is fixed, the rerun is missing.
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

1. **Full `heven_classify.py` harness rerun is uncertified** — code fixed on
   disk (A2 literal direction, A3 `.subs(x, 2)`) with standalone equivalents
   PASS (`verify_257_literal`, `higgs_a057447`), but
   `classify_test_10000_FIXED.captured.txt` is 0 bytes; rerun and capture
   (`timeout 540 … | tee`) before trusting any Phase A/B claim from
   `heven_classify.py`. B3/B4 also still needs certified sieve tables.
2. **Full sieve passes to 10^8 / 10^9 are not captured** — only small-range
   tests; run, capture with `timeout 540`, and restate the 1346-pairs oracle
   equality against the fixed sieve.
3. **`H_even ∩ (122,1200] = ∅` rests on the paper alone** until the B2 witness
   sieve + B3 complete-factor classification are green with certified
   witnesses.
4. Open structural directions, any result: (a) divisor-level problem for
   `Φ_{4p}(2)` — the paper's named analytic target (thread
   `divisor-level-phi4p`; full-factorization window is p ≤ ~307 —
   `heven_extend_probe.captured.txt`, 12 primes 61..307 fully factored;
   probes p=331/401/521 hit the 540 s cap — the natural range for C29
   empirics); (b) lower bound on `a` beyond 11, or impossibility of a
   residue class of `a`; (c) is `3 | n` forced for a sixth? (all five have
   it; open in both directions). Directive-14: CLOSED, see Established
   (argument-level AND computed). `char_mod16_sums.captured.txt` (9128 B)
   now holds the exact S_χ tables for all 24 primes p ≤ 97 — but its two
   internal self-checks FAIL (pinned script artefacts: Parseval /8 vs the
   correct /4; Q2 "sum_e = 3 or 2" targets drop the non-primitive factor 5
   and use a rational e-of-class) and the 7 heads beyond p=61 are NOT
   certified (`char_mod16_verify2.py` prepared, capture 0 bytes): report
   the tables, not their checks, and not the new heads as certified.
   `q_supplement` is DONE (PASS, 43 bytes).
5. Sources not in library: Frei 1978 (e-periodica Heft 4 URL known), Goto
   2007 (paywalled), the 10^102 anchor (Wall–Hagis 1972 letter scanned with
   no OCR; Guy UPNT §B3 paywalled).