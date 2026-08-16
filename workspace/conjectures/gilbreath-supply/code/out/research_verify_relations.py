"""Verify the refuter's counterexamples against the literal fold cell definition.

Fold cell (problem.md facts 1-2):
    T(n,d) = XOR_{o subset of d} h[n-1-d+o],   d = 2..n-1

Check:
A) abel-boundary-recurrence relation:  T(n,d) == T(n-1,d) XOR T(n-1,d-1)
B) substitution-incidence rules:
   (i) T(2n,2d) = T(n,d)
   (ii) T(2n,2d+1) = 0
   (iii) T(2n+1,2d) = T(n,d)
   (iv) T(2n+1,2d+1) = T(n,d)
"""
def submasks(d):
    out = []
    s = d
    while True:
        out.append(s)
        if s == 0:
            break
        s = (s - 1) & d
    return out

def T(n, d, h):
    """fold cell; requires d >= 2 and n-1-d >= 0"""
    acc = 0
    for o in submasks(d):
        acc ^= h[n - 1 - d + o]
    return acc

def check_abel(n_range=8, L=8):
    fails = []
    for n in range(3, n_range + 1):
        for d in range(2, n - 1):   # need T(n-1,d),T(n-1,d-1) defined: d in [2,n-1], n-1-1-d+... 
            # T(n-1,d): need n-1 >= d+1 i.e. d <= n-2; T(n-1,d-1): need d >= 3
            if d < 3 or d > n - 2:
                continue
            for bits in range(1 << L):
                h = [(bits >> i) & 1 for i in range(L)]
                lhs = T(n, d, h)
                rhs = T(n - 1, d, h) ^ T(n - 1, d - 1, h)
                if lhs != rhs:
                    fails.append((n, d, h, lhs, rhs))
                    if len(fails) >= 3:
                        return fails, True
    return fails, bool(fails)

def check_subs(L=8):
    fails = []
    # rule (i) T(2n,2d)=T(n,d): need 2d in [2,2n-1] (d>=1), n-1-... 
    for n in range(2, 6):
        for d in range(1, n):
            # T(2n,2d): index 2n-1-2d+o, need >=0; T(n,d) defined (d>=1, d<=n-1)
            if 2 * n - 1 - 2 * d < 0:
                continue
            for bits in range(1 << L):
                h = [(bits >> i) & 1 for i in range(L)]
                if T(2 * n, 2 * d, h) != T(n, d, h):
                    fails.append(("i", n, d, h))
                    return fails, True
    # rule (ii) T(2n,2d+1)=0: 2d+1 in [2,2n-1]
    for n in range(2, 6):
        for d in range(1, n):
            dd = 2 * d + 1
            if dd < 2 or dd > 2 * n - 1:
                continue
            if 2 * n - 1 - dd < 0:
                continue
            for bits in range(1 << L):
                h = [(bits >> i) & 1 for i in range(L)]
                if T(2 * n, dd, h) != 0:
                    fails.append(("ii", n, d, h))
                    return fails, True
    return fails, bool(fails)

fa, ag = check_abel()
print("ABEL relation fails:", ag, fa[:1])
fs, sg = check_subs()
print("SUBS rules fail:", sg, fs[:1])

# Print the specific documented counterexamples to double-check
h = [0, 0, 0, 1]
print("A: T(4,2)=", T(4, 2, h), " T(3,2)=", T(3, 2, h), " T(3,1)=", T(3, 1, h),
      " RHS=", T(3, 2, h) ^ T(3, 1, h))
print("B(i): T(4,2)=", T(4, 2, h), " T(2,1)=", T(2, 1, h))
# substitution rules with the actual h for the (4,2) case: which n,d gives T(2n,2d)=T(4,2)? n=2,d=1
n, d = 2, 1
print("B(i) T(2n,2d)=", T(4, 2, h), "T(n,d)=", T(2, 1, h))
# rule (ii): n=1,d=0 -> T(2,1) should be 0; h=(1,0,0): T(2,1)=h[0]^h[1]=1
n, d = 1, 0
print("B(ii) T(2,1)=", T(2, 1, [1, 0, 0]), " claimed 0")
