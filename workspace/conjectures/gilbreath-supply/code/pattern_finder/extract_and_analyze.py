#!/usr/bin/env python3
"""Extract nu2(n) and S(n) for the primes and run structural analysis.

nu2(n) = wt(Phi_n h) = #{d in [2,n-1] : T(n,d)=1}, exact via s_sos.
S(n) = (n-2) - 2*nu2(n)   (signed fold deviation; = sum_d (-1)^{T(n,d)}).

Reads nu2(n) for n=2..513 from code/out/nu2_terms.txt (already computed) and
extends via s_sos to a larger N, streaming one n at a time. Writes sequences
to /tmp for the sequence tools.
"""

import sys, os
sys.path.insert(0, '/workspace/code')  # noqa  -- actually code is on PYTHONPATH
from lib.primes import primes_upto_index

def nu2_sos(n, h, cache=None):
    """Exact nu2(n) via the SOS submask-product fold (verified == submask XOR
    oracle). Returns count of T=1 for d in [2,n-1]."""
    from lib.supply_fold import s_sos
    S, ones = s_sos(n, h)
    return ones


def load_known_terms():
    """nu2(n) for n=2..513 from code/out/nu2_terms.txt."""
    terms = {}
    with open('/workspace/code/out/nu2_terms.txt') as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            p = line.split()
            if len(p) == 2:
                terms[int(p[0])] = int(p[1])
    return terms


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    known = load_known_terms()
    print(f"known terms: n=2..{max(known)} count={len(known)}")

    # primes up to q_{N+1} so h index reaches N-1
    ps = primes_upto_index(N + 1)
    # h[j] = ((q_{j+1}-q_j)//2) mod 2; length N (indices 0..N-1), since
    # s_sos(n,h) reads h[0..n-1].
    h = [((ps[j + 1] - ps[j]) // 2) % 2 for j in range(N)]

    out = []
    for n in range(2, N + 1):
        if n in known:
            v = known[n]
        else:
            v = nu2_sos(n, h)
        out.append(v)

    nu2 = {i + 2: out[i] for i in range(len(out))}

    # S(n) = (n-2) - 2*nu2(n)
    S = {n: (n - 2) - 2 * nu2[n] for n in nu2}

    with open('/tmp/nu2_seq.txt', 'w') as f:
        for n in range(2, N + 1):
            f.write(f"{n} {nu2[n]}\n")
    with open('/tmp/S_seq.txt', 'w') as f:
        for n in range(2, N + 1):
            f.write(f"{n} {S[n]}\n")

    # sanity: reproduce nu2(4000)=1975/nu2(53)=18/nu2(64)=27; report nu2/n
    for n, expect in [(53, 18), (64, 27), (4000, 1975)]:
        got = nu2.get(n, 'n/a')
        print(f"n={n} nu2={got}  expect~{expect}  {'OK' if got==expect else 'CHECK'}")
    print("nu2/n at selected n:")
    for n in [100, 1000, 4000]:
        print(f"  n={n}: {nu2[n]}/{n} = {nu2[n]/n:.4f}  S={S[n]}")
    print("max |S(n)|/sqrt(n) over [50,N] and its argmax:")
    best = max((abs(S[n]) / (n ** 0.5), n) for n in range(50, N + 1))
    print(f"  max|S|/sqrt n = {best[0]:.3f} at n={best[1]}")
    print("Cumulative / prefix facts saved to /tmp.")


if __name__ == "__main__":
    main()
