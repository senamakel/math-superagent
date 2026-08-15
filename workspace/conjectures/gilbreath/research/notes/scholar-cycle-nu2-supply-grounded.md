# Scholar cycle: grounded the ν_2 supply precedents (Route B)

Three analytic-number-theory sources the adopted approach
(`chebyshev-bias-granville-nu2-supply`) cited but did not hold are now held,
read in full, and digested. Together they pin the **open content of Route B**:
the atomic bit feeding Granville's ν_2 is a two-point consecutive-pair mod-4
statistic, and no one-sided unconditional forcing of it exists.

## What was verified against the full texts

1. **Rubinstein–Sarnak 1994, "Chebyshev's Bias"** (Project Euclid, genuine):
   the mod-4 bias is real — ρ(P_{4,3,1})≈0.9959 under GRH+GSH — but oscillates
   (Littlewood 1914); both P_{4,1,3} and P_{4,3,1} extend to infinity, so NO
   one-sided unconditional "primes ≡ 3 mod 4 lead" holds, and leadership
   density is strictly in (0,1). Claim `rubinstein-sarnak-bias-oscillates-unconditional-false`.

2. **Lau 2024** (arXiv:2409.12819): even a single non-constant consecutive-
   prime residue pattern being attained infinitely often is beyond present
   methods; the proved counts (mφ(q) patterns; ≫ m/(log m)^10 φ(q)^2 for
   squarefree q) are of distinct patterns, never a frequency bound on a
   prescribed switch. Claim `lau-2024-consecutive-residue-patterns-existence-only`.

3. **Maynard 2015** (arXiv:1311.4600 — genuine id, see correction): liminf
   (p_{n+1}−p_n) ≤ 600 unconditionally (Bombieri–Vinogradov); liminf
   (p_{n+m}−p_n) ≪ m³e^{4m}; positive proportion of admissible m-tuples satisfy
   prime k-tuples. All existence, never frequency. Claim `maynard-2015-existence-not-frequency`.

## The located error (this run)

The `research/sources/maynard-2015-small-gaps-between-primes.full.md` file had
held WRONG content — the mis-resolved arXiv 1404.3329 was a cs.CE portfolio-
selection paper, and my own first two re-downloads (1404.3084 bibliometrics,
1404.6999 WASP) were also wrong. The genuine id is **1311.4600**, now in place.
The librarian's prior summary had also credited this paper with a normalized-gap
bound (liminf (p_{n+1}−p_n)/(√log·(loglog)²) < ∞) that is NOT in it (it belongs
to GPY "Primes in tuples II" Acta Math. 2010). Both corrected.

## What this settles and what it does not

Settles: the honest ν_2 supply deliverable is ν_2 = n/2 + O(bias) at
Hardy–Littlewood / Lemke Oliver–Soundararajan level, never an unconditional
one-sided density. Route B's irreducible open statement is the two-point mod-4
correlation bound ν_2 ≥ n^{0.525+δ} on consecutive primes.

Does not settle (unchanged): the (2,4)-event regeneration rate — whether the
leading {0,2} blocks re-enter fast enough. The three sources bound *what can be
proved* about the supply side but do not supply it. This remains a
Hardy–Littlewood-level open question, exactly as the approach's own falsifier
predicted.

## File actions

- `research/sources/maynard-2015-small-gaps-between-primes.full.md` — replaced with genuine text.
- Summaries rewritten (Maynard, Rubinstein–Sarnak, Lau) with claim blocks.
- `research/threads/regeneration.md` — appended the grounded-precedent paragraph to blocked-by.
- `code/scholar/verify_two_point.py` — documents the exact bit identity and a to-run density check (unexecuted in scholar role).
- Cognee: two durable memories stored (the two-point supply conclusion; the Maynard-file content correction).
- `answers:` ids used: `supply-frequency-vs-existence`, `supply-one-sided-vs-fluctuation` (see REQUESTS G-supply row).
