"""Verify the checkable kernel of research/approaches/forbidden-sublattice-lifting.md.

What: For the pentagon N5 and the diamond M3, compute the join-irreducibles and
their principal-filter sizes, and test Frankl's lattice form (some join-
irreducible j has |[j)| <= |L|/2, where [j) = {x>=j}).

Oracle function: this is a self-contained lattice computation (code/lib/uc.py is
for set-systems, not lattice orders). Each lattice is given by its covering
relations; join/meet/join-irreducibles/filters are computed exactly.

The inventor's kernel claims that N5 has a join-irreducible with |[ )| = 2 <= 5/2
and that M3 has atoms with |[ )| = 2 <= 5/2. This checks both, and reports the
TRUE abundant join-irreducibles.
"""

def make_order(elements, covers):
    """covers: dict element -> list of elements it directly covers (lower covers).
    Return a dict elem -> frozenset(elements <= elem)."""
    n = len(elements)
    idx = {e: i for i, e in enumerate(elements)}
    reach = {e: {e} for e in elements}
    # transitive closure upward from each element
    # build up-set by walking covers reversed (upper covers)
    upper = {e: set() for e in elements}
    for e, lo in covers.items():
        for l in lo:
            upper[l].add(e)
    for e in elements:
        stack = list(elements)
        # compute principal filter [e) = {x : e <= x} by DFS on upper
        seen = set()
        todo = [e]
        while todo:
            x = todo.pop()
            if x in seen: continue
            seen.add(x)
            for u in upper[x]:
                todo.append(u)
        reach[e] = seen
    return {e: frozenset(s) for e, s in reach.items()}

def join_irreducibles(elements, covers, order):
    """j != bottom is join-irreducible iff it has exactly one lower cover."""
    lower_cover_count = {e: len(covers.get(e, [])) for e in elements}
    js = [e for e in elements if lower_cover_count[e] == 1]
    return js

def check_frankl(elements, covers, label):
    order = make_order(elements, covers)
    js = join_irreducibles(elements, covers, order)
    L = len(elements)
    report = []
    for j in js:
        fsize = len(order[j])
        report.append((j, fsize, fsize <= L/2))
    sat = any(fsize <= L/2 for (_, fsize, _) in report)
    print(f"== {label}: |L|={L}, join-irreducibles & filter sizes ==")
    for j, f, ok in report:
        print(f"   {j}: |[{j})|={f}  <= {L}/2={L/2}? {ok}")
    print(f"   Frankl lattice form satisfied: {sat}")
    return sat

if __name__ == "__main__":
    # Pentagons, two standard labellings.
    # N5(A): covers 0<a, 0<c, a<b, c<b, b<1  (a,c the middle-atom pair, b=a∨c)
    N5_A_covers = {0:[], 'a':[0], 'c':[0], 'b':['a','c'], 1:['b']}
    print("PENTAGON layout A: chain 0<a<b<1 and 0<c<b, a∥c")
    check_frankl([0,'a','c','b',1], N5_A_covers, "N5 (layout A)")

    # N5(B): covers 0<a, 0<b, a<c, b<c, c<1, with a∥b  (standard Grätzer N5)
    N5_B_covers = {0:[], 'a':[0], 'b':[0], 'c':['a','b'], 1:['c']}
    print("PENTAGON layout B: 0<a<c<1, 0<b<c<1, a∥b")
    check_frankl([0,'a','b','c',1], N5_B_covers, "N5 (layout B)")

    # Diamond M3: 0 covered by a,b,c; a,b,c covered by 1
    M3_covers = {0:[], 'a':[0], 'b':[0], 'c':[0], 1:['a','b','c']}
    print("DIAMOND M3: 0 < a,b,c < 1")
    check_frankl([0,'a','b','c',1], M3_covers, "M3")
