import sympy
from sympy import factorint, factorial, Rational, nsimplify, sympify
from fractions import Fraction

A = {2:1, 3:10, 4:184, 5:5052, 6:191232, 7:9851040, 8:650626560,
     9:54052427520, 10:5514150297600, 11:680309947699200}
B = {3:1, 4:0, 5:-108, 6:-3600, 7:-208800, 8:-12418560, 9:-932601600,
     10:-85305830400, 11:-9900701798400}

print("=== Factorization of A_n ===")
for n in range(2,12):
    print(f"A_{n} = {A[n]} = {factorint(A[n])}")

print("\n=== Factorization of |B_n| ===")
for n in range(3,12):
    print(f"|B_{n}| = {abs(B[n])} = {factorint(abs(B[n]))}")

print("\n=== ratios A_n/A_{n-1} ===")
for n in range(3,12):
    print(f"A_{n}/A_{n-1} = {Fraction(A[n],A[n-1])}")

print("\n=== A_n / (n-1)! and related normalizations ===")
for n in range(2,12):
    print(f"n={n}: A/(n-1)! = {Fraction(A[n], factorial(n-1))}   A/(n!)^2 = {Fraction(A[n], factorial(n)**2)}   A/n! = {Fraction(A[n],factorial(n))}")

print("\n=== |B_n|/(n-1)! ===")
for n in range(3,12):
    print(f"n={n}: |B|/(n-1)! = {Fraction(abs(B[n]), factorial(n-1))}")

print("\n=== |B_n|/n! ===")
for n in range(3,12):
    print(f"n={n}: |B|/n! = {Fraction(abs(B[n]), factorial(n))}  |B|/(n!)^2={Fraction(abs(B[n]),factorial(n)**2)}")
