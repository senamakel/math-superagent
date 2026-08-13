"""Verify that [2/pi] = i^{-b/2} etc. for primary Gaussian primes, derived from
the Williams (1976) primary anchors and checked against the definitional
quartic-residue evaluation.

Definitional quartic character of alpha mod Gaussian prime pi (Npi!=2):
  [alpha/pi]_4 = alpha^((Npi-1)/4) mod pi = i^k for unique k mod 4.
Check against Williams-derived closed forms (pi = a+bi primary: a+b==1 mod 4,
b even):
  [i/pi]   == i^{-(a-1)/2}
  [1+i/pi] == i^{(a-b-1-b^2)/4}
  [-1/pi]  == (-1)^{(a-1)/2}
  [2/pi]   == i^{-b/2}      (derived from 2 = (1+i)^2*(-i) + multiplicativity)
"""
import math

def is_prime(n):
    if n < 2: return False
    for d in range(2, int(math.isqrt(n))+1):
        if n % d == 0: return False
    return True

def gaussian_is_prime(a, b):
    q = a*a + b*b
    if q < 2: return False
    if q == 2: return True          # 1+i
    if is_prime(q) and q % 4 == 1: return True
    # inert: b==0 and a a rational prime == 3 mod 4
    if b == 0 and is_prime(abs(a)) and abs(a) % 4 == 3: return True
    return False

def gauss_mod(ar, ai, br, bi):
    den = br*br + bi*bi
    for _ in range(2):
        x = (ar*br + ai*bi) / den
        y = (ai*br - ar*bi) / den
        qr = round(x); qi = round(y)
        ar, ai = ar - qr*br + qi*bi, ai - qr*bi - qi*br
    return ar, ai

def pow_mod_gauss(a, e, br, bi):
    ar, ai = a
    res = (1, 0)
    base = (ar, ai)
    while e > 0:
        if e & 1:
            res = gauss_mod(res[0]*base[0] - res[1]*base[1],
                            res[0]*base[1] + res[1]*base[0], br, bi)
        e >>= 1
        if e:
            base = gauss_mod(base[0]*base[0] - base[1]*base[1],
                             2*base[0]*base[1], br, bi)
    return res

def quartic_char(alpha, br, bi):
    N = br*br + bi*bi
    exp = (N - 1)//4
    r, c = pow_mod_gauss(alpha, exp, br, bi)
    units = [(1,0),(0,1),(-1,0),(0,-1)]
    for k,(ur,uc) in enumerate(units):
        zr, zc = gauss_mod(r-ur, c-uc, br, bi)
        if zr == 0 and zc == 0:
            return k
    return None

def check(alim, blim):
    fails = []
    count = 0
    for a in range(1, alim, 2):
        for b in range(0, blim, 2):
            if not gaussian_is_prime(a, b): continue
            if (a + b) % 4 != 1: continue    # primary
            if a*a + b*b == 2: continue      # 1+i
            count += 1
            k_i   = quartic_char((0,1),  a, b)
            k_1pi = quartic_char((1,1),  a, b)
            k_m1  = quartic_char((-1,0), a, b)
            k_2   = quartic_char((2,0),  a, b)
            w_i   = ((-(a-1)//2)) % 4
            w_1pi = (((a - b - 1 - b*b)//4)) % 4
            w_m1  = (2*(((a-1)//2) % 2)) % 4
            w_2   = ((-b//2)) % 4
            for name, got, want in [('i',k_i,w_i),('1+i',k_1pi,w_1pi),
                                    ('-1',k_m1,w_m1),('2',k_2,w_2)]:
                if got != want:
                    fails.append((a,b,name,got,want))
            if count > 500:
                return count, fails
    return count, fails

if __name__ == "__main__":
    cnt, fails = check(400, 400)
    print(f"primary Gaussian primes tested: {cnt}")
    if not fails:
        print("ALL OK")
    else:
        print(f"{len(fails)} MISMATCHES:")
        for f in fails[:20]:
            print("  ", f)
