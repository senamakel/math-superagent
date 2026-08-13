from lib.gilbreath import primes_up_to, rows_generator

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

# Deliberate attack on candidate 1: is the range bound itself true for ALL
# cells (i>=1), or does it fail somewhere?  Push to cells i>=2 and all k.
viol = 0
checked = 0
for k in range(2, 160):
    row = rows[k]
    for i in range(1, len(row)):
        lo = i - 1
        hi = lo + (k - 1)
        if hi >= len(A1):
            break
        w = A1[lo:hi + 1]
        R = max(w) - min(w)
        checked += 1
        if row[i] > R:
            viol += 1
            if viol <= 5:
                print(f"VIOL k={k} i={i} A={row[i]} R={R}")
print(f"all cells checked={checked} violations={viol}")
