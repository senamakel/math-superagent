#!/usr/bin/env python3
"""Check the prime-gap-mod6-structure approach against the oracle.

The approach claims: halved gaps h_n = (p_{n+1}-p_n)/2 take values 0,1,2 mod 3
(gaps 0,2,4 mod 6). The halved Gilbreath triangle H_k(i)=A_k(i)/2 (k>=1, i>=1)
is the absolute-difference triangle of h_n. Claim: position-1 entries H_k(1)
mod 3 are always 0 or 1 (never 2).

We test this claim on the real rows. Also report, for each row k, whether H_k(1)
mod 3 ever equals 2, and the actual values of H_k(1) and their residues.
"""
from lib.gilbreath import primes_up_to, rows_generator


def main():
    N = 500_000            # sieve bound
    depth = 1200           # number of rows to generate
    primes = primes_up_to(N)
    gen = rows_generator(primes, depth)
    A0 = next(gen)         # primes
    # halved gaps h
    h = [ (A0[i+1] - A0[i]) // 2 for i in range(len(A0)-1) ]
    # check gap mod 6 structure
    gap_mod6 = set((2*hi) % 6 for hi in h[:200])
    print("set of gap mod 6 over first 200 gaps:", sorted(gap_mod6))
    empty = (A0[0])  # unused

    # H rows: H_0 = h (the halved gap sequence); H_{k+1}(i)=|H_k(i)-H_k(i+1)|
    H = h
    violations = []   # rows where H_k(1) mod 3 == 2
    values_at1 = []
    for k in range(1, depth+1):
        H = [abs(H[i]-H[i+1]) for i in range(len(H)-1)]
        v = H[1] if len(H) > 1 else None     # position 1 (index 1)
        if v is None:
            break
        values_at1.append((k, v, v % 3))
        if v % 3 == 2:
            violations.append((k, v))
    print(f"rows 1..{depth}: H_k(1) mod 3 == 2 count = {len(violations)}")
    if violations:
        print("first violations:", violations[:20])
    else:
        print("No violation: H_k(1) mod 3 is never 2 up to row", depth)
    # print some sample values
    print("sample (k, H_k(1), H_k(1)%3):", values_at1[:15])
    # how many distinct residues appear at position 1
    res = sorted(set(v % 3 for _, v, _ in values_at1))
    print("residue classes mod 3 appearing at position 1:", res)
    # Also check overall: the max value reached at position 1 (should be < 3 if bounded)
    mx = max(v for _, v, _ in values_at1)
    print("max H_k(1) reached:", mx, "mean:", sum(v for _, v, _ in values_at1)/len(values_at1))


if __name__ == "__main__":
    main()
