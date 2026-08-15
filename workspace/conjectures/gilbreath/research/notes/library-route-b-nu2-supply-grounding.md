# Librarian cycle — Route B (Granville ν₂) precedent grounding

```claim
id: ruzsa-2001-abstract-via-bibliography
statement: The abstract-level content of Ruzsa 2001 "Consecutive primes modulo 4" (Indag. Math. 12(4) 489-503, doi 10.1016/S0019-3577(01)80038-0, paywalled) is now held via the Martin et al. 2024 annotated bibliography for comparative prime number theory (arXiv:2309.08729, entry [231]): the number of pairs of consecutive primes <= x both congruent to 1 mod 4 is >> x loglog x / log^2 x, improving Shiu; the generalization replaces the single class 1 mod 4 by any set of phi(q)/2 reduced residue classes mod q; the proof uses Maier's method. Knapowski-Turan 1977 ([134]) unconditionally show the number of consecutive-prime pairs p_v,p_{v+1} both ≡1 mod 4 exceeds (log T)^B, and leave open the infinitude of consecutive TRIPLES ≡1 mod 4 and note the four pair-classes mod 4 are not equally likely (predating LOS 2016).
hypotheses: consecutive primes, modulus 4 pair-residue statistic; (any) set of phi(q)/2 reduced classes mod q
holds-here: yes (this is exactly the consecutive-pair mod-4 landscape that feeds nu_2; the equal-residue and switch pair-classes are the same 4 classes)
status: sourced (abstract via the standard field survey, not the paywalled full text)
bearing: The Ruzsa/Shiu/Knapowski-Turan results are all on the NON-SWITCH (equal-residue, gap ≡ 0 mod 4) direction, with only weak sub-density (>>x loglog x/log^2 x) or (log T)^B lower bounds. They give NO density lower bound on the SWITCH count (gap ≡ 2 mod 4) that nu_2(q_n) > n^beta needs. Re-confirms G-supply is genuinely open; the honest ceiling stays the conditional result at Hardy-Littlewood / Lemke Oliver-Soundararajan level.
anchor: research/sources/martin-annotated-bibliography-comparative-prime-number-theory.full.md
answers: the open G-supply request row (the Ruzsa abstract that was unobtainable is now held via this survey)
```


State of the reference library where it bears on the run's adopted approach
(`research/approaches/chebyshev-bias-granville-nu2-supply.md`), as of this
librarian cycle.

## What this cycle added to the library

The adopted Route B approach needs the **fluctuation side** of the two-point
consecutive-prime (mod 4) supply statistic that feeds Granville's ν₂. Two
sources were downloaded and digested; the other two precedent sources (Lau
2024, Maynard 2015) were confirmed already held and their bearing re-stated.

1. **Rubinstein & Sarnak 1994, "Chebyshev's Bias"** — the canonical
   analytic-number-theory treatment of prime-race bias.
   - Clean primary: `research/sources/rubinstein-sarnak-1994-chebyshev-bias-full.full.md`
     (Project Euclid PDF: https://projecteuclid.org/download/pdf_1/euclid.em/1048515870).
   - Summary: `research/summaries/rubinstein-sarnak-1994-chebyshev-bias.md`.
   - Key facts (under GRH + GSH): explicit Fourier transform for the mod-4 race;
     `δ(P_{4;3,1}) = 0.9959`; **oscillation (Littlewood) means no one-sided
     unconditional bias** — the honest statement is a *fluctuation bound*.
   - A scanned no-text-layer Waterloo mirror PDF was downloaded by mistake,
     recognised as unreadable garbage, and overwritten with a pointer note
     (`rubinstein-sarnak-1994-chebyshev-bias.full.md`). The clean Project Euclid
     copy is the authoritative source.

2. **Lemke Oliver & Soundararajan 2017, "The distribution of consecutive prime
   biases and sums of sawtooth random variables"** — the rigorous back half of
   the consecutive-prime pattern-bias programme.
   - Full text: `research/sources/lemke-oliver-soundararajan-2017-prime-biases-sawtooth.full.md`
     (arXiv:1709.06168).
   - Summary: `research/summaries/lemke-oliver-soundararajan-2017-prime-biases-sawtooth.md`.
   - Key facts: Theorems 1.1–1.3 — the secondary fluctuation term in
     consecutive-prime (mod q) pattern biases has a **continuous, symmetric-
     about-0 limiting distribution** as q→∞, connected to Dedekind-sum Fourier
     transforms and the φ-mean error term.

3. **Rubinstein–Sarnak mod-4 race (UBC course notes)** — clean secondary
   transcript cross-checking the 0.9959 value and the GRH/LI hypotheses.
   - Full: `research/sources/rubinstein-sarnak-mod4-race-ubc-notes.full.md`
   - Summary: `research/summaries/rubinstein-sarnak-mod4-race-ubc-notes.md`

## Confirmed already held (bearing re-stated)

- **Maynard 2015** "Small gaps between primes" (Annals 181:383–413,
  arXiv:1404.3329): the two-point/small-gap sieve machinery; proves
  *existence* of configurations, not frequency lower bounds.
- **Lau 2024** "Residue class patterns of consecutive primes" (arXiv:2409.12819):
  proves which patterns of consecutive residues occur infinitely often
  (existence, ≥mφ(q) patterns), but no frequency bound.

## Synthesis for the approach (new claim `rubinstein-sarnak-fluctuation-not-bias`)

The adopted Route B conclusion is now *grounded in the primary literature*:

1. **ν₂ is two-point** — the atomic bit is `bit_n = [p_{n+1} ≢ p_n (mod 4)]`,
   a consecutive-prime residue switch. This is NOT a one-point PNT-in-AP
   statistic, so GRH-for-Dirichlet-L alone does not deliver ν₂ > n^β.
2. **The honest deliverable is a FLUCTUATION bound**, not a one-sided bias:
   both Rubinstein–Sarnak (oscillation) and LOS-2017 (symmetric-about-0
   limiting distribution) show the secondary term oscillates. A
   "Chebyshev bias forces ν₂ > n^0.525" unconditional claim is false in form.
3. **The ν₂ ≥ n^{0.525+δ} lower bound itself remains open.** The sieve
   machinery (Maynard, Lau) and the bias distribution theory (RS, LOS) give
   existence and distributional laws, not the required frequency lower bound —
   it stays at Hardy–Littlewood / Lemke-Oliver–Soundararajan conjecture level.

## Searchability

The three new full texts and their summaries are indexed and searchable via
`search_documents`; the two durable summary findings are stored in Cognee via
`remember_memory`. FRONTIER.md is auto-regenerated on download and will reflect
the new citations.

## Unobtainable (no re-attempt)

The Waterloo mirror of Rubinstein–Sarnak 1994 is a scanned PDF with no text
layer — do not re-download; the Project Euclid copy is the authoritative source
and is already held.
