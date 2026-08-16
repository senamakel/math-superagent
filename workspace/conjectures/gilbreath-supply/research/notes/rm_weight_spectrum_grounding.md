# Grounding: RM weight-spectrum problem is open (now sourced)

The `anf-mobius-reed-muller` approach is refuted on the ground that its engine —
Reed-Muller weight enumeration on the ANF support of a sliding window — hands
the work to "the RM weight-spectrum problem, which is open (Carlet 2023/24)".
That claim was previously citation-only: no primary source on it sat on disk.
This note grounds it with two now-downloaded primary sources.

## Claim block

```yaml
id: rm-weight-spectrum-middle-orders-open
status: asserted (source-backed), holds-here yes
holds-here: The fold image wt(Phi_n h) is the weight of a degree<=r Boolean
  function's truth table; per Abbé-Shpilka-Ye (arXiv:2002.03317) the exact
  weight spectra of RM(r,m) are known only for r in {0,1,2,m-2,m-1,m}, and the
  orders r in {3,...,m-5} are open. So no ready weight-spectrum lower bound on
  wt(Phi_n h) exists in that order range.
evidence_class: sourced claim (secondary survey + primary paper)
falsifies: A weight-spectrum or weight-distribution result for a general order r
  strictly inside (3, m-5) — not of the RM(m-c,m) penny-packet type — would
  change this picture.
answers: walsh-spectral-subset-b904  # DOES NOT close it; confirms the request's
  premise that the bound must come from foldspecific structure, not a ready RM
  spectrum.
```

## Source status

- **Downloaded:** `research/sources/abbe_shpilka_ye_reedmuller_survey.full.md`
  (arXiv:2002.03317) — canonical survey of RM weight enumerators; catalogs
  extreme known spectra, flags middle orders open.
- **Downloaded:** `research/sources/lou_wang_weight_spectrum_RMm6.full.md`
  (arXiv:2406.03803) — primary paper; states the opening fact "weight spectra
  of RM(r,m) were unknown for r in {3,...,m-5}" and settles c=6.
- **Not in library, paywalled:** Carlet & Solé, *Weight spectrum of two
  families of RM codes*, Discrete Math 2023, DOI 10.1016/j.disc.2023.113568.
  A guessed arXiv id (2306.04731) fetched an unrelated quant-ph paper and was
  rejected; recorded at `research/sources/DELETED_wrong_arxiv_carlet_sole.md`.

## Implication for SUPPLY

Neither source gives a lower bound on `wt(Phi_n h)` for a **single** folded
image from an arithmetic input on `h`. The generic weight-enumerator decay in
the low-degree regime (Abbe-Shpilka-Wigderson) confirms the fold image *should*
be heavy for almost all inputs — consistent with the proved Binomial(n-2,1/2)
law — but no deterministic per-image bound from an input hypothesis exists.
The request `walsh-spectral-subset-b904` stands open, and this grounding hardens
the negative that made `anf-mobius-reed-muller` a dead end for a real reason,
not a guess.
