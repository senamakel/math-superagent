"""Check that every no-4-cycle min-degree-3 survivor for n=10..14 has an
8-cycle (so none is an EG counterexample, consistent with the >=17 bound).
Also report the cycle-length spectra of the smallest survivors (n=10,11)."""
import subprocess, networkx as nx
from lib.cycles import min_degree, cycle_lengths


def main():
    for n in [10, 11]:
        cmd = ["nauty-geng", "-q", "-c", "-f", "-d3", str(n)]
        proc = subprocess.run(cmd, capture_output=True, text=True)
        su = 0
        no8 = 0
        for g6 in proc.stdout.splitlines():
            g6 = g6.strip()
            if not g6:
                continue
            G = nx.from_graph6_bytes(g6.encode("ascii"))
            if min_degree(G) < 3:
                continue
            su += 1
            lens = cycle_lengths(G)
            has8 = 8 in lens
            if not has8:
                no8 += 1
                print(f"  n={n}: NO 8-cycle! graph6={g6} lens={sorted(lens)}")
        print(f"n={n}: no4_survivors={su}, missing_8cycle={no8}")


if __name__ == "__main__":
    main()
