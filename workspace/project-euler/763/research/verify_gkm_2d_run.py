# Independent run of the 2D CGMO/Zhen-Knessl G(k,m) recurrence, from the
# verbatim equations in the notes, to confirm the indexing convention.
import sys
sys.setrecursionlimit(100000)

def G(k, m, memo):
    key = (k, m)
    if key in memo:
        return memo[key]
    if k < 1:
        r = 0
    elif m == 0:
        r = 2*G(k-1, 0, memo) + G(k, 1, memo) + (1 if k == 2 else 0)
    elif m == 1:
        r = G(k-3, 0, memo) + 2*G(k-2, 1, memo) + G(k-1, 2, memo) + G(k-4, 1, memo)
    else:  # m >= 2
        r = G(k-m-2, m-1, memo) + 2*G(k-m-1, m, memo) + G(k-m, m+1, memo)
    memo[key] = r
    return r

def a(n):
    return 1 if n == 1 else G(n, 0, {})

expected = [1,1,2,4,9,20,46,105,243,561,1301,3014,6995,16227,37668,
            87426,202961,471150,1093819,2539348,5895408,13686805]
got = [a(n) for n in range(1, 23)]
print("a(1..22) =", got)
print("matches OEIS A007902 first 22:", got == expected)

# Sanity: the run's 2D amoeba D2D(N) = configs after N divisions = N+1 pebbles
# = a(N+1).
print("D2D(N)=a(N+1):", {N: a(N+1) for N in range(0, 8)})
