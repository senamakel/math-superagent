"""Structural facts about the minimal double-Wieferich pairs — the exponent
pairs the conditional non-Wieferich theorem does NOT exclude.

1. For (83, 4871): compute h^-(Q(zeta_83))'s divisibility by 83 and 4871.
   83 | h^-(83)? and 4871 | h^-(83)?  -> the torsion of the class group of the
   descent field Q(zeta_83) at the two exponent primes.
2. Irregularity of 2903 (smaller member of the 2nd double-Wieferich pair) and
   of the smaller members found by search, using a fast mod-p Bernoulli
   recurrence (exact, since for even 2k <= p-3, p {bar} denominator(B_{2k})
   by von Staudt-Clausen, so p | numerator(B_{2k}) iff B_{2k} == 0 (mod p)).
3. Extend the double-Wieferich search to larger B and list the pairs found.
All exact integer arithmetic.
"""
import time


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def h_minus_mod(p, hminus_file=None):
    pass


def bernoulli_even_modp(p):
    """Return the list of B_{2k} mod p for 1 <= k <= (p-3)//2, using the exact
    recurrence B_n = -1/(n+1) sum_{k=0}^{n-1} C(n+1,k) B_k  in F_p.
    For these n (<= p-3) the denominators n+1 and the Bernoulli denominators
    are invertible mod p, so this is exact."""
    B = [0] * (p + 1)   # index n, work mod p
    B[0] = 1
    # C(n+1,k) mod p computed incrementally along each row
    b_even = []
    for n in range(1, p - 2 + 1):   # up to n = p-3+1? we need B_{2k}, 2k<=p-3
        # compute sum_{k=0}^{n-1} C(n+1,k) B_k mod p
        s = 0
        c = 1  # C(n+1, 0) = 1
        for k in range(0, n):
            c = c * (n + 1 - k) * pow(k + 1, p - 2, p) % p  # C(n+1,k+1) from C(n+1,k)
            s = (s + (B[k] * c if k > 0 else B[k])) % p
        B[n] = (-s * pow(n + 1, p - 2, p)) % p
    # collect even <= p-3
    out = []
    for k in range(1, (p - 3) // 2 + 1):
        out.append(B[2 * k])
    return out


def is_irregular(p, maxp=700):
    if p > maxp:
        ev = bernoulli_even_modp(p)
        return any(b == 0 for b in ev)
    else:
        return False  # handled separately


def irregular_indices_small(p):
    import sympy
    idx = []
    for k in range(1, (p - 3) // 2 + 1):
        if sympy.bernoulli(2 * k).p % p == 0:
            idx.append(2 * k)
    return idx


def double_wieferich_pairs(B):
    ps = [n for n in range(3, B + 1) if is_prime(n)]
    pairs = []
    for i, p in enumerate(ps):
        for q in ps[i + 1:]:
            if (pow(q, p - 1, p * p) == 1) and (pow(p, q - 1, q * q) == 1):
                pairs.append((p, q))
    return pairs


# ---- 1. torsion of Q(zeta_83) at 83 and 4871 ----
print("Q(zeta_83): h^-(83) = 838216959 (exact, from earlier run)")
print("  83 | h^-(83)? ", 838216959 % 83 == 0)
print("  4871 | h^-(83)? ", 838216959 % 4871 == 0)
print("  83 regular (83 ∤ any B_{2k}, 2k<=80)? ", irregular_indices_small(83) == [])

# ---- 2. irregularity of double-Wieferich smaller members ----
print("=" * 78)
print("Irregularity test for smaller members of known double-Wieferich pairs")
for p in [83, 2903, 911]:
    if p <= 700:
        idx = irregular_indices_small(p)
        print("  p=%d: irregular? %s  indices=%s" % (p, len(idx) > 0, idx))
    else:
        t = time.time()
        ev = bernoulli_even_modp(p)
        idx = [2 * (k + 1) for k, b in enumerate(ev) if b == 0]
        print("  p=%d: irregular? %s  indices=%s  (%.1fs)" % (p, len(idx) > 0, idx[:20], time.time() - t))

# ---- 3. extend double-Wieferich search ----
print("=" * 78)
for B in [60000, 120000, 200000]:
    t = time.time()
    pairs = double_wieferich_pairs(B)
    print("B=%6d: %d pair(s) %s  (%.1fs)" % (B, len(pairs), pairs[:20], time.time() - t))
