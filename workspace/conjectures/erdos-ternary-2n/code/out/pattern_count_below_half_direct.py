"""Independent check of C_k = #{ r in A_k : r < 3^(k-1) } via the DIRECT
residue sieve (the exact oracle route), at the feasible small k.

A_k = { r mod 2*3^(k-1) : low k ternary digits of 2^r mod 3^k avoid 2 }.
Prior captures computed C_k by survivor LIFTING.  This recomputes it by the
independent direct enumeration of every residue (materialising 2^r mod 3^k,
no lifting), feasible only where 2*3^(k-1) is small enough to enumerate.
The point is a second route to the same C_k, and a check that it is never
exactly 2^(k-2) (an exact 50/50 split of the period) for any k here.
"""

import sys, time

def C_k_direct(k):
    period = 2 * 3 ** (k - 1)
    mod = 3 ** k
    half = 3 ** (k - 1)
    cnt, below = 0, 0
    for r in range(period):
        v = pow(2, r, mod)
        # low k digits avoid 2?
        w = v
        ok = True
        for _ in range(k):
            if w % 3 == 2:
                ok = False
                break
            w //= 3
        if ok:
            cnt += 1
            if r < half:
                below += 1
    return cnt, below

def main():
    cap = int(sys.argv[1]) if len(sys.argv) > 1 else 12
    print("=== independent direct-sieve recompute of C_k (k=2..%d) ===" % cap)
    seq = []
    for k in range(2, cap + 1):
        t0 = time.time()
        total, below = C_k_direct(k)
        seq.append(below)
        expect = 2 ** (k - 2)
        print(f"k={k:2d}  |A_k|={total}  C_k={below}  2^(k-2)={expect}  "
              f"equal={'YES' if below==expect else 'no'}  ({time.time()-t0:.1f}s)")
    print("C_k:", seq)
    bad = [k for k, c in zip(range(2, cap+1), seq) if c == 2**(k-2)]
    print("k with C_k == 2^(k-2):", bad if bad else "NONE (no exact half split)")

if __name__ == "__main__":
    main()
