# Rotation of log_3 2 against the no-2 IFS: a middle-digit constraint

```approach
idea: The ternary digit string of 2^n is the base-3 expansion of 3^{{n log_3 2}}.
  Digit-2-freeness = membership of the orbit point 3^theta in a fixed self-similar
  IFS attractor E subset [1,3) (the no-2 set, dim log_3 2). The *middle* block
  condition forces the Kronecker sequence {n log_3 2} into IFS cylinders of
  measure (2/3)^block; by metric theory of irrational rotations (continued
  fractions, Denjoy-Koksma) this can hold only at convergent denominators of
  log_3 2.
mechanism: no-2 on a middle block forces the rotation orbit of theta to lie in
  small IFS cylinders; only convergent denominators of log_3 2 can host such
  good approximations; the witnesses n=0,2,8 should be the exceptional
  good-approximation denominators.
status: refuted
killed-by: The central Diophantine claim is false on evidence. (See hand check,
  research/candidate-precedent-handcheck.md.) Convergent denominators of
  log_3 2 include q = 2 and q = 8 (the two nontrivial witnesses), but also
  q = 1, 3, 19, 65, ... and NONE of the non-{2,8} denominators is digit-2-free:
  q=1 (2^1=2_3 contains 2), q=3 (2^3=8=22_3), q=19 (2^19=524288 has leading
  ternary digit 2, since 3^11=177147 <= 2^19 < 2*3^11=354294).  So
  "n is a convergent denominator" is NECESSARY for the witnesses but utterly
  INSUFFICIENT -- infinitely many denominators fail.  The exclusion of all
  non-{2,8} denominators is the whole conjecture, so the CF/rotation step merely
  restates the problem under a name and supplies no new constraint.
precedent:
  - "Roettger-Ren 2025 arXiv:2511.03861: leading ternary digit of 2^n governed by
     {n log_3 2}; Benford law in base 3; normality of log_3 2 to base 3 is
     UNKNOWN (10^6-digit computational support only)."
  - "Lagarias 2009 (J. London Math. Soc., math/0512006 / jdn080): the 'real
     method' (Thm 1.1) controls only the log_3 X most-significant digits; the
     3-adic method (Thm 1.4) only the log_3 X least-significant. The middle
     ~alpha0 n digits are NOT exploited by either -- this caches the exact gap
     GOAL.md names, but Lagarias states NO Diophantine-approximation constraint
     reaches the middle."
  - "Metric Diophantine approximation / Denjoy-Koksma (Beresnevich-Ramirez-Velani
     2016, https://doi.org/10.1017/9781316402696.002): discrepancy of irrational
     rotations       is an AVERAGE/uniform statement; it says a rotation is
     uniformly distributed, never that a SPECIFIC n crosses a specific cylinder.
     Denjoy-Koksma bounds mean-discrepancy and cannot force n to be any
     particular convergent."
  - "Yu 2021 (Trans. AMS arXiv:1812.04635 / 10.1090/tran/8410): discrepancy of
     irrational rotations applied to binary digits of 3^k -- gives occurrence
     RESULTS (3-term APs of 1-positions) for ALMOST ALL k, not an exclusion of a
     specific n. Shows rotations do produce digit structure, but in the
     occurrence direction, opposite to what this candidate needs."
  - "Saye 2022 arXiv:2202.13256 and Aliyev 2023 (NNTDM 29.3): Benford / uniform
     distribution of leading digits; confirm {n log_3 2} uniformly distributed,
     which is the opposite of 'n forced to be a convergent'."
```

## Verdict

**Refuted, on evidence.** The change of coordinates (`2^n = 3^{n log_3 2}` ⇒
digits of `2^n` = digits of `3^{{n log_3 2}}`) is correct and elementary, and the
no-2 set is genuinely a self-similar IFS attractor of dimension `log_3 2`. But the
*attack* — that the no-2 middle block forces `n` to be a convergent denominator,
and hence the witnesses are exactly the exceptional good approximations — is
false on its face:

- The intended Kepler/lattice interpretation would require `{n log_3 2}` to *equal*
  a special value (the fractional part landing in a specific tiny interval). Metric
  discrepancy (Denjoy–Koksma, Weyl) and all the rotation theory this candidate
  cites describe the *average* behaviour of the whole Kronecker sequence; they never
  force a single specific `n` to be a convergent. The step "can hold only at
  convergent denominators" is not a theorem of the theory — it inverts the usual
  direction (convergents are the *best rational approximations* of `alpha`, and
  `{n alpha}` for a convergent denominator `q` is the *closest* to 0, not a
  constraint that the middle digits be small).
- Empirically the witnesses are *not* singled out: `n=2,8` are convergent
  denominators, but so are `n=1,3,19,...`, and all except `2,8` fail digit-2-freeness.
  The class "convergent denominators of `log_3 2`" strictly contains the
  witnesses and excludes none of the counterexamples that the known bound
  (`n ≤ 2·3^45`) cannot reach — so it carries no exclusion power at all.

This is a genuine middle-digit-attack *shape* (it names the exact gap), and the
IFS/rotation framing correctly identifies where the hard digits are, but the cited
theory (continued fractions + Denjoy–Koksma + normality) is the wrong instrument
for a *pointwise* exclusion: it is average/measure, and the pointwise normality of
`log_3 2` (which would be what makes middle digits random) is **unknown**. So this
candidate is refuted as stated, and its only salvageable residual — "middle digits
are the open target, and no known Diophantine-approximation constraint reaches
them" — is exactly the already-recorded `LAGARIAS-MIDDLE-DIGITS-OPEN` gap, not new.
