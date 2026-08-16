#!/usr/bin/env python3
"""Run the K* brute-force check n=3..14 and write a capture."""
import sys
sys.path.insert(0, "/workspace/code")
import importlib.util
spec = importlib.util.spec_from_file_location("k3", "/workspace/code/refute/kstar_check3.py")
