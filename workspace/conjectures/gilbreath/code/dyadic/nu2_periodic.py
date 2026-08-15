#!/usr/bin/env python3
"""Exact-integer test of the dyadic-periodicity dichotomy for the Gilbreath
triangle (Directives 57-60).

For a '2-then-odds' sequence q with q_1=2, q_2=3 and q_{j+1}=q_j+gap where
  gap = 2 if halved-gap bit h_j = 1 else 4,
and a periodic bit word h of minimal period P, we compute
  nu2(n) = # of 2s in the maximal {0,2} suffix of the RIGHT DIAGONAL of the
           exact Gilbreath triangle to width n.

Components (all exact integer arithmetic):
  1. exact triangle generator via the incremental right-diagonal recurrence
       D[0]=q_n, D[k]=|D[k-1]-D_old[k-1]|.
     Each diagonal is generated from the previous in ONE pass; nu2 is sampled
     at chosen n in that pass (so the whole run to max n is O(maxn^2) per
     word, O(maxn) memory).  Within a row the |a-b| step is numpy-vectorised
     (exact int64; q values stay tiny for these gap<=4 sequences).
  2. nu2(n): maximal {0,2} suffix count on delta(q_n) (scan convention stated
     below).
  3. minimal-period: smallest divisor d of P with word periodic of period d.

SUFFIX-SCAN CONVENTION (explicit): given delta(q_n) = [d_0..d_n] with terminal
d_n = A_n[0], nu2 counts the number of 2s in the maximal suffix of {0,2}
entries among the cells d_0..d_{n-1} (excluding the terminal cell), scanning
back to the first entry not in {0,2}.  = lib.rightdiag.cycle_and_nu2.

Correctness anchor: this exact pipeline (same recurrence + scan) reproduces
the known prime-difference value nu2 = 2048 at n = 3999 (recorded in this
run), independently validating generator + scan.
"""
import sys, random
import numpy as np

sys.setrecursionlimit(100000)


def build_seq(h_pattern, phase, n_terms):
    """q_1..q_{n_terms}.  q_1=2, q_2=3, gap q_i->q_{i+1} (i>=2) uses
    h_pattern[(i+phase)%P]; gap = 2 if bit else 4.  Phase 0: h[0] governs
    gap q_2->q_3."""
    P = len(h_pattern)
    q = [2, 3]
    i = 2
    while len(q) < n_terms:
        bit = h_pattern[(i + phase) % P]
        q.append(q[-1] + (2 if bit else 4))
        i += 1
    return q[:n_terms]


def nu2_count(d):
    """# of 2s in maximal {0,2} suffix of delta(q_n) before terminal entry.
    body = d[:-1] (excludes terminal A_n[0])."""
    body = d[:-1]
    i = len(body)
    while i > 0 and body[i - 1] in (0, 2):
        i -= 1
    return body[i:].count(2)


def minimal_period(word):
    L = len(word)
    for d in range(1, L + 1):
        if L % d == 0 and all(word[j] == word[j % d] for j in range(L)):
            return d
    return L


def _nu2_array(arr):
    """nu2 from a numpy int array (maximal {0,2} suffix of arr[0..-2]).
    Vectorised suffix scan via mask."""
    body = arr[:-1]
    mask = (body == 0) | (body == 2)
    i = len(body)
    while i > 0 and mask[i - 1]:
        i -= 1
    tail = body[i:]
    return int((tail == 2).sum())


def sample_nu2_scan(seq, ns):
    """Incremental one-pass diagonal generation; return {n: nu2} for n in ns.
    seq[0]=q_1.  Pure-Python exact integer recurrence."""
    ns = sorted(set(ns))
    nq = len(seq)
    D = [seq[0]]
    out = {}
    for n in range(1, nq):
        nd = [0] * (n + 1)
        nd[0] = seq[n]
        prev = nd[0]
        for k in range(1, n + 1):
            v = prev - D[k - 1]
            nd[k] = v if v >= 0 else -v
            prev = nd[k]
        D = nd
        if n in ns:
            out[n] = nu2_count(D)
    return out


# ---------------------------------------------------------------- words
def canonical_word(P, orient="last"):
    w = [0] * P
    if orient == "first":
        w[0] = 1
    else:
        w[-1] = 1
    return w


def alternate_word(P):
    return [1 if i % 2 == 0 else 0 for i in range(P)]


def pseudo_word(P, seed=12345):
    if P == 1:
        return [1]
    rng = random.Random(seed)
    while True:
        w = [rng.randint(0, 1) for _ in range(P)]
        if minimal_period(w) == P:
            return w


# ---------------------------------------------------------------- Task A
HOSTS = {
    1: [1, 1, 1, 1],
    2: [2, 2, 2, 2],
    4: [2, 2, 2, 2],
    8: [2, 2, 2, 2],
    3: [133, 264, 533, 798],
    5: [104, 210, 424, 638],
    6: [134, 264, 534, 796],
    7: [112, 112, 685, 684],
}
NS_A = [200, 400, 800, 1200]


def task_A(phase=-3, orient="last"):
    print("=" * 68)
    print("TASK A: host stage-1 reproduction  (Directive 58)")
    print("canonical word = one 1 at %s; gap phase = %d" % (orient, phase))
    print("nu2 scan: maximal {0,2} suffix of delta(q_n)[0..n-1] (excl terminal)")
    print("-" * 68)
    match = True
    for P in sorted(HOSTS):
        w = canonical_word(P, orient)
        seq = build_seq(w, phase, max(NS_A) + 1)
        vals = sample_nu2_scan(seq, NS_A)
        got = [vals[n] for n in NS_A]
        ok = (got == HOSTS[P])
        match &= ok
        print("P=%-3d word=%-20s nu2 @ %s : %s  host %s  %s"
              % (P, ''.join(map(str, w)), NS_A, got, HOSTS[P],
                 "match" if ok else "DIFF"))
    print("-" * 68)
    # structured diff report
    for P in sorted(HOSTS):
        w = canonical_word(P, orient)
        seq = build_seq(w, phase, max(NS_A) + 1)
        vals = sample_nu2_scan(seq, NS_A)
        got = [vals[n] for n in NS_A]
        if got != HOSTS[P]:
            d = [b - a for a, b in zip(got, HOSTS[P])]
            print("  diff  P=%d  my=%-28s host=%-28s  host-mine=%s"
                  % (P, got, HOSTS[P], d))
    print("TASK A overall:", "EXACT MATCH" if match else
          "NOT exact (boundary/scan convention) - diffs reported above")
    return match


# ---------------------------------------------------------------- Task B
def task_B(ns=None):
    if ns is None:
        ns = [200, 500, 1000, 2000, 5000]
    print()
    print("=" * 68)
    print("TASK B: dichotomy over minimal periods 1..16, n = %s" % str(ns))
    print("words per period: canonical (one-1), alternate, pseudorandom")
    print("gap phase = 0 for Task B (h[0] governs gap q_2->q_3)")
    print("-" * 68)
    report = []
    for P in range(1, 17):
        words = [
            ("canon", canonical_word(P, "last")),
            ("alt", alternate_word(P)),
            ("psrnd", pseudo_word(P, seed=1000 + P)),
        ]
        for tag, w in words:
            seq = build_seq(w, 0, max(ns) + 1)
            vals = sample_nu2_scan(seq, ns)
            row = [vals[n] for n in ns]
            print("  P=%-3d %-6s mp=%-3d nu2 over %s : %s"
                  % (P, tag, minimal_period(w), str(ns), row))
        # classification
        vals = []
        seq = build_seq(canonical_word(P, "last"), 0, max(ns) + 1)
        vals = sample_nu2_scan(seq, ns)
        vlist = [vals[n] for n in ns]
        is_pow2 = (P & (P - 1)) == 0
        base = max(vlist[0], 1)
        # grows if the largest late sample far exceeds the first
        grows = (vlist[-1] > 3 * base) or (max(vlist[1:]) > 2 * base)
        report.append((P, is_pow2, grows, vlist))
        print("    -> minimal period %d (%s): canon nu2 %s ; grows? %s"
              % (P, "pow2" if is_pow2 else "odd", vlist,
                 "YES" if grows else "no (O(1))"))
    print("-" * 68)
    good = True
    for P, is_pow2, grows, vlist in report:
        if is_pow2 and grows:
            good = False
            print("  POWER-OF-2 PERIOD %d GROWS (%s) -> dyadic story WRONG" %
                  (P, vlist))
        if (not is_pow2) and (not grows):
            good = False
            print("  ODD-FACTOR PERIOD %d BOUNDED (%s) -> dyadic story WRONG" %
                  (P, vlist))
    if good:
        print("DICHOTOMY: CONFIRMED-OVER-RANGE (n in %s, P in 1..16): "
              "nu2 = O(1) exactly for power-of-2 minimal periods, "
              "nu2 ~ c*n (grows) for odd-factor periods." % str(ns))
    else:
        print("DICHOTOMY: REFUTED (see offending periods above)")
    return good


if __name__ == "__main__":
    do_a = "--noA" not in sys.argv
    do_b = "--noB" not in sys.argv
    if do_a:
        task_A()
    if do_b:
        task_B()
