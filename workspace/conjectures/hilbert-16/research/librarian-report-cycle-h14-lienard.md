# Librarian cycle report — H(4)≥28 primary + Liénard n=5 refinement

## What was added this pass

1. **Prohens & Torregrosa, "New lower bounds for the Hilbert numbers using
   reversible centers", Nonlinearity 32(1):331–355 (2019)** — full open postprint
   held. This is the **held PRIMARY source for H(4) ≥ 28** (previously only
   "reported" via surveys).
   - Full text: `research/sources/prohens-torregrosa-lower-bounds-reversible-centers-2019.full.md`
     (src https://ddd.uab.cat/pub/artpub/2019/204392/newlowbou_a2019v32n1p331.pdf)
   - Summary: `research/summaries/prohens-torregrosa-lower-bounds-reversible-centers-2019.md`
   - Claim: `h16-prohens-torregrosa-h4-28-primary` in `research/notes/claims.md`
   - Establishes (Theorem 1): H(4)≥28, H(5)≥37, H(6)≥53, H(7)≥74, H(8)≥96,
     H(9)≥120, H(10)≥142; Corollary 2: H(13)≥212 … H(43)≥2272 plus quadratic
     scaling H(N) ≥ K0·N²/(N0+1)². Method: simultaneous degenerate Hopf
     bifurcations from symmetric Darboux reversible centers (three-nest
     configurations). Peer-reviewed, full text held.

2. **Liénard degree-5 refinement** — resolved an apparent contradiction in the
   library's Liénard status.
   - Note: `research/notes/lienard-n5-rychkov-odd-vs-general.md`
   - Summary: `research/summaries/lienard-n5-rychkov-odd-vs-general.md`
   - Claim: `h16-lienard-n5-rychkov-odd-vs-general` in `research/notes/claims.md`
   - Rychkov 1975 (Differ. Uravn. 11:390–391) proved the **odd-only** degree-5
     classical Liénard system (ẋ = y−Σaᵢx^{2i+1}, ẏ=−x) has at most 2 limit
     cycles. This is NARROWER than the general (mixed-parity) degree-5 case,
     which remains OPEN per the held Llibre–Zhang 2017 survey. The old
     `h16-lienard-n5-open` claim is refined, not struck.

3. **OEIS miss recorded** — the best-known lower-bound sequence
   [4, 13, 28, 37, 53] (H(2)≥4, H(3)≥13, H(4)≥28, H(5)≥37, H(6)≥53) has NO OEIS
   entry. Note `research/notes/oeis-lloydbound-miss.md`. Recorded so nobody
   searches for it again.

## Re-confirmed unavailable (no new open copy found this pass)

- **Li–Liu–Yang 2009** ("A cubic system with thirteen limit cycles", H(3)≥13,
  JDE 246:3609–3619): only ScienceDirect (paywalled PDF); no open preprint
  located. Claimed at second hand (confirmed contexts, Torregrosa 2024 held,
  Gasull–Santana 2024 held). Status unchanged.
- **Han–Li 2011/2012** ("Lower bounds for the Hilbert number of polynomial
  systems", H(n) ≳ (n+2)²log(n+2)/(2log2), JDE 252(4):3278–3304): only
  ScienceDirect; the theorem statement is preserved verbatim in the held
  Buzzi–Novaes 2024 source. Status unchanged.
- **DRR 1994 raw 121-id catalogue**: still paywalled; only metadata public.
  The 121-graphics framing is confirmed by multiple held sources; a full
  id-by-id open/closed ledger still requires the DRR 1994 paper (or a post-2020
  authoritative table, which does not exist as a single source — recorded in
  drr-list.md).

## Memory / ledger

- Stored two verified findings to durable memory (Prohens–Torregrosa bounds;
  Liénard n=5 Rychkov-vs-general distinction). Cognee was briefly up this pass.
- Claims written to `research/notes/claims.md`; the derived `CLAIMS.md` may lag
  by one re-derivation cycle (observed 110↔111 entries), but the canonical note
  carries both new claim blocks correctly.

## What would fill the remaining top gaps

- Open PDF of Li–Liu–Yang 2009 (H(3)≥13 primary) and Han–Li 2012 (growth
  primary) — the two most valuable still-paywalled lower-bound primaries.
- DRR 1994 raw catalogue, or a post-2020 consolidated graphic-by-graphic ledger
  (neither exists as a single accessible source; requests ledger row
  `complete-current-ledger-cb3d`).
