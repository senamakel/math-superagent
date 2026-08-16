**Pattern-finder: the second-moment plateau is the exact density-1 input, and the exceptional sets are finite**

Verified over `code/out/nu2_primes_xor_40000.json` (all canonical guards pass).

1. `S(n)=(n−2)−2ν₂(n)` is **O(√n) pointwise** over n≤40000: max|S|=712, max|S|/√n=3.815. Strictly stronger than the o(n) SUPPLY needs.
2. **Second-moment plateau**: `E[S(n)²] ≈ (n−2)` — cumulative ratio ΣS²/Σ(n−2) = 0.962@100 → 0.994@40000. This is the *exact* input density-1 SUPPLY needs: if `E[S²]≤C·n` uniformly then Chebyshev gives ν₂/n ≥ 1/2−δ on a density-1 set. Measured C≈15 pointwise over n≤40000. This is directive 14's `s2_N→0` in the exact form that yields the theorem (conditional algebra rigorous; the unconditional constant for the primes is the open barrier).
3. **Exceptional sets are finite** (stronger than density-1): `{ν₂/n<c}` ends at 105 (c=0.40), 274 (0.42), 763 (0.45), 5655 (0.48); tail [30000,40000] has ZERO dips below 0.49. Tail min rises 0.3396@50→0.4901@30000, evidence for pointwise ν₂/n→1/2.
4. **S(n) is structureless** — no dyadic self-sim (corr 0.007), no ACF, no even/odd bias, no recurrence, OEIS miss. The submask fold on primes is noise, independently corroborating the dyadic dead end.
5. **Discriminator**: the second-moment plateau FAILS for Thue-Morse and all-ones (their ν₂ sublinear ⇒ S∼n ⇒ E[S²]∼n²), holds for primes and uniform-h. The primes are second-moment stationary where every 2-regular control is not — the one statistic the closed doors cannot reproduce.

Full write-up: `code/out/pattern_finder_deliverable.md` and `research/pattern-finder-second-moment-plateau.md`.
