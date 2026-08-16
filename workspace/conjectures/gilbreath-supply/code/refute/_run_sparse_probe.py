import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from refute.sparse_fixed_probe import *

if __name__ == "__main__":
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 2048
    for n, make in [(16, make_pow2), (32, make_squares)]:
        h = make(n)
        assert s_sos(n, h) == s_direct(n, h), (n,)
    print("s_sos == s_direct cross-check passed on small n.")
    family_ratio(N, make_pow2, "fixed: ones at powers of 2")
    family_ratio(N, make_squares, "fixed: ones at squares", step=64)
    family_ratio(N, make_triangular, "fixed: ones at triangular numbers", step=64)
