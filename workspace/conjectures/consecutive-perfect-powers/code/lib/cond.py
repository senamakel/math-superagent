"""Necessary divisibility conditions on a hypothetical odd-prime solution of
x^p - y^q = 1 (Catalan's equation).

Imports: `from lib.cond import check_conditions, double_wieferich_pairs`.

All arithmetic is exact integer arithmetic (pow with 3 args for modular
exponentiation); no floats anywhere.

The mathematical background (sourced claim to be checked against the run's
research, skeleton `conditional-non-wieferich`):

  If x^p - y^q = 1 with x, y > 0 and p, q distinct odd primes, then
  (Cassels 1960) q | x and p | y, and the divisibility forces the two
  Wieferich congruences
      q^(p-1) = 1 (mod p^2)   and   p^(q-1) = 1 (mod q^2).
  So any odd-prime solution forces (p, q) to be a double-Wieferich pair.
  The known solution (3,2,2,3) has p = 2 (even), so it is OUTSIDE the
  hypothesis "p, q odd primes" and is excluded by hypothesis, never rejected.
"""


def is_odd_prime(n):
    """True iff n >= 3 is prime. Exact trial division (n small in all uses)."""
    if n < 2:
        return False
    if n == 2:
        return False  # 2 is prime but not ODD
    if n % 2 == 0:
        return False
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def check_conditions(p, q, x=None, y=None):
    """Evaluate the necessary divisibility conditions for exponents (p, q).

    Returns a dict with fields:
      is_odd_prime_pair : bool — True iff both p and q are odd primes (the
                          hypothesis under which the conditions are stated).
      vp_y : bool — Cassels condition p | y. With no concrete y supplied this
             reports "Cassels asserts p | y for a hypothetical odd-prime
             solution", i.e. equals is_odd_prime_pair. If a concrete y is
             given, it is the actual divisibility y % p == 0.
      vq_x : bool — Cassels condition q | x (mirror; actual x % q == 0 when
             a concrete x is supplied).
      wieferich_1 : bool — q^(p-1) == 1 (mod p^2).
      wieferich_2 : bool — p^(q-1) == 1 (mod q^2).

    Exact integer arithmetic throughout (pow(base, exp, mod)); never floats.

    Calibration at the known solution (p,q) = (2,3): is_odd_prime_pair is
    False because p = 2 is even, so all conditions are EXCLUDED BY HYPOTHESIS,
    not rejections of the known solution.
    """
    is_odd_pair = is_odd_prime(p) and is_odd_prime(q)

    if x is not None and y is not None:
        vq_x = (x % q == 0)      # Cassels: q | x, evaluated on a concrete x
        vp_y = (y % p == 0)      # Cassels: p | y, evaluated on a concrete y
    else:
        # No concrete solution object; the Cassels conditions are stated for a
        # hypothetical odd-prime solution, so they only "hold" under that
        # hypothesis. This is deliberately tied to is_odd_pair so that (2,3)
        # is reported as excluded-by-hypothesis rather than rejected.
        vq_x = is_odd_pair
        vp_y = is_odd_pair

    wieferich_1 = (pow(q, p - 1, p * p) == 1)   # q^(p-1) == 1 mod p^2
    wieferich_2 = (pow(p, q - 1, q * q) == 1)   # p^(q-1) == 1 mod q^2

    return {
        "is_odd_prime_pair": is_odd_pair,
        "vp_y": vp_y,
        "vq_x": vq_x,
        "wieferich_1": wieferich_1,
        "wieferich_2": wieferich_2,
    }


def odd_primes_upto(B):
    """Sorted list of odd primes <= B."""
    return [n for n in range(3, B + 1) if is_odd_prime(n)]


def double_wieferich_pairs(B):
    """List of odd prime pairs (p, q) with p < q, p, q <= B, and BOTH
        q^(p-1) == 1 (mod p^2)   and   p^(q-1) == 1 (mod q^2).
    Exact integer arithmetic only."""
    primes = odd_primes_upto(B)
    pairs = []
    for i, p in enumerate(primes):
        for q in primes[i + 1:]:
            if (pow(q, p - 1, p * p) == 1) and (pow(p, q - 1, q * q) == 1):
                pairs.append((p, q))
    return pairs


def crossprime_condition(p, q, hminus=None):
    """Evaluate the cross-prime minus-class-number divisibility condition on
    the exponent pair (p, q):  q | h^-(Q(zeta_p))  AND  p | h^-(Q(zeta_q)).

    This is the descent's claimed consequence for a hypothetical odd-prime
    solution x^p - y^q = 1 (cross-prime, q != p; governed by the analytic
    Bernoulli product, distinct from the same-prime Herbrand-Ribet statement).

    Parameters
    ----------
    p, q : int — the two exponents.
    hminus : dict {prime: int} or None — precomputed h^-(Q(zeta_n)) values for
        the primes involved, so the caller can avoid re-computing the expensive
        Bernoulli products.  If absent (or missing a key), h^-(Q(zeta_n)) is
        computed exactly via lib.cyclo.h_minus.  Exact integer arithmetic.

    Returns a dict:
      is_odd_prime_pair : bool — True iff both p and q are odd primes.
      q_divides_hminus_p : bool — q | h^-(Q(zeta_p)) (or None if p not prime).
      p_divides_hminus_q : bool — p | h^-(Q(zeta_q)) (or None if q not prime).
      satisfied : bool — both divisibilities hold (None unless is_odd_pair).

    Calibration at the known solution (p, q) = (2, 3): p = 2 is even, so
    is_odd_prime_pair is False and the condition is EXCLUDED BY HYPOTHESIS
    (vacuous), never a rejection of the known solution.
    """
    is_odd_pair = is_odd_prime(p) and is_odd_prime(q)
    if not is_odd_pair:
        return {
            "is_odd_prime_pair": False,
            "q_divides_hminus_p": None,
            "p_divides_hminus_q": None,
            "satisfied": None,
        }

    def _hminus(n):
        if hminus is not None and n in hminus:
            return hminus[n]
        from lib.cyclo import h_minus
        return h_minus(n)

    qDp = (_hminus(p) % q == 0)   # q | h^-(Q(zeta_p))
    pDq = (_hminus(q) % p == 0)   # p | h^-(Q(zeta_q))
    return {
        "is_odd_prime_pair": True,
        "q_divides_hminus_p": qDp,
        "p_divides_hminus_q": pDq,
        "satisfied": qDp and pDq,
    }
