# Scholar pass — library digest verification and two claim corrections

This pass read the reference library against the live SUPPLY investigation,
verified the load-bearing digests against their full texts, and corrected two
claim blocks whose holds-here status was wrong or unverified. The library was
already complete (phase 1 passed: ROOT.md states the minimal-counterexample
structure, the verification bounds, and three settled classes); this pass adds
verification, not acquisition.

## The three load-bearing digests verified faithful to their full texts

1. **Guruswami, MacWilliams identities and the LP bound** (CMU Notes 5.1,
   Feb 2010; `research/sources/guruswami_macwilliams_lp_notes_fulltext.full.md`).
   Read the general-codes proof in full (lines 519–590). The Delsarte LP
   constraint `Σ_i A_i K_ℓ(i) ≥ 0` is proved for **any** subset C ⊆ F₂ⁿ by a
   sum of squares:
   `Σ_i A_i^C K_ℓ(i) = (1/|C|) Σ_{wt(z)=ℓ} (Σ_{x∈C} (−1)^{x·z})² ≥ 0`,
   with `A_i^C` the distance (inner) distribution. **No linearity anywhere.**
   The MacWilliams *identity* (dual-code transform) does need linearity, but
   the fold approach uses only the distance distribution and its Krawtchouk
   diagonalization.

2. **Pivato–Yassawi, "Asymptotic randomization of sofic shifts by linear
   cellular automata"** (ETDS 2006; lines 1690–1735 of the full text).
   Theorem 7.1 confirmed verbatim: for Φ = 1+σ, (Φ asymptotically randomizes
   µ) ⇔ (µ is Lucas mixing), with Lucas mixing defined as correlation decay
   of every character along binary-submask unfoldings. The digest is faithful;
   the finite-prefix transfer remains the open step (not in the paper).

3. **Ash–Beltis–Gross–Sinnott 2011** (line 192 of the full text): the
   "wide open, and cannot be treated using L-functions" assessment of the
   consecutive-pair frequency problem is verbatim. The digest is faithful;
   this is the parity barrier behind the switch-density reduction.

## Correction 1 — the Delsarte gate was backwards (claim `krawtchouk-delsarte-linear-code-holds-here` superseded)

The librarian's gate claimed the Delsarte LP bound "needs Ĉ(ω) ≥ 0, which
holds only for linear codes". The primary source refutes that: the Delsarte LP
holds for arbitrary codes by sum-of-squares, and the Krawtchouk diagonalization
is an identity valid for any multiset (verified exact in the capture). The fold
row set's linearity (XOR-closure) is a **non-obstacle**.

**Filed:** `delsarte-lp-holds-for-nonlinear-row-sets` (proved, contradicts the
old gate) in `research/notes/scholar_krawtchouk_gate_resolution.md`. Stored
durably.

**The real gate is the computed distance distribution:** `A_2 = O(n^{0.48})`
over n=16..4096 (NOT Θ(n²), so the fatal z²n² term is absent), and
`F_n(1−2p) = O(n)` with `F_n/n → ~1.0` for every fixed |z| < ~0.86 (exact
Fractions; capture `code/out/fold_second_moment_capture.txt`). Condition (C)
holds on the geometry side. **The remaining open step is (A): prove
`E[S(n)²] = O(n)` for the real prime h** — the submask-window autocorrelation /
second-moment bound, GOAL priority 2.

**Does NOT close request `walsh-spectral-subset-b904`:** the Delsarte LP bounds
code sizes A(n,d), not the per-input wt(Φ_n h). The Krawtchouk machinery is the
coordinate system, not the proof of the primes' second moment.

## Correction 2 — `uniform-second-moment-n-minus-2-exact` is a theorem for all n

The uniform benchmark `E[S²] = n−2` was filed as "verified n=3..7"; it is
provable for every n in one line from ledger facts (diagonal terms only at
p=1/2, off-diagonal vanish because distinct rows are even-sized with distance
≥ 2). The entailment ledger correctly flags it as entailed by the already-proved
`fair-model-exact-binomial` (wt(Φ_n h) exactly Binomial(n−2,1/2)). Its value is
a cleaner proof and an independent Parseval check, plus pinning the ideal
Chebyshev rate 1/(4n) for the density-1 route.

## Correction 3 — `lau-pattern-count-bound`: hypotheses FAIL here (holds-here: NO)

The Lau 2024 count bound has hypotheses **q squarefree** (confirmed in the full
text, Theorem 1.5/Corollary 1.6). The switch-density input needs modulus
q = 4 = 2², which is **not squarefree** — so the theorem does not apply at the
q=4, m=2 case SUPPLY needs. This is the "true theorem whose hypotheses fail
here" case the holds-here field exists to catch. Corrected from "unchecked" to
`holds-here: NO`; it remains context, never the arithmetic input. The operative
barrier is `lau-nonconstant-pattern-open`: even one (1,3)/(3,1) mod-4 pair is
not known to occur infinitely often.

## Ledger hygiene

- The two dangling contradiction rows in CLAIMS.md (`r-finite-verified-contradicted`
  vs `R-finite-verified`, and `rw-not-the-submask-xor-fold` vs
  `rw-described-as-the-fold-itself`) are both real, recorded corrections whose
  left-hand claim exists on disk (in `code/out/r_finite_verified_contradiction.md`
  and `research/summaries/rampersad_wiebe_2regular_fulltext.md`); the "no claim
  of that id" warning is a ledger-typo artifact (the settled rung/gloss were
  never filed as claim blocks). Both are resolved by reading the anchored note.
- The FRONTIER.md supply-chain citation spam is a miner artifact: a "Defining
  Supply Chain Management" paper was fetched and its citation ring (dozens of
  supply-chain papers citing each other) now ranks at the top of FRONTIER. The
  43-source library itself is clean (only 4 "supply chain" string hits, all
  false positives like "defining the Pascal matrix"). The ranking should be
  cleaned or the ring excluded from future frontier derivation.

## Sources that do not help (and why)

- `friedlander_macwilliams_krawtchouk`, `ashikhmin_barg_litsyn_polynomial_method`:
  reference pointers only (landing pages, not full PDFs). Their advertised
  statements are fully covered by the primary tier (MacWilliams 1963, Guruswami
  notes, Wikipedia entries). Do not re-read.
- `essential_coding_theory_guruswami_rudra_sudan_fulltext`: textbook machinery,
  already digested as `essential-coding-theory-machinery` (asserted). It
  corroborates the Delsarte-for-general-codes fact but adds nothing the
  Guruswami notes do not prove more cleanly for this run.

## What the run still lacks

- **The arithmetic heart (A):** a proof that `E[S(n)²] = O(n)` for the real
  prime h. This is GOAL priority 2, strictly weaker than positive mod-4 switch
  density, and is the single open step between the settled geometry side
  (condition (C)) and density-1 SUPPLY. No source in the library supplies it —
  the parity-barrier sources (ABGS, Lau) establish that the *mean* (switch
  density) is out of reach, and the *variance* statement (A) is orthogonal to
  it and untouched by the literature.
- **The finite-prefix transfer** from the Pivato–Yassawi/Takei measure-level
  ergodic theorems to the single deterministic finite-string fold. Named as the
  largest missing technical tool in ROOT.md; no source supplies it.

## Claim blocks filed this pass

- `delsarte-lp-holds-for-nonlinear-row-sets` — proved; contradicts
  `krawtchouk-delsarte-linear-code-holds-here` (superseded).
- `uniform-second-moment-n-minus-2-exact` — proved; entailed by
  `fair-model-exact-binomial`.
- `lau-pattern-count-bound` — holds-here corrected to NO (q=4 not squarefree).

All three stored durably in Cognee. The run's beliefs are now: the geometry
side of the Krawtchouk approach is settled and correctly sourced; the
arithmetic second-moment input (A) is the single open step; and no source
currently in the library closes it.
