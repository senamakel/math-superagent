import numpy as np
from math import tan, cos, sin, acos, pi, sqrt

# stewbasic's general-n formula (Math.SE q.1762665, answer by stewbasic)
# pool = regular n-gon; theta = pi/n; critical multiplier lambda = 1/cos(alpha)
def stewbasic_lambda(n):
    th = pi / n
    # K = largest integer in [0,n] with sin(K*th) - (K+n)*tan(th)*cos(K*th) < 0
    # equivalently floor of the unique root of tan(x*th) - (x+n)*tan(th) in [1, n/2)
    K = None
    for k in range(0, n+1):
        val = sin(k*th) - (k+n)*tan(th)*cos(k*th)
        if val < 0:
            K = k
    # find unique root of f(x)=tan(x th) - (x+n) tan(th) in [1, n/2)
    from scipy.optimize import brentq
    def f(x): return tan(x*th) - (x+n)*tan(th)
    # root r should be in [1, n/2); K should equal floor(r)
    r = brentq(f, 1.0, n/2.0 - 1e-9)
    assert K == int(r), (K, r)
    # alpha
    inner = 2*sin(K*th)/((K+n)*tan(th)) - cos(K*th)
    inner = max(-1.0, min(1.0, inner))
    alpha = 0.5*(K*th + acos(inner))
    lam = 1.0/cos(alpha)
    return K, alpha, lam

for n in [4, 6, 8, 1000]:
    K, alpha, lam = stewbasic_lambda(n)
    print(f"n={n}: K={K}, alpha={alpha:.6f}, lambda={lam:.8f}")

# circle limit: tan mu = mu + pi, lambda = 1/cos mu
from scipy.optimize import brentq
mu = brentq(lambda m: tan(m) - m - pi, 4.0, 4.5)
lam_circ = 1/cos(mu)
print(f"circle limit: mu={mu:.6f}, lambda={1/cos(mu):.8f}  (oracle 4.60333885)")

# David K independent square value: v = sqrt(5/2*(7+sqrt(41)))
v_dk = sqrt(2.5*(7+sqrt(41)))
print(f"David K square closed form sqrt(5/2*(7+sqrt41)) = {v_dk:.8f}  (oracle 5.78859314)")

# circle Ponder-This: cos B = 1/V, sin B = (pi+B)/V  ->  tan B = pi+B
B = brentq(lambda b: tan(b) - pi - b, 1.0, 1.5)
print(f"circle Ponder-This: B={B:.6f}, V={1/cos(B):.8f}  (oracle 4.60333885)")
