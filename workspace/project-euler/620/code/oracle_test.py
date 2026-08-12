"""Driver testing the PE620 meshing model in lib/gears.py against the oracle.

Oracle values (Problem statement, /workspace/problem.md):
    g(16,5,5,6) = 9
    G(16)       = 9
    G(20)       = 205

Runs, from /workspace/code so  `from lib.gears import ...`  works:
  1. g_count(16,5,5,6)   -- must equal 9        (full 400000-grid resolution)
  2. G(16) summed per-pair                      
  3. G(20) summed per-pair                      
plus each (c,s,p,q) pair in G(16)/G(20) individually to show the distribution.

The task asks to use g_count / G_sum from the module, so the verdict calls use
those names when they fit the budget.  G_sum(16) has just 1 pair and is called
directly at the default grid.  G_sum(20) has 22 pairs and at the default
400000 grid is too slow for the 600s tool cap, so its pairs are enumerated and
g_count is called per pair at grid_points=50000, labelled explicitly.  The grid
resolution is only a numeric scan parameter, not part of the model logic; the
single primary case is run at the full default resolution.

Model under test: for fixed (c,s,p,q) each planet centre is forced to one of
the 0/1/2 two-circle intersection points, so an arrangement is determined by
the centre distance d; g_count brute-forces the continuous d interval,
isolating residual zeros of the phase-eliminated meshing conditions
(2F_p, 2F_q, H all integers mod 1).  Rebound cost O(N) grid evaluations per
pair plus a bounded refine per candidate run.
"""
import sys
import time

ORACLE_FILE = "/workspace/code/out/oracle_test.txt"


def main():
    from lib.gears import g_count, G_sum

    out_lines = []
    def emit(s=""):
        print(s, flush=True)
        out_lines.append(s)

    def save():
        with open(ORACLE_FILE, "w") as f:
            f.write("\n".join(out_lines) + "\n")

    def wallclock(fn, *args, **kwargs):
        t0 = time.perf_counter()
        result = fn(*args, **kwargs)
        return result, time.perf_counter() - t0

    emit("PE 620 oracle test of lib/gears.py meshing model")
    emit("=" * 60)

    # ---- 1. g(16,5,5,6) must be 9 (full resolution) ------------------
    g, dt = wallclock(g_count, 16, 5, 5, 6, grid_points=400000)
    emit(f"[1] g_count(16,5,5,6) = {g}   (oracle 9)   "
         f"{'AGREE' if g == 9 else 'DISAGREE'}   [{dt:.2f}s]")
    save()

    # ---- 2. G(16) must be 9 ------------------------------------------
    gsum16, dt16 = wallclock(G_sum, 16)
    emit(f"[2] G_sum(16) = {gsum16[0]}   (oracle 9, over {len(gsum16[1])} pair)   "
         f"{'AGREE' if gsum16[0] == 9 else 'DISAGREE'}   [{dt16:.2f}s]")
    save()

    # ---- 3. G(20) must be 205, per pair at grid 50000 ----------------
    rows20 = []
    g20 = 0
    t0 = time.perf_counter()
    emit("[3] G(20) pairs (g_count per pair, grid_points=50000):")
    emit(f"{'c':>3} {'s':>3} {'p':>3} {'q':>3} {'g':>5}")
    for s in range(5, 20 - 10):
        for p in range(5, 20 - s - 5):
            for q in range(p + 1, 20 - s - p + 1):
                c = s + p + q
                gv, dtt = wallclock(g_count, c, s, p, q, grid_points=50000)
                emit(f"{c:>3} {s:>3} {p:>3} {q:>3} {gv:>5}   [{dtt:.1f}s]")
                rows20.append((c, s, p, q, gv))
                g20 += gv
                save()   # flush incrementally so a timeout loses nothing
    dt20 = time.perf_counter() - t0
    emit(f"[3] G(20) per-pair sum = {g20}   (oracle 205, over {len(rows20)} pairs, "
         f"grid 50000)   {'AGREE' if g20 == 205 else 'DISAGREE'}   [{dt20:.1f}s]")
    save()

    # ---- verdicts -----------------------------------------------------
    v1 = "AGREE" if g == 9 else "DISAGREE"
    v2 = "AGREE" if gsum16[0] == 9 else "DISAGREE"
    v3 = "AGREE" if g20 == 205 else "DISAGREE"
    emit("")
    emit("Verdicts: g(16,5,5,6)=9 -> %s | G(16)=9 -> %s | G(20)=205 -> %s"
         % (v1, v2, v3))
    all_ok = (v1 == v2 == v3 == "AGREE")
    emit("MODEL %s the oracle on all three values."
         % ("MATCHES" if all_ok else "DOES NOT MATCH"))
    save()
    emit("")
    emit(f"Output saved to {ORACLE_FILE}")


if __name__ == "__main__":
    sys.exit(main())