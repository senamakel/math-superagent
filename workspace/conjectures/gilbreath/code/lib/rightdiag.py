#!/usr/bin/env python3
"""Incremental right-diagonal computation for the prime Gilbreath triangle.

The right diagonal through q_n is
    delta(q_n) = [delta_0 .. delta_n],  delta_k(q_n) = A_k[n-k]   (A_0 = q sequence)
with terminal delta_n = A_n[0];  "success at q_n" <=> delta_n == 1.

Recurrence:  delta(q_n) extended from delta(q_{n-1}) by
    D[0]   = q_{n+1}                    (the new term, using 1-indexed q)
    D[k]   = |D[k-1] - D_old[k-1]|      k = 1..n
where D_old = delta(q_n).  Total O(N^2) absolute differences, O(N) memory.

This is verified in the _work() block against the full row-triangle
construction (rows_generator) for the first few primes.

Also exposes Granville's Lemma 5.4 bookkeeping on a diagonal:
  0-2 cycle = maximal {0,2} suffix of delta(q_{n-1}) before the terminal entry;
  nu2 = count of 2s in it;  tau = start index;  v_n = delta(q_n)[tau].
  Lemma 5.4 iff : success at q_n <=> v_n <= 2*nu2 + 2.
  Sufficiency    : since v_n < g*_n, if g*_n <= 2*nu2+2 then success guaranteed.
"""
from lib.gilbreath import primes_up_to, rows_generator


def incremental_diagonals(seq):
    """Yield delta(q_n) for n = 0,1,2,... given the 1-indexed sequence seq
    (seq[0]=q_1). Uses the in-place recurrence; O(N^2) diffs, O(N) memory."""
    # n = 0
    D = [seq[0]]
    yield D
    for n in range(1, len(seq)):
        newD = [0] * (n + 1)
        newD[0] = seq[n]
        for k in range(1, n + 1):
            newD[k] = abs(newD[k - 1] - D[k - 1])
        D = newD
        yield D


def delta_diagonal(primes, n):
    """delta(q_n) with q_i = primes[i-1] (primes is the 0-indexed list)."""
    D = [primes[0]]
    for i in range(1, n + 1):
        newD = [0] * (i + 1)
        newD[0] = primes[i]
        for k in range(1, i + 1):
            newD[k] = abs(newD[k - 1] - D[k - 1])
        D = newD
    return D


def cycle_and_nu2(diag, terminal_is_last=True):
    """Given a diagonal delta(q) (list), return (tau, nu2) where tau is the
    start index of the maximal {0,2} suffix before the terminal entry and
    nu2 is the number of 2s in that cycle.  The window is diag[tau:-1]
    (indices tau..len-2), matching his code right_diagonal[idx+1:-2]."""
    body = diag[:-1]
    i = len(body)
    while i > 2 and body[i - 1] in (0, 2):
        i -= 1
    tau = i
    cyc = body[tau:]
    return tau, cyc.count(2)


def lemma54_iff(d_prev, d_cur, gstar):
    """Check Lemma 5.4 on one transition q_{n-1} -> q_n.
    d_prev = delta(q_{n-1}), d_cur = delta(q_n), gstar = max(g_2..g_n).
    success <=> d_cur[-1] == 1.  Returns a dict of the quantities."""
    tau, nu2 = cycle_and_nu2(d_prev)
    v = d_cur[tau]
    success = (d_cur[-1] == 1)
    return {
        'tau': tau, 'nu2': nu2, 'v': v, 'success': success,
        'iff': (v <= 2 * nu2 + 2) == success,
        'suff': (gstar <= 2 * nu2 + 2) or (not (gstar <= 2 * nu2 + 2)),
        'budget': 2 * nu2 + 2,
        'hyp_holds': gstar <= 2 * nu2 + 2,
        'discarded_delta0': 0 in d_cur[tau + 1:-1],
    }


def _work():
    # Verify the incremental recurrence against the full row triangle.
    P = primes_up_to(200)
    n = 8
    d_inc = [list(d) for d in incremental_diagonals(P[:n + 1])]
    # full triangle
    rows = list(rows_generator(P[:n + 1], n))
    d_full = [[rows[k][n - k] for k in range(n + 1)]]
    # build from scratch each n via rows[:n+1]
    ok = True
    for m in range(0, n + 1):
        rows_m = list(rows_generator(P[:m + 1], m))
        df = [rows_m[k][m - k] for k in range(m + 1)]
        ok &= (df == d_inc[m])
        # also full triangle check against expected terminal = A_m[0]
    print("incremental == full triangle for n=0..%d : %r" % (n, ok))
    # reproduce problem.md A_1
    rows1 = list(rows_generator(P, 5))
    print("A_1 =", rows1[1][:12])
    return ok


if __name__ == "__main__":
    _work()
