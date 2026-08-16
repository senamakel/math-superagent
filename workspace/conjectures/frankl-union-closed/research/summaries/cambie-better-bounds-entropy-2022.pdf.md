# Cambie, "Better bounds for the union-closed sets conjecture using the entropy approach" (arXiv:2212.12500)

**Full text**: `research/sources/cambie-better-bounds-entropy-2022.pdf.full.md`
(821 lines, full body, v2 dated 16 Feb 2025).

## What the body establishes (verified in full text)

```claim
id: cambie-0-38234-published-route
statement: Using dependent samples (Sawin's suggestion) with the entropy approach,
  the union-closed conjecture holds with constant c ≈ 0.3823455 (> (3−√5)/2).
  Core (Question 2, Sawin): the maximum c for which ∃α∈[0,1] with, for p,q,r
  identically distributed [0,1]-valued, expectation < c, p⊥q but p,r not necessarily
  independent,
    (1−α)E[H(p+q−pq)] + α E[H(max(p,r,min(p+r,1/2)))] ≥ E[H(p)].
  Cambie solves Question 2 exactly, improving the constant. Theorem 3: F ⊂ 2^[n]
  nonempty union-closed ⟹ some i appears in ≥ c|F| sets, c ∼ 0.3823455.
  Method: reduce the critical distributions to support ≤ 3 values (3.1, 3.2), then to
  a 4-variable minimisation verified with computer; §3.4 reduces to a 2-variable
  minimisation (combining with Yu's strategy) solved numerically with graphical
  confirmation. Extremal distribution is atomic (2-element support) in one regime.
hypotheses: F union-closed; dependent-coupling class; the 2D/4D minimisation is
  computer-verified, not a fully rigorous symbolic proof (Cambie states this is
  unnecessary for a bound that is not 1/2).
holds-here: true
status: sourced (Theorem 3 proved in body; the local-min estimation is numerically
  verified, which Cambie notes — "slightly less rigorous" than [AHS])
bearing: independent preprint route to Yu's 0.38234 record value; Cambie's value
  t̂_max ≈ 0.3823455334 is the exact ceiling the run's uc-coupling scorer clamps to.
anchor: research/sources/cambie-better-bounds-entropy-2022.pdf.full.md, Question 2,
  Theorem 3, §3.4 two-variable verification
```

## Relevances

- Cambie (arXiv:2212.12500) together with Yu (arXiv:2212.00658, Entropy 2023)
  pinned the dependent-coupling record ≈ 0.38234. Yu is the published one.
- `research/ROOT.md` cites Cambie's 0.3823455; the actual body confirms it. Liu's
  further 0.38271 remains conditional/unpublished.
- The "slightly less rigorous" note is recorded: Cambie's constant rests on a
  computer-verified minimisation, not a fully symbolic proof — matching how the run
  treats `yu-gamma-half-is-phi-over-2` (exact for the α=0 collapse; global sup
  numerical-only).
