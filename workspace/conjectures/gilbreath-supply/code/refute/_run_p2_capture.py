import subprocess
# run the powers-of-two checker via the canonical capture runner
r = subprocess.run(
    ["python3", "-m", "lib.capture",
     "--target", "code/out/refuter_powers_two.txt",
     "--", "python3", "code/refute/powers_two_check.py"],
    cwd="/workspace", capture_output=True, text=True)
print(r.stdout)
print(r.stderr)
