# Digital (automatic-sequence) equidistribution of primes as the fold's input

```approach
idea: >
  The parity barrier that killed every analytic route is specific: it is about
  the ADJACENT pair (q_j, q_{j+1}) mod 4, a two-point consecutive-index object
  that ABGS 2011 §9 say L-functions cannot reach. But the fold never reads
  adjacent indices — it reads h at DIGITAL sets M_d = { n-1-d+o : o ⊆ d }, i.e.
  primes q_j whose INDEX j lies in a submask (2-automatic) set. The distribution
  of the primes along digit-defined / automatic sets is a DIFFERENT input class,
  with its own named engine: Mauduit-Rivat's theorem that the primes are
  equidistributed in residue classes of the sum-of-digits function (and the
  Drmota-Mauduit-Rivat extension to automatic sequences / q-multiplicative
  functions). Claim mauduit-rivat-prime-digit-sum-equidistributed is already on
  disk. The proposal: price whether this digital equidistribution supplies the
  submask-index correlations the second moment E[S(n)^2] = O(n) needs, as an
  input strictly weaker than (and orthogonal to) the adjacent-pair switch density
  that is the known dead end.
mechanism: >
  The second moment E[S(n)^2] = sum_{d,d'} prod_{j in M_d XOR M_{d'}} u_j with
  u_j = chi_4(q_j) chi_4(q_{j+1}). By the run telescope each cell is a product
  over runs of chi_4(q_a) chi_4(q_b) at INDEX pairs a,b drawn from digital
  (submask-derived) sets, with the separations being powers of 2. Reorganizing
  the double sum by the digital set structure turns the needed cancellation into
  a statement about the joint distribution of chi_4(q_j) as j ranges over
  automatic sequences and their translates. Mauduit-Rivat (2009, primes with
  prescribed digit sum; Drmota-Mauduit-Rivat 2019 for automatic sequences; the
  later work of Drmota-Rivat on primes in Beatty/digital sets) is the precise
  named machinery for ONE-point digital equidistribution of primes. The open
  price: one-point digital equidistribution alone cannot force a two-point cell
  (this is the mod2m-lift-onepoint refutation), so the route must name the
  TWO-point digital statement it needs and check whether the Mauduit-Rivat
  circle method (which does handle correlations along digit constraints in some
  regimes) reaches it. If yes, this is a genuinely new, strictly weaker input;
  if the needed two-point digital statement is itself as hard as the adjacent
  switch density, the route is priced out honestly.
status: refuted
killed-by: >
  Refuted on evidence — this candidate was priced to fail honestly, and the
  two-point digital literature, which genuinely exists, fails precisely at the
  index-vs-value transfer. (1) THE TWO-POINT DIGITAL LITERATURE IS REAL BUT IS
  ABOUT THE WRONG STATISTIC. Unlike candidates 1 and 2, the two-point digit-sum
  statement is NOT missing: Toumi 2025 (arXiv:2504.02784, level of distribution
  of exp(2 pi i l s_q(n)/b) correlations, van der Corput + Gowers norms of the
  automatic sequence), Spiegelhofer 2014 (thesis: correlations of s_q(n) and
  s_q(n+k) in residue classes, with power-saving error), Sobolewski-Spiegelhofer
  2024 (arXiv:2411.07779, decomposition of the sum-of-digits correlation
  measure gamma_t(s(n+t)-s(n))), Aloui-Mauduit-Mkaouar 2015 (joint distribution
  of S(n),S(n+1) in APs), and the classical Bésineau / Gelfond two-base joint
  distribution (J. Number Theory 1998, S_q(n) == a_i mod m_i simultaneously).
  But EVERY one controls the digit-sum FUNCTION s_q evaluated at INTEGER
  arguments n, n+k — i.e. at prime-INDEX integers, not at prime VALUES. (2) THE
  FOLD NEEDS INDEX-DOMAIN MOD-4 RESIDUE CORRELATIONS, NOT VALUE-DOMAIN DIGIT
  SUMS. The object E[S(n)^2] = sum_{d,d'} prod chi_4(q_a) chi_4(q_b) is a
  correlation of the residue of the j-th prime, indexed over submask index sets
  — the map j -> q_j -> chi_4(q_j), a composite of the prime-index and prime-
  value maps. Mauduit-Rivat's statistic s_q(p) is the digit sum of the prime
  VALUE; the fold reads GAP PARITY at index positions. This is precisely the
  transfer the library holds is absent (mr-green-set-paradigm-not-transfer: "no
  transfer exists between s_q(p) and the index-domain gap-parity h") and the
  one-point-does-not-determine-two-point obstruction (mod2m-lift-onepoint:
  one-point digital equidistribution cannot force a two-point cell). The
  two-point digital theorems above never evaluate chi_4 at prime-index
  submask positions; they evaluate s_q at integer shifts n+k. There is no
  bridge in the located literature from "s_q is jointly equidistributed at
  integer arguments" to "chi_4(q_j) correlates over submask index sets", and
  that bridge is exactly the value-vs-index gap GOAL priority 2 named. (3) THE
  ROUTE IS PRICED OUT HONESTLY: the needed two-point digital statement about
  the residues at prime-INDEX submask positions is as open as the adjacent
  switch density, which the candidate itself concedes. The honest verdict is
  refuted, not "no evidence": the evidence is that the two-point digital
  machinery reaches digit sums at integer arguments and stops there.
precedent: >
  Mauduit-Rivat, "Sur un probleme de Gelfond: la somme des chiffres des nombres
  premiers", Ann. Math. 171 (2010) 1591-1646 (Theoremes 1-3, on disk at
  research/sources/mauduit_rivat_gelfond_somme_chiffres_premiers_primary.full.md);
  Green, "Three topics in additive prime number theory" (arXiv:0710.0823, Thm
  2.1.1, binary digit-sum of primes 50/50 with power saving); Drmota-Mauduit-
  Rivat, "Primes with an average sum of digits", Compositio Math. 145 (2009)
  DOI 10.1112/s0010437x08003898. TWO-POINT digital (real, wrong object): Toumi,
  arXiv:2504.02784 (level of distribution of s_q correlations); Spiegelhofer,
  "Correlations for numeration systems", PhD thesis, TU Wien 2014;
  Sobolewski-Spiegelhofer, "Decomposing the sum-of-digits correlation measure",
  arXiv:2411.07779; Aloui-Mauduit-Mkaouar, "Repartition simultanee de S(n) et
  S(n+1) dans les progressions arithmetiques", Ramanujan J. 2015, HAL-01272915;
  Bésineau, Acta Arith. 20 (1972) and the J. Number Theory 1998 joint q-base
  distribution. In-workspace (established): mr-green-set-paradigm-not-transfer
  (the value->index transfer is absent); mod2m-lift-onepoint (one-point does
  not determine two-point for fold cells); mauduit-rivat-prime-digit-sum-
  equidistributed (the one-point model theorem); abgs-p1-wide-open / switch
  density is the known barrier.
falsifies: >
  Closed on the evidence that the two-point digital machinery (which exists)
  evaluates s_q at integer arguments and never reaches chi_4 at prime-INDEX
  submask positions. A reopening must name a theorem that controls correlations
  of the primes' residues indexed by the prime COUNT over submask index sets —
  not the digit sum at integer shifts. None of the located two-point digital
  literature does; the nearest (Maynard, "Digits of primes", 2016 survey, and
  the Drmota-Mauduit-Rivat line) stay in the value domain.
```

## Grounding note (research pass, this dossier)

This candidate was honestly priced to fail, and the two-point digital
literature — which is genuinely richer than the one-point Mauduit-Rivat result —
closes it with precision: every two-point statement (Toumi 2025, Spiegelhofer
2014, Sobolewski-Spiegelhofer 2024, Aloui-Mauduit-Mkaouar 2015) controls the
digit-sum function at integer arguments, while the fold needs mod-4 residue
correlations at prime-index submask positions. The value↔index transfer the
fold requires is exactly the gap the library already names
(mr-green-set-paradigm-not-transfer, mod2m-lift-onepoint). Verdict: refuted on
evidence.
