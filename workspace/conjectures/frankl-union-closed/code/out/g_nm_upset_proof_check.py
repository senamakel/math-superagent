"""Verify the PROOF construction of g(n,m) tightness at n=5.

F_S = 2^[n-1]  U  { s|16 : s in S },  S an up-set (filter) of B_4.

Cascade conditions: R2 = S up-set of (full, |)  [TRUE by choice];
R1 = full is union-closed [TRUE]; cross A in R1, B in R2 => A|B in R2
[a|b ⊇ b in up-set S => in S]. So F_S IS union-closed.
|F_S| = 2^{n-1} + |S|;  element n appears exactly in the |S| lifted sets, so
rare(F_S) = |S| (since |S| <= 2^{n-1} <= other counts = 16 + ...).

We test this for several up-sets S (constructed explicitly), including sizes
that span the whole range 1..16.
"""
from lib.uc import decide_union_closed, abundance

n = 5
nminus = 4
xbit = 1 << (n - 1)   # 16
full = list(range(1 << nminus))  # 2^[4]


def is_up_set(S):
    return all((t | s) == t and t in S for s in S for t in full if (t | s) == t)


def build(S):
    F = set(full) | {s | xbit for s in S}
    return F


def check(S, label):
    ok_up = is_up_set(S)
    F = build(S)
    uc = decide_union_closed(F)
    counts = abundance(F, n)
    rare = min(c for c in counts if c > 0)
    m = len(F)
    print(f"S size {len(S):2d} ({label}): up-set={ok_up}, UC={uc}, "
          f"|F|={m}, rare={rare}, rare==|S|={rare==len(S)}, "
          f"m==16+|S|={m==16+len(S)}")
    return uc and ok_up and rare == len(S) and m == 16 + len(S)


allok = True
# principal filters at each rank of B_4 (sizes 16, 8, 4, 2, 1):
for k in range(5):
    a = sum(1 << i for i in range(k))     # subset {0..k-1} of size k
    S = {t for t in full if (t | a) == t}  # supersets of a
    allok &= check(S, f"principal filter at rank {k}")

# explicitly constructed up-sets of intermediate sizes
# size 12: rank>=3 (5 sets) + all rank-2 sets containing bit 0?  simpler:
#   {t : t has bit0 and |t|>=2} U {t : |t|>=3}...
S = {t for t in full if (bin(t).count("1") >= 3)}  # size 5 (ranks 3,4)
S |= {t for t in full if (bin(t).count("1") == 2 and (t & 1))}  # 3 more: {0,1},{0,2},{0,3}
allok &= check(S, "size-8 up-set (rank>=3 + rank2 with bit0)")
#   S of size 12: all of rank >= 2 minus one element, plus fixes
S = {t for t in full if (bin(t).count("1") >= 2)}
S.discard(0b1100)  # remove {3,4}; its supersets 1101,1110,1111 stay
#   but {2,3,4} = 0b1110 is a superset of removed 0b1100?? supersets of 1100:
#   1100,1101,1110,1111 - all in S (rank>=2). Removing 1100 only: S up-set?
S |= {0b1100}     # restore (see note above - it's minimal)
#   build size 12 differently: rank>=2 has 11 elements; add rank-1 elements
#   {1} requires ALL its supersets - that's 8 more. Instead:
S = {t for t in full if (bin(t).count("1") >= 2)}
# rank>=2 alone = 11; add 0111 (a rank-3) -> 12? 0111 already in rank>=2.
S2 = {t for t in full if (bin(t).count("1") >= 2)}
# to get exactly 12 add one more set whose all supersets are already in:
# add 0100 -> supersets: 0100,0101,0110,0111,1100,1101,1110,1111, all rank>=2
# except 0100 itself. So S2 | {0100} is an up-set of size 12.
S2 |= {0b0100}
allok &= check(S2, "size-12 up-set")
# size 6: rank>=3 (5) + {0110}: supersets of 0110: 0111,1110,1111 in rank>=3
S3 = {t for t in full if (bin(t).count("1") >= 3)} | {0b0110}
allok &= check(S3, "size-6 up-set")
# size 3: {1111,1110,1101}: check
S4 = {0b1111, 0b1110, 0b1101}
allok &= check(S4, "size-3 up-set")
# size 7, 9, 10, 11, 13, 14, 15 via complements of down-sets (up-set = full\ideal):
#  ranks: rank0=1, rank1=4, rank2=6, rank3=4, rank4=1.
#  size 15 = rank>=1 (15 sets): verified pattern.
S5 = {t for t in full if (bin(t).count("1") >= 1)}
allok &= check(S5, "size-15 up-set")
S6 = {t for t in full if (bin(t).count("1") == 4)}  # {1111} size 1
allok &= check(S6, "size-1 up-set")

print("ALL up-set constructions correct:", allok)

# also compute the set of ALL up-set sizes of B_4 exhaustively:
from itertools import combinations
upsets = set()
def gen_upsets():
    result = set()
    for mask in range(1 << len(full)):   # 2^16 up-set brute force is too big
        pass
    return result
# use the cascade's upsets_of on the full cube instead:
# (that DFS enumerates up-sets of a poset; B_4 has many but manageable)
def upsets_of(F):
    F = list(F)
    results = set()
    def dfs(present):
        if present in results:
            return
        results.add(present)
        ps = set(present)
        for x in present:
            removable = True
            for y in present:
                if y != x and (y | x) == x:
                    removable = False
                    break
            if removable:
                dfs(frozenset(ps - {x}))
    dfs(frozenset(F))
    return results
sizes = sorted(len(u) for u in upsets_of(full))
print("ALL up-set sizes of B_4:", sizes)
print("All sizes 1..16 present:", sorted(set(sizes)) == list(range(1, 17)))