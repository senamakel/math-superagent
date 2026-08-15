"""Refutation probe: within the fixed-base family 3^x - 2^y = 1, how many
representations c=1 has, and how many total solutions of 3^x - 2^y = c exist.

Claim pillai-falsifier-c1-boundary asserts: c=1 has exactly two representations
(x,y)=(1,1) and (2,3). Also the table asserts various (N,c) two/three-solution
equations. Check by exact integer arithmetic.
"""
def solutions_c(c, xmax, ymax):
    sols = []
    for x in range(1, xmax + 1):
        for y in range(1, ymax + 1):
            if 3**x - 2**y == c:
                sols.append((x, y))
    return sols

# c=1 family
print("3^x - 2^y = 1, x,y <= 8:", solutions_c(1, 8, 8))
print("3^x - 2^y = 1, x,y <= 15:", solutions_c(1, 15, 15))

# The (N,c) exceptional equations from the table
cases = [
    ((3,2),1),  # the base family c=1  (table row (2,1) is the base pair (3,2), c=1)
]
# rows: (2,5): 3^2-2^2=5, 2^3-3=5, 2^5-3^3=5
print("2^a - 3^b = 5 over a,b<=10:", [(a,b) for a in range(1,11) for b in range(1,11) if 2**a - 3**b == 5])
print("3^a - 2^b = 5 over a,b<=10:", [(a,b) for a in range(1,11) for b in range(1,11) if 3**a - 2**b == 5])
print("3^a - 2^b = 7 over a,b<=10:", [(a,b) for a in range(1,11) for b in range(1,11) if 3**a - 2**b == 7])
print("2^a - 3^b = 7 over a,b<=10:", [(a,b) for a in range(1,11) for b in range(1,11) if 2**a - 3**b == 7])
print("2^a - 3^b = 13 over a,b<=12:", [(a,b) for a in range(1,13) for b in range(1,13) if 2**a - 3**b == 13])
print("2^a - 3^b = 23 over a,b<=12:", [(a,b) for a in range(1,13) for b in range(1,13) if 2**a - 3**b == 23])
print("3^a - 2^b = 23 over a,b<=12:", [(a,b) for a in range(1,13) for b in range(1,13) if 3**a - 2**b == 23])
