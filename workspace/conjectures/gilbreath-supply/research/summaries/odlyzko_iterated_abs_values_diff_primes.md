# Summary — Iterated Absolute Values of Differences of Consecutive Primes

Source: A. M. Odlyzko, *Math. Comp.* 61(203) (1993) 373–380.
Full text: `research/sources/odlyzko_iterated_abs_values_diff_primes.full.md`
Source URL: https://www.ams.org/journals/mcom/1993-61-203/S0025-5718-1993-1182247-7/S0025-5718-1993-1182247-7.pdf

## What this source establishes

This is the computational and heuristic origin of this whole problem. It verifies
Gilbreath's conjecture (first term of every iterated absolute-difference row of
the primes is 1) for all primes ≤ 10^13, i.e. `d_k(1) = 1` for `1 ≤ k ≤
3.4×10^11`. Killgrove–Ralston (1959) had verified k ≤ 63,419; Odlyzko pushes
this to π(10^13).

The governing fact for the whole run: the table quickly becomes 0s and 2s.
Define `g(n)` = least k such that `d_j(n) ∈ {0,2}` for all `k < j < k+1000`.
The average of `g(n)` near N is ~22.1 (N=10^8), 27.0 (10^10), 32.8 (10^12) —
very small. Around π(10^12), `d_k(n)` is reduced to {0,2} at k = 213. So the
number of "large" (≥4) cells that survive is tiny and decays fast; the {0,2}
suffix is exactly the object `ν₂` measures.

Two heuristics are critical for what SUPPLY is asking:

1. **The {0,2} reduction is not monotone in k.** The average of `d_k(n)` is not
   monotone decreasing: `d_1 ≈ 27.66, d_2 ≈ 25.51, d_3 ≈ 19.63, d_4 ≈ 19.69,
   d_5 ≈ 13.50`. So the way entries collapse to the {0,2} spine is irregular.

2. **Large values of g(n) are driven by large prime gaps.** Every large g(n)
   examined traced to a large prime gap; correlation between max g(n) and max
   prime gap in a block was 0.52 over 10^4 blocks around 5.25×10^12. The largest
   g(n)=635 (near π(7.17716×10^12)) came from prime gap 674; second 589 from gap
   652. So the slow-{0,2} spots are the large-prime-gap spots.

This matters for SUPPLY because `ν₂(n)`'s suffix runs through `d_k(n)` for
`k = 0..n-1`; deep rows that are still large (≥4) break the {0,2} suffix and
reset `ν₂`. Odlyzko's data say deep-large cells are rare and tied to big gaps.

## Evidence class

Verified computation (his, to 10^13) + heuristic discussion. The {0,2}-reduction
and large-gap association are numerical observations from this computational
study, not proved theorems. Odlyzko's own caveat: the long computation could not
be fully guaranteed; one error was found and corrected.

```claim
id: odlyzko-0-2-reduction
statement: The iterated absolute-difference triangle of the primes reduces to values in {0,2}
  very quickly: average g(n) is ~22 (at 10^8), 27 (10^10), 33 (10^12), and d_k(n) is in {0,2}
  for all n in a window once k reaches ~213 near π(10^12). Deep cells ≥ 4 are rare and
  concentrated near large prime gaps.
hypotheses: primes as initial row; the absolute-difference iteration.
holds-here: true — this is exactly the {0,2} structure that ν₂(n) measures.
status: asserted-by-source (numerical, to π(10^13); the large-gap association is a
  measured correlation, not a theorem).
bearing: situates ν₂ as the size of the {0,2} suffix; deep-large cells (break points of the
  suffix) are the rare, prime-gap-driven events. SUPPLY is about whether they are so rare
  that the suffix is long in linear measure.
anchor: Odlyzko 1993, §§3, Tables 2–4.
```

```claim
id: gilbreath-verified-10^13
statement: Gilbreath's conjecture — d_k(1) = 1 for all k, where d is the iterated absolute
  difference of the primes — holds for all k ≤ π(10^13) ≈ 3.4×10^11.
hypotheses: primes as initial row.
holds-here: true (this run does not need Gilbreath, but the verification bounds the range).
status: verified-numerically by source, to π(10^13).
bearing: defines the canonical reference tier and the {0,2} context; not directly used by
  SUPPLY's proof but the context the problem states must not be re-derived.
anchor: Odlyzko 1993, abstract and §2.
```

```claim
id: deep-cells-are-large-gap-driven
statement: In Odlyzko's data, every very large value of g(n) (slow {0,2}-reduction) examined
  was caused by a large prime gap; correlation between maximal g(n) and maximal prime gap
  per block is ~0.52.
hypotheses: primes over sampled blocks near 5.25×10^12.
holds-here: true as a meas*ured* tendency, not a theorem; relevant to why long {0,2} suffixes
  break.
status: asserted-by-source (measured tendency over 10^4 blocks).
bearing: a natural guess ("ν₂ stays large") must contend with the fact that the suffix breaks
  exactly where large gaps are. Suggests the positive-frequency-of-small-gaps side drives
  long suffixes, aligning with the mod-4 switch-density reduction.
anchor: Odlyzko 1993, §3.
```
