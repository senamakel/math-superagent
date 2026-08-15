"""Characterise the double-Wieferich odd-prime pairs (p<q): the only exponent
pairs the conditional non-Wieferich theorem does NOT already exclude. Ask:
which members are irregular (p | h^-(p), equivalently p | B_{2k} for some
even 2k<=p-3), the residues mod 12 / relations, and between two odd primes
whether the double-Wieferich congruences p^(q-1)==1 mod q^2, q^(p-1)==1 mod
p^2 can even be satisfied by regular primes. Exact integer arithmetic only.

A structural observation candidate: for a PROVEN double-Wieferich pair the
Fermat quotient condition q^(p-1)==1 mod p^2 is a strong constraint. Also
check the hypothesis that double-Wieferich pairs are impossible when both
primes are 'irregular' in a controlled way -- but that is a research question;
here we only COMPUTE the exact facts.
"""
import sympy
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


def irregular_indices(p):
    idx = []
    for k in range(1, (p - 3) // 2 + 1):
        B = sympy.bernoulli(2 * k)
        if B.p % p == 0:
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


# literature-known small double-Wieferich pairs
known = [(83, 4871), (2903, 18787), (911, 318917)]  # (397,?) omitted (unknown member)

print("Known small double-Wieferich pairs and their irregularity structure:")
print("=" * 90)
for (p, q) in known:
    ip = irregular_indices(p) if p <= 700 else None
    iq = irregular_indices(q) if q <= 700 else None
    ex1 = pow(q, p - 1, p * p) == 1
    ex2 = pow(p, q - 1, q * q) == 1
    print("  (%d, %d): both-congs=%s  irregular(p)=%s idx=%s   irregular(q)=%s idx=%s"
          % (p, q, ex1 and ex2,
             (len(ip) > 0) if ip is not None else "?(>700)",
             ip if ip else "-",
             (len(iq) > 0) if iq is not None else "?(>700)",
             iq if iq else "-"))

# Same for pairs found by this run's own exact search
print("=" * 90)
for B in [20000, 40000]:
    t = time.time()
    pairs = double_wieferich_pairs(B)
    print("B=%d: %d double-Wieferich pair(s) %s  (%.1fs)"
          % (B, len(pairs), pairs[:20], time.time() - t))
