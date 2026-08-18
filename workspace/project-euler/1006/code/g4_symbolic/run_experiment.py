#!/usr/bin/env python3
"""Run the G4 cylinder-module experiment; importable from /workspace/code on PYTHONPATH."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from g4_symbolic.test_module import main
main()
