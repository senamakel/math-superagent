def base3(m):
    if m==0: return "0"
    d=[]
    while m>0:
        d.append(m%3); m//=3
    return d  # least significant first

# 1) c1(n) even for n>=1 (digit sum mod 2)
bad=[]
for n in range(1,200):
    s=base3(2**n)
    c1=sum(1 for x in s if x==1)
    c2=sum(1 for x in s if x==2)
    if c1%2!=0:
        bad.append(n)
print("c1 odd for n>=1:", bad[:10], "(empty means all even)")

# 2) |A_k| = 2^(k-1) and survivor residue classes r mod 2*3^(k-1)
def order2(k):
    return 2*3**(k-1)

def digit_free_mod(res, k):
    # low k ternary digits of res avoid 2
    for _ in range(k):
        if res%3==2: return False
        res//=3
    return True

for k in range(1,7):
    period=order2(k)
    survivors=sorted(r for r in range(period) if digit_free_mod(pow(2,r,3**k), k))
    counts=len(survivors)
    print(f"k={k}: |A_k|={counts} (2^(k-1)={2**(k-1)}) survivors={survivors}")
