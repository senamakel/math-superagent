"""Facts 1-5 only (cheap): family closed forms, order-3 LRR, diff=Fibonacci, ratio."""
import math

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

N = 12
ns, ks = [], []
for i in range(1, N+1):
    ns.append(fib(2*i+2)*fib(2*i+3) - 1)
    ks.append(fib(2*i)*fib(2*i+3) - 1)

print("==== Fact 2: n_i == F(2i)F(2i+1)-1 (A089508) ====")
print(all(ns[i-1] == fib(2*i)*fib(2*i+1)-1 for i in range(1, N+1)))

print("==== Fact 3: order-3 LRR n_i=8n_{i-1}-8n_{i-2}+n_{i-3} ====")
print("n:", all(ns[i-1]-8*ns[i-2]+8*ns[i-3]-ns[i-4] == 0 for i in range(4, N+1)))
print("k:", all(ks[i-1]-8*ks[i-2]+8*ks[i-3]-ks[i-4] == 0 for i in range(4, N+1)))

print("==== Fact 4: n diffs == F(4i+7) (A033891/A172968) ====")
for i in range(1, N):
    d = ns[i]-ns[i-1]
    print("i=%d diff=%d F(4i+7)=%d match=%s" % (i, d, fib(4*i+7), d == fib(4*i+7)))

print("==== Fact 5: ratio n_{i+1}/n_i ====")
for i in range(1, N):
    print("i=%d: %.6f" % (i, ns[i]/ns[i-1]))
print("phi^4 =", ((1+math.sqrt(5))/2)**4)

print("==== Fact 1 sanity: identity C(n+1,k+1)=C(n,k+2) i=1..5 ====")
for i in range(1,6):
    n,k = ns[i-1], ks[i-1]
    print("i=%d" % i, math.comb(n+1,k+1) == math.comb(n,k+2))
