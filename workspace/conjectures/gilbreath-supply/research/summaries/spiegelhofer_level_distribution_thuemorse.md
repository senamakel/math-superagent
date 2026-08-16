# Summary — Spiegelhofer, "The level of distribution of the Thue–Morse sequence"

Source: L. Spiegelhofer, *The level of distribution of the Thue–Morse sequence*,
Compositio Math. (2020), DOI 10.1112/s0010437x20007563. Full text:
`research/sources/spiegelhofer_level_distribution_thuemorse.full.md`. (Downloaded this
run from the arXiv preprint arXiv:1803.01689; this is the paper two of this library's
own sources — BKM "Gowers norms for automatic sequences" and Müllner–Spiegelhofer
"Normality … II" — cite as the canonical reference for how well-distributed the
Thue–Morse sequence is.)

## What it establishes

The analogue of Bombieri–Vinogradov for the **Thue–Morse sequence** `t(n) = s₂(n) mod 2`.

- **Theorem 1.1 / 2.1 (level of distribution 1).** For every `ε > 0` there are `η > 0`
  and `C` such that
  ```
  Σ_{d ≤ D}  max_{gcd(a,d)=1} | Σ_{n≤N, n≡a mod d} t(n) |  ≤  C N^{1-η}
  ```
  for `D = N^{1-ε}`. That is, Thue–Morse satisfies a Bombieri–Vinogradov theorem for
  **every exponent `θ < 1`**, so its level of distribution is 1 — essentially best
  possible. This improves the `2/3` obtained earlier by Müllner and the author, and
  `0.5924` of Fouvry–Mauduit.
- **Theorem 1.2 / 2.2 (application).** Thue–Morse along `⌊n^c⌋`, `1 < c < 2`, is simply
  normal (each symbol has asymptotic frequency `1/2`, with explicit power-saving error
  `CN^{-η}`). Closes the gap from Mauduit–Rivat (simple normality for `1 < c < 2` = the
  squares result) to the full `1 < c < 2` range for simple normality.
- **Theorem 2.3.** A quantitative two-parameter statement controlling the error as
  `D = N^{θ₂}` varies.

The technique is a reduction to bounding a **Gowers uniformity norm** of Thue–Morse
(analogous to Konieczny 2017), plus Selberg/Farey machinery for the large-sieve parts.

## Why it matters for SUPPLY / the reopened question

Closed door 3 is that **aperiodicity is insufficient**: Thue–Morse is aperiodic with
`ν₂` sublinear (fold weight decaying toward 0), so no "h is aperiodic/random" hypothesis
can of itself force linear fold weight. This paper quantifies precisely *how* well-
distributed a sequence can be while still being the sublinear‑fold counterexample:
**Thue–Morse has level of distribution 1 — it is as equidistributed on arithmetic
progressions as a random sequence can be, yet its fold weight is sublinear.**

The bearing is a **negative pricing** of the "h is well-distributed on progressions"
input family: the canonical aperiodic sequence that shares the primes' observed
equidistribution-on-progressions quality (level of distribution 1, essentially optimal)
*still collapses the fold*. So a theorem of the form "h has good level of distribution /
is well-distributed on residues ⇒ linear supply" is refuted by Thue–Morse itself as a
witness — it cannot be the needed arithmetic input. This is consistent with the five
closed doors and reinforces that the input must live in Φ's submask-XOR reading (the
request `walsh-spectral-subset-b904`), not in h's progression-distribution.

```claim
id: spiegelhofer-thuemorse-level-1
statement: The Thue–Morse sequence t(n) = s₂(n) mod 2 has level of distribution 1: for every ε > 0 there exist η > 0 and C with Σ_{d≤D} max_{(a,d)=1} |Σ_{n≤N, n≡a mod d} t(n)| ≤ C N^{1−η} for D = N^{1−ε} (a Bombieri–Vinogradov theorem for each exponent θ < 1). Consequently t(⌊n^c⌋) is simply normal for every 1 < c < 2, with error C N^{−η}.
hypotheses: t the Thue–Morse sequence; sums over n ≤ N in a single residue class mod d; D = N^{1−ε}.
holds-here: Yes — t is the model object of closed door 3 (aperiodic with sublinear fold weight); the level-of-distribution quantity is exactly the residue-distribution quality of h the problem must not rely on.
status: sourced (Spiegelhofer 2020, Thm 1.1/2.1/1.2/2.2)
bearing: Prices the "h is well-distributed on arithmetic progressions" input family negatively: Thue–Morse has level of distribution 1 (essentially optimal equidistribution on progressions) yet has sublinear fold weight. Any weaker-than-switch-density arithmetic input of the form "h equidistributes on residue classes" is refuted by Thue–Morse as a witness. So the needed input must live in the fold's submask-XOR reading, not h's progression distribution. Consistent with the five closed doors.
anchor: research/sources/spiegelhofer_level_distribution_thuemorse.full.md
```
