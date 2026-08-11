from fractions import Fraction
from math import factorial

A = {2:1, 3:10, 4:184, 5:5052, 6:191232, 7:9851040, 8:650626560,
     9:54052427520, 10:5514150297600, 11:680309947699200}
B = {3:1, 4:0, 5:-108, 6:-3600, 7:-208800, 8:-12418560,
     9:-932601600, 10:-85305830400, 11:-9900701798400}

def show(name, seq):
    print(f"{name}: {', '.join(str(x) for x in seq)}")

# More A normalizations - try dividing out high powers of n!
print("=== A_n more normalizations ===")
show("A/( (n!)^2 / n^2 )", [Fraction(A[n], factorial(n)**2 // (n*n)) for n in sorted(A)])
show("A/( (n-1)! * n! / n )", [Fraction(A[n], factorial(n-1)*factorial(n)//n) for n in sorted(A)])
show("A/( (n-2)! )", [Fraction(A[n], factorial(n-2)) for n in sorted(A) if n>=3 and n in A])
show("A/( (n-1)! / n )", [Fraction(A[n], factorial(n-1)//n) for n in sorted(A)])

# Try harmonic numbers
from fractions import Fraction
def H(n):
    return sum(Fraction(1,k) for k in range(1,n+1))
show("A/(n! * H_n)", [Fraction(A[n], factorial(n)*H(n)) for n in sorted(A)])
show("A/(n!*(n-1)*H)", [Fraction(A[n], factorial(n)*(n-1)*H(n)) for n in sorted(A)])

print()
print("=== c_n = |B|/(n-1)! , integer part look ===")
c = {n: Fraction(abs(B[n]), factorial(n-1)) for n in B}
show("|B|/(n-1)!", [c[n] for n in sorted(c)])
# ratios
show("c_n/c_{n-1}", [Fraction(c[n].numerator*c[n-1].denominator, c[n].denominator*c[n-1].numerator) for n in sorted(c) if n-1 in c])

print()
print("=== A in terms of (n-1)! * int (check) ===")
# ratio A_n / (n-1)! ~ roughly
show("A/(n-1)! (decimal)", [float(A[n])/factorial(n-1) for n in sorted(A)])
# multiply A/(n-1)! by (n-2) maybe
show("A/(n-1)! * (n-2)", [Fraction(A[n]*(n-2), factorial(n-1)) for n in sorted(A) if n>=3 in A] if 0 else [A[n]*(n-2)/factorial(n-1) for n in sorted(A) if n in A])
