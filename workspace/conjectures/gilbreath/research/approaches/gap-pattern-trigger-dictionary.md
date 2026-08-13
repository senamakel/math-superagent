```approach
idea: gap-pattern-trigger-dictionary
mechanism: |
  This is on the RECHARGE side, and it attacks the recharge problem from the
  only place the record says it is still open: bound the rate of (2,4)-events
  from below using ONLY constraints on the STARTING sequence (the prime gaps),
  not the depth structure of the row evolution.

  The (2,4)-event — the unique block-growing move, established this run with
  zero failures to depth 1000 — is the exact local condition

      A_k(b_k) = 2  and  A_k(b_k+1) = 4.

  Both entries are integer functions of a WINDOW of the starting row A_0. Since
  the operator is local (one cell depends on two cells above), the entries of
  row k in columns 1..t depend only on the first k+t+1 terms of A_0, i.e. on
  the first k+t prime gaps. Therefore a (2,4)-event at row k <= t_0 is a
  finite, explicit constraint on the first ~2 t_0 prime gaps. This turns the
  recharge problem into a FINITE DICTIONARY question:

      find a finite set of short GAP PATTERNS P_1, ..., P_m (each a finite
      string of halved prime gaps) such that
        (a) each P_i PROVABLY forces a (2,4)-event within t_i rows (checked by
            exact symbolic row computation over the small window, not by
            enumerating the answer space — the window has fixed size t_i + 2);
        (b) the prime gap sequence contains a translate of some P_i at least
            every G positions (a gap-statistics statement, stated as an
            explicit hypothesis).

  Then the (2,4)-event rate is >= 1/G, and combined with the exact recharge
  identity b_k = b_1 + sum (j_i + 1) - (k-1) this gives a regeneration-rate
  lower bound. Since each event contributes j_i + 1 >= 1 to the recharge sum,
  an event every <= G rows plus the observed fact that large gaps produce large
  j (the jump mass) is precisely the missing half of the balance.

  Named mathematics: local sufficient conditions (pattern triggers), exact
  symbolic iteration of the difference operator on a bounded window (a finite
  computation whose cost is fixed by t_i, independent of the prime bound), and
  a frequency/lower-density hypothesis on the gap sequence (the only place any
  number-theoretic input enters, and it is stated as a hypothesis, not assumed).

  Why it beats what was refuted. backward-extension-automaton died because
  valid-extension sets are GLOBAL (factorial-weighted); this proposal is the
  FORWARD direction: a local pattern in the STARTING sequence forces a local
  event, with no global extension criterion invoked. mod4/p-adic died because a
  congruence cannot separate {0,2} from higher even values; this proposal works
  at the exact-integer level on a bounded window. rule90/WH died on absorption
  and spectral stall; this proposal never tracks the XOR interior — it asks
  which starting patterns fire the event, which the record's own data shows is
  a single-row fact at the boundary.

  Speculative, flagged: that a finite dictionary with a useful frequency
  hypothesis exists is the open claim; it is falsifiable immediately by running
  the symbolic window computation for t_i <= 8 and seeing whether any short
  pattern fires. If no pattern of length <= 8 fires, the record gains the sharp
  fact "no (2,4)-event is determined by fewer than 8 starting gaps" — itself a
  real structural statement about how non-local regeneration actually is.
status: proposed
first-step: |
  Symbolic window search (sympy, exact integers; depth t and width t+2, so cost
  is O(t^2) per pattern — independent of the prime bound). For each halved-gap
  pattern P of length L <= 8 over a small alphabet {0,1,2,3} (halved gaps are
  <= 3 for small primes), build the starting row A_0 = (2, 3, 3+2P_0,
  3+2P_0+2P_1, ...), iterate the difference operator exactly for t <= 8 rows,
  and record whether a (2,4)-event (A_k(b_k)=2 and A_k(b_k+1)=4) occurs at any
  row k <= 8, together with its row index. Report: (a) the set of firing
  patterns and the minimum row at which each fires, (b) the shortest firing
  pattern and its length, (c) the fraction of patterns of each length that fire.
  This produces the dictionary; then hand research the frequency question:
  which explicit lower-density hypotheses on the halved prime gaps (e.g. "a
  halved gap >= 2 occurs with positive density", "adjacent halved gaps are not
  both 0 beyond some density") are known or provable from the PNT in APs.
```
