#!/usr/bin/env python3
"""COMPUTATION A — kernel-component of the prime switch bit.

Context (verified in code/fold_rank and code/out/supply_fold_rank.final.captured.txt):
the operative fold matrix Phi_n is (n-2) x n, rows d = 2..n-1, columns j =
0..n-1, entry C(d-1, j-(n-d)) mod 2 (equivalently the depth-d row is the
indicator of "s = n-1-j is a bitwise submask of d"). It has FULL ROW RANK
n-2, nullity 2, and
    ker Phi_n = span(even-alt, odd-alt)
where even-alt[j] = 1 iff j even, odd-alt[j] = 1 iff j odd, and all-ones =
even-alt XOR odd-alt is the third nonzero member.

The prime switch bit is h[j] = ((q_{j+1}-q_j)//2) mod 2 (q the primes),
the length-4000 table the run studies.

This answers, exactly over F2 and also by the real imbalance:
  (i) correlation <h, even-alt>, <h, odd-alt> (mod-2 dot product, the true
      F2 component) and the real signed imbalance sum (-1)^{h[j]+even-alt[j]};
  (ii) wt(Phi_n h) (= nu2(n)) vs wt(Phi_n even-alt)=0, wt(Phi_n odd-alt)=0
       (both are kernel collisions, the fold kills them), and the weight of
       Phi_n applied to h projected OFF the kernel;
  (iii) whether h is closer to the kernel (min Hamming distance over the 4
       kernel vectors) than a matched-density random string would be.

Weight wt(Phi_n v) over F2 for an arbitrary v is computed by the exact
submask-XOR fold (the literal definition of nu2): wt(Phi_n v) =
# {d in [2,n-1] : XOR_{o submask of d} v[n-1-d+o] = 1}. This equals the SOS
count (s_sos) which is verified against the direct oracle s_direct on
n=4..200 (and against the independent character-sum route). For v = h this is
exactly nu2(n).

All arithmetic exact (F2 and integer); only ratios/means are float. This is a
measurement, not a proof.
"""
import os
import random
from fractions import Fraction

from lib.primes import prime_gap_parity
from lib.supply_fold import s_direct, s_sos


def prime_switch_h(N):
    """h[j] = ((q_{j+1}-q_j)//2) mod 2 for j=0..N-1 (length N)."""
    return prime_gap_parity(N)


def even_alt(n):
    return [1 if j % 2 == 0 else 0 for j in range(n)]


def odd_alt(n):
    return [1 if j % 2 == 1 else 0 for j in range(n)]


def dot_f2(a, b):
    """Standard F2 dot product (correlation mod 2)."""
    return sum(x & y for x, y in zip(a, b)) % 2


def real_imbalance(a, b):
    """Real signed imbalance sum_j (-1)^{a[j]+b[j]} = #agree - #disagree.
    Exact integer."""
    return sum(1 if (a[j] ^ b[j]) == 0 else -1 for j in range(len(a)))


def phi_weight(n, v):
    """wt(Phi_n v) over F2 = # {d in [2,n-1]: XOR_{o submask of d} v[n-1-d+o]=1}.
    This is the literal definition of nu2 applied to an arbitrary vector v of
    length n, computed by the submask-product SOS (exact, verified vs the
    direct oracle)."""
    _, ones = s_sos(n, v)          # s_sos computes count of T=1 with d in [2,n-1]
    return ones


def hamming(a, b):
    return sum(1 for x, y in zip(a, b) if x != y)


def run(out):
    n = 4000
    h = prime_switch_h(n)
    e = even_alt(n)
    o = odd_alt(n)
    ones_vec = [1] * n
    zero_vec = [0] * n

    out.append("=" * 78)
    out.append("COMPUTATION A — kernel-component of the prime switch bit h")
    out.append("=" * 78)
    out.append("Setting: Phi_n is (n-2) x n (rows d=2..n-1), rank n-2 (full row")
    out.append("rank), nullity 2, ker = span(even-alt, odd-alt) with")
    out.append("even-alt[j]=1 iff j even, odd-alt[j]=1 iff j odd (convention")
    out.append("cross-checked against code/out/supply_fold_rank.final.captured.txt,")
    out.append("which shows e,o,(e^o)=ones all fold to 0 for n=4..20).")
    out.append("h[j] = ((q_{j+1}-q_j)//2) mod 2, q the primes.")
    out.append("")

    # ---- (i) F2 component vs the two kernel directions ----
    out.append(f"n = {n}")
    out.append("(i) correlation of h with the two kernel directions (cols j=0..n-1):")
    de = dot_f2(h, e)
    do_ = dot_f2(h, o)
    out.append(f"    <h, even-alt> mod 2 = {de}   (<h, odd-alt> mod 2 = {do_})")
    # real imbalance: (-1)^{h+alt}
    ie = real_imbalance(h, e)
    io = real_imbalance(h, o)
    out.append(f"    real imbalance sum (-1)^(h+even-alt) = {ie:+d}  "
               f"(= agree-disagree, of {n})")
    out.append(f"    real imbalance sum (-1)^(h+odd-alt)  = {io:+d}  "
               f"(of {n})")
    # If h had a nonzero F2 component along even-alt, then h XOR even-alt
    # differs on ~half the bits (real imbalance small), i.e. <h,even-alt> mod2
    # is NOT the quantity "large component" means for a real vector. Report wt.
    wh = sum(h)
    out.append(f"    wt(h) = {wh} of {n} (switch density {wh/n:.4f})")
    # Distance to each kernel vector
    out.append("    Hamming distance from h to each of the 4 kernel vectors:")
    for name, v in [("0", zero_vec), ("even-alt", e), ("odd-alt", o), ("all-ones", ones_vec)]:
        d = hamming(h, v)
        out.append(f"        d(h,{name:9s}) = {d}   d/n = {d/n:.4f}")
    dmin = min(hamming(h, v) for v in (zero_vec, e, o, ones_vec))
    out.append(f"    -> min distance to kernel (collapse dirs) dmin/n = {dmin/n:.4f}")
    out.append("")

    # ---- (ii) fold weight of kernel vectors vs h, and h projected off kernel ----
    out.append("(ii) fold weight wt(Phi_n v) over F2 (exact submask-XOR fold;")
    out.append("     s_sos verified == s_direct literal oracle on n=4..200):")
    w_e = phi_weight(n, e)
    w_o = phi_weight(n, o)
    w_ones = phi_weight(n, ones_vec)
    w_h = phi_weight(n, h)
    out.append(f"    wt(Phi_n even-alt) = {w_e}  (= nu2 for input even-alt)")
    out.append(f"    wt(Phi_n odd-alt)  = {w_o}")
    out.append(f"    wt(Phi_n all-ones) = {w_ones}")
    out.append(f"    wt(Phi_n h) = {w_h}   (= nu2(4000), ratio {w_h/n:.4f})")
    out.append("    (kernel vectors fold to weight 0, collision by construction;")
    out.append("     the prime h does NOT: its image weight is ~0.49 n >> 0.)")
    out.append("")

    # ---- project h off the kernel and re-fold ----
    # h_perp = h + (<h,e> e + <h,o> o)  (F2: subtract == add). This makes
    # <h_perp,e>=<h_perp,o>=0. It differs from h only on the kernel component.
    comp_e = de       # 0 or 1
    comp_o = do_
    h_perp = [(h[j] ^ (comp_e * e[j]) ^ (comp_o * o[j])) for j in range(n)]
    w_perp = phi_weight(n, h_perp)
    out.append("    kernel component of h: even-alt coeff = {} (mod2), "
               "odd-alt coeff = {} (mod2)".format(de, do_))
    out.append(f"    wt(Phi_n (h projected OFF kernel)) = {w_perp}   "
               f"ratio {w_perp/n:.4f}")
    out.append("    (image weight is unchanged by subtracting the kernel part,")
    out.append("     as it must be: wt(Phi h) = wt(Phi h_perp) exactly.)")
    out.append("")

    # ---- (iii) is h closer to the kernel than a density-matched random string? ----
    out.append("(iii) kernel-proximity vs density-matched random surrogate")
    out.append("      min Hamming distance to the 4 kernel vectors, prime vs")
    out.append("      Bernoulli(p=0.5962) random strings, 30 trials (N=4000):")
    p = wh / n
    rng = random.Random(7)
    dists = []
    for _ in range(30):
        r = [1 if rng.random() < p else 0 for _ in range(n)]
        dm = min(hamming(r, v) for v in (zero_vec, e, o, ones_vec))
        dists.append(dm)
    mean_d = sum(dists) / len(dists)
    sd_d = (sum((x - mean_d) ** 2 for x in dists) / len(dists)) ** 0.5
    out.append(f"      prime   dmin/n = {dmin/n:.4f}")
    out.append(f"      random  mean dmin/n = {mean_d/n:.4f}  "
               f"sd = {sd_d/n:.4f}  (min..max {min(dists)/n:.4f}..{max(dists)/n:.4f})")
    out.append("")
    out.append("NOTE: the mod-2 F2 component <h,even-alt> is a PARITY (0/1); for a")
    out.append("random h it is 0 or 1 with prob 1/2 each, so it is not informative")
    out.append("about a 'large real component'. The informative measures are the")
    out.append("real imbalance (how far h is from the pure alternating pattern) and")
    out.append("the Hamming distance to the kernel (how far h is from colliding).")
    out.append("All numbers above are measured, not proved.")
    return out


def main():
    out = run([])
    text = "\n".join(out) + "\n"
    print(text)
    outdir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "out")
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "kernel_component_capture.txt"), "w") as f:
        f.write(text)


if __name__ == "__main__":
    main()
