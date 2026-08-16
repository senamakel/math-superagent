# Summary — Green, "Three topics in additive prime number theory"

Source: Ben Green, "Three topics in additive prime number theory", arXiv:0710.0823 (2007), CDM conference notes (Current Developments in Mathematics, Harvard, November 2007).
Source URL: https://arxiv.org/pdf/0710.0823. Full text: `research/sources/green_three_topics_additive_prime_number_theory.full.md`.

## What this source establishes

Three independent expositions. Of these, **Topic 2 is the one that matters here.**

**Topic 1 — bounded gaps (GPY).** Theorem 1.4.1: if the Elliott–Halberstam hypothesis EH(θ) holds for some θ > 1/2, then for some k₀(θ), every admissible k-tuple H (k ≥ k₀) has infinitely many n with at least two of n+h₁,…,n+h_k prime. (Prelude to Zhang–Maynard; not the operative result for SUPPLY.)

**Topic 2 — Mauduit–Rivat (the operative result).**

> **Theorem 2.1.1 (Mauduit–Rivat).** Let Λ be the von-Mangoldt function and s : N → N the binary digit sum. Then
> `E_{n≤X} Λ(n)(−1)^{s(n)} = O(X^{−δ})` for some δ > 0.

Consequently the parity of the binary digit sum of the primes is asymptotically **50/50, with a power-saving error term** — the binary Thue–Morse (sum-of-digits) function is equidistributed along the primes. This answers a long-standing question of Gelfond. Green gives a completely self-contained proof of the binary case via Vinogradov's Type I/II (bilinear) sum method: the main estimates (Propositions 2.5–2.8) are the L^∞ bound |f̂_k(r)| ≪ 2^{−ck} on the Fourier coefficients of f(n)=(−1)^{s(n)} and the equidistribution lemmas. The original Mauduit–Rivat paper proves the general base-q, residue-class-a mod m statement; Green restricts to the binary, "which residue is odd" case to keep the proof accessible.

**Topic 3 — linear equations in primes (Green–Tao).** Proposition 3.0.7: generalized von Neumann / complexity-one decomposition — harmonic analysis can handle systems of complexity one. Background only.

## Why it bears on SUPPLY (and its precise limit)

The run exists to test whether the fold Φ can force `wt(Φ_n h) ≥ c·n` from an arithmetic input *weaker than positive mod-4 switch density* (GOAL priority 2, open request `walsh-spectral-subset-b904`). This source is the canonical primary exhibition that **the primes do satisfy strong, unconditional digital-equidistribution** — `(−1)^{s(p)}` sums to O(X^{−δ}) along primes, a genuinely weak arithmetic input that is *proved* and needs no conjecture, no L-function, and no GRH. This is the right *paradigm* for what the weakest-input answer should look like.

**But it does not close request `walsh-spectral-subset-b904`, and must not be filed as doing so.** The request needs an arithmetic input on the *gap-parity string* `h[j] = ((q_{j+1}−q_j)/2) mod 2`, read by Φ along binary-submask windows. Mauduit–Rivat's statistic is `(−1)^{s(q_j)}` — the digit sum of the *prime itself* (a value-domain statistic at prime indices' values), whereas `h` is an *index-domain pairwise gap* statistic. These are different objects; no transfer from "digit-sum of p is equidistributed" to "the gap-parity string h is generic under the submask-XOR fold" is present in this source or anywhere in the library. Claiming the one proves the other would be an overclaim of exactly the kind the scholar flagged for the Pivato note.

So the honest position: **this source fixes the model theorem** for the weakest-input question (primes provably satisfy digital-type vanishing correlation), but the specific finite transfer to `wt(Φ_n h)` from *h* remains open and is not in any source.

## Evidence class

Sourced. Theorem 2.1.1 is Mauduit–Rivat (Annals of Mathematics 171(3), 2010); Green's notes give a self-contained proof of the binary case and are the accessible primary treatment (the general statement is the library's `mauduit_rivat_gelfond_somme_chiffres_premiers_primary` source). Unconditional and proved.

```claim
id: mauduit-rivat-prime-digit-sum-equidistributed
statement: E_{n≤X} Λ(n)(−1)^{s(n)} = O(X^{−δ}) for some δ > 0: the binary digit-sum parity of the primes is equidistributed (50/50) with a power-saving error, answering Gelfond.
hypotheses: Λ von-Mangoldt; s = binary digit sum; Theorem 2.1.1, Green §2, proves the Mauduit–Rivat result by Type I/II bilinear method.
holds-here: no — this is a value-domain (digit-sum of q_j) equidistribution; SUPPLY's h is a gap-parity (index-domain pairwise) statistic, and no transfer from one to the other is established. (See bearing: a true theorem whose hypotheses fail for this problem — recorded so it is not treated as progress.)
status: sourced
bearing: Model of the shape of a prime-statistic equidistribution the averaged line would want, but the fold's object is a different statistic; it does not supply the gap-parity or dyadic-index-autocorrelation input SUPPLY needs. Do not cite as a gap-parity result.
anchor: research/sources/green_three_topics_additive_prime_number_theory.full.md Thm 2.1.1
```

## What would falsify its bearing as a proof input

If anyone treated this as a proof of `wt(Φ_n h) ≥ c·n`, it would fail: the theorem is about `(−1)^{s(q_j)}` summed over primes, whereas h encodes the mod-4 gap structure. A valid use needs either (a) a demonstrated reduction of h's submask-window correlations to digit-sum correlations, or (b) a separate argument that the fold only needs the digit-genericity Mauduit–Rivat supplies. Neither is established. As context it is correct and load-bearing for the *paradigm*; as a proof input it is inert until that transfer is supplied.
