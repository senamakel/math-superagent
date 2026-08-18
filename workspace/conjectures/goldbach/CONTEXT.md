# Shared context

What this run knows, in its own words. The context curator writes this file and
is the only role that writes it; nearly every other role is sent it on every
model call. So what is here is what the run knows without going to look, and
what is missing is what each agent rediscovers separately.

It carries what an agent would otherwise rebuild from disk, from the note store,
or from a session it was not present for: established results with their basis,
approaches that died and why, what the computed numbers look like, what durable
memory relates this problem to, and where two accounts disagree. It is not a
catalogue of files — `research/INDEX.md` is that — and not a narration of what
agents did.

**It has a token budget** (`MATH_AGENT_CONTEXT_TOKENS`, 10,000 by default). The
file is re-sent on every model call in every role that reads it, so length here
is a bill the whole run pays many times over; a brief past its budget is cut
where it exceeds it on the way into a prompt, with a notice saying so. Link the
file that still holds any detail compressed away — source notes under
`research/summaries/`, untouched full texts under `research/sources/`,
reflections, threads. Durable findings belong in Cognee. A statement nobody can
trace to a source is worth less than no statement.

> **Librarian's flag (cycle: search + claims, post-2020 state of the art).**
> The previous "Gaps" entry saying "the library is empty" is **stale and wrong**.
> The library on disk is substantial: `research/ROOT.md` passes the phase-1 exit
> test (minimal-counterexample structure, verification bound 4×10^18, ≥3
> restricted classes with hypotheses, both obstructions stated exactly),
> `derived/CLAIMS.md` holds 41 claims, and `research/sources/` holds ~35 full
> texts. CONTEXT's Established/Ruled-out/Numbers/Recalled/Contradictions
> sections below were empty; this is the librarian's report of what the library
> establishes, for the context curator to reconcile into its own voice.

## Established

What this run may treat as known, each marked proved, computed and checked,
sourced, or conjectured, with a link to what establishes it.

- **Goldbach's binary conjecture is open.** (sourced) Every even n > 2 is a sum
  of two primes; open since 1742. `research/ROOT.md`.
- **Verification to 4×10^18.** (sourced, refereed) Oliveira e Silva–Herzog–
  Pardi, Math. Comp. 83 (2014), exhaustive; no counterexample below 4×10^18.
  `research/sources/oliveira-e-silva-goldbach-verification-page-sweet-ua-pt.full.md`.
  Refereed record stands; beyond-4e18 claims (Zenodo/Preprints/arXiv 2603.02621)
  are unrefereed and below the bar.
- **Chen's theorem.** (sourced, proved) Every sufficiently large even N is
  p + P2 (prime plus number with ≤2 prime factors). Explicit thresholds:
  N > exp(exp 36) (Yamada 2015), N > exp(exp 32.7) (Bordignon–Johnston–
  Starichkova 2022/24). `research/sources/yamada-…full.md`,
  `research/sources/bordignon-…full.md`.
- **Chen-count constant record: 1.9728.** (sourced, arXiv v4 2024/25) Runbo Li,
  D_{1,2}(N) ≥ 1.9728·C(N)·N/(log N)^2, within 1.36% of conjectured 2. Record
  chain: Chen 0.67 → … → 0.899 (Wu) → 1.733 (separate 2024 preprint [13]) →
  1.9728. **Note: v1 of arXiv:2405.05727 proves 1.253, not 1.733.**
  `research/sources/runbo-li-…2405.05727.html.full.md`,
  `research/sources/runbo-li-…2405.05727v1.full.md`.
- **Lichtman level of distribution 66/107 ≈ 0.617.** (sourced, arXiv 2023)
  First level beyond the square-root barrier used for Goldbach; conditional 5/8
  on Selberg eigenvalue conjecture. Goldbach upper bound G(a) ≲ 3.3907·Π_a(a),
  greatest improvement since Bombieri–Davenport 1966. `research/sources/lichtman-…full.md`.
- **Parity problem is a proven sieve limitation.** (sourced, survey) Friedlander–
  Iwaniec, Essential Number Theory 1(1) 13–39 (2022), full text on disk.
  No pure sieve argument can reach "prime" from "P2". `research/sources/friedlander-iwaniec-…ent-2022-fulltext.full.md`.
- **Exceptional-set bounds.** (sourced) E(X) ≪ X^{1−δ}: Montgomery–Vaughan 1975
  (effective δ>0, full text unobtainable — textless scan); published record
  δ=0.121 (Lu 2010, abstract-only); Pintz 2018 preprint E(X)<X^0.72; Zhao 2025
  preprint E(X)=O(X^0.7) unrefereed. `research/notes/claims-exceptional-set-and-circle-method.md`.
- **Ternary Goldbach proved (Helfgott).** (sourced, proved) Every odd n>5 is
  three primes; does NOT resolve binary. Helfgott suite on disk.
- **All-even Chen-pair Goldbach: first failure 302 (≡ 2 mod 6).** (computed and
  checked, exact) The all-even sweep (every even n ∈ [4,B] = p+q with p, q both
  Chen primes) has first failure **302** at every bound; the Grimmelt–Teräväinen
  4-mod-6 class stays clean through 10^9. Complete failure census to 10^6: 27
  failures, all ≡ 2 mod 6 (302, 332, 458, …, 35912), none in 0 or 4 mod 6. Two
  independent routes agree exactly (bytearray sieve + sympy factorisation,
  27-failure list ≤ 10^5); trial-division oracle confirms 302. Mechanism: for
  n ≡ 2 mod 6, every Goldbach pair has both primes ≡ 1 mod 3, so q+2 ≡ 0 mod 3
  and q is Chen iff (q+2)/3 is prime — a congruence-driven both-or-neither
  obstruction. `code/out/chen_goldbach_all_1e9.md` (claim
  chen-prime-goldbach-all-even-1e9), `code/chen_goldbach/check.py`.
- **Chen-count 0.867 claim is superseded** — see 1.9728 above.
- **The Goldbach–Siegel-zero connection.** (sourced, survey) Weak HL-Goldbach
  bounds would rule out exceptional zeros; Friedlander–Iwaniec 2022.

## Ruled out

Approaches that failed, and the reason each failed. A known dead end is a
result, and this section is what stops the run paying for one twice.

- **Pure sieve → "prime".** Parity problem; proven structural limit (FI 2022
  survey). Only reaches p + P2.
- **Classical circle method → binary.** Minor-arc error same order as major
  arcs; only almost-all-n results.
- **GRH alone.** Does not resolve parity or minor-arc control.
- **Disproof by computation.** Verified to 4×10^18; any counterexample larger.

## Numbers

Computed terms, the range over which the oracle and the method agree, the size
of the object at the bound in the statement.

- Verification bound: 4×10^18 (refereed record).
- exp(exp 36) ≈ 10^(4.7×10^14); exp(exp 32.7) ≈ 10^(7.7×10^13) (Chen thresholds).
- Chen-count constant: 1.9728 (record, arXiv v4).
- Exceptional-set exponents: published 0.879 (Lu 2010), preprints 0.72 (Pintz
  2018), 0.7 (Zhao 2025).
- Ternary: verified ≤ 8.875×10^30 (Helfgott–Platt); binary verification implies
  odd Goldbach ≤ 8.37×10^26 (Ramaré–Saouter).
- Chen-pair all-even: first failure 302; 27 failures ≤ 10^6 (all ≡ 2 mod 6);
  largest smallest-witness p ≤ 10^6 is 99991 at n = 884342; 4-mod-6 class
  clean to 10^9 (166,666,667 values, 800.59 s).

## Recalled

What durable memory holds about this problem or problems of its shape, marked as
recalled rather than as this run's own finding, with hypotheses checked against
this problem before being relied on.

- Durable memory (librarian, this cycle) holds the post-2020 state of the art:
  Runbo Li 1.9728 / Lichtman 66-107 / FI 2022 survey, and the resolved
  exp(exp 36) "contradiction" (a search snippet had dropped one "exp"; the true
  threshold exp(exp 36) ≈ 10^(4.7×10^14) is far above 4×10^18, so no conflict).

## Contradictions

Where sources disagree, where a source contradicts recalled memory, or where a
computation contradicts a conjecture. The most valuable rows here: record them
rather than silently picking a side.

- **Apparent**: a Cambridge Bulletin AMS snippet seemed to claim Chen's theorem
  for n > exp(36) ≈ 4.3×10^15, which combined with verification to 4×10^18
  would prove Goldbach. **Resolved**: snippet dropped one "exp"; the actual
  threshold is exp(exp 36), matching Yamada 2015 on disk. No contradiction.
- **Record chain discrepancy**: the claims note originally credited 1.733 to
  "Runbo Li 2024 preprint v1"; v1 actually proves 1.253. 1.733 is the separate
  preprint [13]. Corrected in `research/notes/claims-post2020-state-of-the-art.md`.
- **Chen-pair exceptional set is nonempty**: the earlier 4-mod-6-only run found
  "no failure to 10^8", but the all-even sweep finds first failure 302 (≡ 2 mod
  6). Not a contradiction — the 4-mod-6 class genuinely stays clean — but it
  corrects the impression that the Chen-pair phenomenon is "empty": the
  exceptional set is real and lives in the 2-mod-6 class.

## Gaps

What the run still needs and has not found. State a gap precisely enough to be a
research request rather than a mood.

- Full text of Montgomery–Vaughan 1975 (Acta Arith. 27, 353–370): only textless
  scan exists; DOI route 502; EuDML links to same scan. Statement corroborated
  by Pintz 2018 + Bhowmik–Halupczok on disk. Request `full-text-montgomery-6b42`.
- Chen 1973 original (Sci. Sinica 16, 157–176): paywalled; statement
  corroborated by Yamada 2015 + Zhang 2023 on disk. Request
  `freely-downloadable-copy-17eb`.
- Lu 2010 "Exceptional set of Goldbach numbers" (J. Number Theory 130,
  2359–2392): JNT paywall, no arXiv; the best *published* exceptional-set
  exponent (δ=0.121) rests on abstract + corroboration. New request recorded.
- Oliveira e Silva–Herzog–Pardi journal PDF: AMS rate-limit (429); author's page
  on disk.
