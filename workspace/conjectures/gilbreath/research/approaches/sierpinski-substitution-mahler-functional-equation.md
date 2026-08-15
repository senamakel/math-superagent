```approach
idea: Self-similar / substitution-dynamics formulation of the boundary — the
Rule-90 spacetime of the {0,2} interior is the Sierpinski self-similar set, so
the boundary process (edge readout + intruder) is a self-similar dynamical
system under the 2-adic dilation, and the regeneration rate is the solution of a
Mahler (functional) equation, computable via the Perron–Frobenius eigenvector of
the substitution matrix.

mechanism: |
  Two established facts make the boundary self-similar. (1) Inside the {0,2}
  block the halved entries evolve by Rule 90, whose spacetime is the Sierpinski
  gasket: the cell (d, i) is nonzero iff i ⊂ d bitwise, and the pattern at depth
  2^m is the dilation of the pattern at depth 1 by a factor 2^m (Freshman's
  dream / the rule-90-interior-xor claim). (2) The edge readout e_d = XOR-fold of
  the block's bits is the restriction of this Sierpinski pattern to the block's
  right boundary, and the intruder descends by the drain law y_{k+1} = y_k −
  2·[x_k = 2] (established). So the WHOLE boundary state (edge bit, intruder)
  evolves by a deterministic map that commutes with the dilation d ↦ 2^m on the
  interior.

  This is precisely the setting of self-similar dynamical systems: the boundary
  word is a substitution (morphism) word whose letter frequencies are the
  Perron–Frobenius eigenvector of the substitution matrix (Queffélec), and the
  generating function of the (2,4)-event process satisfies a MAHLER functional
  equation F(x) = M(x) F(x^2) + R(x) from the 2-adic self-similarity. Such
  equations are exactly solvable: the singularity at x=1 determines the growth
  rate of Σ_{events} (j_i+1), i.e. the recharge rate the conjecture needs.

  Why it beats what was refuted: the refuted sofic-block-suffix-subshift treated
  the boundary as a FINITE-STATE suffix process (fails: unbounded gap alphabet,
  unbounded block). Self-similar/substitutive systems allow an INFINITE-state,
  self-similar boundary — which is exactly what the unbounded intruder values and
  unbounded jumps are. The refuted Christoffel/Sturmian route needed a BINARY,
  BALANCED word; a substitution word over a finite alphabet can be unbalanced and
  still have computable frequencies. The refuted kernel-method route needed a
  finite homogeneous step set; the Mahler equation handles the 2-adically
  self-similar (hence inhomogeneous but structured) jumps.

status: refuted
side: general-class / dynamical (attacks regeneration — the open half — via the operator's self-similarity, not via primality)
killed-by: |
  REFUTED at its load-bearing premise — that the BOUNDARY process is a finite
  substitution — on the run's own proved facts, plus an arithmetic mismatch
  in what the machinery computes.

  (1) The self-similarity that is real is the INTERIOR's, and it provably
      cannot reach the boundary this approach needs it to reach. Inside a
      {0,2} block the halved entries evolve by XOR/Rule 90 and the pattern at
      depth 2^m is the 2-adic dilation (held claim rule90-interior-xor,
      proved). Kubelka's mod-p self-similarity, Fraenkel-Kontorovich's q-sieve
      and the whole substitution literature document exactly this interior
      structure. But this IS the erosion/structure half. Held claim
      edge-interior-invertibility-sharpened (proved) shows the interior
      pattern cannot even force edge=2 to recur on a controlled schedule (worst
      case edge-2 only at the final length-1 read), and regeneration needs the
      (2,4)-event, which additionally requires intruder=4 at exactly that row.
      The interior self-similarity does not govern intruder timing.

  (2) The boundary word is over an UNBOUNDED alphabet, so no finite
      substitution matrix / Perron-Frobenius eigenvector exists. The boundary
      state is (edge-bit, halved-intruder) and the jump sizes j_i; intruder
      values are unbounded (measured {4,6,12,14} at the giants, and the drain
      law y_{k+1} = y_k - 2[x_k=2] lets any value >= 4 persist for a block's
      whole life), and the jumps are unbounded (j >= 176181 measured). The
      Mahler equation F(x) = M(x)F(x^2) + R(x) with rational M, R and the
      substitution's Perron-Frobenius eigenvalue require a FINITE alphabet;
      the candidate's own falsifier admits this ("may need infinitely many
      letters"). The primes' tail is the canonical non-self-similar, unbounded
      gap structure (see binary-carry-transducer refutation: primes are
      non-automatic, Hartmanis-Shank; Dubbe caps automaticity near-maximal).

  (3) Even granting a finite substitution, the arithmetic is a category error
      for this conjecture. The recharge identity (held claim
      step-law-and-recharge-identity, proved) is b_k = b_1 + sum_{events i<k}
      (j_i + 1) - (k-1); the conjecture is that the EVENT sum outpaces unit
      consumption. The Perron-Frobenius eigenvalue log_2 lambda of a
      substitution word's LETTER FREQUENCIES computes the exponential growth
      of letter counts of an interior pattern; it is not the recharge surplus
      sum(j_i+1) - (k-1), which is a statement about (2,4)-event RATES,
      governed by the intruder, not by interior bit frequencies. So "the
      conjecture is lambda >= 2" mislocates the quantity: lambda controls
      interior structure, and regenerption is a boundary phenomenon.

  Verdict: refuted, killed by (1) the proved interior-only reach of
  Rule-90/Sierpinski self-similarity, and (2) the unbounded boundary alphabet
  making the finite-substitution / Perron-Frobenius / rational-Mahler machinery
  inapplicable. The interior Sierpinski structure is real and already in the
  library (rule90-interior-xor); the boundary regeneration it is asked to drive
  is precisely the non-self-similar part. Do not re-propose.
precedent: |
  - held claim rule90-interior-xor (proved): interior {0,2} block = XOR / Rule
    90 / Sierpinski / Pascal mod 2; pattern at depth 2^m is the 2-adic
    dilation (the real, interior-only self-similarity this approach leans on)
  - held claim edge-interior-invertibility-sharpened (proved): the interior
    pattern cannot force edge-2 on a controlled schedule (worst case only at
    final read), so interior self-similarity does not time regeneration
  - held claim step-law-and-recharge-identity (proved): recharge = sum over
    (2,4)-events of (j_i+1) - (k-1); lambda-from-letter-frequencies is not
    this quantity
  - interior Sierpinski self-similarity literature (real but interior-only):
    Kubelka 2004 (doi 10.1080/00150517.2004.12428445); Fraenkel-Kontorovich
    q-sieves (doi 10.5281/zenodo.8346356); Northshield (hdl 1951/69939);
    the substitution-dynamical-systems / Mahler-equation machinery
    (Queffelec; Mahler 1983; Bell-Chyzak-Coons-Dumas "Becker's conjecture on
    Mahler functions" doi 10.1090/tran/7762) applies to finite-alphabet
    self-similar words, which the boundary is not
  - held claim binary-carry-transducer refutation: primes are non-automatic,
    so the unbounded tail is not finitely self-similar
named-mathematics: Rule 90 / Sierpinski gasket self-similarity, substitution (morphism) dynamical systems, Perron–Frobenius theory, Mahler functional equations, Rauzy/self-affine tilings, Queffélec's letter-frequency theorem
speculative: The load-bearing claim — that the boundary process is genuinely self-similar under d ↦ 2^m with a FINITE substitution (so a Mahler equation with rational M, R exists) — is conjectured. The interior is exactly self-similar; the question is whether the boundary (with its unbounded intruder and unbounded jump sizes) closes to a finite substitution or a controlled infinite one. If the jumps couple the boundary to unboundedly large interior stretches, the Mahler equation may need infinitely many letters.
falsifier: If the boundary word's letter frequencies are not governed by a finite (or finitely-generated) substitution matrix — i.e. the boundary subshift has no Perron–Frobenius spectrum — the functional-equation route collapses. Measured by computing the boundary word's substitutive complexity on the oracle rows before theory.
first-step: |
  From the oracle rows (blocks_depth1000.json, depth 1000, exact integers)
  extract the boundary process: the sequence of (edge-bit, halved-intruder)
  pairs across the live rows, and the jump sizes j_i at each (2,4)-event. Test
  the self-similarity: does the sub-word over rows [2^m, 2^{m+1}) equal the
  2-adic dilation of the sub-word over [1, 2^m)? Compute the substitution (if
  any) generating the boundary word and its matrix's Perron–Frobenius eigenvalue
  λ; the recharge rate is then log_2 λ, and the conjecture is λ ≥ 2 (recharge
  outpaces unit consumption). Cost O(depth × width), one row live. Report the
  largest 2-adic window where the dilation self-similarity holds verbatim, and
  the substitution matrix found (or the first violation that shows the boundary
  is not finite-type).
```
