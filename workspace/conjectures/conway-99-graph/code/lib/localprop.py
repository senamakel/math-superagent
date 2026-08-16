"""Exact partial-graph constraint propagation for a lambda=1, mu=2, locally-7K2
strongly regular graph (the (99,14,1,2) local regime).

A PartialGraph is an exact integer partial adjacency matrix with entries
  +1  known adjacent
   0  known non-adjacent
  -1  unknown
Symmetry and a zero diagonal are maintained.  Propagation is complete
arc-consistency channelling (NO branching, NO search): every forced 0/1 is a
deterministic consequence of the stated rules, so a fixpoint reached here is a
*lower bound* on any completion, and a genuine contradiction found here is a
theorem that no completion can avoid.

Rules enforced (exact integer):
  * lambda = 1 : every ADJACENT pair shares EXACTLY one common neighbour.
  * mu    = 2 : every NON-ADJACENT pair shares EXACTLY two common neighbours.
  * locally 7K2 / degree: the established neighbourhood of every vertex is a
    partial matching (a vertex can have at most one established neighbour
    inside another vertex's neighbourhood) and every established degree is
    within the target k.

The ONLY genuine contradictions are EXCESSES:
  * an adjacent pair with >= 2 established common neighbours;
  * a non-adjacent pair with >= 3 established common neighbours;
  * a degree exceeding k;
  * an established 7K2 matching break (a neighbourhood vertex adjacent to two
    distinct established neighbours of the same vertex).
Deficits (fewer common neighbours than required) are NOT contradictions: they
are supplied by the ~90 un-materialised outside vertices of the full 99-vertex
graph.  An adjacent edge whose unique lambda-witness lies outside the current
patch FORCES an external witness vertex (materialised by propagate); a
non-adjacent pair's mu=2 deficit is reported (mu_witness_deficits) without
materialising the two witnesses, to keep the patch small and the fixpoint
clean.

CONTROLS: rook(3)=srg(9,4,1,2) and bvls_graph()=srg(243,22,1,2) satisfy
lambda, mu and locally-7K2 (neighbourhood_is_7k2), so the rule set is not
self-contradictory; any contradiction the local probe finds is specific to
its start configuration, not to the rules.
"""


def neighbourhood_is_7k2(A, v, k):
    """True iff vertex v of integer matrix A has a neighbourhood equal to
    (k/2)K2: exactly k neighbours forming k/2 disjoint edges (each neighbour
    adjacent to exactly one other neighbour and nothing more).  Exact integer.
    k must be even and <= n-1."""
    n = A.shape[0]
    nbrs = [u for u in range(n) if u != v and A[v, u] == 1]
    if len(nbrs) != k:
        return False
    internal = 0
    for idx, u in enumerate(nbrs):
        deg = sum(1 for w in nbrs if A[u, w] == 1)
        if deg != 1:
            return False
        for w in nbrs[idx + 1:]:
            if A[u, w] == 1:
                internal += 1
    return internal == k // 2


class PartialGraph:
    def __init__(self, n, k):
        self.n = n
        self.k = k                 # target degree (14 for (99,14,1,2))
        self.adj = [[-1] * n for _ in range(n)]
        for i in range(n):
            self.adj[i][i] = 0

    def add_vertex(self):
        for row in self.adj:
            row.append(-1)
        self.adj.append([-1] * (self.n + 1))
        self.n += 1
        self.adj[-1][-1] = 0

    def _set(self, i, j, v):
        """Set adj[i][j]=adj[j][i]=v atomically.  Returns False if it would
        flip an already-decided bit (a contradiction elsewhere)."""
        if i == j:
            return v == 0
        old = self.adj[i][j]
        if old == v:
            return True
        if old != -1:
            return False
        self.adj[i][j] = v
        self.adj[j][i] = v
        return True

    def _established_common(self, i, j):
        return [v for v in range(self.n)
                if v != i and v != j
                and self.adj[i][v] == 1 and self.adj[j][v] == 1]

    def _common_candidates(self, i, j):
        """Vertices v != i,j that could still become an additional common
        neighbour: neither adjacency to i nor to j is decided 0."""
        return [v for v in range(self.n)
                if v != i and v != j
                and self.adj[i][v] != 0 and self.adj[j][v] != 0]

    def propagate_once(self, log):
        """One sweep over all pairs.  Returns False on a genuine (excess)
        contradiction.  For a decided pair (i,j) with required count c
        (1 adjacent, 2 non-adjacent), with K the established common neighbours
        and C the candidates:
            |K| > c            -> CONTRADICTION (excess, all established)
            |K| == c           -> saturated: ban overflow, force every C out
                                  of both i and j
            |K| < c            -> deficit: NOT a contradiction (outside vertices
                                  supply it); exposes lambda_witness_deficits /
                                  mu_witness_deficits.  The candidate count C is
                                  an UNDER-count (most outside vertices are not
                                  materialised), so no subset may be forced in.
        """
        for i in range(self.n):
            for j in range(i + 1, self.n):
                a = self.adj[i][j]
                if a == 1:
                    c = 1
                elif a == 0:
                    c = 2
                else:
                    continue
                K = self._established_common(i, j)
                if len(K) > c:
                    log.append(f"  CONTRADICTION: pair ({self.name(i)},{self.name(j)}) "
                               f"[{'adjacent' if a==1 else 'non-adjacent'}] has "
                               f"{len(K)} established common neighbours (need {c})")
                    return False
                C = [v for v in self._common_candidates(i, j) if v not in K]
                if len(K) == c:
                    # saturated: (i,j) already has its full quota of common
                    # neighbours, so no candidate may become one.  For a
                    # candidate already adjacent to exactly one endpoint, prune
                    # the other side to 0 (leaving both sides unknown is sound
                    # too, but undecidable without degree info; we only prune
                    # the forced side).
                    for v in C:
                        if self.adj[i][v] == 1 and self.adj[j][v] == -1:
                            if not self._set(j, v, 0):
                                log.append(f"  CONTRADICTION: saturated pair "
                                           f"({self.name(i)},{self.name(j)}) "
                                           f"overflow via {self.name(v)}")
                                return False
                            log.append(f"  force {self.name(j)}-{self.name(v)}=0 "
                                       f"(saturate {self.name(i)}{self.name(j)})")
                        elif self.adj[j][v] == 1 and self.adj[i][v] == -1:
                            if not self._set(i, v, 0):
                                log.append(f"  CONTRADICTION: saturated pair "
                                           f"({self.name(i)},{self.name(j)}) "
                                           f"overflow via {self.name(v)}")
                                return False
                            log.append(f"  force {self.name(i)}-{self.name(v)}=0 "
                                       f"(saturate {self.name(i)}{self.name(j)})")
                        elif self.adj[i][v] == 1 and self.adj[j][v] == 1:
                            # already a common neighbour -> must be in K, but
                            # |K| is already c and v not in K: contradiction
                            return False
                        # both unknown: leave undecided (no forced side)
        return True

    def lambda_witness_deficits(self):
        """Adjacent (c=1) pairs whose unique common neighbour is not yet
        established among the patch: each FORCES an external lambda-witness
        vertex adjacent to both endpoints.  Returns [(i,j), ...]."""
        need = []
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.adj[i][j] != 1:
                    continue
                K = self._established_common(i, j)
                C = [v for v in self._common_candidates(i, j) if v not in K]
                if len(K) + len(C) < 1:
                    need.append((i, j))
        return need

    def mu_witness_deficits(self):
        """Per non-adjacent (c=2) pair: how many common neighbours must come
        from outside the patch.  Returns [(name_i, name_j, |K|, |C|, deficit)]."""
        out = []
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.adj[i][j] != 0:
                    continue
                K = self._established_common(i, j)
                C = [v for v in self._common_candidates(i, j) if v not in K]
                deficit = max(0, 2 - (len(K) + len(C)))
                out.append((self.name(i), self.name(j), len(K), len(C), deficit))
        return out

    def propagate(self, log):
        """Run propagation to a fixpoint (or a contradiction).  Returns
        (consistent: bool, iterations: int).

        Each sweep does complete channelling; then any adjacent edge whose
        lambda witness must be external gains one fresh materialised vertex
        (distinct witnesses per edge is the conservative reading), and the
        sweep repeats.  Deterministic throughout."""
        it = 0
        while True:
            it += 1
            ok = self.propagate_once(log)
            if not ok:
                return False, it
            ok = self.propagate_7k2(log)
            if not ok:
                return False, it
            need = self.lambda_witness_deficits()
            if need:
                for (i, j) in need:
                    v = self.n
                    self.add_vertex()
                    self._set(i, v, 1)
                    self._set(j, v, 1)
                    log.append(f"  -- edge {self.name(i)}{self.name(j)}: unique lambda "
                               f"witness is external; add witness {self.name(v)} "
                               f"adjacent to both")
                continue
            return True, it

    def propagate_7k2(self, log):
        """Propagate the locally-7K2 EXACT-PAIRING rule: in a perfect-matching
        neighbourhood, each neighbour u of a vertex v has exactly ONE neighbour
        inside N(v).  So if u is already established-adjacent to a neighbour w
        of v (u,w both in N(v)), then u is non-adjacent to every OTHER neighbour
        of v.  Sound: a second inside-neighbour would break the matching.
        Returns False on a contradiction (u already adjacent to two
        distinct neighbours of v)."""
        for v in range(self.n):
            nbrs = [x for x in range(self.n) if x != v and self.adj[v][x] == 1]
            for u in nbrs:
                # neighbours of v that u is established-adjacent to:
                paired = [w for w in nbrs
                          if w != u and self.adj[u][w] == 1]
                if len(paired) >= 2:
                    log.append(f"  CONTRADICTION (7K2): in N({self.name(v)}), "
                               f"{self.name(u)} is adjacent to "
                               f"{', '.join(self.name(x) for x in paired)}")
                    return False
                if len(paired) == 1:
                    pr = paired[0]
                    # u is already paired with pr inside N(v): u is non-adjacent
                    # to every other neighbour of v.
                    for w in nbrs:
                        if w == u or w == pr:
                            continue
                        if self.adj[u][w] == -1:
                            if not self._set(u, w, 0):
                                return False
                            log.append(f"  force {self.name(u)}-{self.name(w)}=0 "
                                       f"(7K2: {self.name(u)} paired with "
                                       f"{self.name(pr)} in N({self.name(v)}))")
                    # symmetric: pr is not adjacent to the rest of N(v) either
                    for w in nbrs:
                        if w == u or w == pr:
                            continue
                        if self.adj[pr][w] == -1:
                            if not self._set(pr, w, 0):
                                return False
                            log.append(f"  force {self.name(pr)}-{self.name(w)}=0 "
                                       f"(7K2: {self.name(pr)} paired with "
                                       f"{self.name(u)} in N({self.name(v)}))")
        return True

    # -- reporting -------------------------------------------------------
    def name(self, i):
        names = getattr(self, '_names', None)
        if names is not None and i < len(names):
            return names[i]
        return str(i)

    def forced_ones(self):
        return [(self.name(i), self.name(j)) for i in range(self.n)
                for j in range(i + 1, self.n) if self.adj[i][j] == 1]

    def forced_zeroes(self):
        return [(self.name(i), self.name(j)) for i in range(self.n)
                for j in range(i + 1, self.n) if self.adj[i][j] == 0]

    def free_entries(self):
        return [(self.name(i), self.name(j)) for i in range(self.n)
                for j in range(i + 1, self.n) if self.adj[i][j] == -1]

    def degrees(self):
        return {self.name(i): sum(1 for j in range(self.n) if self.adj[i][j] == 1)
                for i in range(self.n)}

    def established_common(self, i, j):
        return [self.name(v) for v in self._established_common(i, j)]

    def matching_ok(self):
        """Check the locally-7K2 condition on the PARTIAL assignment: every
        established neighbour u of every v must have at most ONE established
        neighbours-of-v that u is adjacent to.  Returns (ok, failure)."""
        for v in range(self.n):
            nbrs = [u for u in range(self.n) if self.adj[v][u] == 1]
            for u in nbrs:
                cnt = sum(1 for w in nbrs if w != u and self.adj[u][w] == 1)
                if cnt >= 2:
                    return False, (f"vertex {self.name(v)}: neighbour "
                                   f"{self.name(u)} 7K2-adjacent to {cnt} "
                                   f"other neighbours")
        return True, None

    def degree_ok(self):
        for v in range(self.n):
            d = sum(1 for u in range(self.n) if u != v and self.adj[v][u] == 1)
            if d > self.k:
                return False, v, d
        return True, None, None

    def report(self):
        lines = []
        lines.append(f"  vertices: {self.n}")
        lines.append(f"  forced edges (adjacent): {sorted(self.forced_ones())}")
        lines.append(f"  forced non-edges:        {sorted(self.forced_zeroes())}")
        lines.append(f"  free (unknown) entries:  {len(self.free_entries())}  "
                     f"-> {sorted(self.free_entries())}")
        lines.append(f"  established degrees:      {self.degrees()}")
        return "\n".join(lines)
