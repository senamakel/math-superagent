# Creates /workspace/code/__init__.py if not present, so `lib` is importable.
import os
base = os.path.dirname(__file__)
init = os.path.join(base, "__init__.py")
if not os.path.exists(init):
    open(init, "w").close()
