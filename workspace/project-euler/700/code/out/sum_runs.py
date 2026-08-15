from math import ceil
A = 1504170715041707
M = 4503599627370517
coins = [(1, A)]
n1, c1 = 1, A
n2, c2 = 3, (3 * A) % M
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
cs = [c for _, c in coins]

# non-overlapping maximal arithmetic runs
i = 0
tot = 0
while i < len(cs):
    if i == len(cs) - 1:
        tot += cs[i]
        break
    d = cs[i + 1] - cs[i]
    j = i + 1
    while j + 1 < len(cs) and cs[j + 1] - cs[j] == d:
        j += 1
    L = j - i + 1
    s = L * (cs[i] + cs[j]) // 2
    tot += s
    i = j + 1
print("non-overlap run total:", tot)
print("direct:", sum(cs))
print("agree:", tot == sum(cs))
