# Scholar pass 2 — the library against the reopened K>1 question

## What this run's job was
Digest each source against the reopened question (GOAL priority 2): is there a
functional of the fold Φ, sensitive to correlation order `K` with `1 < K ≲ n/2`,
controllable by an arithmetic input strictly weaker than pointwise mod-4 switch
density? (`research/REOPENED.md` proved Φ sees order ≈ n/2; the eight-collapse
equivalence conclusion was withdrawn.)

## The main result this pass
The one unconditional K>1 arithmetic input on the prime gap sequence — Lacasa
et al. (arXiv:1802.08349) forbidden mod-6 gap-blocks, counted exactly by
3^m − 2^{m+1} at order m — **does not reach the fold**. The fold reads the parity
string `h[j]=((p_{j+1}−p_j)/2) mod 2`; the mod-6→parity projection destroys the
forbidden structure at every order because per coordinate the free gap part is a
bijection. Claim `lacasa-mod6-forbidden-blocks-parity-invisible` (proved, all m;
mechanical confirmation queued at `code/scholar/lacasa_parity_projection_check.py`).
Board post `teams/posts/scholar_lacasa_parity_invisible.md`.

This upgrades a previously-recorded *conjecture* (the transfer note's general-m
case was "pending mechanical check, do not cite"; it is in fact an argument, and
is now cited as proved).

## Where every source-route to a K>1 prime input lands
Three walls, and every source falls on one:
- **(a) Mod-6 structure, dies at the parity projection.** Lacasa (this pass).
- **(b) Mod-4 structure but non-constant ⇒ parity-barred.** Wu (length-k pattern
  frequencies open, only constant patterns unconditional via Shiu/Maynard); Lau
  (even one non-constant pair beyond reach); ABGS (pair-frequency open,
  L-function-inaccessible). These are the *readable* inputs, and they are the
  conjectural ones.
- **(c) Exists in the prime index/value, transfer absent.** Mauduit–Rivat
  (digit-sum of p equidistributed, unconditional, power-saving), Matomäki–
  Radziwiłł / MRTF / Green–Tao (value-domain cancellations). Correct theorems,
  inert as proof inputs because h encodes mod-4 gap structure, not primes-index
  values, and no reduction to h's submask-window correlations is given.

## Additional sources priced (all already digested; confirmed correct here)
- **Wu (arXiv:1908.07095)** — sharpest statement of the K>1 parity barrier: only
  constant equal-residue patterns are unconditional; the non-constant ones needed
  for switches are open at every length ≥ 2. Confirms wall (b).
- **Lau (arXiv:2409.12819)** — even a single non-constant length-2 pattern is
  beyond current methods; the count bound needs squarefree modulus, which 4=2² is
  not, so it cannot supply the switch input. Wall (b), with the "true theorem
  whose hypotheses fail here" flag.
- **LOS sawtooth (2018/2020)** — the averaged-over-moduli equidistribution is
  over q, not over the fold-time n; transfer to the fixed h is absent. Supports
  the density-1/averaged framing at best, conjecturally.
- **Freiberg (arXiv:1005.4703), BFTB (arXiv:1311.7003)** — equal-residue side
  only; strengthen closed door 2 (arbitrarily long, now bounded-gap, constant
  runs in h). Wrong direction for the switch, correct as negative on any
  "h varies enough" hypothesis.
- **Mauduit–Rivat, Green-notes (binary case)** — the paradigm of a weak
  unconditional prime input, but the statistic is the digit sum s_q(p), not h;
  does NOT close request `walsh-spectral-subset-b904`. Inert as a proof input.

## Sources that do not help (verified, do not re-read for the reopened question)
- **Rampersad–Wiebe (arXiv:2309.04012)** — genuinely useful only as the record
  that its run-length transform is NOT the submask-XOR fold (`rw-not-the-
  submask-xor-fold`); its binomial sums are over k, not XORe over submasks; its
  only growth statement (≈1.207^r) is a caution, not a bound on Φ.
- **Allouche–Shallot, Szechtman, Mestrović (Lucas survey), Hofer (Pascal mod 2)** —
  the Lucas/submask machinery Φ rests on; no weight statement for the fold.
- **Chase random-Gilbreath, Odlyzko, encyclopedia-Gilbreath** — heuristic
  ground truth / background; out of scope per GOAL.
- **Pivato–Yassawi / Takei (Rule-90 randomization)** — proved but need a
  finite-prefix transfer this library does not have; recorded, not usable.

## Contradictions with recalled memory
None found. Cognee is empty (404/409 on recall this pass), so the on-disk claim
ledger is authoritative. The librarian's pass-2 correction (Shiu is sourced, not
a cookie-error stub) is consistent with the claims ledger and unchanged here.

## What the run still lacks
The reopened question stays open as an unconditional arithmetic theorem:
E[S(n)²] = O(n) on the prime gap-parity string h, equivalently a submask-window
second-moment / Walsh bound strictly weaker than pointwise switch density
(request `walsh-spectral-subset-b904`). The geometry side is proved
(`fold-distance-enumerator-On`); the primes input is measured (`n40000-second-
moment-density1-measured`); no source answers the proof. This is in-house
computation / a new theorem, not a library gap.
