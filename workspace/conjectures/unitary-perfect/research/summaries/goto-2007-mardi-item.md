<!-- source: https://portal.mardi4nfdi.de/wiki/Item:Q2478044 | converted from HTML -->

# Goto (2007) — MaRDI/zbMATH review record (corrected note)

Full item page: [[goto-2007-mardi-item.full]] (MaRDI Q2478044; zbMATH DE
5249947; DOI 10.1216/RMJM/1194275935). The article itself is paywalled at
Project Euclid (`research/summaries/goto-2007-upper-bounds.md` — a purchase
page with no content).

## What the review text establishes (zbMATH review by P. Haukkanen, quoted verbatim in the MaRDI item)

- A UPN (resp. UHN = unitary harmonic number) `N` with `k` distinct prime
  factors satisfies
  **`N < 2^{2^k}` (UPN)** — the exponent is `2^k`, i.e. `N < 2^{2^k}` — and
  `N < (2^{2^k})^k` (UHN).
- The paper lists all UHNs with `H*(N) ≤ 50`; the UHN-infinitude question is
  open.

## Correction of the library's earlier record

`research/notes/library-acquisition-cycle-1.md` and the Goto-papers entry
attributed `N < 2^{2^k}` to the *MaRDI structure page* and warned that a
"`N < 2^{k·2^k}`" wording found in a search hit was a misattribution from
A006086 (unitary harmonic numbers). The held review text now **confirms the
UPN bound `N < 2^{2^k}` (exponent `2^k`)** — i.e. the UPN bound is
`log_2 N < 2^k`, the sharper of the two forms that were in play; the
`k·2^k` form is the UHN bound (`(2^{2^k})^k`), both attributed to Goto 2007 by
a primary review. Restating the UPN bound as `N < 2^{k·2^k}` would
**overstate** the exponent; the correct UPN form is `N < 2^{2^k}`.

## Bearing on this run

**Finiteness-adjacent, weak for the actual question.** For a sixth UPN (if it
exists) with `k` distinct primes, `N < 2^{2^k}` is a doubly-exponential upper
bound; the run's *lower* bounds (Subbarao 1970 `a ≥ 11`, Wall 1988
`ω(odd) ≥ 9`) are stronger in the direction that matters (there is no known
upper bound on `ω`, so this cannot close anything). It confirms the
bibliographic control of Goto 2007 and corrects the earlier misattribution
record. It does not touch `H_even` or the divisor-level `Φ_{4p}(2)` gap.

```claim
id: goto2007-upper-bound-upn-2-2^k
statement: A unitary perfect number with k distinct prime factors satisfies
  N < 2^(2^k); a unitary harmonic number with k distinct prime factors
  satisfies N < (2^(2^k))^k. (Goto 2007, RMJM 37(5) 1557-1576, via the zbMATH
  review text held in the MaRDI item.)
hypotheses: N UPN (resp. UHN) with exactly k distinct prime factors
holds-here: yes as a sourced upper bound; it is doubly exponential in k, so it
  gives no finiteness and no constraint on the run's lower-bound directions
status: asserted
bearing: bibliographic + confirms the earlier misattribution correction; the
  run's lower bounds a >= 11 and omega(odd) >= 9 are the stronger instrument
  for any sixth UPN
anchor: research/sources/goto-2007-mardi-item.full.md
answers: goto2007-upn-bound-exact-form
```