"""Faithfully replicate n3_grow_radius's growth to the stable fixpoint and
check the exact identity L_in == V_patch - 4 on every survivor."""
import itertools, sys
sys.path.insert(0, '/workspace/code')
sys.path.insert(0, '/workspace/code/out')

# copy minimal pieces from n3_grow_radius (no imports of that -- it runs main())
DEGREE = 14
SEED = ['a', 'b', 'c', 'd', 'e', 'f']
EDGES = {('a', 'b'), ('b', 'c'), ('c', 'a'),
         ('d', 'e'), ('e', 'f'), ('f', 'd'),
         ('a', 'd'), ('b', 'e')}
NONEDGES = {('c', 'f'), ('a', 'e'), ('b', 'f'), ('c', 'd'),
            ('a', 'f'), ('b', 'd'), ('c', 'e')}
BIT_CAP = 1 << 20

def _fresh_label(used):
    i = 0
    while 'W%02d' % i in used:
        i += 1
    return 'W%02d' % i

def seed():
    verts = list(SEED); A = {}
    for u in verts: A[(u,u)] = 0
    for (u,v) in EDGES: A[(u,v)] = A[(v,u)] = 1
    for (u,v) in NONEDGES: A[(u,v)] = A[(v,u)] = 0
    return verts, A

def undecided_pairs(verts, A):
    return [(verts[i], verts[j]) for i in range(len(verts))
            for j in range(i+1, len(verts)) if (verts[i],verts[j]) not in A]

def add_witness(verts, A, i, j):
    w = _fresh_label(set(verts)); nverts = list(verts)+[w]; nA = dict(A)
    nA[(w,w)] = 0; nA[(w,i)]=nA[(i,w)]=1; nA[(w,j)]=nA[(j,w)]=1
    return nverts, nA

def adj(A): 
    return lambda u,w: A.get((u,w),0)

def upper_ok(verts, A):
    a = adj(A)
    for u,w in itertools.combinations(verts,2):
        common=[x for x in verts if x!=u and x!=w and a(u,x) and a(w,x)]
        limit=1 if a(u,w) else 2
        if len(common)>limit: return False
    for v in verts:
        nbrs=[u for u in verts if u!=v and a(v,u)]
        if len(nbrs)>DEGREE: return False
        for u in nbrs:
            paired=[w for w in nbrs if w!=u and a(u,w)]
            if len(paired)>1: return False
    return True

def closure_rule3(verts, A):
    nverts, nA = list(verts), dict(A)
    while True:
        if not upper_ok(nverts, nA): return nverts, nA, 'excess'
        grew=False
        a=adj(nA)
        for i,j in itertools.combinations(nverts,2):
            if not nA.get((i,j),0): continue
            common=[x for x in nverts if x!=i and x!=j and a(i,x) and a(j,x)]
            if len(common)==0:
                nverts,nA=add_witness(nverts,nA,i,j); grew=True; break
        if not grew: return nverts, nA, 'ok'

def assignments(verts, A):
    free=undecided_pairs(verts,A); lim=1<<len(free)
    if lim>BIT_CAP: return None
    out=[]
    for bits in range(lim):
        nA=dict(A)
        for k,(u,w) in enumerate(free): nA[(u,w)]=nA[(w,u)]=(bits>>k)&1
        out.append((bits,nA))
    return out

def patch_cliques(verts, A):
    a=adj(A); out=[]
    for t in itertools.combinations(verts,3):
        if a(t[0],t[1]) and a(t[0],t[2]) and a(t[1],t[2]): out.append(frozenset(t))
    return out

def forced_ledger(verts, A):
    cliques=patch_cliques(verts,A); L_in=len(cliques)
    tris={v:0 for v in verts}
    for c in cliques:
        for v in c: tris[v]+=1
    # tri_through_v counts patch 3-cliques through v; that is forced lines
    return len(verts), L_in, max(tris.values())

# ---- replicate growth to fixpoint ----
verts, A = seed()
v1, A1, res = closure_rule3(verts, A)
r1_free = len(undecided_pairs(v1, A1))
asg1 = assignments(v1, A1)
r1=[]; seen1=set()
for bits,aA in asg1:
    if upper_ok(v1,aA):
        canon=tuple(sorted((u,w,aA.get((u,w))) for u,w in itertools.combinations(v1,2)))
        if canon not in seen1:
            seen1.add(canon); r1.append((bits,aA))
print("radius-1 survivors:", len(r1))

frontier=[(v1,aA) for (_,aA) in r1]
rad=1
while True:
    rad+=1
    nf=[]
    grew_any=False
    for i,(vv,aA) in enumerate(frontier):
        nv,nA,res=closure_rule3(vv,aA)
        if res=='excess': continue
        grew_any = grew_any or (len(nv)>len(vv))
        nfree=len(undecided_pairs(nv,nA))
        asg=assignments(nv,nA)
        for _,a2 in asg:
            if upper_ok(nv,a2): nf.append((nv,a2))
    if not nf:
        print("radius %d: ZERO survivors"%rad); break
    if not grew_any:
        print("radius %d: stable fixpoint, %d survivors"%(rad,len(nf)))
        break
    frontier=nf

# now check identity on all fixpoint survivors
print("checking L_in == V-4 on %d fixpoint survivors..."%len(nf))
viol=0
seen=set()
for (vv,aA) in nf:
    V,L,maxln=forced_ledger(vv,aA)
    canon=tuple(sorted((u,w,aA.get((u,w))) for u,w in itertools.combinations(vv,2)))
    if canon in seen: continue
    seen.add(canon)
    ok = (L==V-4)
    if not ok:
        viol+=1
        print("  VIOLATION V=%d L_in=%d (V-4=%d)"%(V,L,V-4))
print("distinct fixpoint survivors (dedup):", len(seen))
print("violations of L_in==V-4:", viol)
print("V_values:", sorted(set(len(vv) for vv,_ in nf)))
