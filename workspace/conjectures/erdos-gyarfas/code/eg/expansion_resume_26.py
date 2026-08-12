"""Incremental, resumable driver to push the K4-triangle-expansion census one
more level, from n=24 to n=26, under a hard per-invocation time budget.

The level-24 -> level-26 step expands ~58713 cubic classes on 24 vertices,
each into 24*3! = 144 candidates, ~8.45M pool graphs at n=26, canonicalised by
nauty-labelg and deduplicated. This driver splits the step into three resumable
phases, each checkpointing to disk so a kill loses at most the current chunk:

  Phase A  expansion pool     -> level_26_pool.txt    (one graph6 line per graph)
  Phase B  canonicalise+dedup -> level_26_classes.txt (canonical graph6, one/line)
  Phase C  cycle profile      -> level_26_results.txt (final census row)

Semantics identical to expansion_resume_24.py / expansion_census_fast.py:
family = start from K4, expand a cubic vertex into a triangle attached
bijectively to its 3 neighbours (the Markstrom construction). All members are
cubic. Phase A is parallelised over the 28-core container; phase B is a
chunked labelg canonicalisation (nearly free); phase C computes the full
power-of-two profile:

  total         : number of isomorphism classes (= A027610 12th term; expect 321776)
  avoidsC4      : no 4-cycle
  avoidsC4C8    : no 4- and no 8-cycle         (expect 0; family's only C4,C8-free member is at n=24)
  avoidsC4C16   : no 4- and no 16-cycle        (the C16 cliff test: 0 => cliff survives)
  avoidsC4C8C16 : no 4, 8, or 16-cycle         (expect 0)
  c4free_hasC8_notC16 : C4-free members that have an 8-cycle but no 16-cycle

Exact cycle checks: has_c4 via common-neighbour test O(n^2 deg); has_c8 and
has_c16 via the exact bounded-DFS has_closed_cycle(G, L) from
pattern_finder/census_c16_profile.py.
"""
import os
import sys
import time
import subprocess
import itertools
import multiprocessing as mp
from networkx import Graph
import networkx as nx

POOL = "level_26_pool.txt"
CLASSES = "level_26_classes.txt"
POOL_DONE = "level_26_pool_done"      # number of classes whose pool lines are written
CLASSES_DONE = "level_26_classes_done"  # number of pool lines consumed
CHUNK = 200_000                        # lines per labelg call / pool append chunk
NPROC = max(1, min(mp.cpu_count(), 28))


def expand_one(H):
    """All graphs from cubic H by one vertex-into-triangle expansion (graph6 lines)."""
    out = []
    for v in list(H.nodes()):
        nbrs = list(H[v])
        base = list(H.nodes()) + ["x", "y", "z"]
        for perm in itertools.permutations(nbrs):
            G = Graph()
            G.add_nodes_from(base)
            for u, w in H.edges():
                if u == v or w == v:
                    continue
                G.add_edge(u, w)
            x, y, z = "x", "y", "z"
            G.add_edges_from([(x, y), (y, z), (x, z)])
            for nb, tri in zip(perm, [x, y, z]):
                G.add_edge(nb, tri)
            G.remove_node(v)
            out.append(nx.to_graph6_bytes(G, header=False).decode().strip())
    return out


def _expand_line(line):
    """Worker: one class line -> list of expanded graph6 lines (for mp.Pool)."""
    H = nx.from_graph6_bytes(line.strip().encode())
    return expand_one(H)


def phase_a(src_classes, outdir):
    """Write every expanded candidate as one graph6 line per graph, appended.

    Parallelised across NPROC workers. Checkpoint: POOL_DONE records how many
    source classes have been fully written; a resumed call skips them.
    """
    target = os.path.join(outdir, POOL)
    done_marker = os.path.join(outdir, POOL_DONE)
    done = 0
    if os.path.exists(done_marker):
        with open(done_marker) as f:
            done = int(f.read().strip())
    if done >= len(src_classes):
        with open(target) as f:
            lines_written = sum(1 for _ in f)
        return lines_written, True

    append_mode = "a" if done > 0 else "w"
    with open(target, append_mode) as w:
        with open(src_classes) as rc:
            for _ in range(done):
                next(rc)
            rest = [l.strip() for l in rc if l.strip()]
        # process rest in batches; write + checkpoint each batch (chunk of classes)
        batch = 400
        with mp.Pool(NPROC) as pool:
            for i in range(0, len(rest), batch):
                chunk = rest[i:i + batch]
                t0 = time.time()
                results = pool.map(_expand_line, chunk)
                nb = 0
                for r in results:
                    for g in r:
                        w.write(g + "\n")
                        nb += 1
                done += len(chunk)
                with open(done_marker, "w") as f:
                    f.write(str(done))
                w.flush()
                print(f"  pool: {done}/{len(src_classes)} classes, {nb} lines, "
                      f"{time.time()-t0:.1f}s", flush=True)
        if done >= len(src_classes):
            with open(done_marker, "w") as f:
                f.write(str(done))
    with open(target) as f:
        lines_written = sum(1 for _ in f)
    return lines_written, True


def _canon_chunk(lines):
    """Canonical graph6 of `lines` (strings), order preserved, one labelg call."""
    inp = "\n".join(lines) + "\n"
    proc = subprocess.run(["nauty-labelg", "-q"], input=inp,
                          capture_output=True, text=True)
    if proc.returncode != 0:
        raise RuntimeError(f"labelg failed: {proc.stderr}")
    out = [ln.strip() for ln in proc.stdout.splitlines() if ln.strip()]
    assert len(out) == len(lines), (len(out), len(lines), proc.stderr)
    return out


def phase_b(outdir):
    """Canonicalise pool in chunks, accumulate canonical set on disk incrementally."""
    pool_path = os.path.join(outdir, POOL)
    cls_path = os.path.join(outdir, CLASSES)
    canon = set()
    if os.path.exists(cls_path):
        with open(cls_path) as f:
            for l in f:
                l = l.strip()
                if l:
                    canon.add(l)
    mark_path = os.path.join(outdir, CLASSES_DONE)
    consumed = 0
    if os.path.exists(mark_path):
        with open(mark_path) as f:
            consumed = int(f.read().strip())
    with open(pool_path) as pf:
        for _ in range(consumed):
            next(pf)
        buf = []
        for idx, line in enumerate(pf, start=consumed):
            line = line.strip()
            if not line:
                continue
            buf.append(line)
            if len(buf) >= CHUNK:
                t0 = time.time()
                canon.update(_canon_chunk(buf))
                buf = []
                consumed = idx + 1
                with open(cls_path, "w") as w:
                    w.write("\n".join(sorted(canon)) + "\n")
                with open(mark_path, "w") as w:
                    w.write(str(consumed))
                print(f"  canon: consumed {consumed} pool lines, "
                      f"{len(canon)} classes, {time.time()-t0:.1f}s", flush=True)
        if buf:
            canon.update(_canon_chunk(buf))
            consumed += len(buf)
            with open(cls_path, "w") as w:
                w.write("\n".join(sorted(canon)) + "\n")
            with open(mark_path, "w") as w:
                w.write(str(consumed))
            print(f"  canon: final consumed {consumed}, {len(canon)} classes", flush=True)
    return canon


def has_c4(G):
    nodes = list(G.nodes())
    for i in range(len(nodes)):
        u = nodes[i]
        for j in range(i + 1, len(nodes)):
            v = nodes[j]
            common = set(G[u]) & set(G[v])
            if len(common) >= 2:
                return True
    return False


def has_closed_cycle(G, L):
    """Exact: does G contain a simple cycle of length L? (bounded simple DFS)"""
    adj = {u: set(G[u]) for u in G}

    def search(s):
        def dfs(cur, used, depth):
            if depth == L - 1:
                return s in adj[cur]
            for nb in adj[cur]:
                if nb not in used:
                    used.add(nb)
                    if dfs(nb, used, depth + 1):
                        return True
                    used.remove(nb)
            return False
        return dfs(s, {s}, 0)

    for s in G:
        if search(s):
            return True
    return False


def phase_c(outdir):
    """Full power-of-two profile over the canonical classes.

    Stateless: recomputes all counts from scratch each invocation (cheap next
    to phase A/B). A mid-phase kill only costs re-running this phase.
    """
    cls_path = os.path.join(outdir, CLASSES)
    total = avoids_c4 = avoids_c4c8 = avoids_c4c16 = avoids_c4c8c16 = 0
    c4free_hasC8_notC16 = 0
    with open(cls_path) as f:
        for line in f:
            c = line.strip()
            if not c:
                continue
            H = nx.from_graph6_bytes(c.encode())
            total += 1
            h4 = has_c4(H)
            if h4:
                continue
            avoids_c4 += 1
            h8 = has_closed_cycle(H, 8)
            h16 = has_closed_cycle(H, 16)
            if not h8:
                avoids_c4c8 += 1
            if not h16:
                avoids_c4c16 += 1
            if not h8 and not h16:
                avoids_c4c8c16 += 1
            if h8 and not h16:
                c4free_hasC8_notC16 += 1
    return dict(total=total, avoidsC4=avoids_c4, avoidsC4C8=avoids_c4c8,
                avoidsC4C16=avoids_c4c16, avoidsC4C8C16=avoids_c4c8c16,
                c4free_hasC8_notC16=c4free_hasC8_notC16)


def main(src_classes, outdir):
    os.makedirs(outdir, exist_ok=True)
    t_start = time.time()
    pool_lines, _ = phase_a(src_classes, outdir)
    t_a = time.time()
    canon = phase_b(outdir)
    t_b = time.time()
    prof = phase_c(outdir)
    t_c = time.time()
    res = [f"n=26  classes={prof['total']}  avoidsC4={prof['avoidsC4']}  "
           f"avoidsC4C8={prof['avoidsC4C8']}  avoidsC4C16={prof['avoidsC4C16']}  "
           f"avoidsC4C8C16={prof['avoidsC4C8C16']}  "
           f"c4free_hasC8_notC16={prof['c4free_hasC8_notC16']}\n"]
    with open(os.path.join(outdir, "level_26_results.txt"), "w") as f:
        f.writelines(res)
    with open(os.path.join(outdir, "level_26.txt"), "w") as f:
        f.writelines(res)
    print("n=26  classes=%d  avoidsC4=%d  avoidsC4C8=%d  avoidsC4C16=%d  "
          "avoidsC4C8C16=%d  c4free_hasC8_notC16=%d"
          % (prof['total'], prof['avoidsC4'], prof['avoidsC4C8'],
             prof['avoidsC4C16'], prof['avoidsC4C8C16'],
             prof['c4free_hasC8_notC16']), flush=True)
    print(f"pool_lines={pool_lines}  checked={prof['total']}  "
          f"phaseA={t_a-t_start:.1f}s  phaseB={t_b-t_a:.1f}s  phaseC={t_c-t_b:.1f}s  "
          f"total={t_c-t_start:.1f}s", flush=True)
    return prof


if __name__ == "__main__":
    src = sys.argv[1] if len(sys.argv) > 1 else \
        "/workspace/code/out/expansion_census/level_24_classes.txt"
    outdir = sys.argv[2] if len(sys.argv) > 2 else \
        "/workspace/code/out/expansion_census_26"
    main(src, outdir)
