#!/usr/bin/env python3
"""Extract exact excess sequence E2(n) = 2*nu2(n) - (n-2) = -S(n) via the
canonical oracle (lib.nu2.fold_nu2 = s_sos, cross-checked vs brute). Writes
plain sequences to files for the sequence tools.

nu2(n) = #{d in [2,n-1] : T(n,d)=1}, T the submask-XOR fold of the prime
gap-parity string h. SUPPLY (nu2 >= c*n) is equivalent to E2(n) >= (2c-1)n.
"""
import sys
sys.path.insert(0, "/workspace/code")
from lib.nu2 import fold_nu2
from lib.primes import h_string

def main(N):
    h = h_string(N + 2)
    nu2 = [0, 0]           # indexed by n (nu2[n])
    E2 = [0, 0]
    for n in range(2, N + 1):
        v = fold_nu2(n, h)
        nu2.append(v)
        E2.append(2 * v - (n - 2))
    # sanity: known canonical values
    assert nu2[53] == 18, nu2[53]
    assert nu2[4000] == 1975, nu2[4000]
    with open("out/excess_seq.txt", "w") as f:
        for n in range(2, N + 1):
            f.write(f"{n} {nu2[n]} {E2[n]}\n")
    # also first differences of E2
    with open("out/excess_diff.txt", "w") as f:
        for n in range(3, N + 1):
            f.write(f"{n} {E2[n] - E2[n-1]}\n")
    print(f"wrote out/excess_seq.txt n=2..{N}; nu2[53]={nu2[53]} nu2[64]={nu2[64]} "
          f"nu2[4000]={nu2[4000]} max|E2|={max(abs(E2[n]) for n in range(2,N+1))}")

if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 4000)
