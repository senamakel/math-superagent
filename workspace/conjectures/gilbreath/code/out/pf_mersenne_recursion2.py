#!/usr/bin/env python3
"""Find the exact elementwise self-similar recursion A_{k+1} = f(A_k) for the
Mersenne c_r/2 arrays (length 2^k-1), tail-1 word.  Exact check against arrays
reproduced by the run's own per-residue affine extraction (from
mersenne_array_structure.py output, verified k=2..8).

Goal: a recursion that (a) reproduces every A_k exactly and (b) makes
sum(A_k) = (3^k - 3)/2 provable by induction.  This lifts the checked
conjecture sum c_r = 3^k-3 toward an actual proof.
"""
A = {
 2: [1,1,1],
 3: [1,3,2,2,1,2,1],
 4: [1,7,4,4,2,4,2,2,1,4,2,2,1,2,1],
 5: [1,15,8,8,4,8,4,4,2,8,4,4,2,4,2,2,1,8,4,4,2,4,2,2,1,4,2,2,1,2,1],
 6: [1,31,16,16,8,16,8,8,4,16,8,8,4,8,4,4,2,16,8,8,4,8,4,4,2,8,4,4,2,4,2,2,1,16,8,8,4,8,4,4,2,8,4,4,2,4,2,2,1,8,4,4,2,4,2,2,1,4,2,2,1,2,1],
 7: [1,63,32,32,16,32,16,16,8,32,16,16,8,16,8,8,4,32,16,16,8,16,8,8,4,16,8,8,4,8,4,4,2,32,16,16,8,16,8,8,4,16,8,8,4,8,4,4,2,16,8,8,4,8,4,4,2,8,4,4,2,4,2,2,1,32,16,16,8,16,8,8,4,16,8,8,4,8,4,4,2,16,8,8,4,8,4,4,2,8,4,4,2,4,2,2,1,16,8,8,4,8,4,4,2,8,4,4,2,4,2,2,1,8,4,4,2,4,2,2,1,4,2,2,1,2,1],
}

def check_recursion(block1_transform, block2_transform, label):
    for k in list(A)[:-1]:
        Ak = A[k]
        P = len(Ak)  # 2^k - 1
        An = A[k+1]
        assert len(An) == 2*P + 1, (k, len(An))
        # reconstruction
        b1 = block1_transform(Ak, P)
        b2 = block2_transform(Ak, P)
        rec = [1] + b1 + b2
        if rec != An:
            print(f"{label}: MISMATCH at k={k}")
            for i,(r,a) in enumerate(zip(rec,An)):
                if r!=a:
                    print(f"   index {i}: rec={r} actual={a}")
                    break
            return False
    print(f"{label}: EXACT for k=2..{max(A)}")
    return True

# candidate 1: b1 = [2*Ak[1]+1] + 2*Ak[2:]; b2 = Ak with Ak[1]+=1
def b1c(Ak,P):
    return [2*Ak[1]+1] + [2*a for a in Ak[2:]]
def b2c(Ak,P):
    b = list(Ak); b[1]+=1; return b

ok = check_recursion(b1c,b2c,"candidate1")
print("result1", ok)

# Instead of guessing, derive b1,b2 from the data for each k and look at pattern
print("\nExact b1 (rec - [1] and second-half) derivations:")
for k in list(A)[:-1]:
    Ak=A[k]; An=A[k+1]; P=len(Ak)
    b1=An[1:P+1]; b2=An[P+1:]
    print(f"k={k}: ")
    print("  b1:", b1)
    print("  2*Ak[1:]:", [2*a for a in Ak[1:]])
    print("  b2:", b2)
    print("  Ak:", Ak)
