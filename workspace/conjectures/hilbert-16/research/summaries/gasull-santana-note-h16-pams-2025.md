# Gasull–Santana, "A note on Hilbert 16th problem"

<!-- source: https://ddd.uab.cat/pub/artpub/2025/309367/GasSan24-Postprint.pdf | Proc. AMS 153(2):669–677 (2025), also arXiv:2407.13465 -->

**Monotonicity and realizability of H(n).** Peer-reviewed note (Proc. Amer.
Math. Soc. 2025). Let H(n) be the supremum of the number of limit cycles over
planar polynomial fields of degree n, and π(X) the (countable) number for field X.

## What it establishes

- **Theorem 1**: H(n+1) ≥ H(n) + 1 for all n ∈ N. So H(n) is a **strictly
  increasing function of the degree whenever it is finite**.
- **Theorem 2**: H(n) is realizable by structurally stable fields with only
  hyperbolic limit cycles: (a) if H(n) < ∞ there is a structurally stable X of
  degree n with π(X) = H(n) and all cycles hyperbolic; (b) if H(n) = ∞ then for
  every k there is X(k) with π(X(k)) ≥ k.
- **Proposition 3**: any planar analytic field has an enumerable (≤ ℵ₀) number
  of limit cycles; hence H(n) ≤ ℵ₀ for every n.
- Recalls the Christopher–Lloyd recurrence H(2n+1) ≥ 4H(n) (via the non-invertible
  change (x,y) ↦ (u²,v²) and time rescaling, transplanting cycles into the four
  quadrants).

## Implication for this problem

Establishes structural facts about the Hilbert number independent of its (open)
finiteness: monotone in n, realised in the robust hyperbolic regime. The
Christopher–Lloyd H(2n+1) ≥ 4H(n) recurrence is the concrete mechanism behind
the n² log n growth. The count of limit cycles is at most countable.

**Evidence class**: sourced (peer-reviewed postprint held full
  `research/sources/gasull-santana-note-h16-pams-2025.full.md`).
**Falsifier**: a published error in the monotonicity/realizability argument.
**Holds-here**: yes.

Claims ledger: `h16-strong-monotone-gasull-santana`.
