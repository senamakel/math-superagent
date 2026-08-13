# Odlyzko 1993 — author's LaTeX source (cleaner text of the paper)

**Full text:** `research/sources/odlyzko-1993-iterated-differences-latex-source.full.md` [[odlyzko-1993-iterated-differences-latex-source.full]]
**Source URL:** https://www-users.cse.umn.edu/~odlyzko/doc/arch/gilbreath.conj.tex (author's own TeX)
**Published:** Math. Comp. 61 (1993) no. 203, 373–380; received 15 Jul 1992; dedicated to D. H. Lehmer.

## What it establishes

This is the author's LaTeX of the same paper held as PDF in
`research/sources/odlyzko-1993-iterated-absolute-differences.full.md`; the
cleaned text is the better OCR of the two. The substantive content is already
digested in `research/summaries/odlyzko-1993-iterated-absolute-differences.md`
(definitions, block lemma with constant 1, mod-4 linearization eq.~(2.2),
verification to 10^13, G-table). What this file adds that the PDF digest
records:

- **The block lemma, exact words** (Introduction): "If for some *N* we find a
  *K* such that `d_K (1) = 1` while `d_K (n) = 0` or 2 for all `1 ≤ n ≤ N`,
  then we can conclude that `d_k (1) = 1` for `K ≤ k ≤ N + K−1`." A `{0,2}`
  run of length N−1 after the leading 1 protects **N rows** — coefficient 1.
  This is the primary statement the run's `odlyzko-block-lemma-exact`
  (constant 1, n+1 rows for a block of length n) is consistent with.
- **Killgrove–Ralston verification claim as Odlyzko restates it**: "verified
  for k ≤ 63,419, that is for all primes < 792,731" — the latter digits differ
  slightly from the K–R paper's own < 792,722 figure; the k ≤ 63,419 count is
  unambiguous and common to both.
- **Hardware/method** (§4, in the excerpt): segmented sieve in blocks of
  5×10^5–8×10^6, 50–75 full-array iterations over blocks then isolated
  processing of entries > 2, an SGI 4D-220, 5–20 MB, several months single
  processor, ~2 s per 10^6-length interval. Also tested primes near 10^50 (436
  iterations suffice) and probable primes near 10^100 (1417 iterations).
- **Caveat** (§1): the 10^13 computation "cannot be fully guaranteed" — one
  error found and corrected (block M = 8.972168×10^12: spurious g(n) = 914
  from a nonexistent gap 1158; correct value 261).

## Hypotheses / bearing

The block lemma's hypotheses are: row K is 1 followed by N−1 entries in {0,2},
absolute-difference iteration — exactly the run's consumption setup; holds
here. Endorses the exact constant 1, contradicting nothing the run holds. The
method section documents why brute-force verification to depth is expensive
(~5×10^22 numbers at k ~ 3.4×10^11) — quantifying why the deliverable must be
a proof, not a deeper run.

## Source status

Author's own TeX; identical in content to the AMS PDF. The two files
cross-corroborate each other; the run's `odlyzko-block-lemma` /
`odlyzko-verification-1993` / `odlyzko-mod4-linearization` claims rest on both.