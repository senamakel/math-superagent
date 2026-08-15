"""Attack on S-universe-4color: membership test of M(Groetzsch) in the old
combinatorial universe {min deg >= 4, K4-free, K2,3-free}. M(Groetzsch) is
5-chromatic by the Mycielski theorem (Mycielski raises chi by 1), so if it is
in the universe, the universe does not force 4-colourability -> refutation.
Pure integer adjacency; subgraph tests by backtracking (tiny subgraphs)."""
import itertools

def groetzsch():
    N = 11
    adj = [set() for _ in range(N)]
    def idx(kind, i):
        i %= 5
        return {'a': i, 'b': 5 + i, 'c': 10}[kind]
    for i in range(5):
        adj[idx('a', i)].add(idx('a', (i+1) % 5))
        adj[idx('a', (i+1) % 5)].add(idx('a', i))
    for i in range(5):
        for k in ((i-1) % 5, (i+1) % 5):
            adj[idx('b', i)].add(idx('a', k))
            adj[idx('a', k)].add(idx('b', i))
    for i in range(5):
        adj[idx('c')].add(idx('b', i))
        adj[idx('b', i)].add(idx('c'))
    return adj

def mycielski(adj):
    n = len(adj)
    N = 2*n + 1
    nadj = [set() for _ in range(N)]
    for v in range(n):
        for u in adj[v]:
            if u > v:
                nadj[v].add(u); nadj[u].add(v)
    for v in range(n):
        for u in adj[v]:
            nadj[n + v].add(u); nadj[u].add(n + v)
    for v in range(n):
        nadj[2*n].add(n + v); nadj[n + v].add(2*n)
    return nadj

def has_subgraph(adj, sub_edges, sub_n):
    n = len(adj)
    for combo in itertools.combinations(range(n), sub_n):
        for perm in itertools.permutations(combo):
            if all(perm[b] in adj[perm[a]] for (a, b) in sub_edges):
                return tuple(perm)
    return None

def has_K4(adj):
    return has_subgraph(adj, [(i, j) for i in range(4) for j in range(i+1, 4)], 4)

def has_K23(adj):
    edges = [(0,2),(0,3),(0,4),(1,2),(1,3),(1,4)]
    return has_subgraph(adj, edges, 5)

def min_degree(adj):
    return min(len(a) for a in adj)

def has_K3(adj):
    return has_subgraph(adj, [(0,1),(0,2),(1,2)], 3)

M = mycielski(groetzsch())
n = len(M)
print("M(Groetzsch): n=%d" % n)
print("  min degree      =", min_degree(M))
print("  has K3 (tri?)   =", has_K3(M) is not None)
print("  has K4          =", has_K4(M) is not None)
print("  has K2,3        =", has_K23(M) is not None)
print("  -> in old universe {min-deg>=4, K4-free, K2,3-free}? ",
      min_degree(M) >= 4 and has_K4(M) is None and has_K23(M) is None)
print("  5-chromatic? YES by Mycielski theorem (chi rises by 1 from 4-chromatic Groetzsch)")
