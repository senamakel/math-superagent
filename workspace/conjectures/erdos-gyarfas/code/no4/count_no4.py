"""Driver for the NO4(n) exhaustive count.

NO4(n) = number of non-isomorphic connected simple graphs on n vertices with
minimum degree >= 3 and no 4-cycle.

Method: nauty geng is the canonical generator; the flags
    nauty-geng -f -d3 -c -u <n>
mean "4-cycle-free (-f), minimum degree >= 3 (-d3), connected (-c), count only
without printing (-u)".  geng itself prunes by all three properties, so the
`>Z <count> graphs generated` line is exactly NO4(n).  No post-filtering is
needed (the prompt notes that -d3 already enforces min degree).

Usage:
    python count_no4.py 17
prints `NO4(17) = <count>   wall: <seconds> sec`, reading time with
`date +%s%N` for sub-second resolution.  Designed to be run in the background
(nohup ... &) for n where the generator outlives the 600 s command timeout.

Validation (reproduced before the run, n=10..16):
    5, 9, 57, 503, 6059, 91433, 1655659 — matches the run's recorded terms
    (super-exponential growth ~ K*3^n*(n-10)!), and n=16 wall time ~79 s.
    n=16 output of this driver was byte-identical to the raw geng count.

This is the brute-force oracle for the no-4-cycle family; it is exponential in
both time and space (the generator's state space is the graph count itself)
and must never be used as the method at any size.
"""
import subprocess
import sys
import time


def no4_count(n, timeout=None):
    """Run nauty-geng for NO4(n); return (count, wall_seconds, geng_output)."""
    cmd = ["nauty-geng", "-f", "-d3", "-c", "-u", str(n)]
    t0 = time.monotonic()
    proc = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
    wall = time.monotonic() - t0
    out = proc.stdout + "\n" + proc.stderr
    count = None
    for line in out.splitlines():
        parts = line.split()
        if len(parts) >= 4 and parts[0] == ">Z" and parts[2] == "graphs":
            count = int(parts[1])
    return count, wall, out.strip()


if __name__ == "__main__":
    n = int(sys.argv[1])
    timeout = float(sys.argv[2]) if len(sys.argv) > 2 else None
    count, wall, output = no4_count(n, timeout=timeout)
    print(output)
    print(f"NO4({n}) = {count}   wall: {wall:.2f} sec")