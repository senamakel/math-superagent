"""Verify the mechanism step of the Christol bridge (christol-bridge-dyadic-step2.md).

Claim under test (asserted in subset-zeta-preserves-automaticity-christol):
the F2 subset-zeta (Mobius) transform zeta(h)[d] = sum_{j subseteq d} h[j] (mod 2)
acts on the generating function H(t) = sum_j h[j] t^j as the rational
substitution  Z(t) = (1/(1+t)) * H(t/(1+t))  over F2[[t]].

We test agreement as truncated formal power series over F2, for all bit
strings h up to length L (the full set of 2^L inputs), comparing coefficient
vectors of:
  route A: direct subset-zeta computation zeta(h)[d] for d=0..N-1
  route B: formal power series identity (1/(1+t)) * H(t/(1+t)) truncated,
           computed by truncated polynomial composition/inversion over F2.
"""
import itertools

def subset_zeta(h, N):
    """h: list of bits (h[j] for j>=0). Return zeta[h][d] for d=0..N-1, mod 2.
       zeta[h][d] = sum_{j submask of d} h[j] mod 2."""
    out = []
    for d in range(N):
        s = 0
        for j in range(len(h)):
            if j > d:
                break
            if (j & ~d) == 0 and j <= d:
                s += (h[j] & ((d & j) == j))  # (j submask of d)
        out.append(s & 1)
    return out

def subset_zeta_clean(h, N):
    out = []
    for d in range(N):
        s = 0
        for j in range(min(len(h), d+1)):
            if (d & j) == j:      # j is a bitwise submask of d
                s += h[j]
        out.append(s & 1)
    return out

def poly_sub(u, deg):  # (1/(1+u)) truncated: 1 + u + u^2 + ... over F2
    # 1/(1+u) = sum_{i>=0} u^i  (1 + u + u^2 + ...) since -1 = 1 in F2
    return [1]*(deg+1)  # geometric series: all coefficients 1 (u^i has coeff 1)

def poly_mul(a, b, deg):
    c = [0]*(deg+1)
    for i in range(min(len(a), deg+1)):
        if a[i]:
            for j in range(min(len(b), deg+1-i)):
                if b[j]:
                    c[i+j] ^= 1
    return c

def poly_pow(u, k, deg):
    r = [1]+[0]*deg
    b = u[:]
    while k:
        if k & 1:
            r = poly_mul(r, b, deg)
        b = poly_mul(b, b, deg)
        k >>= 1
    return r

def comp_pow_dec(u, deg):
    """Compute J(t) = u(t) where u = t/(1+t) truncated, i.e. compute the
       substitution H(t/(1+t)) for a general H is what route B needs; here
       we instead directly compute Z via series composition.

       We want Z(t) = (1/(1+t))^? ... simpler: build the actual truncated
       power series of t/(1+t) and compose.
    """
    # J(t) = t/(1+t) = t*(1/(1+t)) = t * (1 + t + t^2 + ...) truncated
    J = [0]+[1]*deg   # coeff of t^i for i>=1 is 1
    return J[:deg+1]

def poly_compose(H, J, deg):
    """H(J(t)) truncated to deg, over F2, where H and J are coefficient lists.
       H has h[j] t^j; J has constant term 0 so composition is well-defined."""
    # result = sum_j H[j] * J^j
    r = [0]*(deg+1)
    # powers of J
    Jpow = [ [1]+[0]*deg ]  # J^0
    for _ in range(len(H)):
        Jpow.append(poly_mul(Jpow[-1], J, deg))
    for j in range(len(H)):
        if H[j]:
            p = Jpow[j]
            for i in range(deg+1):
                if p[i]:
                    r[i] ^= 1
    return r

def zeta_route(H_t, J, one_over_1pt, deg):
    # Z = (1/(1+t)) * H(t/(1+t))
    comp = poly_compose(H_t, J, deg)
    return poly_mul(one_over_1pt, comp, deg)

def run(L, N):
    J = comp_pow_dec(deg=N)               # t/(1+t) truncated
    oneov = poly_sub(None, N)             # 1+t+t^2+... = 1/(1+t)
    bad = 0
    for bits in itertools.product([0,1], repeat=L):
        h = list(bits)
        # route A: direct zeta
        A = subset_zeta_clean(h, N)
        # route B: series identity
        Ht = h + [0]*(N+1-len(h))
        B = zeta_route(Ht[:N+1], J, oneov, N)
        if A != B:
            bad += 1
            if bad <= 3:
                print("MISMATCH h=", h, "zeta=", A[:10], "series=", B[:10])
    return bad

if __name__ == "__main__":
    for L in [3, 4, 5, 6]:
        N = 2**L + 3
        bad = run(L, N)
        total = 2**L
        print(f"L={L}: all {total} bit strings, truncated degree {N}: mismatches = {bad}")
    # Also one longer single-string check up to degree 64
    import time
    h = [ (bin(i).count('1') & 1) for i in range(0, 64) ]  # Thue-Morse prefix
    N = 64
    A = subset_zeta_clean(h, N)
    J = comp_pow_dec(deg=N)
    oneov = poly_sub(None, N)
    B = zeta_route(h[:N+1], J, oneov, N)
    print("Thue-Morse prefix L=64, N=64: zeta==series?", A==B)
    mielsen = [ i for i,(a,b) in enumerate(zip(A,B)) if a!=b ]
    print("first mismatches:", mielsen[:5])
