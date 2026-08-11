#!/usr/bin/env python3
"""extend_f.py — f_n(k) for n=2..11 via the period formula, row j=0 only.

Definitions (0-based one-line permutations of {0..n-1}, pi^i the i-th
iterate: (pi^{i+1})(x) = pi(pi^i(x)), pi^0 = identity):

  f_n(k) = #{(pi, i) : 0 <= i < n!, (pi^i)(k) < (pi^i)(0)},  k = 1..n-1.

Prior work (gaps.py / explore.py) proved the underlying count T(j, j+k) is
independent of j, so the row j=0 suffices.

Period formula: pi^i is periodic with period d = ord(pi) = lcm of cycle
lengths, every cycle length <= n so d | n!, hence among i = 0..n!-1 each
distinct power of pi appears exactly n!/d times.  Therefore

  f_n(k) = sum_{pi in S_n} (n!/d) * #{tau in <pi> : tau(k) < tau(0)}.

Permutations are enumerated with itertools.permutations(range(n)); the
distinct powers <pi> are enumerated by repeated composition starting from the
identity (cur = [perm[x] for x in cur]).  Exact Python ints throughout, no
mod.

For n <= 6 an independent literal oracle (iterating every i = 0..n!-1 for
every pi) is computed and compared.  Each row is printed with flush=True as
it finishes, with first/second differences; the run stops after n = 11 or
whenever a single n exceeds ~280 s wall time.  Results are saved
incrementally to extend_f.json as {n: [f(1), ..., f(n-1)]}.
"""
import itertools
import json
import math
import os
import time

TIME_GATE = 280.0   # stop entirely once a single n exceeds this many seconds


def cycle_order(perm):
    """Order of perm as a group element: lcm of its cycle lengths (0-based)."""
    n = len(perm)
    seen = [False] * n
    l = 1
    for s in range(n):
        if not seen[s]:
            c = s
            cnt = 0
            while not seen[c]:
                seen[c] = True
                c = perm[c]
                cnt += 1
            l = l * cnt // math.gcd(l, cnt)
    return l


def compute_f(n):
    """Return [f(1), ..., f(n-1)] for this n by the period formula.

    Enumerates S_n with itertools.permutations(range(n)); for each pi walks
    the d = ord(pi) distinct powers by repeated composition, accumulating
    (n!/d) per power for which the current power maps k below 0.
    """
    nf = math.factorial(n)
    idt = list(range(n))
    f = [0] * (n - 1)
    for perm in itertools.permutations(range(n)):
        d = cycle_order(perm)
        w = nf // d
        cur = idt
        for _ in range(d):
            c0 = cur[0]
            for k in range(1, n):
                if cur[k] < c0:
                    f[k - 1] += w
            cur = [perm[x] for x in cur]
    return f


def literal_f(n):
    """Independent oracle: literal double count over i = 0..n!-1, each pi."""
    nf = math.factorial(n)
    idt = list(range(n))
    f = [0] * (n - 1)
    for perm in itertools.permutations(range(n)):
        cur = idt
        for _ in range(nf):
            c0 = cur[0]
            for k in range(1, n):
                if cur[k] < c0:
                    f[k - 1] += 1
            cur = [perm[x] for x in cur]
    return f


def main():
    max_n = int(os.environ.get("EXTEND_F_MAX", "11"))
    results = {}
    stopped = None
    t_start = time.time()
    oracle_lim = min(6, max_n)
    for n in range(2, max_n + 1):
        print(f"--- n = {n}: starting ({math.factorial(n)} permutations) ---",
              flush=True)
        t0 = time.time()
        f = compute_f(n)
        dt = time.time() - t0
        results[n] = f
        with open("extend_f.json", "w") as fh:
            json.dump({str(k): v for k, v in results.items()}, fh)
        print(f"n = {n}:  f(k), k=1..n-1 = {f}", flush=True)
        print(f"    time: {dt:.2f} s", flush=True)
        diffs = [f[i + 1] - f[i] for i in range(len(f) - 1)]
        second = [diffs[i + 1] - diffs[i] for i in range(len(diffs) - 1)]
        print(f"    1st diffs: {diffs}", flush=True)
        if second:
            print(f"    2nd diffs: {second}", flush=True)
        if len(second) > 0 and all(s == 0 for s in second):
            print(f"    EXACTLY ARITHMETIC: "
                  f"A_n = f(1) = {f[0]},  B_n = f(2)-f(1) = {diffs[0]}",
                  flush=True)
        elif len(f) <= 2:
            print("    row too short to test 2nd differences", flush=True)
        else:
            print("    NOT exactly arithmetic in k", flush=True)
        if n <= oracle_lim:
            fl = literal_f(n)
            ok = (fl == f)
            msg = f"    literal oracle (i=0..n!-1): {'PASS' if ok else 'FAIL'}"
            if not ok:
                msg += f"   oracle = {fl}"
            print(msg, flush=True)
        if dt > TIME_GATE:
            stopped = n
            print(f"    n = {n} exceeded {TIME_GATE:.0f} s -> stopping",