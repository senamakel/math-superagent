import subprocess, sys
sys.exit(subprocess.call([sys.executable, "code/refute/verify_delta_ladder.py"], cwd="/workspace"))
