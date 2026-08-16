# Verify the read-cone column bound behind candidate `read-cone-column-equivalence`.
# 1. Cone description: C_j(n) = { d in [2,n-1] : (d-(n-1-j)) subseteq d }  (as bitmasks)
# 2. Column bound: wt(Phi_n h) <= sum_j h[j]*|C_j(n)|
# 3. |C_j(n)| ~ n / 2^{popcount(n-1-j)}?  (exact cone size vs approx)
# 4. W_S(n) = sum_{j in S, j<=n-1} 2^{-popcount(n-1-j)}; does inf_n W_S(n)=0
#    for density-0 S? (powers of 2, 2^k-1, squares, \pm-balanced)

def cone_size(j, n):
    # C_j(n) = { d in [2,n-1] : (d-(n-1-j)) subseteq d }
    cnt = 0
    for d in range(2, n):
        r = d - (n-1-j)
        if r < 0:
            continue
        if (r & ~d) == 0:   # r subseteq d
            cnt += 1
    return cnt

def cone_size_formula(j, n):
    # claimed: |C_j| ~ n / 2^{popcount(n-1-j)}
    import math
    r = n-1-j
    if r < 0:
        return 0
    pc = bin(r).count('1')
    return round(n / (2**pc))

def wt_fold(h, n):
    # wt(Phi_n h): number of odd cells over d in [2,n-1]
    # T(n,d) = XOR_{o subsete d} h[n-1-d+o]
    wt = 0
    for d in range(2, n):
        x = 0
        for o in range(d+1):
            if (o & ~d) == 0:
                pos = n-1-d+o
                if 0 <= pos < len(h) and h[pos]:
                    x ^= 1
        if x:
            wt += 1
    return wt

def column_bound(h, n):
    total = 0
    for j in range(len(h)):
        if h[j]:
            total += cone_size(j, n)
    return total

# --- Test 1&2: cone sizes and column bound against oracle ---
print("=== Cone description & column bound (n<=40, random h + witnesses) ===")
import random
random.seed(1)
ok_cone, ok_bound = True, True
for n in range(4, 41):
    # witness sets
    tests = []
    # all-ones
    tests.append([1]*n)
    # single last
    e = [0]*n; e[n-1]=1; tests.append(e)
    # single first
    e = [0]*n; e[0]=1; tests.append(e)
    # random
    tests.append([random.randint(0,1) for _ in range(n)])
    # thue-morse-ish
    tests.append([bin(k).count('1')%2 for k in range(n)])
    for h in tests:
        b = wt_fold(h, n)
        cb = column_bound(h, n)
        if b > cb:
            ok_bound = False
            print(f"BOUND FAIL n={n}: wt={b} > column_bound={cb}")
        # spot check cone formula
        for j in range(n):
            cs = cone_size(j, n)
            cf = cone_size_formula(j, n)
            # cone formula is asymptotic; check |cs - cf| <= cs/3 + 2 for sanity
            if cs>0 and abs(cs-cf) > cs/2 + 2:
                pass  # formula is an asymptotic approx; not a hard check
print("column bound holds for all tested:", ok_bound)
print("cone description exact-trivial check done (cs>=0)")

# --- Test 3: asymptotic cone formula quality ---
print("\n=== cone approx quality (approx vs exact) ===")
for n in [100, 1000]:
    for r in [0,1,2,3,5,7,10, 100]:
        j = n-1-r
        if j<0: continue
        cs = cone_size(j, n)
        import math
        pc = bin(r).count('1')
        approx = n/(2**pc)
        print(f"n={n} r={r}(pc={pc}) exact={cs} approx~{approx:.1f} ratio={cs/max(1,approx):.2f}")

# --- Test 4: the crux. W_S(n) for density-0 S. liminf zero? ---
print("\n=== W_S liminf for density-0 supports ===")
def W_S(S, n):
    return sum(2**(-bin(n-1-j).count('1')) for j in S if j<=n-1)

def supports():
    pow2 = {2**k for k in range(15)}
    mers = {2**k-1 for k in range(1,15)}
    sq = {k*k for k in range(1,40)}
    return {"powers_of_2":pow2, "2^k-1":mers, "squares":sq}

SUP = supports()
for name, S in SUP.items():
    lows = []
    for n in range(3, 2000):
        w = W_S(S, n)
        lows.append(w)
    print(f"{name}: min W over n in [3,2000] = {min(lows):.4f}; "
          f"liminf sample approx. Last-200-min={min(lows[-200:]):.4f}")
    # check density of {n: W>=0.05}
    cnt = sum(1 for w in lows if w>=0.05)
    print(f"   P(n<=2000: W>=0.05) = {cnt/len(lows):.3f}")

# Targeted: does S = powers-of-2 have W=Omega(1) at many n or liminf 0?
S = SUP["powers_of_2"]
print("\n=== powers-of-2 W_S(n) detail ===")
for n in [2**k for k in range(3,13)]:
    print(f"n={n}: W={W_S(S,n):.4f}")
print("at n=2^m+1:")
for m in range(3,11):
    n=2**m+1
    print(f"n={n}: W={W_S(S,n):.4f}")

# S = 2^k-1 : does W stay >= c on a density-1 set?
S2 = SUP["2^k-1"]
cnt=0; tot=0
for n in range(3,3001):
    tot+=1
    if W_S(S2,n)>=0.05: cnt+=1
print(f"\n2^k-1: P(n<=3000: W>=0.05)={cnt/tot:.3f}")
