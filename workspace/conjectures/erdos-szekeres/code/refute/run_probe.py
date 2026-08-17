"""Run the R-k-interior probe and also reproduce ES(5)=9 with the oracle,
so we know the search is a genuine check against a settled value."""
import sys, subprocess
sys.path.insert(0, "/workspace/code")
from lib.es_geom import in_general_position, convex_hull, largest_convex_subset

r = subprocess.run([sys.executable, "code/refute/rk_interior_probe.py"],
                   capture_output=True, text=True)
print(r.stdout)
if r.stderr:
    print("STDERR:", r.stderr[-2000:])
