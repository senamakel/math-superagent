#!/usr/bin/env python3
"""Independent check: the atomic bit Granville's nu2 consumes is the
consecutive-prime mod-4 switch, and nu2 is ~ n/2 with a big margin over n^0.525.

This reproduces (not from the catalogue, from a sharp sieve) two facts the
adopted chebyshev-bias-granville-nu2-supply approach measures:
  (a) bit_n = [p_{n+1} not≡ p_n (mod 4)] = [gap_n ≡ 2 (mod 4)]  -- every gap is
      even, and consecutive primes switch mod-4 class exactly when gap ≡ 2 mod 4.
  (b) nu2(n)/n ≈ 0.5, exceeding n^0.525 by a large factor at n = 3999.
"""
import sys, math

def sieve(n):
    bs = bytearray(b'\x01') * (n+1)
    bs[0:2] = b'\x00\x00'
    r = int(n**0.5)
    for i in range(2, r+1):
        if bs[i]:
            bs[i*i::i] = b'\x00' * (((n-i*i)//i)+1)
    return [i for i in range(2, n+1) if bs[i]]

def main(limit=3_000_000, n_check=3999):
    primes = sieve(limit)
    # gaps between consecutive primes
    gaps = [primes[i+1]-primes[i] for i in range(len(primes)-1)]
    # mod-4 switch bits: p_{i+1} not≡ p_i mod 4  <=> gap≡2 mod4 (gaps even)
    bits = [1 if g % 4 == 2 else 0 for g in gaps]
    # identity check: [p_{i+1} mod 4 != p_i mod 4] == [g%4==2]
    bad = 0
    for i, g in enumerate(gaps):
        pn, pn1 = primes[i], primes[i+1]
        if (pn1 % 4 != pn % 4) != (g % 4 == 2):
            bad += 1
    print(f"identity [p_{n+1}!=p_n mod4]==[gap%4==2]: mismatches = {bad} over {len(gaps)} gaps")
    # nu2 = running count of bits, at n_check
    nu2 = sum(bits[:n_check])
    print(f"nu2(n={n_check}) = {nu2}, nu2/n = {nu2/n_check:.4f}")
    print(f"n^0.525 at n={n_check} = {n_check**0.525:.3f}, margin factor = {nu2/(n_check**0.525):.1f}")
    # asymptotic sanity: fraction of gaps ≡2 mod4 over a long window
    for w in (1000, 10000, 100000):
        frac = sum(bits[:w])/w
        print(f"  fraction gap≡2 mod4 over first {w} gaps: {frac:.4f}")

if __name__ == "__main__":
    main(*(int(a) for a in sys.argv[1:]))
