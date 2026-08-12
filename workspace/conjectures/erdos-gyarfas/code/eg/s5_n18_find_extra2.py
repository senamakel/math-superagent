"""Find exactly the S5(18) survivors that are NOT 3-connected (the 3 extras
over A366224). Stage 1: cheap articulation scan (not even 2-connected).
Stage 2: remove-each-vertex scan (2-connected but not 3-connected),
results written incrementally to /workspace/code/out/n18_extra.txt."""
import subprocess, networkx as nx, time, os

def main():
    n = 18
    cmd = ["nauty-geng", "-q", "-c", "-d3", "-t", "-f", str(n)]
    proc = subprocess.run(cmd, capture_output=True, text=True)
    lines = [l.strip() for l in proc.stdout.splitlines() if l.strip()]
    print(f"S5(18) total: {len(lines)}", flush=True)

    # Stage 1: not 2-connected (has articulation point)
    not2c = []
    t0 = time.time()
    for g6 in lines:
        G = nx.from_graph6_bytes(g6.encode("ascii"))
        if list(nx.articulation_points(G)):
            not2c.append(g6)
    print(f"not-2-connected: {len(not2c)}  ({time.time()-t0:.0f}s)", flush=True)
    for g6 in not2c:
        print("  NOT2CONN:", g6, flush=True)

    # Stage 2: 2-connected but not 3-connected (G-v not 2-connected for some v)
    out = open("/workspace/code/out/n18_extra.txt", "w")
    t0 = time.time()
    found = 0
    for i, g6 in enumerate(lines):
        G = nx.from_graph6_bytes(g6.encode("ascii"))
        if list(nx.articulation_points(G)):
            continue
        for u in list(G.nodes()):
            H = G.copy(); H.remove_node(u)
            if not nx.is_connected(H) or list(nx.articulation_points(H)):
                out.write(g6 + "\n")
                out.flush()
                found += 1
                break
        if (i + 1) % 20000 == 0:
            print(f"  scanned {i+1}/{len(lines)}, found {found} ({time.time()-t0:.0f}s)", flush=True)
    out.close()
    print(f"stage2 done: {found} non-3-connected survivors ({time.time()-t0:.0f}s)", flush=True)

if __name__ == "__main__":
    main()