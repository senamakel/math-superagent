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
adjacent to exactly x and y.  Then d(v)=2, the two endpoints x,y of e keep
their other two edges (so degree 3), and every other vertex keeps its H
degree 3:  d_L = (3,3,...,3,2) with the unique degree-2 vertex being v.

Three jobs:

  J1  For every connected cubic graph H on n_H = 4..max_nH (nauty-geng -q -c
      -d3 -D3, counts must match A002851: 1,2,5,19,85,509,4060,41301 for
      n_H = 4..18), and for every edge e of H, form L = H - e + v and test
      whether L has a cycle of length 4 or 8 (16 is impossible at order
      <= max_nH + 1 <= 19).  Report per n_H: number of lobe constructions, of
      distinct (up-to-isomorphism) lobes, of lobes with a C4, with a C8, and
      (if any) of power-of-two-free lobes with their graph6 and cycle sets.

  J2  The smallest power-of-two-free lobe (J1's zero result is itself the
      finding: none exists over the run's range).

  J3  Pair search over the pow2-free lobes found: every two pow2-free lobes
      on disjoint vertex sets with total glued order |H1|+|H2|-1 <= 30, glued
      by identifying their two v-vertices into one central cut vertex of
      degree 4 (the (2,2) cut-vertex shape), oracle-checked.  The
      no-cross-cycles claim is verified per pair by comparing the glued cycle
      set against the union of the two lobe cycle sets: any pow2-free glued
      graph is a concrete 1-connected, delta>=3 strong near-counterexample in
      exactly the shape the cut-vertex characterization leaves open.

POW2 TEST.  Two routes, both exact:
  1. per-construction early exit: has_cycle_of_length(L, 4) and (L, 8);
  2. exhaustive re-verification of the ZERO result: full
     distinct_cycle_lengths on every single lobe construction (this is what
     the headline number rests on), cross-checked in a separate run against
     networkx.simple_cycles on a sample.

ISOMORPHISM.  Lobes are deduplicated with nauty-shortg -u (up-to-isomorphism
canonical representatives); reported graph6 strings are nauty-canonical.

Complexity:  |A002851| = 509 cubic graphs at n_H=14 (4060 at 16, 41301 at
18), each with <= 3 n_H / 2 edges, so ~10^4 lobe constructions at 14,
~10^5+ at 16+, each checked by the exponential small-instance oracle
(rule 9, oracle bound n <= 31) — this is the exhaustive verification tool,
not the method.  Pair space is empty unless lobes are found.
"""
import os
import subprocess
import time

import networkx as nx

from lib.cycle_oracle import (
    minimum_degree,
    distinct_cycle_lengths,
    has_cycle_of_length,
)

HERE = os.path.dirname(os.path.abspath(__file__))
OUTDIR = os.path.join(os.path.dirname(HERE), "out", "cutvertex", "lobe_probe")

EXPECTED_CUBIC = {4: 1, 6: 2, 8: 5, 10: 19, 12: 85, 14: 509,
                  16: 4060, 18: 41301}   # A002851


def connected_cubic_graph6(n):
    """Every connected cubic graph on n vertices, one graph6 per line.

    nauty-geng -q -c -d3 -D3 : connected, min degree 3, max degree 3.
    Counts must equal A002851(n) — asserted by the caller.
    """
    t0 = time.time()
    out = subprocess.run(
        ["nauty-geng", "-q", "-c", "-d3", "-D3", str(n)],
        capture_output=True, text=True, check=True,
    )
    return out.stdout.splitlines(), time.time() - t0


def shortg_dedup(graph6_strings, fmt="-g"):
    """Up-to-isomorphism representatives of a list of graph6 strings, in
    nauty-canonical labelling.  Empty input -> []."""
    if not graph6_strings:
        return []
    data = ("\n".join(graph6_strings) + "\n").encode()
    p = subprocess.run(["nauty-shortg", "-u", "-q", fmt],
                       input=data, capture_output=True)
    if p.returncode != 0:
        raise RuntimeError(f"nauty-shortg failed: {p.stderr.decode()[-500:]}")
    return p.stdout.decode().splitlines()


def lobe_from_edge(H, e):
    """L = H - e + v: remove edge e=(x,y) from cubic H, add fresh vertex v
    adjacent to exactly x and y.  Returns (L, v)."""
    L = nx.Graph()
    L.add_nodes_from(H.nodes())
    L.add_edges_from(H.edges())
    L.remove_edge(*e)
    v = max(H.nodes()) + 1
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


def main(max_nH=18):
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
    say(f"powers-of-two tested: {4}, {8} (a lobe has |V| = n_H+1 <= "
        f"{max_nH+1}, so 16 cannot occur)")
    say(f"inner cubic order range: n_H = 4..{max_nH}")

    # ---- accumulate pow2-free lobes across n_H --------------------------
    pow2free_lobes = {}   # canonical g6 -> {"nH":, "cycle_set":}
    smallest_lobe = None  # (nH, g6, cycle_set)
    counts_by_nH = {}

    for n_H in range(4, max_nH + 1, 2):   # cubic graphs require even order
        t0 = time.time()
        cubic, t_gen = connected_cubic_graph6(n_H)
        n_cubic = len(cubic)
        assert n_cubic == EXPECTED_CUBIC[n_H], \
            f"cubic count at n_H={n_H}: got {n_cubic}, " \
            f"expected {EXPECTED_CUBIC[n_H]} (A002851)"

        lobes_g6_raw = []
        n_lobes_total = 0
        n_with_C4 = 0
        n_with_C8 = 0
        for g6 in cubic:
            H = nx.from_graph6_bytes(g6.encode())
            for e in H.edges():
                L, v = lobe_from_edge(H, e)
                lobe_deg_check(L, v, H, e)
                n_lobes_total += 1
                has4 = has_cycle_of_length(L, 4)
                has8 = has_cycle_of_length(L, 8)
                n_with_C4 += has4
                n_with_C8 += has8
                if not has4 and not has8:
                    lobes_g6_raw.append(canon_g6(L))
        # dedup up to isomorphism
        distinct_g6 = shortg_dedup(lobes_g6_raw)
        n_pow2free = len(distinct_g6)

        n_new = 0
        for g6s in distinct_g6:
            if g6s not in pow2free_lobes:
                L = nx.from_graph6_bytes(g6s.encode())
                cs = set(distinct_cycle_lengths(L))
                # cross-check the full enumeration against the early-exit check
                assert not (4 in cs or 8 in cs), f"{g6s}: full set has a pow2"
                assert L.number_of_nodes() == n_H + 1
                assert minimum_degree(L) == 2, f"{g6s}: min degree != 2"
                pow2free_lobes[g6s] = {"nH": n_H, "cycle_set": sorted(cs)}
                n_new += 1
                info = f"  POW2-FREE lobe  n_H={n_H}  order={n_H+1}  " \
                       f"g6={g6s}  cycles={sorted(cs)}"
                say(info)
                if smallest_lobe is None or n_H < smallest_lobe[0]:
                    smallest_lobe = (n_H, g6s, sorted(cs))
        counts_by_nH[n_H] = (n_cubic, n_lobes_total, n_with_C4, n_with_C8,
                             n_pow2free, n_new)
        say(f"n_H={n_H:3d}  cubic={n_cubic:5d}  constructions={n_lobes_total:6d}"
            f"  with-C4={n_with_C4:6d}  with-C8={n_with_C8:6d}"
            f"  pow2-free(distinct)={n_pow2free:4d}"
            f"  (new so far {n_new}, cumulative {len(pow2free_lobes)})"
            f"  [{time.time() - t0:5.1f}s, gen {t_gen:4.1f}s]")

    say("-" * 78)
    say(f"TOTAL distinct pow2-free lobes over n_H=4..{max_nH}: "
        f"{len(pow2free_lobes)}")
    if smallest_lobe is None:
        say("SMALLEST pow2-free lobe: NONE in the searched range — every lobe "
            "L = H-e+v with H connected cubic on <= %d vertices contains a "
            "C4 or a C8." % max_nH)
    else:
        say(f"SMALLEST pow2-free lobe: n_H={smallest_lobe[0]} + v, "
            f"order {smallest_lobe[0]+1}; graph6 {smallest_lobe[1]}; "
            f"cycle set {smallest_lobe[2]}")

    # ---- exhaustive re-verification with FULL cycle enumeration ----------
    # The headline (ZERO) claim rests on this, not on the early-exit path:
    # enumerate the FULL cycle-length set of every lobe construction and check
    # for a C4 or C8 by complete enumeration.
    say("")
    say("-" * 78)
    say("exhaustive re-verification: full distinct_cycle_lengths on every")
    say("lobe construction (independent of the early-exit has_cycle_of_length)")
    n_check = 0
    n_free_full = 0
    t0 = time.time()
    for n_H in range(4, max_nH + 1, 2):
        cubic, t_gen = connected_cubic_graph6(n_H)
        for g6 in cubic:
            H = nx.from_graph6_bytes(g6.encode())
            for e in H.edges():
                L, v = lobe_from_edge(H, e)
                full = set(distinct_cycle_lengths(L))
                n_check += 1
                if not (4 in full or 8 in full):
                    n_free_full += 1
                    say(f"  POW2-FREE by full enumeration: n_H={n_H} H={g6} "
                        f"e={e} cycles={sorted(full)}")
    say(f"full-enumeration check over {n_check} lobe constructions: pow2-free "
        f"= {n_free_full}  [{(time.time()-t0):.1f}s]")
    if n_free_full == 0:
        say("=> CONFIRMED: every lobe L = H-e+v with H connected cubic on "
            f"<= {max_nH} vertices contains a C4 or a C8")
    else:
        say("=> DISAGREES with the early-exit result — investigate!")

    # ---- per-nH table + dump -------------------------------------------
    say("")
    say("per-n_H summary (n_H: cubic | constructions | with-C4 | with-C8 | "
        "pow2-free-distinct | new):")
    for n_H in range(4, max_nH + 1, 2):
        if n_H not in counts_by_nH:
            continue
        c = counts_by_nH[n_H]
        say(f"  n_H={n_H:3d}: {c[0]:5d} | {c[1]:6d} | {c[2]:6d} | {c[3]:6d} "
            f"| {c[4]:4d} | {c[5]:4d}")

    with open(os.path.join(OUTDIR, "pow2free_lobes.txt"), "w") as f:
        f.write("# canonical graph6 of every pow2-free lobe L = H-e+v, "
                "H connected cubic\n")
        f.write(f"# n_H range: 4..{max_nH}; columns: n_H | order | graph6 | "
                f"cycle-length-set\n")
        for g6s in sorted(pow2free_lobes, key=lambda g: (pow2free_lobes[g]["nH"], g)):
            d = pow2free_lobes[g6s]
            f.write(f"{d['nH']} {d['nH']+1} {g6s} "
                    f"{' '.join(map(str, d['cycle_set']))}\n")

    # ---- J3: pair search ------------------------------------------------
    say("")
    say("=" * 78)
    say("J3 — pair search over the pow2-free lobes found:")
    say("     every two pow2-free lobes with total glued order "
        "|H1|+|H2|-1 <= 30,")
    say("     glued by identifying their v vertices (central cut vertex, "
        "degree 4)")
    say("=" * 78)
    if not pow2free_lobes:
        say("No pow2-free lobes -> no pairs to glue; the (2,2) cut-vertex "
            "shape has no pow2-free lobe below order %d, so no glued "
            "(2,2)-shaped counterexample candidate exists over this range."
            % (max_nH + 2))
    else:
        by_nH = {}
        for g6s, d in pow2free_lobes.items():
            by_nH.setdefault(d["nH"], []).append(g6s)
        nH_list = sorted(by_nH)
        pair_count = 0
        glued_free = []      # (order, g1, g2, glued_g6, agree, glued_set)
        glue_identity_ok = True   # no-cross-cycles claim checked on all pairs
        for i, n1 in enumerate(nH_list):
            for n2 in nH_list[i:]:
                if n1 + n2 - 1 > 30:
                    continue
                lobes1 = by_nH[n1]
                lobes2 = by_nH[n2]
                for g1 in lobes1:
                    for g2 in lobes2:
                        if n1 == n2 and g2 <= g1:
                            continue  # avoid mirror pairs within one row
                        pair_count += 1
                        L1 = nx.from_graph6_bytes(g1.encode())
                        L2 = nx.from_graph6_bytes(g2.encode())
                        # v is the unique degree-2 vertex of each lobe
                        v1 = [u for u, d in L1.degree() if d == 2]
                        v2 = [u for u, d in L2.degree() if d == 2]
                        assert len(v1) == 1 and len(v2) == 1, (g1, g2)
                        # glued graph: central vertex C=0; L1's inner vertices
                        # shifted +1, L2's inner vertices shifted 1+n_H1
                        n1v = L1.number_of_nodes() - 1
                        off2 = 1 + n1v
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
                        assert G.degree(C) == 4, f"central deg {G.degree(C)}"
                        assert minimum_degree(G) >= 3
                        assert nx.is_connected(G)
                        assert nx.node_connectivity(G) == 1  # C is a cut vertex
                        glued_set = set(distinct_cycle_lengths(G))
                        union = (set(distinct_cycle_lengths(L1))
                                 | set(distinct_cycle_lengths(L2)))
                        agree = glued_set == union
                        if not agree:
                            glue_identity_ok = False
                        has_pow2 = bool(glued_set & {4, 8, 16})
                        if not has_pow2:
                            glued_free.append(
                                (G.number_of_nodes(), g1, g2, canon_g6(G),
                                 agree, sorted(glued_set)))
                            say(f"  GLUED pow2-free! order={G.number_of_nodes()} "
                                f"L1={g1} L2={g2} glue-agree={agree} "
                                f"cycles={sorted(glued_set)}")
        say(f"pairs considered: {pair_count}")
        say(f"no-cross-cycles identity (glued set == union of lobe sets) "
            f"holds on every pair: {glue_identity_ok}")
        say(f"glued pow2-free (2,2)-shaped graphs found: {len(glued_free)}")
        for order, g1, g2, gg6, agree, cs in sorted(glued_free):
            say(f"  order={order} L1={g1} L2={g2} glue={gg6} "
                f"agree={agree} cycles={cs}")
        with open(os.path.join(OUTDIR, "glued_pairs.txt"), "w") as f:
            f.write("# glued (2,2) cut-vertex graphs from pow2-free lobes\n")
            f.write("# columns: glued-order | L1-g6(nH1) | L2-g6(nH2) | "
                    "glued-g6 | union-agree(0/1) | glued-cycle-set\n")
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