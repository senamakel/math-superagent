"""Small exact experiment for G4's cylinder observable.

For alpha=1/phi^2, a length-k factor is represented by an intercept
interval of the rotation coding. On each atom of the partition cut by
{-j alpha: 0<=j<=k}, the k digits are constant.  We record the decimal
value v and v^2, then test whether Fibonacci induction can preserve a
fixed-dimensional span of the resulting cylinder functions.

This is an oracle/obstruction experiment only; it never runs at the target
10^18.
"""
from fractions import Fraction

# rational Fibonacci convergent to alpha=1/phi^2 = [0;2,1,1,...]
def fib(n):
    a,b=0,1
    for _ in range(n): a,b=b,a+b
    return a

def alpha(n=25):
    # F_n/F_{n+2}; for n>=1, converges to 1/phi^2
    return Fraction(fib(n),fib(n+2))

def atoms(k,a):
    cuts=sorted({Fraction(0),Fraction(1),*[( -j*a)%1 for j in range(k+1)]})
    out=[]
    for l,r in zip(cuts,cuts[1:]):
        x=(l+r)/2
        ds=[(x+(j+1)*a).numerator//(x+(j+1)*a).denominator
            -(x+j*a).numerator//(x+j*a).denominator for j in range(k)]
        v=0
        for d in ds: v=10*v+d
        out.append((l,r,tuple(ds),v,v*v))
    return out

def rank_mod(rows,p=1000003):
    A=[[x%p for x in row] for row in rows]
    m,n=len(A),len(A[0]) if A else 0
    rank=0
    for c in range(n):
        piv=next((i for i in range(rank,m) if A[i][c]),None)
        if piv is None: continue
        A[rank],A[piv]=A[piv],A[rank]
        inv=pow(A[rank][c],p-2,p)
        A[rank]=[(x*inv)%p for x in A[rank]]
        for i in range(m):
            if i!=rank and A[i][c]:
                q=A[i][c]
                A[i]=[(x-q*y)%p for x,y in zip(A[i],A[rank])]
        rank+=1
        if rank==m: break
    return rank

def main():
    a=alpha(30)
    print('alpha=',a)
    for k in range(1,11):
        A=atoms(k,a)
        vals=sorted(v for *_,v,_ in A)
        print(k,len(A),vals[:3],vals[-3:])
    # Test whether the vectors of cylinder observables at successive k
    # have bounded rank after embedding by common prefix coordinates.
    # Rows: factor digits, v, v^2; rank growth is a warning against closure.
    rows=[]
    for k in range(1,18):
        for _,_,ds,v,w in atoms(k,a):
            rows.append(list(ds)+[v,w])
        print('rank through k=',k,'=',rank_mod(rows))

if __name__=='__main__': main()
