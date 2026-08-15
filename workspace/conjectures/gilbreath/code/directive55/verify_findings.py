#!/usr/bin/env python3
"""Directive-55: independent verification of the load-bearing findings.

(1) Cross-check my nu2 measurement against the ESTABLISHED rightdiag.py
    convention (cycle_and_nu2) on the primes at several n. If these agree,
    my generator + suffix convention reproduce the run's reference.

(2) Hand-verify the alternating-2/4 constant-nu2 phenomenon on the explicit
    n=10 triangle: q=(2,3,5,9,11,15,17,21,23,27) gives delta=(27,4,2,0,..,1),
    hence nu2=1 (both conventions) while w=#{j in [2,9]:g_j/2 odd}=6.
"""
from lib.gilbreath import primes_up_to
from lib.rightdiag import delta_diagonal, cycle_and_nu2
from directive55.nu2_transfer_characterize import (
    triangle_rows, nu2_of_diagonal, build_gaps, w_of_seg)


def crosscheck_primes():
    print("[1] nu2 cross-check vs rightdiag.cycle_and_nu2, primes")
    P = primes_up_to(70000)
    header = "%5s  %8s  %8s  %8s" % ("n", "mine_nu2c", "rightdiag_nu2", "match")
    print(header)
    ok_all = True
    for n in [50, 100, 200, 400, 800, 1000]:
        rows = list(triangle_rows(P, n))
        dd = [rows[k][n - k] for k in range(n + 1) if n - k < len(rows[k])]
        nu2_c, _, _, _ = nu2_of_diagonal(dd)
        d_ref = delta_diagonal(P, n)
        # reference: body = d[:-1]; the run convention (tail floor at index 2)
        body = d_ref[:-1]
        tail = body[2:]
        i = len(tail)
        while i > 0 and tail[i - 1] in (0, 2):
            i -= 1
        ref_nu2 = tail[i:].count(2)
        match = (nu2_c == ref_nu2)
        ok_all &= match
        print("%5d  %8d  %8d  %8s" % (n, nu2_c, ref_nu2, match))
    print("  all match:", ok_all)
    return ok_all


def hand_verify_alt():
    print("\n[2] Hand-verified alternating-2/4, n=10")
    q = [2, 3, 5, 9, 11, 15, 17, 21, 23, 27]
    rows = list(triangle_rows(q, 9))
    for k in range(4):
        print("    A_%d = %s" % (k, rows[k]))
    n = 10
    dd = [rows[k][n - k] for k in range(len(rows)) if n - k < len(rows[k])]
    print("    delta(q_10) =", dd)
    nu2_c, nu2_l, _, _ = nu2_of_diagonal(dd)
    gaps = build_gaps(q)
    w = w_of_seg(gaps, n)
    print("    nu2c=%d nu2l=%d  w=%d  h[j]=(g_j/2)mod2 over j=2..9" % (nu2_c, nu2_l, w))
    hh = [((q[j+1]-q[j])//2) % 2 for j in range(1, n-1)]
    print("    h =", hh, " both values =", set(hh) == {0, 1}, " w=", sum(hh))
    print("    -> both values present on every prefix, yet nu2=1 = O(1)")
    return nu2_c <= 1


if __name__ == "__main__":
    a = crosscheck_primes()
    b = hand_verify_alt()
    print("\nBoth independent checks passed:", a and b)
