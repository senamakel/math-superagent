"""Driver testing the PE620 meshing model in lib/gears.py against the oracle.

Oracle values (Problem statement, /workspace/problem.md):
    g(16,5,5,6) = 9
    G(16)       = 9
    G(20)       = 205

Runs, from /workspace/code so  `from lib.gears import ...`  works:
  1. g_count(16,5,5,6)   -- must equal 9
  2. G_sum(16)           -- must equal 9
  3. G_sum(20)           -- must equal 205
plus each (c,s,p,q) pair appearing in G(16) and G(20) individually, to show
the distribution of g values.  Prints agree/disagree verdicts and wall-clock
times, and saves the full output to /workspace/code/out/oracle_test.txt.

Model under test: for fixed (c,s,p,q) each planet centre is forced to one of
the 0/1/2 two-circle intersection points, so an arrangement is determined by
the centre distance d; g_count brute-forces the continuous d interval,
isolating residual zeros of the phase-eliminated meshing conditions
(2F_p, 2F_q, H all integers mod 1).  Rebound cost: O(N) grid evaluations per
(c,s,p,q) plus a bounded refine per candidate run; N=400000 fixed.
"""
import sys
import time


def main():
    from lib.gears import g_count, G_sum

    out_lines = []
    def emit(s=""):
        print(s)
        out_lines.append(s)

    def wallclock(fn, *args, **kwargs):
        t0 = time.perf_counter()
        result = fn(*args, **kwargs)
        return result, time.perf_counter() - t0

    emit("PE 620 oracle test of lib/gears.py meshing model")
    emit("=" * 60)

    # ---- 1. g(16,5,5,6) must be 9 ------------------------------------
    g, dt = wallclock(g_count, 16, 5, 5, 6, grid_points=400000)
    emit(f"[1] g_count(16,5,5,6) = {g}   (oracle 9)   "
         f"{'AGREE' if g == 9 else 'DISAGREE'}   [{dt:.2f}s]")

    # ---- 2. G(16) must be 9 ------------------------------------------
    gsum16, dt16 = wallclock(G_sum, 16)
    n16 = len(gsum16[1])
    emit(f"[2] G_sum(16) = {gsum16[0]}   (oracle 9, over {n16} pairs)   "
         f"{'AGREE' if gsum16[0] == 9 else 'DISAGREE'}   [{dt16:.2f}s]")

    # ---- 3. G(20) must be 205 ----------------------------------------
    gsum20, dt20 = wallclock(G_sum, 20)
    n20 = len(gsum20[1])
    emit(f"[3] G_sum(20) = {gsum20[0]}   (oracle 205, over {n20} pairs)   "
         f"{'AGREE' if gsum20[0] == 205 else 'DISAGREE'}   [{dt20:.2f}s]")

    # ---- per-pair distribution for every pair in G(20) ---------------
    emit("")
    emit("Per-pair g values, every (c,s,p,q) with s+p+q <= 20, s>=5, p>=5, p<q:")
    emit(f"{'c':>3} {'s':>3} {'p':>3} {'q':>3} {'g':>5}")
    for (c, s, p, q, gv) in gsum20[1]:
        emit(f"{c:>3} {s:>3} {p:>3} {q:>3} {gv:>5}")

    # ---- verdict ------------------------------------------------------
    emit("")
    v1 = "AGREE" if g == 9 else "DISAGREE"
    v2 = "AGREE" if gsum16[0] == 9 else "DISAGREE"
    v3 = "AGREE" if gsum20[0] == 205 else "DISAGREE"
    emit("Verdicts: g(16,5,5,6)=9 -> %s | G(16)=9 -> %s | G(20)=205 -> %s"
         % (v1, v2, v3))
    all_ok = (v1 == v2 == v3 == "AGREE")
    emit("MODEL %s the oracle on all three values."
         % ("MATCHES" if all_ok else "DOES NOT MATCH"))

    with open("/workspace/code/out/oracle_test.txt", "w") as f:
        f.write("\n".join(out_lines) + "\n")
    emit("")
    emit("Output saved to /workspace/code/out/oracle_test.txt")


if __name__ == "__main__":
    sys.exit(main())