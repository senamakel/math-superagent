import subprocess, shutil

print("=== which ===")
for name in ["geng","nauty-geng","gentourng","python3","pysat"]:
    print(name, "->", shutil.which(name))
print("=== pysat import ===")
try:
    from pysat.solvers import Cadical153
    print("Cadical153 import OK")
except Exception as e:
    print("Cadical import err:", e)
