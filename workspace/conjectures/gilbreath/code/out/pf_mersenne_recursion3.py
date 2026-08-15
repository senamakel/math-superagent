#!/usr/bin/env python3
"""Pin down the exact elementwise self-similar recursion A_{k+1} = g(A_k)
for the Mersenne c_r/2 arrays.  Test concrete candidates against the arrays
reproduced by the run's per-residue affine extraction (k=2..7), and if one
fits, verify sum(A_{k+1}) = 3*sum(A_k)+3 (the induction giving sum c_r=3^k-3).
"""
import sys
sys.path.insert(0,'/workspace/code')

A = {
 2: [1,1,1],
 3: [1,3,2,2,1,2,1],
 4: [1,7,4,4,2,4,2,2,1,4,2,2,1,2,1],
 5: [1,15,8,8,4,8,4,4,2,8,4,4,2,4,2,2,1,8,4,4,2,4,2,2,1,4,2,2,1,2,1],
 6: [1,31,16,16,8,16,8,8,4,16,8,8,4,8,4,4,2,16,8,8,4,8,4,4,2,8,4,4,2,4,2,2,1,16,8,8,4,8,4,4,2,8,4,4,2,4,2,2,1,8,4,4,2,4,2,2,1,4,2,2,1,2,1],
 7: [1,63,32,32,16,32,16,16,8,32,16,16,8,16,8,8,4,32,16,16,8,16,8,8,4,16,8,8,4,8,4,4,2,32,16,16,8,16,8,8,4,16,8,8,4,8,4,4,2,16,8,8,4,8,4,4,2,8,4,4,2,4,2,2,1,32,16,16,8,16,8,8,4,16,8,8,4,8,4,4,2,16,8,8,4,8,4,4,2,8,4,4,2,4,2,2,1,16,8,8,4,8,4,4,2,8,4,4,2,4,2,2,1,8,4,4,2,4,2,2,1,4,2,2,1,2,1],
}

def test(transform, label):
    ok=True
    for k in list(A)[:-1]:
        Ak=A[k]; An=A[k+1]; P=len(Ak)
        rec = transform(Ak, P)
        assert len(rec)==2*P+1, (k,len(rec),len(An))
        if rec!=An:
            ok=False
            print(f"{label} MISMATCH k={k}")
            for i,(r,a) in enumerate(zip(rec,An)):
                if r!=a: print("   idx",i,"rec",r,"act",a); break
            break
    print(f"{label}: {'EXACT k=2..7' if ok else 'failed'}")
    return ok

# candidate from data inspection:
#   A_{k+1} = [1] + b1 + b2
#   b2 = Ak with Ak[1] += 1
#   b1[0] = 2*Ak[1]+1 ; b1 = b1[0] + 2*Ak[1:] with Ak[1] term replaced by doubling Ak[2]?
# Let me reconstruct b1,b2 from each k and print to find exact law.
print("=== b1,b2 exact decomposition ===")
for k in list(A)[:-1]:
    Ak=A[k]; An=A[k+1]; P=len(Ak)
    b1=An[1:P+1]; b2=An[P+1:]
    d2 = [2*x for x in Ak[2:]]
    print(f"k={k} P={P}")
    print("  b1      =", b1)
    print("  2*Ak[1:]= ", [2*x for x in Ak[1:]])
    print("  2*Ak[2:]= ", d2)
    # how many trailing b1 entries equal the double of the shifted next?
    # check b1 == [2*Ak[1]+1] + 2*Ak[2:] + [last]?
    cand = [2*Ak[1]+1]+[2*x for x in Ak[2:]]
    print("  cand [2A1+1]+2Ak[2:] len",len(cand))
    # difference with b1
    if len(cand)<=len(b1):
        diff = b1[:len(cand)]==cand
        print("  b1[:len(cand)]==cand?", diff, "; b1 tail extra", b1[len(cand):] if len(b1)>len(cand) else None)
