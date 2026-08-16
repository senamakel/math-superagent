# Librarian report — log-periodic grounding pass

**Cycle focus.** The run's live third-pass task `log-periodic-oscillation-test-d47`
(directive 48) tests whether the fitted threshold exponent `E = 0.557 ± 0.002`
with oscillating per-doubling slopes is the log-periodic signature of a
Pascal-mod-2 counting function, with `log₂3 − 1 = 0.58496` the named rival
candidate. The run held the *hypothesis* only as an OEIS comment on A006046
(`research/notes/log_periodic_pascal_mod2_engine.md` flagged Stolarsky 1977 and
the Flajolet–Golin Mellin papers as "NOT held locally"). This pass closed that
gap.

## Sources added

1. **Hwang–Janson–Tsai 2024**, *Periodic minimum in the count of binomial
   coefficients not divisible by a prime*, arXiv:2408.06817.
   `research/sources/hwang_janson_tsai_periodic_minimum_binomial_modp.full.md`.
   **Theorem 2.2** proves the exact log-periodic representation
   `F_p(n) = n^ρ·P(log_p n)`, `ρ = log_p((p+1)/2)`, explicit 1-periodic P, for
   the count of Pascal entries not divisible by p. For p=2 (= A006046),
   `ρ = log₂(3/2) = log₂3 − 1 = 0.58496` — **exactly** directive 48's named
   rival exponent. This upgrades the log-periodic phenomenon from OEIS comment
   to **proved theorem** for the prototype object.
2. **Flajolet–Sedgewick**, *The average case analysis of algorithms: Mellin
   transform asymptotics*, INRIA RR-2956.
   `research/sources/flajolet_sedgewick_mellin_transform_asymptotics.full.md`.
   The foundational method (harmonic sums → Mellin transform → singularity
   extraction) by which such log-periodic fluctuations are derived, and why a
   bounded-window log-log fit is biased in their presence — the mechanism behind
   directive 48's warning that `0.5568` may be a window artifact.

## Claim filed

`hjt-p2-log-periodic-representation-proved` — status **proved**, hypotheses
(p prime; F_p the row-count not divisible by p; recurrence (2.1)), holds-here
yes (p=2 is exactly A006046), rendered into CLAIMS.md. Its falsifier is honest:
a monotone trend in `w*(n)/n^E` vs `log₂(n)` for both candidates would refute
the *transfer* to w* (not HJT's own theorem, which is about A006046).

## Scoping honest

The new theorem **grounds** the log-periodic *analogy* for w*(n); it does not
**transfer** the exponent `log₂3−1` to w*(n). The run's own tabulation of
`w*(n)/n^0.5568` vs `w*(n)/n^0.58496` must decide; if neither residual is flat,
keep `E = 0.557` as fitted. The note and claim block both say this.

## Unobtainable

**Stolarsky 1977** (SIAM J. Appl. Math 32, 717–730, DOI 10.1137/0132060) is
paywalled behind SIAM, no open preprint found. Recorded in
`research/notes/stolarsky1977_obtainability.md` with the reason and the note
that its content is fully replaced by HJT's theorem + the OEIS A006046 entry +
cross-ref A077464, so no retry is warranted.

## State

85 source files in `research/sources/`, both new files indexed via
`index_document`, durable finding stored in Cognee. The open request
`walsh-spectral-subset-b904` is untouched by this pass (no reachable primary
gives a deterministic weight lower bound needing neither a complexity
hypothesis on h nor switch density — the existing Donoho–Stark, MacWilliams,
Yoshida, and coding-theory-machinery sources remain the state of that line).
