# Halbeisen–Hungerbühler — optimal bounds for rational Collatz cycle lengths

<!-- src: L. Halbeisen & N. Hungerbühler, "Optimal bounds for the length of rational Collatz cycles", Acta Arith. 78(3) (1997) 227–239; full text from ETH people.math.ethz.ch/~halorenz/publications/pdf/collatz.pdf -->

Full text: `research/sources/halbeisen-hungerbuhler-optimal-bounds-collatz-cycles-eth.full.md`

## What the source establishes

Studies Collatz cycles in the local ring Q[(2)] = rationals with odd
denominator (where parity = parity of numerator in lowest terms). Key
structural facts:

**Lemma 2 (rational cycle formula, after Lagarias).** For a 0-1 parity
sequence s of length l with n(s) ones, the affine iterate is
Ψ_s(x) = (3^{n(s)}·x + φ(s)) / 2^{l(s)}, and the unique x₀ ∈ Q[(2)] that
generates a cycle with parity sequence s is

    x₀ = φ(s) / (2^{l(s)} − 3^{n(s)})

with φ(s) the explicit sum (3). (This is the Böhm–Sontacchi formula in the
rational setting; a cycle of T exists iff 2^l > 3^n, i.e. the rational
approximation n/l ≈ log₂ 3 must be one-sided.)

**Lemma 5 (the extremal sequence).** For each (l, n), the cycle element
φ(s)/(2^l − 3^n) is minimized by the "staircase" sequence ~s(l,n)
(⌈jn/l⌉ − ⌈(j−1)n/l⌉), giving the exact minimum M_{l,n} (Corollary 1).

**Theorem 2 (Eliahou's criterion, restated).** If k(m) is the smallest
integer k with k/n(k) ≤ log₂(3 + 1/m), then every Collatz cycle C in N has
|C| ≥ k(min C). Eliahou: k(2^40) = 17,087,915.

**Theorem 3 (improved Eliahou criterion).** For every positive Collatz cycle
C in Q[(2)] with |C| > 160, |C| ≥ k(min C) — but the criterion now only
requires the verification bound to be ~10% smaller than Eliahou's original
demand.

**Theorem 4 (optimal criterion).** If L(m) is the smallest integer L such
that for n = n(L),
    Σ_{j=1}^L (⌈jn/L⌉ − ⌈(j−1)n/L⌉)·2^{j−1}·3^{n−⌈jn/L⌉}) / (2^L − 3^n) ≥ m,
then every positive Collatz cycle C in Q[(2)] has |C| ≥ L(min C).
**This criterion is optimal** (Lemma 5): for every cycle length there is a
cycle (in Q[(2)], the rational extension) attaining equality.

**Application (the 102,225,496 bound).** If the Collatz conjecture is
verified for all x₀ ≤ 2,123,660,328,072,11 ≈ 2.12×10^14 (about 3.3× the then
record 6.3×10^13; Eliahou's own criterion would need 2.9×10^14), then any
integer Collatz cycle not containing 1 has length ≥ 102,225,496. The proof
uses the continued-fraction convergents p₁₄=301994, p₁₆=17087915,
p₁₈=102225496 of log₂ 3 and the staircase structure.

**Lemma 9 / (A) ⇔ (A′) equivalence.** (A) "the trivial cycle {1,2} is the
only Collatz cycle in N" is equivalent to (A′) "there exists a non-periodic
s ∈ S_l, l > 3, with gcd{φ(t) : t ∈ orbit(s)} = 2^{l(s)} − 3^{n(s)}" — a
gcd reformulation of the cycle-half of the conjecture.

## What it implies for this run

- The 102,225,496 bound's verification hypothesis (2.12×10^14) is **now
  satisfied** by Barina's 2^71 ≈ 2.37×10^21, so it holds today — but it is
  superseded by Barina's 355,504,839,929 (`barina-cycle-length-355b`) which
  uses the same Eliahou machinery with the far larger verification bound.
- The optimal criterion (Theorem 4) is the sharpest cycle-length tool: the
  staircase sequence ~s(l,n) is the extremal parity pattern. This is exactly
  the Diophantine/structural lever `R-no-cycle-via-diophantine` in the
  weakened ladder.
- (A) ⇔ (A′) is a clean reduction: no non-trivial cycle iff no non-periodic
  parity string realizes the gcd condition. The gcd formulation is
  Lean-formalisable.

## Claims

```claim
id: halbeisen-rational-cycle-formula
statement: For a parity sequence s of length l with n(s) ones, the unique x0 in Q[(2)] generating a Collatz cycle with that parity pattern is x0 = phi(s)/(2^l(s) − 3^n(s)); a rational cycle exists iff 2^l > 3^n (Halbeisen–Hungerbühler Lemma 2, after Lagarias).
hypotheses: s a 0-1 sequence, phi(s) the explicit affine constant, cycles in the rational extension Q[(2)]
holds-here: yes — the rational cycle formula; the integer case is the special case x0 in N
status: proved
bearing: the exact rational-cycle characterization behind all cycle-length bounds
anchor: research/summaries/halbeisen-hungerbuhler-optimal-bounds-collatz-cycles-eth.md
```

```claim
id: halbeisen-optimal-criterion
statement: If L(m) is the smallest integer L with (sum over j=1..L of (ceil(jn/L)−ceil((j−1)n/L))·2^{j−1}·3^{n−ceil(jn/L)})/(2^L − 3^n) ≥ m for n = n(L), then every positive Collatz cycle C in Q[(2)] satisfies |C| ≥ L(min C); the criterion is optimal — equality is attained by the staircase parity sequence ~s(L,n) (Halbeisen–Hungerbühler Theorem 4, Lemma 5).
hypotheses: positive Collatz cycles in the rational extension Q[(2)]
holds-here: yes — the sharpest cycle-length-vs-minimum tool
status: proved
bearing: the extremal parity-pattern (staircase) result behind all cycle-length bounds
anchor: research/summaries/halbeisen-hungerbuhler-optimal-bounds-collatz-cycles-eth.md
```

```claim
id: halbeisen-102m-bound
statement: If the Collatz conjecture is verified for all x0 ≤ 2,123,660,328,072,11 ≈ 2.12e14, then any integer Collatz cycle not containing 1 has length at least 102,225,496 (Halbeisen–Hungerbühler 1997 application of Theorem 4, using convergents 301994, 17087915, 102225496 of log2 3).
hypotheses: verification to 2.12e14 (now satisfied by Barina's 2^71)
holds-here: yes — hypothesis satisfied today; superseded by barina-cycle-length-355b
status: proved
bearing: historical landmark of the cycle-length bound; the argument pattern (continued-fraction convergents of log2 3)
anchor: research/summaries/halbeisen-hungerbuhler-optimal-bounds-collatz-cycles-eth.md
```

```claim
id: halbeisen-A-iff-Aprime
statement: The statement (A) 'the trivial cycle {1,2} is the only Collatz cycle in N' is equivalent to (A') 'there exists a non-periodic parity string s of length l > 3 with gcd{phi(t) : t in the orbit of s} = 2^l(s) − 3^n(s)' (Halbeisen–Hungerbühler Lemma 9).
hypotheses: phi the affine constant, orbits under the left-shift permutation
holds-here: yes — a clean reduction of the cycle-half of the conjecture to a gcd condition
status: proved
bearing: a Lean-formalisable reduction of sub-claim (b)
anchor: research/summaries/halbeisen-hungerbuhler-optimal-bounds-collatz-cycles-eth.md
```
