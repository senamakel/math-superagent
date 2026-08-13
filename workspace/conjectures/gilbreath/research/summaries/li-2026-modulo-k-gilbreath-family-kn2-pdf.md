# Li 2026 — The Modulo-k Gilbreath Family (full text obtained)

**Full text:** `research/sources/li-2026-modulo-k-gilbreath-family-kn2-pdf.full.md`
**Source URL:** https://zenodo.org/records/19522976 (record) / https://zenodo.org/records/19522976/files/kn%2B2.pdf (PDF)
**Complete text on disk** (240.8 kB PDF → 7.9 kB Markdown). Zenodo preprint v2, 9 Mar 2026, Dong Li (TH Fire Test Company). The author's `kn+2.tex` is also on the record. **Not peer-reviewed; 0 citations.**

## What it claims (verified against the PDF)

- **Conjecture 2.1 (Modulo-k Gilbreath Conjecture).** For odd `k`, let `P(k)` be the
  ordered primes `p ≡ 2 (mod k)` (`p1 = 2`). Build the difference triangle
  `d_{i,0} = p_i`, `d_{i,j} = |d_{i,j−1} − d_{i+1,j−1}|`. Then there is `J` with
  `d_{1,j} = k` for all `j ≥ J` — the leading entry **stabilises to k**.
  Classical Gilbreath is `k = 1`.
- Mechanism offered: **modular invariance** — every non-initial term is `≡ 2 (mod k)`,
  so consecutive differences are `≡ 0 (mod k)`, rows have shape `(k, 0 mod k, ...)`
  after the first, and `|k − m| = k` iff `m ∈ {0, 2k}` mod k — the exact analogue
  of the run's `{0,2}` reduction for the prime case.
- **Theorem 5.2 (Fault tolerance).** For `a5 = 5k+2`, `a7 = 7k+2`: leading-entry
  stability survives so long as at least one of `a5, a7` stays prime; `gcd(5k+2, 7k+2)
  = gcd(5k+2, 2k)` forces `m | 2k`, and `m | k` contradicts `m | 5k+2` since
  `5k+2 ≡ 2 (mod m)` — so no prime `m > 2` divides both. The argument holds as
  printed.
- **Verification:** all odd `k < 100,000`, presumably by direct triangle computation
  (the digest does not give the depth per k — treat the range as claimed, not
  independently checked).
- Definition 5.1: "inadmissible residue classes" — a residue `c (mod m)` such that
  `k ≡ c (mod m)` forces some sequence entry to be a proper multiple of m,
  disrupting the localised stability.

## Bearing on this run

- The generalisation ROOT.md committed to, made precise with a statement the
  oracle can test: **fix odd k, take primes ≡ 2 (mod k), check the leading entry
  stabilises to k**. The run's own oracle (row generator, exact integers,
  `code/lib/gilbreath.py`) can reproduce this for small k — a natural checked
  claim for the compute phase, independent of the preprint.
- The mechanism is literally the `{0, 2k}`-block analogue of the run's `{0,2}`
  block lemma: **if a row of the k-triangle begins `k, k` or `k, 0, k`, the leading
  entry stays k while the `{0, 2k}` block persists.** Any invariant proved for the
  k=1 case via "{0,2} blocks" should generalise to "{0,2k} blocks" at modulus k,
  which is a falsifier test: an invariant that works at k=1 but provably fails at
  some odd k would be suspect.
- Status: **conjecture (asserted-by-source)**. The stabilisation is verified
  computationally by the author for k < 100,000 but not proved, and neither the
  verification nor the modular-invariance mechanism has been checked by this run.

## Contradictions to check

The summary of the earlier (v1? same record) Zenodo page said "single author,
h-index 0, 0 citations" and "odd k < 100,000" — consistent with the PDF. No
contradiction found between the record page and the full text.