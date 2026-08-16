#!/usr/bin/env python3
"""Package path: this folder is code/scholar and code/ is on PYTHONPATH.
Purely a launcher so subprocess inherits the environment."""
from lib.supply_fold import s_sos
print("lib import OK", s_sos(10, [0,1,1,0,0,1,0,1,1,0])[0])
