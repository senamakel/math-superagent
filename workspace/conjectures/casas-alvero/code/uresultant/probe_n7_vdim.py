"""Measure Singular vdim alone at n=7 (route A of extend_n7_capture.py),
so the n=7 extension's measured boundary can be recorded without a 600s
tool timeout. Wall-capped at 400s: hitting the cap is the boundary result."""
import subprocess, tempfile, os, time
sys_path = "/workspace/code/uresultant"
import sys
if sys_path not in sys.path:
    sys.path.insert(0, sys_path)
from extend_n7_capture import slice_resultants, to_singular

n = 7
R = slice_resultants(n)
vars_ = ",".join(f"a{j}" for j in range(2, n + 1))
script = (
    f"ring R = 0, ({vars_}), dp;\n"
    "ideal I = " + ", ".join(to_singular(r, n) for r in R) + ";\n"
    "ideal G = std(I);\n"
    '"KRULLDIM = " + string(dim(G));\n'
    '"VDIM = " + string(vdim(G));\n'
)
fd, path = tempfile.mkstemp(suffix=".sing", dir="/workspace/code/out")
with os.fdopen(fd, "w") as fh:
    fh.write(script)

WALL_CAP = 400
t0 = time.time()
try:
    proc = subprocess.run(["Singular", "-q", path], capture_output=True,
                          text=True, timeout=WALL_CAP)
    dt = time.time() - t0
    print(f"Singular n=7 finished in {dt:.1f}s (exit {proc.returncode})")
    for line in proc.stdout.splitlines():
        if line.startswith("KRULLDIM") or line.startswith("VDIM"):
            print(line)
    if proc.stderr:
        print("STDERR:", proc.stderr[-800:])
except subprocess.TimeoutExpired:
    dt = time.time() - t0
    print(f"Singular n=7 EXCEEDED {WALL_CAP}s wall cap ({dt:.1f}s elapsed) "
          "-- measured boundary of the vdim route at n=7")
finally:
    os.unlink(path)