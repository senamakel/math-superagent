#!/usr/bin/env python3
"""Indexed diagonal access: yield delta(q_n) for n=1,2,... where delta(q_n)
has length n (indices 0..n-1), terminal delta_{n-1} = A_{n-1}[0].

The generic incremental generator yields length-m+1 diagonals; delta(q_n) is
the yield whose length is n (the (n-1)-th after the length-1 seed).  This
helper hands back (n, delta(q_n)) pairs so there is no off-by-one.
"""
from lib.gilbreath import primes_up_to
from lib.rightdiag import cycle_and_nu2


def diagonals_by_n(seq):
    """Yield (n, delta(q_n)) for n >= 1."""
    D = [seq[0]]
    yield 1, D
    for n in range(2, len(seq) + 1):
        newD = [0] * n
        newD[0] = seq[n - 1]
        for k in range(1, n):
            newD[k] = abs(newD[k - 1] - D[k - 1])
        D = newD
        yield n, D


def nu2_of(diag):
    """nu2 in the maximal {0,2} suffix of delta(q) before the terminal entry.
    Window indices 2..len-2 consistent with the operator's d[2:-1] convention
    (the 0-2 cycle tail)."""
    tail = diag[2:-1]
    i = len(tail)
    while i > 0 and tail[i - 1] in (0, 2):
        i -= 1
    return tail[i:].count(2)


def lemma54_transition(dprev, dcur, gstar):
    """Quantities at a q_{n-1}->q_n transition (Lemma 5.4).
    dprev=delta(q_{n-1}) len n-1; dcur=delta(q_n) len n.
    Returns dict.  All even-integer arithmetic."""
    tau, nu2 = cycle_and_nu2(dprev)
    v = dcur[tau]
    success = (dcur[-1] == 1)
    budget = 2 * nu2 + 2
    return {
        'tau': tau, 'nu2': nu2, 'v': v, 'success': success,
        'budget': budget,
        'hyp': gstar <= budget,
        'iff': (v <= budget) == success,
        'discarded_delta0': 0 in dcur[tau + 1:-1],
        'gstar': gstar,
    }
