import sys, random
sys.path.insert(0, "/workspace/code")
from lib.digits import f_place_value

# General residue identity (derived):
#   For k <= d-1, 0<=x<10^m:  f_d(k*10^m + x) - f_d(x)  ==  k * m * 10^(m-1).
# This equals k*10^m  <=>  m*10^(m-1) == 10^m  <=>  m == 10.
# Test the general formula for several m.
random.seed(21)
fails=[]; checked=0
for m in range(1, 13):
    for d in range(1,10):
        for k in range(1, d):  # <= d-1
            for _ in range(3000):
                x = random.randrange(0, 10**m)
                n = k*10**m + x
                R = f_place_value(n,d) - f_place_value(x,d)
                pred = k * m * 10**(m-1)
                checked += 1
                if R != pred:
                    fails.append((m,d,k,x,R,pred))
                    if len(fails)>4: break
            if len(fails)>4: break
        if len(fails)>4: break
    if len(fails)>4: break
print(f"General residue identity f_d(k*10^m+x)-f_d(x)=k*m*10^(m-1), k<=d-1: checked={checked}")
print("  holds exactly:", len(fails)==0, " failures:", fails[:6])

# The special m=10 case:
print("\nCheck k*m*10^(m-1) == k*10^m when m=10:", 10*10**9 == 10**10)
