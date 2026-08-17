#!/usr/bin/env python3
"""Run the Raz 2017 counterexample verification mechanically.

Verifies the abundance half of raz-reimers-condition-insufficient via
(1) the canonical oracle stub (verify_raz_counterexample) on the direct route,
(2) an independent per-element count from the raw sets, and
(3) a negative control (the family must NOT be union-closed, since it is a
Reimer-condition family, i.e. we are not mistaking it for a UC counterexample).
"""
import sys, os
sys.path.insert(0, "/workspace/code/out")
sys.path.insert(0, "/workspace/code")

import verify_raz_counterexample
import run_raz_crosscheck

print("\nAll three checks completed without assertion failure.")
print("raz-reimers-condition-insufficient (abundance half): verified-mechanically")
print("filter/bijection (Condition 1) half: asserted-by-source (paper appendix)")
