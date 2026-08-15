"""Independent fresh check of the mod-4 switch-majority ballot e(n)>=0,
and quantification of the empirical worst-case slack min e(n)/n over prefixes.

e(n) = sum_{k=3}^{n} (-u_k u_{k+1}), u_k = +1 if p_k=1 mod4, -1 if p_k=3 mod4,
over consecutive primes p_2..p_{n+1}.  Step +1 on a switch (gap ≡ 2 mod 4),
-1 on a non-switch.  Ballot: e(n) >= 0 for all n.
"""
import sys, time

def primes_upto_odds(n):
    if n < 2: return []
    sieve = bytearray(b'\x01') * (n//2)
    sieve[0] = 0
    r = int(n**0.5)
    for i in range(3, r+1, 2):
        if sieve[i//2]:
            start = i*i//2
            sieve[start::i] = b'\x00' * ((n - i*i)//(2*i) + 1)
    return [2] + [2*i+1 for i in range(1, n//2) if sieve[i]]

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 300_000_000
    t0 = time.time()
    P = primes_upto_odds(N)
    print(f"sieve to {N}: {len(P)} primes ({time.time()-t0:.1f}s)")
    # u_k for p_k, k>=1 (2-indexing of OEIS): p_1=2 -> even, ignore.
    # we need pairs from p_2=3 onward; among pairs k=3..n (0-based prime index k-1)
    # u for primes from p_2 (3) onward
    us = []
    for p in P:
        if p == 2: continue
        us.append(1 if p % 4 == 1 else -1)  # 3 mod 4 -> -1
    # switch step between consecutive primes u_k, u_{k+1} is -sum? e step+1 on switch
    e = 0
    min_e = None
    min_e_arg = None
    min_en = None; min_en_arg = None
    viol_first = None
    dips0 = 0
    n = 0
    # consecutive pairs among us[0..] ; pair index k: k=2 means us[0],us[1]
    for i in range(len(us)-1):
        ua, ub = us[i], us[i+1]
        step = 1 if ua != ub else -1   # switch iff residues differ
        e += step
        n += 1  # n = k
        # e(n) is current e
        if e < 0 and viol_first is None:
            viol_first = n
        if e == 0: dips0 += 1
        if min_e is None or e < min_e:
            min_e = e; min_e_arg = n
        if n >= 1:
            r = e/n
            if min_en is None or r < min_en:
                min_en = r; min_en_arg = n
    print(f"ballot e(n)>=0 over n in [1,{n}]: {'YES' if viol_first is None else 'VIOLATED at n='+str(viol_first)}")
    print(f"global min e = {min_e} at n={min_e_arg}; zero-dips count={dips0}")
    print(f"global min e/n = {min_en:.5f} at n={min_en_arg}")
    print(f"final e({n}) = {e}")
    print(f"time {time.time()-t0:.1f}s")

main()
