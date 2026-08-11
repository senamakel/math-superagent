import itertools
from math import factorial

def rank0(p):
    """0-based lexicographic rank of permutation tuple p (Lehmer code sum)."""
    n = len(p)
    r = 0
    for i in range(n):
        c = sum(1 for j in range(i+1, n) if p[j] < p[i])  # Lehmer digit
        r += c * factorial(n-1-i)
    return r

def r1(p):
    return rank0(p) + 1

def apply_power(p, i, n):
    """p^i as one-line tuple."""
    cur = list(range(1, n+1))
    # represent p acting on positions? use value notation: apply p to each symbol
    for _ in range(i):
        cur = [p[x-1] for x in cur]
    return tuple(cur)

def order(p):
    i = 1
    while apply_power(p, i, len(p)) != tuple(range(1, len(p)+1)):
        i += 1
    return i

def Q(n):
    total = 0
    perms = list(itertools.permutations(range(1, n+1)))
    for p in perms:
        for i in range(1, factorial(n)+1):
            total += r1(apply_power(p, i, n))
    return total

# item 4 check: sum of 1-based ranks over all perms
for n in range(1, 6):
    perms = list(itertools.permutations(range(1, n+1)))
    s = sum(r1(p) for p in perms)
    nf = factorial(n)
    print(f"n={n}: sum ranks = {s}, n!(n!+1)/2 = {nf*(nf+1)//2}, match={s==nf*(nf+1)//2}")

print("rank(2,1,3) =", r1((2,1,3)))  # expect 3
print("Q(2) =", Q(2))  # expect 5
print("Q(3) =", Q(3))  # expect 88
print("Q(5) =", Q(5))  # brute reachable
