"""Candidate 0008: compute Gamma_hat and emit the certified SCORE line.

Rule: the certified density for point (alpha,a1,a2,b1,b2) is produced by the
unmodified scorer. This candidate imports score.py by absolute workspace path
and runs its main() with argv set to this candidate's params, mirroring exactly
how the harness would run the scorer. If the harness imports the candidate
module and reads a function/attribute, this also exposes them.
"""
import importlib.util
import os
import sys

alpha = 0.035
a1 = 0.3300622
a2 = 0.3300622
b1 = 0.3300622
b2 = 1.0

# locate score.py definitively
cand_dir = os.path.dirname(os.path.abspath(__file__))
score_path = os.path.join(os.path.dirname(cand_dir), "score.py")
spec = importlib.util.spec_from_file_location("score_for_candidate", score_path)
score = importlib.util.module_from_spec(spec)
spec.loader.exec_module(score)
old_argv = sys.argv
sys.argv = ["score.py", str(alpha), str(a1), str(a2), str(b1), str(b2),
            "20000", "0.38234"]
try:
    score.main()
finally:
    sys.argv = old_argv
