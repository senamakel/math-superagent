# Hand verification of the structural reduction for the powers-of-two string.
# Claim: for h[j]=1 iff j is a power of two, at n=2^m:
#   T(n,d)=1  iff  k = n-1-d  is 0 (m odd) or a power of two.
# So nu2(n) = #{k in [0,n-3] : k is a power of two} + (m mod 2) = O(log n).
#
# Independent numeric check via the literal submask-XOR oracle (no reliance on
# the reduction): directly verify the powers-of-two string's fold weight is
# small (O(log n)), NOT linear.
def powers_of_two_h(N):
    h = [0]*N
    p = 1
    while p < N:
        h[p] = 1
        p <<= 1
    return h

def nu2_direct(n, h):
    # literal definition: XOR over submasks o of d of h[n-1-d+o], d in [2,n-1]
    c = 0
    for d in range(2, n):
        x = 0
        for o in range(d+1):
            if (o & d) == o:
                x ^= h[n-1-d+o]
        c += x
    return c

print("n      ones(h)   nu2(direct)   nu2/n")
for n in [8, 12, 16, 32, 64, 128, 256, 512]:
    h = powers_of_two_h(n)
    v = nu2_direct(n, h)
    print(f"{n:4d} {sum(h):9d} {v:10d}   {v/n:8.4f}")

# contrast: linear weight would be nu2/n -> c>0. Check the ratio decays.
