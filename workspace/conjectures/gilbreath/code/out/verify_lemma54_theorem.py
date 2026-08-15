"""Independent brute-force verification of the repaired Lemma 5.4 (even domain).

Theorem (repaired): let eps in {0,2}^L, nu_2 = #{k: eps_k=2}, and the orbit
delta_0 = v (v even, v >= 0), delta_k = |delta_{k-1} - eps_k|.  If
v <= 2*nu_2 + 2, then delta_L in {0,2} and the orbit stays in {0,2} forever.

The published-proof algebra "delta_L = v - 2*nu_2" is false on bounce
trajectories (delta=0, eps=2 -> 2, a +2 not -2).  The repair is the case
split: if some delta_t <= 2 for t <= L then delta_t in {0,2} and absorption
carries it; else every delta_k >= 4, every 2 subtracts 2, and
delta_L = v - 2*nu_2 <= 2 contradicts delta_L >= 4.

This script checks the CLAIM directly on the orbit (no use of the suspect
algebra), over a wider even-v range, as an independent oracle.
"""
import itertools

def lands(eps, v):
    """Return True iff the orbit delta_0=v, delta_k=|delta_{k-1}-eps_k|
    is in {0,2} at step L (end of eps) and stays in {0,2} forever."""
    d = v
    for e in eps:
        d = abs(d - e)
    # {0,2} absorbing: if d in {0,2} at step L, it stays forever.
    return d in (0, 2)

def main():
    L_max = 9
    viol = 0
    checked = 0
    for L in range(1, L_max + 1):
        for eps in itertools.product((0, 2), repeat=L):
            nu2 = eps.count(2)
            # even v in [0, 2*nu2+4] -- hypothesis region plus a margin above
            for v in range(0, 2 * nu2 + 5, 2):
                checked += 1
                hyp = (v <= 2 * nu2 + 2)
                if hyp and not lands(eps, v):
                    viol += 1
                    print("VIOLATION", eps, "v=", v, "nu2=", nu2)
    print(f"checked={checked} hypothesis-violations={viol}")
    print("PASS" if viol == 0 else "FAIL")

main()
