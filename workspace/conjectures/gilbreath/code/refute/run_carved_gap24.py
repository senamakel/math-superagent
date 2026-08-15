import subprocess, sys
print(subprocess.run([sys.executable, "code/refute/search_carved_gap24.py", "16", "14"],
                     capture_output=True, text=True).stdout)
