"""Verify the Kummer connection: for an odd prime p,
    p | h^-(Q(zeta_p))  <=>  p | B_{2k} for some even 2k with 2 <= 2k <= p-3
This is the exact structural fact behind the 'irregular primes' column of the
pattern tables. We compare it against the h^- values already computed exactly
(pattern_sequences) over a range, and list for each irregular prime the even
Bernoulli indices whose numerator p divides (its 'index of irregularity').

All exact integer arithmetic: Bernoulli numbers via sympy (exact rationals),
numerators reduced mod p.
"""
import sympy
import time

# h^-(Q(zeta_p)) computed exactly earlier in this run (code/out/hminus_full100)
hminus = {
    3: 1, 5: 1, 7: 1, 11: 1, 13: 1, 17: 1, 19: 1, 23: 3, 29: 8, 31: 9,
    37: 37, 41: 121, 43: 211, 47: 695, 53: 4889, 59: 41241, 61: 76301,
    67: 853513, 71: 3882809, 73: 11957417, 79: 100146415, 83: 838216959,
    89: 13379363737, 97: 411322824001,
}


def irregular_bernoulli_indices(p):
    """Even indices 2k, 2 <= 2k <= p-3, with p | numerator(B_{2k})."""
    idx = []
    for k in range(1, (p - 3) // 2 + 1):
        B = sympy.bernoulli(2 * k)
        num = B.p  # exact numerator; B = num/den
        if num % p == 0:
            idx.append(2 * k)
    return idx


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


# ---- 1. Verify p | h^- <=> (some even B_{2k}, 2k<=p-3 has p | numerator) ----
print("Verify over primes 3..N:  p | h^-(p)  <=>  p | B_{2k} for some even 2k<=p-3")
print("=" * 78)
B = 700
primes = [n for n in range(3, B + 1) if is_prime(n)]
mismatches = 0
for p in primes:
    # compute h^-(p) mod p directly from the Bernoulli product where p is
    # the conductor, is expensive, so instead use the theorem direction that
    # can be checked with the already-computed h^- for p<100 plus the pure
    # Bernoulli criterion for all p here.
    bi = irregular_bernoulli_indices(p)
    p_div_hminus_bernoulli = len(bi) > 0
    # For p < 100 we have exact h^-: cross-check the two notions agree.
    if p in hminus:
        ph = (hminus[p] % p == 0)
        if ph != p_div_hminus_bernoulli:
            mismatches += 1
            print("MISMATCH p=%d: h^- divis=%s, bernoulli divis=%s" % (p, ph, p_div_hminus_bernoulli))
    if len(bi) > 0:
        print("  p=%4d IRREGULAR  even-Bernoulli indices with p|num: %s" % (p, bi))
print("primes checked <= %d; cross-check mismatches (p | h^- vs p | B even): %d"
      % (B, mismatches))

# ---- 2. For the specific irregular primes, give index of irregularity ----
print("=" * 78)
print("Index of irregularity (number of even k, 2k<=p-3, with p|B_{2k}) for p<100 irregular primes:")
for p in sorted(hminus):
    if hminus[p] % p == 0:
        bi = irregular_bernoulli_indices(p)
        print("  p=%3d  h^-=%d  p|h^-=%s  index-of-irregularity=%d  indices=%s"
              % (p, hminus[p], True, len(bi), bi))
