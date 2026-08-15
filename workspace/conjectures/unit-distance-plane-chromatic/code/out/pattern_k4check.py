# Resolve: does the 7-vertex Moser spindle contain a K4?
# The certified sharp-nbhd-local lemma says every unit-distance graph is K4-free,
# so "True" in analyze_kernel_chrom.captured.txt must be an analyzer bug.
moser = [(0,1),(0,2),(0,4),(0,5),(1,2),(1,3),(2,3),(3,6),(4,5),(4,6),(5,6)]
n = 7
adj = [set() for _ in range(n)]
for a,b in moser:
    adj[a].add(b); adj[b].add(a)
print("edges:", len(moser))
print("degrees:", [len(adj[v]) for v in range(n)])

# brute-force K4 check
k4s = []
from itertools import combinations
for c in combinations(range(n), 4):
    if all(b in adj[a] for a,b in combinations(c,2)):
        k4s.append(c)
print("K4 subgraphs:", k4s)
assert not k4s, "Moser should be K4-free"
print("confirmed: Moser spindle contains NO K4 (matches certified sharp-nbhd-local)")
