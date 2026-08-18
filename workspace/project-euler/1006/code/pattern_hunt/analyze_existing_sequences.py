from pathlib import Path
import sympy as sp

ROOT=Path('code/out')

def pairs(name):
    out=[]
    for line in (ROOT/name).read_text().splitlines():
        z=line.split()
        if len(z)>=2:
            try: out.append((int(z[0]),int(z[1])))
            except ValueError: pass
    return out

def seq(name): return [v for _,v in pairs(name)]

def first_bad(pred, vals):
    for i,x in enumerate(vals):
        if not pred(i,x): return i+1,x
    return None

def report(name):
    ps=pairs(name); a=[v for _,v in ps]
    print(name, 'terms=',len(a), 'indices=', (ps[0][0],ps[-1][0]) if ps else None)
    if name=='counts.txt':
        print('count=k+1:', all(k==v-1 for k,v in ps))
    if name=='c1_terms.txt':
        # exact floor(k/phi^2) without floating point: floor(k*(3-sqrt5)/2)
        bad=[]
        for k,v in ps:
            # floor(k*(3-sqrt5)/2) = floor((3k-ceil(k sqrt5))/2), use integer sqrt bounds
            # sympy exact floor
            e=1+int(sp.floor(sp.Rational(k,2)*(3-sp.sqrt(5))))
            if v!=e: bad.append((k,v,e)); break
        print('c1=1+floor(k/phi^2):', not bad, 'first_bad=',bad[:1])
    if name=='lmin.txt':
        # next Fibonacci strictly > k, F1=1,F2=1
        f=[1,1]
        while f[-1]<=max((k for k,_ in ps),default=0): f.append(f[-1]+f[-2])
        bad=[]
        for k,v in ps:
            nxt=next(x for x in f if x>k)
            e=k+nxt-1
            if v!=e: bad.append((k,v,e)); break
        print('Lmin=k+NextFib_strict(k)-1:',not bad,'first_bad=',bad[:1])
    if len(a)>=5:
        for order in range(1,min(12,len(a)//2)+1):
            try:
                rec=sp.polys.ring_series.find_simple_recurrence(a, n=order)
            except Exception: rec=None
            if rec not in (None,[],[0]*order):
                print('simple_recurrence_order',order,rec)
                break

for n in ['psi_exact.txt','psi_residues.txt','c1_terms.txt','counts.txt','lmin.txt','ext_recurrence.txt']:
    report(n)

# exact recurrence checks explicitly suggested by existing output
p=seq('psi_exact.txt')
print('psi_exact linear recurrence orders 1..10:')
for d in range(1,11):
    try: r=sp.polys.ring_series.find_simple_recurrence(p,n=d)
    except Exception: r=None
    if r not in (None,[],[0]*d): print(d,r)

# inspect ext file raw numeric rows
print('ext_recurrence first/last lines:')
print('\n'.join((ROOT/'ext_recurrence.txt').read_text().splitlines()[:8]))
print('\n'.join((ROOT/'ext_recurrence.txt').read_text().splitlines()[-5:]))
