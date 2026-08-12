"""Lobe probe for the (2,2) cut-vertex shape of the Cut-Vertex Characterization
lemma (this run's Phase-4 structural candidate, CONTEXT.md / scratch note
"cut-vertex structure lemma derivation").

SETTING.  v is a cut vertex of a minimal counterexample G with k=2 lobes and
d(v)=4, the (2,2) split.  Clauses (d),(e) of the characterization force each
lobe L_i = G[C_i ∪ {v}] to satisfy:  v has exactly two neighbours in C_i
(d_i = 2), every w in C_i has d_L(w) = d_G(w) >= 3, and L_i has no
power-of-two cycle.

The lobe shapes that realise this:  L = H - e + v  where H is a *connected
cubic* graph on n_H vertices, e = xy an edge of H, and v is a fresh vertex
adjacent to exactly x and y.  Then d(v)=2, d_H-removed vertices keep degree
3, and x, y lose e but keep their two other edges, so d_L = (3,3,...,3,2) on
C_i, indeed d_L(w) >= 3 for every w != v, delta(L) = 2 realised only at v.
Conversely any lobe with exactly two low-degree vertices whose low-degree
vertices are adjacent in the lobe (i.e. the "sufficient-neighbourhood" form)
is H - e + v for the cubic H obtained by contracting...  -- this probe only
enumerates the H-e+v shape, which the characterization's d_i = 2 forces v to
have *two* neighbours in C_i.

Three jobs:

  J1  For every connected cubic graph H on n_H = 4..14 (nauty-geng -q -c -d3
      -D3, counts must match A002851 prefix 1,2,5,19,85,509), and for every
      edge e of H, form L = H - e + v and test whether L has a cycle of
      length 4, 8, or 16.  Report per n_H: the number of distinct
      (up-to-isomorphism) power-of-two-free lobes, their canonical graph6
      and full cycle-length sets.

  J2  The smallest power-of-two-free lobe, and its cycle set.

  J3  Pair search: every two power-of-two-free lobes on disjoint vertex sets
      with total glued order |H1| + |H2| - 1 <= 30, glue them by identifying
      their two v-vertices into one central cut vertex of degree 4 (the
      (2,2) cut-vertex shape), and oracle-check the glued graph.  A pair of
      pow2-free lobes *must* glue to a pow2-free (1-connected, delta>=3)
      graph if no simple cycle of the glued graph crosses the cut (the
      no-cross-cycles claim); the probe verifies that claim by comparing the
      glued cycle set against the union of the two lobe cycle sets, and any
      pow2-free glued graph is a concrete 1-connected strong
      near-counterexample shape.

POW2 TEST.  Since |L| = n_H + 1 <= 15, the only possible powers of two are
4 and 8.  The oracle's has_cycle_of_length(L, 4/8) is used (early exit);
the (rare) pow2-free lobes get their FULL cycle set via distinct_cycle_lengths
and are cross-checked against a full enumeration.

ISOMORPHISM.  Lobes (and glued graphs) are deduplicated with nauty-shortg -u
(canonical up-to-isomorphism representatives), and every reported graph6 is
the nauty-canonical form read back from shortg's output.

Complexity:  enumeration of connected cubic graphs is |A002851| <= 509 at
n=14, each with <= 21 edges, so ~10^4 lobe constructions; cycle checks are
the exponential small-instance oracle (rule 9, oracle bound n <= 31) and are
the *verification* tool, not the method.  Pair space: (sum of pow2-free lobe
counts over n_H=4..14 choose 2) but restricted to pairs with total order
<= 30, a few tens of thousands at most.
"""
import os
import subprocess
import sys

import networkx as nx

from lib.cycle_oracle import (
    minimum_degree,
    distinct_cycle_lengths,
    has_cycle_of_length,
    oracle,
)

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(os.path.dirname(HERE), "out", "cutvertex", "lobe_probe")

POW2_MIN = 4
POW2_MAX = 16  # 4, 8, 16 — the powers that can occur at glued order <= 31


def connected_cubic_graph6(n):
    """Every connected cubic graph on n vertices, one graph6 per line.

    nauty-geng -q -c -d3 -D3 : connected, min degree 3, max degree 3.
    Counts must equal A002851(n) (1,2,5,19,85,509,4060,41301 for n=4..18).
    """
    out = subprocess.run(
        ["nauty-geng", "-q", "-c", "-d3", "-D3", str(n)],
        capture_output=True, text=True, check=True,
    )
    return out.stdout.splitlines()


def shortg_dedup(graph6_strings, fmt="-g"):
    """Return the up-to-isomorphism representatives of a list of graph6
    strings, in nauty-canonical labelling (so their graph6 strings are
    identical iff they are isomorphic).  Empty input -> []."""
    if not graph6_strings:
        return []
    data = ("\n".join(graph6_strings) + "\n").encode()
    p = subprocess.run(["nauty-shortg", "-u", "-q", fmt],
                       input=data, capture_output=True)
    if p.returncode != 0:
        raise RuntimeError(f"nauty-shortg failed: {p.stderr.decode()[-500:]}")
    return p.stdout.decode().splitlines()


def lobe_from_edge(H, e, v_label=None):
    """L = H - e + v: remove edge e=(x,y) from cubic H, add fresh vertex v
    adjacent to exactly x and y.  v_label can pin a specific label."""
    L = nx.Graph()
    L.add_nodes_from(H.nodes())
    L.add_edges_from(H.edges())
    L.remove_edge(*e)
    v = v_label if v_label is not None else max(H.nodes()) + 1
    L.add_node(v)
    L.add_edge(v, e[0])
    L.add_edge(v, e[1])
    return L, v


def lobe_deg_check(L, v, H, e):
    """Verify the lobe degree structure: d_L(v)=2, d_L(w)>=3 for all w!=v,
    and d_L(w)==d_H(w) for w not in {x,y} (x,y lose exactly one edge)."""
    degs = dict(L.degree())
    assert degs[v] == 2, f"d(v)={degs[v]} != 2"
    for w in L.nodes():
        if w != v:
            assert degs[w] >= 3, f"lobe vertex w={w} has d_L={degs[w]} < 3"
    for w in L.nodes():
        if w != v and w not in e:
            assert degs[w] == H.degree(w), \
                f"lobe degree changed at w={w}: {degs[w]} vs {H.degree(w)}"


def canon_g6(G):
    """Canonical graph6 of G (nauty-canonical labelling, no trailing NL)."""
    raw = nx.to_graph6_bytes(G, header=False).decode().strip()
    reps = shortg_dedup([raw])
    assert reps, "canon_g6 produced nothing"
    return reps[0]


def main():
    os.makedirs(OUTDIR, exist_ok=True)
    log_path = os.path.join(OUTDIR, "lobe_probe.log")
    log = open(log_path, "w")

    def say(*a):
        line = " ".join(str(x) for x in a)
        print(line, flush=True)
        log.write(line + "\n")
        log.flush()

    say("=" * 78)
    say("Lobe probe — (2,2) cut-vertex shape: L = H - e + v, H connected cubic")
    say("=" * 78)
    say(f"powers-of-two tested: {{{POW2_MIN}, {8}, {POW2_MAX}}} "
        f"(only 4 and 8 can occur in a lobe with |V| <= 15)")

    # ---- accumulate pow2-free lobes across n_H = 4..14 -----------------
    # key: (n_H, canonical lobe graph6) -> dict(info)
    pow2free_lobes = {}   # canonical g6 -> {"nH":, "cycle_set":, "H_g6":, "e":, "h_geng_idx":}
    smallest_lobe = None  # (nH, g6, cycle_set)
    counts_by_nH = {}     # nH -> (n_cubic, n_lobes_total, n_lobes_distinct, n_pow2free)

    for n_H in range(4, 15, 2):   # cubic graphs require even order
        t0 = __import__("time").time()
        cubic = connected_cubic_graph6(n_H)
        n_cubic = len(cubic)
        # sanity: counts must match A002851 prefix
        expected = {4: 1, 6: 2, 8: 5, 10: 19, 12: 85, 14: 509}
        assert n_cubic == expected[n_H], \
            f"cubic count at n_H={n_H}: got {n_cubic}, expected {expected[n_H]}"

        lobes_raw = []       # (H idx, edge idx)
        lobes_g6_raw = []
        n_lobes_total = 0
        for h_idx, g6 in enumerate(cubic):
            H = nx.from_graph6_bytes(g6.encode())
            for e_idx, e in enumerate(H.edges()):
                L, v = lobe_from_edge(H, e)
                lobe_deg_check(L, v, H, e)
                n_lobes_total += 1
                # power-of-two test: only 4 or 8 fit in |V(L)| = n_H+1 <= 15
                has_pow2 = (has_cycle_of_length(L, 4)
                            or has_cycle_of_length(L, 8))
                if not has_pow2:
                    lobes_raw.append((h_idx, e_idx, g6, e))
                    g6s = canon_g6(L)
                    lobes_g6_raw.append(g6s)
        # dedup up to isomorphism
        distinct_g6 = shortg_dedup(lobes_g6_raw)
        n_lobes_distinct = len(distinct_g6)
        n_pow2free = len(distinct_g6)

        n_new = 0
        for g6s in distinct_g6:
            if g6s not in pow2free_lobes:
                L = nx.from_graph6_bytes(g6s.encode())
                cs = set(distinct_cycle_lengths(L))
                # cross-check the full enumeration against the oracle check
                assert not (4 in cs or 8 in cs), f"{g6s}: full set has a pow2"
                assert L.number_of_nodes() == n_H + 1
                assert minimum_degree(L) == 2, f"{g6s}: min degree != 2"
                pow2free_lobes[g6s] = {"nH": n_H, "cycle_set": sorted(cs)}
                n_new += 1
                if smallest_lobe is None or n_H < smallest_lobe[0]:
                    smallest_lobe = (n_H, g6s, sorted(cs))
        counts_by_nH[n_H] = (n_cubic, n_lobes_total, n_lobes_distinct,
                             n_pow2free, n_new)
        say(f"n_H={n_H:3d}  cubic={n_cubic:5d}  lobe-constructions={n_lobes_total:6d}"
            f"  distinct-lobes={n_lobes_distinct:4d}  pow2-free={n_pow2free:4d}"
            f"  (new so far {n_new}, cumulative {len(pow2free_lobes)})"
            f"  [{__import__('time').time() - t0:5.1f}s]")

    say("-" * 78)
    say(f"TOTAL distinct pow2-free lobes over n_H=4..14: {len(pow2free_lobes)}")
    say(f"SMALLEST pow2-free lobe: n_H={smallest_lobe[0]} + v, "
        f"order {smallest_lobe[0]+1}; graph6 {smallest_lobe[1]}; "
        f"cycle set {smallest_lobe[2]}")
    say(f"  (lobe min degree = 2 at v only; all other degrees >= 3; "
        f"no C4, no C8, no C16)")

    # ---- per-nH table + dump -------------------------------------------
    say("")
    say("per-n_H summary table (n_H: cubic, constructions, distinct, "
        "pow2-free, new-this-row):")
    for n_H in range(4, 15, 2):
        c = counts_by_nH[n_H]
        say(f"  n_H={n_H:3d}: {c[0]:5d} cubic -> {c[1]:6d} lobe constructions "
            f"-> {c[2]:4d} distinct -> {c[3]:4d} pow2-free (cumulative new {c[4]})")

    with open(os.path.join(OUTDIR, "pow2free_lobes.txt"), "w") as f:
        f.write("# canonical graph6 of every pow2-free lobe L = H-e+v, "
                "H connected cubic n_H=4..14\n")
        f.write("# columns: n_H | order | graph6 | cycle-length-set\n")
        for g6s in sorted(pow2free_lobes, key=lambda g: (pow2free_lobes[g]["nH"], g)):
            d = pow2free_lobes[g6s]
            f.write(f"{d['nH']} {d['nH']+1} {g6s} {' '.join(map(str, d['cycle_set']))}\n")

    # ---- J3: pair search ------------------------------------------------
    say("")
    say("=" * 78)
    say("J3 — pair search: any two pow2-free lobes with")
    say("     total glued order |H1|+|H2|-1 <= 30  (central vertex deg 4)")
    say("=" * 78)

    # group by nH for the order bound
    by_nH = {}
    for g6s, d in pow2free_lobes.items():
        by_nH.setdefault(d["nH"], []).append(g6s)

    nH_list = sorted(by_nH)
    pair_count = 0
    glued_free = []      # (order, g1, g2, glued_g6, has_pow2, cycle_sets_agree, glued_set)
    longest = None
    for i, n1 in enumerate(nH_list):
        for n2 in nH_list[i:]:
            if n1 + n2 - 1 > 30:
                continue
            lobes1 = by_nH[n1]
            lobes2 = by_nH[n2]
            for g1 in lobes1:
                for g2 in lobes2:
                    if n1 == n2 and g2 <= g1:
                        continue  # avoid mirror pairs within the same row
                    pair_count += 1
                    L1 = nx.from_graph6_bytes(g1.encode())
                    L2 = nx.from_graph6_bytes(g2.encode())
                    # identify the two v-vertices: v is the unique degree-2 vertex
                    v1 = [u for u, d in L1.degree() if d == 2]
                    v2 = [u for u, d in L2.degree() if d == 2]
                    assert len(v1) == 1 and len(v2) == 1, (g1, g2)
                    # Build the glued graph with the central vertex at label 0,
                    # L1's other vertices shifted +1, L2's other vertices
                    # shifted by off2 = 1 + n_H1  (n_H1 = |V(L1)| - 1).
                    n1 = L1.number_of_nodes() - 1        # inner vertices of L1
                    off2 = 1 + n1                        # shift for L2 others
                    G = nx.Graph()
                    C = 0
                    def map1(u):
                        return C if u == v1[0] else u + 1
                    def map2(u):
                        return C if u == v2[0] else u + off2
                    for a, b in L1.edges():
                        G.add_edge(map1(a), map1(b))
                    for a, b in L2.edges():
                        G.add_edge(map2(a), map2(b))
                    # central cut vertex: its degree comes from 2 edges of L1
                    # (v1-x, v1-y) plus 2 of L2 (v2-x', v2-y') = 4.
                    assert G.degree(C) == 4, f"central deg {G.degree(C)}"
                    assert minimum_degree(G) >= 3, "glued graph min degree < 3"
                    assert nx.node_connectivity(G) == 1  # C is a cut vertex
                    assert nx.is_connected(G)
                    glued_set = set(distinct_cycle_lengths(G))
                    union = set(distinct_cycle_lengths(L1)) | set(
                        distinct_cycle_lengths(L2))
                    agree = glued_set == union
                    has_pow2 = bool(glued_set & {POW2_MIN, 8, POW2_MAX})
                    if longest is None or G.number_of_nodes() < longest:
                        longest = G.number_of_nodes()
                    if not has_pow2:
                        glued_free.append(
                            (G.number_of_nodes(), g1, g2, canon_g6(G), agree,
                             sorted(glued_set)))
                        say(f"  GLUED pow2-free! order={G.number_of_nodes()} "
                            f"L1={g1} (nH={n1}) L2={g2} (nH={n2}) "
                            f"cycle-set-agrees={agree}")

    say(f"pairs considered: {pair_count}")
    say(f"smallest glued order among all pairs: {longest}")
    say(f"glued pow2-free pairs found: {len(glued_free)}")
    for order, g1, g2, gg6, agree, cs in sorted(glued_free):
        say(f"  order={order} L1={g1} L2={g2} glue={gg6} "
            f"agree={agree} cycles={cs}")

    # dump the glued graphs
    with open(os.path.join(OUTDIR, "glued_pairs.txt"), "w") as f:
        f.write("# glued (2,2) cut-vertex graphs: L1 and L2 pow2-free lobes, "
                "v's identified\n")
        f.write("# columns: glued-order | L1-g6(nH1) | L2-g6(nH2) | glued-g6 | "
                "union-agree(0/1) | glued-cycle-set\n")
        for order, g1, g2, gg6, agree, cs in sorted(glued_free):
            f.write(f"{order} {g1} {g2} {gg6} {1 if agree else 0} "
                    f"{' '.join(map(str, cs))}\n")

    # ---- write the full log ---------------------------------------------
    log.close()
    say("")
    say(f"done.  log: {log_path}")
    say(f"pow2-free lobe list: {os.path.join(OUTDIR, 'pow2free_lobes.txt')}")
    say(f"glued pair list:     {os.path.join(OUTDIR, 'glued_pairs.txt')}")


if __name__ == "__main__":
    main()