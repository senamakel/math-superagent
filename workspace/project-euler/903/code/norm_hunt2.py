import sympy as sp

A = {2:1, 3:10, 4:184, 5:5052, 6:191232, 7:9851040, 8:650626560,
     9:54052427520, 10:5514150297600, 11:680309947699200}
B = {3:1, 4:0, 5:-108, 6:-3600, 7:-208800, 8:-12418560,
     9:-932601600, 10:-85305830400, 11:-9900701798400}

def H(n):
    return sum(sp.Rational(1,k) for k in range(1,n+1))

def fac(n):
    return sp.factorial(n)

nsA=[2,3,4,5,6,7,8,9,10,11]
nsB=[3,4,5,6,7,8,9,10,11]

def show(title, fn, ns):
    vals=[sp.nsimplify(fn(n)) for n in ns]
    print(f"\n{title}")
    for n,v in zip(ns,vals):
        print(f"   n={n}: {v}")
    # constant?
    if len(set(vals))==1:
        print(f"   ** CONSTANT = {vals[0]}")
    # all integers?
    if all(v.is_integer for v in vals):
        print(f"   --> ALL INTEGERS: {[int(v) for v in vals]}")

# A normalizations
show("A/n!", lambda n:A[n]/fac(n), nsA)
show("A/(n-1)!", lambda n:A[n]/fac(n-1), nsA)
show("A/(n!(n-1)!)", lambda n:A[n]/(fac(n)*fac(n-1)), nsA)
show("A/((n-1)!(n-2)!)", lambda n:A[n]/(fac(n-1)*fac(n-2)), nsA)
show("A/(n!(n-1)!(n-2)!)", lambda n:A[n]/(fac(n)*fac(n-1)*fac(n-2)), nsA)
show("A/( (n-1)!^2 )", lambda n:A[n]/fac(n-1)**2, nsA)
show("A/(n!(n-2)!)", lambda n:A[n]/(fac(n)*fac(n-2)), nsA)

# deficits
show("(n!)^2 - 2A", lambda n:fac(n)**2-2*A[n], nsA)
show("(n!)^2/2 - A", lambda n:fac(n)**2/2-A[n], nsA)
show("((n!)^2-2A)/n!^2", lambda n:(fac(n)**2-2*A[n])/fac(n)**2, nsA)
show("((n!)^2-2A)/(n!(n-1)!)", lambda n:(fac(n)**2-2*A[n])/(fac(n)*fac(n-1)), nsA)
show("((n!)^2-2A)/(n!*n)", lambda n:(fac(n)**2-2*A[n])/(fac(n)*n), nsA)
show("((n!)^2-2A)/((n-1)!(n-2)!)", lambda n:(fac(n)**2-2*A[n])/(fac(n-1)*fac(n-2)), nsA)
show("((n!)^2/2-A)/(n!(n-1)!)", lambda n:(fac(n)**2/2-A[n])/(fac(n)*fac(n-1)), nsA)
show("((n!)^2/2-A)/(n! (n-1)! n)", lambda n:(fac(n)**2/2-A[n])/(fac(n)*fac(n-1)*n), nsA)
show("n!(n-1)! - A, /n!(n-1)!", lambda n:(fac(n)*fac(n-1)-A[n])/(fac(n)*fac(n-1)), nsA)

# B normalizations
show("|B|/(n-1)!", lambda n:abs(B[n])/fac(n-1), nsB)
show("|B|/n!", lambda n:abs(B[n])/fac(n), nsB)
show("|B|/(n!(n-1)!)", lambda n:abs(B[n])/(fac(n)*fac(n-1)), nsB)
show("|B|/((n-1)!(n-2)!)", lambda n:abs(B[n])/(fac(n-1)*fac(n-2)), nsB)
show("|B|/((n-1)! * n)", lambda n:abs(B[n])/(fac(n-1)*n), nsB)
show("|B|/(n!(n-2)!)", lambda n:abs(B[n])/(fac(n)*fac(n-2)), nsB)
show("|B|/(n! (n-1)!)", lambda n:abs(B[n])/(fac(n)*fac(n-1)), nsB)
