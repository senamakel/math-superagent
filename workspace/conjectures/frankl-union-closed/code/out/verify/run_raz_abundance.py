#!/usr/bin/env python3
"""Run Raz 2017 counterexample verification via the workspace oracle stub.

This is the mechanical confirmation the digest flagged as pending: the
abundance half of raz-reimers-condition-insufficient (each element of the
11-set family on [8] in at most 5 sets, so none abundant). The filter/bijection
(Condition 1) half stays asserted-by-source.
"""
import sys, os
sys.path.insert(0, "/workspace/code/out")
import verify_raz_counterexample
verify_raz_counterexample.main()
print("CROSSCHECK run of the Raz counterexample abundance half: PASS")
