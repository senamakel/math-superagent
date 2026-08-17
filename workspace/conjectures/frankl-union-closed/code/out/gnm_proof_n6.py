"""Final structural verification of the PROOF constructions at n=6 (d=5):
(1) F_S = 2^[5] U {s|32 : s in S}, S an up-set of B_5 of size 17 (mid-range),
    must be UC with |F|=49 and rare element count = 17 = 49 - 32.
(2) degree-1 construction F = {0} U S U {U|x}, U=[5], S up-set of B_5 of size
    20 (=> |F| = 22, element x count 1).
Uses the explicit interval construction for the up-set sizes.
"""
from lib.uc import decide_union_closed, abundance

d = 5
n = 6
xbit = 1 << d   # 32
full = list(range(1 << d))


def rank_filter_upset(d, s):
    pop = [bin(A).count("1") for A in range(1 << d)]
    if s == 1 << d:
        return set(range(1 << d))
    Sk = {k: sum(1 for p in pop if p >= k) for k in range(d + 2)}
    for k in range(1, d + 2):
        if Sk[k] <= s <= Sk[k - 1]:
            break
    S = {A for A in range(1 << d) if pop[A] >= k}
    cands = [A for A in range(1 << d) if pop[A] == k - 1]
    S |= set(cands[: s - len(S)])
    return S


def is_upset(S):
    return all((A | B) == B and B in S for A in S for B in full if (A | B) == B)


# (1) F_S with |S| = 17
S = rank_filter_upset(d, 17)
assert is_upset(S) and len(S) == 17
F = set(full) | {s | xbit for s in S}
m = len(F)
counts = abundance(F, n)
rare = min(c for c in counts if c > 0)
print("(1) n=6, |S|=17: UC =", decide_union_closed(F),
      "|F| =", m, "(expect 49) rare =", rare, "(expect 17 = m - 32)")

# (2) degree-1 construction, |S| = 20 => size 22, x count 1
S2 = rank_filter_upset(d, 20)
assert is_upset(S2) and len(S2) == 20
U = (1 << d) - 1          # [5]
xFam = {0} | set(S2) | {U | xbit}
m2 = len(xFam)
c2 = abundance(xFam, n)
print("(2) n=6 degree-1: UC =", decide_union_closed(xFam),
      "|F| =", m2, "count of element 6 =", c2[5], "(expect 1)")

# both at once: expected envelope values
print("Envelope predicts g(6,49)=17, g(6,22)=1: "
      "match" if (rare == 17 and c2[5] == 1) else "MISMATCH")