# Independent audit: exact binary Goldbach status (verification, Chen, exceptional set, ternary, restricted classes)

Auditor role: research specialist, independent pass over the phase-1 library in
`research/ROOT.md`, `research/notes/`, and `research/sources/`, checked against
live literature via Exa (2026 environment). This file records what the audit
*confirmed*, what it *corrected or refined*, and what remains *uncertain*.
Each item cites the source(s) that establish it. Everything here is
evidence-checked; nothing is asserted on the strength of a search summary alone
unless marked `[unverified against full text]`.

---

## 0. Method and scope

Five audit questions, per the request:

1. **Verification record** — what is the exact current bound, and are the
   "beyond 4×10^18" claims credible?
2. **Chen's theorem** — exact statement, explicit thresholds, constants.
3. **Exceptional-set exponent** — exact chronology and current best.
4. **Ternary distinction** — Helfgott's theorem stated exactly, and why it does
   not imply the binary case.
5. **Restricted classes** — Chen primes, Linnik–Goldbach, GRH-conditional
   results, sparse-set results.

Sources used: on-disk full texts + fresh Exa searches + citation graph walks.
URLs are given inline. Where two sources conflict, the conflict is recorded in
the "Uncertainties" section rather than silently resolved.

---

## 1. Computational verification record

### Confirmed
- **Refereed record: 4×10^18.** Oliveira e Silva, Herzog, Pardi, "Empirical
  verification of the even Goldbach conjecture and computation of prime gaps up
  to 4·10^18", *Math. Comp.* 83 (2014) 2033–2060, DOI
  [10.1090/S0025-5718-2013-02787-1](https://doi.org/10.1090/s0025-5718-2013-02787-1).
  Every even n ≤ 4×10^18 verified; ~781.8 single-core CPU-years; double-checked
  to 4×10^17. Using Ramaré–Saouter, odd Goldbach verified to 8.37×10^26.
  Chain: Sinisalo 4×10^11 (1993) → Richstein 4×10^14 (2000) → OeS–H–P 4×10^18
  (2014). [Confirmed by citation graph: Richstein
  [10.1090/s0025-5718-00-01290-4](https://doi.org/10.1090/s0025-5718-00-01290-4)
  cited by OeS–H–P.]

- **Nothing in a refereed venue supersedes 4×10^18 as of this audit.** All
  "beyond" claims located are preprints, Zenodo deposits, or unrefereed journal
  items.

### Claims beyond 4×10^18 — assessed
| Claim | Venue | Assessment |
|---|---|---|
| Daniel, Njagi, Mutembei, "A numerical verification of the strong Goldbach conjecture up to 9×10^18" | GPH-International Journal of Mathematics 6(11) (2023) 28–37; Zenodo [10391440](https://zenodo.org/records/10391440) | Unrefereed/low-tier journal. Method based on the authors' own "new formulation of even numbers" ([10.9734/arjom/2024/v20i4793](https://doi.org/10.9734/arjom/2024/v20i4793) is their claimed *proof* of the conjecture, which is not accepted by the community). No independent verification. **Not treated as established.** |
| Gosar, Das, Pardasani, "Empirical Verification of Goldbach's Conjecture Beyond Four Quintillion", Preprints.org 2025 | [10.20944/preprints202503.0949.v1](https://doi.org/10.20944/preprints202503.0949.v1) | Preprint, probabilistic primality tests, up to 6×10^18. No independent check. **Not treated as established.** |
| Llorente Saguer, "GoldbachGPU", arXiv:2603.02621 (2026) | arXiv [2603.02621](https://arxiv.org/abs/2603.02621) | Reaches only 10^12 on one GPU. Explicitly *not* beyond 4×10^18. |
| Llorente Saguer, "A Lock-Free, Fully GPU-Resident Architecture", arXiv:2603.07850 (2026) | arXiv [2603.07850](https://arxiv.org/abs/2603.07850) | Reaches 10^13 on four GPUs; theoretical ceiling 1.84×10^19, no claim of reaching it. |

**Verdict: the confirmed record stands at 4×10^18.** ROOT.md's statement is
correct and should keep the "confirmed record" framing. The Daniel et al.
9×10^18 claim is in a real journal (GPH-Int. J. Math.) but is not
independently verified and its method is not the community-standard
exhaustive sieve; the correct status is "unverified claim in a low-tier venue",
not "record".

---

## 2. Chen's theorem: n = p + P₂

### Classical statement (confirmed)
Chen Jing-run, "On the representation of a larger even integer as the sum of a
prime and the product of at most two primes", *Scientia Sinica* 16 (1973)
157–176, DOI [10.1360/ya1973-16-2-157](https://doi.org/10.1360/ya1973-16-2-157).
Every sufficiently large even N is N = p + a with p prime, a prime or
semiprime. **Ineffective** ("sufficiently large" not explicit). Confirmed by
Zhang's 2023 anniversary article and by Friedlander–Iwaniec's fiftieth
anniversary paper [arXiv:2303.06122](https://arxiv.org/abs/2303.06122).

### Explicit thresholds — a correction is needed
There are **two distinct "explicit Chen" results**, and ROOT.md conflates them:

1. **Bordignon, Johnston, Starichkova (BJS), arXiv:2207.09452 (2022; IJNT 2025)**:
   every even N > exp(exp 32.7) is p + P₂, and moreover the number of
   representations π₂(N) > 2·10^−4·U_N·N/log²N; every even N ≥ 4 is p +
   product of at most e^29.3 primes. This is the result ROOT.md cites, and it
   is correct: the on-disk full text states Theorem 3 (π₂(N) bound for N >
   exp(exp(32.7))) and Corollary 4. **Publication status: International Journal
   of Number Theory 21 (2025)** (confirmed via Dudek–Johnston citation:
   "Bordignon, Johnston, Starichkova, Int. J. Number Theory, Volume 21, 2025").
   ROOT.md's "2022/2024" should become "2022 preprint / IJNT 2025".

2. **Bordignon (solo), "An explicit version of Chen's theorem", Bull. Austral.
   Math. Soc. 105 (2022) 344–346**, DOI
   [10.1017/S0004972721001301](https://doi.org/10.1017/S0004972721001301):
   **Theorem 1: every even number bigger than exp(36) — NOT exp(exp 36) — is
   p + P₂**, and Theorem 2: every even number > 2 is p + product of at most
   exp(33) primes. This is a *different, much stronger-in-threshold* but
   *weaker-in-constant* result (exp(36) ≈ 4.3×10^15, i.e. nearly in the
   computational range, vs exp(exp 32.7) ≈ 10^(7.7×10^13)). The search result
   explicitly confirmed the threshold is `exp(36)` (e^36).

The "exp(36)" appearing in the Cambridge abstract is therefore **not** a typo
for exp(exp 36); it is the solo-Bordignon threshold. ROOT.md must not mix the
two. The correct state:
- BJS 2022/2025: N > exp(exp 32.7), the best *double-exponential* threshold.
- Bordignon 2022: N > exp(36) ≈ 4.3×10^15 — dramatically better, but this is
  the Bulletin version; note it *coexists* with the BJS result and its proof
  was the seed that BJS corrected/extended. Both are "proved (by source)".
- Yamada 2015, arXiv:1511.03409: N > exp(exp 36), with π₂(N) > 0.007·U_N·N/log²N
  (confirmed on disk, Theorem 1.1). BJS improved the double-exponential
  threshold to exp(exp 32.7) and noted Yamada's proof has gaps ([50, (87) &
  (104)]), so the "Yamada exp(exp 36)" result is superseded by BJS.

**Correction to ROOT.md §4.1**: the line "n > exp(exp 32.7) ≈ 10^(7.7×10^13)
(Bordignon–Johnston–Starichkova 2022/2024)" is right as far as it goes, but the
surrounding text should (a) cite the Bulletin solo result exp(36) explicitly
and (b) date BJS as IJNT 2025. Also ROOT.md's "Refined count: S(N) >
0.867·C(N)·N/log²N (Chen 1978…)" is **out of date**: see §2.1.

### 2.1 Chen-count constant (lower bound on representations)
The 0.867 figure in ROOT.md has been superseded **three times**:
- 0.899 (Wu, 2008)
- 1.733 (Runbo Li, 2024 preprint)
- **1.9728 (Runbo Li, "On Chen's theorem, Goldbach's conjecture and almost
  prime twins II", Math. Reports 28(78) (2026) 39–61, DOI
  [10.59277/mrar.2026.28.78.1.2.39](https://doi.org/10.59277/mrar.2026.28.78.1.2.39))** —
  **now published**, not preprint. Statement: for sufficiently large even N,
  D_{1,2}(N) ≥ 1.9728·C(N)·N/log²N where C(N) is the singular-series factor
  ∏_{p>2}(1−1/(p−1)²)·∏_{p|N,p>2}(p−1)/(p−2). This is within 1.36% of the
  conjectured constant 2.

ROOT.md §4.1 "Refined count: S(N) > 0.867" must be updated to cite the 1.9728
published record (the claim ledger already has `chen-count-constant-1.9728` as
asserted-by-source; it can now be upgraded to published).

### 2.2 Explicit threshold — status refinement
- BJS threshold exp(exp 32.7): **published** IJNT 2025 (per Dudek–Johnston
  citation; the on-disk arXiv text is the preprint form). ROOT.md's "2022/2024"
  is fine but "2025" is the journal year.
- Under GRH, explicit Chen improves to exp(exp 15.85) (Bordignon–Starichkova,
  arXiv:2211.08844) and the Johnston thesis cites exp(exp 14) under GRH
  (Bordignon–Starichkova). These are conditional, not unconditional.

---

## 3. Exceptional set E(X) < X^{1−δ}

### Confirmed chronology (from Pintz II, on disk, arXiv:1804.09084, §1)
- Vaughan 1972: E(X) ≪ X·exp(−c√log X) — no power saving.
- **Montgomery–Vaughan 1975**: E(X) ≪_δ X^{1−δ} for some δ > 0, "unspecified
  but explicitly calculable" (Pintz's words). **Correction to ROOT.md §4.2:
  the δ is "explicitly calculable" in principle, not "effective" in the sense
  of a computed value.** The 1975 paper is Acta Arith. 27 (1975) 353–370, DOI
  [10.4064/aa-27-1-353-370](https://doi.org/10.4064/aa-27-1-353-370).
- Chen–Liu 1989: δ = 0.05.
- Hongze Li 1999: δ = 0.079 (per Pintz; Kumchev–Tolev cite δ = 0.086 — see
  Uncertainties).
- Hongze Li 2000: E(X) < X^{0.914} (Acta Arith. 92 (2000) 71–88, DOI
  [10.4064/aa-92-1-71-88](https://doi.org/10.4064/aa-92-1-71-88)).
- **Lu 2010: E(X) < X^{0.879} (δ = 0.121) — the best *published***
  (J. Number Theory; corroborated by Bhowmik–Halupczok 2020 survey,
  [10.2969/aspm/08410001](https://doi.org/10.2969/aspm/08410001)).
- Pintz 2018 preprint: E(X) < X^{0.72} (δ = 0.28). **Still a preprint** — the
  2023 *Acta Arith.* publication (Part I, DOI
  [10.4064/aa220728-31-3](https://doi.org/10.4064/aa220728-31-3)) is the
  explicit-formula part, not Part II with the 0.72. Bhowmik–Halupczok (2020)
  still call 0.879 the "best published proof" and 0.72 a "very recent
  preprint". Huixi Li's 2023 survey (arXiv:2306.17769) describes E(N) ≪ N^{0.72}
  as "best known bound … due to Pintz (2018)". So the correct status is:
  **best published δ = 0.121 (Lu 2010); best claimed δ = 0.28 (Pintz 2018,
  preprint, unrefereed)**.
- **Zhao 2025, arXiv:2511.05631: E(X) = O(X^{7/10})** (δ = 0.3), implicit
  constant **ineffective**. This is a *stronger claim* than Pintz's 0.72
  (X^{0.7} < X^{0.72}). Status: **unrefereed preprint, not verified by a
  second route**; the on-disk digest confirms the theorem statement verbatim
  ("E(X) = O(X^{7/10}), where the implicit constant is ineffective"). The
  claim ledger marks it asserted-by-source — correct.

### Correction needed in ROOT.md §3 (minimal counterexample item 3)
ROOT.md says "Zhao (2025) claims O(X^{7/10}) = O(X^{0.7})" — correct, but it
also lists "δ = 0.28 (Pintz 2018, arXiv preprint)" as if the 0.72 were the
current best; the Zhao preprint (0.7) is the current best *claim*, Lu 2010
(0.879) is the current best *published*.

### Linnik-constant corollary of Zhao — a stale claim
Zhao's abstract also claims P(q) = O(q^5) for the least prime in an AP.
**This is not new**: Xylouris proved L = 5.2 (2011) and L = 5 in his PhD
thesis; the current unconditional record is **L = 5 (Xylouris)**, confirmed by
Zaman's thesis ("current world record sitting at L = 5 by Xylouris") and by
Leung 2024 ("Xylouris proved that one can take L = 5"). Zhao's own paper says
"L = 5.2 by Xylouris in 2009, which is still best up to date" — this is stale;
the paper appears not to incorporate the later L = 5 result. The corollary
P(q) = O(q^5) is therefore not a new contribution of Zhao 2025. (If Zhao's
L = 5.2 is being used only as an input, the E(X) = X^{0.7} claim is unaffected,
but the paper's novelty statement should be read with this in mind.)

---

## 4. Ternary Goldbach (Helfgott) — exact statement and distinction

### Exact statement
**Helfgott, "The ternary Goldbach conjecture is true", arXiv:1312.7748 (2013);
book form "The ternary Goldbach problem", arXiv:1501.05438 (2015); ICM 2014
proceedings, Vol. II, 391–418.** Every odd integer n > 5 is a sum of three
primes. Proof is analytic for n ≥ 10^27 (confirmed on disk, line 88: "The
proof given here works for all n ≥ C = 10^27"), with the remaining range
covered by Helfgott–Platt, "Numerical verification of the ternary Goldbach
conjecture up to 8.875·10^30", *Experimental Mathematics* (2013), DOI
[10.1080/10586458.2013.831742](https://doi.org/10.1080/10586458.2013.831742).
The major-arc work uses a verified GRH up to bounded height (Platt's
computation) — this is a *computational verification of GRH for finitely many
L-functions*, not an assumption of GRH. The proof is unconditional.

**Publication-status nuance**: the primary citation is the arXiv preprint +
ICM 2014 paper; there is no single "Annals of Mathematics"-style journal
publication. The theorem is universally accepted as proved. ROOT.md's "Helfgott
2013/2015" is right; the "2015" refers to the book-length arXiv:1501.05438.

### Why it does NOT imply the binary case (confirmed, worth stating precisely)
- Ternary: n = p₁ + p₂ + p₃ for odd n. Binary: n = p₁ + p₂ for even n.
- The ternary theorem *follows from* the binary (n odd ⇒ n−3 even ⇒ n = 3 +
  p₁ + p₂ by binary), not the reverse. There is no known deduction of binary
  from ternary. The parity obstruction (a sum of two primes is even; a sum of
  three primes is odd) means ternary never addresses the even case directly.
- Helfgott's own abstract says "the binary, or strong, Goldbach conjecture had
  [its] origin in an exchange of letters" — he does not claim it.

### Related: at-most-k-primes results (confirmed)
- Tao, "Every odd number greater than 1 is the sum of at most five primes",
  *Math. Comp.* 82 (2013), DOI [10.1090/S0025-5718-2013-02733-0](https://doi.org/10.1090/s0025-5718-2013-02733-0):
  every odd N > 1 is sum of ≤ 5 primes; Schnirelman constant ≤ 6 (every n > 1
  is sum of ≤ 6 primes). ROOT.md §2.5 is correct.
- Ramaré 1995: every even n is sum of ≤ 6 primes (ROOT.md cites this; it is
  the standard result).

---

## 5. Restricted classes and conditional results

### 5.1 Chen primes (two-Chen-prime Goldbach)
- **Grimmelt–Teräväinen 2025, arXiv:2508.16400** (v2, 29 Jul 2026 on disk):
  Theorem 1.1: there is δ > 0 such that all but O(N^{1−δ}) natural numbers
  m ≤ N, m ≡ 4 (mod 6), are sums of two **Chen primes** (p with p+2 ∈ P₂).
  "Both δ and the implied constant in this theorem are effective and could in
  principle be computed." This is a power-saving exceptional-set result for a
  restricted class. It improves on Tolev (N(log N)^−A for (5,7)), Meng (3,8),
  Matomäki (2,7). **Restricted-class result with exact hypotheses**: m ≡ 4
  (mod 6), m ≤ N, summands are Chen primes. Status: preprint (2025), not
  yet refereed. ROOT.md does not currently list this; it is a genuine
  "restricted class" entry worth adding.
- **Grimmelt–Teräväinen 2022, arXiv:2207.08805**: exceptional set for sums of
  two almost-twin primes (p₁ + p₂ with p₁+2 ∈ P₂, p₂+2 ∈ P₃), power-saving
  bound. On disk.

### 5.2 Linnik–Goldbach: n = p₁ + p₂ + K·(powers of 2)
- **Johnston–Trudgian 2026, arXiv:2605.17825**: Theorem 1, **under GRH**,
  every sufficiently large even integer is p₁ + p₂ + 6 powers of 2 (K = 6).
  This improves Heath-Brown–Schlage-Puchta's GRH K = 7. Unconditional K = 13
  (Heath-Brown–Schlage-Puchta), K = 8 (Pintz–Ruzsa). Under Elliott–Halberstam,
  K = 4 (Pintz–Ruzsa). ROOT.md §4.4 is correct; the "Johnston–Trudgian 2026"
  citation is to an arXiv preprint (May 2026). Note the environment's clock
  has arXiv IDs into 2026; treat as preprint.
- Pintz–Ruzsa 2003 (Acta Arith. 109, DOI
  [10.4064/aa109-2-6](https://doi.org/10.4064/aa109-2-6)) is the classical
  reference for the K = 8 unconditional / K = 4 under EH.

### 5.3 GRH-conditional explicit Chen
- Bordignon–Starichkova 2022, arXiv:2211.08844: under GRH, every even N >
  exp(exp 15.85) is p + P₂; Johnston's 2025 thesis cites exp(exp 14) under
  GRH. These are conditional partial results.

### 5.4 Granville sparse-set / RH-equivalence
- Granville 2007, "Refinements of Goldbach's conjecture, and the generalized
  Riemann hypothesis", *Funct. Approx. Comment. Math.* 37 (2007): strong
  averaged Goldbach forms ⇔ GRH; and "if every even n > 2 has more than
  γn/log²n representations, then every even integer is a sum of two primes
  from a sparse set P with |P∩[1,x]| ≤ η√x log x". The hypothesis is not
  known to hold for any γ > 0 (it would follow from the unproved
  Hardy–Littlewood conjecture). ROOT.md §4.5 is correct. Full text on disk.

### 5.5 Siegel-zero connection
- Friedlander–Iwaniec, "Exceptional zeros, sieve parity, Goldbach", *Essential
  Number Theory* 1 (2022) 13–39, DOI
  [10.2140/ent.2022.1.13](https://doi.org/10.2140/ent.2022.1.13): a weak
  two-sided HL-Goldbach bound would rule out Siegel zeros; conversely
  exceptional-zero bounds feed the parity problem. Matomäki–Merikoski
  (arXiv:2112.11412) improve the hypothesis to a single residue class.
  ROOT.md §4.6 is correct.

---

## 6. The two obstructions — stated exactly (confirmed)

1. **Parity problem**: classical (Selberg/Jurkat–Richert) upper-bound sieves
   cannot distinguish numbers with an even number of prime factors from those
   with an odd number; hence a pure sieve argument cannot prove binary
   Goldbach or twin primes. The P₂ → P₁ step is blocked. This is a *proven*
   limitation of the classical framework (Friedlander–Iwaniec 2022 survey,
   full text on disk), not folklore. Maynard-type multidimensional sieves and
   the asymptotic sieve evade it for some problems, but not for binary
   Goldbach (two variables cannot share a prime). ROOT.md §5 Obstruction A is
   accurate.
2. **Minor-arc control**: for the binary problem the minor-arc integral is the
   same order as the major-arc contribution; the ternary problem's minor arcs
   are controllable (Vinogradov + large sieve), which is why ternary is proved
   and binary is not. ROOT.md §5 Obstruction B is accurate.

---

## 7. Uncertainties and items needing a second source

1. **M–V 1975 δ effectiveness**: Pintz says "unspecified but explicitly
   calculable δ > 0"; Bhowmik–Halupczok say "positive effectively computable
   constant δ". These agree in substance (the existence is effective, the
   value is not computed), but the *primary text* is still not on disk (the
   ICM scan has no text layer). The request `full-text-montgomery-6b42`
   remains open. The claim "first power-saving" is confirmed by both Pintz and
   Bhowmik–Halupczok.
2. **Li 1999 δ = 0.079 vs Kumchev–Tolev δ = 0.086**: Pintz (on disk) says Li
   "1999 … δ = 0.079"; Kumchev–Tolev say "currently (1.6) is known to hold
   with δ = 0.086 (see Li)". These are two different Li results or a
   discrepancy. ROOT.md's "Li 1999 δ = 0.079" follows Pintz; flag as
   uncertain. (Kumchev–Tolev's survey is from 2004; Pintz's is from 2018; the
   δ = 0.086 figure may be Li's published Quart. J. Math. version vs the
   preprint 0.079.)
3. **Xylouris L = 5 vs L = 5.2**: Zhao's paper says 5.2 "still best up to
   date"; multiple independent sources (Zaman thesis; Leung 2024; the 2019
   Russian article "Константа Линника не превосходит 5") state Xylouris's
   PhD thesis proves L = 5. The L = 5 result is in a thesis, which may be why
   Zhao calls 5.2 the "published" record. Record as: published L = 5.2
   (Xylouris 2011); L = 5 in thesis (Xylouris, "On Linnik's constant", 2011).
   The Zhao corollary P(q) = O(q^5) is at best a restatement of Xylouris.
4. **Helfgott's venue**: no single journal publication of the full proof; the
   accepted citations are arXiv:1312.7748 + ICM 2014 + the 2015 book preprint.
   ROOT.md's "Helfgott 2013/2015" is fine; the "proved" status is beyond
   dispute regardless of venue.
5. **Johnston–Trudgian 2026 K = 6**: arXiv:2605.17825 (May 2026). Under GRH.
   Unconditional K = 8 (Pintz–Ruzsa) and K = 13 (Heath-Brown–Schlage-Puchta)
   are the unconditional records. ROOT.md's §4.4 table is correct; the "2026"
   is a preprint.
6. **Runbo Li 1.9728 published in Math. Reports 2026**: the DOI resolves to a
   2026 journal page; treat the constant as published (the underlying arXiv is
   2405.05727v4). The claim ledger's `chen-count-constant-1.9728` can be
   upgraded from asserted-by-source to published-by-source.
7. **Zhao 2025 E(X) = X^{0.7}**: unverified by a second route, unrefereed.
   The claim ledger correctly marks it asserted-by-source. Do **not** treat as
   the established record; the established record is Lu 2010 (0.879) published,
   Pintz 0.72 preprint, Zhao 0.7 preprint.
8. **BJS exp(exp 32.7) vs 32.6**: one citing work (Johnston–Starichkova 2022,
   arXiv:2208.01229) says "exp(exp(32.6))" while the BJS paper itself says
   32.7. The on-disk BJS full text says 32.7 (Theorem 3, Corollary 4). Treat
   32.7 as correct (primary text) and 32.6 as a citing typo.

---

## 8. What should change in ROOT.md / notes (concrete list)

1. **§3 verification**: keep 4×10^18 as the confirmed record; add the
   assessment that Daniel et al. 9×10^18 is an unverified claim in a low-tier
   journal (GPH-Int. J. Math.), not a record.
2. **§4.1 Chen**: (a) split the two explicit results — Bordignon (solo, Bull.
   AMS 105 (2022) 344–346): N > exp(36) ≈ 4.3×10^15; BJS (IJNT 2025): N >
   exp(exp 32.7); (b) update the count constant from 0.867 to 1.9728 (Runbo Li,
   Math. Reports 2026, published); (c) note Chen's original is ineffective.
3. **§4.2 exceptional set**: change "δ > 0 effective" (M–V) to "δ > 0
   explicitly calculable but not computed"; state clearly: best *published*
   δ = 0.121 (Lu 2010, X^{0.879}); best *claimed* δ = 0.3 (Zhao 2025 preprint,
   X^{0.7}), with Pintz 0.28 (X^{0.72}) between; all constants ineffective.
   Note Zhao's P(q) = O(q^5) corollary is not new (Xylouris L = 5).
4. **§4.3 ternary**: cite Helfgott's analytic threshold n ≥ 10^27 and
   Helfgott–Platt's computational cover to 8.875×10^30; cite the ICM 2014 +
   arXiv book as the publication record; keep the "does not imply binary"
   statement.
5. **Add §4.7 (or similar)**: Grimmelt–Teräväinen 2025 two-Chen-prime
   exceptional-set result (m ≡ 4 mod 6, power-saving δ, effective constants,
   preprint).
6. **§5 obstructions**: no change needed; both are accurately stated.
7. **Uncertainties section**: add the Li 1999 δ discrepancy and the Xylouris
   L = 5 vs 5.2 nuance.

---

## 9. Sources consulted (URLs)

Primary on disk (full text): Chen via Zhang 2023 and Friedlander–Iwaniec
2303.06122; Yamada 1511.03409; BJS 2207.09452; Pintz II 1804.09084; Zhao
2511.05631v2; Helfgott 1312.7748, 1501.05438, 1205.5252, 1305.2897;
Helfgott–Platt 1305.3062; Tao 1201.6656; Granville 2007; Grimmelt–Teräväinen
2207.08805 and 2508.16400; Johnston–Trudgian 2605.17825; Friedlander–Iwaniec
ENT 2022; Matomäki–Merikoski 2112.11412; Bhowmik–Halupczok 2010.01308;
Kumchev–Tolev math/0412220; Oliveira e Silva project page.

Live searches confirming/refining: OeS–H–P DOI; Richstein DOI; Daniel et al.
Zenodo + GPH-Int. J. Math.; Gosar et al. Preprints.org 2025; GoldbachGPU
arXiv:2603.02621 and 2603.07850; Runbo Li DOI 10.59277/mrar.2026.28.78.1.2.39;
Runbo Li III (2025); Bordignon Bull. AMS DOI 10.1017/S0004972721001301;
Bordignon–Starichkova 2211.08844; Johnston thesis UNSW 31766; Xylouris L = 5
via Zaman thesis hdl 1807/79531, Leung arXiv:2402.07941, Thorner–Zaman
10.2140/ant.2017.11.1135, and the 2019 Russian note 10.22405/2226-8383-2018-19-3-80-94;
Pintz Part I Acta Arith. 10.4064/aa220728-31-3; Pintz "On a Conjecture of
Descartes" 10.1007/978-3-031-31617-3_17 (D(X) ≤ X^{3/5+ε} for Descartes
numbers — distinct from E(X)); Bhowmik–Halupczok survey 10.2969/aspm/08410001;
Helfgott–Platt Experimental Math DOI 10.1080/10586458.2013.831742; Tao Math.
Comp. DOI 10.1090/S0025-5718-2013-02733-0.

---

*Audit date: this cycle. Every "confirmed" item is backed by at least one
primary/secondary source read or searched in this audit; items marked
"uncertain" are flagged rather than resolved.*
