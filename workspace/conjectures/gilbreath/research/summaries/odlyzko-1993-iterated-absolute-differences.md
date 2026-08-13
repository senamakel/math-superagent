# Odlyzko 1993 — Iterated absolute values of differences of consecutive primes

**Full text:** `research/sources/odlyzko-1993-iterated-absolute-differences.full.md` (PDF-derived) and `research/sources/odlyzko-1993-iterated-differences-latex-source.full.md` (author's TeX, cleaner OCR).
**Source URL:** https://www.ams.org/journals/mcom/1993-61-203/S0025-5718-1993-1182247-7/S0025-5718-1993-1182247-7.pdf
**Published:** *Math. Comp.* 61 (1993), no. 203, 373–380. doi 10.1090/S0025-5718-1993-1182247-7. Received July 15, 1992. Dedicated to D. H. Lehmer.

## Content

- **(A) Definitions.** `d_0(n) = p_n`; `d_{k+1}(n) = |d_k(n) − d_k(n+1)|`. The conjecture (attributed to Proth 1878, rediscovered by Gilbreath ~1958) is `d_k(1) = 1` for all `k ≥ 1`. Parity shape: `d_k(1)` odd, `d_k(n)` even for `n ≥ 2`, all `k ≥ 1`.
- **(B) The block lemma, exact words (Introduction):** "If for some *N* we find a *K* such that `d_K(1) = 1` while `d_K(n) = 0` or 2 for all `1 ≤ n ≤ N`, then we can conclude that `d_k(1) = 1` for `K ≤ k ≤ N + K − 1`." So a `{0,2}` run of length N−1 after the leading 1 protects **N rows** — one row per block entry, linear coefficient exactly 1. This is stronger than the run's unsourced "≈ n/2 rows" (problem.md, CONTEXT.md), which appears **nowhere** in this paper.
- **(C) Verification bound.** All primes `< 10^13`; `d_k(1) = 1` for `1 ≤ k ≤ π(10^13) ≈ 3.4 × 10^11`. Table 2: `G(π(x)) = 5, 15, 35, 65, 95, 135, 175, 248, 329, 417, 481, 635` for `x = 10^2..10^13`. Largest `g(n) = 635` (least row from which 1000 consecutive entries are 0/2) at `n ≈ π(7.17716 × 10^12)`, caused by the prime gap 674.
- **(D) Methods.** Mod-4 linearization (eq. 2.2): `d_{k+1}(n) ≡ d_k(n) + d_k(n+1) (mod 4)` for `k ≥ 1, n ≥ 2` — absolute values disappear mod 4 and the triangle follows Pascal's rule. Segmented sieve in blocks `5×10^5–8×10^6`, 50–75 full-array iterations then isolated processing of entries `> 2`. Hardware: SGI 4D-220 (4× R3000 25 MHz, 128 MB), 5–20 MB used, several months single-processor, ~2 s per 10^6-length interval. Also tested primes near 10^50 (436 iterations suffice) and probable primes near 10^100 (1417 iterations).
- **(E) Reliability.** Author states results "cannot be fully guaranteed"; one error found (block `M = 8.972168×10^12`: spurious `g(n) = 914` from a nonexistent gap 1158; correct value 261).

## Claims

```claim
id: odlyzko-block-lemma
statement: If d_K(1)=1 and d_K(n) ∈ {0,2} for 1 ≤ n ≤ N, then d_k(1)=1 for K ≤ k ≤ N+K−1 — a leading {0,2} block of length N−1 protects N rows (one row per block entry; coefficient exactly 1, not n/2).
hypotheses: any triangle d_{k+1}(n)=|d_k(n)−d_k(n+1)| from an integer sequence whose row K is 1 followed by N−1 entries in {0,2}; parity shape (odd, even, ...) holds automatically for primes.
holds-here: yes — this is the run's central consumption lemma; the exact constant is N (linear), correcting the ≈ n/2 asserted in problem.md/CONTEXT.md.
status: sourced (Odlyzko 1993, Introduction; identical in the author's LaTeX source; independently in Killgrove–Ralston 1959)
bearing: fixes the protection budget: a {0,2} block of length L protects L+1 rows including the current row; consumption is linear, not geometric. Regeneration is still unproved, but the framing must use the corrected constant.
anchor: research/sources/odlyzko-1993-iterated-differences-latex-source.full.md
```

```claim
id: odlyzko-verification-1993
statement: Gilbreath's conjecture verified for d_k(1), 1 ≤ k ≤ π(10^13) ≈ 3.4×10^11 (all primes < 10^13); G(π(10^13)) = 635; max g(n) = 635 at n ≈ π(7.17716×10^12) from prime gap 674.
hypotheses: exact integer computation; primes from a segmented sieve.
holds-here: yes — the deepest published verification and the bound the run cites.
status: sourced (Odlyzko 1993, §3, Tables 2–3)
bearing: the run need not re-verify depth; the deliverable is a proof. Also documents that long computations are error-prone (one corrected error).
anchor: research/sources/odlyzko-1993-iterated-absolute-differences.full.md
```

```claim
id: odlyzko-mod4-linearization
statement: For k ≥ 1, n ≥ 2, d_{k+1}(n) ≡ d_k(n) + d_k(n+1) (mod 4) because d_k(n) is even there; the absolute-value triangle obeys Pascal's rule mod 4 (mod 2 after halving).
hypotheses: row shapes (odd, even, even, ...) — true for primes and any 2-followed-by-odd-numbers start with even gaps.
holds-here: yes — the cleanest algebraic handle on the operator; generalized in Chase–Hunter–Tao 2026 Lemma 3.10.
status: sourced (Odlyzko 1993, eq. 2.2)
bearing: candidate invariants forcing A_k(1) ∈ {0,2} are best sought at the mod-4/mod-2 level.
anchor: research/sources/odlyzko-1993-iterated-absolute-differences.full.md
```