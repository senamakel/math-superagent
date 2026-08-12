"""Verify stewbasic's general-n formula from Math.SE q.1762665 against the
oracle values V_square and V_hexagon (target)."""
import math

def stewbasic(n):
    """lambda = cutoff speed ratio for regular n-gon (stewbasic formula)."""
    theta = math.pi / n
    tanth = math.tan(theta)
    # K = largest integer in [0,n] with sin(K th) - (K+n) tanth cos(K th) < 0
    K = None
    for k in range(0, n + 1):
        val = math.sin(k * theta) - (k + n) * tanth * math.cos(k * theta)
        if val < 0:
            K = k
    assert K is not None
    # alpha
    inner = 2 * math.sin(K * theta) / ((K + n) * tanth) - math.cos(K * theta)
    inner = max(-1.0, min(1.0, inner))
    alpha = 0.5 * (K * theta + math.acos(inner))
    lam = 1.0 / math.cos(alpha)
    return K, alpha, lam

for n in (4, 6):
    K, alpha, lam = stewbasic(n)
    print(f"n={n}: K={K}, alpha={alpha:.10f}, lambda={lam:.10f}")

# David K closed form for square
vsq = math.sqrt(2.5 * (7 + math.sqrt(41)))
print("David K square closed form sqrt(5/2(7+sqrt41)) =", vsq)

# Oracle
print("Oracle V_square = 5.78859314")
