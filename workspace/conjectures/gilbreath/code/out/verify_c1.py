from lib.gilbreath import primes_up_to, rows_generator

# Copy of verify_three.py so we can run it directly.
primes = primes_up_to(200000)
rows = list(rows_generator(primes, 160))
A1 = rows[1]

def block_profile(row):
    L = 0
    for x in row[1:]:
        if x in (0, 2):
            L += 1
        else:
            break
    return L

viol = 0; checked = 0
for k in range(2, 160):
    row = rows[k]
    for i in range(1, len(row)):
        lo = i - 1; hi = lo + (k - 1)
        if hi >= len(A1): break
        w = A1[lo:hi + 1]
        R = max(w) - min(w)
        checked += 1
        if row[i] > R:
            viol += 1
print(f"C1 all-cells (d160): checked={checked} violations={viol}")
