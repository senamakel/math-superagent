from math import factorial
from fractions import Fraction

A = {2:1, 3:10, 4:184, 5:5052, 6:191232, 7:9851040, 8:650626560,
     9:54052427520, 10:5514150297600, 11:680309947699200}
B = {3:1, 4:0, 5:-108, 6:-3600, 7:-208800, 8:-12418560,
     9:-932601600, 10:-85305830400, 11:-9900701798400}

def show(name, seq):
    print(f"{name}:")
    print("  ", ", ".join(str(x) for x in seq))

# normalize A
print("===== A_n normalizations =====")
for label, f in [
    ("A/(n-1)!", lambda n,a: Fraction(a, factorial(n-1))),
    ("A/n!", lambda n,a: Fraction(a, factorial(n))),
    ("A/(n!(n-1)!)", lambda n,a: Fraction(a, factorial(n)*factorial(n-1))),
    ("A/(n!)^2", lambda n,a: Fraction(a, factorial(n)**2)),
    ("A/(n!*2^n)", lambda n,a: Fraction(a, factorial(n)*(2**n))),
    ("A/((n-1)!^2)", lambda n,a: Fraction(a, factorial(n-1)**2)),
    ("A/(n!*n)", lambda n,a: Fraction(a, factorial(n)*n)),
    ("A/(n!*(n-1))", lambda n,a: Fraction(a, factorial(n)*(n-1))),
]:
    show(label, [f(n,A[n]) for n in sorted(A)])

print()
print("===== B_n normalizations ( |B| ) =====")
for label, f in [
    ("|B|/(n-1)!", lambda n,b: Fraction(abs(b), factorial(n-1))),
    ("|B|/n!", lambda n,b: Fraction(abs(b), factorial(n))),
    ("|B|/(n!(n-1)!)", lambda n,b: Fraction(abs(b), factorial(n)*factorial(n-1))),
    ("|B|/(n!)^2", lambda n,b: Fraction(abs(b), factorial(n)**2)),
    ("|B|/((n-1)!^2)", lambda n,b: Fraction(abs(b), factorial(n-1)**2)),
]:
    show(label, [f(n,B[n]) for n in sorted(B)])

print()
print("===== ratios of consecutive terms =====")
An_ = sorted(A)
show("A_n/A_{n-1}", [Fraction(A[n],A[n-1]) for n in An_ if n-1 in A])
Bn_ = sorted(B)
show("|B_n|/|B_{n-1}|", [Fraction(abs(B[n]),abs(B[n-1])) for n in Bn_ if n-1 in B and B[n-1]!=0])
