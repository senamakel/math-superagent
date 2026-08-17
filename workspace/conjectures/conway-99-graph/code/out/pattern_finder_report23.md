# Pattern-finder report — round 23: the one post-round-22 artifact, closed

## What changed since round 22

Round 22 (00:47) declared the sequence line closed and reported that the only
post-round-21 artifacts were the C3 spectrum closed-form files (which it tooled
for the multiplicity columns `m_r, m_s`). Round 22 did **not** see the content
of `c3_spectrum_exact_verify.captured.txt`, which was 0 bytes at the time.

That file now (00:50) carries real, new content — it is the **exact
verification of the C3 triangle-graph spectrum against the actual triangle
graphs**, and it landed after round 22. Its key datum:

    C3( BvLS(243) )  has spectrum  {-3:648, 3:110, 12:132, 30:1}

## Independent re-verification (this round)

The producing script barely ran (its `spectrum_multiset` returns `{}` for the
small graphs; only the numpy path for BvLS ran), so I re-derived the number by a
fully independent route rather than trusting it:

- Built `bvls_graph()` and its triangle graph `C3` (891 vertices) from
  `lib.srg` / `lib.triangles`.
- Eigensolved `C3` via `numpy.linalg.eigvalsh`; all 891 eigenvalues are exactly
  integral (max deviation from integer < 1e-6).
- Multiplicity multiset: **{-3:648, 3:110, 12:132, 30:1}**, summing to 891 = nT.
- Degree 30 (all 891 rows equal), matching `d = 3(k/2-1) = 30`.
- Compared against the Phillips closed form for u=4 (srg(243,22,1,2)):
  `predicted == actual : True`.

File: `code/out/pf_indep_c3_bvls_verify.py`, capture
`code/out/pf_indep_c3_bvls_verify.captured.txt`.

## Why this is a confirmation, not a new sequence

This is a **single graph-instance spectral measurement**, not a sequence: no
index n, no extrapolating term to falsify. It confirms the Phillips C3 spectrum
closed form (claim already in the catalogue) holds *exactly* at the u=4 family
member — a useful cross-check, but it adds no term the sequence tools can
extend and no invariant that separates 99 (u=3) from 243 (u=4). Both share the
C3-not-strongly-regular fact; both satisfy the same closed-form spectrum
family.

## Verdict

- The only post-round-22 analysis artifact is now independently confirmed and
  closed. No new integer sequence was introduced.
- The sequence line remains fully exhausted (rounds 1-23): every
  parameter-determined count is a|63-governed (a=2u+1), and none separates 99
  from the controls 9 and 243.
- The only 99-specific structural values remain the **coclique bound 22** and
  the **forced n3 ≥ 3** (Makhnev conditional) — neither a sequence.

NOTHING FURTHER is available from the sequence tools.

## Files
- `code/out/c3_spectrum_exact_verify.captured.txt` — the new post-round-22 source artifact (00:50).
- `code/out/pf_indep_c3_bvls_verify.py` / `.captured.txt` — this round's independent re-verification.
- `code/out/pattern_finder_report22.md` — prior state.
