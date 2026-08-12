from fractions import Fraction
from sympy import divisors, gcd, isprime, factorint

LIMIT = 10**18

def sigma(n):
    return sum(divisors(n))

# Known hemiperfects <= 3e7 (oracle set from this run's brute force)
known = [2,24,4320,4680,26208,8910720,17428320,20427264]

def v2(n):
    c=0
    while n%2==0:
        n//=2; c+=1
    return c

print("=== Verify v2(sigma(u))=a-1 and the exact rational identity on known set ===")
for n in known:
    a=v2(n); u=n//(2**a)
    T=Fraction(sigma(u),u)
    # predicted sigma(u)/u = (2k+1) 2^{a-1}/(2^{a+1}-1), with abundancy r/2, r=2k+1
    r=2*sigma(n)//n  # since sigma(n)/n = r/2, 2sigma(n)/n = r odd
    k=(r-1)//2
    pred=Fraction((2*k+1)*2**(a-1), 2**(a+1)-1)
    ok1 = (v2(sigma(u))==a-1)
    ok2 = (T==pred)
    print(f"n={n}: a={a}, r={r}, v2(sig(u))={v2(sigma(u))} (want {a-1}), id ok={ok2}")

print()
print("=== Bound on a: n=2^a*u >= 2^a*(2^{a+1}-1) because D|u ===")
for a in range(1,40):
    lb=2**a*(2**(a+1)-1)
    feasible = lb <= LIMIT
    if a in (28,29,30,31) or (not feasible):
        print(f"a={a}: min feasible n = {lb:.3e}, feasible<=1e18: {feasible}")

print()
print("=== Reachable (a,k) pairs by denominator magnitude (D|u, u>=D, n>=2^a*D<=1e18) ===")
cnt=0
pairs=[]
for a in range(1,30):
    D=2**(a+1)-1
    for k in range(1,7):
        N=(2*k+1)*2**(a-1)
        g=gcd(N,D)
        num=N//g; den=D//g
        # sigma(u)/u=num/den in lowest terms, den|u, so u>=den, n>=2^a*den
        if 2**a*den <= LIMIT:
            cnt+=1
            pairs.append((a,k))
print("possible (a,k) with magnitude-feasible reduced denominator:", cnt)
print("max a among them:", max(a for a,k in pairs))
print("max a for each k:", {k:max(a for aa,k2 in pairs if k2==k) for k in range(1,7)})

print()
print("=== For 11/2 (k=5) known both have a=11; check a range needed ===")
for n in [17116004505600, 75462255348480000, 6219051710415667200]:
    a=v2(n); u=n//2**a
    print(f"n={n}: a={a}, v2(sig(u))={v2(sigma(u))}, want a-1={a-1}")
