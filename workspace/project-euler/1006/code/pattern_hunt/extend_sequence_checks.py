from pathlib import Path

def read(path):
    return [int(x.split()[1]) for x in Path(path).read_text().splitlines() if x.strip()]

def fibs(n):
    a,b=1,2
    out=[]
    while b<=n:
        out.append(a); a,b=b,a+b
    out.append(a)
    return out

def nextfib(k):
    a,b=1,2
    while a<=k: a,b=b,a+b
    return a

def check_c1():
    a=read('code/out/c1_terms.txt')
    bad=[]
    # exact integer equivalent: alpha=(3-sqrt(5))/2; compare floor via rational square test
    # floor(k*alpha)=m iff m <= k alpha < m+1; use alpha irrational and square inequalities.
    for k,v in enumerate(a,1):
        m=v-1
        # alpha=(3-sqrt5)/2; 2m <= k(3-sqrt5)<2m+2
        # sqrt5 <= 3-2m/k for lower; sqrt5 > 3-2(m+1)/k for upper
        lo=3*k-2*(m+1); hi=3*k-2*m
        if not (lo*lo < 5*k*k < hi*hi): bad.append((k,v,m))
    return len(a),bad[:1]

def check_lmin():
    a=read('code/out/lmin.txt'); bad=[]
    for k,v in enumerate(a,1):
        if v != k+nextfib(k)-1: bad.append((k,v,k+nextfib(k)-1))
    return len(a),bad[:1]

def check_defect():
    a=read('code/out/topelitz_defects.txt')
    fib=[]; x,y=1,2
    while x-1<=len(a): fib.append(x-1); x,y=y,x+y
    zeros=[i+1 for i,v in enumerate(a) if v==0]
    return len(a),zeros,[z for z in zeros if z not in fib]

print('c1',check_c1())
print('lmin',check_lmin())
print('defect',check_defect())
