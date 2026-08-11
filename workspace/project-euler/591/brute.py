import math

def bqa(d, x, n):
    """Naive BQA: minimize |a + b*sqrt(d) - x| with |a|,|b| <= n.
    Returns (a, b, error)."""
    sd = math.sqrt(d)
    best = None
    for b in range(-n, n+1):
        # a = nearest integer to x - b*sd, clamped to [-n,n]
        av = round(x - b*sd)
        if av < -n: av = -n
        if av > n: av = n
        err = abs(av + b*sd - x)
        if best is None or err < best[2]:
            best = (av, b, err)
    return best

pi = math.pi
print("BQA_2(pi,10) =", bqa(2, pi, 10))
print("BQA_5(pi,100) =", bqa(5, pi, 100))
print("BQA_7(pi,10^6) =", bqa(7, pi, 10**6))
