# Stolarsky 1977 — obtainability note

**Not obtainable locally; do not retry.**

K. B. Stolarsky, "Power and exponential sums of digital sums related to
binomial coefficient parity", SIAM J. Appl. Math. 32 (1977) 717–730,
DOI 10.1137/0132060.

- Paywalled behind SIAM (the DOI resolves to a SIAM landing page with no free
  PDF). No preprint is archived on arXiv or any open repository found by
  search. JSTOR carries it under institutional access only.
- **Its content is fully replaced by sources already in the library.** The
  asymptotic/log-periodic structure of the odd-Pascal-entry count F₂ (OEIS
  A006046) that Stolarsky's paper establishes is now carried:
  - as a *theorem* by Hwang–Janson–Tsai 2024 (arXiv:2408.06817), Thm 2.2:
    `F_2(n) = n^ρ·P(log_2 n)`, ρ = log₂3 − 1 = 0.58496, explicit 1-periodic P
    (`research/sources/hwang_janson_tsai_periodic_minimum_binomial_modp.full.md`);
  - as the OEIS A006046 entry's asymptotics comment (`a(n) = n^{log₂3}·G(log₂n)`,
    Cloitre/Finch, with Sloane's "for the asymptotics see Stolarsky (1977)")
    (`research/summaries/oeis_a006046.md`);
  - as the canonical digital-sum reference (Stolarsky's own `S_d(N)` power-sum
    asymptotics later treated by Stein and others) — a side aspect the run does
    not need.
- The one thing this library would take from the primary that the substitutes
  do not state verbatim is Stolarsky's own proof that the lim-sup is 1 and
  lim-inf ≈ 0.812556 (Harborth's constant for β₂); that bound is stated and
  used in HJT (line ~109) and in the OEIS cross-ref A077464, so the *content*
  is held. The run's log-periodic hypothesis needs none of Stolarsky's
  method beyond what HJT's theorem already provides.

Concluded: no value in further attempts at `10.1137/0132060`.

Files: `research/summaries/hwang_janson_tsai_periodic_minimum_binomial_modp.md`,
`research/summaries/oeis_a006046.md`.
