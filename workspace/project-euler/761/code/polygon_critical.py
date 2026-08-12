import sympy as sp

# Exact formula for regular n-gon critical speed (stewbasic, math.SE):
# theta = pi/n, K = floor of unique root of tan(x*theta) - (x+n)*tan(theta) in [1, n/2)
# such that sin(K*theta) - (K+n)*tan(theta)*cos(K*theta) < 0
# alpha = 1/2*(K*theta + arccos(2*sin(K*theta)/((K+n)*tan(theta)) - cos(K*theta)))
# lambda = 1/cos(alpha)
#
# This formula is stated (by stewbasic) to give lambda=5.789 for square. Validate against
# the oracle V_square = 5.78859314, then compute hexagon.

def critical_speed(n, dps=15):
    theta = sp.pi / n
    tan_th = sp.tan(theta)
    # find K: largest integer with sin(K*theta) - (K+n)*tan_th*cos(K*theta) < 0
    K = None
    for k in range(0, n+1):  # K between 0 and n
        val = sp.sin(k*theta) - (k+n)*tan_th*sp.cos(k*theta)
        if val < 0:
            K = k
    if K is None:
        return None
    # also K should be floor of root; verify consistency
    # cross-check: K heard of as floor(root) in [1,n/2) - find the root to confirm
    # compute alpha
    inner = 2*sp.sin(K*theta)/((K+n)*tan_th) - sp.cos(K*theta)
    # clamp inner to [-1,1]
    inner = sp.Max(sp.Min(inner, 1), -1)
    alpha = sp.Rational(1,2)*(K*theta + sp.acos(inner))
    lam = 1/sp.cos(alpha)
    return K, alpha, lam

for n in [4, 6, 1000]:
    r = critical_speed(n)
    K, alpha, lam = r
    print(f"n={n}: K={K} alpha={alpha.evalf(15)} lambda={lam.evalf(15)}")

# Validate square
K4, a4, l4 = critical_speed(4)
print("\nsquare oracle:", 5.78859314, "formula:", l4.evalf(12))

# Print the sequence V(n) for n=3..20
print("\nV(n) sequence:")
for n in range(3, 21):
    K, alpha, lam = critical_speed(n)
    print(n, round(lam.evalf(12), 8))
