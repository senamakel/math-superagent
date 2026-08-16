"""Independent exact oracle for nu2(n) under the operative definition.

nu2(n) = #{ d in [2, n-1] : T(n,d) = 1 }
T(n,d) = XOR over bitwise submasks o (subset of set bits) of d of h[n-1-d+o]
h[j]   = ((q_{j+1} - q_j)//2) mod 2,  primes q.

Verification targets (guarded in CONTEXT.md, all floored d in [2,n-1]):
  nu2(53)=18, nu2(64)=27, nu2(4000)=1975, and nu2(4000)/4000 ~ 0.4938.
"""
import sympy, sys

def h_of_primes(n):
    primes = list(sympy.primerange(2, sympy.nextprime(2) + 0))  # placeholder
    # build primes q_1..q_{n+1}
    ps = list(sympy.primerange(1, 10**9))
    q = ps[:n+1]
    h = [((q[j+1]-q[j])//2) % 2 for j in range(n)]
    return q, h

def T(n, d, h):
    # XOR over submasks o of d of h[n-1-d+o]
    res = 0
    o = d
    base = n-1-d
    while True:
        res ^= h[base + o]
        if o == 0:
            break
        o = (o-1) & d
    return res

def nu2(n, h):
    cnt = 0
    for d in range(2, n):
        if T(n, d, h):
            cnt += 1
    return cnt

def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    q, h = h_of_primes(N+1)
    print("h[:20] =", h[:20])
    for n in [53, 64, 100, 1000, 4000][:]:
        if n > N: continue
        print(f"nu2({n}) = {nu2(n, h)}   ratio = {nu2(n,h)/n:.6f}")
    # full small sweep to a file
    if N <= 2000:
        vals = [nu2(n,h) for n in range(2, N+1)]
        open('code/out/pattern_nu2_exact.txt','w').write(repr(vals))

if __name__ == "__main__":
    main()
