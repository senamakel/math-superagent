import subprocess, shutil, sys, os
print("python", sys.version)
print("PYTHONPATH:", os.environ.get("PYTHONPATH"))
print("cwd:", os.getcwd())
print("=== which geng/nauty ===")
for name in ["geng","nauty-geng"]:
    print(name, "->", shutil.which(name))
print("=== lib import ===")
try:
    from lib.satcolor import is_k_colorable
    print("lib.satcolor import OK")
except Exception as e:
    print("lib.satcolor err:", repr(e))
