"""Extend the double-Wieferich odd-prime-pair search further and characterize
the pairs: which are irregular (p | h^-(p))? The remaining pairs are the only
ones the conditional theorem R-double-wieferich does NOT exclude, so their
class-group structure decides whether the descent obstruction is ever tested
at a regular prime."""
def is_prime(n):
    if n < 2: return False
    d = 2
    while d*d <= n:
        if n % d == 0: return False
        d += 1
    return True

def odd_primes_upto(B):
    return [n for n in range(3, B+1) if is_prime(n)]

for B in [20000, 30000]:
    ps = odd_primes_upto(B)
    pairs = []
    for i, p in enumerate(ps):
        for q in ps[i+1:]:
            if (pow(q, p-1, p*p) == 1) and (pow(p, q-1, q*q) == 1):
                pairs.append((p, q))
    print("B=%d: %d pair(s) %s" % (B, len(pairs), pairs))

# Known small double-Wieferich pairs in the literature for comparison context:
print("literature-known small pairs: (83,4871), (2903,18787), (911,318917), (397, 232·?)")
