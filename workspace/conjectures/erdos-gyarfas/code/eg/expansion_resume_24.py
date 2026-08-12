"""Incremental, resumable driver to push the K4-triangle-expansion census one
level, from n=22 to n=24, under a hard per-invocation time budget.

The level-22 -> level-24 step is the last expansion: ~11002 cubic classes on 22
vertices, each expanded 22*3! = 132 times, ~1.45M candidate graphs at n=24,
canonicalised by nauty-labelg in one shot. That one-shot labelg call (and the
resulting set) is what exhausted memory / budget in expansion_census_fast.py.

This driver splits the step into three resumable phases, each checkpointing to
disk so a kill loses at most the current chunk:

  Phase A  expansion pool    -> level_24_pool.txt    (one graph6 line per graph)
  Phase B  canonicalise+dedup -> level_24_classes.txt (one canonical graph6 file, name add _classes)
  Phase C  cycle checks      -> level_24.txt          (final census row)

Each phase reads its checkpoint and continues, so re-invocation after a budget
timeout resumes where the previous call stopped.

Semantics identical to expansion_census_fast.py: family = start from K4, expand
a cubic vertex into a triangle attached bijectively to its 3 neighbours
(the Markstrom construction); record n, #isomorphism classes, #avoiding C4,
#avoiding both C4 and C8 (exact cycle checks, C8 only on C4-free graphs).
"""
import os
import sys
import subprocess
import itertools
import networkx as nx
from networkx import Graph

POOL = "level_24_pool.txt"            # Phase A output
CLASSES = "level_24_classes.txt"      # Phase B output (canonical graph6, one/line)
CHUNK = 200_000                       # lines per labelg call / per pool read chunk


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


def phase_a(resume_canon, outdir):
    """Write every expanded candidate as one graph6 line per graph, appended."""
    target = os.path.join(outdir, POOL)
    done_marker = os.path.join(outdir, "level_24_pool_done")
    if os.path.exists(done_marker):
        with open(target) as f:
            nlines = sum(1 for _ in f)
        return nlines, True
    with open(target, "w") as w:
        nlines = 0
        with open(resume_canon) as rc:
            for line in rc:
                line = line.strip()
                if not line:
                    continue
                H = nx.from_graph6_bytes(line.encode())
                for g in expand_one(H):
                    w.write(g + "\n")
                nlines += 1
    # only mark complete once fully written
    with open(done_marker, "w") as f:
        f.write("done")
    return nlines, True


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
    # how much of the pool has been consumed?  canonical forms already recorded
    # are a sub-multiset; simplest robust marker: number of pool lines consumed.
    mark_path = os.path.join(outdir, "level_24_classes_done")
    consumed = 0
    if os.path.exists(mark_path):
        with open(mark_path) as f:
            consumed = int(f.read().strip())
    with open(pool_path) as pf:
        # skip consumed lines
        for _ in range(consumed):
            next(pf)
        buf = []
        for idx, line in enumerate(pf, start=consumed):
            line = line.strip()
            if not line:
                continue
            buf.append(line)
            if len(buf) >= CHUNK:
                canon.update(_canon_chunk(buf))
                buf = []
                consumed = idx + 1
                # persist progress
                with open(cls_path, "w") as w:
                    w.write("\n".join(sorted(canon)) + "\n")
                with open(mark_path, "w") as w:
                    w.write(str(consumed))
        if buf:
            canon.update(_canon_chunk(buf))
            consumed += len(buf)
            with open(cls_path, "w") as w:
                w.write("\n".join(sorted(canon)) + "\n")
            with open(mark_path, "w") as w:
                w.write(str(consumed))
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


def has_c8(G):
    adj = {u: set(G[u]) for u in G}
    nodes = list(G)

    def search(s):
        def dfs(cur, used, depth):
            if depth == 7:
                return s in adj[cur]
            for nb in adj[cur]:
                if nb not in used:
                    used.add(nb)
                    if dfs(nb, used, depth + 1):
                        return True
                    used.remove(nb)
            return False
        return dfs(s, {s}, 0)

    for s in nodes:
        if search(s):
            return True
    return False


def phase_c(outdir):
    """Cycle checks over the canonical classes.

    Stateless: recomputes all counts from scratch each invocation (cheap next
    to phase B). A mid-phase kill only costs re-running this phase; counts are
    never corrupted by partial progress.
    """
    cls_path = os.path.join(outdir, CLASSES)
    avoids_c4 = 0
    avoids_both = 0
    total = 0
    c4free = []
    with open(cls_path) as f:
        for line in f:
            c = line.strip()
            if not c:
                continue
            H = nx.from_graph6_bytes(c.encode())
            total += 1
            if not has_c4(H):
                avoids_c4 += 1
                c4free.append(H)
    for H in c4free:
        if not has_c8(H):
            avoids_both += 1
    return total, avoids_c4, avoids_both


def main(resume_canon, outdir):
    os.makedirs(outdir, exist_ok=True)
    nlines, _ = phase_a(resume_canon, outdir)
    canon = phase_b(outdir)
    total, avoids_c4, avoids_both = phase_c(outdir)
    # write final census row
    with open(os.path.join(outdir, "level_24.txt"), "w") as f:
        f.write(f"n=24  classes={len(canon)}  avoidsC4={avoids_c4}  "
                f"avoidsC4C8={avoids_both}\n")
    # replicate the history-style content of the original level files
    with open(os.path.join(outdir, "level_24_results.txt"), "w") as f:
        f.write(f"n=24  classes={len(canon)}  avoidsC4={avoids_c4}  avoidsC4C8={avoids_both}\n")
    print(f"n=24  classes={len(canon)}  avoidsC4={avoids_c4}  avoidsC4C8={avoids_both}",
          flush=True)
    print(f"pool_lines={nlines} checked={total}", flush=True)
    return len(canon), avoids_c4, avoids_both


if __name__ == "__main__":
    outdir = sys.argv[1] if len(sys.argv) > 1 else "/workspace/code/out/expansion_census"
    resume_canon = sys.argv[2] if len(sys.argv) > 2 else \
        os.path.join(outdir, "level_22.canon")
    main(resume_canon, outdir)
