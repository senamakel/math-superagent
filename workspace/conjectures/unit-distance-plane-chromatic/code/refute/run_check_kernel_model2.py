import sys, os
sys.path.insert(0, "/workspace/code")
# force import from workspace lib
namespace = {}
fpath = "/workspace/code/refute/check_kernel_model.py"
with open(fpath) as f:
    src = f.read()
exec(compile(src, fpath, "exec"), namespace)
