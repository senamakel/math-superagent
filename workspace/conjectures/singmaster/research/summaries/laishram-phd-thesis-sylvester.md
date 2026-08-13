# Laishram PhD thesis — Sylvester refinements for products of consecutive integers (corrected route to Laishram–Shorey 2004)

Source: Shanta Laishram, "Some Topics in Number Theory (Refinements, Extensions
and Generalisations of a Theorem of Sylvester on the prime factors of a
product of consecutive integers)", PhD thesis, Tata Institute of Fundamental
Research, Mumbai (advisor T. N. Shorey). Full text held:
`research/sources/laishram-phd-thesis-sylvester.full.md`
(https://www.isid.ac.in/~shanta/PhDThesis.pdf).

**This is the corrected route to the corrupted download.** The library's
`research/sources/laishram-shorey-prime-divisors-consecutive-2004.full.md`
holds a corrupt fetch (a topology paper, claim
`laishram-shorey-corrupt-download`). The intended source — Laishram–Shorey,
"Number of prime divisors in a product of consecutive integers", Acta Arith.
113 (2004) 327–341 — could not be fetched directly (IMPAN proxy 502, author
PDF link 404, DML-PL 503), but the author's PhD thesis **reproduces that
paper's theorems verbatim as Theorem 1.2.1–1.2.7 (ref. [28]) and the
companion greatest-prime-divisor paper Acta Arith. 120 (2005) as Thm 1.3.1
(ref. [30])**. So the theorem content of the intended source is now in the
library, with the thesis as the anchor.

## The theorems, as stated in the thesis (verbatim from Laishram–Shorey)

Notation: `∆(n,k) = n(n+1)···(n+k−1)`; `ω(ν)` = number of distinct prime
divisors; `P(ν)` = greatest prime divisor; `π(k)` = number of primes ≤ k.

- **Theorem 1.2.1 (Laishram–Shorey [28])**: Let `n > k`. Then
  `ω(∆(n,k)) ≥ π(k) + ⌊¾π(k)⌋ − 1 + δ(k)`
  except for (n,k) in an explicitly given finite set. (δ(k) is a small
  k-dependent correction; the exceptional pairs are listed in the full text.)
  This refines Sylvester's theorem `ω(∆(n,k)) > π(k)` — i.e. a product of k
  consecutive integers each exceeding k has not just one prime > k, but a
  density of distinct primes substantially above π(k).

- **Corollary 1.2.2 / 1.2.3**: follow-up bounds on ω(∆) for n > k; each
  improves Sylvester with smaller exceptional sets.

- **Theorem 1.2.4 (Laishram–Shorey [28])**: for `(n,k) ≠ (6,4)` a further
  ω(∆)-bound (exact form in full text).

- **Theorem 1.2.6 (Laishram–Shorey [31])**: Grimm's conjecture holds for
  `n ≤ p_{N₀}` and all k (computational verification range).

- **Theorem 1.3.1 (Laishram–Shorey [30])**: `P(∆(n,k)) > 1.95k` for
  `n > k > 2`; Corollary 1.3.2: `P(∆(n,k)) > 1.8k` for `n > k`. (The
  greatest-prime-divisor refinement: a run of k consecutive integers each > k
  has a prime divisor almost twice k.)

The thesis also contains the Hirata-Kohno–Laishram–Shorey–Tijdeman results
(Thm 6–8: equation (6) with 4 ≤ k ≤ 109, b = 1 impossible; Thm 9–14: perfect
power / square avoidance for products of arithmetic-progression terms), which
extend the equal-products / consecutive-block machinery.

## Bearing for this run

**Corroboration, not a new line.** The theorem family is exactly the
Sylvester-prime machinery that the run already closed as a route to
Singmaster: `sylvester-prime-machine` (refuted — redundant with
Saradha–Shorey–Tijdeman 1995 and Beukers–Shorey–Tijdeman 1999, both held) and
`consecutive-block-merge` (refuted — identical in mechanism to SST/BST). The
Laishram–Shorey refinement gives quantitative control on the **number** of
distinct primes in a consecutive block (`ω(∆) ≥ π(k)+¾π(k)−1+δ(k)`), i.e. the
*counting* side of Sylvester, where the run's existing SST/BST sources supply
the *equal-products* side. It does not overcome the uniformity wall: the
bounds are per-k (the constant depends on k through π(k)), and the witnesses
(`3003 = C(15,5)=C(14,6)` with all large primes 7,11,13 inside both blocks)
show the prime-alignment contradiction the block-merge engine hoped for does
not materialise. Keep as corroborating structure for the equal-products
reduction; do not re-propose the Sylvester engine against Singmaster.

## Status

`checked` (full text held; theorems reproduced verbatim in the thesis).
Replaces the intended-but-corrupt Laishram–Shorey 2004 fetch with real
content; the corrupt-download tombstone stays on disk so nobody re-cites the
topology paper.

```claim
id: laishram-shorey-sylvester-refinements-thesis
statement: Laishram-Shorey (Acta Arith. 113 (2004) 327-341, reproduced verbatim
  as Thm 1.2.1-1.2.7 of the author's TIFR PhD thesis): for n>k,
  omega(D(n,k)) >= pi(k) + floor(3/4 pi(k)) - 1 + delta(k) except for an
  explicitly listed finite set, refining Sylvester's omega > pi(k); and
  P(D(n,k)) > 1.95k for n>k>2 (Acta Arith. 120). Here D(n,k)=n(n+1)...(n+k-1),
  omega = # distinct prime divisors, pi = prime count.
hypotheses: n > k >= 2; k fixed (constants depend on k through pi(k)).
holds-here: yes — the hypotheses (n>k, k fixed) hold for the equal-products
  reduction; but BEARING is corroboration-only: this is the Sylvester-prime
  counting machinery already closed (sylvester-prime-machine,
  consecutive-block-merge refuted as redundant with SST 1995 / BST 1999); gives
  per-k quantitative prime-count structure, not a uniform N(a) bound; the
  witness 3003 has the large primes 7,11,13 inside both blocks, so no
  prime-alignment contradiction fires.
status: checked (thesis full text held; intended 2004 paper unavailable
  directly, theorem content reproduced in thesis)
bearing: fixes the previously-corrupted Laishram-Shorey gap with real content;
  corroborates the equal-products reduction's prime discipline; does not open a
  new route to Singmaster.
anchor: research/sources/laishram-phd-thesis-sylvester.full.md
```

## Access record for the intended paper

The 2004 Acta Arith. paper itself remains unfetched: IMPAN DOI proxy returned
502, journals.impan.pl article page 502, author PDF (ActaOmCons.pdf) 404, DML-PL
503. The thesis is the available primary-content substitute. If the paper's
exact exceptional-set list (beyond what the thesis reproduces) is ever needed,
the IMPAN CC-BY PDF must be fetched from a working mirror.