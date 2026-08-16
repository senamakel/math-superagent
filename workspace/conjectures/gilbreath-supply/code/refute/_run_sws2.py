import os, sys, subprocess
sys.path.insert(0, "/workspace/code")
# run the search directly by importing and executing its main
import importlib.util
spec = importlib.util.spec_from_file_location("sws", "/workspace/code/refute/sparse_witness_search.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
m.main()
