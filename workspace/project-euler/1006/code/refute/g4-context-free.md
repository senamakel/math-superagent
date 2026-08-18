# G4 thesis attack — context-free window-sum test

## Statement tested

Let `W = S_∞[0..N)` be a prefix of the Fibonacci word (with N chosen so the
first Lmin windows contain all k+1 distinct factors), and define

    w_r   = Σ_{j=0}^{k-1} W[r+j] · 10^{k-1-j}     (r = 0..L-k)
    Ψ_k(W) = Σ_r w_r²

The thesis `g4-fixed-dimensional-collapse` (and the run's missing G4) claims
that no fixed-dimensional O(log k) aggregation of Ψ(k) over the k+1 distinct
mechanical intercepts is *known/available*; the sub-question tested here is
whether the *window-scan* formulation of Ψ_k(W) admits a bounded-state
recurrence in r with only O(1) stored scalars.

## Theory used

The rolling window satisfies `w_{r+1} = 10·w_r − y_r·10^k + y_{r+k}`, so
`w_r` is the state of a finite linear recurrence. A bounded-state evaluation
of `Σ w_r²` needs the recurrence's transition to preserve a *quadratic*
invariant (a second-moment transfer matrix). The affine map
`(w,1) ↦ (10w + c_r, 1)` is rank-2; its square-sum transfer is 3-dimensional.
This is the *same* monoid the run already verified
(`monoid-composition-formulas-verified`, `code/lib/ueuclid.py`), which
evaluates `Σ z^i floor((pi+q)/r)²` in O(log) — *provided* the input is a
sequence of affine-floor form. The window digit sequence `y_r` of the
Fibonacci word is NOT of that form in a single intercept: it is the *union*
over k+1 intercepts (G4's core obstruction, already pinned at k=1..3 by
`code/out/pinning_k123.txt`).

## Small exact test executed

`code/refute/small_oracle_thesis_attack.py`:

- oracle F_3 = {001,010,100,101}, Ψ(3) = 20302  ✓ (statement example)
- oracle Ψ(10) mod M = 10699667  ✓ (statement example)
- appending-digit closure collision: the 3-number state
  (count, Σw, Σw²) is NOT closed — two distinct contexts `010` and `101`
  share it at k=2 and diverge on the next digit (`0100` vs `1010`).
  (This is the run's own recorded counterexample, reproduced verbatim:
  `code/out/immediate_oracle_and_counterexample_capture.md`.)
- single-intercept replacement: `mech_psi` vs the m=0-only value differs at
  k=1,2,3 (recorded in `code/out/pinning_k123.txt`).

## Verdict

**No new counterexample found; thesis survives this attack.** The small
exact cases and existing artifacts confirm the recorded obstruction: the
3-number additive summary is not closed, the single-intercept reduction is
false, and no O(1)-state window recurrence for the joint sum is available in
this workspace. The only surviving candidates for a *positive* fixed-
dimensional route remain the adopted approaches (Ostrowski/three-gap closed
form; Rauzy right-special extension recurrence), neither of which is yet a
computed full-size evaluator — so "no fixed-dimensional O(log k) aggregation
is known/available" stands, but as *unproven* rather than *established*.

## Boundary of the claim

The attack tested the additive/single-intercept candidate families, not the
full class of all fixed-dimensional states; a *richer* bounded state
(preserving prefix/suffix boundary contexts) is not ruled out by these cases
— exactly what the thesis itself records as its refutation condition.
