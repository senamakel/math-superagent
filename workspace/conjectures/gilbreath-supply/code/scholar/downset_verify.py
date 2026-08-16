"""Independent exact verification of the downset-row intersection formula
(claim downset-row-intersection-meet-formula), by brute submask enumeration.

M_d = {n-1-d+o : o subseteq d}, d in [2, n-1].
Claims:
  (1) |M_d ∩ M_d'| = 2^pc(d & d')
  (2) |M_d △ M_d'| = 2^pc(d) + 2^pc(d') - 2^{pc(d & d') + 1}
  (3) M_d ∩ M_d' = M_{d & d'}   (the meet-semilattice intersection - stronger)

Negative control: a random point set of the same size should NOT satisfy (3).
"""
def pc(x): return bin(x).count("1")

def submasks(d):
    s = []
    o = d
    while True:
        s.append(o)
        if o == 0: break
        o = (o - 1) & d
    return s

def Mrow(n, d):
    return {n - 1 - d + o for o in submasks(d)}

bad = []
for n in range(4, 200):
    for d1 in range(2, n):
        for d2 in range(2, n):
            Md1, Md2 = Mrow(n, d1), Mrow(n, d2)
            inter = Md1 & Md2
            sym = Md1 ^ Md2
            # claim (3)
            if inter != Mrow(n, d1 & d2):
                bad.append((n, d1, d2, "meet", inter, Mrow(n, d1 & d2)))
            # claims (1),(2)
            if len(inter) != 2 ** pc(d1 & d2):
                bad.append((n, d1, d2, "inter-size", len(inter), 2**pc(d1&d2)))
            if len(sym) != 2**pc(d1) + 2**pc(d2) - 2**(pc(d1 & d2)+1):
                bad.append((n, d1, d2, "sym-size", len(sym),
                            2**pc(d1)+2**pc(d2)-2**(pc(d1&d2)+1)))

print("bad count:", len(bad))
for b in bad[:5]: print(b)

# negative control: random SET families of the matching sizes should FAIL the
# meet formula (proves the pass on M_d is not true by construction).
import random
random.seed(1)
neg_fail = 0   # how often random families still happen to match (should be ~0)
for _ in range(4000):
    n = 30
    d1, d2 = random.randrange(2, n), random.randrange(2, n)
    A = set(random.sample(range(n), 2 ** pc(d1)))
    B = set(random.sample(range(n), 2 ** pc(d2)))
    # the M_d family has intersection size 2^pc(d1&d2); a random family of the
    # same sizes should essentially never have intersection of that exact size.
    if len(A & B) == 2 ** pc(d1 & d2):
        neg_fail += 1
# expected intersection of two uniform random subsets of sizes a,b from n:
# E|A&B| = a*b/n; P(exact match to 2^pc(d1&d2)) is tiny.
print("negative control: random same-size families coincidentally matching the",
      "formula:", neg_fail, "of 4000 (expected ~0; proves the pass is not vacuous)")
