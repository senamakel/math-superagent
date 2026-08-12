# Alekseyev 2026, PDF version — same paper as the HTML

**Source:** arXiv:2601.17832 [math.NT] PDF. Full text: `[[alekseyev2601_pdf.full]]`.
This is the PDF rendering of the same paper digested in `[[alekseyev_diophantine_sigma_html]]`
— do not re-summarise; the two differ only in rendering (this PDF preserves the raw
Theorem statements the HTML mangles).

## What this rendering adds (Theorem 3.1, the explicit shortcut used for abundance)

**Theorem 3.1 (OEIS).** For integers d and ℓ > 0, if 2^ℓ − d − 1 is prime then
n = 2^{ℓ−1}(2^ℓ − d − 1) satisfies σ(n) = 2n + d. (The m=2^{ℓ−1} shortcut: a′−c′ =
2^ℓ−1−d must be prime.)

- This is the abundance-eq shortcut (perfect: σ(n)=2n, d=0; near-perfect d=±1).
- Not needed for hemiperfects (which are 2σ=(2k+1)n, i.e. a=2, c=0 — not of the
  σ=2n+d form). Keep as the source's own worked instance of the §3.1 shortcut.

Theorems 3.2 and 3.3 (prime-wheel pruning and completeness) are stated in full and
proved — same content as the HTML rendering. See `[[alekseyev_diophantine_sigma_html]]`
for the digest and the one claim block `alekseyev-tree-search-complete` for this problem.

```claim
id: alekseyev-theorem31-shortcut
statement: For integers d and ell>0, if 2^ell - d - 1 is prime then n = 2^(ell-1)(2^ell-d-1) solves sigma(n)=2n+d; the shortcut n'=p^k forces p | (a'-c').
hypotheses: 2^ell - d - 1 prime
holds-here: no
status: proved (Alekseyev 2026, Thm 3.1)
bearing: PE241's equation is 2*sigma(n)=(2k+1)n (c=0 form, a=2), not sigma(n)=2n+d; the shortcut is the same-paper illustration of the method, not the run's equation. Not load-bearing for the hemiperfect sum.
bearing: illustrates the shortcut machinery behind the complete tree-search; not load-bearing for the hemiperfect sum
anchor: research/sources/alekseyev2601_pdf.full.md
```
