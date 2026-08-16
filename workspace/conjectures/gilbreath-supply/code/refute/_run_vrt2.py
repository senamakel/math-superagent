import os, sys
sys.path.insert(0, "/workspace/code")
os.chdir("/workspace/code")
import importlib.util
spec = importlib.util.spec_from_file_location("vrt", "/workspace/code/refute/verify_run_telescope.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)
m.main()
