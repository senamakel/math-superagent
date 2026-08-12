"""Pure verification oracle for Project Euler 763 (3D amoeba).

Definition: an amoeba at (x,y,z) may divide into three amoebas at
(x+1,y,z), (x,y+1,z), (x,y,z+1) iff all three of those cubes are empty; the
dividing amoeba disappears.  Each division nets +2 amoebas, so after N
divisions there are 2N+1 occupied cubes.  D(N) = number of DISTINCT sets of
occupied cubes reachable after exactly N divisions (a set reachable many ways
counts once).

This is the naive, obviously-correct BFS (brute: forward_level from
lib.amoeba, frozenset-of-tuples states, level = number of divisions).  It is
NOT a solver: exponential state space, only meant for definition checks and
for reporting how far exact BFS can run in this container.

Task points:
  (1) reproduce the worked examples D(2)=3 and D(10)=44499;
  (2) report how far this exact BFS can go here, giving D(0..Nmax) and the
      cap reason (time / frontier-size / memory);
  (3) confirm D(20)=9204559704 is out of reach by brute force, with a
      timing/state-count estimate.
"""

import resource
import time

from lib.amoeba import forward_level

D_EXPECTED = [1, 1, 3, 9, 30, 99, 336, 1134, 3855, 13086,
              44499, 151263, 514419, 1749267, 5949063]

# Hard stops for the exact BFS.  The frontier (number of distinct configs at
# the current level) is the driver of both time and memory: each frozenset of
# 2N+1 tuples costs ~0.5-1 KB, so a frontier of ~6M configs is ~4-6 GB, well
# past this container's 2 GiB cgroup cap.
FRONTIER_CAP = 5_000_000          # stop growing when one level exceeds this
TIME_BUDGET_S = 500                # stop gracefully when wall-time exceeds this


def rss_bytes():
    return resource.getrusage(resource.RUSAGE_SELF).ru_maxrss * 1024


def main():
    start_cell = frozenset({(0, 0, 0)})
    level = {start_cell}          # configs at 'current' number of divisions
    values = []
    t0 = time.time()
    Nmax = 0
    stop_reason = ""

    print(f"frontier cap        = {FRONTIER_CAP:,} configs")
    print(f"time budget         = {TIME_BUDGET_S}s")
    print(f"container mem cgroup check: peak RSS so far {rss_bytes()/1e6:.2f} MB")
    print("-" * 60)
    print("  N          D(N)            frontier    elapsed_s")
    print("-" * 60)

    for N in range(0, 1_000_000):
        d = len(level)
        values.append(d)
        elapsed = time.time() - t0
        print(f"{N:3d}  {d:>14,}  {len(level):>12,}   {elapsed:8.2f}")

        # Confirm the worked examples while we are at it.
        if N == 2:
            assert d == 3, f"D(2)={d}, expected 3"
            print("      -> D(2) == 3  MATCHES worked example")
        if N == 10:
            assert d == 44499, f"D(10)={d}, expected 44499"
            print("      -> D(10) == 44499  MATCHES worked example")

        # Decide whether we can take another division step.
        if N >= 1 and len(level) > FRONTIER_CAP:
            stop_reason = (f"frontier {len(level):,} > cap {FRONTIER_CAP:,} at "
                           f"level {N}")
            break
        if time.time() - t0 > TIME_BUDGET_S:
            stop_reason = f"time budget {TIME_BUDGET_S}s exceeded at level {N}"
            break
        if not level:
            stop_reason = f"no configs at level {N} (impossible)"
            break

        # One exact division step.
        t_step = time.time()
        level = forward_level(level, 3)
        Nmax = N + 1

    elapsed = time.time() - t0
    rss = rss_bytes() / 1e6

    print("-" * 60)
    print(f"exact BFS stopped at D({Nmax}) after {elapsed:.2f}s, "
          f"peak RSS {rss:.0f} MB")
    if stop_reason:
        print(f"cap reason: {stop_reason}")
    else:
        print("cap reason: reached loop end")

    # Report the full computed sequence.
    print("\nComputed D(0..Nmax):")
    print("  " + ", ".join(str(v) for v in values))
    print(f"  (Nmax = {Nmax})")

    # Compare to the known reference list where we have it.
    n_known = min(len(values), len(D_EXPECTED))
    ok = all(values[i] == D_EXPECTED[i] for i in range(n_known))
    print(f"\nReference check against D(0..{n_known - 1}) = {D_EXPECTED[:n_known]}:")
    print("  " + ("MATCH" if ok else "MISMATCH"))
    if ok and n_known == len(D_EXPECTED):
        print("      full reference list D(0..14) reproduced exactly.")
    elif ok:
        print(f"      first {n_known} reference values (up to D({n_known - 1})) "
              "all reproduced; the run stopped before reaching the rest.")

    # Task (3): why D(20) is out of reach by brute force.
    print("\nTask (3) — D(20)=9204559704 unreachable by exact BFS:")
    print("  The frontier (distinct configs at one level) is what matters:")
    print("      N=13 frontier: 1,749,267 configs")
    print("      N=14 frontier: 5,949,063 configs  (~> FRONTIER_CAP, stop)")
    print("  Level N=20 has ~9.2e9 distinct configs (state space ~9.2e9).")
    print("  Storing one frozenset config (~2N+1 tuples, ~0.5-1 KB) gives")
    print("  ~4-6 GB for the 5.9M-config N=14 frontier alone, already past")
    print("  this container's 2 GiB cgroup memory.max.  A 9.2e9-config set")
    print("  would need ~5-9 TB of RAM, and enumerating it would take far")
    print("  longer than any feasible time budget.")
    print("  => D(20) is not reachable by this exact BFS in this container.")


if __name__ == "__main__":
    main()
