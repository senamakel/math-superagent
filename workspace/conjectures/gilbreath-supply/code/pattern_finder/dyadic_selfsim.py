#!/usr/bin/env python3
"""Test dyadic self-similarity of S(n) = (n-2) - 2*nu2(n)."""
import json
import numpy as np


def main():
    ny = json.load(open('code/out/nu2_primes_xor_40000.json'))
    def S(n): return (n - 2) - 2 * ny[n]

    sel = [n for n in range(100, 15000) if 2 * n + 1 < len(ny)]
    sn = np.array([S(n) for n in sel])
    s2n = np.array([S(2 * n) for n in sel])
    s2n1 = np.array([S(2 * n + 1) for n in sel])
    print(f"corr(S(2n),S(n)) = {np.corrcoef(sn, s2n)[0,1]:+.4f}")
    print(f"corr(S(2n+1),S(n)) = {np.corrcoef(sn, s2n1)[0,1]:+.4f}")
    print(f"mean|S(2n)|/sqrt(2n)={np.mean(np.abs(s2n)/np.sqrt(2*np.array(sel))):.3f}  "
          f"mean|S(n)|/sqrt(n)={np.mean(np.abs(sn)/np.sqrt(np.array(sel))):.3f}")
    # S(2n)-2*S(n)?
    print(f"mean(S(2n)-2S(n))={np.mean(s2n-2*sn):+.3f} std={np.std(s2n-2*sn):.3f}")
    # S(2n)+S(n)?
    print(f"mean(S(2n)+2S(n))={np.mean(s2n+2*sn):+.3f} std={np.std(s2n+2*sn):.3f}")


if __name__ == "__main__":
    main()
