# Investigate why CLAIM B (D(N+1)=sum f(C)) appears to FAIL from N=3 onward,
# while the inventor recorded it as "reproduces D exactly".
# Hypothesis: the map (C,p)->child is NOT injective; some children reachable
# from two different (C,p).  Check by explicit collision counting.
from lib.amoeba import children, f_of

E = [(1,0,0),(0,1,0),(0,0,1)]

def fwd(level):
    nxt = set()
    for S in level:
        Sset = set(S)
        for p in Sset:
            p = tuple(p)
            ch = children(p, 3)
            if all(c not in Sset for c in ch):
                nxt.add(frozenset((Sset - {p}) | set(ch)))
    return nxt

for N in range(0, 7):
    level = {frozenset([(0,0,0)])}
    for _ in range(N):
        level = fwd(level)
    childmap = {}
    for C in level:
        Sset = set(C)
        for p in Sset:
            p = tuple(p)
            ch = children(p, 3)
            if all(c not in Sset for c in ch):
                child = frozenset((Sset - {p}) | set(ch))
                childmap.setdefault(child, []).append((C, p))
    sumf = sum(f_of(C) for C in level)
    coll = sum(1 for v in childmap.values() if len(v) > 1)
    print(f'N={N}: D={len(level)} sum_f={sumf} distinct_children={len(childmap)} '
          f'D+1={len(fwd(level))} colliding_children={coll}')
    for child, v in childmap.items():
        if len(v) > 1:
            print('   CHILD', sorted(child))
            for C, p in v:
                print('      from C=', sorted(C), ' p=', p)
