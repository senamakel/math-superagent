# Scholar audit — reference library pass (PE 351)

Audited every summary in `research/summaries/` against this run's goal
(compute H(10^8) for Project Euler 351), the tasks, and the claims ledger.
Read the full texts of every load-bearing source and spot-checked the rest.
Dated with the research agent's completion of the library build.

## Verdict

The library fully supports the run's conclusion:

- H(10^8) = **11762187201804552**, from Φ(10^8) = **3039635516365908**
  (OEIS A064018 row 8, reproduced by two independent sieves and the A063985
  recursion) via the closed form H(n) = 6·(C(n+1,2) − Φ(n)) = 3n²+3n−6Φ(n)
  (OEIS A216453, Kumar–Israel 2014).
- The answer matches the published PE 351 answer (three independent answer
  lists, per `research/research-report-pe351-known*.md`).
- Every load-bearing identity is sourced and, where the run used it, checked
  by a program: gcd=1 visibility (MathWorld VisiblePoint; brute.py),
  φ = μ∗id and Φ(n) = ½Σμ(d)⌊n/d⌋(1+⌊n/d⌋) (MathWorld, Wikipedia, ProofWiki;
  verify_mobius.py), Gauss divisor sum → floor-grouped recursion (MathWorld
  eq. 15, Wikipedia; patterns.py), Chai Wah Wu's A063985 recursion (OEIS;
  patterns.py).

## What each source group establishes

**Load-bearing for the answer** (summaries match full texts):
- OEIS A216453 — the exact sequence and closed form; `hexagonal-orchard-closed-form` (checked).
- OEIS A064018 — Φ(10^n) catalogue; a(8)=3039635516365908; `totient-sum-verification-values` (catalogued + checked by the two sieves).
- OEIS A063985 — cototient partial sums + Chai Wah Wu recursion; `totient-sum-fast-recursion` (checked).
- OEIS A002088 — per-sector visible count = Φ(n); `summatory-totient-counts-visible-pairs`.
- OEIS A018805 — coprime-pairs recursion base a(n)=2Φ(n)−1; `coprime-pairs-square-recursion`.
- OEIS A051953 — cototient; per-ring hidden count n−φ(n); `cototient-definition`.
- MathWorld VisiblePoint / TotientFunction / TotientSummatoryFunction, Wikipedia (Totient summatory, Möbius, Farey, Triangular lattice), ProofWiki — the classical identities, quoted verbatim.

**Corroborating context, not load-bearing** (all correctly flagged as such in
their summaries): Adhikari–Granville, Chen–Cheng, Goins–Harris–Kubik–Mbirika,
Baake–Grimm–Warrington, Baake–Moody–Pleasants, Murphy–Schmiedeler–Stonner,
Martin (rational polygons), Hensley (contours), Hening–Kelly,
Haase–Nill–Paffenholz (Ehrhart), Moree (carefree couples).

**Algorithmic context for the alternative Φ routes** (correctly marked
context/verification, not the adopted method): Deléglise–Rivat,
Helfgott–Thompson (both the Springer full text and the arXiv-ID correction),
Hurst, Brown (arXiv:2506.07386 + `totientsum.py`), Kulkov, gbroxey.

**Correctly marked unusable / irrelevant / abstract-only:**
- arXiv:1801.07931 — wrong paper (Barczy–Bősze–Pap), DO NOT CITE; correct HT paper at springer-helfgott-thompson.
- deleglise-rivat-summatory-mobius / -2 — wrong Project Euclid URL (Boender–te Riele), DO NOT CITE; correct DR at -correct.
- OEIS A098484, A113743, A212096, A293484 — wrong-candidate lookups, irrelevant; correct sequences listed.
- OEIS A308685 — disk count on the triangular lattice, the "trap" version of A003215; must not substitute.
- Ahuja, Erives–Sathiamurthy–Brady, Goodrich–Mbirika–Nielsen, Rearick, Nielsen–Goodrich, Hening–Kelly — abstract/landing pages only; summaries honestly say nothing is established by the file on disk.

## Inconsistencies found

1. **Durable memory still holds the stale check anchor "11762189901804552"**
   (transcription typo). Already contradicted in CONTEXT.md and by every
   program/catalogue; the correct value is 11762187201804552. The stale chunk
   should be superseded, not propagated.
2. **THREADS.md lists `pe351-phi-1e8` as "open"** though the thread file says
   `status: resolved`. The derived ledger was not refreshed after the thread
   file was updated. Tried changing the thread file's status to `closed`
   (recognised vocabulary in the approaches ledger); the re-derivation still
   shows `open`, so the thread derivation does not recognise either value and
   defaults unknown statuses to `open`. Mechanical artifact of the derived
   ledger; the thread file itself is accurate (`next: none`).
3. **BACKWARD.md and WEAKENED.md are stale**: both say "research/CLAIMS.md is
   empty; no code/brute.py exists on disk", but the ledger now holds 40+
   claims and brute.py exists. The three backward gaps (G-hexorchard-visibility,
   G-summatory-totient-value, G-answer-verification) are all settled by the
   run's verified computation but still listed open. The "Resting on nothing
   recorded" row is a parsing artifact of a `rests-on` line written before the
   ledger populated.
4. **Three summaries reference .full.md files absent from research/sources/**:
   rearick-1960-visibility-point-lattices, nielsen-goodrich-invisible-regions,
   ivl-projecteuler-problem-351. Their summaries honestly say "landing page
   only", so this is a dangling-wikilink provenance gap, not a correctness gap.

## Contradictions with recalled memory

Only the check-anchor typo (item 1) — already flagged on disk. No source
contradicts the run's computed answer; the two research reports independently
confirm it is the published answer to a known problem.

## What the run still lacks

Nothing blocking. Optional fourth route (per CONTEXT.md Gaps): the
Dirichlet-hyperbola / Gauss floor-quotient recursion for Φ(10⁸) at Θ(n^{2/3})
— the approach files mark it refuted-as-a-new-line but valid as an
independent verification; it would run without the 400 MB sieve.

## Durable findings stored

- `remember_memory`: the audit verdict + the three stale-ledger issues.
