# Reproduce the analyzer's K4 check verbatim to find why it printed True.
moser = [(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(3,6),(4,5),(4,6),(5,6)]
n = 7
adjsets = [set() for _ in range(n)]
for a,b in moser:
    adjsets[a].add(b); adjsets[b].add(a)
k4=False
for a in range(n):
    for b in range(a+1,n):
        if b not in adjsets[a]:
            continue
        inter = adjsets[a]&adjsets[b]
        if len(inter)>=2:
            for c in inter:
                for d in inter:
                    if c<d and d in adjsets[c]:
                        k4=True
                        print("K4 trigger: a,b,c,d =",a,b,c,d)
print("analyzer-style K4 check result:", k4)
# debug each adjacent pair's common-neighbour set size
for a in range(n):
    for b in range(a+1,n):
        if b in adjsets[a]:
            inter = adjsets[a]&adjsets[b]
            if len(inter)>=2:
                print(f"  pair ({a},{b}) common nbrs {inter}, common-nbr adjacency check:")
                for c in inter:
                    for d in inter:
                        if c<d:
                            print(f"     {c}-{d} adjacent? {d in adjsets[c]}")
