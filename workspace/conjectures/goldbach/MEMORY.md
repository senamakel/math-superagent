# MEMORY — structural facts this run has established

Each entry is marked by evidence class: **proved** (mathematically established
by this run or a cited theorem), **verified-numerically** (computed and
cross-checked by this run), **sourced** (established by a cited primary
source), or **conjectured** (this run's hypothesis, not yet established).
Each carries what would falsify it.

## 1. Verified: n ≡ 4 (mod 6) are sums of two Chen primes for all n ≤ 10^8

- **Statement.** For every even n with 4 ≤ n ≤ 10^8 and n ≡ 4 (mod 6), there
  exist Chen primes p, q with p + q = n. (Chen prime: p prime and p+2 prime or
  semiprime.)
- **Evidence class.** verified-numerically. Exact sieve to B+2 (Eratosthenes),
  semiprimes marked by prime pairs f·g ≤ B+2 with f ≤ g, search for each n ≡ 4
  (mod 6) for p ≤ n/2 with p and n−p both Chen. Independent route: naive
  trial-division oracle (factor count with multiplicity, straight from the
  definition) agrees with the sieve's Chen flags for every p ≤ 200; Chen primes
  ≤ 50 exactly [2,3,5,7,11,13,17,19,23,29,31,37,41,47] (43 excluded: 45 = 3·3·5
  is not semiprime). Ordinary Goldbach oracle (lib/goldbach.py) reproduced for
  all even n ≤ 1000.
- **Runs:** 10^6 (none, 0.39 s), 10^7 (none, 4.6 s), 10^8 (none, 63.1 s). 16,666,667
  values of n tested at 10^8.
- **What would falsify it.** A single even n ≡ 4 (mod 6), n ≤ 10^8, with no
  Chen-prime pair; or a bug in the sieve/flag code (cross-checked to 200 only).
- **Source/artifact.** `code/chen_goldbach/check.py`,
  `code/out/chen_goldbach_1e8.md` (claim id `chen-prime-goldbach-check-1e8`).
  Bears on gap **G-structural-closure candidate (d)** in
  `research/backward/full-goldbach-via-exceptional-set.md`.
- **What it does NOT establish.** It is finite evidence only; the
  Grimmelt–Teräväinen exceptional set (n ≡ 4 mod 6 not sums of two Chen primes)
  could be nonempty above 10^8, and an empty finite exceptional set proves
  nothing about the binary Goldbach conjecture itself. It does show the
  restricted-class route is computationally clean and that any GT-exception
  below 10^8 would have been a novel finding (there is none).

## 2. Sourced: the Grimmelt–Teräväinen theorem this bears on

- **Statement.** (arXiv:2508.16400, Thm 1.1) All but O(N^{1−δ}) integers
  m ≤ N with m ≡ 4 (mod 6) are sums of two Chen primes, with δ > 0 and
  constants effective.
- **Evidence class.** sourced (preprint, not refereed). Recorded in the claim
  ledger as `grimmelt-teravainen-2025-two-chen-primes` by the research audit.
- **Consequence for this run.** The theorem already says the exceptional set is
  power-saving; the question this run's computation addresses is whether it is
  empty in the verified range. Answer so far: yes through 10^8 (for the
  n ≡ 4 mod 6 class).

## 3. Refuted-as-analogy: positive-density closure of a minimal counterexample set

- **Statement attacked.** If n_0 is the least even Goldbach counterexample then
  the counterexample set has positive lower density (E(X) ≫ X). (Gap
  G-structural-closure in the backward decomposition.)
- **Outcome.** refuted-as-analogy (checked). The backward skeleton's inference
  (E(X) ≪ X^{2/3} ∧ E(X) ≫ X ⇒ E(X) = 0) is logically valid, but the
  structural lemma supplying E(X) ≫ X rests on no known structure:
  - translation-by-modulus fails: primality is not translation-invariant;
  - multiplication-by-prime fails: p + q = n is additive, np − q is a different
    equation;
  - Bohr-set quasiperiodicity is unsupported: the singular series is a local
    major-arc feature and a counterexample is a place where minor arcs cancel it.
  - Small-scale analogues: least-failure closure fails for prime, square, and
    semiprime predicates (`code/refute/closure_analogues.py`).
- **What would refute this refutation.** A concrete provable map T with
  n ∈ E ⇒ T(n) ∈ E for a positive-density family. None is known.
- **Source/artifact.** `research/approaches/structural-closure-analogue.md`,
  claim `structural-closure-analogue-refuted` in
  `research/notes/claims-exceptional-set-and-circle-method.md`.
- **Lesson.** Do not spend another attempt on the positive-density closure
  inference directly; the live route is candidate (d) — the Chen-prime
  restricted class — or a genuinely new structural handle.

## 4. Sourced corrections from the literature audit (this run's research agent)

- **Chen explicit threshold, strongest single-exponential form.** Bordignon,
  *Bull. Austral. Math. Soc.* 105 (2022) 344–346: every even N > exp(36) ≈
  4.3×10^15 is p + P_2. (Distinct from Bordignon–Johnston–Starichkova's
  exp(exp 32.7).) Evidence: sourced (published).
- **Chen count constant record is 1.9728, published.** Runbo Li, *Math. Reports*
  28(78) (2026) 39–61: D_{1,2}(N) ≥ 1.9728·C(N)·N/(log N)^2. Evidence: sourced.
- **Zhao's P(q) = O(q^5) corollary is not new.** Xylouris already proved Linnik
  constant L = 5 (PhD thesis); Zhao's paper's "5.2 best up to date" is stale.
  Evidence: sourced (research audit cross-check).
- **Montgomery–Vaughan δ is "explicitly calculable but not computed"** (Pintz's
  exact paraphrase), not "effective". Evidence: sourced.
- Full audit: `research/audit/audit-binary-goldbach-literature-2026.md`.

## 5. Conjectured: the GT exceptional set is empty, and the all-even Chen-prime statement holds

- **Statement.** Every even n ≤ B is a sum of two Chen primes (all residue
  classes, not just 4 mod 6), for B at least as large as this run can verify.
- **Evidence class.** conjectured — being tested by the all-even run
  (10^7 → 10^8 → 10^9); the 4 mod 6 class is verified to 10^8 (entry 1).
- **What would falsify it.** An even n ≤ B with no Chen-prime pair. This is a
  stronger statement than the GT theorem's (all residue classes, and emptiness
  rather than power-saving sparseness), so a failure would be a genuine finding.

## 6. The standing thesis

- **Bet.** The Grimmelt–Teräväinen exceptional set is empty in every initial
  segment this run can verify; the first failing n, if it exists, lies beyond
  the verified Goldbach range. (Thesis ledger: `chen-prime-exceptional-set`.)
- **Because.** GT prove all but a power-saving set of n ≡ 4 (mod 6) are sums of
  two Chen primes; every small case checked has a Chen-prime representation; the
  full Goldbach exceptional set is empty below 4×10^18.
- **Refuted by.** A single even n ≡ 4 (mod 6) within our verified bound not a
  sum of two Chen primes; or a source establishing the GT exceptional set is
  provably nonempty.
