"""Runs check_binomial_approach in-process; capture with timeout+tee."""

import sys, os
sys.path.insert(0, "/workspace/code")
os.chdir("/workspace")
ns = {}
code = open("code/out/check_binomial_approach.py", encoding="utf-8").read()
head = code.split('if __name__')[0]
exec(compile(head, "check", "exec"), ns)
witnesses = ns['witnesses']; validate = ns['validate']

witnesses()
print("\n=== validating the reformulation on every n up to 60 ===")
all_ok = True
for n in range(0, 61):
    a, b, lu, got, exact = validate(n)
    ok = a and b and lu
    all_ok &= ok
    flag = "OK " if ok else "FAIL"
    print(f"n={n:3d} reform(A)={a} carry==digits(B)={b} lucas={lu} [{flag}] "
          f"low_digits(of 2^n)={exact}")
print("\nALL OK" if all_ok else "\nSOME FAILED")
