# Cross-prime minus-class divisibility vs Wieferich / irregularity — correlation check

Program: `code/pattern_crossprime_corr.py` → `code/out/pattern_crossprime_corr.captured.txt`.
Exact integer arithmetic only. h^-(Q(zeta_p)) reused from the already-captured,
OEIS-A000927-matched exact values (all 45 odd primes <= 199). Bound stated:
**all odd-prime pairs p < q <= 199, 990 pairs.**

## Direction of the double-Wieferich congruences (kept explicit)
For a pair of odd primes (p, q):
- "q is a Wieferich prime base p"  ⟺  p^(q-1) ≡ 1 (mod q²)
- "p is a Wieferich prime base q"  ⟺  q^(p-1) ≡ 1 (mod p²)
- double-Wieferich ⟺ both.
The question's "q being a Wieferich prime base p" is the first of these.

## Exact numbers (over p < q <= 199, 990 pairs)

Base rates:
- q | h^-(p)              : 4 pairs (0.40%)
- p | h^-(q)              : 41 pairs (4.14%)
- q Wieferich base p      : 8 pairs (0.81%)
- p Wieferich base q      : 45 pairs (4.55%)
- double-Wieferich (both) : 0 pairs  (minimal pair (83,4871) is outside the bound)

Contingency  q|h^-(p)  ×  q-Wieferich-base-p:
- both        : 0
- divis only  : 4
- wieferich only : 8
- neither     : 978
- P(divis | wieferich) = 0/8 = 0   (base P(divis) = 0.004)

The 4 pairs with q | h^-(p), and their flags (all false for every Wieferich
direction, all regular-regular):
- (47,139):  h^-(47)=695 = 5·139
- (73,89):   h^-(73)=11957417 = 89·134353
- (89,113):  h^-(89)=13379363737 = 113·118401449
- (163,181): 181 | h^-(163)
Every one of these FAILS both single-Wieferich congruences (hence fails
double-Wieferich), and both primes in each pair are REGULAR (p ∤ h^-(p), q ∤ h^-(q)).

## What this establishes (and does not)

- **No correlation is observable between q | h^-(p) and q being a Wieferich
  prime base p in this range**: the two events never co-occur (0/990). This is
  the direction the claim crossprime-hminus-divisibility-sweep already stated
  for the unique (47,139) survivor; it is now stronger — ALL four
  divisibility-pairs are Wieferich-free, not just the survivor.
- **No correlation with irregularity either**: none of the four divisibility
  pairs involves an irregular p or q; all are regular-regular.
- **This is a small-sample null, NOT evidence of negative correlation.** Both
  events are rare (0.4% and 0.8%). Under independence the expected number of
  co-occurrences over 990 pairs is ~0.03, so observing 0 is fully consistent
  with independence. We cannot distinguish "no correlation" from "positive
  correlation too weak to see in a 0.03-expectation sample." That is the honest
  reading; a fit here would be fabrication.

## Why a bigger run would not change the mathematical picture
Extending the bound (recomputing exact h^-(p) toward 300) would only replace
a 0.03-expected-coincidence sample with, say, a 0.1-expectation one: still
unable to separate independence from a weak correlation, and the cross-prime
h^- forcing is already dead as a disciplinary tool (the chisel school's
dead-end: the forcing is not sourceable, and at the minimal double-Wieferich
pair (83,4871), Cl^-(Q(ζ_83)) is coprime to both exponents). So scaling this
null yields nothing new; the useful output is the negative it already gives.

## Consistent with established findings
The chisel-school dead-end board post: the cross-prime minus-class forcing is
not a consequence of double-Wieferich, and at (83,4871) the relevant class
group is coprime to both exponents. This run's data is consistent: in the whole
computable small range, the q | h^-(p) accidents pick out exactly the regular,
Wieferich-free pairs, i.e. the divisibility carries no information about the
Wieferich structure that the descent claims to need.
