import sys, random
sys.path.insert(0, "/workspace/code")
from lib.digits import f_place_value

# Corrected structural claim:
#   For digit d, 0 <= k <= d-1, and ANY x in [0, 10^10):
#       f(k*10^10 + x, d) - f(x, d)  ==  k*10^10.
# Consequently f(n,d)-n is (k*10^10+... ) invariant, so n=k*10^10+x is a
# solution iff x is a solution with x<10^10.
random.seed(11)
fails=[]; checked=0
for d in range(1,10):
    for k in range(1,d):   # k in 1..d-1 (k=0 is trivially 0)
        for _ in range(20000):
            x = random.randrange(0, 10**10)
            n = k*10**10 + x
            R = f_place_value(n,d) - f_place_value(x,d)
            checked += 1
            if R != k*10**10:
                fails.append((d,k,x,R))
                if len(fails)>4: break
        if len(fails)>4: break
    if len(fails)>4: break
print(f"Corrected residue identity: checked={checked} (20000 random x per (d,k), k=1..d-1)")
print("  holds exactly:", len(fails)==0)
print("  failures:", fails[:6])

# verify the counter-side: for k >= d the residue is NOT k*10^10 (breaks at k=d)
print("\nVerify it breaks at k=d (should differ):")
for d in [1,3,8]:
    x = 1234567890
    R = f_place_value(d*10**10+x, d) - f_place_value(x,d)
    print(f"  d={d} k=d: R={R} vs d*10^10={d*10**10} -> {R!=d*10**10}")
