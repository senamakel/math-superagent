from math import gcd

A = [5248, 1312, 2624, 5760, 3936]
B = [640, 1888, 3776, 3776, 5664]
SA = sum(A); SB = sum(B)
SAi = A; SBi = B

def verify(p, q):
    """m=p/q reduced. Find integer s_i,t_i counts OR state impossibility."""
    # s_i/t_i = R_i/m = (A[i]/B[i])/(p/q) = A[i]q / (B[i]p)
    c = []; d = []
    for i in range(5):
        num = A[i]*q; den = B[i]*p
        g = gcd(num,den); c.append(num//g); d.append(den//g)
    print("reduced s/t per product (c_i/d_i):", list(zip(c,d)))
    # need k_i with s_i=k c_i<=A[i], t_i=k d_i<=B[i]
    K = [min(A[i]//c[i], B[i]//d[i]) for i in range(5)]
    print("max k_i:", K)
    # overall: sum k c / SA = (p/q) sum k d / SB  => q*SB*sum c k = p*SA*sum d k
    w = [q*SB*c[i]-p*SA*d[i] for i in range(5)]
    print("w_i:", w)
    return c,d,K,w

# smallest and largest
for p,q in [(1476,1475),(123,59)]:
    print("="*40)
    print(f"m = {p}/{q}")
    c,d,K,w = verify(p,q)
    # try to find a k vector
    pos = [i for i in range(5) if w[i]>0]
    neg = [i for i in range(5) if w[i]<0]
    print("pos:",[(i,w[i]) for i in pos],"neg:",[(i,w[i]) for i in neg])
    # brute small search
    found=[False]
    def rec(idx, cur, ks):
        if found[0]: return
        if idx==5:
            if cur==0:
                found[0]=True
                print("  FOUND k:", ks[:])
            return
        for k in range(1,K[idx]+1):
            ks[idx]=k
            rec(idx+1,cur+k*w[idx],ks)
    rec(0,0,[0]*5)
    if not found[0]: print("  no k found in full search")
