# Independent compact-sequence audit (2026-08-18)

## Method
Read the existing inspection and survey first, then independently loaded the compact integer artifacts and ran exact rational homogeneous recurrence fitting through order 12 with `code/pattern_hunt/independent_compact_audit.py`. This is a bounded diagnostic, not a proof of non-recurrence. The relevant structural candidates were also checked against the existing exact analyzers; no conjecture survived that required a fresh extension.

## Exact output

No nontrivial fixed-coefficient recurrence of order ≤12 was found for:

- `psi_exact.txt` (25 terms)
- `psi_residues.txt` (400)
- `c1_terms.txt` (400)
- `lmin.txt` (400)
- `dj_raw.txt` (1145)
- `topelitz_defects.txt` (400)
- `vr_rungaps.txt` (153)
- `ext_recurrence.txt` (40)
- `extrecur_res.txt` (400)

`counts.txt` produced only the tautological linear recurrence family for the already-established sequence `k+1`; this is not a new finding.

The prior exact checks remain the only surviving regularities: `count(k)=k+1`, `c1(k)=1+floor(k/phi^2)`, `Lmin(k)=k+NextFib_strict(k)-1`, the recorded A019587/Wythoff identification for `d_j`, Wythoff run starts/gaps, and the finite Fibonacci-boundary Toeplitz-zero pattern. I found no genuinely relevant unsettled compact sequence yielding an exact new regularity, so no conjecture was proposed and no extension was warranted.

## Decision

**NOTHING FURTHER.**

Run bearing on the claim: the output is evidence only for the negative bounded recurrence search; it does not establish the global absence of recurrences. Complexity: polynomial in the stored sequence lengths, with exact symbolic linear algebra.
