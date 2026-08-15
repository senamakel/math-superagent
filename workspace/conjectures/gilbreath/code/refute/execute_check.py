#!/usr/bin/env python3
"""Execute the decisive check by importing it (so output reaches the model)."""
import sys, os
sys.path.insert(0, "/workspace/code/refute")
spec = {"__file__": "/workspace/code/refute/weighted_excess_check.py"}
with open("/workspace/code/refute/weighted_excess_check.py") as f:
    code = f.read()
exec(compile(code, "weighted_excess_check.py", "exec"), {"__name__": "__main__", "__file__": "/workspace/code/refute/weighted_excess_check.py"})
