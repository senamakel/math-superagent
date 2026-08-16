#!/usr/bin/env python3
"""Compute nu2(n) by the literal definition from problem.md for a clean
canonical sequence, cross-checked against the endpoint character-sum form.

Literal definition:
  A_0(i)=q_{i+1}; A_{k+1}(i)=|A_k(i)-A_k(i+1)|.
  delta_k(n)=A_k(n-1-k), k=0..n-1  (right diagonal through column n).
  Read from bottom, longest unbroken run of cells with value 0 or 2,
  nu2(n) = number of 2s in that run.
"""
import sys

def primes_upto_index(n):
    ps, cand = [2], 3
    while len(ps) < n:
        ok = True
        r = int(cand**0.5)
        for p in ps:
            if p > r: break
            if cand % p == 0: ok = False; break
        if ok: ps.append(cand)
        cand += 2
    return ps

def nu2_literal(n, ps):
    """ps = primes list (full, index 0..n-1 is q_1..q_n)."""
    diag = [ps[n-1]]
    row = ps[:n]
    while len(row) > 1:
        row = [abs(row[i]-row[i+1]) for i in range(len(row)-1)]
        diag.append(row[-1])
    # diag[k] = delta_k(n), k=0..n-1
    cnt = 0
    for k in range(n-1, -1, -1):
        v = diag[k]
        if v == 0 or v == 2:
            if v == 2: cnt += 1
        else:
            break
    return cnt

def nu2_endpoint(n, ps):
    """h[j]=((q_{j+1}-q_j)//2)%2 ; nu2=(n-2-S)/2 with S=endpoint sum.
    Using the d in [2,n-1] convention."""
    S = 0
    for j in range(n-1):
        h = ((ps[j+1]-ps[j])//2) % 2
        S += (1 if h else -1)
    return (n-2-S)//2

def main():
    N = int(sys.argv[1]) if len(sys.argv)>1 else 800
    ps = primes_upto_index(N+2)
    seq = []
    for n in range(2, N+1):
        seq.append(nu2_literal(n, ps))
    # cross-check subset against endpoint
    for n in [100, 200, 500]:
        e = nu2_endpoint(n, ps)
        print(f"n={n} literal={seq[n-2]} endpoint={e} diff={seq[n-2]-e}")
    print("LITERAL", ' '.join(map(str,seq)))

if __name__ == "__main__":
    main()
