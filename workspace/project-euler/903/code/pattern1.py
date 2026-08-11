import sympy as sp

A = {2:1, 3:10, 4:184, 5:5052, 6:191232, 7:9851040, 8:650626560, 9:54052427520, 10:5514150297600, 11:680309947699200}
B = {3:1, 4:0, 5:-108, 6:-3600, 7:-208800, 8:-12418560, 9:-932601600, 10:-85305830400, 11:-9900701798400}

print("=== A_n factorizations ===")
for n in range(2,12):
    print(n, sp.factorint(A[n]))

print("\n=== B_n factorizations (abs) ===")
for n in range(3,12):
    print(n, sp.factorint(abs(B[n])))

print("\n=== ratios A_n/A_{n-1} ===")
for n in range(3,12):
    print(n, sp.Rational(A[n], A[n-1]))

print("\n=== A_n / (n-1)! ===")
for n in range(2,12):
    print(n, sp.Rational(A[n], sp.factorial(n-1)))

print("\n=== A_n / n! ===")
for n in range(2,12):
    print(n, sp.Rational(A[n], sp.factorial(n)))

print("\n=== |B_n| / (n-1)! ===")
for n in range(3,12):
    print(n, sp.Rational(abs(B[n]), sp.factorial(n-1)))

print("\n=== |B_n| / n! ===")
for n in range(3,12):
    print(n, sp.Rational(abs(B[n]), sp.factorial(n)))
