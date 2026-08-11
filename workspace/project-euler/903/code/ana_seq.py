from sympy import factorial, Rational, Integer, factorint, ntheory

A = {2:1, 3:10, 4:184, 5:5052, 6:191232, 7:9851040, 8:650626560,
     9:54052427520, 10:5514150297600, 11:680309947699200}
# B keyed by n (n>=3)
B = {3:1, 4:0, 5:-108, 6:-3600, 7:-208800, 8:-12418560,
     9:-932601600, 10:-85305830400, 11:-9900701798400}

print("=== A_n / A_{n-1} ===")
for n in range(3,12):
    print(n, Rational(A[n], A[n-1]))

print("\n=== A_n / (n-1)! ===")
for n in range(2,12):
    print(n, Rational(A[n], factorial(n-1)))

print("\n=== A_n / n! ===")
for n in range(2,12):
    print(n, Rational(A[n], factorial(n)))

print("\n=== A_n / (n-2)! ===")
for n in range(2,12):
    print(n, Rational(A[n], factorial(n-2)))

print("\n=== B_n / B_{n-1} (n>=5) ===")
for n in range(5,12):
    print(n, Rational(B[n], B[n-1]))

print("\n=== |B_n| / (n-1)! ===")
for n in range(3,12):
    print(n, Rational(abs(B[n]), factorial(n-1)))

print("\n=== |B_n| / (n-2)! ===")
for n in range(3,12):
    print(n, Rational(abs(B[n]), factorial(n-2)))

print("\n=== |B_n| / (n-3)! ===")
for n in range(3,12):
    print(n, Rational(abs(B[n]), factorial(n-3)))

print("\n=== A_n/(n-1)! * something ===")
# c_n = |B|/(n-1)! is integer for n>=6: 30,290,2464,23130,235080,2728368
c = {6:30,7:290,8:2464,9:23130,10:235080,11:2728368}
print("\n=== c_n ratios c_n/c_{n-1} ===")
for n in range(7,12):
    print(n, Rational(c[n], c[n-1]))

print("\n=== prime factorizations of A_n ===")
for n in range(2,12):
    print(n, factorint(A[n]))

print("\n=== prime factorizations of |B_n| ===")
for n in range(3,12):
    print(n, factorint(abs(B[n])))
