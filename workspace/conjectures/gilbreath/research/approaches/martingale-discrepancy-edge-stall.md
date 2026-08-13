```approach
idea: martingale-discrepancy-edge-stall
mechanism: |
  This is on the RECHARGE side (not consumption, which is settled): it attacks
  the open problem "why does the boundary keep re-entering (2,4) before the
  block hits length 0" by turning the edge process into a MARTINGALE and using
  discrepancy theory instead of an i.i.d. law of large numbers.

  Setup. Work in the halved triangle H_k(i) = A_k(i)/2 for i >= 1. The block's
  last entry has halved value x_k = H_k(b_k) in {0,1}, and the intruder has
  halved value w_k = H_k(b_k+1) >= 2 (since intruder >= 4). The exact drain
  law, in halved form, is

      w_{k+1} = w_k - x_k       (each x=1 step drains the intruder by one unit)

  and regeneration (the only block-growing event) is the exact local condition

      (x_k = 1 and w_k = 2)     <==>  (A_k(b_k)=2 and A_k(b_k+1)=4).

  This is the established (2,4)-criterion, restated in halved coordinates.

  The martingale. Inside the {0,2} block the halved entries evolve under XOR
  (Rule 90, proved in research/notes/block_lemma.md). During erosion the block
  loses one column per row, so the edge at row k+d is the XOR of a window of
  the halved block's bits that grows by one fresh bit per step:

      x_{k+d} = x_{k+d-1} XOR (fresh bit entering the window).

  Hence x_k is a martingale in the filtration that reveals one halved-gap
  parity bit per erosion step: E[x_{k+d} | past] = x_{k+d-1} exactly, because
  XOR-ing an independent fair bit preserves expectation. The increments are
  bounded (they are in {-1,+1} after centering), so Doob's optional-stopping
  and Azuma-Hoeffding apply WITHOUT the i.i.d. assumption of the renewal
  proposal. The event-time problem is a first-passage problem: regeneration
  fires when the partial sum

      S_{k} = sum_{j<k} x_j   reaches   w_0 - 2.

  Mechanism, and why it is not the refuted/renewal items. The renewal proposal
  postulated the edge bits are i.i.d. fair and used a renewal-reward LIMIT
  theorem — that is exactly the assumption Eppstein's class defeats and that
  the primes are not known to satisfy. This proposal replaces it with a
  finite-time, almost-sure bound derived from DISCREPANCY of the halved-gap
  parity sequence: the fresh bits are not arbitrary, they are
  (p_{n+1}-p_n)/2 mod 2, i.e. the parity of prime-gap halves. A bound of the
  form |S_k - k/2| <= D(k) with D(k) = o(k) (a discrepancy bound, the kind
  studied by Erdos-Turan / van der Corput for mod-1 and mod-m sequences) forces
  the walk to hit the level w_0 - 2 within a finite, explicit number of steps,
  because the intruder is a bounded counter (w_0 <= max prime gap / 2 in the
  relevant window). Concretely: if the partial sums of the parity bits have
  bounded discrepancy D, the first passage time to w_0-2 is bounded by a
  function of D and w_0 alone. That yields a LOWER BOUND on the (2,4)-event
  rate using only a discrepancy hypothesis on the prime-gap parities — no
  independence, no Cramer, no 2-separation concentration needed (it is strictly
  weaker: a 2-separated gap sequence can still have bounded parity discrepancy).

  What would falsify it. (i) A computation showing the halved edge x_k is NOT
  a martingale in the "reveal one bit" filtration on the real rows (i.e. the
  fresh bit is predictable from the past), or (ii) the prime-gap-parity
  sequence having discrepancy D(k) that grows linearly (so the first-passage
  bound is vacuous). Both are checkable at depth 1000. Note the asymmetry the
  run has already paid for: a partial result here would be "under bounded
  discrepancy of gap parities, the event rate suffices" — a REAL general-class
  theorem with the primes as a candidate instance, not another erosion count.
status: proposed
first-step: |
  Two independent checks, run against code/out/blocks_depth1000.json and a
  fresh sieve:
  (1) MARTINGALE CHECK. For the live regime k=1..161, compute the halved edge
      x_k and the halved intruder w_k; verify the drain law w_{k+1}=w_k-x_k has
      zero failures and, crucially, test whether x_{k+1} is predictable from
      the past by computing E[x_{k+1} | x_1..x_k] empirically (it must be
      1/2 ± o(1), i.e. no drift) and the autocorrelation of the increments
      (a non-martingale shows as a nonzero lag-1 correlation).
  (2) DISCREPANCY CHECK. For the halved-gap parity sequence
      b_n = ((p_{n+1}-p_n)/2) mod 2, compute the partial-sum discrepancy
      D(N) = max_{0<=a<=b<=N} |sum_{a<=n<=b} (2 b_n - 1)| for N up to the
      width of the depth-1000 sieve, and report its growth (log? sqrt? linear?).
      Then hand research the precise question: which known discrepancy bounds
      (Erdos-Turan, van der Corput, Halasz) apply to prime-gap parities, and
      does any of them already give D(N)=o(N)?
```
