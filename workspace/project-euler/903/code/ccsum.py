#!/usr/bin/env python3
"""ccsum.py — f_n(k) via summing over conjugacy classes (cycle types).

Definitions (0-based one-line permutations of {0..n-1}, pi^i the i-th
iterate, pi^0 = identity):

  f_n(k) = #{(pi, i) : 0 <= i < n!, (pi^i)(k) < (pi^i)(0)},  k = 1..n-1.

Prior proven structure (gaps.py / explore.py / verify_red.py): f_n is exactly
arithmetic in k, f_n(k) = A_n + (k-1) B_n with A_n=f(1), B_n=f(2)-f(1),
and the identity row j=0 suffices.  The chain Q(n)=(n!)^2 + A_n(n!-1) +
(B_n/2)T(n) reduces PE 903 to knowing A_n and B_n.

Period formula: pi^i is periodic with period d = ord(pi) = lcm of the cycle
lengths (every cycle length <= n so d | n!), hence among i = 0..n!-1 each
distinct power appears exactly n!/d times, and

  f_n(k) = sum_{pi in S_n} (n!/d) * #{tau in <pi> : tau(k) < tau(0)}.

Conjugacy-class reduction (NEW, the point of this file): bith ord(pi) and
the cyclic-subgroup count #{tau in <pi>: tau(k)<tau(0)} are invariant under
conjugation (conjugating pi moves the whole orbit and preserves the number
of t with the comparison true).  So summing over all n! permutations reduces
to summing over partitions lambda of n:

  f_n(k) = sum_{lambda |- n} class_size(lambda) * (n!/lcm(lambda))
                            * S(lambda, k),
  S(lambda,k) = #{tau in <pi>: tau(k) < tau(0)} for one representative pi
                of cycle type lambda,  <pi> has lcm(lambda) elements.

Representative powers are read analytically off cycles: for a cycle
(c_0,...,c_{L-1}) with pi(c_j)=c_{j+1 mod L}, pi^t(c_j) = c_{(j+t) mod L}.
So S(lambda,k) is computed by iterating t = 0..lcm(lambda)-1 and comparing
the images of k and 0, each image found by an index modulo the cycle length
(no repeated composition, no n!-permutation enumeration).

Number of partitions p(n): n=11 -> 56, n=12 -> 77, n=14 -> 135, n=16 -> 231;
max lcm g(n) (Landau) grows ~ e^{sqrt(n ln n)}: n=12 -> 60, n=14 -> 84,
n=16 -> 140, n=20 -> 420, n=30 -> 2310.  Compared with the n!-permutation
iteration of extend_f.py (which walled at n=12 ~54 min), this runs in
O(p(n) * lcm_max * n) big-int steps, sub-second per n even well past 20.

Exact Python ints throughout, no mod, so A_n and B_n are produced exactly.
Sanity-checked against the known rows in out/extend_f.json (n=2..11) and
then extended to n=12..17 (and beyond while each n stays within the per-n
wall gate), the rows and the resulting A_n, B_n written to out/ccsum.json.
"""
import json
import math
import os
import time

TIME_GATE = float(os.environ.get("CCSUM_GATE", "120.0"))  # seconds per n


def partitions(n):
    """Yield all partitions of n as non-increasing lists of parts."""
    parts = [0] * n
    out = []

    def rec(remaining, max_part, idx):
        if remaining == 0:
            out.append(list(parts[:idx]))
            return
        for p in range(min(max_part, remaining), 0, -1):
            parts[idx] = p
            rec(remaining - p, p, idx + 1)

    rec(n, n, 0)
    return out


def representative(parts):
    """Build one 0-based permutation pi of cycle type `parts`.

    0 is placed in the first cycle.  For a cycle (c_0,...,c_{L-1}) we set
    pi(c_j) = c_{(j+1) mod L}.  Cycles are filled with consecutive integers.
    """
    n = sum(parts)
    perm = [0] * n
    nxt = 0
    for ci, L in enumerate(parts):
        cyc = list(range(nxt, nxt + L))
        # ensure 0 is in the first cycle
        if ci == 0:
            # move 0 into this cycle if it has room (it does: L>=1)
            cyc = [0] + [x for x in cyc if x != 0]
        for j in range(L):
            perm[cyc[j]] = cyc[(j + 1) % L]
        nxt += L
    # if cycle 0 did not get 0 (L of first part is 1 and 0 already), fine
    return perm


def compute_f(n):
    """Return [f(1), ..., f(n-1)] summed over cycle types (exact ints)."""
    nf = math.factorial(n)
    f = [0] * (n - 1)
    for parts in partitions(n):
        lcm = 1
        for p in parts:
            lcm = lcm * p // math.gcd(lcm, p)
        d = lcm
        # class size = n! / prod_j (j^{m_j} * m_j!)
        m = {}
        for p in parts:
            m[p] = m.get(p, 0) + 1
        denom = 1
        for j, mj in m.items():
            denom *= (j ** mj) * math.factorial(mj)
        cs = nf // denom
        w = nf // d
        weight = cs * w  # = class_size * (n!/ord(pi))

        # representative and cycle membership
        perm = representative(parts)
        # decompose into cycles with 0-based positions
        cycles = []          # list of cycles (lists of elements)
        idx_of = {}          # element -> own cycle index
        pos_of = {}          # element -> position within its cycle
        seen = [False] * n
        for s in range(n):
            if not seen[s]:
                cyc = []
                c = s
                while not seen[c]:
                    seen[c] = True
                    idx_of[c] = len(cycles)
                    pos_of[c] = len(cyc)
                    cyc.append(c)
                    c = perm[c]
                cycles.append(cyc)
        L = [len(c) for c in cycles]
        # S(lambda,k) over t = 0..d-1
        S = [0] * (n - 1)
        for t in range(d):
            c0 = cycles[idx_of[0]]
            L0 = len(c0)
            v0 = c0[(pos_of[0] + t) % L0]
            for k in range(1, n):
                ck = cycles[idx_of[k]]
                Lk = len(ck)
                vk = ck[(pos_of[k] + t) % Lk]
                if vk < v0:
                    S[k - 1] += 1
        for k in range(1, n):
            f[k - 1] += weight * S[k - 1]
    return f


def main():
    start_n = int(os.environ.get("CCSUM_START", "2"))
    max_n = int(os.environ.get("CCSUM_MAX", "16"))
    # load known rows for sanity comparison
    known = {}
    if os.path.exists("out/extend_f.json"):
        known = json.load(open("out/extend_f.json"))
    results = {}
    if os.path.exists("out/ccsum.json"):
        results = json.load(open("out/ccsum.json"))
    ab = {}
    if os.path.exists("out/ccsum_ab.json"):
        ab = json.load(open("out/ccsum_ab.json"))

    t_start = time.time()
    for n in range(start_n, max_n + 1):
        t0 = time.time()
        row = compute_f(n)
        dt = time.time() - t0
        results[str(n)] = row
        A = row[0]
        B = (row[1] - row[0]) if len(row) >= 2 else 0
        ab[str(n)] = {"A": A, "B": B}
        with open("out/ccsum.json", "w") as fh:
            json.dump(results, fh)
        with open("out/ccsum_ab.json", "w") as fh:
            json.dump(ab, fh)
        # arithmetic check
        diffs = [row[i + 1] - row[i] for i in range(len(row) - 1)]
        second = [diffs[i + 1] - diffs[i] for i in range(len(diffs) - 1)]
        arith = (not second) or all(s == 0 for s in second)
        # compare to known
        if str(n) in known:
            exp = known[str(n)]
            match = (row == exp)
        else:
            match = "no-previous"
        print(f"n={n}: time {dt:.2f}s  match_prev={match}  "
              f"arith={arith}  A={A}  B={B}", flush=True)
        if str(n) in known and not match:
            print(f"    got      {row}", flush=True)
            print(f"    expected {known[str(n)]}", flush=True)
        if dt > TIME_GATE:
            print(f"    n={n} exceeded gate {TIME_GATE:.0f}s -> stopping",
                  flush=True)
            break

    print(f"\nTotal wall: {time.time()-t_start:.2f}s", flush=True)
    # final table
    print("\nA_n / B_n table:")
    for sn in sorted(ab, key=int):
        print(f"  n={sn}: A={ab[sn]['A']}, B={ab[sn]['B']}", flush=True)


if __name__ == "__main__":
    main()
