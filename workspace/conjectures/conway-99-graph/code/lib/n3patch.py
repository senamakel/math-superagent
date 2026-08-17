"""n3patch.py -- the n3 seed patch and its sound local-growth machinery.

The n3 seed is a 2-edge-joined disjoint triangle pair: T1={a,b,c}, T2={d,e,f}
are disjoint triangles, joined by EXACTLY two cross edges a-d and b-e with the
other seven cross pairs non-adjacent.  This is the local configuration whose
existence Makhnev's Thm 2 leaves open (n3 >= 1), and the k=14-specific step the
order-6 identities cannot see.

This module is the single reusable home for:
  * seed() / EDGES / NONEDGES  -- the radius-0 seed (6 vertices, all 15 pairs
    decided).
  * upper_ok()                -- the SOUND upper-bound criterion over a
    materialised patch: an ADJACENT pair may have <=1 common neighbour in the
    patch, a NON-ADJACENT pair <=2; locally-7K2 (each N(v) a partial
    matching); degree <= 14.  ONLY excesses are contradictions -- deficits are
    satisfiable by the ~90 un-materialised outside vertices, so they are never
    contradictions.  This is exactly what arc-consistency may soundly conclude.
  * closure_rule3()           -- grow a patch to a lambda-witness fixpoint:
    every ADJACENT pair with 0 interior common neighbours gets one fresh
    materialised witness vertex adjacent to both (distinct witnesses, the
    conservative reading).  This is the ONLY thing that grows the patch; mu
    deficits are reported, never materialised.
  * assignments()/undecided_pairs() -- complete enumeration of the still-
    undecided interior pairs of a patch.
  * patch_cliques / forced_ledger -- exact forced-line / incidence ledger of a
    fully-decided patch against the global budget (99 points, 7 lines each,
    693 incidences, 231 lines).

Correctness: radius 1 MUST reproduce the established result (8 vertices, 2
satisfying assignments) and the growth reaches a stable fixpoint with 19
fully-decided survivors at radius 6 (all interior pairs decided, 0 free bits),
matched by code/out/n3_grow_radius.captured.txt.  See code/out/n3_global_ledger
for the ledger that consumes this.

This is the THIRD place the seed/growth functions would otherwise appear (they
were copied in n3_seed_consistency_ub.py and n3_grow_radius.py); moving the
definition here is the fix that keeps the copies from drifting.
"""
import itertools

DEGREE = 14
SEED = ['a', 'b', 'c', 'd', 'e', 'f']
EDGES = {('a', 'b'), ('b', 'c'), ('c', 'a'),
         ('d', 'e'), ('e', 'f'), ('f', 'd'),
         ('a', 'd'), ('b', 'e')}
NONEDGES = {('c', 'f'), ('a', 'e'), ('b', 'f'), ('c', 'd'),
            ('a', 'f'), ('b', 'd'), ('c', 'e')}

# ---- global budget of a putative srg(99,14,1,2) as partial STS ----
V = 99
K = 14
LAM = 1
MU = 2
LINES_PER_POINT = 7
N_LINES = 231          # 99*7/3
N_INC = 693            # 99*7


def _fresh_label(used):
    i = 0
    while 'W%02d' % i in used:
        i += 1
    return 'W%02d' % i


def seed():
    """Radius-0 seed: the 6 named vertices, all 15 pairs decided.
    Returns (verts, A) with A a dict keyed by ordered pair -> {0,1}."""
    verts = list(SEED)
    A = {}
    for u in verts:
        A[(u, u)] = 0
    for (u, v) in EDGES:
        A[(u, v)] = A[(v, u)] = 1
    for (u, v) in NONEDGES:
        A[(u, v)] = A[(v, u)] = 0
    return verts, A


def undecided_pairs(verts, A):
    return [(verts[i], verts[j]) for i in range(len(verts))
            for j in range(i + 1, len(verts))
            if (verts[i], verts[j]) not in A]


def add_witness(verts, A, i, j):
    """Rule (3): materialise a fresh witness w adjacent to both i and j."""
    w = _fresh_label(set(verts))
    nverts = list(verts) + [w]
    nA = dict(A)
    nA[(w, w)] = 0
    nA[(w, i)] = nA[(i, w)] = 1
    nA[(w, j)] = nA[(j, w)] = 1
    return nverts, nA


def upper_ok(verts, A):
    """SOUND upper-bound criterion over the materialised patch.

    (1) adjacent pairs <= 1 common neighbour; (2) non-adjacent <= 2;
    (4) locally 7K2: each N(v) a partial matching; (5) degree <= 14.
    Returns (ok, witness_text).  ONLY excesses are contradictions.
    """
    def adj(u, w):
        return A.get((u, w), 0)
    for u, w in itertools.combinations(verts, 2):
        common = [x for x in verts if x != u and x != w
                  and adj(u, x) and adj(w, x)]
        limit = 1 if adj(u, w) else 2
        if len(common) > limit:
            return False, ("pair %s%s %s has %d common neighbours (limit %d)"
                           % (u, w, 'ADJ' if adj(u, w) else 'NONADJ',
                              len(common), limit))
    for v in verts:
        nbrs = [u for u in verts if u != v and adj(v, u)]
        if len(nbrs) > DEGREE:
            return False, ("vertex %s degree %d > %d" % (v, len(nbrs), DEGREE))
        for u in nbrs:
            paired = [w for w in nbrs if w != u and adj(u, w)]
            if len(paired) > 1:
                return False, ("7K2: neighbour %s of %s adjacent to two "
                               "neighbours %s" % (u, v, paired))
    return True, "ok"


def closure_rule3(verts, A):
    """Grow a patch to a lambda-witness fixpoint via rule (3), re-checking
    (1),(2),(4),(5) between additions.  Returns (verts, A, status) where
    status is 'ok' (fixed point reached) or 'excess' (a patch assignment died).
    Grows ONLY by lambda-witness materialisation."""
    nverts, nA = list(verts), dict(A)
    while True:
        ok, _ = upper_ok(nverts, nA)
        if not ok:
            return nverts, nA, 'excess'
        grew = False
        for i, j in itertools.combinations(nverts, 2):
            if not nA.get((i, j), 0):
                continue
            common = [x for x in nverts
                      if x != i and x != j
                      and nA.get((i, x), 0) and nA.get((j, x), 0)]
            if len(common) == 0:
                nverts, nA = add_witness(nverts, nA, i, j)
                grew = True
                break
        if not grew:
            return nverts, nA, 'ok'


def assignments(verts, A, bit_cap=1 << 20):
    """All assignments of the undecided pairs, decoded as (bits, A').
    Returns None if the count exceeds bit_cap."""
    free = undecided_pairs(verts, A)
    lim = 1 << len(free)
    if lim > bit_cap:
        return None
    out = []
    for bits in range(lim):
        nA = dict(A)
        for k, (u, w) in enumerate(free):
            nA[(u, w)] = nA[(w, u)] = (bits >> k) & 1
        out.append((bits, nA))
    return out


def patch_cliques(verts, A):
    """All 3-cliques (triangles) fully inside the patch = the FORCED lines.
    With lambda=1 every triangle is a line (a triangle's third point is the
    unique common neighbour of any of its edges), so each patch triangle is a
    line pinned entirely inside the fixed set.  Returns the list of frozensets."""
    def adj(u, w):
        return A.get((u, w), 0)
    out = []
    for t in itertools.combinations(verts, 3):
        if adj(t[0], t[1]) and adj(t[0], t[2]) and adj(t[1], t[2]):
            out.append(frozenset(t))
    return out


def forced_ledger(verts, A):
    """Exact forced-line / incidence ledger of a FULLY-DECIDED patch against
    the global budget (99 pts, 7 lines/point, 693 incidences, 231 lines).

    Returns a dict with fields:
      V_patch          number of patch vertices
      fully_decided    whether every interior pair is decided (0 free bits)
      L_in             forced lines = #3-cliques fully inside the patch
      inc_in           3 * L_in  (forced incidences)
      per_vertex       {v: (tris_through_v, inside_neighbours)}
      line_deficit     {v: 7 - tri_through_v}  (residual lines each patch pt
                       must get from OUTSIDE partners)
      max_lines_v      max over patch vertices of tri_through_v
      odd_IN           list of vertices with odd |I(v)|  (a genuine obstruction
                       if nonempty: breaks matching-pairing closure)
      sat_overflow     list of vertices with tri_through_v > 7 (over-subscribed)
      residual_lines   231 - L_in
      residual_inc     693 - 3 * L_in
      sum_patch_deficit sum of line_deficit over patch vertices (== 7V-3L_in)
      outside_pts      99 - V_patch
      consistent       True iff no odd_IN, no sat_overflow, and deficits
                       nonnegative -- the arithmetically-overflow-free case.
    """
    def adj(u, w):
        return A.get((u, w), 0)
    cliques = patch_cliques(verts, A)
    L_in = len(cliques)
    tris_through = {v: 0 for v in verts}
    for c in cliques:
        for v in c:
            tris_through[v] += 1
    inside_nbrs = {}
    for v in verts:
        inside_nbrs[v] = [u for u in verts if u != v and adj(v, u)]
    odd_IN = [v for v in verts if len(inside_nbrs[v]) % 2 == 1]
    sat_overflow = [v for v in verts if tris_through[v] > 7]
    line_deficit = {v: 7 - tris_through[v] for v in verts}
    min_deficit = min(line_deficit.values())
    if min_deficit < 0:
        sat_overflow = [v for v in verts if line_deficit[v] < 0]
    return {
        'V_patch': len(verts),
        'fully_decided': not undecided_pairs(verts, A),
        'L_in': L_in,
        'inc_in': 3 * L_in,
        'tris_through': tris_through,
        'inside_nbrs': inside_nbrs,
        'line_deficit': line_deficit,
        'max_lines_v': max(tris_through.values()) if verts else 0,
        'odd_IN': odd_IN,
        'sat_overflow': sat_overflow,
        'residual_lines': N_LINES - L_in,
        'residual_inc': N_INC - 3 * L_in,
        'sum_patch_deficit': sum(line_deficit.values()),
        'outside_pts': V - len(verts),
        'consistent': (not odd_IN) and (not sat_overflow)
                      and min(line_deficit.values()) >= 0,
    }
