from itertools import combinations
# The analyzer's OTHER/unused edge list
moser_edges = [(0,1),(0,2),(0,3),(0,4),(1,2),(1,5),(2,5),(5,6),(3,4),(3,6),(4,6)]
# and the labeled one actually used
labeled = [(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(3,6),(4,5),(4,6),(5,6)]

def k4(es):
    n = max(max(e) for e in es)+1
    adj=[set() for _ in range(n)]
    for a,b in es:
        adj[a].add(b); adj[b].add(a)
    out=[]
    for c in combinations(range(n),4):
        if all(b in adj[a] for a,b in combinations(c,2)):
            out.append(c)
    return out

print("moser_edges K4:", k4(moser_edges), "edges=", len(moser_edges))
print("labeled    K4:", k4(labeled),    "edges=", len(labeled))

# Are they isomorphic (both 7v/11e, chi=4)? Check degrees
from collections import Counter
def degseq(es):
    n=max(max(e) for e in es)+1
    d=[0]*n
    for a,b in es: d[a]+=1; d[b]+=1
    return sorted(d)
print("degseq moser_edges:", degseq(moser_edges))
print("degseq labeled:    ", degseq(labeled))
