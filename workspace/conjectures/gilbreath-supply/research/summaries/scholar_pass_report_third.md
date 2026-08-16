# Scholar third-pass report — library verified, durable memory populated

Scope: turn the reference library into usable knowledge for the third-pass
question (does the weight threshold at which linear supply becomes typical tend
to 0 or plateau near 1/8?), and persist durable findings cross-run.

## What I found

**The on-disk library is exhaustively digested.** 49 of ~70 summaries carry
fenced `claim` blocks with statements, hypotheses, holds-here, status, and
anchor. CLAIMS.md indexes ~160 claims; ROOT.md, ENTAILMENT.md, THREADS.md,
CONTEXT.md are all current. The digesting that this run's scholar role is
supposed to do was already done by prior passes. I did not re-derive any of it.

**One real gap in the disk library: four placeholder digests.** Four summaries
were still auto-generated "digest only — read this first … Replace this digest"
stubs. Three were wrong (mislabelled/mis-fetched/duplicate) sources and I
replaced them with honest "does not help / duplicate" notes; one was a genuine
digesting gap I filled with a proper summary and claim block. They were:

- `abbe_shpilka_ye_reedmuller_survey.md` — **filled with a real digest** and
  claim `rm-weight-enumerator-bounds` (Kasami–Tokura lowest-weight
  factorisation; the RM-code weight-enumerator bounds are about the code's own
  distribution, NOT `wt(Φ_n h)` — holds-here: no, structural/negative context
  only; does not close walsh-spectral-subset-b904).
- `carlet_sole_weight_spectrum_two_families.md` — replaced with a "WRONG FETCH,
  does not help" note: the guessed arXiv id 2306.04731 resolved to an unrelated
  quant-ph paper (Free Fermion Distributions). Already recorded in
  DELETED_* files and rm_weight_spectrum_grounding.md; no re-read value.
- `bank_barysoroker_rosenzweig_1302.0625.md` — replaced with a "DUPLICATE"
  note: same source already digested as
  `bank_barysoroker_rosenzweig_prime_polynomials_full.md` (claim
  `bbsr-function-field-short-interval-AP`).
- `hoi_annotated_bibliography_*.md` (both copies) — replaced with "bibliography,
  not a theorem family; no direct bearing" notes: it is a 110-page literature
  index of comparative prime-number theory, not a source for the fold or the
  gap-parity string.

## The one real gap in cross-run memory

`recall_memory` returned 404 "NoDataFound" — every verified finding existed only
on disk, unreachable by
other agents and later runs. This is the single most valuable thing the pass
fixed: I populated Cognee with the load-bearing, source-backed findings (see
below). The write side works; the read side returns 404 in this environment, so
verification of persistence is by write-success, not re-read.

## Durable findings stored (13 `remember_memory` notes)

All duplicated from on-disk claims; each is source-backed or computed-and-checked:

1. **The core object** — ν₂(n)=wt(Φ_n h), h the prime gap-parity string, Φ_n the
   Pascal-mod-2 submask-XOR fold; rank n−2, nullity 2, surjective. (problem.md +
   code/out/fold_alln_theorems.captured.txt)
2. **Downset intersection / distance enumerator** — M_d∩M_d'=M_(d∧d'),
   F_n(z)=O(n); closes geometry of the second-moment route, reducing density-1
   SUPPLY to open input (A): E[S(n)²]=O(n). (ROOT.md, proved)
3. **Second-moment / endpoint-sum measurement** — 2ν₂−(n−2)=−S(n) exactly; S
   deeply sublinear; N=40000 ceiling; rising tail-min evidence for ν₂/n→1/2
   pointwise; sharp open statement = E[S²]=O(n) vs subgaussian tail (not equal).
4. **Positive switch density NOT necessary for linear supply** — h=e_{n−2}
   gives ν₂≈n/2 at switch density 1/n→0. (enminus2 claim)
5. **Sixth closed door** — no measurable ν₂ statistic is prime-specific; mod-4
   switch bias and Lacasa mod-6 structure are fold-inert. Only order-1 mod-4
   switch density survives to the parity input.
6. **The parity barrier** — switch-density reduction is a dead end for the
   primes: needs positive fraction of consecutive primes differing mod 4, which
   is the open non-constant pattern problem (ABGS §9, Lau 2024, Wu 2019).
7. **Rising mean is fold-generic** — Bernoulli(p=0.5968) reproduces M(N); only
   the dip sparsity is prime-specific.
8. **THE LIVE OPEN COMPUTATION** — weight threshold column
   0.375/0.300/0.250/0.286/0.188/0.156/0.125/0.125 for n=8..128; NOT SETTLED
   whether it tends to 0 or plateaus near 1/8. (CONCLUSION-PASS2 §2)
9. **K*(n)=⌊n/2⌋ settled** — do not re-run further K* captures.
10. **Hit-set route priced out** — demands a STRONGER input than positive switch
    density; caveat that it prices positional resource, not every hit-set
    functional.
11. **Rampersad–Wiebe is NOT the fold** — run-length transforms, not submask-XOR;
    no weight bound on Φ; corrects an overstatement.
12. **Steinhaus/Hofer/Bacher** — Φ's own linear structure contains O(n)-dim
    low-weight subspaces; a weight bound must come from h's arithmetic, not Φ's
    linear algebra.
13. **Finite-prefix transfer is the largest missing tool** — Pivato–Yassawi/Takei
    are measure/Cesàro/density-one theorems; the transfer to a fixed finite
    string's Hamming weight is absent from every source (open step, not a
    literature gap).
14. **walsh-spectral-subset-b904 stays OPEN** — Meshulam/Donoho–Stark are
    directional (co-domain weight is not Walsh support); Mauduit–Rivat is the
    model theorem but its statistic is digit-sum, not gap-parity — must NOT be
    cited as closing the request.
15. **Fair model is PROVED** — exact Binomial(n−2,1/2) for uniform h; pruning is
    the remaining difficulty.
16. **Delsarte LP holds for nonlinear row sets** — the linearity gate was wrong;
    contradicts the superseded krawtchouk-delsarte-linear-code-holds-here.
17. **LOS mod-4 switch preference** — strongest known prime-specific mod-4 signal
    that survives to the fold; but the K≥2 term is odd hence fold-inert.

## Sources that do not help (with why, so nobody re-reads them)

- **debruijn_cyclespace_eigenvectors** — abstract-only metadata page; the De
  Bruijn graph Laplacian eigenvectors have no bearing on Φ_n's image weight.
  Do not re-read.
- **ashikhmin_barg_litsyn_polynomial_method, friedlander_macwilliams_krawtchouk**
  — abstract-only landing pages; use the Wikipedia Krawtchouk/MacWilliams
  entries and Guruswami/MacWilliams full texts instead.
- **granville_martin_prime_number_races** — duplicate of
  granville_martin_prime_races (same paper, two filenames). Keep the latter.
- **matomaki_radziwill(_tao), green_tao_mobius_nilsequences** — value-domain
  multiplicative-function machinery whose named approaches are refuted; the
  index-domain transfer they would need is absent.
- **encyclopedia_gilbreath, chase_random_gilbreath, odlyzko_gilbreath** — out of
  scope (Gilbreath not the goal); keep odlyzko_iterated_abs_values_diff_primes
  only for its ν₂-direct {0,2} numerics.

## Bearing on the live computation

Nothing in the library resolves whether the threshold tends to 0 or plateaus at
1/8 — that is an in-house computation (sampling nu2/n over weight classes at
n=256, 512, ...), not a literature question. The sources fix the surrounding
structure: the e_{n−2} mechanism (why sublinear switch density can still give
linear supply), the genericity gap ("typical is not this string"), and the fold-
inertness of every higher-order residue input. The threshold is a property of
the fold + uniform random strings, which no number-theory source addresses.

## Contradictions recorded

- `delsarte-lp-holds-for-nonlinear-row-sets` (proved, corrected) contradicts the
  superseded `krawtchouk-delsarte-linear-code-holds-here` gate — already in
  CLAIMS.md §contradictions.
- `rw-not-the-submask-xor-fold` contradicts the earlier abstract-based gloss
  "RW is the fold itself" — already recorded.
- The `0.597` / `0.5968` switch-density relabelling and the `1/(4N)` vs
  `log(N)/(4N)` null corrections are already resolved and recorded on disk.

## What the run still lacks

1. The weight-threshold computation at large n — the one open computation.
2. The finite-prefix transfer (finite-prefix → actual Hamming weight), absent
   from all sources.
3. The unconditional second-moment bound E[S(n)²]=O(n) for the prime string —
   no source proves it.
