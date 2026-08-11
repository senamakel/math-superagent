"""Reusable routines for the Project Euler 763 3D amoeba problem.

Reachability: an amoeba at p=(x,y,z) may divide into three amoebas at the
positive-unit neighbours (x+1,y,z), (x,y+1,z), (x,y,z+1) provided those three
cubes are empty; the parent disappears.  After N divisions a config holds
2N+1 cubes, each coordinate in [0,N].  D(N) is the number of DISTINCT sets of
occupied cubes reachable after exactly N divisions.

Encodings supported:
  * frozenset of (x,y,z) tuples
  * int bitmask with fixed width W: bit index (x*W + y)*W + z

Feature extraction (what /workspace/data records): given the set of occupied
cubes of a config, compute
  * histogram a_k  = #cubes with x+y+z == k  (the "level" / generation)
  * bbox          = (xmin,xmax,ymin,ymax,zmin,zmax)
  * bbox_dims     = (xmax-xmin, ymax-ymin, zmax-zmin)
  * M             = max level present = max(x+y+z)

Correctness of the BFS/claim is established elsewhere (see brute oracles
reproducing D(2)=3 and D(10)=44499); this module only supplies parse/feature
helpers shared by the driver and the data dumps.
"""

# --- forward neighbours ----------------------------------------------------


def children(p, d):
    """Forward d-neighbours of a point p in Z^d: p + e_i for i in 0..d-1
    (one unit added to coordinate i).  Returns a list of the d child tuples.

    This is the single canonical shared definition of the amoeba division's
    forward children, consolidated from four copies formerly in
    verify_reverse_merge.py, probe_reachable.py and the two
    research_structure.py files (they had NOT diverged, so no definition was
    chosen over another).  Correctness established by those programs
    reproducing D(2)=3 and D(10)=44499.
    """
    return [tuple(p[i] + (1 if i == j else 0) for i in range(d)) for j in range(d)]


# --- BFS step on frozenset-of-tuples configs ------------------------------


def next_level_fs(level):
    """One BFS step over 3D frozenset-of-tuples configs (exact arithmetic).

    `level` is an iterable of frozensets of (x,y,z) cubes.  Returns the set
    of all distinct configurations reachable by exactly one division: a cube
    p may divide iff its three positive-unit neighbours (x+1,y,z), (x,y+1,z),
    (x,y,z+1) are all empty, and the result replaces p with those three.

    This is the naive frozenset oracle step — exponential state space, used
    only for small-N definition checks and for dumping actual configs.  Its
    correctness is established by reproducing D(2)=3 and D(10)=44499 (see the
    brute oracles), and it is the same frozenset semantics as the bitmask
    twin next_level_bits.
    """
    E1, E2, E3 = (1, 0, 0), (0, 1, 0), (0, 0, 1)
    nxt = set()
    for S in level:
        Sset = set(S)
        for p in S:
            a = (p[0] + E1[0], p[1] + E1[1], p[2] + E1[2])
            b = (p[0] + E2[0], p[1] + E2[1], p[2] + E2[2])
            c = (p[0] + E3[0], p[1] + E3[1], p[2] + E3[2])
            if a not in Sset and b not in Sset and c not in Sset:
                ns = Sset - {p} | {a, b, c}
                nxt.add(frozenset(ns))
    return nxt


def forward_level(level, d):
    """One forward-BFS step over frozenset-of-tuples configs in d dimensions.

    `level` is an iterable of frozensets of d-tuples (occupied cubes/cells).
    Returns the set of all distinct configurations reachable by exactly one
    division: a cell p may divide iff all d of its positive-unit forward
    neighbours p+e_i (i=0..d-1) are empty, and the result replaces p with
    those d.  For d=3 this is exactly the naive oracle step next_level_fs,
    and for d=2 it is the 2D step.

    This is the CANONICAL shared definition of the one-step frozenset BFS,
    consolidated from four copies that formerly lived in
    amoeba2d/verify_reverse_merge.py (parametrized by d) and
    inventor/check_recurrence.py, inventor/probe_reachable.py,
    inventor/probe_topcap.py (each hardcoded d=3); for their common 3D case
    the four agreed exactly, and the parametrized one reduces to the 3D
    copies at d=3, so no definition had to be chosen over another.
    Correctness established by those programs reproducing D(2)=3 and
    D(10)=44499.
    """
    nxt = set()
    for S in level:
        Sset = set(S)
        for p in Sset:
            ch = children(p, d)
            if all(c not in Sset for c in ch):
                nxt.add(frozenset((Sset - {p}) | set(ch)))
    return nxt


# --- naive BFS driver -----------------------------------------------------


def reachable_sets(N, d=3):
    """All distinct frozensets of d-tuples reachable after exactly N divisions.

    Naive level-by-level BFS driver: start from the single config {(0,...,0)}
    and apply forward_level one step per division.  For d=3 this is exactly
    the 3D oracle used in the brute programs (D(2)=3, D(10)=44499); for d=2
    it is the 2D oracle (D_2D).  Exponential state space; only for tiny N as
    a definition check.

    This is the single CANONICAL definition of the naive `reachable_sets`
    driver, consolidating three copies that were previously in
    code/brute.py, code/amoeba/brute.py (identical 3D copies) and
    code/amoeba2d/d2d.py (a genuinely divergent 2D copy).  The divergence is
    resolved by the dimension parameter d, not by silently choosing one: the
    two 3D copies agreed with each other exactly, and the 2D copy reduces to
    this at d=2.  Correctness of the underlying one-level step is established
    by the brute oracles reproducing D(2)=3 and D(10)=44499.
    """
    start = frozenset({(0,) * d})
    level = {start}
    for _ in range(N):
        level = forward_level(level, d)
        if not level:
            break
    return level


def D(N, d=3):
    """Number of distinct frozenset configs reachable after exactly N divisions
    in d dimensions (d=3 for PE763, d=2 for the 2D analogue)."""
    return len(reachable_sets(N, d))


# --- decoding -------------------------------------------------------------


def decode_bits(S, W):
    """Decode an int bitmask (width W) into a frozenset of (x,y,z) tuples."""
    W2 = W * W
    cells = set()
    m = S
    while m:
        low = m & -m
        i = low.bit_length() - 1
        m ^= low
        x, r = divmod(i, W2)
        y, z = divmod(r, W)
        cells.add((x, y, z))
    return frozenset(cells)


def encode_bits(cells, W):
    """Encode a set of (x,y,z) tuples into an int bitmask of width W."""
    W2 = W * W
    S = 0
    for (x, y, z) in cells:
        S |= 1 << (x * W2 + y * W + z)
    return S


# --- structural features --------------------------------------------------


def config_features(cells):
    """Structural features of an occupied-cube set.

    Returns dict with keys: 'hist' (dict level->count), 'bbox' (tuple of six
    bounds), 'dims' (tuple of three bounding-box extents), 'M' (max level).
    """
    hist = {}
    xs, ys, zs = [], [], []
    lv = 0
    for (x, y, z) in cells:
        xs.append(x)
        ys.append(y)
        zs.append(z)
        k = x + y + z
        hist[k] = hist.get(k, 0) + 1
        if k > lv:
            lv = k
    return {
        'hist': hist,
        'bbox': (min(xs), max(xs), min(ys), max(ys), min(zs), max(zs)),
        'dims': (max(xs) - min(xs), max(ys) - min(ys), max(zs) - min(zs)),
        'M': lv,
    }


def feature_record(cells):
    """Compact textual record of one config: hist as a_k list and dims.

    Used by the /workspace/data dumps. Returns (level_hist_list, M, dims).
    """
    f = config_features(cells)
    a = [f['hist'].get(k, 0) for k in range(f['M'] + 1)]
    return a, f['M'], f['dims']


# --- BFS step on bitmasks -------------------------------------------------


def next_level_bits(level, W):
    """One BFS step on a set of int-masked configs; W is fixed grid width.

    Returns the set of all distinct one-division successors.  A cube p may
    divide iff its three positive-unit neighbours are all empty; successors
    are S with p cleared and the three neighbours set.
    """
    nxt = set()
    W2 = W * W
    for S in level:
        m = S
        while m:
            low = m & -m
            i = low.bit_length() - 1
            m ^= low
            x, r = divmod(i, W2)
            y, z = divmod(r, W)
            a = 1 << ((x + 1) * W2 + y * W + z)
            b = 1 << (x * W2 + (y + 1) * W + z)
            c = 1 << (x * W2 + y * W + (z + 1))
            if (S & (a | b | c)) == 0:
                ns = (S ^ low) | a | b | c
                nxt.add(ns)
    return nxt
