# Shiu 2000, "Strings of Congruent Primes"

<!-- source: https://doi.org/10.1112/s0024610799007863 | J. London Math. Soc. (2) 61 (2000) 359–373; content read via summary, full text not downloaded (paywalled) -->

## Claim (established at source, asserted here — the run holds only the abstract/summary)

**D. Shiu, *Strings of Congruent Primes*, J. London Math. Soc. (2) 61 (2000) 359–373, doi 10.1112/s0024610799007863.**

Proves Chowla's conjecture for all moduli q and residues a with (q,a)=1: there are infinitely many consecutive-prime pairs p_n, p_{n+1} with p_n ≡ p_{n+1} ≡ a (mod q). Moreover, for any k there are arbitrarily long "strings" of consecutive primes all congruent to a mod q.

For q=4, a∈{1,3}: infinitely many consecutive-prime pairs with equal residue mod 4 (i.e. gaps divisible by 4, NOT the switch gaps ≡ 2 mod 4).

```claim
id: shiu-2000-strings-of-congruent-primes
statement: (Shiu 2000) There are infinitely many consecutive-prime pairs p_n, p_{n+1} with p_n ≡ p_{n+1} ≡ a (mod q) for any modulus q and residue a coprime to q; and arbitrarily long strings of consecutive primes sharing a residue a mod q.
hypotheses: primes; consecutive-prime residue patterns mod q; unconditional (sieve/character-sum methods, no HL, no GRH).
holds-here: yes
status: asserted            # only abstract-level content held; full proof not downloaded
bearing: Proves the OPPOSITE direction from the one Route B needs. ν₂ (the Gilbreath supply) counts consecutive mod-4 SWITCHES ([p_{n+1} ≢ p_n mod 4] = gap ≡ 2 mod 4); Shiu proves infinitely many NON-switches (equal residues, arbitrarily long runs). It does NOT give any positive-density or even quantitative lower bound on the switch count — so it does not supply ν₂ > n^β. It is the strongest unconditional result in the mod-4 residue-pair landscape and it goes the wrong way for the supply bound.
anchor: research/summaries/shiu-2000-strings-of-congruent-primes.md
```

## Why the run needs this row

The adopted forward approach `chebyshev-bias-granville-nu2-supply` (research/approaches/chebyshev-bias-granville-nu2-supply.md) reduces the entire open content of Route B (the proved Granville Lemma 5.4 → Theorem 5.5 reduction) to a supply-side lower bound ν₂(q_n) > n^β, β > 0.525, where ν₂ counts the descent coefficient, whose atomic bit is bit_n = [p_{n+1} ≢ p_n (mod 4)] (a TWO-POINT consecutive-prime statistic, a gap ≡ 2 mod 4). The run's measured ν₂/n ≈ 0.49–0.52 gives a factor-26 margin over n^0.525, but the bound is unproved.

The relevant literature, now confirmed:

- **No unconditional positive-density or quantitative lower bound on the mod-4 switch count is known.** The switch count (= n/2 to first order under the conjectural equidistribution of residue pairs) is provable only at the Hardy–Littlewood / Lemke Oliver–Soundararajan conjecture level, which is conditional.
- **Shiu 2000** (this row): the only unconditional result in this corner, and it is about equal-residue runs (non-switches), the reverse of the supply. It guarantees the switch count is *deficient* in a long-run sense, never that switching has positive density.
- **Lemke Oliver–Soundararajan 2016** (already held, `los-2016-consecutive-pair-mod4-bias`): the bias is conjectural; the honest deliverable is a FLUCTUATION bound (bias oscillates, Littlewood-type), never a one-sided assertion. Its Conjecture 1.2 says the distinct-residue pair (a,−a) outnumbers the repeating pair (a,a), which would push ν₂ slightly ABOVE n/2 → good for Route B — but conjecturally.
- **Ruzsa, "Consecutive primes modulo 4", Indag. Math. 2003** — paywalled; only the abstract-level result held (π_ij(x) counts; Shiu's bound for π_11 improved to at least c x loglog x / (log x)^2). That is still an INFINITUDE bound, not a positive-density lower bound; does not supply ν₂.

## Net verdict for Route B

The supply-side lower bound ν₂ > n^β that the whole of Route B needs is **not unconditional and not provable from PNT-in-AP or Shiu-level methods**; it is a two-point consecutive-prime statement at Hardy–Littlewood / Lemke Oliver–Soundararajan conjecture level. A conditional partial result ("IF the mod-4 switch count has positive density / ν₂ ≥ c·n, THEN GC holds via Lemma 5.4") is a real GOAL.md-countable deliverable, but the hypothesis is genuinely open and cannot be upgraded to unconditional with held or found methods. Recorded so nobody re-searches for an unconditional supply bound that does not exist.
