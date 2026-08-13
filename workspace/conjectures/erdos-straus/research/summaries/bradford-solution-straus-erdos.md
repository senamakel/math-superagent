# Bradford, "A Solution to the Straus–Erdős Conjecture" (2026, claimed)

Source: arXiv:2602.11774 (12 Feb 2026), HTML: https://arxiv.org/html/2602.11774v1
Full text: `research/sources/bradford-solution-straus-erdos.full.md`

## What it establishes (sourced, primary) — and does NOT establish

**Status: this is a claimed proof that does not complete.** The paper derives
two solution shapes from the two-variable reduction and leaves the covering
argument unfinished. Anyone citing it as a proof of the conjecture is wrong.

- **Prop 1**: for a prime `p ≡ 1 mod 4`, a Type I solution exists iff (roughly)
  `z = ((4k+3)p² + p)/4` for some `k ≥ 0` (with `(x+y)/gcd(xy,x+y) = 4k+3`).
- **Lemma 1**: primes `p ≡ n mod M(k,ℓ)` with `(4k+3)n ≡ −1 mod M` where
  `M = (16ℓ(4k+3) − 4ℓ²)/gcd(ℓ,4)²`, `1 ≤ ℓ ≤ 2(4k+3)`, `gcd(ℓ,4k+3)=1`, have
  explicit solutions — the three fractions
  `4(4k+3)−ℓ, ℓ` over `(4k+3)p+1` and `4/(p((4k+3)p+1))`.
- **Lemma 2**: Type II analogue: primes `p ≡ −(4k+3) mod M(k,ℓ)` have solutions
  `4/(p+(4k+3)) + (4(4k+3)−ℓ)/(p(p+(4k+3))) + ℓ/(p(p+(4k+3)))`.
- The paper's last line: "The last thing that we must show is that this is a
  covering system" — then stops. The k=0 worked example lists the first few
  primes (5,13,17,29) but no theorem shows the residues cover all primes
  `p ≡ 1 mod 4`.

## Consequence

A concrete, checkable family structure (two lemmas with explicit unit
fractions) that may or may not cover the open classes; the covering claim is
open. Lemma 1's three-term shape for `p ≡ 1 mod 4` with parameter k: the
first term `(4(4k+3)−ℓ)/((4k+3)p+1)` is a unit fraction only when
`4(4k+3)−ℓ | (4k+3)p+1` as integers — an identity constraint per class, not a
per-n check, so it is exactly the kind of family the oracle's
`is_identity`/`solves` checker must test before any coverage claim.

```claim
id: bradford-2026-covering-open
statement: Bradford (arXiv:2602.11774) claims an elementary proof of the Erdős–Straus conjecture via two lemmas producing explicit solutions for primes in residue classes modulo M(k,ℓ), but the concluding covering-system claim is not proved in the paper (v1); the paper ends stating the covering step remains.
hypotheses: p prime, p ≡ 1 mod 4.
holds-here: true — the six open classes are all ≡ 1 mod 4 primes; the covering step is what would settle them, and it is absent.
status: sourced (arXiv:2602.11774 v1; the paper itself disclaims completion).
bearing: do NOT treat this as a proof; treat Lemma 1/2 families as candidates to verify/refute with the oracle, and the missing covering step as the concrete gap this run could attack.
anchor: research/sources/bradford-solution-straus-erdos.full.md
```