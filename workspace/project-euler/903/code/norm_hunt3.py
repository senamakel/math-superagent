import sympy as sp

A = {2:1, 3:10, 4:184, 5:5052, 6:191232, 7:9851040, 8:650626560,
     9:54052427520, 10:5514150297600, 11:680309947699200}
B = {3:1, 4:0, 5:-108, 6:-3600, 7:-208800, 8:-12418560,
     9:-932601600, 10:-85305830400, 11:-9900701798400}

def fac(n): return sp.factorial(n)
def H(n): return sum(sp.Rational(1,k) for k in range(1,n+1))
def H2(n): return sum(sp.Rational(1,k**2) for k in range(1,n+1))

nsA=[2,3,4,5,6,7,8,9,10,11]
nsB=[6,7,8,9,10,11]

def show(title, fn, ns, hunt_const=False):
    vals=[sp.nsimplify(fn(n)) for n in ns]
    print(f"\n{title}")
    for n,v in zip(ns,vals):
        print(f"   n={n}: {v}")
    if len(set(vals))==1:
        print(f"   ** CONSTANT = {vals[0]}")
    if all(v.is_integer for v in vals):
        print(f"   --> INTEGERS: {[int(v) for v in vals]}")
    return vals

# Deficit D_n = (n!)^2/2 - A
D = {n: fac(n)**2//2 - A[n] for n in nsA}
print("D_n = (n!)^2/2 - A_n:", [D[n] for n in nsA])
show("D/(n!(n-1)!)", lambda n: D[n]/(fac(n)*fac(n-1)), nsA)
show("D/(n!^2)  [=1/2 - A/n!^2]", lambda n: D[n]/fac(n)**2, nsA)
show("D/(n! (n-1)! )*2", lambda n: 2*D[n]/(fac(n)*fac(n-1)), nsA)
show("D/((n-1)!^2)", lambda n: D[n]/fac(n-1)**2, nsA)
show("D/((n-1)!(n-2)!)", lambda n: D[n]/(fac(n-1)*fac(n-2)), nsA)
show("D/(n!(n-1)!) * (n-1)/(n+1)", lambda n: D[n]/(fac(n)*fac(n-1))*(n-1)/(n+1), nsA)
show("D/(n! (n-1)!/n)", lambda n: D[n]/(fac(n)*fac(n-1))*n, nsA)

# harmonic combos on D/(n!(n-1)!) = d
show("H:: d_n vs (H_n/H_{n-1})", lambda n: (D[n]/(fac(n)*fac(n-1))) - H(n)/H(n-1), nsA)
show("d_n - 1/2", lambda n: D[n]/(fac(n)*fac(n-1)) - sp.Rational(1,2), nsA)
# Eulerian-ish: try d_n * n(n-1)
show("d_n * (n(n-1))", lambda n: D[n]/(fac(n)*fac(n-1))*n*(n-1), nsA)
show("d_n * n", lambda n: D[n]/(fac(n)*fac(n-1))*n, nsA)

# c_n = |B|/(n-1)!
c = {n: abs(B[n])/fac(n-1) for n in [3,4,5,6,7,8,9,10,11]}
print("\nc_n=|B|/(n-1)!:", [c[n] for n in [3,4,5,6,7,8,9,10,11]])
show("c_n (n=6..11 only ints)", lambda n: c[n], nsB)
# ratios c_n/c_{n-1}
v=[c[n] for n in [6,7,8,9,10,11]]
print("ratios c_n/c_{n-1}:", [sp.nsimplify(v[i]/v[i-1]) for i in range(1,len(v))])
# normalize c_n further
show("c_n / (n-1)!(n-2)!", lambda n: c[n]/(fac(n-1)*fac(n-2)), nsB)
show("c_n / n!", lambda n: c[n]/fac(n), nsB)
show("c_n / (n-2)!", lambda n: c[n]/fac(n-2), nsB)
show("c_n / (n-3)!", lambda n: c[n]/fac(n-3), nsB)
show("c_n / binom(n,2)", lambda n: c[n]/sp.binomial(n,2), nsB)
show("c_n / (n^2 binom)", lambda n: c[n]/sp.binomial(n,2)/n, nsB)
show("c_n / ((n-1)(n-2)!)", lambda n: c[n]/((n-1)*fac(n-2)), nsB)
# compare deficit and c
print("\nD_n vs c_n (n=6..11):")
for n in nsB:
    print(f"  n={n}: D={D[n]}, c={c[n]}, D/(n! c)= {sp.nsimplify(D[n]/(fac(n)*c[n]))}")
show("D/(n! * c_n)", lambda n: D[n]/(fac(n)*c[n]), nsB, hunt_const=True)
show("(2D/n!^2)/c_n * (n-1)!", lambda n: (2*D[n]/fac(n)**2)/c[n]*fac(n-1), nsB)
