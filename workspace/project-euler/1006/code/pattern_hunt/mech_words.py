#!/usr/bin/env python3
"""PE1006: mechanical-word factor generator with POSITION data.

Returns the k+1 distinct length-k factors of the Fibonacci word as exact
strings (leading zeros kept), by the mechanical (rotation) construction:

  slope a = p/q, q = Fibonacci number > k (all cut points distinct);
  cut points {-m*a mod 1 : m = 0..k} partition the circle into k+1 arcs;
  the factor on each arc, read at its midpoint x with
      digit_j(x) = floor(x + (j+1)a) - floor(x + j a),  j = 0..k-1,
  is one of the k+1 distinct length-k factors (mechanical-word theorem;
  verified against code/brute.py for k <= 50 by mech_psi.py).

All arithmetic exact integer.  We work in units of 1/q:
  cut point for m is  c_m = (-m*p) mod q  (integer in [0, q)).
  Arc i: from c_i to c_{i+1} (c_{k+1} = c_0 + q).
  Midpoint x = (c_i + c_{i+1}) / (2q).
  digit_j(x) = floor( (c_i+c_{i+1})/2 + j*p ) / q ) - floor( (c_i+c_{i+1})/2 + (j+1)*p )/q )
  with the convention floor over rationals: floor( (N + jp*2q ... ) hmm, see code.
"""
from math import gcd


def fib_q_gt(k):
    a, b = 1, 1
    while b <= k:
        a, b = b, a + b
    return b


def mech_words(k):
    """Return sorted list of the k+1 distinct length-k factor strings."""
    q = fib_q_gt(2 * k)          # q > 2k: safe margin; distinct cut points
    p = None
    # p/q must be a Fibonacci convergent of 1/phi^2 with denominator q.
    # Fibonacci denominators: q = F_n, p = F_{n-2}.
    a, b = 1, 1
    while b < q:
        a, b = b, a + b
    # now b == q, and a = previous Fibonacci = F_{n-1}; need F_{n-2}:
    # rewind one more step
    # easier: regenerate with tracking
    f = [1, 1]
    while f[-1] < q:
        f.append(f[-1] + f[-2])
    assert f[-1] == q
    p = f[-3] if len(f) >= 3 else 0
    if q == 1:
        p = 0
    assert gcd(p, q) == 1 or p == 0

    pts = sorted(((-m * p) % q) for m in range(k + 1))
    words = []
    for i in range(k + 1):
        c1 = pts[i]
        c2 = pts[(i + 1) % (k + 1)] if i < k else pts[0] + q
        # midpoint x = (c1 + c2) / (2q) ; digit j:
        # floor(x + (j+1)a) - floor(x + j a),  a = p/q
        # x + j a = (c1 + c2 + 2 j p) / (2q)
        digs = []
        for j in range(k):
            lo = (c1 + c2 + 2 * j * p) // (2 * q)
            hi = (c1 + c2 + 2 * (j + 1) * p) // (2 * q)
            digs.append('1' if hi - lo else '0')
        words.append(''.join(digs))
    return sorted(words)


if __name__ == '__main__':
    # sanity vs recorded exact Psi and brute factor sets
    from math import isqrt
    SCALE = 4 ** 60
    SQRT5 = isqrt(5 * SCALE * SCALE)

    def c1f(k):
        return 1 + (3 * k * SCALE - k * SQRT5) // (2 * SCALE)

    bad = 0
    for k in range(1, 51):
        ws = mech_words(k)
        assert len(ws) == k + 1, (k, len(ws))
        pc = [sum(1 for w in ws if w[j] == '1') for j in range(k)]
        dev = [p - c1f(k) for p in pc]
        if any(abs(d) > 1 for d in dev):
            bad += 1
            print("  k=", k, "|dev|>1", dev)
    print("mech_words: k=1..50 count=k+1 and |dev|<=1:", bad == 0)
