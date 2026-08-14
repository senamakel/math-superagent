import sympy as sp

# Derive f_d(k*10^m + x) - f_d(x) = k*m*10^(m-1) for k<=d-1, 0<=x<10^m.
# Using the classical closed form: f_d(n) = sum over positions with place-value
# identity. For n whose top digit is k<d and remaining part x (<10^m):
#   f_d(k*10^m + x) = [f_d(x) contribution adjusted] + ...
# Cleanest independent check: verify the identity symbolically on small explicit
# exponents by brute force enumeration (tiny numbers) — full brute force.

def f_naive(n, d):
    return sum(str(i).count(str(d)) for i in range(0, n+1))

# Check identity by brute force for small m where numbers stay tiny.
bad = []
for m in range(1, 5):
    for d in range(1, 10):
        for k in range(0, d):
            for x in range(0, 10**m):
                n = k*10**m + x
                lhs = f_naive(n, d) - f_naive(x, d)
                pred = k * m * 10**(m-1)
                if lhs != pred:
                    bad.append((m,d,k,x,lhs,pred))
                    if len(bad) > 5: break
            if len(bad) > 5: break
        if len(bad) > 5: break
print(f"Brute-force (definition-level) verification of "
      f"f_d(k*10^m+x)-f_d(x)=k*m*10^(m-1), k<=d-1: checked all x<10^m")
print("  holds exactly:", len(bad)==0, bad[:6])
