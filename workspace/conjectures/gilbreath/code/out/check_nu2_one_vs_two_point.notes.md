# ν₂: one-point or two-point? — structural determination

## The question (candidate 3, chebyshev-bias-granville-nu2-supply)

Granville's Theorem 5.5 reduces Gilbreath's conjecture (conditional on his
own Conjecture 5.1 being the supply) to the single density statement
`ν₂(q_n) > n^β, β > 0.525`, where `ν₂(q_n)` counts the 2s (`c_s = 2`) in the
maximal `{0,2}` tail of the Gilbreath diagonal through `q_n`. The candidate
asks: is `ν₂` a ONE-POINT statistic (primes in a residue class → PNT-in-AP /
GRH gives it) or a TWO-POINT statistic (consecutive primes in residue classes
→ Hardy–Littlewood gives it)?

## The answer: the atomic bits are two-point (consecutive-prime mod-4)

Inside the `{0,2}` diagonal tail, the halved entry `c_s/2 ∈ {0,1}` evolves by
XOR (= Pascal mod 2, the run's proved `rule90-interior-xor`). By the mod-4
linearization (Odlyzko eq. 201; the run's `mod4-linearization`), a diagonal
entry's exact value mod 4 is a binomial (Rule-90) combination of the *halved
gaps* of the initial sequence. The parity of each halved gap is:

    g_n = p_{n+1} − p_n               (even, since both primes > 2 are odd)
    (p_{n+1} − p_n)/2 mod 2 = 1  ⟺  g_n ≡ 2 (mod 4)
                              ⟺  p_{n+1} ≢ p_n (mod 4)
                              ⟺  consecutive primes in DIFFERENT mod-4 classes.

So the atomic bit that feeds `ν₂` is

    bit_n = [ p_n mod 4 ≠ p_{n+1} mod 4 ],

which is a **two-point statistic**: it is not determined by `p_n mod 4` alone
(you must also know `p_{n+1} mod 4`). `ν₂` is a binomial/Rule-90 additive
transform of these two-point bits. **It is NOT a one-point count of a single
residue class, so PNT-in-AP / GRH-for-Dirichlet-L does not, by itself, give
`ν₂ > n^β`.**

## Consequence

The candidate's dichotomy resolves as: **two-point**. The honest supply
statement needs control of the joint (consecutive-prime) residue distribution
mod 4 — exactly the Hardy–Littlewood prime-tuple / Lemke Oliver–Soundararajan
"Unexpected biases in the distribution of consecutive primes" (PNAS 2016)
level, or (at the spectral/fluctuation level) the Rubinstein–Sarnak
Chebyshev-bias framework under GRH + Linear-Independence.

The run's own measurement (`granville-nu2-density-measured`: `ν₂/n ∈
[0.42, 0.52]` over n ≤ 3999, factor-26 margin over `n^0.525` at n=3999)
shows the target is comfortable — the honest claim is `ν₂ = n/2 + O(n^{1/2+ε})`
(a Gaussian-fluctuation / two-point level statement), from which
`n/2 − O(n^{0.525}) > n^0.525` for large n. But the Chebyshev-bias / Littlewood
oscillation caution (Rubinstein–Sarnak 1994) is load-bearing: the bias
OSCILLATES, so no one-sided lower bias can be asserted unconditionally; the
deliverable must be a fluctuation bound under stated hypotheses, exactly as
the candidate's own `falsifier` says.

## Status

Structural determination, no computation run. Precise and checkable: the bit
`[p_{n+1} ≢ p_n (mod 4)]` is the atomic input; it is two-point by definition.
Falsifier: if `ν₂` were reducible to `#{p ≤ x : p ≡ a (mod 4)}` (one-point),
PNT-in-AP would give it — but the mod-4 gap parity shows it is the
consecutive-pair class switch, hence two-point.
