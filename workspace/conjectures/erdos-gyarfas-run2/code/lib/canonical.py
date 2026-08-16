"""Exact canonical form for small graphs (networkx 2.8.8 lacks nx.canonical_label).

Method (canonical Weisfeiler-Lehman colour refinement + enumeration in classes):
  1. Colour by degree. Then repeatedly refine: each vertex's colour becomes the
     rank of its signature (colour, sorted multiset of neighbour colours), where
     distinct signatures are ordered LEXICOGRAPHICALLY so the colour ids depend
     only on graph structure, never on vertex names. Iterate to a fixed point.
     This gives a CANONICAL colouring: if G ~= G' then the colour classes and
     sizes match and colour ids are preserved by the isomorphism.
  2. Assign labels to vertices block-by-block, block c getting labels
     [sum_{d<c}|class_d|, ...]. Enumerate every labelling that permutes vertices
     WITHIN each colour class, and keep the lexicographically smallest flattened
     adjacency matrix. That minimum is the canonical key.

Correctness: the colour-class partition is a pure function of graph structure,
so for isomorphic graphs the block structures coincide and the two sets of
admissible labelings correspond under the isomorphism; the minima therefore
agree. Conversely the min encoding is always a valid labelling of the graph, so
canon(G)==canon(G') with the same labelled matrix implies G and G' are both
isomorphic to that matrix, hence to each other. So equal key  <=>  isomorphic.

Complexity: polynomial in n except enumeration over the product of (class size)!
over colour classes. Only vertex-transitive graphs have a single large class
(e.g. C8: 8! = 40320), and n <= 8 throughout, so the worst case stays tiny.

Correctness established by cross-checking the per-level count of distinct keys
against the validated VF2-based generator (A002218: 1,3,10,56,468 at n=3..7)
and by pairwise VF2 spot checks.
"""

import itertools


def _colour(graphs_adj):
    """Canonical WL colouring. graphs_adj: dict v -> set of neighbours (one graph).
    Returns dict v -> colour id with colour ids canonical (structure-only)."""
    adj = graphs_adj
    # round 0: by degree
    deg = {v: len(adj[v]) for v in adj}
    degs = sorted(set(deg.values()))
    col = {v: degs.index(deg[v]) for v in adj}
    while True:
        signatures = {}
        for v in adj:
            nc = tuple(sorted(col[nbr] for nbr in adj[v]))
            signatures[v] = (col[v], nc)
        # unique signatures ordered lexicographically -> canonical ids
        uni = sorted(set(signatures.values()))
        newid = {s: i for i, s in enumerate(uni)}
        ncol = {v: newid[signatures[v]] for v in adj}
        if ncol == col:
            break
        col = ncol
    return col


def _classes(adj, col):
    classes = {}
    for v in adj:
        classes.setdefault(col[v], []).append(v)
    return [classes[c] for c in sorted(classes)]


def _encode(adj, labeling):
    size = len(adj)
    idx = {v: labeling[v] for v in adj}
    rows = []
    for v in sorted(adj, key=lambda x: labeling[x]):
        row = [0] * size
        for w in adj[v]:
            row[idx[w]] = 1
        rows.append(row)
    flat = []
    for row in rows:
        flat.extend(row)
    return tuple(flat)


def canonical_key(G):
    """Exact canonical key: min flattened adjacency matrix over all
    isomorphism-compatible labelings. Equal keys <=> isomorphic graphs."""
    adj = {v: set(G.neighbors(v)) for v in G.nodes()}
    col = _colour(adj)
    cls = _classes(adj, col)
    # assign contiguous label blocks in canonical colour order
    blocks = []
    used = 0
    for c in cls:
        blocks.append(list(range(used, used + len(c))))
        used += len(c)
    best = None
    for choice in itertools.product(*[itertools.permutations(b) for b in blocks]):
        labeling = {}
        for ci, c in enumerate(cls):
            for v, lab in zip(sorted(c), choice[ci]):
                labeling[v] = lab
        flat = _encode(adj, labeling)
        if best is None or flat < best:
            best = flat
    return best
