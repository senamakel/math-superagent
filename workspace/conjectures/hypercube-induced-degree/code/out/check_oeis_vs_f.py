"""Check whether any of the four fetched OEIS sequences matches f(n).

f(n) = min{ D(S) : S subset of {0,1}^n, |S|=2^{n-1}+1 } (max internal degree).
Established exact values in this run: f(1..5) = 1,2,2,2,3 = ceil(sqrt(n)).

The four sequences fetched by lookup:
  A002264 = floor(n/3)            (nonneg integers repeated 3x)
  A003056 = floor((sqrt(1+8n)-1)/2)  (inverse triangular; n appears n+1 times)
  A053251 = 3rd-order mock theta psi(q) coefficients (partitions)
  A202453 = Fibonacci self-fusion matrix entries

Verdict target: does any of them equal f(n) (or ceil(sqrt(n))) on a range?
"""
import math

def f_exact_range(n_max):
    return [math.ceil(math.sqrt(n)) for n in range(1, n_max+1)]

def a002264(n):
    return n // 3

def a003056(n):
    return (math.isqrt(1 + 8*n) - 1) // 2

def a053251_terms(N):
    # generating function from note: psi(q) = sum_{n>=1} q^(n^2)/prod(1-q^(2i-1))
    # recurrence b(n,i): partitions of n with 0<d1/1<d2/2<...
    from functools import lru_cache
    @lru_cache(maxsize=None)
    def b(n, i):
        s = i*(i+1)//2
        if n > s: return 0
        if n == s: return 1
        return b(n, i-1) + b(n-i, min(n-i, i-1))
    res = [0]
    for n in range(1, N+1):
        res.append(sum(b(j, min(j, n-2*j-1)) for j in range(0, n//2 + 1)))
    return res  # res[n] = a(n)

def a202453(n, k):
    # F(n,k) = F(n)*F(k+1) if k even, F(n+1)*F(k) if k odd
    F = [0,1]
    for _ in range(2, n+k+3):
        F.append(F[-1]+F[-2])
    return F[n]*F[k+1] if k % 2 == 0 else F[n+1]*F[k]

f = f_exact_range(20)
print("f(1..20) (=ceil(sqrt n)):", f)

ok_264 = all(a002264(n) == f[n-1] for n in range(1, 21))
ok_056 = all(a003056(n) == f[n-1] for n in range(1, 21))
a53 = a053251_terms(20)
ok_531 = all(a53[n] == f[n-1] for n in range(1, 21))
# A202453 is a 2-D array; antidiagonal read is the 'sequence'. Check if any
# antidiagonal sum or entry happens to match -- just report it is 2-D.
print("A002264 == f on 1..20?", ok_264)
print("A003056 == f on 1..20?", ok_056)
print("A053251 == f on 1..20?", ok_531, "  a053[1..5] =", a53[1:6])
print("A202453 is 2-D (entries F(n,k)); not a 1-D sequence indexable against f.")
