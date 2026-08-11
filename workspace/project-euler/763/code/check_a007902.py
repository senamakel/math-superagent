from functools import lru_cache

@lru_cache(maxsize=None)
def G(k, m):
    if k < 1:
        return 0
    if m == 0:
        return 2*G(k-1,0) + G(k,1) + (1 if k==2 else 0)
    if m == 1:
        return G(k-3,0) + 2*G(k-2,1) + G(k-1,2) + G(k-4,1)
    # m >= 2
    return G(k-m-2, m-1) + 2*G(k-m-1, m) + G(k-m, m+1)

def a(n):
    if n == 1:
        return 1
    return G(n, 0)

expected = [1,1,2,4,9,20,46,105,243,561,1301,3014,6995,16227,37668]
got = [a(n) for n in range(1, 16)]
print("recurrence:  ", got)
print("expected(N+1):", expected)
print("MATCH" if got == expected else "MISMATCH")
