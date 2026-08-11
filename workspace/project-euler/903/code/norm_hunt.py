import sympy as sp

A = {2:1, 3:10, 4:184, 5:5052, 6:191232, 7:9851040, 8:650626560,
     9:54052427520, 10:5514150297600, 11:680309947699200}
B = {3:1, 4:0, 5:-108, 6:-3600, 7:-208800, 8:-12418560,
     9:-932601600, 10:-85305830400, 11:-9900701798400}

def H(n):
    if n<=0: return sp.Integer(0)
    return sum(sp.Integer(1,1) if False else sp.Rational(1,k) for k in range(1,n+1))

def fac(n):
    return sp.factorial(n)

def check(name, vals):
    # all must be equal
    c = vals[0]
    for v in vals[1:]:
        if v != c:
            return False
    return True

def report(title, fn, ns, exact_int=True):
    vals = []
    ok = True
    seen = None
    for n in ns:
        v = sp.nsimplify(fn(n))
        vals.append(v)
        if seen is None: seen = v
        elif v != seen: ok = False
    which = "INT" if all(v.is_integer for v in vals) else "RATIO"
    if ok:
        print(f"[EXACT CONST] {title}: = {seen}  ({which}, n={ns})")
    return ok, vals, seen

nsA = [2,3,4,5,6,7,8,9,10,11]
nsB = [3,4,5,6,7,8,9,10,11]

print("="*70)
print("A_n normalizations")
print("="*70)
report("A/(n!)", lambda n: A[n]/fac(n), nsA)
report("A/(n!)^2", lambda n: A[n]/fac(n)**2, nsA)
report("A/(n!(n-1)!)", lambda n: A[n]/(fac(n)*fac(n-1)), nsA)
report("A/(n!(n-1)!(n-2)!)", lambda n: A[n]/(fac(n)*fac(n-1)*fac(n-2)), nsA)
report("A/(n-1)!", lambda n: A[n]/fac(n-1), nsA)
report("A/n!", lambda n: A[n]/fac(n), nsA)
report("A/(n! * n)", lambda n: A[n]/(fac(n)*n), nsA)
# deficit
report("(n!)^2 - 2A", lambda n: fac(n)**2 - 2*A[n], nsA)
report("(n!)^2/2 - A", lambda n: fac(n)**2/2 - A[n], nsA)
report("n!(n-1)! - A", lambda n: fac(n)*fac(n-1) - A[n], nsA)
# deficits normalized
def deficit2(n):
    return fac(n)**2 - 2*A[n]
report("((n!)^2-2A)/n!^2", lambda n: deficit2(n)/fac(n)**2, nsA)
report("((n!)^2-2A)/(n!(n-1)!)", lambda n: deficit2(n)/(fac(n)*fac(n-1)), nsA)
report("((n!)^2-2A)/(n! n)", lambda n: deficit2(n)/(fac(n)*n), nsA)
report("((n!)^2-2A)/(n-1)!", lambda n: deficit2(n)/fac(n-1), nsA)
# (n!)^2/2 - A
def dA(n): return fac(n)**2/2 - A[n]
report("(n!^2/2-A)/(n!(n-1)!)", lambda n: dA(n)/(fac(n)*fac(n-1)), nsA)
report("(n!^2/2-A)/(n! (n-1)!) *n", lambda n: dA(n)/(fac(n)*fac(n-1))*n, nsA)
# A/(n! (n-1)!(n-2)!)
report("A/(n!(n-1)!(n-2)!)", lambda n: A[n]/(fac(n)*fac(n-1)*fac(n-2)), nsA)

print()
print("="*70)
print("B_n normalizations (|B|)")
print("="*70)
report("|B|/(n-1)!", lambda n: abs(B[n])/fac(n-1), nsB)
report("|B|/(n!)", lambda n: abs(B[n])/fac(n), nsB)
report("|B|/(n!(n-1)!)", lambda n: abs(B[n])/(fac(n)*fac(n-1)), nsB)
report("|B|/((n-1)!(n-2)!)", lambda n: abs(B[n])/(fac(n-1)*fac(n-2)), nsB)
report("|B|/(n!(n-1)!(n-2)!)", lambda n: abs(B[n])/(fac(n)*fac(n-1)*fac(n-2)), nsB)
report("|B|/((n-1)! n)", lambda n: abs(B[n])/(fac(n-1)*n), nsB)
