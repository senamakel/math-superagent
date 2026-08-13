# Hwang–Janson–Tsai 2024 — Periodic minimum in the count of binomial coefficients not divisible by a prime

Source: Hsien-Kuei Hwang, Svante Janson, Tsung-Hsi Tsai, arXiv:2408.06817v1
(13 Aug 2024); published version Math. Comp. (2025), DOI 10.1090/mcom/4108.
Full text held at `research/sources/hwang-janson-tsai-parity-count-2024.full.md`.

## What it establishes

Let `F_p(n)` be the number of binomial coefficients C(m,k), 0 ≤ k ≤ m < n, not
divisible by a prime p. For p = 2 this is the number of **odd entries in the
first n rows of Pascal's triangle** — the object the binary-digit thread's scan
counts, OEIS A006046.

**Theorem 2.1** (p-ary recurrence, proven from Volodin's digit formula):
`F_p(n) = Σ_{0≤j<p} (p−j) F_p(⌊(n+j)/p⌋)` (n ≥ p), initials `F_p(j) = C(j+1,2)`
for j = 1..p−1. For p = 2: `F_2(n) = 2 F_2(⌊n/2⌋) + F_2(⌊(n+1)/2⌋)`, with
F_2(1) = 1, so `F_2(2^m) = 3^m` exactly (Stein's F_p(pn) = C(p+1,2)·F_p(n)).

**Theorem 2.2** (exact periodic representation, generalising Stein's
continuity): with `ϱ_p = log_p C(p+1,2)` (so for p=2, ϱ = log_2 3 ≈ 1.585):

```
F_p(n) = n^{ϱ_p} · 𝒫_p(log_p n),   𝒫_p(t) = A^{1−{t}} φ(p^{{t}−1}),  A = C(p+1,2),
φ(Σ_j b_j p^{−j}) = ½ Σ_j (b_j / A^j) Π_{1≤i≤j} (b_i + 1)   (2.11)
```

𝒫_p is continuous and 1-periodic; `α_p = limsup F_p(n)/n^{ϱ_p} = max 𝒫_p = 1`
for all p; `β_p = liminf = min 𝒫_p` and `C(p+1,2)^{−1} ≤ β_p < 1`.

**Theorem 1.1** resolves Wilson's conjecture (Acta Arith. 83 (1998) 105–116)
for all odd primes 3 ≤ p ≤ 113: `β_p = B_{ξ,η}` with the explicit closed form
(1.13) and the (ξ,η) table; e.g. β_3 = 2^{log_3 2 − 1} (Franco), β_5 = (3/2)^{1−ϱ_5},
β_11 = (59/44)(22/31)^{ϱ_11}, and β_113 = (7780/2147)(226/555)^{log_113 6441} ≈
0.68432. Verified numerically to p ≈ 7907; a proof for **all** odd primes remains
open; `β_p → 1/2` as p → ∞ (Wilson's (1.9)) with the refined estimates
`ξ ∼ log_4 p`, `η ∼ p/(4 log_2 p)` (Section 6.2).

**Problem 1.2** — the case the run cares about, p = 2: **no exact expression
for β_2 is known or even conjectured** (β_2 ≈ 0.812556, the Stolarsky–Harborth
constant, Harborth's 1977 value; only its many digits are known, cf. OEIS
A077464). The p = 2 minimum point ŝ_2 is uncharacterised.

## Relevance to this run

1. **Completeness oracle for the binary-digit thread's scan.** The thread's
   first step is an odd-triangle multiplicity scan to n ≤ 2^18. Theorem 2.1
   gives the exact number of odd entries with m < 2^18: F_2(2^18) = 3^18 =
   **387,420,489** — an independent, exact benchmark the scan's total must
   reproduce (via the recurrence, not by hand-counting). The thread's earlier
   estimate (~3.5·10^7) was off by ~11×.
2. **Correction to the thread's stated scan domain.** Odd *values* can sit in
   even rows: 15 = C(6,2) is odd with even row 6 (k = 10₂ ⊆ 110₂). So the scan
   must run over ALL n ≤ 2^18 with k ⊆ n (Lucas mod 2), not "odd n" only.
   F_2 counts all such pairs exactly, which is why the 3^18 benchmark applies.
3. **The sparsity-vs-multiplicity distinction stands.** HJT quantifies how many
   entries are odd (n^{log_2 3} with an explicit periodic factor) but says
   nothing about how often one integer *value* recurs across rows — the
   binary-digit thread's actual question remains unstudied in this literature,
   so the thread's novelty premise survives, now with exact counting machinery
   underneath it.
4. For the general p-ary story (p odd, multinomial analogues, Problem 1.4) the
   paper gives the modern exact treatment replacing Wilson 1998; Wilson's paper
   itself is paywalled at EuDML and its content relevant to us is subsumed by
   Theorem 1.1.

## Status

`asserted` — sourced from the arXiv primary, not independently re-derived.
Theorem 2.1 and the digit formula (2.11) are directly checkable in this
workspace and should be (they are the oracle for the odd-triangle scan).

```claim
id: hjt-parity-count-exact-periodic
statement: F_p(n) (binomial coefficients with m<n not divisible by p) satisfies
  F_p(n)=Σ_{0≤j<p}(p−j)F_p(⌊(n+j)/p⌋), F_p(j)=C(j+1,2), hence the exact periodic
  representation F_p(n)=n^{ϱ_p}𝒫_p(log_p n) with ϱ_p=log_p C(p+1,2), 𝒫_p
  continuous 1-periodic and explicitly given (Thm 2.2); for p=2, F_2(2^m)=3^m
  exactly. Wilson's conjecture on the liminf minimum β_p is proved for all odd
  primes 3≤p≤113 with the closed forms (1.13); β_2 (Stolarsky–Harborth constant
  ≈ 0.812556) has no known closed form (Problem 1.2).
hypotheses: p prime (Theorem 2.1/2.2: any integer p≥2); Theorem 1.1: p odd,
  3≤p≤113 (with the proven/exhaustive numeric partition checks inside the proof).
holds-here: yes — p=2 is exactly the odd triangle of the binary-lucas-submask
  thread; gives F_2(2^18)=3^18=387420489 as an exact completeness benchmark
  for the planned odd-entry scan, and confirms the scan must cover all n (even
  rows contain odd values, e.g. 15=C(6,2)), not just odd n.
status: asserted
bearing: grounds the binary-digit thread's first step with an exact count oracle;
  establishes the sparsity side (count of odd entries) with full precision, so
  the thread's value-multiplicity question is precisely what remains unstudied.
anchor: research/summaries/hwang-janson-tsai-parity-count-2024.md
```

## References surfaced by this source (already in library unless noted)

Fine 1947 (AMM 54, 589–592) — binomial coefficients mod p, "almost all
divisible"; Harborth 1977 (Proc AMS 62, 19–22) — held
(`research/sources/harborth-1977-odd-binomial-count.full.md`); Stein 1980
(Proc AMS 80) — being fetched; Stolarsky 1977 (SIAM J. Appl. Math. 32,
717–730) — paywalled (epubs.siam.org), content carly attested in this summary's
account of α_2=1, 0.72 ≤ β ≤ (9/7)(3/4)^θ ≤ 0.815; Wilson 1998 (Acta Arith. 83,
105–116) — paywalled (EuDML), subsumed by Thm 1.1 here.