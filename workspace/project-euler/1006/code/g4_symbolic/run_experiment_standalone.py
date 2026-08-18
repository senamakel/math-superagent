#!/usr/bin/env python3
"""Oracle/obstruction test for the G4 cylinder-observable module.

Exact rational arithmetic on Fibonacci approximants of alpha=1/phi^2.
For each k it builds the cylinder partition cut by {-j alpha: 0<=j<=k},
computes on each atom the digit tuple, decimal value v, and v^2, and reports
the rank (over a prime) of the accumulated (digits, v, v^2) vectors.  Rank
growth is a falsification diagnostic for a fixed-dimensional closure; it is
not a proof and not a full-size algorithm.

Usage:  python3 code/g4_symbolic/run_experiment_standalone.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from g4_symbolic.test_module import main
main()
