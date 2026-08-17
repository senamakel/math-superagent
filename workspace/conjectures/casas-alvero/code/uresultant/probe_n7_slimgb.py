"""Try Singular slimgb at n=7 (route A alternative): slimgb is often an order
of magnitude faster than std on such polynomial ideals. Wall-capped at 450 s;
hitting the cap confirms the vdim-route boundary at n=7 independently of the
std engine."""
import subprocess, tempfile, os, time
import sys

sys.path.insert(0, "/workspace/code/uresultant")
from extend_n7_capture import slice_resultants, to_singular

n = 7
R = slice_resultants(n)
vars_ = ",".join(f"a{j}" for j in range(2, n + 1))
script = (
    f"ring R = 0, ({vars_}), dp;\n"
    "ideal I = " + ", ".join(to_singular(r, n) for r in R) + ";\n"
    "ideal G = slimgb(I);\n"
    '"KRULLDIM = " + string(dim(G));\n'
    '"VDIM = " + string(vdim(G));\n'
    '"GB_SIZE = " + string(size(G));\n'
)
fd, path = tempfile.mkstemp(suffix=".sing", dir="/workspace/code/out")
with os.fdopen(fd, "w") as fh:
    fh.write(script)

WALL_CAP = 450
t0 = time.time()
try:
    proc = subprocess.run(["Singular", "-q", path], capture_output=True,
                          text=True, timeout=WALL_CAP)
    dt = time.time() - t0
    print(f"Singular slimgb n=7 finished in {dt:.1f}s (exit {proc.returncode})")
    for line in proc.stdout.splitlines():
        if line.startswith("KRULLDIM") or line.startswith("VDIM") \
           or line.startswith("GB_SIZE"):
            print(line)
    if proc.stderr:
        print("STDERR:", proc.stderr[-800:])
except subprocess.TimeoutExpired:
    dt = time.time() - t0
    print(f"Singular slimgb n=7 EXCEEDED {WALL_CAP}s cap ({dt:.1f}s elapsed)")
finally:
    os.unlink(path)