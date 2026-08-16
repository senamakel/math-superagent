#!/usr/bin/env python3
"""Probe: does the C2 telescoping identity break under a 3-valued boundary?

Identity under test: for two-valued r, h[j] = [r_{j+1} != r_j], and for any
consecutive run [u,v]:
    XOR_{o in [u,v]} h[pos+o] == [ r_{pos+u} != r_{pos+v+1} ].
This holds because XOR over an interval is the parity of flips, and for a
2-valued boundary odd flips <-> endpoints differ.

Negative control: use a THREE-valued boundary (residues mod 3). Now the parity
of flips no longer determines endpoint difference (0->1->2 is two flips but
endpoints differ), so the identity MUST break. Count and report mismatches.
"""
import sys
from lib.submasks import downset_runs


def boundary_h(r):
    return [1 if r[j + 1] != r[j] else 0 for j in range(len(r) - 1)]


def count_mismatches(fn_res, DMAX, positions, L):
    """fn_res(N) -> list of boundary values. Returns (pairs, mismatches)."""
    r = fn_res(L + 10)
    h = boundary_h(r)
    pairs = 0
    mismatches = 0
    first = None
    for d in range(DMAX + 1):
        for (u, v) in downset_runs(d):
            for pos in positions:
                acc = 0
                for o in range(u, v + 1):
                    acc ^= h[pos + o]
                tel = 1 if r[pos + u] != r[pos + v + 1] else 0
                pairs += 1
                if acc != tel:
                    mismatches += 1
                    if first is None:
                        first = (d, pos, u, v, acc, tel)
    return pairs, mismatches, first


def main():
    DMAX = 64
    L = DMAX + 600
    positions = range(0, 21)

    def primes_mod2(N):
        ps, p = [], 3
        while len(ps) < N:
            ok = True
            for q in ps:
                if q * q > p:
                    break
                if p % q == 0:
                    ok = False
                    break
            if ok:
                ps.append(p)
            p += 2
        return [q % 2 for q in ps]

    # 2-valued control: MUST hold (mismatches == 0)
    p2, m2, f2 = count_mismatches(primes_mod2, DMAX, positions, L)
    print(f"[control 2-valued] pairs={p2} mismatches={m2}  (expect 0)")

    # 3-valued negative control: MUST fail (mismatches > 0)
    def primes_mod3(N):
        ps, p = [], 3
        while len(ps) < N:
            ok = True
            for q in ps:
                if q * q > p:
                    break
                if p % q == 0:
                    ok = False
                    break
            if ok:
                ps.append(p)
            p += 2
        return [q % 3 for q in ps]

    p3, m3, f3 = count_mismatches(primes_mod3, DMAX, positions, L)
    print(f"[negative 3-valued] pairs={p3} mismatches={m3}  (expect >0)"
          + (f"  first mismatch d={f3[0]} pos={f3[1]} run={f3[2]}-{f3[3]} "
             f"xor={f3[4]} tel={f3[5]}" if f3 else ""))

    ok = (m2 == 0) and (m3 > 0)
    print("SUCCESS" if ok else "FAILED (probe did not behave as expected)")


if __name__ == "__main__":
    main()
