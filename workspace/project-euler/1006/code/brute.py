from itertools import product

# Naive exponential oracle.  It constructs S_n until all length-k factors
# stabilize, then computes the requested moment exactly.
def fibonacci_word(n):
    a, b = '0', '01'
    if n == 0: return a
    if n == 1: return b
    for _ in range(2, n + 1):
        a, b = b, b + a
    return b

def factors(k):
    seen = set()
    prev = set()
    n = 0
    while True:
        w = fibonacci_word(n)
        seen |= {w[i:i+k] for i in range(max(0, len(w)-k+1))}
        if seen == prev and len(w) >= 2*k:
            return seen
        prev = set(seen)
        n += 1

def psi(k, mod=None):
    ans = 0
    for x in factors(k):
        ans += int(x) ** 2
    return ans if mod is None else ans % mod

if __name__ == '__main__':
    M = 101001001
    f3 = factors(3)
    print('F3=', sorted(f3))
    print('Psi(3)=', psi(3))
    print('Psi(10) mod M=', psi(10, M))
