# Pattern-finder report on PE591 data (n = 10^13, all 90 non-square d in [2,99])

Data source: /workspace/results_full_bothsides.txt (90 rows: d, b, a, |a|; S=526007984625966).

## Tools run
- `analyze_sequence` on |a_d| (90 terms): not low-degree polynomial; differences never
  constant. `analyze_sequence` on b_d (90 terms): same, no polynomial structure.
- `find_linear_recurrence` (max order 8) on |a_d|: NO constant-coefficient linear
  recurrence of order <= 8 fits all 90 terms.
- Conclusion: neither |a_d| nor b_d is polynomial or low-order linearly recurrent
  in d. This is expected — each d is an independent inhomogeneous-approximation
  outcome. No derivation should be attempted from a recurrence-in-d.

## Laws verified EXACTLY over all 90 terms (90/90, independent of the solver)

Let a_d, b_d be the optimum with sign kept, |a_d| = |I_d|. Verified at 60-digit mpmath.

1. **Sign-opposition.** sign(a_d) = -sign(b_d) for all 90 d (45 with b>0,a<0; 45 with b<0,a>0).
   Equivalently I_d = a_d is always negative when b_d positive and vice versa.

2. **Master |a| identity.** |a_d| = |nint(b_d*sqrt(d) - pi)| (90/90). Also
   |a_d| = nint(|b_d|*sqrt(d)) - 3*sign(b_d) (90/90). Both are the same statement
   (pi = 3 + {pi} and the integer digit {pi} ~ 0.14 < 1/2 so nint shifts by exactly 3).

3. **m^2 scaling law** (re-confirmed): for d1 = m^2 * d0 both non-square in range,
   |a_{d1}| = |a_{d0}|  iff  m | b_{d0};  and when equal, b_{d1} = b_{d0}/m.
   36/36 pairs hold. (Gives b-dependence: |a| ~ |b|*sqrt(d0), so |a| invariant under
   scaling iff b scales inverse-squarely, i.e. b_{m^2 d0} = b_{d0}/m.)

4. **Equal-|a| groups.** 72 distinct |a| values; 15 groups of size >= 2. All are
   explained either by the m^2-scaling law (e.g. d in {2,8,32,50} share 6188084046055)
   or by genuine coincidence failing the scaling rule (12-75, 48-75, 8-50, 32-50).

## Re-sum cross-check (independent of solver accumulator)
S recomputed as sum_d |nint(b_d*sqrt(d)-pi)| = 526007984625966. Matches the printed S.

## Cabanillas-structure reminder (from memory.md, not re-derived here)
b_d = the Cabanillas Prop 9/10 candidate minimizing ||b*alpha_d - beta|| over
0<=b<=L (and the beta'=1-beta side for b<0). This is the derivation basis; the
above laws are downstream consequences one can use to sanity-check output (any
row violating laws 1-2 is an immediate red flag).
