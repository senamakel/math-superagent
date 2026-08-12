#!/usr/bin/env python3
"""
PE 761 — critical speed V(n) for a regular n-gon pool.

Implements the EXACT sourced formula of stewbasic (math.SE question 1762665,
"Active cat, inactive cat" / boy-escape-teacher regular n-gon), which
generalises the circular-pool critical speed identity to a regular n-gon.

Exact formula (stewbasic)
-------------------------
Let theta = pi/n and t = tan(theta).

  K   = largest integer in [0, n] with  sin(K*theta) - (K+n)*t*cos(K*theta) < 0
        (equivalently floor of the unique root of
         tan(x*theta) - (x+n)*t  in [1, n/2))

  alpha = 0.5 * ( K*theta + acos( 2*sin(K*theta) / ((K+n)*t) - cos(K*theta) ) )

  V(n) = 1 / cos(alpha)

The mechanism (boundary-time comparison, same as the circle goblin-in-the-lake
identity): the critical speed is the speed factor at which the swimmer's time
to reach a chosen boundary point equals the runner's perimeter travel time to
that point.  V(n) is the value that equalizes the two at optimal play.

Published anchors this routine must reproduce:
  n=3   -> 7.4049183473   (Abel et al.)
  n=4   -> 5.78859314459  (== statement oracle V_square = 5.78859314)
  n->inf-> 4.60333885     (circle oracle)

All arithmetic uses mpmath at mp.dps = 50 (exact high precision).

Usage:
    python code/solution.py
"""

import mpmath as mp

mp.mp.dps = 50


def critical_speed(n, dps=50):
    """Return (K, alpha, V) for a regular n-gon, all as mpmath numbers.

    K      : largest int in [0,n] with sin(K theta) - (K+n) t cos(K theta) < 0
    alpha  : the critical half-angle, 0.5*(K theta + acos(...))
    V      : critical runner-speed factor = 1/cos(alpha)
    """
    mp.mp.dps = dps
    theta = mp.pi / n
    t = mp.tan(theta)

    # K = largest integer k in [0, n] with sin(k theta) - (k+n) t cos(k theta) < 0
    K = None
    for k in range(0, n + 1):
        val = mp.sin(k * theta) - (k + n) * t * mp.cos(k * theta)
        if val < 0:
            K = k
    if K is None:
        raise ValueError(f"no K<0 for n={n}")

    inner = 2 * mp.sin(K * theta) / ((K + n) * t) - mp.cos(K * theta)
    # clamp acos argument to [-1, 1] for safety
    inner = mp.nstr(mp.mpf(max(-1.0, min(1.0, float(inner)))), dps)
    inner = mp.mpf(inner)
    alpha = mp.mpf("0.5") * (K * theta + mp.acos(inner))
    V = 1 / mp.cos(alpha)
    return K, alpha, V


def circle_limit(dps=50):
    """Circle critical speed from the Ponder-This identity tan(mu) = mu + pi,
    V = 1/cos(mu).  Independent of the polygon formula (sourced separately)."""
    mp.mp.dps = dps
    # root tan(mu) = mu + pi lies in (pi/2 - 1, pi/2); bracket it there
    # (tan has a pole at pi/2, so never start near/near the pole)
    mu = mp.findroot(lambda m: mp.tan(m) - m - mp.pi, (1.2, 1.5))
    return 1 / mp.cos(mu)


def main():
    print("=" * 72)
    print("PE 761 — regular n-gon critical speed  V(n) = 1/cos(alpha)")
    print("Exact stewbasic formula (math.SE 1762665); mpmath dps=50")
    print("=" * 72)

    results = {}
    for n in [3, 4, 6, 1000]:
        K, alpha, V = critical_speed(n)
        results[n] = V
        print(f"n={n:5d}: K={K:3d}  alpha={mp.nstr(alpha, 20):>22s}  "
              f"V={mp.nstr(V, 18):>22s}")

    print("-" * 72)
    # Property: as n -> inf the polygon converges to the circle (oracle 4.60333885)
    Vc = circle_limit()
    print(f"circle limit (tan mu = mu + pi)      V = {mp.nstr(Vc, 12)}  "
          f"oracle 4.60333885")
    print(f"n=1000 (finite-gon approximation)    V = {mp.nstr(results[1000], 12)}")
    print("-" * 72)

    # The ANSWER — hexagon, to the required precision.
    V_hex = results[6]
    print("ANSWER")
    print(f"  V_hexagon = V(6) to 15 decimals = {mp.nstr(V_hex, 16)}")
    print(f"  V_hexagon = V(6) to  8 decimals = {mp.nstr(V_hex, 9)}   <- the answer")

    print("-" * 72)
    print("Anchor checks")
    check3 = abs(results[3] - mp.mpf("7.4049183473")) < mp.mpf("1e-8")
    check4 = abs(results[4] - mp.mpf("5.78859314459")) < mp.mpf("1e-9")
    checkc = abs(Vc - mp.mpf("4.60333885")) < mp.mpf("1e-7")
    print(f"  n=3   -> {mp.nstr(results[3], 11)}   matches Abel et al. 7.4049183473 ? {check3}")
    print(f"  n=4   -> {mp.nstr(results[4], 12)}  matches oracle 5.78859314 ?      {check4}")
    print(f"  n->inf-> {mp.nstr(Vc, 10)}  matches circle oracle 4.60333885 ? {checkc}")


if __name__ == "__main__":
    main()
