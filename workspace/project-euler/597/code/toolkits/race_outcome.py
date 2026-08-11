"""The brute-force race oracle for PE 597, as a single callable.

This is the reference implementation every exact method is checked against.
It replays the chronological bump/finish dynamics over iid Exp(1) speeds and
returns the parity (0 even / 1 odd) of the new order, following the statement's
bump-chain rule.

Signature:
    outcome_parity(n, L, speeds) -> int (0 = even, 1 = odd)

This wraps `brute.outcome_parity`, which after the edge-loss fix records every
bump edge and computes `above` by full graph reachability (a boat m is placed
below i iff there is a bump chain i -> ... -> m). Correctness established by:
  - reproducing all five rows of the n=3,L=160 statement table (parities
    none=0, B->C=1, A->B=1, A/B->C=0, A->B->C=1);
  - matching p(3,160)~0.414815 (56/135) and p(4,400)~0.5107843137 via Exp(1)
    Monte Carlo;
  - 2M random-trials differential vs an independent full-reachability
    reconstruction with identical total orders and parities.
"""
from brute import outcome_parity as _outcome_parity


def outcome_parity(n, L, speeds):
    """Return 0 (even) or 1 (odd) for the race with n boats over course L.

    speeds: length-n sequence of Exp(1) draws (float or exact). L: course
    length in metres (finish line upstream of the lowest boat's start).
    """
    return _outcome_parity(n, L, speeds)
