"""Exact-int check: Thue-Morse h[j]=popcount(j) mod 2 over F2,
subset-zeta transform z[d]=XOR_{j subseteq d} h[j], and the integer
identity sum_{j subseteq d} popcount(j) = popcount(d)*2^(popcount(d)-1).
"""
N = 512

def is_power_of_two(d):
    return d >= 1 and (d & (d - 1)) == 0

h = [(bin(j).count('1') % 2) for j in range(N + 1)]

# subset-zeta over F2: z[d] = XOR of h[j] for j submask of d
z = [0] * (N + 1)
for m in range(1, N + 1):
    # funny: also for standard zeta d=0 gives single submask {0}
    acc = h[0]
    s = m
    sub = s
    # enumerate submasks of m
    acc ^= 0  # placeholder
# recompute cleanly
z = []
for d in range(N + 1):
    acc = 0
    j = d
    while True:
        acc ^= h[j]
        if j == 0:
            break
        j = (j - 1) & d
    z.append(acc)

nonzero = [d for d in range(N + 1) if z[d] == 1]
# expected: powers of two 1,2,4,...,256 (<=N); also d=0? z[0]=h[0]=0.
expected = [1 << k for k in range((N).bit_length()) if (1 << k) <= N]
expected = [d for d in expected if d >= 1]

z_correct = (nonzero == expected)
count_ones = len(nonzero)
expected_count = (N).bit_length() - 1  # powers 2^0..2^8 -> 9 for N=512? 2^8=256<=512, 2^9=512<=512
# careful: powers of two <= 512 are 1..512 = 2^0..2^9 -> 10 values
expected_count = 10 if N == 512 else expected_count
count_correct = (count_ones == expected_count)

# integer identity for d up to N
id_ok = True
bad_d = []
for d in range(N + 1):
    s = 0
    j = d
    while True:
        s += bin(j).count('1')
        if j == 0:
            break
        j = (j - 1) & d
    pc = bin(d).count('1')
    rhs = pc * (1 << (pc - 1)) if pc > 0 else 0
    if s != rhs:
        id_ok = False
        bad_d.append(d)

print("N =", N)
print("h[0..31] =", h[:32])
print("z nonzero positions (actual):", nonzero)
print("expected nonzero (powers of 2 <= N):", expected)
print("Z[d]==1 iff power of 2 :", "PASS" if z_correct else "FAIL")
print("count of d with z[d]=1 =", count_ones, "| floor(log2(N))+1 =", expected_count,
      "->", "PASS" if count_correct else "FAIL")
print("integer identity sum_{j subseteq d} popcount(j) = pc(d)*2^(pc(d)-1):",
      "PASS" if id_ok else f"FAIL at {bad_d[:10]} ...")
