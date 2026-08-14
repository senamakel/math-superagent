def f_naive(n, d):
    return sum(str(i).count(str(d)) for i in range(0, n+1))

# Definition-level check of the residue identity, small m, sampled x.
# (full x-range for m<=2; 5000 random x for m=3,4)
import random
random.seed(7)
bad = []
checked = 0
for m in range(1, 5):
    for d in range(1, 10):
        for k in range(0, d):
            if m <= 2:
                xs = range(10**m)
            else:
                xs = [random.randrange(0, 10**m) for _ in range(2000)]
            for x in xs:
                n = k*10**m + x
                lhs = f_naive(n, d) - f_naive(x, d)
                pred = k * m * 10**(m-1)
                checked += 1
                if lhs != pred:
                    bad.append((m,d,k,x,lhs,pred))
                    if len(bad) > 5: break
            if len(bad) > 5: break
        if len(bad) > 5: break
    if len(bad) > 5: break
print(f"definition-level (string-count) check of f_d(k*10^m+x)-f_d(x)=k*m*10^(m-1), k<=d-1:")
print(f"  checked={checked} holds exactly: {len(bad)==0}  failures: {bad[:6]}")