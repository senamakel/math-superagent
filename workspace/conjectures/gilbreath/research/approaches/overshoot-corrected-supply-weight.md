# overshoot-corrected-supply-weight

```approach
idea: |
  The true supply count nu2 (number of 2s in the maximal {0,2} suffix of the
  right diagonal) is the F2 fold weight F minus an EXACT correction term O:

      nu2 = F - O,
      F   = #{k in [2, n-1] : delta_k == 2 (mod 4)},      (fold/parity cells)
      O   = #{k in [2, tau-1] : delta_k == 2 (mod 4)}     (cells OUTSIDE the
                                                            maximal {0,2} suffix
                                                            that are == 2 mod 4),

  where tau is the start of the maximal {0,2} suffix. O splits into stray 2s
  (delta_k = 2 outside the suffix) and overshoot (delta_k = 6, 10, ... outside
  the suffix). Every refuted parity approach — subset-zeta, KKL/influence,
  code-min-distance, and the broken adopted identity nu2 = #{zeta=1} in
  `dyadic-linear-complexity-supply` — dropped O. The fold bit fires on halved
  values that are odd, i.e. actual values 2, 6, 10, ...; only the suffix
  restriction and the correction term O together recover the exact count. The
  magnitude content of the conjecture is carried ENTIRELY by the overshoot
  component of O, and that component is governed by the run's proved
  descent/excess machinery, not by any new parity theory. This is the
  exact-count lift the three refutations pointed at but did not name.
mechanism: |
  Three proved facts compose; none of them is conjectural.

  (1) [proved] rule90-interior-xor: inside any {0,2} block the halved fold is
      XOR / Rule 90, so an even diagonal cell delta_k has delta_k == 2 (mod 4)
      iff its halved value is odd iff the Pascal-mod-2 fold bit zeta(h)[k] = 1.

  (2) [proved] mod-lift-obstruction: mod 4 is the ceiling of the free
      linearization, and it CONFLATES the value 2 with 6 (both == 2 mod 4);
      so the fold bit alone cannot certify delta_k = 2.

  (3) [proved + Lean] descent/excess renormalization: the intruder column
      drains exactly c_{k+1} = |c_k - e_k| with e_k in {0,2} (step law, drain
      law), and the halved excess t = max(0, h-1) evolves under
      E(t) = (D t - 1)_+ with max-excess non-increasing
      (excess-renorm-identity-proved). Overshoot cells (delta_k >= 6) are
      exactly the tail cells with excess t >= 2, so the overshoot component of
      O is controlled by the proved max principle and drain law.

  CONVENTION LOCK (important, and where the earlier attempts conflated two
  objects). Distinguish two parity statistics:

      F_diag = #{k in [2, n-1] : delta_k ≡ 2 (mod 4)}   (the ACTUAL diagonal's
              parity count — no linearization assumption, always well-defined);
      F_fold = the F2 Pascal/Rule-90 fold weight of the gap bits h over the
              fixed ancestor window (rule90fold.fold_weight) — the linearized
              statistic.

  These AGREE on the maximal {0,2} suffix (rule90-interior-xor is valid there),
  but may differ OUTSIDE the suffix, where the mod-4 linearization can fail
  (mod-lift-obstruction). The exact decomposition below is stated in terms of
  F_diag; the relation F_fold vs F_diag is itself measured, not assumed.

  The decomposition nu2 = F_diag - O is immediate and exact. On one fixed
  diagonal body [2, n-1] with tau the start of the maximal {0,2} suffix
  (suffix entries are 0 or 2), every cell splits by position relative to tau:

      F_diag = #{k in [2, n-1] : delta_k ≡ 2 (mod 4)}
             = #{k >= tau : delta_k ≡ 2 (mod 4)} + #{k < tau : delta_k ≡ 2 (mod 4)}.

  For k >= tau the entry is 0 or 2, so "≡ 2 (mod 4)" iff "= 2"; that set is
  exactly nu2. Hence

      O := F_diag - nu2 = #{k in [2, tau-1] : delta_k ≡ 2 (mod 4)},

  the cells OUTSIDE the suffix whose value is ≡ 2 (mod 4). They split disjointly
  into

      (a) stray 2s outside the suffix:  delta_k = 2, k < tau;
      (b) overshoot outside the suffix:  delta_k ≡ 2 (mod 4), delta_k >= 6, k < tau.

  Both live only before tau (a suffix cell cannot overshoot, and a stray 2 after
  tau would contradict maximality). (b) is the genuine magnitude content —
  cells of value 6, 10, ... with excess t >= 2 — and is governed by the proved
  descent/excess machinery. (a) is convention bookkeeping and must be measured,
  not assumed zero. Hence the open supply bound nu2 >= c*n SPLITS into parts
  of genuinely different character:

      (i)  parity side:    F_diag >= c'*n (and the gap-fold F_fold tracks it)
           — the named-open ABGS 2011 s9 two-point consecutive-prime mod-4
           switch lower bound is exactly the statement on the switch/fold side;
      (ii) magnitude side: O <= (c' - c)*n — NEW, and the attackable half:
           components (a) and (b) are governed by the proved descent/excess
           dynamics, so a bound on O may follow from Lemma 5.4's exact drain +
           the excess max-principle WITHOUT any prime-gap hypothesis beyond the
           switch bound. Component (a) is a suffix-position bookkeeping term.

  Why this beats the refuted neighbours: it does not throw away magnitude — it
  isolates magnitude in O and gives O a proved dynamical law. It also repairs
  the broken adopted identity nu2 = #{zeta=1} (dyadic-linear-complexity-supply)
  by naming the exact correction term O, which is what that approach's
  "faithful shadow" evidence was implicitly measuring.
status: adopted
side: supply side (regeneration) — general-class exact decomposition; only step
  (i) carries a prime hypothesis (the switch bound)
named-mathematics: |
  mod-4 linearization of the even interior (Pascal / Rule-90 fold); the
  subset-zeta / Mobius transform over F2 and its exact integer weight; the
  descent/absorption lemma (Lemma 5.4) and the excess-height renormalization
  E(t) = (D t - 1)_+; the max principle for the tail excess.
speculative: |
  (i) is named-open (ABGS 2011 s9). (ii) is the NEW conjecture: O = o(F_diag) on
  the primes, and O <= (c' - c)*n for the needed c. The exact decomposition
  nu2 = F_diag - O is PROVED (immediate); the bound on O is the target and is
  NOT proved, and the coincidence F_fold vs F_diag outside the suffix is
  measured, not assumed. The existing 'faithful shadow' measurement
  (dyadic-separating-invariant-three-strings: true nu2 within 0-3 of the 2/4
  reconstruction at every sampled n) is weak evidence that O is small on the
  primes, but O must be measured directly — that is the decisive first step.
falsifier: |
  (a) the identity nu2 = F_diag - O failing on the oracle diagonal would refute
      the decomposition — but it is immediate, so a failure means a convention
      error, not a mathematical refutation;
  (b) O NOT small: if O grows like c''*n with c'' close to F_diag/n, the parity
      approaches were not dropping a small error but certifying the wrong
      object outright, and step (ii) must carry the whole bound, making the
      route as hard as before;
  (c) O <= (c'-c)*n not derivable from the descent/excess machinery even under
      the ABGS switch bound. NOTE component (a) is handled by measuring it
      directly, not by assuming it is zero.
first-step: |
  tool_builder, today (O(n^2) incremental right diagonals, one diagonal live at
  a time; report sieve, nmax, and worker count in the capture):

  1. Write code/out/overshoot_decomposition.py using lib.rightdiag
     (delta_diagonal, cycle_and_nu2) and lib.gilbreath.primes_up_to. For each n
     compute on ONE diagonal delta(q_n): true nu2 (cycle_and_nu2),
     F_diag = #{k in [2, n-1] : delta_k == 2 (mod 4)}, O = F_diag - nu2, and the
     direct counts O_a = #{k in [2, tau-1] : delta_k = 2},
     O_b = #{k in [2, tau-1] : delta_k == 2 (mod 4) and delta_k >= 6};
     assert O == O_a + O_b (0 violations expected — the exact identity).
     Separately compute the gap-fold F_fold = fold_weight_h(h, n-2) and report
     |F_fold - F_diag| per n — the outside-suffix linearization mismatch.

  2. Run on: the real primes (sieve 1e6, nmax 5000); Thue-Morse 2-then-odds
     (nmax 4000); the period-3 odd-factor word; and the consecutive-odds
     control (F_diag must be 0 there — a sanity check, since every diagonal
     entry is 0 or 2). Tabulate O/n, O_a/n, O_b/n, F_diag/n, nu2/n, O/F_diag,
     and |F_fold - F_diag|/n.

  3. DECISIVE test: is O = o(F_diag) on the primes (overshoot negligible, parity
     approximately exact), or does O carry real density (parity is the wrong
     object)? Report the measured O density and state which reading the numbers
     support — never 'proved'. This single measurement decides whether the ABGS
     switch bound (parity side) suffices up to a provable small error, or
     whether the magnitude term is the whole problem.
precedent: |
  - rule90-interior-xor (proved: halved fold = XOR inside the block)
  - mod-lift-obstruction (proved: mod 4 conflates 2 with 6)
  - excess-renorm-identity-proved (proved + Lean: E(t) = (Dt-1)+, max principle)
  - step-law-theorem-proved (proved: c_{k+1} = |c - e|, drain law)
  - g-supply-transfer-measured (checked: true nu2/w in [0.689, 0.867])
  - abgs-2011-s9-mod4-switch-limit-open (named-open: the parity side (i))
  - dyadic-separating-invariant-three-strings (checked: the 'faithful shadow'
    evidence that O is small on the primes)
  - supersedes the broken identity nu2 = #{zeta=1} in
    dyadic-linear-complexity-supply (refuted by this run's own measurements)
```

## Convergence note

Research refuted all three of this round's candidates, and the three refutations
share one through-line: each candidate certifies a scale-invariant or
mod-4-parity object, never the exact value `2`. The same finding exposes the
run's own **adopted** supply identity `nu2 = #{zeta=1}`
(`dyadic-linear-complexity-supply`) as the same conflation — the fold bit
`zeta(h)[k]` fires on halved values odd (`2, 6, 10, ...`), not on cells exactly
`2`.

The synthesis above is the third option neither side named: keep the F2 fold
structure (which is right), but lift it from parity to the **exact** count by
the correction term `O`. The magnitude content is not thrown away — it is
isolated in `O` and given a proved dynamical law (the descent drain and the
excess renormalization). This turns the open supply bound into two parts: the
named-open ABGS switch bound (parity) and a **new** overshoot bound `O ≤ (c'−c)n`
that may be provable from Lemma 5.4's exact drain and the excess max-principle.

### Caveat recorded for the first-step verifier

The refutation of the Boolean-influence candidate rests on the measured numbers
"Thue-Morse true nu2(100)=27 vs fold count 7". That pair is **internally
inconsistent as stated**: a cell of value exactly `2` is `≡ 2 (mod 4)`, so
`#{cells exactly 2} ≤ #{cells ≡ 2 (mod 4)}` must hold on one fixed diagonal —
`27 ≤ 7` cannot. One of the two numbers was computed on a different convention
or a different object. The structural refutation does not depend on those
numbers (mod-lift-obstruction is proved independently), but the first-step
verifier should compute all three quantities (`nu2`, `F`, `O`) on **one**
diagonal under **one** convention, which is exactly what settles it.
