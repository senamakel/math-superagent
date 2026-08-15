from math import ceil
A = 1504170715041707
M = 4503599627370517

# Recurrence coins (values and indices), same as before
coins = [(1, A)]
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

rec_idx = [n for n, _ in coins]
rec_val = [c for _, c in coins]
S = sum(rec_val)
print("recurrence coin count:", len(coins), "sum:", S)

# Independent route 1: forward prefix-min scan up to LIMIT, compare found coins
LIMIT = 7_000_000  # covers first 13 recurrence coins (largest idx 6755007)
run_min = None
fwd = []
n = 1
c = A % M
run_min = c
fwd.append((1, c))
n = 2
prev_coin_idx = 0
k = 1  # which recurrence coin we expect next
mismatch = None
while n <= LIMIT:
    c = (A * n) % M
    if c < run_min:
        run_min = c
        fwd.append((n, c))
        # check against recurrence
        if k < len(rec_idx):
            if n != rec_idx[k] or c != rec_val[k]:
                mismatch = (n, c, rec_idx[k], rec_val[k], k)
                break
            k += 1
    n += 1

print("brute scan to n =", LIMIT, "found coins:")
for t in fwd:
    print("   ", t)
print("recurrence coins in [1, LIMIT]:", list(zip(rec_idx[:k+1], rec_val[:k+1])) if k < len(rec_idx) else rec_idx)
print("mismatch:", mismatch)
if mismatch is None:
    # confirm every coin with index <= LIMIT is accounted for (k reached them)
    expected = sum(1 for idx in rec_idx if idx <= LIMIT)
    print("brute coins found:", len(fwd), "expected (recurrence idx<=LIMIT):", expected)
    print("forward scan MATCHES recurrence through n =", LIMIT)
else:
    print("MISMATCH at", mismatch)
