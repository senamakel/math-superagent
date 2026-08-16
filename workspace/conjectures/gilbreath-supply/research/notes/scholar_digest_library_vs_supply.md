# Scholar digest — the reference library against SUPPLY

Author: scholar. Date: this pass. The library is mature: every full text has a
digest, every digest carries its claim blocks, and the derived `research/CLAIMS.md`
holds ~90 claim rows. This pass re-read the whole library against the run's
single hypothesis (GOAL.md: **can the fold `Φ` do work the switch-density form
cannot see**), digested the one remaining stub (`rowland_nonzero_binomial_modp`),
and stored the durable source-backed findings in Cognee. Report of what the
library establishes, what it does not, and what each source's bearing is.

## What the library establishes, claim by claim

### The parity barrier — why the switch-density reduction is a dead end
- **Ash–Beltis–Gross–Sinnott 2011 §1 p.401** (primary, verbatim): the
  asymptotics of consecutive-prime-pair ordered-residue frequencies mod m —
  Problem 1.1 — *"is wide open, and cannot be treated using L-functions"*.
  §9 leaves even the equality of class frequencies open. Claims
  `abgs-p1-wide-open`, `abgs-pair-frequency-equality-open`. This is the exact
  arithmetic input the reduction needs.
- **Lau 2024**: even a single non-constant 2-term pattern mod 4 ((1,3)/(3,1)) is
  *not known to occur infinitely often*. Claim `lau-nonconstant-pattern-open`.
  Strongest clean statement of how far we are from positive switch density.
- **Equal-residue side is fully understood and is the WRONG direction.** Shiu
  2000 (quantitative), Maynard 2016 Thm 3.3 (positive density), Freiberg 2011
  (short gaps), BFTB 2015 (bounded gaps) all establish the *same-class*
  direction — long constant runs in the gap-parity string `h`. These refute
  closed doors 1–3 *with density*; none touches the differing side SUPPLY needs.

**Bearing:** the reduction of SUPPLY to positive mod-4 switch density lands on an
L-function-inaccessible open problem. This is the entire justification for the
fold route, and it is a sourced, verified fact, not a belief.

### The five closed doors — why "h is complicated enough" cannot work
(problem.md, verified against sources here.) All-ones (kernel) ⇒ ν₂=O(1);
Shiu ⇒ long zero runs in h; Thue–Morse ⇒ aperiodic yet sublinear; balanced
anti-dyadic ⇒ wt∈{1,2}; primes-not-periodic true but inert. The unifying
obstruction: `Φ` has low-weight images on structurally rich inputs, so
complexity-of-`h` hypotheses are refuted as a family. Stored as durable memory.

### The fold's structure — the object the run must exploit
- **Fold-rank correction (computed+checked, the strongest evidence class).** The
  operative `Φ_n` is `(n−2)×n`, rows `d=2..n−1`, rank `n−2` (full row rank),
  nullity 2, `ker = span(even-alt, odd-alt)`, all-ones in the kernel. Supersedes
  the inherited "rank n−3, nullity 1" (which fits no row convention). Corollary:
  for uniform h, `wt(Φ_n h)` is exactly `Binomial(n−2, 1/2)`, E=(n−2)/2 — SUPPLY
  holds w.h.p. for random h (Chernoff), so the difficulty is entirely the fixed
  prime string. Claim `fold-rank-n-minus-2-binomial-proved`.
- **Lucas/submask (proved).** `C(d,i) mod 2 = 1` iff `i` binary-submask of `d`;
  the depth-d cell is an XOR over the `2^{s₂(d)}` submasks of d. This confines
  `Φ` to reading `h` only along binary-submask XORs — `submask-read`: any usable
  arithmetic input must be a statement about those specific linear forms.
- **2-regular machinery (Rampersad–Wiebe full text).** Corrects the earlier
  overstatement: RW analyses sums of *products* of binomials via run-length
  transforms, NOT the submask-XOR zeta transform that is SUPPLY's fold. RW gives
  **no** weight bound on the fold. Also records a caution: natural binomial-F2
  sums need not grow linearly (the Thm-5 average is ~1.207^r, super-polynomial).
- **Bacher (transfer unchecked).** Determinant/LU structure is for the *symmetric*
  square Pascal matrix; the fold is the rectangular offset `Φ_n`. Transfer to
  `Φ_n` is *in spirit only* and must be verified by direct computation before any
  claim rests on it.

### The weakest-input candidate — and its hard limit
- **Pivato–Yassawi 2006 Thm 7.1** (verified verbatim): `Φ=1+σ` randomizes µ
  (weak-* to Haar at density-one times) **iff** µ is Lucas mixing — correlation
  decay of every character along binary-submask unfoldings. Sharp (weakest)
  ergodic condition, and it reads exactly the submask sets Lucas makes Φ read.
- **BUT it does not close the request.** It is a measure-level ergodic
  equivalence, not a finite bound `wt(Φ_n h) ≥ c·n` for one fixed string at one
  depth. The finite-prefix transfer (a) the prime-gap empirical measure is Lucas
  mixing, and (b) quantitative weak-*→weight stability — is absent and is the
  run's single largest missing tool. The request `walsh-spectral-subset-b904`
  stays **open**.

### The Walsh side — sharp bounds, but not the engine
- Meshulam 2003 Thm 1.2, Tao 2005 Thm 1.1, Donoho–Stark/MOP 2004 Thm 1.1 fix the
  sharp Walsh-basis uncertainty trade-offs on the Boolean cube `(Z/2)^n` — the
  exact coordinate system where the fold lives. Equality cases are subgroup
  indicators, which are precisely the structured low-weight inputs the closed
  doors forbid. **Cannot be the engine:** `wt(Φ_n h)` is a co-domain image weight,
  not a Walsh-basis support size, and the extremals are the obstruction.

### Measured (not theorems) — recorded so nobody builds on them as proof
Mean `ν₂/n` of the primes rises 0.4394→0.4973 (n=100→4000), while Thue–Morse
falls and all-ones is 0 — the averaged signal is prime-specific (negative
controls pass). At N=40000 mean=0.499658, tail-min of ν₂/n over [X,N] rising
(evidence for ν₂/n→1/2, not a proof). ABGS mod-4 data: switch pairs 57.5% vs
equal 42.5% (finite range). LOS conjecture switch pairs strictly dominate at
every x — *heuristic only*, not a proof of the arithmetic input.

## Sources that do NOT help (so nobody re-reads them)
- **OEIS A271223 / A004603 / A004595 / A307332** — base-4 digits of quadratic
  irrationals/π/e and a fractal ternary sequence; nothing to do with the fold.
  (Notes already say "do not re-read".)
- **`odlyzko_gilbreath`** — a bibliography index page, leads not evidence.
- **`granville_martin_prime_number_races`** — a duplicate mirror of the canonical
  `_prime_races` paper.
- **The five `citations_w...` files** — citation graphs, explicitly not evidence.
- **Rowland 2011** (now digested) — counts nonzero binomials mod p^α on a row;
  background for the submask count `2^{s₂(d)}`, gives no weight bound on the
  fold.

## Contradictions flagged
- **ABGS vs LOS emphasis (not factual):** ABGS leave even the frequency limit
  open; LOS conjecture switch dominance at every x. Both can hold; neither is a
  theorem.
- **Rampersad–Wiebe overstatement corrected:** `rw-not-the-submask-xor-fold`
  supersedes the earlier "this is the fold Φ itself" gloss.
- **Bacher rank note vs the corrected rank:** Bacher concerns square symmetric
  Pascal matrices, independent of the (corrected) rectangular fold rank; do not
  import "rank n−3" from any old note.

## The open gap, restated precisely
The finite-prefix transfer is the single largest missing tool: a quantitative
`wt(Φ_n h) ≥ c·n` (all n ≥ N₀, or on a density-1 set) from an arithmetic input
on the prime-gap-parity prefix. Its two halves — (a) is the prime-gap empirical
measure Lucas/harmonically mixing, and (b) quantitative weak-*→weight — appear in
no source in the library. This is what the next loop should attack; it is
in-house computation (structure-of-`Φ` plus prime-gap correlation), not a new
literature fetch, per directive 7's search freeze.

## Durable memory stored this pass
The parity barrier/ABGS synthesis; the Pivato–Yassawi Thm 7.1 statement + the
finite-transfer caveat (request stays open); the uncertainty-principle Walsh-side
bounds + why they cannot be the engine; the Rampersad–Wiebe does-not-cover-the-fold
correction; the fold-rank correction; the Bacher transfer caveat; the five closed
doors; the mod-4 switch data + LOS heuristic; the measured captures; the
R-finite-verified correction + single-sparse amplification; the equal-residue side
synthesis; the Shiu source-status caveat; and the Rowland digestion.
