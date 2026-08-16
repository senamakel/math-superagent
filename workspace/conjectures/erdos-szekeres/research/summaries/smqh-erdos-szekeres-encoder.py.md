> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/smqh-erdos-szekeres-encoder.py.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://raw.githubusercontent.com/bsubercaseaux/automatic-symmetries/main/encoders/erdos_szekeres.py | converted from plain text -->

## What is in it

- linear order on the points
    for (p, q) in itertools.permutations(range(n), 2):…
- non-degeneracy of the order
    for (p, q) in itertools.combinations(range(n), 2):…
- transitivity <
    for (p, q, r) in itertools.permutations(range(n), 3):…
- cyclic symmetry and anti-symmetry
    def cc(p, q, r):
        res = tuple(sorted((p, q,…
- Enforce symmetry
    sym_map = {}
    if forced_sym:
        layers =…
- for tri in itertools.combinations(range(n), 3):
        #     sym_tri = (sym_map[tri[0]],…
- convex quadrilaterals
    cnt = 0
    for (p, q, r, s) in…
- no g-gons
    cnt = 0
    for comb in itertools.combinations(range(n), g):
        cnt +=…
- Convex hull structure
    if forced_sym:
        print(f"layers: {layers}")
        for i…
- …


## What it claims

def encode(n, g, forced_sym=False):
    """
    Encode the existence of N points in the plane (general position) without g-gons.
    Args:
        N (int): number of points
        g (int): number of sides forbidden gon
        forced_sym (bool, int): forces k-fold symmetry when provided a positive integer.
    Returns:
        modeler.Modeler: encoded model"""
    enc = modeler.Modeler()
    for (p, q, r) in itertools.combinations(range(n), 3):
        enc.add_var(f"cc_{p, q, r}")

*[digest of a 5651 character source; every section, statement, and proof in full at `research/sources/smqh-erdos-szekeres-encoder.py.full.md`]*
