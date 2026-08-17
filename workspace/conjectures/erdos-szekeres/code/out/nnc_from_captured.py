#!/usr/bin/env python3
"""Derive the non-convex-4-subset counts NNC(N) of the verified es_construct
template from ALREADY-CAPTURED convex-4 counts (no new geometry run):

  convex-4 rows (captures on disk, EXIT 0, exact oracle):
    n=5 N=8   : 38   (code/out/convex_spectrum.captured.txt)
    n=6 N=16  : 1119 (code/out/convex_spectrum.captured.txt)
    n=7 N=32  : 23220(code/out/convex_spectrum.captured.txt)
    n=8 N=64  : 422186(code/out/convex_spectrum_n8_k4.captured.txt)

NNC(N) = C(N,4) - convex4(N).  Then the covering-ratio test that the open
queued task con4-supersat-nnc-count asks as its FIRST step:

  an n-avoiding set must satisfy  NNC(N) * C(N-4, n-4) >= C(N, n)
  (count incidences (n-subset, non-convex-4-subset): every n-subset of an
   n-avoiding set contains at least one non-convex 4-subset, else it is a
   convex n-gon by the 4-point criterion).

Exact integer arithmetic only (math.comb)."""
from math import comb

# captured convex-4 counts, with capture provenance
CONV4 = {
    5: (8, 38, "convex_spectrum.captured.txt"),
    6: (16, 1119, "convex_spectrum.captured.txt"),
    7: (32, 23220, "convex_spectrum.captured.txt"),
    8: (64, 422186, "convex_spectrum_n8_k4.captured.txt"),
}

print("=== NNC(N) = C(N,4) - convex4(N) on es_construct, from captured rows ===")
nnc = {}
for n in sorted(CONV4):
    N, c4, src = CONV4[n]
    total = comb(N, 4)
    nc = total - c4
    nnc[n] = nc
    print(f"n={n} N={N}: C(N,4)={total}  convex4={c4} (capture {src})  "
          f"NNC={nc}  NNC/C(N,4)={nc/total:.4f}")

print("\nNNC sequence n=5..8:", [nnc[n] for n in sorted(nnc)])

print("\n=== covering-ratio test at the extremal N=2^{n-2} (n=5,6,7,8) ===")
print("n-avoiding requires NNC*C(N-4,n-4) >= C(N,n); ratio = NNC*C(N-4,n-4)/C(N,n)")
for n in sorted(CONV4):
    N = CONV4[n][0]
    nc = nnc[n]
    inc = nc * comb(N - 4, n - 4)
    tot = comb(N, n)
    ratio = inc / tot
    print(f"n={n} N={N}: NNC*C({N-4},{n-4})={inc}  C({N},{n})={tot}  "
          f"hold={inc>=tot}  ratio={ratio:.3f}")

# out-of-sample note: at N=2^{n-2}+1 the test needs NNC at N+1, which the run
# has not computed (no convex-4 count at N+1 on disk).  State plainly.
print("\nAt N=2^{n-2}+1 the test needs NNC(N+1), which is not on disk: "
      "no convex-4 count at N+1 exists in any capture. Not asserted either way.")
print("EXIT: 0")