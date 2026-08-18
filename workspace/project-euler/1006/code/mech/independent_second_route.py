"""Independent exact check: cyclic-window second moment plus prefix subtraction.

For q of Fibonacci length N>k, take doubled q q and windows r=0..N-1.
The k+1 factors are r=N-k-1,...,N-1.  This artifact checks that identity
and computes the same sum using a cyclic rolling recurrence, independently of
mechanical intercepts and universal-Euclidean floor moments.
"""
import sys
sys.set_int_max_str_digits(0)
from lib.fibword import fib_prefix, fibs_upto, next_fib
from mech.mech_psi import mech_psi, M

def cyclic_route(k):
    N = next_fib(k, fibs_upto(k+1))
    q = fib_prefix(N)
    qq = q + q
    tenk = 10**k
    vals=[]
    v=int(qq[:k])
    for r in range(N):
        vals.append(v)
        v=10*v-int(qq[r])*tenk+int(qq[r+k])
    # The position theorem gives the terminal windows in first-occurrence
    # order, but for small N the doubled prefix can expose a repeated terminal
    # window; retain distinct strings exactly as the definition requires.
    chosen = {}
    for r in range(N-k-1,N):
        chosen[qq[r:r+k]] = vals[r]
    return sum(v*v for v in chosen.values()) % M, len(chosen)

def main():
    for k in range(1,151):
        got,c=cyclic_route(k)
        want=mech_psi(k)[0] % M
        assert c==k+1 and got==want,(k,got,want,c)
    print('CYCLIC POSITION ROUTE vs mechanical: PASS k=1..150')
    for k in (3,10):
        got,c=cyclic_route(k)
        print(f'Psi({k})={got}, count={c}')

if __name__=='__main__': main()
