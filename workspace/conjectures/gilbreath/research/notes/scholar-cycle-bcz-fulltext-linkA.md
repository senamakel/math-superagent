# Scholar cycle — BCZ filtered-rays full text verified; Link A still unrun

## What this cycle confirmed (the one genuinely-new digestible item)

**BCZ 2024 "Filtered rays" is now read in FULL PDF** — the previous
`incomplete-source` flag referred only to the arXiv abstract-page copy
(`...-filtered-rays.full.md`). The FULLPDF
(`bhat-cobeli-zaharescu-filtered-rays-FULLPDF.full.md`) contains all six
theorems, the two lemmas, the construction, and Table 1. The canonical digest
(`summaries/bhat-cobeli-zaharescu-2023-filtered-rays-iterated-abs-diffs.md`,
claim `bcz-2023-left-edge-stabilization`) is correct and complete; this cycle
replaced the stale `summaries/bhat-cobeli-zaharescu-filtered-rays.md` that
still carried the `incomplete-source` flag. Nobody should re-read that file
for content.

Key verified content (at most two lines each):
- Thm 2: for binary u, left-edge map T(f)(X)=f(X/(1+X))·(1/(1+X)) over F2[[X]],
  and T^2 = id (Υ²(u)=u for binary u); finite analogue Thm 3 mod X^N.
- Thm 4: Υ⁶(u)=u for all binary u (helicoid one layer) ⟺ u has ≤1 champion (necessary, not sufficient).
- Thm 5: almost all binary u of length N have every ray's 0/1 proportion within
  [1/2−ε,1/2+ε] — the ONLY proved balance theorem, and only for GENERIC binary
  rows, not the primes' specific halved bits.
- Thm 6: any prescribed even-indexed western edge realized by some square-prime
  sequence (anti-universality witness, like Eppstein/Colonna).
- Conjecture 2 (prime ray balance ν_d(n)=n/2±c√n) UNPROVED; Table 1
  |#0−#2|≤431/78,496 per ray is strong numerical support only.

## Bearing (what changed, what did not)

- Table 1 is a **second independent corroboration** of Route B's supply density
  ν₂ ~ n/2 (the run's own `nu2_granville_check` being the first). Two-source
  corroboration is now recorded (`bcz-2023-left-edge-stabilization` + `granville-nu2-density-measured`).
- Thm 5's balance is proved for GENERIC binary rows; it does NOT transfer to the
  primes' specific halved-gap bits, so it motivates but does not prove the
  supply bound. Do not over-cite it.
- The F2 involution T²=id is an exact structural constraint on any future
  halved/mod-2 invariant.

## What is still open on Route B

- The supply-side lower bound ν₂(q_{n−1}) ≥ c·n (c>0) remains the entire open
  content. Lemma 5.4 is re-derived/proved on the even domain and the failing
  side is validated non-vacuously; the demand side (α=0.525) is unconditional
  via BHP; the ν₂ transfer (rising-sea's w = #{gaps ≡ 2 mod 4}, nu2/w ∈
  [0.689,0.867]) is measured but only a hunch, not a proved transfer.
- **Link A (`v ≤ g*_n`, `code/out/verify_lemma54_v_le_gstar.py`)** remains the
  one un-run cosmetic item: it needs `exec`, which this scholar run does not
  have. The served-v form (what the primes actually measure) is proved/checked,
  so this does not block Route B.

## No new contradiction with recalled memory

Everything verified this cycle agrees with the established ledger. The only
stale flag (`incomplete-source` on BCZ) is repaired, not amplified.
