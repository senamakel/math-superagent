from math import ceil

A = 1504170715041707
M = 4503599627370517

# n_1 = 1 (value A), n_2 = 3 (value 8912517754604)
coins = [(1, A)]
# find second coin index: smallest n>1 with A*n mod M < A
# given: n=3. Use that.
n1, c1 = 1, A
n2, c2 = 3, (3*A) % M
coins.append((n2, c2))

while True:
    alpha = ceil(c1 / c2)
    n3 = alpha * n2 - n1
    c3 = (A * n3) % M
    coins.append((n3, c3))
    if c3 == 0:
        break
    n1, c1 = n2, c2
    n2, c2 = n3, c3

vals = [c for _, c in coins]
print("number of Eulercoins:", len(coins))
print("indices:", [n for n, _ in coins])
print("values:")
print(vals)
print("sum:", sum(vals))

# inverse indices to match statement example
print("\nfirst two:", vals[0], vals[1], "sum", vals[0]+vals[1])
