def fold_weight(n, h):
    """wt(Phi_n h) = #{d in [2,n-1] : T(n,d)=1}, T(n,d)=XOR over bitwise
    submasks o of d of h[n-1-d+o].  Exact."""
    ones = 0
    for d in range(2, n):
        x = 0
        for o in range(d + 1):
            if (o & d) == o:
                x ^= h[n - 1 - d + o]
        ones += x
    return ones

n = 40
print("n=40: wt(Phi_n e_j) per single-1 column j (m = distance from last index n-1):")
for j in range(n):
    m = n - 1 - j
    h = [0] * n
    h[j] = 1
    w = fold_weight(n, h)
    print("  j=%3d m=%2d wt=%3d ratio=%.3f" % (j, m, w, 1.0 * w / n))
